#!/usr/bin/env python3
"""Generate spaced-repetition flashcards from the doctrine modules.

Cards are derived, not authored: the module is the source of truth, and this
script transforms its Rule statement, Elements and Standard of review into
cards in <class>/60-drills/<Module>.md.

**Review schedule is user data and is never destroyed.** obsidian-spaced-
repetition stores scheduling in the card file as an HTML comment, e.g.
`<!--SR:!2026-11-02,14,270-->`. On every run this script reads the existing
card file, keys each schedule to the exact question text it followed, and
re-attaches it to the regenerated card. A card whose question text changes
loses its schedule, because the plugin has no way to know they are the same
card — so treat question wording as close to permanent.

  build_cards.py --class conlaw                   # every module
  build_cards.py --class conlaw --only "Nondelegation" "Bills of"
  build_cards.py --class conlaw --dry-run
"""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", ".."))
SR = re.compile(r"<!--SR:.*?-->")
SEP = "?"                      # plugin's multiline separator


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def fm(text, key):
    m = re.search(r"^%s:\s*(.+)$" % key, text.split("---")[1], re.M)
    return m.group(1).strip().strip('"') if m else ""


def section(body, name):
    m = re.search(r"^## %s\n(.*?)(?=\n## |\Z)" % re.escape(name), body, re.S | re.M)
    return m.group(1).strip() if m else ""


def harvest_schedules(path):
    """question text -> SR comment, from the card file as it stands."""
    if not os.path.exists(path):
        return {}
    out, q = {}, None
    block = []
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.strip() == SEP:
            q = "\n".join(block).strip()
            block = []
            continue
        m = SR.search(line)
        if m and q:
            out[q] = m.group(0)
            q = None
            block = []
            continue
        if line.startswith("#") or not line.strip():
            if not q:
                block = []
            continue
        block.append(line)
    return out


CAP = 70          # words; an answer longer than this cannot be self-graded

ABBR = {"co","corp","inc","ltd","llc","llp","assn","bros","no","nos","art","cl","u.s","s.ct",
        "f","supp","ch","r","jr","sr","mr","mrs","ms","dr","st","rev","op","o.l.c","stat","cir",
        "ct","const","amend","v","vs","cf","e.g","i.e","al","ed","ex","re","pp","p","n",
        "jan","feb","mar","apr","jun","jul","aug","sept","sep","oct","nov","dec"}


def sentences(text):
    """Split into sentences without cutting a case name or a wikilink.

    A naive split on [.?!] breaks "Youngstown Sheet & Tube Co. v. Sawyer" after
    "Co.", which severs a wikilink and drops a card boundary inside it. So
    wikilinks are masked out first, and a break that follows a known legal
    abbreviation or a lone initial is stitched back up.
    """
    links = []

    def mask(m):
        links.append(m.group(0))
        return "\x00%d\x00" % (len(links) - 1)

    t = re.sub(r"\[\[[^\]]*\]\]", mask, text)
    raw = re.split(r"(?<=[.?!])\s+", t)
    out = []
    for piece in raw:
        if out:
            last = out[-1]
            w = re.sub(r"[^A-Za-z.]", "", last.split()[-1] if last.split() else "").rstrip(".").lower()
            if w in ABBR or len(w) == 1:
                out[-1] = last + " " + piece
                continue
        out.append(piece)
    return [re.sub(r"\x00(\d+)\x00", lambda m: links[int(m.group(1))], x) for x in out]


def bullets(sec):
    """Top-level bullets of a section, each with its sub-bullets folded in."""
    out, cur = [], None
    for ln in sec.split("\n"):
        if not ln.strip():
            continue
        ind = len(ln) - len(ln.lstrip())
        if re.match(r"^(\d+\.|[-*+])\s", ln.strip()) and ind == 0:
            if cur:
                out.append(cur)
            cur = [ln.strip()]
        elif cur is not None:
            cur.append(ln.strip())
    if cur:
        out.append(cur)
    return out


def lead(b):
    """The checkable claim at the head of a bullet: its bold phrase, else its first sentence."""
    first = re.sub(r"^(\d+\.|[-*+])\s*", "", b[0])
    m = re.match(r"\*\*(.+?)\*\*", first)
    if m:
        return m.group(1).rstrip(".?!")
    return re.split(r"(?<=[.?!])\s", first)[0].rstrip(".?!")


def trim(parts, cap=CAP):
    """Join until the cap, so no answer outruns what you can say aloud."""
    out, n = [], 0
    for p in parts:
        w = len(p.split())
        if out and n + w > cap:
            break
        out.append(p)
        n += w
    return "\n".join(out)


def cards_for(body, name):
    """-> list of (question, answer). Recall cards, decomposed so each answer is gradeable."""
    out = []
    rule = section(body, "Rule statement")
    if rule:
        prose = [p for p in rule.split("\n") if p.strip() and not p.lstrip().startswith(("-", "*"))]
        if prose:
            # The schema puts the operative rule first and the contest after it, so a
            # long rule splits at that seam rather than being truncated.
            sents = sentences(" ".join(x.strip() for x in prose))
            head, n = [], 0
            for sv in sents:
                if head and n + len(sv.split()) > CAP:
                    break
                head.append(sv)
                n += len(sv.split())
            tail = sents[len(head):]
            out.append(("State the rule.", " ".join(head)))
            # chunk the contest the same way, so no single answer outruns the cap
            chunks, cur, n = [], [], 0
            for sv in tail:
                if cur and n + len(sv.split()) > CAP:
                    chunks.append(cur); cur, n = [], 0
                cur.append(sv); n += len(sv.split())
            if cur:
                chunks.append(cur)
            for i, ch in enumerate(chunks, 1):
                q = "Where is that rule contested, or what is the competing formulation?"
                if len(chunks) > 1:
                    q += " (%d of %d)" % (i, len(chunks))
                out.append((q, " ".join(ch)))
        quotes = [l.strip() for l in rule.split("\n") if l.lstrip().startswith(("-", "*"))]
        for i, q in enumerate(quotes[:3], 1):
            out.append(("The court's own words, formulation %d of %d." % (i, min(len(quotes), 3)), q))

    el = section(body, "Elements")
    bs = bullets(el)
    if bs:
        names = [lead(b) for b in bs]
        out.append(("Name the steps of the inquiry, in order (%d)." % len(names),
                    "\n".join("%d. %s" % (i, n) for i, n in enumerate(names, 1))))
        for i, b in enumerate(bs, 1):
            ans = trim(b[1:] or [b[0]])
            if ans.strip():
                out.append(("Step %d is *%s*. What must be shown?" % (i, names[i - 1]), ans))

    std = section(body, "Standard of review / burden")
    if std:
        out.append(("Standard of review, and who bears the burden?", trim(std.split("\n"))))

    for sec_name, q in (("Exceptions", "Carve-out %d of %d?"),
                        ("Common trap", "Trap %d of %d — the wrong answer that sounds right?")):
        bb = bullets(section(body, sec_name))
        for i, b in enumerate(bb[:4], 1):
            out.append((q % (i, min(len(bb), 4)), trim(b)))

    lc = section(body, "Leading case")
    if lc:
        first = next((l.strip() for l in lc.split("\n") if l.strip()), "")
        if first:
            out.append(("Leading case, and the fact that drove it?",
                        trim([first] + [l.strip() for l in lc.split("\n")[1:] if l.strip()][:2])))
    bc = section(body, "Best counter-case")
    if bc:
        first = next((l.strip() for l in bc.split("\n") if l.strip()), "")
        if first:
            out.append(("Best counter-case, and how do you argue each side?",
                        trim([first] + [l.strip() for l in bc.split("\n")[1:] if l.strip()][:2])))
    return out


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--class", dest="cls", required=True)
    a.add_argument("--only", nargs="*")
    a.add_argument("--dry-run", action="store_true")
    args = a.parse_args()

    base = os.path.join(VAULT, args.cls)
    mdir, ddir = os.path.join(base, "30-doctrine"), os.path.join(base, "60-drills")
    mods = sorted(f for f in os.listdir(mdir) if f.endswith(".md"))
    if args.only:
        mods = [m for m in mods if any(o.lower() in m.lower() for o in args.only)]
    if not args.dry_run:
        os.makedirs(ddir, exist_ok=True)

    total = kept = 0
    over = []
    for m in mods:
        text = open(os.path.join(mdir, m), encoding="utf-8").read()
        body = text.split("---", 2)[2]
        name = m[:-3]
        topic, sub = fm(text, "topic"), fm(text, "sub_topic")
        emph, like = fm(text, "professor_emphasis"), fm(text, "exam_likelihood")
        dst = os.path.join(ddir, name + ".md")
        sched = harvest_schedules(dst)

        cs = cards_for(body, name)
        lines = ["---",
                 "module: \"%s\"" % name.replace('"', '\\"'),
                 "class: %s" % args.cls,
                 "topic: \"%s\"" % topic.replace('"', '\\"'),
                 "professor_emphasis: %s" % (emph or "null"),
                 "exam_likelihood: %s" % (like or "null"),
                 "card_kind: recall",
                 "generated: true",
                 "---", "",
                 "#flashcards/%s/%s" % (args.cls, slug(topic) or "misc"), "",
                 "Source of truth is [[%s]]. Edit the module, then regenerate." % name, "",
                 "> [!info] %s" % (sub or name), ""]
        for q, ans in cs:
            qt = "**%s** — %s" % (name, q)
            lines += [qt, SEP, ans]
            if qt in sched:
                lines.append(sched[qt]); kept += 1
            lines.append("")
            total += 1
            w = len(ans.split())
            if w > CAP + 25 and not q.startswith("Name the steps"):
                over.append((name, q, w))
        if args.dry_run:
            print("%-62s %d cards (%d schedules kept)" % (name[:62], len(cs), sum(1 for q, _ in cs if "**%s** — %s" % (name, q) in sched)))
            continue
        open(dst, "w", encoding="utf-8").write("\n".join(lines).rstrip() + "\n")
        print("%-62s %d cards" % (name[:62], len(cs)))
    print("\n%d cards across %d modules; %d existing schedules carried forward"
          % (total, len(mods), kept))
    if over:
        print("over the %d-word cap (%d):" % (CAP, len(over)))
        for nm, q, w in over[:8]:
            print("   %3dw  %s — %s" % (w, nm[:34], q[:50]))


if __name__ == "__main__":
    main()
