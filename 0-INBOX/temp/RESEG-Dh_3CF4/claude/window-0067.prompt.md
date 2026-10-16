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
སེམས་ཞེས་བྱ་བ་སྨོས་པས་ནི་ཐབས་ལ༌[^1483]མཁས་པའི་རྣམ་པ་སྟེ། མཁས་པའི་རྣམ་པ་ནི་ཤེས་རབ་སྟེ། དེ་ཡང་སེམས་རྩེ་གཅིག་པས་བྱས་པར་བསྟན་པའི་ཕྱིར་གཉི་ག་སྨོས་སོ། །

[Block 2347]
དོན་ཡང་སྤྱོད་ཅེས་བྱ་བ་འདིས་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 2348]
འགྲོ་ལ་ཕན་སེམས་ཞེས་བྱ་བ་འདིས༌[^1484]ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། བསམ་གཏན་དང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་གཉིས་ཀྱིས་སོ། །

[Block 2349]
བག་མེད་པའི་དབང་གིས་ཁ་ཅིག་ཏུ་ཐན་པ་འབྱུང་བས་འཁྲུག་ཅིང་གནོད་པར་གྱུར་ཏོ་ཞེས་བྱ་བ་ལ། ཆར་འབབ་མི་མཁས་པས་ཁ་ཅིག་ཏུ་ཐན་པ་འབྱུང་བ་དེས་འཁྲུགས༌[^1485]པའོ། །

[Block 2350]
གང་དག་ཅེ་ན། སེམས་ཅན་རྣམས་སོ། །

[Block 2351]
ཆོས་ལེགས་པར་མ་སྤྱད་པ༌[^1486]ཞེས་བྱ་བ་ལ། ངན་པར་སྤྱད་པ་ནི་ལེགས་པར་མ་སྤྱད་པ་སྟེ། དེ་བས་ན་མ་རུངས་པར་གྱུར་པ་ནི་གོམས་པར་གྱུར་པའོ། །

[Block 2352]
དེའི་སྡུག་བསྔལ་ནི་འགྲོ་བའི་སྡུག་བསྔལ་ལོ། །

[Block 2353]
དེ་ལས་ཐར་པར་བྱ་བའི་ཐབས་ནི་སྐྱེ་དགུ་རྣམས་སྡུག་བསྔལ་ལས་འདོན་པའི་ཐབས་སོ། །

[Block 2354]
རྣམ་པ་དུ་མའི་སྲོག་ཆགས་དག་ནི་སྲོག་ཆགས་དུ་མའོ། །

[Block 2355]
དེ་དག་གསོད་ཅིང་འཇིགས་འཇིགས་སྐད་ཟེར་བའི་སྲོག་ཆགས་དུ་མ་གསོད་པར་རྩོམ་པ་དེ་གང་དུ་གནོད་སྦྱིན་ནོ། །

[Block 2356]
ཡིད་ལ་འབབ་པ་ཞེས་བྱ་བ་ནི་བསམ་པའོ། །

[Block 2357]
ངོ་ཟློགས༌[^1487]ཕོད་པ་ཉིད་ཚིག་རྩུབ་པ་ཡིན་པས་ངོ་ཟློགས༌[^1488]ཕོད་པའི་ཚིག་རྩུབ་པོ། །ཡང་ན་ངོ་ཟློགས༌[^1489]ཕོད་པའམ་ཚིག་རྩུབ་པོ་ནི་ངོ་ཟློགས༌[^1490]ཕོད་པའི་ཚིག་རྩུབ་པའོ། །

[Block 2358]
སེལ་བར་བྱེད་པ་ནི་གཅོད་པར་བྱེད་པའོ། །

[Block 2359]
ཆོས་ཀྱི་གཏམ་ཉིད་ནི་ཆོས་ཀྱི༌[^1491]གཏམ་མོ། །

[Block 2360]
ཆོས་ཀྱི་གཏམ་གྱི་སྐབས་ནི་ཆོས་ཀྱི་གཏམ་བྱ་བའི་སྐབས་ཏེ། དེའི་སྐབས་ཀྱི་གོ་སྐབས་རྙེད་པ་གང་ཡིན་པ་དེ་ནི་ཆོས་ཀྱི་གཏམ་བྱ་བའི་སྐབས་རྙེད་པའོ། །

[Block 2361]
བསམ་པ་ནི་མངོན་པར་སེམས་པའོ། །

[Block 2362]
གང་དུ་དུས་ལས་མི་འདའ་བ་ནི༌[^1492]གང་གི་ཚེ་དམིགས་པ་ཡོངས་སུ་སྲུང་བར་བྱེད་པ་དེའི་ཚེ་སྙིང་རྗེ་བས་སོ། །

[Block 2363]
དེ་དག་ས་གཞི་ལེགས་པར་ཡོངས་སུ་སྐྱོང་བའི་བྱ་བ་གང་ཡིན་པ་དེ་དག་ནི་བགྱི་བ་སྟེ། བགྱི་བ་ལས་མི་འདའ་བའོ། །

[Block 2364]
རིམ་པ་གང་གིས་བྱ་བ་དེ་ནི་དུས་ལས་མི་འདའ་བའོ། །

[Block 2365]
ཆོས་དང་བདེ་བ་བཞིན་ཞེས་བྱ་བ་ནི་དུས་ལས་ཀྱང་མི་འདའ་བ་སྟེ། དེ་དག་གི་ཆོས་དང་བདེ་བ་རྣམས་ལས་མི་འདའ་བ་དེ་བཞིན་ནོ། །

[Block 2366]
འཁོར་གསུམ་བསྟན༌[^1493]ལ་མཁས་པར་གྱུར་པ་དང་། །ཞེས་བྱ་བ་བསྟན་མ་ཐག་པའི་ཚིགས་བཅད་དུ་ཇི་སྐད༌[^1494]བཤད་པའོ། །

[Block 2367]
དེ་བཞིན་དུ། །འབངས་ལ་ཕན་ཕྱིར་གནམ་རུ༌[^1495]བསྣམས་པ་དེ། །ཞེས་བྱ་བ་ནི། ལྟ་བ་ངན་པས་ཉམས་པའི་སྐྱེ་དགུ་དག །ཅིའི་ཕྱིར་ཡལ་བར་དོར་ཞེས་བྱ་བ་དང་སྦྱར་བར་བྱའོ། །

[Block 2368]
མཐོ་རིས་འདོད་པས་འདི་སྐད་སྟོན་ཏེ། མཐོ་རིས་ཐེམ་སྐས་ཞེས་བྱ་བ་ནི་མཐོ་རིས་ཀྱི་ལམ་མོ། །

[Block 2369]
བག་མེད་པ་ཉིད་ལམ་ཡིན་པས་བག་མེད་པའི་དབང་ངོ་། །མཐོ་རིས་ཀྱི་ཐེམ་སྐས་དེ་ལ་བག་མེད་པའི་དབང་གིས༌[^1496]ཡུན་རིང་པོར་ལྷན་ཅིག་ཏུ་བག་མེད་པའི་དབང་དུ༌[^1497]གྱུར་པའོ། །

[Block 2370]
བག་མེད་པའི་དབང་གིས་ནི་མཆོད་སྦྱིན་བྱ་བའི་དུས་ལས་འདས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 2371]
ཁྱོད་ཀྱི་བཀའ་ནི༌[^1498]ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་བརྩམས་པ་ནི་གལ་ཏེ་འདི་ལྟར་ཡང་འགྱུར་ཏེ། མ་ཐོབ་པ་ཐོབ་པར་འདོད་པ་དང་ལྷག་མ་ཡོད་དོ་ཞེས་པ་མེད་པ་དེ་མེད་པར༌[^1499]བསྟན་པའི་ཕྱིར་རོ། །

[Block 2372]
ཡང་ན་སྟོབས་དང་ལྡན་པས༌[^1500]ཀུན་ནས་རྣམ་པར་འགལ་བ་དེ་མེད་པ་སྟེ།[^1501] མཆོད་སྦྱིན་དང་འགལ་བར་བརྩམས་པར་མི་འགྱུར་རོ་ཞེས་བསྟན་ཏོ། །

[Block 2373]
ཡང་ན་ཡོངས་སུ་སྲུང་བ་རྣམ་པར་སྤེལ་བའི༌[^1502]སྐབས་ཐོབ་པའི་ངོ་བོ་བསྟན་ཏེ། གང་གི་ཕྱིར་རྒྱལ་ཕྲན་དག་བཀའ་བཞིན་དུ་བྱེད་པ་དེ་དང་ལས་གང་ཐོབ་པ་ལ་སོགས༌[^1503]རྙེད་པའོ། །

[Block 2374]
ཡོངས་སུ་སྲུང་བ་ལས་བྱུང་བ་ཡང་བསྟན་ཏོ། །

[Block 2375]
ད་ནི་སྟེགས་མང་པོ་ལ་སྒྲུབ་པ་ཙམ་གྱིས༌[^1504]ལྷག་མ་དེའི་སྐབས་འདི་ཞེས་བསྟན་ཏོ། །

[Block 2376]
ལེགས་པ་དག་ཅེས་བྱ་བ་ནི་བསོད་ནམས་ཏེ། མངོན་པར་མཐོ་བའི་རྒྱུར་གྱུར་པས་སྟེགས་ལ་རབ་ཏུ་སྒྲུབ་པ་ནི་ལེགས་པ་ཞེས་བརྗོད་དེ། འདིས་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་འབྲས་བུ་ཆེན་པོ་ཉིད་དོ། །

[Block 2377]
གྲགས་འབར་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་འབྲས་བུ་ཉིད་དོ། །

[Block 2378]
དུས་ལ་བབ་ཅེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་བག་མེད་དབང་གྱུར་ཞེས་བྱ་བ་དེའི་གཉེན་པོས་དུས་དེ་ལས་མི་འདའ་བས་ལས་ལ་གཟུང་བ་ཡིན་ནོ། །

[Block 2379]
སྦྱིན་པ་མཛད་ཅིང་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་འདི་ལྟར་འགྱུར་ཏེ། རྟག་ཏུ་དབང་བསྐུར་ཞིང་རྒྱུན་དུ་དབང་བསྐུར་བ་ཉིད་དེ། སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2380]
འོན་ཀྱང་ཞེས་བྱ་བ་ནི་བྱ་བ་གཞན་དག་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2381]
དབང་བསྐུར་ཀྱང་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་དབང་བསྐུར་བར༌[^1505]གྱུར་ཀྱང་ངོ་། །ལྷ་ཡི་བུ་ལོན་བྲལ་བར་མཛད་པའི་རིགས།[^1506] །ཞེས་བྱ་བ་འདིས་ནི་རང་གི་དོན་ཕུན་སུམ་ཚོགས་པ་འགྲུབ་པའི་དབང་དུ་བྱས་ནས་བརྩམས་པའི་ཁྱད་པར་བསྟན་ཏོ། །

[Block 2382]
ད༌[^1507]ནི་སྐྱེ་དགུ་རྣམས་ཀྱི་ཕུན་སུམ་ཚོགས་པ་འགྲུབ་པའི་དབང་དུ་བྱས་ནས་མཆོད་སྦྱིན་ལེགས་པར་བགྱིས་པས་ཞེས་བྱ་བའི༌[^1508]ཚིགས་བཅད་དོ། །

[Block 2383]
དེ་བས་འབངས་ལ་ཕན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་མཆོད་སྦྱིན་ལེགས་པར་བྱས་པས་ལྷ༌[^1509]མཉེས་པར་གྱུར་ཏེ་ཆར་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2384]
བདག་ལ་ཕན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་དགྲ་ལས་རྣམ་པར་གྲོལ་བའོ། །

[Block 2385]
གྲགས་པར་འགྱུར་བའི་ཞེས་བྱ་བ་ནི་གཉིས་ཀར་གྲགས་པར་འགྱུར་བ་ཉིད་ཀྱི་མཆོད་སྦྱིན་གྱི་ཆོ་གའོ། །
--- END BLOCKS ---
