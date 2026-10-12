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

[Block 286]
ཕཊ་ནི་གསོད་པའོ་ཞེས་བྱ་བ་ནི་ཕཊ་ཆེ་གེ་མོ་མཱ་ར་ཡ་ཕཊ་ཅེས་པའོ།།

[Block 287]
འདི་ནི་གསོད་པའི་སྔགས་ཏེ་ཞི་བ་ལ་སོགས་པའི་སྔགས་ལ་ཡང་ཐ་མར༌[^107]གསད་པའི༌[^108]སྔགས་བྱིན་ན་གང་གི་ཚེ་ཡི་གེ་ཕཊ་དེ། དེའི་ཚེ་གསོད་པའི་དོན་གྱི་བྱ་བ་བྱེད་དོ།།

[Block 288]
ཡེ་ཤེས་ཀྱི་རིམ་པ་ཞེས་བྱ་བ་ནི་ཡེ་ཤེས་སེམས་དཔའ་བཅུག་པའི་རིམ་པས་རྡོ་རྗེ་མི་བསྐྱོད་པར་བསྒོམས་ནས། སྤྱན་ལ་སོགས་པའི་ལྷ་མོ་བཞི་པོ་རྣམས་བཏོན་ཏོ།།

[Block 289]
[^109]དཀྱིལ་འཁོར་ལྔའི་བདག་ཉིད་དུ་སྐད་ཅིག་གིས་བསྐྱེད་ལ་རྣལ་འབྱོར་པར་བསྒོམ་པར་བྱའོ།།

[Block 290]
སྔགས་དང་ཕྱག་རྒྱས་ལེགས་པར་བརླབས་པའི༌[^110]བུད་མེད་བཞི་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་རིག་པའི་བརྟུལ་ཞུགས་ཁོ་ན་བཤད་པ་ཡིན་ནོ།།

[Block 291]
རང་གི་སྙིང་གའི་པདྨོ་ལ་སོགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་པདྨའི་སྟེང་དུ་ཡེ་ཤེས་སེམས་དཔའོ།།

[Block 292]
དེའི་སྟེང་དུ་ཡི་གེ་ཧཱུཾ་གནས་པར་བསྒོམས་ཏེ། དེ་ཉིད་དཀྱིལ་འཁོར་གྱི་བདག་པོ་རྡོ་རྗེ་འཆང་དང་མི་ཕྱེད་པར་ལྷག་པར་མོས་པར་བྱས་ལ་དེ་ནས་གང་ཡང་རུང་བར་བྱས་ནས། ཡེ་ཤེས་སེམས་དཔའ་དགུག་པར་བྱ་སྟེ། ནང་གི་བདག་ཉིད་ཀྱིས་འབད་པར་བྱའོ།།

[Block 293]
དེ་ཡང་སེམས་དཔའ་ལས་སྐྱེས་པའི་སྣ་ཚོགས་རྡོ་རྗེ་ལ་གནས་པ་འོག་ནས་འཆད་པའི་ཞལ་གྱི་པདྨ་བཞད་བག་ཅན་དུ་གྱུར་པའི་ཞལ་དང་ལྡན་པར་བསྒོམ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ།།

[Block 294]
ད་ནི་ཕྱག་རྒྱ་གཅིག་དང་ཞེས་བྱ་བ་ནི་རྡོ་རྗེ་སེམས་དཔའ་འབའ་ཞིག་གི་རྣལ་འབྱོར་གྱི་ཕྱག་རྒྱ་གཅིག་ཙམ་ཞིག་དང་ལྷན་ཅིག་ཏུ་རིག་པའི་བརྟུལ་ཞུགས་དཔྱད་པར༌[^111]བྱ་བའོ།[^112] །ཛ༌[^113]ནི་ཛ་ར་ཡུ་སྟེ་བུད་མེད་ཀྱི་ཤ་མའོ།།

[Block 295]
སུ་ནི་སུ་བརྞ་སྟེ་གསེར་ཏི་ནི་ཏམ་པ་སྟེ་ཟངས་མའོ།།

[Block 296]
རུ་ནི་རུ་པ་ན་རུ་སྟེ་དེ་དག་གིས་བཀྲི་བར༌[^114]བརྗོད་དོ།།

[Block 297]
ནུས་པ་བསྐྱེད་པའི་ཕྱིར་དང་ཞེས་བྱ་བ་ནི་མཐུ་ཆེན་པོ་བསྐྱེད་པའི་ཕྱིར་ནའོ།།

[Block 298]
དེ་ལྟར་མངོན་དུ་བྱས་པ་ལ་སྤྱོད་པའི་ཞེས་བྱ་བ་ནི་སྐྱིལ་མོ་ཀྲུང་བཅས་པའོ།།

[Block 299]
ཡང་དག་པར་བསྐུལ་ལ་ཐབས་ཀྱི་ཡེ་ཤེས་འབྱུང་བར་བྱས་ན་ཞེས་བྱ་བ་ནི་སེམས་སྙིང་རྗེའི་རང་བཞིན་ཅན་ཡེ་ཤེས་སེམས་དཔའ་བསྐྱེད་དེ་བསྒོམ་པར་བྱས་ནས་ཡི་གེ་བཞི་པོ་སྣོད་ལ་གསལ་པོར་བསམ་ཤིང་བལྟའོ།།

[Block 300]
གསུང་གི་རྡོ་རྗེ་སྙིང་གའི་ཕྱོགས་སུ་བབས་ནས་ཞེས་བྱ་བ་ནི་གསུང་གི་རྡོ་རྗེའི་འོད་ཟེར་ཐུགས་རྡོ་རྗེ་ལ་བབས་ཏེ་བསྐུལ་བས་སོ།།

[Block 301]
འདི་ལྟ་བུར་བསྒྲུབ་བྱ་དང་པོར་བསམས་ནས་ཞེས་བྱ་བ་ནི་བསྒྲུབ་བྱ་ཐོབ་པ་ལ་སོགས་པ་དང་ལྡན་པའི་མི་བསྐྱོད་པར་བསམས་པའི༌[^115]བསྒྲུབ་བྱ་དེས་ཐོབ་པ་ལ་སོགས་པས་རང་སངས་རྒྱས་ལ་སོགས་པ་ལ་རབ་ཏུ་བསྣུན་པར་བལྟའོ།།

[Block 302]
དེ་ནས་བསྒྲུབ་བྱ་དེའི་མིག་ལ་སོགས་པ་རང་གི་སའི་སྙིང་པོ་ལ་སོགས་པ་ལ་བཅུག་ལ་བསྒྲུབ༌[^116]བྱ་དེ་བསྒྲུབ་པར་བྱའོ།།

[Block 303]
ཡི་གེ་ཧྲིའི་འོད་ཟེར་གྱིས་ཞེས་བྱ་བ་ནི་ཁ་ན་གནས་པའི་ཡི་གེ་ཁཾ་དེའི་སྟེང་གི་ནང་རོལ་དཔྲལ་བའི་ཐད་ཀར་ཡི་གེ་ཧྲི་བལྟས་ལ་དེའི་འོད་ཟེར་གྱིས་དུག་རྣམས་དྲངས་ཏེ་བྲིས་པའི་སྦྲུལ་གྱི་དཔྲལ་བར་ཞུགས་ནས། ཁ་ན་གནས་པའི་ཡི་གེ་ཁཾ་གི་ནང་དུ་དུག་དེ་འོང་བར་བསམ་མོ།།

[Block 304]
བསྒྲུབ་པར་བྱ་བས་མཉེས་པར་བྱ་བ་ཞེས་བྱ་བ་ནི་བསྒྲུབ་བྱའི་རང་གི་ཡི་དམ་གྱི་ལྷ་སྟེ་དེ་ཕུར་བུས་གདབ་པོ།།སྣོད་ཀྱི་སྙིང་གར་གནས་པ་ཞེས་བྱ་བ་ནི་བསྒྲུབ་བྱ་གང་ཡིན་པའི་ལུས་སྤོ༌[^117]ལ་དུག་སྤོ༌[^118]བར་བྱས་པ་ལ་དེ་ནས་སྙིང་གར་རོ།།

[Block 305]
ཡི་གེ་ཧཱུཾ་ཞེས་བྱ་བ་ནི་སྔར་གྱི་སྐུ་རྡོ་རྗེའི་རང་བཞིན་ཡི་གེ་ཨོཾ་གྱིས་དུག་གསོ་བར་བྱ་བ་དང་སྤོ་བ་དེ་བཞིན་དུ་འདིར་ཡང་ཐུགས་རྡོ་རྗེའི་རང་བཞིན་ཡི་གེ་ཧཱུཾ་གིས་བྱ་བར་བརྗོད་དོ།།

[Block 306]
རྐང་པའི་འོག་ནི་སྙིང་གའི་དབུས་དང་རྐང་མཐིལ་གྱི་དབུས་སོ།།

[Block 307]
དེ་ལྟར་སྡུད༌[^119]པའི་ཚུལ་གྱིས་ཞེས་བྱ་བ་ནི་དེ་ལྟ་བུར་ཐམས་ཅད་འདིས་གཅིག་ཏུ་བསྡུས་པར་བྱས་ཏེ། སྐྱུགས་པར་བལྟ་བར་བྱའོ།།

[Block 308]
ཧྲི་བསྒོམས་ནས་ཞེས་བྱ་བ་ནི་འདབ་མ་རྣམས་ལ་གནས་པའི་ཡི་གེ་ཧྲིའི་འོད་ཟེར་གྱིས་དུག་རྣམས་མཉེས་ཤིང་བསྡུས་ནས་དྲངས་ཏེ། ཡི་གེ་ཨ་ལས་ཞུགས་པས་ཡི་གེ་ཨ་རྒྱས་པར་གྱུར་པས་བསྡུས་ནས་ས་ལ་བཏབ་པར༌[^120]བྱའོ།།

[Block 309]
མཚན་མ་དང་བཅས་པས་ཞེས་བྱ་བ་ནི་སྔགས་ལ་མཆོག་ཏུ་གཞོལ་བས་སྐྱེས་པ་དང་བུད་མེད་ལ་སོགས་པ་མཐོང་བའོ།།

[Block 310]
མཚན་མ་མེད་པ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ལས་འདས་པའི་དངོས་གྲུབ་ཀྱི་མཚན་མ་སྟེ་ནང་ལ་མཆོག་ཏུ་གཞོལ་བས་བྱང་ཆུབ་ཡེ་ཤེས་མཆོག་ཅེས་བྱ་བ་ལ་སོགས་པ་མཐོང་བར་འགྱུར་རོ།།

[Block 311]
དགའ་བ་ལྔ་ཞེས་བྱ་བ་ནི་དབང་པོ་ལྔ་པོ་དགའ་ཞིང་བདེ་བའོ།།

[Block 312]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་བཅོ་ལྔ་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 313 [HEADING]]
## ལེའུ་བཅུ་དྲུག་པ། ^16-0

[Block 314]
འབའ་ཞིག་ཏུ་བྲིས་ཤིང་གཞག་པར༌[^121]བྱའོ་ཞེས་བྱ་བ་ནི་བདག་པོ་ཕྱག་རྒྱ་དང་ལྡན་པར་དབུས་སུ་གཞག༌[^122]ལ་གཞན་མི་བསྐྱོད་པ་ལ་སོགས་པ༌[^123]ནི་ཤར་ལ་སོགས་པའི་ཕྱོགས་སུ་ཕྱག་རྒྱ་ཡངས་པར་བྲིའོ་ཞེས་བྱ་བའི་དོན་ཏོ།།

[Block 315]
པདྨས་བརྒྱན་པ་བྲིས་ལ་ཞེས་བྱ་བ་ནི་པདྨའི་དཀྱིལ་འཁོར་ཟླ་བའི་དབྱིབས་ལྟ་བུར་པདྨའི་ཕྲེང་བས་བརྒྱན་པ་སྟེ། ལྷ་དེ་ཁོ་ན་ཉིད་ཀྱི་ཕྱིར་ལྷའི་བདག་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་དུ་བྱའོ།།

[Block 316]
སྔགས་ལ་མཆོག་ཏུ་གཞོལ་བ་སྟེ་དེས་ནི་ཞེས་བྱ་བ་ནི་འཕགས་པ་དེ་ཁོ་ན་ཉིད་བསྡུས་པ་ལས༌[^124]གསུངས་པའི་ཚུལ་ཤེས་པས་རྣལ་འབྱོར་ཙམ་བསྐྱེད་པ་ཡིན་ཡང་གསང་བ་འདུས་པ་དང༌[^125]མཚུངས་པར་བྱ་བ་ནི་མ་ཡིན་ནོ།།

[Block 317]
ཡང་དབང་པོ་གཉིས་ཀྱི་སྦྱོར་བ་ཞེས་བྱ་བ་ནི་ཇི་ལྟ་བའི་ཕྱི་རོལ་གྱི་མེ་ལ་ལྷག་མ་ལ་སོགས་པའི་སྲེག་རྫས་རྣམས་ཕྱིའི་སྦྱིན་སྲེག་བྱེད་པ་དེ་བཞིན་དུ་སྙོམས་པར་འཇུག་པའི་སྦྱོར་བས་ཀྱང་ནང་གི་བདག་ཉིད་ཀྱི་སྦྱོར་བས་ནང་གི་སྦྱིན་སྲེག་བྱ༌[^126]སྟེ། དབབ་པའི་རྡོ་རྗེས་ཞེས་བྱ་བ་ནི་འོད་དཔག་མེད་ཀྱི་རང་གི་ངོ་བོས་ཕབ་ལ་གཟུང༌[^127]ངོ་།།འདི་ཡིས་ནི་སྔོན་དུ་བརྗོད་པའི་དབབ་པའི་ཆོ་ག་གསལ་བར་བྱེད་དོ།།

[Block 318]
དབབ་པ་བྱས་ནས་མི་བསྐྱོད་པ་ལ་སོགས་པས་བསྒྲུབ་བྱའི་ལུས་དང་ངག་དང་ཡིད་ལ་བྱིན་གྱིས་བརླབ་པར༌[^128]མཛད་དོ།།

[Block 319]
ཨ་ཁཾ་བི་ར་ཧཱུཾ་ཞེས་བྱ་བ་འདིས་ནི་སློབ་མ་དཀྱིལ་འཁོར་དུ་གཞུག་པར་བྱའོ།།

[Block 320]
སངས་རྒྱས་ཀུན་གྱི་ཞེས་བྱ་བ་ནི་རྡུལ་ཚོན་གྱི་དཀྱིལ་འཁོར་ལ་བསྒྲུབ་པ་བྱས་ནས་ནང་གི་མཆོད་པ་བྱ་བ་སྟོན་ཏོ།།
--- END BLOCKS ---
