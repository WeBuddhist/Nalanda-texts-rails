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

[Block 3681]
ཡང་ཞེས་བྱ་བའི་སྒྲས་ནི་ཚུལ་ཁྲིམས་དང་ཆོས་ལ་ཤེས་ནས་དད་པ་དག་ཀྱང་ཐོབ་པར་སྟོན་ཏོ། །

[Block 3682]
འདིར་གང་ལ་ཆོས་སུ་དགོངས་པ་ཡིན་ཞེ་ན།

[Block 3683 [VERSE]]
ཆོས་བདེན་གསུམ་དང་རང་སངས་རྒྱས། །
བྱང་ཆུབ་སེམས་དཔའི་ལམ་ཡིན་ནོ། །

[Block 3684]
དེ་དག་ནི་དད་པའི་གཞིའི༌[^1453]བྱེ་བྲག་ལས་མིང་གི་སྒོ་ནས་ཤེས་ནས་དད་པ་བཞི་ཞེས་བྱའོ། །

[Block 3685]
རྫས་སུ་གཉིས་ཏེ་དད་པ་དང་། ཚུལ་ཁྲིམས་དང་། སངས་རྒྱས་དང་། ཆོས་དང་། དགེ་འདུན་ལ་ཤེས་ནས་དད་པ་རྣམས་ནི་དད་པའི་རང་བཞིན་དག་གོ། །

[Block 3686]
འཕགས་པ་དགྱེས་པའི་ཚུལ་ཁྲིམས་རྣམས་ནི་ཚུལ་ཁྲིམས་ཁོ་ནའོ། །ཤེས་ནས་དད་པ་རྣམས༌[^1454]གཅིག་ཏུ། །དྲི་མ་མེད་པ་ཡིན། ཟག་པ་མེད་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3687]
མདོ་ལས།

[Block 3688 [HEADING]]
### ཡང་དག་པའི་རྣམ་པར་གྲོལ་བ་དང་ཡང་དག་པའི་ཤེས་པ། ^6-7-0

[Block 3689]
སློབ་པ་རྣམས་ནི་ལམ་ཡན་ལག་བརྒྱད་དང་ལྡན་ནོ། །

[Block 3690]
མི་སློབ་པ་རྣམས་ནི་བཅུ་དང་ལྡན་ནོ་ཞེས་གསུངས་པ། ཅིའི་ཕྱིར་སློབ་པ་ལ་ཡང་དག་པའི་རྣམ་པར་གྲོལ་བ་དང་། ཡང་དག་པའི་ཤེས་པ་མ་བཤད་ཅེ་ན། བཅིངས་ཕྱིར་སློབ་པའི་ཡན་ལག་ཏུ། །རྣམ་གྲོལ་མ་བཤད། སློབ་པ་ནི་ཉོན་མོངས་པའི་འཆིང་བའི་ཕྱོགས་གཅིག་གིས་བཅིངས་པ་ཡིན་པས་འདི་ལ་རྣམ་པར་གྲོལ་བ་ཞེས་མ་གསུངས་སོ། །

[Block 3691]
རྣམ་པར་གྲོལ་བ་མེད་པའི་ཕྱིར་རྣམ་པར་གྲོལ་བའི་ཤེས་པ་ཡང་མེད་དོ། །

[Block 3692]
དེ་རྣམ་གཉིས། འདུས་བྱས་དང་འདུས་མ་བྱས་པའོ། །

[Block 3693]
དེ་ལ། ཉོན་མོངས་བཅོམ་པ་འདུས་མ་བྱས། མོས་པ་འདུས་བྱས།[^1455] །ཉོན་མོངས་པ་སྤངས་པ་ནི་རྣམ་གྲོལ་འདུས་མ་བྱས་པ༌[^1456]ཡིན་ནོ། །

[Block 3694]
མི་སློབ་པའི་མོས་པ་ནི་འདུས་བྱས་སོ། །

[Block 3695]
ཡན་ལག་ནི། དེ་ཡིན། འདུས་བྱས་པའི་མོས་པ་དེ་ཉིད་མི་སློབ་པའི་ཡན་ལག་ཏུ་བཤད་དེ། ཡན་ལག་རྣམས་འདུས་བྱས་པའི་ཕྱིར་རོ། །

[Block 3696]
དེ་ཉིད་རྣམ་གྲོལ་གཉིས། སེམས་རྣམ་པར་གྲོལ་བ་དང་། ཤེས་རབ་རྣམ་པར་གྲོལ་བའོ། །བྱང་ཆུབ་ཇི་སྐད་བཤད༌[^1457]ཤེས་པ། །

[Block 3697]
སྔར་བྱང་ཆུབ་བཤད་པ་གང་ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་དེ་ཉིད་འདིར་ཡང་དག་པའི་ཤེས་པའོ། །

[Block 3698]
སེམས་ཇི་ལྟར་རྣམ་པར་གྲོལ་ཞེ་ན།

[Block 3699 [VERSE]]
མི་སློབ་སེམས་ནི་སྐྱེ་འགྱུར་བ། །
སྒྲིབ་པ་ལས་ནི་རྣམ་གྲོལ་འགྱུར། །

[Block 3700]
མི་སློབ་པའི་སེམས་མ་འོངས་པ་སྒྲིབ་པ་རྣམས་ལས་གྲོལ་ལོ། །

[Block 3701]
གནས་སྐབས་གང་བའི་ལམ་གྱིས་དེའི་སྒྲིབ་པ་སྤོང་ཞེ་ན།

[Block 3702 [VERSE]]
འགག་པར་འགྱུར་བའི་ལམ་གྱིས་ནི། །
དེ་ཡི་སྒྲིབ་པ་རབ་ཏུ་སྤོང་། །

[Block 3703]
ད་ལྟར་གྱི་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3704 [HEADING]]
### སྤངས་པའི་ཁམས་དང་འདོད་ཆགས་དང་བྲལ་བའི་ཁམས་དང་འགོག་པའི་ཁམས། ^6-8-0

[Block 3705]
རྣམ་པར་གྲོལ་བ་འདུས་མ་བྱས་བཤད་པ་གང་ཡིན་པ་དང་། ཁམས་གསུམ་པོ་སྤངས་པའི་ཁམས་དང་། འདོད་ཆགས་དང་བྲལ་བའི་ཁམས་དང་། འགོག་པའི་ཁམས་ཞེས་འབྱུང་བ་གང་ཡིན་པ་དེ་དག་ལ་ཁྱད་པར་ཅི་ཡོད་ཅེ་ན། འདུས་མ་བྱས་ཉིད་ཁམས་ཞེས་བྱ། །རྣམ་པར་གྲོལ་བ་འདུས་མ་བྱས་པ་དེ་ཉིད་ཁམས་གསུམ་ཡིན་ནོ། །

[Block 3706]
དེ་ལ་ཡང་། འདོད་ཆགས་ཀུན་ཟད་འདོད་ཆགས་བྲལ། །འདོད་ཆགས་སྤངས་པ་ནི་འདོད་ཆགས་དང་བྲལ་བའི་ཁམས་ཡིན་ནོ། །

[Block 3707]
སྤངས་པའི་ཁམས་ནི་གཞན་དག་གོ། །

[Block 3708]
འདོད་ཆགས་ལས་གཞན་ཉོན་མོངས་པ་སྤངས་པ་ནི་སྤངས་པའི་ཁམས་ཡིན་ནོ། །

[Block 3709]
འགོག་པའི་ཁམས་ཞེས་བྱ་བ་གཞི། །ཡང་དག་པར་ཟད་པ་ཞེས་བྱ་བ་ཁོ་ནར་སྦྱར་ཏེ། ཉོན་མོངས་པ་ལ་མ་གཏོགས་པའི་གཞི་སྤོང་བ་ནི་འགོག་པའི་ཁམས་ཡིན་ནོ། །

[Block 3710 [HEADING]]
### ཡིད་འབྱུང་བ་དང་འདོད་ཆགས་དང་བྲལ་བའི་མུ་བཞི། ^6-9-0

[Block 3711]
དངོས་པོ་གང་གིས་ཡིད་འབྱུང་བར་འགྱུར་བའི་དངོས་པོ་དེས་འདོད་ཆགས་དང་བྲལ་བར་ཡང༌[^1458]འགྱུར་རམ་ཞེ་ན། མུ་བཞིའོ། །ཇི་ལྟར་བྱས་པས་ཤེ་ན། སྡུག་བསྔལ་རྒྱུ་བཟོད་ཤེས་རྣམས་ཀྱིས། །ཡིད་འབྱུང་། སྡུག་བསྔལ་དང་ཀུན་འབྱུང་གི་བཟོད་པ་དང་ཤེས་པ་རྣམས་ཁོ་ནས་ཡིད་འབྱུང་ངོ་། །གང་གིས་སྤོང༌[^1459]འགྱུར་བ། ཀུན་གྱི༌[^1460]འདོད་ཆགས༌[^1461]བྲལ་བར་འགྱུར། །སྡུག་བསྔལ་ལ་སོགས་པ་ལ་བཟོད་པ་དང་ཤེས་པ་དག་གིས་ཉོན་མོངས་པ་སྤོང་བར་འགྱུར་བ་ཐམས་ཅད་ཀྱིས་ཀྱང་འདོད་ཆགས་དང་བྲལ་བར་འགྱུར་རོ། །

[Block 3712]
དེ་ལྟ་ན་ནི་མུ་བཞི་སྲིད། །དེ་ལ་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་ལ་བཟོད་པ་དང་། ཤེས་པ་རྣམས་ཀྱིས་ཉོན་མོངས་པ་མི་སྤོང་ན་ཡིད་འབྱུང་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 3713]
འགོག་པ་དང་ལམ་ལ་བཟོད་པ་དང་ཤེས་པ་རྣམས་ཀྱིས་ཉོན་མོངས་པ་དག་སྤོང་ན་འདོད་ཆགས་དང་བྲལ་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 3714]
སྔ་མ་རྣམས་ཀྱིས་ཉོན་མོངས་པ་དག་སྤོང་ན་གཉིས་ཀ་ཡིན་ནོ། །

[Block 3715]
ཕྱི་མ་རྣམས་ཀྱིས་ཉོན་མོངས་པ་དག་མི་སྤོང་ན་གཉིས་ཀ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
