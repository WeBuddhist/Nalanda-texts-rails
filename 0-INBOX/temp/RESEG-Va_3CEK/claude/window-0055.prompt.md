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

[Block 1931]
ཡུལ་གཞན་དུ་བགྲོད་པར་བྱ་བ་ལ་བར་ཆད་བྱེད་པ་ནི་གསུམ་ཡོད་དོ། །

[Block 1932]
[^1435]འགྲོ་མི་འདོད་པ་དང་། ལམ་གཞན་ལ་བརྟེན་པའི༌[^1436]ཕྱིར་ལམ་ནོར་བ་དང་། ལམ་ལ་ཐེ་ཚོམ་ཟ་བའོ། །

[Block 1933]
དེ་བཞིན་དུ་ཐར་པ་བགྲོད་པར་བྱ་བ་ལ་ཡང་གསུམ་པོ་དེ་དག་ཉིད་བར་ཆད་བྱེད་དེ། དེ་ལ་འཇིག་ཚོགས་ལ་ལྟ་བས་ནི་ཐར་པས་སྐྲག་པར་འགྱུར་བས༌[^1437]འགྲོ་མི་འདོད་པར་འགྱུར་རོ། །

[Block 1934]
ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པས་ནི་ལམ་གཞན་ལ་ཡང་དག་པར་བརྟེན་པའི་ཕྱིར་ལམ་ནོར་བར་འགྱུར་རོ། །

[Block 1935]
ཐེ་ཚོམ་གྱིས་ནི་ལམ་ལ་ཐེ་ཚོམ་ཟ་བར་འགྱུར་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་རྒྱུན་དུ་ཞུགས་པས་ཐར་པར༌[^1438]བགྲོད་པའི་བར་ཆད་བྱེད་པ་དེ་དག་སྤང་བར༌[^1439]སྟོན་པ་ན་ཉོན་མོངས་པ་གསུམ་ཁོ་ན་སྤང་བར༌[^1440]བསྟན་ཏོ་ཞེས་ཟེར་རོ། །

[Block 1936 [HEADING]]
##### གོང་མའི་ཆ་དང་མཐུན་པ་ལྔ། ^2-28-1-3-0

[Block 1937]
བཅོམ་ལྡན་འདས་ཀྱིས༌[^1441]ཇི་ལྟར་ཀུན་དུ་སྦྱོར་བ་ཐ་མའི་ཆ་དང་མཐུན་པ་ལྔ་བཤད་པ་དེ་བཞིན་དུ་ཡང་། གོང་མའི་ཆ་དང་མཐུན་ལྔ་ཉིད། །ཇི་ལྟ་ཞེ་ན།

[Block 1938 [VERSE]]
གཟུགས་དང་གཟུགས་མེད་ལས་སྐྱེས་པའི། །
འདོད་ཆགས་གཉིས་རྒོད་ང་རྒྱལ་རྨོངས། །

[Block 1939]
ཞེས༌[^1442]ཏེ། འདི་དག་གི༌[^1443]ཀུན་དུ་སྦྱོར་བ་གོང་མའི་ཆ་དང་མཐུན་པ་ལྔ་ཡིན་ཏེ། འདི་ལྟ་སྟེ་གཟུགས་ཀྱི་འདོད་ཆགས་དང་། གཟུགས་མེད་པའི་འདོད་ཆགས་དང་། རྒོད་པ་དང་། ང་རྒྱལ་དང་། མ་རིག་པ་སྟེ། དེ་དག་མ་སྤངས་པར་ཁམས༌[^1444]གོང་མ་ལས་མི་འདའ་བའི་ཕྱིར་རོ། །

[Block 1940]
ཀུན་དུ་སྦྱོར་བའི་སྐབས་རྫོགས་སོ།། །།

[Block 1941 [HEADING]]
#### འཆིང་བ། ^2-28-2-0

[Block 1942]
འཆིང་བ་རྣམས་གང་ཞེ་ན། འཆིང་བ་ནི་གསུམ་སྟེ། འཆིང་བ་འདོད་ཆགས་ཐམས་ཅད་དང་། འཆིང་བ་ཞེ་སྡང་དང་། གཏི་མུག་ཐམས་ཅད་དོ། །ཅིའི་ཕྱིར་གསུམ་པོ་ནི༌[^1445]འཆིང་བར་བཤད་ཅེ་ན། ཚོར་བའི་དབང་གིས་འཆིང་བ་གསུམ། །ཚོར་བ་གསུམ་གྱི༌[^1446]དབང་གིས་འཆིང་བ་གསུམ་སྟེ། བདེ་བའི་ཚོར་བ་ལ་ནི་འདོད་ཆགས་དམིགས་པ་དང་མཚུངས་པར་ལྡན་པའི་སྒོ་ནས་རྒྱས་པར་འགྱུར་ལ། སྡུག་བསྔལ༌[^1447]ལ་ནི་ཞེ་སྡང་ངོ་། །བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་ཡང་མ་ཡིན་པ་ལ༌[^1448]ནི་གཏི་མུག་སྟེ། འདོད་ཆགས་དང་། ཞེ་སྡང་དག་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 1943]
ཡང་ན་རང་གི་རྒྱུད་ལ་ཡོད་པའི་དམིགས་པའི་སྒོ་ནས་ངེས་པ་ཡིན་ནོ། །

[Block 1944 [HEADING]]
#### ཕྲ་རྒྱས། ^2-28-3-0

[Block 1945]
ཕྲ་རྒྱས་རྣམས་ནི་སྔར་བཤད་པ་ཁོ་ནར་ཟད་དོ། །

[Block 1946 [HEADING]]
#### ཉེ་བའི་ཉོན་མོངས་པ། ^2-28-4-0

[Block 1947]
ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་བརྗོད་པར་བྱ་སྟེ། དེ་ལ༌[^1449]རེ་ཞིག་གང་དག་ཉོན་མོངས་པ་ཡིན་པ་དེ་དག་ནི་ཉེ་བའི་ཉོན་མོངས་པ་ཡང་ཡིན་ཏེ། སེམས་ཉེ་བར་ཉོན་མོངས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1948]
ཉོན་མོངས་ལས་གཞན་ཉོན་མོངས་ཅན། །སེམས་བྱུང་འདུ་བྱེད་ཕུང་ཞེས་བྱ།[^1450] །

[Block 1949 [VERSE]]
གང་དེའང་ཉེ་བའི་ཉོན་མོངས་ཏེ། །
དེ་དག་ཉོན་མོངས་ཞེས་མི་བྱ། །

[Block 1950]
ཉོན་མོངས་པ་རྣམས་ལས་གཞན་པ༌[^1451]ཆོས་ཉོན་མོངས་པ་ཅན་སེམས་ལས་བྱུང་བ་འདུ་བྱེད་ཀྱི་ཕུང་པོས་བསྡུས་པ་གང་དག་ཡིན་པ་དེ་དག་ནི་ཉེ་བའི་ཉོན་མོངས་པ་ཁོ་ན་ཡིན་གྱི། ཉོན་མོངས་པ་དག་ནི་མ་ཡིན་ཏེ། དེ་དག་ཀྱང་གཞི་ཕྲན་ཚེགས་ལས་བྱུང་བ་གང་དག་ཡིན་པའོ། །

[Block 1951 [HEADING]]
##### ཀུན་ནས་དཀྲིས་པ། ^2-28-4-1-0

[Block 1952]
འདིར་ནི་ཀུན་ནས་དཀྲིས་པ་དང་། ཉོན་མོངས་པའི་དྲི་མས་བསྡུས་པ་ཁོ་ན་བསྟན་པར་བྱ་སྟེ། ཀུན་ནས་དཀྲིས་པ་རྣམས་གང་ཞེ་ན། སྨྲས་པ་ཉོན་མོངས་པ་ཡང་ཀུན་ནས་དཀྲིས་པ་ཡིན་ཏེ།

[Block 1953]
མདོ་ལས།

[Block 1954]
འདོད་པའི་འདོད་ཆགས་ཀྱི་ཀུན་ནས་དཀྲིས་པ་སྡུག་བསྔལ་གྱི་རྐྱེན་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1955]
བསྟན་བཅོས་རབ་ཏུ་བྱེད་པ་ལས་ནི།

[Block 1956 [VERSE]]
ངོ་ཚ་མེད་དང་ཁྲེལ་མེད་དང་། །
ཕྲག་དོག་སེར་སྣ་རྒོད་པ་དང་། །
འགྱོད་དང་རྨུགས་དང་གཉིད་དང་ནི། །
ཀུན་ནས་དཀྲིས་པ་རྣམ་པ་བརྒྱད། །

[Block 1957]
འབྱུང་ངོ་། །བྱེ་བྲག་ཏུ་སྨྲ་བའི་ལུགས་ཀྱིས་ནི་ཀུན་ནས༌[^1452]དཀྲིས་པ་བཅུ་སྟེ། བརྒྱད་པོ་དེ་དག་དང་། ཁྲོ་དང་འཆབ་པའོ། །

[Block 1958]
དེ་ལ་ངོ་ཚ་མེད་པ་དང་ཁྲེལ་མེད་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 1959]
ཕྲག་དོག་ནི་གཞན་གྱི་དོན༌[^1453]ཕུན་སུམ་ཚོགས་པ་ལ་སེམས་ཁོང་ནས་འཁྲུག་པའོ། །

[Block 1960]
སེར་སྣ་ནི་ཆོས་དང་ཟང་ཟིང་དང་མཁས་པ་རབ་ཏུ་སྦྱིན་པ་དང་འགལ་བ་ཅན་སེམས་ཀྱིས༌[^1454]ཀུན་ནས༌[^1455]འཛིན་པའོ། །

[Block 1961]
རྒོད་པ་ནི་སེམས་རྣམ་པར་མ་ཞི་བའོ། །

[Block 1962]
འགྱོད་པ་དང་རྨུགས་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 1963]
གཉིད་ནི་ལུས་ཡང་དག་པར་འཛིན་པར༌[^1456]མི་ནུས་པ་སེམས་མངོན་པར་སྡུད་པའོ། །

[Block 1964]
དེ་དང་འགྱོད་པ་ནི་ཉོན་མོངས་པ་ཅན་ཁོ་ན་ཀུན་ནས་དཀྲིས་པ་ཡིན་ནོ། །

[Block 1965]
ཁྲོ་བ་ནི་གནོད་སེམས་དང་། རྣམ་པར་འཚེ་བ་མ་གཏོགས་པ་སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པ་ལ་ཀུན་ནས་མནར་སེམས་པ་གང་ཡིན་པའོ། །
--- END BLOCKS ---
