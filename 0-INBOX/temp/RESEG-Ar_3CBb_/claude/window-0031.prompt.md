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
[Block 1086]
[^520]དེ་ནས་སྣང་བ་གསུམ་གྱི་གོ་རིམས༌[^521]གཏན་ལ་དབབ་པར་བྱ་བའི་ཕྱིར། གང་ཡང་རྣམ་ཤེས་གསུམ་དང་པོ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རྣམ་པར་ཤེས་པ་གསུམ་གྱི་དང་པོ་ནི་དེའི་མིང་ཅན་སྣང་བའོ། །

[Block 1087]
གཉིས་པ་སྣང་བ་མཆེད་པ༌[^522]སྟེ། །ཞེས་བྱ་བ་ནི་སྣང་བ་མཆེད་པ༌[^523]ནི་སྣང་བ་ལ་ལྟོས༌[^524]ནས་གཉིས་པའོ། །

[Block 1088]
དེ་ནི་སྟོང་པ་ཆེར་འགྲོ་ལ། །ཞེས་པ་ནི་སྣང་བ་ཐོབ་པ་ཉིད་དོ། །

[Block 1089]
གཉིས་སྔོན་དུ་འགྲོ་བའོ། །

[Block 1090]
དེ་ཡང་འོད་གསལ་བར་འགྲོའོ། །ཞེས་པ་ནི་དེས་ཐམས་ཅད་སྟོང་པ་འོད་གསལ་བ་ཐོབ་པར་འགྱུར་རོ། །

[Block 1091]
འདི་དག་གི༌[^525]གོ་རིམས༌[^526]ཀྱང་སློབ་པའི༌[^527]གོ་རིམས༌[^528]དང་རང་བཞིན་འབྱུང་བའི་གོ་རིམས༌[^529]དང་མཐར་ཕྱིན་པའི་གོ་རིམས་སོམོ།[^530] །དེ་ལ་སློབ་པའི་གོ་རིམས༌[^531]གང་ཞེ་ན་གང་ཞིག་རིམ་གྱིས་སློབ་པར་འགྱུར་བ་སྟེ། འདི་ལྟར་འཕོང་གི་སློབ་དཔོན་ནམ་སློབ་མ་མཁས་པ་དག་ནི་ཐོག་མར་བ་ལང་གི་ཀོ་བ་ལ་སློབ་པར་བྱེད་དོ། །

[Block 1092]
གང་གི་ཚེ་བ་ལང་གི་ཀོ་བ་ལ་ལོབས་པ་དེའི་ཚེ་ཤིང་ལེབ་ལ་སློབ་པར་བྱེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་གསུངས་པའི་ཕྱིར་རོ། །

[Block 1093]
འདི་ནི་སློབ་པའི་གོ་རིམས༌[^532]ཉིད་དོ། །

[Block 1094]
རང་བཞིན་འབྱུང་བའི་གོ་རིམས༌[^533]ནི་མ་བཅོས་པར་ཡོད་པའི་ཆོས་ཏེ་འདི་ལྟར་རླུང་ལས་ནི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བའི་བཤད་པ། བློ་གྲོས་ཆེན་པོ་ཤིང་ཨ་མྲའི་འབྲས་བུ་ནི་རིམ་གྱིས་སྐྱེའི་ཅིག་ཅར་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་དང་། གཞན་ཡང་།

[Block 1095 [VERSE]]
བསྐྱེད་པའི་རིམ་ལ་ལེགས་གནས་ཤིང་། །
རྫོགས་པའི་རིམ་པ་འདོད་རྣམས་ལ། །
ཐབས་འདི་རྫོགས་པའི་སངས་རྒྱས་ཀྱིས། །
སྐས་ཀྱི་རིམ་པ་ལྟ་བུར་གསུངས། །

[Block 1096]
ཞེས་བྱ་བ་ལ་སོགས་པའི་སྒྲའི་རྗེས་སུ་འབྲངས་ཏེ་གསུངས་པ་ཤེས་པར་བྱའོ། །

[Block 1097]
འོད་གསལ་བ་ལས་ནི་སྣང་བ་ཐོབ་པ་འབྱུང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་མཐར་ཕྱིན་པའི་གོ་རིམས༌[^534]བསྟན་ཏོ། །

[Block 1098]
དེ་བས་ན་གང་གིས་གང་ཞིག་ལེགས་པར་རྟོགས་པར་འདོད་པ་དང་མྱུར་དུ་རྟོགས་པར་འདོད་པ་དང་། ཐབས་སླ་བ་རྟོགས་པར་འདོད་པས་ནི་ཇི་སྐད་དུ་གསུངས་པ་དང་བཤད་པའི་གོ་རིམས༌[^535]ལ་མཁས་པར་བྱའོ། །

[Block 1099]
དེ་བས་ན༌[^536]སྣང་བ་གསུམ་པ་འདིས༌[^537]ནི་སེམས་ཅན་ཐམས་ཅད་འཕེལ་བ་དང་འགྲིབ་པར་བྱེད་དོ་ཞེས་བྱ་བ༌[^538]རྟོགས་པར་བྱ་བའི་ཕྱིར། སྣང་བ་གསུམ་གྱི་མཚན་ཉིད་ཅན། །ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་ལ་སྣང་བའི་མཚན་ཉིད་གང་ཞེ་ན་རྣམ་པ་མེད་པའི་རང་བཞིན་རང་རིག་པ་ལུས་དང་ངག་མེད་པ་སྟེ། ཇི་ལྟར་སྟོན་ཀའི་དུས་སུ་ནམ་མཁའ་དྲི་མ་མེད་པ་ལ་ཟླ་བའི་འོད་ཟེར་གྱིས་རབ་ཏུ་སྣང་ཞིང་ཀུན་དུ་སྣང་བ་དང་། ཁྱབ་པར་བྱེད་པ་དེ་བཞིན་དུ་རང་བཞིན་གྱིས་གསལ་བའི་རྣམ་པ༌[^539]དངོས་པོ་མ་ལུས་པ་ཐམས་ཅད་ལ་དམིགས་པས་ན། སྣང་བ་སྟེ།[^540] དོན་དམ་པ་བྱང་ཆུབ་ཀྱི་སེམས་ཤེས་རབ་ཀྱི་སྣང་བ་སྟོང་པ་དང་པོ་སྟེ། ཨོཾ་ཞེས་བྱ་བའི་ངག་གི་སྒོ་ལ་བརྟེན༌[^541]ནས་རང་གི་ས་བོན་སྟོན་པར༌[^542]བྱེད་པ་སྟེ། མོས་པ་དམན་པའི་སེམས་ཅན་རྣམས་ཀྱིས་དེ་བཞིན་གཤེགས་པས་དགོངས་ཏེ་གསུངས་པ་རྟོགས་པར་མི་འགྱུར་བས་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་གཟུགས་སོ་ཞེས་དམིགས་པར་བྱེད་ཅིང་པདྨའམ་བུད་མེད་ཀྱི་གཟུགས་ལ་སོགས་པས་ཡོངས་སུ་གསལ་བར་བརྗོད་པ༌[^543]འཇུག་པར་འགྱུར་རོ། །

[Block 1100]
སྣང་བ་མཆེད་པའི་མཚན་ཉིད་ཇི་ལྟ་བུ་ཞེ་ན་གཟུང་བ་དང་འཛིན་པ་དང་བྲལ་བ་ལུས་དང་ངག་མེད་པ་སྟེ། དཔེར་ན་སྟོན་ཀའི་དུས་སུ་ཉི་མའི་འོད་ཟེར་གྱིས་ཁྱབ་པ་བཞིན་དུ་ཤིན་ཏུ་གསལ་ཞིང་དྲི་མ་མེད་པའི་ངོ་བོ་ཉིད་དུ་དངོས་པོ་མ་ལུས་པ་དམིགས་པ་བྱང་ཆུབ་ཀྱི་སེམས་ཀུན་དུ་བཟང་པོའི་རིམ་པ་གཉིས་པ་ཤིན་ཏུ་སྟོང་པའི་མཚན་ཉིད་ཅན། ཨཱཿཞེས་བྱ་བའི་ངག་གི་སྒོ་ལ་རྟེན་པར༌[^544]བྱེད་པའི་ས་བོན་བསྟན་པར༌[^545]བྱ་བའི༌[^546]རྒྱུ་སྟེ། མོས་པ་ཆུང་བའི་སེམས་ཅན་རྣམས་ཀྱིས་དེ་བཞིན་གཤེགས་པས་དགོངས་ཏེ་གསུངས་པ་རྟོགས་པར་མི་འགྱུར་བས་ཉི་མའི་དཀྱིལ་འཁོར་ལ་བརྟེན་ནས་དམིགས་པར་བྱེད་ཅིང་རྡོ་རྗེ་རྩེ་ལྔ་པའམ་རིན་པོ་ཆེ་འམ། ཉིན་མོ་འམ། གཡས་པ་ཞེས་བྱ་སྟེ་སྲ་བའི་རྣམ་པ་དང་། ཀུན་དུ་རྒྱས་པའི་རྣམ་པ་ནི་སེམས་ལས་བྱུང་བ་ཀུན་རྫོབ་ཀྱི་གཟུགས་སོ། །

[Block 1101]
སྣང་བ་ཐོབ་པའི་མཚན་ཉིད་གང་ཞེ་ན་ནམ་མཁའི་མཚན་ཉིད་དངོས་པོ་ཐམས་ཅད་དང་བྲལ་བ་ལུས་དང་ངག་མེད་པ་སྟེ། ཇི་ལྟར་མཚམས་ཀྱི་སྨག་ལ་བབ་པ་ངོ་བོ་ཁྱབ་པ་བཞིན་དུ་ཕྲ་ཞིང་བདག་མེད་པ་སྣང་བ་མེད་པ་ཀུན་དུ་ཉེ་བར་སྣང་བ་མེད་པ་སྟེ་སྲོག་དང་རྩོལ་བ་མི་རྒྱུ་བས་སེམས་མེད་པ་མི་གཡོ་བ། ཨཱཿཞེས་བྱ་བ་ངག་གི་ས་བོན་ལ་བརྟེན་པའི་སྒོ་ཡོངས་སུ་གྲུབ་པ་བླུན་པ། ཞེན་པ་གང་གིས་གང་ལ་གཡོ་བ་མེད་པ་མ་རིག་པ་འདི་ནི་སྣང་བ་ཐོབ་པ་ཞེས་བྱའོ། །

[Block 1102 [VERSE]]
འདི་དག་གིས་ལས་ཅི་བྱེད་ཅེ་ན། །
སེམས་ཅན་ཁམས་ནི་མ་ལུས་པའི། །
རང་བཞིན་རྩ་བ་ཉིད་ཡིན་ནོ། །

[Block 1103]
ཞེས་པ། སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་སྐྱེ་བ་དང་ཀུན་དུ་འཆི་བ་ལ་སོགས་པ་བྱེད་པ་སྟེ། བྱམས་པའི་གསུང་གིས་ཇི་ལྟ་བུར་ཡོངས་སུ་བཤད་པ་ལྟ་བུའོ། །

[Block 1104]
དེས་ན༌[^547]ཡུལ་འདི་དག་ལ་ནི་ཤེས་པས་སོ་སོར་ངེས་པར་འཛིན་ཏེ་དེའི་རླུང་གིས་ཉེ་བར་བླངས་པ་ཉིད་དོ་ཞེས་བྱ་བ་འདི་བསྟན་ལ། དེ་ནི་རེ་རེའི་དོན་སྣང་བ། །ཞེས་པ་ནི་གཟུགས་དང་སྒྲ་ལ་སོགས་པས་ཤེས་པ་སོ་སོར་ངེས་པར་འགྱུར་རོ། །

[Block 1105]
དེ་བས་ན་ཞེས་བྱ་བ་ལ་སོགས་པར་སྣང་བའོ། །གང་གི་སྟོབས་ཀྱིས༌[^548]འབྱུང་ཞེ་ན།

[Block 1106 [VERSE]]
དེ་ནི་རེ་རེའི་དོན་སྣང་བ། །
རླུང་གིས་བླངས་ནས་འཛིན་བྱེད་ལ། །

[Block 1107]
ཞེས་པ་རླུང་གིས་ཤེས་པ་ཀུན་དུ་གཡོ་བར་འགྱུར་རོ། །ཤེས་པས་ནི་ཡུལ་འཛིན་པར་འགྱུར་རོ། །

[Block 1108]
རླུང་དང་རྣམ་ཤེས་ནི་རླུང་དང་རྣམ་ཤེས་ཏེ་ལྷན་ཅིག་ཏུ་འབྱུང་ཞིང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1109]
དེ་གང་ལ་གནས་ཤེ་ན།

[Block 1110 [VERSE]]
རླུང་དང་ལྡན་པའི་རྣམ་ཤེས་ནི། །
རྟག་ཏུ་འགྲོ་ལ་གནས་པར་འགྱུར། །

[Block 1111]
ཞེས་པ་སྟེ་རླུང་དང་ཤེས་པ་གཉིས་ནི་འགྲོ་བ་ཐམས་ཅད་ལ་གནས་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1112]
དེ་དག་གི་དོན་ནི་འདི་སྐད་དུ་སྟོན་ཏོ།[^549] །ཤེས་པ་བེམས་པོའི་ངོ་བོ་ལས་ལོག་ཅིང་རང་རིག་པ་ནི་སེམས་ཅན་ཐམས་ཅད་ལ་རང་བཞིན་གྱིས་གནས་ཏེ་ཀུན་དུ་གཡོ་བ་དང་རབ་ཏུ་འཁྲུལ་པའི༌[^550]བྱ་བ་བྱེད་པར་འགྱུར་བ་མེད་དོ།[^551] །གང་ཞིག་ཏུ་འདི་དག་རླུང་གིས་བསྐུལ་ནས་མིག་ལ་སོགས་པ་ལ་བརྟེན་ཏེ་གཟུགས་ལ་སོགས་པ་ལ་དམིགས་ནས་སོ་སོར་རྣམ་པར་རིག་པར་འགྱུར་རོ། །

[Block 1113]
གང་རྣམ་པར་རིག་པ་དེ་ནི་གཙོ་བོ་ཡིན་པར་འགྱུར་རོ། །

[Block 1114]
གང་གཙོ་བོ་ཡིན་པ་དེ་ནི་ངེས་པར་གཟུང་བ་ཉིད་དང་ལྡན་པར་འགྱུར་རོ། །

[Block 1115]
གང་ངེས་པར་གཟུང་བ་གཉིས༌[^552]ལྡན་པ་དེ་ནི་ངེས་པའི༌[^553]ཤེས་པ་མྱུར་དུ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1116]
དེ་བས་ན་གང་དང་གང་ལྡན་པ་དེ་ལ་དེ་དང་དེས་གང་དུ་ངེས་པར་རྟོགས་པ་དེ་ནི་དཀའ་བ༌[^554]མ་ཡིན་ཏེ་བཤད་པར་བྱའོ། །

[Block 1117]
སེམས་དེ་ལས་ཀྱང་། རང་བཞིན་ཇི་ལྟར་འབྱུང་བར་འགྱུར། །ཞེས་ཉེ་བར་རྟོག་པ་གང་དག་ལ་རབ་ཏུ་གསལ་བར་བཤད་པ། ཨེ་འདི་ནི་རླུང་ཁམས་ཆེན་པོ་སྟེ་ཞེས་པ་ཁམས་ཕྲ་བར་གྱུར་པ་ཉིད་དོ། །

[Block 1118]
རྣམ་ཤེས་གསུམ་གྱི་བཞོན་པ་ཡིན། །ཞེས་པ་སྣང་བ་ལ་སོགས་པའི་ཤེས་པའི་བཞོན་པར་གྱུར་པ་ཉིད་དོ།[^555] །

[Block 1119 [VERSE]]
དེ་ཡི་རང་བཞིན་རྟག་ཏུ་ནི། །
ཇི་ལྟ་ཇི་ལྟར་འགྲོ་བར་འགྱུར། །

[Block 1120]
ཞེས་པ་ཤེས་པ་པོ་ལ་ཡུལ་ལ་དམིགས་པ༌[^556]ལས་རང་བཞིན་དེ་དང་དེའི་རྣམ་པ་མ་ལུས་པ་དུས་ཐམས་ཅད་དུ་འབྱུང་བར་འགྱུར་རོ། །

[Block 1121]
ཇི་སྐད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་ཡེ་ཤེས་རྡོ་རྗེ་ཀུན་ལས་བཏུས་པ་ཞེས་བྱ་བ་ལས་གསུངས་ཏེ། དེ་ནས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་བྱམས་པ་སྟན་ལས་ལངས་ཏེ། བཅོམ་ལྡན་འདས་ཀྱི་ཞབས་ལ་སྤྱི་བོས་ཕྱག་འཚལ་ནས་བཅོམ་ལྡན་འདས་ལ་འདི་སྐད་ཅེས་གསོལ་ཏོ། །

[Block 1122]
ཨེ་མའོ་སྟོན་པ་རྣམ་པར་ཤེས་པ་གསུམ་པོ་རྟོགས་པར་དཀའ་བ་མཆོག་ཏུ་རྟོགས་པར་དཀའ་བ་སྟེ། རྣམ་པར་ཤེས་པ་གསུམ་གྱི་དབྱེ་བ་བསྟན་དུ་གསོལ། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རྣམ་པར་ཤེས་པ་ནི༌[^557]འོད་གསལ་བ་ལས་འབྱུང་ངོ་། །དེ་ནི་སེམས་དང་ཡིད་ཅེས་བྱ་སྟེ་ཀུན་ནས་ཉོན་མོངས་པ་དང་རྣམ་པར་བྱང་བ་དང་དེའི་བདག་ཉིད་ཅན་གྱི་ཆོས་ཐམས་ཅད་ཀྱི་རྩ་བ་ཡིན་ནོ། །

[Block 1123]
དེ་ལས་བདག་དང་གཞན་དུ་རྟོག་པ་འབྱུང་བར་འགྱུར་རོ། །

[Block 1124]
རྣམ་པར་ཤེས་པ་དེ་རླུང་ལ་ཞོན༌[^558]ཏེ་རླུང་ལས་ནི་མེའོ། །

[Block 1125]
མེ་ལས་ནི་ཆུའོ། །
--- END BLOCKS ---
