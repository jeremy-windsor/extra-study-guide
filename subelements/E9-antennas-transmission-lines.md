# E9 — Antennas and Transmission Lines

E9 is where the Extra exam expects you to think like a station designer instead of just an operator.

A radio signal does not stop at the transmitter output connector. It still has to make its way through feed lines, matching networks, phasing lines, and antenna structures before it leaves as electromagnetic radiation. On receive, the reverse is just as important: the antenna system decides what direction a signal comes from, what noise gets rejected, and how the feed line transforms what the receiver actually sees.

That is why this subelement mixes several topics that belong together in practice:

- antenna gain and efficiency
- radiation patterns and what they really mean
- phased arrays and common wire antennas
- shortened antennas and loading methods
- matching systems such as gamma, beta, and stub matches
- transmission line behavior and impedance transformation
- Smith chart basics
- receiving and direction-finding antennas

The pool has **93 questions**, and the exam pulls **8** from E9.

The groups are:

- **E9A:** antenna fundamentals, gain, efficiency, and ground effects
- **E9B:** radiation patterns, far field, and antenna modeling
- **E9C:** wire antennas, phased verticals, and pattern behavior over real ground
- **E9D:** directional antennas and electrically short antennas
- **E9E:** matching systems and feed arrangements
- **E9F:** transmission line characteristics and impedance transformation
- **E9G:** Smith chart concepts
- **E9H:** receiving antennas and direction finding

The easiest way to keep E9 organized is to keep asking four questions:

1. **Where is the RF current actually flowing?**
2. **Where is the power going — radiation, heat, or reflection?**
3. **How is the antenna pattern being shaped?**
4. **What impedance does the transmitter or receiver actually see?**

If you keep those four questions in mind, E9 becomes much more connected and much less like a pile of unrelated antenna trivia.

---

## Group E9A — Antenna fundamentals, gain, efficiency, and ground effects

This group is the vocabulary and bookkeeping layer of antenna systems.

It asks about:

- what gain references actually mean
- how to calculate ERP and EIRP
- what affects feed point impedance
- why ground and radials matter
- how efficiency is defined
- why higher frequencies have smaller Fresnel zones

### Isotropic radiator: the reference antenna that does not exist

An **isotropic radiator** is a hypothetical, lossless antenna that radiates equally in all directions.

That means:

- it is not physically buildable
- it has no favored direction
- it is used as a mathematical reference
- its gain is defined as **0 dBi**

This is one of the most important reference ideas in antenna work. A real antenna with gain does **not** create extra power. It simply concentrates more of the available radiated power into some directions and less into others.

So when a question mentions **gain over isotropic**, it means **dBi**.
When it mentions **gain over a half-wave dipole**, it means **dBd**.

The conversion you need is:

**dBi = dBd + 2.15 dB**

So:

- 6 dBi = 3.85 dBd
- 7 dBd = 9.15 dBi

That 2.15 dB difference shows up repeatedly in antenna math.

### ERP vs. EIRP: same idea, different reference

These two terms sound similar because they are.

- **ERP** = effective radiated power, referenced to a **dipole**
- **EIRP** = effective isotropic radiated power, referenced to an **isotropic radiator**

Both take the transmitter output and then account for:

- feed line loss
- duplexer or filter loss
- circulator loss
- connector losses if they matter
- antenna gain

The safest way to do these problems is in **dB**.

#### ERP example

Suppose the station has:

- 150 W transmitter output
- 2 dB feed line loss
- 2.2 dB duplexer loss
- 7 dBd antenna gain

Convert power to dBW:

**10 log10(150) = 21.76 dBW**

Then add gains and subtract losses:

**ERP = 21.76 - 2 - 2.2 + 7 = 24.56 dBW**

Convert back to watts:

**10^(24.56/10) ≈ 286 W**

That is the E9A02 style of calculation.

#### ERP example with more losses

If the station has:

- 200 W transmitter output
- 4 dB feed line loss
- 3.2 dB duplexer loss
- 0.8 dB circulator loss
- 10 dBd antenna gain

Then:

**10 log10(200) = 23.01 dBW**

**ERP = 23.01 - 4 - 3.2 - 0.8 + 10 = 25.01 dBW**

**10^(25.01/10) ≈ 317 W**

That is the E9A06 pattern.

#### EIRP example

Now use the isotropic reference instead:

- 200 W transmitter output
- 2 dB feed line loss
- 2.8 dB duplexer loss
- 1.2 dB circulator loss
- 7 dBi antenna gain

Then:

**EIRP = 23.01 - 2 - 2.8 - 1.2 + 7 = 24.01 dBW**

**10^(24.01/10) ≈ 252 W**

That is the E9A07 pattern.

The exam is really checking whether you can keep three things straight:

1. use **dBd** for ERP and **dBi** for EIRP
2. subtract every loss
3. convert back to watts only at the end

### Feed point impedance depends on the antenna and its environment

The feed point impedance of an antenna is not set only by its wire length.

One of the biggest practical influences is **height above ground**.

Why? Because the ground is part of the antenna system whether you want it to be or not. The radiated field reflects from the earth, and that reflected field changes:

- current distribution
- feed point impedance
- takeoff angle
- pattern shape

This is why a dipole at one height can behave very differently from the same dipole at another height.

A tuner at the transmitter does **not** change the antenna’s actual feed point impedance. It only changes what the transmitter sees looking into the feed line.

That distinction matters throughout E9:

- **antenna impedance** is a property of the antenna system itself
- **shack-side impedance** may be a transformed version of that

### Ground gain

**Ground gain** is the increase in signal strength caused by ground reflections in the antenna environment.

This is not “free power.” It is a pattern effect.

The direct wave and the ground-reflected wave can add constructively at certain angles, especially low angles. When they do, the field strength in those directions increases.

This is why antenna height matters so much, especially on HF:

- low height may favor high-angle radiation for regional work
- greater height often improves low-angle radiation for DX
- reflective ground can improve useful radiation at favored angles

### Fresnel zone: why higher microwave frequencies fit through tighter spaces

The **first Fresnel zone** is the region around the direct path between two antennas where obstructions can cause significant cancellation even if they do not block the exact line of sight.

For the exam, the key idea is simple:

- **higher frequency** → **shorter wavelength**
- shorter wavelength → **smaller first Fresnel zone**

So among choices like 900 MHz, 2.4 GHz, 3.4 GHz, and 5.8 GHz, the **5.8 GHz** system has the smallest first Fresnel zone.

This matters in microwave link planning. A path can look visually clear and still perform poorly if trees, ridges, or buildings intrude into the Fresnel zone.

### Antenna efficiency: what fraction is actually radiated?

Antenna efficiency is one of the cleanest formulas in the subelement:

**efficiency = radiation resistance / total resistance**

where:

**total resistance = radiation resistance + loss resistance**

That means efficiency answers this question:

**Of all the RF power accepted by the antenna system, how much becomes radiation instead of heat?**

If an antenna has:

- radiation resistance = 36 Ω
- loss resistance = 4 Ω

then:

**efficiency = 36 / 40 = 0.90 = 90%**

This is why electrically short antennas can be disappointing. Their radiation resistance is often small, so even modest loss resistance can consume a painful fraction of the power.

### Why radials improve vertical efficiency

A ground-mounted quarter-wave vertical depends heavily on the return path through the ground region near the base.

Without a good radial system, RF current flows through lossy soil. That adds ground loss resistance and reduces efficiency.

Installing a **ground radial system** improves efficiency because it provides a lower-resistance return path.

That is one of the most practical E9A ideas:

- more radials generally means lower ground loss
- lower ground loss means better efficiency
- better efficiency means more of the transmitter power becomes radiation

### Soil conductivity matters

For ground-mounted HF verticals, the dominant factor in ground losses is **soil conductivity**.

High-conductivity soil helps.
Poor-conductivity soil hurts.

That is why verticals near seawater often perform unusually well. The ground system is still important, but the environment is helping instead of fighting you.

### Putting E9A together

E9A is mostly about keeping the accounting straight.

Know the references, know what counts as loss, know what actually sets efficiency, and remember that the antenna’s surroundings are part of the antenna system.

If you remember the following, you are in good shape:

- isotropic radiator = theoretical 0 dBi reference
- dipole reference = dBd
- **dBi = dBd + 2.15 dB**
- ERP and EIRP include gains and losses
- height above ground affects feed point impedance and pattern
- ground gain comes from constructive reflection effects
- higher frequency means smaller Fresnel zones
- efficiency = radiation resistance / total resistance
- radials and good soil reduce ground loss in verticals

---

## Group E9B — Radiation patterns, far field, and antenna modeling

This group is about reading patterns correctly and understanding what pattern measurements actually mean.

### How to read an antenna pattern

A radiation pattern is a map of how strongly an antenna radiates or receives in different directions.

Two pattern views appear again and again:

- **azimuth pattern**: horizontal direction around the antenna
- **elevation pattern**: vertical angle above the horizon

Those two views tell different stories.

- Azimuth tells you **which compass directions** are strong or weak.
- Elevation tells you **which takeoff angles** are favored.

On HF, elevation angle matters enormously:

- **low angles** often favor long-distance DX
- **high angles** favor shorter-range or NVIS-style paths

### 3 dB beamwidth means half-power width

The **3 dB beamwidth** is the angular width of the main lobe between the two points where the response falls by 3 dB.

A drop of 3 dB means half the power.

So the 3 dB beamwidth is also called the **half-power beamwidth**.

A narrower beamwidth usually means:

- more directivity
- more gain
- tighter aiming requirements

That does not necessarily mean “better” in every situation. A narrow beam is great when you want concentration in one direction. A wider beam can be more forgiving.

### Front-to-back and front-to-side ratios

These are pattern-rejection measurements.

- **front-to-back ratio** compares the main forward lobe to the response directly behind the antenna
- **front-to-side ratio** compares the main forward lobe to the response off the side

High front-to-back ratio helps reject signals and noise from the rear.
High front-to-side ratio helps reject signals from the sides.

These ratios do not tell you the antenna’s total gain by themselves. They describe **how well the antenna rejects unwanted directions relative to the favored one**.

### Gain does not increase total radiated power

One of the easiest E9 mistakes is to think a lossless directional antenna radiates more total power than an isotropic antenna fed with the same transmitter power.

It does **not**.

If both antennas are lossless and both are driven with the same power:

- total radiated power is the same
- the directional antenna is just redistributing that power

That is what gain really means in this context.

More in one direction means less somewhere else.

### Far field: where the pattern stops changing shape

The **far field** is the region where the shape of the radiation pattern no longer varies with distance.

That is where pattern measurements make sense.

In the far field:

- the electric and magnetic fields behave as a radiated wave
- field strength falls roughly as 1/r
- pattern shape is stable

A common far-field estimate is:

**distance ≈ 2D² / λ**

where:

- **D** = largest antenna dimension
- **λ** = wavelength

The exact boundary is not the point of the exam. The idea is that you must be far enough away that you are measuring the real radiation pattern, not complicated near-field interactions.

### Method of Moments: the modeling method you are expected to recognize

The antenna-analysis method most often named in the Extra pool is the **Method of Moments**.

You do not need the math behind it for the exam. You do need the concept.

In Method of Moments modeling:

- the antenna wire is divided into many short segments
- each segment is assigned a current value
- the interactions among all segments are solved numerically
- the model predicts feed point impedance, current distribution, and radiation pattern

This is the logic behind NEC-style modeling.

The important practical warning is that too few segments reduce accuracy.

If you decrease the segmentation below roughly **10 segments per half-wavelength**, the computed feed point impedance can become unreliable.

That is a classic “garbage in, garbage out” problem. A model is only useful if it is fine enough to represent the actual current distribution.

### Putting E9B together

E9B is testing whether you can interpret patterns like an engineer instead of just admiring them.

The key ideas are:

- azimuth vs. elevation are different pattern views
- 3 dB beamwidth means half-power width
- front-to-back and front-to-side describe rejection
- gain redistributes power; it does not create power
- far-field measurements must be made where pattern shape is stable
- Method of Moments models wires as many short current segments
- too few segments can give bad impedance results

---

## Group E9C — Wire antennas, phased verticals, and real-world pattern behavior

This group mixes several antenna families, but the underlying theme is simple:

**current phasing and geometry determine the pattern.**

### Two-element phased vertical arrays

With two quarter-wave verticals, spacing and phasing decide the pattern.

The exam asks about three classic cases.

#### 1/2 wavelength spacing, fed in phase

This produces a **figure-eight broadside to the array axis**.

Why? Because signals add constructively in directions broadside to the line between the antennas, while cancellation occurs along the axis.

#### 1/2 wavelength spacing, fed 180° out of phase

This produces a **figure-eight oriented along the axis of the array**.

Now the phase reversal changes where reinforcement and cancellation occur.

#### 1/4 wavelength spacing, fed 90° out of phase

This produces a **cardioid** pattern.

That combination of spacing and phasing creates strong radiation in one favored direction and deep cancellation in the opposite direction.

If you want a useful memory hook:

- **in phase, 1/2 λ** → **broadside figure-eight**
- **180° out, 1/2 λ** → **end-fire figure-eight**
- **90° out, 1/4 λ** → **cardioid**

### Long wires, rhombics, and termination

As an **unterminated long-wire antenna** gets longer, additional lobes form and the strongest lobes move more nearly along the wire axis.

That means a longer wire becomes more directional, but also more complex.

If you add a **terminating resistor** to a rhombic or long-wire antenna, you absorb the traveling wave instead of letting it reflect from the far end.

That changes the pattern from:

- **bidirectional** without termination
- to **unidirectional** with termination

The price is efficiency. Some power is deliberately dissipated in the resistor.

But the benefit is a much cleaner forward pattern.

### Off-center-fed dipole (OCFD)

An **off-center-fed dipole** is fed away from the center so that it presents a similar feed point impedance on multiple bands.

That is the real reason for the off-center feed.

It is not magic broadbanding. It is not pattern suppression. It is an impedance strategy.

A well-chosen off-center feed position can make the antenna usable on several harmonically related bands with the same matching arrangement.

### Folded dipole

A standard two-wire half-wave folded dipole has a feed point impedance of about **300 ohms**.

That is about four times the impedance of an ordinary half-wave dipole.

Why four times?

Because with two conductors carrying comparable currents, the impedance transformation is approximately the square of the conductor count ratio. For the common equal-wire folded dipole, that works out to roughly **4 × 72 Ω ≈ 288 Ω**, which is treated as **300 Ω** in practice.

That makes the folded dipole a natural fit for 300-ohm balanced line.

It also explains why folded dipoles are commonly used as the driven elements in Yagis.

### G5RV, Zepp, and extended double Zepp

These names can sound old-fashioned, but the exam expects you to know what they are.

#### G5RV

A **G5RV** is a center-fed wire antenna that uses a **specific length of open-wire line** as part of the matching system, usually followed by a balun and coax.

The key idea is that the matching section is not arbitrary. Its length is part of the design.

#### Zepp antenna

A **Zepp** antenna is an **end-fed half-wave dipole**.

Because it is end-fed, the feed point impedance is very high. That is why matching is such a big part of practical end-fed half-wave systems.

#### Extended double Zepp (EDZ)

An **extended double Zepp** is a **center-fed 1.25-wavelength dipole**.

The extra length narrows the main lobe and increases gain compared with a simple half-wave dipole, though it also raises feed point impedance and creates a more complex pattern.

### Ground and mounting environment shape the pattern

This is one of the most practical sections in the whole subelement.

#### Vertical polarization over seawater

A vertically polarized antenna mounted over seawater produces stronger **low-angle radiation** than the same antenna over ordinary soil.

That is why coastal verticals are famous for DX performance.

Seawater is an excellent RF reflector and conductor, so low-angle radiation is strongly reinforced.

#### Height above ground for horizontal antennas

As a horizontally polarized antenna is raised higher above ground, the **takeoff angle of the lowest elevation lobe decreases**.

That means:

- lower antenna → higher launch angle
- higher antenna → lower launch angle

This is one of the most important HF pattern rules.

If you want low-angle DX radiation, more height usually helps.
If you want high-angle regional coverage, a lower antenna may actually be useful.

#### Long slope effect

If a horizontally polarized antenna is mounted above a long slope, the main lobe takeoff angle tends to decrease in the **downhill** direction.

That is another reminder that terrain is part of the antenna system.

Flat-earth antenna assumptions are often only a first approximation.

### Putting E9C together

E9C is about geometry and phasing.

If you remember these ideas, most of the questions become manageable:

- spacing plus feed phase determines array pattern
- long wires form more lobes as they get longer
- termination makes long-wire and rhombic patterns unidirectional
- OCFD feed location is mainly about multi-band impedance behavior
- folded dipole ≈ 300 Ω
- G5RV uses a specific matching-line section
- Zepp = end-fed half-wave
- EDZ = center-fed 1.25 λ dipole
- seawater improves low-angle vertical performance
- raising a horizontal antenna lowers its lowest takeoff angle
- slopes can tilt the practical pattern

---

## Group E9D — Directional antennas and electrically short antennas

This group combines two things that seem different but share the same theme:

**how physical structure changes radiation behavior.**

### Parabolic reflectors: why frequency matters so much

For a parabolic reflector of fixed physical size, gain is proportional to **1/λ²**.

That means if the operating frequency doubles, the wavelength halves, and the gain increases by a factor of four.

A factor of four in power ratio is:

**6 dB**

So an ideal parabolic dish gains **6 dB** every time frequency doubles, assuming the dish size and efficiency stay the same.

That is why dish antennas become so powerful at microwave frequencies.

### Crossed Yagis for circular polarization

Two linearly polarized Yagis can produce **circular polarization** if they are:

- mounted on the same axis
- oriented at right angles to each other
- fed **90 degrees out of phase**

One antenna provides one linear component, the other provides the orthogonal component, and the 90° phase shift makes the field vector rotate.

That is the standard crossed-Yagi idea used for satellite work.

### Yagi basics you should know cold

A Yagi’s **driven element** is approximately **1/2 wavelength** long.

The **reflector** is slightly longer than resonance.
The **director(s)** are slightly shorter than resonance.

That difference in length is not mechanical decoration. It sets the **phase shift** of the reradiated currents, which is what produces the directional pattern.

That is the answer behind questions asking why parasitic elements are made longer or shorter than resonance.

### Why two-element Yagis usually use a reflector

For normal spacing, a two-element Yagi usually uses a **reflector** rather than a director because the reflector arrangement gives **higher gain**.

That also tends to give a useful front-to-back ratio.

The exam is not asking you to compare every possible optimized two-element design. It is checking the common practical result.

### Electrically short antennas: the price of being compact

An electrically short antenna is physically smaller than ideal resonance would suggest.

That saves space.
It does **not** come free.

Short antennas usually suffer from:

- lower radiation resistance
- higher reactance
- higher current in loss-producing parts
- narrower bandwidth
- reduced efficiency if losses are not controlled

This is why so many E9D questions revolve around loading, Q, and bandwidth.

### What a loading coil is doing

A short antenna is usually **capacitive** at the feed point.

A **loading coil** adds inductive reactance to cancel that capacitive reactance and bring the antenna to resonance.

That is the whole job:

**short antenna capacitance + loading coil inductance → resonance**

### Best loading-coil position

For a short whip, the most efficient place for a loading coil is **near the center of the vertical radiator**.

Why? Because center loading keeps current distributed over more of the radiator.

Compare the usual options:

- **base loading**: easiest mechanically, but poorest current distribution
- **center loading**: better current distribution and better efficiency
- **top loading**: usually best current distribution, but often implemented as a capacity hat rather than a literal loading coil

The exam answer for loading-coil location is **near the center**.

### Coil Q and efficiency

A loading coil should have a **high ratio of reactance to resistance**.

That is just another way of saying **high Q**.

Why do you want that?

Because the coil’s resistance is loss resistance. A coil with too much resistance wastes power as heat.

So for loading coils:

- high Q → lower loss → better efficiency
- low Q → higher loss → worse efficiency

### Q and bandwidth always pull in opposite directions

This relationship shows up repeatedly in E9D:

**higher Q → narrower bandwidth**

That means if you use loading coils to resonate an electrically short antenna, the **SWR bandwidth decreases**.

This is why compact HF antennas often need retuning across even modest frequency changes.

The antenna may be resonant, but it is usually very sharp.

### Top loading improves efficiency

**Top loading** improves the radiation efficiency of a short vertical by increasing current over more of the vertical radiator and reducing how much inductance is needed in the loading coil.

Less required inductance usually means less loss.

So top loading is one of the classic ways to make a short vertical less bad.

That is often what short-antenna work comes down to: not perfection, just making the unavoidable compromises hurt less.

### Radiation resistance falls as the antenna becomes electrically smaller

For a short base-fed whip, radiation resistance decreases as the operating frequency goes below the antenna’s resonant frequency.

A simple way to think about it is this:

- lower frequency means longer wavelength
- same whip is now a smaller fraction of a wavelength
- smaller electrical size means lower radiation resistance

And lower radiation resistance makes loss resistance more damaging.

That is why short antennas become harder to make efficient as frequency drops.

### Putting E9D together

E9D is the “there are no free lunches” section of the subelement.

The big ideas are:

- dish gain rises 6 dB when frequency doubles
- crossed Yagis with 90° phasing produce circular polarization
- Yagi driven element is about 1/2 λ
- reflector and directors are longer/shorter than resonance to control phase
- short antennas need loading because they are capacitive
- center loading is more efficient than base loading
- high-Q loading coils improve efficiency but narrow bandwidth
- top loading improves short-vertical efficiency
- radiation resistance drops as the antenna becomes electrically smaller

---

## Group E9E — Matching systems and feed arrangements

This group is really about one question:

**How do we make a real antenna and a real feed line work together?**

### Why matching exists

Maximum power transfer and minimum reflection happen when the impedance presented to the line matches the line’s characteristic impedance.

But antennas rarely land exactly where you want them.

So we use matching systems to transform impedance and sometimes cancel reactance.

The Extra pool expects you to recognize several standard systems by description.

### Gamma match

A **gamma match** is an unbalanced matching system often used with Yagis or grounded structures.

Its key features are:

- the coax shield connects to the center or boom side of the driven element system
- the center conductor connects partway out along one side through the gamma rod arrangement
- a **series capacitor** is used to cancel unwanted inductive reactance introduced by the gamma structure

Two major uses show up in the exam:

1. matching a Yagi to coax
2. **shunt-feeding a grounded tower at its base**

That second use is especially important. A grounded tower cannot simply be broken open like an insulated base-fed radiator. The gamma arrangement creates a feed method without isolating the whole tower from ground.

### Beta or hairpin match

A **beta match**, also called a **hairpin match**, is a balanced matching method used with Yagi driven elements.

The exam points to remember are:

- the driven element must be **insulated from the boom**
- the driven element should present a **capacitive** feed point impedance
- the hairpin section adds **inductive reactance** to cancel that capacitance

So the beta match is basically the balanced opposite of “this antenna is a little short and capacitive; let’s add inductive reactance right at the feed point.”

### Stub match

A **stub match** uses a short length of transmission line connected in parallel with the feed line near the feed point.

The stub can be open or shorted, and its electrical length is chosen so its susceptance cancels the undesired reactive part of the load.

This is one of the places where transmission line behavior and antenna matching overlap directly.

### Quarter-wave transformer

A quarter-wave matching section, sometimes called a **Q-section**, is one of the cleanest matching ideas in RF.

Its characteristic impedance should be:

**Zt = √(Z1 × Z2)**

So to match 100 Ω to 50 Ω:

**Zt = √(100 × 50) = √5000 = 70.7 Ω**

The practical line choice is **75 Ω**.

That is exactly the E9E06 style of problem.

### Reflection coefficient: the basic measure of mismatch

The parameter that directly describes the interaction of a load and transmission line is the **reflection coefficient**, usually written **Γ**.

**Γ = (ZL - Z0) / (ZL + Z0)**

What it tells you:

- Γ = 0 → perfect match
- |Γ| close to 1 → strong reflection
- open circuit and short circuit are extreme mismatch cases

SWR is derived from the magnitude of the reflection coefficient:

**SWR = (1 + |Γ|) / (1 - |Γ|)**

So if you understand reflection coefficient, SWR becomes much easier to interpret.

### Wilkinson divider

A **Wilkinson divider** is used to divide power equally between two loads while maintaining the correct input impedance and good isolation between the outputs.

For the exam, remember the practical description:

- equal power split
- two 50-ohm loads
- 50-ohm input impedance maintained
- good isolation between output ports

It is a power divider, not a frequency divider.

### Phasing lines and multiple driven elements

When multiple driven elements are connected through **phasing lines**, the purpose is to **control the antenna’s radiation pattern**.

That control can be used to:

- favor one direction
- suppress another
- create an array pattern
- steer or shape the main lobe

This is another place where E9 reminds you that current phase is one of the main tools of antenna engineering.

### Putting E9E together

The important ideas are:

- gamma match works well with grounded or boom-connected systems
- the gamma capacitor cancels unwanted inductive reactance
- beta/hairpin match needs a capacitive driven element and boom isolation
- stub matches use transmission-line sections in parallel
- quarter-wave transformer impedance is the geometric mean
- reflection coefficient directly describes mismatch
- Wilkinson dividers split power while holding the right impedance
- phasing lines are used to shape the pattern of multiple driven elements

---

## Group E9F — Transmission line behavior and impedance transformation

This group is where feed lines stop being mere cables and become circuit elements.

### Velocity factor: why waves travel slower in real lines

The **velocity factor** of a transmission line is:

**wave velocity in the line / speed of light in vacuum**

So it is always less than or equal to 1.

Typical examples:

- solid polyethylene coax: about **0.66**
- foam dielectric coax: often around **0.8**
- open-wire or air-spaced line: close to **1.0**

The main thing that determines velocity factor is the **dielectric material**.

That makes sense physically. The electromagnetic field interacts with the dielectric, and that slows propagation.

### Electrical length vs. physical length

Because waves move more slowly in coax than in free space, a piece of coax is **electrically longer** than its physical length.

If you want a line that is electrically a quarter wavelength long, the physical line must be shorter by the velocity factor:

**physical length = free-space electrical length × VF**

That is why line sections used as stubs or transformers must be cut with velocity factor in mind.

### Example: half-wave air-insulated line at 14.10 MHz

Free-space wavelength at 14.10 MHz is about:

**300 / 14.10 ≈ 21.28 meters**

Half of that is:

**10.64 meters**

For an air-insulated parallel-conductor line, the velocity factor is near 1, so the physical length is still about **10.6 meters**.

That is the logic behind E9F06.

### Why parallel conductor line often has lower loss than coax

Compared with coax that uses a plastic dielectric, parallel-conductor line usually has **lower loss**.

Why?

- much of the dielectric is air
- dielectric loss is lower
- conductor geometry is favorable
- high-impedance lines carry less current for a given power

That is why open-wire and ladder line remain attractive for some HF applications even though they are less convenient mechanically.

### Foam dielectric vs. solid dielectric coax

If all other parameters are the same, **foam dielectric coax** generally has:

- **higher velocity factor**
- **lower loss per unit length**
- **lower maximum safe operating voltage**

That combination appears directly in the question pool.

### Half-wave line behavior

A **1/2-wavelength transmission line** repeats the load impedance at its input.

So if the far end is shorted, the input also looks like a short:

- short at load → low impedance at input

That is the E9F04 idea.

### Quarter-wave line behavior

A **1/4-wavelength line** inverts impedance.

That means:

- short at load → open at input
- open at load → short at input

That is why shorted and open quarter-wave stubs are so useful in RF design.

### Short stubs below a quarter wavelength

For lengths shorter than λ/4:

- a **shorted** stub looks **inductive**
- an **open** stub looks **capacitive**

At **1/8 wavelength**, those are the classic exam answers:

- shorted λ/8 line → **inductive reactance**
- open λ/8 line → **capacitive reactance**

This is another example of feed line behaving like a reactive component.

### Microstrip

**Microstrip** is a printed transmission line made from a conductor trace above a ground plane on a dielectric substrate.

It is widely used at VHF, UHF, and microwave frequencies because a PCB trace can be designed for a controlled impedance.

So microstrip is not tiny coax and not shielding material. It is a **precision transmission line geometry built on a circuit board**.

### Putting E9F together

This group is all about treating line length as an electrical property, not just a mechanical one.

Remember:

- velocity factor is wave speed divided by c
- dielectric material mainly sets velocity factor
- coax is electrically longer than its physical length
- open-wire line usually has lower loss than plastic-dielectric coax
- foam dielectric coax has higher VF, lower loss, and lower breakdown voltage
- λ/2 line repeats the load
- λ/4 line inverts open and short conditions
- shorted stubs below λ/4 look inductive
- open stubs below λ/4 look capacitive
- microstrip is a controlled-impedance PCB transmission line

---

## Group E9G — Smith chart basics

The Smith chart looks intimidating until you realize what it is:

**a graphical calculator for transmission lines and complex impedance.**

### What the Smith chart is used for

A Smith chart is commonly used to find:

- impedance along a transmission line
- SWR relationships
- matching-stub length and location
- normalized impedance and admittance transformations

It is not an antenna pattern plot and not a propagation chart.

### The coordinate system: resistance circles and reactance arcs

A Smith chart is built from two families of curves:

- **resistance circles**
- **reactance arcs**

That is the most important visual fact to recognize.

Every point on the chart represents a complex impedance.

- points above the horizontal axis are **inductive**
- points below are **capacitive**
- points on the horizontal axis are **purely resistive**

The only straight line on the chart is the **resistance axis** — the horizontal line through the center.

The outer boundary where the reactance arcs terminate is called the **reactance axis** in the exam figure terminology.

### Normalization: why the center becomes 1 + j0

A Smith chart is **normalized** to the line characteristic impedance.

That means you divide impedance by **Z0**.

So in a 50-ohm system:

- 50 + j0 Ω becomes **1 + j0**
- 25 + j0 Ω becomes **0.5 + j0**
- 100 + j0 Ω becomes **2 + j0**

That is why the chart center represents a perfect match.

The same chart can be used for 50-ohm, 75-ohm, or other systems because you simply renormalize the impedances.

### Constant-SWR circles

A third family of circles often emphasized in matching work is the **constant-SWR circle**.

Once a load is plotted, moving along the transmission line moves you around a constant-SWR circle.

That gives you a graphical way to see what happens to impedance as you move toward the generator or toward the load.

The center of the chart is the special point where:

- normalized impedance = 1 + j0
- reflection coefficient = 0
- SWR = 1:1

Every matching process is, in a sense, trying to move the operating point to the center.

### Wavelength scales

The outer scales on a Smith chart are calibrated in **fractions of transmission line electrical wavelength**.

That is an important phrase.

Not free-space wavelength of the antenna.
Not “frequency units.”

Electrical wavelength along the line.

One complete revolution around the chart corresponds to **1/2 wavelength** of transmission line.

### Practical Smith-chart workflow

You do not need to become a chart artist for the exam. But it helps to understand the usual flow:

1. normalize the load impedance
2. plot the point
3. follow the constant-SWR circle toward generator or load
4. read transformed impedance at the new position
5. choose stub length or line length to bring the point to the center

That is why the Smith chart is so useful for stub-matching problems. It turns algebra into geometry.

### Putting E9G together

The main points are:

- Smith charts are used for transmission line impedance work
- they are built from resistance circles and reactance arcs
- the horizontal line is the resistance axis
- the chart is normalized to Z0
- the center is the matched condition
- constant-SWR circles show movement along a mismatched line
- wavelength scales are in fractions of transmission line electrical wavelength

---

## Group E9H — Receiving antennas and direction finding

This group shifts from “how much can I radiate?” to a different question:

**How well can I hear what I want while rejecting what I do not want?**

That difference matters especially on the low bands.

### Low-band receiving antennas care more about directivity than efficiency

On 160 and 80 meters, atmospheric noise is usually so high that small receiving-antenna losses are often less important than **directivity**.

That means a receive antenna can be worthwhile even if it is not highly efficient, provided it gives you better rejection of:

- local noise
- atmospheric noise from unwanted directions
- interfering stations

This is a very different mindset from transmit-antenna design.

### Beverage antenna

A **Beverage antenna** is a long, low, traveling-wave receiving antenna.

Important exam facts:

- it should be **at least one wavelength long** for good performance at the design frequency
- it is typically mounted low to the ground
- it uses a **termination resistor**
- the termination makes the pattern **unidirectional**

Without proper termination, the wave reflects from the far end and the pattern becomes less directional.

With the proper termination, the reverse-traveling energy is absorbed and the preferred receiving direction becomes much cleaner.

### How to judge Beverage termination

The exam point here is slightly unusual: the correct terminating resistance is indicated by **minimum variation in SWR over the desired frequency range**.

In other words, proper termination makes the antenna behave more like a traveling-wave system and less like a resonant line with strong standing-wave behavior.

### Receiving directivity factor (RDF)

**Receiving Directivity Factor** is a measure of how much the antenna favors its best direction compared with its average response over the useful hemisphere around it.

The short version is:

- higher RDF = better discrimination against unwanted noise and signals

That is why RDF is such a useful comparison tool for low-band receiving antennas.

It captures the idea that on receive, pattern quality often matters more than raw gain.

### Small loop direction-finding antennas

A small wire loop responds mainly to the magnetic field and produces a pattern with **deep nulls**.

That makes it useful for direction finding because a null is often easier to identify precisely than a broad maximum.

But there is a catch.

A simple loop has a **bidirectional null pattern**.

That means the null occurs in two opposite directions, so you know the signal lies on a line, but you do not know which end of the line contains the source.

This is the classic **180-degree ambiguity**.

### Electrostatic shield on a DF loop

A small DF loop may be surrounded by an **electrostatic shield**.

The purpose is to reduce unwanted electric-field pickup from nearby objects and wiring.

That matters because electric-field pickup tends to fill in the loop’s nulls, making them less deep and less useful.

So the shield improves the loop’s direction-finding performance by preserving deeper nulls.

### Sense antenna

A **sense antenna** is used to resolve the loop’s 180-degree ambiguity.

It adds an omnidirectional component that combines with the loop response to create a **cardioid** pattern.

And that cardioid pattern has the exam feature you need to remember:

**a single null**

That single null is what makes a cardioid pattern useful for direction finding.

### Terminated receiving loops

A single-turn terminated loop such as a **pennant** antenna produces a **cardioid** pattern.

Again, the termination is what makes the pattern directional by absorbing energy from one side and preventing the pattern from being simply bidirectional.

### Increasing loop output voltage

For a multiple-turn receiving loop, output voltage increases by increasing:

- the **number of turns**
- the **enclosed area**

That makes physical sense. More turns and more area intercept more magnetic flux.

### Putting E9H together

The central idea of E9H is that receiving antennas are often judged by what they reject, not just by what they hear.

The key points are:

- on 160 and 80 meters, directivity often matters more than efficiency
- Beverage antennas are long, low, terminated, and directional
- proper Beverage termination is indicated by flat SWR behavior
- RDF is a measure of receive directivity performance
- small loops have bidirectional nulls
- electrostatic shielding improves null depth by reducing E-field pickup
- a sense antenna resolves the 180° ambiguity
- cardioid patterns are useful because they have a single null
- more loop turns or more area increases output voltage

---

## Final Summary

E9 is the subelement that ties together the radiator, the feed system, and the pattern you actually get on the air.

The most important ideas to hold onto are:

- **gain depends on reference**: dBi is referenced to isotropic, dBd to a dipole
- **ERP and EIRP** are power-accounting problems in dB
- **efficiency** is radiation resistance divided by total resistance
- **ground systems, soil, seawater, height, and terrain** all change real antenna performance
- **beamwidth, front-to-back, and front-to-side** are pattern-reading tools
- **gain does not create total power**; it redistributes it
- **phasing and spacing** control array patterns
- **folded dipoles, OCFDs, G5RVs, Zepps, and EDZs** are defined mainly by geometry and feed method
- **short antennas** are capacitive, need loading, and usually pay with bandwidth and efficiency
- **gamma, beta, stub, and quarter-wave sections** are matching tools with distinct jobs
- **transmission lines transform impedance** according to electrical length, not just physical length
- **velocity factor** comes from dielectric properties
- the **Smith chart** is a graphical way to solve line and matching problems
- good **receiving antennas** often win by rejecting noise and unwanted directions rather than by having impressive transmit-style gain numbers

If E7 taught you what RF circuit blocks do and E8 taught you what happens to the signal, E9 teaches you how the signal actually gets launched into space — and how the station hears it again on the way back.

That is why E9 feels so practical. It is the part of the Extra pool where theory meets aluminum, wire, dirt, and feed line.

---

*Extra-class exam: 50 questions, must pass with 37 or higher (74%). E9 contributes 8 questions.*
