#!/usr/bin/env python3
"""
root-text-segmentation — lay out a Tibetan root text (treatise, praise, ritual, prayer,
letter) the way the vault's processed root texts are laid out: verse texts as stanzas,
prose texts as paragraphs with their verse passages as stanzas.

    python root_text_build.py classify <source.md>
    python root_text_build.py prepare  <source.md> <workdir> [--tree <anchored tree.md>]
                                       [--form auto|verse|prose]
                                       [--grouping auto|sloka|free] [--front-title <title>]
                                       [--body-title <title>]
    #   verse: give <workdir>/group-in.md to prompts/stanza-grouping.md → groups-free.json;
    #          the sloka version's groups-sloka.json is written here
    #   prose: give <workdir>/group-in.md to prompts/prose-grouping.md → groups-prose.json
    python root_text_build.py finish   <workdir>   # → final-sloka.md / final-free.md / final-prose.md

classify  content first, title second: commentary (glosses another text) / verse / mixed /
          prose. Verse share counts only metrical lines (a clause with the same syllable
          count as a neighbour); a commentary word in the title does not make a verse text
          a commentary ("…ཚད་མ་རྣམ་འགྲེལ།", "བྱང་ཆུབ་སེམས་ཀྱི་འགྲེལ་པ།"). Exit 0 for
          verse, mixed and prose (prepare picks the form); 1 for a commentary, which goes to
          commentary-segmentation.
prepare   1. units. verse form: pādas — a pāda ends at a shad (།) or tsheg-shad (༔) cluster
             before the next syllable; footnote markers [^n] stay on the line they follow.
             prose form: sentences — a sentence ends at a final verb (…འོ། …སོ། …ཏོ། …ནོ།
             …ཤོག …ཅིག …ཞེ་ན།); verse passages inside (4+ lines of one metre, each closed by
             "། །") stay pāda by pāda.
          2. frame, by pattern only (added only when present):
             Sanskrit (or Chinese: རྒྱའི་སྐད་དུ།) title + Tibetan title + homage, or the
             title repeated + homage → ## <front-title> ^I-0
             the closing matter → ## མཇུག་བྱང། ^a-0, with one sub-section per colophon in
             text order (as the commentary skill does): author's (… མཛད་པ་རྫོགས་སོ།) →
             ### མཛད་བྱང། ^a-1-0, translators' (… ལོ་ཙཱ་བ … བསྒྱུར …) → ### འགྱུར་བྱང། ^a-2-0
             The title line becomes "# <title> ^0". With front matter and no TOC parts,
             the body gets "## <body-title> ^1-0" (default གཞུང་དངོས།).
          3. body headings: the top-level nodes (1., 2. …, II.) of an anchored tree from
             toc-tree-extraction mode root; no tree = no body headings.
          4. grouping. verse form, --grouping auto (default): a text translated from
             Sanskrit (it has "རྒྱ་གར་སྐད་དུ") gets TWO versions — sloka (4 pādas per block,
             counted by the script) and free (by sense, prompts/stanza-grouping.md); any
             other text only free. --grouping sloka|free forces one version.
             prose form: one version, prose (paragraphs and stanzas, prompts/prose-grouping.md).
finish    for each version: applies groups-<version>.json → final-<version>.md, stamps
          block IDs, verifies the text is unchanged. Prose sentences of one block are joined
          on one line; verse lines keep one pāda per line.
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
# "…མཛད་པ་རྫོགས་སོ།", and the title between: "…མཛད་པའི་<title>་རྫོགས་སོ།" / "…མཛད་པ་<title>་རྫོགས་སོ།"
AUTHOR = re.compile(r"མཛད་པ(?:་|འི་)?(?:རྫོགས|ཡིན|ལགས)|མཛད་པ(?:འི)?་[^།]{0,300}?རྫོགས|[གཀ]ྱིས་སྦྱར་བ|བརྩམས་པ་རྫོགས")
TRANSLATOR = re.compile(r"ལོ་ཙཱ་བ|བསྒྱུར་(?:ཅིང|ཞིང|ནས|ཏེ|བ)|ཞུས་ཏེ|གཏན་ལ་ཕབ|འགྱུར་བཅོས")
FRAME_SECTIONS = ("^I-0", "^a-")       # front matter; the closing matter and its sub-sections
COLOPHON_TITLE = {"author": "མཛད་བྱང།", "translators": "འགྱུར་བྱང།"}
COMM_TITLE = re.compile(r"འགྲེལ|རྣམ་པར་བཤད|རྣམ་བཤད|ཊཱི་ཀཱ|ཊཱི་ཀ|བཤད་སྦྱར|དཀའ་འགྲེལ")
SRC_LANG = re.compile(r"རྒྱ་གར་སྐད་དུ|རྒྱའི་སྐད་དུ|རྒྱ་ནག་སྐད་དུ")
# a clause closed the way verse lines are: "། །", "ག །", "༔"
DOUBLE = re.compile(r"(?:།[\s་]*(?:" + FN + r")?\s*།|[གཀཤ]\s+།|༔)[\s།༔]*(?:" + FN + r")*\s*$")
# a finite ending closes a prose sentence: …འོ། …སོ། …ཏོ། …ནོ། …ཤོག …ཅིག …ཞེ་ན།
FINAL = re.compile(r"(?:འོ|(?<![ཀ-ྼ])[སཏནརལདངག]ོ|ཤོག|[ཅཤ]ིག|[ཞཅཤ]ེ་ན|"
                   # the -o particle repeating a final བ / མ: "…འགྲུབ་བོ།" "…འཚམ་མོ།"
                   r"བ་[བཔ]ོ|མ་མོ)[\s་]*$")
SENT_MAX = 200          # syllables: a longer run is cut at the next clause end
VERSE_MIN = 4           # lines of one metre, each closed by "། །", make a verse passage


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

def measure(text):
    """(kind, title, gloss markers per 1000 syllables, metrical share) of a source file."""
    fm, body, _ = split_doc(text)
    first = next((l for l in body.splitlines() if l.strip()), "")
    title = re.sub(r"^#+\s*", "", first)
    t = re.sub(FN, "", body).replace("༌", "་")
    n = syl(t) or 1
    gloss = len(re.findall(r"ཞེས་པ་(?:ནི|སྟེ|ལ)|ཞེས་བྱ་བ་(?:ནི|ལ)", t)) / n * 1000
    lens = [syl(c) for c in re.split(r"[།༔]+", t) if syl(c)]
    # metrical: a clause of 5+ syllables with the same count as a neighbour
    verse = sum(m for k, m in enumerate(lens) if m >= 5 and m in
                [lens[j] for j in (k - 1, k + 1) if 0 <= j < len(lens)]) / n
    # a verse text stays verse unless it glosses heavily: one "ཞེས་པ་" in a short prayer
    # is not a commentary
    if (gloss >= 1.0 and verse < 0.6) or gloss >= 3.0 or (COMM_TITLE.search(title) and verse < 0.6):
        kind = "commentary"
    elif verse >= 0.6:
        kind = "verse"
    else:
        kind = "prose" if verse < 0.3 else "mixed"
    return kind, title, gloss, verse


def classify(src):
    kind, title, gloss, verse = measure(src.read_text(encoding="utf-8"))
    print(f"{src.name}: {kind}  (title: {title[:60]} · gloss markers {gloss:.2f}/1000 syl · "
          f"metrical share {verse:.0%})")
    if kind == "commentary":
        print("  → a commentary: use commentary-segmentation, not this skill")
    elif kind in ("prose", "mixed"):
        print("  → prose form: paragraphs, with its verse passages as stanzas (prepare --form prose)")
    elif COMM_TITLE.search(title):
        print("  → the title reads like a commentary, but the text is verse: laid out as verse")
    return 1 if kind == "commentary" else 0


# ── prepare ──────────────────────────────────────────────────────────────────

def core(s):
    """Tibetan letters and tshegs only, for comparing a title with its repetition."""
    return re.sub(r"[^ཀ-ྼ་]", "", re.sub(FN, "", s).replace("༌", "་")).strip("་")


def prose_units(run, a, b):
    """Prose body → units: sentences (S) and, inside them, verse passages pāda by pāda (V)."""
    spans = pada_spans(run, a, b)
    lens = [syl(run[x:y]) for x, y in spans]
    clean = [re.sub(r"[།༔\s]+$", "", re.sub(FN, "", run[x:y])).replace("༌", "་").strip() for x, y in spans]
    # a clause opening with "ཞེས" closes a quotation: prose, never a verse line
    dbl = [bool(DOUBLE.search(run[x:y])) and not c.startswith("ཞེས") for (x, y), c in zip(spans, clean)]
    final = [bool(FINAL.search(c)) for c in clean]
    isv = [False] * len(spans)
    # long metres drift with Sanskrit names: exact up to 9 syllables, ±1 up to 12, ±2 above
    tol = lambda m: 0 if m <= 9 else (1 if m <= 12 else 2)
    i = 0
    while i < len(spans):
        j = i
        while j < len(spans) and 5 <= lens[i] <= 25 and dbl[j]:
            ref = sorted(lens[i:j])[(j - i - 1) // 2] if j > i else lens[i]   # lines so far
            if abs(lens[j] - ref) > tol(ref):
                break
            j += 1
        # a run of rubrics of similar length ("…བྱའོ། །" "…ཕྱག་རྒྱའོ། །") is prose: in a
        # loose (long-metre) run, at most a third of the lines may end on a final verb
        loose = tol(sorted(lens[i:j])[(j - i) // 2]) > 0 if j > i else False
        # …unless the final verbs are a homage or praise refrain ("…ལ་ཕྱག་འཚལ་ལོ། །" on every
        # line); parallel prose lists ("…ནི་རྣམ་པར་སྣང་མཛད་ཀྱིའོ།") share endings too, so
        # only these refrains count
        ends = Counter(" ".join(re.findall(r"[ཀ-ྼ]+", clean[k])[-2:]) for k in range(i, j) if final[k])
        top = ends.most_common(1)[0] if ends else ("", 0)
        refrain = bool(re.search(r"ཕྱག|འཚལ|བསྟོད|འདུད", top[0])) and top[1] * 2 >= sum(final[i:j])
        if j - i >= VERSE_MIN and not (loose and not refrain and sum(final[i:j]) * 3 > j - i):
            isv[i:j] = [True] * (j - i)
        i = max(j, i + 1)
    # a line right after (or between) verse lines, closed like verse and one syllable off
    # the metre — a contraction: "…བདག་མཆིའོ། །" is 6 in a 7-syllable passage — belongs to
    # the passage; a quotation close ("…ཞེས་སོ།") never does
    for k in range(1, len(spans)):
        if isv[k] or not dbl[k] or not isv[k - 1] or "ཞེས" in run[spans[k][0]:spans[k][1]]:
            continue
        if abs(lens[k] - lens[k - 1]) <= 1:
            isv[k] = True
    # a line closed like verse with verse on both sides is verse, whatever its length (a
    # damaged or irregular pāda would otherwise split its stanza)
    for k in range(1, len(spans) - 1):
        if not isv[k] and dbl[k] and isv[k - 1] and isv[k + 1]:
            isv[k] = True
    units, types, start, size = [], [], None, 0
    for k, (x, y) in enumerate(spans):
        if isv[k]:
            if start is not None:
                units.append((start, x))
                types.append("S")
                start, size = None, 0
            units.append((x, y))
            types.append("V")
            continue
        start = x if start is None else start
        size += lens[k]
        seg = re.sub(r"[།༔\s]+$", "", re.sub(FN, "", run[x:y])).replace("༌", "་")
        if FINAL.search(seg) or size >= SENT_MAX:
            units.append((start, y))
            types.append("S")
            start, size = None, 0
    if start is not None:
        units.append((start, b))
        types.append("S")
    return [run[x:y].strip() for x, y in units], types


def prepare(src, work, tree, grouping, front_title, body_title, form="auto"):
    work.mkdir(parents=True, exist_ok=True)
    text = src.read_text(encoding="utf-8")
    if form == "auto":
        form = "verse" if measure(text)[0] == "verse" else "prose"
    fm, body, notes = split_doc(text)
    lines = body.strip("\n").split("\n")
    title_line = lines[0].strip() if lines and lines[0].lstrip().startswith("#") else None
    run = "\n".join(lines[1:] if title_line else lines).strip()
    run = re.sub(r"\s*\n\s*", " ", run)          # one run; boundaries are re-derived
    report = []

    # 1–2a. front matter: source-language title / Tibetan title / homage — or, without the
    #       language labels, the title repeated and the homage
    front, pos = [], 0
    i = run.find("བོད་སྐད་དུ")
    hom_re = re.compile(r"ཕྱག་འཚལ་ལོ")
    if SRC_LANG.search(run[:200]) and 0 < i < 600:
        h = hom_re.search(run, i)
        if h and h.start() - i < 600:
            cuts = [m.end() for m in END.finditer(run, i, h.start())]
            hom = cuts[-1] if cuts else h.start()
            m = END.search(run, h.end())
            pos = m.end() if m else len(run)
            front = [run[:i].strip(), run[i:hom].strip(), run[hom:pos].strip()]
            lang = "Chinese" if "རྒྱ་གར་སྐད" not in run[:200] else "Sanskrit"
            report.append(f"front matter ({lang} title, Tibetan title, homage)")
    elif title_line:
        # leading clauses that repeat the title or pay homage (a prose text may put the
        # homage before the title); the opening marks (༄༅། །) join the next clause. In a
        # verse text a lone homage is usually the first pāda of the first stanza: only the
        # title repetition counts there.
        t_core = core(re.sub(r"བཞུགས(?:་སོ)?", "", title_line)).split("་")
        segs, p0 = [], 0
        for m in END.finditer(run):
            if m.end() > 400 or len(segs) >= 3:
                break
            if core(run[p0:m.end()]):
                segs.append((p0, m.end()))
                p0 = m.end()
        kinds = []
        for x, y in segs:
            c = core(run[x:y]).split("་")
            if len(t_core) >= 3 and c[:3] == t_core[:3]:
                kinds.append("title")
            elif hom_re.search(run[x:y]) and form == "prose" and syl(run[x:y]) <= 20:
                kinds.append("homage")
            else:
                break
        if "title" in kinds or ("homage" in kinds and form == "prose"):
            n_front = len(kinds)
            pos = segs[n_front - 1][1]
            front = [run[x:y].strip() for x, y in segs[:n_front]]
            report.append(f"front matter ({', '.join(kinds)})")

    # 2b. colophons: the tail of the text that is out of metre or worded as a colophon
    spans = pada_spans(run, pos)
    metre = Counter(syl(run[a:b]) for a, b in spans).most_common(1)[0][0] if spans else 0
    k = len(spans)
    floor = max(0, len(spans) - 30) if form == "prose" else 0   # prose: the last 30 clauses
    while k > floor:
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
    if k >= len(spans):
        # verse after the colophon — a translator's dedication ("…ཞི་བར་ཤོག") — stops the
        # walk back; look for colophon wording among the last lines instead
        k = next((j for j in range(max(0, len(spans) - 16), len(spans))
                  if is_author(run[spans[j][0]:spans[j][1]]) or is_translator(run[spans[j][0]:spans[j][1]])),
                 len(spans))
    tail = run[spans[k][0]:].strip() if k < len(spans) else ""
    if tail and not (is_author(tail) or is_translator(tail)):
        k, tail = len(spans), ""                 # out-of-metre lines, but no colophon
    colophons = []
    if tail:
        # the author's colophon ends with the first clause that completes its wording
        ends = [m.end() for m in END.finditer(tail)] + [len(tail)]
        cut = next((e for e in ends if is_author(tail[:e])), None)
        if cut is not None:
            colophons.append(("author", tail[:cut].strip()))
            rest = tail[cut:].strip()
        else:
            rest = tail
        if rest and is_translator(rest):
            colophons.append(("translators", rest))
        elif rest:
            colophons[-1:] = [(colophons[-1][0], colophons[-1][1] + " " + rest)] if colophons else \
                [("author", rest)]
        report += ["author's colophon" if kind == "author" else "translators' colophon"
                   for kind, _ in colophons]
    if form == "prose":
        padas, types = prose_units(run, pos, spans[k][0] if k < len(spans) else len(run))
    else:
        padas = [run[a:b].strip() for a, b in spans[:k]]
        types = ["P"] * len(padas)

    out = []
    if title_line:
        out.append(re.sub(r"^#+\s*", "# ", title_line).rstrip() + " ^0")
    else:
        report.append("no title line found — add '# <title> ^0' by hand")
    if front:
        out += [f"## {front_title} ^I-0"] + front
    if padas and not tree:
        # the body needs its own heading, or its blocks would be counted as front matter
        # (^I-4 …) or get no section number; with a tree, its first part takes this role
        out.append(f"## {body_title} ^1-0")
        report.append(f"body heading '{body_title}' added (no TOC parts)")
    out += padas
    if colophons:
        # the closing matter as in the commentary skill: ## མཇུག་བྱང། ^a-0, one ### per
        # colophon in text order (^a-1-0, ^a-2-0)
        out.append("## མཇུག་བྱང། ^a-0")
        for i, (kind, c) in enumerate(colophons, 1):
            out += [f"### {COLOPHON_TITLE[kind]} ^a-{i}-0", c]
    prepared = work / "prepared.md"
    res = fm + "\n\n".join(out) + "\n" + ("\n" + notes if notes else "")
    assert no_headings(res) == no_headings(text), "text changed — nothing written"
    prepared.write_text(res, encoding="utf-8")

    # 3. body headings: top-level tree nodes only
    nf = "no tree"
    if tree:
        tl = tree.read_text(encoding="utf-8").splitlines()
        # top-level nodes only — but a tree with a single numbered top node (one rite
        # section, one chapter) would give a single heading: its children count too
        child = len([l for l in tl if re.match(r"^\* \d+\. ", l)]) == 1
        keep = [l for l in tl if l.startswith("## ") or not l.strip() or re.match(r"^\* (?:\d+|II)\.? ", l)
                or (child and re.match(r"^\s+\* \d+\.\d+ ", l))]
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
    if form == "prose":
        modes = ["prose"]
    elif grouping == "auto":
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
            lst.append(f"{types[n - 1]}{n}  {b}")
            sections[-1].append(n)
    (work / "group-in.md").write_text("\n".join(lst).strip() + "\n", encoding="utf-8")
    if "sloka" in modes:
        groups = [[s[j], s[min(j + 3, len(s) - 1)]] for s in sections for j in range(0, len(s), 4)]
        (work / "groups-sloka.json").write_text(json.dumps({"stanzas": groups, "notes": {}, "mode": "sloka"}),
                                                encoding="utf-8")
    assert n == len(types), "unit count changed between prepare steps"
    json.dump({"source": str(src), "form": form, "modes": modes, "translated": translated,
               "front": bool(front), "tree": str(tree) if tree else None, "types": "".join(types)},
              open(work / "state.json", "w", encoding="utf-8"), ensure_ascii=False)
    steps = []
    if "sloka" in modes:
        steps.append("sloka (groups-sloka.json written)")
    if "free" in modes:
        steps.append("free → run prompts/stanza-grouping.md → groups-free.json")
    if "prose" in modes:
        steps.append("prose → run prompts/prose-grouping.md → groups-prose.json")
    if form == "prose":
        passages = len(re.findall(r"V+", "".join(types)))
        units = (f"prose: {types.count('S')} sentences, {types.count('V')} verse lines in "
                 f"{passages} passage(s)")
    else:
        units = f"pādas {n} · metre {metre} syllables"
    print(f"{units} · {', '.join(report) or 'no frame elements'} · "
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
            prompt = "prose-grouping.md" if mode == "prose" else "stanza-grouping.md"
            sys.exit(f"{g} is missing — run prompts/{prompt} first (version '{mode}')")
        build(work, g, work / f"final-{mode}.md", state.get("types"))


def build(work, groups_path, final, types=None):
    prepared = work / "prepared.md"
    text = prepared.read_text(encoding="utf-8")
    fm, body, notes = split_doc(text)
    blocks = [b.strip() for b in re.split(r"\n\s*\n", body) if b.strip()]
    groups = json.loads(groups_path.read_text(encoding="utf-8"))["stanzas"]
    ends = {z for _, z in groups}
    kind =lambda i: types[i - 1] if types else "P"
    for a, z in groups:
        assert len({kind(i) for i in range(a, z + 1)}) == 1, \
            f"block [{a}, {z}] mixes prose sentences and verse lines"
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
                # a prose paragraph runs on one line; verse keeps one pāda per line
                out.append((" " if kind(n) == "S" else "\n").join(cur))
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
    if types and "S" in types:
        para = [z - a + 1 for a, z in groups if kind(a) == "S"]
        st = [z - a + 1 for a, z in groups if kind(a) != "S"]
        print(f"{final}: {len(para)} paragraphs (sentences per paragraph: "
              + ", ".join(f"{s} ×{para.count(s)}" for s in sorted(set(para))) + f") · {len(st)} stanzas"
              + (" (" + ", ".join(f"{s} lines ×{st.count(s)}" for s in sorted(set(st))) + ")" if st else ""))
        return
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
                opt("--front-title", "ཀླད་ཀྱི་དོན།"), opt("--body-title", "གཞུང་དངོས།"),
                opt("--form", "auto"))
    elif a[0] == "finish":
        finish(Path(a[1]))
    else:
        sys.exit(__doc__)
