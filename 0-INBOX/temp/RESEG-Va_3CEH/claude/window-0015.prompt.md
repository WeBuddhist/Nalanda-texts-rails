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

[Block 531]
གང་བདེ་འགྲོ་དང་ངན་འགྲོ་དང་། འཆི་འཕོ་བ་དང་། སྐྱེ་བའི་རྣམ་པར་རིག་པ་སྟེ། འཁོར་བའི་འགྲོ་བ་སྣ་ཚོགས་དེ་ནི་སྲིད་པའི་ཡན་ལག་གི་བག་ཆགས་ཀྱི་ས་བོན་ཉེ་བར་ལེན་པ་ལས་བྱུང་ངོ་། །རྣམ་པར་རིག་པ་འདི་རྣམས་ཀྱིས་ཞེས་བྱ་བ་ནི་བཤད་མ་ཐག་པའི་རྣམ་པར་རིག་པ་དག་གོ། །

[Block 532]
ཁམས་དང་། འགྲོ་བ་དང་། སྐྱེ་གནས་ཐམས་ཅད་བསྡུས་པ་ཞེས་བྱ་བ་ནི་ཁམས་གསུམ་དང་དེའི་ཁོངས་སུ་གཏོགས་པ་འགྲོ་བ་རྣམ་པ་ལྔ་དང་། སྐྱེ་གནས་རྣམ་པ་བཞི་དང་། ཀུན་ནས་ཉོན་མོངས་པའོ། །

[Block 533]
བསྡུས་པ་ཞེས་བྱ་བ་ནི་དེའི་ངོ་བོ་ཉིད་དོ། །

[Block 534]
གཞན་གྱི་དབང་གི་མཚན་ཉིད་ཅེས་བྱ་བ་ནི་གཞན་གྱི་དབང་གི་བདག་ཉིད་དེ། ཡང་དག་པ་མ་ཡིན་པའི་ཀུན་ཏུ་རྟོག་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 535]
རྣམ་པར་རིག་པ་འདི་རྣམས་ཀྱི་རྣམ་པར་རིག་པ་ཙམ་ཉིད་ཡང་དག་པ་མ་ཡིན་པའི་ཀུན་ཏུ་རྟོག་པས་བསྡུས་པ་ཞེས་བྱ་བ་དེ་ལ་ཡང་དག་པ་མ་ཡིན་པའི་ཀུན་ཏུ་རྟོག་པས་བསྡུས་པ་ཞེས་བྱ་བ་ནི༌[^396]དེའི་ངོ་བོ་ཉིད་དོ། །

[Block 536]
ཡོད་པ་མ་ཡིན་པ་དང་། ནོར་བའི་དོན་སྣང་བའི་གནས་གང་ཡིན་པ་འདི་ནི་ཞེས་བྱ་བ་ནི་ཡོད་པ་མ་ཡིན་པ་དང་། ནོར་བའི་དོན་སྣང་བའི་རྒྱུ་སྟེ། དེ་ལ་ཡོད་པ་མ་ཡིན་པ་ནི་མེད་པ་སྟེ། འདི་ལྟར་བདག་གི་ངོ་བོ་དོན་དེ་བཞིན་དུ་ཡོད་པར་བཟུང་ནས་དེ་ཉིད་ལ་བདག་མེད་པར་བདག་ཅེས་སྣང་བ་སྟེ། དེའི་གནས་ནི་སྣང་བའི་གནས་ཏེ་རྒྱུ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 537]
དེ་ལྟ་བུ་ནི་གཞན་གྱི་དབང་གི་མཚན་ཉིད་དོ། །

[Block 538 [HEADING]]
### ཀུན་ཏུ་བརྟགས་པའི་མཚན་ཉིད། ^2-2-0

[Block 539]
ཀུན་ཏུ་རྟོག་པའི༌[^397]མཚན་ཉིད་གང་ཞེ་ན། གང་དོན་མེད་ཀྱང་འདི་ལྟར་བདེན་པ་ཉིད་དུ་སྣང་བའོ། །

[Block 540]
རྣམ་པར་རིག་པ་ཙམ་སྟེ༌[^398]དོན་ཉིད་དུ་ཞེས་བྱ་བ་ནི་ཡང་དག་པ་མ་ཡིན་པའི་དོན་གྱི་སྣང་བ་སྟེ། འདི་ལྟར་བདག་ཉིད་ཀྱི་དོན་སྣང་བ་ཙམ་དེའི་སྣང་བའོ། །

[Block 541]
དོན་ཉིད་དུ་སྣང་བ་ཞེས་བྱ་བ་ནི་གཟུང་བ༌[^399]ཉིད་དུ་སྣང་བ་སྟེ། འདི་ལྟར་བདག་མེད་པ་དེ་བདག་ཏུ་སྣང་བའོ། །

[Block 542 [HEADING]]
### ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད། ^2-3-0

[Block 543]
ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་ནི་གང་ཡོད་པ་མ་ཡིན་པ་མི་བདེན་པ་སྣང་བའི་རྒྱུ་དོན་དེའི་བདག་ཉིད་དུ་སྣང་བ་གཏན་མེད་པར་གྱུར་པ་སྟེ། འདི་ལྟར་བདག་ཏུ་སྣང་བ་གཏན་མེད་པར་གྱུར་པ་ཉིད་ནི་བདག་མེད་པ་ཙམ་ཡོད་པར་གྱུར་པ་ཉིད་ཡིན་ཏེ། འདི་དག་ནི་རྣམ་པར་ཤེས་པ་ཙམ་མོ་ཞེས་བྱ་བ་ས་བཅུ་པ་ལས་གསུངས་པ་དང་། དགོངས་པ་ངེས་པར་འགྲེལ་པའི་མདོ་ལས་ཀྱང་། རྣམ་པར་ཤེས་པ་ནི་དམིགས་པ་རྣམ་པར་རིག་པ་ཙམ་གྱིས་རབ་ཏུ་ཕྱེ་བ་ཅན་ནོ་ཞེས་ངས་བཤད་དོ་ཞེས་གསུངས་པ་དེས་ན་དམིགས་པ་རྣམ་པར་རིག༌[^400]པ་ཙམ་གྱིས་རབ་ཏུ་ཕྱེ་བ་ཅན་དེ་ནི་རྣམ་པར་རིག་པ་ཙམ་ཉིད་དེ། དོན་གྱིས་སྟོང་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 544 [HEADING]]
### རྣམ་པར་རིག་པ་ཙམ་ཉིད། ^2-4-0

[Block 545]
རྣམ་པར་ཤེས་པ་ཞེས་ངས་བཤད་དོ་ཞེས་བྱ་བའི་རྣམ་པར་ཤེས་པ་སྨོས་པ་དེས་ནི་ཏིང་ངེ་འཛིན་གྱི་སྤྱོད་ཡུལ་གྱི་རྣམ་པར་ཤེས་པ་བསྟན་ཏོ། །

[Block 546]
འོན་ཀྱང་དེ་ལྟར་སྐྱེས་པའི་ཞེས་བྱ་བ་ནི་རྣམ་པ་དེ་ལྟ་བུར་སྐྱེས་པའོ། །

[Block 547]
དེས་ན༌[^401]དོན་ཐ་དད་པར་སྣང་བ༌[^402]ཞེས་བྱ་བ་ལ། དེ་ལས་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་གྱི་སྤྱོད་ཡུལ་ལས་སོ། །

[Block 548]
དོན་ཐ་དད་པར་ཞེས་བྱ་བ་ནི་གཟུང་བའི་ངོ་བོ་ཉིད་དུ་རྣམ་པར་ཆད་པ་ལྟ་བུར༌[^403]རྣམ་པར་ཤེས་པ་སྣང་བ་ཉིད་དོ། །

[Block 549]
རྣམ་པར་བསྔོས་པ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་གྱི་སྤྱོད་ཡུལ་གྱི་གཟུགས་བརྙན་ནི་རྣམ་པར་ཤེས་པས་དྲན་པ་ནི་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་ཇི་ལྟ་བ་བཞིན་དུ་ཡུལ་ན་གནས་པའི་ཕྱིར་རོ། །

[Block 550]
དེ་བཞིན་དུ་ཉམས་སུ་མྱོང་བ་ནི་དྲན་པ་མ་ཡིན་ཏེ། མདུན་དུ་བྱས་པ་མཐོང་བའི་ཕྱིར་དང་། རྣམ་པར་ཤེས་པས་དྲན་པའི་དོན་ནི་མི་གསལ་བ་ཡིན་པའི་ཕྱིར་ལ། མདུན་ན་གནས་པ་འདི་ནི་གསལ་བར་མཐོང་བའི་ཕྱིར་རོ། །

[Block 551]
གཞན་ཡང་གལ་ཏེ་ཇི་ལྟར་ཐོས་པ་དང་། བསམས་པ་དང་། གོམས་པར་བྱས་པ་དེ་ནི་རིང་དུ་འདས་པར་གྱུར་ན་ཡང་། ཇི་ལྟར་ད་ལྟར་བྱུང་བ་བཞིན་དུ་དེ་ཡང་དེ་བཞིན་ནོ་ཞེ་ན། དེ་ལ་ཐོས་པ་དང་བསམས་པ༌[^404]ནི་འདས་ནས་རིང་དུ་ལོན་པ་ཉིད་ཀྱིས་མེད་པ་ཡིན་ལ། ཐོས་པ་དང་བསམས་པའི༌[^405]རང་བཞིན་ནི་འདས་ནས་རིང་དུ་ལོན་པས་མེད་པའི་ཕྱིར་ཏེ༌[^406]མེད་པ་ཉིད་ཡིན་ཏེ་དེས་ན་གང་བྱུང་བ་དེ་ནི་རྣམ་པར་ཤེས་པ་ཉིད་དེ། དེ་ལྟ་བུར་སྣང་བར་གྱུར་པ་ཡིན་པས་དེས་ན་འདི་དག་ནི་རྣམ་པར་རིག་པ་ཙམ་ཉིད་དུ་འཐད་དེ། དེའི་ཕྱིར་དོན་མེད་པ་ཉིད་དུ་གྲུབ་བོ། །

[Block 552]
མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པའི་རྣམ་པར་རིག་པ་རྣམས་ནི་གཟུགས་ཅན་མ་ཡིན་པས་རྣམ་པར་རིག་པ་ཙམ་ཉིད་དུ་རིགས་ན། མིག་ལ་སོགས་པའི་རྣམ་པར་རིག་པ་གཟུགས་ཅན་རྣམས་ཇི་ལྟར་ཞེས་བྱ་བ་དེ་ལ། དེ་དག་ཀྱང་ལུང་དང་རིགས་པས་བལྟ་བར་བྱ་སྟེ། སྔ་མ་བཞིན་ནོ་ཞེས་བྱ་བར་བསྟན་ཏོ། །

[Block 553]
མཚུངས་ལ་བརྟན་པར༌[^407]རྒྱུན་གྱིས་འཇུག །ཅེས་བྱ་བ་དེ་ལ་མཚུངས་པ་ནི་འདྲ་བའོ། །

[Block 554]
བརྟན་པ་ནི་དུས་གཞན་དུ་གནས་པའོ། །

[Block 555]
ཕྱིན་ཅི་ལོག་ལ་སོགས་པའི་ཀུན་ནས་ཉོན་མོངས་པ༌[^408]སྟེ། ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་ཞེས་བྱ་བ་རྒྱུར་གྱུར་པ་དག་གོ། །

[Block 556]
གཞིའི་གནས་ཞེས་བྱ་བ་ནི་རྒྱུའི་ངོ་བོའི་འདི་དག་ཉིད་གཞན་དུ་འཇུག་པར་འགྱུར་ན་དོན་མ་ཡིན་པ་ལ་དོན་ཡིན་ནོ་ཞེས་སེམས་ཕྱིན་ཅི་ལོག་ཏུ་འབྱུང་བར་མི་འགྱུར་ལ། དེ་མེད་པས་ཀྱང་ཉོན་མོངས་པའི་སྒྲིབ་པའི་ཀུན་ནས་ཉོན་མོངས་པ་དང་། ཤེས་བྱའི་སྒྲིབ་པའི་ཀུན་ནས་ཉོན་མོངས་པ་དེ་མི་འབྱུང་ངོ་། །དོན་འདི་དག་ཉིད་ཚིགས་སུ་བཅད་པས་བསྟན་པ་ནི། འཁྲུལ་པའི་རྒྱུ་དང་འཁྲུལ་པ་ནི་རིམ་པ་བཞིན་དུ་གཟུགས་ཀྱི་རྣམ་པར་རིག་པ་དང་། རྣམ་རིག་གཟུགས་ཅན་མིན་པར་འདོད། །ཅེས་བྱ་བའོ། །

[Block 557]
དེ་ལ་གཟུགས་ཅན་གྱི་རྣམ་པར་རིག་པ་ནི་འཁྲུལ་པའི་རྒྱུ་སྟེ། རྒྱུར་གྱུར་པའི་གཟུགས་ཅན་གྱི་རྣམ་པར་རིག་པ་མེད་ན་འབྲས་བུར་གྱུར་པའི་རྣམ་པར་རིག་པ་གཟུགས་ཅན་མ་ཡིན་པ་གང་ཡིན་པ་ཡང་མི་འབྱུང་བས་ཇི་ལྟར་ན་ལུས་དང་ལོངས་སྤྱོད་ཐམས་ཅད་ཡོད་པར་འགྱུར་ཞེས་བྱ་བའོ། །

[Block 558]
ལུས་དང་ལུས་ཅན་དང་ཟ་བ་པོར་རྣམ་པར་རིག་པ་གསུམ་རྣམ་པར་རིག་པ་ལུས་ཐམས་ཅད་ལ་ལྷན་ཅིག་འབྱུང་ཞིང་ཞེས་བྱ་བ་ནི་དུས་གཅིག་ཏུ་འབྱུང་བའོ།[^409] །

[Block 559]
ཉེ་བར་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་རྒྱུའི་ངོ་བོ་སྟེ། རྣམ་པ་གསུམ་ཆར༌[^410]རྣམ་པར་རིག་པ་ཙམ་དུ་ཚིགས་སུ་བཅད་པ་དང་། རྐྱང་པས་རྣམ་པར་འཇོག་པར་བྱེད་དོ། །

[Block 560]
དེ་རྐྱང་པ་ནི་དེ་ཙམ་དུ་ཟད་པས་ཞེས་བྱ་བ་སྟེ། ཐམས་ཅད་རྣམ་པར་རིག་པ་ཙམ་ནི་རྣམ་པར་རིག་པ་ཙམ་ཉིད་ཡིན་པའི་ཕྱིར་དེ་རྙེད༌[^411]ནི་རྣམ་པར་རིག་པ་ཙམ་མོ། །

[Block 561]
དེའི་ཕྱིར་རྣམ་པར་རིག་པ་ཙམ་ཡིན་གྱི་དོན་ནི་མེད་དོ།[^412] །ཡང་རྣམ་པ་གཉིས་ཉིད་ནི་རྒྱུ་མཚན་དང་བཅས་པ་དང་། ལྟ་བ་ཅན་གྱི༌[^413]རྣམ་པར་ཤེས་པས་རྣམ་པར་གཞག་པར་འགྱུར་རོ། །

[Block 562]
གལ་ཏེ་རྣམ་པར༌[^414]རིག་པ་ཙམ་གཅིག་པོ་དེའི་ཆ་གཅིག་ནི་རྒྱུ་མཚན་ཡིན་ལ།

[Block 563]
གཉིས་པ་ནི་ལྟ་བར་འགྱུར་ན། དེས་ན་ཡང་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་རྣམས་གཉིས་ཉིད་དེ། སྣ་ཚོགས་ཀྱི་ངོ་བོ་ཉིད་དུ་རྣམ་པར་བཞག་པས་ཡང་རྣམ་པར་རིག་པ་ཙམ་གཅིག་པོ་དེ་ཉིད་ལ་ཇི་ལྟར་རིགས་པ་ཆ་གཅིག་ནི་སྣ་ཚོགས་སུ་འབྱུང་བར་འགྱུར་ལ། གཉིས་པས་ནི་འདི་ལྟར་འཛིན་པར་བྱེད་དོ། །

[Block 564]
ཡང་གང་གི་ཕྱིར་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་འཛིན་པར་བྱེད་པ་དེས་ན་མིག་ལ་སོགས་པའི་རྣམ་པར་རིག་པ་ཆོས་ཀྱི་མཐར་ཐུག་པ་ཐམས་ཅད་ནི༌[^415]རྒྱུ་མཚན་ཡིན་པས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ནི་འདི་ལྟར༌[^416]ལྟ་བ་ཞེས་བྱའོ། །

[Block 565]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དེ་དག༌[^417]ཉིད་ནི་རྒྱུ་ཞེས་བྱ་བར་ཡང་བསྟན་ཏེ་སོ་སོར་ངེས་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
