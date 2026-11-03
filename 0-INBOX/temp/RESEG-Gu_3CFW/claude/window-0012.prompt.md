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
[Block 421]
འདིར་བརྗོད་པ་ཡང་བབས་པ་དང་ཤི་བར་གྱུར་པ་གཉིས་ལ་ཡང་མི་འོས་པ་ཉིད་ཀྱི་དོགས་པ་ཡོད་པར་འགྱུར་བ་དེ་བས་ན་དེའི་ཕྱིར་བརྗོད་པར་བྱ་སྟེ། བབས་པ་དང་ཤི་བར་གྱུར་པ་གཉིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་འདི་གཉིས་ཀྱང་ཆེས་རིང་དུ་གནས་པ་ཡིན་ན༌[^393]དེའི་དུས་ཀྱི་རྙེད་པ་དབང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 422]
ཤི་བའི་ཕྱིར་འདི་སྨོས་པ་ལ་དགོས་པ་ཅི་ཡོད་ཅེ་ན། གལ་ཏེ་སུ་ཞིག་ལ་ཕུལ་ནས་ཤི་ན་བུ་ལོན་འདི་ལ་ཡོད་པའམ། ཉེ་བར་གནས་པས་ཡོ་བྱད་དྲུག་པོ་མ་ཐོབ་ན་དེ་ལ་སྦྱིན་པར་བྱའོ། །

[Block 423]
གལ་ཏེ་མ་ཡིན་ན་གང་རྣམས་ཀྱིས་དེ་ནི༌[^394]ཤི་བའི་ཡོ་བྱད་ལ་དབང་བ་ཉིད་དེ་དེ༌[^395]རྣམས་ལ་འདིར་རྙེད་པ་ཞེས་བྱ་བ་འདི་བསྟན་པའོ། །

[Block 424]
རྙེད་པ་ནི་ཇི་ལྟར་རྣམ་པར་ངེས་པར་བྱེད་པ་ལྟར་རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བ་ནི། གཙུག་ལག་ཁང་འདི་ན་གནས་པའི་དགེ་སློང་རྣམས་ཀྱིས་གནས་མལ་དང་བསོད་སྙོམས་ལ་སོགས་པ་འདི་ལོངས་སྤྱོད་པར་བྱའོ་ཞེའམ། དེ་ན་གནས་པའི་རྟེན་པ༌[^396]ལ་རྐང་པའི་མར་བསྐུ་བ་ལ་སྦྱར་བར་བྱའོ། །

[Block 425]
སྨན་གྱི་རིན་ལ་སོགས་པ་དང་ཞེས་བྱ་བ་འདིར་སྤྲོས་པ་མ་བྱས་ཏེ། སྤྲོས་པ་མ་བྱས་པ་ནི་གནས་ཁང་ལ་སོགས་པ་དགེ་སློང་གི་དབང་དུ་མཛད་ནས་རྙེད་པ་གནང་བ་ལ་དེ་ལྟ་བུར་གྱུར་པ་ཉིད་ཀྱིས་ལོངས་སྤྱད༌[^397]པར་བྱའོ། །

[Block 426]
གནས་ཁང་དང་ཞིང་དང་ཁང་པ་བརྩེགས་པ་འདི་ལ་ངེས་པར་དེ་ནི་གནས་པས་འདི་ལོངས་སྤྱོད་པར་བྱའོ་ཞེས་སྤྲོས་པ་མ་བྱས་ཏེ། དེ་ན་དགེ་སློང་གི་དབང་དུ་མཛད་ནས་གནང་བའོ། །

[Block 427]
གཞན་དུ་གནས་པས་ལོངས་སྤྱད༌[^398]པར་བྱའོ། །

[Block 428]
འདིར་དགུན་ནམ་དབྱར་གནས་པ་ལ་འདི་དབུལ་བར༌[^399]བྱའོ། །

[Block 429]
ངེས་པར་གནས་པ་ཉིད་ཀྱིས་དེར་དུས་དེར་མནོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམ་པར་དཔྱད་པར་བྱས་ནས་གང་ཟག་ལ་སྦྱིན་བར་བྱ་སྟེ་དེ་ཉིད་ལ་དེའོ། །

[Block 430]
འཐོབ་པ་རྣམས་ཀྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་། རྙེད་པ་ནི་ཇི་ལྟར་ངེས་པར་བྱེད་པ་ལྟར་རྙེད་པ་རྣམ་པར་གཞག་པའོ། །

[Block 431]
གང་དུ་དེ་རྣམས་འགྲོ་བ་དེར་གཏོགས་པའི་རྣམ་པར་ངེས་པ་ལ་ཞེས་བྱ་བ་དེ་ནི༌[^400]དོན་གྱིས་རྟོགས་པར་བྱའོ། །

[Block 432]
གང་དུ་ཡང་དེ་རྣམས་འགྲོ་བ་སྟེ། ཕུལ་བའི་རྫས་ལ་ཁྱིམ་ཆེ་གེ་མོ་ནི་ཁྱེད་ཀྱིའོ། །

[Block 433]
ཁྱིམ་ཆེ་གེ་མོ་ནི༌[^401]ངེད་ཀྱིའོ། །

[Block 434]
ལམ་པོ་ཆེ་འདི་ནི་ཁྱེད་ཀྱིའོ། །

[Block 435]
ལམ་པོ་ཆེ་འདི་ནི་ངེད་ཀྱིའོ། །

[Block 436]
བཞི་མདོའི་དབུས་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུར་ཁྲིམས་སུ་བྱ་བ་བཅས་ནས་ཐ་དད་པ་དག་ལ་ཆོས་ཀྱི་འདོད་པ་ཁས་བླངས་པ་དང་མ་བླངས་པ་དག་གིས་ཕྱོགས་གཉིས་ལ་དབྱར་གནས་པར་ཁས་བླངས་པ་ལ་གཞི་མདོ༌[^402]ལ་སོགས་པ་ལས་གནས་གཞན་ལས་གང་གིས་ཕྱོགས་གཞན་རྣམ་པར་ངེས་པའི་ཁྱིམ་གྱི་ཕྱོགས་གཞན་ཀྱི་རྙེད་པ་རྙེད་པའོ། །

[Block 437]
ཁྱིམ་དེ་ཉིད་དུ་རྣམ་པར་ངེས་པར་བྱས་པའི་ཕྱོགས་ཀྱི་རྙེད་པ་དེའོ། །

[Block 438]
དེའི་ཕྱོགས་གཉིས་ཀ་ཡང་གལ་ཏེ་ཁྱིམ་དེ་དང་ལྡན་པ་རྙེད་པ་དེ་དང་སྦྱོར་བ་ཡིན་ན་དེ་ལྟར་ཡང་ཕྱོགས་དེ་ཉིད་ཁྱིམ་དེར་རྣམ་པར་ངེས་པ་ལ་རྙེད་པ་དེ་ཡོད་པར་འགྱུར་རོ། །

[Block 439]
འདིར་ཐམས་ཅད་སྟོན་པ་ལ་སུ་ཞིག་ལ་དགོས་པ་འགྲུབ་པའི་ཕྱོགས་དེ་ལ་ཡང་རྙེད་པ་དེ་ལ་གཞན་གྱི་ཅི་ཞིག་སྙམ་པ་དེ་བཟློག་པའི༌[^403]དོན་དུ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་ཐམས་ཅད་ཀྱི༌[^404]ཕུལ་ན་ཡང་ངོ་ཞེས་བྱ་བ༌[^405]སྨོས་ཏེ། དེ་ལྟར་ཡང་ཇི་ལྟར་རྣམ་པར་ངེས་པའི་རྙེད་པ་རྣམ་པར་གཞག་པའི་དཔེར་འདིར་དབྱར་གྱི་དུས་སུ་བྱེད་པ་དག་གི་ཕྱོགས་དུས་གཞན་དག་ལ་ཡང་སྡེ་ཚན་གཞན་ལ་ཡང་འདི་རུང་བས། དེའི་ཕྱིར་འདིར་སྤྱིར་མདོར་བསྡུས་པའོ། །

[Block 440]
གལ་ཏེ་ཟས་ལ་ཡང་དེ་ལྟར་རྣམ་པར་ངེས་པར་བྱས་པར་གྱུར་ན་དེའི་ཚེ་ཁྱིམ་གཞན་རྣམ་པར་མ་ངེས་པ་ལ་གཞན་གྱིས་བཟའ་བར་མི་བྱ་སྟེ། རྣམ་པར་མ་ངེས་པའི་ཕྱོགས་ཀྱི་ཁྱིམ་གཞན་ལས་རྙེད་པར་འགྱུར་བ་ཅིག་ཤོས་ཀྱིས་ཕྱོགས༌[^406]ཀྱི་རྗེས་སུ་གནང་བ་ཉིད་ཡིན་ན་ཉེས་པ་མེད་པར་རིག་པར་བྱའོ། །

[Block 441]
དགེ་འདུན་ཡོངས་སུ་མ་བཅད་ན་ལས་ཀྱི་མཚམས་ཀྱིས༌[^407]ཡོངས་སུ་བཅད་དོ་ཞེས༌[^408]བྱ་བ་ནི། དགེ་འདུན་ཡོངས་སུ་མ་བཅད་ན་དགེ་འདུན་ལ་རྙེད་པ་རྣམ་པར་ངེས་པ་ལ་གང་ཞིག་གནས་དེ་ལ་གསོལ་བ་ལ་སོགས་པའི་ལས་ཀྱི་མཚམས་དེས་དགེ་འདུན་ཡོངས་སུ་བཅད་པ་དེའི་མཚམས་ཀྱི་ནང་དུ་གཏོགས་པའི་སྣ་ཚོགས་པའི་གནས་སམ་གནས་གཅིག་པ་ཐམས་ཅད་ལ། གློ་བུར་བ་དང་བཅས་པ་ལ་རྙེད་པ་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 442]
འདི་ལ་གཅིག་ལ་སོགས་པ་ནི་དེ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདིར་དགེ་འདུན་ལ་བརྟེན་ནས་ཕུལ་བའི་རྙེད་པ་ལ་གལ་ཏེ། མཚམས་གཅིག་གི་ནང་དུ་གཏོགས་པར་གྱུར་པ༌[^409]གཉིས་སམ་གསུམ་ནི་དགེ་འདུན་ཉིད་དོ། །

[Block 443]
དེ་ལ་དེ་ཙམ་དེར་འོས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 444]
སྐྱེས་པའམ་བུད་མེད་དམ་མ་ནིང་འགའ་ཞིག་ལ་བརྟེན་ནས་དབྱར་གནས་པར་ཁས་ལེན་ཅིང་གནས་མེད་པར་དེ་ན་བུད་མེད་ལ་སོགས་པས་དབུལ་བར༌[^410]བྱེད་ན་དེ་གནས་ཆེ་གེ་མོར་དགེ་འདུན་ལ་ཕུལ་ལོ་ཟེར་ལ། གལ་ཏེ་དེ་ལྟར་གནས་དེར་མཚམས་གང་ཡིན་པའི་ཁོངས་སུ་ཆུད་པ་དེ་རྣམས་ཀྱི་རྙེད་པ་ནི་དེ་ཡིན་ནོ། །

[Block 445]
གལ་ཏེ་བདག་གིས་འདི་ཉིད་ཀྱི་དགེ་འདུན་ལ་ཕུལ་ལོ་ཞེས་ཟེར་ལ། གལ་ཏེ་དེ་ན་གང་ཟག་གཞན་མེད་ན་ནི་རྙེད་པ་དེ་མཚམས་ཀྱིས་བསྟབས་པ་ཡིན་ནོ། །

[Block 446]
གལ་ཏེ་འདི་ཁྱོད་ཁོ་ན་ལ་ཕུལ་ལོ་ཞེས་ཟེར་ན་ནི་རྙེད་པ་དེ་རྟེན་གྱིས་བསྟབས་པ་ཡིན་ཏེ་རྟེན་གྱི་དབང་གིས་གྲུབ་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 447]
ཆོས་ཀྱི་རྙེད་པ་ནི་དེ་སྨྲ་བ་རྣམས་དབང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདིར་སྨྲ་བ་རྣམས་ལ་ཤུགས་ཀྱིས་དབང་བྱེད་པ་ཉིད་དོ། །

[Block 448]
དེའི་སྒྲས་ནི་ཆོས་དང་འབྲེལ་པའོ། །

[Block 449]
ཆོས་ཀྱི་རྙེད་པས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 450]
འདུལ་བ་བྱེ་བྲག་ཏུ་བཤད་པ་དག་ལས་མྱ་ངན་ལས་འདས་པ་དག་ལ༌[^411]ཕུལ་བ་ནི་མཆོད་རྟེན་གྱི་དང་འདྲ་བར་གཞག་གོ་ཞེས་གསུངས་པས། དེའི་ཕྱིར་འདིར༌[^412]ཆོས་རིན་པོ་ཆེ་མ་ཡིན་གྱི་འོན་ཏེ་གཞན་ཡིན་ཏེ། སིལ་བུ་དག་ལས་ཀྱང་དེར་ཆོས་གཞན་བཟུང་བ༌[^413]ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 451]
རིན་པོ་ཆེའི་གོ་རིམས་འདི་ནི་ཞེས་བྱ་བ་གལ་ཏེ་ཡོད་པར་འགྱུར་ན་ནི་མི་མཁས་པ་ལ་རིན་པོ་ཆེའི་གོ་རིམས་ལ་བརྡ་བྱས་པ་ལ་ཆོས་ཀྱི་མིང་ངོ་། །གཙུག་ལག་ཁང་གི་ཚིགས་སུ་བཅད་པ་གཅིག་འཛིན་པ་ནི་འདིར་དེ་ཉིད་ཀྱི་མཐའ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་དེ་ཉིད་ཀྱི་ཞེས་བྱ་བ་ནི་ཆོས་སྨྲ་བ་པོ་ཉིད་ལའོ། །

[Block 452]
འདི་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་རྙེད་པ་དབང་བ་འདི་ལའོ། །

[Block 453]
མདོ༌[^414]འདི་ནི་རྩོད་པའི་གཞིའི་གཞུང་ལས་འབྱུང༌[^415]ངོ་། །མཚན་མི་མཐུན་པའི་ཤི་བའི་ཡོ་བྱད་ལ་ཅིག་ཤོས་ཡོད་ན་མི་དབང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། མཚན་མི་མཐུན་པའི་ཞེས་བྱ་བ་ནི། འདིར་གཞུང་ནི།

[Block 454]
གླེང་གཞི་རྣམས་ལས།

[Block 455]
དགེ་སློང་དག་དགེ་ཚུལ་གྱི་རྒྱུད་དུ་གཏོགས་པ་དེའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 456]
ཅི་ཐམས་ཅད་དུ་རྣམ་པར་གཞག་པ་འདི་ཡིན་ནམ་ཞེ་ན་མ་ཡིན་ཏེ་དེའི་ཕྱིར་ཅིག༌[^416]ཤོས་ཡོད་ན་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅིག་ཤོས་ཞེས་བྱ་བ་གོང་ན་མཚན་མཐུན་པ་ཡོད་པ་དེ་མཚན་མ་མཐུན༌[^417]པ་མི་དབང་ངོ་ཞེས༌[^418]བྱ་བའི་དོན་ཏོ། །

[Block 457]
གནས་ནས་ཕྱུང་བའི་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་ཅིག་ཤོས་ཡོད་ན་ཤི་བའི་ཡོ་བྱད་ལ་ཡང་གནས་ནས་ཕྱུང་བའི་མི་དབང་ངོ་ཞེས་བྱ་བ་འདིར་ཉེ་བར་གཞག་པའོ། །

[Block 458]
འདིར་གནས་ནས་ཕྱུང་བའི་ནི་ཅིག་ཤོས་ཉིད་ལ་མཐར་ཐུག་པའོ། །

[Block 459]
འདིར་གནས་ནས་མ་ཕྱུང་བ་ལ་ནི་ཅིག་ཤོས་ཀྱི་སྒྲའི་རྣམ་པར་གཞག་པའོ། །

[Block 460]
མེད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཅིག་ཤོས་ལའོ། །
--- END BLOCKS ---
