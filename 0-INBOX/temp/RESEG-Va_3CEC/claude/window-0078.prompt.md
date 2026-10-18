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
[Block 2731]
བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་དད་པ་སྟེ་ཞེས་བྱ་བ་ནི་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཆོས་དང་། དེ་དག་གི་ཡོན་ཏན་ལ་དད་ཅིང་ཡིད་ཆེས་པའོ། །

[Block 2732]
སྤྱོད་པ་དེ་ལ་ཞུགས་པ་ནི་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྤྱོད་པ་ལ་ཞུགས་པའོ། །

[Block 2733]
ནས༌[^2396]ཀྱང་ཞེས་བྱ་བ་ནི་ཞུགས་ཕན་ཆད༌[^2397]དོ། །

[Block 2734]
ཐེག་པ་གཞན་ལ་འདོད་པ་མི་སྐྱེད་པ་ནི་ཉན་ཐོས་ལ་སོགས་པའི་ཐེག་པ་ལ་མི་སྤྱོད་པའོ། །

[Block 2735 [HEADING]]
##### ཆོས་ཐམས་ཅད་ལ་དོན་དམ་པ། ^8-4-1-3-0

[Block 2736]
ཆོས་ཐམས་ཅད་ལ་དོན་དམ་པ་ཞེས་བྱ་བ་ནི་དད་དོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཆོས་ཐམས་ཅད་ཉིད་དོན་དམ་པར་ངེས་པའི་དོན་ཟབ་མོ་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཡིན་པ་ལ་སོགས་པར་དད་པའོ། །

[Block 2737]
དོན་དམ་པར་ནི་སྟོང་པའོ། །

[Block 2738]
ངེས་པའི་དོན་ཟབ་མོ་ནི་ཕྱིན་ཅི་མ་ལོག་པའི་དོན་གཞན་གྱིས་ཁོང་དུ་ཆུད་པར་དཀའ་བའོ། །

[Block 2739]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ནི་རྒྱུ་རྐྱེན་ལས་འབྱུང་བས་མ་སྐྱེས༌[^2398]པའོ། །

[Block 2740]
དད་པ་ནི་དེ་བཞིན་དུ་ཡིན་པར་ཡིད་ཆེས་པའོ། །

[Block 2741]
ལྟ་བར་གྱུར་པ་ཐམས་ཅད་ལ་བག་ལ་ཉལ་བར་མི་བྱེད་པ་ནི་ལྟ་བ་ཕྱིན་ཅི་ལོག་རྣམས་ཀྱི་བག་ཆགས་སྩོགས་པར༌[^2399]མི་བྱེད་པའོ། །

[Block 2742 [HEADING]]
##### སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པ་ལ་དད་པ། ^8-4-1-4-0

[Block 2743]
སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པ་ལ་དད་པ་ནི་དེ་བཞིན་གཤེགས་པའི་ཡོན་ཏན་ལ་ཡོད་པར་ཡིད་ཆེས་ཤིང་དད་པའོ། །

[Block 2744]
དེ་དག་ཅེས་བྱ་བ་ནི་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པ་ཉིད་ལ་སྙེགས་པའོ། །

[Block 2745 [HEADING]]
#### བརྩོན་འགྲུས་ཀྱི་མཆོག། ^8-4-2-0

[Block 2746]
བརྩོན་འགྲུས་ཀྱི་མཆོག་གི་བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་བརྩོན་འགྲུས་ཀྱི་དབང་པོ་ལ་རབ་ཏུ་ཞུགས་པས་ཏེ། དེའི༌[^2400]དབང་དུ་བྱས་ནས། དེ་ལ་བརྩོན་འགྲུས་ཀྱི་དབང་པོ་གང་ཞེ་ན༌[^2401]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2747]
དད་པར་གྱུར་པ་ན་ཡོད་པར་ཡིད་ཆེས་པར་གྱུར་པའོ། །

[Block 2748 [HEADING]]
#### དྲན་པའི་མཆོག། ^8-4-3-0

[Block 2749]
དྲན་པའི་མཆོག་ནི་གང་དྲན་པའི་དབང་པོ་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་དྲན་པའི་དབང་པོ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2750]
ཆུད་མི་གསོན་པ་ཉིད་ནི་ཉམས་པར་མི་བྱེད་ཅིང་བརྗེད་པར་མི་བྱེད་པའོ། །

[Block 2751 [HEADING]]
#### ཏིང་ངེ་འཛིན་གྱི་མཆོག། ^8-4-4-0

[Block 2752]
ཏིང་ངེ་འཛིན་གྱི་མཆོག་ནི། གང་ཏིང་ངེ་འཛིན་གྱི་དབང་པོ་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས་དེ་ལ་ཏིང་ངེ་འཛིན་གྱི་དབང་པོ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2753]
རྩེ་གཅིག་ཏུ་བྱེད་པས་ནི་རྩེ་གཅིག་ཏུ་དམིགས་པར་བྱེད་པའོ། །

[Block 2754 [HEADING]]
#### ཤེས་རབ་ཀྱི་མཆོག། ^8-4-5-0

[Block 2755]
ཤེས་རབ་ཀྱི་མཆོག་ནི་གང་ཤེས་རབ་ཀྱི་དབང་པོ་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས་དེ་ལ་ཤེས་རབ་ཀྱི་དབང་པོ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2756]
རབ་ཏུ་རྟོགས་པ་ནི་ཆོས་དེ་དག་གི་རང་གི་མཚན་ཉིད་ལ་རབ་ཏུ་འབྱེད་པའོ། །

[Block 2757]
ཤིན་ཏུ་རྟོགས་པ་ནི་ཆོས་དེ་དག་གི་སྤྱིའི་མཚན་ཉིད་ཁོང་དུ་ཆུད་པའོ། །

[Block 2758]
གཞན་གྱི་དྲིང་ལ་མི་འཇོག་པ་ནི༌[^2402]གཞན་གྱིས་བསྟན་པ་ལ་བརྟེན་མི་དགོས་པར་ཤེས་པའོ། །

[Block 2759]
སོ་སོ་རང་གིས་ཤེས༌[^2403]པ་ནི་ཆོས་དེ་དག་རང་ཉིད་ཀྱིས་མངོན་སུམ་དུ་གྱུར་པའོ།[^2404] །དེ་ལྟར་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པ་ལྟར་རོ། །

[Block 2760]
ལྷན་ཅིག་འགྲོགས་ཤིང་རྗེས་སུ་འབྲེལ་པ་ནི་དད་པ་ལ་སོགས་པའི་དབང་པོ་དེ་ལྔ་པོ་གཅིག་གི་གྲོགས་གཅིག་གིས་བྱས་ནས་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་རྫོགས་པར་བྱེད་པའོ། །

[Block 2761]
ལུང་བསྟན་པའི་སར་ཡང་གཞོག་གོ་ཞེས་བྱ་བ་ནི་དེ་རྣམས་དང་ལྡན་ན་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་ལུང་བསྟན་དུ་མངོན་ཞིང་། ལུང་བསྟན་པར༌[^2405]འོས་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2762]
འཇིག་རྟེན་ལས་འདས་པའི་དབང་པོ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་རྟོགས་པར་བྱེད་པའི་དབང་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2763 [HEADING]]
#### དབང་པོའི་དོན། ^8-4-6-0

[Block 2764]
དེ་ལ་དབང་བྱེད་པའི་དོན་ནི་དབང་པོའི་དོན་ཏེ། དད་པའི་དབང་པོས་ནི་དགེ་བའི་ཆོས་རྣམས་ལ་འཇུག་པར་བྱ་བ་ལ་དབང་བྱེད་དེ། དེའི་དབང་གིས༌[^2406]དགེ་བའི་ཆོས་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 2765]
བརྩོན་འགྲུས་ཀྱི་དབང་པོས་ནི་དགེ་བའི་ཆོས་རྣམས་སྐྱེད་པ༌[^2407]ལ་དབང་བྱེད་དེ། དེའི་མཐུས་དགེ་བའི་ཆོས་རྣམས་སྐྱེད་པར་བྱེད་པས་སོ། །

[Block 2766]
དྲན་པའི་དབང་པོས་ནི་དགེ་བའི་ཆོས་རྣམས་ཆུད་མི་ཟ་བ༌[^2408]ལ་དབང་བྱེད་དེ། དེས་མི་བརྗེད་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2767]
ཏིང་ངེ་འཛིན་གྱི་དབང་པོས་ནི་གཞན་དུ་མི་གཡེང་བ་ལ་དབང་བྱེད་དེ། དེས་དམིགས་པའི་ཡུལ་ལ་རྩེ་གཅིག་ཏུ་འཇོག་པས༌[^2409]སོ། །

[Block 2768]
ཤེས་རབ་ཀྱི་དབང་པོས༌[^2410]ནི་མཐར་འབྱིན་པ་ལ་དབང་བྱེད་དེ། དེས་དགེ་བའི་ཆོས་ཐམས་ཅད་མཐར་འབྱིན་པར་བྱེད་པས་སོ། །

[Block 2769]
དབང་པོ་ལྔ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 2770 [HEADING]]
### སྟོབས་ལྔ་མི་ཟད་པ། ^8-5-0
--- END BLOCKS ---
