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
མདོ་ལས་ཤཱ་རིའི་བུ་ཁྱོད་འདི་ལྟར་ཞེས་པ་ནས་མྱ་ངན་ལས་འདས་སོ་སྙམ་དུ་སེམས་ཏེ་ཞེས་པའི་བར་དུ་ནི་ཕྱིས་ཡང་དག་པ་ཉིད་ལ་གནས་པར་འགྱུར་བ་བསྟན་ཏེ། མི་དྲན་ནས་ཞེས་པ་ནི་དྲང་བའི་དོན་ལ་བརྟེན༌[^1511]ཅིང་ངེས་པའི་དོན་བརྗོད་པའོ། །

[Block 1822]
འཕགས་པ་ཉན་ཐོས་པའི་ཡེ་ཤེས་དང་མྱ་ངན་ལས་འདས་པ༌[^1512]ཉིད་མཐར་ཕྱིན་པའི་གནས་ཙམ་དུ་གནས༌[^1513]ཤིང་ཐེག་པ་ཆེན་པོའི་ཡེ་ཤེས་དང༌[^1514]མྱ་ངན་ལས་འདས་པ་མི་འགྲུབ་པའོ། །

[Block 1823]
མདོ་ལས་ཤཱ་རིའི་བུ་ངས་ཁྱོད་ཀྱི་སྤྱོད་པ༌[^1515]དང་ཞེས་པ་ནས་ཉན་ཐོས་པ་རྣམས་ལ་ཡང་དག་པར་བསྟན་ཏོ་ཞེས་པའི་བར་དུ་སྔོན་ཐེག་པ་ཆེན་པོ་སྤྱོད་པའི་སེམས་དྲན་པ་དང་བསྐུལ་བ་སྟེ། དམ་པའི་ཆོས་དང་བསམ་གྱིས་མི་ཁྱབ་པ་བྱང་ཆུབ་སེམས་དཔའ་ལ་གདམས་པ་དང་། སངས་རྒྱས་ཀྱིས༌[^1516]ཡོངས་སུ་གཟུང་བ༌[^1517]ནི་མདོ་སྡེ་འདི་ཉིད་ཀྱི་རྣམ་གྲངས་ཏེ། འདི་ཐེག་པ་ཆེན་པོ་ལ་འཇུག་པའི་ཐབས་དང་སྤྱོད་པ་ཐོབ་པར་འགྱུར་བ་བསྟན་ཏོ། །

[Block 1824 [HEADING]]
###### ལུང་བསྟན་པ། ^4-3-4-2-4-0

[Block 1825]
མདོ་ལས་ཤཱ་རིའི་བུ་ཁྱོད་ནི་འདི་ལྟར་མ་འོངས་པའི་དུས་ཞེས་པ་ནས་འདི་དག་ཡོངས་སུ་རྫོགས་པར་བྱས་ནས་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་དུམ་བུ་བཞིར་དབྱེ་སྟེ། སྔར་ལུང་བསྟན་པ་དང་། ལྷ་དང་མིས་མཆོད་ཅིང་བསྟོད་པའོ། །

[Block 1826]
དང་པོ་ལ་ཡང་གཉིས་ཏེ། རྒྱུའི་སྒོ་ནས་ལུང་བསྟན་པ་དང་། འབྲས་བུའི་སྒོ་ནས་ལུང་བསྟན་པའོ། །

[Block 1827 [HEADING]]
###### **རྒྱུའི་སྒོ་ནས་ལུང་བསྟན་པ།** ^4-3-4-2-4-1-0

[Block 1828]
དེའི་དང་པོ་ལ་ཡང་བཞི་སྟེ། བསྐལ་པ་ཚད་མེད་ཅེས་པ་ནི་དུས་བསྟན་པའོ། །

[Block 1829]
དེ་བཞིན་གཤེགས་པ་བྱེ་བ་ཁྲག་ཁྲིག་ཅེས་པ་ནི་བཤེས་གཉེན་དམ་པ་བསྟན་པའོ། །

[Block 1830]
དམ་པའི་ཆོས་འཛིན་པ་དང་། སེམས་ཅན་མང་པོ་ལ་ཕན་པ་སྣ་ཚོགས་བྱས་ནས་བླ་ན་མེད་པའི་སངས་རྒྱས་སུ་འགྲུབ་ཅེས་པའོ། །

[Block 1831 [HEADING]]
###### **འབྲས་བུའི་སྒོ་ནས་ལུང་བསྟན་པ།** ^4-3-4-2-4-2-0

[Block 1832]
མདོ་ལས་པད་མོའི་འོད་ཅེས་བྱ་བ་ཞེས་པ་ནས་འཇིག་རྟེན་དུ་འབྱུང་ངོ་ཞེས་པའི་བར་དུ་ནི་འབྲས་བུ་དངོས་སུ་ལུང་བསྟན་པ་སྟེ། དེ་ཡང་ཚིག་རྐྱང་པ་དང་ཚིགས་སུ་བཅད་པ་དབྱེའོ། །

[Block 1833 [HEADING]]
###### **ཚིག་རྐྱང་པ།** ^4-3-4-2-4-2-1-0

[Block 1834]
ཚིག་རྐྱང་པ་ལ་ཡང་རྣམ་པ་དྲུག་སྟེ། ནང་གི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་དང་། ཕྱིའི་ཞིང་རྒྱན་དམ་པ་དང་ལྡན་པ་དང་། ཆོས་སྟོན་པའི་ལུགས་གཅིག་པ་དང་བསྐལ་བའི་མིང་མི་མཐུན་པ༌[^1518]དང་། འཁོར་བཟང་ངན་དང་ཆོས་གནས་པའི་ཡུན་རིང་ཐུང་དང་དྲུག་ལས༌[^1519]འདི་ནི་དང་པོའོ། །

[Block 1835 [HEADING]]
###### **ནང་གི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ།** ^4-3-4-2-4-2-1-1-0

[Block 1836]
སངས་རྒྱས་ཀྱི་མཚན་འདོགས་པ་ཡང་ལ་ལ་ནི་སྔོན་གྱི་སངས་རྒྱས་མཐོང་བ་ལས་དྲས་ཏེ༌[^1520]མཚན་བཏགས་པ་དང་སེམས་བསྐྱེད་པའི་སྒོ་དང་། མཚན་མ་ལས་མཚན་འདོགས་པ་དང་། ཡུལ་དང་སེམས་ཅན་གྱི་དོན་མཛད་པ་ལས་མཚན་འདོགས་པ་སྟེ། འཕགས་པ་ཤཱ་རིའི་བུ་མངོན་པར་བྱང་ཆུབ་པའི་མཚན་པདྨོའི་འོད་ཅེས་བཏགས་པ་ནི་མེ་ཏོག་གི་ཆར༌[^1521]བབ་ཅིང་འོད་ཀྱིས༌[^1522]སྣང་བར་མཛད་པས་དེ་བཞིན་གཤེགས་པ༌[^1523]པདྨོའི་ཡེ་ཤེས་འོད་ཀྱིས༌[^1524]སྣང་བར་མཛད་པ་ལས་པདྨོའི་འོད་ཅེས་གདགས་པ་དང་། དམ་པའི་ཆོས་ཀྱི་རོ་མྱོང༌[^1525]བས་ཡེ་ཤེས་ཀྱི་འོད་ཤར་ཏེ། ཐེག་པ་རྣམ་པ༌[^1526]གཉིས༌[^1527]ལ་སྣང་བར་མཛད་པའི་པདྨོའི་འོད་ཅེས་བཏགས་སོ། །

[Block 1837 [HEADING]]
###### **ལུང་སྟོན་པ།** ^4-3-4-2-4-2-1-1-1-0

[Block 1838]
དེ་ལ་ལུང་སྟོན་པ་ཡང་རྣམ་པ་བཞི་སྟེ། ཅིའི་ཕྱིར་ལུང་སྟོན་པ་དང་། སུས་ལུང་སྟོན་པ་དང་། དོགས་པ་བསལ་བ་དང་བཞིའོ། །

[Block 1839 [HEADING]]
###### **ཅིའི་ཕྱིར་ལུང་སྟོན་པ།** ^4-3-4-2-4-2-1-1-1-1-0

[Block 1840]
ཅིའི་ཕྱིར་ལུང་བསྟན་པ་ཡང་རྣམ་པ་ལྔ་སྟེ། འཕགས་པ་ཉན་ཐོས་པའི་རྣམས་ངེས་པའི་སེམས་བསྐྱེད་པ་སྟེ། ཉན་ཐོས་པའི་ཆོས་ཉིད་མ་ཡིན་པ་དང་། བདག་མེད་པ་དང་རྣམ༌[^1528]གཉིས་ཉན་ཐོས་པས་ཆུད་པར་བྱ་བ་མ་ཡིན་པར་སེམས་པ་དག་སེམས་ངེས་པས་ཐེག་པ་ཆེན་པོ་ལ་བཞུགས༌[^1529]པའི་ཕྱིར་ལུང་བསྟན་པ་དང་། དེ་བཞིན་གཤེགས་པའི་ཆོས་ཀྱི་སྐུ་མཉམ་པ་ཉིད་འདུས་བྱས་ཀྱི་དབྱེ་བ༌[^1530]ཙམ་དུ་ཟད་ཀྱི་ཐེག་པ་རྣམ་གསུམ་ཡང་དག་པའི་གཞུང་མི་མཐུན་པ་མེད་པར་ལུང་བསྟན་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་འཕགས་པ་ཉན་ཐོས་པ་རྣམས་ཐེག་པ་ཆེན་པོའི་མྱ་ངན་ལས་འདས་པ་གཏན་མི་འཐོག་པ༌[^1531]ཙམ་དུ་སེམས་པའི༌[^1532]ཐེ་ཚོམ་བཅད་པའི་ཕྱིར་ལུང་བསྟན་པ་དང་། ལུང་བསྟན་པ་འདིས་ཀུན་ལ་སངས་རྒྱས་སུ་འགྲུབ་པའི་རྒྱུ་ཡོད་པར་བསྟན་པས་སངས་རྒྱས་ཀྱི་སྤྱོད་པ་ལ་མང་པོ་གཟུད་པའི་ཕྱིར་ལུང་བསྟན་པ་དང་། ཐེག་པ་གཅིག་པོ་འདི་རྟོགས་པས་ལུང་བསྟན་པ་དང་ལྔའོ། །

[Block 1841 [HEADING]]
###### **སུས་ལུང་སྟོན་པ།** ^4-3-4-2-4-2-1-1-1-2-0

[Block 1842]
སུས་ལུང་སྟོན་པ་ནི་རྣམ་པ་གསུམ་དུ་དབྱེ་སྟེ། ཅི་ལ་གནས་པ་དང་ལུང་སྟོན་པའི་རང་བཞིན་དང་། ལུང་སྟོན་པའི་ལས་སོ། །

[Block 1843 [HEADING]]
###### **ཅི་ལ་གནས་ཏེ་ལུང་སྟོན་པ།** ^4-3-4-2-4-2-1-1-1-2-1-0

[Block 1844]
ཅི་ལ་གནས་ཏེ་ལུང་སྟོན་པ་ནི་ལུང་སྟོན་པ་རྣམ་པ༌[^1533]དྲུག་ལས།

[Block 1845]
ལྔ་ནི་བཅོམ་ལྡན་འདས་ཉག་གཅིག་གིས་མཁྱེན་ཅིང་ལུང་སྟོན། གཅིག་ནི་བྱང་ཆུབ་སེམས་དཔས་ལུང་སྟོན་ཏེ། དེ་བཞིན་གཤེགས་པས་ལུང་སྟོན་པ་ལྔ་ནི་བྱེ་བྲག་ཏུ་ལུང་སྟོན་པ་དང་། མཐུན་པར་ལུང་སྟོན་པ་དང་། ཕྱིས་ལུང་སྟོན་པ་དང་། བཀོལ་བ་མེད་པའི་ལུང་སྟོན་པ་དང་། སྤྱོད་པ་ལས་ལུང་སྟོན་པའོ། །

[Block 1846]
བྱང་ཆུབ་སེམས་དཔས་ནི་རྒྱུ་དང་ལྡན་པ་ཙམ་ལ་ལུང་སྟོན་ཏེ། །ཇི་ལྟར་རྟག་ཏུ་མི་བརྙས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་ཅན་ཐམས་ཅད་དེ་བཞིན་གཤེགས་པའི་རང་བཞིན་ཅན་ནོ་ཞེས་ལུང་སྟོན་པ་སྟེ། ལུང་སྟོན་པར་ནུས་པ་དེ་གཉིས་ལས་གཞན་མེད་དོ་ཞེས་པའོ། །

[Block 1847 [HEADING]]
###### **ལུང་སྟོན་པའི་རང་བཞིན།** ^4-3-4-2-4-2-1-1-1-2-2-0

[Block 1848]
ལུང་སྟོན་པའི་རང་བཞིན་ནི་ཕྱིས་ཐོབ་པའི་ཡེ་ཤེས་དང་། ཀུན་རྫོབ་ཀྱི་ཡེ་ཤེས་སོ། །

[Block 1849 [HEADING]]
###### **ལུང་སྟོན་པའི་ལས།** ^4-3-4-2-4-2-1-1-1-2-3-0

[Block 1850]
ལུང་སྟོན་པའི་ལས༌[^1534]ནི་ཚིག་གིས༌[^1535]སྤྱོད་པ་སྟེ། སྤྲུལ་པའི་སྐུ་ལ་སོགས་པ་ལ་ལྡན་པ་དང་བཅས་པའོ། །

[Block 1851]
སུས་ལུང་སྟོན་པ་ནི་གང་ལ་བརྟེན་པ་དང༌[^1536]རང་བཞིན་ནོ། །

[Block 1852 [HEADING]]
###### **ལུང་བསྟན་པར་བྱ་བ།** ^4-3-4-2-4-2-1-1-1-3-0

[Block 1853]
གང་ལུང་བསྟན་པར་བྱ་བ་ཉིད་གང་ལ་བརྟེན་པ༌[^1537]སྟེ། ལུང་བསྟན་པར་བྱ་བ་རྣམ་པ༌[^1538]དྲུག་ལ། འཕགས་པ་ཤཱ་རིའི་བུ་ལ་སོགས་པ་ཉན་ཐོས་ཆེན་པོ་བཞི་སོ་སོར་ཕྱེ་སྟེ་ལུང་བསྟན་པ་དང་། འཕགས་པ་གང་པོ་ལ་སོགས་པ་དགེ་སློང་ལྔ་བརྒྱ་མཚན་གཅིག་པ་ལ་སོགས་པ་སྤྱིར་མཐུན་པར་ལུང་བསྟན་པ་དང་། སློབ་པ་དང་མི་སློབ་པ་ལ་སོགས་པ་དབང་པོ་ཞན་པ་རྣམས་ཕྱིས་ལུང་བསྟན་པ་དང་། ལྷས་བྱིན་ལྟ་བུ་ལུང་བསྟན་པས་བཀོལ་བ་མེད་པར་ལུང་བསྟན་པ་དང་། སྤྱོད་པ་ལས་ལུང་བསྟན་པ་སྟེ། དགེ་སློང་མ་དང་ལྷའི་བུ་མོ་ལ་སོགས་པ་ལུང་བསྟན་པ་དང་། རྒྱུ་དང་ལྡན་པ་ཙམ་ལས་ལུང་བསྟན་པ་སྟེ། སེམས་ཅན་ཐམས་ཅད་ལ༌[^1539]སངས་རྒྱས་ཀྱི་རང་བཞིན་ཡོད་པར་ལུང་བསྟན་པ་སྟེ། ཞིབ་ཏུ་མདོ་འདི་ཉིད་ཀྱི་སོ་སོའི་ལེའུ་ལས་འབྱུང་བ་བཞིན་དུ་སྦྱར་རོ། །

[Block 1854 [HEADING]]
###### **དོགས་པ་བསལ་བ།** ^4-3-4-2-4-2-1-1-1-4-0

[Block 1855]
དོགས་པ་བསལ་བ༌[^1540]ནི་འཕགས་པ་ཉན་ཐོས་པ་རྣམས་ལུང་བསྟན་པ་ངེས་པར་སངས་རྒྱས་སུ་འགྲུབ་པ་ཡིན་ནམ། ཐབས་ཀྱིས༌[^1541]བསྟན། དེ་སྟེ་ངེས་པར་འགྲུབ་པ་ཡིན་ན་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་རླབས་པོ༌[^1542]ཆེ་དེ་སྙེད༌[^1543]སྤྱད་ཀྱང་ཅི་དགོས། དེ་སྟེ་ངེས་པར་འགྲུབ་པ་མ་ཡིན་ན་ནི་འགྲུབ་པར་ཅིའི་ཕྱིར་ལུང་བསྟན། དེ་ནི་འཕགས་པ་ཉན་ཐོས་པ་རྣམས་ཐེག་པ་ཆེན་པོར་ངེས་པའི་སེམས༌[^1544]བསྐྱེད་པ་ལ་དགོངས་ཏེ་ལུང་བསྟན་གྱི་གྲུབ་ཟིན་པའི་རང་བཞིན་ལས་ལུང་བསྟན་པ་མ་ཡིན་པ་དང་། ཡང་དེ་བཞིན་གཤེགས་པས་ཐེག་པ་གསུམ་མཉམ་པ་སྟེ། ཐེག་པ་གཅིག་པོར་བསྡུ་ཞིང་ཆོས་ཀྱི་སྐུ་དང་། འཕགས་པ་ཉན་ཐོས་པས༌[^1545]ལུས་སུ་ཡང་མཉམ་པ་ཉིད་པས་ལུང༌[^1546]བསྟན་པ་ཡིན་གྱི། སྤྱོད་པ་དང་ཡོན་ཏན་ཐམས་ཅད་རྫོགས་པའི་སྒོ་ནས་ལུང་བསྟན་པ་མ་ཡིན་ནོ། །

[Block 1856 [HEADING]]
###### **ཕྱིའི་ཞིང་རྒྱན་དམ་པ་དང་ལྡན་པ།** ^4-3-4-2-4-2-1-2-0

[Block 1857]
མདོ་ལས་ཤཱ་རིའི་བུ་དེའི་ཚེ་ན་ཞེས་པ་ནས་ལྷ་དང་མི་མང་པོས་རབ་ཏུ་གང་ཞེས་པའི་བར་དུ་ནི་ཕྱིའི་ཞིང་རྒྱན་དམ་པ་དང་ལྡན་པ་སྟེ། [^1547]ཞིང་རྣམ་པར་དག་པའོ། །

[Block 1858]
དེ་ལ་ཡང་དགའ་བ༌[^1548]འབའ་ཞིག་གིས་བསྐྱེད་པའི་ཕྱིར་རྡུལ་མེད་པའི་ཕྱིར༌[^1549]ཞིང་ཞེས་བྱ་སྟེ། དྲི་མའི་སྐྱོན་མེད་པའོ། །

[Block 1859]
ང་རྒྱལ་གྱི་སེམས་སྤངས་པས༌[^1550]མཉམ་ཞིང་མཐོ་དམན་མེད་པ་དང་། སེམས་ཅན་གྱི་སེམས་རྣམ་པར་དག་པ་ཕྱིར་ཞིང་རྣམ་པར་དག་པ་རྒྱན་སྣ་ཚོགས་ཀྱིས་བརྒྱན་པ་དང་། གསོད་པ་དང་འཕྲོག༌[^1551]པའི་སེམས་དང་བྲལ་བའི་ཕྱིར་བདེ་བ་སྐྱིད་པ་ནད་དང་མུ་གེ་མེད་པའི་ཞིང་དང་། སྡིག་པའི་བཤེས་གཉེན་དང་བྲལ་བའི་ཕྱིར་ལྷ་དང་མིས༌[^1552]ཡོངས་སུ་རྒྱས་པའོ། །

[Block 1860]
མདོ་ལས་བཻ་ཌཱུརྱ་ལས་བྱས་པ་ཞེས་བྱ་བ་ནས་མེ་ཏོག་འབྲས་བུར་ལྡན་ནོ་ཞེས་པའི་བར་དུ་ནི་སེམས་ཀྱི་སྐྱོན་དང་བྲལ་བའི་ཕྱིར་ཞིང་བཻ་ཌཱུརྱ་ལྟར་རྣམ་པར་དག་པ་སྟོང་པ་བརྒྱད་ལ་གནས་ཤིང་འཕགས་པའི་ལམ་བརྒྱད་སྒྲུབ༌[^1553]པའི་ཕྱིར་གསེར་གྱི་ཐིག་གིས་ཕྱོགས་བརྒྱད་དུ་རེའུ་མིག་བྲིས༌[^1554]པའོ། །
--- END BLOCKS ---
