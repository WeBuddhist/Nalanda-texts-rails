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
[Block 1]
༄༅། །ཕྱག་འཚལ་ཉེར་གཅིག་གི་བསྟོད་པའི་རྣམ་པར་བཤད་པ་བཞུགས་སོ། །

[Block 2 [HEADING]]
## མཆོད་བརྗོད། ^I-0

[Block 3]
ན་མོ་ལོ་ཀེ་ཤྭ་རཱ་ཡ།

[Block 4 [VERSE]]
སྒྲོལ་མ་འཁོར་བ་ཀུན་སྒྲོལ་བ། །
དེ་ལ་གུས་པས་ཕྱག་འཚལ་ནས། །
བསྟོད་པའི་རྒྱུད་དོན་ཅུང་ཟད་བཤད། །
བགེགས་རྣམས་མ་ལུས་ཞི་བར་མཛོད། །

[Block 5 [HEADING]]
## རྒྱུད་ཀྱི་རིགས་བསྟན་པ། ^II-0

[Block 6]
དེ་ལ་རྒྱུད་འདི་ནི་རྣལ་འབྱོར་བླ་ན་མེད་པ་ཡིན་ལ། དེ་ལས་ཀྱང་རྣལ་འབྱོར་མའི་རྒྱུད་དོ། །

[Block 7]
དེ་ལ་རིགས་དྲུག་ལས་རྡོ་རྗེ་རྟ་མཆོག་སྟེ་རྟའི་རྒྱལ་པོའི་རིགས་སོ། །

[Block 8]
དེ་ལས་ཀྱང་རིགས་ཀྱི་འཁོར་ལོའི་དབང་ཕྱུག་མ་བཅོམ་ལྡན་འདས་མ་སྒྲོལ་མའི་རྒྱུད་དེ། བསྟོད་པ་འདི་ཡང་རྒྱུད་ཆ་ཚང་པ་ཁོ་ནར་བཞེད་དོ། །

[Block 9 [HEADING]]
## བསྟོད་པ་དངོས། ^1-0

[Block 10 [HEADING]]
### ཕྱག་འཚལ་དང་པོ། ^1-1-0

[Block 11]
དེ་ལ་ཚིགས་བཅད་དང་པོ་ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ་ཞེས་པ་ལ་སོགས་པ་ལ། ཕྱག་འཚལ་ལོ་ཞེས་པ་དང་པོར་འབྱུང་བ་ནི་བརྗོད་པ་གླེང་སློང་པའི་གཞིར་གཞག་པ་སྟེ་འོག་མ་རྣམས་ལའང་ཤེས་པར་བྱའོ། །

[Block 12]
གང་ལ་ཕྱག་འཚལ་ན་བཅོམ་ལྡན་འདས་མ་སྒྲོལ་མ་ལའོ། །

[Block 13]
དེ་ཉིད་ཀྱི་ཁྱད་པར་ཇི་ལྟ་བུ་ཞེ་ན། ཐུགས་དམིགས་པ་མེད་པའི་སྙིང་རྗེ་ཆེན་པོས་མྱུར་དུ་སེམས་ཅན་གྱི་དོན་མཛད་པས་མ་དང་འཇིགས་པ་ཐམས་ཅད་ལས་སྐྱོབ་པར་དཔའ་བ་མོ་ནི་ནུས་མཐུ་ཐོགས་པ་མེད་པའི་ཕྲིན་ལས་དང་། སྐད་ཅིག་གཅིག་ལ་ཡེ་ཤེས་ཀྱི་སྤྱན་གློག་དང་འདྲ་བ་མྱུར་དུ་སྐྱེད་པས། ཤེས་བྱ་མཐའ་དག་གཟིགས་པའི་མཁྱེན་པ་པོའོ། །

[Block 14]
དེའི་ཕྱིར་སྒྲོལ་མ་སྟེ་སེམས་ཅན་ཐམས་ཅད་འཁོར་བ་ལས་སྒྲོལ་བའི་ཕྲིན་ལས་ཅན་ནོ། །

[Block 15]
དེ་ལྟར་ན་མཁྱེན་པ་དང་བརྩེ་བ་དང་ནུས་པ་དང་ཕྲིན་ལས་ཏེ། དེ་ཙམ་བསྟན་པས་མཐའ་ཡས་པའི་ཡོན་ཏན་ཐམས་ཅད་མཚོན་ནུས་པ་ཡིན་ལ། དེ་ལྟ་བས་ན་ཚིག་གཉིས་པོ་དེ་ནི་ཐམས་ཅད་ཀྱི་མདོར་བསྟན་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 16]
དེ་ལྟ་བུའི་ཡོན་ཏན་མངའ་བའི་ལྷ་མོ་འདི་ནི། འཇིག་རྟེན་གསུམ་གྱི་མགོན་པོ་སྤྱན་རས་གཟིགས་ཀྱི་ཞལ་རས་ཀྱི་ཆུ་སྐྱེས་ཏེ་པདྨ་གེ་སར་བྱེ་བ་ལས་སྤུལ་ཞིང་བྱུང་བའོ། །

[Block 17]
འདི་ལ་ལོ་ཙྭ་བ་ནམ་མཁའ་བཟང་པོས། འཇིག་རྟེན་གསུམ་མགོན་ཞལ་གི་ཆུ་སྐྱེས། །བྱེ་བའི་གེ་སར་ལས་ནི་བྱུང་མ། །ཞེས་པ་འགྱུར་བཅོས་པ་གོ་བདེ་བའོ། །སྒྲ་ཇི་བཞིན་པ་མ་ཡིན་པ་ནི། འཇིག་རྟེན་གསུམ་མགོན་ཆོས་ཀྱི་སྐུ། །དེ་ལས་བྱུང་བ་ནི་གཟུགས་ཀྱི་སྐུའོ། །

[Block 18 [HEADING]]
### ཕྱག་འཚལ་གཉིས་པ། ^1-2-0

[Block 19]
ཚིགས་བཅད་གཉིས་པ་ཕྱག་འཚལ་སྟོན་ཀའི་སོགས་ལ། སྟོན་ཀའི་ཟླ་བ་ཀུན་ཏུ་གང་བ་སྟེ། ཉ་གང་བ་བརྒྱ་ཕྱག་ནི་བརྩེགས་པ་མེ་སྤུངས་པའི་འོད་ཟེར་དང་མཚུངས་པའི་ཞལ་རས་རབ་ཏུ་དྭངས་བ་མཛེས་པ་མ་དང་། སྐར་མ་སྟོང་ཕྲག་མང་པོ་ཚོགས་པ་རྣམས་ཀྱི་སྟེ་ལྟ་བུའམ་དུ་མར་གྱེས་པས་རབ་ཏུ་ཕྱེ་ཞིང་འཕྲོ་བའི་འོད་ཟེར་རབ་ཏུ་འབར་བའི་སྐུ་ཅན་མ་སྟེ། སྐུ་མདོག་དཀར་ཞིང་དྭངས་ལ་ཡིད་འཕྲོག་ཅིང་འོད་ཟེར་དཀར་པོ་འཕྲོ་བའོ། །

[Block 20]
སྦས་དོན་ནི་སྟོན་ཟླ་ལྟ་བུའི་བྱང་ཆུབ་ཀྱི་སེམས་ནོར་བུ་ནས་སྤྱི་བོའི་བར་འཕོ་མེད་དུ་བརྩེགས་པ་དང་། རྩ་ཕྲན་ཐམས་ཅད་ཀུན་ནས་གང་བ་ནི་སྐར་ཚོགས་ལྟ་བུའོ། །

[Block 21 [HEADING]]
### ཕྱག་འཚལ་གསུམ་པ། ^1-3-0

[Block 22]
ཚིགས་བཅད་གསུམ་པ་ཕྱག་འཚལ་གསེར་སྔོ་སོགས་ལ། གསེར་གྱི་ཡུ་བ་ཅན་མེ་ཏོག་སྔོ་བ་ཆུ་ལས་སྐྱེས་པའི་པདྨས་ཕྱག་རྣམ་པར་བརྒྱན་པ་སྟེ་ཕྱག་ན་བསྣམས་པའི་ལྷ་མོ་ཁྱོད་ནི་སྦྱིན་པ་དང་བརྩོན་འགུས་དང་། དཀའ་ཐུབ་སྟེ་ཚུལ་ཁྲིམས་དང་། ཞི་བ་སྟེ་ཤེས་རབ་དང་། བཟོད་པ་དང་བསམ་གཏན་ཏེ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་མངའ་བརྙེས་པས། ཕར་ཕྱིན་ནི་ཁྱོད་ཀྱི་སྤྱོད་ཡུལ་ཉིད་ཡིན་ལ། ལྷ་མོ་ཁྱོད་ནི་དེ་ལ་སྤྱོད་པ་མོའོ། །

[Block 23]
སྦས་དོན་ནི་ཆུ་སྐྱེས་གནས་པའི་པདྨ་དང་། ཕྱག་གི་རྒྱས་རྡོ་རྗེ་སྟེ་མཉམ་པར་སྦྱར་བ་ལས་འཕོ་བ་མེད་པའི་ཚུལ་ཁྲིམས་དཀའ་ཐུབ་དང་། བདེ་པའི་བསམ་གཏན་དང་། སྟོང་ཉིད་རྟོགས་པས་རྣམ་རྟོག་ཞི་བའི་ཤེས་རབ་དང་། དེ་ལས་མི་མངའ་པའི་བརྩོན་འགྲུས་དང་། བདེ་སྡུག་ཐམས་ཅད་དེའི་ངང་དུ་སྙོམས་པའི་བཟོད་པ་དང་། བདག་འཛིན་བཏང་བའི་སྦྱིན་པ་སྟེ། སྔགས་ཀྱི་སྤྱོད་པ་བསྟན་པའོ། །

[Block 24 [HEADING]]
### ཕྱག་འཚལ་བཞི་པ། ^1-4-0

[Block 25]
ཚིགས་བཅད་བཞི་པ་ཕྱག་འཚལ་དེ་བཞིན་སོགས་ལ།

[Block 26]
དེ་བཞིན་གཤེགས་པ་རྣམ་པར་སྣང་མཛད་ཀྱི་གཙུག་གཏོར་ལས།

[Block 27]
ཕན་ཡོན་མཐའ་ཡས་པ་དང་ལྡན་ཞིང་མི་མཐུན་པའི་ཕྱོགས་ཐམས་ཅད་ལས་རྣམ་པར་རྒྱལ་བར་བྱེད་པའི་རིག་སྔགས་ཀྱི་ཡེ་ཤེས་སྤྲུལ་པ་དེ། དགེ་མ་ཁྱོད་ཀྱིས་བདག་གིར་མཛད་ནས་ལོངས་སྤྱོད་དེ། སེམས་ཅན་དཔག་ཏུ་མེད་པའི་རིག་སྔགས་ངེས་མཛད་ལ། ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་མ་ལུས་པར་ཐོབ་པའི། རྒྱལ་བའི་སྲས་པོ་ས་བཅུའི་དབང་ཕྱུག་རྣམས་ཀྱིས་ཀྱང་ཉིད་ལ་གུས་པས་བརྟེན་ཅིང་མཆོད་པའོ། །

[Block 28]
ཟབ་དོན་ལ་ལུགས་འབྱུང་ལུགས་བཟློག་གི་དགའ་བའི་ས་ནི།

[Block 29 [VERSE]]
དཔལ་ལྡན་དེ་བཞིན་ཉིད་གཤེགས་ཤིང་། །
དེ་བཞིན་སླར་ཡང་གཤེགས་པ་ཉིད། །
ཅེས་པ་ལྟར་དེ་བཞིན་གཤེགས་པའོ། །

[Block 30]
ཁམས་དང་རླུང་གི་ཚོགས་པ་གཙུག་གཏོར་དུ་ཐིམ་པས་སྤང་བྱ་མཐའ་ཡས་པ་ལས་རྣམ་པར་རྒྱལ་ཞིང་། ཕར་ཕྱིན་བཅུ་སྟེ་རླུང་བཅུ་གནས་གྱུར་པས། རྒྱལ་སྲས་བྱང་ཆུབ་སེམས་དཔའ་སྟེ་མིག་སོགས་སྐྱེ་མཆེད་རྣམས་ཀྱང་ཡེ་ཤེས་སུ་གནས་གྱུར་པའོ། །

[Block 31]
འདི་དང་གོང་གི་སྟོན་ཟླ་སོགས་སྦྱང་བས་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་གོ། །

[Block 32 [HEADING]]
### ཕྱག་འཚལ་ལྔ་པ། ^1-5-0

[Block 33]
ཚིགས་བཅད་ལྔ་པ་ཕྱག་འཚལ་ཏུ་ཏྟཱ་ར་སོགས་ལ་ཏུ་ཏྟཱ་རེ་དང་ཧཱུྃ་གི་སྔགས་ཀྱི་སྒྲས་འཇིག་རྟེན་འདིའི་འདོད་ཁམས་ཀྱི་གནས་ཐམས་ཅད་དང་། ནམ་མཁའ་སྟེ་གཟུགས་ཁམས་གཟུགས་མེད་ཀྱི་གནས་དང་། ཕྱོགས་ཞེས་པས་ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་གཞན་ཐམས་ཅད་ཀྱང་། ཁྱབ་ཅིང་གང་བར་མཛད་ལ་འཇིག་རྟེན་བདུན་པོ་ཞབས་ཀྱི་འོག་ཏུ་མནན་པ་ལྟར་དབང་དུ་མཛད་ཅིང་། ཁྱོད་ཀྱིས་བྱིན་གྱིས་བརླབས་པའི་རིག་སྔགས་ཀྱི་མཐུས། དབང་ཕྱུག་ཆེན་པོ་ལ་སོགས་པའི་ལྷ་ཆེན་པོ་རྣམས་ཀྱང་བྲན་དུ་འགུགས་པའི་ནུས་མཐུ་ཡོད་ན། ཕྲ་མོ་གཞན་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། དེ་ལ་འཇིག་རྟེན་བདུན་ཞེས་པ་སྣོད་བདུན་དང་། བཅུད་ཀྱི་བདུན་དང་། སྣོད་བཅུད་བསྡོམས་པའི་བདུན་ལ་སོགས་པའི་འཆད་ཚུལ་མི་གཅིག་པ་མང་ཡང་། འདིར་ནི་མཐུ་དང་ལྡན་པའི་འཇིག་རྟེན་བདུན་ཏེ། ཀླུ་དང་ཡི་དྭགས་དང་ལྷ་མ་ཡིན་དང་། མི་དང་རིག་པ་འཛིན་པ་དང་མིའམ་ཅི་དང་ལྷའི་འཇིག་རྟེན་ནོ། །

[Block 34]
སྦས་དོན་ནི་ཏུཏྟཱ་ར་ནི་གདུང་པ་སྟེ། གཏུམ་མོའི་མེས་གདུང་བའོ། །

[Block 35]
ཧཱུྃ་གི་ཡི་གེ་ནི་མི་ཤིགས་པའི་སྒྲ་སྟེ་གཏུམ་མོ་ལས་བྱུང་བའོ། །

[Block 36]
འདོད་པ་ནི་གསང་བའི་འཁོར་ལོ་དང་། ཕྱོགས་ནི་དབུ་མའི་ནང་སྟེ་སྒྲ་དེས་གང་བ་དང་། ནམ་མཁའ་གང་མ་ནི་བརྗོད་བྲལ་ལོ། །

[Block 37]
འཇིག་རྟེན་བདུན་ནི་རྩ་འཁོར་ལོ་ལྔ་དང་། མེ་རླུང་གི་འཁོར་ལོ་གཉིས་ཏེ་བདུན་གཏུམ་མོ་འབར་བ་ཞུ་པའི་ཀུན་དེས་གང་བ་དང་། ཀུན་ད་དེ་ཉིད་མ་ལུས་པར་སླར་ཡང་གསང་བ་ནས་སྤྱི་བོའི་བར་དུ་འགུགས་པའོ། །

[Block 38 [HEADING]]
### ཕྱག་འཚལ་དྲུག་པ། ^1-6-0

[Block 39]
ཚིག་བཅད་དྲུག་པ་ཕྱག་འཚལ་བརྒྱ་བྱིན་སོགས་ལ།

[Block 40 [VERSE]]
བརྒྱ་བྱིན་ནི་ལྷའི་འགྲོ་བ་རྣམས་ཀྱི་རྒྱལ་པོའོ། །
མེ་ལྷ་ནི་དྲང་སྲོང་གི་གཙོ་བོའོ། །
ཚངས་པ་འཇིག་རྟེན་གྱི་བྱེད་པོར་འདོད་པའོ། །
--- END BLOCKS ---
