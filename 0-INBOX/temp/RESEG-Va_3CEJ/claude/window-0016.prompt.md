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
ཡིད་ཀྱི་དྲན་པ་ཉིད་མཉམ་པར་གཞག་པ་དང་མཉམ་པར་གཞག་པ༌[^231]མ་ཡིན་པ་ཐམས་ཅད་ནི་རྗེས་སུ་དྲན་པའི་རྣམ་པར་རྟོག་པ་ཡིན་ནོ། །

[Block 562 [HEADING]]
#### དམིགས་པ་དང་བཅས་པ་དང་དམིགས་པ་མེད་པ། ^1-3-8-0

[Block 563]
དམིགས་པ་དང་བཅས་པ་རྣམས་ནི་དུ། དམིགས་པ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན། དམིགས་བཅས་སེམས་ཀྱི་ཁམས་བདུན་ནོ། །

[Block 564]
མིག་དང་། རྣ་བ་དང་། སྣ་དང་ལྕེ་དང་། ལུས་དང་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་རྣམས་དང་། ཡིད་ཀྱི་ཁམས་ཏེ། སེམས་ཀྱི་ཁམས་བདུན་པོ་དེ་དག་ནི་ཡུལ་འཛིན་པའི་ཕྱིར་དམིགས་པ་དང་བཅས་པ་དག་གོ། །

[Block 565]
ཆོས་ཀྱི་སྐྱེ་མཆེད༌[^232]ཀྱང་། དམིགས་པ་དང་བཅས་པ་ཡིན་ཏེ། སེམས་ལས་བྱུང་བའི་རང་བཞིན་གང་ཡིན་པའོ། །

[Block 566]
ལྷག་མ་གཟུགས་ཅན་གྱི་ཁམས་བཅུ་པོ་དག་དང་། ཆོས་ཀྱི་ཁམས་ཀྱི་ཕྱོགས་ལྡན་པ་མ་ཡིན་པ་ནི་དམིགས་པ་མེད་པ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 567 [HEADING]]
#### ཟིན་པ་དང་མ་ཟིན་པ། ^1-3-9-0

[Block 568]
ཟིན་པ་རྣམས་ནི་དུ། མ་ཟིན་པ་རྣམས་ནི་དུ་ཞེ་ན། མ་ཟིན༌[^233]དགུ། དགུ་གང་ཞེ་ན། དམིགས་པ་དང་བཅས་པ་བདུན་བརྒྱད་པའི་ཕྱེད་དང་བཅས་ཏེ་བཤད་པ་གང་དག་ཡིན་པ། བརྒྱད་པོ་དེ་དག་རྣམས་དང་སྒྲ། །དེ་ལྟར་ན་སེམས་ཀྱི་ཁམས་བདུན་དང་། ཆོས་ཀྱི་ཁམས་དང་། སྒྲའི་ཁམས་དང་། ཁམས་དགུ་པོ་དེ་དག་ནི་མ་ཟིན་པ་ཡིན་ནོ། །

[Block 569]
དགུ་པོ་གཞན་ནི་རྣམ་པ་གཉིས། །ཟིན་པ་དག་ཀྱང་ཡིན། མ་ཟིན་པ་དག་ཀྱང་ཡིན་ཏེ། དེ་ལ་མིག་དང་རྣ་བ་དང་སྣ་དང་ལྕེ་དང་ལུས་དང༌[^234]ད་ལྟར་བྱུང་བ་རྣམས་ནི་ཟིན་པ་ཡིན་ནོ། །

[Block 570]
འདས་པ་དང་མ་འོངས་པ་རྣམས་ནི་མ་ཟིན་པ་ཡིན་ནོ། །

[Block 571]
གཟུགས་དང་། དྲི་དང་། རོ་དང་། རེག་བྱའི་ཁམས་ད་ལྟར་བྱུང་བ་དབང་པོ་དང་ཐ་མི་དད་པ་རྣམས་ནི་ཟིན་པ་ཡིན་ནོ། །

[Block 572]
གཞན་དག་ནི་མ་ཟིན་པ་རྣམས་ཏེ། འདི་ལྟ་སྟེ་རྩ་བ་མ་གཏོགས་པའི་སྐྲ་དང་། བ་སྤུ་དང་། སེན་མོ་དང་། སོ་དག་ལ་ཡོད་པ་དང་། ཕྱི་ས་དང་། གཅིན་དང་། མཆིལ་མ་དང་། སྣབས་དང་། ཁྲག་ལ་སོགས་པ་དག་ལ་ཡོད་པ་དང་། ས་དང༌[^235]ཆུ་ལ་སོགས་པ་དག་ལ་ཡོད་པ་ལྟ་བུའོ། །

[Block 573]
ཟིན་པ་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། ཕན་པ་དང་གནོད་པ་དག་གིས་ཕན་ཚུན་མཐུན་པར་བྱེད་པའི་ཕྱིར་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱིས་རྟེན་གྱི་དངོས་པོར་ཉེ་བར་གཟུང་བ་སྟེ། འཇིག་རྟེན་གྱི་ན་སེམས་པ་དང་བཅས་པ་ཞེས་བརྗོད་པ་གང་ཡིན་པའོ། །

[Block 574 [HEADING]]
#### འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པ། ^1-3-10-0

[Block 575]
ཁམས་དུ་དག་གཅིག་ནི་འབྱུང་བའི་ངོ་བོ་ཉིད་ཡིན། དུ་དག་གཅིག་ནི་འབྱུང་བ་ལས་གྱུར་པ་ཡིན་ཞེ་ན། རེག་བྱ་རྣམ་པ་གཉིས་ཡིན་ཏེ། འབྱུང་བ་དག་དང་། འབྱུང་བ་ལས་གྱུར་པའོ། །

[Block 576]
དེ་ལ་འབྱུང་བ་དག་ནི་བཞིའོ། །

[Block 577]
འབྱུང་བ་ལས་གྱུར་པ་ནི་འཇམ་པ་ཉིད་ལ་སོགས་པ་རྣམ་པ་བདུན་ཏེ།

[Block 578 [VERSE]]
འབྱུང་བ་དག་ལ་ཡོད་པའི་ཕྱིར་རོ། །
ལྷག་མ་གཟུགས་ཅན་དགུ་པོ་ནི། །

[Block 579]
འབྱུང་གྱུར། [^236]དབང་པོ་ལྔའི་ཁམས་དག་དང་ཡུལ་བཞི་སྟེ། ཁམས་དགུ་པོ་དེ་རྣམས་ནི་འབྱུང་བ་ལས་གྱུར་པ་དག་ཁོ་ནའོ། །

[Block 580]
ཆོས་ཁམས་ཕྱོགས་གཅིག་ཀྱང་། འབྱུང་བ་ལས་གྱུར་པ་སྟེ། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཞེས་བྱའོ། །

[Block 581]
ལྷག་མ་སེམས་ཀྱི་ཁམས་བདུན་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་མ་གཏོགས་པ་ཆོས་ཀྱི་ཁམས་ནི་གཉིས་ག་མ་ཡིན་པའོ། །

[Block 582]
བཙུན་པ་སངས་རྒྱས་ལྷ་ན་རེ་ནི་སྐྱེ་མཆེད་བཅུ་པོ་དག་ནི་འབྱུང་བ་ཙམ་མོ་ཞེས་ཟེར་རོ། །

[Block 583]
དེ་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། མདོ་ལས་འབྱུང་བ་རྣམས་ནི་བཞི་ཉིད་དང་། སྲ་བ་ལ་སོགས་པའི་མཚན་ཉིད་དུ་ངེས་པར་གཟུང་བའི་ཕྱིར་ལ། དེ་དག་ཀྱང་རེག་བྱ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 584]
མིག་ལ་སོགས་པས་ཀྱང་སྲ་བ་ལ་སོགས་པ་མི་འཛིན་ལ། ལུས་ཀྱི་དབང་པོས་ཀྱང་ཁ་དོག་ལ་སོགས་པ་མ་ཡིན་ནོ། །

[Block 585]
མདོ་ལས་ཀྱང་དགེ་སློང་མིག་ནི་ནང་གི་སྐྱེ་མཆེད་ཡིན་ཏེ། འབྱུང་བ་ཆེན་པོ་བཞི་དག་རྒྱུར་བྱས་པ་གཟུགས་དང་བ་གཟུགས་ཅན་བསྟན་དུ་མེད་ལ་ཐོགས་པ་དང་བཅས་པ་སྟེ་ལུས་ཀྱི་བར་དུ་ཡང་དེ་བཞིན་ནོ། །

[Block 586]
དགེ་སློང་གཟུགས་རྣམས་ནི་ཕྱིའི་སྐྱེ་མཆེད་ཡིན་ཏེ། འབྱུང་བ་ཆེན་པོ་བཞི་དག༌[^237]རྒྱུར་བྱས་པ་གཟུགས་ཅན་བསྟན་དུ་ཡོད་ལ་ཐོགས་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 587]
དགེ་སློང་སྒྲ་ནི་ཕྱིའི་སྐྱེ་མཆེད་ཡིན་ཏེ། འབྱུང་བ་ཆེན་པོ་བཞི་དག་རྒྱུར་བྱས་པ་གཟུགས་ཅན་བསྟན་དུ་མེད་ལ་ཐོགས་པ་དང་བཅས་པ་སྟེ། དྲི་དང་རོ་ཡང་དེ་བཞིན་ནོ། །

[Block 588]
དགེ་སློང་རེག་བྱ་རྣམས་ནི་ཕྱིའི་སྐྱེ་མཆེད་ཡིན་ཏེ། འབྱུང་བ་ཆེན་པོ་བཞི་དག་དང་། འབྱུང་བ་ཆེན་པོ་བཞི་དག་རྒྱུར་བྱས་པ་གཟུགས་ཅན་བསྟན་དུ་མེད་ལ་ཐོགས་པ་དང་བཅས་པའོ་ཞེས་གསུངས་ཏེ། རེག་བྱའི་སྐྱེ་མཆེད་ཀྱི་ཕྱོགས་གཅིག་ཁོ་ནས་འབྱུང་བ་རྣམས་བསྡུས་པའི་ཕྱིར་ལྷག་མ་རྣམས་ནི་འབྱུང་བ་དག་མ་ཡིན་ནོ་ཞེས་བྱ་བར་གསལ་བར་ཀུན་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 589]
འོ་ན་མདོ་ལས།

[Block 590]
གང་མིག་གི་ཤའི༌[^238]གོང་བུ་ལ་སྲ་བ་མཁྲང་བར་གྱུར་པ་གང་ཡིན་པ་ཞེས་གསུངས་སོ། །

[Block 591]
དེ་དང་ཐ་མི་དད་པར་འཇུག་པའི་ཤའི༌[^239]གོང་བུ་ལ་དེ་སྐད་དུ་བསྟན་པར་ཟད་དོ། །

[Block 592]
མངལ་དུ་འཇུག་པ་ལས།

[Block 593]
དགེ་སློང༌[^240]འདི་ནི་ཁམས་དྲུག་པ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 594]
སེམས་ཅན་གྱི་རྫས་ཀྱི་གཞི་བསྟན་པའི་ཕྱིར་ཏེ། ཡང་རེག་པའི་སྐྱེ་མཆེད་དྲུག་ཅེས་གསུངས་པའི་ཕྱིར་དང་། སེམས་ལས་བྱུང་བ་རྣམས་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 595]
སེམས་ཉིད་སེམས་ལས་བྱུང་བ་རྣམས་ཡིན་ནོ་ཞེས་བྱ་བར་ཁས་བླངས་པར་རིགས་པ༌[^241]ཡང་མ་ཡིན་ཏེ།

[Block 596]
མདོ་ལས།

[Block 597]
འདུ་ཤེས་དང་སེམས་པའི་ཆོས་འདི་ནི་སེམས་ལས་བྱུང་བ་སེམས་ལ་བརྟེན་པའོ་ཞེས་འབྱུང་བའི་ཕྱིར་དང་། སེམས་འདོད་ཆགས་དང་བཅས་པ་ལ་སོགས་པ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 598]
དེ་ལྟ་བས་ན་ཁམས་རྣམས་ཀྱི་འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པ་ཉིད་ནི་ཇི་སྐད་བཤད་པ་བཞིན༌[^242]ཡིན་ནོ། །

[Block 599 [HEADING]]
#### བསགས་པ་དང་བསགས་པ་མ་ཡིན་པ། ^1-3-11-0

[Block 600]
བསགས་པ་རྣམས་ནི་དུ། བསགས་པ་མ་ཡིན་པ་རྣམས་ནི་དུ་ཞེ་ན། གཟུགས་ཅན་བཅུ་ནི་བསགས་པའོ། །
--- END BLOCKS ---
