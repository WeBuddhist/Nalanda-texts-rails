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
[Block 316]
འདིར་སྨྲས་པ། འགྲོ་བ་ནི་ཡོད་པ་ཁོ་ནའོ། །ཅིའི་ཕྱིར་ཞེ་ན། བགོམ་པ་དང་སོང་བ་དང་མ་སོང་བ་ཡོད་པའི་ཕྱིར་ཏེ། གང་གི་ཕྱིར་འགྲོ་བ་དང་ལྡན་པའི་ཕྱིར་བགོམ་པ་ཞེས་བྱ་བ་ཡིན་ལ། འགྲོ་བ་མཐར་ཕྱིན་པ་ནི་སོང་བ་ཞེས་བྱ་བ་ཡིན། འགྲོ་བའི་བྱ་བ་མ་སོང་བ་ལ་ལྟོས་ནས་མ་སོང་བ་ཞེས་བྱ་བ་ཡིན་པས་ན་དེ་ལྟ་བས་ན་བགོམ་པ་དང་སོང་བ་དང་། མ་སོང་བ་ཡོད་པའི་ཕྱིར་འགྲོ་བ་ཡོད་དོ། །

[Block 317]
བཤད་པ། ཅི་ཁྱེད་ནམ་མཁའ་འདི་ལ་ལྡང་བར་བསྐྱོད་དམ། གང་གི་ཚེ།

[Block 318 [VERSE]]
འགྲོ་བ་རྩོམ་པའི་སྔ་རོལ་ན། །
གང་དུ་འགྲོ་བ་རྩོམ་འགྱུར་བ། །
བགོམ་པ་མེད་ཅིང་སོང་བ་མེད། །

[Block 319]
འདི་ལ་འགྲོ་བ་རྩོམ་པའི་སྔ་རོལ་སྡོད་པར་གྱུར་པ་ན་གང་དུ་འགྲོ་བ་རྩོམ་པར་འགྱུར་བའི་བགོམ་པ་ཡང་མེད་ཅིང་། སོང་བ་ཡང་མེད་དོ། །

[Block 320]
འགྲོ་བ་རྩོམ་པ་མེད་ན་བགོམ་པ་འགྲོ་བ་དང་ལྡན་པར་ག་ལ་འགྱུར། འགྲོ་བ་དང་ལྡན་པ་མེད་ན་འགྲོ་བ་མཐར་ཕྱིན་པ་ཡོད་པར་ཡང་ག་ལ་འགྱུར། འདིར་སྨྲས་པ། མ་སོང་བ་ནི་ཡོད་དེ། དེར་འགྲོ་བ་རྩོམ་པར་འགྱུར་རོ། །

[Block 321]
བཤད་པ། མ་སོང༌[^220]འགྲོ་བ་ག་ལ༌[^221]ཡོད། །འདི་ལ་སྡོད་ཅིང་མི་བསྐྱོད་པ༌[^222]པ་གང་ཡིན་པ་དེ༌[^223]ནི་མ་སོང་བ་སྟེ། དེ་ལ་ནི་རྩོམ་པ་མེད་དོ། །

[Block 322]
གང་གི་ཚེ་སྐྱོད་པར་བྱེད་པ་དེའི་ཚེ་ན་ནི་གོ་སྐབས་གང་དུ་སྐྱོད་པར་བྱེད་པ་དེ་མ་སོང་བ་མ་ཡིན་ནོ། །

[Block 323]
དེའི་ཚེ་མ་སོང་བའི་གོ་སྐབས་གང་ཡིན་པ་དེ་ལ་ནི་བསྐྱོད་པ༌[^224]མེད་དོ། །

[Block 324]
དེ་ལྟ་བས་ན་མ་སོང་བ་ལ་འགྲོ་བའི་རྩོམ་པ་གང་ལ༌[^225]ཡོད། དེ་ལྟར་བརྟགས་ན།

[Block 325 [VERSE]]
འགྲོ་རྩོམ་རྣམ་པ་ཐམས་ཅད་དུ། །
སྣང་བ་མེད་པ་ཉིད་ཡིན་ན། །
སོང་བ་ཅི་ཞིག་བགོམ་པ་ཅི། །
མ་སོང་ཅི་ཞེས་རྣམ་པར་བརྟག །

[Block 326]
གང་གི་ཚེ་དེ་ལྟར་རྣམ་པ་ཐམས་ཅད་ཀྱིས་རྣམ་པར་བརྟག་པ༌[^226]ན་འགྲོ་བའི་རྩོམ་པ་སྣང་བ་མེད་པ་ཉིད་ཡིན་པ་དེའི་ཚེ་ཁྱོད་ཀྱི་སོང་བ་ཡང་ཅི། བགོམ་པ་ཡང་ཅི། མ་སོང་བ་དེ་ཡང་ཅི། ཞེས་རྣམ་པར་བརྟག །སྨྲས་པ། རེ་ཞིག་མ་སོང་བ་ནི་ཡོད་དོ། །

[Block 327]
བཤད་པ། ཅི་ཁྱོད་བུ་མ་བཙས་པར་འཆི་བའི་མྱ་ངན་བྱེད་དམ། ཁྱོད་སོང་བ་མེད་པར་མ་སོང་བ་ལ་རྟོག་གོ། །

[Block 328]
འདི་ལྟར་སོང་བའི་གཉེན་པོ་ནི་མ་སོང་བ༌[^227]ཡིན་ན། དེ་ལ་གལ་ཏེ་སོང་བ་ཉིད་མེད་ན་ཁྱོད་ཀྱི་མ་སོང་བ་ཡོད་པར་ག་ལ་འགྱུར། སྨྲས་པ། གལ་ཏེ་གཉེན་པོ་མེད་པས་སོང་བ་མེད་ན་འོ་ན། [^228]འགྲོ་བ་འགྲུབ་པོ། །ཅིའི་ཕྱིར་ཞེ་ན། མི་མཐུན་པའི༌[^229]ཡོད་པའི་ཕྱིར་ཏེ། འདི་ལྟར་འགྲོ་བའི་མི་མཐུན་པ་སྡོད་པ་ཡོད་དེ།[^230] དེ་བས་ན༌[^231]མི་མཐུན་པ་ཡོད་པའི་ཕྱིར་འགྲོ་བ་ཡོད་པ་ཁོ་ནའོ། །

[Block 329]
བཤད་པ།[^232] གལ་ཏེ་སྡོད་པ་ཡོད་ན་ནི་འགྲོ་བ་ཡང༌[^233]ཡོད་པར་འགྱུར་གྲང་ན། སྡོད་པ་མི་འཐད་པས་འགྲོ་བ་ཡོད་པར་ག་ལ་འགྱུར། ཇི་ལྟར༌[^234]ཞེ་ན། འདི་ལ་གལ་ཏེ་སྡོད་པ་ཡོད་པར་གྱུར་ན། འགྲོ་བ་པོའི་འམ། འགྲོ་བ་པོ་མ་ཡིན་པའི་ཡིན་གྲང་ན། དེ་ལ།

[Block 330 [VERSE]]
རེ་ཞིག་འགྲོ་པོ་མི་སྡོད་དེ། །
འགྲོ་བ་པོ་མིན་སྡོད་པ་མིན། །
འགྲོ་པོ་འགྲོ་པོ་མིན་ལས་གཞན། །
གསུམ་པ་གང་ཞིག་སྡོད་པར་འགྱུར། །

[Block 331]
དེ་ལྟ་བས་ན་སྡོད་པ་ནི་མེད་པ་ཁོ་ནའོ། །ཅིའི་ཕྱིར་ཞེ་ན། མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 332]
ཇི་ལྟར་ཞེ་ན། བཤད་པ།

[Block 333 [VERSE]]
རེ་ཞིག་འགྲོ་པོ་སྡོད་དོ་ཞེས། །
ཇི་ལྟར་འཐད་པ་ཉིད་དུ་འགྱུར། །
འགྲོ་བ་མེད་ན་འགྲོ་བ་པོ། །
ནམ་ཡང་འཐད་པར་མི་འགྱུར་རོ། །

[Block 334]
འདི་ལ་འགྲོ་བ་དང་ལྡན་པས་འགྲོ་བ་པོར་འགྱུར་བས་འགྲོ་བ་མེད་ན། འགྲོ་བ་པོར་མི་འཐད་པ་ཉིད་དོ། །

[Block 335]
འགྲོ་བ་ལོག་པ་ནི་སྡོད་པ་ཞེས་བྱ་བ་ན་འགྲོ་བ་དང་སྡོད་པ་མི་མཐུན་པ་དེ་གཉིས་གཅིག་ན་ལྷན་ཅིག་འདུག་པ་མེད་དོ། །

[Block 336]
དེའི་ཕྱིར་དེ་ལྟར་རེ་ཞིག་འགྲོ་བ་པོ་སྡོད་དོ་ཞེས་བྱ་བ་དེ་ཇི་ལྟར་འཐད་པ་ཉིད་དུ་འགྱུར། དེ་ནི་འགྲོ་བ་པོ་མ་ཡིན་པ་ཡང་མི་སྡོད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 337]
འདི་ལ་འགྲོ་བ་ལོག་པ་ནི་སྡོད་པ་ཞེས་བྱ་བ་ན་འགྲོ་བ་པོ་མ་ཡིན་པ་ནི་འགྲོ་བ་དང་བྲལ་བའི་ཕྱིར་སྡོད་པ་ཉིད་ཡིན་པས་དེ་ལ་ཡང་སྡོད་པས་ཅི་ཞིག་བྱ། སྡོད་པ་དེ་ལ་ཡང་སྡོད་པར་བརྟག་ན། སྡོད་པ་གཉིས་སུ་ཐལ་བར་འགྱུར་བ་དང་། སྡོད་པ་པོ་ཡང་གཉིས་སུ་ཐལ་བར་འགྱུར་བས་དེའི་ཕྱིར་འགྲོ་བ་པོ་མ་ཡིན་པ་ཡང་མི་སྡོད་དོ། །

[Block 338]
དེ་ལ་འདི་སྙམ་དུ་འགྲོ་བ་པོ་ཡིན་པ་དང་། འགྲོ་བ་པོ་མ་ཡིན་པ་སྡོད་པར་སེམས་ན། བཤད་པ། འགྲོ་པོ་འགྲོ་པོ་མིན་ལས་གཞན། །

[Block 339]
གསུམ་པ་གང་ཞིག་སྡོད་པར་འགྱུར། འགྲོ་པོ༌[^235]དང་འགྲོ་བ་པོ་མ་ཡིན་པ་ལས་གཞན་པ་གསུམ་པ་འགྲོ་བ་པོ་ཡིན་པ་དང་། འགྲོ་བ་པོ་མ་ཡིན་པ་གང་སྡོད་དོ་ཞེས་བྱ་བར་བརྟགས་པ་དེ་གང་ཞིག་ཡིན། དེ་ལྟ་བས་ན་མེད་པ་ཁོ་ནའི་ཕྱིར་འགྲོ་བ་པོ་ཡིན་པ་དང་། འགྲོ་བ་པོ་མ་ཡིན་པ་ཡང་མི་སྡོད་དོ། །

[Block 340]
ཡང་གཞན་ཡང་། འགྲོ་བ་ལོག་པ་ནི་སྡོད་པ་ཞེས་བྱ་བ།[^236] ལྡོག་པ་དེ་ཡང་བགོམ་པ་ལས་སམ། སོང་བ་ལས་སམ་མ་སོང་བ་ལས་ལྡོག་པར་འགྱུར་གྲང་ན། དེ་ལ།

[Block 341 [VERSE]]
བགོམ་ལས་ལྡོག་པར༌[^237]མི་འགྱུར་ཏེ། །
སོང་དང་མ་སོང་ལས་ཀྱང་མིན། །

[Block 342]
བགོམ་པ་ལས་སྡོད་པ༌[^238]མི་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་འགྲོ་བ་དང་ལྡན་པའི་ཕྱིར་བགོམ་པ་ཡིན་ལ། འགྲོ་བ་ལོག་པ་ནི་སྡོད་པ་ཡིན་པས་སྡོད་པ་དང་འགྲོ་བ་མི་མཐུན་པ་དེ་གཉིས་ཅིག་ན་མི་སྲིད་པས་དེའི་ཕྱིར་རེ་ཞིག་བགོམ་པ་ལས་ལྡོག་པར་མི་འགྱུར་ཏེ། དེ༌[^239]ནི་སོང་བ་དང་མ་སོང་བ་ལས་ཀྱང་སྡོད་པར་མི་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 343]
འདི་ལྟར་འགྲོ་བ་ལོག་པ་ནི་སྡོད་པ་ཡིན་ན། [^240]འགྲོ་བ་ནི་སོང་བ་དང་མ་སོང་བ་ལ་མེད་དེ། འགྲོ་བ་མེད་ན་འགྲོ་བ་ལྡོག་པ་ག༌[^241]ལ་ཡོད། འགྲོ་བ་ལྡོག་པ་མེད་ན་སྡོད་པ་ག་ལ་ཡོད། དེ་ལྟ་བས་ན་སོང་བ་དང་མ་སོང་བ་ལས་ཀྱང་ལྡོག་པར་མི་འགྱུར་རོ། །

[Block 344 [VERSE]]
འགྲོ་བ་དང་ནི་འཇུག་པ་དང་། །
ལྡོག་པ་ཡང་ནི་འགྲོ་དང་མཚུངས། །

[Block 345]
ཇི་ལྟར་འགྲོ་བ་པོ་མི་སྡོད་དེ། སྡོད་པ་དང་། འགྲོ་བ་གཉིས་མི་མཐུན་པའི་ཕྱིར་རོ། །ཞེས་བཤད་པ་དེ་བཞིན་དུ་སྡོད་པ་པོ་ཡང་མི་འགྲོ་སྟེ། སྡོད་པ་དང་འགྲོ་བ་གཉིས་མི་མཐུན་པའི་ཕྱིར་རོ། །

[Block 346]
ཇི་ལྟར་འགྲོ་བ་པོ་མ་ཡིན་པ་མི་སྡོད་དེ། སྡོད་པ་གཉིས་སུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ་ཞེས་བཤད་པ་དེ་བཞིན་དུ་སྡོད་པ་པོ་མ་ཡིན་པ་ཡང་མི་འགྲོ་སྟེ། འགྲོ་བ་གཉིས་སུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 347]
ཇི་ལྟར་འགྲོ་བ་པོ་ཡིན་པ་དང་། [^242]འགྲོ་བ་པོ་མ་ཡིན་པ་མི་སྡོད་དེ། མི་སྲིད་པའི་ཕྱིར་རོ་ཞེས་བཤད་པ་དེ་བཞིན་དུ་སྡོད་པ་པོ་ཡིན་པ་དང་། སྡོད་པ་པོ་མ་ཡིན་པ་ཡང་མི་འགྲོ་སྟེ། མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 348]
དེ་ལྟར་རེ་ཞིག་འགྲོ་བ་པོའི་སྡོད་པ་དང་། སྡོད་པ་པོའི་འགྲོ་བ་མཚུངས་པ་ཡིན་ནོ། །

[Block 349]
ད་ནི་ཇི་ལྟར་འགྲོ་བའི་རྩོམ་པ་སོང་བ་དང་། མ་སོང་བ་དང་། བགོམ་པ་ལ་མི་འཐད་དོ་ཞེས་བཤད་པ་དེ་བཞིན་དུ་སྡོད་པའི་འཇུག་པ་ཡང་བསྡད་པ་དང་མ་བསྡད་པ་དང་། སྡོད་པ་ལ་མི་འཐད་དེ། དེ་ལྟར་ན་འགྲོ་བའི་རྩོམ་པ་དང་སྡོད་པའི་འཇུག་པ་མཚུངས་པ་ཡིན་ནོ། །

[Block 350]
ད་ནི་ཇི་ལྟར་འགྲོ་བའི་ལྡོག་པ་སོང་བ་དང་། མ་སོང་བ་དང་། བགོམ་པ་ལས་ལྡོག་པར་མི་འགྱུར༌[^243]ཞེས་བཤད་པ་དེ་བཞིན་དུ་སྡོད་པའི་ལྡོག་པ་ཡང་གང་དུ་བསྡད་པ་དེ་ནས་མི་འགྲོ་སྟེ། འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 351]
གང་དུ་མ་བསྡད་པ་དེ་ནས་ཀྱང་མི་འགྲོ་སྟེ། འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 352]
གང་དུ་བསྡད་པ༌[^244]དེ་ནས་ཀྱང་མི་འགྲོ་སྟེ། སྡོད་པ་དང་འགྲོ་བ་གཉིས་མི་མཐུན་པའི་ཕྱིར་རོ། །

[Block 353]
དེ་ལྟར་ན་འགྲོ་བའི་ལྡོག་པ་དང་། སྡོད་པའི་ལྡོག་པ་མཚུངས་པ་ཡིན་ནོ། །

[Block 354]
འདིར་སྨྲས་པ། འགྲོ་བ་དང་འཇུག་པ་དང་། ལྡོག་པ་སོང་བ་དང་མ་སོང་བ་དང་། བགོམ་པ་ལ་ཡོད་དོ་ཞེའམ་འགྲོ་བ་པོ་དང་། འགྲོ་བ་པོ་མ་ཡིན་པ་དང་། དེ་ལས་གཞན་པ་ལ་ཡོད་དོ་ཞེས་བྱ་བ་དེ་ལ༌[^245]བརྗོད་པར་མི་ནུས་སུ་ཟིན་ཀྱང་། ཙཻ་ཏྲའི་བགོམ་པ༌[^246]འདོར་བ་མཐོང་ནས། ཙཻ་ཏྲའི་འགྲོ་བ་པོ་ཞེས་བྱ་བར་འགྱུར་བས་དེའི་ཕྱིར་འགྲོ་བ་པོ་དང་འགྲོ་བ་ཡོད་དོ། །

[Block 355]
བཤད་པ། རེ་ཞིག་བརྗོད་པར་མི་ནུས་སུ་ཟིན་ཀྱང་ཞེས་བྱ་བ་དེ་ནི་ཕོངས་པའི་ཚིག་ཡིན་ནོ། །
--- END BLOCKS ---
