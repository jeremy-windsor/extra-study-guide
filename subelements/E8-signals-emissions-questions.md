# E8 — Signals and Emissions
*4 questions on the exam from a pool of 48*

## Group E8A — AC waveforms: sine, square, sawtooth, and irregular waveforms; AC measurements; average and PEP of RF signals; Fourier analysis; analog to digital conversion

### E8A01
**What technique shows that a square wave is made up of a sine wave and its odd harmonics?**
- **A) Fourier analysis** ✅
- B) Vector analysis
- C) Numerical analysis
- D) Differential analysis

> Fourier analysis shows that a square wave is made up of a sine wave at the fundamental frequency plus all odd harmonics (3rd, 5th, 7th...) with amplitudes that decrease as 1/n. A perfect square wave = sin(f) + (1/3)sin(3f) + (1/5)sin(5f) + ... This mathematical decomposition is the foundation of signal analysis and explains why non-sinusoidal waveforms generate harmonics.

### E8A02
**Which of the following is a type of analog-to-digital conversion?**
- **A) Successive approximation** ✅
- B) Harmonic regeneration
- C) Level shifting
- D) Phase reversal

> Successive approximation is a type of analog-to-digital conversion. The SAR ADC uses a binary search algorithm: it compares the input to a series of reference voltages, starting with the most significant bit and working down. Each comparison determines one bit. An N-bit conversion takes N clock cycles. SAR ADCs are the most common type for medium-speed, medium-resolution applications.

### E8A03
**Which of the following describes a signal in the time domain?**
- A) Power at intervals of phase
- **B) Amplitude at different times** ✅
- C) Frequency at different times
- D) Discrete impulses in time order

> A signal in the time domain shows amplitude at different times. This is what an oscilloscope displays — voltage (vertical) vs. time (horizontal). The time domain representation shows the waveform's shape, including rise times, pulse widths, and amplitude variations. The frequency domain (spectrum analyzer) shows amplitude vs. frequency instead.

### E8A04
**What is “dither” with respect to analog-to-digital converters?**
- A) An abnormal condition where the converter cannot settle on a value to represent the signal
- **B) A small amount of noise added to the input signal to reduce quantization noise** ✅
- C) An error caused by irregular quantization step size
- D) A method of decimation by randomly skipping samples

> Dither is a small amount of noise intentionally added to the input signal of an ADC to reduce quantization noise. Without dither, low-level signals that fall between quantization levels produce severe distortion. Adding a small random noise signal causes the ADC to toggle between adjacent levels, averaging out to the true signal value. The noise floor increases slightly but distortion drops dramatically.

### E8A05
**What is the benefit of making voltage measurements with a true-RMS calculating meter?**
- A) An inverse Fourier transform can be used
- B) The signal’s RMS noise factor is also calculated
- C) The calculated RMS value can be converted directly into phasor form
- **D) RMS is measured for both sinusoidal and non-sinusoidal signals** ✅

> A true-RMS meter correctly measures RMS voltage for both sinusoidal and non-sinusoidal signals. Standard meters assume a sine wave and apply a correction factor that's only accurate for sinusoidal waveforms. For digital signals, pulsed waveforms, or distorted signals, only a true-RMS meter gives accurate readings. This matters in amateur radio for measuring digital mode transmit power and non-sinusoidal waveforms.

### E8A06
**What is the approximate ratio of PEP-to-average power in an unprocessed single-sideband phone signal?**
- **A) 2.5 to 1** ✅
- B) 25 to 1
- C) 1 to 1
- D) 13 to 1

> The PEP-to-average power ratio of an unprocessed SSB voice signal is approximately 2.5 to 1. Human speech has peaks (consonants, emphasis) that are about 2.5 times the average level. This ratio determines how much of the amplifier's capability is actually used on average. Speech processing (compression) reduces this ratio, increasing average power toward PEP.

### E8A07
**What determines the PEP-to-average power ratio of an unprocessed single-sideband phone signal?**
- A) The frequency of the modulating signal
- **B) Speech characteristics** ✅
- C) The degree of carrier suppression
- D) Amplifier gain

> Speech characteristics determine the PEP-to-average power ratio of an unprocessed SSB signal. Different voices, speaking styles, and languages produce different peak-to-average ratios. A person who speaks with even emphasis has a lower ratio; someone with punchy, percussive speech has a higher ratio. The typical average is about 2.5:1.

### E8A08
**Why are direct or flash conversion analog-to-digital converters used for a software defined radio?**
- A) Very low power consumption decreases frequency drift
- B) Immunity to out-of-sequence coding reduces spurious responses
- **C) Very high speed allows digitizing high frequencies** ✅
- D) All these choices are correct

> Direct (flash) conversion ADCs are used for SDR because their very high speed allows digitizing high frequencies. A flash ADC converts the entire input in one clock cycle using parallel comparators — no iterative steps needed. This enables sampling rates of hundreds of MHz to GHz, sufficient for directly digitizing RF signals. The tradeoff: flash ADCs are expensive and power-hungry.

### E8A09
**How many different input levels can be encoded by an analog-to-digital converter with 8-bit resolution?**
- A) 8
- B) 8 multiplied by the gain of the input amplifier
- C) 256 divided by the gain of the input amplifier
- **D) 256** ✅

> An 8-bit ADC can encode 2⁸ = 256 different input levels. Each bit doubles the number of levels: 1 bit = 2 levels, 2 bits = 4, ... 8 bits = 256. The step size (resolution) = full-scale range / 256. For a 1V range: each step = 1/256 ≈ 3.9 mV.

### E8A10
**What is the purpose of a low-pass filter used at the output of a digital-to-analog converter?**
- A) Lower the input bandwidth to increase the effective resolution
- B) Improve accuracy by removing out-of-sequence codes from the input
- **C) Remove spurious sampling artifacts from the output signal** ✅
- D) All these choices are correct

> A low-pass filter at the output of a DAC removes spurious sampling artifacts (images of the baseband signal at multiples of the sample frequency). The DAC output is a stepped (staircase) waveform that contains the desired signal plus copies at the sample rate and its harmonics. The low-pass reconstruction filter smooths the steps and removes these artifacts.

### E8A11
**Which of the following is a measure of the quality of an analog-to-digital converter?**
- **A) Total harmonic distortion** ✅
- B) Peak envelope power
- C) Reciprocal mixing
- D) Power factor

> Total harmonic distortion (THD) is a measure of ADC quality. THD quantifies how much harmonic content the ADC adds to a pure sine wave input — lower THD means a more linear, accurate converter. Other ADC quality metrics include ENOB (effective number of bits), SFDR (spurious-free dynamic range), and INL/DNL (integral/differential nonlinearity).

## Group E8B — Modulation and demodulation: phase modulation; phase velocity; digital waveforms; modulation index; pulse modulation; frequency and time division multiplexing

### E8B01
**What is the modulation index of an FM signal?**
- **A) The ratio of frequency deviation to modulating signal frequency** ✅
- B) The ratio of modulating signal amplitude to frequency deviation
- C) The modulating signal frequency divided by the bandwidth of the transmitted signal
- D) The bandwidth of the transmitted signal divided by the modulating signal frequency

> The modulation index of an FM signal is the ratio of frequency deviation to modulating signal frequency: β = Δf / f_mod. For example, if the deviation is 5 kHz and the modulating frequency is 1 kHz: β = 5000/1000 = 5. Higher modulation index means wider bandwidth. The modulation index determines the number and amplitude of significant sidebands (from Bessel functions).

### E8B02
**How does the modulation index of a phase-modulated emission vary with RF carrier frequency?**
- A) It increases as the RF carrier frequency increases
- B) It decreases as the RF carrier frequency increases
- C) It varies with the square root of the RF carrier frequency
- **D) It does not depend on the RF carrier frequency** ✅

> The modulation index of a phase-modulated signal does NOT depend on the RF carrier frequency. PM modulation index depends on the modulating signal amplitude and the phase sensitivity of the modulator, not on the carrier frequency. FM modulation index similarly doesn't depend on carrier frequency — both depend on deviation and modulating frequency only.

### E8B03
**What is the modulation index of an FM phone signal having a maximum frequency deviation of 3000 Hz either side of the carrier frequency if the highest modulating frequency is 1000 Hz?**
- **A) 3** ✅
- B) 0.3
- C) 6
- D) 0.6

> Modulation index = maximum deviation / modulating frequency. β = 3000 Hz / 1000 Hz = 3. This is straightforward application of the FM modulation index formula. A modulation index of 3 means the signal has significant energy in multiple sideband pairs (Bessel function analysis shows about 6 significant sidebands on each side).

### E8B04
**What is the modulation index of an FM phone signal having a maximum carrier deviation of plus or minus 6 kHz if the highest modulating frequency is 2 kHz?**
- A) 0.3
- **B) 3** ✅
- C) 0.6
- D) 6

> Modulation index = maximum deviation / modulating frequency. β = 6000 Hz / 2000 Hz = 3. The 6 kHz deviation with 2 kHz maximum modulating frequency gives the same modulation index as the previous example. Note: the modulating frequency used is the highest audio frequency present.

### E8B05
**What is the deviation ratio of an FM phone signal having a maximum frequency swing of plus or minus 5 kHz if the highest modulation frequency is 3 kHz?**
- A) 6
- B) 0.167
- C) 0.6
- **D) 1.67** ✅

> Deviation ratio = maximum frequency deviation / highest modulating frequency. Deviation ratio = 5000 Hz / 3000 Hz = 1.67. Deviation ratio is similar to modulation index but uses the highest modulating frequency (maximum audio frequency) as the denominator, giving a single worst-case figure for bandwidth calculation.

### E8B06
**What is the deviation ratio of an FM phone signal having a maximum frequency swing of plus or minus 7.5 kHz if the highest modulation frequency is 3.5 kHz?**
- **A) 2.14** ✅
- B) 0.214
- C) 0.47
- D) 47

> Deviation ratio = maximum deviation / highest modulating frequency. Deviation ratio = 7500 Hz / 3500 Hz = 2.14. This represents the maximum modulation index that occurs when the highest audio frequency is present at maximum deviation.

### E8B07
**Orthogonal frequency-division multiplexing (OFDM) is a technique used for which types of amateur communication?**
- **A) Digital modes** ✅
- B) Extremely low-power contacts
- C) EME
- D) OFDM signals are not allowed on amateur bands

> OFDM (Orthogonal Frequency-Division Multiplexing) is used for digital modes in amateur communications. OFDM divides the available bandwidth into many closely-spaced subcarriers, each carrying a portion of the data at a lower rate. The subcarriers are orthogonal (mathematically non-interfering). OFDM is used in Wi-Fi, digital TV, and some amateur digital modes.

### E8B08
**What describes orthogonal frequency-division multiplexing (OFDM)?**
- A) A frequency modulation technique that uses non-harmonically related frequencies
- B) A bandwidth compression technique using Fourier transforms
- C) A digital mode for narrow-band, slow-speed transmissions
- **D) A digital modulation technique using subcarriers at frequencies chosen to avoid intersymbol** ✅

> OFDM is a digital modulation technique using subcarriers at frequencies chosen to avoid intersymbol interference. The key word is 'orthogonal' — the subcarrier spacing is chosen so that each subcarrier's peak aligns with zeros of all other subcarriers, eliminating crosstalk without guard bands. This maximizes spectral efficiency.

### E8B09
**What is deviation ratio?**
- A) The ratio of the audio modulating frequency to the center carrier frequency
- **B) The ratio of the maximum carrier frequency deviation to the highest audio modulating frequency** ✅
- C) The ratio of the carrier center frequency to the audio modulating frequency
- D) The ratio of the highest audio modulating frequency to the average audio modulating frequency

> Deviation ratio is the ratio of the maximum carrier frequency deviation to the highest audio modulating frequency. It's used for FM bandwidth estimation: bandwidth ≈ 2 × (Δf + f_mod_max) = 2 × f_mod_max × (deviation_ratio + 1) (Carson's rule). Higher deviation ratio = wider bandwidth.

### E8B10
**What is frequency division multiplexing (FDM)?**
- A) The transmitted signal jumps from band to band at a predetermined rate
- **B) Dividing the transmitted signal into separate frequency bands that each carry a different data stream** ✅
- C) The transmitted signal is divided into packets of information
- D) Two or more information streams are merged into a digital combiner, which then pulse position

> Frequency division multiplexing (FDM) divides the transmitted signal into separate frequency bands, each carrying a different data stream simultaneously. Each data stream is modulated onto its own carrier frequency within the allocated bandwidth. FDM is used in telephone trunk lines, cable TV, and some radio applications. OFDM is a modern digital form of FDM.

### E8B11
**What is digital time division multiplexing?**
- A) Two or more data streams are assigned to discrete sub-carriers on an FM transmitter
- **B) Two or more signals are arranged to share discrete time slots of a data transmission** ✅
- C) Two or more data streams share the same channel by transmitting time of transmission as the sub-
- D) Two or more signals are quadrature modulated to increase bandwidth efficiency

> Digital time division multiplexing (TDM) arranges two or more signals to share discrete time slots in a data transmission. Each signal gets exclusive use of the full bandwidth during its time slot. Signals take turns transmitting in a regular pattern. TDM is used in digital telephone systems (T1/E1 lines) and some digital radio systems.

## Group E8C — Digital signals: digital communication modes; information rate vs bandwidth; error correction coding; spread spectrum; OFDM

### E8C01
**What is Quadrature Amplitude Modulation or QAM?**
- A) A technique for digital data compression used in digital television which removes redundancy in the
- **B) Transmission of data by modulating the amplitude of two carriers of the same frequency but 90** ✅
- C) A method of performing single sideband modulation by shifting the phase of the carrier and
- D) A technique for analog modulation of television video signals using phase modulation and

> QAM (Quadrature Amplitude Modulation) transmits data by modulating the amplitude of two carriers of the same frequency but 90 degrees out of phase (in quadrature). By independently varying both amplitude and phase, QAM creates a constellation of signal points, each representing a different data symbol. 16-QAM has 16 points = 4 bits per symbol; 64-QAM has 64 points = 6 bits per symbol. Higher-order QAM increases data throughput, but the constellation points are packed closer together, so the receiver needs a better signal-to-noise ratio to distinguish them reliably.

### E8C02
**What is the definition of symbol rate in a digital transmission?**
- A) The number of control characters in a message packet
- B) The maximum rate at which the forward error correction code can make corrections
- **C) The rate at which the waveform changes to convey information** ✅
- D) The number of characters carried per second by the station-to-station link

> Symbol rate is the rate at which the transmitted waveform changes state to convey information. It is measured in symbols per second, or baud.

### E8C03
**Why should the phase of a PSK signal be changed at the zero crossing of the RF signal?**
- **A) To minimize bandwidth** ✅
- B) To simplify modulation
- C) To improve carrier suppression
- D) All these choices are correct

> Changing PSK phase at a zero crossing avoids abrupt amplitude discontinuities and keeps the signal spectrally cleaner. The result is less splatter, so the occupied bandwidth stays as small as possible.

### E8C04
**What technique minimizes the bandwidth of a PSK31 signal?**
- A) Zero-sum character encoding
- B) Reed-Solomon character encoding
- **C) Use of sinusoidal data pulses** ✅
- D) Use of linear data pulses

> PSK31 minimizes bandwidth by shaping the symbols with sinusoidal data pulses. Smooth symbol edges reduce keying sidebands and keep the signal much narrower than a hard-switched waveform would be.

### E8C05
**What is the approximate bandwidth of a 13-WPM International Morse Code transmission?**
- A) 13 Hz
- B) 26 Hz
- **C) 52 Hz** ✅
- D) 104 Hz

> Morse code bandwidth is very narrow because the keyed signal is slow and its transitions are shaped by the sending speed. At about 13 WPM, the occupied bandwidth is roughly 4 times the WPM rate, or about 52 Hz.

### E8C06
**What is the bandwidth of an FT8 signal?**
- A) 10 Hz
- **B) 50 Hz** ✅
- C) 600 Hz
- D) 2.4 kHz

> FT8 occupies about 50 Hz because it uses a very narrow 8-tone digital signal with closely spaced symbols. Its design prioritizes weak-signal robustness rather than throughput, so the occupied bandwidth stays tiny.

### E8C07
**What is the bandwidth of a 4,800-Hz frequency shift, 9,600-baud ASCII FM transmission?**
- **A) 15.36 kHz** ✅
- B) 9.6 kHz
- C) 4.8 kHz
- D) 5.76 kHz

> A 9600-baud signal with a 4800-Hz shift needs bandwidth for both the symbol rate and the tone separation. When you apply the standard FSK bandwidth estimate, the result is about 15.36 kHz.

### E8C08
**How does ARQ accomplish error correction?**
- A) Special binary codes provide automatic correction
- B) Special polynomial codes provide automatic correction
- C) If errors are detected, redundant data is substituted
- **D) If errors are detected, a retransmission is requested** ✅

> ARQ detects that an error occurred and then asks for the data to be sent again. The retransmission request is what makes the error correction automatic from the user’s point of view.

### E8C09
**Which digital code allows only one bit to change between sequential code values?**
- A) Binary Coded Decimal Code
- B) Extended Binary Coded Decimal Interchange Code
- C) Extended ASCII
- **D) Gray code** ✅

> Gray code is the code where only one bit changes between adjacent values. That minimizes transition errors in encoders and makes the code easier to read during a single-step change.

### E8C10
**How can data rate be increased without increasing bandwidth?**
- A) It is impossible
- B) Increasing analog-to-digital conversion resolution
- **C) Using a more efficient digital code** ✅
- D) Using forward error correction

> You can raise data rate without widening the signal by packing more information into each symbol. Using a more efficient digital code increases throughput while keeping the occupied bandwidth the same.

### E8C11
**What is the relationship between symbol rate and baud?**
- **A) They are the same** ✅
- B) Baud is twice the symbol rate
- C) Baud rate is half the symbol rate
- D) The relationship depends on the specific code used

> Baud is simply symbol rate, so the two terms mean the same thing. If a system sends 100 symbols per second, its rate is 100 baud.

### E8C12
**What factors affect the bandwidth of a transmitted CW signal?**
- A) IF bandwidth and Q
- B) Modulation index and output power
- **C) Keying speed and shape factor (rise and fall time)** ✅
- D) All these choices are correct

> CW bandwidth depends on how fast the keying changes and how gently the waveform rises and falls. Faster keying and sharper edges spread more energy into the sidebands, widening the signal.

### E8C13
**What is described by the constellation diagram of a QAM or QPSK signal?**
- A) How many carriers may be present at the same time
- **B) The possible phase and amplitude states for each symbol** ✅
- C) Frequency response of the signal stream
- D) The number of bits used for error correction in the protocol

> A constellation diagram shows the allowed phase and amplitude states for each symbol in a QAM or QPSK signal. Each dot represents one symbol location in the complex plane.

### E8C14
**What type of addresses do nodes have in a mesh network?**
- A) Email
- B) Trust server
- **C) Internet Protocol (IP)** ✅
- D) Talk group

> Mesh network nodes use Internet Protocol addresses so they can route packets like normal IP devices. The mesh layers routing on top of standard network addressing.

### E8C15
**What technique do individual nodes use to form a mesh network?**
- A) Forward error correction and Viterbi codes
- B) Acting as store-and-forward digipeaters
- **C) Discovery and link establishment protocols** ✅
- D) Custom code plugs for the local trunking systems

> Individual mesh nodes discover each other and establish links using discovery and link-establishment protocols. That lets the network self-form without manually wiring every route.

## Group E8D — Keying defects and noise in digital signals: signal noise; static; interference; modulation index

### E8D01
**Why are received spread spectrum signals resistant to interference?**
- **A) Signals not using the spread spectrum algorithm are suppressed in the receiver** ✅
- B) The high power used by a spread spectrum transmitter keeps its signal from being easily overpowered
- C) Built-in error correction codes minimize interference
- D) If the receiver detects interference, it will signal the transmitter to change frequencies

> Spread-spectrum receivers suppress signals that do not match the spreading code. Anything outside the code looks like noise, so interference from unrelated signals is strongly reduced.

### E8D02
**What spread spectrum communications technique uses a high-speed binary bit stream to shift the phase of an RF carrier?**
- A) Frequency hopping
- **B) Direct sequence** ✅
- C) Binary phase-shift keying
- D) Phase compandored spread spectrum

> Direct sequence spread spectrum uses a fast binary chip stream to flip the phase of the carrier. The high-rate code spreads the signal energy across a wider band.

### E8D03
**Which describes spread spectrum frequency hopping?**
- A) If interference is detected by the receiver, it will signal the transmitter to change frequencies
- B) RF signals are clipped to generate a wide band of harmonics which provides redundancy to correct
- C) A binary bit stream is used to shift the phase of an RF carrier very rapidly in a pseudorandom
- **D) Rapidly varying the frequency of a transmitted signal according to a pseudorandom sequence** ✅

> Frequency hopping spread spectrum rapidly changes the transmit frequency according to a pseudorandom pattern. Both ends follow the same hopping sequence so they stay synchronized.

### E8D04
**What is the primary effect of extremely short rise or fall time on a CW signal?**
- A) More difficult to copy
- B) The generation of RF harmonics
- **C) The generation of key clicks** ✅
- D) More difficult to tune

> Very short rise and fall times make the CW waveform abrupt, which produces key clicks. Those sharp transitions spread energy widely and create interference outside the intended channel.

### E8D05
**What is the most common method of reducing key clicks?**
- **A) Increase keying waveform rise and fall times** ✅
- B) Insert low-pass filters at the transmitter output
- C) Reduce keying waveform rise and fall times
- D) Insert high-pass filters at the transmitter output

> The usual way to reduce key clicks is to lengthen the rise and fall times of the keying waveform. Smoother edges mean less wideband energy and fewer clicks.

### E8D06
**What is the advantage of including parity bits in ASCII characters?**
- A) Faster transmission rate
- B) Signal-to-noise ratio is improved
- C) A larger character set is available
- **D) Some types of errors can be detected** ✅

> Parity bits let the receiver check whether the number of 1s is even or odd, so some transmission errors can be detected. They do not correct every error, but they provide a simple error check.

### E8D07
**What is a common cause of overmodulation of AFSK signals?**
- A) Excessive numbers of retries
- B) Excessive frequency deviation
- C) Bit errors in the modem
- **D) Excessive transmit audio levels** ✅

> AFSK overmodulation usually happens when the audio drive level is too high. Too much audio pushes the modulator past its linear range and distorts the transmitted tones.

### E8D08
**What parameter evaluates distortion of an AFSK signal caused by excessive input audio levels?**
- A) Signal-to-noise ratio
- B) Baud error rate
- C) Repeat Request Rate (RRR)
- **D) Intermodulation Distortion (IMD)** ✅

> Intermodulation distortion is the metric used to judge how badly excessive audio levels are distorting an AFSK signal. Higher IMD means the tones are mixing into unwanted products.

### E8D09
**What is considered an acceptable maximum IMD level for an idling PSK signal?**
- A) +5 dB
- B) +10 dB
- C) +15 dB
- **D) -30 dB** ✅

> For an idling PSK signal, the unwanted intermodulation products should be at least 30 dB below the main signal. That is why -30 dB is the acceptable maximum IMD level.

### E8D10
**What are some of the differences between the Baudot digital code and ASCII?**
- A) Baudot uses 4 data bits per character, ASCII uses 7 or 8; Baudot uses 1 character as a letters/figures
- **B) Baudot uses 5 data bits per character, ASCII uses 7 or 8; Baudot uses 2 characters as letters/figures** ✅
- C) Baudot uses 6 data bits per character, ASCII uses 7 or 8; Baudot has no letters/figures shift code, ASCII
- D) Baudot uses 7 data bits per character, ASCII uses 8; Baudot has no letters/figures shift code, ASCII

> Baudot uses 5 data bits per character and relies on letters/figures shift codes, while ASCII uses 7 or 8 bits and can represent uppercase, lowercase, and many more symbols.

### E8D11
**What is one advantage of using ASCII code for data communications?**
- A) It includes built-in error correction features
- B) It contains fewer information bits per character than any other code
- **C) It is possible to transmit both uppercase and lowercase text** ✅
- D) It uses one character as a shift code to send numeric and special characters

> ASCII can represent both uppercase and lowercase text, which is one of its big advantages for data communications. The larger character set makes it more flexible than older 5-bit codes.
