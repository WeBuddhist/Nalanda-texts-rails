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
[Block 561]
གལ་ཏེ་ཐ་མི་དད་པའི་བརྗོད་པ་དང་། བློའི་རྒྱུ་མཚན་དུ་གྱུར་པ་གཅིག༌[^404]སྤྱི་ཡིན་གྱི་ཐམས་ཅད་ནི་མ་ཡིན་ནོ་ཞེ་ན། ཇི་ལྟར་གཞན་གྱི་སྒོ་ནས་གཞན་ལ་ཤེས་པ་འཇུག །དེ་དང་འབྲེལ་པའི་ཕྱིར་རོ་ཞེ་ན། གྲངས་དང་འབྲས་བུའི་རྫས་ལ་སོགས་པ་ཡོད་ན་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 562]
གལ་ཏེ་སྤྱིའི་བདག་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེ་ན། སྤྱིའི་བདག་ཉིད་འདི༌[^405]གང་ཡིན་ཞེས་དེ་ཉིད་དཔྱོད་པ་མ་ཡིན་ནམ། དེ་ལ་འབྲེལ་པ་ཡོད་ན་ཤེས་པ་འཇུག་སྟེ། དེས་ན་སྤྱི་ཡིན་ནོ་ཞེས་སྨྲས་པ་དེ་ལ་བཤད་པ༌[^406]རྒྱུ་མཚན་སྲིད་པའི་ཕྱིར་རྫས་ལ་སོགས་པ་དུ་མ་དང་འབྲེལ་པ་ཅན་དག་ལས་ཀྱང་ཤེས་པ༌[^407]འཇུག་སྟེ། དེའི་ཕྱིར་སྤྱིའི་བདག་ཉིད་ཡིན་ནོ། །

[Block 563]
དེ་ལྟ་མ་ཡིན་ན་གཞན་ལ་ཡང་མི་འཇུག་སྟེ། ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 564]
དེ་ལྟ་ན་ནི་རྫས་དང་ཡོན་ཏན་དང་སྤྱི་རྣམས་ཀྱི་ངོ་བོ་འཆོལ་བ་ཡིན་ནོ། །

[Block 565]
དེ་ལྟ་ན་འོ་ན་ནི། བློའི་སྣང་བ་ཁོ་ན་ཤེས་པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་ཡོད་པ་ཉིད་པས་སྤྱི་ཡིན་ནོ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། འདི་ལྟར། ཤེས་དང་ཐ་དད་མ་ཡིན་པ། ཇི་ལྟར་དོན་གཞན་འབྲང་བར་འགྱུར། །ཤེས་པ་པོའི་ངོ་བོ་ཇི་ལྟར་དོན་གཞན་རྣམས་ཀྱི་སྤྱི་ཡིན་ཏེ། དེ་ནི་དེ་རྣམས་ལ་མེད་པའི་ཕྱིར་རོ། །

[Block 566]
གལ་ཏེ་དེའི་ངོ་བོ༌[^408]ཞེན་པའི་ཕྱིར། དེ་ལྟར་འཁྲུལ་པས་ཐ་སྙད་འདོགས་སོ་ཞེ་ན། དེ་ལ་དེ་ལྟར་ཤེས་པ་སྐྱེ་བའི་རྒྱུ་གང་ཞིག་ཡིན། རྟེན་མེད་པར་སྐྱེ་ན་ནི་ཐམས་ཅད་ལ་འགྱུར་རོ་རྣམ་པ་གཅིག་ཏུ་ན་ཤེས་པ་གཅིག་དང་། ཐ་དད་པ་མ་ཡིན་པ་ཇི་ལྟར་ཤེས་པ་གཞན་བསལ་བ༌[^409]གཞན་ལས་བྱུང་བའི༌[^410]ངོ་བོ་ཡིན། དེའི་ཕྱིར་ཤེས་པ་གཞན་དང་བསལ་བ༌[^411]གཞན་ལ་ཁྱད་པར་བྱེད་པ་མ་ཡིན་པ་ཇི་ལྟར་སྤྱི་ཡིན་པར་འགྱུར།

[Block 567 [VERSE]]
དེ་ལྟས༌[^412]དོན་ལ་གཅིག་བདག་ཏུ། །
འཛིན་པའི་རྣམ་རྟོག་འདི་འཁྲུལ་པ། །

[Block 568]
དོན་རྣམས་ནི་ཐ་དད་པའམ་ཐ་དད་པ་མ་ཡིན་པས་ཀྱང་རུང་བདག་ཉིད་གང་གིས་ཀྱང་མཚུངས་པ་མ་ཡིན་པས་དེ་རྣམས་ལ་དེ་ལྟར་འཛིན་པའི་རྣམ་པར་རྟོག་པ་ནི་འཁྲུལ་པ་ཡིན་ནོ། །

[Block 569 [VERSE]]
མིང་དོན་གང་ལྡན་ཕན་ཚུན་དུ། །
ཐ་དད་པ་འདིའི་ས་བོན་ཡིན། །

[Block 570]
བསྒྲུབ་པར༌[^413]བྱ་བ་ཐ་མི་དད་པ་ཅན་གྱི་དངོས་པོ་རྣམས་དེའི་བསྒྲུབ་པར་བྱ་བ་ཅན་མ་ཡིན་པ་དག་ལས་ཤེས་པར་བྱ༌[^414]སྟེ། དེ་དག་ཡོངས་སུ་སྤངས་ནས་འཇུག་པར་འགྱུར་བར་གང་ཞིག་ཤེས་པར་བྱ་བའི་ཕྱིར༌[^415]བརྡར་བྱེད་པ་ཕན་ཚུན་ཐ་དད་པ་དེ་ནི་ནོར་བའི་རྣམ་པར་རྟོག་པ་གཅིག་གི་བདག་ཉིད་དུ་སྣང་བ་ཅན་དེའི་ས་བོན༌[^416]ཏེ། རྣམ་པར་རྟོག་པ་འདི་ནི་དེ་ཁོ་ན་འཛིན་པ་ན་རང་གི་བག་ཆགས་ཀྱི་རང་བཞིན་ལས་དེ་ལྟར་སྣང་ངོ་། །

[Block 571]
ཡང་ཇི་ལྟར་ན་གང་གིས་ན་དེ་མ་ཡིན་པ་དག་ལས་ལོག་པའི་ཕྱིར་ཐ་མི་དད་པ་ཞེས་བརྗོད་པ། ཐ་དད་པ་རྣམས་ཀྱི༌[^417]འབྲས་བུ་ཐ་མི་དད་པ་ཡིན་ཞེ་ན། དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ནི་འདི་ལྟ་བུ་ཡིན་ཏེ། །

[Block 572 [VERSE]]
གཅིག་རྟོགས་དོན་ཤེས་ལ་སོགས་པ། །
དོན་གཅིག་བསྒྲུབ༌[^418]ལ་ཁ་ཅིག་ནི། །
ཐ་དད་ཡིན་ཡང་རང་བཞིན་གྱིས། །
ངེས་ཏེ་དབང་པོ་ལ་སོགས་བཞིན། །

[Block 573]
ཇི་ལྟར་དབང་པོ་དང་ཡུལ་དང་སྣང་བ་དང་། ཡིད་ལ་བྱེད་པ་རྣམས་སམ། བདག་དང་དབང་པོ་དང་ཡིད་དང་དོན་དང་དེ་རྣམས་ཕྲད་པས་དེའི་ངོ་བོར་ངེས་པའི་སྤྱི་མེད་ཀྱང་། གཟུགས་ཀྱི་རྣམ་པར་ཤེས་པ་གཅིག་བསྐྱེད་པ་དེ་བཞིན་དུ། ཤིང་ཤ་པ་ལ་སོགས་པ་ཐ་དད་པ་དག་ཀྱང་ཕན་ཚུན་རྗེས་སུ་མི་འགྲོ་བ་ཡང་རང་བཞིན་ཁོ་ནས་རྣམ་པ་གཅིག་ཏུ་མངོན་པར་ཤེས་པའམ། གཞན་མེ་དང་ཁྱིམ་ལ་སོགས་པ་ཤིང་གིས་བསྒྲུབ་པར་བྱ་བའི་དོན་བྱ་བ་རྐྱེན་ཇི་ལྟ་བ་བཞིན་དུ་སྐྱེད་པར་བྱེད་དོ། །

[Block 574]
ཐ་དད་པ༌[^419]ཁྱད་པར་མེད་ཀྱང་ཆུ་ལ་སོགས་པ་ནི་མ་ཡིན་ཏེ། གཟུགས་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པ་ལ་རྣ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 575 [VERSE]]
དཔེར་སྨན་ཁ་ཅིག་ཐ་དད་ཀྱང་། །
ལྷན་ཅིག་པའམ་སོ་སོ་ཡིས། །
རིམས་ལ་སོགས་པ་ཞི་བྱེད་པ། །
གཞན་གྱིས་མ་ཡིན་མཐོང་བ་བཞིན། །

[Block 576]
ཡང་ན་དཔེར་ན་སླེ་ཏྲེས༌[^420]ཀྱིས་བསལ་བ༌[^421]ལ་སོགས་པ་ལྷན་ཅིག་པའམ། སོ་སོས་རིམས་ལ་སོགས་པ་ཞི་བ་ལ་སོགས་པའི་མཚན་ཉིད་ཀྱི་འབྲས་བུ་གཅིག་བྱེད་པ་ལྟ་བུའོ། །

[Block 577]
དེ་ལ་སྤྱི་ལ་ལྟོས་པ་ནི་མེད་དོ། །

[Block 578]
ཐ་དད་ཀྱང་དེའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 579]
དེར་ཁྱད་པར་མེད་ཀྱང་ཞོ་དང་ག་གོན་ལ་སོགས་པ་ལས༌[^422]ནི་མ་ཡིན་ནོ། །

[Block 580]
གལ་ཏེ་འདི་སྙམ་དུ་དེ་ལྟ་བུ་དེ༌[^423]དག་ལ་སྤྱི་ཉིད་ཅུང་ཟད་ཅིག་ཡོད་དེ། དེ་ཁོ་ན་ལ་འབྲས་བུ་གཅིག་པ་དེར་འགྱུར་རོ་སྙམ་དུ་སེམས་ན། དེ་ནི་རིགས་པ་མ་ཡིན་ཏེ། སྤྱི་ཁྱད་པར་མེད་ཕྱིར་སྤྱིས་འབྲས་བུ་དེ་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 581]
དེ་དག་ཞིང་སོགས་ཐ་དད་ཀྱང་། །ཁྱད་པར་མེད་པར་ཐལ་འགྱུར་ཞིང་།[^424] །གལ་ཏེ་སྤྱི་ལས་རིམས་ལ་སོགས་པ་ཞི་བའི་འབྲས་བུར་འགྱུར་ན། དེ་ལ་ཁྱད་པར་མེད་པའི་ཕྱིར། །བསལ་བ༌[^425]རྣམས་ཀྱི་ཞིང་ལ་སོགས་པ་ཐ་དད་ཀྱང་། ཞི་བ་མྱུར་བ་དང་། བུམ་པ་ལ་སོགས་པའི་ཁྱད་པར་དང་། ཡོན་ཏན་མཆོག་དང་། ཆེས་མཆོག་ཏུ་ཡང་མི་འགྱུར་རོ། །

[Block 582]
འོན་ཏེ་སྤྱི་ལ་ཁྱད་པར་ཡོད་ན་ནི་ངོ་བོ་ཉིད་ཐ་དད་པའི་ཕྱིར་རང་གི་ངོ་བོ་ཉམས་པ་ཡིན་ནོ། །

[Block 583]
སྤྱི་བརྟན་པས་ཕན་འདོགས་མེད་ཕྱིར་ཡང་གལ་ཏེ་འདིས་ཕན་འདོགས་པར་བྱེད་ན་ནི། བོགས་དབྱུང་དུ་མེད་པ་ནི་གཞན་ལ་མི་ལྟོས་པའི་ཕྱིར། རང་གི་འབྲས་བུ་ཐམས་ཅད་ཅིག་ཅར་སྐྱེད་པར་འགྱུར་རོ། །

[Block 584]
ཡང་ན་ནི་བསྐྱེད་པའི་རང་བཞིན་མ་ཡིན་ནོ། །

[Block 585]
བསལ་བ༌[^426]དུས་དང་། ཡུལ་དང་ལེགས་པར་བྱ་བའི་དབང་གིས་ཁྱད་པར་འབྱུང་བ་ཅན་རྣམས་ནི་འབྲས་བུ་ཁྱད་པར་ཅན༌[^427]བྱེད་པ་ཞེས་བྱ་བ་ལ་འགལ་བ་མེད་དོ། །

[Block 586]
དེ་བཞིན་དུ་དོན་ཁ་ཅིག་ཀྱང་རང་གི་ངོ་བོ་ཐ་དད་ཀྱང་། གཅིག་ཏུ་མངོན་པར་ཤེས་པ་ལ་སོགས་པའི་དོན་བྱ་བ་བྱེད་པ་ན། དེ་མི་བྱེད་པ་ཅན་དག་ལས་ཐ་དད་པའི་ཕྱིར་རམ། གཅིག་གིས་དུ་མ་བསྐྱེད་པ་ན་དེས་བསྐྱེད་པར་བྱ་བ་མ་ཡིན་པ་དག་ལས་ཐ་དད་པའི་ཕྱིར། ཐ་མི་དད་པ་ཞེས་བྱའོ།[^428] །ཡང་ཅི་མཚན་ཉིད་ཐ་དད་པ་ཅན་གྱི་སྤྱི་འདི་རང་གི་མཚན་ཉིད་དང༌[^429]མཚུངས་སོ་ཞེས་བྱ་བར་ཤེས་པར༌[^430]བྱའམ། འོན་ཏེ་གཞན་ཁོ་ན་དང་ཡིན་ཞེ་ན། དེ་ལས་ཅིར་འགྱུར། གལ་ཏེ་རང་གི་མཚན་ཉིད་ཡིན་ན་ནི་ཇི་ལྟར་རྣམ་པར་རྟོག་པའི་ཡུལ་ཡིན། ཡང་ན་ནི་གཞན་གྱི་ཇི་ལྟར་དོན་བྱེད། རང་གི་མཚན་ཉིད་ལ་མི་རྟག་པ་ཉིད་ལ་སོགས་པ་མི་རྟོགས་པའི་ཕྱིར་དེའི་ངོ་བོ་མ་ཡིན་ལ། དེ་དག་ཀྱང་དངོས་པོའི་ཆོས་ཉིད་མ་ཡིན་ནོ་ཞེ་ན། དེས༌[^431]ནི་ཉེས་པ་མེད་དེ། ཤེས་པ་ལ་སྣང་བའི་དོན་ལ་སྤྱི་དང་གཞི་མཐུན་པ་དང་། ཆོས་དང་ཆོས་ཅན་གྱི་ཐ་སྙད་རྣམས་འདོགས་ཏེ། དངོས་པོའི་རང་གི་ངོ་བོ་འཛིན་པས་ཉམས་སུ་མྱོང་བས་གཞག་པའི་བག་ཆགས་ལ་བརྟེན་ནས་རྣམ་པར་རྟོག་པའི་བག་ཆགས༌[^432]སྐྱེ་བ་གང་ཡིན་པ་འདི་ནི་དེའི་ཡུལ་ཅན་མ་ཡིན་ཡང་། དེའི་ཡུལ་ཅན་ལྟ་བུ་དེ་ཉམས་སུ་མྱོང་བས་གཞག་པའི་བག་ཆགས་ལས་སྐྱེས་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར། དེའི་དངོས་པོར་ལྷག་པར་ཞེན་པའི་རང་གི་ངོ་བོ་ཅན་འབྲས་བུ་ཐ་མི་དད་པའི་དངོས་པོ་ལས་སྐྱེ་བའི་ཕྱིར། དོན་ཐ་མི་དད་པ་འཛིན་པ་ལྟ་བུ་དོན་དམ་པར་ན་དེ་ལས་གཞན་པ་ལས་ཐ་དད་པ་དང་། རྣམ་པ༌[^433]མཚུངས་པ་ཅན་ཡིན་ཏེ། དེ་ལ་དོན་གྱི་རྣམ་པ་ཡོད་པ་ནི་ཐ་སྙད༌[^434]འདོགས་པ་རྣམས་དེ་ལྟར་ལྷག་པར་ཞེན་ནས་འཇུག་པའི་ཕྱིར། ཕྱི་རོལ་ལྟ་བུ་དང་། གཅིག་པ་ལྟ་བུ་དང་། དོན་མི་བྱེད་ཀྱང་དེ་བྱེད་པ་ལྟ་བུར་སྣང་སྟེ། གཞན་དུ་ན་འཇུག་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 587]
དེ་ནི་དོན་བྱ་བ་བྱེད་པ་ཉིད་དུ་སྣང་བའི་ཕྱིར། དེ་ནི༌[^435]བྱེད་པ་དག་ལ་ཐ་དད་པ་ལྟ་བུ་སྟེ། དེ་ཡང་བརྟག་པའི༌[^436]ཡན་ལག་མ་ཡིན་པའི་ཕྱིར། དེ་ཁོ་ན་ཉིད་མ་ཡིན་ནོ་ཞེས་བཤད་པར་བྱའོ། །

[Block 588]
བློ་ལ་གནས་པའི་དོན་དེ་དག་ནི་དེ་དང་མཚུངས་སོ་ཞེས་བྱ་བར་འཛིན་ཏེ། འགའ་ཞིག་ལས་ལོག་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 589]
རང་གི་མཚན་ཉིད་ནི་མ་ཡིན་ཏེ། དེ་ལ་མི་སྣང་བའི་ཕྱིར་རོ། །

[Block 590]
དེ་དག་ཉིད་འགའ་ཞིག་ལས་ལོག་པ་ན་གཞན་ཡང་ལྡོག་པ་དང་ལྡན་པ་དང་། ཐ་མི་དད་པར་ཡང་སྣང་ངོ་། །བདག་ཉིད་ཀྱིས་མེད་ཀྱང་བློས་དེ་ལྟར་སྟོན་པའི་ཕྱིར། ནོར་བའི་དོན་ཁོ་ན་ལ་སྤྱི་དང་གཞི་མཐུན་པའི་ཐ་སྙད་འདོགས་སོ། །

[Block 591]
འདི་ཐམས་ཅད་རང་གི་མཚན་ཉིད་དག་ཁོ་ན་མཐོང་བས་གཞག་པའི་བག་ཆགས་ཀྱིས་བྱས་པའི་བསླད་པ༌[^437]ཡིན་པ་ལས་དེ་དང་འབྲེལ་པ་ལས་སྐྱེ་བའི་རྣམ་པར་རྟོག་པ་རྣམས་ནི་དེ་སྣང་བ་ཉིད་མ་ཡིན་ཡང་དངོས་པོ་ལ་མི་བསླུ༌[^438]སྟེ། ནོར་བུའི་འོད་ལ་ནོར་བུར་འཁྲུལ་པ་ལྟ་བུའོ། །

[Block 592]
གཞན་དག་ནི་མ་ཡིན་ཏེ། དེའི་ཁྱད་པར་ལས་རབ་ཏུ་སྐྱེ་བ་ཡིན་ཡང་ཇི་ལྟར་མཐོང་བའི་ཁྱད་པར་གྱི་རྗེས་སུ་འབྲང་བ་ཡོངས་སུ་བོར་ནས་འདྲ་བ་ཅུང་ཟད་ཙམ་གཟུང་བས༌[^439]ཁྱད་པར་གཞན་སྒྲོ་འདོགས་པའི་ཕྱིར་མར་མེའི་འོད་ལ་ནོར་བུའི་བློ་ལྟ་བུའོ། །

[Block 593]
དེའི་ཕྱིར་རྣམ་པར་རྟོག་པའི་ཡུལ་གྱི་དོན་རྣམས་ལ་དོན་བྱ་བ་བྱེད་པ་ཉིད་མེད་དོ། །

[Block 594]
རང་གི་མཚན་ཉིད་ལ་མི་རྟག་པ་ཉིད་ལ་སོགས་པ་མེད་པ་ཡང༌[^440]མ་ཡིན་ཏེ། འདི་ལྟར་དངོས་པོ་གཡོ་བ་ལ་མ་རྟོགས་པ་ཉིད་ཅེས་བྱ་བ་ནི་ཅུང་ཟད་ཀྱང་མེད་ཀྱི། དེ་དེ་ལྟ་བུ་ལ་སྐད་ཅིག་མར་གནས་པའི་ཆོས་ཉིད་དུ་གཟུང་བའི་ཕྱིར། འདི་སྙམ་དུ་འདི་ནི་མི་རྟག་པའོ། །

[Block 595]
འདི་ནི་མི་རྟག་པ་ཉིད་དོ་སྙམ་དུ་སེམས་སོ། །

[Block 596]
རྣམ་པར་རྟོག་པ་རྣམས་ནི་དེའི་ཆོས་ཉིད་ཁོ་ན་ལ་འཇུག་པ་ན་ཆོས་དུ་མ་དང་གཅིག་པ་དང་ཐ་དད་པ་དག་ཏུ་སྟོན་པར་བྱའོ།[^441] །དེ་རྣམས་རྟེན༌[^442]མེད་པ་ཡང་མ་ཡིན་ཏེ། དེའི་ཁྱད་པར་མཐོང་བ་ལ་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 597]
དངོས་པོ་མེད་པའི་ཆོས་ཉིད་ཀྱང་མ་ཡིན་ཏེ། དེའི་རང་གི་ངོ་བོ་ཁོ་ན་དེ་ལྟར་སྣང་བའི་ཕྱིར་རོ། །

[Block 598]
དངོས་པོ་ལ་དུ་མ་དང་གཅིག་པ་དང་ཐ་དད་པར་འཛིན་པ་ནི་འཁྲུལ་པར་འགྱུར་ཏེ། དོན་གཅིག་དང་དུ༌[^443]མ་བྱེད་པ་དེ་ལ་དེ་ལྟར་ཤེས་པར་འདོད་ན་དེ་ལྟ་བུའི་ངོ་བོ་བསྟན་པའི་ཆེད་དུ་དེ་ལྟར་གཞག་པར་བྱས༌[^444]པའི་ཕྱིར་རོ། །

[Block 599]
དངོས་པོའི་ཁྱད་པར་གྱི་སྒོ་ནས་ནི་མ་ཡིན་ཏེ། གཅིག་པོ་དེ་ལ་དུ་མ་ཉིད་མི་རུང་བའི་ཕྱིར་དང་། དུ་མ་ལའང་གཅིག་པ་ཉིད་མི་རུང་བའི་ཕྱིར་དང་། ཐ་དད་པ་ཡང་བཀག་པའི་ཕྱིར་རོ། །

[Block 600]
དེ་རྣམས་ཀྱི་རང་བཞིན་ཐ་དད་པའི་ཕྱིར། སྒྲའི་དོན་དངོས་པོ་ཇི་ལྟ་བ་བཞིན་ཡིན་པར་ཁས་ལེན་ན་གཞི་མཐུན་པ་ཉིད་མི་རུང་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
