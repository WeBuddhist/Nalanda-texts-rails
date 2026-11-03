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
[Block 2066]
[^1825]

[Block 2067 [HEADING]]
### ཡེ་ཤེས་ཀྱི་ཚོགས་མི་ཟད་པ། ^7-2-0

[Block 2068]
ཐེ་ཚོམ་ཐམས་ཅད་གཅོད་པའི་དབང་དུ་བྱས་ནས། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཡེ་ཤེས་ཀྱི་ཚོགས་མི་ཟད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2069]
ཡེ་ཤེས་རྟོགས་པར༌[^1826]འགྱུར་ཞེས་བྱ་བ་ནི་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ཁོང་དུ་ཆུད་ཅིང་མངོན་སུམ་དུ་འགྱུར་བའོ། །

[Block 2070]
དེ་ལ་ཡེ་ཤེས་ཡོངས་སུ་ཚོལ་བ་ལ་འདུན་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཕྱི་རོལ་མ་ཡིན་པའི་ཆོས་སྟོན་ཏོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་རྒྱུ་བསྟན་ཏོ། །

[Block 2071]
དེས་ཆོས་དེ་དག་ཐོས་ནས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ལས་ཡོངས་སུ་དག་པའི་ཡེ་ཤེས་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^1827]རྐྱེན་བསྟན་ཏོ། །

[Block 2072 [HEADING]]
#### རྒྱུ། ^7-2-1-0

[Block 2073]
ཡེ་ཤེས་ཡོངས་སུ་ཚོལ་བ་ལ་རབ་ཏུ་འདུན་པ་ཞེས་བྱ་བ་ནི་ཡེ་ཤེས་འགྲུབ་པར་འགྱུར་བའི་རྒྱུའི་ཚོལ་བ་ལ་འདུན་པ་སྟེ། གླེགས་བམ་འདྲི་བ་དང་། ཀློག་པ་ལ་སོགས་པ་ལ་འདུན་ཞིང་བརྩོན་པའོ། །

[Block 2074]
ཡེ་ཤེས་རྟོགས་པའི་དགེ་བའི་བཤེས་གཉེན་ཞེས་བྱ་བ་ལ་ཡེ་ཤེས་གཉིས་སུ་མེད་པ་མངོན་དུ་བྱས་པའི་དགེ་བའི་བཤེས་གཉེན་ནམ། ཡེ་ཤེས་རྟོགས་པར༌[^1828]འགྱུར་བའི་ཆོས་སྟོན་པའི་དགེ་བའི་བཤེས་གཉེན་ནི་ཡེ་ཤེས་རྟོགས་པའི་དགེ་བའི་བཤེས་གཉེན་ཏེ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་ཆོས་སྟོན་པའི་མཁན་པོ་དང་སློབ་དཔོན་ལ་སོགས་པའོ། །

[Block 2075]
རྟག་ཏུ་ཞེས་བྱ་བ་ནི་རྟག་ཏུ་བསྟེན་པ་དང་། རྟག་ཏུ་འགྲོགས་པ་དང་། རྟག་ཏུ་བསྙེན་བཀུར་བྱེད་པ་ཞེས་ཚིག་རེ་རེ་དང་སྦྱར་རོ། །

[Block 2076]
རྟག་ཏུ་བསྟེན་པ༌[^1829]ནི་དུས་ཐམས་ཅད་དུ་དེའི་གན་དུ་ཉེ་བར་འགྲོ་བའོ། །

[Block 2077]
རྟག་ཏུ་འགྲོགས་པ་ནི་དུས་ཐམས་ཅད་དུ་དེ་དང་ལྷན་ཅིག་ཏུ་གནས་པ་མི་གཏང༌[^1830]བའོ། །

[Block 2078]
རྟག་ཏུ་བསྙེན་བཀུར་བྱེད་པ་ནི་དུས་ཐམས་ཅད་དུ་དེ་དག་ལ་ཕྱག་འཚལ་བ་ལ་སོགས་པ་བསྟི༌[^1831]སྟང་བྱེད་པའོ། །

[Block 2079]
གང་ཡང་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ལ་རྟོན་ཅིང་ཞེས་བྱ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི༌[^1832]རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བའི་ཕྱིར་འབད་པར་བྱེད་ཀྱི་ཉན་ཐོས་ལ་སོགས་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བ་ལ་འབད་པ་མེད་པའོ། །

[Block 2080]
དགེ་བའི་བཤེས་གཉེན་དེ་དག་ལ་ང་རྒྱལ་མེད་ཅེས་བྱ་བ་ནི་ཆོས་སྟོན་པའི་གང་ཟག་རྣམས༌[^1833]ལ་ང་རྒྱལ་བ་མི་བྱེད་པའོ། །

[Block 2081]
བླ་མ་བཞིན་དུ་ཕངས་པར་འཛིན་པ་ཞེས་བྱ་བ་ནི་མཁན་པོ་དང་སློབ་དཔོན་ལ་བཙུན་ཞིང་ཕངས་པར་བྱེད་པ་བཞིན་དུ་དགེ་བའི་བཤེས་གཉེན་ལ་ཡང་བཙུན་ཞིང་ཕངས་པར་བྱེད་པའོ། །

[Block 2082]
སྟོན་པ་བཞིན་དུ་ཕངས་པར་འཛིན་པ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་བཙུན་ཞིང་ཕངས་པར་བྱེད་པ་བཞིན་དུ་དགེ་བའི་བཤེས་གཉེན་ལ་ཡང་བཙུན་ཞིང་ཕངས་པར་བྱེད་པའོ། །

[Block 2083]
དགེ་བའི་བཤེས་གཉེན་དེ་དག་གིས་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ལ་སོགས་པ་དགེ་བའི་བཤེས་གཉེན་དེ་དང་དེ་དག་གིས་སོ། །

[Block 2084]
འདི་བསམ་པ་ཕུན་སུམ་ཚོགས་པར་རིག་ཅེས་བྱ་བ་ནི་གང་ཟག་ཆོས་ཚོལ་བ་དེའི་བསམ་པ་གོང་དུ་བཤད་པ་ལྟར་ན་ཁེ་དང་བཀུར་སྟི་ཙམ་འདོད་པའི་ཕྱིར་ཆོས༌[^1834]ཚོལ་བ་ནི་མ་ཡིན་གྱི་ཡེ་ཤེས་གཉིས་སུ་མེད་པ་ཚོལ་བ་ཡིན་པར་ཁོང་དུ་ཆུད་ནས་ཆོས་སྟོན་པར་བྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2085]
ཆོས་ཀྱང་རྣམ་པ་གསུམ་སྟོན་ཏེ། བཤད་པར་བྱ་བའི་ཆོས་སྟོན་པ་དང་། བསྒྲུབ་པར༌[^1835]བྱ་བའི་ཆོས་སྟོན་པ་དང་། ཁོང་དུ་ཆུད་པར་བྱ་བའི་ཆོས་སྟོན་པའོ། །

[Block 2086]
འབྲེལ་པའི་གཏམ་ཞེས་བྱ་བས་བཤད་པར་བྱ་བའི་ཆོས་སྟོན་པ་བསྟན་ཏེ། གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་རྣམས་ཕྱིན་ཅི་མ་ལོག་པར་འཆད་པའི་ཕྱིར་རོ།[^1836] །དེ་ཡེ་ཤེས་ཀྱི་གཏམ་སྒྲུབ་པར་བྱེད་ཅེས་བྱ་བས་བསྒྲུབ་པར་བྱ་བའི་ཆོས་སྟོན་པ་བསྟན་ཏེ། ཡེ་ཤེས་གཉིས་སུ་མེད་པ་ཐོབ་པར་བྱེད་པའི་རྒྱུ་སྟོང་པ་ཉིད་ལ་སོགས་པ་འཆད་པའི་ཕྱིར་རོ། །

[Block 2087]
སྣོད་དུ་རིག་ནས་ཞེས་བྱ་བ་ལ་སོགས་པས་ཁོང་དུ་ཆུད་པར་བྱ་བའི་ཆོས་སྟོན་པ་བསྟན་ཏེ། ཁོང་དུ་ཆུད་པར་བྱ་བའི་ཆོས་བསྟན༌[^1837]པའི་སྣོད་ཡིན་པར་རིག་ནས་ཕྱི་རོལ་གྱི་གཙུག་ལག་བྱཱ་ཀ་ར་ཎ་ལ་སོགས་པ་མ་ཡིན་པ་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་རྒྱུན་དུ་སྟོན་པའོ། །

[Block 2088 [HEADING]]
#### རྐྱེན། ^7-2-2-0

[Block 2089]
དེས་ཆོས་དེ་དག་ཐོས་ནས་ཞེས་བྱ་བ་ནི་ཆོས་ཚོལ་བའི་གང་ཟག་དེས་གོང་དུ་བཤད་པའི་ཆོས་གསུམ་པོ་དེ་དག་དགེ་བའི་བཤེས༌[^1838]གཉེན་ལས་ཐོས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2090]
ཆོས་ཀྱི་ཚོགས་ལ་སྦྱོར་བར་བྱེད་དེ་ཞེས་བྱ་བ་ནི་ཆོས་དེ་གསུམ་ཁོང་དུ་ཆུད་ཅིང་རྟོགས་པར་འགྱུར་བའི་རྒྱུ་ལ་སྦྱོར་བར་བྱེད་ཅིང་རྒྱུ་རྩོམ་པར་བྱེད་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2091]
གང་ཆོས་ཀྱི་ཚོགས་ལ་སྦྱོར་བ་དེ་ནི་ཞེས་བྱ་བ་ལ་ཆོས་ཚོལ་བའི་གང་ཟག་གསུམ་རྟོགས་པར་འགྱུར་བའི་རྒྱུ་ལ་སྦྱོར་བ་དེ་ཉིད་གང་ཟག་དེའི་ཡེ་ཤེས་ཀྱི་ཚོགས་དང་རྒྱུ་ཡིན་ནོ། །

[Block 2092]
དེ་ལ་ཆོས་ཀྱི་ཚོགས་ལ་སྦྱོར་བ་གང་ཞེ་ན་ཞེས་བྱ་བ་ནི་ཆོས་གསུམ་རྟོགས་པའི་རྒྱུ་ལ་རྩོམ་པ་གང་ཞེ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2093]
དེ་ལ་དོན་ཉུང་བ་ནི་བདག་གི་དོན་དུ་ཡོ་བྱད་མང་པོ་མི་ཚོལ་བའོ། །

[Block 2094]
བྱ་བ་ཉུང་བ་ནི་འཇིག་རྟེན་གྱི་བྱ་བ་ཚོང་དང་ཞིང་རྨོད་པ༌[^1839]ལ་སོགས་པ་ཐམས་ཅད་མི་བྱེད་པའོ། །

[Block 2095]
སྨྲ་བ་ཉུང་བ་ནི་འགྲོ་བ་མང་པོ་ཚོགས་པའི་ནང་དུ་གཏམ་མི་བྱ་བ་སྣ་ཚོགས་ཀྱི་དུས་ཆུད་ཟ་བར་མི་བྱེད་པའོ། །

[Block 2096]
ཡོ་བྱད་ཉུང་བ་ནི་བདག་ལ་ཇི་ཙམ་དགོས་པའི་ལྷུང་བཟེད་དང་ཆོས་གོས་ལ་སོགས་པའི་ཡོ་བྱད་ལས་ལྷག་པར་མང་པོ་མི་འཆང་བའོ། །

[Block 2097]
ནམ་གྱི་ཆ་སྟོད་དང་ཆ་སྨད་ལ་མི་ཉལ་བ་ནི་དུས་དེ་གཉིས་སུ་ཡང་གཉིད་ཀྱིས་བསྒྲིབས་པ༌[^1840]མེད་པར་བྱས་ནས་ཇི་ལྟར་ཐོས་པའི་ཆོས་རྣམས་སེམས་ཤིང་བསྒོམ་པ་ལ་འབད་པར་བྱེད་པའོ། །

[Block 2098]
ཐོས་པའི་དོན་ལ་རྟོག་པ་ནི་དེ་ལྟར་སེམས་པའི་དུས་ན་ཆོས་གང་ཐོས་པའི་དོན་དེ་ཉིད་ལ་རྟོག་ཅིང་སེམས་ཀྱི་ཚིག་ཙམ་ལ་མི་བརྟེན༌[^1841]པའོ། །

[Block 2099]
ཡང་དང་ཡང་ཚོལ་བ་ནི་བསམ་པའི༌[^1842]ཆོས་དེ་ལ་ཡང་དང་ཡང་དུ་དཔྱོད༌[^1843]པའོ། །

[Block 2100]
སེམས་ལ་རྙོག་པ་མེད་པ་ནི་དེའི་དུས་ན་སེམས་རྨོངས་ཤིང་མི་གསལ་བར་མ་གྱུར་པའོ། །

[Block 2101]
ཡང་ན་སེམས་ལ་རྙོག་པ་མེད་པ་ནི་ཆོས་དེ་ཉིད་ལ་དད་ཅིང་ཡིད་ཆེས་པས་སེམས་དང་བའོ།[^1844] །སྒྲིབ་པ་རྣམས་རྣམ་པར་སེལ་བ་ནི་འདོད་པ་ལ་འདུན་པ་ལ་སོགས་པའི་སྒྲིབ་པ་ལྔ་རྣམས་ནི་མི་ལྡང་བར་གནོན་ཞིང་སེལ་བར་བྱེད་པའོ། །

[Block 2102]
ལྟུང་བ་རྣམས་ལས་འབྱུང་བ་ཤེས་པ་ནི་ཉེས་པ་བྱུང་བ་རྣམས་ཚངས་པ་འམ་ཐར་བར་བྱ་བའི་ཐབས་ལ་མཁས་པ་འམ། གཉེན་པོ་སྤྱོད་པ་ལ་མཁས་པའོ། །

[Block 2103]
འགྱོད་པ་མེད་པ་ནི་དགེ་བ་བྱས་པ་ལ་མི་འགྱེད་པའོ། །

[Block 2104]
ཀུན་ནས་ལྡང་བ་མེད་པ་ནི་ཉོན་མོངས་པ་རྣམས་སེམས་ལ་མི་སྐྱེ་བར་བྱེད་པའོ། །

[Block 2105]
སྒྲུབ་པའི༌[^1845]སྙིང་པོར་བྱེད་པ་ནི་ཚིག་ཙམ་གྱིས་ཆོག་པར་མི་འཛིན་གྱི། །ཇི་ལྟར་ཐོས་པའི་ཆོས་རྣམས་སྒྲུབ་པ་ལྷུར་བྱེད་པའོ། །
--- END BLOCKS ---
