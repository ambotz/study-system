#!/usr/bin/env python3
"""Re-wrap prose in vault markdown.

Joins hard-wrapped prose back into logical lines, then optionally re-wraps at a
given width. Frontmatter, headings, tables, code fences, callouts, wikilinks and
blank lines are left exactly as found; a wikilink is never split across a line.

  rewrap.py --path busorg/30-doctrine            # unwrap fully (one line per paragraph)
  rewrap.py --path busorg/10-cases --width 100   # re-wrap at 100 columns
  rewrap.py --path X --width 100 --out DIR       # write copies instead of editing
"""
import argparse, os, re, sys

FENCE = re.compile(r"^\s*(```|~~~)")
SKIP = re.compile(r"^\s*(#{1,6}\s|\||>|---\s*$|===)")
BULLET = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+")


def wrap(text, width, indent):
    """Greedy wrap that never breaks inside [[...]] or `...`."""
    toks, buf, depth = [], "", 0
    for ch in text:
        buf += ch
        if buf.endswith("[["):
            depth += 1
        elif buf.endswith("]]") and depth:
            depth -= 1
        if ch == " " and depth == 0:
            toks.append(buf)
            buf = ""
    if buf:
        toks.append(buf)
    lines, cur = [], indent
    for t in toks:
        if cur.strip() and len(cur) + len(t.rstrip()) > width:
            lines.append(cur.rstrip())
            cur = indent + t
        else:
            cur += t
    if cur.strip():
        lines.append(cur.rstrip())
    return lines


def process(txt, width):
    head = ""
    if txt.startswith("---"):
        p = txt.split("---", 2)
        if len(p) > 2:
            head, txt = "---" + p[1] + "---", p[2]
    src = txt.split("\n")
    out, i, fence = [], 0, False
    while i < len(src):
        ln = src[i]
        if FENCE.match(ln):
            fence = not fence
            out.append(ln)
            i += 1
            continue
        if fence or not ln.strip() or SKIP.match(ln):
            out.append(ln)
            i += 1
            continue
        m = BULLET.match(ln)
        if m:
            lead = m.group(0)
            cont = " " * len(lead)
            body = ln[len(lead):].strip()
            base = len(m.group(1))
            i += 1
            # fold continuation lines: indented deeper than the marker, not a new bullet
            while i < len(src) and src[i].strip() and not FENCE.match(src[i]) \
                    and not SKIP.match(src[i]) and not BULLET.match(src[i]) \
                    and len(src[i]) - len(src[i].lstrip()) > base:
                body += " " + src[i].strip()
                i += 1
            if width:
                w = wrap(body, width, cont)
                out.append(lead + w[0][len(cont):] if w else lead.rstrip())
                out.extend(w[1:])
            else:
                out.append(lead + body)
        else:
            base = len(ln) - len(ln.lstrip())
            body = ln.strip()
            i += 1
            while i < len(src) and src[i].strip() and not FENCE.match(src[i]) \
                    and not SKIP.match(src[i]) and not BULLET.match(src[i]):
                body += " " + src[i].strip()
                i += 1
            ind = " " * base
            out.extend(wrap(body, width, ind) if width else [ind + body])
    return head + "\n".join(out)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--path", required=True)
    a.add_argument("--width", type=int, default=0, help="0 = unwrap fully")
    a.add_argument("--out")
    a.add_argument("--only")
    args = a.parse_args()
    files = ([args.path] if args.path.endswith(".md")
             else [os.path.join(args.path, f) for f in sorted(os.listdir(args.path))
                   if f.endswith(".md") and (not args.only or args.only in f)])
    if args.out:
        os.makedirs(args.out, exist_ok=True)
    n = 0
    for p in files:
        s = open(p, encoding="utf-8").read()
        r = process(s, args.width)
        if not r.endswith("\n"):
            r += "\n"
        dst = os.path.join(args.out, os.path.basename(p)) if args.out else p
        if args.out or r != s:
            open(dst, "w", encoding="utf-8").write(r)
            n += 1
    print("%s %d file(s) at width %s" % ("wrote" if args.out else "rewrote", n, args.width or "unwrapped"))


if __name__ == "__main__":
    main()
