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
[Block 1961]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་དངོས་པོ་མ་མཆིས་པའི་ཆོས་རྣམས་རྟོགས་པ་ལགས་ཞེས་བྱ་བ་ནི་ལྔ་པའོ། །

[Block 1962]
བཅོམ་ལྡན་འདས་ཅི་ལགས་གཟུགས་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་དྲུག་པའོ། །

[Block 1963]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ཆོས་ཐམས་ཅད་སྒྱུ་མ་ལྟ་བུར་འཚལ་ཞིང་ཞེས་བྱ་བ་ནི་བདུན་པའོ། །

[Block 1964]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་རྨི་ལམ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་བརྒྱད་པའོ། །

[Block 1965]
བཅོམ་ལྡན་འདས་མིང་ནི་གང་ལགས་མཚན་མ་ནི་གང་ལགས་ཞེས་བྱ་བ་ནི་དགུ་པའོ། །

[Block 1966]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་འདི་དག་ཐམས་ཅད་དུ༌[^1326]དེ་ཙམ་དུ་བས་ཏེ་ཞེས་བྱ་བ་ནི་བཅུ་པའོ། །

[Block 1967]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་མཚན་མ་མ་མཆིས་ཤིང་དྲན་པ་མ་མཆིས་ཏེ་ཞེས་བྱ་བ་ནི་བཅུ་གཅིག་པའོ། །

[Block 1968]
བཅོམ་ལྡན་འདས་རྣམ་པ་གང་གི་ཚུལ་དུ་ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་བཅུ་གཉིས་པའོ། །

[Block 1969]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཚེ་ཕན་ཚུན་ཐ་དད་པའི་ཆོས་དེ་དག་དེ་ལྟར་འཚལ་ན་ཞེས་བྱ་བ་ནི་བཅུ་གསུམ་པའོ། །

[Block 1970]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཆོས་ཀྱི་དབྱིངས་ལ་སློབ་པས་ཞེས་བྱ་བ་ནི་བཅུ་བཞི་པའོ། །

[Block 1971]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་ཆོས་ཀྱི་དབྱིངས་ལགས་ན་ཞེས་བྱ་བ་ནི་བཅོ་ལྔ་པའོ། །

[Block 1972]
བཅོམ་ལྡན་འདས་གལ་ཏེ་སེམས་ཅན་ཤིན་ཏུ་དམིགས་སུ་མ་མཆིས་ལ་ཞེས་བྱ་བ་ནི་བཅུ་དྲུག་པའོ། །

[Block 1973]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཡང་དག་པའི་མཐའ་ཡང་གཞན་མ་ལགས་སེམས་ཅན་གྱི་མཐའ་ཡང་གཞན་མ་ལགས་ན་ཞེས་བྱ་བ་ནི་བཅུ་བདུན་པའོ། །

[Block 1974]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཚེ་ཐབས་མཁས་པ་དང་ལྡན་པས་ཞེས་བྱ་བ་ནི་བཅོ་བརྒྱད་པའོ། །

[Block 1975]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་ཀྱི༌[^1327]རང་བཞིན་གྱིས་སྟོང་པ་ལགས་ན་ཞེས་བྱ་བ་ནི་བཅུ་དགུ་པའོ། །

[Block 1976]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་དབྱེར་མ་མཆིས་པ་ལགས༌[^1328]ན་ཅིའི་སླད་དུ་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་པའོ། །

[Block 1977]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས༌[^1329]བྱང་ཆུབ་འཛིན་པ་ལ་ཡང་མི་སྤྱོད། མི་འཛིན་པ་ལ་ཡང་མི་སྤྱོད་ན་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་གཅིག་པའོ། །

[Block 1978]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་འཛིན་པ་ལ་ཡང་མི་སྤྱོད། མི་འཛིན་པ་ལ་ཡང་མི་སྤྱོད་གཟུགས་ལ་ཡང་མི་སྤྱོད་ཅེས་བྱ་བ་ནི་ཉི་ཤུ་གཉིས་པའོ། །

[Block 1979]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་བྱང་ཆུབ་སེམས་དཔའི་ས་བཅུ་ལ་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་གསུམ་པའོ། །

[Block 1980]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་གང་ལ་སྤྱད་དེ་སེམས་ཅན་རྣམས་ཡོངས་སུ་སྨིན་པར་བགྱི་བ་དང་། སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་བགྱི་བའི་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོའི་ལམ་གང་ལགས་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་བཞི་པའོ། །

[Block 1981]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོའི༌[^1330]སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་ཅིང་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་ལྔ་པའོ། །

[Block 1982]
བྱང་ཆུབ་སེམས་དཔའི༌[^1331]ལམ་གང་ལགས་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་དྲུག་པའོ། །

[Block 1983]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་སྟོང་པ་ལགས་ན་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་བདུན་པའོ། །

[Block 1984]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་མི་གནས་པ་ལགས༌[^1332]ཞེས་བྱ་བ་ནི་ཉི་ཤུ་བརྒྱད་པའོ། །

[Block 1985]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་མ་སྐྱེས་ན་ཞེས་བྱ་བ་ནི་ཉི་ཤུ་དགུ་པའོ། །

[Block 1986]
བཅོམ་ལྡན་འདས་འོ་ན་དེ་བཞིན་གཤེགས་པ་རྣམས་བྱུང་ཡང་རུང་མ་བྱུང་ཡང་རུང་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་པའོ། །

[Block 1987]
བཅོམ་ལྡན་འདས་ཅི་ལགས་སྐྱེས་པར་གྱུར་པའི་ལམ་གྱིས་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་ལགས་སམ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་གཅིག་པའོ། །

[Block 1988]
འདིར་བར་སྐབས་སུ་ཞུས་པ་ལྔའོ། །

[Block 1989]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་ཉིད་ཀྱང་ལམ་ལགས༌[^1333]ལ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་གཉིས་པའོ། །

[Block 1990]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས་དབེན་པ་ལགས་ན་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་གསུམ་པའོ། །

[Block 1991]
བཅོམ་ལྡན་འདས་ལུས་ཀྱི་གནས་ངན་ལེན་ནི་གང་ལགས་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་བཞི་པའོ། །

[Block 1992]
བཅོམ་ལྡན་འདས་ཅི་ལགས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་དེས་ཤེས༌[^1334]བགྱིའམ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་ལྔ་པའོ། །

[Block 1993]
བཅོམ་ལྡན་འདས་ཕུང་པོ་གང་དུ་ངེས་པ་ལགས་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་དྲུག་པའོ། །

[Block 1994]
བཅོམ་ལྡན་འདས་ཅི་ལགས་སེམས་དང་པོའི༌[^1335]བསྐྱེད་པ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་བདུན་པའོ། །

[Block 1995]
བཅོམ་ལྡན་འདས་ཅི་ལགས་ངེས་པའི་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ངེས་པར༌[^1336]ངན་སོང་རྣམས་སུ་སྐྱེ་བར་འགྱུར་ལགས་སམ༌[^1337]ཞེས་བྱ་བ་ནི་སུམ་ཅུ་བརྒྱད་པའོ། །

[Block 1996]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ངེས་པའི་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་སུམ་ཅུ་དགུ་པའོ། །

[Block 1997]
བཅོམ་ལྡན་འདས་དགེ་བའི་ཆོས་དག༌[^1338]གང་ལ་གནས་ཤིང་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་པའོ། །

[Block 1998]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་འཕགས་པའི་ཆོས་དཀར་པོ་དང་ལྡན་པ༌[^1339]ཞེས་བྱ་བ་ནི་བཞི་བཅུ་གཅིག་པའོ། །

[Block 1999]
བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་ནི་འཕགས་ཤིང་ཟག་པ་མི་མངའ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་གཉིས་པའོ། །

[Block 2000]
བཅོམ་ལྡན་འདས་དགེ་བའི་ཆོས་གང་དག་ལ་གནས་ཏེ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་གསུམ་པའོ། །
--- END BLOCKS ---
