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
[Block 4901]
འགྱུར་བ་ཞེས་བྱ་བ་ནི་དྲིན་གཟོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4902]
དེའི་ཞེས་བྱ་བ༌[^3176]ནི་སྐྱེ་བོ་དམ་པ་འདིའི་དོན་ཏེ། དོན་འདི་གང་ཡིན་ཞེ་ན། སེམས་ཅན་འདི་ལྟ་བུ་ཞིག་གིས་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་བསྟན་པའོ། །

[Block 4903]
ཤ་བཟའ་བར་རུང་བས་ནི་བཟར་རུང་བའོ། །

[Block 4904]
རབ་ཏུ་ཆགས་པར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་གཟུགས་ཀྱི་ཡོན་ཏན་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 4905]
དེ་གཉི་གས་ཉམས་པར་འགྱུར་བ་ནི། སྙིང་རྗེ་ཆུང་བ་ཡིན་ཏེ། ངའི་ལུས་ནི་ཤ་བཟར་རུང་བ་དང་རབ་ཏུ་ཆགས་པར་འགྱུར་བ་ཡིན་ལ། མི་རྣམས་ཀྱི་སྙིང་ནི་རབ་ཏུ་ཆགས་པར་བྱེད་པའི་གཟུགས་ཡོད་པས་སོ། །

[Block 4906]
དེ་བས་ཞེས་བྱ་བ་ནི་ལུས་དང་། མི་རྣམས་ཀྱི་སྙིང་ཤེས་པར་བྱས་ནས་སོ། །

[Block 4907]
བདག་གི་ཡོན་ཏན་ཞེས་བྱ་བ་ནི་དྲིན་གཟོ་བ་ལ་སོགས་པའོ། །

[Block 4908]
འདིར་དེ་ལྟར་གནོད་པ་བྱེད་ན་དེའི་ཉེས་དམིགས་བསྟན་པའི་དབང་དུ་བྱས་ནས། མཛའ་བོ་དག་ལ་སྙིང་རིང་བ། །ཞེས་བྱ་བའི༌[^3177]ཚིགས་བཅད་ཀྱི་ཕྱེད་དེ། དེ་ལྟར་བྱས་ན་ཁྱོད་ཀྱི་ཡོན་ཏན་དང་། ང་ཡང་མ་བསྲུངས་པ་དེའི་ཉེས་དམིགས་སོ། །

[Block 4909]
ཁྱོད་ཀྱིས༌[^3178]བདག་མ་བསྲུངས་སོ་ཞེས་བརྗོད་པ་ན་འཁོན༌[^3179]དུ་གཟུང་བས༌[^3180]ནི་མི་དགའ་བར་སེམས་པའི་སྙིང་གང་ཡིན་པ་དེ་ནི་འཁོན༌[^3181]དུ་འཛིན་པའམ་སྙིང་མི་དགའ་བར་སེམས་པའོ། །

[Block 4910]
གཡོ་སྒྱུ་ཉིད་ཀྱི་ཕྱི་བཞག་ཡིན་པས། གཡོ་སྒྱུ་དང་ཕྱི་བཞག་སྟེ། མི་རྣམས་ཅི༌[^3182]ལ་གོམས་པ་མེད་པས་སོ། །

[Block 4911]
མི་རྣམས་ཀྱི་གཡོ་སྒྱུའི་ཕྱི་བཞག་ལ་མ་གོམས་པ་གང་ཡིན་པ་དེ་ནི་མིའི་གཡོ་སྒྱུ་དང་ཕྱི་བཞག་ལ་མ་གོམས་པའོ། །

[Block 4912]
གང་ན་གཡོ་སྒྱུ་དང་། ཕྱི་བཞག་ནི་གཡོ་སྒྱུ་དང་ཕྱི་བཞག་གོ། །

[Block 4913]
ཕྱི་བཞག་ནི་ལུས་དང་།

[Block 4914 [VERSE]]
ངག་གི་ལས་ཀྱི་མཚན་ཉིད་དོ། །
གཡོ་སྒྱུ་ནི་སེམས་གྱ༌[^3183]གྱུ་བའོ། །
ཚུལ་འཆོས་མཁས་པ་ཞེས་བྱ་བ་དང་།
དེ་ལྟའི་གཡོ་དག་བྱས་པའི་ཕྱིར། །

[Block 4915]
ཞེས་བྱ་བ་ནི་ཕྱི་བཞག་བཅོས་མ་ལ་མཁས་པ་སྟེ། གང་གིས༌[^3184]བསམ་པ་མ་དག་པའོ། །

[Block 4916]
རང་བཞིན་གྱིས་ནི་དུལ་བའི་སྐྱེ་བོ་རྣམས། །ཞེས་བྱ་བ་ནི་བསམ་པ་དག༌[^3185]སྤྱོད་པ་དང་ལྡན་པ་ཡིན་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4917]
རང་བཞིན་ནི་བསམ་པའོ། །

[Block 4918]
དུལ་བ་ནི་ལུས་དང་ངག་གི་ལས་དུལ་བའི་སྤྱོད་པ་ཉིད་དེ། བསམ་པ་དུལ་བར་གྱུར་པ་ནི་བསམ་པ་དུལ་བའོ། །

[Block 4919]
དོགས་པ་སྐྱེ་ཞེས་བྱ་བ་ནི་ཚུལ་འཆོས་དང་། ཕྱི་བཞག་སྤྱོད་པ་དེས་དོགས་པ་སྐྱེ་བའོ། །

[Block 4920]
ཡང་ན་གཡོ་སྒྱུ་དང་ཕྱི་བཞག་སྤྱོད་པ་དེས་སོ། །

[Block 4921]
ཐོ་རངས་ཀྱི་རྨི་ལམ་ཞེས་བྱ་བ་སྨོས་པས་ནི་དེའི་ཚེ་རྨི་ལམ་ངེས་པར་མཐོང་བའི་ཕྱིར་རོ། །

[Block 4922]
ཚིག་གསལ་ཞིང་སྡེབ་ལེགས་པ་གང་ཡིན་པ་དེ་ནི། ཚིག་གསལ་ཞིང་སྡེབ༌[^3186]ལེགས་པའོ། །

[Block 4923]
མིག་ཉིད་དཔལ་དང་ལྡན་པ་ཡིན་པས་མིག་དཔལ་ལྡན་ནོ། །

[Block 4924]
ངོ་མཚར་ཆེ་བས་བགྲད་པའི་མིག་གི་དཔལ་དང་ལྡན་པ་གང་ཡིན་པ་དེ་ནི་ངོ་མཚར་ཆེ་བས་མིག་བགྲད༌[^3187]དཔལ་ལྡན་ནོ། །

[Block 4925]
མཁུར༌[^3188]ཚོས་མཛེས་པའི་གཡོ་བ་གང་ཡིན་པ་དེ་ནི་མཁུར༌[^3189]ཚོས་མཛེས་པ་གཡོ་བཞིན་པའོ། །

[Block 4926]
དེས་ཞེས་བྱ་བ་ནི་རྨི་ལམ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 4927]
དེའི་ཞེས་བྱ་བ་ནི་དེའི་སྙིང་དགའ་བར་བྱ་བ་དང་། བདག་ཀྱང་རི་དགས་རིན་པོ་ཆེ་རྙེད་པར་འདོད་པའོ། །

[Block 4928 [VERSE]]
མཐོང་ཞེས་བྱ་བ་ནི་སྔོན༌[^3190]མཐོང་བའོ། །
བརྐམ་པ་དང་ནི་དེ་ཡིས་ཕན་བཏགས་པ། །

[Block 4929]
ཞེས་བྱ་བ་ནི་དབུལ་བའི་སྡུག་བསྔལ་གྱིས་ཡོངས་སུ་སྐྱོ་བ་དང་། བརྐམ་པ་དེ་ཡིས་དྲངས་པས་སོ། །

[Block 4930]
ཡོན་ཏན་ལ་ལྟ་ཞེས་བྱ་བ་ནི་བྱས་པ་གཟོ་བ་ལ་སོགས་པ་སྟེ་རི་དགས་མི་བསྟན་པའོ། །

[Block 4931]
འོན་ཏེ་འབྱོར་པ་ལ༌[^3191]ལྟ་ཞེས་བྱ་བ་ནི་རི་དགས་བསྟན་པས་སོ། །

[Block 4932]
དཔུང་ཐམས་ཅད་ཀྱིས་ཞེས་བྱ་བ་ནི་དམག་གི་ཚོགས་པ་ཐམས་ཅད་ཀྱིས་སོ། །

[Block 4933]
ནགས་ཚལ་སྟུག་པོ་དེའི་ནང་དུ་ཞུགས་སོ་ཞེས་བྱ་བ་ནི་གནོད་པ་དང་བཅས་པའི་ཆེད་དུའོ། །

[Block 4934]
དེའི་གནོད་པ་དེ་མེད་པའི་དབང་དུ་བྱས་ནས། ནགས་ཚལ་སྟུག་པོ་དེ་ཡང་དམག་གི་དཔུང་ཐམས་ཅད་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ཡིན་ནོ། །

[Block 4935]
དངོས་པོ་དེ་ལྟ་བུ་ལ་བརྟེན་པ་ཞེས་བྱ་བ་ནི་དེ་འདྲ་བ་ལ་སྟེ།

[Block 4936 [VERSE]]
འདིས་ནི་ཡོན་ཏན་གྱི་ཞིང་དུ་བསྟན་ཏོ། །
བྱ་བའི་ཁྱད་པར་དག་གིས་བཏང༌[^3192]ན་ནི། །

[Block 4937]
ཞེས་བྱ་བ་ནི་ཕན་འདོགས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4938]
གཉེན་པོ་ཆུང་ན་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དགེ་བའི་ལས་ཡིན་ན་དེའི་གཉེན་པོ་ནི་ཉོན་མོངས་པ་ཡིན་ཏེ་དེ་ཚུང་བའོ། །

[Block 4939]
གལ་ཏེ་མི་དགེ་བའི་ལས་ཡིན་ན་ནི་དེའི་གཉེན་པོ་དགེ་བ་ཡིན་ནོ། །

[Block 4940]
འདིར་གཉེན་པོ་ཞེས་དགོངས་པ་ནི་དགེ་བའི་ལས་ཉམ་ཆུང་བ་ལ་བྱའོ། །
--- END BLOCKS ---
