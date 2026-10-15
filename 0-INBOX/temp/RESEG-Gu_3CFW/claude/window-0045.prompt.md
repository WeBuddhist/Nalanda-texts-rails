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
[Block 1576]
དུས་གསུམ་པར་བྱིན་གྱིས་བརླབ་པའི་རུང་བའི་ཁང་པ་འདིའི་མིང་ནི་ལས་ཀྱི༌[^1366]མཐའ་ལས་བྱུང་བའི་ཞེས་བྱ་བའོ། །

[Block 1577]
བཞི་པ༌[^1367]ལ་ནི་ཇི་སྙེད་ཕྱིན་པ་དེ་སྙེད་ཀྱིས་རུང་བའི་ཁང་པ་ཉིད་དུ་བསྒྲག༌[^1368]པའི་ཚིག་ཅིག་ཅར་བརྗོད་པས་སོ་ཞེས་བྱ་བ་ལ། ཇི་སྙེད་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མ་ཐོབ་པ་རྣམས་ལ་མང་པོ་ཉིད་དུ་འཇུག་པར་འགྱུར་བས། མཉམ་པ་སྲིད་པ་ལ་བྱིན་གྱིས་བརླབ་པར༌[^1369]འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1578]
བཞི་པ་ལ་ནི་ཞེས་བྱ་བ་ནི་དུས་ལའོ། །

[Block 1579]
དེ་མ་ཡིན་པ་ལ་ལྷག་པར་གནས་པའི་ཕྱིར་དགེ་སློང་རྣམས་ཕྱིན་པ་ཞེས་བྱ་བ་དེ་ལའོ། །

[Block 1580]
ཅིག་ཅར་ཞེས་བྱ་བ་ལ་དགེ་སློང་ཕྱིན་པ་ཐམས་ཅད་ཀྱིས་གཞི་འདི་ནི་དགེ་འདུན་གྱི་རུང་བའི་ཁང་པར་འགྱུར་རོ་ཞེས་ཚིག་མཐུན་པར་ཅིག་ཅར་བར༌[^1370]བརྗོད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1581]
འདིར་ཆོ་ག་དང་སྔགས་མ་བརྗོད་པ་དེ་བས་ན་འདི་ལྟར་སྨོས་སོ། །

[Block 1582]
འདིའི་མིང་ནི་འཕྲལ་ལ༌[^1371]བྱུང་བའི་གནས་ཞེས་བྱའོ། །

[Block 1583]
དུས་གཞན་གྱི་ཚེ་ན་དགེ་སློང་གནས་པ་ཉིད་དང་མ་བྲལ་ལོ་ཞེས་བྱ་བའི་དུས་གསུམ་པ་འདི་ལ་ལས་གཅིག་པ༌[^1372]ཉིད་ཀྱིས༌[^1373]ཞེས་བྱ་བ་དེ་གནས་པར་རིག་པར་བྱའོ། །

[Block 1584]
གཅིག་གིས་གཙུག་ལག་ཁང་དུ་མའི་བྱ་བ་བྱེད་པ་ལ་མི་མཛེས་པ་མེད་པ་ཞེས་བྱ་བ་ལ་གཅིག་གིས་ཞེས་བྱ་བ་ནི་རུང་བའི་ཁང་པའོ། །

[Block 1585]
འདིར་གཞུང་ནི། བ་ལང་གི་གནས་པ་ལྟ་བུ་གང་ཞེ་ན། གཙུག་ལག་ཁང་ཐ་དད་པ་ན་གནས་པའོ་ཞེས་བྱ་བའི་དོན་དེ་འདིས་ཤེས་པའོ། །

[Block 1586]
དེ་ནི་ཐ་དད་པར་གྱུར་པའི་གནས་ཏེ་ཐ་དད་པ་དུ་མ་དག་ཏུ་རུང་བའི་ཁང་པ་གཅིག་ཏུ་གཙུག་ལག་ཁང་དུ་མའི་དེ་གནས་རྣམས་ཀྱིས་བྱ་བ་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་མི་མཛེས་པ་མ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 1587]
དེ་ནི་ཐ་དད་པར་གྱུར་པའི་རུང་བ་ཉིད་དུ་མ་བསྟན་ཏོ་ཞེས་བྱ་བ་ནི་དོན་གཞན་འདིས་དོགས་པ་ཡིན་ལ༌[^1374]འབྲེལ་བར་གནས་པའི་གཞི་ཐ་དད་པར་གྱུར་པ་གང་ཡིན་པ་དེས་སོ། །

[Block 1588]
བྱིན་གྱིས་མ་བརླབས་པར་ཡང་རུང་བ་ཞེས་བྱ་བ་གཞུང་འདིས་སྨོས་པ་དེ་བས་ན་དེའི་འདི་བཀག་པའོ། །

[Block 1589]
འདིར༌[^1375]ནི་དེ་མ་གསུངས་སོ་ཞེས་བྱ་བ་ཡང་ཅིའི་ཕྱིར་ངེས་པ་འདིར༌[^1376]ཡིན་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་གནས་ཀྱི་གཞི་ཡིན་ན། དེའི་ཕྱིར་ཐ་དད་པར་གྱུར་པའོ། །

[Block 1590]
འདི་བྱིན་གྱིས་བརླབ་པ་མེད་པ་རུང་བ་ཉིད་ལ་མི་སྦྱར༌[^1377]རོ། །

[Block 1591]
གལ་ཏེ་མ་ཡིན་ན་འདིར་མི་རུང་བ་ཉིད་དུ་ཐལ་བ་མེད་པའོ། །

[Block 1592]
གསོག་འཇོག་ཏུ་གྱུར་པ་ཟ་བ༌[^1378]དེ་བསལ་བའོ། །

[Block 1593]
གནས་པ་མ་ཡིན་པའི་གཞི་ལ་མི་སྤྲོ་བ་འདི་མཐོང་བ་མ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 1594]
ཡང་ཁ་ཅིག་ནི་འདི་སྐད་ཅེས་ཟེར་ཏེ། བ་ལང་གི༌[^1379]གནས་ཞེས་བྱ་བ་འདི་ལྟར་བརྗོད་པ་ཡིན་ཏེ། ཇི་ལྟར་ཡང་མཚམས་གཅིག་ཏུ་གཙུག་ལག་ཁང་རབ་ཏུ་མང་པོ་ཐ་དད་པ་དག་ཏུ་བཀོད་པར་གྱུར་ཅིང་།[^1380] དེ་རུང་བའི་ཁང་པ་གཅིག་ལ་བློ་མཐུན་པར་བྱས་ནས་གཙུག་ལག་ཁང་དེ་དག་ཐམས་ཅད་ཀྱི་རུང་བའི་ཁང་པ་གཅིག་ཁོ་ན་ཡིན་ཏེ་བ་ལང་གི་གནས་ལྟ་བུ་ཞེས་གསུངས་པ་ནི་ཁང་པ་གཅིག་ཁོ་ན་ཡིན་ནོ། །

[Block 1595]
པད་མའི་ཞེས་བྱ་བ་ཡན་ཆད་མུ་གེའི་ཚེའོ། །

[Block 1596]
མུ་གེའི་ཚེ་དགེ་སློང་གིས༌[^1381]བཙོས་པ་དག་དང་ལག་ཉེར་བླངས་པ་དང་། བྱིན་ལེན་མ་བྱས་པ་དག་བཟའ་བར་བྱའོ། །

[Block 1597]
ནང་དུ་བཙོས་པ་དང་ཞག་ལོན་པའོ། །

[Block 1598]
སྔ་དྲོ་བའི་ཟས་སོ་ཞེས་བྱ་བ་དེ་དག་ནི་ཟས་སྤངས་ནས་བཟའ་བ་དང་ཡང་ཡང་ཟ་བའི་གནང་བའོ། །

[Block 1599]
བཏུང་བ་ནི་དུས་ཐམས་ཅད་དུའོ་ཞེས་བྱ་བ་ནི་ལོ་ལེགས་པའི་དུས་སུ་ཡང་བཟའ་བར་བྱའོ།[^1382] །འདིར་གཞུང་ནི་སིལ་བུ་ལས་དེ་ལྟ་བས་ན་ཚེ་དང་ལྡན་པ་གྲོ་བཞིན་སྐྱེས་རྣ་བ་བྱེ་བ་ཉི་ཤུ་པ་ལ༌[^1383]བརྟེན་ཏེ། དེ་དགེ་འདུན་ཐམས་ཅད་ཀྱིས་གང་ཞིག་བཏུང་བ་བཏུང་བར་རྗེས༌[^1384]སུ་གནང་ངོ་ཞེས་གསུངས་པ་དེ་ཡིས་བསྡུས་པ་འདི་ཡིན་ནོ། །

[Block 1600]
དེ་ཡང་སྤངས་པ་ཟ་བ་དང་ཡང་ཡང་ཟ་བ་བག་ཡངས་སུ་གནང་བར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1601]
སྔར་བྱིན་ལེན་བྱས་པ་སྤངས་ཏེ་ལངས་པས་སོ་ཞེས་བྱ་བ་ནི་སྔར་བྱིན་ལེན་བྱས་པ་གང་ཡིན་པ་དེ་སྤངས་ཏེ་ལངས་པས་བཟའ་བར་བྱའོ། །

[Block 1602]
དེ་བླང་བར་བྱ་བའི་ཕྱིར་ལྡང༌[^1385]བར་བྱའོ་ཞེས་བྱ་བ་ནི་སྔར་བྱིན་ལེན་བྱས་པ་དེ་བླང་བར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1603]
འདི་ནི་ཟས་བརྩམས་པས་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི༌[^1386]དེའི་བག་ཡངས་སུ་བྱ་བ་ཡིན་ནོ། །

[Block 1604]
ལྷག་མའོ༌[^1387]ཞེས་བྱ་བ་ནི་དེས་བཟའ་བར་བྱ་བའི་ཕྱིར་སྟ་གོན་བྱས་པ་གང་ཡིན་པ་དེ་ལས་ལྷག་མ་ཡོད་པ་དེ་གང་ཡིན་པ་དེ་དགེ་སློང་སྤངས་ཏེ་ལངས་པས་བཟའ་བར་བྱའོ། །

[Block 1605]
མངོན་པར་བསྒྲུབ་པོ་ཞེས་བྱ་བ་ནི་གཞག་པའི་གནས་པས་དྲངས་པ་སྤངས་ཏེ་ལངས་པས་བཟའ་བར་བྱའོ། །

[Block 1606]
ལྷག་མ་དེ་འབྱུང་བ་གང༌[^1388]གིས་མི་རིགས་པ་གང་ཞིག་གི་འདོད་པ་དེ་ལ་བརྗོད་པར་བྱ་སྟེ། དེས་བསྒྲུབ་པར་བྱའོ། །

[Block 1607]
གཞན་ཡང་གནང་བ་དེའི་ཕྱིར་ནགས་ཀྱི་རུས་པའོ༌[^1389]ཞེས་བྱ་བ་སྨོས་ཏེ། སྤངས་ཏེ་ལངས་པ་ལས་བཟའ་བར་བྱའོ། །

[Block 1608]
ནགས་ཀྱི་རུས་པ་ཞེས་བྱ་བ་ནི་དཔེར་ན་ཤའི་རུས་པ་ནི་རུས་པ་དག་ཡིན་པ་དེ་བཞིན་དུ་ནགས་ཀྱི་ཤིང་དག་ནི༌[^1390]རུས་པ་ཅན་དག་ཡིན་པས་དེའི་ཕྱིར་ཤིང་ཐོག་རུས་པ་ཅན་ནི༌[^1391]ནགས་ཀྱི་རུས་པ་ཡིན་ནོ། །

[Block 1609]
ཤ་གན་དྷ་ལ་སོགས་པ་ལྟར་གཞན་གྱི་གཟུགས་སོ། །

[Block 1610]
ཡང་ནགས་ཀྱི་རུས་པ་ཞེས་བྱ་བ་ཅི་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འདི་ལྟ་སྟེ་རྒུན༌[^1392]དང་བལ་པོ་སེའུ་དང་། འབྲ༌[^1393]གོ་དང་སྟར༌[^1394]ཀ་དང་པ་ཏ༌[^1395]མ་དང་། ཨུ་རུ་མའི་ཀ་དང་ཀུ་རུ་མའི་ཀ་དང་ཁམ་བུ་དང་རྒྱ་ཤུག་དང་ས་ར་དག༌[^1396]ནི་དེ་ཞེས་བྱ་བའོ། །

[Block 1611]
པདྨའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཡང་ནགས་ཀྱི་རུས་པ་ཡིན་ཏེ། སྤངས་ཏེ་ལངས་པས་བཟའ་བར་བྱའོ། །

[Block 1612]
འདིར་ཐམས་ཅད་དུ་ལྷག་མའོ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྤངས་ཏེ་ལངས་པས་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 1613]
པདྨ་ཞེས་བྱ་བ་དེ་ཅི་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འདི་ལྟ་སྟེ་པདྨའི་རྩ་བ་དང་། པདྨའི་རྩ་ལག་དང་བེ་ཊ་དང་། ཨུཏྤ་ལའི་རྩ་བ་དང་པདྨའི་སྙིང་པོ་དག་ནི་དེ་ཞེས་བྱའོ་ཞེས་སྨོས་སོ། །

[Block 1614]
གཞིར་གཏོགས་པའི་སྨན་གྱི་གཞིའོ།། །།

[Block 1615]
དེ་ལ་རེ་ཞིག་འབྲེལ་པ་བསྟན་པར་བྱ་སྟེ། བཀྲེས་པ་དང་སྐོམ་པ་དག་ནི་ནད་དང་འདྲ་བ་མ༌[^1397]ཡིན་ཏེ། དེ་བས་ན་དེ་དག་གི་གཉེན་པོར་གྱུར་པ་འཚོ་བ་ཙམ་སྒྲུབ་པར་བྱེད་པ་བཟའ་བར་བྱ་བ་དང་། བཏུང་བར་བྱ་བ་དུས་སུ་རུང་བའི་སྨན་གྱི་ཆོས་ཁོངས་སུ་གཏོགས་པ༌[^1398]ཉིད་གང་ཡིན་པ་དེ་དག་གི་འདུ་བའི་སྒོ་བསྟན་པའི་ཕྱིར། རྒྱལ་སྲིད་དང་དེའི་ཕྱེད་ནོད༌[^1399]པར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་དེའི་ཞེས་བྱ་བ་ནི་རྒྱལ་སྲིད་དེའོ། །
--- END BLOCKS ---
