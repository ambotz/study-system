---
kind: tracker
scope: cross_class
generated: false
source: 60-drills/attempts
---

# Rep tracker

Reads the frontmatter `essay-grade` writes into `<class>/60-drills/attempts/`.
Nothing here is maintained by hand — grade an attempt and the tables fill in.

`score_max` varies by mode, because a micro-drill only scores the axes it can
observe: an outline rep is out of 9, an opening rep out of 6, a triage rep out
of 3, a full attempt out of 18. Read **Pct**, not Score.

## Everything, newest first

```dataview
TABLE WITHOUT ID
  file.link AS Attempt,
  class AS Class,
  mode AS Mode,
  date AS Date,
  (score_total + "/" + score_max) AS Score,
  round(100 * score_total / score_max) + "%" AS Pct
FROM "busorg/60-drills/attempts" OR "conlaw/60-drills/attempts"
WHERE kind = "exam_attempt"
SORT date DESC
```

## Axis trend — the thing to actually watch

A column stuck at 1 across several rows is the drill to run next. A column
climbing 1 → 2 → 3 is a habit that took. Blanks are modes that cannot see that
axis, not misses.

```dataview
TABLE WITHOUT ID
  date AS Date,
  mode AS Mode,
  scores.thesis_placement AS "1 Thesis",
  scores.visible_structure AS "2 Struct",
  scores.element_discipline AS "3 Elem",
  scores.counterargument_weighting AS "4 Counter",
  scores.commitment_grammar AS "5 Commit",
  scores.budget_discipline AS "6 Budget"
FROM "busorg/60-drills/attempts" OR "conlaw/60-drills/attempts"
WHERE kind = "exam_attempt"
SORT date ASC
```

## Volume by mode

```dataview
TABLE WITHOUT ID
  mode AS Mode,
  length(rows) AS Reps,
  round(100 * sum(rows.score_total) / sum(rows.score_max)) + "%" AS "Avg pct"
FROM "busorg/60-drills/attempts" OR "conlaw/60-drills/attempts"
WHERE kind = "exam_attempt"
GROUP BY mode
SORT length(rows) DESC
```

## Con Law only

```dataview
TABLE WITHOUT ID
  date AS Date, mode AS Mode, source AS Source,
  round(100 * score_total / score_max) + "%" AS Pct
FROM "conlaw/60-drills/attempts"
WHERE kind = "exam_attempt"
SORT date DESC
```

## BusOrg only

```dataview
TABLE WITHOUT ID
  date AS Date, mode AS Mode, source AS Source,
  round(100 * score_total / score_max) + "%" AS Pct
FROM "busorg/60-drills/attempts"
WHERE kind = "exam_attempt"
SORT date DESC
```

## Drill queue — low confidence, high stakes, not drilled lately

`confidence` is yours alone to set. Until you do, every module reads `1` and
this table is sorted by emphasis only.

```dataview
TABLE WITHOUT ID
  file.link AS Module,
  professor_emphasis AS Emph,
  exam_likelihood AS Likely,
  confidence AS Conf,
  last_drilled AS "Last drilled"
FROM "conlaw/30-doctrine" OR "busorg/30-doctrine"
WHERE exam_likelihood = "high" AND confidence <= 2
SORT professor_emphasis DESC, confidence ASC
LIMIT 25
```

## Never drilled

```dataview
LIST
FROM "conlaw/30-doctrine" OR "busorg/30-doctrine"
WHERE !last_drilled AND professor_emphasis = 3
```
