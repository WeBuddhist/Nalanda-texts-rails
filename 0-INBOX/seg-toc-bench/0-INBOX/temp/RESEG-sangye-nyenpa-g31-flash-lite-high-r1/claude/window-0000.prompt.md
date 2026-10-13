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
༄༅། །རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ཉི་ཤུ་རྩ་གཅིག་གི་ཚིག་འགྲེལ་དང་དམིགས་རིམ་ཉུང་ངུར་བཀོད་པ་འཕགས་མའི་བྱིན་རླབས་གྲུ་ཆར་བཞུགས། །

[Block 2 [HEADING]]
## མཆོད་བརྗོད། ^I-0

[Block 3 [VERSE]]
ཡེ་ཤེས་ལང་ཚོས་གང་བའི་རྗེ་བཙུན་མ། །
ཁྱེད་ཞབས་དྲན་ཙམ་གྱིས་ཀྱང་དུཿཁའི་འགྲོ། །
སྡུག་བསྔལ་རྒྱུ་བཅས་མིང་གི་ལྷག་མ་རུ། །
བགྱིད་མཛད་གང་ཁྱེད་ཚེ་རབས་གཏན་གྱི་སྐྱབས། །

[Block 4]
ཞེས་མཆོད་པར་བརྗོད་པར་སྔོན་དུ་སོང་ནས། འཆད་བྱའི་གཞུང་ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་ཚིག་འགྲེལ་དང་། དེ་དག་གི་དམིགས་རིམ་བཅས། དེང་དུས་ཀྱི་ལེ་ལོ་དང་རྣམ་གཡེང་ཅན་རྣམས་ཀྱི་ཁམས་དང་འཚམས་པར་ཉུང་ངུའི་ངག་གིས་འགྲེལ་བ་ལ།

[Block 5 [HEADING]]
## ཕྱག་འཚལ་སྒྲོལ་མ་ཉེར་གཅིག་གི་ཚིག་འགྲེལ་དང་དམིགས་རིམ། ^II-0

[Block 6]
དང་པོ། ཨོཾ་རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ལ་འཚལ་ལོ། ། ཞེས་པ་ལ། ༀ་ནི། འཕགས་མ་སྒྲོལ་མའི་སྐུ་གསུང་ཐུགས་ཀྱི་རྡོ་རྗེ་གསུམ་མཚོན། དམིགས་པ་མེད་པའི་ཐུགས་རྗེས་རྟག་ཏུ་སྐྱོང་ཞིང་ཉེས་རྩུབ་ཐམས་ཅད་སྤངས་པས་རྗེ་བཙུན་མ། སྲིད་དང་ཞི་བའི་མཐའ་ལས་ཤིན་ཏུ་འདས་པས་འཕགས་མ། འགྲོ་རྣམས་འཇིགས་པ་ཆེན་པོ་བརྒྱད་དང་བཅུ་དྲུག་ལས་སྒྲོལ་བས་སྒྲོལ་མ་སྟེ་ཡོན་ཏན་དེ་རྣམས་དང་ལྡན་པས་འཕགས་མ་ཁྱེད་ལ་རབ་ཏུ་དད་པས་ཕྱག་འཚལ་ལོ། །

[Block 7 [HEADING]]
### ཕྱག་འཚལ་དང་པོ། ^1-2-0

[Block 8 [HEADING]]
#### ཚིག་འགྲེལ། ^1-2-1-0

[Block 9 [VERSE]]
ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ། །
སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། །
འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི། །
གེ་སར་བྱེ་བ་ལས་ནི་བྱུང་མ། །

[Block 10]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། རྒྱལ་ཀུན་ཕྲིན་ལས་ཀྱི་བདག་ཉིད། སྲིད་པའི་ལས་ཉོན་དང་དེའི་འབྲས་བུ་ཚད་མེད་པའི་བརྩེ་བ་ཆེན་པོས་བཅས་ལས་སྒྲོལ་བར་མཛད་མ། འགྲོ་ཀུན་ཕན་བདེར་སྦྱོར་བ་ལ་ནམ་དུའང་གཡེལ་བ་མེད་པས་མྱུར་མ། དེ་དག་ཇི་བཞིན་མཛད་པ་ལ་ནུས་མཐུ་ཐོགས་པ་མེད་པས་དཔའ་མོ། གནས་ལུགས་གཟིགས་པའི་ཡེ་ཤེས་ཀྱི་སྤྱན་ནི། དུས་སྐད་ཅིག་གཅིག་གིས་གློག་དང་འདྲ་བར་ཆགས་ཐོགས་དང་བྲལ་བར་གཟིགས་པས་ཡེ་ཤེས་ཅན་མ། ས་འོག་ས་སྟེང་ས་བླ་སྟེ་འཇིག་རྟེན་གསུམ་གྱི་མགོན་པོ་འཕགས་པ་སྤྱན་རས་གཟིགས་ཀྱི་ཡིད་འོང་མཛེས་པའི་ཆུ་སྐྱེས་མེ་ཏོག་ལྟ་བུའི་ཞལ་གྱི་པདྨའི་སྤྱན་ཟུང་གེ་སར་ཟེའུ་འབྲུ་ལྟར་དུ་བྱེ་བ་ལས་ནི་སྙིང་རྗེ་ཆེན་པོའི་སྤྱན་ཆབ་ལས་བྱུང་བའི་འཕགས་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 11 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-2-2-0

[Block 12]
གསལ་འདེབས་ཚུལ་ནི། བྱང་ཆུབ་ཀྱི་སེམས་འཕེལ་ཞིང་སྣང་བ་དབང་དུ་སྡུད་པའི་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ་འདི་ཉིད་སྐུ་མདོག་དམར་མོ་ཁྲོ་འཛུམ་ཆགས་པའི་ཉམས་ཅན། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན། གཡོན་སྐྱབས་སྦྱིན་མཆོག་གསུམ་གྱི་རྒྱའི་མཐེབ་སྲིན་བར་ན་ཨུཏྤལ་རབ་ཏུ་རྒྱས་པའི་སྟེང་དུ་དུང་གཡས་འཁྱིལ་བྱང་ཆུབ་ཀྱི་སེམས་འཇིག་རྟེན་ཀུན་ན་ཁྱབ་པར་བསྒོམ་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 13 [HEADING]]
### ཕྱག་འཚལ་གཉིས་པ། ^1-3-0

[Block 14 [HEADING]]
#### ཚིག་འགྲེལ། ^1-3-1-0

[Block 15 [VERSE]]
ཕྱག་འཚལ་སྟོན་ཀའི་ཟླ་བ་ཀུན་ཏུ། །
གང་བ་བརྒྱ་ནི་བརྩེགས་པའི་ཞལ་མ། །
སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས། །
རབ་ཏུ་ཕྱེ་བའི་འོད་རབ་འབར་མ། །

[Block 16]
ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། ཤིན་ཏུ་དྭངས་པའི་སྟོན་ཀའི་དུས་ཀྱི་ཟླ་བ་ཀུན་ཏུ་ཉ་གང་བ། ཕྱོགས་གཅིག་ཏུ་དེ་དག་བརྒྱ་ཕྲག་རྣམས་ནི་བརྩེགས་པ་ལྟ་བུའི་དཀར་ལ་མཛེས་ཤིང་འོད་ཟེར་རབ་ཏུ་འཕྲོ་བའི་ཞལ་རས་དང་ལྡན་མ། མཁྱེན་གཉིས་ཀྱི་སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་ལྟ་བུ་རྣམས་ཀྱིས། རབ་ཏུ་སོ་སོར་ཕྱེ་བའི་སོ་སོ་ཡང་དག་རིག་པ་བཞིའི་བློ་གྲོས་ཀྱི་འོད་ཟེར་རབ་ཏུ་འབར་བའི་འཕགས་མ་སྒྲོལ་མ་དབྱངས་ཅན་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 17 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-3-2-0

[Block 18]
གསལ་འདེབས་ཚུལ་ནི། ཤེས་རབ་ཀྱི་སྟོབས་འཕེལ་ཞིང་བློ་གྲོས་རྒྱས་པར་བྱེད་པའི་སྒྲོལ་མ་བློ་གཏེར་དབྱངས་ཅན་འདི་ཉིད་སྐུ་མདོག་སྟོན་ཟླ་ལྟར་དཀར་བ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན་དང་། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་། མེ་ལོང་ལ་ས་བོན་ཧྲཱིཿ་གྱིས་མཚན་པ་ལས་འོད་འཕྲོས། འགྲོ་བའི་མ་རིག་པ་བསལ། ཇི་བཞིན་རྟོགས་པའི་བློ་གྲོས་ཀྱི་རྩལ་འབར་བའི་ཤེས་རབ་ཀྱི་གཏེར་ཕྱེ་བར་མཛད་པ་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 19 [HEADING]]
### ཕྱག་འཚལ་གསུམ་པ། ^1-4-0

[Block 20 [HEADING]]
#### ཚིག་འགྲེལ། ^1-4-1-0

[Block 21 [VERSE]]
ཕྱག་འཚལ་གསེར་སྔོ་ཆུ་ནས་སྐྱེས་ཀྱི། །
པདྨས་ཕྱག་ན་རྣམ་པར་བརྒྱན་མ། །
སྦྱིན་པ་བརྩོན་འགྲུས་དཀའ་ཐུབ་ཞི་བ།
བཟོད་པ་བསམ་གཏན་སྤྱོད་ཡུལ་ཉིད་མ། །

[Block 22]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། སྐུ་གསེར་གྱི་མདོག་ལྟར་སེར་ལ་ཨུཏྤལ་སྔོན་མོ་ཆུའི་ནང་ནས་སྐྱེས་ཀྱི་པདྨས་ཕྱག་གཡོན་ན་རྣམ་པར་བརྒྱན་ཏེ་འཛིན་མ་འཕགས་མ་ཁྱེད། ལམ་སྦྱིན་པ། བརྩོན་འགྲུས། དཀའ་ཐུབ་ཚུལ་ཁྲིམས། ཞི་བ་ཤེས་རབ། བཟོད་པ་དང་། དེ་བཞིན་བསམ་གཏན་བཅས་ཕར་ཕྱིན་དྲུག་གི་སྤྱོད་པ་དང་བཅས་ཏེ་ཡུལ་འགྲོ་བ་རྣམས་སྒྲོལ་ཞིང་འཇུག་པའི་བྱང་སེམས་སྤྱོད་པ་རྒྱ་མཚོར་དབང་བསྒྱུར་བར་ཉིད་མ་སྟེ་མཛད་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 23 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-4-2-0

[Block 24]
གསལ་འདེབས་ཚུལ་ནི། འཕགས་མ་སེར་མོ་བསོད་ནམས་མཆོག་སྟེར་འདི་ནི་སྐུ་མདོག་སེར་མོ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་ཡིད་བཞིན་གྱི་ནོར་བུ་དགོས་འདོད་ཀུན་སྩོལ་ལས་འོད་ཟེར་མཁའ་ཁྱབ་ཏུ་འཕྲོ་བར་བསྒོམ་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 25 [HEADING]]
### ཕྱག་འཚལ་བཞི་པ། ^1-5-0

[Block 26 [HEADING]]
#### ཚིག་འགྲེལ། ^1-5-1-0

[Block 27 [VERSE]]
ཕྱག་འཚལ་དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར། །
མཐའ་ཡས་རྣམ་པར་རྒྱལ་བར་སྤྱོད་མ། །
མ་ལུས་ཕ་རོལ་ཕྱིན་པ་ཐོབ་པའི། །
རྒྱལ་བ་སྲས་ཀྱིས་ཤིན་ཏུ་བསྟེན་མ། །

[Block 28]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར་ལས་སྤྲུལ་པ། སྲིད་པའི་སྐྱོན་མཐའ་ཡས་པ་ལས་རབ་ཏུ་རྣམ་པར་རྒྱལ་བར་སྤྱོད་པའི་ཕྲིན་ལས་ཅན་མ། སྤངས་རྟོགས་མ་ལུས་པ་ཡོངས་སུ་རྫོགས་པས་སྤང་བྱ་སྒྲིབ་པ་བཅུ་སྤངས་ཤིང་། ཡོན་ཏན་ཕ་རོལ་ཕྱིན་པ་བཅུ་ཐོབ་པའི་རྒྱལ་བ་སྲས་དང་བཅས་པ་རྣམས་ཀྱིས་ཤིན་ཏུ་གུས་པས་ཁྱེད་ཉིད་བསྟེན་པའི་འཕགས་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 29 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-5-2-0

[Block 30]
གསལ་འདེབས་ཚུལ་ནི། འཆི་མེད་ཚེ་སྒྲུབ་གཙུག་ཏོར་རྣམ་པར་རྒྱལ་མ་སྐུ་གསེར་མདོག པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་། འཆི་མེད་ཚེའི་བུམ་པ་ལས་འོད་ཟེར་འཕྲོས་ཏེ་འཁོར་འདས་ཀྱི་དྭངས་བཅུད་ཐམས་ཅད་བདུད་རྩིས་གང་བ་རང་གཞན་ལ་ཐིམ། འཆི་མེད་ཚེའི་དངོས་གྲུབ་ཐོབ་པར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 31 [HEADING]]
### ཕྱག་འཚལ་ལྔ་པ། ^1-6-0

[Block 32 [HEADING]]
#### ཚིག་འགྲེལ། ^1-6-1-0

[Block 33 [VERSE]]
ཕྱག་འཚལ་ཏུཏྟཱ་ར་ཧཱུཾ་ཡི་གེས། །
འདོད་དང་ཕྱོགས་དང་ནམ་མཁའ་གང་མ། །
འཇིག་རྟེན་བདུན་པོ་ཞབས་ཀྱིས་མནན་ཏེ། །
ལུས་པ་མེད་པར་འགུགས་པར་ནུས་མ། །

[Block 34]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། ཏུཏྟཱ་ར་ཡི་གཟུང་སྔགས་ལས་འོད་སྣ་ཚོགས་འབར་ཞིང་ལས་བཞི་ཐོགས་མེད་དུ་བསྒྲུབ་པའི་ཤེས་རབ་དང་། སྙིང་རྗེ་དབྱེར་མེད་ཀྱི་ངོ་བོ་ཧཱུཾ་གྱི་ཡི་གེའི་སྒྲས་འདོད་ཁམས་དང་། ཕྱོགས་བྲལ་ཏེ་གཟུགས་ཁམས་དང༌། ནམ་མཁའ་གཟུགས་མེད་ཁམས་ཀྱི་རྒྱ་ཁྱོན་གང་བར་མཛད་པའི་འཕགས་མ་གང་གིས། འཇིག་རྟེན་བདུན་ཏེ། ཀླུ། ཡི་དྭགས། ལྷ་མ་ཡིན། རིག་འཛིན། མི། མིའམ་ཅི། ལྷ་སྟེ་བདུན་པོ་ཞབས་ཀྱིས་མནན་པ་ལྟར་དབང་དུ་བསྡུས་ཏེ། གཞན་གཅིག་ཀྱང་ལུས་པ་མེད་པར་འགུགས་པར་ནུས་པའི་སྟོབས་དང་ལྡན་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 35 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-6-2-0

[Block 36]
གསལ་འདེབས་ཚུལ་ནི། དབང་དུ་སྡུད་པའི་རིག་བྱེད་ལྷ་མོ་འདི་ཉིད་སྐུ་མདོག་དམར་མོ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན་གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་མདའ་གཞུ་བཀང་བ་ལས་འོད་ཟེར་འཕྲོ་པ་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 37 [HEADING]]
### ཕྱག་འཚལ་དྲུག་པ། ^1-7-0

[Block 38 [HEADING]]
#### ཚིག་འགྲེལ། ^1-7-1-0

[Block 39 [VERSE]]
ཕྱག་འཚལ་བརྒྱ་བྱིན་མེ་ལྷ་ཚངས་པ། །
རླུང་ལྷ་སྣ་ཚོགས་དབང་ཕྱག་མཆོད་མ། །
འབྱུང་པོ་རོ་ལངས་དྲི་ཟ་རྣམས་དང་། །
གནོད་སྦྱིན་ཚོགས་ཀྱིས་མདུན་ནས་བསྟོད་མ། །

[Block 40]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། ཤར་གྱི་ལྷ་དབང་བརྒྱ་བྱིན། ཤར་ལྷོའི་དྲང་སྲོང་མེ་ལྷ། སྟེང་གི་ཚངས་པ། ནུབ་བྱང་གི་རླུང་ལྷ། ལྷོ་ཕྱོགས་ཀྱི་སྣ་ཚོགས་དབང་ཕྱག་སྟེ་གཤིན་རྗེ། གཞན་ཡང་ནུབ་ཕྱོགས་ཀྱི་ཀླུའི་དབང་པོ། འོག་ཕྱོགས་ཀྱི་ལྷ་བརྟན་མ། ས་འཛིན་ལག་པ་ཆེན་པོ་སོགས་ཀྱིས་གུས་པས་མཆོད་ཅིང་བསྟོད་པའི་གནས་སུ་བཞུགས་པ་ནི་འཕགས་མ་ཁྱེད་ཡིན་ལ། དེ་བཞིན་བྱང་ཤར་གྱི་བགེགས་སོགས་འབྱུང་པོ་དང༌། ལྷོ་ནུབ་ཏུ་རོ་ལངས་ཏེ་བདེན་དང་བྲལ་བ་ལེགས་ལྡན། ཤར་ཕྱོགས་སུ་བརྒྱ་བྱིན་གྱི་འཁོར་དྲི་ཟ་རྣམས་དང༌། བྱང་ཕྱོགས་སུ་གནོད་སྦྱིན་རྣམ་ཐོས་སྲས་སོགས་ནོར་བདག་ཚོགས་ཀྱིས། སྲིད་འདིར་ཆེ་བར་སྒྲོགས་པ་རྣམས་ཀྱིས་ཀྱང་ཁྱེད་ཀྱི་མདུན་དུ་གུས་པས་འཁོད་ནས་བསྟོད་པའི་ཡུལ་སྒྲོལ་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །
--- END BLOCKS ---
