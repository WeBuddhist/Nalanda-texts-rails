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
[Block 491]
ཤ་ཟ་རྣམས་མཐོང་བ་ཡོད་དོ་ཞེས་སྨྲ་ལ། བདག་ཉིད་ཡིན་པར་མི་སྨྲ་ན་ནི་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 492]
དགོན་པ་ན་དགེ་སློང་དུ་གནས་པ་དེ་ལ་མི་མ་ཡིན་པ་རྣམས་ཀྱིས་གཙེས་པ་ལས་འཕགས་པ་རྣམས་ལ་མི་གཙེ་སྟེ་བདག་ལ་ཡང་མི་གཙེ་ཟེར་ན་ཕམ་པ། འཕགས་པ་རྣམས་ཀྱི་ཕྱིར་ཁྱིམ་བདག་རྣམས་སྟན་ཁྲ་བོ་འདིངས་ཏེ་བདག་གི་ཕྱིར་ཡང་ཁྱིམ་བདག་སྟན་ཁྲ་བོ་འདིངས་སོ་ཞེས་ཟེར་བ་ཡང་དོན་རིག་ན་ཕམ་པའོ། །

[Block 493]
ཁྱད་པར་ཐོབ་པ་མ་གཏོགས་པར་ཞེས་བྱ་བ་ལ་སོགས་པས་ཉེས་བྱས་སུ་འགྱུར་བ་བསྟན་ཏོ། །

[Block 494 [VERSE]]
དེ་ལས་གཞན་པའི་བརྫུན་ཚིག༌[^378]རྣམས། །
དེ་དག་ཐམས་ཅད་སྡིག་མང་འགྱུར། །

[Block 495]
ཞེས་བྱ་བ༌[^379]ནི་གོང་དུ་ཡོན་ཏན་ཁྱད་པར་ཅན་ཐོབ་བོ་ཞེས་བྱ་བ་ལས་མ་གཏོགས་པར་ཀུ་རེ་དང་ཀྱལ་ཀ་ལ་སོགས་པའི་ཕྱིར། བརྫུན་པའི༌[^380]ཚིག་སྨྲས་ན་སྡིག་པ་མང་དུ་འགྱུར་ཏེ་ཉེས་བྱས་ལྕི་བར་འགྱུར་རོ། །

[Block 496 [VERSE]]
ཇི་ལྟར་མཛའ་བོ་འབྱེད་འགྱུར་བ། །
ཕྲ་མའི་ཚིག་རྣམས་སྨྲ་མི་བྱ། །

[Block 497]
ཞེས་བྱ་བས་ནི་ངག་གི་ཉེས་པ་གཉིས་པ་བསྟན་ཏེ་འདུམ་ཞིང་མཛའ་བར་འགྱུར་བས༌[^381]འཐབ་ཅིང་དབྱེ་བར་འགྱུར་བའི་ཕྲ་མའི་ཚིག་གིས་དབྱེ་བ་རྣམས་སླར་མི་སྡུམ༌[^382]ཞིང་དབྱེས་སུ་འགྱུར་བ་ཕྲ་མའི་ཚིག་རྣམས་མི་བྱའོ། །

[Block 498 [VERSE]]
ངན་དུ་ཟེར་ལ་ངན་མི་སྨྲ། །
གཤེ་བ་ལ་ཡང་སླར་མི་གཤེ། །
མཚང་འབྲུ་བ་ལ༌[^383]སླར་མི་འབྲུ། །
རྡེག་པ༌[^384]ལ་ཡང་སླར་མི་རྡེག །

[Block 499]
[^385]ཅེས་བྱ་བས་ནི་ངག་གི་ཉེས་པ་སྤོང་བ་དགེ་སྦྱོང་གི་ཚུལ་བཞི་སྟེ། བདག་ཉིད་ལ་ཉེས་པ་རྣམས་ལའང་མི་རིགས་པར་མི་བྱ་ན། སེམས་ཅན་ཉེས་པ་མེད་པ་རྣམས་ལ་བདག་ཉིད་ཀྱིས་མི་རིགས་པར་བྱ་བ་ལྟ་ཅི་སྨོས། གཞན་གྱིས་ངན་དུ་སྨྲ་བ་ལ་སོགས་པ་བྱས་པ༌[^386]སླར་ལན་མི་གླན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 500 [VERSE]]
བློ་ལྡན་བསླབ་པ༌[^387]འདོད་པ་ཡིན། །
བསྒྲིམས་ཏེ་ངག་གི་སྐྱོན་རྣམས་སྤང་། །

[Block 501]
ཞེས་བྱ་བ་ནི་ངག་གི་ཉེས་པ་བཞི་པ་སྟེ། རྒྱལ་པོའི་གཏམ་དང་། ཆོམ་པོའི་གཏམ་དང་། ཚོང་པའི་གཏམ་ལ་སོགས་པ་ནི་ཚིག་ཀྱལ་པ་སྟེ་ངག་གི་སྐྱོན་རྣམས་ཏེ་གང་བསླབ་པར་འདོད་པའི་དགེ་སློང༌[^388]བློ་དང་ལྡན་པས་སྤང་བར་བྱའོ། །

[Block 502 [VERSE]]
དེ་ལྟར་འགྱུར་བར༌[^389]རིག་ནས་ནི། །
ངག་རྣམས་ཤིན་ཏུ་བསྡམ་པར༌[^390]བྱ། །

[Block 503]
ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པ་ལྟར་ངག་གིས༌[^391]ཉེས་པ་བཞི་སྤྱད་ན་བརྫུན༌[^392]དང་སྦོམ་པོ་དང་ཉེས་བྱས་སུ་རིག་ནས་དེ་དག་བསྡམ་ཞིང་སྤང༌[^393]ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 504]
ཕམ་པ་བཞི་པ་བཤད་པ་སྟེ་ཕས་ཕམ་པ་བཞིའི་བཤད་པ་རྫོགས་སོ།། །།

[Block 505 [HEADING]]
## བསླབ་པ་ཕྲ་མོའི་གནས། ^6-0

[Block 506]
དེ་ལྟར་ཕས་ཕམ་པའི་གནས་བསྟན་ནས། ད་ནི་བསླབ་པ་ཕྲ་མོའི་གནས་བསྟན་པའི་ཕྱིར། འབྲུ་བཏགས་ཕབས་དང་སྦྱར་བ་ཡི།[^394] །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 507]
དེ་ཡང་རྣམ་པ་དྲུག་སྟེ།

[Block 508 [HEADING]]
### ཆང་འཐུང་བ། ^6-1-0

[Block 509 [VERSE]]
འབྲུ་བཏགས་ཕབས་དང་སྦྱར་བ་ཡི། །
བཏུང་བའི་བྱེ་བྲག་འབྲུ་ཡི་ཆང་། །

[Block 510]
ཞེས་བྱ་བ་ནི་ནས་འབྲས་བཏགས་ཏེ་ཆང་དུ་བྱ་བའམ། མ་བཏགས་པ༌[^395]ཆང་དུ་བྱས་པ་རྣམས་ཏེ།

[Block 511 [VERSE]]
དེ་ནི་མྱོས་པར་འགྱུར་རིག་ནས། །
རྩྭ་མཆོག་གིས་ཀྱང་མི་བཏུང་ངོ་། །

[Block 512]
ཞེས་བྱ་བར་འགྱུར་རོ། །

[Block 513 [VERSE]]
སྡོང་བུ་མེ་ཏོག་འབྲས་བུ་ལས། །
སྦྱར་བའི་ཁུ་བ་བཅོས་པའི་ཆང་། །
དེ་ནི་མྱོས་པར་འགྱུར་རིག་ནས། །

[Block 514]
ཞེས་བྱ་བ་དང་། རྩྭ༌[^396]མཆོག་གིས་ཀྱང་མི་བཏུང་ངོ་། །ཞེས་བྱ་བར་སྦྱར་ཏེ། འདི་ལྟར་སྡོང་བུ་སྟེ་བུ་རམ་ཤིང་བཙིར་བ་ལས་བྱས་པ་དང་། མེ་ཏོག་འབྲས་བུ་སྟེ་རྒུན་འབྲུམ་ལ་སོགས་པ་སྦྱར་བའི་ཁུ་བས་མྱོས་ཤིང་དྲན་པ་ཉམས་པར་འགྱུར་བར་རིག་ནས་བདག་ཉིད་ཀྱང་རྩྭ་མཆོག་གིས་མི་བཏུང༌[^397]ལ་གཞན་ལ་ཡང་སྦྱིན་པར་མི་བྱ་ཞེས་སྟོན་ཏོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྡོམ་ཅན་ཕན་འདོད་མི་བཏུང་ངོ་། །ཞེས་བྱ་བ་སྟེ། འདི་ལྟར་དགེ་སྦྱོང་སྡོམ་པ་ཅན་བསླབ་པ༌[^398]ལ་གནས་པས་བདག་ལ་ཕན་པ་དང་བདེ་བར་བྱ་བའི་ཕྱིར་རོ། །

[Block 515]
འཐུངས་ན་ཉེས་པ་ཅི་ཡོད་ཅེ་ན།

[Block 516 [VERSE]]
དེ་འཐུངས་ན་ནི་དྲན་ཉམས་ཤིང་། །
བརྟུལ་ཞུགས་ལྡན་པ་བག་མེད་འགྱུར། །
བག་མེད་པ་ལས་བརྟུལ་ཞུགས་ཉམས། །

[Block 517]
ཞེས་བྱ་བ་སྟེ། གོང་དུ་སྨོས་པའི་ཆང་གི་རྣམ་པ་དེ་དག་འཐུངས་ཤིང་གཞན་ལ་བླུད་ན་བདག་དང་གཞན་གྱི་སེམས་རང་བཞིན་དུ་གནས་ཤིང་གསལ་བ་ཉམས་སུ་མྱོང་བའི་དྲན་པ་ཉམས་པས་ལུས་ཀྱིས་རྗེས་སུ་རྡེག༌[^399]བཙོག་དང་། ངག་གི་སྒོ་ནས་ཚིག་ངན་པ་ལ་སོགས་པ་བག་མེད་པ་འབྱུང་ངོ་། །དེ་ལྟར་བག་མེད་པའི་སྒོ་ནས་སྲོག་གཅོད་པ་དང་། མ་བྱིན་པར་ལེན་པ༌[^400]ལ་སོགས་པ་བརྟུལ་ཞུགས་ཏེ་ཚུལ་ཁྲིམས་ཉམས་པར་འགྱུར་རོ། །

[Block 518]
དེ་བས་ན།

[Block 519 [VERSE]]
དེ་བས་སྟོན་པའི་བཀའ་དྲན་བྱ། །
མྱོས་འགྱུར་ཉེས་པ་འཕེལ་འགྱུར་བ། །
རྩྭ༌[^401]མཆོག་གིས་ཀྱང་མི་བཏུང་ངོ་། །

[Block 520]
ཞེས་སྨོས་ཏེ། དེ་བས་ན་སྟོན་པ༌[^402]སངས་རྒྱས་ཀྱི་བཀའ་ཚད་མ་དྲན་པར་བྱས་ལ་དྲན་པ་ཉམས་ཤིང་མྱོས་པར་འགྱུར་བའི་གནས་ཉེས་པ་རྣམ་པ་དུ་མ་འཕེལ་བར་བྱེད་པའི་རྒྱུ་རྩྭ་མཆོག་གིས་ཀྱང་རེག་པར་མི་བྱ་ན་གཞན་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 521]
ཇི་ལྟར་ཆང་འཐུངས་ན་ཉེས་བྱས་སུ་འགྱུར་བ་བཞིན་དུ་གླུ་མ་དང་སྦང་མ་ཟོས་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 522]
འདི་ལྟར་ཆང་ལ་ཆང་གི་ཁ་དོག་དང་དྲི་དང་རོ་དང་མྱོས་པར་འགྱུར་བའི་མཐུ་དང་བཞི་ཆར་ལྡན་པ་འཐུངས་ན་ཉེས་པར་གཞག༌[^403]གོ། །

[Block 523]
སྦྲང་རྩི་དང་བྲོ་བ༌[^404]ལ་སོགས་པ་མྱོས་པའི་མཐུ་ཡོད་དུ་ཟིན་ཀྱང་ཁ་དོག་དང་དྲི་དང་རོ་ལ་སོགས་པ་དང་། འཇིག་རྟེན་ལ་སོགས་པ་སྨད་པ་མ་ཡིན་པས་དེ་དག་གིས་མྱོས་པ་ནི་མ་ཡིན་ནོ། །

[Block 524]
གལ་ཏེ་དགེ་སྦྱོང་ནད་ཀྱིས་ཐེབས་ཏེ་ཆང་གི་ཆོ་ག་བྱ་དགོས་ན་ཆང་གིས་ལུས་ལ་བསྐུ་བར་བྱའོ། །

[Block 525]
ཡི་ག༌[^405]འཆུས་པ་ཕན་པར་བྱ་ན་ཡང་ཁར་བླུགས་པ་ལས་བཏུང་བར་མི་བྱའོ། །

[Block 526]
ཆང་མ་འཐུངས་ན་ཡང་མི་འཚོ་བ་ཙམ་དུ་ཐུག༌[^406]ན་བསྐོལ་བ་ཆང་གི་རོ་དང་མྱོས་པའི་མཐུ་མེད་པར་བྱས་ཏེ། ཆང་དང་རོ་ཉམས་པ་དང་ཁ་དོག་དང་འདྲ་བ་ཙམ་བྱའོ། །

[Block 527 [HEADING]]
### གླུ་གར་རོལ་མོ། ^6-2-0

[Block 528]
གླུ་གར་རོལ་མོའི་གླེང་གཞི་ནི་བཅོམ་ལྡན་འདས་རྒྱལ་པོའི་ཁབ་ན་བཞུགས་སོ། །

[Block 529]
རྒྱལ་པོ་གཟུགས་ཅན་སྙིང་པོས་ཀླུའི་རྒྱལ་པོ་རི་བོ་དང་ཡིད་འོང་གི་ཕྱིར་གཙུག་ལག་ཁང་བརྩིགས་ནས་དུས་སྟོན་ཆེན་པོ་བྱས་པའི་ཚེ། ལྷོ་ཕྱོགས་ནས་གར་མཁན་འོངས་ཏེ་དྲུག་སྡེ་ཅི་བྱེད་པའི་ལད་མོ་བཟླས་པ་དང་། དྲུག་སྡེ་ཁྲོས་ནས་དུས་གཞན་ཞིག་ན་དུས་སྟོན་བྱེད་པའི་གར་མཁན་ལ་གནོད་པའི་ཕྱིར་དྲུག་སྡེས་བྲོ་གར་བྱས་པ་དང་། སྐྱེ་བོ་ཀུན་གར་མཁན་ལ་མི་ལྟ་བར་དྲུག་སྡེས་བྲོ་གར་བྱེད་པ་ལ་བལྟས་ནས་རོལ་མོ་མཁན་གྱིས་རྙེད་པ་མ་གྲུབ་སྟེ། འཚོ་བ་ཆད་ནས་རོལ་མོ་མཁན་ཁ་ཟེར་བ་ལ་བཅས། ཡུལ་ནི་རྒྱལ་པོའི་ཁབ། གང་ཟག་ནི་དྲུག་སྡེ།[^407] ཉོན་མོངས་པ་ནི་ཞེ་སྡང་། ཉེས་པ་ནི་གླུ་གར་རོལ་མོའི་སྒྲ་བྱེད་པའོ། །

[Block 530 [VERSE]]
གླུ་གར་དེ་བཞིན་སིལ་སྙན་རྣམས། །
སྡོམ་ལ་གནས་པས་མི་བྱའོ། །
--- END BLOCKS ---
