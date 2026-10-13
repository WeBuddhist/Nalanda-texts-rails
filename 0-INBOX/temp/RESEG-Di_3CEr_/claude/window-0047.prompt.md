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

[Block 1651]
འདི་ལ་ཅི་ཞིག༌[^1285]བརྗོད་པར་བྱའོ།[^1286] །

[Block 1652]
རེ་ཞིག་བ་ལང་ལ་སོགས་པའི་རྗོད་པར་བྱེད་པའི་སྒྲར་བྱས་པ་དེ་དག་གི་སྒྲ་འདོད་རྒྱལ་བ་ལ་རང་རང་གི་སྒྲས་བརྗོད་པར་བྱ་བ་དེ་དག་ཁྱད་པར་ཡིན་ནོ། །

[Block 1653]
དེ་ལ།

[Block 1654 [VERSE]]
ཐ་དད་རྗོད་བྱེད་ཐ་དད་ལས། །
ཞེ༌[^1287]ན་རང་ལས་ཁྱད་མེད་སྒྲ། །

[Block 1655]
དེ་ལྟ་ན་ནི་སྤྱི་དང་བྱེ་བྲག་རྣམས་ཀྱི་སྒྲ་ཙམ་ཐ་དད་པ་ནི་དེའི་རང་བཞིན་མ་ཡིན་ནོ། །

[Block 1656]
གལ་ཏེ་ཁྱད་པར་མེད་པའི་དངོས་པོ༌[^1288]ལ་ནི་རྗོད་པར་བྱེད་པའི་སྒྲས་ཐ་དད་དུ་ཉེ་བར་འདོགས་སོ་ཞེ་ན། བརྗོད་པར་མི་བྱ་སྟེ། བྱེ་བྲག་ནི་སྤྱི་གསལ་བར་བྱེད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1657]
བ་ལང་ལ་སོགས་པ་ཁྱད་པར་མེད་པས་འགྱུར་བས་ནའོ། །

[Block 1658]
གལ་ཏེ་ནག་པ་ལ་སོགས་པ༌[^1289]བཞིན་རྗོད་པར་བྱེད་པ་ཐ་དད་པས་སོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་ཉིད་དཔྱད་པར་བྱ་བའི་ཕྱིར་ཏེ། གཅིག་ལ་ཡང་སྒྲའི་རྣམ་གྲངས་དུ༌[^1290]མ་བརྗོད་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1659]
འདི་ལ་ཇི་ལྟ་བ་བཞིན་དུ་སྒྲ་དག་རང་ལས་ཁྱད་པར་ཡོད་པ༌[^1291]མ་ཡིན་ནོ་ཞེས་འགྱུར་ཏེ། སྒྲ་ལ་ཡང་བ་ལང་ལ་སོགས་པ་དང༌[^1292]རང་ལས་བྱེ་བྲག་ཏུ་གྱུར་པ་ནི་མེད་ཀྱང་། འོན་ཀྱང་སྤྱི་ལས་བྱེ་བྲག་ཏུ་བྱས་པར་ཟད་ན་དེ་ལ་ནི་དེ་བཞིན་དུ་རྣམ་པར་བརྟག་གོ། །

[Block 1660]
གལ་ཏེ་མངོན་སུམ་ཉིད་བ་ལང་གི་སྒྲ་ལ་སོགས་པའི་བྱེ་བྲག་མ་ཡིན་ནམ་ཞེ་ན། མངོན་སུམ་ལ་བྱེ་བྲག་ཡོད་དུ་ཟིན་ཀྱང་དེ་ནི་བརྗོད་པར་བྱ་བ་མ་ཡིན་ཏེ། དོན་དང་ལྷན༌[^1293]ཅིག་མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1661]
ཤིང་རྟ་ལ་སོགས་པ་རྨོངས་པ་རྣམས་ཀྱི་ཐ་སྙད༌[^1294]ཀྱང་དོན་རྗོད་པར་བྱེད་པ་མ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་བས་ན་སྤྱི་ལས་སྒྲ་རྣམས་ལ་བྱེ་བྲག་ཏུ་བྱེད་པ་ཡིན་ནོ། །

[Block 1662]
བྱེ་བྲག་པ་རྣམས་ནི་རང་བཞིན་གྱིས་སྤྱི་རྣམས་ཀྱི་བྱེ་བྲག་ཡོད་པ་སྟེ། རང་རང་ལ་བརྟེན་པའི༌[^1295]སྤྱི་གསལ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 1663]
དེ་ཡང་ཇི་སྐད་དུ། མགོ་བོ་དང་རྒྱབ་དང་གསུས་པ་དང་ལག་པའོ་ཞེས་བྱ་བའི་བྱེ་བྲག་དེ་དག་ལས་སོ་ཞེས་ཟེར་རོ། །

[Block 1664]
དེ་དག་གི་ལྟར་ན་ཡང་།

[Block 1665 [VERSE]]
གསལ་བྱེད་གསལ་བ་ཐ་དད་ལ། །
ཕན་ཚུན་བརྟེན་པ་འཐོབ་པར་འགྱུར། །

[Block 1666]
ཕན་ཚུན་བརྟེན་པ་ཞེས་བྱ་བ་ནི་བཤད་པ་དེ་དག་འཐོབ་པར་འགྱུར་བ་སྟེ། རྫས་ཀྱི་རང་བཞིན་ཅི༌[^1296]ཞིག་རང་གི་ཅི་གསལ༌[^1297]བར་བྱེད་པ་ཉིད་དོ། །

[Block 1667]
སྤྱིའི་རང་བཞིན་ཅི༌[^1298]ཞིག་རང་གི་རྫས་ཀྱི༌[^1299]གསལ་བར་བྱ་བ་ཉིད་དོ་ཞེས་ནུས་པའོ།[^1300] །

[Block 1668]
གཞན་ཡང་། རང་བཞིན་དུ་མ་དང་གཅིག་གི །ཕན་ཚུན་གསལ་བ༌[^1301]མང་པོར་འགྱུར། །གསལ་བ་མང་པོ་ཞེས་བྱ་བ་ནི་མང་པོ་རྣམས་ཀྱི་གསལ་བ་དང་། མང་པོ་རྣམས་ཀྱི་གསལ་བ་སྟེ། རྫས་ནི་ཡོད་པ་ལ་སོགས་པ་སྤྱི་དུ་མའི་གསལ་བར་བྱེད་པའོ་ཞེས་སྤྱི་གཅིག་གི་རང་བཞིན་དུ་མར་བྱ་བ་དང་། ས་ལས་བྱུང་བ་ལ་སོགས་པའི་རྫས་དུ་མས་ཡོད་པ་རྣམས་ཀྱི་གསལ་བར༌[^1302]བྱེད་དོ་ཞེས་ཡོད་པ་རྣམས་ཀྱི་རང་བཞིན་དུ་མར་བྱ་བའོ།[^1303] །

[Block 1669]
འདི་ལ་རྣམ་པ་ཐམས་ཅད་དུ་ཡོན་ཏན་དང་འབྲེལ་པ་ཐ་དད་པའི་ཕྱིར་དང་། ནུས་པ་ཐ་དད་པའི་ཕྱིར་དང་། རྗོད་པར་བྱེད་པ་ཐ་དད་པའི་ཕྱིར་གཅིག་ཡིན་ཡང་། ཁས་བླངས་པའི་བདག་ཉིད་དུ་མ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1670]
ཡང་བརྗོད༌[^1304]པ།

[Block 1671 [VERSE]]
ཡོན་ཏན་ནུས་པ་རྗོད༌[^1305]བྱེད་ཀྱི། །
དབྱེ་བས་ཐ་དད་རབ་ཏུ་བརྟག །
གཅིག་མང་པོ་དང་འབྲེལ་པའི་ཕྱིར། །
དུ་མ་ཉིད་དུ་ཐལ་བར་འགྱུར། །

[Block 1672]
ཞེས་བྱ་བ་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 1673]
དེ་ལྟར་ན་རེ་ཞིག་གཞི་མཐུན་པ་ཉིད་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1674]
ཁྱད་པར་བྱེད་དང་ཁྱད་པར་དུ། །བྱ་ཉིད་རང་དབང་མིན་སྔར་བརྗོད། །

[Block 1675]
ཇི་ལྟར་དེ་དང་ལྡན་པར་བརྗོད་པ་ལ་ཁྱད་པར༌[^1306]བྱེད་པ་དང་ཁྱད་པར༌[^1307]བྱ་བ་ཉིད་མི་སྲིད་དོ།[^1308] །

[Block 1676]
དེ་ནི་སྔར་ཉིད་དུ་བརྗོད་ཟིན་ཏོ། །

[Block 1677]
དེ་ལྟ་བས་ན༌[^1309]

[Block 1678 [HEADING]]
#### དོན་གཞན་སེལ་བའི་སྒྲའི་དོན་ཉིད་ལ་གཞི་མཐུན་པ། ^5-7-3-0

[Block 1679]
དོན་གཞན་སེལ་བའི་སྒྲའི་དོན་ཉིད་ལ་གཞི་མཐུན་པ་དང་། ཁྱད་པར་བྱེད་པ་དང་། ཁྱད་པར་བྱ་བའི་དངོས་པོ་འཐད་པ༌[^1310]ཡིན་གྱི་དེ་ལས་གཞན་དུ་མ་ཡིན་ནོ། །

[Block 1680]
དེ་ལ་ཡང་།

[Block 1681]
གཞན་ཉིད་དུ་མིན་སྤྱི་དང་ནི། །ཐ་དད་རྣམ་གྲངས་བརྗོད་བསྐུལ་ཡིན། །

[Block 1682]
མཚུངས་སུ་ཟིན་ཀྱང་གཞན་ཉིད་དུ་ནི་མ་ཡིན་གྱི་སྤྱི་དང་ཁྱད་པར་དུ་བྱེད་པ་དང་། ཁྱད་པར་དུ་བྱ་བའི་རྣམ་གྲངས་ཀྱི་སྒྲ༌[^1311]རྣམས་ཀྱི་དོན་ལ་གཞན་སེལ་བའི་སྒྲ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། འགལ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1683]
རེ་ཞིག་རྣམ་གྲངས་ཀྱི་སྒྲ་ལ་ནི་ཅིག་ཅར་དུ་སྦྱོར་བར༌[^1312]བྱེད་པའི་ཕྱིར་གཞན་སེལ་བར་མཚུངས་པ་ཡིན་གྱི་རང་གི་དོན་སོ་སོར་སྤོང་བ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1684]
སྤྱིའི་སྒྲས་ཀྱང་རང་གི་ཐ་དད་པ་རྣམས་ལ་དོན་གཞན་སེལ་བ་ནི། ཐ་དད་ཀྱི་སྒྲ་ཆེད༌[^1313]ཆེར་མི་འཛིན་པ་ཡང་མ་ཡིན་ཏེ། དོན་དུ་གཉེར་བའི་ཕྱིར་རོ། །

[Block 1685]
འདི་ལྟར་ཤིང་ཤ་པ་ནི་པ་ལ་ཤ་ལ་སོགས་པ་མ་ཡིན་པ་དེ་བཞིན་དུ་བུམ་པ་ལ་སོགས་པ་ཡང་མ་ཡིན་ནོ། །
--- END BLOCKS ---
