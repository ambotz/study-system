---
name: case-brief
description: Write a case file for an assigned reading, against the fixed two-layer schema in CLAUDE.md section 5. Use when asked to brief a case, prepare a reading, or fill 10-cases for a class meeting. Refuses to brief statutes, rules, and governance documents, which take doctrine modules instead.
---

# case-brief

Produces one file in `<class>/10-cases/<Case Name>.md` from an assigned reading.

The case file has two layers. The **brief layer** is extraction that must still be
true in December and that feeds `30-doctrine`. The **class layer** is cold-call
prep against the opinion and is allowed to decay after the class meeting passes.

`CLAUDE.md` is authoritative for the schema and the house style. This file is the
procedure.

## Before anything else: is this a case?

Look the reading up in `<class>/99-meta/case-index.json`.

- `kind: "case"` with a page range → brief it.
- `kind: "statute"` or `"rule"` → **stop**. These have no opinion to brief. They
  produce a doctrine module built from the text of the provision, not a case file.
  Say so and stop; do not produce an empty case file and do not improvise a brief
  from background knowledge.
- `kind: "document"` or `"note"` → **not a case brief, but still a file.** A charter,
  a set of bylaws, or a casebook note gets a **document note** in the same
  `10-cases/` folder, on the light three-section schema in `CLAUDE.md` section 5 —
  What it is / What to notice / Where it goes. Do not apply the two-layer case
  schema to a document.
- Not in the index at all → **stop and ask**. The index is generated from the
  syllabus. A reading that is missing from the index means either the syllabus
  changed or the name is wrong, and both are worth a human's attention.

## Procedure

1. **Resolve and extract.**

   ```
   python3 .claude/skills/case-brief/scripts/extract_case.py "<case name>" --out /tmp/case.txt
   ```

   The script converts the syllabus's printed page range to PDF pages using a
   per-source offset and refuses non-paginated readings. Do not hand it PDF page
   numbers; hand it the case name.

2. **Read one page past the end of the range.** Syllabus ranges are not always
   self-contained — the range for Van Gorkom (B&C 120–134) clips the § 102(b)(7)
   note, which finishes on 135. If the extra page continues the same case or its
   notes, use it. If the extra page starts a new case, discard it.

3. **Read the whole extract before writing anything.** The brief layer depends on
   knowing which facts the court explained away, and that is only visible after
   the reasoning.

4. **Write the file** to `<class>/10-cases/<Case Name>.md`, using the case name
   exactly as `case-index.json` spells it, so wikilinks from doctrine modules
   resolve.

   **A case name must never end in a period.** "Moelis & Co." becomes a file named
   `...Co.md`, whose note name is `...Co` without the period, so every wikilink
   written with the period fails to resolve — silently, like every other wikilink
   failure. If the syllabus name ends in a period or is unwieldy, shorten it to a
   filesystem-safe canonical form, **update `case-index.json` to match**, and use
   that form everywhere. Avoid `/` and `:` for the same reason. Follow the section order below exactly.

5. **Fill `feeds_module`** with a wikilink to the doctrine module this case
   supports. If no such module exists yet, say which module needs creating rather
   than inventing a filename that will not resolve.

6. **Leave `Professor gloss` empty.** An empty heading, no placeholder text and
   no comment. `session-reconcile` populates the gloss from the class debrief.

## Section order

**Brief layer**

1. `## Rule` — one sentence. What this case adds to the doctrine that was not
   already there. "Nothing — illustration of [[X]]" is a legitimate answer, and a
   better answer than inventing a contribution.
2. `## Facts` — bulleted, **pivotal facts only**. A fact belongs here if it
   decided the case, if the issue or ruling turns on it, or if changing it would
   change the result. Apply that last test deliberately — these are the facts a
   hypothetical gets built on.
   A fact the court discussed and then explained away still belongs here, with
   its fate noted in italics, because a hypothetical that removes the defect
   around it comes out differently.
   Everything else — background, narrative, procedural colour, good-to-know
   detail — goes to the class layer Facts section and is **not** repeated here.
   The two Facts sections divide the material; they do not duplicate it.
3. `## Court Ruling` — two bolded groups, `**Held**` and `**Rejected**`, each
   bulleted. Under **Rejected**, state each losing argument at its strongest, in
   italics, and then give the court's answer to that argument. An argument
   summarised only as the court's dismissal of the argument is useless for
   drilling.
4. `## Context` — prose, with wikilinks. Neighbouring cases and the fact that
   distinguishes this case from each one; statutory or legislative response;
   where the case sits in the arc of the course; anything a reader in December
   would want that the three sections above have no room for.
5. `## Professor gloss` — empty.

**Class layer**, below a `---`, under `## Class layer`:

- `### Posture` — one or two bullets. Note the posture explicitly when the
  posture is unusual and drives how hard the holding bites.
- `### Facts` — prose, carrying the **full narrative**: background, how the
  parties arrived at the dispute, procedural colour, and the detail that is worth
  knowing but decided nothing. Prose packs more densely than bullets here. Do not
  restate the brief layer's pivotal facts except where the narrative is
  unintelligible without them.
- `### Issue` — bulleted, one bullet per issue.
- `### Holding` — bulleted, one bullet per issue, in the same order as the
  issues. Each bullet gives the disposition **and** what the disposition turned
  on. Never compress to "no on both" or any answer that sends the reader back up
  the page to decode it.
- `### Rule` — bulleted. Redundant with the brief layer's Rule by design, so that
  the class layer reads as a complete brief standing alone.
- `### Reasoning` — bulleted, with the judge named in parentheses above the
  bullets where the judge is notable.
- `### Dissent / concurrence` — bulleted main points, judge named in parentheses.
  Give a real dissent its strongest form; a dissent is usually the best available
  counter-argument and feeds the counterfactual drill type.
  Where the panel was unanimous, say so in one line. Then add a **very short**
  sketch of what could have been argued — two or three lines — and **only where
  there is genuinely something to say**: a tension the opinion glosses over, a
  definition doing more work than it admits. Where the opinion is simply
  uncontroversial, one line and stop. Manufacturing an objection to fill the
  heading is worse than leaving the heading nearly empty.
- `### Cold-call notes` — the most elaborated section in the class layer. Cover
  what will be asked, the wrong answer that sounds right, what to be ready to be
  pushed on, and anything memorisable that shows command of the case. Specific
  numbers, dates and quotations belong here.

## House style

Repeated from `CLAUDE.md` because violating these is the most common failure.

- **No meta-commentary.** Never narrate a section's purpose inside that section.
  Not "only the facts that did work", not "what follows is", not an explanation
  of the template. The heading says what the section is. A sentence about the
  file's own construction is noise in a file read under time pressure.
- **One idea per bullet.** No compression that has to be read twice.
- **MECE.** Bullets in a list do not overlap and together cover the ground.
- **Name the antecedent.** Prefer the noun to "it", "this", or "that", even when
  the noun is longer.
- **Wikilink every case and module name**, everywhere, including cases not on the
  syllabus. The graph view is how doctrine connects to cases. Use a display alias
  for long names — `[[In re Caremark International Inc. Derivative Litigation|Caremark]]`.
- **Never let a wikilink wrap across a line break.** Obsidian will not resolve a
  link containing a newline, and the failure is silent.

## Refusals

Stop and say so, rather than producing something plausible:

- The reading is a statute, rule, note, or governance document.
- The reading is not in `case-index.json`.
- The extracted text is empty, truncated, or visibly garbled.
- The case genuinely contributes no new rule — write that in `Rule` rather than
  manufacturing a contribution.

## Before finishing, check

1. Every section present, in order, both layers.
2. `Professor gloss` empty — no placeholder, no comment.
3. `feeds_module` resolves to a real module, or the missing module is named.
4. No wikilink wraps across a line.
5. No meta-commentary anywhere in the file.
6. Holding bullets map one-to-one onto Issue bullets, in the same order.
7. Every rejected argument stated at its strongest before the court's answer.
8. `case` frontmatter matches the filename and matches `case-index.json`.
9. The two Facts sections divide the material rather than duplicating it — every
   bullet in the brief layer passes the would-changing-it-change-the-result test,
   and nothing that fails that test appears in both places.
