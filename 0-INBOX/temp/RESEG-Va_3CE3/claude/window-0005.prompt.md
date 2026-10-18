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
[Block 176]
རྩོམ་པ་ཐམས་ཅད་ཀྱི་རྩ་བ་ནི་དེ་དག་ཡིན་པས་སེམས་ཅན་ཡོངས་སུ་མི་གཏོང་བ༌[^121]ཡིད་ལ་བྱེད་དོ། །

[Block 177]
བདག་གི་སྡུག་བསྔལ་གྱི་འདུ་ཤེས་རྣམ་པར་བཟློག་པའི་ཕྱིར་སྙིང་རྗེ་ཡིད་ལ་བྱེད་དོ། །

[Block 178]
གུས་པ་བསྐྱེད་པའི་ཕྱིར་བླ་མ་རྣམས་ལ་དད་པས་འཕངས་པར༌[^122]ཡིད་ལ་བྱེད་དོ། །

[Block 179]
བྱང་ཆུབ་ཀྱི་ཚོགས་ཀྱི་ཕྱིར་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡིད་ལ་བྱེད་དེ། ཡིད་ལ་བྱེད་པ་བརྒྱད་དོ། །

[Block 180]
དེ་བཞིན་དུ་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 181]
སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་བྱ་བའི་དགེ་བའི་རྩ་བ་བསྐྱེད༌[^123]ཅིང་ཡོངས་སུ་བསྔོ་བ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་འགྱུར་བའི་དགེ་བའི་རྩ་བ་རྣམས་བསྐྱེད་ནས་དགེ་བའི་རྩ་བ་འདིས་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་གྱུར་ཅིག་ཅེས་ཡོངས་སུ་བསྔོ་བའོ། །

[Block 182]
སངས་རྒྱས་ཀྱི་ཞིང་ཞེས་བྱ་བའི་དངོས་པོ་ནི་གང་ཡང་མེད་ཀྱི། བདག་དང་གཞན་དག་ལ། དེ་ལྟ་དེ་ལྟ་བུར་སྣང་བ་ཙམ་དུ་ཟད་པས། སེམས་ཅན་ཡོངས་སུ་སྦྱང་བ་ཉིད་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 183]
དགོན་པ་ལ་གནས་པ་ཡོངས་སུ་མི་གཏང་བ༌[^124]ཞེས་བྱ་བ་ལ་དགོན་པ་ལ་གནས་པ༌[^125]ཞེས་བྱ་བའི་སྒྲ་ནི་འདིར་ནགས་ཚལ་ན་གནས་པ་ལ་ནི་མི་བྱའི། སེམས་འདྲེ་བ་མེད་པར་གནས་པ་དང་། དབེན་པར་གནས་པ་ལ་འདིར་དགོན་པ་ལ་གནས་པ་ཞེས་བྱའོ། །

[Block 184]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་སེམས་འདྲེ་བ་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་དང་། རང་བྱང་ཆུབ་ཡིད་ལ་བྱེད་པའི་དབང་གིས་འགྱུར་ཏེ། ཇི་སྐད་དུ་རབ་འབྱོར་གང་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཉན་ཐོས་དང་། རང་སངས་རྒྱས་ཀྱི་ཡིད་ལ་བྱེད་པ་དང་མི་ལྡན་པར་དབེན་པར༌[^126]གནས་པ་འདི་ནི་རབ་འབྱོར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ༌[^127]དབེན་པ་ཡིན་པར་ངས་རྗེས་སུ་གནང་སྟེ། གལ་ཏེ་དབེན་པ་འདིས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཉིན་མཚན་དུ་གནས་ན་དབེན་པ་ཉིད་དུ་གནས་པའོ་ཞེས་འོག་ནས་བཤད་པ་ལྟ་བུའོ། །

[Block 185]
གཞན་ཡང༌[^128]དེ་དགོན་པ་དང༌[^129]ནགས་ཚལ་གྱི་ཕྱོགས་དང་། བས་མཐའི་གནས་ན་གནས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 186]
དེ་བཞིན་དུ་སྦྱངས་པའི་ཡོན་ཏན་ཞེས་བྱ་བའི་སྒྲ་ཡང་རྣམ་པར་རྟོག་པ་སྦྱོང་བའི༌[^130]རྒྱུར་གྱུར་པའི་ཡོན་ཏན་རྣམས་ལ་བྱའི། ཕྱག་དར་ཁྲོད་པ་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 187]
གང་ལ་བསླབ་པ་ཐམས་ཅད་རྒྱུ་བ་མེད་པ་སྟེ༌[^131]ཞེས་བྱ་བ་ནི་རྣམ་པར་མི་རྟོག་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པ་ལ་བྱའོ། །

[Block 188]
གང་ཆོས་ཐམས་ཅད་ལ་མངོན་པར་འདུ་བྱེད་པ་མེད་པ་ཞེས་བྱ་བ་ནི་གང་ཆོས་ཐམས་ཅད་ལ་གཡོ་བ་ཡོངས་སུ་བཏང་བའོ། །

[Block 189]
གང་རྣམ་པར་ཤེས་པ་གནས་པ་ལ་དེའི་སེམས་མི་སྦྱོར་བ་སྟེ་ཞེས་བྱ་བ་ནི་ཀུན་ཏུ་འདྲེ་བར་མི་འགྱུར་ཞིང་། བག་ལ་ཉལ་དུ་མི་འགྱུར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 190]
སངས་རྒྱས་སུ་ལྟ་བ་ལ་བརྟེན་པས་སངས་རྒྱས་མཐོང་བར་མི་འགྱུར་ཏེ༌[^132]ཞེས་བྱ་བ་ནི་སངས་རྒྱས་མཐོང་ངོ་སྙམ་ནས་སངས་རྒྱས་སུ་དམིགས་པའི་ལྟ་བས་སངས་རྒྱས་སུ་ལྟ་བ་ལ་གནས་པའི་ཕྱིར་སངས་རྒྱས་མཐོང་བ་མེད་དེ། མི་དམིགས་པའི་ཡེ་ཤེས་ཉིད་ཀྱིས་སངས་རྒྱས་མཐོང་ངོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 191]
ཆོས་དང་དགེ་འདུན་ལ་ཡང་དེ་བཞིན་ནོ། །

[Block 192]
འདི་ལྟར་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་ཀྱིས་སྟོང་པ་ནི་མ་ཡིན་གྱི། རང་གི་མཚན་ཉིད་ཀྱིས་སྟོང་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་འདི་ལྟར་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་གཟུགས་ལ་སོགས་པ་ཀུན་བརྟགས་པའི་མཚན་ཉིད་དུ་ནི་ཡོད་པ་མ་ཡིན་གྱི། བརྗོད་དུ་མེད་པའི་མཚན་ཉིད་དོན་དམ་པ་སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་དུ་ནི་མེད་པ༌[^133]མ་ཡིན་ཏེ། དེའི་ཕྱིར་སྟོང་པ་ཉིད་ལ་ཐམས་ཅད་ཆད་པར་ལྟ་བའི་རྒྱུ་ལས་བྱུང་བའི་འཇིགས་པར་མི་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 193]
རང་གི་མཚན་ཉིད་ཀྱིས་སྟོང་པ་ཉིད་སྟོང་པས། སྟོང་པ་ཉིད་ནི་སྟོང་པ་ཉིད་དང་འགལ་བར་མི་བྱེད་པའི་ཕྱིར་ཏེ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་སྟོང་པ་ཉིད་ཀྱང་སྟོང་པ་ཉིད་ཀྱི༌[^134]མཚན་ཉིད་ཀྱིས་སྟོང་པ་མ་ཡིན་ན། དེ་ལྟ་ན་ནི་མི་སྟོང་པའི་ཆོས་ཤིག་ཡོད་པར་གྱུར་པས་ཆོས་ཐམས་ཅད་སྟོང་ངོ་ཞེས་བྱ་བ་དང་། སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་འདི་འགལ་བའི་ཕྱིར་སྟོང་པ་ཉིད་འགལ་བར་འགྱུར་བ་ཞིག་ན་འདི་ལྟར་སྟོང་པ་ཉིད་ཀྱང་སྟོང་པ་ཉིད་ཅེས་བྱ་བའི་ཆོས་གཞན་དུ་གྱུར་པ་གང་ཡང་མེད་པས་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་ཀྱིས་སྟོང་པར་ཁས་ལེན་ཏེ། དེ་བས་ན་ཆོས་ཐམས་ཅད་སྟོང་ངོ་ཞེས་བྱ་བ་འགྲུབ་པའི་ཕྱིར་སྟོང་པ་ཉིད་ནི་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་དང་འགལ་བར་མི་བྱེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 194]
འདི་ལྟར་སྟོང་པ་ཉིད་ཀྱིས་སྟོང་པ་ཉིད་སྟོང་གི། སྟོང་པ་ཉིད་ལ་སྟོང་པ་ཉིད་རྟོགས་པར་མི་བྱེད་ཅེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་ལ་སྟོང་པ་ཉིད་གཉིས་པ་མེད་དེ། དེ་བས་ན་སྟོང་པ་ཉིད་གཉིས་པ་མེད་པའི་ཕྱིར་སྟོང་པ་ཉིད་ལ་སྟོང་པ་ཉིད་རྟོགས་པར་མི་བྱེད་དོ་ཞེས་བྱ་བར༌[^135]ཤེས་པ་གང་ཡིན་པ་དེ་དག་ཉིད་ཀྱིས༌[^136]སྟོང་པ་ཉིད་རྟོགས་པའོ། །

[Block 195]
འཁོར་གསུམ་ཡོངས་སུ་དག་པ་ཞེས་བྱ་བ་ནི་ལུས་དང་། ངག་དང་། ཡིད་ཀྱི་འཁོར་གསུམ་ཡོངས་སུ་དག་པའོ། །

[Block 196]
སེམས་ཅན་གྱི་ཞིང་ཡོངས་སུ་དག་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཐམས་ཅད་དེ་བཞིན་གཤེགས་པའི་སྙིང་པོ་ཉིད་ཡིན་པའི་ཕྱིར༌[^137]སེམས་ཅན་གྱི་ཞིང་ཡོངས་སུ་དག་པའོ། །

[Block 197]
བསྣན་པ་མེད་པ་དང་དབྲི་བ་མེད་པ་ཞེས་བྱ་བ་ལ། ཡོད་པ༌[^138]སྐུར་པ་མི་འདེབས་པ་ནི་དབྲི་བ་མེད་པའོ། །

[Block 198]
མེད་པ་སྒྲོ་མི་འདོགས་པ་ནི་བསྣན་པ་མེད་པ་སྟེ། ཡང་དག་པར་ཡོད་པ་ལ་སྐུར་པ་མི་འདེབས་པ་དང་། ཡང་དག་པར་མེད་པ་ལ་སྒྲོ་མི་འདོགས་པས་མཉམ་པ་ཉིད་དུ་མཐོང་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 199]
གང་ཆོས་ཐམས་ཅད་རབ་ཏུ་རྟོགས་པ་མེད་པ་ཞེས་བྱ་བ་ནི་རྟོགས་པར་བྱ་བ་དང་། རྟོགས་པར་བྱེད་པ་གཉི་ག་མ་མཐོང་བའི་ཕྱིར་རྟོགས་པ་མེད་པ་ཉིད་ཡང་དག་པའི་ཚུལ་རྟོགས་པའོ། །

[Block 200]
ཆོས་ཉིད༌[^139]ལ་ཀུན་ཏུ་སྤྱོད་པ་མེད་པ་ཉིད་དེ་ཚུལ་གཅིག་ཏུ་བསྟན་པའོ་ཞེས་བྱ་བ་ནི་དཔེར་ན་ནམ་མཁའ་གཅིག་པུའི་ངོ་བོ་ཡིན་པས། ངོ་བོ་ཉིད་ལ༌[^140]ཐ་དད་དུ་དབྱེ་བ་མེད་པ་དེ་བཞིན་དུ། དེ་བཞིན་ཉིད་ཀྱང་རྣམ་པ་གཅིག་པའི་ཕྱིར། ཡོད་པ་དང་མེད་པ་དང་། ཆོས་དང་། ཆོས་མ་ཡིན་པ་དང་། རྟག་པ་དང་། མི་རྟག་པ་ལ་སོགས་པའི་ཆོས་གཉིས༌[^141]ལ་ཀུན་ཏུ་སྤྱོད་པ་མེད་པས་ཚུལ་གཅིག་ཏུ་བསྟན་ཏོ། །

[Block 201]
ཉན་ཐོས་དང་རང་སངས་རྒྱས་རྣམས་ཀྱི་ལྟ་བ་རྣམས་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་རྣམས་ཀྱི་ལྟ་བ་མ་སྤངས་པའི་རྣམ་པར་རྟོག་པ་གང་ཡིན་པ་དེ་དག་ལ་བྱའོ། །

[Block 202]
གང༌[^142]དབང་པོ་དྲུག་པོ་དག་རབ་ཏུ་མི་འཕྲོ་བ་གང་ཡིན་པ་ཞེས་བྱ་བ་ནི་འགྲོ་བ་མེད་ཅིང་འདུ་བའོ། །ཤེས་པ༌[^143]ཐོགས་པ་མེད་པའི་ཡེ་ཤེས་ཀྱིས་རྗེས་སུ་ཆགས་པའི་ས་མ་ཡིན་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ནི་གང་རྗེས་སུ་ཆགས་པ་དང་། ཁོང་ཁྲོ་བ་དང་བྲལ་བའི་ཡེ་ཤེས་དེ༌[^144]གང་ཞེ་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 203]
གང་ཆོས་ལ་བསྙེན༌[^145]བཀུར་བ་སྟེ་ཞེས་བྱ་བ་ནི། སུས་ཆོས་མཐོང་བ་དེས་སངས་རྒྱས་མཐོང་ངོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 204]
བདག་དང་གཞན་གྱི་སེམས་ཅན་གྱི༌[^146]ཞིང་ཡོངས་སུ་སྦྱོང་བར་བྱེད་པའོ༌[^147]ཞེས་བྱ་བ་ནི་སེམས་ཅན་གྱི༌[^148]ཞིང་མ་གཏོགས་པར་སངས་རྒྱས་ཀྱི་ཞིང་ཞེས་བྱ་བ་གཞན་མེད་དེ། རྣམ་པར་རིག་པ་ཙམ་དུ་ཟད་པའི་ཕྱིར་རོ། །

[Block 205]
གང་རྣམ་པར་སྨིན་པའི་ཏིང་ངེ་འཛིན་ཞེས་བྱ་བ་ནི་ས་བརྒྱད་པ་ལ་རྩོལ་བ་མེད་པའི་ཕྱིར་དོན་དམ་པར་རྩོལ་བ་དང་བཅས་པའི་སྤྱོད་པའི་ས་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་ཏེ། དགེ་བའི་ཆོས་རྣམས་རྣམ་པར་སྨིན་པའི་བདག་ཉིད་དུ་གནས་སོ། །

[Block 206]
དེ་བས་ན་སྔོན་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་པའི་རྣམ་པར་སྨིན་པར་གྱུར་པའི་ཏིང་ངེ་འཛིན་རྣམས་ལྷུན་གྱིས་གྲུབ་པ་ཉིད་དུ་བྱང་ཆུབ་སེམས་དཔའ་ལ་ཉེ་བར་འདུ་སྟེ། དེ་བས་ན་མཉམ་པར་གཞག་པ་ཞེས་བྱའོ། །

[Block 207]
སྤོབས་པའི་ཀླུང་ནི་སྤོབས་པའི་རྒྱུན་དང་། ཚུལ་དང་། སྤོབས་པ་རྒྱུན་དུ་འབྱུང་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 208]
རྫུས་ཤིང་སྐྱེ་བ་སྟེ་ཞེས་བྱ་བ་ནི་ས་བརྒྱད་པ་ཡན་ཆད་ནི༌[^149]མངལ་ན་གནས་པ་མེད་དེ། སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱ་བའི་དོན་དུ་ནི་དེ་ལྟ་བུར་ཡང༌[^150]སྟོན་ཏོ། །

[Block 209]
དཀར་པོ་རྣམ་པར་མཐོང་བའི་ས་ཞེས་བྱ་བ་ནི་མོས་པས་སྤྱོད་པའི་སའོ། །

[Block 210]
རིགས་ཀྱི་ས་ཞེས་བྱ་བ་ནི་བཟོད་པ་ཆེན་པོའི་སའོ། །

[Block 211]
བརྒྱད་པའི་ས་ཞེས་བྱ་བ་ནི་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་འཇུག་པའི་ས་སྟེ། དེ་ནི་དགྲ་བཅོམ་པའི་འབྲས་བུ་ལ་གནས་པ་ནས་བཟུང་སྟེ་བགྲངས་ནས་བརྒྱད་པར་འགྱུར་རོ། །

[Block 212]
མཐོང་བའི་ས་ཞེས་བྱ་བ་ནི་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་གནས་པའི་སའོ། །

[Block 213]
བསྲབས་པའི་ས་ཞེས་བྱ་བ་ནི་ལན་ཅིག་ཕྱིར་འོང་བའི་ས་སྟེ། དེའི༌[^151]འདོད་པའི་འདོད་ཆགས་ལ་སོགས་པ་སྲབ་མོར་བྱས་པ་ཙམ་དུ་ཟད་དོ། །

[Block 214]
འདོད་ཆགས་དང་བྲལ་བའི་ས་ནི་ཕྱིར་མི་འོང་བ་སྟེ།[^152] དེས་འདོད་པ་ལ་འདུན་པ་དང་གནོད་སེམས་ཡང་དག་པར་བཅད་པ་དང༌[^153]འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བ་ཡིན་ནོ། །

[Block 215]
བྱས་པ་རྟོགས་པ་ཅན་གྱི་ས་ནི་དགྲ་བཅོམ་པ་ཉིད་དེ། བྱ་བ་བྱས་སོ་ཞེས་ཁོང་དུ་ཆུད་པ་ནི་བྱས་པ་རྟོགས་པ་སྟེ། དེ་འདི་ལ་ཡོད་པས་ན་བྱས་པ་རྟོགས་པ་ཅན་ཞེས་བྱ་སྟེ་དགྲ་བཅོམ་པའོ། །
--- END BLOCKS ---
