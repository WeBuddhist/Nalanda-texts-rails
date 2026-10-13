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
[Block 246]
དེ་ལ་ཡང་ལུས་ཐབས་དང་ལྡན་པ་ལ་བརྟེན་པ་ཆགས་པ་འབྲིང་ནི་རྡོ་རྗེ་མི་ཕྱེད་ནི་ལྟེ་བའི་གནས་སྟོང་པའོ། །

[Block 247 [VERSE]]
སྲིད་པ་གསུམ་ནི་རྩ་གསུམ་མོ། །
གཅིག་ནི་ཨ་ཝ་དྡྷཱུ་ཏཱིར་བསྡུའོ། །

[Block 248]
དེར་སྐྱེས་པའི་ཡེ་ཤེས་ནི་གཟུང་འཛིན་དང་བྲལ་བས་ཤེས་རབ་ཀྱི་རིགས་པའོ། །

[Block 249]
དེས་ན་སྟོང་པ་ཉིད་ཀྱི་ཡེ་ཤེས་དང་ལྡན་པས་རྡོ་རྗེ་སེམས་དཔའ་ཞེས་བྱར་བརྗོད་ཅེས་པའོ། །

[Block 250]
ཡེ་ཤེས་ཆེན་པོ་རོས་གང་བ་ནི་བདེ་བ་ཆེན་པོ་ལས་ལུས་ཀུན་དུ་ཞུ་ཞིང་གང་བའོ། །

[Block 251]
དེས་ཕུལ་དུ་གྱུར་པའི་ཡེ་ཤེས་མྱོང་བས་སེམས་ཡེ་ཤེས་ཆེན་པོར་གྱུར་པ་ཁྱད་པར་གྱི་རོ་དང་ལྡན་པའི་ཕྱིར་སེམས་དཔའ་ཆེན་པོར་བརྗོད་པར་བྱ་ཞེས་པའོ། །

[Block 252]
རྟག་ཏུ་དམ་ཚིག་ལ་སྤྱོད་ཕྱིར་ནི་རྟག་ཏུ་སྟེ་སྟེང་འོག་རྒྱུན་མི་འཆད་པར་ས་མ་ཡ་སྟེ། །མཉམ་པ་བྱང་ཆུང་སེམས་ཀྱིས་ཁྱབ་པར་རོ། །

[Block 253]
ཡ་ཡོ་ག་སྟེ།

[Block 254 [VERSE]]
ལུས་དང་སྦྱོར་བས་མི་འབྲལ་བས་ཚུལ་ལོ། །
དེས་གཞན་དོན་ཇི་ལྟར་ཡང་འགྲུབ་པས།
དམ་ཚིག་སེམས་དཔར་བརྗོད་པར་བྱ། །

[Block 255]
ཞེས་པའོ། །

[Block 256 [HEADING]]
###### **དབྱེར་མེད་ཕྱག་རྒྱ་ཆེན་པོ།** ^1-1-3-1-2-3-0

[Block 257]
དེ་ལ་ཕྱག་རྒྱ་ཆེན་པོ་ནི་ཆགས་པ་ཆུང་བ་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ཏེ། །

[Block 258 [VERSE]]
རྡོ་རྗེ་མི་ཕྱེད་ནི་སྟོང་པ་ཉིད་དོ། །
སྲིད་པ་གསུམ་ནི་ཁམས་གསུམ་མོ། །

[Block 259]
གཅིག་པ་ནི་རང་རིག་འོད་གསལ་དང་སྟོང་པ་འོད་གསལ་ལོ། །

[Block 260]
ཡེ་ཤེས་ཆེན་པོ་རོས་གང་བ་ནི་ཐབས་སྣང་བ་མ༌[^109]བཀག་པར་བསྒོམ་པའོ། །

[Block 261]
རྟག་ཏུ་དམ་ཚིག་ལ་སྤྱོད་ནི་སྤྱོད་པ་རྒྱུན་མི་འཆད་པ་སྟེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་ཚད་མེད་པས་འཇུག་པའོ། །

[Block 262]
ཆགས་ཅན་གྱི་ལྟ་བུ་ནི་རྡོ་རྗེ་མི་ཕྱེད་པ་ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པ་སྟེ། སེམས་ཅན་ཀུན་གྱི་དབང་པོའོ། །

[Block 263]
སྲིད་གསུམ་ལུས་དག་བསྡུས་པ་སྤྱི་བོ་དང་། རྐང་པར་བྱ་བ་སྟེ།

[Block 264 [VERSE]]
སྤྱི་གཙུག་ནས་ནི་རྐང་པའི་མཐར། །
སྡུད་པ༌[^110]གཅིག་ལ་ཡང་དག་བརྟེན། །

[Block 265]
ཞེས་གསུངས་སོ། །

[Block 266]
ཡེ་ཤེས་ཆེན་པོ་རོས་གང་སྟེ་དེར་བདེ་བ་ཆེན་པོ་དབྱེར་མེད་བསྒོམ་པ་སྟེ་ཡེ་ཤེས་རང༌[^111]འབར་བའོ། །

[Block 267]
གང་བ་ནི་དབང་པོ་རང་སྣང་བའི་ཚུལ་ལོ། །

[Block 268]
རྟག་ཏུ་དམ་ཚིག་ལ་སྤྱོད་ནི་སྤྱོད་ལམ་དང་བསྲེས་པ་སྟེ། རྟག་ཏུའམ་རྒྱུན་མི་འཆད་པར་རང་གི་ནང་ནི་ཉམས་ཀྱི་གཟུགས་དང་སྒྲ་དབང་པོ་རང་སྣང་དུ་སྦྱོར་རོ།[^112] །དྲི་དང་རོ་གཉིས་རེག་བྱ་འགྲོ་འདུག་སྤྱོད་ལམ་དུ་བསྲེའོ། །

[Block 269]
དེ་ལ་ཡང་ལྟ་བའི་རྟགས་མི་འགྱུར་བ་བསྒོམ་པའི་རྟགས་དངོས་པོ་ཀུན་ལ་ཆགས་མེད་དྲོད། སྤྱོད་པའི་རྟགས་འཇིག་རྟེན་ཆོས་བརྒྱད་སྤངས་པའོ། །

[Block 270]
དེ་ཡང་བསྡུས་པའི་ཚུལ་གྱིས་མིང་བཏགས་ན།[^113] རྡོ་རྗེ་སེམས་དཔའ་ནི་གསང་བའི་དོན་ཏེ་ཤེས་རབ་ལྟ་བའོ། །

[Block 271]
སེམས་དཔའ་ཆེན་པོ་ནི་ཤིན་ཏུ་གསང་བའི་དོན་ཏེ་ཐབས་བདེ་བ་ཆེན་པོའི་ཡེ་ཤེས་བསྒོམ་པའོ། །

[Block 272]
དམ་ཚིག་སེམས་དཔའ་ནི་ཆེས་གསང་བའི་དོན་ཏེ་དབྱེར་མེད་པར་རྟག་ཏུ་སྤྱོད་པའོ། །

[Block 273]
ཡང་ན་གསང་བ་ཤིན་ཏུ་གསང་བ་ཆེས་གསང་བ་ནི་སྔར་བཞིན་དུ་ཡང་སྦྱར།

[Block 274 [HEADING]]
#### མིང་བསྡུས་པ། ^1-1-4-0

[Block 275 [HEADING]]
##### དང་པོར་སྙིང་པོར་བསྡུས་པ། ^1-1-4-1-0

[Block 276]
མིང་བསྡུས་པ༌[^114]ནི་ཇི་ལྟ་བུ་ཞེ་ན། བྱ་བ་ནི་དྲི་བ་སྟེ་ཚུལ་གཉིས་ཀྱིས་སྔར་གྱི་གསང་བ་གསུམ་དུ་བཤད་པ་དེ་སྙིང་པོར་ཇི་ལྟར་བསྡུས་པ་དགྱེས་པ་རྡོ་རྗེ་ཇི་ལྟར་འདུས་པས་དོན་ཡང་ཇི་ལྟར་བསྡུས་ཤེ་ན། མིང་བསྡུས་པས་ནི་ཇི་ལྟ་བུ། །ཞེས་བྱ་སྟེ། དེ་ལ་དང་པོར་སྙིང་པོར་བསྡུས་པ་ཡང་སྟོན་པ་དང་བསྟན་པའི་ཚུལ་གྱིས་བསྡུས་ཏེ། སྟོན་པ་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་ནི་སྐུ་རྡོ་རྗེ་ལ་སོགས་པ་དང་རིན་ཆེན་ཏེ་ཡོན་ཏན་རྡོ་རྗེ་དང་ཕྲིན་ལས་རྡོ་རྗེ་སྟེ་དེ་རྣམས་ཀུན་ལ་ཡང་སྐུ་རྡོ་རྗེ་ལ་སོགས་པ་དང་ལྡན་པ་ཡང་རྡོ་རྗེ་འཛིན་ཞེས་པས་བསྡུས་ཏེ་བྱེ་བྲག༌[^115]འཆང་ཞེས་པས་བསྡུས་སོ། །

[Block 277]
སྟོན་པ་དོན་བསྡུས་པ་ནི་རྣམ་སྣང་ལ་སོགས་པ་སྐུ༌[^116]རྡོ་རྗེ་ལ་སོགས་པ་ནི་ཡེ་ཤེས་ལྔ་ལ་འཆད་དེ་དེ་ཡང་བྱང་ཆུབ༌[^117]སེམས་ལས་གཞན་ན་མེད་པས་འདིར་འདུས་པའོ། །

[Block 278]
བསྟན་པ་མིང་བསྡུས་པ་གསང་བ་གསུམ་ཀྲྀ་ཡ་ཡོ་ག་ལ་སོགས་པ་གསུམ་ཐ་དད་དུ་བཏགས་པ་དེ་གསང་བ་འདུས་པ་ཞེས་བྱ་བའི་མིང་བསྡུས་པའོ། །

[Block 279]
དོན་བསྡུས་པ་ནི་བྱ་བ་དང་སྤྱོད་པ་ལས་རྣམ་གྲངས་དུ་མ་བཤད་པ་ཡང་བྱང་ཆུབ་སེམས་ལས་མི་འདའ་བས༌[^118]བསྡུས་པ་སྟེ་དེས་ན་དོན་དེ་ཁོ་ན་ཉིད་ལ་སྟོན་པ་དང་བསྟན་པ་དབྱེར་མེད་དོ། །

[Block 280 [HEADING]]
##### དགྱེས་པའི་རྡོ་རྗེ་མིང་བསྡུས་པ། ^1-1-4-2-0

[Block 281]
དགྱེས་པའི་རྡོ་རྗེ་མིང་བསྡུས་པས་ནི་དོན་གྱི་སྟེ་སྟོན་པ་དང་། བསྟན་པ་བསྡུས་པའོ། །

[Block 282]
སྟོན་པ་མིང་བསྡུས་པ་ནི་སྐུ་རྡོ་རྗེ་ལ་སོགས་པ་བཛྲིའི་མིང་གོང༌[^119]མ་ལྟར་གྱུར་པས་བསྡུས་པའོ། །

[Block 283]
དོན་བསྡུས་པ་ནི་ཡེ་ཤེས་རྣམས་སེམས་སུ་བསྡུས་ལ་དེ་ཡང་ལྷན་སྐྱེས་བདེ་ཆེན་དུ་འདུས་སོ། །

[Block 284]
འོ་ན་སྔ་མ་ལས་ཁྱད་པར་ཅི་ཡོད་ཅེ་ན། འདིར་ཁྲོ་བ་དང་ཆགས་པས་འདུལ་བའི་དོན་དུའམ། ཡང་ན་དེ་བཞིན་གཤེགས་པའི་སའི་སྐད་ཅིག་མ་གཉིས་ལ་སོགས་པ་ཡིན་ཏེ་གཞན་དོན་རྫོགས་པའོ། །

[Block 285]
སྔར་གྱི་ནི་དེ་ལྟར་མ་ཡིན་ནོ། །
--- END BLOCKS ---
