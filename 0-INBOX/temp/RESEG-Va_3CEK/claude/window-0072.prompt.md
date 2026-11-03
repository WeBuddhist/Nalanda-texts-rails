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
ལུས་ལ་རྗེས་སུ་ལྟ་བ་ནི་ལུས་ཀྱི་རྗེས་སུ་ལྟ་བའོ། །

[Block 2522]
ཅིའི་ཕྱིར་ཤེས་རབ་ལ་དྲན་པ་ཉེ་བར་གཞག་པ་ཞེས་བཤད་ཅེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་དྲན་པ་ཤས་ཆེ་བའི་ཕྱིར་ཏེ། ཤིང་གཤེགས༌[^1786]པའི་ཁྱེའུ་དག་གིས་འཛིན་པ་ལྟར་དྲན་པའི་སྟོབས་བསྐྱེད་པས་འཇུག་པ་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ་ཞེས་ཟེར་རོ། །

[Block 2523]
འདི་ལྟར་ནི་རུང་སྟེ། འདིས་དྲན་པ་ཉེ་བར་འཇོག་པས་ན་དྲན་པ༌[^1787]ཉེ་བར་གཞག་པ་ནི་ཤེས་རབ་ཡིན་ཏེ། ཇི་ལྟར་མཐོང་བ་མངོན་པར་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 2524]
འདི་ལྟར་ཚེ་དང་ལྡན་པ་མ་འགགས་པས་ཀྱང་། ལུས་ལ་ལུས་ཀྱི་རྗེས་སུ་ལྟ་ཞིང་གནས་པ་དེའི་ལུས་ལ་དམིགས་པའི་དྲན་པ་གནས་པ་ཡང་དག་པར་གནས་ཞེས་རྒྱས་པར་བཤད་དོ། །

[Block 2525]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ལུས་ལ་ལུས་ཀྱི་རྗེས་སུ་ལྟ་ཞིང་གནས་པ་དེའི་དྲན་པ་ཉེ་བར་གནས་ཤིང་ཀུན་ཏུ་མི་རྨོངས་པ་ཡིན་ཞེས་གསུངས་སོ། །

[Block 2526]
གང་ལས་དགེ་སློང་དག་ཇི་ལྟར་ན་དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་ཀུན་འབྱུང་བ་དང་། ནུབ་པ་ཡིན་ཞེ་ན། ཟས་ཀུན་འབྱུང་བས་ནི་ལུས་ཀུན་འབྱུང་བ་ཡིན་ལ། ཟས་འགགས་པས་ནི་ལུས་ནུབ་པ་ཡིན་ནོ་ཞེས་གསུངས་པ་དེ་ལས་ནི་དམིགས་པ་ཁོ་ན་དྲན་པ་ཉེ་བར་གཞག་པར་གསུངས་པ་ཡིན་ཏེ། འདི་ལ་དྲན་པ་ཉེ་བར་གནས་པའི་ཕྱིར་རོ། །

[Block 2527]
འདི་དག་གི་མིང་ནི་དམིགས་པ་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 2528]
འདི་དག་རང་དང་གཞན་དང་གཉི་གའི་རྒྱུད་ལ་དམིགས་པའི་ཕྱིར་རེ་རེ་ཞིང་རྣམ་པ་གསུམ་གསུམ་ཡིན་ནོ། །

[Block 2529 [HEADING]]
###### དྲན་པ་ཉེ་བར་གཞག་པའི་རིམ། ^3-1-3-5-2-0

[Block 2530]
རིམ་ནི་ཇི་ལྟར་སྐྱེ་བ་བཞིན་ཅིའི་ཕྱིར་དེ་ལྟར་སྐྱེ་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ། སྔར་རགས་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2531]
ཡང་ན་འདི་ལྟར་འདོད་པ་ལ་འདོད་ཆགས་པའི་རྟེན་ནི་ལུས་ཡིན་ལ། དེ་ཡང་ཚོར་བ་མངོན་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 2532]
དེ་ཡང་སེམས་མ་ཞི་བའི་ཕྱིར་རོ། །

[Block 2533]
དེ་ཡང་ཉོན་མོངས་པ་མ་སྤངས་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 2534]
ཕྱིན་ཅི་ལོག་གི་གཉེན་པོར་བཞི། །གཙང་བ་དང་བདེ་བ་དང་རྟག་པ་དང་བདག་ཏུ་ཕྱིན་ཅི་ལོག་རྣམ་པ་བཞིའི་གཉེན་པོར་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་གོ་རིམས་བཞིན་དུ་བསྟན་ཏེ་མི་མང་མི་ཉུང་ངོ་། །དེ་དག་ལས་གསུམ་ནི་མ་འདྲེས་པ་ལ་དམིགས་པ་ཡིན་ནོ། །

[Block 2535]
བཞི་པ་ནི་གཉི་ག་ཡིན་ཏེ། གལ་ཏེ་ཆོས་ཁོ་ན་ལ་ལྟ་ན་མ་འདྲེས་པ་ལ་དམིགས་པ་ཡིན་ནོ། །

[Block 2536]
འོན་ཏེ་ལུས་ལ་སོགས་པ་གཉིས་སམ་གསུམ་མམ་བཞི་པོ་སྤྱི་ལ་ལྟ་ན་འདྲེས་པ་ལ་དམིགས་པ་ཡིན་ནོ། །

[Block 2537 [HEADING]]
###### ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་སྤྱི་ལ་དམིགས་པ། ^3-1-3-5-3-0

[Block 2538]
དེ་ལྟར་ལུས་ལ་སོགས་པ་ལ་དམིགས་པའི་དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་གོམས་པར་བྱས་ནས།

[Block 2539 [VERSE]]
དེ་ནི་ཆོས་དྲན་ཉེ༌[^1788]གཞག་པ། །
སྤྱི་ལ་དམིགས་པ་ལ་གནས་ཏེ། །
དེ་དག་ལ་ནི་མི་རྟག་དང་། །
སྡུག་བསྔལ་སྟོང་བདག་མེད་པར་ལྟ། །

[Block 2540]
ཆོས་དྲན་པ་ཉེ་བར་གཞག་པར་འདྲེས་པ་ལ་དམིགས་པ་ལ་གནས་ཏེ། ལུས་ལ་སོགས་པ་དེ་དག་ཐམས་ཅད་སྤྱིར་བསྡུས་ཏེ། མི་རྟག་པ་དང་། སྡུག་བསྔལ་བ་དང་། སྟོང་པ་དང་བདག་མེད་པ་དང་། རྣམ་པ་བཞིར་ལྟའོ། །

[Block 2541 [HEADING]]
##### ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ། ^3-1-3-6-0

[Block 2542 [HEADING]]
###### དྲོ་བར་གྱུར་པ། ^3-1-3-6-1-0

[Block 2543]
དེ་ལས་དྲོ་བར་གྱུར་པ་འབྱུང་། །ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་དེ་ལྟར་གོམས་པ་ལས་རིམ་གྱིས་དགེ་བའི་རྩ་བ་དྲོ་བར་གྱུར་པ་ཞེས་བྱ་བ་སྐྱེའོ། །

[Block 2544]
དྲོ་བར་གྱུར་པ་དང་འདྲ་བས་ན་དྲོ་བར་གྱུར་པ་སྟེ། ཉོན་མོངས་པའི་བུད་ཤིང་སྲེག་པར་བྱེད་པ་འཕགས་པའི་ལམ་གྱི་མེའི་སྔ་ལྟས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2545]
དེ་ནི་བདེན་བཞི་སྤྱོད་ཡུལ་ཅན། །དྲོ་བར་གྱུར་པ་དེ་ནི་རྒྱུན་ཆགས་པ་ཡིན་པའི་ཕྱིར་བདེན་པ་བཞི་ལ་དམིགས་པ་ཡིན་ནོ། །

[Block 2546]
རྣམ་པ་བཅུ་དྲུག །སྡུག་བསྔལ་ལ་མི་རྟག་པ་དང་། སྡུག་བསྔལ་བ་དང་། སྟོང་པ་དང་། བདག་མེད་པ་དང་། རྣམ་པ་བཞིར་ལྟའོ། །

[Block 2547]
ཀུན་འབྱུང་ལ་རྒྱུ་དང་། ཀུན་འབྱུང་བ་དང་། རབ་ཏུ་སྐྱེ་བ་དང་། རྐྱེན་དང་རྣམ་པ་བཞིར་ལྟའོ། །

[Block 2548]
འགོག་པ་ལ༌[^1789]འགོག་པ་དང་། ཞི་བ་དང་། གྱ་ནོམ་པ་དང་། ངེས་པར་འབྱུང་བ་དང་རྣམ་པ་བཞིར་ལྟའོ། །

[Block 2549]
ལམ་ལ་ལམ་དང་། རིགས་པ་དང་། སྒྲུབ་པ་དང་། ངེས་པར་འབྱིན་པ་དང་རྣམ་པ་བཞིར་ལྟ་སྟེ་འདི་དག་གི་བྱེ་བྲག་ནི། འོག་ནས་བཤད་པར་བྱའོ། །

[Block 2550 [HEADING]]
###### རྩེ་མོ། ^3-1-3-6-2-0

[Block 2551]
དྲོ་བ་ལས།

[Block 2552]
རྩེ་མོ། །

[Block 2553]
དྲོ་བ་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོའི་རིམ་གྱིས་མངོན་པར་འཕེལ་བ་ལས་རྩེ་མོ་དག་ཀྱང་སྐྱེ་སྟེ། དེ་ཡང་དེ་དང་འདྲ། ཇི་ལྟར་དྲོ་བར་གྱུར་པ༌[^1790]རྣམས་བདེན་པ་བཞི་ལ་དམིགས་པ་དང་། རྣམ་པ་བཅུ་དྲུག་ཡིན་པ་བཞིན་ཏེ། ཆེས་མཆོག་ཏུ་གྱུར་པའི་ཕྱིར་ན་མིང་གཞན་དུ་བཏགས་སོ། །

[Block 2554]
དགེ་བའི་རྩ་བ་གཡོ་བའི་རྩེ་མོ་ཡིན་པའི་ཕྱིར་རྩེ་མོ་རྣམས་ཏེ། དེ་དག་ལས་ལྟུང་བའམ་འདའ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2555]
གཉི་ག༌[^1791]ཆོས་ཀྱི༌[^1792]རྣམ་པ་གཏོད། །དྲོ་བར་གྱུར་པ་དང་རྩེ་མོ་གཉིས་ཀ་ཆོས་དྲན་པ་ཉེ་བར་གཞག་པས་རྣམ་པ་གཏོད་པར༌[^1793]བྱེད་དོ། །

[Block 2556]
རྣམ་པ་གཏོད་ཅེས་བྱ་བ་འདི་ཅི་ཞེ་ན།

[Block 2557]
དང་པོ་ཉིད་དུ་བདེན་པ་རྣམས་ལ་རྣམ་པ་དག་འགོད་པའོ། །

[Block 2558]
གཞན་དག་གིས་ཀྱང་འཕེལ་བར་བྱེད། དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་ཆར་གྱིས་ཀྱང་དེ་དག་འཕེལ་བར་བྱེད་དོ། །

[Block 2559]
རྣམ་པར་འཕེལ་བར་བྱེད་པ་ན་སྔོན་ཐོབ་པ་རྣམས་མངོན་སུམ་དུ་མི་བྱེད་དེ། དགའ་བ་ཆེན་པོ་མེད་པའི་ཕྱིར་རོ། །

[Block 2560 [HEADING]]
###### བཟོད་པ། ^3-1-3-6-3-0
--- END BLOCKS ---
