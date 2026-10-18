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
###### སེམས་བསྐྱེད་པའི་ཡོན་ཏན། ^1-1-3-5-1-0

[Block 492]
ཐེག་པ་དེ་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་གོ་སྐབས་འབྱེད་པས་ན་དཔག་ཏུ་མེད་པའོ་ཞེས་བྱ་བས་སེམས་བསྐྱེད་པའི་ཡོན་ཏན་བསྟན་ཏེ། སེམས་ཅན་ཚད་མེད་པ་རྣམས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་གདོན་ཞིང༌[^442]མངོན་པར་འཚང་རྒྱ་བའི་སྐབས་འབྱེད་པས་ན་གོ་སྐབས་འབྱེད་པ་ཞེས་བྱ་སྟེ། ཐེག་པ་དེ་ཡང་དེའི་རྒྱུར་གྱུར་པའི་ཕྱིར།[^443] སེམས་ཅན་དཔག་ཏུ་མེད་པས་དེ་ཡང་དཔག་ཏུ་མེད་པའོ། །

[Block 493]
རྣམ་པ་གཉིས་ཀྱིས༌[^444]དཔག་ཏུ་མེད་པ་སྟེ། རྒྱ་ཆེ་བ་དང་། ཚད་མེད་པའོ། །

[Block 494]
ཅི་ཙམ་དུ་བསྒྲུབ་པར་བྱ་བའི་དགེ་བའི་རྩ་བ་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པ་ཐམས་ཅད་སྒྲུབ་པར་བྱེད་པས་རྒྱ་ཆེ་བས་སོ།[^445] །དགེ་བའི་རྩ་བ་དེ་དག་ཐམས་ཅད་ཀྱང་སེམས་ཅན་གྱི་དོན་དུ་སྒྲུབ་པར་བྱ་བའི༌[^446]ཕྱིར་ཚད་མེད་པའོ། །

[Block 495]
ཡང་ན་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའི་ཚེ་སེམས་ཅན་འགའ་ཡང་མ་བཀོལ་བར༌[^447]སེམས་ཅན་ཚད་མེད་པ་ཐམས་ཅད་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་བསྒྲལ་ལོ་ཞེས་སེམས་བསྐྱེད་པས་ན། སེམས་ཅན་ཐམས་ཅད་ཀྱི་གོ་སྐབས་འབྱེད་པ་ཞེས་བྱ་སྟེ། སེམས་ཅན་དཔག་ཏུ་མེད་པའི་ཕྱིར་ཐེག་པ་དེ་ཡང་དཔག་ཏུ་མེད་པའོ། །

[Block 496 [HEADING]]
###### ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་ཏེ་ཤེས་པ་ཁོང་དུ་ཆུད་པའི་ཡོན་ཏན། ^1-1-3-5-2-0

[Block 497]
ཐེག་པ་དེ་ནི་ཆགས་པ་མེད་པའི་ཡེ་ཤེས་ལ་བཏང་བ་སྟེ། སྒྲིབ་པ་མེད་པའོ་ཞེས་བྱ་བས་ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་ཏེ་ཤེས་པ་ཁོང་དུ་ཆུད་པའི་ཡོན་ཏན་བསྟན་ཏེ། ཤེས་བྱའི་སྒྲིབ་པ་ཐམས་ཅད་སྤངས་ནས་ཤེས་པར་བྱ་བའི་དངོས་པོ་རྣམས་སྐྱུ་རུ་ར་ལག་མཐིལ་དུ་བཞག་པ༌[^448]བཞིན་དུ་གསལ་བར་མཁྱེན་པའི་ཡེ་ཤེས་ནི་ཆགས་པ་མེད་པའི་ཡེ་ཤེས་ཏེ། ཐེག་པ་དེའི་ཡེ་ཤེས་རྒྱུར་གྱུར་པ་འམ།[^449] །ཐེག་པ་དེས་ཡེ་ཤེས་ཐོབ་པར་བྱེད་པས་ན། ཐེག་པ་དེ་ནི་ཆགས་པ་མེད་པའི་ཡེ་ཤེས་ལ་བཏང་བ་ཞེས་བྱའོ། །

[Block 498]
ད་ལྟར་སྒྲིབ་པ་མེད་པའི་ཡེ་ཤེས་ཀྱི་རྒྱུར་གྱུར་པས་ཐེག་པ་དེ་ཡང་སྒྲིབ་པ་མེད་པ་ཞེས་བྱའོ། །

[Block 499 [HEADING]]
###### རྒྱུ་བསྩགས་པའི་ཡོན་ཏན། ^1-1-3-5-3-0

[Block 500]
ཐེག་པ་དེ༌[^450]ནི་སེམས་ཅན་ཐམས་ཅད་ཉེ་བར་འཚོ་བ་སྟེ། བསོད་ནམས་ཀྱི་ཚོགས་དང་དགེ་བའི་རྩ་བ་ཐམས་ཅད་བསགས་པའོ་ཞེས་བྱ་བས་རྒྱུ་བསྩགས་པའི་ཡོན་ཏན་བསྟན་ཏེ། ཚོགས་ཇི་ལྟ་བ་བསྩགས་པས་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་ཀྱི་གསོས་སུ་འགྱུར་བའི་མཐུ་དང་ལྡན་པས་སེམས་ཅན་ཐམས་ཅད་ཉེ་བར་འཚོ་བ་ཞེས་བྱའོ། །

[Block 501]
བསོད་ནམས་ཀྱི་ཚོགས་ནི་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་ལ་སོགས་པའོ། །

[Block 502]
དགེ་བའི་རྩ་བ་ནི་འདོད་མ་ཆགས་པ་དང་། ཞེ་མི་སྡང་བ་ལ་སོགས་པའོ། །

[Block 503 [HEADING]]
###### སྤྱོད་པ་དག་པའི་ཡོན་ཏན། ^1-1-3-5-4-0

[Block 504]
ཐེག་པ་དེ་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་ཀྱི་སྤྱོད་པ་ལས་སུ་རུང་བའི་ཕྱིར༌[^451]ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་ཡོངས་སུ་སྦྱོང་བར༌[^452]བྱས་པའོ་ཞེས་པས༌[^453]སྤྱོད་པ་དག་པའི་ཡོན་ཏན་བསྟན་ཏེ། སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་ཀྱི་རྒྱུད་ལ་གནས་པ༌[^454]སྦྱིན་པ་ལ་སོགས་པའི་མི་མཐུན་པའི་ཕྱོགས་སེར་སྣ་དང་འཆལ་བའི་ཚུལ་ཁྲིམས་ལ་སོགས་པ་ཐེག་པ་དེས་སྤངས་པས་ན་སེམས་ཅན་གྱི་སེམས་ཀྱི༌[^455]སྤྱོད་པ་ལ་ལས་སུ་རུང་བ་ཞེས་བྱའོ། །

[Block 505]
དེ་ལྟར་སེར་སྣ་ལ་སོགས་པ་སྤངས་པ་དང་སྦྱིན་པ་ལ་སོགས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་སྦྱང་བ་བྱས་པར་འགྱུར་རོ།[^456] །ཡོངས་སུ་རྫོགས་པར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 506 [HEADING]]
###### མངོན་པར་བྱང་ཆུབ་པའི་ཡོན་ཏན། ^1-1-3-5-5-0

[Block 507]
ཐེག་པ་དེ་ནི་ཐོགས་པ་མེད་པར་བྱང་ཆུབ་ཀྱི་སྙིང་པོར་འགྲོ་བས་ན་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཀྱི་ཚོགས་ཉམས་སུ་ལོན་པར༌[^457]བྱེད་པའོ་ཞེས་བྱ་བས་མངོན་པར་བྱང་ཆུབ་པའི་ཡོན་ཏན་བསྟན་ཏེ། བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་རྫོགས་ནས་སྒྲིབ་པ་གཉིས་སྤངས་ཏེ། གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ཀྱི༌[^458]འབྲས་བུར་གྱུར་པ་ནི་བྱང་ཆུབ་ཀྱི་སྙིང་པོ་སྟེ། དྲི་མ་མེད་པར་གྲགས་པས་བསྟན་པའི་མདོ་ལས་ཀྱང་བྱང་ཆུབ་ནི་སྦྱིན་པའི་སྙིང་པོ། །བྱང་ཆུབ་ནི་ཚུལ་ཁྲིམས་ཀྱི་སྙིང་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པའི་ཕྱིར་རོ། །

[Block 508]
ཐེག་པ་དེ་ལ་ཞུགས་པས་བདུད་དང་བགེགས་ཀྱི་བར་ཆད་མེད་པར་བྱང་ཆུབ་ཀྱི་སྙིང་པོ་ཐོབ་པར་འགྱུར་བས་ན་ཐེག་པ་དེ་ནི་ཐོགས་པ་མེད་པར་བྱང་ཆུབ་ཀྱི་སྙིང་པོར་འགྲོ་བའོ། །

[Block 509]
དེ་བས་ན་ཐེག་པ་དེས་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པར་འགྱུར་བའི་རྒྱུ་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཡོངས་སུ་རྫོགས་ཤིང་མཐར་འབྱིན་པར་བྱེད་པས་ན་ཚོགས་གཉིས་ཉམས་སུ་ལོན་པར༌[^459]བྱེད་པ་ཞེས་བྱའོ། །

[Block 510 [HEADING]]
###### མཉམ་པར་ཕན་འདོགས་པའི་ཡོན་ཏན། ^1-1-3-5-6-0

[Block 511]
སེམས་ཅན་ཐམས་ཅད་སྦྱིན་པའི་གནས་ཀྱི་ཕྱིར་སེམས་ཅན་ཐམས་ཅད་ལ་ཐོགས་པ་མེད་པའི་འོད་ཟེར་མཉམ་པར་གཏོང་བ་ཞེས་བྱ་བས་མཉམ་པར་ཕན་འདོགས་པའི་ཡོན་ཏན་བསྟན་ཏེ། སེམས་ཅན་ཐམས་ཅད་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་མངོན་པར་སངས་རྒྱས་ནས་བསོད་ནམས་ཀྱི་ཞིང་སྦྱིན་པའི་གནས་སུ་འགྱུར་བར་བྱ་བའི་ཕྱིར་མཐོན་དམན་དང་ཉེ་རིང་མེད་པར༌[^460]བྱམས་པ་དང་ཡེ་ཤེས་ཀྱི་སྣང་བའི་འོད་ཟེར་སྙོམས་པར་གཏོད་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 512 [HEADING]]
###### ཉན་ཐོས་དང་སོ་སོའི་སྐྱེ་བོའི་ལམ་ལས་རྒལ་བའི་ཡོན་ཏན། ^1-1-3-5-7-0

[Block 513]
ཐེག་པ་དེ་ནི་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་མངོན་དུ་གྱུར་པའི་ཕྱིར་ལམ་ངན་པའི་འཇིགས་པ་ཐམས་ཅད་ལས་འདས་པའོ་ཞེས་བྱ་བས་ཉན་ཐོས་དང་སོ་སོའི་སྐྱེ་བོའི་ལམ་ལས་རྒལ་བའི༌[^461]ཡོན་ཏན་བསྟན་ཏེ། སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ནི་སྤང་བར༌[^462]བྱ་བ་དང་། ཤེས་པར་བྱ་བ་དང་། བསྒྲུབ་པར་བྱ་བ་དང་། རྫོགས་པར་བྱ་བ་དང་། ཐོབ་པར་བྱ་བ་རྣམས་ཏེ། དེ་དག་ཐམས་ཅད་ཁོང་དུ་ཆུད་ཅིང་། རྟོགས་པས་ན་མངོན་དུ་གྱུར་པའོ། །

[Block 514]
དེ་ལ་སྤང་བར༌[^463]བྱ་བ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པ་དང་། ཤེས་བྱའི་སྒྲིབ་པའོ། །ཤེས་པར་བྱ་བ་ནི་གང་ཟག་ལ་བདག་མེད་པ་དང་། ཆོས་ལ་བདག་མེད་པའོ། །

[Block 515]
བསྒྲུབ་པར་བྱ་བ་ནི་བདག་དང་གཞན་གྱི་དོན་ཏོ། །

[Block 516]
རྫོགས་པར་བྱ་བ་ནི་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 517]
ཐོབ་པར་བྱ་བ་ནི་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 518]
ཆོས་དེ་དག་མངོན་སུམ་དུ་གྱུར་པས་ཉན་ཐོས་ཀྱི་མྱ་ངན་ལས་འདས་པར་ཡང་མི་ལྟུང་། འཁོར་བར་ཡང་མི་ལྟུང་བས་ན་ལམ་ངན་པའི་འཇིགས་པ་ཐམས་ཅད་ལས་འདས་པ་ཞེས་བྱའོ། །

[Block 519]
ཡང་ན་ཐེག་པ་དེ་ནི༌[^464]གང་ཟག་ལ་བདག་མེད་པར་མངོན་སུམ་དུ་བྱས་བས་ངན་སོང་གསུམ་དུ་སྐྱེ་བའི་འཇིགས་པ་མེད་པས་ན་འཇིགས་པ་ཐམས་ཅད་ལས་འདས་པ་ཞེས་བྱའོ། །

[Block 520 [HEADING]]
###### བགེགས་འཇོམས་པའི་ཡོན་ཏན། ^1-1-3-5-8-0

[Block 521]
ཐེག་པ་དེ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་ཐམས་ཅད་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་བགེགས་འཇོམས་པའི༌[^465]ཡོན་ཏན་བསྟན་ཏེ། བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་ཐམས་ཅད་ནི་དྲན་པ་ཉེ་བར་གཞག་པ༌[^466]བཞི་དང་། ཡང་དག་པར་སྤོང་བ་བཞི་དང་། རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞི་ལ་སོགས་པ་བྱང་ཆུབ་ཀྱི་ཕྱོགས་སུམ་ཅུ་རྩ་བདུན་རྣམས་སོ། །

[Block 522]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ནི་ཆོས་རྣམས་ཀྱི༌[^467]བྱེད་པ་པོས་མ་བྱས་ཤིང་རྟག་པ་དང་ཆད་པ་ལས་འདས་པ་རྒྱུ་དང་རྐྱེན་ལས་སྐྱེས་པས་ན༌[^468]རང་བཞིན་གྱིས༌[^469]མ་སྐྱེས་པ་སྟེ། ནམ་མཁའ་བཞིན་ནོ། །

[Block 523]
ཆོས་དེ་དག་ཉིད་ཐམས་ཅད་ལས་འཕགས་པར་གནས་ཤིང་མུ་སྟེགས༌[^470]དང་བདུད་ལ་སོགས་པ་ལས་རྒྱལ་བར་བྱེད་པས་རྒྱལ་མཚན་དང་བ་དན་ཞེས་བྱའོ། །

[Block 524]
ཆོས་དེ་དག་གི་སྒྲ་གསང་མཐོན་པོར་བསྒྲགས་པ་ནི་རྒྱལ་མཚན་དང་བ་དན་བསྒྲེང་བའོ། །

[Block 525]
དེ་ལྟར་མུ་སྟེགས་ཅན་ཐམས་ཅད་ལས་རྒྱལ་བའི་རྒྱལ་མཚན་དང་བ་དན་བསྒྲེང་བས༌[^471]ཕ་རོལ་རྒོལ་བ་མང་པོ་དང་ལོག་པའི་ཚོགས༌[^472]མང་པོ་ཚར་གཅོད་པར་བྱེད་པས་ན་བདུད་དང་ཕས་ཀྱི་རྒོལ་བ་དང་། ངན་པའི་ཚོགས་ཅན་གྱི་ཚོགས་རབ་ཏུ་འཇོམས་པ་ཞེས་བྱ་སྟེ། བདུད་ནི་བདུད་ཉིད་དོ། །

[Block 526]
ཕས་ཀྱི་རྒོལ་བ་ནི་མུ་སྟེགས་ཅན་རྣམས་སོ། །

[Block 527]
ངན་པའི་ཚོགས་ཅན་གྱི་ཚོགས་ནི་བདུད་ཀྱི་འཁོར་སྟོབས་དང་བཅས་པ་འམ། མུ་སྟེགས་ཅན་འཁོར་དང་བཅས་པ་ལ་བྱའོ། །

[Block 528 [HEADING]]
###### ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་སྤོང་བའི་ཡོན་ཏན། ^1-1-3-5-9-0

[Block 529]
ཐེག་པ་དེ་ནི་སངས་རྒྱས་ཀྱི་ཐེག་པ་སྒྲིབ་པ་མེད་པར་གྱུར་པ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཉོན་མོངས་པ་དང་། ཉེ་བའི་ཉོན་མོངས་པ་སྤོང་བའི་ཡོན་ཏན་བསྟན་ཏེ། སངས་རྒྱས་སུ་འགྲོ་བའི་ཐེག་པ་ནི་སངས་རྒྱས་ཀྱི་ཐེག་པ་སྟེ། སངས་རྒྱས་སུ་འགྲོ་བར་བྱེད་པའི་ཐེག་པ་ཡང་ཡིན་ལ་ཐེག་པ་དེས་ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པའི་སྒྲིབ་པ་ཡང་སེལ་བར་བྱེད་པས་ན། ཐེག་པ་དེ་ནི་སངས་རྒྱས་ཀྱི་ཐེག་པ་སྒྲིབ་པ་མེད་པར་གྱུར་པ་ཞེས་བྱའོ། །

[Block 530]
དེ་ལྟར་སྒྲིབ་པ་མེད་པར་འགྱུར་བས་མཐའ་དང་མཐའ་མེད་པར་ལྟ་བ་ལ་སོགས་པ་ལྟ་བའི་ཉོན་མོངས་པ་རྣམས་སེལ་བར་བྱེད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །
--- END BLOCKS ---
