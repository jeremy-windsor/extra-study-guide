# E8 — Signals and Emissions

E8 is where the Extra exam asks you to think like a signal engineer instead of just an operator.

At a practical level, every transmitter does four jobs:

1. **create a waveform**
2. **put information onto it**
3. **fit that information into a limited bandwidth**
4. **keep the transmitted signal clean enough not to bother everyone else**

That is exactly what this subelement is about.

Some of the questions are about signal representation: time domain vs. frequency domain, Fourier analysis, RMS measurements, and the difference between peak and average power. Others are about modulation methods such as FM, PM, OFDM, QAM, and spread spectrum. The rest are about the practical limits that matter on the air: occupied bandwidth, key clicks, intermodulation, and how digital systems detect or recover from errors.

The pool has **48 questions**, and the exam pulls **4** from E8.

The groups are:

- **E8A:** waveform analysis, ADC/DAC concepts, RMS measurements, and PEP vs. average power
- **E8B:** FM and PM modulation index, deviation ratio, OFDM, FDM, and TDM
- **E8C:** digital signaling, symbol rate, bandwidth, coding, ARQ, and mesh networking
- **E8D:** spread spectrum, keying defects, AFSK/PSK signal quality, and digital-code details

The easiest way to organize E8 is to keep asking four questions:

1. **What does this signal look like in time?**
2. **What does it look like in frequency?**
3. **How efficiently does it carry information?**
4. **What makes it wider or dirtier than it should be?**

If you keep those four questions in mind, the whole subelement starts to connect.

---

## Group E8A — Waveforms, measurement, and conversion between analog and digital

This group ties together three related ideas:

- how we describe a signal
- how we measure it correctly
- how modern radios convert it between analog and digital form

### Time domain vs. frequency domain

A signal can be described in more than one useful way.

In the **time domain**, you look at **amplitude at different times**. This is the oscilloscope view: voltage on the vertical axis, time on the horizontal axis. If you want to see:

- pulse width
- rise and fall time
- envelope shape
- clipping
- timing relationships

then you want the time-domain view.

In the **frequency domain**, you look at how much signal energy exists at different frequencies. This is the spectrum-analyzer view. If you want to see:

- harmonics
- sidebands
- occupied bandwidth
- spurious products
- unwanted emissions

then the frequency-domain view is the right tool.

A lot of E8 becomes easier once you stop thinking of those as competing descriptions. They are just two ways of looking at the same signal.

### Fourier analysis: why square waves are full of harmonics

One of the foundational ideas in E8 is that a complex waveform can be broken into simpler sine waves.

That is what **Fourier analysis** does.

A perfect square wave is not a single frequency. It is made from:

- the **fundamental** frequency
- plus **odd harmonics**
- with amplitudes that decrease as the harmonic number increases

So a square wave contains the fundamental, 3rd harmonic, 5th harmonic, 7th harmonic, and so on.

That matters because it explains something every operator eventually sees in practice: **the sharper and less sinusoidal a waveform is, the more spectral content it has away from the fundamental**.

This is why abrupt switching, clipped audio, and fast keying edges tend to create wider signals. The time-domain sharpness shows up as frequency-domain spread.

### RMS measurements and why true-RMS meters matter

E8 also reminds you that not every AC waveform is a perfect sine wave.

A conventional average-responding meter often assumes the waveform is sinusoidal and then applies a correction factor. That works well enough for clean sine waves. It does **not** work well for:

- pulsed waveforms
- distorted audio
- switching waveforms
- many digital-mode signals

A **true-RMS** meter directly measures RMS for **both sinusoidal and non-sinusoidal signals**.

That makes it the right tool when the waveform shape is not purely sinusoidal.

This is an important practical point. In radio work, a lot of signals are not clean sine waves:

- keyed signals
- digital-mode drive signals
- switching power-supply waveforms
- shaped envelopes during modulation

If the waveform is odd-looking, a true-RMS meter is often the only way to get a trustworthy reading.

### Average power, peak envelope power, and SSB speech

Another measurement idea in E8 is the difference between **average power** and **peak envelope power (PEP)**.

For an unprocessed SSB phone signal, the approximate **PEP-to-average-power ratio is 2.5 to 1**.

That ratio is determined by **speech characteristics**.

That makes sense if you think about what human speech looks like. Voice is not a steady tone. It has:

- peaks and valleys
- syllabic structure
- consonants that create brief peaks
- different emphasis from one speaker to another

So the average power is much lower than the maximum instantaneous envelope power.

This matters in real stations because it explains why an amplifier may show high peak output on voice peaks but spend most of its time delivering much less average power.

It also explains what speech processing does. Compression reduces the peak-to-average ratio, which pushes the average power closer to the PEP limit. That can make a signal sound louder, but it also increases stress on the transmitter chain and can worsen splatter if overdone.

### Analog-to-digital conversion: turning a voltage into numbers

Modern radios do a huge amount of signal processing digitally, so E8 expects you to know the basic ideas behind **analog-to-digital converters (ADCs)**.

An ADC samples an analog voltage and represents it as one of a finite number of digital values.

#### Successive-approximation ADCs

One common ADC type is **successive approximation**.

A successive-approximation ADC works like a binary search. It tests the most significant bit first, compares the result to the input, keeps or clears that bit, and then moves to the next bit. This continues until all bits are resolved.

That makes SAR converters a practical middle ground:

- faster than slow integrating approaches
- lower power and simpler than flash converters at high resolution
- common in measurement and control applications

#### Flash or direct-conversion ADCs

A **flash** ADC performs conversion extremely quickly by using many comparators in parallel.

That is why flash or direct-conversion ADCs are used in software-defined radio: **their very high speed allows high-frequency signals to be digitized directly**.

The tradeoff is cost, complexity, and power consumption. But if you want to digitize RF at very high sample rates, speed is everything.

### ADC resolution: number of bits means number of levels

ADC resolution is one of the easiest calculations in the subelement.

If an ADC has **N bits**, it can represent **2^N** different input levels.

So an **8-bit ADC** can encode:

**2^8 = 256 levels**

That is the whole idea behind resolution: more bits means finer voltage steps and better ability to distinguish small changes.

### Dither: adding noise on purpose

One of the stranger E8 facts is that sometimes you deliberately add noise to improve results.

**Dither** is a small amount of noise added to the ADC input to reduce quantization noise and low-level distortion.

That sounds backward until you picture what quantization does. A converter forces an analog value onto discrete step levels. When a small signal falls awkwardly between those levels, the error can become structured and distortion-like. Adding a little random noise makes that error less correlated with the signal.

The result is:

- slightly higher noise floor
- but lower low-level distortion and fewer quantization artifacts

In other words, carefully chosen randomness can make the result more faithful.

### Measuring ADC quality

An ADC can be judged in many ways, but one E8 answer you need to know is that **total harmonic distortion (THD)** is a measure of ADC quality.

If you feed an ADC a pure sine wave and harmonic content appears that was not in the original input, the converter is introducing distortion.

Lower THD means the ADC is reproducing the waveform more linearly.

### Digital-to-analog conversion and reconstruction filtering

Going the other direction, a **digital-to-analog converter (DAC)** turns numbers back into a voltage waveform.

A DAC does not automatically produce a perfectly smooth analog signal. Its raw output often looks more like a staircase than a smooth curve. That stepped output contains:

- the desired baseband or audio signal
- plus sampling-related artifacts and images

That is why a **low-pass filter** is used at the output of a DAC: **to remove spurious sampling artifacts** and smooth the waveform into the desired analog signal.

This is often called a **reconstruction filter**.

### Putting E8A together

E8A is really about one big idea: **signals can be represented, measured, sampled, and reconstructed without losing sight of what they really are**.

If you remember the following, you are in good shape:

- time domain = amplitude vs. time
- Fourier analysis explains complex waveforms in terms of sine waves
- square waves contain odd harmonics
- true-RMS meters matter for non-sinusoidal signals
- unprocessed SSB voice has about a 2.5:1 PEP-to-average ratio
- speech characteristics set that ratio
- ADC resolution = 2^N levels
- dither can reduce quantization artifacts
- flash ADCs are used when speed is critical
- DAC output filters remove sampling images

---

## Group E8B — FM and PM behavior, multiplexing, and OFDM

This group is about how information is impressed onto a carrier and how multiple information streams can share spectrum efficiently.

### Modulation index in FM

For **frequency modulation (FM)**, the **modulation index** is:

**β = frequency deviation / modulating frequency**

That formula matters because it tells you how “wide” the modulation is in a spectral sense. Larger deviation or lower modulating frequency means a larger modulation index.

Worked examples from the pool:

- deviation = 3000 Hz, highest modulating frequency = 1000 Hz
  - β = 3000 / 1000 = **3**
- deviation = 6000 Hz, highest modulating frequency = 2000 Hz
  - β = 6000 / 2000 = **3**

The same index can come from different combinations of deviation and modulating frequency.

A useful mental model is this:

- **larger β** = more significant sidebands and more occupied bandwidth
- **smaller β** = narrower FM spectrum

### Deviation ratio

The **deviation ratio** is closely related, but the exam treats it as its own term.

It is the ratio of:

**maximum carrier frequency deviation / highest audio modulating frequency**

Examples:

- ±5 kHz deviation with 3 kHz highest audio → 5000 / 3000 = **1.67**
- ±7.5 kHz deviation with 3.5 kHz highest audio → 7500 / 3500 = **2.14**

The easiest way to think about deviation ratio is that it gives a practical “worst-case” relationship between audio content and carrier swing. It is useful when thinking about FM occupied bandwidth.

### PM modulation index does not depend on carrier frequency

One easy place to overthink E8 is phase modulation.

The modulation index of a **phase-modulated** signal **does not depend on the RF carrier frequency**.

That is because PM is about **phase deviation**, not about where the carrier happens to sit in the RF spectrum. Changing the carrier frequency moves the whole signal, but it does not change the underlying phase-deviation relationship produced by the modulating signal.

### OFDM: many subcarriers, one digital signal

**Orthogonal Frequency-Division Multiplexing (OFDM)** is a digital technique that uses many closely spaced subcarriers.

It shows up in the pool in two ways:

- it is used for **digital modes**
- it is a **digital modulation technique that uses carefully spaced subcarriers so the receiver can separate them efficiently**

The key word is **orthogonal**.

Orthogonality means the subcarriers are mathematically arranged so that, even though they overlap in frequency, they can still be separated correctly at the receiver.

That gives OFDM some major advantages:

- high spectral efficiency
- robustness in channels with reflections or multipath
- the ability to split a fast data stream into many slower parallel streams

A good plain-language description is: **OFDM turns one wide, fast problem into many narrow, slower ones**.

### FDM vs. TDM

E8 also wants you to distinguish between two basic ways of combining multiple data streams.

#### Frequency Division Multiplexing (FDM)

In **frequency division multiplexing**, different streams occupy **different frequency slots at the same time**.

Each stream gets its own slice of spectrum.

Think:

- same time
- different frequencies

#### Time Division Multiplexing (TDM)

In **time division multiplexing**, different streams share the **same channel at different times**.

Each stream gets its own time slot.

Think:

- same channel
- different time slots

This distinction is easy to remember if you ask: *Are the streams separated by frequency or by time?*

### Putting E8B together

The whole group is really about managing information on carriers and inside channels.

Keep these straight:

- FM modulation index = deviation / modulating frequency
- deviation ratio = max deviation / highest audio frequency
- PM modulation index does not depend on carrier frequency
- OFDM = many orthogonal subcarriers for digital communication
- FDM separates streams by frequency
- TDM separates streams by time

If you remember the function of each technique instead of just the names, the questions become much easier.

---

## Group E8C — Digital signaling, bandwidth, error handling, and modern networked modes

This is the broadest E8 group. It covers how digital symbols carry information, how occupied bandwidth is controlled, how errors are handled, and how some digital radio networks organize themselves.

### Symbol rate and baud

The first idea to anchor is that **symbol rate** is the rate at which the waveform changes state to convey information.

That is the same thing as **baud**.

So when the pool asks for the relationship between symbol rate and baud, the answer is simple:

**they are the same**

This matters because people often confuse:

- **symbol rate**
- **bit rate**
- **character rate**

They are not automatically the same.

A symbol can represent one bit, or more than one bit, depending on the modulation scheme.

### QAM and constellation diagrams

**Quadrature Amplitude Modulation (QAM)** transmits data by modulating two carriers of the same frequency that are **90 degrees out of phase**.

Those two components are often called the I and Q components.

Because both amplitude and phase can vary, QAM can pack a lot of information into each symbol.

That is why higher-order QAM formats support high data rates.

The visual tool used to describe this is the **constellation diagram**.

A constellation diagram shows the **possible amplitude and phase states for each symbol**.

Each point represents one allowed symbol location in the complex plane.

This gives you a useful chain of ideas:

- QAM uses amplitude and phase together
- each unique signal state is a symbol
- constellation points show those states visually
- more points means more bits per symbol, but tighter spacing and less noise margin

### Increasing data rate without increasing bandwidth

One of the most important conceptual questions in E8 asks how to increase data rate without increasing bandwidth.

The answer is **use a more efficient digital code**.

In practical terms, that means encoding more information into each symbol or using the available waveform states more effectively.

The general lesson is that you do **not** always need a wider signal to carry more information. Sometimes you need smarter coding and modulation.

Of course, the tradeoff is usually that the receiver needs:

- better signal-to-noise ratio
- more linearity
- better frequency and phase accuracy

Efficiency is rarely free.

### PSK bandwidth control: change phase cleanly

Phase-shift keying can occupy more bandwidth than necessary if symbol transitions are abrupt.

That is why the exam emphasizes two related ideas.

#### Change phase at zero crossings

The phase of a PSK signal should be changed at the **zero crossing of the RF signal** to **minimize bandwidth**.

Why? Because a phase jump at some arbitrary amplitude can create abrupt discontinuities. Abrupt discontinuities spread energy over a wider frequency range.

Changing the phase where the waveform crosses zero reduces that spectral splatter.

#### PSK31 uses sinusoidal data pulses

PSK31 minimizes bandwidth by using **sinusoidal data pulses**.

This is really the same lesson in another form: **smooth transitions occupy less bandwidth than abrupt ones**.

That is not just a PSK31 trick. It is a general signal-quality principle that shows up over and over in radio.

### Occupied bandwidth examples: CW, FT8, and high-speed FM data

E8 includes a few bandwidth numbers that are worth knowing because they anchor your intuition.

#### CW bandwidth depends on speed and edge shaping

The bandwidth of a transmitted CW signal depends on:

- **keying speed**
- **shape factor**, meaning rise and fall time

Faster keying means faster changes. Sharper rise and fall times mean more abrupt changes. Both of those widen the signal.

That is why the approximate bandwidth of a **13-WPM** Morse transmission is about **52 Hz**.

The exact number is less important than the principle: CW is narrow, but not infinitely narrow, and bad keying shape makes it wider.

#### FT8 is very narrow

An **FT8** signal is about **50 Hz** wide.

That fits the whole design philosophy of FT8. It is optimized for:

- weak-signal work
- modest information rate
- high decoding sensitivity
- compact occupied bandwidth

#### High-speed ASCII FM data is much wider

At the other end of the scale, a **4,800-Hz frequency shift, 9,600-baud ASCII FM transmission** occupies about **15.36 kHz**.

For the exam, know that number and what it means. The big picture is enough:

- higher symbol rate widens the signal
- larger frequency shift widens the signal
- fast FM data takes much more bandwidth than narrow weak-signal modes

That is exactly the kind of comparison the exam wants you to understand.

### ARQ: error correction by asking again

**ARQ** stands for an automatic repeat-request method.

Its key idea is simple: **if errors are detected, a retransmission is requested**.

So ARQ is not “magic forward correction inside the same block.” It is a feedback process.

That makes it very effective when:

- a return path exists
- delay is acceptable
- the system can afford occasional retransmissions

### Gray code: one-bit change between adjacent values

**Gray code** is the code in which only **one bit changes between sequential values**.

That matters in systems such as shaft encoders and other transition-sensitive devices because it reduces ambiguity during state changes. If two or three bits tried to change at once and they did not switch perfectly together, a conventional binary code could momentarily look like the wrong number. Gray code reduces that risk.

### Mesh networking basics in amateur radio

The E8 pool includes two questions about mesh networks.

The important facts are:

- mesh nodes use **Internet Protocol (IP)** addresses
- nodes form the network through **discovery and link-establishment protocols**

That tells you what a mesh network really is: a self-forming packet network where nodes find neighbors and build paths dynamically.

It is not just ordinary repeater operation with a new name. It is networking.

### Putting E8C together

E8C is easier if you treat it as one continuous story about digital efficiency.

- baud = symbol rate
- QAM uses amplitude and phase to encode symbols
- constellation diagrams show possible symbol states
- more efficient coding can raise data rate without widening bandwidth
- smoother transitions reduce occupied bandwidth
- CW and FT8 are narrow because they change slowly and/or are tightly designed
- ARQ fixes errors by retransmission
- Gray code minimizes ambiguity between adjacent states
- mesh networking uses IP and self-discovery protocols

---

## Group E8D — Spread spectrum, signal cleanliness, and common digital-mode quality issues

This group is where E8 turns from “how signals carry information” to “how signals stay usable and polite.”

### Why spread spectrum resists interference

A spread-spectrum receiver is resistant to interference because signals that do **not** match the spreading method are strongly suppressed in the receiver.

That is the real point.

Spread-spectrum resistance is not mainly about brute transmitter power. It is about the fact that the receiver is looking for a very specific coded structure. Signals without that structure do not correlate correctly and tend to appear noise-like.

### Direct sequence vs. frequency hopping

The pool asks you to distinguish the two best-known spread-spectrum methods.

#### Direct sequence spread spectrum (DSSS)

**Direct sequence** spread spectrum uses a **high-speed binary bit stream** to shift the phase of an RF carrier.

This fast code sequence spreads the signal energy over a wider bandwidth.

The receiver uses the same code to despread the signal and recover the wanted information.

#### Frequency hopping spread spectrum (FHSS)

**Frequency hopping** spread spectrum rapidly changes the transmitter frequency according to a **pseudorandom sequence**.

Both transmitter and receiver follow the same hopping pattern, so they stay coordinated while interference on any one frequency only affects a small part of the overall transmission.

A good memory shortcut is:

- **direct sequence** = spread by coding the waveform directly
- **frequency hopping** = spread by moving around the band

### Key clicks: the cost of abrupt CW keying

A very common E8 theme is that abrupt transitions create wider signals.

In CW, **extremely short rise or fall time** causes **key clicks**.

Key clicks are wideband transients produced by turning RF on and off too abruptly.

That is why the most common way to reduce key clicks is to **increase rise and fall times**.

Notice the bigger principle underneath:

- abrupt edge = wide spectrum
- smoother edge = narrower spectrum

That principle connects CW keying, PSK shaping, Fourier analysis, and DAC reconstruction. E8 keeps coming back to the same physics from different directions.

### AFSK overmodulation and excessive audio drive

In AFSK systems, one very common cause of overmodulation is **excessive transmit audio level**.

That is a practical station-adjustment issue.

If you feed too much audio into the transmitter chain:

- the tones stop being clean
- the transmitted deviation may be wrong
- distortion products rise
- the signal becomes wider and harder to decode cleanly

This is why digital-mode setup usually starts with careful audio-level adjustment instead of simply “more drive = better signal.”

### IMD as a measure of digital-signal cleanliness

For AFSK distortion caused by excessive input audio, the evaluated parameter is **intermodulation distortion (IMD)**.

IMD tells you how much unwanted mixing or nonlinear-product energy is being created.

Lower IMD products mean a cleaner, more linear signal.

The pool also gives one benchmark value: an acceptable maximum IMD level for an **idling PSK** signal is **-30 dB**.

That means the unwanted products should be at least 30 dB below the main signal.

This is one of those questions that is worth learning exactly, but the practical lesson matters too: **digital signals still depend heavily on transmitter linearity**.

### Parity bits: simple error detection

Including **parity bits** in ASCII characters gives the receiver a way to detect **some types of errors**.

Parity is simple, not magical.

It can tell the receiver that something is wrong with a character, but it does not provide full correction and it does not catch every possible error pattern. Still, it is a useful first layer of protection.

### Baudot vs. ASCII

The E8 pool closes with a pair of classic digital-code questions.

#### Baudot

Baudot uses:

- **5 data bits per character**
- **letters and figures shift characters** to change meaning

That means the same five-bit patterns can represent different symbols depending on whether the system is in letters mode or figures mode.

#### ASCII

ASCII uses:

- **7 or 8 bits** in common practice
- a much larger character set
- the ability to represent **both uppercase and lowercase** text

That larger character set is the specific exam advantage tested in E8.

So if you need a quick contrast:

- **Baudot** = compact, older, shift-dependent
- **ASCII** = larger, more flexible, mixed case available

### Putting E8D together

The whole group is about keeping signals recoverable in the real world.

- spread spectrum rejects unmatched interference by code structure
- direct sequence and frequency hopping are different spreading methods
- abrupt CW keying causes key clicks
- longer rise/fall times reduce clicks
- AFSK is easily degraded by too much audio drive
- IMD is a key cleanliness measure
- parity detects some errors
- ASCII is more expressive than Baudot

---

## Pulling the whole subelement together

E8 looks broad at first, but most of it comes back to a few recurring themes.

### 1. Sharp time-domain edges create wide frequency-domain signals

This shows up in:

- square-wave harmonics
- key clicks
- PSK transitions
- DAC output artifacts

If a waveform changes abruptly, expect it to occupy more spectrum.

### 2. Digital systems trade speed, complexity, and bandwidth

This shows up in:

- flash ADCs for SDR
- QAM constellation density
- efficient coding for higher throughput
- OFDM using many coordinated subcarriers

You can often get more performance, but usually at the cost of tighter design tolerances.

### 3. Signal quality is not just about whether communication works

It is also about whether the signal is clean.

This shows up in:

- true-RMS measurement of non-sinusoidal waveforms
- PEP vs. average power in SSB
- IMD in digital modes
- proper rise and fall shaping in CW and PSK

### 4. A lot of modern radio is really applied signal processing

This shows up in:

- Fourier analysis
- ADC and DAC behavior
- OFDM
- QAM
- ARQ
- mesh networking

The amateur exam is not asking you to become a communications theorist. It is asking you to recognize the core ideas behind the tools modern radios already use.

---

## Final Summary

E8 is the subelement that ties waveform shape, modulation, bandwidth, and signal cleanliness into one picture.

The most important points to hold onto are:

- **time domain** means amplitude vs. time
- **Fourier analysis** explains why non-sinusoidal waveforms contain harmonics
- **true-RMS meters** are needed for many non-sinusoidal signals
- **unprocessed SSB voice** has about a **2.5:1** PEP-to-average-power ratio
- **ADC resolution** is **2^N** levels, and fast SDR sampling needs very fast converters
- **FM modulation index** and **deviation ratio** tell you how wide FM behavior tends to be
- **OFDM, FDM, and TDM** are all ways of organizing information efficiently
- **baud equals symbol rate**
- **QAM** and **constellation diagrams** describe digital states in amplitude and phase
- **smooth transitions** keep signals narrow; abrupt ones make them wider
- **ARQ** corrects errors by requesting retransmission
- **spread spectrum** rejects unmatched interference by coding or hopping methods
- **key clicks, IMD, and overdriven audio** are all reminders that dirty signals are usually caused by bad transitions or bad linearity
- **ASCII** is more capable than **Baudot**, especially because it supports both uppercase and lowercase characters

If E7 taught you what circuit blocks do, E8 teaches you what those blocks are trying to do to the signal itself.

And in radio, the signal is the whole game.

---

*Extra-class exam: 50 questions, must pass with 37 or higher (74%). E8 contributes 4 questions.*
