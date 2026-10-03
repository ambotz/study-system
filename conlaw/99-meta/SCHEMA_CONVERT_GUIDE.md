# Con Law case files — convert to the one-pass schema

You are rewriting existing Con Law case files onto a new schema. The material is
already researched: the current file is the source of substance. Your job is to
re-architect it, not to re-brief the case from scratch — except for Cold-call
notes, which is rebuilt from the casebook.

## Why

The old schema had two layers that each stood alone, so each retold the facts,
the rule and the holding. The reader met the same case three times at different
altitudes, and the narrative arrived on page two. The new schema makes one pass:
each subject appears **once**.

## Inputs

- `UPLOADS/conlaw/10-cases/<Case>.md` — the current file. Every fact, quotation
  and cross-reference in it is already verified; reuse it.
- `UPLOADS/_inbox/schema-v2/extracts/<Case>.txt` — the casebook text for the
  reading plus three pages past it, which is where the numbered Notes live. Some
  cases have no extract; see step 5.
- `UPLOADS/99-templates/case-brief-conlaw-EXAMPLE (Lovett).md` — a finished file
  on this schema. Match it.
- `UPLOADS/conlaw/10-cases/` — list it to check whether a wikilink target exists.

## Schema — FIXED. Nine sections, this order, nothing added or reordered.

```
## Snapshot
## Issue
## Rule
## Operative facts
## Holding and reasoning
## Arguments rejected
## Where it sits
## Professor gloss
## Cold-call notes
```

1. **Snapshot** — 60–90 words of prose, orientation only. What was done, how the
   case got here in a clause, what the court held, the provisions in play. No
   narrative detail; the story is Operative facts' job. Past 90 words it is doing
   another section's work. Draw it from the old `### Posture` and `### Facts`.
2. **Issue** — bulleted, one per question, in the order the court takes them.
   A question argued and left undecided is marked **Argued, not decided**. If the
   casebook's section introduction frames the unit around a stated question, quote
   that in one lead sentence and say which question this case answers — the
   extract usually contains it a page or two before the case starts.
3. **Rule** — the synthesized statement first as prose, 2–5 sentences: the opening
   line of an exam answer. Then the court's own quotable formulations as bullets.
   Merge the old `## Rule` (synthesized) with the old `### Rule` (quotes).
4. **Operative facts** — bulleted, **chronological**, six to ten bullets. Each
   opens with the fact in bold, stated plainly and fully enough to stand alone,
   then its significance in italics: what it decided, or what changing it would
   change. There is no second facts section, so a fact that matters goes here or
   nowhere — fold in the load-bearing narrative from the old `### Facts`. A fact
   that decided nothing and explains nothing is dropped. Order by **when it
   happened**, not by importance: the sequence is usually the argument.
5. **Holding and reasoning** — a `**Held**` line with the vote and full lineup
   (including any judge who took no part), then bulleted dispositions in issue
   order, then reasoning under a bold heading per opinion, majority first, judge
   named. A unanimous court is a clause in the Held line, not a section. Merge the
   old `## Court Ruling` **Held** group with `### Holding`, `### Reasoning` and
   `### Dissent / concurrence`.
6. **Arguments rejected** — the old `## Court Ruling` **Rejected** group, kept as
   it is. Losing argument at its strongest in italics, then the court's answer.
7. **Where it sits** — the old `## Context`, tightened to three or four bolded
   themes. Prose with wikilinks.
8. **Professor gloss** — heading only. No text, no placeholder.
9. **Cold-call notes** — **rebuild from the casebook's numbered notes.** Find them
   in the extract (they follow the opinion, headed `NOTES` or `Notes`). Quote each
   note as the prompt, in the casebook's words, and answer it beneath in bullets.
   Where the notes follow a later reading and cover several together, say so in one
   line and quote them anyway. A question that reads as rhetorical — "is it
   relevant that the Constitution says . . ." — is the live one; that is where the
   professor is going. Keep the best of the old cold-call content below a
   `### Further drilling` subheading, trimmed to four or five bullets.

   **If there is no extract** for your case, the casebook notes are unavailable.
   Keep the old cold-call content, restructured and trimmed, with no
   `### Further drilling` split, and add a line at the top of the section:
   `The casebook notes for this reading were not available; these questions are
   drawn from the opinion.`

## Rules

- **Every wikilink must resolve to a file that exists in `10-cases/` or
  `30-doctrine/`.** Check with `ls`. A case with no file is written as an
  *italicised case name* in plain text, never as a link. The current files were
  already cleaned this way — do not reintroduce links.
- **No meta-commentary.** Never describe the file or a section inside it. No "in
  order, because…", no "what follows is…". The heading says what the section is.
- **No hard wrapping.** Each paragraph and each bullet is one line, however long.
- Never split a wikilink across a line. No link target ends in a period.
- Frontmatter is unchanged — copy it across verbatim, including any `> [!note]`
  or `> [!caution]` callout that sits immediately after it.
- Quote only what the current file or the extract already quotes. Invent nothing.
- **Proofread before writing the file out.** Check subject-verb agreement, singular
  and plural after an intervening clause, its/it's and their/there, dangling or
  misattached modifiers, sentences that lost their main verb during editing, doubled
  words, a missing space after a period, parallel structure inside a bulleted list,
  and consistent em dashes. Every bullet is finished prose, not a note to itself.
- **Per-section word budget.** The whole file is 1,600–2,000 words. A first
conversion attempt came in at 2,620 because Rule and Operative facts ran double.
Hold to these, which are the worked example's actual counts:

| Section | Words |
|---|---|
| Snapshot | 60–90 |
| Issue | 50–70 |
| Rule | 130–170 |
| Operative facts | 350–420 |
| Holding and reasoning | 380–450 |
| Arguments rejected | 150–200 |
| Where it sits | 180–220 |
| Cold-call notes | 450–560 |

Count before you finish. Over budget means prose that restates, not detail worth
keeping — cut the restatement, not the substance.

## Output

Write `<Exact Case Name>.md` — the complete file, frontmatter included — into the
directory named in your prompt. Keep the filename exactly as the input's.

Before finishing, verify each file: nine headings present in order and nothing
else at `##` level; Professor gloss empty; every wikilink resolves; no link ends
in a period; no wikilink spans a newline; no `***`; frontmatter intact; word count
in band. Report tersely: files written, any case where the casebook notes were
missing or unclear, and judgment calls.
