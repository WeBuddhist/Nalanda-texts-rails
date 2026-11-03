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
འདི་ལྟ་བུའི་དགོན་པ་ཞེས་བྱ་བ་ནི་དེ་ན་སྐྱེ་བོ་གནས་པ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1577]
འགྲོ་བ་མེད་པ་ན༌[^889]ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་ལམ་དུ་འགྲོ་བ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1578]
གཅིག་པུ་ནི་གྲོགས་པོ་མེད་པའོ། །

[Block 1579]
བལྟས་པས་ནི་གྱེན་ཀུན་དུ་བལྟས་པར་བྱས་པ༌[^890]སྟེ།

[Block 1580 [VERSE]]
སྲིན་པོ་དང་ཤ་ཟ་དེ་དག་ལའོ། །
དེ་བས་ནགས་ནའང་ཁྱིམ་བཞིན་དུ། །

[Block 1581]
ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པ་འདི་ལྟ་བུ་དགོན་པ་དབེན་པ་འགྲོ་བ་མེད་པ་ན་ཞེས་བྱ་བ་དེའི་གཉེན་པོར་བསྟན་ཏོ། །

[Block 1582]
མཚན་མོ་དག་ཀྱང་ཉིན་པར་བཞིན། །ཞེས་བྱ་བ་ནི་གང་གི་ཚེ་སྲིན་པོ་དང་ཤ་ཟ༌[^891]རྣམས་ཀྱིས་གཞན་ཟིལ་གྱིས་གནོན་པའི་ནུས་པ་མེད་པ་དེའི་ཚེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1583]
གང་གི་ཕྱིར་སྲིན་པོ་དང་ཤ་ཟ་དེ་དག་ནི་རང་བཞིན་གྱིས༌[^892]གཏུམ་ཞིང་མ་རུངས་པ༌[^893]ཡིན་ནོ་ཞེས་བསྟན་པ་དེའི་གཉེན་པོར་བསྟན་ཏོ། །

[Block 1584]
གཅིག་པུར་གྲོགས་ཀྱི་ནང་འདུག༌[^894]འདྲ། །ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་གཅིག་པུ་ཇི་ལྟར་མི་འཇིགས་ཞེས་བྱ་བ་དེའི་གཉེན་པོར་བསྟན་ཏོ། །

[Block 1585]
ཁྱེད་ཅག་གང་ནས་ལྷགས་པའི་ཡུལ་དེའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་རྒྱུ་གསུམ་གྱིས་ཡུལ་ཇི་ལྟ་བ་བཞིན་དུ་ཡོངས་སུ་ཤེས་པའི་ཕྱིར་ཏེ། ཉམས་སད་པའི་དངོས་པོ་ཡོད་པའི་ཕྱིར་དང་། ཡུལ་གསལ་བའི་རྣམ་པ་ཡིན་པའི་ཕྱིར་དང་། ཡོན་ཏན་ཚོལ་བ༌[^895]ཡོངས་སུ་ཤེས་པས་མཁས་པའང་ཡིན་ནོ་ཞེས་བསྟན་པ་ཡིན་ཏེ། ཡོན་ཏན་འཚོལ་བ་ཆེད་ཆེར་མི་འཛིན་པ་ཞེས་བྱ་བ་འདིས་ནི་ཉམས་སད་པའི་དངོས་པོ་བསྟན་ཏོ། །

[Block 1586]
ཐོས་པར་མི་འདོད་པ་དེས། མི་དབང་གྲགས་པ་རྣམ་པར་སྤངས་པའམ། སྐལ་བ་ཅུང་ཟད་ཅིག་ཡོད་དོ་ཞེས་བྱ་བ་འདིས་ཡུལ་གསལ་བའི་རྣམ་པའོ། །

[Block 1587]
དེ་བས་ན་ཞེས་བྱ་བ་ནི་གང་ཡུལ་དེ་ལས་འདིར་ལྷགས་པའོ། །

[Block 1588]
མཐའ་འཁོབ༌[^896]ཅེས་བྱ་བའི༌[^897]ཡུལ་གྱི་ཡང་དགོན་པ་ཉིད་དེ། [^898]ཡོན་ཏན་ཤེས་པའི་སྐྱེས་བུ་མེད་པའི་ཕྱིར་ཏོ།[^899] །གང་གི་དཔུང་བྱམས་པ་སྟེ། འདིའི་དོན་ནི་མཐུན་པ་ལ་སོགས་པའི་ཐབས་ཀྱིས་ས་སྲུང་བར་བྱེད་པའོ། །

[Block 1589]
དེ་ལྟ་མོད་ཀྱི་བྱམས་པ་ལ་སོགས་པས་བསྲུང་བ༌[^900]ནི་ཆད་པ་བྱམས་པ་གང་ཡིན་པའི་དཔུང་གིས་སོ་ཞེས་བྱ་བའི་ཚིག་སྟེ། གང་དེ་ཐ་མལ་པའི༌[^901]དཔུང་ནི་ཆོ་ག་ཙམ་མོ། །

[Block 1590]
ཆོ་ག་ཙམ་ཞེས་བྱ་བ་ནི་རྒྱལ་པོ་ལ་སོགས་པའི་སྤྱོད་པའོ། །

[Block 1591]
འདི་ནི་རུ་མཚོན་ཁྲ་བོའི་དཔུང་ཡོངས་སུ་བཟུང་སྟེ། གཞན་ལ་གནོད་པའི་ཕྱིར་ནི་མ་ཡིན་ནོ། །

[Block 1592]
མི་རིགས་ཞེས་བྱ་བ༌[^902]ནི་དབྱེ་བ་ལས་བརྩམས་པའོ། །

[Block 1593]
ཁྲོ་བ་ནི་ཞེ་སྡང་བ་སྟེ་དེའི་ཚིག་གིས་སྨྲ་བའོ། །

[Block 1594]
རྩུབ་པ་ནི་སྤྱོ་བའོ།[^903] །འདི་གཉིས་ཀྱི་དབྱེ་བས་ནི་བསམ་པ་དང་སྦྱོར་བ་མེད་པར་བསྟན་ཏོ། །

[Block 1595]
བཀའ་ཁྲིམས་ཆོས་ཡིན་སྒྱུ་མེད་ནོར་ཡང་ཞེས་བྱ་བ་ནི་མཐུན་པ་ལས་བརྩམས་པའོ། །

[Block 1596]
ཆོས་ནི་བདེན་པའོ། །

[Block 1597]
བཀའ་ཁྲིམས་ནི་གཞུང་ལུགས་སོ། །

[Block 1598]
སྒྱུ་མེད་ཅེས་བྱ་བ་ནི་བྱ་བ་བསྒྲུབ་པའི༌[^904]ཕྱིར་བདེན་པ་དང་ཚིག་བསྟན་པའོ། །

[Block 1599]
ནོར་ཡང་དམ་པ་མཆོད་ཅེས་བྱ་བ་ནི་སྦྱིན་པ་ལས་བརྩམས་པ་སྟེ། དམ་པ་མཆོད་པའི་ཕྱིར་ཡིན་གྱི། རང་གི་དོན་བསྒྲུབ་པའི༌[^905]ཕྱིར་ནི་མ་ཡིན་ཏེ། དཔེར་ན་ལུགས་ཀྱི་བསྟན་བཅོས་ཀྱི་དོན་ལ་མཁས་པ་ནི་རང་གི་དོན་བསྒྲུབ་པའི༌[^906]ཕྱིར་ནོར་ཉེ་བར་སྒྲུབ་པར་བྱེད་དོ། །

[Block 1600]
དེ་ལྟར་ཡང་རྨད་དུ་བྱུང་ཡང་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ངོ་མཚར་གྱི་ཡོན་ཏན་གྱི༌[^907]མཆོག་ཏུ་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་དེ་ལྟར་རྨད་དུ་བྱུང་བའོ། །

[Block 1601]
དྲེགས་པ་ནི་མཐོ་བར་སེམས་པའོ། །

[Block 1602]
ཡ་རབས་ཀྱི་ཚུལ་ལ་གནས་པ་གང་ཡིན་པའི་སྐྱེ་བོ་དེ་ནི་ཡ་རབས་ཀྱི་གཞུང་ལུགས་ལ་རྣམ་པར་གནས་པའི་སྐྱེ་བོའོ། །

[Block 1603]
ཡང་ན་འཕགས་པའི་གཞུང་ལུགས་ལ་གནས་པའི་སྐྱེ་བོ༌[^908]གང་ཡིན་པ་དེའོ། །

[Block 1604]
རྟག་ཏུ་བདེ་ཞིང་ལོ་ལེགས་པས་རབ་ཏུ་དགའ་བ་ཕུན་སུམ་ཚོགས་ཞེས་བྱ་བ་ནི་རྟག་ཏུ་བདེ་ཞིང་དགའ་བ་དང་།[^909] རྟག་ཏུ་ལོ་ལེགས་པའི་ཕྱིར་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 1605]
ཡོན་ཏན་མང་པོ་བརྗོད་པས་དེ་ལའོ། །

[Block 1606]
སྙིང་ནས་བརྗོད་ཅིང་ཞེས་བྱ་བ་ནི་བརྩེ་བ་དང་ལྡན་པ་སྟེ། རིགས་པ་དང་མི་རིགས་པའོ། །

[Block 1607]
བདེན་པ་ཞེས་བྱ་བ་ནི་སྙན་པ་དང་ཕན་པ་ནི་བདེན་པའོ་ཞེས་བསྟན་པའོ། །

[Block 1608]
གསུམ་པོ་འདིས་ནི་གོ་རིམས་བཞིན་དུ་སེམས་ཅན་གཏི་མུག་གི་རང་བཞིན་དངོས་པོ་གང་ལ་མི་བཟོད་པའོ། །

[Block 1609]
དེ་གྲགས་པ་ཞེས་བྱ་བ་ནི་དེའི་གྲགས་པ་ཡིན་པས་དེ་གྲགས་པའོ། །

[Block 1610]
དེ་ཡིས་དེ་ལྷག་པར་གདུང་བར་འགྱུར་ཞེས་བྱ་བ་ལ། དེ་ཡིས་ཞེས་བྱ་བ་ནི་མི་བཟོད་པས་ཡིད་གདུངས་པས་ལྷག་པར་གདུང་ཞིང་ཚིག་པར་འགྱུར་རོ། །

[Block 1611]
མཐོང་བ་ཉིད་ཀྱི་དུས་ནི་མཐོང་བའི་ཚེ་ཉེ་བར་གནས་པ་དེའི་དབང་དུ་བྱས་པའོ། །

[Block 1612]
བཟའ་བ་བསླངས་པ་ནི་ཟས་བླངས་པ་བྱས་པའོ། །

[Block 1613]
ཞིམ་པོ་ནི་ཤིན་ཏུ་གཡོས་ལེགས་པ་དང་ཞིམ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1614]
ཁྱེར༌[^910]ཏེ་འོངས་ན་ཡང་ཞེས་བྱ་བ་ནི་གུས་པ་དང་བཅས་པས་མདུན་དུ་འོངས་པའོ། །

[Block 1615]
སྟག་གཟིག༌[^911]རྩྭ་སྔོན་མི་འདོད་པ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་དཔེར་ན་རི་དགས་རྣམས་ལ་རྩྭ་སྔོན་པོ་ཤིན་ཏུ་ཞིམ་པ༌[^912]ཡིན་ཡང་སྟག་ལ་སོགས་པ་མངོན་པར་མི་འདོད་པ་ཡིན་ཏེ། རྒྱལ་པོ་ལ་འོས་པའི་རྩྭ་སྔོན་པོ་ལྟ་བུར་དེ་གནོད་སྦྱིན་རྣམས་ལ་མངོན་པར་མི་འདོད་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
