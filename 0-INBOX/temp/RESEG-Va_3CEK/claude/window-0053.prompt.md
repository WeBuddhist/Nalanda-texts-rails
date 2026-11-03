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

[Block 1861 [VERSE]]
དེ་ལུང་མ་བསྟན་ཁ་ནང་བལྟས། །
མཉམ་གཞག་པ༌[^1379]ཡི་ཕྱིར་གཅིག་བྱས། །

[Block 1862]
དེ་གཉི་ག་ཡང་ལུང་དུ་མ་བསྟན་པ་དང་། ཁ་ནང་དུ་བལྟས་ཏེ་འཇུག་པ་དང་། མཉམ་པར་གཞག་པའི་ས་པ་དག་ཡིན་པའི་ཕྱིར་ཆོས་མཐུན་པ་རྣམ་པ་གསུམ་གྱིས་གཅིག་ཏུ་བྱས་ཏེ། རྒྱུ་གང་གིས་སྲིད་པའི་འདོད་ཆགས་ཞེས་བཤད་པ་དེ་ཉིད་ཀྱི༌[^1380]སྲིད་པའི་ཟག་པ་ཞེས་བྱའོ། །

[Block 1863]
ད༌[^1381]ནི་མ་རིག་པའི༌[^1382]ཁམས་གསུམ་པ་རྫས་བཅོ་ལྔ་ནི་མ་རིག་པའི་ཟག་པ་ཞེས་བྱ་བར་གྲུབ་བོ། །ཅིའི་ཕྱིར་འདི་ལོགས་ཤིག་ཏུ་རྣམ་པར་གཞག་ཅེ་ན། དེ་དག་ཐམས་ཅད་ཀྱི།

[Block 1864 [VERSE]]
རྩ་བ་མ་རིག་ཡིན་པས་ན། །
ལོགས་ཤིག་ཏུ་ནི་ཟག་པར་བསྟན། །

[Block 1865 [HEADING]]
#### ཆུ་བོ་དང་སྦྱོར་བ། ^2-27-2-0

[Block 1866]
ཟག་པ་དེ་དག་ཇི་སྐད་དུ་བཤད་པ་ལྟར། ཆུ་བོ་སྦྱོར་བའང་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 1867]
ལྷ༌[^1383]རྣམས་གསལ༌[^1384]ཕྱིར་ལོགས་ཤིག་བསྟན། །ལྟ་བ་རྣམས་མ་གཏོགས་པ་འདོད་པའི་ཟག་པ་ཁོ་ནར༌[^1385]འདོད་པའི་ཆུ་བོ་དང་། འདོད་པའི་སྦྱོར་བ་ཡིན་ལ། དེ་བཞིན་དུ་སྲིད་པའི་ཟག་པ་ཁོ་ན་སྲིད་པའི་ཆུ་བོ་དང་། སྲིད་པའི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 1868]
དེ་དག་ནི་བསལ་བའི་ཕྱིར་ཆུ་བོ་དང་སྦྱོར་བ་དག་ནི༌[^1386]ནང་དུ་ལོགས་ཤིག་ཏུ་བསལ་བའི༌[^1387]རྣམ་པར་གཞག་གོ་ཞེས་གྲག་གོ། །

[Block 1869 [VERSE]]
ཟག་པ་མ་ཡིན་གྲོགས་མེད་རྣམས། །
འཇོག་པའི་རྗེས་སུ་མི་མཐུན་ལོ། །

[Block 1870]
ཟག་པ་རྣམས་ཀྱི་ངེས་པའི་ཚིག་ནི་འཇོག་པར་བྱེད་པས་ན་ཞེས་འོག་ནས་འཆད་ན། ལྟ་བ་རྣམས་འབའ་ཞིག་ནི་བསལ་བའི༌[^1388]ཕྱིར་འཇོག་པའི་རྗེས་སུ་མཐུན་པ་མ་ཡིན་པས་དེའི་ཕྱིར་ཟག་པ་དག་ཏུ་ལོགས་ཤིག་ཏུ་མ་བཞག་གི་བསྲེས་ཏེ་ནི་བཞག་གོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 1871]
དེ་ལྟར་ན་འདོད་པའི་ཆུ་བོ་ནི་རྫས་ཉི་ཤུ་རྩ་དགུ་སྟེ། འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། ང་རྒྱལ་བཅོ་ལྔ་དང་། ཐེ་ཚོམ་བཞི་དང་། ཀུན་ནས་དཀྲིས་པ་བཅུའོ། །

[Block 1872]
སྲིད་པའི་ཆུ་བོ་ནི་རྫས་ཉི་ཤུ་རྩ་བརྒྱད་དེ། འདོད་ཆགས་དང་ང་རྒྱལ་ཉི་ཤུ་དང་། ཐེ་ཚོམ་བརྒྱད་དོ། །

[Block 1873 [VERSE]]
ལྟ་བའི་ཆུ་བོ་ནི་རྫས་སུམ་ཅུ་རྩ་དྲུག་གོ། །
མ་རིག་པའི་ཆུ་བོ་ནི་རྫས་བཅོ་ལྔ་སྟེ།
སྦྱོར་བ་ཡང་ཆུ་བོ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 1874 [HEADING]]
#### ཉེ་བར་ལེན་པ། ^2-27-3-0

[Block 1875 [VERSE]]
ཇི་སྐད་བཤད་ཉིད་མ་རིག་བཅས། །
ཉེར་ལེན་རྣམས་ཏེ་ལྟ་རྣམ༌[^1389]གཉིས། །

[Block 1876]
ཕྱེ་བའི་ཕྱིར་རོ། །

[Block 1877]
འདོད་པའི་སྦྱོར་བ་མ་རིག་པ་དང་བཅས་པ་རྫས་སུམ་ཅུ་རྩ་བཞི་ཁོ་ན་འདོད་པ་ཉེ་བར་ལེན་པ་ཡིན་ཏེ། འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། ང་རྒྱལ་དང་། མ་རིག་པ་ཉི་ཤུ་དང་། ཐེ་ཚོམ་བཞི་དང་། ཀུན་ནས་དཀྲིས་པ་བཅུའོ། །

[Block 1878]
སྲིད་པའི་སྦྱོར་བ་ཉེ་བར༌[^1390]མ་རིག་པ་དང་བཅས་པ་རྫས་སུམ་ཅུ་རྩ་བརྒྱད་ཁོ་ན་བདག་ཏུ་སྨྲ་བ་ཉེ་བར་ལེན་པ་ཡིན་ཏེ། འདོད་ཆགས་དང་། ང་རྒྱལ་དང་། མ་རིག་པ་སུམ་ཅུ་དང་། ཐེ་ཚོམ་བརྒྱད་དོ། །

[Block 1879]
ལྟ་བའི་སྦྱོར་བ་ལས་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས༌[^1391]ཕྱུང་སྟེ། ལྟ་བ་ལ༌[^1392]ཉེ་བར་ལེན་པ་རྫས་སུམ་ཅུ་ཡིན་ནོ། །

[Block 1880]
ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་ཉེ་བར་ལེན་པ་ནི་རྫས་དྲུག་གོ། །ཅིའི་ཕྱིར་ལྟ་བ་རྣམས་ལས་ཕྱུང་ཞེ་ན། ལམ་གྱི་དགྲར་འགྱུར་བའི༌[^1393]ཕྱིར་དང་། ཕྱོགས་གཉི་ག་བསླུ་བའི༌[^1394]ཕྱིར་ཏེ། འདིས་ཁྱིམ་པ་རྣམས་ཀྱང་ལམ་མ་ཡིན་པ༌[^1395]ལ་ལམ་དུ་འདུ་ཤེས་པས་ཟས་མི་ཟ་བ་ལ་སོགས་པས་བསླུས་ལ། རབ་ཏུ་བྱུང་བ་རྣམས་ཀྱང་ཡུལ་ཡིད་དུ་འོང་བ་ཡོངས་སུ་སྤངས་པས་དག་པར་ཡིད་ཆེས་པས་བསླུས༌[^1396]སོ། །

[Block 1881]
ཅིའི་ཕྱིར་མ་རིག་པ་བསྲེས་ཏེ་ཉེ་བར་ལེན་པར་བཤད་ལ་ལོགས་ཤིག་ཏུ་མ་བཤད་ཅེ་ན། སྲིད་པ་འཛིན་པའི་ཕྱིར་ཉེ་བར་ལེན་པ་དག་ཡིན་ནོ། །

[Block 1882]
མ་རིག་པ། འཛིན་པར་བྱེད་པ་མིན་ཕྱིར་བསྲེས། །མ་རིག་པ་ནི་མི་ཤེས་པའི་མཚན་ཉིད་ཀྱིས་མི་གསལ་བའི་ཕྱིར་འཛིན་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་བསྲེས་སོ་ཞེས་གྲག་གོ། །

[Block 1883]
བཅོམ་ལྡན་འདས་ཀྱིས་མདོ་ལས་ནི་འདོད་པའི་སྦྱོར་བ་གང་ཞེ་ན་ཞེས་བྱ་བ་ནས་རྒྱས་པར་འདིའི་འདོད་པ་རྣམས་ལ་འདོད་པ་ལ་འདོད་ཆགས་པ་དང་། འདོད་པ་ལ་འདུན་པ་དང་། འདོད་པ་ལ་སྲེད་པ་དང་། འདོད་པ་ལ་དད༌[^1397]ཆེ་བ་དང་། འདོད་པ་ལ་འདོད་པས་བརྒྱལ་བ་དང་། འདོད་པ་ལ་ཞེན་པ་དང་།[^1398] འདོད་པ་ལ་དགའ་བ་དང་། འདོད་པ་ལ་འཆུམས་པ་དང་། འདོད་པ་ལ་ལྷག་པར་ཆགས་པ་ཡོད་པ་གང་ཡིན་པ་དེས་འདིའི་སེམས་ཡོངས་སུ་གཏུགས་ཏེ་གནས་པ་འདི་ནི་འདོད་པའི་སྦྱོར་བ་ཞེས་བྱའོ་ཞེས་བྱ་བའི་བར་དང་། ལྟ་བའི་སྦྱོར་བ་ཡང་དེ་དང༌[^1399]འདྲ་བའི་བར༌[^1400]གསུངས་སོ། །

[Block 1884]
མདོ་གཞན་དག་ལས་འདུན་པའི་འདོད་ཆགས་ཀྱང་ཉེ་བར་ལེན་པ་ཡིན་པར་གསུངས་ཏེ། དེའི་ཕྱིར་འདོད་པ་ལ་སོགས་པ་ལ་འདུན་པའི་འདོད་ཆགས་གང་ཡིན་པ༌[^1401]ནི་འདོད་པ་ཉེ་བར་ལེན་པ་ལ་སོགས་པ་ཡང་ཡིན་པར་ཤེས་སོ། །

[Block 1885]
མདོ་དག་ལས་ཕྲ་རྒྱས་རྣམས་ཁོ་ན་ཟག་པ་དང་། ཆུ་བོ་དང་། སྦྱོར་བ་དང་། ཉེ་བར་ལེན་པའི་མིང་དུ་གསུངས་པ་འདི་ནི་བཤད་ཟིན་ཏོ། །

[Block 1886 [HEADING]]
#### ཕྲ་རྒྱས་ནས་ཉེ་བར་ལེན་པའི་བར་གྱི་དོན། ^2-27-4-0

[Block 1887 [HEADING]]
##### ཕྲ་རྒྱས་ཀྱི་དོན། ^2-27-4-1-0

[Block 1888]
ཡང་ཕྲ་རྒྱས་ཀྱི་དོན་ནི་ཅི་ཡིན། ཉེ་བར་ལེན་པའི་བར་གྱི་དོན་ནི་ཅི་ཡིན་ཞེ་ན། གང་ཕྱིར་དེ་དག་ཕྲ་བ་དང་།

[Block 1889 [VERSE]]
རྗེས་འབྲེལ་རྣམ་གཉིས་རྒྱས་འགྱུར་དང་། །
རྗེས་སུ་འབྲང་བ་དེ་ཡི་ཕྱིར། །
ཕྲ་རྒྱས་རྟག༌[^1402]ཏུ་བཤད་པ་ཡིན། །

[Block 1890]
དེ་ལ་ཕྲ་བ་རྣམས༌[^1403]ནི་རྟོགས་པར་དཀའ་བས་རྒྱུ་བ་ཕྲ་བའི་ཕྱིར་རོ། །

[Block 1891]
རྗེས་སུ་འབྲེལ་པ་ནི་ཐོབ་པ་དང་རྗེས་སུ་འབྲེལ་པས་སོ། །

[Block 1892]
རྒྱས་པར་འགྱུར་བ་ནི་རྣམ་པ་གཉིས་ཏེ། དམིགས་པ་དང་། མཚུངས་པར་ལྡན་པའི་སྒོ་ནས་སོ། །

[Block 1893]
རྗེས་སུ་འབྲང་བས༌[^1404]ནི་སྦྱོར་བ་མེད་པར་ཏེ། བཟློག་བཞིན་དུ་ཡང༌[^1405]དང་ཡང་དུ་མངོན་པར༌[^1406]འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1894]
རྒྱུ་དེ་དག་གིས་ན་ཕྲ་རྒྱས་རྣམས་ཞེས་བྱའོ། །

[Block 1895 [HEADING]]
##### ཟག་པ་ལ་སོགས་པའི་ངེས་ཚིག། ^2-27-4-2-0
--- END BLOCKS ---
