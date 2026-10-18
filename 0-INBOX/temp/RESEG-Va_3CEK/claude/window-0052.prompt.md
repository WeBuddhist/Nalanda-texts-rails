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
དེ་ལ་ཅི་རིགས་པར་ཕྲ་རྒྱས་འདོད་པ་ན་སྤྱོད་པ་རིས་བཞི་དང་། གཟུགས་ན་སྤྱོད་པ་འདུས་བྱས་ལ་དམིགས་པ་རྣམས་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པ་རིས་གཉིས་དང་། ཀུན་དུ་འགྲོ་བ་རྣམས་རྒྱས་པར་འགྱུར་བར་ཤེས་པར་བྱའོ། །

[Block 1822]
བདེ་བའི༌[^1340]དབང་པོ་ལ་དམིགས་པའི༌[^1341]རྣམ་པར་ཤེས་པ་ལ་ཕྲ་རྒྱས་དུ་ཞིག་རྒྱས་པར་འགྱུར་ཞེ་ན། བདེ་བའི་དབང་པོ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་རྣམ་པ་བཅུ་གཉིས་པོ་དེ་ནི༌[^1342]རྣམ་པར་ཤེས་པ་གང་གི་དམིགས་པ་ཡིན་ཞེ་ན། རྣམ་པ་བཅུ་གཉིས་པོ་དེ་ཉིད་དང་། ཡང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་རྣམ་པ་གཉིས་ཏེ། སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ༌[^1343]མཐོང་བས་སྤང་བར་བྱ་བའི་དམིགས་པ་ཡིན་ཏེ། རྣམ་པ་བཅུ་བཞི་པོ་འདི་ནི་བདེ་བའི་དབང་པོ་ལ་དམིགས་པ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 1823]
དེ་ལ་གཟུགས་མེད་པ་ན་སྤྱོད་པ་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་མཐོང་བས་སྤང་བར་བྱ་བ་དག་བསྐྱེད༌[^1344]ནས་འདོད་པ་ན༌[^1345]སྤྱོད་པ་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་རིས་བཞི་བཞི་དང་། གཟུགས་ན་སྤྱོད་པ་འདུས་བྱས་ལ་དམིགས་པ་རྣམས་རྒྱས་པར་འགྱུར་རོ་ཞེས་བྱ་བར་ཤེས་པར་བྱ་སྟེ། ལམ་འདིས་གཞན་ཡང་ཁོང་དུ་ཆུད་པར་བྱ་སྟེ།[^1346] ཕྲ་རྒྱས་གང་དག་གི༌[^1347]སེམས་ཕྲ་རྒྱས་དང་བཅས་པའི་ཕྲ་རྒྱས་དེ་དག་སེམས་དེ་ལ་རྒྱས་པར་འགྱུར་རམ་ཞེ་ན། རྒྱས་པར་འགྱུར་བ་དག་ཀྱང་ཡོད་དེ། སེམས་དེ་དང་མཚུངས་པར་ལྡན་པ་ཡང་མ་སྤངས་ལ་དེ༌[^1348]ལ་དམིགས་པ་ཡང་མ་སྤངས་པའི་ཕྲ་རྒྱས་གང་དག་ཡིན་པའོ། །

[Block 1824]
རྒྱས་པར་མི་འགྱུར་བ་དག་ཀྱང་ཡོད་དེ། སེམས་དེ་དང་མཚུངས་པར་ལྡན་པ་སྤངས་པའི་ཕྲ་རྒྱས་གང་དག་ཡིན་པའོ། །

[Block 1825 [HEADING]]
#### སེམས་ཕྲ་རྒྱས་དང་བཅས་པ། ^2-24-3-0

[Block 1826]
དེ་ལྟར་བྱས་ན། ཉོན་མོངས་ཕྲ་རྒྱས་བཅས་རྣམ༌[^1349]གཉིས། །ཡིན་ལ། ཉོན་མོངས་ཅན་མིན་རྒྱས་འགྱུར་གྱི།[^1350] །སེམས་ཉོན་མོངས་པ༌[^1351]ཅན་ནི་དེ་དང་མཚུངས་པར་ལྡན་པ་དང་། དེ་ལ་དམིགས་པ་མ་སྤངས་པར་བྱ་བའི༌[^1352]ཕྲ་རྒྱས་རྒྱས་པར་འགྱུར་བ་རྣམས་དང་། དེ་དང་མཚུངས་པར་ལྡན་པ་སྤངས་པ༌[^1353]རྒྱས་པར་མི་འགྱུར་བ་རྣམས་ཀྱི་ཕྲ་རྒྱས་དང་བཅས་པ་ཡིན་ཏེ། དེ་དང་ལྷན་ཅིག་པའི་ཕྱིར་རོ། །

[Block 1827]
སེམས་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ནི་དེ་ལ་དམིགས་པ་མ་སྤངས་པ༌[^1354]རྒྱས་པར་འགྱུར་བ་དག་ཁོ་ནས་ཕྲ་རྒྱས་དང་བཅས་པ་ཡིན་ནོ། །

[Block 1828 [HEADING]]
### ཕྲ་རྒྱས་བཅུ་འཇུག་པའི་རིམ་པ། ^2-25-0

[Block 1829]
ཡང་ཕྲ་རྒྱས་བཅུ་པོ་འདི་དག་ཇི་ལྟར་འཇུག་པར་འགྱུར་ཞེ་ན། རེ་ཞིག་དང་པོ་ཁོ་ནར་མ༌[^1355]རིག་པ་དང་ལྡན་པ་ལས་བདེན་པ་རྣམས་ལ་ཀུན་དུ་རྨོངས་པར་འགྱུར་ཏེ། དེ་སྡུག་བསྔལ་ནས་ལམ་གྱི་བར་དུ་མི་འདོད་དོ། །

[Block 1830]
དེའི་འོག་ཏུ། རྨོངས་ལས་ཐེ་ཚོམ། ཐེ་ཚོམ༌[^1356]རྨོངས་པར་གྱུར་པ་ཕྱོགས་གཉིས་ཐོས་ནས་འདི་སྡུག་བསྔལ་ཡིན་ནམ། འདི་སྡུག་བསྔལ་མ་ཡིན༌[^1357]སྙམ་པ་དེ་ལྟ་བུ་ལ་སོགས་པའི་ཐེ་ཚོམ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1831]
དེ་ནས་ནི་ལོག་ལྟ། ཐེ་ཚོམ་ལས་ལོག་པའི་ལྟ་བ་འཇུག་སྟེ། ཐེ་ཚོམ་སྐྱེས་པ་ལོག་པར་ཐོས་པ་དང་། བསམས་པ་ལས་སྡུག་བསྔལ་མེད་དོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་ལོག་པར་ངེས་པ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1832]
དེ་ནས་འཇིག་ཚོགས་ལྟ། ལོག་པར་ལྟ་བ་ལ༌[^1358]འཇིག་ཚོགས་ལ་ལྟ་བ་འཇུག་སྟེ། སྡུག་བསྔལ་ལས་ཕུང་པོ་བསལ་ནས་བདག་ཏུ་མངོན་པར་ཞེན་པའི་ཕྱིར་རོ་ཞེས་གྲག་གོ། །

[Block 1833]
དེ་ནས་མཐར་འཛིན་འཇིག་ཚོགས་ལ་ལྟ་བ་ལས་མཐར་འཛིན་པར་ལྟ་བ་འཇུག་སྟེ། བདག་རྟག་པ་དང་ཆད་པའི་མཐར་འཛིན་པའི་ཕྱིར་རོ། །

[Block 1834]
དེ་ནས་ནི། ཚུལ་ཁྲིམས་མཆོག་འཛིན། མཐར་འཛིན་པ་ལས་ཚུལ་ཁྲིམས་དང་། བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་འཇུག་སྟེ། གང་ཁོ་ན་ལ་མཐར་འཛིན་པ་དེས་དག་པར་ཡིད་ཆེས་པའི་ཕྱིར་རོ། །

[Block 1835]
དེ་ནས་ལྟ། མཆོག་ཏུ་འཛིན་ཅེས་བྱ་བར་སྦྱར་ཏེ། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་ལས་ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་འཇུག་སྟེ། གང་གིས་དག་པར་ཡིད་ཆེས་པ་དེ་ལས༌[^1359]མཆོག་ཏུ་འཛིན་པའི་ཕྱིར་རོ། །

[Block 1836]
དེ་ནས་ནི།

[Block 1837 [VERSE]]
རང༌[^1360]གི་ལྟ་ལ་ང་རྒྱལ་ཆགས། །
དེ་ལ་ཆགས་པའི་ཕྱིར་དང་།
དེས་ཁེངས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1838]
གཞན་ལ་ཞེ་སྡང་། རང་གི་ལྟ་བ་ལ་ལྷག་པར་ཞེན་པར་གྱུར་པ་དེའི་དགྲ་བོར་གྱུར་པ་གཞན་གྱི་ལྟ་བ་ལ་ཞེ་སྡང་འཇུག་གོ། །

[Block 1839]
གཞན་དག་ནི་རང་གི་ལྟ་བ་བླངས་ནས་བོར་བ་གཞན་ལ་ཞེ་སྡང་བར་འདོད་དོ། །

[Block 1840]
[^1361]འདོད་ཆགས་ལ་སོགས་པ་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་ཀྱི་དམིགས་པ་ནི་རང་གི་རྒྱུད་ལ་ཡོད་པའི་ལྟ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1841]
དེ་ལྟར་རིམ། འདི་ནི་ཕྲ་རྒྱས་བཅུ་པོ་དེ་དག་གི་འཇུག་པའི་རིམ་པ་ཡིན་ནོ། །

[Block 1842 [HEADING]]
### ཉོན་མོངས་པ་སྐྱེ་བའི་རྒྱུ་གསུམ། ^2-26-0

[Block 1843]
སྐྱེ་བ་ནི་རྒྱུ་གསུམ་གྱིས་སྐྱེ་སྟེ།

[Block 1844 [VERSE]]
ཕྲ་རྒྱས་སྤང་བ༌[^1362]མ་ཡིན་དང་། །
ཡུལ་ནི་ཉེ་བར་གནས་པ་དང་། །
ཚུལ་བཞིན་མ་ཡིན་ཡིད་བྱེད་ལས། །

[Block 1845]
ཉོན་མོངས་སྐྱེ་སྟེ། འདི་ལྟ་སྟེ་འདོད་པའི་འདོད༌[^1363]ཆགས་ཀྱི་ཕྲ་རྒྱས་མ་སྤངས་ཤིང་ཡོངས་སུ་མ་ཤེས་པ་ཡིན། འདོད་པའི་འདོད་ཆགས་ཀྱི་ཀུན་ནས་དཀྲིས་པ་དང་། མཐུན་པའི་ཆོས་རྣམས་ཀྱང་སྣང་བར་འགྱུར་བ༌[^1364]ཡིན། དེ་ལ་ཡང་ཚུལ་བཞིན༌[^1365]མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ཡིན་ཏེ། དེ་ལྟར་ན་འདོད་པའི་འདོད་ཆགས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1846]
དེ་དག་ནི་གོ་རིམས་བཞིན་དུ་རྒྱུ་དང་ཡུལ་དང་སྦྱོར་བའི་སྟོབས་དག་ཡིན་ཏེ། ཉོན་མོངས་པ་གཞན་ཡང་དེ་བཞིན་དུ་སྐྱེ་བར་རིག་པར་བྱའོ། །

[Block 1847]
གང་ཞིག །རྒྱུ་ནི་ཚངས་པ༌[^1366]ཡིན། རེས་འགའ་ཡུལ་གྱི་སྟོབས་ཁོ་ན།[^1367] །སྐྱེའི་རྒྱུའི་སྟོབས་ཀྱིས་མ་ཡིན་ཏེ། དཔེར་ན་དགྲ་བཅོམ་པ་ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་གྱི་ལྟ་བུའོ་ཞེས་གྲག་གོ། །

[Block 1848 [HEADING]]
### ཟག་པ་དང་ཆུ་བོ་དང་སྦྱོར་བ་དང་ཉེ་བར་ལེན་པ། ^2-27-0

[Block 1849]
ཡང༌[^1368]ཕྲ་རྒྱས་དེ་དག་ཉིད་བཅོམ་ལྡན་འདས་ཀྱིས་ཟག་པ་གསུམ་དུ་གསུངས་ཏེ། འདོད་པའི་ཟག་པ་དང་། སྲིད་པའི་ཟག་པ་དང་། མ་རིག་པའི་ཟག་པའོ། །

[Block 1850]
ཆུ་བོ༌[^1369]བཞི་སྟེ། འདོད་པའི་ཆུ་བོ་དང་། སྲིད་པའི་ཆུ་བོ་དང་། ལྟ་བའི་ཆུ་བོ་དང་། མ་རིག་པའི་ཆུ་བོའོ། །

[Block 1851]
སྦྱོར་བ༌[^1370]བཞི་སྟེ། དེ་དག་ཉིད་དོ། །

[Block 1852]
ཉེ་བར་ལེན་པ༌[^1371]བཞི་སྟེ། འདོད་པ་ཉེ་བར་ལེན་པ་དང་། ལྟ་བ་ཉེ་བར་ལེན་པ་དང་། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་ཉེ་བར་ལེན་པ་དང་།[^1372] བདག་ཏུ་སྨྲ་བ་ཉེ་བར་ལེན་པའོ། །

[Block 1853 [HEADING]]
#### ཟག་པ། ^2-27-1-0

[Block 1854]
དེ་ལ་རེ་ཞིག །

[Block 1855 [VERSE]]
འདོད་ན་གཏི་མུག་མ་གཏོགས་པའི། །
ཉོན་མོངས་ཀུན་ནས་དཀྲིས་བཅས་ཟག །

[Block 1856]
མ་རིག་པ་རྣམས་མ་གཏོགས་པ༌[^1373]འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པའི༌[^1374]ཀུན་ནས་དཀྲིས་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པ༌[^1375]རྫས་བཞི་བཅུ་རྩ་གཅིག་ནི་འདོད་པའི་ཟག་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ། མ་རིག་པ་རྣམ་པ་ལྔ་མ་གཏོགས་པ་ཕྲ་རྒྱས་སུམ་ཅུ་རྩ་གཅིག་དང་ཀུན་ནས་དཀྲིས་པ་བཅུའོ། །

[Block 1857 [VERSE]]
གཟུགས་དང་གཟུགས་ནི་མེད་པ་ན། །
ཕྲ་རྒྱས་ཁོ་ན་སྲིད་པའི་ཟག །

[Block 1858]
མ་རིག་པ་མ་གཏོགས་པ༌[^1376]ཞེས་བྱ་བར་སྦྱར་ཏེ། མ་རིག་པ་རྣམས་མ་གཏོགས་པར༌[^1377]གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཕྲ་རྒྱས་རྫས་ལྔ་བཅུ་རྩ་གཉིས་ནི་སྲིད་པའི་ཟག་པ་ཡིན་ཏེ། མ་རིག་པ་རྣམ་པ་ལྔ་མ་གཏོགས་པ་གཟུགས་ན་སྤྱོད་པའི་ཕྲ་རྒྱས་ཉི་ཤུ་རྩ་དྲུག་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉི་ཤུ་རྩ་དྲུག་གོ། །

[Block 1859]
དེ་ན་ཡང་རྨུགས་པ་དང་རྒོད་པ་དང་ཀུན་ནས་དཀྲིས་པ་གཉིས་ཡོད་པ༌[^1378]མ་ཡིན་ནམ། རབ་ཏུ་བྱེད་པ་དག་ལས་ཀྱང་། སྲིད་པའི་ཟག་པ་གང་ཞེ་ན། མ་རིག་པ་རྣམས་མ་གཏོགས་པ་དེ་ལས་གཞན་པ་གཟུགས་དང་གཟུགས་མེད་པ་དང་ལྡན་པའི་ཀུན་དུ་སྦྱོར་བ་དང་། འཆིང་བ་དང་། ཕྲ་རྒྱས་དང་། ཉེ་བའི་ཉོན་མོངས་པ་དང་། ཀུན་ནས་དཀྲིས་པ་གང་དག་ཡིན་པའོ་ཞེས་བཤད་ན་ཅིའི་ཕྱིར་འདིར་དེ་མ་སྨོས་ཤེ་ན། ཁ་ཆེ་བ་རྣམས་ན་རེ་རང་དབང་ཅན་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 1860]
ཅིའི་ཕྱིར་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཕྲ་རྒྱས་རྣམས་གཅིག་ཏུ་བསྡུས་ནས་སྲིད་པའི་ཟག་པར་བཤད་ཅེ་ན།
--- END BLOCKS ---
