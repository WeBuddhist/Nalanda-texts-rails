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
[Block 3361 [VERSE]]
ཙའི་སྡེ་ཚན་ནི་གཉིས་པ་སྟེ་ཡིག་འབྲུ་ལྔ་ལྔའོ། །
ཊ་ཋ་ནི་གསུམ་པ་སྟེ་ཀུན་ལ་ཤེས་སོ། །

[Block 3362]
ཏ་ཐ་ནི་བཞི་པ་དང་ལྔ་པ་གཉིས་ཆར་ཡང་སྡེ་ཚན་ནི་ལྔ་ལྔར་ཤེས། པ་ཕ་ནི་ལྔ་པར་ཤེས། ཡ་ར་ནི་མཐར་གནས་ཞེས་བྱ་བའི་འབྱུང་བ་བཞི་ས་བོན་ཞེས་བྱ། དྲུག་པའམ༌[^1348]བདུན་པའི་སྡེ༌[^1349]ཞེས་བྱ། [^1350]བརྒྱད་པའི་སྡེ་པ༌[^1351]ཨུཥྨ་ཞེས་བྱ། སྡེ་ཚན་འདི་རྣམས་མེད་དེ་ཡི་གེ་འདི་རྣམས་ལས་སྔགས་བཏུ་བར་བྱའོ། །

[Block 3363]
ཡི་གེ་འོག་མ་གསུམ་ནི་ཡི་གེའི་བདག་པོ་ཞེས་བྱ། ཡི་གེའི་དབང་ཕྱུག་ཅེས་བྱ། ཡི་གེ་ཐུ་བོ་ཞེས་བྱ། རིག་བྱེད་དང་པོ་ཞེས་བྱ། གཏི་མུག་རིགས་ཞེས་བྱ། རྣམ་པར་སྣང་མཛད་ཅེས་བྱ་སྟེ། གཉིས་པོ་ལ་ཡང་སྐབས་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 3364]
འདིས་ནི་རྒྱུད་ཐམས་ཅད་ཀྱི་སྔགས་བཏུ་བ་ལ་འཇུག་གོ། །

[Block 3365]
འབྲུ་སོ་སོར་སྦྱར་བ་ནི་གོ་སླའོ། །

[Block 3366]
ལེའུ་དགུ༌[^1352]པའོ།། །།

[Block 3367 [HEADING]]
### ལེའུ་བཅུ་པ། ^2-9-0

[Block 3368 [HEADING]]
#### བཟླས་པའི་རྟེན་བགྲང་ཕྲེང་དང་བཟའ་བ། ^2-9-1-0

[Block 3369 [HEADING]]
##### བགྲང་ཕྲེང། ^2-9-1-1-0

[Block 3370]
དེ་ནས་ཆོས་ཀུན་སྡོམ་གཅིག་པའི། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྤྱིར་བསྟན་པ་བཟླས་པའི་རྟེན་བགྲང་ཕྲེང་དང་བཟའ་བ་གཉིས་སྟོན་ཏེ། ལས་སོ་སོའི༌[^1353]ཕྲེང་བ་ནི།

[Block 3371 [VERSE]]
ཤེལ་གྱིས་རེངས་པའི་བཟླས་པ་ཉིད། །
ཅེས་བྱ་བ་ལ་སོགས་པ་གོ་སླའོ། །

[Block 3372 [HEADING]]
##### བཟའ་བ། ^2-9-1-2-0

[Block 3373]
རེངས་པའི་འོ་མ་བཏུང་བ་ཉིད་ནི་ཆང་ངམ་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 3374]
དབང་ལ་རང་གི་འདུན་པས་སྤྱད་ནི་གང་འདོད་པའོ། །

[Block 3375]
བསད་པ་ལ་ནི་སི་ཧླ་ལ༌[^1354]ཉིད་ནི་རང་འབྱུང་གི་ཁྲག་གོ། །

[Block 3376 [VERSE]]
དགུག་པ་ལ་ནི་བཞི་མཉམ་ཉིད་ནི་དྲི་ཆེན་ནོ། །
སྡང་ལ༌[^1355]སཱ་ལུ་སྐྱེས་པར་བརྗོད་ནི་ཤ་ཆེན་ནོ། །
བསྐྲད་པ་ཉིད་ལ་གླ་བ་བརྗོད་ནི་དྲི་ཆུའོ། །

[Block 3377]
ཡང་ན་མཐའི་ཤྭ༌[^1356]དང་ཞེས་པ་ལ་སོགས་པ་ནི་རབ་གནས་ཀྱི་ལེའུར་བཤད་དོ། །

[Block 3378]
དེ་དག་གིས་ཀྱང་རེངས་པ་ལ་སོགས་པའི་ལས་གོ་རིམས་བཞིན་ནོ། །

[Block 3379]
དེ་སྐད་དུ་ཡང་།

[Block 3380 [VERSE]]
གསང་སྔགས་སྒྲུབ་པ་ལྔ་བཅུ་སྟེ། །
དབང་གི་ལས་ལ་དེ་ཡི་ཕྱེད། །
ཞི་ལ་བརྒྱ་ཕྲག་གཅིག་ཡིན་ཏེ། །
དེ་བཞིན་རྒྱས་ལ་བརྒྱ་ལྷག་པའོ། །

[Block 3381 [VERSE]]
མངོན་སྤྱོད་ལ་ནི་དྲུག་ཅུ་སྟེ། །
ལས་ཀྱི་ཁྱད་པར་གྱིས་ནི་སྦྱར། །
ལས་ཀྱི་བྱེ་བྲག་ཇི་བཞིན་དུ། །
བགྲང་བའི་ཕྲེང་བ་ལ་སོགས་བྱ། །

[Block 3382 [VERSE]]
ཕྱོགས་དང་ཕྱོགས་མཚམས་བརྒྱད་དང་ནི། །
དགུག་པ་དབུས་ཀྱི་སངས་རྒྱས་ཏེ། །
སྐུད་པ་དགུ་ལ་བྱིན་གྱིས་བརླབ། །
རི་ལུ་རྣམ་ནི་དགྲ་བཅོམ་སྟེ། །

[Block 3383 [VERSE]]
སྟེང་དུ་མཆོད་རྟེན་བརྟག་པར་བྱ། །
མཆོད་རྟེན་ཆོས་ཀྱི་དབང་པོ་བས། །
སྟེང་དུ་ཆོས་ཀྱི་དབྱིངས་ཡིན་ནོ། །

[Block 3384]
ཞེས་གསུངས་པས་ནི་བགྲང་ཕྲེང་གི་ལས་ཀྱི་བྱེ་བྲག་བསྟན་ནོ། །

[Block 3385]
ལེའུ་བཅུ་པ།།[^1357] །།

[Block 3386 [HEADING]]
### ལེའུ་བཅུ་གཅིག་པ། ^2-10-0

[Block 3387]
ཀྱེའི་རྡོ་རྗེས༌[^1358]དམ་འཁྱུད་ཅིང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཁྲོ་ཆགས་རྣམ་པ་གཉིས་དང་ལྡན་པས་ཀུན་རྫོབ་ཀྱི་རྣམ་པའི་སྐྱེས་པ་དང་བུད་མེད་ཀྱི་རིགས་མཚོན་པའི་རྟགས་གསུངས་པ། བུད་མེད་དམ་ནི་སྐྱེས་པ་ཡི།[^1359] །

[Block 3388 [VERSE]]
གང་གི༌[^1360]སྲིན་ལག་རྩ་བ་ན། །
རྡོ་རྗེ་རྩེ་དགུ་པར་གྱུར་པ། །

[Block 3389]
ཞེས་བྱ་བ་ལ་སོགས་པ་རིགས་ཀྱི་མཚན་མ་དང་།

[Block 3390 [VERSE]]
རྣལ་འབྱོར་པ་གང་ནག་པོ་ཡིན། །
དེ་ཡི་ལྷ་ནི་མི་བསྐྱོད་པ། །

[Block 3391]
ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཁ་དོག་གི་མཚན་མ་དང་། གཞན་ཡང་སྤྱོད་ལམ་དང་། མཆོད་པའི་རྟེན་དང་ཆོས་འབྱུང་ལ་སོགས་པས་དེ་རྣམས་མཚོན་ཏེ། རྒྱུད་འདིར་ནི་གཉིས་མཚོན་གཞན་དུ་ནི་གཞན་དག་ཀྱང་བཤད་དོ། །

[Block 3392]
དེ་སྐད་དུ་ཡང་།

[Block 3393 [VERSE]]
གང་ཞིག་སྨིན་མ་གཡོ་བྱེད་ཅིང་། །
ཀུན་དུ་ཆགས་པས་བལྟ་བ་དང་། །
སྔོན་གྱི་གཟུགས་ནི་བསྡུས་ནས་སུ། །
ཤི་ནས་འཇོག་པར་བྱེད་པ་དག །

[Block 3394 [VERSE]]
གཟུགས་ཅན་མར་ནི་ཤེས་བྱ་སྟེ། །
དཔའ་བོ་གཉིས་མེད་པར་བསྟེན་བྱ། །

[Block 3395]
ཞེས་གསུངས་པ་དང་། ཡང་།

[Block 3396 [VERSE]]
དམར་ཞིང་སེར་བའི་བུད་མེད་གང་། །
པདྨའི་འདབ་ལྟར་དཀྱུས་རིང་མིག །
རྟག་ཏུ་གོས་དཀར་ལ་དགའ་ཞིང་། །
ཙནྡན་སར་པའི་དྲི་དང་ལྡན། །

[Block 3397 [VERSE]]
བདེ་གཤེགས་འདུས་པ་ཉིད་ལ་དགའ། །
ཞེན་པར་ལྟ་བའི་རྗེས་སུ་འགྲོ། །
ཁྱིམ་དུ་པདྨ་བྲི་བར་བྱེད། །
པདྨ་གར་དབང་རིགས་འབྱུང་ཡིན། །

[Block 3398]
ཞེས་གསུངས་སོ། །

[Block 3399]
འདིས་ནི་སེམས་ཅན་གྱི་དུས་ན་དེ་དང་དེའི་རིགས་སུ་ཤེས་པས་རང་ང་རྒྱལ་མི་བཅག་པ་དང་། གཞན་ལ་མཐོ་མི་བཙམ་པ་དང་བརྙས་པར་མི་བྱ་བའོ། །

[Block 3400]
སངས་རྒྱས་པའི་དུས་སུ་རིགས་དེ་དང་དེ་རུ་སངས་རྒྱས་པར་འགྱུར་རོ། །
--- END BLOCKS ---
