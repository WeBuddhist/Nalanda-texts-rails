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
འདི་ལྟར། གཞན་སེལ་མིན། འདི་ལྟར་སྔོན་པོའི་སྒྲ་དང་མེ་ཏོག་ཀུནྡ་ལ་སོགས་པ་བཞིན་སྔོན་པོ་ལ་སོགས་པ༌[^1239]གཞན་སེལ་བ་མ་ཡིན་ནོ། །

[Block 1612]
དེའི་ཕྱིར་ཁོངས་སུ་འདུས་པ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1613]
ཁས་བླངས་ཀྱང་བརྗོད་པར་བྱ་བ་ཉིད་ཀྱི་ཁོངས་སུ༌[^1240]འདུས་པ་ཡིན་ནོ། །

[Block 1614]
གལ་ཏེ་གཉིས་ཀ་ཡང་བྱེ་བྲག་གི་དོན་དུ་ཡིན་ན་ནི་རྣམ་གྲངས་པའི་སྒྲར་འགྱུར་ཏེ། གཅིག་ལས་རྣམ་གྲངས་སུ་འགྱུར་བས༌[^1241]མཐོང་བ་ཡིན་ནོ། །

[Block 1615]
རྣམ་གྲངས་ཀྱི་སྒྲ་ནི་མ་རྟོགས་པ་དང་། དོན་དུ་མ་ལ༌[^1242]ཡིན་གྱི་སྔར་གྱི་དོན་དེ་ཉིད་རྟོགས་པར་བྱ་བའི་ཕྱིར༌[^1243]རྣམ་གྲངས་གཞན་སྦྱོར་བ་ཡིན་ནོ། །

[Block 1616]
དེ་ལྟར་ན་ནི་རྣམ་གྲངས་ཀྱི་སྒྲ་རྣམས་ཀྱི་སྒྲ་ཉིད་དེ། གང་རྣམ་གྲངས་ཀྱི་སྒྲ་དེས་དོན་དེ་བརྗོད་པ་ཡིན་གྱི་ཅིག་ཅར་བ་ནི་མ་ཡིན་ནོ། །

[Block 1617]
དེ་ལྟར་ན་ཡང་སྔོན་པོའི་སྒྲ་ཉིད་ཀྱིས་ཨུཏྤ་ལའི་དོན་རྟོགས་པས་ན༌[^1244]ཁྱད་པར་དུ་བྱེད་པ་དང་ཁྱད་པར་དུ་བྱ་བ་དག་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1618]
དེ་དག་ནི་རེ་ཞིག་ཐ་མི༌[^1245]དད་པའི་ཕྱོགས་ལ་སྐྱོན་བརྗོད་པའོ། །

[Block 1619 [HEADING]]
##### ཐ་དད་པ་ལ་སྐྱོན་བརྗོད་པ། ^5-7-2-2-0

[Block 1620]
ཇི་ལྟར་ཐ་མི་དད་པ་ལ་བརྗོད་པ་དེ་བཞིན་དུ་ཐ་དད་པ་ལ་ཡང་སྟེ། ཐ་དད་པས་ཀྱང་འདུས་པ་རྣམས་ལས་འདུས་པ་གཞན་ཉིད་གཅིག་བསྒྲུབ་པར་བྱ་བ་དེ་ལ་དེའི་དེ་དག་རྣམས་ལའམ། དེ་དག་རྣམས་ཀྱི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1621]
མ་ལུས་པར་ཕྱོགས་གཅིག་ནས་འཇུག་པ་ཡང་མི་སྲིད་དོ། །

[Block 1622]
ཁས་བླངས་ཀྱང་། ཐ་དད་ན་ཡང་གཉིས་ཀ་མེད། །དེ་ལ་ཡང་གཞི་མཐུན་ཡོད་པ་མ་ཡིན་ལ། ཁྱད་པར་དུ་བྱེད་པ་དང་ཁྱད་པར་དུ༌[^1246]བྱ་བ་ཡང༌[^1247]ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1623]
དེ་ནི་དོན་དག་གམ། སྒྲ་དག་གཅིག་ཏུ་འགྱུར་གྲང་། དོན་དུ་འགྱུར་བ་ལྟར་ན་ཡང་ཡོན་ཏན་དང་རྫས་དག་གམ། དེ་དང༌[^1248]ལྡན་པར་འགྱུར་དྲང་།[^1249] དེ་བཞིན་དུ་སྒྲ་ལས༌[^1250]ཡང་ཡོན་ཏན་དང་རྫས་དག་གམ། དེ་དང༌[^1251]ལྡན་པར་འགྱུར་གྲང་ངོ་ཞེས་བརྟག་ཅིང་དཔྱད་པར་བྱའོ། །

[Block 1624]
དེ་ལ།

[Block 1625 [VERSE]]
དོན་གྱིས༌[^1252]རྫས་དང་ཡོན་ཏན་དག །
གལ་ཏེ་དོན་གཅིག་ལ་འཇུག་ན། །
སྤྱི་དང་བྱེ་བྲག་གཉིས་ཡོད་མིན། །

[Block 1626]
གལ་ཏེ་ཡོན་ཏན་སྔོན་པོ་དང༌[^1253]ཨུཏྤ་ལའི་རིགས་དག་རྫས་གཅིག་ལ་འཇུག་པའི་ཕྱིར་གཞི་མཐུན་པ་དང་ཁྱད་པར་དུ་བྱེད་པ་དང་ཁྱད་པར་དུ་བྱ་བ་དག་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1627]
ཡོན་ཏན་སྔོན་པོ་ཨུཏྤ་ལའི་རིགས་དང་ལྡན་པ༌[^1254]ལ་ཡང་ཡོད་པ་མ་ཡིན་ལ། ཨུཏྤ་ལའི་རིགས་ཡོན་ཏན་སྔོན་པོ་དང་ལྡན་པ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1628]
དེ་ལྡན༌[^1255]གཉིས་དང་ཡོད༌[^1256]མ་ཡིན། །གང་གི་ཚེ་ཡོན་ཏན་སྔོན་པོ་དང་། ཨུཏྤ་ལའི་རིགས་སྤྱིའི་དོན་ལ་ལྡན་པ༌[^1257]དེའི་ཚེ་གཞི་མཐུན་པ༌[^1258]ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1629]
གཞན་ལ་འཇུག་པའི་རྫས་དག་ལ་ཡང་ཁྱད་པར་དུ་བྱེད་པ་དང་ཁྱད་པར༌[^1259]བྱ་བའི་དངོས་པོའམ་གཉིས་ཀ་གཅིག་པ་དག་ཡོད་པ་མ་ཡིན་ཏེ། སྤྱི་དང་བྱེ་བྲག་ཉིད་དང་མི་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1630]
དེ་ལྟར་ན་རེ་ཞིག་དོན་ལ་གཉིས་སྲིད་པ་མ་ཡིན་ནོ། །

[Block 1631 [VERSE]]
དོན་ལ་གཉིས་ཇི་ལྟ་བ། །
དེ་བཞིན་དུ་སྒྲ་རིགས་དང་ནི། །
ཡོན་ཏན་ཙམ་ཞིག་བརྗོད་པར་འགྱུར། །

[Block 1632]
ཤིན་ཏུ་ཐ་དད་ན་ནི་རིགས་དང་ཡོན་ཏན་ནི་སྒྲ་བརྗོད་པར་འགྱུར་བ་ཡིན་ན་དེ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1633]
དེ་དག་གི་གཞི་མཐུན་པ་ལ་ཡང་འབྲེལ་པ་མ་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 1634]
དེའི་སྒྲ་དག་ལ་ཡང་ཁྱད་པར་བྱེད་པ་ཉིད་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1635]
དེ་ལྟར་ན་རེ་ཞིག་རིགས་དང་ཡོན་ཏན་ཙམ་བརྗོད་པ་ཉིད་ཡིན་ནོ། །

[Block 1636]
དེ་ལྡན༌[^1260]བརྗོད་པ་ཉིད་ལ་ནི། །མཚུངས་མི་མཚུངས་སུ་ཐལ་བར་འགྱུར། །

[Block 1637]
གལ་ཏེ༌[^1261]རིགས་དང་ཡོན་ཏན་གྱི་སྒྲ་དག་རྫས་ཀྱི་ཁྱད་པར་གཅིག་ལ་བརྗོད་པ་དེའི་ཕྱིར་རྟེན་མཚུངས་པར་འགྱུར་རོ། །

[Block 1638]
གང་གི་ཕྱིར་ཁྱད་པར་དུ་བྱེད་པ་ཐ་དད་པའི་རྫས་བརྗོད་པ་དེའི་ཕྱིར་མི་མཚུངས་པར་འགྱུར་རོ། །

[Block 1639]
དེའི་ཕྱིར་ངེས་པ་མེད་པ་ལ་གཞི་མཐུན་པ་མེད་དོ། །

[Block 1640]
གལ་ཏེ། མཚུངས་ཕྱིར་བརྗོད་པར་མི་འདོད་ཅེས།[^1262] །གལ་ཏེ་འདི་སྙམ་དུ་རེ་ཞིག་ཉེ་བར་བླངས་པའི་གཞི་མཐུན་པར་མཚུངས་པར་འགྱུར་བས༌[^1263]བརྗོད་པར་མི་འདོད་པ་ནི་འབྲེལ་པར་བྱས་པ༌[^1264]ཁྱད་པར་མེད་དོ། །

[Block 1641]
གང་ལ་བློ་མཚུངས་པའི་རྒྱུ་ཡོད་པ་ཉིད་གཞི་མཐུན་པ་ཡིན་པར་བརྗོད་ཀྱི། དེ་ལ་གཞན་མེ་ཏོག་ཁ་ཟུམ་པ་ལ་སོགས་པའི་ཁྱད་པར་ནི་ཡོད་དུ་ཟིན་ཀྱང་བརྗོད་པར་མི་འདོད་དོ་ཞེ་ན། འདི་ནི་མི་ཟད་པར་བརྒལ་བ་སྟེ། གཉི་ག་རྣམ་པར་བསལ་བ་རྗེས་སུ་བཟུང་ན་ནི་ཇི་སྲིད་དུ་དོན་ཡོད་པ་དེ་ལ་སྒྲའི་བྱ་བ་ཡོད་པས་ན་དེ་ཙམ་བརྗོད་པར་འདོད་པར༌[^1265]སྦྱར་བར་བྱའོ། །

[Block 1642]
འབྲེལ་པ་ཅན་དུ་བྱས་པ་ལ་ནི་བརྗོད་པར་འདོད་པའི་ཁྱད་པར་མ་ཡིན་པ་ལ་ཇི་ལྟར་དངོས་པོར་བརྗོད་པར་བྱ། གཞན་ཡང་། བ་ལང་རྟ་སོགས༌[^1266]ལ་ཡང་མཚུངས། །བ་ལང་དང་རྟ་ལ་སོགས་པ་ཡང་བ་ལང་ཉིད་ཀྱི་ཡོད་པ་ལ་སོགས་པས༌[^1267]འབྲེལ་པར་བྱས་པ་ཁྱད་པར་མེད་པར་འགྱུར་ན། དེ་ལ་ནི་སྤྱི་བརྗོད་པར་མི་འདོད་ལ། དེའི་དངོས་པོར་བརྗོད་པར་བྱ་བ་ཡིན་པས་ན་ཨུཏྤ་ལ་དང་སྔོན་པོ་ལ་སོགས་པ་བཞིན་བ་ལང་དང༌[^1268]རྟ་དག་ཀྱང་གཞི་མཐུན་པར་ཐལ་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1643]
གལ་ཏེ། དེར་བྱེ་བྲག་ཏུ་མ་བྱས་ཤེ་ན། [^1269]གལ་ཏེ་འདི་སྙམ་དུ་བ་ལང་དང་རྟ་ལ་སོགས་པ་ལ༌[^1270]དབྱིབས་ཀྱི་བྱེ་བྲག་ཏུ་བྱས་ཏེ་ཡོད་པར་མ་བརྗོད་དོ། །

[Block 1644]
རང་རང་གི་བསལ་བའི༌[^1271]རིགས་ཀྱི་རྒྱུའི་བྱེ་བྲག་དེར༌[^1272]བྱས་པ་དེ་དག་དེ་བཞིན་དུ་བརྗོད་པ་ཡིན་པར་ཇི་ལྟར་ན་བརྗོད་པར་མི་འདོད། དོན་དེ་ཨུཏྤ་ལ་དང་སྔོན་པོ་བཞིན་ནོ་ཞེས་པ་ཡང་མ་ཡིན་ལ། དེ་བཞིན་དུ་གཞི་མཐུན་པར་ཐལ་བར་འགྱུར་བ་ཡང༌[^1273]མ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟ་ན་ནི། དུ་མར་བྱས་པ་འདུས་པར་འགྱུར། །དངོས་པོ་གཅིག་ལ་སྤྱི་དུ་མས་གསལ་བར༌[^1274]བྱེད་པའི་ཕྱིར་དབྱིབས་དུ་མ་འདུས་པར་འགྱུར་ན་དེ་ལྟར༌[^1275]ན་ཡང་མ༌[^1276]མཐོང་ངོ་། །

[Block 1645]
གཞན་ཡང་། མཚུངས་པ་ནི་བ་ལང་དང་རྟ་ལ་སོགས་པ༌[^1277]ཡང་རྟེན་མཚུངས་པ་དང་མི་མཚུངས་པ་ཉིད་དུ་མ་བརྗོད་པའི་ཕྱིར། བ་ལང་ཉིད་ཀྱི་ཡོད་པ་ཉིད་ལ་སོགས་པ་གསལ་བར་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་དེ་ལ་ཡང་མཚུངས་པར་བརྗོད་པ་ནི་གཞི་མཐུན་པར་ཐལ་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1646]
འདོད་པ་ལ༌[^1278]ཡང་མེད། གང་ལ་གཞི་མཐུན་ཡོད་པར་འདོད་པའི་ཨུཏྤ་ལ་དང་རྫས་ལ་སོགས་པ་ཡོད་དོ་ཞེས་པ་དེ་ལ་ཡང་མི་འཐོབ་པར་འགྱུར་རོ། །

[Block 1647]
གལ་ཏེ་སྤྱི་ཐ་དད་པར་གསལ་བར༌[^1279]བྱེད་པ་ཡིན་པའི་ཕྱིར་བ་ལང་དང་། རྟ་དག་ལ་གཞི་མཐུན་པ་མེད་པ་ཡིན་ན་ནི་དེ་ལྟ་ན་ཨུཏྤ་ལའི་ཡང་ཡོད་པ་དང་རྫས་ལ་སོགས་པ་གསལ་བར༌[^1280]བྱེད་པ་ཉིད་དུ་མཐོང་བ་ཡིན་ནོ། །

[Block 1648]
གཞན་ཡང་། ཡོན་ཏན་རྫས་དག་གསལ་མི་འགྱུར། །ཡོན་ཏན་དང་རྫས་དག་ནི་དབྱིབས་མ་ཡིན་པའི་ཕྱིར་དེ་དང་འབྲེལ་པའི་སྤྱི་གསལ་བར་བྱེད་པ་མ་ཡིན་པར་ཐལ་བར༌[^1281]འགྱུར་རོ། །

[Block 1649]
གལ་ཏེ་ནུས་པའི༌[^1282]བྱེ་བྲག་གིས་རང་དང་སྤྱིའི་མཚན་ཉིད་གསལ་བར་བྱེད་པའི་ཕྱིར༌[^1283]རྫས་ལ་སོགས་པའི་ཐ་དད་ལ་ནི་དབྱིབས་ཀྱི༌[^1284]བྱེ་བྲག་ཡོད་པ་མ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། དངོས་པོ་ཐ་དད་ལ་ཡང་ནུས་པའི་བྱེ་བྲག་ཁས་བླངས་པའི་ཕྱིར་ཏེ་ཨུཏྤ་ལའི་དངོས་པོ་བཞིན་ནོ། །

[Block 1650]
གལ་ཏེ་གང་དག་སྤྱི་ཐ་དད་པ་མངོན་པར་གསལ་བའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བརྗོད་དོ་ཞེ་ན། དེ་ལ་བ་ལང་ཉིད་དང་རྟ་ཉིད་ལ་སོགས་པའི་བྱེ་བྲག་ཅི་ཞིག་ཡིན་ཞེས་བརྗོད་པར་བྱའོ། །
--- END BLOCKS ---
