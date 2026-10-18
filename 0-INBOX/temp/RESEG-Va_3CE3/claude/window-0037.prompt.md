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
[Block 1296]
ཚོར་བ་དང་འདུ་ཤེས་དང་འདུ་བྱེད་དང་རྣམ་པར་ཤེས་པའི་ཕུང་པོ་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་དེ་དག་གཟུགས་མེད་པས་མིང་གི་ཚོགས་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1297]
ཆོས་ཐམས་ཅད་འགྲོ་བ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་འགྲོ་བ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1298]
ཆོས་ཐམས་ཅད་གཟུང་དུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ་ཆོས་རྣམས་ནི་ཆོས་རྣམས་མི་འཛིན་ཏེ། དེ་བས་ན་མི་འཕྲོགས་པའོ། །

[Block 1299]
ཆོས་ཐམས་ཅད་ཤིན་ཏུ་བྱང་ཞིང་ཟད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཤིན་ཏུ་བྱང་བས་སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པའི་བདག་ཉིད་ཀྱིས་ཟད་པར་སྣང་བའོ། །

[Block 1300]
ཆོས་ཐམས་ཅད་སྐྱེ་བ་མེད་པ་དང་འགག་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་སྟོང་པ་སྟེ་སྐྱེ་བ་ཡང་མེད་འགག་པ་ཡང་མེད་པར་སྣང་བའོ། །

[Block 1301]
འཆི་འཕོ་དང་སྐྱེ་བ་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་དེའི་ཚེ་འཆི་འཕོ་བ་དང་། སྐྱེ་བ་དག་ཀུན་བརྟགས་པའི་དབང་གིས་སྣང་གི།[^907] དོན་དམ་པར་ནི་མ་ཡིན་པར་ཤེས་པའོ། །

[Block 1302]
ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས་འཇིག་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་ནི༌[^908]དེ་བཞིན་ཉིད་དེ། །དེ་ཡང་འགྱུར་བ་མེད་པའི་ཕྱིར་མི་འཇིག་པའོ། །

[Block 1303]
རྨི་ལམ་མཐོང་བ་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་རྨི་ལམ་གྱི་མཐོང་བའི་མིའི༌[^909]རྨི་ལམ་གྱི་དངོས་པོ་གང་ཡིན་པ་དེ་མི་དམིགས་ཤིང་མེད་པ་དེ་བཞིན་དུ་ཆོས་ཐམས་ཅད་ཀྱང་དངོས་པོ་མེད་པར་གནས་པའོ། །

[Block 1304]
འདི་ནི་རྣམ་པར་བྱང་བ་མ་མཆིས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། [^910]ཀུན་ནས་ཉོན་མོངས་པ་ཡོད་པར་མི་དམིགས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཀུན་ནས་ཉོན་མོངས་པ་ཡོད་ན་ནི་རྣམ་པར་བྱང་ཞིང་ཡོངས་སུ་དག་པར་འགྱུར་ན་འདི་ལྟར་ཆོས་ཐམས་ཅད་ངོ་བོ་ཉིད་ཀྱིས་ཡོངས་སུ་དག་པ་སྟེ། དེ་བས་ན་ཀུན་ནས་ཉོན་མོངས་པ་ཡང་མེད། རྣམ་པར་བྱང་བ་ཡང་མེད་དོ། །

[Block 1305]
འདི་ནི་གནས་མ་མཆིས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། ཆོས་ཐམས་ཅད་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་ཆོས་ཐམས་ཅད་དམིགས་སུ་མེད་པ་དེའི་ཕྱིར་གང་ན་ཡང་གནས་པར་མི་དམིགས་པའོ། །

[Block 1306]
ཆོས་ཐམས་ཅད་མ་ནོར་བ་དེ་བཞིན་ཉིད་དུ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་བྱེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ནི་མ་ནོར་བ་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་དེ་མ་ནོར་བའི་ངོ་བོ་ཉིད༌[^911]མངོན་སུམ་དུ་བྱེད་པའི་ཕྱིར་ཆོས་ཐམས་ཅད་ཞི་བའོ་ཞེས་ཤེས་རབ་ཉེ་བར་གནས་སོ། །

[Block 1307]
འདོད་ཆགས་ཀྱི་མཚན་མ་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆགས་པར་བྱ་བའི་དངོས་པོའི་མཚན་མ་མེད་པའོ། །

[Block 1308]
ཞེ་སྡང་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཞེ་སྡང་གི་རྒྱུར་གྱུར་པའི་མཚན་མ༌[^912]མེད་པའོ། །

[Block 1309]
འདི་ནི་ཚད་མ་མཆིས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། ཆོས་ཐམས་ཅད་ཀུན་ནས་ལྡང་བ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ་ཆོས་ཐམས་ཅད་ནི་ཚད་མའི༌[^913]དབང་གིས་ཀུན་ནས་བསླང་བ་ཡིན་ན་འདི་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་ཆོས་ཐམས་ཅད་ཀྱི་ཚད་ཀུན་དུ་འབྱུང་བའི་གཞི་མི་མཐོང་སྟེ་དེ་བས་ན་ཚད་མེད་པའོ། །

[Block 1310]
ཆོས་ཐམས་ཅད་འདྲེས་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་དབེན་པའི་ཕྱིར་རོ། །

[Block 1311]
ཆོས་ཐམས་ཅད་ཚད་མ་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་གཞལ་བྱ་ཡོད་ན་ཚད་མ་ཡང༌[^914]ཡོད་ན་གཞལ་བྱ་ཡང་ཡོད་པར་འགྱུར་ན་འདི་ལྟར་ཆོས་ཐམས་ཅད་ཀྱི་ཚད་མ་མི་དམིགས་ཤིང་མེད་པས་དེ་བས་ན་གཞལ་བྱ་མེད་དོ། །

[Block 1312]
ཆོས་ཐམས་ཅད་ནམ་མཁའ་ལྟར་ཆགས་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ནམ་མཁའ་དང་འདྲ་བར་ཆགས་པ་མེད་པའོ། །

[Block 1313]
འདི་ནི་མི་རྟག་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། ཆོས་ཐམས་ཅད་འཇིག་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཆོས་ཐམས་ཅད་རི་བོང་གི་རྭ་ལ་སོགས་པ་བཞིན་དུ་མ་སྐྱེས་པའི་ཕྱིར་མི་འཇིག་པ་སྟེ་དེ་བས་ན་མེད་དོ།[^915] །ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་མི་རྟག་པ་སྟེ་མེད་པའི་དོན་ནི་མི་རྟག་པའི་དོན་ཏོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1314]
ཆོས་ཐམས་ཅད་ལྷག་པར་ཞེན་པར་བྱ་བའི་འོས་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཆོས་ཐམས་ཅད་ལྷག་པར་ཞེན་པར་བྱ་བའམ། གནས་པར་བྱ་བའམ། ཉེ་བར་སྤྱད་པར་བྱ་བའི་འོས་མ་ཡིན་ཏེ་དེ་བས་ན་སྡུག་བསྔལ་བའོ། །

[Block 1315]
འདི་ནི་སྟོང་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་ཀྱི་ངོ་བོ་ཉིད་གཟུགས་སུ་རུང་བ་དང་། མྱོང་བ་ལ་སོགས་པའི་ངོ་བོ་ཉིད་གང་ཡིན་པ་དེ་དོན་དམ་པར་ཡོད་པ་མ་ཡིན་ཏེ། དེ་བས་ན་ཆོས་དེ་དག་ངོ་བོ་ཉིད་དེས་སྟོང་ངོ་། །འདི་ནི་བདག་མ་མཆིས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། ཆོས་ཐམས་ཅད་མངོན་པར་ཞེན་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་མེད་དོ། །

[Block 1316]
དེའི་ཕྱིར་དེ་དག་མངོན་པར་ཞེན་པར་བྱ་བའི་འོས་མ་ཡིན་ཏེ། དེ་ལྟར་ན་ཆོས་ཐམས་ཅད་མེད་པ་ནི་བདག་མེད་པའོ། །

[Block 1317]
སྟོང་པ་ཉིད་དང་བདག་མེད་པ༌[^916]གཉིས་ལ་དོན་ཐ་དད་པ་མེད་དུ་ཟིན་ཀྱང་བརྟགས་པའི་དབང་གིས་ཐ་དད་པ་ཡོད་དོ། །

[Block 1318]
སྟོང་པ་ནི་གཞན༌[^917]བྲལ་བ་སྟེ། དཔེར་ན་ཆུ་དང་བྲལ་བའི་ཕྱིར་བུམ་པ་སྟོང་པ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1319]
དེ་བཞིན་དུ་རང་གི་མཚན་ཉིད་ལ་སོགས་པའི་ངོ་བོ་ཉིད་དང་བྲལ་བའི་ཕྱིར་ཆོས་དེ་དག་ཉིད་ལ་སྟོང་པ་ཞེས་ཀུན་ཏུ་རྟོག་གོ། །

[Block 1320]
བདག་མེད་པ་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་མེད་པ་ཉིད་དེ། དཔེར་ན་སྒྱུ་མའི་གླང་པོ་ཆེ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 1321]
ཆོས་དེ་དག་ཉིད། རང་གི་མཚན་ཉིད་ལ་སོགས་པ་དང་བྲལ་བར་བརྗོད་པར་འདོད་པ་ལ་སྟོང་པ་ཞེས་བྱའོ། །

[Block 1322]
ཡོད་པ་མ་ཡིན་ནོ་ཞེས་དངོས་པོ་མེད་པར་བརྗོད་པར་འདོད་པ་ལ་ནི་བདག་མེད་པ་ཞེས་བྱའོ། །

[Block 1323]
ཆོས་ཐམས་ཅད་མཚན་མ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ་མཚན་མ་ནི་མཚན་ཉིད་ཡིན་ན་འདི་ལྟར་མཚན་མ་མེད་པས་དེའི་ཕྱིར་མཚན་ཉིད་མེད་པའོ། །

[Block 1324]
སྟོང་པ་སྟོང་པ་ཉིད་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་ལ་སྟོང་པ་ཉིད་གཉིས་པ་མེད་པ་ཙམ་ལ། སྟོང་པ་སྟོང་པ་ཉིད་ཅེས་བྱའི། སྟོང་པ་སྟོང་པ་ཉིད་ཅེས་བྱ་བའི་ཆོས་གཞན་ནི་གང་ཡང་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1325]
ཆེན་པོ་སྟོང་པ་ཉིད་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཕྱོགས་ཐམས་ཅད་ན་ཡང༌[^918]གཟུགས་རྣམས་མེད་པ་ཙམ་གྱི་ཆེ་བ་ལ་ཆེན་པོ་སྟོང་པ་ཉིད་ཅེས་བྱའོ། །

[Block 1326]
ཆེན་པོ་སྟོང་པ་ཉིད་ཅེས་བྱ་བའི་ཆོས་གཞན་ནི་གང་ཡང་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1327]
དེ་བཞིན་དུ་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1328]
འདི་ནི་རང་བཞིན་སྟོང་པ་ཉིད་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་ཆོས་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་འདུས་བྱས་དང་འདུས་མ་བྱས་པའི་ཆོས་རྣམས་དམིགས་སུ་ཡོད་ན་ནི་དེ་དག་གི་རང་བཞིན་སྟོང་པ་མ་ཡིན་པར་འགྱུར་བ་ཞིག་ན། འདི་ལྟར་ཆོས་ཐམས་ཅད་སྟོང་པ་སྟེ། དེ་བས་ན་དེ་དག་གི་རང་བཞིན་སྟོང་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1329]
འདི་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། སེར་སྣ་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སེར་སྣ་དམིགས་སུ་མེད་པ་གང་ཡིན་པ་དེ་ཡང་སྦྱིན་པའི་མཚན་ཉིད་དོ། །

[Block 1330]
དེ་བཞིན་དུ་གཞན་དག་ལ་ཡང་སྦྱར་རོ། །

[Block 1331]
འདི་ནི་སྟོབས་བཅུའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། ཆོས་ཐམས་ཅད་ཀྱི་རྣམ་པ་ཐམས་ཅད་དམིགས་སུ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་རྣམ་པ་ཐམས་ཅད་ནི་གནས་དང་གནས་མ་ཡིན་པ་མཁྱེན་པའི་སྟོབས་ལ་སོགས་པ་ཡེ་ཤེས་བཅུའི་སྤྱོད་ཡུལ་ཡིན་ན་དེ་དག་གི་སྤྱོད་ཡུལ་དུ་མ་གྱུར་པ་ནི་རྣམ་པ་ཡོད་པ་མ་ཡིན་ཏེ། འདི་ལྟར་རྣམ་པ་དེ་དག་དོན་དམ་པར་མེད་པས་དེའི་ཕྱིར་སྟོབས་བཅུའི་ཡུལ་དུ་གྱུར་པ་རྣམ་པ་རྣམས་མེད་པར་མཐོང་བའི་ཕྱིར་སྟོབས་བཅུའི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 1332]
ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ཞུམ་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ནི་ཆོས་གང༌[^919]ཡང་ཞུམ་པ་མེད་དེ་དེ་བས་ན་ཐམས་ཅད་དུ་ཞུམ་པ་མེད་པའི་རང་བཞིན་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ལ་མི་འཇིགས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 1333]
ཐམས་ཅད་དུ་ཡེ་ཤེས་ཆགས་པ་མེད་ཅིང་ཐོགས་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའི་ཡེ་ཤེས་ནི་ཐམས་ཅད་དུ་ཆགས་པ་མེད་པ་དང་། ཐོགས་པ་མེད་པ་སྟེ། དེ་བས་ན་དེ་སོ་སོ་ཡང་དག་པར་རིག་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 1334]
ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ལས་ཡང་དག་པར་འདས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་འདི་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དེ༌[^920]ཉན་ཐོས་ལ་སོགས་པ་ལ་མེད་པས་དེའི་ཕྱིར་དེ་སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པ་ཞེས་བྱ་བར་བགྲང་ངོ་། །འདི་ནི་དེ་བཞིན་གཤེགས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། སངས་རྒྱས་ཐམས་ཅད༌[^921]ཀྱིས་གསུངས་པ་དེ་བཞིན་གཤེགས་པ་ཉིད་ཡིན་པའི༌[^922]ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ངེས་པའི་ཚིག་གིས་ནི༌[^923]དེ་བཞིན་དུ་གསུང་བའི༌[^924]ཕྱིར་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་སྟེ། སངས་རྒྱས་ཀྱིས་གསུངས་པ་ཐམས་ཅད་ལ་དེ་བཞིན་དུ་དམིགས་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་དེ་བཞིན་གཤེགས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 1335]
འདི་ནི་རང་བྱུང་གི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། ཆོས་ཐམས་ཅད་ལ་དབང་བསྒྱུར་བའི༌[^925]ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཆོས་ཐམས་ཅད་དེའི་དབང་དུ་འགྱུར་ཏེ།[^926] དེའི་ཕྱིར་རང་གིས་ཆོས་ཐམས་ཅད་ཟིལ་གྱི༌[^927]གནོན་པས་རང་བྱུང་གི༌[^928]ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །
--- END BLOCKS ---
