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
[Block 1821]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་འཁོར་བའི་སྐྱོན་བསྒྲགས་ཤིང་བརྗོད་པའོ་ཞེས་བྱ་བ་ལ་ཕུང་པོ་གཅིག་ནས་གཅིག་ཏུ་ཚེའི་ཉིང་མཚམས་སྦྱོར་ཞིང་སྐྱེ་བ་ནི་འཁོར་བའོ། །

[Block 1822]
འཁོར་བའི་སྐྱོན་ནི་འཁོར་བའི་ཉེས་པ་སྟེ། རྒ་བ་དང་འཆི་བ་ལ་སོགས་པའི་སྡུག་བསྔལ་མང་པོ་དང་ལྡན་པ་སྟེ། དེ་ལྟར་འཁོར་བའི་སྐྱོན་བསྒྲགས་ཤིང་འཆད་པ་ནི་ཚིག་འབྲུའོ། །

[Block 1823]
དོན་ཞེས་བྱ་བ་ནི༌[^1580]འཁོར་བ་ལ་མི་དམིགས་པར་རྟོགས་པའོ༌[^1581]ཞེས་བྱ་བ་ལ་ཉེས་པ་དུ་མའི་གནས་སུ་གྱུར་པའི་འཁོར་བ་དེ་ཡང་རང་བཞིན་གྱིས་སྟོང་ཞིང་མེད་པར་ཁོང་དུ་ཆུད་པ་ནི་དོན་ཞེས་བྱའོ། །

[Block 1824]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་མྱ་ངན་ལས་འདས་པའི་ཡོན་ཏན་དང་ཕན་ཡོན་བརྗོད་ཅེས་བྱ་བ་ལ། ཉོན་མོངས་པ་མ་ལུས་པར་སྤངས་ནས་ཚེ་གཅིག་ནས་གཅིག་ཏུ་ཉིང་མཚམས༌[^1582]སྦྱོར་བའི་རྒྱུན་ཆད་པ༌[^1583]ནི་མྱ་ངན་ལས༌[^1584]འདས་པའོ། །

[Block 1825]
མྱ་ངན་ལས་འདས་པའི་ཡོན་ཏན་ནི་ཞི་བ་དང་གྱ་ནོམ་པ་དང་། ངེས་པར་འབྱུང་བ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1826]
ཕན་ཡོན་ནི་སྡུག་བསྔལ་ཐམས་ཅད་སྤངས་ཤིང་བདེ་བ་རྣམས་ཀྱི་རྟེན་དུ་གྱུར་པ་སྟེ། གང་མྱ་ངན་ལས་འདས་པའི་ཡོན་ཏན་དང་། ཕན་ཡོན་ཆད༌[^1585]ཅིང་བརྗོད་པ་ནི་ཚིག་འབྲུ་ཞེས་བྱའོ། །

[Block 1827]
དོན་ཞེས་བྱ་བ་ནི་རང་བཞིན་གྱིས༌[^1586]ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས་འོད་གསལ་བ། ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་གློ་བུར་དང་། མ་འདྲེས་པ་ཡིན་པས་རང་བཞིན་གྱིས་མྱ་ངན་ལས་འདས་པ་སྟེ། དེ་ལྟར་ན་རང་བཞིན་གྱིས༌[^1587]མྱ་ངན་ལས་འདས་པའི་ཆོས་དེ་དག་ལ་ཡང་ཉེས་པ་དང་སྐྱོན་དང་ཡོན་ཏན་དང་ཕན་ཡོན་དུ་མི་རྟོགས་པ༌[^1588]ནི་དོན་ཞེས་བྱའོ། །

[Block 1828]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་ཐེག་པ་ཇི་ལྟར་རྣམ་པར་གཞག་པ་བཞི་ཞེས་བྱ་བ་ལ། ཐེག་པ་གསུམ་ཇི་ལྟར་འཇིག་རྟེན་དུ་རྣམ་པར་གཞག་པ༌[^1589]དེ་བཞིན་དུ་སོ་སོར་མཚན་ཉིད་མ་ནོར་བར་སྟོན་ཅིང་འཆད་པ་འམ། གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་ཇི་ལྟར་འཇིག་རྟེན་དུ་གཞག་པ་དེ་བཞིན་དུ་སོ་སོར་མཚན་ཉིད་མ་ནོར་བར༌[^1590]འཆད་པ་ནི་ཚིག་འབྲུ་ཞེས་བྱའོ། །

[Block 1829]
དོན་ཞེས་བྱ་བ་ནི་གང་ཆོས་ཀྱི་དབྱིངས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ཐེག་པ་གསུམ་ལ་སོགས་པ་ཇི་སྙེད་ཆོས༌[^1591]ཐ་དད་པར་གཞག་པའི༌[^1592]རྣམ་པ་དོན་དམ་པར་ཚུལ་གཅིག་པ་སོ་སོར་དབྱེར་མེད་པར་ཁོང་དུ་ཆུད་ཅིང་ཤེས་པ་ནི་དོན་ཞེས་བྱའོ། །

[Block 1830]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་བདོག་པ༌[^1593]ཐམས་ཅད་ཡོངས་སུ་གཏོང་བ་བསྟན་པ་ཞེས་བྱ་བ་ལ། ནོར་དང་འབྲུ་ལ་སོགས་པ་བདག་གིར་བྱས་པའི་དངོས་པོ་ཐམས་ཅད་གཞན་ལ་གཏོང་བར༌[^1594]བསྟན་ཅིང་བཤད་པ་ནི་ཚིག་འབྲུའོ། །

[Block 1831]
དོན་ཞེས་བྱ་བ་ནི་གང་འཁོར་གསུམ་ཡོངས་སུ་དག་པའི་ཞེས་བྱ་བ་ལ་གཏོང་བ༌[^1595]པོ་དང་། གཏོང་བའི༌[^1596]དངོས་པོ་དང་། ལེན་པ་གསུམ་ཆར་ཡང་རང་བཞིན་མེད་པར་ཤེས་པ་ནི་དོན་ཏོ། །

[Block 1832]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་ལུས་དང་ངག་དང་ཡིད་ཀྱི་སྡོམ་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ༌[^1597]ཚུལ་ཁྲིམས་དང་ཚུལ་ཁྲིམས་ཀྱི་འཁོར་དུ་གཏོགས་པ་ཆོས་མིང་གིས་སྨོས་པ་རྣམས་ཡང་དག་པ་མནོད་ཅིང་བླང་བར་བསྟན་ཅིང་བཤད་པ་ནི་ཚིག་འབྲུའོ། །

[Block 1833]
དེ་ལ་ལུས་དང༌[^1598]ངག་དང་ཡིད་ཀྱི་སྡོམ་པ་གསུམ་ནི་ལུས་ཀྱིས་ལེགས་པར་སྤྱོད་པ་ལ་འཇུག་པ་དང་། ངག་གིས་ལེགས་པར་སྤྱོད་པ་ལ་འཇུག་པ་དང་། ཡིད་ཀྱིས་ལེགས་པར་སྤྱོད་པ་ལ་འཇུག་པ་ནི་འཇུག་པའི་ཚུལ་ཁྲིམས་སོ། །

[Block 1834]
ཚུལ་ཁྲིམས་ཞེས་བྱ་བའི་སྒྲས་ནི་ཡན་ལག་དྲུག་པའི་ཚུལ་ཁྲིམས་ལ་བྱ་བར་འདོད་དོ། །

[Block 1835]
བསླབ་པའི་སྒྲས་ནི་སྲོག་གཅོད་པ་ལས་ཕྱིར་ལྡོག་པ་དང་། མ་བྱིན་པར་ལེན་པ་ལས་ཕྱིར་ལྡོག་པ་ལ་སོགས་པ་ལ་སློབ་པས༌[^1599]ལྡོག་པའི་ཚུལ་ཁྲིམས་ལ་བྱའོ། །

[Block 1836]
སྦྱངས་པའི་ཡོན་ཏན་ནི་སྦྱངས་པའི་ཡོན་ཏན༌[^1600]བཅུ་གཉིས་རྣམས་སོ། །

[Block 1837]
ཡོ་བྱད་བསྙུངས་པ་ནི་ལྷུང་བཟེད་དང་ཆོས་གོས་ལ་སོགས་པ་མང་པོ་མི་འཛིན་པའོ། །

[Block 1838]
ཡོངས་སུ་དག་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་དང་ཚུལ་ཁྲིམས་ཀྱི་ཡན་ལག་ཏུ་གཏོགས་པའི་ཆོས་དེ་དག་རང་བཞིན་གྱིས་དག་པར་ཤེས་པ་ནི་དོན་ཏོ། །

[Block 1839]
ཡང་དག་པར་འཇོམས་ཤིང་བཟོད་པའི་སྟོབས་དང་ངེས་པ་བསྟན་པ་ཞེས་བྱ་བ་རབ་ཏུ་འཇོམས་པ༌[^1601]ནི་གནོད་སེམས་ལ་སོགས་པ་སྤོང་པའོ། །

[Block 1840]
བཟོད་པ་ནི་གཞན་གྱིས་གནོད་པ་བྱས་ཀྱང་སེམས་མི་འཁྲུག༌[^1602]ཅིང་གནོད་པ་ཉམས་སུ་ལེན་པ་སྟེ། སྟོབས་ནི་བཟོད་པ་དང་མི་མཐུན་པའི་ཆོས་ཁོང་ཁྲོ་བ་ལ་སོགས་པའི་དབང་དུ་མི་འགྲོ་བའོ། །

[Block 1841]
ངེས་པ་ནི་སེམས་ཅན་ལ་གནོད་པ་མི་བྱེད་པ་སྟེ། དེ་ལྟ་བུ་བསྟན་ཅིང་བཤད་པ་ནི་ཚིག་འབྲུའོ། །

[Block 1842]
དོན་ཞེས་བྱ་བ་ནི་གང་མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པ་ཞེས་བྱ་བ་ལ་ཆོས་ཐམས་ཅད་མ་བྱུང་བ༌[^1603]སྐྱེས་པར་ཁོང་དུ་ཆུད་ཅིང་སྟོང་པ་ཉིད་ཀྱི་ཆོས་ལ་མི་སྐྲག་པ་ཐོབ་པ་ནི་དོན་ཞེས་བྱའོ། །

[Block 1843]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་དགེ་བའི་རྩ་བ་ཐམས་ཅད་ཡང་དག་པར་སྒྲུབ་པ་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་དགེ་བའི་རྩ་བ་ཐམས་ཅད་ཡང་དག་པར་བླང་ཞིང་བསྒྲུབ་པར་བྱ་བའི༌[^1604]ཕྱིར། བརྩོན་འགྲུས་བརྩམ་པར༌[^1605]བྱ་བ༌[^1606]བསྟན་ཅིང་བཤད་པ་ནི་ཚིག་འབྲུའོ། །

[Block 1844]
དོན་ཞེས་བྱ་བ་ནི་གང་བླང་བ་དང་དོར་བ་ལ་མི་གནས་ཞེས་བྱ་བ་ལ་དགེ་བའི་ཆོས་བླང་བ་ལ་ཡང་མི་གནས། མི་དགེ་བའི་ཆོས་སྤང་བ་ལ་ཡང་མི་གནས་ཏེ། བྱ་བ་གཉིས་མཐར་ཕྱིན་པའི་བརྩོན་འགྲུས་ཀྱི་འབྲས་བུ་དང་ལྡན་པ་ལ་དོན་ཞེས་བྱའོ། །

[Block 1845]
སྙོམས་པར་འཇུག་པ་བསྟན་པ་ཞེས་བྱ་བ་ནི་མིང་གིས་སྨོས་པའི་ཆོས་དེ་རྣམས་ཀྱི་མཚན་ཉིད་གང་ཡིན་པ་བཤད་པ་ནི་ཚིག་འབྲུའོ། །

[Block 1846]
ཆོས་དེ་དག་གི་འབྲས་བུ་འགོག་པའི་སྙོམས་པར་འཇུག་པ་མངོན་དུ་བྱས་ཤིང་། ཁོང་དུ་ཆུད་པ་ནི་དོན་ཏོ། །

[Block 1847]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་ཐོས་པ་ཐམས་ཅད་འཛིན་པ་ཞེས་བྱ་བ་ལ་ཤེས་རབ་བསྐྱེད་པའི༌[^1607]རྩ་བར་གྱུར་པའི་དགེ་བའི་བཤེས་གཉེན་ལ་བརྟེན་ནས་དམ་པའི་ཆོས་སུ་ཉན་ཅིང་ཇི་ལྟར་མཉན་པའི་ཆོས་ཀྱི་དོན་དང་ཚིག་མི་བརྗེད་པར་འཛིན་པ་ནི་ཚིག་འབྲུའོ། །

[Block 1848]
དོན་དམ་པར་ནི༌[^1608]ཆོས་ཐམས་ཅད་བཤད་པ་དང་ཉན་པ་ལས་འདས་སོ་ཞེས་གང་སྟོང་པ་བརྗོད་དུ་མེད་པའི་དོན་ཞེས་པ༌[^1609]ནི་དོན་ཏོ། །

[Block 1849]
དོན་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་བསྒྲུབ་པའི༌[^1610]འབྲས་བུ་མངོན་སུམ་དུ་བྱེད་ཅེས་བྱ་བ་ལ། བྱང་ཆུབ་ཀྱི་ཕྱོགས་སུམ་ཅུ་རྩ་བདུན་བསྒྲུབ་པའི༌[^1611]སོ་སོའི་འབྲས་བུ་རེ་རེ་ནས་མངོན་སུམ་དུ་བྱེད་པའམ། དེ་དག་ཅིའི༌[^1612]འབྲས་བུ་སངས་རྒྱས་སུ་གྲུབ་པའི་མཚན་ཉིད་མངོན་སུམ་དུ་བྱེད་པ་ནི་དོན་ཏོ། །

[Block 1850]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་སྡུག་བསྔལ་དང་ཞེས་བྱ་བ་ལ། སེམས་ཅན་གཞན་དག་ལ་འདི་ནི་སྡུག་བསྔལ་གྱི་བདེན་པ། འདི་ནི་ཀུན་འབྱུང་བའི་བདེན་པ། འདི་ནི་ལམ་གྱི་བདེན་པ་ཞེས་བདེན་པ་གསུམ་འཆད་ཅིང་བསྟན་པ་ནི་ཚིག་འབྲུའོ། །

[Block 1851]
དོན་ཞེས་བྱ་བ་ནི་གང་འགོག་པ་མངོན་སུམ་དུ་བྱེད༌[^1613]ཅེས་བྱ་བ་ལ་དེ་ལྟར་བསྟན་ཅིང་བསྒྲུབ་པའི༌[^1614]འབྲས་བུ་འགོག་པའི་བདེན་པ་མངོན་དུ་བྱེད་པ་ནི་དོན་ཏོ། །

[Block 1852]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་མ་རིག་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་མ་རིག་པ་ནས་བརྩམས་ཏེ། རྒ་ཤིའི་བར་དུ་འཁོར་བར་འཇུག་པའི་རྒྱུ་བསྟན་ཅིང་འཆད་པ་ནི་ཚིག་འབྲུའོ། །

[Block 1853]
མ་རིག་པ་འགོག་པ་ནས་རྒ་ཤི་འགོག་པའི་བར་དུ་འཁོར་བ་ལས་བཟློག་པའི༌[^1615]རང་བཞིན་ནི་དོན་ཏོ། །

[Block 1854]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་ཞི་གནས་དང་། ལྷག་མཐོང་གི་ཚོགས་བསྟན་པ་ཞེས་བྱ་བ་ལ་ཚུལ་ཁྲིམས་རྣམ་པར་དག་པ་ལ་གནས་ཏེ་ཟས་ལ་ཚོད་རིག་པ་དང་། འདུ་འཛི་མང་པོའི་ནང་ན་མི་གནས་པ་དང་། ནམ་གྱི་ཆ་སྟོད་དང་ཆ་སྨད་ལ་མི་ཉལ་བའི་ཞི་གནས་དང་ལྷག་མཐོང་གི་ཚོགས་ལ་བརྟེན་ནས་ཞི་གནས་དང༌[^1616]ལྷག་མཐོང་སྒྲུབ་པར༌[^1617]བསྟན་ཅིང་བཤད་པ་ནི་ཚིག་འབྲུའོ། །

[Block 1855]
དོན་ཞེས་བྱ་བ་ནི་གང་རིག༌[^1618]པ་དང་རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་ཞེས་བྱ་བ་ལ་དེ་ལྟར་ཚུལ་ཁྲིམས་ལ་གནས་ནས་ཞི་གནས་དང་ལྷག་མཐོང་བསྒྲུབ་པ༌[^1619]ལས་འདི་ནི་སྡུག་བསྔལ་གྱི་བདེན་པ། འདི་ནི་ཀུན་འབྱུང་བའི་བདེན་པ། འདི་ནི་འགོག་པའི་བདེན་པ། [^1620]འདི་ནི་ལམ་གྱི་བདེན་པ་ཞེས་རྣམ་པར་རིག་པ་སྐྱེས་པ་དང་། དེའི་འོག་ཏུ་སྡུག་བསྔལ་བ་ནི་ཤེས་པར་བྱས། ཀུན་འབྱུང་ནི་སྤངས། ལམ་ནི་བསྒོམས། འགོག་པ་ནི་མངོན་དུ་བྱས་སོ་ཞེས་རྣམ་པར་གྲོལ་བ༌[^1621]སྐྱེས་པ་དང་། དེ་ལ༌[^1622]སྡུག་བསྔལ་ཤེས་ཟིན་པས། ཤེས་པར་བྱ་མི་དགོས། ཀུན་འབྱུང་བ་སྤངས་པས་སྤང་མི་དགོས། ལམ་བསྒོམས་པས་བསྒོམ་མི་དགོས། འགོག་པ་མངོན་དུ་བྱས་པས་མངོན་དུ་བྱ་མི་དགོས་ཞེས་རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་སྐྱེས་པ་ནི་དོན་ཏོ། །

[Block 1856]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་འདོད་ཆགས་དང་ཞེ་སྡང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་སེམས་ཅན་རྣམས་ཀྱི་ཉོན་མོངས་པ་བརྒྱད་ཁྲི་བཞི་སྟོང་གི་གཉེན་པོ་མི་གཙང་བ་དང་བྱམས་པ་ལ་སོགས་པ་བསྟན་ཅིང་བཤད་པ་ནི་ཚིག་འབྲུའོ། །

[Block 1857]
དོན་ཞེས་བྱ་བ་ནི་གང་སེམས་རྣམ་པར་གྲོལ་བ་མི་འཁྲུག་པའི་ཡེ་ཤེས་ཞེས་བྱ་བ་ལ་ཉོན་མོངས་པ་དེ་རྣམས་ལས་རྣམ་པར་གྲོལ་པའི་ཡེ་ཤེས་མི་ཉམས་པ་ནི་དོན་ཏོ། །

[Block 1858]
ཚིག་འབྲུ་ཞེས་བྱ་བ་ནི་གང་སྒྲིབ་པ་དང་སྒྲིབ་པར་འགྱུར་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་སྒྲིབ་པ་ནི་ཤེས་བྱ་དང་ཉོན་མོངས་པའི་སྒྲིབ་པའོ། །

[Block 1859]
སྒྲིབ་པར་འགྱུར་བ་ནི་འདོད་པ་ལ་འདུན་པ་དང་གནོད་སེམས་ལ་སོགས་པའི་སྒྲིབ་པ་ལྔ་ལ་བྱ་སྟེ། དེ་དག་ནི་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་དང་མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་བྱ་བ་ལ་བསྒྲིབས་པ༌[^1623]སྟེ། དེ་དག་སྤང་བར་བྱའོ་ཞེས་བསྟན་ཅིང་འཆད་པ་དེ་ནི་ཚིག་འབྲུའོ། །

[Block 1860]
དོན་ཞེས་བྱ་བ་ནི་གང་སྒྲིབ་པ་མེད་པའི་ཡེ་ཤེས་དང་རྣམ་པར་ཐར་པ་ཞེས་བྱ་བ་ལ་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་པ་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་དང་ཉོན་མོངས་པའི་སྒྲིབ་པ་ཐམས་ཅད་སྤངས་པ། མྱ་ངན་ལས་འདས་པ་ནི་དོན་ཏོ། །
--- END BLOCKS ---
