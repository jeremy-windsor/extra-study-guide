# E7 — Practical Circuits
*8 questions on the exam from a pool of 99*

## Group E7A — Digital circuits: digital circuit principles; flip-flops; counters; shift registers; multiplexers; demultiplexers; adders

### E7A01
**Which circuit is bistable?**
- A) An AND gate
- B) An OR gate
- **C) A flip-flop** ✅
- D) A bipolar amplifier

> A flip-flop is the classic bistable circuit — it has two stable states and remains in one state until triggered to switch to the other. An AND gate and OR gate are combinational logic (output depends only on current inputs, no memory). A bipolar amplifier is an analog device. The key word is 'bistable' — two stable states with memory. Flip-flops are the building blocks of registers, counters, and digital memory.

### E7A02
**What is the function of a decade counter?**
- **A) It produces one output pulse for every 10 input pulses** ✅
- B) It decodes a decimal number for display on a seven-segment LED display
- C) It produces 10 output pulses for every input pulse
- D) It decodes a binary number for display on a seven-segment LED display

> A decade counter counts from 0 through 9 (ten states), then resets to 0. This means it produces one output pulse for every 10 input pulses — it divides the input frequency by 10. A BCD-to-seven-segment decoder is a separate device that converts binary-coded decimal to display format. Decade counters are built from flip-flops with feedback to reset at count 10 instead of the natural power-of-2 rollover.

### E7A03
**Which of the following can divide the frequency of a pulse train by 2?**
- A) An XOR gate
- **B) A flip-flop** ✅
- C) An OR gate
- D) A multiplexer

> A flip-flop toggles between two states on each clock edge. If you connect a flip-flop so it toggles on every input pulse (T flip-flop or JK with J=K=1), the output changes state once per input cycle, producing an output frequency exactly half the input. An XOR gate is combinational — no memory, no division. Multiplexers select between inputs, they don't divide.

### E7A04
**How many flip-flops are required to divide a signal frequency by 16?**
- **A) 4** ✅
- B) 6
- C) 8
- D) 16

> Each flip-flop divides frequency by 2. To divide by 16, you need N flip-flops where 2^N = 16, so N = 4. The binary counter counts: 0000→0001→...→1111→0000. Four flip-flops cascaded (each clocked by the previous one's output) create a ÷16 counter. This is the basis of all binary counters — each stage halves the frequency.

### E7A05
**Which of the following circuits continuously alternates between two states without an external clock signal?**
- A) Monostable multivibrator
- B) J-K flip-flop
- C) T flip-flop
- **D) Astable multivibrator** ✅

> An astable multivibrator has NO stable state — it continuously oscillates between two states without any external trigger. A monostable (one-shot) has one stable state and temporarily switches to the other. A JK or T flip-flop is bistable (stays in either state). The classic 555 timer in astable mode is the most common example — it generates a continuous square wave.

### E7A06
**What is a characteristic of a monostable multivibrator?**
- **A) It switches temporarily to an alternate state for a set time** ✅
- B) It produces a continuous square wave
- C) It stores one bit of data
- D) It maintains a constant output voltage, regardless of variations in the input voltage

> A monostable multivibrator (one-shot) has ONE stable state. When triggered, it switches to the alternate state for a predetermined time, then returns to the stable state. The pulse duration is set by an RC time constant. The 555 timer in monostable mode produces one output pulse of fixed duration for each trigger. Monostables are used for pulse generation, debouncing switches, and creating time delays.

### E7A07
**What logical operation does a NAND gate perform?**
- A) It produces a 0 at its output only if all inputs are 0
- B) It produces a 1 at its output only if all inputs are 1
- C) It produces a 0 at its output if some but not all inputs are 1
- **D) It produces a 0 at its output only if all inputs are 1** ✅

> A NAND gate is AND followed by NOT. The AND gate produces 1 only when ALL inputs are 1. Inverting that: NAND produces 0 only when ALL inputs are 1 — otherwise the output is 1. Truth table for 2-input NAND: 00→1, 01→1, 10→1, 11→0. NAND is a universal gate — you can build ANY logic function using only NAND gates.

### E7A08
**What logical operation does an OR gate perform?**
- **A) It produces a 1 at its output if any input is 1** ✅
- B) It produces a 0 at its output if all inputs are 1
- C) It produces a 0 at its output if some but not all inputs are 1
- D) It produces a 1 at its output if all inputs are 0

> An OR gate produces a 1 at its output if ANY input is 1. Only when ALL inputs are 0 does the output go to 0. Truth table for 2-input OR: 00→0, 01→1, 10→1, 11→1. OR gates are used for combining conditions where any one trigger should activate the output.

### E7A09
**What logical operation is performed by a two-input exclusive NOR gate?**
- A) It produces a 0 at its output only if all inputs are 0
- B) It produces a 1 at its output only if all inputs are 1
- **C) It produces a 0 at its output if one and only one of its inputs is 1** ✅
- D) It produces a 1 at its output if one and only one input is 1

> An exclusive NOR (XNOR) gate is XOR followed by NOT. XOR produces 1 when inputs DIFFER; XNOR produces 1 when inputs are the SAME. So XNOR produces 0 when one and only one input is 1. Truth table: 00→1, 01→0, 10→0, 11→1. XNOR is used as a coincidence detector — output is high when both inputs match.

### E7A10
**What is a truth table?**
- A) A list of inputs and corresponding outputs for an op-amp
- **B) A list of inputs and corresponding outputs for a digital device** ✅
- C) A diagram showing logic states when the digital gate output is true
- D) A table of logic symbols that indicate the logic states of an op-amp

> A truth table is a complete listing of all possible input combinations and their corresponding outputs for a digital device. For a 2-input gate, the truth table has 4 rows (2²). For 3 inputs, 8 rows (2³). Truth tables completely define the behavior of any combinational logic circuit. They're the fundamental design tool for digital logic.

### E7A11
**What does “positive logic” mean in reference to logic devices?**
- A) The logic devices have high noise immunity
- **B) High voltage represents a 1, low voltage a 0** ✅
- C) The logic circuit is in the “true” condition
- D) 1s and 0s are defined as different positive voltage levels

> In positive logic, high voltage represents logic 1 and low voltage represents logic 0. Standard TTL: high = 2.0-5.0V = logic 1, low = 0-0.8V = logic 0. Negative logic reverses this convention (high voltage = 0, low voltage = 1). Nearly all modern digital systems use positive logic convention.

## Group E7B — Amplifiers: class A; class B; class C; class AB; push-pull amplifiers; distortion; efficiency

### E7B01
**For what portion of the signal cycle does each active element in a push-pull, Class AB amplifier conduct?**
- **A) More than 180 degrees but less than 360 degrees** ✅
- B) Exactly 180 degrees
- C) The entire cycle
- D) Less than 180 degrees

> Class AB biases each transistor slightly above cutoff so each conducts for more than 180° but less than 360° of the signal cycle. In push-pull Class AB, one transistor handles the positive swing and the other handles the negative swing, with both conducting during the crossover region to reduce crossover distortion. Class A = 360° (full cycle), Class B = exactly 180°, Class C = less than 180°. Class AB is the standard for linear power amplifiers in amateur radio.

### E7B02
**What is a Class D amplifier?**
- **A) An amplifier that uses switching technology to achieve high efficiency** ✅
- B) A low power amplifier that uses a differential amplifier for improved linearity
- C) An amplifier that uses drift-mode FETs for high efficiency
- D) An amplifier biased to be relatively free from distortion

> A Class D amplifier uses switching technology — the active devices are either fully on (saturated) or fully off (cutoff), switching at high frequency. The output is a pulse-width modulated (PWM) signal that, after filtering, reproduces the desired waveform. Because the transistors spend almost no time in the linear region (where power is dissipated as heat), efficiency can exceed 90%. Class D is used in audio amplifiers and some RF applications.

### E7B03
**What circuit is required at the output of an RF switching amplifier?**
- **A) A filter to remove harmonic content** ✅
- B) A high-pass filter to compensate for low gain at low frequencies
- C) A matched load resistor to prevent damage by switching transients
- D) A temperature compensating load resistor to improve linearity

> An RF switching amplifier (Class D, E, or F) produces a rectangular or shaped pulse waveform rich in harmonics. A low-pass or band-pass filter at the output removes harmonic content, leaving only the desired fundamental frequency. Without this filter, the harmonics would be transmitted as spurious emissions, violating FCC rules. The filter is essential — it's what makes switching amplifiers usable for radio transmission.

### E7B04
**What is the operating point of a Class A common emitter amplifier?**
- **A) Approximately halfway between saturation and cutoff** ✅
- B) Approximately halfway between the emitter voltage and the base voltage
- C) At a point where the bias resistor equals the load resistor
- D) At a point where the load line intersects the zero bias current curve

> A Class A amplifier's operating point (Q-point) is approximately halfway between saturation and cutoff on the load line. This allows the transistor to swing equally in both directions without clipping. The transistor conducts for the entire 360° of the signal cycle. Maximum theoretical efficiency is 50% (25% with a resistive load), but Class A produces the lowest distortion of any class.

### E7B05
**What can be done to prevent unwanted oscillations in an RF power amplifier?**
- A) Tune the stage for minimum loading
- B) Tune both the input and output for maximum power
- **C) Install parasitic suppressors and/or neutralize the stage** ✅
- D) Use a phase inverter in the output filter

> Unwanted oscillations in RF power amplifiers are typically caused by parasitic elements (stray capacitance and inductance) forming unintended feedback paths. Solutions: (1) Parasitic suppressors — small resistor-inductor combinations on tube plate leads or transistor collectors that dampen VHF/UHF parasitic oscillations. (2) Neutralization — feeding back a small amount of signal in anti-phase to cancel the feedback through device capacitance. These are standard RF amplifier stability techniques.

### E7B06
**What is a characteristic of a grounded-grid amplifier?**
- A) High power gain
- **B) Low input impedance** ✅
- C) High electrostatic damage protection
- D) Low bandwidth

> A grounded-grid (or common-grid) amplifier has the grid (or gate) at RF ground. The input signal is applied to the cathode (or source), and the output is taken from the plate (or drain). Key characteristic: low input impedance (typically 50-300 ohms), making it easy to match to coaxial feed lines. It also provides inherent stability because the grounded grid shields the input from the output. Grounded-grid amplifiers are common in amateur HF linear amplifiers.

### E7B07
**Which of the following is the likely result of using a Class C amplifier to amplify a single-sideband phone signal?**
- A) Reduced intermodulation products
- B) Increased overall intelligibility
- C) Reduced third-order intermodulation
- **D) Signal distortion and excessive bandwidth** ✅

> Class C amplifiers conduct for less than 180° of the signal cycle and produce severe distortion of the waveform. They work well for FM and CW (constant envelope signals) because the output tank circuit restores the sine wave. For SSB, the varying envelope would be destroyed — the clipping creates signal distortion and generates excessive bandwidth (splatter). Never use Class C for SSB; use Class A, AB, or B.

### E7B08
**Why are switching amplifiers more efficient than linear amplifiers?**
- A) Switching amplifiers operate at higher voltages
- **B) The switching device is at saturation or cutoff most of the time** ✅
- C) Linear amplifiers have high gain resulting in higher harmonic content
- D) Switching amplifiers use push-pull circuits

> Switching amplifiers (Class D, E, F) are more efficient because the active device is either fully saturated (very low voltage across it) or fully cutoff (no current through it). In both states, power dissipation (V × I) is minimal. A linear amplifier's transistor operates in the active region where both voltage and current are simultaneously present, generating significant heat. Efficiency: Class D >90%, Class A ~25-50%, Class AB ~50-65%.

### E7B09
**What is characteristic of an emitter follower (or common collector) amplifier?**
- A) Low input impedance and phase inversion from input to output
- B) Differential inputs and single output
- C) Acts as an OR circuit if one input is grounded
- **D) Input and output signals in-phase** ✅

> An emitter follower (common collector) has unity voltage gain (slightly less than 1) with no phase inversion — the output signal is in-phase with the input. Its key properties: very high input impedance, very low output impedance, making it an excellent impedance-matching buffer. Current gain is high (approximately β). It's used to drive low-impedance loads from high-impedance sources.

### E7B10
**In Figure E7-1, what is the purpose of R1 and R2?**
- A) Load resistors
- **B) Voltage divider bias** ✅
- C) Self bias
- D) Feedback

> In the circuit shown in Figure E7-1, R1 and R2 form a voltage divider that sets the DC bias voltage at the base of the transistor. This establishes the Q-point (operating point) of the amplifier. Voltage divider bias is the most stable bias method for common emitter amplifiers because it's relatively immune to transistor β variations and temperature changes.

### E7B11
**In Figure E7-1, what is the purpose of R3?**
- A) Fixed bias
- B) Emitter bypass
- C) Output load resistor
- **D) Self bias** ✅

> R3 in Figure E7-1 is in the emitter circuit and provides self-bias (also called emitter degeneration or DC feedback bias). The voltage developed across R3 by the emitter current opposes changes in collector current, stabilizing the operating point against temperature variations and transistor parameter spreads. If the transistor tries to draw more current, the voltage across R3 increases, reducing base-emitter voltage and limiting the current increase.

### E7B12
**What type of amplifier circuit is shown in Figure E7-1?**
- A) Common base
- B) Common collector
- **C) Common emitter** ✅
- D) Emitter follower

> Figure E7-1 shows a common emitter amplifier — the emitter is common to both the input and output circuits (via the bypass capacitor). The input is at the base, the output is at the collector. Common emitter provides both voltage gain and current gain, with a 180° phase inversion. It's the most widely used BJT amplifier configuration.

## Group E7C — Filters and matching networks: types of networks; types of filters; filter applications; filter characteristics; impedance matching

### E7C01
**How are the capacitors and inductors of a low-pass filter Pi-network arranged between the network’s input and output?**
- A) Two inductors are in series between the input and output, and a capacitor is connected between the
- B) Two capacitors are in series between the input and output, and an inductor is connected between the
- C) An inductor is connected between the input and ground, another inductor is connected between the
- **D) A capacitor is connected between the input and ground, another capacitor is connected between the** ✅

> A low-pass Pi-network has the topology: capacitor from input to ground, inductor in series between input and output, capacitor from output to ground. The shape looks like the Greek letter π. This is the standard output network for tube-type amateur transmitters — it simultaneously provides impedance matching and harmonic filtering. Capacitors shunt high frequencies to ground while the series inductor passes low frequencies.

### E7C02
**What is the frequency response of a T-network with series capacitors and a shunt inductor?**
- A) Low-pass
- **B) High-pass** ✅
- C) Band-pass
- D) Notch

> A T-network with series capacitors and a shunt inductor is a high-pass filter. The series capacitors block low frequencies (high reactance at low f) and pass high frequencies. The shunt inductor shorts low frequencies to ground (low reactance at low f) and is invisible at high frequencies. The T shape has components in series on both sides with a shunt element in the middle.

### E7C03
**What is the purpose of adding an inductor to a Pi-network to create a Pi-L-network?**
- **A) Greater harmonic suppression** ✅
- B) Higher efficiency
- C) To eliminate one capacitor
- D) Greater transformation range

> Adding an inductor to a Pi-network creates a Pi-L network, which provides greater harmonic suppression. The extra inductor adds another pole to the filter response, giving a steeper rolloff above the cutoff frequency. This means second and third harmonics are attenuated more than with a simple Pi alone. Pi-L networks are used in amplifiers where harmonic suppression is critical.

### E7C04
**How does an impedance-matching circuit transform a complex impedance to a resistive impedance?**
- A) It introduces negative resistance to cancel the resistive part of impedance
- B) It introduces transconductance to cancel the reactive part of impedance
- **C) It cancels the reactive part of the impedance and changes the resistive part to the desired value** ✅
- D) Reactive currents are dissipated in matched resistances

> An impedance-matching circuit transforms a complex impedance (R + jX) to a pure resistance by: (1) canceling the reactive part (adding equal and opposite reactance to neutralize jX), and (2) transforming the resistive part to the desired value (typically 50 ohms). L-networks, Pi-networks, and T-networks all accomplish this. The reactive part cancellation is key — you can't match a complex impedance without first dealing with the reactance.

### E7C05
**Which filter type has ripple in the passband and a sharp cutoff?**
- A) A Butterworth filter
- B) An active LC filter
- C) A passive op-amp filter
- **D) A Chebyshev filter** ✅

> A Chebyshev filter has ripple in the passband (amplitude varies within specified limits) but achieves a sharper cutoff than a Butterworth filter of the same order. The tradeoff: Butterworth is maximally flat in the passband (no ripple) but has a gentler transition to the stopband. Chebyshev allows controlled ripple in exchange for a steeper rolloff. The ripple amount is a design parameter — more ripple = sharper cutoff.

### E7C06
**What are the characteristics of an elliptical filter?**
- A) Gradual passband rolloff with minimal stop-band ripple
- B) Extremely flat response over its pass band with gradually rounded stop-band corners
- **C) Extremely sharp cutoff with one or more notches in the stop band** ✅
- D) Gradual passband rolloff with extreme stop-band ripple

> An elliptical (Cauer) filter has the sharpest possible cutoff of any filter type for a given order. It achieves this by placing transmission zeros (notches) in the stopband. The tradeoff: ripple in BOTH the passband and stopband. The notches in the stopband provide extremely sharp transitions — useful when you need a very narrow guard band between the passband and a strong interfering signal.

### E7C07
**Which describes a Pi-L network?**
- A) A Phase Inverter Load network
- **B) A Pi-network with an additional output series inductor** ✅
- C) A network with only three discrete parts
- D) A matching network in which all components are isolated from ground

> A Pi-L network is a Pi-network with an additional series inductor at the output. The 'L' refers to this added inductor, not the L-network topology. This creates a more effective low-pass filter for harmonic suppression while still providing impedance transformation. The extra element gives the designer more degrees of freedom for simultaneously optimizing matching and filtering.

### E7C08
**Which of the following is most frequently used as a band-pass or notch filter in VHF and UHF transceivers?**
- A) A Sallen-Key filter
- **B) A helical filter** ✅
- C) A swinging choke filter
- D) A finite impulse response filter

> Helical filters are compact resonant structures used as band-pass or notch filters at VHF and UHF. They consist of helical (coiled) resonators in shielded cavities, coupled together. Helical filters are smaller than cavity filters at the same frequency and provide better selectivity than LC filters. They're commonly found in the front end of VHF/UHF transceivers for image rejection and adjacent-channel selectivity.

### E7C09
**What is a crystal lattice filter?**
- A) A power supply filter made with interlaced quartz crystals
- B) An audio filter made with four quartz crystals that resonate at 1 kHz intervals
- C) A filter using lattice-shaped quartz crystals for high-Q performance
- **D) A filter for low-level signals made using quartz crystals** ✅

> A crystal lattice filter uses multiple quartz crystals arranged in a lattice network to create a very narrow, high-Q band-pass filter. Quartz crystals have extremely high Q factors (tens of thousands), enabling very selective filters. Crystal lattice filters are used in IF stages of SSB and CW receivers where narrow bandwidth and sharp skirts are essential. They operate at the crystal resonant frequency, typically 455 kHz or 9 MHz.

### E7C10
**Which of the following filters is used in a 2-meter band repeater duplexer?**
- A) A crystal filter
- **B) A cavity filter** ✅
- C) A DSP filter
- D) An L-C filter

> A cavity filter is used in repeater duplexers because it can provide the extreme selectivity needed to separate the transmit and receive frequencies (typically 600 kHz apart on 2 meters). Cavity filters are resonant metal enclosures that provide very high Q and excellent rejection of nearby frequencies. A duplexer typically uses 4-6 cavities to achieve 80+ dB of isolation between the transmitter and receiver ports.

### E7C11
**Which of the following measures a filter’s ability to reject signals in adjacent channels?**
- A) Passband ripple
- B) Phase response
- **C) Shape factor** ✅
- D) Noise factor

> Shape factor measures a filter's ability to reject signals in adjacent channels. It's defined as the ratio of bandwidth at -60 dB to bandwidth at -6 dB: SF = BW(-60dB) / BW(-6dB). A perfect rectangular filter would have SF = 1:1. Real filters: crystal ladder filter SF ≈ 2:1 (excellent), LC filter SF ≈ 5:1 (moderate). Lower shape factor = steeper skirts = better adjacent channel rejection.

## Group E7D — Power supplies and voltage regulators: power transformers; rectifiers; filters; regulators; shunt and series regulators; switching regulators; inverters

### E7D01
**How does a linear electronic voltage regulator work?**
- A) It has a ramp voltage as its output
- B) It eliminates the need for a pass transistor
- C) The control element duty cycle is proportional to the line or load conditions
- **D) The conduction of a control element is varied to maintain a constant output voltage** ✅

> A linear electronic voltage regulator uses a control element (pass transistor) in series with the load. The conduction of this pass transistor is continuously varied by a feedback loop to maintain a constant output voltage regardless of input voltage changes or load current changes. The pass transistor operates in its linear (active) region — hence 'linear regulator.' The excess voltage (input - output) is dropped across the pass transistor as heat.

### E7D02
**How does a switchmode voltage regulator work?**
- A) By alternating the output between positive and negative voltages
- **B) By varying the duty cycle of pulses input to a filter** ✅
- C) By varying the conductivity of a pass element
- D) By switching between two Zener diode reference voltages

> A switchmode (switching) voltage regulator uses a transistor as a high-frequency switch (on/off), varying the duty cycle of pulses that are then smoothed by an LC filter. Higher duty cycle = higher output voltage; lower duty cycle = lower output voltage. The switching frequency is typically 50 kHz to several MHz. Because the transistor is either fully on (low V_CE) or fully off (no current), very little power is wasted as heat, achieving efficiencies of 80-95%.

### E7D03
**What device is used as a stable voltage reference?**
- **A) A Zener diode** ✅
- B) A digital-to-analog converter
- C) An SCR
- D) An analog-to-digital converter

> A Zener diode is the standard stable voltage reference. When reverse biased beyond its breakdown voltage, the Zener maintains a nearly constant voltage across it. The voltage is determined by the doping level and is very stable with current changes. Precision voltage regulators (like the LM317 or 7805) use internal Zener references. The temperature-compensated Zener (around 5.6V) is the most stable.

### E7D04
**Which of the following describes a three-terminal voltage regulator?**
- A) A series current source
- **B) A series regulator** ✅
- C) A shunt regulator
- D) A shunt current source

> A three-terminal voltage regulator (like 7805, 7812, LM317) is a series regulator — it has input, output, and ground (or adjust) pins. The pass element is in series with the load, dropping the excess voltage. These ICs contain the reference, error amplifier, and pass transistor in one package. They're the simplest way to build a regulated power supply.

### E7D05
**Which of the following types of linear voltage regulator operates by loading the unregulated voltage source?**
- A) A constant current source
- B) A series regulator
- C) A shunt current source
- **D) A shunt regulator** ✅

> A shunt regulator works by diverting (shunting) excess current to ground to maintain a constant voltage. It's connected in parallel with the load. When the load draws less current, the shunt regulator draws more to keep the total current (and thus the voltage across the series resistor) constant. Zener diode regulators are the simplest shunt regulators. Shunt regulators waste power but are simple and inherently short-circuit-proof.

### E7D06
**What is the purpose of Q1 in the circuit shown in Figure E7-2?**
- A) It provides negative feedback to improve regulation
- B) It provides a constant load for the voltage source
- **C) It controls the current to keep the output voltage constant** ✅
- D) It provides regulation by switching or “chopping” the input DC voltage

> In the linear voltage regulator circuit of Figure E7-2, Q1 is the series pass transistor. It controls the current flowing from input to output, maintaining constant output voltage. A feedback loop senses the output voltage and adjusts Q1's base drive to compensate for changes in load or input voltage. Q1 operates in its linear region, dissipating the voltage difference as heat.

### E7D07
**What is the purpose of C2 in the circuit shown in Figure E7-2?**
- **A) It bypasses rectifier output ripple around D1** ✅
- B) It is a brute force filter for the output
- C) To prevent self-oscillation
- D) To provide fixed DC bias for Q1

> In Figure E7-2, C2 bypasses the rectifier output ripple around the Zener reference diode D1. Without C2, the ripple from the unregulated supply would modulate the Zener reference voltage, degrading regulation. C2 provides a low-impedance path for AC ripple, keeping the reference voltage clean. This is critical for achieving good power supply ripple rejection.

### E7D08
**What type of circuit is shown in Figure E7-2?**
- A) Switching voltage regulator
- B) Common emitter amplifier
- **C) Linear voltage regulator** ✅
- D) Common base amplifier

> Figure E7-2 shows a linear voltage regulator circuit. The key components: a series pass transistor (Q1) controlled by a feedback network that compares the output voltage to a Zener diode reference. The pass transistor continuously adjusts its conductance to maintain constant output voltage. This is NOT a switching regulator (no pulse-width modulation) and NOT an amplifier (no signal amplification purpose).

### E7D09
**How is battery operating time calculated?**
- A) Average current divided by capacity in amp-hours
- B) Average current divided by internal resistance
- **C) Capacity in amp-hours divided by average current** ✅
- D) Internal resistance divided by average current

> Battery operating time = Capacity (amp-hours) ÷ Average current (amps). Example: a 12 Ah battery powering a 2A load: 12 Ah ÷ 2A = 6 hours. This is an approximation — real batteries have reduced capacity at higher discharge rates (Peukert's effect) and temperature affects capacity. For intermittent use (like ham radio), calculate the average current considering transmit/receive duty cycle.

### E7D10
**Why is a switching type power supply less expensive and lighter than an equivalent linear power supply?**
- A) The inverter design does not require an output filter circuit
- B) The control circuitry uses less current, therefore smaller heat sinks are required
- **C) The high frequency inverter design uses much smaller transformers and filter components for an** ✅
- D) It recovers power from the unused portion of the AC cycle, thus using fewer components

> Switching power supplies operate at high frequency (typically 50-500 kHz), which allows much smaller transformers and filter components. Transformer size is inversely proportional to operating frequency — a 100 kHz transformer can be 1/100th the size of a 60 Hz transformer for the same power. The same applies to filter capacitors and inductors. This makes switching supplies lighter, smaller, and less expensive than equivalent linear supplies.

### E7D11
**What is the purpose of an inverter connected to a solar panel output?**
- A) Reduce AC ripple on the output
- B) Maintain voltage with varying illumination levels
- C) Prevent discharge when panel is not illuminated
- **D) Convert the panel’s output from DC to AC** ✅

> An inverter converts DC to AC. Solar panels produce DC power, but most household appliances and the power grid use AC. The inverter converts the panel's DC output to AC (typically 120/240V, 60 Hz) for home use or grid feed-in. Grid-tie inverters synchronize their output to the utility grid frequency and phase.

### E7D12
**What is the dropout voltage of a linear voltage regulator?**
- A) Minimum input voltage for rated power dissipation
- B) Maximum output voltage drop when the input voltage is varied over its specified range
- **C) Minimum input-to-output voltage required to maintain regulation** ✅
- D) Maximum that the output voltage may decrease at rated load

> Dropout voltage is the minimum input-to-output voltage difference required for a linear regulator to maintain regulation. For a standard 7805 (5V output), dropout is about 2V — meaning input must be at least 7V. Below that, the output drops below 5V. Low-dropout (LDO) regulators can operate with as little as 0.1-0.5V dropout. Dropout voltage determines the minimum input voltage for proper operation.

### E7D13
**Which of the following calculates power dissipated by a series linear voltage regulator?**
- A) Input voltage multiplied by input current
- B) Input voltage divided by output current
- **C) Voltage difference from input to output multiplied by output current** ✅
- D) Output voltage multiplied by output current

> Power dissipated by a series linear voltage regulator = (V_in - V_out) × I_out. The pass transistor drops the excess voltage, and all load current flows through it. Example: V_in=12V, V_out=5V, I_out=1A: P = (12-5) × 1 = 7W dissipated as heat. This is why linear regulators need heat sinks and why switching regulators are preferred for large voltage differences or high currents.

### E7D14
**What is the purpose of connecting equal-value resistors across power supply filter capacitors connected in series?**
- A) Equalize the voltage across each capacitor
- B) Discharge the capacitors when voltage is removed
- C) Provide a minimum load on the supply
- **D) All these choices are correct** ✅

> Connecting equal-value resistors across series filter capacitors serves ALL three purposes: (1) equalizing voltage across each capacitor (preventing one from seeing more than its rated voltage), (2) discharging the capacitors when power is removed (safety — prevents dangerous stored charge), and (3) providing a minimum load on the supply. All these choices are correct.

### E7D15
**What is the purpose of a step-start circuit in a high-voltage power supply?**
- A) To provide a dual-voltage output for reduced power applications
- B) To compensate for variations of the incoming line voltage
- C) To prevent arcing across the input power switch or relay contacts
- **D) To allow the filter capacitors to charge gradually** ✅

> A step-start circuit in a high-voltage power supply allows the filter capacitors to charge gradually rather than all at once. Without it, the initial inrush current when charging empty capacitors can be enormous — potentially tripping breakers, welding relay contacts, or stressing rectifiers. A step-start typically uses a series resistor that's bypassed by a relay after a time delay, limiting the initial charging current.

## Group E7E — Modulation and demodulation: modulation methods; modulation index; frequency and phase modulation; demodulation; mixer theory

### E7E01
**Which of the following can be used to generate FM phone signals?**
- A) Balanced modulation of the audio amplifier
- **B) Reactance modulation of a local oscillator** ✅
- C) Reactance modulation of the final amplifier
- D) Balanced modulation of a local oscillator

> FM signals can be generated by reactance modulation of a local oscillator. A reactance modulator varies the effective capacitance (or inductance) across the oscillator's tuned circuit in response to the audio signal, causing the oscillator frequency to deviate proportionally. This is the classic indirect FM generation method. Balanced modulation produces DSB (double-sideband), not FM.

### E7E02
**What is the function of a reactance modulator?**
- A) Produce PM or FM signals by varying a resistance
- B) Produce AM signals by varying an inductance
- C) Produce AM signals by varying a resistance
- **D) Produce PM or FM signals by varying a capacitance** ✅

> A reactance modulator produces PM (phase modulation) or FM signals by varying a reactance (capacitance) in the oscillator circuit. A varactor diode is the most common reactance element — its capacitance varies with the applied audio voltage. As the audio signal varies, the varactor capacitance changes, shifting the oscillator frequency up and down. The result is frequency modulation.

### E7E03
**What is a frequency discriminator?**
- A) An FM generator circuit
- B) A circuit for filtering closely adjacent signals
- C) An automatic band-switching circuit
- **D) A circuit for detecting FM signals** ✅

> A frequency discriminator is a circuit for DETECTING (demodulating) FM signals. It converts frequency variations back to audio voltage variations. Common types: Foster-Seeley discriminator and ratio detector. The discriminator's output voltage is proportional to the instantaneous frequency deviation from the center frequency. It's the FM equivalent of an AM envelope detector.

### E7E04
**What is one way to produce a single-sideband phone signal?**
- **A) Use a balanced modulator followed by a filter** ✅
- B) Use a reactance modulator followed by a mixer
- C) Use a loop modulator followed by a mixer
- D) Use a product detector with a DSB signal

> A balanced modulator followed by a filter produces SSB. The balanced modulator produces DSB-SC (double sideband, suppressed carrier) — both sidebands but no carrier. The filter then removes the unwanted sideband, leaving only USB or LSB. This is the 'filter method' of SSB generation. The phasing method uses phase shifters instead of a filter to cancel one sideband.

### E7E05
**What is added to an FM speech channel to boost the higher audio frequencies?**
- A) A de-emphasis network
- B) A harmonic enhancer
- C) A heterodyne enhancer
- **D) A pre-emphasis network** ✅

> A pre-emphasis network boosts the higher audio frequencies before modulation in an FM transmitter. This compensates for the fact that FM demodulation produces more noise at higher audio frequencies (triangular noise spectrum). The matching de-emphasis network in the receiver attenuates the boosted highs back to normal, also reducing the noise — improving overall SNR.

### E7E06
**Why is de-emphasis used in FM communications receivers?**
- **A) For compatibility with transmitters using phase modulation** ✅
- B) To reduce impulse noise reception
- C) For higher efficiency
- D) To remove third-order distortion products

> De-emphasis in FM receivers is used for compatibility with transmitters using phase modulation. Phase modulation inherently emphasizes higher audio frequencies (deviation increases with modulating frequency). De-emphasis compensates for this, making PM sound like FM. This is how most amateur FM transceivers work — they actually use PM at the transmitter and de-emphasis at the receiver.

### E7E07
**What is meant by the term “baseband” in radio communications?**
- A) The lowest frequency band that the transmitter or receiver covers
- **B) The frequency range occupied by a message signal prior to modulation** ✅
- C) The unmodulated bandwidth of the transmitted signal
- D) The basic oscillator frequency in an FM transmitter that is multiplied to increase the deviation and

> Baseband refers to the frequency range occupied by the original message signal before it's modulated onto a carrier. For voice, the baseband is roughly 300-3000 Hz. For video, it might be 0-4.5 MHz. Modulation shifts the baseband signal up to the RF carrier frequency for transmission. At the receiver, demodulation recovers the baseband signal.

### E7E08
**What are the principal frequencies that appear at the output of a mixer?**
- A) Two and four times the input frequency
- B) The square root of the product of input frequencies
- **C) The two input frequencies along with their sum and difference frequencies** ✅
- D) 1.414 and 0.707 times the input frequency

> A mixer's output contains: the two original input frequencies (f1 and f2) along with their sum (f1+f2) and difference (f1-f2). These are the principal products. In a superheterodyne receiver, the RF signal and LO feed the mixer, and the IF filter selects the difference frequency. Practical mixers also produce higher-order products (2f1±f2, etc.) but these are undesired spurious responses.

### E7E09
**What occurs when the input signal levels to a mixer are too high?**
- **A) Spurious mixer products are generated** ✅
- B) Mixer blanking occurs
- C) Automatic limiting occurs
- D) Excessive AGC voltage levels are generated

> When input signal levels to a mixer are too high, the mixer operates in a nonlinear region beyond its design range, generating spurious mixer products. These are intermodulation products and harmonics at unwanted frequencies that can appear as phantom signals. Keeping mixer input levels within the specified range (typically below the 1 dB compression point) minimizes spurs.

### E7E10
**How does a diode envelope detector function?**
- **A) By rectification and filtering of RF signals** ✅
- B) By breakdown of the Zener voltage
- C) By mixing signals with noise in the transition region of the diode
- D) By sensing the change of reactance in the diode with respect to frequency

> A diode envelope detector works by rectification and filtering. The diode rectifies the AM signal (passes only positive half-cycles), and an RC filter smooths the rectified output to follow the envelope (the audio modulation). This is the simplest AM demodulator — literally a diode and a capacitor. It's used in crystal radios and AM broadcast receivers.

### E7E11
**Which type of detector is used for demodulating SSB signals?**
- A) Discriminator
- B) Phase detector
- **C) Product detector** ✅
- D) Phase comparator

> A product detector demodulates SSB signals. It multiplies (mixes) the incoming SSB signal with a locally generated carrier (the BFO — beat frequency oscillator) to recover the original audio. The BFO replaces the carrier that was suppressed during SSB generation. Without the BFO, SSB sounds like unintelligible noise. Product detectors are also used for CW reception.

## Group E7F — DSP and software radio techniques: digital filters; software defined radio; signal processing

### E7F01
**What is meant by “direct sampling” in software defined radios?**
- A) Software is converted from source code to object code during operation of the receiver
- B) I and Q signals are generated by digital processing without the use of RF amplification
- **C) Incoming RF is digitized by an analog-to-digital converter without being mixed with a local oscillator** ✅
- D) A switching mixer is used to generate I and Q signals directly from the RF input

> Direct sampling in an SDR means the incoming RF signal is digitized directly by an analog-to-digital converter (ADC) without first being mixed down to an intermediate frequency. The ADC samples the RF signal at a rate high enough to satisfy the Nyquist criterion. All frequency conversion, filtering, and demodulation are then performed in software/firmware. This eliminates mixers, LOs, and IF stages from the hardware.

### E7F02
**What kind of digital signal processing audio filter is used to remove unwanted noise from a received SSB signal?**
- **A) An adaptive filter** ✅
- B) A crystal-lattice filter
- C) A Hilbert-transform filter
- D) A phase-inverting filter

> An adaptive filter is used to remove unwanted noise from a received signal. It continuously adjusts its filter coefficients to minimize the noise component while preserving the desired signal. The LMS (Least Mean Squares) algorithm is the most common adaptive filter technique. Unlike fixed filters, adaptive filters can track and cancel changing noise environments — ideal for QRM and QRN reduction.

### E7F03
**What type of digital signal processing filter is used to generate an SSB signal?**
- A) An adaptive filter
- B) A notch filter
- **C) A Hilbert-transform filter** ✅
- D) An elliptical filter

> A Hilbert-transform filter generates the 90° phase shift needed to produce SSB using the phasing method. The Hilbert transform shifts all frequency components of a signal by exactly 90° while maintaining equal amplitude. By combining the original signal with its Hilbert transform (in quadrature), one sideband adds constructively and the other cancels. This is the DSP equivalent of the analog phasing method of SSB generation.

### E7F04
**Which method generates an SSB signal using digital signal processing?**
- A) Mixing products are converted to voltages and subtracted by adder circuits
- B) A frequency synthesizer removes unwanted sidebands
- C) Varying quartz crystal characteristics are emulated in digital form
- **D) Signals are combined in quadrature phase relationship** ✅

> DSP generates SSB by combining signals in quadrature phase relationship (I and Q channels, 90° apart). The in-phase (I) and quadrature (Q) components are processed so that one sideband adds constructively and the other cancels destructively. This is the phasing method implemented digitally. The precision of DSP makes the sideband suppression much better than analog phasing methods.

### E7F05
**How frequently must an analog signal be sampled to be accurately reproduced?**
- A) At least half the rate of the highest frequency component of the signal
- **B) At least twice the rate of the highest frequency component of the signal** ✅
- C) At the same rate as the highest frequency component of the signal
- D) At four times the rate of the highest frequency component of the signal

> The Nyquist theorem states that an analog signal must be sampled at least twice the rate of the highest frequency component to be accurately reproduced. This minimum rate is the Nyquist rate. For a 4 kHz audio signal, sample at ≥8 kHz. For an HF signal up to 30 MHz, sample at ≥60 MHz. Sampling below the Nyquist rate causes aliasing — false frequencies appear in the digitized signal.

### E7F06
**What is the minimum number of bits required to sample a signal with a range of 1 volt at a resolution of 1 millivolt?**
- A) 4 bits
- B) 6 bits
- C) 8 bits
- **D) 10 bits** ✅

> To resolve 1 millivolt in a 1V range: number of levels needed = 1V / 0.001V = 1000 levels. The number of bits N must satisfy 2^N ≥ 1000. 2^9 = 512 (not enough), 2^10 = 1024 ≥ 1000. So 10 bits are required. Each additional bit doubles the resolution. This is why high-resolution ADCs (16-24 bits) are used in precision measurements.

### E7F07
**What function is performed by a Fast Fourier Transform?**
- A) Converting analog signals to digital form
- B) Converting digital signals to analog form
- **C) Converting signals from the time domain to the frequency domain** ✅
- D) Converting signals from the frequency domain to the time domain

> A Fast Fourier Transform (FFT) converts signals from the time domain to the frequency domain. A time-domain signal (amplitude vs. time) is transformed into its frequency components (amplitude and phase vs. frequency). This is the mathematical basis of spectrum analyzers and waterfall displays in SDR software. The FFT is an efficient algorithm for computing the Discrete Fourier Transform.

### E7F08
**What is the function of decimation?**
- A) Converting data to binary-coded decimal form
- **B) Reducing the effective sample rate by removing samples** ✅
- C) Attenuating the signal
- D) Removing unnecessary significant digits

> Decimation reduces the effective sample rate by removing samples from the data stream. For example, keeping every 4th sample reduces the sample rate by a factor of 4. This is useful in SDRs where the ADC samples much faster than needed for the signal bandwidth. Decimation reduces the data rate and processing load while increasing effective bit resolution (through oversampling benefits).

### E7F09
**Why is an anti-aliasing filter required in a decimator?**
- **A) It removes high-frequency signal components that would otherwise be reproduced as lower** ✅
- B) It peaks the response of the decimator, improving bandwidth
- C) It removes low-frequency signal components to eliminate the need for DC restoration
- D) It notches out the sampling frequency to avoid sampling errors

> An anti-aliasing filter is required in a decimator because reducing the sample rate also reduces the Nyquist frequency. Without filtering, frequency components above the new Nyquist frequency would alias — appearing as false lower-frequency signals in the output. The anti-aliasing filter removes these high-frequency components before decimation to prevent this distortion.

### E7F10
**What aspect of receiver analog-to-digital conversion determines the maximum receive bandwidth of a direct-sampling software defined radio (SDR)?**
- **A) Sample rate** ✅
- B) Sample width in bits
- C) Integral non-linearity
- D) Differential non-linearity

> The ADC sample rate determines the maximum receive bandwidth of a direct-sampling SDR. By the Nyquist theorem, the usable bandwidth is at most half the sample rate. A 100 MHz ADC can digitize up to 50 MHz of bandwidth. Higher sample rates = wider receivable bandwidth. Bit width affects dynamic range and noise floor, not bandwidth.

### E7F11
**What sets the minimum detectable signal level for a direct-sampling software defined receiver in the absence of atmospheric or thermal noise?**
- A) Sample clock phase noise
- **B) Reference voltage level and sample width in bits** ✅
- C) Data storage transfer rate
- D) Missing codes and jitter

> In a direct-sampling SDR where the noise floor is above the ADC's quantization noise, the minimum detectable signal is set by the reference voltage level and sample width in bits. The reference voltage defines the full-scale range, and the number of bits determines how finely that range is divided. Theoretical dynamic range ≈ 6.02 × N + 1.76 dB (where N is the number of bits). A 14-bit ADC provides about 86 dB of dynamic range.

### E7F12
**Which of the following is generally true of Finite Impulse Response (FIR) filters?**
- **A) FIR filters can delay all frequency components of the signal by the same amount** ✅
- B) FIR filters are easier to implement for a given set of passband rolloff requirements
- C) FIR filters can respond faster to impulses
- D) All these choices are correct

> FIR (Finite Impulse Response) filters can delay all frequency components by the same amount — this is called linear phase response. Linear phase means no phase distortion — all frequencies pass through with identical delay. This is critical for digital communications where phase distortion causes intersymbol interference. IIR filters achieve the same rolloff with fewer taps but cannot guarantee linear phase.

### E7F13
**What is the function of taps in a digital signal processing filter?**
- A) To reduce excess signal pressure levels
- B) Provide access for debugging software
- C) Select the point at which baseband signals are generated
- **D) Provide incremental signal delays for filter algorithms** ✅

> Taps in a DSP filter provide incremental signal delays for filter algorithms. Each tap is a delay element (one sample period) followed by a multiply-and-accumulate operation. The collection of tap coefficients defines the filter's frequency response. More taps = more delay elements = more coefficients = sharper filter response. The coefficients are calculated using filter design algorithms (windowed sinc, Parks-McClellan, etc.).

### E7F14
**Which of the following would allow a digital signal processing filter to create a sharper filter response?**
- A) Higher data rate
- **B) More taps** ✅
- C) Lower Q
- D) Double-precision math routines

> More taps create a sharper filter response in a DSP filter. Each tap adds a degree of freedom in shaping the frequency response. More taps allow steeper rolloff, narrower transition bands, and deeper stopband rejection. The tradeoff: more taps require more computation and introduce more delay (latency). A filter with 64 taps has much sharper response than one with 16 taps.

## Group E7G — Active filters and op-amp circuits: active audio filters; op-amp circuits; op-amp applications; frequency response; gain bandwidth product

### E7G01
**What is the typical output impedance of an op-amp?**
- **A) Very low** ✅
- B) Very high
- C) 100 ohms
- D) 10,000 ohms

> An ideal op-amp has very low output impedance — typically fractions of an ohm with negative feedback applied. This means the op-amp can drive loads without significant voltage drop. The low output impedance is a result of the negative feedback reducing the open-loop output impedance by the loop gain factor. Without feedback, the output impedance is moderate (75-150 ohms for typical op-amps), but with feedback it drops to near zero.

### E7G02
**What is the frequency response of the circuit in E7-3 if a capacitor is added across the feedback resistor?**
- A) High-pass filter
- **B) Low-pass filter** ✅
- C) Band-pass filter
- D) Notch filter

> In the op-amp circuit of Figure E7-3 (inverting amplifier), adding a capacitor across the feedback resistor creates a low-pass filter. At low frequencies, the capacitor has high impedance and the circuit behaves as a normal inverting amplifier. At high frequencies, the capacitor's impedance drops, reducing the effective feedback impedance and thus reducing the gain. The result: gain decreases with increasing frequency — a low-pass response.

### E7G03
**What is the typical input impedance of an op-amp?**
- A) 100 ohms
- B) 10,000 ohms
- C) Very low
- **D) Very high** ✅

> An ideal op-amp has very high input impedance — approaching infinity. For real op-amps: bipolar input types (LM741) have input impedance of 1-10 MΩ, while FET-input types (TL071, OPA2134) have input impedance of 10^12 Ω or higher. High input impedance means the op-amp draws negligible current from the signal source, preventing loading effects.

### E7G04
**What is meant by the term “op-amp input offset voltage”?**
- A) The output voltage of the op-amp minus its input voltage
- B) The difference between the output voltage of the op-amp and the input voltage required in the
- **C) The differential input voltage needed to bring the open loop output voltage to zero** ✅
- D) The potential between the amplifier input terminals of the op-amp in an open loop condition

> Op-amp input offset voltage is the small differential voltage that must be applied between the input terminals to bring the output to exactly zero volts (in open-loop configuration). Real op-amps have slight mismatches between their internal transistor pairs, causing a small output voltage even with zero input. The offset voltage is typically 1-10 mV and can be nulled with a trim pot.

### E7G05
**How can unwanted ringing and audio instability be prevented in an op-amp audio filter?**
- **A) Restrict both gain and Q** ✅
- B) Restrict gain but increase Q
- C) Restrict Q but increase gain
- D) Increase both gain and Q

> Unwanted ringing and instability in op-amp audio filters can be prevented by restricting both gain and Q. High Q creates sharp resonance peaks that can ring (oscillate briefly after a transient). High gain amplifies noise and increases the tendency to oscillate. Keeping both gain and Q moderate ensures stable operation. The gain-bandwidth product of the op-amp sets the ultimate limit.

### E7G06
**What is the gain-bandwidth of an operational amplifier?**
- A) The maximum frequency for a filter circuit using that type of amplifier
- **B) The frequency at which the open-loop gain of the amplifier equals one** ✅
- C) The gain of the amplifier at a filter’s cutoff frequency
- D) The frequency at which the amplifier’s offset voltage is zero

> The gain-bandwidth product (GBW) of an op-amp is the frequency at which the open-loop gain drops to unity (1, or 0 dB). For example, an op-amp with GBW = 1 MHz has gain of 1000 at 1 kHz, gain of 100 at 10 kHz, and gain of 1 at 1 MHz. Gain × bandwidth = constant. This means you trade gain for bandwidth: more gain = less bandwidth, and vice versa.

### E7G07
**What voltage gain can be expected from the circuit in Figure E7-3 when R1 is 10 ohms and RF is 470 ohms?**
- A) 0.21
- B) 4700
- **C) 47** ✅
- D) 24

> The inverting op-amp gain = -RF/R1. With R1 = 10 ohms and RF = 470 ohms: Gain = -470/10 = -47. The magnitude (absolute voltage gain) is 47. The negative sign indicates phase inversion (180° phase shift). This is the fundamental inverting amplifier formula — the gain is set entirely by the external resistor ratio, independent of the op-amp's open-loop gain.

### E7G08
**How does the gain of an ideal operational amplifier vary with frequency?**
- A) It increases linearly with increasing frequency
- B) It decreases linearly with increasing frequency
- C) It decreases logarithmically with increasing frequency
- **D) It does not vary with frequency** ✅

> An ideal operational amplifier has infinite open-loop gain that does NOT vary with frequency. Real op-amps have very high gain at DC (typically 100,000 to 1,000,000) that decreases with frequency, but the IDEAL op-amp model assumes constant gain at all frequencies. This simplification makes circuit analysis tractable and is valid within the gain-bandwidth product range.

### E7G09
**What will be the output voltage of the circuit shown in Figure E7-3 if R1 is 1,000 ohms, RF is 10,000 ohms, and 0.23 volts DC is applied to the input?**
- A) 0.23 volts
- B) 2.3 volts
- C) -0.23 volts
- **D) -2.3 volts** ✅

> Using the inverting op-amp formula: V_out = -(RF/R1) × V_in. With R1 = 1,000 ohms, RF = 10,000 ohms, and V_in = 0.23V: V_out = -(10,000/1,000) × 0.23 = -10 × 0.23 = -2.3 volts. The negative sign indicates phase inversion. The output is -2.3V.

### E7G10
**What absolute voltage gain can be expected from the circuit in Figure E7-3 when R1 is 1,800 ohms and RF is 68 kilohms?**
- A) 1
- B) 0.03
- **C) 38** ✅
- D) 76

> Absolute voltage gain = RF/R1 = 68,000/1,800 = 37.78 ≈ 38. The inverting amplifier's gain magnitude is simply the ratio of the feedback resistor to the input resistor. The absolute value ignores the phase inversion (negative sign).

### E7G11
**What absolute voltage gain can be expected from the circuit in Figure E7-3 when R1 is 3,300 ohms and RF is 47 kilohms?**
- A) 28
- **B) 14** ✅
- C) 7
- D) 0.07

> Absolute voltage gain = RF/R1 = 47,000/3,300 = 14.24 ≈ 14. Again, this is straightforward resistor ratio calculation for an inverting op-amp configuration.

### E7G12
**What is an operational amplifier?**
- **A) A high-gain, direct-coupled differential amplifier with very high input impedance and very low output** ✅
- B) A digital audio amplifier whose characteristics are determined by components external to the
- C) An amplifier used to increase the average output of frequency modulated amateur signals to the legal
- D) A RF amplifier used in the UHF and microwave regions

> An operational amplifier is a high-gain, direct-coupled differential amplifier with very high input impedance and very low output impedance. These three characteristics (high gain, high Zin, low Zout) make it nearly ideal for building amplifiers, filters, oscillators, and signal-processing circuits whose characteristics are determined by external components rather than the op-amp itself.

## Group E7H — Oscillators and signal sources: types of oscillators; oscillator stability; synthesizers; phase-locked loops; frequency dividers; signal sources

### E7H01
**What are three common oscillator circuits?**
- A) Taft, Pierce, and negative feedback
- B) Pierce, Fenner, and Beane
- C) Taft, Hartley, and Pierce
- **D) Colpitts, Hartley, and Pierce** ✅

> The three most common oscillator circuits are Colpitts, Hartley, and Pierce. Colpitts uses a capacitive voltage divider for feedback. Hartley uses a tapped inductor (or inductive voltage divider). Pierce uses a quartz crystal for frequency-determining feedback. All three use positive feedback at the resonant frequency to sustain oscillation. The Barkhausen criterion requires loop gain ≥ 1 and phase shift = 0° (or 360°) at the oscillation frequency.

### E7H02
**What is a microphonic?**
- A) An IC used for amplifying microphone signals
- B) Distortion caused by RF pickup on the microphone cable
- **C) Changes in oscillator frequency caused by mechanical vibration** ✅
- D) Excess loading of the microphone by an oscillator

> A microphonic is a change in oscillator frequency caused by mechanical vibration. Physical shock or vibration causes small movements in oscillator components (particularly variable capacitors, crystals, or inductors), which changes their values slightly, shifting the oscillator frequency. This creates unwanted FM on the transmitted signal. The name comes from the way a microphone converts mechanical vibration to electrical signals.

### E7H03
**What is a phase-locked loop?**
- A) An electronic servo loop consisting of a ratio detector, reactance modulator, and voltage-controlled
- B) An electronic circuit also known as a monostable multivibrator
- **C) An electronic servo loop consisting of a phase detector, a low-pass filter, a voltage-controlled** ✅
- D) An electronic circuit consisting of a precision push-pull amplifier with a differential phase input

> A phase-locked loop (PLL) is an electronic servo loop consisting of: a phase detector, a low-pass filter, and a voltage-controlled oscillator (VCO). The phase detector compares the VCO output to a reference signal. The error voltage (filtered) adjusts the VCO to maintain phase lock. PLLs are used for frequency synthesis, FM demodulation, clock recovery, and frequency multiplication.

### E7H04
**How is positive feedback supplied in a Colpitts oscillator?**
- A) Through a tapped coil
- B) Through link coupling
- **C) Through a capacitive divider** ✅
- D) Through a neutralizing capacitor

> In a Colpitts oscillator, positive feedback is supplied through a capacitive divider — two capacitors in series across the tuned circuit. The junction of the two capacitors provides the feedback voltage. The feedback fraction is determined by the capacitance ratio. The Colpitts is one of the most common LC oscillators, known for good stability and spectral purity.

### E7H05
**How is positive feedback supplied in a Pierce oscillator?**
- A) Through a tapped coil
- B) Through link coupling
- C) Through a neutralizing capacitor
- **D) Through a quartz crystal** ✅

> In a Pierce oscillator, positive feedback is supplied through a quartz crystal. The crystal operates between its series and parallel resonant frequencies, providing the precise frequency-selective feedback path. The Pierce oscillator is extremely common in digital systems (every microcontroller crystal oscillator is a Pierce) and produces very stable frequency output.

### E7H06
**Which of these functions can be performed by a phase-locked loop?**
- A) Wide-band AF and RF power amplification
- **B) Frequency synthesis and FM demodulation** ✅
- C) Photovoltaic conversion and optical coupling
- D) Comparison of two digital input signals and digital pulse counting

> A phase-locked loop can perform frequency synthesis and FM demodulation. For frequency synthesis: placing a programmable divider in the feedback path allows the VCO to lock at any multiple of the reference frequency. For FM demodulation: when the PLL tracks an FM signal, the VCO control voltage follows the frequency deviations, which IS the demodulated audio. PLLs are fundamental to modern transceiver design.

### E7H07
**How can an oscillator’s microphonic responses be reduced?**
- A) Use NP0 capacitors
- B) Reduce noise on the oscillator’s power supply
- C) Increase the gain
- **D) Mechanically isolate the oscillator circuitry from its enclosure** ✅

> Microphonic responses are reduced by mechanically isolating the oscillator circuitry from its enclosure. This means shock mounting the oscillator board or components using rubber grommets, foam padding, or other vibration-absorbing materials. The goal is to prevent external vibrations from reaching the frequency-determining components. Some designs pot (encapsulate) the oscillator in epoxy for maximum isolation.

### E7H08
**Which of the following components can be used to reduce thermal drift in crystal oscillators?**
- **A) NP0 capacitors** ✅
- B) Toroidal inductors
- C) Wirewound resistors
- D) Non-inductive resistors

> NP0 (Negative-Positive-Zero, also called C0G) capacitors have essentially zero temperature coefficient — their capacitance doesn't change with temperature. Using NP0 capacitors in a crystal oscillator's external circuit minimizes frequency drift due to temperature changes. Other capacitor types (X7R, Y5V) have significant temperature coefficients that would cause the oscillator frequency to drift.

### E7H09
**What type of frequency synthesizer circuit uses a phase accumulator, lookup table, digital-to-analog converter, and a low-pass anti-alias filter?**
- **A) A direct digital synthesizer** ✅
- B) A hybrid synthesizer
- C) A phase-locked loop synthesizer
- D) A direct conversion synthesizer

> A Direct Digital Synthesizer (DDS) uses a phase accumulator, lookup table, digital-to-analog converter, and low-pass filter. The phase accumulator increments by a tuning word each clock cycle. The accumulated phase value indexes a sine wave lookup table. The DAC converts the digital sine values to an analog voltage, and the low-pass filter removes sampling artifacts. DDS provides very fine frequency resolution and fast switching.

### E7H10
**What information is contained in the lookup table of a direct digital synthesizer (DDS)?**
- A) The phase relationship between a reference oscillator and the output waveform
- **B) Amplitude values that represent the desired waveform** ✅
- C) The phase relationship between a voltage-controlled oscillator and the output waveform
- D) Frequently used receiver and transmitter frequencies

> The DDS lookup table contains amplitude values that represent the desired waveform — typically a sine wave. The phase accumulator generates addresses into this table, and the looked-up amplitude values are sent to the DAC. By changing the phase increment (tuning word), the output frequency changes. The lookup table can also store other waveform shapes.

### E7H11
**What are the major spectral impurity components of direct digital synthesizers?**
- A) Broadband noise
- B) Digital conversion noise
- **C) Spurious signals at discrete frequencies** ✅
- D) Harmonics of the local oscillator

> The major spectral impurity of DDS is spurious signals at discrete frequencies (called 'spurs'). These arise from: phase truncation (not all accumulator bits are used as table address), DAC quantization, and DAC nonlinearity. The spurs appear at predictable frequencies related to the tuning word and clock frequency. DDS phase noise is generally good (determined by the reference clock), but the discrete spurs can be problematic for sensitive receiver applications.

### E7H12
**Which of the following ensures that a crystal oscillator operates on the frequency specified by the crystal manufacturer?**
- A) Provide the crystal with a specified parallel inductance
- **B) Provide the crystal with a specified parallel capacitance** ✅
- C) Bias the crystal at a specified voltage
- D) Bias the crystal at a specified current

> Crystal oscillators require a specified parallel capacitance (load capacitance) to operate on the marked frequency. Crystals are manufactured for a specific load capacitance (typically 18 pF or 20 pF). If the external circuit presents a different capacitance, the oscillator frequency shifts. Providing the correct load capacitance ensures the crystal operates at its specified frequency.

### E7H13
**Which of the following is a technique for providing highly accurate and stable oscillators needed for microwave transmission and reception?**
- A) Use a GPS signal reference
- B) Use a rubidium stabilized reference oscillator
- C) Use a temperature-controlled high Q dielectric resonator
- **D) All these choices are correct** ✅

> All three choices provide highly accurate and stable oscillator references: (1) GPS signal reference — disciplined by atomic clocks on GPS satellites, accuracy to 10^-12. (2) Rubidium stabilized reference — atomic clock technology, excellent long-term stability. (3) Temperature-controlled high-Q dielectric resonator — excellent short-term stability at microwave frequencies. All these choices are correct.
