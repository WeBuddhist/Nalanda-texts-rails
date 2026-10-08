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
[Block 806]
ལྷའི་གཟུགས་སུ་གནས་སོ་ཞེས་བྱ་བ་འདིས༌[^319]ནི་རྫོགས་པའི་རིམ་པའི་སྤྱོད་ལམ་ཡང་གཟུང༌[^320]སྟེ།

[Block 807 [VERSE]]
དེ་གཉིས་ཀ་ཡང་འོག་ནས་འཆད་དོ། །
ལེའུ་བཞི་པ་སྟེ་སྔ་མ་བཞིན་ནོ།། །།

[Block 808 [HEADING]]
### ལྔ་པ་རྫོགས་པའི་རིམ་པའི་ལྷ་བསྒོམ། ^1-5-0

[Block 809]
དེ་ནས་ཞེས་པ་ནི་བསྐྱེད་པའི་རིམ་པའི་རྗེས་ཐོགས་ལའོ། །

[Block 810]
དེ་ཁོ་ན་ཉིད་ཀྱི་ལེའུ་རྫོགས་པའི་རིམ་པ་བཤད་པར་འདོད་ནས་བཤད་པར་བྱའོ་ཞེས་མཚམས་སྦྱར་བའོ། །

[Block 811]
དེ་ཁོ་ན་ཉིད་ཏཏྟྭ་སྟེ། དེ་བཞིན་དུ་རོ་གཅིག་པའམ། རང་བཞིན་ཇི་ལྟ་བ་ཉིད་དུ་བསྟན་པའམ། ཤིན་ཏུ་རོ་གཅིག་པའམ། བསྡུས་ཤིང་སྙིང་པོ༌[^321]ལྟ་བུའི་དོན་བྱེད་པས་སོ། །

[Block 812 [HEADING]]
#### ཐུན་མོང་ཤེས་རབ་ཀྱི་ལྟེ་བ་དབུ་མ་དང་ཆ་མཐུན་པར་གཏན་ལ་འབེབས་པ། ^1-5-1-0

[Block 813]
ངོ་བོས་གཟུགས་མེད་ཅེས་བྱ་བ་ལ་སོགས་པས་ནི་ལྟ་བ་ཤེས་རབ་གཙོ་བོར་སྟོན་ཏེ། དེ་ཡང་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་ཐུན་མོང་དུ༌[^322]རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ནི།

[Block 814 [VERSE]]
བདག་ལས་མ་ཡིན་གཞན་ལས་མིན། །
གཉིས་ཀ་ལས་མིན་རྒྱུ་མེད་མིན། །

[Block 815]
ཞེས་བྱ་བ་ལ་སོགས་པ༌[^323]ངོ་བོ་ཉིད་ཀྱིས་སྐྱེ་བ་བཀག་པ་དང་རང་ལས་རང་སྐྱེ་བར་མི་འཐད་དེ་རང་གྲུབ་ན་དགོས་པ་མེད། མ་གྲུབ་ན་ནུས་པ་མེད་པས་སོ། །

[Block 816]
རྒྱུ་མེད་པ་ལས་མི་འཐད་དེ་རི་བོང་གི་རྭ་དང་འདྲ་བས་གཏན་མེད་པས་སོ། །

[Block 817]
གཉིས་ཀ་ལས་ཀྱང་མི་འཐད་དེ། སྒྲུབ་པའི་ཕུང་པོ་གསུམ་པ་དང་དགག་པའི་ཕུང་པོ་གསུམ་པ་གཉིས་ཀ༌[^324]མི་སྲིད་དོ། །

[Block 818]
གཞན་ལས་སྐྱེ་ན་འདས་པ་ལས་སམ། མ་འོངས་པ་ལས་སམ། ད་ལྟར་བ་ལས་ཏེ། དེ་ལྟར་མི་འཐད་དེ༌[^325]དུས་མཉམ་པ་ལས་རྒྱུ་འབྲས་མི་སྲིད་དོ། །

[Block 819]
མ་འོངས་པ་ལས་ཀྱང་མི་འཐད་དེ་ཕྱིས་འབྱུང་བའི་ཕྱིར་ན་རྒྱུ་ཉིད་མིན་ནོ། །

[Block 820]
འོ་ན་འདས་པ་ལས་སྐྱེའོ་ཞེ་ན། ཞིག་པ་ལས་སམ་མ་ཞིག་པ་ལས་སྐྱེ་ཞེ་ན། ཞིག་པ་ལས་མ་ཡིན་ཏེ། མེད་པའི་ཕྱིར་རི་བོང་གི་རྭ་དང་འདྲའོ། །

[Block 821]
མ་ཞིག་པ་ལས་སྐྱེ་ན་དུས་མཉམ་པར་ཐལ་ལོ་ཞེས་སུན་འདོན་པ་ལ་ཕྱོགས་སྔ་མ་རྒྱུའི་དུས་ན་མ་ཞིག་པ་འབྲས་བུའི་དུས་ན་ཞིག་གོ་ཞེ་ན། དེ་ཡང་སྐད་ཅིག་མ་གཞན་ཞིག་གིས་ཆོད་དམ་མ་ཆོད། ཆོད་ན་སྔ་མ་ཞིག་པ་དེ་སྐྱེད་པར་བྱེད་པའི་རྒྱུ་མེད།[^326] མ་ཆོད་ན་ཡང༌[^327]དུས་མཉམ་དུ་འགྱུར་རོ། །

[Block 822]
བྱས་པས་དེ་རང་གི་དུས་ཀྱིས་ཆོད༌[^328]ཀྱི་གཞན་གྱི་དུས་ཀྱིས་མ་ཆོད་དོ།[^329] །སྔ་མ་ལས་སྐྱེ་བ་དུས་མི་མཉམ་པར་མི་འགྱུར་རམ་ཞེ་ན། རྒྱུ་འབྲས་གཉིས་ལ་ཡང་སྐད་ཅིག་མ་གསུམ་གྱིས་བསྡུས་ཏེ། སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་ཆ་གསུམ་ཡོད་པས་གཞན་དུས་ཀྱི་མ༌[^330]ཆོད་པ་ཁོ་ནའོ། །

[Block 823]
གང་དེ་སྐད་ཅིག་མ༌[^331]ཡིན་ན་དངོས་པོ་དེ་གཏན་མེད་པར་ཐལ་ཏེ་རི་བོང་གི་རྭ་བཞིན་ནོ། །

[Block 824]
ངོ་བོས་གཟུགས་མེད༌[^332]ནི་བུམ་པ་ལྟ་བུ་ཅིག༌[^333]ཆོས་ཅན་དུ་གཞག་སྟེ། གཅིག་དང་དུ་མ་དང་བྲལ་བའི་ཕྱིར༌[^334]ཡང་དག་པར་མེད་དེ་དཔེར་ན་སྒྱུ༌[^335]མ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 825]
གཞན་དག་གཏན་ཚིགས་མ་གྲུབ་སྟེ། བུམ་པ་ནི་ཆ་ཤས་དང་བཅས་པའི་དུས་ཡིན་ལ་ཆ་མེད་པ་གཅིག་ཡིན༌[^336]ཞེ་ན།

[Block 826]
དང་པོ་ལྟར་ཡོད་པ་མ་ཡིན་ཏེ། གཅིག་མ་ཡིན་ཏེ་ཆ་ཤས་དུ་མ་ཡོད་པའི་ཕྱིར། ཆ་ཤས་ཀྱི༌[^337]དུ་མ་ཡང་མ་གྲུབ་སྟེ་ཕྱོགས་གཅིག་རང་ལ་ཡང་ཆ་དྲུག་ཡོད་པས་སོ། །

[Block 827]
ཕྱོགས་གཅིག་མེད་པས་ཆ་ཤས་ཀྱི་དུ་མ་མེད་དོ། །

[Block 828]
ཡང་ཁ་ཅིག་རྡུལ་ཕྲ་རབ་ཡོད་དོ་ཞེས་ཟེར་ན་ཡང་ཆ་ཤས་ཡོད་དམ་མེད་བརྟགས་ཏེ།[^338] ཡོད་ན་སྔ་མ་དང་འདྲའོ། །

[Block 829]
ཆ་ཤས་མེད་ན་ནི་ཆ་ཤས་མེད་པའི་ཕྱིར་དངོས་པོ་གཟུགས་མེད་དུ་ཐལ་ཏེ་སེམས་དང་སེམས་ལས་བྱུང་བ་བཞིན་ནོ། །

[Block 830 [VERSE]]
དེ་བཞིན་དུ་ལྟ་བ་པོའི་གང་ཟག་ཀྱང་མེད་དོ། །
དེ་བཞིན་དུ་སྒྲ་ལ་སོགས་པ་ལ་ཡང་སྦྱོར༌[^339]རོ། །
འགའ་ཞིག་སེམས་ཡང་དག་ཏུ་འདོད་དོ་ཞེ་ན།

[Block 831]
སེམས་མེད་སེམས་ལས་བྱུང་བ་མེད། །ཅེས་སྔ་མ་དང་འདྲ་བའི་རིགས་པ་མ་གྲུབ་པོ། །དེ་སྐད་དུ། གཟུགས་ཁམས་ཞེས་བྱ་སྟོང་པ་སྟེ། དེ་ཉིད་དུ་ནི་སྒྲ་ཡང་བྱ། །ཞེས་པ་ནས། དམིགས་ཞེས་བྱ་བ་སྟོང་པ་སྟེ།

[Block 832 [VERSE]]
དབུས་སུ་རྣམ་ཤེས་ཇི་ལྟར་འགྱུར། །
རྣ་བ་ཞེས་བྱ་སྟོང་པ་ཡིན། །
བར་ན་རྣམ་ཤེས་ཇི་ལྟར་མཆིས། །
ཞེས་པ་རྒྱ་ཆེར་གསུངས་སོ། །

[Block 833]
ཐུན་མོང་ཤེས་རབ་ཀྱི་ལྟེ་བ་དབུ་མ་དང་ཆ་མཐུན་པར་གཏན་ལ་འབེབས་པ། [^340]རང་རིག་སེམས་ཙམ་དང་ཆ་མཐུན་པར་སྟོན་ཏེ། ལེའུ་བརྒྱད་པར་འཆད་པར་འགྱུར་རོ། །

[Block 834 [HEADING]]
#### ལྟ་བ་ཐུན་མོང་མ་ཡིན་པ་ཐབས་གཙོར་བྱས་པ་བདེ་བ་ཆེན་པོ་ཤེས་པ། ^1-5-2-0

[Block 835]
ལྟ་བ་ཐུན་མོང་མ་ཡིན་པ་ཐབས་གཙོར་བྱས་པ་བདེ་བ་ཆེན་པོ་ཤེས་པ་སྟེ། སྐྱེད་བྱེད་མ་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་སྟོན་ཏོ། །

[Block 836]
སྐྱེད་བྱེད་མ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^341]ནི་བསྒོམ་པ་དང་སྤྱོད་པ་ཡིན་ནོ་ཞེ་ན། བདེན་ཏེ་འོན་ཀྱང་ཐུན་མོང་མ་ཡིན་པའི་སྐབས་སུ་ཐབས་གཙོར་བྱས་ཏེ། ལྟ་བ་ཤེས་རབ་བསྐྱེད་པ་ཡིན་པའི༌[^342]ཕྱིར་དང་ཡང་ན་བསྒོམ་པའི་ཐབས་ཡིན་ཡང་། ལྟ་བ་ཉམས་སུ་ལེན་པའི་ཐབས་གཙོར་བྱས་ཏེ། ཡིད་སོ་སོར་རྟོག་པའི་ཤེས་རབ་བསྐྱེད་པའི་ཕྱིར་སོམ་ཉི་མི་བྱའོ། །

[Block 837]
དེ་ཡང་གསུམ་སྟེ་གཞན་ལུས་ཤེས་རབ་སྟེ་འོག་སྒོ་ལ་བརྟེན་པ་དང་། རང་ལུས་ཐབས་ཏེ་སྟེང་སྒོ་ལ་བརྟེན་པ་དང་། དེ་ཁོ་ན་ཉིད་ཤེས་རབ་མི་དམིགས་པ་དང་སྦྱར་བའོ། །

[Block 838 [HEADING]]
##### གཞན་ལུས་ཤེས་རབ་སྟེ་འོག་སྒོ་ལ་བརྟེན་པ། ^1-5-2-1-0

[Block 839]
དེ་ལ་ཤེས་རབ་ལ་བརྟེན་པ་ཡང་གཉིས་ཏེ། ལས་དང་པོ་པ་དང་ལས་སྨིན་པའོ། །

[Block 840 [HEADING]]
###### ལས་དང་པོ་པ། ^1-5-2-1-1-0

[Block 841]
ལས་དང་པོ་པས་ནི་མ་ཞེས་པས་ནི་རང་གིས་དེ་ལ་དབང་ནོས་པའོ། །

[Block 842 [VERSE]]
སྲིང་མོ་ནི་དབང་ལྷན་ཅིག་ནོས་པའོ། །
བུ་མོ་ནི་རང་གིས་དབང་བསྐུར་བའོ། །

[Block 843]
རྟག་ཏུ་མཆོད༌[^343]ཅེས་པ་ནི་དབང་གི་དུས་སུ་ཇི་ལྟར༌[^344]རྒྱུན་མི་འཆད་པར་རོ། །

[Block 844]
རྣལ་འབྱོར་རིག་པ་ཞེས་པ་ནི་བླ་མའི་མན་ངག་བརྗོད་པའོ། །

[Block 845]
གར་མ་ནི་ཤེས་རབ་ཆེ་བའོ། །
--- END BLOCKS ---
