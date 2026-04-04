# Amateur Extra Class Cram Sheet

_Final-pass review. Use this to cram, not to reread the whole course._

## Where the points are

If time is short, bias your final review toward the biggest buckets:

| Subelement | Questions on exam |
|---|---:|
| E7 Practical Circuits | 8 |
| E9 Antennas / Transmission Lines | 8 |
| E1 Rules | 6 |
| E6 Components | 6 |
| E2 Operating Procedures | 5 |
| E4 Amateur Practices | 5 |
| E5 Electrical Principles | 4 |
| E8 Signals / Emissions | 4 |
| E3 Propagation | 3 |
| E0 Safety | 1 |

---

## Must-know formulas and number anchors

### Core circuit math

| Know cold | Meaning / use |
|---|---|
| **X_L = 2πfL** | inductive reactance |
| **X_C = 1 / (2πfC)** | capacitive reactance |
| **f_r = 1 / (2π√LC)** | resonant frequency |
| **Q = f_r / BW** | resonant circuit quality factor |
| **BW = f_r / Q** | half-power bandwidth |
| **Q(series) = X / R** | series resonant circuit |
| **Q(parallel) = R / X** | parallel resonant circuit |
| **τ = RC** | RC time constant |
| **θ = arctan((X_L - X_C)/R)** | phase angle in series RLC |
| **P = I²R** | real power in resistance |
| **S = VI** | apparent power |
| **S² = P² + Q²** | apparent / real / reactive power triangle |
| **absorbed power = forward − reflected** | net power to load |

### RF / receiver math

| Know cold | Meaning / use |
|---|---|
| **dBi = dBd + 2.15 dB** | isotropic vs dipole reference |
| **P(dBW) = 10 log10(P watts)** | ERP / EIRP math |
| **dBm = dBW + 30** | common conversion |
| **Γ = (Z_L - Z_0)/(Z_L + Z_0)** | reflection coefficient |
| **SWR = (1 + \|Γ\|)/(1 - \|Γ\|)** | mismatch from reflection coefficient |
| **Z_transformer = √(Z_1 Z_2)** | quarter-wave transformer |
| **physical line length = electrical length × VF** | cut coax / stubs correctly |
| **far field ≈ 2D²/λ** | minimum distance for real pattern shape |
| **noise rise = 10 log10(BW ratio)** | receiver bandwidth noise increase |
| **thermal noise floor = -174 dBm/Hz** | ideal 1 Hz noise power at room temp |

### Digital / modulation math

| Know cold | Meaning / use |
|---|---|
| **ADC levels = 2^N** | N-bit converter resolution |
| **sample rate ≥ 2 × highest frequency** | Nyquist minimum |
| **FM modulation index β = deviation / modulating frequency** | wide vs narrow FM behavior |
| **deviation ratio = max deviation / highest audio frequency** | FM rule-of-thumb width |
| **inverting op-amp gain = -R_F / R_1** | E7G favorite |
| **linear regulator dissipation = (V_in - V_out) I_out** | heat in pass regulator |
| **battery time = Ah / average current** | run-time questions |
| **received level = TX power + gains - losses** | link budget in dB |

### “See this number, think this answer” list

- **30–300 MHz** = most restrictive RF exposure limits
- **80 meters** = RF exposure evaluation **always required**
- **5%** of MPE in an over-limit shared site = you share mitigation responsibility
- **2200 m = 1 W EIRP**, **630 m = 5 W EIRP**
- **60 m data max bandwidth = 2.8 kHz**
- **HF digital voice / SSTV = 3 kHz**
- **Remote-control link fails → max 3 minutes of transmission**
- **Below 30 MHz spurious = 43 dB below fundamental**
- **Folded dipole ≈ 300 Ω**
- **Solid PE coax VF ≈ 0.66**
- **FT8 ≈ 50 Hz wide**
- **13 WPM CW ≈ 52 Hz wide**
- **Dish gain +6 dB when frequency doubles** (same physical dish)
- **Silicon BJT V_BE on ≈ 0.6–0.7 V**
- **Silicon photovoltaic cell ≈ 0.5 V open-circuit**

---

## High-miss mnemonics / one-liners

- **USB goes up, LSB goes down** → watch band edges.
- **ELI the ICE man** → **E** leads **I** in **L**; **I** leads **E** in **C**.
- **Higher Q = narrower BW**.
- **Flip-flop halves frequency**.
- **Gamma = grounded / unbalanced vibe**; **Beta (hairpin) = balanced**.
- **λ/2 repeats, λ/4 flips**.
- **Shorted stub < λ/4 = inductive**; **open stub < λ/4 = capacitive**.
- **Gain concentrates power; it does not create power**.
- **Beverage = long, low, terminated, one-way**.
- **Colpitts = capacitors**, **Hartley = inductor tap**, **Pierce = crystal**.
- **Direct sequence = code the waveform**; **frequency hopping = move around the band**.
- **Bi / mono / astable** = 2 stable / 1 stable / 0 stable states.

---

## E0–E2: rules, safety, operating traps

### E0 Safety

- Ground rod / earth connection primary purpose: **lightning charge dissipation**.
- Neighbor’s property = **uncontrolled environment**.
- Most restrictive exposure range: **30–300 MHz**.
- **SAR** = rate body absorbs RF energy.
- Shared site rule: if your transmitter contributes **≥5%** of MPE in an over-limit area, you share responsibility.
- Microwave danger is **high field strength from high-gain antennas**, not ionizing radiation.
- **100% tie-off** = at least one lanyard attached at all times.
- Attach climbing lanyard to **tower legs**.
- Shock-absorbing lanyard anchor should be **above head level**.

### E1 Rules — the traps exam writers love

#### Band edges / special bands
- Entire **emission** must stay legal, not just the dial frequency.
- **USB near upper edge:** subtract bandwidth from upper band edge.
- **LSB near lower edge:** add bandwidth to lower band edge.
- **60 m CW** goes on **channel center frequency**.
- **60 m data max = 2.8 kHz**.
- **Spread spectrum only above 222 MHz**.
- **2200 m / 630 m** use **EIRP**, not just transmitter output.
- **630 m phone** is allowed across the entire 630 m band.

#### Special operating restrictions
- Ship / aircraft operation requires permission from **master / pilot in command**.
- Automatic control may pass **third-party traffic only for RTTY or data**.
- Lost remote-control link: transmission may continue **max 3 minutes**.
- Before **2200 m / 630 m** operation, notify **UTC** with call sign + antenna coordinates, then wait **30 days** unless told otherwise.

#### Exact rule items worth memorizing
- If within **1 mile of an FCC monitoring facility**, you must protect it.
- **PRB-1** applies to **state and local zoning** and requires **reasonable accommodation**.
- North of **Line A**, no **420–430 MHz** transmission.
- Below **30 MHz**, spurious output must be **43 dB below fundamental**.
- On **29 MHz and below**, max angle-modulation index at highest modulating frequency = **1.0**.

#### Satellites / message content / exceptions
- **Telemetry** = one-way measurements at a distance.
- **Telecommand** = send commands to control a device.
- Only narrow secrecy exception you should trust: **space telecommand may be encrypted**.
- Mesh networks still **may not obscure meaning**.
- Amateurs generally may not transmit for **pecuniary interest**.
- Forwarded bad traffic: primary responsibility is the **originating control operator**.

### E2 Operating procedures

#### Satellite / specialty mode anchors
- **Ascending pass** = satellite moves **south to north**.
- Satellite mode designator = **uplink/downlink band pair**, not FM/SSB style mode.
- Linear transponder = wideband “bent pipe”; many signals can share passband.
- **Inverting linear transponder:** USB up → LSB down, and vice versa.
- On linear satellites, too much uplink ERP reduces downlink power available to everyone.
- Satellite circular polarization helps with **Faraday rotation / spin fading**.
- **L band = 23 cm**, **S band = 13 cm**.

#### ATV / SSTV
- NTSC frame = **525 lines**.
- Interlace = **odd lines, then even lines**.
- Vestigial sideband = **one full sideband + part of the other**.
- SSTV: **brightness by tone frequency**, **color sent sequentially line-by-line**, **VIS code identifies mode**.

#### DX / logging / APRS / weak-signal digital
- Remote station in the U.S.: **no extra ID indicator required**.
- **Latency** = delay between control action and transmitter response.
- **ADIF** = general log exchange format.
- **Cabrillo** = contest log submission format.
- **LoTW** = contact confirmation system.
- Contesting is generally excluded from **30 meters**.
- In a DX pileup, send your **full call once or twice**.
- **APRS** rides on **AX.25** and usually uses a **UI frame**.
- **WIDE3-1** = three hops requested, one hop remaining.
- **MSK144** = meteor scatter.
- **Q65** = EME / moonbounce.
- **JT65** = very low SNR weak-signal mode.
- EME QSOs use **alternating synchronized transmit periods**.
- In VHF FT8/FT4 contest exchanges, the key item is the **grid square**.
- **WSPR** = propagation beaconing, not keyboard chat.
- **PSK31** = variable-length character coding.
- **PACTOR IV** = highest throughput of the common listed HF digital modes.
- **ALE** = radios scan a frequency list until the called station is heard.

---

## E3–E6: propagation, measurement, math, components

### E3 Propagation — anchor facts

- EM wave: **E and H fields are perpendicular to each other and to direction of travel**.
- EME likes **perigee**; fluttery EME fading = **libration fading**.
- MUF drops after dark → **move to a lower band**.
- Meteor scatter uses ionized trails in the **E region**.
- Tropospheric ducts often form over **large bodies of water**; think **100–300 miles**.
- Auroral propagation is tied to **severe geomagnetic storms** and favors **CW**.
- **TEP**: afternoon / early evening, roughly **2000–3000 miles**, path crosses geomagnetic equator.
- **160 m DX** likes a path in **darkness**.
- Long-path most common on **40 m and 20 m**.
- **Low takeoff angle = longer hops / DX**.
- Ground wave prefers **vertical polarization** and gets worse as frequency rises.
- **Sporadic-E** favors **solstice season** and **daytime**.
- **Chordal hop** = ionosphere-to-ionosphere hops without ground reflection.
- **X class** = strongest solar flare class.
- **G5** = extreme geomagnetic storm.
- Rising **A** or **K** index = increasing geomagnetic disturbance.
- **Southward Bz** = more likely geomagnetic trouble.
- Radio horizon is about **15% farther** than optical horizon.
- **VOACAP** = HF propagation prediction software.

### E4 Measurements / receiver behavior

#### Instruments
- Oscilloscope = **voltage vs time**.
- Spectrum analyzer = **amplitude vs frequency**.
- Scope probe compensation uses a **square wave**.
- Keep scope probe ground lead **short**.
- For linear-supply ripple, use **line trigger**.
- Frequency counter accuracy mostly depends on **time base accuracy**.
- Analog voltmeter sensitivity is in **ohms per volt**; low input resistance loads the circuit.

#### VNA / S-parameter basics
- **S11** = input reflection / return-loss behavior.
- **S21** = forward transmission / gain.
- VNA calibration standards: **open, short, 50 Ω load**.

#### Receiver / dynamic range anchors
- **Noise figure** = how much worse the receiver is than ideal thermal noise.
- **MDS** = minimum discernible signal.
- Widening bandwidth raises noise: use **10 log10(BW ratio)**.
- Excessive phase noise + strong nearby signal = **reciprocal mixing**.
- Preselector / front-end filter rejects strong out-of-band signals before overload.
- **Capture effect** is an FM receiver behavior.
- In an SDR, overload happens when the analog signal exceeds **ADC reference voltage range**.
- High IF makes **image rejection** easier.
- On low HF, a little **attenuation** can improve strong-signal handling with little SNR penalty.
- Roofing filter improves **blocking dynamic range**.
- **Blocking dynamic range**: difference from noise floor to 1 dB gain compression point.
- **Desensitization** = strong nearby signal reduces receiver sensitivity.
- Intermod comes from **nonlinearity**.
- Trouble products: **2f1 − f2** and **2f2 − f1**.
- **Higher IP3 = better strong-signal handling**.
- Common-mode current makes cables radiate or receive when they shouldn’t.
- Station surge protector belongs on the **single-point ground panel**.

### E5 Electrical principles — the fast version

- **Series resonance:** minimum impedance, maximum current.
- **Parallel resonance:** maximum impedance, minimum source current.
- In series resonance, voltage across L or C can be **Q × applied voltage**.
- At resonance, voltage and current are **in phase**.
- **1 time constant = 63.2% charge**, **5τ ≈ fully charged (99.3%)**.
- **Y = 1/Z**; admittance parts are **G + jB**.
- Rectangular form: **R + jX**.
- Polar form: **|Z|∠θ**.
- Positive reactance = **inductive**; negative reactance = **capacitive**.
- Skin effect pushes RF current toward the conductor **surface** as frequency rises.
- At RF, keep lead lengths short to minimize **inductance, coupling, parasitics**.
- Self-resonance = component’s intended reactance resonates with its **parasitic opposite reactance**.
- Real power is dissipated in **R**; inductors/capacitors only exchange **reactive power**.

### E6 Components — compare/contrast

| If you see… | Think… |
|---|---|
| **donor impurity** | makes **N-type** material |
| **acceptor impurity** | makes **P-type** material / holes |
| **GaAs** | high electron mobility, good at UHF/microwave |
| **GaN** | highest listed MMIC frequency capability |
| **BJT beta** | Δcollector current / Δbase current |
| **depletion-mode FET** | normally on at V_G = 0 |
| **MOSFET gate protection** | Zener diodes for static protection |
| **Zener diode** | nearly constant voltage reference |
| **Schottky** | metal-semiconductor, low forward drop, fast RF use |
| **varactor** | voltage-controlled capacitance |
| **PIN diode** | RF switch / attenuator; attenuation set by forward DC bias |
| **point-contact diode** | RF detector |
| **CMOS** | lowest power; threshold ~ half supply |
| **BiCMOS** | high input impedance + low output impedance |
| **tri-state** | 0 / 1 / high impedance |
| **ferrite** | fewer turns for same inductance |
| **powdered iron** | better temperature stability |
| **brass slug** | decreases inductance |
| **toroid** | magnetic field stays mostly inside core |
| **ferrite bead** | VHF/UHF parasitic suppressor |
| **quartz crystal** | piezoelectric electromechanical resonator |
| **microstrip** | PCB transmission line at RF/microwave |
| **DIP package** | through-hole; bad at UHF+ because leads are too long |
| **photovoltaic** | light → electrical energy |
| **photoconductive** | resistance decreases with light |
| **optoisolator** | LED + phototransistor; electrical isolation |

---

## E7–E8: circuit blocks, modulation, digital signal traps

### E7 Practical circuits — what to recognize instantly

#### Digital / logic
- **Flip-flop** = bistable memory element; divide-by-2.
- **4 flip-flops** = divide by **16**.
- **Decade counter** = divide by **10**.
- **Monostable** = one-shot.
- **Astable** = oscillator.
- **XNOR** = output high when inputs are the **same**.
- Positive logic: **high voltage = 1**.

#### Amplifier classes

| Class | Conduction angle | Why you care |
|---|---:|---|
| **A** | 360° | best linearity, worst efficiency |
| **B** | 180° | efficient, crossover distortion risk |
| **AB** | >180° and <360° | common linear compromise |
| **C** | <180° | efficient, nonlinear, **not for SSB** |
| **D** | switching | very efficient, needs output filtering |

Other amplifier anchors:
- Class A Q-point sits near midpoint between **cutoff and saturation**.
- **Emitter follower / common collector**: output **in phase**, low Zout, buffer role.
- **Grounded-grid** amplifier: **low input impedance**.
- Bias divider = **voltage-divider bias**; emitter resistor gives **self-bias / stabilization**.
- Parasitic oscillation cures: **parasitic suppressors** and **neutralization**.

#### Filters / matching / power supplies
- Low-pass **Pi network** = **shunt C, series L, shunt C**.
- T with **series capacitors + shunt inductor** = **high-pass**.
- **Pi-L** = extra series output inductor for **more harmonic suppression**.
- Matching means **cancel reactance + transform resistance**.
- **Butterworth** = maximally flat passband.
- **Chebyshev** = passband ripple, sharper cutoff.
- **Elliptical** = sharpest cutoff, ripple + stopband notches.
- **Shape factor** = how well the filter rejects adjacent channels.
- Linear regulator varies conduction of a **series pass element**.
- Switching regulator varies **duty cycle** into a filter.
- **Three-terminal regulator** = series regulator.
- **Zener** often serves as stable reference.
- Step-start lets HV capacitors charge **gradually**.
- Equalizing resistors across series capacitors: equalize voltage, discharge caps, provide minimum load.

#### Modulation / SDR / op-amp / oscillators
- **Baseband** = original message signal before modulation.
- **Reactance modulator** changes effective **capacitance** in oscillator → FM/PM generation.
- **Frequency discriminator** = FM detector.
- **Balanced modulator + filter** = SSB generation.
- **Envelope detector** = AM detector.
- **Product detector** = SSB detector.
- Mixer outputs include originals plus **sum and difference**.
- Overdriven mixer creates **spurious products**.
- **Direct-sampling SDR** digitizes RF straight into ADC.
- **FFT** = time domain → frequency domain.
- **Decimation** lowers sample rate; use **anti-alias filter** first.
- **Hilbert transform** helps create 90° phase relation for DSP SSB.
- **FIR** filters can give **linear phase**; more taps = sharper response.
- Op-amp: **very high Zin, very low Zout**.
- Add capacitor across inverting feedback resistor → **low-pass** response.
- Too much gain and Q in active filters → **ringing / instability**.
- **Colpitts = capacitive divider**.
- **Hartley = inductive divider**.
- **Pierce = crystal feedback path**.
- **PLL = phase detector + low-pass filter + VCO**.
- **DDS = phase accumulator + lookup table + DAC + low-pass filter**; main impurity is discrete **spurs**.
- Oscillator frequency drift from vibration = **microphonics**.
- **NP0/C0G** caps reduce thermal drift in oscillators.

### E8 Signals / emissions — what people mix up

#### Waveform / power / converters
- Time domain = **amplitude vs time**.
- Frequency domain = **amplitude vs frequency**.
- Square wave = **fundamental + odd harmonics**.
- **True-RMS** meters are needed for many **non-sinusoidal** signals.
- Unprocessed SSB speech: **PEP : average ≈ 2.5 : 1**.
- **SAR ADC** = binary search style conversion.
- **Flash ADC** = very high speed for direct conversion.
- **Dither** = small added noise to reduce quantization artifacts.
- DAC output low-pass filter removes **sampling images / artifacts**.

#### Modulation / multiplexing / coding
- **FM modulation index** and **deviation ratio** look similar; both are deviation divided by modulating/audio frequency.
- **PM modulation index does NOT depend on carrier frequency**.
- **OFDM** = many orthogonal subcarriers.
- **FDM** = different frequencies at the same time.
- **TDM** = same channel, different time slots.
- **Baud = symbol rate**.
- **QAM** uses amplitude + phase; constellation shows allowed symbol states.
- More efficient coding can raise data rate **without increasing bandwidth**.
- Change PSK phase at **zero crossings** to minimize bandwidth.
- **PSK31** uses sinusoidal data pulses to stay narrow.
- **ARQ** handles errors by **requesting retransmission**.
- **Gray code** changes only **one bit** between adjacent values.

#### Clean-signal reminders
- Abrupt CW rise/fall times cause **key clicks**.
- Fix key clicks by **lengthening rise and fall times**.
- AFSK overmodulation usually comes from **too much transmit audio**.
- Digital cleanliness metric: **IMD**.
- Acceptable idling PSK IMD benchmark: **-30 dB**.
- **DSSS** uses high-speed code to spread the waveform.
- **FHSS** hops among frequencies in a pseudorandom pattern.
- **Baudot** = 5-bit, letters/figures shifts.
- **ASCII** = larger set, supports upper and lower case.

---

## E9 Antennas / transmission lines — highest-yield final pass

### Gain / power / efficiency
- **dBi** is referenced to isotropic; **dBd** is referenced to a dipole.
- Use **dBd for ERP**, **dBi for EIRP**.
- Antenna gain **redistributes** power; it does not increase total radiated power.
- **Efficiency = radiation resistance / (radiation resistance + loss resistance)**.
- Ground-mounted verticals get better with better **soil conductivity** and **more radials**.
- **Seawater** is fantastic for low-angle vertically polarized radiation.
- Higher frequency → **smaller Fresnel zone**.

### Pattern reading / modeling
- **Azimuth** plot = compass direction.
- **Elevation** plot = takeoff angle.
- **3 dB beamwidth** = **half-power beamwidth**.
- **Front-to-back** compares forward lobe to directly behind.
- **Front-to-side** compares forward lobe to side response.
- Far field = region where pattern shape no longer changes with distance.
- **Method of Moments** = NEC-style wire segmentation / numerical current solving.
- Too few segments (< about **10 per half-wave**) can spoil impedance accuracy.

### Arrays / wire antennas / geometry traps

| Setup | Pattern |
|---|---|
| 2 verticals, **1/2 λ apart, in phase** | **broadside figure-eight** |
| 2 verticals, **1/2 λ apart, 180° out of phase** | **end-fire figure-eight** |
| 2 verticals, **1/4 λ apart, 90° out of phase** | **cardioid** |

More geometry anchors:
- Longer **unterminated** long wire → more lobes, strongest lobes move toward wire axis.
- Termination resistor on long wire / rhombic makes it **unidirectional**.
- **OCFD** feed offset is about multi-band **impedance behavior**.
- **Folded dipole ≈ 300 Ω**.
- **G5RV** uses a **specific open-wire matching section**.
- **Zepp** = **end-fed half-wave**.
- **EDZ** = **center-fed 1.25 λ dipole**.
- Raising a horizontal antenna generally **lowers the lowest takeoff angle**.
- Over a long slope, the main lobe tends to tilt **downhill**.

### Directional antennas / short antennas
- Fixed-size parabolic reflector: **frequency doubles → gain +6 dB**.
- Crossed Yagis on same axis, 90° apart in orientation and feed phase → **circular polarization**.
- Yagi driven element ≈ **1/2 λ**.
- **Reflector** is slightly **longer** than resonance; **directors** are slightly **shorter**.
- Short antennas are usually **capacitive** and need loading inductance.
- For a short whip, **center loading** is more efficient than base loading.
- High-Q loading coil = **lower loss** but **narrower bandwidth**.
- **Top loading** improves short-vertical efficiency by reducing required loading inductance and improving current distribution.
- As an antenna becomes electrically smaller, **radiation resistance drops**.

### Matching systems

| Match type | Key fact |
|---|---|
| **Gamma match** | unbalanced; good with Yagis / grounded towers; series capacitor cancels inductive reactance |
| **Beta / hairpin** | balanced; driven element insulated from boom; uses inductive hairpin to cancel capacitive feedpoint reactance |
| **Stub match** | transmission-line section in parallel near feedpoint |
| **Quarter-wave transformer** | use **√(Z1·Z2)** characteristic impedance |
| **Wilkinson divider** | equal power split with correct input match and isolation |

### Transmission line behavior
- **Velocity factor = line wave velocity / speed of light**.
- Dielectric material mainly sets VF.
- **Open-wire / parallel line** usually has lower loss than plastic-dielectric coax.
- **Foam coax**: higher VF, lower loss, lower breakdown voltage than solid dielectric coax.
- **λ/2 line repeats the load**.
- **λ/4 line inverts impedance**: short ↔ open.
- **Shorted stub shorter than λ/4** looks **inductive**.
- **Open stub shorter than λ/4** looks **capacitive**.
- **Microstrip** = controlled-impedance PCB trace above a ground plane.

### Smith chart essentials
- It is a **graphical transmission-line / impedance calculator**.
- Built from **resistance circles** and **reactance arcs**.
- Horizontal center line = **resistance axis**.
- Above axis = **inductive**, below = **capacitive**.
- Chart is **normalized to Z0**.
- Center = **1 + j0** = perfect match.
- Moving along a mismatched line follows a **constant-SWR circle**.
- One full trip around the chart = **1/2 wavelength of line**.

### Receiving antennas / DF
- On **160/80 m receive**, **directivity** often matters more than efficiency.
- **Beverage** = long, low, terminated, directional; usually at least **1 wavelength** long.
- Proper Beverage termination shows up as **minimum SWR variation across the desired range**.
- **RDF** measures receive directivity performance.
- Small loop has deep nulls but a **180° ambiguity**.
- Electrostatic shield preserves loop nulls by reducing **E-field pickup**.
- **Sense antenna** resolves the ambiguity by creating a **cardioid** pattern with a **single null**.
- **Pennant / terminated loop** also gives a cardioid receive pattern.
- More turns or more loop area = more loop output voltage.

---

## Easy compare/contrast table

| Don’t confuse | Correct distinction |
|---|---|
| **ERP vs EIRP** | ERP uses **dBd** reference; EIRP uses **dBi** reference |
| **Telemetry vs telecommand** | telemetry = status data; telecommand = control commands |
| **ADIF vs Cabrillo** | ADIF = general logs; Cabrillo = contest submission |
| **Envelope detector vs discriminator vs product detector** | AM / FM / SSB respectively |
| **Butterworth vs Chebyshev vs Elliptical** | flat / ripple+sharper / sharpest+notches |
| **Linear vs switching regulator** | vary conduction / vary duty cycle |
| **DSSS vs FHSS** | spread by code / spread by hopping frequencies |
| **Photovoltaic vs photoconductive** | makes voltage/current / changes resistance |
| **S11 vs S21** | input reflection / forward transmission |
| **Quarter-wave vs half-wave line** | inverts / repeats |
| **Open vs short stub under λ/4** | capacitive / inductive |
| **dBi vs dBd** | isotropic / dipole reference |
| **Class AB vs Class C** | linear compromise / nonlinear high efficiency |
| **Colpitts vs Hartley vs Pierce** | capacitive divider / inductive divider / crystal |

---

## Last 2-minute sweep

If you can say these out loud without hesitation, you are in good shape:

- USB up, LSB down.
- 30–300 MHz has the tightest MPE limits.
- 80 m always needs RF exposure evaluation.
- Spread spectrum only above 222 MHz.
- 2200 m = 1 W EIRP, 630 m = 5 W EIRP.
- A/K up means geomagnetic disturbance up; southward Bz is bad.
- Scope = time, spectrum analyzer = frequency.
- S11 reflection, S21 forward gain.
- Higher Q means narrower bandwidth.
- Series resonance = minimum Z; parallel resonance = maximum Z.
- -174 dBm/Hz is the thermal-noise anchor.
- Flip-flop divides by 2.
- Class C is not for SSB.
- Linear regulator varies conduction; switcher varies duty cycle.
- Envelope detector = AM, discriminator = FM, product detector = SSB.
- Nyquist: sample at least twice the highest frequency.
- Baud = symbol rate.
- Smooth transitions keep signals narrow; abrupt transitions splatter.
- dBi = dBd + 2.15.
- λ/2 repeats, λ/4 flips.
- Gamma / beta / stub / quarter-wave transformer are matching tools.
- Smith chart center = perfect match.
- Beverage = long, low, terminated, directional.

---

_This sheet is intentionally compressed. If you miss a topic here, go back to that subelement’s full guide for the long-form explanation._
