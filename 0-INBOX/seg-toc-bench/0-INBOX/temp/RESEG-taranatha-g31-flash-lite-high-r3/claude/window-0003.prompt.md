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
#### ཚིག་འགྲེལ། ^1-14-1-0

[Block 107]
ཚིགས་བཅད་བཅུ་བཞི་པ་ཕྱག་འཚལ་ས་གཞི་སོགས་ལ། རི་རབ་གླིང་དང་བཅས་པའི་ས་གཞི་ཆེན་པོའི་ངོས་ལ། ཐལ་མོ་བརྡབས་པའི་ཕྱག་གི་མཐིལ་གྱིས་བསྣུན་པའོ། །

[Block 108]
ཞབས་ཀྱིས་རྡུང་མ་ལས་དང་། ཞལ་རས་ཁྲོ་གཉེར་ཅན་དུ་མཛད་ཅིང་ཁྲོ་བའི་ཤུགས་ཀྱིས་ཧཱུྃ་ཞེས་ཤངས་ནས་འཇིགས་པའི་སྒྲ་བསྒྲགས་པས་ས་འོག་རིམ་པ་བདུན་ན་ནས་པའི་ཀླུ་དང་ལྷ་མིན་དང་སྲིན་པོ་དང་ཡི་དྭགས་གདུག་པ་ཅན་རྣམས་ཐམས་ཅད་འགེམས་པ་མོ་སྟེ་དུམ་བུར་འཐོར་པར་མཛད་པའོ། །

[Block 109]
དེ་ལས་འོག་བདུན་ནི། ས་གཞི་ཆེན་པོ་འདི་ཉིད་ལ། འོག་ཏུ་ཐོག་ཕུགས་རིམ་པ་བདུན་བཞིན་དུ་མི་མ་ཡིན་གྱི་ཡུལ་ཆེན་པོ་དག་གནས་པའོ། །

[Block 110]
ཁ་ཅིག་ནི་རི་རབ་ཀྱི་རྩེ་མོའི་ཁོངས་སེང་ནས་ཐུར་དུ་གཞལ་བ་ཡིན་ཟེར་ཡང་མི་ལེགས་པར་མངོན་ནོ། །

[Block 111]
དེ་ཡང་གཞི་དང་། ལྷག་པའི་གཞི་དང་། གཞི་མེད་པ་དང་། གཞི་ཉིད་དང་བཅུད་ཀྱི་གཞི་དང་། གཞི་བཟང་པོ་དང་། དག་པའི་གཞི་ཞེས་བྱའོ། །

[Block 112]
ས་འོག་གི་འཇིག་རྟེན་ཆེན་པོ་རྣམས་སོ། །

[Block 113 [HEADING]]
#### སྦས་དོན། ^1-14-2-0

[Block 114]
སྦས་དོན་ནི། ས་གཞིའི་ངོས་ནི་ལྟེ་བའི་དཀྱིལ་འཁོར་ཏེ། དེ་ལ་གཏུམ་མོ་ཡེ་ཤེས་ཀྱི་མེ་ངེས་པའི་དོན་གྱི་ལྷ་མོའི་ཞབས་ཀྱིས་བརྡུངས་པ་དང་མེ་ལྕེའི་ཕྱག་གིས་བསྣུན་པའོ། །

[Block 115]
དེ་ཡང་ས་འོག་བདུན་ཏེ། དབུ་མའི་མས་སྣ་ན་ཚངས་པའི་མེ་སྤུལ་ལྟར་འཁིལ་བ་ལན་བདུན་པ། རབ་ཏུ་འབར་བ་གནས་པ་དེར། གཏུམ་མོ་འབར་བའི་བྱང་ཆུབ་ཀྱི་སེམས་འོངས་བ་ན་མེའི་གདུང་བ་རབ་ཏུ་ཞི་བ་དང་། དེའི་རྩ་མདུད་རྣམས་འགེམས་ཤིང་འཇིགས་པའོ། །

[Block 116 [HEADING]]
### ཕྱག་འཚལ་བཅོ་ལྔ་པ། ^1-15-0

[Block 117 [HEADING]]
#### ཚིག་འགྲེལ། ^1-15-1-0

[Block 118]
ཚིགས་བཅད་བཅོ་ལྔ་པ་ཕྱག་འཚལ་བདེ་མ་སོགས་ལ། བཅོམ་ལྡན་འདས་མ་ཉིད་རྟག་ཏུ་བདེ་བ་དང་། དགེ་མ་དང་། ཞི་བའི་ངང་ཚུལ་ཅན་མ། མྱ་ངན་ལས་འདས་པ་མཆོག་ཏུ་ཞི་བ། འགོག་བདེན་གྱི་དབྱིངས་ལ་མཉམ་པར་འཇོག་པས་ཞི་བའི་སྤྱོད་ཡུལ་ཅན་མ་སྟེ། དེའི་ཕྱིར་འགྲོ་བ་རྣམས་ལ། ཚེ་འདིའི་བདེ་བ་དང་། ཕ་རོལ་གྱི་དོན་དུ་དགེ་བ་བསྐྱེད་པར་མཛད་པ་མ། སྐལ་པ་དང་ལྡན་པ་རྣམས་ལ། ཞི་བའི་ལམ་སྟོན་པར་མཛད་ཅིང་། འབྲས་བུ་མི་གནས་པའི་མྱང་འདས་ཞི་བ་དམ་པའི་སྤྱོད་ཡུལ་ལ་འགོད་པར་མཛད་པ་སྟེ། གཞན་ཡང་ལྷ་མོ་ཉིད་ཀྱིས་གསུངས་པའི་རིག་སྔགས་སྭཱ་ཧཱ་དང་ཨོཾ་དང་ཡང་དག་པར་ལྡན་བདག་བཟླས་པས། སྡིག་པ་ཆེན་པོ་དང་དེའི་འབྲས་བུ་སྡུག་བསྔལ་ཆེན་པོ་རྣམས་ཀྱང་འཇོམས་པར་མཛད་པ་ཉིད་དོ། །

[Block 119]
འདིས་ཞི་བའི་ལས་ཀྱི་མཐའ་བསྒྱུར་བའི་སྔགས་སྭཱ་ཧཱ་ར་བཤད་ཅིང་། གོང་དུ་ཟློག་པ་ལ་ཏྲཊ་དང་། བསད་པ་ལ་ཕཊ་དུ་གསུངས་པས། ལས་གཞན་རྣམས་ཀྱི་སྔགས་ཀྱི་མཐའ་བསྒྱུར་བ་ཡང་ཞོར་ལ་འཕངས་པ་ཡིན་ནོ། །

[Block 120 [HEADING]]
#### ངེས་དོན། ^1-15-2-0

[Block 121]
འདིའི་ངེས་པའི་དོན་མཐར་ཐུག་པ་ནི། བདེ་མ་ནི་སོར་རྟོག་ཡེ་ཤེས། དགེ་མ་ནི་མེ་ལོང་ཡེ་ཤེས། ཞི་མ་མཉམ་ཉིད་ཡེ་ཤེས། མྱ་ངན་འདས་ཞི་ནི་ཆོས་དབྱིངས་ཡེ་ཤེས། སྡིག་པ་ཆེན་པོ་འཇོམས་པ་ནི་བྱ་གྲུབ་ཡེ་ཤེས་སོ། །

[Block 122]
གསུང་གཞོམ་མེད་ཀྱི་སྒྲ་རིག་སྔགས་ཨོཾ་དང་སྭཱ་ཧཱ་ས་མཚོན་པ་མཐའ་ཡས་པར་ཤར་བས། སྡིག་པ་ཞི་བ་སོགས་སེམས་ཅན་གྱི་དོན་མཛད་པ་སྟེ་འབྲས་བུ་ལ་སྦྱར་བའོ། །

[Block 123 [HEADING]]
### ཕྱག་འཚལ་བཅུ་དྲུག་པ། ^1-16-0

[Block 124 [HEADING]]
#### ཚིག་འགྲེལ། ^1-16-1-0

[Block 125]
ཚིགས་བཅད་བཅུ་དྲུག་པ་ཕྱག་འཚལ་ཀུན་ནས་སོགས་ལ། གྲུབ་པ་རིག་པ་འཛིན་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་ཏིང་ངེ་འཛིན་དང་རབ་ཏུ་དགའ་བའི་ཐུགས་དང་ལྡན་པ་རྣམས་ཀྱིས་ཀུན་ནས་བསྐོར་ཞིང་། གཞན་འཕྲུལ་དབང་བྱེད་ཀྱི་བདག་པོ་སྡིག་ཏོ་ཅན་ལ་སོགས་པ་སེམས་ཅན་རྣམས་ལ་ཉེ་བར་འཚེ་བའི་དགྲའི་ལུས་རབ་ཏུ་འགེམས་པ་སྟེ་འཐོར་བར་མཛད་པ། ཡི་གེ་བཅུ་པའི་ངག་སྟེ་སྔགས་ཀྱི་བཀོད་པ་ལས་བྱུང་བའི་ལྷ་མོ་ཁྱོད། རིག་པ་སྟེ་རིག་སྔགས་ཧཱུྃ་ཡིག་ལས་བྱུང་བའི་སྒྲོན་མ་འོད་ཟེར་འབར་བའི་སྐུ་ཅན་ཉིད་མའོ། །

[Block 126]
འདིས་ནི་སྒྲོལ་མ་ཁྲོ་མོ་ལ་ས་བོན་ཧཱུྃ་དང་བསྙེན་པའི་སྔགས་ཡི་གེ་བཅུ་པར་བསྟན་ནོ། །

[Block 127 [HEADING]]
#### ངེས་དོན། ^1-16-2-0

[Block 128]
ངེས་དོན་ནི།  སྟོང་གཟུགས་ཕྱག་རྒྱ་ཆེན་པོའི་འོད་ཟེར་གྱིས་བསྐོར་བའི་རབ་དགའ་སྟེ་གཡོ་མེད་བདེ་བས། དགྲ་སྟེ་མ་དག་པའི་སྣང་བའི་ལུས་འཇོམས་པར་བྱེད་དོ། །ཅེས་པ་བསམ་གཏན་གྱི་ཡན་ལག་དང་། ཡི་གེ་བཅུ་ནི་གཡས་གཡོན་གྱི་དཀྱིལ་འཁོར་བཅུའི་ཆ་ཤས་འགག་པ་ལས་ཐོབ་པའི་རྟགས་བཅུའོ། །

[Block 129]
དེ་ཡང་ཡི་གེས་རླུང་མཚོན་ཞིང་། ཡི་གེའི་སྐད་དོད་ཨ་ཀྵར་འགྱུར་བ་མེད་པ་སྟེ། ཆོས་དབྱིངས་འགྱུར་བ་མེད་པའི་སྣང་བ་བཅུའམ། དེ་མཐོང་བ་ལས་བྱུང་བའི་བདེ་བ་མི་འགྱུར་བའི་ཆ་ཤས་བཅུའོ། །

[Block 130]
རིག་པ་ཧཱུྃ་གི་བརྡས་ནི། ཧཱུྃ་ཆ་ལྔ་པས་ཡེ་ཤེས་ལྔ་མཚོན་ཏེ་ཡེ་ཤེས་ལྔའི་རང་བཞིན་གྱི་ཐིག་ལེ་ཁམས་གསུམ་གྱི་གཟུགས་བརྙན་དང་བཅས་པའོ། །

[Block 131]
དེ་ཡང་རྟགས་བཅུ་པོ་དེ་དག་གི་ཆོས་སུ་འཇོག་སྟེ་རླུང་དབུ་མར་བཀང་བ་ལས་བྱུང་བས་སོ། །

[Block 132]
དེ་ལ་མཉམ་པར་འཇོག་པ་ནི་དོན་དམ་པའི་རིག་སྔགས་ཆེན་པོ་སྟེ་སྒྲོན་མ་ནི་སྟོང་གཟུགས་ཀྱི་གསལ་སྣང་ངོ། འདི་ནི་སོ་སོར་སྡུད་པའི་རྣལ་འབྱོར་རོ། །

[Block 133 [HEADING]]
### ཕྱག་འཚལ་བཅུ་བདུན་པ། ^1-17-0

[Block 134 [HEADING]]
#### ཚིག་འགྲེལ། ^1-17-1-0

[Block 135]
ཚིགས་བཅད་བཅུ་བདུན་པ་ཕྱག་འཚལ་ཏུ་རེ་སོགས་ཀྱི་དོན་ནི། ཏུ་རེ་ཞེས་པ་མྱུར་མ་སྟེ། འགོ་བའི་དོན་མྱུར་དུ་སྤྱོད་པའི་ལྷ་མོས་ཁྲོ་བའི་ཚུལ་གྱིས་ཞབས་གཉིས་ནི་བརྡབས་པས། རིའི་རྒྱལ་པོ་རི་རབ་དང་། མནྡ་ར་ཞེས་བྱ་བའི་ར་དང་། རི་བོ་གངས་ཅན་ཞེས་བྱ་བ་དང་དབང་ཕྱུག་ཆེན་པོ་གནས་པའི་རི་རྣམས་དང་བཅས་པའི། འཇིག་རྟེན་གསུམ་སྟེ་ས་འོག་ས་སྟེང་ས་བླ་རྣམས་ཀྱང་གཡོ་བར་བྱེད་དོ། །

[Block 136]
བོད་དཔེ་ཕལ་ཆེར་ལས།

[Block 137]
འབིགས་བྱེད་ཅེས་འབྱུང་བ་ལྟར་ན། རིའི་རྒྱལ་པོ་འབིགས་བྱེད་དེ། གཞུང་འདིའི་རྒྱ་སྐད་མཐོང་པ་རྣམས་ན། ཀཻ་ལ་ཤ་ཞེས་པར་སྣང་སྟེ། དེ་ལྟར་ན་གངས་རི་ཞེས་འདོན་པ་དང་མཐུན་མོད། དཔེ་སྣ་ཚོགས་པ་སྣང་བའི་ཕྱིར། གཅིག་ཏུ་ངེས་བཟུང་བ་དཀའ་བས་གཉིས་ཀ་ལྟར་མི་འགལ་བར་བྱའོ། །

[Block 138]
ཧཱུྃ་གི་རྣམ་པའི་ཞེས་པ་ཧཱུྃ་ཀ་རེ་སྟེ་ཧཱུྃ་གི་ཡི་གེའོ། །

[Block 139]
འཇིག་རྟེན་གསུམ་ན་ཞེས་པ་གཉིས་པའི་དོན་ལ་བདུན་པའི་ཚིག་སྟེ་གསུམ་པོ་ལ་གཡོ་བའི་བྱེད་པ་འཇུག་པའོ། །

[Block 140]
འཇིག་རྟེན་གསུམ་སྐྱོད་པར་གྱུར་ན། རི་རབ་སོགས་སྨོས་པས་ཅི་ཞིག་བྱ་ཞེ་ན། སྤྱིར་འཇིག་རྟེན་གསུམ་སྐྱོད་པར་གྱུར་ཡང་། ལྷ་མཐུ་བོ་ཆ་དག་གནས་པའི་གནས་ཀྱི་ཁྱད་པར་དེ་རྣམས་གཡོ་བར་མི་འགྱུར་བ་ཡང་སྲིད་པས། འཕགས་མ་ཉིད་མཐུ་ཆེ་བའི་དོན་དུ་སྨོས་སོ། །

[Block 141 [HEADING]]
#### སྦས་དོན། ^1-17-2-0

[Block 142]
སྦས་དོན་ནི། རི་རབ་ནི་ཚངས་པའི་རུས་པ། རི་གཞན་གཉིས་ནི་ཡིད་བཟང་མ་དང་དུང་ཅན་མ། གཡོ་བ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས་ཡོངས་སུ་གང་བ། འཇིག་རྟེན་གསུམ་ནི་སྟེང་འོག་གི་དབྱེ་བས་རྩ་གསུམ་གསུམ་དྲུག་གོ། །

[Block 143]
ཧཱུྃ་གི་བརྡས་ནི། ཐུགས་རྡོ་རྗེའི་རྩ་ཨ་ཝ་དྷཱུ་ཏི་སྟེ་རྩ་ཐམས་ཅད་ཀྱི་ས་བོན་ནུས་པ་དེར་ཐིམ་པའོ། །

[Block 144 [HEADING]]
### ཕྱག་འཚལ་བཅོ་བརྒྱད་པ། ^1-18-0

[Block 145 [HEADING]]
#### ཚིག་འགྲེལ། ^1-18-1-0
--- END BLOCKS ---
