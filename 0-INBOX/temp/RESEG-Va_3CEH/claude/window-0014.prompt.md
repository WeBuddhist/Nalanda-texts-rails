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
[Block 491 [HEADING]]
#### མཚན་ཉིད་ཀྱིས་རབ་ཏུ་དབྱེ་བ། ^1-6-5-0

[Block 492]
དེ་ལ་མཚན་ཉིད་ཀྱིས་རབ་ཏུ་དབྱེ་བ་ཞེས་བྱ་བ་ལ། དེ་ནི་རྣམ་པ་མང་དུ་འབྱུང་ངོ་། །དེ་ཡང་ཐུན་མོང་གི་མཚན་ཉིད་དང་། ཐུན་མོང་མ་ཡིན་པའི་མཚན་ཉིད་དང་། ཚོར་བ་མེད་པ་འབྱུང་བའི་ས་བོན་གྱི་མཚན་ཉིད་དང་། ཚོར་བ་དང་བཅས་པ་འབྱུང་བའི་ས་བོན་གྱི་མཚན་ཉིད་དེ་ཞེས་བྱ་བ་ནི་མདོར་བསྟན་པའོ། །

[Block 493 [HEADING]]
##### ཐུན་མོང་གི་མཚན་ཉིད། ^1-6-5-1-0

[Block 494]
དེ་ལ་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཐུན་མོང་གི་སྣོད་ཀྱི་འཇིག་རྟེན་རྒྱུར་གྱུར་པས་ན། ཚོར་བ་མེད་པ་འབྱུང་བའི་ས་བོན་ནོ། །

[Block 495 [HEADING]]
##### ཐུན་མོང་མ་ཡིན་པའི་མཚན་ཉིད། ^1-6-5-2-0

[Block 496]
གང་ཐུན་མོང་མ་ཡིན་པ་ཞེས་བྱ་བ་དེ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་སོ་སོ༌[^381]རང་གི་གཟུགས་ལ་སོགས་པ་དང་། སྐྱེ་མཆེད་རྣམས་ཀྱི༌[^382]རྒྱུར་གྱུར་པ་སྟེ། དེ་ནི་ཚོར་བ་དང་བཅས་པ་འབྱུང་བའི་ས་བོན་ནོ། །

[Block 497]
དེ་ལྟ་བུའི་རྣམ་པ་ཅན་གྱི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་མེད་ན་གང་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཐུན་མོང་གི་ལོངས་སྤྱོད་ཀྱི་རྒྱུར་གྱུར་པ་སྣོད་ཀྱི་འཇིག་རྟེན་ཡོད་པར་མི་འགྱུར་རོ། །

[Block 498]
དེ་བཞིན་དུ་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་གཉིས་པ་མེད་ན་ཡང་སེམས་ཅན་གྱི་འཇིག་རྟེན་ཡོད་པར་ཡང་མི་འགྱུར་ཏེ། དེས་ན་ཤིང་བཞིན་དུ་ཚོར་བ་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 499 [HEADING]]
##### གནས་ངན་ལེན་གྱི་མཚན་ཉིད། ^1-6-5-3-0

[Block 500]
ཡང་གནས་ངན་ལེན་གྱི་མཚན་ཉིད་ཅེས་བྱ་བ་ནི་གང་རྟེན་ལས་སུ་མི་རུང་བ་ཉིད་དོ། །

[Block 501 [HEADING]]
##### ཤིན་ཏུ་སྦྱངས་པའི་མཚན་ཉིད། ^1-6-5-4-0

[Block 502]
ཤིན་ཏུ་སྦྱངས་པའི་མཚན་ཉིད་ནི་གང་ལས་སུ་རུང་བ་ཉིད་དོ། །

[Block 503 [HEADING]]
##### སྤྱད་ཟིན་པའི་མཚན་ཉིད། ^1-6-5-5-0

[Block 504]
སྤྱད༌[^383]ཟིན་པའི་མཚན་ཉིད་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་མེད་ན་ཡང་དང་ཡང་དུ་བྱས་པའི་དགེ་བ་དང་མི་དགེ་བའི་ལས་གང་གིས༌[^384]འབྲས་བུ་འབྱུང་བ༌[^385]ཟད་པར་འགྱུར་བ་དེ་ཡོད་པར་མི་རུང་ངོ་། །

[Block 505 [HEADING]]
##### མ་སྤྱད་པའི་མཚན་ཉིད། ^1-6-5-6-0

[Block 506]
མ་སྤྱད་པའི་མཚན་ཉིད་ནི་གང་མངོན་པར་བརྗོད་པའི་བག་ཆགས་ཀྱི་ས་བོན་ཏེ་ཞེས་བྱ་བ་ནི་མངོན་པར་བརྗོད་པའི་བག་ཆགས་ཀྱི་བྱེ་བྲག་ཇི་ལྟ་བ་བཞིན་དུ་བསྟན་པའོ། །

[Block 507]
ཐོག་མ་མེད་པའི་དུས་ནས་སྤྲོས་པ་འབྱུང་བས་ས་བོན་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ། ཐོག་མ་མེད་པའི་དུས་ནས་ཡང་དག་པའི་ཐ་སྙད་ཀྱི་རྒྱུར་གྱུར་པ་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཞེས་བརྗོད་པ༌[^386]དེ་མེད་ན་མངོན་པར་བརྗོད་པའི་བག་ཆགས་གསར་དུ་འབྱུང་བ་ཡང་མི་འཐད་དོ། །

[Block 508]
རྙིང་རྣམས་མེད་པས་དེའི་ཕྱིར་ད་ལྟར་གྱི་མངོན་པར་བརྗོད་པ༌[^387]ཡང་མ་ཡིན་ནོ། །

[Block 509]
སྔ་ན་མེད་པར་ཡང་འགྱུར་ཏེ། གང་འཇིག་རྟེན་ན༌[^388]ཐོག་མ་མེད་པ་ནས་མ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 510 [HEADING]]
##### དཔེའི་མཚན་ཉིད། ^1-6-5-7-0

[Block 511]
དཔེའི༌[^389]མཚན་ཉིད་ནི་ཅི་སྒྱུ་མ་སྒྱུ་མ་བྱས་པའི་རྒྱུ་ཉིད་ཡིན་པས་འཁྲུལ་པའི་གླང་པོ་ལ་སོགས་པའི་རྒྱུར་འགྱུར་བ་དེ་བཞིན་དུ་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་དཔེའི་མཚན་ཉིད་དུ་བསྟན་པ་ཡང་ཡང་དག་པ་མ་ཡིན་པའི་ཀུན་ཏུ་རྟོག་པའི་ས་བོན་ཡིན་པས་ཕྱིན་ཅི་ལོག་གི་རྒྱུ་མཚན་ཡིན་ཏེ། དེ་མེད་ན་རྒྱུ་མཚན་ཉིད་དུ་མི༌[^390]རུང་ངོ་། །

[Block 512 [HEADING]]
### མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ། ^1-7-0

[Block 513]
མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཞེས་བྱ་བ་ལ། མ་བསྒྲིབས་པ་ནི༌[^391]ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་སྟེ། ཉོན་མོངས་པ་ཅན་གང༌[^392]ཡིན་པ་དང་ལུང་དུ་མ་བསྟན་པ་ནི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཡིན་གྱི། ཇི་ལྟར་གཟུགས་ཀྱི་ཁམས་སུ་སྐྱེ་བས༌[^393]ཉོན་མོངས་པ་དང་། དགེ་བ་མ་ཡིན་པ་དང་། ལུང་དུ་མ་བསྟན་པ་ནི་མ་ཡིན་ནོ། །

[Block 514]
དགེ་བ་དང་མི་དགེ་བའི་རྣམ་པར་སྨིན་པ་ཉིད་ཡོད་ན་ཀུན་ནས་ཉོན་མོངས་པར༌[^394]ལྡོག་པར་མི་འགྱུར་རོ། །

[Block 515]
དེའི་ཕྱིར་ན་དགེ་བ༌[^395]ལས་དགེ་བ་དང་། མི་དགེ་བ་ལས་མི་དགེ་བར་འབྱུང་བས་འདུས་བྱས་ལ་མཐར་ཐུག་པ་མེད་དེ། དེས་ན་ཀུན་ནས་ཉོན་མོངས་པ་དང་། དགེ་བ་ཟག་པ་དང་བཅས་པས་འཁོར་བར་འགྱུར་རོ། །

[Block 516 [HEADING]]
## ཤེས་བྱའི་མཚན་ཉིད། ^2-0

[Block 517 [HEADING]]
### གཞན་གྱི་དབང་གི་མཚན་ཉིད། ^2-1-0

[Block 518]
ཤེས་བྱའི་མཚན་ཉིད་ཀྱི་དབང་དུ་བྱས་ནས་བསྟན་པ་ལ་དེ་ལ་གཞན་གྱི་དབང་གི་མཚན་ཉིད་གང་ཞེ་ན། དེ་ནི་མདོར་བསྡུ་ན་ཞེས་བྱ་བ་ནི་ཡང་དག་པར་བསྡུས་པའོ། །

[Block 519]
ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པས་བསྡུས་པ་ཞེས་བྱ་བ་ནི་ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་རྟོག་པའོ། །

[Block 520]
ལུས་དང་། ལུས་ཅན་དང་། ཟ་བ་པོའི་རྣམ་པར་རིག་པ་ཞེས་བྱ་བ་དེ་ལ། ལུས་ནི་མིག་ལ་སོགས་པའི་ཁམས་ལྔའོ། །

[Block 521]
ལུས་ཅན་ནི་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་དོ། །

[Block 522]
ཟ་བ་པོ་ནི་ཡིད་ཀྱི་ཁམས་སོ། །

[Block 523]
དེས་ཉེ་བར་སྤྱད་པར་བྱ་བའི་རྣམ་པར་རིག་པ་ནི་ཕྱི་རོལ་གྱི་གཟུགས་ལ་སོགས་པའི་ཁམས་དྲུག་གོ། །

[Block 524]
དེ་ལ་ཉེ་བར་སྤྱོད་པའི་རྣམ་པར་རིག་པ་ནི་རྣམ་པར་ཤེས་པ་དྲུག་གི་ཁམས་སོ། །

[Block 525]
དུས་ཀྱི་རྣམ་པར་རིག་པ་ནི་འཁོར་བའི་རྒྱུན་འཇུག་པ་རྣམ་པར་ཆད་པ་མེད་པ་ཉིད་དོ། །

[Block 526]
གྲངས་ཀྱི་རྣམ་པར་རིག་པ་ནི་བགྲང་བའོ། །

[Block 527]
ཡུལ་གྱི་རྣམ་པར་རིག་པ་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་ནོ། །

[Block 528]
ཐ་སྙད་ཀྱི་རྣམ་པར་རིག་པ་ནི་མཐོང་བ་དང་། ཐོས་པ་དང་། ཤེས་པ་དང་། རྣམ་པར་ཤེས་པ་སྟེ། ཐ་སྙད་རྣམ་པ་བཞིའོ། །

[Block 529]
རེ་ཞིག་དེ་ལྟ་བུའི་རྣམ་པར་རིག་པ་དག་ནི་ཤེས་བྱའི་གནས་སུ་བསྟན་པ་ནི་མངོན་པར་བརྗོད་པའི་བག་ཆགས་ཀྱི་རྒྱུ་ཅན་ཡིན་ནོ། །

[Block 530]
བདག་དང་གཞན་གྱི་བྱེ་བྲག་གི་རྣམ་པར་རིག་པ་གང་ཡིན་པའི་བྱེ་བྲག་གི་རྟེན་ནི་བདག་ཏུ་ལྟ་བའི་བག་ཆགས་ཀྱི་རྒྱུ་ཅན་ནོ། །
--- END BLOCKS ---
