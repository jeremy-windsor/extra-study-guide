#!/usr/bin/env python3
"""
Extra Class Ham Radio Practice Exam

Simulates the real FCC Extra exam: 50 questions drawn randomly from the
2024-2028 question pool, weighted by subelement (same distribution as the
actual exam). Interactive CLI — no dependencies beyond stdlib.

Usage:
    python3 scripts/practice-test.py
    python3 scripts/practice-test.py --pool pools/2024-2028/questions.json
    python3 scripts/practice-test.py --quick
    python3 scripts/practice-test.py --stats
"""

import json
import os
import random
import re
import sys
from pathlib import Path

# Real exam weights per subelement (total = 50)
EXAM_WEIGHTS: dict[str, int] = {
    "E0": 1,   # Safety
    "E1": 6,   # Commission's Rules
    "E2": 5,   # Operating Procedures
    "E3": 3,   # Radio Wave Propagation
    "E4": 5,   # Amateur Practices
    "E5": 4,   # Electrical Principles
    "E6": 6,   # Circuit Components
    "E7": 8,   # Practical Circuits
    "E8": 4,   # Signals and Emissions
    "E9": 8,   # Antennas and Transmission Lines
}

PASSING_SCORE = 37
TOTAL_QUESTIONS = 50

SUBELEMENT_NAMES: dict[str, str] = {
    "E0": "Safety",
    "E1": "Commission's Rules",
    "E2": "Operating Procedures",
    "E3": "Radio Wave Propagation",
    "E4": "Amateur Practices",
    "E5": "Electrical Principles",
    "E6": "Circuit Components",
    "E7": "Practical Circuits",
    "E8": "Signals & Emissions",
    "E9": "Antennas & Transmission Lines",
}

# Questions that reference figures
FIGURE_QUESTIONS: dict[str, str] = {
    "E5C10": "E5-1", "E5C11": "E5-1", "E5C12": "E5-1",
    "E6A10": "E6-1", "E6A11": "E6-1",
    "E6B10": "E6-2",
    "E6C08": "E6-3", "E6C10": "E6-3", "E6C11": "E6-3",
    "E7B10": "E7-1", "E7B11": "E7-1", "E7B12": "E7-1",
    "E7D06": "E7-2", "E7D07": "E7-2", "E7D08": "E7-2",
    "E7G07": "E7-3", "E7G09": "E7-3", "E7G10": "E7-3", "E7G11": "E7-3",
    "E9B01": "E9-1", "E9B02": "E9-1", "E9B03": "E9-1",
    "E9B04": "E9-2", "E9B05": "E9-2", "E9B06": "E9-2",
    "E9G06": "E9-3", "E9G07": "E9-3",
}


def load_pool(pool_path: str) -> list[dict]:
    """Load question pool from JSON file."""
    with open(pool_path) as f:
        data = json.load(f)
    questions = data.get("questions", data)
    if not isinstance(questions, list):
        print(f"Error: Expected a list of questions in {pool_path}")
        sys.exit(1)
    return questions


def select_exam_questions(pool: list[dict]) -> list[dict]:
    """Select 50 questions weighted by subelement, matching real exam distribution."""
    by_subelement: dict[str, list[dict]] = {}
    for q in pool:
        sub = q["subelement"]
        by_subelement.setdefault(sub, []).append(q)

    selected: list[dict] = []
    for sub, count in EXAM_WEIGHTS.items():
        available = by_subelement.get(sub, [])
        if len(available) < count:
            print(f"Warning: {sub} has only {len(available)} questions, need {count}")
            selected.extend(available)
        else:
            selected.extend(random.sample(available, count))

    random.shuffle(selected)
    return selected


def format_question(num: int, total: int, question: dict) -> str:
    """Format a question for display."""
    lines = []
    lines.append(f"━━━ Question {num}/{total} ━━━  [{question['id']}]")
    lines.append("")
    lines.append(question["question"])
    if question["id"] in FIGURE_QUESTIONS:
        fig = FIGURE_QUESTIONS[question["id"]]
        lines.append(f"    📎 See figures/{fig}")
    lines.append("")
    for letter in ("A", "B", "C", "D"):
        answer_text = question["answers"].get(letter, "")
        if answer_text:
            lines.append(f"  {letter}) {answer_text}")
    lines.append("")
    return "\n".join(lines)


def get_answer() -> str:
    """Get a valid answer (A-D) or Q to quit."""
    while True:
        try:
            raw = input("Your answer (A/B/C/D or Q to quit): ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print()
            return "Q"
        if raw in ("A", "B", "C", "D", "Q"):
            return raw
        print("  Please enter A, B, C, or D (or Q to quit)")


def run_exam(questions: list[dict]) -> None:
    """Run a full interactive practice exam."""
    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║      Extra Class Amateur Radio Practice Exam      ║")
    print("║                                                    ║")
    print("║  50 questions • 37 to pass (74%)                   ║")
    print("║  Same subelement weights as the real exam          ║")
    print("║                                                    ║")
    print("║  Enter A, B, C, or D for each question             ║")
    print("║  Press Q at any time to quit                       ║")
    print("╚══════════════════════════════════════════════════╝")
    print()
    input("Press Enter to begin...")
    print()

    correct = 0
    wrong = 0
    missed: list[dict] = []
    sub_correct: dict[str, int] = {}
    sub_total: dict[str, int] = {}

    for i, q in enumerate(questions, 1):
        sub = q["subelement"]
        sub_total[sub] = sub_total.get(sub, 0) + 1

        print(format_question(i, TOTAL_QUESTIONS, q))
        answer = get_answer()

        if answer == "Q":
            print(f"\n  Exam ended early after {i - 1} questions.")
            break

        correct_letter = q["correct"]
        correct_text = q["answers"][correct_letter]

        if answer == correct_letter:
            correct += 1
            sub_correct[sub] = sub_correct.get(sub, 0) + 1
            print(f"  ✅ Correct! The answer is {correct_letter}) {correct_text}")
        else:
            wrong += 1
            your_text = q["answers"].get(answer, "")
            missed.append({"question": q, "your_answer": answer})
            print(f"  ❌ Wrong. You chose {answer}) {your_text}")
            print(f"     Correct answer: {correct_letter}) {correct_text}")

        print(f"     Score so far: {correct}/{i}")
        print()

    print_results(correct, wrong, missed, sub_correct, sub_total)


def run_quick(questions: list[dict]) -> None:
    """Show all questions with answers revealed."""
    print(f"\n{'='*60}")
    print(f"  EXTRA CLASS PRACTICE EXAM — ANSWER KEY")
    print(f"{'='*60}\n")

    for i, q in enumerate(questions, 1):
        print(f"Q{i}. [{q['id']}] {q['question']}")
        if q['id'] in FIGURE_QUESTIONS:
            fig = FIGURE_QUESTIONS[q['id']]
            print(f"    📎 See figures/{fig}")
        for letter in ("A", "B", "C", "D"):
            mark = " ✅" if letter == q["correct"] else ""
            text = q["answers"].get(letter, "")
            print(f"    {letter}) {text}{mark}")
        print()


def show_stats(pool: list[dict]) -> None:
    """Show pool statistics."""
    by_sub: dict[str, list[dict]] = {}
    for q in pool:
        by_sub.setdefault(q["subelement"], []).append(q)

    print(f"\n{'='*60}")
    print(f"  EXTRA CLASS QUESTION POOL STATISTICS")
    print(f"{'='*60}\n")

    print(f"  {'Sub':<5} {'Topic':<35} {'Pool':>5} {'Exam':>5}")
    print(f"  {'-'*55}")
    for sub in ("E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9"):
        name = SUBELEMENT_NAMES.get(sub, "Unknown")
        pool_count = len(by_sub.get(sub, []))
        exam_count = EXAM_WEIGHTS[sub]
        print(f"  {sub:<5} {name:<35} {pool_count:>5} {exam_count:>5}")

    total_pool = sum(len(v) for v in by_sub.values())
    total_exam = sum(EXAM_WEIGHTS.values())
    print(f"  {'-'*55}")
    print(f"  {'Total':<41} {total_pool:>5} {total_exam:>5}")
    print(f"\n  Passing score: {PASSING_SCORE}/{TOTAL_QUESTIONS} (74%)\n")


def print_results(correct: int, wrong: int, missed: list[dict],
                  sub_correct: dict[str, int], sub_total: dict[str, int]) -> None:
    """Print exam results with subelement breakdown."""
    total_answered = correct + wrong
    if total_answered == 0:
        print("No questions answered.")
        return

    pct = (correct / total_answered) * 100
    passed = correct >= PASSING_SCORE and total_answered == TOTAL_QUESTIONS

    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║                  EXAM RESULTS                    ║")
    print("╚══════════════════════════════════════════════════╝")
    print()
    print(f"  Score: {correct}/{total_answered} ({pct:.0f}%)")
    print(f"  Passing: {PASSING_SCORE}/{TOTAL_QUESTIONS} (74%)")
    print()

    if total_answered < TOTAL_QUESTIONS:
        print(f"  ⚠️  Exam incomplete ({total_answered}/{TOTAL_QUESTIONS} answered)")
        if correct >= PASSING_SCORE:
            print("  You have enough correct answers to pass!")
        else:
            remaining = TOTAL_QUESTIONS - total_answered
            needed = PASSING_SCORE - correct
            if needed <= remaining:
                print(f"  You need {needed} more correct out of {remaining} remaining to pass")
            else:
                print("  Not enough remaining questions to pass")
    elif passed:
        print("  🎉 PASSED! You would pass the Extra exam!")
    else:
        needed = PASSING_SCORE - correct
        print(f"  ❌ Not passing. Need {needed} more correct answers.")

    # Per-subelement breakdown
    print()
    print("  Per-Subelement Breakdown:")
    print("  ─────────────────────────────────────────────")
    for sub in ("E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9"):
        total_sub = sub_total.get(sub, 0)
        correct_sub = sub_correct.get(sub, 0)
        name = SUBELEMENT_NAMES.get(sub, sub)
        if total_sub > 0:
            bar = "█" * correct_sub + "░" * (total_sub - correct_sub)
            print(f"  {sub} {name:<28s} {bar} {correct_sub}/{total_sub}")

    # Missed questions review
    if missed:
        print()
        print(f"  Questions to Review ({len(missed)} missed):")
        print("  ─────────────────────────────────────────────")
        for m in missed:
            q = m["question"]
            correct_letter = q["correct"]
            print(f"  {q['id']}: {q['question'][:70]}...")
            print(f"         Correct: {correct_letter}) {q['answers'][correct_letter]}")
            print()

    print()


def find_pool() -> str:
    """Find the question pool file."""
    candidates = [
        Path(__file__).parent.parent / "pools" / "2024-2028" / "questions.json",
        Path("pools/2024-2028/questions.json"),
        Path("../pools/2024-2028/questions.json"),
    ]
    for p in candidates:
        if p.exists():
            return str(p)
    print("Error: Could not find pools/2024-2028/questions.json")
    print("Usage: python3 scripts/practice-test.py [--pool PATH]")
    sys.exit(1)


def main() -> None:
    """Entry point."""
    pool_path = None
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print(__doc__)
        sys.exit(0)

    quick = "--quick" in args
    stats = "--stats" in args

    if "--pool" in args:
        idx = args.index("--pool")
        if idx + 1 < len(args):
            pool_path = args[idx + 1]
        else:
            print("Error: --pool requires a path argument")
            sys.exit(1)

    if pool_path is None:
        pool_path = find_pool()

    pool = load_pool(pool_path)

    if stats:
        show_stats(pool)
        return

    questions = select_exam_questions(pool)

    if quick:
        run_quick(questions)
        return

    try:
        run_exam(questions)
    except KeyboardInterrupt:
        print("\n\nExam cancelled.")
        sys.exit(0)


if __name__ == "__main__":
    main()
