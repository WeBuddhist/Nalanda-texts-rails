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
[Block 1786]
གང༌[^1412]བ་ལང་མ་ཡིན་པ་ལས་ལོག༌[^1413]པའི་བ་ལང་གི་བློ་དེ་ཇི་ལྟར་ན༌[^1414]ནོག་ལ་སོགས་པ་མཐོང་བའི་རྒྱུ་མཚན༌[^1415]དུ་སྨྲ་བར་བྱེད། བ་ལང་དང་ནོག་ལ་སོགས་པ་སྒྲ་ཐ་དད་པས་ཐ་དད་དུ་སེལ་བ་ཅན་ཡིན་ཡང་ཁྱོད་ཀྱི་ལུགས་ཁས་བླངས་ནས། འགལ༌[^1416]བཞིན་དུ་ཡང་དེ་ངེས་པར་བསྟན་ཏོ། །

[Block 1787 [VERSE]]
དེ་མི་ལྟོས་ཤེས་པ་འདི་ནི། །
རང་གི་རྣམ་རྟོག་སྤྲོས་པར་ཟད། །
སེལ་བ་མིན་པའི་སྒྲ་ཡིས་ནི། །
རང་བཞིན་འགའ་ཡང་བརྗོད་མི་བྱ། །

[Block 1788]
ནོག་ལ་སོགས་པ་ལ་སྤྱིའི་ངོ་བོ་དང་ལྡན་པ་གཞན་མེད་པར་མི་ལྟོས་པ་ནི་མི་སྲིད་དོ་ཞེས་སྔར་བཤད་ཟིན་ཏོ། །

[Block 1789]
རང་གི་ངོ་བོ་ནི༌[^1417]བརྗོད་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་དེའི་སྒོ་ནས་ཐ་སྙད་དུ་མི་བྱའོ། །

[Block 1790 [HEADING]]
### དང་པོའི་ཤེས་པ་མེད་པ། ^5-14-0

[Block 1791]
གང་དག་དང་པོའི་ཤེས་པ་མེད་དོ་ཞེས་ཟེར་བ་དེ་ལ། ཐོག་མ་མེད་ཕྱིར་འདོད་པ་གྲུབ། །དང་པོའི་ཤེས་པ་ཞེས་བྱ་བ༌[^1418]ནི་མེད་པ་ཉིད་དེ། ཐ་སྙད་པའི༌[^1419]རྒྱུ་དང་འབྲས་བུ་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པ་དག་ལ་དུས་ཀྱི་ཐོག་མ་མེད་པའི་ཕྱིར་རོ། །

[Block 1792]
གང་ལ་དང་པོའི་ཤེས་པ་མེད་ན་ནི་རིགས་དང་ལྡན་པས་ཁྱབ་པར་ཡང་མི་ནུས་ལ། རིགས༌[^1420]དང་ལྡན་པ་ལས་ལོག་པའམ་མ་ལོག་པར་ཡང་མི་ནུས་ཤིང་གཅིག་མཐའ་དག་ལ་འཇུག་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་སྐྱོན་དེ་དག་ཡོད་དོ། །

[Block 1793 [HEADING]]
### ཤེས་པ་ཡང་དག་པར་རབ་ཏུ་འཇུག་པ་ཉིད་མེད་པ། ^5-15-0

[Block 1794]
གང་དག་ཤེས་པ་ཡང་དག་པར་རབ་ཏུ་འཇུག་པ་ཉིད་མེད་དོ་ཞེས༌[^1421]པ་དེ་ལ་ཡང་བརྗོད་པ།[^1422] སྤྱིའི་སྒོ་ནས་སེལ་བར་བྱེད། །དེ་གཞན་རྣམས་ལ་རིགས་ལྟ་བུར་སེལ་བར༌[^1423]བྱེད་པའི་རྫས་ནི་མེད་ཀྱི། འོན་ཀྱང་འདི་ལྟར་རྣམ་པར་བཅད་པར་བྱ་བའི་ཡུལ་ལ་གང་སྤྱིའི་ཆོས་ཀྱིས་ཡིན་ཏེ། འདི་ལ་ཡང་། རིགས་མི་མཐུན་པ༌[^1424]ལ་མ་མཐོང་བར་བསྟན་པ་ཙམ་གྱིས་རྗེས་སུ་དཔོག་གོ་ཞེས་བརྗོད་ཟིན་ཏེ། ཁྱེད༌[^1425]ཀྱི་ཕྱོགས་ལ་ཡང་ཉེས་པ་དེ་དག་མཚུངས་ཏེ། གལ་ཏེ་རིགས་མཐུན་ལ་ཁྱབ་པར༌[^1426]འཇུག་པའི་ལྟ་ན་ཁྱབ་པ་ལ་ནི་མཐའ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1795]
དེའི་ཕྱིར་འདི་ལྟར་རྭ་ཅན་ཡིན་པའི་ཕྱིར་རྟ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་རྭ་ཅན་ཉིད་མ་ལུས་པར༌[^1427]མ་མཐོང་བ་དེ་རྣམ་པར་བཅད་པ་རྗེས་སུ་དཔག་པའི་ཕྱིར་རྟ་དང་བ༌[^1428]ལ་སོགས་པ་སོ་སོར་རྣམ་པར་སེལ་བ་མ་ཡིན་ཞིང་། བ་ལང་ལ་སོགས་པ་སོ་སོ་ལ༌[^1429]འཇུག་པ་མ་ཡིན་ནོ། །

[Block 1796]
ཡིན་ན་ཡང་ལྡོག་པ་དང་འཇུག་པ་དག་ནི་བློ་དེ་བཞིན་དུ་འདི་ལ་ཡང་རིགས་པ་ཡིན་ནོ། །

[Block 1797 [HEADING]]
### བདག་གཞན་ཡོད་པར་ཁས་ལེན་པ། ^5-16-0

[Block 1798 [VERSE]]
བདག་གཞན་ཡོད་པར་ཁས་ལེན་ན། །
གཅིག་ཉིད་དུ་ཉིད་ཀྱིས༌[^1430]བརྟག་པ། །
དེ་དག་དངོས་པོ་ལ་མི་རིགས། །

[Block 1799]
གལ་ཏེ་བདག་དངོས་པོ་ལ་ཡོད་ན་ནི་དེ་ལ་གཅིག་དང་དུ་མ་ཉིད་དུ༌[^1431]བརྟག་པར་མི་རིགས་སོ། །

[Block 1800]
བདག་གཞན་ཡོད་པར་ཁས་མི་ལེན་ན་ནི་ཁྱོད་ཀྱིའང་གསལ་བ་ནུས་པར་འགྱུར། གལ་ཏེ་དངོས་པོ་ལ་མེད་ན་ནི་བརྟག་པ་དེ་དག་རིགས་ན༌[^1432]ཁྱོད་ཀྱིའང་གསལ་བ་དང་ནུས་པ་མཚུངས་པར་འགྱུར་རོ། །

[Block 1801]
གལ་ཏེ་ནུས་པ་རྣམས་ཀྱི་གསལ་བ༌[^1433]དང་མི་གསལ་བ་གཅིག་ཉིད་ཡིན་ན་ནི་གསལ་བའི་དབྱེ་བ་མེད་པར་འགྱུར་རོ། །

[Block 1802]
ཅི་སྟེ་དུ་མ་ཉིད་ཡིན༌[^1434]ན་ནི༌[^1435]ནུས་པ༌[^1436]རྣམས་ལས་གཞན་མ་ཡིན་པའི་ཕྱིར་གཙོ་བོ་གཅིག་ཅེས་བྱ་བ་འགལ་ལོ། །

[Block 1803 [VERSE]]
སྒྲ་ཡི་བརྗོད་དོན་ལ་དཔྱོད་པ། །
འདི་ཡང་དབང་པོའི་སྤྱོད་ཡུལ་མིན། །
གང་ཞིག་སྒྲ་ལ་སོགས་པ་འདིའི། །
འཇུག་པའི་དབང་པོ་སོ་སོར་མིན། །

[Block 1804]
མངོན་སུམ་གྱི་ཡུལ་ནི་བསྟན་དུ་མེད་དོ། །

[Block 1805]
བསྟན་དུ་མེད་པའི་ལྟ་ན་བདག་གཞན་མེད་པ་བདག་གཞན་ཡིན་ནོ་ཞེས་བརྗོད་པ་ཡིན་ནོ། །

[Block 1806]
དེའི་ཕྱིར་འདི་མངོན་སུམ་གྱི་འཇུག་པ་མ་ཡིན་ནོ། །

[Block 1807]
འདི་ལ་ཡང་།

[Block 1808 [HEADING]]
### ངག་གི་དོན། ^5-17-0

[Block 1809 [VERSE]]
གང་ཞིག་ཚིག་གི་བརྗོད་པ་འདི། །
ངག་ལས་དོན་དུ་རྣམ་པར་བརྟགས། །
ངག་དོན་སོ་སོར་སྣང་བརྗོད་གང་། །
དེ་ཡིས་དང་པོ་ཉེ་བར་བསྐྱེད། །

[Block 1810]
ཚིག་གི་བརྗོད་པ་ལ་དོན་མེད་དུ༌[^1437]ཟིན་ཀྱང་ཁ་ཡར་བ་ལ་ནུས་པ་མེད་པའི་ཕྱིར་ལུང་ལས་ཇི་ལྟར་གཞག་པ་ངག་ལས་རྣམ་པར་འཇོག་པར་བྱེད་དེ། རང་བཞིན་དང་རྐྱེན་བཞིན་ནོ། །

[Block 1811]
ལུང་ནས་གཞག་པ༌[^1438]དེ་ཡང་ལུང་གཞན་རྣམས་སུ་མི་རིགས་པར་འཛིན་པའི་ཕྱིར་འདི་དོན་གཞན་ཉེ་བར་གཞག་པ་ཡིན་ནོ། །

[Block 1812]
དེའི་ཕྱིར་ཚིག་གི་དོན་གཟུང་བར་བྱ་བའི་ཐབས༌[^1439]ངག་གི་དོན་དུ་སྣང་བ་དང་པོའི་མ་གོམས་པའི་སྒྲའི་དོན་དང་འབྲེལ་པ་ཡིན་ཏེ། ངག་ཉིད་དང་དེའི་དོན་དག་ལ་དངོས་སུ་ནི༌[^1440]སྒྲའི་དོན་དུ་ཐ་དད་མེད་པའི་ཕྱིར་ལ། ཕྱིས་སྒྲའི་དོན་འཛིན་པའི་མངོན་པའི་ང་རྒྱལ་གྱིས་གཞག་པ་སྟེ༌[^1441]ལྕགས་ཀྱུ་མེད་པ་པ༌[^1442]ཡིན༌[^1443]ཕྱིར་རོ། །

[Block 1813]
གང་དག་སོ་སོར་སྣང་བའི་དོན་རྣམས་ལ་ཕྱིའི་དོན་གཞན་ནམ་དེ་དང་འབྲེལ་པ་བོར་ནས་ངག་གི་དོན་དུ་རྟོགས་པར་བྱེད་པ་དེ་དག་གི་ལྟར་ན་ཡང་དེ་ནི་རྣམ་པར་རྟོག་པ༌[^1444]ཙམ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1814 [VERSE]]
ཇི་ལྟར་གོམས་པའི་ངག་དག་ལས། །
དོན་ལ་མེད་དུ་ཟིན་ཀྱང་སྐྱེ། །
རང་གི་རྐྱེན་དང་རྗེས་འབྲེལ་བས། །
རྣམ་པ་དུ་མ་སོ་སོར་རྟོགས། །

[Block 1815]
དོན་དུ་གོམས་པའི་བག་ཆགས་ལ་ལྟོས་པའི་ངག་ལས་དོན་བྱེད་པ་ལྟར་རྟོགས་པ་འབྱུང་སྟེ། རྟག་པ་ལ་སོགས་པའི་བརྗོད་པ་དང་། དེ་དང་ཁྱད་པར་མེད་པ་དག་བཞིན་ཕྱི་རོལ་གྱི་དོན་མེད་ཀྱང་རང་གི་རྐྱེན་དང་རྗེས་སུ་འབྲེལ་པས་རྣམ་པར་རྟོག་པ་སྣ་ཚོགས་པ་སྐྱེད་པར་བྱེད་དོ། །

[Block 1816]
འདི་ལྟར་རྩེད་འཇོའི་སྙན་དངགས་ཐོས་པ་ལས་ཆགས་པ་ཅན་རྣམས་ལས༌[^1445]འདོད་ཆགས་དང་རྗེས་སུ་མཐུན་པའི་ཤེས་པ་སྐྱེ་ལ། ཆགས་པ་དང་བྲལ་བ་རྣམས་ལ་ནི་ཡང་དག་པའི་ཤུགས་དང་རྗེས་སུ་མཐུན་པ་ཡིན་ནོ། །

[Block 1817 [VERSE]]
དེ་ཡང་ངག་གི་དོན་གཞན་ལས། །
རྣམ་པར་བཅད་པའི་དོན་དུ་འདོད། །
འབྲེལ་པར་ཤེས་པའི་ངག་གི་དོན། །
འདི༌[^1446]ཡང་རྗེས་དཔག་ལས་གཞན་མིན། །

[Block 1818]
སོ་སོར་སྣང་བ་ཡང་རྫས་བཞིན་ངག་གཞན་ལས་ཐ་དད་ཅིང་འབྲེལ་པ་ཤེས་པ་ལས་ཡིན་པས་རྗེས་སུ་དཔག་པ་ལས་གཞན་མ་ཡིན་ནོ། །

[Block 1819 [VERSE]]
གང་ཞིག་ངག་ལས་སྐྱེས་པ་ཡི། །
རྣམ་རྟོག་སྣ་ཚོགས་ཤེས་པ་ནི། །
དེ་ཡང་རང་རིག༌[^1447]ཡིན་པས་ན། །
མངོན་སུམ་ཉིད་ལས་གཞན་མ་ཡིན། །

[Block 1820]
རྟོག་པ༌[^1448]ནི་རང་རིག་ཡིན་པའི་ཕྱིར་ན་མངོན་སུམ་ཉིད་ཡིན་པས་དེ་ལས་གཞན་དུ་དབྱེ་བར་མི་བྱའོ། །

[Block 1821 [HEADING]]
### འདོད་རྒྱལ་བ་ལ་དོན་དབྱེ་བ། ^5-18-0

[Block 1822]
གལ་ཏེ་རེ་ཞིག་རྒྱུ་མཚན་ཅན་གྱི་སྒྲ་རྣམས་ལ་ལྟ་དོན་གང་དག་བསལ་བའི༌[^1449]སྒོ་ནས་དོན་མངོན་པར་བརྗོད་པ་རིགས་གྲངས་ན་འདོད་རྒྱལ་བ་རྣམས་ལ་ཇི་ལྟར་ཞེ་ན། འདོད་རྒྱལ་བ་ལ་དོན༌[^1450]དབྱེ་བས། །འདོད་རྒྱལ་བ་ལ་ཤིང་ཏོག་དིད་ཐཱ་ལ་སོགས་པའི་སྒྲ་སྤྱི་བརྗོད་པ་ཡིན་ཞིང་སྤྱི་དེའི་དབྱེ་བས་རྗོད་པར་བྱེད་དོ། །

[Block 1823 [HEADING]]
### རིགས་དང་མཐུན་པའི་འདུས་པ་སྒྲ། ^5-19-0

[Block 1824]
གལ་ཏེ་རིགས་དང་མཐུན་པའི་འདུས་པ་སྒྲ་དག་ལ་བྱེ་བྲག་ཅི་ཡོད་ཅེ་ན། ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 1825]
རིགས་ཀྱི་སྒྲ་ཡང་གྲགས་པའི་དབང་གིས། ཁ་ཅིག་ཏུ་ཡན་ལག་སོ་སོ་ལ་འདོགས་པར་འདོད་དེ། དཔེར་ན་གྲོང་གི་ཕག་པ་བཟའ་བྱ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །
--- END BLOCKS ---
