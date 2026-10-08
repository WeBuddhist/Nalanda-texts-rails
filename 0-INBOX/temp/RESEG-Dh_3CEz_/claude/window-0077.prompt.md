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

[Block 2701]
མུམྨུ་སྟེ་རྣལ་འབྱོར་མའི་ལུས་དང་ཀ་ཀྐོ་ལ་སྟེ་གསང་བའི་གནས་སོ། །

[Block 2702]
གྷ་ཎ་སྟེ་ཕྲད་ཅིང་ཞུགས་པའོ། །

[Block 2703]
ཀྲྀ་པི་ཊ་ཧོ་བཛྲ་ཨི་གདུངས་ཤིང་བརྩེ་བའི་ངག་སྟོན་པས་སོ། །

[Block 2704]
ཀཱ་རུ་ཎི་ཀ་ཨ་ཨི་ཎ་རོལ་ཏེ་ཆགས་ཤིང་གདུངས༌[^1154]པའི་སེམས་ཤིན་ཏུ་འཕེལ་བའོ། །

[Block 2705]
དེ་ནས་ཌི་ཎྜི་མ་ཏ་ཧིནྣ་བཱཛྫི་ཨ་ཨི་སྟེ། དེས་གཡུང་མོ་ལ་སོགས་པ་ཡང་མི་སྤོང་བར༌[^1155]རོ། །

[Block 2706]
མ་ལ་ས་ཛ་འདུས་པ་ལུས་མཉམ་པར་སྦྱོར་བ་ཞུ་བདེ་ཆ་མཉམ་པའོ། །

[Block 2707 [HEADING]]
###### ཡོན་ཏན་སྤོང་བའི་ཁྱད་པར། ^2-4-1-2-2-0

[Block 2708]
དེ་ནས་ཡོན་ཏན་སྤོང་བའི་ཁྱད་པར་བ་ལ་ཁཱ་ཛྫ་ཨི་སྟེ་བདེ་བ་རྟོག་པ་སྤངས་ནས་མི་རྟོག་པ་ལ་འཇུག་པའོ། །

[Block 2709]
ག་ཌྷེཾ་མ་སྟེ་འབད་པས་ཞུ་བ་དང་མི་འབྲལ་ཞིང་། །འཐུངས་པས་དམ་ཚིག་ཏུ་ལུས་རྒུད་པ་མེད་པར་སྟོབས་ཅན་དུ་འབྱུང་ངོ་། །ཧ་ལེ་ཀཱ་ལི་སྟེ་ལྷན་ཅིག་སྐྱེས་པའི་སྐལ་བ་དང་ལྡན་པས་སོ། །

[Block 2710]
དུཾ་དུ་ར་ནི་སྐལ་མེད་སྤོང་བ་སྟེ་ཆགས་པ་ལ་སོགས་པའི་སྐལ་མེད་སྤོང་བའོ། །

[Block 2711]
དེ་ནས་ཚིག་རྐང་གཉིས་ཀྱིས་སྦྱོར་བ་སྔ་མ་བཞིན་ནོ། །

[Block 2712 [HEADING]]
###### ཡོན་ཏན་ཐོབ་པའི་ཁྱད་པར། ^2-4-1-2-3-0

[Block 2713]
ད་ནི་ཡོན་ཏན་ཐོབ་པའི་ཁྱད་པར་ནི་རྣལ་འབྱོར་མ་ལ་ཙ་ཨུ་ས་མ་ལ་སོགས་པ་ཕུང་པོ་ལྔའི་བདག་ཉིད་ཀྱི་རོ་བསྡུས་པ་ཞུ་བ་ཀུནྡ་ལྟ་བུར་ཨ་ཨི་བྷ་རུ་སྟེ། ལུས་གང་བས་འཇོག་གི་གཉུག་མའི་ཡེ་ཤེས་ཐོབ་པའོ། །

[Block 2714]
རྣལ་འབྱོར་མས་ནི་ཙ་ཨུ་ས་མ་ལ་སོགས་པ་འབྱུང་བ་ལྔའི་རོའི་བདག་ཉིད་འདུས་པ་ཉི་མའི་རྣམ་པ་ཅན་ཀུན་འདུས་ལུས་བཀང་བས་གཉུག་མའི་ལུས་ཐོབ་པའོ། །

[Block 2715]
ཚིག་རྐང་གཉིས་ཀྱིས་སྦྱོར་བ་ནི་འདིར་ཡང་སྔ་མ་བཞིན་ནོ། །

[Block 2716 [HEADING]]
###### དབྱེར་མེད་སྒོམ་པའི་ཁྱད་པར། ^2-4-1-2-4-0

[Block 2717]
ད་ནི་དབྱེར་མེད་སྒོམ་པའི་ཁྱད་པར་ནི་ཀུན་རྫོབ་བྱང་ཆུབ་སེམས་ཏེ་མན་ངག་གི་ཚུལ་དུ་གཟུང་བ་དང་དམ་ཚིག་ཏུ་བཟའ་བའོ། །

[Block 2718]
མན་ངག་གི༌[^1156]སྒྲུབ་པ་ནི་ས་འོག་ས་སྟེངས་ས་བླ་མ་ཡིན་པ་ནམ་མཁའི་དཀྱིལ་དུ་ཕྲེཾ་ཁ་ཎ་སྟེ། འགྲོ་འོང་གི་དོགས་པ་མེད་བར་མི་གཡོ་བར་གཟུང་བའོ། །

[Block 2719]
དམ་ཚིག་གི་ཚུལ་ནི་ལག་པ་དང་སྣོད་མ་ཡིན་པར་དག་པ་དང་མ་དག་པར་གཙང་བ་དང་མི་གཙང་བ་མེད་པར་ལྕེས་བླང་ངོ་། །དེ་ཡང་མན་ངག་དག་གིས་གཟུང་བ་ནི་ནི་རཾ་ཤུ་སྟེ། ལུས་ཐམས་ཅད་རུས་པ་དང་འདྲ་བར་བརྒྱན་པ་གཉུག་མའི་བདེ་བ་ལ་འཇུག་གོ། །

[Block 2720]
དེ་ཡང་དམ་ཚིག་ཏུ་ཟོས་པས༌[^1157]ཏ་ཧིཾ་ཛ་ས་ར་ཝའི་རོ་དང་འདྲ་བར་རྟོག་པ་མེད་པར་འཇུག་གོ། །

[Block 2721]
གཡུང་མོ་མི་སྤོང་བ༌[^1158]དང་ཀུན་དུ་རུ་ནི་སྔ་མ་ལྟར་གཞན་དག་ལ་སྦྱར་རོ། །

[Block 2722 [HEADING]]
##### རང་ལུས་ཐབས་དང་ལྡན་པ། ^2-4-1-3-0

[Block 2723]
རང་ལུས་ཐབས་དང་ལྡན་པ་ནི། ཀོ་ལ་ཨི་རི་ཊྛི་སྟེ་མགོ་བོའི་གནས་སོ། །

[Block 2724]
བོ་ལ་སྟེ་ཧཾ་ངོ་། །མུམྨུ་སྟེ་ལྟེ་བའོ། །

[Block 2725]
ཀཀྐོ་ལ་སྟེ་ཨཾ་ངོ་། །གྷ་ཎ་སྟེ་བྱང་ཆུབ་ཀྱི་སེམས་རྒྱུན་སྟེང་འོག་ཏུ་འདུས་པའོ། །

[Block 2726]
ཀྲྀ་པི་ཊ་སྟེ་ནཱ་དའི་སྒྲ་སྐྲའི་རྩེ་མོ་དབབ་པས་ཕྲ་བའོ། །

[Block 2727 [VERSE]]
ཀཱ་རུ་ཎི་སྟེ་ཆགས་པས་ནང་དུ་བལྟས་པའོ། །
ཨ་ཨི་ན་སྟེ་ཕྱི་རོལ་དུ་མི་གཡེངས༌[^1159]པས་སོ། །
བ༌[^1160]ལ་ཁཱཛྫ་སྟེ་ཕྱི་རོལ་གྱི་རྟོག་པ་སྤངས་པའོ། །

[Block 2728]
གཌྷེཾ་སྟེ་ནང་གི་རོ་མྱང་བའོ། །

[Block 2729]
ཧ་ལེ་ཀཱ་ལི་སྟེ་རླུང་སྐལ་བ་དང་ལྡན་པར་ནང་དུ་བཅུག་པས་སོ། །

[Block 2730]
དུཾ་དུ༌[^1161]ར་སྟེ་ཕྱི་རོལ་གྱི་རྟོག་པ་གཟུང་བའི་ཡུལ་སྤང་ངོ་། །ཙ་ཨུ་ས་མ་ལ་སོགས་ཉོན་མོངས་པ་ལྔའོ། །

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
--- END BLOCKS ---
