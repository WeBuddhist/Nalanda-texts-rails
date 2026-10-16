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
དོན་དེ་ཉིད་ཀྱང་རང་གི་མཚན་ཉིད་ཡིན་ནོ་ཞེས་བརྗོད་པར་མི་ནུས་ཏེ། མ་ཐོབ་པ་དང་འགགས་པའི་དོན་དག་ཀྱང་དེ་དང་མ་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1472]
དངོས་པོ་ལ་ཕྱིན་ཅི་ལོག་པའི་རྣམ་པ་ལ་མངོན་པར་ཞེན་པ་ཅན་གྱི་གཞན་མུ་སྟེགས་པའི་ཤེས་པ་དག་ལ་ཡང་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1473 [VERSE]]
དོན་དམ་ལ་གཅིག་ཕྱོགས་ཉིད་ཡོད། །
མཐོང་བའི་བྱེ་བྲག་ཐ་དད་པའི། །
དོན་རྣམས་ལ་ནི་སྒྲ་རྣམས་ཀྱིས། །
རྒྱུ་མེད་ཅན་འཇུག་མི་འགྱུར་དང་། །

[Block 1474 [VERSE]]
འདས་དང་མ་སྐྱེས་པ་ལ་ཡང་། །
ཚིག་འགའ་ཞིག་ཀྱང་བརྫུན་པ་ཡི། །
དོན་ཅན་ཉིད་དུ་མི་འགྱུར་ཕྱིར། །
དེ་དག་བློ་དོན་ཡུལ་ཅན་འདོད། །

[Block 1475]
ཅེས་བྱ་བ་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 1476]
དེ་ནི་ཇི་ལྟར་འདོད་པའི་ངོ་བོ་ཉེ་བར་ལེན་པ་མེད་པ་ཅན་བསྒྲུབ་པར་བྱ་བ་ལ། དེ་ལྟར་འདི་ལ་མི་དམིགས་པའི་ཆོས་ཡོད་པའི་ཕྱིར། བསྒྲུབ་པར་བྱ་བའི་ཆོས་མ་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 1477]
འདི་ལ་ཡང་སྒྲ་ལས་སྣང་བའི་དོན་འདི་ཉིད་ནི་བསྙོན་པར་ནུས་པ་མ་ཡིན་ཏེ། དེ་ནི་བློ་ལ་བསྐྱེད་པའི་ཕྱིར་སྒྲ་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 1478]
དེ་མེད་ན་ནི༌[^1102]མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1479]
གཞན་ཡང་།

[Block 1480 [VERSE]]
སྒྲ་དོན་བསྙོན་ན་བསྒྲུབ་བྱ་བའི། །
ཆོས་ཀྱི་རྟེན༌[^1103]ནི་བརྩལ་བའི་ཕྱིར། །
བསྡུས་པ་བསྒྲུབ་བྱར་མི་འགྱུར་ཞིང་། །
ཡན་འགར་ཆོས་ནི་གྲུབ་པ་ཡིན། །

[Block 1481]
གལ་ཏེ་སྒྲའི་དོན་ཁོ་ན་ལ་བསྙོན་ན་གཙོ་བོའི་སྒྲའི་བརྗོད་པར་བྱ་བ་ཆོས་ཅན་ཉིད་ལ་བརྩལ་བའི་ཕྱིར། བསྒྲུབ་པར་བྱ་བའི་ཆོས་ཀྱི་རྟེན༌[^1104]མེད་པར་འགྱུར་རོ། །

[Block 1482]
དེ་བས་ན་འདི་ནི་རྟེན་རྣམ་པར་གཅོད༌[^1105]ལ་ལྟོས་པ་མེད་པ་ཅན་རྩོད་པའི་གཞི་མ་ཡིན་པའི་ཕྱིར་ཉེ་བར་དགོད་པར་བྱ་བ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 1483]
གཞན་ཡང་།

[Block 1484 [VERSE]]
སྒྲ་དོན་བསྙོན་པ་མེད་རྣམས་ཀྱིས། །
ཡོད་མེད་ཕྱོགས་ཀྱི་བྱེ་བྲག་གིས། །
དངོས་པོ་ཉིད་ནི་དཔྱད་བྱ་སྟེ། །
འདི་ལ་འབྲས་འབྱུང་རག་ལས་ཕྱིར། །
དོན་བྱེད་ནུས་པ་མ་ཡིན་ཕྱིར།

[Block 1485]
[^1106] །དེ་འདོད་བརྟགས་པས་ཅི་ཞིག་བྱ། །མ་ནིང་གཟུགས་བཟང་མི་བཟང་ཞིང་།[^1107] །འདོད་ལྡན་རྣམས་ཀྱིས་བརྟགས་ཅི་ཕན། །སྒྲའི་དོན་ཡོད་པ་འམ་མེད་པ་ནི་སྐྱེས་བུའི་དོན་ཅུང་ཟད་ཀྱང་ཉེ་བར་འགོག་པའམ། །ཡང་དག་པར་བྱེད་པ་མ་ཡིན་ཏེ། མངོན་པར་ཞེན་པ་ཇི་ལྟ་བ་བཞིན་དུ་དེ་ཁོ་ན་ཉིད་དུ་མེད་པའི་ཕྱིར་དང་། དེ་ཁོ་ན་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་མི་གནས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1486]
དེ་བས་ན་འདི་འཇུག་པ་ན་ཐམས་ཅད་དུ་ཡོད་པ་དང་མེད་པ་དཔྱོད་པ་ན་རྣམ་པར་རྟོག་པའི་སྣང་བ་ལ་ལྟོས་པ་མེད་པར་གང་ལ་སྐྱེས་བུའི་དོན་འདི་རག་ལུས་པའི་དངོས་པོ་ཉིད་ལ་དམིགས་པར་བྱེད་དེ་དཔེར་ན་མེ་ནི་གྲང་བ་ཟློག༌[^1108]པར་བྱེད་པ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1487]
འདི་ལ་སྒྲའི་དོན་ནི་ནུས་པ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ཉམས་སུ་མྱོང་བར་གྱུར་པ་ཡིན་དུ་ཟིན་ཀྱང་དེ་མེད་པའི་ཕྱིར་རོ། །

[Block 1488]
དེ་བས་ན་དོན་བྱེད་པར་འདོད་པ་འདི་ནི་མི་ནུས་པ་ལ་གུས་པས་རྗེས་སུ་སྦྱོར་བར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1489]
འདོད་ལྡན་རྣམས་ཀྱིས་མ་ནིང་གཟུགས་བཟང་བ་དང་མི་བཟང་བ་བརྟག་པ༌[^1109]ལ་གུས་པར་མི་འགྱུར་རོ། །

[Block 1490]
གང་ཡང་ཇི་སྐད༌[^1110]དུ་བརྟགས་པ་མི་དམིགས་པ་ཆོས་ཞེས་བཤད་པ་དེའི་དོན་གང་ཡིན་ཞེ་ན།

[Block 1491 [VERSE]]
རྟོག་པའི་ཤེས་པའི་ཡུལ་ཉིད་ཀྱིས། །
སྒྲ་ཡི་དོན་ནི་བརྟགས་པ་ཡིན། །
དངོས་བརྟེན་མ་གྲུབ་འདི་ཆོས་སུ། །
རིགས་པ་སྨྲ་བས་བཤད་པ་ཡིན། །

[Block 1492]
རྟོག་པའི༌[^1111]ཡུལ་ཉིད་ཡིན་པའི་ཕྱིར་སྒྲའི་དོན་ཉིད་བརྟགས་པ་ཡིན་ལ། དེ་ནི་དངོས་པོ་ལ་བརྟེན་པ་མི་དམིགས་པ་ནི་ཆོས་ཡིན་ནོ་ཞེས་བྱ་བར་དགོངས་སོ། །

[Block 1493]
ཚད་མ་གསུམ་ལོག་ཏུ་ཟིན་ཀྱང་དངོས་པོ་མེད་པར་འགྲུབ་པ་མ་ཡིན་ནོ་ཞེས་བཤད་པ་གང་ཡིན་པ་དེ་ཚད་མ་གཞན་ལོག་པ་ན་ལྡོག་པར་མི་འགྱུར་ཏེ། དེ་དག་ནི་མ་ལུས་པའི་ཡུལ་ཅན་ཉིད་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1494]
འདི་ལ་ལུང་གིས་ནི་ཅུང་ཞིག་ཀྱང་མ་ཁྱབ་པ་མེད་དེ། དེ་ལ་ལོག་པ་ཇི་ལྟར་གོ་བར་བྱེད་པ་མ་ཡིན་ཞེ་ན། འདི་ལ་ལུང་དག་ཏུ་དོན་ཐམས་ཅད་ཉེ་བར་སྦྱོར་བ༌[^1112]མེད་པར་ནི་བཤད་ཟིན་ཏེ། སྐབས་སུ་བབ་པ་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1495]
གཞན་ཡང་།

[Block 1496 [VERSE]]
སྒྲ་རྣམས་དངོས་དང་ལྷན་ཅིག་ཏུ། །
མེད་ན་མི་འབྱུང་ཉིད་མེད་ཕྱིར། །
དེ་ལས་དོན་གྲུབ་མིན་དེ་དག །
སྨྲ་བའི་བསམ་པ་སྟོན་པར་བྱེད། །

[Block 1497]
སྒྲ་ནི་དངོས་པོ་ཇི་ལྟ་བ་བཞིན་དུ་འཇུག་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་དེ་དག་ལས་དོན་གྱི་རང་བཞིན་ངེས་པར་འགྱུར་ན། དེ་དག་ནི་སྨྲ་བ་པོ་བརྗོད་པར་འདོད་པ༌[^1113]ལ་རག་ལུས་པས་འཇུག་པ་ཅན་དག་ཡིན་པའི་ཕྱིར། དེ་མེད་ན་མི་འབྱུང་བ་ཡིན་པས་དེ་ཉིད་ཀྱིས་གོ་བར་བྱེད་པ་ཡིན་པར༌[^1114]འགྱུར་རོ། །

[Block 1498]
སྐྱེས་བུའི་འདོད་པ་ཐམས་ཅད་ཀྱང་དོན་ཇི་ལྟ་བ་བཞིན་དུ་འགྱུར་བ་ཅན་མ་ཡིན་ལ། དེ་ལ་རག་ལུས་པ་མེད་པའི་རང་བཞིན་ཅན་གྱི་དངོས་པོ་ནི་གཞན་གོ་བར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1499]
འོན་ཀྱང་གང་།

[Block 1500 [HEADING]]
## ལུང་རྗེས་སུ་དཔག་པ་ཉིད། ^6-0

[Block 1501 [VERSE]]
ཡིད་ཆེས་ཚིག་ནི་མི་སླུ་བ། །
སྤྱི་ལ་རྗེས་སུ་དཔག་པ་ཉིད། །

[Block 1502]
ཅེས་ལུང་རྗེས་སུ་དཔག་པ་ཉིད་དུ་གསུངས་པ་དེ་ཇི་ལྟར་ཡིན་ཞེ་ན། སྐྱེས་བུ་འདི་ནི་ལུང་གི་ཚད་མ་ལ་མ་བརྟེན་པར་གཞག་པར་ནུས་པ་མ་ཡིན་ཏེ། འབྲས་བུ་མངོན་སུམ་དུ་གྱུར་པ་མ་ཡིན་པ་ཅན་ལ་ལ་དག་གི་འཇུག་པ་དང་། ལྡོག་པའི་ཕན་ཡོན་ཆེན་པོ་དང་། ངན་སོང་དག་ཐོས་པའི་ཕྱིར་དང་། དེ་ཡོད་པ་ལ་འགལ་བ༌[^1115]མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1503]
དེ་བས་ན་འཇུག་པར་བྱ་བ་ཡོད༌[^1116]ན་འདི་ལྟར་འཇུག་པ་ཡིན་པའི་ཕྱིར་བརྟགས་ནས་ཚད་མར་གསུངས་སོ། །

[Block 1504]
དེ་ཡང་།

[Block 1505 [VERSE]]
འབྲེལ་པ་དང་ནི་རྗེས་མཐུན་ཐབས། །
སྐྱེས་བུའི་དོན་ནི་རྗོད་བྱེད་ངག །
ཡོངས་སུ་བརྟགས་པ་དབང་བྱས་ཡིན། །
དེ་ལས་གཞན་པ་དབང་བྱས་མིན། །

[Block 1506]
འབྲེལ་པ་ནི་ངག་རྣམས་དོན་གཅིག་ཏུ་སྡུག་པ༌[^1117]ལ་ཕན་འདོགས་པར་བྱེད་པའོ། །

[Block 1507]
དེ་ལྟར་མ་ཡིན་ན་སྨྲ་བ་པོ༌[^1118]མི་མཐུན་པ་སྟོན་པར་འགྱུར་ཏེ། སེའུ་བཅུ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ངག་དང་འདྲ་བར་བསྡུར་མེད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1508]
འབྲས་བུ་འདོད་པ་བསྟན་བཅོས་ཐབས་ནུས་པ་མེད་པ་ཅན་གྱི་འབྲས་བུ་ཅན་ལ་དཔྱོད་པར་བྱ་བའི་ཕྱིར་གུས་པར་མི་འགྱུར་ཞིང་། སྐྱེས་བུ་དོན་གྱི་འབྲས་བུ་མེད་པ་ཅན་དག་ལ་ཡང་སྟེ། དུག་ཞི་བར་བྱ་བའི་ཕྱིར་འཇོག་པའི་གཙུག་གི་རིན་པོ་ཆེའི་རྒྱན་གྱི་མན་ངག་ལྟ་བུ་དང་། བྱ་རོག་གི་སོ་ལ་བརྟགས༌[^1119]པ་ལྟ་བུའོ། །

[Block 1509]
དེ་བཟློག་ནས་སྡུད་པ་དང་ལྡན་པ་དང་ཐབས་ནུས་པ་ཅན་དང་། སྐྱེས་བུའི་དོན་རྗོད་པར་བྱེད་པའི་བསྟན་བཅོས་ནི་ཡོངས་སུ་བརྟག་པར་བྱ་བ་ཡིན་ཏེ། གཞན་ལ་གུས་པར་བྱ་བ་ཉིད་ནི་མི་རིགས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1510]
དེ་ནི་གལ་ཏེ་ཡོངས་སུ་བརྟགས་པ་ལ་སླུ་བ་བསྟན་པ༌[^1120]མེད་པ་དེ༌[^1121]ལ་འཇུག་པ་ན་མཛེས་པར་འགྱུར་རོ། །
--- END BLOCKS ---
