# E2 — Operating Procedures

E2 is the Extra subelement that asks whether you understand how more advanced amateur operating actually works once you move beyond ordinary HF phone contacts.

At first it can feel like a grab bag: satellites, television, DX pileups, contest logging, APRS, meteor scatter, moonbounce, FT8, PACTOR, ALE, and remote stations all show up here. But the theme is consistent: **what operating method fits the system you are using, and what habits make that method work well?**

This subelement covers five groups: satellite operation (E2A), amateur television (E2B), contest/DX/remote/mesh practices (E2C), specialized digital operating methods including APRS and weak-signal work (E2D), and HF digital modes with error-correction concepts (E2E). The exam pulls 5 questions from a pool of 60.

The best way to study E2 is not to memorize mode names in isolation. Instead, connect each mode or procedure to its purpose:

- satellites require orbit awareness, frequency planning, and power discipline
- television modes trade bandwidth against image speed and quality
- contest and DX work depend on efficient operating procedure
- weak-signal digital modes are designed around specific propagation paths
- HF digital modes differ mainly in what they are optimized to do: chat, beaconing, file transfer, or automatic linking

Build that operating picture and the pool makes a lot more sense.

---

## Group E2A — Satellite operation and orbital basics

Amateur satellite questions are really about two things: **where the satellite is** and **how its transponder behaves**.

### Orbits, passes, and what “ascending” means

A satellite pass is described by the direction the spacecraft is moving across your sky.

An **ascending pass** is one in which the satellite is moving **from south to north**. A descending pass is the opposite.

That definition matters because tracking software, pass predictions, and operating notes often use those terms without explanation. The exam is checking that you can think in orbital terms rather than just “it came up over there somewhere.”

To predict where a satellite will be, tracking programs use **Keplerian elements**. These are simply the orbital parameters that define the satellite’s path. You do not need to derive them for the exam; you just need to know that they describe the orbit and allow software to calculate future passes.

One special case is the **geostationary satellite**. A geostationary satellite appears to stay in one position in the sky because its orbit matches Earth’s rotation. Most amateur satellites are not geostationary; they are low-Earth-orbit satellites that move noticeably during a pass. But the exam expects you to recognize the one that appears fixed.

### Satellite “mode” means uplink/downlink band pairing

In satellite work, the word **mode** does not mean FM versus SSB in the ordinary HF sense. Here it means the satellite’s **uplink and downlink frequency bands**.

Likewise, the letters in a satellite’s **mode designator** specify the **uplink and downlink frequency ranges**. That is the key idea to learn. The designator is telling you where you transmit and where you listen, not whether the satellite is polar-orbiting, geostationary, or linearly polarized.

A practical way to remember this: for a satellite contact you always need two frequencies in mind — one going up to the bird, one coming down from it. The mode designator summarizes that pair.

### Linear transponders: what they do and why inversion matters

A **linear transponder** acts like a wide, frequency-translating repeater in space. Instead of repeating only one channel, it relays a range of frequencies. That means multiple stations can use different parts of the passband at the same time.

Because it is passing a slice of spectrum rather than one fixed channel, a linear transponder can relay many kinds of signals that fit its passband: CW, SSB, SSTV, packet, PSK, and other narrow enough signals. The pool treats this broadly: the key idea is that a linear transponder is not limited to a single narrow operating mode.

An **inverting linear transponder** reverses signal position within the passband. If your uplink signal is near one side of the transponder passband, your downlink will appear near the opposite side. This reversal also means that **USB on the uplink becomes LSB on the downlink, and vice versa**.

The exam goes one step deeper and asks how that happens. The answer is that the uplink is mixed with a local oscillator and the **difference product** is transmitted. In other words, the frequency conversion process itself causes the inversion.

That inversion also helps explain one more exam point: **Doppler shift is reduced** in an inverting system because the uplink and downlink shifts act in opposite directions. You do not need to do satellite Doppler math for this subelement, but you do need to understand the operating consequence.

### Why power discipline matters on linear satellites

One of the most important real-world satellite operating habits is to use only the uplink power you actually need.

On a satellite with a linear transponder, if you transmit too much **effective radiated power**, you do not just make yourself louder. You can push the transponder toward compression and effectively **reduce the downlink power available to everyone else**.

That is why good satellite operators are careful about ERP. The goal is not to dominate the bird. The goal is to be readable while leaving room for other users.

A useful practical rule is: on a linear satellite, use just enough uplink power to hear your own signal comfortably on the downlink, and no more.

### Antennas, polarization, and higher microwave bands

Satellite paths often suffer from **Faraday rotation** and, in some cases, **spin modulation** from the spacecraft itself. The standard antenna answer here is **circular polarization**. A circularly polarized antenna helps minimize fading and mismatch caused by changing polarization on the path.

The pool also expects you to know that **L band** and **S band** refer to the **23-centimeter and 13-centimeter amateur bands**. These names show up frequently in microwave and satellite work, so they are worth learning as a vocabulary item rather than trying to infer them on the fly.

### Store-and-forward satellites

Not every amateur satellite is strictly a real-time bent-pipe repeater. Some have **digital store-and-forward** capability. The purpose is straightforward: the satellite can **hold digital messages for later download**.

That means the message does not have to be delivered instantly while both stations are simultaneously in view. Think of it as message storage in orbit rather than immediate relay.

---

## Group E2B — Amateur television and SSTV basics

This group is easier once you separate **fast-scan television** from **slow-scan television**.

- **Fast-scan TV (FSTV)** is ordinary moving video, more like broadcast television.
- **Slow-scan TV (SSTV)** sends a still image slowly enough to fit through narrow amateur channels.

They solve different problems, so they use different techniques.

### Fast-scan TV: frames, fields, and interlacing

For NTSC fast-scan television, a frame contains **525 horizontal lines**. That number is a pure memory item, but it becomes easier to keep straight if you connect it to how analog television was built.

NTSC also uses **interlaced scanning**. Instead of drawing every line in one pass, the system first scans the **odd-numbered lines** and then scans the **even-numbered lines**. Those two fields combine to make one full frame.

The exam is not trying to turn you into a broadcast engineer here. It is testing whether you recognize how interlacing works: odd field, even field, full frame.

### Vestigial sideband: why TV does not send two full AM sidebands

Analog fast-scan TV uses **vestigial sideband**. That means **one complete sideband and only a portion of the other** are transmitted.

Why do this? Because it is a smart compromise. Vestigial sideband **reduces bandwidth while preserving good low-frequency video fidelity**. If you sent full double-sideband AM video, the occupied bandwidth would be larger than necessary. If you removed too much sideband information, picture quality would suffer. Vestigial sideband keeps enough of the second sideband to make the video work properly without taking the full bandwidth penalty.

That definition matters because the exam asks both what vestigial sideband is and why it is useful.

### Digital amateur TV: modulation and coding rate

Modern amateur digital television commonly uses **QAM** and **QPSK** in DVB-T systems. That is another vocabulary item worth learning directly.

The pool also asks about **coding rate**. A coding rate of **3/4** means that only three-quarters of the transmitted bit stream is payload data; the other quarter is **forward error correction** information. So if the question asks what 3/4 means, the clean answer is: **25% of the transmitted data is FEC overhead**.

That is an important operating idea beyond the exam. More error correction usually means better robustness, but it also means less net data throughput.

### Using ordinary TV receivers on 70 centimeters

One clever practical item in the pool is that commercial analog TV receivers could be used for amateur fast-scan TV on 70 centimeters by **transmitting on channels shared with cable TV**.

The point is not nostalgia for old cable-channel plans. It is that amateurs have often chosen frequency plans that match existing receiver hardware, because it makes equipment easier to obtain and use.

### Slow-scan TV: think in tones, not wide video channels

SSTV is completely different from fast-scan TV in bandwidth and operating style. A slow-scan picture is turned into audio-frequency tones that fit through an SSB transmitter and receiver chain.

That explains several exam answers at once.

In analog SSTV:

- **brightness is encoded by tone frequency**
- **color is sent sequentially, line by line**
- the **VIS code** identifies which SSTV mode is in use
- the receiving software starts a new line when it hears **specific tone frequencies**

This is worth understanding as a system instead of as four isolated facts.

The receiver is listening to an audio stream. Certain tones mean “this is the mode,” certain tones mark line timing, and the varying tone frequency carries picture intensity information. Once you understand that, the answers stop feeling arbitrary.

### SSTV over SSB and DRM-based decoding

Another easy-to-miss clue in the pool is that SSTV using the Digital Radio Mondiale protocol can be received and decoded with an **SSB receiver**.

That fits the same basic idea: these image systems often ride through a narrowband audio path. The SSB receiver is providing the audio/baseband signal that software then decodes.

---

## Group E2C — Contesting, DX procedure, remote control, logging, and mesh networking

This group is less about electronics and more about operating cleanly and efficiently.

### Remote stations: identification and latency

If you are a U.S.-licensed amateur operating a station by remote control and the remote transmitter is located in the United States, **no additional indicator is required** in your identification.

That is a common rule trap because operators often assume some extra suffix must be used. The exam answer is narrower and simpler: if the remote transmitter is still in the U.S., **no extra identifier is required**.

The group also expects you to know the word **latency**. Latency is the **delay between a control action and the corresponding change in the transmitted signal**.

That matters in real remote operating. If you click PTT, tune, or switch bands and the station responds a fraction of a second later, that delay is latency. It affects timing, especially in contesting, satellite work, and other fast-paced operating.

### ADIF, Cabrillo, LoTW, and QSL managers

Modern operating depends heavily on logging and confirmation systems, and E2 expects you to keep the main ones straight.

**ADIF** is the standard file format used for **exchanging amateur radio log data** between programs. Think of it as the general-purpose logbook interchange format.

**Cabrillo** is different. It is the standard format for **electronic contest log submissions**. If ADIF is the all-purpose notebook, Cabrillo is the contest sponsor’s official scoring form.

The **Logbook of The World (LoTW)** can confirm a wide range of contacts, including:

- domestic contacts such as special-event stations
- international contacts
- contacts used for awards such as Worked All States

So when the pool asks what kinds of contacts LoTW can confirm, the point is that it is broadly useful, not limited to one narrow category.

A **DX QSL manager** handles the receiving and sending of confirmations for a DX station. This is especially useful for rare entities, expeditions, or stations that would otherwise be swamped by direct QSL traffic.

### Contest operating: where activity is and where it usually is not

One convention worth learning exactly is that amateur radio contesting is **generally excluded from 30 meters**. The word “generally” matters. This is mostly an operating-practice and band-plan issue, but it is strong enough to be a standard exam answer.

On VHF/UHF contests, the highest concentration of SSB and CW activity is usually in the **weak-signal segment**, with much of it clustered near the **calling frequency**. That is how weak-signal operators naturally find one another: use the recognized activity area, then move as needed.

The pool is testing whether you understand that VHF/UHF weak-signal contesting does not happen primarily in repeater channels or some special “contest-only” segment at the top of the band.

### Split operation and DX pileups

DX questions in E2 are really questions about operating discipline.

A DX station often transmits on one frequency and listens on another — **split operation** — for several reasons at once:

- some responding stations may not be authorized to transmit on the DX station’s transmit frequency
- separating the callers from the DX station reduces interference at the DX station’s own transmit frequency
- the arrangement improves efficiency in a crowded pileup

This is a classic E2 pattern: when the correct answer is “all of these,” the real lesson is that the operating method solves multiple problems at once.

The correct way to call that DX station is usually simple: **send your full call sign once or twice**.

Not half your call. Not a long speech. Not the DX station’s call sign three times followed by phonetics and your biography. In a pileup, brevity wins. Full call, once or twice, at the right time.

### Mesh networking in amateur radio

Amateur radio mesh networks commonly use **frequencies shared with unlicensed wireless data services**. In practice this often means hardware and spectrum similar to ordinary Wi‑Fi systems, but operated within amateur rules and using amateur-oriented firmware.

The common hardware answer is a **wireless router running custom firmware**.

That is the point of the pool item: amateur mesh networking is not usually built from legacy packet TNCs on VHF. It is much more often built from repurposed wireless networking gear.

---

## Group E2D — Specialized digital modes, APRS, meteor scatter, and EME

This section makes much more sense when you think of each mode as a tool built for a specific path.

### Modes matched to unusual propagation paths

**MSK144** is designed for **meteor scatter** communication.

That makes sense because meteor scatter contacts depend on brief ionized trails left by meteors. The mode has to work quickly and efficiently in short bursts.

**Q65** is designed for **EME** — Earth-Moon-Earth, or moonbounce — where signals are extremely weak and the path is long and stable but punishing. The pool also asks how Q65 differs from JT65: a key distinction is that **multiple receive cycles are averaged**.

That averaging helps pull signals out of the noise over repeated sequences.

**JT65** is another weak-signal mode associated with very low signal levels. The important exam characteristic is that it can **decode very low signal-to-noise ratio signals**. Its modulation is **multitone AFSK**.

So if you need the simple memory chain:

- meteor scatter → **MSK144**
- very weak-signal legacy WSJT work → **JT65**
- EME → **Q65**

### EME operating procedure: synchronized alternating sequences

The pool also asks about **how** EME contacts are made, not just which mode is used. The key method is **time-synchronous transmissions alternating between stations**.

That is classic moonbounce procedure. One station transmits during one timed sequence while the other listens; then they swap. With such weak signals and such long paths, orderly timing matters.

### FT8/FT4 contest exchanges on VHF

On HF, people often think of FT8 exchanges as signal report and locator-style shorthand. In a **VHF contest**, the key exchanged information for FT8 or FT4 is the **grid square**.

That reflects what matters in VHF contest scoring: where the station is, not just how strong it was.

### APRS: tracking and packet relay in practice

**APRS** is the standard answer for **real-time tracking of balloons carrying amateur radio transmitters**. More broadly, APRS is used for position reporting, status messages, weather data, objects, and tactical information.

The protocol underneath APRS is **AX.25**.

When APRS beacon data is transmitted, it uses an **Unnumbered Information (UI)** packet frame. That fits APRS well because APRS is usually connectionless broadcast information rather than a formal connected packet session.

APRS data is relayed by **packet digipeaters**. That is another important system concept: APRS coverage depends on intermediate stations repeating packets, not on voice repeaters or digital voice systems.

The path notation can look cryptic if you have never seen it before. For example, **WIDE3-1** means **three digipeater hops are requested with one remaining**. In practical terms, the number before the hyphen identifies the requested path class, and the number after the hyphen shows how many retransmissions remain.

You do not need to become an APRS path-planning expert for the exam, but you should be able to read that notation well enough to understand what the packet is asking the network to do.

---

## Group E2E — HF digital modes, synchronization, and choosing the right tool

Once you get past the alphabet soup, this group is mostly about why one digital mode is chosen over another.

### Basic HF digital modulation ideas

For the question pool, the digital modulation type to know for data emissions below 30 MHz is **FSK**.

The pool also asks the difference between **direct FSK** and **audio FSK**. In **direct FSK**, the transmitter’s **VFO is modulated directly**. With audio FSK, you are generally generating audio tones and feeding them through an SSB transmitter path instead.

That distinction matters because it explains why the signal is being shifted at different points in the transmit chain.

### WSJT-X timing: the clock matters

WSJT-X modes depend heavily on time synchronization. The exam answer is simple and important: transmit/receive timing is synchronized by **synchronizing the computer clocks**.

That is not a minor implementation detail. If your system clock is off, your FT8, FT4, Q65, and related decoders will start missing decodes or transmitting in the wrong window.

### FT4, FT8, and FST4

The “4” in **FT4** refers to **four-tone continuous-phase frequency shift keying**.

For **FT8**, the major memory item is the transmission cycle length: **15 seconds**.

FT8 also has the **narrowest bandwidth** among the listed modes in that pool question. That is part of why it performs so well for weak-signal structured exchanges.

**FST4** is a separate WSJT-X family mode with three characteristics the exam wants you to connect together:

- it uses **four-tone Gaussian frequency shift keying**
- it supports **variable transmit/receive periods**
- it offers **multiple tone spacings**

The test presents those as separate facts and then expects you to realize they are all true.

### Keyboard chat, propagation beacons, and file transfer

Different HF digital modes exist because operators want different things out of the circuit.

**WSPR** is not a keyboard-to-keyboard mode. It is a propagation-reporting and beaconing mode. That is why it is such a common exam answer when the question asks which mode is *not* used for conversational operation.

**PSK31** uses **variable-length character coding**. That is part of what made it efficient and attractive for keyboard chat: common characters can be sent compactly.

**PACTOR** is the listed HF digital mode that can be used to **transfer binary files**.

Under clear communication conditions, **PACTOR IV** has the **highest data throughput** among the listed choices. That fits its real purpose: it is designed for efficient data transfer rather than ultra-weak-signal minimal exchanges.

A good operating mindset for this part of E2 is:

- **FT8/FT4/Q65/JT65**: structured, synchronized weak-signal work
- **WSPR**: propagation beaconing
- **PSK31**: keyboard chat efficiency
- **PACTOR**: robust file/data transfer

### ALE: automatic link establishment

**ALE** — Automatic Link Establishment — is another good example of a mode designed around procedure.

ALE stations establish contact by **constantly scanning a list of frequencies**, and the radio activates when the designated call sign is heard.

That means the system is doing the listening and channel hunting for you. Instead of sitting on one fixed frequency waiting, the radios coordinate across a channel list until the link is established.

---

## Putting the whole subelement together

E2 feels broad because it covers many different operating styles, but most of it reduces to a few repeatable ideas.

### 1. Know what problem the mode was built to solve

- satellite modes solve moving-platform, split-frequency, limited-power problems
- SSTV solves still-image transmission in narrow bandwidth
- MSK144 solves brief meteor-scatter bursts
- Q65 and JT65 solve extremely weak-signal paths
- WSPR solves propagation reporting
- PACTOR solves file transfer

If you remember the job each mode is for, the names stop blurring together.

### 2. Advanced operating is often about discipline, not brute force

On a linear satellite, too much ERP hurts other users. In a DX pileup, too many words hurt your chances. In a remote station, latency changes your timing. In APRS, path settings matter. E2 rewards operators who work efficiently rather than noisily.

### 3. Much of E2 is vocabulary with a system behind it

- **ADIF** = general log exchange
- **Cabrillo** = contest log submission
- **LoTW** = contact confirmation system
- **AX.25** = APRS protocol basis
- **VIS** = SSTV mode identifier
- **Keplerian elements** = orbit-defining parameters
- **latency** = control-to-signal delay

If you tie each term to its system, memorization becomes much easier.

### 4. Timing matters in modern digital operation

Computer clock sync for WSJT-X, alternating timed periods for EME, line-sync tones in SSTV, and interlaced fields in television all point to the same thing: modern operating procedures depend on timing being correct.

---

## Final Summary

E2 is the Extra subelement about using the right operating method for the right situation.

You should come away knowing that:

- satellite operating depends on orbit awareness, transponder behavior, polarization, and careful power control
- amateur television splits into wideband fast-scan video and narrowband slow-scan still-image techniques
- remote, contest, and DX operating reward efficient procedure and correct logging formats
- APRS, meteor scatter, and EME each use specialized modes and relay methods matched to their operating environment
- HF digital modes differ mainly in synchronization, bandwidth, throughput, and intended use

If you study E2 as a long list of acronyms, it is miserable. If you study it as **how experienced operators match tools to paths and procedures to goals**, it becomes much more logical — and much easier to remember on the exam.

---

*Extra-class exam: 50 questions, must pass with 37 or higher (74%). E2 contributes 5 questions.*
