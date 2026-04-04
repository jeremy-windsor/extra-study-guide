# E9 — Antennas and Transmission Lines
*8 questions on the exam from a pool of 93*

## Group E9A — Antenna fundamentals: types of antennas; antenna gain; radiation patterns; polarization; efficiency; ground effects

### E9A01
**What is an isotropic radiator?**
- A) A calibrated, unidirectional antenna used to make precise antenna gain measurements
- B) An omnidirectional, horizontally polarized, precisely calibrated antenna used to make field
- **C) A hypothetical, lossless antenna having equal radiation intensity in all directions used as a reference** ✅
- D) A spacecraft antenna used to direct signals toward Earth

> An isotropic radiator is a hypothetical, lossless antenna that radiates equally in all directions — a perfect sphere of radiation. It doesn't physically exist but serves as a mathematical reference (0 dBi) for expressing antenna gain. All real antennas have directional patterns. The isotropic radiator is purely a theoretical construct used in antenna engineering calculations.

### E9A02
**What is the effective radiated power (ERP) of a repeater station with 150 watts transmitter power output, 2 dB feed line loss, 2.2 dB duplexer loss, and 7 dBd antenna gain?**
- A) 469 watts
- B) 78.7 watts
- C) 420 watts
- **D) 286 watts** ✅

> ERP = transmitter power - feed line loss - duplexer loss + antenna gain (over dipole). P_tx = 150W = 10log(150) = 21.76 dBW. Feed line loss = -2 dB. Duplexer loss = -2.2 dB. Antenna gain = +7 dBd. ERP (dBW) = 21.76 - 2 - 2.2 + 7 = 24.56 dBW. Convert: 10^(24.56/10) ≈ 286 watts. ERP is referenced to a dipole, so we use dBd for antenna gain.

### E9A03
**What term describing total radiated power takes into account all gains and losses?**
- A) Power factor
- B) Half-power bandwidth
- **C) Effective radiated power** ✅
- D) Apparent power

> Effective radiated power (ERP) takes into account ALL gains and losses in the system: transmitter power, feed line losses, connector losses, duplexer/filter losses, and antenna gain. It represents the total power that would need to be fed to a reference antenna (dipole for ERP, isotropic for EIRP) to produce the same field strength in the direction of maximum radiation.

### E9A04
**Which of the following factors affect the feed point impedance of an antenna?**
- A) Transmission line length
- **B) Antenna height** ✅
- C) The settings of an antenna tuner at the transmitter
- D) The input power level

> Antenna height affects feed point impedance because the ground acts as a reflector. At different heights, the reflected wave arrives at the feed point with varying phase relationships, changing the impedance. A dipole at 1/2 wavelength height has about 72 ohms; at other heights, the impedance varies considerably. Transmission line length, tuner settings, and input power do NOT directly affect the antenna's feed point impedance.

### E9A05
**What does the term “ground gain” mean?**
- A) The change in signal strength caused by grounding the antenna
- B) The gain of the antenna with respect to a dipole at ground level
- C) To force net gain to 0 dB by grounding part of the antenna
- **D) An increase in signal strength from ground reflections in the environment of the antenna** ✅

> Ground gain is an increase in signal strength from ground reflections in the environment of the antenna. The ground acts as a reflector, and at certain elevation angles the direct and reflected waves add constructively, increasing the effective radiated signal in that direction. Ground gain can add 3-6 dB over some elevation angles. It's why antenna height matters — different heights produce different ground reflection patterns.

### E9A06
**What is the effective radiated power (ERP) of a repeater station with 200 watts transmitter power output, 4 dB feed line loss, 3.2 dB duplexer loss, 0.8 dB circulator loss, and 10 dBd antenna gain?**
- **A) 317 watts** ✅
- B) 2,000 watts
- C) 126 watts
- D) 300 watts

> ERP = P_tx - feed loss - duplexer loss - circulator loss + antenna gain (dBd). P_tx = 200W = 23.01 dBW. Feed line = -4 dB. Duplexer = -3.2 dB. Circulator = -0.8 dB. Antenna = +10 dBd. ERP(dBW) = 23.01 - 4 - 3.2 - 0.8 + 10 = 25.01 dBW. Convert: 10^(25.01/10) ≈ 317 watts. This is a straight gain-and-loss calculation in dB.

### E9A07
**What is the effective isotropic radiated power (EIRP) of a repeater station with 200 watts transmitter power output, 2 dB feed line loss, 2.8 dB duplexer loss, 1.2 dB circulator loss, and 7 dBi antenna gain?**
- A) 159 watts
- **B) 252 watts** ✅
- C) 632 watts
- D) 63.2 watts

> EIRP = P_tx - feed loss - duplexer loss - circulator loss + antenna gain (dBi). P_tx = 200W = 23.01 dBW. Feed = -2 dB. Duplexer = -2.8 dB. Circulator = -1.2 dB. Antenna = +7 dBi. EIRP(dBW) = 23.01 - 2 - 2.8 - 1.2 + 7 = 24.01 dBW. Convert: 10^(24.01/10) ≈ 252 watts. EIRP uses dBi (referenced to isotropic), while ERP uses dBd (referenced to dipole). dBi = dBd + 2.15.

### E9A08
**Which frequency band has the smallest first Fresnel zone?**
- **A) 5.8 GHz** ✅
- B) 3.4 GHz
- C) 2.4 GHz
- D) 900 MHz

> The first Fresnel zone radius is proportional to √(wavelength × distance). Higher frequencies have shorter wavelengths, so they have smaller Fresnel zones. 5.8 GHz has the shortest wavelength of the choices, so it has the smallest Fresnel zone. Fresnel zones matter for microwave point-to-point links — obstructions within the first Fresnel zone cause signal loss.

### E9A09
**What is antenna efficiency?**
- A) Radiation resistance divided by transmission resistance
- **B) Radiation resistance divided by total resistance** ✅
- C) Total resistance divided by radiation resistance
- D) Effective radiated power divided by transmitter output

> Antenna efficiency = radiation resistance / total resistance. Total resistance = radiation resistance + loss resistance (conductor losses, ground losses, loading coil losses). An antenna with R_rad = 36 ohms and R_loss = 4 ohms has efficiency = 36/40 = 90%. The remaining 10% is dissipated as heat. Electrically short antennas have low R_rad and can have very poor efficiency.

### E9A10
**Which of the following improves the efficiency of a ground-mounted quarter-wave vertical antenna?**
- **A) Installing a ground radial system** ✅
- B) Isolating the coax shield from ground
- C) Shortening the radiating element
- D) All these choices are correct

> Installing a ground radial system improves the efficiency of a ground-mounted quarter-wave vertical by reducing ground loss resistance. Without radials, RF currents must flow through lossy soil, creating significant I²R losses. Radials provide a low-resistance return path near the surface. More radials = lower ground loss. A 1/4-wave vertical with 120 radials approaches 90%+ efficiency; with 4 radials, efficiency might be only 30-50%.

### E9A11
**Which of the following determines ground losses for a ground-mounted vertical antenna operating on HF?**
- A) The standing wave ratio
- B) Distance from the transmitter
- **C) Soil conductivity** ✅
- D) Take-off angle

> Soil conductivity is the primary factor determining ground losses for a ground-mounted vertical antenna. High-conductivity soil (salt marsh, wet clay) produces lower losses; poor soil (rocky, sandy, dry) produces higher losses. Ground loss directly reduces antenna efficiency by adding loss resistance to the total resistance. This is why coastal stations often have stronger signals from vertical antennas.

### E9A12
**How much gain does an antenna have compared to a half-wavelength dipole if it has 6 dB gain over an isotropic radiator?**
- **A) 3.85 dB** ✅
- B) 6.0 dB
- C) 8.15 dB
- D) 2.79 dB

> An isotropic radiator is 2.15 dB below a dipole. So 6 dBi = 6 - 2.15 = 3.85 dBd. The antenna has 3.85 dB gain compared to a half-wavelength dipole. This conversion is essential: dBi (over isotropic) = dBd (over dipole) + 2.15. Always check whether gain is specified in dBi or dBd when comparing antennas.

## Group E9B — Antenna patterns: pattern measurements; far-field; antenna testing; phased arrays; antenna modeling

### E9B01
**What is the 3 dB beamwidth of the antenna radiation pattern shown in Figure E9-1?**
- A) 75 degrees
- **B) 50 degrees** ✅
- C) 25 degrees
- D) 30 degrees

> The 3 dB beamwidth is the angular width between the half-power (-3 dB) points on either side of the main lobe. Reading the radiation pattern in Figure E9-1, the main lobe extends approximately 25° on each side of the peak before dropping 3 dB, giving a total 3 dB beamwidth of about 50 degrees. Narrower beamwidth indicates higher directivity and gain.

### E9B02
**What is the front-to-back ratio of the antenna radiation pattern shown in Figure E9-1?**
- A) 36 dB
- B) 14 dB
- C) 24 dB
- **D) 18 dB** ✅

> Front-to-back ratio is the difference in dB between the forward lobe maximum and the response directly behind the antenna (180°). Reading Figure E9-1, the main lobe peak minus the back lobe level = approximately 18 dB. Higher F/B ratio means better rejection of signals from behind the antenna — important for reducing QRM and interference.

### E9B03
**What is the front-to-side ratio of the antenna radiation pattern shown in Figure E9-1?**
- A) 12 dB
- B) 24 dB
- C) 18 dB
- **D) 14 dB** ✅

> Front-to-side ratio is the difference in dB between the forward lobe maximum and the response at 90° to the side. From Figure E9-1, this is approximately 14 dB. Front-to-side ratio is important for rejecting signals from the sides, such as in a crowded band where strong stations are off to the side of your bearing.

### E9B04
**What is the front-to-back ratio of the radiation pattern shown in Figure E9-2?**
- A) 15 dB
- **B) 28 dB** ✅
- C) 3 dB
- D) 38 dB

> Reading the radiation pattern in Figure E9-2 (an elevation pattern), the front-to-back ratio is approximately 28 dB. This is the difference between the maximum forward lobe and the signal level in the reverse direction (180°).

### E9B05
**What type of antenna pattern is shown in Figure E9-2?**
- **A) Elevation** ✅
- B) Azimuth
- C) Near field
- D) Polarization

> Figure E9-2 shows an elevation pattern — it shows the antenna's radiation as a function of vertical angle (elevation) above the horizon. An azimuth pattern would show radiation as a function of horizontal direction (compass bearing). Elevation patterns are important for understanding the antenna's ability to communicate at different distances (low angles = DX, high angles = NVIS/local).

### E9B06
**What is the elevation angle of peak response in the antenna radiation pattern shown in Figure E9-2?**
- A) 45 degrees
- B) 75 degrees
- **C) 7.5 degrees** ✅
- D) 25 degrees

> Reading the elevation pattern in Figure E9-2, the peak response occurs at approximately 7.5 degrees above the horizon. This low elevation angle is ideal for DX communication on HF, where ionospheric skip requires low takeoff angles to reach distant stations. Higher elevation peaks would favor shorter-distance communication.

### E9B07
**What is the difference in radiated power between a lossless antenna with gain and an isotropic radiator driven by the same power?**
- A) The power radiated from the directional antenna is increased by the gain of the antenna
- B) The power radiated from the directional antenna is stronger by its front-to-back ratio
- **C) They are the same** ✅
- D) The power radiated from the isotropic radiator is 2.15 dB greater than that from the directional

> A lossless directional antenna and an isotropic radiator, driven by the same power, radiate the SAME total power. The directional antenna doesn't create power — it concentrates it in certain directions at the expense of others. Gain means power is redirected, not amplified. Total radiated power is identical; the directional antenna just puts more of it where you want it.

### E9B08
**What is the far field of an antenna?**
- A) The region of the ionosphere where radiated power is not refracted
- B) The region where radiated power dissipates over a specified time period
- C) The region where radiated field strengths are constant
- **D) The region where the shape of the radiation pattern no longer varies with distance** ✅

> The far field of an antenna is the region where the radiation pattern shape no longer changes with distance. In the far field, the electric and magnetic fields are perpendicular to each other and to the direction of propagation, and they decrease as 1/r. The far field begins at approximately 2D²/λ, where D is the largest antenna dimension. Pattern measurements must be made in the far field.

### E9B09
**What type of analysis is commonly used for modeling antennas?**
- A) Graphical analysis
- **B) Method of Moments** ✅
- C) Mutual impedance analysis
- D) Calculus differentiation with respect to physical properties

> Method of Moments (MoM) is the most common numerical analysis technique for modeling antennas. It divides the antenna wire into small segments, calculates the current on each segment considering mutual coupling with all other segments, and computes the resulting radiation pattern and impedance. NEC (Numerical Electromagnetics Code) is the most widely used MoM software for amateur radio antenna modeling.

### E9B10
**What is the principle of a Method of Moments analysis?**
- **A) A wire is modeled as a series of segments, each having a uniform value of current** ✅
- B) A wire is modeled as a single sine-wave current generator
- C) A wire is modeled as a single sine-wave voltage source
- D) A wire is modeled as a series of segments, each having a distinct value of voltage across it

> In Method of Moments analysis, a wire antenna is modeled as a series of short segments, each having a uniform value of current. The boundary conditions are applied to find the current distribution that satisfies Maxwell's equations. The assumption of piecewise-constant (or piecewise-sinusoidal) current on each segment makes the integral equations solvable numerically.

### E9B11
**What is a disadvantage of decreasing the number of wire segments in an antenna model below 10 segments per half-wavelength?**
- A) Ground conductivity will not be accurately modeled
- B) The resulting design will favor radiation of harmonic energy
- **C) The computed feed point impedance may be incorrect** ✅
- D) The antenna will become mechanically unstable

> Using fewer than 10 segments per half-wavelength reduces the accuracy of the model, potentially making the computed feed point impedance incorrect. With too few segments, the current distribution is poorly approximated, and the boundary conditions are not satisfied accurately. The rule of thumb is at least 10 segments per half-wavelength (some models recommend 20) for reliable results.

## Group E9C — Wire and phased vertical antennas: beverage antennas; terminated antennas; rhombic antennas; NVIS antennas; phased arrays

### E9C01
**What type of radiation pattern is created by two 1/4-wavelength vertical antennas spaced 1/2- wavelength apart and fed 180 degrees out of phase?**
- A) Cardioid
- B) Omni-directional
- C) A figure-eight broadside to the axis of the array
- **D) A figure-eight oriented along the axis of the array** ✅

> Two 1/4-wave verticals spaced 1/2 wavelength apart and fed 180° out of phase create a figure-eight pattern oriented ALONG the axis of the array (end-fire). The 180° phase difference plus the 180° path-length difference (from 1/2λ spacing) causes constructive interference along the axis connecting the antennas and cancellation broadside to the array.

### E9C02
**What type of radiation pattern is created by two 1/4-wavelength vertical antennas spaced 1/4- wavelength apart and fed 90 degrees out of phase?**
- **A) Cardioid** ✅
- B) A figure-eight end-fire along the axis of the array
- C) A figure-eight broadside to the axis of the array
- D) Omni-directional

> Two 1/4-wave verticals spaced 1/4 wavelength apart and fed 90° out of phase create a cardioid (heart-shaped) pattern. The 90° phase offset plus the 90° path-length difference (from 1/4λ spacing) causes complete cancellation in one direction and reinforcement in the other. This is the classic directional pattern used in AM broadcast stations for directional coverage.

### E9C03
**What type of radiation pattern is created by two 1/4-wavelength vertical antennas spaced 1/2- wavelength apart and fed in phase?**
- A) Omni-directional
- B) Cardioid
- **C) A figure-eight broadside to the axis of the array** ✅
- D) A figure-eight end-fire along the axis of the array

> Two 1/4-wave verticals spaced 1/2 wavelength apart and fed in phase (0° phase difference) create a figure-eight pattern broadside to the axis of the array. The signals add constructively perpendicular to the line connecting the antennas (where path lengths are equal) and cancel along the axis (where the 1/2λ spacing creates destructive interference).

### E9C04
**What happens to the radiation pattern of an unterminated long wire antenna as the wire length is increased?**
- A) Fewer lobes form with the major lobes increasing closer to broadside to the wire
- **B) Additional lobes form with major lobes increasingly aligned with the axis of the antenna** ✅
- C) The elevation angle increases, and the front-to-rear ratio decreases
- D) The elevation angle increases, while the front-to-rear ratio is unaffected

> As an unterminated long wire antenna gets longer, additional lobes form and the major lobes become increasingly aligned with the wire axis. The number of lobes equals roughly the length in wavelengths. A 1λ wire has 4 lobes; a 4λ wire has 8 lobes. The main lobes get closer to the wire direction. This is why Beverage antennas (long, low wires) are directive along their length.

### E9C05
**What is the purpose of feeding an off-center-fed dipole (OCFD) between the center and one end instead of at the midpoint?**
- **A) To create a similar feed point impedance on multiple bands** ✅
- B) To suppress off-center lobes at higher frequencies
- C) To resonate the antenna across a wider range of frequencies
- D) To reduce common-mode current coupling on the feed line shield

> An off-center-fed dipole (OCFD) is fed at a point other than the center to create a similar feed point impedance on multiple bands. At the standard 1/3 offset point, the impedance is approximately 200-300 ohms on multiple harmonic frequencies, making it possible to use a single balun/matching device for multi-band operation. A center-fed dipole's impedance varies wildly on non-fundamental frequencies.

### E9C06
**What is the effect of adding a terminating resistor to a rhombic or long-wire antenna?**
- A) It reflects the standing waves on the antenna elements back to the transmitter
- **B) It changes the radiation pattern from bidirectional to unidirectional** ✅
- C) It changes the radiation pattern from horizontal to vertical polarization
- D) It decreases the ground loss

> Adding a terminating resistor to a rhombic or long-wire antenna absorbs energy traveling toward the far end, changing the pattern from bidirectional to unidirectional. Without the termination, waves reflect from the open end and radiate in both directions. The resistor absorbs the backward wave (wasting some power as heat) but eliminates the rear lobe, creating a clean forward pattern.

### E9C07
**What is the approximate feed point impedance at the center of a two-wire half-wave folded dipole antenna?**
- **A) 300 ohms** ✅
- B) 72 ohms
- C) 50 ohms
- D) 450 ohms

> A half-wave folded dipole has a feed point impedance of approximately 300 ohms — four times the 72-ohm impedance of a standard half-wave dipole. The impedance transformation ratio is N², where N is the number of conductors (2 for a standard folded dipole: 2² = 4, so 72 × 4 = 288 ≈ 300 ohms). This conveniently matches 300-ohm twin-lead transmission line.

### E9C08
**What is a folded dipole antenna?**
- A) A dipole one-quarter wavelength long
- B) A center-fed dipole with the ends folded down 90 degrees at the midpoint of each side
- **C) A half-wave dipole with an additional parallel wire connecting its two ends** ✅
- D) A dipole configured to provide forward gain

> A folded dipole is a half-wave dipole with an additional parallel wire connecting its two ends, forming a continuous loop. The folded structure transforms the impedance upward (to ~300 ohms) while maintaining the same radiation pattern as a regular dipole. The wider conductor cross-section also provides broader bandwidth. Folded dipoles are commonly used as Yagi driven elements.

### E9C09
**Which of the following describes a G5RV antenna?**
- **A) A wire antenna center-fed through a specific length of open-wire line connected to a balun and** ✅
- B) A multi-band trap antenna
- C) A phased array antenna consisting of multiple loops
- D) A wide band dipole using shorted coaxial cable for the radiating elements and fed with a 4:1 balun

> A G5RV antenna is a wire antenna center-fed through a specific length of open-wire line connected to a balun and then coaxial cable. The open-wire section transforms the antenna impedance to a range that the balun and coax can handle on multiple bands. It's popular as a simple multi-band antenna for HF operation. The standard G5RV uses a 102-foot dipole with 34 feet of open-wire feed line.

### E9C10
**Which of the following describes a Zepp antenna?**
- A) A horizontal array capable of quickly changing the direction of maximum radiation by changing
- **B) An end-fed half-wavelength dipole** ✅
- C) An omni-directional antenna commonly used for satellite communications
- D) A vertical array capable of quickly changing the direction of maximum radiation by changing phasing

> A Zepp antenna is an end-fed half-wavelength dipole. Originally used on Zeppelins (airships), it was fed from the end through open-wire line. An end-fed half-wave has very high impedance at the feed point (several thousand ohms), requiring a matching network or transformer. Modern 'end-fed half-wave' (EFHW) antennas use a 49:1 transformer for this matching.

### E9C11
**How is the far-field elevation pattern of a vertically polarized antenna affected by being mounted over seawater versus soil?**
- A) Radiation at low angles decreases
- B) Additional lobes appear at higher elevation angles
- C) Separate elevation lobes will combine into a single lobe
- **D) Radiation at low angles increases** ✅

> Mounting a vertically polarized antenna over seawater (excellent conductor) increases radiation at low angles compared to mounting over poor soil. Seawater's high conductivity creates near-perfect ground reflections, reinforcing low-angle radiation. This is why vertical antennas at coastal stations are exceptionally effective for DX — the seawater acts almost like a perfect mirror at RF.

### E9C12
**Which of the following describes an extended double Zepp antenna?**
- A) An end-fed full-wave dipole antenna
- B) A center-fed 1.5-wavelength dipole antenna
- **C) A center-fed 1.25-wavelength dipole antenna** ✅
- D) An end-fed 2-wavelength dipole antenna

> An extended double Zepp (EDZ) is a center-fed 1.25-wavelength dipole antenna. The extra length beyond a full wavelength increases gain to about 3 dBd (compared to 0 dBd for a half-wave dipole). The radiation pattern has a narrower main lobe than a standard dipole but with some side lobes. The feed point impedance is high (several hundred ohms), requiring matching.

### E9C13
**How does the radiation pattern of a horizontally polarized antenna vary with increasing height above ground?**
- A) The takeoff angle of the lowest elevation lobe increases
- **B) The takeoff angle of the lowest elevation lobe decreases** ✅
- C) The horizontal beamwidth increases
- D) The horizontal beamwidth decreases

> As a horizontally polarized antenna is raised higher above ground, the takeoff angle of the lowest elevation lobe decreases. At 1/4 wavelength height, the main lobe is nearly straight up (NVIS). At 1/2 wavelength, it's around 30°. At 1 wavelength, about 14°. Higher antennas favor DX (low angles); lower antennas favor local/regional communication (high angles).

### E9C14
**How does the radiation pattern of a horizontally-polarized antenna mounted above a long slope compare with the same antenna mounted above flat ground?**
- A) The main lobe takeoff angle increases in the downhill direction
- **B) The main lobe takeoff angle decreases in the downhill direction** ✅
- C) The horizontal beamwidth decreases in the downhill direction
- D) The horizontal beamwidth increases in the uphill direction

> When a horizontally polarized antenna is mounted above a long slope, the effective ground plane is tilted. The main lobe takeoff angle decreases in the downhill direction — the slope tilts the reflection geometry to favor lower angles downhill. This can be advantageous for DX in the downhill direction. Conversely, the takeoff angle increases in the uphill direction.

## Group E9D — Directional antennas: Yagi antennas; Quad antennas; stacking; feeding Yagi antennas

### E9D01
**How much does the gain of an ideal parabolic reflector antenna increase when the operating frequency is doubled?**
- A) 2 dB
- B) 3 dB
- C) 4 dB
- **D) 6 dB** ✅

> Parabolic reflector antenna gain = (π²D²)/(λ²) × efficiency. When frequency doubles, wavelength halves: λ → λ/2. Since gain ∝ 1/λ², gain increases by a factor of 4 = 6 dB. Every doubling of frequency adds 6 dB of gain for a parabolic dish of the same physical size. This is why large dishes are more effective at higher frequencies.

### E9D02
**How can two linearly polarized Yagi antennas be used to produce circular polarization?**
- A) Stack two Yagis to form an array with the respective elements in parallel planes fed 90 degrees out of
- B) Stack two Yagis to form an array with the respective elements in parallel planes fed in phase
- **C) Arrange two Yagis on the same axis and perpendicular to each other with the driven elements at the** ✅
- D) Arrange two Yagis collinear to each other with the driven elements fed 180 degrees out of phase

> To produce circular polarization from two Yagis, arrange them on the same boom axis, perpendicular to each other (crossed), with the driven elements at the same location and fed 90° out of phase. One Yagi handles horizontal and the other handles vertical polarization. The 90° phase difference rotates the combined field vector, creating circular polarization. This is standard for satellite work on VHF/UHF.

### E9D03
**What is the most efficient location for a loading coil on an electrically short whip?**
- **A) Near the center of the vertical radiator** ✅
- B) As low as possible on the vertical radiator
- C) At a voltage maximum
- D) At a voltage null

> The most efficient location for a loading coil on a short vertical is near the center of the radiator. Center loading distributes current more evenly along the element, resulting in more of the antenna carrying useful current. Base loading is easiest mechanically but least efficient — it causes high current only at the base with rapid falloff. Top loading (capacity hat) is most efficient but center loading is the practical compromise.

### E9D04
**Why should antenna loading coils have a high ratio of reactance to resistance?**
- A) To swamp out harmonics
- B) To lower the radiation angle
- **C) To maximize efficiency** ✅
- D) To minimize the Q

> Loading coils should have a high ratio of reactance to resistance (high Q) to maximize efficiency. The coil's resistance is loss resistance that wastes power as heat rather than radiating it. A coil with Q = X_L/R = 300 wastes much less power than one with Q = 50. On an electrically short antenna where radiation resistance may be only 5-10 ohms, even a few ohms of coil loss resistance significantly reduces efficiency.

### E9D05
**Approximately how long is a Yagi’s driven element?**
- A) 234 divided by frequency in MHz
- B) 1005 divided by frequency in MHz
- C) 1/4 wavelength
- **D) 1/2 wavelength** ✅

> A Yagi's driven element is approximately 1/2 wavelength long. The driven element is a half-wave dipole (or folded dipole) that is directly connected to the feed line. It's slightly shorter than an exact half wavelength due to the effect of the parasitic elements. Directors are shorter than the driven element; reflectors are longer.

### E9D06
**What happens to SWR bandwidth when one or more loading coils are used to resonate an electrically short antenna?**
- A) It is increased
- **B) It is decreased** ✅
- C) It is unchanged if the loading coil is located at the feed point
- D) It is unchanged if the loading coil is located at a voltage maximum point

> Adding loading coils to resonate an electrically short antenna decreases the SWR bandwidth. The loading coils add reactance with high Q, making the antenna system more frequency-selective (higher Q overall). Higher Q = narrower bandwidth. The more loading needed (shorter antenna), the narrower the bandwidth becomes. A full-size resonant antenna always has wider bandwidth than a loaded short one.

### E9D07
**What is an advantage of top loading an electrically short HF vertical antenna?**
- A) Lower Q
- B) Greater structural strength
- C) Higher losses
- **D) Improved radiation efficiency** ✅

> Top loading an electrically short vertical (using a capacity hat, radial wires, or a disk at the top) improves radiation efficiency. Top loading increases the current distribution along the vertical portion of the antenna, putting more current on the radiating element where it can contribute to the far field. This increases the radiation resistance while requiring less loading coil inductance (and its associated losses).

### E9D08
**What happens as the Q of an antenna increases?**
- A) SWR bandwidth increases
- **B) SWR bandwidth decreases** ✅
- C) Gain is reduced
- D) More common-mode current is present on the feed line

> As antenna Q increases, SWR bandwidth decreases. Q and bandwidth are inversely related: BW = f_0/Q. A high-Q antenna has a very sharp impedance curve — SWR rises rapidly as you move away from resonance. Electrically small antennas inherently have high Q and narrow bandwidth. Full-size antennas and fat conductors lower Q and increase bandwidth.

### E9D09
**What is the function of a loading coil in an electrically short antenna?**
- A) To increase the SWR bandwidth by increasing net reactance
- B) To lower the losses
- C) To lower the Q
- **D) To resonate the antenna by cancelling the capacitive reactance** ✅

> A loading coil cancels the capacitive reactance of an electrically short antenna to achieve resonance. An antenna shorter than 1/4 wavelength (vertical) or 1/2 wavelength (dipole) has capacitive reactance at its feed point. The loading coil adds inductive reactance (equal and opposite) to cancel it, making the feed point impedance purely resistive at the design frequency. This is tuning the antenna to resonance.

### E9D10
**How does radiation resistance of a base-fed whip antenna change below its resonant frequency?**
- A) Radiation resistance increases
- **B) Radiation resistance decreases** ✅
- C) Radiation resistance becomes imaginary
- D) Radiation resistance does not depend on frequency

> As a base-fed whip is operated below its resonant frequency, its radiation resistance decreases. The radiation resistance of a short vertical is proportional to (height/wavelength)². As frequency decreases, the antenna becomes a smaller fraction of a wavelength, and R_rad drops. At 1/4 wavelength resonance, R_rad ≈ 36 ohms. At 1/8 wavelength, it's roughly 8 ohms. Lower R_rad means lower efficiency unless ground losses are also very low.

### E9D11
**Why do most two-element Yagis with normal spacing have a reflector instead of a director?**
- A) Lower SWR
- B) Higher receiving directivity factor
- C) Greater front-to-side
- **D) Higher gain** ✅

> Most two-element Yagis use a reflector instead of a director because the reflector configuration provides higher gain. A 2-element Yagi with reflector has about 4-5 dBd gain, while a 2-element Yagi with director has about 3-4 dBd. The reflector also provides better front-to-back ratio. The spacing is less critical with a reflector, making it easier to build and tune.

### E9D12
**What is the purpose of making a Yagi’s parasitic elements either longer or shorter than resonance?**
- A) Wind torque cancellation
- B) Mechanical balance
- **C) Control of phase shift** ✅
- D) Minimize losses

> Making a Yagi's parasitic elements either longer (reflector) or shorter (directors) than resonance controls the phase shift of the reradiated signal. A longer-than-resonant element has inductive reactance and reradiates with a lagging phase. A shorter-than-resonant element has capacitive reactance and reradiates with a leading phase. This controlled phase shift is what creates the directional pattern.

## Group E9E — Matching techniques: matching antennas to feed lines; power matching; SWR; antenna tuners; common-mode chokes

### E9E01
**Which matching system for Yagi antennas requires the driven element to be insulated from the boom?**
- A) Gamma
- **B) Beta or hairpin** ✅
- C) Shunt-fed
- D) T-match

> A beta (hairpin) match requires the driven element to be insulated from the boom because the match connects between the two halves of a split driven element. The hairpin (a shorted stub of wire) connects across the feed point to add inductive reactance that cancels the capacitive reactance of a shorter-than-resonant driven element. The gamma match, by contrast, can work with a boom-connected (grounded) element.

### E9E02
**What antenna matching system matches coaxial cable to an antenna by connecting the shield to the center of the antenna and the conductor a fraction of a wavelength to one side?**
- **A) Gamma match** ✅
- B) Delta match
- C) T-match
- D) Stub match

> A gamma match connects the coax shield to the boom (center of the driven element) and the center conductor to a point partway along one side of the element via a parallel rod. This asymmetric tap achieves impedance transformation from the element's impedance to 50 ohms. The gamma match is popular for Yagi antennas because the driven element can be electrically connected to the boom.

### E9E03
**What matching system uses a short length of transmission line connected in parallel with the feed line at or near the feed point?**
- A) Gamma match
- B) Delta match
- C) T-match
- **D) Stub match** ✅

> A stub match uses a short length of transmission line connected in parallel with the feed line at or near the feed point. The stub can be open or shorted at its far end and its length is chosen to present a specific susceptance that cancels the reactive component of the antenna impedance. Single or double stubs can match a wide range of impedances.

### E9E04
**What is the purpose of the series capacitor in a gamma match?**
- A) To provide DC isolation between the feed line and the antenna
- **B) To cancel unwanted inductive reactance** ✅
- C) To provide a rejection notch that prevents the radiation of harmonics
- D) To transform the antenna impedance to a higher value

> The series capacitor in a gamma match cancels the unwanted inductive reactance introduced by the gamma rod (the parallel conductor). The gamma rod adds inductive reactance to the match; the series capacitor provides equal and opposite capacitive reactance. Adjusting the capacitor tunes out this reactance, leaving a purely resistive 50-ohm match.

### E9E05
**What Yagi driven element feed point impedance is required to use a beta or hairpin matching system?**
- **A) Capacitive (driven element electrically shorter than 1/2 wavelength)** ✅
- B) Inductive (driven element electrically longer than 1/2 wavelength)
- C) Purely resistive
- D) Purely reactive

> A beta (hairpin) matching system requires the driven element to be electrically shorter than 1/2 wavelength, presenting capacitive reactance at the feed point. The hairpin (a short-circuited stub of wire across the feed point) adds inductive reactance to cancel the capacitive reactance. If the element were inductive, you'd need a capacitor instead — but the beta match specifically uses an inductive hairpin, so the element must be capacitive.

### E9E06
**Which of these transmission line impedances would be suitable for constructing a quarter-wave Q- section for matching a 100-ohm feed point impedance to a 50-ohm transmission line?**
- A) 50 ohms
- B) 62 ohms
- **C) 75 ohms** ✅
- D) 90 ohms

> A quarter-wave Q-section (matching transformer) impedance = √(Z₁ × Z₂). For Z₁ = 100 ohms and Z₂ = 50 ohms: Z_section = √(100 × 50) = √5000 = 70.7 ≈ 75 ohms. A 75-ohm transmission line (like RG-11 or RG-59) cut to exactly 1/4 wavelength will transform 100 ohms to 50 ohms. This is the quarter-wave transformer matching technique.

### E9E07
**What parameter describes the interaction of a load and transmission line?**
- A) Characteristic impedance
- **B) Reflection coefficient** ✅
- C) Velocity factor
- D) Dielectric constant

> The reflection coefficient describes the interaction of a load and transmission line. It's the ratio of reflected wave amplitude to incident wave amplitude: Γ = (Z_L - Z_0) / (Z_L + Z_0). When the load matches the line (Z_L = Z_0), Γ = 0 (no reflection). A short circuit gives Γ = -1, an open gives Γ = +1. SWR = (1 + |Γ|) / (1 - |Γ|).

### E9E08
**What is a use for a Wilkinson divider?**
- A) To divide the operating frequency of a transmitter signal so it can be used on a lower frequency band
- B) To feed high-impedance antennas from a low-impedance source
- **C) To divide power equally between two 50-ohm loads while maintaining 50-ohm input impedance** ✅
- D) To divide the frequency of the input to a counter to increase its frequency range

> A Wilkinson divider splits power equally between two 50-ohm loads while maintaining 50-ohm input impedance and providing isolation between the output ports. It uses quarter-wave transmission line sections and a bridging resistor. Wilkinson dividers are used in phased arrays, measurement systems, and any application requiring equal power division with good port isolation.

### E9E09
**Which of the following is used to shunt feed a grounded tower at its base?**
- A) Double-bazooka match
- B) Beta or hairpin match
- **C) Gamma match** ✅
- D) All these choices are correct

> A gamma match is used to shunt-feed a grounded tower at its base. Since the tower is grounded (connected to earth at the base), you can't break it to insert a feed point. The gamma match attaches a parallel rod alongside the tower base and feeds between the rod and the tower, effectively creating a feed point without insulating the tower from ground.

### E9E11
**What is the purpose of using multiple driven elements connected through phasing lines?**
- **A) To control the antenna’s radiation pattern** ✅
- B) To prevent harmonic radiation from the transmitter
- C) To allow single-band antennas to operate on other bands
- D) To create a low-angle radiation pattern

> Multiple driven elements connected through phasing lines control the antenna's radiation pattern. By adjusting the phase and amplitude of current in each element through the phasing lines, you can steer the beam, create nulls in specific directions, or change the pattern shape. This is the basis of phased array antennas used for directional control.

## Group E9F — Transmission lines: characteristics; standing waves; SWR; velocity factor; electrical length; coaxial cable

### E9F01
**What is the velocity factor of a transmission line?**
- A) The ratio of its characteristic impedance to its termination impedance
- B) The ratio of its termination impedance to its characteristic impedance
- C) The velocity of a wave in the transmission line multiplied by the velocity of light in a vacuum
- **D) The velocity of a wave in the transmission line divided by the velocity of light in a vacuum** ✅

> Velocity factor is the ratio of the speed of an electromagnetic wave in the transmission line to the speed of light in a vacuum. For example, solid polyethylene coax has VF ≈ 0.66 (66%), meaning waves travel at 66% of the speed of light. Foam dielectric coax has VF ≈ 0.80. Open-wire line has VF ≈ 0.95. Velocity factor is needed to calculate the physical length of electrically-specified transmission line sections.

### E9F02
**Which of the following has the biggest effect on the velocity factor of a transmission line?**
- A) The characteristic impedance
- B) The transmission line length
- **C) The insulating dielectric material** ✅
- D) The center conductor resistivity

> The insulating dielectric material has the biggest effect on velocity factor. VF = 1/√(ε_r), where ε_r is the relative permittivity (dielectric constant) of the insulating material. Air has ε_r = 1.0 (VF = 1.0), polyethylene ε_r = 2.3 (VF = 0.66), Teflon ε_r = 2.1 (VF = 0.69), foam ε_r ≈ 1.5 (VF = 0.82). The conductor material and line length don't affect VF.

### E9F03
**Why is the electrical length of a coaxial cable longer than its physical length?**
- A) Skin effect is less pronounced in the coaxial cable
- B) Skin effect is more pronounced in the coaxial cable
- C) Electromagnetic waves move faster in coaxial cable than in air
- **D) Electromagnetic waves move more slowly in a coaxial cable than in air** ✅

> The electrical length of coax is longer than its physical length because electromagnetic waves travel more slowly in coaxial cable than in air. The dielectric material (polyethylene, Teflon, foam) slows the wave to a fraction of the speed of light (the velocity factor). A cable that's physically 10 feet long but has VF = 0.66 is electrically equivalent to 10/0.66 = 15.2 feet of free space.

### E9F04
**What impedance does a 1/2-wavelength transmission line present to an RF generator when the line is shorted at the far end?**
- A) Very high impedance
- **B) Very low impedance** ✅
- C) The same as the characteristic impedance of the line
- D) The same as the output impedance of the RF generator

> A half-wavelength transmission line reproduces the load impedance at its input. If the far end is shorted (Z_L = 0), the input also looks like a short — very low impedance. This is because the impedance transformation goes through a full cycle in λ/2: short → open → short. The formula: Z_in = Z_0² / Z_L only applies to quarter-wave lines; for half-wave: Z_in = Z_L.

### E9F05
**What is microstrip?**
- A) Special shielding material designed for microwave frequencies
- B) Miniature coax used for low power applications
- C) Short lengths of coax mounted on printed circuit boards to minimize time delay between microwave
- **D) Precision printed circuit conductors above a ground plane that provide constant impedance** ✅

> Microstrip is a precision printed circuit conductor above a ground plane that provides constant impedance. It's a flat conductor trace on one side of a dielectric substrate with a ground plane on the other side. The impedance is determined by the trace width, substrate thickness, and dielectric constant. Microstrip is the standard transmission line technology for microwave circuits on PCBs.

### E9F06
**What is the approximate physical length of an air-insulated, parallel conductor transmission line that is electrically 1/2 wavelength long at 14.10 MHz?**
- A) 7.0 meters
- B) 8.5 meters
- **C) 10.6 meters** ✅
- D) 13.3 meters

> Physical length = (electrical length) × (velocity factor). A half wavelength at 14.1 MHz: λ = 300/14.1 = 21.28 meters. Half wavelength = 10.64 meters. For air-insulated parallel conductor line, VF ≈ 0.95-1.0. With VF ≈ 1.0: physical length ≈ 10.6 meters. The answer accounts for the near-unity velocity factor of air-spaced parallel conductor line.

### E9F07
**How does parallel conductor transmission line compare to coaxial cable with a plastic dielectric?**
- **A) Lower loss** ✅
- B) Higher SWR
- C) Smaller reflection coefficient
- D) Lower velocity factor

> Parallel conductor (open-wire, ladder line) transmission line has lower loss than coaxial cable with plastic dielectric. The reasons: (1) the dielectric is mostly air (lower dielectric losses), (2) the conductors are farther apart (lower conductor losses per unit length), and (3) the higher characteristic impedance means lower current for the same power (I²R losses are lower). Ladder line at 450 ohms has dramatically less loss than RG-8 at 50 ohms.

### E9F08
**Which of the following is a significant difference between foam dielectric coaxial cable and solid dielectric coaxial cable, assuming all other parameters are the same?**
- A) Foam dielectric coaxial cable has lower safe maximum operating voltage
- B) Foam dielectric coaxial cable has lower loss per unit of length
- C) Foam dielectric coaxial cable has higher velocity factor
- **D) All these choices are correct** ✅

> Foam dielectric coax compared to solid dielectric coax (all other factors equal): foam has (1) lower safe maximum voltage (the foam can break down), (2) lower loss per unit length (less dielectric material = less dielectric loss), and (3) higher velocity factor (foam ε_r is closer to air). All these choices are correct.

### E9F09
**What impedance does a 1/4-wavelength transmission line present to an RF generator when the line is shorted at the far end?**
- **A) Very high impedance** ✅
- B) Very low impedance
- C) The same as the characteristic impedance of the transmission line
- D) The same as the generator output impedance

> A quarter-wavelength shorted transmission line presents very high impedance at its input. The short circuit at the far end is transformed through a quarter wavelength of phase shift to look like an open circuit at the input. Z_in = Z_0² / Z_L, and as Z_L → 0, Z_in → ∞ (in practice, very high). This is a quarter-wave stub's fundamental property.

### E9F10
**What impedance does a 1/8-wavelength transmission line present to an RF generator when the line is shorted at the far end?**
- A) A capacitive reactance
- B) The same as the characteristic impedance of the line
- **C) An inductive reactance** ✅
- D) Zero

> A 1/8-wavelength shorted transmission line presents an inductive reactance at its input. A shorted line shorter than λ/4 looks inductive (positive reactance). The exact value: Z_in = jZ_0 × tan(βl). For l = λ/8: βl = 45°, tan(45°) = 1, so Z_in = jZ_0. The reactance is purely inductive and equal to the characteristic impedance in magnitude.

### E9F11
**What impedance does a 1/8-wavelength transmission line present to an RF generator when the line is open at the far end?**
- A) The same as the characteristic impedance of the line
- B) An inductive reactance
- **C) A capacitive reactance** ✅
- D) Infinite

> A 1/8-wavelength open-ended transmission line presents a capacitive reactance at its input. An open line shorter than λ/4 looks capacitive (negative reactance). Z_in = -jZ_0 × cot(βl). For l = λ/8: βl = 45°, cot(45°) = 1, so Z_in = -jZ_0. The reactance is purely capacitive with magnitude equal to the characteristic impedance. Open stubs shorter than λ/4 are capacitive.

### E9F12
**What impedance does a 1/4-wavelength transmission line present to an RF generator when the line is open at the far end?**
- A) The same as the characteristic impedance of the line
- B) The same as the input impedance to the generator
- C) Very high impedance
- **D) Very low impedance** ✅

> A quarter-wavelength open transmission line presents very low impedance at its input. The open circuit at the far end is transformed through λ/4 to look like a short circuit at the input. This is the complement of the λ/4 shorted line (which looks open). The quarter-wave transformation: Z_in = Z_0² / Z_L, and Z_L = ∞ gives Z_in = 0.

## Group E9G — The Smith chart: using the Smith chart; normalizing impedances; impedance matching; transmission line analysis

### E9G01
**Which of the following can be calculated using a Smith chart?**
- **A) Impedance along transmission lines** ✅
- B) Radiation resistance
- C) Antenna radiation pattern
- D) Radio propagation

> A Smith chart can be used to calculate impedance along transmission lines. By plotting the load impedance (normalized to the line's characteristic impedance) and rotating around the chart, you can find the impedance at any point along the line. One full rotation = λ/2 of transmission line. The Smith chart graphically solves the complex transmission line equations.

### E9G02
**What type of coordinate system is used in a Smith chart?**
- A) Voltage circles and current arcs
- **B) Resistance circles and reactance arcs** ✅
- C) Voltage chords and current chords
- D) Resistance lines and reactance chords

> A Smith chart uses a coordinate system of resistance circles and reactance arcs. The resistance circles are centered on the horizontal (real) axis, and the reactance arcs curve from the right side of the chart. Every point on the Smith chart represents a unique complex impedance Z = R + jX (normalized to Z_0).

### E9G03
**Which of the following is often determined using a Smith chart?**
- A) Beam headings and radiation patterns
- B) Satellite azimuth and elevation bearings
- **C) Impedance and SWR values in transmission lines** ✅
- D) Point-to-point propagation reliability as a function of frequency

> Smith charts are commonly used to determine impedance and SWR values in transmission lines. By plotting the load impedance and rotating clockwise (toward generator) along constant-SWR circles, you can find the impedance at any point along the line. The SWR is read from the intersection of the constant-SWR circle with the real axis.

### E9G04
**What are the two families of circles and arcs that make up a Smith chart?**
- A) Inductance and capacitance
- B) Reactance and voltage
- **C) Resistance and reactance** ✅
- D) Voltage and impedance

> The two families of curves on a Smith chart are resistance circles and reactance arcs. Resistance circles are complete circles (centered on the real axis) representing constant resistance values. Reactance arcs are portions of circles representing constant reactance values (positive above the center line = inductive, negative below = capacitive).

### E9G05
**Which of the following is a common use for a Smith chart?**
- **A) Determine the length and position of an impedance matching stub** ✅
- B) Determine the impedance of a transmission line, given the physical dimensions
- C) Determine the gain of an antenna given the physical and electrical parameters
- D) Determine the loss/100 feet of a transmission line, given the velocity factor and conductor materials

> A common use for the Smith chart is determining the length and position of an impedance matching stub. To design a stub match: (1) plot the load impedance, (2) rotate along the transmission line to find where the conductance circle passes through 1.0, (3) calculate the stub length needed to cancel the remaining susceptance. The Smith chart makes this graphical solution straightforward.

### E9G06
**On the Smith chart shown in Figure E9-3, what is the name for the large outer circle on which the reactance arcs terminate?**
- A) Prime axis
- **B) Reactance axis** ✅
- C) Impedance axis
- D) Polar axis

> The large outer circle on the Smith chart where reactance arcs terminate is the reactance axis. It represents points of zero resistance and pure reactance. The top half represents positive (inductive) reactance and the bottom half represents negative (capacitive) reactance. The rightmost point is an open circuit; the leftmost point is a short circuit.

### E9G07
**On the Smith chart shown in Figure E9-3, what is the only straight line shown?**
- A) The reactance axis
- B) The current axis
- C) The voltage axis
- **D) The resistance axis** ✅

> The only straight line on the Smith chart is the resistance axis — the horizontal line running from left (R=0, short circuit) to right (R=∞, open circuit) through the center (R=1, normalized). This line represents all purely resistive impedances (zero reactance). Every other line on the chart is a circle or arc.

### E9G08
**How is a Smith chart normalized?**
- A) Reassign the reactance axis with resistance values
- B) Reassign the resistance axis with reactance values
- **C) Reassign the prime center’s impedance value** ✅
- D) Reassign the prime center to the reactance axis

> A Smith chart is normalized by reassigning the impedance value at the prime center (the center point of the chart). Normally, the center represents Z/Z_0 = 1.0 + j0 (normalized to the characteristic impedance). For a 50-ohm system, the center is 50+j0 ohms. For 75-ohm, you renormalize by dividing all impedances by 75 instead of 50. This allows the same chart to be used for any Z_0.

### E9G09
**What third family of circles is often added to a Smith chart during the process of designing impedance matching networks?**
- **A) Constant-SWR circles** ✅
- B) Transmission line length circles
- C) Coaxial-length circles
- D) Radiation-pattern circles

> Constant-SWR circles are often added to Smith charts during impedance matching design. A constant-SWR circle is centered on the prime center and passes through the plotted impedance point. Every point on this circle has the same SWR. Moving along the transmission line moves you around this circle. The goal of matching is to move the impedance to the center (SWR = 1:1).

### E9G10
**What do the arcs on a Smith chart represent?**
- A) Frequency
- B) SWR
- C) Points with constant resistance
- **D) Points with constant reactance** ✅

> The arcs on a Smith chart represent points with constant reactance. Each arc connects points that have the same reactive component (the same X in Z = R + jX). Upper arcs = positive (inductive) reactance; lower arcs = negative (capacitive) reactance. The arcs all terminate at the right edge of the chart (open circuit point) and at the outer circle (reactance axis).

### E9G11
**In what units are the wavelength scales on a Smith chart calibrated?**
- A) In fractions of transmission line electrical frequency
- **B) In fractions of transmission line electrical wavelength** ✅
- C) In fractions of antenna electrical wavelength
- D) In fractions of antenna electrical frequency

> The wavelength scales on a Smith chart are calibrated in fractions of transmission line electrical wavelength. The outer scales show 'wavelengths toward generator' and 'wavelengths toward load,' each running from 0 to 0.5 (half wavelength = one complete revolution around the chart). These scales let you determine the impedance transformation for a given length of transmission line.

## Group E9H — Receiving antennas: direction finding antennas; active antennas; noise-canceling antennas; loop antennas; magnetic loops

### E9H01
**When constructing a Beverage antenna, which of the following factors should be included in the design to achieve good performance at the desired frequency?**
- A) Its overall length must not exceed 1/4 wavelength
- B) It must be mounted more than 1 wavelength above ground
- C) It should be configured as a four-sided loop
- **D) It should be at least one wavelength long** ✅

> A Beverage antenna should be at least one wavelength long for good performance at the design frequency. The Beverage is a traveling-wave antenna — its directivity increases with length. Typical Beverage antennas for 160 meters are 500-1000 feet long. They're mounted low (1-2 meters above ground) and terminated with a matching resistor. Longer = more directivity and gain.

### E9H02
**Which is generally true for 160- and 80-meter receiving antennas?**
- **A) Atmospheric noise is so high that directivity is much more important than losses** ✅
- B) They must be erected at least 1/2 wavelength above the ground to attain good directivity
- C) Low loss coax transmission line is essential for good performance
- D) All these choices are correct

> On 160 and 80 meters, atmospheric noise (QRN) is so high that it far exceeds the antenna's internal losses. This means directivity (the ability to reject noise from unwanted directions) is much more important than antenna efficiency. A lossy but directional antenna (like a small loop or Beverage) outperforms an efficient but omnidirectional antenna because it rejects most of the noise.

### E9H03
**What is receiving directivity factor (RDF)?**
- A) Forward gain compared to the gain in the reverse direction
- B) Relative directivity compared to isotropic
- C) Relative directivity compared to a dipole
- **D) Peak antenna gain compared to average gain over the hemisphere around and above the antenna** ✅

> Receiving Directivity Factor (RDF) is the ratio of peak antenna gain to the average gain over the hemisphere around and above the antenna. Higher RDF means the antenna discriminates better between desired signals and noise from all other directions. RDF is the most useful single number for comparing receiving antennas, especially on the low bands where noise rejection matters most.

### E9H04
**What is the purpose of placing an electrostatic shield around a small-loop direction-finding antenna?**
- A) It adds capacitive loading, increasing the bandwidth of the antenna
- **B) It eliminates unbalanced capacitive coupling to the antenna’s surroundings, improving the depth of its** ✅
- C) It eliminates tracking errors caused by strong out-of-band signals
- D) It increases signal strength by providing a better match to the feed line

> An electrostatic shield around a small-loop direction-finding antenna eliminates unbalanced capacitive coupling to the surroundings, improving the depth of its pattern nulls. Without the shield, electric field pickup (which is omnidirectional) fills in the nulls of the magnetic field pattern (which has deep nulls). The Faraday shield blocks the electric field while allowing the magnetic field to pass through to the loop.

### E9H05
**What challenge is presented by a small wire-loop antenna for direction finding?**
- **A) It has a bidirectional null pattern** ✅
- B) It does not have a clearly defined null
- C) It is practical for use only on VHF and higher bands
- D) All these choices are correct

> A small wire-loop antenna for direction finding has a bidirectional null pattern — the figure-eight pattern has two nulls, 180° apart. This means you can determine the LINE the signal is on but not which direction along that line it comes from (the 180° ambiguity). A sense antenna is needed to resolve this ambiguity and determine the actual bearing.

### E9H06
**What indicates the correct value of terminating resistance for a Beverage antenna?**
- A) Maximum feed point DC resistance at the center of the desired frequency range
- B) Minimum low-angle front-to-back ratio at the design frequency
- C) Maximum DC current in the terminating resistor
- **D) Minimum variation in SWR over the desired frequency range** ✅

> The correct termination resistance for a Beverage antenna is indicated by minimum variation in SWR over the desired frequency range. A properly terminated Beverage is a traveling-wave antenna with flat SWR. If the termination is wrong, standing waves appear, and SWR varies with frequency. Adjusting the termination for flattest SWR gives the best match and pattern.

### E9H07
**What is the function of a Beverage antenna’s termination resistor?**
- A) Increase the front-to-side ratio
- **B) Absorb signals from the reverse direction** ✅
- C) Decrease SWR bandwidth
- D) Eliminate harmonic reception

> The termination resistor in a Beverage antenna absorbs signals arriving from the reverse direction. Without it, energy reaching the far end reflects back along the wire, creating a bidirectional pattern. The resistor absorbs this reverse-traveling wave, making the pattern unidirectional — the Beverage receives best from the direction pointing away from the termination.

### E9H08
**What is the function of a sense antenna?**
- **A) It modifies the pattern of a DF antenna to provide a null in only one direction** ✅
- B) It increases the sensitivity of a DF antenna array
- C) It allows DF antennas to receive signals at different vertical angles
- D) It provides diversity reception that cancels multipath signals

> A sense antenna modifies the bidirectional pattern of a DF loop antenna to provide a null in only one direction (cardioid pattern). The sense antenna (typically a short vertical) provides an omnidirectional signal that, when combined with the loop's figure-eight pattern, eliminates one of the two nulls. This resolves the 180° ambiguity inherent in loop DF antennas.

### E9H09
**What type of radiation pattern is created by a single-turn, terminated loop such as a pennant antenna?**
- **A) Cardioid** ✅
- B) Bidirectional
- C) Omnidirectional
- D) Hyperbolic

> A single-turn, terminated loop (like a pennant, flag, or diamond antenna) creates a cardioid radiation pattern. The termination absorbs energy from one direction, creating a single null in the reverse direction. These small terminated loops are popular low-band receiving antennas because they provide good directivity in a compact size.

### E9H10
**How can the output voltage of a multiple-turn receiving loop antenna be increased?**
- A) By reducing the permeability of the loop shield
- B) By utilizing high impedance wire for the coupling loop
- **C) By increasing the number of turns and/or the area enclosed by the loop** ✅
- D) All these choices are correct

> The output voltage of a receiving loop antenna increases with more turns and/or larger enclosed area. The induced voltage is proportional to N × A × B × ω, where N = number of turns, A = area enclosed, B = magnetic field strength, and ω = angular frequency. Doubling turns doubles the voltage; doubling the area also doubles the voltage.

### E9H11
**What feature of a cardioid pattern antenna makes it useful for direction-finding antennas?**
- A) A very sharp peak
- **B) A single null** ✅
- C) Broadband response
- D) High radiation angle

> A cardioid pattern antenna is useful for direction finding because it has a single null — one deep minimum in one direction. A single null eliminates the 180° ambiguity of a bidirectional pattern (which has two nulls). You simply rotate the antenna until the signal disappears in the null, and the signal source is in the opposite direction.
