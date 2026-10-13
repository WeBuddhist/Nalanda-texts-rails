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
[Block 561 [HEADING]]
###### **བཤད་ཚུལ་སྦྱོར་བ།** ^1-1-5-2-1-2-4-2-2-0

[Block 562]
བཤད་པའི་ཚུལ་སྦྱར་བ་ལ་ཡང་གཉིས་ཏེ། བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པའོ། །

[Block 563 [HEADING]]
###### **བསྐྱེད་པའི་རིམ་པ།** ^1-1-5-2-1-2-4-2-2-1-0

[Block 564]
དེ་ལ་བསྐྱེད་པ་ལ་ཡང་ལྟེ་བར་ནི་སྣ་ཚོགས་པདྨའོ། །

[Block 565 [VERSE]]
གཏུམ་མོ་ནི་རང་གི་རིག་མའོ། །
ཨཱ་ལི་ཟླ་བ་ཅན་རྡོ་རྗེ་སེམས་དཔའོ། །
འབར་བ་ནི་དེ་གཉིས་རྗེས་སུ་ཆགས་པའོ། །
དེ་བཞིན་གཤེགས་པ་ནི་ཕུང་པོ་ལྔ་སྟེ།

[Block 566]
རྡོ་རྗེ་སེམས་དཔའ་ལ་ཡོད་པའོ། །

[Block 567]
སྤྱན་ལ་སོགས་པ་ནི་འབྱུང་བ་ལྔ་སྟེ་རིག་མ་ལ་ཡོད་པའོ། །

[Block 568]
བསྲེགས་པ་ནི་ཆགས་པས་ཞུ་བའོ། །

[Block 569]
རི་བོང་ཅན་ནི་ཁུ་བའི་མིང་གི་རྣམ་གྲངས་སོ། །

[Block 570]
འཛག་པ་ནི་ཐིག་ལེ་བཞི་ཆད་པའོ། །

[Block 571]
ཧཾ་ནི་བསྐུལ་བའི་གླུའོ། །

[Block 572 [HEADING]]
###### **རྫོགས་པའི་རིམ་པ།** ^1-1-5-2-1-2-4-2-2-2-0

[Block 573]
རྫོགས་པའི་རིམ་པ་ལ་གསུམ་སྟེ། གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་དང་། རང་ལུས་ཐབས་དང་ལྡན་པ་དང་གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོའོ། །

[Block 574 [HEADING]]
###### **གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ།** ^1-1-5-2-1-2-4-2-2-2-1-0

[Block 575]
དེ་ལ་ཤེས་རབ་ལ་བརྟེན་པ༌[^185]ཡང་ཙཎྜ་ལཱི་ཉི་མ། ཨཱ་ལི་ནི་ཟླ་བའོ། །

[Block 576]
ལྟེ་བ་ནི་རིན་པོ་ཆེའི་ཟེ་འབྲུ་དང་བྱ་རོག་གི་གདོང་ཅན་ནོ། །

[Block 577]
འབར་པ་ནི་ཆགས་པས་བསྐྱེད་པའོ། །

[Block 578]
དེ་བཞིན་གཤེགས་པ་ལྔ་ནི་ལུས་ཅན་གྱིས་བསྡུས་པ་བཅུད་ཀྱི་འཇིག་རྟེན་ནོ། །

[Block 579]
སྤྱན་ལ་སོགས་པ་ནི་འབྱུང་བས་བསྡུས་པ་སྣོད་ཀྱི་འཇིག་རྟེན་ནོ། །

[Block 580]
བསྲེགས་པ་ནི་ཐ་མལ་པ་མི་དམིགས་པར་འཇུ་བར་བྱེད་པའོ། །

[Block 581]
རི་བོང་ཅན་ནི་ཞུ་བའོ། །

[Block 582]
ཧཾ་ནི་བདེ་བ་ཆེན་པོའི་གནས་ལ་ཡོད་པའོ། །

[Block 583]
འཛག་པ་ནི་དེ་ལ་རྒྱུ་བའོ། །

[Block 584 [HEADING]]
###### **རང་ལུས་ཐབས་དང་ལྡན་པ།** ^1-1-5-2-1-2-4-2-2-2-2-0

[Block 585]
རང་ལུས་ཐབས་ཀྱི་བསྒོམ་པ་རྩ་དང་འཁོར་ལོར་གནས་པ་དེ་ཡང་ལྟེ་བར་ཨཾ་ལས་རླུང་དང་མེ་སྦར་ཏེ༌[^186]འོད་ཟེར་ལངས་པས་དེ་བཞིན་གཤེགས་པ་ལྔ་བསྲེགས་ཏེ། རྣམ་པ་དང་དོན་དང་མིང་རྣམས་ཀྱང་བསྲེགས་པའོ། །

[Block 586]
མགྲིན་པར་སྤྱན་ལ་སོགས་པ་ཡང་རྣམ་པ་དང་། དོན་དང་མིང་རྣམས་བསྲེགས་ནས་སྨིན་ཕྲག་ནས་བྱུང་ནས༌[^187]དེ་བཞིན་གཤེགས་པ་རྣམས་འོད་ཟེར་དུ་བཀུག་སྟེ་ཧཾ་ལ་ཐིམ་པས་ཆ་དང་ཆ་མེད་དུ་སོང་ནས་སུམ་ཅུ་རྩ་གཉིས་མཐའ་བདེ་བ་འབྱུང་བ་དང་ཧཾ་ཞུ་ནས་རྐན་ལ་སོགས་པར་ཁྱབ་པར་བྱས༌[^188]ཏེ་དྲི་ཆེན་བུ་ག་ནས་བྱུང་ནས། དེ་ནས་མགྲིན་པར་སོང་སྟེ་ངལ་བསོས་རང་གི་ཡི་གེ་རྣམས་གསོས། སྙིང་གར་དབུགས་ཕྱུང་སྟེ་སྔ་མ་བཞིན་བྱས། ལྟེ་བའི་ཨཾ་དེ་སོས་ཀའི་གླང་པོ་ཚད་པས་གདུངས་པ་ལ་བུམ་པ་བརྒྱ་ཡིས་ཁྲུས་གསོལ་བའམ། བཙུན་མོ་རྒྱན་གྱིས༌[^189]བརྒྱན་པ་འདོད་པས་གདུངས་པ་ལ་ཚིམ་པར་བྱས་པ་ལྟར་བདེ་བ་དང་དགའ་བར་འགྱུར་རོ། །

[Block 587 [HEADING]]
###### **གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོ།** ^1-1-5-2-1-2-4-2-2-2-3-0

[Block 588]
གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོ་ཡང་ཙཎྜ་ལཱི་ནི་སྤྲོས་པའི་རང་བཞིན་ལ་གཏུམ་པའོ། །

[Block 589]
ཨཱཾ་ལཱི་ནི་མོ་རྟགས་ཏེ་ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པའོ། །

[Block 590]
ལྟེ་བ་ནི་སའི་དཀྱིལ་འཁོར་སྤྲུལ་པའི་འཁོར་ལོ་དང་ནམ་མཁའི་དཀྱིལ་བདེ་ཆེན་གྱི་འཁོར་ལོ་ལྟེ་བར་ཟུག༌[^190]ཅིང་གནས་པའོ། །

[Block 591]
འབར་བ་ནི་མཆོག་གི༌[^191]དབང་པོ་དང་བའམ། ཡེ་ཤེས་རང་འབར་བའོ། །

[Block 592]
དེ་བཞིན་གཤེགས་པ་ལྔ་བསྲེགས་པ༌[^192]ནི་སེམས་ཡོངས་སུ་རྫོགས་པ་ཡེ་ཤེས་ལྔའི་རང་བཞིན་ཡང་དབྱེར་མེད་པས་བསྲེགས་ཏེ་བདེ་ཆེན་རྡོ་རྗེ་སེམས་དཔར་གྱུར་པའོ། །

[Block 593]
སྤྱན་ལ་སོགས་པ་ནི་ལུས་རྫོགས་པ་འབྱུང་བ་ལྔའོ། །

[Block 594]
བསྲེགས་པ་ནི་ཞུ་བའི་ཐིག་ལེར་དབྱེར་མེད་པས་རྡོ་རྗེ་སེམས་དཔར་གྱུར་པའོ། །

[Block 595]
རི་བོང་ཅན་ནི་རྡོ་རྗེ་སེམས་དཔའ་ཉིད་ཀྱི་མིང་གི་རྣམ་གྲངས་སོ། །

[Block 596]
ཧཾ་ནི་བདེ་བ་ལྷན་ཅིག་སྐྱེས་པའི་རླུང་དང་བཅས་པའོ། །

[Block 597]
འཛག་པ་ནི་ནང་དུ་འབར་བ་སྟེ་བདེ་གསལ་མི་རྟོག་པའོ། །

[Block 598]
ལེའུའི་མཚན་ཡང་ཕྱོགས་རེ་རེ་ནས་བརྟགས་པ༌[^193]ཕལ་ཆེར་ཡིན་ཡང་འདིར་ནི་ཀུན་ལ་སྦྱར་ཏེ་དང་པོ་གླེང་གཞི་ཡང་པ་རི་ཝརྟ༌[^194]ཞེས་བྱ་སྟེ། བརྗེ་བའམ་རྣམ་པར་འཕྲོག་པའོ། །

[Block 599 [VERSE]]
དེས་ན་རྡོ་རྗེ་ནི་དགྱེས་པའི་རྡོ་རྗེའོ། །
རིགས་ནི་འཁོར་ལ་སོགས་པའི་ཡན་ལག་གོ། །
ལེའུ་ནི་སྟོན་པ་ལ་འཁོར་དུ་འཕྲོ་ཞིང་བརྗེ་བའམ།

[Block 600]
སྟོན་པ་ལ་སོགས་པ་རྣམ་པར༌[^195]ཕྱེ་བའོ། །
--- END BLOCKS ---
