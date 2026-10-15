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
གལ་ཏེ་སྒོ་མ་བཅད་ན་ནི་ཉེ་འཁོར་གྱི་མཐའ་འདིར་དང་པོ༌[^1331]རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2102]
སྒོ་བཅད་ན་ནི་དེའི་ཚེ་སྒོ་གཏན༌[^1332]གྱི་མཐའོ། །

[Block 2103]
རྒྱལ་པོའི་ཕོ་བྲང་དང༌[^1333]གྲོང་ཁྱེར་དག་ཀྱང་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་བཙུན་མོའི་འཁོར་དུ་འདུག་པའི་གནས་ཀྱི་དང་པོའི་སྒོ་གཏན་པའི༌[^1334]ཉེན་ཀོར་གྱི་མཐའ་གཉིས་ནི་དང་པོ་ཡིན་ནོ། །

[Block 2104]
དེ་བཞིན་དུ་རྒྱལ་པོའི་ཕོ་བྲང་དང་གྲོང་ཁྱེར་དག་གི་དང་པོ་ཡང་སྒོའི་གཏན་པའི༌[^1335]ཉེ་ཀོར་གྱི་མཐའ་གཉིས་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2105]
འོབས་ཀྱིས༌[^1336]བསྐོར་བ་ཉིད་ལ་ནི་སྒོའི་དབུས་ཀྱི་རི་མོ་ལ་ནི་སྒོའི་ངོགས་ཀྱི་དབུས་ཉིད་དུ་ངེས་པ་འདི་ནི་ཆོ་ག་དང་པོར་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 2106]
ཞར་ལ་བྱུང་བ་བཤད་ཟིན་ཏོ།། །།

[Block 2107]
གང་དུ་འདི་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བ་འདི་ལ་འཇུག་པ་གཞན་ལྟུང་བྱེད་གཞན་བྱེད་པའི་ཚུལ་གཞན་བརྗོད་པར་བྱ་སྟེ། རྒྱལ་པོའི་ཕོ་བྲང་གི༌[^1337]གནས་ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འབྲེལ་པ་ཉིད་ལའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2108]
འདིར་གཞུང་ནི་དགེ་སློང་ནམ༌[^1338]ལངས་པ་ལས༌[^1339]ནམ་མ་ལངས་པར་འདུ་ཤེས་བཞིན་དུ་རྒྱལ་པོའི་ཕོ་བྲང་གི་སྒོའི་གཏན་པ་ལས་འདས་པར་བྱེད་ན་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2109]
གྲོང་ཁྱེར་དང་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་གྲོང་ཁྱེར་གྱི་གནས་དང་འབྲེལ་པ་ཉིད་ལས་ནི་སྦྱོར་བ་ལས་བྱུང་བའི་ཉེས་བྱས་སུ་འགྱུར་བའོ། །

[Block 2110]
སྔ་མའི་ལྟུང་བྱེད་ཅེས་བྱ་བ་འདི་ལ་ཉེས་བྱས་ཀྱི༌[^1340]ཚིག་དང་སྐབས་ཀྱིས་རྟོགས་པའོ། །

[Block 2111]
ཅི་གང་ཡང་རུང་བ་ལ་འདི་དང་འབྲེལ་པ་ཉིད་ལ་ཉེས་བྱས་ནི་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་དེའི་དོན་ཉིད་ཡིན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་འདི་འབྲེལ་པ་གཉིས་བརྩམས་ན་གལ་ཏེ་གཅིག་ལ་ཡང་འདིའི་དོན་དུ་འབྲེལ་པ་ཉིད་ནི་འདི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2112]
འདི་ལ་ཅིག་ཤོས་ཀྱི་ཁ་ན་མ་ཐོ་བ་དེ་ཡང་ངོ་། །འདི་ལ་ཁ་ན་མ་ཐོ་བ་གཉིས་དེ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། གང་དུ་དུས་མ་ཡིན་པར་འདུག་པའི༌[^1341]ཁ་ན་མ་ཐོ་བ་མེད་པ་སྐྱ་རེངས༌[^1342]

[Block 2113]
དང་པོ་ཤར་བའི་མདུན་རོལ་དུ་མ་སྨྲས་པར་འཇུག་པ་འདི་ལ་དེའི་དགོངས་པ༌[^1343]ཅན་གྱི་ཚིག་སྟེ་དེ་ཡང་འདིར་ལྟུང་བྱེད་དུ་རིག་པར་བྱའོ། །

[Block 2114]
དེའི་ཕྱིར་དེ་ལ་བསྟན་པའོ། །

[Block 2115]
ཅི་གང་ཡང་རུང་བའི་འབྲེལ་པ་སྔ་མ་དག་ལ་གྲོང་ཁྱེར་དང་འབྲེལ་པ་དང་དེའི་དོན་ཉིད་དུ་ཁ་ན་མ་ཐོ་བ༌[^1344]དེ་ཡང་ཡོད་དམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་རྒྱལ་པོ་དང་། བཙུན་མོ་དང་། གཞོན་ནུ་དང་ཞང་བློན་དང་བར་ཆད་དང་། [^1345]གདུལ་བའི་དབང་གིས་མ་ཡིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གདུལ་བའི་དབང་གིས་འགྲོ་བའི་ལུང་ནི་འཕགས་པ་ཤཱ་རིའི་བུའི་བྱུང་བའི་མཐའ་ལས་རྗེས་སུ་གནང་བ་ཡིན་ཏེ། བྱེ་བྲག་ཏུ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 2116]
འདིར་ལུང་ནི་རྒྱལ་པོས་བོས་པ་དང་། བཙུན་མོ་དང་། གཞོན་ནུ་དང་ཞང་བློན་དང་བར་ཆད་བརྒྱད་པོ་དག་ལས་གང་ཡང་རུང་བ་ཉེ་བར་གནས་པར་གྱུར་ན་ཉེས་པ་མེད་དོ་ཞེས་གསུངས་སོ། །

[Block 2117]
མ་བཟླུགས་པར་རྒྱལ་པོའི་ཕོ་བྲང་དུ་འཇུག་པར་མི་བྱའོ། །

[Block 2118]
འོ་ན་འདིར་གཞུང་ནི་མ་ཞུས་པར་རྒྱལ་པོའི་ཕོ་བྲང་དུ་འཇུག་པར་མི་བྱ་བར་དགེ་འདུན་གྱི་དབྱེན་གྱི་གཞི་ལས་གསུངས་སོ། །

[Block 2119]
ཁྱོད་ཀྱིས་ཀྱང་གྱ་ཚོམ་དུ་རྒྱལ་པོའི་ཕོ་བྲང་དུ་འཇུག་པར་མི་བྱ་བར་སྒོར༌[^1346]བསྡད་ནས་ཤཱཀྱའི་དགེ་སློང་འོངས་སོ་ཞེས་བརྗོད་པར་བྱ་ཞིང་། གལ་ཏེ་སྤྱོན༌[^1347]ཅིག་ཟེར་ན་འཇུག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2120]
རྒྱལ་པོའི་ཕོ་བྲང་དུ་ནུབ་མོ་འགྲོ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 2121]
གང་ལ་བསླབ་པ་བསྟན་པ་ལ་ལོག་པར་བསྒྲུབ་པ་ནི་རྣམ་པ་གསུམ་གནང་སྟེ། ཁྱད་དུ་གསོད་པ་དང་སྤོང་བ་དང་བསླབ་པའི་གཞི་དངོས་པོ་ལ་ཁྱད་དུ་གསོད་པའོ། །

[Block 2122]
དེ་གཉིས་གང་ཡང་སྔགས་ཀྱི་གཞི་ཐོབ་པ་ལས་བརྟགས་པ༌[^1348]སྟེ། དེ་ནི་མདུན་ནས་རྣམ་པར་གཞག་པ་ཡིན་ཏེ། དེ་བས་ན་དོན་དེ་ཉིད་དུ་རྣམ་པར་གཞག་པའོ། །

[Block 2123]
དངོས་པོ་ལ་ཁྱད་དུ་གསོད་པ་གང་ཡིན་པ་དེ་ནི། འདིར་ཡང་དག་པར་ཞུགས་ཏེ། དེ་བས་ན་འདི་ཉིད་དུ་རྣམ་པར་འབྱེད་པར་བྱ་སྟེ། གང་ལ་འདིའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སོ་སོར་ཐར་པའི་མདོ་གདོན་པ༌[^1349]འདོན་པའི་ཚེ། དེ་ལ༌[^1350]ལན་གཉིས་ཉམས་སུ་མྱོང་ཞིང་ཡིད་རྨོངས་པ་མ་ཡིན་པས།[^1351] འདི་ལ་ཆོས་འདི་ཡོད་པར་གཟོད༌[^1352]ཤེས་སོ་ཞེས་ཟེར་བ་དེ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལན་གཉིས་ཉམས་སུ་མྱོང་ཞིང་ཞེས་བྱ་བ་ནི་སོ་སོར་ཐར་པའི་མདོ་གདོན་པ་འདོད་པ༌[^1353]གང་གིས༌[^1354]ལན་གཉིས་ཉམས་སུ་མྱོང་བ་དེ་ཡིས་སོ། །

[Block 2124]
ཉམས་སུ་མྱོང་བ་མེད་པ་ཉིད་ལ་གཉིས་པོ་འདིས་མ་གྲོལ་བ་ལ་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 2125]
གལ་ཏེ་དགེ་སློང་དག་གིས་དེང་ཤེས་པར་འགྱུར་ན། ཚེ་དང་ལྡན་པ་འདི་ནི་སྔར་གནས་པ་ལན་གཉིས་ལན་གསུམ་དུ་གསོ་སྦྱོང་གི་ལས་སླར་བརྗོད་པ་གང་ཡིན་པ་དེའི་ས་འདི་ནི་བསྡུ་བ་ཡིན་ནོ། །

[Block 2126]
ཡིད་རྨོངས་པ་མ་ཡིན་པས་ཞེས་བྱ་བ་ནི་ལྟུང་བ་མ་ཡིན་པའི་ངོ་བོ་ལ་རྒན་པོ་ཁོ་ན་ལ་མི་ཤེས་པར་འབྱུང་བ་ཡིན་ཏེ། ཡིད་རྨོངས་པ་མ་ཡིན་པས་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2127]
རིགས་པ་ལས་སྤྱོད་པ་འདི་དགེ་བ་ཡིན་ཏེ། [^1355]དོན་གང་ལ་ཡིད་རྨོངས་པ༌[^1356]མ་ཡིན་པས་སོ། །

[Block 2128]
དེ་བས་ན༌[^1357]ལྟུང་བ་རྣམ་པར་གཞག་པ་འདི་ནི་རིགས་པ་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2129]
ཁ་ན་མ་ཐོ་བ་འདི་ལ་ཐམས་ཅད་མ་གུས་པར་གྱུར་པའི་སེམས་དེར་གལ་ཏེ་སངས་རྒྱས་ལ་ཡང་འདིར་འདི་མ་གྲུབ་པས་མ་གུས་པའི་ལྟུང་བྱེད་ཀྱང་རིག་པར་བྱའོ། །

[Block 2130]
གལ་ཏེ་མ་ཡིན་ན་མ་གུས་པའི་ཉེས་བྱས་ཀྱང་མ་ཡིན་ནོ། །

[Block 2131]
བརྫུན་དུ་སྨྲ་བ་ཡིན་ན་ནི་བརྫུན་དུ་སྨྲ་བའི་ལྟུང་བྱེད་གཞན་དུ་ཡང་འགྱུར་རོ། །

[Block 2132]
མཚན་གཞན་གྱིས་འདོན་པའི་ཚེ། ཐུན་མོང་བ་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ལ། མཚན་གཞན་འདོན་པའི་ཚེ་ཞེས་བྱ་བ་ནི། [^1358]དགེ་སློང་ལ་ལྟུང་བྱེད་དོ་ཞེས་བྱ་བ་དགེ་སློང་མ་རྣམས་ཀྱིས་གསོ་སྦྱོང་འདོན་པའི་ཚེ་བསླབ་པ་ཐུན་མོང་པའི་ཕྱིར་ད་ལྟར་བདག་གིས་ཤེས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ཉེས་བྱས་སོ། །

[Block 2133]
ལྟུང་བ་མ་ཡིན་པ་བསྟན་པ་ལས་འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་བཙུན་པ་དགེ་སློང་མ་རྣམས་ཀྱིས༌[^1359]སོ་སོར་ཐར་པའི་མདོ་འདོན་པ་ན་འདི་སྐད་ཅེས་འདི་ལྟར་ཆོས་འདི་ཡང་མདོའི་ནང་དུ་འདུས་པར༌[^1360]བདག་གིས་ད་གཟོད༌[^1361]ཤེས་སོ་ཞེས་མཆི་ན་ལྟུང་བ་ཅིར་འགྱུར། གལ་ཏེ་བསླབ་པ་ཐུན་མོང་མ་ཡིན་པ་ལ་བསམས་ཏེ་སྨྲས་ན་ལྟུང་བ་མེད་དོ། །

[Block 2134]
གང་གི་ཚེ་བསླབ་པ་ཐུན་མོང་པ་ལས་བསམས་ཏེ་སྨྲས་ན་ཉེས་བྱས་སོ། །

[Block 2135]
དེ་བཞིན་དུ་དགེ་སློང་མ་ལ་ཡང་སྦྱར་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2136]
མདོ་སྡེ་དང་ལྡན་པ་སྨྲས་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི། མདོ་སྡེ་དང་ལྡན་པའི༌[^1362]བསླབ་པའི་གཞི་སྨྲ་བ༌[^1363]ན་དེ་སྐད་ཟེར་བ་དེ་ལ་ཉེས་བྱས་སོ། །

[Block 2137]
གཞུང་ཁ་ཅིག་ལས་འདིར་གཞུང་ནི་འདུལ་བ་དང་ལྡན་པའི་མདོ་མ་གཏོགས་པ་ལ་འདི་སྐད་ཅེས་འདི་ལྟར་ཆོས་འདི་ཡང་མདོའི་ནང་དུ་གཏོགས་མདོའི་ནང་དུ་འདུས་པ་དང་། ཟླ་བ་ཕྱེད་ཕྱེད་ཅིང་བཏོན་པར་བདག་གིས་ད་གཟོད་ཤེས་སོ་ཞེས་ཟེར་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2138]
ཐུན་མོང་མ་ཡིན་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། མཚན་གཞན་བསྟན་པ་འདི་ནི་བསླབ་པའི་གཞི་ཐུན་མོང་མ་ཡིན་པ་འདོན་པའི་ཚེ་ལྟུང་བ་མེད་པའོ། །

[Block 2139]
སོ་སོར་ཐར་པའི་མདོ་འདོན་པའི་ཚེ་མ་གུས་པར་ཉན་པ་ཉེ་བར་བསྒྲུབ་པ་འགྱོད་དུ་གཞུག་གོ་ཞེས་བྱ་བ་ནི། བདག་གིས་ད་གཟོད་ཤེས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཙམ་ལ་ཡང་སྔར་འདུག་པ་ན་འདོན་པ་ལ་མ་གུས་པར་ཉན་པ་ལ་ཉེ་བར་སྦྱར་བར་རིག་པར་བྱའོ། །

[Block 2140]
དངོས་སུ་ནི་མ་ཡིན་ཏེ། གང་ཞིག་འདི་བསྟན་པ་ཅི་ཁོ་བོ་ཅག་ལ་ལས་འདི་ཉིད་གཅིག་པུ་ཡིན་ནམ། ཁོ་བོ་ཅག་གིས་ཀྱང་འདོད་པའི་རྣམ་པར་རྟོག་པ་ལ་ཡང་རྣམ་པར་རྟོག༌[^1364]དགོས་སོ། །
--- END BLOCKS ---
