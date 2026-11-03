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
འཚོ་ཚིས་ཀྱི་བྱ་བ་ལེགས་པར་འབྱོར་པ་ནི་ཞིང་ལས་དང་། བསྲུང་བ་དང་། ཚོང་ལ་སོགས་པ་འཚོ་ཚིས་ཞེས་བརྗོད་དོ། །

[Block 1927]
དཔའ་བ་ཕུན་སུམ་ཚོགས་པའི་རྣམ་པར་རྒྱལ་བའི་དཔལ་ཐོབ་པ་དང་ཞེས་བྱ་བ་འདིས་ནི༌[^1134]མ་ཐོབ་པ་འཐོབ་པར༌[^1135]བསྟན་ཏོ། །

[Block 1928]
རང་གི་ཆོས་དང་ལས་དང་འབད་པ་དང་ཡིད་མ་བྱུང་ཞིང་བདེ་བར་འཚོ་བ་དང་། འཚོ་ཚིས་བྱས་པ་ལེགས་པར་འབྱོར་པ་ཞེས་བྱ་བ་དག་གིས་ནི་རྣམ་པར་འཕེལ་བ་བསྟན་ཏོ། །

[Block 1929]
ཡོན་ཏན་ལྡན་པས་ཞེས་བྱ་བས་ནི་ཐོབ་པ་རྣམ་པར་སྤེལ་བ་དང་། ཡོངས་སུ་བསྲུང་བ༌[^1136]དབང་དུ་བྱས་པའོ། །

[Block 1930]
ཡོན་ཏན་དང༌[^1137]ལྡན་པས༌[^1138]ཞེས་བྱ་བའི་ཕྱེད་ཀྱིས་ནི༌[^1139]ཡོན་ཏན་དང་ལྡན་པ་དེས་རང་བཞིན་གྱིས་ཉམས་པ་མེད་པ་བསྟན་ཏེ། དེས་ན་ཡང་དེ༌[^1140]བསྲུང་བར་འགྱུར་བ་ཡིན་ཏེ། འདིས༌[^1141]ནི་གསང་ཚིག་གི་ནུས་པ་བསྟན་ཏོ། །

[Block 1931]
རང་གི་ཡུལ་འཁོར་ལ་ནི་རི་ཕུག་སེང་གེས༌[^1142]བསྲུངས་པ་ཞེས་བྱ་བའི་འོག་མ་འདིས་སྟོབས་དང་ལྡན་པས་རྒྱལ་ཕྲན་རྣམས་ཟིལ་གྱིས་གནོན་པ་ཉིད་དུ་བསྟན་ཏེ། འདིས་ནི་སྤྲོ་བའི་ནུས་པ་བསྟན་ཏོ། །

[Block 1932]
མིའི་བདག་པོའི༌[^1143]དཔལ་ཞེས་བྱ་བ་ནི༌[^1144]གཙོ་བོའི་ནུས་པ་སྟེ། མིའི་བདག་པོ་ནི་དཔལ་གྱི་སྒྲས་བརྗོད་དོ། །

[Block 1933]
ཅིའི་ཕྱིར་རིམ་པས་ཡོངས་སུ་བསྲུང་བ༌[^1145]འདི་ལྟར་སྨོས་ཤེ་ན། [^1146]གང་གི་ཕྱིར་འདི་ཉིད་ཀྱི་རིམ་པ་ནི་ཡོངས་སུ་སྤེལ་བ་དང་། བསྲུང་བ་ཡིན་པའི་ཕྱིར་རིགས་པའི་ཚུལ་ཡིན་ནོ། །

[Block 1934]
གཞན་དུ་ལུགས་ཀྱི་བསྟན་བཅོས་ལྟར་ན་ནི་རྣམ་པར་སྤེལ་བ་དང་ཡོངས་སུ་བསྲུང་བ་བཤད་པ་མེད་པར་འགྱུར་རོ། །

[Block 1935]
དཀའ་ཐུབ་རྣམས་དང་རིགས༌[^1147]དང་སྒྱུ་རྩལ་ཞེས་བྱ་བའི་ཚིགས༌[^1148]བཅད་འདིས་ནི་མུ་སྟེགས་ཀྱིས༌[^1149]རབ་ཏུ་བསྒྲུབས་པའི་དབང་དུ་བྱས་ན་དཀའ་ཐུབ་ལ་སོགས་པ་འདི༌[^1150]གསུམ་སྨོས་པ་ནི་ལུས་དང་། ངག་དང་། ཡིད་ཀྱི་ལས་ཁྱད་པར་ཅན་བཟུང་བའི༌[^1151]ཕྱིར་རོ། །

[Block 1936]
འོངས་ན་རིམ་གྲོ་ལྷག་པ༌[^1152]ཆེ་བ་ཞེས་བྱ་བ་ནི་དཀའ་ཐུབ་ལ་སོགས་པ་གསུམ་ཆེ་བར་གྱུར་པས་རིམ་གྲོ་ལྷག་པ་སྟེ། ཁྱད་པར་དུ༌[^1153]ཇི་ལྟར་འོས་པ་བཞིན་དུ་བྱེད་པར་འགྱུར་བའོ།[^1154] །བཀུར་སྟི་བྱས་ནས་ཞེས་བྱ་བས་ནི་སྦྱིན་པ་ལ་སོགས་པས་སོ། །

[Block 1937]
གཙོ་བོར་སྣང་ངོ་ཞེས་བྱ་བ་ལ་མཆོད་པས་ཕན་པ་ཁྱད་པར༌[^1155]དུ་གྱུར་པ་སྟེ། དཀའ་ཐུབ་ལ་སོགས་པའི་ཕན་པ་ཁྱད་པར༌[^1156]དུ་གྱུར་པའི་སྣང་བ་ཡིན་ནོ། །

[Block 1938]
རིམ་གྲོ་དང་བཀུར་སྟི་ཞེས་བྱ་བ་གཉིས་ཀྱིས་ནི་རྙེད་པ་དང་བཀུར་སྟི་གོ་རིམས་བཞིན་དུ་བསྟན་ཏོ། །

[Block 1939]
རྒྱལ་སྲིད་ཐོབ་མ་ཐག་ཏུ་ཞེས་བྱ་བས༌[^1157]ནི་རྒྱལ་པོའི་སྲིད་དེ། དེ༌[^1158]མ་ཐག་ཏུ༌[^1159]ནི་རྒྱལ་པོའི་སྲིད་ཐོབ་པ་ཡིན་ཏེ། རྒྱལ་པོ་དང་མཉམ་ཞིང་རྒྱལ་པོའི་སྲིད་བྱེད་པར་འོས་པའི་ཕྱིར་རོ། །

[Block 1940]
ཡོན་ཏན་མང་པོ་རྟག་ཏུ་གྲགས་པ་ཞེས་བྱ་བ་ནི༌[^1160]ཡོན་ཏན་གྱི་གྲགས་པ༌[^1161]ཐམས་ཅད་དུ་ཁྱབ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1941]
གཞོན་ཡང་རྒན་པའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་བའི་དོན་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ལ་གནས་ཀྱང་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ལ་བག་ཡོད་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ།[^1162] །གཞོན་ཡང་ཞེས་བྱ་བ་འདིས་ནི་ཚུལ་ཁྲིམས་ཀྱི༌[^1163]བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ལ་གནས་པ་བསྟན་ཏོ། །

[Block 1942]
གཞོན་པ་ཞེས་བྱ་བ་འདིས་ནི་བདག་གི་ཕུན་སུམ་ཚོགས་པའི་ཚིག་གིས་ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུ་བསྟན་པ་ཡིན་ནོ་ཞེས་རྟོགས་ཏེ། བདག་གི་ཕུན་སུམ་ཚོགས་པ་ནི་ཚུལ་ཁྲིམས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1943]
རྒན་པ་རྣམས་ཀྱི་ཉེ་བར་ཞི་བ་ཡིན་པས་རྒན་པའི་ཉེ་བར་ཞི་བའོ། །

[Block 1944]
ཡང་ན་རྒན་པ་བཞིན་དུ་ཉེ་བར་ཞི་བས་རྒན་པའི་ཉེ་བར་ཞི་བའོ། །

[Block 1945]
དེ་ལ་མངོན་པར་དགའ་བ་ནི་རྒན་པའི་ཉེ་བར་ཞི་བ་ལ་མངོན་པར་དགའ་བ་སྟེ། འདིས་ནི་ཚུལ་ཁྲིམས་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་བསགས་པ་ལ་བག་ཡོད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1946]
གཟི་བརྗིད་ཆེ་ཡང་ཞེས་བྱ་བ་འདིས་ནི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི༌[^1164]འབྲས་བུ་ལ་གནས་པ་སྟེ། བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ནི་སྐྱེ་བོ་མང་པོའི་གཡོག་འཁོར་གྱི་འབྲས་བུ་ཡིན་ཏེ། དེ་ལ་གནས་པའི་གཟི་བརྗིད་ཆེ་བ་སྟེ། གང་གི་མཐུ་ཆེ་བའི་གཟི་བརྗིད་ཆེ་བ་ཡིན་ནོ། །

[Block 1947]
བཟོད་ཅིང་བདེ་བའི་ངང་ཞེས་བྱ་བ་འདིས་ནི་བཟོད་པའི་བསོད་ནམས་ཀྱི་ཚོགས་ལ་བག་ཡོད་པ་ཉིད་དུ་བསྟན་ཏོ། །ཤེས་པར་གྱུར་ཀྱང་ཞེས་བྱ་བས་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ལ་གནས་པ་བསྟན་ཏོ། །ཤེས་པའི་ང་རྒྱལ་མེད་ཅེས་བྱ་བ་འདིས་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་བསགས་པ་ལ་བག་ཡོད་པ་ཉིད་བསྟན་ཏོ། །

[Block 1948]
གང་གི་ཕྱིར་ཤེས་པས་ང་རྒྱལ་སྐྱེ་བར་གྱུར་ན་ནི་བདག་ཉིད་ལ་བསྟོད་ཅིང་གཞན་ལ་སྨོད་པར་བྱེད་དེ། བདག་ལ་བསྟོད་ཅིང་གཞན་ལ་སྨོད་པས་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཐེག་པ་ཆེན་པོ་དག་ཏུ་ཤེས་རབ་ཉམས་པར་གསུངས་ཏེ། ཡེ་ཤེས་ཀྱི་ཚོགས་ལ་བག་ཡོད་པར་བསྟན་ཏོ། །

[Block 1949]
ཡང་ན་མཁས་པར་གྱུར་ཀྱང་ཤེས་པའི་ང་རྒྱལ་མེད་ཅེས་བྱ་བས་ནི་ཤེས་པས་ངོམས་པ་མེད་པ་བསྟན་ཏོ། །

[Block 1950]
ཡེ་ཤེས་ཀྱི་ཚོགས་ལ་ཡང་དང་ཡང་དུ་སྦྱོར་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 1951]
དཔལ་དང་ལྡན་ཞིང་འབྱོར་ཡང་ཞེས་བྱ་བས༌[^1165]ནི་སྦྱིན་པའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ལ་གནས་པ་ཉིད་དོ། །

[Block 1952]
དྲེགས་པ་མེད་ཅེས་བྱ་བ་ལ་དྲེགས་པ་ནི་དཔལ་གྱི་དྲེགས་པས་དྲེགས་པ་ཉིད་དེ། དེ་བས་ན་དྲགས་པ་དེས་འཇུག་ན་ནི་སྦྱིན་པའི་བསོད་ནམས་ཀྱི་ཚོགས་སོགས་པ་ལ་འཇུག་པར་མི་འགྱུར་རོ། །

[Block 1953]
དྲེགས་པ་མེད་པ་ལ་ཡང་འཇུག་པ་ཡིན་ཏེ། རྒྱ་ཆེ་མཐོང་གྱུར་ཞེས་བྱ་བ་འདི་དང་སྦྱར་བར་བྱའོ། །

[Block 1954]
གཞོན་ཡང་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་འདི་ལ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་དང་། འཇིག་རྟེན་གསུམ་དུ༌[^1166]རབ་ཏུ་ལྡན་པ་རྒྱུ་དང་འབྲས་བུའི་གནས་སྐབས་སུ་བསྟན་པ་དེ་གཉི་གའི་ཡོན་ཏན་ལྡན་པ་དེས་གྲགས་པའི་ཁྱད་པར་གྱིས་ཁྱབ་པ་ཡིན་ནོ། །

[Block 1955]
མཐོང་བར་འགྱུར་པ་ནི་རིགས༌[^1167]པའོ། །

[Block 1956]
རྒྱ་ཆེ་བ་ནི་ཡངས་པའི༌[^1168]ཕྱོགས་གང་ཡིན་པ་མཐོང་བ་སྟེ་རྒྱ་ཆེན་མཐོང་གྱུར་པའོ། །

[Block 1957]
ཁྱབ་པ་ནི་མཐའ་ཡས་པར་གྲགས་པས་ཁྱབ་པར་བསྟན་ཏོ། །

[Block 1958]
འཇིག་རྟེན་གསུམ་ནི་སའི་སྟེང་དང་། ནམ་མཁའ་དང་། མཐོ་རིས་ཏེ།

[Block 1959 [VERSE]]
སྟེང་དུ་གྲགས་པ་འཇུག་པར་བསྟན་ཏོ། །
དེ་ཡི་གྲགས་པས་འཇིག་རྟེན་གསུམ་ཁྱབ་པས། །

[Block 1960]
ཞེས་བྱ་བ་འདིས་ནི་གྲགས་པ་ཅུང་ཟད་ཡོད་པ་ཞེས་སྨོས་ཏེ། ཤིན་ཏུ་ཆུང་བ་མངོན་པར་བཟུང་བའི༌[^1169]ཕྱིར་ཏེ། དེ་ལས་གཞན་པའི་ཡོན་ཏན་ནི་ཅུང་ཟད་ཉིད་དེ། སྦྱིན་པའི་མདའ་རྣམས་ཆར་བཞིན་འབེབས་པ་ཞེས་བྱ་བས༌[^1170]ནི་སྦྱིན་པའི་མདའ་ཉིད་དེ། དབུལ་བའི་སྡུག་བསྔལ་འབྱུང་བ་རྣམ་པར་འཇིག་པའོ། །

[Block 1961]
སྙིང་རྗེའི་གཞུ་དྲག་པ༌[^1171]ཉིད་ཀྱིས་ནི་སྦྱིན་པ་འཕེན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1962]
དེ་དང༌[^1172]ཞེས་བྱ་བ་ནི་འགྲོ་བ་རྣམས་ཀྱི་དབུལ་བའི་སྡུག་བསྔལ་འབྱུང་བ་དང་ངོ་། །བསླང་ས་པ་བས་ལྷག་པ་ནི་འདོད་པས༌[^1173]ལྷག་པ་སྟེ་འདིས་ནི་སྦྱིན་པའི་དངོས་པོ་མང་དུ་གཏོང་བར་བསྟན་ཏོ། །

[Block 1963]
ཉོན་མ༌[^1174]མོངས་པར་ཞེས་བྱ་བ་འདིས་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པར་བསྟན་ཏེ། བདག་ནི༌[^1175]འཁོར་བའི་ཕུན་སུམ་ཚོགས་པའི་བདག་ཉིད་མྱ་ངན་ལས་འདས་པར་ཡོངས་སུ་བསྔོ་བས་སོ། །

[Block 1964]
ཚིག་འཇམ་པོ་དང་། གུས་པ་དང་ཡིད་དུ་འོང་བ་ཞེས་བྱ་བས༌[^1176]ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ལུས་དང་ངག་གི་ལས་ཀྱིས་སློང་བ་རྣམས་ཀྱི་ཡིད་དུ་འོང་བའི་ཕྱིར་རོ། །

[Block 1965]
འདིས་ནི་འདས་པའི་དུས་སུ་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསགས་པ་བསྟན་ཏོ། །
--- END BLOCKS ---
