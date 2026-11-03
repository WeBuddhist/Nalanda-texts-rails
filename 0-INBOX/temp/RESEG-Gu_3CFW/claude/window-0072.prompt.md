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
[Block 2521]
ཕྱིར་མི་འཆོས་པ༌[^2332]བསྟན་པ༌[^2333]སྨད་པར་བྱ་བའི་ལས་བྱའོ། །

[Block 2522]
ཚར་བཅད་ནས༌[^2334]ནན་ཏུར་གྱི༌[^2335]ལས་རིགས་པ་ཡིན་ཏེ། དག་པ་ལ་འཇུག་པར་གྱུར་པ་ལ༌[^2336]ནི༌[^2337]མ་ཡིན་ནོ་སྙམ་དུ་བྱས་ནས༌[^2338]སོ། །

[Block 2523]
ཁྱིམ་སུན་འབྱིན་པ་ལ་ནི་བསྐྲད་པའོ་ཞེས་བྱ་བ་ནི་གང་གི་ཁྱིམ་སུན་འབྱིན་པ་མ་བཏང་བ་དེ་གནས་དེ་ནས་བསྐྲད་པའི་ལས་བྱའོ། །

[Block 2524]
དེའི་ཕྱིར་འདུ་བ་མི་སྦྱིན་པ་དང་སྐབས་མི་འབྱེད་པ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་དེའི་ཕྱིར་ཞེས་བྱ་བ་ནི་གནས་ནས་བསྐྲད་པའི་ཕྱིར་རོ། །

[Block 2525]
གླེང་བའི་ཕྱིར་ཡོངས་སུ་རྫོགས་པས་དེའི་དོན་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2526]
འདུ་བ་མི་སྦྱིན་པ་དང་། སྐབས་མི་འབྱེད་པ་དག་ལ་གནས་ནས་སྐྲོད་པར༌[^2339]བྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2527]
དེ་མ་མཐོང་ངོ་ཞེས་ཟེར་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་སུན་འབྱིན་པ་སྟེ། མ་མཐོང་བ་ནི་དེ་མ་མཐོང་བའོ་ཞེས༌[^2340]ཟེར་ན་ཁྱིམ་སུན་འབྱིན་པ་དེ་ལ་བསྐྲད་པའི་ལས་བྱ་བ་ཁོ་ན་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2528]
ཁྱིམ་པ་ལ་བརྙས་ཐབས་བྱེད་པ་ལ་ནི་ཕྱིར་འགྱེད་པའོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་ལ་གང་གིས་ཐོ༌[^2341]འཚམ་པ་ནི་བརྙས་ཐབས་བྱེད་པ་སྟེ། དེ་ནི་ཁྱིམ་པ་ལ་བརྙས་ཐབས་བྱེད་པ་ཡིན་པས་དེ་ལ་ཕྱིར་འགྱེད་པའོ། །

[Block 2529]
བརྙས་ཐབས་སུ་བྱ་བ་མི་བདེན་པའི་ཕྱིར་རོ། །

[Block 2530]
དེ་ལྟར་ཡང་དེའི་མིང༌[^2342]གིས་བཟློག་པར་བྱ་བ་བདག་ཅག་གིས་ཁྱེད་ཀྱི་དྲུང་ནས་བསམ་པ་བཟློག་པར་བྱས་པས་སོ།[^2343] །ཇི་སྲིད་དུ་ཁྱེད་ཀྱི༌[^2344]ལས་ཀྱི་མཐའ་འདི་མ་བཏང་གི་བར་དུ་ཁྱེད་ཀྱི༌[^2345]ཡུལ་ལས་ངེད་ཀྱི༌[^2346]མཛའ་གཅུགས༌[^2347]ཀྱི་དངོས་པོ་དང་། དགའ་བའི་དངོས་པོ་ཕྱིར་བསྡུ་ཞིང་ངེད་ཕྱིར་འབྱེད༌[^2348]པར་བྱའོ་ཞེས་བྱ་བ་དེའི་དོན་ཏོ། །

[Block 2531]
འདི་ལ༌[^2349]བཟོད་པ་གསོལ་བའི་ལས་ཀྱི་གནས་སུ་དེ་ལ་བཟོད་པ་གསོལ་དུ་གཞུག་གོ་ཞེས་བྱ་བ་ནི། ཕྱིར་འགྱེད་པའི་ལས་འདི་ལ་བཟོད་པ་གསོལ་བའི༌[^2350]ལས་ཀྱི་གནས་སུ་ཁྱིམ་པ་དེ་ལ་བཟོད་པ་གསོལ་དུ་གཞུག་པ་ཡིན་པར་བལྟ་བར་བྱའི་འདིར་ལས་ནི་མི༌[^2351]བྱའོ། །

[Block 2532]
འོན་ཀྱང་གསོལ་བ་བྱ་སྟེ། ཁྱིམ་པ་ལ་གསོལ་དུ་གཞུག་པར་བྱ་སྟེ། ཁྱིམ་པས་བཟོད་པ་ཉིད་བཟོད་པ་བྱས་པ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 2533]
ལྟུང་བ་གྲགས་པ་ཕྱིར་མ་བཅོས་པ་བསྡམས་པས༌[^2352]ཕྱིར་བཅོས་སུ་མི་རུང་བ་དང་། མ་མཐོང་ངོ་ཞེས་ཟེར་ཞིང་ཕྱིར་འཆོས་པ༌[^2353]རྗེས་སུ་བསྒྲུབ་པར་མི་འདོད་པ་དང་སྡིག་པ་ཅན་གྱི་ལྟ་བ་མི་གཏོང་བ་ལ་ནི་གནས་ནས་དབྱུང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་ནི་གནས་ནས་དབྱུང་བ་རྣམས་ཀྱིས་དེ་ལ་ལྟུང་བ་གྲགས་པ་ཕྱིར་མ་བཅོས་པ་བསྡམས་པས་ཕྱིར་བཅོས་སུ་མི་རུང་བ༌[^2354]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2534]
དེ་ལ་མ་མཐོང་ངོ་ཞེས་ཟེར་ཞིང་ཞེས་བྱ་བ་ནི་མ་མཐོང་བས་གནས་ནས་དབྱུང་བ་བསྟན་ཏེ། དེའི་ཕྱིར་བཅོས་པ་རྗེས་སུ་བསྒྲུབ་པར་མི་འདོད་ཅིང་ཇི་ལྟར་ཆོས་བཞིན་ཕྱིར་བཅོས་པར་གྱིས་ཤིག་ཅེས་བྱ་བ་དེ་ལྟར་བརྗོད་པར་གྱུར་པ་ཇི་ལྟར་ལྟུང་བ་ཕྱིར་འཆོས་པའི་ཕྱིར་འཆོས་པ་རྗེས་སུ་བསྒྲུབ་པ་མི་འདོད་པ་ཞེས་བྱ་བས་ནི་མ་མཐོང་བ་གནས་ནས་དབྱུང་བའོ། །

[Block 2535]
ལྟུང་བ་སླར་མི་འཆོས་པའི་ཕྱིར་གནས་ནས་དབྱུང་བའི་ཕྲིན་ལས་མཛད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 2536]
ལྟ་བར་གཏོགས་པའི་ལྟུང་བྱེད་ལ་བརྗོད་པའི་རྣམ་པས་སྡིག་པ་ཅན་ཆོས་འདུལ་བ་ལས་དབྱུང་བར་གྱུར་པའི་ལྟ་བའི་རྣམ་པ་མི་གཏོང་བས་གནས་ནས་དབྱུང་བ་བསྟན་ཏོ། །

[Block 2537]
སྡིག་པ་ཅན་གྱི་ལྟ་བ་གཏོགས་པ་ལ་གནས་ནས་དབྱུང་བའི་ལས་འདི་བྱའོ། །

[Block 2538]
འདི་ཉིད་དུ་ལྟུང་བ་འདི་ཕྱིར་འཆོས་པར་གྱིས་ཤིག །དགེ་འདུན་འདི་ཉིད་ཀྱིས་ཁྱོད་ལ་བག་ཡངས་སུ་བྱེད་པར་འགྱུར་རོ་ཞེས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། ལྟུང་བ་བཅབ་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་རང་གི་ལྟུང་བའི་དབང་དུ་བྱས་པ་ཡིན་གྱི་གཞན་གྱི་འཆབ་པའི་ཉེས་པ་བསྟན་ཟིན་པའི་ཕྱིར་རོ། །

[Block 2539]
དགེ་འདུན་ལྷག་མ་འབའ་ཞིག་ཏུ་མ༌[^2355]ཟད་དེ། དེ་ལྟར་ཡང་གཞུང་ནི་བཙུན་པ་རེ་ཞིག༌[^2356]ལྟུང་བ་དང་བཅས་པ་དགེ་སློང་མ༌[^2357]མཆིས་པའི་གནས་ན་གནས་པས་གང་ལ་མི༌[^2358]བརྗོད་ན་བཅབས་པར་བརྗོད་པར་བགྱི་འམ། ཉེ་བ༌[^2359]འཁོར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ༌[^2360]ཡིན་ནོ། །

[Block 2540]
འདིར་ཞུ་བ་ལས་ཀྱང་ལྟུང་བ་བཅབས་པ་ཙམ་ལས༌[^2361]ལྡང་བ་ལ༌[^2362]དྲི་བ་རྣམས་བྱེད་པ་དང་། དེའི་ལན་ལྡོན་པ་ཡིན་ནོ། །

[Block 2541]
ཐ་ན་མིང་གོ་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་རྒྱ་ཆེར་གོ་བར་བྱེད་མ་ནུས་ན་ལྟུང་བ་སྡེ་ལྔ་པོ་དག་ལས་གང་བྱུང་བའི་མིང་ཙམ་ཡང་གོ་བར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 2542]
འདིར་གཞུང་ནི་བདག་ལ་ཕམ་པར་འགྱུར་བ་བྱུང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྷག་མ་དང་ལྟུང་བྱེད་བྱུང་ངོ་ཞེའམ། སོ་སོར་བཤགས་པར་བྱ་བའི་རིགས་བརྗོད་པ་མ་བྱས་པ་གང་ཡིན་པ་དང་། དགེ་སློང་སྟན་དེ་ཉིད་ལ་འདུག་པ་དེས་ཚེ་དང་ལྡན་པ་བདག་ལ་དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་བྱུང་ངོ་ཞེའམ། ལྟུང་བ་བྱུང་ངོ་ཞེས་བྱ་བའི་མིང་གིས་གསུངས་པ་ཡིན་ནོ། །

[Block 2543]
རྒྱ་ཆེར་གོ་བར་བྱ་བ་ཤིན་ཏུ་རིགས་མོད་ཀྱི་ཐ་ན་ལྟུང་བའི་མིང་ཡང་བརྗོད་པར་བྱ་བ་ཉིད་དོ། །

[Block 2544]
དེའི་གཞུང་ཡང་བཙུན་པ་བདག་གིས་བསླབ་པ་མ༌[^2363]ཕུལ་བར་མི་ཚངས་པར་སྤྱོད་པ་འཁྲིག་པའི་ཆོས་བརྟེན་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 2545]
དེ་ལྟ་བས་ན་ཐ་མའི་མཐར་ཐུག་པའི་དབང་དུ་བྱ་སྟེ། མིང་ཙམ་གྱིས་རིག་པར་བྱ་བ་ཉིད་དུ་གསུངས་པ་ཉིད་དུ་རྣམ་པར་གནས་པ་དེ་མདོ་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 2546]
ཉེས་བྱས་ནི་གང་ཡང་རུང་བས་སོ་ཞེས་བྱ་བ༌[^2364]ནི་ཉེས་བྱས་རིག་པར༌[^2365]བྱ་བ་ཉིད་ལ་ནི་བདག་ལ་ནི་ལྟུང་བ་བྱུང་ངོ་ཞེས་བྱ་བ་འམ།[^2366] བདག་གིས་ཁ་ན་མ་ཐོ་བ་བྱས་སོ་ཞེས་བྱ་བ་རྣམ་པ་གང་ཡང་རུང་བས་རིག་པར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 2547]
ལྟུང་བྱེད་གཞན་ལ་འདི་ལྟར་མིང་བརྗོད་པ་ཉིད་འབྱུང་བ་ཡིན་ཏེ། བདག་ཉིད་ཀྱི༌[^2367]སྨད་གཡོགས་ལ་ཐུན་མོང་བ་ཉིད་ཀྱི༌[^2368]ངོ་བོ་འདི་ལ་ཉེས་བྱས་མ་ཡིན་ནོ། །

[Block 2548]
དེ་དག་ལས་གང་ལ་རིག་པར་བྱ་བ༌[^2369]ཡིན་ཞེ་ན། དེའི་ཕྱིར་རང་བཞིན་དུ་གནས་པ་ལའོ་ཞེས་སྨོས༌[^2370]སོ། །

[Block 2549]
གང་གི༌[^2371]དྲུང་དུ་བཅབས༌[^2372]པ་མ༌[^2373]འཆགས་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་རང་བཞིན་དུ་གནས་པ་མཚམས་ཀྱི་ནང་ན༌[^2374]འདུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2550]
འདིར་གཞུང་ནི་ཞུ་བའི་གང་ཟག་གི་གཞི་ལས།

[Block 2551]
རང་བཞིན་དུ་གནས་པ་མཚམས་ཀྱི་ནང་ན་འདུག་པ་ལའོ་ཞེས་གསུངས་པ་དེ་འདིར་ལུང་ཡིན་ནོ། །

[Block 2552]
ཅི་ལྟ་བ་ལས་རང་གི་ཕྱོགས་མ་ཡིན་པའང་རང་བཞིན་དུ་གནས་པ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ལྟ་བ་ཐ་མི་དད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་མ་རྫོགས་པ་དང་མ༌[^2375]བསྙིལ་བ་ཡང་དག་པར་སྡོམ་པ་དང་། ཁྱིམ་པ་ཡང་དག་པར་སྡོམ་པ་ཡང་རང་བཞིན་དུ་གནས་པ་ཉིད་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་བསྙེན་པར་རྫོགས་པ་དང་བཅས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་གིས་ཀྱང་དགེ་སློང་མ་ལ་རིག་པར་བྱ་བ་ཉིད་ཡིན་ལ། དགེ་སློང་མས་ཀྱང་དགེ་སློང་ལ་རིག་པར་བྱ་བ་ཉིད་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་མཚན་མཐུན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལ་རིག་པར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 2553]
རིགས་མཐུན་པས་རིག་པར་བྱ་བ་ཉིད་དང་བཤགས་པ་ལ་སོགས་པ༌[^2376]བྱ་བ་ཉིད་དམ་ཞེ་ན། དེའི་ཕྱིར་དེ་ཉིད་ལ་འདི་དང་འོག་མ་དང་བཅས་ཏེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྟུང་བར་རིག་པར་བྱ་བ་འདི་ཉིད་ལྟུང་བ་བཤགས་པར་བྱ་བ་ནས་འོག་ནས་བྱུང་བ་དང་བཅས་ཏེ་བྱའོ། །

[Block 2554]
དེ་ཉིད་ལ་ཞེས་བྱ་བ་ནི་རང་བཞིན་དུ་གནས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་བྱེ་བྲག་དང་བཅས་པས་གང་ཟག་ལ་རིག་པར་བྱའོ། །

[Block 2555]
རབ་ཏུ་བྱུང་བ་བསྙེན་པར་མ་རྫོགས་པ་དག་ནི་བསྙེན་པར་རྫོགས་པའི་དགེ་འདུན་གྱིས་ཡོངས་སུ་བཟུང་བ་ཙམ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་དེ་རྣམས་ནི་ཐམས་ཅད་དུ་རག་ལས་པ་ཁོ་ན་ཡིན་པར་རྣམ་པར་གནས་སོ། །

[Block 2556]
དེ་ལྟར་ཡང་རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་མ༌[^2377]རྫོགས༌[^2378]པ་དག་གིས་དགེ་འདུན་ལ་དགག་དབྱེ་བྱའོ་ཞེས་གསུངས་པ་ལས་ཤེས་སོ། །

[Block 2557]
ཆོས་འདི་པ་ལ་དེ་བྱས་ན་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། ཆོས་འདི་བ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པ༌[^2379]མཚན་མི་མཐུན་པ་དང་། རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་མ་རྫོགས་པ་དང་། ཁྱིམ་པ་དེ་བཞིན་གཤེགས་པའི་ཆོས་ཀྱི་ལྟ་བ་ཅན་ཐམས་ཅད་བསྡུས་ཏེ། ཆོས་འདི་པ་དེ་དག་ལ་ལྟུང་བ་རིག་པར་བྱ་བ་དེ་བྱས་ནས༌[^2380]ཡང་བྱས་པ་ཉིད་དེ། དེ་རིག་པར་བྱས་ན་བཅབས་པར་མི་འགྱུར་རོ། །

[Block 2558]
དེ་ལ་འདིར་བྱ་བ་ནི་དགེ་འདུན་གྱི་ཡུལ་ལ་མ་གུས་པ་སྤང་བའི་ཕྱིར་ཏེ། མི༌[^2381]རིགས་པ་སྤངས་པར་གསུངས་སོ། །

[Block 2559]
འོ་ན་མདོ་འདི་ཅིའི་ཕྱིར་བྱས་ཤེ་ན། མ་བརྗོད་པ་བརྗོད་པར་བྱ་བའི་ཕྱིར་ཏེ། དེ་བས་ན་མཚན་མི་མཐུན་པ་བསྙེན་པར་རྫོགས་པ་དག་ལ་རིག་པར་བྱེད་ན་ཡང་བཅབས་པར་མི་འགྱུར་ལ། །རིག་པར་བྱེད་པ་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 2560]
འདིར་གཞུང་ནི་ཉེ་བ༌[^2382]འཁོར་གྱིས་ཞུས༌[^2383]པའི་གང་དག་གི༌[^2384]གཞི་ལས།
--- END BLOCKS ---
