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

[Block 1896 [VERSE]]
དེ་དག་འཇོག་བྱེད་ཟག་བྱེད་དང་། །
ཁྱེར་བར༌[^1407]བྱེད་དང་འབྱར་བྱེད་དང་། །
ཉེ་བར་འཛིན་ཕྱིར་ཟག་ལ་སོགས། །
དེ་དག་གི་ནི་ངེས་ཚིག་ཡིན། །

[Block 1897]
འཁོར་བར་འཇོག་པར་བྱེད་པ་དང་། །སྲིད་པའི་རྩེ་མོ་ནས་མནར་མེད་པའི་བར་དུ་སྐྱེ་མཆེད་དྲུག་གི་རྨ་ནས་འཛག་པས་ན་ཟག་པ་དག་ཡིན་ནོ། །

[Block 1898]
ཁྱེར་བར༌[^1408]བྱེད་པས༌[^1409]ན་ཆུ་བོ་དག་ཡིན་ནོ། །

[Block 1899]
འབྱར་བར་བྱེད་པས་ན་སྦྱོར་བ་དག་ཡིན་ནོ། །

[Block 1900]
ཉེ་བར་འཛིན་པས་ན༌[^1410]ཉེ་བར་ལེན་པ་དག་ཡིན་ནོ། །

[Block 1901]
འདི་སྐད་དུ་འདི་དག་གིས། རྒྱུད༌[^1411]ཡུལ་རྣམས་ལ་འཛག་པར་བྱེད་པས་ན་ཟག་པ་རྣམས་ཡིན་ཏེ། ཚེ་དང་ལྡན་པས་དཔེར་ན་གྲུ་མངོན་པར་འདུ་བྱ་བ་ཆེན་པོས་ཆུའི་བཟློག་ཕྱོགས་སུ་བཀྲི་བ་དེ་མངོན་པར་འདུ་བྱ་བ་དེ་དག་ཉིད་མེད་པར་ཚེགས་ཆུང་ངུས་ཆུའི་འབབ་ཕྱོགས་སུ་འཁྱེར་བར་འགྱུར་བ་བཞིན་ནོ་ཞེས་གསུངས་པའི་མདོའི་ཚིག་དང་མཐུན་པའི་ཕྱིར་རོ། །

[Block 1902]
ཤུགས་ཆེན་པོ་དང་ལྡན་པའི་ཕྱིར་ཆུ་བོ་དག་སྟེ། དེའི་རྗེས་སུ་འབྱེད་པའི༌[^1412]ཕྱིར་དེ་དག་གིས་དེ་དག༌[^1413]དང་ལྡན་པ་འཁྱེར་བར་འགྱུར་རོ། །

[Block 1903]
ཆེ་བ་དང༌[^1414]ཀུན་དུ་མི་འབྱུང་བ་རྣམས་ནི་སྦྱོར་བ་དག་སྟེ། སྡུག་བསྔལ་སྣ་ཚོགས་དང་སྦྱོར་བའི༌[^1415]ཕྱིར་རམ། ཡང་ན་ཡང་དང་ཡང་དུ་རྗེས་སུ་འབྲེལ་བའི་སྒོ་ནས་སོ། །

[Block 1904]
འདོད་པ་ལ་སོགས་པ་ཉེ་བར་ལེན་པའི་ཕྱིར་ཉེ་བར་ལེན་པ་རྣམས་ནི༌[^1416]ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཆེས་ལེགས་པ་ཡིན་ནོ། །

[Block 1905 [HEADING]]
### ཀུན་དུ་སྦྱོར་བ་ལ་སོགས་པའི་དབྱེ་བ་རྣམ་ལྔ། ^2-28-0

[Block 1906 [VERSE]]
དེ་དག་ཀུན་དུ་སྦྱོར་སོགས་ཀྱི། །
དབྱེ་བས་ཡང་རྣམ་ལྔར་བཤད་དོ། །

[Block 1907 [HEADING]]
#### ཀུན་དུ་སྦྱོར་བ། ^2-28-1-0

[Block 1908]
ཕྲ་རྒྱས་དེ་དག་ཉིད་ཀུན་དུ་སྦྱོར་བ་དང་། འཆིང་བ་དང་། ཕྲ་རྒྱས་དང་། ཉེ་བའི་ཉོན་མོངས་པ་དང་། ཀུན་ནས་དཀྲིས་པའི༌[^1417]དབྱེ་བས་ཡང་རྣམ་པ་ལྔར་ཕྱེ་ནས་བཤད་དེ། དེ་ལ་ཀུན་དུ་སྦྱོར་བ་ནི་དགུ་སྟེ། རྗེས་སུ་ཆགས་པ་དང་། ཁོང་ཁྲོ་བ་དང་། ང་རྒྱལ་དང་། མ་རིག་པ་དང་། ལྟ་བ་དང་། མཆོག་ཏུ་འཛིན་པ་དང་། ཐེ་ཚོམ་དང་། ཕྲག་དོག་དང་། སེར་སྣའི་ཀུན་དུ་སྦྱོར་བ་རྣམས་སོ། །

[Block 1909 [HEADING]]
##### ཀུན་དུ་སྦྱོར་བ་དགུ། ^2-28-1-1-0

[Block 1910]
དེ་ལ་རྗེས་སུ་ཆགས་པའི་ཀུན་དུ་སྦྱོར་བ་ནི་ཁམས་གསུམ་པའི་འདོད་ཆགས་ཏེ། དེ་བཞིན་དུ་གཞན་དང་གཞན་དག་ཀྱང་ཅི་རིགས་པར་སྦྱོར་བར༌[^1418]བྱའོ། །

[Block 1911]
ལྟ་བའི་ཀུན་དུ་སྦྱོར་བ་ནི་ལྟ་བ་གསུམ་མོ། །

[Block 1912]
མཆོག་ཏུ་འཛིན་པའི་ཀུན་དུ་སྦྱོར་བ་ནི་ལྟ་བ་གཉིས་སོ། །

[Block 1913]
དེ་ཉིད་ཀྱི་ཕྱིར་ལྟ་བ་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་རྣམས་ལ་རྗེས་སུ་ཆགས་པའི་ཀུན་དུ་སྦྱོར་བས་ལྡན་ཞིང་ལྟ་བའི་ཀུན་དུ་སྦྱོར་བ༌[^1419]མ་ཡིན་པ། [^1420]དེ་ལ་ལྟ་བའི་ཕྲ་རྒྱས་རྒྱས་པར་མི་འགྱུར་བ་ཡང་མ་ཡིན་པ་ལྟ་ཡོད་དམ་ཞེ་ན། སྨྲས་པ་ཡོད་དེ། ཀུན་འབྱུང་ཤེས་པ་སྐྱེས་པ༌[^1421]ལ་འགོག་པ་ཤེས་པ་མ་སྐྱེས་པའི་ཚེ་འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་དང་། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་རྣམས་ཏེ།[^1422] དེ་དག་ནི་རྗེས་སུ་ཆགས་པའི་ཀུན་དུ་སྦྱོར་བ་དེ་ལ་དམིགས་པར༌[^1423]ལྡན་ལ་ལྟ་བའི་ཀུན་དུ་སྦྱོར་བས་ནི་མི་ལྡན་ཏེ། ཀུན་དུ་འགྲོ་བ་ནི་སྤངས་པའི་ཕྱིར་ལ་ཀུན་དུ་འགྲོ་བ་མ་ཡིན་པ་དེ་ལ་དམིགས་པ་དང་མཚུངས་པར་ལྡན་པ་ཅན་ལྟ་བའི་ཀུན་དུ་སྦྱོར་བ་ནི་མེད་པའི་ཕྱིར་རོ། །

[Block 1914]
དེ་དག་ལ་ལྟ་བའི་ཕྲ་རྒྱས་དག་ནི་རྒྱས་པར་འགྱུར་ཏེ། མཆོག་ཏུ་འཛིན་པའི་ལྟ་བ་དེ་དག་ཁོ་ན་མཚུངས་པར་ལྡན་པའི་སྒོ་ནས་རྒྱས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནས།[^1424] ཡང་ཅིའི་ཕྱིར་ཀུན་དུ་སྦྱོར་བ་དག་གི་ནང་དུ་ལྟ་བ་གསུམ་ནི་ལོགས་ཤིག་ཏུ་ལྟ་བའི་ཀུན་དུ་སྦྱོར་བར་བཤད་ལ། གཉིས་ནི་ལོགས་ཤིག་ཏུ་མཆོག་ཏུ་འཛིན་པའི་ཀུན་དུ་སྦྱོར་བའི་ནང་དུ་བཤད་ཅེ་ན།

[Block 1915 [VERSE]]
རྫས་དང་མཆོག་འཛིན་འདྲ་བའི་ཕྱིར། །
ལྟ་གཉིས་ཀུན་དུ་སྦྱོར༌[^1425]གཞན་ནོ། །

[Block 1916]
ལྟ་བ་མཆོག༌[^1426]གསུམ་ཡང་རྫས་བཅོ་བརྒྱད་ཡིན་ལ། མཆོག་ཏུ་འཛིན་པའི་ལྟ་བ་གཉིས་ཀྱང་རྫས་བཅོ་བརྒྱད་ཁོ་ན་ཡིན་ཏེ། དེའི་ཕྱིར་རྫས་མཉམ་པས་འདི་གཉིས་ཀུན་ཏུ་སྦྱོར་བས་གཞན་དུ་བྱས་སོ་ཞེས་གྲག་གོ། །

[Block 1917]
འདི་གཉིས་ནི་མཆོག་ཏུ་འཛིན་པའི་རང་བཞིན་ཡིན་ལ། ལྷག་མ་རྣམས་ནི་མ་ཡིན་པས་མཆོག་ཏུ་འཛིན་པར་འདྲ་བའི་ཕྱིར་ཡང་འདི་གཉིས་ལོགས་ཤིག་ཏུ་བཤད་དེ། གཟུང་བ་དང་འཛིན་པ་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 1918]
ཡང་ཅིའི་ཕྱིར་ཀུན་ཏུ་སྦྱོར་བ་དག་ཏུ་ཕྲག་དོག་དང་། སེར་སྣ་ནི་ལོགས་ཤིག་ཏུ་ཀུན་དུ་སྦྱོར་བ་གཉིས་སུ་བཤད་ལ། ཀུན་ནས་དཀྲིས་པ་གཞན་ནི་མ་ཡིན་ཞེ་ན།

[Block 1919 [VERSE]]
གང་ཕྱིར་གཉི་ག་གཅིག་ཏུ་ནི། །
མི་དགེ་རང་དབང་དེ་ཡི་ཕྱིར། །
ཕྲག་དོག་སེར་སྣ་དེ་དག་ལས། །
ལོགས་ཤིག་ཀུན་སྦྱོར་གཉིས་སུ་བཤད། །

[Block 1920]
གང་ལ་གཅིག་ཏུ་མི་དགེ་བ་དང་རང་དབང་ཅན་འདི་གཉིས་ཀ་ཡོད་པ་དེ་ལྟ་བུའི་ཀུན་ནས་དཀྲིས་པ་གཞན་ནི་མེད་དོ། །

[Block 1921]
གཞན་དག་ན་རེ་གང་གི་ཀུན་ནས་དཀྲིས་པ་བརྒྱད་ཡིན་པ་དེའི་ཕྱིར༌[^1427]ནི་དེ་ལྟར་འགྱུར་གྱི། གང་གི་བཅུ་ཡིན་པ་དེ་ནི་ཁྲོ་བ་དང་འཆབ་པ་ཡང་རྣམ་པ་གཉི་ག་ཡིན་པས་དེའི་ཕྱིར་འདི་ལ༌[^1428]ལན་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1922 [HEADING]]
##### ཐ་མའི་ཆ་དང་མཐུན་པ་ལྔ། ^2-28-1-2-0

[Block 1923]
ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་གཞན་དུ་ཀུན་དུ་སྦྱོར་བ། ཐ་མའི་ཆ་དང་མཐུན་རྣམ་ལྔ། །གསུངས་ཏེ། འདི་ལྟ་སྟེ། འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་དང་། ཐེ་ཚོམ་དང་། འདོད་པ་ལ་འདུན་པ་དང་། གནོད་སེམས་སོ། །

[Block 1924]
ཅིའི་ཕྱིར་འདི་དག་ཐ་མའི་ཆ་དང་མཐུན་པ་རྣམས་ཞེས་བྱ་ཞེ་ན། ཐ་མའི་ཆ་དང་ལྡན་པའི་ཕྱིར་ཏེ། ཐ་མའི་ཆ་ནི་འདོད་པའི་ཁམས་ཡིན་ལ། འདི་དག་ཀྱང་དེའི་རྗེས་སུ་མཐུན་པ་ཡིན་ཏེ། འདི་ལྟར་གཉིས་ཀྱིས་འདོད་པ༌[^1429]ལས་མི་འདའ་ལ། གསུམ་པོ་ཡིས་ནི་ཕྱིར་ཟློག་བྱེད། །འདོད་པ་ལ་འདུན་པ་དང་། གནོད་སེམས་དག་གིས་ནི་འདོད་པའི་ཁམས་ལས་མི་འདའོ། །

[Block 1925]
འཇིག་ཚོགས་ལ་ལྟ་བ་ལ་སོགས་པ་དག་གིས་ནི་འདས་ཀྱང་ཕྱིར་ཟློག་པར་བྱེད་དེ། སྒོ་བ་དང་། རྗེས་སུ་འབྲང་བ་དང་ཆོས་མཐུན་པའི་ཕྱིར་རོ། །

[Block 1926]
གཞན་དག་ན་རེ་གསུམ་གྱིས་ནི་སེམས་ཅན་གྱི་ཐ་མ་སོ་སོའི་སྐྱེ་བོ་ཉིད་ལས་མི་འདའ་ལ། གཉིས་ཀྱིས་ནི་ཁམས་ཀྱི་ཐ་མ་འདོད་པའི་ཁམས་ལས་མི་འདའ་སྟེ། དེའི་ཕྱིར་འདི་དག་ཐ་མའི་ཆ་དང་མཐུན་པ་རྣམས་ཞེས་བྱའོ་ཞེས་ཟེར་རོ། །

[Block 1927]
གང་གི་ཚེ་རྒྱུན་དུ་ཞུགས་པས་ཀུན་དུ་སྦྱོར་བ་གསུམ་ཡོངས་སུ་གཏུགས་ཏེ་སྤང་བའི་ཕྱིར༌[^1430]ཉོན་མོངས་པ་དྲུག་སྤངས་པ་ཡིན་ན། ཅིའི་ཕྱིར་ལྟ་བ་གསུམ་བོར་ལ། འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་དང་། ཐེ་ཚོམ་གསུམ་ཁོ་ན་གསུངས་ཤེ་ན། དེ་དག༌[^1431]ཐམས་ཅད་བརྗོད་པར་བྱ་བ་ནི་ཡིན་མོད་ཀྱི་འོན་ཀྱང་། སྒོ་དང་རྩ་བ་བསྡུས་ཕྱིར་གསུམ། །དུ་བཤད་དེ། ཉོན་མོངས་པ་རྣམས་ནི་རྣམ་པ་གསུམ་སྟེ། རྣམ་པ་གཅིག་དང་། རྣམ་པ་གཉིས་དང་། རྣམ་པ་བཞི་དག་ཡིན་ལ། དེ་དག་གི་སྒོ་ནི་འདི་གསུམ་གྱིས་བསྡུས་སོ། །

[Block 1928]
གཞན་ཡང་མཐར་འཛིན་པར་ལྟ་བ་ནི་འཇིག་ཚོགས་ལ་ལྟ་ལྟ༌[^1432]བས་རབ་ཏུ་བཅུག་ལ། ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་ནི་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པས་རབ་ཏུ་བཅུག །ལོག་པར་ལྟ་བ་ནི་ཐེ་ཚོམ་གྱིས་རབ་ཏུ་བཅུག་སྟེ། དེའི་ཕྱིར་རྩ་བ་བསྡུས་སོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 1929]
གཞན་དག་ན་རེ།

[Block 1930 [VERSE]]
འགྲོ་མི་འདོད་དང་ལམ་ནོར་དང་། །
ལམ་ལ་ཐེ་ཚོམ་དེ་སྙེད་ཅིག །
ཐར་པ༌[^1433]བགྲོད་པ་བགེགས༌[^1434]བྱེད་པ། །
དེ་ཡི་ཕྱིར་ན་གསུམ་བསྟན་ཏོ། །
--- END BLOCKS ---
