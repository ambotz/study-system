#!/usr/bin/env python3
"""Check every wikilink in the vault.

Three failure modes, all of which Obsidian fails at silently:

  1. A wikilink broken across a line. Obsidian will not resolve a link containing
     a newline, and nothing marks it as broken.
  2. A link to a note that does not exist. Legitimate for a case not yet briefed,
     so these are reported separately as forward references.
  3. A note name ending in a period, which collides with the .md extension.

Exit code 1 on a hard failure (1 or 3). Forward references never fail the check.

CLAUDE.md files are skipped. They are format law, and their schema examples carry
placeholder wikilinks that are not meant to resolve to anything.
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", ".."))

md = [f for f in glob.glob(os.path.join(VAULT, "**", "*.md"), recursive=True)
      if "/99-templates/" not in f and "/.claude/" not in f
      and os.path.basename(f) != "CLAUDE.md"]
notes = {os.path.splitext(os.path.basename(f))[0] for f in md}

multiline, trailing, links = [], [], {}
for f in md:
    rel = os.path.relpath(f, VAULT)
    text = open(f).read()
    if os.path.splitext(os.path.basename(f))[0].endswith("."):
        trailing.append(rel)
    for m in re.finditer(r"\[\[[^\]]*\]\]", text, re.S):
        raw = m.group(0)
        if "\n" in raw:
            multiline.append((rel, " ".join(raw.split())[:70]))
            continue
        target = raw[2:-2].split("|")[0].split("#")[0].strip()
        if target:
            links.setdefault(target, set()).add(rel)

resolved = {t: f for t, f in links.items() if t in notes}
forward = {t: f for t, f in links.items() if t not in notes}

print(f"notes: {len(notes)}   distinct link targets: {len(links)}   "
      f"resolved: {len(resolved)}   forward refs: {len(forward)}")

if forward:
    print("\nforward references (fine — a case or module not yet written):")
    for t in sorted(forward):
        print(f"  {t}")

fail = False
if multiline:
    fail = True
    print("\nBROKEN — wikilink split across a line (Obsidian will not resolve):")
    for rel, raw in multiline:
        print(f"  {rel}: {raw}")
if trailing:
    fail = True
    print("\nBROKEN — note name ends in a period (collides with .md):")
    for rel in trailing:
        print(f"  {rel}")

print("\nFAIL" if fail else "\nOK")
sys.exit(1 if fail else 0)
