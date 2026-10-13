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

[Block 3716]
དེ་ལ་འཇིག་རྟེན་གྱི་ལམ་གྱིས་འདོད་ཆགས་དང་བྲལ་བ་ཞིག་བདེན་པ་རྣམས་ལ༌[^1462]ལྟ་ན་ཆོས་ཤེས་པའི་བཟོད་པ་རྣམས་ཀྱིས་ཉོན་མོངས་པ་དག་མི་སྤོང་ངོ་། །ཤེས་པ་རྣམས་ཀྱིས་སྦྱོར་བ་དང་། །རྣམ་པར་གྲོལ་བ་དང་ཁྱད་པར་ཅན་གྱི་ལམ་གྱིས་བསྡུས་པ་རྣམས་ཀྱང་མི་སྤོང་ངོ་། །ལམ་དང་གང་ཟག་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་དྲུག་པའོ།། །།

[Block 3717 [HEADING]]
## ཡེ་ཤེས་བསྟན་པ། ^7-0

[Block 3718 [HEADING]]
### ལྟ་བ་དང་ཤེས་པ། ^7-1-0

[Block 3719]
བཟོད་པ་རྣམས་དང་། ཞེས་པ༌[^1463]རྣམས་དང་། ཡང་དག་པའི་ལྟ་བ་རྣམས་དང་། ཡང་དག་པའི་ཤེས་པ་ཞེས་ཀྱང་འབྱུང་ན། ཅི་བཟོད་པ་དག་ཡིན་ལ་ཤེས་པ་མ་ཡིན་ནམ། ཡང་དག་པའི་ཤེས་པ་ཡིན་ལ་ཡང་དག་པའི་ལྟ་བ་མ་ཡིན་ནམ་ཞེ་ན། དྲི་མེད་བཟོད་རྣམས་ཤེས༌[^1464]པ་མིན། །དེས་སྤང་བར་བྱ་བའི་ཕྲ་རྒྱས་ཐེ་ཚོམ་མ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 3720]
དེ་དག་ཡང་དག་པར་རྟོག་པ་དང་། ཡོངས་སུ་ཚོལ་བའི་བདག་ཉིད་ཅན་ཡིན་པའི༌[^1465]ཕྱིར་ལྟ་བ་དག་ཡིན་ནོ། །

[Block 3721]
ཇི་ལྟར་བཟོད་པ་རྣམས་ལྟ་བ་ཡིན་གྱི་ཤེས་པ་རྣམས་མ་ཡིན་པ་དེ་བཞིན་དུ། ཟད་དང་མི་སྐྱེའི་བློ་ལྟ་མིན། །ཡང་དག་པར་རྟོག་པ་མེད་པ་དང་། ཡོངས་སུ་ཚོལ་བའི༌[^1466]བསམ་པ་ཅན་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3722]
དེ་ལས་གཞན་འཕགས་བློ་གཉིས་ཀ །བཟོད་པ་དང་། ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་དག་ལས་གཞན་པ་ཟག་པ་མེད་པའི་ཤེས་རབ་ནི་ལྟ་བ་དང་ཤེས་པ་ཡང་ཡིན་ནོ། །

[Block 3723]
གཞན་ཤེས། འཇིག་རྟེན་གྱི་ཤེས་རབ་པོ། །དྲུག་ནི་ལྟ་བའང་ཡིན། ལྟ་བ་ལྔ་དང་། འཇིག་རྟེན་པའི་ཡང་དག་པའི་ལྟ་བ་དང་འཇིག་རྟེན་པའི་ཤེས་རབ་རྣམ་པ་དེ་དྲུག་ལྟ་བ་ཡིན་གྱི་གཞན་ནི་ལྟ་བ་མ་ཡིན་ནོ། །

[Block 3724]
འདི་དག་དང་གཞན་དག་ཀྱང་ཤེས་པ་ནི་ཡིན་ནོ། །

[Block 3725 [HEADING]]
### ཤེས་པ་བཅུ། ^7-2-0

[Block 3726]
ཇི་སྙེད་ཅིག་གིས་ཤེས་པ་ཐམས་ཅད་བསྡུས་ཤེ་ན། ཤེས་པ་བཅུ་བསྡུས་སོ། །

[Block 3727]
མདོར་བསྡུ་ན། ཤེས་པ་ཟག་བཅས་ཟག་པ་མེད། །དེ་གཉིས་ལས་ཀྱང་།

[Block 3728]
དང་པོ་ཀུན་རྫོབ་ཅེས་བྱའོ། །

[Block 3729]
ཟག་པ་དང་བཅས་པ༌[^1467]གང་ཡིན་པ་དེ་ནི་ཀུན་རྫོབ་ཤེས་པ་ཡིན་ནོ། །

[Block 3730 [VERSE]]
ཟག་མེད་རྣམ་གཉིས་ཆོས་དང་ནི། །
རྗེས་སུ་ཤེས་པ་ཁོ་ན་ཡིན། །

[Block 3731]
ཤེས་པ་གཉིས་པོ་དེ་དག་ནི་གསུམ་ཡིན་ནོ། །

[Block 3732]
དེ་ལ་ཀུན་རྫོབ་ཡུལ་ནི་ཐམས་ཅད་དོ། །

[Block 3733]
ཀུན་རྫོབ་ཤེས་པའི་དམིགས་པ་ནི་ཆོས་ཐམས་ཅད་དོ། །

[Block 3734]
ཆོས་ཤེས་བྱ་བའི་སྤྱོད་ཡུལ་ནི། །འདོད་སྡུག་བསྔལ་སོགས། ཆོས་ཤེས་པའི་དམིགས་པ་ནི་འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་དང་། དེའི་ཀུན་འབྱུང་བ་དང་། འགོག་པ་དང་། ལམ་རྣམས་ཡིན་ནོ། །

[Block 3735]
རྗེས་ཤེས་པའི། སྤྱོད་ཡུལ་གོང་མའི༌[^1468]སྡུག་བསྔལ་སོགས། །རྗེས་སུ་ཤེས་པའི་དམིགས་པ་ནི་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་རྣམས་ཀྱི་སྡུག་བསྔལ་ལ་སོགས་པའོ། །

[Block 3736]
དེ་དག་ཉིད་བདེན༌[^1469]བྱེ་བྲག་གིས། །བཞི་སྟེ། སྡུག་བསྔལ་ལ་སོགས་པའི་ཤེས་པ་རྣམས་ཡིན་ཏེ། དེ་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3737]
རྣམ་བཞི་དེ་དག་ནི། མི་སྐྱེ་བ་དང་ཟད་པ་ཤེས། །དེ་དག་ཆོས་དང་རྗེས་སུ་ཤེས་པ་བཞི་སྟེ། ཟད་པ་ཤེས་པ་དང་། མི་སྐྱེ་བ་ཤེས་པ་ཞེས་བྱའོ། །

[Block 3738 [VERSE]]
དེ་གཉིས་དང་པོ་སྐྱེས་པ་ནི། །
སྡུག་བསྔལ་རྒྱུ་རྗེས༌[^1470]ཤེས་པ་ཡིན། །

[Block 3739]
སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་གི་རྣམ་པ་རྣམས་ཀྱིས་སྲིད་པའི་རྩེ་མོའི་ཕུང་པོ་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3740 [HEADING]]
#### ཕ་རོལ་གྱི་སེམས་ཤེས་པ། ^7-2-1-0

[Block 3741]
བཞི་ལས་ཕ་རོལ་སེམས་རིག་པ། །ཕ་རོལ་གྱི་སེམས༌[^1471]རིག་པ་ནི་ཆོས་དང་རྗེས་སུ་ཤེས་པ་དང་། ལམ་དང་། ཀུན་རྫོབ་ཤེས་པ་རྣམས་སུ་བལྟ་བར་བྱའོ། །

[Block 3742]
དེའི་ངེས་པ་ནི་འདི་ཡིན་ཏེ།

[Block 3743 [VERSE]]
དེས་ནི་ས་དབང་གང་ཟག་འདས། །
ཞིག་དང་མ་སྐྱེས་མི་རིག་གོ། །

[Block 3744]
ས་འདས་པ་མི་རིག༌[^1472]པ་ནི་བསམ་གཏན་འོག་མའི་ས་པས་བསམ་གཏན་གོང་མའི་ས་པའོ། །

[Block 3745]
དབང་པོ་འདས་པ་མི་ཤེས་པ་ནི་དད་པས་མོས་པ་དང་། དུས་ཀྱི་རྣམ་པར་གྲོལ་བའི་ལམ་གྱིས་མཐོང་བས་ཐོབ་པ་དང་དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བའི་ལམ་མོ། །

[Block 3746]
གང་ཟག་འདས་པ་མི་ཤེས་པ་ནི་ཕྱིར་མི་འོང་བ་དང་དགྲ་བཅོམ་པ་དང་ཉན་ཐོས་དང་། རང་སངས་རྒྱས་དང་། སངས་རྒྱས་ཀྱི་ལམ་འོག་མས་གོང་མའོ། །

[Block 3747]
ཞིག་པ་དང་མ་སྐྱེས་པ་མི་ཤེས་པ་ནི་འདས་པ་དང་མ་འོངས་པའོ། །

[Block 3748]
གཞན་ཡང་། ཆོས་རྗེ༌[^1473]བློ༌[^1474]ཕྱོགས་ཕན་ཚུན་མིན། །ཕ་རོལ་གྱི་སེམས་ཤེས་པས༌[^1475]ཆོས་ཤེས་པའི་ཕྱོགས་དང༌[^1476]མཐུན་པས་ཀྱང༌[^1477]རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པའི་སེམས་མི་ཤེས་སོ། །

[Block 3749]
དེ་བཞིན་དུ་གཞན་གྱི༌[^1478]གཞན་ཡང་ངོ་། །མཐོང་བའི་ལམ་ལ་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་མེད་དོ། །

[Block 3750]
དེའི་དམིགས་པ་ནི་ཡོད་དེ། དེ་ལ་ཕ་རོལ་གྱི་སེམས་ཤེས་པས་མཐོང་བའི་ལམ་ཤེས་པར་འདོད་པས་སྦྱོར་བ་བྱས་པ།
--- END BLOCKS ---
