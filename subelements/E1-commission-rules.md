# E1 — Commission's Rules

Most of E1 is not about electronics at all. It is about operating legally, cleanly, and predictably under Part 97.

That can make the subelement feel scattered at first. One question is about sideband bandwidth at a band edge. The next is about satellites, then Volunteer Examiners, then whether a business-related message is allowed. But the underlying theme is consistent: **what privileges do amateurs have, what limits come with those privileges, and who is responsible when something goes wrong?**

This subelement covers six groups: operating standards and special band rules (E1A), station restrictions and special operations (E1B), digital and international rules (E1C), satellites and telecommand (E1D), the Volunteer Examiner system (E1E), and miscellaneous rule questions (E1F). The exam pulls 6 questions from a pool of 68.

The best way to study E1 is not to memorize isolated answers. Instead, learn the operating logic behind the rules:

- your transmitted **signal**, not just the displayed carrier, must stay inside the authorized segment
- special operating situations come with specific conditions
- amateurs must protect other services and certain protected locations
- a few narrow exceptions exist, but they stay narrow
- responsibility usually follows the control operator, the station licensee, or the administering VE

Build that mindset, and most E1 questions become much easier.

---

## Group E1A — Band edges, signal placement, and special operating situations

### The displayed frequency is not the entire signal

One of the most common E1 traps is forgetting that your radio may display a carrier or reference frequency, while the actual transmitted energy occupies a range above or below that point.

That matters most near **band edges**.

For **USB**, the energy extends **upward** from the displayed carrier frequency. For **LSB**, it extends **downward**. So a transmission can be illegal even when the number on the screen looks like it is still inside the band.

This leads to a simple rule:

- **USB near an upper band edge:** subtract the signal bandwidth from the upper edge
- **LSB near a lower band edge:** add the signal bandwidth to the lower edge

That is why a 3 kHz USB emission with a carrier at 14.348 MHz is not legal on 20 meters. The radio may display 14.348, but the top of the signal reaches about 14.351 MHz, which extends beyond the band edge.

The same logic explains why a properly adjusted LSB phone signal needs its displayed carrier roughly **3 kHz above the lower band edge** to keep the whole emission in-band. It also explains why an Extra operator may not answer an LSB CQ on 3.601 MHz if the lower edge of the phone segment is 3.600 MHz: the lower sideband components would spill below the authorized phone segment.

The exam likes this topic because it tests whether you are thinking about the **occupied bandwidth**, not just the dial reading.

### Data and sideband bandwidth still have to fit

The exact same principle applies to digital and data emissions.

If a band segment ends at a certain frequency, the highest legal carrier for a USB data signal is the segment edge minus the signal bandwidth. That is why a 2.8 kHz wide USB data signal in a segment ending at 14.150 MHz has a highest legal carrier of **14.1472 MHz**.

The operating habit to build is straightforward: whenever you are close to an edge, think in terms of **where the sidebands actually go**.

### 60 meters is channelized, so think in centers, not edges

Sixty meters is one of the places where normal "pick a frequency in the band" thinking does not fully apply.

For channelized 60-meter operation, a CW signal must be transmitted on the **center frequency of the channel**. The channel is treated as the basic operating unit. You are not simply free to slide around inside it the way you might on most HF allocations.

This is also why E1 asks about bandwidth on 60 meters separately from other HF bands. The details matter more there.

### LF and MF power limits are measured as EIRP, not transmitter output

On 2200 meters and 630 meters, the exam expects you to know the unusually low power limits and the fact that they are stated in **EIRP**:

- **2200 meters:** maximum **1 watt EIRP**
- **630 meters:** maximum **5 watts EIRP**, except for certain Alaska provisions

This is a rules concept, but it reflects real operating conditions. On those bands, antennas are usually very inefficient, so the FCC regulates the radiated result rather than simply the transmitter's output power.

### Ships and aircraft require permission and proper control

If an amateur station is installed aboard a ship or aircraft, operation must be approved by the appropriate person in command:

- the **master** of the ship
- or the **pilot in command** of the aircraft

That is a practical rule, not just a paperwork rule. The person responsible for safe operation of the vessel or aircraft gets final say.

The exam also wants you to know who may physically control such a station aboard a U.S.-documented or U.S.-registered vessel or craft: any person holding an FCC amateur license, or someone authorized for alien reciprocal operation.

And if you are on a **U.S.-registered vessel in international waters**, the required amateur licensing is simply **any FCC-issued amateur license**.

### In message forwarding systems, the originator carries primary responsibility

If a station in a message forwarding system accidentally forwards a message that violates FCC rules, the station primarily accountable is the **control operator of the originating station**.

That makes sense if you think about how message systems work. Intermediate stations may be relaying automatically or semi-automatically. The person who created and launched the improper message is the primary source of the violation.

That said, the broader lesson is still to use good judgment when relaying traffic. "I was only forwarding it" is not a good operating habit, even if the exam's primary-accountability answer points to the originator.

---

## Group E1B — Protecting other services, protected places, and station-location rules

### Spurious emissions are unwanted emissions outside what is necessary

A **spurious emission** is not just any signal somebody dislikes. It is an emission **outside the necessary bandwidth** of the intended signal that can be reduced or eliminated without affecting the transmitted information.

In plain language: if energy is splattering out where it does not need to be, that is spurious.

This matters because the FCC expects amateurs to occupy no more spectrum than necessary and to avoid causing trouble outside their intended channel or segment.

### HF digital voice and SSTV are still narrow by design

For digital voice and slow-scan TV transmissions on the HF amateur bands, the acceptable bandwidth is **3 kHz**.

That is another reminder that HF rules assume relatively modest occupied bandwidths. The exam is nudging you away from the idea that any digital mode automatically gets a wider lane.

### Some facilities and services get special protection

Certain places and services receive specific interference protection.

If your station is within **1 mile of an FCC monitoring facility**, you must protect that facility from harmful interference.

Likewise, if a repeater on 70 centimeters causes interference to a radiolocation system, the control operator must **cease operation or make changes that mitigate the interference**. The answer is not "keep going until somebody proves it beyond doubt." If you are interfering with a protected service, you fix it or stop.

### The National Radio Quiet Zone is about radio astronomy

The **National Radio Quiet Zone** is the area surrounding the **National Radio Astronomy Observatory**.

That question is easy to memorize, but it helps more if you remember why the rule exists. Radio astronomy depends on receiving extremely weak natural signals. Transmitters that might be insignificant elsewhere can be a serious problem there.

### Antenna structures near airports may trigger FAA and FCC requirements

If you are putting up an amateur antenna structure at or near a public-use airport, you may have to:

- notify the **FAA**
- and register the structure with the **FCC**

The exam is testing whether you recognize that antenna construction is not purely an amateur-radio matter. Once structure height and location begin affecting aviation safety, other regulatory systems come into play.

### PRB-1 applies to state and local zoning, not every private restriction

**PRB-1** applies to **state and local zoning** regulations.

Its core idea is that state and local regulations affecting amateur antennas must make **reasonable accommodation** for amateur radio.

That does **not** mean amateurs automatically win every zoning fight. It also does **not** mean PRB-1 overrides homeowners associations or all private land-use restrictions. On the exam, the key takeaways are:

- PRB-1 is about **state and local zoning**
- it requires **reasonable accommodation**

Those two points show up repeatedly.

### Broadcast interference may lead to operating limits, not necessarily a shutdown

If an amateur station causes interference to domestic broadcast reception and the affected receivers are of good engineering design, the FCC may require the amateur station to **avoid transmitting during certain hours on the frequencies that cause the problem**.

That is a useful nuance. The answer is not always "cease operation entirely." Sometimes the FCC's remedy is more specific and limited.

### RACES stations must be certified, and normal privileges still matter

Under **RACES** rules, the stations that may operate are FCC-licensed amateur stations **certified by the responsible civil defense organization for the area**.

And the frequencies authorized under RACES are **all amateur service frequencies authorized to the control operator**.

That pairing matters. RACES is special, but it is not a separate free-floating radio service where ordinary amateur licensing and privileges disappear.

---

## Group E1C — Digital rules, foreign operation, remote control, and LF/MF coordination

### On 60 meters, data bandwidth has a specific limit

For data emissions on 60 meters, the maximum bandwidth is **2.8 kHz**.

That number is easy to confuse with other HF bandwidth limits, which is exactly why it appears in the pool. Sixty meters is one of the bands where the FCC expects you to remember the special handling.

### International communication is allowed, but it is not unrestricted

Communications transmitted to amateur stations in foreign countries must be limited to:

- communications incidental to the purpose of the amateur service
- and remarks of a personal character

The exam uses this to test whether you understand what amateur radio is for. It is not a loophole for unrestricted business traffic, coded content, or any topic whatsoever just because the station on the other end is in another country.

### IARP and CEPT are different operating arrangements

Two reciprocal operating frameworks appear in E1:

- **IARP**: a permit allowing U.S. amateurs to operate in certain countries of the Americas
- **CEPT**: an arrangement that allows an FCC-licensed U.S. citizen to operate in many European countries, and amateurs from many European countries to operate in the U.S.

For CEPT operation where permitted, the exam expects one specific detail: you must have a copy of **FCC Public Notice DA 16-1048**.

This is classic E1 material: not hard, but very specific. Learn the names and the regions they are associated with.

### Automatically controlled stations have narrow permission for third-party traffic

A station being automatically controlled may transmit **third-party communications only when transmitting RTTY or data emissions**.

The lesson here is that automatic control is allowed in some carefully defined cases, but you should not mentally broaden those cases into a general permission for any mode or content.

### Remote control failures have a hard time limit

If a remotely controlled station loses its control link because of a malfunction, the maximum permissible duration of its transmissions is **3 minutes**.

That is a safety-and-control rule. A station that can no longer be supervised must not be allowed to continue transmitting indefinitely.

### LF and MF operation requires notice to UTC and a waiting period

Before transmitting on **630 meters** or **2200 meters**, operators must notify the **Utilities Technology Council (UTC)** and provide their **call sign** and the **coordinates of the antenna system**.

After filing that notification, the operator must wait **30 days** before operating, provided UTC does not advise that there is a nearby power-line-carrier concern that must be addressed.

The practical point is that these bands are shared with incumbent systems using infrastructure that amateurs could potentially interfere with. Coordination comes first.

### Angle modulation and spurious-emission limits are still fair game

E1 also tests a couple of technical rule limits that are really about regulatory compliance:

- below **29.0 MHz**, the highest permitted modulation index at the highest modulation frequency for angle modulation is **1.0**
- below **30 MHz**, the maximum mean power of a spurious emission is **43 dB below the fundamental**

You do not need to turn these into a deep theory lesson for the exam. Just recognize them as the numbers the FCC uses to define acceptable emissions in those cases.

### Phone on 630 meters is allowed across the band

Phone emissions are permitted in **the entire 630-meter band**.

That is one of those questions that catches people who assume very narrow-mode-only operation on unusual bands. The exam wants the exact rule, not the assumption.

---

## Group E1D — Satellites, telemetry, telecommand, and one-way communications

### Learn the vocabulary first: telemetry vs. telecommand

In satellite and remote-device questions, the definitions matter.

**Telemetry** is the **one-way transmission of measurements at a distance from the measuring instrument**.

That means the data is reporting what something is doing: temperature, voltage, battery condition, orientation, and so on.

By contrast, **telecommand** is about sending instructions that initiate, modify, or terminate a function at a distance.

If telemetry is "here is my status," telecommand is "do this now."

### The encryption exception is narrow and specific

Amateur radio generally forbids messages encoded to obscure their meaning. E1 makes you learn one of the important narrow exceptions: **telecommand signals from a space telecommand station may be encrypted**.

That exception is easy to understand in practical terms. If you are controlling a space station, you do not want random people being able to issue valid control commands.

The test point is not that "satellites can use secret messages." The point is that **space telecommand** is a special case.

### What a space telecommand station is

A **space telecommand station** is an amateur station that transmits communications to initiate, modify, or terminate functions of a **space station**.

That is more specific than just "a station that talks to a satellite." The defining purpose is control.

### Identification and posted information still matter

A balloon-borne telemetry station must include its **call sign** in its identification transmissions.

And a station being operated by telecommand on or within **50 kilometers of the Earth's surface** must have all of the following posted at the station location:

- a photocopy of the station license
- the name, address, and telephone number of the station licensee
- the name, address, and telephone number of the control operator

The big idea is that unattended or remotely controlled operation does not remove accountability. The rules make sure someone can identify who is responsible.

### Model craft telecommand power is very limited

When operating a model craft by telecommand, the maximum permitted transmitter output power is **1 watt**.

That is a detail question, but it fits the broader theme: telecommand privileges are real, but tightly bounded.

### Space-station allocations are specific, not universal

The exam expects a few specific frequency-allocation facts for space stations:

- HF bands with space-station allocations: **40, 20, 15, and 10 meters**
- VHF band with space-station frequencies: **2 meters**
- UHF bands with space-station frequencies: **70 centimeters and 13 centimeters**

Do not overgeneralize from normal satellite operating habits. E1 wants the rule-based allocations.

### Who may operate as telecommand and Earth stations

Any amateur station designated by the **space station licensee** may be a telecommand station for that space station, subject to the class privileges of its control operator.

Any amateur station may operate as an **Earth station**, again subject to the privileges of the class of operator license held by the control operator.

So the limiting factors are not special satellite endorsements or membership in a particular organization. They are designation where required, and ordinary amateur license privileges.

### One-way communications are allowed only in certain cases

One-way communications may be transmitted by a:

- **space station**
- **beacon station**
- **telecommand station**

That is another example of E1 rewarding precision. Amateur radio is usually about two-way communication, but a few station types are specifically authorized to transmit one-way information.

---

## Group E1E — The Volunteer Examiner system

### Know the difference between VEs and VECs

A **Volunteer Examiner (VE)** is an accredited person who helps administer amateur examinations.

A **Volunteer Examiner Coordinator (VEC)** is an **organization** that has entered into an agreement with the FCC to coordinate, prepare, and administer amateur operator examinations.

That distinction matters because E1 asks both about people and about organizations.

The VECs are also the entities tasked with **maintaining the question pools** for the amateur license examinations.

### VE accreditation comes through a VEC

To be accredited as a VE, a VEC must confirm that the applicant meets the FCC requirements to serve as an examiner.

So the FCC sets the rules, but the accreditation step in practice runs through the coordinating organization.

### Each administering VE is responsible for proper conduct of the session

If the exam asks who is responsible for proper conduct and necessary supervision during an amateur operator license examination session, the answer is **each administering VE**.

That is an accountability point. Responsibility does not disappear into the group.

### Noncompliance by a candidate means stop the exam

If a candidate fails to comply with the examiner's instructions during an amateur operator license examination, the VE should **immediately terminate that candidate's examination**.

The rule is intentionally direct. Exam integrity is not something the VE team is supposed to negotiate on the fly.

### VEs may not examine certain relatives

A VE may not administer an examination to relatives of the VE as listed in the FCC rules.

This is basic conflict-of-interest protection. The exam will not usually ask you to recite the whole family tree from memory; it wants you to understand that certain close relationships disqualify a VE from serving as that person's examiner.

### What happens to the paperwork depends on pass or fail

If an examinee does **not** pass, the VE team must **return the application document to the examinee**.

If the examinee passes all required elements for a new license or upgrade, **three VEs must certify** that the person is qualified and that the examination was properly administered. The application document is then submitted to the coordinating **VEC** according to that VEC's instructions.

Again, the structure is formal on purpose. Examinations create license privileges, so the chain of custody and certification matter.

### Reimbursement is limited to real out-of-pocket exam expenses

Part 97 allows VEs and VECs to be reimbursed for out-of-pocket expenses related to:

- preparing
- processing
- administering
- and coordinating

an amateur operator examination.

This does not mean they are being paid to sell licenses or run training businesses under Part 97 authority. The allowed reimbursement is tied to the examination process itself.

### Fraud by a VE can cost more than VE status

A VE who fraudulently administers or certifies an examination can face severe penalties, including **revocation of the VE's amateur station license grant** and **suspension of amateur operator privileges**.

That is the FCC making clear that the exam system is not casual paperwork. It is part of the licensing system, and fraud attacks the integrity of that system.

---

## Group E1F — Pecuniary interest, spread spectrum, amplifiers, Line A, and other rule traps

### Spread spectrum is allowed only above 222 MHz

For the exam, the spread-spectrum rule is simple: it is permitted only on amateur frequencies **above 222 MHz**.

This is one of those clean memory items worth learning exactly.

### Canadian amateurs in the U.S. operate under reciprocal limits

Persons holding an amateur service license granted by the government of Canada may operate in the United States under the operating terms and conditions of the Canadian license, **not to exceed U.S. amateur privileges**.

That wording matters. Reciprocal operation does not mean automatic access to whatever privilege is broader in either country.

### External RF amplifiers below 144 MHz are regulated tightly

The FCC pays special attention to external RF power amplifiers capable of operation below **144 MHz**.

A dealer may sell one that has **not** been granted FCC certification only when the amplifier was **constructed or modified by an amateur radio operator for use at an amateur station**.

And one of the standards for amplifier certification is that the amplifier must satisfy the FCC's **spurious emission standards** when operated at the lesser of **1500 watts** or its maximum rated output.

This is a rules area shaped by long experience with misuse of amplifiers. The details are more restrictive than many operators first assume.

### Line A is near the Canadian border, and it matters on 420–430 MHz

**Line A** is a geographic boundary roughly parallel to and south of the border between the United States and Canada.

If an amateur station is in the contiguous 48 states and **north of Line A**, it may not transmit in the **420 to 430 MHz** segment.

This is the sort of rule that feels arbitrary until you remember the larger theme of E1: amateur privileges often exist alongside coordination obligations and protections for other users.

### STA exists for unusual experimental situations

The FCC may issue a **Special Temporary Authority (STA)** to an amateur station to provide for **experimental amateur communications**.

That is not a routine operating shortcut. It is a mechanism for unusual situations where special temporary permission is warranted.

### Pecuniary interest is the real issue in business-related communications

Amateurs may send a message to a business only when **neither the amateur nor the amateur's employer has a pecuniary interest in the communication**.

That fits the broader prohibition in Part 97: communications transmitted for **hire or material compensation** are generally not allowed, except where the rules specifically provide otherwise.

The exam is not saying amateurs can never mention a business or talk to someone at a business. It is saying the amateur service is not to be used as a substitute for compensated communications.

### A mesh network does not create a secrecy exception

Even over an amateur radio mesh network, you may not transmit **messages encoded to obscure their meaning**.

That is a good E1 reminder because modern networking language can make operators forget that Part 97 still applies. Changing the transport does not erase the rule.

### Auxiliary stations require at least Technician-class control

The control operator of an auxiliary station may be only a **Technician, General, Advanced, or Amateur Extra** class operator.

On the modern exam, the practical memory aid is simple: **Technician or higher**.

---

## Putting the whole subelement together

E1 looks broad because it collects a lot of rule topics in one place, but most of the questions boil down to a few repeatable habits.

### 1. Always think about the full occupied signal
A dial frequency can be legal while the actual emission is not. USB goes up, LSB goes down, and the whole signal has to stay inside the authorized segment.

### 2. Treat special privileges as conditional privileges
60 meters, 630 meters, 2200 meters, shipboard operation, aircraft operation, telecommand, automatic control, and satellite control all come with specific conditions. Learn the condition that makes the privilege legal.

### 3. When amateurs share with protected services, amateurs adapt
Monitoring facilities, radiolocation systems, radio astronomy sites, airport safety rules, and LF/MF utility coordination all reflect the same principle: amateurs do not get to ignore higher-priority or specially protected users.

### 4. Exceptions stay narrow
Encrypted space telecommand is an exception. Automatically controlled third-party traffic in RTTY/data is an exception. One-way communication by space, beacon, or telecommand stations is an exception. E1 punishes you when you mentally expand an exception beyond what the rule actually says.

### 5. Accountability is built into the rules
The originating control operator is primarily accountable for an improper forwarded message. Each administering VE is responsible for exam conduct. Telecommand stations must have identifying information posted. The system is built around knowing who is responsible.

### 6. Amateur radio is not for compensated or obscured communications
Pecuniary interest and obscured meaning are recurring Part 97 themes. If a question asks whether amateur radio can be used like a private paid communications service, the answer is usually no unless a very specific rule says otherwise.

---

## Final Summary

E1 is the Extra subelement that checks whether you can operate with good legal judgment.

You should come away knowing that:

- the entire emission must fit inside the authorized frequency segment
- 60 meters, 630 meters, and 2200 meters have special operating rules
- ships, aircraft, remote control, message forwarding, and automatic control each carry specific responsibilities
- amateurs must protect certain services, facilities, and locations from interference
- satellites and telecommand have their own vocabulary and a few narrow rule exceptions
- the VE/VEC system is formal, documented, and accountability-driven
- compensated communications and messages encoded to obscure meaning are generally prohibited

If E1 feels like a pile of rule trivia, step back and look for the operating logic: **stay inside your privileges, protect shared spectrum, and know exactly when a special exception does or does not apply.** That mindset is what the FCC is really testing.

---

*Extra-class exam: 50 questions, must pass with 37 or higher (74%). E1 contributes 6 questions.*
