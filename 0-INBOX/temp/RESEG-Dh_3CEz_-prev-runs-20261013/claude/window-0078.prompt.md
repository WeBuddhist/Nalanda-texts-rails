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
[Block 2731]
ག་ཎ་བཟའ་སྟེ་དེ་དག་རང་རིག་འོད་གསལ་དུ་མི་རྟོག་པའོ། །

[Block 2732]
ཕྲེཾ་ཁ་ཎ་སྟེ་སྟེང་ནས་བྱང་ཆུབ་ཀྱི་སེམས་རྒྱུ་བ་དང་འོག་ནས་རླུང་དང་འོད་ཟེར་རྒྱུ་བ་སྟེ་དེ་གཉིས་ལ་ཤུདྡྷ་ཨ་ཤུདྡྷ་སྟེ། བཟང་ངན་དུ་མི་རྟོག་གོ། །

[Block 2733]
ནི་རཾ་ཤུ་སྟེ་ཞུ་བ་འདུས་པ་སྟེ་ཡང་སར་པ་སྟེ་རོ་དང་འདྲ་བའི་བདེ་བ་ལ་མི་རྟོག་པ་སྐྱེ་བའོ། །

[Block 2734]
དེ་ལྟར་དེ་ཉིད་གཡུང་མོ་ལ་སོགས་པ་ལྟོས་པ་མེད་ཅིང་སྤང་བླང་མེད་པར་ནང་གི་ཀུན་དུ་རུའི་སྦྱོར་བའོ། །

[Block 2735 [HEADING]]
##### གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོ། ^2-4-1-4-0

[Block 2736]
གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོ་ལ་དྲུག་སྟེ། ལྟ་བ་དང་སྤྱོད་པ་དང་སྒོམ་པ་དང་དབང་པོ་རང་སྣང་དང་སྤྱོད་ལམ་དང་བསྲེ་བ་དང་། འབྲས་བུ་ལ་སོགས་པའོ། །

[Block 2737 [HEADING]]
###### ལྟ་བ། ^2-4-1-4-1-0

[Block 2738]
དེ་ལ་ལྟ་བ་ནི་ཀོ་ལླ་ཨི་རེ་སྟེ་དངོས་པོ་རཱུ་པ་ལ་སོགས་པ་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ཐབས་ཀུན་དུ་སྣང་བའོ། །

[Block 2739]
མུམྨུ་ཎི་ནི༌[^1162]གཅིག་དང་དུ་བྲལ་གྱིས་ཤེས་བྱ་སྟོང་ཞིང་བདག་མེད་པ་མི་རྟོག་ཅིང་མི་དམིགས་པ་བདག་མེད་པའི་ཤེས་རབ་བོ། །

[Block 2740]
དེ་གཉིས་དབྱེར་མེད་པར་བྱས་པའོ། །

[Block 2741 [HEADING]]
###### སྤྱོད་པ། ^2-4-1-4-2-0

[Block 2742]
སྤྱོད་པ་ལ་གཉིས་ཏེ་སྤྱོད་པ་དང་སྤྱོད་པའི་རྒྱུ་མཚན་ནོ། །

[Block 2743 [HEADING]]
###### **སྤྱོད་པ།** ^2-4-1-4-2-1-0

[Block 2744]
སྤྱོད་པ་ནི་ག་ཎ་སྟེ་ཅུང་ཟད་སྨྱོན་པའི་རྡོ་རྗེ་ཐོད་པའི་སྤྱོད་པས་ང་རྒྱལ་དུ་བསྒོམ་པ་དང་། ཀྲྀ་པི་ཊ་སྟེ་ཅང་ཏེའུའི་སྒྲས༌[^1163]བཟླས་པ་བྱེད་པའོ། །

[Block 2745 [HEADING]]
###### **སྤྱོད་པའི་རྒྱུ་མཚན།** ^2-4-1-4-2-2-0

[Block 2746]
སྤྱོད་པའི་རྒྱུ་མཚན་ནི་ཀཱ་རུ་ཎ་སྟེ་སེམས་ཅན་ཀུན་ལ་སྙིང་རྗེ་འཇུག་པ་དང་། བ་ལ་ཁཱ་ཛྫ་སྟེ་ཞེ་སྡང་མེད་པར་རྣམ་པར་རྟོག་པའི་སྟོབས་བཟའ་བའི་ཟས་དང་ག་ཌྷེཾ་མ་ཨ་ཎི་པ་སྟེ་བདེ་བའི་རོ་འཐུང༌[^1164]བའི་སྒོམ་པ༌[^1165]དང་ལྡན་པ་སྟེ་འབད་པའི་ཚུལ་གྱིས་སྤྱོད་པ་བྱེད་དོ། །

[Block 2747 [HEADING]]
###### སྒོམ་པའི་རྟེན་བསྟན་པ། ^2-4-1-4-3-0

[Block 2748]
ཡང་སྒོམ་པའི༌[^1166]རྟེན་བསྟན་པ༌[^1167]ནི་ཧ་ལེ་ཀཱ་ལིཉྫ་སྟེ་རྣམ་པར་མི་གཡེང་བའི་དབང་པོ་ཡེ་ཤེས་ཀྱི་སྐལ་བ་ཅན་བསྟེན་པའོ། །

[Block 2749]
དུཾ་དུ་ར་སྟེ་སྐལ་མིན་ནི་ཡིད་ཀྱི་རྗེས་སུ་འབྲང་བའི་ཐ་མལ་པའི་དབང་པོ་སྤངས་པའོ། །

[Block 2750 [HEADING]]
###### དབང་པོ་རང་སྣང། ^2-4-1-4-4-0

[Block 2751]
དབང་པོ་རང་སྣང་ནི་སྐལ་ལྡན་གྱི་དབང་པོ་དང་པོར༌[^1168]བྱེད་པ་དང་། དབང་པོ་དེའི་བྱིན་རླབས་རང་སྣང་བ་སྟེ་དོན་གྱི་ཚུལ་གཉིས་སོ། །

[Block 2752]
དེ་ཡང་ཙ་ཨུ་ས༌[^1169]མ་ནེ་གཟུགས་སྡུ་གུ༌[^1170]ཀཙྪུ་རི་སྒྲ་སྙན་པ་སི་ཧླ༌[^1171]དྲི་ཞིམ་པ་ཀཔྤུ་ར་རོ་ཞིམ་པོ་མ་ལ་སཱ་ཛ་རེག་བྱ་འཇམ་པ་ལ་སོགས་པའོ། །

[Block 2753]
སོགས་པ་ལྔ་པོ་འདོད་པའི་ཡོན་ཏན་ལྔ་སྟེ་གཟུགས་ལ་སོགས་པའོ། །

[Block 2754]
བྷ་རུ་ཁ་སྟེ་བཀང་ཞིང་ཚིམ་པས་དབང་པོ་དང་བ་དང་། ཁེངས་པར་ཟོས་ཤིང་འཐུངས་པས་བྱིན་རླབས་མི་རྟོག་པར་སྣང་བའོ། །

[Block 2755 [HEADING]]
###### སྤྱོད་ལམ་དང་བསྲེ་བ། ^2-4-1-4-5-0

[Block 2756]
སྤྱོད་ལམ་དང་བསྲེ་བས༌[^1172]ནི་འཇུག་པ་དང་སྤྱོད་པའོ། །

[Block 2757]
འཇུག་པ་ནི་བཟའ་བ་ལ་སོགས་པ་གང་ལ་འཇུག་ཀྱང་། ཁ༌[^1173]ཊ་ཀ་ར་སྟེ་འཇུག་དང་འགྲོ་བ་མི་རྟག་དང་། ཕྲེཾ་ཁ་ཎ་འོང་ཞིང་བཟློག་པ་མི་རྟག་པའོ། །

[Block 2758]
སྤྱོད་པ་ནི་ཤུདྡྷ་སྟེ་དག་པ་དང་མ་དག་པ་དང་གཙང་བ་དང་མི་གཙང་བ་དང་། ཡིད་དུ་འོང་བ་དང་མི་འོང་བ་ལ་སོགས་པ་ཞེན་པ་ཙམ་དུ་མི་བྱའོ། །

[Block 2759 [HEADING]]
###### འབྲས་བུ་རྫོགས་པ། ^2-4-1-4-6-0

[Block 2760]
འབྲས་བུ་རྫོགས་པ་ནི་ལྟ་བ་ལ་སོགས་པ་ཀུན་གྱི་འབྲས་བུ་ཆེན་པོ་སྟེ། རྟེན་ལུས་དང་བརྟེན་པ་སེམས་ཐབས་ཤེས་རབ་དབྱེར་མེད་དོ། །

[Block 2761]
རྟེན་ཡང་ལུས་ཅན་ཀུན་ལ་གནས་པ་ནི་རཾ་ཤུ་སྟེ་དབང་པོ་དང་བའི་དབུས་སུ་ཞུ་བ་དེ་རྫོགས་པའི་ཐབས་སོ། །

[Block 2762]
བརྟེན་པ་སེམས་ནི་སྟེ༌[^1174]རོ་དང་འདྲ་བར་རྣམ་པར་རྟོག་པའི་ཟུག་རྔུ་མེད་པས་མི་རྟོག་པ་རང་རྣལ་དུ་འཇུག་པ་སྟེ་ཤེས་རབ་བོ། །

[Block 2763]
ད་ནི་དབྱེར་མེད་བསྟན་པའི་ཕྱིར་མ་ལཱ་ཛེ་སྟེ་ཆུ་དང་འོ་མ་དང་། ནམ་མཁའ༌[^1175]བཞིན་དུ་ཀྱེ་ཨཾ་འདུས་ཤིང་དབྱེར་མེད་པའོ། །

[Block 2764]
དེ་ཡང་ཀུན་དུ་བ་ཏ་ཨི་སྟེ་རང་རིག་པ་ཀུན་དུ་རུ་སྟེ་ཀུན་དུ་སྦྱོར་བའོ། །

[Block 2765]
བརྟེན་པ་སེམས་ནི་ས་ར་བ་སྟེ་རོ་དང་འདྲ་བར་རྣམ་པར་རྟོག་པའི་ཟུག་རྔུ་མེད་པས་ཉི་མའི་འོད་ཟེར་དྲོ་གསལ་གྱིས་ཀུན་ལ་ཁྱབ་པ་བཞིན་དུ་ལུས་ཀྱི་དངས་མ་དང་སེམས་ཀྱི་དངས་མ་དབྱེར་མེད་དེས་གཡུང་མོ་ལ་སོགས་པ་རིགས་ངན་པ་དང་། བཟང་པོ་ལ་ཁྱད་པར་མེད་པར་འབྲས་བུ་མ་ཧཱ་མུ་དྲ་དེ་ལྕགས་ཀྱི་ཁང་རུམ་འབར་བ་སྣང་ཡང་མི་སྦྱོར། དེ་བཞིན་དུ་ཡི་དགས་དང་ལྷའི་ལོངས་སྤྱོད་ཀུན་དུ་སྣང་ཡང་མི་སྦྱོར་རོ། །

[Block 2766]
ཌིཎྜི་མ་སྟེ་གཡུང་མོ་ལ་སོགས་པ་མི་སྤང་བ་སྟེ། རང་རིག་གི་འོད་ཟེར་མཐའ་ཡས་པ་སྣང་བས་འབྱུང་བ་ལྔ་དང་ཡེ་ཤེས་ལྔ་ལ་སོགས་པ་རིགས་ཀྱི་དབྱེ་བ་ཡོངས་སུ་རྫོགས་པའོ། །

[Block 2767]
ཡང་ན་བླ་ན་མེད་པའི་རིགས་དབྱེ་བ་ཡོངས་སུ་རྫོགས་པའོ། །

[Block 2768]
དེ་ལྟར་བྱས་པས་རྟགས་གསུམ་འབྱུང་སྟེ་འཛིན་པའི་རྟགས་དངོས་གྲུབ་གྲུབ་པའི་རྟགས་དེ་ཁོ་ན་ཉིད་ལ་འཇུག་པའི་རྟགས་སོ། །

[Block 2769]
ཡང་ན་ལྟ་བའི་རྟགས་བསྒོམ་པའི་རྟགས་ཙརྱའི་རྟགས་སོ། །

[Block 2770]
དཔལ་དགྱེས་པ་རྡོ་རྗེའི་རྒྱུད་ནས་རྡོ་རྗེའི་གླུ། བརྟག་པ་གཉིས་ཀྱི་དོན་ཡང་འདིར་གནས་ཤིང་ལམ་གྱི་རིམ་པ་ཉེ་བར་རྫོགས་པ་ན་ཐ་མར༌[^1176]ཕྱག་རྒྱ་ཆེན་པོར་ཉེ་བར་གནས་པའོ། །
--- END BLOCKS ---
