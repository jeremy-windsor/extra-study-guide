# Amateur Extra Class — 7-Day Study Plan

A structured plan to prepare for the FCC Amateur Extra class exam in one week. This assumes you already hold a General class license and are comfortable with HF operating, basic electronics, and propagation fundamentals.

## Before You Start

**What you need:**
- This study guide (you're reading it)
- The [PWA Study App](https://jeremy-windsor.github.io/extra-study-guide/apps/study-app/) on your phone or desktop
- A quiet 2–3 hours each day
- Optionally: the MP3 audio files for listening during commutes or workouts

**Coming from General?** The Extra exam is a significant step up. Where General tested whether you understand HF operating and basic electronics, Extra tests whether you can *analyze and design*. Expect more math (complex impedance, Smith charts, filter design), deeper circuit theory (op-amps, mixers, PLLs), and detailed antenna engineering. The rules section is trickier too — you need to know satellite operations, spread spectrum restrictions, and international agreements at a level General didn't require.

Start with [What You Should Already Know](GENERAL-BRIDGE.md) — a quick refresher on General-class concepts the Extra exam builds on. If you can answer the self-test questions at the end without looking them up, you're ready to begin.

---

## How This Plan Works

Each day covers one or two subelements. The pattern:

1. **Read the narrative guide** — learn the concepts, not just the answers
2. **Drill the question bank** — use the PWA to work through every question in the section
3. **Review weak areas** — the PWA tracks what you miss; revisit those
4. **Start Day 4+:** take at least one practice exam per day

The exam draws **50 questions** from a pool of **599**. You need **37 correct (74%)** to pass. The questions are weighted by subelement — E7 and E9 each contribute 8 questions (16% of the exam each), while E0 contributes only 1.

### Where the Points Are

| Subelement | Exam Questions | % of Exam | Priority |
|:-----------|:--------------:|:---------:|:--------:|
| E7 — Practical Circuits | 8 | 16% | 🔴 High |
| E9 — Antennas & Transmission Lines | 8 | 16% | 🔴 High |
| E1 — Commission's Rules | 6 | 12% | 🟡 Medium |
| E6 — Circuit Components | 6 | 12% | 🟡 Medium |
| E2 — Operating Procedures | 5 | 10% | 🟡 Medium |
| E4 — Amateur Practices | 5 | 10% | 🟡 Medium |
| E5 — Electrical Principles | 4 | 8% | 🟢 Standard |
| E8 — Signals & Emissions | 4 | 8% | 🟢 Standard |
| E3 — Radio Wave Propagation | 3 | 6% | 🟢 Standard |
| E0 — Safety | 1 | 2% | 🟢 Light |

If you're short on time, bias your review toward **E7, E9, E1, and E6** — those four sections account for **56% of the exam**.

---

## Day 1: Rules & Safety (~2 hours)

> 📋 **Rusty on General material?** Read [What You Should Already Know](GENERAL-BRIDGE.md) first (5 min audio, 10 min reading).

**Goal:** Know your Extra-class privileges, operating restrictions, and safety requirements.

| Activity | Time | Resource |
|----------|------|----------|
| Read bridge refresher | 10 min | `GENERAL-BRIDGE.md` |
| Read E1 narrative | 30 min | `subelements/E1-commission-rules.md` |
| Drill E1 questions | 50 min | PWA → Study by Section → E1 |
| Read E0 narrative | 10 min | `subelements/E0-safety.md` |
| Drill E0 questions | 10 min | PWA → Study by Section → E0 |
| Review missed questions | 10 min | PWA → Weak Areas |

**Focus areas:**
- Extra-only frequency segments on 80m, 40m, 20m, 15m — know the exact boundaries
- 60m channelized operation (5 channels, 100W ERP, USB/data, 2.8 kHz max BW for data)
- 2200m (1W EIRP) and 630m (5W EIRP) — EIRP limits, UTC notification, 30-day wait
- Spread spectrum only above 222 MHz
- Remote control failure: max 3 minutes transmit
- Space operation: telemetry vs. telecommand, only space telecommand may be encrypted
- Below 30 MHz: spurious emissions at least 43 dB below fundamental
- RF exposure: 30–300 MHz is the most restrictive range; 80m always requires evaluation
- Shared site: 5% MPE contribution triggers shared mitigation responsibility

**General bridge:** You know Part 97 basics and VE requirements. Extra adds satellite rules, spread spectrum restrictions, low-frequency bands, and deeper exposure calculations.

---

## Day 2: Operating Procedures & Propagation (~2.5 hours)

**Goal:** Master satellite operation, digital modes, and propagation theory.

| Activity | Time | Resource |
|----------|------|----------|
| Read E2 narrative | 30 min | `subelements/E2-operating-procedures.md` |
| Drill E2 questions | 35 min | PWA → Study by Section → E2 |
| Read E3 narrative | 20 min | `subelements/E3-radio-wave-propagation.md` |
| Drill E3 questions | 20 min | PWA → Study by Section → E3 |
| Review missed questions | 15 min | PWA → Weak Areas |
| Review cram sheet sections | 10 min | `CRAM-SHEET.md` — E2/E3 anchors |

**Focus areas:**
- Satellite designators: mode = uplink/downlink band pair (not modulation type)
- Linear transponders: bent-pipe, shared passband; too much uplink ERP steals downlink from everyone
- Inverting linear transponder flips sideband (USB up → LSB down)
- L band (23 cm) / S band (13 cm) satellite terminology
- APRS: AX.25 UI frames; WIDE3-1 means 3 hops requested, 1 remaining
- Weak-signal: MSK144 (meteor scatter), Q65 (EME), JT65, WSPR (beaconing only)
- VHF FT8/FT4 contest exchange: grid square
- Tropospheric ducting: over water, 100–300 miles
- Transequatorial propagation (TEP): afternoon/evening, 2000–3000 miles, crosses geomagnetic equator
- Sporadic E: solstice season, daytime, E region
- EME: best at perigee, libration fading
- Solar: X-class strongest flare, G5 extreme storm, southward Bz = trouble
- Long-path most common on 40m and 20m

**General bridge:** You know basic ionospheric propagation from G3. Extra adds EME, meteor scatter, TEP, chordal hops, and detailed solar indices. The satellite material is entirely new.

---

## Day 3: Amateur Practices (~2 hours)

**Goal:** Understand test equipment, receiver design, and station measurements.

| Activity | Time | Resource |
|----------|------|----------|
| Read E4 narrative | 35 min | `subelements/E4-amateur-practices.md` |
| Drill E4 questions | 45 min | PWA → Study by Section → E4 |
| Review missed questions | 15 min | PWA → Weak Areas |
| Take first practice exam | 20 min | PWA → Practice Exam |

**Focus areas:**
- Oscilloscope: voltage vs. time; spectrum analyzer: amplitude vs. frequency
- VNA: S11 (input reflection/return loss), S21 (forward transmission/gain)
- Calibration standards: open, short, 50Ω load
- Noise figure: how much worse the receiver is than ideal thermal noise
- MDS (minimum discernible signal)
- Phase noise + strong nearby signal → reciprocal mixing
- Preselector / front-end filter: reject out-of-band before overload
- ADC overload in SDR: signal exceeds reference voltage range
- High IF makes image rejection easier
- Roofing filter improves blocking dynamic range (noise floor to 1 dB compression)
- Intermodulation: 2f1−f2 and 2f2−f1 are the trouble products
- Higher IP3 = better strong-signal handling
- Common-mode current makes cables radiate/receive when they shouldn't
- Analog voltmeter sensitivity: ohms per volt

**General bridge:** You know basic SWR meters and dummy loads. Extra demands understanding of S-parameters, dynamic range, noise figure calculations, and receiver architecture at block-diagram level.

**First practice exam:** Don't stress about the score. This sets your baseline and tells the PWA where to focus your review time.

---

## Day 4: Electrical Principles (~2.5 hours)

**Goal:** Master the math — complex impedance, reactance, resonance, and power calculations.

| Activity | Time | Resource |
|----------|------|----------|
| Read E5 narrative | 25 min | `subelements/E5-electrical-principles.md` |
| Drill E5 questions | 60 min | PWA → Study by Section → E5 |
| Review formulas | 15 min | `CRAM-SHEET.md` — Core Circuit Math + RF Math |
| Review missed questions | 15 min | PWA → Weak Areas |
| Practice exam | 20 min | PWA → Practice Exam |

**Focus areas:**
- **Series resonance:** minimum impedance, maximum current, voltage across L or C = Q × applied
- **Parallel resonance:** maximum impedance, minimum source current
- Q = f₀/bandwidth; Q(series) = X/R; Q(parallel) = R/X
- RC time constant τ = RC; 63.2% at 1τ, 99.3% at 5τ
- Phase angle θ = arctan((XL − XC)/R) in series RLC
- Admittance Y = 1/Z = G + jB
- Rectangular form: R + jX (positive = inductive, negative = capacitive)
- Polar form: |Z|∠θ
- Skin effect: RF current → surface as frequency rises
- Self-resonance: component's intended reactance resonates with parasitic
- Real power = I²R; apparent power S = VI; S² = P² + Q²
- Thermal noise floor: −174 dBm/Hz at room temperature
- Noise rise = 10·log₁₀(bandwidth ratio)

**This is the math day.** Extra-level electrical theory is calculation-heavy. Work every problem — don't skip the math. The cram sheet's formula section is your best friend here. If you can calculate Q, bandwidth, phase angle, and power triangle values without looking at formulas, you've got this section.

**General bridge:** You know impedance and basic resonance. Extra adds complex notation (rectangular/polar), admittance, skin effect, thermal noise, and the power triangle. This is the biggest conceptual jump from General.

---

## Day 5: Components & Practical Circuits (~3.5 hours)

**Goal:** Understand component types, circuit topologies, and common building blocks.

> ⚠️ **This is the heaviest day.** E7 alone has 99 pool questions (8 on the exam). Plan for a longer session or split across two sittings.

| Activity | Time | Resource |
|----------|------|----------|
| Read E6 narrative | 35 min | `subelements/E6-circuit-components.md` |
| Drill E6 questions | 50 min | PWA → Study by Section → E6 |
| Read E7 narrative | 55 min | `subelements/E7-practical-circuits.md` |
| Drill E7 questions | 75 min | PWA → Study by Section → E7 |
| Review missed questions | 15 min | PWA → Weak Areas |

**E6 focus areas:**
- N-type (donor) vs. P-type (acceptor) semiconductors
- GaAs = high electron mobility (UHF/microwave); GaN = highest MMIC frequency
- BJT beta = ΔIc/ΔIb; depletion-mode FET = normally on
- PIN diode = RF switch/attenuator (DC bias controls attenuation)
- Varactor = voltage-controlled capacitance
- Schottky = metal-semiconductor, low forward voltage, fast RF
- Ferrite core: fewer turns, VHF/UHF suppression; powdered iron: better temp stability
- Brass slug decreases inductance
- Toroid: magnetic field stays inside
- Crystal: piezoelectric resonator

**E7 focus areas:**
- Flip-flop divides by 2; 4 flip-flops = divide by 16; decade counter = divide by 10
- Monostable = one-shot; astable = oscillator; bistable = memory
- Amplifier classes: A (360°, best linearity, worst efficiency), B (180°, crossover distortion), AB (compromise), C (<180°, nonlinear, not for SSB), D (switching, efficient)
- Emitter follower (common collector): output in phase, low Zout, buffer
- Pi network: shunt C → series L → shunt C (low-pass); pi-L adds extra L for more harmonic suppression
- Butterworth = flat; Chebyshev = ripple + sharper; elliptical = sharpest + notches
- Linear regulator: varies conduction; switching regulator: varies duty cycle
- Colpitts = capacitive divider; Hartley = inductive divider; Pierce = crystal
- PLL: phase detector → LPF → VCO
- DDS: phase accumulator → lookup table → DAC → LPF (main impurity: discrete spurs)
- Balanced modulator + filter = SSB; product detector = SSB receiver
- Mixer: outputs f1, f2, f1+f2, f1−f2; overdriven mixer = spurious products

**General bridge:** You know basic components (resistors, caps, diodes, transistors). Extra requires detailed knowledge of RF-specific parts (PIN diodes, varactors, MMICs) and circuit blocks (mixers, PLLs, DDS, modulators, detectors).

---

## Day 6: Signals, Emissions & Antennas (~3.5 hours)

**Goal:** Understand modulation theory, digital encoding, antenna patterns, and transmission line matching.

> ⚠️ **Second heaviest day.** E9 has 93 pool questions (8 on the exam). Plan accordingly.

| Activity | Time | Resource |
|----------|------|----------|
| Read E8 narrative | 35 min | `subelements/E8-signals-emissions.md` |
| Drill E8 questions | 40 min | PWA → Study by Section → E8 |
| Read E9 narrative | 50 min | `subelements/E9-antennas-transmission-lines.md` |
| Drill E9 questions | 75 min | PWA → Study by Section → E9 |
| Review missed questions | 15 min | PWA → Weak Areas |
| Practice exam | 20 min | PWA → Practice Exam |

**E8 focus areas:**
- FM modulation index β = deviation/modulating frequency
- Deviation ratio = max deviation/max audio frequency
- OFDM: many orthogonal subcarriers; FDM: different frequencies simultaneously; TDM: same channel, different time slots
- Baud = symbol rate; QAM uses both amplitude and phase
- SAR ADC: binary search; flash ADC: very high speed
- Dither: small noise that reduces quantization artifacts
- SSB speech PEP/average ≈ 2.5:1
- PSK31: sinusoidal pulses at zero crossings for narrow bandwidth
- ARQ: error handling via retransmission request
- DSSS: high-speed code spreads waveform; FHSS: hops frequencies in pseudorandom pattern
- Acceptable PSK IMD: −30 dB or better
- Key clicks: fix by lengthening CW rise/fall times

**E9 focus areas:**
- dBi = dBd + 2.15; use dBd for ERP, dBi for EIRP
- Antenna gain *redistributes* power — does not increase total radiated power
- Efficiency = Rrad/(Rrad + Rloss)
- Azimuth = compass direction; elevation = takeoff angle; 3 dB beamwidth = half-power
- Front-to-back (forward vs. directly behind) vs. front-to-side (forward vs. side)
- Method of Moments = NEC-style wire segmentation; <10 segments per half-wavelength spoils impedance
- Two verticals, λ/2 apart, in phase → broadside figure-8; 180° out of phase → end-fire figure-8; λ/4 apart, 90° → cardioid
- Folded dipole ≈ 300Ω; parabolic: +6 dB when frequency doubles (same dish)
- Gamma match: unbalanced, grounded, series cap cancels inductive reactance
- Beta/hairpin match: balanced, insulated from boom, inductive hairpin cancels capacitive reactance
- Quarter-wave transformer: Z = √(Z1·Z2)
- Half-wave line repeats load impedance; quarter-wave line inverts it
- Shorted stub < λ/4 = inductive; open stub < λ/4 = capacitive
- Velocity factor: foam coax (higher VF, lower loss, lower breakdown) vs. solid polyethylene (VF ≈ 0.66)
- Smith chart: center = perfect match (1+j0); above center = inductive; below = capacitive
- Beverage: long, low, terminated, directional, at least 1λ; RDF measures receive performance
- Small loop: deep nulls, 180° ambiguity; sense antenna resolves to cardioid

**General bridge:** You know dipoles, SWR, and basic feed lines. Extra adds phased arrays, matching networks, Smith chart navigation, transmission line impedance transformation, and specialized receiving antennas.

---

## Day 7: Review & Exam Prep (~2–3 hours)

**Goal:** Cement everything. Identify and fix remaining weak spots.

| Activity | Time | Resource |
|----------|------|----------|
| Read cram sheet | 20 min | `CRAM-SHEET.md` or listen to `CRAM-SHEET.mp3` (31 min) |
| Practice exam #1 | 20 min | PWA → Practice Exam |
| Review weak areas | 30 min | PWA → Weak Areas (focus on sections you missed) |
| Practice exam #2 | 20 min | PWA → Practice Exam |
| Practice exam #3 | 20 min | PWA → Practice Exam |
| Final weak area review | 20 min | Re-read narrative sections for any remaining trouble spots |
| Re-read cram sheet | 10 min | Last pass before exam day |

**Scoring targets:**
- If you're consistently scoring **42+/50 (84%+)**, you're ready
- If you're scoring **37–41 (74–82%)**, focus your review on your weakest 2–3 subelements
- If you're scoring **below 37**, go back to the narrative guides for the sections dragging you down and re-drill the question banks

**Exam day tips:**
- Read the cram sheet one more time before walking in
- There's no time limit — work through every question carefully
- Skip and come back to math questions; answer the easy ones first to build confidence
- If you can narrow it to two choices, guess — there's no penalty for wrong answers
- Bring a non-programmable calculator (the exam does not provide one)

---

## Alternative: 10-Day Plan

If you have more time and want a gentler pace, split the heavy days:

| Day | Content |
|-----|---------|
| 1 | Bridge refresher + E1 Rules |
| 2 | E0 Safety + E2 Operating |
| 3 | E3 Propagation + practice exam |
| 4 | E4 Amateur Practices |
| 5 | E5 Electrical Principles |
| 6 | E6 Circuit Components + practice exam |
| 7 | E7 Practical Circuits |
| 8 | E8 Signals & Emissions + practice exam |
| 9 | E9 Antennas & Transmission Lines |
| 10 | Review: cram sheet + 3 practice exams |

---

## Audio Study Schedule

If you learn by listening, here's how to fit the audio into your week:

| Day | Listen To | Duration |
|-----|-----------|----------|
| 1 | E1 narrative → E1 questions | 69 min |
| 2 | E2 narrative → E2 questions → E3 narrative | 72 min |
| 3 | E3 questions → E4 narrative | 51 min |
| 4 | E5 narrative → E5 questions | 75 min |
| 5 | E6 narrative → E6 questions → E7 narrative | 125 min |
| 6 | E7 questions → E8 narrative | 107 min |
| 7 | E8 questions → E9 narrative → cram sheet | 113 min |

Total: ~10 hours of audio across the week. Perfect for commutes, workouts, or chores.

---

## Good Luck

The Extra exam is the hardest of the three amateur radio licenses, but it's completely beatable with focused study. The question pool is public, every answer is knowable, and you've already proven you can pass a license exam (twice). This is the last one.

> 💡 **One last thing:** Add the [study app](https://jeremy-windsor.github.io/extra-study-guide/apps/study-app/) to your phone's home screen. Five minutes of flashcards while waiting in line adds up over a week.
