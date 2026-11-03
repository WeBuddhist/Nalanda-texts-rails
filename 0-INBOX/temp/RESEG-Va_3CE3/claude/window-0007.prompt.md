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
རྣམ་པར་དག་པའི་རྒྱུར་མངོན་པར་འདུ་བྱེད་པ་མེད་པའི་ཕྱིར། མངོན་པར་འདུ་བྱ་བ་མེད་པའོ། །

[Block 247 [HEADING]]
#### ཐེག་པ་གང་དུ་གནས་པ། ^1-1-4-0

[Block 248]
ད་ནི་ཐེག་པ་གང་དུ་གནས་པར་འགྱུར་ཞེས་བྱ་བ་ནི༌[^178]ཞུས་པ་བཞི་པ༌[^179]བརྩམས་ཏེ། རབ་འབྱོར་ཐེག་པ་དེ་ནི་གང་དུ་ཡང་གནས་པར་འགྱུར་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ནམ་མཁའ་གང་ན་ཡང་མི་གནས་པ་དེ་བཞིན་དུ་ཐེག་པ་ཆེན་པོ་ཡང་མཐར་ཕྱིན་ཅིང་ཆོས་ཀྱི་སྐུའི་བདག་ཉིད་ཡིན་པས་གང་དུ་ཡང་གནས་པར་མི་འགྱུར་རོ། །

[Block 249]
[^180]ཐེག་པ་ཆེན་པོ་འབའ་ཞིག་གནས་པར་མི་འགྱུར་བར་མ་ཟད་ཀྱི། ཀུན་བརྟགས་པ་དང་། ཡོངས་སུ་གྲུབ་པའི་ཆོས་ཐམས་ཅད་ཀྱང༌[^181]གང་ན་ཡང་མི་གནས་སོ་ཞེས་བྱ་བར་སྟོན་ཏོ། །

[Block 250]
ཆོས་ཐམས་ཅད་གནས་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ། ཀུན་བརྟགས་པ་ནི་མེད་པའི་ཕྱིར་གང་ན་ཡང་མི་གནས་སོ། །

[Block 251]
ཡོངས་སུ་གྲུབ་པ་ནི་གཞི་དང་བརྟེན་པ་མེད་པའི་ཕྱིར་གང་ན་ཡང་མི་གནས་སོ། །

[Block 252]
འོན་ཀྱང་ཐེག་པ་ཆེན་པོ་དེ་ནི་མི་གནས་པའི་ཚུལ་གྱིས་གནས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་གནས་པ་མེད་པ་ཉིད་དེའི་གནས་པ་ཡིན་པར་ཐ་སྙད་གདགས་པར་བསྟན་པའོ། །

[Block 253]
དེ་བས་ན་དེ་བཞིན་ཉིད་ནི་གནས་པ་ཡང་མ་ཡིན་མི་གནས་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་གསུངས་ཏེ། དོན་དམ་པར་བརྟེན་པའི་མཚན་ཉིད་མེད་པའི་ཕྱིར་གནས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 254]
མི་གནས་པའི་མཚན་ཉིད་དུ་གནས་པའི་ཕྱིར་ཐ་སྙད་དུ་མི་གནས་པ་ཡང༌[^182]མ་ཡིན་ནོ། །

[Block 255]
དེ་བཞིན་དུ་གནས་པ་དང་། མི་གནས་པའི་མཚན་ཉིད་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 256]
མི་གནས་པར་གནས་པའི་ཚུལ་དང་། བསྐྱོད་དུ་མེད་པའི་ཚུལ་གྱིས་གང་དུ༌[^183]ཡང་གནས་པར་འགྱུར་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་རྟེན་གྱི་དངོས་པོར་གང་དུ་ཡང་གནས་པར་འགྱུར་བ་མེད་དེ། དེ་བས་ན་མི་གནས་པ་ཞེས་བྱའོ། །

[Block 257]
མི་གནས་པའི་མཚན་ཉིད་ཀྱིས་གནས་པ་དང་། བརྟན་པ་དང་། ཕྱིན་ཅི་ལོག་མེད་པའི་ཕྱིར་གནས་པ་ཞེས་བྱའོ། །

[Block 258 [HEADING]]
#### སུ་ཞིག་ངེས་པར་འབྱུང་བ། ^1-1-5-0

[Block 259]
དེས་སུ་ཞིག་ངེས་པར་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བ་ནི་ཞུས་པ་ལྔ་པ་སྟེ། ཐེག་པ་དེ་གང་ཡིན་པ་དང་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཆེན་པོའོ། །

[Block 260]
[^184]གང་ངེས་པར་འབྱུང་བར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་གང་ཟག་གོ། །

[Block 261]
གང་གིས་ངེས་པར་འབྱུང་བར་འགྱུར༌[^185]ཞེས་བྱ་བ་ནི་ལམ་གྱི་ཆོས་གང་གིས་ཞེས་བྱ་བ་སྟེ། རྒྱུ་གང་གིས་ངེས་པར་འབྱུང་བར་འགྱུར༌[^186]བའོ། །

[Block 262]
གང་ནས་ངེས་པར༌[^187]འབྱུང་བར༌[^188]འགྱུར་བ་ཞེས་བྱ་བ་ནི་སྲིད་པ་ལས་སོ། །

[Block 263]
ཤིན་ཏུ་རྣམ་པར་དག་པའི་ཕྱིར་བདག་མི་དམིགས་སོ༌[^189]ཞེས་བྱ་བ་ནི་གལ་ཏེ་བདག་ལ་སོགས་པ་དང་། གཟུགས་ལ་སོགས་པ་ཡོངས་སུ་ཟིན་ན། ཡོངས་སུ་གྲུབ་པ་ཤིན་ཏུ་རྣམ་པར་དག་པ་གང་ཡིན་པ་དེ་ཉམས་པར་འགྱུར་རོ་ཞེས་སྟོན་ཏོ། །

[Block 264]
བཅོམ་ལྡན་འདས་གང་མི་དམིགས་པས་ཆོས་འདི་དག་ཐམས་ཅད་དམིགས་སུ་མ་མཆིས་པ་ལགས་ཞེས་བྱ་བ་ནི་མི་དམིགས་པ་སྔར་སྨོས་པ་ཐམས་ཅད་ཀྱི་གཏན་ཚིགས་ཞུས་པའོ། །

[Block 265]
དེ་ལ་འགྲེས་གསུམ་སྟེ། ཐོག་མར་དེ་བཞིན་ཉིད་ལ་སོགས་པ་མི་དམིགས་པ་ནི་ཆེས་དེ་དག༌[^190]དམིགས་སུ་མེད༌[^191]པའི་གཏན་ཚིགས་ཀྱི་འགྲེས་དང་པོའོ། །

[Block 266]
དེའི་འོག་ཏུ་དེ་བཞིན་ཉིད་ལ་སོགས་པ་ཅིའི་ཕྱིར་མི་དམིགས་སྙམ་དུ་ཐེ་ཚོམ་དུ་གྱུར་པ་དང་། དེ་བཞིན་ཉིད་ལ་སོགས་པ་དེ་དག་གི་རང་གི་མཚན་ཉིད་མི་དམིགས་པས། དམིགས་སུ་མེད་དོ་ཞེས་བྱ་བ་ནི་འགྲེས་གཉིས་པའོ། །

[Block 267]
དེ་ནས་སྟོང་པ་ཉིད་ཐམས་ཅད་དང་། ས་ལ་སོགས་པའི་ཆོས་རྣམས་མི་དམིགས་པ་ཞེས་བྱ་བ་ནི་འགྲེས་གསུམ་པའོ། །

[Block 268]
དཀར་པོ་རྣམ་པར་མཐོང་བའི་ས་ཞེས་བྱ་བ་ནི་ལྷག་མཐོང་གི་གནས་སྐབས་འབའ་ཞིག་ལ་བྱ་སྟེ། མོས་པ༌[^192]སྤྱོད་པའི་ས་ལའོ། །

[Block 269]
རིགས་ཀྱི་ས་ཞེས་བྱ་བ་ནི་རིགས་ཀྱི་གནས་སྐབས༌[^193]ལ་ས་ཞེས་བྱ་སྟེ། རིགས་ཀྱི་ས་ཞེས་བྱ་བ་ནི༌[^194]ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པའི་དགེ་བའི་རྩ་བའི་གནས་སྐབས་མ་ལུས་པར་བསྟན་ཏོ། །

[Block 270 [HEADING]]
#### ཐེག་པ་ཆེན་པོའི་ངེས་པའི་ཚིག། ^1-1-6-0

[Block 271]
བཅོམ་ལྡན་འདས་ཐེག་པ་ཆེན་པོ་ཞེས་བགྱི་བ་འདི་ནི༌[^195]ཞེས་བྱ་བ་ཐེག་པ་ཆེན་པོ་ནི་སྔར་བཤད་ཟིན་པ་སྙམ་ན༌[^196]སྐབས་གང་ཡིན་ཞེ་ན། དེ་ཡང་བདེན་མོད་ཀྱི།

[Block 272]
སྔར་ནི་ཐེག་པ་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པའི་སྒྲ་བཤད་པ་ལས།

[Block 273]
འཇུག་པའི་སྐབས་སུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་གཟུངས་ཀྱི་སྒོའི་མཐའ་ལ་ཐུག་གི་བར་དུ་སྒྲུབ་པའི་ཆོས་རྣམས་ཐེག་པ་ཆེན་པོ་ཡིན་པར་བསྟན་ཏོ། །

[Block 274]
ད༌[^197]ནི་ཐེག་པ་དེ་གང་ནས་ངེས་པར་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པ་ངེས་པར་འབྱུང་བའི་གནས༌[^198]སྐབས་ནས་འབྲས་བུའི་ཐེག་པ་ཆེན་པོ་སངས་རྒྱས་ཉིད་དུ༌[^199]བསྟན་ཏོ། །

[Block 275]
དེ་བས་ན་ད་ནི་འབྲས་བུའི་ཐེག་པ་ཆེན་པོ་འདི་ལ། ཐེག་པ་ཆེན་པོའི་ངེས་པའི་ཚིག་དང་། ཐེག་པ་ཆེན་པོའི་ཆོས་རྣམས་ཡང་བསྟན་པར་བྱ་སྟེ། འདི་ནི་གནས༌[^200]སྐབས་སོ། །

[Block 276]
ལྷ་དང་མི་དང་། ལྷ་མ་ཡིན་དུ་བཅས་པའི་འཇིག་རྟེན་ཟིལ་གྱིས་མནན་ནས་ངེས་པར་འབྱུང་བར་འགྱུར་ཏེ། དེའི་སླད་དུ་ཐེག་པ་ཆེན་པོ་ཞེས་བགྱིའོ་ཞེས་བྱ་བ་ལ། འགྲོ་བ་ནི་འདིར་ཐེག་པ་ཆེན་པོ༌[^201]ཞེས་བྱའོ། །

[Block 277]
ངེས་པར་འབྱུང་བ་ཆེ་བ་གང་ཡིན་པ་དེ་ཐེག་པ་ཆེན་པོའོ། །

[Block 278]
གང་གི་ཕྱིར་འཇིག་རྟེན་གསུམ་པོ་ཟིལ་གྱིས་མནན་ཏེ་ཐམས་ཅད་ལས་ངེས་པར་འབྱུང་བ་དེའི་ཕྱིར། འདིའི་ངེས་པར་འབྱུང་བ་ཆེ་བས་ཐེག་པ་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 279]
ཐེག་པ་ཆེན་པོ༌[^202]དེ་ནི་ནམ་མཁའ་དང་མཉམ་པ་སྟེ་ཞེས་བྱ་བས་ནི་དེ་ཉིད་ཀྱི་ཆེ་བ་ཉིད་སྒྲུབ་སྟེ་སྐབས་འབྱེད་པ་ཆེ་བ་དང་། སྐྱེ་བ་དང་། འགག་པ་ལ་སོགས་པ་མེད་པ་དང་། དུས་ཀྱིས༌[^203]མ་བསྡུས་པ་དང་རྒྱུ༌[^204]རྣམ་པ་གསུམ་གྱིས་ནམ་མཁའ་དང་འདྲ་བར་བསྟན་ཏོ། །

[Block 280]
དཔེར་ན་ནམ་མཁའ་ལ་སེམས་ཅན་ཐམས་ཅད་སྐད་ཅིག་གཅིག་ལ་ཇི་ལྟར་འདོད་པའི་སྤྱོད་ལམ་ཐམས་ཅད་ཀྱིས༌[^205]གནས་ཀྱང་དོགས་པ༌[^206]མེད་པས་གོ་སྐབས་ཕྱེ་བ་དེ་བཞིན་དུ། ཐེག་པ་ཆེན་པོ་འདི་ལ་ཡང་སྐད་ཅིག་གཅིག༌[^207]ལ་སེམས་ཅན་ཐམས་ཅད་ཅིག་ཅར་ལྷག༌[^208]ནས་ཐམས་ཅད་ཤེས་པ་ཉིད་དང་། ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་དང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ལ་འཁོད་ནས་གནས་ཀྱང་གོ་སྐབས་ཡངས་པའི་ཕྱིར་གནོད་པ་ཅི་ཡང་མེད་དོ། །

[Block 281]
དཔེར་ན་ནམ་མཁའ་ནི་དུས་འདི་ལ་འོངས་སོ་བྱུང་ངོ་ཞེས་བྱ་བའམ། སོང་ངོ་འགགས་སོ་ཞེས་བྱ་བ་འམ། གནས་པའི་སྐད་ཅིག་གི་དབང་གིས༌[^209]གནས་སོ་ཞེས༌[^210]བྱ་བར་བརྗོད་དུ་མི་རུང་སྟེ། ཐེག་པ་ཆེན་པོ་ཡང་དེ་བཞིན་ནོ། །

[Block 282]
དཔེར་ན་ནམ་མཁའ་ནི་སྔོན་གྱི་དུས་དེ་ན་བྱུང་ངོ་། ། ཕྱི་མའི་དུས་དེ་ན་འབྱུང་བར་འགྱུར་རོ། །

[Block 283]
བར་གྱི་དུས་དེ་ན་ཡོད་དོ་ཞེས་བརྗོད་པར་མི་ནུས་ཏེ། ཐེག་པ་ཆེན་པོ་ཡང་དེ་བཞིན་ནོ་ཞེས་དེའི་རིམ་གྱིས་འགྲེས་གསུམ་གྱིས་བསྟན་ཏོ། །

[Block 284]
དེ་ནས་གནས་བརྟན་གྱིས་སྨྲས་པའི་འགྲེས༌[^211]ཉིད་ལ། བཅོམ་ལྡན་འདས་ཀྱིས་མངོན་པར་དགྱེས་པར་མཛད་ནས་སྔར་བཤད་པའི་རིམ་གྱིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པའི་ཆོས་རྣམས་རྣམ་པར་སྨིན་པའི་བདག་ཉིད་དུ་གྱུར་པ་ཆོས༌[^212]ཀྱི་སྐུས་བསྡུས་པ་དང་། ཐེག་པ་ཆེན་པོ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 285]
ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་སོགས་པས་དེ་ལྟར་ཐེག་པ་ཆེན་པོ་བསྟན་ནས་དེའི་འོག་ཏུ་གནས་བརྟན་གྱིས༌[^213]ལྷ་དང་། མི་དང་། ལྷ་མ་ཡིན་དུ་བཅས་པའི་འཇིག་རྟེན་ཟིལ་གྱིས་མནན་ནས། ཐེག་པ་དེ་ངེས་པར་འབྱུང་བར་འགྱུར་ཏེ་ཞེས་བྱ་བ་དང་། ཐེག་པ་དེ་ནམ་མཁའ་དང་མཉམ་པ་སྟེ་ཞེས་བྱ་བ་དང་། བཅོམ་ལྡན་འདས་འདི་ལྟ་སྟེ་དཔེར་ན་ནམ་མཁའ་ནི་སེམས་ཅན་གྲངས་མ་མཆིས་ཚད་མ་མཆིས། དཔག་ཏུ་མ་མཆིས་པ་རྣམས་ཀྱི་གོ་འབྱེད་དོ་ཞེས་བྱ་བ་དང་། འོང་བའམ། འགྲོ་བ་མི་དམིགས་ཞེས་བྱ་བ་དང་། སྔོན་གྱི་མཐའ་འམ། [^214]ཕྱི་མའི་མཐའ་མི་དམིགས་ཞེས་བྱ་བ་ཚིག་ལྔ་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས། རབ་འབྱོར་གང་ཡང་ཁྱོད་ཀྱིས་འདི་སྐད་དུ་ཐེག་པ་དེ་ནི་ལྷ་དང་མི་དང་། ལྷ་མ་ཡིན་དུ་བཅས་པའི་འཇིག་རྟེན་ཟིལ་གྱིས་མནན་ནས་ངེས་པར་འབྱུང་བར་འགྱུར་ཞེས་སྨྲས་པ་ནི་ཞེས༌[^215]བྱ་བ་ལ་སོགས་པས་ཚིག་དེ་དག་སོ་སོར་སྨོས་ཏེ། དེ་དག་རྒྱ་ཆེར་བསྟན་ཏོ། །
--- END BLOCKS ---
