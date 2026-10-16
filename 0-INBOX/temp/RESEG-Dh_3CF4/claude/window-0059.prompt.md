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
རང་གི་ལུས་ཀྱང་ཞེས་བྱ་བ་ནི་བསྟན་མ་ཐག་པར་བཤད་པ་སྟོན་ཏོ། །

[Block 2067]
རང་གི་མིག་དང་མགོ་ཡང་ངས་སྦྱིན་ན། །ཞེས་བྱ་བ་འདིས་ནི། སྐྲག་པར་བྱས་ན༌[^1270]མི་སྦྱིན་ཞེས་སྨོས་ཏེ། ཕྱི་རོལ་གྱི་དངོས་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2068]
གང་སྔར་བསྟན་པའི་རང་གི་བསྟན་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་ཕྱིར་ཞེས་བྱ་བ་དེའི་དབང་དུ་བྱས་པ་ནི། ཤི་བི་པ་རྣམས་ཐམས་ཅད་ཀྱིས༌[^1271]ཞེས་བྱ་བ༌[^1272]སྨོས་སོ། །

[Block 2069]
ངེས་པ་ནི་བསྐྲད་པར་འདོད་པ༌[^1273]ངེས་པར་བྱས་པའོ། །

[Block 2070]
ཅི་ཐོབ་དང་ཞེས་བྱ་བ་ནི་དེ་ཉིད་ངེས་པར་བྱས་པའི་ཕྱིར་ང་ལས་ཐོབ་པའི་ནོར་ཅི་ཡོད་པའོ། །

[Block 2071]
ཕའི་ནོར་རྣམས་ཞེས་བྱ་བ་ནི་གཉི་ག་བཟུང༌[^1274]སྟེ། གྱོས་པོའི་ནོར་བཟུང༌[^1275]ཚུལ་ཁྲིམས་ལྡན་པ་ཞེས་བྱ་བ་ནི་ལེན་པ་པོ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 2072]
རྟག་པར་བྱིན་པ༌[^1276]ཞེས་བྱ་བ་ནི་རྟག་ཏུ་སྦྱིན་པར་བྱེད་པའོ། །

[Block 2073]
བཀུར་སྟིས་བརྒྱན་པ་སྦྱིན་ཞེས་བྱ་བ་ནི་གུས་པར་བྱིན༌[^1277]པའོ། །

[Block 2074]
སྦྱིན་པར་བྱེད་པ་ཡིན་པས་སྦྱིན་པ་སྟེ། སྦྱིན་པའི་དངོས་པོའོ། །

[Block 2075]
དབྲོག་ཏུ་མེད་ཅེས་བྱ་བ་ནི་སྔ་མ༌[^1278]དང་ཐུན་མོང་དུ་གྱུར་པའི་ནོར་ལས་ཁྱད་པར་དུ་གྱུར་པ་བསྟན་ཏོ། །

[Block 2076]
རྗེས་སུ་འགྲོ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་རྣམ་པ་ནི་བོར་ནས་འགྲོ་བ་ཡིན་པས་དེའི་མི་མཐུན་པའི་ཕྱོགས་བསྟན་ཏོ། །

[Block 2077]
གྱོས་སྒྱུག་གཉིས་ཞེས་བྱ་བ་ནི་གྱོས་པོ་དང་སྒྱུག་མོ་ནི་གྱོས་སྒྱུག་གཉིས་སོ། །

[Block 2078]
བུ་དང་བུ་མོ་ནི༌[^1279]བུས་པ་གཉིས་སོ། །

[Block 2079]
གྱོས་སྒྱུག་གཉིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི༌[^1280]ནོར་གྱི་སྒྲུབ་པ་དང་། ཆོས་ཀྱི་སྒྲུབ་པ་བསྟན་ཏེ།[^1281] དང་པོའི་ཕྱེད་ཀྱིས་ནི་ནོར་གྱི་སྒྲུབ་པ༌[^1282]སྟེ།

[Block 2080 [VERSE]]
དེ་ཉིད་ནི་འཇིག་རྟེན་འདི་སྒྲུབ་པའོ། །
ཆོས་ལ་གཅིག་ཏུ་བག་ཡོད་བྱོས། །

[Block 2081]
ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་སྒྲུབ་པ་སྟེ། དེ་ཉིད་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་སྒྲུབ༌[^1283]པའོ། །

[Block 2082]
འདི་ནི་འབྲལ་བ་དང་འདུ་བ་ལས་བརྩམས་ཏེ། ང་མེད་མྱ་ངན་མ་བྱེད་ཅིག །[^1284]ཅེས་སྨོས་སོ། །

[Block 2083]
དེ་ཐོས་ནས་ཞེས་བྱ་བ་ནི་འབྲལ་བར་བྱ་བ་བསྟན་པའོ། །

[Block 2084]
སྙིང༌[^1285]རབ་ཏུ་གདུངས་ཀྱང་ཞེས་བྱ་བ་ནི་ཐོས་པས་ཡིད་རབ་ཏུ་གདུངས་པར་གྱུར་ཀྱང་ངོ་། །ཆོས་མ་མཆིས་ཞེས་བྱ་བ་ནི་ཆུང་མ་བོར་ནས་དཀའ་ཐུབ་ཀྱི་ནགས་སུ་གཤེགས་པའོ། །

[Block 2085]
དེ་བས་ཞེས་བྱ་བ་ནི་གཅིག་པུ་གཤེགས་པའི་ཆོས་མེད་པས་སོ། །

[Block 2086]
ངེས་པར་ནགས་སུ་གནས་པ་ཉིད་ནི་སྡུག་བསྔལ་བ་ཡིན་ནོ་ཞེས་ཤེས་ཤིང་ཆོས་མ་ཡིན་པ་ཉིད་དེ། གཅིག་པུ་ནགས་སུ་འགྲོ་ཞིང་བདག་སྤངས་ནས་གང་དུ་འགྲོ་བར་བྱེད་པའོ༌[^1286]ཞེས་རྟོགས༌[^1287]པའོ། །

[Block 2087]
མི་སྲུན་མི་བྱེད་ཤིང་དང་ཞེས་བྱ་བ་འདིའི་བསྡུས་པའི་དོན་ནི་སྐྱེད་མོས་ཚལ་བས་ཀྱང་ལྷག་པར་དཀའ་ཐུབ་ཀྱི་ནགས་བདེ་བ་སྟེ། ཡོན་ཏན་གང་གིས་སྐྱེད་མོས་ཚལ་བས་དཀའ་ཐུབ་ཀྱི་ནགས་ལྷག་པ་ཡིན་ཞེ་ན། སྐྱེད་མོས་ཚལ་ནི་མི་སྲུན་པའི་སྐྱེ་བོའི་གནོད་པ་ཡོད་ལ་དཀའ་ཐུབ་ཀྱི་ནགས་ན༌[^1288]ནི་དེ་མེད་དེ་ཤིང་དང་ཆུ་ལ་སྤྱོད་པའི་ཕྱིར་རོ། །

[Block 2088]
སྐྱེད་མོས་ཚལ་ནི་མི་གཙང་བ་ཡིན་ལ་དེ་མེད་པས་ན་གཙང་བའོ། །

[Block 2089]
སྐྱེད་མོས་ཚལ་ནི་སྐྱེ་བོའི་སྒྲ་དང་ལྡན་ལ། དཀའ་ཐུབ་ཀྱི་ནགས་ན་ནི་བྱ་རྣམས་སྐད་སྣ་ཚོགས་འབྱིན་པ་ཡིན་ནོ། །

[Block 2090]
སྐྱེད་མོས་ཚལ་ན༌[^1289]ནི་མི་ལ་སོགས་པའི་གནོད་པ་ཡོད་པ་ཡིན་ལ། དཀའ་ཐུབ་ཀྱི་ནགས་ན་ནི་རི་དགས་མང་བ་ཡིན་ནོ། །

[Block 2091]
སྐྱེ་བོ་རྒྱུ་བས་བརྫིས༌[^1290]པའི་ནེའུ་གསིང༌[^1291]ནི་རེག་ན་སྡུག་བསྔལ་བ་ཡིན་ལ། དཀའ་ཐུབ་ཀྱི་ནགས་ན་ནི་ས་གཞི་བཻ་ཌཱུརྱ་ལྟ་བུའི་རང་བཞིན་ནེའུ་གསིང༌[^1292]སྔོན་པོ་ཡིད་དུ་འོང་བ་དང་སྐྱེ་བོ་རྒྱུ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2092]
འདིས་ནི་བདག་ཉིད་ཀྱི༌[^1293]སྡུག་བསྔལ་མེད་པ་བསྟན་ནས། ད༌[^1294]ནི་བྱང་ཆུབ་སེམས་དཔའ་ནགས་ན་གནས་པ་ལ་སྡུག་བསྔལ་མེད་པ་ཉིད་དུ་བསྟན་པའི་ཚིགས་བཅད་དྲུག་གིས་སྤྲོ་བ་བསྐྱེད་པ་ཡིན་ནོ། །

[Block 2093]
ནགས་ཚལ་ལྕུག་མའི༌[^1295]ཁྲོད་དག་ན། །ཞེས་བྱ་བ་འདིས་ནི་གཡོག་འཁོར་ཕུན་སུམ་ཚོགས་པ་ལས་བརྩམས་ཏེ། རྒྱལ་སྲིད་ཡོངས་སུ་སྤངས་ཀྱང་སྡུག་བསྔལ་མེད་ཅིང་རྒྱལ་སྲིད་དྲན་པར་མི་འགྱུར་བ་ཡིན་ཏེ། རྒྱལ་སྲིད་ནི་གཡོག་འཁོར་གྱི་རྣམ་པའི་ཕྱིར་ཏེ། གཡོག་འཁོར་ཕུན་སུམ་ཚོགས་པ་དེས་དྲན་པར་མི་འགྱུར་བའོ། །

[Block 2094 [VERSE]]
གཞོན་ནུ་མ་དང་གཞོན་ནུ་ནི་གཞོན་ནུ༌[^1296]གཉིས་སོ། །
ནགས་ལ་སྡུག་བསྔལ་མེད་པའི་དབང་དུ་བྱས་ནས།
དུས་ཀྱི་དབང་གིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2095]
གླུ་དང་གར་དང་རོལ་མོའི་དབང་དུ་བྱས་ཏེ་གསུམ་ཡོངས་སུ་སྤངས་ཀྱང་ཁྱད་པར་དུ་གྱུར་པ་གསུམ་ཡོད་དོ་ཞེས་བསྟན་པའི་ཕྱིར། དགའ་བ་འཚལ༌[^1297]བའི་བྱ་རྣམས་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2096]
གང་གི༌[^1298]གནས་མལ་ཡོངས་སུ་སྤངས་ཀྱང་ཁྱད་པར་དུ་གྱུར་པའི་གནས་མལ་ཡོད་དོ་ཞེས་བསྟན་པའི་དབང་དུ་བྱས་ནས། ནགས་ཚལ་དག་ན་མཚན་མོའི་ཟླ་འོད་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རེག་པ༌[^1299]དང་དྲི་ཞིམ་པ་ཕུན་སུམ་ཚོགས་པའི་གནས་སུ་ཚིགས་བཅད་འདི་གཉིས་ཀྱིས་གོ་རིམས་བཞིན་དུ་བསྟན་ཏོ། །

[Block 2097]
མྱ་ངན་གྱིས་གདུངས་པའི་ཤུགས་ཞེས་བྱ་བ་ལ། མྱ་ངན་དང་གདུངས་པ་གཉིས་ནི་གོང་དུ་བཤད་པའི་དོན་གྱི་རྗེས་སུ་རྟོགས་པར༌[^1300]བྱའོ། །

[Block 2098]
བརྒྱལ་བ་བཞིན་དུ་གྱུར་ཞེས་བྱ་བ་ནི་བརྒྱལ་བར་གྱུར་པ་དང་འདྲ་བ་སྟེ། དྲན་པ་མེད་པར་གྱུར་པ་ལས་ཕྱིས་ཡང་དྲན་པ་དང་ལྡན་པའོ། །

[Block 2099]
སྨྱོ་བླ༌[^1301]ཅན་དུ་གྱུར་པ་ཡིན། །[^1302]ཞེས་བྱ་བ་ནི་སེམས་རྣམ་པར་འཁྲུགས་པ༌[^1303]ཐོབ་པའོ། །

[Block 2100]
གྲིབ་ཤིང་ལྟ་བུ་ནི་བྱང་ཆུབ་སེམས་དཔའ་སྟེ། ཕོངས་པའི་ཚ་བས་མངོན་པར་གདུངས་ཤིང་འཁོར་བའི་འབྲོག་དགོན་པར་ཡུན་རིང་པོར༌[^1304]ཡོངས་སུ་དུབ་པའི་སེམས་ཅན་རྣམས་ཀྱི་སྡུག་བསྔལ་སེལ་བའི་ཕྱིར་ཏེ། བཞིན་ཁྲོ་གཉེར་མེད་པ་དང་ཚིག་གི༌[^1305]ལན་ལ་སོགས་པས་སོ། །

[Block 2101]
འབྲས་བུ་ཞིམ་པོ་ཡོད་པ་ཞེས་བྱ་བ་ནི་གུས་པར་བྱེད་པས་ཇི་ལྟར་བསམས་པའི་འདོད་པའི་དོན་སྟེར་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2102]
ཤིང་ལྟ་བུ་ནི་གཞན་གྱི་དོན་བྱེད་པ་དང་། དེའི་འབྲས་བུ་ལ་འཇུག་པའོ། །

[Block 2103]
སྟ་རིས་གཟས་པ༌[^1306]རྣམས་འཛིན་པ་ནི་ཞེས་བྱ་བ་ནི་འཛིན་པར་བྱེད་པའི་འབྲས་བུ་སེམས་པའོ། །

[Block 2104]
ཆུ་གཙང་ཞིམ་པོ་བསིལ་བའི་རྫིང་བུ་ཞེས་བྱ་བ་ནི་མཚོ་ལ་སོགས་པ་གང་འཐུངས་ན་བསིལ་བ་དང་། དྲི་མ༌[^1307]མེད་པ་དང་། ཆུ་ཞིམ་པའི་ཆུས་གང་བ་ཡིན་པ་དང་། [^1308]བསིལ་བ་ནི་དབུལ་བའི་སྡུག་བསྔལ་སེལ་བའི་ཕྱིར་རོ། །

[Block 2105]
དྲི་མ་མེད་པ་ནི་ཉོན་མོངས་པ་མེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
