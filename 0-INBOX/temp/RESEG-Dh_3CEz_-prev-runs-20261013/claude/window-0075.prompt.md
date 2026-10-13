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
[Block 2626]
དེ་ཡང་ཡུལ་ལ་སོགས་པའི་གྲངས་དྲིས་པ་དང་། ལན་ནི་གོ་སླའོ། །

[Block 2627]
ད་ནི་སྔར་གྱི་གཅིག་དང་དུ་བྲལ་ལ་སོགས་པ་དང་འདྲ་བའི་རང་བཞིན་སྦྱོར་བ་བསྟན་པའི་ཕྱིར། རང་བཞིན་ཅི་ལགས་དྲིས་པའི་ལན་དུ། རང་བཞིན་གདོད་ནས་མ་སྐྱེས་པ། །ཞེས་པ་ནི་རང་བཞིན་ཉིད་དུ་འབྲེལ་ཏེ། དེའི་ཁྱད་པར་ཅི་ཞེ་ན། ཨ་ཏ་ཨ་ནུཏྤ་ན་སྟེ།

[Block 2628 [VERSE]]
གདོད་མ་ནས་མ་སྐྱེས་པའི་ཕྱིར་རོ། །
དཔེར་ན་ཐམས་ཅད་ཆུའི་ཟླ་བ་ལྟ་བུའོ། །
འདོད་པས་ནི་གྲུབ་པའི་མཐས་སོ། །

[Block 2629]
ཡང་ན་འདོད་ན་སྟེ་ཟབ་མོ་ལ་མོས་ནའོ། །

[Block 2630 [VERSE]]
རྣལ་འབྱོར་མ་ནི་བོད་པའོ། །
ཤེས་རབ་ཀྱིས་ནི་གདམས་པའོ། །

[Block 2631]
ད་ནི་དཔེ་ལ་ངེས་པ་བསྐྱེད་པའི་མན་ངག་ཏུ་བསྟན་པའི་ཕྱིར་འདི་ལྟ་སྟེ་ཏདྱ་ཐཱ་སྟེ་དཔེར་ན་ཞེས་པའམ། འདི་ལྟ་བུ་སྟེ་གཞན་དག་ནི་གཙུབ་ཤིང་གཙུབ་གཏན་ཞེས་པ་ལ་སོགས་པ་ནི་ཆོས་ཐམས་ཅད་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཡིན་པས་ཆོས་ཐམས་ཅད་རང་བཞིན་མེད་པར་གཏན་ལ་དབབ་པའོ། །

[Block 2632]
ཡང་ན་གཙུབ་ཤིང་ནི་རྩ་ཨ་ཝ་དྷཱུ་ཏཱིའོ། །

[Block 2633]
གཙུབ་གཏན་ནི་ལྟེ་བའི་པདྨའོ། །

[Block 2634]
ལག་པའི་རྩོལ་བ་ནི་ལ་ལ་ནཱ་དང་ར་ས་ནཱ་གཉིས་ཏེ། དེ་གཉིས་ནས་རླུང་རྒྱུ་བས་ཨ་ཝ་དྷཱུ་ཏཱིའི་གནས་སུ་ཆུད་པ་དང་། རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་སྐྱེ་སྟེ། རུས༌[^1123]གྱི་གནད་ཅེས་བྱ་སྟེ། ལག་ཏུ་ལེན་པའི་བླ་མ་ལས་ཤེས་པར་བྱའོ། །

[Block 2635]
ད་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཆེ་བའི་མན་ངག་གིས་ལྟ་བ་རྟོགས་ནས། དེ་ནས་རྣལ་འབྱོར་མ་བདག་མེད་མ་ལ་སོགས་པས༌[^1124]མཆོད་པ་བྱས་ཏེ་གོ་སླའོ། །

[Block 2636]
དེ་ནས་བཅོམ་ལྡན་འདས་དགྱེས་ནས་ཞེས་པ་ནི་དམ་ཚིག་གི་མཆོད་པ་དང་། བདེ་མཆོག་སྡོམ་པའི་མཆོད་པས་སོ། །

[Block 2637]
རང་བྱིན་གྱིས་བརླབ་པ་ནི་བསྒོམ་པའི༌[^1125]མན་ངག་གིས་རང་གི་མཚན་ཉིད་ཉམས༌[^1126]སྐྱེས་པའོ། །

[Block 2638]
བསྟན་པ་ནི་དེའི་ཕྱིར་རོ། །

[Block 2639]
ཀྱེ་ཀྱེ་ནི་མཛེས་པས་བོད་པ་སྟེ་གནང་བ་སྦྱིན་པ་དང་ཉན་པ་ལ་སྦྱར་བ་སྟེ་གོ་སླའོ། །

[Block 2640]
ད་ནི་སྨྱོན་པའི་བརྟུལ་ཞུགས་ཆེན་པོའི་སྤྱོད་པ་དམ་ཚིག་དང་སྡོམ་པས་གཉུག་མའི་དབང་པོ་སྡངས༌[^1127]པར་བྱེད་པའི་ཐབས་དང་ཅུང་ཟད་སྨྱོན་པའི་བརྟུལ་ཞུགས་སྔར་གྱི་ལས་རྣམ་པ་གཞན་གྱིས་དབང་པོ་དང་བར་བྱིན་གྱིས་བརླབ་པའི་ཐབས་བསྟན་པའི་ཕྱིར། །བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ལ་སོགས་པ་བསྟན་ཏེ་གོ་སླའོ། །

[Block 2641]
དེ་ནས་རྡོ་རྗེ་སྙིང་པོས་གསོལ་ཞེས་པ་ནི་བདག་དྲི་བའི་སྐབས་ཡིན་པ་བཞིན་དུ་རྣལ་འབྱོར་མ་རྣམས་ཀྱང་མ་ཡིན་ཏེ། སྔར་དབང་པོའི་གྲངས་བསྟན་པའི་སྐབས་སུ།

[Block 2642 [VERSE]]
གཏི་མུག་རྡོ་རྗེ༌[^1128]ལ་སོགས་ལྡན། །
ཞེས་པ་གནང་བ་དེ་ཞུས་པའི༌[^1129]ཕྱིར་རོ། །

[Block 2643]
ཐམས་ཅད་ཡུལ་གྱི་རྣམ་དག་ནི་ལེའུ་དགུ་པར་སྒྱུ་མ་རྣམ་དག་གོ། །

[Block 2644]
དེའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་སོ། །

[Block 2645]
དབང་པོ་དྲུག་ལམ་གསུངས་པའི་བར༌[^1130]ལེའུ་དགུ་པར་མ་བསྟན་ཅིང་། དབང་པོའི་གྲངས་བསྟན་པའི་སྐབས་སུ་གནང་བ་མཛད་དེ་གསོལ་བ་ཞེས་སྔ་མར་འབྲེལ་ལོ། །

[Block 2646]
གཞན་དག་ནི་གོ་སླའོ། །

[Block 2647]
གོ་ཆ་ཞེས་བྱ་བ་ནི་ཐ་མལ་གྱི་དབང་པོ་སྤངས་ནས། ལྷའི༌[^1131]ས་བོན་ལས་མོས་པ་མི་མཐུན་པ་འཇུག་མི་ནུས་པས་ཀ་བ་ཙ་སྟེ་གོ་ཆའམ་ཁྲབ་བོ། །

[Block 2648]
སེམས་དཔའ་ཆེན་པོ་བོས་ནས་དགོས་པ་ཡོད་པར་བསྟན་པའོ། །

[Block 2649]
རྡོ་རྗེ་སྙིང་པོས་གསོལ་ཞེས་པ་ནི་གླེང་གཞི་དང་སྡོམ་པ་ལ་དགོས་པའི་ཡན་ལག་གི་ཐབས་རྣལ་འབྱོར་མ་ཀུན་ལ་གནང་བ་སྟེ། མ་ལུས་པར་བསམས་ནས་དྲིས་པའོ། །

[Block 2650]
དགོངས་པའི་སྐད་ཅི་ཞེས་པ་ནི་སྔར་གནང་ཡང་ངེས་པར་མ་གསུངས་སོ། །

[Block 2651]
བཅོམ་ལྡན་འདས་ཀྱིས་ངེས་པར་གསུངས་པ་ནི་བཤད་པར་རོ། །

[Block 2652]
རྣལ་འབྱོར་མའི་དམ་ཚིག་ཆེན་པོ་ནི་རྡོ་རྗེ་སྙིང་པོས་དྲིས་ཀྱང་རྣལ་འབྱོར་མ་ལ་ཐུགས་སྟོན་པས་མངོན་རྟོགས་སྐྱེས་པའོ། །

[Block 2653]
ཉན་ཐོས་ལ་སོགས་མི་ཤེས་པ། །ཞེས་པ་ནི་རང་རྒྱལ་བ་དང་ཕ་རོལ་ཕྱིན་པས་མི་ཤེས་པའོ། །

[Block 2654]
འོ་ན་བྱ་བའི་རྒྱུད་ལ་སོགས་པ་རྒྱུད་སྡེ་གཞན་གྱིས་ཀྱང་ཤེས་སམ་ཞེ་ན། དབང་གི་ཐབས་ཀྱིས་སྟོན་པའི་གླེང་གཞི་སྡོམ་ཡོད་ཀྱིས་ཀྱང་། དགོངས་པའི་སྐད་མ༌[^1132]བསྒྲགས་ཤིང༌[^1133]བཤད་པས་འདིར་ངེས་པར་བསྟན་པ་གོ་སླའོ། །

[Block 2655]
ད་ནི་ཉམས་སུ་ལེན་པ་སུ་དག་དང་སྨྲ་ཞེ་ན། དེའི་ཕྱག་རྒྱ་ནི་གཡུང་མོ་ལ་སོགས༌[^1134]གོ་སླའོ། །

[Block 2656]
ད་ནི་སྐད་ཀྱིས༌[^1135]མ་སྨྲས་པའི་སྐྱོན་བསྟན་པའི་ཕྱིར་རྡོ་རྗེ་སྙིང་པོ་ལ་སོགས་པའོ། །

[Block 2657]
དགྱེས་པའི་རྡོ་རྗེ་དབང་བསྐུར་ཞེས་པ་ནི་དབང་བསྐུར་བའི་དུས་སུའམ།

[Block 2658 [VERSE]]
ཡང་ན་དབང་ཐོབ་ནས་དུས་ཐམས་ཅད་དུའོ། །
རང་གི་དམ་ཚིག་རིགས་རྙེད་ནས། །

[Block 2659]
ཞེས་པ་ནི་ཁྱད་པར་གྱི་དུས་ཏེ་ཞིང་སྐྱེས་མ་ལ་སོགས་པ་རྙེད་ནས་སྤྱོད་པའི་ཚེའོ། །

[Block 2660]
ལེའུ་གསུམ་པའོ།། །།

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
--- END BLOCKS ---
