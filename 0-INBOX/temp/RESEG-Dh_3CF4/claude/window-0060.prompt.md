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

[Block 2106]
ཞི་བ་ནི་གུས་པར་བྱེད་པའི་སྦྱོར་བ་ལ་སོགས་པའི༌[^1309]ཁྱད་པར་ཅན་གྱིས་ཡིད་དུ་འོང་བའི་ཕྱིར་རོ། །

[Block 2107]
འདྲལ་བ༌[^1310]དག་ཅེས་བྱ་བ་ནི་འཇིག་པ་འདོད་ཅིང་དབུལ་བ་བཟློག༌[^1311]པའོ། །

[Block 2108]
མིང་ལ་ནི་དོན་མེད༌[^1312]ཅེས་བྱ་བ་ནི་འདི་དག་དོན་དང་ལྡན་པ་མ་ཡིན་ཏེ་འདོད་དགའི་མིང་ངོ་། །ཡང་ན་དོན་དང་ལྡན་པ་ཡིན་དུ༌[^1313]ཟིན་ཀྱང་འོན་ཀྱང་གུད་དུ་སོང་བ་ཞེས་སྨོས་ཏེ། ཡུལ་ཕྱོགས་གཞན་དུ་སོང་ཞིང་ཉེ་བ་དག་ན༌[^1314]མི་གནས་པའོ། །

[Block 2109]
ཡང་ན་གྲགས་པ་ཟད་ཅེས་བྱ་བ་སྨས༌[^1315]ཏེ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2110]
གྲིབ་ཤིང་འབྲས་བུ་ཞིམ་པོ་ཡོད་པ་དག་དང་དྲི་མ་མེད་པ་དང་། གཙང་ཞིང་ཞིམ་པའི་ཆུས་གང་བའི་རྫིང་བུ་ཞེས་སྨོས་པས་ནི་ངལ་བསོ་བའི༌[^1316]གནས་དང་། བཟའ་བ་དང་བཏུང་བའི་སྡུག་བསྔལ་གསོ་བའི་ཐུན་མོང་གི་རྒྱུར་གྱུར་པ་དེ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་ཡང་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཐུན་མོང་གི༌[^1317]དགོས་པ་ཡིན་ཏེ། གྲིབ་ཤིང་དང་རྫིང་བུ་ལྟ་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2111]
དེ་ལྟར་རེ་ཞིག་འབྲས་བུ་ཞིམ་པོ་ཡོད་པ་ཞེས་བྱ་བ་དང་། ཆུ་གཙང་ཞིམ་པོ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་གཉིས་ཀྱིས་ནི་བྱང་ཆུབ་སེམས་དཔའི་བསྐྲད་པའི་སྒོ་ནས་བདག་གི༌[^1318]སྡུག་བསྔལ་ལས་བརྩམས་ཏེ་སྨྲེ་སྔགས་འདོན་པ་བསྟན་ཏོ། །

[Block 2112]
གང་ན་རྒྱལ་པོ་ཐམས་ཅད་སྒྲོལ་ཞེས་བྱ་བ་འདིས་ནི་བྱང་ཆུབ་སེམས་དཔའ་སྤྱུགས་པའི་དབང་དུ་བྱས་ནས་སྨྲེ་སྔགས་འདོན་པ་བསྟན་ཏོ། །

[Block 2113]
བདག་ཅག་ཕོངས་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་བདག་ཉིད་སྡུག་བསྔལ་ལས་བརྩམས་སོ། །

[Block 2114]
ནོར་བུ་རིན་པོ་ཆེ་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཐ་སྙད་ཀྱི་དངོས་པོའི་དབང་དུ་བྱས་པའོ། །

[Block 2115]
ནོར་དང་འབྲུ་མང་པོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཉེ་བར་དོགས་པའི་དངོས་པོ་བཟུང་བའོ། །

[Block 2116]
ཉེ་འཁོར་སྐྱེད་མོས་ཚལ་བཟང་པོ་ཡིད་དུ་འོང་བ་གང་ཡིན་པ་དེ་ནི་ཉེ་འཁོར་སྐྱེད་མོས་ཚལ་བཟང་པོ་ཡིད་དུ་འོང་བའོ། །

[Block 2117]
མཐར་གྱིས་ཞེས་བྱ་བ་ནི་གྲོང་ཁྱེར་གྱི༌[^1319]མཆོག་ལས་སོ། །

[Block 2118]
འདས་པ་འདི༌[^1320]རིམ་གྱིས་ཞེས་བྱ་བའི་དོན་ཏེ། གྲོང་དང་གྲོང་ཁྱེར་ལས་འདས་པའོ། །

[Block 2119]
གྲིབ་ཤིང་བར་མཚམས་མེད་པའི་དགོན་པ་གང་ཡིན་པ་དེ་ནི་གྲིབ་ཤིང་བར་མཚམས་མེད་པའོ། །

[Block 2120]
རབ་ཏུ་རྒྱུ་བ་ཕྱོགས་གསལ་བ་གང་ཡིན་པ་དེ་ནི་རབ་ཏུ་རྒྱུ་བས་ཕྱོགས་གསལ་བར་སྣང་བའོ། །

[Block 2121]
ཤིང་རྟ་འདྲེན་པའི་རྟ་ནི་གཞན་མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2122]
དཔག་ཚད་དུ་མའི་ལམ་དུ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་དོན་རྟ་བྱིན་པ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། སྦྱིན་པ་ལ་དགའ་བ་སྟེ། དེ་བས་ན་སྒྲུབ་པའི་ཁྱད་པར་མཐའ་དག་འདིར་དཔག་ཚད་དུ་མ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2123]
འདི་དག་ལས་གཞན་མེད་པས་དེ་སྒྲུབ་པར༌[^1321]མི་འགྱུར་རོ། །

[Block 2124]
ལམ་དུ་དེ་ལུས་ལ་ཞེས་བྱ་བ་ནི་རྟ་དེ་བྱིན་པའི་སློང་བས་དེ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2125]
དཔག་ཚད་དུ་མ་ནི་དུས་མང་པོའི་དབང་དུ་བསྟན་ཏོ། །

[Block 2126]
གྲོགས་ནི་མེད་གྱུར་ཀྱང་ཞེས་བྱ་བ་ནི་གཞན་དེ་ན་བྱེད་པ་མེད་པའོ།[^1322] །བུ་སྨད་བཅས་ཤིང་ཞེས་བྱ་བ་ནི༌[^1323]དོན་གཉེར་བའི་གཞན་གྱི་དོན་ཉིད་དེ། དེ་ཡང་རང་གི་སྐྱོ་བ་བཟོད་པའོ། །

[Block 2127]
ཕྱི་རྗེས་མི་ལྟ་བར་ཞེས་བྱ་བ་ནི༌[^1324]སྡུག་བསྔལ་དེ་བཅོས་པའི་རྒྱུ་ཐོབ་པ་དག་གསལ་བའོ། །

[Block 2128]
རྟ་བཞིན་ནི་ཐམས་ཅད་ལུས་པ་མེད་པར་བྱིན་པའོ། །

[Block 2129]
ཚིག་རྐང་དེ་དག་གིས༌[^1325]ནི་སྦྱིན་པ་ལ་དགའ་བའི་རྒྱུ་ཉིད་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 2130]
ནགས་ཞེས་བྱ་བ་ནི་དཀའ་ཐུབ་ཀྱི་ནགས༌[^1326]སོ། །

[Block 2131]
གོམས་ཀྱང་ཞེས་བྱ་བ་ནི་ཡུན་རིང་པོར་ཤིན་ཏུ་གོམས་པ་སྟེ་ཡུན་རིང་དུ་རྟག་ཏུ་བྱེད་པ་དང་། གུས་པར་སྦྱོར་བ་དང་ལྡན་པ་དེས་སོ། །

[Block 2132]
དམ་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཏེ། ཡོན་ཏན་ལ་གོམས་པ་ནི་གཞན་ལ་ཕན་པ་དང་བདེ་བ་བྱེད་པ་ལ་གོམས་པ་སྟེ། གང་ལ་གང་ཞིག་བྱེད་པ་དེ་ཉིད་དེའི་བསོད་ནམས་ཀྱི་སྟོབས་ཡིན་གྱི་བྱེད་པ་པོའི་ཡོན་ཏན་ནི་མ་ཡིན་ནོ། །

[Block 2133]
དེ༌[^1327]ཅིའི་ཕྱིར་ཞེ་ན། སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་ཞིང་བདེ་བ་ལ་འཇུག་པ༌[^1328]ནི་མི་འགྲུབ་པར་སྣང་བས་སོ། །

[Block 2134]
དཔེར་ན་བྱང་ཆུབ་སེམས་དཔའ་ནི་གཞན་ལ་ཕན་ཞིང་བདེ་བར་འཇུག་པར་གྱུར༌[^1329]ན་ཡང་། ཡི་དགས་དང་དམྱལ་བ་ལ་སོགས་པར་སྐྱེས་པའི་སེམས་ཅན་བདེ་བར་འཇུག་པ་གྲུབ་པ༌[^1330]མེད་པས་སོ། །

[Block 2135]
ཀུ་མུ་ཏའི༌[^1331]ཁ་འབྱེད་པའི་ཟླ་བ་ཡང་གལ་ཏེ་ཟླ་བ་ཁ་འབྱེད་པ་ཡིན་ན་ནི། ཅིའི་ཕྱིར་པདྨ་ཁ་འབྱེད་པར་མི་བྱེད་དེ། ཁྱད་པར་མེད་པར་ལྟོས༌[^1332]ཤིང་ཁ་འབྱེད་རྒྱུར་གྱུར་པས་སོ། །

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
--- END BLOCKS ---
