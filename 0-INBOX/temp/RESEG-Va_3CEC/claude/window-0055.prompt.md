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
མཐོང་བའི་ལམ་སེམས་ཀྱི་སྐད་ཅིག་མ་བཅུ་དྲུག་ལ་གནས་པ་ནི། རྒྱུན་དུ་ཞུགས་པའི་གང་ཟག་གོ། །

[Block 1927]
གང་བསྒོམ་པའི་ལམ་འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་རྣམ་པ༌[^1699]དྲུག་སྤངས་པའི་ལམ་ལ་གནས་པ་ནི་ལན་ཅིག་ཕྱིར་འོང་བའི་གང་ཟག་གོ། །

[Block 1928]
གང་བསྒོམ་པའི་ལམ་འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པའི་རྣམ་པ་ཐམས་ཅད་སྤངས་པའི་ལམ་ལ་གནས་པ་ནི་ཕྱིར་མི་འོང་བའི་གང་ཟག་གོ། །

[Block 1929]
སྲིད་པའི་རྩེ་མོའི་ཉོན་མོངས་པ་རྣམ་པ་དགུ་ཆར་སྤངས་པའི་ལམ་ལ་གནས་པ་ནི་དགྲ་བཅོམ་པའི་གང་ཟག་གོ། །

[Block 1930]
སངས་རྒྱས་འཇིག་རྟེན་དུ་མ་བྱུང་བའི་ཚེ་འདོད་པའི་ཁམས་སུ་སྐྱེས་ནས་གཞན་གྱི་མན་ངག་མེད་པར་ཁམས་གསུམ་གྱི་ཉོན་མོངས་པ་ཐམས་ཅད་སྤངས་ཏེ་རང་བྱང་ཆུབ་མངོན་སུམ་དུ་བྱས་པ་ནི་རང་སངས་རྒྱས་ཀྱི་གང་ཟག་གོ། །

[Block 1931]
མོས་པས་སྤྱོད་པའི་ས་ནས་བརྩམས་ནས་ས༌[^1700]བཅུ་མན་ཆད་ལ་གནས་པ་བདག་དང་གཞན་གྱི་དོན་གྱི༌[^1701]ཕྱིར་ཞུགས་པ་རྣམས་ནི་བྱང་ཆུབ་སེམས་དཔའི་གང་ཟག་གོ། །

[Block 1932]
གང་ཟག་གཅིག་ཅེས་བྱ་བས་དེ་བཞིན་གཤེགས་པ་གཉིས་འཇིག་རྟེན་དུ་འབྱུང་བ་མི་སྲིད་པར་སྟོན་ཏོ། །

[Block 1933]
འཇིག་རྟེན་དུ་འབྱུང་བ་ན་ཞེས་བྱ་བ་ནི་དགའ་ལྡན་གྱི་ཕོ་བྲང་ནས་འཆི་འཕོ་བ་བསྟན་ཏེ། འདོད་པའི་ཁམས་སུ་སྐྱེས༌[^1702]ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1934]
ཕན་པ་ནི་འདོད་པའི་བསོད་ཉམས༌[^1703]ཀྱི་མཐའ་ཡོངས་སུ་སྤངས་པའོ། །

[Block 1935]
བདེ་བ་ནི་བདག་ཉིད་ངལ་བའི་མཐའ་ཡོངས་སུ་སྤངས་པའོ། །

[Block 1936]
འཇིག་རྟེན་ལ་སྙིང་བརྩེ་བ༌[^1704]ནི་འཇིག་རྟེན་དུ་སྐྱེ་ཞིང་ལམ་དབུ་མ་སྟོན་པ་ཡང་། སེམས་ཅན་ལ་ཐུགས༌[^1705]རྗེའི་རྒྱུས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1937]
དོན་ནི་མྱ་ངན་ལས་འདས་པའི་འབྲས་བུ་ལ་གཞག་པའོ། །

[Block 1938]
སྟོན་པ་ནི་འཕགས་པའི་བདེན་པ་བཞི་འཆད་པའི་ཕྱིར་རོ། །

[Block 1939]
དེ༌[^1706]ནི་གང་ཟག་ཅེས་བྱའོ་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པ་དེ་དག་ནི་གང་ཟག་ཅེས་བྱའོ། །

[Block 1940]
ཀུན་རྫོབ་ཀྱི་ཚིག་གི་གནས་ཀྱིས་ཞེས་བྱ་བ་ནི་གང་ཟག་ཅེས་གསུངས་པ་ཡང་གང་ཟག་གི་དངོས་པོ་ཡོད་པའི་ཕྱིར་གསུངས་པ་ནི་མ་ཡིན་གྱི། གང་ཟག་ཅེས་གང་ཟག་གི་ཚིག་མ་བརྟགས༌[^1707]ན་ཐ་སྙད་དུ་བྱ་ཞིང་སེམས་ཅན་དྲང་དུ་མི་རུང་བས་སེམས༌[^1708]ཅན་རྣམ་གྲངས་མང་པོའི་ཕྱིར་ཀུན་རྫོབ་ཙམ་དུ་བཏགས་ནས་བསྟན་པ་སྟེ།[^1709] བཏགས་པ་ཙམ་ལ་གང་ཟག་གི་དངོས་པོ་ཡོད་པར་མངོན་པར་ཆགས་པ་དེ་དག་ནི་ཆོས་ཉིད་ལ་སྟོན་པ་མ་ཡིན་ནོ། །

[Block 1941]
འབྱུང་བ་མེད་པ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་དེ་ནམ་ཡང་མཚན་ཉིད་གཞན་དུ་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1942]
སྒྲོ་བཏགས་པ་མེད་པར༌[^1710]ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་སྟོང་པའི་ངོ་བོ་ལ་ཡོད་པར་སྒྲོ་གདགས་སུ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1943]
བྱ་བ་མེད་པ་ཞེས་བྱ་བ་ནི་མི་དགེ་བའི་ཆོས་རྣམས་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1944]
རྣམ་པར་བྱང་བ་མེད་པ་ཞེས་བྱ་བ་ནི། དགེ་བའི་ཆོས་ཀྱང་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1945]
མི་གནས་པ་ཞེས་བྱ་བ་ནི་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་ལ་མི་བརྟན་པའི༌[^1711]ཕྱིར་རོ། །

[Block 1946]
རབ་ཏུ་མི་གནས་པ་ཞེས་བྱ་བ་ནི། མིག་ལ་སོགས་པའི་དབང་པོ་ལ་མི་བརྟེན་པའི་ཕྱིར།[^1712] རྩ་བ་མེད་པ་ཞེས་བྱ་བ་ནི་ལས་དང་ཉོན་མོངས་པས་མ་བསྐྱེད༌[^1713]ཅིང་དེ་ལ་མི་གནས་པའི་ཕྱིར་རོ། །

[Block 1947]
ཐམས་ཅད་མཉམ་པ་ཞེས་བྱ་བ་ནི་ནམ་མཁའ་བཞིན་དུ་ཀུན་དུ་ཁྱབ་པའི་ཕྱིར་རོ། །

[Block 1948]
མཉམ་པ་དག་ལ་མཉམ་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་མཚན་ཉིད་གཅིག་པར༌[^1714]མཉམ་པ་སྟེ། མཚན་ཉིད་གཅིག༌[^1715]པར་འདུ་བས༌[^1716]ན་མཉམ་པ་ལ་མཉམ་པའོ། །

[Block 1949]
མི་མཉམ་པ་དག་ལ་མཉམ་པ་ཞེས་བྱ་བ་ནི་མི་མཉམ་པའི་ཆོས་ཀྱི་སྐུ་སྟེ་ཆོས་ཐམས་ཅད་དེ་དང་འདྲ་བས་ན་མི་མཉམ་པ་དག་ལས་མཉམ་པའོ། །

[Block 1950]
ཆོས་ཐམས་ཅད་མཚན་ཉིད་གཅིག་པར༌[^1717]འདྲ་བ་དང་། ཆོས་ཀྱི་སྐུ་དང་འདྲ་བས་ན། མཉམ་པ༌[^1718]དང་མི་མཉམ་པ་དག་ལ༌[^1719]མཉམ་པའོ། །

[Block 1951]
རྟོག་པ་ཐམས་ཅད་ལས་འདས་པས་ན་རྟོག་པ་མེད་པའོ། །

[Block 1952]
བྱ་བ་ཐམས་ཅད་ལས་འདས་པས་ན་རྩོམ་པ༌[^1720]མེད་པའོ། །

[Block 1953]
ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས་མྱ་ངན་ལས་འདས་པའི་མཚན་ཉིད་དུ་མཐོང་བས་ན། ཆོས་ཐམས་ཅད་ལ་སྐྱོན་མེད་པ་རྙེད་པའོ། །

[Block 1954]
ནམ་མཁའ་བཞིན་དུ་ངོ་བོ་མེད་པ་ཡིན་པས་ན། ཤིན་ཏུ་ནམ་མཁའ༌[^1721]རང་བཞིན་གྱི་མཚན་ཉིད་དོ། །

[Block 1955]
དེ་ལ་གང་དག་ཆོས་ཉིད་ལ་རྟོན་ཅེས༌[^1722]བྱ་བ་ནི་གང་སྟོང་པ་ཉིད་ལ་རྟོན་ཅིང་དེ་ཁོང་དུ་ཆུད་པ་དེ་དག་ནི་མིག་ལ་སོགས་པའི་ཁམས་གང་ལ་ཡང་དངོས་པོར་མི་འཛིན་ཅིང་མི་རྟོན༌[^1723]པའོ། །

[Block 1956]
ཆོས་ཉིད་ཀྱི་དོན་རྒྱས་པར་བཤད་པ་བསྡུས་ཏེ་བསྟན་པའི་ཕྱིར། དེ་བས་ན་ཆོས་ཀྱི་སྒོའི་ཚུལ་ལ་འཇུག་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཆོས་ཐམས་ཅད་ཆོས་ཀྱི་དབྱིངས་སུ་རྟོགས་པ༌[^1724]ནི་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་སྐྱེ་བའི་རྒྱུ་ཡིན་པས་ན་ཆོས་ཀྱི་སྒོ་སྟེ། ཚུལ་ལ་འཇུག་པ་ནི་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་དུ་རྟོགས༌[^1725]པའོ། །

[Block 1957]
འདིས་ཆོས་ཐམས་ཅད་ལ་རྟོན་པའི་ཕྱིར༌[^1726]ཆོས་ཐམས་ཅད་ཆོས་ཉིད་ཁོ་ནར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་མཚན་ཉིད་ཡིན་པ་འདིས་ཆོས་ཐམས་ཅད་ལ་རྟོན་པས་ཕུང་པོ་དང་ཁམས་ལ་སོགས་པའི་ཆོས་རྣམས་ཆོས་ཉིད་ཡིན་པར་འགྱུར་བའོ། །

[Block 1958]
འདི་ནི་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པ་ལྟར་ཁོང་དུ་ཆུད་པ་འདི་ནི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1959]
རྟོན་པ་བཞི་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1960 [HEADING]]
## ཡོངས་སུ་བྱང་བའི་བྱང་ཆུབ་སེམས་དཔའ། ^7-0

[Block 1961]
ཡོངས་སུ་བྱང་བའི་བྱང་ཆུབ་སེམས་དཔའ༌[^1727]བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱང་མི་ཟད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་དག་མི་ཟད་པ་ཡང་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱིས་སྤྱད་པའི༌[^1728]ཡུལ་སྦྱིན་པ་ལ་སོགས་པ་མི་ཟད་པའི་ཕྱིར་རོ། །

[Block 1962]
ཡོངས་སུ་བྱང་བའི་བྱང་ཆུབ་སེམས་དཔའ་ཡང་རྣམ་པ་གཉིས་ཏེ། རྟག་པར་ཕོངས་པ་མེད་པ་དང་། ཐེ་ཚོམ༌[^1729]ཐམས་ཅད་གཅོད་པའོ། །

[Block 1963]
ཚོགས་གཉིས་ཀྱིས་བསྡུས་པའི་དོན་ཚོགས་ཀྱི་ལམ་བསྟན་པར་ཡང་སྦྱར་རོ། །

[Block 1964]
དེ་ལ་རྟག་པ༌[^1730]ཕོངས་པ་མེད་པ་གང་ཞེ་ན།

[Block 1965 [VERSE]]
གང་གིས་བསོད་ནམས་ཀྱི་ཚོགས་བསགས་པའོ། །
ཐེ་ཚོམ༌[^1731]ཐམས་ཅད་གཅོད་པ་གང་ཞེ་ན།
གང་གིས་ཡེ་ཤེས་ཀྱི་ཚོགས་བསགས་པའོ། །
--- END BLOCKS ---
