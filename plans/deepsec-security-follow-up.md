# DeepSec Security Follow-up Plan

Date: 2026-06-28

## #1 Review Study App DOM injection candidates

DeepSec fast scan found security candidates in `apps/study-app/app.js`: 21 hits total. These are **not AI-confirmed vulnerabilities yet**; they are matcher hits that need triage.

Candidate clusters:

1. `dangerous-html` / `xss` — `innerHTML` and template literal render paths. Verify inserted values are trusted static question-pool content, or convert untrusted/dynamic values to `textContent` / DOM node construction.
2. `insecure-crypto` — likely `Math.random()` / shuffle usage; confirm it is only study randomization and not security-sensitive token generation.

Repair checklist:

1. Identify every `innerHTML` sink in `apps/study-app/app.js`.
2. Classify data source for each sink: static bundled content, user input, imported JSON, URL/hash params, localStorage.
3. Replace any non-static/untrusted insertion with safe DOM APIs.
4. Add regression tests or a sanitizer helper if imported study data can ever be user-controlled.
5. Run full DeepSec AI processing when gateway auth is restored; current result is matcher-only.
