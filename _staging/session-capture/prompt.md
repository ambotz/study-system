You are transcribing photographed handwritten class notes from a University of Chicago law student into a raw-capture session note. The class is {{CLASS_NAME}}, taught by {{PROFESSOR}}.

Read every image listed below with the Read tool. Then reply with ONE JSON object and nothing else: no prose, no code fence.

IMAGES (already resized; read all of them):
{{PHOTOS}}

SESSION INDEX for this class (session number | date | title | readings). Use it to work out which meeting each set of pages belongs to, and to resolve unclear words against that day's topic:
{{SESSION_INDEX}}

THE AUTHOR'S HANDWRITING
- He writes "&" as a sideways brace that looks like "}". Read it as "and".
- He writes "→" as a small triangle arrow that looks like "-D" or "▷". Read it as an arrow.
- A star before a line and underlining both mark emphasis. Render emphasised text in **bold**.
- Circled numbers are numbered list items.
- Roman numerals are often written small above a word (for example I, II, III over Legislative, Executive, Judicial).

TRANSCRIPTION RULES
1. Transcribe; do not summarise, improve, or add. Keep his wording and his order. Join a wrapped line, but never merge two ideas into one bullet. Fix only plain spelling slips.
2. Never add law he did not write. No definitions, no holdings, no extra citations.
3. Where a word or reference is uncertain, write your best reading followed by [?].
4. Where his note seems to state something incorrectly, and the day's topic or readings make the intended reference clear, keep his words exactly and append [check: the specific correction]. Never correct silently.
5. One idea per bullet. Group related lines under a short heading, using his own phrase where he has one. Use numbered items where he numbered them. Show hierarchy with level 0, 1 or 2.
6. Expand an abbreviation only where there is no doubt about it. Otherwise keep his abbreviations (BoD, AoC, Art., cl.).

DIAGRAMS
- If he drew a relationship, flow or hierarchy, return a diagram block with form "mermaid": `flowchart TB` or `flowchart LR`, every node label in double quotes, edge labels in double quotes (A ---|"label"| B), arrows `-->` or `<-->`. Use a `subgraph` for regions he separates with a line. Reproduce only the labels and connections he drew; invent no nodes.
- If the drawing is spatial rather than a graph, return form "text": an ASCII sketch of at most eight lines.
- Put [?] inside a label whose text you cannot read.
- Also put a short prose line under the diagram (a bullet) only if he wrote words next to it.

WIKILINKS
Link every mention of a case or doctrine module from the list below, exactly as [[Exact Name|as he wrote it]] (drop the |… part when identical). Never invent a link target and never link anything else.
LINKABLE NOTES:
{{LINK_TARGETS}}

SIGNALS
For each meeting, give one short line for each of six prompts, drawn ONLY from what the notes say. Write "—" wherever the notes do not clearly support an answer. Never infer what the professor was fishing for and never guess at emphasis.
- doctrine: the doctrine on the table
- hypo: the hypo posed, and what he was fishing for
- pushback: pushback on a student
- hard_case: what he called the hard case
- doesnt_matter: what he said does not matter
- exam_signal: any exam signal

MEETINGS
Return one session object per distinct class meeting in the photos. A page headed "cont." continues the previous meeting.
- header: the header as written on the first page (for example "9/28" or "Class 1 - 9/28")
- class_number: the integer if the header states one, otherwise null
- date: ISO date (YYYY-MM-DD) using the year of the session index dates, otherwise null
- pages: the image file names in reading order (file names only, not full paths)
- flags: one entry per [?] or [check: …] you wrote, as {"quote": "...", "reason": "..."}

OUTPUT FORMAT
{
  "sessions": [
    {
      "header": "Class 1 - 9/28",
      "class_number": 1,
      "date": "2026-09-28",
      "pages": ["IMG_0001.jpg", "IMG_0002.jpg"],
      "blocks": [
        {"type": "heading", "text": "Timeline"},
        {"type": "bullet", "text": "One idea per bullet.", "level": 0},
        {"type": "numbered", "text": "A numbered item.", "level": 0},
        {"type": "paragraph", "text": "Plain prose, only if he wrote prose."},
        {"type": "diagram", "form": "mermaid", "title": "Short title",
         "code": "flowchart TB\n  A[\"Owner\"] ---|\"contracts\"| B[\"Bank\"]"}
      ],
      "signals": {
        "doctrine": "—", "hypo": "—", "pushback": "—",
        "hard_case": "—", "doesnt_matter": "—", "exam_signal": "—"
      },
      "flags": [{"quote": "or (les)", "reason": "unclear word"}]
    }
  ]
}
Every block text must be a single line. Use headings only for topic groups on the page.
