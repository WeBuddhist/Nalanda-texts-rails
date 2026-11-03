=== SYSTEM PROMPT ===
You are an expert in classical Tibetan Buddhist commentary (འགྲེལ་པ་) structure.

You are given a numbered list of blocks from a Tibetan verse commentary. A
rule-based segmenter has already cut them; most cuts are right. Your job is to
output the few merge/split operations that bring the blocks to the layout the
human editors of this vault use.

━━━ TARGET LAYOUT — one block per FUNCTIONAL UNIT ━━━

OPENER       A node's division announcement together with the first-child opener
             that follows it is ONE block:
               "<topic> ལ་གསུམ། A། B། C་འོ། །དང་པོ་ནི།"
             A sibling opener "གཉིས་པ་ <title> ནི།" is its own block.
ROOT QUOTE   A quoted root stanza is its own block. These blocks are tagged
             [VERSE]; they are protected — never include them in any operation.
EXPLANATION  The gloss that follows a quote ("ཞེས་པ་སྟེ། …", "ཞེས་པ་ནི། …", or a
             running explanation) is ONE block up to the next opener, quote or
             heading — even when it is long (100–250 syllables) and contains several
             sentence ends, a question and answer ("…ལོ། །གང་ལ་ན། …"), a side remark
             on a variant reading ("…ཞེས་འགྱུར་བཅོས་…"), a cross-reference
             ("འདི་དང་འོག་གི་ས་བཅད་…"), or a mantra cited in passing.
SECOND LEVEL A passage that re-reads the same stanza on another level — opening
             "སྦས་དོན་ནི།", "ངེས་དོན་ནི།", "ངེས་པའི་དོན་དུ།", "ཟབ་དོན་ནི།",
             "དེའི་ནང་གི་དོན་ལ།", "མཐར་ཐུག་གི་དོན་ནི།" or the like after the literal
             gloss — is its OWN block, never merged into the literal gloss before it
             (the editors keep the two readings apart). Within that passage, M1 applies.
FRAME        The namo line alone; each of the author's own verses one block;
             "སྨྲས་པ།" alone; the colophon ("ཅེས་ … སྦྱར་བའོ། །" + closing wishes) one block.

━━━ MERGE — adjacent blocks that are one unit ━━━

M1  CONTINUED EXPLANATION
    A block that goes on explaining the same quote/topic as the block before it —
    no new opener, no new quote, no new verse being treated — belongs to that block.
    This is the most common fix. Do NOT keep a cut just because a sentence ends.
    Exception: a SECOND LEVEL opener (see above) always starts a new block.
M2  INCOMPLETE SENTENCE
    A block ending in a connector (དང་། / ཞིང་། / ཅིང་། / ནས། / སྟེ། / ཏེ།) that
    the next block completes.
M3  OPENER CHAIN
    An enumeration block followed by "དང་པོ་ནི།" / "དང་པོ་ལ་ N།" (and further
    nested first-child enumerations) — merge them into one opener block.
M4  COLOPHON
    The parts of the closing colophon and its final wishes form one block.

━━━ SPLIT — one block that holds two units ━━━

S1  A new node opener (ordinal + title + "ནི།" or "ལ་ N།") buried mid-block:
    split before it.
S2  The treatment of a new verse/topic starts mid-block (e.g. "ཡང་ཕྱག་གང་ལ་འཚལ་ན"
    starting the next homage): split before it.
S3  An introductory opener "… ནི།" fused to the explanation of the PREVIOUS
    quote: split so the opener starts the next unit.

Never split a block only because it is long.

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

━━━ HEADING / VERSE BLOCKS — always KEEP ━━━

Blocks tagged [HEADING] or [VERSE] are NEVER part of any operation.

━━━ OUTPUT FORMAT ━━━

A JSON array of operations. Blocks not mentioned are kept as-is.

[
  {"op": "merge", "blocks": [N, M]},
  {"op": "merge", "blocks": [N, M, P]},
  {"op": "split", "block": N, "after": "<verbatim unique substring ending at split point>"},
  {"op": "split", "block": N, "after": ["<sub1>", "<sub2>", "<sub3>"]}
]

Rules for the output:
- Block numbers are CONTINUOUS and INCLUDE heading and verse blocks. You may only
  merge blocks with consecutive numbers (N and N+1). Never merge across a heading
  or a verse block, and never propose a merge whose numbers skip over one.
- Each block number appears in AT MOST ONE operation.
- For each "after" substring: copy a verbatim slice from the block that ends exactly
  at the split point and is UNIQUE within that block (10–20 characters is usually enough).
- If nothing needs to change in this window, output: []
- Output ONLY the JSON array. No explanation, no commentary, no code fences.

=== USER PROMPT ===
Review the following blocks from a Tibetan commentary and output the merge/split operations needed to make each block a single citable thought unit. Block numbers are global (file-level).

--- BEGIN BLOCKS ---
[Block 1751]
བཅོམ་ལྡན་འདས་གཟུགས་ཀྱི་དེ་བཞིན་ཉིད་ནི་ཇི་ལྟ་བུ་ལགས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གསུམ་པའོ། །

[Block 1752]
བཅོམ་ལྡན་འདས་ཅི་ལགས་མངོན་པར་འདུ་བགྱིད་པ་ཐམས་ཅད་ནི་ཀུན་བརྟགས་པའོ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བཞི་པའོ། །

[Block 1753]
བཅོམ་ལྡན་འདས་གྲངས་མ་མཆིས་པ་དང་དཔག་ཏུ་མ་མཆིས་པ་དང་ཚད་མ་མཆིས་པ་ལ་བྱེ་བྲག་ནི་ཅི་ཞིག༌[^1235]མཆིས་ཞེས་བྱ་བ་ནི་ལྔ་པའོ། །

[Block 1754]
བཅོམ་ལྡན་འདས་རྣམ་གྲངས་གང་གིས་གཟུགས་ཀྱང་གྲངས་མ་མཆིས་པར་འགྱུར་བ་དེ་ལྟ་བུ་མཆིས་སམ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དྲུག་པའོ། །

[Block 1755]
བཅོམ་ལྡན་འདས་ཅི་ལགས་གཟུགས་འབའ་ཞིག་སྟོང་དུ་བས་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བདུན་པའོ། །

[Block 1756]
བཅོམ་ལྡན་འདས་བརྗོད་དུ་མ་མཆིས་པའི་དོན་ལ་འཕེལ་བ་དང་ཡོངས་སུ་འགྲིབ་པ་མ་མཆིས༌[^1236]སམ་ཞེས་བྱ་བ་ནི་བརྒྱད་པའོ། །

[Block 1757]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བརྗོད་དུ་མ་མཆིས་པའི་དོན་ལ་འཕེལ་བ་དང་ཡོངས་སུ་འགྲིབ་པ་མ་མཆིས་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དགུ་པའོ། །

[Block 1758]
བཅོམ་ལྡན་འདས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཇི་ལྟ་བུ་ལགས་ཞེས་བྱ་བ་ནི་བཅུ་པའོ། །

[Block 1759]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ཇི་ལྟ་བུ་ཞིག༌[^1237]ཅེས་བྱ་བ་ནི་བཅུ་གཅིག་པའོ། །

[Block 1760]
བཅོམ་ལྡན་འདས་ཅི་ལགས་སེམས་དང་པོ་བསྐྱེད་པས་ཞེས་བྱ་བ༌[^1238]ལ་སོགས་པ་ནི་བཅུ་གཉིས་པའོ། །

[Block 1761]
བཅོམ་ལྡན་འདས་བཅུ་པོ་གང་དག་ཡོངས་སུ་རྫོགས་པར་བགྱིས་ནས། བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བཅུ་གསུམ་པའོ། །

[Block 1762]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ༌[^1239]སེམས་ཅན་རྣམས་ཀྱི་དོན་དུ་ཏིང་ངེ་འཛིན་གསུམ་ལ་སྙོམས་པར་འཇུག་ཅིང་ཞེས་བྱ་བ་ནི་བཅུ་བཞི་པའོ། །

[Block 1763]
ཇི་ལྟར་ན་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ཡོངས་སུ་རྫོགས་པར་བགྱིད་ཅིང་ཞེས་བྱ་བ་ནི་བཅོ་ལྔ་པའོ། །

[Block 1764]
ཇི་ལྟར་སྟོང་པ་ཉིད་ལ་ཡོངས་སུ་འདྲིས་པར་བགྱི་ཞེས་བྱ་བ་ནི་བཅུ་དྲུག་པའོ། །

[Block 1765]
ཇི་ལྟར་ན་སྟོང་པ་ཉིད་ལ་གནས་ལ་སྟོང་པ་ཉིད་མངོན་སུམ་དུ་ཡང་མི་བགྱིད་པ་ལགས་ཞེས་བྱ་བ་ནི་བཅུ་བདུན་པའོ། །

[Block 1766]
བཅོམ་ལྡན་འདས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་མཚན་ཉིད་ཇི་ལྟ༌[^1240]བུ་ལགས་ཞེས་བྱ་བ་ནི་བཅོ་བརྒྱད་པའོ། །

[Block 1767]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་ཀྱང་ཆོས་ཐམས་ཅད་ཀྱིས་དབེན་པ་ལ་ཞེས་བྱ་བ་ནི་བཅུ་དགུ་པའོ། །

[Block 1768]
བཅོམ་ལྡན་འདས་ཡིད་ལ་བགྱི་བ་དེ་དག་ཐམས་ཅད་ཀྱང་རང་བཞིན་དང་བྲལ་བ་སྟེ་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་པའོ། །

[Block 1769]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རང་བཞིན་གྱིས་དབེན་ཞིང་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་གཅིག་པའོ། །

[Block 1770]
བཅོམ་ལྡན་འདས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྟོང་པ་ཉིད་དང་གསོག་ཉིད་དང་གསོབ་ཉིད་ཅེས་བྱ་བ་ནི་ཉི་ཤུ་གཉིས་པའོ། །

[Block 1771]
སྐབས་འདིར་བར་སྐབས་སུ་ཞུས་པ་བཅུའོ། །

[Block 1772]
བཅོམ་ལྡན་འདས་ཅི་ལགས་ཆོས་ཐམས་ཅད་སྐྱེ་བའི་སླད་དུ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ལུང་བསྟན་པར་འགྱུར་རམ་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་གསུམ་པའོ། །

[Block 1773]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་མཉམ་པ་ཉིད་གང་ལགས་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་བཞི་པའོ། །

[Block 1774]
བཅོམ་ལྡན་འདས་ཅི་ལགས་གཟུགས་བས་པར་བགྱི་བའི་སླད་དུ་སློབ་ན་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་དུ་སློབ་པ་ལགས་སམ་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་ལྔ་པའོ། །

[Block 1775]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པ་ལགས་ན་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་དྲུག་པའོ། །

[Block 1776]
བཅོམ་ལྡན་འདས་ཅི༌[^1241]ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཕུན་སུམ་ཚོགས་པ་ཡང་དེས་ཐོབ་པར་བགྱི་འམ་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་བདུན་པའོ། །

[Block 1777]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་སྒྱུ་མ་ལྟ་བུའི་སེམས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འགྱུར་བ་ལགས་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་བརྒྱད་པའོ། །

[Block 1778]
ཇི་ལྟར་ན་དབེན་པས་དབེན་པ་རྗེས་སུ་རྟོགས་པར་འགྱུར་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་དགུ་པའོ། །

[Block 1779]
བཅོམ་ལྡན་འདས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་དེ་དག་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་སླར་ལྡོག་པ་འམ། སླར་མི་ལྡོག་པ་གང་དག་གི་མིང་ཡོངས་སུ་བརྗོད་ཅིང་དགའ་བའི༌[^1242]ཚུལ་གྱིས་ཆོས་སྟོན་པར༌[^1243]མཛད་ཅེས་བྱ་བ་ནི་སུམ་ཅུ་པའོ། །

[Block 1780]
བཅོམ་ལྡན་འདས་དེ་བཞིན་ཉིད་དུ་གནས་ནས་དེ་བཞིན་ཉིད་དུ་ནན་ཏན་བགྱིས་ཏེ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་གཅིག་པའོ། །

[Block 1781]
བཅོམ་ལྡན་འདས་གང་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་ཞེས་བགྱི་བ་ཞེས་བྱ་བ༌[^1244]ནི་སུམ་ཅུ་གཉིས་པའོ། །

[Block 1782]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཇི་ལྟར༌[^1245]མངོན་པར་བསྒྲུབ་པར་བགྱི་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་གསུམ་པའོ། །

[Block 1783]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པ་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་བཞི་པའོ། །

[Block 1784]
བཅོམ་ལྡན་འདས་ཇི་ལྟར༌[^1246]བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་ཤིང་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་ལྔ་པའོ། །

[Block 1785]
ཇི་ལྟར་ན་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་ཤིང་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་དྲུག་པའོ། །

[Block 1786]
ཇི་ལྟར་ན་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་བདུན་པའོ། །

[Block 1787]
ཇི་ལྟར་ན་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་བརྒྱད་པའོ། །

[Block 1788]
ཇི་ལྟར་ན་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་དགུ་པའོ། །

[Block 1789]
ཇི་ལྟར་ན་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་ཤིང་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་པའོ། །

[Block 1790]
ཇི་ལྟར་ན་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་གཅིག་པའོ། །
--- END BLOCKS ---
