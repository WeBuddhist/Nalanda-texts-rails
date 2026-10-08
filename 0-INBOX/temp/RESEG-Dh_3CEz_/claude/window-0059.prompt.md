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
[Block 2066 [VERSE]]
ཀྱེའི་རྡོ་རྗེས་གསུངས་མཚན་ཉིད། །
སྐྱེ་བ་བདུན་པ་དེ་ནས་བརྟག །

[Block 2067]
ཅེས་པ་ནི། སྐྱེ་བ་བདུན་པའི་ཤ་བཟའ་བ་སྟེ། དེ་ཡང༌[^904]བརྟག་པ་ནི་ནང་གི་བརྟག་པ་དང་ཕྱིའི་བརྟག་པའོ། །

[Block 2068 [HEADING]]
##### ནང་གི་བརྟག་པ། ^1-11-1-1-0

[Block 2069]
ནང་གི་བརྟག་པ་ནི། དགའ་བྲལ་དགའ་བ་ལ་སྨོད་པ། །ཞེས་ལས་ཀྱི་ཕྱག་རྒྱའི་དགའ་བ་སྤོང་བ་དང་། མིག་དང་ལྡན་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཤིན་ཏུ་ཆེ་བའོ། །

[Block 2070 [HEADING]]
##### ཕྱིའི་བརྟག་པ། ^1-11-1-2-0

[Block 2071]
ཕྱིའི་བརྟག་པ་ནི།

[Block 2072 [VERSE]]
སྐད་སྙན་མིག་དང་ལྡན་པ་ནི། །
ཞེས་པ་ནི་མིག་དཀར་ནག་ཕྱེད་པའོ། །

[Block 2073]
དྲི་ལུས་གཟི་བརྗིད་ཆེན་པོ་ནི་ལུས་ལ་དྲི་བཟང་པོ་ཡོད་པ་དང་། གང་ཟག་གཞན་པས་གཟི་བརྗིད་ཆེ་བ་དང་། དེའི་གྲིབ་མ་བདུན་དུ་འགྱུར་བ་ནི་ཟླ་བ༌[^905]ཉའི་དུས་སུ་བྱ་རྒོད་ཀྱི་རྗེ་ངར་གྱི་སྦུབས་རྣམ་པར་སྣང་མཛད་ཀྱིས་བྱུགས་ལ། བལྟས་ན་དེའི་གྲིབ་མ་བདུན་བྱུང་ན་སྐྱེ་བ་བདུན་པར་ཤེས་པར་བྱའོ། །

[Block 2074 [VERSE]]
དེ་ནི་ཟོས་པ་ཙམ་གྱིས་ནི། །
སྐད་ཅིག་ལ་ནི་མཁའ་སྤྱོད་འགྱུར། །
ཞེས་པ་ནི་དེའི་ཤ་བཟའ་བ་སྟེ།
རྒྱལ་པོ་ཨིནྡྲ་བྷཱུ་ཏིའི་གཏམ་རྒྱུད་ལྟ་བུའོ། །

[Block 2075 [VERSE]]
ཡང་ནི༌[^906]དེའི་བཀའ་དྲིན་ནོད་པ་ཡིན་ནོ། །
རྫོགས་པའི་རིམ་པ་ལྟར་ན་ནི།
ཀྱེའི་རྡོ་རྗེ་གསུང་མཚན་ཉིད། །

[Block 2076]
ཅེས་པ། དགྱེས་པ་རྡོ་རྗེའི་རྒྱུད་འབུམ་ཚོ་ལྔའི་ནང་དུ་སྐྱེ་བ་བདུན་པའི་བརྟག་པ་གསུངས་པ་སྟེ། སྐྱེ་བ་བདུན་པས་ནི་ཉི་མ་མཚོན་པ་སྟེ། ཟླ་བ་བྱང་ཆུབ་ཀྱི་སེམས་བཟའ་ཞེས་བྱའོ། །

[Block 2077 [VERSE]]
གང་གི་དུས་སུ་ཞེ་ན།
དགའ་བྲལ་དགའ་བ་ལ་སྨོད་པ། །

[Block 2078]
ཞེས་པ་ལྷན་ཅིག་སྐྱེས་པའི་དགའ་བའི་དུས་སུའོ། །

[Block 2079]
ལན་བདུན་པས་ནི་འགྲུབ་པར་འགྱུར། །ཞེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པ་དེ་བསྒོམས་པའི༌[^907]ཡོན་ཏན་སྐད་སྙན་མིག་དང་ལྡན་ཞེས་པ་ལ་སོགས་པ་སྐྱེ་བ་བདུན་པའི་ཡོན་ཏན་རྣམས༌[^908]འབྱུང་ངོ་། །

[Block 2080]
ད་ནི་རིམ་པ་གཉིས་ཀྱི་ཧེ་བཛྲའི་སྒྲུབ་ཐབས་བསྟན་ནས་རྒྱུད་འདིར་ལྷ་གཞན་གྱིས་མི་འགྲུབ་ཅེ་ན་འགྲུབ་པར་བསྟན་པའི་ཕྱིར། [^909]ཀུ་རུ་ཀུལླེའི་སྒྲུབ་ཐབས་བཤད་པར་བྱ་སྟེ། གོང་དུ་བརྟག་པ་བཅུ་གཉིས་པར།[^910] རྒྱས་པར་གསུངས་པ་མདོ་རུ་བསྡུ། །ཞེས་བྱ་བ་ནི་དགྱེས་པའི་རྡོ་རྗེ་འབུམ་ཚོ་ལྔ་པ་རུ། ཀུ་རུ་ཀུལླེའི༌[^911]ཤློ་ཀ་ནི་ཁྲི་ཕྲག་གསུམ་གསུངས་ལ། །བརྟག་པ་ནི་བཅུ་གཉིས་རྒྱས་པར་གསུངས་པ་དེ་རྩ་བའི་རྒྱུད་མདོར་བསྡུས་པ་འདི་རུ་བསྡུས་ནས་སྟོན་པར་བྱེད་པ་སྟེ། དེའི༌[^912]དོན་ནི་སྔོན་དུ་དགྱེས་པའི་རྡོ་རྗེའི་བསྙེན་པ་རྫོགས་པའམ།

[Block 2081 [HEADING]]
#### འདི་ཉིད་ཀྱི་བསྙེན་པ། ^1-11-2-0

[Block 2082]
ཡང་ན་འདི་ཉིད་ཀྱི་བསྙེན་པ་བྱ་སྟེ། དེ་ཡང་ལུགས་གཉིས་ཏེ། དཔའ་མོ་གཅིག་པ་དང་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོའོ། །

[Block 2083 [HEADING]]
##### དཔའ་མོ་གཅིག་པ། ^1-11-2-1-0

[Block 2084]
དཔའ་མོ་གཅིག་པར་བསྒོམ་པར་འདོད་པས་ཚོགས་བསགས་པ་དང་། བསྲུང་བ་མཚམས་ཀྱི་འཁོར་ལོའི་ནང་དུ་རྡོ་རྗེ་རྣམ་བཞིའམ་ས་བོན་ཕྱག་མཚན་ཙམ་ལ། ཧྲཱིཿལས་བྱུང་བའི་ལྷ་མོ་ནི།

[Block 2085 [VERSE]]
ཁ་དོག་དམར་ཞིང་ཕྱག་བཞི་མ། །
མདའ་དང་གཞུ་ཡི་ལག་པ་མ། །
ཨུཏྤ་ལ་དང་ལྕགས་ཀྱུ་འཛིན། །
འདི་ནི་བསྒོམས་པ་ཙམ་གྱིས་ནི། །

[Block 2086]
ཞེས་པ་དེ་ལ་ཡེ་ཤེས་བསྟིམ་པ་དང་སྐྱེ་མཆེད་བྱིན་གྱིས་བརླབ་པ་དང་། སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་བརླབ་པ་དང་། [^913]དབང་བསྐུར་བ་དང་མཆོད་བསྟོད་བདུད་རྩི་མྱང་བ་བྱས་ལ། བཟླས་པའི་མཐུར་ཐུག་པར་བྱའོ། །

[Block 2087 [HEADING]]
##### དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ། ^1-11-2-2-0

[Block 2088]
དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ནི་སྲུང་བ་མཚམས་ཀྱི་འཁོར་ལོ་ཡན་ཆད་སྔ་མ་བཞིན་བྱས་ལ། ཆོས་ཀྱི་འབྱུང་གནས་ཀྱི་ནང་དུ་རྟེན་གཞལ་ཡས་ཁང་ལེའུ་བརྒྱད་པ་ལྟར་བསྒོམས་ལ། བརྟེན་པ་ལྷ་བསྒོམ་པ་ནི་ལེའུ་བརྒྱད་པ་ལྟར༌[^914]མངོན་པར་བྱང་ཆུབ་པ་རྣམ་པ་ལྔའི་དབུས་སུ་རྡོ་རྗེ་ཀུ་རུ་ཀུལླེ། ཤར་ཕྱོགས་སུ་སངས་རྒྱས་ཀུ་རུ་ཀུལླེ། །ལྷོ་ཕྱོགས་སུ་རིན་ཆེན་ཀུ་རུ་ཀུལླེ། ནུབ་ཕྱོགས་སུ་པདྨ་ཀུ་རུ་ཀུལླེ། བྱང་ཕྱོགས་སུ་སྣ་ཚོགས་ཀུ་རུ་ཀུལླེ། མངོན་པར་བྱང་ཆུབ་པ་རྣམ་པ༌[^915]ལྔའི་རྐང་ཐོན་དུ་བསྐྱེད་པར་བྱ། ས་བོན་དང་། ཕྱག་མཚན་དང་སྐུ་མདོག་ཆ་བྱད་ཐམས་ཅད་མཐུན་པར་བྱ་སྟེ་དབང་གི་ལས་བསྒྲུབ་པའི་ཕྱིར་རོ། །

[Block 2089]
དེ་ལ་སེམས་དཔའ་སུམ་བརྩེགས༌[^916]ནས་ཡེ་ཤེས་ཀྱི་འཁོར་ལོ་སྤྱན་དྲངས། བྱིན་གྱིས་བརླབ་དབང་བསྐུར་མཆོད་བསྟོད་བདུད་རྩི་མྱང་བའི་བར་དུ་བྱས་ལ་ཐུན་བཞིའི་རིམ་པས་བཟླས་པ་བྱ་བ་ནི་མཚན་མ་ཐོབ༌[^917]པའི་བར་དུ་བྱའོ། །

[Block 2090]
དེ་ནས་བསྒྲུབ་པ་བྱ་བ་ནི་ཆོ་ག་སྔ་མ་དང་འདྲ་བ་ལས།

[Block 2091]
རང་གི་ཐུགས་ཀ་དང༌[^918]ལྷའི་ཐུགས་ཀ་ནས་འོད་ཟེར་ལྕགས་ཀྱུའི་ཚུལ་གྱིས་རྡོ་ཁབ་ལེན་ལྟར་བསྒྲུབ་པར་བྱ་བའི་ལུས་ངག་ཡིད་གསུམ་རང་དབང་མེད་པར་འོང་བར་བསམ་མོ། །

[Block 2092]
འདི་རུ་བྱམས་པ་ཆེན་པོ་ནི་མན་ངག་གོ། །

[Block 2093]
སྔགས་ལ་ནི་སོ་སོའི་མིང་ལ་བ་ཤིཾ་ཀ་ར་ན་ཧཱུཾ་ཕཊ་སྭཱ་ཧཱ་སྤེལ་ལོ། །

[Block 2094]
དེའི་གྲངས་ཀྱི་ཚད་ནི། །འབུམ་ཕྲག་གཅིག་གིས་རྒྱལ་པོ་ནི་བསོད་ནམས་ལས་གྲུབ་པས་སོ། །

[Block 2095 [VERSE]]
ཕལ་པ་ཉིད་ནི་དམན་པས་གྲངས་ཉུང་པའོ། །
ཕྱུགས་ནི་དུད་འགྲོའི་གཙོ་བོ་སྟེ་ཀླུའོ། །

[Block 2096]
གནོད་སྦྱིན་ཡང་གླེགས་བམ་ལ་ལར་བཀྵ་ན་བྱ་བ་བྱ་སྟེ། ཡཀྵ་ཡིན་པས་གནོད་སྦྱིན་ནོ། །

[Block 2097]
དེ་དག་ལ་གྲངས་མང་བར་བྱ་བ་ནི་འགྲོ་བ་གཞན་དུ་གཏོགས་ཤིང་མ་རུངས་པས་སོ། །

[Block 2098]
ལྷ་མ་ཡིན་ཡང་དེ་བཞིན་ནོ། །

[Block 2099]
ལྷ་ནི་འགྲོ་བ་གཞན་པས་བསོད་ནམས་ལྷག་པས་སོ། །

[Block 2100]
སྔགས་པ་གྲངས་ཉུང་བ་ནི་འགྲོ་བ་གཅིག་པ་དང་། དམ་ཚིག་གིས་བརྩེ་བའི་ཕྱིར་རོ། །

[Block 2101 [VERSE]]
རྡོ་རྗེ་སྙིང་པོ་ནི་སྡུད་པ་པོས་ཞུས་པས་སོ། །
མངོན་པར་བྱང་ཆུབ་ནི་རིམ་པ་གཉིས་སོ། །

[Block 2102]
བརྟག་པ་ནི་ཆོ་ག་ཞི་བ་མོའོ།[^919] །རྒྱལ་པོ་ནི་དེ་ཁོ་ན་ཉིད་དམ་རྫོགས་པའི་རིམ་པ་དང་ལྡན་པས་སོ། །

[Block 2103 [VERSE]]
ལེའུ་བཅུ་གཅིག་པ་ནི་ལྷག་མའོ། །
བརྟག་པ་དང་པོ་རྫོགས་སོ།། །།

[Block 2104 [HEADING]]
## བརྟག་པ་ཕྱི་མ། ^2-0

[Block 2105 [HEADING]]
### དང་པོ་རབ་གནས་ཀྱི་ལེའུ། ^2-1-0
--- END BLOCKS ---
