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
[Block 3396]
ཁང་པའི་དགེ་འདུན་ལྷག་མ་པ༌[^2346]ཡན་ལག་གཞན་གཉིས་བརྗོད་པར་བྱ་སྟེ། གཅིག་གི་དོན་དུའོ་ཞེས་བྱ་བ་ནི་གང་ཟག་གཅིག་གི་དོན་དུ་བྱེད་དུ་འཇུག་ན་དགེ་འདུན་ལྷག་མར་འགྱུར་གྱི་གཉིས་དང་མང་པོ་དག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3397]
འདིར་གཞུང་ནི་ཉེ་བ་འཁོར་གྱིས་ཞུས་པའི་གཞུང་ཁ་ཅིག་ལས།

[Block 3398]
[^2347] གཉིས་ཀྱིས་སྤྱི་ལ་བྱེད་དུ་འཇུག་ན་སྦོམ་པོར་རོ་ཞེས་འབྱུང་ངོ་། །འདིར་མང་པོའི་དོན་དུ་ནི་ཉེས་པ་མེད་པ་ཉིད་རིགས་པ་ཡིན་ཏེ། དགེ་འདུན་གྱི་དོན་ཉིད་དུ་ནི་ཉེས་བྱས་སུ༌[^2348]བརྗོད་པའི་ཕྱིར་དངོས་གཞི་ནི་མ་ཡིན་ནོ། །

[Block 3399]
འདིར་ཤིན་ཏུ་འབྱུང་བར་འདོད་པ་དང་འབྲེལ་པ་ལ་གནས་པས་ཉེས་བྱས་ཙམ་ནི་མ་ཡིན་ནོ། །

[Block 3400]
ལྟུང་བ་བྱེད་པའི་དངོས་པོ་ཐམས་ཅད་ལ་ཡན་ལག་འདའ་བར་བྱེད་པ་ལ་སྦོམ་པོའི་ལྟུང་བ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3401]
དེ་བས་ན་གཉིས་ལ་སོགས་པ་དུ་མ་ཉིད་ལ་འདི་བསྟན་པ་ནི༌[^2349]འདིར་གཉིས་ཀྱི་ཚིག་རྣམ་པར་གནས་པ་ཞེས་བྱ་བ་གཅིག་པ་ཉིད་ཀྱི་གཙོ་བོ་འདི་ཤེས་པ་ཡིན་ནོ། །

[Block 3402]
དེ་བས་ན་བདག་ཉིད་གཅིག་པུ་འམ་དགེ་སློང་གཞན་གཅིག་གམ། ཁྱིམ་པ་གཅིག་གི་དོན་བྱེད་དུ་བཅུག་ན་དགེ་འདུན་ལྷག་མ་སྟེ་ཞེས་བྱ་བ་བྱེ་བྲག་ཏུ་མ་བྱས་པའི་ཕྱིར་རྟོགས་པར་བྱའོ། །

[Block 3403]
ཅི་གནས་བྱེད་དུ་བཅུག་པ་ཐམས་ཅད་ལས་དེར་འགྱུར་རམ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་ཚད་ལས་ལྷག་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚད་ལས་འདས་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3404]
གཞི་མ་དག་པ༌[^2350]ལའོ་ཞེས་སྨོས་ན་འདིར་མ་དག་པ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མི་རུང་བ་ཉིད་དང་རྩོད་པ་དང་བཅས་པ་ཉིད་དང་བརྩམ་དུ་མི་རུང་བ་ཉིད་ནི་མ་དག་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་གསུམ་གྱི་རང་བཞིན་ཇི་ལྟར་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་སྐྱེ་བ་པོ་ཕྲ་མོའི་གནས་དང་ལྡན་པ་ཉིད་དང་རྒྱལ་པོ་དང་ལྷའི་གནས་དང་། མུ་སྟེགས་ཅན་གྱི་འདུག་གནས་ལ་བརྟེན་པ་ཉིད་དང་། ཤིང་ལྗོན་པ་གཅད་པར༌[^2351]བྱ་བ་མ་ཡིན་པ་ཉིད་དང་། ཕྱི་རོལ་འདོམ་གང་གི༌[^2352]མཐའི་ཉེན་ཀོར༌[^2353]གྱི་ནང་རོལ་དུ་ཆུ་ཀླུང་ངམ་ངམ་གྲོག་གམ་ཁྲོན་པ་དང་འདོམ་པ་ཉིད༌[^2354]ནི་གོ་རིམས་བཞིན་དུ་དེ་དག་ཡིན་ནོ་ཞེས་སྨོས་ཏེ། དེ་ལ་སྐྱེ་བ་པོ་ཕྲ་མོའི་གནས་དང་ལྡན་པ་ཉིད་དང་འདོམ་པ་ཉིད་ནི་མི་རུང་བ་ཉིད་དང་། རྒྱལ་པོའི་གནས་ལ་སོགས་པར་བརྟེན་པ་ཉིད་དང་། ཤིང་ལྗོན་པ་གཅད་པར༌[^2355]བྱ་བ་མ་ཡིན་པ་ཉིད་ནི་རྩོད་པ༌[^2356]དང་བཅས་པ་ཉིད་དང་། ཕྱི་རོལ་ཞེས་བྱ་བ་ལ་སོགས་པ་བརྩམ་དུ་མི་རུང་བ་ཉིད་དོ། །

[Block 3405]
འདིར་གཞུང་ནི་གལ་ཏེ་དེ་ན་སྐྱེ་བ་པོ་ཕྲ་མོའི་གནས་དང་སྦྲུལ་གྱི་གནས་སམ། སྡིག་པའི་གནས་སམ། སྦྲང་བུ་ཏྲེ་མ་བུ་ཀ༌[^2357]དང་ཏྲཻ་ལ་ཏ་ཀའི་གནས་ཡོད་པ་ཉིད་དོ་ཞེས་གསུངས་པ་ཉིད་དོ། །

[Block 3406]
འདིར་སྦྲུལ་ལ་སོགས་པ་སྐྱེ་བ་ཕྲ་མོ་རྣམས་ནི་དཔེ་ཙམ་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3407]
དེ་བས་ན་འདི་རྣམས་ཐམས་ཅད་ཁོངས་སུ་བསྡུ་བར་བྱའོ།[^2358] །རྒྱལ་པོའི་གནས་ལ་སོགས་པ་ལ་བརྟེན་པ་ཉིད་ནི་དེའི་དྲུང་དུ་འགྲོ་བ་ཉིད་དོ། །

[Block 3408]
འདིར་མཐོ་བཙམས་པ༌[^2359]ལས་འབྱུང་བའི་ཉེས་པའོ། །

[Block 3409]
སྒྲ་དེ་དང་དེའི་དབང་གིས་བྱུང་བའི་སྲོག་ཆགས་རྣམས་དང་རྫས་གཞན་རྣམས་ཀྱིས་ཀྱང་ངོ་། །འདིར་རྣམ་པར་མཐོ་བཙམས་པ༌[^2360]ནི་གནོད་པའོ། །

[Block 3410]
ཤིང་ལྗོན་པ་གཅད་པར༌[^2361]བྱ་བ་མ་ཡིན་པ་ཉིད་དང་ཞེས་བྱ་བ་ནི་གཅད༌[^2362]པར་འོས་པ་མ་ཡིན་པ་ནི་འདིར་ཤིང་ཞེས༌[^2363]འཇིག་རྟེན་པ་དག་ལ་མཁོ་བ་ཡིན་པའི་ཕྱིར་ཁ་མཆུ་འབྱུང་བ་མི་རྩོམ་པའོ། །

[Block 3411]
ཡུན་ཐུང་བར་གནས་པ་ཉིད་ཀྱིས་དགོས་པ་ཆུང་བ་ཉིད་དོ། །

[Block 3412]
རྣམ་པར་གནོན་པ་མ་ཡིན་པ་ཉིད་ཙམ་དུ་མི་རུང་བ་ཉིད་ཀྱི་སྐྱོན་ནོ། །

[Block 3413]
ཕྱོགས་གཅིག་པ༌[^2364]ཡང་འདོམ་སྟེ་དེའི་གང་ཞིག་ཉེན་ཀོར༌[^2365]གྱི་ནང་རོལ་དེ་མ་ཐག་པ་གཞན་གྱིས༌[^2366]ཉེ་བར་ལོངས་སྤྱོད་པ་དེའི་ཕྱི་རོལ་ཉིད་དུ་འཛིན་པ་ཉིད་མ་ཡིན་པ༌[^2367]ཇི་ཙམ་པ་དེ་ཙམ་གྱི་ཕྱོགས་ལའོ། །

[Block 3414]
གཅིག་གིས་ཀྱང་ཆུ་ཀླུང་ལ་སོགས་པ་རྣམས་ལ་ཉེས་པ་འདི་ཡིན་ནོ། །

[Block 3415]
འདིར་གཞུང་ནི་འདོམ་གང་གི་མཐའི་ཉེན་ཀོར༌[^2368]བརྟག་པར་བྱ་སྟེ། གལ་ཏེ་གཞི་ཆུ་ཀླུང་ལ་བརྟེན་ནམ་ངམ་གྲོག་ལ་བརྟེན་པ་ཡིན་ན་བརྩམ་དུ་མི་རུང་བའི་ཕྱིར་བསྟན་པར༌[^2369]མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3416]
གང་ལས་འདས་ན་གནས་ཚད་ལས་འདས་པར་གྱུར་པའི་ཚད་དེ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཚད་དང་ལྡན་པའི་ཁྲུ་ཕྱེད་དང་དོ་ནི་བདེ་བར་གཤེགས་པའི་མཐོ་གང་སྟེ། ནང་རོལ་ནས་དེ་བཅུ་གཉིས་དང་བདུན་གྱི་ཚད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཞེས་བྱ་བ་ནི་འདི་ཙམ་གྱི་ཚད་དེ་ལའོ། །

[Block 3417]
བདེ་བར་གཤེགས་པའི་མཐོ་གང་ཞེས་བྱ་བ་ནི་དཀྱུས་སུའོ། །

[Block 3418]
ནང་རོལ་དུ་ནི་དེ་བཅུ་གཉིས་ཏེ།[^2370] རྒྱར་ནི་བདུན་གྱི་ཚད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3419]
དེ་ལས་བཟློག་པ་ཉིད་ནི་མ་བསྟན་པ་ཉིད་དོ་ཞེས་སྨྲས་ན་བསྟན་པ་ཉིད་དེ་གང་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་ལ་བསྟན་པ་ཐོབ་པ་ཉིད་ནི་བསྟན་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཤིན་ཏུ་གཏོང་བར་གྱུར་པའི་གཞི་དེའི༌[^2371]ལས་ལ་མངོན་པར་རྗེས་སུ་གནང་བར་གྱུར་པའི་ཚིག་ནི་བསྟན་པ་སྟེ། གཞི་གང་ལས་དགེ་འདུན་ལ་ཐོབ་པ་དེ་ནི་བསྟན་པ་ཞེས་བྱ་བར་འདིར་འདོད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3420]
མ་དག་པ་གསོལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཞི་མི་རུང་བ་ཉིད་ལ་སོགས་པ་དང་ལྡན་པ་དང༌[^2372]མ་དག་པ་དགེ་འདུན་ལས་བསྟན་པ་གསོལ་བར་མི་བྱའོ། །

[Block 3421]
རང་དག་རྟོག་ཏུ་དོང་བར་བྱའོ། །

[Block 3422]
ཡང་ན་དགེ་སློང་བསྐོས་པ་དག་གོ་ཞེས་བྱ་བ་ནི་གང་དག་ལ་གཞི་བསྟན་པ་ལ་གསོལ་པ་དེ་རྣམས་རང་གི་རྐྱེན་གྱིས་དངོས་པོའི་དག་པ་ཉིད་ཤེས་པར་འགྱུར་བ་འམ། རང་ཉིད་ཀྱིས་བསྐོས་པའི་དགེ་སློང་རྣམས་ཀྱི་རྐྱེན་གྱིས༌[^2373]ཤེས་པར་འགྱུར་རོ། །

[Block 3423]
སྟན་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་རྙིང་པ༌[^2374]ཉིད་ཀྱི་ཕྱིར་ལོ་དྲུག༌[^2375]ཚུན་ཆད་དུ་སྟན་བྱ་བའི་ཕྱིར་གནང་བ་གསོལ་བར་བྱེད་ན་བསྟན༌[^2376]ལ་རང་གི་རྐྱེན་གྱིས་ཤེས་པར་འགྱུར་བ་འམ་གསོལ་བའི་དགེ་སློང་རྣམས་ཀྱིས་ཞེས་བྱ་བ་འདི་རྟོགས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3424]
བྱས་པ་རྙེད་པ་དང་བྱས་པ་ལ་ལོངས་སྤྱོད་པ༌[^2377]དག་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་རྙེད་པར་བྱས་པའམ་ལོངས་སྤྱད༌[^2378]པར་བྱས་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 3425]
འདི་ལ་བདག་ཏུ་བྱས་པའི་དབང་གིས་ཁ་ན་མ་ཐོ་བ་མེད་དོ། །

[Block 3426]
ལྷག་པར་གནས་པའི་དབང་གིས་མ་ཡིན་ནོ༌[^2379]ཞེས་བྱ་བ་འདི་བསྟན་པའི་ཕྱིར་ཚིག་འདིའོ། །

[Block 3427]
རྙིང་པ༌[^2380]མ་འཆོས་པ་ལ་སོགས་པ༌[^2381]ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་ལྟུང་བ་མེད་དོ་ཞེས་སྦྱར་རོ། །

[Block 3428]
འདིར་གསར་པ་བརྩིག་པ་ལ་ནི་སྐྱོན་ཏེ། རྙིང་པ་མ༌[^2382]འཆོས་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3429]
དེ་བས་ན་རྙིང་པ་མ་ཡིན་པ་མ༌[^2383]འཆོས་པ་ལ་ཡང་ལྟུང་བ་མེད་དེ། འདིར་རྙིང་པའི་ཚིག་སྨོས་པ་ནི་དཔེར་ན་རིག་པར་བྱའོ། །

[Block 3430]
ཁང་པའི་དགེ་འདུན་ལྷག་མའོ།། །།

[Block 3431]
གང་བྱས་ན་གཙུག་ལག་ཁང་གི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། འདིར་འོག་མ་ལ་ཡང་དེ་དག་ཉིད་དེ། དེ་མ་བཙལ་བ་ཉིད་དོ་ཞེས་བྱ་བ་སྔར་བསྟན་པའི་ཆོ་ག་ལ་ལྟོས་ནས་བྱེ་བྲག་བརྗོད་པར་བྱ་སྟེ། ཚོགས་ཀྱི་དོན་དུའོ་ཞེས་བྱ་བ་ནི་འདིར་ཁྱིམ་པ་ཡན་ཆད་ཀྱི་གང་ཟག་བཞི་ལ་སོགས་པ་ཚོགས་ཞེས་བྱ་བ་མངོན་པར་འདོད་པར་རིག་པར་བྱའོ། །

[Block 3432]
ཤིན་ཏུ་སྡིག་པ་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་ཁྱིམ་པའི་དོན་ཉིད་ཀྱི་བསམ་པ་ལ་འཕགས་པའི་དགེ་འདུན་རྗེས་སུ་གཟུང་བའི་བསམ་པ་ལ་ཤིན་ཏུ་དགེ་བ་ཉིད་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 3433]
གང་ཞིག་ཚོགས་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་ཉན་ཐོས་ཀྱི་དགེ་འདུན་ནོ་ཞེས་གསུངས་པ་དེ་ནི་གླེང་གཞིའི་དབང་གིས་དེ་དཔེ་ཙམ་དུ་ཟད་པར༌[^2384]འདི་ལ་ཉེས་པ་མེད་དོ་ཞེས་རིག་པར་བྱའོ། །

[Block 3434]
གཙུག་ལག་ཁང་གི་དགེ་འདུན་ལྷག་མའོ།། །།

[Block 3435]
རྩོམ་པ་ཉིད་ནི་སྦྱོར་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མཐར་ཐུག་པ་གང་ལ་དངོས་གཞིའི་ཚད་འདའ་བར་བྱེད་པ་ཉིད་ལ་ཐམས་ཅད་དུ་ཡན་ལག་ལྷག་མ་རྣམས་ལ་འདའ་བར་བྱེད་པ་དང་། སྦྱོར་བ་ཉིད་ལ་དེར་འདི་རྣམས་སྦོམ་པོར་སྟོན་པར་བྱེད་པའི་ཚིག་རྣམས་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །
--- END BLOCKS ---
