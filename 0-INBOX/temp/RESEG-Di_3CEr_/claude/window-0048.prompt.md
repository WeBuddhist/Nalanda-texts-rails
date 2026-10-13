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

[Block 1686]
དེ་དག་གིས་ནི་སྤྱི་མ་ཡིན་པ༌[^1314]སྒྲའི་དོན་གཞན་སྤོང་བ་ལ་ལན་བརྗོད་པ་ཡིན་ནོ། །

[Block 1687]
དེ་བཞིན་དུ་སྤྱིའི་སྒྲ་རང་གི་འདོད་པའི་དོན་གྱི་ཡུལ་ཉེ་བར་འགོད་པར་བྱེད་པ་ན་ཁྱད་པར་དུ་བྱེད་པ་རྣམས།[^1315] ཁྱད་པར་དུ་བྱ་བའི་སྒྲ་ལ་ཇི་ལྟར་ན་མི་ལྟོས་པ་ཡིན། །དེ་བཞིན་དུ། འགལ་མེད་ཕྱིར་ན། ཚོགས་སྤྱི༌[^1316]ལ་སོགས་པའི་སྒྲའི་དོན་ལ་གཞན་སེལ་བ་སླར་ཡང་མི་རིགས་པ་མ༌[^1317]ཡིན་ནོ། །

[Block 1688]
ཚོགས་པ་ཡང་། དེ་བཞིན་དོན་གཞན་རྗོད་པར་བྱེད། །དེ་བཞིན་དུ་སྤྱི་དང་ཁྱད་པར་གྱི་སྒྲ་དག་གི་རང་གི་དོན་ལ་སྤྱི་ལ་འཇུག་པར་བྱེད་པས་ན་གཉིས་སམ་མང་པོ་ཡང་རུང་སྟེ། དེས་ཁྱད་པར་དུ་བྱས་པའི་དོན་གཞན་རྗོད་པར་བྱེད་པ་ཉིད་དུ་འཐད་པ་ཡིན་ཏེ། སྔར་ཇི་སྐད་དུ་བརྗོད་པ་བཞིན་ནོ། །

[Block 1689]
ཡང་བརྗོད་པ།

[Block 1690 [VERSE]]
དེ་ཙམ་འདོད་པའི་ཕྱིར་ཐ་དད། །
རང་དང་སྤྱི་ཡིས་བར༌[^1318]མ་ཡིན། །
མ་བཟུང་ན་ནི་དོན་གཅིག་ལ།
འདི་དག་ཐེ་ཚོམ་བསྐྱེད་པར་མཚུངས། །

[Block 1691 [VERSE]]
དུས་མ་ཡིན་དུ་ཟིན་ཀྱང་སྤྱི། །
བཟུང་ན་ཐ་དད་ཀྱིས་མི་འཁྲུལ། །
ཁྱད་པར་བྱེད་དང་ཁྱད་པར་དུ། །
བྱ་བ་དེ་དག་ཉིད་མཚུངས་མིན། །

[Block 1692]
ཞེས་བྱ་བ་བསྡུ་བའི་ཚིགས་སུ་བཅད་པ་དག་གོ། །

[Block 1693 [HEADING]]
### ཐ་དད་པའི་སྒྲའི་དོན་གཞན་སེལ་བར་བྱེད་པའི་རྒྱུ། ^5-8-0

[Block 1694]
ཅི་ཡང་རྒྱུ་གང་གིས་ན༌[^1319]ཐ་དད་པའི་སྒྲའི་དོན་གཞན་སེལ་བར་བྱེད་ཅེ་ན།

[Block 1695 [VERSE]]
ཐ་དད་ཐ་དད་གཞན་རྣམས་དང་། །
འགལ་བའི་ཕྱིར་ན་སེལ་བར་བྱེད། །

[Block 1696]
ཐ་དད་པའི་དོན་གྱི་སྒྲ་ནི་རང་དང་སྤྱིའི་དོན༌[^1320]དབང་དུ་བྱེད་པའི་ཕྱིར་རྒྱལ་པོའི་བུ་བཞིན་ཕན་ཚུན་དུ་འགལ་བ་ཉིད་ཡིན་ནོ། །

[Block 1697]
དེའི་ཕྱིར་དོན་གཞན་གྱིས༌[^1321]བཟོད་པར་མི་ནུས་ཏེ། དཔེར་ན༌[^1322]ཤིང༌[^1323]ཤ་པ་ཡིན་ནོ་ཞེས། ཤིང་ཤ་པའི་སྒྲ་ཤིང་དང་ལྷན་ཅིག་ཏུ་སྦྱར་བས་སེང་ལྡེང་ལ་སོགས་པའི་ཤིང་རྣམ་པར་སྤྱད༌[^1324]ནས་རང་གི་ཡུལ་དུ་ཉེ་བར་འཇོག་པར་བྱེད་པ་བཞིན་ནོ། །

[Block 1698]
དེ་བཞིན་དུ་ཅིག་ཤོས་ལ་ཡང་སྟེ། དེ་བཞིན་དུ་རེ་ཞིག་ཐ་དད་པའི་སྒྲ་ལ་རྫས་གཅིག་བཏང་སྙོམས་སུ་བྱེད་པའི་ཕྱིར་ཁྱད་པར་དུ་གཞན་གྱི་སྒྲའི་དོན་སེལ་བར་རིགས་པ་ཡིན་ནོ། །

[Block 1699]
གལ་ཏེ་བུམ་པ་ལ་སོགས་པ་དང་མ་འབྲེལ་པའི་སྤྱི་གཞན་ཐ་དད་པའི་དོན་ལ་ཅི་ལྟར་སེལ་བར་བྱེད་ཅེ་ན། འདི་ལྟར།

[Block 1700]
སྤྱི་གཞན་ཐ་དད་དོན་རྣམས་ཀྱི། །རང་དང་སྤྱི་དག་འགལ་བ་ཡིན། །

[Block 1701]
ཤིང་གི་སྒྲས་ནི་བུམ་པ་ལ་སོགས་པའི་ས་ལས་བྱུང་བ༌[^1325]དབང་དུ་བྱས་པའི་ཕྱིར་འགལ་བ་ཡིན་ནོ། །

[Block 1702]
དེས་ན་དེས་སྤང་བར་བྱ་བའི་དངོས་པོ་ལ་གྲོགས་པོའི་སྒྲ་བཞིན་རྗེས་སུ་ཡི་རང་བར་བྱེད་དོ། །

[Block 1703]
དོན་ལ་ཡང་དེ་དེས་སྤངས༌[^1326]སོ་ཞེས་ཤེས་པར་བྱའོ། །

[Block 1704]
དེ་དག་གིས་ནི་སྤྱི་གཞན་གྱི་ཐ་དད་པ་རྣམས་དང་། ཡོན་ཏན་ལ་སོགས་པ་རྣམས་དང་། དེའི་བྱེ་བྲག་རྣམས་གཟུགས་ལ་སོགས་པ་དང་། འབྲེལ་པ་ཅན་དང་འབྲེལ་པ་ཅན་མ་ཡིན་པ་ཡང་གྲོགས་པོ་དང་གྲོགས་པོའི་སྒྲ་བཞིན་དང་། སེལ་བར་བྱེད་པ་དང་། བཏང་སྙོམས་སུ་བྱེད་པར་རིག་པར་བྱའོ། །

[Block 1705]
དེ་ལ་ཡང་། དེ་དེའི༌[^1327]དངོས་སུ་བསིལ༌[^1328]བྱིམ་ན། །ཤིང་ཤ་པའི་སྒྲས་བུམ་པ་ལ་སོགས་པ་དངོས་སུ་སེལ་བར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1706]
[^1329]ཅིའི་ཕྱིར་ཞེ་ན། སྤྱི་ནི་མཚུངས་པ་ཉིད་མ་ཡིན། །གལ་ཏེ་དངོས་སུ་སེལ་བར་བྱེད་ན་ནི། ཤིང་གི་སྒྲ་དང་དོན་མཚུངས་པར་འགྱུར་རོ། །

[Block 1707 [VERSE]]
དེ་བཞིན་ཁྱད་པར་གཞན་རྣམས་ནི། །
དེ་ཡིས་སེལ་བར་འགྱུར་མ་ཡིན། །

[Block 1708]
ཇི་ལྟར་ཤིང་གི་སྒྲས་པ་ལ་ཤ་ལ་སོགས་པ་སེལ་བར་མི་བྱེད་པ་དེ་བཞིན་དུ་ཤིང་ཤ་པའི་སྒྲས་ཀྱང་སེལ་བར་མི་བྱེད་དེ། དེས་མཚུངས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1709]
གལ་ཏེ་ཉེས་པ་མེད་དེ་ཉུང་ངུ་དང་མང་པོར་སེལ་བ་ཉིད་ཀྱིས་ཐ་དད་པའི་ཕྱིར་རོ༌[^1330]ཞེ་ན། དེ་ལྟར་འགྱུར་བར་རིགས་པ་མ་ཡིན་ཏེ། ཇི་ལྟར་ཤིང་དང་ཤིང་ཤ་པའི་སྒྲ་དག་ནི། ཤིང་ཉིད་དང་ཤིང་ཤ་པ་ཉིད་ཀྱིས་བྱེ་བྲག་ཏུ་བྱས་པའི་དངོས་པོ་རྗོད་པར་བྱེད་པའི་ཕྱིར། ཤིན་ཏུ་ཐ་དད་པའི་དོན་རྗོད་པར་བྱེད་དོ། །

[Block 1710]
དེ་བཞིན་དུ༌[^1331]འདི་ལ་ཡང་དོན་མ་འདྲེས་པར་བྱ་བ་འབྱུང་སྟེ། ཉུང་ངུ་དང་མང་པོར་སེལ་བ་ཞེས་པ་ནི་དོན་ལ་ཡང་འགྱུར་རོ། །

[Block 1711]
གལ་ཏེ་ཁྱད་པར་གཞན་གྱི་དོན་སེལ་བར་བྱེད་པ་ཡིན་ན་ནི་གང་འདི་ཡོན་ཏན་དང་ཡོན་ཏན་གཞན་གྱིས་གཞི་མཐུན་པ་སྟེ། རོ་མངར་པ་ལ་སྣུམ་པ་དང་། བསིལ་བ་དང་། ལྕི་བ་ཉིད་དོ་ཞེས་པ་དེ༌[^1332]ཇི་ལྟར་ཞེ་ན། འདི་ལ་འགལ་བ་ཡོད་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར།

[Block 1712 [VERSE]]
གང་ཞིག་གཞི་མཐུན་གྱུར་པ་སྟེ།[^1333] །
ཡོན་ཏན་དང་ནི་ཡོན་ཏན་གཞན། །
དེ་རྫས་གཅིག་ལ་འཇུག་པའི་ཕྱིར། །
གཞི་ཡི་མི་འགལ་བར་བྱས་ཉིད། །

[Block 1713]
རྫས་ཡོད་པ༌[^1334]ལ་ནི། རོ་མངར་བ་ལ་སྣུམ་པ་ཉིད་ལ་སོགས་པའི་ཡོན་ཏན་ཉེ་བར་འདོགས་པར་བྱེད་དོ། །

[Block 1714]
དོན་གཅིག་ལ་འཕྲོད་པ་འདུ་བའི་ཕྱིར་ཞེས་པའི་ཉེས་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1715]
མ་མཐོང་ཕྱིར་ཡང་སེལ་བ་ཡིན། །གང་གི་ཕྱིར་ཐ་དད་ཀྱི་སྒྲ་ཐ་དད་པའི་དོན་གཞན་ལ༌[^1335]མཐོང་བ་དེའི་ཕྱིར་ཡང་སེལ་བ་ཉིད་དོ། །

[Block 1716]
ཅི་སྟེ་གང་གི་ཕྱིར་ན་མ་མཐོང་ངོ་ཞེས་བྱ། དངོས་པོའི་དོན་ལ་ནི་ཁོ་བོ་ཅག་གི༌[^1336]ང་རྒྱལ་ཙམ་གྱིས་ཆོག་པར༌[^1337]འཛིན་པའི་འཇུག་པ་བཀག་པའི་ཕྱིར་རོ། །

[Block 1717]
དེ་ལྟ་ན་ནི། རང་ཐ་དད་ལ་སྤྱི་སེལ་འགྱུར། །གལ་ཏེ་མ་མཐོང་བ་ལས་སེལ་བར་བྱེད་ན་སྤྱིའི་སྒྲ་ཡང་རང་རང་གི༌[^1338]ཐ་དད་པ་རྣམས་ལ་མ་མཐོང་ངོ་ཞེས་གཞན་སེལ་བར་ཐལ་བར་འགྱུར་རོ། །

[Block 1718]
གཞན་མིན་རིགས་པར་མཐོང་བའི་ཕྱིར། །མཐོང་ཞེས་པ་ནི་སྐབས་ལ་སོགས་པ་སྤྱིའི་སྒྲ་ལས་བྱེ་བྲག་སྤོང་བར་རོ། །

[Block 1719]
དེ་ལྟ་དེ་སྣང་ལ་ཐེ་ཚོམ། །དེ་ལྟར་བྱས་ན་ནི་སྤྱིའི་སྒྲ་དེ་བྱེ་བྲག་གི་སྣང་བ་ལ་ཐེ་ཚོམ་ཟ་བར་རིགས་པ་ཡིན་ནོ། །

[Block 1720]
གལ་ཏེ་དེ་རྣམས་ལ་ཡང་སྔར་དམིགས་པ་ཡིན་ན་ནི་རེ་ཞིག་འགྲེང་བ་ལ་ཡང་། ཐེ་ཚོམ་ཟ་བར་རིགས་ཤེ་ན། འདི་སྙམ་དུ་གལ་ཏེ་སྐབས་ལ་སོགས་པ་དང་དོན་དག་ལྷན་ཅིག་དམིགས་པ་ཡིན་ན་ནི་དེའི་ཕྱིར་ཇི་ལྟར་ན་ཐེ་ཚོམ་ཟ༌[^1339]ཞེ་ན། ངེས་པར་ཡན་གར་བ་ལ༌[^1340]ཞེས་དེ་ལྟར་དུ་བརྗོད་པར་མི་བྱ་སྟེ། དེ་ལ་སོགས་པ་དང་ལྡན་པའི་ཐེ་ཚོམ་ཟ་བ༌[^1341]ནི་དོན་ལ་སོགས་པ་དང་ལྡན་པར་ངེས་པ་ལ་དུས་ཕྱིས་ཡན་གར་བ་ལས༌[^1342]ཐེ་ཚོམ་ཟ་བ་ཡིན་ནོ། །
--- END BLOCKS ---
