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

[Block 41]
བཅུ་དྲུག་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཐུགས་ཀར་འཁོར་ལོའི་ལྟེ་བར་ཨོཾ་དང་རྩིབས་རྣམས་ལ་སྔགས་ཀྱི་ཡི་གེས་ཀུན་ནས་བསྐོར་བའི་རབ་ཏུ་དགའ་བར་མཛད་པའི་སྒྲོལ་འོད་ཀྱིས། དགྲ་ཡི་ལུས་ནི་རབ་ཏུ་འགེམས་པར་མཛད་མ། ཨོཾ་ཏཱ་རེ་ཏུཏྟཱ་རེ་ཏུ་རེ་སྭཱ་ཧཱ། ཞེས་པའི་ཡི་གེ་བཅུ་པོའི་ངག་ནི་འཁོར་ལོའི་རྣམ་པར་བཀོད་པའི་རིག་པ་ཧཱུཾ་ལས།

[Block 42]
ༀ་ན་མཿ ཏཱ་རེ་ན་མོ་ཧཱ་རེ་ཧཱུྃ་ཧཱ་རེ་སྭཱ་ཧཱ་ཞེས་བདུད་སྡེ་འཇོམས་པའི་ཁྲོ་བོའི་ཚུལ་གྱིས་སྒྲོལ་མ་ཉིད་དུ་མཛད་མ་ལའོ། །

[Block 43 [HEADING]]
### ཕྱག་འཚལ་བཅུ་བདུན་པ། ^1-17-0

[Block 44]
བཅུ་བདུན་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཏུ་རེ་ནི་མྱུར་མ་སྟེ་སྒྲོལ་མའི་ཞབས་ས་ལ་བརྡབས་པས། ཧཱུཾ་གི་རྣམ་པའི་ས་བོན་ཉིད་དང་ལྡན་མ། དེས་སྟོང་གསུམ་གྱི་ཕྱི་རོལ་ན་གནས་རི་རབ་མནྡ་ར་ཞེས་པ་དང་རི་རབ་འབིགས་བྱེད་ལ་སོགས་པ་སྟེ། མདོར་ན་འཇིག་རྟེན་སྲིད་པ་གསུམ་པོ་རྣམ་པར་གཡོ་བར་མཛད་པའི་བདག་ཉིད་མ་ལའོ། །

[Block 45 [HEADING]]
### ཕྱག་འཚལ་བཅོ་བརྒྱད་པ། ^1-18-0

[Block 46]
བཅོ་བརྒྱད་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། དྭངས་ཤིང་བསིལ་བ་སོགས་ཡོན་ཏན་ཁྱད་པར་ཅན་དང་ལྡན་པའི་ལྷ་ཡི་བདུད་རྩིའི་མཚོ་ཡི་རྣམ་པའི་བདག་ཉིད་ཅན་གྱི་རི་དྭགས་རྟགས་ཅན་ཏེ་ཟླ་བ་ཕྱག་ན་བསྣམས་མ། ཏཱ་ར་གཉིས་བརྗོད་པའི་མཐར་ཕཊ་ཀྱི་ཡི་གེས་སེམས་ཅན་གང་ཞིག་བརྟན་གཡོའི་དུག་རྣམས་མ་ལུས་པ་ནི་སེལ་བའི་སྒྲོལ་མ་ལའོ། །

[Block 47 [HEADING]]
### ཕྱག་འཚལ་བཅུ་དགུ་པ། ^1-19-0

[Block 48]
བཅུ་དགུ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ལྷ་ཡི་ཚོགས་རྣམས་ཀྱི་རྒྱལ་པོ་ཚངས་པ་དང་། བརྒྱ་བྱིན་དང་། ལྷ་ཕལ་པ་དང་། མིའམ་ཅི་ཡི་ཚོགས་ཐམས་ཅད་ཀྱིས་ཞབས་ལ་བརྟེན་མ། ཀུན་ནས་ལྷ་ཡི་རྣམ་པ་དང་སྔགས་ཀྱི་གོ་ཆ་དགའ་བའི་སྟེ་གཟི་བརྗིད་ཀྱིས་རྩོད་པ་དང་རྨི་ལམ་ངན་པ་ཐམས་ཅད་སེལ་བའི་སྒྲོལ་མ་ལའོ། །

[Block 49 [HEADING]]
### ཕྱག་འཚལ་ཉི་ཤུ་པ། ^1-20-0

[Block 50]
ཉི་ཤུ་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། ཉི་མ་དང་ཟླ་བ་རབ་ཏུ་རྒྱས་པ་ལྟ་བུས་སྤྱན་གཉིས་པོ་ལས་འོད་རབ་ཏུ་གསལ་ཞིང་འབར་མ་ཧཱ་ར་གཉིས་བརྗོད་པའི་ཏུཏྟཱ་རེ་སྟེ་རིག་སྔགས་ཀྱི་ཡི་གེ་ཤིན་ཏུ་དྲག་པོས་རིམས་ནད་ཐམས་ཅད་སེལ་བར་མཛད་པའི་སྒྲོལ་མ་ལའོ། །

[Block 51 [HEADING]]
### ཕྱག་འཚལ་ཉེར་གཅིག་པ། ^1-21-0

[Block 52]
ཉེར་གཅིག་པ་ནི། ཕྱག་འཚལ། གང་ལ་ན། གནས་གསུམ་དེ་ཉིད་གསུམ་སྟེ་འབྲུ་གསུམ་གྱི་ཡི་གེ་རྣམས་བཀོད་པས་དེའི་འོད་ཀྱིས་ཉོན་མོངས་ཞི་བའི་མཐུ་དང་ཡང་དག་པར་ལྡན་མ། གདོན་དང་རོ་ལངས་དང་གནོད་སྦྱིན་གྱི་ཚོགས་དང་འཇིགས་པ་དང་གནོད་པ་རྣམས་འཇོམས་པ་ལ། ཏུ་རེ་རབ་མཆོག་སྟེ་ཡི་གེ་བཅུ་པའི་སྔགས་ཀྱིས་འཇོམས་པར་མཛད་པ་ཉིད་ཀྱི་སྒྲོལ་མ་ལའོ། །

[Block 53]
རྩ་བའི་སྔགས་ཏེ་སྔར་བསྟན་པའི་ཞི་ཁྲོའི་སྔགས་ཀྱིས་བརྒྱན་པའི་བསྟོད་པ་འདི་དང་། ཕྱག་འཚལ་བ་ནི་གང་ལ་ན་རྣམ་འཕྲུལ་ཉི་ཤུ་རྩ་གཅིག་དང་ལྡན་པའི་སྒྲོལ་མ་ལའོ། །

[Block 54 [HEADING]]
## ཕན་ཡོན། ^2-0

[Block 55]
གཉིས་པ་ཕན་ཡོན་ནི། ལྷ་མོ་སྒྲོལ་མ་ལ་གུས་པ་ཡང་དག་པ་དང་ལྡན་པའི་བློ་དང་ལྡན་པས་གང་ཟག་གིས་བསྟོད་པའི་རྒྱལ་པོ་འདི་སེམས་རབ་ཏུ་དང་བས་བརྗོད་དེ། སྲོད་ལ་དྲག་པོ་དང་ཐོ་རངས་ཞི་བ་སོགས་སྐུར་མོས་པས་ལངས་པར་བྱས་ནས། ཡིད་ལ་དྲན་པས་འཇིགས་པ་ལས་སྐྱོབ་ཅིང་མི་འཇིགས་པ་ཐམས་ཅད་རབ་ཏུ་གཏོར་རོ། །

[Block 56]
དེར་མ་ཟད་ངན་འགྲོའི་རྒྱུ་སྡིག་པ་ཐམས་ཅད་རབ་ཏུ་ཞི་ཞིང་། འབྲས་བུ་ངན་འགྲོའི་སྡུག་བསྔལ་ཐམས་ཅད་འཇོམས་པ་ཉིད་དོ། །

[Block 57]
རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན་རྣམས་ཀྱིས་ཀྱང་མྱུར་དུ་དབང་ནི་བསྐུར་བར་འགྱུར་ལ། ཚེ་འདི་ཉིད་ལ་བདེ་བ་ཆེ་བ་ཉིད་ནི་ཐོབ་ཅིང་། མཐར་ཐུག་ཏུ་ཡང་སངས་རྒྱས་ཀྱི་གོ་འཕང་ཡང་མཐར་ཐུག་པ་དེར་འགྲོ་བ་ཉིད་དོ། །

[Block 58]
དེ་འཐོབ་པ་ལ་བར་དུ་གཅོད་པའི་དུག་ནི་དྲག་པོ་ཆེན་པོ་སྟེ་བདག་ཏུ་ལྟ་བ་དང་། རྐུན་པོ་དང་། ཤ་ཟ་ལ་སོགས་པ་བརྟེན་གནས་པ་སྟེ་རྟག་པར་གནོད་པའམ། གཞན་ཡང་འགྲོ་བ་སྦྲུལ་ལ་སོགས་པའི་དུག་ཀྱང་དྲན་པ་ཙམ་གྱིས་རབ་ཏུ་སེལ་བ་ཉིད་ཐོབ་ལ། གདོན་དང་རིམས་དང་དུག་གིས་གཟིར་བའི་སྡུག་བསྔལ་ཉེར་འཚེའི་ཚོགས་ནི་རྣམ་པར་སྤང་ཞིང་། སེམས་ཅན་རང་ལས་གཞན་པ་རྣམས་ལ་ཡང་ཕན་ཡོན་འདི་ལྟ་བུ་འབྱུང་ངོ་། ། ཉིན་མཚན་གཉིས་དང་ཉིན་མཚན་ལན་གསུམ་གསུམ་དུ་བསྟོད་པ་འདི་བདུན་བདུན་དུ་མངོན་པར་བརྗོད་ན། བུ་འདོད་པའི་ནི་བུ་ཐོབ་འགྱུར་ཞིང་། ནོར་འདོད་པའི་ནི་ནོར་རྣམས་ཉིད་ཐོབ་ཅིང་། མདོར་ན་ཡིད་ལ་ཇི་ལྟར་བསམ་པའི་འདོད་པ་ཐམས་ཅད་འགྲུབ་པར་འགྱུར་ཏེ། བགེགས་དང་བར་དུ་གཅོད་པ་ཐམས་ཅད་མེད་ཅིང་མི་འབྱུང་ལ། བྱུང་ཡང་སོ་སོར་རྗེ་བཙུན་མ་ཉིད་ཀྱི་མཐུས་འཇོམས་པར་འགྱུར་རོ། །

[Block 59 [HEADING]]
## མཇུག་བྱང། ^a-0

[Block 60 [HEADING]]
### མཛད་བྱང། ^a-1-0

[Block 61]
ཞེས་པའང་རང་གི་བརྗེད་ཐོ་ལྟ་བུར། ༸ཀརྨ་མཻ་ཏྲིའི་མིང་གིས་མཁས་གྲུབ་ཀྱིས་གསུངས་པ་དག་ལས་ཟིན་ཐོར་བྲིས་པ་ཤུ་བྷཾ།། ༎
--- END BLOCKS ---
