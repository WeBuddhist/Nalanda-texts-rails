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
དེ་ཡང་།

[Block 1472 [VERSE]]
[^1035]རྨོངས་པ་གང་གིས་འཆིང་བ་ནི། །
མཁས་པ་དེས་ནི་རབ་ཏུ་གྲོལ། །
དེ་ལྟར་བྱང་ཆུབ་བསྒོམ་པའི༌[^1036]ཕྱིར། །
ཐབས་འདི་ཐམས་ཅད་ལོག་པ་ཡིན། །

[Block 1473]
ཞེས་འབྱུང་ངོ་། །

[Block 1474 [VERSE]]
གང་དང་གང་གིས་སྐྱེ་བོ་རྣམས། །
མི་བཟད་ལས་ཀྱིས་འཆིང་འགྱུར་བ། །
ཐབས་དང་བཅས་པ་དེ་ཉིད་ཀྱིས། །
སྲིད་པའི་འཆིང་བ་ལས་གྲོལ༌[^1037]འགྱུར། །

[Block 1475]
ཞེས་འབྱུང་ངོ་། །འོད་སྲུངས་འདི་ལྟ་སྟེ། བུ་རམ་གྱི་ཤིང་དང་འབྲས་ཀྱི་ཞིང་རྣམས་ལ་ལུད་ཀྱི་ཕུང་པོ་ཕན་པར་གྱུར་པ་དེ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ལ་ཡང་ཉོན་མོངས་པ་ཁོ་ན་ཕན་པར་འགྱུར་ཞེས་གསུངས་པས་སོ། །

[Block 1476]
དེའི་ཕྱིར་སྔགས་ཀྱི་ཐེག་པ་ལ་སྣོད་དུ་གྱུར་པའི་རྣལ༌[^1038]འབྱོར་པ་རྣམས་ནི་དབང་པོ་རྣོ་བ་ཡིན་ནོ། །

[Block 1477]
ཐེག་པ་ཆེན་པོ་པ་དེ་དག་ཀྱང་འདིར་རྗེས་སུ་གཟུང་བར་བྱ་བ་ཡིན་པ་དང་། སྔགས་ཀྱི་ཐེག་པ་ཆེན་པོའི་སྣོད་དུ་རུང་བ་ཡིན་ཏེ། འབྲས་བུ་ལ་དབྱེར་མེད་པའི་ཕྱིར་རོ། །

[Block 1478]
ཇི་སྐད་དུ།

[Block 1479 [VERSE]]
དགའ་བ་མི་ཟད་འོད་གསལ་ཞིང་། །
སྣ་ཚོགས་གཟུགས་ཅན་མི་རྟོག༌[^1039]པ། །
སྙིང་རྗེ་ཆེན་པོའི་རོས་ཁྱབ་པ། །
ཆོས་དབྱིངས་བདག་ཉིད་འབྲས་བུ་ཡིན། །

[Block 1480]
ཞེས་གསུངས་སོ། །

[Block 1481]
རེ་ཞིག་ཐེག་པ་ཆེན་པོ༌[^1040]འདི་བཞག༌[^1041]ན་གསུམ་པོ་དག་ཀྱང་སྔགས་ཀྱི་ཐེག་པ་ཆེན་པོའི་སྣོད་དུ་རུང་བར་འགྱུར་རོ། །

[Block 1482]
གང་གི༌[^1042]ཚེ་དེ་རྣམས་བཅོམ་ལྡན་འདས་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་རྣམས་ཀྱི་འོད་ཟེར་གྱི་འཁོར་ལོས༌[^1043]བསྐུལ་བ་དེའི་ཚེ། དོན་དམ་པའི་བློ་ཡང་དག་པར་བསྐྱེད་པས༌[^1044]མི་རྟོག་པའི༌[^1045]ཏིང་ངེ་འཛིན་མངོན་དུ་བྱས་ནས། །དེ་ཁོ་ན་ཉིད་ལ་འཇུག་ཅིང་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཉིད་དུ་འགྱུར་རོ། །

[Block 1483]
འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོས་དབང་བསྐུར་བས་ཐ་མལ་པའི་རྒྱལ་པོ་རྒྱལ་པོ༌[^1046]ཆེན་པོར་འགྱུར་བ་བཞིན་ནོ། །

[Block 1484]
གཞན་ཡང་ཉན་ཐོས་ལ་སོགས་པ་དེ་རྣམས་སངས་རྒྱས་ཀྱི་སྣོད་ཡིན་ཞེས་ངོ་མཚར་མེད་དེ། དེ་ནི་རང་གི་ཚོགས་པ་དང་བཅོམ་ལྡན་འདས་ཀྱི་ལམ་ལ་གནས་པའི་ཕྱིར་སྔགས་ཀྱི་ཐེག་པ་ཆེན་པོ་ལ་བརྟེན་ཏེ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 1485]
རྒྱང་པན་པ་ལ་སོགས་པ་གཞན་གྱི་ཚོགས་པ་རྣམས་དེ་དག་ཀྱང་བསྟན་པ་འདི་ལ་བརྟེན་ཏེ་དངོས་གྲུབ་ཐོབ་པའོ། །

[Block 1486]
ཇི་སྐད་དུ།

[Block 1487 [VERSE]]
ཕ་རོལ་སྨྲ་བ་གང་དག་ནི། །
རྟགས་ཀྱི་དབྱེ་བས་རྣམ་པར་གནས། །
རྡོ་རྗེ་སེམས་དཔའི༌[^1047]སྤྲུལ་པས་སོ། །

[Block 1488]
ཞེས་འབྱུང་ངོ་། །

[Block 1489]
ཚད་མའི་ལམ་ལ་གནས་པ་མཁས་པ་དེ་དག་རེ་ཞིག་ཚད་མས་གྲུབ་པའི་བསྟན་བཅོས་ཐོས་པ་ཙམ་གྱིས་ལམ་འདིར༌[^1048]འཇུག་པར་འདོད་པ་དེ་དག་གཞན༌[^1049]ན། འོན་ཀྱང་ཤིན་ཏུ་གདུག་པ་དང་རྐུ་བ་དང་གཡེམ་པའི་ཆོས་ཅན་དང་མཚམས་མེད་པའི་ལས་བྱེད་པ་དེ་རྣམས་ཀྱང་སྔགས་ཀྱི་ཐེག་པ་ཆེན་པོ་ལ་བརྟེན་ཏེ། དངོས་གྲུབ་ལྷག་པར་ཐོབ་པའོ། །

[Block 1490]
ཇི་སྐད་དུ། རིགས་ངན་སྨྱུག་མ་མཁན་ལ་སོགས།

[Block 1491 [VERSE]]
གསོད་པས་ནོར་ནི་དོན་གཉེར་བ། །
དེ་ཡང་ཐེག་པ་མཆོག་འདི་ལ། །
བླ་མེད་དངོས་གྲུབ་ཐོབ་པར་འགྱུར། །
མཚམས་མེད་ལ་སོགས་ལས་བྱེད་རྣམས། །

[Block 1492 [VERSE]]
ཤིན་ཏུ་སྡིག་ཅན་སེམས་ཅན་རྣམས། །
དེ་ཡང་ཐེག་པ་བླ་མེད་འདི། །
འགྲུབ་པར་འགྱུར་ཏེ་ཐེ་ཚོམ་མེད། །

[Block 1493]
ཅེས་འབྱུང་ངོ་། །དེ་ལྟར་འདི་སྐྱོན་ཐམས་ཅད་ལས་ངེས་པར་གྲོལ་བ། ཡོན་ཏན་ཐམས་ཅད་ཀྱིས་བརྒྱན་པ། ཟབ་པ་དང་རྒྱ་ཆེ་བ་རྡོ་རྗེ་ཐེག་པ་ཆེན་པོ་འདི་ཡིན་ནོ། །

[Block 1494]
དེ་ལ་རྣམ་པ་ལྔ་སྟེ། བྱ་བ་དང་། སྤྱོད་པ་དང་། རྣལ་འབྱོར་དང་། རྣལ་འབྱོར་ཆེན་པོ༌[^1050]དང་། [^1051]རྣལ་འབྱོར་ཆེན་པོའི་མཐར་ཐུག༌[^1052]པའི་བྱེ་བྲག་གིས༌[^1053]དེ་རྣམས་ཀྱི་རང་རང༌[^1054]གི་མཚན་ཉིད་དང་། དབང་པོའི་དངོས་པོ་དང་། ཡུལ་གྱི་བྱེ་བྲག་སྔོན་དུ་བཤད་ཟིན་ཏོ། །

[Block 1495]
དེ་རྣམས་ཀྱི༌[^1055]རིམ་པ་གཉིས་འདི་ལྟར་ཡིན་ཏེ། དེ་ལ་བྱ་བའི་རྒྱུད་ཀྱི༌[^1056]རྣལ་འབྱོར་པ་རྣམས་ཀྱི༌[^1057]བསྐྱེད་པའི་རིམ་པ་ནི་དང་པོའི་ཡི་གེ་ཙམ་ཡོངས་སུ་གྱུར་པས་སོ། །

[Block 1496]
རྫོགས་པའི་རིམ་པ་ཡང་མཛོད་སྤུ་ལས་བྱུང་བའི་འོད་ཟེར་གྱི་འཁོར་ལོས་སྤྲོ་བ་དང་། བསྡུ་བའི་རིམ་པས་སོ། །

[Block 1497]
སྤྱོད་པ་དང་རྣལ་འབྱོར་གྱི་རྒྱུད་ཀྱི་རྣལ་འབྱོར་པ་རྣམས་ཀྱི་བསྐྱེད་པའི་རིམ་པ་ནི༌[^1058]མངོན་པར་བྱང་ཆུབ་པའི༌[^1059]རྣམ་པ་ལྔའི་རིམ་པས་སོ། །

[Block 1498]
རྫོགས་པའི་རིམ་པ་ནི་ཕྲ་བའི་རྡོ་རྗེ་ལ་སོགས་པའི་བསྒོམ་པའི༌[^1060]རིམ་པས་སོ། །

[Block 1499]
རྣལ་འབྱོར་པ་ཆེན་པོ་པ་རྣམས་ཀྱི་བསྐྱེད་པའི་རིམ་པ་ནི་རྣལ་འབྱོར་བཞི་དང་ལྡན་པའི་དང་པོ་སྦྱོར་བ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་གྱི་རིམ་པའམ་རྡོ་རྗེ་བཞི་པས་སོ། །

[Block 1500]
རྫོགས་པའི་རིམ་པ་ནི་བསྒོམ་པ༌[^1061]དུ་མ་སྟེ། དཔེར་ན་ཕྲ་མོའི་རྣལ་འབྱོར་ནི་སོ་སོར་སྣང་བ་ཙམ་གྱི་རང་བཞིན་ནི༌[^1062]ཤེལ་དག་པ་ལྟ་བུའི་རྣམ་པ་འོད་ཟེར་གྱི་སྦྱོར་བས་སོ། །

[Block 1501]
ཐིག་ལེའི་རྣལ་འབྱོར་ནི་སྣ་གསུམ་གྱི་རྩེ་མོར་དགོད་པའི་ཁམས་གསུམ་མ་ལུས་པའི་ངོ་བོ་ཕྲ་ཞིང་དང་བའི་ཐིག་ལེ་ཙམ་བསྒོམ་པའི་རིམ་པས་སོ། །

[Block 1502]
ཡང་ན་རྩའི་ཀུན་ཏུ་རྒྱུ་བས་བྱང་ཆུབ་ཀྱི་སེམས་ཡོངས་སུ་གཡོ་བས་སོ། །

[Block 1503]
ཡང་ན་པདྨའི་ནང་དུ་དམ་ཚིག་གི་དཀྱིལ་འཁོར་བསྒོམ་པའི་རིམ་པས་སོ། །

[Block 1504]
ཡང་ན་རྩ་ཐམས་ཅད་ཀྱི་ཁུང་བུ་ནས་འཕོ་བའི་བྱང་ཆུབ༌[^1063]སེམས་ཀྱི་སྟེང་དུ་བཟློག་པར་འགྱུར་བས་བདེ་བ་ཆེན་པོའི༌[^1064]ཉམས་སུ་མྱོང་བའི་ཏིང་ངེ་འཛིན་གྱིས་སོ། །

[Block 1505]
རྡོ་རྗེ་ནོར་བུའི་ནང་དུ་ཆུད་པའི་ཐིག་ལེ་ཧཱུཾ་ཕཊ་ལ་སོགས་པའི་ས་བོན་སྔོན་དུ༌[^1065]འགྲོ་བས༌[^1066]འཛིན་པའམ་སྙོམས་པར་ཞུགས་པའི་དུས་སུ་དེ་བཞིན་གཤེགས་པ་རྣམས་འཇུག་པས་རོ་གཅིག་པར༌[^1067]བྱེད་པའི་རྣལ་འབྱོར་གྱིས་སམ། དེ་ལས་མ་ལྷུང་བའི་བྱང་ཆུབ་ཀྱི་སེམས་དེ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་འདུས་པའི་བློས་ལྕེས་ཡང་དག་པར་མྱོང་བའི་རིམ་པས་སམ། ཡུལ་དང་དབང་པོ་ཕྲད་པ་དང་དེའི་རྣམ་པར་དག་པ་དང་བྱང་ཆུབ་ཀྱི་སེམས་དེ་སྤྲོ་བ་དང་དེ་འཛིན་པ་དང་། ནམ་མཁའི་གཏོས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་ཡོངས་སུ་གང་བ་དང་། ཐམས་ཅད་ཡོངས་སུ་སྡུད་པས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཕྱག་རྒྱ་ཆེན་པོ་བསྒོམ་པའི་རིམ་པ་ཞེས་བྱ་བ་ཡན་ལག་དྲུག་གི་རིམ་པས་སོ། །

[Block 1506]
ཡང་ན་རིམ་པ་ལྔ་སྟེ་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་ནི་ངག་རྣམ་པར་དག་པའི་ཕྱིར་རོ། །

[Block 1507]
སེམས་རྣམ་པར་དག་པ་ནི་སེམས་ལ་དམིགས་པའི་རིམ་པས་སོ། །

[Block 1508]
ཀུན་རྫོབ་ཀྱི་བདེན་པ་རྣམ་པར་དག་པ་ནི་རང་བྱིན་གྱིས་རློབ་པས་སོ། །

[Block 1509]
དོན་དམ་པའི་བདེན་པ་རྣམ་པར་དག་པ་ནི་མངོན་པར་བྱང་ཆུབ་པས་སོ། །

[Block 1510]
མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་སུ་འཇུག་པ་ནི༌[^1068]ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་གྱི་རིམ་པས་སོ། །
--- END BLOCKS ---
