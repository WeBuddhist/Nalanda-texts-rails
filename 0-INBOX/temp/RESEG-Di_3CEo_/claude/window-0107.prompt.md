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

[Block 3751 [VERSE]]
[^1479] ཉན་ཐོས་མཐོང་བའི་སྐད་ཅིག་གཉིས། །
རིག་སྟེ་བསེ་རུ་ལྟ་བུས་གསུམ། །
སངས་རྒྱས་སྦྱོར་བ་མེད་པར་ཀུན། །

[Block 3752]
ཕ་རོལ་གྱི་སེམས་ཤེས་པས་སྐད་ཅིག་མ་གཉིས་ཤེས་པ་སྟེ། སྡུག་བསྔལ་ལ་ཆོས་ཤེས༌[^1480]པའི་བཟོད་པ་དང་། ཆོས་ཤེས་པའོ། །

[Block 3753]
རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པ་ལ་དམིགས་པ་ནི་སྦྱོར་བ་གཞན་གྱིས་བསྒྲུབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3754]
རང་སངས་རྒྱས་ཀྱིས་ནི་དང་པོ་གཉིས་དང་།

[Block 3755]
བརྒྱད་པ་ཀུན་འབྱུང་བ་ལ་རྗེས་སུ་ཤེས་པ་དང་། གསུམ་ཤེས་ཏེ་སྦྱོར་བ་ཆུང་བའི་ཕྱིར།[^1481] གཞན་དག་ན་རེ་དང་པོ་དང༌[^1482]

[Block 3756]
གཉིས་པ་དང་བཅོ་ལྔ་པ་རྣམས་ཤེས་སོ་ཞེས་ཟེར་རོ། །

[Block 3757]
སངས་རྒྱས་ཀྱིས་ནི་སྦྱོར་བ་མེད་པར་མཐོང་བའི་ལམ་གྱི་སྐད་ཅིག་མ་ཐམས་ཅད་མཁྱེན་ཏོ། །

[Block 3758 [HEADING]]
#### ཟད་པ་ཤེས་པ་དང་མི་སྐྱེ་བ་ཤེས་པའི་ཁྱད་པར། ^7-2-2-0

[Block 3759]
ཡང་ཟད་པ་ཤེས་པ་དང་མི༌[^1483]ཤེས་པ་དག་ལ་ཁྱད་པར་ཅི་ཡོད་ཅེ་ན།

[Block 3760 [VERSE]]
ཟད་པ་ཤེས་པ་བདེན་རྣམས་ལ། །
ཡོངས་ཤེས་པ༌[^1484]ལ་སོགས་ངེས་པའོ། །
ཡོངས་ཤེས་བྱར་མེད་ཅེས་ལ་སོགས། །
མི་སྐྱེ་བ་ཡི་བློར་འདོད་དོ། །

[Block 3761]
སྡུག་བསྔལ་ལ་སོགས་པ་རྣམས་ལ་ཡོངས་སུ་ཤེས། སྤངས་མངོན་སུམ་དུ་བྱས། བསྒོམས་པ་ཉིད་ཀྱི་ངེས་པ་ནི་ཟད་པ་ཤེས་པའོ། །

[Block 3762]
དེ་བཞིན་དུ་ཡོངས་སུ་ཤེས་པར་བྱ་བ་མེད་པ་ནས་བསྒོམ་པར་བྱ་བ་མེད་དོ་ཞེས་བྱ་བའི་བར་གྱིས་ངེས་པ་ནི་མི་སྐྱེ་བའི་ཤེས་པའོ། །

[Block 3763 [HEADING]]
#### རང་བཞིན་དང་གཉེན་པོ་ལ་སོགས་པ་ལས་བཅུ། ^7-2-3-0

[Block 3764]
དེ་ལྟར་དེ་དག་ནི་ཤེས་པ་བཅུ་སྟེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། ཀུན་རྫོབ་ཤེས་པ་དང་། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དང་། ཀུན་འབྱུང་ཤེས་པ་དང་། འགོག་པ་ཤེས་པ་དང་། ལམ་ཤེས་པ་དང་། ཟད་པ་ཤེས་པ་དང་། མི་སྐྱེ་བ་ཤེས་པའོ། །ཅིའི་ཕྱིར་དེ་དག་གསུམ་ཡོད་ལ་བཅུར་རྣམ་པར་གཞག་ཅེ་ན།

[Block 3765 [VERSE]]
རང་བཞིན་དང་ནི་གཉེན་པོ་དང་། །
རྣམ་པ་རྣམ་པ་སྤྱོད་ཡུལ་དང་། །
སྦྱོར་དང་བྱ་བ་བྱས་ཉིད་དང་། །
རྒྱུ་བྱས་པ༌[^1485]ལས་བཅུ་ཡིན་ནོ། །

[Block 3766 [VERSE]]
རང་བཞིན་ལས་ནི་ཀུན་རྫོབ་ཤེས་པ་སྟེ། །
དོན་དམ་པ༌[^1486]ནི་མི་ཤེས་པའི་ཕྱིར་རོ། །

[Block 3767]
གཉེན་པོ་ལས་ནི་ཆོས་དང་རྗེས་སུ་ཤེས་པ་དག་སྟེ། འདོད་པའི་ཁམས་དང་། ཁམས་གོང་མའི་གཉེན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3768]
རྣམ་པ༌[^1487]ལས་ནི་སྡུག་བསྔལ་དང་། །ཀུན་འབྱུང་བ་ཤེས་པ་དག་སྟེ། རྫས་ལ་དམིགས་པ་ཐ་མི་དད་པའི་ཕྱིར་རོ། །

[Block 3769]
རྣམ་པ་དང་དམིགས་པ་ལས་ནི་འགོག་པ་དང་ལམ་ཤེས་པ་དག་སྟེ། རྣམ་པ་དང་དམིགས་པ་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 3770]
སྦྱོར་བ་ལས་ནི་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་སྟེ། སེམས་ཤེས་པར་བྱ་བའི་དོན་དུ་སྦྱོར་བ་བྱས་པ་ལས་གྲུབ་པའི་ཕྱིར་སེམས་ལས་བྱུང་བ་ཡང་ཤེས་སོ། །

[Block 3771]
བྱ་བ་བྱས་པ་ལས་ནི་ཟད་པ་ཤེས་པ་ལྟ།[^1488] བྱ་བ་བྱས་པའི་རྒྱུད་ལ་དངོས་པོ་ཉིད་དུ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 3772]
རྒྱུ་རྒྱས་པ་ལས་ནི་མི་སྐྱེ་བ་ཤེས་པ་སྟེ། ཟག་པ༌[^1489]མེད་པའི་ཤེས་པ་ཐམས་ཅད་ཀྱི་རྒྱུ་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3773]
ཐམས་ཅད་ཀྱི་གཉེན་པོ་ཐམས་ཅད་ཡིན་པའི་ཕྱིར་ཆོས་ཤེས་པ་འདོད་པའི་ཁམས་ཀྱི་གཉེན་པོ་ཞེས་བཤད་པར་ཟད་ཀྱི།

[Block 3774 [VERSE]]
བསྒོམ་པའི་ལམ་ལ་འགོག་པའི་ལམ། །
ལམ་ལ་ཆོས་ཤེས་གང་ཡིན་དེ། །
ཁམས་གསུམ་གྱི་ནི་གཉེན་པོ་ཡིན། །

[Block 3775]
འགོག་པ་དང་ལམ་ལ་ཆོས་ཤེས་པའི་བསྒོམ་པའི་ལམ་གྱིས་བསྡུས་པ་དག་ནི་ཁམས་གསུམ་ཆར་གྱི་གཉེན་པོ་ཡིན་ནོ། །

[Block 3776 [HEADING]]
### རྣམ་པ་བཅུ་དྲུག། ^7-3-0

[Block 3777 [VERSE]]
འདོད་པའི་ཁམས་ཀྱི་རྗེས་མ་ཡིན། །
ཤེས་པ་བཅུ་པོ་དེ་དག་ལས། །
ཆོས་ཤེས་པ་དང་རྗེས་སུ་ཤེས། །

[Block 3778]
རྣམ་པ་བཅུ་དྲུག །དེ་དག་ནི་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 3779]
ཀུན་རྫོབ་ནི། དེ་བཞིན་གཞན་དུ་འོང་།[^1490] རྣམ་པ་བཅུ་དྲུག་དང་ལྡན་པ་ཡང་ཡིན་ལ། གཞན་གྱི་རྣམ་པ་ཅན་ཡང་ཡིན་ཏེ། ཆོས་ཐམས་ཅད་ཀྱི་རང་དང་སྤྱིའི་མཚན་ཉིད་ལ་སོགས་པ་འཛིན་པའི་ཕྱིར་རོ། །

[Block 3780]
རང་རང་གི་བདེན་པའི་རྣམ་པས་བཞི་ཡིན་ནོ། །

[Block 3781]
སྡུག་བསྔལ་གྱི་བདེན་པ་ལ་སོགས་པ་རྣམས་ནི་རང་རང་གི་བདེན་པའི་རྣམ་པ་དག་ཏུ་འཇུག་པ་རེ་རེ་ཞིང་རྣམ་པ་བཞི་བཞི་ཡིན་ནོ། །

[Block 3782]
ཕ་རོལ་ཡིད་ཤེས་དྲི་མེད་ཀྱང་། །དེ་བཞིན་རྣམ་པ་བཞི་དང་ལྡན་པ་ཡིན་ཏེ། ལམ་ཤེས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3783]
དྲི་མ་དང་བཅས་ནི། ཤེས་བྱའི་རང་གི་མཚན་ཉིད་རྣམ། །ཟག་པ་དང་བཅས་པ་ནི་ཤེས་བྱ་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱི་རང་གི་མཚན་ཉིད་གང་ཡིན་པ་དེ་ནི་རྣམ་པ་འཛིན་པའོ། །

[Block 3784]
གཉིས་ཀ་ཡང་། རྫས་རེ་རེ་ཞིག་སྤྱོད་ཡུལ་ལོ། །

[Block 3785]
གང་གི་ཚེ་སེམས་འཛིན་པ་དེའི་ཚེ་སེམས་ལས་བྱུང་བ་རྣམས་མི་འཛིན་ལ། གང་གི་ཚེ་ཚོར་བ་འཛིན་པ་དེའི་ཚེ་འདུ་ཤེས་མི་འཛིན་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །
--- END BLOCKS ---
