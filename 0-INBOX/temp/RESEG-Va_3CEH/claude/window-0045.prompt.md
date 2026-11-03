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
ཇི་ལྟར་ནམ་མཁའ་ལ་གཟུགས་ཀྱི་སྣང་བ་རྣམ་པར་བརྟགས་པ་ལྟར། དེ་བཞིན་དུ་དེའི་རྗེས་ལས་ཐོབ་པའི་ཡེ་ཤེས་བལྟ་བར་བྱ་སྟེ། རྣམ་པར་བརྟག་པར༌[^961]བྱ་བ་ལ་རྣམ་པར་རྟོག་པ་མེད་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1577 [HEADING]]
### སེམས་ཅན་གྱི་དོན་མཛད་པ་རྣམ་པར་རྟོག་པ་མེད་པ། ^8-16-0

[Block 1578]
ཡང་གལ་ཏེ་དེ་ལྟ་བུའི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀྱིས་རབ་ཏུ་བསྒོས་པའི་སངས་རྒྱས་ཉིད་དེས་སེམས་ཅན་གྱི་རྣམ་པར་རྟོག་པ་མེད་པ་དེ་བཞིན་དུ། དེའི་སེམས་ཅན་གྱི་དོན་མཛད་པ་ཡང་རྣམ་པར་རྟོག་པ་མེད་པར་ཇི་ལྟར་འགྱུར་ཞེ་ན། དེ་ཚིགས་སུ་བཅད་པས་ནོར་བུ་དང་སིལ་སྙན་གྱི་དཔེས་བསྟན་པ། ཇི་ལྟར་ནོར་བུ་སིལ་སྙན་དག །ཅེས་བྱ་བ་ལ། ཇི་ལྟར་ཡིད་བཞིན་གྱི་ནོར་བུ་རྣམ་པར་རྟོག་པ་མེད་པ་བཞིན་དུ་ཡང་སེམས་ཅན་རྣམས་ཀྱི་འདོད་པའི་དོན་གྱི་ལས་བྱེད་པ་དང་། ལྷ་རྫས་ཀྱི་སིལ་སྙན་རྣམས་མ་བརྡུངས་པར་ཡང་དེར་སྐྱེས་པའི་སེམས་ཅན་རྣམས་ཀྱི་འདོད་པ་བཞིན་དུ་སྒྲ་འབྱུང་བར་འགྱུར་བ་ལྟར། སངས་རྒྱས་རྣམས་ཀྱང་རྣམ་པར་རྟོག་པ་མི་མངའ་བཞིན་དུ་ཡང་ཕྲིན་ལས་རྣམ་པ་སྣ་ཚོགས་འབྱུང་བར་འགྱུར་རོ་ཞེས་ཤེས་པར་བྱའོ། །

[Block 1579 [HEADING]]
### རྣམ་པར་མི་རྟོག་པའི་ཟབ་པ་ཉིད། ^8-17-0

[Block 1580]
རྣམ་པར་མི་རྟོག་པའི་ཟབ་པ་ཉིད་བརྗོད་པར་བྱ་སྟེ། ཅི་ཡེ་ཤེས་དེ་གཞན་གྱི་དབང་ཞེས་བརྗོད་པའི་རྣམ་པར་བརྟག་པར༌[^962]བྱ་བའི་དངོས་པོ་ལ་འཇུག་གམ། འོན་ཏེ་གཞན་ཞིག་ལ་དམིགས་དེས༌[^963]ཅིར་འགྱུར། གལ་ཏེ་རྣམ་པར་བརྟག་པར༌[^964]བྱ་བ་ལ་དམིགས་ན་ནི་དེའི་རྣམ་པར་མི་རྟོག་པ་ཉིད་མི་དམིགས་སོ། །

[Block 1581]
གཞན་ལ་མི༌[^965]དམིགས་སོ་ཞེ་ན། དེའི་དམིགས་པ་གཞན་ནི་མེད་པ་ཉིད་ཀྱི་ཕྱིར། དེ་ལ་མ་ཡིན་གཞན་ལ་མིན། །ཞེས་བྱ་སྟེ། དེ་ལ་རེ་ཞིག་དེ་ལ་ནི་མ་ཡིན་ཏེ། རྣམ་པར་བརྟག་པར་བྱ་བ་ལ་དམིགས་པ་ནི་མི་འགྱུར་ཏེ། རྣམ་པར་མི་རྟོག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1582]
གཞན་ལ་ཡང་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་གཞན་གྱི་དབང་ཞེས་བརྗོད་པའི་ཆོས་དེ་ཉིད་ཀྱི་ཆོས་ཉིད་ལ་དམིགས་པའི་ཕྱིར་ཏེ། དེའི་ཆོས་ཉིད་དང༌[^966]ཆོས་དེ་དག་ནི་གཅིག་པ་ཉིད་དང་གཞན་པ་ཉིད་དུ་བརྗོད་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 1583]
དེའི་ཕྱིར་རྣམ་པར་བརྟག་པར་བྱ་བ་ལ་དམིགས་པའམ། གཞན་ལ་དམིགས་པ་ཡིན་ཞེས་བརྗོད་པར་མི་བྱའོ། །

[Block 1584]
གཞན་ཡང་དེ་ཤེས་པ་ཡིན་ནམ། ཡང་ན་མ་ཡིན། དེས་ཅིར་འགྱུར། གལ་ཏེ་ཤེས་པ་ཡིན་ན་ནི་དེ་ཇི་ལྟར་རྟོག་པ་མེད་པར་འགྱུར། འོན་ཏེ་མི་ཤེས་པའི༌[^967]ངོ་བོ་ཡིན་ན་ནི་ཇི་ལྟར་ན་ཡེ་ཤེས་རྣམ་པར་མི་རྟོག་པ་ཞེས་བརྗོད་པར་བྱ་ཞེ་ན། ཤེས་དང་མི་ཤེས་པ་མ་ཡིན། །ཞེས་བྱ་བས་བསྟན་ཏེ། རེ་ཞིག་དེ་ཤེས་པ་ནི་མ་ཡིན་ཏེ། འདི་ལྟར་སྦྱོར་བ་ལས་བྱུང་བའི་རྣམ་པར་རྟོག་པ་དང་བཅས་པའི་ཡེ་ཤེས་ཀྱི་ངོ་བོ་ལྟར་མི་འཇུག་པས་སོ། །

[Block 1585]
དེ་མི་ཤེས་པ་ཡང་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་སྦྱོར་བ་ལས་བྱུང་བ་རྣམ་པར་རྟོག་པ་དང་བཅས་པའི་ཡེ་ཤེས་རྒྱུར་གྱུར་པ་ལས་དེ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 1586 [VERSE]]
དེ་ལ་མ་ཡིན་གཞན་ལ་མིན། །
ཤེས་དང་མི་ཤེས་པ་མ་ཡིན། །

[Block 1587]
ཞེས་བྱ་བའི་དོན་གཞན་ཡང་གང་གི་ཕྱིར་རྣམ་པར་རྟོག་པ་འཇུག་པ་དེ་ལ་ཡང་མ་ཡིན་ཏེ། དེས་ན་ཤེས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1588]
གང་གི་ཕྱིར་ཆོས་ཉིད་ལ་འཇུག་པས་དེ་ལས༌[^968]གཞན་པ་ཡང་མ་ཡིན་ཏེ། དེས་ན་མི་ཤེས་པ་མ་ཡིན་ནོ། །

[Block 1589]
དེ་ནི་སྔ་མ་ཕྱི་མས་བཤད་པར་གྱུར་པ་མ་ཡིན་ནོ། །

[Block 1590 [VERSE]]
ཤེས་བྱ་དང་ནི་ཁྱད་མེད་པའི། །
ཤེས་གང་དེ་ནི་མི་རྟོག་ཉིད། །

[Block 1591]
ཅེས་བྱ་བ་ལ། གང་གཟུང་བ་དང་འཛིན་པའི་ངོ་བོར་འཇུག་པའི་སྦྱོར་བ་ལས་བྱུང་བ་ལྟ་བུ་ནི༌[^969]རྣམ་པར་མི་རྟོག་པ་མ་ཡིན་གྱི། གང་ཡང་གཟུང་བ་དང་ཤེས་བྱ་ཐ་མི་དད་པར་འཇུག་པས་མཉམ་པ་ཉིད་དུ་འཇུག་པ་དེ་ནི་རྣམ་པར་མི་རྟོག་པ་ཉིད་དོ། །

[Block 1592]
ཡེ་ཤེས་དེ་ནི་གཟུང་བ་དང་འཛིན་པའི་ངོ་བོ་ལ་མི་གནས་པ་ཉིད་དོ། །

[Block 1593]
གང་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་མདོ་གཞན་ལས།

[Block 1594]
ཆོས་ཐམས་ཅད་རྣམ་པར་རྟོག་པ་མེད་པའོ་ཞེས་གསུངས་པ་དེ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཆོས་རྣམས་ཐམས་ཅད་རང་བཞིན་གྱིས། །རྣམ་རྟོག་མེད་པ༌[^970]ཞེས་བྱ་བ་ལ། ཆོས་ཐམས་ཅད་ནི་རང་བཞིན་གྱིས་རྣམ་པར་རྟོག་པ་མེད་པའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །གང་གི་ཕྱིར་ཞེ་ན། རྣམ་པར་བརྟག་བྱ་མེད་པས་ན། །ཞེས་བྱ་བ་སྟེ། གང་གི་ཕྱིར་བརྟག་པར་བྱ་བའི་དངོས་པོ་མེད་པས་སོ། །

[Block 1595]
གང་ཡང་དེ་ལྟར་རྣམ་པར་བརྟག་པར་བྱ་བ་མེད་པས་རང་བཞིན་གྱིས་ཆོས་རྣམས་རྣམ་པར་མི་རྟོག་པ་ཉིད་ཡིན་པ་དེའི་ཕྱིར་དེས་ན་སེམས་ཅན་ཐམས་ཅད་གང་གི་ཕྱིར་ཐར་བར་མི་འགྱུར་ཞེ་ན། འདི་ལྟར། ཤེས་གང་དེ་ནི་མི་རྟོག་ཉིད། །ཅེས་བྱ་བས་ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས་རྣམ་པར་རྟོག་པ་མེད་པ་ཉིད་ཡིན་ན་ཡང་སེམས་ཅན་ལ་ཐར་པ་མེད་པར་བསྟན་པ་ནི་གང་ཡང་རྣམ་པར་རྟོག་པ་མི་བརྟེན་པ་ཉིད་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1596]
དེས༌[^971]ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས་རྣམ་པར་མི་རྟོག་པ་ཉིད་ཡིན་ན་ཡང་། གལ་ཏེ་དེར་རྟོགས་པའི་ཡེ་ཤེས་སྐྱེས་པར་གྱུར་ན་དེས་མངོན་སུམ་དུ་མཐོང་བར་འགྱུར་ལ། དེ་ནི་རྣམ་པར་མི་རྟོག་པ་ཉིད་དོ། །

[Block 1597]
དེས་ཀྱང་གྲོལ་བར་འགྱུར་ཏེ༌[^972]སྐྱེས་པར་མ་གྱུར་ན་ནི་གྲོལ་བར༌[^973]མི་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1598]
དེའི་ཕྱིར་ཡེ་ཤེས་དེ་ནི་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 1599 [HEADING]]
### ཡེ་ཤེས་གསུམ་གྱི་རབ་ཏུ་དབྱེ་བ། ^8-18-0

[Block 1600 [HEADING]]
#### སྦྱོར་བ་ལས་བྱུང་བ། ^8-18-1-0

[Block 1601]
ཡེ་ཤེས་གསུམ་པ་དེ་རྣམས་ཀྱི༌[^974]རབ་ཏུ་དབྱེ་བ་བསྟན་པར་བྱ་བའི་ཕྱིར་རྒྱུ་དང་འཕེན་པ་དང་། གོམས་པ་ལས་བྱུང་བས༌[^975]རབ་ཏུ་དབྱེ་བའི༌[^976]ཕྱིར་རོ་ཞེས་བྱ་བ་སྟེ། དེ་ལ་རྣམ་པར་མི་རྟོག་པའི་སྦྱོར་བ་ལས་བྱུང་བ་ནི་རྣམ་པ་གསུམ་སྟེ།

[Block 1602]
འདི་ལྟར་ཁ་ཅིག་ནི་རིགས་ཀྱི་སྟོབས་ལས།

[Block 1603]
ཁ་ཅིག་ནི་འཕེན་པའི་སྟོབས་ལས།

[Block 1604]
ཁ་ཅིག་ནི་ད་ལྟར་གྱི་དུས་སུ་གོམས་པའི་སྟོབས་ལས་འབྱུང་བར་འགྱུར་རོ། །

[Block 1605 [HEADING]]
##### རིགས་ཀྱི་སྟོབས། ^8-18-1-1-0

[Block 1606]
དེ་ལ་རིགས་ཀྱི་སྟོབས་ལས་ནི་དེར་རྒྱུར་གྱུར་པ་ལས་འབྱུང་བར་འགྱུར་བ་ཉིད་དོ། །

[Block 1607 [HEADING]]
##### འཕེན་པའི་སྟོབས། ^8-18-1-2-0

[Block 1608]
དེ་འཕེན་པའི་སྟོབས་ལས་ནི་དེ་སྐྱེ་བ་སྔ་མ་ལ་གོམས་པར་བྱས་པའི་རྒྱུ་ཉིད་ལས་འབྱུང་བར་འགྱུར་རོ། །

[Block 1609 [HEADING]]
##### གོམས་པའི་སྟོབས། ^8-18-1-3-0

[Block 1610]
གང་གོམས་པའི་སྟོབས་ལས་ད་ལྟར་གྱི་སྐྱེ་བ་ཉིད་ལ་སྐྱེས་བུ་བྱེད་པའི་སྟོབས་ཀྱི་རྒྱུ་ལས་དེ་འབྱུང་བར་འགྱུར་བའོ། །

[Block 1611 [HEADING]]
#### རྣམ་པར་མི་རྟོག་པ། ^8-18-2-0

[Block 1612 [HEADING]]
##### ཆོག་ཤེས་པས་རྣམ་པར་མི་རྟོག་པ། ^8-18-2-1-0

[Block 1613]
ཆོག་ཤེས་པ་དང་། ཕྱིན་ཅི་མ་ལོག་པ་དང་། སྤྲོས་པ་མེད་པས་རྣམ་པར་མི་རྟོག་པའི་ཕྱིར་རོ༌[^977]ཞེས་བྱ་བ་ལ། དེ་ལ་ཆོག་ཤེས་པས་རྣམ་པར་མི་རྟོག་པ་ནི་ཐོས་པ་དང་བསམས་པ་ལས་བྱུང་བའི་མཐར་ཕྱིན་པ་ཡིན་པར་བལྟ་བར་བྱ་སྟེ། ཆོག་ཤེས་པ་ལས༌[^978]རྣམ་པར་མི་རྟོག་པ་ནི་ཆོག་ཤེས་པས་རྣམ་པར་མི་རྟོག་པའོ་ཞེས་དེ་ལྟར་བྱས་ནས་ཐོས་པའམ་བསམས་པ་གང་གིས་བློ་གང་གི་མཐར་ཕྱིན་པར་གྱུར་པ་དེ་ནི་སོ་སོའི་སྐྱེ་བོའི་ས་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའི་ཆོག་ཤེས་པ་འབྱུང་བར་འགྱུར་བ་སྟེ། དེ་ནི་རེ་ཞིག་འདི་ཙམ་མོ་ཞེས་དེ་ལྟར་བྱས་པའི་དོན་འདིས་ཆོག་ཤེས་པའི་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 1614]
དོན་གཞན་ཡང་འཇིག་རྟེན་པའི་ཆོག་ཤེས་པའི་རྣམ་པར་མི་རྟོག་པར་བལྟ་བར་བྱ་སྟེ། གང་སྲིད་པའི་རྩེ་མོར་ཕྱིན་པར་གྱུར་པ་དེ་ནི་མྱ་ངན་ལས་འདའ་བར་བལྟ་བས་དེའི་ཕ་རོལ་ན་རྟོགས་པར་བྱ་བ་གཞན་མེད་དོ་ཞེས་ཆོག་ཤེས་པ་འབྱུང་བར༌[^979]འགྱུར་བའོ། །

[Block 1615 [HEADING]]
##### ཕྱིན་ཅི་མ་ལོག་པས་རྣམ་པར་མི་རྟོག་པ། ^8-18-2-2-0
--- END BLOCKS ---
