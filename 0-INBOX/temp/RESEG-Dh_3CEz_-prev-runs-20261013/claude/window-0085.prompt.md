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
[Block 2976]
ཁྲིམས་ནི་སིན་ཁྱ་སྟེ་བསླབ་པའི་རིམ་པའོ། །

[Block 2977]
གནས་ནི་བནྡྷན་ཛ་སྟེ། སྟོན་པའི་ཚིག་གམ་ནོད་པའི་གནས་སོ། །

[Block 2978 [VERSE]]
དེ་བཞིན་ཨ་ཧཾ་ཐོག་མ་ཉིད་ནས་སྐད་འདོན་པའོ། །
སྔགས་བཟླས་ནི་ཨཱ་ལི་ཀཱ་ལི་བསྡུས་པའོ། །

[Block 2979]
གང་དུ་ཞེ་ན།

[Block 2980 [VERSE]]
སྐྱེ་གནས་འཁོར་ལོ་ནི་ལྟེ་བར་རོ། །
རྣམ་པ༌[^1222]ཨ་ནི་ཨཾ་ཡིག་གོ། །
བདེ་ཆེན་གྱི་ཡང་ནི་སྤྱི་བོར་རོ། །
རྣམ་པ་ཧཾ་ནི་ཧཾ་ཡིག་གོ། །

[Block 2981]
གཅེར་བུ་སྐྲ་དང་ཁ་སྤུ་བྲེགས་ནི་ཐོག་མ་ཉིད་ནས་དགེ་སློང་ཉིད་དོ། །

[Block 2982]
ཁྱད་པར་ནི་ཅི་ཞེ་ན། གོང་གི་ཨ་ཧཾ་དང་ལྡན་པས་སྔགས་སྐྱེས་པའོ། །

[Block 2983]
ད་ནི་རྫོགས་པའི་སངས་རྒྱས་སུ་བསྟན་པས་སྐྲག་པའི་ཐེ་ཚོམ་དུ་གྱུར་པས་ནི་དེ་ནས་རྣལ་འབྱོར་མ་ལ་སོགས་པའོ། །

[Block 2984]
དེ་ནས་དེ་དབུགས་དབྱུང་བར་བྱ་བའི་ཕྱིར་ཡང་རྡོ་རྗེ་ཅན་གྱིས་ནི་དགྱེས་པའི་རྡོ་རྗེས་སོ། །

[Block 2985 [VERSE]]
ལྷ་མོ་ཐམས་ཅད་གཟིགས་ནས་ནི་འགྱེལ་བ་རྣམས་སོ། །
བསླང་བའི༌[^1223]ཕྱིར་ནི་དྲན་པ་རྙེད་ནས་དབུགས་དབྱུང་བའོ། །
ཡང་དག་པར་བསྟོད་པ་ནི་ཡོན་ཏན་བརྗོད་པའོ། །

[Block 2986]
ཅི་ཞེ་ན། ཁི་ཏོ་ཛ་ལ་སོགས་པ་མིང་ཁྱད་པར་ལྡན་པ༌[^1224]ལ་སོགས་པ་བསྡུས་པའི་ལྷ་མོ་སྤྱན་ལ་སོགས་པ་ཆོས་ཀྱི་སྣོད་ཡིན་པར་བསྟོད་པའོ། །

[Block 2987]
གང་ཞིག་སུས་ཀྱང་མི་ཤེས་པ་ནི་བྱང་ཆུབ་སེམས་དཔས་ཀྱང་ངོ་། །དེ་ཉིད་ང་ཡིས་སྤྲོ་ཡི༌[^1225]ཉོན་ནི་གདམས་པར་གནང་བའོ། །

[Block 2988]
བཅོམ་ལྡན་འདས་ཀྱི་གསུང་ནི་ལྷ་མོ་དག་ལ་བསྟོད་པ་དེ་དག་གོ། །

[Block 2989]
རྨི་ལམ་ལྟ་བུར་ཐོས་ནས་བརྒྱལ་བའི་སྐབས་སུ་ཡང་ཡང༌[^1226]དུ་དྲན་པས་སོ། །

[Block 2990]
ཐམས་ཅད་སྲོག་རྙེད་བར་འགྱུར་ནི་བརྒྱལ་བ་ཅུང་ཟད་སངས་པའོ། །

[Block 2991 [HEADING]]
#### དབུགས་གཉིས་པ་དབྱུང་བ། ^2-4-3-0

[Block 2992]
ད་ནི་དབུགས་གཉིས་པ་དབྱུང་བའི་ཕྱིར། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ནི་དྲན་པ་ཅུང་ཟད་རྙེད་པ་རྣམས་ལའོ། །

[Block 2993]
བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ་ནི་ལྷ་མོ་དག་ལ་བསྟོད་པ་དག་གོ། །

[Block 2994]
སེམས་ཅན་རྣམས་ནི་སངས་རྒྱས་ཉིད་ནི་སྟོང་པ་ཉིད་ནི་རྟོགས་པས་སོ། །

[Block 2995]
འོན་ཀྱང་གློ་བུར་དྲི་མས་བསྒྲིབས་ནི་སྟོང་པ་སངས་རྒྱས་ཀྱི་རང་བཞིན་ཡིན་ཡང་སྒྲིབ་པའོ། །

[Block 2996]
དེ་ཉིད་བསལ་ནས་སངས་རྒྱས་ཀྱི་སྒྲིབ་པ་དེ་ཉིད་བདག་མེད་པར་གསལ་བའི་སངས་རྒྱས་སོ། །

[Block 2997]
ལྷ་མོས་གསོལ་བ་ནི་དྲན་པ་བརྟན་པར་གྱུར་ནས་སོ། །

[Block 2998]
བཅོམ་ལྡན་འདས་དེ་དེ་བཞིན་ཏེ་སེམས་ཅན་གྱི་སེམས་བདག་མེད་པའི་དབང་དུ་བྱས་པའི་ཚེའོ། །

[Block 2999]
བདེན་ཏེ་ནི་དོན་དམ་དུའོ། །

[Block 3000]
བརྫུན་པ་མ་ལགས་ནི་ཀུན་རྫོབ་ཐབས་ཀྱི་དབང་དུ་བྱས་པས་སོ།[^1227] །ཡང་ན་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་དེ་མི་བརྫུན་པའོ། །

[Block 3001 [HEADING]]
#### དབུགས་གསུམ་པ་དབྱུང་བ། ^2-4-4-0

[Block 3002]
ད་ནི་དབུགས་གསུམ་པ་དབྱུང་བའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ༌[^1228]ནི་ལྷ་མོ་དག་རྟོག་པ་དང་ལྡན་པ་ལ།

[Block 3003 [VERSE]]
བདེ་བའི་ཉམས་བསྐྱེད་པའི་ཕྱིར་རོ། །
མི་ཤེས་བཙན་དུག་ཏུ་དཔེའོ། །

[Block 3004]
རྨོངས་སྤངས་དེ་ཉིད་ཀྱིས༌[^1229]ཞེས་པ་ནི་དཔེ་ལས་འབྱུང་བ་སྔར་གྱི་བདག་པོའོ། །

[Block 3005]
དེའི་མྱ་ངན་ཡོངས་སུ་གཅོད་ནི་སྟོང་པར་རྟོགས་པས་དབུགས་གཉིས་པ་ཕྱུང༌[^1230]ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3006]
དེ་བཞིན་དཔེ་ལྟར་རོ། །

[Block 3007]
ཞི་བའམ་ཐར་པ་ནི༌[^1231]བདག་མེད་པ་དཔེ་ལས་བྱུང་བའོ། །

[Block 3008]
ཐབས་ཤེས་རབ་ནི་བདེ་བའོ། །

[Block 3009]
དགྱེས་པའི་རྡོ་རྗེ་ལ་སོགས་པ༌[^1232]ནི་ལྷན་ཅིག་སྐྱེས་པའི་རོར་བྱས་པའོ། །

[Block 3010]
མ་རིག་པ་ལ་སོགས་པ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པའོ། །

[Block 3011]
གཏི་མུག་ལ་སོགས་པ་ནི་ཤེས་བྱའི༌[^1233]སྒྲིབ་པའོ། །

[Block 3012]
ཡང་ན་མ་རིག་པ་ལ་སོགས་པས་མི་འཛིན་ནི་སྔར་བདག་མེད་པར་བྱས་པས་སོ། །

[Block 3013]
གཏི་མུག་ལ་སོགས་པས་མི་འཆིང་ནི་ལྷན་ཅིག་སྐྱེས་པའི་བདེ་བས་སོ། །

[Block 3014]
རང་དང་རང་གི་བྱང་ཆུབ་ཕྱིར་ནི་གཉུག་མའི་ཡེ་ཤེས་ཡིན་པས་སོ། །

[Block 3015]
སངས་རྒྱས་མ་ཡིན་སེམས་ཅན་ནི། །ཞེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་གཉིས་ལས་གཞན་པའི་ལུས་སེམས་སོ། །
--- END BLOCKS ---
