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
མདོ་ལས་ཕྱུག་པོ་རིན་པོ་ཆེ་ཞེས་པ་ནས་སྒོ་གཅིག་པ་ཞེས་པའི་བར་དུ་ནི་འབྱོར་པ་བསྟན་ཏེ། ཕྱུག་ཅིང་རིན་པོ་ཆེ་མང་བ་ནི་འཕགས་པའི་ནོར་བདུན་དང་ལྡན་པའོ། །

[Block 1962]
ཁང་པ་ཞེས་པ་ནི་རྣམ་པར་སྨིན་པའི་རྣམ་པར་ཤེས་པ་ཉིད་ཁང་ཁྱིམ་ལྟ་བུར་བལྟའོ། །

[Block 1963]
ཡང་ན་འཇིག་རྟེན་གྱི་རྒྱལ་པོ་ཆེན་པོ་ངོས་བཞི་ལ་དབང་བྱེད་པ་བཞིན་བཅོམ་ལྡན་འདས་ཀྱང་སེམས་ཅན་མང་པོའི་གནས་དང་བདག་པོར་གྱུར་པའོ། །

[Block 1964]
སྒོ་གཅིག་པ་ཞེས་པ་སྒོ་ནི་འབྱུང་བ་དང་འཇུག་པའི་དགོས་པ་བྱེད་པ་བཞིན་ཐེག་པ་གཅིག་པོའི་བསྟན་པ་འདིས་སེམས་ཅན༌[^1627]ཐམས་ཅད་མྱ་ངན་ལས་འདའ་བའི༌[^1628]གནས་སུ་འདིས་འཇུག་པའི་ཕྱིར་སྒོ་ཞེས་བྱའོ། །

[Block 1965 [HEADING]]
###### **འགྲོ་བ་རྣམ་ལྔ་གཡང་ཟ་བའི་དཔེ།** ^4-3-5-4-1-1-1-2-0

[Block 1966 [HEADING]]
###### **སྲོག་ཆགས་མང་དུ་གནས་པ།** ^4-3-5-4-1-1-1-2-1-0

[Block 1967]
མདོ་ལས་ཞིག་ལ་ཐུག་པ་རྩྭས༌[^1629]གཡོགས་པ་ཞེས་པ་ནས་སྲོག་ཆགས་བརྒྱ་ཕྲག་གཅིག་གམ་གཉིས་སམ་ལྔའི་བར་དུ་དེ་ན་གནས་ཞེས་པའི་བར་དུ་ནི་འགྲོ་བ་རྣམ་ལྔ་གཡང་ཟ་བའི་དཔེ་སྟེ། འདི་མན་ཆད་སྲོག་ཆགས་མང་དུ་གནས་པ་དང་ཁང་ཁྱིམ་རྙིངས་པ་དང་ཕྱོགས་བཞི་ནས་མེ་འབར་བ་དང་། བུ་མང་པོ་དེ་ན་གནས་པའི་དཔེ་སྟོན་པ་ལ་འདི་ནི་དང་པོའོ། །

[Block 1968 [HEADING]]
###### **ཁང་ཁྱིམ་རྙིངས་པ།** ^4-3-5-4-1-1-1-2-2-0

[Block 1969]
མདོ་ལས་ཁྱིམས༌[^1630]རྣམས་ཀྱང་འདྲུམས་པ་ཞེས་པ་ནས་གོགས་པར་གྱུར་པའི་ཁང་པ་དེ་ལ་ཞེས་པའི་བར་དུ་ནི་གནས་རྙིང་པ༌[^1631]བསྟན་ཏེ། དཔེ་རྣམ་པ་བཞི་ཞིང་སྟོན་ཏོ། །

[Block 1970]
ཁང་པའི་དཔེ་ནི་གཟུགས་ཀྱི་དཔེའོ། །

[Block 1971]
རྩིག་པ་ནི་འདུ་ཤེས་ཀྱི་དཔེའོ། །

[Block 1972]
ཀ་བའི་རྩ་བ་རུལ་པ་ནི་འདུ་བྱེད་ཀྱི་དཔེའོ། །

[Block 1973]
གདུང་མ་གཡོ་བ་ནི་ཚོར་བའི་དཔེའོ། །

[Block 1974]
སྤྱིར་ཁང་པ་གཡོ་བ༌[^1632]ནི་རྣམ་པར་ཤེས་པའི་དཔེ་སྟེ། ཕུང་པོ་བཞི་རྣམ་པར་ཤེས་པ་ལ་བརྟེན་ཞེས་པའི་དོན་ཏོ། །

[Block 1975 [HEADING]]
###### **ཕྱོགས་བཞི་ནས་མེ་འབར་བ།** ^4-3-5-4-1-1-1-2-3-0

[Block 1976]
མདོ་ལས་གློ་བུར་དུ་མེའི་ཕུང་པོ་ཆེན་པོ་ངོས་ཐམས་ཅད་ནས་རབ་ཏུ་འབར་བར་གྱུར་ལ་ཞེས་པ་ལ་མེ་ཀུན་ནས་འབར་ཞེས་པ་ནི་སྐྱེ་བ་དང་འཇིག་པའི༌[^1633]མཚན་ཉིད་བཞི་པོ་དག་གིས་ཕུང་པོ་ལྔ་འཇོམས་ཞེས་པའི་དོན་ཏོ། །

[Block 1977]
གློ་བུར་ཞེས་པ་ནི་ལུགས་དང་རྒྱུ་མེད་པར་ཉོན་མོངས་པའི་མཚན་ཉིད་སྐད་ཅིག་གཅིག་ལ་སྐྱེ་ཞིང་འབྱུང་ཞེས་པའི་དོན་ཏོ། །

[Block 1978]
ཀུན་ནས་ཞེས་པ་ནི་སྐྱེ་བ་དང་རྒ་བ་དང་ན་བ་དང་ཤི་བས་འཇོམས་པའོ། །

[Block 1979 [HEADING]]
###### **བུ་མང་པོ་དེ་ན་གནས་པ།** ^4-3-5-4-1-1-1-2-4-0

[Block 1980]
མདོ་ལས་སྐྱེས་བུ་དེ་ལ་ཡང་ཞེས་པ་ནས་ཕྱི་རོལ་ཏུ་བྱུང་བར་གྱུར་ན་ཞེས་པའི་བར་དུ་ནི་འགྲོ་བ་རྣམ་ལྔའི་སེམས་ཅན་ཐམས་ཅད་ལ་བཅོམ་ལྡན་འདས་སྲས་དང་འདྲ་བའི་ཕྱིར་བུ་ཞེས་བཀའ་སྩལ་ཏོ། །

[Block 1981]
མདོ་དག་ལས་ཐེག་པ་རྣམ་པ༌[^1634]གསུམ་སོ་སོའི་སྤྱོད་པ་དང་། རིགས་ལས་བྱང་ཆུབ་སེམས་དཔའ་ནི་གྲངས་བཅུ་དང་སྦྱར། རང་སངས་རྒྱས་ནི་གྲངས་ཉི་ཤུ་དང་སྦྱར། ཉན་ཐོས་ནི་གྲངས་སུམ་ཅུ་དང་སྦྱར་ཞེས་འབྱུང་ངོ་། །

[Block 1982 [HEADING]]
###### **ཁྱིམ་བདག་ཕྱུག་པོས་མེ་འབར་བ་ཆེན་པོ་མཐོང་བས་ཐབས་ཀྱིས་འདྲེན་པའི་དཔེ།** ^4-3-5-4-1-1-1-3-0

[Block 1983]
མདོ་ལས་དེ་ནས་ཤཱ་རིའི་བུ་སྐྱེས་བུ་དེ་ཞེས་པ་ནས་སེམས་མི་དགའ་བར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་དྲང་བའི་ཐབས༌[^1635]སྦྱོར་བའི་དཔེ་སྟོན་ཏེ། །འདིས་བཅོམ་ལྡན་འདས་ཐུགས་རྗེ་ཆེན་པོས་སེམས་ཅན་ལ་དགོངས་ཤིང་འདྲེན་པའི་དཔེ་སྟོན་པ་ལ་མེ་དང་ཀུན་ལས་འབར་བའི་དོན་ནི་གོང་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 1984]
མདོ་ལས་འདི་ལྟར་བདག་ནི་མེའི་ཕུང་པོ་འདི་ཞེས་པ་ནས་ཕྱིར་འབྱུང་བར་ཡང་ཡིད་ལ་བྱ་བ་མི་བསྐྱེད༌[^1636]དོ་སྙམ་དུ་སེམས་སོ་ཞེས་པའི་བར་དུ་ནི་འདིས་བཅོམ་ལྡན་འདས་ཐུགས་རྗེས་སེམས་ཅན་རྣམས་ལ་ཕན་འདོགས་པར་དགོངས་པའི་དཔེ་སྟེ། འབར་བའི་སྒོ་ཞེས་པ་ནི་ཐེག་པ་གཅིག་པུ༌[^1637]སྟོན་པ་དམ་པའི་ཆོས་ལ་སྐུར་བ༌[^1638]འདེབས་ཤིང་མ་དད་པ་རྣམས་ཉོན་མོངས་པ་ཕྲག་དོག་གི་སེམས་ཀྱིས༌[^1639]མདོ་སྡེ་འདི་ལ་འཇུག་པ་སྟོང་པ་རྣམ་པ༌[^1640]གཉིས་དང་ཕན་པ་རྣམ་གཉིས་ཀྱི་སྤྱོད་པ་སྲེག་ཅེས་པའི་དོན་ཏོ། །

[Block 1985]
རྩེ་དགའ་ཞེས་པ་ནི་གནས་དང་ཁམས་དང་ཐེག་པ་ལ་སོགས་པ་ལ་ཆགས་ཤིང་བག་མེད་པར་སྤྱོད་པའི་དོན་ཏོ། །

[Block 1986]
མི་ཤེས་ཁོང་དུ་མི་ཆུད་པ་ནི་མངོན་སུམ་དང་རྗེས་སུ་དཔོག་པའི་སྒོ་ནས་མི་འཇུག་པའོ། །

[Block 1987]
ཡང་ན་མི་དང༌[^1641]མི་འཇིགས་སྐྱེ༌[^1642]ཞིང་སྤོང་བར་མི་བྱེད་ཅེས་པའི་དོན་ཏོ། །

[Block 1988]
ཕྱིར་འབྱུང་བར་ཡིད་ལ་མི་བྱེད་པ་ནི་ཐེག་པ་ཆེན་པོའི་མྱ་ངན་ལས་འདའ་བ་མི་ཚོལ༌[^1643]བའོ། །

[Block 1989 [HEADING]]
###### **ཐེག་པ་ཆེན་པོ་འདིར་གཟུད་པ།** ^4-3-5-4-1-1-1-3-1-0

[Block 1990]
མདོ་ལས་ཤཱ་རིའི་བུ་སྐྱེས་བུ་དེ་ཞེས་པ་ནས་འབྱུང་ངོ་སྙམ་དུ་བསམས་པ་དང་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆེན་པོ་འདིར་གཟུད་པ་ཡང་ཐེག་པ་ཆེན་པོའི་འབྲས་བུ་བསྟན་ཏེ། གཟུད་པ་དང་རྒྱུ་བསྟན་ཏེ་གཟུད་པ་དང་། ཐེག་པ་ཆེན་པོའི་སྤྱོད་པ་བསྟན་ཏེ་གཟུད་པ་དང་། ཆེན་པོ་ལ་རེག་པ་བསྐྱེད༌[^1644]དེ་གཟུད་པ་ལ་འདི་ནི་དང་པོའོ། །

[Block 1991 [HEADING]]
###### **ཐེག་པ་ཆེན་པོའི་འབྲས་བུ་བསྟན་ཏེ་གཟུད་པ།** ^4-3-5-4-1-1-1-3-1-1-0

[Block 1992]
ཐེག་པ་ཆེན་པོའི་འབྲས་བུ་ནི་ཡེ་ཤེས་རྣམ་གཉིས་དང་ལྡན་པའོ། །

[Block 1993]
སྟོབས་དང་ལྡན་པ་ནི་ཡང་དག་པའི་ཡེ་ཤེས་རྣམ་གཉིས་སྐུ་ལྟ་བུར་ལྟ་བ༌[^1645]དེ་དང་ལྡན་པའོ། །

[Block 1994]
སྟོབས་ཆེ་བ་ཞེས་པ་ནི་མངོན་པར་ཤེས་པ་དྲུག་དང་ལྡན་པའི་སྐུའི་ཡན་ལག་ལྟ་བུར་བལྟ་བས༌[^1646]དེ་གཉིས་དང་ལྡན་པའི་ཕྱིར་ཐེག་པ་རྣམ་གཉིས་པ༌[^1647]ཐེག་པ་ཆེན་པོ་ལ་མངོན་དུ་དད་པ་མེད་ཀྱིས་ཀྱང་ཡོན་ཏན་དེ་གཉིས་ཀྱི༌[^1648]མཐུས་བསྒྱུར་ཞིང་ཐེག་པ་ཆེན་པོ་ལ་འཛུད་ཅེས་པའོ། །

[Block 1995]
ཐེག་པ་བར་མ་ནི་བཅོམ་ལྡན་འདས་ཀྱི་ཡེ་ཤེས་རྣམ་གཉིས་ཀྱི༌[^1649]མཐུས་འཛུད་དོ། །

[Block 1996]
ཉན་ཐོས་པ༌[^1650]རྣམས་ནི་བུས་པ༌[^1651]མང༌[^1652]དུ་བླངས་ཏེ་སྒོར་འབྱིན་པ་བཞིན་མངོན་པར་ཤེས་པའི་མཐུས་ཐེག་པ་ཆེན་པོ་ལ་འཛུད་དོ། །

[Block 1997 [HEADING]]
###### **རྒྱུ་བསྟན་ཏེ་འཛུད་པ།** ^4-3-5-4-1-1-1-3-1-2-0

[Block 1998]
མདོ་ལས་དེ་ཡང་འདི་སྙམ་དུ་སེམས་ཏེ་ཁང་པ་འདི་སྲང་གཅིག་ལ་སྒོ་ཡང་དོག་ཅེས་པ་ནི་ཐེག་པ་ཆེན་པོའི་རྒྱུད་བསྟན་ཏེ་འཛུད་པ་སྟེ། དེ་ལས༌[^1653]རྒྱུ་བསྟན་པ་ཡང་ཐེག་པ་ཆེན་པོའི་སྤྱོད་པ་ཆེན་པོ་ལ་བརྟེན་པ་དང་། སྐུར་བའི་སེམས་སྐྱེས་ན་ངན་སོང་དུ་ལྟུང་བར་བསྟན་པ་དང་། དཀའ་བ་སྣ་ཚོགས་སྟོན་ཅིང་ཐེག་པ་ཆེན་པོ་ཉིད་གསངས་ཏེ་སྨོན་པ༌[^1654]དང་གསུམ་ལས༌[^1655]འདི་ནི་དང་པོའོ། །

[Block 1999 [HEADING]]
###### **ཐེག་པ་ཆེན་པོའི་སྤྱོད་པ་ཆེན་པོ་ལ་བརྟེན་པ།** ^4-3-5-4-1-1-1-3-1-2-1-0

[Block 2000]
ཁམས་གསུམ་ནས་འབྱུང་བའི༌[^1656]སྲང་ཐེག་པ་ཆེན་པོ་གཅིག་ཡིན་པའི་ཕྱིར་སྲང་གཅིག་ཅེས་པ་དང་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་ཉན་ཐོས་པའི་སྤྱོད་པས་མི་ཆུད་པའི་ཕྱིར་སྒོ་ཡང་དོག༌[^1657]པ་ཞེས་སྨོས་ཏེ། རྒྱ་མཚོ་ཤིན་ཏུ་ཡངས་ཀྱང་མི་རོ་ཞག་ཏུ་མི་འཇོག་པ༌[^1658]བཞིན་ནོ། །
--- END BLOCKS ---
