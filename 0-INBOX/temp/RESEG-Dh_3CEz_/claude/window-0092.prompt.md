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
[Block 3221]
དེ་ནས་ཆགས་བྲལ་གྱི་དབང་བསྐུར་བ་བསྟན་པ་ནི།

[Block 3222]
རྡོ་རྗེ་མཆོད་པས་ཡང་སྦྱར་ནས། །

[Block 3223 [VERSE]]
ལྷ་དེ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཞུས་པའོ། །
བཅོམ་ལྡན་འདས་བཀའ་སྩལ་ཞེས་བྱ་བ་ནི་ལན་ཏེ།

[Block 3224 [HEADING]]
###### **དེར་ནི་ཐོག་མ་ཐ་མ་མེད།** ^2-5-2-3-1-2-1-0

[Block 3225 [VERSE]]
དེར་ནི་ཐོག་མ་ཐ་མ་མེད། །
སྲིད་མེད་མྱ་ངན་འདས་པ་མེད། །
འདི་ནི་མཆོག་ཏུ་བདེ་ཆེན་ཉིད། །
བདག་མེད་གཞན་ཡང་མེད་པ་ཉིད། །

[Block 3226]
ཅེས་པ་སྟེ་འདིས་ནི་བྱ་རོག་གི་མིག་དང་འདྲ་བར་སྔ་མ་དང་ཕྱི་མ་གཉིས་ཀྱི་དོན་གཏན་ལ་འབེབས་ཏེ། ཤེས་བྱའི་དབང་དུ་བྱས་ཏེ་བཤད་པ་དང་། སྔ་ཕྱིའི་དོན་ལྷན་ཅིག་སྐྱེས་པར་གཏན་ལ་དབབ་པ་དང་། རྫོགས་པའི་རིམ་པ་མངོན་རྟོགས་ཅིག་ཅར་སྟོན་ཏོ། །

[Block 3227 [HEADING]]
###### **དང་པོ་ཤེས་བྱའི་དབང་དུ་བྱས་ཏེ་བཤད་པ།** ^2-5-2-3-1-2-1-1-0

[Block 3228]
དང་པོ༌[^1307]ནི་ཐོག་མ་སྟེ་དངོས་པོ་སྐྱེ་བར་མ་གྲུབ། དབུས་གནས་པ་མ་གྲུབ། ཐ་མ་འགག་པར་མ་གྲུབ། སྲིད་མེད་འཁོར་བའི་དངོས་པོ་ཐམས་ཅད་ཀྱང་མི་གནས་སོ། །

[Block 3229]
མྱ་ངན་ལས་འདས་པར་ཡང་མི་གནས་སོ། །

[Block 3230]
བདག་དང་གཞན་མེད་པ་སྟེ་གཟུང་བ་དང་འཛིན་པའི་དངོས་པོ་ཡང་མེད་དེ།[^1308] འདིར་ནི་མཆོག་ཏུ་བདེ་ཆེན་ནི་འབྲས་བུའི་མཚན་ཉིད་དེ་མ་བཅོས་པའི་རང་བྱུང་གི་ཡེ་ཤེས་ཆེན་པོ་སྟོན་ཏོ། །

[Block 3231 [HEADING]]
###### **སྔ་ཕྱིའི་དོན་ལྷན་ཅིག་སྐྱེས་པར་གཏན་ལ་དབབ་པ།** ^2-5-2-3-1-2-1-2-0

[Block 3232]
ཡང་ཐོག་མར་དགའ་བའི། [^1309]དབུས་མ་མཆོག་དགའ། ཐ་མ་དགའ་བྲལ་ལོ། །

[Block 3233]
སྲིད་མེད་མྱ་ངན་འདས་མེད་ནི་ལྷན་ཅིག་སྐྱེས་པའི་དགའ་བ་སྟེ་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་དབྱེར་མེད་པའོ། །

[Block 3234]
འདི་ནི་མཆོག་ཏུ་བདེ་ཆེན་ཉིད་ནི་ཟག་པ་མེད་པའི་དོན་གྱི་ཡེ་ཤེས་མཚོན་པའོ། །

[Block 3235]
བདག་མེད་གཞན་མེད་ཅེས་བྱ་བ་ནི་བདག་གཞན་གྱི་རྟོག་པ༌[^1310]འགགས་པའོ། །

[Block 3236 [HEADING]]
###### **རྫོགས་པའི་རིམ་པ་མངོན་རྟོགས་ཅིག་ཅར་སྟོན་པ།** ^2-5-2-3-1-2-1-3-0

[Block 3237]
ཡང་སིད་མེད་ཅེས་པ་ཕྱི་སྣོད་ཀྱི་འཇིག་རྟེན་དང་། ནང་བཅུད་ཀྱི་སེམས་ཅན་ཐམས་ཅད་རྟེན་དང༌[^1311]བརྟེན་པའི་དཀྱིལ་འཁོར་དུ་བསྡུ། མྱ་ངན་ལས་འདས་པ་མེད་ཅེས་པ་ནི། རྟེན་དང་བརྟེན་པའི་དཀྱིལ་འཁོར་ཧེ་རུ་ཀ་དང་བདག་མེད་མར་བསྡུས་པའོ། །

[Block 3238]
བདག་མེད་གཞན་མེད་ནི་བདག་མེད་མ་ཡང་ཧེ་རུ་ཀ་ལ་བསྡུ་བའོ། །

[Block 3239]
དེར་ཐོག་མ་དབུས་མཐའ་མེད་ནི་ཐུགས་ཀའི་ཟླ་བ་དང་ཉི་མ་ནི་དབུས་ཀྱི་ཡི་གེ་ཧཱུཾ་ལ་བསྡུ་བའོ། །

[Block 3240]
ཧཱུཾ་ཡང་ཞབས་ཀྱུ་ལ་དེ་འ༌[^1312]ལ་འ༌[^1313]ཡང་ཧ་ལའོ། །

[Block 3241]
ཧ་ནི་ཟླ་ཚེས་ལའོ། །

[Block 3242]
ཟླ་ཚེས༌[^1314]ནི་ཐིག་ལེ་ལའོ། །

[Block 3243 [VERSE]]
ཐིག་ལེ་ནཱ་ད་མར་མེ་ལྟར་ཕྲ་བའོ། །
འདི་ནི་མཆོག་ཏུ་བདེ་ཆེན་ཉིད། །

[Block 3244]
ཅེས་བྱའོ། །

[Block 3245]
ལྷན་ཅིག་སྐྱེས་པའི་ཡེ་ཤེས་སྤྲོས་པ་ཐམས་ཅད༌[^1315]དང་བྲལ་བ་བསྒོམ་པའོ། །

[Block 3246]
ད་ནི་དབང་བསྐུར་བའི་ཐབས་བསྟན་པ་ནི།

[Block 3247 [VERSE]]
ལོངས་སྤྱོད་ཀྱི་ནི་རླབས་ཉིད་ལ། །
རང་གི་གཡས་དང་ལག་གཞན་གྱི། །
མཐེ་བོང་དང་ནི་སྲིན་ལག་གང་། །
དེ་ནི་རྣལ་འབྱོར་པ་ཡིས་བཙིར། །

[Block 3248]
ཞེས་པ་ལ་ལ་ནཱ་དང་ར་ས་ནཱ་གཉིས་རང་གི་ལག་པ་དང་བླ་མའི་ལག་པས་བཙིར་བ་སྟེ། དེ་ལས་དགའ་བ་བཞི༌[^1316]རིམ་གྱིས་ཡེ་ཤེས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3249]
དེ་ལ་ཅི་ཞིག་སྐྱེ་ཞེ་ན། གཞོན་ནུའི་དགའ་བ་ཇི་ལྟ་བའམ། ལྐུགས་པའི་རྨི་ལམ་ཇི་ལྟ་བ། །ཞེས་བྱ་སྟེ་ཉམས་སུ་མྱོང་བ་བརྗོད་དུ་མེད་པའི་དཔེའོ། །ཇི་ལྟར་མཚོན་དུ་བཏུབ་ཅེ་ན།

[Block 3250 [VERSE]]
མཆོག་གི་མཐའ་དང་དགའ་བྲལ་དབུས། །
སྟོང་དང་སྟོང་མིན་ཧེ་རུ་ཀ །

[Block 3251]
ཞེས་པ་སྟེ་མཆོག་གི་མཐའ་ནི་མཆོག་དགའ་བའོ། །

[Block 3252]
དགའ་བྲལ་དབུས་ནི་དགའ་བྲལ་ཡང་ཡིན་ལ་དབུས་ཡིན་ཏེ་མཆོག་དགའི་རྗེས་ལ་བྱ་ཞེས་བྱའོ། །

[Block 3253]
ཐ་མ་ནི་ལྷན་ཅིག་སྐྱེས་པ་སྟེ། དེའི་དོན་སྟོང་པ་དང་ཞེས་པ་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་མོ། །

[Block 3254]
སྟོང་མིན་ནི་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ཏེ་དཔལ་ཧེ་རུ་ཀ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3255]
ཁ་ཅིག་ནི་དགའ་བྲལ་དབུས་ཞེས་བྱ་བ་ནི་དགའ་བྲལ་ཐ་མར་ཏེ། གསུམ་པར་ལྷན་ཅིག་སྐྱེས་པ་ཡིན་ཞེས་ཟེར་རོ། །

[Block 3256]
འདི་ལ་བརྟག་པ་མང་དུ་ཡོད་མོད༌[^1317]ཀྱང་སྤྲོས་པ་མང་དུ་དོགས་པས་མ་བྱས་སོ། །

[Block 3257]
དབང་དེ་རྣམས་བསྐུར་བའི་ཐབས་ནི་བླ་མ་ལས་ཤེས་པར་བྱའོ། །

[Block 3258]
ལེའུ་ལྔ་པའོ།། །།

[Block 3259 [HEADING]]
### ལེའུ་དྲུག་པ་དང་བདུན་པ། ^2-6-0

[Block 3260]
ད་ནི་བྲིས་སྐུ་དང་གླེགས་བམ་ལ་སོགས་པའི་མཚན་ཉིད་ཇི་ལྟར་བྱ་བ་དང་ཆོ་ག་ཇི་ལྟར་བྱ་བ་དང་ཚོགས་ཀྱི་འཁོར་ལོ་སྔར་འདུ་བ་ལ་སོགས་པའི་གནས་བསྟན་ཀྱང་མངོན་པར༌[^1318]རྟོགས་པ་མ་བསྟན་པས་ལེའུ་གཉིས་གསུངས་སོ། །
--- END BLOCKS ---
