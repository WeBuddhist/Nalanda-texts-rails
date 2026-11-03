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
[Block 4131]
དེ་ལྟར་སྤངས་པར་གྱུར་ཟིན་པ་ནི། འབུལ་བར་བྱེད་ན་སྤངས་པར་སྨྲ་སྟེ། སྦྱིན་པར་བྱེད་པའི་སེམས་བསྡུ་བར་རྗེས་སུ་བསྒྲུབ་པ་ཁས་ལེན་པ་ལས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་འབུལ་བར་བྱེད་ན་ཞེས་བྱ་བ་ནི་ཞལ་ཏ་བྱེད་པས་སོ། །

[Block 4132]
སྤངས་པ་སྨྲ་ཏེ༌[^2832]ཞེས་བྱ་བ་ནི། སྦྱིན་བདག་ལ་སླར་སྦྱིན་པ་ཉིད་འདི་ལ་ཞེས་བྱ་བ་འདིས་བསྡུས་པའོ། །

[Block 4133]
གཞན་བསྐུལ་བ་ལ་གནས་ཀྱི་ཁས་བླངས་པ་ལའོ། །

[Block 4134]
བསྐུལ་བ་ལ་ཡང་གཞན་སྒོ་གསུམ་ལས་གནས་དང་ཕྱོགས་ལ་སྒོ་གསུམ་ལས་གཞན་དུ་ཁས་མི་ལེན་པ་ལ་ཡང་ཁས་བླངས་པ་ཉིད་ལ་སྦྱིན་པར་བྱེད་པ་ནི། སེམས་བསྡུ་བར་རྗེས་སུ་བསྒྲུབ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4135]
འདིར་འཇུག་པ་ནི་གཙོ་བོ་སྟེ་རིམ་པས་ནི་མ་ཡིན་ནོ། །

[Block 4136]
དེ་བས་ན་སྔར་གནས་པ་དང་། ཕྱིས་བསྐུལ་བ་ཞེས་བྱ་བ་དབང་དུ་བྱ་བ་འདི་དག་ལ་འདྲེན་མར་བྱས་པ་ཉིད་དོ། །

[Block 4137]
བསྐུལ་བས་ཤེས་པར༌[^2833]གྱུར་པ་ཉིད་ལྷག་པའི་གནས་ལ་མ་ཆོག་པ་ཉིད༌[^2834]ཀྱི་ཕྱིར་འདི་ལ་བསྐུལ་བས་ཤེས་པར་བྱ་བ་རིག་པར་བྱའོ། །

[Block 4138]
ཅི་སླར་འདིས་དངོས་གཞིའི་རྗེས་སུ་བསྒྲུབ་པ་འདི་ལ་འདི་བརྗོད་པ་ལ་སྔར་གྱི་ཆར་གྱུར་པ་ཡོད་པ་ལ་གང་དུ་བྱེད་བཞིན་པའི་སྤང་བ་འདིས་ཤེ་ན། དེའི་ཕྱིར༌[^2835]ཁས་ལེན་པ་ལས་ཞེས་བྱ་བ་སྨོས་ཏེ། སྦྱིན་པར་བྱེད་པའི་སེམས་བཟུང་བ་ལ་རྗེས་སུ་བསྒྲུབ་པ་ནི་དེ་གང་གིས་ཁས་བླངས་པ་བརྗོད་པ་འདི་ལས་སུན་འབྱིན་པ་ལ་སོགས་པ་རྗེས་སུ་བསྒྲུབ་པས་སོ། །

[Block 4139]
རྗེས་སུ་བསྒྲུབ་པ་གང་ལ་བཟུང་བ་ལས་སྔོན་གྱི་ཆར་གྱུར་པ་ཡོད་པ་ལས་བསྐུལ་བའི་སྤང་བའི་དེའི་ཕྱིར་བླངས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་ལྟ་བུ་ཉིད་ལ་སྦྱིན་པ་པོ་དང་། ཕོ་ཉ་དང་། ཞལ་ཏ་བྱེད་པས་ཤེ་ན། དེའི་ཕྱིར་གསུམ་ཆར་མི་ཉིད་དང་། ཁྱིམ་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4140]
འདིར་གཞུང་ནི་མི་མ༌[^2836]ཡིན་པས་སྦྱིན་པར་བྱེད་ཅིང་མི་མ་ཡིན་པས་ཕོ་ཉ་བྱེད་ལ་མི་མ་ཡིན་པས་རུང་བར་བྱེད་ན་ཉེས་བྱས་ཀྱི་ལྟུང་བར་འགྱུར་རོ། །

[Block 4141]
མི་མ་ཡིན་པས་སྦྱིན་པར་བྱེད་ཅིང་མིའི་ཕོ་ཉ་དང་། མི་མ་ཡིན་པས་རུང་བར་བྱེད་ན་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 4142]
མི་མ་ཡིན་པས་སྦྱིན་པར་བྱེད་ཅིང་། མིའི་ཕོ་ཉ་དང་མི་མ་ཡིན་པས་རུང་བར་བྱེད་ན་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 4143]
མིས་སྦྱིན་པར་བྱེད་ཅིང་མི་མ་ཡིན་པའི་ཕོ་ཉ་དང་། མི་མ་ཡིན་པས་རུང་བར་བྱེད་ན་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 4144]
མིས་སྦྱིན་པར་བྱེད་ཅིང་མིའི་ཕོ་ཉ་དང་མིས་རུང་བར་བྱེད་ན་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 4145]
མིས་སྦྱིན་པར་བྱེད་ཅིང་། མི་མ་ཡིན་པའི་ཕོ་ཉ་དང་མིས་རུང་བར་བྱེད་ན་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 4146]
མི་མ་ཡིན་པས་རུང་བར་བྱེད་ཅིང་མིའི་ཕོ་ཉ་དང་མིས་རུང་བར་བྱེད་ན་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 4147]
མིས་སྦྱིན་པར་བྱེད་ཅིང་མིའི་ཕོ་ཉ་དང་། མིས་རུང་བར་བྱེད་ན་ཡང་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ། །

[Block 4148 [VERSE]]
མི་མ་ཡིན་པས་གསུམ་གཅིག་དང་། །
གཉིས་པ་གསུམ་དུ་བྱས་པ་དང་། །
མི་ཡི་གཉིས་པ་གསུམ་དག་དང་། །
གསུམ་གཅིག་དེ་དག་མུ་བརྒྱད་དོ། །

[Block 4149]
མ་སྨྲས་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཕོ་ཉས་བྱུང་བའི་མཐའ་རྗེས་སུ་བརྗོད་པ་སྔར་བྱས་པ་མ་སྨྲས་པར་ཞལ་ཏ་བྱེད་པ་ལ་སྐུལ་བར་བྱེད་ན་དེ་ལས་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 4150]
མ་སྤངས་པ་ལའོ་ཞེས་བྱ་བ་ནི་རུང་བ་མ་ཡིན་པ་ཆོས་གོས་ཀྱི་རིན་ལ་སོགས་པ་བདག་ཅག་ནི་གོས་ཀྱི་རིན་དག་བླང་དུ་མི་རུང་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས༌[^2837]མ་སྤངས་པ་ལ་ཞལ་ཏ་བྱེད་པས་བསྐུལ་བ་བྱས་པ་དང་། ཕྱོགས་སུ་བསྡད་པས་གོས་སྦྱིན་པར་བྱེད་པ་མ་སྤངས་པར་ལེན་ན་ཉེས་བྱས་སོ། །

[Block 4151]
མ་དྲིས་པར་སྟོན་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་ཕོ་ཉས་མ་དྲིས་པ་ཉིད་ཞལ་ཏ་བྱེད་པ་ལ་སྟོན་ན༌[^2838]དེ་ལ་ཡང་ཉེས་བྱས་སོ། །

[Block 4152]
རེ་བ་རེ་བ་མེད་པ་ཉིད་ན་མ་སྦྲན་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རེ་བ་མེད་པ་ཉིད་ན་སྦྱིན་པར་བྱེད་པ་ལ་མ་སྦྲན་ན་ཡང་ཉེས་བྱས་སུ་འགྱུར་བའོ། །

[Block 4153]
འདི་ནི་འདི་རྣམས་མེད་པར་དངོས་གཞིར་གྱུར་པའི༌[^2839]སྤྱོད་པ་འབྲིང་པོར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་འདི་རྣམས་ལ་ཞེས་བྱ་བར་འདིའི་དོན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 4154]
གཞན་ཡང་བསྒྲུབ་པ་འདི་ཉིད་ནི༌[^2840]མི་མཐུན་པ་ཞེས་བྱ་བས་ན་འདི་རྣམས་མེད་ཀྱང་གོས་འཛིན་པ་ལ་ཉེས་པ་མེད་ཅེས་རིག་པར་བྱའོ། །

[Block 4155]
མ་བསླངས་པ་ཉིད་ཀྱིས་འདི་རྣམས་ལ་ཤིན་ཏུ་བསླངས་པ་ཉིད་ནི་འདིར་མཚན་མ་ཡིན་ཏེ། འདི་ལ༌[^2841]ཡང་གོ་བར་བྱ་བར་འོས་པའི་བསླབ་པའི་གཞི་ལ་སོགས་པ་བཞིན་དུ་བསླངས་པའི་བསླབ་པའི་གཞི་དང་འདྲ་བར་ལྷག་མར་གྱུར་པ་ཉིད་ནི་བསླབ་པའི་གཞི་སྟེ། དེའི་འོག་ཏུ་ཆོས་གོས་བསྒྲུབ་པའི་ཕྱིར་འབད་པར་བྱའོ། །

[Block 4156]
གོས་བསྒྲུབ་ན་སྤང་བའི་ལྟུང་བྱེད་ཅེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4157]
བསྐུར་བའི༌[^2842]སྤང་བ་རྣམས་སོ།། །།

[Block 4158]
སྟན་གཙང་བར༌[^2843]བྱའོ་ཞེས་བྱ་བ་ལ། སྟན་ནི་རྣམ་པ་གཉིས་ཏེ། ནང་ཚངས་ཅན་དང་། བླིངས་པའོ། །

[Block 4159]
སྤྱིར་སྟན་ཞེས་བྱ་བ་འདིས་གཉིས་ཀ་ཡང་བཟུང་བ་ཉིད་ཡིན་ནོ། །

[Block 4160]
ནང་ཚངས་ཅན་ཞེས་བྱ་བ་ནི་ཚིག་གིས་འདིར་ཕྱི་ཤུན་གྱི་རྫས་ཀྱང་རྗེས་སུ་གནང་བར་བསྒྲུབ་པར་རིག་པར་བྱའོ། །

[Block 4161]
འདིར་འདུག་པའི་རྣམ་གྲངས་ནི་འདིར་བརྗོད་པ་ཡིན་ཞེས་བྱ་བ་ཁ་ཅིག་གིས༌[^2844]རྣམ་པ་འདི་མི་བདེན་པར་འདུག་པ་ལ་དངོས་པོ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4162]
འདི་དག་ལ་ཡང་ཐ་དད་པ་ཉིད་ཀྱི་ཕྱིར་དོན་ལ་རིམ་པ་གཅིག་པ་དང་། རིམ་པ་གཉིས་པ་རྣམ་པར་གཞག་པས་གོས་གཉིས་པ་ཉིད་འདུག་པ་ལ་གོ་བར་གྱུར་པ་ནི་ཆས་འདུག་པ་བླངས་ནས་ཞེས་བྱ་བའི་ཚིག་གིས༌[^2845]མི་མཐུན་པ་ཆས་བླངས་ཏེ། སྟན་ནང་ཚངས་ཅན་དང་ཞེས་བྱ་བ་ལ་སྟན་ནི་གྲང་བའི་གཉེན་པོ་ཡིན་ནོ། །

[Block 4163]
འདི་ལྟར་འབྲོག་ཕྱོགས་དག་ཏུ་གྲང་བའི་གཉེན་པོ་ནི་འདིང༌[^2846]བའི་དགོས་པ་སྟེ། འདི་རྒྱུ་མཚན་དུ་རྗེས་སུ་གནང་བའི་ཕྱིར་རོ། །

[Block 4164]
གང་གི་ཕྱིར་དགོན་པ་ལ་གནས་པ་རྣམས་ལ་གྲང་བས་གནོད་པར་གྱུར་པ་རྣམས་ཀྱི་དབང་དུ་མཛད་ནས་འདི་རྗེས་སུ་གནང་བ་ཡིན་ལ་གདིང་བ་ནི་མལ་སྟན་ལ་གཡོགས་པའི༌[^2847]ཕྱིར་དང་། ཀུན་དུ་བསྲུང་བའི་ཕྱིར་གདིང་བའི་དགོས་པ་སྟེ། དེ་ལྟར་ན་འདིའི་གདིང་བ་ཞེས་བྱ་བ་རྣམ་པར་འབྱེད་པའོ། །

[Block 4165]
གདིང་བའི་ཚད་ནི་གང་ཞིག་སྟན་ལ་དེ་ཉིད་རིག་པར་བྱ་སྟེ་ཡུལ་འདྲ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4166]
གང་ཞིག་སྲིན་བལ་གྱི་སྤང་བ་ཞེ་ན། དེའི་ཕྱིར་སྲིན་བལ་གྱི་ལས་བྱས་སམ་བྱེད་དུ་བཅུག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱས་པ་འམ་བྱེད་དུ་བཅུག་པ་ལ་སྲིན་བལ་གྱི་གདིང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4167]
ཐམས་ཅད་པ་འམ་སོ་སོ་བ་བྱས་པ་འམ་བྱེད་དུ་བཅུག་པ་དག་ལ་ཉེས་པ་དང་ལྡན་པ་ཉིད་དོ། །

[Block 4168]
གང་ཞིག་གནས་པ་ལ་མཐར་ཐུག་པས་འཁོར་གསུམ་གཡོགས་པ་ཉིད་དོ། །

[Block 4169]
དེ་ཉིད་འདི་སྤང་བར་བྱེད་པ་ཉིད་ལ་རྟོགས་པར་བྱའོ།[^2848] །འདི་ཙམ་ཉིད་ཀྱིས་འདིར་ཡང་མཐར་ཐུག་པར་གྱུར་པའི་དོན་ལ་བཀྲམ་པ་ལ་སོགས་པ་སྟེ། གང་ཞིག་མཐར་ཐུག་པའི་གོས་རྙིང་པར་གྱུར་པ་རྣམས་ལ༌[^2849]བརྐུས་ན་ལོངས་སྤྱོད་པ་རྣམས་ནི་བལ་ལས་བྱས་པ་རྣམས་ལ་སྤང་བར་བྱེད་པ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4170]
འདི་རྣམས་ལ་ཐམས་ཅད་ཕྱི་མ་དག་ལ་ཉེས་བྱས་ཉིད་དེ་ཆུང་བ་ལ་ཡང་འདིར་འཇུག་པས་རྗེས་སུ་མཐུན་པ་ཉིད་ཀྱང་བྱི་དོར་ལ་སོགས་པའི་དོན་དེ་ལ་དེ་ཙམ་དུའོ། །
--- END BLOCKS ---
