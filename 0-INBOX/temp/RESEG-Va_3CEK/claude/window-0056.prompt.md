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

[Block 1966]
འཆབ་པ་ནི་ཁ་ན་མ་ཐོ་བ་མཁྱུད༌[^1457]པའོ། །

[Block 1967]
ཀུན་ནས་དཀྲིས་པ་དེ་རྣམས་ལས། །

[Block 1968]
འདོད་ཆགས་དང་།[^1458] ངོ་ཚ་མེད་རྒོད་སེར་སྣ་བསླང་། །ཉེ་བའི་ཉོན་མོངས་པ་གསུམ་པོ་འདི་དག་ནི་འདོད་ཆགས་ཀྱི་རྒྱུ་མཐུན་པ་ཡིན་ནོ། །

[Block 1969]
འཆབ་པ་རྩོད་དོ། །

[Block 1970]
ཁ་ཅིག་ན་རེ། སྲེད་པའི་རྒྱུ་མཐུན་པའོ་ཞེས་ཟེར་རོ། །

[Block 1971]
གཞན་དག་ན་རེ་མ་རིག་པའི་རྒྱུ་མཐུན་པའོ་ཞེས་ཟེར་རོ། །

[Block 1972]
གཞན་དག་ན་རེ་དེ༌[^1459]གཉི་གའི་ཡིན་ཏེ། གོ་རིམས་བཞིན་དུ་ཤེས་པ་དང་མི་ཤེས་པ་རྣམས་ཀྱི་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1973]
མ་རིག་པ༌[^1460]ལས།

[Block 1974]
རྨུགས་དང་གཉིད་དང་ཁྲེལ་མེད་དོ། །

[Block 1975]
གསུམ་པོ་འདི་དག་ནི་མ་རིག་པའི་རྒྱུ་མཐུན་པ་ཡིན་ནོ། །

[Block 1976 [VERSE]]
ཐེ་ཚོམ་ལས་འགྱོད་ཁྲོ་བ་དང་། །
ཕྲག་དོག་ཁོང་ཁྲོའི་རྒྱུ་ལས་བྱུང་། །

[Block 1977]
ཁོང་ཁྲོ་བས་ཀུན་ནས་བསླང་བ་དག་ཡིན་ཏེ། དེ་ལྟར་ན་ཉེ་བའི་ཉོན་མོངས་པ་བཅུ་པོ་དེ་དག་ནི་ཉོན་མོངས་པའི་རྒྱུ་མཐུན་པ་དག་ཡིན་ནོ། །

[Block 1978 [HEADING]]
##### ཉོན་མོངས་པའི་དྲི་མ། ^2-28-4-2-0

[Block 1979]
གཞན་ཡང་ཉོན་མོངས་དྲི་མ་དྲུག །འདི་ལྟ་སྟེ།

[Block 1980 [VERSE]]
སྒྱུ་དང་གཡོ་དང་རྒྱགས་པ་དང་། །
དེ་བཞིན་འཚིག་དང་ཁོན་འཛིན་དང་། །

[Block 1981]
རྣམ་འཚེ། དེ་ལ་སྒྱུ༌[^1461]ནི་གཞན་འདྲིད་པའོ། །

[Block 1982]
གཡོ་ནི་སེམས་གྱ་གྱུ་བ་སྟེ། གང་གིས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་མི་འཆགས་ཀྱི་གཏམ་རླུང་བསྐུར་བ༌[^1462]འམ་མི་གསལ་བར་བྱེད་པའོ། །

[Block 1983]
རྒྱགས་པ་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 1984]
འཚིག་པ་ནི་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པའི་དངོས་པོ་དམ་དུ་འཛིན་པ་སྟེ། གང་གིས་རིག་པར༌[^1463]གཏམས་པ་མི་འཛིན་པའོ། །

[Block 1985]
ཁོན་དུ་འཛིན་པ་ནི་ཀུན་ནས་མནར་སེམས་ཀྱི་དངོས་པོ་ལན་མང་དུ་བྱེད་པའོ། །

[Block 1986]
རྣམ་པར་འཚེ་བ་ནི་རྣམ་པར་ཐོ་འཚམས་པ༌[^1464]སྟེ།

[Block 1987]
གང་གིས་མཚོན་ཆ་དང་ཚིག་རྩུབ་པོ་དག་གིས་ཕ་རོལ་པོ་རྣམ་པར་ཐོ་འཚམས་པར༌[^1465]བྱེད་པའི༌[^1466]ཉོན་མོངས་པའི་དྲི་མ་དྲུག་པོ་དེ་དག་ལས།

[Block 1988]
སྒྱུ་དང་རྒྱགས་པ་ནི།

[Block 1989 [VERSE]]
འདོད་ཆགས་ལས་སྐྱེས་ཁོན་འཛིན་དང་། །
རྣམ་འཚེ་ཁོང་ཁྲོ་ལས་སྐྱེས་སོ། །
འཚིག་པ་ལྟ་བ་མཆོག་འཛིན་ལས། །
གཡོ་ནི་ལྟ་བས་ཀུན་ནས་བསླང་། །

[Block 1990]
གྱ་གྱུ་ཅི་ཡིན་སྡིག་ཅན་ལྟ། །ཞེས་ཚིགས་སུ་བཅད་དེ་འབྱུང་བའི་ཕྱིར་གཡོ་ནི་ལྟ་བའི་རྒྱུ་མཐུན་པ་ཡིན་པར་རུང་ངོ་། །འདི་དག་ཅི་ཞིག་གིས་སྤང་བར་བྱ་བ་ཡིན་ཞེ་ན། རེ་ཞིག་ཀུན་ནས་དཀྲིས་པ་བཅུར་བཤད་པ་གང་དག་ཡིན་པ།

[Block 1991 [VERSE]]
དེ་ལས་ངོ་ཚ་མེད་པ་དང་། །
ཁྲེལ་མེད་རྨུགས་གཉིད་རྒོད་རྣམ་གཉིས། །

[Block 1992]
ཆོས་ལྔ་པོ་འདི་དག་ནི་ཉོན་མོངས་པ་རྣམ་པ་གཉིས་ཀ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་མཐོང་བ་དང་བསྒོམ་པས་སྤང་བར་བྱ་བ་རྣམ་པ་གཉིས་ཡིན་ཏེ། གང་ཞིག་གང་མཐོང་བས་སྤང་བར་བྱ་བ་དང་མཚུངས་པར་ལྡན་པ་དེ་ནི་དེ་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1993]
དེ་ལས་གཞན་ནི་བསྒོམ་སྤང་བྱ། །དེ་དག་ལས་གཞན་པའི་ཉེ་བའི་ཉོན་མོངས་པ་ཀུན་ནས་དཀྲིས་པས་བསྡུས་པ་ཕྲག་དོག་དང་། སེར་སྣ་དང་། འགྱོད་པ་དང་། ཁྲོ་བ་དང་། འཆབ་པ་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་ཁོ་ན་དང་། ཉེ་བའི་ཉོན་མོངས་པ་ལྔ་པོ་དེ་དག་ནི། རང་དབང་ཅན་ཡིན་ཏེ། མ་རིག་པ་ཙམ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1994]
ཇི་ལྟར་ཕྲག་དོག་ལ་སོགས་པ་ཉེ་བའི་ཉོན་མོངས་པ་ལྔ་པོ་དེ་དག་བསྒོམ་པས་སྤང་བར་བྱ་བ་དང་། རང་དབང་ཅན་ཡིན་པ། དེ་བཞིན་དྲི་མ་རྣམས། ཉོན་མོངས་པའི་དྲི་མ་དྲུག་ཀྱང་དེ་དང་འདྲའོ། །

[Block 1995]
ཉེ་བའི་ཉོན་མོངས་པ་ཇི་སྐད་དུ་བཤད་པ་དེ་དག་ནི། འདོད་ན་མི་དགེ། འདོད་པའི་ཁམས་ན་ནི་མི་དགེ་བ་དག་ཡིན་ནོ། །

[Block 1996]
དེ་དག༌[^1467]ལས་ཀྱང་། གསུམ་རྣམ་གཉིས། རྨུགས་པ་དང་། རྒོད་པ་དང་། གཉིད་རྣམས་ནི་མི་དགེ་བ་དང་།

[Block 1997 [VERSE]]
ལུང་དུ་མ་བསྟན་པ་དག་ཡིན་ནོ། །
དེ་ཡན་ཆད་ནི་ལུང་མ་བསྟན། །

[Block 1998]
འདོད་པའི་ཁམས་ཡན་ཆད་ཀྱི་ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་ནི་ཅི་རིགས་པར་ལུང་དུ་མ་བསྟན་པ་དག་ཡིན་ནོ། །

[Block 1999 [HEADING]]
##### ཉེ་བའི་ཉོན་མོངས་པ་དུ་ཞིག་གང་ན་ཡོད་པ། ^2-28-4-3-0

[Block 2000]
དེ་དག་ལས་དུ་ཞིག་གང་ན་ཡོད་པར་རིག་པར་བྱ་ཞེ་ན། འདོད་དང་བསམ་གཏན་དང་པོ་ན། །གཡོ་སྒྱུ། འདི་གཉིས་ནི་འདོད་པའི་ཁམས་དང་། བསམ་གཏན་དང་པོ་ན་ཡོད་དོ། །
--- END BLOCKS ---
