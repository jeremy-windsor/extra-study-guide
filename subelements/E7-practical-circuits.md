# E7 — Practical Circuits

Practical circuits are where a lot of separate Extra-class topics finally snap together.

Up to this point, you have seen theory, components, propagation, operating practice, and electrical principles. E7 is about how those ideas are assembled into real working circuit blocks: logic circuits that count and divide, amplifiers that trade efficiency against linearity, filters that shape signals, power supplies that regulate voltage, modulators and detectors that move information onto and off of carriers, DSP systems that replace hardware with math, op-amp circuits that build useful analog functions, and oscillators that create stable signals in the first place.

This is one of the broadest Extra subelements. The pool has **99 questions**, and the exam pulls **8** of them. The question count is large because E7 is really a tour of modern radio design.

The groups are:

- **E7A:** digital circuits and logic concepts
- **E7B:** amplifier classes, biasing, and stability
- **E7C:** filters and impedance-matching networks
- **E7D:** power supplies and voltage regulators
- **E7E:** modulation, demodulation, and mixer behavior
- **E7F:** DSP and software-defined radio concepts
- **E7G:** op-amps and active filters
- **E7H:** oscillators, PLLs, and synthesizers

The easiest way to study E7 is not to memorize 99 isolated facts. Instead, keep asking:

1. **What job is this circuit block doing?**
2. **What tradeoff is it making?**
3. **Why is this approach preferred in radio equipment?**

That turns E7 from a long checklist into a connected picture of how actual transceivers and amplifiers are built.

---

## Group E7A — Digital circuits and logic building blocks

Digital circuitry is built from a small number of simple ideas: stable states, logic decisions, and timing.

The pool touches flip-flops, counters, multivibrators, gates, truth tables, and logic conventions. These are basic blocks, but they appear everywhere in radio gear: frequency counters, synthesizer dividers, microcontroller interfaces, keyers, timers, display logic, and control systems.

### Bistable, monostable, and astable: three useful timing behaviors

One of the cleanest E7A distinctions is between the three classic multivibrator behaviors:

- **Bistable**: two stable states
- **Monostable**: one stable state, one temporary state
- **Astable**: no stable state; continuously oscillates

A **flip-flop** is the classic **bistable** circuit. It can store one bit of information because it stays in one of two stable states until something makes it switch.

A **monostable multivibrator** is a one-shot. It normally rests in one state, then when triggered it moves to the other state briefly and returns after a preset time. This is useful for pulse stretching, switch debouncing, timing delays, and creating clean fixed-length pulses.

An **astable multivibrator** never settles. It alternates continuously between two states on its own, which means it acts as an oscillator. If you want a square wave without an external clock, astable is the behavior you want.

That gives you a simple memory shortcut:

- **bi** = two stable states
- **mono** = one stable state
- **a**stable = no stable state

### Flip-flops as memory and frequency dividers

A flip-flop is not just a memory element. It is also a frequency divider.

If a flip-flop is arranged so it toggles on each input pulse, its output changes state once for every input cycle. That makes the output frequency exactly **one-half** of the input frequency.

This matters because cascading flip-flops gives you powers-of-two division:

- 1 flip-flop → divide by 2
- 2 flip-flops → divide by 4
- 3 flip-flops → divide by 8
- 4 flip-flops → divide by 16

That is why a divide-by-16 circuit requires **4 flip-flops**. In general, if you need division by 2^N, you need N flip-flops.

This same idea is used all over frequency synthesis and digital counting. A counter is really just a controlled arrangement of flip-flops.

### Decade counters and counting by 10

A **decade counter** is different from a pure binary divider chain. Instead of counting through all 2^N states, it counts **ten states**, from 0 through 9, then resets.

That means it produces one output pulse for every **10 input pulses**. In other words, it divides by 10.

Binary counters are natural for digital design because powers of two fall out of flip-flop stages automatically. A decade counter is what you use when the application is decimal-oriented, such as display driving or decimal counting.

### Logic gates: understand the behavior, not just the names

You do not need to memorize dozens of truth tables if you understand what each gate is doing.

#### OR gate
An **OR** gate produces a **1** if **any** input is 1. It only outputs 0 when **all** inputs are 0.

That makes OR a “one or more” detector.

#### NAND gate
A **NAND** gate is an **AND** gate followed by inversion.

An AND gate would output 1 only when all inputs are 1. So NAND does the opposite:

- it outputs **0 only when all inputs are 1**
- otherwise it outputs 1

NAND matters because it is a universal gate. In practice, many digital functions can be built entirely from NANDs.

#### XNOR gate
An **exclusive NOR** gate, or **XNOR**, outputs 1 when its inputs are the **same** and 0 when they are **different**.

For two inputs, that means it outputs **0 when one and only one input is 1**.

That makes XNOR a coincidence or equality detector.

### Truth tables: the complete definition of logic behavior

A **truth table** is simply a list of all possible input combinations and the corresponding output for a digital device.

This is important because digital circuits are defined by state behavior. A schematic symbol tells you what family of function a device belongs to; the truth table tells you exactly how it behaves.

For a 2-input device, there are 2² = 4 possible input combinations. For a 3-input device, there are 2³ = 8. The truth table lays them all out.

If you understand truth tables, you understand why digital circuits can be predictable and testable in a way analog circuits often are not.

### Positive logic

In **positive logic**, a **high voltage** represents logic **1**, and a **low voltage** represents logic **0**.

That is the normal convention in most modern digital electronics. The main exam point is not to overthink it. Positive logic does not mean the circuit is “good” or that both states are positive voltages. It just defines which voltage level corresponds to 1 and which corresponds to 0.

### The practical viewpoint for E7A

The digital-circuit questions in E7 are really checking whether you can recognize a few standard jobs:

- **store a state** → flip-flop
- **make a timed pulse** → monostable
- **make a continuous square wave** → astable
- **divide frequency** → flip-flops/counters
- **combine conditions logically** → gates
- **describe behavior completely** → truth table

If you keep the functional role clear, the questions become much easier than they look.

---

## Group E7B — Amplifiers, bias, conduction angle, and stability

This group is one of the most practical parts of the Extra exam because it deals with how amplifiers actually behave.

The big themes are:

- **how long the device conducts during each cycle**
- **how linear the amplifier is**
- **how efficient it is**
- **how the bias network sets the operating point**
- **how parasitics can make a power amplifier misbehave**

### Amplifier classes are mostly about conduction angle and tradeoffs

If you strip away the terminology, the amplifier classes are about one central tradeoff:

- more linearity usually means less efficiency
- more efficiency usually means more distortion unless the signal type tolerates it

### Class A

A **Class A** amplifier conducts for the **entire 360 degrees** of the signal cycle.

To make that possible, the transistor or tube is biased well into its active region. The operating point, or **Q-point**, is usually set approximately **halfway between cutoff and saturation** so the signal can swing in both directions without clipping.

Why use Class A?

- best linearity
- lowest distortion
- simple behavior

Why avoid it for high power?

- poor efficiency
- lots of heat

It is the most forgiving class electrically, but the least attractive for power efficiency.

### Class B and Class AB

A **Class B** stage conducts for **180 degrees** of the cycle per device. In push-pull form, one device handles one half-cycle and the other handles the opposite half.

This improves efficiency, but pure Class B has a problem: **crossover distortion** around the point where one device hands off to the other.

That is why practical linear RF power amplifiers often use **Class AB** instead. In Class AB, each active device conducts for **more than 180 degrees but less than 360 degrees**.

This small extra conduction overlap reduces crossover distortion while keeping efficiency much better than Class A.

That is the usual Extra-class exam takeaway:

- **Class A**: 360°
- **Class B**: 180°
- **Class AB**: more than 180°, less than 360°
- **Class C**: less than 180°

### Class C: efficient but not linear

A **Class C** amplifier conducts for **less than 180 degrees** of the cycle.

That makes it efficient, but very nonlinear. The waveform is heavily distorted at the device itself, so it only works well when a tuned circuit can recover the desired RF sinusoid and when the signal envelope does not need to be preserved.

That is why Class C is fine for some constant-envelope RF applications, but it is a terrible choice for **SSB**. If you run SSB through Class C, the varying envelope gets mangled, producing **distortion and excessive bandwidth**.

That is a real operating issue, not just an exam issue. Nonlinear amplification of SSB creates splatter.

### Class D and switching amplifiers

A **Class D** amplifier uses **switching** rather than linear operation.

The active device spends most of its time either:

- fully **on** (saturated), or
- fully **off** (cut off)

That minimizes power dissipation because high current and high voltage across the device do not occur at the same time for long. That is why switching amplifiers are more efficient than linear amplifiers.

But switching comes with a price: the output waveform contains lots of harmonics. In RF service, the amplifier output must therefore feed a **filter** to remove harmonic content before the signal is usable on the air.

This is one of the most important “why” ideas in the whole section:

- switching gives efficiency
- filtering cleans up the resulting spectrum

### Push-pull and emitter followers

A **push-pull** stage uses two active devices working on opposite halves of the waveform. This is common in Class B and Class AB designs because it improves efficiency and symmetry.

An **emitter follower**, also called a **common collector** amplifier, has a different role. Its important characteristic is that the **input and output are in phase**. It usually has:

- high input impedance
- low output impedance
- current gain
- voltage gain near 1

So the emitter follower is mostly a **buffer** or impedance-matching stage, not a voltage-gain stage.

### Grounded-grid amplifiers

A **grounded-grid** amplifier is known for **low input impedance**.

That is a practical trait, because it can make matching to a low-impedance source easier. Grounded-grid designs are also known for good stability because the grounded grid provides shielding between input and output.

For exam purposes, “grounded-grid” should make you think **low input impedance**.

### Bias networks: what the resistors are doing

The pool includes figure questions about a transistor amplifier using resistors labeled R1, R2, and R3.

The important concepts are general:

- **R1 and R2** forming a divider are typically **voltage-divider bias**
- **R3** in the emitter lead typically provides **self-bias** or emitter degeneration

The divider sets the base voltage. The emitter resistor then provides feedback: if emitter current rises, the voltage across the emitter resistor rises, which reduces effective base-emitter drive and pushes the current back down.

That is why emitter resistors stabilize operating point against transistor gain variation and temperature drift.

The overall stage in that figure is a **common-emitter amplifier**.

### Preventing parasitic oscillation

RF power amplifiers do not always fail gracefully. Unwanted feedback through stray capacitance, lead inductance, or internal device capacitance can produce oscillation at frequencies you never intended.

Two classic cures are:

- **parasitic suppressors**
- **neutralization**

Parasitic suppressors add damping to kill unwanted high-frequency resonances. Neutralization feeds back a carefully phased cancelling signal to oppose the unwanted internal feedback path.

If the question asks how to prevent unwanted oscillations in an RF power amplifier, that is the answer direction: **stability measures**, not tuning tricks.

### The practical viewpoint for E7B

If you remember only a few things from this group, make them these:

- conduction angle defines the amplifier class
- Class AB is the common linear compromise
- Class C is not for SSB
- switching amplifiers need output filtering
- Class A Q-point sits near midline between cutoff and saturation
- grounded-grid means low input impedance
- emitter follower means in-phase buffering
- bias resistors set and stabilize the operating point

That is enough to answer a large fraction of E7B correctly.

---

## Group E7C — Filters and impedance-matching networks

Filters and matching networks are central to radio design because RF circuits rarely want “everything.” They want:

- one frequency range, not all frequencies
- one impedance, not whatever the load happens to be
- the desired signal, not its harmonics
- nearby channels rejected as much as possible

This group combines two related ideas:

1. **frequency selection**
2. **impedance transformation**

### Pi and T networks: recognize the shape and the job

A **Pi-network** gets its name from looking like the Greek letter π:

- shunt element at the input
- series element in the middle
- shunt element at the output

For a **low-pass Pi-network**, the arrangement is:

- capacitor from input to ground
- inductor in series from input to output
- capacitor from output to ground

That low-pass behavior makes sense physically:

- the series inductor resists rapid changes, helping block high-frequency components
- the shunt capacitors provide a low-impedance path to ground for higher frequencies

This is why Pi networks are commonly used in transmitter output stages: they can both **match impedance** and **suppress harmonics**.

A **T-network** is the complementary shape. The pool emphasizes a T with:

- series capacitors
- shunt inductor

That configuration is a **high-pass** network.

Again, the component behavior explains it:

- series capacitors block low frequencies better than high
- a shunt inductor is a lower impedance at low frequency than at high frequency

### Pi-L network: why add another inductor?

A **Pi-L** network is a Pi-network with an additional **series output inductor**.

The reason for adding that element is **greater harmonic suppression**.

That is a classic exam point. The extra section makes the low-pass response steeper, which means unwanted harmonics are attenuated more strongly.

So if the question asks what the added inductor does, the answer is not “make it simpler” or “remove a capacitor.” It is mainly about **better filtering**.

### What impedance matching really does

An impedance-matching network takes a complex impedance and transforms it into the resistive value the source wants to see.

That requires two separate actions:

1. **cancel the reactive part**
2. **transform the resistive part** to the desired value

This is an important conceptual point. A mismatch is not fixed just by changing resistance or just by “absorbing” reactance somewhere. The reactive part has to be cancelled with equal and opposite reactance, and then the remaining resistive value has to be transformed.

That is why matching networks use inductors and capacitors. Their reactance can cancel existing reactance and also create impedance transformation through the network geometry.

### Filter families: what each one is trading

The pool asks about several named filter responses. The easiest way to remember them is by their tradeoffs.

#### Butterworth
A **Butterworth** filter is the “maximally flat” response in the passband. It has no ripple there, but its cutoff is not the sharpest possible.

#### Chebyshev
A **Chebyshev** filter allows **passband ripple** in exchange for a **sharper cutoff** than Butterworth of the same order.

That is the exam point: **ripple in the passband, sharp cutoff**.

#### Elliptical
An **elliptical** filter has the **sharpest cutoff** for a given order, but it does that by accepting ripple and by creating one or more **notches in the stopband**.

If Chebyshev is “sharper than Butterworth,” elliptical is the extreme version with even more aggressive behavior.

### Specialized RF filters

Some filter types in E7C are really about application.

#### Helical filters
A **helical filter** is commonly used as a **band-pass or notch filter at VHF and UHF**. These are compact, high-Q structures useful where ordinary lumped LC circuits start to lose selectivity.

#### Crystal lattice filters
A **crystal lattice filter** is a very selective filter for **low-level signals** using quartz crystals. Because crystals have very high Q, they are ideal for narrow IF filtering in receivers and SSB equipment.

#### Cavity filters
A **cavity filter** is the classic answer for a **2-meter repeater duplexer**. Duplexers need very high selectivity and isolation between transmitter and receiver frequencies that are relatively close together. Cavities provide that.

### Shape factor

**Shape factor** measures how well a filter rejects signals in adjacent channels. In practical terms, it tells you how steep the filter skirts are.

A filter with a better shape factor has a more rectangular response:

- it passes what you want
- then drops off quickly
- and strongly rejects nearby unwanted signals

That is why shape factor is tied directly to adjacent-channel rejection.

### The practical viewpoint for E7C

This group becomes manageable if you reduce it to a few questions:

- What network shape is it?
- Is it low-pass or high-pass?
- Is the goal filtering, matching, or both?
- What tradeoff does the filter family make?
- What real hardware is used at HF, VHF/UHF, or duplexer power levels?

The high-value memory points are:

- low-pass Pi = shunt C, series L, shunt C
- T with series C and shunt L = high-pass
- Pi-L = more harmonic suppression
- matching = cancel reactance and transform resistance
- Chebyshev = ripple plus sharper cutoff
- elliptical = extremely sharp cutoff with stopband notches
- shape factor = adjacent-channel rejection quality

---

## Group E7D — Power supplies and voltage regulators

Every radio depends on power that is clean, stable, and appropriate to the circuits it feeds.

E7D covers the practical chain from raw DC to regulated DC, plus a few real-world concerns like inrush current, capacitor balancing, and battery life.

### Linear regulation: smooth control, more heat

A **linear regulator** works by varying the conduction of a **control element** so the output voltage remains constant.

Usually that control element is a **series pass transistor** operating in its active region. The regulator continuously adjusts how much voltage is dropped across that device.

If the input rises, the pass element drops more voltage.
If the load current changes, the pass element adjusts again.

That makes linear regulation conceptually simple and electrically quiet, but it creates heat. The lost power is the voltage difference times the load current.

That is why the power dissipation formula for a series linear regulator is:

**P = (V_in − V_out) × I_out**

This is one of the most important formulas in the group.

### Switching regulation: duty cycle instead of dissipation

A **switchmode regulator** works differently. Instead of continuously adjusting conduction in the linear region, it varies the **duty cycle of pulses** feeding a filter.

The active device switches rapidly between on and off, and an output filter averages the pulses into steady DC.

That gives high efficiency because the device spends little time in the high-voltage/high-current dissipation region.

This is the same core reason switching amplifiers are efficient: the active device is mostly at **saturation or cutoff**.

### Series vs. shunt regulators

A **three-terminal voltage regulator** is a **series regulator**. The regulating element sits in series with the load and controls current flow to it.

A **shunt regulator** works by loading the unregulated source. It diverts extra current away from the load to hold the voltage constant.

Shunt regulation is simpler but less efficient because it intentionally burns power whenever it is regulating.

A Zener-diode regulator is the classic simple shunt regulator.

### Zener diode as a reference

A **Zener diode** is commonly used as a **stable voltage reference**. In reverse breakdown, it maintains a nearly constant voltage across it over a useful current range.

That is why it shows up in regulator circuits. A stable reference is the anchor the feedback system compares against.

### Understanding the typical linear regulator figure

The E7D figure questions ask about a linear regulator containing Q1, D1, and C2.

The underlying roles are common:

- **Q1** is the control or pass element that regulates current to keep output voltage constant
- **D1** is the reference element, usually a Zener
- **C2** bypasses ripple around the reference so the regulator compares against a steadier voltage

This is useful beyond the exam because it teaches you how to look at a regulator schematic: first identify the pass element, then the reference, then the feedback path, then the filtering.

### Battery operating time

Battery life questions are straightforward if you remember the basic relation:

**Operating time = capacity in amp-hours ÷ average current in amps**

So a 12 Ah battery feeding an average 2 A load lasts about 6 hours.

The word **average** matters. In radio service, current often changes a lot between receive and transmit, so the real calculation depends on duty cycle.

### Why switching supplies are smaller and lighter

A switching supply is lighter and usually less expensive than an equivalent linear supply mainly because it uses a **high-frequency inverter design**.

At high frequency, you can use:

- smaller transformers
- smaller inductors
- smaller capacitors

That is the central reason, not that switching supplies magically eliminate filtering or recover unused half-cycles.

### Inverters and solar systems

An **inverter** connected to a solar panel system converts the panel’s output from **DC to AC**.

That is the whole job. Solar panels produce DC. Homes and the grid use AC. The inverter bridges that gap.

### Dropout voltage

The **dropout voltage** of a linear regulator is the **minimum input-to-output voltage difference required to maintain regulation**.

If the input falls too close to the desired output, the pass element no longer has enough headroom to control properly, and the output begins to sag.

That is why low-dropout regulators are useful in battery-powered gear where every volt of headroom matters.

### Series filter capacitors and equalizing resistors

When filter capacitors are placed in series in a high-voltage supply, equal-value resistors are often connected across each capacitor.

Those resistors do three helpful things:

- help **equalize the voltage** across the capacitors
- **discharge** them when power is removed
- provide a small **minimum load**

That is why the correct answer is effectively “all of the above.”

This is one of those exam facts that is also an important bench safety habit.

### Step-start circuits

A **step-start** circuit in a high-voltage power supply allows the filter capacitors to **charge gradually**.

Without step-start, the initial charging current into large empty capacitors can be enormous. That inrush can stress switches, relays, rectifiers, and fuses.

So the step-start circuit is there to soften startup, not to provide adjustable output or regulate line voltage.

### The practical viewpoint for E7D

Most of the questions in this group are checking whether you understand the functional difference between:

- **linear control** and **switching control**
- **series regulation** and **shunt regulation**
- **reference**, **pass element**, and **filtering**

The most useful memory items are:

- linear regulator varies conduction of a control element
- switcher varies duty cycle of pulses into a filter
- Zener = stable reference
- shunt regulator loads the source
- battery time = Ah ÷ average current
- switching supplies are smaller because of higher operating frequency
- dropout = minimum input-output difference for regulation
- regulator dissipation = voltage drop × output current

---

## Group E7E — Modulation, demodulation, and mixer behavior

This group is about how information is put onto a carrier, taken back off, and translated between frequencies.

These are not separate unrelated ideas. In a real radio:

- an oscillator creates a carrier
- modulation puts information on it
- mixers shift it to useful frequencies
- detectors recover the original baseband

### Baseband first, RF later

The word **baseband** means the frequency range occupied by the **original message signal before modulation**.

For voice, baseband is the audio range. For data or video, baseband may be much wider.

This matters because modulation is really a translation process: you are taking baseband information and moving it to RF so it can be transmitted efficiently.

### FM generation with reactance modulation

A classic way to generate FM is **reactance modulation of a local oscillator**.

A **reactance modulator** changes the effective reactance in the oscillator’s tuned circuit, usually by varying an effective **capacitance**. That changes the oscillator frequency in step with the audio signal, producing frequency or phase modulation.

For exam purposes, the key point is:

- reactance modulation works by varying **capacitance** in the oscillator system

### FM detection with a discriminator

A **frequency discriminator** is a circuit for **detecting FM signals**.

Its job is to convert frequency variation back into voltage variation that matches the original audio.

That makes it the FM analog of an envelope detector in AM reception.

### SSB generation: balanced modulator plus filter

A standard way to generate **single sideband** is:

1. use a **balanced modulator** to create a double-sideband suppressed-carrier signal
2. use a **filter** to remove one sideband

That is the classic filter method of SSB generation.

The balanced modulator removes the carrier. The filter then chooses whether the remaining output is USB or LSB.

### Pre-emphasis and de-emphasis

FM systems often use **pre-emphasis** in the transmitter and **de-emphasis** in the receiver.

A **pre-emphasis network** boosts the higher audio frequencies before modulation.

A **de-emphasis network** in the receiver then restores the original balance while also reducing high-frequency noise.

The exam pool specifically connects de-emphasis to compatibility with transmitters using **phase modulation**, since PM inherently emphasizes high audio frequencies compared with FM.

You do not need to turn this into a philosophical fight about all FM implementations. For the exam, keep the tested relationship straight:

- pre-emphasis boosts highs before transmission
- de-emphasis reduces them again at reception
- this fits PM/FM system behavior and improves recovered audio/noise performance

### Mixers: sum and difference machines

A **mixer** is one of the most important circuits in radio. Feed it two frequencies and, due to nonlinearity, it produces outputs including:

- the two original input frequencies
- the **sum** frequency
- the **difference** frequency

Those are the principal products the exam cares about.

This is the heart of the superheterodyne receiver, where an incoming RF signal and local oscillator are mixed to create an intermediate frequency.

### Mixer overload and spurious products

When the input levels to a mixer are too high, the mixer generates **spurious mixer products**.

That is a predictable consequence of driving a nonlinear device beyond its intended operating range. Instead of producing only the desired sum and difference products cleanly, it creates a mess of intermodulation terms.

If you remember one practical lesson here, make it this: mixers are useful because they are nonlinear, but if they are **too nonlinear**, they become dirty.

### Envelope detection for AM

A **diode envelope detector** works by **rectification and filtering** of the RF signal.

The diode passes one polarity of the carrier peaks, and the RC network smooths the waveform so it follows the modulation envelope. That recovered envelope is the original audio.

This is one of the simplest detector circuits in all of radio.

### Product detection for SSB

A **product detector** is used to demodulate **SSB**.

This makes sense because SSB suppresses the carrier. To recover the audio, the receiver has to reinsert a carrier-like signal locally and mix it with the incoming SSB. That multiplication process is what the product detector does.

Without it, SSB would not sound like intelligible speech.

### The practical viewpoint for E7E

The efficient way to think about this group is by function:

- FM generation → reactance modulation
- FM detection → discriminator
- SSB generation → balanced modulator + filter
- AM detection → envelope detector
- SSB detection → product detector
- frequency translation → mixer
- original message range → baseband

Once you keep the signal-flow story straight, the details stop feeling random.

---

## Group E7F — DSP and software-defined radio techniques

This group can feel modern compared with some of the older circuit topics, but the underlying ideas are still the same: filtering, frequency translation, and detection.

The difference is that DSP does these jobs with **sampling and computation** instead of only with analog hardware.

### Direct sampling in an SDR

In a **direct-sampling SDR**, incoming RF is digitized by an **analog-to-digital converter** without first being mixed with a local oscillator.

That is the core definition.

Older receiver architectures often convert RF to an IF using mixers and analog stages before detection. Direct sampling moves the analog-to-digital boundary much closer to the antenna, then lets software or firmware handle the rest.

That gives tremendous flexibility, but it also makes the ADC extremely important.

### Sampling theorem: twice the highest frequency

One of the highest-value facts in this group is the **Nyquist criterion**:

To reproduce a signal accurately, it must be sampled at **at least twice the highest frequency component present**.

That is the minimum theoretical condition. Sampling more than twice the bandwidth is common in real systems, but below twice the highest frequency you get **aliasing**.

### Resolution in bits

If an ADC must cover a range of 1 volt with a resolution of 1 millivolt, you need about 1000 distinguishable levels.

Since:

- 2⁹ = 512
- 2¹⁰ = 1024

you need **10 bits**.

This is a classic exam example because it connects digital resolution directly to practical voltage measurement.

### What sets bandwidth in a direct-sampling receiver

In a direct-sampling SDR, the maximum receive bandwidth is determined by the ADC **sample rate**.

That follows directly from Nyquist. Faster sampling means a wider chunk of spectrum can be represented digitally.

### What sets the minimum detectable signal, absent other noise

In the absence of atmospheric or thermal noise, the minimum detectable signal level is limited by the ADC’s **reference voltage level** and **sample width in bits**.

That is really a quantization issue. The full-scale voltage range and the number of code steps determine how small a signal change can be represented.

So sample rate mainly sets **bandwidth**, while reference level and bit depth mainly set **amplitude resolution/dynamic range**.

### FFT: time domain to frequency domain

A **Fast Fourier Transform** converts a signal from the **time domain** to the **frequency domain**.

This is why SDR software can display panadapters and waterfalls. The receiver samples the waveform over time, and the FFT reveals how much energy is present at each frequency.

That is one of the most powerful conceptual bridges in the whole Extra syllabus: a waveform can be described either as changing over time or as a collection of frequency components.

### Decimation and anti-alias filtering

**Decimation** reduces the effective sample rate by removing samples.

That is useful when the original sample rate is higher than necessary for the bandwidth you actually care about. But decimation introduces a risk: once the sample rate is reduced, the new Nyquist limit is lower.

That is why a **decimator needs an anti-aliasing filter**. High-frequency components that no longer fit inside the new Nyquist range must be removed first, or they will fold back into the passband as false lower-frequency signals.

This is a pure cause-and-effect concept:

- lower sample rate → lower Nyquist limit
- frequencies above new Nyquist limit will alias
- so filter them out first

### Adaptive filters, Hilbert transforms, and I/Q processing

DSP is not just about converting analog to digital. It is about using mathematical operations to perform signal tasks elegantly.

#### Adaptive filter
An **adaptive filter** is used to remove unwanted noise from a received SSB signal. Unlike a fixed filter, it can adjust its characteristics to changing signal conditions.

#### Hilbert-transform filter
A **Hilbert-transform filter** is used in DSP-based SSB generation because it creates the required **90-degree phase shift** relationship across the signal.

#### Quadrature combination
SSB generation in DSP is done by combining signals in **quadrature phase relationship** — the familiar **I and Q** concept.

This is worth seeing as one idea, not three isolated facts:

- Hilbert transform helps create the quadrature relationship
- I/Q paths carry that relationship
- combining them appropriately lets one sideband cancel while the other remains

### FIR filters and taps

A **Finite Impulse Response (FIR)** filter has an important property: it can be designed so that **all frequency components are delayed by the same amount**. That is linear phase.

Linear phase matters because it preserves waveform shape better than filters that delay different frequencies by different amounts.

The term **taps** refers to the incremental signal delays used in the filter algorithm. Each tap contributes another weighted delayed sample to the output.

More taps generally allow a **sharper filter response**. The tradeoff is more computation and more delay.

That tradeoff is classic engineering:

- more taps → better selectivity and stopband performance
- more taps → more processing cost and latency

### The practical viewpoint for E7F

E7F is much easier if you connect every fact to one of four questions:

- How is the signal digitized?
- How fast must it be sampled?
- How precisely must it be quantized?
- What digital math is being used afterward?

The must-remember items are:

- direct sampling = RF straight to ADC
- sample at least twice the highest frequency
- sample rate sets bandwidth
- reference voltage plus bit depth set quantization limits
- FFT = time to frequency domain
- decimation lowers sample rate
- anti-alias filter protects against foldover
- FIR can provide linear phase
- taps are delay elements; more taps sharpen the response

---

## Group E7G — Active filters and operational amplifiers

Op-amps are among the most useful analog building blocks because they let external components determine circuit behavior.

The pool focuses on basic op-amp properties, inverting-amplifier calculations, frequency response with feedback components, and stability considerations in active filters.

### What an op-amp is

An **operational amplifier** is a **high-gain, direct-coupled differential amplifier** with:

- **very high input impedance**
- **very low output impedance**

Those two impedance characteristics are why op-amps are so useful:

- high input impedance means they do not load the source much
- low output impedance means they can drive following stages effectively

### Input offset voltage

A real op-amp is not perfectly symmetrical internally. Because of that, a tiny differential input voltage may be required to force the output to zero.

That small required input voltage is the **input offset voltage**.

The exam wording to know is:

- it is the **differential input voltage needed to bring the open-loop output voltage to zero**

This is not the same thing as overall gain error or output swing limit. It is a small inherent imbalance parameter.

### Gain-bandwidth product

The **gain-bandwidth product** is the frequency at which the op-amp’s **open-loop gain falls to one**.

The practical meaning is that gain and bandwidth trade against one another. If you configure the op-amp for more closed-loop gain, the usable bandwidth decreases.

That matters especially in active filters. A circuit that asks too much gain at too high a frequency may become unstable or simply fail to perform as designed.

### Inverting amplifier behavior

The figure in E7G is the standard **inverting op-amp** configuration.

Its gain is set by the resistor ratio:

**Voltage gain = −R_F / R_1**

The minus sign indicates inversion.

For example:

- R1 = 10 Ω, RF = 470 Ω → gain = −47
- R1 = 1000 Ω, RF = 10,000 Ω → gain = −10
- 0.23 V input with gain −10 gives **−2.3 V output**

A lot of E7G is really just checking whether you know this formula and remember the sign convention.

If the question asks for **absolute** voltage gain, ignore the sign and use the magnitude only.

### Adding a capacitor across the feedback resistor

If a capacitor is placed across the feedback resistor in the inverting amplifier, the circuit becomes a **low-pass filter**.

Why?

At low frequency, the capacitor has high reactance and barely affects the feedback network.
At higher frequency, its reactance falls, changing the effective feedback impedance and reducing gain.

So the stage passes low frequencies more strongly than high frequencies.

### Preventing ringing and instability in active filters

Unwanted ringing and audio instability in an op-amp filter are reduced by restricting both **gain** and **Q**.

That makes sense physically:

- very high Q creates strong resonance and ringing
- high gain gives the circuit more opportunity to reinforce that ringing or oscillate

The exam is testing your sense of stability, not your willingness to maximize every parameter at once.

### Ideal vs. real op-amp behavior

The pool includes one “ideal op-amp” question. In the ideal model, the gain **does not vary with frequency**. Real op-amps do, of course, but the ideal model is a simplified abstraction used for analysis.

This is one of those questions where the test wants you to distinguish the ideal model from real hardware behavior.

### The practical viewpoint for E7G

If you keep just a few relationships clear, this whole group simplifies dramatically:

- op-amp input impedance is very high
- op-amp output impedance is very low
- inverting gain = −RF/R1
- capacitor across feedback resistor creates low-pass action
- gain-bandwidth product sets the speed/gain tradeoff
- too much gain and too much Q invite instability

---

## Group E7H — Oscillators, PLLs, and signal sources

A radio cannot translate, modulate, or receive signals without stable frequency sources.

This group covers classic oscillator types, methods of stabilization, phase-locked loops, direct digital synthesis, and high-accuracy references used at microwave frequencies.

### Three classic oscillators

The three common oscillator circuits you need to know are:

- **Colpitts**
- **Hartley**
- **Pierce**

These are not just names to memorize. Each one identifies the feedback method used around the resonant element.

### Colpitts: capacitive divider feedback

In a **Colpitts oscillator**, positive feedback is supplied through a **capacitive divider**.

That is the key identifier. If the question says Colpitts, think **capacitors**.

### Hartley: inductive divider feedback

A **Hartley oscillator** uses an inductive divider or tapped coil for feedback.

The pool does not hammer Hartley details the way it does Colpitts and Pierce, but you should still keep the contrast straight:

- Colpitts → capacitive divider
- Hartley → inductive divider

### Pierce: crystal feedback path

A **Pierce oscillator** provides positive feedback through a **quartz crystal**.

This is why Pierce oscillators are so common where frequency stability matters. The crystal, not a free-running LC tank, is the frequency-determining element.

### Microphonics and vibration sensitivity

An oscillator is called **microphonic** when its frequency changes due to **mechanical vibration**.

This happens because vibration can slightly change the values or geometry of frequency-determining components. If that occurs in a transmitter oscillator, the vibration becomes unwanted frequency modulation.

The cure is straightforward in principle: **mechanically isolate the oscillator circuitry from its enclosure**.

That is a practical reminder that frequency stability is not only about electrical design. Mechanical design matters too.

### Thermal drift and NP0 capacitors

Thermal drift in crystal oscillators can be reduced by using **NP0** capacitors.

NP0, also called C0G, means the capacitance changes very little with temperature. That makes these capacitors ideal in oscillator and tuned-circuit applications where even a small capacitance change would shift frequency.

### Crystal load capacitance

A crystal oscillator must present the crystal with the **specified parallel capacitance** the crystal manufacturer expects.

If the load capacitance is wrong, the oscillator will not run at the exact marked frequency.

That is a very practical lab fact. Crystal frequency is not just a number printed on the can; it depends on the intended circuit loading.

### Phase-locked loops

A **phase-locked loop (PLL)** is an electronic servo loop made from:

- a **phase detector**
- a **low-pass filter**
- a **voltage-controlled oscillator**

The phase detector compares the VCO output, usually after division, against a reference. The resulting error signal steers the VCO until the phases line up in the required relationship.

This is one of the most important control ideas in modern radio.

A PLL can be used for:

- **frequency synthesis**
- **FM demodulation**

For synthesis, dividers in the loop let the output frequency be an exact multiple or fraction of a stable reference. For FM detection, the control voltage that keeps the loop locked tracks the incoming frequency deviation.

### Direct digital synthesis

A **direct digital synthesizer (DDS)** uses:

- a **phase accumulator**
- a **lookup table**
- a **digital-to-analog converter**
- a **low-pass anti-alias filter**

The lookup table contains **amplitude values representing the desired waveform**, usually a sine wave.

The phase accumulator advances by a set amount each clock cycle. That selects successive waveform samples from the lookup table. The DAC converts those digital values to analog voltage, and the output filter smooths away sampling artifacts.

The big advantages of DDS are:

- very fine tuning resolution
- rapid frequency changes
- good repeatability

The main spectral impurity to remember is **discrete spurious signals**, or **spurs**, not just generic broadband noise.

### Highly stable microwave references

At microwave frequencies, very accurate and stable oscillators may use:

- **GPS-based references**
- **rubidium-stabilized references**
- **temperature-controlled high-Q dielectric resonators**

The exam answer is that **all of these** are valid techniques.

The broader lesson is that the higher the frequency and the tighter the system requirements, the more seriously the reference source matters.

### The practical viewpoint for E7H

This group becomes much easier if you connect each source type to its stabilizing mechanism:

- Colpitts → capacitive divider
- Hartley → inductive divider
- Pierce → crystal
- PLL → control loop with phase detector, filter, VCO
- DDS → digital phase accumulation and lookup table
- crystal accuracy → correct load capacitance
- oscillator drift → vibration and temperature matter

---

## Putting the whole subelement together

E7 looks broad because it spans digital logic, analog amplification, filtering, power conversion, modulation, DSP, op-amps, and oscillators. But all of it fits one unified picture of a working radio.

### 1. Logic provides control and timing

Flip-flops, counters, and multivibrators create timing, storage, and division functions. These are the control skeleton of digital radio systems.

### 2. Amplifiers trade linearity against efficiency

Class A, AB, C, and D are all answers to the same design question: how much distortion can the application tolerate, and how much heat can you afford?

### 3. Filters and matching networks shape what gets through

Pi networks, T networks, cavity filters, crystal filters, and DSP filters are all trying to pass what you want and reject what you do not.

### 4. Power supplies make the rest of the radio usable

Raw DC is not enough. It has to be regulated, filtered, and delivered safely. Linear and switching regulators simply solve that problem in different ways.

### 5. Modulators, detectors, and mixers move information around

Baseband becomes RF, RF becomes IF, IF becomes audio again. Balanced modulators, discriminators, product detectors, and mixers are the translation machinery.

### 6. DSP replaces hardware with math

Sampling, FFTs, decimation, FIR filters, Hilbert transforms, and I/Q processing let a modern radio do in software what once required racks of analog circuitry.

### 7. Oscillators and synthesizers provide the frequency reference for everything else

Without stable sources, nothing else works properly. Oscillator design, PLLs, DDS systems, and reference stability are the time-and-frequency backbone of the station.

Seen that way, E7 is not a random collection of practical facts. It is a block diagram of radio design.

---

## Final Summary

E7 is the Extra-class subelement about **how real radio circuits are put together and why those circuit choices matter**.

You should come away knowing that:

- a flip-flop is bistable and divides frequency by 2
- monostable, astable, and bistable circuits are distinguished by how many stable states they have
- amplifier classes are defined mainly by conduction angle and linearity/efficiency tradeoffs
- Class AB is the common linear compromise, while Class C is unsuitable for SSB
- switching amplifiers and switching regulators are efficient because their devices spend most of the time fully on or fully off
- matching networks cancel reactance and transform resistance
- Chebyshev and elliptical filters trade ripple for sharper cutoff
- a linear regulator controls output by varying conduction, while a switcher controls duty cycle
- SSB uses balanced modulation plus filtering and requires a product detector for reception
- direct-sampling SDRs depend heavily on ADC sample rate and resolution
- FIR filters use taps and can provide linear phase response
- op-amp circuits are governed by high input impedance, low output impedance, feedback ratio, and gain-bandwidth limits
- oscillator stability depends on the feedback method, the reference element, and control of temperature and vibration

If you want a compact review list for the exam, focus especially on these:

- flip-flop / monostable / astable
- Class A / AB / C / D
- Pi / T / Pi-L network behavior
- linear vs. switching regulator
- envelope detector / discriminator / product detector
- Nyquist sampling rule and FFT
- inverting op-amp gain formula
- Colpitts / Pierce / PLL / DDS identification

That covers a large share of the E7 pool and, more importantly, gives you a usable mental model of the signal chain inside real amateur equipment.

---

*Extra-class exam: 50 questions, must pass with 37 or higher (74%). E7 contributes 8 questions.*
