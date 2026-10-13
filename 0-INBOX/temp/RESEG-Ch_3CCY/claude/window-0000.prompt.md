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
[Block 1 [HEADING]]
## ༄༅། །སྟོང་ཉིད་བདུན་ཅུ་པའི་འགྲེལ་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ཤཱུ་ནྱ་ཏཱ་སཔྟ་ཏི༌[^1]ཀ་བྲྀཏྟི། བོད་སྐད་དུ། སྟོང་ཉིད་བདུན་ཅུ་པའི་འགྲེལ་པ།

[Block 4 [VERSE]]
སངས་རྒྱས་ལ་ཕྱག་འཚལ་ལོ། །
མདོར་བསྡུས་དེ་ཉིད་ངེས་པའི་ཕྱིར། །
སྟོང་ཉིད་བདུན་ཅུ་གསུང་བ་གང་། །

[Block 5]
དེ་ལ་ཕྱག་འཚལ་བདུན་ཅུ་པར།[^2] །བསྟན་དོན་བདག་གིས་ཡང་དག་དབྱེ། །འདིར་སློབ་དཔོན་བདག་ཉིད་ཀྱིས་ཟབ་པ་དང་ཤིན་ཏུ་རྒྱ་ཆེ་བའི་དངོས་པོ་རྣམས་ཀྱི་དོན་རྣམ་པར་ངེས་པའི་དབུ་མའི་བསྟན་བཅོས་རྣམས་བརྩམས་པ་ཡོད་མོད་ཀྱི། གཞུང་དང་དོན་དག་ཤིན་ཏུ་མང་བའི་ཕྱིར་དང་། ཤེས་རབ་ཆུང་བ་རྣམས་བྱ་བར་ངེས་པ་འདི་ལ་ཀུན་ནས་ཆགས་པ་དང་ལྡན་པ་སྟོང་པ་ཉིད་བསྟན་པའི་སྣོད་དུ་གྱུར་ཀྱང་། དེ་ཐོབ་པ༌[^3]དང་། འཛིན་པ་དང་། ཉེ་བར་སེམས་པས་འཇིགས་པ༌[^4]རྣམས་ལ་སློབ་དཔོན་གྱི་ཐུགས་ཀྱི་རྒྱུད་ཤེས་རབ་དང་ཐབས་དང་བརྩེ་བའི་རྗེས་སུ་ཞུགས་པའི་ཕྱིར་ཚིགས་སུ་བཅད་པ་བདུན་ཅུས་ཀྱང་ཁྱད་པར༌[^5]དུ་འཕགས་པ༌[^6]དོན་གྲུབ་པར་གཟིགས་ནས། མདོར་བསྡུས་པས་དེ་ཁོ་ན་ཉིད་ངེས་པའི་དོན་དུ་སྟོང་པ་ཉིད་བདུན་ཅུ་པ་ཞེས་བྱ་བ་འདི་བརྩམས་སོ། །

[Block 6 [HEADING]]
## སྔོན་འགྲོའི་དོན། ^II-0

[Block 7]
དེ་ཡང་མདོར་བསྡུས་པས་དེ་ཁོ་ན་ཉིད་ངེས་པ་འདི་ནི་ཤིན་ཏུ་དོན་ཆེན་པོ་ཡང་གནས་པ་དང་སྐྱེ་བ་ལ་སོགས་པའི་སྒོ་ནས་འཇིག་རྟེན་པས་བདེ་བླག་ཏུ་ཤེས་པར་འགྱུར་རོ། །

[Block 8]
གང་ཞིག་ཐོག་མ་མེད་པ་ནས་ལོག་པའི་ལྟ་བ་ལ་གོམས་པའི་ཕྱིར༌[^7]བྱིས་པ་ལོག་པར་རྟོག་པའི་དངོས་པོའི་རང་གི་མཚན་ཉིད་ཀྱིས་གནས་པའི་མཚན་ཉིད་ལ་གནས་པ་ལ་ཆགས་པའི་རྟེན་ལ་དངོས་པོར་ཉེ་བར་བརྟགས་ལ། དེའི་དབང་ལས་བྱུང་བའི་འདོད་ཆགས་ལ་སོགས་པའི་ཉོན་མོངས་པའི་དབང་ཕྱུག་གཞན་ལ་རག་ལས་ནས་འཇུག་པ་དག་ལས་མི་བྱེད་པར་གནས་པ་ནི་སྐད་ཅིག་ཀྱང་མི་རྙེད་ལ། གལ་ཏེ་ཡང་ལས་མི་བྱེད་པར་འགྱུར་གྲང་ན། འདི་ལྟར་ལས་ཅན་རྣམས་ཀྱི་ལས་དེའི་རྒྱུ་ལས་བྱུང་བའི་འབྲས་བུ་མེད་པར་འགྱུར་བའི་ཕྱིར་ངེས་པར་སྐྱེ་བ་ལྡོག་པར་འགྱུར་ན། གང་ཞིག་དར་དྲག་ཅིང་རྒྱུན་རིང་བའི་མཆོག་ཏུ་འཛིན་པ་དང་། ཁོན༌[^8]དུ་འཛིན་པ་དང་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པའི་དབང་ཕྱུག་གིས་བྱིན་གྱིས་བརླབས་པའི་སྐྱེ་བའི་སྐྱེ༌[^9]བོ་རྣམས་ལས་མི་བྱེད་པར་འགྱུར་ཞིང་། ལས་ཀྱི་འབྲས་བུ་ཡང་སྲིད་འབྱུང་བར་མི་འགྱུར་བ་འདི་ལྟ་བུ་ཡོད་པ་ཡང་མི་སྲིད་དོ། །

[Block 9]
དེའི་ཕྱིར་གནས་པ་ལ་སོགས་པ་ལ་མངོན་པར་ཞེན་པ་ནི་བྱིས་པ་རྣམས་ཀྱི་དོན་མ་ཡིན་པ་ཐམས་ཅད་ཀྱི་རྒྱུའི་གཙོ་བོའོ། །

[Block 10]
གནས་པ་འདི་ཡང་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་ཆོས་ཉིད་དང་རྗེས་སུ་འབྲེལ་པ་དང་ལྡན་པས་ངེས་པར་སྐྱེ་བ་དང་འཇིག་པ་ལ་ལྟོས་ལ། སྐྱེ་བ་དང་འཇིག་པ་དང་མི་ལྡན་པའི་ནམ་མཁའ་ལ་སོགས་པ་ནི་གནས་པ་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱའོ། །

[Block 11]
དེས༌[^10]ན་གནས་པའི་སྒོ་ནས་འདུས་བྱས་རྣམས་འཆད་པར་གྱུར་པའི༌[^11]མཚན་ཉིད་དང་མཚན་གཞི་ལ་སོགས་པ་ལ་དཔྱད་པ་སྟོང་པ་ཉིད་ལ་མོས་པ་རྣམས་ཀྱི་ཡིད་མགུ༌[^12]བའི་ཕྱིར་བརྗོད་དོ། །

[Block 12]
གཞན་ཡང་གནས་པ་ལ་སོགས་པའི་དོན་འདི་རྣམས་འདུས་བྱས་ཀྱི་མཚན་ཉིད་ཉེ་བར་བསྟན་བཞིན་པའམ་བཟུང་བཞིན་པ་དག་མཚན་གཞི་ལ་ལྟོས་པ་ཁོ་ནས་གནས་ལ། མཚན་གཞི་དེ་ཡང་མཚན་ཉིད་མེད་ན་མཚན་ཉིད་ལ་ལྟོས་པས་མཚན་གཞི་མེད་པའི་ཕྱིར་རོ། །

[Block 13]
དེ་བཞིན༌[^13]ཕན་ཚུན་བརྟེན་པས་བསྡུས་པའི་བདག་ཉིད་ཀྱི་དངོས་པོ་མཚན་གཞི་དང་མཚན་ཉིད་དག་མཚན་ཉིད་ལ་ལྟོས༌[^14]པར་མཚན་གཞིར་གྱུར་པ་གང་དུ་གནས་པ་ལ་སོགས་པའི་མཚན་ཉིད་ཅན་གྱི་རྟེན་འགྲུབ་པར་ག་ལ་འགྱུར། གནས་པ་ལ་སོགས་པ་མ་གྲུབ་པས་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་ཡོད་པ་མ་ཡིན་ལ། རྣམ་པར་ཤེས་པ་ལ་སོགས་པའི་དངོས་པོ་མེད་ན་དེ་ལ་ལྟོས་ནས་དེ་ལས་ལོག་པའི་དངོས་པོ་མེད་པའི་རང་བཞིན་ག་ལ་ཡོད། དངོས་པོ་མེད་པར་གྱུར་པ་ལ་ཅི་རྣམ་པར་ཤེས་པའི་དམིགས་པ་ཡོད་དམ། དམིགས་པས་བསྐྱེད་པའི་རྣམ་པར་ཤེས་པ་དམིགས་པ་མེད་པར་སྐྱེ་བར་ནུས་པ་མ་ཡིན་ནོ། །

[Block 14]
རྣམ་པར་ཤེས་པ་སྐྱེ་བ་མེད་ན་འདོད་ཆགས་ལ་སོགས་པ་རྟེན་མེད་པས་ན་མེད་ལ། ཕྱིན་ཅི་ལོག་རྩད་ནས་ཕྱུང་ལ༌[^15]ཡོད་པ་མ་ཡིན་པས་ལས་སྐྱེད་པའི་རྒྱུ་མ་ཡིན་ནོ། །

[Block 15]
ལས་མེད་ན་དེའི་འབྲས་བུ་མ་འོངས་པའི་སྐྱེ་བ་མི་འབྱུང་བ་དང་། སྔར་སྐྱེས་པའི་ཉེ་བར་ལེན་པ་ཟད་པས་ཉེར་ལེན་མེད་དེ། ངེས་པར་གནས་པ་ལ་སོགས་པ་ལ་དཔྱོད་པ་རྣམས་མྱ་ངན་ལས་འདས་པའི་སྣོད་དུ་འགྱུར་རོ། །

[Block 16]
ཇི་སྐད་དུ་འཕགས་པ་ལྷས།

[Block 17 [VERSE]]
གང་གི༌[^16]རྣམ་ཤེས་དེ་ཉིད་དང་། །
གནས་པ་ལ་སོགས་རྣམ་ཤེས་པ། །
དེ་ཚེ་བློ་ལྡན་ཉོན་མོངས་ལ། །
ནམ་ཡང་གནས་པ་མ་ཡིན་ནོ། །

[Block 18]
ཞེས་གསུངས་སོ། །

[Block 19]
གལ་ཏེ་དེ་ལྟར་གནས་པ་ལ་སོགས་པ་མེད་ན། དེ་ལྟ་ན་གང་ཞིག་འདི་ལྟར་ཕྱིན་ཅི་ལོག༌[^17]གི་མ་རིག་པ་མ་ལུས་པ༌[^18]བྲལ་བས་མངོན་པར་རྟོགས་པའི་སངས་རྒྱས་ཀྱིས་གསུངས་པ། དགེ་སློང་དག་འདུས་བྱས་ནི་སྐྱེ་བར་ཡང་རབ་ཏུ་ཤེས་སོ། །

[Block 20]
འགག་པར་ཡང་རབ་ཏུ་ཤེས་སོ། །

[Block 21]
གནས་པ་ལས་གཞན་དུ་འགྱུར་བར་ཡང་རབ་ཏུ་ཤེས་སོ་ཞེས་སོ། །

[Block 22]
དེ་ཇི་ལྟར་དེ་བཞིན་གཤེགས་པའི་གསུང་དོན་མེད་པར་འགྱུར་བ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 23]
འདི་དག་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ་ནི༌[^19]བདེན་ལ། འདི་དག་དོན་མེད་པར་འགྱུར་བར་རིགས་པ་མ་ཡིན་ཏེ།

[Block 24]
རྒྱུ་མཚན་ཅིས་ན་གང་གི་ཕྱིར། །

[Block 25 [HEADING]]
## གཞུང་དོན། ^1-0

[Block 26 [HEADING]]
### ཚིགས་བཅད་དང་པོ། ^1-1-0

[Block 27 [VERSE]]
གནས་པའི༌[^20]སྐྱེ་འཇིག་ཡོད་མེད་དམ། །
དམན་པའམ་མཉམ་པའམ་ཁྱད་པར་ཅན། །
སངས་རྒྱས་འཇིག་རྟེན་སྙེད་དབང༌[^21]གིས། །
གསུངས་ཀྱི༌[^22]ཡང་དག་དབང་གིས་མིན། །

[Block 28]
འདིར་དངོས་པོ་རྣམས་ཕྱིན་ཅི་ལོག་དང་ཕྱིན་ཅི་མ་ལོག་པའི་ཤེས་པའི་དབང་གིས་བདེན་པ་གཉིས་ཏེ། ཀུན་རྫོབ་ཀྱི་བདེན་པ་དང་དོན་དམ་པའི་བདེན་པ་ཞེས་བྱ་བར་འཕགས་པས་ཐ་སྙད་མཛད་ལ།[^23] འཕགས་པ་འབའ་ཞིག་ཁོ་ན་བདེན་པ་གཉིས་རྣམ་པར་འཇོག་པར་མཛད་པ་མ་ཡིན་ཏེ། འཇིག་རྟེན་པ་འཇིག་རྟེན་གྱི་ཐ་སྙད་ལ་མཁས་པ་རྣམས་ཀྱང་བདེན་པ་གཉིས༌[^24]ཐ་སྙད༌[^25]བྱེད་དོ། །

[Block 29]
འདི་ལྟར་བདེན་པའི་དོན་ནི་མི་སྣང་ལ་སྒྲོ་བཏགས་པའི་དོན་རིགས་པར༌[^26]ཐ་སྙད་བྱེད་པ་ལ་འདི་ནི་ཀུན་རྫོབ་པའོ་ཞེས་ཐ་སྙད་བྱེད་དོ། །

[Block 30]
གང་དུ་བདེན་པའི་དོན་མི་སྣང་བ་མ༌[^27]ཡིན་ལ་སྒྲོ་མ་བཏགས་པའི་དོན་རིག་པའི་ཐ་སྙད་ལ། དེ་ལ་འདི་ནི་དོན་དམ་པ་ཁོ་ནའོ༌[^28]ཞེས་རྣམ་པར་འཇོག་གོ། །

[Block 31]
རེ་ཞིག་གང་ལ་འདི་ཀུན་རྫོབ་ཅེས་ཐ་སྙད་བྱེད་པ་དེ་ལ་མི་བདེན་པའི་དོན་འཇིག་རྟེན་པས་ཁོང་དུ་ཆུད་པ་ཉིད་ཀྱིས་དེའི་ཡུལ་ལ་བསམ་པ་གཏང་བར་མི་བྱའོ། །

[Block 32]
གང་ཡང་འཇིག་རྟེན་གྱི་ཐ་སྙད་ལ་བདེན་པར་འདོད་པ་དེ་ཡང་འཕགས་པ་རྣམས་འཇིག་རྟེན་ཀུན་རྫོབ་ཀྱི་བདེན་པར་བཞེད་དེ། མེད་པའི་དོན་ལ་ཐ་སྙད་འདོགས་པ་ལྟར་དོན་མེད་པ་ཉིད་དུ་བརྗོད་དོ། །

[Block 33]
དེ་ཡང་བརྫུན་པ་ཉིད་དུ་རྟོགས་པར་བྱེད་པ། འཕགས་པ་ཉིད་ཀྱིས་འཆད་པར་འགྱུར་བའི་འཇིག་རྟེན་པ༌[^29]རབ་ཏུ་གྲགས་པའི་རིགས་པ་ཉིད་ཀྱིས༌[^30]ཉེ་བར་སྟོན་པར་མཛད་དེ། དེ་ནི་རབ་ཏུ་གྲགས་པའི་དཔེས་མ་གྲགས་པའི་དོན་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 34]
དེ་ནི་འདིར་འཇིག་རྟེན་གྱི་ཐ་སྙད་ལ་རྣམ་པར་དཔྱད་ན། ཡང་དག་པའི་དོན་མ་གྲུབ་པའི་ཕྱིར་འཕགས་པས་འཇིག་རྟེན་གྱི་ཐ་སྙད་ལ་ཀུན་རྫོབ་ཅེས་གསུངས་སོ། །

[Block 35]
ཀུན་རྫོབ་ཀྱི་སྒྲ་ནི་འཇིག་རྟེན་པའི་ཐ་སྙད་ཀྱི་རྣམ་གྲངས་མ་ཡིན་ཏེ། ཀུན་རྫོབ་དང་དོན་དམ་པའི་དབྱེ་བས་དེ་ནི་རྣམ་པ་གཉིས་སུ་གནས་པའི་ཕྱིར་དང་ཐ་སྙད་ཀྱི་ཕྱོགས་གཅིག་ལ་ཀུན་རྫོབ་ཀྱི་སྒྲས་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 36]
རིགས་པའི་སྟོབས་ཀྱིས༌[^31]འདིའི་དོན་ནི་གང་ཞིག་འཇིག་རྟེན་གྱི་ཐ་སྙད་ལ་ཀུན་རྫོབ་ཀྱི་སྒྲས་བརྗོད་ལ། དེ་ནི་འདི་ལྟར་གང་འཇིག་རྟེན་གྱི་ཐ་སྙད་འདི་ནི་འཇིག་རྟེན་ཀུན་རྫོབ་སྟེ། དེ་ནི་དེ་ཁོ་ན་ཉིད་མ་ཡིན་ནོ་ཞེས་འཕགས་པ་ཁོ་ན་གསུངས་པར༌[^32]རིགས་ལ། ཐ་སྙད་དང་ཀུན་རྫོབ་ཀྱི་སྒྲ་དག་ཀྱང་རྣམ་གྲངས་ཉིད་དེ། དེ་ལ་སྐྱོན་མེད་དོ། །

[Block 37]
དེ་སྐད་དུ་མདོ་ལས།

[Block 38]
ཀུན་རྫོབ་ཀྱི་བདེན་པ་གང་ཞེ་ན། ཇི་སྲིད་དུ་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཡི་གེ་དང་སྐད་ཀྱིས་སྟོན་པའོ། །ཞེས་སོ། །

[Block 39]
ཡང་ན་ཅི་ཞིག་ལ་འདིར་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཅེས༌[^33]བྱ་ཞེ་ན། དེ་ལ་རེ་ཞིག་བུད་ཤིང་ལ་བརྟེན་ནས་མེ་བཞིན་དུ་ཕུང་པོ་ལ་བརྟེན་ནས་བརྟགས་པའི་གང་ཟག་ལ་འཇིག་རྟེན་ཞེས་བརྗོད་དོ། །

[Block 40]
དེ་ཡང་ཕྱིན་ཅི་ལོག་དང་ཕྱིན་ཅི་མ་ལོག་པ་ཉིད་ཀྱིས༌[^34]རྣམ་པ་གཉིས་སོ། །
--- END BLOCKS ---
