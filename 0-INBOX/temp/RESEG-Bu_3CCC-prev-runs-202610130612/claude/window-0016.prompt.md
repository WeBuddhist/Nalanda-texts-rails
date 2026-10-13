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
[Block 561]
ཅིའི་ཕྱིར་ཞེ་ན། མི་སྲིད་པའི་ཕྱིར་ཏེ། གལ་ཏེ་མཚན་ཉིད་དང་བཅས་ན་ནི་མཚན་ཉིད་མེད་པ་མ་ཡིན་ལ། ཅི་སྟེ་མཚན་ཉིད་མེད་ན་ནི་མཚན་ཉིད་དང་བཅས་པ་མ་ཡིན་པས་དེའི་ཕྱིར་མཚན་ཉིད་དང་བཅས་པ་དང་མཚན་ཉིད་མེད་པ་ཞེས་བྱ་བ་དེ་ནི་དགག་པར་མི་མཐུན་པ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་མི་སྲིད་པ་ཁོ་ནའི་ཕྱིར་མཚན་ཉིད་དང་བཅས་པ་དང་མཚན་ཉིད་མེད་པ༌[^352]གཞན་ལ་ཡང་མཚན་ཉིད་འཇུག་པར་མི་འཐད་དོ། །

[Block 562 [VERSE]]
མཚན་ཉིད་འཇུག་པ་མ་ཡིན་ན། །
མཚན་གཞི་འཐད་པར་མི་འགྱུར་རོ། །

[Block 563]
མཚན་ཉིད་འཇུག་པ་མ་ཡིན་ན་མཚན་ཉིད་ཀྱི་གཞི་ཡང་འཐད་པར་མི་འགྱུར་ཏེ། འདི་ལྟར་ཁྱོད་ཀྱིས་མཚན་ཉིད་དང་ལྡན་པ་ལས་ཁམས་རབ་ཏུ་འགྲུབ་པར་བསྟན་ན་མཚན་ཉིད་དང་ལྡན་པ་དེ་ཡང་མཚན་ཉིད་མི་འཇུག་པའི་ཕྱིར་མི་འཐད་དོ། །

[Block 564]
དེ་མེད་ན་ཁྱོད་ཀྱི་མཚན་ཉིད་ཀྱི་གཞི་གང་གིས་འགྲུབ་པར་འཐད།

[Block 565]
སྨྲས་པ། དེ་རེ༌[^353]ཞིག་མཚན་ཉིད་ནི་ཡོད་དེ། མཚན་ཉིད་ཡོད་པས་མཚན་ཉིད་ཀྱི་གཞི་ཡང་རབ་ཏུ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 566]
བཤད་པ།

[Block 567 [VERSE]]
མཚན་གཞི་འཐད་པ་མ་ཡིན་ན། །
མཚན་ཉིད་ཀྱང་ནི་ཡོད་མ་ཡིན། །

[Block 568]
འདི་ལ་མཚན་ཉིད་ཀྱི་གཞི་ལ་བརྟེན་ནས་མཚན་ཉིད་དུ་འགྱུར་ན་མཚན་ཉིད་ཀྱི་གཞི་དེ་ཡང་མི་འཐད་དོ། །

[Block 569]
མཚན་ཉིད་ཀྱི་གཞི་མེད་ན་གཞི་མེད་པའི་མཚན་ཉིད་ཇི་ལྟར་འཐད། དེ་ལྟ་བས་ན་མཚན་ཉིད་ཀྱང་ཡོད་པ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 570 [VERSE]]
དེ༌[^354]ཕྱིར་མཚན་གཞི་ཡོད་མིན་ཏེ། །
མཚན་ཉིད་ཡོད་པ་ཉིད་མ་ཡིན། །

[Block 571]
དེ་ལྟར་གང་གི་ཕྱིར་རྣམ་པ་ཐམས་ཅད་དུ་བརྟགས་ན་མཚན་ཉིད་འཇུག་པར་མི་འཐད་པ་དེའི་ཕྱིར་མཚན་ཉིད་ཀྱི་གཞི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 572]
གང་གི་ཕྱིར་མཚན་ཉིད་ཀྱི་གཞི་ཡོད་པ་མ་ཡིན་པ་དེའི་ཕྱིར་གང་ཞིག་མེད་པའི་མཚན་ཉིད་ཀྱང་ཡོད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 573]
སྨྲས་པ། འདི་ནི་མཚན་ཉིད་ཀྱི་གཞིའོ། །

[Block 574]
འདི་ནི་མཚན་ཉིད་དོ། །ཞེས་བྱ་བ་དེ་བརྗོད་པར་མི་ནུས་མོད་ཀྱི། འོན་ཀྱང་རེ་ཞིག་དངོས་པོ་ནི་ཡོད་དོ། །

[Block 575]
བཤད་པ།

[Block 576 [VERSE]]
མཚན་གཞི་མཚན་ཉིད་མ་གཏོགས་པའི། །
དངོས་པོ་ཡང༌[^355]ནི་ཡོད་མ་ཡིན། །

[Block 577]
གལ་ཏེ་དངོས་པོ་འགའ་ཞིག་ཡོད་པར་འགྱུར༌[^356]ན་མཚན་ཉིད་ཀྱི་གཞི་འམ་མཚན་ཉིད་གཅིག་ཏུ་འགྱུར་གྲང་ན། གང་མཚན་ཉིད་ཀྱི་གཞི་ཡང་མ་ཡིན་ལ་མཚན་ཉིད་ཀྱང་མ་ཡིན་པ་དེ་ནི་ཡོད་པ་ཉིད་མ་ཡིན་པ་དེའི་ཕྱིར་མཚན་ཉིད་ཀྱི༌[^357]གཞི་དང་མཚན་ཉིད་མ་གཏོགས་པའི་དངོས་པོ་འགའ་ཡང་ཡོད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 578]
སྨྲས་པ། དངོས་པོ་ནི་ཡོད་པ་ཉིད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་མེད་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 579]
འདི་ལ་ཁྱོད་ན་རེ་མཚན་ཉིད་ཀྱི་གཞི་དང་མཚན་ཉིད་དག་མེད་དོ་ཞེས་ཟེར་བ་དེ་ནི་དངོས་པོ་ལ་ལྟོས༌[^358]པ་ཡིན་ཏེ། དེའི་ཕྱིར་གང་གི་དངོས་པོ་མེད་དོ་ཞེས་བརྗོད་པའི་དངོས་པོ་དེ་ནི་འགའ་ཞིག་ཡོད་པས་དེ་ལྟ་བས་ན་དངོས་པོ་མེད་པ་ཡོད་པའི་ཕྱིར་དངོས་པོ་ཡོད་པ་ཉིད་དོ། །

[Block 580]
བཤད་པ་ལེགས་པར་བརྗོད་དོ། །

[Block 581]
གལ་ཏེ་དངོས་པོ་མེད་པ་ཡོད་ན་ནི་དངོས་པོ་ཡང་ཡོད་པར་འགྱུར་བ་ཞིག་ན། དངོས་པོ་མེད་པ་ཡོད་པ་མ་ཡིན་པས་དངོས་པོ་ཡོད་པར་ག་ལ་འགྱུར། ཇི་ལྟར་ཞེ་ན།

[Block 582 [VERSE]]
དངོས་པོ་ཡོད་པ་མ་ཡིན་ན། །
དངོས་མེད་གང་གི་ཡིན་པར་འགྱུར། །

[Block 583]
སྔར།

[Block 584 [VERSE]]
མཚན་གཞི་མཚན་ཉིད་མ་གཏོགས་པའི། །
དངོས་པོ་ཡང་ནི་ཡོད་མ་ཡིན། །

[Block 585]
ཞེས་བསྟན་པས་དངོས་པོ་དེ༌[^359]ཡོད་པ་མ་ཡིན་ན་ཁྱོད་ཀྱི་དངོས་པོ་མེད་པ་དེ་གང་གི་ཡིན་པར་བརྟག །འདི་ལྟར་དངོས་པོའི་དངོས་པོ་མེད་པར་འགྱུར་གྲང་ན། དངོས་པོ་དེ་ཡང་ཡོད་པ་མ་ཡིན་ན་དངོས་པོ་མེད་པ་དེ་གང་གི་ཡིན་པར་འགྱུར། དེ་ལྟ་བས་ན་དངོས་པོ་མེད་པའི་ཕྱིར་དངོས་པོ་མེད་པ་ཡང་མེད་དོ། །

[Block 586]
སྨྲས་པ། གང་གི་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དེ་དག་ཤེས་པར་བྱེད་ཅིང་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་རྟོག་པར་བྱེད་པ་དེ་ནི་རེ་ཞིག་ཡོད་དོ། །

[Block 587]
དེ་ཡོད་པས་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་ཀྱང་རབ་ཏུ་འགྲུབ་པ་ཉིད་དོ། །

[Block 588]
བཤད་པ།

[Block 589 [VERSE]]
དངོས་དང་དངོས་མེད་མི་མཐུན་ཆོས། །
གང་གིས་དངོས་དང་དངོས་མེད་ཤེས། །

[Block 590]
མི་མཐུན་པའི་ཆོས་ནི་དེ་དག་མི༌[^360]བཟློག་པའི་ཆོས་ཏེ། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་གི་མི་མཐུན་པའི་ཆོས་ནི་དངོས་པོ་དང་དངོས་པོ་མེད་པ༌[^361]མི་མཐུན་པའི་ཆོས་སོ། །

[Block 591]
དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་གི་མི་མཐུན་པའི་ཆོས་གང་ཡིན་ཞེ་ན། དངོས་པོ་ཡང་མ་ཡིན་ལ་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་པའོ། །

[Block 592]
དེ་ལ་གལ་ཏེ་འགའ་ཞིག་ཡོད་པར་འགྱུར༌[^362]ན་དངོས་པོའི་ཆོས་སམ། དངོས་པོ་མེད་པའི་ཆོས་ཤིན་ཏུ་འགྱུར་གྲང་ན། གང་དངོས་པོའི་ཆོས་ཀྱང་མ་ཡིན་ལ་དངོས་པོ་མེད་པའི་ཆོས་ཀྱང་མ་ཡིན་པ་དེ་ནི་ཡོད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 593]
དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག༌[^363]དང་མི་མཐུན་པའི་ཆོས་དེ་མེད་ན་གང་གིས༌[^364]དངོས་པོ་དང་དངོས་པོ་མེད་པ་དེ་དག་ཤེས་པར་བརྟག །དེ་ལྟ་བས་ན་དངོས་པོ་དང་དངོས་པོ་མེད་པར༌[^365]ཤེས་པ་ཡང་མེད་དོ། །

[Block 594 [VERSE]]
དེ་ཕྱིར་ནམ་མཁའ་དངོས་པོ་མིན། །
དངོས་མེད་མ་ཡིན་མཚན་གཞི་མིན། །

[Block 595]
མཚན་ཉིད་མ་ཡིན། །དེ་ལྟར་གང་གི་ཕྱིར་བརྟགས་ན་མཚན་ཉིད་ཀྱི་གཞི་དང་མཚན་ཉིད་དག་མེད་ཅིང་། མཚན་ཉིད་ཀྱི་གཞི་དང་མཚན་ཉིད་དག་མ་གཏོགས་པའི་དངོས་པོ་གཞན་ཡང་མེད་དོ། །

[Block 596]
དངོས་པོ་མེད་ན་དངོས་པོ་མེད་པ་ཡང་མེད་པ་དེའི་ཕྱིར་ནམ་མཁའ་ནི་དངོས་པོ་ཡང་མ་ཡིན་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན། མཚན་ཉིད་ཀྱི་གཞི་ཡང་མ་ཡིན་མཚན་ཉིད་ཀྱང་མ་ཡིན་ནོ། །

[Block 597]
འདི་ལྟར་གལ་ཏེ་ནམ་མཁའ་ཞེས་བྱ་བ་ཅུང་ཞིག་ཡོད་པར་གྱུར་ན་དེ་བཞི་པོ་དེ་དག་ལས་གང་ཡང་རུང་བ་ཞིག་ཏུ་འགྱུར་གྲང་ན། བཞི་པོ་དེ་དག་ཀྱང་མེད་པས་དེའི་ཕྱིར་ནམ་མཁའ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 598]
ཁམས་ལྔ་པོ། །

[Block 599 [VERSE]]
གཞན་གང་དག་ཀྱང་ནམ་མཁའ་མཚུངས། །
ནམ་མཁའ་མཚུངས་ཞེས་བྱ་བ་ནི། །

[Block 600]
ནམ་མཁའ་དང་མཚུངས་པ་སྟེ། ཇི་ལྟར་ནམ་མཁའ་བརྟགས་ན་དངོས་པོ་ཡང་མ་ཡིན། དངོས་པོ་མེད་པ་ཡང་མ་ཡིན། མཚན་ཉིད་ཀྱི་གཞི་ཡང་མ་ཡིན་མཚན་ཉིད་ཀྱང་མ་ཡིན་ཏེ། ནམ་མཁའ་ཞེས་བྱ་བ་ནི༌[^366]ཅི་ཡང་མ་ཡིན་པ་དེ་བཞིན་དུ་ས་ལ་སོགས་པ་ཁམས་ལྔ་པོ་གཞན་དག་གང་ཡིན་པ་དེ་དག་ཀྱང་དངོས་པོ་ཡང་མ་ཡིན། དངོས་པོ་མེད་པ་ཡང་མ་ཡིན། མཚན་ཉིད་ཀྱི་གཞི་ཡང་མ་ཡིན། མཚན་ཉིད་ཀྱང་མ་ཡིན་ཏེ། དངོས་པོ་འགའ་ཡང་ཡོད་པ་མ་ཡིན་པས་དེའི་ཕྱིར་ཁམས་རྣམས་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
