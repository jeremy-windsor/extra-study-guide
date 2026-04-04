# Amateur Radio Extra Class Exam Study Guide

Pass the FCC Amateur Extra class license exam — the top-tier amateur radio license with full privileges on all bands and modes.

## What's Inside

- **599 real exam questions** (2024-2028 pool, 4th errata) with correct answers
- **10 study sections** organized by topic (subelements E1-E0)
- **Cram sheet** for last-minute review
- **Practice test script** to simulate the real exam
- **7-day study plan** to get you from zero to licensed
- **PWA study app** with flashcards, practice exams, and progress tracking

## The Exam

| | |
|---|---|
| **Questions** | 50 multiple choice |
| **Passing** | 37 correct (74%) |
| **Time** | No official time limit |
| **Fee** | $35 (ARRL VEC) |
| **Prerequisite** | General class license |
| **Where** | Find a session at [arrl.org/find-an-amateur-radio-license-exam-session](http://www.arrl.org/find-an-amateur-radio-license-exam-session) |

The exam pulls from a **fixed public question pool** — every possible question and answer is published. This guide covers all of them.

### What Extra Gets You

The Amateur Extra license is the highest class of amateur radio license issued by the FCC. It grants:

- **Full frequency privileges** on all amateur bands
- **Exclusive access** to portions of 80m, 40m, 20m, and 15m bands
- **Authority** to be a Volunteer Examiner for all license classes
- **International recognition** as a fully licensed amateur operator

## Study App (PWA)

The fastest way to study — a browser-based app that works on your phone, tablet, or desktop. No install required.

### **[Open the Study App](https://jeremy-windsor.github.io/extra-study-guide/apps/study-app/)**

| Feature | |
|---------|---|
| **Flashcard mode** | Tap through all questions with instant answer reveal |
| **Practice exams** | Timed 50-question tests drawn randomly from the real pool |
| **Section study** | Drill down into individual subelements and groups |
| **Weak areas** | Automatically focuses on questions you've missed |
| **Progress tracking** | Mastery tracking, streaks, and achievements |
| **Formula reference** | Expanded formulas for Extra-level math (Smith chart, complex impedance, filters, toroids) |
| **Offline capable** | Works without internet after first load |
| **Installable** | Add to Home Screen on mobile, or install from Chrome/Edge on desktop |

> 💡 **Tip:** Add it to your phone's home screen — it runs like a native app, works offline, and tracks your progress across sessions.

## Question Pool

| Pool | Effective | Expires | Questions |
|------|-----------|---------|-----------|
| [2024-2028](pools/2024-2028/) | July 1, 2024 | June 30, 2028 | 599 |

**Source:** [NCVEC](https://www.ncvec.org/index.php/2024-2028-extra-class-question-pool-release) — released into public domain. Includes 4th errata (Feb 4, 2026).

## How to Study

### Quick Path (7 days)

See [STUDY-PLAN.md](STUDY-PLAN.md) for the full day-by-day plan.

| Day | Topic | Section |
|-----|-------|---------|
| 1 | Rules & Safety | [E1](subelements/E1-commission-rules.md), [E0](subelements/E0-safety.md) |
| 2 | Operating & Propagation | [E2](subelements/E2-operating-procedures.md), [E3](subelements/E3-radio-wave-propagation.md) |
| 3 | Amateur Practices | [E4](subelements/E4-amateur-practices.md) |
| 4 | Electrical Principles | [E5](subelements/E5-electrical-principles.md) |
| 5 | Circuit Components & Practical Circuits | [E6](subelements/E6-circuit-components.md), [E7](subelements/E7-practical-circuits.md) |
| 6 | Signals, Antennas & Transmission Lines | [E8](subelements/E8-signals-emissions.md), [E9](subelements/E9-antennas-transmission-lines.md) |
| 7 | Review + Practice Test | [Cram Sheet](CRAM-SHEET.md) + `python3 scripts/practice-test.py` |

### Study Sections

Each subelement has three files:

- **`E{N}-{name}.md`** — Study guide: a narrative walkthrough of the topic, written for learning
- **`E{N}-{name}.mp3`** — Audio version of the study guide (listen while driving, working out, etc.)
- **`E{N}-{name}-questions.md`** — Exam question bank: every question with the correct answer highlighted and explained

Start with the study guide to learn the material, then drill the question bank to lock in the answers.

| Section | Topic | Study Guide | Question Bank | Exam Qs | Pool Size |
|---------|-------|-------------|---------------|:-:|:-:|
| E1 | Commission's Rules | [guide](subelements/E1-commission-rules.md) | [questions](subelements/E1-commission-rules-questions.md) | 6 | 68 |
| E2 | Operating Procedures | [guide](subelements/E2-operating-procedures.md) | [questions](subelements/E2-operating-procedures-questions.md) | 5 | 60 |
| E3 | Radio Wave Propagation | [guide](subelements/E3-radio-wave-propagation.md) | [questions](subelements/E3-radio-wave-propagation-questions.md) | 3 | 39 |
| E4 | Amateur Practices | [guide](subelements/E4-amateur-practices.md) | [questions](subelements/E4-amateur-practices-questions.md) | 5 | 63 |
| E5 | Electrical Principles | [guide](subelements/E5-electrical-principles.md) | [questions](subelements/E5-electrical-principles-questions.md) | 4 | 49 |
| E6 | Circuit Components | [guide](subelements/E6-circuit-components.md) | [questions](subelements/E6-circuit-components-questions.md) | 6 | 68 |
| E7 | Practical Circuits | [guide](subelements/E7-practical-circuits.md) | [questions](subelements/E7-practical-circuits-questions.md) | 8 | 99 |
| E8 | Signals and Emissions | [guide](subelements/E8-signals-emissions.md) | [questions](subelements/E8-signals-emissions-questions.md) | 4 | 48 |
| E9 | Antennas and Transmission Lines | [guide](subelements/E9-antennas-transmission-lines.md) | [questions](subelements/E9-antennas-transmission-lines-questions.md) | 8 | 93 |
| E0 | Safety | [guide](subelements/E0-safety.md) | [questions](subelements/E0-safety-questions.md) | 1 | 12 |
| | **Total** | | | **50** | **599** |

### Practice Test

```bash
python3 scripts/practice-test.py
```

Generates a random 50-question exam from the real pool, scores it, and shows which areas need work.

### Audio Study Guide

Every section and the cram sheet are available as MP3 audio — study while driving, working out, or doing chores.

| File | Duration |
|------|----------|
| `subelements/E1-commission-rules.mp3` | 28 min |
| `subelements/E1-commission-rules-questions.mp3` | 41 min |
| `subelements/E2-operating-procedures.mp3` | 25 min |
| `subelements/E2-operating-procedures-questions.mp3` | 27 min |
| `subelements/E3-radio-wave-propagation.mp3` | 19 min |
| `subelements/E3-radio-wave-propagation-questions.mp3` | 18 min |
| `subelements/E4-amateur-practices.mp3` | 32 min |
| `subelements/E4-amateur-practices-questions.mp3` | 35 min |
| `subelements/E5-electrical-principles.mp3` | 21 min |
| `subelements/E5-electrical-principles-questions.mp3` | 54 min |
| `subelements/E6-circuit-components.mp3` | 30 min |
| `subelements/E6-circuit-components-questions.mp3` | 42 min |
| `subelements/E7-practical-circuits.mp3` | 51 min |
| `subelements/E7-practical-circuits-questions.mp3` | 75 min |
| `subelements/E8-signals-emissions.mp3` | 30 min |
| `subelements/E8-signals-emissions-questions.mp3` | 32 min |
| `subelements/E9-antennas-transmission-lines.mp3` | 48 min |
| `subelements/E9-antennas-transmission-lines-questions.mp3` | 71 min |
| `subelements/E0-safety.mp3` | 10 min |
| `subelements/E0-safety-questions.mp3` | 6 min |
| `CRAM-SHEET.mp3` | 32 min |
| **Total** | **12h 7m** |

Each MP3 is the audio version of the corresponding study guide narrative or question bank. Pronunciation of ham radio acronyms follows standard conventions (see `tts/pronunciation.txt`).

### Study Tips

- **Master the math** — Extra has significantly more calculations than General (impedance, reactance, filter design, Smith chart)
- **E7 and E9 are the heaviest** — 8 exam questions each, from pools of 99 and 93 questions
- **Understand Smith charts** — they appear in multiple subelements; learn to read them
- **Know your rules (E1)** — 6 exam questions cover frequency privileges, power limits, and operating restrictions
- **Practice exams daily** — take at least one practice test per study session
- **Use the formula reference** — tap the formula button in the app for comprehensive formula access
- **Don't memorize blindly** — Extra-level questions test understanding, not just recall

### Cram Sheet

[CRAM-SHEET.md](CRAM-SHEET.md) — one page of key facts, formulas, frequencies, and power limits. Read this the morning of your exam.

## Quick References

- **[Cram Sheet](CRAM-SHEET.md)** — Formulas, frequencies, and key numbers on one page
- **[Study Plan](STUDY-PLAN.md)** — 7-day structured study schedule

## Regenerating Audio

Audio is generated via [Kokoro](https://github.com/remsky/Kokoro-FastAPI) (OpenAI-compatible TTS). Requires Python 3.6+, `curl`, `ffmpeg`.

```bash
tts/scripts/gen-all.sh
```

Pronunciation rules are in `tts/pronunciation.txt`. Individual modules can be regenerated with `tts/scripts/gen-module-tts.sh`.

## Updating for a New Pool

1. Download the new pool PDF from [ncvec.org](https://ncvec.org/index.php/amateur-question-pools)
2. Parse into `pools/YYYY-YYYY/questions.json` using `python3 scripts/parse-pool.py`
3. Regenerate subelement files with `python3 scripts/gen-question-files.py`
4. Update practice test pool path in `scripts/practice-test.py`
5. Update dates in this README
6. Regenerate audio with the TTS pipeline above

## License

Question pool content is public domain (NCVEC). Study guide explanations and scripts are MIT licensed.
