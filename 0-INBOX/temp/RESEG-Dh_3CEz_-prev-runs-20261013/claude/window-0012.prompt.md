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
[Block 421 [HEADING]]
###### **རྟེན་རྡོ་རྗེའི་ལུས་ལམ་དུ་བྱེད་པ།** ^1-1-5-2-1-2-2-0

[Block 422]
རྟེན་རྡོ་རྗེའི་ལུས་བསྟན་པ་ནི་ལུས་ལ་ཞེས་པ་ལ་སོགས་པ་སྟེ། རྡོ་རྗེ་སྙིང་པོས་གསོལ་པ་ཞེས་པ། ཀྱེ༌[^154]རྡོ་རྗེའི་ལུས་ལ་རྩ་དུ་ལགས། ཞེས་པ་ནི་དགྱེས་པའི་རྡོ་རྗེར་འབྲེལ་ལོ། །

[Block 423]
ཀུན་བརྟགས་ཀྱི་ལུས་ལ་ཀུན་བརྟགས་ཀྱི་རྩ་དུ་མཆིས་པ་དང་། གཞན་དབང་གི་ལུས་ལ་གཞན་དབང་གི་རྩ་དུ་མཆིས་པ་དང་། ཡོངས་གྲུབ་ཀྱི་ལུས་ལ་ཡོངས་གྲུབ་ཀྱི་རྩ་དུ་མཆིས་ཞེས་དགོངས་པའོ། །

[Block 424]
ལན་དུ་རྩ་སུམ་ཅུ་རྩ་གཉིས་ཏེ་ཕྱིར་ལེན༌[^155]བཏབ་སྟེ་ཀུན་བརྟགས་ཀྱི་ལུས་ལ་རྩ་སུམ་ཅུ་རྩ་གཉིས་གང་ཞེ་ན། མི་ཕྱེད་མ༌[^156]ཞེས་བྱ་བ་ལ་སོགས་པ་བྱང་ཆུབ་ཀྱི་སེམས་སུམ་ཅུ་རྩ་གཉིས་འབབ་པའོ་ཞེས་བྱ་བར་སྦྱར་ཏེ་རྣལ་འབྱོར་གྱི་ཀུན་རྫོབ་བོ། །

[Block 425]
ཀུན་བརྟགས་ཀྱི་ལུས་ལ་ཡང་སུམ་ཅུ་རྩ་གཉིས་ཏེ། ཡང་མི་ཕྱེད་མ་དང་ཕྲ་གཟུགས་མ༌[^157]ལ་སོགས་པ་སྟེ། ཁམས་དང་ཉེ་བའི་ཁམས་བསྐྱེད་པའོ། །

[Block 426 [HEADING]]
###### **རྣམ་པར་གཞག་པ།** ^1-1-5-2-1-2-2-1-0

[Block 427]
དེ་ལ་རྣམ་པར་གཞག་པའི་ནི་གྲངས་དང་ལས་དང་སོ་སོའི་མཚན་ཉིད་དང་གནས་དང་། གཙོ་བོ་དང་། ཕལ་བར་དབྱེ་བའོ། །

[Block 428 [HEADING]]
###### **གྲངས།** ^1-1-5-2-1-2-2-1-1-0

[Block 429]
དེ་ལ་གྲངས་ནི་སུམ་ཅུ་རྩ་གཉིས་ཏེ། མི་ཕྱེད་མ་དང་ཕྲ་གཟུགས་མ་ལ་སོགས་པའོ། །

[Block 430 [HEADING]]
###### **ལས།** ^1-1-5-2-1-2-2-1-2-0

[Block 431 [VERSE]]
ལས་ནི་དྲང༌[^158]ངེས་པའི་རྒྱུ་མཚན་ཏེ།
བྱང་ཆུབ་ཀྱི་སེམས་འབབ་པའི་ཕྱིར་རོ། །

[Block 432 [HEADING]]
###### **སོ་སོའི་མཚན་ཉིད།** ^1-1-5-2-1-2-2-1-3-0

[Block 433]
སོ་སོའི་མཚན་ཉིད་ནི་ཐབས་དང་ཤེས་རབ་ལ་སོགས་པའི་མཚན་ཉིད་འཛིན་པའོ། །

[Block 434 [HEADING]]
###### **གནས།** ^1-1-5-2-1-2-2-1-4-0

[Block 435]
གནས་ནི་གཡས་དང་གཡོན་ལ་སོགས་པའོ། །

[Block 436]
བརྐྱང༌[^159]མི་མོ་བསྐྱོད་པ་འབབ་པ་སྟེ། སྐྱེས་པ་ལ་གཡོན་ན་གནས་ཏེ།

[Block 437 [VERSE]]
མགྲིན་པར་གནས་ནས༌[^160]བཤང་ལམ་དུ་སེལ་བའོ། །
རོ་མ་དེ་བཞིན་ཁྲག་འབབ་ཅིང་། །

[Block 438 [VERSE]]
གཡས་ན་གནས་ཏེ་ལྟེ་བ་ལས་མགྲིན་པར་སེལ་བའོ། །
བུད་མེད་རྣམས་ལ་ནི་གོ་བཟློག༌[^161]ཤེས་པར་བྱའོ། །

[Block 439]
ཡོངས་གྲུབ་ཀྱི་རྩ་སུམ་ཅུ་རྩ་གཉིས་ནི་བཅོམ་ལྡན་འདས་རྩ་སུམ་ཅུ་རྩ་གཉིས་པོ་འདི་རྣམས་ཇི་ལྟ་བུ་ལགས་ཞེས་པ་ལ་སོགས་པ་སྟེ། རྩ་སུམ་ཅུ་རྩ་གཉིས་པོ་འདི་རྣམས་ཀྱི་སྤྱིའི་རང་བཞིན་ནམ་མཚན་ཉིད་ཇི་ལྟ་བུ་ལགས་ཞེས་དགོངས་པའོ། །

[Block 440]
དེ་རྣམས་ཀྱི་རང་བཞིན་ཡང༌[^162]སྲིད་གསུམ་ཡོངས་གྱུར་ནི་རྩ་འདི་གསུམ་དུ་གྱུར་པ་སྟེ། དེ་གཟུང་བ་དང་། འཛིན་པ་རྣམ་པར་སྤངས་ཞེས་པ་ཆོས་ཐམས་ཅད་སྟོང་པར་ཤེས་པའོ། །

[Block 441]
ཡང་ན་ཐབས་ནི༌[^163]ཐམས་ཅད་ཀྱིས།[^164] །དངོས་པོའི་མཚན་ཉིད་དུ་ནི་བརྟག །ཅེས་པ་ཐབས་རྣམ་པ་སྣ་ཚོགས་སུ་སྣང་བའོ། །

[Block 442 [HEADING]]
###### **གཙོ་བོ་དང་ཕལ་པར་དབྱེ་བ།** ^1-1-5-2-1-2-2-1-5-0

[Block 443]
གཙོ་བོ་དང་ཕལ་པར་དབྱེ་བ་ནི་གསུམ་དུ་གཞག་གོ། །

[Block 444]
དེ་ཡང་སེམས་ཅན་རེ་རེ་ལ་རྩ་བྱེ་བ་ཕྱེད་དང་བཅུ་དང་སྟོང་ཕྲག་བདུན་ཅུ་གཉིས་སུ་བསྡུས་ཏེ། དེ་ཡང་བརྒྱ་ཉི་ཤུར་བསྡུས།[^165] དེ་ཡང་སུམ་ཅུ་རྩ་གཉིས་སུ་བསྡུས་ཏེ་རྣལ་འབྱོར་མ་བཅོ་ལྔར་ཤེས་པར་བྱའོ། །

[Block 445]
དེ་ཡང་།

[Block 446 [VERSE]]
རྩ་རྣམས་བྱེ་བ་ཕྱེད་དང་བཅུ། །
ལུས་ཀྱི་ལྟེ་བའི་པདྨར་གནས། །
འཁོར་ལོ་བཞི་ཡི་གྲངས་ཀྱིས་ནི། །
བརྒྱ་དང་ཉི་ཤུ་ལྷག་པ་ཡིན། །

[Block 447 [VERSE]]
བྱང་སེམས་སུམ་ཅུ་རྩ་གཉིས་ཀྱི། །
རྩ་མཆོག་སུམ་ཅུ་རྩ་གཉིས་སོ། །

[Block 448]
ཞེས་གསུངས་སོ། །

[Block 449]
དེ་ནི་རྣམ་པར་གཞག་པའོ། །

[Block 450 [HEADING]]
###### **བཤད་པའི་ཚུལ་རྣམ་པར་སྦྱར་བ།** ^1-1-5-2-1-2-2-2-0

[Block 451]
རང་བཞིན་ནི་བཤད་པའི་ཚུལ་རྣམ་པར་སྦྱར་བ་སྟེ། བཤད་པའི་ཚུལ་སྦྱར་བ་ཡང་ཀུན་ལ་ལྡན་པ་ཡིན་ཡང་། བླ་མའི་མན་ངག་གིས་སྐབས་སོ་སོར་སྦྱར་བ་ནི། ལྗོན་ཤིང་གི་ཡལ་ག་ལྟ་བུར་ཤེས་པར་བྱའོ། །

[Block 452]
དེ་ཡང་བསྐྱེད་པའི་རིམ་པ་དང་། རྫོགས་པའི་རིམ་པའོ། །

[Block 453 [HEADING]]
###### **བསྐྱེད་པའི་རིམ་པ།** ^1-1-5-2-1-2-2-2-1-0

[Block 454]
བསྐྱེད་པའི་རིམ་པ་ནི། སྲིད་གསུམ་ཡོངས་གྱུར་ཐམས་ཅད་ནི། །ཞེས་པ་ནི་ཆོ་གའི་རིམ་པ་ཐ་མལ་གྱི་སྒོ་གསུམ་ཡོངས་སུ་གྱུར་པའོ། །

[Block 455 [VERSE]]
གཟུང་དང་འཛིན་པ་རྣམ་པར་སྤངས། །
ཞེས་པ་ནི་བདག་མེད་རྣལ་འབྱོར་ལྡན་པའོ། །
ཡང་ན་ཐབས་ནི་ཐམས་ཅད་ཀྱི། །

[Block 456]
ཞེས་པ་ནི་ཡང་ན་ཧེ་རུ་ཀ་དཔལ་མཚོན་པའོ། །

[Block 457]
དངོས་པོའི་མཚན་ཉིད་དུ་ནི་བརྟག །ཅེས་པ་ནི་ཕུང་པོ་ལ་སོགས་པའི་ཆོས་ཀུན་ཏེ་གཉིས་སྦྱོར་བ་ལས་བྱུང་བའི་ལྷའི་འཁོར་ལོར་བརྟགས་ཤིང་སྣང་བའོ། །

[Block 458 [HEADING]]
###### **རྫོགས་པའི་རིམ་པ།** ^1-1-5-2-1-2-2-2-2-0

[Block 459 [HEADING]]
###### **གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ།** ^1-1-5-2-1-2-2-2-2-1-0

[Block 460]
དེ་ལ་རྫོགས་པའི་རིམ་པ་ཡང་གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་དང་། རང་ལུས་ཐབས་དང་ལྡན་པ་དང་དབྱེར་མེད་ཕྱག་རྒྱ་ཆེན་པོའོ། །ཤེས་རབ་ལ་བརྟེན་པ་ཡང་། སྲིད་གསུམ་ཡོངས་གྱུར་ཐམས་ཅད་ནི། །ཞེས་པ་ནི་ཤེས་རབ་མའི་གསང་བའི་གནས་ཏེ་རྩ་གསུམ་ཡོངས་སུ་གྱུར་པའི་བྱ་རོག་གི་གདོང་ཅན་ནོ། །
--- END BLOCKS ---
