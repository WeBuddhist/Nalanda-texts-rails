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
[Block 3571]
དེ་དག་ཀྱང་འཛམ་བུའི་གླིང་འདི་ཉིད་ཀྱི་འོག་དམྱལ་བ་ཆེན་པོ་རྣམས་ཀྱི་ཐད་ཀ་ན་ཡོད་དོ། །

[Block 3572]
འཛམ་བུའི་གླིང་འདི་ཙམ་གྱི་འོག་ན་མནར་མེད་པ་ལ་སོགས་པའི་གོ་སྐབས་ག་ལ་ཡོད་ཅེ་ན། གླིང་རྣམས་ནི་འབྲུའི་ཕུང་པོ་བཞིན་དུ་ཞབས་རྒྱ་ཆེ་བ་ཡིན་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་རྒྱ་མཚོ་ཆེན་པོ་རིམ་གྱིས་གཞོལ་བ་ཡིན་ནོ། །

[Block 3573]
དེ་ལྟར་ན་སེམས་ཅན་དམྱལ་བ་བཅུ་དྲུག་པོ་དེ་རྣམས་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ལས་ཀྱི་དབང་གིས་མངོན་པར་གྲུབ་པ་དག་ཡིན་ནོ། །

[Block 3574 [HEADING]]
###### ཉི་ཚེ་བའི་དམྱལ་བ། ^3-2-1-9-5-0

[Block 3575]
ཉི་ཚེ་བའི་དམྱལ་བ་རྣམས་ནི་མང་པོའམ་གཉིས་སམ་གཅིག་གི་སོ་སོའི་ལས་དག་གིས་མངོན་པར་གྲུབ་པ་ཡིན་ཏེ། དེ་དག་གི་རྣམ་པའི་བྱེ་བྲག་ནི་རྣམ་པ་དུ་མ་ཡོད་དོ། །

[Block 3576]
གནས་ནི་ངེས་པ་མེད་དེ། ཆུ་བོ་དང་། རི་དང་། མྱ་ངམ་གྱི་ཕྱོགས་དག་དང་། གཞན་དག་དང་། འོག་ན་ཡང་ཡོད་པའི་ཕྱིར་རོ། །

[Block 3577]
རེ་ཞིག་འདི་ནི་དམྱལ་བའི་སྣོད་རྣམས་ཀྱི་གནས་པ་ཡིན་ནོ། །

[Block 3578 [HEADING]]
##### དུད་འགྲོ་དང་ཡི་དགས། ^3-2-1-10-0

[Block 3579]
དུད་འགྲོ་ནི་ཐང་དང་། ཆུ་དང་། ནམ་མཁའི་སྤྱོད་ཡུལ་པ་དག་ཡིན་ནོ། །

[Block 3580]
དེ་དག་གི་གནས་ཀྱི་རྩ་བ་ནི་རྒྱ་མཚོ་ཆེན་པོ་ཡིན་ཏེ། གཞན་ནི་དེ་དག་ལས་འཕྲོས་པ་དག་ཡིན་ནོ། །

[Block 3581]
ཡི་དགས་རྣམས་ཀྱི་རྒྱལ་པོ་ནི་གཤིན་རྗེ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 3582]
དེ་དག་གི་གནས་ཀྱི་རྩ་བ་རྒྱལ་པོའི་ཁབ་ནི་འཛམ་བུའི་གླིང་འདིའི༌[^2058]འོག་དཔག་ཚད་ལྔ་བརྒྱས་བཅད་པ་ན་ཡོད་དེ། གཞན་ནི་དེ་ལས་འཕྲོས་པ་དག་ཡིན་ནོ། །

[Block 3583]
དེ་ལས་ཡི་དགས་རྫུ་འཕྲུལ་ཆེན་པོ་ཁ་ཅིག་ནི་ལྷའི་དཔལ་ལྟ་བུ་ཡང་ཉམས་སུ་མྱོང་ངོ་། །ལྷག་མ་ནི་ཇི་ལྟར་ཡི་དགས་ཀྱི་རྟོགས་པ་བརྗོད་པ་དག་ལས་འབྱུང་བ་ཡིན་ནོ། །

[Block 3584 [HEADING]]
##### ཉི་མ་དང་ཟླ་བ། ^3-2-1-11-0

[Block 3585]
ཡང་ཉི་མ་དང་ཟླ་བ་འདི་དག་ཅི་ལ་བརྟེན་ཞེ་ན། རླུང་ལ་སྟེ། སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཐུན་མོང་གི་ལས་ཀྱི་དབང་གིས་བར་སྣང་ལ་ཉི་མ་དང་། ཟླ་བ་དང་། སྐར་མ་རྣམས་འཕུལ་བར༌[^2059]བྱེད་པའི་རླུང་དག་གྲུབ་སྟེ། རི་རབ་ལ་རླུང་གི་འཁོར་ལོ་བཞིན་དུ་འཁོར་རོ། །

[Block 3586]
ཉི་མ་དང་ཟླ་བ་དག་འདི་ནས་ཐག་ཇི་སྲིད་ཅེ་ན། ཉི་ཟླ་ལྷུན་པོའི་ཕྱེད་ནའོ། །

[Block 3587]
རི་གཉའ་ཤིང་འཛིན་གྱི་རྩེ་མོ་དང་མཉམ་པ་ནས་རྒྱུའོ། །

[Block 3588]
ཚད་ཇི་ཙམ་ཞེ་ན། གོ་རིམས་བཞིན་དུ། དཔག་ཚད་ལྔ་བཅུ་གཅིག་དང་བཅས། །ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་ཚད་ནི་དཔག་ཚད་ལྔ་བཅུའོ། །

[Block 3589]
ཉི་མའི་དཀྱིལ་འཁོར་གྱི་ནི་གཅིག་དང་བཅས་པའི་ལྔ་བཅུ་སྟེ། ལྔ་བཅུ་རྩ་གཅིག་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3590]
སྐར་མའི་གཞལ་ཡས་ཁང་རྣམས་ཀྱི་ནང་གི་ཚད་ཆུང་བ་དེའི་ནི་རྒྱང་གྲགས་གཅིག་གོ། །

[Block 3591]
སྲོག་ཆགས་རྣམས་ཀྱི་ལས་དག་གིས་ཉི་མའི་གཞལ་མེད་ཁང་འོག་གི་ཕྱི་རོལ་ནི་མེ་ཤེལ་གྱི་དཀྱིལ་འཁོར་ཚ་བར་བྱེད་པ་དང་། སྣང་བར་བྱེད་པ་མངོན་པར་གྲུབ་བོ། །

[Block 3592]
ཟླ་བའི་གཞལ་མེད་ཁང་གི་ནི་ཆུ་ཤེལ་བསིལ་བར་བྱེད་པ་དང་། སྣང་བར་བྱེད་པ་མངོན་པར་གྲུབ་སྟེ། ཅི་རིགས་པར་མིག་དང་། ལུས་དང་། འབྲས་བུ་དང་། མེ་ཏོག་དང་། ལོ་ཏོག་དང་། སྨན་རྣམས་ལ་ཕན་འདོགས་པར་བྱེད་པ་དང་། གནོད་པར༌[^2060]བྱེད་པ་དག་ཡིན་ནོ། །

[Block 3593]
གླིང་བཞི་པ་གཅིག་ཏུ་ནི་ཟླ་བ་གཅིག་ཁོ་ན་དང་། ཉི་མ་གཅིག་གིས་བྱ་བ་བྱེད་དོ། །

[Block 3594]
ཅི་གླིང་བཞི་པོ་དག་ཏུ་ཉི་མས་ཅིག་ཅར་བྱ་བ་བྱེད་དམ་ཞེ་ན། མ་ཡིན་ནོ། །

[Block 3595]
འོ་ན་ཅི་ཞེ་ན། དེ་དག་ཏུ།

[Block 3596 [VERSE]]
ནམ་ཕྱེད་ཉི་མ་ནུབ་པ་དང་། །
ཉི་མ་ཕྱེད་དང་འཆར་དུས་གཅིག །

[Block 3597]
གང་གི་ཚེ་བྱང་གི་སྒྲ་མི་སྙན་དུ་ནམ་ཕྱེད་པ་དེའི་ཚེ་ཤར་གྱི་ལུས་འཕགས་སུ་ནི་ཉི་མ་ནུབ་བོ། །

[Block 3598 [VERSE]]
འཛམ་བུའི་གླིང་དུ་ནི་ཉི་མ་ཕྱེད་དོ། །
བ་ལང་སྤྱོད་དུ་ནི་ཉི་མ་ཤར་ཏེ།
དེ་བཞིན་དུ་གཞན་དག་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 3599]
ཉི་མའི་འགྲོས་ཀྱི་བྱེ་བྲག་ལས་འདི་ན་ཉིན་མོ་དང་མཚན་མོ་རྣམས་རིང་ཐུང་དུ་འགྱུར་ཏེ། དེ་ལ།

[Block 3600 [VERSE]]
དབྱར་གྱི་ཟླ་བ་གཉིས་པ་ཡི། །
ཐ་མའི་ཚེས་དགུ་ནས་མཚན་རིང་། །

[Block 3601]
དབྱར་རྣམས་ཀྱི་ཟླ་བ་གཉིས་པ་དབྱར༌[^2061]ཟླ་ཐ་ཆུངས༌[^2062]ཡར་གྱི་ངོའི་ཚེས་དགུ་ནས་མཚན་མོ་རིང་ངོ་། །དགུན་རྣམས་ཀྱི་ནི་བཞི་པ་ལ། །ཐུང་ངུར༌[^2063]འགྱུར་རོ། །

[Block 3602]
དེ་བཞིན་དུ་དགུན་རྣམས་ཀྱི་ཟླ་བ་བཞི་པའི་ཐ་མའི་ཚེས་དགུ་ནས་ཐུང་ངུར༌[^2064]འགྱུར་ཞེས་བྱ་བར་སྦྱར་ཏེ། དགུན་ཟླ༌[^2065]ཐ་ཆུངས༌[^2066]ཡར་གྱི་ངོའི་ཚེས་དགུ་ནས་སོ། །

[Block 3603]
ཉིན་མོ་བཟློག །གང་གི་ཚེ་མཚན་མོ་རིང་བ་དེའི་ཚེ་ཉིན་མོ་ཐུང་བར་འགྱུར་རོ། །

[Block 3604]
གང་གི་ཚེ་མཚན་མོ་ཐུང་བ་དེའི་ཚེ་ཉིན་མོ་རིང་བར་འགྱུར་རོ། །ཇི་ཙམ་ཞིག་གིས་རིང་པོར་འགྱུར་ཞེ་ན། ཉིན་མཚན་མཚན༌[^2067]རིང་བ་ཐང་ཅིག་གོ། །

[Block 3605]
ཉིན་མོ་འམ་མཚན་མོ་ཐང་ཅིག་ཐང་ཅིག་གིས་རིང་བར་འགྱུར་རོ། །

[Block 3606]
རིང་བ་དེ་དག་ཀྱང་གོ་རིམས་བཞིན་དུ། ཉི་མ་ལྷོ་བྱང་འགྲོ་ཚེའོ། །

[Block 3607]
ཉི་མ་འཛམ་བུའི་གླིང་གི་ལྷོ་ཕྱོགས་ཀྱི་ངོས་སུ་འགྲོ་བ༌[^2068]མཚན་མོ་རིང་ངོ་། །བྱང་ཕྱོགས་སུ་འགྲོ་བ་ན་ཉིན་མོ་རིང་ངོ་། །ཟླ་བ་ཡར་གྱི་ངོའི་དང་པོའི་ཟླ་བའི་དཀྱིལ་འཁོར་མ་རངས་པར་སྣང་བ་དེ་ལ་རྒྱུ་ཅི་ཡོད་ཅེ་ན།

[Block 3608 [VERSE]]
ཉི་མ་དང་ནི་ཉེ་བ་ལས། །
རང་གི་གྲིབ་མས་འགྲིབ་པར་སྣང་། །

[Block 3609]
བཏགས་པ༌[^2069]ལས།

[Block 3610]
གང་གི་ཚེ་ཟླ་བའི་གཞལ་མེད་ཁང་ཉི་མའི་གཞལ་མེད་ཁང་དང་ཉེ་བར་རྒྱུ་བ་དེའི་ཚེ་ཉི་མའི་འོད་ཀྱིས་དེའི་གཞལ་མེད་ཁང་ལ་འབབ་སྟེ། དེས་ན་དེའི་ཕྱི་རོལ་གྱི་ངོས་སུ་གྲིབ་མ་བབ་པས་དཀྱིལ་འཁོར་མ་རངས་པར་སྣང་ངོ་ཞེས་བསྟན་ཏོ་ཞེས་གྲག་གོ།[^2070] །སྔོན་གྱི་སློབ་དཔོན་རྣམས་ན་རེ་གང་རེས་འགའ་གཞལ་མེད་ཁང་གི་ཕྱེད་སྣང་བ་དེ་ལྟ་བུ་དེ་ནི་རྒྱུ་བའི་ཚུལ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །
--- END BLOCKS ---
