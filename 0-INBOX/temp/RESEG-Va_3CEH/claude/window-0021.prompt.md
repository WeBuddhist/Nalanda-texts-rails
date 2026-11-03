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
[Block 736]
དེ་འཐོབ་པའི་ལམ་རྣམ་པར་བྱང་བ་ཞེས་བྱ་བ་ནི་དེ་འཐོབ་པའི་ལམ་གང་ཡིན་པ་དེ་ཡང་རྣམ་པར་བྱང་བ་སྟེ། དེ་ཡང་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་སོགས་པའོ། །

[Block 737 [HEADING]]
#### དེ་སྐྱེད་པ་ཉིད་ཀྱི་དམིགས་པ་རྣམ་པར་བྱང་བ། ^2-14-4-0

[Block 738]
དེ་སྐྱེད་པ་ཉིད་ཀྱི་དམིགས་པ་རྣམ་པར་བྱང་བ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་དེ་རྣམས་མངོན་པར་རྟོགས་པ་སྐྱེད་པ་ཡང་ཡིན་ལ་དམིགས་པ་ཡང་ཡིན་པས་སྐྱེད་པ་ཉིད་ཀྱི་དམིགས་པའོ། །

[Block 739]
དེ་རྣམ་པར་བྱང་བ་ཡང་ཡིན་པས་དེ་སྐྱེད་པ་ཉིད་ཀྱི་དམིགས་པ་རྣམ་པར་བྱང་བ་ཞེས་བྱའོ། །

[Block 740]
དེ་ཡང་མདོའི་སྡེ་ལ་སོགས་པ་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་སུ་གཏོགས་པའི་བསྟན་པ་སྟེ། གང་གི་ཕྱིར་བསྟན་པ་གང་ཡིན་པ་དེ་ཀུན་ཏུ་བརྟགས་པ་ཡིན་ན་ནི་ཀུན་ནས་ཉོན་མོངས་པའི་རྒྱུ་ལས་བྱུང་བར་འགྱུར་རོ། །

[Block 741]
འོན་ཏེ་གཞན་གྱི་དབང་ཡིན་ན་ནི་བདེན་པ་མ་ཡིན་པའི་དོན་དུ་འགྱུར་རོ། །

[Block 742]
ཆོས་ཀྱི་དབྱིངས་རྣམ་པར་དག་པའི་རྒྱུ་མཐུན་པ་ཅན་ཡིན་པས་དེ་དག་གཉི་ག་ལས་རྣམ་པར་གྲོལ་བའི་ཕྱིར་མི༌[^508]བདེན་པ་མ་ཡིན་ཏེ། ཡོངས་སུ་གྲུབ་པ་ཉིད་ལས་འབྱུང་བར༌[^509]འགྱུར་བ་ཡིན་ནོ། །

[Block 743]
ཡང་གང་དུ་རྣམ་པ་བཞི་པོ་དེ་དག་ལས་གང་ཡང་རུང་བ་ཞིག་བསྟན་པ་ནི་ཐེག་པ་ཆེན་པོ་སྟེ། ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་སྟོན་པ་ཡིན་ནོ་ཞེས་འདི་ལྟར་རིག་པར་བྱའོ། །

[Block 744]
དེ་ལ་དང་པོ་གཉིས་ནི་མི་འགྱུར་བར་ཡོངས་སུ་གྲུབ་པ་ཉིད་ཀྱི་ཡོངས་སུ་གྲུབ་པའོ། །

[Block 745]
ཕྱི་མ་ནི་ཕྱིན་ཅི་མ་ལོག་པར་ཡོངས་སུ་གྲུབ་པ་ཡིན་ནོ། །

[Block 746]
དོན་འདི་དག་ཉིད་ཚིགས་སུ་བཅད་པ་ཕྱི་མས་བསྟན་ཏོ། །

[Block 747]
བྱུང་རྟེན་སྒྱུ་མ་ལ་སོགས་བསྟན།[^510] །ཞེས་བྱ་བ་ནི་གཞན་གྱི་དབང་དུ་འབྱུང་བར༌[^511]བསམ༌[^512]པའོ། །

[Block 748]
དེ་ཡང་གང་དུ་ཆོས་ཐམས་ཅད་སྒྱུ་མ་ལྟ་བུའོ་ཞེས་བྱ་བ་ནས་སྤྲུལ་པ་ལྟ་བུའོ་ཞེས་བྱ་བའི་བར་གྱིས་བསྟན་པ་སྟེ། དེ་ནི་གཞན་གྱི་དབང་གི་ངོ་བོ་བསྟན་པ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 749]
བརྟགས་ལ་བརྟེན་ནས་མེད་པ་བསྟན། །ཞེས་བྱ་བ་ནི་གང་དུ་གཟུགས་མེད་ཅེས་བྱ་བ་ནས། ཆོས་ཐམས་ཅད་མེད་དོ་ཞེས་བྱ་བའི་བར་དུ་བསྟན་པ་དེར་ནི་ཀུན་ཏུ་བརྟགས་པ་བསྟན་པ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 750 [HEADING]]
### གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་སྒྱུ་མ་ལ་སོགས་པའི་དཔེས་བསྟན་པ། ^2-15-0

[Block 751 [HEADING]]
#### སྒྱུ་མ། ^2-15-1-0

[Block 752]
གང་གི་ཕྱིར་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་སྒྱུ་མ་ལ་སོགས་པའི་དཔེ་ཉིད་ཀྱིས་བསྟན་པས་དེ་སྟོན་པར་མཛད་པ་ནི་དེ་ལ་ནོར་པ་ཉིད་དུ་སོམ་ཉི་ཟ་བ་ཡིན་ཏེ། ནོར་པ་ཉིད་ལ་སོམ་ཉི་ཟ་བ་ལ་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་དེ༌[^513]སྒྱུ་མའི་དཔེས་སྟོན་པར་མཛད་དེ། ཇི་ལྟར་སྒྱུ་མའི་གླང་པོ་དང་། རྟ་དོན་དུ་མེད་ན་ཡང་ཡུལ་དུ་འགྱུར་བ་དེ་བཞིན་དུ་དོན་ཡང་བལྟ་བར་བྱའོ་ཞེས་དེའི་སོམ་ཉི་བཟློག་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 753 [HEADING]]
#### སྨིག་རྒྱུ། ^2-15-2-0

[Block 754]
གཞན་ཡང་སེམས་དང་སེམས་ལས་བྱུང་བ་དོན་མེད་པ་རྣམས་དམིགས་པ་མེད་པར་ཇི་ལྟར་འབྱུང་བར་འགྱུར་སྙམ་དུ་སོམ་ཉི་ཟ་བར་འགྱུར་བས་དེའི་གཉེན་པོར་སྨིག་རྒྱུ་སྟེ། དེ་ལ་སྨིག་རྒྱུའི་གནས་ལྟ་བུ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བའོ། །

[Block 755]
ཆུའི་གནས་ལྟ་བུ་ནི་དོན་ཏོ། །

[Block 756]
དེས་ན་ཇི་ལྟར་སྨིག་རྒྱུ་རྒྱུ་བར་གྱུར་པ་ན་ཆུའི་དོན་མེད་བཞིན་དུ་ཡང་ཆུའི་དོན་གྱི་བློ་སྐྱེད་པར་བྱེད་པའོ། །

[Block 757]
དེ་བཞིན་དུ་སེམས་དང་སེམས་ལས་བྱུང་བའི་རྒྱུ་བར་གྱུར་པ་ན་ཡང་ཡོད་པ་མ་ཡིན་པའི་དོན་གྱི་བློ་འབྱུང་བར་འགྱུར་རོ། །

[Block 758 [HEADING]]
#### རྨི་ལམ། ^2-15-3-0

[Block 759]
ཡང་བྱིས་པ་རྣམས་ཇི་ལྟར་དོན་མེད་ན་འདོད་པ་དང་མི་འདོད་པའི་ཉེ་བར་སྤྱོད་པ་ཇི་ལྟར་ཐོབ་པར་འགྱུར་ཞེས་སོམ་ཉི་ཟ་བ་དེ་བཟློག་པར་བྱ་བའི་ཕྱིར་གཞན་གྱི་དབང་ནི་རྨི་ལམ་ལྟ་བུ་ཉིད་དེ། རྨི་ལམ་ན་དོན་ཇི་ལྟ་བ་བཞིན་དུ་མེད་ན་ཡང་འདོད་པ་དང་མི་འདོད་པའི་ཉེ་བར་སྤྱད་པ་ཐོབ་པ་མཐོང་བ་བཞིན་དུ་འདིར་ཡང་དེ་བཞིན་དུ་འགྱུར་རོ༌[^514]ཞེས་ཤེས་པར་བྱའོ། །

[Block 760 [HEADING]]
#### གཟུགས་བརྙན། ^2-15-4-0

[Block 761]
ཡང་དོན་མེད་ན་ལས་དགེ་བ་དང་མི་དགེ་བ་རྣམས་ཀྱི༌[^515]འབྲས་བུ་འདོད་པ་དང་མི་འདོད་པ་ཇི་ལྟར་མངོན་པར་འགྲུབ་པར་འགྱུར་སྙམ་དུ་སོམ་ཉི་ཟ་བ་དེ་བཟློག་པའི་ཕྱིར་གཟུགས་བརྙན་གྱི་དཔེས་ཆོས་མཐུན་པའི་གཞན་གྱི་དབང་བསྟན་ཏེ། ཇི་ལྟར་གཟུགས་ཀྱི་དོན་མེད་བཞིན་དུ་ཡང་གཟུགས་བརྙན་ལ་གཟུགས་ཉིད་ཀྱི་བློ་འབྱུང་བར་འགྱུར་ན་ཡང་གཟུགས་ཉིད་ཀྱི་དོན་ཡོད་པ༌[^516]ནི་མ་ཡིན་པ་དེ་བཞིན་དུ་འདིར་ཡང་འདོད་པ་དང་མི་འདོད་པའི་འབྲས་བུའི་དོན་ཡོད་པ་མ་ཡིན་ན་ཡང་དེ་དམིགས་པ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 762 [HEADING]]
#### མིག་ཡོར། ^2-15-5-0

[Block 763]
ཡང་དོན་མེད་ན་ཇི་ལྟར་རྣམ་པར་ཤེས་པ་སྣ་ཚོགས་འབྱུང་བར་འགྱུར་སྙམ་དུ་སོམ་ཉི་ཟ་བ་དེའི་གཉེན་པོར་གཞན་གྱི་དབང་དང་ཆོས་མཐུན་པ༌[^517]མིག་ཡོར་གྱི་དཔེས་བསྟན་ཏེ། ཇི་ལྟར་གྲིབ་མའི་རྩེད་མོ་འདོད་པའི་དབང་གིས་རྣམ་པ་སྣ་ཚོགས་སུ་སྒྱུར་བར༌[^518]བྱེད་པ་ན་དེ་ནི༌[^519]མིག་ཡོར་གྱི་དོན་མེད་བཞིན་དུ་ཡང་རྣམ་པ་སྣ་ཚོགས་སུ་སྣང་བ་ནི་དམིགས་སོ། །

[Block 764]
དེ་བཞིན༌[^520]རྣམ་པར་ཤེས་པ་ཡང་དོན་རྣམ་པ་སྣ་ཚོགས་མེད་ན་ཡང་དོན་རྣམ་པ་སྣ་ཚོགས་པ་ཉིད་དུ་སྣང་བ་ཡིན་ནོ། །

[Block 765 [HEADING]]
#### བྲག་ཅ། ^2-15-6-0

[Block 766]
ཡང་དོན་མེད་ན་ཇི་ལྟར་ཐ་སྙད་བརྗོད་པ་རྣམ་པ༌[^521]སྣ་ཚོགས་འབྱུང་བར་འགྱུར་སྙམ་དུ་སོམ་ཉི་ཟ་བ་དེ་བཟློག་པའི་ཕྱིར་བྲག་ཅ༌[^522]ལྟ་བུ་ཉིད་དོ་ཞེས་འདི་ལྟར་རྣམ་པར་འཇོག་པར་བྱེད་དེ། འདི་ལྟར༌[^523]དོན་མེད་བཞིན་དུ་ཡང་བྲག་ཅ་གྲག་པ༌[^524]དམིགས་པར་འགྱུར་བ་དེ་བཞིན་དུ་ཡང་ཐ་སྙད་བརྗོད་པ་སྣ་ཚོགས་མེད་བཞིན་དུ་དེ་ཉེ་བར་དམིགས་པར་འགྱུར་རོ། །

[Block 767 [HEADING]]
#### ཆུ་ཟླ། ^2-15-7-0

[Block 768]
ཡང་དོན་མེད་ན་ཇི་ལྟར་མཉམ་པར་གཞག་པ་རྣམས་ཀྱི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ལ་འཇིག་རྟེན་པའི་དོན་དམིགས་པར་འགྱུར་ཞེས་བྱ་བ་དང་། མཉམ་པར་གཞག་པའི་སེམས་ཀྱིས༌[^525]ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་ཤིང་ཇི་ལྟ་བ་བཞིན༌[^526]མཐོང་ངོ་ཞེས་འདི་ལྟར་འབྱུང་བ་དེ་ཇི་ལྟ་བུ་ཞེས་སོམ་ཉི་ཟ་བས་དེའི་གཉེན་པོར་ཆོས་མཐུན་པ་ཆུ་ཟླའི་དཔེས་བསྟན་ཏེ། ཇི་ལྟར་ཆུ་ལ་ཟླ་བའི་དོན་མེད་བཞིན་དུ་ཡང་རླན་པ༌[^527]ཉིད་དང་། དང་བའི་ཕྱིར་ཆུ་ལ་དེ་ཉེ་བར་དམིགས་པ་བཞིན་དུ་མཉམ་པར་གཞག་པའི་སེམས་ལ་དམིགས་པའི་དོན་མེད་བཞིན་དུ་ཡང་དེ་ཉེ་བར་དམིགས་པར་འགྱུར་ཏེ། འདིར་ཡང་ཆུ་ཟླ་ལྟ་བུ་ནི་རླན་པའི༌[^528]བདག་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་ཏིང་ངེ་འཛིན་ཡིན་ནོ། །

[Block 769 [HEADING]]
#### སྤྲུལ་པ། ^2-15-8-0

[Block 770]
ཡང་ཇི་ལྟར༌[^529]དོན་མེད་ན་སེམས་ཅན་གྱི་བྱ་བ་བསྒྲུབ་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་དེ་ཁོ་ན་ཉིད་རྟོགས་པ་རྣམས་སེམས་ཅན་རྣམས་ཀྱི་དོན་གྱི་ཕྱིར་བློ་སྔོན་དུ་བཏང་ནས་འགྲོ་བ་དེ་དང་དེ་དག་ཏུ་བདག་གི་ལུས་འཛིན་པར་བྱེད་ཅེས་སོམ་ཉི་ཟ་བ་དེའི་གཉེན་པོར་གཞན་གྱི་དབང་དང་ཆོས་མཐུན་པ་སྤྲུལ་པ་ལྟ་བུས་བསྟན་ཏེ། ཇི་ལྟར་སྤྲུལ་པའི་དོན་མེད་བཞིན་དུ་ཡང་སྤྲུལ་པའི་དབང་གིས་དགོས་པ་སྒྲུབ་པར་བྱེད་པ་ན་ཡང་སྤྲུལ་པའི་དོན་དམིགས་པ་བཞིན་དུ་བདག་གི་ལུས་ལེན་པའི་དོན་མེད་བཞིན་དུ་ཡང་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བྱེད་པ་པོའི་བདག་གི་ལུས་ལེན་པའི་དོན་ཉེ་བར་དམིགས་པར་བལྟ་བར་བྱའོ། །

[Block 771 [HEADING]]
### སྒྱུ་མ་ལ་སོགས་པའི་དཔེ་བརྒྱད། ^2-16-0

[Block 772]
བཅོམ་ལྡན་འདས་ཀྱིས་དོན་ཅི་ལས༌[^530]དགོངས་ནས་ཡོད་པ་མ་ཡིན་པའི་སྒྱུ་མ་ལ་སོགས་པའི་དཔེ་བརྒྱད་བསྟན་ཅེ་ན། དེ་བསྟན་པར་བྱའོ། །

[Block 773 [HEADING]]
#### སྒྱུ་མའི་དཔེ། ^2-16-1-0

[Block 774]
དེ་ལ་རེ་ཞིག་སྒྱུ་མའི་དཔེ་ནི་ནང་གི་བདག་ཉིད་ཅན་གྱི་སྐྱེ་མཆེད་དྲུག་པོ་མིག་ལ་སོགས་པ་རྣམས་ཀྱི་གཉེན་པོ་སྟེ་གང་གི་ཕྱིར་སྒྱུ་མའི་གླང་པོ་བཞིན་དུ་དེ་དག་ཡོད་པ་མ་ཡིན་ན་ཡང་ཉེ་བར་དམིགས་པ་ཉིད་དུ་བལྟ་བར་བྱའོ་ཞེས་སྟོན་ཏོ། །

[Block 775 [HEADING]]
#### སྨིག་རྒྱུའི་དཔེ། ^2-16-2-0
--- END BLOCKS ---
