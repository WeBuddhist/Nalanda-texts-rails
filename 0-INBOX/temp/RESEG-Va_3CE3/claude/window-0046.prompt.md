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
ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་གང་ཡིན་པ་དེ་ནི་རབ་འབྱོར༌[^1137]དེ་བཞིན་ཉིད་ཀྱང་དེའོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་གཅིག་པའི་ཕྱིར་གཅིག་གོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1612]
དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་གནས་པ་ཞེས་བྱ་བ་ནི་ཆོས་གནས་པའི་མཚན་ཉིད་དུ་ཡང་གཅིག་གོ་ཞེས་སྟོན༌[^1138]ཏོ། །

[Block 1613]
འགྱུར་བ་མེད་ཅིང་རྣམ་པར་རྟོག་པ་མེད་ཅེས་བྱ་བ་ལ། འགྱུར་བ་མེད་ཅེས་བྱ་བ་འདིས་ནི་མི་འགྱུར་བའི་ཡོངས་སུ་གྲུབ་པས་ཡོངས་སུ་གྲུབ་པར་སྟོན༌[^1139]ཏོ། །

[Block 1614]
རྣམ་པར་རྟོག་པ་མེད་ཅེས་བྱ་བ་འདིས་ནི་ཕྱིན་ཅི་མ་ལོག་པར་ཡོངས་སུ་གྲུབ་པས་ཡོངས་སུ་གྲུབ་པར་སྟོན་ཏོ། །

[Block 1615]
ཅི་ལ་འང་ཐོགས་པ་མེད་པ༌[^1140]ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ལ་ཁྱབ་པ་སྟེ། གང་ན་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1616]
དེ་བས་ན་གང་གི་དེ་བཞིན་ཉིད་དུ་མ་གྱུར་པ༌[^1141]ཡང་མེད་དེ་ཞེས་བྱ་བ་གསུངས་ཏེ། ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ཀྱང་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1617]
ནམ་ཡང་དེ་བཞིན་ཉིད༌[^1142]དུ་མ་གྱུར་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི་དུས་ཐམས་ཅད་དུ་ཡང་དེ་བཞིན་ཉིད་དོ། །

[Block 1618]
གཉིས་སུ་མེད་ཅེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་གཅིག་པའོ། །

[Block 1619]
དེ་གཉིས་སུ་བྱར་མེད་ཅེས་བྱ་བ་ནི་རྣམ་པ་གཉིས་སུ་དབྱེར་མི་ནུས་པའོ། །

[Block 1620]
ཇི་ལྟར་དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་ཐ་མི་དད་པ་དབྱེར་མེད་པ་གཉིས་སུ་མེད་པ་དེ་བཞིན་དུ་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ཀྱང་ཐ་མི་དད་པར་དབྱེར་མེད་པ་དམིགས་སུ་མེད་པའོ། །

[Block 1621]
དེ་བཞིན་དུ་གནས་བརྟན་རབ་འབྱོར་གྱི་དེ་བཞིན་ཉིད་ཀྱང་ཐ་མི་དད་པ་དབྱེར་མེད་པ་དམིགས་སུ་མེད་པ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་བཞིན་དུ་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ཀྱང་དམིགས་སུ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱིས་ཐ་མི་དད་དོ། །

[Block 1622]
ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་བཞིན་དུ་གནས་བརྟན་རབ་འབྱོར་གྱི་དེ་བཞིན་ཉིད་ཀྱང་དམིགས་སུ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱིས་ཐ་མི་དད་དོ༌[^1143]ཞེས་སྟོན་ཏེ། [^1144]ཇི་ལྟར་དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་གཉིས་སུ་མེད་པའི་ཕྱིར་ཐ་མི་དད་པ་དང་གཉིས་སུ་བྱར༌[^1145]མེད་པའི་ཕྱིར་དབྱེར་མེད་པ་དང་། དམིགས་སུ་མེད་པའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱིས་དམིགས་སུ་མེད་དེ་གཅིག་པ་དང་། ཇི་ལྟར་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ཀྱང་ཐ་མི་དད་དབྱེར་མེད་པ༌[^1146]དམིགས་སུ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པ་དེ་བཞིན་དུ་རབ་འབྱོར་གྱི་དེ་བཞིན་ཉིད་ཀྱང་དམིགས་སུ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱིས་ཐ་མི་དད་དེ། དབྱེར་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1623]
དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་གང་ཡིན་པ་དེ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ལས་གུད་ན་ཡོད་པ་མ་ཡིན་ཏེ། ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ལས་གུད་ན་ཡོད་པ་མ་ཡིན་པ་དེ་ནི་ནམ་ཡང་དེ་བཞིན་ཉིད་མ་ཡིན་པ་མ་ཡིན་ཞིང་། དེ་ནི་རྟག་ཏུ་དེ་བཞིན་ཉིད་དོ། །

[Block 1624]
གནས་བརྟན་རབ་འབྱོར་གྱི་དེ་བཞིན་ཉིད་ཀྱང་དེ་ལྟ་བུ་སྟེ། དེའི་ཕྱིར་རྣམ་པ་གཞན་མ་ཡིན་པས་དེ་བཞིན་གཤེགས་པའི་རྗེས་སུ་སྐྱེས་ཀྱང་གང་དུ་ཡང་རྗེས་སུ་སྐྱེས་པ་མེད་དོ་ཞེས་བྱ་བས་ནི་དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད༌[^1147]དུ་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ཀྱང་དམིགས་སུ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱིས་ཐ་མི་དད་དོ། །

[Block 1625]
ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་བཞིན་དུ་གནས་བརྟན་རབ་འབྱོར་གྱི་དེ་བཞིན་ཉིད་ཀྱང་དམིགས་སུ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱིས་ཐ་མི་དད་དོ་ཞེས་སྟོན་ཏེ། དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་གང་ཡིན་པ་དེ་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ལས་གཞན་མ་ཡིན་ལ། གང་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ལས་གཞན་པ་མ་ཡིན་པ་དེ་ཡང་ནམ་ཡང་དེ་བཞིན་ཉིད་མ་ཡིན་པ་མ་ཡིན་ཏེ། ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ནི་དུས་ཐམས་ཅད་དུ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1626]
དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད༌[^1148]དེ་ལས་གཞན་མ་ཡིན་པའི་ཕྱིར། དུས་ཐམས་ཅད་དུ་ཡོད་དོ། །

[Block 1627]
དེ་བཞིན་དུ་གནས་བརྟན་རབ་འབྱོར་གྱི་དེ་བཞིན་ཉིད་ཀྱང་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ལས་གཞན་པ༌[^1149]མ་ཡིན་པའི་ཕྱིར་དུས་ཐམས་ཅད་དུ་ཡོད་དོ། །

[Block 1628]
དེ་བས་ན་དུས་ཐམས་ཅད་དུ་ཡོད་པའི་ཕྱིར། དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་ཀྱི་རྗེས་སུ་སྐྱེས་པ་ཞེས་བྱའོ། །

[Block 1629]
སྐྱེ་བའི་མཚན་ཉིད་མེད་པའི་ཕྱིར་གང་དུ་ཡང་རྗེས་སུ་སྐྱེས་པ་མེད་པ་ཞེས་ཀྱང་བྱའོ། །

[Block 1630]
ཇི་ལྟར་དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་འདས་པ་མ་ཡིན་མ་འོངས་པ་མ་ཡིན། ད་ལྟར་བྱུང་བ་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྟོན་ཏེ། ཇི་ལྟར་དེ་བཞིན་གཤེགས་པ་ཀུན་བརྟགས་པའི་བདག་ཉིད་ཀྱིས་དུས་གསུམ་དུ་གཏོགས་ཀྱང་དེ་བཞིན་ཉིད་ནི་དུས་ཀྱིས་བསྡུས་པ་མ་ཡིན་པ་དེ་བཞིན་དུ༌[^1150]ཆོས་ཐམས་ཅད་ཀྱང་ཀུན་བརྟགས་པའི་བདག་ཉིད་དུ་དུས་གསུམ་དུ་གཏོགས་ཀྱང་། དེ་དག་གིས༌[^1151]དེ་བཞིན་ཉིད་ནི་དུས་ཀྱིས་བསྡུས་པ་མ་ཡིན་ནོ། །

[Block 1631]
དེ་བཞིན་དུ་གནས་བརྟན་རབ་འབྱོར་གྱི་དེ་བཞིན་ཉིད་ཀྱང་དུས་ཀྱིས༌[^1152]བསྡུས་པ་མ་ཡིན་ནོ། །

[Block 1632]
དེའི་ཕྱིར་དེ་བཞིན་གཤེགས་པའི་རྗེས་སུ་སྐྱེས་པ་ཞེས་བྱའོ། །

[Block 1633]
ལྷའི་བུ་དག་འདི་ལ་འདས་པའི་དེ་བཞིན་ཉིད་ཀྱི་མཉམ་པ་ཉིད་ཀྱིས་དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་མཉམ་པ་ཉིད་དུ་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་སྟོན་ཏེ། འདི་ལྟར་འདས་པའི་ཆོས་ཐམས་ཅད་ཀྱི་འདས་པའི་དེ་བཞིན་ཉིད་ངོ་བོ་ཉིད་གཅིག་པའི་ཕྱིར་མཉམ་པས་དེའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱང་མཉམ་མོ། །

[Block 1634]
དེ་དག་ཀྱང་དེ་བཞིན་ཉིད་དེ་དང་བདག་ཉིད་གཅིག་པའི་ཕྱིར་མཉམ་མོ། །

[Block 1635]
གང་གི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་མཉམ་པ་དེ་ཉིད་ཀྱི་ཕྱིར་འདས་པའི་ཆོས་རྣམས་ཀྱི་དེ་བཞིན་ཉིད་ཀྱང་མཉམ་མོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་དང་། ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་གཅིག་པའི་ཕྱིར་རོ། །

[Block 1636]
ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་མཉམ་པ་ཉིད་ཀྱིས་དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་ཀྱང་མཉམ་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 1637]
དེ་བཞིན་གཤེགས་པའི་དེ་བཞིན་ཉིད་མཉམ་པ་ཉིད་ཀྱིས་འདས་པའི་ཆོས་ཐམས་ཅད་མཉམ་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 1638]
དེ་བཞིན་དུ་གཞན་དག་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1639]
གཟུགས་ཀྱི་ཆོས་མཉམ་པ་ཉིད་ཀྱིས༌[^1153]ཞེས་བྱ་བ་ལ་སོགས་པས་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་དེ་ཉིད་རྒྱ་ཆེར་སྟོན་ཏོ། །

[Block 1640]
[^1154]ལྷའི་བུ་དག་དེ་བཞིན་གཤེགས་པས་ཡང་དག་པའི་དེ་བཞིན་ཉིད༌[^1155]འདི་ལ་བརྟེན་ནས་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་བའི་མཚན་ཐོབ༌[^1156]པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི༌[^1157]རབ་འབྱོར་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་བ་དེ་ནི་ཡང་དག་པའི༌[^1158]དེ་བཞིན་ཉིད་ཀྱི་ཚིག་བླ་དགས་སོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1641]
རྣམ་པ་དྲག་ཏུ་གཡོས་ཞེས་བྱ་བ་ནི་གཡོ་བ་དང་། འགུལ་བ་དང་། ལྡེག་པ་དང་། ཆེམ་ཆེམ་པ༌[^1159]དང་། འུར་འུར་དང་། འཁྲུགས་ཞེས་བྱ་བ་རྣམ་པ་དྲུག་སྟེ། དེ་དག་ལས་ཆུང་ངུ་དང་འབྲིང་པོ་དང་ཆེན་པོའི་དབང་གིས་རེ་རེ་ལ་ཡང་རྣམ་པ་གསུམ་དུ་ཕྱེ་ན། མཚན་ལྟས་ཆེན་པོ་རྣམ་པ་བཅོ་བརྒྱད་དང་། ཕྱོགས་དྲུག་རྣམས་སུ་མཐོ་བ་དང་། དམའ་བའི་དབང་གིས་ཕྱོགས་སུ༌[^1160]གྱུར་པ་རྣམ་པ་བཅུ་གཉིས་ཏེ། དེ་དག་ཀྱང་གླེང་གཞིའི་ལེའུ་ཉིད་དུ་བཤད་ཟིན་ཏོ། །

[Block 1642]
དེ་ལ་གཡོས་པ་ལ་སོགས་པ་འདི་དག་ཀྱང་རྒྱུ་རྣམ་པ་གཉིས་ཀྱིས་འབྱུང་སྟེ་ལྷ་མཐུ་ཆེན་པོ་རྣམས་དམ་པའི་ཆོས་ཐོས་ནས་དགའ་ཞིང་མགུ་བ་སྐྱེས་པའི་མཐུས་ཕན་ཚུན་ཡོངས་སུ་འཁོར་ཞིང་འཁྲུགས་པ་དང་། ཆོས་ཉིད་ཀྱི༌[^1161]མཐུས་གནས་པའི་འཇིག་རྟེན་གྱིས་ཀྱང་ཆོས་ཀྱི་ཆེ་བའི་བདག་ཉིད་བསྟན་པའི༌[^1162]ཕྱིར་འདས་པའི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་བཤད་པའི་ཆོས་ཉིད་ཀྱིས་དབང་དུ་གྱུར་པ་ཉིད་དུ་སྟོན་པ་ལྟ་བུར་གྱུར་པའོ། །

[Block 1643]
དེ་ལ་ཕྱོགས་གཅིག་པར་རབ་ཏུ༌[^1163]ལྡེག་པ་ནི་གཡོ་བའོ། །

[Block 1644]
ཤིང་ལྗོན་པ་བཞིན༌[^1164]བདག་ཉིད་ཐམས་ཅད་འགུལ་བ་ནི་འགུལ་བའོ། །

[Block 1645]
མེ་མགལ་སྐོར༌[^1165]བ་བཞིན་དུ་འཁོར་བ་ནི་ལྡེག་པའོ། །

[Block 1646]
སྒྲ་སྐད་རིང་དུ་འབྱུང་བའི་སྒྲ་ནི་ཆེམ་ཆེམ་མོ། །

[Block 1647]
རྣམ་པར་འཁྲུག་པ་ནི་འཁྲུག་པའོ། །

[Block 1648]
སྒྲ་བེར་བེར་པོ་ནི་འུར་འུར་རོ། །

[Block 1649]
ཡང་ན་ས་ནི་གཡོས་སོ། །

[Block 1650]
ཤིང་ཐམས་ཅད་ནི་འགུལ་ལོ། །
--- END BLOCKS ---
