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
[Block 1611]
གཞུང་གཞན་ལས་ཅུང་ཟད་ཟིན་ཏམ། སྐྲངས་པ་ཉིད་དམ། རུལ་བ་ཉིད་དམ། སྲོག་ཆགས་དག་གིས་ཟོས་པ་ཉིད་དམ་ཞེས་གསུངས་པ་སྟེ། དེ་ལ་འདིར་སྐྲངས་པ་དང་སྲོག་ཆགས་རྣམས་ཀྱིས་ཟིན་པའི་ཚིག་བྱས་པ་ཡིན་ནོ། །

[Block 1612]
འདིར་ཅུང་ཟད་ཟིན་པས་ནི་མ་ཟིན་པ་ཤེས་པར་བྱའོ། །

[Block 1613]
ལྷག་མ་ནི་གོ་སླ་བ་ཉིད་ཀྱི་ཕྱིར་རྒྱས་པར་མ་བཤད་དོ། །

[Block 1614]
རྨའི་སྒོ་ལ་བརྟེན་པའི་ཕྱོགས་འདི་བཟུང་བ་ཡིན་གྱི་གཞན་གྱི་ལུས་ལ་བརྟེན་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1615]
བགྲོད༌[^1117]པར་བྱ་བ་ཕྱེད་བཅད་པ་ཉིད་ལ་ཡང་ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་འདིར་བགྲོད་པར་བྱ་བའི་ཚིག་གིས་གནས་མ་ལུས་པ་བཟུང་བ་སྟེ། རྨའི་སྒོ་ཙམ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1616]
མི་ཚངས་པར་སྤྱོད་པའི་ཕྱིར་ཉེ་བར་སོང་བའི་བགྲོད་པར་བྱ་བ་ཕོ་དང་མོ་དང་མ་ནིང་ཕྱེད་བཅད་པ་ཉིད་ལ་དང་པོ་ཡོངས་སུ་རྫོགས་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1617]
འདིར་གཞུང་ནི། བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་བུད་མེད་ལུས་ཕྱེད་དུ་བཀུམ་ལ་རྨའི་སྒོ་གསུམ་པོ་རྣམས་ལ་རྨའི་སྒོ་གཞན་དང་གཞན་གང་ཡང་རུང་བ་ཞིག་མ་ཉམས་པ་དེར་མི་ཚངས་པར་སྤྱོད་པ་སོ་སོར་བསྟེན་ན༌[^1118]མཐར་འགྱུར་རམ་ཞེས་གསུངས་པ་དེ་ནི་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 1618]
ཡང་གི་སྒྲ་ནི་ན་སྨད་པ་ཉིད་མེད་པ༌[^1119]ཞེས་བྱ་བ་རྗེས་སུ་འཇུག་པའི་དོན་དུའོ། །

[Block 1619]
བསྟེན་པར་བྱ་བའི་དབུས་ཕྱེ་བའི༌[^1120]མཚམས་སྦྱར་བ་མི་མངོན་པ་ལ་ཡང་ངོ་། །མངོན་པ་ལ་ནི་ཚིག༌[^1121]འོག་མར་རོ་ཞེས་བྱ་བ་ནི་མངོན་པའི་རྗེས་སུ་མཚམས་ཐམས་ཅད་མངོན་པ་ལ་དེ་མ་ཐག་པའི་རིམ་པ་ཞེས་བྱ་བའོ། །

[Block 1620]
གང་དུ་མཚམས་མངོན་པ་ལ་དེར་རྩ་བ་ནི་འདིར་སྦོམ་པོའོ། །

[Block 1621]
གང་དུ་སྦོམ་པོ་དེ་ལ་ནི་འདིར་ཉེས་བྱས་སོ། །

[Block 1622]
གང་དུ་ཉེས་བྱས་དེ་ལ་ནི་འདིར་ཕྲ་མོར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1623]
སྦོམ་པོའི་དབང་དུ་བྱས་པ་ནི་ཕག་ལ་སོགས་པ་བཙོས་པ་སྤུ་མེད་པ་དག་ལའོ་ཞེས་བྱ་བ་ནི་དབང་དུ་བྱས་པ་བསྟན་པའི་ཕྱིར་དང་པོར་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ནི་ཞེས་བྱ་བའི་ཚིག་སྨོས་སོ། །

[Block 1624]
དེ་ལས་གཞན་བརྗོད་པར་བྱ་ཞེས་བྱ་བ་ནི་དེ་ལས་སྔ་རོལ་དུ་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཞེས་བྱ་བ་འདི་དང་འབྲེལ་ཏོ། །

[Block 1625]
འདིར་ལོག་པར་རྟོག་པ་ལ་སྦོམ་པོ་ནི་གཉེན་པོ་ཀུན་ཏུ་སྤྱོད་པ་གཞན་ཡང་མ་ཡིན་ཏེ། འདིའི་རྗེས་སུ་འབྲང༌[^1122]ནས་ཉེས་བྱས་དང་གཞན་ལ་ནི་ཉམས་པ་ཉིད་དོ། །

[Block 1626]
རྨའི་སྒོ་རྣམས་ལ་གང་ཞིག་བཅོས་མ་ཉིད་འདི་ནི་དེ་བས་ན་སྨད་པའོ། །

[Block 1627]
སྤུ་མེད་པའི་ཚིག་ནི་འདིར་མིའི་པགས་པ་ཉིད་དང་འདྲ་བའི་ཕྱིར་སྤུ་མེད་པ་ཉིད་ལ་ན༌[^1123]སྨད་པ་མེད་དོ་ཞེས་བྱ་བའི་ཀུན་ཏུ་རྟོག་པ༌[^1124]བཟློག་པའི་དོན་དུ་སྟེ། སྤུ་དང་བཅས་པ་ཉིད་ལ་ན་སྨད་པ་མེད་པ་བསྟན་པའི་ཕྱིར་ནི་མ་ཡིན་ནོ། །

[Block 1628]
འདིར་སོགས་པའི་སྒྲ་ནི་རབ་ཏུ་དབྱེ་བ་ཉེ་བར་བསྡུ་བའི་དོན་དུའོ། །

[Block 1629]
དེ་བས་ན་སྤུ་དང་བཅས་པའི་དུད་འགྲོ་རྣམས་ལ་འདིས་འཕངས་པར་རིག་པར་བྱའོ། །

[Block 1630]
འདིར་གཞུང་ནི། དེ་ལྟར་དུད་འགྲོའི་སྐྱེས་གནས༌[^1125]སུ་སྐྱེས་པ་ཐམས་ཅད་ལ་གཏོགས་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1631]
མགོ་བཅད་པའི་ཁར་རོ་ཞེས་བྱ་བ་ནི་འདིར་གཅིག་པུ་དེ་ལ་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་དོ། །

[Block 1632]
ཟག་བྱེད་དང་བཤང་བའི་ལམ་དག་ལ་ནི་ཕམ་པ་ཉིད་དུ་བྱེད་པ་ཉིད་དོ། །

[Block 1633]
ཁྱད་པར་མེད་པར་བརྗོད་པའི་ཕྱིར་ཁ་དང་འབྲེལ་པ་ཐམས་ཅད་ལའོ། །

[Block 1634]
བསྟེན་པར་བྱ་བ་དང་། སྟེན་པར་བྱེད་པ་ལུས༌[^1126]ཐ་དད་པར་བྱས་པ་གཉིས་ཀྱིའོ་ཞེས་བྱ་བ་ནི་ཁ་དང་བཤང་བའི་ལམ་དང་གཞན་དག་དང་མོའི་དབང་པོ་བསྟེན་པ༌[^1127]དང་བཅས་པ་ལ་སོགས་པ་ལུས་ལས་ཐ་དད་པར་བྱས་པའི་ཕོའི་དབང་པོ་དང་ཡང་དག་པར་སྦྱོར་བ་ལ་རང་གི་ཕོའི་དབང་པོ་དང་རང་གི་ཁའི་ལམ་དང་བཤང་བའི་ལམ་དུ་དགེ་སློང་མ་ལ་མོའི་དབང་པོས་ཀྱང་རང་གི་ཡང་དག་པར་སྦྱོར་བ་ལ་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1635]
གཞན་པ་གཉིས་ཀྱང་གཞན་གྱི་གཉིས་དང་གཞན་དུ་སྦྱོར་བར་བྱེད་ནའོ་ཞེས་བྱ་བ་ནི་ལུས་ལས་ཐ་དད་པར་མ་གྱུར་པ་ལ་ཡང་གཞན་གྱི་བསྟེན་པར་བྱ་བ་དང་སྟེན་པར་བྱེད་པ་དང་ཕོ་དང་མོ་དང་མ་ནིང་དང་གཞན་ལ་ཅི་རིགས་པར་བསྟེན་པར་བྱ་བ་སྟེན་པར་བྱེད་པ་ལ་ཡང་དག་པར་སྦྱོར་བ་ལ་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་དོ། །

[Block 1636]
དེ་བཞིན་དུ་གཞན་དུ་ཡང་གསུངས་ཏེ། བུད་མེད་ཀྱི་ཚོགས་ལ་བཅད་ནས་འཇུག་པར་བྱེད་ན་ཅི་ཞིག་ཐོབ་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྦོམ་པོའི་ལྟུང་བ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1637]
གཅིག་ལས་གསུངས་པ་བུད་མེད་ཀྱི་ཚོགས་ལ་རྩོལ་བར་བྱེད་ན་ལྟུང་བ་ཅིར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གཞན་གྱི་ཡན་ལག་གི་རྣམ་པ་གཞན་གྱི་ཟག་བྱེད་དུ་རྩོལ་བར་བྱེད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྦོམ་པོའི་ལྟུང་བ་ཞེས་བྱ་བའོ། །

[Block 1638]
གཞན་དུ་ཡང་དགེ་སློང་འགའ་ཞིག་ཡོད་དེ་ཟག་བྱེད་ལ་ཟག་བྱེད་རྩོལ་བར་བྱེད་ན་ལྟུང་བ་མེད་པར་འགྱུར་རམ། བཀའ་སྩལ་པ། མཐར་འགྱུར་རོ། །

[Block 1639]
བུད་མེད་ཀྱི་ཚོགས་ལ་བཅད་ནས་རྩོལ་བར་བྱེད་པ་དང་གཉིས་ཆར་བཅད་ནས་བཅུག་ན་ཉེས་པ་སྦོམ་པོའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1640]
ལྷག་མ་འདིའི་རྗེས་སུ་འབྲང༌[^1128]ནས་ཤེས་པར་བྱ་སྟེ། མདོ་འདི་དག་བྱས་པ་ཡིན་ནོ། །

[Block 1641]
གཞན་པའི་བུ་ག་ལུས་ལས་བཅད་པ་ལ་ཡང་ཞེས་བྱ་བ་ནི་རྨའི་སྒོ་གསུམ་ལས་གཞན་པའི་བུ་ག་མཚན་གྱིས་དྲལ་བ་ལ་སོགས་པ་བཅོས་མ་དང་། མི་ན་བ་ལ་སོགས་པ་ལུས་བྱུང་བ་ཉིད་ལས་བྱུང་བ་དང་པོ་ལས་དོད་པ་ལུས་ལས་བཅད་པ་དང་མ་བཅད་པ་ཡང་སྦོམ་པོའི་དབང་དུ་བྱས་པ་མ༌[^1129]ཡིན་པའོ། །

[Block 1642]
གཅིག་ནས་གསུངས་པ། ལུས་དྲལ་ཏེ་ཡན་ལག་གི་རྣམ་པས་རྩོལ༌[^1130]ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་ཞེས་གསུངས་སོ། །

[Block 1643]
གཞན་དུ་ཡང་མགོ་བོ་བཅད་པར་གྱུར་ཏེ། མཐའ་གཉིས་པ་ལ་འཇུག་པར་བྱེད་ན་ལྟུང་བར་འགྱུར་རམ། ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་དེ་འདིའི་བསྡུས་པའོ། །

[Block 1644]
བསྟེན་པར་བྱ་བ་མ་ནིང་མོ་སྦུབས་མེད་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། བུ་ག་ལུས་ལས༌[^1131]བཅད་པ་ལ་ཡང་ངོ་ཞེས་སྔར་སྨོས་པའི་རྗེས་བསྙག་པའི་ཕྱིར་ཡང་གི་སྒྲའོ། །

[Block 1645]
སྦུབས་ཞེས་བྱ་བ་ནི་གང་ལ་ཕོའི་དབང་པོ་གཞུག་པར་བྱ་བའི་སྐབས་ཀྱི་ཚད་དེ་ལྟ་བུ་སྦུབས་ཀྱི་རྒྱུན་མ་ཆད་པར་བསྙེན་པར༌[^1132]འགྱུར་བའི་མ་ནིང་ལ་བུ་ག་ལུས་ལས་བཅད་པ་ལ་ཡང་ངོ་ཞེས་སྦོམ་པོའི་དབང་དུ་བྱས་པའོ། །

[Block 1646]
འབྲེལ་པ་ཙམ་ལ་འདིར་ཕམ་པ་ཞེས་བྱ་བ་སྦུབས་ཀྱི་སྒྲས་ཤེས་པར་བྱའོ། །

[Block 1647]
ཀློག་པ་འབའ་ཞིག་ཏུ་འདི་བརྗོད་དེ་མ་ནིང་ལ་རྩོལ་བར་བྱེད་དེ་གང་དུ་གླགས་མེད་པ་ལ་ལྟུང་བར་འགྱུར་བ་མཆིས་སམ། སྦོམ་པོའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་བསྡུས༌[^1133]པའོ། །

[Block 1648]
མཆུ་གཉིས་ལའོ་ཞེས་བྱ་བ་ནི་མཆུ་གཉིས་ལ་སྦྱར་བ་ཙམ་ལ་ཡང་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་དེ། [^1134]སོའི་མཐའ་ཚུན་ཆད་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་ཇི་སྲིད་དུ་བསྩལ་བ༌[^1135]ཞེས་བྱ་བ་སྔོན་གྱི་རྗེས་སུ་འབྲང་བས་རྟོགས་པར་བྱའོ། །

[Block 1649]
ཕྱི་རོལ་གྱི་མཚམས་ལ་ཐུག་པར་རོ་ཞེས་བྱ་བ་ཁའི་དང་པོ་ནི་སོ་ཕན་ཆད་དོ་ཞེས་བསྟན་པ་ལ་ཕྱི་རོལ་དུ་སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་དོ། །

[Block 1650]
འདིར་གཞུང་ནི། སོའི་ཕྱི་རོལ་དུ་ཉམས་པར་བྱེད་ན་ཉེས་པ་སྦོམ་པོའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
