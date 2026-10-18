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

[Block 286]
གང་ཡང་སྔར་བསྟན་པའི་ས་བོན་གཉིས་པོ་ཕྱི་དང་ནང་གི་སྐྱེད་པ་དང་ནི་འཕེན་པར་འདོད་ཅེས་བྱ་བ་ལས།

[Block 287]
དེ་ལ་སྐྱེད་པར་བྱེད་པའི་ས་བོན་ནི༌[^188]ཕྱི་རོལ་གྱི་འབྲས་བུ་སྨིན་པར་འགྱུར༌[^189]གྱི་བར་དུའོ། །

[Block 288]
ནང་གི་ས་བོན་ནི་མཐར་ཐུག་པའི་བར་དུ་སྐྱེད་པར་བྱེད་པ་ཉིད་དོ། །

[Block 289]
འཕེན་པར་བྱེད་པ་མ་བཏབ་པ་ནི་ཕྱི་རོལ་གྱིའོ། །

[Block 290]
ཤི་བ་ནི་ནང་གི་སྟེ། ལུས་ནི༌[^190]འདི་ཕྱིས་ཀྱང་མི་འགྱེས་པར་འཕངས་ནས་གནས་སོ། །

[Block 291]
གལ་ཏེ་སྐྱེ་བའི་ས་བོན་གྱི་རྒྱུ་ཅན་ཡིན་ན། གང་གིས་ན་དེ་ཉམས་པར་མི་འགྱུར་ཏེ། དུས་ཕྱིས་ཅུང་ཟད་ཙམ་ཡང་རྗེས་སུ་འཇུག་པར་མི་འགྱུར་རོ། །

[Block 292]
གལ་ཏེ་སྐད་ཅིག་མ་གཅིག་ནས་གཅིག་ཏུ་འཇུག་པར་འགྱུར་ན། སྐད་ཅིག་སྔ་མ་སྐད་ཅིག་ཕྱི་མའི་རྒྱུར་གྱུར༌[^191]ན་ནི་དེས་ན་ནམ་ཡང་ཉམས་པར་མི་འགྱུར་བས་དེ་བས་ན༌[^192]ངེས་པར་འཕེན་པའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་ནོ། །

[Block 293]
ས་བོན་དེ་དག་ཀྱང་མདའ་སྟོང༌[^193]སྦྱོར་བ་དང་འདོམ་རྫོགས་པ་གཉིས་མདའ་འགྲོ་བ་དང་ཕོག་པ་གཉིས་ཀྱི་རྒྱུར་འགྱུར་བ་བཞིན་ནོ། །

[Block 294 [HEADING]]
#### འཇུག་པའི་རྣམ་པར་ཤེས་པ་ཉེ་བར་སྤྱོད་པ་ཅན། ^1-4-8-0

[Block 295]
ཡང་འཇུག་པའི་རྣམ་པར་ཤེས་པ་གཞན་གང་ཡིན་པ་དེ༌[^194]ནི་ལུས་དང་འགྲོ་བ་ཐམས་ཅད་དུ་ཉེ་བར་སྤྱོད་པ་ཅན་དུ་བལྟ་བར་བྱ་སྟེ་ཞེས་བྱ་བ་ལ། འདི་ལྟར་དེ་ལ་ཉེ་བར་སྤྱོད་པ་འབྱུང་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏེ། ཉེ་བར་སྤྱོད་པའི་ངོ་བོ༌[^195]ནི་ཉེ་བར་སྤྱོད་པ་ཅན་ཞེས་བྱས་ནས་སོ། །

[Block 296]
དོན་དེ་ཉིད་དབུས་དང་མཐའ་རྣམ་པར་འབྱེད་པའི་ཚིགས་སུ་བཅད་པ་དང་མངོན་པའི་ལུང་གིས་བསྟན་ཏེ།

[Block 297]
རྣམ་པར་ཤེས་པ་དེ་དག་ཉིད་གཅིག་གི་རྐྱེན་གཅིག་ཡིན་པ་ཉིད་ཀྱི་ལུང་ནི་ཆོས་མངོན་པའི་མདོ་ལས།

[Block 298]
ཆོས་ཀུན་རྣམ་པར་ཤེས་ལ་སྦྱོར། །ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་སྟེ། ཕན་ཚུན་རྒྱུའི་དངོས་པོ་དང་ཞེས་བྱ་བ་ལ་རྩ་བའི་རྣམ་པར་ཤེས་པ་ལས་དེ་དག་འབྱུང་བའི་ཕྱིར་རྒྱུའོ། །

[Block 299]
འབྲས་བུའི་དངོས་པོར་རྟག་ཏུ་སྦྱོར། །ཞེས་བྱ་བ་ལ་གང་གི་ཚེ་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་རྒྱུ་ཡིན་པ་ན་དེའི་ཚེ་དེ་འབྲས་བུ་ཡིན་ལ། གང་གི་ཚེ་དེ་རྒྱུ་ཡིན་པ་ན་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་འབྲས་བུ་ཡིན་ནོ། །

[Block 300]
དེ་དག་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྣམ་པ་གསུམ་མོ། །

[Block 301]
འཁོར་བ་དང་། འདོད་པ་དང་། མི་འདོད་པའི་འགྲོ་བ་དང་། ཉེ་བར་སྤྱོད་པ་ཅན་ལ་རྐྱེན་རྣམ་པ་བཞིར་འགྱུར་ཏེ། དེ་ལ་དང་པོ་ལ་ནི་རྒྱུའི་རྐྱེན་ཏེ། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལ་གནས་པའི་ཆོས་རྣམས་ཀྱི་བག་ཆགས་སོ། །

[Block 302]
གཉིས་པ་ལ་ནི་བདག་པོའི་རྐྱེན་ཏེ། མ་རིག་པ་ལ་སོགས་པའི་དབང་གིས་འདུ་བྱེད་རྣམས་འབྱུང་ངོ་། །ཡང་ཉེ་བར་སྤྱོད་པ་ཅན་གྱི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་བརྗོད་ལ། རྣམ་པར་ཤེས་པ་དྲུག་པོ་རྣམས་ཀྱི་ནི་རྐྱེན་གསུམ་དུ་འགྱུར་ཏེ། [^196]དེ་ལ་མིག་གི་རྣམ་པར་ཤེས་པའི་བདག་པོའི་རྐྱེན་ནི་མིག་གོ། །

[Block 303]
དམིགས་པའི་རྐྱེན་ནི་གཟུགས་སོ། །

[Block 304]
མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ནི་གང་གི་དེ་མ་ཐག་ཏུ་རྣམ་པར་ཤེས་པ་གང་འབྱུང་བ་སྟེ། གང་གི་ཕྱིར་གལ་ཏེ་དེས་སྐབས་མ་བྱིན་ན་གང་ཡང་འབྱུང་བར་མི་འགྱུར་བས་སོ། །

[Block 305]
དེ་བཞིན་དུ་རྣམ་པར་ཤེས་པ་ལྷག་མ་རྣམས་ལ་ཡང་ངོ་། །

[Block 306 [HEADING]]
### རིག་པས་ངེས་པར་བསྟན་པ། ^1-5-0

[Block 307 [HEADING]]
#### ཀུན་ནས་ཉོན་མོངས་པ། ^1-5-1-0

[Block 308 [HEADING]]
##### ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པ། ^1-5-1-1-0

[Block 309]
དེ་ལྟར་ཀུན་གཞི་རྣམ་པར་ཤེས་པའི་རྣམ་གྲངས་གཞན་བསྟན་ནས། ད་ནི་མཚན་ཉིད་རྣམ་པར་གཞག་པར་བྱ་སྟེ། ཇི་ལྟར་གཉི་ག་ཡང་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལ་རུང་གི །གཞན་དུ་མ་ཡིན་པ༌[^197]དེ་ལྟར་རིག་པས༌[^198]ངེས་པར་བསྟན་པར་བྱ་སྟེ། དེ་ཡང་འདི་ལྟར་མིག་གི་རྣམ་པར་ཤེས་པ་གང་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པ་དང་། ཉེ་བའི་ཉོན་མོངས་པ་གང་དག་དང་ལྷན་ཅིག་སྐྱེས་ཤིང་འགགས་པ༌[^199]དེ་ཉིད་ལ་དེ་དག་གི་ས་བོན་གྱི་དངོས་པོར་བག་ཆགས་བསྒོས་པར་འགྱུར་གྱི་གཞན་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་དེ་ལ་དེ་ཉིད་ལ་ཞེས་བྱ་བ་ནི་མིག་གི་རྣམ་པར་ཤེས་པ་ལའོ། །

[Block 310]
དེ་དག་གི་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་ལ་སོགས་པ་དག་གིའོ། །

[Block 311]
ས་བོན་གྱི་དངོས་པོར་ཞེས་བྱ་བ་ནི་རྒྱུའི་དངོས་པོར་རོ། །

[Block 312]
གཞན་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བ་ནི་རྣ་བའི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 313]
རྣམ་པར་ཤེས་པ་གཞན་གྱིས་བར་དུ་ཆོད་པ་ཞེས་བྱ་བ་ནི་རྣ་བའི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པས་བར་དུ་ཆོད་པའོ། །

[Block 314]
བག་ཆགས་ཞེས་བྱ་བ༌[^200]ནི་འདོད་ཆགས་ལ་སོགས་པའི་བག་ཆགས་སོ། །

[Block 315]
བག་ཆགས་ཀྱི་གནས་ཞེས་བྱ་བ་ནི་མིག་གི་རྣམ་པར་ཤེས་པའོ། །

[Block 316]
འདོད་ཆགས་ལ་སོགས་པ་དང་བཅས་པར་འབྱུང་དུ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས༌[^201]པ་དང་བཅས་པར་འབྱུང་བའོ། །

[Block 317]
དེ་ལྟ་བས་ན་འདས་པའི་རྒྱུ་ལས་ནི་མི་རུང་སྟེ། འདི་ལྟར་འདས་པའི་དུས༌[^202]ལས་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་འབྱུང་བ་ཇི་ལྟར་མི་རུང་བ་བཞིན་དུ་དེའི་ཡང་མི་རུང་ངོ་། །གལ་ཏེ་བྱེ་བྲག་ཏུ་སྨྲ་བ་འདས་པ་ཡོད་པ་ཉིད་དུ་འདོད་པས་དེའི་ཕྱིར་འདས་པ་ལས་འབྱུང་ངོ་ཞེ་ན། དེ་དག་གི༌[^203]འདས་པ་ཞེས་བྱ་བ་ནི་བརྗོད་པས་བརྗོད་པར་བྱ་བ་ཉིད་དུ་མི་འགྲུབ་པས་དེ་ནས༌[^204]འདས་པ་ཞེས་བྱ་བ་འདི་གང་ཡིན། ཆོས་གང་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་སྐྱེས་པ་ཡོད་པ་དེ་ནི་བག་ཆགས་མེད་པས་མ་ཡིན་ནོ། །

[Block 318]
མིག་གི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ལ། [^205]རེ་ཞིག་མིག་གི་རྣམ་པར་ཤེས་པ་འདོད་ཆགས་ལ་སོགས་པ་དང་ལྷན་ཅིག་འབྱུང་བ་དེ་ལ་ཡང་བག་ཆགས་མི་རུང་སྟེ། མིག་གི་རྣམ་པར་ཤེས་པ༌[^206]ལས་སྐྱེས་པ་དེ་ལ་བག་ཆགས་ཇི་ལྟར་རིགས། རེ་ཞིག་འདོད་ཆགས་ལ་ནི་མ་ཡིན་ཏེ། འདོད་ཆགས་ལ་མིག་གི་རྣམ་པར་ཤེས་པའི་བག་ཆགས་ནི༌[^207]མི་རིགས་ཏེ། གང་གི་ཕྱིར་འདོད་ཆགས་ནི་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་བརྟེན་པའི་ཕྱིར་དང་། མི་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 319]
རྣམ་པར་ཤེས་པ་གཞན་དག་ལ་ཡང་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནི་རྣ་བའི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ༌[^208]ལ་སྟེ། གང་གི་ཕྱིར་དེ་དག་ནི་གནས་ཐ་དད་པའི་ཕྱིར་དང་། གནས་ཐ་དད་པ་ཉིད་ཡོད་ན་ལྷན་ཅིག་འབྱུང་བ་དང་འགག་པ་མེད་པའི༌[^209]ཕྱིར་རོ། །

[Block 320]
མིག་གི་རྣམ་པར་ཤེས་པའི་གནས་ནི་མིག །རྣ་བའི་རྣམ་པར་ཤེས་པའི་གནས༌[^210]ནི་རྣ་བའོ། །
--- END BLOCKS ---
