---
note-type: dashboard
---

# Study queue

Generated views over `30-doctrine` frontmatter. Nothing here is authored —
if a table is empty, there are no modules matching, not a broken query.

> [!warning] Dataview and hyphenated keys
> The schema uses hyphenated frontmatter keys (`professor-emphasis`,
> `sub-topic`). In Dataview expressions a bare hyphen parses as subtraction,
> so every query below reaches those fields as `row["professor-emphasis"]`.
> Writing `professor-emphasis >= 2` will silently return nothing.

## Drill queue — high emphasis, low confidence

```dataview
TABLE WITHOUT ID
  file.link AS "Module",
  topic AS "Topic",
  row["professor-emphasis"] AS "Emph",
  confidence AS "Conf",
  row["last-drilled"] AS "Last drilled"
FROM "busorg/30-doctrine" OR "conlaw/30-doctrine"
WHERE row["professor-emphasis"] >= 2 AND confidence <= 3
SORT row["professor-emphasis"] DESC, confidence ASC
```

## Never drilled

```dataview
TABLE WITHOUT ID
  file.link AS "Module",
  topic AS "Topic",
  row["exam-likelihood"] AS "Exam likelihood"
FROM "busorg/30-doctrine" OR "conlaw/30-doctrine"
WHERE !row["last-drilled"]
SORT row["exam-likelihood"] ASC
```

## Coverage — modules per topic

```dataview
TABLE WITHOUT ID
  topic AS "Topic",
  length(rows) AS "Modules",
  min(rows.confidence) AS "Weakest"
FROM "busorg/30-doctrine" OR "conlaw/30-doctrine"
GROUP BY topic
SORT length(rows) DESC
```

## Sessions not yet reconciled

Session files are raw capture; a reconciled one is linked from at least one
doctrine module. A session with no backlinks has not been processed.

```dataview
TABLE WITHOUT ID
  file.link AS "Session",
  file.day AS "Date",
  length(file.inlinks) AS "Backlinks"
FROM "busorg/20-sessions" OR "conlaw/20-sessions"
WHERE length(file.inlinks) = 0
SORT file.day DESC
```
