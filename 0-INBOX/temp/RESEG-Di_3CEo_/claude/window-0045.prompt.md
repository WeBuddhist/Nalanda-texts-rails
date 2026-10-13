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
ངོས་རེ་རེ་ཞིང་དཔག་ཚད་ཉིས་སྟོང་ལྔ་བརྒྱ་པ། འཕང་དུ་དཔག་ཚད་ཕྱེད་དང་གཉིས་པ་དེ་ནི་རྒྱལ་པོའི་ཕོ་བྲང་ངོ་། །

[Block 1577 [VERSE]]
དེ་ནི་རྣམ་པར་རྒྱལ་བྱེད་དེ། །
ངོས་ལ་ཉིས་བརྒྱ་ལྔ་བཅུའོ། །

[Block 1578]
གྲོང་ཁྱེར་གྱི་དབུས་ན་རྣམ་པར་རྒྱལ་བྱེད་ཅེས་བྱ་བའི་ཁང་བཟངས་ངོས་དང་ངོས་ཀྱི་སྲིད་དུ་དཔག་ཚད་ཉིས་བརྒྱ་ལྔ་བཅུ་པ་ཞིག༌[^591]ཡོད་དོ། །

[Block 1579]
རེ་ཞིག་འདི་ནི་གྲོང་གི་མངོན་པར་དགའ་བ་ཡིན་ནོ། །

[Block 1580 [VERSE]]
ཕྱི་རོལ་ཤིང་རྟ་སྣ་ཚོགས་དང་། །
རྩུབ་འགྱུར་འདྲེས་ཚལ་དགའ་བས་བརྒྱན། །
ངོས་བཞིའི་ཚལ་བཞི་ནི་ལྷ་རྣམས་ཀྱིའོ། །
དེ་དག་གི་ནི་ཕྱོགས་བཞི་ན། །

[Block 1581]
ཉི་ཤུས༌[^592]བཅད་ན་ས་གཞི་བཟང་། སྐྱེད་མོས་ཚལ་དེ་དག་གི་ཕྱོགས་བཞིའི་དཔག་ཚད་ཉི་ཤུ་བཅད་པ་ན༌[^593]ས་གཞི་བཟང་པོའོ། །

[Block 1582]
གྲོང་ཁྱེར་གྱི་ཕྱི་རོལ་གྱི་ངོས་ཉིད་དུ།

[Block 1583 [VERSE]]
བྱང་ཤར་མཚམས་ན་ཡོངས་འདུ་སྟེ། །
ལྷོ་ནུབ་མཚམས་ན་ཆོས་བཟང་ངོ་། །

[Block 1584]
ཤིང་ས་བརྟོལ་ཡོངས་འདུ་ཞེས་བྱ་བ་ལྷ༌[^594]རྣམས་ཀྱི་འདོད་པའི་དགའ་བ་མཆོག་གི་གནས་གཅིག་ཡོད་དོ། །

[Block 1585]
གང་དུ་ལྷ་རྣམས་འཁོད་ནས་བྱ་བ་དང་། བྱ་བ་མ་ཡིན་པ་འགྲོ་བར་བྱེད་པ་ལྷའི་འདུན་ས་ཆོས་བཟང་ཞེས་བྱ་བ་ཡོད་དོ། །

[Block 1586]
རེ་ཞིག་དེ་ནི་ས་དང་འབྲེལ་པའི་ལྷ་རྣམས་ཀྱི་སྣོད་ཀྱི་གནས་པ་ཡིན་ནོ། །

[Block 1587]
དེ་སྟེང་ལྷ་རྣམས་གཞལ་མེད་ཁང་། །གང་དག་གི་སྣོད་མངོན་པ་ནི་མདོར་བསྡུ་ན། །འདོད་པ་སྤྱོད་པ༌[^595]དྲུག་ཡིན་ནོ། །

[Block 1588]
དྲུག་པོ་ཁོ་ན་འདོད་པ་དག་ལ་སྤྱོད་ཀྱི༌[^596]ལྷག་མ་རྣམས་ནི་མ་ཡིན་ནོ། །

[Block 1589]
དེ་དག་ཀྱང་།

[Block 1590 [VERSE]]
གཉིས་གཉིས་འཁྱུད་དང་ལག་བཅངས་དང་། །
དགོད༌[^597]དང་ལྟ་བས༌[^598]འཁྲིག་པ་ཡིན། །

[Block 1591]
ས་དང་འབྲེལ་པར་གནས་པ་རྒྱལ་ཆེན་བཞི་དང་། སུམ་ཅུ་རྩ་གསུམ་པ་རྣམས་ནི་མི་རྣམས་ཇི་ལྟ་བ་བཞིན་དུ་གཉིས་ཀྱིས་འཁྲིག་གོ། །

[Block 1592]
དེ་དག་ལ་ཡང་རླུང་བཏང་བས་ཡོངས་སུ་གདུང་བ་དང་འབྲལ་ལོ། །

[Block 1593]
ལྷག་མ་རྣམས་ནི་འཁྱུད་པ་ལ་སོགས་པ་གྲངས་བཞིན་དུའོ། །

[Block 1594]
ལྷའམ་ལྷ་མོ་གང་གི་པང་དུ་ལྷ་གཞོན་ནུའམ་ལྷའི་བུ་མོ་སྐྱེ་བར་འགྱུར་བ་དེ་ནི་གཉིས་ཀྱི་བུ་ཡང་ཡིན་ལ། བུ་མོ་ཡང་ཡིན་ནོ།[^599] །

[Block 1595]
བོང་ཚོད་ཇི་ཙམ་དུ་སྐྱེ་ཞེ་ན། བྱིས་པ་ལོ་ལྔ་ལོན་པ་ནས། ལོ་བཅུ་ལོན་པ་ལྟ་བུའི་བར་དེ་དག་ཏུ་སྐྱེ། ལྷའི་རིས་དེ་དག་ཏུ་གྲངས་བཞིན་དུའོ། །

[Block 1596]
གཟུགས་ཅན་རྣམས། ཀུན་རྫོགས་གོས་དང་བཅས་པ་ཉིད། །དེ་ལ།

[Block 1597 [VERSE]]
འདོད་པའི༌[^600]སྐྱེ་བ་གསུམ་པོ་ནི། །
འདོད་པའི་ལྷ་དང་མིར་བཅས་རྣམས། །

[Block 1598]
འདོད་པའི་ཁམས་སུ་རིག་པར་བྱ་སྟེ། དེ་ལ་འདོད་པའི༌[^601]ཉེ་བར་གནས་པ་རྣམས་ནི་མི་དང་ལྷའི་རིས་བཞི་རྣམས་སོ། །

[Block 1599]
འདོད་པ་རང་གིས་སྤྲུལ་པ་ནི་འཕྲུལ་དགའ༌[^602]བ་དག་གོ། །

[Block 1600]
འདོད་པ་གཞན་གྱིས༌[^603]སྤྲུལ་པ་ནི་གཞན་འཕྲུལ་དབང་བྱེད་པ་རྣམས་སོ།[^604] །

[Block 1601]
གཟུགས་ཀྱི་ཁམས་ན་ནི་བདེ་བ་སྐྱེ་བ་གསུམ་པོ་ནི། །བསམ་གཏན་གསུམ་ལས་ས་དགུ་ཡིན། །ལྷ་དེ་དག་ནི་དབེན་པ་ལས་སྐྱེས་པའི་བདེ་བ་དང་། ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པའི་དགའ་བའི་བདེ་བ་དང་། དགའ་བ་མེད་པའི་བདེ་བར་གནས་པ༌[^605]ཞེས་བྱ་བ་ནི་རིམ་པ་བཞིན་དུ་བདེ་བ་སྐྱེ་བ་དག་གོ། །

[Block 1602 [VERSE]]
ལྷའི་རིས་འདི་དག་གི་གནས་ནི། །
གནས་ནས་གནས་འོག་ཇི་སྲིད་པར། །
དེ་ནས་དེའི་གོང༌[^606]དེ་སྲིད། །

[Block 1603]
འདི་ལྟ་སྟེ། འདི་ནས་དཔག་ཚད་བཞི་ཁྲི་ན་རྒྱལ་པོ་ཆེན་པོ་བཞིའི་གནས་སོ། །

[Block 1604]
ཇི་སྲིད་དེ་དག་གི་བར་དེ་སྲིད་དུ་དེ་ནས་སྟེང་དུ་ནི་སུམ་ཅུ་རྩ་གསུམ་མོ། །

[Block 1605]
དེ་བཞིན་དུ་སུམ་ཅུ་རྩ་གསུམ་ནས༌[^607]འོག་ཏུ་འཛམ་བུའི་གླིང་ཇི་སྲིད་པར་གོང་མ་འཐབ་བྲལ་བ་རྣམས་ཀྱི་གནས་སུ་ཡང་དེ་སྲིད་དོ་ཞེས་རྒྱས་པར་དྲང་བར་བྱའོ། །

[Block 1606]
ཡང་ཅི་གནས་འོག་མར་སྐྱེས་པ་རྣམས་གོང་མའི་གཞལ་མེད་ཁང་དུ་དོང་ནས་མཐོང་བར་འགྱུར་རམ་ཞེ་ན།

[Block 1607 [VERSE]]
རྫུ་འཕྲུལ་གཞན་རྟེན༌[^608]མ་གཏོགས་པར། །
དེ་དག་གོང་མ་མཐོང་བ་མེད། །

[Block 1608]
རྫུ་འཕྲུལ་གྱིས་སམ། གཞན་ལ་བརྟེན་ནས་ཏེ་རྫུ་འཕྲུལ་དང་ལྡན་པའམ། །དེ་ན་གནས་པའི་ལྷས་ཁྲིད་པར་གྱུར་ན་སུམ་ཅུ་རྩ༌[^609]

[Block 1609]
གསུམ་པ་རྣམས་འཐབ་བྲལ་བའི་ནང་དུ་འགྲོ་བར་འགྱུར་ཏེ། ལྷག་མ་རྣམས་ཀྱང་དེ་དང་འདྲའོ། །

[Block 1610]
ཡང་འཐབ་བྲལ་བ༌[^610]ལ་སོགས་པའི་གཞལ་མེད་ཁང་བཞིའི་ཚད་ནི་རི་རབ་གྱི་རྩེ་མོ་ཇི་ཙམ་ཡོད་པ་དེ་ཙམ་མོ། །

[Block 1611]
གཞན་དག་ན་རེ་གོང་མ་ཉིས་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 1612]
བསམ་གཏན་དང་པོ་ནི་གླིང་བཞི་པ་ཙམ་མོ། །

[Block 1613]
བསམ་གཏན་གཉིས་པ་དག༌[^611]

[Block 1614]
གསུམ་པ་དང་།

[Block 1615]
བཞི་པ་ནི་སྟོང་ཆུང་ངུའི་དང་། སྟོང་གཉིས་པ་དང་། སྟོང་གསུམ་པའི་འཇིག་རྟེན་གྱི་ཁམས་ཙམ་མོ། །
--- END BLOCKS ---
