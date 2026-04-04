# E4 — Amateur Practices

E4 is where the Extra exam asks whether you can do more than operate a radio — whether you can **measure**, **evaluate**, and **improve** a station like an experienced amateur.

This subelement is really about station literacy. It covers the tools you use to inspect signals, the measurement habits that keep you from fooling yourself, the receiver characteristics that separate a pleasant radio from a frustrating one, and the interference-control techniques that make a station usable in the real world.

The question pool is organized into five groups:

- **E4A:** test equipment and basic instrument use
- **E4B:** measurement technique, accuracy, and vector network analyzers
- **E4C:** receiver performance characteristics
- **E4D:** dynamic range, intermodulation, and link-budget thinking
- **E4E:** noise suppression, interference, and grounding practice

The exam pulls **5 questions from a pool of 63**.

The easiest way to study E4 is not as a list of instrument names. Think instead in terms of a few recurring ideas:

- every instrument has limits
- every measurement changes the circuit a little
- every receiver is a compromise between sensitivity, selectivity, and strong-signal handling
- every interference problem has a path, and the fix is to interrupt that path

If you build that mindset, the E4 questions stop feeling random.

---

## Group E4A — Test equipment and what each instrument is really showing you

E4A is about basic lab awareness. The exam is not trying to turn you into an RF metrology specialist. It wants you to recognize **which instrument answers which question**, and where that instrument can mislead you.

### Digital oscilloscopes: sampling rate matters

A digital oscilloscope does not look at a waveform continuously the way an ideal analog scope would. It samples the signal, converts those samples to numbers, and then reconstructs a display from them.

That means the highest frequency you can display accurately is limited by the **sampling rate of the analog-to-digital converter**.

This is the core concept behind two E4A ideas at once:

- the ADC sampling rate limits what the scope can display correctly
- if the sampling rate is too low, you can get **aliasing**

**Aliasing** is when a higher-frequency signal is displayed as a false lower-frequency waveform. On the screen it often looks like a jittery or unstable low-frequency signal that is not really present at all.

The practical lesson is simple: if a digital scope display looks weird, do not immediately assume the circuit is weird. Sometimes the scope is under-sampling the signal.

### Spectrum analyzer: amplitude versus frequency

An oscilloscope answers the question, **“How does voltage change with time?”**

A **spectrum analyzer** answers a different question: **“How much signal is present at each frequency?”**

So on a spectrum analyzer:

- the **horizontal axis** is **frequency**
- the **vertical axis** is **signal amplitude**

That makes it the right tool for looking at:

- harmonics
- spurious outputs
- intermodulation products
- unwanted mixing products near a desired signal

This is why it is the correct instrument for checking an SSB transmitter for **spurious signals** or **intermodulation distortion products**. If you want to see energy where it should not be in the frequency domain, use a spectrum analyzer.

### Oscilloscope probe compensation and probe habits

A scope probe is not just a wire. It is part of the measurement system, and if it is adjusted badly, the display lies.

To **compensate** a typical oscilloscope probe, you display a **square wave** and adjust the probe until the flat parts of the waveform are truly flat. That is the key idea: a correctly compensated probe reproduces the square wave without rounded corners from under-compensation or overshoot from over-compensation.

Another good habit from the pool is to **keep the ground lead short**. A long probe ground clip adds inductance, and at RF or with fast edges that inductance can distort the measurement badly.

The practical rule:

- short ground lead = cleaner, more honest measurement
- long dangling ground lead = extra inductance, ringing, and confusion

### Scope trigger choice: why “line” trigger is useful for ripple

If you want to look at **power-supply ripple** in a linear supply, the most effective trigger mode is **line trigger**.

That makes sense because ripple is tied to the AC mains frequency. Using line trigger helps stabilize the display relative to the source of the ripple itself.

This is a good example of E4 thinking: choose the trigger source that matches the phenomenon you are studying.

### Frequency counters and prescalers

A frequency counter counts cycles over a precise time window. But every counter has an upper operating frequency range.

A **prescaler** is used to divide a very high input frequency down to something the counter can handle. Its purpose is to **reduce the input signal frequency to within the counter’s operating range**.

So a prescaler is not there to amplify the signal or make the counter more stable. It is there to let the counter measure frequencies that would otherwise be too high.

### Antenna analyzers, SWR bridges, and what “better” means

An SWR bridge or directional wattmeter can measure standing-wave behavior. But an **antenna analyzer** is more informative because it can automatically compute **SWR and impedance**, and many models can also estimate things like:

- resonant frequency
- cable length
- velocity factor

The deeper idea is that an analyzer does more than tell you **“good match”** or **“bad match.”** It helps tell you **why**.

For example:

- an SWR meter may show a mismatch
- an antenna analyzer may show whether the load looks resistive, inductive, or capacitive
- that extra information helps you decide whether to shorten the antenna, lengthen it, retune a network, or inspect the feed line

### More than one instrument can measure SWR

The pool also makes the point that SWR is not tied to one magical tool. You can measure it with a:

- **directional wattmeter**
- **vector network analyzer**
- **antenna analyzer**

That is worth remembering because E4 often tests concepts by making sure you are not overly attached to one piece of equipment. Different instruments may get to the same answer in different ways.

---

## Group E4B — Measurement technique, accuracy, and vector network analyzer basics

E4B is about what makes a measurement trustworthy.

Two operators can measure the same circuit and get different answers. Often the difference is not intelligence. It is **instrument loading, calibration, reference accuracy, or using the wrong method**.

### Frequency counter accuracy comes from the time base

A frequency counter works by counting cycles during a known time interval. So the measurement is only as accurate as the **time base** that defines that interval.

That means the factor that most affects frequency-counter accuracy is the **accuracy of the counter’s time base**, not the logic temperature coefficient or attenuator accuracy.

The practical meaning is straightforward:

- a stable, accurate reference clock gives accurate readings
- a drifting or inaccurate reference clock gives confident-looking but wrong readings

### Voltmeter sensitivity and circuit loading

Older analog voltmeters are often rated in **ohms per volt**. This tells you the input resistance the meter presents on a given range.

The rule is:

**meter input resistance = full-scale voltage × ohms-per-volt rating**

So if a meter is rated at 20,000 ohms per volt and you are on the 10 V range, the meter input resistance on that range is 200,000 ohms.

Why do you care? Because the meter is part of the circuit once you connect it. A low-input-resistance meter can **load** the circuit and pull the voltage away from its true unloaded value.

This is classic E4 thinking: measuring a circuit can change the circuit.

### Vector network analyzers and S-parameters

A **vector network analyzer (VNA)** is one of the most useful RF measurement tools because it can describe how a device behaves at its ports across frequency.

The exam only needs you to know the basics, but those basics matter.

#### What the subscripts mean

The subscripts in an **S-parameter** identify the port or ports involved in the measurement.

For a two-port device:

- the first number tells you where the signal is observed
- the second number tells you where the signal was applied

So:

- **S11** = reflection seen at port 1 when exciting port 1
- **S21** = forward transmission from port 1 to port 2

#### The important ones to memorize

For the Extra pool, the two most important S-parameters are:

- **S11** = input reflection coefficient / return loss / VSWR-related behavior
- **S21** = forward gain or forward transmission

That means:

- if you are asking how much of the signal gets reflected back at the input, think **S11**
- if you are asking how much gets through in the forward direction, think **S21**

#### Calibration loads

A VNA must be calibrated against known standards. The classic calibration set in the pool is:

- **short circuit**
- **open circuit**
- **50-ohm load**

This is the familiar **open-short-load** idea. Calibration teaches the instrument what the known reference conditions look like so it can measure the unknown device accurately.

#### What a VNA can measure

A VNA can be used to measure things such as:

- input impedance
- output impedance
- reflection coefficient
- filter frequency response

That is why it is such a powerful all-around RF tool. A scalar SWR meter gives you one narrow slice of information. A VNA gives you a much fuller picture.

### Using bandwidth to determine Q

For a tuned circuit, one way to determine **Q** is from the **bandwidth of the frequency response**.

The essential relationship is:

**Q = resonant frequency / bandwidth**

So:

- high Q means narrow bandwidth and sharper selectivity
- low Q means wider bandwidth and broader response

This connects E4 directly to E5. E4 asks how you would **measure** Q; E5 asks you to understand what Q means physically.

### Forward and reflected power: what the load actually absorbs

If a directional power meter reads:

- 100 W forward
- 25 W reflected

then the load is absorbing **75 W**.

The simple exam relationship is:

**absorbed power = forward power − reflected power**

That does not mean the transmitter “creates” 125 W. It means 100 W is moving toward the load, 25 W is coming back, and the net power delivered to the load is 75 W.

### Two-tone testing for SSB intermodulation

To measure intermodulation distortion in an SSB transmitter, the standard lab method is the **two-tone test**.

The pool wants a specific version of that method:

- use **two AF tones**
- make them **non-harmonically related**
- observe the resulting RF output products

Why AF tones? Because in an SSB transmitter, speech is normally introduced as audio. Two clean audio tones produce predictable RF products, making it easier to evaluate linearity.

Why non-harmonically related? Because harmonically related tones can hide or confuse the distortion products you are trying to inspect.

The practical lesson: a good SSB transmitter should reproduce the wanted two-tone envelope cleanly without generating a forest of extra products nearby.

---

## Group E4C — Receiver performance: noise, selectivity, overload, and why some radios sound better than others

E4C is where the exam starts asking, “What makes one receiver pleasant and another one exhausting?”

A receiver is not just sensitive or insensitive. It also has to survive strong nearby signals, reject images, choose appropriate bandwidth, and keep internally generated noise under control.

### Phase noise and reciprocal mixing

A local oscillator or master clock is never perfectly pure. Real oscillators have **phase noise** — a fuzziness around the ideal carrier.

In a receiver, especially an SDR, excessive phase noise can combine with a strong nearby signal and create interference in the desired channel. This effect shows up in the pool two ways:

- excessive phase noise in an SDR master clock can cause nearby strong signals to produce interference
- **reciprocal mixing** is when local oscillator phase noise mixes with a strong adjacent signal and raises the apparent noise in the desired receive channel

This is not ordinary “another station is too close” interference. It is the receiver’s own oscillator impurity helping create the problem.

The practical meaning: even if the desired signal is on frequency, a noisy oscillator can let a nearby strong signal smear into your passband.

### Front-end filters and preselectors

One of the best defenses against strong out-of-band signals is a **front-end filter** or **preselector**.

Its job is to reject signals outside the band of interest before they reach the sensitive early stages of the receiver.

That matters because once a very strong unwanted signal gets into the front end, it can:

- overload active devices
- create mixing products
- reduce gain for the desired signal
- raise the effective noise floor

So the preselector does not store favorite frequencies or magically increase gain. Its purpose is to **improve rejection of signals outside the band being received**.

### Capture effect in FM

In FM reception, if two signals are present on the same frequency, the stronger one often dominates and suppresses the weaker one. That behavior is called the **capture effect**.

This is a specifically FM idea. It explains why one repeater user can “capture” an FM receiver while a weaker station on the same frequency may disappear entirely.

### Noise figure, thermal noise, and the meaning of -174 dBm

A receiver always adds some noise of its own. **Noise figure** tells you how much worse the real receiver is than an ideal noiseless receiver.

Formally, it is the ratio, in dB, of the noise generated by the receiver to the theoretical minimum noise.

A related number that Extra operators should recognize cold is **-174 dBm**. This represents the theoretical thermal noise power in a **1 Hz bandwidth** at the input of a perfect receiver at room temperature.

That number is the starting point for a huge amount of receiver thinking.

If bandwidth increases, noise power increases too. The pool’s example is a good one:

- increase bandwidth from 50 Hz to 1000 Hz
- that is a 20:1 increase in bandwidth
- noise rise = **10 log10(20) ≈ 13 dB**

So a wider filter lets in more signal, but it also lets in more noise.

That is why receiver bandwidth choice matters so much.

### Minimum discernible signal and bandwidth choice

The **MDS** of a receiver is the **minimum discernible signal** — the smallest signal that can be detected usefully.

A receiver with selectable bandwidths has a real advantage because you can choose a bandwidth that more closely matches the signal you are trying to copy.

That improves **signal-to-noise ratio**:

- too wide a filter lets in unnecessary noise
- too narrow a filter may distort the wanted signal
- the best choice is the bandwidth that fits the mode

This is why different bandwidth settings are so useful for CW, SSB, AM, digital modes, and weak-signal work.

### SDR overload and ADC limits

In an SDR, the analog-to-digital converter has a finite input range. If signals exceed the **reference voltage of the ADC**, the receiver overloads.

That is the important E4C idea. Overload in an SDR is not defined by half the sample rate or buffer size. It happens when the analog signal exceeds what the ADC can convert properly.

### High IF and image rejection

One reason to choose a **high intermediate frequency** in a superheterodyne receiver is that it makes **image rejection** easier.

The image frequency is farther away from the desired frequency when the IF is higher, and that greater spacing makes it easier for the front-end tuned circuits to reject the image.

So the benefit is not fewer parts or better noise figure by magic. The key advantage is easier image suppression.

### Attenuation can help on the low HF bands

A very practical E4C concept is that on the lower HF bands, especially where atmospheric noise is already high, adding some **input attenuation** can reduce overload with little or no real penalty in signal-to-noise ratio.

Why? Because on those bands the external noise from nature is often greater than the receiver’s own internal noise even after some attenuation.

In plain language:

- the band is already noisy
- a few dB of attenuation hurts everything equally
- but it can greatly improve strong-signal handling
- so the radio may actually copy weak stations better in a crowded environment

### Roofing filters and IF shift

A **roofing filter** is an early, relatively narrow filter in the IF chain. Its purpose is to reduce the energy from strong nearby signals before later stages can be overloaded.

That improves **blocking dynamic range**.

The **IF Shift** control, by contrast, moves the receive passband relative to the tuned signal so you can reduce adjacent-channel interference without moving the transmit frequency.

That is a subtle but useful distinction:

- roofing filter = improve strong-signal handling in the receiver chain
- IF Shift = reposition the passband to avoid interference nearby

---

## Group E4D — Dynamic range, intermodulation, desensitization, and link budgets

E4D is where the exam asks whether you understand what happens when radios are used in the real RF world, not an empty one.

Weak-signal performance is nice. But if the receiver collapses in the presence of strong nearby signals, the station is still poor.

### Blocking dynamic range

The **blocking dynamic range** of a receiver is the difference, in dB, between the noise floor and the level of an incoming signal that causes **1 dB of gain compression**.

The practical meaning is:

- how much strong-signal stress the receiver can tolerate
- before the desired signal path starts being measurably suppressed

Poor dynamic range causes problems like:

- cross modulation
- desensitization
- spurious responses from strong adjacent signals

This is one of the most important receiver-quality ideas in the whole Extra pool.

### Desensitization

**Desensitization** is the reduction in receiver sensitivity caused by a strong nearby signal.

The desired station may not disappear because it is weak in absolute terms. It disappears because the front end is being pushed around by something else.

One way to reduce the likelihood of desensitization is to **insert attenuation before the first RF stage**. That sounds backward at first — why weaken the signal on purpose? But when overload is the limiting problem, a little attenuation can keep the front end in its linear operating range.

Again, E4 rewards practical thinking over instinct.

### Intermodulation: nonlinear devices create new frequencies

**Intermodulation distortion** occurs in **nonlinear circuits or devices**. When two or more signals pass through a nonlinear stage, new sum-and-difference products are created.

This matters especially at repeater sites and multi-transmitter locations.

For example, if two repeaters are in close proximity, intermodulation can be created because the output signals **mix in the final amplifier of one or both transmitters**.

The important thing to remember is that intermod is not caused by negative feedback or lack of neutralization by itself. The root cause is **nonlinearity**.

### Why odd-order products matter most

Odd-order intermodulation products are especially troublesome because, when the original signals are near the band of interest, the odd-order products are also likely to land **inside that same band**.

That is why third-order products get so much attention.

For two signals at frequencies f1 and f2, the troublesome third-order products appear at:

- **2f1 − f2**
- **2f2 − f1**

Those often land annoyingly close to the original signals, which makes them hard to filter away.

### Third-order intercept point

The **third-order intercept point** is a figure of merit used to describe how a receiver or amplifier handles intermodulation.

When the exam says a receiver has a third-order intercept level of **40 dBm**, it means that if you extrapolate the signal and third-order product lines, a pair of **40 dBm input signals** would theoretically produce a third-order product of equal strength.

That intercept is theoretical, but it is useful because a higher intercept point generally indicates better resistance to intermodulation problems.

### Circulators and repeater-site cleanup

At repeater sites, one way to reduce intermodulation trouble caused by a nearby transmitter is to use a **properly terminated circulator** at the output of the repeater transmitter.

A circulator helps isolate the transmitter from reflections and unwanted interactions, reducing the chance that strong RF energy will be reintroduced into nonlinear paths that create products.

### Link budgets: adding gains and subtracting losses

E4D also includes practical system calculations.

A **link budget** is just disciplined bookkeeping in dB:

- start with transmitter power in dBm
- add antenna gains
- subtract feed-line losses
- subtract path loss
- compare the received signal to what the receiver requires

That sounds abstract until you do it.

#### Received signal level example

If you have:

- transmit power = **+40 dBm** (10 W)
- transmit antenna gain = **+6 dBi**
- receive antenna gain = **+3 dBi**
- path loss = **100 dB**

then received signal level is:

**+40 + 6 + 3 − 100 = -51 dBm**

That is the direct E4D13 idea.

#### Link margin example

If you have:

- transmit power = **+40 dBm**
- antenna gain = **+10 dBi**
- cable loss = **3 dB**
- path loss = **136 dB**
- receiver MDS = **-103 dBm**
- required SNR = **6 dB**

then:

1. Effective transmitted level = **+40 + 10 − 3 = +47 dBm**
2. Received signal = **+47 − 136 = -89 dBm**
3. Required signal level = **-103 + 6 = -97 dBm**
4. Link margin = **-89 − (-97) = +8 dB**

A positive margin means the link should work, at least on paper.

### dBm and tiny signals

The pool also expects you to recognize just how small receiver signals can be.

An MDS of **-100 dBm** corresponds to **0.1 picowatts**.

That is a useful calibration point for your intuition. Amateur receivers routinely work with astonishingly small signals, which is why shielding, filtering, oscillator purity, and dynamic range matter so much.

---

## Group E4E — Noise suppression, interference hunting, and station grounding practice

E4E is the troubleshooting section of the subelement.

The exam is asking whether you recognize common noise signatures and whether you know which tool or practice is appropriate for each one.

### DSP tools: useful, but not magic

Modern receivers often provide DSP features such as:

- **digital noise reduction (DNR)**
- **automatic notch filter (ANF)**
- **noise blanker (NB)**

Each does a different job.

#### Digital noise reduction

Digital noise reduction can often help with a wide range of noise types, including:

- broadband white noise
- ignition noise
- power-line noise

The exam frames this broadly because the important idea is that DSP noise reduction can improve readability across multiple noise types, not just one special category.

#### Noise blanker

A **noise blanker** is primarily for **impulse noise** — short, sharp bursts such as ignition noise or certain switching transients.

But it is not free. One undesirable effect is that **strong signals may be distorted** and may even sound as if spurious products are being created.

So the operating habit is:

- use the blanker when impulsive noise is the real problem
- do not leave it cranked up blindly on every signal

#### Automatic notch filter

An **automatic notch filter** is intended to remove steady interfering tones or carriers. That sounds perfect for CW until you realize the trap: a CW signal is itself basically a tone.

So if you use ANF aggressively while receiving CW, it may remove **the desired CW signal along with the interfering carrier**.

That is a very E4-style lesson: the tool can be correct in principle and still wrong for the specific signal you are copying.

### Suppressing conducted and line-borne interference

Some interference rides in on power or control leads rather than arriving through the antenna.

For conducted noise from an automobile charging system, a standard cure is to install **ferrite chokes on the charging-system leads**.

For RFI from a line-driven AC motor, a common fix is a **brute-force AC-line filter** in series with the motor’s power leads.

These are practical, path-based solutions:

- if the noise is traveling along the wire, choke or filter the wire
- if the noise is being radiated, improve bonding, shielding, or distance

### Recognizing common interference signatures

E4E includes several classic “what does this noise source sound or look like?” questions.

#### Network equipment

Computer network equipment often creates **unstable modulated or unmodulated signals at specific frequencies**.

In practice these often appear as birdies or carriers that come and go or wander slightly, rather than sounding like smooth hum.

#### Switch-mode power supplies

A **switch-mode power supply** often produces a **series of carriers at regular intervals** across a wide frequency range.

That regular spacing is the clue. The supply switches at some fundamental frequency and throws off harmonics, making a comb-like pattern across the spectrum.

#### AC line roaring and buzzing

Intermittent roaring or buzzing AC line interference can be caused by things such as:

- arcing contacts in thermostatic devices
- defective doorbells or transformers
- malfunctioning illuminated signs or displays

The pool groups these together because they are all common real-world sources of line noise.

#### Broadcast mixing on rusty metal

If local AM broadcast signals seem to be combining and producing spurious signals on MF or HF, one likely cause is **nearby corroded metal connections** acting like nonlinear mixers and reradiating the results.

That is a deeply practical amateur-radio observation. Rusty hardware, loose joints, and corroded metal fences can become accidental detectors and mixers.

### Common-mode current and why shields sometimes fail

Shielding is not perfect just because a cable has braid around it.

A shielded cable can radiate or receive interference when **common-mode current** flows on the shield and conductors.

In an unshielded multiconductor cable, current that flows equally on all conductors is also called **common-mode current**.

This matters because common-mode current does not stay neatly confined the way differential current ideally does. It turns the entire cable into part of the antenna system.

That is why ferrites, chokes, and good grounding practices are so often aimed at common-mode current rather than the wanted signal path itself.

### Single-point grounding and surge protection

The station AC surge protector should be installed on the **single-point ground panel**.

The purpose of the single-point ground panel is to ensure that **all lightning protectors operate against the same reference at the same time**.

That is the heart of the concept.

You do not want different pieces of equipment clamped to wildly different potentials during a surge. You want everything bonded to one common point so voltage differences inside the station are minimized.

This is why the single-point ground idea matters so much in station protection:

- one reference point
- one bonding system
- coordinated protector action
- less chance of destructive voltage differences between equipment

---

## Putting the whole subelement together

E4 looks broad, but almost everything in it fits into one of four habits.

### 1. Know what your instrument is really measuring

- oscilloscope = voltage versus time
- spectrum analyzer = amplitude versus frequency
- antenna analyzer/VNA = impedance and reflection behavior versus frequency
- frequency counter = cycle count based on a reference time base

If you use the wrong instrument, or interpret the right one the wrong way, the measurement will mislead you.

### 2. Respect instrument limits and calibration

- digital scopes can alias
- probes need compensation
- long probe grounds distort fast measurements
- counters depend on time-base accuracy
- VNAs depend on proper calibration

E4 repeatedly rewards operators who distrust easy-looking readings until they understand how the instrument got them.

### 3. Receiver quality is more than sensitivity

A good receiver also needs:

- low internal noise
- good image rejection
- appropriate bandwidth choices
- strong dynamic range
- resistance to desensitization and intermodulation
- clean oscillator performance with low phase noise

That is why one radio may hear weak signals beautifully in a quiet band yet struggle badly in a contest or near a strong local station.

### 4. Noise and interference are solved by finding the path

- impulse noise → noise blanker
- conducted noise on leads → ferrites and filters
- out-of-band overload → preselector or front-end filtering
- common-mode current → choking and better bonding
- surge protection → single-point ground system

The fix works when it attacks the **actual mechanism**, not just the symptom.

---

## Final Summary

E4 is the Extra subelement about station competence.

You should come away understanding that:

- digital scopes are limited by sampling rate and can alias
- spectrum analyzers show amplitude versus frequency and are ideal for spotting spurs and distortion products
- probes, counters, meters, and VNAs all have specific accuracy and calibration concerns
- receiver performance includes noise figure, MDS, bandwidth choice, image rejection, phase noise, and overload behavior
- dynamic range, desensitization, and third-order intermodulation determine how well a receiver survives strong-signal environments
- link budgets are just disciplined dB arithmetic
- interference control depends on recognizing noise signatures and interrupting the correct path
- common-mode current and poor grounding can turn cables and equipment into unintended antennas
- single-point grounding coordinates surge protection and station bonding

If E4 feels like a pile of lab trivia, step back. It is really teaching one big lesson: **a good amateur operator does not just transmit and listen — they measure intelligently, interpret correctly, and troubleshoot systematically.**

---

*Extra-class exam: 50 questions, must pass with 37 or higher (74%). E4 contributes 5 questions.*
