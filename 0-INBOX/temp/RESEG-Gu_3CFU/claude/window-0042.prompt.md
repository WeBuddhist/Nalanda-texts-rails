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
དེ་ལྟར་ན་ཡང་དུད་འགྲོའི་སྐྱེ་གནས་སུ་གཏོགས་པའི་མ་གསོད་པར༌[^1045]བྱེད་པ་ལ་རབ་ཏུ་དབྱུང་བ་བཀག་པར་འགྱུར་རོ། །

[Block 1472]
སྐྱེས་པས་དགེ་སློང་མ་ལ་ཇི་ཞིག་བྱས་ན་དགེ་སློང་མ་སུན་ཕྱུང་བར་འགྱུར་ཞིང་བུད་མེད་ཀྱིས་ཀྱང་དགེ་སློང་ལ་ཇི་ཞིག་བྱས་ན་སུན་ཕྱུང་བར་འགྱུར་ཅིའི་ཕྱིར་དེ་གཉིས་སུ་བསྟན་ཞེ་ན། དེའི་ཕྱིར་ཕམ་པར་གྱུར་པ་མ་བྱུང་བ་ཉིད་ལ་མི་ཚངས་པར་སྤྱོད་པས་ཉམས་སུ་མྱོང་བ་དག་སུན་ཕྱུང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1473]
འདིར་གཞུང་ནི་བཙུན་པ་ཇི་ཙམ་གྱིས་ན་དགེ་སློང་མ་སུན་ཕྱུང་བ་ཞེས་བགྱི། ཉེ་བ་འཁོར་གང་གིས་མི་ཚངས་པར་སྤྱད་པས་དགེ་སློང་མ་སུན་ཕྱུང་བར་གྱུར་ནའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1474]
ཅི་སེམས་གང་ཡང་རུང་བའི་སེམས་དག་ལ་འདི་འབྱུང་བར་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་ཉམས་སུ་མྱོང་བ་དག་ལ་ཞེས་བྱ་བ་སྨོས་ཏེ། བགྲོད་པར་བྱ་བ་ཡང་སུན་ཕྱུང་བར་འགྱུར་ལ་བགྲོད་པ༌[^1046]པོ་ལ་ཡང་སུན་ཕྱུང་བར་འགྱུར་བ་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུ་འདིར་གཉིས་པའི་ཚིག་གོ། །

[Block 1475]
བརྗོད་པ་དང་བཅས་པའི་ཟླས་ཉམས་སུ་མྱོང་བས་སུན་ཕྱུང་བ༌[^1047]ཉིད་མི་འགྱུར་བ་ཞེས་བྱ་བ་འདི་ལ་འདིར་ཟླས་ཉམས་སུ་མྱོང་བ་ཡན་ལག་མ་ཡིན་པ་ཉིད་དེ་གང་གི་ཕྱིར་གཞན་གྱི་ཉེས་པས་གཞན་ལ་མི་གོས་པའི་ཕྱིར་རོ། །

[Block 1476]
འདོད་ཆགས་དང་བྲལ་བ་སུན་ཕྱུང་བ་ལ་ཡང་སུན་འབྱིན་པ་ཉིད་མི་འགྱུར་བར་ཐལ་བའི་ཕྱིར་རོ། །

[Block 1477]
འདུན་པ་ཞེས་བྱ་བའི་ཚིག་གང་ཡིན་པ་དེ་ནི་འདིར་ལུང་སྟེ། རང་གི་འདོད་པས་ཞེས་བྱ་བ་འདིའི་དོན་ཏོ། །

[Block 1478]
ཅི་ཕམ་པར་གྱུར་པ་བྱུང་བའི་ཡུལ་ལ་ཡང་དགེ་སློང་དང་དགེ་སློང་མ་ཉིད་ཡོད་དམ་གནས་སྐབས་དེ་དང་ལྡན་པ་འདི་དག་ལ་ཡང་སུན་འབྱིན་པར་བགྱིད་ན་སུན་ཕྱུང་བ་ཉིད་དུ་འགྱུར་རམ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་ཕམ་པར་གྱུར་པ་མ་བྱུང་བ་ཉིད་ལ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1479]
འདིར་གཞུང་ནི། བཙུན་པ་རེ་ཞིག་གང་ཟག་བརྒྱད་ཀྱིས་དགེ་སློང་མ་གཅིག༌[^1048]ལ་དངོས་པོ་བརྒྱད་པོ་རེ་རེས་སུན་འབྱིན་པར་བགྱིད་ན་དགེ་སློང་མ་དེ་སུན་ཕྱུང་བ་ཞེས་བགྱིའམ། ཉེ་བ་འཁོར་སུན་ཕྱུང་བ་ཞེས་བྱའོ། །

[Block 1480]
གང་ཟག་དེ་རྣམས་ལས་དུ་ཞིག་གིས་དགེ་སློང་མ་སུན་ཕྱུང་བ་ཞེས་བགྱི། བཀའ་སྩལ་པ། ཉེ་བ་འཁོར་འགའ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 1481]
དེ་ནི་རེག་པ་དང་ལུས་བཀན་པ་དག་གིས་དགེ་སློང་མ་ལ་ཕམ་པར་མི་འགྱུར་བ་ཞེས་བྱ་བ་འདི་ནི་སུན་ཕྱུང་བ་ཉིད་དུ་རྣམ་པར་གཞག་པར་མི་སྣང་ངོ་། །ཇི་ལྟར་ཞེ་ན། དེ་ལ་ཡང་སྐྱེ་བ་དོན་གཞན་གྱིས་རེག་པ་དང་། ལུས་བཀན་པ་ལ་ཁས་མི་ལེན་པ་དང་། ནོམ་པ་དང་ཉུག་པ་ལ་ཡང་དག་པར་ཞུགས་པའོ། །

[Block 1482]
རེག་ནས་ཀྱང་ཁས་མ་བླངས་པ་ལ་དེས་རེག་པ་ལའོ། །

[Block 1483]
སྐྱེས་པའི་ལུས་ལ་རང་གིས་རེག་ཅིང་སྐྱེས་པ་དང་ཉེ་བར་གྱུར་པ་ལའོ། །

[Block 1484]
བུད་མེད་བསླབ་པ་ཕུལ་ནས་སྐྱེས་པ་ཉིད་དུ་གྱུར་པ་ནི་རབ་ཏུ་དབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་རུང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་བུད་མེད་བསླབ་པ་ཕུལ་ནས་ཉམས་པར་གྱུར་པ་མཚན་གྱུར་ནས་སྐྱེས་པ་ཉིད་དུ་གྱུར་པ་ནི་རབ་ཏུ་དབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་བྱར་རུང་བ་ཉིད་ཡིན་ནོ། །

[Block 1485]
བུད་མེད་མ་ཡིན་པ་ཉིད་ཀྱིས་གནས་སྐབས་དང་འདྲ་བར་མི་རུང་བ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1486]
ཕམ་པར་གྱུར་པ་ཐུན་མོང་མ་ཡིན་པ་ལྷག་པར་སྤྱད་པ་ཅན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སྐྱེས་པ་ཉིད་དུ་ཁས་བླངས་པ་ལ་རབ་ཏུ་འབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་བྱར་རུང་བ་ཉིད་ཡིན་ཏེ། བུད་མེད་བསླབ་པ་ཕུལ་ནས་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ།[^1049] །བུད་མེད་བསྙེན་པར་རྫོགས་པར་བྱ་བ་ལ་གཉུག་མར་གནས་པ་རྣམས་ཡན་ལག་ཡིན་ནོ་ཞེས་བྱ་བ་ལ།

[Block 1487]
འདིར་གཞུང་ནི་གསོ་སྦྱོང་གི་གཞི་ལས།

[Block 1488]
ཇི་སྐད་དུ། བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་མ་རྣམས་ཀྱི༌[^1050]དགེ་སློང་རྣམས་དང་ཉེ་བར་དགེ་སློང་མའི་དངོས་པོ༌[^1051]ཡོངས་སུ་བཙལ་བར་བྱའོ་ཞེས་གང་གསུངས་པ་ལ་དགེ་སློང་དེ་རྣམས་གང་དག་ལགས། ཉེ་བ་འཁོར་གཉུག་མར་གནས་པ་དང་རིང་དུ་གནས་པ་དག་གོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེའི་གནས་ལ་བརྟེན་པའི་གནས་ལ་གནས་པའི་དགེ་སློང་གི་དགེ་འདུན་ལ་ཉེ་བར་བརྟེན་པས་དགེ་སློང་མ་རྣམས་ཀྱི༌[^1052]གནས་སོ། །

[Block 1489]
དེ་ནས་དུས་དུས་སུ་གདམས་ངག་དང་རྗེས་སུ་བསྟན་པ་སློང་བ་སྟེ། གནས་པ་ལས་འདའ་བ་ནི་རིགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིས༌[^1053]ཤེས་པའོ། །

[Block 1490]
གཉུག་མར་གནས་པ་ཉིད་ནི་འདིར་ཡུན་རིང་པོར་གནས་པ་ཉིད་ཀྱིས་ཁྱད་པར་དུ་གྱུར་པ་ལ་རིང་དུ་གནས་པ་ཡིན་ནོ། །

[Block 1491]
སྐྱེ་བའི་ཚེ་ཉིད་ན་ཕུལ་ལམ་ཉམས་ན་མི་སྐྱེའོ་ཞེས་བྱ་བ་ལ། སྐྱེ་བའི་དངོས་པོ་ནི་སྐྱེ་བ་ཉིད་དེ་སྐྱེ་བཞིན་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1492]
སྡོམ་པ་ལེན་པའི་ཚེ་ན་སྡོམ་པ་དེ་སྐྱེ་བའི་ཚེ་ཉིད་གང་ཡིན་པའི་སྐྱེ་བཞིན་པ་ཉིད་ཀྱི་དེའི་གནས་སྐབས་དེ་ལ་ཕུལ་བས་ཡོངས་སུ་བཏང་བ་ལ་སོགས་པས་ཕུལ་ལམ་ཉམས་པར་འགྱུར་རོ། །

[Block 1493]
གང་ཞིག་སྡོམ་པ་སྐྱེ་བཞིན་པ་དེ་ནི་རྟོགས་པ་སྟེ། རྟོགས་པ་ལ་ནི་སླར་ལོག་པ་རྒལ་བ་ལ་སོགས་པ་ལ་མཐོང་བ་མ་ཡིན་ནོ། །

[Block 1494]
དེ་བས་ན་སྡོམ་པ་སྐྱེ་བཞིན་པ་ལ་སླར་ལོག་པས་གནས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་གང་ཞིག་གིས་འདོད་པ་དེ་བཟློག་པའི་དོན་དུ་མདོ་འདིའོ། །

[Block 1495]
འདིར་གཞུང་ནི་སིལ་བུ་རྣམས་ལས།

[Block 1496]
ཉེ་བ་འཁོར་རེ་ཞིག་བསྙེན་པར་རྫོགས་ནས་ཁྱིམ་པ་ཉིད་ཡིན་ནོ་སྙམ་དུ་སོ་སོར་ཤེས་ན༌[^1054]ཡང་བསྙེན་པར་རྫོགས་པ་མ་ཡིན་ཞེས་བྱ་བ་ན༌[^1055]བསྙེན་པར་རྫོགས་པར་བྱེད་པའི་ཚེ་ན་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས༌[^1056]གསུངས་པ་ཡིན་ནོ། །

[Block 1497]
རབ་ཏུ་བྱུང་བའི་གཞི་ཞུ་བ་ཕལ་ཆེ་བའི་སྐབས་སོ། །

[Block 1498]
[^1057]འདུལ་བའི་འགྲེལ་པ་རང་གིས་རྣམ་པར་བཤད་པ་ཞེས་བྱ་བ་ལས་རབ་ཏུ་བྱུང་བའི་གཞི་རྫོགས་སོ།། །།

[Block 1499 [HEADING]]
## མི་ཚངས་པར་སྤྱོད་པའི་ཕམ་པར་འགྱུར་བ། ^2-0

[Block 1500]
རང་བཞིན་ཉམས་པས་བྱས་པ་ཉིད་ནི་ཕུལ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། རང་བཞིན་ཉམས་པས་བྱས་པ་ནི་རང་བཞིན་ཉམས་པས་བྱས་པ་ཉིད་དོ། །

[Block 1501]
ཕུལ་བ་ལས༌[^1058]གང་ཞིག་རང་བཞིན་ཉམས་པས་བྱས་པ་ཉིད་དེ་ནི་ཕུལ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1502]
རང་བཞིན་ཉམས་པ་ནི་ཐ་སྙད་ལས་ཉམས་པ་ཞེས་བྱའོ། །

[Block 1503]
རང་བཞིན་ཉམས་པ་ཉིད་ནི་རྣམ་པ་གསུམ་གྱིས་སྐྱེས་པ༌[^1059]ཡིན་ཏེ། སྨྱོས་པ་དང་། སེམས་རྣམ་པར་གཡེང་བ་དང་། སྡུག་བསྔལ་གྱིས་མངོན་པར་གདུངས་པས་སོ། །

[Block 1504]
དེ་ལ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རང་བཞིན་ཉམས་པའི་གང་ཟག་ལ་ཕུལ་བ་ཉིད་གང་ཞིག་བྱེད་པ་འདི་ཉིད་དེ་ནི་ཕུལ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1505]
འདི་ནི་ཐ་སྙད་དུ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1506]
གང་ཞིག་འདིར་ལྐུགས་པ་ལ་མ་ཡིན་ནོ་ཞེས་བྱ་བས་ནི་དེ་ལ་ཡང་གང་ཞིག་ཕུལ་བ་ཉིད་དེ་ནི་ཕུལ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1507]
རྣམ་པ་ཐམས་ཅད་དུ་སྨྲ་བར་མི་ནུས་པ་དེ་ནི། འདིར་ལྐུགས་པར་འདོད་དེ། དེ་ལ་གང་ཞིག་རབ་ཏུ་རིག་པ་དེ་ནི་རབ་ཏུ་རིག་པས་འདི་ཞུགས་པ་མ་ཡིན་ནོ། །

[Block 1508]
མི་མ་ཡིན་པའི་འགྲོ་བ་ལ༌[^1060]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ལྷ་དང་སྤྲུལ་པ་ལ་སོགས་པ་ལའོ། །

[Block 1509]
མ་གོ་བ་ཉིད་ལ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གླེན་པ་དང་འོན་པ་དང་སྙོམས་པར་ཞུགས་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་རྣམས་ཀྱང་བསྡུས་ཏེ། གླེན་པ་དང་འོན་པ་དག་བསྡུས་པ་ཉིད་ཀྱི་ཕྱིར་འདི་རྒྱུ་གཞན་མཐོང་བ་ཡིན་ཏེ། དེ་བས༌[^1061]རྣམ་པ་ཐམས་ཅད་དུ་གོ་བ་དང་ཉན་པའི་ཕྱིར་ཞེས་བྱ་བ་གྲངས་ཇི་ལྟ་བ་བཞིན་དུ་འདིར་མི་ནུས་པ་ནི་གླེན་པ་དང་འོན་པ་དག་ལ་འདོད་པ་རྣམ་པར་གནས་པ་ཡིན་ཏེ། གང་དང་ཉེ་བར་ཕུལ་བ་དེ་ལ་གོ་བ་ཉིད་ལ་ཞེས་བྱ་བ་འདི་འདིར་ཤུགས་ཀྱིས་རྟོགས་པ་ཡིན་ནོ། །

[Block 1510]
དབེན་པར་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་དབེན་པའི་འདུ་ཤེས་ཀྱིས་སམ་དབེན་པ་མ་ཡིན་པའི་འདུ་ཤེས་ཀྱིས་དབུལ་བ་ཉིད་བྱས་ན་ཡང་དེ་ཕུལ་བ་ཉིད་མ་ཡིན་ནོ། །
--- END BLOCKS ---
