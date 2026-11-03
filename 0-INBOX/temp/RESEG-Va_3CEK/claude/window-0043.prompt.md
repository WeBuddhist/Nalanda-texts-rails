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

[Block 1511]
འོ་ན་བསྟན་བཅོས་ལས་ང་རྒྱལ་རྣམ་པ་དགུ་སྟེ། བདག་མཆོག་ཡིན་ནོ་སྙམ་པ༌[^1095]ང་རྒྱལ་གྱི་རྣམ་པ་དང་། བདག་དང་འདྲའོ་སྙམ་པའི་ང་རྒྱལ་གྱི་རྣམ་པ་དང་། བདག་དམན་ནོ་སྙམ་པའི༌[^1096]ང་རྒྱལ་གྱི་རྣམ་པ་དང་བདག་པས་མཆོག་ཡོད་དོ། །

[Block 1512]
བདག་དང་མཉམ་པ་ཡོད་དོ། །

[Block 1513]
བདག་པས༌[^1097]དམན་པ་ཡོད་དོ། །

[Block 1514]
བདག་པས་མཆོག་མེད་དོ། །

[Block 1515]
བདག་དང་མཉམ་པ་མེད་དོ། །

[Block 1516]
བདག་པས་དམན་པ་མེད་དོ་སྙམ་པ་ང་རྒྱལ་གྱི་རྣམ་པ་ཞེས་གང་བཤད་པ་ཇི་ལྟ་བུ་ཞེ་ན། རྣམ་པ༌[^1098]དགུ་པོ་དེ་དག་ནི་གསུམ་པོ་འདི་དག་ཉིད་ལས་བྱུང་བ༌[^1099]སྟེ། གསུམ་གང་ལས་ཤེ་ན། ང་རྒྱལ་དང་། ལྷག་པའི་ང་རྒྱལ་དང་། ཅུང་ཟད་སྙམ་པའི་ང་རྒྱལ་དག་ལས་སོ། །

[Block 1517]
དེ་ལ་དང་པོའི་གསུམ་ནི་ལྟ་བ་ལ་བརྟེན་པའི་ང་རྒྱལ་གསུམ་སྟེ། ལྷག་པའི་ང་རྒྱལ་དང་། ང་རྒྱལ་དང་། ཅུང་ཟད་སྙམ་པའི་ང་རྒྱལ་རྣམས་སོ། །

[Block 1518]
གཉིས་པའི་གསུམ་ནི་ཅུང་ཟད་སྙམ་པའི་ང་རྒྱལ་དང་། ང་རྒྱལ་དང་། ལྷག་པའི་ང་རྒྱལ་རྣམས་སོ། །

[Block 1519]
གསུམ་པའི་གསུམ་ནི་ང་རྒྱལ་དང་། ལྷག་པའི་ང་རྒྱལ་དང་། ཅུང་ཟད་སྙམ་པའི་ང་རྒྱལ་རྣམས་སོ། །

[Block 1520]
རེ་ཞིག་ཆེས་ཁྱད་པར་དུ་འཕགས་པ་བས་བདག་ཅུང་ཟད་ཅིག་གིས་དམན་ནོ་སྙམ་པ་ནི་སེམས༌[^1100]ཁེངས་པའི་གནས་ཡིན་པའི་ཕྱིར་ཅུང་ཟད་སྙམ་པའི་ང་རྒྱལ་དུ་རིགས་ན། བདག་པས་དམན་པ་མེད་དོ་སྙམ་པ་འདི་ལ་གོ་ཁེངས་པའི་གནས་ཅི་ཞིག་ཡོད་ཅེ་ན། གང་ཞིག་མངོན་པར་འདོད་པའི་སེམས་ཅན་གྱི་ཚོགས་དམ་པའི་ནང་ན་བདག་ཉིད་དམན་ཡང་ཐ་གིའོ་སྙམ་དུ་སེམས་པ་དེ་ལྟ་བུ་དེ་ཡོད་དོ། །

[Block 1521]
གཞན་ཡང་འདི་ནི་ཡེ་ཤེས་ལ་འཇུག་པ་ལས་བཤད་པའི་ལུགས་ཡིན་གྱི་རབ་ཏུ་བྱེད་པ་ལས་བསྟན་པ་ཡོངས་སུ་བཟུང་སྟེ། བདག་མཆོག་ཡིན་ནོ་སྙམ་པ་འདི་ནི་དམན་པ་དང་། མཉམ་པ་དང་། ཁྱད་པར་དུ༌[^1101]འཕགས་པ་ལ་ལྟོས་ནས་ང་རྒྱལ་ཡང་ཡིན་ལ། ལྷག་པའི་ང་རྒྱལ་ཡང་ཡིན།[^1102] ང་རྒྱལ་ལས་ཀྱང་ང་རྒྱལ་ཡང་ཡིན་ནོ། །

[Block 1522 [HEADING]]
#### ང་རྒྱལ་བདུན་པོ་སྤང་བྱ། ^2-11-3-0

[Block 1523]
ཡང་ན༌[^1103]ང་རྒྱལ་བདུན་པོ་འདི་དག་ཅི་ཞིག་གིས་སྤང་བར་བྱ་བ་ཡིན་ཞེ་ན། སྨྲས་པ། མཐོང་དང་བསྒོམ་པས་ཟད་བྱ་བ། །དེ་དག་ནི་མཐོང་བ་དང་བསྒོམ་པ་དག་གིས་ཟད་པར་བྱ་བ་སྟེ། དེ་ནས་འདི་སྐད་དུ་ཐམས་ཅད་མཐོང་བ་དང་བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་ཡིན་ནོ་ཞེས་བཤད་པར་འགྱུར་རོ། །

[Block 1524 [HEADING]]
### འཕགས་པ་རྣམས་བསྒོམ་པས་སྤང་བར་བྱ་བ་མ་སྤངས་པ། ^2-12-0

[Block 1525]
ཅི་འཕགས་པ་རྣམས་བསྒོམ་པས་སྤང་བར་བྱ་བ་མ་སྤངས་པ་གང་ཡིན་པ་དེ་ཀུན་དུ་སྤྱོད་དམ་ཞེ་ན། ངེས་པ་མེད་དེ་འདི་ལྟར་བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི། གསོད་སོགས་ཀུན་ནས་དཀྲིས་པའོ། །

[Block 1526]
ཉོན་མོངས་པ་ཀུན་ནས་དཀྲིས་པ་གང་གི༌[^1104]ཆེད་དུ་བསམས་ཏེ། སྲོག་ཆགས་ཀྱི་སྲོག་གཅོད་པར་བྱེད་པ་ནས་བརྫུན་དུ་སྨྲ་བར་བྱེད་པའི་བར་དེ་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་ཡིན་ཏེ་བསྒོམ་པས་སྤང་བར་བྱ་བའི༌[^1105]ཆོས་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 1527]
དེ་བཞིན་འཇིག་སྲེད། འཇིག་པའི་སྲེད་པ་ཡང་བསྒོམ་པས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1528]
འཇིག་པའི་སྲེད་པ་ཞེས་བྱ་བའི་ཆོས་འདི་ཅི་ཞིག་ཡིན་ཞེ་ན། ཁམས་གསུམ་པའི་མི་རྟག་པ་སྟེ། དེ་ལ་དོན་དུ་གཉེར་བ་ནི་འཇིག་པའི་སྲེད་པའོ། །

[Block 1529]
དེ་བཞིན་ཞེས་བྱ་བའི་སྒྲས་ནི་སྐྱེ་བའི་སྲེད་པའི་ཕྱོགས་བདག་ནི་གླང་པོ་ཆེའི་རྒྱལ་པོ་ས་སྲུང་གི་བུར་གྱུར་ཀྱང་ཅི་མ་རུང་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་བཟུང༌[^1106]ངོ་། །བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི་ང་རྒྱལ་གྱི་རྣམ་པ་རྣམས་ཀྱང་ཡོད་དོ་ཞེས་བཤད་ལ། ངའོ་སྙམ་པའི་ང་རྒྱལ་ཡང་ཡོད་མོད་ཀྱི། འཕགས་པ་ལ། རྣམ་སོགས་ངའོ་སྙམ་མི་འབྱུང་། །སོགས་པ༌[^1107]སྨོས་པས་ནི་འཇིག་པའི་སྲེད་པའི་བར་དུ་བཟུང༌[^1108]ངོ་། །ཅིའི་ཕྱིར་དེ་དག་མ་སྤངས་ཀྱང་མི་འབྱུང་ཞེ་ན། ལྟ་བས་རྒྱས་པར་འགྱུར་ཕྱིར་རོ། །

[Block 1530]
ང་རྒྱལ་གྱི་རྣམ་པ་རྣམས་དང་། ངའོ་སྙམ་པའི་ང་རྒྱལ་ནི་འཇིག་ཚོགས་ལ་ལྟ་བས་རྒྱས་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1531]
དེའི་ཕྱིར་རྐེད་པ༌[^1109]བཅག་པའི་ཕྱིར་ཡང་ལྡང་བར་མི་ནུས་སོ། །

[Block 1532]
གསོད་པ་ལ་སོགས་པའི་ཀུན་ནས་དཀྲིས་པ་ནི་ལོག་པར་ལྟ་བས་རྒྱས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1533]
འཇིག་པའི་སྲེད་པ་ནི་ཆད་པར་ལྟ་བས་རྒྱས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1534]
སྐྱེ་བའི་སྲིད་པའི༌[^1110]ཕྱོགས་ནི་རྟག་པར་ལྟ་བས་རྒྱས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1535]
མི་དགེ་བའི༌[^1111]འགྱོད་པའམ༌[^1112]མ་ཡིན་ནོ། །

[Block 1536]
འགྱོད་པ་མི་དགེ་བ༌[^1113]ཡང་བསྒོམ་པས་སྤང་བར་བྱ་བ༌[^1114]ཡིན་ན་འཕགས་པ་ལ་ནི༌[^1115]མི་འབྱུང་སྟེ། དེ་ཐེ་ཚོམ་གྱིས་ཀུན་ནས་བསླང་བ་ཡིན་པའི༌[^1116]ཕྱིར་རོ། །

[Block 1537 [HEADING]]
### ཀུན་དུ་འགྲོ་བ། ^2-13-0

[Block 1538]
ཡང་ཕྲ་རྒྱས་དགུ་བཅུ་རྩ་བརྒྱད་པོ་དེ་དག་ལས་དུ་ནི་ཀུན་དུ་འགྲོ་བ་དག་ཡིན། དུ་ནི་ཀུན་དུ་འགྲོ་བ་མ་ཡིན་ཞེ་ན།

[Block 1539 [VERSE]]
སྡུག་བསྔལ་རྒྱུ་མཐོང་སྤང་བྱ་བ། །
ལྟ་དང་དེ་བཞིན་ཐེ་ཚོམ་དང་།
གང་དེ་ལྷན་ཅིག་མ་འདྲེས་པའི། །
མ་རིག་གང་ཡིན་ཀུན་དུ་འགྲོ། །

[Block 1540]
སྡུག་བསྔལ་དང་ཀུན་འབྱུང་མཐོང་བས་སྤང་བར་བྱ་བའི་ལྟ་བ་རྣམས་དང་། ཐེ་ཚོམ་དང་། དེ་དག་དང་མཚུངས་པར་ལྡན་པའི་མ་རིག་པ་དང་། སྡུག་བསྔལ་བ༌[^1117]དང་ཀུན་འབྱུང་མཐོང་བས་སྤང་བར་བྱ་བའི་མ་རིག་པ་མ་འདྲེས་པ་ཁོ་ན་སྟེ། དེ་ལྟར་ན་ལྟ་བ་བདུན་དང་། ཐེ་ཚོམ་གཉིས་དང་། མ་རིག་པ་གཉིས་དང་། ཕྲ་རྒྱས་བཅུ་གཅིག་པོ་དེ་དག་ནི་རང་གི་ཁམས་མཐའ་དག་ལ་དམིགས་པའི་ཕྱིར། སྐལ་བ་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་ཡིན་ནོ། །

[Block 1541]
ཅི་རེ་ཞིག་རིམ་གྱིས་སམ་འོན་ཏེ་ཅིག་ཅར་ཡང༌[^1118]དམིགས། གལ་ཏེ་རིམ་གྱིས་ན་ནི་གཞན་དག་ལ་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 1542]
འོན་ཏེ་ཅིག་ཅར་རོ་ཞེ་ན་ནི། སུ་ཞིག་འདོད་པའི་ཁམས་མཐའ་དག་གིས་འདག་པར༌[^1119]ཡིད་ཆེས་པར་འགྱུར་བའམ། མཐའ་དག་རྒྱུ་མ་ཡིན་པ་ལས༌[^1120]རྒྱུར་ཡིད་ཆེས་པར་འགྱུར། མཐའ་དག་ལ་ནི༌[^1121]ཅིག་ཅར་དུ་དམིགས་སོ་ཞེས་ནི་མི་ཟེར་རོ། །

[Block 1543]
འོན་ཀྱང་རྣམ་པ་ལྔ་པོ་ཐམས་ཅད་ཀྱང་ཅིག་ཅར་དུ་དམིགས་སོ། །

[Block 1544]
དེ་ལྟ་ན་ཡང་གང་ལ་བདག་ཏུ་ལྟ་བ་ཡོད་པ་དེ་ལ་བདག་ལ་སྲེད་པ་ཡོད་ལ།[^1122] གང་ལ་མཆོག་དང་དག་པར་ལྟ་བ་ཡོད་པ་དེ་ལ་དེའི་དོན་དུ་གཉེར་བ་ཡོད་ཅིང་། དེས་ཀྱང་ང་རྒྱལ་དུ་འགྱུར་བས་སྲེད་པ་དང་ང་རྒྱལ་དག་ཀྱང་རུང༌[^1123]ཀུན་དུ་འགྲོ་བ་ཡིན་པར་འགྱུར་རོ། །

[Block 1545]
དེ་ལྟ་ཡིན་ན་དེ་གཉི་ག་མཐོང་བ་དང་བསྒོམ་པས་སྤང་བར་བྱ་བ་ལ་དམིགས་པའི་ཕྱིར་ཅི་ཞིག་གིས་སྤང་བར་བྱ་བ་ཡིན་ཞེ་ན། འདྲེན་མ་ལ་དམིགས་པའི་ཕྱིར༌[^1124]བསྒོམ་པས་སྤང་བར་བྱ་བ་དག༌[^1125]ཡིན་ནོ། །
--- END BLOCKS ---
