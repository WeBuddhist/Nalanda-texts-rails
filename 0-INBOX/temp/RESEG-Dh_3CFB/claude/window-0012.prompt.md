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
གཞན་དུ་དངོས་པོ་གཅིག་པུ་ལ། །
སྒྲ་འམ་བློ་གཅིག་གིས་ཁྱབ་ན། །
གཞན་ཡུལ་མ་ཡིན་དེ་ཡི་ཕྱིར། །
རྣམ་གྲངས་པ་ནི་ཉིད་དུ་འགྱུར། །

[Block 422]
ཞེས་བྱ་བ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པ་དག་གོ། །

[Block 423]
གང་གི་ལྟར་བློ་ཁྱད་པར་ནི།[^277] །སྣ་ཚོགས་ཅན་དོན་ཐ་དད་འཛིན། །གང་ཞིག་ཁྱད་པར་རྣམས་ནི་ཕན་ཚུན་དང་རྟེན༌[^278]ལས་ཐ་དད་པ་ཁོ་ན་ཡིན་ལ། དེའི་རྒྱུ་ཅན་གྱི་གཉེན་པོ༌[^279]དག་ནི་དེ་དག་གི་རྟེན༌[^280]ནམ་དེ་དག་ཁོ་ན་ལ་འཇུག་གོ། །

[Block 424]
དེ་བས་ན་ཐལ་པ་འདིར་མི་འགྱུར་རོ་སྙམ་དུ༌[^281]སེམས་པ་དེའི་ལྟར་ན་ཡང་། །

[Block 425 [VERSE]]
ཁྱད་པར་སྣ་ཚོགས་ལ་ཕན་པའི། །
ཡན་ལག་ནུས་ལས་མི་གཞན་པའི། །
བདག་ཉིད་བདག་ཉིད་ཀུན་གཟུང་ན། །
ཕན་བྱའི་བྱེ་བྲག་གང་མ་ངེས། །

[Block 426]
ཁྱད་པར་ཐ་དད་པ་དག་ཁོ་ན་དོན་ལ་སྒྲ་དང་། ཤེས་པ་གཞན་དག་གི་རྒྱུ་མཚན་ཡིན་དུ་ཟིན་ཀྱང་དེ་དང་ལྡན་པ་གཅིག་པུ་ཉིད་དེ་ནི་དེ་དག་གིས་ཉེ་བར་ལེན་ཏོ། །

[Block 427]
ཁྱད་པར་སྣ་ཚོགས་པ་ལ་ཕན་པའི་རྟེན་ནུས་པའི་ངོ་བོ་ཉིད་དེ་ནི་བདག་ཉིད་ལ་ཐ་དད་པ་མེད་པའི་ཕྱིར། བདག་ཉིད་ཐམས་ཅད་དུ་གཟུང་ན་ཁྱད་པར་གྱི་བྱེ་བྲག་མ་ངེས་པ་གང་ཞིག་ཡོད་དེ། ཁྱད་པར་ཐམས་ཅད་ལ་ཕན་འདོགས་པར་བྱེད་པ་ཉིད་དུ་གཟུང་བའི་ཕྱིར་རོ། །

[Block 428]
རང་གི་ངོ་བོ་གཟུང་བ་དེའི་ཕན་པར་བྱེད་པ་ཉིད་མ་བཟུང་བ་གཞན་ན༌[^282]ནི་མེད་པ་ཁོ་ནའོ། །

[Block 429]
དེའི་ཕྱིར་འདིའི་རང་གི་ངོ་བོར་གཟུང་བ་གང་ཡིན་པ་དེ་ཉིད་ཕན་པར་བྱེད་པ་ཉིད་དུ་ཡང་ཡིན་ནོ། །

[Block 430]
དེ་དག་བདག་ཉིད་ལ་འབྲེལ་ཕྱིར།[^283] །གཅིག་ཤེས་ན་ནི་གཉི་ག་གཟུང་། །ཁྱད་པར༌[^284]དེ་དང་ལྡན་པ་ཕན་པར་བྱ་བ་དང་། ཕན་པར་བྱེད་པའི་ངོ་བོ་བདག་ཉིད་དུ་གྱུར་པ་གཟུང་བའི་ཕྱིར་གཅིག་ཤེས་ན༌[^285]གཉི་ག་གཟུང་བས༌[^286]དེ༌[^287]ཁྱད་པར༌[^288]དུ་བྱས་པ་གཟུང༌[^289]ན་ཡང་ཁྱད་པར༌[^290]ཐམས་ཅད་གཟུང་བ་ཡིན་ཏེ། ཁྱད་པར་དང་ལྡན་པ་འཛིན་པ་ནི་དེ་འཛིན་པ་མེད་ན་དེ༌[^291]མེད་པའི་ཕྱིར་རོ། །

[Block 431]
གཞན་དུ་ན་དེ་ལྟར་ཡང་འཛིན་པར་མི་འགྱུར་རོ། །

[Block 432]
གཞན་ལ་ཕན་པར་བྱེད་པ་གང་ཞིག་མ་བཟུང་བར་གྱུར་པ་གཞན་ནི་མེད་པ་ཉིད་དོ། །

[Block 433]
ཕན་པར་བྱེད་པ་དེ་ལྟར་གཟུང་ན༌[^292]ཕན་པར་བྱ་བ་མ་བཟུང་བ་ཡང་མེད་དེ། དེ་ལ་ཡང་མ་བཟུང་བར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རྗེ༌[^293]ཁོལ་བཞིན་ནོ། །

[Block 434]
དེའི་ཕྱིར་ཁྱད་པར་དོན་གཞན་ཡིན་པར་སྨྲ་བ་ལ་ཡང་ཐལ་བར་འགྱུར་བར་མཚུངས་སོ། །

[Block 435]
འོན་ཏེ་གང་དག་གིས་ཁྱད་པར་ལ་ཕན་འདོགས་པའི་ནུས་པ་དག་ནི་ཐ་དད་པ་ཁོ་ན་སྟེ། དེའི་ཕྱིར་ཐལ་བ་འདིར་མི་འགྱུར་རོ་སྙམ་དུ་སེམས་ན།

[Block 436 [VERSE]]
ཆོས་ཕན་ནུས་རྣམས་ཐ་དད་ན། །
དེ་དག་དེའི་ཅི་ཡིན་གལ་ཏེ། །
དེ་ལས་དེ་དག་ལ་ཕན་མེད། །
དེ་ལྟ་ཡིན་ནི༌[^294]ཐུག་མེད་འགྱུར། །

[Block 437]
གལ་ཏེ་ཁྱད་པར་རེ་རེ་ལ་ཕན་པར་བྱེད་པ་ཉིད་དག་ཡིན་ན་ནི་དེའི་རང་གི་བདག་ཉིད་དུ་གྱུར་པ་དག་མ་ཡིན་པ་ཁོ་ན་སྟེ། དེ་ལས་ཕན་པ་ཉམས་སུ་མྱོང་བ་ཡང་མེད་ན་ཅི་སྟེ་དེའི་དེ་དག་ཡིན་ཞེས་བྱ། འོན་ཏེ་ཕན་ན༌[^295]འདི་གཅིག་པུས་རང་གི་བདག་ཉིད་དུ་གྱུར་པའི་ནུས་པ་དག་གིས་ནུས་པ་ལ་ཕན་པ་བྱེད་པ་ན་ཁྱད་པར་གཅིག་གིས་གཟུང་ན་ཡང་བདག་ཉིད་ཐམས་ཅད་དུ་གཟུང་བ་ཁོ་ན་ཡིན་ཏེ། འདི་ལྟར་ཁྱད་པར་གཟུང་ན་དེ་ལ་ཕན་འདོགས་པའི་ནུས་པ་བཟུང་བ་ཡིན་ནོ། །

[Block 438]
དེ་གཟུང་ན་དེ་ལ་ཕན་པར་བྱེད་པའི་དངོས་པོ་ནུས་པ་ལ་ཕན་པ་རང་གི་བདག་ཉིད་དུ་གྱུར་པ་མཐའ་དག་དང་ལྡན་པ་གཟུང་བས་ཐམས་ཅད་ཀྱི་ནུས་པ་འཛིན་པར་བྱེད་ལ། དེ་དག་གིས་ཀྱང་ཁྱད་པར་རྣམ་པར༌[^296]འཛིན་པར་བྱེད་པས་ཐལ་བར་འགྱུར་པ་སོ་ན་འདུག་པ་ཡིན་ནོ། །

[Block 439]
འོན་ཏེ་ནུས་པ་ལ་ཕན་འདོགས་པའི་ནུས་པ་དེ་དག་ཀྱང་དངོས་པོ་ལས་ཐ་དད་པ་ཁོ་ན་ཡིན་ན། དེ་ལྟར་ན་ཁྱད་པར་དང་དེའི་ནུས་པ་རྣམས་ནུས་པ་གཞན་དག་ཁོ་ན་ལ་མཐར་ཐུག་པ་མེད་པར་སྦྱོར་བའི་ཕྱིར། དེ་ལ་ཕན་པའི་བདག་ཉིད་དེ་གཅིག་པུ་ནམ་ཡང་དེ་དག་དང་མ་བཟུང་བས་དེ་དང་ལྡན་པ་ཉིད་དུ་འཛིན་པར་མི་འགྱུར་རོ། །

[Block 440]
ཡང་གལ་ཏེ་སྒྲ་དང་ཤེས་པ་རྣམས་ཀྱི༌[^297]ཁྱད་པར་བདག༌[^298]ཉི་ཚེ་ལ་ཉེ་བར་སྦྱོར་བར་འགྱུར་ལ། དེའི་ཚེ་དེ༌[^299]དང་མ་འབྲེལ་བའི་ཕྱིར་དེ་རྟོགས་པའི་སྒོ་ནས་ཐམས་ཅད་རྟོགས་པར་མི་འགྱུར་རོ་ཞེ་ན། དེའི་ཚེ་ཡང་སྒྲ་དག་གིས་དེ་མ་འཕངས་པའི་ཕྱིར། དེ་ལ་སྒྲ་མི་འཇུག་པས༌[^300]སྒྲ་སྦྱོར་བ་དེ་མེད༌[^301]པར་འགྱུར་ཏེ། སྒྲུབ་པ་དང་དགག་པ་དག་གིས་ཐ་སྙད་ཐམས་ཅད་ནི་དོན་བྱེད་པའི་རྟེན་ཅན་ཡིན་པས་སོ། །

[Block 441]
ཁྱད་པར་རྣམས་ཀྱིས༌[^302]ནི་དེར་མི་ནུས༌[^303]ལ་ནུས་པ་ནི་མི་བརྗོད་པས་སྒྲ་སྦྱོར་བ་དག་གིས་ཅི་ཞིག་བྱ། དེའི་ཕྱིར་ཁྱད་པར་རྣམས་ནི་ཁྱད་པར་ཡང་མ་ཡིན་པར་འགྱུར་ཏེ། འགའ་ཞིག་ལ་ཞུགས་ན་ནི་གཙོ་བོ་འགའི་ཡན་ལག་ཏུ་གྱུར་པའི་ཕྱིར། དེ་ལ་ལྟོས་ནས་དེ་སྐད་ཅེས་བརྗོད་དོ། །

[Block 442]
སྒྲ་དག་གིས་དེ་མི་འཕེན་ན་ནི་དེ་དག་གང་གི་ཡང་ཡན་ལག་ཏུ་གྱུར་པ་མ་ཡིན་པས་ཅི་སྟེ་ཁྱད་པར་དག་ཡིན། གལ་ཏེ་ཤེས་པར་བྱས་པས་མཚོན་པའི༌[^304]ཕྱིར་ཉེས་པ་མེད་དོ་ཞེ་ན། ཐལ་བར་འགྱུར་བར་མཚུངས་ཏེ། རེ་ཞིག་མེད་ན་མེད་པའི༌[^305]ཕྱིར་ཁྱད་པར་དེ་དག་གིས་དེ་ཉེ་བར་མཚོན་པ་ན་གཅིག་གིས་ཉེ་བར་མཚོན་ན་ཡང་བདག་ཉིད་ཐམས་ཅད་ཉེ་བར་མཚོན་པ་ཡིན་པས་ཐལ་བར་འགྱུར་བ་སོན་འདུག་པ་ཡིན་ནོ། །

[Block 443]
འདི་སྒྲས་ཉེ་བར་མཚོན་པར་བྱེད་ཀྱང་རུང་། དེས་ཉེ་བར་མཚོན་པའི་ཁྱད་པར་དག་གིས་ཉེ་བར་མཚོན་པར༌[^306]བྱེད་ཀྱང་རུང་སྟེ། འདི་ལ་ཁྱད་པར་ཅི་ཞིག་ཡོད། རེ་ཞིག་དེའི་ཚེ་དེ་ཐམས་ཅད་ལ་ཕན་པར་བྱེད་པ་པོ་ཡིན་ནོ་ཞེས་བྱ་བར་ངེས་པར༌[^307]བྱེད་པས་དེ་ནི་གྱི་ནའོ། །

[Block 444]
དེའི་ཕྱིར།

[Block 445 [VERSE]]
གཅིག་ལ་ཕན་བྱེད་གཟུང་ན་ནི། །
དེ་ལས་མཐོང་ལ་མ་མཐོང་བ། །
ཕན་པ་གཞན་མིན་དེ་ཡི་ཕྱིར། །

[Block 446]
དེ་གཟུང༌[^308]ན་ནི་ཐམས་ཅད་གཟུང་།[^309] །ཞེས་བྱ་བ་ནི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 447 [VERSE]]
གལ་ཏེ་འཁྲུལ་པ་བཟློག་པའི་ཕྱིར། །
གཟུང་བ་ལ་ཡང་གཞན་འདོད་ན། །

[Block 448]
གལ་ཏེ་འདི་སྙམ་དུ་དངོས་པོ་ཆ་མེད་པ་གཟུང་ན། དེའི་ཚེ་མ་བཟུང་བ་གཞན་ཅི་ཞིག་ཡོད་དེ། [^310]དེ་ནི་འཁྲུལ་པས་ངེས་པར་མི༌[^311]འཛིན་པས་ཚད་མ་གཞན་འཇུག་གོ་སྙམ་དུ་སེམས་ན། གལ་ཏེ་དེ་ལྟ་ན། །

[Block 449 [VERSE]]
དེ་རྣམ་གཅོད་པའི་ཡུལ་ཅན་གྲུབ། །
དེ་ལས་གཞན་ལའང་དེ་དང་འདྲ། །
སྒྲོ་འདོགས་མེད་པའི་ཡུལ་ལ་ནི། །

[Block 450]
འཇུག་ཕྱིར། འཁྲུལ་པ་བཟློག་པའི་ཕྱིར་ཞུགས་པའི་ཚད་མ་དེ་ནི་གཞན་སྒྲོ་འདོགས་པ་རྣམ་པར་གཅོད་པའི་འབྲས་བུ་ཅན་ཡིན་པས། གཞན་སེལ་བའི་ཡུལ་ཅན་དུ་གྲུབ་ལ། གཞན་ཡང་དེ་དང་འདྲ་སྟེ། སྒྲོ་འདོགས་པ་མེད་པའི་ཡུལ་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 451]
གང་ལ་འདིའི་སྒྲོ་འདོགས་པ་ཡོད་པ་དེ་ལ་ངེས་པ་མེད་པ་དེའི་ཕྱིར་སྒྲོ་འདོགས་པ་མེད་པ་ལ་འཇུག་པ་ནི་གཞན་སེལ་བའི་ཡུལ་ཅན་དུ་འགྲུབ༌[^312]བོ། །

[Block 452]
གཞན་ཡང་ངོ་བོ་གང་། །

[Block 453 [VERSE]]
ངེས་པ་རྣམས་ཀྱིས་མ་ངེས་པ། །
དེ་ནི་ཇི་ལྟར་དེ་དག་ཡུལ། །

[Block 454]
ངེས་པ་རྣམས་ཀྱིས༌[^313]རང་གི་དོན་རྟོགས་པ་ནི་ངེས་པ༌[^314]གང་ཡིན་པ་འདི་ཁོ་ན་ཡིན་ན། གལ་ཏེ་རྣམ་པ་གཞན་བཞིན་དུ་མ་ངེས་ན། ཇི་ལྟར་དེ་དག་གིས་གཟུང་བ་ཡིན། ད་ནི་ཇི་ལྟར་མ་ངེས་པ་མངོན་སུམ་གྱིས་ཀྱང་གཟུང་བ་ཡིན་ཞེ་ན། མངོན་སུམ་ནི་གང་གི་ཡང་ངེས་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེས་གང་ཞིག་འཛིན་པ་དེ་ཡང་ངེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 455]
འོ་ན་ཅི་ཞེ་ན། དེར་སྣང་བས་སོ། །

[Block 456]
དེ་བས་ན་ངེས་པ་དང་མ་ངེས་པའི་དབང་གིས་མངོན་སུམ་གྱིས་འཛིན་པ་དང་མི་འཛིན་པ་དག་མ་ཡིན་ནོ། །

[Block 457]
ངེས་པ་རྣམས་ཀྱིས་ནི་དེ་ལྟར་མ་ཡིན་ཏེ། འགའ་ཞིག་ངེས་ཀྱང་གཞན་ལ་མ་ངེས་པས་འཇུག་པ༌[^315]ཐ་དད་པས་འཛིན་པ་དང་མི་འཛིན་པ་ཡིན་ནོ། །

[Block 458]
དེའི་ཕྱིར་ངེས་པ་གང་ཡིན་པ་དེ་ཉིད་འདི་འཛིན་པ་ཡིན་ནོ། །

[Block 459]
དེ་ལྟ་མ་ཡིན་ན་རྣམ་པ་གཅིག་ལ་ཡང་དེར་མི་འགྱུར་རོ། །

[Block 460]
ཡང་ཅིའི་ཕྱིར་ཐམས་ཅད་པས༌[^316]ཐ་དད་པའི་དངོས་པོའི་ངོ་བོ་ལ་ཉམས་སུ་མྱོང་བ་སྐྱེས་ཀྱང་དེ་ཁོ་ན་བཞིན་དུ་དྲན་པའི་ངེས་པ་མི་འབྱུང་ཞེ་ན། ལྷན་ཅིག་བྱེད་པ་མ་ཚང་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
