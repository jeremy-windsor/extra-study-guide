# Extra Class Cram Sheet — Rapid Fire Review

## Where the Points Are

If time is short, bias your final review toward the biggest buckets.

E7, Practical Circuits, has 8 questions on the exam.

E9, Antennas and Transmission Lines, has 8 questions on the exam.

E1, Rules, has 6 questions on the exam.

E6, Components, has 6 questions on the exam.

E2, Operating Procedures, has 5 questions on the exam.

E4, Amateur Practices, has 5 questions on the exam.

E5, Electrical Principles, has 4 questions on the exam.

E8, Signals and Emissions, has 4 questions on the exam.

E3, Propagation, has 3 questions on the exam.

E0, Safety, has 1 question on the exam.

## Must-Know Formulas and Number Anchors

### Core Circuit Math

Inductive reactance equals two pi times frequency times inductance.

Capacitive reactance equals one divided by two pi times frequency times capacitance.

Resonant frequency equals one divided by two pi times the square root of inductance times capacitance.

Quality factor Q equals resonant frequency divided by bandwidth.

Bandwidth equals resonant frequency divided by Q.

Q in a series resonant circuit equals reactance divided by resistance.

Q in a parallel resonant circuit equals resistance divided by reactance.

The RC time constant tau equals resistance times capacitance.

Phase angle theta equals the arctangent of the quantity inductive reactance minus capacitive reactance, divided by resistance. This applies to a series RLC circuit.

Real power equals current squared times resistance.

Apparent power S equals voltage times current.

Apparent power squared equals real power squared plus reactive power squared. This is the power triangle relationship.

Absorbed power equals forward power minus reflected power.

### RF and Receiver Math

To convert between antenna gain references, dBi equals dBd plus 2.15 dB.

Power in dBW equals 10 times the log base 10 of power in watts.

dBm equals dBW plus 30.

Reflection coefficient gamma equals load impedance minus characteristic impedance, divided by load impedance plus characteristic impedance.

Standing wave ratio equals one plus the absolute value of gamma, divided by one minus the absolute value of gamma.

Quarter-wave transformer impedance equals the square root of the product of the two impedances being matched.

Physical line length equals electrical length times velocity factor.

Far field distance is approximately two times the aperture squared divided by wavelength.

Noise rise in dB equals 10 times the log base 10 of the bandwidth ratio.

The thermal noise floor is negative 174 dBm per hertz at room temperature.

### Digital and Modulation Math

The number of ADC levels equals 2 raised to the power of N, where N is the number of bits.

The Nyquist minimum sample rate must be at least two times the highest frequency.

FM modulation index beta equals deviation divided by the modulating frequency.

Deviation ratio equals maximum deviation divided by the highest audio frequency.

Inverting op-amp gain equals negative R sub F divided by R sub 1.

Linear regulator power dissipation equals the quantity input voltage minus output voltage, times the output current.

Battery run time equals amp-hours divided by average current.

Received signal level equals transmit power plus gains minus losses, all in dB.

### See This Number, Think This Answer

30 to 300 megahertz is the range with the most restrictive RF exposure limits.

80 meters always requires an RF exposure evaluation.

If your transmitter contributes 5 percent or more of the maximum permissible exposure in an over-limit shared site, you share mitigation responsibility.

2200 meters has a limit of 1 watt EIRP. 630 meters has a limit of 5 watts EIRP.

60 meter data maximum bandwidth is 2.8 kilohertz.

HF digital voice and SSTV bandwidth is 3 kilohertz.

If a remote-control link fails, maximum transmission time is 3 minutes.

Below 30 megahertz, spurious emissions must be at least 43 dB below the fundamental.

A folded dipole has an impedance of approximately 300 ohms.

Solid polyethylene coax has a velocity factor of approximately 0.66.

FT8 is approximately 50 hertz wide.

13 words-per-minute CW is approximately 52 hertz wide.

A parabolic dish gains 6 dB when the frequency doubles, assuming the same physical dish.

A silicon bipolar junction transistor has a base-emitter turn-on voltage of approximately 0.6 to 0.7 volts.

A silicon photovoltaic cell produces approximately 0.5 volts open-circuit.

## High-Miss Mnemonics and One-Liners

USB goes up, LSB goes down. Watch the band edges.

ELI the ICE man. Voltage leads current in an inductor. Current leads voltage in a capacitor.

Higher Q means narrower bandwidth.

A flip-flop halves the frequency.

Gamma match means grounded, unbalanced. Beta or hairpin match means balanced.

A half-wavelength line repeats the load impedance. A quarter-wavelength line inverts it.

A shorted stub shorter than a quarter wavelength looks inductive. An open stub shorter than a quarter wavelength looks capacitive.

Gain concentrates power. It does not create power.

A Beverage antenna is long, low, terminated, and one-way.

Colpitts uses capacitors. Hartley uses an inductor tap. Pierce uses a crystal.

Direct sequence spread spectrum codes the waveform. Frequency hopping spread spectrum moves around the band.

Bistable has 2 stable states. Monostable has 1 stable state. Astable has 0 stable states.

## E0 through E2. Rules, Safety, and Operating Traps

### E0 Safety

The primary purpose of a ground rod or earth connection is lightning charge dissipation.

A neighbor's property is considered an uncontrolled environment.

The most restrictive RF exposure range is 30 to 300 megahertz.

SAR stands for specific absorption rate, which is the rate the body absorbs RF energy.

In a shared site, if your transmitter contributes 5 percent or more of the maximum permissible exposure in an over-limit area, you share responsibility.

Microwave danger comes from high field strength due to high-gain antennas, not ionizing radiation.

100 percent tie-off means at least one lanyard is attached at all times.

Attach your climbing lanyard to the tower legs.

A shock-absorbing lanyard anchor should be above head level.

### E1 Rules. The Traps Exam Writers Love

Band edges and special bands. The entire emission must stay within the legal band, not just the dial frequency. For USB near the upper edge, subtract the bandwidth from the upper band edge. For LSB near the lower edge, add the bandwidth to the lower band edge. On 60 meters, CW goes on the channel center frequency. 60 meter data maximum bandwidth is 2.8 kilohertz. Spread spectrum is only allowed above 222 megahertz. On 2200 meters and 630 meters, limits use EIRP, not just transmitter output. Phone operation is allowed across the entire 630 meter band.

Special operating restrictions. Operating from a ship or aircraft requires permission from the master or pilot in command. Automatic control may pass third-party traffic only for RTTY or data. If the remote-control link is lost, transmission may continue for a maximum of 3 minutes. Before operating on 2200 meters or 630 meters, notify the UTC with your call sign and antenna coordinates, then wait 30 days unless told otherwise.

Exact rule items worth memorizing. If you are within 1 mile of an FCC monitoring facility, you must protect it. PRB-1 applies to state and local zoning and requires reasonable accommodation. North of Line A, no transmission on 420 to 430 megahertz. Below 30 megahertz, spurious output must be at least 43 dB below the fundamental. On 29 megahertz and below, the maximum angle-modulation index at the highest modulating frequency is 1.0.

Satellites, message content, and exceptions. Telemetry means one-way measurements at a distance. Telecommand means sending commands to control a device. The only narrow secrecy exception you should trust is that space telecommand may be encrypted. Mesh networks still may not obscure meaning. Amateurs generally may not transmit for pecuniary interest. For forwarded bad traffic, the primary responsibility falls on the originating control operator.

### E2 Operating Procedures

Satellite and specialty mode anchors. An ascending pass means the satellite moves south to north. A satellite mode designator is an uplink and downlink band pair, not an FM or SSB style mode. A linear transponder is a wideband bent pipe where many signals can share the passband. An inverting linear transponder flips the sideband. USB up becomes LSB down, and vice versa. On linear satellites, too much uplink ERP reduces the downlink power available to everyone. Satellite circular polarization helps deal with Faraday rotation and spin fading. L band corresponds to 23 centimeters. S band corresponds to 13 centimeters.

ATV and SSTV. An NTSC frame has 525 lines. Interlace means odd lines first, then even lines. Vestigial sideband means one full sideband plus part of the other. In SSTV, brightness is encoded by tone frequency, color is sent sequentially line by line, and the VIS code identifies the mode.

DX, logging, APRS, and weak-signal digital. A remote station in the U.S. requires no extra ID indicator. Latency is the delay between a control action and the transmitter response. ADIF is the general log exchange format. Cabrillo is the contest log submission format. LoTW is the contact confirmation system. Contesting is generally excluded from 30 meters. In a DX pileup, send your full call once or twice. APRS rides on AX.25 and usually uses a UI frame. The path WIDE3-1 means three hops requested and one hop remaining. MSK144 is used for meteor scatter. Q65 is used for EME or moonbounce. JT65 is a very low signal-to-noise weak-signal mode. EME QSOs use alternating synchronized transmit periods. In VHF FT8 and FT4 contest exchanges, the key item is the grid square. WSPR is a propagation beaconing mode, not a keyboard chat mode. PSK31 uses variable-length character coding. PACTOR IV has the highest throughput of the commonly listed HF digital modes. ALE means radios scan a frequency list until the called station is heard.

## E3 through E6. Propagation, Measurement, Math, and Components

### E3 Propagation Anchor Facts

An electromagnetic wave has E and H fields perpendicular to each other and perpendicular to the direction of travel.

EME works best at perigee. Fluttery EME fading is called libration fading.

When the MUF drops after dark, move to a lower band.

Meteor scatter uses ionized trails in the E region.

Tropospheric ducts often form over large bodies of water. Think 100 to 300 miles.

Auroral propagation is tied to severe geomagnetic storms and favors CW.

Trans-equatorial propagation, or TEP, occurs in the afternoon or early evening over roughly 2000 to 3000 miles, with the path crossing the geomagnetic equator.

160 meter DX works best when the path is in darkness.

Long-path propagation is most common on 40 meters and 20 meters.

A low takeoff angle means longer hops and better DX.

Ground wave prefers vertical polarization and gets worse as frequency rises.

Sporadic E favors solstice season and daytime.

A chordal hop goes from ionosphere to ionosphere without a ground reflection.

X class is the strongest solar flare class.

G5 is an extreme geomagnetic storm.

A rising A or K index means increasing geomagnetic disturbance.

Southward Bz means more likely geomagnetic trouble.

The radio horizon is about 15 percent farther than the optical horizon.

VOACAP is HF propagation prediction software.

### E4 Measurements and Receiver Behavior

Instruments. An oscilloscope shows voltage versus time. A spectrum analyzer shows amplitude versus frequency. Oscilloscope probe compensation uses a square wave. Keep the scope probe ground lead short. For linear supply ripple, use line trigger. Frequency counter accuracy mostly depends on time base accuracy. Analog voltmeter sensitivity is measured in ohms per volt. Low input resistance loads the circuit.

VNA and S-parameter basics. S11 is input reflection or return-loss behavior. S21 is forward transmission or gain. VNA calibration standards are open, short, and 50 ohm load.

Receiver and dynamic range anchors. Noise figure describes how much worse the receiver is compared to ideal thermal noise. MDS stands for minimum discernible signal. Widening bandwidth raises noise. Use the formula 10 times the log base 10 of the bandwidth ratio. Excessive phase noise plus a strong nearby signal causes reciprocal mixing. A preselector or front-end filter rejects strong out-of-band signals before overload. Capture effect is an FM receiver behavior. In an SDR, overload happens when the analog signal exceeds the ADC reference voltage range. A high intermediate frequency makes image rejection easier. On low HF, a little attenuation can improve strong-signal handling with little signal-to-noise penalty. A roofing filter improves blocking dynamic range. Blocking dynamic range is the difference from the noise floor to the 1 dB gain compression point. Desensitization means a strong nearby signal reduces receiver sensitivity. Intermodulation comes from nonlinearity. The trouble products are 2 times f1 minus f2, and 2 times f2 minus f1. Higher IP3 means better strong-signal handling. Common-mode current makes cables radiate or receive when they should not. The station surge protector belongs on the single-point ground panel.

### E5 Electrical Principles

Series resonance means minimum impedance and maximum current.

Parallel resonance means maximum impedance and minimum source current.

In series resonance, the voltage across the inductor or capacitor can be Q times the applied voltage.

At resonance, voltage and current are in phase.

One time constant equals 63.2 percent charge. Five time constants is approximately fully charged at 99.3 percent.

Admittance Y equals one divided by impedance Z. The parts of admittance are conductance G plus j times susceptance B.

Rectangular form for impedance is resistance plus j times reactance.

Polar form for impedance is the magnitude of Z at angle theta.

Positive reactance means inductive. Negative reactance means capacitive.

Skin effect pushes RF current toward the conductor surface as frequency rises.

At RF, keep lead lengths short to minimize inductance, coupling, and parasitics.

Self-resonance occurs when a component's intended reactance resonates with its parasitic opposite reactance.

Real power is dissipated in resistance. Inductors and capacitors only exchange reactive power.

### E6 Components

If you see donor impurity, think N-type material.

If you see acceptor impurity, think P-type material and holes.

If you see gallium arsenide, think high electron mobility and good performance at UHF and microwave.

If you see gallium nitride, think highest listed MMIC frequency capability.

If you see BJT beta, think change in collector current divided by change in base current.

If you see depletion-mode FET, think normally on at zero gate voltage.

If you see MOSFET gate protection, think Zener diodes for static protection.

If you see Zener diode, think nearly constant voltage reference.

If you see Schottky diode, think metal-semiconductor junction with low forward voltage drop and fast RF use.

If you see varactor, think voltage-controlled capacitance.

If you see PIN diode, think RF switch or attenuator where attenuation is set by forward DC bias.

If you see point-contact diode, think RF detector.

If you see CMOS, think lowest power with a threshold at about half the supply voltage.

If you see BiCMOS, think high input impedance combined with low output impedance.

If you see tri-state, think zero, one, or high impedance.

If you see ferrite core, think fewer turns needed for the same inductance.

If you see powdered iron core, think better temperature stability.

If you see brass slug, think it decreases inductance.

If you see toroid, think the magnetic field stays mostly inside the core.

If you see ferrite bead, think VHF and UHF parasitic suppressor.

If you see quartz crystal, think piezoelectric electromechanical resonator.

If you see microstrip, think PCB transmission line at RF and microwave frequencies.

If you see DIP package, think through-hole and bad at UHF and above because the leads are too long.

If you see photovoltaic, think light converted to electrical energy.

If you see photoconductive, think resistance decreases with light.

If you see optoisolator, think LED plus phototransistor providing electrical isolation.

## E7 through E8. Circuit Blocks, Modulation, and Digital Signal Traps

### E7 Practical Circuits

Digital and logic. A flip-flop is a bistable memory element that divides by 2. Four flip-flops divide by 16. A decade counter divides by 10. A monostable is a one-shot. An astable is an oscillator. An XNOR gate outputs high when the inputs are the same. In positive logic, high voltage equals 1.

Amplifier classes. Class A has a conduction angle of 360 degrees. It has the best linearity but the worst efficiency. Class B has a conduction angle of 180 degrees. It is efficient but has crossover distortion risk. Class AB has a conduction angle greater than 180 degrees and less than 360 degrees. It is the common linear compromise. Class C has a conduction angle less than 180 degrees. It is efficient and nonlinear. Do not use Class C for SSB. Class D uses switching. It is very efficient but needs output filtering.

Other amplifier anchors. A Class A amplifier Q-point sits near the midpoint between cutoff and saturation. An emitter follower, also called common collector, has output in phase with the input, low output impedance, and serves as a buffer. A grounded-grid amplifier has low input impedance. Bias divider means voltage-divider bias. An emitter resistor gives self-bias and stabilization. Parasitic oscillation cures include parasitic suppressors and neutralization.

Filters, matching, and power supplies. A low-pass pi network has a shunt capacitor, then a series inductor, then a shunt capacitor. A T network with series capacitors and a shunt inductor is a high-pass filter. A pi-L network adds an extra series output inductor for more harmonic suppression. Matching means cancel the reactance and transform the resistance. A Butterworth filter has a maximally flat passband. A Chebyshev filter has passband ripple but a sharper cutoff. An elliptical filter has the sharpest cutoff with both ripple and stopband notches. Shape factor describes how well the filter rejects adjacent channels. A linear regulator varies the conduction of a series pass element. A switching regulator varies the duty cycle into a filter. A three-terminal regulator is a series regulator. A Zener diode often serves as a stable reference. Step-start lets high-voltage capacitors charge gradually. Equalizing resistors across series capacitors equalize voltage, discharge caps, and provide a minimum load.

Modulation, SDR, op-amps, and oscillators. Baseband is the original message signal before modulation. A reactance modulator changes the effective capacitance in an oscillator to generate FM or PM. A frequency discriminator is an FM detector. A balanced modulator plus a filter generates SSB. An envelope detector is an AM detector. A product detector is an SSB detector. A mixer outputs the original signals plus their sum and difference. An overdriven mixer creates spurious products. A direct-sampling SDR digitizes RF straight into the ADC. FFT converts from the time domain to the frequency domain. Decimation lowers the sample rate. Use an anti-alias filter first. A Hilbert transform helps create a 90 degree phase relationship for DSP-based SSB. FIR filters can give linear phase. More taps means a sharper response. An op-amp has very high input impedance and very low output impedance. Adding a capacitor across the inverting feedback resistor gives a low-pass response. Too much gain and Q in active filters causes ringing or instability. Colpitts uses a capacitive divider. Hartley uses an inductive divider. Pierce uses a crystal feedback path. A phase-locked loop, or PLL, consists of a phase detector, a low-pass filter, and a voltage-controlled oscillator. A direct digital synthesizer, or DDS, consists of a phase accumulator, a lookup table, a digital-to-analog converter, and a low-pass filter. Its main impurity is discrete spurs. Oscillator frequency drift from vibration is called microphonics. NP0 or C0G capacitors reduce thermal drift in oscillators.

### E8 Signals and Emissions

Waveforms, power, and converters. Time domain shows amplitude versus time. Frequency domain shows amplitude versus frequency. A square wave contains the fundamental plus odd harmonics. True-RMS meters are needed for many non-sinusoidal signals. For unprocessed SSB speech, the ratio of PEP to average power is approximately 2.5 to 1. A SAR ADC uses a binary search style conversion. A flash ADC provides very high speed for direct conversion. Dither is small added noise that reduces quantization artifacts. A DAC output low-pass filter removes sampling images and artifacts.

Modulation, multiplexing, and coding. FM modulation index and deviation ratio look similar. Both involve deviation divided by a modulating or audio frequency. PM modulation index does not depend on carrier frequency. OFDM uses many orthogonal subcarriers. FDM uses different frequencies at the same time. TDM uses the same channel at different time slots. Baud is the symbol rate. QAM uses both amplitude and phase. A constellation diagram shows the allowed symbol states. More efficient coding can raise the data rate without increasing bandwidth. Change PSK phase at zero crossings to minimize bandwidth. PSK31 uses sinusoidal data pulses to stay narrow. ARQ handles errors by requesting retransmission. Gray code changes only one bit between adjacent values.

Clean-signal reminders. Abrupt CW rise and fall times cause key clicks. Fix key clicks by lengthening the rise and fall times. AFSK overmodulation usually comes from too much transmit audio. The digital cleanliness metric is IMD, or intermodulation distortion. An acceptable idling PSK IMD benchmark is negative 30 dB. Direct sequence spread spectrum uses a high-speed code to spread the waveform. Frequency hopping spread spectrum hops among frequencies in a pseudorandom pattern. Baudot uses 5-bit encoding with letters and figures shifts. ASCII uses a larger character set and supports upper and lower case.

## E9 Antennas and Transmission Lines

### Gain, Power, and Efficiency

dBi is referenced to an isotropic antenna. dBd is referenced to a dipole. Use dBd for ERP. Use dBi for EIRP. Antenna gain redistributes power. It does not increase total radiated power. Efficiency equals radiation resistance divided by the sum of radiation resistance plus loss resistance. Ground-mounted verticals perform better with better soil conductivity and more radials. Seawater is fantastic for low-angle vertically polarized radiation. Higher frequency means a smaller Fresnel zone.

### Pattern Reading and Modeling

An azimuth plot shows compass direction. An elevation plot shows takeoff angle. The 3 dB beamwidth is the half-power beamwidth. Front-to-back compares the forward lobe to the response directly behind. Front-to-side compares the forward lobe to the side response. The far field is the region where the pattern shape no longer changes with distance. Method of Moments is NEC-style wire segmentation with numerical current solving. Using fewer than about 10 segments per half wavelength can spoil impedance accuracy.

### Arrays, Wire Antennas, and Geometry Traps

Two verticals spaced one-half wavelength apart and fed in phase produce a broadside figure-eight pattern.

Two verticals spaced one-half wavelength apart and fed 180 degrees out of phase produce an end-fire figure-eight pattern.

Two verticals spaced one-quarter wavelength apart and fed 90 degrees out of phase produce a cardioid pattern.

More geometry anchors. A longer unterminated long wire has more lobes, and the strongest lobes move toward the wire axis. Adding a termination resistor to a long wire or rhombic makes it unidirectional. An OCFD feed offset is about multi-band impedance behavior. A folded dipole has an impedance of approximately 300 ohms. A G5RV uses a specific open-wire matching section. A Zepp is an end-fed half-wave antenna. An EDZ is a center-fed 1.25 wavelength dipole. Raising a horizontal antenna generally lowers the lowest takeoff angle. Over a long slope, the main lobe tends to tilt downhill.

### Directional Antennas and Short Antennas

For a fixed-size parabolic reflector, doubling the frequency adds 6 dB of gain. Crossed Yagis on the same axis, oriented 90 degrees apart and fed 90 degrees out of phase, produce circular polarization. A Yagi driven element is approximately one-half wavelength long. The reflector is slightly longer than resonance. The directors are slightly shorter. Short antennas are usually capacitive and need loading inductance. For a short whip, center loading is more efficient than base loading. A high-Q loading coil has lower loss but narrower bandwidth. Top loading improves short-vertical efficiency by reducing the required loading inductance and improving current distribution. As an antenna becomes electrically smaller, radiation resistance drops.

### Matching Systems

A gamma match is unbalanced. It is good with Yagis and grounded towers. A series capacitor cancels the inductive reactance.

A beta match, also called a hairpin match, is balanced. The driven element is insulated from the boom. An inductive hairpin cancels the capacitive feedpoint reactance.

A stub match uses a transmission-line section in parallel near the feedpoint.

A quarter-wave transformer uses a characteristic impedance equal to the square root of the product of the two impedances being matched.

A Wilkinson divider provides equal power split with correct input match and isolation.

### Transmission Line Behavior

Velocity factor equals line wave velocity divided by the speed of light. The dielectric material mainly sets the velocity factor. Open-wire or parallel line usually has lower loss than plastic-dielectric coax. Foam coax has higher velocity factor, lower loss, and lower breakdown voltage compared to solid dielectric coax. A half-wavelength line repeats the load impedance. A quarter-wavelength line inverts the impedance, so a short becomes an open and an open becomes a short. A shorted stub shorter than a quarter wavelength looks inductive. An open stub shorter than a quarter wavelength looks capacitive. Microstrip is a controlled-impedance PCB trace above a ground plane.

### Smith Chart Essentials

A Smith chart is a graphical transmission-line and impedance calculator. It is built from resistance circles and reactance arcs. The horizontal center line is the resistance axis. Above the axis is inductive. Below the axis is capacitive. The chart is normalized to the characteristic impedance. The center point is 1 plus j0, which represents a perfect match. Moving along a mismatched line follows a constant SWR circle. One full trip around the chart equals one-half wavelength of line.

### Receiving Antennas and Direction Finding

On 160 and 80 meter receive, directivity often matters more than efficiency. A Beverage antenna is long, low, terminated, and directional. It is usually at least one wavelength long. Proper Beverage termination shows up as minimum SWR variation across the desired range. RDF measures receive directivity performance. A small loop has deep nulls but a 180 degree ambiguity. An electrostatic shield preserves loop nulls by reducing E-field pickup. A sense antenna resolves the ambiguity by creating a cardioid pattern with a single null. A pennant or terminated loop also gives a cardioid receive pattern. More turns or more loop area means more loop output voltage.

## Easy Compare and Contrast

Do not confuse ERP with EIRP. ERP uses the dBd reference. EIRP uses the dBi reference.

Do not confuse telemetry with telecommand. Telemetry is status data. Telecommand is control commands.

Do not confuse ADIF with Cabrillo. ADIF is for general logs. Cabrillo is for contest submission.

Do not confuse an envelope detector, a discriminator, and a product detector. An envelope detector is for AM. A discriminator is for FM. A product detector is for SSB.

Do not confuse Butterworth, Chebyshev, and elliptical filters. Butterworth is flat. Chebyshev has ripple but is sharper. Elliptical is the sharpest with notches.

Do not confuse linear and switching regulators. A linear regulator varies conduction. A switching regulator varies duty cycle.

Do not confuse DSSS and FHSS. Direct sequence spreads by code. Frequency hopping spreads by hopping frequencies.

Do not confuse photovoltaic and photoconductive. Photovoltaic makes voltage and current. Photoconductive changes resistance.

Do not confuse S11 and S21. S11 is input reflection. S21 is forward transmission.

Do not confuse a quarter-wave line and a half-wave line. A quarter-wave inverts. A half-wave repeats.

Do not confuse open and shorted stubs under a quarter wavelength. An open stub is capacitive. A shorted stub is inductive.

Do not confuse dBi and dBd. dBi uses an isotropic reference. dBd uses a dipole reference.

Do not confuse Class AB and Class C. Class AB is a linear compromise. Class C is nonlinear with high efficiency.

Do not confuse Colpitts, Hartley, and Pierce oscillators. Colpitts uses a capacitive divider. Hartley uses an inductive divider. Pierce uses a crystal.

## Last Two-Minute Sweep

If you can say these out loud without hesitation, you are in good shape.

USB up, LSB down.

30 to 300 megahertz has the tightest maximum permissible exposure limits.

80 meters always needs an RF exposure evaluation.

Spread spectrum only above 222 megahertz.

2200 meters equals 1 watt EIRP. 630 meters equals 5 watts EIRP.

A rising A or K index means geomagnetic disturbance is increasing. Southward Bz is bad.

Oscilloscope shows time. Spectrum analyzer shows frequency.

S11 is reflection. S21 is forward gain.

Higher Q means narrower bandwidth.

Series resonance means minimum impedance. Parallel resonance means maximum impedance.

Negative 174 dBm per hertz is the thermal-noise anchor.

A flip-flop divides by 2.

Class C is not for SSB.

A linear regulator varies conduction. A switching regulator varies duty cycle.

Envelope detector for AM. Discriminator for FM. Product detector for SSB.

Nyquist says sample at least twice the highest frequency.

Baud equals symbol rate.

Smooth transitions keep signals narrow. Abrupt transitions cause splatter.

dBi equals dBd plus 2.15.

A half-wavelength repeats. A quarter-wavelength inverts.

Gamma, beta, stub, and quarter-wave transformer are matching tools.

Smith chart center equals a perfect match.

Beverage is long, low, terminated, and directional.

End of cram sheet. Good luck on the exam.
