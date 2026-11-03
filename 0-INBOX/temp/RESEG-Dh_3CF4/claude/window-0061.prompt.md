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
[Block 2136]
རང་གི་ནུས་པའི་ཁྱད་པར་ཉིད་མ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར་མཚོའི་ནང་ན་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 2137]
སྐར་མ་རྣམས་ཀྱི་གཟུགས་བརྙན་ནི་སྐར་མ་རྣམས་ཀྱི༌[^1333]གཟུགས་བརྙན་ནོ། །

[Block 2138]
དེས་མཛེས་པའི་སྐར་མའི་གཟུགས་བརྙན་རྣམས་ལྷག་པར་མཛེས་པ་སྟེ། ཀུ་མུ་ཏ་རྒྱས་པ་དང་འདྲ་བའི་མཚོའི་ནང་ནས༌[^1334]སྐར་མའི་གཟུགས་བརྙན་དེ་དག་ལའོ། །

[Block 2139]
ཀུ་མུ་ཏ་རྣམ་པར་དག་པས་ནི་ལྷག་པར་སྐར་མའི་གཟུགས་བརྙན་མཛེས་པ་ཡིན་གྱི་གཞན་དུ་ནི་མ་ཡིན་ཏེ། འདིས་ནི་ཀུ་མུ་ཏ་ཁ་འབྱེད་པ་དག་ཙམ་འདིར་ནི༌[^1335]བརྗོད་ལ་གཞན་གྱི༌[^1336]རྒྱན་གྱི་དོན་དུ་བསྟན་ཏོ། །

[Block 2140]
ཟླ་བའི་འོད་ཟེར་ལྟད་མོ་ལྟ་བ་བཞིན་ཞེས་བྱ་བ་འདིས་ནི་མཚོའི་ནང་ན་སྐར་མའི་གཟུགས་བརྙན་རྣམས་ཀུ་མུ་ཏ་རྒྱས་པ་མཐོང་ན་ལྷག་པར་ལྟད་མོ་ལྟ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 2141]
རྒྱུར་གྱུར་པ༌[^1337]ཞེས་བྱ་བ་ནི་མཚན་མ་ཙམ་དུ་གྱུར་པ་སྟེ། ཟླ་བས་ཁ་འབྱེད་པར་བྱས་པ༌[^1338]ནི་ཟླ་བ་འཆར་བའི་དུས་སུ་དེ་ཁ་འབྱེད་པར་སྣང་བའི་ཕྱིར་ཏེ། གལ་ཏེ་ཁ་འབྱེད་པའི་ནུས་པ་ཡོད་པར་གྱུར་ན་ནི་པདྨ་ལ་སོགས་པ་ཅིའི་ཕྱིར་ཁ་འབྱེད་པར་མི་བྱེད། དེ་བཞིན་དུ་བདག་གིས་བསམས་ན་རྒྱལ་པོ་ཁྱོད་ཀྱི་མཐུ་སྟོབས་ཡིན་སྙམ་ན། [^1339]རི་དྭགས་ཀྱི་མཆོག་དག༌[^1340]ནི་ཐམས་ཅད་དུ་མཉམ༌[^1341]པར་རབ་ཏུ་གནས་པ་དང་བཅས་པ་ཡིན་བའི་ཕྱིར་ཁྱེད་ཉིད་ཀྱིའོ། །

[Block 2142]
གཅིག་ལ་གཅིག་སྙན་པར་སྨྲ་ཞིང་ཞེས་བྱ་བ་ལ། རེ་ཞིག་རིགས་པ༌[^1342]ནི་མད་དྲིས་བྱང་ཆུབ་སེམས་དཔའ་ལ་རིགས་ཀྱི་བྱང་ཆུབ་སེམས་དཔའ་ནི་དེ་ལ་སྙན་པར་སྨྲ་བ་མ་ཡིན་ནོ། །

[Block 2143]
གློ་བུར་དུ༌[^1343]འོངས་པ་ལ་བྱམས་པ་ཞེས་བྱ་བ་འདིས་ནི་གློ་བུར་དུ་འོངས་པ་ཡིད་ལ་བྱེད་པ་བསྟན་ཏེ། གཅིག་ལ་གཅིག་སྙན་པར་སྨྲ་བའོ། །

[Block 2144]
བུ་སྨད་ཅེས་བྱ་བ་ནི་མད་དྲི་དང་གཞོན་ནུ་གཉིས་སོ། །

[Block 2145]
ཕབ་ནས་ནི༌[^1344]བབས་སུ་བཅུག་པའོ། །

[Block 2146]
རྒྱབ་ཏུ་ཞེས་བྱ་བ་འདིས་ནི་འགྲོ་བ་ལ་སྐྱོབ་པ་ཉིད་དུ་བསྟན་ཏོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ནི་འདི་ལྟར་ཁ་ཟས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 2147]
མངོན་དུ་ལྟ་བྱེད་ཅིང་ཞེས་བྱ་བ་ནི་དོན་དུ་གཉེར་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2148]
ཟེ་བ་རྣམས་ཀྱི་རྡུལ༌[^1345]དེ་སྟེ་དེ་ལྷགས་པས༌[^1346]ཁྱབ་ཅིང་གསལ་བར་གྱུར་པའི་སེར་པོ་གང་ཡིན་པ་དེ་ནི་ཟེ་བ་ལྷགས་པས་སེར་པོར་གསལ་བར་གྱུར་པའོ། །

[Block 2149]
ཉི་མའི་འོད་ཟེར་གྱིས་གདུངས་པའི་སྡུག་བསྔལ་གྱིས་འཇིགས་པ་མེད་པའི་དབང་དུ་བྱས་ནས། སྤྲིན་རྣམས་ཀྱིས་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། དེའི་ཕྱེད་ཀྱིས་ནི་ལམ་གྱིས་ཡོངས་སུ་དུབ་པའི་སྡུག་བསྔལ་མེད་པའི་དབང་དུ་བྱས་པས་སོ།[^1347] །ངལ་བའི་སྡུག་བསྔལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་མི༌[^1348]འཆག་པའི་འཇིག་པ་མེད་ཅིང་བདེ་བའོ། །

[Block 2150]
འཆག་པ་ཉིད་རྣམ་པར་འཇིག་པ་ཡིན་པས་འཆག་པ་རྣམ་པར་འཇིག་པའོ། །

[Block 2151]
དེ་ཉིད་བདེ་བ་ཡིན་པས་འཆག་པ་རྣམ་པར་འཇིག་པའི་བདེ་བའོ། །

[Block 2152]
ལམ་གྱིས་དུབ་པ་དེའི་སྡུག་བསྔལ་གྱི་ཚོར་བ་ནི་ལམ་དུ་འགྲོ་བའི་སྡུག་བསྔལ་གྱི་ཚོར་བ་སྟེ་དེས་སོ། །

[Block 2153]
མེ་ཏོག་དང་། འབྲས་བུ་དང་། ལོ་མས་བརྒྱན་པའི་ཤིང་ལྗོན་པ་ནི་ཤིང་ལྗོན་པའོ། །

[Block 2154]
སྣུམ་པ་ཡང་ཡིན་ལ་རྣམ་པ་སྣ་ཚོགས་པ་ཡིན་པས་སྣུམ་སྣུམ་ལྟར་འདུག་པ་རྣམ་པ་དུ་མའི་ཤིང་ལྗོན་པ་སྟེ། མེ་ཏོག་དང་། འབྲས་བུ་དང་། ལོ་མ་རྣམས་ཀྱིས་བརྒྱན་པའི་ཤིང་ལྗོན་པ་སྣུམ་སྣུམ་ལྟར་འདུག་པ་རྣམ་པ་དུ་མའོ། །

[Block 2155]
གང་བ་ནི་མེ་ཏོག་དང་། འབྲས་བུ་དང་། ལོ་མ་རྣམས་ཀྱིས་བརྒྱན་པའི་ཤིང་ལྗོན་པ་སྣུམ་སྣུམ་ལྟར་འདུག་པ་དུ་མས་གང་བ་སྟེ་སེམས་མེད་པའི་དགའ་བའོ། །

[Block 2156]
འདོད་པས་མྱོང་བའི༌[^1349]དགའ་བ་ཡང་ཡིན་ལ་བྱ་ཡང་ཡིན་པས་འདོད་པས་དགའ་བའི་བྱའོ། །

[Block 2157]
དུ་མའི་སྒྲ་ནི༌[^1350]མང་པོའི་སྒྲའོ། །

[Block 2158]
དེ་དག་གི་སྒྲོགས་པ་ནི་མང་པོའི་སྒྲ་འབྱིན་པར་རོ། །

[Block 2159]
འདོད་པས་མྱོས་ཤིང་རབ་ཏུ་དགའ་བ་མང་པོ་སྒྲ་འབྱིན་པའི་དཀའ་ཐུབ་ཀྱི་ནགས་ཚལ་གང་ལ༌[^1351]ཡོད་པ་དེ་ནི་བྱ་མང་པོ་འདོད་པས་མྱོས་ཤིང་དགའ་བས་སྒྲ་འབྱིན་པའི་དཀའ་ཐུབ་ཀྱི་ནགས་ཚལ་ལོ། །

[Block 2160]
གང་དུ་རི་དགས་ཀྱི་རྣམ་པ་དུ་མ་རྒྱུ་བ་དེ་ནི་རི་དགས་ཀྱི་རིགས་རྣམ་པ་དུ་མ་རྒྱུ་བའོ། །

[Block 2161]
གར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་གར་བྱེད་པ་ཉིད་དོ། །

[Block 2162]
གར་བྱེད་པ་ཉིད་རྨ་བྱ་ཡིན་པས་རྨ་བྱ་མང་པོ་གར་བྱེད་པ་སྟེ་དེས་མཛེས་པའོ། །

[Block 2163]
མེ་ཏོག་གི་དྲིས་བསྒོས་པ༌[^1352]ནི་མེ་ཏོག་གི་དྲིས་བསྒོས་པའོ། །

[Block 2164]
དཀའ་ཐུབ་ཀྱི་ནགས་ཚལ་གང་དུ་མེ་ཏོག་གི་དྲིས་བསྒོས་པའི་སེར་བུ་ལྡང་བ་དང་ལྡན་པ་དེ་ནི་ལམ་གྱི་རྡུལ་གྱིས་རྐང་པ་དང་བྱིན་པ་རྩུབ་རྩུབ་ལྟར་འདུག་པའོ། །

[Block 2165]
ངལ་བས་ཉམས་པའི་མདོག་དང་མིག་རྩ་གང་ཡིན་པ་དེ་ནི་ངལ་བས་བཞིན་མདོག་དང་མིག་རྩ་ཉམས་པའོ། །

[Block 2166]
དབྱིག་པ༌[^1353]ལ་བཏགས༌[^1354]ཤིང་ཕྲག་པ་ལ་ཐོགས་པའི་སྤྱི་བླུགས་གང་ཡིན་པ་དེ་ནི་སྤྱི་བླུགས་དབྱིག་པ༌[^1355]ལ་བཏགས་པ་ཕྲག་པ་ལ་ཐོགས་པའོ། །

[Block 2167]
གློ་བུར༌[^1356]དུ་འོངས་པ་ལ་བཀུར་སྟིའི་བྱ་བ་བྱས་པ་གང་ཡིན་པ་དེ་ནི་གློ་བུར༌[^1357]དུ་འོངས་པ་ལ་བཀུར་སྟིའི་བྱ་བ་བྱས་སོ།[^1358] །འགྲོ་བ་འདི་དག་ནི་ཞེས་བྱ་བ་ནི་མི་བཟད་པ་སྟེ། མི་བཟད་པའི་སེམས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2168]
སེར་སྣའི་མོས་པ༌[^1359]ཡིན་པས་སེར་སྣས་བསྒྲིབས་པའི་འགྲོ་བའོ། །

[Block 2169]
འདི་གཉིས་ནི་སེམས་མི་བཟད་པའི་ཕྱིར་འཇིག་རྟེན་སྣང་བ་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2170]
གཞན་དུ་ཞེས་བྱ་བ་ནི་ཁྱེད་ལས་གཞན་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2171]
སློང་བ་ཉིད་ནི་སློང་བའོ། །

[Block 2172]
སློང་བ་ཉིད་ཀྱི་ཚིག་ཡིན་པས་སློང་བའི་ཚིག་སྟེ། དོན་དུ་གཉེར་བའི་ཚིག་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2173]
མ་ཕྱིན་པ་ནི་མི་ནུས་པ་ཞེས་བྱ་བའི་དོན་ཏེ། སྣང་བ་མེད་པ་དང་། མི་མཉམ་པའི་འཇིག་རྟེན་པའོ། །གང་ལས་ཤེ་ན། མི་མཉམ་པའི་ལམ་ལས་འཇིག་རྟེན་འགྲོ་བ་ཉིད་དུ་སྣང་བའི་ཕྱིར་ཏེ། གཞན་ནི་མི་འགྲོ་བ་ཡིན་ནོ་ཞེས་དོན་གྱིས་རྟོགས་པའོ།[^1360] །དེ་བས་ན་བསྟན་པའི་སྐྱོན་གཉིས་མེད་དེ། མཐོང་བཞིན་དུ་ལམ་མཉམ་པ་ནས་འགྲོ་བར་སྣང་བའི་ཕྱིར་ཁྱོད་ཉིད་ལ་ཕྱིན་པ་ཡིན་ལ། གཞན་པ་མི་སློང༌[^1361]བའི་ཚིག་ཕྱིན་པ་མ་ཡིན་ནོ་ཞེས་སྦྱར༌[^1362]རོ། །

[Block 2174]
དེའི་རྒྱུ་སྐྱོན་གཉིས་དང་བྲལ་བ་མེད་ན་ནི་དེ་ཇི་ལྟར་སློང་བའི་དབང་དུ་བྱས་ནས། སྦྱིན་པ་ལ་དཔའ་བའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 2175]
དེའི་ཕྱིར་ཞེས་བྱ་བ་ནི་གྲགས་པ་ཐོས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
