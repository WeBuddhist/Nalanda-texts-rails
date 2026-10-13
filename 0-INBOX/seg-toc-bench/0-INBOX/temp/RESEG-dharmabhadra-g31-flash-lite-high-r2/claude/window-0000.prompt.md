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
༄༅། །སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་རྣམ་བཤད་ཡིད་འཕྲོག་ཨུཏྤལའི་ཆུན་པོ་ཞེས་བྱ་བ་བཞུགས་སོ། །

[Block 2 [HEADING]]
## མཆོད་བརྗོད། ^I-0

[Block 3]
ན་མོ་གུ་རུ་ཨཱརྱ་ཏྭ་རཱ་ཡེ། །

[Block 4 [VERSE]]
སྐུ་གསུམ་ཡེ་ཤེས་ལྔ་ལྡན་བླ་མ་དང༌། །
དབྱེར་མེད་རྒྱལ་ཡུམ་སྒྲོལ་མའི་ཞབས་བཏུད་ནས། །
དེ་ཡི་རྣམ་འགྱུར་གཅིག་ལྷག་བཅུ་ཕྲག་གཉིས། །
བསྟོད་པའི་རྒྱུད་དོན་མདོར་བསྡུས་བཤད་པར་བྱ། །

[Block 5 [HEADING]]
## དང་པོ་མདོར་བསྟན་པ། ^1-0

[Block 6]
དེ་ཡང་སྒྲོལ་མར་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་དོན་འཆད་པ་ལ་གསུམ། མདོར་བསྟན་པ། རྒྱས་པར་བཤད་པ། ཕན་ཡོན་བསྟན་པའོ། །དང་པོ་ནི།

[Block 7]
ཨོཾ་རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 8]
དོན་ནི། ཨོཾ་ནི་མཚམས་སྦྱོར་ཕྲལ་ན་ཡི་གེ་ཨ་ཨུ་མ་གསུམ་དུ་འགྱུར་བས། ཕྱག་ཡུལ་གྱི་སྐུ་གསུང་ཐུགས་གསུམ་མཚོན་ལ། རྒྱལ་བའི་ཡུམ་གྱི་མཆོག་ཏུ་གྱུར་ཅིང༌། སྡོམ་པ་གསུམ་དང་ལྡན་པས་ན་རྗེ་བཙུན་མ། འཁོར་འདས་ལ་མི་གནས་པས་ན་འཕགས་མ། སེམས་ཅན་ཐམས་ཅད་སྡུག་བསྔལ་ལས་སྐྱོབ་པས་ན་སྒྲོལ་མ་སྟེ། དེའི་ཞབས་ལ་ཕྱག་འཚལ་བ་ནི་སྒོ་གསུམ་གུས་པར་འདུད་པའོ། །

[Block 9 [HEADING]]
## གཉིས་པ་རྒྱས་པར་བཤད་པ། ^2-0

[Block 10 [HEADING]]
### དང་པོ་ལོ་རྒྱུས་ཀྱི་སྒོ་ནས་བསྟོད་པ། ^2-1-0

[Block 11]
གཉིས་པ་རྒྱས་པར་བཤད་པ་ལ་གསུམ། ལོ་རྒྱུས་ཀྱི་སྒོ་ནས་བསྟོད་པ། སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ། འཕྲིན་ལས་ཀྱི་སྒོ་ནས་བསྟོད་པའོ། །དང་པོ་ནི།

[Block 12 [VERSE]]
ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔལ་མོ། །
སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། །
འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི། །
གེ་སར་བྱེ་བ་ལས་ནི་བྱུང་མ། །

[Block 13]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་བ་སྟེ་གུས་པས་འདུད་དོ། །གང་ལ་འདུད་ཅེ་ན། སེམས་ཅན་འཁོར་བ་ལས་འདོན་པས་ན་སྒྲོལ་མ། དེ་ལ་རྒྱལ་བ་གཞན་ལས་འཕྲིན་ལས་མྱུར་བས་ན་མྱུར་མ། བདུད་སྡེ་ལྷག་མེད་དུ་འཇོམས་པས་ན་དཔལ་མོ། ཡེ་ཤེས་ཀྱི་སྤྱན་ནི་སྐད་ཅིག་གི་གློག་འཁྱུག་པ་དང་འདྲ་བར་ཤེས་བྱ་མཐའ་དག་སྐད་ཅིག་ལ་གཟིགས་མ། ས་འོག་ཀླུའི་འཇིག་རྟེན། ས་སྟེང་མིའི་འཇིག་རྟེན། ས་བླ་ལྷའི་འཇིག་རྟེན་གསུམ་གྱི་མགོན་སྐྱབས་ནི་འཕགས་པ་སྤྱན་རས་གཟིགས་ཡིན་ལ། དེའི་ཞལ་གྱི་དཀྱིལ་འཁོར་ལ་གནས་པའི་སྤྱན་ཆབ་ལས་སྐྱེས་པའི་མེ་ཏོག་པདྨའི་གེ་སར་ཁ་བྱེ་བ་ལས་བྱུང་བའི་ལོ་རྒྱུས་དང་ལྡན་མ་དེ་ལ་འདུད་པ་སྟེ། ལོ་ཆེན་ནམ་བཟང་གིས། ཚིག་རྐང་གསུམ་པར། འཇིག་རྟེན་གསུམ་མགོན་ཞལ་གྱི་ཆུ་སྐྱེས་ཞེས་འགྱུར་བཅོས་མཛད་པ་ལྟར་བདེ་བས་དེ་བཞིན་དུ་བཤད་དོ། །

[Block 14 [HEADING]]
### གཉིས་པ་སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-0

[Block 15 [HEADING]]
#### དང་པོ་ལོངས་སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-0

[Block 16 [HEADING]]
##### དང་པོ་ཞི་བའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-1-0

[Block 17 [HEADING]]
###### དང་པོ་ཞལ་མདངས་གསལ་ཞིང་འོད་ཟེར་འཕྲོ་བའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-1-1-0

[Block 18]
གཉིས་པ་སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ་ལ་གཉིས། ལོངས་སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ་དང༌། ཆོས་སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པའོ། །དང་པོ་ལ་གཉིས། ཞི་བའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ་དང༌། ཁྲོ་མོའི་རྣམ་པ་སྒོ་ནས་བསྟོད་པའོ། །དང་པོ་ལ་དྲུག ། ཞལ་མདངས་གསལ་ཞིང་འོད་ཟེར་འཕྲོ་བའི་སྒོ་ནས་བསྟོད་པ། སྐུ་མདོག་དང་ཕྱག་མཚན་དང་རྒྱུའི་སྒོ་ནས་བསྟོད་པ། རྒྱལ་བ་དང་རྒྱལ་སྲས་ཀྱིས་གུས་པར་བསྟན་པའི་སྒོ་ནས་བསྟོད་པ། མི་མཐུན་ཕྱོགས་གནོན་པའི་སྒོ་ནས་བསྟོད་པ། འཇིག་རྟེན་པའི་ལྷ་ཆེན་པོ་རྣམས་ཀྱིས་བཀུར་བའི་སྒོ་ནས་བསྟོད་པ། ཕ་རོལ་འཇོམས་པའི་སྒོ་ནས་བསྟོད་པའོ། །དང་པོ་ནི།

[Block 19 [VERSE]]
ཕྱག་འཚལ་སྟོན་ཀའི་ཟླ་བ་ཀུན་ཏུ། །
གང་བ་བརྒྱ་ནི་བརྩེགས་པའི་ཞལ་མ། །
སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས། །
རབ་ཏུ་ཕྱེ་བའི་འོད་རབ་འབར་མ། །

[Block 20]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། རྡུལ་སྤྲིན་ལུག་རྣ་སོགས་དང་བྲལ་བའི་སྟོན་ཀའི་དུས་ཀྱི་ཟླ་བ་སྐྱེ་འཕྲོ་རྫོགས་ཤིང་འབྲི་བའི་འགོ་མ་ཚུགས་པའི་ཉ་ཀུན་ཏུ་གང་བ་གྲངས་བརྒྱ་ཐམ་པ་ནི། ཕྱོགས་གཅིག་ཏུ་བརྩེགས་པ་སྟེ་སྤུངས་པ་ལྟ་བུར་མཆོག་ཏུ་དཀར་ཞིང་མཛེས་པའི་ཞལ་རས་དང་ལྡན་མ། ཞལ་དེ་ལས་སྐར་མ་སྟོང་ཕྲག་དུ་མ་ཕྱོགས་གཅིག་ཏུ་ཚོགས་པ་ལྟ་བུའི་འོད་ཟེར་རྣམས་ཀྱི་རབ་ཏུ་ཕྱེ་ཞིང་གསལ་བར་བྱས་པ་དང་འདྲ་བའི་འོད་ཟེར་དཀར་པོར་རབ་ཏུ་འབར་ཞིང་འཕྲོ་མ་དེ་ལའོ། །

[Block 21 [HEADING]]
###### གཉིས་པ་སྐུ་མདོག་དང་ཕྱག་མཚན་དང་རྒྱུའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-1-2-0

[Block 22]
གཉིས་པ་སྐུ་མདོག་དང་ཕྱག་མཚན་དང་རྒྱུའི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 23 [VERSE]]
ཕྱག་འཚལ་གསེར་སྔོ་ཆུ་ནས་སྐྱེས་ཀྱི། །
པདྨས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་མ། །
སྦྱིན་པ་བརྩོན་འགྲུས་དཀའ་ཐུབ་ཞི་བ། །
བཟོད་པ་བསམ་གཏན་སྤྱོད་ཡུལ་ཉིད་མ། །

[Block 24]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། སྐུ་མདོག་འཛམ་བུ་ཆུ་བོའི་གསེར་ལྟར་མཛེས་ཤིང་ཅུང་ཟད་སྔོ་བའི་རྣམ་པ་ཅན། ཆུ་ནང་ནས་སྐྱེས་པའི་པདྨ་སྟེ་ཨཏྤལའི་ཡུ་བས་ཕྱག་གཡོན་གྱི་མཐེབ་སྲིན་ནི་རྣམ་པར་བརྒྱན་ཅིང་འདབ་མ་སྙན་ཐད་དུ་ཁ་བྱེ་བས་མཚན་མ། རྒྱུ་སྦྱིན་པ་དང་། བརྩོན་འགྲུས་དང་། བསྲུང་དཀའ་བ་ཐུབ་པའི་ཚུལ་ཁྲིམས་དང༌། རྨོངས་པའི་མུན་པ་ཞི་བའི་ཤེས་རབ་དང༌། བཟོད་པ་དང་། བསམ་གཏན་ཏེ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་མངོན་སུམ་གྱི་སྤྱོད་ཡུལ་དུ་བྱས་པ་ཉིད་ལས་བྱུང་མ་དེ་ལའོ། །

[Block 25 [HEADING]]
###### གསུམ་པ་རྒྱལ་བ་དང་རྒྱལ་སྲས་ཀྱིས་གུས་པས་བསྟེན་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-1-3-0

[Block 26]
གསུམ་པ་རྒྱལ་བ་དང་རྒྱལ་སྲས་ཀྱིས་གུས་པས་བསྟེན་པའི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 27 [VERSE]]
ཕྱག་འཚལ་དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར། །
མཐའ་ཡས་རྣམ་པར་རྒྱལ་བར་སྤྱོད་མ། །
མ་ལུས་ཕ་རོལ་ཕྱིན་པ་ཐོབ་པའི། །
རྒྱལ་བའི་སྲས་ཀྱིས་ཤིན་ཏུ་བསྟེན་མ། །

[Block 28]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ཡུམ་ཡིན་པས་དེ་རྣམས་ཀྱི་དབུའི་གཙུག་ཏོར་གྱི་རྩེ་ན། མི་མཐུན་ཕྱོགས་མཐའ་ཡས་པ་ལས་རྣམ་པར་རྒྱལ་བའི་ཚུལ་དུ་སྤྱོད་ཅིང་བཞུགས་མ། ས་བཅུ་མ་ལུས་པའི་ངོ་བོ་ཕ་རོལ་དུ་ཕྱིན་པ་བཅུ་ཐོབ་པའི་རྒྱལ་བའི་སྲས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་ཤིན་ཏུ་གུས་པའིགཙུག་གིས་བསྟེན་མ་དེ་ལའོ། །

[Block 29 [HEADING]]
###### བཞི་པ་མི་མཐུན་ཕྱོགས་གནོན་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-1-4-0

[Block 30]
བཞི་པ་མི་མཐུན་ཕྱོགས་གནོན་པའི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 31 [VERSE]]
ཕྱག་འཚལ་ཏུཏྟཱ་ར་ཧཱུཾ་ཡི་གེས། །
འདོད་དང་ཕྱོགས་དང་ནམ་མཁའ་གང་མ། །
འཇིག་རྟེན་བདུན་པོ་ཞབས་ཀྱིས་མནན་ཏེ། །
ལུས་པ་མེད་པར་འགུགས་པར་ནུས་མ། །

[Block 32]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། གསུང་ཏུཏྟཱ་ར་ཞེས་སོགས་སྔགས་འཕྲེང་ལས་འཕྲོས་པའི་འོད་ཟེར་དང་། ཐུགས་སྟོང་ཉིད་སྙིང་རྗེ་མཚོན་པའི་ཧཾ་གི་ཡི་གེའི་སྒྲ་སྐད་ཀྱིས། དམྱལ་བ། ཡི་དྭགས། དུད་འགྲོ། མི། །ལྷ་སྟེ་འདོད་ཁམས་ཀྱི་འགྲོ་བ་རྒྱུད་ལྔ་དང༌། ཕྱོགས་ཏེ་གཟུགས་ཁམས་དང༌། །ནམ་མཁའ་སྟེ་གཟུགས་མེད་ཁམས་པའི་གནས་གཉིས་ཏེ་བདུན་གང་བར་མཛད་མ། དེ་ལྟ་བུའི་འཇིག་རྟེན་གྱི་ཁམས་བདུན་པོ་དེ་རྣམས་འོད་དང་སྒྲས་གང་བར་མ་ཟད་སྐུའི་ཞབས་ཀྱིས་ཀྱང་མནན་པ་སྟེ་བཅགས་ཏེ། དེར་གནས་པའི་འགྲོ་བ་གཅིག་ཀྱང་ལུས་པ་མེད་པར་དབང་དུ་འགུགས་པར་ནུས་པའི་མཐུ་དང་ལྡན་མ་དེ་ལའོ། །

[Block 33 [HEADING]]
###### ལྔ་པ་འཇིག་རྟེན་པའི་ལྷ་ཆེན་པོ་རྣམས་ཀྱིས་བཀུར་བའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-1-5-0

[Block 34]
ལྔ་པ་འཇིག་རྟེན་པའི་ལྷ་ཆེན་པོ་རྣམས་ཀྱིས་བཀུར་བའི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 35 [VERSE]]
ཕྱག་འཚལ་བརྒྱ་བྱིན་མེ་ལྷ་ཚངས་པ། །
རླུང་ལྷ་སྣ་ཚོགས་དབང་ཕྱུག་མཆོད་མ། །
འབྱུང་པོ་རོ་ལངས་དྲི་ཟ་རྣམས་དང་། །
གནོད་སྦྱིན་ཚོགས་ཀྱིས་མདུན་ནས་བསྟོད་མ། །

[Block 36]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། ཤར་གྱི་ཕྱོགས་སྐྱོང་བརྒྱ་བྱིན་དང༌། ཤར་ལྷོའི་མེ་ལྷ་དང༌། སྟེང་གི་ཚངས་པ་དང་། ནུབ་བྱུང་གི་རླུང་ལྷ་དང༌། དེ་དག་གིས་མཚོན་པའི་གཤིན་རྗེ་དང་ཀླུ་སོགས་སྡེ་རིས་སྣ་ཚོགས་ཀྱི་དབང་ཕྱུག་སྟེ་གཙོ་བོ་རྣམས་ཀྱིས་གུས་པས་མཆོད་པའི་གནས་སུ་གྱུར་མ། དབང་ལྡན་གྱི་འཁོར་འབྱུང་པོ་རྣམས་དང༌། སྲིན་པོའི་འཁོར་རོ་ལངས་རྣམས་དང༌། བརྒྱ་བྱིན་གྱི་འཁོར་དྲི་ཟ་རྣམས་དང༌། ལུས་ངན་གྱི་འཁོར་གནོད་སྦྱིན་སོགས་འཁོར་གྱི་ཚོགས་རྣམས་ཀྱིས་ཀྱང་སྐུ་མདུན་དུ་བཏུད་ནས་གུས་པས་བསྟོད་པའི་ཡུལ་དུ་གྱུར་མ་དེ་ལའོ། །

[Block 37 [HEADING]]
###### དྲུག་པ་ཕ་རོལ་འཇོམས་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-1-6-0

[Block 38]
དྲུག་པ་ཕ་རོལ་འཇོམས་པའི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 39 [VERSE]]
ཕྱག་འཚལ་ཏྲཊ་ཅེས་བྱ་དང་ཕཊ་ཀྱིས། །
ཕ་རོལ་འཁྲུལ་འཁོར་རབ་ཏུ་འཇོམས་མ། །
གཡས་བསྐུམས་གཡོན་བརྐྱངས་ཞབས་ཀྱིས་མནན་ཏེ། །
མེ་འབར་འཁྲུག་པ་ཤིན་ཏུ་འབར་མ། །

[Block 40]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། ཞལ་ནས་ཏྲཊ་(འདྲལ་བ་སྟེ་འཇོམས་པའོ)ཅེས་བྱ་བ་དང་ཕཊ་(འགས་པ་)ཅེས་བྱ་བའི་རིག་སྔགས་ཀྱི་ང་རོ་བསྒྲགས་པ་ཙམ་གྱིས་ཕ་རོལ་བྱད་མས་བསམ་སྦྱོར་ངན་པས་བྱས་པའི་འཁྲུལ་འཁོར་གྱི་ནུས་པ་ཐམས་ཅད་སྐད་ཅིག་ལ་རབ་ཏུ་འཇོམས་པར་མཛད་མ། གཡས་བསྐུམས་ཤིང་གཡོན་བརྐྱངས་པ་སྟོང་ཉིད་སྙིང་རྗེ་མཚོན་པའི་ཞབས་ཀྱི་འོག་ཏུ་བྱད་མ་དང་རྦད་འདྲེ་ལ་སོགས་པ་མནན་ཏེ། སྐུ་ལས་ཡེ་ཤེས་ཀྱི་མེ་འབར་ཞིང་འཁྲུག་པ་དང༌། ཤིན་ཏུ་འབར་བས་ཐལ་བ་ཙམ་ཡང་མ་ལུས་པར་སྲེག་པར་མཛད་མ་དེ་ལའོ། །
--- END BLOCKS ---
