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
རང་བཞིན་ཐ་དད་མིང་ཅན་དེ། །ཞེས་པ༌[^1568]དོན་དང་ལྡན་པའི་མིང་འཛིན་པའོ། །

[Block 2417 [VERSE]]
ཐམས་ཅད་མཁྱེན་པས་གསུངས་པ་ཡིན། །
ཞེས་པ་འདིས་རང་བཟོ་བཀག་པའོ། །
དེ་ནི་མ་ལུས་དོན་ཐོས་ནས། །

[Block 2418]
ཞེས་པ་ནི་རྒྱས་པར་བསྟན་པའོ། །

[Block 2419]
དོན་མ་ལུས་པ་ནི་གཞལ་བར་བྱ་བའི་དངོས་པོ་སློབ་དཔོན་གྱི་ཞལ་ནས་ཐོས་ཏེ། འཛིན་པ་ལ་ནི་རྣམ་པར་མཁས། །ཞེས་པ་ནི་ཕྱིན་ཅི་མ་ལོག་པར་འཛིན་པར་བྱེད་དོ། །

[Block 2420]
སྐད་ཅིག་གིས་ནི་བརྗེད༌[^1569]གྱུར་པ། །ཞེས་པ་ནི། དེ་ནས་ལངས་ཏེ་ཅང་མི་དྲན་པའོ། །

[Block 2421]
དེ་བས་ན་ཨུཏྤལ་ལྟར་ཨུཏྤལ་ཏེ། གང་གི་ཕྱིར་མཚོན་གནས་པའི་ཨུཏྤལའི་དྲི་དང༌[^1570]ཁ་དོག་ཡོད་དེ། དེ་ནས་བཅད་མ་ཐག་ཏུ་དྲི་མེད་པ་དང་མདོག་ཡལ་ལོ། །

[Block 2422]
གཟུང་བྱ་ལྷག་པར་མང་ཐོས་ཀྱང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་འདིས་པདྨ་དཀར་པོ་བསྟན་ཏོ།[^1571] །

[Block 2423]
གཟུང་བྱ་ནི་ཆོས་ཀྱི་དོན་ནོ། །

[Block 2424]
ལྷག་པ་ནི་ཆོས་གྲོགས་པོ་ལས་ཁྱད་པར་དུ་གྱུར་པའོ། །

[Block 2425]
དེ་ཉིད་མང་དུ་ཐོས་ནས་འཛིན་ཅིང་དྲན་པས་ཀྱང་བྱེད་དོ། །

[Block 2426]
སྟོན་པ་ཡིས་ནི་ནུས་མེད་པ། །ཞེས་པ་ནི་ཐོས་ནས་ཀྱང་བཤད་པའི་དུས་སུ་ཕྱོགས་དང་གཏན་ཚིགས་དང་དཔེ་དང་བཤད་པའི་རྒྱུད་དང་ཡན་ལག་གི་རྒྱུད་ཀྱི་རིམ་པས་སོ་སོར་སྟོན་པར་མི་ནུས་པ་སྟེ། སྐྱེ་བས་ཐོབ་པའི་ཤེས་རབ་མེད་པའི་ཕྱིར་དང་། ཆོས་ལ་དམིགས་པ་ལས་བྱུང་བའི༌[^1572]ཤེས་རབ་དམན་པའི་ཕྱིར་ཞེས་དགོངས་སོ། །

[Block 2427]
བུམ་པའི་རས་བལ་ཞེས་བྱ་བའི་དཔེ་ཡིན་ཏེ།

[Block 2428]
དེས་ན་བུམ་པ༌[^1573]གནས་པའི་རས་བལ་གྱི་ས་བོན་ལས།

[Block 2429]
མྱུ་གུ་ལ་སོགས་པ་མི་འབྱུང་ངོ་ཞེས་ཐ་ཚིག་གོ། །

[Block 2430]
འདྲ་བ་ནི་པདྨ་དཀར་པོའི་གང་ཟག་ཀྱང་དེ་དང་འདྲ་བ་ཡིན་ཏེ་པདྨ་དཀར་པོའི་དྲི་རང་གི་ལྟེ་བར་འཁོར་ཞིང་ཕྱིར་སྤྲོ་བ་མེད་དོ། །

[Block 2431]
པདྨ་བསྟན་པར་བྱ་བའི་ཕྱིར། དད་དང་ལྡན་ཞིང་སྙིང་རྗེ་ཤེས། །ཞེས་པ་ནི་ཡོན་ཏན་ཐམས་ཅད་ཀྱི་གཞིར་གྱུར་པ་ནི་དད་པའོ། །

[Block 2432]
དེས་ནི་དགེ་བ་ཅན་ཡིན༌[^1574]བཞིན་དུ་རྣལ་འབྱོར་པ་ལ་སྲུང་བར་བྱེད་པ་སྟེ། བདེན་པ་དང་དཀོན་མཆོག་གསུམ་ལ་སོགས་པ་རྣམས་ལ་མངོན་པར་དད་པའོ།[^1575] །

[Block 2433]
ཤེས་པ་ནི་ཡང་དག་པར་རྟོགས་པའོ། །

[Block 2434]
སྙིང་རྗེ་ནི་ཐོས་པ་ལ་སོགས་པའི་འབྲས་བུ་དེ་དང་ལྡན་པའོ། །

[Block 2435]
ཐོས་པ་བློ་ལ་རྒྱས་པར༌[^1576]གྱུར་པ་ཞེས་པ་ནི་སློབ་དཔོན་གྱི་ཞལ་ནས་གང་ཐོས་པ་དེ་ཉིད་སེམས་ཀྱི་རྒྱུད་དུ་རིགས་པ་རྣམ་པ་བཞིས་འཕེལ་བར་གྱུར་པའི་ངང་ཚུལ་ཅན་ནོ། །

[Block 2436 [VERSE]]
དེ་བཞིན་དུ་འཆད་པའི་དུས་སུ། །
ཚིགས་མེད་འོད་མ་བཞིན་དུ་འཛག །

[Block 2437]
[^1577]ཅེས་པ་ནི་ཆོས་ཐམས་ཅད་གཏོང་བར་བྱེད་པའོ། །

[Block 2438]
དེ་ནི་པདྨར་བཤད་པ་ཡིན་ཏེ། པདྨའི་ལྟེ་བར་ཡོད་པའི་ཟིལ་བ་རྣམས་ཉི་མས་ཁ་ཕྱེ་མ་ཐག་ཏུ་འཐོར་བར༌[^1578]བྱེད་དོ། །

[Block 2439]
ཙནྡན་བསྟན་པར་བྱ་བའི་ཕྱིར། ཐོས་པ་ཉུང་ཞིང་ཞེས་སྨོས་ཏེ། སློབ་དཔོན་གྱི་ཞལ་ནས༌[^1579]ཐོས་པ་མང་དུ་མ་ཐོས་པའོ། །

[Block 2440]
གལ་ཏེ་མཁས་པ་གཞན་གང་ཞིག་གིས་སྐུལ་བར༌[^1580]བྱེད་ན་ཀྱེ་གདོང་བཟང་འབད་པར་གྱིས་ཤིག །ཇི་སྲིད་འདོད་པར་བདག་གིས་ཁྱོད་ལ་ཐམས་ཅད་བཤད་པར་བྱ་ཞེས་ཐོས་ནས་སྨྲ་ན་བདག་གིས་ཐམས་ཅད་ཤེས་པས་ཆོས་གཞན་ཐོས་པས་བདག་ལ་དགོས་པ་མེད་དོ་ཞེས་ཁྲོས་ནས་ལངས་ཏེ་འགྲོ་བ་ནི་ང་རྒྱལ་ལྡན་པའོ། །

[Block 2441]
ཇི་སྐད་དུ།

[Block 2442 [VERSE]]
ཐོས་པའི་རྗེས་སུ་འབྲང་བ་གང་ཞིག་བློ་ལྡན་ཉིད། །
ཐོབ༌[^1581]ནས་ཐོས་པ་ཉིད་ལ་བཏང་སྙོམས་གང་བྱེད་པ། །
ཐོས་པ་སྣ་ཚོགས་རྣམ་པ་དཔག་མེད་ལུས་པ་ན། །
རྨོངས་པ་དེ་ནི་ངེས་པ་སྐྱེ་བར་ག་ལ་འགྱུར། །

[Block 2443]
ཞེས་འབྱུང་ངོ་། །

[Block 2444]
གལ་ཏེ་ང་རྒྱལ་ལྡན་པ་ཡིན་ན་དེ་སྐྱོན་མེད་དུ་ཆུག་ན་གལ་ཏེ་བཤད་པའི་དུས་སུ་མང་དུ་སྨྲ་སྟེ་སྐྱོ་བ་སྐྱེད་པར་བྱེད་དོ། །

[Block 2445]
གལ་ཏེ་རིགས་པ་སྨྲ་ན་དེའི་ཚེ་སྐྱོན་མེད་དོ། །

[Block 2446]
འོན་ཀྱང་རྩ་བ་མེད་པར་ནི་མདོ་ལས་འདས་ཤིང་བསྟན་པ་གཞན་དང་བསྲེས་ཏེ་རང་གི་གྲུབ་པའི་མཐའ་དང་བྲལ་བར་སྨྲ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2447]
སྐྱོན་དེ་བསལ་བར་བྱ་བའི་ཕྱིར་ཐོས་པའི་སྣོད་དུ་རུང་བར་གལ་ཏེ་བྱས་ན་དེ་ཡང་མི་ནུས་ཏེ། ང་རྒྱལ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2448]
ཇི་སྐད་དུ།

[Block 2449 [VERSE]]
མི་ཤེས་པ་ནི་བདེ་བར་མགུ་བྱ་སྟེ། །
ཁྱད་པར་ཤེས་པ་ཤིན་ཏུ་མགུ་བར་སླ།[^1582] །
དུམ་ཅིག་ཤེས་པས༌[^1583]ཁེངས་པ་གང་ཡིན་པ། །
སངས་རྒྱས་ཀྱིས་ཀྱང་མགུ་བར་བྱེད་མི་ནུས། །

[Block 2450]
ཞེས་འབྱུང་ངོ་། །དེ་ནི་ཙནྡན་ཞེས་བྱ་བ་སྟེ་ཙནྡན་ནི་རང་བཞིན་གྱིས་འབྲས་བུ་མེད་པ་དང་མཆེ་བའི་དུག་ཅན་གྱི་སྦྲུལ་རྣམས་ཀྱིས་བསྐོར་བའི་ཕྱིར་དེའི་གམ༌[^1584]དུ་གང་གིས་ཀྱང་མི་ཉེ་བས་རྗེས་སུ་གཟུང་བར་མི་ནུས་སོ། །

[Block 2451]
དེ་ལྟར་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 2452]
[^1585]བདག་གི༌[^1586]དོན་དང་གཞན་གྱི་དོན་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 2453]
རིན་པོ་ཆེ་བསྟན་པར་བྱ་བའི་ཕྱིར། །ཚུལ་ཁྲིམས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རྒྱུ་དང་མི་རྒྱུ་རྣམས་ཀྱི་རྟེན་ས་གཞི་བཞིན་དུ་ཡོན་ཏན་ཐམས་ཅད་ཀྱི་གཞི༌[^1587]ནི་ཚུལ་ཁྲིམས་དེ་དང་ལྡན་པའོ། །

[Block 2454]
དག་པ་ནི་གཡོ་སྒྱུ༌[^1588]མེད་པའོ། །

[Block 2455]
མཁས་པ་སྒྲིན༌[^1589]ཞེས་བྱ་བ༌[^1590]ནི་དགེ་བའི་ལས་རྣམས་ལ་བརྩོན་ཞིང་ཡོངས་སུ་ཤེས་པའོ། །ཤེས་རབ་ལྡན་ཞིང་ཞེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པའི་ཤེས་རབ་ཡོད་པའོ། །
--- END BLOCKS ---
