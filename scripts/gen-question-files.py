#!/usr/bin/env python3
"""Generate question files for each subelement from the 2024-2028 Extra pool JSON.

Reads pools/2024-2028/questions.json and outputs one markdown file per
subelement into subelements/, matching the existing study-guide format.
"""

import json
import re
import runpy
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
POOL_PATH = REPO / "pools" / "2024-2028" / "questions.json"
PRESERVED_EXPLANATIONS_PATH = REPO / "scripts" / "new-explanations.py"
OUTPUT_DIR = REPO / "subelements"

# Mapping of subelement IDs to output filenames (stem only)
SUBELEMENT_FILES = {
    "E0": "E0-safety",
    "E1": "E1-commissions-rules",
    "E2": "E2-operating-procedures",
    "E3": "E3-radio-wave-propagation",
    "E4": "E4-amateur-practices",
    "E5": "E5-electrical-principles",
    "E6": "E6-circuit-components",
    "E7": "E7-practical-circuits",
    "E8": "E8-signals-emissions",
    "E9": "E9-antennas-transmission-lines",
}

# Group descriptions for the Extra 2024-2028 pool
GROUP_DESCRIPTIONS = {
    # E0 — Safety
    "E0A": "Safety: RF radiation hazards; exposure limits; hazardous materials; station safety",
    # E1 — Commission's Rules
    "E1A": "Operating standards: frequency privileges; emission standards; automatic message forwarding; frequency sharing; stations aboard ships or aircraft",
    "E1B": "Station restrictions and special operations: restrictions on station location; spurious emissions; national quiet zone; beacon operation; restricted operation; spread spectrum; auxiliary station; Canadian amateurs operating in US; online exams",
    "E1C": "Definitions and restrictions for digital communications: automaticaly controlled digital station; definitions; RTTY and data emission standards",
    "E1D": "Amateur satellites: definitions; frequencies; modes; licensing requirements",
    "E1E": "Volunteer Examiner program: definitions; qualifications; preparation and administration of exams; accreditation; question pools; documentation requirements",
    "E1F": "Miscellaneous rules: external RF power amplifiers; business communications; national security; auxiliary stations; parachutes; spread spectrum; auxiliary stations; Section 97.1",
    # E2 — Operating Procedures
    "E2A": "Amateur radio in space: amateur satellites; orbital mechanics; frequencies and modes; satellite hardware; satellite operations; geosynchronous vs. non-geosynchronous orbits",
    "E2B": "Television practices: fast-scan television standards and techniques; slow-scan television standards and techniques",
    "E2C": "Operating methods: contest and DX operating; remote operation techniques; Cabrillo format; QSLing; RF network connected systems",
    "E2D": "Operating methods: digital modes; full break-in; WSPR; mesh networks; APRS",
    "E2E": "Operating methods: operating HF digital modes; error correction",
    # E3 — Radio Wave Propagation
    "E3A": "Propagation and technique: electromagnetic waves; Earth-Moon-Earth communications; meteor scatter; aurora propagation; knife-edge diffraction; scatter propagation",
    "E3B": "Propagation and technique: transequatorial propagation; long-path and short-path; gray-line; multi-path propagation; ordinary and extraordinary waves; chordal hop; sporadic E",
    "E3C": "Radio horizon; solar propagation; HF propagation; transequatorial; aurora",
    # E4 — Amateur Practices
    "E4A": "Test equipment: analog and digital instruments; spectrum and network analyzers; antenna analyzers; oscilloscopes; RF measurements; computer-controlled test equipment",
    "E4B": "Measurement technique and limitations: instrument accuracy and precision; signal source improvements to measurements; two-port measurements; AF and RF measurements; pulse and noise measurement using spectrum analyzers",
    "E4C": "Receiver performance characteristics: phase noise; capture effect; noise floor; image rejection; MDS; signal-to-noise ratio; selectivity; intermodulation distortion",
    "E4D": "Receiver performance characteristics: blocking dynamic range; intermodulation distortion; third-order intercept; desensitization; preselector",
    "E4E": "Noise suppression and interference: system noise; electrical appliance noise; line noise; DSP noise reduction; noise blankers; grounding for signals",
    # E5 — Electrical Principles
    "E5A": "Resonance and Q: characteristics of series and parallel RLC circuits; resonant frequency calculations; half-power bandwidth; phase relationships at resonance",
    "E5B": "Time constants and phase angles: RC and RL time constants; definition and calculation of time constant; admittance and susceptance; phase angles in RLC circuits",
    "E5C": "Impedance plots and coordinate systems: plotting impedance; rectangular and polar coordinates; phasor diagrams; logarithmic frequency scales",
    "E5D": "Real and reactive power; skin effect; electrostatic and electromagnetic fields; reactive power; power factor; parasitic effects in RF components",
    # E6 — Circuit Components
    "E6A": "Semiconductor materials and devices: semiconductor materials; germanium; silicon; P-type; N-type; transistor types; NPN; PNP; junction diode; zener diode",
    "E6B": "Diodes: rectifier diodes; current flow; tunnel diodes; varactor diodes; hot carrier diodes; signal diodes; zener diodes; LEDs; photodiodes; Schottky diodes; PIN diodes",
    "E6C": "Digital ICs: families of digital ICs; gates; programmable logic devices (PLDs)",
    "E6D": "Toroidal and solenoidal inductors: permeability; core material; selecting RF inductors; ferrite and powdered-iron materials; quartz crystals; electromechanical filters; piezoelectric devices",
    "E6E": "Analog ICs: MMICs; SiGe; quartz crystal devices; monolithic amplifiers",
    "E6F": "Optical components: photoconductive principles; photovoltaic diodes; optoisolators; photovoltaic cells; light-dependent resistors (LDRs)",
    # E7 — Practical Circuits
    "E7A": "Digital circuits: digital circuit principles; flip-flops; counters; shift registers; multiplexers; demultiplexers; adders",
    "E7B": "Amplifiers: class A; class B; class C; class AB; push-pull amplifiers; distortion; efficiency",
    "E7C": "Filters and matching networks: types of networks; types of filters; filter applications; filter characteristics; impedance matching",
    "E7D": "Power supplies and voltage regulators: power transformers; rectifiers; filters; regulators; shunt and series regulators; switching regulators; inverters",
    "E7E": "Modulation and demodulation: modulation methods; modulation index; frequency and phase modulation; demodulation; mixer theory",
    "E7F": "DSP and software radio techniques: digital filters; software defined radio; signal processing",
    "E7G": "Active filters and op-amp circuits: active audio filters; op-amp circuits; op-amp applications; frequency response; gain bandwidth product",
    "E7H": "Oscillators and signal sources: types of oscillators; oscillator stability; synthesizers; phase-locked loops; frequency dividers; signal sources",
    # E8 — Signals and Emissions
    "E8A": "AC waveforms: sine, square, sawtooth, and irregular waveforms; AC measurements; average and PEP of RF signals; Fourier analysis; analog to digital conversion",
    "E8B": "Modulation and demodulation: phase modulation; phase velocity; digital waveforms; modulation index; pulse modulation; frequency and time division multiplexing",
    "E8C": "Digital signals: digital communication modes; information rate vs bandwidth; error correction coding; spread spectrum; OFDM",
    "E8D": "Keying defects and noise in digital signals: signal noise; static; interference; modulation index",
    # E9 — Antennas and Transmission Lines
    "E9A": "Antenna fundamentals: types of antennas; antenna gain; radiation patterns; polarization; efficiency; ground effects",
    "E9B": "Antenna patterns: pattern measurements; far-field; antenna testing; phased arrays; antenna modeling",
    "E9C": "Wire and phased vertical antennas: beverage antennas; terminated antennas; rhombic antennas; NVIS antennas; phased arrays",
    "E9D": "Directional antennas: Yagi antennas; Quad antennas; stacking; feeding Yagi antennas",
    "E9E": "Matching techniques: matching antennas to feed lines; power matching; SWR; antenna tuners; common-mode chokes",
    "E9F": "Transmission lines: characteristics; standing waves; SWR; velocity factor; electrical length; coaxial cable",
    "E9G": "The Smith chart: using the Smith chart; normalizing impedances; impedance matching; transmission line analysis",
    "E9H": "Receiving antennas: direction finding antennas; active antennas; noise-canceling antennas; loop antennas; magnetic loops",
}

# ── Explanation generator ────────────────────────────────────────────
# Hand-written explanations for every question in the 2024-2028 Extra pool.
# Key = question ID, value = explanation paragraph.

EXPLANATIONS: dict[str, str] = {}


def _load_explanations() -> None:
    """Populate the EXPLANATIONS dict.

    The explanations are defined inline below rather than in a separate
    data file so the script is fully self-contained.
    """
    # fmt: off
    E = EXPLANATIONS

    # ── E5A — Resonance and Q ─────────────────────────────────────────

    E["E5A01"] = (
        "At resonance in a series RLC circuit, the inductive reactance (X_L) exactly equals the "
        "capacitive reactance (X_C). They don't cancel to zero — they both exist, they cancel "
        "each other in terms of the net impedance seen by the source, but the voltage across each "
        "individual reactance is amplified. The voltage across the inductor V_L = I × X_L, and "
        "since at resonance X_L can be much larger than R, V_L can be much larger than the applied "
        "voltage. The ratio of this magnified voltage to the applied voltage equals Q — the quality "
        "factor. A high-Q series circuit at resonance has enormous voltages across the individual "
        "reactive components, even though the net terminal voltage is just what you applied. This "
        "voltage magnification is why resonance is both useful (filters, oscillators) and potentially "
        "destructive (capacitor breakdown in high-Q resonant circuits)."
    )

    E["E5A02"] = (
        "Use the resonant frequency formula: f = 1 / (2π√(LC)). "
        "With L = 50 µH = 50×10⁻⁶ H and C = 40 pF = 40×10⁻¹² F: "
        "LC = 50×10⁻⁶ × 40×10⁻¹² = 2000×10⁻¹⁸ = 2×10⁻¹⁵. "
        "√(LC) = √(2×10⁻¹⁵) = 4.47×10⁻⁸. "
        "f = 1 / (2π × 4.47×10⁻⁸) = 1 / (2.81×10⁻⁷) ≈ 3,559,000 Hz ≈ 3.56 MHz. "
        "Note that R = 22 Ω is a distractor — resistance does not affect the resonant frequency "
        "(only L and C determine where the reactances are equal). R affects the Q and bandwidth "
        "of the resonance, but not the resonant frequency itself."
    )

    E["E5A03"] = (
        "At resonance in a series RLC circuit, X_L = X_C exactly. These equal-but-opposite "
        "reactances cancel in the series path — the net reactance is zero. What remains is only "
        "the resistance R. So the total series impedance at resonance is Z = R + j(X_L - X_C) = "
        "R + j(0) = R. The impedance magnitude equals the circuit resistance. This is why series "
        "resonant circuits are used as filters that pass the resonant frequency: at resonance, "
        "impedance drops to a minimum (just R), so maximum current flows at that frequency. At "
        "all other frequencies, the net reactance adds to R and impedance is higher, so less "
        "current flows. Series resonance = minimum impedance = maximum current."
    )

    E["E5A04"] = (
        "In a parallel RLC circuit at resonance, the impedance is at its MAXIMUM and equals "
        "the equivalent parallel resistance. When X_L = X_C in the parallel circuit, the LC "
        "parallel combination presents infinite impedance (the circulating reactive currents "
        "cancel, leaving no net current drawn from the source at that frequency). The only "
        "path left for source current is through R, so Z = R. This is why the answer says "
        "'approximately equal to circuit resistance' — at resonance the tank's reactive currents "
        "circulate internally, drawing no reactive current from the source. This high-impedance "
        "behavior is the basis of bandpass filters and tank circuits in amplifiers. Contrast with "
        "series resonance where impedance is minimum at resonance."
    )

    E["E5A05"] = (
        "Q (quality factor) is inversely proportional to bandwidth: BW = f_r / Q. A higher Q "
        "means a narrower bandwidth. In an impedance-matching circuit, higher Q creates sharper "
        "frequency selectivity — it matches well at the design frequency but poorly at adjacent "
        "frequencies. This narrow bandwidth can be a problem in wideband applications but is "
        "desirable when you want selectivity. In practical terms, if you're building an "
        "impedance-matching network for an antenna that needs to work over a 500 kHz range, "
        "you want moderate Q. If you're building a crystal filter, you want extremely high Q "
        "for sharp selectivity. Higher Q = narrower bandwidth = more selective but less flexible."
    )

    E["E5A06"] = (
        "In a parallel LC circuit at resonance, the circulating current within the tank — flowing "
        "back and forth between the inductor and capacitor — is at its maximum. This internal "
        "circulating current equals Q times the current supplied by the source. The source only "
        "supplies enough current to replace the small energy lost to the circuit's resistance; "
        "the much larger reactive current circulates internally. Physically, energy sloshes back "
        "and forth: the capacitor discharges into the inductor, the inductor's collapsing field "
        "recharges the capacitor, and the cycle repeats. The Q of the circuit tells you how many "
        "times the energy circulates before it's dissipated. A Q of 100 means the circulating "
        "current is 100× the source current."
    )

    E["E5A07"] = (
        "At resonance, a parallel RLC circuit presents its highest impedance to the source (E5A04). "
        "By Ohm's law, I = V/Z — if impedance is maximum, current from the source is minimum. "
        "The reactive currents circulate internally within the LC tank, drawing no net reactive "
        "current from the source. The source only supplies the resistive (real) current to "
        "overcome losses. This minimum input current at resonance is the defining characteristic "
        "used in practical circuit design: a parallel resonant tank is connected in series with "
        "a load to create a bandstop notch at the resonant frequency (maximum impedance = "
        "minimum throughput), or in parallel to create a bandpass response. Compare to the "
        "series circuit (E5A03) where current is maximum at resonance."
    )

    E["E5A08"] = (
        "In a series RLC circuit AT resonance, X_L = X_C, so the net reactance is zero. The "
        "circuit behaves as a pure resistance. For a pure resistance, voltage and current are "
        "exactly in phase — no phase shift at all. This is a crucial distinction: below resonance "
        "the circuit is capacitive (current leads voltage), above resonance it is inductive "
        "(voltage leads current), but at the resonant frequency the phase angle is precisely zero "
        "degrees. The circuit 'looks' purely resistive at resonance. Don't confuse this with "
        "the individual components: the voltage across the inductor still leads its current by 90°, "
        "and the voltage across the capacitor still lags, but the terminal voltage and current of "
        "the complete series circuit are in phase at resonance."
    )

    E["E5A09"] = (
        "For a parallel RLC circuit, Q = R / X_L (or equivalently R / X_C, since X_L = X_C at "
        "resonance). This is the inverse of the series RLC formula where Q = X_L / R. The "
        "difference makes physical sense: in a series circuit, high Q requires high reactance "
        "relative to resistance (high voltage magnification). In a parallel circuit, high Q "
        "requires high resistance relative to reactance (the tank has low losses compared to the "
        "reactive energy circulating). Numerically, if R = 5000 Ω and X_L = 50 Ω at resonance, "
        "Q = 5000/50 = 100. This high Q means the parallel tank has sharp resonance and the "
        "circulating current is 100× the source current (E5A06)."
    )

    E["E5A10"] = (
        "Use f = 1 / (2π√(LC)) with L = 50 µH = 50×10⁻⁶ H and C = 10 pF = 10×10⁻¹² F: "
        "LC = 50×10⁻⁶ × 10×10⁻¹² = 500×10⁻¹⁸ = 5×10⁻¹⁶. "
        "√(LC) = √(5×10⁻¹⁶) = 2.236×10⁻⁸. "
        "f = 1 / (2π × 2.236×10⁻⁸) = 1 / (1.405×10⁻⁷) ≈ 7,118,000 Hz ≈ 7.12 MHz. "
        "Compare to E5A02 where C = 40 pF gave 3.56 MHz. Here C is ¼ as large, so f is 2× "
        "higher (f scales as 1/√C). That's consistent: 3.56 × 2 = 7.12 MHz. "
        "Again, R = 33 Ω has no effect on the resonant frequency."
    )

    E["E5A11"] = (
        "The half-power bandwidth formula is BW = f_r / Q. "
        "With f_r = 7.1 MHz = 7,100,000 Hz and Q = 150: "
        "BW = 7,100,000 / 150 = 47,333 Hz ≈ 47.3 kHz. "
        "The 'half-power' bandwidth is the frequency span between the points where the signal "
        "power drops to half (-3 dB) of the peak. A Q of 150 on the 40-meter band is fairly "
        "high — this represents a selective circuit that passes only a 47 kHz window around "
        "7.1 MHz. Crystal filters can achieve Q values in the thousands, giving bandwidths "
        "of just a few hundred hertz. The BW = f_r/Q relationship is one of the most useful "
        "formulas in RF design."
    )

    E["E5A12"] = (
        "Use BW = f_r / Q with f_r = 3.7 MHz = 3,700,000 Hz and Q = 118: "
        "BW = 3,700,000 / 118 = 31,356 Hz ≈ 31.4 kHz. "
        "This is on the 80-meter band. A Q of 118 gives a bandwidth of about 31 kHz, which is "
        "narrower than the entire 80m phone segment (~200 kHz wide). If you're designing an "
        "antenna matching circuit for 80m, Q = 118 would give good selectivity but would "
        "need adjustment as you move across the band. For broadband coverage you want lower Q; "
        "for maximum selectivity at one frequency you want higher Q."
    )

    E["E5A13"] = (
        "In a series resonant circuit, Q = X_L / R = voltage across the inductor (or capacitor) "
        "divided by the applied voltage. When Q increases, the internal voltages across the "
        "inductor and capacitor both increase proportionally. Recall from E5A01 that V_L = Q × V_applied. "
        "If Q doubles from 50 to 100, the voltage across the inductor also doubles. This voltage "
        "magnification is real — in a high-Q series resonant circuit, the reactive component "
        "voltages can be many times the applied voltage. This has practical implications: "
        "capacitors in high-Q circuits must be rated for the magnified voltage, not just the "
        "source voltage. It also means fewer components are NOT needed for the same performance; "
        "in fact, the high voltages impose more demanding component requirements."
    )

    # ── E5B — Time Constants and Phase Angles ────────────────────────

    E["E5B01"] = (
        "The time constant τ (tau) is the time it takes for a capacitor in an RC circuit to "
        "charge to 63.2% of the applied voltage (or discharge to 36.8% of its initial voltage). "
        "τ = R × C, with R in ohms and C in farads, giving τ in seconds. The 63.2% figure comes "
        "from the exponential charging equation: V(t) = V_final × (1 - e^(-t/τ)). At t = τ: "
        "V = V_final × (1 - e^(-1)) = V_final × (1 - 0.368) = V_final × 0.632 = 63.2%. "
        "After 5τ the capacitor is considered fully charged (99.3%). The time constant concept "
        "applies equally to RL circuits where τ = L/R. Memorize: one time constant = 63.2% "
        "charged, five time constants = fully charged."
    )

    E["E5B02"] = (
        "The letter B represents susceptance. This is a vocabulary question requiring straight "
        "memorization. The complex electrical quantities use these symbols: Z = impedance, "
        "Y = admittance (inverse of Z), R = resistance, G = conductance (inverse of R), "
        "X = reactance, B = susceptance (inverse of X). Admittance Y = G + jB, just as "
        "impedance Z = R + jX. The parallel: G is to R as B is to X. Susceptance B = 1/X "
        "(for pure reactance) in siemens. Don't confuse B (susceptance) with G (conductance) "
        "or Y (admittance) — they're related but distinct quantities."
    )

    E["E5B03"] = (
        "To convert impedance in polar form Z∠θ to admittance Y∠φ: take the reciprocal of the "
        "magnitude and change the sign of the angle. If Z = 50∠30° then Y = (1/50)∠(-30°) = "
        "0.02∠-30°. This follows from Y = 1/Z. If Z = |Z|×e^(jθ), then Y = 1/(|Z|×e^(jθ)) = "
        "(1/|Z|)×e^(-jθ). The magnitude inverts (50Ω → 0.02 S) and the angle negates (+30° → -30°). "
        "This makes physical sense: a capacitive impedance (negative angle) becomes a capacitive "
        "admittance (positive angle in admittance convention since jB is positive for capacitive "
        "susceptance). Polar form makes reciprocal operations simple: just flip magnitude and "
        "negate angle."
    )

    E["E5B04"] = (
        "With two 220 µF capacitors and two 1 MΩ resistors all in PARALLEL: "
        "Parallel capacitances ADD: C_total = 220 + 220 = 440 µF = 440×10⁻⁶ F. "
        "Parallel resistances: R_total = (1×10⁶ × 1×10⁶) / (1×10⁶ + 1×10⁶) = 0.5 MΩ = 500,000 Ω. "
        "Time constant τ = R × C = 500,000 × 440×10⁻⁶ = 500,000 × 0.000440 = 220 seconds. "
        "The answer is 220 seconds. Two components in parallel for both capacitors and resistors: "
        "parallel caps double the capacitance, parallel resistors halve the resistance. "
        "The net effect: τ = (R/2) × (2C) = RC = unchanged from a single pair. "
        "Here: τ = (1×10⁶/2) × (2 × 220×10⁻⁶) = 0.5×10⁶ × 440×10⁻⁶ = 220 s."
    )

    E["E5B05"] = (
        "Susceptance is the reciprocal of reactance: B = 1/X. So if a capacitor has a reactance "
        "of X_C = 50 Ω at some frequency, its susceptance is B_C = 1/50 = 0.02 siemens. The "
        "magnitude is replaced by its reciprocal — 50 Ω becomes 0.02 S. Note that the sign "
        "also inverts in the complex sense: a capacitive reactance is -jX (negative j, by "
        "convention), but capacitive susceptance is +jB (positive j). The magnitude question "
        "here asks specifically about magnitude: it becomes the reciprocal. Small reactance = "
        "large susceptance (easy current flow). Large reactance = small susceptance (hard current "
        "flow). This is the same reciprocal relationship as resistance vs. conductance (G = 1/R)."
    )

    E["E5B06"] = (
        "Susceptance is the imaginary part of admittance. Admittance Y = G + jB, where G is "
        "conductance (real part) and B is susceptance (imaginary part). Just as impedance "
        "Z = R + jX has a real part (resistance) and imaginary part (reactance), admittance "
        "has its own real and imaginary parts. Susceptance B is measured in siemens (S). "
        "For a purely reactive component: B = -1/X for an inductor and B = +1/X for a capacitor "
        "(the sign convention inverts when going from impedance to admittance). Susceptance "
        "is NOT a measure of transformer efficiency (that's just efficiency), NOT the ratio of "
        "magnetic to electric fields (that's the wave impedance of free space), and NOT magnetic "
        "impedance (a non-standard term). It is specifically the imaginary part of admittance."
    )

    E["E5B07"] = (
        "Phase angle θ = arctan((X_L - X_C) / R). With X_C = 500 Ω, R = 1000 Ω, X_L = 250 Ω: "
        "θ = arctan((250 - 500) / 1000) = arctan(-250/1000) = arctan(-0.25) = -14.0°. "
        "The negative angle means the circuit is net capacitive: X_C > X_L (500 > 250 Ω). "
        "In a capacitive circuit, current leads voltage — equivalently, voltage lags current. "
        "So the voltage lags the current by 14.0°. "
        "Quick check of the magnitudes: the net reactance is only 250 Ω out of 1000 Ω resistance, "
        "so the angle should be fairly small, not 45° or 68° — 14° is consistent."
    )

    E["E5B08"] = (
        "Phase angle θ = arctan((X_L - X_C) / R). With X_C = 300 Ω, R = 100 Ω, X_L = 100 Ω: "
        "θ = arctan((100 - 300) / 100) = arctan(-200/100) = arctan(-2) = -63.4° ≈ -63°. "
        "Negative angle → net capacitive circuit (X_C = 300 > X_L = 100) → voltage lags current. "
        "The reactance (200 Ω net) is twice the resistance (100 Ω), so the angle is large, close "
        "to the 90° of a pure reactance. arctan(2) = 63.4° confirms this. "
        "Answer: 63 degrees with the voltage lagging the current."
    )

    E["E5B09"] = (
        "For a capacitor, current LEADS voltage by 90°. The mnemonic is 'ICE' (I before C before E, "
        "where E = EMF = voltage): Current (I) leads Voltage (E) in a Capacitor (C). Physically: "
        "current flows first to charge the capacitor, then voltage builds up across it. The "
        "capacitor's voltage is the integral of the current, which introduces a 90° phase lag "
        "in voltage relative to current. In complex notation: for a capacitor V = I × (1/jωC), "
        "which equals I × (-j/ωC), introducing a -90° phase shift in voltage. Since voltage is "
        "-90° relative to current, current is +90° (leading) relative to voltage. "
        "Contrast with inductors where voltage leads current (E5B10)."
    )

    E["E5B10"] = (
        "For an inductor, VOLTAGE leads current by 90°. The mnemonic is 'ELI' (E before L before I): "
        "Voltage (E/EMF) leads Current (I) in an Inductor (L). Physically: voltage is applied "
        "and induces current that builds up gradually due to the inductor's opposition to changing "
        "current. Voltage precedes current. In complex notation: V = L × dI/dt, which in frequency "
        "domain is V = jωL × I. The j operator represents a +90° phase shift, so V leads I by 90°. "
        "Combined mnemonic: ELI the ICEman — voltage leads in inductors, current leads in capacitors. "
        "This 90° relationship is what makes reactive power oscillate without dissipation (E5D03)."
    )

    E["E5B11"] = (
        "Phase angle θ = arctan((X_L - X_C) / R). With X_C = 25 Ω, R = 100 Ω, X_L = 75 Ω: "
        "θ = arctan((75 - 25) / 100) = arctan(50/100) = arctan(0.5) = 26.6° ≈ 27°. "
        "Positive angle → net inductive circuit (X_L = 75 > X_C = 25 Ω) → voltage leads current. "
        "The net reactance is 50 Ω inductive vs. 100 Ω resistance, giving a moderate angle of ~27°. "
        "Answer: 27 degrees with the voltage leading the current. "
        "Compare to E5B07 and E5B08 — the sign of (X_L - X_C) tells you everything: "
        "positive → inductive → voltage leads; negative → capacitive → voltage lags."
    )

    E["E5B12"] = (
        "Admittance is the inverse (reciprocal) of impedance: Y = 1/Z. Just as conductance G = 1/R "
        "makes it easier to calculate parallel resistors (add conductances instead of using the "
        "parallel resistance formula), admittance Y = 1/Z makes parallel impedance calculations "
        "simpler (Y_total = Y_1 + Y_2 + ...). Admittance is measured in siemens (S). "
        "Y is NOT the inverse of reactance (that's susceptance B), NOT the gain of a FET "
        "(that's transconductance g_m), and NOT the on-impedance of a FET. "
        "The complete relationship: Y = G + jB, where G = conductance (1/R) and B = susceptance "
        "(imaginary part). Admittance is the complete AC analog of conductance for complex circuits."
    )

    # ── E5C — Impedance Plots and Coordinate Systems ─────────────────

    E["E5C01"] = (
        "Pure capacitive reactance of 100 Ω in rectangular notation is written as 0 - j100. "
        "In the rectangular (Cartesian) impedance notation Z = R + jX: the real part R (resistance) "
        "is the first term, and the imaginary part jX (reactance) is the second. For pure "
        "capacitive reactance: R = 0 (no resistance) and X = -100 Ω (capacitive reactance is "
        "negative by convention). The negative j indicates the reactance is capacitive (below "
        "the real axis on a phasor diagram). A pure inductive reactance of 100 Ω would be 0 + j100. "
        "A 100 Ω resistor with no reactance would be 100 + j0, or simply 100. "
        "The j convention: +j = inductive (positive imaginary), -j = capacitive (negative imaginary)."
    )

    E["E5C02"] = (
        "In polar coordinates, impedance is described by MAGNITUDE and PHASE ANGLE — written as "
        "Z∠θ or |Z|∠θ. For example, a 50 Ω impedance at +45° is written 50∠45°. The magnitude "
        "|Z| = √(R² + X²) tells you the total opposition to AC current. The angle θ = arctan(X/R) "
        "tells you the phase relationship between current and voltage. "
        "Contrast with rectangular coordinates (R + jX), which describe the same impedance by "
        "its resistive and reactive components. The two are mathematically equivalent: "
        "R = |Z|cos(θ) and X = |Z|sin(θ). Polar is natural for multiplication and division "
        "(multiply magnitudes, add angles); rectangular is natural for addition and subtraction. "
        "For exam purposes: polar = magnitude and angle; rectangular = R ± jX."
    )

    E["E5C03"] = (
        "A pure inductive reactance in polar coordinates has a positive 90° phase angle. "
        "If X_L = 100 Ω (pure inductance, no resistance), then in polar form: "
        "|Z| = X_L = 100 Ω, and θ = arctan(X_L/R) = arctan(100/0) = +90°. "
        "So the polar form is 100∠+90°. The positive angle confirms this is inductive. "
        "For pure capacitive reactance, the polar form would be X_C∠-90° (negative 90°). "
        "For pure resistance, the polar form is R∠0° (zero angle). "
        "The sign of the phase angle tells you the character of the reactance: "
        "+90° = pure inductive, -90° = pure capacitive, 0° = pure resistive. "
        "Intermediate angles indicate a mix of resistance and reactance."
    )

    E["E5C04"] = (
        "A logarithmic scale is used on the Y-axis (or most often X-axis) for circuit frequency "
        "response graphs. Logarithmic frequency scales compress the wide dynamic range of typical "
        "filter responses into a readable plot. A filter might have a response from -1 dB at "
        "10 kHz to -60 dB at 1 MHz — a 100:1 frequency range and a 60 dB amplitude range. "
        "Both ranges are much more readable on log scales. The 'Bode plot' uses log frequency "
        "on the horizontal axis and dB on the vertical axis. For frequency response, logarithmic "
        "is standard because an octave (2:1 frequency ratio) always looks the same width "
        "regardless of whether you're at 100 Hz or 100 MHz. Linear scales would waste most of "
        "the plot on the low-frequency end."
    )

    E["E5C05"] = (
        "A phasor diagram shows the phase relationships between voltages and currents in a circuit. "
        "Phasors are rotating vectors — each component's voltage or current is represented as an "
        "arrow whose length equals the magnitude and whose angle relative to a reference "
        "represents the phase. In a series RLC circuit: V_R points along the reference (0°), "
        "V_L points upward (+90°), V_C points downward (-90°), and the total voltage V is the "
        "vector sum. Phasor diagrams let you visualize why V_L and V_C partially cancel, why the "
        "total voltage isn't simply the sum of the magnitudes, and why phase angles change with "
        "frequency. Not a Venn diagram (sets), not a near-field diagram (antenna patterns), "
        "not a far-field diagram (antenna gain patterns) — a phasor diagram for phase relationships."
    )

    E["E5C06"] = (
        "Impedance 50 - j25 ohms represents 50 Ω resistance in series with 25 Ω capacitive "
        "reactance. In Z = R + jX notation: R = 50 Ω (the real part, positive resistance), "
        "X = -25 Ω (the imaginary part). The negative sign on the j term indicates capacitive "
        "reactance (recall from E5C01 that capacitive reactance is written as -jX). "
        "The '-j25' means 25 Ω of capacitive reactance, not inductive. If it were inductive, "
        "it would be written as +j25. The number 50 is the resistive part, and 25 is the "
        "magnitude of the reactive part. This notation is fundamental to RF engineering — "
        "every impedance can be expressed as a complex number in this form."
    )

    E["E5C07"] = (
        "Pure resistance plots on the horizontal axis (real axis) in rectangular coordinates. "
        "In the complex impedance plane (R + jX), the horizontal axis represents the real "
        "component (resistance) and the vertical axis represents the imaginary component "
        "(reactance). A pure resistor has zero reactance, so its impedance Z = R + j0 = R "
        "plots directly on the horizontal axis. Moving right along the axis = increasing "
        "resistance. Pure inductance (Z = 0 + jX_L) plots on the positive vertical axis. "
        "Pure capacitance (Z = 0 - jX_C) plots on the negative vertical axis. "
        "This Argand diagram structure is the basis of the Smith chart, which maps the entire "
        "impedance plane onto a circle for transmission line calculations."
    )

    E["E5C08"] = (
        "Polar coordinates are used to display the phase angle of a circuit containing "
        "resistance and reactance. Polar form Z∠θ directly gives you the phase angle θ, making "
        "it ideal when you want to know 'what angle is the impedance?' Rectangular form R + jX "
        "doesn't directly show you the angle — you'd have to calculate arctan(X/R). For quickly "
        "answering 'is this mostly resistive or mostly reactive?' or 'what's the phase shift "
        "through this network?', polar coordinates give you the answer immediately. "
        "Maidenhead grid locates geographic positions, Faraday grid isn't a standard coordinate "
        "system, and elliptical coordinates are used in antenna analysis but not for impedance "
        "phase angles."
    )

    E["E5C09"] = (
        "In rectangular coordinates for impedance: the X axis (horizontal) represents the "
        "resistive component (R), and the Y axis (vertical) represents the reactive component "
        "(X). Positive Y direction (+j) indicates inductive reactance; negative Y direction (-j) "
        "indicates capacitive reactance. This is the standard complex plane representation where "
        "Z = R + jX maps to the point (R, X) in Cartesian coordinates. The question asks about "
        "what the positive j (vertical) direction indicates — it indicates inductive reactance "
        "(positive imaginary = inductive by the standard j convention). "
        "A 50 + j75 impedance plots right and up (resistive and inductive). "
        "A 50 - j75 impedance plots right and down (resistive and capacitive)."
    )

    E["E5C10"] = (
        "Series circuit: 400 Ω resistor + 38 pF capacitor at 14 MHz. "
        "Calculate X_C = 1/(2πfC) = 1/(2π × 14×10⁶ × 38×10⁻¹²) = 1/(3.33×10⁻³) ≈ 299 Ω. "
        "Impedance Z = 400 - j299 Ω. In rectangular coordinates this is at (400, -299) — "
        "large positive resistance, significant negative (capacitive) reactance. "
        "On Figure E5-1, Point 4 represents this: it's in the fourth quadrant (positive R, "
        "negative X), with resistance larger than the capacitive reactance component. "
        "The resistive component (400) is larger than the reactive component (299), "
        "so the point is closer to the R axis than to the -jX axis — consistent with Point 4."
    )

    E["E5C11"] = (
        "Series circuit: 300 Ω resistor + 18 µH inductor at 3.505 MHz. "
        "Calculate X_L = 2πfL = 2π × 3.505×10⁶ × 18×10⁻⁶ = 2π × 63.09 ≈ 396 Ω. "
        "Impedance Z = 300 + j396 Ω. This plots in the first quadrant (positive R, positive X) "
        "at coordinates (300, +396) — resistance and inductive reactance are comparable, "
        "with reactance slightly larger. On Figure E5-1, Point 3 represents this: "
        "first quadrant with reactance somewhat greater than resistance. "
        "The similar magnitudes of R (300) and X_L (396) place the point at roughly 53° angle, "
        "not hugging either axis."
    )

    E["E5C12"] = (
        "Series circuit: 300 Ω resistor + 19 pF capacitor at 21.200 MHz. "
        "Calculate X_C = 1/(2πfC) = 1/(2π × 21.2×10⁶ × 19×10⁻¹²) = 1/(2.53×10⁻³) ≈ 395 Ω. "
        "Impedance Z = 300 - j395 Ω. This plots in the fourth quadrant (positive R, negative X) "
        "at coordinates (300, -395) — resistance and capacitive reactance are comparable, "
        "with reactance slightly larger. On Figure E5-1, Point 1 represents this: "
        "fourth quadrant with reactance somewhat greater than resistance. "
        "Compare to E5C10: both are capacitive (fourth quadrant), but this one has more "
        "balanced R and X values, placing it at a steeper angle from the R axis."
    )

    # ── E5D — Real and Reactive Power; Parasitic Effects ─────────────

    E["E5D01"] = (
        "Skin effect causes resistance to increase with frequency because RF current flows "
        "closer to the surface of the conductor. At DC, current distributes uniformly across "
        "the conductor's cross-section. As frequency increases, the alternating magnetic field "
        "inside the conductor opposes current flow in the interior, pushing current toward the "
        "surface. This 'skin depth' (the depth to which current penetrates) decreases as "
        "frequency increases — δ = √(2ρ/ωμ), where ρ is resistivity and μ is permeability. "
        "At RF frequencies, current effectively flows only in a thin skin on the outside, "
        "dramatically reducing the effective cross-sectional area carrying current. Less area "
        "= higher resistance. This is why hollow copper tubing makes an excellent RF conductor — "
        "the interior carries no current anyway at HF, so it's just dead weight."
    )

    E["E5D02"] = (
        "Short lead lengths are critical at VHF and above to minimize inductive reactance. "
        "Every wire has inductance — roughly 20 nH per inch for typical component leads. "
        "At low frequencies this is negligible, but inductive reactance X_L = 2πfL grows with "
        "frequency. At 300 MHz, 1 inch of wire (20 nH) has X_L = 2π × 300×10⁶ × 20×10⁻⁹ ≈ 38 Ω. "
        "That's enough to significantly alter circuit behavior, detune filters, and add parasitic "
        "resonances. Short leads also minimize parasitic capacitance (from lead-to-lead proximity) "
        "and reduce the component's tendency to self-resonate (E5D07). At microwave frequencies "
        "(GHz), even millimeter-length leads matter — that's why surface-mount components replaced "
        "through-hole components in RF circuits."
    )

    E["E5D03"] = (
        "For reactive power, current and voltage are 90° out of phase. Reactive power (Q, measured "
        "in VAR — volt-amperes reactive) is the power that oscillates between the source and a "
        "reactive component. In a pure inductor or capacitor, current and voltage are exactly 90° "
        "out of phase (E5B09, E5B10). When they're 90° apart, the product V×I averages to zero "
        "over a full cycle — no real power is dissipated. Instead, energy is stored for a quarter "
        "cycle then returned. Real power (watts) requires voltage and current to be in phase; "
        "reactive power (VAR) is the out-of-phase component. The distinction matters for power "
        "factor: P_real = V × I × cos(θ), and reactive power Q = V × I × sin(θ)."
    )

    E["E5D04"] = (
        "Short connections at microwave frequencies reduce phase shift along the connection. "
        "At microwave frequencies (GHz), the wavelength is on the order of centimeters or even "
        "millimeters. A wire or PCB trace that seems 'short' at audio frequencies can be a "
        "significant fraction of a wavelength at 10 GHz. A quarter-wavelength trace acts as an "
        "impedance transformer; a half-wavelength trace is a resonant element. Any connection "
        "longer than about λ/20 introduces meaningful phase shift that changes circuit behavior "
        "in ways not captured by simple lumped-element circuit models. Short connections keep "
        "everything in the lumped-element regime where component values dominate over "
        "transmission-line effects. 'Reduce phase shift along the connection' is the engineering "
        "statement of this — longer connections shift the phase of signals traversing them."
    )

    E["E5D05"] = (
        "Electrolytic capacitors are unsuitable for RF because of their high inductance (ESL — "
        "equivalent series inductance). Electrolytics are constructed with rolled foil and "
        "electrolyte, which creates significant internal inductance. At some frequency, this "
        "parasitic inductance resonates with the capacitance, above which the component behaves "
        "as an inductor, not a capacitor. This self-resonant frequency (SRF) is typically in "
        "the low kHz to tens of kHz for large electrolytics — far too low for RF applications. "
        "Above the SRF, the capacitor provides no filtering benefit and actually adds inductance. "
        "For RF bypassing and filtering, use ceramic or film capacitors with low ESL. "
        "Electrolytics are fine for power supply filtering at 60-120 Hz where their high "
        "capacitance-per-volume is valuable."
    )

    E["E5D06"] = (
        "Inter-turn capacitance creates an inductor's self-resonance. Every pair of adjacent turns "
        "in a coil acts as a tiny capacitor — the wire forms one plate, the insulation is the "
        "dielectric, and the adjacent turn is the other plate. At some frequency, this distributed "
        "capacitance resonates with the coil's inductance. Above the self-resonant frequency "
        "(SRF), the component no longer behaves as an inductor — the distributed capacitance "
        "dominates and it looks like a capacitor. This is why RF inductors are designed with "
        "wide turn spacing, low-permeability cores, and sometimes single-layer windings — to "
        "minimize inter-turn capacitance and push the SRF as high as possible. A coil used "
        "above its SRF is useless as an inductor."
    )

    E["E5D07"] = (
        "Self-resonance in a component occurs when the component's nominal reactance (what it's "
        "designed to do) resonates with its parasitic reactance (an unwanted side effect). "
        "For an inductor: the nominal inductance resonates with the parasitic inter-turn "
        "capacitance (E5D06). For a capacitor: the nominal capacitance resonates with the "
        "parasitic lead inductance (E5D05). In both cases, it's the interaction between the "
        "'intentional' reactance and the 'accidental' reactance of the opposite sign. At "
        "the self-resonant frequency, the component has its lowest impedance (for a capacitor) "
        "or highest impedance (for an inductor), and above the SRF the component's behavior "
        "reverses. Resistance doesn't cause resonance; electrical length matters but isn't "
        "the mechanism; inductance alone or capacitance alone doesn't resonate — they need a "
        "partner of the opposite type."
    )

    E["E5D08"] = (
        "The primary cause of loss in film capacitors at RF is skin effect. In a film capacitor, "
        "RF current flows through thin metallic film electrodes. Skin effect (E5D01) confines "
        "the current to the surface of these thin films, effectively reducing the conducting "
        "cross-section and increasing resistance. This skin-effect resistance shows up as "
        "equivalent series resistance (ESR) in the capacitor model. The ESR dissipates real "
        "power: P = I²×ESR. The dielectric loss (loss tangent of the film material) also "
        "contributes but is generally secondary for good film materials like polypropylene or "
        "Teflon. For RF power applications (transmitter output filters, matching networks), "
        "low-ESR film capacitors with silver or thick metallic electrodes minimize skin-effect "
        "losses. This is distinct from electrolytic capacitors where ESL dominates (E5D05)."
    )

    E["E5D09"] = (
        "In ideal inductors and capacitors, reactive power energy is stored in magnetic or "
        "electric fields but is NOT dissipated as heat. The energy alternately flows in and "
        "then back out — stored for a quarter cycle, returned for the next quarter cycle. "
        "An ideal inductor stores energy in its magnetic field (E = ½LI²) when current flows, "
        "then releases it back to the circuit as current decreases. An ideal capacitor stores "
        "energy in its electric field (E = ½CV²) when charged, then returns it as it discharges. "
        "No power is lost in this exchange — reactive power is 'borrowed and returned,' not "
        "consumed. This is fundamentally different from resistors where energy is irreversibly "
        "converted to heat. Real-world components have resistance that does dissipate power — "
        "the ESR of capacitors and the wire resistance of inductors."
    )

    E["E5D10"] = (
        "As a conductor's diameter increases, its electrical length increases (it becomes "
        "electrically longer). This is the velocity factor effect: thicker conductors have a "
        "lower velocity factor — RF waves travel more slowly along them relative to the speed "
        "of light. Lower velocity means shorter wavelength for the same frequency: λ = v/f. "
        "Shorter wavelength means the physical conductor is a larger fraction of a wavelength "
        "= electrically longer. This effect is significant for antennas: a thick-element Yagi "
        "has electrically longer elements than a thin-wire version at the same physical length, "
        "which shifts the resonant frequency lower. Antenna designers account for this by "
        "shortening thick elements relative to the 'half-wave' formula that assumes infinitely "
        "thin wire."
    )

    E["E5D11"] = (
        "The circuit draws 1 ampere through a 100 Ω resistor in series with 100 Ω inductive "
        "reactance. Real power is only dissipated in the resistor: P = I² × R = 1² × 100 = 100 watts. "
        "The inductive reactance dissipates NO real power — it stores and returns energy (E5D09). "
        "To verify: total impedance Z = √(R² + X²) = √(100² + 100²) = √20000 = 141.4 Ω. "
        "With I = 1 A: voltage = I × Z = 141.4 V, and apparent power S = V × I = 141.4 VA. "
        "Real power P = I² × R = 100 W. Reactive power Q = I² × X_L = 100 VAR. "
        "Power factor = P/S = 100/141.4 = 0.707 = cos(45°), confirming the 45° phase angle "
        "between V and I (equal R and X). Only the resistor burns real watts."
    )

    E["E5D12"] = (
        "Reactive power is wattless, nonproductive power. It's the apparent power that circulates "
        "between the source and reactive components (inductors and capacitors) without doing useful "
        "work. Reactive power is measured in VAR (volt-amperes reactive) to distinguish it from "
        "real power (watts) and apparent power (VA). 'Wattless' means it appears on the ammeter "
        "(current flows) and voltmeter (voltage is present) but no watts are dissipated — the "
        "energy is borrowed then returned each cycle. Power utilities charge industrial customers "
        "for reactive power because it still loads the transmission system even though no useful "
        "work is done. In amateur radio, reactive power means your antenna feedline is carrying "
        "current that isn't being radiated — it's bouncing back as reflections (high SWR). "
        "Minimizing reactive power means maximizing the useful work done by your transmitter."
    )

    # ── E8D — Keying Defects and Noise ──────────────────────────

    E["E8D01"] = (
        "Spread-spectrum receivers suppress signals that do not match the spreading code. Anything outside the code "
        "looks like noise, so interference from unrelated signals is strongly reduced."
    )

    E["E8D02"] = (
        "Direct sequence spread spectrum uses a fast binary chip stream to flip the phase of the carrier. The high-rate "
        "code spreads the signal energy across a wider band."
    )

    E["E8D03"] = (
        "Frequency hopping spread spectrum rapidly changes the transmit frequency according to a pseudorandom pattern. "
        "Both ends follow the same hopping sequence so they stay synchronized."
    )

    E["E8D04"] = (
        "Very short rise and fall times make the CW waveform abrupt, which produces key clicks. Those sharp transitions "
        "spread energy widely and create interference outside the intended channel."
    )

    E["E8D05"] = (
        "The usual way to reduce key clicks is to lengthen the rise and fall times of the keying waveform. Smoother edges "
        "mean less wideband energy and fewer clicks."
    )

    E["E8D06"] = (
        "Parity bits let the receiver check whether the number of 1s is even or odd, so some transmission errors can be "
        "detected. They do not correct every error, but they provide a simple error check."
    )

    E["E8D07"] = (
        "AFSK overmodulation usually happens when the audio drive level is too high. Too much audio pushes the modulator "
        "past its linear range and distorts the transmitted tones."
    )

    E["E8D08"] = (
        "Intermodulation distortion is the metric used to judge how badly excessive audio levels are distorting an AFSK "
        "signal. Higher IMD means the tones are mixing into unwanted products."
    )

    E["E8D09"] = (
        "For an idling PSK signal, the unwanted intermodulation products should be at least 30 dB below the main signal. "
        "That is why -30 dB is the acceptable maximum IMD level."
    )

    E["E8D10"] = (
        "Baudot uses 5 data bits per character and relies on letters/figures shift codes, while ASCII uses 7 or 8 bits "
        "and can represent uppercase, lowercase, and many more symbols."
    )

    E["E8D11"] = (
        "ASCII can represent both uppercase and lowercase text, which is one of its big advantages for data communications. "
        "The larger character set makes it more flexible than older 5-bit codes."
    )

    # ── E8C — Digital Signals ───────────────────────────────────

    E["E8C02"] = (
        "Symbol rate is the rate at which the transmitted waveform changes state to convey information. "
        "It is measured in symbols per second, or baud."
    )

    E["E8C03"] = (
        "Changing PSK phase at a zero crossing avoids abrupt amplitude discontinuities and keeps the signal "
        "spectrally cleaner. The result is less splatter, so the occupied bandwidth stays as small as possible."
    )

    E["E8C04"] = (
        "PSK31 minimizes bandwidth by shaping the symbols with sinusoidal data pulses. Smooth symbol edges "
        "reduce keying sidebands and keep the signal much narrower than a hard-switched waveform would be."
    )

    E["E8C05"] = (
        "Morse code bandwidth is very narrow because the keyed signal is slow and its transitions are shaped by "
        "the sending speed. At about 13 WPM, the occupied bandwidth is roughly 4 times the WPM rate, or about 52 Hz."
    )

    E["E8C06"] = (
        "FT8 occupies about 50 Hz because it uses a very narrow 8-tone digital signal with closely spaced symbols. "
        "Its design prioritizes weak-signal robustness rather than throughput, so the occupied bandwidth stays tiny."
    )

    E["E8C07"] = (
        "A 9600-baud signal with a 4800-Hz shift needs bandwidth for both the symbol rate and the tone separation. "
        "When you apply the standard FSK bandwidth estimate, the result is about 15.36 kHz."
    )

    E["E8C08"] = (
        "ARQ detects that an error occurred and then asks for the data to be sent again. The retransmission request "
        "is what makes the error correction automatic from the user’s point of view."
    )

    E["E8C09"] = (
        "Gray code is the code where only one bit changes between adjacent values. That minimizes transition errors "
        "in encoders and makes the code easier to read during a single-step change."
    )

    E["E8C10"] = (
        "You can raise data rate without widening the signal by packing more information into each symbol. Using a more "
        "efficient digital code increases throughput while keeping the occupied bandwidth the same."
    )

    E["E8C11"] = (
        "Baud is simply symbol rate, so the two terms mean the same thing. If a system sends 100 symbols per second, "
        "its rate is 100 baud."
    )

    E["E8C12"] = (
        "CW bandwidth depends on how fast the keying changes and how gently the waveform rises and falls. Faster keying "
        "and sharper edges spread more energy into the sidebands, widening the signal."
    )

    E["E8C13"] = (
        "A constellation diagram shows the allowed phase and amplitude states for each symbol in a QAM or QPSK signal. "
        "Each dot represents one symbol location in the complex plane."
    )

    E["E8C14"] = (
        "Mesh network nodes use Internet Protocol addresses so they can route packets like normal IP devices. The mesh "
        "layers routing on top of standard network addressing."
    )

    E["E8C15"] = (
        "Individual mesh nodes discover each other and establish links using discovery and link-establishment protocols. "
        "That lets the network self-form without manually wiring every route."
    )

    # ── E4C/E/D/E — Receiver Performance and Interference ────────

    E["E4C13"] = (
        "Reciprocal mixing happens when local-oscillator phase noise combines with a strong nearby "
        "signal and produces interference in the desired receive channel. It is a receiver noise-floor "
        "problem, not ordinary two-signal intermodulation inside the front end."
    )

    E["E4C14"] = (
        "The IF Shift control moves the receiver passband relative to the tuned signal so you can "
        "avoid interference from adjacent stations. It shifts the filter position in the IF chain "
        "without changing the transmitted frequency."
    )

    E["E4D12"] = (
        "Convert the pieces to dB, then compare received level to required level. 10 W is +40 dBm; "
        "adding 10 dBi antenna gain gives +50 dBm, and subtracting 3 dB cable loss leaves +47 dBm "
        "at the antenna. With 136 dB of path loss, the received level is -89 dBm. The receiver needs "
        "-103 dBm plus 6 dB SNR, or -97 dBm, so the link margin is +8 dB."
    )

    E["E4D13"] = (
        "Add the transmit power and gains, then subtract the path loss. 10 W is +40 dBm; plus 6 dBi "
        "transmit gain and 3 dBi receive gain gives +49 dBm before propagation. Subtracting 100 dB "
        "of path loss leaves -51 dBm at the receiver."
    )

    E["E4D14"] = (
        "0 dBm is 1 milliwatt, so -100 dBm is 10⁻¹³ watts. That equals 0.1 picowatts, which is the "
        "correct tiny signal level for a receiver minimum discernible signal."
    )

    E["E4E12"] = (
        "Switch-mode power supplies switch at a fixed frequency and create a comb of harmonics across "
        "a wide range of HF and VHF frequencies. Those regularly spaced carriers are the classic signature "
        "of an SMPS or similar switching device."
    )

    E["E4E13"] = (
        "The AC surge protector belongs on the single-point ground panel so the protected AC path ties "
        "into the same grounding system as the rest of the station. That keeps the surge reference and "
        "the equipment reference at one common point."
    )

    E["E4E14"] = (
        "A single-point ground panel ties all station grounds and protectors to one common reference point. "
        "That way, a lightning transient is clamped by the same grounding system everywhere instead of "
        "finding different potentials between pieces of gear."
    )

    # ── E3A/B/C — Radio Wave Propagation ────────────────────────

    E["E3A14"] = (
        "Circular polarization means the electric and magnetic fields rotate as the wave propagates, tracing a circle "
        "over one RF cycle. The rotation can be right-hand or left-hand. It is the field orientation that rotates, "
        "not the wave path around Earth."
    )

    E["E3B12"] = (
        "Chordal-hop propagation uses a series of ionospheric refractions without a ground reflection between hops. "
        "The signal bends from layer to layer in the ionosphere instead of taking an intermediate bounce from the earth."
    )

    E["E3B13"] = (
        "Ground-wave propagation works best with vertical polarization. Vertical antennas couple to the surface wave "
        "and keep the field component that hugs the earth, while horizontal polarization is absorbed more readily by the ground."
    )

    E["E3C12"] = (
        "A sudden rise in HF background noise across a wide range usually means the Sun has disturbed the ionosphere, "
        "such as from a solar flare or a coronal mass ejection impact. Those events raise ionization and absorption and make the whole band sound noisy."
    )

    # ── E2E — Operating HF Digital Modes ─────────────────────────

    E["E2E13"] = (
        "PACTOR IV has the highest data throughput of the listed modes. It is designed for faster, more robust HF data "
        "transfer than MFSK16, narrow-shift RTTY, or FT8. Under clear conditions, the wider and more sophisticated mode can move more data per second."
    )

    # fmt: on


RULE_CITATION_RE = re.compile(r"^\[[^\]]+\]\s*")


def build_fallback_explanation(q: dict) -> str:
    """Generate a safe explanation that always matches the current question."""
    answer = q["answers"][q["correct"]]
    question = RULE_CITATION_RE.sub("", q["question"]).strip()
    q_lower = question.lower()

    if answer == "All these choices are correct":
        return f"All of the listed choices are correct for this question."

    if q_lower.startswith(("what is ", "what are ")):
        return f"The correct answer is {answer}."

    if q_lower.startswith(("what does ", "which term", "what term")):
        return f"{answer} is the correct term or definition for this question."

    if q_lower.startswith(("which of the following", "which frequency", "which band", "what type")):
        return f"The correct choice here is {answer}."

    if q_lower.startswith(("where ", "when ", "how ", "why ")):
        return f"The correct answer is {answer}."

    return f"The correct answer is {q['correct']}) {answer}."


def _merge_preserved_explanations() -> int:
    """Load preserved explanation blocks from the staging file."""
    namespace = runpy.run_path(str(PRESERVED_EXPLANATIONS_PATH))
    preserved = namespace.get("E", {})

    if not isinstance(preserved, dict):
        raise SystemExit("scripts/new-explanations.py did not define an E dict")

    overlap = sorted(set(EXPLANATIONS).intersection(preserved))
    if overlap:
        raise SystemExit(f"duplicate explanation keys in preserved merge: {', '.join(overlap)}")

    EXPLANATIONS.update(preserved)
    return len(preserved)


def _backfill_missing_explanations(questions: list[dict]) -> int:
    """Fill any remaining questions with a safe fallback explanation."""
    added = 0
    for q in questions:
        qid = q["id"]
        if qid not in EXPLANATIONS:
            EXPLANATIONS[qid] = build_fallback_explanation(q)
            added += 1
    return added


def validate_explanations(questions: list[dict]) -> None:
    """Fail fast if the explanation map drifts from the question pool."""
    question_ids = {q["id"] for q in questions}
    explanation_ids = set(EXPLANATIONS)
    missing = sorted(question_ids - explanation_ids)
    orphaned = sorted(explanation_ids - question_ids)

    if missing or orphaned or len(EXPLANATIONS) != len(question_ids):
        issues = []
        if len(EXPLANATIONS) != len(question_ids):
            issues.append(
                f"expected {len(question_ids)} explanations, found {len(EXPLANATIONS)}"
            )
        if missing:
            issues.append(f"missing explanation keys: {', '.join(missing)}")
        if orphaned:
            issues.append(f"orphan explanation keys: {', '.join(orphaned)}")
        raise SystemExit("; ".join(issues))


def load_pool() -> dict:
    """Load the 2024-2028 pool JSON."""
    with open(POOL_PATH) as f:
        return json.load(f)


def group_questions(questions: list[dict]) -> dict[str, dict[str, list[dict]]]:
    """Group questions by subelement and then by group.

    Returns: {subelement: {group: [question, ...]}}
    """
    result: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for q in questions:
        result[q["subelement"]][q["group"]].append(q)
    return result


def format_question(q: dict) -> str:
    """Format a single question as markdown."""
    lines = [f"### {q['id']}"]
    # Strip rule citations from question text for cleaner display
    question_text = RULE_CITATION_RE.sub("", q["question"]).strip()
    lines.append(f"**{question_text}**")

    for letter in ("A", "B", "C", "D"):
        text = q["answers"].get(letter, "")
        if not text:
            continue
        if letter == q["correct"]:
            lines.append(f"- **{letter}) {text}** ✅")
        else:
            lines.append(f"- {letter}) {text}")

    explanation = EXPLANATIONS.get(q["id"], "")
    if not explanation:
        explanation = build_fallback_explanation(q)
    lines.append("")
    lines.append(f"> {explanation}")

    return "\n".join(lines)


def generate_subelement_file(
    subelement: str,
    name: str,
    exam_questions: int,
    pool_size: int,
    groups: dict[str, list[dict]],
) -> str:
    """Generate the full markdown file for one subelement."""
    lines = [f"# {subelement} — {name}"]
    lines.append(f"*{exam_questions} questions on the exam from a pool of {pool_size}*")
    lines.append("")

    for group_id in sorted(groups.keys()):
        desc = GROUP_DESCRIPTIONS.get(group_id, group_id)
        lines.append(f"## Group {group_id} — {desc}")
        lines.append("")

        for q in groups[group_id]:
            lines.append(format_question(q))
            lines.append("")

    return "\n".join(lines)


def main() -> None:
    pool = load_pool()
    _load_explanations()
    merged = _merge_preserved_explanations()
    backfilled = _backfill_missing_explanations(pool["questions"])

    print(
        f"Merged {merged} preserved explanations; backfilled {backfilled} fallback explanations"
    )

    all_questions = pool["questions"]
    validate_explanations(all_questions)

    subelements_meta = pool["subelements"]
    grouped = group_questions(all_questions)

    OUTPUT_DIR.mkdir(exist_ok=True)

    generated = 0
    for sub_id, groups in sorted(grouped.items()):
        meta = subelements_meta.get(sub_id, {})
        name = meta.get("name", sub_id)
        exam_qs = meta.get("exam_questions", 0)
        pool_size = meta.get("pool_size", sum(len(qs) for qs in groups.values()))

        file_stem = SUBELEMENT_FILES.get(sub_id)
        if not file_stem:
            print(f"WARNING: No file mapping for subelement {sub_id}", file=sys.stderr)
            continue

        content = generate_subelement_file(sub_id, name, exam_qs, pool_size, groups)
        out_path = OUTPUT_DIR / f"{file_stem}-questions.md"
        out_path.write_text(content)
        print(f"  ✓ {out_path.name} ({pool_size} questions)")
        generated += 1

    print(f"\nDone — {generated} subelement file(s) generated.")


if __name__ == "__main__":
    main()
