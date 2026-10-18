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
[Block 2206]
ཆོས་ཐམས་ཅད་མི་སྐྱེ་བའི་སླད་དུ་ཞེས་བྱ་བ་ནི༌[^1539]གཟུགས་ལ་སོགས་པའི་ཆོས་སམ་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་ཀྱང་རུང་སྟེ་ཐམས་ཅད་མི་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 2207]
རབ་འབྱོར་དེ་ཇི་སྙམ་དུ་སེམས། གང་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ལུང་བསྟན་པར་འགྱུར་བའི་ཆོས་དེ་ལྟ་བུ་ཁྱོད་ཀྱིས་ཡང་དག་པར་རྗེས་སུ་མཐོང་ངམ་ཞེས་བྱ་བ་ནི་ལུང་བསྟན་པར་བྱ་བ་དང་། མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པར་བྱེད་པ་དངོས་པོ་མེད་པས་འདི་དང་། འདི་ལྟ་བུའི་དོན་དུ་ལུང་བསྟན་པར་འགྱུར་ཞེས་བྱ༌[^1540]བའི་ཐ་ཚིག་གོ། །

[Block 2208 [HEADING]]
##### བསོད་ནམས་མང་པོ་བསྟན་པ། ^1-2-7-17-0

[Block 2209]
དེ་ལྟར་ཟབ་ཅིང་ཟབ་པའི་གནས་དག་བསྟན་པས། བཅོམ་ལྡན་འདས་འདི་ནི་ཟབ་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསོལ་ཏོ། །

[Block 2210]
དེ་ནས་ཡང་བསོད་ནམས་མང་པོ་བསྟན་པ་ཡང་། དད་པ་རབ་ཏུ་སྐྱེད་པའི་ཕྱིར་རོ། །

[Block 2211]
རབ་ཏུ་བསྔགས་པའི་ཚིག་ཐམས་ཅད་དང་། ཕན་ཡོན་བསྟན་པ་དང་། བརྒྱ་བྱིན་དང་། ཀུན་དགའ་བོའི་ཚིག་དང་། བདུད་ཀྱི་གཏམ་དང་། བདུད་ཀྱི་ལས་དང་། དེ་ལས་བྱུང་བའི༌[^1541]གཏམ་དང་། བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་པའི་གང་ཟག་རྣམས་ཀྱི་དྲུང་དུ་ཇི་ལྟར་གནས་པར་བྱ་བ་དང་། མཉམ་པ་ཉིད་བཤད་པ་གང་ཡིན་པ་དང་། ཟད་པ་དང་། འདོད་ཆགས་དང་བྲལ་བ་དང་། འགོག་པ་ལ་སོགས་པའི་གཏམ་དང་། བསླབ་པའི་ཕན་ཡོན་བཤད་པ་དང་། [^1542]སེམས་ཅན་དང་། སེམས་ཅན་མ་ཡིན་པ་རྣམས་ཟིལ་གྱིས་གནོན་པ་དང་། བརྒྱ་བྱིན་གྱི༌[^1543]ཚིག་དང་། བསོད་ནམས་ཚད་མེད་པ་དང་། དེ་ནས་ཡང་བརྒྱ་བྱིན་གྱི༌[^1544]ཚིག་རྣམས་ནི་གཞུང་ཉིད་ལས་གོ་སླ་བས་རྣམ་པར་ཕྱེ་སྟེ་མ་བཤད་དོ། །

[Block 2212 [HEADING]]
##### གཉིས་ཀྱི་འདུ་ཤེས་སུ་འགྱུར་བ་མེད་པར་ཡོངས་སུ་བསྔོ་བ། ^1-2-7-18-0

[Block 2213]
ཅི་ནས་ཀྱང་གཉིས་ཀྱི་འདུ་ཤེས་སུ་འགྱུར་བ་མེད་པ་དང་གཉིས་མ་ཡིན་པའི་འདུ་ཤེས་སུ་འགྱུར་བ་མེད་པ་དེ་ལྟ་བུར་ཡོངས་སུ་བསྔོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་དག་གི་སེམས་བསྐྱེད་པ་གང་ཡིན་པ་དང་། བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་གང་ཡིན་པ་དེ་དག་དོན་དམ་པར་ཐ་དད་པ་མ་ཡིན་ཏེ། དེ་དག་གི་དེ་བཞིན་ཉིད་ནི་རྣམ་པར་དག་པར་རབ་ཏུ་ཕྱེ་བ་ཡིན་པས་དེའི་ཕྱིར་གཉིས་ཀྱི་འདུ་ཤེས་སུ་མི་འགྱུར་རོ། །

[Block 2214]
གཉིས་ནི་དྲི་མ་དང་བཅས་པ་དང་། དྲི་མ་མེད་པའི་བྱེ་བྲག་ལས་ཐ་དད་པ་ཡོད་པས་གཉིས་ཀྱི་འདུ་ཤེས་སུ་ཡང་འགྱུར་རོ། །

[Block 2215]
དེ་བས་ན་གཅིག་པའི་ཕྱིར་གཉིས་ཀྱི་འདུ་ཤེས་སུ་མི་འགྱུར༌[^1545]ཞེས་གསུངས་སོ། །

[Block 2216]
ཐ་དད་པའི་ཕྱིར་གཉིས་སུ་འདུ་ཤེས་སོ། །

[Block 2217]
ཡང་ན་ཡོད་པ་དང་། མེད་པ་ཞེས་བྱ་བ་ནི་གཉིས་སུ་འདུ་ཤེས་པའོ། །

[Block 2218]
ཡོད་པ་ཡང་མ་ཡིན་མེད་པ་ཡང་མ་ཡིན་པ་ནི་གཉིས་སུ་འདུ་ཤེས་མེད་པ་སྟེ། དེ་ཡང་འོག་ནས་འབྱུང་བའི་གཞུང་གིས་གསལ་བར་བཤད་དོ། །

[Block 2219]
དེ་ནས་ཡང་འོག་ནས་ཅི་ནས་ཀྱང་སེམས་དེ་ལ་ཡང་མ་ཡིན་ཞིང་། སེམས་གཞན་ལ་ཡང་མ་ཡིན་པ་དེ་ལྟར་ཡོངས་སུ་བསྔོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་གྱུར་པའི་དབང་གིས་སེམས་དེ་ལ་ཡང་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 2220]
དོན་དམ་པར་ནི་ཐ་དད་པ་མེད་པས་སེམས་གཞན་ལ་ཡང་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 2221]
རབ་འབྱོར་དེ་ཇི་སྙམ་དུ་སེམས་སྒྱུ་མ་ལྟ་བུའི་སེམས་དེ་ཁྱོད་ཀྱིས་ཡང་དག་པར་རྗེས་སུ་མཐོང་ངམ་ཞེས་བྱ་བ་ཅི་ལས་དགོངས་ཤེ་ན། གལ་ཏེ་སེམས་སྒྱུ་མ་ལྟ་བུ་ཡིན་ལ། བྱང་ཆུབ་སྒྱུ་མ་ལྟ་བུ་མ་ཡིན་ན་ནི་དེ་ལྟ་ན༌[^1546]ཀླན་ཀར་འགྱུར་ན། འདི་ལྟར་སེམས་དང་བྱང་ཆུབ་གཉི་ག་ཡང་སྒྱུ་མ་ལྟ་བུ་ཡིན་ཏེ། དེའི་ཕྱིར་ཀླན་ཀ༌[^1547]མེད་དོ། །

[Block 2222]
ཆོས་གང་ཤིན་ཏུ་དབེན་པ་དེ་ནི་མཆིས་པའམ་མ་མཆིས་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི། ཀུན་བརྟགས་པའི་ཆོས་གང་ཡིན་པ་དེ་སྒྱུ་མ་ལྟ་བུ་ཡིན་པའི་ཕྱིར། །སྒྱུ་མ་དང་འདྲ་བར་ཡོད་དོ་ཞེས་བྱ་བའམ། མེད་དོ་ཞེས་བྱ་བར་བརྗོད་དུ་མི་རུང་ལ། ཡོད་པ་ཡང་མ་ཡིན་མེད་པ་ཡང་མ་ཡིན་ཞེས་ཀྱང་བརྗོད་དུ་མི་རུང་ངོ་། །ཡོངས་སུ་གྲུབ་པའི་ཆོས་གང་ཡིན་པ་དེ་ཡང་དངོས་པོའི༌[^1548]རྣམ་པ་ཐམས་ཅད་ཀྱིས་དབེན་པའི་ཕྱིར་ཡོད་དོ་ཞེས་བརྗོད་དུ་མི་རུང་ངོ་། །བརྗོད་དུ་མེད་པ༌[^1549]དབེན་པའི་རང་བཞིན་ཡོད་པའི་ཕྱིར་མེད་དོ་ཞེས་ཀྱང་བརྗོད་དུ་མི་རུང་ངོ་། །ཡོད་དོ་ཞེས་བྱ་བའི་ཐ་སྙད་ཡོད་པའི་ཕྱིར་མེད་དོ་ཞེས་ཀྱང་བརྗོད་དུ་མི་རུང་ངོ་། །མེད་དོ་ཞེས་བྱ་བའི་ཐ་སྙད་ཡོད་པའི་ཕྱིར་མེད་པ་མ་ཡིན་ནོ་ཞེས་ཀྱང་བརྗོད༌[^1550]དུ་མི་རུང་ངོ་། །དེ་བས་ན་གཉིས་ཀྱི་འདུ་ཤེས་དང་། གཉིས་སུ་མེད་པའི་འདུ་ཤེས་མི་རིགས་སོ། །

[Block 2223]
བཅོམ་ལྡན་འདས་འདི་ལྟར་གང་ཀུན་ནས་ཉོན་མོངས་པར་འགྱུར་བའམ། རྣམ་པར་བྱང་བར་འགྱུར་བའི་ཆོས་དེ་དག་ཐམས་ཅད་ནི་མ་མཆིས་ཤིང་མི་དམིགས་སོ་ཞེས་བྱ་བ་ནི་ཀུན་ནས་ཉོན་མོངས་པར་འགྱུར་བ་དང་། རྣམ་པར་བྱང་བར་འགྱུར་བའི་ཆོས་རྣམས་ཡོད་པ་མ་ཡིན་ཏེ། དྲི་མ་དང་བཅས་པའི་གནས་སྐབས་ན་ཡང་། ནམ་མཁའ་བཞིན་དུ་རང་བཞིན་གྱིས་དབེན་པའི་ཕྱིར་ཀུན་ནས་ཉོན་མོངས་པ་མེད་དོ། །

[Block 2224]
དེ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་སྔོན་མ་བྱུང་བའི་རྣམ་པར་བྱང་བ་ཡང༌[^1551]མེད་དོ། །

[Block 2225]
འདི་ནི་སེམས་དེ་ལ་ཡང་མ་ཡིན། སེམས་གཞན་ལ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་བཤད་པ་ཡིན་ནོ། །

[Block 2226]
ཆོས་གང་ཤིན་ཏུ་དབེན་པ་དེ་ནི་བསྒོམ་པར་བགྱི་བ་ཡང་མ་ལགས། རྣམ་པར་གཞིག་པར་བགྱི་བ་ཡང་མ་ལགས་ཞེས་བྱ་བ་ལ་བསྒོམ་པ་ཞེས་བྱ་བ་ནི་གོམས་པར་བྱ་བ་སྟེ། དེ་དབེན་པའི་ཕྱིར་མི་རིགས་སོ། །

[Block 2227]
རྣམ་པར་གཞིག་པ་ཞེས་བྱ་བ་ནི་དྲི་མ༌[^1552]བསྩལ་བ་སྟེ། དེ་ཡང་ཤིན་ཏུ་དབེན་པའི་ཕྱིར་མི་རིགས་སོ། །

[Block 2228]
བསྒྲུབ་པར་བགྱིད་པའི་ཆོས་ཀྱང་གང་ཡང་མ་མཆིས་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་དབེན་པའི་ཕྱིར༌[^1553]བྱང་ཆུབ་ཐོབ་པར་བྱེད་པ་མ་ཡིན་པའོ། །

[Block 2229 [HEADING]]
##### དབེན་པས་དབེན་པ་རྗེས་སུ་རྟོགས་པ། ^1-2-7-19-0

[Block 2230]
དབེན་པ་ཉིད་ལགས་པའི་སླད་དུ་ཇི་ལྟར་དབེན་པས་དབེན་པ་རྗེས་སུ་རྟོགས་པར་འགྱུར་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་དབེན་པ་ཡིན་ན། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དབེན་པས་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་དབེན་པ་ཇི་ལྟར་རྗེས་སུ་རྟོག་པར༌[^1554]འགྱུར་ཞེས་ཞུས་པའོ། །

[Block 2231]
རབ་འབྱོར་དེ་དེ་བཞིན་ནོ། །

[Block 2232]
དེ་དེ་བཞིན་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པས་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་གསུངས་ཏེ། གལ་ཏེ་གཅིག་ནི་དབེན༌[^1555]ལ། ཅིག་ཤོས་ནི་མི་དབེན་པ་ཞིག་ཡིན་ན་ནི་དེ་ལྟ་ན་ནི་མི་རིགས་པར་འགྱུར་ན། འདི་ལྟར་དེ་གཉིས་ཀ་ཡང་དབེན་པས་དེའི་ཕྱིར་ཉེས་པ་མེད་དེ། ཆོས་ཐམས་ཅད་ཀྱི་དབེན་པའི་མཚན་ཉིད་དེ་ཉིད་ཤེས་ན་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འགྱུར་རོ་ཞེས་སྟོན་ཏོ། །

[Block 2233]
བཅོམ་ལྡན་འདས་བདག་གིས༌[^1556]བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པའི་དོན་བདག་གིས་འཚལ་བ་ལྟར་ན། བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ནི་དཀའ་བ་བགྱིད་པ་མ་ལགས་སོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་ལ་ལ་ནི༌[^1557]དམིགས། ལ་ལ་ནི་མི་དམིགས་ན་ནི་དེ་ལྟ་ན༌[^1558]མི་མཐུན་པས་དཀའ་བར་འགྱུར་ན། འདི་ལྟར་ཆོས་ཐམས་ཅད་ནི་ཡོད་པ་མ་ཡིན་ཏེ། མེད་པ་ཉིད་ཀྱི་ཕྱིར་མི་དམིགས་སོ། །

[Block 2234]
མེད་པ་ནི་མི་དམིགས་པ་ཞེས་བྱ་བར་ཤེས་པར་མི་དཀའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2235]
བཅོམ་ལྡན་འདས་མི་དམིགས་པར་སྤྱོད་པ་འདི་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་སྟེ་ཞེས་བྱ་བ་ནི་མི་དམིགས་པར་སྤྱོད་པ་མ་གཏོགས་པ༌[^1559]སྤྱོད་པ་གཞན་མེད་དོ། །

[Block 2236]
དེའི་འོག་ཏུ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམ་པར་མི་རྟོགས་པ༌[^1560]ཉིད་དུ་བསྟན་པ་ནི་གོ་སླའོ།། །།

[Block 2237 [HEADING]]
##### འཁོར་བ་དང་རྣམ་པར་བྱང་བའི་ཆོས་རྣམ་པར་གཞག་པ། ^1-2-7-20-0

[Block 2238]
བམ་པོ་ཉི་ཤུ༌[^1561]བཞི་པ། འགྲོ་བ་ལྔར་འཁོར་བ་ཞེས་ཐ་དད་དུ་དབྱེ་བ་འདི་ཅི་ལས་གྱུར༌[^1562]རྒྱུན་དུ་ཞུགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་དབྱེ་བའང་ཅི་ལས་གྱུར་ཅེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་སྟོན་ཏོ། །

[Block 2239]
གལ་ཏེ་ཆོས་ཐམས་ཅད་རྣམ་པར་མི་རྟོག་པ་ཡིན་ན་འཁོར་བ༌[^1563]དང་། རྣམ་པར་བྱང་བའི་ཆོས་རྣམས་ཅི་ལས་བྱུང་ཞེས་དྲིས་པའོ། །

[Block 2240]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱི༌[^1564]བཀའ་སྩལ་པ། འདི་དག་ནི་ཕྱིན་ཅི་ལོག་པ་སྟེ། མེད་པ་ལ་འཛིན་པ། ཡོད་པ་སྒྲིབ་པར༌[^1565]བྱེད་པའི་མཚན་ཉིད་དོ། །

[Block 2241]
དེ་དག་དང་འདྲེས་པའི་ཕྱིར། འདོད་ཆགས་དང་ཞེ་སྡང་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པ་ཡང་ཡོད་པ་ལ་ནི་སྒྲིབ་པོ། །མེད་པ་ལ་ནི་འཛིན་ཏོ། །

[Block 2242]
དེ་དག་གིས་བསྐྱེད་པའི་ཕྱིར། བསོད་ནམས་དང་། བསོད་ནམས་མ་ཡིན་པ་ལ་སོགས་པའི་ལས་བྱེད་པའི་སེམས་པ་ཡང་། ཕྱིན་ཅི་ལོག་ཏུ་འཛིན་པ་ཡིན་ཏེ་ལས་དེ་དང་རྣམ་པར་རྟོག་པ་དེ་དག་གིས་བསྐྱེད་པའི་ཕྱིར། རྣམ་པར་སྨིན་པའི་ཤེས་པ་ཡང་དེ་ཁོ་ན་ཉིད་འཛིན་པ་མ་ཡིན་ནོ། །

[Block 2243]
དེ་བས་ན་འདུན་པ་དང་། འདོད་ཆགས་ལ་སོགས་པ་ཡང་དེ་ཁོ་ན་མ་ཡིན་པའི་ཡུལ་ཅན་ཏེ། ཀུན་འབྱུང་བ་ཐམས་ཅད་ནི་ཡང་དག་པའི་ངོ་བོ་ཉིད༌[^1566]མ་ཡིན་ནོ། །

[Block 2244]
སེམས་ཅན་དམྱལ་བ་དང་། དུད་འགྲོ་དང་། ཡི་དགས་དང་། ལྷ་དང་མིའི་འགྲོ་བ་རྣམས་ཞེས་བྱ་བ་ནི་འགྲོ་བ་ལྔ་པོ་དག་དེ་ཁོ་ནའི་ངོ་བོ་ཉིད་དུ༌[^1567]སྟོན་ཏེ། དེའི་ཕྱིར་ཆོས་རྣམས་རྣམ་པར་མི་རྟོག་པ་ཡིན་ཡང་དེ་ལྟར་འཁོར་བར༌[^1568]རྣམ་པར་གཞག་གོ། །

[Block 2245]
རྣམ་པར་བྱང་བའི་ཆོས་རྣམས་ལ་ཡང་། རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པ་རྣམ་པར་གཞག་ཅིང་། ཐམས་ཅད་ཀྱང་རྣམ་པར་མི་རྟོག་པ་ཉིད་དེ། རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པ་ནས། དེ་བཞིན་གཤེགས་པའི་བར་དུ་ངོ་བོ་ཉིད་ཀྱིས་ཐ་དད་པ་ནི་གང་ཡང་མེད་དེ། ཐམས་ཅད་ཀྱང་ཆོས་ཀྱི་སྐུ་ལས་མ་འདས་པའི་ཕྱིར་རོ་ཞེས་བསྟན་པའོ། །
--- END BLOCKS ---
