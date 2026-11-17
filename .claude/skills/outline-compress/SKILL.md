---
name: outline-compress
description: Generate the outline layer from the doctrine modules — master outline, then attack outline, then the exam-room artifact (a one-page sheet for Con Law, a recall scaffold for the fully closed BusOrg exam). Use when asked to build, compress, or regenerate an outline, an attack outline, a one-pager, or a scaffold. Everything it writes into 50-outline is generated and regenerable; it never edits a doctrine module.
---

# outline-compress

`50-outline/` is a **generated view** of `30-doctrine/`. Nothing here is
authored. If a fact is wrong in the outline it is wrong in the module, and the
fix goes there and the outline is regenerated. Hand-editing a generated file
means the next regeneration silently discards the edit.

Reconcile before compressing. `professor_emphasis` and `exam_likelihood` are the
weights this skill compresses *by*, and until `session-reconcile` has run they
are September predictions off the syllabus, not evidence. Compressing against
unreconciled weights produces a confident outline pointed at the wrong things.

## Three artifacts, three jobs

Do not collapse them. Each is a different compression ratio with a different
reader in mind.

| | Reader | Job | Rough size |
|---|---|---|---|
| **Master** | you in week one, absorbing | every rule, in a navigable order | 30–60 pages |
| **Attack** | you in the exam room, from memory | the decision tree you run on a fact pattern | 4–8 pages |
| **Exam-room artifact** | you at minute 40, stuck | only what you cannot reconstruct | one sheet, or a card deck |

The master is the cheapest of the three here, because the modules already exist
and it is mostly ordering and de-duplication. The attack outline is where the
thinking is. The third artifact is the hardest and must be built **last**, from
evidence, for the reason below.

## The exam-room artifact differs by class

**Con Law — one page, front and back.** A sheet is permitted.

**BusOrg — nothing.** The exam is in-class, closed-book and word-limited, with
no sheet of any kind. So the third artifact is not a page; it is a **recall
scaffold**: the finite list of things that must be in memory, structured for
drilling rather than for reading. It feeds `exam-drill`, not a printer.

Buccola's house style runs on bare section numbers and bare case names, and his
only closed-book script carries the highest section-number density in the set —
5.7 per 1,000 words, all from memory. The scaffold's core is therefore the
post-SB 21 § 144 subsection map, the standard-of-review gates in the order
Chancery walks them, and the case-name-to-proposition pairs in the register
*"Fair price matters more (Trados)."*

**The sheet is insurance, not a substitute.** Do not thin the Con Law
memorisation because a sheet exists. Scanning paper at minute 40 costs time and
breaks a train of thought; the sheet earns its place by catching the two or
three things that fall out under pressure, not by holding what should be fluent.
Build the Con Law scaffold too, and let the sheet be the overflow.

## Procedure

### Master outline

1. **Order by doctrine, not by syllabus.** The syllabus order is a teaching
   sequence; the outline is a retrieval structure. Group by `topic`, then
   `sub_topic`, which leads with the governing provision.
2. One section per module, carrying: the Rule statement's first plain-English
   sentence, the Elements as bold questions, Standard of review, Exceptions,
   Leading case and Best counter-case with the distinguishing line, Professor
   gloss, Common trap.
3. **Keep the wikilinks.** The master's value over reading the modules is that
   it is one scrollable document with the graph intact.
4. Write to `<class>/50-outline/Master outline.md` with `generated: true`.

### Attack outline

The compression that matters. Not a shorter master — a different shape.

1. **One entry per decision, not per module.** An attack outline answers "a fact
   pattern just landed, what do I ask first." Several modules often collapse into
   one gate, and one module can appear at two gates.
2. **Order the gates the way the decider hits them.** Buccola's strong answers
   invent exactly this and use it as their headings: *Direct or Derivative →
   Controlling Stockholder → Conflicted Director → Entire Fairness → Revlon →
   Unocal*. Baude's mirror the prompt's labels instead, so the Con Law attack
   outline is organised by **power claimed** and **who is acting**, not by case.
3. Each gate carries: the question in bold, the test with its elements numbered,
   who bears the burden, the one case that resolves it, the one case that cuts
   the other way with the distinguishing fact, and the Common trap.
4. **Carry the professor's verdict word into the template.** `should` for Baude,
   `likely` for Buccola. The attack outline is also a prose template.
5. Drop anything at `professor_emphasis: 1` and `exam_likelihood: low` to an
   appendix list of names. It stays findable without costing a page.
6. Write to `<class>/50-outline/Attack outline.md`.

### Exam-room artifact — build last, from the error log

Building this before drilling means guessing at your own failure modes.

1. **Run at least two graded timed-fulls first**, so `<class>/60-drills/error-log.md`
   and the attempt files exist.
2. **Source the contents from evidence, in this order:** anything a graded
   attempt got wrong or omitted; anything marked as a Common trap in a module at
   `professor_emphasis: 3`; closed lists that are long enough to lose a member
   under pressure; exact phrases worth two words each.
3. **Exclude anything reconstructible.** No narrative, no facts, no reasoning you
   can rebuild from the test. If you can derive it in ten seconds, it is costing
   a line that something else needs.

   For Con Law the qualifying content is things like the Youngstown categories
   with the conclusive-and-preclusive carve-outs, the *Dole* conditions, the
   *Casey* and *Ramos* stare decisis factor sets, and case-plus-Justice pairings
   — closed lists where dropping one member is a visible hole.

4. **Set a hard budget and enforce it.** One page front and back. When something
   new earns a place, something else leaves. Track what was cut and why at the
   bottom of the source file so the next version does not relitigate it.
5. Write the Con Law sheet to `<class>/50-outline/One-pager.md` and the recall
   scaffold to `<class>/50-outline/Recall scaffold.md`. The scaffold is the input
   to `exam-drill`, so group it by retrieval cue, not by topic.

## Versioning

The exam-room artifact is regenerated repeatedly — v1 after two attempts, then
again after each pair. Keep the version in frontmatter (`version: 3`,
`built_from_attempts: 6`) rather than in the filename, so the wikilink target
never moves.

## Frontmatter

Written by script, never freehand. Every generated file carries:

```yaml
kind:            # master_outline | attack_outline | one_pager | recall_scaffold
class:           # busorg | conlaw
generated: true
source: 30-doctrine
modules_covered: # integer
built: # YYYY-MM-DD
```

## What this skill does not do

- It does not edit a doctrine module. A wrong rule is a `doctrine-module` fix, after which this regenerates.
- It does not set `professor_emphasis` or `exam_likelihood`; it only reads them. Only `session-reconcile` may revise them.
- It does not touch `confidence` or `last_drilled`.
- It does not build the exam-room artifact before graded attempts exist. If asked to, say why and offer the attack outline instead.
