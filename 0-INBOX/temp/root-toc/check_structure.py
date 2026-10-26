#!/usr/bin/env python3
"""Pattern check of the heading structure of finished root texts (processed/root-gemini).

    py -X utf8 0-INBOX/temp/root-toc/check_structure.py [--size large] [ids…]

Per file:
  ids        heading IDs follow the tree: ## = ^N-0, ### = ^N-M-0 under its parent, siblings
             numbered 1, 2, 3 … without gaps or repeats; II only before 1; a- (colophons) last
  blocks     content blocks of a top-level part run ^N-1 … ^N-n in order (across sub-headings)
  empty      a heading with no text before the next heading of the same or higher level
  ordinal    a title opening with an ordinal (དང་པོ … ) or naming its chapter (…ལེའུ་ … གཉིས་པ)
             whose number differs from its place among its siblings
  dup        two sibling headings with the same title
  long       a title of more than 40 syllables (a sentence, not a title)
  balance    one top-level part holds more than 85% of the blocks (3+ parts), or a part has
             a single block while the average is 20+
  tree       top-level headings in the file vs top-level nodes of the anchored tree
  front      language labels in the opening lines but no ཀླད་ཀྱི་དོན། ^I-0
Writes 0-INBOX/temp/root-toc/STRUCTURE-CHECK-<size>.md and prints a summary.
"""
import argparse, json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
OUT = VAULT / "0-INBOX/processed/root-gemini"
ORD = ["དང་པོ", "གཉིས་པ", "གསུམ་པ", "བཞི་པ", "ལྔ་པ", "དྲུག་པ", "བདུན་པ", "བརྒྱད་པ", "དགུ་པ", "བཅུ་པ",
       "བཅུ་གཅིག་པ", "བཅུ་གཉིས་པ", "བཅུ་གསུམ་པ", "བཅུ་བཞི་པ", "བཅོ་ལྔ་པ", "བཅུ་དྲུག་པ", "བཅུ་བདུན་པ",
       "བཅོ་བརྒྱད་པ", "བཅུ་དགུ་པ", "ཉི་ཤུ་པ", "ཉེར་གཅིག་པ", "ཉེར་གཉིས་པ", "ཉེར་གསུམ་པ", "ཉེར་བཞི་པ",
       "ཉེར་ལྔ་པ", "ཉེར་དྲུག་པ", "ཉེར་བདུན་པ", "ཉེར་བརྒྱད་པ", "ཉེར་དགུ་པ", "སུམ་ཅུ་པ"]
ORD_ALT = "|".join(sorted(map(re.escape, ORD), key=len, reverse=True))
OPEN_ORD = re.compile(r"^(?:" + ORD_ALT + r")(?=་|$|།)")
CHAP_ORD = re.compile(r"ལེའུ(?:་[^་།]+){0,3}?་(" + ORD_ALT + r")(?=་|$|།|འོ)")
HEAD = re.compile(r"^(#{2,6})\s+(.*?)\s*\^(\S+)\s*$")
BLOCK = re.compile(r"(?<=\s)\^([0-9]+(?:-[0-9]+)+|I-\d+|II-\d+|a(?:-\d+)+)\s*$")
LABELS = re.compile(r"(?:རྒྱ་གར|རྒྱའི)་སྐད་དུ")


def syl(s):
    return len([x for x in re.split(r"[་།\s]+", s) if x])


def ordinal(title):
    t = re.sub(r"\*\*", "", title).strip()
    m = OPEN_ORD.match(t)
    if m:
        return ORD.index(m.group(0)) + 1
    m = CHAP_ORD.search(t)
    return ORD.index(m.group(1)) + 1 if m else None


def check(i, size):
    path = OUT / f"{i}.md"
    t = path.read_text(encoding="utf-8")
    body = re.split(r"(?m)^\[\^\d+\]:", t)[0]
    lines = body.split("\n")
    issues = []
    heads = []                                     # (line, level, title, id)
    blocks = []                                    # (line, id)
    for n, l in enumerate(lines, 1):
        m = HEAD.match(l)
        if m:
            heads.append((n, len(m.group(1)), m.group(2), m.group(3)))
            continue
        m = BLOCK.search(l)
        if m and not l.startswith("#"):
            blocks.append((n, m.group(1)))
    # ids: path and sibling order
    stack = {}                                     # level -> path list
    sibs = {}                                      # parent path -> [numbers]
    order = []                                     # top-level kinds in order
    for n, lv, title, hid in heads:
        if not hid.endswith("-0"):
            issues.append(("ids", n, f"heading ID ^{hid} does not end in -0"))
            continue
        p = hid[:-2].split("-")
        if p[0] in ("I", "II") or p[0] == "a":
            order.append(p[0])
            continue
        if not all(x.isdigit() for x in p):
            issues.append(("ids", n, f"odd heading ID ^{hid}"))
            continue
        depth = len(p)
        if lv - 1 != depth and not (lv == 6 and depth >= 5):
            issues.append(("ids", n, f"level {'#' * lv} but ID depth {depth} (^{hid})"))
        if depth > 1:
            parent = stack.get(depth - 1)
            if parent != p[:-1]:
                issues.append(("ids", n, f"^{hid} is not under its parent ^{'-'.join(p[:-1])}-0"))
        else:
            order.append("N")
        stack[depth] = p
        for d in list(stack):
            if d > depth:
                del stack[d]
        sibs.setdefault("-".join(p[:-1]), []).append((int(p[-1]), n, title))
    for par, lst in sibs.items():
        nums = [x[0] for x in lst]
        # a continuation volume may number its top-level parts from the author's chapter
        # number (Sh_3CCt_: ^6-0 … ^19-0); they must still run without gaps
        first = nums[0] if not par else 1
        if nums != list(range(first, first + len(nums))):
            issues.append(("ids", lst[0][1], f"siblings under {'^' + par + '-0' if par else 'top level'} "
                                             f"numbered {nums[:12]}{'…' if len(nums) > 12 else ''}"))
        seen = {}
        for k, (num, n, title) in enumerate(lst, 1):
            o = ordinal(title)
            if o and o != num and len(lst) > 1:
                issues.append(("ordinal", n, f"'{title[:40]}' says {ORD[o - 1]} but is number {num}"))
            key = re.sub(r"[\s།་*]", "", title)
            if key in seen:
                issues.append(("dup", n, f"same title as line {seen[key]}: '{title[:40]}'"))
            seen[key] = n
    if "II" in order and "N" in order and order.index("II") > order.index("N"):
        issues.append(("ids", 0, "II comes after a numbered part"))
    if "a" in order and order[-1] != "a":
        issues.append(("ids", 0, "a colophon section is not last"))
    # long titles
    for n, lv, title, hid in heads:
        if syl(title) > 40:
            issues.append(("long", n, f"title of {syl(title)} syllables: '{title[:50]}…'"))
    # empty sections
    for k, (n, lv, title, hid) in enumerate(heads):
        nxt = heads[k + 1] if k + 1 < len(heads) else None
        end = nxt[0] if nxt else len(lines) + 1
        has_text = any(n < b < end for b, _ in blocks)
        if not has_text and (nxt is None or nxt[1] <= lv):
            issues.append(("empty", n, f"'{title[:40]}' (^{hid}) has no text"))
    # content blocks per top-level part
    tops = [(n, hid[:-2]) for n, lv, title, hid in heads if re.fullmatch(r"\d+-0", hid)]
    counts = {}
    for k, (n, top) in enumerate(tops):
        end = tops[k + 1][0] if k + 1 < len(tops) else len(lines) + 1
        frame = next((h[0] for h in heads if h[0] > n and h[3].startswith(("a-", "I-", "II-"))), end)
        end = min(end, frame)
        ids = [b for ln, b in blocks if n < ln < end]
        counts[top] = len(ids)
        want = [f"{top}-{j}" for j in range(1, len(ids) + 1)]
        if ids != want:
            bad = next(j for j, (a, b) in enumerate(zip(ids, want)) if a != b) if len(ids) == len(want) else min(len(ids), len(want))
            issues.append(("blocks", n, f"part {top}: block IDs break at #{bad + 1} "
                                        f"(^{ids[bad] if bad < len(ids) else '—'} for ^{want[bad] if bad < len(want) else '—'})"))
    # balance
    if len(counts) >= 3:
        tot = sum(counts.values())
        big = max(counts, key=counts.get)
        if tot and counts[big] / tot > 0.85:
            issues.append(("balance", 0, f"part {big} holds {counts[big]} of {tot} blocks ({counts[big] * 100 // tot}%)"))
        avg = tot / len(counts)
        for top, c in counts.items():
            if c <= 1 and avg >= 20:
                issues.append(("balance", 0, f"part {top} has {c} block(s) (average {avg:.0f})"))
    # tree
    tree = VAULT / f"0-INBOX/temp/TOC-{i}/toc-tree-anchored-{i}.md"
    if tree.exists():
        tl = tree.read_text(encoding="utf-8").splitlines()
        n_top = len([l for l in tl if re.match(r"^\* \d+\. ", l)])
        n_child = len([l for l in tl if re.match(r"^\s+\* \d+\.\d+ ", l)])
        want = n_top + (n_child if n_top == 1 else 0)
        have = len([h for h in heads if re.fullmatch(r"\d+(?:-\d+)?-0", h[3])
                    and (n_top == 1 or re.fullmatch(r"\d+-0", h[3]))])
        if have != want:
            issues.append(("tree", 0, f"{have} headings in the file, {want} in the tree"))
    # front
    src = (VAULT / f"0-INBOX/root/{i}.md").read_text(encoding="utf-8")
    if LABELS.search(src[:800]) and "^I-0" not in t:
        issues.append(("front", 0, "language labels at the start but no ཀླད་ཀྱི་དོན། ^I-0"))
    return heads, counts, issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", default="large", choices=["small", "medium", "large", "all"])
    ap.add_argument("--dir", default=None, help="folder of finished files (default processed/root-gemini)")
    ap.add_argument("ids", nargs="*")
    a = ap.parse_args()
    global OUT
    if a.dir:
        OUT = (VAULT / a.dir).resolve()
    st = json.loads((HERE / "status.json").read_text(encoding="utf-8"))
    ids = a.ids or [k for k, r in st.items() if (a.size == "all" or r.get("size") == a.size)
                    and (OUT / f"{k}.md").exists()]
    rows, detail, tally = [], [], {}
    for i in ids:
        heads, counts, issues = check(i, st[i].get("size"))
        kinds = sorted({k for k, _, _ in issues})
        for k in kinds:
            tally[k] = tally.get(k, 0) + 1
        tops = len([h for h in heads if re.fullmatch(r"\d+-0", h[3])])
        subs = len([h for h in heads if re.fullmatch(r"\d+(?:-\d+)+-0", h[3])])
        rows.append(f"| {i} | {tops} | {subs} | {sum(counts.values())} | "
                    f"{', '.join(f'{k} {sum(1 for x in issues if x[0] == k)}' for k in kinds) or 'ok'} |")
        if issues:
            detail.append(f"\n### {i}\n")
            detail += [f"- **{k}**{f' (line {n})' if n else ''}: {msg}" for k, n, msg in issues]
    doc = HERE / f"STRUCTURE-CHECK-{a.size}{'-' + OUT.parent.name if a.dir else ''}.md"
    doc.write_text(f"# Structure check — {a.size} root texts\n\n"
                   "Made by `check_structure.py` (see its docstring for what each check means).\n\n"
                   "| Text | Parts | Sub-headings | Blocks | Findings |\n|---|---|---|---|---|\n"
                   + "\n".join(rows) + "\n\n## Details\n" + "\n".join(detail) + "\n", encoding="utf-8")
    print(f"{len(ids)} texts · clean {sum(1 for r in rows if r.endswith('| ok |'))} · "
          + " · ".join(f"{k} in {v}" for k, v in sorted(tally.items())) + f"\n→ {doc}")


if __name__ == "__main__":
    main()
