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
[Block 631]
འདིར་བསྐྱེད་པའི་རིམ་པའི་རྒྱུར་ཇི་ལྟར་འགྱུར་ཞེ་ན།

[Block 632 [VERSE]]
དེ་ཡང་སྙིང་པོ་དང་ལྷའི་སྔགས་སོ། །
དེ་ལ་སྙིང་པོ་ནི་བསྐྱེད་པའི་རིམ་པའི་རྒྱུའོ། །
ལྷའི་སྔགས་ནི་གསལ་བར་བྱེད་པའི་རྒྱུའོ། །

[Block 633]
ལས་ཀྱི་སྔགས་ནི་ནུས་པ་ཐོབ་པར་བྱེད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་སོམ་ཉི་མི་བྱའོ། །

[Block 634]
དང་ལ༌[^210]གཏོར་མའི་སྔགས་བསྟན་པ་ཡང་གཏོར་མ་ནི་ལས་རྣམས་སྒྲུབ་པའི་སྔོན་དུ་འགྲོ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 635]
དེ་ལ་ཨོཾ་ཨ༌[^211]ཀཱ་རོ་ནི༌[^212]ཝ་ར་ཎ་སྟེ་ཨ་ཨརྠ་ནི་དོན། །ཨུ་ཧ་བི་ག་ཏ་དོན་དང་བྲལ༌[^213]བའོ། །

[Block 636]
མ་མ་ནི་སེམས་ཙམ། ཨ་ཨ་ཀར་ཎ་རྣམ་པ། ཨུ་ཧ་བི་ཀ་ཏ་རྣམ་པ་དང་བྲལ་བ། མ་མ་ནི༌[^214]སེམས་ཙམ་སྟེ་རྣམ་པས་སྟོང་པའི་སེམས་ཙམ་མོ། །

[Block 637]
ཡང་ཨོཾ་ནི་ཨ༌[^215]སྟེ་བརྗོད་བྱའི་ཆོས་གཟུགས་ནས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་བར་རྗོད་བྱེད་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་ཐམས་ཅད་མ་སྐྱེས་པར་སྟོན་པའོ།[^216] །ཨ་ཨ། དེ་ལྟར་ན་དེ་ཡང་ཨོཾ་ནི་ཁས་ལེན་པའོ། །

[Block 638]
སརྦ་དྷརྨ་ནི་ཆོས་ཅན་ནོ། །

[Block 639]
ཨ་ཀཱ་རོ་མུ་ཁཾ་ནི་ཨའི་སྒོ་ཅན་དུ་དམ་བཅའ་བའོ། །

[Block 640]
ཨཱདྱ་ནུཏྤནྣ་ཏྭཱ་ཏ་ནི་ཐོག་མ་ཉིད་ནས་མ་སྐྱེས་པའི་ཕྱིར་ཏེ། གཏན་ཚིགས་སོ། །

[Block 641]
ཨོཾ་ཨཱཿཧཱུཾ་ནི་བྱིན་གྱིས་བརླབ་པའོ། །

[Block 642]
ཕཊ་ནི་མི་མཐུན་པའི་བགེགས༌[^217]ཞི་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 643 [VERSE]]
སྭཱ་ཧཱ་ནི་ཞེས་པས་གཞི་འཛུགས་པའོ། །
འབྱུང་པོ་ཐམས་ཅད་ནི་འགྲོ་བ་ཀུན་ནོ། །

[Block 644]
གཏོར་མ་ནི་བ་ལིཾ་སྟེ། ཚོགས་གཉིས་དང་ལྡན་པས་སྟོབས་སུ་འགྱུར་བའོ། །

[Block 645]
དེའི་སྔགས་སོ། །

[Block 646]
དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་རྣམ་པར་སྣང་མཛད་དང་། སྣང་བ་མཐའ་ཡས་དང་རིན་ཆེན་འབྱུང་ལྡན་དང་། དོན་ཡོད་གྲུབ་པ་དང་མི་བསྐྱོད་པ་སྟེ་ས་བོན་གོ་རིམས་བཞིན་ནོ། །

[Block 647]
དེ་དག་ཀྱང་ཅི་ལ་དགོངས་ཤེ་ན། གཏུམ་མོ་འབར་བས༌[^218]ས་བོན་དང་དབང་བསྐུར་བའི་རིགས་ཀྱི་བདག་པོ་མཚོན་པའམ། ཧཱུཾ་གཅིག་བསྣན་ཏེ་ཧཱུཾ་གཉིས་ཀྱིས་རིགས་དྲུག་གི༌[^219]ང་རྒྱལ་གྱི་དུས་སུ་དགོས་པ་དང་། ཡི་གེ་དྲུག་གི་ཕྲ་མོའི་རྣལ་འབྱོར་བསྟན་པ་དང་། བདུད་རྩི་མྱང་བའི་ས་བོན་དང་། འབུམ་ཚོ་ལྔ་བསྡུས་པའི་དོན་ཁོ་ནའོ། །

[Block 648]
དེ་ཝ་པི་ཙུ་བཛྲ་ཧཱུཾ་ཧཱུཾ་ཧཱུཾ་ཕཊ་སྭཱ་ཧཱ། ཀྱེའི་རྡོ་རྗེའི་སྙིང་པོའོ། །

[Block 649]
ཉོན་མོངས་པ་དང་རྣམ་པར་རྟོག་པའི་ཟུག་རྔུ་ཞི་བས་དེ་ཝའོ། །

[Block 650 [VERSE]]
རས་བལ་ལྟར་འཇམ་པས་ན་པི་ཙུའོ། །
སྐུ་གསུང་ཐུགས་ཧཱུཾ་གསུམ་མོ། །
ཐུགས་སྐུལ་བར་བྱེད་པས་ན་སྙིང་པོའོ། །
ལྷན་ཅིག་སྐྱེས་པའི་རྟེན་ཅན།

[Block 651]
འབྲས་བུ་བདེ་བ་ཆེན་པོའི་སྐུ་བསྐྱེད་པའོ། །

[Block 652]
སྔགས་ཐམས་ཅད་ཀྱི་རྐང་པ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^220]ནི་དགྱེས་པའི་རྡོ་རྗེའི་སྔགས་རྣམས་ལ་ཨོཾ་ནི་དང་པོའོ། །

[Block 653]
ཧཱུཾ་ཕཊ་བར་དུའོ། །

[Block 654]
སྭཱ་ཧཱ་ཐ་མར་གཞག་པ་ནི་གདུལ་བྱ་རྣམ་པ་གསུམ་དུ་ངེས་ཏེ།

[Block 655 [VERSE]]
ཨོཾ་གྱིས་ནི་གདུལ་བྱ་ཞི་བའི་རྗེས་སུ་འཛིན་པའོ། །
ཧཱུཾ་ཕཊ་ཀྱིས་ནི་མ་རུངས་པ་ཚར་གཅོད་པའོ། །
སྭཱ་ཧཱ་ནི་བར་པ་རྗེས་སུ་འཛིན་པའོ། །

[Block 656 [HEADING]]
#### གྲོང་ཁྱེར་དཀྲུག་པ། ^1-2-1-0

[Block 657]
ཨ་ཀ་ཙ་ཊ་ཞེས་པ་ནི་གྲོང་ཁྱེར་དཀྲུག་པ་སྟེ་ཕྱི་དང་ནང་གིའོ། །

[Block 658 [HEADING]]
##### ཕྱི། ^1-2-1-1-0

[Block 659]
ཕྱི་ནི་ལས་ཀྱི་གཙོ་བོ་སྟེ། སྔོན་དུ་དགྱེས་པའི་རྡོ་རྗེའི་བསྙེན་པ་རྫོགས་ནས་ལས་ཀྱི་བསྙེན་པ་བྱ་སྟེ། སྙིང་ག་པདྨ་འདབ་མ་བརྒྱད་པའི་སྟེང་དུ་ཡིག་འབྲུ་བརྒྱད་པོ་བཀོད་ལ། འོད་ཟེར་སྤྲོ་བསྡུ་དང་བཅས་པས་བཟླས་པར་བྱའོ། །

[Block 660]
སྒྲུབ་པ་ནི་འོད་ཟེར་དེས་རྡོ་ཁབ་ལེན་གྱི་ཚུལ་དུ་གྲོང་ཁྱེར་བའི་ལུས་ངག་ཡིད་གསུམ་རྡོ་ཁབ་ལེན་གྱིས་བླངས་པ་བཞིན་དུ་འདུས་པར་བསམ་ཞིང་པུར་ཁྲོད་པ་ཧཱུཾ་ཕཊ་ཅེས་བཏགས་སོ། །

[Block 661]
ཌོཾ་བི་བ་ལྟ་བུའོ། །

[Block 662 [HEADING]]
##### ནང། ^1-2-1-2-0

[Block 663]
ནང་གི་ནི་སྙིང་གར་ཐིག་ལེ་བརྒྱད་བསྒོམས་ལ། དེ་ལ་སེམས་ཟིན་པ་དང་ཕྱིའི་དབང་པོ་དྲུག་གི་གྲོང་ཁྱེར་རྣམས་འདུས་པའོ། །

[Block 664]
གཞན་གྱི་སྔགས་ཀྱིས་མི་འགྲུབ་པོ་ཞེ་ན། དེའི་ཕྱིར༌[^221]རྣལ་འབྱོར་མ་རྣམས་ཀྱིས་ཀྱང་ངོ་། །

[Block 665 [HEADING]]
#### རིམ་དང་ཅིག་ཅར་བའི་བཟླས་པ། ^1-2-2-0

[Block 666]
དེ་ལ་གཉིས་ཏེ། རིམ་དང་ཅིག་ཅར་བའི༌[^222]བཟླས་པའོ། །

[Block 667 [HEADING]]
##### རིམ་གྱིས་པ། ^1-2-2-1-0

[Block 668]
རིམ་གྱིས་པ་ནི། ཨོཾ་ཨཱཿཨཾ་ཧཱུཾ་ཕཊ་སྭཱ་ཧཱ་ཞེས་བདག་མེད་མ༌[^223]ལ་འབུམ་མོ། །

[Block 669]
དེ་བཞིན་དུ་དེ་ཉིད་གསུམ་གྱི་སྤེལ་ལ་ལྷ་མོ་ཀུན་ལ་ཁྲི་ཁྲིར་སྦྱར་རོ། །

[Block 670 [HEADING]]
##### ཅིག་ཅར་བ། ^1-2-2-2-0
--- END BLOCKS ---
