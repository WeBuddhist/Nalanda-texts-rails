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
ལྷ་ཡི་སྲས་པོ་དེ་རྣམས་ཀྱི། །ཞེས་པ་ནས། འདི་ལ་གཞན་གྱིས་དད་པར་དཀའ། །ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་བདུན་ལ་བཞིར་དབྱེ་སྟེ་ཚིགས་བཅད་དང་པོ་གཉིས་ཀྱིས༌[^1608]སྔོན་བཤད་པའི་དོན་ཆུང་། ད་འདིར་བཤད་པ་ནི་དོན་ཆེ་བར་བསྟན་པ་དང་། དེའི་འོག་ཏུ་ཚིགས་བཅད་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་དོན་དམ་པའི་ཆོས་ལ་རྗེས་སུ་ཡི་རང་བར་བསྟོད་པ་དང་། ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་གཞན་རྟོགས་པ་བསྐྱེད་པས་བདག་ཉིད་ཀྱང་སངས་རྒྱས་སུ་འགྲུབ་པར་བསྟན་པ་དང་། ཚིགས་བཅད་གཅིག་གིས་ནི་བསྔོ་བ་སྟོན་ཏེ་འདི་ནི་དང་པོའོ། །

[Block 1927]
ཕུང་པོ་ལྔའི་སྐྱེ་བ་དང་འཇིག་པ་སྨོས་པས་བདེན་པ་བཞིའི་དོན་སྟོན་ཏེ། དྲང་བའི་དོན་སྤང་ཞིང་ངེས་པའི་དོན་ལ་འཇུག་པ་བསྟན་པའོ། །

[Block 1928 [HEADING]]
###### **དོན་དམ་པའི་ཆོས་ལ་རྗེས་སུ་ཡི་རང་བར་བསྟོད་པ།** ^4-3-4-2-5-2-1-2-2-0

[Block 1929]
མདོ་ལས།

[Block 1930]
རྣམ་པར་འདྲེན་པས་དེང་བཤད་དོ། །ཞེས་པ་ནས། དཔའ་བོ་བདག་ཅག་རྗེས༌[^1609]ཡི་རང་། །ཞེས་པའི་བར་དུ༌[^1610]ནི་ཆོས་དམ་པ་ལ་རྗེས་སུ་ཡི་རང་ཞིང་སྤྱོད་པ་ཆེན་པོ་ལ་གཞོལ་བ་བསྟན་ཏོ། །

[Block 1931 [HEADING]]
###### **གཞན་རྟོགས་པ་བསྐྱེད་པའི་སྒོ་ནས་བདག་ཉིད་བྱང་ཆུབ་པ་དང་བསྔོ་བ།** ^4-3-4-2-5-2-1-2-3-0

[Block 1932]
མདོ་ལས།

[Block 1933]
ལྡེམ་ངག་དྲང་སྲོང་ཞེས་གསུངས་ཏེ། །ཞེས་པ་ནས། བྱང་ཆུབ་ཏུ་ཡང་སྨོན་པར་ཤོག །ཅེས་པའི་བར་དུ་ནི་གཞན་རྟོགས་པ་བསྐྱེད་པའི༌[^1611]སྒོ་ནས་བདག་ཉིད་བྱང་ཆུབ་པ་དང་བསྔོ་བ་བསྟན་ཏོ། །

[Block 1934 [HEADING]]
#### དཔེས་དབང་པོ་འབྲིང་པོ་ལ་ཆོས་བསྟན་པ། ^4-3-5-0

[Block 1935 [HEADING]]
##### གཞན་གྱི་དོགས་པ་གླེང་བ། ^4-3-5-1-0

[Block 1936]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་སོམ་ཉི་དང་བྲལ་བར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་སྔར་དབང་པོ་རྣོན་པོ་ལ་དྲང་བ་དང་ངེས་པའི་དོན་བསྟན༌[^1612]ཏེ། དོན་དུ་གྱུར་པས་དབང་པོ་བར་མ་ལ་དཔེའི་སྒོ་ནས་བསྟན་པའི་ཕྱིར་འདི་སྟོན་ཏེ། འཕགས་པ་ཤཱ་རིའི་བུ་དོན་རྟོགས་ཏེ་ལུང་བསྟན་པ་ཐོས་པས༌[^1613]ཡང་བཅོམ་ལྡན་འདས་ལ་གསོལ་བ་ནི་བདག་དང་གཞན་ལ་ཕན་གདགས་པ་དང་། དེ་བཞིན་གཤེགས་པའི་དགོངས་པ་དང་མཐུན་པར་བྱ་བའི་ཕྱིར་ཤཱ་རིའི་བུས་གསོལ་ཏེ། མདོ་ལས་བཅོམ་ལྡན་འདས་གང་འདི་དག་ཅེས་པ་ནས་ཐེ་ཚོམ་འཚལ་བར་གྱུར་ན་ཞེས་པའི་བར་དུ༌[^1614]ནི་གཞན་གྱི༌[^1615]དོགས་པ་གླེང་བ་སྟེ། འབྱུང་བར་ལྟ་བ་དང་། འཇིག་པར་ལྟ་བ་ཞེས་པ་ནི་ཡོད་མེད་དུ་ལྟ་བའི་མཐའོ། །

[Block 1937]
བདག་ཏུ་ལྟ་བ་ནི་ལོག་པར་ལྟ་བའོ། །

[Block 1938]
ལྟ་བ་དེ་དག་གི་མུ་སྟེགས་ཅན་གྱི་ལྟ་བ་དྲུག་ཅུ་རྩ་གཉིས་དེར་འདུས་ཏེ་དེ་ལས་འཕེལ་བའོ། །

[Block 1939]
ལྟ་བ་དེ་དག་གི་སྐྱོན་དང་བྲལ་བའི་ཕྱིར་འདི་ལྟར་བསྟན་ཏོ། །

[Block 1940]
ཡང་ན་ལྟ་བ་དེ་གསུམ་གྱི་ཉོན་མོངས་པ་ཐམས་ཅད་བསྐྱེད་པའི༌[^1616]ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་ལྟ་བ་དེ་དག་དང་བྲལ་བའི་ཕྱིར་ཉོན་མོངས་པའི་རྒྱུ་བཀག་ན་འབྲས་བུ་ཡང་མི་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1941]
དེ་ལྟར་ཐེག་པ་ཆུང་ངུའི་མྱ་ངན་ལས་འདས་པའི༌[^1617]མཐར་ཕྱིན་པ་དག་ཡང་ངེས་པ་དང་དྲང་བའི་དོན་འདི་བསྟན་པས་ཐེ་ཚོམ་དུ་གྱུར་བའོ། །

[Block 1942 [HEADING]]
##### ཐེ་ཚོམ་བསལ་བར་གླེང་པ། ^4-3-5-2-0

[Block 1943]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཅི་ནས་འཁོར་བཞི་པོ་འདི་དག་ཅེས་པ་ནས་བདེ་བར་གཤེགས་པ༌[^1618]བཀའ་སྩལ་དུ་གསོལ་ཞེས་པའི་བར་དུ་ནི་ཐེ་ཚོམ་བསལ་བར་གླེང་པ་ལ་སྔར་ནི་གཏན་ཚིགས་གསོལ་དེའི་འོག་ཏུ་ནི་རིགས་པར་ཞི༌[^1619]བའོ། །

[Block 1944 [HEADING]]
##### མདོར་བསྡུས་ཏེ་གླེངས་པའི་ལན་བཏབ་པ། ^4-3-5-3-0

[Block 1945]
མདོ་ལས་དེ་སྐད་ཅེས་གསོལ་བ་དང་ཞེས་པ་ནས་བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་ཉིད་ལ་འཛུད་དོ་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས༌[^1620]དོན་ཆེན་པོ་སྟོན་པར་བཞེད་པ་ལ་མདོར་བསྡུས་ཏེ་གླེངས་པའི་ལན་བཏབ་པ་དང་། གྲོང་ཁྱེར་གྱི་དཔེ་བསྟན་པ་དང་། དཔེ་དང་དོན་དུ་སྦྱར་བ་དང་གསུམ་མོ། །

[Block 1946]
དེ་ཡང་འཕགས་པ་ཉན་ཐོས་པ་རྣམས་བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་ལ་གཟུད་ཅིང་སོ་སོའི་དད་པ་བཞིན་སྟོན་པའི་ཕྱིར་རྒྱུ་དང་དཔེ་སྣ་ཚོགས་ཀྱིས་སྔར་ནི་དྲང་བའི་དོན་བསྟན། ཕྱིས་འདིར་ནི་ངེས་པའི་དོན་སྟོན༌[^1621]པ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 1947 [HEADING]]
##### གྲོང་ཁྱེར་གྱི་དཔེ། ^4-3-5-4-0

[Block 1948]
མདོ་ལས་འདི་ལྟར་ཡང་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་དཔེས་དོན་ཤེས་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་ཐེ་ཚོམ་དགྲོལ་བར་དགོས་པའི༌[^1622]དཔེར་གླེང་པའོ། །

[Block 1949 [HEADING]]
###### ཚིག་རྐྱང་པ། ^4-3-5-4-1-0

[Block 1950]
མདོ་ལས་ཤཱ་རིའི་བུ་འདི་ལྟ་སྟེ་ཞེས་པ་ནས་དགོག་ཏུ་ཕྱིན་པ་ཞེས་པའི་བར་དུ་ནི་དཔེ་འདི་ལ་ཚིག་རྐྱང་པ་དང་ཚིགས་སུ་བཅད་པ་གཉིས་སུ་དབྱེའོ། །

[Block 1951]
ཚིག་རྐྱང་པ་ལ་སྔར་དཔེ་བསྟན། དེའི་འོག་ཏུ་དོན་སྟོན་ཏོ། །

[Block 1952 [HEADING]]
###### **དཔེ།** ^4-3-5-4-1-1-0

[Block 1953]
དཔེ་ཡང་སྔར་ནི་དྲང་བའི་དོན་གྱི་དཔེ། ཕྱིས་ནི་ངེས་པའི་དོན་གྱི་དཔེའོ། །

[Block 1954 [HEADING]]
###### **དྲང་བའི་དོན་གྱི་དཔེ།** ^4-3-5-4-1-1-1-0

[Block 1955]
དྲང་བའི་དོན་གྱི་དཔེ་ལ་ཡང་ཁམས་གསུམ་ན་སངས་རྒྱས་བཞུགས་པའི་དཔེ་དང་། འགྲོ་བ་རྣམ་ལྔ་ཡང༌[^1623]ཟ་བའི་དཔེ་དང་། ཁྱིམ་བདག་ཕྱུག་པོས་མེ་འབར་བ་ཆེན་པོ་མཐོང་བས་ཐབས་ཀྱིས༌[^1624]འདྲེན་པའི་དཔེ་དང་། བུ་རྣམས་ཀྱིས་ཁྱིམ་བདག་དེའི་ཚིག་མཉན་པས༌[^1625]སྡུག་བསྔལ་དེ་ལས་ཐར་བའི་དཔེའོ། །

[Block 1956 [HEADING]]
###### **ཁམས་གསུམ་ན་སངས་རྒྱས་བཞུགས་པའི་དཔེ།** ^4-3-5-4-1-1-1-1-0

[Block 1957]
དཔེ་དང་པོ་ལ་ཡང་རྣམ་པ་དྲུག་ཏུ་དབྱེ་སྟེ། དེའི་གནས་དང་དེའི་བདག་པོ་དང་། དེའི་རྒན་གཞོན་དང་། དེའི་འབྱོར་པ་དང་། དེའི་ཁང་ཁྱིམ་དང་། དེའི་སྐར་ཁུང་དང་། དྲུག་ཏུ་དབྱེའོ། །

[Block 1958]
གྲོང་ཁྱེར་དང་གྲོང་རྡལ་དང་ལྗོངས་ཞེས་པ་ནི་གནས་སོ། །

[Block 1959]
ཐེག་པ་རྣམ་གསུམ་སྟོང་པ་ཉིད་སྤྲུལ་པའི་སངས་རྒྱས་སུ་མངོན་ཏེ། དེ་ཉིད་སྟོང་གསུམ་གྱི་འཇིག་རྟེན་གྱི་ཁམས་ན་མངའ་མཛད་པའི་བདག་པོ་སྟེ། དེད་དཔོན་ཕྱུག་པོ་གྲོང་ཁྱེར་གྱི་བདག་པོ་བྱེད་པ་བཞིན་ནོ། །

[Block 1960]
དགོག་ཏུ་ཕྱིན་པ་ཞེས་པ་ནི་རྒན་གཞོན་བསྟན་པ་སྟེ། བཅོམ་ལྡན་འདས་མཁྱེན་པ་སྣ་ཚོགས་ཀྱིས་བགྲེས་ཤིང་མཐར་ཕྱིན་པ༌[^1626]ཞེས་པའོ། །

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
--- END BLOCKS ---
