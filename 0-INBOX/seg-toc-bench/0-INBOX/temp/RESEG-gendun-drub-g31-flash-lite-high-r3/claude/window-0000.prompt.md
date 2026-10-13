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
༄༅། །སྒྲོལ་མ་ཕྱག་འཚལ་ཉེར་གཅིག་གི་ཊཱིཀྐ་རིན་པོ་ཆེའི་ཕྲེང་བ་བཞུགས་སོ། །

[Block 2 [HEADING]]
## མཆོད་བརྗོད། ^I-0

[Block 3 [VERSE]]
འཕགས་པ་དཀོན་མཆོག་གསུམ་ལ་ཕྱག་འཚལ་ལོ། །
དུས་གསུམ་སངས་རྒྱས་ཀུན་གྱི་འཕྲིན་ལས་མ། །
རྒྱལ་བའི་ཡུམ་གྱུར་བཅོམ་ལྡན་སྒྲོལ་མ་ལ། །
ལུས་ངག་ཡིད་གསུམ་གུས་པས་ཕྱག་འཚལ་ལོ། །

[Block 4]
ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་རྣམ་སྣང་གིས་གསུངས་པའི་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་མ། ཇི་ལྟར་ནུས་ཤིང་འབྱེད་ལ་ཤིན་ཏུ་མཁས།

[Block 5 [HEADING]]
## རྒྱུད་ཀྱི་ཁུངས་བསྟན་པ། ^II-0

[Block 6]
དེ་ལ་རྒྱུད་འདི་སྔོན་གྱི་མཁས་པ་ཕལ་ཆེ་བ་ནི། རྒྱུད་སྡེ་བཞིའི་ནང་ནས་བྱ་རྒྱུད་དུ་གཏོགས་ཞེས་གསུང་ངོ། །

[Block 7]
དེ་ཡང་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ཡུམ་སྒྲོལ་མ་ལ་བསྟོད་པ་ཞེས་བྱ་བའི་རྒྱུད་ལེའུ་སུམ་ཅུ་རྩ་ལྔ་ཡོད་པའི་ལེའུ་གསུམ་པ་ལ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་མ་འདི་གསུངས་སོ། །

[Block 8]
འདི་བྱ་རྒྱུད་ཡིན་མིན་བརྟག་སྟེ། ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་མ་འདི། བླ་མེད་རྒྱུད་དུ་བཀྲལ་བའང་འདུག་གསུང་ངོ་། །

[Block 9 [HEADING]]
## དང་པོ་གླེང་གཞི། ^1-0

[Block 10]
འདི་ལ་གཉིས། གླེང་གཞི་དང་། དངོས་བཤད་པའོ། །དང་པོ་ནི། དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་ལ་བཀའ་སྩལ་བ། འཇམ་དཔལ་ཡུམ་འདི་ནི་དུས་གསུམ་གྱི་སངས་རྒྱས་ཐམས་ཅད་ཀྱི་ཡུམ་མོ། །

[Block 11]
འཇམ་དཔལ་དེའི་ཕྱིར། དུས་གསུམ་གྱི་སངས་རྒྱས་ཐམས་ཅད་ཀྱིས་བསྟོད་པ་འདི། འཇམ་དཔལ་ཁྱོད་ཀྱི་ཡིད་ལ་གྱིས་ཤིག །དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བསྟོད་པའི་གཟུངས་སྔགས་གསུངས་པ་ཞེས་སོ། །

[Block 12 [HEADING]]
## གཉིས་པ་དངོས་བཤད་པ། ^2-0

[Block 13 [HEADING]]
### དང་པོ་མདོར་བསྟན་པ། ^2-1-0

[Block 14]
གཉིས་པ་ལ། རྩ་བའི་སྔགས་ཀྱིས་བསྟོད་པ་འདི་དང་། །ཕྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག །ཅེས་གཉིས་སུ་ཕྱེ་བའི། རྩ་བའི་སྔགས་ཀྱིས་བསྟོད་པ་ནི། ན་མ་སརྦ་ཏཱ་ཐཱ་ག་ཏཱ་ནཱཾ། ཏདྱ་ཐཱ། ཨོཾ་ན་མོ་སུ་ཀ་ས་ན་མ་ཏཱ་རེ་པཱ་ར་མི་ཏ་ཞེས་པ་འདི་ཡིན་ཞེས་འགའ་ཞིག་གསུང་ལ། སྤང་ལོ་ཆེན་པོ་ནི། ཨོཾ། ཕྱག་འཚལ་སྒྲོལ་མ་ཏཱ་རེ་དཔའ་མོ། །ཏུཏྟཱ་ར་ཡིས་འཇིགས་པ་ཀུན་སེལ། །ཏུ་རེས་དོན་རྣམས་ཐམས་ཅད་རབ་སྟེར། །སྭཱཧཱ་ཡི་གེར་བཅས་ལ་རབ་འདུད། །ཅེས་པ་རྒྱ་དཔེ་ལ་ཡོད་པ་སྤང་ལོས་བསྒྱུར་བ་འདི་ཡིན་གསུང་ཡང་། རྩ་བའི་སྔགས་ཀྱིས་བསྟོད་པ་ནི། འདིར་བསྟན་སྔགས་དང་སྤེལ་བའི་བསྟོད་ཚིག་ཉི་ཤུ་པོ་འདི་ཡིན་ལ། ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་ནི། དེ་སྤེལ་བའི་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་པོ་འདི་ཡིན་ཞེས་བླ་མ་རྣམས་གསུང་ངོ་། ། དེས་ན། མདོར་བསྟན་པ། རྒྱས་པར་བཤད་པ། ཕན་ཡོན་བསྟན་པ་དང་གསུམ། དང་པོ་ནི། ཨོཾ་རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ལོ། ། ཞེས་པ་འདི་ཡིན་པས། ཨོཾ་ཞེས་པ་ནི། སྐྱབས་སུ་འགྲོ་བའམ། མཆོད་པ་འབུལ་བའམ། མ་དག་པ་སྦྱོང་བའོ། །

[Block 15]
རྗེ་བཙུན་མ་ཞེས་པ་ལ། རྗེ་ནི། དུས་གསུམ་གྱི་སངས་རྒྱས་ཐམས་ཅད་བསྐྱེད་པའི་ཡུམ་གྱི་ནང་ནས་མཆོག་ཏུ་གྱུར་པའོ། །

[Block 16]
བཙུན་ཞེས་པ་ནི། ཕྱི་ལྟར་ན་སོ་ཐར། ནང་ལྟར་ན་བྱང་སེམས། གསང་བ་ལྟར་ན་སྔགས་ཀྱི་སྡོམ་པ་དང་ལྡན་པའོ། །

[Block 17]
འཕགས་མ་ནི། མཐོང་སྤངས་མི་དགེ་བ་ལས་རིང་དུ་སོང་ཞིང་འཁོར་འདས་ལས་འཕགས་པའོ། །

[Block 18]
སྒྲོལ་མ་ནི། སྡུག་བསྔལ་གྱི་རྒྱ་མཚོ་ལས་སྒྲོལ་བའོ། །

[Block 19]
མ་ཞེས་པ་ནི། སེམས་ཅན་ཐམས་ཅད་ལ་ཉེ་རིང་མེད་པར་འགྲོ་དོན་མཉམ་དུ་མཛད་པའོ། །

[Block 20]
ཕྱག་ཅེས་པ་ནི། ལས་ཉོན་གྱི་སྡིག་(སྒྲིབས་,སྒྲིབ་)འཕྱག་པར་བྱེད་པའོ། །

[Block 21]
འཚལ་ཞེས་པ་ནི། ལུས་ངག་ཡིད་གསུམ་གུས་པར་བགྱིད་ཅེས་པའི་དོན་ཏོ། །

[Block 22 [HEADING]]
### གཉིས་པ་རྒྱས་པར་བཤད་པ། ^2-2-0

[Block 23 [HEADING]]
#### དང་པོ་ལོ་རྒྱུས་ཀྱི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-0

[Block 24]
གཉིས་པ་ལ། ལོ་རྒྱུས་ཀྱི་སྒོ་ནས་བསྟོད་པ་དང་། སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ། འཕྲིན་ལས་ཀྱི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ་དང་གསུམ། དང་པོ་ནི། ཕྱག་འཚལ་སྒྲོལ་མ་མྱུར་མ་དཔའ་མོ། །སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། །འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི། །གེ་སར་བྱེ་བ་ལས་ནི་བྱུང་མ། །ཕྱག་འཚལ་ལོ་ཞེས་དྲང་ངོ། །གང་ལ་ན། སྒྲོལ་མ་ལའོ། །

[Block 25]
དེ་གང་ལས་བྱུང་ན། སྐད་གཅིག་གིས་འཇིགས་པའི་ཕུང་པོ་ལྔའམ། བཞི་ལ་བརྟེན་པའི་འདོད་པ་དང་། གཟུགས་དང་། གཟུགས་མེད་པའི་ཁམས་གསུམ་གྱི་མགོན་སྐྱབས་འཕགས་པ་འཇིག་རྟེན་དབང་ཕྱུག་གིས་འགྲོ་བ་ཇི་སྙེད་ཅིག་འཁོར་བ་ལས་བཏོན་ཀྱང་། ཉུང་དུ་མ་སོང་བར་གཟིགས་ནས། བཤུམས་པའི་སྤྱན་ཆབ་ཀྱི་ཆུ་ལས་སྐྱེས་པའི་ཨུཏྤ་ལའི་ཞལ་གྱི་གེ་སར་བྱེ་བ་ལས་བྱུང་བའོ། །

[Block 26]
དེས་སེམས་ཅན་གྱི་དོན་གྱི་མྱུར་བ་ནི། མྱུར་དུ་དེ་དག་འཁོར་བ་ལས་སྒྲོལ་བའི་ཞབས་ཏོག་བགྱིད་ལགས་ཀྱིས། སྤྱན་ཆབ་མི་གཏོང་བར་ཞུ། ཞུས་ནས་འཁོར་བའི་གཡུལ་ངོ་ཟློག་པ་ལ་དཔའ་མོའོ། །

[Block 27]
དེ་བས་ན། དེའི་སྤྱན་ཆབ་གཉིས་སྐད་ཅིག་གིས་གསལ་བའི་གློག་དང་འདྲ་བས་འཇིག་རྟེན་གསུམ་ལ་གཟིགས་པའོ། །

[Block 28]
འདི་ལ་པཎ་ཆེན་ཉི་མ་སྦས་པས། རབ་ཏུ་དཔའ་བའི་སྒྲོལ་མ་ཞེས་གསུངས་སོ། །

[Block 29 [HEADING]]
#### གཉིས་པ་སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-2-0

[Block 30 [HEADING]]
##### དང་པོ་ལོངས་སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-2-1-0

[Block 31 [HEADING]]
###### དང་པོ་ཞི་བའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-2-1-1-0

[Block 32]
གཉིས་པ་ལ། ལོངས་སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ་དང་། ཆོས་སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ་གཉིས། དང་པོ་ལ། ཞི་བའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ་དང་། ཁྲོ་མོའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ་གཉིས། དང་པོ་ལ། ཕྱག་འཚལ་དྲུག་ཡོད་པའི།

[Block 33 [HEADING]]
###### **དང་པོ་ཞལ་མདངས་གསལ་ཞིང་འོད་ཟེར་འཕྲོ་བའི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-1-1-0

[Block 34]
དང་པོ་ཞལ་མདངས་གསལ་ཞིང་འོད་ཟེར་འཕྲོ་བའི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་སྟོན་ཀའི་ཟླ་བ་ཀུན་ཏུ། །གང་བ་བརྒྱ་ནི་བརྩེགས་པའི་ཞལ་མ། །ཞེས་སོགས་ཏེ། སྤྲིན་དང་། (ཁུག་,ཁུ་)རྣ་སོགས་ཀྱི་སྒོ་ནས་རྡུལ་དང་བྲལ་བའི། སྟོན་ཀའི་ཟླ་བ་ཀུན་ཏུ་གང་བ། ཞེས་པ་སྐྱེ་འཕྲོ་རྫོགས་ཤིང་འབྲི་བའི་མགོ་མ་ཚུགས་པའི་ཉ་གང་བའི་ཟླ་བའོ། །

[Block 35]
དེ་འདྲ་བརྒྱ་ནི་བརྩེགས་པ་བས་ཏེ། བརྒྱ་སྤུངས་པ་ལས་ཀྱང་འོད་ཕྱེ་བའི་ཞལ་དང་ལྡན་མ། ཞལ་དེ་ནས་སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་བས་ཀྱང་རབ་ཏུ་ཕྱེ་བའི་འོད་རབ་འབར་མའོ། །

[Block 36]
ཡང་ན། བརྒྱད་གཉིས་པ་སྒྲིགས་ཞེས་འདོན་པ་ལྟར་ན། ཞལ་གྱི་ནང་ན་ཟླ་བ་ལྟ་བུའི་ཚེམས་བརྒྱད་གཉིས་བཅུ་དྲུག་བསྒྲིགས་པའི་ཞལ་རས་ལ་སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་བས་ཀྱང་ལྷག་པའི་འོད་འཕྲོ་ཞེས་པ་དང་། བརྒྱད་པོ་དེ་གཉིས་བསྒྲིགས་ཞེས་པས། མཚན་བཟང་པོ་སོ་གཉིས་མཚོན་པའོ། །

[Block 37]
འདི་ལ་དཀར་མོ་མདངས་ལྡན་སྒྲོལ་མ་ཞེས་བཤད་དོ། །

[Block 38 [HEADING]]
###### **གཉིས་པ་སྐུ་མདོག་དང་ཕྱག་མཚན་དང་རྒྱུའི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-1-2-0

[Block 39]
གཉིས་པ་སྐུ་མདོག་དང་། ཕྱག་མཚན་དང་། རྒྱུའི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་སེར་སྔོ་ཆུ་ནས་སྐྱེས་ཀྱི། །པདྨས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་མ། །ཞེས་སོགས་ཏེ། སྔོ་བ་ནི། སྐུ་མདོག །སེར་ནི། ཁ་དོག་དྭངས་པ་མཚོན་པ་སྟེ། གསེར་མདོག་ཅན་གྱི་སྒྲོལ་མ་ཞེས་འབྱུང་བས་སོ། །

[Block 40]
དེའི་ཕྱག་གཡོན་གྱི་སྲིན་ལག་གིས་ཆུ་ནས་སྐྱེས་པའི་པདྨ་སྟེ་ཨུཏྤ་ལས་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་པ་སྟེ། བཟུངས་ནས་སྙན་གྱི་ཐད་ཀར་ཁ་བྱེ་བ་ནི། ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་དག་པའི་རྟགས་སོ། །
--- END BLOCKS ---
