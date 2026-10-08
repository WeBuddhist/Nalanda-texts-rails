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

[Block 461]
གཟུང་དང་འཛིན་པ་རྣམ་པར་སྤངས། །

[Block 462 [VERSE]]
ཞེས་པ་ནི་དེའི་ནང་ཁོང་སྟོང་གི་རྣམ་པའོ། །
ཡང་ན་ནི་ཨ་ཐ་སྟེ་དེ་ནས་སོ། །

[Block 463]
ཐམས་ཅད་ནི་ལུས་ཐམས་ཅད་དོ། །

[Block 464]
ཐབས་ནི་རིན་པོ་ཆེའི་ཟེ་འབྲུའི་བདེ་བ་གནས་པའི་ཐབས་སོ། །

[Block 465]
དངོས་པོའི་མཚན་ཉིད་དུ་ནི་བརྟག །ཅེས་པ་ནི་དངོས་པོ་ཞུ་བ་དང་མཚན་ཉིད་བདེ་བ་ལྷན་ཅིག་སྐྱེས་པའི་ངོ་བོ་བླ་མའི་མན་ངག་ནི་བསྒོམ་པས་བརྟག་པའོ། །

[Block 466 [HEADING]]
###### **རང་ལུས་ཐབས་དང་ལྡན་པ།** ^1-1-5-2-1-2-2-2-2-2-0

[Block 467]
དེ་ལ་རང་ལུས་ཐབས་དང་ལྡན་པ་ནི་སྲིད་པ་གསུམ་གྱི་རྩ་གསུམ་མོ། །

[Block 468 [VERSE]]
ཡོངས་གྱུར་ནི་སྐྱེ་གནས་གྲུ་གསུམ་མོ། །
ཐམས་ཅད་དེ་ལུས་ཀུན་འདུས་པའོ། །
གཟུང་དང་འཛིན་པ་རྣམ་པར་སྤང་། །

[Block 469]
ཞེས་པ་ནི་ནང་ཁོང་སྟོང་ལྟ་བུའམ། ཡང་ན༌[^166]འོག་ན་གནས་པ་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡིན་པས་སོ། །

[Block 470 [VERSE]]
ཨ་ཐ་ནི་ཨ་ཀྲ་སྟེ་དེ་ལའོ། །
ཐབས་ནི་བདེ་བ་ཆེན་པོའི་གནས་སོ། །
ཐམས་ཅད་ནི་ལུས་ཀུན་ཞུ་བའོ། །
དངོས་པོའི་མཚན་ཉིད་དུ་ནི་བརྟག །

[Block 471]
ཅེས་པ་སྔ་མ་ལྟར་ལྷན་ཅིག་སྐྱེས་པ་བསྒོམ་པའོ། །

[Block 472 [HEADING]]
###### **གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོ།** ^1-1-5-2-1-2-2-2-2-3-0

[Block 473]
གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོ་ལ་གཉིས་ཏེ། བརྟེན་པ་ཆོས་ལ་འཇུག་པ་དང་། རྟེན་ནང་ནས་འཇུག་པའོ། །

[Block 474 [HEADING]]
###### **བརྟེན་པ་ཆོས་ལ་འཇུག་པ།** ^1-1-5-2-1-2-2-2-2-3-1-0

[Block 475]
བརྟེན་པ་ཆོས་ལ་འཇུག་པ་ནི་ཤེས་རབ་དང་ཐབས་དབྱེར་མེད་པའོ། །

[Block 476]
དེ་ལ་ཤེས་རབ་ནི་སྲིད་གསུམ་སྟེ་ཁམས་གསུམ་མོ། །

[Block 477]
ཡོངས་གྱུར་ནི་གཅིག་དང་དུ་མ་དང་བྲལ་བའི་སྦྱོར་བས་རང་བཞིན་མེད་པས་ཐམས་ཅད་ཡོངས་སུ་གྱུར་པའོ། །

[Block 478]
དེ་ལ་ཤེས་རབ་ཀྱི་ཇི་ལྟར་བལྟ་ཞེ་ན། དེའི་ཕྱིར། གཟུང་དང་འཛིན་པ་རྣམ་པར་སྤང་། །ཞེས་གསུངས་སོ། །

[Block 479]
དེ་ལ་ཐབས་ཀྱི་ཇི་ལྟར་བལྟ་ཞེ་ན། ཕ་རོལ་ཕྱིན་པའི་ཐེག་པ་ལྟར་གཅིག་དང་དུ་བྲལ་ལ་སོགས་པ་སྦྱོར་བ་ལ་མི་ལྟོས་པས་ཨ་ཐ་བ་སྟེ། རྣམ་གྲངས་སམ་ཐབས་སྣང་བའི་བདག་ཉིད་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ཚད་མེད་པ་ལ་སོགས་པའི་དངོས་པོའི་མཚན་ཉིད་དུ་བརྟག་པའོ། །

[Block 480 [HEADING]]
###### **རྟེན་ནང་ནས་འཇུག་པ།** ^1-1-5-2-1-2-2-2-2-3-2-0

[Block 481]
ཡང་ན། སྲིད་གསུམ་ཡོངས་གྱུར་ཐམས་ཅད་ནི། །ཞེས་པ་ནི་ལུས་ངག་ཡིད་གསུམ་གྱི་ཁམས་གཉུག་མའི་ཨ་ཝ་དྷཱུ་ཏཱི་དེས་བསྡུས་པའོ། །

[Block 482]
གཟུང་དང་འཛིན་པ་རྣམ་པར་སྤང་།[^167] །ཞེས་པ༌[^168]ནི་དེར་སྐྱེས་པའི་ཡེ་ཤེས་ཀྱི་རྟོག་པ་གཅོད་ཅིང་མི་རྟོག་པ་སྐྱེ་བའོ། །

[Block 483]
ཐབས་ནི་ཞེས་པ་ནི་བདེ་བའི་རོར་རང་སྣང་བས་མི་རྟོག་པ་རང་རྣལ་དུ་འཇུག་པའོ། །

[Block 484]
ཐམས་ཅད་ཀྱི་ཞེས་པ་ནི་ཐབས་དང་ཤེས་རབ་དབྱེར་མེད་དོ། །

[Block 485]
དེ་ལྟ་བུའི་ཡེ་ཤེས་ཆེན་པོ་དེ་གང་དུ་གནས་ཤིང་བརྟེན་ཞེ་ན། དེའི་ཕྱིར། དངོས་པོའི་མཚན་ཉིད་དུ་ནི་བརྟག །ཅེས་པ་སྟེ། དངོས་པོ་ནི་བསྟན་དུ་མེད་ལ་ཐོགས་པ་མེད་པའི་གཟུགས་གཉུག་མའི་དབང་པོའོ། །

[Block 486]
མཚན་ཉིད་ནི་དེར་གནས་པའི་ཡེ་ཤེས་ཆེན་པོའོ། །

[Block 487]
དུ་ནི་བརྟག་ཅེས་པ་སྟེ་དབང་པོ་རང་སྣང་བ་དང་ཡེ་ཤེས་རང་འབར་བའི་མན་ངག་གོ། །

[Block 488]
དེ་རྣམས་ལ་ཆོ་ག་ཁ་བསྐང་བ་སྔ་མ་དང་འདྲའོ། །

[Block 489 [HEADING]]
###### **རྟགས།** ^1-1-5-2-1-2-2-3-0

[Block 490]
དེ་རྣམས་ཀྱི་རྟགས་ནི་གསུམ་སྟེ།

[Block 491 [VERSE]]
མི་འགྱུར་བ་ནི་ལྟ་བའི་རྟགས་སོ། །
དངོས་པོ་ཀུན་ལ་ཆགས་མེད་དྲོད། །
འཇིག་རྟེན་ཆོས་བརྒྱད་སྤངས་པ་ནི། །
སྤྱོད་པའི་རྟགས་སུ་ཤེས་པར་བྱ། །

[Block 492]
ཞེས་པའོ། །

[Block 493 [HEADING]]
###### **སྡོམ་པའི་དབྱེ་བ།** ^1-1-5-2-1-2-3-0

[Block 494]
སྡོམ་པའི་དབྱེ་བ་ལ་དོན་གཉིས་ཏེ། བཤད་ཚུལ་སྦྱར་བ་དང་བརྟག་པ༌[^169]ཕྱི་མའི་རྒྱུ་མཚན་བཏུ་བའོ། །

[Block 495 [HEADING]]
###### **བཤད་ཚུལ་སྦྱར་བ།** ^1-1-5-2-1-2-3-1-0
--- END BLOCKS ---
