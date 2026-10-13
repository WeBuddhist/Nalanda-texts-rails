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
[Block 71 [HEADING]]
###### **བཞི་པ་ཕྱོགས་སྐྱོང་བཅུས་འཕྲིན་ལས་སྒྲུབ་པའི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-2-4-0

[Block 72]
བཞི་པ་ཕྱོགས་སྐྱོང་བཅུས་འཕྲིན་ལས་སྒྲུབ་པའི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་ས་གཞི་སྐྱོང་བ་ནི། ཕྱོགས་སྐྱོང་བཅུ་ཡིན་ལ། ཚོགས་རྣམས་ནི། འཁོར་དང་བཅས་པ་ཐམས་ཅད་འགུགས་པར་ནུས་མ་སྟེ། དེ་ཐམས་ཅད་བཀུག་ནས་འཕྲིན་ལས་སྒྲུབ་ཏུ་འཇུག་པའོ། །

[Block 73]
ཁྲོ་གཉེར་གཡོ་བ་ནི། ཁྲོ་མོར་བཞུགས་པའི་ཐུགས་ཀའི་ཧཱུཾ་ཡིག་གི་འོད་ཟེར་གྱི་བདེ་བས། འཕོངས་ཞིང་སྡུག་བསྔལ་གྱིས་གཟིར་བ་ཐམས་ཅད་སྡུག་བསྔལ་དེ་ལས་རྣམ་པར་སྒྲོལ་བར་མཛད་མའོ། །འདི་ལ་དགུག་པའི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 74 [HEADING]]
###### **ལྔ་པ་དབུ་རྒྱན་གྱི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-2-5-0

[Block 75]
ལྔ་པ་དབུ་རྒྱན་གྱི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་ཟླ་བའི་རྩེ་མོས་དབུ་བརྒྱན། །བརྒྱན་པ་ཐམས་ཅད་ཤིན་ཏུ་འབར་མ། །ཞེས་པ་དབུ་རྒྱན་དངོས་ཏེ། ཟླ་བའི་རྩེ་མོ་སྟེ། ཚེས་གཅིག་གི་ཟླ་བས་དབུ་བརྒྱན་ཅིང་།

[Block 76]
དབུ་རྒྱན་ཟླ་བ་ཐམས་ཅད་ལས། སྡུག་བསྔལ་སེལ་བའི་འོད་ཟེར་ཤིན་ཏུ་འབར་མའོ། །རལ་པའི་ཁུར་ན་འོད་དཔག་མེད་ལས། །རྟག་པར་ཤིན་ཏུ་འོད་ནི་མཛད་མ། །ཞེས་པ་ནི། དབུ་རྒྱན་གཉིས་པ་སྟེ། སྤྱི་གཙུག་གི་སྐྲའི་གསེབ་ན་སྣང་བ་མཐའ་ཡས་བཞུགས་པ་ལ། སེམས་ཅན་གྱི་དོན་དུ་དུས་རྟག་པར་ཤིན་ཏུ་སྟེ་མང་པོར་འོད་ནི། འགྱེད་པར་མཛད་མའོ། །

[Block 77]
འདི་ལ་བཀྲ་ཤིས་སྣང་བའི་སྒྲོལ་(,མ་)ཞེས་འབྱུང་ངོ་། །

[Block 78 [HEADING]]
###### **དྲུག་པ་དྲག་པོའི་བཞུགས་ཚུལ་གྱི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-2-6-0

[Block 79]
དྲུག་པ་དྲག་པོའི་བཞུགས་ཚུལ་གྱི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་བསྐལ་པ་མཐའ་མའི་མེ་ལྟར། །འབར་བའི་ཕྲེང་བའི་དབུས་ན་གནས་མ། །གཡས་བརྐྱངས་གཡོན་བསྐུམས་ཀུན་ནས་བསྐོར་དགའ། །དགྲ་ཡི་དཔུང་ནི་རྣམ་པར་འཇོམས་མ། །ཞེས་པ་སྟེ། བསྐལ་པ་མཐའ་མའི་མེ་ནི། ཉི་མ་བདུན་ལས་ཚ་བའི་འོད་ཟེར་གྱིས་ས་རྡོ་རྣམས་སྲེག་པ་ལྟར། ཡེ་ཤེས་ཀྱི་མེ་ལྕེ་འབར་བའི་ཕྲེང་བའི་དབུས་ན་ཁྲོ་མོའི་བཞུགས་ལུགས་བསྟན་ནས། ཞབས་གཡས་བརྐྱངས་ཤིང་གཡོན་བསྐུམས་ནས་དད་པས་ཆོས་འཁོར་བསྐོར་བར་དགའ་བའི་གདུལ་བྱ་རྣམས་ཀྱི་དགྲ་ཡི་དཔུང་ཉོན་མོངས་པ་རྣམ་པར་འཇོམས་པའོ། །

[Block 80]
འདི་ལ་སྨིན་པར་བྱེད་པའི་སྒྲོལ་(,མ་)ཞེས་འབྱུང་ངོ་། །

[Block 81 [HEADING]]
###### **བདུན་པ་ཧཱུཾ་ཡིག་ལས་འོད་ཟེར་འཕྲོ་བའི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-2-7-0

[Block 82]
བདུན་པ་ཧཱུཾ་ཡིག་ལས་འོད་ཟེར་འཕྲོ་བའི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་(གི་,)འཚལ་ས་གཞིའི་ངོས་ལ་ཕྱག་གི། །མཐིལ་གྱིས་བསྣུན་ཅིང་ཞབས་ཀྱིས་བརྡུང་མ། །ཁྲོ་གཉེར་ཅན་མཛད་ཡི་གེ་ཧཱུཾ་གིས། །རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས་མ། །ཞེས་པ་ལ། ཁྲོ་གཉེར་ཅན་མཛད་ཅེས་པ། ཁྲོ་མོའི་ཆ་བྱད་ཀྱི་ཞབས་གཡས་ཀྱི་མཐིལ་གྱིས་ས་ལ་བསྣུན་ཅིང་། སྡིགས་མཛུབ་མཛད་དེ་ཐུགས་ཀའི་ཡི་གེ་ཧཱུཾ་གིས་འཇིག་རྟེན་རིམ་པ་བདུན་པོ་རྣམས་ཀྱི་སྲིད་མཚོ་འགེམས་མ་སྟེ། སྐེམས་མའོ། །

[Block 83]
འདི་ལ་ཁྲོ་གཉེར་གཡོ་བའི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 84 [HEADING]]
##### གཉིས་པ་ཆོས་སྐུའི་སྒོ་ནས་བསྟོད་པ། ^2-2-2-2-0

[Block 85]
གཉིས་པ་ཆོས་སྐུའི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་བདེ་མ་དགེ་མ་ཞི་མ། །མྱ་ངན་འདས་ཞི་སྤྱོད་ཡུལ་ཉིད་མ། །ཞེས་པ་རྗེ་བཙུན་གྲགས་པས། བདེ་མ་ནི། ཟག་མེད་ཀྱི་བདེ་བ་དང་ལྡན་མ། དགེ་མ་ཡང་སྤང་བྱ་ཉོན་མོངས་པ་དང་བྲལ་བས་དགེ་མ། ཞི་མ་ནི། འབྲས་བུ་སྡུག་བསྔལ་ཞི་མ། རྟོག་པ་ཞི་བའི་མྱ་ངན་ལས་འདས་པ་ལ་སྤྱོད་པ་ཉིད་མ་ཞེས་སོ། །

[Block 86]
ཡང་མཁས་པ་ཁ་ཅིག་ནི། རང་བཞིན་སྐྱེ་མེད་ལ་ཚོགས་ལམ་དུ་ཐོས་བསམ་གྱིས་སྒྲོ་འདོགས་ཆོད་ནས། མ་བདེ་བ་མེད་པས་བདེ་མ། སྦྱོར་ལམ་དུ་སྒོམ་བྱུང་གིས་ཉམས་སུ་མྱོང་ནས་ཉོན་མོངས་རགས་པའི་རྣམ་རྟོག་གི་མཚན་མ་མེད་པས་དགེ་མ། མཐོང་ལམ་དུ་ས་བོན་དང་བྲལ་ནས། འབྲས་བུ་སྐྱེ་རྒ་ན་འཆི་སོགས་ཀྱི་སྡུག་བསྔལ་ཞི་བས་ཞི་མ། མི་སློབ་ལམ་དུ་བག་ཆགས་དང་བཅས་པ་ཞི་བའི་མྱ་ངན་ལས་འདས་པ་ཆོས་སྐུ་མངོན་དུ་མཛད་མའོ། །སྭཱཧཱ་ཨོཾ་དང་ཡང་དག་ལྡན་པས། །སྡིག་པ་ཆེན་པོ་འཇོམས་པ་ཉིད་མ། །ཞེས་པ་གསུང་ཡི་གེ་བཅུ་པ། མཇུག་ཏུ་སྭཱཧཱ། དང་པོར་ཨོཾ་དང་། བར་དུ་སྔགས་བརྒྱད་དང་ཡང་དག་པར་ལྡན་པས། སྡིག་པ་ཆེན་པོ་དངོས་འཛིན་གྱི་གཏི་མུག་འཇོམས་པ་ཉིད་མ། ཞེས་པ་ཐུགས་དང།གསུང་ཆོས་སྐུའི་སྒོ་ནས་བསྟོད་པའོ། །

[Block 87]
འདི་ལ་དགེ་ལེགས་ཞི་བའི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 88 [HEADING]]
#### གསུམ་པ་འཕྲིན་ལས་ཀྱི་སྒོ་ནས་བསྟོད་པ། ^2-2-3-0

[Block 89]
གསུམ་པ་འཕྲིན་ལས་ཀྱི་སྒོ་ནས་བསྟོད་པ་ལ། ཕྱག་འཚལ་དྲུག་ཡོད་པའི།

[Block 90 [HEADING]]
##### དང་པོ་ཞི་ཁྲོའི་སྔགས་ཀྱི་འཕྲིན་ལས། ^2-2-3-1-0

[Block 91]
དང་པོ་ཞི་ཁྲོའི་སྔགས་ཀྱི་འཕྲིན་ལས་ནི། ཕྱག་འཚལ་ཀུན་ནས་བསྐོར་རབ་དགའ་བའི། །དགྲ་ཡི་ལུས་ནི་རབ་ཏུ་འགེམས་མ། །ཡི་གེ་བཅུ་པའི་ངག་ནི་བཀོད་པའི། །རིག་པ་ཧཱུཾ་ལས་སྒྲོལ་མ་ཉིད་མ། །ཞེས་པའི་ཡི་གེ་བཅུ་པའི་ངག་གི་བཀོད་པ་ནི། ཨོཾ་ཏཱ་རེ་ཏུཏྟཱ་རེ་ཏུ་རེ་སྭཱཧཱ།ཞེས་པ་ཡི་གེའི་སྔགས་སོ། །

[Block 92]
རིག་པ་ཧཱུཾ་ནི། ཨོཾ་ན་མ་ཏ་རེ་ན་མོ། ཧ་རེ་ཧཱུཾ་ཧ་ར་སྭཱཧཱ། ཞེས་པ་ཁྲོ་མོའི་སྔགས་སོ། །

[Block 93]
དེ་གཉིས་ཀྱིས་ཀུན་ནས་དད་པས་ཆོས་འཁོར་བསྐོར་བ་ལ་རབ་ཏུ་དགའ་བའི་གདུལ་བྱ་རྣམས་ཀྱི་ཐར་པའི་དགྲ་བོ་ལུས་ནང་ལ་བདག་ཏུ་ཆགས་པ་དང་། ཕྱི་རོལ་ལ་བདག་གིར་ཆགས་པ་རབ་ཏུ་འགེམས་མ་སྟེ།

[Block 94]
ཆགས་པ་འཇོམས་པའི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 95 [HEADING]]
##### གཉིས་པ་ཁྲོ་མོས་ཁམས་གསུམ་གཡོ་བའི་འཕྲིན་ལས། ^2-2-3-2-0

[Block 96]
གཉིས་པ་ཁྲོ་མོས་ཁམས་གསུམ་གཡོ་བའི་འཕྲིན་ལས་ནི། ཕྱག་འཚལ་ཏུ་རེའི་ཞབས་ནི་བརྡབས་པས། །ཧཱུཾ་གི་རྣམ་པའི་ས་བོན་ཉིད་མ། །ཞེས་སོགས་ཏེ། ཧཱུཾ་གི་རྣམ་པའི་ས་བོན་ལས་སྐྱེས་པའི་ཏུ་རེའི་ཞབས་བརྡབས་པས་ཕྱི་རོལ་ན། རི་རབ་མནྡ་ར་དང་འབིགས་བྱེད་ལ་སོགས་པ། འཇིག་རྟེན་གསུམ་པོ་རྣམས་གཡོ་ནུས་པ་ཉིད་དོ། །འདི་ལ་བདེ་བ་སྒྲུབ་པའི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 97 [HEADING]]
##### གསུམ་པ་བརྟན་གཡོའི་དུག་རྣམས་སེལ་བའི་འཕྲིན་ལས། ^2-2-3-3-0

[Block 98]
གསུམ་པ་བརྟན་གཡོའི་དུག་རྣམས་སེལ་བའི་འཕྲིན་ལས་ནི། ཕྱག་འཚལ་ལྷ་ཡི་མཚོ་ཡི་རྣམ་པའི། །རི་དྭགས་རྟགས་ཅན་ཕྱག་ན་བསྣམས་མ། །ཞེས་སོགས་ཏེ། ལྷའི་མཚོ་ལྟ་བུའི་ཟླ་བའི་དཀྱིལ་འཁོར་རི་བོང་གི་རྟགས་ཅན་ཕྱག་ན་བསྣམས་མ་སྟེ། བརྟན་པའི་དུག་ཉོན་མོངས་པའི་གདུང་བ་སེལ་བའི་རྟགས་སོ། །

[Block 99]
ངག་ཏུ་ཏཱ་ར་གཉིས་བརྗོད་ཕཊ་ཀྱི་ཡི་གེས་གཡོ་བའི་དུག་རྣམས་མ་ལུས་པར་ནི་སེལ་མའོ། །

[Block 100]
འདི་ལ་རྣམ་པར་རྒྱལ་བའི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 101 [HEADING]]
##### བཞི་པ་རྩོད་པ་དང་རྨི་ལམ་ངན་པ་སེལ་བའི་འཕྲིན་ལས། ^2-2-3-4-0

[Block 102]
བཞི་པ་རྩོད་པ་དང་རྨི་ལམ་ངན་པ་སེལ་བའི་འཕྲིན་ལས་ནི། ཕྱག་འཚལ་ལྷ་ཡི་ཚོགས་རྒྱལ་པོ་དང་ཞེས་པ་འདོད་ལྷ་བརྒྱ་སྦྱིན་དང། གཟུགས་ཀྱི་ཚངས་པ་ཆེན་པོ་སྟེ་ལྷའི་ཚོགས་རྣམས་ཀྱི་རྒྱལ་པོ་དང་། ལྷ་དང་མིའམ་ཅིའི་རྒྱལ་པོ་ལྗོན་པ་ཆེན་པོ་ལ་སོགས་པས་གཙུག་གིས་གུས་པས་བསྟེན་མ་སྒྲོལ་མ་ཉིད་དོ། །

[Block 103]
ཀུན་ནས་གུས་པས་སྐུ་ཞི་ཁྲོའི་ཆེ་དང་། ཞི་ཁྲོའི་སྔགས་ཀྱི་གོ་ཆ་དགའ་བའི་ཡིད་རྩེ་གཅིག་པས་ཡིད་ལ་བྱེད་ན། བྱིན་རླབས་ཀྱི་གཟི་བརྗིད་ཀྱིས་ཕ་རོལ་པོའི་རྩོད་པ་དང་། རྨི་ལམ་ངན་པ་ཡང་སེལ་བ་ཉིད་དོ། །

[Block 104]
འདི་ལ་སྡུག་བསྔལ་སྲེག་བྱེད་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 105 [HEADING]]
##### ལྔ་པ་རིམས་ནད་སེལ་བའི་སྒྲོལ་མའི་འཕྲིན་ལས། ^2-2-3-5-0

[Block 106]
ལྔ་པ་རིམས་ནད་སེལ་བའི་སྒྲོལ་མའི་འཕྲིན་ལས་ནི། ཕྱག་འཚལ་ཉི་མ་ཟླ་བ་རྒྱས་པ་ལྟ་བུའི་སྤྱན་གཡས་པ། ཟླ་བ་རྒྱས་པ་ལྟ་བུའི་སྤྱན་གཡོན་པ་(ཅེས་,ཞེས་)གསུང་ཡང་། ཉི་མ་རྒྱས་པ་ལྟ་བུའི་ཁྲོ་མོའི་སྤྱན། ཟླ་བ་རྒྱས་པ་ལྟ་བུའི་ཞི་བའི་སྤྱན་གཉིས་པོ་ལ་འོད་རབ་ཏུ་གསལ་བ་འཕྲོ་བ་དང་། ངག་ཏུ་ཁྲོ་མོའི་སྔགས་ཧ་ར་གཉིས་བརྗོད། ཞི་བའི་སྔགས་ཏུ་ཏྟཱ་ར་ཡི་སྔགས་བརྗོད་པ་ཡིས་ཤིན་ཏུ་དྲག་པོའི་རིམས་ནད་སེལ་མ་ཉིད་དོ། འདི་ལ་དངོས་གྲུབ་འབྱུང་གནས་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 107 [HEADING]]
##### དྲུག་པ་གདོན་དང་རོ་ལངས་འཇོམས་པའི་འཕྲིན་ལས། ^2-2-3-6-0

[Block 108]
དྲུག་པ་གདོན་དང་རོ་ལངས་འཇོམས་པའི་འཕྲིན་ལས་ནི། ཕྱག་འཚལ་དེ་ཉིད་གསུམ་རྣམས་བཀོད་པའི། །ཞེས་པ་སྐུ་གསུང་ཐུགས་ཀྱི་དེ་ཉིད་དེ། སྐུའི་དེ་ཉིད་སྤྱི་བོར་ཨོཾ། གསུང་གི་དེ་ཉིད་མགྲིན་པར་ཨཱཿ ཐུགས་ཀྱི་དེ་ཉིད་ཐུགས་ཀར་ཧཱུཾ་རྣམས་བཀོད་པའི་མཐུ་བརྟན་པའི། དྲུག་ཉོན་མོངས་ཞི་བའི་མཐུ་དང་ཡང་ལྡན་མ། གཡོ་བའི་དུག་གདོན་དང་རོ་ལངས་གནོད་སྦྱིན་ཚོགས་རྣམས་འཇོམས་པ་ལ། རབ་མཆོག་ནི། ཏུ་རེ་སྒྲོལ་མ་ཉིད་ཡིན་ནོ། །

[Block 109]
འདི་ལ་ཡོངས་སུ་རྫོགས་བྱེད་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 110 [HEADING]]
### གསུམ་པ་ཕན་ཡོན་བསྟན་པ། ^2-3-0
--- END BLOCKS ---
