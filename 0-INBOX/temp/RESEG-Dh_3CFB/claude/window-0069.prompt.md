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
[Block 2416]
དེ་བས་ན་རྒྱུ་གཞན་དང་ལྡན་པའི་ཡི་གེ་དེ་དག་ནི་རང་གི་རྒྱུའི་གོ་རིམས་བཞིན་དུ་སྐྱེ་བ་ཅན་ཡིན་ནོ། །

[Block 2417]
ཐོས་པའི་དུས་སུ་ཡང་གང་གི་ཚེ་ངལ་བར་འཇུག་པ་ཅན་ཡི་གེ་སྔ་མ་ཤེས་པའི་ལྷན་ཅིག་བྱེད་པའི་རྐྱེན་ལ་ལྟོས་པ་ཅན་དག་གིས་རང་གི་ཤེས་པ་སྐྱེད་པར་བྱེད་པ་དེའི་ཚེ། སྔ་མ་དྲན་པ༌[^1654]ལྟོས་པ་ཉིད་ཀྱིས་དྲན་པ་སྐྱེད་པར་བྱེད་དོ། །

[Block 2418]
རྒྱུ་དང་འབྲས་བུ་ཐ་དད་པ་ཅན་གྱི་རྐྱེན་ལས་བྱུང་བའི་ཆོས་ཅན་དང་། ཐ་དད་པར་བསྐྱེད་པའི་ཆོས་ཅན་དེ་དང་དེ་ནི་ཡི་གེ་རྣམས་ཀྱི་རང་བཞིན་ཡིན་ཏེ། སྐྱེས་བུས་འདུས་བྱས་པའི་ཁྱད་པར་གྱིས་ཐ་དད་པ་ནི་གོ་རིམས་ཞེས་བརྗོད་དོ། །

[Block 2419 [VERSE]]
དེ༌[^1655]ཕྱིར་ཡི་གེའི་ངོ་བོ་དེ། །
ཚིག་དང་ཚིག་ལ་གཞན་ཉིད་དེ། །
བྱེད་པའི་འདུ༌[^1656]བྱེད་ལས་ཐ་དད། །
འབྲས་བུའི་ཁྱད་པར༌[^1657]ལྷན་ཅིག་བྱེད། །

[Block 2420]
དེ་བས་ན་ཚིག་དག་ལ་ཡི་གེ་རྣམས་ཀྱི་རང་བཞིན་གཅིག་ཉིད་མ་ཡིན་ཏེ། བྱེད་པ་པོའི་སེམས་ཀྱི༌[^1658]འདུས་བྱས་པའི་ཁྱད་པར་གྱིས་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 2421]
དེ་ཕན་ཚུན་ལྷན་ཅིག་པ་ན་འབྲས་བུའི་ཁྱད་པར་གྱི་རྒྱུ་ཡིན་ནོ། །

[Block 2422 [VERSE]]
ཡི་གེ་རྣམས་ཀྱི་གོ་རིམས་དེའང་། །
རྩོམ་པར་བྱེད་ལས་འཇུག་ཡིན་ཏེ། །
འདོད་པས་མི་འགལ་གྲུབ་ཅན་གྱི། །
གནས་པའི་གོ་རིམས་འགལ་ཕྱིར་རོ། །

[Block 2423]
རྒྱུ་དང་འབྲས་བུར་གྱུར་པའི་རྐྱེན་ལས་བྱུང་བའི་རང་བཞིན་གྱི་ཁྱད་པར་ཡི་གེ་རྣམས་ཀྱི་གོ་རིམས་ཡིན་ནོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2424]
དེ་ཡང་སྐྱེས་བུའི་རྟོག་པ་དང་དཔྱོད་པས་བྱས་པ༌[^1659]ཡིན་པའི་ཕྱིར། གནས་པ་ཅན་གྱི་གོ་རིམས་ཡི་གེ་མ་ཡིན་ཏེ། འདོད་པས་མི་འགལ་བ་གྲུབ་པ་ཅན་གྱི་གོ་རིམས་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་ཏེ། ལས་ཀྱི་ཁྱད་པར་གྱི་གོ་རིམས་བཞིན་ནོ། །

[Block 2425]
ཡུལ་དང་དུས་དག་ཏུ་གནས་པའི་གོ་རིམས་ཅན་རི་གངས་ཅན་དང་། འབིགས་བྱེད་དང་། མ་ལ་ཡའམ། ས་བོན་དང་མྱུ་གུ་ལ་སོགས་པ་དག་རང་གི་འདོད་པས་གོ་རིམས་ཀྱི༌[^1660]བཀོད་པ་བྱ་བར་ནུས་པ་མ་ཡིན་ནོ། །

[Block 2426]
དེ་ཉིད་ཀྱི་ཕྱིར་སྐྱེས་བུའི་ཆོས་སུ་བགྲང་བའི་རྣམ་པར་རྟོག་པའི་གོ་རིམས་ཡོད་ན་ཡོད༌[^1661]པའི་ཕྱིར་དང་།

[Block 2427 [VERSE]]
མེད་ན་མེད་པའི་ཕྱིར་རོ། །
སྐྱེས་བུ་དང་ནི་ཡིག་གོ་རིམས། །
རྒྱུ་དང་འབྲས་ཉིད་གྲུབ་པའི་ཕྱིར། །
སྐྱེས་བུས་ཡིག་ཀུན་གོ་རིམས་ཏེ། །

[Block 2428]
མེ་དང་ཤིང་གི་རིགས་བཞིན་ནོ། །

[Block 2429]
ཤིང་ཡོད་ན་མེ་བྱུང་བའི་ཕྱིར་དང་། མེད་ན་མེད་པའི་ཕྱིར་རོ། །

[Block 2430]
མེ་ཤིང་མ་མཐོང་བ་ཅན་ཡང་ཤིང་མེད་པ་ཅན་མ་ཡིན་ཏེ། དེའི་ཡུལ་དང་དུས་ཀྱི་ངེས་པ་མི་རུང་བའི་ཕྱིར་དང་། ངེས་པ་ཡོད་ན་ནི་དེ་ཉིད་ཤིང་ཡིན་པའི་ཕྱིར་དང་། ཤིང་ནི་མེའི་ཉེ་བར་ལེན་པའི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2431]
དེ་བཞིན་དུ་ཡི་གེའི་གོ་རིམས་འདི་ཡང་གལ་ཏེ་སྐྱེས་བུའི་རྣམ་པར་རྟོག་པ་ལ་ལྟོས་པ་མེད་པ་ཡིན་ན། དམིགས་པ་མེད་པར་རང་ཉིད་གསལ་བ་ཡིན་ན་འབད་པས་ཀྱང་མི་ནུས་ཏེ། དེ༌[^1662]རབ་ཏུ་ཕྱེ་བ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2432]
ལ་ལར་ནུས་ན་ནི་ཐམས་ཅད་དེ་ལྟར༌[^1663]འགྱུར་ཏེ། ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 2433]
དེ་ཡོད་པའི་ངང་ཚུལ་ཅན་དེ་དང་ཁྱད་པར་མེད་པས་དེས་མ་བྱས་པ་ཡིན་ན་ཡང་། ཐམས་ཅད་ལ་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོ་ཡང་གསལ་བར་འགྱུར་ཏེ། དེ་ནི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པའི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2434]
[^1664]མཚན་ཉིད་གཞན་བརྗོད་པར་བྱའོ། །

[Block 2435]
བུམ་པ་ལ་སོགས་པའི་དངོས་པོ་ཐམས་ཅད་ཀྱང་བཅོས་མ་དང་། བཅོས་མ་མ་ཡིན་པ་ཐོབ་པར་འགྱུར་ཏེ། དེ་ལ༌[^1665]ཡང་དེ་ལྟ་བུའི་རྣམ་པར་རྟོག་པ་སྲིད་པའི་ཕྱིར་དང་། ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 2436]
དེ་དག་ཀྱང་གཞན་མེད་པ་མཐོང་བ་སྔོན་དུ་སོང་བ་ཉིད་ཀྱིས་གཞན་བྱེད་པ་དང་འགའ་ཞིག་བྱེད་པ་པོ་མི་ཤེས་པ་དེ་ལྟར་ན་ཐམས་ཅད་དམ་འགའ་ཞིག་ཀྱང་བྱས་པ་མ་ཡིན་པར་མངོན་པར་ཞེན་པར་འགྱུར་རོ། །

[Block 2437]
དེ་བས་ན། ཡི་གེའི་གོ་རིམས་འདི་ནི་རབ་ཏུ་གྲགས་པ༌[^1666]དང་འབྲས་བུར་ཡོད་པ་ཅན་གྱི་དངོས་པོའི་ཆོས་ལས་མ་འདས་པའི་ཕྱིར་ཐམས་ཅད་སྐྱེས་བུས་བྱས་པ༌[^1667]ཉིད་ཡིན་ནོ། །

[Block 2438]
དེ་ཉིད་ཀྱི་ཕྱིར།

[Block 2439 [VERSE]]
ཤེས་མཐུ་དག་གིས་སྔགས་ཤེས་པའི། །
གོ་རིམས་བྱེད་ཚུལ་ཅན་སྐྱེས་བུའི། །
ཐུན་མོང་མིན་པ༌[^1668]ཉིད་གྲུབ་སྟེ། །
གཞན་ལ་དེ་དག་མེད་པའི་ཕྱིར། །

[Block 2440]
གལ་ཏེ་གཞན་གྱིས་ཀྱང་ཡི་གེའི༌[^1669]གོ་རིམས་འདིས་ནི་དུག་བཅོམ་པ༌[^1670]ལ་སོགས་པ་ནུས་པ་ཡིན་གྱི། གཞན་ནི་མ་ཡིན་ནོ་ཞེས་ཤེས་པར་འགྱུར་བ་དེ་དེ་ཁོ་ན་བཞིན་དུ་རྟོགས་པར་འགྱུར་ན་དེ་ལྟར་ནི་མ་ཡིན་ནོ། །

[Block 2441]
དེ་བས་ན་གོ་རིམས་འདི་ནི་ངོ་བོ་ཉིད་ཀྱིས་འབྲས་བུ་བྱེད་པ་ཉིད་ཡིན་ན་ཡང་། འགའ་ཞིག་གིས་རྣམ་པར་ཤེས་པའི་ཕྱིར། ལྐོག་ཏུ་གྱུར་པ་མཐོང་བའི་སྐྱེས་བུ་ཡོད་དོ། །

[Block 2442]
འདིས་ནི་དོན་བྱེད་ནུས་ཀྱི་འདིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ༌[^1671]ཤེས་པར་མི་ནུས་ཏེ། རྟགས་ཀྱི་ཁྱད་པར་མ་འཆོལ་བ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2443]
མངོན་སུམ་གྱིས་ཀྱང་སྔགས་དང་སྔགས་མ་ཡིན་པ་མ་བསྟན་པ་དག་ཡོངས་སུ་ཤེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2444]
བསྟན་དུ་ཟིན་ཀྱང་རྣམ་པ་འགའ་ཞིག་གིས་རང་བཞིན་གྱི་ཁྱད་པར་མི་ཤེས་པའི་ཕྱིར་དང་། གཞན་དུ་འབྲས་བུ་མི་སླུ་བའི་ཕྱིར་དང་། དེ༌[^1672]ཡང་བྱེད་པ་ལས་སྔར་མཐོང་བར་མི་ནུས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2445]
གོ་རིམས་འདི་ནི་ངོ་བོ་ཉིད་ཀྱིས་བྱེད་པ་ཡང༌[^1673]མ་ཡིན་ཏེ། འགའ་ཞིག་གིས་མྱུར་དུ་འགྲུབ་པའི་ཕྱིར་དང་། གཞན་གྱི་དུས་རིང་པོ་ནས་འགྲུབ་པའི་ཕྱིར་དང་། གཞན་ནི་བརྟུལ་ཞུགས་སྤྱོད་པ་ལ་སོགས་པ་ལ༌[^1674]ལྟོས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2446]
ལས་གཅིག་ལས་ཀྱང་འགའ་ཞིག་གི་དོན་དང་དོན་མེད་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2447]
སྔགས་དག་བྱ་བ་བྱེད་དུ་ཟིན་ཀྱང་འགའ་ཞིག་ལ་སླུ་བའི༌[^1675]ཕྱིར། རྣམ་པ་འདི་ནི་རང་བཞིན་ལ་རིགས་པ་མ་ཡིན་ཏེ། རང་བཞིན་ནི་ཐམས་ཅད་ལ་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 2448]
སྐྱེས་བུ་རང་གི་འདོད་པས་འཇུག་པ་ཅན་ཡིན་པས་སེམས་ཅན་སྐལ་བ༌[^1676]མཉམ་པ་ལ་སོགས་པའི༌[^1677]དབང་གིས་སམ་བསྙེན་པའི་ཁྱད་པར་གྱིས་འགའ་ཞིག་རྗེས་སུ་འཛིན་གྱི་གཞན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རིགས་སོ། །

[Block 2449]
གལ་ཏེ་བརྟུལ་ཞུགས་ཀྱི་སྤྱོད་པ་དང་། ཉམས་པ་ལ་སོགས་པས་ཆོས་དང་ཆོས་མ་ཡིན་པ་འཕེལ་བ་ན།[^1678] ཆོས་སམ་ཆོས་མ་ཡིན་པའི་བདག་ཉིད་ཅན་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་དང་མ་གྲུབ་པ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། སྲོག་གཅོད་པ་དང་རྐུ་བ་དང་འཁྲིག་པ་དང་དམན་པ་ལ་སོགས་པའི་ཆོས་འགལ་བ་མང་པོ་དག་ཀྱང་མཁའ་འགྲོ་མ་དང་། སྲིང་མོའི༌[^1679]རྒྱུད་ལ་སོགས་པ་དག་ལ་མཐོང་བའི་ཕྱིར་དང་། དེ་དག་གིས་ཀྱང་གྲུབ་པའི་ཁྱད་པར་བསྒྲུབ་པའི༌[^1680]ཕྱིར་རོ། །

[Block 2450]
དེ་ལྟ་བུའི་རྣམ་པ་ཡང་ཆོས་ཀྱི་རང་བཞིན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྐབས་ཇི་ལྟ་བ་བཞིན་དུ་སྟོན་པར་འགྱུར་རོ། །

[Block 2451]
བྱམས་པ་དང་གཙང་སྦྲ་དང་ཆོས་ལ་གཞོལ་བ་དག་གི་རྒྱུ་མཚན་དེ་ཉིད་གྲུབ་པ་འགའ་ཞིག་ཀྱང་མི་བསྒྲུབ་པའི༌[^1681]ཕྱིར་བཟློག་པ་དག་གིས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2452]
ལས་ཀྱི་ངོ་བོ་གཅིག་ལས་ཀྱང་དེ་དང་འགལ་བའི་ཆོས་དང་ཆོས་མ་ཡིན་པ་མི་རིགས་སོ། །

[Block 2453]
ད་ནི་ཇི་ལྟར་ན་ཆོས་མ་ཡིན་པའི་བདག་ཉིད་ཅན་གྱི་བརྟུལ་ཞུགས་ལ་སོགས་པ་ལས་ཆོས་ཀྱི་འབྲས་བུ་འདོད་པ་ཐོབ་པར་འགྱུར། འབྲས་བུ་འདོད་པ་དེ་ནི་བརྟུལ་ཞུགས་ལ་སོགས་པ་དེའི་རྣམ་པར་སྨིན་པ་ནི་མ་ཡིན་གྱི། འོན་ཀྱང་སྔོན་གྱི་ལས་ཀྱིས་ཡིན་ཏེ། བྲམ་ཟེ་གསོད་པའི་ལུང་ནན་ཏན་དུ་བྱས་པ་ལས་ཡུལ་རྙེད་པ་བཞིན་ནོ། །

[Block 2454]
ཆོས་མ་ཡིན་པའི་བདག་ཉིད་ཅན་བརྟུལ་ཞུགས་དེ་མ་འོངས་པའི་འབྲས་བུ་ནི་མི་འདོད་པ་ཡིན་ནོ།[^1682] །འབྲས་བུ་འདོད་པ་ཅན་གྱི་ལས་དེའི༌[^1683]སྔགས་ལ་སོགས་པའི་སྦྱོར་བ་དེ་རྣམ་པ་འགའ་ཞིག་གིས་ཕན་འདོགས་པར་བྱེད་པའི་ཕྱིར་སྨིན་པར་བྱེད་པ་ཡིན་ཏེ། ཕན་འདོགས་པར་བྱེད་པའི་ནུས་པ་ནི་སྣ་ཚོགས་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2455]
སྐྱེས༌[^1684]བུའི་ཁྱད་པར་ལ་བརྟེན་པ་རྣམ་པར་སྨིན་པའི༌[^1685]ཆོས་ཅན་གྱི་ཆོས་དེ་དང་དེས་བྱས་པ་ནི། དེ་ལྟར་མགུ་བར་བྱས་པས་འབྲས་བུ་འབྱིན་པ་ཡིན་ནོ། །
--- END BLOCKS ---
