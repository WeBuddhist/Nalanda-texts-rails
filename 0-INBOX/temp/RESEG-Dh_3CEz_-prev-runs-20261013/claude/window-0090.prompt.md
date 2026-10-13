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
[Block 3151]
ཁྲོ་བོའི་འདི་ཡིན་ཏེ།

[Block 3152 [VERSE]]
འབྲས་བུ་ཧེ་རུ་ཀའི་ང་རྒྱལ་གྱིས་བཟླས་པ་བྱའོ། །
སྔགས་ཀྱི་འབྲས་བུའི་དོན་ནི་གཞན་དུ་ཤེས་པར་བྱའོ། །

[Block 3153]
དེ་ནས་ལྷ་མོ་དེ་དགྱེས་ནས་ཞེས་པ་ལ་སོགས་པ་སྒྲུབ་པའི་དཀྱིལ་འཁོར་ཞུས་པའོ། །

[Block 3154 [HEADING]]
#### ཉིད་ཀྱི་དཀྱིལ་འཁོར་བྲི་བར་མཛད། ^2-5-1-0

[Block 3155 [HEADING]]
##### སྔོན་བྱུང། ^2-5-1-1-0

[Block 3156]
དེ་ལ་སྟོན་པ་ཞེས་པ་ནས། ཉིད་ཀྱི་དཀྱིལ་འཁོར་བྲི་བར་མཛད། །ཅེས་པ་ནི་སྔོན་བྱུང་དང་རྗེས་འཇུག༌[^1285]རྣམ་པ་གཉིས་ཏེ། སྔོན་བྱུང་དུ་ཁྲོ་ཆགས་རྣམ་པ་གཉིས་དང་ལྡན་པའི་རྡོ་རྗེ་འཆང་ཆེན་པོས་དཀྱིལ་འཁོར་བྲི་བ་བསྟན་ཏོ། །

[Block 3157 [HEADING]]
##### རྗེས་འཇུག། ^2-5-1-2-0

[Block 3158]
རྗེས་སུ་འཇུག་པ་ནི་ཉིད་ཀྱི་ཞེས་པས་གང་ཟག་བཞིའི་རིམ་པ་སྟོན་ཏེ། ཐོས་བསམ་གྱི་མཐར་ཕྱིན་པའི་རྟགས་མ་ཐོབ་ཀྱི་བར་དུ་ལས་དང་པོ་པའི་གང་ཟག་ཡིན་ཏེ། རང་ཉིད་ཀྱིས་དཀྱིལ་འཁོར་ལ་སོགས་པའི་ལས་ཐམས་ཅད་བྱའོ། །

[Block 3159]
གཉིས་པ་གསུམ་པ་ཕབ་སྟེ་བྲི།[^1286] །ཞེས་པ་ཅུང་ཟད་ཡེ་ཤེས་ལ་དབང་བ་ནི་དབང་པོ་སྤྲིན་དང་འདྲ་བའི་རྟགས་དང་། མངོན་པར་ཤེས་པ་གཅིག་ཙམ་ཐོབ་པ་དང་།

[Block 3160]
གསུམ་པ་ཡེ་ཤེས་ལ་དབང་བའི་རྟགས་ནི་དུ་བ་དང་། སྲིན་བུ་མེ་ཁྱེར་དང་མངོན་པར་ཤེས་པ་གསུམ་ཙམ་ཐོབ་པ་དང་། ཁྱེའུ་དང་བུ་མོ་གཞོན་ནུ་མ་ལས་ཡེ་ཤེས་ཕབ་སྟེ་འདྲི་རུ་གཞུག་གོ། །

[Block 3161]
ཡང་དག་པའི་ཡེ་ཤེས་ལ་དབང་བའི་རྟགས་ནི་ནམ་མཁའ་ལྟ་བུ་མཐོང་བ་དང་། མངོན་པར་ཤེས་པ་ལྔ་ཐོབ་པས་དཀྱིལ་འཁོར་སྤྲུལ་ལ་དབང་བསྐུར་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3162 [HEADING]]
#### སྒྲུབ་པ། ^2-5-2-0

[Block 3163]
དེའི་དོན་ནི་འདི་ཡིན་ཏེ་སྔར་བསྟན་པས་བསྙེན་པ་རྫོགས་ནས། དེ་ནས་སྒྲུབ་པ་ནི་སའི་ཆོ་ག་དང་སྟ་གོན་གྱི་ཆོ་ག་དང་དབང་བསྐུར་བའོ། །

[Block 3164 [HEADING]]
##### སའི་ཆོ་ག། ^2-5-2-1-0

[Block 3165]
དེ་ལ་སའི་ཆོ་ག་ནི་ལེའུ་བཅུ་པ་ནས་བཤད་པ་བཞིན་དུ་བྱས་ལ།

[Block 3166 [HEADING]]
##### སྟ་གོན་གྱི་ཆོ་ག། ^2-5-2-2-0

[Block 3167]
སྟ་གོན་དུ་གནས་པ་དང་བུམ་པ་དང་སློབ་མ་སྟ་གོན༌[^1287]ནི་བརྟག་པ་ཕྱི་མའི་ལེའུ་དང་པོར་བཤད་པ་ལྟར་བྱའོ། །

[Block 3168]
བུམ་པ་སྟ་གོན་ནམ༌[^1288]གྲངས་ནི་རྒྱས་པར་བསྡུ་ན་བཅུའམ་དྲུག་སྟེ། རྣམ་པར་རྒྱལ་བ་དང་། ལྷ་མོ་བརྒྱད་ཀྱི་བུམ་པ་དང་། ལས་ཐམས་ཅད་པ་དང་བཅུའོ། །

[Block 3169]
ཡང་ན་རྣམ་རྒྱལ་གཙོ་བོའི་བུམ་པ་དང་ལྷ་མོ་བརྒྱད་པོ་རིགས་བཞི་རུ༌[^1289]བསྡུས་ལ་ལྔ། ལས་ཐམས་ཅད་པ་དང་དྲུག་གོ། །

[Block 3170]
གང་བའི་བུམ་པ་ནི་ཅི་རིགས་པར་ཤེས་པར་བྱའོ། །

[Block 3171]
ལྷ་སོ་སོའི་མཚན་མས་མཚན་ལ༌[^1290]རིན་པོ་ཆེའི་བུམ་པའམ་གཞལ་ཡས་ཁང་དུ་བསྐྱེད། པཾ་ལས་པདྨ་འདབ་བརྒྱད་བསྐྱེད་ལ། རྣམ་པར་རྒྱལ་བའི་བུམ་པར་ས་བོན་ཙཾ་ལས་ལྷ་ཚང་བར་བསྐྱེད། ཡེ་ཤེས་པ་སྤྱན་དྲངས་ལ་མཆོད་བསྟོད་བཟླས་པ་བྱས་ལ་ལྷ་ཞུ་བར་བསམ་མོ། །

[Block 3172]
གཞན་དག་ལ་ལྷ་རེ་རེའམ། ལྷ་གཉིས་གཉིས་བསྐྱེད་ལ་ཆོ་ག་སྔ་མ་བཞིན་བྱའོ། །

[Block 3173]
དེ་ནས་སློབ་མའི་སྟ་གོན་ནི་ཁྲུས་བྱས་ཏེ་ཀུན་གྱིས་མཎྜལ་ཕུལ་ལ། དགའ་ཆེན་ཁྱོད་བདག་སྟོན་པ་བས། །ཞེས་བྱ་བ་ལ་སོགས་པས་གསོལ་བ་གདབ་པ་དང་། བུ་ཚུར་ཐེག་པ་ཆེན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྤྲོ་བ་བསྐྱེད་ལ། བདུན་རྣམ་པར་དག་པས་སྦྱང་བ་བྱ། དེ་ནས། ཐུབ་པ་ཉི་མ་མ་ལུས་པ།[^1291] །ཞེས་བྱ་བས་སྡོམ་པ་ལ་གསོལ་བ་གདབ། རྟོག་པ་རྣམས་ནི་ལེགས་པར་བསྡུས་ནས་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སྡོམ་པ་བཤད། སྡོམ་པ་དཔོག་གོ། །

[Block 3174]
དེ་ནས་སེམས་བསྐྱེད་པ་གསང་བ་སྟ་གོན་ལ་གནས་ཏེ་མཆོད་པར་བྱའོ། །

[Block 3175]
དེ་ནས་སོ་ཤིང་དོར་བའི་ཆོ་ག་བྱ། ཧུབ་གསུམ་གྱིས་ཆུ་བླུད། ཀུ་ཤ་སྦྱིན་སྲུང་སྐུད་གདགས་ལ་ཟབ་ཅིང་རྒྱ་ཆེ་བའི་ཆོས་བཤད་པར་བྱའོ། །

[Block 3176]
དེ་ནས་འབྱོར༌[^1292]ན་སྦྱིན་སྲེག་གིས་ལྷག་པར་གནས་པར་ཡང་བྱའོ། །

[Block 3177]
རྨི་ལམ་མ་བརྗེད་པར་བསྒོས་ལ་ཉལ་ཁང་དུ་གཏང་། དེ་དག་གི་ཆོ་གར་བྱ་བ་ནི་མཚོ་སྐྱེས་ཀྱི་དཀྱིལ་འཁོར་གྱི་ཆོ་ག་ལྟར་ཤེས་པར་བྱའོ། །

[Block 3178]
དེ་ནས་ནང་པར་སྔར་ལངས་ལ་རྨི་ལམ་བརྟག །མཆོད་བསྟོད་བྱ་སྟེ། སྟ་གོན་གྱི་དཀྱིལ་འཁོར་ནམ་མཁའ་ལ་བཏེག་ལ་ཉི་ཟླ་ཁ་སྦྱར་དུ་བཅུག །དབྱངས་ཡིག་གིས་རྒྱས་གདབ་པར་བྱའོ། །

[Block 3179]
ཐིག་དང་ཚོན་ནི་ལེའུ་བཅུ་པ་ལྟར་ཤེས་པར་བྱའོ། །

[Block 3180 [VERSE]]
དཀྱིལ་འཁོར་གྱི་མཚན་ཉིད་བསྟན་པ་ནི།
འཕར་མ་གཅིག་དང་སྒོ་བཞི་པ། །

[Block 3181]
ཞེས་བྱ་བ་ནས།

[Block 3182]
བརྒྱད་པ་ཟེ་བ་བཅས་པར་བྲི། །ཞེས་བྱ་བའི་བར་དུ་དཀྱིལ་འཁོར་གྱི་རྣམ་དག་སྔར་བཞིན་ཤེས་པར་བྱའོ། །

[Block 3183]
དེ་ནས་མཚན་མ་ཙ་ཀླི་དགོད་པ་ནི།

[Block 3184 [VERSE]]
སྙིང་པོར༌[^1293]བསྐྱེད་པའི་ཐོད་པ་ཉིད། །
མདོག་དཀར་ཆ་ནི་གསུམ་པ་བྲི། །

[Block 3185]
དེའི་རྗེས་སུ་དབུས་སུ་ཐོད་པ་དཀར་པོ་ཡང་ཚིག་གཉིས་སྦྱར་རོ། །

[Block 3186]
དེ་ནས། དབང་ལྡན་དུ་ནི་ཤ་ར་བྷ། །ཞེས་བྱ་བ་ནས། ཕྱག་མཚན་བརྒྱད་དུ་རབ་ཏུ་གྲགས། །ཞེས་པ་སྟེ་རང་རང་གི་སྔགས་ལ་དེ་ཉིད་གསུམ་སྤེལ་ཞིང་ལྷ་རུ་མོས་པ་དགོད་པར་བྱའོ། །

[Block 3187]
དེ་ནས་བུམ་པ་དགོད་པ་ནི་དེ་ནས་རྣམ་རྒྱལ་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་བུམ་པའི་ཡོ་བྱད་ཐམས་ཅད་གསོས་གདབ་སྟེ། སྟ་གོན་གྱི་གནས་ནས༌[^1294]རོལ་མོ་དང་བཅས་པས་སྤྱན་དྲངས་ལ་རྣམ་པར་རྒྱལ་བའི་བུམ་པ་ནི་གཙོ་བོའི་སྤྱན་སྔར་གཞག་པར་བྱའོ། །

[Block 3188]
བུམ་པ་གཞན་རྣམས་ནི་རང་རང་གི་གནས་ལ་ཉེ་བར་གཞག༌[^1295]གོ། །

[Block 3189]
ལས་ཐམས་ཅད་པའི་བུམ་པ་ནི་སྒོའི་གཡས་ཕྱོགས་སུ་དགོད་པར་བྱའོ། །

[Block 3190]
དེ་བཞིན་དུ་མཆོད་པ་ཐམས་ཅད་ཀྱང་ཉེ་བར་བཤམ། བླ་རེ་དང་རྒྱན་དང་གདུགས་དང་བདན་ལ་སོགས་པ་དང་རྟ་བབས༌[^1296]དང་རོལ་མོ་དང་། ན་བཟའི་བྱེ་བྲག་ཐམས་ཅད་ཀྱང་ལྷ་རྣམས་ལ་རས་ཟུང་རེ་རེ་དབུལ་བར་བྱའོ། །
--- END BLOCKS ---
