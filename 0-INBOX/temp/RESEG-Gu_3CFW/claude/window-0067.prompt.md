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
[Block 2346]
བྱས་པ་ཉིད་ནི་གནས་པར༌[^2135]བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ལས་ལ་རབ་ཏུ་གནས་པ༌[^2136]ཉིད་ཅེས་བྱ་བ་ལས་བྱེད་པ་པོ་མ་ཡིན་པས་བྱས་པ་ཉིད་འདི་ལ་རིག་པར་བྱའོ། །

[Block 2347]
དཔེར་ན་དགེ་འདུན་གྱིས་བཟོད་ཅིང་གནང་ནས་དགེ་འདུན་མིང་འདི་ཞེས་བགྱི་བ་དགེ་སློང་རུང་བ་ལ་འཆགས་པའི༌[^2137]གཞི་བསྟན་པ་སྦྱིན་པ་སྟེ། གང་གི་ཚེ༌[^2138]འདི་ལྟར༌[^2139]ཅང་མི་གསུང་བས༌[^2140]དེ་དེ་བཞིན་དུ་འཛིན་ཏོ་ཞེས་གསུངས་པ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2348]
གསོལ་བ་ནི་གོ་བར་བྱ་བ་ཙམ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2349]
འདི་ལ་བྱེད་པ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་གསོལ་བ་དང་བཞིའི་ལས་ལ་དེ་ཐལ་བ་མ་ཡིན་ནོ། །

[Block 2350]
མཚམས་གཅོད་པ་ཉིད་ནི་གཅད་པ༌[^2141]དང་འདྲ་བ་ཉིད་དུ་ཤེས་པར་བྱའོ་ཞེས་བྱ་བ་ལ་འདིར་མཚམས་གཅོད་པ་ཉིད་ཅེས་བྱ་བ་ནི་མཚམས་མ༌[^2142]མནན་པར་དགེ་འདུན་གནས་པ་ལ་མཚམས་བཅད་པ་ཉིད་འགྲུབ་པ་མ་ཡིན་ཏེ། དེ་བཞིན་དུ་བཅད་པར་གྱུར་པ་ཉིད་ཀྱང་མི་འགྲུབ་སྟེ། འདི་ལྟར་མཚམས་གཅད་པར༌[^2143]འདོད་པ༌[^2144]ངོས་དེ་དང་ཉེ་བའི་ཕྱོགས་དེ་ན་གནས་པའི་དགེ་འདུན་གྱི་ཆའི་ཕྱོགས་དེར་ཡང་བཅད་པར་མི་འགྱུར་རོ། །

[Block 2351]
སྡུད་པར་བྱེད་པས་གཎྜཱི་བརྡུང་བ་དང་། འདྲི་བ་ལ་བརྗོད་པ་རྗེས་སུ་བསྒྲུབ་པ༌[^2145]དག་གིས་བསྡུ་བར་བྱ་བ་དག་ལ་གོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། དགེ་འདུན་སྡུད་པར་བྱེད་པའི་གང་ཟག་གིས་གཎྜཱི་བརྡུང་བ་དང་། ཅིའི་ཕྱིར་བརྡུང༌[^2146]ཞེས་དྲི་བ་དག་ལ་ཚིག་གང་ཞིག་རིགས་པ་ལས་མ་འདས་པ་དེ་དང་འདྲ་བའི་ཚིག་དྲི་བ་ལ་བརྗོད་པའོ། །

[Block 2352]
དེས་དེ་དག་གི་དོན་དུ་བཤམ་མོ་ཞེས་བྱ་བ་ནི། སྡུད་པར་བྱེད་པ་དེས་སྡུད་པར་བྱ་བ་དེ་དག་གི་དོན་དུ་སྟན་བཤམ་པར་བྱའོ། །

[Block 2353]
བསྐོས་པའི་བྱ་བ་དེའི་དོན་ཉིད་ལ་ནི་དེ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། བསྐོས་པ་དེའི་བྱ་བ་ལག་གི་བླ་ལ་སོགས་པ་དོན་གང་གི་ཕྱིར་དེ་བགོ་བར༌[^2147]བྱ་བ་དེའི་དོན་ཉིད་ལ་བསྡུ་བར་བྱ་བ་དེ་བསྐོ་བར་བྱ་བ་དེ་ཉིད་ནི་འདུག་པར་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 2354]
དེས་འདིར་གཎྜཱི་བརྡུང་བ་ལ་སོགས་པ་བྱའོ། །

[Block 2355]
ཐམས་ཅད་ལ་རྒན་རིམས་སུའོ་ཞེས་བྱ་བ་ནི་ཤིང་དྲུང་དང་ནེའུ་གསིང་གི་ཕྱོགས་དང་དགོན་པའི་ས་གཞི་དང་། འདུག་པའི་གནས་ཐམས་ཅད་ལ་རྒན་རིམས་སུ་བསྐོ་བ་རིགས་པ་ཉིད་ཡིན་ནོ། །

[Block 2356]
བླང་བར་བྱ་བ་ཉིད་ལ་ནི་འདོད་པ་མཆོག་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བསྡུ་བར་བྱ་བ་དང་འདུལ་བ་དང༌[^2148]ཕྱག་བྱ་བ་དང་། མདུན་དུ་འགྲོ་བ་དག་གམ། དེ་ལྟ་བུ་གཞན་ལ་ཡང་རྣམ་པར་རྟོག་པ་མེད་དོ། །

[Block 2357]
དེར་ཇི་ལྟར་རྒན་རིམས་ཁོ་ནས་རྣམ་པར་མི་གཞག་གོ། །

[Block 2358]
བླང་བར་བྱ་བ་གནས་མལ་ལ་སོགས་པ་དག་ལ་ནི་འདོད་པས་མཆོག་ཉིད་དུ་རྣམ་པར་གཞག་གི་དངོས་པོ་ལས་རྣམ་པར་མི་གཞག་སྟེ། ལེན་པ་པོ་རྒན་པ་དེ་འདོད་པ་ཡིན་ན་ངན་པ་གང་ཡིན་པ་དེ་ཡང་དེ་ལ་སྦྱིན་པར་བྱ་བའི་ཕྱིར་མཆོག་ཡིན་གྱིས་གང་ཐོབ་པ༌[^2149]བཟང་པོ་དེ་ནི་མཆོག་ཉིད་མ་ཡིན་ནོ། །

[Block 2359]
འདིར་གཞུང་ནི་དངོས་པོ༌[^2150]ཆེན་པོ་གང་དག་ཡིན་པ་ལ་བྱི་དོར་བྱེད་པས་རྒན་པོ་དག་ངལ་བར་གྱུར་པས་མི་འདོད་ནས། དེ་དག་ལ་མི་འདོད་བཞིན་དུ་སྦྱིན་པར་མི་བྱ་བར་གསར་བུ་དག་གིས་དེ་དག་བླང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2360]
ལས་སྤྱིར་བསྟན་པའོ།། །།

[Block 2361]
བསྒོ་བ་ལས་བྱུང་བ་ཕྱིར་མ་བཅོས་པས་ལས་ཉམས་སུ་མྱོང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བསྒོ་བ་ལས་གྱུར་པ་འདིས་མ་བྱས་པ་དགེ་འདུན་གྱི་ལྷག་མ་བཞི་ལས་ལྟུང་བ་འབའ་ཞིག་དང་། ལྟ་བའི་རྣམ་པ་མི་གཏོང་བའི་ལྟུང་བྱེད་ཀྱི་བདག་ཉིད༌[^2151]བསྒོ་བ་ལས་བྱུང་བ་ཕྱིར་མ་བཅོས་པ་དེས་ལས་ཉམས་སུ་མྱོང་བར་མི་བྱ་སྟེ། དེ་ཉམས་སུ་མྱོང་བ་དེ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 2362]
གང་དག་གིས་དེས༌[^2152]ཁ་ན་མ་ཐོ་བ་དེ་ཕྱིར་མ་བཅོས་པར་ཤེས་བཞིན་དུ་དེ་དང་ལྷན་ཅིག་ལས་ཉམས་སུ་མྱོང་བར་བྱེད་པ་དེ་དག་ལ་ཡང་ཉེས་བྱས་སུ་འགྱུར་བར་རིག་པར་བྱའོ། །

[Block 2363]
དགེ་འདུན་ལས་ཐ་དད་པའི་དངོས་པོར་གྱུར་པ་ཞེས་བྱ་བ་དེ་ལྟ་བུར་གྱུར་པའི་ཁ་ན་མ་ཐོ་བ་འདི་རྣམས་དང་། ལུས་ཀྱི༌[^2153]ལས་ངན་པ་བྱེད་པ་གཞན་དུ་གྱུར་པ་ལ༌[^2154]གཞན་དུ་གཏོགས་པ་ཞེས་བྱ་བ་ཉེས་བྱས་འདི་ཤེས་པས་སོ། །

[Block 2364]
གསོ་སྦྱོང་དང་དགག་དབྱེ་དག་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་ནི་དེ་ན༌[^2155]གཉིས་ཉམས་སུ་མྱོང་བ་ལ་ཉེས་བྱས་སུ་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2365]
དགེ་འདུན་དུ་བྱེད་པ་ལ་ནི་ཡན་ལག་གི་དངོས་པོར་མི་སྦྱོར་བའོ། །

[Block 2366]
རང་གི་དོན་དུ་འགྲོ་བ་དག་གང་ཞིག་བྱེད་པ་འདི་དགེ་འདུན་གྱིས་དོར་བར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2367]
དགེ་སློང་གི་དོན་ལ་གཞི་སྤངས་པ་ལ་ཉམས་ཞེས་བྱ་བ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 2368]
འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 2369]
དགེ་སློང་གིས་ཇི་སྲིད་དུ་གཞི་དེས་མ་བཤགས་ཤིང་སོ་སོར་མ་བཤགས་པར་གསོལ་བ་དང་། གསོལ་བ་དང་གཉིས་དང་གསོལ་བ་དང་བཞིའི་ལས་ཉམས་སུ་མྱོང་བར་བྱེད་ན་ཐམས་ཅད་དུ་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2370]
འདིར་འདྲ་བའི་རྗེས་སུ་འབྲངས་ནས་སྨོས་པ་ཡིན་གྱི། ཆོས་མ་ཡིན་གྱི་ལས་ཉིད་སྨོས་པ་ཞེས་བྱ་བ་སྔ་མ་ལ་འདི་གོ་བར་བྱེད་པ་ཉིད་ནི་མ་ཡིན་ཏེ། གསོ་སྦྱོང་དང་དགག་དབྱེ་དག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2371]
མཚམས་གཞན་ན་གནས་པ་ནི་གང་གི་ཡན་ལག་ཉིད་ཀྱང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ནམ་གང་ཟག་མཚམས་གཞན་ན་གནས་པ་ནི་ལས་གང་གི་ཡན་ལག་ཉིད་ཀྱང་མ་ཡིན་ཏེ། བྱིན་ལེན་ལ་སོགས་པ་བྱས་ཀྱང་མ་བྱས་པ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 2372]
མཚམས་གཞན་ན་གནས་པ་ཉིད་ན་བཟོད་པར་གསོལ་བ་ལ་སོགས་པའི་གསོལ་བ་ཡང་འདི་ལྟ་སྟེ། འདུན་པ་དང་ཡོངས་སུ་དག་པ་དང་དགག་དབྱེ་བྱ་བ་དང་། བརྗོད་པ་འདི་རྣམས་ལ་ཡང་དགག་དབྱེ་བྱེད་པ་པོ་འཇོག་པ་དང་དགག་དབྱེ་ལའོ། །

[Block 2373]
དེར་སོང་ན་ཚོགས་པའི་ཡན་ལག་ཉམས་སོ་ཞེས་བྱ་བ་ནི་མཚམས་གཞན་དུ་སོང་ན་གང་ཞིག་ཚོགས་པའི་ཡན་ལག་འདི་ལྟ་སྟེ། འདུན་པ་དང་ཡོངས་སུ་དག་པ་དང་དགག་དབྱེ་བླངས་པ་དེ་མཐར་ནི་ཉམས་པ་སྟེ་དེ་ལའོ། །

[Block 2374]
དེ་བས་ན་ཉམས་པའི༌[^2156]ཉེས་པ་སྤང་བའི༌[^2157]ཕྱིར།

[Block 2375]
འདུན་པ་ལ་སོགས་པ་ལེན་པ་དེས་ནམ་མཁའ་ལ་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་བསླབ་པའི་གཞི་བཅའ་བར༌[^2158]མཛད་དེ། །[^2159]འདིར་གཞུང་ནི་གླེང་གཞི་དག་ལས།

[Block 2376]
བཙུན་པ་དགེ་སློང་གི་འདུན་པ་བླངས་ཏེ། སྟེང་གི་ནམ་མཁའ་ལ་མཆིས་ན་འདུན་པ་འཚལ་ཏེ་མཆིས་ཞེས་བརྗོད་པར་བགྱིའམ། འཚལ་ཏེ་མ་མཆིས་ཞེས་བརྗོད་པར་བགྱི། ཉེ་བ༌[^2160]འཁོར་ཁྱེར་ཏེ་མ་འོངས་ཞེས་བརྗོད་པར་བྱ་སྟེ། ཡང་བླང་བར་བྱའོ། །

[Block 2377]
བཙུན་པ་དགེ་སློང་ཡོངས་སུ་དག་པ་ལེན་པས༌[^2161]ཡོངས་སུ་དག་པ་བླངས་ཏེ། སྟེང་གི་ནམ་མཁའ་ལ་འཚལ་ཏེ་མཆིས་ཞེས་བརྗོད་པར་བགྱིའམ། འཚལ་ཏེ་མ་མཆིས་ཞེས༌[^2162]བགྱི། ཉེ་བ༌[^2163]འཁོར་མ་འོངས་ཞེས་བརྗོད་པར་བྱ་སྟེ་ཡང་བླང་བར་བྱའོ་ཞེས་གསུངས་པ་དང་། ཞུ་བ་ལས་ཀྱང་ཡོངས་སུ་དག་པ་བླངས་ནས་མཚམས་ཀྱི་སླད་རོལ་ནས་མཆིས་ནས་ཡོངས་སུ་དག་པ་རྒྱུན་ཆད་པར་བརྗོད༌[^2164]པར་བགྱིའམ། རྒྱུན་མི་འཆད་པར༌[^2165]བརྗོད་པར་བགྱི་བཀའ་སྩལ་པ། རྒྱུན་ཆད་པར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2378]
འདི་ནི་དེས་འཇིགས་པས་མཚམས་ཀྱི་ཕྱི་རོལ་ནས་ཁྱེར་ཏེ་འོངས་པ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་གང་སྨོས་པ་དེའི་དམིགས་ཀྱིས་བསལ་བ༌[^2166]ཡིན་པར་རིག་པར༌[^2167]བྱའོ། །

[Block 2379]
གཅིག་ཏུ་རྐང་པ་ཡ་གཅིག་ལ་གཅིག་ཏུ་ཡ་གཅིག་ན་གཉིས་ཀར་གནས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མཚམས་གཅིག་ཏུ་གང་གི་རྐང་པ་ཡ་གཅིག་བཞག་ལ་མཚམས་གཅིག་ཏུ་རྐང་པ་ཡ་གཅིག་བཞག་ན་དེའི་མཚམས་དེ་གཉི་གར་གནས་པ་ཡིན་པའོ། །

[Block 2380]
ཐམས་ཅད་ནོན་པ་ལ་གནས་ན་ནོན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མཚམས་སུ་མ་ནོན་པའི་རྫས་ལ་གནས་པ་གང་ཡིན་པ་དེས་ནི་མཚམས་ཇི་ཙམ་ནོན་པ་ཉིད་ཡིན་པའི་རྫས་དེས་ནོན་པའི་མཚམས་དེ་ཐམས་ཅད་དུ་གནས་པ་ཉིད་ཡིན་ནོ། །

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
--- END BLOCKS ---
