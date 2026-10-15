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
[Block 2626]
མིང་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་ཉེས་པ་སྦོམ་པོ་དང་། དགེ་འདུན་ལྷག་མ་དང་། སྤང་བའི་ལྟུང་བྱེད་དང་། ལྟུང་བྱེད་འབའ་ཞིག་པ་དང་། སོ་སོར་བཤགས་པར་བྱ་བ་དང་། ཉེས་བྱས་ཞེས་བྱ་བ་རྣམས་སོ། །

[Block 2627]
རིགས་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་མི་ཚངས་པར་སྤྱོད་པས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དང་། བསམས་བཞིན༌[^2443]དུ་ཁུ་བ་འབྱིན་པས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དང་། རེག་པས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དང་། འཁྲིག་པ་སྨྲ་བས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དང་། བསྙེན་བཀུར་བསྔགས་པས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དང་། ཚིག་རྩུབ་པ༌[^2444]སྨྲ་བས་ཀུན་ནས་བསླང་བའི་བར་དང་། ཞག་བཅུ་ལས་འདའ་བས་ཀུན་ནས་བསླང་བ་དང་། བརྫུན་དུ་སྨྲ་བས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དང་། དགེ་སློང་མའི་བསོད་སྙོམས་བྱིན་ལེན་བྱེད་པས་ཀུན་ནས་བསླང་བ་དང་། ཤམ་ཐབས་ཟླུམ་པོར་མ་བགོས་པས་ཀུན་ནས་བསླང་བ་ལ་སོགས་པ་དག་སྟེ། དེ་ལྟར་མིང༌[^2445]དང་རིགས་དང་ལྡན་པར་བརྗོད་པས་ལྟུང་བ་བཤགས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2628]
འདིར་བདག་ལས་བརྗོད་པ་ནི་སྔགས་ལས་ཤེས་པར་བྱ་སྟེ།

[Block 2629]
བདག་དགེ་སློང་མིང་འདི་ཞེས་བགྱི་བ་ལ་ལྟུང་བྱེད་ཀྱི་སྡེ་ཚན་ལས།

[Block 2630]
བརྫུན་དུ་སྨྲ་བས་ཀུན་ནས་བསླང་ཞེས་བྱ་བ་ལ་སོགས་པས་དེ་ལྟར་དེ་བརྗོད་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2631]
དགེ་འདུན་ལྷག་མ་ལས་ནི་དུས་འདི་ཇི་སྲིད་ཅིག་བཅབས་པ་ཉིད་དམ་མ་བཅབས་པ་ཉིད་དང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལྷག་མ་ལས་ནི་གཞན་འདི་དང་ལྡན་པར་བརྗོད་པར་བྱ་སྟེ། འཆབ་པ་འཛིན་པར་བྱེད་ན་ནི་དུས་ཇི་སྲིད་འཆབ་པར་བྱེད་པའི་དུས་དེ་ཙམ༌[^2446]པ་ཉིད་ཀྱིས་སོ། །

[Block 2632]
ཞག་གཅིག་བཅབས་པའམ༌[^2447]ཞག་གཉིས་བཅབས་པ་ལ་སོགས་པ་དེ་དང༌[^2448]བརྗོད་པར་བྱའོ། །

[Block 2633]
བཅས་པ་མ་ཡིན་པ་ལ་བཅས་པ་མ་ཡིན་པ་ཉིད་ཀྱིས་འཆབ་བ༌[^2449]མ་ཡིན་པ་ལ་སོགས་པའོ། །

[Block 2634]
དེ་ལས་བསླབ་བ༌[^2450]བྱེད་པ་ནི་དབྱུང་བའོ་ཞེས་བྱ་བ་ལ།[^2451] དེ་ལས་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལྷག་མ་དེ་ལས་སོ། །

[Block 2635]
གང་ཞིག་དེ་ལས་སློང་བར་བྱེད་པ་དེ་ཉིད་ཀྱི་ཕྱིར་མིང་འདི་དབྱུང་བ་ཞེས་བྱ་སྟེ་ལྟུང་བ་ལས་དབྱུང་བ༌[^2452]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2636]
ལྟུང་བར་བྱ་བའི་རྣམ་པ་ཉིད་ཀྱི་ཕྱིར་སྡེ་ཚན་དེ་ལ་འདིར་དེ་བརྗོད་པའོ། །

[Block 2637]
དབྱུང་བ་གང་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་ལས་ཞག་དྲུག་མགུ་བར་བྱ་བ་མནོས་ཏེ་སྤྱད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་འདུན་ལས་ཞག་དྲུག་མགུ་བར་བྱ་བ་མནོས་ཏེ་སྤྱད་ཅིང་དབྱུང་བ་གང་ཡིན་པ་དེ་ནི་ལྟུང་བ་དེ་ལས་སློང་བར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་དབྱུང་བ་ཡིན་གྱི་གཞན་ནི་མ་ཡིན་ནོ། །

[Block 2638]
དགེ་སློང་མས་ནི་ཟླ་བ་ཕྱེད་དོ་ཞེས་བྱ་བ་ནི་འདི་ལས་ཞག་དྲུག་ཏུ་མགུ་བ༌[^2453]སྤྱོད་པར་བྱ་བ་མ་ཡིན་ཏེ། འོན་ཀྱང་ཟླ་བ་ཕྱེད་ནི་གཉིས་ཀའི་དགེ་འདུན་ལས་ཞེས་བྱའོ། །

[Block 2639]
དེ་ནི་ལས་ཀྱི་གཞི་ལས་དགེ་སློང་མས༌[^2454]ལྕི་བའི་ཆོས་ལས་འདས་ན་ཡང་གཉིས་ཀའི་དགེ་འདུན་ལས་ཟླ་བ་ཕྱེད་མགུ་བར་བྱ་བ་མནོས་ཏེ་སྤྱད་པར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 2640]
ལྕི་བའི་ཆོས་ལས་འདས་ན་ཡང་དེ་སྤྱད་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བས༌[^2455]ནི་དགེ་སློང་མས་ལྕི་བའི་ཆོས་ལས་འདས་ན་ཡང་གཉིས་ཀའི་དགེ་འདུན་ལས་ཟླ་བ༌[^2456]ཕྱེད་མགུ་བར་བྱ་བ་དེ་མནོས་ཏེ། སྤྱད་པར་བྱ་བ་ཉིད་ཡིན་གྱི་དགེ་འདུན་ལྷག་མ་འབའ་ཞིག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2641]
བཅབས་པའི་ཉེས་པ་མེད་ན་དེ་འཆགས་སོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་བཅབས་པའི་ཉེས་པ་མེད༌[^2457]ན་དེའི་ཚེ་མགུ་བར་བྱ་བ་དེ་འཆགས་སོ། །

[Block 2642]
སྤོ་བས་དེ་མེད་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་སྤོ་བ་དེས་བཅབས་པའི་ཉེས་པ་དེ་འབྱང་ཞིང་མེད་པར་འགྱུར་ཏེ། སྤོ་བ་དེས་བཅབས་པའི་ཉེས་པ་བསལ་བ་བྱས་པ་ལ་མགུ་བར་བྱས་པ་འཆགས་སོ། །

[Block 2643]
ལྟུང་བ་གཞན་བསྐྱེད་པ་བསྒྲུབ་པ་རྗེས་སུ་སྒྲུབ་པར་བྱེད་པ་ལ་ཡང་ཉེས་པ་ཕྱིར་བཅོས་པར་བྱ་ཞིང་འཆགས་པ་ཞེས་བྱ་བའི་རྗེས་སུ་འབྲངས་ནས་ཤེས་པར་བྱའོ། །

[Block 2644]
སྤོ་བས༌[^2458]ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་ལས་དུས་དེ་སྲིད་མནོས་ཏེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྟུང་བ་འབྱིན་པར་བྱེད་པ་དེས་དུས་ཇི་སྲིད་དུ་བཅབས་པའི་དུས་དེ་སྲིད་སྤོ་བ་དགེ་འདུན་ལས་མནོས་ཏེའོ་ཞེས་བྱ་བའི་དོན་ནོ། །

[Block 2645]
དེ་གཉིས་བྱེད་པ་ཉིད་ན་དགེ་འདུན་ལྷག་མ་དེ་བྱུང་ན་མནོས་ཏེ་བྱས་པ་དེ་གཉིས༌[^2459]ཞིག་པས་དེའི་ཕྱིར་གཞི་ནས་བརྩམས་པ་ཉིད་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལྷག་མ་དེ༌[^2460]ཕྱིར་བཅོས་པའི༌[^2461]ཕྱིར་སྤོ་བ་དང་མགུ་བར་བྱ་བ་དེ་གཉིས་བྱེད་པ་ཉིད་ན་དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་བྱུང་བ་གང་ཞིག་སྔ་མ་དང་འདྲ་བ་རིགས་མཐུན་པ་ཡང་བྱུང་ན་སྤོ་བ་ལ་གནས་པ་དང་། མནོས་པ༌[^2462]མགུ་བར་བྱ་བ་སྤྱད་པ་མནོས་ཏེ། བྱས་པ་དེ་ཉིད་ཉམས་པ་ཡིན་ནོ། །

[Block 2646]
དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་སྔ་མ་དང་མི་འདྲ་བ་བྱུང་བ་ལ་ནི་མི་ཉམས་སོ། །

[Block 2647]
གང་གི་ཕྱིར་དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་སྔ་མ་དང་འདྲ་བ་སྤོ་བ་དང་མགུ་བར་བྱ་བ་མནོས་ཤིང་བྱས་པ་དེ་གཉིས་ཉམས་པ་དེའི་ཕྱིར་གཞི་ནས་བརྩམས་པ་ཉིད་སྦྱིན་པར་བྱ༌[^2463]སྟེ། དགེ་སློང་དེ་ལ་ཡང་གཞི་ནས་བརྩམས་ཏེ་སྤོ་བ་དང་མགུ་བར་བྱ་བ་ཉིད་སྦྱིན་པར་བྱ་བ་ཞེས་བྱ་བའི་དོན་ནོ། །

[Block 2648]
བརྩམས་པ་ནི་མཐར་ཐུག་པར་བྱ་བ་དང་འདྲའོ་ཞེས་བྱ་བ༌[^2464]ནི་གང་ལ་སྤོ་བ་བརྩམས༌[^2465]ནས་གཞི་ནས་སྤོ་བ་དང་ཡང་གཞི་ནས་བསླང་སྟེ་སྤོ་བ་དང་། མགུ་བར་བྱ་བ་དང་གཞི་ནས་བསླང་སྟེ་མགུ་བར་བྱ་བ་བརྩམས་པ་གང་ལ་དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་རིགས་མཐུན་པ་བྱུང་ན༌[^2466]མཐར་ཐུག་པ་དང་འདྲ་བ་དེ་བལྟ་བར་བྱའོ། །

[Block 2649]
ཡང་དག་པར་བླངས་པར་གྱུར་པ་དེ་ལ་སླར་བསླང་བར་བྱ་བ༌[^2467]ཀུན་དུ་སྤྱད་པ་སྤྱོད་དུ༌[^2468]འཇུག་པ་སྔ་མ་ལྟར་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ནོ། །ཤེས་པ་དེ་ཡང་དེ་ཁོ་ན་ལྟར་བློ་གནས་པས་དེ་ཉིད་འདིར་སྐབས་སུ་བབ་པ་དེ་ལྟར་མ་གྲུབ་པ་ཞེས་བྱ་བ་སླར་བྱེད་པ་སྟེ། གཞན་གྱིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2650]
དེའི་ཕྱིར་དེ་མ་ཆགས་ན་དེའི་ཚེ་དང་པོ་ཡང་ཐ་དད་པར་བསླང་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་བརྩམས་པ་ནི་མཐར་ཐུག་པ་དང་འདྲ་བ་དེའི་ཕྱིར་སྤོ་བ་ལ་སོགས་པ་སྔ༌[^2469]མ་ལྟར་ནི་མ་ཡིན་ནོ། །

[Block 2651]
དེ་བས་ན་མ་གྲུབ་པས་བསླང་བ་དེ་ནི་དེའི་ཚེ་སྦྱིན་པ་ལ་མ་ཆགས་པའོ། །

[Block 2652]
དེ་མ་ཆགས་པའི་གནས་སྐབས་སུ་གཞི་ནས་བསླང་བ་ཉིད་སྦྱིན་པར་བྱ་བ་མ་ཡིན་པས་ཐ་དད་པར་བསླང་བར་བྱའོ། །

[Block 2653]
ཇི་ལྟར༌[^2470]ལྟུང་བ་བར༌[^2471]མེད་པར་གྱུར་པ་ལ་ཡང་སྤོ་བ་མགུ་བ༌[^2472]སྦྱིན་དགོས་པ་དེ་བཞིན་དུ་བར་མ་གྱུར་པ༌[^2473]ལ་ཡང་ཐ་དད་པར་སྦྱིན་པའོ། །

[Block 2654]
བར་མ་དེ་ཕྱིར་བཅོས་པར་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བ་ནི་ཕྱིར་བཅོས་པའི་བདག་ཉིད་ཅན་གྱི་དོན༌[^2474]སྨོས་པས་སོ། །

[Block 2655]
གང་ཞིག་ལྟུང་བ་བར་མའི་བདག་ཉིད་འདི་ཁ་ན༌[^2475]མ་ཐོ་བ་ཕྱིར་བཅོས་པ་དེའི་དོན་དུ་སྤོ་བ་ལ་སོགས་པའོ། །

[Block 2656]
དེ་བས་ན་འདིར་སྤོ་བ་ལ་སོགས་པས་ཕྱིར་བཅོས་པ་ཉིད་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2657]
དེའི་ཕྱིར་དེའི་དོན་དུ་ཡང་བརྟེན་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་ལྟུང་བ་བར་མའི་བདག་ཉིད་ཁ་ན་མ་ཐོ་བ་དེའི་ཕྱིར་བཅོས་པར་བྱ་བ་ཁོ་ན་སྟེ། དེའི་ཕྱིར་གཞི་ནས་བརྩམས་པས་གང་གི་ཚེ་མ་ཆགས་པ་ལེན་པར་བྱེད་པ་དེའི་ཚེ་དེ་ཕྱིར་བཅོས་པ་དེའི་དོན་དུ་སྔར་བྱས་པ་ཡང་བསླང་བར༌[^2476]བྱ་བའི་དོན་ཏོ།[^2477] །དེར་གཏོགས་པའི་སེམས་ཅན་ཐམས་ཅད་བསྐྱེད་དེ་རྒྱུད༌[^2478]དང་འདྲ་བའི་དུ་མ་ཅིག་ཅར་གཟུང༌[^2479]བའོ། །

[Block 2658]
ཇི་ལྟར་བརྩོན་པ་སྔོན་དུ་འགྲོ་བ་ཅན་ལྟུང་བ་དུ་མ་རྣམས་ཀྱི་ཕྱིར་དེར་གཏོགས་པའི་སེམས་ཅན་ཐམས་ཅད་བསྐྱེད་ནས་རྒྱུད་ལ་བྱ་བ་དུ་མ་ཅིག་ཅར་ལེན་པར་བྱེད་པ་དེ་ལྟར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2659]
དེ་བཅབས་པའི༌[^2480]དུས་ལྷག་མ་ཡང་དེར་གཞུག་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདིར་ལྟུང་བ་བར་མའི་དུས་ལྷག་པར་འགྱུར་བ་གཞི་ནས་བསླངས༌[^2481]ཏེ་ལེན་པ་ལ་ཁོངས་སུ་བསྡུ་བ་ཉིད་ལ་སྤོ་བའམ་གཞི་ནས་སྤོ་བ་དུས་དེ་ཙམ་ཡང་དག་པར་བསླང་བར་བྱ་ཞེས་བྱ་བའོ། །

[Block 2660]
ཡང་ཇི་ལྟར་ལྟུང་བ་བར་མ་བཅབས་པའི་དུས་ལྷག་པར་འབྱུང་བ་ཇི་སྲིད་པས་དེའི་ཕྱིར་བརྗོད་པར་བྱ་སྟེ། སྤྱོད་པ་ལ་ཞུགས་པ་མཐར་ཐུག་ན་ལྟུང་བ་བར་མ་བརྗོད་པ་དང་གཞན་དུ་ཡང་མ་བརྗོད་པས་སོ། །

[Block 2661]
རྣམ་པ༌[^2482]གཞན་གྱིས་ཀྱང་འདི་ལྟ་སྟེ། སྤོ་བའམ་གཞི་ནས་སྤོ་བ་བྱེད་པས་ལྟུང་བ་རིགས་མཐུན་པ་བྱུང་ནས་འཐབ་ཀྲོལ་བྱེད་པ་འོང་བ་ཕྱིར་སྤོ་བའམ་གཞི་ནས་སྤོ་བ་ལ་སོགས་པ་བཏང་སྟེ་ཡང་ཕྱིར་ལེན་པ་དེས་བཏང་བའི་གནས་སྐབས་སུ་བཅབས་པའི༌[^2483]དུས་རིང་དུ་སྒྲུབ་པར་བྱེད་པའོ། །

[Block 2662]
མནོས་ཏེའོ་ཞེས་སྨོས་ཏེ་དགེ་འདུན་གྱི་སྤོ་བ་དང་མགུ་བར་བྱ་བ་དེ་གཉིས་ཇི་ལྟར་སྦྱིན་པར་བྱ་བ་ནི༌[^2484]བསྟན་པས༌[^2485]དེའི་ཕྱིར། དབྱུང་བ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་ལས་ཀྱིས་སྦྱིན་ནོ་ཞེས་བྱ་བའི་རྗེས་སུ་བསྙེག་པའི༌[^2486]ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 2663]
དེར་བསྡིགས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཁྱོད་ཀྱིས་ལེགས་པར་མ་བྱས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྔགས་ལས་ལྡང་བར་བྱེད་པའོ། །

[Block 2664]
དེར་ཞེས་བྱ་བ་ནི་དབྱུང་བ་དེར་རོ། །

[Block 2665]
བསྡིགས་པ་དེ་ནམ་གྱི་ཚེ་ན་བྱ་ཞེ་ན་དེའི་ཕྱིར་གསོལ་བ་དང་ལས་བརྗོད་པ་དང་པོའི་བར་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གསོལ་བ་བྱས་ནས་དེའི་རྗེས་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
