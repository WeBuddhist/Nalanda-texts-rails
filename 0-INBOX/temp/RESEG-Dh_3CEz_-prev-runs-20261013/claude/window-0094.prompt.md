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
[Block 3291]
སྡེར་ལ་གསུམ་སྟེ་རབ༌[^1323]ཞིང་གི་པགས་པ། འབྲིང་དུར་ཁྲོད་ཀྱི་རས། ཐ་མ་ཤིང་ལོའི་སྡེར་རོ། །

[Block 3292]
ཇི་ལྟར་བཟའ་བའི་ཚུལ་ཚོད་མ་དང་བཅས་པ་དང་། དེ་སྐད་དུ།

[Block 3293 [VERSE]]
ལྟོས་ཤིག་དགའ་བ་ཡི་ནི་ཆོས། །
འདི་ལ་རྣམ་རྟོག་ཡོད་མ་ཡིན། །
བྲམ་ཟེ་ཁྱི་དང་གདོལ་པ་གསུམ། །
རང་བཞིན་གཅིག་ལས་ལྷན་ཅིག་བཟའ། །

[Block 3294]
ཞེས་གསུངས་སོ། །

[Block 3295]
བཏུང་བའི་གཙོ་བོ་སུ་ར་སྟེ་ཅུང་ཟད་ཙམ་དང་། ཇི་ལྟར་བཏུང་བའི་ཚུལ་སྣོད་དང་བཅས་པའོ། །

[Block 3296 [HEADING]]
###### **ཚོགས།** ^2-6-1-4-2-2-0

[Block 3297]
ཚོགས་ལ་གཉིས་ཏེ་ལས་དང་པོ་པས་ཡོན་ཏན་དང་ལྡན་པའི་ཕྱག་རྒྱས༌[^1324]གཡས་སུ་འདུག་སྟེ་བསྒོམ་པ་དང་། ལས་སྨིན་བས་བགྲོད་དང་བགྲོད་མིན་དུ་མཆོད་པས་འབྲས་བུ་དང་བཅས་པའོ། །

[Block 3298]
འདིའི་དོན་ནི་མངོན་པར་རྟོགས་པ་སྟེ་དམ་ཚིག་བསྒྲུབ་པ་དབང་བསྐུར་བ་དང་རབ་ཏུ་གནས་པ་དང་། དངོས་གྲུབ་བསྒྲུབ་པ་དཔའ་བོའི་སྟོན་མོ་ཙམ་དང་ག་ཎ་ཙ་ཀྲ་ལ་བརྟེན་པའོ། །

[Block 3299 [HEADING]]
###### **ལས་དང་པོ་པས་ཡོན་ཏན་དང་ལྡན་པའི་ཕྱག་རྒྱས་གཡས་སུ་འདུག་སྟེ་བསྒོམ་པ།** ^2-6-1-4-2-2-1-0

[Block 3300]
ཚོགས་ཀྱི་འཁོར་ལོ་ནི་གནས་དབེན་པར་ཡོ་བྱད་རྣམས་ཚོགས་པར༌[^1325]བྱས་ཏེ། རྣལ་འབྱོར་མ་རྣམས་དང་པ་རྣམས་ཚོགས་པར༌[^1326]བྱས་ལ་དང་པོར་བྱ་བའི་རིམ་པ་ཐིག་གདབ་པ་དང་མཎྜལ་བྱ་སྟེ། མཆོད་པ་བཤམས་ཏེ་གདན་རྣམས་ལ་རང་གི་རྒྱན་དང་བཅས་པས་ལྷ༌[^1327]སོ་སོར་དགོད་དོ། །

[Block 3301]
དེ་ནས་ལས་ཀྱི་རྡོ་རྗེ་མཆོད་པ་ནས་ཚོགས་དང་། ཚད་མེད་པ་དང་སྟོང་པ་ཉིད་དང་ར་བ་དང་དྲ་བ་དང་རྟེན་གྱི་རྣལ་འབྱོར་བསྒོམས་ཏེ་སྦྱོར་བ་གསུམ་མམ་ཡན་ལག་དྲུག་བསྒོམས་ལ། དེ་ནས་བླ་མས་དཀྱིལ་འཁོར་བསྒྲུབ་པའི་ཚུལ་དུ་རྣལ་འབྱོར་པ་རྣམས་ལྷར་བསྐྱེད་པ་དང་ཡེ་ཤེས་པར་བསྒྲུབ་བ༌[^1328]བྱའོ། །

[Block 3302]
ཕྱོགས་མཚམས་ཀྱི་རྣལ་འབྱོར་པ་རྣམས་ནི་རང་རང་གི་ལྷར་མོས་ཤིང་བསྐྱེད་ལ། དེ་ནས་ལས་ཀྱི་རྡོ་རྗེས་ཚོགས་བརླབས་སྤྱན་དྲངས་ལ་དབུལ་བའི་རིམ་པ་མཎྜལ་བྱས་ལ་རིམ་བཞིན་དུ་དབུལ། ཚོགས་དབུལ་བ་ལ་སློབ་དཔོན་གྱིས་བྱིན་གྱིས་བརླབ་པའི༌[^1329]གླུ་དང་གར་བྱའོ། །

[Block 3303]
སློབ་མ་རྣམས་རང་གི་མན་ངག་བསྒོམ་མོ། །

[Block 3304 [HEADING]]
###### **ལས་སྨིན་བས་བགྲོད་དང་བགྲོད་མིན་དུ་མཆོད་པས་འབྲས་བུ་དང་བཅས་པ།** ^2-6-1-4-2-2-2-0

[Block 3305]
དེ་ནས་ཅི་རིགས་པར་བྱའོ། །

[Block 3306 [VERSE]]
དབང་བསྐུར་རམ་རབ་གནས་བྱེད་ན་དུས་དེར་བྱའོ། །
དངོས་གྲུབ་བསྒྲུབ་པ་ནི་ཡང་དང་ཡང་དུ་བྱའོ། །
དཔའ་བོའི་སྟོན་མོ་ནི་ལྷའི་ང་རྒྱལ་ཙམ་གྱིས་བྱའོ། །
ག་ཎ་ཙཀྲའི་ལྡང་ཚད་ཀྱང་ཤེས་པར་བྱའོ། །

[Block 3307]
ལེའུ་དྲུག་པ་དང་བདུན་པའོ།། །།

[Block 3308 [HEADING]]
### ལེའུ་བརྒྱད་པ། ^2-7-0

[Block 3309]
དེ་ནས་རྣལ་འབྱོར་མ་ཞེས་བྱ་བ་ལ་སོགས་པས་བརྟགས་ནས། ལས་ཀྱི་ཕྱག་རྒྱ༌[^1330]ཆེན་པོ་ཇི་ལྟ་བུ་ཞེས་དྲིས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། །ཞེས་པ་ལ་སོགས་པ་ལན་གསུངས་ཏེ། གང་ཟག་བཞི་ལས་ཆགས་ཅན་འདུལ་བ་ལ་དགོངས་ནས་ལྷ་མོ་རིགས་བཞི་སྟེ། གླང་པོ་ཅན་དང་དུང་ཅན་དང་པདྨ་ཅན་དང་རི་བོང༌[^1331]ཅན་ཏེ་འདིར་ནི་པདྨ་ཅན་བསྟན་ཏོ། །

[Block 3310]
རྡོ་རྗེའི་རིགས་དང་རིན་པོ་ཆེའི་རིགས་དང་པདྨའི་རིགས་དང་ལས་ཀྱི་རིགས་ཏེ་གོ་རིམས་བཞིན་དུ་སྦྱར༌[^1332]རོ། །

[Block 3311]
དེ་ནས་རྣལ་འབྱོར་མ་ལ་སོགས་པས་སྨོན་ལམ་གདབ་པ་ཞུས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ནི་དད་པ་ཅན་འདུལ་བ་སྟེ། བསྐྱེད་པའི་རིམ་པ་ལ་སྨོན་ལམ་གདབ་པ་དང་རྫོགས་པའི་རིམ་པ་ལ་གདབ་པའོ། །

[Block 3312]
རིགས་སུ་སྐྱེ་དང་ཞེས་བླ་མ་ལ་འཇིག་རྟེན་པའི་རིགས་བཙུན་པའམ། ཡང་ན་ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་དུ་སྐྱེ་བ་དང་། དམ་ཚིག་མ་ཉམས་པ་དང་། དགྱེས་པའི་རྡོ་རྗེ་ཕྱིན་ཅི་མ་ལོག་པར་སྟོན་པ་དང་།

[Block 3313 [VERSE]]
ལག་པ་རྡོ་རྗེ་དྲིལ་བུ་འཁྲོལ། །
ཟབ་མོའི་ཆོས་ནི་ཀློག་པ་དང་། །

[Block 3314]
ཞེས་པ་སྟེ་ལུས་དང་ངག་དང་ཡིད་དེ་ལྷའི་རྣལ་འབྱོར་དང་། བཟླས་པ་དང་བསྒོམ་པ་དེ་དང་ལྡན་པའི་བླ་མ་དེ་འདྲ་བ་དང་།

[Block 3315 [VERSE]]
སྐྱེ་བ་གང་དུ་སྐྱེས་ཀྱང༌[^1333]ཕྲད་པར་ཤོག་ཅིག༌[^1334]པའོ། །
ཡང་ན་རང་ཉིད་དེ་བཞིན་སྐྱེ་བར་ཤོག་ཅེས་བྱའོ། །

[Block 3316]
བཙུན་མོ་ཞུ་བ་ཞེས་བྱ་བ་ནི་ཐིག་ལེ་བསྒོམ་པ་དང་། རྫོགས་རིམ་དེ་ཁོ་ན་བསྒོམ་པ་བླ་མ་དང་རང་ཡང་དེ་དང་ཕྲད་པར་ཤོག་ཅེས་པའོ། །

[Block 3317]
ལྷ་མོ་དེ་དགྱེས་ནས་ཞེས་པ་གཏི་མུག་ཅན་འདུལ་བའི་ཐབས་ཞུས་བ། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ལན་ཏེ།

[Block 3318]
དང་པོ་གསོ་སྦྱོང་སྦྱིན་པ་ནི་བསྙེན་གནས་ནས་བཟུང་ལ༌[^1335]དགེ་ཚུལ་དང་དེ་ཅི་རིགས་པར་སྦྱིན་ནོ། །

[Block 3319]
དེ༌[^1336]རྗེས་བསླབ་པའི་གནས་བཅུ་ནི་མི་དགེ་བ་བཅུ་སྤང་བ་བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པ་སྦྱིན་པའོ། །

[Block 3320]
དེ་ལ་བྱེ་བྲག་སྨྲ་བ་བསྟན་པ་ནི་སོ་སོར་ཐར་པ་དང་ལྡན་པ་ལ་བྱེ་བྲག་ཏུ་སྨྲ་བའི་གྲུབ་མཐའ་བསྟན་ཏེ། གཟུང་བའི་ཡུལ་རྡུལ་ཕྲ་རབ་དང་ནང་འཛིན་པའི་སེམས་གཉིས་ཡོད་པར་སྟོན་པའོ། །

[Block 3321]
མདོ་སྡེ་པ་ཡང་དེ་བཞིན་ནོ། །ཞེས་པ་དགེ་སློང་གི་སྡོམ་པ་དང་ལྡན་པ་ལ་མདོ་སྡེ་པའི་གྲུབ་མཐའ་བསྟན་པའི་ཕྱིར་གཟུང་བའི་ཡུལ་འདུས་པར་སྣང་ཞིང་ནང་འཛིན་པའི་སེམས་ཀྱང་ཡོད་དེ་རྣམ་པ་དང་བཅས་པ་དེ་སྦྱོར་བ༌[^1337]དང་ནི་བསྐོར་བ་དང་། བར་མེད་རྣམ་པར་གནས་ཀྱང་རུང་། །ཞེས་བྱའོ། །

[Block 3322]
དེ་ནས་རྣལ་འབྱོར་སྤྱོད་པ་བསྟན། །ཞེས་པ་བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པ་དང་ལྡན་པ་ལ་སེམས་ཙམ་བསྟན་ཏེ། རྣམ་བཅས་དང་རྣམ་མེད་དེ་རྣམ་པ་སྣ་ཚོགས་པ་ཤེས་པ་གཅིག་ཏུ་བདེན་པའོ། །

[Block 3323]
རྣམ་མེད་ནི་བརྟགས་ཏེ་ཤེས་པ་ཤེལ་དག་པ་ལྟ་བུར་སྣང་བ་སྟེ། རིགས་པས་འགྲུབ་ཅིང་རིགས་པས་མི་གནོད་པར་འདོད་པའོ། །

[Block 3324]
དེའི་རྗེས་སུ་དབུ་མ་བསྟན་པ་ནི་སྒྱུ་མར་སྨྲ་བ་དང་རབ་ཏུ་མི་གནས་པའོ། །

[Block 3325]
སྒྱུ་མར་སྨྲ་བ་ནི་རྣམ་བཅད་ཡང་དག་པར་བཅད་ནས་ཡོངས་གཅོད་སྒྱུ་མར་འདོད། རབ་ཏུ་མི་གནས་པ་ནི་སྤྲོས་པའི་མཐའ་བཞི་བཅད་ནས་ཁས་ལེན་ཡང་མེད་པའོ། །

[Block 3326]
སྔགས་ཀྱི་རིམ་པ་ཀུན་ཤེས་ནས་ནི་བྱ་བ་དང་སྤྱོད་པ་དང་རྣལ་འབྱོར་རྒྱུད་དེ་ཕྱི་རོལ་དབྱིབས༌[^1338]ཀྱི་རྣལ་འབྱོར་བསྟན་པའོ། །

[Block 3327]
དགྱེས་པའི་རྡོ་རྗེ་མཐར་ཐུག་ཕྱག་རྒྱ་ཆེན་པོ་ལྷན་ཅིག་སྐྱེས་པ་བསྟན་པའོ། །

[Block 3328]
དེ་སྐད་དུ།

[Block 3329 [VERSE]]
དང་པོ་ཞིང་ནི་སྦྱང་བའི༌[^1339]ཕྱིར། །
དྲུག་ཅུ་པ་ཡི་ཁ་ཟས་གདབ། །
དེ་ནས་འབྲུ་རྣམས་རིམ་གྱིས་གདབ། །
ཕྱི་ནས་འབྲས་དཀར་ས་བོན་ནོ། །

[Block 3330 [VERSE]]
བསླབ་ཚིག་ལྔ་པའི་རིམ་པ་ཡིས། །
རྒྱུད་ནི་དེ་ལྟར་སྦྱང་བར་བྱ། །
--- END BLOCKS ---
