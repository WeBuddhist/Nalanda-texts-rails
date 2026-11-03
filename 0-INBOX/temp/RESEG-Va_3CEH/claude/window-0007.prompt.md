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
[Block 246]
ས་བོན་ཐམས་ཅད་པ་ཉིད༌[^166]ནི་དེས་བསྒོས་པའི་ཕྱིར་རོ། །

[Block 247]
ལུས་ཐམས་ཅད་དང་འགྲོ་བ་ཐམས་ཅད་ཅེས་བྱ་བ་དེ་ལ་འགྲོ་བ་ནི་ལྔའོ། །

[Block 248]
འགྲོ་བ་དེ་དང་དེའི་རིས་མཐུན་པ་དང་རིས་མི་མཐུན་པ་རྣམ་པ་སྣ་ཚོགས་པ༌[^167]ནི་ལུས་ཐམས་ཅད་དོ། །

[Block 249 [HEADING]]
#### ས་བོན་གྱི་ངོ་བོ་ཉིད། ^1-4-5-0

[Block 250]
ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཆོས་ཐམས་ཅད་ཀྱི་ས་བོན་དུ་བསྟན་པ་དེ་ས་བོན་གྱི་ངོ་བོ་ཉིད་དུ་ཀུན་ཏུ་གསལ་བར་བྱ་བར་འདོད་ནས། ཕྱི་དང་ནང༌[^168]ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་ལྔས་བསྟན་ཏོ། །

[Block 251]
དེ་ལ་ཕྱི་དང་ནང་ལ་སོགས་པ་ལ་ནང་གི་བདག་ཉིད་ཅན་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པའོ། །

[Block 252]
མི་གསལ་བ་ནི་ཕྱི་རོལ་ཏེ། ལུང་དུ་མ་བསྟན་པས་ཞེས་བྱ་བའི༌[^169]དོན་ཏོ། །

[Block 253]
གཉིས་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་དགེ་བ་དང་། མི་དགེ་བའོ། །

[Block 254]
དོན་གཞན་ཡང་ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བའོ། །

[Block 255]
ཀུན་རྫོབ་ཅེས་བྱ་བ་ནི་ཕྱི་རོལ་ཏེ། ཀུན་རྫོབ་དེའི་ས་བོན་ཞེས་བརྗོད་དོ། །

[Block 256]
དེ་བས་ན་འདི་དག་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཡོངས་སུ་གྱུར་པ་ཉིད་ཡིན་ནོ། །

[Block 257]
དམ་པའི་དོན་ཡང་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་སྟེ། དེ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་ས་བོན་ནོ། །

[Block 258]
འདི་ལྟར་ཀུན་གྱི་ས་བོན་ཉིད་ནི་རྣམ་པ་དྲུག་གོ། །

[Block 259 [HEADING]]
##### སྐད་ཅིག་པ། ^1-4-5-1-0

[Block 260]
ཡང་དེ་དག་ནི་སྐད་ཅིག་པ་སྟེ། གཉི་ག་ཡང་བྱུང་མ་ཐག་ཏུ་འཇིག་པའི་ཕྱིར་དང་། ས་བོན་གྱི་ངོ་བོ་ཉིད་དུ་རྟག་ཏུ་མི་རུང་བའི་ཕྱིར་དང་། དེ་བཞིན་དུ་དུས་ཐམས་ཅད་དུ་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 261 [HEADING]]
##### ལྷན་ཅིག་འབྱུང་བ། ^1-4-5-2-0

[Block 262]
ལྷན་ཅིག་འབྱུང་བ་ནི་འདས་པ་མ་ཡིན། མ་འོངས་པ་མ་ཡིན། ཐ་དད་དུ་མ་ཡིན་པར་ས་བོན་གྱི་དུས་ན༌[^170]གང་ཡིན་པ་དེ་ཉིད་ནི་འབྲས་བུ་སྐྱེད༌[^171]པའོ། །

[Block 263 [HEADING]]
##### རྒྱུན་ཆགས་འབྱུང་བ། ^1-4-5-3-0

[Block 264]
དེ་ནི་རྒྱུན་ཆགས་འབྱུང་བར་འདོད། དེ་ནི་རྟེན་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ནི་ཇི་སྲིད་གཉེན་པོ་སྐྱེས་ཀྱི་བར་དུའོ། །

[Block 265]
ཕྱི་རོལ་གྱི་ཡང་ཇི་སྲིད་རྩ་བ་ཡོད་པ་དང་། ཇི་སྲིད་སྨིན་པ་ཡོད་ཀྱི་བར་དུའོ། །

[Block 266 [HEADING]]
##### ངེས་པ། ^1-4-5-4-0

[Block 267]
ངེས་དང་སྟེ་གང་ས་བོན་ཐམས་ཅད་ལས་ཐམས་ཅད་འབྱུང་བ་ནི་མེད་དེ། སོ་སོར་ངེས་པ་དེའི་ས་བོན་ལས་དེ་འབྱུང་ངོ་། །

[Block 268 [HEADING]]
##### རྐྱེན་ལ་ལྟོས་པ། ^1-4-5-5-0

[Block 269]
རྐྱེན་ལ་ལྟོས་པ༌[^172]དང་།[^173] ས་བོན་ཐམས་ཅད་ལས་ཐམས་ཅད་དུ་མི་འབྱུང་སྟེ། རྐྱེན་གང་ཐོབ་པ་ན་དེ་འབྱུང་བར་འགྱུར་རོ། །

[Block 270 [HEADING]]
##### རང་གི་འབྲས་བུས་བསྒྲུབས་པ། ^1-4-5-6-0

[Block 271]
རང་གི་འབྲས་བུས་བསྒྲུབས་པ་ཞེས་བྱ་བ་ལ། རང་གི་ས་བོན་ལས་རང་གི་འབྲས་བུ་འབྱུང་བ་སྟེ། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལས་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཉིད་དང་། འབྲུ་ལས་འབྲུ་ཉིད་དེ། དེ་ལྟར་རེ་ཞིག་ས་བོན་ལས་འབྲས་བུ་འབྱུང་ངོ་། །

[Block 272 [HEADING]]
#### བག་ཆགས་ཀྱི་མཚན་ཉིད། ^1-4-6-0

[Block 273]
བག་ཆགས་ཀྱི་མཚན་ཉིད་ཇི་ལྟ་བ༌[^174]བཞིན་དུ་བསྟན་པར་བྱ་བ་ནི། བརྟན་པ༌[^175]ལ་བསྒོ་བར་བྱའོ།[^176] །གཡོ་བ་ལ་ནི་མ་ཡིན་ཏེ། རླུང་བཞིན་ནོ། །

[Block 274]
རླུང་གིས་ནི་བསྒོ་བ་མི་འཛིན་ཏེ། གང་གི་ཕྱིར་རྒྱང་གྲགས་ཙམ་གྱི་བར་དུ་ཡང་དེ་ལ་བསྒོས་པ་རྗེས་སུ་མི་འཇུག་གོ། །

[Block 275]
ཙམ་གྱི་བར་གྱིས་ནི་དཔག་ཚད་བརྒྱའི་བར་དུ་ཡང་དྲི་རྗེས་སུ་འབྱུང་ངོ་། །ལུང་མ་བསྟན་ཞེས་བྱ་བ་ནི་ལུང་དུ་མ་བསྟན་པ་ལ་དྲི་ཞེས་བྱ་བའི་དོན་ཏོ།[^177] །གང་དྲི་མི་ཞིམ་པ་སྒོག་སྐྱ་དང་དེ་བཞིན་དུ་དྲི་ཞིམ་པ་ལ་ནི་མ་ཡིན་ཏེ། ལུང་དུ་མ་བསྟན་པ་ལ་སྒོ་བར༌[^178]བྱེད་དོ། །

[Block 276]
བསྒོ་བར་འོས་པ་ལ་སྒོ་བར་བྱེད་ཀྱི་བསྒོ་བར་བྱ་བ་མ་ཡིན་པ་འདི་ལྟ་སྟེ། རྡོ་བ་དང་། དངུལ་དང་། གསེར་ལ་སོགས་པ་ལ༌[^179]མི་བསྒོའོ། །

[Block 277]
གང་བསྒོ་བ་འཛིན་པ་དེ་ལ་སྒོ་བར༌[^180]བྱེད་པས་བསྒོ་བ་ཞེས་བྱ་བ་སྟེ། བསྒོ་བར་འོས་པ་ལའོ། །

[Block 278]
འབྲེལ་པ་ལ་སྒོ༌[^181]བྱེད་ཅེས་བྱ་བ་ནི་འབྲེལ་པ་མེད་པ་ལ་ནི་མ་ཡིན་ཏེ། བར་ཆད་མེད་པར་འབྱུང་བ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 279]
དེ་ལས་གཞན་ནི་མིན་ཞེས་བྱ་བ་ནི་དེ༌[^182]ལས་གཞན་ཉིད་དེ། དེ་མ་ཡིན་པ་དེ་ལས་གྲོལ་བ་སྟེ། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལས་གཞན་པ་ལ་མི་བསྒོའོ། །

[Block 280]
སྐད་ཅིག་མ་ལ་སོགས་པ་དེ་དག་ཐམས་ཅད་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལ་ཡོད་ཀྱི། དེ་ནི་སྐད་ཅིག་མ་ཉིད་ཀྱི་འཇུག་པའི་རྣམ་པར་ཤེས་པ་དང་། གཉེན་པོ་སྐྱེས་པའི་བར་ལ་མི་འཇུག་པའམ། འཁོར་བ་ཇི་སྲིད་པའི་བར་དུ་དགེ་བ་ལ་སོགས་པ་ངེས་པའི་རྒྱུར་གྱུར་པའི་ཕྱིར་བསོད་ནམས་དང་བསོད་ནམས་མ་ཡིན་པ་དང་མི་གཡོ་བ་འདུ་བྱེད་པའི་རྐྱེན་ལ་ལྟོས༌[^183]ནས་དགེ་བ་དང་མི་དགེ་བའི་འགྲོ་བར་རྣམ་པར་སྨིན་པ་ཉིད་ཡིན་གྱི་འཇུག་པའི་རྣམ་པར་ཤེས་པ་ལ་ནི་ཆོས་མི་མཐུན་པ་ཐམས་ཅད་ལ༌[^184]སྦྱར་བར་བྱའོ། །

[Block 281]
གང་ཡང་དེ་ལྟར་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཡོན་ཏན་དེ་དག་དང་ལྡན་པས་དེ་ན་བསྒོ་བར་བྱ་བ་ཡིན་གྱི། དྲུག་པོ་དག་ལ་ནི་མ་ཡིན་ཏེ། འབྲེལ་པ་མེད་པ་དང་། རྣམ་པར་ཤེས་པ་གཡོ་བ་ཉིད་ཀྱིས་སོ། །

[Block 282]
ཐ་དད་གསུམ་དང་འགལ་བའི་ཕྱིར། །ཞེས་བྱ་བ་ལ། རྟེན་གཞན་དང་གཞན་ལ་རེ་རེ་ཞིག །དམིགས་པ་གཞན་དང་གཞན་ལ། ཡིད་ལ་བྱེད་པ་གཞན་གྱི༌[^185]དོན་གཞན་ལ་རྣམ་པ་གཞན་གྱིས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 283]
སྐད་ཅིག་མ༌[^186]སྔ་མ་ལས་སྐད་ཅིག་ཕྱི་མ་འབྱུང་བར་འགྱུར་བས་ཞེས་བྱ་བ་དཔེས་བསྟན་པ་དེ་དགག་པར་བྱ་བའི་ཕྱིར། སྐད་ཅིག་ལྷན་ཅིག་མེད་པའི་ཕྱིར། །ཞེས་པ་སྟེ། སྐད་ཅིག་དག་གཅིག་ཏུ་ཡོད་པ་མེད་དེ། གང་ལྷན་ཅིག་འབྱུང་བ་དང་འགག་པ་ཡོད་ན་ནི་བག་ཆགས་ཀྱི་གནས་སུ་འགྱུར་རོ། །

[Block 284]
གལ་ཏེ་རིགས་མཐུན་པའི་རྣམ་པར་ཤེས་པ་དེ་དང་མཐུན་པའི་རིགས་གང་ཡིན་པ་ལ་འབྲེལ་པ་མེད་ཀྱང་སྒོ་བར་བྱེད་དེ་ཞེས་འདོད་ན། རིགས་ལ་བྱ་ན་གཞན་དུ་ཐལ་ཏེ།[^187] རིགས་གཞན་ལ་ཡང་ཐལ་བར་འགྱུར་ཏེ། མིག་ལ་སོགས་པ་རྣམས་གཟུགས་དང་བ་ཉིད་དུ་རིགས་མཐུན་པས་དེ་དག་ཀྱང་ཕན་ཚུན་བསྒོ་བར་ཐལ་བར་འགྱུར་རོ། །

[Block 285 [HEADING]]
#### ས་བོན་གཉིས་པོ་ཕྱི་དང་ནང་གི་སྐྱེད་པ་དང་འཕེན་པ། ^1-4-7-0
--- END BLOCKS ---
