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
[Block 1891]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་སེམས་དང་པོ་བསྐྱེད་པ་དང་ལྡན་པ་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་དུ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འཚལ་བ་དེ༌[^1291]བསོད་ནམས་ཇི་ཙམ་ཞིག་བསྐྱེད་པར༌[^1292]འགྱུར་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་བདུན་པའོ། །

[Block 1892]
བཅོམ་ལྡན་འདས་སེམས་དང་པོ་བསྐྱེད་པས་ཅི་ཞིག༌[^1293]ཡིད་ལ་བགྱི་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་བརྒྱད་པའོ། །

[Block 1893]
བཅོམ་ལྡན་འདས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི༌[^1294]དམིགས་པ་ཇི༌[^1295]ལྟ་བུ་ལགས་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་དགུ་པའོ། །

[Block 1894]
བཅོམ་ལྡན་འདས་ཅི་ལགས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་འབའ་ཞིག་དངོས་པོ་མ་མཆིས་པ་ལགས་སམ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་པའོ། །

[Block 1895]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ངོ་བོ་ཉིད་མ་མཆིས་པ་ལགས་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་གཅིག་པའོ། །

[Block 1896]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་དངོས་པོ་མ་མཆིས་པའི་ངོ་བོ་ཉིད་ལགས་ན་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་གཉིས་པའོ། །

[Block 1897]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་རྣམས་ཆོས༌[^1296]ཉིད་དང་བྲལ་བ་ལགས་སམ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་གསུམ་པའོ། །

[Block 1898]
བཅོམ་ལྡན་འདས་ཅི་ལགས་འཇིག་རྟེན་གྱི་ཀུན་རྫོབ་ཀྱང་གཞན་ཞིག་ལ་དོན་དམ་པ་ཡང་གཞན་ཞིག་ལགས་སམ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་བཞི་པའོ། །

[Block 1899]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ཞེས་བགྱི་ན་ཞེས༌[^1297]བྱ་བ་ནི་བཞི་བཅུ་ལྔ་པའོ། །

[Block 1900]
བཅོམ་ལྡན་འདས་སངས་རྒྱས་སངས་རྒྱས་ཞེས་བགྱི་ན༌[^1298]ཞེས་བྱ་བ་ནི་བཞི་བཅུ་དྲུག་པའོ། །

[Block 1901]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་བྱང་ཆུབ་ཅེས་བགྱི་ན༌[^1299]ཞེས་བྱ་བ་ནི་བཞི་བཅུ་བདུན་པའོ། །

[Block 1902]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་གང་བྱང་ཆུབ་འདི་ལ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་བརྒྱད་པའོ། །

[Block 1903]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་བྱང་ཆུབ་ཅེས་བྱ་བ་ནི་བཞི་བཅུ་དགུ་པའོ། །

[Block 1904]
བཅོམ་ལྡན་འདས་གལ་ཏེ་གཉིས་ཀྱི་ཚུལ་གྱིས་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་པའོ། །

[Block 1905]
བཅོམ་ལྡན་འདས་ཅི་ལགས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་དགེ་བའི་རྩ་བ་རྣམས་ཀྱི་སླད་དུ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་གཅིག་པའོ། །

[Block 1906]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ལ་བསྙེན་བཀུར་མ་བགྱིས་པ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་གཉིས་པའོ། །

[Block 1907]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་མི་འགྱུར་རམ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་གསུམ་པའོ། །

[Block 1908]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་བསྙེན་བཀུར་བགྱིས་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་བཞི་པའོ། །

[Block 1909]
བཅོམ་ལྡན་འདས་ཐབས་མཁས་པ་གང་དང་ལྡན་པས་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་ལྔ་པའོ། །

[Block 1910]
བཅོམ་ལྡན་འདས་ཅི་ལགས་དངོས་པོ་མ་མཆིས་པས་དངོས་པོ་མ་མཆིས་པར་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་བགྱི་བར་མི༌[^1300]ནུས་སམ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་དྲུག་པའོ། །

[Block 1911]
སྐབས་འདིར་བར་སྐབས་སུ་ཞུས་པ་བཞིའོ། །

[Block 1912]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོའི་སྤྲོས་པ་གང་ལགས་ཞེས་བྱ་བ་ནི་ལྔ༌[^1301]བདུན་པའོ། །

[Block 1913]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་གང༌[^1302]ཡང་ངོ་བོ་ཉིད་དམིགས་སུ་མ་མཆིས་ན་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་བརྒྱད་པའོ། །

[Block 1914]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ལམ་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བགྱིས་ཤིང་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་དགུ་པའོ། །

[Block 1915]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བདག་གི༌[^1303]བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ལམ་འདི་དག་མ་བསྐྱེད་པར་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་བགྱིད་ཅེས་བྱ་བ་ནི་དྲུག་ཅུ་པའོ། །

[Block 1916]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའི་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ཀྱི་ལམ་གང་ལགས་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་གཅིག་པའོ། །

[Block 1917]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་རྣམས་གང་ལགས་པ་དང་བྱང་ཆུབ་གང་ལགས་པ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་གཉིས་པའོ། །

[Block 1918]
བཅོམ་ལྡན་འདས་ཆོས༌[^1304]རྣམས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ཤེས་པ་དང་། མཐོང་བས་བསླབས་ནས་རྟོགས་པར་བགྱི་བའི་ཆོས་རྣམས་ནི་གང་ལགས༌[^1305]ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་གསུམ་པའོ། །

[Block 1919]
བཅོམ་ལྡན་འདས་འཕགས་པའི་ཆོས་འདུལ་བ་ལ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་བཞི་པའོ། །

[Block 1920]
བཅོམ་ལྡན་འདས་འོ་ན་གཟུགས་ཀྱི་མཚན་ཉིད་ལ་བསླབ་པར་མི་བགྱི་འམ༌[^1306]ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་ལྔ་པའོ། །

[Block 1921]
གལ་ཏེ་ཆོས་འདི་དག་གི་མཚན་ཉིད་ལ་བསླབ་པར་མི་བགྱི་ན་བཅོམ་ལྡན་འདས་ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་དྲུག་པའོ། །

[Block 1922]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་ལ་མཚན་ཉིད་མ་མཆིས་ཤིང་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་བདུན་པའོ། །

[Block 1923]
བཅོམ་ལྡན༌[^1307]འདས་ཇི་ལྟར་ན་མཚན་ཉིད་མ་མཆིས་པ་ལ་སྒོམ་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་བསྒོམ་པར་འགྱུར་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་བརྒྱད་པའོ། །

[Block 1924]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་གཟུགས་ལ་བསྒོམ་པ༌[^1308]རྣམ་པར་འཇིག་པ་ཇི་ལྟར༌[^1309]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ༌[^1310]བསྒོམ་པ་ལགས་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་དགུ་པའོ། །

[Block 1925]
བཅོམ་ལྡན་འདས་གལ་ཏེ་དངོས་པོའི་འདུ་ཤེས་ཅན་ལ་མཐུན་པའི་བཟོད་པ་ཡང་མ་མཆིས་སམ་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་པའོ། །

[Block 1926]
བཅོམ་ལྡན་འདས་ཅི་ལགས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཚེ་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གཅིག་པའོ། །

[Block 1927]
བཅོམ་ལྡན་འདས་དངོས་པོ་ཞེས་བགྱི་བ་ནི་ཅི་ལགས་དངོས་པོ་མ་མཆིས་པ་ཞེས་བགྱི་བ་ནི་ཅི་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གཉིས་པའོ། །

[Block 1928]
བཅོམ་ལྡན་འདས་གཉིས་ནི་གང་ལགས་གཉིས་སུ་མ་མཆིས་པ་ནི་གང་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གསུམ་པའོ། །

[Block 1929]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་དངོས་པོ་མ་མཆིས་པའི་ངོ་བོ་ཉིད་ལགས་ན་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་བཞི་པའོ། །

[Block 1930]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཀྱིས་དངོས་པོ་མ་མཆིས་པའི་ངོ་བོ་ཉིད་ཀྱི་བསམ་གཏན་བཞི་བསྐྱེད་པར་གྱུར་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་ལྔ་པའོ། །
--- END BLOCKS ---
