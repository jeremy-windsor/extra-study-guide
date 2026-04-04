# E3 — Radio Wave Propagation

E3 is where the Extra exam stops treating propagation like a convenient background condition and starts asking you to understand *why* signals travel the way they do.

Some of the questions are straightforward fact checks: when Sporadic-E is most likely, what a rising K-index means, or which flare class is strongest. Others are about operating judgment: when to move to a lower band, why vertical polarization is favored for ground wave, why satellite operators care about perigee, or what kind of path suffers during geomagnetic disturbance.

This subelement covers three groups: propagation mechanisms and operating technique (E3A), ionospheric path types and special propagation modes (E3B), and solar/space-weather effects with horizon and prediction tools (E3C). The exam pulls 3 questions from a pool of 39.

The best way to study E3 is not to memorize a pile of isolated terms. Instead, connect each propagation mode to the physical situation that creates it:

- Earth-Moon-Earth depends on geometry and enormous path loss
- meteor scatter depends on brief ionized trails in the E region
- aurora depends on geomagnetic disturbance
- Sporadic-E depends on seasonal ionized patches in the E layer
- tropospheric ducting depends on lower-atmosphere conditions, especially over water
- HF long-distance propagation depends on ionospheric refraction, takeoff angle, time of day, and solar conditions

Once you see the pattern, the subelement becomes much easier.

---

## Group E3A — Electromagnetic waves, EME, meteor scatter, tropospheric ducting, and aurora

### Start with the wave itself

Radio is an electromagnetic wave. For the exam, there are three basic geometric facts to know:

- the **electric field** and **magnetic field** are at right angles to each other
- the wave travels at right angles to both of those fields
- in a medium, wave speed is determined by the **index of refraction**

That means the fields are not pointing in the same direction the wave is going. They are transverse. If you picture the wave moving forward, the electric and magnetic fields are each oscillating sideways, perpendicular to the direction of travel and perpendicular to one another.

That basic geometry helps explain polarization. A **circularly polarized** wave is one in which the field orientation rotates as the wave travels. The wave is not moving in a circle through space; rather, the electric and magnetic fields rotate through one RF cycle.

### EME: moonbounce is mostly a path-loss problem

Earth-Moon-Earth communication is exactly what it sounds like: transmit from Earth, bounce the signal off the Moon, and receive the return on Earth.

The first thing to understand is scale. The path is extremely long and extremely lossy. Even so, two stations can communicate over roughly **12,000 miles along Earth’s surface** if the Moon is visible to both of them. That is not because the signal hugs the Earth; it is because the Moon is acting as the common reflector for two widely separated stations.

When scheduling EME, operators prefer the Moon at **perigee** because that is when it is closest to Earth and the path loss is lowest. The difference is not magic, just geometry: a shorter path loses less signal.

One distinct EME effect is **libration fading**, which sounds like a fluttery, irregular fading of the signal. The Moon is not a perfect still mirror. Its surface and apparent motion cause small phase and path differences that make the returned signal sound rough or rapidly fluttery, especially on CW.

The practical lesson: EME is a weak-signal mode where every dB matters. Operators care about lunar distance, antenna gain, polarization, accurate frequency control, and careful timing because the path is brutal.

### When darkness lowers the MUF, move down in frequency

One of the most practical HF operating questions in E3 asks what to do when the **maximum usable frequency (MUF)** for a path drops due to darkness.

The answer is simple: **switch to a lower HF band**.

Why? Because if the ionosphere will no longer refract the higher frequency back to Earth, that higher band stops working for that path. Lower frequencies continue to refract under weaker ionization, so you move downward to stay under the MUF.

This is a core propagation habit:

- daytime ionization often supports higher frequencies
- nighttime ionization usually lowers the MUF
- when the band “goes long” or dies after sunset, try a lower band

### Meteor scatter: brief mirrors in the E region

Meteor scatter works because a meteor entering the atmosphere leaves behind a brief **ionized trail**. For the exam, the important region is the **E region**.

That trail can reflect or scatter VHF signals for a fraction of a second to a few seconds, sometimes longer for stronger events. Because the openings are short and the reflections are not stable like normal HF ionospheric paths, meteor-scatter communication favors fast, highly structured weak-signal digital modes.

The frequency range most suited to meteor scatter in the question pool is **28 MHz to 148 MHz**. That should fit your intuition: this is mainly a low-VHF and upper-HF/6-meter-to-2-meter style phenomenon, not a normal HF or UHF operating method.

The practical picture is this: for a brief moment, the meteor trail becomes a usable reflector. Operators transmit in timed bursts, hoping enough of the message gets through during those short ionized events.

### Tropospheric ducting: microwave range beyond line of sight

Not all unusual propagation is ionospheric. **Tropospheric ducting** happens in the lower atmosphere, typically when temperature and humidity create layers that bend and trap radio waves.

For the exam, two facts matter:

- ducts capable of propagating microwave signals often form over **large bodies of water**
- a typical tropospheric duct range is about **100 to 300 miles**

That makes sense in practice. Large water surfaces help create stable temperature inversions and moisture gradients, especially along coasts. Those conditions can form ducts that carry VHF and microwave signals much farther than normal line-of-sight would suggest.

This is why microwave and VHF operators watch marine weather, inversion forecasts, and coastal conditions. A band that is usually local can suddenly open for surprisingly long distances.

### Auroral propagation: distorted paths from geomagnetic storms

**Auroral propagation** is associated with **severe geomagnetic storms**. Charged particles interacting with Earth’s magnetic field create ionization in the auroral regions, and signals can scatter from that disturbed area.

Auroral signals are distinctive. They often sound rough, hissy, or distorted rather than clean and stable. Because of that, **CW** is usually the best emission mode among the listed choices. CW tolerates distortion better than voice.

The exam point is not just that aurora exists. It is that this is a disturbed, noisy, unstable path. If you try to imagine auroral propagation as an ordinary clean VHF reflection, the questions stop making sense.

---

## Group E3B — TEP, long-path, ground wave, Sporadic-E, ordinary/extraordinary waves, and chordal hop

### Transequatorial propagation: a special low-latitude path

**Transequatorial propagation (TEP)** occurs on paths that cross the geomagnetic equator, typically over a path roughly **perpendicular to the geomagnetic equator** rather than parallel to it.

The question pool emphasizes a few operating facts:

- TEP is most likely between stations about **2,000 to 3,000 miles apart**
- the approximate maximum range is about **5,000 miles**
- it is most likely in the **afternoon or early evening**

TEP is most often discussed on 6 meters and 10 meters, where operators in the northern and southern hemispheres can suddenly find surprisingly strong contacts across low-latitude paths.

The practical takeaway is that TEP is not random “DX magic.” It has a geographic preference, a timing preference, and a distance range. If you remember those three ideas, the exam questions line up.

### Ordinary and extraordinary waves

When a radio wave enters the ionosphere, the magnetic field and plasma properties can split it into two independently propagating components called the **ordinary** and **extraordinary** waves.

For the exam, the important definition is that they are **independently propagating, elliptically polarized waves created in the ionosphere**.

You do not need a full plasma-physics derivation here. The useful point is that the ionosphere is not just a simple mirror. It is a magnetized medium that can treat different components of the wave differently.

### Darkness helps 160 meters, and long-path is common on 40 and 20

On **160 meters**, long-distance propagation is most likely on a path **entirely in darkness**.

That fits what you already know about the D layer. Daytime absorption is a serious enemy on the lower HF bands, especially 160 and 80 meters. Once darkness removes much of that D-layer absorption, the low bands often become dramatically better for long-distance work.

The exam also expects you to know that **long-path propagation** is most frequent on **40 meters and 20 meters**.

Long-path means the signal reaches the distant station by going the long way around the Earth instead of the short great-circle route. It is not the normal assumption, but on certain bands and under the right conditions it becomes practical enough to be a recognizable operating pattern.

### Lower takeoff angle means longer hops

If you lower the transmitted **elevation angle** for ionospheric HF skip, the distance covered by each hop increases.

This is intuitive if you picture the geometry. A low-angle ray travels farther before it comes back down. A high-angle ray returns sooner and covers less ground per hop.

That is why low-angle antennas and low-angle radiation are valuable for DX, while high-angle radiation is valuable for shorter skip paths like NVIS.

A clean memory shortcut:

- **low angle = long hop = better for DX**
- **high angle = short hop = better for closer-in ionospheric coverage**

### Ground wave: lower frequencies go farther, and vertical wins

**Ground-wave propagation** hugs the Earth’s surface rather than being refracted by the ionosphere. For the exam, two linked ideas matter:

- as frequency increases, the maximum ground-wave range **decreases**
- ground-wave propagation favors **vertical polarization**

This is why AM broadcast and LF/MF services use vertical antennas so often. Vertical polarization couples effectively to the surface wave, while horizontal polarization is more heavily absorbed by the ground.

This also explains why low-frequency signals can cover impressive distances by ground wave, while higher frequencies tend to lose that advantage.

### Sporadic-E: seasonal and daytime-friendly

**Sporadic-E** is caused by dense, patchy ionization in the E layer. It is called “sporadic” because it is not steady or predictable like ordinary F-layer propagation, but it still has recognizable patterns.

The two exam facts to know are:

- it is most likely around the **solstices**, especially the **summer solstice**
- it is most likely between **sunrise and sunset**

That matches real operating experience on 10 meters and especially 6 meters. A band that seems dead can suddenly open with strong short-to-medium-distance single-hop paths.

Think of Sporadic-E as a temporary, unusually dense E-layer patch that makes VHF and upper-HF signals behave more like HF skip.

### Chordal-hop propagation: skipping without touching the ground

In ordinary multi-hop ionospheric propagation, the signal goes up to the ionosphere, comes back down to Earth, reflects, then goes back up again.

In **chordal-hop propagation**, the signal undergoes **successive ionospheric refractions without an intermediate ground reflection**.

That matters because every ground reflection costs energy. By avoiding the ground bounce, chordal-hop propagation generally produces **less loss** than ordinary multi-hop paths that use Earth as a reflector.

This is one of those questions where the definition and the operating consequence reinforce each other:

- chordal hop = no intermediate ground reflection
- therefore less loss than ordinary multi-hop with ground reflections

---

## Group E3C — Solar flares, geomagnetic indices, radio horizon, propagation reports, and prediction tools

### Solar flares and blackouts

Short-term radio blackouts are caused by **solar flares**.

That is an important distinction. Flares can produce sudden ionospheric disturbances very quickly, especially on the sunlit side of Earth. A band that was fine a few minutes ago can suddenly become noisy or go flat.

The flare intensity scale item to know is simple: **Class X** indicates the greatest flare intensity among the listed answers. If you are choosing between A, M, and X, X is the big one.

The exam also uses the term **G5** for an extreme geomagnetic storm. That is a space-weather storm classification, not a flare class. Keep those categories separate:

- **X-class** = strong solar flare
- **G5** = extreme geomagnetic storm

### A-index, K-index, and why disturbed geomagnetic conditions matter

A rising **A-index** or **K-index** indicates **increasing disturbance of the geomagnetic field**.

That is usually bad news for stable HF propagation, especially on polar paths. One specific exam consequence is that paths **through the auroral oval** are likely to experience high levels of absorption when A or K is elevated.

That makes sense: the auroral region is where geomagnetic disturbance is especially active, so signals crossing it often suffer badly during storms.

The operating habit here is simple:

- low A/K = generally quieter geomagnetic conditions
- rising A/K = more disturbance, more absorption, more unstable paths
- polar and auroral paths are often the first to suffer

### Bz: the north-south component that operators watch

The value of **Bz** refers to the **north-south strength of the interplanetary magnetic field**.

The orientation that increases the likelihood of disturbed conditions is **southward Bz**.

Why does this matter? Because southward Bz couples more effectively with Earth’s magnetic field, allowing solar wind energy to drive geomagnetic disturbance more strongly. You do not need to work the magnetohydrodynamics for the exam; just remember:

- **southward Bz = greater chance of geomagnetic trouble**

### The radio horizon is farther than the optical horizon

For VHF and UHF, the **radio horizon** is approximately **15 percent farther** than the geographic horizon.

That is because the atmosphere slightly refracts radio waves, bending them enough to extend line-of-sight range a bit beyond what pure geometry would predict.

This is a very practical concept. When people say VHF is “line of sight,” that is mostly true, but real radio line of sight is usually a little better than visual line of sight.

### Propagation reporting networks and what they actually report

Amateur radio propagation reporting networks do not primarily report sunspot counts or magnetic declination. They report actual received **digital-mode and CW signals**.

That makes these systems useful because they are based on observed propagation, not just predicted conditions. If a reporting network shows FT8 or WSPR spots between two areas, you know the path is working for at least those kinds of signals.

This is one reason modern operators can verify openings in near real time instead of relying only on solar charts and guesswork.

### Solar indicators and software tools

The **304A solar parameter** measures **UV emissions at 304 angstroms**, and it correlates with the solar flux index. For the exam, this is mainly a vocabulary item, but it fits the broader theme that operators use several solar indicators, not just sunspot number.

**VOACAP** is software that models **HF propagation**.

That is worth remembering because it gives the exam a concrete name for propagation prediction software. VOACAP is about estimating likely HF path performance based on band, path, time, season, and solar conditions.

### Sudden broadband HF noise usually points to solar disturbance

If radio background noise suddenly rises across a large portion of the HF spectrum, that likely indicates a **solar flare or a coronal mass ejection impact**.

This is a good practical clue. If one band is noisy, that might just be local interference. But if a wide swath of HF suddenly changes character at once, think space weather.

---

## Putting the whole subelement together

E3 works best when you organize it by *what kind of medium is controlling the path*.

### 1. Free-space and geometry problems
These include electromagnetic-wave orientation and EME. The important ideas are field geometry, polarization, and path length.

### 2. Ionospheric refraction and scattering
These include ordinary HF skip, TEP, Sporadic-E, meteor scatter, aurora, and chordal hop. The key questions are which layer or region is involved, what time or season favors it, and what operating style fits it.

### 3. Tropospheric and surface-wave effects
These include tropospheric ducting, radio horizon extension, and ground-wave propagation. These are not classic ionospheric modes, so time-of-day and weather structure often matter more than solar conditions.

### 4. Solar and geomagnetic control of propagation
These include solar flares, A/K index, Bz orientation, auroral absorption, and prediction/reporting tools such as VOACAP and propagation spotting networks.

If you sort E3 this way, the facts stop feeling random.

---

## Final Summary

E3 is the Extra propagation subelement, but it is really a subelement about *matching operating expectations to the physical path*.

You should come away knowing that:

- electromagnetic waves have electric and magnetic fields at right angles to each other and to the direction of travel
- EME works when both stations can see the Moon, favors perigee, and often shows fluttery libration fading
- meteor scatter uses E-region ionized trails and is mainly a VHF/upper-HF technique
- tropospheric ducting often forms over large bodies of water and can carry microwave signals 100 to 300 miles or more
- auroral propagation comes with geomagnetic storms and favors CW
- TEP, Sporadic-E, long-path, and chordal-hop each have recognizable distance, timing, and geometry patterns
- ground wave prefers vertical polarization and gets worse as frequency rises
- solar flares, geomagnetic indices, Bz orientation, and auroral absorption all directly affect HF reliability
- propagation networks and tools like VOACAP help confirm and predict what the bands are likely to do

If you study E3 as a list of names, it is annoying. If you study it as a map of **what the wave is interacting with — the Moon, the ionosphere, the troposphere, the ground, or disturbed solar plasma —** it becomes much more logical and much easier to remember.

---

*Extra-class exam: 50 questions, must pass with 37 or higher (74%). E3 contributes 3 questions.*
