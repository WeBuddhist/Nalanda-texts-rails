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

[Block 3261]
ལྷ་མོ་ལ་ནི་དམ་འཁྱུད་ཅིང་། །ཞེས་བྱ་བ་ནས། མཉམ་སྦྱར་བདེ་བ་མྱོང་མཛད་ནས། །ཞེས་པའི་བར་གྱིས་གཙོ་བོ་ཆགས་པ་དང་ཁྲོ་བོའི་ཚུལ་གྱིས་གསུངས་པའོ། །

[Block 3262 [VERSE]]
ཕྱག་རྒྱ་ལྔ་ནི་རབ་ཕྱེ་ཞེས་པ་ནས། །
སངས་རྒྱས་ལྔ་ཡི་ཕྱག་རྒྱས་གདབ། །

[Block 3263]
ཅེས་པའི་བར་ནི་དགོངས་པ་དང་། ཕྱག་རྒྱ་ལྔའི་རྣམ་དག་གོ་སླ་བ་དང་སྔར་བཤད་དོ། །

[Block 3264]
དེ་ནས་རབ་ཏུ་བཞད་མཛད་ཅིང་། །བྱ་བ་ནས་བྱེད་པ་བདེ་བ་ཆེན་པོ་གསུངས་ཀྱི་བར་གྱིས་བྲིས་སྐུའི་བྱ་བ་དང་ཆོ་ག་ཞུས་པའོ། །

[Block 3265]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་ཞེས་པ་ནས། འདིར་ནི་འདྲི་མཁན་དམ་ཚིག་ཅན། །ཞེས་པ་ལ་སོགས་པས་སྒྲུབ་པ་པོ་དང་རི་མོ་མཁན་དང་རས་ཡུག་འཁལ་བ་དང་ཐག་པའི༌[^1319]བར་ཀྱང་དམ་ཚིག་ཅན་གྱིས་བྱའོ། །

[Block 3266]
དབེན་པའི་གནས་སུ་ཚོན་ཀོང་དང་པིར་ལ་སོགས་ཏེ། མཆོད་པ་དང་ཚོགས་ཀྱི་འཁོར་ལོ་ཅི་འབྱོར་པ་བྱའོ། །

[Block 3267]
དེ་ནས་དེ་ལ་ལྷ་མོས་ཞུས། །ཞེས་པ་ལ་སོགས་པ་ལེའུ་བདུན་པ་སྦྱར་ཏེ། གླེགས་བམ་ཇི་ལྟ་ཇི་ལྟར་བྱ་བ་སྔ་མ་དང་འདྲ་སྟེ་གོ་སླའོ། །

[Block 3268]
བྷ་གར་ལིང་ག་རབ་གནས་ཞེས་བྱ་བ་ནས་སྒྲུབ་པ་ཅན་གྱི་དངོས་གྲུབ་འགྱུར་གྱི་བར་གྱིས་ཚོགས་ཀྱི་དགོས་པ་བསྟན་ཏོ། །

[Block 3269]
ལེའུ་གཉིས་གཅིག་ཏུ་བསྐོར་ཏེ་མངོན་རྟོགས་སུ་ཤེས་པར་བྱེད་པའི་ཚེ། ཚོགས་ཀྱི་འཁོར་ལོར་འདོད་པ་དང་ལ་ལ་དག་སྤྲོས་བཅས་ཀྱི་སྤྱོད་པར་ཡང་བཞེད་དོ། །

[Block 3270 [HEADING]]
#### ཚོགས་ཀྱི་འཁོར་ལོ། ^2-6-1-0

[Block 3271]
དེ་ལ་ཚོགས་ཀྱི་འཁོར་ལོ་ནི་བཞི་སྟེ། ཕན་ཡོན་དང་། གནས་དང་། ཟླ་བ་དུས་དང་། འཇུག་པའོ། །

[Block 3272 [HEADING]]
##### ཕན་ཡོན། ^2-6-1-1-0

[Block 3273]
དེ་ལ་ཕན་ཡོན་ནི་སྟོན་མོ་བཟའ་བའམ་ཚོགས་ལ་ཞུགས་པའི་དུས་སུ་སྒྲུབ་པ་དང་དངོས་གྲུབ་ཏུ་གྱུར༌[^1320]ཏེ་གདུལ་བྱ་བྲོད་པ་སྐྱེའོ། །

[Block 3274 [HEADING]]
##### གནས། ^2-6-1-2-0

[Block 3275]
གནས་ནི་དུར་ཁྲོད་ལ་སོགས་པའོ། །

[Block 3276 [HEADING]]
##### ཟླ་བ་དུས། ^2-6-1-3-0

[Block 3277]
དུས་ནི་ཟླ་བ་བྱུང༌[^1321]ངོ་ཅོག༌[^1322]གི་བཅུ་བཞི་པའམ་མཚན་ཕྱེད་དམ་བསམ་པའི་ཁྱད་པར་ལྡན་པའོ། །

[Block 3278 [HEADING]]
##### འཇུག་པ། ^2-6-1-4-0

[Block 3279]
འཇུག་པ་ལ་གཉིས་ཏེ། ཐུན་མོང་དང་ཁྱད་པར་རོ། །

[Block 3280 [HEADING]]
###### ཐུན་མོང། ^2-6-1-4-1-0

[Block 3281 [HEADING]]
###### **གདན་བྲི་བ།** ^2-6-1-4-1-1-0

[Block 3282]
ཐུན་མོང་ལ་གསུམ་སྟེ། གདན་བྲི་བ་ནི་གདན་ལ་རབ་འབྲིང་གསུམ་སྟེ། སྟག་གི་པགས་པ་དང་། ཞིང་གི་པགས་པ་དང་། དུར་ཁྲོད་ཀྱི་རས་ཏེ་རོ་རུ་མོས་པས་བྱའོ། །

[Block 3283 [HEADING]]
###### **རྒྱན་དགྲམ་པ།** ^2-6-1-4-1-2-0

[Block 3284]
རྒྱན་དགྲམ་པ་ལ་ཡང་གསུམ་སྟེ་ཐལ་ཆེན་གྱིས་བྱུག་པ་དང་། ཞིང་དང་སྟག་གི་པགས་པ་དང་། །རུས་པའི་རྒྱན་ནོ། །

[Block 3285 [HEADING]]
###### **རྣལ་འབྱོར་པ་ལྷའི་ཚུལ་དུ་དགོད་པ།** ^2-6-1-4-1-3-0

[Block 3286]
རྣལ་འབྱོར་པ་ལྷའི་ཚུལ་དུ་དགོད་པའོ། །

[Block 3287 [HEADING]]
###### ཐུན་མོང་མ་ཡིན་པ། ^2-6-1-4-2-0

[Block 3288]
ཐུན་མོང་མ་ཡིན་པ་ལ་དཔའ་བོའི་སྟོན་མོ་དང་ཚོགས་ཀྱི་འཁོར་ལོའོ། །

[Block 3289 [HEADING]]
###### **དཔའ་བོའི་སྟོན་མོ།** ^2-6-1-4-2-1-0

[Block 3290]
དཔའ་བོའི་སྟོན་མོ་ལ་བཞི་སྟེ། སྡེར་དགོད་ཅིང་བཟའ་བའི་སྟོན་མོ་གཙོ་བོར་བསྟན་པའོ། །

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
--- END BLOCKS ---
