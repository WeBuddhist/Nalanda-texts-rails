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

[Block 2001]
བཅོམ་ལྡན་འདས་ཅི་ལགས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཆོས་གཞན་ལ་མི་གནས་ཀྱི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འབའ་ཞིག་ལ་གནས་ཤིང་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་བཞི་པའོ། །

[Block 2002]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་པ་ཉིད་ལགས་ན་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་ལྔ་པའོ། །

[Block 2003]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་དྲུག་པའོ། །

[Block 2004]
བཅོམ་ལྡན་འདས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འགྱུར་བའི་ལམ་དེ༌[^1340]གང་ལགས་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་བདུན་པའོ། །

[Block 2005]
གལ་ཏེ་ཆོས་ཐམས་ཅད་རང་གི་མཚན་ཉིད་ཀྱིས་སྟོང་པ་ལགས་ན་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་བརྒྱད་པའོ། །

[Block 2006]
ཅི་ལགས་བཅོམ་ལྡན་འདས་ཀྱིས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས་ཞེས་བྱ་བ་ནི་བཞི་བཅུ་དགུ་པའོ། །

[Block 2007]
བཅོམ་ལྡན་འདས་ཅི་ལགས་དེ་བཞིན་གཤེགས་པས་ཆོས་ནག་པོའམ་དཀར་པོ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་པའོ། །

[Block 2008]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་རང་གི་མཚན་ཉིད་ཀྱིས་སྟོང་པ་ལགས་ན་ཇི་ལྟར༌[^1341]ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་གཅིག་པའོ། །

[Block 2009]
བཅོམ་ལྡན་འདས་ཅི་ལགས་སྡུག་བསྔལ་འཚལ་བས་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་གཉིས་པའོ། །

[Block 2010]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ཇི་ལྟར་སྤྱོད་ན་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་གསུམ་པའོ། །

[Block 2011]
བཅོམ་ལྡན་འདས་ཆོས་ཐམས་ཅད་ཀྱི་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་ཞེས་བགྱི་བ་གང་ལགས་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་བཞི་པའོ། །

[Block 2012]
བཅོམ་ལྡན་འདས་དེ་ལྟར་ལགས་ན༌[^1342]བྱང་ཆུབ་དངོས་པོ་མ་མཆིས་ན་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་ལྔ་པའོ། །

[Block 2013]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་དངོས་པོ་མ་མཆིས་པའི་ངོ་བོ་ཉིད་ལགས་ཏེ་དེ་དག་སངས་རྒྱས་ཀྱིས་ཀྱང་མ་མཛད་ཅེས་བྱ་བ་ནི་ལྔ་བཅུ་དྲུག་པའོ། །

[Block 2014]
བཅོམ་ལྡན་འདས་བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་རྣམས་གང་ལ་དངོས་པོའོ་ཞེས་མངོན་པར་ཞེན་པར་གྱུར་པ་དེ་ལྟ་བུའི་དངོས་པོ༌[^1343]བཞིན་མ་ནོར་བ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་བདུན་པའོ། །

[Block 2015]
བཅོམ་ལྡན་འདས་ཡང་དག་པ་མཐོང་བ་ལ་ཀུན་ནས་ཉོན་མོངས་པར་འགྱུར་བའམ་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་བརྒྱད་པའོ། །

[Block 2016]
བཅོམ་ལྡན་འདས་ཆོས་ཐམས་ཅད་ཀྱི་མཉམ་པ་ཉིད་དེ་གང་ལགས་ཞེས་བྱ་བ་ནི་ལྔ་བཅུ་དགུ་པའོ། །

[Block 2017]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་སྒྱུ་མ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་པའོ། །

[Block 2018]
བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པས་ཆོས་གང་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པ་དེ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་གཅིག་པའོ། །

[Block 2019]
བཅོམ་ལྡན་འདས་ཆོས་དངོས་པོ་མ་མཆིས་པའི་ངོ་བོ་ཉིད་རྣམས་ལ་ཆོས་ཀྱི་མཉམ་པ་ཉིད་ཅེས་བགྱི་བ་ཡང་གང་ཞིག་མཆིས་ལགས༌[^1344]ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་གཉིས་པའོ། །

[Block 2020]
བཅོམ་ལྡན་འདས་ཅི་ལགས་ཆོས་མཉམ་པ་ཉིད༌[^1345]དེ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་གསུམ་པའོ། །

[Block 2021]
བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཆོས་ཐམས་ཅད་ཀྱི་ཡུལ་ལ་མངའ་བསྒྱུར་བ༌[^1346]མ་ལགས་སམ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་བཞི་པའོ། །

[Block 2022]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་ཀྱི་མཉམ་པ་ཉིད་ལ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་ལྔ་པའོ། །

[Block 2023]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་མཉམ་པ་ཉིད་ལ་སོ་སོའི་སྐྱེ་བོ་རྣམས་དང་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་དྲུག་པའོ། །

[Block 2024]
བཅོམ་ལྡན་འདས་ཅི་ལགས་ཇི་ལྟར་དེ་བཞིན་གཤེགས་པ་ཆོས་མཉམ་པ་ཉིད་ལས་མི་གཡོ་བ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་བདུན་པའོ། །

[Block 2025]
བཅོམ་ལྡན་འདས་གལ་ཏེ་དེ་ལྟར་ཆོས་རྣམས་ཀྱི་ཆོས་ཉིད་ཅེས་བྱ་བ་ནི་དྲུག་ཅུ་བརྒྱད་པའོ། །

[Block 2026]
བཅོམ་ལྡན་འདས་ཅི་ལགས་ཆོས་ཉིད་འདུས་བགྱིས་ལགས་སམ་ཞེས་བྱ་བ་ནི་དྲུག་ཅུ་དགུ་པའོ། །

[Block 2027]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་ཀྱི་མཉམ་པ་ཉིད་ནི་རང་བཞིན་གྱིས་སྟོང་པ་སྟེ་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་པའོ། །

[Block 2028]
བཅོམ་ལྡན་འདས་ཅི་ཞིག་གིས༌[^1347]སྟོང་པ་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གཅིག་པའོ། །

[Block 2029]
བཅོམ་ལྡན་འདས་གལ་ཏེ་འཇིག་རྟེན་པའི་ཆོས་འདི་དག་སྤྲུལ་པ་ལགས་ན༌[^1348]ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གཉིས་པའོ། །

[Block 2030]
བཅོམ་ལྡན་འདས་གང་སྤངས་པ་ཞེས་བགྱི་བ་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་གསུམ་པའོ། །

[Block 2031]
བཅོམ་ལྡན་འདས་གང་མ་སྤྲུལ་པའི་ཆོས་དེ་གང་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་བཞི་པའོ། །

[Block 2032]
བཅོམ་ལྡན་འདས་དེ་གང་ལགས་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་ལྔ་པའོ། །

[Block 2033]
བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་དུ་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་དྲུག་པའོ། །

[Block 2034]
བཅོམ་ལྡན་འདས་ལས་དང་པོ་པའི་གང་ཟག་གིས་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་པ་ཉིད་ཡོངས་སུ་བཙལ་བར་བགྱི་ན་ཇི་ལྟར་གདམས་ཤིང་རྗེས་སུ་བསྟན་པར་བགྱི་ཞེས་བྱ་བ་ནི་བདུན་ཅུ་བདུན་པའོ། །

[Block 2035]
ཞུས་པ་འདི་དག་ཐམས་ཅད་ཀྱི༌[^1349]འཁོར་དེ་ན་འཁོད་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཕྱིར་མི་ལྡོག༌[^1350]པ་རྣམས་ཀྱི་དོན་དང་། མ་འོངས་པའི་སྐྱེ་བོ་རྣམས་ལ་ཕན་གདགས་པའི་ཕྱིར་ཞུས་པ༌[^1351]རིག་པར་བྱའོ།། །།
--- END BLOCKS ---
