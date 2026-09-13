---
note_type: dashboard
---

# Study queue

Generated views over `30-doctrine` frontmatter. Nothing here is authored — if a
table is empty, there are no modules matching, not a broken query.

## Drill queue — high emphasis, low confidence

```dataview
TABLE WITHOUT ID
  file.link AS "Module",
  topic AS "Topic",
  professor_emphasis AS "Emph",
  confidence AS "Conf",
  last_drilled AS "Last drilled"
FROM "busorg/30-doctrine" OR "conlaw/30-doctrine"
WHERE professor_emphasis >= 2 AND confidence <= 3
SORT professor_emphasis DESC, confidence ASC
```

## Never drilled

```dataview
TABLE WITHOUT ID
  file.link AS "Module",
  topic AS "Topic",
  exam_likelihood AS "Exam likelihood"
FROM "busorg/30-doctrine" OR "conlaw/30-doctrine"
WHERE !last_drilled
SORT exam_likelihood ASC
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

## Cases not yet feeding a module

A case file whose `feeds_module` is empty has been read but not reconciled into
the doctrine layer. That is the date-in/doctrine-out rule, made visible.

```dataview
TABLE WITHOUT ID
  file.link AS "Case",
  topic AS "Topic",
  read_for AS "Read for"
FROM "busorg/10-cases" OR "conlaw/10-cases"
WHERE !feeds_module
SORT read_for DESC
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
