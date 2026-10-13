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
[Block 211]
མ་རིག་པ་ཡི༌[^156]རྐྱེན་གྱིས་བྱུང་། །ཞེས་བྱ་བ་ལ་མ་རིག་པ་ནི་འདུ་བྱེད་དང་རྣམ་པར་ཤེས་པ་ལ་སོགས་པའི་དོན་གྱིས༌[^157]མངོན་སུམ་དང་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་རྐྱེན་ཏོ། །

[Block 212]
མ་རིག་པའི་རྐྱེན་ལས་བྱུང་བ་འདུ་བྱེད་ལ་སོགས་པའི་དོན་གལ་ཏེ་རང་གི་མཚན་ཉིད་དུ་གྲུབ་པར་གྱུར་ན་དེ་རང་གི་མཚན་ཉིད་དུ་གྲུབ་པའི་ཕྱིར་མ་རིག་པ་ལ་མི་ལྟོས་སོ། །

[Block 213]
རང་གི་མཚན་ཉིད་དུ་གྲུབ་པ་བུམ་པ་ལ་སོགས་པ་ནི་རང་གི་ངོ་བོ་ལ་སྒྲིབ་པ་མུན་པ་མེད་ན་ཤིན་ཏུ་གསལ་བར་དམིགས་སོ། །

[Block 214]
རྐྱེན་གྱི་བྱེ་བྲག་དག༌[^158]དང་ལྡན་པས་རབ་རིབ་ཅན་གྱིས་ཡོངས་སུ་བརྟགས་པ་སྐྲ་ལ་སོགས་པའི་དངོས་པོར་ཤེས་པ་ནི་ཇི་ལྟ་ཇི་ལྟར་རང་གི་ངོ་བོ་མེད་པར་འགྱུར་ཏེ། རྣམ་པར་བྱང་བའི་མིག་ཅན་དག་ལ་ནི་སྣང་བར་མི་འགྱུར་རོ། །

[Block 215]
དེ་ལྟར་རྣམ་པར་བརྟགས་པའི་མཚན་ཉིད་དུ་གྲུབ་པ་ནི་སྒྲ་ཡང་དག་པ་ལ་སོགས་པ་བཞིན་དུ་ཡོད་པར་གཞག་མི་ནུས་སོ། །

[Block 216]
དེ་བཞིན་དུ་འདུ་བྱེད་ལ་སོགས་པ་འདི་དག་ཀྱང་གལ་ཏེ་རང་གི་མཚན་ཉིད་དུ་གྲུབ་པར་གྱུར་ན་དེའི་ཚེ་བདེན་པའི་དོན་གཏན་ལ་ཕབ་པ་ལས་སྐྱེས་པ་འཕགས་པ་ཡང་དག་པའི་ཡེ་ཤེས་ཅན་རྣམས་ཀྱིས་ཀྱང་རང་གི་མཚན་ཉིད་གཞིག་ཏུ་མི༌[^159]རུང་བ་གཟིགས་པས་བུམ་པ་ལ་སོགས་པ་སྣང་བ་དང་བཅས་པ་བཞིན་དུ་དམིགས་ཤིང་ཡུལ་དུ་འགྱུར་བའི་རིགས་ན་མ་རིག་པ་འགགས་པས་འདུ་བྱེད་འགག་གོ་ཞེས་བྱ་བའི་ཚིག་གིས་དེ་ལྟར་ཡང་མི་འགྱུར་རོ། །

[Block 217]
དེའི་ཕྱིར་ཡང་དག་པའི་ཡེ་ཤེས་ཤར་བ་ན་རབ་རིབ་ཅན་གྱིས་དམིགས་པའི་སྐྲ་ལ་སོགས་པ་འདི་དག་ལྟར་རང་གི་མཚན་ཉིད་མི་སྣང་བས་རང་གི་མཚན་ཉིད་ཡོད་པ་གཞག༌[^160]མི་ནུས་སོ། །

[Block 218]
ནམ་ཞིག་འདི་ལྟར་མ་རིག་པའི་རྐྱེན་ལས་བྱུང་བ་འདུ་བྱེད་ལ་སོགས་པ་ལ་རབ་རིབ་མེད་པ་ཅན་རྣམས་ལྟར་ཡང་དག་པའི་ཡེ་ཤེས་ཀྱིས་བརྟགས་ན་དེ་རབ་རིབ་ཅན་གྱིས་དམིགས་པའི་སྐྲ་ལ་སོགས་པ་བཞིན་དུ་ཡང་དག་པའི་ཡེ་ཤེས་ཀྱི་དུས་ན་འདུ་བྱེད་ལ་སོགས་པའི་སྐྱེ་བ༌[^161]འགག་པ་གང་ཡང་ངེས་པར་མི་དམིགས་སོ། །

[Block 219]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་གང་ཡིན་པ་འདི་ཡི་སྐྱེ་བ་དང་འགག་པ་མི་དམིགས་པའི་ཡེ་ཤེས་ཀྱི་དུས་ན།

[Block 220 [HEADING]]
### ཚིགས་བཅད་བཅུ་གཅིག་པ། ^1-12-0

[Block 221]
མཐོང་བའི་ཆོས་ལ་མྱ་ངན་འདས། །བྱ་བ་བྱས་པའང་དེ་ཉིད་དོ། །

[Block 222]
ཚེ་འདི་ཉིད་ལ་རྣལ་འབྱོར་པ་དེའི་ཆོས་ཐམས་ཅད་མི་དམིགས་པའི་ཡེ་ཤེས་ཀྱི་དུས་གང་ཡིན་པ་དེ་ཉིད་མཐོང་བའི་ཆོས་ལ་མྱ་ངན་ལས༌[^162]འདས་པའོ། །

[Block 223]
བྱ་བ་བྱས་པ་ཉིད༌[^163]ཁོ་ན་བྱ་བ་བྱས་པ་ཉིད་ཅེས་བྱའོ། །

[Block 224]
སྐྱེ་བ་དང་འགག་པ་མི་དམིགས་པའི་ཡེ་ཤེས་ཀྱི་དུས་གང་ཡིན་པ་དེ་ཉིད་མཐོང་བའི་ཆོས་ལ་མྱ་ངན་ལས་འདས་པ་དང༌[^164]བྱ་བ་བྱས་པ་ཞེས་བྱ་བར་ཤེས་པར་བྱ་སྟེ། ལུང་དག་ལས་དགེ་སློང་མཐོང་བའི་ཆོས་ལ་མྱ་ངན་ལས་འདས་པ་ཞེས་གསུངས་པ་དང་འཕགས་པ་ཤཱ་རིའི་བུས་མྱ་ངན་ལས་འདས་པ་མངོན་སུམ་དུ་བྱས་ཏེ། མདོ་འདི་བཤད་དོ་ཞེས་འབྱུང་བ་དེ་ཉིད་དེའི་མཐོང་བའི་ཆོས་ལ་མྱ་ངན་ལས་འདས་པ་ཡིན་པར་བལྟའོ། །

[Block 225]
སྐྱེ་བ་ཟད་དོ། །

[Block 226]
ཚངས་པར་སྤྱོད་པ་བསྙེན་ཏོ། །

[Block 227]
བྱ་བ་བྱས་སོ། །

[Block 228]
འདི་ལས་སྲིད་པ་གཞན་མི་ཤེས་སོ་ཞེས་གང་གསུངས་པ་དེ་ཡང་བྱ་བ་བྱས་པ་འདི་ཉིད་ཡིན་པར་རིག་པར་བྱ་སྟེ། དེ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་སྐྱེ་བ་མེད་པའོ།[^165] །ཅི་སྟེ་ཞེས་པ་འདི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་སྐྱེ་བ་དང་འགག་པ་མི་དམིགས་པའི་མཚན་ཉིད་དེ་ཁོ་ན་བོར་ཏེ། དམིགས་པའི་དངོས་པོ་རང་གི་མཚན་ཉིད་ཀྱི་ངོ་བོ་ཞིག་ཡོད་པར་ཡོངས་སུ་རྟོག་ན་དངོས་པོ་རྣམས་ནི་ཕན་ཚུན་ཐ་དད་པའི་རང་གི་ངོ་བོ་ཡིན་པས་དེ་ངེས་པར་དེས་བྱེ་བྲག་ཏུ་ཡོངས་སུ་གཅད༌[^166]དགོས་པར་འགྱུར་ཏེ། ངོ་བོ་གཞན་ཡོངས་སུ་ཤེས་པས་དངོས་པོའི་ངོ་བོ་གཞན་ཡོངས་སུ་གཅད་པར༌[^167]མི་ནུས་སོ། །

[Block 229]
སྔོན་པོའི་ངོ་བོ་ཤེས་པས་སེར་པོ་ཡོངས་སུ་གཅོད་མི་ནུས་པ་དེ་བཞིན་དུ་འདི་ལ་ཡང་།

[Block 230 [HEADING]]
### ཚིགས་བཅད་བཅུ་གཉིས་པ། ^1-13-0

[Block 231 [VERSE]]
ཆོས་ཤེས་དེ་ཡི་འོག་ཏུ་ནི། །
འདི་ལ་བྱེ་བྲག་དབྱེ་ཡོད་ན། །
ཤིན་ཏུ་ཕྲ་བའི་དངོས་ལ་ཡང་། །
གང་གིས་སྐྱེ་བར་རྣམ་བརྟགས་པ། །
རྣམ་པར་མི་མཁས་དེ་ཡིས་ནི། །
རྐྱེན་ལས་བྱུང་བའི་དོན་མ་མཐོང་། །

[Block 232]
དེ་ལ་ཆོས་ཞེས༌[^168]བྱ་བའི་སྒྲ་ནི་མྱ་ངན་ལས་འདས་པ་ལ་བྱའོ། །

[Block 233]
དེ་ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ངོ་བོ་ཉིད་ལས་གཞན་མ་ཡིན་ཏེ། མདོ་སྡེ་ལས་ཀྱང་སུས་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་མཐོང་བ་དེས་ཆོས་མཐོང་ངོ་ཞེས་ཇི་སྐད་འབྱུང་བ་ཡིན་ནོ། །

[Block 234]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དེ་དང་མྱ་ངན་ལས་འདས་པ་ཐ་མི་དད་པའི་རང་བཞིན་དུ་གྱུར་པར་ཡོངས་སུ་གཅོད་པའི་ཤེས་པ་གང་ཡིན་པ་དེ་ཆོས་ཤེས་པའོ། །

[Block 235]
ཆོས་ཤེས་པས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་དོན་ཁོང་དུ་ཆུད་པར་བྱ་སྟེ།

[Block 236]
དེ་ཡང་བསྟན་བཅོས་ལས།

[Block 237 [VERSE]]
གང་དང་གང་དག་རྟེན་འབྱུང་བ། །
དེ་དག་ངོ་བོ་ཉིད་ཀྱིས་ཞི། །
དེ་ལྟ་བས་ན་སྐྱེ་བ་དང་། །
སྐྱེས་པ་ཉིད་ནི་ཞི་བའོ། །

[Block 238]
ཞེས་འབྱུང་བ་ཡིན་ནོ། །

[Block 239]
འདི་ལ་སྐྱེས་པར་གྱུར་པ་དང་། །སྐྱེ་བ་ངོ་བོ་ཉིད་ཀྱིས་སྐྱེ་བ་མེད་པ་གང་ཡིན་པ༌[^169]རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་དོན་དུ་གསུངས་སོ། །

[Block 240]
སྡུག་བསྔལ་ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡིན་པས་རང་བཞིན་གྱིས་མ་སྐྱེས་པའོ། །

[Block 241]
གང་གིས༌[^170]ངོ་བོ་ཉིད་ཀྱིས་སྐྱེ་བ་མེད་པ་དེ་ཉིད་མྱ་ངན་ལས་འདས་པ་སྟེ། གཉི་ག་ཡང་མ་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 242]
འདི་ལྟར་ཡང་འཁོར་བ་ལས་ནི་མྱ་ངན་འདས། །

[Block 243 [VERSE]]
བྱེ་བྲག་དབྱེ་བ་ཅུང་ཟད་མེད། །
མྱ་ངན་འདས་ལས་འཁོར་བ་ཡང་། །
བྱེ་བྲག་དབྱེ་བ་ཅི་ཡང་མེད། །
མྱ་ངན་འདས་ཀྱི་མཐའ་འདི་ནི། །

[Block 244 [VERSE]]
འཁོར་བའི་མཐའ་ཡང་དེ་ཡིན་ཏེ། །
དེ་གཉིས་ལ་ནི་ཅུང་ཟད་ཀྱང་། །
བྱེ་བྲག་ཤིན་ཏུ་ཕྲ་བའང་མེད། །

[Block 245]
ཅེས་བྱ་བ་བསྟན་པ་ཡིན་ནོ། །

[Block 246]
མཐའ་ཞེས་བྱ་བའི་སྒྲ་ནི་མཆོག་ཏུ་བྱུང༌[^171]བའོ། །

[Block 247]
མཆོག་ཏུ་བྱུང་བ་ཞེས་བྱ་བ་ནི་ཕུལ་དུ་ཕྱིན་པ་ཞེས་བྱ་སྟེ། བྱིས་པའི་སྐྱེ་བོ་རྣམས་ཀྱི་སྤྱོད་ཡུལ་དུ༌[^172]གྱུར་པའི་མཐའི་རང་བཞིན་ནི་གཉི་ག་ཡང་མ་སྐྱེས་པའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱིས་སྐྱེ་བ་མེད་པས་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་གཉིས་གཅིག་གོ། །

[Block 248]
དེ་བས་ན་མྱ་ངན་ལས་འདས་པ་དང་ཁྱད་པར་མེད་པའི་ཕྱིར་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ལ་ཡང་ཆོས་ཞེས༌[^173]བྱ་སྟེ། དེ་མཐོང་བས་མྱ་ངན་ལས་འདས་པ་ཡང་མཐོང་བས་ན་སུས་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་མཐོང་བ་དེས་ཆོས་མཐོང་ངོ་། །ཆོས་ཀྱི་ངོ་བོ་ཉིད་དང་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཐ་མི་དད་པས༌[^174]ན༌[^175]མཐོང་བས་སངས་རྒྱས་མཐོང་བ་ཡིན་ནོ། །

[Block 249]
དེ་ལྟར་ན་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་སྐྱེ་བ་མེད་པ༌[^176]ལ་དམིགས་པའི་ཆོས་ཤེས་པས་རྟེན་བདེན་པ་གསུམ་རྟེན་ཅིང་འབྲེལ༌[^177]བར་འབྱུང་བ་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་ལ། མྱ་ངན་ལས་འདས་པ་ཡང་དེའི་ངོ་བོ་ཉིད་ཡིན་པར་མཐོང་བས་མངོན་པར་རྟོགས་པ་གཅིག་ཏུ་ཟད་དོ། །

[Block 250]
དེ་ལ་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ལ་དམིགས་པའི་ཆོས་ཤེས་པ་སྡུག་བསྔལ་གྱི་སྐྱེ་བ་མེད་པ་དང་འགག་པ་མེད་པ་ཡོངས་སུ་གཅོད་པ་གང་ཡིན་པའི་བདག་ཉིད་དེ་སྡུག་བསྔལ་ཡོངས་སུ་ཤེས་སོ། །
--- END BLOCKS ---
