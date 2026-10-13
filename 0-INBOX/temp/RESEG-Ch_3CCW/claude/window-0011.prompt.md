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
[Block 386]
བདག་གིས་སྟོང་པའི་ཕྱིར་བདག་མེད་པ་སྟེ། མི་རྟག་པ་ལ་སོགས་པས་དངོས་པོའི་རང༌[^264]གི་ངོ་བོ་བསྙད་དོ། །

[Block 387]
དེ་བས་ན་དངོས་པོ་འདི་དེ་ལྟར་མཐོང་བས་མཁས་པ་དེ་དག་གིས་དབེན་པར་མཐོང་ངོ་། །དབེན་ཞེས་བྱ་བ་ནི་སྟོང་པའོ། །

[Block 388]
དེ་ལྟར་ན་དབེན་པ༌[^265]མཐུན་པའི་ཕྱིར་སྐྱེ་བ་མེད་པའི་དགོན་པ་རྣམས་ལ་དབེན་པ་ཞེས་བྱ་སྟེ། དེ་བཞིན་དུ་འདིར་ཡང་རྣལ་འབྱོར་པས་དངོས་པོ་དབེན་པར་མཐོང་ཞེས་བྱ་བ་ནི་སྟོང་པར་མཐོང་བའི་བར་ལ་བྱའོ། །

[Block 389]
དེ་དག་དངོས་པོ་ཉིད་སྐུར་ཏེ་དབེན་པར་མཐོང་བ༌[^266]མ་ཡིན་གྱི། དངོས་པོ་སྟོང་པར་གྱུར་པ་ལ་སྟོང་པར་མཐོང་ངོ་། །སྟོང་པ་ཉིད་བསྟན་པའི་ཕྱིར་མི་རྟག་པ་ལ་སོགས་པ་བྱེ་བྲག་རྣམས་སྨོས་སོ། །

[Block 390]
ཡང་ན་དབེན་པ་ནི་དྲི་མ་མེད་པ་ཡིན་ན་འདི་ལྟར་སོ་སོའི་སྐྱེ་བོ་རྣམས་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པའི་དངོས་པོ་ཡང་རང་གི་རྟོག་པའི་དྲི་མས་སྦགས་པའི་ཕྱིར་ཕྱིན་ཅི་ལོག་ཏུ་ཁོང་དུ་ཆུད་ཀྱི་འཕགས་པ་རྣམས་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། དེ་དག་ནི་མེད་པ་ལ་སྒྲོ་མི་འདོགས་པར་དབེན་པར་དྲི་མ་མེད་པ་ཉིད་དུ་གཟིགས་སོ། །

[Block 391]
ཡང་ན་འཕགས་པ་རྣམས་དེ་ཁོ་ནའི་ཡེ་ཤེས་ལས་བཞེངས་ནས་དངོས་པོ་ལ་གཟིགས་ན་དབེན་པར་གཟིགས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 392]
འཕགས་པ་མཛད་པ་མཐར་ཕྱིན་པ་ཉི་ཚེས་འདི་ལྟར་གཟིགས་པར་ཡང་མ་ཟད་དེ། སློབ་དཔོན་ཡང་རང་གི་ཤེས་པ་ལ་བརྟེན་ནས། རིགས་པ༌[^267]དང་བཅས་པའི་ཆོས་ཉིད་རབ་ཏུ་རྟོགས་པས་ཆོས་ཉིད་ལ་གཅེས་པར་འཛིན་པ་ཡང་དག་པར་སྐྱེས་ཏེ།

[Block 393 [HEADING]]
### ཚིགས་བཅད་ཉེར་དྲུག་པ། ^1-27-0

[Block 394 [VERSE]]
རང་གིས་རིགས་པ་སྟོན་པ་ན། །
གནས་མེད་དམིགས་པ་ཡོད་མ་ཡིན། །
རྩ་བ་མེད་ཅིང་གནས་པ་མེད། །
མ་རིག་རྒྱུ་ལས༌[^268]ཤིན་ཏུ་བྱུང་། །

[Block 395 [VERSE]]
ཐོག་མ་དབུས་མཐའ་རྣམ་པར་སྤངས། །
ཆུ་ཤིང་བཞིན་དུ་སྙིང་པོ་མེད། །
དྲི་ཟའི་གྲོང་ཁྱེར་འདྲ་བ་སྟེ། །
རྨོངས་པའི་གྲོང་ཁྱེར་མི་བཟད༌[^269]པ། །
འགྲོ་བ་སྒྱུ་མ་བཞིན་དུ་སྣང་། །

[Block 396]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 397]
འདི་ལ་བརྟེན་པས་གནས་ཏེ།

[Block 398 [VERSE]]
[^270] ལོ་ཏོག་རྣམས་ཀྱི་རྒྱུར་གྱུར་པ། །
ས་གཞི་བཞིན་དུ་གཞི་བྱེད་པའོ། །
འདིའི་གནས་མེད་པས་གནས་མེད་པའོ། །

[Block 399]
བརྟེན་པར་བྱ་བས་དམིགས་པ་སྟེ། ལྡང་མི་ནུས་པ་རྣམས་ལྡང་བར་བྱེད་པའི་འཁོར་བ་བཞིན་ནོ། །

[Block 400]
འདིའི་དམིགས་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 401]
རྩ་བ་ནི་རྒྱུའི་གཙོ་བོ་སྟེ་དེ་ཡང་དེ་ལས་འབྱུང་བ་རྣམས་ཀྱི་སྐྱེ་བ་དང་། འདས་པ་དང་འཕེལ་བའི་རྒྱུ་སྟེ། དཔེར་ན། ཤིང་རྣམས་ཀྱི་རྩ་བ་ལྟ་བུའོ། །

[Block 402]
གནས་པ་ཡོད་པ་མ་ཡིན་པས་གནས་པ་མེད་པའོ། །

[Block 403]
གནས་པ་དང་དམིགས་པ་དང་སྐྱེ་བའི་རྒྱུ་དང་གནས་པ་མེད་པ་འདིས་འགྲོ་བ་མ་གྲུབ་པ་ཉིད་དུ་བརྗོད་དོ། །

[Block 404]
དེ་དག་ནི་དངོས་པོ་རྣམས་འགྲུབ་པའི་རྒྱུ་ཡིན་ན་དེ་དག་ཀྱང་འགྲོ་བ༌[^271]མེད་པས། དེའི་ཕྱིར་འགྲོ་བ་ནི་ལོག་པའོ། །

[Block 405]
དེ་ལ་གནས་ནི་སྐྱེ་མཆེད་དྲུག་གོ། །

[Block 406]
དམིགས་པ་ནི་ཆོས་ཐམས་ཅད་དེ་མཐུན་མཐུན༌[^272]དུ་སྦྱར་རོ། །

[Block 407]
རྩ་བ་ནི་ས་བོན་གྱི་ཆོས་ཀྱི་ཚུལ་གྱིས་རྒྱུའི་རྐྱེན་ཏོ། །

[Block 408]
འདིས་གནས་པར་བྱེད་པས་གནས་པ་སྟེ། དེས་སྐྱེས་པ་གནས་པའི་ཕྱིར་རོ། །

[Block 409]
དེ་དག་ཐམས་ཅད་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བས་ངོ་བོ་ཉིད་མེད་དེ།

[Block 410 [VERSE]]
དེ་དང་དེ་བརྟེན་གང་བྱུང་བ། །
རང་གི་དངོས་པོར་དེ་མ་སྐྱེས། །

[Block 411]
ཞེས་གོང་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 412]
དེའི་ཕྱིར་གནས་ལ་སོགས་པ་དང་བྲལ་བའི་འགྲོ་བ་ནི་ཡོད་པར་མི་རུང་ངོ་། །གལ་ཏེ་དེ་ལྟར་འགྲོ་བ་མེད་ན་ཇི་ལྟར་དེའི་རང་གི་ངོ་བོ་རྣམ་པ་སྣ་ཚོགས་སུ་དམིགས་ཞེ་ན། [^273]འཕགས་པ་རྣམས་ནི་འགྲོ་བ་རྣམ་པ་སྣ་ཚོགས་སུ་མི་དམིགས་ཏེ། དེ་དག་ལ་འགྲོ་བ་སྟོང་པ་ཉིད་དུ་རོ་གཅིག་པས་སྟོང་པ་ཉིད་ལ་རྣམ་པ་སྣ་ཚོགས་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 413]
དེ་བས་ན་བྱིས་པ་མ་རིག་པའི་གཉིད་ཀྱིས་ལོག་པ་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་དག་ནི་མ་སད་དེ་རྨི་ལམ་རྨི་བ་བཞིན་དུ་སྣ་ཚོགས་སུ་དམིགས་པར་བསྟན་པའི་ཕྱིར། མ་རིག་རྒྱུ་ལས་ཤིན་ཏུ་བྱུང་། །ཞེས་བྱ་བ་སྨོས་ཏེ། ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་མེད་པ་དང་། མ་རིག་པ་ཡོད་པས་འགྲོ་བ་ངོ་བོ་ཉིད་ཀྱིས་མ་གྲུབ་སྟེ། མ་རིག་པའི་ས་བོན་གྱི་རྒྱུ་ལས་གྱུར་པ༌[^274]ངེས་སོ། །

[Block 414]
ཇི་ལྟར་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་མེད་པ་དེ་ལྟར་བསྟན་པའི་ཕྱིར། ཐོག་མ་དབུས་མཐའ་རྣམ་པར་སྤངས། །ཞེས་བྱ་བ་སྟོན་ཏེ་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དང་བྲལ་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 415 [HEADING]]
### ཚིགས་བཅད་ཉེར་བདུན་པ། ^1-28-0

[Block 416]
འདིའི་ཕྱིར་ཡང་མ་རིག་པའི་ས་བོན་ལས་བྱུང་བ་སྟེ། འདི་ལྟར་ཆུ་ཤིང་བཞིན་དུ་སྙིང་པོ་མེད་པའོ། །

[Block 417]
གལ་ཏེ་མ་རིག་པའི་ས་བོན་ལས་བྱུང་བ་མ་ཡིན་ན། དེའི་ཚེ་བརྟགས་ན་སྙིང་པོ་དམིགས་པར་འགྱུར་བའི་རིགས་ན༌[^275]འདུས་བྱས་ནི་བརྟགས་ན་ཆུ་ཤིང་གི་ཕུང་པོ་བཞིན་དུ་སྙིང་པོ་མེད་དོ། །

[Block 418]
གང་སྙིང་པོ་མེད་ཀྱང་སྙིང་པོ་ཅན་དུ་སྣང་བ་དེ་གཏི་མུག་གི་མཐུ་ལས་བྱུང་བ་སྟེ། དེ་ལྟར་ན་འགྲོ་བ་ནི་མ་རིག་པའི་ས་བོན་ལས་བྱུང་བའོ། །

[Block 419]
འདིའི་ཕྱིར་ཡང་མ་རིག་པའི་ས་བོན་ལས་བྱུང་བ་སྟེ། འདི་ལྟར་དྲི་ཟའི་གྲོང་ཁྱེར་ལྟ་བུ་ཡིན་པའི་ཕྱིར་ཏེ། འདི་ལྟར་དྲི་ཟའི་གྲོང་ཁྱེར་ཡང་དག་པ་བཞིན་དུ་སྣང་ཡང་བརྟགས་ན་དེ་བཞིན་མ་ཡིན་པས་གྲོང་ཁྱེར་ཡང་དག་པ་མ་ཡིན་ནོ། །

[Block 420]
གང་གི་ཕྱིར་དེ་ལྟར་བརྟགས་ན་མ་རིག་པའི་ས་བོན་གྱི་རྒྱུ་ལས་བྱུང་བའི་འགྲོ་བ་ངོ་བོ་ཉིད་ཀྱིས་མ་གྲུབ་པ་དེའི་ཕྱིར་འདི་ནི་ངེས་པར་རྨོངས་པའི་གྲོང་ཁྱེར་མི་བཟད་པ། འགྲོ་བ་སྒྱུ་མ་བཞིན་དུ་སྣང་། །གནོད་པར་བྱེད་པ་བཟློག་པར་དཀའ་བ་དང་། མུན་པས་བསྒྲིབས་པས་རང་གི་ངོ་བོ་རྟོགས་པར་དཀའ་བའི་ཕྱིར། འགྲོ་བ་མི་བཟད་པ་ཞེས་བྱ་བ༌[^276]སྟེ། མ་རུངས་པ༌[^277]དང་དབུགས་འབྱིན་པ་མེད་པའི་གནས་དང་འཇིགས་པར་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 421]
དེའི་ཕྱིར་འདི་ནི་ཕྱིན་ཅི་མ་ལོག་པ་རྣམས་ཀྱིས༌[^278]སྒྱུ་མ་བཞིན་དུ་གཟིགས་སོ། །

[Block 422]
བྱིས་པ་རྣམས་ཀྱི་རྨོངས་པའི་གྲོང་ཁྱེར་གང་ཡིན་པ་དེ་འཕགས་པ་རྣམས་ཀྱིས་སྒྱུ་མ་བཞིན་དུ་གཟིགས་ཏེ། མ་རིག་པའི་མུན་པ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 423]
འདིའི་ཕྱིར་ཡང་འདི་ལྟར་འགྲོ་བ་དེ་དངོས་པོ་མེད་དེ་འདི་ལྟར།

[Block 424 [HEADING]]
### ཚིགས་བཅད་ཉེར་བརྒྱད་པ། ^1-29-0

[Block 425 [VERSE]]
ཚངས་པ༌[^279]ལ་སོགས༌[^280]འཇིག་རྟེན་འདི། །
བདེན་པར༌[^281]རབ་ཏུ་གང་བརྗོད་པ། །
འཕགས་ལ་དེ་ཡང་བརྫུན་ཞེས་གསུངས། །
དེ་ལས་གཞན་ན༌[^282]ཅི་ཞིག་ལུས། །
--- END BLOCKS ---
