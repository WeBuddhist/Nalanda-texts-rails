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
[Block 631]
སློབ་དཔོན་ཞི་བའི་ལྷས་ནི་མདོ་སྡེ་མ་ལུས་པ་གང་ཟག་གསུམ་གྱི་བསླབ་པ་མཛད་དེ། འདི་ལྟར་ཐེག་པ་ཆེན་པོ་ལ་གོམས་པ་ཆེ་བ་དང་། གོམས་པ་འབྲིང་དང་། གོམས་པ་ཆུང་བའོ། །

[Block 632]
གོམས་པ་ཆེ་བའི་དབང་དུ་མཛད་ནས་བསླབ་པ་ཀུན་ལས་བཏུས་པ་ནས།

[Block 633 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པ་ནི། །
རྒྱས་པར་ཐེག་པ་ཆེ་ལས་འབྱུང་། །

[Block 634]
ཞེས་འབྱུང་བ་དང་། སྤྱོད་འཇུག་ལས་ཀྱང་།

[Block 635]
རྒྱལ་སྲས་རྣམས་ཀྱིས༌[^356]མི་བསླབ་པ། །འགའ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །ཞེས་གསུངས་སོ། །

[Block 636]
བླ་མ་དཔལ་བྱང་ཆུབ་བཟང་པོའི་ཞལ་ནས་ཀྱང་། འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བསླབ་པའི་གཞི་རྣམས་དངོས་སུ་བྱུང་བ་འདི་དག་ནི་མདོར་བསྡུས་པ་སྟེ། གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་དག་གི་བསླབ་པ་ནི་དཔག་ཏུ་མེད་ཅིང་མཐར་ཐུག་པ་མེད་པའི་ཕྱིར། དེ་དང་དེ་དག་ཏུ་བསྟན་པའི་རྗེས་སུ་འབྲངས་ནས་ཉེས་པར་འགྱུར་བ་དང་། ཉེས་པར་མི་འགྱུར་བ་དག་རིག་པར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 637]
དེ་ལ་གོམས་པ་འབྲིང་པོའི་དབང་དུ་མཛད་ནས་ཡང་བསླབ་པ་ཀུན་ལས་བཏུས་པ་ནས་གང་གིས་ལྟུང་བར་མི་འགྱུར་བའི།

[Block 638 [VERSE]]
གནད་ཀྱི་གནས་རྣམས་འདིས་རིག་བྱ། །
བདག་གི༌[^357]ལུས་དང་ལོངས་སྤྱོད་དང་། །
དུས་གསུམ་སྐྱེས་པའི་དགེ་བ་རྣམས། །
སེམས་ཅན་ཀུན་ལ་བཏང་བ་དང་། །

[Block 639]
དེ་བསྲུང་དག་པ་སྤེལ་བའོ། །ཞེས་གསུངས་སོ། །

[Block 640]
གོམས་པ་ཆུང་བའི་དབང་དུ་མཛད་ན༌[^358]ཡང་དེ་ཉིད་ལས་དེ་བས་ན་བྱང་ཆུབ་སེམས་དཔའ་སངས་རྒྱས་ཀྱི་སྤྱན་སྔར་བསླབ་པ་རྣམས་ཀྱི་ནང་ནས་བསླབ༌[^359]པ་གང་ཡང་རུང་བ་སྲུང་བར་འདོད་ནས་ཡི་དམ་བཅའ་བར་བྱེད་དོ། །

[Block 641]
དགེ་བའི་བཤེས་གཉེན་མེད་ན་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའི་སྤྱན་སྔར་རང་གི་ནུས་པ་དང་སྦྱར་ནས་སྡོམ་པ་འཛིན་ནོ། །

[Block 642]
དེ་བས་ན་རང་གི་ནུས་པ་དང་སྦྱར་ནས་བསླབ་པ་གཅིག་ཙམ་ཡང་ཡང་དག་པར་བླངས་ལ་བསྲུང་བར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 643 [HEADING]]
### སྡོམ་པ་གཏོང་བའི་རྒྱུ། ^6-3-0

[Block 644]
དེ་ལ་སྡོམ་པ་གཏོང་བའི་རྒྱུ་ནི་འཕགས་པ་ཐོགས་མེད་ཀྱི་ལུགས་ཀྱིས་ནི་འདི་ལྟར་བྱང་ཆུབ་ཆེན་པོར་སྨོན་ལམ་བཏབ་པ་བཏང་བ་དང་། ཀུན་ནས་དཀྲིས་པ༌[^360]ཆེན་པོས་ཕམ་པ་བྱུང་བའོ། །

[Block 645]
དེ་ལ་སྔ་མ་ནི་སེམས་ཅན་གྱི་དོན་ལ་སྐྱོ་བ་དང་། བྱང་ཆུབ་ཐག་རིང་བར་སེམས་པ་དང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་ཕྱིར་རོལ༌[^361]པར་སྨོན་པ་སྐྱེས་པའོ། །

[Block 646]
དེ་ལ་ཕྱི་མ་ཡང་ངོ་ཚ་བ་དང་ཁྲེལ་ཡོད༌[^362]པར་གྱུར་ཅིང་དེ་ལ་འགྱོད་པ་མེད་པར་སེམས་ཀྱིས༌[^363]བཏང་བ་དང་། མི་བརྡ་ཕྲད་པའི་དྲུང་དུ་བསླབ་པའི་གཞི་ཕུལ་བའོ། །

[Block 647]
སློབ་དཔོན་ཞི་བ་ལྷའི་ལུགས་ནི་བསླབ་པ་ཀུན་ལས་བཏུས་པའི་བདུད་ཀྱི་ལས་གནོད་པ་དང་། དམ་པའི་ཆོས་མི་འཛིན་པའི་གནོད་པ་ལ་སོགས་པ་བཅུ་བཞི་པོ་རྣམས་མི་སྤོང་བ་དང་། ཡང་ན་དྲན་པ་ཉམས་པ་དང་ལེ་ལོ་དང་བག་མེད་པ་དང་ལྟུང་བ་ལ་མི་མཁས་པ་དང་ངོ་ཚ་མེད་པ་དང་ཁྲེལ་མེད་པའོ། །

[Block 648]
བླ་མའི་ཞལ་ནས་ནི་བསླབ་པའི་གཞི་རྣམས་ལ་མི་མཁས་པ་དང་། དྲན་པ་མེད་པ་དང་འཁྲུལ་པ་དང་མ་གུས་པའོ་ཞེས་སྡོམ་པ་ཉི་ཤུ་པའི་འགྲེལ་པ་ལས་གསུངས་སོ། །

[Block 649 [HEADING]]
### ལྟུང་བ་མི་འབྱུང་བའི་རྒྱུ། ^6-4-0

[Block 650]
དེ་ལ་ལྟུང་བ་མི་འབྱུང་བའི་རྒྱུ་ནི། འཕགས་པ་ཐོགས་མེད་ཀྱི་ལུགས་ནི་འདི་ལྟར་ཤེས་བཞིན་དང་དྲན་པ་དང་། བརྩོན་འགྲུས་དང་། བག་ཡོད་པ་དང་། ཉེས་པ་དང་ཉེས་པ་མེད་པ་ཤེས་པ་དང་། ངོ་ཚ་བ་དང་ཁྲེལ་ཡོད་པའོ། །

[Block 651]
སློབ་དཔོན་ཞི་བའི་ལྷའི་ཡང་དེ་དག་ཐུན་མོང་བ་ཉིད་ལས་གནོད་པ་བཅུ་བཞིས༌[^364]སེལ་ཞིང་སྤོང་བའོ། །

[Block 652]
སླར་གསོ་བ་དང་། ཐོག་མ་ཉིད་ནས་འགལ་བར་མི་བྱེད་པ་ནི་འགྱོད་པ་མེད་པ་ཡིན་ནོ། །

[Block 653]
ཉེས་པ་ལ་ཉེས་པར་མཐོང་ན་སྲབ་པར་བྱེད་ལ། དེ་ཉིད་མཐོལ་ཞིང་བཤགས་ན་བྱང་བར་འགྱུར་རོ་ཞེས་ཀྱང་བླ་མ་དག་གསུང་ངོ་། །

[Block 654 [HEADING]]
### ལྟུང་བ་ལས་ལྡང་བ། ^6-5-0

[Block 655]
འཕགས་པ་ཐོགས་མེད་ཀྱི་ལུགས་ཀྱིས་ནི་འདི་ལྟར། ལྟུང་བ་ལས་ལྡང་བ་ནི་ཚུལ་ཁྲིམས་ཀྱི་ལེའུ་ལས་གལ་ཏེ་སློབ་དཔོན་དུ་རུང་བའི་གང་ཟག་མེད་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་དང་། ཡང་ཀུན་ནས་དཀྲིས་པ་ཆེན་པོའི་ཕམ་པ་བྱུང་ན། དེས་དགེ་འདུན་གྱི་མདུན་དུ་བཤགས་ལ་སྡོམ་པ་སླར་མནོད་པར༌[^365]བྱའོ། །

[Block 656]
ཉེས་བྱས་ནི་ཉན་ཐོས་སམ། ཐེག་པ་ཆེན་པོ༌[^366]གང་ཡང་རུང་བ་ལ་བཤགས་སོ། །

[Block 657]
སློབ་དཔོན་ཞི་བའི་ལྷས་ནི་བསླབ་པ་ཀུན་ལས་བཏུས་པར།

[Block 658]
རྫོགས་སངས་རྒྱས་ཀྱིས་གསུངས་ཚུལ་དུ། །འབད་པ་མེད་ན་ངན་སོང་འགྲོ། །ཞེས་པའི་སྐབས་སུ། འཕགས་པ་ཆོས་བཞི་པའི་མདོའི་དོན་བཤད་པའི་སྐབས་ན༌[^367]གསལ་བར་བཀོད་དོ། །

[Block 659 [HEADING]]
### ཚུལ་ཁྲིམས་ཀྱི་ཕན་ཡོན། ^6-6-0

[Block 660]
ཚུལ་ཁྲིམས་ཀྱི་ཕན་ཡོན་ནི་ཇི་སྐད་དུ་ཚུལ་ཁྲིམས་ཀྱི་ལེའུ་ལས་དེ་ལྟར་བྱང་ཆུབ་སེམས་དཔའི་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་ཆེན་པོ་འདི་ནི་བྱང་ཆུབ་ཆེན་པོའི་འབྲས་བུ་བསྐྱེད་པ་སྟེ། འདི་ལ་བརྟེན་ནས་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པར་བྱས་ནས་མངོན་པར་འཚང་རྒྱའོ། །

[Block 661]
ཇི་སྲིད་སངས་མ་རྒྱས་ཀྱི་བར་དུ་ཡང་ཕན་ཡོན་ལྔ་ཐོབ་པར་འགྱུར་ཏེ་སངས་རྒྱས་ཀྱིས༌[^368]དགོངས་པར་འགྱུར་བ་དང་། མཆོག་ཏུ་དགའ་བ་ཆེན་པོ་ལ་གནས་བཞིན་དུ་འཆི་བའི་དུས་བྱེད་པ་དང་། ཚེ་ཕྱི་མ་ལ་ཡང་ཆོས་མཐུན་པའི་དགེ་བའི་བཤེས་གཉེན་གནས་པ་དེར་སྐྱེ་བ་དང་། ཚེ་འདི་ལ་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྫོགས་པར་བྱེད་པའི་བསོད་ནམས་ཀྱི་ཕུང་པོ་ཚད་མེད་པ་དང་ལྡན་པར་འགྱུར་བ་དང་། ཚེ་ཕྱི་མ་ཡང་རང་འཁྲུངས་ཀྱི་ཚུལ་ཁྲིམས་དེ་དང་དེ་ཉིད་འཐོབ་པར་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 662]
བསླབ་པ་ཀུན་ལས་བཏུས་པ་ནས་ཀྱང་འདི་སྐད་དུ། དེང་སང་གི་དུས་ན་བསླབ་པ་བསྲུང་བ་ནི་ཤིན་ཏུ་ཕན་ཡོན་ཆེ་བས་དེ་ལ་བརྩོན་པར་རིགས་སོ་ཞེས་གསུངས་ཏེ། དེ་ཡང་འཕགས་པ་ལྷག་པའི་བསམ་པ་བསྐུལ་བ་དང་། རབ་ཏུ་ཞི་བ་ཆོ་འཕྲུལ་དང་། ཟླ་བ་སྒྲོན་མ་དང་། དཀོན་མཆོག་སྤྲིན་གྱི་མདོ་རྣམས་དེར་བཀོད་པ་ཡིན་ནོ། །

[Block 663]
བླ་མའི་ཞལ་ནས་ཀྱང་དེ་ལྟར་ན་འདི་ནི་དེའི་མོད་ལ་ངན་སོང་དུ་འགྲོ་བ་རྣམ༌[^369]བཅད་ཅིང་སྐྱེ་བར་འགྱུར་བ༌[^370]མ་ཡིན་ནོ་ཞེས་པ་དང་། ཡང་དེ་ནི་ངན་སོང་དུ་སྐྱེ་བ་མ་ཡིན་ལ། བརྒྱ་ལ་སྐྱེས་ན་ཡང་སྡུག་བསྔལ་དྲག་པོ་མི་མྱོང་བ་དང་། མྱུར་དུ་ཐར་བ་དང་། དེར་གནས་པ་ན་ཡང་གཞན་ཡོངས་སུ་སྨིན་པར་བྱེད་དོ་ཞེས་སྡོམ་པ་ཉི་ཤུ་པའི་འགྲེལ་པ་ལས་གསུངས་སོ། །

[Block 664]
སྡོམ་པ་ཡང་དག་པར་བླངས་པ་དེ་ལ་ཕན་ཡོན་གཞན་ཡོད་དེ། འཕགས་པ་ཙན་དྲ་གོ་མིའི་ཞལ་ནས།

[Block 665 [VERSE]]
དེ་ཚེ་དེ་ལ་དགེ་བའི་ཕྱིར།[^371] །
སངས་རྒྱས་སྲས་དང་བཅས་རྣམས་ཀྱིས། །
དགེ་བའི་ཐུགས་ཀྱིས༌[^372]རྟག་པར་ཡང་། །
བུ་སྡུག་འདྲ་བར་དགོངས་པར་འགྱུར། །

[Block 666]
ཞེས་གསུངས་པ་དང་། ཡང་སློབ་དཔོན་ཞི་བ་ལྷའི་ཞལ་ནས་ཀྱང་།

[Block 667 [VERSE]]
དེ་རིང་སངས་རྒྱས་རིགས་སུ་སྐྱེས། །
སངས་རྒྱས་སྲས་སུ་བདག་གྱུར་ཏོ། །
རིགས་དང་མཐུན་པའི་ལས་བརྩམས་ཏེ།[^373] །
སྐྱོན་མེད་བཙུན་པའི་རིགས་འདི་ལ། །

[Block 668]
རྙོག་པར་མི་འགྱུར་དེ་ལྟར་བྱ། །ཞེས་གསུངས་པས། སྡོམ་པ་བླངས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེས་ཚུལ་ཁྲིམས་བསྲུང་ཞིང་སྤེལ་དགོས་པས།

[Block 669 [VERSE]]
རང་གི༌[^374]ལུས་ངག་སེམས་ནི་རྣམ་དག་རྒྱུ། །
འཇུག་པའི་སེམས་ཀྱིས་བདག་ཉིད་སྡོམ་གནས་པས།[^375] །

[Block 670]
ཞེས་སྨྲས་ཏེ།
--- END BLOCKS ---
