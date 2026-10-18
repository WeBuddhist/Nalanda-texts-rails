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
[Block 2486]
དེའི་ངོ་བོ་ནི་གཟུགས་མེད་པ་ཉིད་དོ། །

[Block 2487]
དེ་དང་ལྡན་པའི་ཁམས་ནི་གཟུགས་མེད་པའི་ཁམས་སོ། །

[Block 2488]
ཡང་ན་འདོད་པ་རྣམས་ཀྱི་ཁམས་ནི་འདོད་པའི་ཁམས་ཏེ། གང་ཞིག་འདོད་པ་རྣམས་འཛིན་པའོ། །

[Block 2489]
གཟུགས་དང་གཟུགས་མེད་པའི༌[^1297]ཁམས་དག་ཀྱང་དེ་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 2490]
འདོད་པ་ཞེས་བྱ་བ་འདི་ཅི་ཡིན་ཞེ་ན། མདོར་བསྡུ་ན་ཁམ་གྱི༌[^1298]ཟས་དང་། འཁྲིག་པ་དང་ལྡན་པའི་འདོད་ཆགས་ཡིན་ཏེ།

[Block 2491 [VERSE]]
འཇིག་རྟེན་སྣ་ཚོགས་གང་ཡང༌[^1299]འདོད་པ་མིན། །
སྐྱེས་བུའི་ཀུན་རྟོག་འདོད་ཆགས་འདོད་པ་ཡིན། །
འཇིག་རྟེན་དག་ན་སྣ་ཚོགས་དེ་བཞིན་གནས། །
འོན་ཀྱང་རྟེན༌[^1300]རྣམས་འདི་ལ་འདུན་པ་འདུལ། །

[Block 2492]
ཞེས་ཚིགས་སུ་བཅད་དེ་གསུངས་པའི་ཕྱིར་རོ།[^1301] །ཀུན་ཏུ་རྒྱུ་འཚོ་བྱེད་ཀྱིས༌[^1302]འཕགས་པ་ཤཱ་རིའི་བུ་ལ།

[Block 2493 [VERSE]]
འཇིག་རྟེན་སྣ་ཚོགས་གང་དེ་འདོད་མིན་གྱི། །
ཀུན་རྟོག་འདོད་ཆགས་འདིར་འདོད་ཡིན་སྨྲ་ན། །
དེ་ནི་མི་དགེའི་རྟོག་པ༌[^1303]ཀུན་རྟོག་ཚེ། །
དགེ་སློང་ཡང་ནི་འདོད་སྤྱོད་ཅན་དུ་འགྱུར། །

[Block 2494]
ཞེས་སྨྲས་པ་དང་། འཕགས་པ་ཤཱ་རིའི་བུས།

[Block 2495 [VERSE]]
གལ་ཏེ་འཇིག་རྟེན་སྣ་ཚོགས་གང་དེ་འདོད། །
ཅི་སྟེ་ཁྱོད་ཀྱི་ཀུན་རྟོག་འདོད་ཆགས་ནི། །

[Block 2496 [VERSE]]
འདོད་པ་མིན་ན་གཟུགས་རྣམས་མཐོང་ནས་ནི། །
ཁྱོད་ཀྱི་སྟོན་པ་འང་འདོད་སྤྱོད་ཅན་དུ་འོང་། །

[Block 2497]
ཞེས་སྨྲས་སོ། །

[Block 2498]
ཡང་ཅི་ཆོས་གང་དག་འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པ་དག་ན་སྤྱོད་པ་དེ་དག་ཐམས་ཅད་འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པ་དང་ལྡན་པ་དག་ཅིག་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 2499]
འོ་ན་ཅི་ཞེ་ན། གང་དག་ལ་འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པའི་འདོད་ཆགས་དག་རྒྱས་པར་འགྱུར་བའོ། །

[Block 2500]
འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པའི་འདོད་ཆགས་དེ་དག་ཀྱང་གང་ཡིན་ཞེ་ན། གང་དག་འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དག་ཏུ་རྒྱས་པར་འགྱུར༌[^1304]བའོ། །

[Block 2501]
ད་ནི་འདི་རྟ་དང་བྲེས་ལྟ་བུ་དེ་ཡིན་ཏེ། རྟའི་བྲེས་འདི་སུའི་ཡིན་ཞེས་སྨྲས་ན། རྟ་འདི་སུའི་ཡིན་པའོ་ཞེས་ཟེར་རོ། །

[Block 2502]
རྟ་འདི་སུའི་ཡིན་ཞེས་སྨྲས༌[^1305]ན། རྟའི་བྲེས་འདི་སུའི་ཡིན་པའོ་ཞེས་ཟེར་བས་གཉི་ག་ཡང་མི་ཤེས་པ་ལྟ་བུ་ཡིན་ནོ། །

[Block 2503]
འདི་ནི་རྟ་དང་བྲེས་ལྟ་བུ་མ་ཡིན་ཏེ། འདོད་པའི་ཁམས་སུ་གནས་བརྟེན༌[^1306]པ་དེ་དག་ལ་འདོད་ཆགས་དང་མ་བྲལ་བའི་འདོད་ཆགས་གང་ཡིན་པ་དེ་ནི་འདོད་ཆགས་ཡིན་ལ་དེ་གང་དུ་རྒྱས་པར་འགྱུར་བའི་ཆོས་དེ་ཡང་འདོད་པ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 2504]
དེ་བཞིན་དུ་གཟུགས་དང༌[^1307]གཟུགས་མེད་པའི་འདོད་ཆགས་དང་། འོག་མའི་འདོད་ཆགས་དང་བྲལ་བའི་དག་ཀྱང་ཅི་རིགས་པར་རིག་པར་བྱའོ། །

[Block 2505]
ཡང་ན་མཉམ་པར་གཞག་པའི་ས༌[^1308]པའི་འདོད་ཆགས་ནི་འདོད་པའི་འདོད་ཆགས་སོ། །

[Block 2506]
བསམ་གཏན་དང༌[^1309]གཟུགས་མེད་པ་དག་ལ་འདོད་ཆགས་པ་ནི་གཟུགས་དང་གཟུགས་མེད་པའི་འདོད་ཆགས་སོ། །

[Block 2507]
སྤྲུལ་པའི་སེམས་ལ་ཇི་ལྟར་འདོད་པའི་འདོད་ཆགས་པ༌[^1310]ཡིན་ཞེ་ན། ཐོས་པ་དང་ཡོངས་སུ་ཉམས་ནས་དེ་ལ༌[^1311]ཆགས་པའི་ཕྱིར་རོ། །

[Block 2508]
ཡང་ན་སྤྲུལ་པའི་དབང་གིས་སྤྲུལ་པ་བྱེད་པའི་སེམས་ལ་ཡང་འདོད་ཆགས་སོ། །

[Block 2509]
ཡང་ན༌[^1312]དྲི་དང་རོ་སྤྲུལ་པའི་ཕྱིར་ན་དེ་འདོད་པ་ན་སྤྱོད་པ་ཉིད་ཡིན་ཏེ། གཟུགས་ན་སྤྱོད་པས་ནི་དེ་གཉིས་མི༌[^1313]སྤྲུལ་པའི་ཕྱིར་རོ། །

[Block 2510]
ཡང་ཅི་ཁམས་གསུམ་གཅིག་ཁོ་ན་ཞིག་ཡིན་ནམ་ཞེ་ན། ཁམས་གསུམ་རྣམས་ལ་མཐའ་མེད་དེ། །ནམ་མཁའ་ཇི་ཙམ་པ་འཇིག་རྟེན་གྱི་ཁམས་དག་ཀྱང་དེ་ཙམ་མོ། །

[Block 2511]
དེ་ཉིད་ཀྱི་ཕྱིར་སྔོན་མེད་པའི་སེམས་ཅན་འབྱུང་བ་ཡང་མེད་ལ། སངས་རྒྱས་འབྱུང་བ་རེ་རེས་སེམས་ཅན་གྲངས་མེད་པ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་ཀྱང་སེམས་ཅན་རྣམས་ཡོངས་སུ་གཏུགས་པ་མེད་དེ་ནམ་མཁའ་བཞིན་ནོ། །

[Block 2512]
འཇིག་རྟེན་གྱི་ཁམས་རྣམས་ཇི་ལྟར་གནས་ཤེ་ན། ཐད་ཀར་གནས་ཏེ། མདོ་ལས་དཔེར་ན་ཆར་གྱི་རྒྱུན་གཉའ་ཤིང་ཙམ་འབབ་པ་ན་བར་སྣང་ལས་ཆུའི་རྒྱུན་འབབ་པ་རྣམས་ཀྱི་མཚམས་སམ་བར་མེད་དོ། །

[Block 2513]
དེ་བཞིན་དུ་ཤར་ཕྱོགས་སུ་འཇིག་རྟེན་གྱི་ཁམས་འཆགས་པ༌[^1314]དང་འཇིག་པ་རྣམས་ཀྱི་མཚམས་སམ་བར་མེད་དོ། །

[Block 2514]
ཤར་ཕྱོགས་སུ་ཇི་ལྟ་བར་ལྷོ་དང་ནུབ་དང་བྱང་གི་བར་དུ་ཡང་དེ་དང་འདྲའོ་ཞེས་གསུངས་ཀྱི་སྟེང་དང་འོག་ཅེས་ནི་མ་གསུངས་སོ། །

[Block 2515]
གཞན་དག་ན་རེ་སྡེ་པ་གཞན་དག་ལས་བྱུང་བའི༌[^1315]ཕྱིར་སྟེང་དང་འོག་དག་ན་ཡང་ཡོད་དེ། འོག་མིན་གྱི་གོང་ན་ཡང་འདོད་པའི་ཁམས་ཡོད་ལ། འདོད་པའི་ཁམས་ཀྱི་འོག་ན་ཡང་འོག་མིན་ཡོད་དོ་ཞེས་ཟེར་རོ། །

[Block 2516]
གང་འདོད་པའི་ཁམས་གཅིག་ལས་འདོད་ཆགས་དང་བྲལ་བ་དེ་ནི་ཐམས་ཅད་ལས༌[^1316]འདོད་ཆགས་དང་བྲལ་བ་ཡིན་ནོ། །

[Block 2517]
གཟུགས་དང་གཟུགས་མེད་པ་དག་ལས་ཀྱང་དེ་དང་འདྲའོ། །

[Block 2518]
གང་ཞིག་བསམ་གཏན་དང་པོ་ལ་བརྟེན་པའི་རྫུ་འཕྲུལ་སྐྱེད་པར་བྱེད་པ་དེ་ནི་དེས་འཇིག་རྟེན་གྱི་ཁམས་གང་དུ་སྐྱེས་པ་ནས་སྐྱེད་པར་བྱེད་པ་དེ་ཁོ་ན་ན་ཡོད་པའི་ཚངས་པའི་འཇིག་རྟེན་གྱི་བར་དུ་འགྲོའི་གཞན་དུ་ནི༌[^1317]མ་ཡིན་ནོ། །

[Block 2519 [HEADING]]
#### འགྲོ་བ་ལྔ། ^3-1-2-0

[Block 2520]
ཁམས་གསུམ་པོ་དག་བཤད་པ་གང་ཡིན་པ། །དེར་ནི་དམྱལ་སོགས་འགྲོ་བ་ལྔ། །རང་གི་མིང་གིས་བསྟན། དེ་དག་ཏུ་དམྱལ་བ་དང་། དུད་འགྲོ་དང་། ཡི་དགས་དང་། ལྷ་དང་མི་ཞེས་བྱ་བ་འགྲོ་བ་ལྔ་པོ་རང་གི་མིང་དག་ཁོ་ནས་བསྟན་ཏེ། འདོད་པའི་ཁམས་ན་ནི་འགྲོ་བ་བཞི་དང་ལྔ་པའི་ཕྱོགས་སོ། །

[Block 2521]
གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དག་ན་ནི་ལྷའི་འགྲོ་བ་གཅིག་ཁོ་ནའི་ཕྱོགས་སོ། །གང་གིས་ན། དེ་དག་ཁམས་དག་ཏུ་ཞེས་བྱ་བ་ཅི་འགྲོ་བ་ལས་མ༌[^1318]གཏོགས་པའི་ཁམས་དག་ཅིག་ཡོད་དམ་ཞེ་ན། ཡོད་དེ་ཁམས་རྣམས་ནི་དགེ་བ་དང་། ཉོན་མོངས་པ་ཅན་དང་། སྣོད་དང་སྲིད་པ་བར་མ་པའི་རང་བཞིན་དག་ཀྱང་ཡིན་གྱི་འགྲོ་བ་ལྔ་པོ་གང༌[^1319]དག༌[^1320]ཡིན་པ། དེ་དག་ཉོན་མོངས་ཅན་མིན་ལུང་བསྟན་མིན། །སེམས་ཅན་ཞེས་བྱ་བར་སྲིད་མིན། །འགྲོ་བ་རྣམས་ནི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཁོ་ནའོ། །

[Block 2522]
དེ་ལྟ་མ་ཡིན་ན་འགྲོ་བ་ལྔ་འཆོལ་བར་འགྱུར་རོ། །

[Block 2523]
སེམས་ཅན་ཞེས་བྱ་བ་ཁོ་ན་ཡིན་ཡང་སྲིད་པ་བར་མའི་རང་བཞིན་དག་ནི་མ་ཡིན་ནོ། །

[Block 2524]
བཏགས་པ་ལས་ཀྱང་། སྐྱེ་གནས་བཞིས་ནི་འགྲོ་བ་ལྔ་བསྡུས་ཀྱི་འགྲོ་བ་ལྔས་ནི་སྐྱེ་གནས་བཞི་མ་བསྡུས་ཏེ། གང་ཞིག་མ༌[^1321]བསྡུས་ཤེ་ན། སྲིད་པ་བར་མའོ་ཞེས་གསུངས་སོ། །

[Block 2525]
ཆོས་ཀྱི་ཕུང་པོ་ལས་ཀྱང་མིག་གི་ཁམས་གང་ཞེ་ན། འབྱུང་བ་ཆེན་པོ་བཞི་དག་རྒྱུར་བྱས་པའི་གཟུགས་དང་བ་གང་ཡིན་པ་དམྱལ་བ་འམ་དུད་འགྲོའི་སྐྱེ་གནས་པ་དང་ཡི་དགས་པའི་ཡུལ་པའམ། ལྷ་འམ་མི་འམ། བསྒོམས་པ་ལས་བྱུང་བའམ། སྲིད་པ་བར་མ་པའི༌[^1322]མིག་དང་། མིག་གི་དབང་པོ་དང་། མིག་གི་སྐྱེ་མཆེད་དང་། མིག་གི་ཁམས་སོ་ཞེས་གསུངས་སོ། །
--- END BLOCKS ---
