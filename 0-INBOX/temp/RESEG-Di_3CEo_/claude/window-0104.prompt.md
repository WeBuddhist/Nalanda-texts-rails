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
[Block 3641]
ཡང་ལམ་དེ་ཉིད་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་སུམ་ཅུ་རྩ་བདུན་དུ་གསུངས་ཏེ། དེ་ལ་ཟད་དང་མི་སྐྱེ་ཤེས་པ་ནི། །བྱང་ཆུབ། ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་ནི་གང་ཟག་གི༌[^1429]བྱེ་བྲག་གིས་རྣམ་པ་གསུམ་མོ། །

[Block 3642]
དེ་དང་མཐུན་ཉིད་ཕྱིར། སུམ་ཅུ་རྩ་བདུན་དེའི་ཕྱོགས་མཐུན། བྱང་ཆུབ་དང་མཐུན་པའི་ཕྱིར། མིང་གི༌[^1430]སྒོ་ནས། བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་སུམ་ཅུ་རྩ་བདུན་ཞེས་བྱའོ། །

[Block 3643]
རྫས་སུ་བཅུ།[^1431] བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་ཐམས་ཅད་ནི་རྫས་བཅུ་པོ་འདི་ལྟ་སྟེ།

[Block 3644 [VERSE]]
དད་དང་བརྩོན་འགྲུས་དྲན་པ་དང་། །
ཤེས་རབ་ཏིང་འཛིན་བཏང་སྙོམས་དགའ། །
རྟོག་དང་ཚུལ་ཁྲིམས་ཤིན་ཏུ་སྦྱངས། །
དེ་ལྟར་དེ་དག་ནི་རྫས་བཅུའོ། །

[Block 3645]
ཇི་ལྟར་བྱས་ནས་ཤེ་ན།

[Block 3646 [VERSE]]
དྲན་པ་ཉེར་གཞག་ཤེས་རབ་སྟེ། །
བརྩོན་འགྲུས་ཡང་དག་འཇོག་ཅེས་བྱ། །
རྫུ་འཕྲུལ་རྐང་པ་ཏིང་འཛིན་ཏོ། །
དྲན་པ་ཉེ་བར་གཞག་པ་དང་། །

[Block 3647]
ཡང་དག་པར་རབ་ཏུ་སྤོང་བ་དང་། རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་ནི་ཤེས་རབ་དང་། བརྩོན་འགྲུས་དང་། ཏིང་ངེ་འཛིན་གྱི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 3648]
དེའི་ཕྱིར་རེ་ཞིག་དབང་པོ་དང་སྟོབས་ནི་མིང་གིས་སྨོས་ལ། དད་པ་དང་། བརྩོན་འགྲུས་དང་། དྲན་པ་དང་། ཏིང་ངེ་འཛིན་དང་། ཤེས་རབ་ཀྱི༌[^1432]རྫས་ལྔ་ཡིན་ཏེ། དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་དང་། ཆོས་རྣམ་པར་འབྱེད་པ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་། ཡང་དག་པའི་ལྟ་བ་ནི་ཤེས་རབ་ཁོ་ན་ཡིན་ནོ། །

[Block 3649]
ཡང་དག་པར་རབ་ཏུ་སྤོང་བ་རྣམས་དང་། བརྩོན་འགྲུས་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་། ཡང་དག་པའི་རྩོལ་བ་ནི་བརྩོན་འགྲུས་ཁོ་ན་ཡིན་ནོ། །

[Block 3650]
རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་དང་། ཏིང་ངེ་འཛིན་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་། ཡང་དག་པའི་ཏིང་ངེ་འཛིན་ནི་ཏིང་ངེ་འཛིན་ཁོ་ན་ཡིན་ནོ། །

[Block 3651]
དྲན་པ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་། ཡང་དག་པའི་དྲན་པ་ནི་དྲན་པ་ཁོ་ན་ཡིན་ནོ། །ཅི་ཞིག་ལུས་ཤེ་ན། དགའ་བ་དང་། ཤིན་ཏུ་སྦྱངས་པ་དང་། བཏང་སྙོམས་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་། ཡང་དག་པའི་རྟོག་པ་དང་། ཡང་དག་པའི་ངག་དང་། ཡང་དག་པའི་ལས་ཀྱི་མཐའ་དང་། ཡང་དག་པའི་འཚོ་བ་རྣམས་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཡན་ལག་སྟེ། དེ་ལྟར་ན་བཅུ་ཡིན་ནོ། །

[Block 3652]
འདི་སྐད་དུ། དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་ནི་ཤེས་རབ་དང་བརྩོན་འགྲུས་དང་ཏིང་ངེ་འཛིན་གྱི་རང་བཞིན་དག་ཡིན་ནོ་ཞེས་གང་བཤད་པ་དེས༌[^1433]ནི། གཙོ་བོ་སྨོས་པས། ཡིན་པར་རིག་པར་བྱའི། དེ་དག་ནི། སྦྱོར་བྱུང་ཡོན་ཏན་ཀུན་ཀྱང་ཡིན། །གཙོ་བོ་སྨོས་པས་དེ་སྐད་བཤད་ཀྱི། དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་ནི་སྦྱོར་བ་ལས་བྱུང་བའི་ཡོན་ཏན་ཐམས་ཅད་ཀྱང་ཡིན་ནོ། །

[Block 3653]
གནས་སྐབས་གང་དུ་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་གང་ཞིག་རབ་ཏུ་འབྱེད་ཅེ་ན།

[Block 3654 [VERSE]]
སྡེ་ཚན་བདུན་ནི་གོ་རིམས་བཞིན། །
ལས་ནི་དང་པོ༌[^1434]པ་དག་དང་། །
ངེས་འབྱེད་ཆ་མཐུན་རྣམས་དང་ནི། །
བསྒོམ་དང་མཐོང་ལ་རབ་ཏུ་ཕྱེ། །

[Block 3655]
ལས་དང་པོ་པའི་གནས་སྐབས་སུ་ནི་ལུས་ལ་སོགས་པ་ཉེ་བར་བརྟག་པའི༌[^1435]ཕྱིར་དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་སོ། །

[Block 3656]
ཁྱད་པར་ཐོབ་པས་བརྩོན་འགྲུས་ཡང་དག་པར་སྤེལ་བའི་ཕྱིར་དྲོ་བར་འགྱུར་བ༌[^1436]དག་ལ་ནི་ཡང་དག་པར་རབ་ཏུ་འཇོག་པ་རྣམས་སོ། །

[Block 3657]
ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་བའི་དགེ་བའི་རྩ་བ་ལ་འཇུག་པའི་ཕྱིར་རྩེ་མོ་དག་ལ་ནི། རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་སོ། །

[Block 3658]
ཡང་ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་བའི་སྒོ་ནས་དབང༌[^1437]ཐོབ་པའི་ཕྱིར་བཟོད་པ་དག་ལ་ནི་དབང་པོ་རྣམས་སོ། །

[Block 3659]
ཉོན་མོངས་པ་རྣམས་ཀྱིས་མི་བརྫི་བའི༌[^1438]ཕྱིར་ཆོས་མཆོག་དག་ལ་ནི་སྟོབས་རྣམས་སོ། །

[Block 3660]
བྱང་ཆུབ་དང་ཉེ་བའི་ཕྱིར་བསྒོམ་པའི་ལམ་ལ་ནི་བྱང་ཆུབ་ཀྱི་ཡན་ལག་རྣམས་སོ། །

[Block 3661]
འགྲོ་བས་རབ་ཏུ་ཕྱེ་བའི་ཕྱིར་མཐོང་བའི་ལམ་ལ་ནི་ལམ་གྱི་ཡན་ལག་རྣམས་ཏེ། དེ་ནི་མྱུར་བར་འགྲོ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3662]
བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་དུ་ཞིག་ནི་ཟག་པ་དང་བཅས་པ་ཡིན། དུ་ཞིག་ནི་ཟག་པ་མེད་པ་ཡིན་ཞེས་བྱ་བ་འདི་བརྗོད་པར་བྱ་སྟེ། བྱང་ཆུབ་ཡན་ལག་ལམ་ཡན་ལག །ཟག་པ་མེད། དེ་གཉིས་ནི་བསྒོམ་པ་དང་མཐོང་བའི་ལམ་ལ་རྣམ་པར་གཞག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3663]
གཞན་རྣམས༌[^1439]གཉིས་སོ། །

[Block 3664]
བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་གཞན་དག་ནི་ཟག་པ་དང་བཅས་པ་དང་། ཟག་པ་མེད་པ་དག་ཡིན་ནོ། །

[Block 3665]
ས་གང་ན་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་དུ་ཞིག་ཡོད་ཅེ་ན།

[Block 3666 [VERSE]]
བསམ་གཏན་དང་པོ་ན་ཐམས་ཅད། །
མི་ལྕོགས་མེད་ན་དགའ༌[^1440]མ་གཏོགས། །

[Block 3667]
ཉེར་བསྡོགས༌[^1441]རྣམས་ནི་སྟོབས་ཀྱིས་དྲང་དགོས་པའི་ཕྱིར་དང་། [^1442]ས་འོག་མའི་དགོས་པ་དང་བཅས་པའི་ཕྱིར་དགའ་བ་མེད་དོ། །

[Block 3668]
གཉིས་པ་ན་ནི་རྟོག་མ་གཏོགས།[^1443] །

[Block 3669]
གཉིས་པ་ན་ཡང༌[^1444]དག་པའི་རྟོག་པ་མེད་དེ།

[Block 3670 [VERSE]]
དེ་ན་རྟོག་པ་མེད་པའི་ཕྱིར་རོ། །
གཉིས་ན་དེ་གཉིས་མ་གཏོགས་པ། །

[Block 3671]
བསམ་གཏན༌[^1445]

[Block 3672]
གསུམ་པ་དང་བཞི་པ་དག༌[^1446]ན་ནི་དགའ་བ་དང་རྟོག་པ་དག་མ་གཏོགས་པའོ། །

[Block 3673]
བསམ་གཏན་བར་ནའང་། དེ་གཉིས་ཉིད་མ་གཏོགས་པ་སུམ་ཅུ་རྩ་ལྔ་ཁོ་ནའོ། །

[Block 3674]
གཟུགས་མེད་པ། གསུམ་ནའང་། དེ་དང་ཚུལ་ཡན་ལག །མ་གཏོགས་ཞེས་བྱ་བར་སྦྱར་ཏེ། གཟུགས་མེད་པ་གསུམ་ན་ནི་ཡང་དག་པའི་ངག་དང་། ལས་ཀྱི་མཐའ་དང་། འཚོ་བ་རྣམས་དང་། དགའ་བ་དང་།

[Block 3675 [VERSE]]
རྟོག་པ་དག་མ་གཏོགས་པའོ། །
བྱང་ཆུབ་དང་ནི་ལམ་ཡན་ལག །
མ་གཏོགས་འདོད་ཁམས་སྲིད་རྩེ་ན། །

[Block 3676]
འདོད་པའི་ཁམས༌[^1447]སྲིད་པའི་རྩེ་མོ་ལ་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་། ལམ་གྱི་ཡན་ལག་མ་གཏོགས་ཏེ། དེ་དག་ལ་ཟག་པ་མེད་པའི་ལམ་མེད་པའི་ཕྱིར་རོ། །

[Block 3677 [HEADING]]
### ཤེས་ནས་དད་པ། ^6-6-0

[Block 3678]
བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་ལ་གནས་པ་གནས༌[^1448]སྐབས་གང་དུ་ཤེས་ནས་དད་པ་ཐོབ་པར་རིག་པར་བྱ་ཞེ་ན།

[Block 3679 [VERSE]]
བདེན་གསུམ་མཐོང་ན་ཚུལ་ཁྲིམས་དང་། །
ཆོས་ལ་ཤེས་ནས་དད་པ་ཐོབ།[^1449] །
ལམ་མངོན་རྟོགས་ན༌[^1450]སངས་རྒྱས་དང་། །
དེ་ཡི་དགེ་འདུན་དག་ལ་ཡང་། །

[Block 3680]
སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་བ་དང་། འགོག་པའི་བདེན་པ་རྣམས་མངོན་པར་རྟོགས་ན་ཆོས་ལ་ཤེས་ནས་དད་པ་དང་། འཕགས་པ་དགྱེས་པའི་ཚུལ་ཁྲིམས་རྣམས་ཐོབ༌[^1451]པོ། །ལམ་གྱི་བདེན་པ་མངོན་པར་རྟོགས་ན་སངས་རྒྱས་དང་དེའི་ཉན་ཐོས་ཀྱི་དགེ་འདུན་ལ་ཤེས་ནས་དད་པ་ཐོབ་སྟེ། གང་ཞིག་དེ་གཉིས་ལ་དད་པ་དེ་ནི་སངས་རྒྱས་སུ་བྱེད་པའི་ཆོས་མི་སློབ་པ་དང་། དགེ་འདུན་དུ༌[^1452]བྱེད་པའི་ཆོས་སློབ་པ་དང་། མི་སློབ་པ་རྣམས་ལའོ། །
--- END BLOCKS ---
