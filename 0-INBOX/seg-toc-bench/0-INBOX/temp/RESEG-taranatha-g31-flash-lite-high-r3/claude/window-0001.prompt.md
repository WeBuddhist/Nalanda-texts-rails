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
[Block 36 [VERSE]]
དཔལ་ལྡན་དེ་བཞིན་ཉིད་གཤེགས་ཤིང་། །
དེ་བཞིན་སླར་ཡང་གཤེགས་པ་ཉིད། །
ཅེས་པ་ལྟར་དེ་བཞིན་གཤེགས་པའོ། །

[Block 37]
ཁམས་དང་རླུང་གི་ཚོགས་པ་གཙུག་གཏོར་དུ་ཐིམ་པས་སྤང་བྱ་མཐའ་ཡས་པ་ལས་རྣམ་པར་རྒྱལ་ཞིང་། ཕར་ཕྱིན་བཅུ་སྟེ་རླུང་བཅུ་གནས་གྱུར་པས། རྒྱལ་སྲས་བྱང་ཆུབ་སེམས་དཔའ་སྟེ་མིག་སོགས་སྐྱེ་མཆེད་རྣམས་ཀྱང་ཡེ་ཤེས་སུ་གནས་གྱུར་པའོ། །

[Block 38]
འདི་དང་གོང་གི་སྟོན་ཟླ་སོགས་སྦྱང་བས་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་གོ། །

[Block 39 [HEADING]]
### ཕྱག་འཚལ་ལྔ་པ། ^1-5-0

[Block 40 [HEADING]]
#### ཚིག་འགྲེལ། ^1-5-1-0

[Block 41]
ཚིགས་བཅད་ལྔ་པ་ཕྱག་འཚལ་ཏུ་ཏྟཱ་ར་སོགས་ལ་ཏུ་ཏྟཱ་རེ་དང་ཧཱུྃ་གི་སྔགས་ཀྱི་སྒྲས་འཇིག་རྟེན་འདིའི་འདོད་ཁམས་ཀྱི་གནས་ཐམས་ཅད་དང་། ནམ་མཁའ་སྟེ་གཟུགས་ཁམས་གཟུགས་མེད་ཀྱི་གནས་དང་། ཕྱོགས་ཞེས་པས་ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་གཞན་ཐམས་ཅད་ཀྱང་། ཁྱབ་ཅིང་གང་བར་མཛད་ལ་འཇིག་རྟེན་བདུན་པོ་ཞབས་ཀྱི་འོག་ཏུ་མནན་པ་ལྟར་དབང་དུ་མཛད་ཅིང་། ཁྱོད་ཀྱིས་བྱིན་གྱིས་བརླབས་པའི་རིག་སྔགས་ཀྱི་མཐུས། དབང་ཕྱུག་ཆེན་པོ་ལ་སོགས་པའི་ལྷ་ཆེན་པོ་རྣམས་ཀྱང་བྲན་དུ་འགུགས་པའི་ནུས་མཐུ་ཡོད་ན། ཕྲ་མོ་གཞན་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། དེ་ལ་འཇིག་རྟེན་བདུན་ཞེས་པ་སྣོད་བདུན་དང་། བཅུད་ཀྱི་བདུན་དང་། སྣོད་བཅུད་བསྡོམས་པའི་བདུན་ལ་སོགས་པའི་འཆད་ཚུལ་མི་གཅིག་པ་མང་ཡང་། འདིར་ནི་མཐུ་དང་ལྡན་པའི་འཇིག་རྟེན་བདུན་ཏེ། ཀླུ་དང་ཡི་དྭགས་དང་ལྷ་མ་ཡིན་དང་། མི་དང་རིག་པ་འཛིན་པ་དང་མིའམ་ཅི་དང་ལྷའི་འཇིག་རྟེན་ནོ། །

[Block 42 [HEADING]]
#### སྦས་དོན། ^1-5-2-0

[Block 43]
སྦས་དོན་ནི་ཏུཏྟཱ་ར་ནི་གདུང་པ་སྟེ། གཏུམ་མོའི་མེས་གདུང་བའོ། །

[Block 44]
ཧཱུྃ་གི་ཡི་གེ་ནི་མི་ཤིགས་པའི་སྒྲ་སྟེ་གཏུམ་མོ་ལས་བྱུང་བའོ། །

[Block 45]
འདོད་པ་ནི་གསང་བའི་འཁོར་ལོ་དང་། ཕྱོགས་ནི་དབུ་མའི་ནང་སྟེ་སྒྲ་དེས་གང་བ་དང་། ནམ་མཁའ་གང་མ་ནི་བརྗོད་བྲལ་ལོ། །

[Block 46]
འཇིག་རྟེན་བདུན་ནི་རྩ་འཁོར་ལོ་ལྔ་དང་། མེ་རླུང་གི་འཁོར་ལོ་གཉིས་ཏེ་བདུན་གཏུམ་མོ་འབར་བ་ཞུ་པའི་ཀུན་དེས་གང་བ་དང་། ཀུན་ད་དེ་ཉིད་མ་ལུས་པར་སླར་ཡང་གསང་བ་ནས་སྤྱི་བོའི་བར་དུ་འགུགས་པའོ། །

[Block 47]
ཚིག་བཅད་དྲུག་པ་ཕྱག་འཚལ་བརྒྱ་བྱིན་སོགས་ལ།

[Block 48 [VERSE]]
བརྒྱ་བྱིན་ནི་ལྷའི་འགྲོ་བ་རྣམས་ཀྱི་རྒྱལ་པོའོ། །
མེ་ལྷ་ནི་དྲང་སྲོང་གི་གཙོ་བོའོ། །
ཚངས་པ་འཇིག་རྟེན་གྱི་བྱེད་པོར་འདོད་པའོ། །

[Block 49]
རླུང་ལྷ་ནི་འཇིག་རྟེན་གཟོའི་གནས་དང་བཀོད་པའི་ཁྱད་པར་བྱེད་པའོ། །

[Block 50]
དྲག་པོ་དང་གཏོགས་འདོད་དང་། དྲང་སྲོང་ཉི་མའི་མདོག་དང་། ཕྱྭ་ལ་སོགས་པ་བྱེད་པོའམ་དབང་ཕྱུག་ཏུ་གྲགས་པ་སྣ་ཚོགས་པ་ནི། སྣ་ཚོགས་དབང་ཕྱུག་སྟེ། འཇིག་རྟེན་ན་ཆེས་ཆེ་བར་གྲགས་པ་དེ་རྣམས་ཀྱིས་ཀྱང་། མཆོད་པའི་གནས་སུ་གྱུར་ཅིང་། འབྱུང་པོ་ནི་ཚོགས་ཀྱི་བདག་པོ་ལ་སོགས་པ་བགེགས་དང་ལོག་པར་འདྲེན་པ་རྣམས་སོ། །

[Block 51]
རོ་ལངས་ནི་རོ་ལངས་ཀྱི་ལས་བྱེད་པས་ལས་ཀྱི་མིང་བྱེད་པ་པོ་ལ་བཏགས་པ་སྟེ། ལྷའི་སྲིན་པོའི་རིགས་སྔགས་ཀྱི་མཐུ་གྲུབ་པ། རྫུ་འཕྲུལ་ཆེན་པོ་དང་ལྡན་པའི་འཇིགས་བྱེད་དགུ་ལ་སོགས་པའོ། །

[Block 52]
དྲི་ཟ་ནི་སྣ་ཚོགས་ཤིང་རྟ་ལ་སོགས་པ་རྣམས་དང་། གནོད་སྦྱིན་ནི་རྣམ་ཐོས་བུ་ལ་སོགས་པ་གཏེར་གྱི་བདག་པོ་རྣམས་དང་། མདངས་འཕྲོག་པའི་ལྷ་མ་སྲིན་རྣམས་ཏེ། འདུལ་བར་དཀའ་བའི་ཚོགས་དེ་རྣམས་ཀྱིས་ཀྱང་། ཁྱོད་ཀྱི་མདུན་ནས་བསྟོད་པར་བྱེད་པ་སྟེ་འགྲོ་བ་ཐམས་ཅད་ཀྱིས་བླ་མར་བསྔགས་སོ། །

[Block 53 [HEADING]]
#### སྦས་དོན། ^1-6-2-0

[Block 54]
སྦས་དོན་ནི་བརྒྱ་བྱིན་སོགས་ལྔ་ནི་འབྱུང་བ་ལྔ་སྟེ། བརྒྱ་བྱིན་ནི་ས། མེ་ལྷ་ནི་མེ། ཚངས་པ་ནི་ཆུ། རླུང་ལྷ་ནི་རླུང་། སྣ་ཚོགས་དབང་ཕྱུག་ནམ་མཁའ་འོ། །

[Block 55]
དེ་ལྟར་ཁམས་ལྔའི་རླུང་ཐིག་ལེར་ཐིམ་པ་ནི་མཆོད་པའོ། །

[Block 56]
འབྱུང་པོ་རྩ། རོ་ལངས་ཐིག་ལེ། དྲི་ཟ་རླུང་། གནོད་སྦྱིན་རྣམ་རྟོག་སྟེ། དེ་དག་ཀྱང་ཐིག་ལེར་ཐིམ་པ་ནི་མདུན་ནས་བསྟོད་པའོ། །

[Block 57]
འདིས་ནི་འཇིག་པའི་ཡན་ལག་བསྟན་ནོ། །

[Block 58]
ཚིག་བཅད་བདུན་པ་ཕྱག་འཚལ་ཏྲཊ་ཅེས་སོགས་ལ་ཏཊ་དང་ཕཊ་ཀྱི་གསང་སྔགས་ལ་སོགས་པ། འཕགས་མ་སྒྲོལ་མས་གསུངས་པའི་རིག་སྔགས།

[Block 59]
དྲག་ཤུལ་སྤྱོད་པ་རྣམས་ཀྱི་མཐུ་ལས།

[Block 60]
དྲག་པོའི་ལས་སྣ་ཚོགས་པར་བྱེད་པར་འགྱུར་ལ། དེ་ཡང་གཞན་ལ་ཕན་པའི་ཕྱིན་གདུལ་དཀའ་འདུལ་བ་ཡིན་གྱི། གནོད་པའི་སྦྱོར་བ་ནི་མ་ཡིན་ནོ། །

[Block 61]
རིག་སྔགས་དེ་ལྟ་བུའི་ཁད་པར་འགའ་ཞིག་ལས།

[Block 62]
ཕ་རོལ་པོའི་བྱད་མ་རྣམས་ཀྱི་འཁྲུལ་འཁོར་དང་སྔགས་ཀྱི་སྟོབས་བཟློག་ཅིང་འཇོམས་པ་དང་། ཁྲོ་མོའི་སྐུར་བསྟན་ཏེ། གཡས་བསྐུམ་གཡོན་བརྐྱང་ལ་སོགས་པའི་ཞབས་ཀྱིས། གདུག་པ་ཅན་རྣམས་མནན་པའི་ཚུལ་གྱིས། རིམས་དང་ནད་ཡམས་ལ་སོགས་པ་ཞི་བར་མཛད་ཅིང་། ཁྲོ་བས་འཁྲུགས་པའི་སྐུ་ལས་མེ་འབར་ཞིང་ཤིན་ཏུ་འབར་བ་སྟོན་པས། གཤིན་རྗེ་ལ་སོགས་པའི་གདོན་རྣམས་བྱེར་བ་དང་། འགྲོ་བ་རྣམས་ལ་སྲུང་བ་ཆེན་པོ་མཛད་པ་ཡིན་ནོ། །

[Block 63 [HEADING]]
#### སྦས་དོན། ^1-7-2-0

[Block 64]
སྦས་དོན་ནི་ཏྲཊ་ཅེས་པ་ནི་དལ་བ། ཕཌ་ནི་འགས་པ་སྟེ་རྣམ་རྟོག་འཇོམས་པའོ། །

[Block 65]
ཕ་རོལ་ལས་དང་ཉོན་མོངས་པའི་འཕྲུལ་འཁོར་དུས་སྦྱོར་བཅུ་གཉིས་ཀྱི་རླུང་སོགས་འགགས་པ་དང་། གཡས་ཀྱི་རྩ་རོ་མ་ནི་བསྐུམ་པ་སྟེ་ཁ་སྟེང་དུ་བལྟ་བ་དང་། གཡོན་གྱི་རྩ་རྐྱང་མ་ནི་བརྐྱང་པ་སྟེ་ཁ་འོག་ཏུ་བལྟ་བ་ཡིན་ལ། དེ་གཉིས་དབུ་མའི་ཞབས་ཀྱིས་ཡོངས་སུ་མནན་པ་ནི། དེ་གཉིས་ཀྱི་རླུང་དབུ་མར་འགགས་པའོ། །

[Block 66]
དེ་ལས་གཏུམ་མོའི་མེ་འབར་བ་དང་། ཧཾ་ཡིག་ཞུ་བའི་ཆུ་འཁྲུགས་པ་དང་། སླར་ཡང་ཤིན་ཏུ་འབར་ཞིང་ཆེས་ཞུ་བ་ལ་སོགས་པ་སྟེ། སྲོག་རྩོལ་གྱི་ཡན་ལག་གོ། །

[Block 67]
ཚིག་བཅད་བརྒྱད་པ་ཕྱག་འཚལ་ཏུ་རེ་སོགས་ལ་ཨོཾ་ཏུ་རེ་སོགས་ཀྱི་རིག་སྔགས་ཟློས་པའི་མཐུས། རང་བཞིན་ཞི་བའི་དབྱིངས་ལས་སྒྲོལ་མ་ཉིད་འཇིགས་པ་ཆེན་པོའི་སྐུར་སྟོན་པར་འགྱུར་ལ། དེས་ནི་བདུད་ཀྱི་དཔའ་བོ་སྟེ་དམག་དཔོན་རྣམས་འཇོམས་ཤིང་། ཞལ་རས་ཆུ་སྐྱེས་ཁོ་གཉེར་དང་ལྡན་པར་མཛད་པས། བསྟན་པ་ལ་སྡང་བ་དང་། སེམས་ཅན་མང་པོ་ལ་འཚེ་བ་དང་། སྒྲུབ་པ་པོ་ལ་བར་དུ་གཅོད་པའི་དགྲ་རྣམས་གསོད་པ་མ་སྟེ། འཆི་བའམ་གནོད་པའི་བསམ་སྦྱོར་མེད་པར་འགྱུར་བའོ། །

[Block 68]
དེའི་ནང་གི་དོན་ལ། བདུད་ཀྱི་དཔའ་བོ་འཇོམས་པ་ནི་ཕྱོགས་ལས་རྣམ་པར་རྒྱལ་བའི་སྤྱོད་པའོ། །

[Block 69]
ཁྲོ་གཉེར་ནི་ལྷའི་ཆས་སུ་ཞུགས་པ་མཚོན་ཏེ། དེས་ཀྱང་ཡེ་ཤེས་ཀྱི་སྐུ་གྲུབ་པ་མཚོན་པ་ཡིན་ལ། བདེ་སྟོང་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ནི་སྐལ་དམན་རྣམས་སྐྲག་པར་མཛད་པའི་ཕྱིར་འཇིགས་པ་ཆེན་པོའོ། །

[Block 70]
ཡེ་ཤེས་དང་ཡེ་ཤེས་ཀྱི་སྐུ་དེ་གཉིས་ཀྱིས་དགྲ་བོ་སྟེ་སྒྲིབ་པ་མ་ལུས་པ་བཅོམ་ནས། ཏུ་རེ་སྟེ་མྱུར་བར་ལམ་གོང་མ་རྣམས་བགོད་ནས་རྫོགས་པའི་སངས་རྒྱས་ཐོབ་པའོ། །

[Block 71]
འདི་ནི་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་གི་འབྲས་བུ་ཀུན་ཏུ་འོད་ལ་སོགས་པའི་ས་བཅུ་གཉིས་སོ། །

[Block 72 [HEADING]]
### ཕྱག་འཚལ་དགུ་པ། ^1-9-0

[Block 73 [HEADING]]
#### ཚིག་འགྲེལ། ^1-9-1-0

[Block 74]
ཚིགས་བཅད་དགུ་པ་ཕྱག་འཚལ་དཀོན་མཆོག་སོགས་ལ། དཀོན་མཆོག་གསུམ་མཚོན་པར་བྱེད་པ་ཨུཏྤ་ལའི་ཕྱག་རྒྱ་ནི་སྒྲོལ་མའི་དམ་ཚིག་གི་ཕྱག་རྒྱ་སྟེ། སྙིམས་པ་ཁ་སྦྱར་གྱི་གུང་མོ་སྦྱར་ཞིང་མཛུབ་མོས་བརྟེན་ནས་མཐེ་བོང་གཤིབས་ཏེ་རྩེ་བར་བཀོད་པ་ཐུགས་ཀར་གཏོང་པས་རྣམ་པར་བརྒྱན་པ་ནི། རྗེས་འཇུག་རྣམས་ཀྱིས་ཀྱང་དམ་ཚིག་གི་ཕྱག་རྒྱ་དེ་ལྟ་བུ་ཆོག་བཞིན་དུ་བཅིངས་ན། རིག་སྔགས་ཀྱི་ལྷས་བྱིན་གྱིས་བརླབ་པའི་དོན་སྔོན་བྱུང་ལ་བཅོམ་ལྡན་འདས་མ་ཉིད་ཕྱག་རྒྱ་དེ་ལྟ་བུ་འཆིང་བའི་སྐུའི་རྣམ་འགྱུར་དང་། ཕྱོགས་ཀྱི་འཁོར་ལོ་སྟེ་ཕྱོགས་བཅུའི་ཞིང་ཁམས་མ་ལུས་པ། རང་གི་སྐུ་ལས་བྱུང་བའི་འོད་ཟེར་གྱི་ཚོགས་རབ་ཏུ་འཁྲུགས་ཤིང་འཕྲོས་པས་ཁབ་ཅིང་བརྒྱན་པར་མཛད་པའོ། །

[Block 75]
དེ་ཉིད་རྗེས་འཇུག་ལ་ནི། ཕྱག་རྒྱ་དེས་སྤྱན་དྲངས་ན་ཕྱོགས་བཅུའི་ཞིང་ནས་འོད་ཟེར་འཕོ་ཞིང་དངོས་སུ་འབྱོན་པའོ། །
--- END BLOCKS ---
