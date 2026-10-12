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
[Block 351]
རྡོ་རྗེ་ཕྲ་མོ་ནི་ལྕེ་སྟེ་ལྕེ་དེའི་རྩེ་མོ་ཁ་ལ་རེག་པ་ལས་སེམས་མཉམ་པར་གཞག་པར༌[^145]འགྱུར་རོ།།

[Block 352]
རྣལ་འབྱོར་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་ཀུན་རྫོབ་དང་དོན་དམ་པའི་བདག་ཉིད་ཅན་གྱི་རྡོ་རྗེ་འཛིན་པ་སྟེ། བདག་དང་ཁམས་གསུམ་པོ་དེར་མཉམ་པར་ལོངས་སྤྱོད་པར་བྱའོ།།

[Block 353]
ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ནི་མངོན་སུམ་དུ་བྱེད་པའི་ཐབས་ཀྱི་སྦྱོར་བ་རིགས༌[^146]པའོ།།

[Block 354]
སོམ་ཉིར་གྱུར་པ་ནི་དེའི་ཤེས་རབ་ཡིད་གཉིས་ཟོས་ནས་ཕན་ཚུན་དུ་གྲོས་སུ་འགྲོ་བར་བྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ།།

[Block 355]
སྐུ་རྡོ་རྗེའི་རྒྱུར་གྱུར་པ་ཞེས་བྱ་བ་ནི་ཕྱག་རྒྱ་ཆེན་པོའི་རྒྱུར་གྱུར་པ་ལ་བྱའོ།།

[Block 356]
སྤྱི་བོར་རྡོ་རྗེ་ཞེས་བྱ་བ་ནི༌[^147]རྡོ་རྗེ་རྩེ་ལྔ་པའོ།།

[Block 357]
དེ་ཡོངས་སུ་གྱུར་པ་ལས་རྡོ་རྗེས་ཉེ་བར་མཚན་པའི་རྡོ་རྗེ་སེམས་དཔའོ།།

[Block 358]
རྡོ་རྗེ་སེམས་དཔའ་དེ་ཡོངས་སུ་གྱུར་པ་ལས་མི་བསྐྱོད་པ་ལ་སོགས་པར་བསྒོམ་པར་བྱའོ།།

[Block 359]
རིམ་པ་འདི་ཉིད་དང་ཞེས་བྱ་བ་ནི་རྡོ་རྗེ་སེམས་དཔའ་ཡོངས་སུ་གྱུར་པ་ལས་མི་བསྐྱོད་པ་ལ་སོགས་པར་གྱུར་པ་ཇི་ལྟ་བ་བཞིན་དུ་མི་བསྐྱོད་པ་ལ་སོགས་པར་གྱུར་པས་ཀྱང་འཇམ་དཔལ་ལ་སོགས་པ་རྣམས་སུ་གྱུར་ཏེ།[^148] །རྡོ་རྗེ་དབྱིངས་ཀྱི་དབང་ཕྱུག་མ་ནི་ཤེས་རབ་མའི་རང་བཞིན་ནོ།།

[Block 360]
ཕྱི་རོལ་གྱི་ལྷ་ལ་ཞེས་བྱ་བ་ནི་མི་བསྐྱོད་པ་ལ་སོགས་པའོ།།

[Block 361]
དེ་རྣམས་ལས་མངོན་པར་ཞེན་པར་བྱེད་པའི་ལག་པའི་ཕྱག་རྒྱ་མི་བཅིང་བའོ།།

[Block 362]
དྲེགས་པ༌[^149]དང་གདུགས་ནི་མིའི་སྣའོ།།

[Block 363]
རྫོགས་པ་དང་ཟླ་བ་ནི་དེའི་ནང་གི་རྩ་ཟླུམ་པོའི་རྣམ་པར༌[^150]དག་གོ།།

[Block 364]
རུས་སྦལ་མགྲིན་ནི་དེའི་ནང་ན་རྩ་པདྨའི་རྣམ་པ་ལྟ་བུར་གནས་པའོ།།

[Block 365]
ལྟ་བ་དེ་བཟློག་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཐ་མལ་བའི་ལྟ་བ་ལ་སོགས་པ་རྣམ་པར་དག་པའོ།།

[Block 366]
སློབ་དཔོན་དེ་ཞེས་བྱ་བ་ནི་འདུས་པ་སྟོན་པ་པོ་སྟེ། དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པའི་གཟུགས་དེ་ལ་རབ་ཏུ་མཆོད་ཅིང་སྐུ་ལ་སོགས་པས་བྱིན་གྱིས་རློབ་པ་དང་། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་རྗེས་སུ་གནང་བ་སྩོལ་བ༌[^151]དང་བླ་ན་མེད་པའི་ཡང་བླ་ན་མེད༌[^152]པའི་དབང་བསྐུར་བས་ན་བྱང་ཆུབ་ཀྱི་སེམས་རྡོ་རྗེ་སློབ་དཔོན་ནོ།།

[Block 367]
དེ་ཉིད་ཀྱི་ཟུང་དུ་འཇུག་པའི་བདག་ཉིད་ཡིན་པས་ན་རྡོ་རྗེ་འཛིན་ཆེན་པོ་དང་ཤིན་ཏུ་རྣམ་པར་དག་པ་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ངོ་བོ་མི་བསྐྱོད་པའོ།།

[Block 368]
གསང་བ་ལྔའི་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པ་ལྔའི་བདག་ཉིད་སློབ་དཔོན་གྱི༌[^153]ལུས་ལ་མཆོད་པའི་སྤྱི་ཀུན་བྱའོ།།

[Block 369]
རང་གི་སྙིང་གའི་པདྨ་ལ་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་སྤྲོས་པ་མེད་པ་ཤེས་པར་འདོད་པ་ལ་སྔོན་དུ་དཀྱིལ་འཁོར་སྤྲུལ་ནས་ཡི་གེ་གསུམ་དང་སྲོག་དང་སྩོལ་བས༌[^154]བྱང་ཆུབ་ཀྱི་སེམས་ངེས་པར་ཕབ་སྟེ། སློབ་མའི་སྤྱི་བོར་བླུགས༌[^155]ལ་དེ་ནས་ཡང་དག་པའི་བདེན་པའི་ངོ་བོར་སློབ་མ་བསམས༌[^156]ནས་ཆུ་ལ་སོགས་པའི་རིམ་པས་དབང་བསྐུར་བ་སྦྱིན་པར་བྱའོ།།

[Block 370]
ནམ་མཁའི་དབྱིངས་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^157]ནི་སྤྲོས་པ་དང་བཅས་པ་ཤེས་པར་འདོད་པའི་དོན་སྟོན་པ་ཡིན་ནོ།།

[Block 371]
དེའི་འོག་ཏུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྔ་མ་བཞིན་ནོ།།

[Block 372]
རབ་ཏུ་སྦྱངས་པ་འགྲོ་བ་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་ཡང་སྤྲོས་པ་མེད་པ་འདོད་པ་ལ་དེ་ལྟ་བུར་བྱ་བ་ཡིན་ནོ།།

[Block 373]
རང་གི་ལུས་ཞེས་བྱ་བ་ནི་ཐོག་མར་རྣལ་འབྱོར་པ་རང་གི་ལུས་ཀྱི་ཤ་དང་རུས་པ་ལ་སོགས་པ་འོད་གསལ་བར་བལྟ་བར་བྱའོ།།

[Block 374]
དེ་ནས་ཧཱུཾ་ཏྲི་ཁཾ་ཞེས་བྱ་བ་ལ་སོགས་པས་རྡོ་རྗེ་མཁའ་འགྲོ་སྐྱེད་པར་བྱེད་པ་ཡིན་ནོ།།

[Block 375]
བུ་ནི་སངས་རྒྱས་རྣམས་སོ།།

[Block 376]
ཚ་བོ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སོ།།

[Block 377]
པདྨ་དང་རྡོ་རྗེ་ཡང༌[^158]སྦྱར་བས་དོན་སྐྱེ་བར་བྱེད་པར་ཤེས་པར་བྱའོ།།

[Block 378]
ས་ནི་སྤྱན་མ་སྟེ་ཤེས་རབ་ཀྱི་དངོས་པོར་རོལ་པར་བྱའོ།།

[Block 379]
འདི་ལྟ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཡི་གེ་ཨོཾ་ལས་བྱུང་བའི་འཁོར་ལོའི་དབུས་སུ་བསྒྲུབ་བྱ་འོད་ཟེར་སེར་པོ་དང་ལྡན་པར་བཞག་ལ།།དེའི་སྟེང་དུ་ཡང་འཁོར་ལོ་གནས་པར་བསམས་ཏེ་དུག་མེད་པར་བྱའོ།།

[Block 380]
སེར་པོ་ལྟ་བུར་བྱ་བ་ནི་མནན་པའི༌[^159]དུས་སུ་ནི་ཐམས་ཅད་སེར་པོར་བསྒོམ་པར་བྱའོ།།

[Block 381]
མཆོད་ཡོན་གྱི་ཤིང་ནི་ཤིང་དེའི་འབྲས་བུའི་ནང་ན་པདྨོའི་བལ་ཏེ་དེ་བསྒྲིལ་ལ་པདྨའི་སྐུད་པས་དཀྲིས་པའོ།།

[Block 382]
ནང་གི་མངོན་པར་བྱང་ཆུབ་པ་ནི་སྣང་བ་ལ་སོགས་པའོ།།

[Block 383]
ཤེས་རབ་ཀྱི་རབ་རིབ་ཀྱི་ཞེས་བྱ་བ་ནི་དེ་ཁོ་ན་ཉིད་རྟོགས་པས་སེམས་ཞུ་བར་གྱུར་པའོ།།

[Block 384]
དྲུག་པའི་བདག་ཉིད་ནི་རྡོ་རྗེ་འཛིན་པའོ།།

[Block 385]
སྙོམས་པར་ཞུགས་པའི་བདག་ཨཱ་ལི་ཀཱ་ལི་ཞེས་བྱ་བ་ནི་གཡས་དང་གཡོན་པའི་རྩའོ།།

[Block 386]
ནམ་མཁའི་གཏོས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་མངོན་པར་རྟོགས་པའི་རིམ་པས་བསྟན་པ་ཡིན་པར་བརྗོད་དོ།།

[Block 387]
འདིའི་དོན་ནི་རྡོ་རྗེ་སེམས་དཔའ་ཆུར་ཞུ་བའི་འོད་ཟེར་གྱིས་སེམས་ཅན་ཐམས་ཅད་ལ་རེག་པས་དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱས་པའི་ས་བསྒུལ་བའི་དེ་མ་ཐག་པར་ཀུན་བཞེངས་པར་གྱུར་ཏེ། དེ་བཞིན་གཤེགས་པ་རྡོ་རྗེ་འཛིན་པའི་སྤྱོད་པ་ལ་བཅོམ་ལྡན་འདས་ཉམས་སུ་བསྟར་ནས་བཞུགས་པ་ན༌[^160]ངོ་མཚར་དུ་ཆེའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བརྗོད་པ་ཡིན་ནོ།།

[Block 388]
དེ་ལྟར་བསྟན་པ་མཛད་ནས་གསུང་གི་རྡོ་རྗེ་ལ་བསྟོད་པར་མཛད་པ་རྡོ་རྗེ་ཆོས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟོན་ཏོ།།

[Block 389]
རྡོ་རྗེ་ཆོས་ཞེས་བྱ་བའི་ཚིག་ནི་ཕྱག་ན་རྡོ་རྗེ་ལ་བྱ་བ་ཡིན་ནོ།།

[Block 390]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་བཅུ་བདུན་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།
--- END BLOCKS ---
