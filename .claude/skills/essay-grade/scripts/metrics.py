#!/usr/bin/env python3
"""Deterministic prose metrics for an exam answer.

Reads a plain-text or markdown answer and prints JSON. Counts only — no
judgment. The model reads the JSON and does the judging; the numbers here are
reproducible and comparable against the benchmarks recorded in
99-exam-writing/1L writing diagnostic.md.

Usage:
    python3 metrics.py answer.txt
    python3 metrics.py answer.txt --caps 1200,750,1050

Exam4 PDF exports carry their own per-section word counts in the header and
repeat an institution banner on every page; --exam4 strips that banner and
splits on the ANSWER-N-ABOVE dividers.
"""

import argparse
import json
import re
import sys

# Hedges that attach to an argument. Benchmark: Rappaport models 1.5-3.3/1k,
# Baude Elements exemplars 5.7-14.2/1k soft modals. Low is not the target.
HEDGE = [
    r"\barguably\b", r"\bit could be argued\b", r"\bone could argue\b",
    r"\bcould argue\b", r"\bit might be argued\b", r"\bon the other hand\b",
    r"\bit is unclear\b", r"\bit'?s unclear\b", r"\bit is not clear\b",
    r"\bit is possible\b", r"\bperhaps\b", r"\bmight\b", r"\bmay\b",
    r"\bpossibly\b", r"\bseems\b", r"\bappears\b",
]

# Verdict labels. Benchmark: Rappaport models 18-20/1k, Baude Con Law 3.3-8.7/1k
# narrow. Ashwin's 1L range was 3.2-9.5/1k.
VERDICT = [
    r"\blikely\b", r"\bunlikely\b", r"\bshould\b", r"\bmust\b", r"\bcannot\b",
    r"\bI conclude\b", r"\bI would advise\b", r"\bI would recommend\b",
    r"\bI think\b", r"\bI believe\b", r"\bthe better view\b",
    r"\bthe stronger argument\b", r"\bthe strongest\b", r"\bplausibly\b",
]

# Explicit judgments about an argument's weight. The move that is everywhere in
# the benchmark sets and nearly absent from Ashwin's 1L answers.
WEIGHING = [
    r"\bweak(?:er|est)?\b", r"\bstronger\b", r"\bstrongest\b", r"\bmore convincing",
    r"\bless convincing", r"\bfalls flat\b", r"\bsuspect\b", r"\bshakier\b",
    r"\bmost likely to succeed\b", r"\bweakest link\b",
]

# Self-verbs that should not be softened. Flagged when a hedge sits next to one.
SOFTENED_VERB = [
    r"\bshould probably\b", r"\bwill probably\b", r"\bwould probably\b",
    r"\bprobably should\b", r"\bmight should\b", r"\bseems like we should\b",
]

MISSING_FACT = [
    r"\bit would (?:be )?(?:help|important|useful)\b", r"\bwe (?:do not|don'?t) know\b",
    r"\bwe lack\b", r"\bmore research\b", r"\bI would need to\b",
    r"\bif .{0,60} we(?:'| w)ould\b", r"\bassum(?:e|ing|ption)\b",
]

BANNER = re.compile(
    r"^(?:\d{4,6}\s+\d{4,6}|Institution\s|Course\s|Course / Session|Event\s|"
    r"Exam Mode|Exam ID|Extegrity|Count\(s\)|Section \d+\s+\d+|Total\s+\d+|_{10,})"
    r".*$\n?",
    re.M,
)
DIVIDER = re.compile(r"^-{5,}.*$|^Answer-to-Question-_?\d+_?.*$", re.M)
SECTION_SPLIT = re.compile(r"Answer-to-Question-_?(\d+)_?")
# Headings as they actually appear in Exam4 output and in markdown: an ATX
# heading, a bolded line, or a short standalone line with no terminal
# punctuation, optionally carrying a numeric or lettered label.
HEADING = re.compile(
    r"^(?:"
    r"#{1,6}\s+\S.*"                                  # markdown
    r"|\*\*[^*\n]{2,80}\*\*\s*"                       # bolded line
    r"|(?:\d{1,2}[.)]|[A-Z][.)])\s*(?:[A-Z][^.\n]{0,58})?" # "2. Tort", "A) Formation", bare "A)"
    r"|[A-Z][^.\n;,]{1,58}[?:]"                       # "Law or equity?", "Tax?"
    r"|[A-Z][\w'’-]*(?:\s+[\w'’&-]+){0,5}"            # "Formation", "April and May"
    r")\s*$",
    re.M,
)
ENUM = re.compile(r"\((?:\d+|[ivx]+|[a-f])\)|^\s*(?:\d+\.|[-*])\s+", re.M | re.I)


def strip_exam4(text: str) -> str:
    text = BANNER.sub("", text)
    return re.sub(r"\n{3,}", "\n\n", text)


def per_1k(n: int, words: int) -> float:
    return round(n * 1000 / words, 2) if words else 0.0


def count(patterns, text: str) -> int:
    return sum(len(re.findall(p, text, re.I)) for p in patterns)


def analyse(text: str, label: str) -> dict:
    body = DIVIDER.sub("", text).strip()
    words = len(body.split())
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", body) if s.strip()]
    paras = [p for p in re.split(r"\n\s*\n", body) if len(p.split()) > 3]
    headings = HEADING.findall(text)
    first = sentences[0].strip() if sentences else ""
    second = sentences[1].strip() if len(sentences) > 1 else ""
    return {
        "label": label,
        "words": words,
        "sentences": len(sentences),
        "mean_sentence_words": round(words / len(sentences), 1) if sentences else 0,
        "paragraphs": len(paras),
        "median_paragraph_words": sorted(len(p.split()) for p in paras)[len(paras) // 2] if paras else 0,
        "headings": len(headings),
        "heading_text": [h.strip() for h in headings][:20],
        "enumerated_markers": len(ENUM.findall(body)),
        "first_sentence": first[:400],
        "second_sentence": second[:400],
        "last_sentence": sentences[-1].strip()[:400] if sentences else "",
        "hedge_per_1k": per_1k(count(HEDGE, body), words),
        "verdict_per_1k": per_1k(count(VERDICT, body), words),
        "weighing_per_1k": per_1k(count(WEIGHING, body), words),
        "missing_fact_moves": count(MISSING_FACT, body),
        "softened_own_verb": [m for p in SOFTENED_VERB for m in re.findall(p, body, re.I)],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--caps", help="comma-separated word cap per section, in order")
    ap.add_argument("--exam4", action="store_true", help="strip Exam4 page banners")
    args = ap.parse_args()

    raw = open(args.path, encoding="utf-8", errors="replace").read()
    if args.exam4 or "Extegrity" in raw:
        raw = strip_exam4(raw)

    parts = SECTION_SPLIT.split(raw)
    sections = []
    if len(parts) > 1:
        for i in range(1, len(parts), 2):
            sections.append(analyse(parts[i + 1], f"Q{parts[i]}"))
    else:
        sections.append(analyse(raw, "whole"))

    if args.caps:
        caps = [int(c) for c in args.caps.split(",")]
        for sec, cap in zip(sections, caps):
            sec["cap"] = cap
            sec["cap_utilisation_pct"] = round(sec["words"] * 100 / cap, 1)

    total = sum(s["words"] for s in sections)
    print(json.dumps({
        "path": args.path,
        "total_words": total,
        "sections": sections,
        "benchmarks": {
            "baude_exemplar_cap_utilisation_pct": "98.1-100.0",
            "rappaport_model_verdict_per_1k": "18.8-20.1",
            "ashwin_1L_verdict_per_1k": "3.2-9.5",
            "note": "hedge_per_1k below ~1.5 is not a virtue; see the diagnostic",
        },
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
