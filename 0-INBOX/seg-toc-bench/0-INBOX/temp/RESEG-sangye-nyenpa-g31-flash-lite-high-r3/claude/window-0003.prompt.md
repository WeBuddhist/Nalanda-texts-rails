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
[Block 106 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-17-2-0

[Block 107]
གསལ་འདེབས་ཚུལ་ནི། དགྲ་དང་བྱད་མའི་རིག་སྔགས་སྟོབས་གཞོམ་སྒྲོལ་མ་འདི་ཉིད་སྐུ་མདོག་དམར་མོ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས་གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་། རྡོ་རྗེ་རྒྱ་གྲམ་ལས་འོད་ཟེར་འཕྲོས་པས་དགྲ་བོ་བྱད་མའི་མཐུ་སྟོབས་ངག་ནུས་ཐམས་ཅད་བཤིག་པར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 108 [HEADING]]
### ཕྱག་འཚལ་བཅུ་བདུན་པ། ^1-18-0

[Block 109 [HEADING]]
#### ཚིག་འགྲེལ། ^1-18-1-0

[Block 110 [VERSE]]
ཕྱག་འཚལ་ཏུ་རེའི་ཞབས་ནི་བརྡབས་པས། །
ཧཱུྃ་གི་རྣམ་པའི་ས་བོན་ཉིད་མ། །
རི་རབ་མནྡཱ་ར་དང་འབིགས་བྱེད། །
འཇིག་རྟེན་གསུམ་རྣམས་གཡོ་བ་ཉིད་མ། །

[Block 111]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། ཏུ་རེ་ཞེས་པ་མྱུར་མ་ཁྱེད་ཀྱི་ཞབས་མཐིལ་གཉིས་ནི་ས་ལ་བརྡབས་ཅིང་བསྣུན་པས། ཐུགས་ཀའི་ཧཱུཾ་ལས་འོད་ཟེར་ཧཱུཾ་གི་རྣམ་པའི་ས་བོན་ཚོགས་ཉིད་ནི་འཕྲོ་བར་མཛད་མའི་རྗེ་བཙུན་མ། རིའི་རྒྱལ་པོ་རི་རབ་དང་མནྡ་ར་དང་། རི་བོ་འབིགས་བྱེད་ཅེས་རི་བོ་གངས་ཅན་དང་། འཇིག་རྟེན་གསུམ་རྣམས་གཡོ་བར་མཛད་པའི་མཐུ་སྟོབས་ཀྱིས་ཕ་རོལ་དགྲ་ཇག་སོགས་མནན་ཏེ་འགྲོ་རྣམས་བདེ་བར་འགོད་པར་མཛད་མ་ཉིད་ནི་འཕགས་མ་ཁྱེད་ལའོ། །

[Block 112 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-18-2-0

[Block 113]
གསལ་འདེབས་ཚུལ་ནི། དགྲ་ཇག་ཆོམ་རྐུན་འཆིང་བའི་སྒྲོལ་མ་དཔག་མེད་གནོན་མ་འདི་ཉིད་སྐུ་མདོག་དམར་སེར། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་དུ། མཆོད་རྟེན་དང༌། ཐུགས་ཀའི་ཧཱུཾ་ལས་འོད་ཟེར་ཧཱུཾ་ཡིག་གྲངས་མེད་དང་། ཞབས་མཐིལ་ས་ལ་བརྡབས་པས་རི་རབ་དང༌། མནྡཱ་ར། འབིགས་བྱེད། ཁམས་གསུམ་གཡོ་བའི་སྟོབས་ཀྱིས་དམིགས་བྱ་རྣམས་ཞབས་འོག་ཏུ་མནན་པར་བསྒོམས་ནི་དམིགས་རིམ་ཡིན།

[Block 114 [HEADING]]
### ཕྱག་འཚལ་བཅོ་བརྒྱད་པ། ^1-19-0

[Block 115 [HEADING]]
#### ཚིག་འགྲེལ། ^1-19-1-0

[Block 116 [VERSE]]
ཕྱག་འཚལ་ལྷ་ཡི་མཚོ་ཡི་རྣམ་པའི། །
རི་དྭགས་རྟགས་ཅན་ཕྱག་ན་བསྣམས་མ། །
ཏཱ་ར་གཉིས་བརྗོད་ཕཊ་ཀྱི་ཡི་གེས། །
དུག་རྣམས་མ་ལུས་པ་ནི་སེལ་མ། །

[Block 117]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། ལྷ་ཡི་ཡུལ་གྱི་བདུད་རྩིའི་མཚོ་ཡི་རྣམ་པའི་དཀར་ཞིང་། དཀར་ཟླུམ་གྱི་རི་དྭགས་རྟགས་ཅན་ཟླ་བ་ཉ་གང་བ་ཕྱག་གཡོན་ན་བསྣམས་པའི་འཕགས་མ་སྐུའི་ཏིང་འཛིན་གྱི་གསལ་སྣང་བསྒོམས་པས་བརྟན་པའི་དུག་སེལ་བ། ཏཱ་ར་གཉིས་བརྗོད་པ་ཅན་གྱི་རིག་སྔགས་ཡི་གེ་བཅུ་པ་ལ་ཕཊ་ཀྱིས་བརྒྱན་པའི་ཡི་གེ་ཅན་གྱིས་རིག་སྔགས་བཟླས་པས་གཡོ་བའི་དུག་རྣམས་མ་ལུས་པ་ནི་སེལ་བར་མཛད་མ་རྗེ་བཙུན་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 118 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-19-2-0

[Block 119]
གསལ་འདེབས་ཚུལ་ནི། དུག་རིགས་ཞི་ཞིང་སྲུང་བའི་འཕགས་མ་རྨ་བྱ་ཆེན་མོ་འདི་ཉིད་སྐུ་མདོག་དཀར་མོ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་ན། ཟླ་བ་ཉ་གང་བ་རི་དྭགས་རྟགས་ཅན་ལས་འོད་ཟེར་ཕྱོགས་ཀུན་ཏུ་འཕྲོ་པས་བརྟན་གཡོའི་དུག་རྣམས་བཅོམ་པར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 120 [HEADING]]
### ཕྱག་འཚལ་བཅུ་དགུ་པ། ^1-20-0

[Block 121 [HEADING]]
#### ཚིག་འགྲེལ། ^1-20-1-0

[Block 122 [VERSE]]
ཕྱག་འཚལ་ལྷ་ཡི་ཚོགས་རྣམས་རྒྱལ་པོ། །
ལྷ་དང་མིའམ་ཅི་ཡིས་བསྟེན་མ། །
ཀུན་ནས་གོ་ཆ་དགའ་བས་བརྗིད་ཀྱིས། །
རྩོད་དང་རྨི་ལམ་ངན་པ་སེལ་མ། །

[Block 123]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། འདོད་གཟུགས་ཀྱི་ལྷ་ཡི་ཚོགས་རྣམས་ཀྱི་རྒྱལ་པོ་ཚངས་དང་བརྒྱ་བྱིན་སོགས་དང༌། འཇིག་རྟེན་ན་མཐུ་ཆེ་བར་གྲགས་པ་རི་དང་ཤིང་ཆུ་སོགས་ཀྱི་ལྷ་དང་། མིའམ་ཅི་ཡི་རྒྱལ་པོ་སོགས་ཀྱིས་གུས་པས་ཁྱེད་ཞབས་བསྟེན་མ། འཕགས་མ་གདུགས་དཀར་མོས་ཀུན་ནས་བྱིན་གྱིས་བརླབས་པའི་སྔགས་དང་ཕྱག་རྒྱའི་གོ་ཆ་དགའ་བས་འཕགས་མ་ཁྱེད་ཉིད་གོ་པོའི་སྒོ་གསུམ་གཟི་བརྗིད་ཀྱིས་ཕ་རོལ་པོའི་རྩོད་པ་དང༌། རྨི་ལམ་མཚན་མ་ངན་པ་རྣམས་ཡོངས་སུ་སེལ་བར་མཛད་པའི་འཕགས་མ་ཁྱེད་ལའོ། །ཞེས་ཚིག་འགྲེལ་ཡིན།

[Block 124 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-20-2-0

[Block 125]
གསལ་འདེབས་ཚུལ་ནི། རྩོད་དང་རྨི་ལམ་ངན་པ་སེལ་བའི་འཕགས་མ་མི་ཕམ་གདུགས་དཀར་མོ་འདི་ཉིད་སྐུ་མདོག་དཀར་མོ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་སྟེང་ན་གདུགས་དཀར་པོ་ལས་རྡོ་རྗེའི་མེ་ཡི་ཚྭ་ཚྭ་འཕྲོས་པས། རྒོལ་ངན་གྱི་རྩོད་པ་དང༌། འབྱུང་བ་འཁྲུགས་པའི་རྨི་ལམ་ངན་པ་བསལ་བར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 126 [HEADING]]
### ཕྱག་འཚལ་ཉི་ཤུ་པ། ^1-21-0

[Block 127 [HEADING]]
#### ཚིག་འགྲེལ། ^1-21-1-0

[Block 128 [VERSE]]
ཕྱག་འཚལ་ཉི་མ་ཟླ་བ་རྒྱས་པའི། །
སྤྱན་གཉིས་པོ་ལས་འོད་རབ་གསལ་མ། །
ཧ་ར་གཉིས་བརྗོད་ཏུཏྟཱ་ར་ཡིས། །
ཤིན་ཏུ་དྲག་པོའི་རིམས་ནད་སེལ་མ། །

[Block 129]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། ཉི་མ་དང་ཟླ་བ་རྒྱས་པ་ལྟ་བུའི་སྤྱན་གཉིས་པོ་ལས་འོད་ཟེར་རབ་ཏུ་འབར་བ་འཕྲོས་པས་ནད་བདག་དང་ནད་རིམས་བཅས་གསོ་བར་མཛད་མ་ཁྱེད་ཀྱི་སྐུ་གསལ་ལ་མཛེས་མ། རྩ་བའི་རིག་སྔགས་བཅུ་པ་ལ་ཧཱ་ར་གཉིས་ལྡན་གྱི་བརྗོད་པ་ཏུཏྟཱ་ར་ཡིས་ཤིན་ཏུ་དྲག་པོའི་རིམས་ནད་གསོ་དཀའ་བ་རྣམས་ཀྱང་སེལ་བར་མཛད་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 130 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-21-2-0

[Block 131]
གསལ་འདེབས་ཚུལ་ནི། རིམས་ནད་སེལ་བའི་འཕགས་མ་རི་ཁྲོད་ལོ་གྱོན་མ་འདི་ཉིད་སྐུ་མདོག་དཀར་སེར། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་ན། བདུད་རྩིས་གང་བའི་ཟ་མ་ཏོག་ལས་འོད་ཟེར་འཕྲོས་པས་ནད་བདག་དང་ནད་རིམས་བསྲེག་ཅིང་གསོ་བར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 132 [HEADING]]
### ཕྱག་འཚལ་ཉེར་གཅིག་པ། ^1-22-0

[Block 133 [HEADING]]
#### ཚིག་འགྲེལ། ^1-22-1-0

[Block 134 [VERSE]]
ཕྱག་འཚལ་དེ་ཉིད་གསུམ་རྣམས་བཀོད་པའི། །
ཞི་བའི་མཐུ་དང་ཡང་དག་ལྡན་མ། །
གདོན་དང་རོ་ལངས་གནོད་སྦྱིན་ཚོགས་རྣམས། །
འཇོམས་པ་ཏུ་རེ་རབ་མཆོག་ཉིད་མ། །

[Block 135]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། སྒྲུབ་པ་པོ་རང་གི་སྤྱི་བོར་ཨོཾ་དཀར་པོ། མགྲིན་པར་གསུང་གི་ཨཱཿདམར་པོ། སྙིང་གར་ཐུགས་ཀྱི་ཧཱུཾ་སྔོན་པོ་སྟེ་དེ་ཁོ་ན་ཉིད་གསུམ་རྣམས་མཚོན་ནས་གནས་གསུམ་དུ་བཀོད་ནས་བསྒོམ་ན། འཕགས་མའི་ལྷ་སྔགས་ཏིང་འཛིན་གྱི་དེ་ཉིད་གསུམ་རང་ལ་གནས་པའི་ཕྱིར། ཕྱི་ནང་གསང་གསུམ་གྱི་ཁར་ཆད་ཐམས་ཅད་རང་བཞིན་གྱིས་ཞི་བའི་མཐུ་དང་ཡང་དག་པར་ལྡན་མ་དེ་ཉིད་ཀྱི་གནས་གསུམ་ལས་སྤྲོས་པའི་འོད་ཀྱིས། གདོན་རིགས་བཅོ་བརྒྱད་སོགས་དང་རོ་ལངས་འབྱུང་པོ། མདངས་འཕྲོག་པའི་གནོད་སྦྱིན་སོགས་ཀྱི་ཚོགས་རྣམས་ཀྱི་བསམ་སྦྱོར་ངན་པ་རྣམས་འཇོམས་པར་མཛད་མ། ཏཱུ་རེ་སྟེ་མྱུར་མ་ཁྱེད་ཐུགས་རབ་ཏུ་བརྩེ་བའི་མཆོག་གི་བདག་ཉིད་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 136 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-22-2-0

[Block 137]
གསལ་འདེབས་ཚུལ་ནི། ནད་པའི་བླ་ཚེ་བླུ་བྱེད་ཀྱི་འཕགས་མ་ལྷ་མོ་འོད་ཟེར་ཅན་མ་འདི་ཉིད་སྐུ་མདོག་དཀར་མོ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་དུ་གསེར་ཉ་ལས་འོད་ཟེར་འཕྲོས་པས། ནད་པའི་བླ་ཚེ་བརྐུས་པ་སླར་བཀུག་ནས་ཐོབ་པར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 138 [HEADING]]
### གཞུང་གི་དོན་བསྡུ་བ། ^1-23-0

[Block 139]
གཞུང་གི་དོན་བསྡུ་བ།

[Block 140 [VERSE]]
རྩ་བའི་སྔགས་ཀྱི་བསྟོད་པ་འདི་དང་། །
ཕྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག །

[Block 141]
ཞེས་པ་སྟེ། དོན་བསྡུ་ན་སྒྲོལ་མའི་རྩྭ་བའི་རིག་སྔགས་ཀྱི་དོནདང་ཡོན་ཏན་སྤེལ་བའི་སྒོ་ནས་བསྟོད་པ་འདི་དང་ཕྱག་འཚལ་བའི་ཚིགས་སུ་བཅད་པ་ཉི་ཤུ་རྩ་གཅིག་གིས་འཕགས་མའི་རྣམ་འཕྲུལ་ཉི་ཤུ་རྩ་གཅིག་གཞུང་འདིར་ཚང་བ་བསྟན་པ་ཡིན་ནོ། །

[Block 142 [HEADING]]
## མཇུག་བྱང། ^a-0

[Block 143 [HEADING]]
### མཛད་བྱང། ^a-1-0

[Block 144]
ཕྱག་འཚལ་ཉེར་གཅིག་གི་རྒྱས་འགྲེལ་ནི་ཀློག་པ་པོ་ཉུང་ཞིང་དོན་རྟོགས་དཀའ་བ་ལ་རྟེན། རྒྱུན་ལྡན་སྒྲོལ་མའི་ཉམས་ལེན་ལ་བརྩོན་པ་རྣམས་ལ་ཕན་དུ་རེ་བས། ཏཱ་ར་ན་ཐ་དང༌། ཀུན་མཁྱེན་འཇིགས་མེད་གླིང་པ། རྒྱལ་སྲས་བསྟན་འཛིན་རབ་རྒྱས་སོགས་ཀྱི་འགྲེལ་པ་གཞིར་བཞག ཚིག་འགྲེལ་རྣམས་གང་ཐུབ་གོ་བདེ་བར་བྱས། རྒྱས་བསྡུས་རན་པོར་བཀོད་དེ། ཕྲན་སངས་རྒྱས་མཉན་སྤྲུལ་མིང་དུ་འབོད་པས་བྲིས་པས། ཀུན་ལ་སྨན་པའི་རྒྱུར་གྱུར་ཅིག།།
--- END BLOCKS ---
