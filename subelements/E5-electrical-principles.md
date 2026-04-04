# E5 — Electrical Principles

You've been through Technician and General. You know Ohm's Law, you've worked with RLC circuits, you understand that reactance is the AC version of resistance. Now in Extra we go deeper — into the math that makes RF circuits actually work.

This subelement covers four groups: resonance and Q (E5A), time constants and phase angles (E5B), impedance representation (E5C), and parasitic effects with real vs. reactive power (E5D). The exam pulls 4 questions from this pool of 49.

The concepts here aren't abstract — every filter, every impedance-matching network, every antenna system depends on this material. Let's build real understanding.

---

## Group E5A — Resonance and Q

### Series vs. Parallel Resonance

In General, you learned that resonance happens when X_L = X_C. In Extra, we care about *what that means* in series vs. parallel circuits — because they behave oppositely.

**Series RLC at resonance:**
- X_L = X_C, so net reactance = 0
- Impedance = R (minimum)
- Current = maximum (V/R)
- Voltage across L or C = Q × applied voltage (can be much larger than source!)

**Parallel RLC at resonance:**
- X_L = X_C, so circulating currents cancel
- Impedance = R (maximum — purely resistive)
- Current from source = minimum
- Circulating current inside the tank = Q × source current

The inversion is the key insight: **series resonance = minimum impedance, maximum current; parallel resonance = maximum impedance, minimum current.** Both circuits are purely resistive at resonance — all the reactance cancels.

### Voltage Magnification in Series Circuits

Here's the thing General didn't fully emphasize: at resonance in a series circuit, the voltage across the inductor (and the capacitor) isn't just the applied voltage — it's Q times the applied voltage.

If you apply 10V to a series RLC at resonance with Q = 50, the voltage across the inductor alone is 500V. The voltage across the capacitor is also 500V. These enormous voltages are equal and exactly opposite, so they cancel in the series path — the net voltage is still 10V. But each component individually has huge voltage across it.

This voltage magnification is both useful (crystal filters, oscillator tank circuits) and dangerous (capacitor breakdown in high-Q resonant power circuits).

### Resonant Frequency Calculation

The formula you need cold:

**f = 1 / (2π√(LC))**

Where f is in hertz, L is in henrys, C is in farads.

Notice what's NOT in this formula: resistance. R has no effect on resonant frequency — it only affects Q and bandwidth.

**Worked example (E5A02):** L = 50 µH, C = 40 pF
- LC = 50×10⁻⁶ × 40×10⁻¹² = 2×10⁻¹⁵
- √(LC) = 4.47×10⁻⁸
- f = 1 / (2π × 4.47×10⁻⁸) ≈ 3.56 MHz

**Worked example (E5A10):** L = 50 µH, C = 10 pF
- C is ¼ as large, so f is 2× higher (f ∝ 1/√C)
- f ≈ 3.56 × 2 = 7.12 MHz

### Q Factor: Quality Factor

Q is the quality factor. It measures how "sharp" or "selective" a resonant circuit is. There are several equivalent definitions:

- **Series circuit:** Q = X_L / R (reactance divided by resistance at resonance)
- **Parallel circuit:** Q = R / X_L (resistance divided by reactance)
- **In general:** Q = energy stored / energy dissipated per cycle

High Q = sharp resonance, narrow bandwidth, low losses, high selectivity.
Low Q = broad resonance, wide bandwidth, high losses, less selective.

The series and parallel formulas are inverses — a high-Q parallel tank has high R relative to X (low losses), while a high-Q series circuit has high X relative to R (high voltage magnification).

### Half-Power Bandwidth

The bandwidth of a resonant circuit (at the -3 dB, half-power points) is:

**BW = f_r / Q**

This is one of the most useful formulas in RF design. Higher Q = narrower bandwidth = more selective.

**Worked example (E5A11):** f_r = 7.1 MHz, Q = 150
- BW = 7,100,000 / 150 = 47,333 Hz ≈ **47.3 kHz**

**Worked example (E5A12):** f_r = 3.7 MHz, Q = 118
- BW = 3,700,000 / 118 = 31,356 Hz ≈ **31.4 kHz**

Note the direct consequence: increasing Q narrows bandwidth (E5A05, E5A13). In a series resonant circuit, higher Q means larger internal voltages (V_L = Q × V_applied) and narrower bandwidth. Both effects together.

### Phase Relationships at Resonance

At resonance in a series RLC circuit, V and I are exactly in phase — zero degrees phase shift. Below resonance the circuit is capacitive (I leads V); above resonance it's inductive (V leads I). At the resonant frequency, reactances cancel and the circuit appears purely resistive.

---

## Group E5B — Time Constants and Phase Angles

### RC Time Constants

You saw time constants in General. Extra expects you to use them confidently.

**τ = R × C** (in seconds, with R in ohms and C in farads)

The time constant τ is the time for a capacitor to charge to **63.2%** of the applied voltage. Where does 63.2% come from? The charging equation is V(t) = V_final × (1 - e^(-t/τ)). At t = τ: V = V_final × (1 - e^(-1)) = V_final × 0.632.

**Five time constants** to charge to 99.3% — consider this "fully charged."

For discharge: one time constant = discharge to 36.8% (= 100% - 63.2%) of initial voltage.

**Watch out on E5B04:** Two 220 µF capacitors and two 1 MΩ resistors all in **parallel**:
- Parallel capacitors add: 220 + 220 = 440 µF
- Parallel resistors halve: 1 MΩ || 1 MΩ = 0.5 MΩ
- τ = 500,000 × 440×10⁻⁶ = **220 seconds**

If they were in series: C_series = 110 µF, R_series = 2 MΩ, τ = 220 seconds too — same answer! (That's a coincidence of halving capacitance and doubling resistance.) Read the question carefully.

### Admittance and Susceptance

In General you learned impedance (Z = R + jX). Admittance is the inverse:

**Y = 1/Z** (admittance, in siemens)

Just as impedance has real (R) and imaginary (X) parts, admittance has:
- **G** = conductance (real part, inverse of resistance)
- **B** = susceptance (imaginary part, inverse of reactance)

Written out: **Y = G + jB**

The letter for susceptance is **B** (not to be confused with G for conductance or Y for admittance).

Why does admittance matter? For parallel circuits, admittances add directly — just like conductances add for parallel resistors. It's easier to work in admittance when analyzing parallel networks.

**Converting impedance to susceptance:**
If a reactance has magnitude X, its susceptance magnitude is **1/X** (the reciprocal). The sign also inverts in the complex sense — but the key fact for the exam is that the magnitude becomes the reciprocal.

### Polar Form Conversion

Impedance in polar form Z∠θ converts to admittance as:
- **Take the reciprocal of the magnitude**
- **Change the sign of the angle**

Z = 50∠+30° → Y = (1/50)∠(-30°) = 0.02∠-30°

This follows directly from Y = 1/Z = 1/(|Z|∠θ) = (1/|Z|)∠(-θ).

### Phase Angles in Series RLC Circuits

The phase angle between voltage and current in a series RLC:

**θ = arctan((X_L - X_C) / R)**

Rules of sign:
- **X_L > X_C** → positive angle → net inductive → voltage LEADS current
- **X_C > X_L** → negative angle → net capacitive → current LEADS voltage (voltage LAGS)

**E5B07 example:** X_C = 500 Ω, R = 1000 Ω, X_L = 250 Ω
- θ = arctan((250 - 500)/1000) = arctan(-0.25) = **-14.0°**
- Net capacitive: voltage lags current by 14°

**E5B08 example:** X_C = 300 Ω, R = 100 Ω, X_L = 100 Ω
- θ = arctan((100 - 300)/100) = arctan(-2) = **-63°**
- Large capacitive dominance, large angle

**E5B11 example:** X_C = 25 Ω, R = 100 Ω, X_L = 75 Ω
- θ = arctan((75 - 25)/100) = arctan(0.5) = **+27°**
- Net inductive: voltage leads current by 27°

### ELI the ICEman

Classic mnemonic for individual component phase relationships:

- **ELI**: In an inductor (L), voltage (E) leads current (I) by 90°
- **ICE**: In a capacitor (C), current (I) leads voltage (E) by 90°

These are the 90° relationships for pure reactive components. In a real RLC circuit, the phase angle is somewhere between 0° and 90° depending on the ratio of reactance to resistance.

---

## Group E5C — Impedance Plots and Coordinate Systems

### Rectangular (Cartesian) Coordinates

Impedance in rectangular form: **Z = R + jX**

- R is the real part (horizontal axis) — resistance
- X is the imaginary part (vertical axis) — reactance
- Positive j (+jX) → inductive reactance → plots above the horizontal axis
- Negative j (-jX) → capacitive reactance → plots below the horizontal axis
- Pure resistance → plots on the horizontal axis (zero imaginary part)

Examples:
- 0 - j100 = pure capacitive reactance of 100 Ω (on negative vertical axis)
- 0 + j100 = pure inductive reactance of 100 Ω (on positive vertical axis)
- 100 + j0 = pure 100 Ω resistance (on horizontal axis)
- 50 - j25 = 50 Ω resistance in series with 25 Ω capacitive reactance

### Polar Coordinates

Impedance in polar form: **Z = |Z|∠θ**

- |Z| = magnitude = √(R² + X²)
- θ = phase angle = arctan(X/R)
- 0° = pure resistance
- +90° = pure inductive reactance
- -90° = pure capacitive reactance

Polar form is natural for multiplication, division, and expressing phase shift. Rectangular form is natural for addition and subtraction of series impedances.

**To convert:** R = |Z|cos(θ), X = |Z|sin(θ)

### Phasor Diagrams

A phasor diagram is the visual representation of AC quantities as rotating vectors. Each voltage or current in a circuit is drawn as an arrow: length = magnitude, angle = phase relative to reference.

In a series RLC circuit:
- V_R is the reference (0°, along the horizontal)
- V_L points up (+90°)
- V_C points down (-90°)
- V_total = vector sum of all three

Phasor diagrams make visible why V_L and V_C partially cancel, why the total voltage and current aren't simply related by the sum of magnitudes, and why the phase angle changes as you change frequency.

### Frequency Response Graphs: Logarithmic Scale

Circuit frequency response graphs use a **logarithmic** Y-axis (and often X-axis too). Logarithmic scales are used because:
1. Frequency spans typically cover many decades (e.g., 100 Hz to 100 MHz)
2. Response in dB is linear on a log-frequency plot for simple RC/RL filters
3. Bode plots (the standard tool) use log frequency

A linear scale would show almost all the interesting behavior squeezed into a corner of the plot.

### Figure E5-1 Calculations

For the Figure E5-1 questions, you calculate the actual complex impedance and identify which quadrant/region the point falls in:

- **E5C10:** 400 Ω + 38 pF at 14 MHz → X_C = 1/(2π×14×10⁶×38×10⁻¹²) ≈ 299 Ω → Z = 400 - j299 → fourth quadrant, R > X → **Point 4**
- **E5C11:** 300 Ω + 18 µH at 3.505 MHz → X_L = 2π×3.505×10⁶×18×10⁻⁶ ≈ 396 Ω → Z = 300 + j396 → first quadrant, X slightly > R → **Point 3**
- **E5C12:** 300 Ω + 19 pF at 21.2 MHz → X_C = 1/(2π×21.2×10⁶×19×10⁻¹²) ≈ 395 Ω → Z = 300 - j395 → fourth quadrant, X slightly > R → **Point 1**

Pattern: calculate the reactance, write Z = R ± jX, determine the quadrant, estimate R vs. X ratio to identify which specific point.

---

## Group E5D — Real Power, Reactive Power, and Parasitic Effects

### Real Power vs. Reactive Power

**Real power** (P, watts): Power dissipated as heat in resistance. P = I²R. Voltage and current are in phase.

**Reactive power** (Q, VAR — volt-amperes reactive): Power stored and returned by inductors and capacitors. No dissipation. Voltage and current are 90° out of phase.

**Apparent power** (S, VA): The product of RMS voltage and current. S = V × I. This is what you'd read on an ammeter and voltmeter without knowing phase.

The relationship: **S² = P² + Q²**

In an ideal inductor or capacitor, voltage and current are exactly 90° out of phase — the product averages to zero over a full cycle. Energy is borrowed from the source for a quarter cycle, stored in the field (magnetic or electric), and returned to the source for the next quarter cycle. No net energy flows into the component; no power is dissipated.

**Reactive power is wattless and nonproductive** — it shuttles energy back and forth but doesn't accomplish work. In power systems, reactive power still loads the transmission lines (current flows), which is why utilities penalize industrial customers for poor power factor.

### Real Power Calculation — E5D11

"How much real power is consumed in a circuit consisting of a 100 Ω resistor in series with 100 Ω inductive reactance drawing 1 ampere?"

P = I² × R = 1² × 100 = **100 watts**

The reactive component dissipates nothing. Only R burns real watts. Even though the total impedance is Z = √(100² + 100²) = 141 Ω and the apparent power is S = I² × Z = 141 VA, the real power is only 100 W because the power factor is cos(45°) = 0.707.

### Skin Effect

At DC, current distributes uniformly across the full cross-section of a conductor. As frequency increases, the alternating magnetic field inside the conductor opposes interior current flow, pushing current toward the surface.

**Result:** Current flows in a thin skin on the conductor's surface. The effective conducting cross-section decreases with frequency, so **resistance increases with frequency**.

Skin depth δ = √(2ρ/ωμ) — it decreases as frequency (ω) increases.

Practical consequences:
- Hollow copper tubing is an excellent RF conductor (the interior carries no RF current anyway)
- Solid copper wire doesn't help vs. tube for RF
- Silver plating (highest conductivity) on the surface maximizes the current-carrying area

### Lead Lengths at RF

At VHF and above, component lead lengths must be kept short to:
- **Minimize inductive reactance**: Every wire has inductance (~20 nH/inch). At 300 MHz, 1 inch = 38 Ω of reactance.
- **Minimize capacitive coupling** between adjacent leads
- **Prevent parasitic resonances** (lead inductance + component capacitance can self-resonate)

At microwave frequencies specifically, short connections reduce **phase shift** — a connection that's a significant fraction of a wavelength introduces meaningful phase delay that disrupts circuit function.

### Parasitic Components

Every real component has hidden parasitic elements that degrade performance at RF:

**Capacitors:**
- Real capacitors have lead inductance (ESL = equivalent series inductance)
- This makes them self-resonate at some frequency — above the self-resonant frequency (SRF), the component behaves as an inductor
- **Electrolytics** are especially bad for RF due to their rolled-foil construction creating high ESL — unsuitable for RF bypass
- **Film capacitors** lose power at RF primarily due to **skin effect** in the thin metallic film electrodes (ESR increases)

**Inductors:**
- Real inductors have inter-turn capacitance — adjacent turns are separated by insulation, forming tiny capacitors
- This distributed capacitance resonates with the inductance, creating a self-resonant frequency
- Above the SRF, the inductor looks like a capacitor
- Wide turn spacing and single-layer windings push the SRF higher

**Self-resonance mechanism (E5D07):** In any component, self-resonance occurs when the component's nominal reactance (what it's designed for) resonates with its **parasitic reactance** of the opposite sign. Capacitor nominal C + parasitic L → self-resonance. Inductor nominal L + parasitic C → self-resonance. Above the SRF, the component's identity flips.

### Conductor Diameter and Electrical Length

Thicker conductors have a lower velocity factor — RF waves travel more slowly along them. Slower wave velocity = shorter wavelength = the physical conductor is a larger fraction of a wavelength = **electrically longer**.

As conductor diameter increases, electrical length increases. This matters for antennas: a thick-element Yagi has electrically longer elements than thin wire of the same physical length. The resonant frequency is lower, so thick elements must be physically shorter than the "standard" half-wave formula predicts.

---

## Putting It Together

The four groups in E5 describe one coherent framework:

1. **E5A** (Resonance): How L and C interact to create frequency-selective circuits. The foundation of filters, matching networks, oscillators, and antenna systems.

2. **E5B** (Time Constants and Phase): How circuits behave over time and how phase angles are calculated. Essential for understanding transient behavior and steady-state AC response.

3. **E5C** (Impedance Representation): The mathematical language for describing complex impedances. Rectangular and polar forms are just two ways of expressing the same thing — like latitude/longitude vs. bearing/distance.

4. **E5D** (Power and Parasitics): Why real components deviate from ideal behavior at RF, and how to account for the difference between apparent power and real power.

Master the resonant frequency formula, the bandwidth formula, the phase angle formula, and the skin effect/parasitic concepts — those cover the majority of E5 exam questions.

---

*Extra-class exam: 50 questions, must pass with 37 or higher (74%). E5 contributes 4 questions.*
