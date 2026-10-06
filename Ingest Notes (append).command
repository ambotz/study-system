#!/bin/zsh
# Double-click to add photographed class notes BENEATH notes you already typed
# in the session file, under a dated heading. Your own text is never rewritten.
cd "$(dirname "$0")" || exit 1
SCRIPT=".claude/skills/session-capture/scripts/ingest_notes.py"
[ -f "$SCRIPT" ] || SCRIPT="_staging/session-capture/scripts/ingest_notes.py"
if [ ! -f "$SCRIPT" ]; then
  echo "The session-capture script is missing from this vault."
  echo "Expected: .claude/skills/session-capture/scripts/ingest_notes.py"
  echo "Your photos have not been touched."
  echo
  read -k 1 "?Press any key to close this window..."
  exit 1
fi
python3 "$SCRIPT" --append "$@"
rc=$?
echo
read -k 1 "?Press any key to close this window..."
exit $rc
