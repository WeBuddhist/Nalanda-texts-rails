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
[Block 106]
མི་འབྱིན་པའི་ཐབས་ནི་ལྷ་སྒོམ་པའོ། །

[Block 107]
རང་བཞིན་དག་པ་ནི་ལྟ་བ་གཉིས་སོ། །

[Block 108]
སོམ་ཉི་ཟ་བ་ནི་དེ་གཉིས་ཀྱི་རྟོག་པ༌[^66]མ་སྐྱེས་པའོ། །

[Block 109]
དེའི་བདག་ཉིད་དུ་རྟོག་པ༌[^67]མེད་པར་ཉིན་མཚན་འདས་ནའོ། །

[Block 110]
རྐྱེན་བླ་མ་དམ་པ་དང་བྲལ་བས་དངོས་པོར་ལྟ་བའི་དབང་གིས་སོ། །

[Block 111]
མི་འབྱིན་པའི་ཐབས་ནི་བླ་མ་དམ་པའི་ངག་ལ་བརྟེན་ནས་ལྟ་བ་གོམས་པར་བྱའོ། །

[Block 112]
གདུག་པ་ཅན་ནི་མི་དང་མི་མ་ཡིན་པ་རྣམས་སོ། །

[Block 113]
བདག་ལ་གནོད་པའི་དབང་གིས་ཞེ་སྡང་གིས་བསླང་ནས་ཕན་པ་མ་ཡིན་པ་དྲག་པོ་བྱེད་པ༌[^68]ཉིན་མཚན་འདས་ནའོ། །

[Block 114]
རྐྱེན་ནི་ཉེས་པར་བྱས་པའི་དབང་གིས་སོ། །

[Block 115]
མི་འབྱིན་པའི་ཐབས་ནི་བཟོད་པ་བསྒོམ་པ་སྟེ་བདུད་ཕྱིར་བཟློག་པའི་ལུང་ལས་ཤེས་པར་བྱའོ། །

[Block 116]
མིང་སོགས་བྲལ་བའི་ཆོས་ནི་འོད་གསལ་བ་དང་ཟུང་དུ་འཇུག་པའོ། །

[Block 117]
དེ་རྟོགས་པ༌[^69]ནི་དེ་གཉིས་ཀྱི་རང་བཞིན་དང་མི་མཐུན་པར་གཞན་དུ་རྟོགས་པས༌[^70]ཉིན་མཚན་འདས་པའོ། །

[Block 118]
རྐྱེན་ནི་དགེ་བའི་བཤེས༌[^71]གཉེན་དང་མ་ཕྲད་པའོ། །

[Block 119]
མི་འབྱིན་པའི་ཐབས་ནི་དེའི་གདམས་པ་ལས་སོ། །

[Block 120]
དད་ལྡན་ནི་ལམ་རིམ་གྱིས་མ་སྦྱངས་ཀྱང་གྲུབ་པར་གནས་པའི་དོན་ལ་འདོད་པའོ། །

[Block 121]
སུན་འབྱིན་པ་ནི་མ་བསྟན་པ་དང་ལོག་པར་བསྟན་པས་སོ། །

[Block 122]
རྐྱེན་ནི་མོས་པའི་གང་ཟག་དང་ཕྲད་པས་སོ། །

[Block 123]
མི་འབྱིན་པའི་ཐབས་ནི་རྟོག་པ་དང་སྦྱར་ཏེ་ཆོས་བསྟན་པའོ། །

[Block 124]
དམ་ཚིག་ནི་བཟའ་བའི་དམ་ཚིག་བདུད་རྩི་ལྔ་ལ་སོགས་པའོ། །

[Block 125]
མི་སྟོན་པ་ནི་མི་གཙང་བའི་བློས་དོར་ཏེ་དུས་འདས་པའོ། །

[Block 126]
རྐྱེན་ནི་རྫས་ཉེ་བར་གནས་པའོ། །

[Block 127]
མི་འབྱིན་པའི་ཐབས་ནི་མི་རྟོག་པའི་སེམས་ཀྱིས་སོ། །

[Block 128]
ཉེས་པ་འདི་རྣམས་ལྕི་ཡང་ཡོད་ཀྱང་གནོད་པ་ནི་འདྲའོ། །

[Block 129]
ཅིའི་ཕྱིར་ཞེ་ན་རྩ་བའི་ལྟུང་བ་ཡིན་པས་སོ། །

[Block 130 [VERSE]]
སྔགས་པས་འདི་དག་སྤངས་ནས་ནི། །
དངོས་གྲུབ་ངེས་པར་ཐོབ་པར་འགྱུར། །

[Block 131]
ཞེས་བྱ་བ་ནི་སྤང་བྱ་སྤངས་པའི་ཡོན་ཏན་ནོ། །

[Block 132 [VERSE]]
གཞན་དུ་དམ་ཚིག་ལས་ཉམས་ན། །
ཉམས་པས་བདུད་ཀྱིས་བཟུང་བར་འགྱུར། །
དེ་ནས་སྡུག་བསྔལ་མྱོང་འགྱུར་ཞིང་། །
ཐུར་དུ་བལྟས༌[^72]ཏེ་དམྱལ་བར་འགྲོ། །

[Block 133]
ཞེས་བྱ་བ་ནི་ཉམས་པའི་ཉེས་པ་མདོར་བསྡུས་པའོ། །

[Block 134 [VERSE]]
དེ་བས་ང་རྒྱལ་བཅོམ་ནས་ནི། །
བདག་ཉིད་མ་འཁྲུལ་ཤེས་པར་བྱ། །

[Block 135]
ཞེས་པ་ནི་བག་བྱ་བ་ལ་བསླབ་པའོ། །

[Block 136]
དབང་བསྐུར་ནས་ལྟུང་བ་བཅུ་བཞི་པ་དང་བླ་མ་ལྔ་བཅུ་གང་འདོད་པའི་སྒྲུབ་ཐབས་དག་ནི་དོན་རྒྱས་པར་སྟོན་པ་ཡིན་པས་ངེས་པར་ནན་ཏན་གྱིས་བསླབས་ཏེ་གཞན་དུ་ན་བླ་མའི་ཉེས་པའོ། །

[Block 137 [HEADING]]
## བཅུ་བཞི་པོ་བསྡུ་ན། ^3-0

[Block 138]
དེ་ལྟར་བཅུ་བཞི་པོ་བསྡུ་ན་གསུམ་སྟེ། ཐུན་མོང་གི་བྱང་ཆུབ་ཀྱི་སེམས་མི་ཉམས་པར་བྱེད་པ་དང་། ཁྱད་པར་གྱི་བྱང་ཆུབ་ཀྱི་སེམས་མི་ཉམས་པར་བྱེད་པ་དང་། དེ་གཉིས་ཀ་མི་ཉམས་པར་བྱེད་པའོ། །

[Block 139]
ལྟུང་བ་དང་པོ་དང་གཉིས་བ་ནི་གཉིས་ཀ་མི༌[^73]ཉམས་པར་བྱེད་པའོ། །

[Block 140]
སྤུན་ལ་དང་། བྱམས་སྤོང་དང་། བྱང་ཆུབ་སེམས་འདོར་དང་། གྲུབ་པའི་མཐའ་སྨོད་པ་དང་། གདུག་ལ༌[^74]བྱམས་པ་སྤོང་བ་སྟེ། ལྔ་པོ་དེ་དག་ནི་ཐུན་མོང་གི་སེམས་མི་ཉམས་པར་བྱེད་པ་སྟེ། དེ་བས་ན་འབད་པས་བསྲུང་ངོ་། །

[Block 141]
གསང་བ་སྒྲོགས་པ་དང་། ཕུང་པོ་སྨོད་པ་དང་།

[Block 142 [VERSE]]
དག་པའི་ཆོས་ལ་ཡིད་གཉིས་དང་། །
མིང་སོགས་བྲལ་ལ་དེར་རྟོག་དང་། །

[Block 143]
སེམས་སུན་འབྱིན་པ་དང་། དམ་ཚིག་མི་བསྟེན་པ་དང་། ཤེས་རབ་སྨོད་པ་དེ་རྣམས་སྤངས་པས་ཁྱད་པར་གྱི་བྱང་ཆུབ་ཀྱི་སེམས་མི་ཉམས་པར་བྱེད་པའོ། །

[Block 144]
ཡང་དེ་ནི་ལྟ་སྤྱོད་སྒོམ༌[^75]གསུམ་གྱི་རང་བཞིན་ཡང་ཡིན་ཏེ། ཆོས་ལ་ཡིད་གཉིས་དང་། མིང་སོགས་བྲལ་ལ་དེར་རྟོག་སྤངས་པས་ལྟ་བ་རྣམ་གཉིས༌[^76]རྟོགས་པའོ། །

[Block 145]
དང་པོ་དང་གཉིས་པ་དང་གསུམ་པ་དང་བཞི་པ་དང་ལྔ་པ་དང་དྲུག་པ་དང་བདུན་པ་དང་བརྒྱད་པ་དང༌[^77]བཅུ་པའི་དགུ་སྤངས་པས་སྒོམ་པའི༌[^78]མན་ངག་དང་། སེམས་སུན་འབྱིན་པ་དང་། དམ་ཚིག་མི་བསྟེན་པ༌[^79]དང་། ཤེས་རབ་སྨོད་པ་གསུམ་གྱིས༌[^80]དགུ་སྤངས་ཤིང་སྦྱངས་པས་སྤྱོད་པའོ། །
--- END BLOCKS ---
