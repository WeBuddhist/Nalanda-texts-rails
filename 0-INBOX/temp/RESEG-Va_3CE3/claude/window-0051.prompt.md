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

[Block 1791]
ཇི་ལྟར་ན་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་གཉིས་པའོ། །

[Block 1792]
ཇི་ལྟར་ན་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་གསུམ་པའོ། །

[Block 1793]
ཇི་ལྟར་ན་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་བཞི་པའོ། །

[Block 1794]
ཇི་ལྟར་ན་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་ཤིང་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་ལྔ་པའོ། །

[Block 1795]
ཇི་ལྟར་ན་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་དྲུག་པའོ། །

[Block 1796]
ཇི་ལྟར་ན་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་བདུན་པའོ། །

[Block 1797]
ཇི་ལྟར་ན་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་བརྒྱད་པའོ། །

[Block 1798]
ཇི་ལྟར་ན་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་དགུ་པའོ། །

[Block 1799]
ཇི་ལྟར་ན་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་ཤིང་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་པའོ། །

[Block 1800]
ཇི་ལྟར་ན་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་གཅིག་པའོ། །

[Block 1801]
ཇི་ལྟར་ན་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་གཉིས་པའོ། །

[Block 1802]
ཇི་ལྟར་ན་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་གསུམ་པའོ། །

[Block 1803]
ཇི་ལྟར་ན་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་བཞི་པའོ། །

[Block 1804]
ཇི་ལྟར་ན་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་ཤིང་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་ལྔ་པའོ། །

[Block 1805]
ཇི་ལྟར་ན་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ༌[^1247]དྲུག་པའོ། །

[Block 1806]
ཇི་ལྟར་ན་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་བདུན་པའོ། །

[Block 1807]
ཇི་ལྟར་ན་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་བརྒྱད་པའོ། །

[Block 1808]
ཇི་ལྟར་ན་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་དགུ་པའོ། །

[Block 1809]
ཇི་ལྟར་ན་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་ཤིང་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་པའོ། །

[Block 1810]
ཇི་ལྟར་ན་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་གཅིག་པའོ། །

[Block 1811]
ཇི་ལྟར་ན་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་གཉིས་པའོ། །

[Block 1812]
ཇི་ལྟར་ན་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་གསུམ་པའོ། །

[Block 1813]
ཇི་ལྟར་ན་བསམ་གཏན་གྱི༌[^1248]ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་བཞི་པའོ། །

[Block 1814]
བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་གང༌[^1249]ཐབས་མཁས་པ་དེ་ལྟ་བུ་དང་ལྡན་པ་དེ་ཡུན་རིང་པོ་ཇི་སྲིད་ཅིག་ནས་ཡང་དག་པར་ཞུགས་པ་ལགས་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་ལྔ་པའོ། །

[Block 1815]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་གང༌[^1250]ཐབས་མཁས་པ་དེ་ལྟ་བུ་དང་ལྡན་པ་དེས་སངས་རྒྱས་ཇི་སྙེད་ཅིག་བསྙེན་བཀུར་བགྱིས་པ༌[^1251]ལགས་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་དྲུག་པའོ། །

[Block 1816]
དགེ་བའི་རྩ་བ་ཇི་ཙམ་ཞིག་བསྐྱེད་པ་ལགས་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་བདུན་པའོ། །

[Block 1817]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས་སྟོང་པ་ལགས་ན་ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་བརྒྱད་པའོ། །

[Block 1818]
བཅོམ་ལྡན་འདས་གལ་ཏེ་དོན་གྱི་རྗེས་སུ་ཞུགས་པའི་ཆོས་གང་ཡང་བྱེ་བྲག་གམ་ཐ་དད་དུ་བགྱི་བ་མ་མཆིས་ན། ཇི་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྔ་པོ༌[^1252]དག་གི་རབ་ཅེས༌[^1253]བྱ་བ་ནི་དྲུག་ཅུ་དགུ་པའོ། །

[Block 1819]
བཅོམ་ལྡན་འདས་ཅི་ལགས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཆོས་གང་ཡང་ཡོངས་སུ་འཛིན་པའམ་གཏོང་བ་མ་མཆིས་སམ་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་པའོ། །

[Block 1820]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་གཟུགས་ཡོངས་སུ་མ་བཟུང་མ་བཏང་བ་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གཅིག་པའོ། །

[Block 1821]
བཅོམ་ལྡན་འདས་གལ་ཏེ་གཟུགས་ཡིད་ལ་མི༌[^1254]བགྱི་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གཉིས་པའོ། །

[Block 1822]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་འདི་ལྟར་གཟུགས་ཡིད་ལ་མི༌[^1255]བགྱི་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གསུམ་པའོ། །

[Block 1823]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་དེ་ལྟར་སྤྱོད་པ་གང་ལ་གནས་པར་མི་འགྱུར་བ་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་བཞི་པའོ། །

[Block 1824]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་བྱང་ཆུབ་སེམས་དཔའ་གཟུགས་ལ་གནས་པར་མི་འགྱུར་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་ལྔ་པའོ། །

[Block 1825]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་སྐྱོན་འདི་དག་མ་མཆིས་པར་འགྱུར་བ་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་དྲུག་པའོ། །
--- END BLOCKS ---
