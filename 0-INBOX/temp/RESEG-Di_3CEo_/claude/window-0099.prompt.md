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
[Block 3466]
ཡང་སྲིད་པའི་རྩེ་མོ་པའི་རྣམ་པ་དགུ་པར་བཤད་པ་གང་ཡིན་པ། དེ་ཟད་ཐོབ་དང་ཟག་པ་ཤེས། །

[Block 3467]
དང་པོ་ཉིད་དུ་ཟག་པ་ཐམས་ཅད་ཟད་པའི་ཐོབ་པ་དང་ལྷན་ཅིག་སྐྱེས་པའི་ཕྱིར་ཟད་པ་ཤེས་པ་ཡིན་ནོ། །

[Block 3468]
དེ་ཚེ་དེ་མི་སློབ་དགྲ་བཅོམ། །དགྲ་བཅོམ་པ་ཉིད་ལ་ཞུགས་པ་དེ་ཟད་པ་ཤེས་པ་སྐྱེས་ན་མི་སློབ་པ་དང་། དགྲ་བཅོམ་པའི་འབྲས་བུ་ཐོབ་པ་ཉིད་ཀྱི་ཕྱིར་དགྲ་བཅོམ་པའོ། །

[Block 3469]
འབྲས་བུ་གཞན་གྱི་ཕྱིར་བསླབ༌[^1364]པར་བྱ་བ་མེད་པའི་ཕྱིར་མི་སློབ༌[^1365]པའོ། །

[Block 3470 [HEADING]]
#### འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པས་འདོད་ཆགས་དང་བྲལ་བ། ^6-2-3-0

[Block 3471]
བསྒོམ་པའི་ལམ་འཇིག་རྟེན༌[^1366]ལས་འདས་པ་དང་རྣམ་པ་གཉིས་སུ་བཤད་པ་ལ་སློབ་པ་འདི་གང་གིས་གང་ལ་འདོད་ཆགས་དང་བྲལ་བ་ཐོབ་ཅེ་ན། འཇིག་རྟེན་འདས་ཀྱིས་སྲིད་རྩེ་ལས། །

[Block 3472]
ཆགས་བྲལ་འཇིག་རྟེན་པས་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེའི་གོང་ན་འཇིག་རྟེན་པ་མེད་པའི་ཕྱིར་དང་། [^1367]རང་གི་ས་པའི་གཉེན་པོ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3473]
གཉེན་པོ་མ་ཡིན་པ་ཡང་ཉོན་མོངས་པ་རྒྱས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 3474]
ཉོན་མོངས་པ་གང་ཞིག་དངོས་པོ་གང་ལ་རྒྱས་པར་འགྱུར་བ་དེ་ནི་དངོས་པོ་དེས་སྤོང་བར་བྱེད་པ་མ་ཡིན་ལ། གང་གི་གཉེན་པོ་གང་ཡིན་པ་དེ་ལ་ནི་ཉོན་མོངས་པ་དེ་རྒྱས་པར་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 3475]
གཞན་ལས་རྣམ་པ་གཉིས་སྲིད་པའི་རྩེ་མོ་ལས་གཞན་པའི་ས་ལ་ནི་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པས་ཀྱང་འདོད་ཆགས་དང་བྲལ་ལོ། །

[Block 3476]
དེ་ལ་ཡང་།

[Block 3477 [VERSE]]
འཇིག་རྟེན་པ་ཡིས་ཆགས་བྲལ་བའི། །
འཕགས་ལ་བྲལ་བའི་ཐོབ་རྣམ་གཉིས། །

[Block 3478]
འཕགས་པ་འཇིག་རྟེན་པའི་ལམ་གྱིས་འདོད་ཆགས་དང་བྲལ་བར་གྱུར་པ་ལ་བྲལ་བའི་ཐོབ་པ་འཇིག་རྟེན་པ་དང་། འཇིག་རྟེན་ལས་འདས་པ་རྣམ་པ་གཉིས་སྐྱེའོ། །

[Block 3479 [VERSE]]
ཁ་ཅིག་འཇིག་རྟེན་འདས་ཀྱིས་ཀྱང་། །
བཏང་ལ་ཉོན་མོངས་མི་ལྡན་ཕྱིར། །

[Block 3480]
གལ་ཏེ་འཕགས་པའི་ལམ་གྱིས་འདོད་ཆགས་དང་བྲལ་བ་ཐོབ་པ་ལ་འཇིག་རྟེན་པའི་བྲལ་བའི་ཐོབ་པ་མི་སྐྱེན་དེ་ལྟ་ན་འཕགས་པའི་ལམ་གྱིས་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ལས་འདོད་ཆགས་དང་བྲལ་བ་བསམ་གཏན་ལ་བརྟེན་ཏེ་དབང་པོ་རྣམས་འཕོ་བར་བྱེད་པ་གང་ཡིན་པ་དེ་ལམ༌[^1368]སྔ་མ་ཟད་པར་བཏང་བའི་ཕྱིར་དང་། འབྲས་བུའི་ལམ་འབའ་ཞིག་ཐོབ་པའི་ཕྱིར་ས་གོང་མ་པའི༌[^1369]ཉོན་མོངས་པ་བྲལ་བ་དང་མི་ལྡན་པར་ཡང་འགྱུར་ལ། དེ་བཏང་ན་ཡང་ཉོན་མོངས་པ་དེ་དག་དང་ལྡན་པར་ཡང་འགྱུར་རོ། །

[Block 3481]
སྲིད་རྩེའི་ཕྱེད་ལས་རྣམ་གྲོལ་དང་། གོང་དུ་སྐྱེས་པ་བཞི༌[^1370]མི་ལྡན། འཇིག་རྟེན་པའི་འབྲལ་བའི༌[^1371]ཐོབ་པ་མེད་དུ་ཟིན་ཀྱང་དེ་དག་དང་ལྡན་པར་མི་འགྱུར་ཏེ། དཔེར་ན་སྲིད་པའི་རྩེ་མོའི་རྣམ་པ་ཕྱེད་ལས་རྣམ་པར་གྲོལ་བ་ལ་དེའི་བྲལ་བའི་ཐོབ་པ༌[^1372]འཇིག་རྟེན་པ་ཡང་མེད་ལ། དབང་པོ༌[^1373]འཕོ་བས་འཇིག་རྟེན་ལས་འདས་པ་ལ་ཡང་བཏང་བཞིན་དུ་ཡང་ཉོན་མོངས་པ་དེ་དག་དང་ལྡན་པར་མི་འགྱུར་བ་དང་། ཡང་དཔེར་ན་སོ་སོའི་སྐྱེ་བོ་ལ་བསམ་གཏན་དང་པོ་ཡན་ཆད་དུ་སྐྱེས་པ་འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པའི་བྲལ་བའི་ཐོབ་པ་བཏང་བས་ཡང་དེ་དག་དང་ལྡན་པར་མི་འགྱུར་བ་བཞིན་པས་འདི་ནི་ཤེས་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 3482]
ས་གང་ཞིག་གིས་གང་ལས་འདོད་ཆགས་དང་བྲལ་བར་འགྱུར་ཞེ་ན།

[Block 3483 [VERSE]]
ཟག་མེད་མི་ལྕོགས་མེད་པ་ཡིས། །
ཐམས་ཅད་ལས་ནི་འདོད་ཆགས་བྲལ། །
སྲིད་པའི་རྩེ་མོའི་བར་ལས་སོ། །

[Block 3484]
ཡང་གང་ཞིག་ཉེར་བསྡོགས་ལ་བརྟེན་ཏེ་ས་འོག་མ་ལས་འདོད་ཆགས་དང་བྲལ་བ་ཐོབ་ན། ཅི་འདིའི་རྣམ་པར་གྲོལ་བའི་ལམ་ཐམས་ཅད་བར་ཆད་མེད་པའི་ལམ་བཞིན་དུ་ཉེར་བསྡོགས་ལས་སྐྱེའམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 3485]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 3486 [VERSE]]
ས་གསུམ་རྒྱལ་ལ་བསམ་གཏན་ནམ། །
ཉེར་བསྡོགས་ལས་མཐའི་རྣམ་གྲོལ་ལམ། །

[Block 3487]
འདོད་པའི་ཁམས་དང་། བསམ་གཏན་གཉིས་ཀྱི་འདོད་ཆགས་དང་བྲལ་བ་ལ་རྣམ་པར་གྲོལ་བའི་ལམ་ཐ་མ་ཉེར་བསྡོགས་སམ་བསམ་གཏན༌[^1374]དངོས་གཞི་ལས་སྐྱེའོ། །

[Block 3488]
གོང་མའི་ཉེར་བསྡོགས་ལས་མིན། ས་གསུམ་ལས་རྒྱལ་བ་ཡན་ཆད་ནི་བཏང་སྙོམས་གྱི་དབང་པོ་ཐུན་མོང་ཡིན་པའི་ཕྱིར་དངོས་གཞི་ཁོ་ན་ལས་སྐྱེའི་ཉེར་བསྡོགས་ལས་ནི་མ་ཡིན་ནོ། །

[Block 3489 [VERSE]]
ཟག་མེད་མི་ལྕོགས་མེད་པ་ཡིས། །
ཐམས་ཅད་ལས་ནི་འདོད་ཆགས་བྲལ།[^1375] །

[Block 3490]
ཞེས་བཤད་ཀྱི། གཞན་དག་ནི་མ་བཤད་པས་དེའི་ཕྱིར་འཕགས། བརྒྱད་ཀྱིས་རང་གོང་ས་ལས་རྒྱལ། །ཞེས་བྱ་བ་སྨོས་ཏེ། ཟག་པ་མེད་པའི་བསམ་གཏན་དང་། །བསམ་གཏན་ཁྱད་པར་ཅན་དང་། གཟུགས་མེད་པ་གསུམ་དང་བརྒྱད་ཀྱིས་ནི་རང་གི་ས་དང་གོང་མ་ལས་འདོད་ཆགས་དང་བྲལ་བར་འགྱུར་རོ། །

[Block 3491]
འོག་མ་ལས་ནི་མ་ཡིན་ཏེ། འདོད་ཆགས་དང་བྲལ་ཟིན་པའི་ཕྱིར་རོ། །

[Block 3492]
དེ་ལ་འཇིག་རྟེན་ལས་འདས་པའི་ལམ་བར་ཆད་མེད་པ་དང་། རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་ནི་བདེན་པ་ལ་དམིགས་པའི་ཕྱིར་བདེན་པའི་རྣམ་པར་ཞུགས་པ་དག་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་པོ། །

[Block 3493 [VERSE]]
འཇིག་རྟེན་པ་ཡི་རྣམ་གྲོལ་དང་། །
བར་ཆད་མེད་ལམ་གོ་རིམས་བཞིན། །
ཞི་སོགས་རགས་སོགས་རྣམ་པ་ཅན། །
གོང་དང་འོག་མའི་སྤྱོད་ཡུལ་ཅན། །

[Block 3494]
རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་ནི༌[^1376]ཅི་རིགས་པར་ས༌[^1377]གོང་མ་ལ་ཞི་བ་དང་། གྱ་ནོམ་པ་དང་། ངེས་པར་འབྱུང་བའི་རྣམ་པར་ལྟའོ། །

[Block 3495]
བར་ཆད་མེད་པའི་ལམ་རྣམས་ནི་ཞི་བ་ལ་སོགས་པའི་རྣམ་པ་ལས་བཟློག་པ་ས་འོག་མ་ལ་རག་ལས་པ་དང་། ཐ་བ་ངན་པ་དང་། རྩིག་པ་སྟུག་པོ་ལྟ་བུར་ལྟའོ། །

[Block 3496]
ཞར་ལ་འོངས་པ༌[^1378]རྫོགས་སོ།། །།

[Block 3497 [HEADING]]
#### ཟད་པ་ཤེས་པའི་མཇུག་ཐོགས་སུ་སྐྱེ་བ། ^6-2-4-0

[Block 3498]
ཡང་ཟད་པ་ཤེས་པའི་མཇུག་ཐོགས་སུ་ཅི་ཞིག་སྐྱེ་ཞེ་ན། གལ་ཏེ་མི་གཡོའི་ཟད་ཤེས་ལས། །

[Block 3499]
མི་སྐྱེའི་བློ་གྲོས། གལ་ཏེ་དགྲ་བཅོམ་པ་མི་གཡོ་བའི་ཆོས་ཅན་ཞིག་ཡིན་ན། [^1379]དེ་ལ་ཟད་པ་ཤེས་པའི་དེ་མ་ཐག་ཏུ་མི་སྐྱེ་བའི་ཤེས་པ་སྐྱེའོ། །

[Block 3500]
གལ་ཏེ་མིན། ཟད་པ་ཤེས་སམ་མི་སློབ་ལྟ། །གལ་ཏེ་མི་གཡོ་བའི་ཆོས་ཅན་མ་ཡིན་ན་ནི་ཟད་པ་ཤེས་པ་ལས་ཟད་པ་ཤེས་པ་ཁོ་ནའམ། མི་སློབ་པའི་ཡང་དག་པའི་ལྟ་བ་སྐྱེའོ། །

[Block 3501]
ཡོངས་སུ་ཉམས་པ་སྲིད་པའི་ཕྱིར་མི་སྐྱེ་བ་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 3502]
ཅི་མི་གཡོ་བའི་ཆོས་ཅན་ལ་དེ་མི་སྐྱེ་བ་ཁོ་ན་ཡིན་ནམ་ཞེ་ན། དེ་ནི་དགྲ་བཅོམ་ཐམས་ཅད་ལ། །མི་གཡོ་བའི༌[^1380]ཆོས་ཅན་ལ་ཡང་རེས་འགའ་མི་སྐྱེ་བ་ཤེས་པ་ལས་མི་སྐྱེ་བ་ཤེས་པ་ཁོ་ན་སྐྱེ་ལ། རེས་འགའ་མི་སློབ་པའི༌[^1381]ཡང་དག་པའི་ལྟ་བ་སྐྱེའོ། །

[Block 3503 [HEADING]]
#### དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ། ^6-2-5-0

[Block 3504]
གང་དག་འབྲས་བུ་བཞིར་བཤད་པ་དེ་དག་གང་གི་འབྲས་བུ་ཡིན་ཞེ་ན། དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་ཡིན་ནོ། །

[Block 3505]
དགེ་སྦྱོང་གི་ཚུལ་ཞེས་བྱ་བ་འདི་ཅི་ཞིག་ཅེ་ན། དགེ་སྦྱོང་ཚུལ་ནི་དྲི་མེད་ལམ། །དགེ་སྦྱོང་གི་ཚུལ་ནི་ཟག་པ་མེད་པའི་ལམ་ཡིན་ནོ། །
--- END BLOCKS ---
