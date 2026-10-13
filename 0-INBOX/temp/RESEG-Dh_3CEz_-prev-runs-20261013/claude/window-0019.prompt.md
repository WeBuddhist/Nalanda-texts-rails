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

[Block 671]
ཅིག་ཅར་བ་ནི་ཨོཾ་ཨཱཿནས་སྔགས་ཀུན་ལ་ཧཱུཾ་ཕཊ་སྭཱ་ཧཱ་ཞེས་གཙོ་མོ་དང་འཁོར་ལ་གྲངས་སྔ་མ་བཞིན་ནོ། །

[Block 672 [VERSE]]
ས་བོན་སྦྱོར་བ་ནི་འོག་ནས་འཆད་པའོ། །
ཏྲཻ་ལོཀྱཱ་ཀྵེ་པ་ནི་འཇིག་རྟེན་གསུམ་གཡོས་ཤིག་པའོ། །
ཕྱག་གཉིས་པའི་དགའ་བའི་རྟེན་ཅན་ཆོས་ཀྱི་སྐུའོ། །

[Block 673]
གཞན་སྔ་མ་བཞིན་ནོ། །

[Block 674]
ཛྭ་ལ་ཛྭ་ལ་ནི་དོན་ནམ་རྣམ༌[^224]པར་རྟོག་པ་ལ་འབར་བའོ། །

[Block 675]
བྷྱོ་ནི་ཚིམ་པའོ། །

[Block 676]
ཕྱག་བཞི་པའི་ནི་མཆོག་དགའི་རྟེན་ཅན༌[^225]ལོངས་སྤྱོད་རྫོགས་པའི་སྐུའོ། །

[Block 677]
ཀི་ཊི་ཀི་ཊི་ཞེས་བྱ་བ་སྟེ་མི་མཐུན་པ་ཆོད་ཅིག་པའོ། །

[Block 678]
ཕྱག་དྲུག་པའི་ནི་དགའ་བྲལ་གྱི་རྟེན་ཅན་སྤྲུལ་པའི་སྐུའོ། །

[Block 679]
ཨོཾ་ནི་ཨ་ཡིག་དང༌[^226]ཨུ་ཡིག་དང་ཧཾ་ཡིག་སྟེ་སྟོང་པ་ཉིད་དོ། །

[Block 680 [VERSE]]
ཨ་ནི་མཚན་མ་མེད་པའོ། །
ཧཱུཾ་ནི་སྨོན་པ་མེད་པའོ། །

[Block 681]
བསྙེན་སྒྲུབ་ཀྱི་ལྷ་བསྐྱེད་པའི་དུས་སུ་སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་བརླབ་པ་དང་བཟའ་བཏུང་བདུད་རྩིར་བྱིན་གྱིས་བརླབ་པའི་སྔགས་སོ། །

[Block 682]
ཨོཾ་རཀྵ་ཞེས་བྱ་བ་ནི་ས་སྦྱོང་བའི་སྔགས༌[^227]ཏེ་གནས་སྐབས་རྣམ་པ་གསུམ་དུ་འགྱུར་ཏེ། བསྙེན་པའི་ས་བསྲུང་བ་དང་། རྣལ་འབྱོར་གྱི་ས་བསྲུང་བ་དང་། སྒྲུབ་པའི་ས་བསྲུང་བའོ། །

[Block 683]
ཨོཾ་ཧཱུཾ་སྭཱ་ཧཱ་རེངས་པའོ་ཞེས་པ་ནི་སྔར་དགྱེས་པའི་རྡོ་རྗེ་དཔའ་བོ་གཅིག་པའམ་དཀྱིལ་འཁོར་གྱི་བསྙེན་པ་སྔོན་དུ་སོང་བའམ། [^228]ཡང་ན་འདི་རང་གི་བསྙེན་པ་སྔོན་དུ་སོང་བས་སྒྲུབ་པ་ནི་ཚོགས་བསགས་ནས་རབ་དང་། གུར་གྱི་ནང་དུ་རྡོ་རྗེ་རྣམ་བཞིའམ་ས་བོན་ཕྱག་མཚན་ལས་རྡོ་རྗེ་རྣལ་འབྱོར་མ་བསྐྱེད་ལ། ཡེ་ཤེས་སེམས་དཔའ་དགུག་གཞུག༌[^229]བྱིན་གྱིས་བརླབ། དབང་བསྐུར་མཆོད་བསྟོད་བདུད་རྩི་མྱང་བ་བྱས་ལ་ཨོཾ་ཨཱཿཧཱུཾ་སྭཱ་ཧཱ་ཁྲི་བཟླས་ལ་སྒྲུབ་པ་ལས་སྦྱོར་ནི་ཆེ་གེ་མོ་སྟམྦྷ་ཡ་ཀུ་རུ་མཾ་ཞེས་བཏགས་ཤིང་ཏིང་ངེ་འཛིན་གྱི་ངག་གིས༌[^230]ལུས་རྡོ་རྗེའམ་དབང་ཆེན་ལ་སོགས་པས་མནན་བར་བསམ་མོ། །

[Block 684]
དེ་བཞིན་དུ་རྣལ་འབྱོར་མ་རེ་རེ་དང་སྔགས་རེ་རེར༌[^231]སྦྱར་རོ། །

[Block 685]
ཨ་ཕུཿཞེས་པ་ནས༌[^232]ཆར་དབབ་པ་སྟེ། འདིའི་དོན་བསྙེན་པ་དང་ཉེ་བའི་བསྙེན་པ་དང་། སྒྲུབ་པ་དང་སྒྲུབ་པ་ཆེན་པོ་སྟེ། བསྙེན་པ་ནི་ཧེ་བཛྲའི་དཀྱིལ་འཁོར་གྱི་བསྙེན་པ་སྟེ་སློབ་དཔོན་གྱིས་ཞེས་བྱ་བར་སྦྱར༌[^233]རོ། །

[Block 686]
ཉེ་བའི་བསྙེན་པ་ནི་ཨོཾ་གུ་རུ་ཞེས་པ་ནས་ཧཱུཾ་ཕཊ་སྭཱ་ཧཱ་གོང་མ་ཚོ་སྦྱར་རོ། །

[Block 687]
དེ་ལ་མཚན་མ་ཐོབ་པས་སྒྲུབ་པ་བྱ་སྟེ། རླུང་གི་ཕྱོགས་སུ་རྫིང་བུ་བྱས། །ཞེས་པར་སྦྱར་ཏེ་དང་ལ༌[^234]སྟ་གོན་བྱས་ཏེ་དེ་ནས་རྡུལ༌[^235]ཚོན་བྲིས་ལ་ཙ་ཀ་ལི་དགོད་པ་དང་ཡང་བསྒོམ་པ༌[^236]ལྷ་མོ་ཚོ་མས༌[^237]སྦྲུལ་མནན་པ་གཙོ་བོས་མཐའ་ཡས་མནན་པ་དེ་ལ་དཀྱིལ་འཁོར་བསྒྲུབ་པ་མཆོད་བསྟོད་བདུད་རྩི་མྱང་བ་བྱས་ན་ཨ་ཕུཿའི་རྣམ་པ་ཞེས་བྱ་བ་སྟ་གོན་དུས་སུ་གཟུགས་བརྙན་བྱས་པ་ཡང་མཐའ་ཡས་སུ་བསྐྱེད་ལ་རང་བཞིན་པ་བཀུག་ལ༌[^238]དེ་ལ་བསྟོད་པ་དང་འོག་གི༌[^239]བཟླས་པ་བྱས་ལ་སྒྲུབ་པ་ཆེན་པོ་ནི་མཐའ་ཡས་དེར་གཞག་ཅེས་བྱ་སྟེ་མནན་པ་བྱས་ལ། ཨ་ནནྟ་ཁྲོ་བ༌[^240]ཞེས་སྔགས་དེར༌[^241]གཟིར་རོ། །

[Block 688]
མ་གྲུབ་ན་སྤོགས་པ་ནི་སྔགས་བཟློག་སྟེ་བཟླས༌[^242]ཞེས་པ་ཡི་གེ་བཟློག་སྟེ་ཕཊ་ཅེས་མས་བཟློག་པའོ། །

[Block 689]
དེ་བཞིན་དུ་བསྙེན་པ་དང་སྒྲུབ་པ་དང་སྒྲུབ་པ་ལས་ལ་སྦྱར་བ་གོ་སླའོ། །

[Block 690 [HEADING]]
#### ལྷ་དགས་པ། ^1-2-3-0

[Block 691 [HEADING]]
##### ཕྱི། ^1-2-3-1-0

[Block 692 [VERSE]]
ལྷ་དགས་པ་ལ་གཉིས་ཏེ་ཕྱི་དང་ནང་ངོ་། །
ཚངས་པའི་ས་བོན་ནི་པ་ལ་ཤ་རྒྱ་སྐྱེགས་སོ། །

[Block 693]
རྒྱལ་ལ་སྒྲུབ་པ་ནི་སྐར་མ་རྒྱལ་གྱི་ཉིན་པར་རོ། །

[Block 694]
ཀུ་ཥཱ་རཙྪིནྣ་ནི་རྩྭ༌[^243]སྟ་རེས་གཅོད་པའོ། །

[Block 695]
ཉི་མ་གཟས་ཟིན་པ་ནི་ཟླ་བ་བདུན་བདུན་ལ་གླིང་འདིའམ། གཞན་དུ་གཟའ་ཡིས་ཟིན་པའོ། །

[Block 696]
མི་བསྐྱོད་པ་བཏགས༌[^244]ཤིང་བྱ་བ་ནི། དེ་ཡིས་སྦྲུས༌[^245]ལ། དགྲ་སྟའི་གཟུགས་ཅིག༌[^246]བྱས་ལ། བཛྲ་ཀུ་ཥཱ་ར་སྒྲུབ་པའི་དོན་དུ་ཁྲི་བཟླས་ཤིང་བསྒྲུབ་པ་ལས་སྦྱོར༌[^247]གྱི་དུས་སུ་དེ་བརྡར་ལ་དཔྲལ་བར་ཐིག་ལེ༌[^248]བྱས་ལ། ལྷ་གང་ལ་ཕྱག་བྱས་པ་དེ་འགས་ཞེས་པ་ནི་དབང་ཕྱུག་ཆེན་པོ་ལ་སོགས་པའི་ལྷ་རྟེན་ལ་སྟ་རེ་དམིགས་ལ་ཕྱག་བཙལ་ལོ། །

[Block 697]
བསྙེན་པ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 698 [HEADING]]
##### ནང། ^1-2-3-2-0

[Block 699]
ནང་ནི་ཚངས་པའི་ས་བོན་ནི་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 700 [VERSE]]
རྒྱལ་ལ་སྒྲུབ་པ་ནི་ལྷན་ཅིག་པའི་དུས་སོ། །
ཀུ་ཥཱ་ར་ཙྪིནྣ་ནི་བྱང་ཆུབ་སེམས་ཀྱི་རིམ་གྲོའོ། །

[Block 701]
མི་བསྐྱོད་པ་བཏགས་པ༌[^249]ནི་བརྡུང༌[^250]བའོ། །

[Block 702]
ཉི་མ་གཟས་ཟིན་པ་ནི་རང་བྱུང་གི་མེ་ཏོག་གོ། །

[Block 703]
དགྲ་སྟ་ནི་གཅོད་པས་ན་དགྲ་སྟ་སྟེ་རྐང་པས་མནན་པ་དང་འདྲ་བ་སྟེ། འོག་ཏུ་འཇོམས་པའོ། །

[Block 704]
བཟླས་པ་ནི་ཡང་དང་ཡང་དུ་བསྒོམ་པ་སྟེ། ལྷ་གང་ལ་ཕྱག་བྱས་པ་ནི་དངོས་པོ་གཟུགས་ལ་སོགས་པ་དངོས་པོ་ལ་ཞེན་པ་གང་ཡང་རུང་བདེ༌[^251]འཇོམས་པའོ། །

[Block 705]
ལྷག་མ་རྣམས་ནི་གོ་སླ་བས་མ་བཤད་དོ། །
--- END BLOCKS ---
