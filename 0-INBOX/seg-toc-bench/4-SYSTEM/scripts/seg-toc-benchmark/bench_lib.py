"""
Shared parsing for the segmentation + TOC benchmark.

A commentary file is read as a sequence of paragraphs (split on blank lines):
  - heading      : line(s) starting with '#'
  - transclusion : '![[...]]'  (ignored for scoring)
  - content      : everything else (trailing ^block-id stripped and kept)

All positions are measured in the *squeezed content stream*: the concatenation of
every content paragraph with all whitespace removed.  Headings and block IDs are
not part of the stream, so a gold file and a prediction made from the same text
share one coordinate system no matter how they are laid out.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

FRONTMATTER_RE = re.compile(r'^---[ \t]*\r?\n.*?\r?\n---[ \t]*\r?\n', re.DOTALL)
ID_RE = re.compile(r'\s*\^([A-Za-z0-9][A-Za-z0-9-]*)\s*$')
WS_RE = re.compile(r'\s+')
SYL_RE = re.compile(r'[ཀ-ྼ]+')


def squeeze(s: str) -> str:
    return WS_RE.sub('', s)


def syllables(s: str) -> int:
    return len(SYL_RE.findall(s))


@dataclass
class Heading:
    level: int
    title: str
    block_id: str | None
    offset: int          # squeezed-stream offset of the first content after it
    order: int           # document order among headings

    @property
    def editorial(self) -> bool:
        """Editorial (non-sa-bcad) sections use a non-numeric first ID segment: I, II, a, b."""
        return bool(self.block_id) and not self.block_id.split('-')[0].isdigit()


@dataclass
class Block:
    text: str
    block_id: str | None
    start: int
    end: int

    @property
    def syl(self) -> int:
        return syllables(self.text)

    @property
    def is_verse(self) -> bool:
        return self.text.count('\n') >= 1


@dataclass
class Doc:
    headings: list[Heading] = field(default_factory=list)
    blocks: list[Block] = field(default_factory=list)
    stream: str = ''
    title_block: Block | None = None   # the '# title ^0' line, treated as content

    def inner_ws(self) -> set[int]:
        """Squeezed offsets where the text has whitespace INSIDE a block (a space,
        or a line break between pādas) — the source's own spacing such as "། །"."""
        out = set()
        for b in self.blocks:
            pos = b.start
            prev_ws = False
            for ch in b.text:
                if ch.isspace():
                    prev_ws = True
                    continue
                if prev_ws and pos > b.start:
                    out.add(pos)
                prev_ws = False
                pos += 1
        return out

    @property
    def boundaries(self) -> set[int]:
        return {b.start for b in self.blocks if b.start > 0}


def parse(text: str, title_as_content: bool = True) -> Doc:
    """Paragraphs are split on blank lines; inside a paragraph, a heading line (or a
    transclusion line) always ends the paragraph — Markdown semantics — so a heading
    inserted without a blank line still splits the block it sits in."""
    m = FRONTMATTER_RE.match(text)
    body = text[m.end():] if m else text
    doc = Doc()
    pos = 0
    pending: list[Heading] = []

    def add_content(lines):
        nonlocal pos, pending
        s = '\n'.join(lines).strip()
        mid = ID_RE.search(s)
        bid = mid.group(1) if mid else None
        txt = ID_RE.sub('', s).strip()
        sq = squeeze(txt)
        if not sq:
            return
        doc.blocks.append(Block(txt, bid, pos, pos + len(sq)))
        for h in pending:
            h.offset = pos
        pending = []
        doc.stream += sq
        pos += len(sq)

    for p in re.split(r'\n[ \t]*\n', body):
        run = []
        for l in p.split('\n'):
            ls = l.strip()
            if not ls:
                continue
            if ls.startswith('![['):
                if run:
                    add_content(run); run = []
                continue
            if ls.startswith('#'):
                if run:
                    add_content(run); run = []
                lvl = len(ls) - len(ls.lstrip('#'))
                rest = ls.lstrip('#').strip()
                mid = ID_RE.search(rest)
                bid = mid.group(1) if mid else None
                title = ID_RE.sub('', rest).strip().strip('*').strip()
                if lvl == 1 and title_as_content:
                    sq = squeeze(title)
                    blk = Block(title, bid, pos, pos + len(sq))
                    doc.blocks.append(blk)
                    doc.title_block = blk
                    doc.stream += sq
                    pos += len(sq)
                    continue
                h = Heading(lvl, title, bid, -1, len(doc.headings))
                doc.headings.append(h)
                pending.append(h)
                continue
            run.append(l)
        if run:
            add_content(run)
    for h in pending:
        h.offset = pos
    return doc


# ── title normalisation ───────────────────────────────────────────────────────
ORDINALS = [
    'དང་པོ', 'གཉིས་པ', 'གསུམ་པ', 'བཞི་པ', 'ལྔ་པ', 'དྲུག་པ', 'བདུན་པ', 'བརྒྱད་པ',
    'དགུ་པ', 'བཅུ་པ', 'བཅུ་གཅིག་པ', 'བཅུ་གཉིས་པ',
]
ORD_RE = re.compile(r'^(?:' + '|'.join(sorted(ORDINALS, key=len, reverse=True)) + r')[་\s]*')
TAIL_RE = re.compile(r'[\s་།༎༑༔]*(?:ནི|ལ)?[\s་།༎༑༔]*$')


def norm_title(t: str) -> str:
    t = t.replace('*', '').strip()
    t = ORD_RE.sub('', t)
    t = TAIL_RE.sub('', t)
    t = re.sub(r'[\s།༎]', '', t)
    t = t.replace('་', '')
    return t
