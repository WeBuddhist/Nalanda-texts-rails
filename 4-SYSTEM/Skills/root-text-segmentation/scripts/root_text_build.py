#!/usr/bin/env python3
"""
root-text-segmentation — lay out a Tibetan verse root text (treatise, praise, ritual,
prayer) the way the vault's processed root texts are laid out.

    python root_text_build.py classify <source.md>
    python root_text_build.py prepare  <source.md> <workdir> [--tree <anchored tree.md>]
                                       [--grouping auto|sloka|free] [--front-title <title>]
                                       [--body-title <title>]
    #   free version: give <workdir>/group-in.md to prompts/stanza-grouping.md, which writes
    #   <workdir>/groups-free.json; the sloka version's groups-sloka.json is written here
    python root_text_build.py finish   <workdir>      # → final-sloka.md and/or final-free.md

classify  title + content: commentary (glosses another text) / verse / prose. Exit 0 only
          for a verse text — a commentary goes to commentary-segmentation instead.
prepare   1. pādas: a pāda ends at a shad (།) or tsheg-shad (༔) cluster before the next
             syllable; footnote markers [^n] stay on the line they follow.
          2. frame, by pattern only (added only when present):
             Sanskrit title + Tibetan title + homage → ## <front-title> ^I-0
             author's colophon (… མཛད་པ་རྫོགས་སོ།)   → ## མཛད་བྱང། ^a-0
             translators' colophon (… ལོ་ཙཱ་བ … བསྒྱུར …) → ## འགྱུར་བྱང། ^b-0
             The title line becomes "# <title> ^0". With front matter and no TOC parts,
             the body gets "## <body-title> ^1-0" (default གཞུང་དངོས།).
          3. body headings: the top-level nodes (1., 2. …, II.) of an anchored tree from
             toc-tree-extraction mode root; no tree = no body headings.
          4. stanza grouping. --grouping auto (default): a text translated from Sanskrit (it
             has "རྒྱ་གར་སྐད་དུ") gets TWO versions — sloka (4 pādas per block, counted by
             the script) and free (by sense, prompts/stanza-grouping.md); any other text
             only free. --grouping sloka|free forces one version.
finish    for each version: applies groups-<version>.json → final-<version>.md, stamps
          block IDs, verifies the text is unchanged.
"""
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent


def vault_root():
    for d in (HERE, *HERE.parents):
        if (d / "4-SYSTEM").is_dir():
            return d
    sys.exit("cannot find the vault root (a folder containing 4-SYSTEM/)")


ING = vault_root() / "4-SYSTEM/Skills/toc-tree-ingest/scripts/toc_tree_ingest.py"
PY = sys.executable
FN = r"\[\^\d+\]"
END = re.compile(r"[།༔](?:[ \t]*(?:" + FN + r")?[ \t]*[།༔])*(?:" + FN + r")*[ \t]*(?=[ཀ-ྼ༄])")
NOTES = re.compile(r"(?m)^\[\^\d+\]:")
# "…མཛད་པ་རྫོགས་སོ།", and the title between: "…ཨཱརྱ་དེ་བས་མཛད་པའི་<title>་རྫོགས་སོ།"
AUTHOR = re.compile(r"མཛད་པ(?:་|འི་)?(?:རྫོགས|ཡིན|ལགས)|མཛད་པའི་[^།]{0,300}?རྫོགས|[གཀ]ྱིས་སྦྱར་བ|བརྩམས་པ་རྫོགས")
TRANSLATOR = re.compile(r"ལོ་ཙཱ་བ|བསྒྱུར་ཅིང|ཞུས་ཏེ་གཏན་ལ་ཕབ|བསྒྱུར་བའོ|འགྱུར་བཅོས")
FRAME_SECTIONS = ("^I-0", "^a-0", "^b-0")


def norm(s):
    """For matching colophon wording: no footnote markers, no editorial parentheses,
    the non-breaking tsheg as a tsheg ("…མཛད་པ་)རྫོགས", "ལོ་ཙཱ༌[^11]བ")."""
    return re.sub(r"[()\s]", "", re.sub(FN, "", s)).replace("༌", "་")


def is_author(s):
    return bool(AUTHOR.search(norm(s)))


def is_translator(s):
    return bool(TRANSLATOR.search(norm(s)))


def syl(s):
    return len(re.findall(r"[ཀ-ྼ]+", re.sub(FN, "", s)))


def squeeze(s):
    return re.sub(r"\s+", "", s)


def no_headings(s):
    return squeeze(re.sub(r"(?m)^#.*$", "", s))


def split_doc(text):
    fm = ""
    m = re.match(r"^---\n.*?\n---\n", text, flags=re.S)
    if m:
        fm, text = m.group(0), text[m.end():]
    n = NOTES.search(text)
    body, notes = (text[:n.start()], text[n.start():]) if n else (text, "")
    return fm, body, notes


def pada_spans(run, start=0, end=None):
    end = len(run) if end is None else end
    spans, pos = [], start
    for m in END.finditer(run, start, end):
        spans.append((pos, m.end()))
        pos = m.end()
    if run[pos:end].strip():
        spans.append((pos, end))
    return spans


# ── classify ─────────────────────────────────────────────────────────────────

def classify(src):
    fm, body, _ = split_doc(src.read_text(encoding="utf-8"))
    first = next((l for l in body.splitlines() if l.strip()), "")
    title = re.sub(r"^#+\s*", "", first)
    t = re.sub(FN, "", body)
    n = syl(t) or 1
    gloss = len(re.findall(r"ཞེས་པ་(?:ནི|སྟེ|ལ)|ཞེས་བྱ་བ་(?:ནི|ལ)", t)) / n * 1000
    clauses = re.split(r"[།༔]", t)
    verse = sum(syl(c) for c in clauses if 6 <= syl(c) <= 11) / n
    if re.search(r"འགྲེལ|རྣམ་པར་བཤད|རྣམ་བཤད|ཊཱི་ཀཱ|ཊཱི་ཀ|བཤད་སྦྱར|དཀའ་འགྲེལ", title) or gloss >= 1.0:
        kind = "commentary"
    elif verse >= 0.6:
        kind = "verse"
    else:
        kind = "prose" if verse < 0.3 else "mixed"
    print(f"{src.name}: {kind}  (title: {title[:60]} · gloss markers {gloss:.2f}/1000 syl · "
          f"verse share {verse:.0%})")
    if kind == "commentary":
        print("  → a commentary: use commentary-segmentation, not this skill")
    elif kind in ("prose", "mixed"):
        print("  → not (mainly) verse: this skill's stanza layout does not fit; ask the editor")
    return 0 if kind == "verse" else 1


# ── prepare ──────────────────────────────────────────────────────────────────

def prepare(src, work, tree, grouping, front_title, body_title):
    work.mkdir(parents=True, exist_ok=True)
    text = src.read_text(encoding="utf-8")
    fm, body, notes = split_doc(text)
    lines = body.strip("\n").split("\n")
    title_line = lines[0].strip() if lines and lines[0].lstrip().startswith("#") else None
    run = "\n".join(lines[1:] if title_line else lines).strip()
    run = re.sub(r"\s*\n\s*", " ", run)          # one run; boundaries are re-derived
    report = []

    # 1–2a. front matter: Sanskrit title / Tibetan title / homage
    front, pos = [], 0
    i = run.find("བོད་སྐད་དུ")
    if "རྒྱ་གར་སྐད་དུ" in run[:200] and 0 < i < 600:
        h = re.compile(r"ཕྱག་འཚལ་ལོ").search(run, i)
        if h and h.start() - i < 600:
            cuts = [m.end() for m in END.finditer(run, i, h.start())]
            hom = cuts[-1] if cuts else h.start()
            m = END.search(run, h.end())
            pos = m.end() if m else len(run)
            front = [run[:i].strip(), run[i:hom].strip(), run[hom:pos].strip()]
            report.append("front matter (Sanskrit title, Tibetan title, homage)")

    # 2b. colophons: the tail of the text that is out of metre or worded as a colophon
    spans = pada_spans(run, pos)
    metre = Counter(syl(run[a:b]) for a, b in spans).most_common(1)[0][0] if spans else 0
    k = len(spans)
    while k > 0:
        seg = run[spans[k - 1][0]:spans[k - 1][1]]
        # colophon region: colophon wording, a line out of metre, or prose — a clause that
        # ends on a single shad ("…དང་།") where a pāda ends on "། །" / "ག །" / "༔"
        prose = not re.search(r"(?:།[\s་]*(?:" + FN + r")?[\s]*།|ག\s+།|༔)[\s།༔]*(?:" + FN + r")*\s*$", seg)
        if is_author(seg) or is_translator(seg) or abs(syl(seg) - metre) > 2 or prose:
            k -= 1
        else:
            break
    # a colophon starts at its own wording: closing verses in another metre (a dedication
    # in 9- or 11-syllable lines after 7-syllable verse) stay in the body
    while k < len(spans) and not (is_author(run[spans[k][0]:spans[k][1]])
                                  or is_translator(run[spans[k][0]:spans[k][1]])):
        k += 1
    tail = run[spans[k][0]:].strip() if k < len(spans) else ""
    if tail and not (is_author(tail) or is_translator(tail)):
        k, tail = len(spans), ""                 # out-of-metre lines, but no colophon
    colophons = []
    if tail:
        # the author's colophon ends with the first clause that completes its wording
        ends = [m.end() for m in END.finditer(tail)] + [len(tail)]
        cut = next((e for e in ends if is_author(tail[:e])), None)
        if cut is not None:
            colophons.append(("## མཛད་བྱང། ^a-0", tail[:cut].strip()))
            rest = tail[cut:].strip()
        else:
            rest = tail
        if rest and is_translator(rest):
            colophons.append(("## འགྱུར་བྱང། ^b-0", rest))
        elif rest:
            colophons[-1:] = [(colophons[-1][0], colophons[-1][1] + " " + rest)] if colophons else \
                [("## མཛད་བྱང། ^a-0", rest)]
        report += ["author's colophon" if "^a-0" in h else "translators' colophon" for h, _ in colophons]
    padas = [run[a:b].strip() for a, b in spans[:k]]

    out = []
    if title_line:
        out.append(re.sub(r"^#+\s*", "# ", title_line).rstrip() + " ^0")
    else:
        report.append("no title line found — add '# <title> ^0' by hand")
    if front:
        out += [f"## {front_title} ^I-0"] + front
        if padas and not tree:
            # the body needs its own heading after the front matter, or its blocks would be
            # counted as front matter (^I-4 …); with a tree, its first part takes this role
            out.append(f"## {body_title} ^1-0")
            report.append(f"body heading '{body_title}' added (no TOC parts)")
    out += padas
    for h, c in colophons:
        out += [h, c]
    prepared = work / "prepared.md"
    res = fm + "\n\n".join(out) + "\n" + ("\n" + notes if notes else "")
    assert no_headings(res) == no_headings(text), "text changed — nothing written"
    prepared.write_text(res, encoding="utf-8")

    # 3. body headings: top-level tree nodes only
    nf = "no tree"
    if tree:
        keep = [l for l in tree.read_text(encoding="utf-8").splitlines()
                if l.startswith("## ") or not l.strip() or re.match(r"^\* (?:\d+|II)\.? ", l)]
        tmd, tjs = work / "tree-top.md", work / "tree-top.json"
        tmd.write_text("\n".join(keep) + "\n", encoding="utf-8")
        subprocess.run([PY, "-X", "utf8", str(ING), "parse", "--input", str(tmd), "--out", str(tjs)],
                       check=True, capture_output=True)
        r = subprocess.run([PY, "-X", "utf8", str(ING), "ingest", "--tree", str(tjs), "--commentary",
                            str(prepared), "--split-frame-nodes"], capture_output=True, text=True,
                           encoding="utf-8")
        assert "Integrity: text unchanged" in r.stdout, r.stdout + r.stderr
        m = re.search(r"Not found:\s+(\d+)", r.stdout)
        nf = f"{m.group(1) if m else '?'} not placed"
        # the front-matter section holds only its frame blocks: the author's own opening
        # verses belong to the body, so the first body heading moves up to meet them
        if front:
            t = prepared.read_text(encoding="utf-8")
            f2, b2, n2 = split_doc(t)
            bl = [x.strip() for x in re.split(r"\n\s*\n", b2) if x.strip()]
            fi = next(j for j, x in enumerate(bl) if x.startswith("## ") and "^I-0" in x)
            nxt = next((j for j in range(fi + 1, len(bl)) if bl[j].startswith("#")), None)
            gap = nxt - (fi + 1 + len(front)) if nxt is not None else 0
            if gap > 0 and not any(s in bl[nxt] for s in FRAME_SECTIONS):
                bl.insert(fi + 1 + len(front), bl.pop(nxt))
                prepared.write_text(f2 + "\n\n".join(bl) + "\n" + ("\n" + n2 if n2 else ""), encoding="utf-8")
                report.append(f"first body heading moved up {gap} pāda(s) to follow the front matter")

    # 4. stanza grouping input. Versions: a text translated from Sanskrit (it has
    #    "རྒྱ་གར་སྐད་དུ") gets two — sloka (script) and free (prompt); any other text only free.
    translated = "རྒྱ་གར་སྐད་དུ" in run[:300]
    if grouping == "auto":
        modes = ["sloka", "free"] if translated else ["free"]
    else:
        modes = ["free" if grouping in ("free", "sense") else "sloka"]
    t = split_doc(prepared.read_text(encoding="utf-8"))[1]
    lst, n, sec, sections = [], 0, None, [[]]
    for b in [x.strip() for x in re.split(r"\n\s*\n", t) if x.strip()]:
        if b.startswith("#"):
            sec = b
            lst.append("\n" + b)
            sections.append([])
        elif sec and any(s in sec for s in FRAME_SECTIONS):
            lst.append("[frame] " + b)
        else:
            n += 1
            lst.append(f"P{n}  {b}")
            sections[-1].append(n)
    (work / "group-in.md").write_text("\n".join(lst).strip() + "\n", encoding="utf-8")
    if "sloka" in modes:
        groups = [[s[j], s[min(j + 3, len(s) - 1)]] for s in sections for j in range(0, len(s), 4)]
        (work / "groups-sloka.json").write_text(json.dumps({"stanzas": groups, "notes": {}, "mode": "sloka"}),
                                                encoding="utf-8")
    json.dump({"source": str(src), "modes": modes, "translated": translated, "front": bool(front),
               "tree": str(tree) if tree else None},
              open(work / "state.json", "w", encoding="utf-8"), ensure_ascii=False)
    steps = []
    if "sloka" in modes:
        steps.append("sloka (groups-sloka.json written)")
    if "free" in modes:
        steps.append("free → run prompts/stanza-grouping.md → groups-free.json")
    print(f"pādas {n} · metre {metre} syllables · {', '.join(report) or 'no frame elements'} · "
          f"body headings: {nf} · {'translated from Sanskrit' if translated else 'not translated'} · "
          f"versions: {' + '.join(steps)}")
    for h in re.findall(r"(?m)^#.*$", prepared.read_text(encoding="utf-8")):
        print("   " + h)


# ── finish ───────────────────────────────────────────────────────────────────

def finish(work):
    state = json.loads((work / "state.json").read_text(encoding="utf-8"))
    for mode in state.get("modes", ["sloka"]):
        g = work / f"groups-{mode}.json"
        if not g.exists():
            sys.exit(f"{g} is missing — run prompts/stanza-grouping.md first (version '{mode}')")
        build(work, g, work / f"final-{mode}.md")


def build(work, groups_path, final):
    prepared = work / "prepared.md"
    text = prepared.read_text(encoding="utf-8")
    fm, body, notes = split_doc(text)
    blocks = [b.strip() for b in re.split(r"\n\s*\n", body) if b.strip()]
    groups = json.loads(groups_path.read_text(encoding="utf-8"))["stanzas"]
    ends = {z for _, z in groups}
    out, cur, n, sec = [], [], 0, None
    for b in blocks:
        if b.startswith("#"):
            assert not cur, f"a stanza crosses the heading {b}"
            sec = b
            out.append(b)
        elif sec and any(s in sec for s in FRAME_SECTIONS):
            out.append(b)
        else:
            n += 1
            cur.append(b)
            if n in ends:
                out.append("\n".join(cur))
                cur = []
    assert not cur and [i for a, z in groups for i in range(a, z + 1)] == list(range(1, n + 1)), \
        f"{groups_path.name} must cover every pāda once, in order"
    res = fm + "\n\n".join(out) + "\n" + ("\n" + notes if notes else "")
    assert squeeze(res) == squeeze(text), "text changed — nothing written"
    final.write_text(res, encoding="utf-8")
    # block IDs: stamp against the tree's JSON if there is one, else a frame-only tree
    tjs = work / "tree-top.json"
    if not tjs.exists():
        tjs.write_text(json.dumps({"source": "", "total_nodes": 0, "max_depth": 0, "nodes": []}), encoding="utf-8")
    r = subprocess.run([PY, "-X", "utf8", str(ING), "ingest", "--tree", str(tjs), "--commentary", str(final),
                        "--stamp-body-ids"], capture_output=True, text=True, encoding="utf-8")
    assert "Integrity: text unchanged" in r.stdout, r.stdout + r.stderr
    sizes = [z - a + 1 for a, z in groups]
    print(f"{final}: {len(groups)} stanzas — " + ", ".join(f"{s} lines ×{sizes.count(s)}" for s in sorted(set(sizes))))


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    if not a:
        sys.exit(__doc__)
    if a[0] == "classify":
        sys.exit(classify(Path(a[1])))
    elif a[0] == "prepare":
        t = opt("--tree")
        prepare(Path(a[1]), Path(a[2]), Path(t) if t else None, opt("--grouping", "auto"),
                opt("--front-title", "ཀླད་ཀྱི་དོན།"), opt("--body-title", "གཞུང་དངོས།"))
    elif a[0] == "finish":
        finish(Path(a[1]))
    else:
        sys.exit(__doc__)
