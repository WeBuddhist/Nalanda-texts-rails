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
[Block 2381]
དུ་མར་གནས་པ་ཁས་བླངས་པ་ལ་ནི་འཆགས་པ༌[^2168]ཁོ་ནའོ་ཞེས་བྱ་བ་ནི་མཚམས་གཉིས་ལ་གནས་པའི་རྐང་པ་དག་གིས་ནོན་པའི་རྫས་ལ་གནས་པ་གང་ཡིན་པ་ཇི་སྙེད་པའི་གནས་གཅིག་ཏུ་དབྱར་གནས་པར་ཁས་ལེན་པ་དེ་ལ་ནི་མི་འཆགས་པ༌[^2169]མ་ཡིན་ཏེ། འཆགས་པ༌[^2170]ཁོ་ན་ཡིན་ནོ། །

[Block 2382]
གནས་མལ་དུ་མ་མནོད་པར་རིགས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་ཚུལ་ཀྱིས་མཚམས་དུ་མར་གནས་བསྟེན་པར་གྱུར་པ་ལ་དེ་དང་ཉེ་བ་དེ་དག་གི་ཁོངས་སུ་གཏོགས་པ་གནས་མལ་མནོད་པར༌[^2171]བྱེད་པ་དེ་ནི་ཆོས་དང་མི༌[^2172]མཐུན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2383]
ཅི་དེས་ཐམས་ཅད་དུ་དུས་མཉམ་པར་གནས་པར་བྱའམ། འོན་ཏེ་མཚམས་དུ་མར་ཅི་དགར་གནས་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཇི་ལྟར་འདོད་པས་དུས་འགའ་ཞིག་གི༌[^2173]ཚེ་སྐབས་འགའ་ཞིག་གམ་གཅིག་ལ་དུས་ཐམས་ཅད་དུ་མངོན་པར་བརྟེན་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2384]
དེའི་ཕྱིར་དེས་ཅི་དགར་གནས་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེས་གཙུག་ལག་ཁང་དུ་དུས་ཇི་སྲིད་གནས་པར་འདོད་པ་དེ་སྲིད་དུ་དེར༌[^2174]གནས་པར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 2385]
ཆོ་ག་འདི༌[^2175]རྣམས་ལ་ནམ་མཁའ་ཅིའི་ཕྱིར་མ་སྨོས་ན། མཚམས་གཞན་སྨོས་པ་ཉིད་ཀྱི་ཕྱིར་ནམ་མཁའ་ལ་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་ཅིའི་ཕྱིར་སྨོས། ནང་གི་ནམ་མཁར་ཕྱི་རོལ་དུའོ་ཞེས་བྱ་བ་གཏོགས་པའི་ཕྱིར་རོ། །

[Block 2386]
རྒྱལ་བ་ནི་མི༌[^2176]མཐུན་པ་ཉིད་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པ་ནང་གི་མཚམས་ལ་གནས་ཤིང་རྗེས་སུ་མ་ཞུགས་པར་འདུག་པ་ལ་ལས་བྱེད་པ་དེ་ནི་དཀོན་མཆོག་གཞན་ཡིན་པས་ལས་མི་མཐུན་པར་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2387]
ཁ་སྐོང་བར་བྱེད་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྒྱལ་བ་ནི་དགེ་འདུན་གྱི༌[^2177]ཁ་སྐོང་བར་བྱེད་པ་མ་ཡིན་ཏེ། །ལས་དག་མི་བྱ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 2388]
དེས་བྱ་བ་ལས་མ་ཡིན་པས་མི་འཆགས༌[^2178]སོ་ཞེས་བྱ་བ་ནི་ལས་དེས་བསྙེན་པར་རྫོགས་པ་ལ་སོགས་པར་བྱ་བར་རྣམ་པར་གཞག་པ་གང་ཡིན་པ་དེ་ལས་མ་ཡིན་པས་བྱས་ན་མི་འཆགས་སོ། །

[Block 2389]
འདིར་གཞུང་ནི་བསྙེན་པར་རྫོགས་པར་བགྱི་བ་གསོལ་བ་དང་། བཞིའི་ལས་མི་བགྱིད་ན་བསྙེན་པར་རྫོགས་ཞེས་བགྱིའམ། བསྙེན་པར་མ་རྫོགས༌[^2179]ཞེས་བརྗོད་པར་བགྱི། བཀའ་སྩལ་པ། བསྙེན་པར་རྫོགས་ཞེས་བརྗོད་པར་བགྱིའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2390]
དེ་བསྙེན་པར་རྫོགས་པར་བྱ་བའི་སྐབས་སུ་གསུངས་པ་ཡིན་མོད་ཀྱི་ཐམས་ཅད་ལ་འདྲ་བས་འདིར་སྤྱིར་མདོར་བྱས་སོ། །

[Block 2391]
ཕལ་ཆེར་བྱས་པ་ཉིད་ཡིན་ཡང་ལས་ཡོངས་སུ་མ་རྫོགས་པའི་ཕྱིར་དེ་མ་བྱས་པ་ཉིད་ཡིན་པར་དོགས་པ་བསལ་བའི་ཕྱིར། ཚིག་ཕལ་ཆེར་བྱས་པ་ཉིད་ནི་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་གསོལ་བའི་བདག་ཉིད་དམ་བརྗོད་པའི་བདག་ཉིད་ཀྱི་ཚིག་ཕལ་ཆེར་བྱས་པ་ཉིད་ཅེས་བྱ་བ་སུམ་གཉིས་བརྗོད་ཟིན་ན་སུམ་ཆ་བརྗོད་པའི་ཚེ་ན་རིལ་གྱིས་ཟིན་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2392]
གསོལ་བ་དང་བརྗོད་པ་དག་ལ་དོན་འདི་སྐབས་གསུམ་ཡོད་དེ།

[Block 2393]
དང་པོ་ནི་རང་གི་ངོ་བོ་ཙམ་བརྗོད་པ་སྟེ། དཔེར་ན་དགེ་འདུན་བཙུན་པ་རྣམས་གསན་དུ་གསོལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2394]
གཉིས་པ་ནི་བྱ་བ་བརྗོད་པ་སྟེ། དཔེར་ན་མིང་འདི་ཞེས་བགྱི་བ་འདི་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2395]
གསུམ་པ་ནི་བྱེད་པ་བརྗོད་པར་བྱ་སྟེ། དཔེར་ན་དགེ་འདུན་གྱི༌[^2180]དུས་ལ་བབ་ཅིང་བཟོད་ན་དགེ་འདུན་གྱིས༌[^2181]གནང་བར་མཛོད་ཅིག་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2396]
གང་རྣམས་ཀྱིས་ཞེས་བྱ་བ་དང་པོར་བརྗོད་པ་ཞེས་བྱ་བ་འདིར་གསུམ་པའི་ཆ་ལ་ཐ་མ་འཇུག་པ་ཉིད་དོ་ཞེས་བྱ་བ་དེའི་རྗེས་སུ་འབྲངས༌[^2182]པས་རྟོགས་པར་བྱའོ། །

[Block 2397]
ཅི་ཚིག་ཐམས་ཅད་ལ་ཕལ་ཆེར་བྱས་པ་ཉིད་ན་བྱས་པ་ཉིད་ཡིན་ནམ་ཞེ་ན་དེའི་ཕྱིར་འོག་མ་མེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚིག་གང་ལ་འོག་མ་མེད་པ་དེ་ནི་འོག་མ་མེད་པ་སྟེ། གང་ཞིག་ཐ་མའི་ཚིག་དེ་ལས༌[^2183]ཕལ་ཆེར་བྱས་པ་ཉིད་ན་བྱས་པ་ཉིད་དོ། །

[Block 2398]
གསོལ་བའི་ལས་ནི་ཕལ་ཆེར་བྱས་པ་ཉིད་ན་བྱས་པ་ཉིད་དོ། །

[Block 2399]
གསོལ་བ་དང་གཉིས་ཀྱི་ལས་ལ་ནི་ལས་བརྗོད་པ་ཉིད་འོག་མ་མེད་པ་ཡིན་ནོ། །

[Block 2400]
གསོལ་བ་དང་བཞིའི་ལས་ལ་ནི་ལས་བརྗོད་པ་གསུམ་པ་འོག་མ་མེད་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2401]
འདིར་གཞུང་ནི༌[^2184]གླེང་གཞི་དག་ལས།

[Block 2402]
མཚམས་བཅད་པ་ལ་བཙུན་པ་རེ་ཞིག་མཚམས་འགུམས་པ༌[^2185]ན་དགེ་སློང་ལས་བགྱིད་པ་སྲོག་ཆད་ཅིང་དུས་བགྱིས་པར་གྱུར་ན་མཚམས་བཀུམ་པར་བརྗོད་པར་བགྱིའམ། མ་བཀུམ་པར་བརྗོད་པར་བགྱི། ཉེ་བ༌[^2186]འཁོར་གལ་ཏེ་མཚན་མ་དག་བརྗོད་པར་གྱུར་ན་ནི་ལས་ཕལ་ཆེར་བྱས་པས་གཅད་པར༌[^2187]བརྗོད་པར་བྱའོ། །

[Block 2403]
བཟློག་པས་ནི་མ་བཅད་པར་བརྗོད་པར་བྱའོ། །

[Block 2404]
དགེ་སློང་མའི་མཚམས་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2405]
དེ་ཉིད་ཐམས་ཅད་དུ་རུང་བས་འདིར་སྤྱིར་མདོར་བྱས་སོ། །

[Block 2406]
གང་ཞིག་སླར་བྱས་པ་ཉིད་ལ་ཡང་ཚིག་ཕྱི་མའི་ཚིག་ལ་ཞེས་བྱ་བ་དེ་བས་འདིར་ཚིག་འོག་མ་མ་ཡིན་པ་ལ༌[^2188]ཞེས་བྱེ་བྲག་ཏུ་བསྟན་པའོ། །

[Block 2407]
མཚན་མ་དག་མ་བརྗོད་པ་ཉིད་ན་མ་བཅད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། ཕལ་ཆེར་བྱས་པ་ཉིད་ན་བྱས་པ་ཉིད་ཡིན་དུ་ཟིན་ཀྱང་ཕྱོགས་བཞིའི་མཚན༌[^2189]དག་མ་བརྗོད་ན་མཚམས་གཅད་པའི༌[^2190]ལས་བྱས་པ་དག་མ་ཡིན་ཏེ། མཚམས་ངེས་པ་ལ༌[^2191]དེ་རྣམ་པར་གཞག་པར་འགྱུར་རོ། །

[Block 2408]
དེ་ལ་རྣམ་པར་གཞག་པ་དེ་ནི་ལས་ཞེས་བྱ་སྟེ་དེ་བས་ན་དེ་ཤེས་པའོ། །

[Block 2409]
ཡོངས་སུ་གནས་པས་ནི་ཉེ་བར་གནས་པ་ལས་གཞན་པའོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པས་ནི་ཚངས་པར་སྤྱོད་པ་སྟེ། ཉེ་བར་གནས་པའི་སྡོམ་པ་མ་གཏོགས་པར་དེ་ལས་གཞན་པའི་ལས་བྱས་པ་ཉིད་ན་བྱས་པ་ཉིད་ཡིན་པའོ། །

[Block 2410]
འདིར་གཞུང་ནི་དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 2411]
ཡོངས་སུ་གནས་པས་དགེ་སློང་གནས་ནས་འབྱིན་པ་གནས་ནས་ཕྱུང་བར་བརྗོད་པར་བགྱིའམ། ཉེ་བར་གནས་པའི་སྡོམ་པ་མ་གཏོགས་པར་ལས་ཐམས་ཅད་བྱས་པར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2412]
གང་ཞིག་འདིས་ལས་རྣམས་མི་བྱ་བ་ཉིད་དུ་གསུངས་པ་དེར་མི་འཆགས་པ་ཉིད་ལ་དེ་ནི་དཔེ་ཙམ་དུ་ཟད་དེ། བསྡུ་བར་བྱས་ནས་མ་ཡིན་པ་ཞེས་བྱ་བ་དེའི་ཕྱིར་དེ་ཤེས་པའོ། །

[Block 2413]
དེ་ལྟ་བས་ན་དཔེ་ཙམ་དུ་ཟད་དེ་དགེ་འདུན་ལྷག་མ་སྤྱོད་པ་ལ་གནས་པ་གཞན་དག་ལ་ཡང་ཆོ་ག་འདི་ཞེས་བྱ་བ༌[^2192]ཤེས་པར་བྱའོ། །

[Block 2414]
སྨྱོན་པས་བཏོན་པ༌[^2193]ཡང་ངོ་ཞེས་བྱ་བ་ནི་སྨྱོན་པས༌[^2194]སོ་སོར་ཐར་པའི་མདོ་གདོན་པར་བྱས་པ་ལ་ཡང་བྱས་པ་ཉིད་ཡིན་ནོ། །

[Block 2415]
འདིར་གཞུང་ནི་སྨྱོན་པས་སོ་སོར་ཐར་པའི་མདོ་བཏོན་ན། སོ་སོར་ཐར་པའི་མདོ་གདོན་པར་བརྗོད་པར་བགྱིའམ།[^2195] བཀའ་སྩལ་པ་བཏོན༌[^2196]པར་བརྗོད་པར་བགྱིའོ། །

[Block 2416]
གསོ་སྦྱོང་བགྱིད་པར༌[^2197]བརྗོད་པར་བགྱིའམ། བཀའ་སྩལ་པ་བྱས་པར༌[^2198]བགྱིའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2417]
འདིར་སྨྱོན་པ་ནི་དཔེ་ཙམ༌[^2199]དུ་ཟད་དེ་དེས་ན་རང་བཞིན་དུ་ཉམས་པ་ཐམས་ཅད་འཕངས་པ་ཡིན་ཏེ་དོན་དྲན་པའི་ཕྱིར་རོ། །

[Block 2418]
དབྱེན་རྗེས་སུ་སྒྲུབ་པ་ནི་གསོལ་བ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་རྒྱུ་གང་དག་གིས་གསོལ་བའི་ལས་བྱས་པ་མི་འཆགས་པ་དེ་བཞིན་དུ་རྒྱུ་དེ་དག་ཉིད་ཀྱིས་དགེ་འདུན་གྱི་དབྱེན་གྱི་སྦྱོར་བ་རྗེས་སུ་སྒྲུབ་པ་ལ་ནི་ཡང་དེ་རྣམས་ཀྱིས་ཤེས་པའི་དོན་ཏོ། །

[Block 2419]
གང་ཞིག་འདིར་ཚུལ་ཤིང་དག་ལེན་པ་དང་། འདྲིམ་པར་བྱེད་པའི་ངོ་བོ་དེའི་དོན་དུ་མདོ་འདི་བྱས་ཏེ། གཞན་ལ་གསོལ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2420]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་གནས་ནས༌[^2200]ཕྱུང་བ་དང་དགུས་དགེ་འདུན་འབྱེད་ན་དགེ་འདུན་མ་ཕྱེད་པར་བརྗོད་པར་བྱའོ། །
--- END BLOCKS ---
