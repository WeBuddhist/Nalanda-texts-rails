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
༄༅། །ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཕན་ཡོན་དང་བཅས་པ་གསལ་བའི་མེ་ལོང་ཞེས་བྱ་བ་བཞུགས་སོ།། །།

[Block 2 [HEADING]]
## དང་པོ་མདོར་བསྟན་པ། ^1-0

[Block 3]
ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གིས་བསྟོད་པ་ལ་མདོར་བསྟན། རྒྱས་བཤད།

[Block 4]
ཕན་ཡོན་བསྟན་པས་མཇུག་བསྡུ་བ་གསུམ་ལས། དང་པོ་མདོར་བསྟན་པ་ནི།

[Block 5]
ཨོཾ་རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 6]
ཞེས་པ་སྟེ། ཨོཾ་ནི་སྐུ་ལྔ་ཡེ་ཤེས་ལྔ་ཡི་ངོ་བོ་སེམས་ཅན་གྱི་སེམས་ཀྱི་དྲི་མ་སྦྱངས་བར་མཛད་པ། སྐྱབས་སུ་འགྲོ་བར་བྱེད་པ་དང་ཕྱག་འཚལ་བར་བྱེད་པ་ཨོཾ་ཞེས་བརྗོད་དོ། །

[Block 7]
རྗེ་བཙུན་མ་ནི་འཇིག་རྟེན་གསུམ་གྱི་མགོན་སྐྱབས་སུ་གྱུར་པའི་ཕྱིར་དང་སྡོམ་པ་གསུམ་ཡང་དག་པར་ལྡན་པས་ནའོ། །

[Block 8]
འཕགས་མ་ནི་སོ་སྐྱེའི་ས་ལས་རིང་དུ་འཕགས་པས་ནའོ། །

[Block 9]
སྒྲོལ་མ་ནི་སེམས་ཅན་ཐམས་ཅད་སངས་རྒྱས་ཀྱི་ས་ལས་སྒྲོལ་བར་མཛད་པས་ནའོ། །

[Block 10 [HEADING]]
## གཉིས་པ་རྒྱས་པར་བཤད་པ། ^2-0

[Block 11]
གཉིས་པ་རྒྱས་པར་བཤད་པ་ལའང༌། སྤྱིར་ལོ་རྒྱུས་ཀྱི་དབང་དུ་བྱས་ཏེ་ཕྱག་འཚལ་བ། སྐུའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ། ཕྲིན་ལས་བསྟན་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ།

[Block 12 [HEADING]]
### དང་པོ་སྤྱིར་ལོ་རྒྱུས་ཀྱི་དབང་དུ་བྱས་ཏེ་ཕྱག་འཚལ་བ། ^2-1-0

[Block 13]
དང་པོ་ནི།

[Block 14 [VERSE]]
ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ། །
སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། །
འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི། །
གེ་སར་བྱེ་བ་ལས་ནི་བྱུང་མ། །

[Block 15]
ཞེས་པ་སྟེ། སྒྲོལ་མ་ནི་དང་པོ་སྐུ་ཅི་ལས་བྱུང༌། བར་དུ་སེམས་ཅན་གྱི་དོན་ཅི་ལྟ་བུ་མཛད་ཅེ་ན།

[Block 16]
དང་པོ་འཇིག་རྟེན་གསུམ་གྱི་མགོན་པོ་འཕགས་པ་སྤྱན་རས་གཟིགས་དབང་ཕྱུག་གིས་གདུལ་བྱ་སེམས་ཅན་ཐམས་ཅད་སངས་རྒྱས་ཀྱི་གོ་འཕང་ལ་བཀོད་པར་མཛད་ན་ཡང་། སེམས་ཅན་གྱི་གནས་སྟོང་དུ་མེད་པ་མ་ཟད་སྡུག་བསྔལ་ཆེན་པོ་ཡོད་པ་ལ་བརྟེན་ནས། སྤྱན་ཆབ་མང་དུ་བསིལ་བས་ཆུ་ཡི་རྒྱུན་དུ་གྱུར། དེ་ལས་མེ་ཏོག་ཨུཏྤལ་ལ་སྐྱེས་ཏེ། དེ་ཡི་གེ་སར་ལས་འཁྲུངས་པས་ན། གེ་སར་བྱེ་བ་ལས་ནི་བྱུང་མ། །ཞེས་དང༌། འཁྲུངས་ནས་གདུལ་བྱའི་དོན་ཅི་ལྟ་བུ་མཛད་སྙམ་ན། ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ་ཞེས་པས་བསྟན་ཏེ། སེམས་ཅན་གྱི་དོན་མྱུར་དུ་མཛད་པས་ན་མྱུར་མ་དང༌། སྙིང་སྟོབས་དཔའ་མི་ཞུམ་པས་ན་དཔའ་མོ། དེ་ལྟར་མྱུར་ཞིང་དཔའ་བའི་རྗེ་བཙུན་སྒྲོལ་མ་དེ་ཉིད་ཀྱིས་སེམས་ཅན་གྱི་དོན་དུ་ཉིན་མཚན་དུས་དྲུག་ཏུ་ཡེ་ཤེས་སྤྱན་གྱིས་གཟིགས་པ་མི་གཡེལ་བར། སུ་ནི་རྒུད། སུ་ནི་དར་སོགས་གཟིགས་པ་ལ་སྒྲིབ་པ་མེད་པས་ན། སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། །ཞེས་པ་སྟེ། དེ་ལྟ་བུའི་ཡོན་ཏན་དང་ལྡན་པའི་རྗེ་བཙུན་མ་ལ་སྒོ་གསུམ་གུས་པས་ཕྱག་འཚལ་ལོ། །

[Block 17 [HEADING]]
### གཉིས་པ་སྐུའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ། ^2-2-0

[Block 18 [HEADING]]
#### དང་པོ་ལོངས་སྐུའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ། ^2-2-1-0

[Block 19]
གཉིས་པ་སྐུའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་ལ། ལོངས་སྐུའི་རྣམ་པ་དང༌། ཆོས་སྐུའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་གཉིས། དང་པོ་ལོངས་སྐུའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་ལའང་ཞི་བའི་རྣམ་པ་དང་།

[Block 20 [HEADING]]
##### དང་པོ་ཞི་བའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ། ^2-2-1-1-0

[Block 21 [HEADING]]
###### དང་པོ་ཞལ་མདངས་གསལ་ཞིང་འོད་ཟེར་འཕྲོ་བའི་སྒོ་ནས་བསྟོད་པར་མཛད་པ། ^2-2-1-1-1-0

[Block 22]
ཁྲོ་བོའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་གཉིས་ལས། དང་པོ་ཞི་བའི་རྣམ་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་ལ། ཕྱག་འཚལ་དྲུག་གི་སྒོ་ནས་བསྟོད་པར་མཛད་པ་ལ། དང་པོ་ཞལ་མདངས་གསལ་ཞིང་འོད་ཟེར་འཕྲོ་བའི་སྒོ་ནས་བསྟོད་པར་མཛད་པ་ནི།

[Block 23 [VERSE]]
ཕྱག་འཚལ་སྟོན་ཀའི་ཟླ་བ་ཀུན་ཏུ། །
གང་བ་བརྒྱ་ནི་བརྩེགས་པའི་ཞལ་མ། །
སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས། །
རབ་ཏུ་ཕྱེ་བའི་འོད་རབ་འབར་མ། །

[Block 24]
ཞེས་པ་སྟེ། སྤྱིར་ཟླ་བ་དེ་དངོས་པོ་གཞན་ལས་ཁྱད་པར་དུ་འཕགས་པ་བཀྲག་མདངས་དང་ལྡན་པ་ཞིག་ཡིན་ལ། དབྱར་གྱི་དུས་སུ་སྤྲིན་དང་རླངས་པས་སྒྲིབ་ཅིང་། དགུན་གྱི་དུས་སུ་དུ་བ་དང་ས་རྡུལ་གྱིས་སྒྲིབ་ནས་བཀྲག་མདངས་མི་གསལ་བ་ཡིན་ནའང་། སྟོན་གྱི་དུས་སུ་དེ་གཉིས་ཀ་དང་བྲལ་བས་བཀྲག་མདངས་གསལ་བ་ཡིན་ལ། ཚེས་བཅོ་ལྔའི་ཟླ་བ་ནི་གང་བའི་ཆ་དང་ལྡན་པ་དེ་བཞིན་དུ། རྗེ་བཙུན་གྱི་ཞལ་རས་ཀྱང་ཤིན་ཏུ་གསལ་ཞིང་བཀྲག་མདངས་དང་ལྡན་པ། སྟོན་ཀའི་ཟླ་བ་ཉ་གང་བ་དང་ཆོས་མཚུངས་པར་བསྟན་པ་དང༌། དེ་ལས་འོད་ཟེར་འཕྲོ་བར་བསྟན་པར་མཛད་པ་ནི། སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས། །ཞེས་སྐར་མ་སྟོང་ཕྲག་ཙམ་གཅིག་ཏུ་འཚོགས་པ་ན་འོད་ཟེར་ཀྱང་མིག་གི་ལྟ་བས་མི་བཟོད་པར་འཕྲོ་བ་དེ་བཞིན་དུ་རྗེ་བཙུན་མའི་ཞལ་རས་ལས་ཀྱང་འོད་དང་འོད་ཟེར་མིག་གིས་ལྟ་བས་མི་བཟོད་པར་འཕྲོ་བ་སྟེ། ཞལ་རས་མཛེས་པ་དང་། འོད་ཟེར་འཕྲོ་བའི་ཡོན་ཏན་དང་ལྡན་པའི་སྒོ་ནས་ཕྱག་འཚལ་བ་དང༌།

[Block 25 [HEADING]]
###### གཉིས་པ་སྐུ་མདོག་དང་ཕྱག་མཚན་དང་སྐུའི་སྒོ་ནས་བསྟོད་པར་མཛད་པ། ^2-2-1-1-2-0

[Block 26]
གཉིས་པ་སྐུ་མདོག་དང་ཕྱག་མཚན་དང་སྐུའི་སྒོ་ནས་བསྟོད་པར་མཛད་པ་ནི།

[Block 27 [VERSE]]
ཕྱག་འཚལ་གསེར་སྔོ་ཆུ་ནས་སྐྱེས་ཀྱི། །
པདྨས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་མ། །
སྦྱིན་པ་བརྩོན་འགྲུས་དཀའ་ཐུབ་ཞི་བ། །
བཟོད་པ་བསམ་གཏན་སྤྱོད་ཡུལ་ཉིད་མ། །

[Block 28]
ཞེས་པ་སྟེ། སྐུ་མདོག་གི་དབང་དུ་ན། གསེར་སྔོ་ཆུ་ནས་སྐྱེས་ཀྱི། ཞེས་མདངས་ཤིན་ཏུ་གསལ་བའི་ཆ་ནས་གསེར་གྱི་མདངས་དང་ཆོས་མཚུངས་ཤིང་། ཁ་དོག་གི་བཀྲག་མདངས་དངོས་སུ་མེད་པར་སྔོན་པོའི་རྣམ་པ་དང་ལྡན་པར་བསྟན་པར་མཛད་པ་དང་། ཕྱག་མཚན་གྱི་དབང་དུ་ན། ཆུ་ནས་སྐྱེས་ཀྱི་སྟེ། པདྨས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་མ། །ཞེས་དེ་ལ་ཆུ་ལས་སྐྱེས་པའི་མེ་ཏོག་ཨུཏྤལ་སྔོན་པོ་འདབ་མ་ཤིན་ཏུ་ཡངས་ཤིང་རྒྱ་ཆེ་བ་ཕྱག་གཡོན་པས་ཐུགས་ཀར་འཛིན་ཅིང་འདབ་མ་སྙན་གྱི་ཐད་ཀར་ཕྱེ་བ་དེ་སྐུའི་ཡོན་ཏན་དང་ལྡན་པ་བསྟན་པར་མཛད་པ་དང༌། སྐུའི་དབང་དུ་ན། རྗེ་བཙུན་མ་ནི་སྐུ་གང་ལས་བྱུང་སྙམ་ན། རྒྱུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལས་བྱུང་བ་ཡིན་ཏེ་དང་པོ་སྦྱིན་པའི་ཕར་ཕྱིན་དང༌། དཀའ་ཐུབ་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕར་ཕྱིན། བཟོད་པའི་ཕར་ཕྱིན། བརྩོན་འགྲུས་ཀྱི་ཕར་ཕྱིན། བསམ་གཏན་གྱི་ཕར་ཕྱིན། བསམ་གཏན་གྱི་སྤྱོད་ཡུལ་ཞེས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། ཕར་ཕྱིན་དྲུག་ལ་བརྟེན་ནས་བསྐྱེད་པ་ཡིན་ཞིང་། རྒྱུ་ཕར་ཕྱིན་དྲུག་གིས་བསྐྱེད་པ་ཙམ་དུ་མ་ཟད། ཞི་བ་ཞེས་པས་དངོས་བསྟན་གྱི་དབང་དུ་བྱས་ན། ཕྱིན་དྲུག་ལ་སྐྱོན་གྱི་རྣམ་པས་མ་གོས་པ་སྟེ། སྦྱིན་པའི་སྐབས་སུ་སེར་སྣའི་སྐྱོན་གྱིས་མ་གོས་པ་དང༌། ཚུལ་ཁྲིམས་ལ་ཚུལ་འཆལ་གྱི་སྐྱོན་གྱིས་མ་གོས་པ། བཟོད་པ་ལ་ཁོང་ཁྲོའི་སྐྱོན་གྱིས་མ་གོས་པ། བརྩོན་འགྲུས་ལ་ལེ་ལོའི་སྐྱོན་གྱིས་མ་གོས་པ། བསམ་གཏན་ལ་རྣམ་གཡེང་གི་སྐྱོན་གྱིས་མ་གོས་པ། ཤེས་རབ་ལ་ཤེས་འཆལ་གྱི་སྐྱོན་གྱིས་མ་གོས་པར། ཕར་ཕྱིན་དྲུག་ལ་བརྟེན་ནས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ཏེ་གདུལ་བྱ་སེམས་ཅན་གྱི་དོན་མཛད་པ་སྟེ། དེ་ལྟར་སྐུ་མདོག ཕྱག་མཚན། སྐུའི་སྒོ་ནས་བསྟོད་པའམ་ཕྱག་འཚལ་བར་མཛད་པ་དང༌།

[Block 29 [HEADING]]
###### གསུམ་པ་རྒྱལ་དང་རྒྱལ་བའི་སྲས་ཀྱིས་གུས་པས་བསྟེན་པར་མཛད་པ། ^2-2-1-1-3-0

[Block 30]
གསུམ་པ་རྒྱལ་དང་རྒྱལ་བའི་སྲས་ཀྱིས་གུས་པས་བསྟེན་པར་མཛད་པས། དེ་ཡང་ཕྱག་འཚལ་ཞེས་པ་ལ།

[Block 31]
ཐོག་མཐའ་བར་གསུམ་གྱི་གསལ་བྱེད་གསུམ་དུ་ཡོད་པ་ལས།

[Block 32]
སྐབས་འདིར་ཕྱག་འཚལ་བ་ནི་ཐོག་མའི་གསལ་བྱེད་དུ་བསྟན་པར་མཛད་པ་སྟེ། གང་ལ་ན་རྗེ་བཙུན་མ་ལའོ། །

[Block 33]
ཕྱག་འཚལ་བ་ལ་ཡོན་ཏན་གང་དང་ལྡན་ན། རྒྱལ་བ་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱིས་གུས་པས་བསྟེན་ཅིང་ཕྱག་འཚལ་བས་ཕྱག་འཚལ་བའི་ཡུལ་དུ་གྱུར་པ་དང་། དེ་ལའང་སངས་རྒྱས་ཀྱིས་གུས་པས་བསྟེན་པའི་ཚུལ་དང༌།

[Block 34 [HEADING]]
###### **དང་པོ་སངས་རྒྱས་ཀྱིས་གུས་པས་བསྟེན་པའི་ཚུལ།** ^2-2-1-1-3-1-0

[Block 35]
བྱང་སེམས་ཆེན་པོ་རྣམས་ཀྱིས་གུས་པས་བསྟེན་པའི་ཚུལ་ཏེ་རྣམ་པ་གཉིས་ལས། དང་པོ་སངས་རྒྱས་ཀྱིས་གུས་པས་བསྟེན་པའི་ཚུལ་ནི། ཕྱག་འཚལ་དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར། ། ཞེས་པ་སྟེ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་རྗེ་བཙུན་མ་ལ་ཕྱག་འཚལ་བའི་རྒྱུ་མཚན་ཅི་ལྟ་བུ་ཡིན་ཞེ་ན། རྗེ་བཙུན་མ་ནི་ཡུམ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ངོ་བོར་གྱུར་པ་ཡིན་ནོ། །

[Block 36]
སངས་རྒྱས་ཐམས་ཅད་ནི་ཤེར་ཕྱིན་ལ་བརྟེན་ནས་འཁྲུངས་པ་ཡིན་པའི་ཕྱིར་ནའོ། །

[Block 37]
ཆོས་ཀྱི་དབྱིངས་ཤེར་ཕྱིན་གྱི་དོན་དེ་ཚུལ་བཞིན་རྟོགས་ཅིང་མངོན་དུ་གྱུར་ན་སངས་རྒྱས་ཀྱི་གོ་འཕང་ཐོབ་ལ། དེ་མངོན་དུ་མ་གྱུར་ན་སངས་རྒྱས་མི་འཐོབ་པའི་ཕྱིར་རོ། །

[Block 38]
དེས་ན་རྗེ་བཙུན་མ་ནི་ཤེར་ཕྱིན་གྱི་རང་གཟུགས་ཡིན་པའི་ཕྱིར་ན།

[Block 39 [VERSE]]
དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་ཕྱག་འཚལ་བའོ། །
མཐའ་ཡས་རྣམ་པར་རྒྱལ་བར་སྤྱོད་མ། །

[Block 40]
དེ་ཡང་མཐའ་ཡས་པའི་སེམས་ཅན་ཐམས་ཅད་ཀྱིས་ཤེར་ཕྱིན་ཇི་ལྟ་བ་བཞིན་མི་རྟོགས་པའི་འགལ་རྐྱེན་སྒྲིབ་གཉིས་སྦྱང་། ཤེར་ཕྱིན་ཇི་ལྟ་བར་རྟོགས་པ་ལ་བརྟེན་ནས་རྣམ་པར་རྒྱལ་བར་སྤྱོད་མ་ཞེས་བསྟན་པར་མཛད་པ་དང༌།
--- END BLOCKS ---
