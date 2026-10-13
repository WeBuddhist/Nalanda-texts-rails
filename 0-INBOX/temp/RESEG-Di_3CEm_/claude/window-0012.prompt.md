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
མཁས་པ་དེ་དང་ཞེས་བྱ་བ་ནི་དེ་ཉིད་ལ༌[^295]མཁས་པའོ། །

[Block 422]
མཚུངས་པར་སྤྱད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་མཐུན་པར་སྤྱད་པ་སྟེ། ཇི་ལྟར་བསྟན་པའི་དགེ་བའི་རྩ་བ་འདི་དག་ཐམས་ཅད་སྐད་ཅིག་རེ་རེ་ལ་ཡོངས་སུ་བསྔོ་བར་བྱ་བའོ། །

[Block 423]
ལུས་དང་ངག་དང་ཡིད་ཀྱང་རྣམ་དག་ཅིང་། །ཞེས་བྱ་བ་ནི་ལུས་དང་ངག་དང་ཡིད་རྣམས་ཀྱི་སྤྱོད་པ་རྣམ་པར་དག་པ་དང་ཞིང་རྣམས་རྣམ་པར་དག་པ་སྟེ། བསྔོ་བ༌[^296]བཟང་པོ་མཁས་པ་ཞེས་བྱ་བ་ནི་འཕགས་པ་ཀུན་དུ་བཟང་པོ་མཁས་པའོ། །

[Block 424]
ཅི་འདྲ་བར་ཞེས་བྱ་བ་ནི་ཇི་ལྟ་བུ་ཡིན་པར་རོ། །

[Block 425]
དེ་འདྲར་ཞེས་བྱ་བ་ནི་དེ་འདྲ་བར་བདག་ཀྱང་གྱུར་ཅིག་པའོ། །

[Block 426 [VERSE]]
མཚུངས་པར་ཞེས་བྱ་བ་ནི་འདྲ་བར་རོ། །
ཀུན་ནས་དགེ་བ་བཟང་པོ་སྤྱད་པའི༌[^297]ཕྱིར། །

[Block 427]
ཞེས་བྱ་བ་ནི་ཐོག༌[^298]མ་དང་ཐ་མ་དང་བར་དུ་དགེ་བའོ། །

[Block 428]
འཇམ་དཔལ་གྱི་ནི་སྨོན་ལམ་སྤྱད་པར་བགྱི།[^299] །ཞེས་བྱ་བ་ནི་ཚད་མེད་པ༌[^300]འཇམ་དཔལ་གྱི་སྨོན་ལམ་སྤྱོད་པར་ཤོག་ཤིག༌[^301]པའོ། །

[Block 429]
དེའི་སྨོན་ལམ་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 430]
གཞུང༌[^302]ལས།

[Block 431]
འཕགས་པ་འཇམ་དཔལ་ནམ་མཁའ་ཞེས་བྱ་བའི་རྒྱལ་པོར་གྱུར་པའི་ཚེ་འཁོར་བ་ཐོག༌[^303]མ་དང་ཐ་མ་དང་བྲལ་བ་ཇི་སྲིད་པ་དེ་སྲིད་དུ་སེམས་ཅན་རྣམས་ལ་ཚད་མེད་པའི་ཕན་པ་སྤྱད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱ་ཆེན་པོ་རྣམས་སོ། །

[Block 432]
མ་འོངས་བསྐལ་པ་ཀུན་དུ་མི་སྐྱོ་བར། །ཞེས་བྱ་བ་ནི་མ་འོངས་པའི་བསྐལ་པ་ཐམས་ཅད་དུ༌[^304]མ་ལུས་པར་མི་སྐྱོ་བའི་ཡིད་ཀྱིས་གཞན་དུ་མི་སེམས་པར་སངས་རྒྱས་དང་། བྱང་ཆུབ་སེམས་དཔའ་དེ་དག་གི་བྱ་བའི་ལས་མ་ལུས་པ་ཡོངས་སུ་རྫོགས་པར་བྱ་ཞིང་རབ་ཏུ་བསྒྲུབ་པར་བགྱིའོ། །

[Block 433 [HEADING]]
#### བསྡུ་བར་བྱ་བ། ^2-8-16-0

[Block 434]
སྦྱོར་བ་དང་ཡོན་ཏན་དང་སྤྱོད་པ་དང་གནས་དང་ཚད་མེད་པའི་ཁྱད་པར་བསྡུ་བ་ནི་རྣམ་པ་བཅུ་དྲུག་པ་སྟེ། དེ་ཡང་གང་ཞེ་ན། སྤྱོད་པ་དག་ནི་ཚད་ཡོད་མ་གྱུར་ཅིག །ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 435]
བདག་གི་སྤྱོད་པ་ཡང་ཚད་ཡོད་མ་གྱུར་ཅེས་བྱ་བ་ནི་ཚད་མེད་པར་གྱུར་ཅིག་པ་སྟེ། ཚད་མེད་པའི་སྤྱོད་པ་དང་། ཚད་མེད་པའི་ཡོན་ཏན་ལ་གནས་པས་དེ་ལྟར་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམ་པར་སྤྲུལ་པའི་འཕྲུལ་གྱི་ཡ་མཚན་ཐམས་ཅད་ཡོངས་སུ་ཤེས་པར་གྱུར་ཅིག་པའོ། །

[Block 436]
དེའི་བྱེ་བྲག་རྣམ་པ་བཅུ་དྲུག་སྟེ། དེ་ཡང་བརྒྱད་པའོ། །

[Block 437 [HEADING]]
### སྨོན་ལམ་གྱི་མཐའ། ^2-9-0

[Block 438]
ད་ནི་དེའི་མཐའ་སྟེ་རྣམ་པ་དགུ་པའོ། །

[Block 439]
བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་གྱི་མཐའ་དེ་ཡང་ནམ་མཁའ་ལ་སོགས་པ་དཔེར་བརྗོད་པ་རྣམ་པ་བཞི་སྟེ། དེ་ཡང་གང་ཞེ་ན། ནམ་མཁའི་མཐར་ཐུག་གྱུར་པ་ཇི་ཙམ་པ། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 440]
ཇི་ཙམ་ཞེས་བྱ་བ་ནི་ནམ་མཁའི་མཐའ༌[^305]ཇི་ཙམ་པ་སྟེ། ནམ་མཁའི་མཐའ་ཙམ་དུ་གྱུར་ཅིག་པའོ། །

[Block 441]
སེམས་ཅན་ཀུན་གྱི་མཐའ་ཇི་ཙམ་པ་དང་། འགྲོ་བ་རྣམས་ཀྱི་ལས་དང་ཉོན་མོངས་པའི་མཐའ་ཇི་ཙམ་པར་བདག་གི་བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་གྱི་མཐའ་ཡང་དེ་ཙམ་དུ་གྱུར་ཅིག་པའོ། །

[Block 442]
ནམ་མཁའ་ལ་སོགས་པ་ལ་ཡང་ཡོངས་སུ་ཟད་ཅིང་ཐུག་པ་མེད་དེ། དེ་ལྟར་བདག་གི་སྨོན་ལམ་འདིའི་མཐའ་ཡང་ཟད་ཅིང་ཐུག་པ༌[^306]མེད་པར་གྱུར་ཅིག་པའོ། །

[Block 443 [HEADING]]
### སྨོན་ལམ་གྱི་ཡོན་ཏན། ^2-10-0

[Block 444]
སྨོན་ལམ་གྱི་ཡོན་ཏན་ནི་རྣམ་པ་བཅུ་པ་སྟེ། ཚེ་འདི་དང་ཕ་རོལ་གྱི་རྣམ་པ་གཉིས་སོ། །

[Block 445 [HEADING]]
#### ཚེ་འདིའི་ཡོན་ཏན། ^2-10-1-0

[Block 446]
དེ་ལ་ཚེ་འདིའི་ནི་རྣམ་པ་བཞི་སྟེ། འདི་ལྟ་སྟེ། བསོད་ནམས་ཁྱད་པར༌[^307]ཅན་ཡོངས་སུ་སྡུད་པ་དང་། དེ་བཞིན་གཤེགས་པ་མཐོང་བ་དང་། བྱང་ཆུབ་སེམས་དཔའ་དང་སྐལ་བ་མཐུན་པ་ཐོབ་པ་དང་། ལས་ཀྱི་སྒྲིབ་པ་འབྱང་བ་རྣམས་སོ། །

[Block 447]
དེ་དངོས་པོ་ཆེ་བ་དང་རྒྱ་ཆེ་བ་དང་། སྣ་ཚོགས་ཀྱི་དངོས་པོ་བསྡུ་བ་དང་། ཞིང་ཁྱད་པར་ཅན་གྱི་དཔེ༌[^308]དང་། གང་གིས་བྱང་ཆུབ་ཐོབ་པར་བྱ་བའི་ཕྱིར་སྨོན་ལམ་འདི་ལ་དད་པས་བསོད་ནམས་ཁྱད་པར་ཅན་ཡོངས་སུ་སྡུད་པར་འགྱུར་ཏེ། དེ་ཡང་གང་ཞེ་ན། གང་ཡང་ཕྱོགས་བཅུའི་ཞིང་རྣམས་མཐའ་ཡས་པ། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 448]
འདི་ལྟར་རིགས་ཀྱི་བུ་ཕོའམ་རིགས་ཀྱི་བུ་མོ༌[^309]གང་གིས་ཕྱོགས་བཅུ་མཐའ་ཡས་པ་མུ་མེད་པ་ན་སངས་རྒྱས་ཀྱི་ཞིང་རྣམས་རིན་པོ་ཆེ་སྣ་ཚོགས་དང་། ན་བཟའ་དང་། བླ་རེ་དང་། གདུགས་དང་། རྒྱལ་མཚན་དང་། བ་དན་དང་། རིན་པོ༌[^310]ཆེའི་དྲིལ་བུའི་ཕྲེང་བ་དང་སྤོས་དང་། མེ་ཏོག་དང་། བདུག་པ་དང་། མར་མེ་དང་། ཕྲེང་བ་ལ་སོགས་པ་དང་། སིལ་སྙན་མིའི་ལས་འདས་པ་འཕྲུལ་གྱི་རྒྱན་རྣམས་ཀྱིས་རབ་ཏུ་བརྒྱན་པ་དང་། མིའི་མ་ཡིན་པའི་འཕྲུལ་གྱི་ཞལ་ཟས་རོ་ལྔ་བརྒྱ་དང་ལྡན་པ་མཆོག་ཏུ་བདེ་བ་བསྐྱེད་པ༌[^311]རྣམས་སངས་རྒྱས་ཀྱི་ཞིང་གི་རྡུལ་དང་མཉམ་པའི་བསྐལ་པར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་གསོལ་ཞིང་ཕུལ་བ་བས།

[Block 449 [VERSE]]
གང་གིས་བསྔོ་བའི་རྒྱལ་པོ་འདི་ཐོས་ནས། །
ལན་ཅིག་ཙམ་ཡང་དད་པ་བསྐྱེད་པ༌[^312]ནི། །

[Block 450]
ཞེས་བྱ་བ་སྟེ། འདི་ནི་འདི་ཉིད་དོ་ཞེས་ངེས་པ་བསྐྱེད་པར་བྱས་པ་སྟེ། དེ་ཡང་གང་ཞེ་ན། བྱང་ཆུབ་མཆོག་གི་རྗེས་སུ་རབ་མོས་ཤིང་། །ཞེས་བྱ་བ་ཐེག་པ་ཆེན་པོ་ལ་ཞུགས་པ་དེས་སྔ་མའི་སྦྱིན་པའི་བསོད་ནམས་པས་འདིའི་བསོད་ནམས་ཁྱད་པར་ཅན་དུ་འགྱུར་རོ། །

[Block 451]
སྡིག་པའི་གྲོགས་པོ་ཡོངས་སུ་སྤངས་པས་དེ་བཞིན་གཤེགས་པ་མཐོང་བ་སྟེ། དེ་ཡང་གང་ཞེ་ན། དེས་ནི་ངན་སོང་ཐམས་ཅད་སྤང་བར༌[^313]འགྱུར། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 452]
དེས་སྤང་བར་བྱ་བ་ནི་སྡིག་པ་དང་ངན་སོང་གསུམ་མོ། །

[Block 453]
དེས་ནི་གྲོགས་པོ་ངན་པ་སྤང་བར༌[^314]འགྱུར། །ཞེས་བྱ་བ་ནི་ཉན་ཐོས་ལ་སོགས་པ་མི་དགེ་བའི་བཤེས་གཉེན་རྣམས་སོ། །

[Block 454]
འཆི་བའི་ཚེ་བཅོམ་ལྡན་འདས་སྣང་བ༌[^315]མཐའ་ཡས་དེ་བཞིན་གཤེགས་པ་དེ་ཡང་དེས་མྱུར་དུ་གདོན་མི་ཟ་བར་མཐོང་བར་འགྱུར་ཏེ། གང་གིས་མཐོང་ཞེ་ན། གང་གིས་འདི་ལྟར་བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་འདིའི་དོན་དང་ཚིག་བཅས་པར་སེམས་ཀྱིས་ཆུབ་པའོ། །

[Block 455]
ཚེའི་འཚོ་བ་དགེ་བ་ཐོབ་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དང་སྐལ་བ་མཐུན་པ་ཐོབ་པ་སྟེ་དེ་ཡང་གང་ཞེ་ན། དེ་གང་རྙེད་པ་རབ་རྙེད་བདེ་བར་འཚོ། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 456]
བླ་ན་མེད་པའི་སྨོན་ལམ་རིན་པོ་ཆེ༌[^316]ཐོབ་པ་ནི་རབ་ཏུ་རྙེད་པ་སྟེ། བདེ་བར་འཚོ་བ་རྙེད་པ་ཡང་སྨོན་ལམ་རིན་པོ་ཆེ་འདི་ལྟ་བུ་ཐོབ་པས༌[^317]སོ། །

[Block 457]
དེ་ལྟ་བས་ན༌[^318]ཚེའི་མཆོག་ཐོབ་པར་བྱ་བའི་དངོས་པོ་ཐོབ་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 458 [VERSE]]
མི་ཚེ་འདིར་ཡང་དེ་དག་ལེགས་པར་འོངས།[^319] །
ཞེས་བྱ་བ་ནི་དགེ་བར་འོངས་པའོ། །
ཀུན་དུ་བཟང་པོ་དེ་ཡང་ཅི་འདྲ་བར། །

[Block 459]
ཞེས་བྱ་བ་ནི་དེ་ལྟར་རིང་པོར་མི་ཐོགས་པར་འགྱུར་བའོ། །

[Block 460]
ལས་ཀྱི་སྒྲིབ་པ་ཡོངས་སུ་འབྱང་བའི་ཡོན་ཏན་ནི་རྣམ་པ་བཞི་པ་སྟེ། དེ་ཡང་གང་ཞེ་ན། མཚམས་མེད་ལྔ་པོ་དག་གི་སྡིག་པ་རྣམས། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །
--- END BLOCKS ---
