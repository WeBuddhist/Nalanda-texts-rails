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
[Block 421 [VERSE]]
དེ་བཞིན་གྲུ་ཡི་བཙས༌[^319]རྣམས་དང་། །
ཞེས་པ་དང་ཡང་སྦྱར་བར་བྱའོ། །
སྲོག་ཆགས་རྐང་པ་མེད་པ་དང་། །
རྐང་མངས༌[^320]རྐང་གཉིས་རྐུ་བ་དང་། །

[Block 422 [VERSE]]
བརྟུལ་ཞུགས་ཅན་གྱིས༌[^321]མི་ཡི་ནོར། །
དབྱིག་ལ་སོགས་པ་གང་ཡང་རུང་། །
རྐུ་བའི༌[^322]སེམས་ཀྱིས་གང་བརྐུས་ཀྱང་། །
རིན་ཐང་ཚང་ན་སྡོམ་པ་ཞིག །

[Block 423]
ཅེས་བྱ་བ་ལ། མིའི་ལོངས་སྤྱོད་དགོས་པར་བྱ་བའི་ཕྱིར་གསོས་ཤིང་བཙལ་བ༌[^323]སྲོག་ཆགས་རྐང་པ་མེད་པ་སྦྲུལ་དང་འབུ་ལྟ་བུ་དང་། རྐང་པ་གཉིས་པ་མི་ལྟ་བུ་དང་། ཕ་རོལ་ལ་གནོད་པར་བྱ་བའི་ཕྱིར་རྐང་མངས་སྡིག་པ་ལ་སོགས་པ་ལྟ་བུ། རང་ཉིད་ཀྱིས་བརྐུས་པ་དང་། རྐུར་བཅུག་པ་དང་། ཡང་གཞན་གྱིས༌[^324]ནོར་གསེར་དངུལ་ལྟ་བུ་རྣམས་རྐུ་བའི་སེམས་ཀྱིས་བརྐུས་ཏེ་རིན་ཐང་ཚང་ན་ཕམ་པའོ། །

[Block 424]
སྩོགས་པའི་སྒྲས་ནི་མིའི་ནོར་རྙི་དང་སྤྲེའུ་དང་བྱ་རྒྱ་དང་བོད་རྒྱ་དང་ཉ་རྒྱ་ལ་སོགས་པ་རྐུ་བ༌[^325]ཡང་བསྡུ་སྟེ། འདིར་དགེ་སྦྱོང་གིས་བདག་གི་ནོར་དུ་རྐུ་སེམས་ཀྱིས་མིང་དུ་སྨོས་པ་འདི་དག་བརྐུས་ཏེ་རིན་ཐང་ཚང་ན་ཕམ་པའོ། །

[Block 425]
བདག་གི་དོན་དུ་མ་ཡིན་གྱི་ཕ་རོལ་ལ་གནོད་པ༌[^326]བྱ་བའི་བསམ་པས་རྐུ་ན་ཕམ་པའོ།[^327] ། གཉིས་ཀ༌[^328]ལ་ཕན་གནོད་མེད་པའི་བསམ་པས་དེ་དག་དྲལ་ཞིང་བསྲེགས་ན་ཡང་སྦོམ་པོའོ། །

[Block 426]
སྙིང་རྗེའི་བསམ་པས་དྲལ་ཞིང་བསྲེགས་ན་ཉེས་བྱས་སོ། །

[Block 427]
དེ་དག་གིས་ཟིན་པའི་སྲོག་ཆགས་བརྐུས་ཏེ་རིན་ཐང་ཚང་ན་ཕམ་པའོ། །

[Block 428]
གཉིས་ཀ་ལ་མི་ཕན་པའི་བསམ་པས་བཏང་ན་སྦོམ་པོའོ། །

[Block 429]
སྙིང་རྗེའི་བསམ་པས་བཏང་ན་ཉེས་བྱས་སོ། །

[Block 430]
སྔགས་ཀྱི་བདག་པོ་ཡོད་པའི་གཏེར་བདག་གིར་བྱས་པ་སྒྲུབ་པ་ལས་གཏེར་ཕས་འོང་ན་ཇི་ཙམ་མིག་གིས་མ་མཐོང་གི་བར་དུ་སྦོམ་པོའོ། །

[Block 431]
མཐོང་སྟེ་རིན་ཐང་ཚང༌[^329]ན་ལག༌[^330]ཏུ་མ་ཐོབ་ཀྱང་ཕམ་པའོ། །

[Block 432]
བདག་པོ་མེད་པའི་གཏེར་བསྒྲུབས་པ༌[^331]ལས་ཕས་འོང་བ་མ་མཐོང་གི་བར་དུ་ཉེས་བྱས།

[Block 433 [VERSE]]
མཐོང་སྟེ་རིན་ཐང་ཚང་ན་སྦོམ་པོའོ། །
ལྷུང་བཟེད་ལ་སོགས་རྐུན་ཁྱེར་ན། །
ཆོས་བཤད་ནས་ནི་བསྒྲུབ་པར་བྱ། །

[Block 434]
ཡང་ན་རི་བའི་རིན་གྱིས་བླུ།[^332] །དེ་ལྟར་མ་བྱས་ཉེས་བྱས་སོ། །ཞེས་བྱ་བས་ནི་མ་བྱིན་པར་ལེན་པའི་དངོས་པོ་ཐམས་ཅད་ནས་ཐམས་ཅད་དུ་མི་བྱ་བར་དགག་པ༌[^333]སྟེ། འདི་ལྟར་བདག་གི་འཚོ་བའི་ཡོ་བྱད་མེད་དུ་མི་རུང་བ་ལྷུང་བཟེད་དང་ཁར་གསིལ༌[^334]དང་། ཆོས་གོས་ལ་སོགས་པ་རྐུན་པོས་ཁྱེར་ཞིང་ཕྲོགས་ན་རྐུ་བའི་རྣམ་པར་སྨིན་པ་ཡིད་དུ་མི་འོང་བ་ལ་སོགས་པ་རྣམ་པར་སྨིན་པ་ཐོབ་པར་འགྱུར་བའི་ཆོས་བཤད་ནས་སླར་བླང་བར་བྱའོ། །

[Block 435]
དེ་ལྟར་ཆོས་བཤད་པ་ལས་སླར་མ་སྟེར་ན་ཡོ་བྱད་དེ་དག༌[^335]དགེ་སྦྱོང་བདག་ལ་མེད་དུ་མི་རུང་བས་ཅི་རི་བའི་རིན་གྱིས་བླུས་ཏེ་བླང་བར་བྱའོ། །

[Block 436]
དེ་ལྟར་མ་བྱས་པར་ནན་གྱིས་བླངས་སམ་ཕྲོགས་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 437]
ཕས་ཕམ་པ་གཉིས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 438 [HEADING]]
### མི་ཚངས་པར་སྤྱོད་པའི་ཕས་ཕམ་པ། ^5-3-0

[Block 439]
ཕས་ཕམ་པ་གསུམ་པ་མི་ཚངས་པར་སྤྱོད་པའི་གླེང་གཞི་ནི། བཅོམ་ལྡན་འདས་ཡུལ་ཀ་ལན་ད་ཀ་གནས་པའི་གྲོང་ན་བཞུགས་སོ། །

[Block 440]
དེའི་ཚེ་ཁྱིམ་བདག་ཀ་ལན་ད༌[^336]ཀའི་བུ་བཟང་བྱིན་ཞེས་བྱ་བ་ཞིག་རབ་ཏུ་བྱུང་ནས་གནས་པ་ལས།

[Block 441]
[^337]དེའི་མས་བུ་ཁྱོད་ཕ་དང་མའི་ནོར་ནི་སྦྱིན་དུ་ཡོད་པ་ལ་བདག་ཅག་བཟའ་བྲན་རྒས་ཏེ་ཤི་བར་གྱུར་ན་ཀུན་ཀྱང་རྒྱལ་པོའི་ནོར་དུ༌[^338]གྱུར་ན་ཁྱོད་སླར་འབབས་སུ་མི་རུང་ན་ཡང་ས་བོན་ཅུང་ཟད་ཅིག་ཞོག་ཅིག་ཅེས་བྱས་ནས། བཟང་བྱིན་གྱི་ཆུང་མ་ཟླ་མཚན་དང་ལྡན་ཞིང་དུས་ལ་བབ་པ་རྒྱན་གྱིས་ཀླུབས་ཏེ་ཁྲིད་དེ་འོངས་པ་དང་། ཚེ་དང་ལྡན་པ་བཟང་བྱིན་ཡང་འདོད་ཆགས་བདོ་བ་དང་ཉེས་དམིགས་མ་མཐོང་བས་མི་ཚངས་པར་སྤྱོད་དོ། །

[Block 442]
དེ་ནས་དུས་མི་རིང་བ་ཞིག་ན་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་རྣམས་ལ་འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་གི་ཉེས་པ་ལས་དབྲལ་བའི་ཕྱིར། སེམས་རྣམ་པར་གྲོལ་བ་དང་ཤེས་རབ་རྣམ་པར་གྲོལ་བར་འགྱུར་བའི་ཆོས་བཤད་པ་དང་། ཚེ་དང་ལྡན་པ་བཟང་བྱིན་ཉེས་པ་དྲན་ནས་ཤིན་ཏུ་འགྱོད་ཅིང་མི་དགའ་ནས། དེ་དགེ་སློང་རྣམས་ཀྱིས་མཐོང་ནས་ཅི་ཉེས་སྨྲས་པ་དང་། ཚེ་དང་ལྡན་པ་བཟང་བྱིན་གྱིས་དྲང་པོར་སྨྲས་སོ། །

[Block 443]
དེ་ལྟ་བུ་བཅོམ་ལྡན་འདས་ལ་གསོལ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཟང་བྱིན་ལ་རྣམ་པ་དུ་མས་སྨད་ནས་ལེགས་པ་བཅུ་གཟིགས་ཏེ་འདུལ་བ་ལ་བསླབ་པའི་གནས་བཅས་སོ། །

[Block 444 [VERSE]]
སྡོམ་ཅན་ཉམས་པ་མེད་སེམས་ཀྱིས། །
ཉམས་པ་མེད་པའི་སྒོ་གསུམ་དུ། །
ཆགས་པས་ནང་དུ་ནོར་བུ་འདས། །
དགའ་བ་ཚོར་ན་བརྟུལ་ཞུགས་ཉམས། །

[Block 445]
ཞེས་བྱ་བས་མི་ཚངས་པར་སྤྱོད་པ་དང་། རང་བཞིན་བསྟན་ཏེ། སྡོམ་པ་ཅན་དགེ་སྦྱོང་བསླབ་པ་མ་ཕུལ་ཞིང་ཉམས་པ་མེད་པའི་སེམས་རང་བཞིན་དུ་གནས་པས་ཁ་དང་། རྐུབ་དང་། མོ་མཚན་ཏེ་སྒོ་གསུམ་པོ་འདི་དག་མ་རུལ་པ་དང་། རྨ་མ་བྱུང་བ་དང་། འབུ་ཞུགས་པ་ལྟ་བུ་ཉམས་པ་མེད་པ་སྤྱད་དུ་བཟོད་པར་བདག་ཉིད་ཆགས་པའི་སེམས་ཀྱིས་ནང་དུ་བཅུག་སྟེ་མཚམས་འདས་ལ། དགའ་བ་ཚོར་ན་བརྟུལ་ཞུགས་ཉམས་ཏེ་ཕམ་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 446]
དེ་ལ་ཡན་ལག་ནི་རྣམ་པ་ལྔ་སྟེ། སེམས་མ་ཉམས། སྒོ་གསུམ་སྤྱད་བཟོད། ཆགས་སེམས་ཡོད། མཚམས་ལས་འདས། དགའ་བ་ཚོར། དེ་རྣམས་གཅིག་དང་མི་ལྡན་ན་སྦོམ་པོར་གཞག༌[^339]གོ། །

[Block 447 [VERSE]]
སྐྱེས་པ་བུད་མེད་མ་ནིང་གིས། །
ཚན༌[^340]ཀར་བོར་ཏེ་མནན་པ་ལས། །
གང་གིས་བདེ་བའི་རོ་མྱོང་བ། །
དེ་ཡང་སྡོམ་པ་ཞིག་པར་འགྱུར། །

[Block 448]
ཞེས་བྱ་བ་ནི་བདག་དགེ་སྦྱོང་མཐུ་ཆུང་ཞིང་ཞན་པ་ལ། སྐྱེས་པ་དང་བུད་མེད་དང་མ་ནིང་སྟེ། མི་རྣམ་པ་གསུམ་གྱིས་ཚན༌[^341]ཀར་བོར་ཏེ་མནན་ནས་བདག་དང་དེ་དག་གི་སྒོ་གསུམ་གང་ཡང་རུང་བར་བཅུག་པའི་ཚེ། བདག་ཉིད་ཀྱིས༌[^342]ཉམས་སུ་བླངས་ཏེ་དགའ་བ་ཚོར་ན་དེ་ཡང་སྡོམ་པ་ཞིག་སྟེ་ཕས་ཕམ་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 449]
འདིས་ནི་ཇི་ལྟར་གྱུར་ཡང་ཉམས་སུ་མི་བླང་བ་སྟོན་ཏོ། །

[Block 450 [VERSE]]
ཡན་ལག་སྐྱེས་ནས་བདེ་འདོད་པས། །
གདུག་པ་སྦྲུལ་གྱི་ཁར་བཅུག་བླ། །
ལུས་ལ་དཀའ་ཐུབ་མི་གཞིག་ཅེས། །
རྫོགས་སངས་རྒྱས་ཀྱིས་བཀའ་སྩལ་ཏོ། །

[Block 451]
ཞེས་བྱ་བ་ལ། གལ་ཏེ་འདོད་ཆགས་ཀྱི་དབང་གིས་བདག་གི་ཡན་ལག་སྐྱེས་བསྒྲེངས་ཏེ༌[^343]ཤིན་ཏུ་བདོ་བར་གྱུར་པ༌[^344]འདོད་ཆགས་དེ་དང་བྲལ་ཞིང་བདེ་བར་འདོད་པར་བྱ་བའི་ཕྱིར། སྦྲུལ་གདུག་པའི་ཁར་བཅུག་སྟེ། འདོད་ཆགས་དང་བྲལ་བར་གྱུར་པ་ནི་བདག་ལ་ཕན་པ་ཡིན་པས་བླའི། ལུས་ལ་བདག་གི་སྡོམ་པ་ནི་མི་གཞིག་པར་བྱའོ་ཞེས་རྫོགས་པའི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་ཏོ། །ཇི་ལྟར༌[^345]ཞེ་ན།

[Block 452 [VERSE]]
གལ་ཏེ་སྦྲུལ་གྱིས་གསད༌[^346]གྱུར་ཀྱང་། །
ཚུལ་ཁྲིམས་གནས་ལ་དེ་ཕན་ཏེ། །

[Block 453]
ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་ཆགས་པའི་དབང་གིས་ཡན་ལག་སྐྱེས་བསྒྲེངས༌[^347]ནས་སྦྲུལ་གདུག་པའི་ཁར་བཅུག་སྟེ་ཤི་བར་གྱུར་པ་ནི་སྒོ་གསུམ༌[^348]སྣང་བའི་གནས་སུ་མ་བཅུག་པ་ཚུལ་ཁྲིམས་ཅན་དེ་ལ་ཕན་ཏེ་མཐོ་རིས་སུ་སྐྱེས་པའི་ཕྱིར་རོ།[^349] །ཚུལ་ཁྲིམས་དེ་ཞིག་པར་གྱུར་པས་སྡུག་བསྔལ་ཡིན་ཏེ་ངན་སོང་གསུམ་དུ་སྐྱེའོ། །

[Block 454]
དེར་ཡང་མ་ཟད་ཀྱི་མྱ་ངན་ལས་འདས་པ་ལའང་སྒྲིབ་པར་འགྱུར་ཏེ། ཚུལ་ཁྲིམས་ཉམས་ན་ཐར་པ་མྱ་ངན་ལས་འདས་པའི་སྐལ་བ་ཡང་མེད་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 455]
ཕས་ཕམ་པ་གསུམ་པ་བཤད་ཟིན་ཏོ།། །།

[Block 456 [HEADING]]
### བརྫུན་དུ་སྨྲ་བའི་ཕས་ཕམ་པ། ^5-4-0

[Block 457]
ཕས་ཕམ་པ་བཞི་པ་བརྫུན་གྱི་གླེང་གཞི་ནི། བཅོམ་ལྡན་འདས་ཡུལ་ཡངས་པ་ཅན་གྱི་སྤྲེའུ་རྫིང་གི་འགྲམ་ན་བཞུགས་སོ། །

[Block 458]
དེའི་ཚེ་མུ་གེ་ཆེན་པོ་བྱུང་ནས་ཁ་ཟས་ཀྱིས་ཤིན་ཏུ་བྲེལ་ཏེ༌[^350]ཕ་མ་ཡང་བུ་ལ་ཁ་ཟས་མི་སྟེར་བ་ཙམ་དུ་དཀོན་པའི་ཚེ། དགེ་སློང་རྫུ་འཕྲུལ་ཅན་དང་གནས་བརྟན་རྣམས་ནི་བྱང་གི་སྒྲ་མི་སྙན་ལ་སོགས་པ་ཡུལ་གཞན་འབྱོར་ཅིང་རྒྱས་པ་དག་ཏུ་དོང་ཞིང་བདག་ཉིད་ཀྱང་ཟ། གང་ཟག་གཞན་ལ་ཡང་སྟོབས་སོ། །

[Block 459]
དེ་ལ་ཉ་པ་ལས་རབ་ཏུ་བྱུང་བའི་དགེ་སློང་ལྔ་བརྒྱ་ལ་སོགས་པ་དག་གིས་ཀྱང་དགེ་སློང་དེ་དག་ལྟར་བྱ་ཞིང་དབྱར་ཚུལ་དུ་འཇུག་ཏུ་ནི་རྫུ་འཕྲུལ་ཡང་མ་ཐོབ་ཅིང་ཐོས་པ་དག་ཀྱང་ཉུང་ཞིང་དེ་ལྟར་མི་ནུས་ཀྱིས་བདག་ཅག་གིས་ཡུལ་ཉིད་དུ་དབྱར་ཚུལ་དུ་ཞུགས་ལ་བདག་ཅག༌[^351]སོ་སོའི་ཡོན་ཏན་བསྒྲགས་ཏེ་རྙེད་པ་བསྒྲུབ་པོ་སྙམ་ནས་ཚུལ་དུ་ཞུགས་སོ། །

[Block 460]
དེ་ནས་ལྔ་བརྒྱ་པོ་དེ་དག་གིས་གཅིག་གིས་གཅིག་གི་ཡོན་ཏན་བརྗོད་པ་ལ་ཞུགས་སོ། །
--- END BLOCKS ---
