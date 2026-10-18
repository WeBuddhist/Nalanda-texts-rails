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
[Block 1471]
ཡང་གང་ལ་ལམ་ལ་དམིགས་པ་ལོག་པར་ལྟ་བའམ། ཐེ་ཚོམ་ཡོད་པ་དེ་ཐར་པའི་ལམ་མེད་དོ་ཞེས་ལྟ་བའམ། ཐེ་ཚོམ་ཟ་བ་ན༌[^1046]ཇི་ལྟར་དཔེ་དག༌[^1047]པར་ཡིད་ཆེས་པར་འགྱུར། འོན་ཏེ་ཐར་པའི་ལམ་གཞན་མཆོག་ཏུ་བཟུང་ནས་འདི་ནི་ཐར་པ་ཡིན་གྱི་ལམ་ནི་མེད་དོ་ཞེས་སྨྲའོ་ཞེ་ན། དེ་ཡང་གཞན་དེ་ཁོ་ནས་དག་པར་ཡིད་ཆེས་ཀྱི་ལོག་པར་ལྟ་བ་དེ༌[^1048]ནི་མ་ཡིན་པས་དེའི་དེ་ཡང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ལ་དམིགས་པར་མི་འགྲུབ་བོ། །

[Block 1472]
ཡང་གང་ཞིག་ཀུན་འབྱུང་དང་འགོག་པ་མཐོང་བས་སྤང་བར་བྱ་བ་ལ་དམིགས་པའི་ལོག་པར་ལྟ་བས་ཡང༌[^1049]དག་པར་ཡིད་ཆེས་པར་འགྱུར་བ་དེ་ཡང་། ཅིའི་ཕྱིར་དེ་དག་མཐོང་བས་སྤང་བར་བྱ་བ་མ་ཡིན། དེ་ལྟ་བས་ན་དོན་འདི་ནི་རྟག༌[^1050]པར་བྱ་བ༌[^1051]ཡིན་ནོ། །

[Block 1473 [HEADING]]
### ཕྱིན་ཅི་ལོག་བཞི། ^2-10-0

[Block 1474]
བདག༌[^1052]རྟག༌[^1053]ཕྱིན་ཅི་ལོག་པ་ཡིས། །ཞེས་གང་བཤད་པ། ཅི་ཕྱིན་ཅི་ལོག་དེ་གཉིས་ཁོ་ནར་ཟད་དམ་ཞེ་ན། ཕྱིན་ཅི་ལོག་ནི་བཞི་སྟེ། མི་རྟག་པ་ལ་རྟག་པ་དང་། སྡུག་བསྔལ་བ་ལ་བདེ་བ་དང་། མི་གཙང་བ་ལ་གཙང་བ་དང་། བདག་མེད་པ་ལ་བདག་ཏུ་ཕྱིན་ཅི་ལོག་པའོ། །

[Block 1475]
ཡང་ཕྱིན་ཅི་ལོག་བཞི་ཚན་འདིའི་རང་བཞིན་ཅི་ཞེ་ན། ལྟ་བ་གསུམ་ལས་ཕྱིན་ཅི་ལོག །བཞི་ཚན། མཐར་འཛིན་པར་ལྟ་བ་ལས་རྟག་པར་ལྟ་བ་ནི། རྟག་པར་ནི༌[^1054]ཕྱིན་ཅི་ལོག་གོ། །

[Block 1476]
ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་ལས་ནི་བདེ་བ་དང་གཙང་བར་ཕྱིན་ཅི་ལོག༌[^1055]གོ། །

[Block 1477]
འཇིག་ཚོགས་སུ་ལྟ་བ་ལས་ནི་བདག་ཏུ་ལྟ་བ་ཕྱིན་ཅི་ལོག་གོ། །

[Block 1478]
གཞན་དག་ན་རེ་ཐམས་ཅད་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1479]
ཅི་ལྟར༌[^1056]ན་བདག་གིར་ལྟ་བ་ཕྱིན་ཅི་ལོག་མ༌[^1057]ཡིན། ཅི་ལྟར༌[^1058]ན་ཕྱིན་ཅི་ལོག་མ་ཡིན། ཕྱིན་ཅི་ལོག་གི་མདོ་ལས་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1480]
དེ་ལས་ནི་བདག་ཁོ་ན་དབང་བྱེད་པར༌[^1059]ལྟ་བ་ན། བདག་གིར་ལྟ་བར་འགྱུར་བར༌[^1060]བཤད་པ་ཡིན་པས། བདག་ཏུ་ལྟ་བ་འདི་ཉིད་སྒོ་གཉིས་པ་ཅན་ཡིན་ནོ། །

[Block 1481]
འོན་ཏེ་བདག་ཅེས་བྱ་བ་འདི་ལས་བདག་གི་ཞེས༌[^1061]བྱ་བ་ལྟ་བ་གཞན་ཞིག་ཡིན༌[^1062]ན་ནི་བདག་གིས༌[^1063]ཞེས་བྱ་བ་དང་། བདག་གི་ཕྱིར་ཞེས་བྱ་བ་འདིར༌[^1064]ཡང་འགྱུར་རོ། །

[Block 1482]
ཅིའི་ཕྱིར་ཉོན་མོངས་པ་གཞན་དག་ཕྱིན་ཅི་ལོག་མ་ཡིན་ཞེ་ན། འདི་ལྟར་རྒྱུ་གསུམ་གྱིས་རྟེན་ཕྱིན་ཅི་ལོག༌[^1065]རྣམ་པར་བཞག་སྟེ། གསུམ་གང་ཞེ༌[^1066]ན། ཕྱིན་ཅི་ལོག་ཕྱིར་དང་། ངེས་རྟོག་ཕྱིར་དང་སྒྲོ་འདོགས་ཕྱིར། །དམིགས་པ་ལ་གཅིག་ཏུ་ཕྱིན་ཅི་ལོག་པའི་ཕྱིར་དང་། ངེས་པར་རྟོག་པའི་ཕྱིར་དང་། སྒྲོ་འདོགས་པའི་ཕྱིར་ཏེ།[^1067] ཆད་པར་ལྟ་བ་དང་། ལོག་པར་ལྟ་བ་ནི་མེད་པའི་སྒོར་ཞུགས་པའི་ཕྱིར་དང༌[^1068]སྒྲོ་འདོགས་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1483]
ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་ནི་དེ་ཙམ༌[^1069]ཞིག་གིས། འདག་པར་དམིགས་པའི་ཕྱིར་གཅིག་ཏུ་ཕྱིན་ཅི་ལོག་པ་མ་ཡིན་ནོ། །

[Block 1484]
ཉོན་མོངས་པ་གཞན་དག་ནི་ངེས་པར་རྟོག་པར་བྱེད་པ་མ་ཡིན་པས་དེའི་ཕྱིར་ཕྱིན་ཅི་ལོག་དག་མ་ཡིན་ནོ། །

[Block 1485]
འོ་ན་མདོ་ལས་མི་རྟག་པ་ལ་རྟག་གོ་སྙམ་དུ་འདུ་ཤེས་ཕྱིན་ཅི་ལོག་པ་དང་། སེམས་ཕྱིན་ཅི་ལོག་པ་དང་། ལྟ་བ་ཕྱིན་ཅི་ལོག་པ་ཞེས་གང་གསུངས་པ་ཇི་ལྟ་བུ་ཞེ་ན། འདིར་ནི་ལྟ་བ་ཁོ་ན་ཕྱིན་ཅི་ལོག༌[^1070]ཡིན་ལ། སེམས་དང་འདུ་ཤེས་དེའི་དབང་གིས་ལྟ་བ་ཕྱིན་ཅི་ལོག་གི་དབང་གིས༌[^1071]དེ་དང་མཚུངས་པར་ལྡན་པ་འདུ་ཤེས་དང་། སེམས་ཕྱིན་ཅི་ལོག་ཏུ་བཤད་དོ། །

[Block 1486]
ཚོར་བ་ལ་སོགས་པ་ཡང་ཅིའི་ཕྱིར་མ་བཤད་ཅེ་ན། འཇིག་རྟེན་ན༌[^1072]གྲགས་པའི་ཕྱིར་ཏེ། འཇིག་རྟེན་ན་ནི་འདུ་ཤེས་ཕྱིན་ཅི་ལོག །སེམས་ཕྱིན་ཅི་ལོག་ཅེས་གྲགས་ཀྱི་ཚོར་བ་ཕྱིན་ཅི་ལོག་ཅེས་ནི་མ་གྲགས་སོ། །

[Block 1487]
ཕྱིན་ཅི་ལོག་དེ་དག༌[^1073]ཐམས་ཅད་ཀྱང་། རྒྱུན་དུ་ཞུགས་པས་སྤང་བ༌[^1074]ཡིན་ཏེ། ལྟ་བ་མཚུངས་པར༌[^1075]ལྡན་པ་དང་བཅས་པ་རྣམས་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1488]
སྡེ་པ་གཞན་དག་ན་རེ་མི་རྟག་པ་ལ་རྟག་གོ་སྙམ་པའི༌[^1076]འདུ་ཤེས་དང་། སེམས་དང་། ལྟ་བ་ཕྱིན་ཅི་ལོག་གསུམ་ནས་དེ་བཞིན་དུ་བདག་མེད་པ་ལ་བདག་གོ་སྙམ་པའི་བར་གསུམ་སྟེ། ཕྱིན་ཅི་ལོག་ནི་བཅུ་གཉིས་ཡིན་ནོ། །

[Block 1489]
དེ་ལ་བརྒྱད་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1490]
སྡུག་བསྔལ་བ༌[^1077]དང་། མི་གཙང་བ་ལ་འདུ་ཤེས་དང་། སེམས་ཕྱིན་ཅི་ལོག་པ་བཞི་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 1491]
དེ་ལྟ་མ་ཡིན་ན་བདེ་བ་དང་། གཙང་བའི་འདུ་ཤེས་དག་མིད་པར༌[^1078]ཇི་ལྟར་ན། འཕགས་པ་འདོད་ཆགས་དང་མ་བྲལ་བ་ལ་འདོད་པའི་འདོད་ཆགས་སྐྱེས་པར༌[^1079]འགྱུར་ཞེས་ཟེར་རོ། །

[Block 1492]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་འདི་མི་འདོད་དེ་གལ་ཏེ་འཕགས་པ་ལ་བདེ་བ་དང་གཙང་བའི་འདུ་ཤེས་དང་། སེམས་ཀུན་དུ་འབྱུང་བ་དང་།[^1080] དེ་དག་གི་ཕྱིན་ཅི་ལོག་དག་ཏུ་འདོད་ན་ནི། སེམས་ཅན་གྱི་འདུ་ཤེས་དང་། སེམས་ཀུན་དུ་འབྱུང་བས་དེ་དག་གི་ཕྱིན་ཅི་ལོག་དག༌[^1081]ཏུ་ཡང་ཅིའི་ཕྱིར་མི་འདོད། བུད་མེད་དང་བདག་ལ་སེམས་ཅན་དུ་འདུ་ཤེས་པ༌[^1082]མེད་པར་མི༌[^1083]འདོད་པའི་འདོད་ཆགས་སྐྱེ་བར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1493]
མདོ་ལས་ཀྱང་འདི་ལྟར་འཕགས་པའི༌[^1084]ཉན་ཐོས་ཐོས༌[^1085]པ་དང་ལྡན་པ་འདི་ནི་སྡུག་བསྔལ་འཕགས་པའི་བདེན་པའོ་ཞེས་བྱ་བར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བ་ནས། དེའི་ཚེ་དེའི་མི་རྟག་པ་ལ་རྟག་གོ་སྙམ་དུ་འདུ་ཤེས་ཕྱིན་ཅི་ལོག་པ་དང་། སེམས་ཕྱིན་ཅི་ལོག་པ་དང་། ལྟ་བ་ཕྱིན་ཅི་ལོག་པ་གང་ཡིན་པ་དེ་སྤོང་བར་བྱེད་དོ༌[^1086]ཞེས་བྱ་བ་རྒྱས་པར་གསུངས་སོ། །

[Block 1494]
དེ་ལྟ་བས་ན་ལྟ་བས༌[^1087]ཀུན་ནས་བསླང་བའི་འདུ་ཤེས་དང་། སེམས་ཁོ་ན་ཕྱིན་ཅི་ལོག་ཡིན་གྱི་གཞན་དག་ནི་མ་ཡིན་ཏེ། དེའི་དུས་སུ་འཁྲུལ་པ་ཙམ་ཡིན་པའི་ཕྱིར་མགལ་མེའི་འཁོར་ལོ་དང་། རི་མོའི་གནོད་སྦྱིན་ལ་འཁྲུལ་པ༌[^1088]བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1495]
གཞན་དག་ན་རེ་འོ་ན་གནས་བརྟན་ཀུན་དགའ་བོས། འཕགས་པ་ངག་གི་དབང་ཕྱུག་གི་དབང་དུ་བྱས་ནས།

[Block 1496 [VERSE]]
འདུ་ཤེས་ཕྱིན་ཅི་ལོག་པ་ཡིས། །
ཁྱོད་ཀྱི་སེམས་ནི་ཡོངས་སུ་གདུང་། །

[Block 1497]
ཞེས་གང་སྨྲས་པ་ཇི་ལྟ་བུ། དེའི་ཕྱིར༌[^1089]སློབ་པས་འདུ་ཤེས་དང་། སེམས་ཕྱིན་ཅི་ལོག་བརྒྱད་པོ་ཐམས་ཅད་མ་སྤངས་པ་ཁོ་ནའོ། །

[Block 1498]
དེ་དག་ཀྱང་འཕགས་པའི་བདེན་པ་རྣམས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་ཤེས་པས་སྤང་བར༌[^1090]འགྱུར་གྱི། དེ་མེད་པར་ནི་མ་ཡིན་ནོ་ཞེས་ཐབས་ཡང་དག་པར་བསྟན་པ་ཡིན་པའི་ཕྱིར་མདོ་དང་འགལ་བ་མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 1499 [HEADING]]
### ང་རྒྱལ་གྱི་དབྱེ་བ། ^2-11-0

[Block 1500]
ཡང་ཇི་ལྟ་བའི་ཕྲ་རྒྱས་ཁོ་ན་ལ་དབྱེ་བ་ཡོད་ཀྱི་གཞན་ལ་མེད་དམ་ཞེ་ན། ང་རྒྱལ་ལ་ཡང་ཡོད་དེ། ཇི་ལྟ་ཞེ་ན། ང་རྒྱལ་བདུན། ཞེས་བྱ་བ་སྨོས་ཏེ། ང་རྒྱལ་དང་། ལྷག་པའི་ང་རྒྱལ་དང་། ང་རྒྱལ་ལས་ཀྱང་ང་རྒྱལ་དང་། ངའོ་སྙམ་པའི་ང་རྒྱལ་དང་། མངོན་པའི་ང་རྒྱལ་དང་། ཅུང་ཟད་སྙམ་པའི་ང་རྒྱལ་དང་། ལོག་པའི་ང་རྒྱལ་ལོ། །

[Block 1501]
བྱེ་བྲག་མེད་པར་སེམས་ཁེངས་པ་ལ་ང་རྒྱལ་ཞེས་བཤད་དོ། །

[Block 1502 [HEADING]]
#### ང་རྒྱལ་རྣམ་པ་བདུན། ^2-11-1-0

[Block 1503]
དེ་ལ༌[^1091]འཇུག་པའི་བྱེ་བྲག་ལས་ནི་རྣམ་པ་བདུན་ཡིན་ཏེ། ཆུང་ངུ་བས་བདག་ཁྱད་པར་དུ་འཕགས་པའམ། མཉམ་པ་དང་མཉམ་མོ་སྙམ་དུ་སེམས༌[^1092]ཁེངས་པ་ནི་ང་རྒྱལ་ལོ། །

[Block 1504]
མཉམ་པ་བས་བདག་ཁྱད་པར་དུ་འཕགས་སོ་སྙམ་པ༌[^1093]ནི་ལྷག་པའི་ང་རྒྱལ་ལོ། །

[Block 1505]
ཁྱད་པར་དུ་འཕགས་པ་བས་ཀྱང་བདག་ཁྱད་པར་དུ་འཕགས་སོ་སྙམ་པ་ནི་ང་རྒྱལ་ལས་ཀྱང་ང་རྒྱལ་ལོ། །

[Block 1506]
ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་ལ་བདག་གམ་བདག་གིས༌[^1094]སེམས་པ་ནི་ངའོ་སྙམ་པའི་ང་རྒྱལ་ལོ། །

[Block 1507]
ཁྱད་པར་ཐོབ་པར་བྱ་བ་མ་ཐོབ་པར་བདག་གིས་ཐོབ་བོ་སྙམ་པ་ནི་མངོན་པའི་ང་རྒྱལ་ལོ། །

[Block 1508]
ཆེས་ཁྱད་པར་དུ་འཕགས་པ་བས་བདག་ཅུང་ཟད་ཅིག་གིས་དམན་ནོ་སྙམ་པ་ནི་ཅུང་ཟད་སྙམ་པའི་ང་རྒྱལ་ལོ། །

[Block 1509]
ཡོན་ཏན་མ་ཡིན་པ་དང་ལྡན་པ་ལ་བདག་ཡོན་ཏན་དང་ལྡན་ནོ་སྙམ་པ་ནི་ལོག་པའི་ང་རྒྱལ་ལོ། །

[Block 1510 [HEADING]]
#### ང་རྒྱལ་གྱི་རྣམ་པ་དགུ། ^2-11-2-0
--- END BLOCKS ---
