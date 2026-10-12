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
[Block 246]
ཕུན་སུམ་ཚོགས་པ་ནི་བསྐྱེད་པའོ།།

[Block 247]
བདག་ནི་ཞེས་བྱ་བ་ནི་བདག་དེ་བཞིན་གཤེགས་པ་ཆེ་གེ་མོའི་ཞེས་ང་རྒྱལ་དང་ལྡན་པར་བྱའོ།།

[Block 248]
བསྒྲུབ་བྱའི་ལུས་རང་གི་གཞིར་གྱུར་པ་ཞེས་བྱ་བ་ནི་བཞི་པའི་བསྒྲུབ་བྱའི་བདག་ཉིད་སྟོང་པར་བསམ་པའོ།།

[Block 249]
ནམ་མཁའི་དབྱིངས་ཀྱི་དབུས་ཏེ་ཞེས་བྱ་བ་ནི་རྡོ་རྗེ་སེམས་དཔའི་ཤེས་རབ་ཀྱི་ཆོས་འབྱུང་བ་ལའོ།།

[Block 250]
དེར་ཡི་གེ་ཨོཾ་བལྟས་ལ་རྡོ་རྗེ་སེམས་དཔའ་ནང་དུ་བཅུག་ནས་བདག་ཉིད་བསྒོམས་ཏེ། བདག་ཉིད་ཀྱི་སྙིང་གར་བསྒྲུབ་བྱ་དགོད་པར་བྱ་བའོ།།

[Block 251]
དེའི་མདུན་དུ་སྟེ་ཞེས་བྱ་བ༌[^97]ནི་སྣང་བ་མཐའ་ཡས་ཀྱི་མདུན་དུ་སྟེ། བྱང་ན་གནས་པའི་དོན་ཡོད་གྲུབ་པའོ།།

[Block 252]
དེ་དག་ལ་ཞེས་བྱ་བ་ནི་མི་བསྐྱོད་པ་དང་སྣང་བ་མཐའ་ཡས་དག་གི་གཙོ་བོ་དོན་ཡོད་གྲུབ་པ་སྟེ། དེ་མི་བསྐྱོད་པ་ལས་བྱུང་བའི་དོན་ཡོད་གྲུབ་པའོ།།

[Block 253]
དེའི་སྙིང་གར་འདོད་པ་དགོད་དེ། ཟླ་བ་དང་རྡོ་རྗེ་ལ་སོགས་པ་ལ་ལྟོས་པ་མེད་པ་ནི་ཟླ་བ་དང་ཉི་མ་དང་ས་བོན་ལ་སོགས་པ་ལ་མི་ལྟོས་པར་ཟུང་དུ་འཇུག་པས་བསྐྱེད་པ་ལ་བཤད་དོ།།

[Block 254]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་བཅུ་གསུམ་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 255 [HEADING]]
## ལེའུ་བཅུ་བཞི་པ། ^14-0

[Block 256]
སྔགས་རྣམ་པ་བཞིའི་ཞེས་བྱ་བ་ནི་སྦྲུལ་ལ་སོགས་པའི་སྔགས་བཟླས་པས་དྲག་པོའི་ལས་དང་རིམས་ལ་སོགས་པ་ཞི་བར་བྱ་བའི༌[^98]ལས་སོ།།

[Block 257]
སྙིང་གའི་ཕྱོགས་སུ་ཞེས་བྱ་བ་ནི་སྭཱ་ཧཱ་སྔོན་དུ་སོང་བའི་ཆེ་གེ་མོ་ཨཱ་ཀཱཪྵ་ཡ་ཧྲི་ཞེས་བྱ་བའི་སྔགས་དང་སྤེལ་བ་བྲིས་ཏེ་སྙིང་གར་གཞུག༌[^99]པའོ།།

[Block 258]
ཉི་མའི་དཀྱིལ་འཁོར་གཉིས་ཀྱི་དབུས་སུ་ཚུད་པར་བྱས་ལ་ཞེས་པ་ནི་བསྒྲུབ་བྱ་སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་དུ་བསྒོམས་ཏེ། དེའི་ཏིང་ངེ་འཛིན་གྱི་སེམས་དཔའི་འོད་ཟེར་གྱིས་བསྒྲུབ་བྱ་བཀྲུ་བར་བྱ་བར༌[^100]བསམ་མོ།།

[Block 259]
ལག་མཐིལ་གཉིས་སུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གསལ་ལོ།།

[Block 260]
དེའི་དེ་ཁོ་ན་ཉིད་ནི་གཞན་དུ་མི་འགྱུར་བ་ཉིད་ཅེས་བྱ་བ་ནི་རྫས་དང་བཟླས་བརྗོད་ལ་ལྟོས་པ་མེད་པར་བསམ་གཏན་ཙམ་གྱིས་འགྲུབ་པ་ལ་བྱའོ།།

[Block 261]
སངས་རྒྱས་ནི་སྟོན་པའོ་ཞེས་བྱ་བ་ནི་རྡོ་རྗེ་འཛིན་པ་ལ་སོགས་པའི་ཕྱག་རྒྱ་རྣམ་པ་གཉིས་པོའི་སྦྱོར་བ་ཅན་དག་སྟེ། བསྐྱེད་པ་དང་རྫོགས་པའི་རིམ་པ་རྣམ་པ་གཉིས་པོ་ཅན་ནོ།།

[Block 262]
ལས་གྱི་ཚོགས་ལ་མཁས་པ་རྣམས་ཀྱང་ཞེས་བྱ་བ་ནི་རྒྱུད་གཞན་གྱི་ལས་ཀྱི་ཚོགས་རྣམས་མཐོང་ཞིང་བྱེད་པ་ལ་མཁས་པ་རྣམས་ཀྱང་ངོ་།།མིའི་རུས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་མིའི་རུས་པའི་ཕུང་པོ་ནི་རྣམ་པར་སྣང་མཛད་ཀྱིའོ།།

[Block 263]
སེང་ལྡེང་གི་ཕུར་པ་ནི་སྣང་བ་མཐའ་ཡས་ཀྱིའོ།།

[Block 264]
ལྕགས་ཀྱི་ཕུར་པ་ནི་མི་བསྐྱོད་པའིའོ།།

[Block 265]
ཙནྡན་ལ་སོགས་པའི་ཕུར་པ་ནི་དོན་ཡོད་གྲུབ་པ་དང་། རིན་ཆེན་འབྱུང་ལྡན་གྱིའོ།།

[Block 266]
གནས་ལས་ཉམས་པར་འགྱུར་བ་ནི་གནས་འདོར་བའོ།།

[Block 267]
དེ་བཞིན་དུ་ངག་མནན་པ་དང་སེམས་མནན་པ་ཡང་བྱ་བ་ཡིན་ནོ།།

[Block 268]
ཡང་ན་གསང་བ༌[^101]འགྲུབ་པར་འགྱུར་རོ།།

[Block 269]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་བཅུ་བཞི་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 270 [HEADING]]
## ལེའུ་བཅོ་ལྔ་པ། ^15-0

[Block 271]
དཀྱིལ་འཁོར་གྱི་དབུས་སུ་ཞེས་བྱ་བ་ནི་མི་བསྐྱོད་པའི་རྣལ་འབྱོར་པས་ཤེས་རབ་མ་དང་རིགས་ལྔ་དང་ལྡན་པར་བྱས་ཏེ་གནས་པའོ།།

[Block 272]
འཁྱུད་པར་བྱས་པ་ནི་དཀྱིལ་འཁོར་གྱི་དབུས་སུ་རོལ་པར་བྱ་བའོ།།

[Block 273]
ནུབ་ནས་ཞེས་བྱ་བ་ནི་ཐུན་ཚོད་དག་འདས་ནས་ཟླ་བ་འཆར་བའི་དུས་ཏེ། ནམ་ཕྱེད་ཀྱི་དུས་སུ་དབང་བསྐུར་བ་ཐོབ་པར་བྱ་བའོ།།

[Block 274]
འགྲུབ་ཅེས་བྱ་བ་ནི་ཉི་མ་འཆར་བའི་དུས་སུ་སྟེ། ཕྱི་རོལ་གྱི་སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་ཀྱི་སྣོད༌[^102]དུ་གྱུར་པའོ།།

[Block 275]
རང་བཞིན་གྱིས༌[^103]འོད་གསལ་བར་སྔོན་དུ་འགྲོ་བས་ཞེས་བྱ་བ་ནི་འོད་གསལ་བ་མདུན་དུ་དྲན་པར་བྱས་ནས། ཐབས་དང་ཤེས་རབ་སྙོམས་པར་ཞུགས་ཏེ་སྣང་བ་ལ་སོགས་པ་ནང་གི་བདག་ཉིད་ཅན་རྣམས་ཡང་དག་པར་བསམ་པར་བྱ་བའོ།།

[Block 276]
ཉི་མ་ནི་སྣང་བ་ཉེ་བར་ཐོབ་པའོ།།

[Block 277]
འདི་སྤེལ་བ་ནི་བརྟན་པར་བྱེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྭཱ་ཧཱ་སྔོན་དུ་འགྲོ་བའི་ཆེ་གེ་མོ་སྟྭཾ་བྷ་ཡ་ཕཊ་ཅེས་པའོ།།

[Block 278]
དམ་ཚིག་ཆེན་པོའི་ཁྲོ་བོ་ཞེས་པ་ནི་གཤིན་རྗེ་མཐར་བྱེད་དོ།།

[Block 279]
སྒྲུབ་པོ་གཞན་ལས་ལེན་པ་ཞེས་པ་ལ་སྒྲུབ་པོ་ནི་དགུག་པ་ཤེས་པའི་སློབ་དཔོན་ལས་ཀྱང་ངོ་།།གནོད་པ་འདི༌[^104]གཅོད་པར་འདོད་པ་ཡི་ཞེས་བྱ་བ་ནི་རྣམ་པར་སྣང་མཛད་དང་རྡོ་རྗེ་འཛིན་པ་ནས་ཁྲོ་བོའི་རྣལ་འབྱོར་པ་གང་ཡང་རུང་བའི༌[^105]བར་གྱིས་དེ་ཟློག་པར་བྱེད་ན་ཚེ་ཟད་ཅིང་གཏུགས་པར་འགྱུར་བ་ཡིན་ནོ།།

[Block 280]
ལས་དེ་བརྩམས་པ་ནས་ཞེས་བྱ་བ་ནི་བགེགས་བྱ་བའི་ལས་བརྩམས་ནས་སོ།།

[Block 281]
ཨི་དཾ་དི་བ༌[^106]ཡ་ཞེས་བྱ་བ་ནི་གསེར་ལ་སོགས་པ་བྱིན་ཅིག་ཧྲི་སྭཱ་ཧཱ་ཞེས་བྱ་བའོ།།

[Block 282]
རླུང་ལ་སོགས་པ་ཞེས་བྱ་བ་ནི་རླུང་གི་དཀྱིལ་འཁོར་ལ་སོགས་པའོ།།

[Block 283]
གལ་ཏེ་བག་མེད་པས་བྱུང་བར་གྱུར་ན་དེའི་ཚེ་མཆེ་བའི་ཕྱག་རྒྱ་ཞེས་པ་ལ། ཕྱག་རྒྱ་ནི་མཆེ་བ་ཚར་གཅོད་པའི་ཕྱག་རྒྱ་སྟེ་རྟ་མགྲིན་ནོ།།

[Block 284]
དེའི་སྦྱོར་བས་བགེགས་ཀྱི་ལས་རྣམས་མེད་པར་བྱའོ།།

[Block 285]
དེ་ལྟར་མ་བྱས་ན་བྱ་བ་རྣམས་མི་འགྲུབ་སྟེ། དེའི་ཚེ་དཀྱིལ་འཁོར་ལ་སོགས་པ་རྣམས་འཇིག་ཅིང་གཅོད་པར་འགྱུར་རོ།།
--- END BLOCKS ---
