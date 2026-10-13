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
[Block 246]
བཟང་པོ་སྤྱོད་པ་དག་ནི་རབ་སྟོན་ཅིང་། །ཞེས་བྱ་བ་ལ་འདིར་བཟང་པོ་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་དམ་པའི་ཆོས་འཆད་པ་ཉིད་གཟུང༌[^118]སྟེ་ཐབས་ཀྱིས༌[^119]སྒྲོ་བཏགས་པ་དང་། འཆད་པ་དང་། སྟོན་པའོ། །

[Block 247]
མ་འོངས་བསྐལ་པ་ཀུན་དུ་སྤྱོད་པར་གྱུར། །ཅེས་བྱ་བ་ནི་མ་འོངས་པའི་བསྐལ་པ་མཐའ་ཡས་པ་ཐམས་ཅད་དུ་མི་སྐྱོ་བའི་ཡིད་ཀྱིས་སྤྱོད་པའོ། །

[Block 248 [HEADING]]
#### སྐལ་བ་མཐུན་པའི་བྱང་ཆུབ་སེམས་དཔའ་བསྟེན་པ། ^2-8-6-0

[Block 249]
ལུས་དང་ངག་དང་ཡིད་ཀྱི༌[^120]སྤྱོད་པ་དང་། སྨོན་ལམ་གྱིས་སྐལ་བ༌[^121]མཉམ་པའི་བྱང་ཆུབ་སེམས་དཔའ་དང་མཐུན་པར་བསྟན་པ༌[^122]སྟེ་དེ་ནི་རྣམ་པ་དྲུག་པའོ། །དེ་ཡང་གང་ཞེ་ན། བདག་གི་སྤྱོད་དང་མཚུངས་པར་གང་སྤྱོད་པ། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 250]
བདག་གི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་དང་མཐུན་པར་གང་སྤྱོད་པ་དེ་དག་དང་རྟག་པར་ནམ་བྱང་ཆུབ་པའི་བར་དུ་འགྲོགས་པ་དང་། ལུས་དང་ངག་དང་ཡིད་ཀྱིས་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་དང་། སྨོན་ལམ་དེ་དང་ལྷན་ཅིག་ཏུ་སྤྱོད་པར་ཤོག་ཤིག༌[^123]པའོ། །

[Block 251 [HEADING]]
#### དགེ་བའི་བཤེས་གཉེན་མགུ་བར་བྱེད་པ། ^2-8-7-0

[Block 252]
ཕན་པར་བསམ་པའི་མན་ངག་སྒྲུབ་པ་ནི་དགེ་བའི་བཤེས་གཉེན་མགུ་བར་བྱེད་པ་སྟེ། དེ་ནི་རྣམ་པ་བདུན་པའོ། །དེ་ཡང་གང་ཞེ་ན། བདག་ལ་ཕན་པར་འདོད་པའི་གྲོགས་པོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 253]
དགེ་བའི་བཤེས་གཉེན་གང་ཕན་པར་འདོད་པས་བཟང་པོ་སྤྱོད་པ་སྟོན་པ་དང་། འཆད་པ་དང་། ཆོས་ཀྱི་གཏམ་ཟེར་བ༌[^124]དང་། བདག་རྟག་པར་ལྷན་ཅིག་ཏུ་མཚུངས་པར་སྤྱོད་པར་གྱུར་ཅིག་པའོ། །

[Block 254]
དེ་དག༌[^125]བདག་གིས་ནམས་ཀྱང་སྟེ༌[^126]གཞར་ཡང་ཡིད་དབྱུང་བར་མི་བྱ་སྟེ། ནམ་བྱང་ཆུབ་པའི་བར་དུ་རྟག་པར་དེ་དང་མཐུན་པར་གྱུར་ཅིག་པའོ། །

[Block 255 [HEADING]]
#### དེ་བཞིན་གཤེགས་པ་མངོན་སུམ་དུ་བྱ་བ། ^2-8-8-0

[Block 256]
དུས་དང་འཁོར་དང་མཆོད་པ་བྱ་བ་ལ་སྐྱོ་བ་མེད་པ་ནི་དེ་བཞིན་གཤེགས་པ་མངོན་དུ་བྱེད་པ་སྟེ་དེ་ནི་རྣམ་པ་བརྒྱད་པའོ། །དེ་ཡང་གང་ཞེ་ན། སངས་རྒྱས་སྲས་ཀྱིས་བསྐོར་བའི་མགོན་པོ་རྣམས། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 257]
མངོན་སུམ་ཞེས་བྱ་བ་ནི་མངོན་སུམ་དུ་བྱ་བ་སྟེ་ཕྱོགས་བཅུ་ཀུན་གྱིའོ། །

[Block 258]
རྒྱལ་བ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཏེ། བྱང་ཆུབ་སེམས་དཔའི་འཁོར་གྱིས་བསྐོར་བའོ། །

[Block 259]
མགོན་པོ་ཞེས་བྱ་བ་ནི་འགྲོ་བ་ཐམས་ཅད་ཀྱི་གཉེན་གཅིག་པུར་གྱུར་པའོ། །

[Block 260]
རྟག་ཏུ་བལྟ་ཞེས་བྱ་བ་ནི་སྐྱོན་མེད་པའི་མིག་གིས་སོ། །

[Block 261]
དེ་དག་ཀུན་རེ་རེ་ལ་ཡང་རྣམ་པ་ཐམས་ཅད་དང་ལྡན་པ་རྒྱ་ཆེན་པོ་ནམ་མཁའ་དང་མཉམ་པ་ཆོས་ཀྱི་དབྱིངས་ཀུན་དུ་ཁྱབ་པའི་མཆོད་པས་མཆོད་པར་བྱའོ། །ཇི་སྲིད་ཀྱི་བར་དུ་ཞེ་ན། མ་འོངས་བསྐལ་པ་ཀུན་དུ་མི་སྐྱོ་བར། །ཞེས་བྱ་བ་སྟེ། སྐྱོ་བ་མེད་པའི་ཡིད་ཀྱིས་མ་འོངས་པའི་བསྐལ་པ་ཐམས་ཅད་ཀྱི་མཐར་ཐུག་པའི་བར་དུའོ། །

[Block 262 [HEADING]]
#### དམ་པའི་ཆོས་ཡོངས་སུ་བསྡུ་བ། ^2-8-9-0

[Block 263]
འཛིན་པ་དང་། བཤད་པ༌[^127]དང་། ཡོངས་སུ་སྦྱང་བ་དང་གསུམ་ནི་དམ་པའི་ཆོས་ཡོངས་སུ་བསྡུ་བ་སྟེ་དེ་ནི་རྣམ་པ་དགུ་པའོ། །དེ་ཡང་གང་ཞེ་ན། རྒྱལ་བ་རྣམས་ཀྱི་དམ་པའི་ཆོས་འཛིན་ཅིང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་ནི༌[^128]དུས་གསུམ་དུ་གཤེགས་པའི་རྒྱལ་བ་ཐམས་ཅད་ཀྱི་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་པོ་བཤད་པའི་ཆོས་དེ་དག་གཟུངས་ཀྱི་སྟོབས་ཀྱིས་འཛིན་པས་ན་འཛིན་ཅིང་ཞེས་བྱ་བའོ།[^129] །

[Block 264]
བྱང་ཆུབ་སྤྱོད་པ་ནི་བསྒྲག་པར༌[^130]བྱ་བའི་ཆོས་ཉིད་དེ།[^131] ཀུན་དུ་སྣང་བར་བྱེད་ཅེས་བྱ་བ་ནི་འགྲོ་བ་རྣམས་ལ་ཡོངས་སུ་བསྒྲགས་ཤིང་རབ་ཏུ་བསྟན་པའོ། །

[Block 265]
བཟང་པོ་སྤྱོད་པ་རྣམ་པར་སྦྱང་བ་ཡང་། །ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པའོ། །

[Block 266]
དེ་རྣམས༌[^132]རྣམ་པར་སྦྱང་བ་ནི་དྲི་མ་མེད་པར་བྱ་བ་སྟེ།

[Block 267 [VERSE]]
ཉེས་པ་ཐམས་ཅད་རིང་དུ་སྤོང་བའོ། །
མ་འོངས་བསྐལ་པ༌[^133]ཀུན་དུ་སྤྱད་པར༌[^134]བགྱི། །

[Block 268]
ཞེས་བྱ་བ་ནི་དེ་ལྟར་བརྩལ་བའོ། །

[Block 269 [HEADING]]
#### མི་ཟད་པའི་མཛོད་རྙེད་པ། ^2-8-10-0

[Block 270]
བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ལ་སོགས་པའི་ཚོགས་ཐོབ་པས་མི་ཟད་པའི་མཛོད་རྙེད་པ་སྟེ་འདི་ནི་རྣམ་པ་བཅུ་པའོ། །དེ་ཡང་གང་ཞེ་ན། སྲིད་པ་ཐམས་ཅད་དུ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 271]
འདོད་པ་ལ་སོགས་པའི་སྲིད་པ་ཐམས་ཅད་ན་སེམས་ཅན་གྱི་དོན་དུ་འཁོར་བར་འཁོར་ཞིང་སྐྱེ་བར་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་མི་ཟད་པ་ཐོབ་པས་ལྡན་པར་གྱུར་ཅིག །དེ་ལྟར་ཤེས་རབ་དང་། ཐབས་དང་། ཏིང་ངེ་འཛིན་ནམ་མཁའི་མཛོད་དང་དྲི་མ་མེད་པའི་ཕྱག་རྒྱ་རྣམས་དང་། དེ་ལྟར་བྱང་ཆུབ་སེམས་དཔའི༌[^135]རྣམ་པར་ཐར་པ་འདི་ལྟ་སྟེ། སྙིང་རྗེ་ཆེན་པོ་ཐོགས་པ་མེད་པ་དང་། སྒྱུ་མར་གྱུར་པ་དང་། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའི་ཡོན་ཏན་ཐུན་མོང་བ་དང་། ཐུན་མོང་མ་ཡིན་པའི་མཛོད་མི་ཟད་པ་དང་། མི་ཟད་པའི་ཡོན་ཏན་གྱི་གཏེར་དུ་འགྲོ་བ་ཐམས་ཅད་ལ་བདེ་ཞིང་ཕན་པའི་ཕྱིར་གྱུར་ཅིག་པའོ། །

[Block 272 [HEADING]]
#### འཇུག་པར་བྱ་བ། ^2-8-11-0

[Block 273]
འཇུག་པ་ནི་རྣམ་པ་བཅུ་གཅིག་པ་སྟེ། དེ་ཡང་རྣམ་པ་བརྒྱད་དོ། །

[Block 274]
འདི་ལྟ་སྟེ། སངས་རྒྱས་དང་དེའི་ཞིང་བལྟ་བར་འཇུག་པ་རྣམ་པ་གཉིས་དང་། སངས་རྒྱས་ཀྱི་གསུང་ལ་འཇུག་པ་དང་། ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་འཇུག་པ་དང་། བསྐལ་པར་འཇུག་པ་དང་། དེ་བཞིན་གཤེགས་པ་ལ་བལྟ་བ་དང་།[^136] དེའི་སྤྱོད་ཡུལ་ལ་འཇུག་པ་དང་། སངས་རྒྱས་ཀྱི་ཞིང་མངོན་པར་སྒྲུབ་པར་འཇུག་པ་དང་། དེ་བཞིན་གཤེགས་པ་ལ་བསྙེན་བཀུར་བྱ་བར་འཇུག་པ་དང་བརྒྱད་དོ། །

[Block 275]
དེ་ལ་སངས་རྒྱས་དང་དེའི་ཞིང་བལྟ་བར་འཇུག་པ་རྣམ་པ་གཉིས་ནི་ཚིགས་བཅད་རྣམ་པ་གཉིས་ཀྱིས་ཏེ། དེ་ཡང་གང་ཞེ་ན། རྡུལ་གཅིག་སྟེང་ན་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 276]
རྡུལ་གཅིག་གི་སྟེང་དུ་ཕྱོགས་བཅུའི་དུས་གསུམ་དུ་གཤེགས་པའི་སངས་རྒྱས་ཀྱི་ཞིང་གི་རྡུལ་སྙེད་ཀྱི་སངས་རྒྱས་ཀྱི་ཞིང་རྣམས་ཏེ། ཞིང་དེར་ཞེས་བྱ་བ་ནི་ཞིང་དེ་དང་དེར་རོ། །

[Block 277]
བསམ་གྱིས་མི་ཁྱབ་ཅེས་བྱ་བ་ནི་བསམ་ཡས་པ་སྟེ། སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་སོ། །

[Block 278]
སངས་རྒྱས་སྲས་ཀྱི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིའོ། །

[Block 279]
དབུས་ན་བཞུགས་ཞེས་བྱ་བ་ནི་དབུས་ན་བཞུགས་པའོ། །

[Block 280]
བྱང་ཆུབ་སྤྱད་པ་སྤྱོད་ཅིང་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སྤྱད་པ༌[^137]སྤྱོད་ཅིང་སྤྱད༌[^138]པ་རབ་ཏུ་སྒྲུབ་པ་ནའོ། །

[Block 281]
བལྟ་བར་བགྱི་ཞེས་བྱ་བ་ནི་འཇུག་པའོ། །

[Block 282]
བྱང་ཆུབ་སེམས་དཔའི་སྨོན་ལམ་མི་སྲིད་པར་བཏབ་ན་དོན་མེད་པར་འགྱུར་རོ། །ཇི་ལྟ༌[^139]ཞེ་ན། འདི་ལྟ་སྟེ། སངས་རྒྱས་ཀྱི་ཞིང་གི་ཕྱོགས་ཆ་གཅིག་ཀྱང་རྡུལ་གཅིག་གི༌[^140]སྟེང་དུ་ཆུད་པར་བསྟན་མི་སྲིད་ན་ཇི་ལྟར་དུས་གསུམ་དུ་གཤེགས་པའི་སངས་རྒྱས་ཀྱི་ཞིང་གི་རྡུལ་སྙེད་ཀྱི༌[^141]སངས་རྒྱས་ཐམས་ཅད་ཀྱི་ཞིང་རེ་རེ་ན་ཡང་གྲངས་མེད་པའི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རེ་རེ༌[^142]ཡང་བྱང་ཆུབ་སེམས་དཔའི་འཁོར་གྱི་དབུས་ན་བཞུགས་པས་ཀུན་དུ་གང་བ་དེ་སྙེད་དུ་རྡུལ་གཅིག་གི་སྟེང་དུ་སོ་སོར་བལྟ་ཞིང་སྨོན་པ༌[^143]ཇི་ལྟར་བྱ་ཞེས་བརྒལ་བ༌[^144]དང་། དེ་ལྟར་མ་ཡིན་ཏེ། འདི་ལྟར་བསམ་གྱིས་མི་ཁྱབ་པའི་ལས་འཇིག་རྟེན་གྱི་ཁམས་སྣ་ཚོགས་པ་བླ་འོག་སྣྲེལ༌[^145]ཞི་ལ་སོགས་པ་སྤྲུལ་པ་བཞིན་ཏེ། དེ་ལྟར་བསམ་དུ་མེད་པའི་ཡེ་ཤེས་ཀྱིས་སྤྲུལ་ན་རྡུལ་གཅིག་གི་སྟེང་དུ་ཅིའི་ཕྱིར་མི་སྲིད་དེ། བསམ་གྱིས་མི་ཁྱབ་པར་ལུང་ལས་ཀྱང་བཤད་པ།

[Block 283 [VERSE]]
མཁས་པ་དག་གིས་ས་འདི་ལ། །
ངོ་མཚར་འགྱུར་བ་ཅུང་ཟད་མེད། །
སྒྱུ་མའི་རྣམ་པར་གྱུར་པ་ལ། །
ཡ་མཚན་དུ་ནི་སུ་ཞིག་འཛིན། །

[Block 284 [VERSE]]
བསམ་གཏན་ལས་དང་ཀླུ་རྣམས་དང་། །
སངས་རྒྱས་རྣམས་ཀྱི་ཆེ་བ་ཉིད། །
འཇིག་རྟེན་མགོན་པོ་འདྲེན་པ་དེས། །
བསམ་གྱིས་མི་ཁྱབ་རྣམ་བཞིར་བཤད། །

[Block 285]
དེ་ལྟ་བས་ན་སངས་རྒྱས་ཐམས་ཅད་ཀྱི་གསུང་རབ་ལ་མི་སྲིད་པར་འཛིན་པ་དེ་དག་ཀྱང་འདིས་ཡིད་ཆེས་པར་གྱིས་ཤིག །འཇིག་རྟེན་ན་ཡང་ཤིན་ཏུ་ཆུང་བའི་སྣོད་དུ་ཆུ་དངས་པས་གང༌[^146]བ་ལ། གཟའ་སྐར་ལ་སོགས་པ་ནམ་མཁའི་རྒྱན་ཐམས་ཅད་སྣང་བ་བཞིན་ནོ། །
--- END BLOCKS ---
