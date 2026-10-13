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
༄༅། །ཀརྨ་མཻ་ཏྲིའི་སྒྲོལ་བསྟོད་ཟིན་བྲིས་བཞུགས་སོ། །

[Block 2 [HEADING]]
## མཆོད་བརྗོད། ^I-0

[Block 3]
ན་མོ་གུ་རུ་ཨཱརྻ་ཏཱ་ར་ཡཻ།

[Block 4]
ཕྱག་འཚལ་ཉེར་གཅིག་ལ་བསྟོད་པ་དངོས་དང་། ཕན་ཡོན་ནོ། །

[Block 5]
དང་པོ་ལ་ཉེར་གཅིག་ཡོད་པ་ལས།

[Block 6 [HEADING]]
## བསྟོད་པ་དངོས། ^1-0

[Block 7 [HEADING]]
### ཕྱག་འཚལ་དང་པོ། ^1-1-0

[Block 8]
དང་པོ་ནི། ཕྱག་འཚལ། གང་ལ་ན། སྒྲོལ་མ་ལའོ། །

[Block 9]
དེ་ལ་ཡོན་ཏན་ནམ་ཁྱད་པར་ཅི་ཡོད་ཅེ་ན། སེམས་ཅན་སྐད་ཅིག་གིས་སྒྲོལ་བས་ན་མྱུར་མ། ཉོན་མོངས་བདུད་སྡེ་འཇོམས་པས་ན་དཔའ་མོ། སྤྱན་གྱི་འོད་ནི་སྐད་ཅིག་གིས་གློག་འཁྱུག་པ་དང་འདྲ་བས་སྒྲོལ་མ་དེ་ནི་ས་འོག་ས་སྟེང་ས་བླའི་འཇིག་རྟེན་གསུམ་གྱི་མགོན་པོ་སྤྱན་རས་གཟིགས་ཀྱི་ཆུ་སྐྱེས་ལས་སྐྱེས་པའི་ཞལ་གྱི་མེ་ཏོག་པདྨའི་གེ་སར་བྱེ་བ་ལས་ནི་ཉེ་བར་བྱུང་སྒྲོལ་མ་ལའོ། །

[Block 10 [HEADING]]
### ཕྱག་འཚལ་གཉིས་པ། ^1-2-0

[Block 11]
གཉིས་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། སྟོན་ཀའི་ཟླ་བ་ཉ་ཀུན་ཏུ་གང་བ་བརྒྱ་ཐམ་པ་ནི་རྣམས་པ་བརྩེགས་པ་ལྟར་དཀར་ཞིང་མཛེས་པའི་ཞལ་དང་ལྡན་མ། སྐར་མའི་ཚོགས་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས་འགྲན་དུ་མེད་ཅིང་རབ་ཏུ་ཕྱེ་བའི་འོད་དཀར་པོ་རབ་ཏུ་འབར་བའི་སྒྲོལ་མ་ལའོ། །

[Block 12 [HEADING]]
### ཕྱག་འཚལ་གསུམ་པ། ^1-3-0

[Block 13]
གསུམ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། གསེར་ལྟར་མཛེས་ཤིང་ཅུང་ཟད་སྔོ་བའི་མདོག་ཅན་ཆུ་ནི་སྐྱེ་ཕྱིར་པདྨ་རབ་ཏུ་བཀྲ་བས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་པའི་སྒྲོལ་མ། དེ་ཡང་སྦྱིན་པ་དང་། བརྩོན་འགྲུས་དང་། དཀའ་ཐུབ་སྟེ་ཚུལ་ཁྲིམས་དེས་ཉོན་མོངས་པ་ཞི་བར་བྱེད་པ། བཟོད་པ་དང་། བསམ་གཏན་དང་། །

[Block 14 [HEADING]]
### ཕྱག་འཚལ་བཞི་པ། ^1-4-0

[Block 15]
བཞི་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར་ལྟར་མཆོད་པའི་གནས་སུ་གྱུར་ཅིང་། བདུད་སོགས་ཕས་རྒོལ་མཐའ་ཡས་པ་ལས་རྣམ་པར་རྒྱལ་བ་སྤྱོད་པའི་སྒྲོལ་མ། ཕར་ཕྱིན་བཅུ་དང་ས་བཅུ་མ་ལུས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་གོ་འཕང་ཐོབ་པའི་བདག་ཉིད་དེ་ལ་རྒྱལ་བའི་སྲས་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་ཐམས་ཅད་ཀྱི་ཡུམ་དུ་གྱུར་པས་གུས་པ་ཆེན་པོའི་ཤིན་ཏུ་བརྟེན་པས་སྒྲོལ་མ་ལའོ། །

[Block 16 [HEADING]]
### ཕྱག་འཚལ་ལྔ་པ། ^1-5-0

[Block 17]
ལྔ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཏུཏྟཱ་རེ་ཧཱུཾ་ཞེས་པའི་ཡི་གེས་འདོད་ཁམས་དང་། ཕྱོགས་ཏེ་གཟུགས་ཁམས་དང་། ནམ་མཁའ་སྟེ་གཟུགས་མེད་པའི་ཁམས་གང་བར་མཛད་མ་འགྲོ་བ་རྒྱུད་ལྔ་ཁམས་གོང་མ་གཉིས་ཏེ་འཇིག་རྟེན་བདུན་པོ་ཞབས་ཀྱིས་མནན་ཏེ། རིག་སྔགས་ཀྱི་མཐུས་ལུས་པ་མེད་པར་དབང་དུ་འགུགས་པར་ནུས་པའམ་མཛད་པའི་སྒྲོལ་མ་ལའོ། །

[Block 18 [HEADING]]
### ཕྱག་འཚལ་དྲུག་པ། ^1-6-0

[Block 19]
དྲུག་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། བརྒྱ་བྱིན་དང་། མེ་ལྷ་དང་། ཚངས་པ་དང་། རླུང་ལྷ་དང་། སྣ་ཚོགས་དབང་ཕྱུག་སྟེ་དབང་ཕྱུག་ཆེན་པོ་དག་གིས་མཆོད་མ། ཚོགས་བདག་འབྱུང་པོ། དུར་ཁྲོད་ན་གནས་པའི་རོ་ལངས། ཟུར་ཕུད་ལྔ་སོགས་དྲི་ཟ་རྣམས་དང་། སྨུག་འཛིན་སོགས་གནོད་སྦྱིན་གྱི་ཚོགས་ཀྱིས་གང་གི་མདུན་ནས་རྟག་པར་བསྟོད་པའི་སྒྲོལ་མ་ལའོ། །

[Block 20 [HEADING]]
### ཕྱག་འཚལ་བདུན་པ། ^1-7-0

[Block 21]
བདུན་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཞལ་ནས་ཏྲད་ཅེས་བྱ་བ་དང་། ཕཊ་ཅེས་བྱ་བ་ལ་སོགས་པའི་དྲག་པོའི་སྒྲ་ཡིས་ཕ་རོལ་པོས་གནོད་པའི་འཁྲུལ་འཁོར་རབ་ཏུ་འཇོམས་པར་མཛད་མ། གཡས་བསྐུམ་ཞིང་གཡོན་བརྐྱང་བའི་ཞབས་ཀྱིས་འཇིག་རྟེན་བདུན་པོ་མནན་ཏེ། མེ་དཔུང་འབར་ཞིང་འཁྲུགས་པ་ཤིན་ཏུ་འབར་བའི་དབུས་ན་བཞུགས་པའི་སྒྲོལ་མ་ལའོ། །

[Block 22 [HEADING]]
### ཕྱག་འཚལ་བརྒྱད་པ། ^1-8-0

[Block 23]
བརྒྱད་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཏུ་རེ་ལ་སོགས་པའི་གསུང་གི་འཇིགས་པ་ཆེན་པོ་བརྒྱད་ལས་སྐྱོབ་ཅིང་། ལྷའི་བུ་སོགས་བདུད་ཀྱི་དཔའ་བོ་བཞི་རྣམ་པར་འཇོམས་མ། ཆུ་ལས་སྐྱེས་པའི་མེ་ཏོག་མཛེས་པའི་ཞལ་ནས་ཁྲོ་གཉེར་དང་ལྡན་པར་མཛད་ཅིང་། ཉོན་མོངས་ལ་སོགས་པའི་དགྲ་བོ་ཐམས་ཅད་གཅིག་ཀྱང་མ་ལུས་པ་གསོད་པར་བྱེད་པའི་སྒྲོལ་མ་ལའོ། །

[Block 24 [HEADING]]
### ཕྱག་འཚལ་དགུ་པ། ^1-9-0

[Block 25]
དགུ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཕྱག་གཡོན་མཛུབ་གུང་མཐེའུ་ཆུང་གསུམ་དཀོན་མཆོག་གསུམ་མཚོན་པའི་སྐྱབས་སྦྱིན་གྱི་ཕྱག་རྒྱའི་སོར་མོ་ཤིན་ཏུ་མཛེས་པའི་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་པར་མཛད་མ། གཅིག་མ་ལུས་པའི་ཕྱོགས་ཀྱི་འོད་ཟེར་ཐམས་ཅད་ཕྱག་གཡས་མཆོག་སྦྱིན་ཕྱག་རྒྱའི་མཐིལ་དུ་འཁོར་ལོས་བརྒྱན་པའི་ཆ་ལས་འཕྲོས་པའི་རང་གི་འོད་ཀྱི་ཚོགས་རྣམས་རབ་ཏུ་འཁྲུགས་པས་གང་ཞིང་འོད་གཞན་རྣམས་ཟིལ་གྱིས་གནོན་པར་མཛད་མ་ལའོ། །

[Block 26 [HEADING]]
### ཕྱག་འཚལ་བཅུ་པ། ^1-10-0

[Block 27]
བཅུ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། འགྲོ་བ་ཀུན་གྱི་རེ་བ་བསྐང་བའི་རབ་ཏུ་དགའ་བ་འབྱུང་བར་བགྱིད་པའི་རིན་པོ་ཆེའི་དབུ་རྒྱན་དང་། ནོར་བུའི་དོ་ཤལ་སོགས་འོད་ཟེར་གྱི་ཕྲེང་བ་འབར་ཞིང་འཁྲུགས་པ་སྤེལ་ལེགས་པའི་བརྒྱན་པའི་སྒྲོལ་མ་བཞད་པ་དང་རབ་ཏུ་བཞེད་པའི་སྔགས་ཏུཏྟཱ་ར་ལ་སོགས་པའི་སྒྲ་ཡིས། གཞན་འཕྲུལ་དབང་བྱེད་ཀྱི་བདག་པོ་བདུད་དང་། གཞན་ཡང་འཇིག་རྟེན་ཐམས་ཅད་དབང་དུ་བསྡུ་བར་བྱེད་པའི་སྒྲོལ་མ་ལའོ། །

[Block 28 [HEADING]]
### ཕྱག་འཚལ་བཅུ་གཅིག་པ། ^1-11-0

[Block 29]
བཅུ་གཅིག་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཕྱོགས་སྐྱོང་བཅུ་སོགས་ས་གཞི་སྐྱོང་བའི་ཚོགས་རྣམས་མ་ལུས་པ་ཐམས་ཅད་བྲན་དུ་འགུག་པར་ནུས་མ་ཉིད་ཀྱི་སྒྲོལ་མ། ཞལ་ཁྲོ་གཉེར་གཡོ་བའི་ཐུགས་ཀར་ཡི་གེ་ཧཱུྃ་གིས་མཚན་པའི་འོད་ཀྱིས་འཇིགས་ཤིང་ཕོངས་པར་གྱུར་པའི་འགྲོ་བ་ཐམས་ཅད་སྡུག་བསྔལ་ལས་རྣམ་པར་བསྒྲལ་ནས་བདེ་བ་དམ་པ་ལ་འགོད་པར་མཛད་པའི་སྒྲོལ་མ་ལའོ། །

[Block 30 [HEADING]]
### ཕྱག་འཚལ་བཅུ་གཉིས་པ། ^1-12-0

[Block 31]
བཅུ་གཉིས་པ་ནི། ཕྱག་འཚལ། གང་ལ་ནི། ཟླ་བའི་དུམ་བུ་སྟེ་ཕྱེད་པའི་དབུ་ལ་བརྒྱན་ཅིང་། བརྒྱན་པ་ཐམས་ཅད་ལས་ཀྱང་འོད་དཀར་པོ་ཤིན་ཏུ་འབར་བའི་བདག་ཉིད་མ།

[Block 32]
རལ་པའི་ཁྲོད་ན་རིགས་བདག་འོད་དཔག་མེད་བཞུགས་པ་ལས།

[Block 33]
སེམས་ཅན་གྱི་དོན་དུ་རྟག་པར་ཤིན་ཏུ་འཚེར་བའི་འོད་རབ་ཏུ་འགྱེད་པར་མཛད་པའི་སྒྲོལ་མ་ལའོ། །

[Block 34 [HEADING]]
### ཕྱག་འཚལ་བཅུ་གསུམ་པ། ^1-13-0

[Block 35]
བཅུ་གསུམ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། བསྐལ་པ་ཐ་མ་སྟེ་འཇིག་པའི་དུས་ཀྱི་མེ་ལྟར་རབ་ཏུ་འབར་བའི་ཕྲེང་བས་བསྐོར་བའི་དབུས་ན་གནས་མ། གཡས་བརྐྱང་གཡོན་བསྐུམ་པའི་སྟབས་ཀྱིས་འོད་ཀྱི་ཕྲེང་བས་བསྐོར་བའི་བདེ་བ་སྦྱིན་པའི་དགའ་བར་མཛད་ཅིང་། དགྲ་ཡི་དཔུང་ཐམས་ཅད་རྣམ་པར་འཇོམས་པར་མཛད་མ་ལའོ། །

[Block 36 [HEADING]]
### ཕྱག་འཚལ་བཅུ་བཞི་པ། ^1-14-0

[Block 37]
བཅུ་བཞི་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ས་གཞི་ངོས་ལ་སྡིགས་མཛུབ་དང་བཅས་པའི་ཕྱག་གི་མཐིལ་གྱིས་བསྣུན་ཅིང་ཞབས་ཀྱིས་བརྡུང་བར་མཛད་མ། ཁྲོ་གཉེར་ཅན་དུ་མཛད་ཅིང་། གཡས་ཀྱི་ཕྱག་མཐིལ་ན་ཡི་གེ་ཧཱུྃ་གི་འོད་འཕྲོ་བས་ས་རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས་པར་མཛད་ཅིང་། སེམས་ཅན་ཀུན་གྱི་བར་གཅོད་སེལ་བའི་སྒྲོལ་མ་ལའོ། །

[Block 38 [HEADING]]
### ཕྱག་འཚལ་བཅོ་ལྔ་པ། ^1-15-0

[Block 39]
བཅོ་ལྔ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཟག་མེད་ཀྱི་རང་བཞིན་བདེ་མ། ཉོན་མོངས་སྤང་བའི་དགེ་མ། རྩུབ་རེག་བྲལ་བའི་ཞི་མ། མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་མཆོག་ཏུ་རབ་ཏུ་ཞི་བའི་སྤྱོད་ཡུལ་ཅན་ཉིད་དུ་འགྱུར་བའི་སྒྲོལ་མ། སྭཱ་ཧཱ་དང་ཨོཾ་ཞེས་པ་དང་ཡང་དག་པར་ལྡན་པའི་སྔགས་ཀྱིས་སྡིག་པ་དང་སྒྲིབ་པ་ཆེན་པོ་ཐམས་ཅད་འཇོམས་པར་ནུས་པ་ཉིད་ཀྱི་སྒྲོལ་མ་ལའོ། །

[Block 40 [HEADING]]
### ཕྱག་འཚལ་བཅུ་དྲུག་པ། ^1-16-0
--- END BLOCKS ---
