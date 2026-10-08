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
[Block 2661 [HEADING]]
### ལེའུ་བཞི་པ། ^2-4-0

[Block 2662]
དེ་ནས་ནི་རྗེས་ལ་སྟེ་ལེའུ་སྔ་མའིའོ། །

[Block 2663]
རྡོ་རྗེ་སྙིང་པོ་ལ་སོགས་པ་རྡོ་རྗེ་མཁའ་འགྲོ་མ་ཐེ་ཚོམ་དུ་གྱུར་པ་ནི་སྔར་ནི་སོ་སོར་དྲིས་ལ༌[^1136]ད་ནི་སྡོམ་སྟེ་བཅོམ་ལྡན་འདས་ལ་གསོལ་ཏོ། །

[Block 2664]
དེ་དག་གིས་སོ་སོར་དྲིས་པ་ནི་གོ་སླའོ། །

[Block 2665 [VERSE]]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། །
ཞེས་པ་ལན་རིམ་གྱིས་ཏེ་དང་པོར་གླུའོ། །

[Block 2666 [HEADING]]
#### རྡོ་རྗེའི་གླུ། ^2-4-1-0

[Block 2667]
རྡོ་རྗེའི་གླུ་ཡང་བཞིར་གནས་ཏེ་བསྐྱེད་རིམ་གྱི་ང་རྒྱལ་དང་ལྡན་པའི་དཔའ་བོའི་སྟོན་མོ་དང་། ཚོགས་བྱ་བ་དང་། གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་ཀུན་གྱི་ཆགས་པའི་ཆོས་སུ་བསྟན་པ་དང་རང་ལུས་ཐབས་དང་ལྡན་པ་དང་གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོའོ། །

[Block 2668 [HEADING]]
##### བསྐྱེད་རིམ། ^2-4-1-1-0

[Block 2669]
བསྐྱེད་རིམ་ལ་གཉིས་ཏེ། དཔའ་བོའི་སྟོན་མོ་དང་ཚོགས་སོ། །

[Block 2670 [HEADING]]
###### དཔའ་བོའི་སྟོན་མོ། ^2-4-1-1-1-0

[Block 2671]
དཔའ་བོའི་སྟོན་མོ་ལ་བཞི་སྟེ། འདུ་བའི་ཁྱད་པར་དང་ལོངས་སྤྱོད་དང་དམ་ཚིག་དང་རྟོག༌[^1137]པའོ། །

[Block 2672 [HEADING]]
###### **འདུ་བའི་ཁྱད་པར།** ^2-4-1-1-1-1-0

[Block 2673]
དེ་ལ་འདུ་བའི་ཀོ་ལ་ཨི་རེ་ཊྛི་སྟེ་གནས་ལ་སོགས་པའི་རྣལ་འབྱོར་པ་དང་། མུམྨུ་ནི་ཞིང་ལ་སོགས་པའི་རྣལ་འབྱོར་མ་རྣམས་དང་གྷ་ཎེ་སྟེ་ཉེ་བར་འདུས་ནས་ཧ༌[^1138]ལེ་ཀ་ལི་སྟེ་སྐལ་པ་དང་ལྡན་པ་ནི་གཞུག །དུཾ་དུ་ར་སྟེ་སྐལ་བ༌[^1139]དང་མི་ལྡན་པ་ནི་མི་གཞུག་གོ། །

[Block 2674]
ནི་རཾ་ཤུ་རུས་པའི་རྒྱན་བཏགས་པའོ། །

[Block 2675]
ཀྲྀ་པི་ཊ་ཧོ་བཛྲ་ཞེས་པ་ནི་ཅང་ཏེའུའི་སྒྲ་ནི་བརྡུང་བ་དང་བཅས་པའོ། །

[Block 2676 [VERSE]]
ཀཱ་རུ་ཎ་ནི་བརྩེ་བ་དང་ལྡན་པའོ། །
ཨ་ཨི་ན་རོལ་སྟེ་ཞེ༌[^1140]འགྲས་པ་མེད་པས་སོ། །
ཏ༌[^1141]ཧི་ཛཾ་ས་རཱ་བ་སྟེ་རོ་བཙལ་ནས་སོ། །

[Block 2677]
པ་ཎི་ཨ་ཨི་སྟེ་དབུས་སུ་བཅུག་པ་དང་བཅས་པའོ། །

[Block 2678 [HEADING]]
###### **ལོངས་སྤྱོད།** ^2-4-1-1-1-2-0

[Block 2679]
ཀུན་ཀྱང་རྟོག་པ་བསྐྱེད་ཅིང་བསྒོམ་སྟེ། ལོངས་སྤྱོད་ཀྱི་རྣལ་འབྱོར་ཀུན་དང་སྤྱད་པར་བྱ་བའི་རོ་ལ་སོགས་པ་རྫས་ཀུན་ལ་རོ་ནི་ཕྲེཾ་ཁ་ཎ་སྟེ་གང་ནས་ཀྱང་མ་འོངས། ཁ༌[^1142]ཊ་ཀ་རན་ཏེ༌[^1143]གང་དུ་ཡང་འགྲོ་བའི་དགོས་པ་མེད་པའོ། །

[Block 2680]
གཞན་དག་བཟའ་བཏུང་གི་ཆོ་གས༌[^1144]ནི་ཤུདྡྷ་སྟེ་དག་པ་དང་། །

[Block 2681 [VERSE]]
ཨ་ཤུདྡྷ་སྟེ་མ་དག་པར་རོ། །
མུ་ཎི་ཨ་ཨི་སྟེ་མི་བལྟ་བར་རོ། །

[Block 2682]
གཙང་བ་དང་མི་གཙང་བ་མེད་པའི་ཕྱིར་དག་པ་དང་མ་དག་པར་མི་བལྟ་སྟེ་ལྷར་རྟོགས་པས་བསྒོམ་པ་དང་། ཏ་ཧིཾ་བ་ལ་སྟེ་སྟོབས་བཟའ་བ་དང་། ག་ཌྷེཾ་སྟེ་འབད་པས་ཆང་བཏུང་བ་སྟེ་ལོངས་སྤྱོད་དོ། །

[Block 2683 [HEADING]]
###### **དམ་ཚིག།** ^2-4-1-1-1-3-0

[Block 2684]
དེ་ནས་དམ་ཚིག་ནི་ཙ༌[^1145]ཨུ་མ་སྟེ། བཞི་མཉམ་ལ་སོགས་པའོ། །

[Block 2685]
ཨ་ཨི་བྷ་རུ་ཁཱ་ཨི༌[^1146]སྟེ་དེར་ཁེངས་པར་བཟའ་བཏུང་ངོ་། །

[Block 2686 [HEADING]]
###### **རྟོག་པ།** ^2-4-1-1-1-4-0

[Block 2687]
རྟོགས་པ་ནི་མངོན་རྟོགས་འཁྲུག་སྟེ༌[^1147]ཤེས་པར་བྱའོ། །

[Block 2688 [HEADING]]
###### ཚོགས། ^2-4-1-1-2-0

[Block 2689]
ཚོགས་ལ་གཉིས་ཏེ་ཡུལ་མཉམ་པ་དང་སྦྱོར་བ་མཉམ་པའོ། །

[Block 2690]
དེ༌[^1148]ཡང་ཚིག་གི་གོ་རིམས་བཟློག་པའོ། །

[Block 2691 [HEADING]]
###### **ཡུལ་མཉམ་པ།** ^2-4-1-1-2-1-0

[Block 2692]
དེ་ཡུལ་མཉམ་པ་ནི་ཌི་མ་སྟེ་གཡུང་མོ་ཉེ་བར་མཚོན་པ་སྟེ་བྲམ་ཟེ་མོའི་བར་དུ་མི་སྤང་བར་སྤྱད་དོ། །

[Block 2693]
ཀྱེ་ཧ་ཧི་ནི་བྷ་ཛའི་སྟེ་མི་སྤང༌[^1149]བར་བཤད་དོ། །

[Block 2694 [HEADING]]
###### **སྦྱོར་བ་མཉམ་པ།** ^2-4-1-1-2-2-0

[Block 2695]
སྦྱོར་བ་མཉམ་པ་ནི་མ་ལཱ་ཛེ་སྟེ་ཡབ་ཡུམ་ལུས་ཆ་མཉམ་པ་དང་ཀུན་དུ་རུ་བྷ་ཏ་ཧི༌[^1150]སྙོམས་འཇུག་ལས་བྱུང་བའི་ཞུ་བ་དེ་མཉམ་པར་མི་སྤང་བའོ། །

[Block 2696 [HEADING]]
##### གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ། ^2-4-1-2-0

[Block 2697]
ད་ནི་གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་ལ་རྗེས་སུ་ཆགས་པའི་ཆོས་སུ་བསྟན་པའི་ཕྱིར་ལ་ཚིག་བཞི་བཞི༌[^1151]ལ་རྐང་པ་གཉིས་སུ་སྦྱར་ཏེ་བླང་ངོ་། །དེ་ཡང་བཞི་སྟེ། སྙོམས་པར་འཇུག་པའི་སྦྱོར་བ་དང་ལྡན་པ་དང་། ཡོན་ཏན་སྤོང་བའི་ཁྱད་པར་དང༌[^1152]ལྡན་པའི་སྦྱོར་བ་དང་། ཡོན་ཏན་ཐོབ་པའི་ཁྱད་པར་དང་ལྡན་པའོ། །

[Block 2698]
སྦྱོར་བ་དང་དབྱེར་མེད་བསྒོམ་པའི་ཁྱད་པར་ལྡན་པའི་སྦྱོར་བའོ། །

[Block 2699 [HEADING]]
###### སྙོམས་པར་འཇུག་པའི་སྦྱོར་བ། ^2-4-1-2-1-0

[Block 2700]
དེ་ལ་སྙོམས་པར་འཇུག་པའི་སྦྱོར་བའི་ཆོས་ནི་ཀོལླ༌[^1153]ཨི་རི་སྟེ་རྣལ་འབྱོར་པའི་ལུས་དང་པོ་ལ་སྟེ་གསང་བའི་ལུས་སོ། །
--- END BLOCKS ---
