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

[Block 496]
བཤད་ཚུལ་སྦྱར་བ་ལ་ཡང་དོན་གསུམ་སྟེ། ངེས་པའི་ཚིག་དང་བཤད་ཚུལ་དབྱེ་བ་དང་མངོན་པར་རྟོགས་པའོ། །

[Block 497 [HEADING]]
###### **ངེས་པའི་ཚིག།** ^1-1-5-2-1-2-3-1-1-0

[Block 498]
ངེས་པའི་ཚིག་ལ་གསུམ་སྟེ། མང་བ་ཉུང་བར་སྡོམ་པ་དང་། ཕྱི་རོལ་ལུས་ལ་སྡོམ་པ་དང་། བདེ་བ་ཆེན་པོའི༌[^170]མཆོག་ཏུ་བསྟིམ་པའོ། །

[Block 499]
ཡང་གང་གིས་སྡོམ་པ༌[^171]དང་གང་དུ་སྡོམ་པ་དང་ཡང་དག་པར་སྡོམ་པའོ། །

[Block 500 [HEADING]]
###### **མང་བ་ལ་ཉུང་བར་སྡོམ་པ།** ^1-1-5-2-1-2-3-1-1-1-0

[Block 501]
དེ་ལ་མང་བ་ལ་ཉུང་བར་སྡོམ་པ་ནི་ཐབས་དང་ཤེས་རབ་ལ་སྡོམ་པ་དང་། ལུས་ངག་ཡིད་གསུམ་ལ་སྡོམ་པའོ། །

[Block 502 [HEADING]]
###### **ཕྱི་རོལ་ལུས་ལ་སྡོམ་པ།** ^1-1-5-2-1-2-3-1-1-2-0

[Block 503]
ཕྱི་རོལ་ལུས་ལ་སྡོམ་པ་ནི་འཁོར་ལོ་བཞི་ལ་སྡོམ་པའོ། །

[Block 504 [HEADING]]
###### **བདེ་བ་མཆོག་ཏུ་སྡོམ་པ།** ^1-1-5-2-1-2-3-1-1-3-0

[Block 505]
བདེ་བ་མཆོག་ཏུ་སྡོམ་པ་ནི་དགའ་བ་དང་སྐད་ཅིག་གོ།[^172] །

[Block 506 [HEADING]]
###### **བཤད་ཚུལ་དབྱེ་བ།** ^1-1-5-2-1-2-3-1-2-0

[Block 507]
བཤད་ཚུལ་དབྱེ་བ་ལ་གཉིས་ཏེ།

[Block 508 [HEADING]]
###### **བསྐྱེད་པ་ལྟར་སྦྱར་བ།** ^1-1-5-2-1-2-3-1-2-1-0

[Block 509 [VERSE]]
བསྐྱེད་པ་ལྟར༌[^173]སྦྱར་བ་དང་རྫོགས་རིམ་མོ། །
བསྐྱེད་པ་ལྷ་ལ་གཉིས་ཏེ།
ལམ་ཆོ་ག་དང་འབྲས་བུའོ། །

[Block 510 [HEADING]]
###### **ལམ་ཆོ་ག།** ^1-1-5-2-1-2-3-1-2-1-1-0

[Block 511]
དེ་ལ་ལམ་ནི་ཨཱ་ལི་ཀཱ་ལི་ཡོངས་སུ་གྱུར་པ་ལས་ཟླ་བ་དང་ཉི་མའོ། །ཤེས་རབ་དང་ཐབས་སོ། །

[Block 512]
དེས་ནི་ཆོས་ཀུན་བསྡུས་ཤིང་དབྱེ་བས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 513 [HEADING]]
###### **འབྲས་བུ།** ^1-1-5-2-1-2-3-1-2-1-2-0

[Block 514 [VERSE]]
འབྲས་བུ་ཡང་སྐུ་གསུམ་དང་རྡོ་རྗེ་གསུམ་མོ། །
དེར༌[^174]ལྷ་ཀུན་གྱི་འབྲས་བུ་འདུས་པས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 515 [HEADING]]
###### **རྫོགས་རིམ།** ^1-1-5-2-1-2-3-1-2-2-0

[Block 516]
རྫོགས་པའི་རིམ་པ་ལ་གསུམ་སྟེ། གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་དང་རང་ལུས་ཐབས་དང་ལྡན་པ་དང་དེ་ཁོ་ན་ཉིད་དང་སྦྱར་བའོ། །

[Block 517 [HEADING]]
###### **གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ།** ^1-1-5-2-1-2-3-1-2-2-1-0

[Block 518]
དེ་ཡང་གཞན་ལུས་ཤེས་རབ་ལ་སྦྱར་བ་ནི་ཨེ་ཝཾ་མ་ཡཱ་ལྷ་མོ་བཞི་སྟེ། དེ་ཉིད་ཕྱག་རྒྱ་བཞིའམ་ལྷན་སྐྱེས་ལ་སོགས་པའི་རྣལ་འབྱོར་མ་བཞིའོ། །

[Block 519]
དེས་ན་རྟེན་ཐམས་ཅད་དེར་འདུས་པས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 520 [HEADING]]
###### **རང་ལུས་ཐབས་དང་ལྡན་པ།** ^1-1-5-2-1-2-3-1-2-2-2-0

[Block 521]
རང་ལུས་དང་ཐབས་དང་ལྡན་པ་ནི་འཁོར་ལོ་བཞིའི་འདབ་མའི་གྲངས་དང་རྣམ་པ་སྟེ། དེར་ལུས་ཀུན་འདུས་པས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 522 [HEADING]]
###### **དེ་ཁོ་ན་ཉིད་དང་སྦྱར་བ།** ^1-1-5-2-1-2-3-1-2-2-3-0

[Block 523]
དེ་ཁོ་ན་ཉིད་དང་སྦྱར་བ་ལ་ཡང་ཐུན་མོང་དང་ཁྱད་པར་རོ། །

[Block 524 [HEADING]]
###### **ཐུན་མོང།** ^1-1-5-2-1-2-3-1-2-2-3-1-0

[Block 525]
ཐུན་མོང་ནི་བདེན་པ་བཞི་དང་སྡེ་པ་བཞི་སྟེ་སྡེ་པ་མཆོག་ཏུ་སྡོམ་པའོ། །

[Block 526 [HEADING]]
###### **ཁྱད་པར།** ^1-1-5-2-1-2-3-1-2-2-3-2-0

[Block 527]
ཁྱད་པར་ནི་མཆོག་དང༌[^175]མཆོག་མ་ཡིན་པ་སྟེ། དེ་ཡང་མཆོག་ནི་སྐད་ཅིག་དང་དགའ་བ་བཞིའི་བདེ་བ་མཆོག་ཏུ་སྡོམ་པའོ། །

[Block 528]
མཆོག་མ་ཡིན་པ་ནི་དེ་ཁོ་ན་ཉིད་བཞི་བདེ་བ་མཆོག་ཏུ་སྡོམ་པས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 529 [HEADING]]
###### **བརྟག་པ་ཕྱི་མའི་ཚུལ་དུ་རྒྱུ་མཚན་བསྟན་པ།** ^1-1-5-2-1-2-3-2-0

[Block 530]
བརྟག་པ་ཕྱི་མའི་ཚུལ་དུ་རྒྱུ༌[^176]མཚན་བསྟན་པ་ལ་གཉིས་ཏེ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་དང་། སངས་རྒྱས་སོ། །
--- END BLOCKS ---
