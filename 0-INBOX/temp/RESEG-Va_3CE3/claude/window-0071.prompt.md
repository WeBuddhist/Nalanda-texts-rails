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
[Block 2486]
དེས་ཡང་དག་པའི་དོན་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པས་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམ་པ་གསུམ་གྱིས་ངེས་པའི་ཚིག་གསུངས་པ་སྟེ། བཅོམ་ལྡན་འདས་ཀྱིས་ནི་དགྲ་བཅོམ་པའི་ལམ་གྱི་ཡེ་ཤེས་ཀྱིས་ཡང་དག་པའི་ཆོས་མྱ་ངན་ལས་འདས་པ་ཉིད་སངས་རྒྱས་པར་འགྱུར་བ་དང་། དེའི་འོག་ཏུ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཡེ་ཤེས་ཀྱིས་ཡང་དག་པའི་དོན་སྟོང་པ་དང་ཞི་བ་ལ་སོགས་པའི་དོན་དུ་རྟོགས་པ་དང་། དེའི་རྗེས་ལ་ཐོབ་པ་དང༌[^1768]ཐམས་ཅད་མཁྱེན་པ་ཉིད་པའི༌[^1769]ཡེ་ཤེས་ཀྱིས༌[^1770]ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་རྗེས་སུ་རྟོགས་པར་འགྱུར་ཏེ། དེ་ལྟར་ཡང་དག་པའི་ཆོས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པ་དང་། ཡང་དག་པའི་དོན་རབ་ཏུ་རྟོགས་པ་དང་། ཆོས་ཐམས་ཅད་ཇི་ལྟ་བ་བཞིན་དུ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པའི་ཕྱིར་སངས་རྒྱས་ཞེས་བྱའོ། །

[Block 2487 [HEADING]]
##### བྱང་ཆུབ་རྣམ་པ་གསུམ་དུ་བསྟན་པ། ^1-2-7-54-0

[Block 2488]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་ཅེས་བགྱི་བ་དེ་གང་གི་ཚིག་བླ་དགས་ལགས་སོ༌[^1771]ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱང་རྣམ་པ་གསུམ་དུ་བསྟན་ཏེ་ངོ་བོ་ཉིད་དང་མཚན་ཉིད་དང་ངེས་པའི་ཚིག་གིས་སོ། །

[Block 2489 [HEADING]]
###### ངོ་བོ་ཉིད། ^1-2-7-54-1-0

[Block 2490]
དེ་ལ་ངོ་བོ་ཉིད་རྣམ་པ་གཉིས་ཏེ། ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་དང་། ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 2491 [HEADING]]
###### **ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད།** ^1-2-7-54-1-1-0

[Block 2492]
དེ་ལ་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་ནི་རབ་འབྱོར་བྱང་ཆུབ་ཅེས་བྱ་བ་དེ་ནི་སྟོང་པ་ཉིད་ཀྱི་ཚིག་བླ་དགས་སོ་ཞེས་གསུངས་པའོ། །

[Block 2493 [HEADING]]
###### **ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད།** ^1-2-7-54-1-2-0

[Block 2494]
ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་ནི་རབ་འབྱོར་འདི་ལྟར་ཡང་། བྱང་ཆུབ་ཅེས་བྱ་བ་དེ་ནི་མིང་ཙམ་ཞེས་གསུངས་པའོ། །

[Block 2495 [HEADING]]
###### མཚན་ཉིད། ^1-2-7-54-2-0

[Block 2496]
མཚན་ཉིད་ནི་ཡང་དག་པའི་དོན་ནི་བྱང་ཆུབ་ཀྱི་དོན་ཏོ་ཞེས་གསུངས་པ་སྟེ། དོན་དམ་པའི་མཚན་ཉིད་ནི་ཡང་དག་པར༌[^1772]དོན་དམ༌[^1773]པའི་དོན་ཞེས་བྱའོ། །

[Block 2497 [HEADING]]
###### ངེས་པའི་ཚིག། ^1-2-7-54-3-0

[Block 2498 [HEADING]]
###### **ཀུན་བརྟགས་པའི་མཚན་ཉིད་རྟོགས་པའི་ངེས་པའི་ཚིག།** ^1-2-7-54-3-1-0

[Block 2499]
ངེས་པའི་ཚིག་ནི་དེ་ནི་ཆོས་ཐམས་ཅད་མིང་དང་མཚན་མ་ཙམ་དུ་རྟོགས་པར་བྱེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམ་པ་གསུམ་སྟེ། དེ་ལ་ཀུན་བརྟགས་པའི་མཚན་ཉིད་རྟོགས་པའི་ངེས་པའི་ཚིག་ནི་དེ་ནི་ཆོས་ཐམས་ཅད་མིང་དང་མཚན་མ་ཙམ་དུ་རྟོག་པར༌[^1774]བྱེད་པ་ཞེས་གསུངས་པའོ། །

[Block 2500 [HEADING]]
###### **གཞན་གྱི་དབང་རྟོགས་པ།** ^1-2-7-54-3-2-0

[Block 2501]
གཞན་གྱི་དབང་རྟོགས་པས། གནས་གྱུར་པའི་མཚན་ཉིད་ཆོས་ཀྱི་སྐུའི་ཚུལ་ནི་དེ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་བྱང་ཆུབ་སྟེ། དེའི་ཕྱིར་བྱང་ཆུབ་ཅེས་བྱའོ་ཞེས་གསུངས་པའོ། །

[Block 2502 [HEADING]]
###### **ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་རྟོགས་པ།** ^1-2-7-54-3-3-0

[Block 2503]
ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་རྟོགས་པ་ནི་དེ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱིས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས༌[^1775]ན་དེའི་ཕྱིར་བྱང་ཆུབ་ཅེས་བྱའོ་ཞེས་གསུངས་པའོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་བྱང་ཆུབ་ནི་ཆོས་གང་ཡང་བསྩགས་པའི་ཕྱིར་རམ། འགྲིབ་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་ལ་སོགས་པའི་དགེ་བའི་རྩ་བ་རྣམས་བསྩགས་པའི་ཕྱིར་རམ། སེར་སྣ་དང་འཆལ་པའི་ཚུལ་ཁྲིམས་ལ་སོགས་པ་འགྲིབ་པར་བྱ་བའི་ཕྱིར་རམ། ནག་པོའི་ཕྱོགས་རྣམས་ཉམས་པར་བྱ་བའི་ཕྱིར་རམ། དཀར་པོའི་ཕྱོགས་རྣམས་འཕེལ་བར་བྱ་བའི་ཕྱིར་རམ། སངས་རྒྱས་ཀྱི་ཆོས་མ་སྐྱེས་པ་རྣམས་བསྐྱེད་པར་བྱ་བའི༌[^1776]ཕྱིར་རམ། ཀུན་ནས་ཉོན་མོངས་པ་སྐྱེས་པ་རྣམས་དགག་པའི་ཕྱིར་རམ། དྲི་མ་དང་བཅས་པའི་གནས་སྐབས་ན་ཀུན་ནས་ཉོན་མོངས་པར་བྱ་བའི་ཕྱིར་རམ། དྲི་མ་མེད་པའི་གནས་སྐབས་ན་རྣམ་པར་བྱང་བར་བྱ་བའི་ཕྱིར་དམིགས་པའི་ཚུལ་གྱིས་ཉེ་བར་གནས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་ནི་དམིགས་པ་ཐམས་ཅད་སེལ་བའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་དེ་སྐད་ཅེས་གསུངས་སོ། །

[Block 2504]
གཉིས་ཀྱི་ཚུལ་གྱིས་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་ཅེས་བྱ་བ་ནི་དམིགས་པར་བྱ་བ་དང་དམིགས་པར་བྱེད་པའི་དངོས་པོས༌[^1777]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2505]
དེ་ལྟར་དགེ་བའི་རྩ་བ་དང་ལྡན་པའི་ཕྱིར༌[^1778]བྱང་ཆུབ་སེམས་དཔའ་ཡང་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་མི་ནུས་ཞེས་བྱ་བ་ནི་དམིགས་པའི་དབང་གིས་ཐབས་མཁས་པ་དང་མི་ལྡན་པའི་ཕྱིར་རོ་ཞེས་དེ་མ་ཐག་ཏུ་འོག་ནས་འཆད་དོ། །

[Block 2506]
ཇི་ལྟར་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་འཛིན་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ལ་དམིགས་ནས་སྦྱིན་པ་བྱིན་ན་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་མིང་དུ་འགྱུར་རོ་སྙམ་ནས་གསོལ་པའོ། །

[Block 2507]
གཉིས་ཀྱི་ཚུལ་གྱིས་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་མི་སྤྱོད་དོ་ཞེས་བྱ་བ་ནི་འདི་བྱང་ཆུབ་ཀྱི་ཕྱིར་བྱའོ་ཞེས་དམིགས་པར་བྱ་བ་དང་དམིགས་པར་བྱེད་པ་གཉིས་ཀྱི་དངོས་པོར་རྣམ་པར་བརྟགས་ནས་མི་སྤྱོད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2508]
བཅོམ་ལྡན་འདས་གལ་ཏེ་གཉིས་ཀྱི༌[^1779]ཚུལ་གྱིས་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་མི་སྤྱོད་ན་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གཉིས་ཀྱི༌[^1780]ཚུལ་གྱིས་བྱང་ཆུབ་ཀྱི་ཕྱིར་ཡོངས་སུ་སྔོ༌[^1781]ཞིང་མི་བྱེད་ན་ཇི་ལྟར་དགེ་བའི་རྩ་བ་རྣམས་མངོན་པར་འཕེལ་བར་འགྱུར་ཞེས་ཞུས་པའོ། །

[Block 2509]
རབ་འབྱོར་གང་གཉིས་ལ་སྤྱོད་པ་དེ་དག་ནི་དགེ་བའི་ཆོས་རྣམས་རྣམ་པར་འཕེལ་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་གཉིས་སུ་མེད་པར་སྤྱོད་པ་ཉིད་དགེ་བའི་རྩ་བ་འཕེལ་བའི་རྒྱུ་ཡིན་གྱི་གཉིས་སུ་སྤྱོད་པ་ནི་མ་ཡིན་ནོ་ཞེས་བསྟན་པ་སྟེ། འདི་ནི་གཉིས་སུ༌[^1782]མེད་པར་སྤྱོད་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 2510]
དེ་ནས་ཡང་ཐབས་མཁས་པས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་སྤྱོད་པ་དང་། བྱང་ཆུབ་ཀྱི་ཕྱོགས་ལ་སྤྱོད་པ་དང་། སངས་རྒྱས་ཀྱི་ཆོས་ལ་སྤྱོད་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་བསྔགས་པའི་ངོ་བོ་ཉིད་ལས་མི་གཡོ་བ་རྣམས་ནི་གཞུང་ཉིད་ལས་གོ་སླའོ། །

[Block 2511]
དངོས་པོ་མ་མཆིས་པས་དངོས་པོ་མ་མཆིས་པ་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པར་བགྱི་བར་ནུས་སམ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམ་པར་རྟོག་པ་བཞི་ནི༌[^1783]མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་ལ་དེ་ལྟ་བུའི་རྣམ་པར་རྟོག་པས་སྤྲོར་རུང་བ་མ་ཡིན་པའི་ཕྱིར་འདི་ལ་ཤེས་པར་བྱེད་པ་མེད་དོ། །

[Block 2512]
ཇི་ལྟར་དངོས་པོ་དང་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་པ་དེ་ལྟར་མཉམ་པ་ཉིད་མཐོང་བ་ནི་མངོན་པར་རྟོགས་པ་ཞེས་བྱ་བ་ནི་སྒྱུ་མ་བྱས་པ་བཞིན་ཏེ་ཀུན་བརྟགས་པ་ནི་དངོས་པོའི་རྣམ་པ་མ་ཡིན་ལ་རི་བོང་གི་རྭ་ལྟར་ཤིན་ཏུ་མེད་པའི་རྣམ་པ་ཡང་མ་ཡིན་ནོ། །

[Block 2513]
དངོས་པོ་དང་དངོས་པོ་མེད་པ་མཉམ་པ་ཉིད་གང་ཡིན་པ་དེ་ནི་དངོས་པོ་དང་དངོས་པོ༌[^1784]མེད་པ་མཉམ་པ་ཉིད་མཐོང་བ་མངོན་པར་རྟོགས་པ་ཞེས་བྱ་སྟེ། འདི་ནི་སྤྲོས་པ་མེད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 2514]
རབ་འབྱོར་འདི་ལྟ་སྟེ་དཔེར་ན། དགྲ་བཅོམ་པས་ལམ་ཐམས་ཅད་ལ་བསླབས་ནས་ཞེས་བྱ་བ་ནི་རྒྱུན་དུ་ཞུགས་པ་དང་། ལན་ཅིག་ཕྱིར་འོང་བ་དང་ཕྱིར་མི་འོང་བ་དང་། དགྲ་བཅོམ་པའི་ལམ་ལ་བསླབས་ནས་སོ། །

[Block 2515]
ཡང་དག་པ་ཉིད་སྐྱོན་མེད་པ་ལ་འཇུག་སྟེ་ཞེས་བྱ་བ་ནི་དགྲ་བཅོམ་པ་ཉིད་ཀྱི་སྐྱོན་མེད་པ༌[^1785]འཇུག་པའོ། །

[Block 2516]
རེ་ཞིག་ལམ་གྱི་སྐད་ཅིག་ལ་དགྲ་བཅོམ་པའི་ལམ་གྱི་འབྲས་བུ་མ་ཐོབ་ཀྱི་བར་དུ་ཞེས་བྱ་བ་ནི་ཇི་སྲིད་དུ་ཐ་མ་ལ་རྣམ་པར་གྲོལ་བའི་ལམ་གྱི་སྐད་ཅིག་མི་སྐྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2517]
སྐད་ཅིག་གཅིག་དང་ལྡན་པའི་ཤེས་རབ་ཀྱིས་ཞེས་བྱ་བ་ནི་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི༌[^1786]སྐད་ཅིག་དང་ལྡན་པས་སོ། །ཤེས་པ་དང་མཐོང་བས་ས་བརྒྱད་པོ་དག་ལ་རྣམ་པར་བལྟས་ནས༌[^1787]ཡོངས་སུ་འདའ་སྟེ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་དྲིས་པའི་ཤེས་པ་བསྟན་པའི་སྐབས་སུ་སྔར་ཇི་སྐད༌[^1788]དུ་བསྟན་པ་བཞིན་ནོ། །

[Block 2518]
དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་སྐད་དང་བརྡ་དང་སྒྲ་ཐམས་ཅད་ཡང་དག་པར་བསྒྲུབ་པར་བྱ༌[^1789]ཞེས་བྱ་བ་ནི་སེམས་ཅན་སྣ་ཚོགས་ཀྱི་སྐད་དང་མཐུན་པར་རོ། །

[Block 2519]
ཆོས་གང་ལ་ཡང་སྒྲུབ༌[^1790]པའམ། འཇིག་པར་བགྱིད་པ་མ་མཆིས་སོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་མཚན་ཉིད་མེད་པ། དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་དེ་དག་བྱང་ཆུབ་སྒྲུབ་པ༌[^1791]མ་ལགས་སམ་ཞེས་ཞུས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་རབ་འབྱོར་དེ་དེ་བཞིན་ནོ་དེ་དེ་བཞིན་ཏེ་ཞེས་བསྔགས་པ་མཛད་དེ། ཆོས་གང་ཡང་ཆོས་གང་ལ་ཡང་སྒྲུབ་པར་མི་བྱེད་དེ། ཆོས་རྣམས་གནས་པའི་མཚན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2520]
དེ་ལྟ་མོད་ཀྱི་བྱིས་པ་རྣམས་ཁོང་དུ་ཆུད་པར་བྱ་བའི་ཐབས་སུ་ཀུན་རྫོབ་ཏུ་འདི་མཛད་དེ། རིམ་པ་འདིས་ཤེས་པར་གྱུར༌[^1792]ནས་དེ་བཞིན་དུ་བསྒྲུབས་པས་འཚང་རྒྱ་བར་འགྱུར་རོ། །

[Block 2521]
འཕགས་པའི་ཆོས་འདུལ་བ་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་ཀྱིས་འདོད་ཆགས་ལ་སོགས་པ་འདུལ་བ་དང་། བསྒྲུབས་པས༌[^1793]འདུལ་བར་གནས་པའི་མཚན་ཉིད་དུ་སྟོན་ཏོ། །

[Block 2522]
འཕགས་པའི་ཆོས་འདུལ་བ་འདི་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བའོ། །

[Block 2523]
འདི་ནི་ཆོས་ཐམས་ཅད་སྒོམ་པ༌[^1794]རྣམ་པར་འཇིག་པའོ་ཞེས་བྱ་བ་ནི། གཟུགས་ལ་སོགས་པའི་ཆོས་ཐམས་ཅད་སྒོམ་པ་མེད་པར་བྱེད་པའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2524]
གཟུགས་དངོས་པོ་ཡོད་ཅེས་བྱ་བར་མི་སྒོམ་མོ་ཞེས་བྱ་བ་ནི་གཟུགས་དངོས་པོ་ཡོད་པའི་ངོ་བོ་ཉིད་དོ་སྙམ་དུ་མི་སྒོམ་པ་དེ་ནི་དངོས་པོ་ལ༌[^1795]འདི་ནི་བདག་གོ་ཞེས་བྱ་བར་མཐའ་གཉིས་ལ་ཆགས་ཏེ་ཞེས་བྱ་བ་ནི་དངོས་པོའི་འདུ་ཤེས་ཅན་ཏེ། འདི་ནི་བདག་སྟེ་གུད་ན་ཡོད་དོ་ཞེའམ། བདག་ནི་གཟུགས་སོ། །

[Block 2525]
བདག་ནི་ཚོར་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཆད་པ་དང་། རྟག་པའི་མཐའ་གཉིས་ལ་ཆགས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །
--- END BLOCKS ---
