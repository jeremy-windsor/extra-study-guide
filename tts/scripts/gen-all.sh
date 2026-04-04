#!/bin/bash
# Regenerate all 21 MP3s (10 narrative + 10 question files + cram sheet).
# Usage: gen-all.sh [voice]
set -e

VOICE="${1:-will}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
SUBELEMENTS_DIR="$REPO_DIR/subelements"
CRAM_SHEET="$REPO_DIR/CRAM-SHEET.md"
KOKORO="$HOME/.openclaw/skills/voice/scripts/tts-kokoro"

echo "=== Extra Class Study Guide — Full TTS Generation ==="
echo "Voice: $VOICE"
echo "Repo:  $REPO_DIR"
echo ""

# Verify TTS server is reachable
echo "-> Checking TTS server..."
CHECK=$(python3 "$KOKORO" --check 2>&1)
if ! echo "$CHECK" | python3 -c "import sys,json; d=json.load(sys.stdin); sys.exit(0 if d.get('available') else 1)" 2>/dev/null; then
    echo "ERROR: TTS server not reachable." >&2
    echo "$CHECK" >&2
    exit 1
fi
echo "   Server OK"
echo ""

FAILED=0
DONE=0
TOTAL=21

# Narrative files (non-question .md files)
NARRATIVE_FILES=$(ls "$SUBELEMENTS_DIR"/*.md | grep -v "\-questions\.md" | sort)

# Question files
QUESTION_FILES=$(ls "$SUBELEMENTS_DIR"/*-questions.md | sort)

# Process narratives
for md_file in $NARRATIVE_FILES; do
    DONE_IDX=$((DONE + FAILED + 1))
    name=$(basename "$md_file" .md)
    OUTPUT="${md_file%.md}.mp3"
    echo "--- [$DONE_IDX/$TOTAL] $name (narrative) ---"
    if bash "$SCRIPT_DIR/gen-narrative.sh" "$md_file" "$OUTPUT" "$VOICE"; then
        DONE=$((DONE + 1))
    else
        echo "FAILED: $name" >&2
        FAILED=$((FAILED + 1))
    fi
    echo ""
done

# Process question files
for md_file in $QUESTION_FILES; do
    DONE_IDX=$((DONE + FAILED + 1))
    name=$(basename "$md_file" .md)
    echo "--- [$DONE_IDX/$TOTAL] $name (questions) ---"
    if bash "$SCRIPT_DIR/gen-module-tts.sh" "$md_file" "$VOICE"; then
        DONE=$((DONE + 1))
    else
        echo "FAILED: $name" >&2
        FAILED=$((FAILED + 1))
    fi
    echo ""
done

# Process cram sheet
DONE_IDX=$((DONE + FAILED + 1))
echo "--- [$DONE_IDX/$TOTAL] CRAM-SHEET ---"
WORK_DIR=$(mktemp -d)
cleanup() { rm -rf "$WORK_DIR"; }
trap cleanup EXIT

python3 "$SCRIPT_DIR/extra-to-tts.py" "$CRAM_SHEET" --cram > "$WORK_DIR/cram-spoken.txt"
if bash "$SCRIPT_DIR/generate-audio.sh" "$WORK_DIR/cram-spoken.txt" "$REPO_DIR/CRAM-SHEET.mp3" "$VOICE"; then
    DONE=$((DONE + 1))
else
    echo "FAILED: CRAM-SHEET" >&2
    FAILED=$((FAILED + 1))
fi

echo ""
echo "=== Summary: $DONE/$TOTAL complete, $FAILED failed ==="

if [ "$FAILED" -gt 0 ]; then
    exit 1
fi
