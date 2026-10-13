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
[Block 526]
དེ་ལྟར་ཡང་།

[Block 527 [VERSE]]
གཟུགས་ནི་དབུ་བ་རྡོས་པ་འདྲ། །
ཚོར་བ་ཆུ་བུར་དག་དང་མཚུངས། །
འདུ་ཤེས་སྨིག་རྒྱུ་འདྲ་བ་སྟེ། །
འདུ་བྱེད་རྣམས་ནི་ཆུ་ཤིང་བཞིན། །

[Block 528]
རྣམ་ཤེས་སྒྱུ་མ་ལྟ་བུ་ཞེས། །ཉི་མའི་གཉེན་གྱིས་བཀའ་སྩལ་ཏོ། །ཞེས་ཀྱང་གསུངས་སོ། །

[Block 529]
ཕུང་པོ་རྣམས་ཉི་ཚེ་གཟུགས་མི་འཐད་པ་ཉིད་ཀྱིས་མི་འཐད༌[^334]པར་རིམ་པ་མཚུངས་པར་མ་ཟད་ཀྱི། ཆོས་ཐམས་ཅད་ཀྱང་གཟུགས་མི་འཐད་པ་ཉིད་ཀྱིས་མི་འཐད་པར་རིམ་པ་མཚུངས་སོ། །

[Block 530]
དེ་ལྟར་གང་གི་ཕྱིར་ཆོས་ཐམས་ཅད་གཟུགས་མི་འཐད་པ་ཉིད་ཀྱིས་མི་འཐད་པར་རིམ་པ་མཚུངས་པ་དེའི་ཕྱིར།

[Block 531 [VERSE]]
སྟོང་པ་ཉིད་ཀྱིས་བརྩད་བྱས་ཚེ། །
གང་ཞིག་ལན་འདེབས་སྨྲ་བྱེད་པ། །
དེ་ཡིས༌[^335]ཐམས་ཅད་ལན་བཏབ་མིན། །
བསྒྲུབ་པར་བྱ་དང་མཚུངས་པར་འགྱུར། །

[Block 532]
སྟོང་པ་ཉིད་ཀྱིས་བརྩད༌[^336]ཅིང་འགྱེད་པ་བརྩམས་ཏེ་ཡོངས་སུ་གླེང་བའི་ཚེ་གང་ཞིག་སྟོང་པ་ཉིད་མ་ཡིན་པས་ལན་འདེབས་ཤིང་སྨྲ་བར་བྱེད་པ་དེའི་ཚེ༌[^337]དེ་དག་ཐམས་ཅད་ནི་ལན་བཏབ་པ་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། བསྒྲུབ་པར་བྱ་བ་དང་མཚུངས་པར་འགྱུར་བའི་ཕྱིར་དང་།[^338] འདི་ལྟ་སྟེ་དཔེར་ན་དངོས་པོ་ཐམས་ཅད་ངོ་བོ་ཉིད་སྟོང་པའོ། །ཞེས་དམ་བཅས་ན༌[^339]དཔེ་བསྟན་པའི་ཕྱིར་སྣམ་བུ་ངོ་བོ་ཉིད་སྟོང་པར་སྒྲུབ་པར་བྱེད་པའི་ཚེ་གང་ཞིག་རེ་ཞིག་རྒྱུ་སྤུན་དག་ནི་ཡོད་དོ་ཞེས་ཟེར་བའི་དེ་ནི་བསྒྲུབ་པར་བྱ་བ་དང་མཚུངས་པ་ཡིན་ཏེ། གཏན་ཚིགས་གང་དག་ཉིད་ཀྱིས་སྣམ་བུ་ངོ་བོ་ཉིད་སྟོང་པར་བསྟན་པ་དེ་དག་ཉིད་རྒྱུ་སྤུན་དག་སྟོང་པ་ཉིད་དུ་རབ་ཏུ་སྒྲུབ་པར༌[^340]བྱེད་པ་ཡང་ཡིན་པས་དེའི་ཕྱིར་རྒྱུ་སྤུན་དག་སྟོང་པ་ཉིད་མ་ཡིན་པར་སྟོན་པ་ནི་བསྒྲུབ་པར་བྱ་བ་སྣམ་བུ་དང་མཚུངས་པ་ཡིན་ནོ། །

[Block 533]
དེ་བཞིན་དུ་སྐྱེ་བོ་ཆོས་ཀྱི་གནས་སྐབས་ཤེས་པ་དག་དགེ་བའི་ཆོས་རྣམས་ཀྱི༌[^341]ངོ་བོ་ཉིད་ནི་དགེ་བའོ་སྙམ་པ་དང་། ལྷག་མ་རྣམས་ཀྱང་དེ་བཞིན་དུ་རྣམ་པར་ངེས་སོ་སྙམ་དུ་སེམས་ཤིང་དེ་དག་ལ་སོགས་པ་སྨྲ་ན་དགེ་བའི་ཆོས་རྣམས་ཀྱང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡིན་པའི་ཕྱིར་ངོ་བོ་ཉིད་མེད་པས་ན་དེ་ཡང་བསྒྲུབ་པར་བྱ་བ་དང་མཚུངས་པ་ཡིན་ཏེ། བསྒྲུབ་པར་བྱ་བ་དང་མཚུངས་པའི་ཕྱིར་ལན་བཏབ་པ་མ་ཡིན་ནོ། །

[Block 534]
སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།

[Block 535 [VERSE]]
དངོས་པོ་གཅིག་ལ་གང་ལྟ་བ། །
དེ་ནི་ཀུན་ལའང་ལྟ་བར་འདོད། །
གཅིག་གི་སྟོང་ཉིད་གང་ཡིན་པ། །
དེ་ཉིད་ཀུན་གྱི་སྟོང་པ་ཉིད། །

[Block 536]
ཅེས་གསུངས་སོ། །

[Block 537 [VERSE]]
སྟོང་པ་ཉིད་ཀྱིས་བཤད་བྱས་ཚེ། །
གང་ཞིག་སྐྱོན་འདོགས་སྨྲ་བྱེད་པ། །
དེ་ཡིས༌[^342]ཐམས་ཅད་སྐྱོན་བཏགས་མིན། །
བསྒྲུབ་པར་བྱ་དང་མཚུངས་པར་འགྱུར། །

[Block 538]
སྟོང་པ་ཉིད་ཀྱི༌[^343]དངོས་པོ་ངོ་བོ་ཉིད་མེད་པ་ཉིད་དུ་རྣམ་པར་བཤད་པའི་ཚེ་གང་ཞིག་སྟོང་པ་ཉིད་མ་ཡིན་པས་སྐྱོན་འདོགས་ཤིང་སྨྲ་བར་བྱེད་པ་དེའི་དེ་དག་ཐམས་ཅད་ཀྱང་སྔ་མ་ཁོ་ན་བཞིན་དུ་བསྒྲུབ་པར་བྱ་བ་དང་མཚུངས་པའི་ཕྱིར་སྐྱོན་བཏགས་པ་མ་ཡིན་ཏེ། དེ་ནི་དོན་གཅིག་པ་ཁོ་ན་ཡིན་མོད་ཀྱི། གནས་སྐབས་གཞན་གྱི་བྱེ་བྲག་གིས་ཡང་བསྟན་ཏོ། །

[Block 539]
ཚིགས་སུ་བཅད་པ་འདི་གཉིས་ནི་རབ་ཏུ་བྱེད་པ་ཐམས་ཅད་ཀྱི་ཁོངས་སུ་གཏོགས་པར་བལྟ་བར༌[^344]བྱ་སྟེ། ཐམས་ཅད་དུ༌[^345]གྲུབ་པའི་ཕྱིར་རོ། །

[Block 540]
ཕུང་པོ་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་བཞི་པའོ།། །།

[Block 541 [HEADING]]
## ཁམས་བརྟག་པ། ^5-0

[Block 542]
འདིར༌[^346]སྨྲས་པ། འདི༌[^347]ལ་སོགས་པ་ཁམས་དྲུག་པོ་དག་ཀྱང་བསྟན། དེ་དག་གི་སོ་སོའི་མཚན་ཉིད་ཀྱང་བསྟན་ཏོ། །

[Block 543]
དེ་ལ་ནམ་མཁའི་མཚན་ཉིད་ནི་མི་སྒྲིབ་པའོ། །ཞེས་བསྟན་ཏེ། དངོས་པོ་མེད་ན་ནི་མཚན་ཉིད་བསྟན་པར་མི་རིགས་པས་དེ་ལྟ་བས་ན་མཚན་ཉིད་ཡོད་པའི་ཕྱིར་ནམ་མཁའ་ཡོད་དོ། །

[Block 544]
ཇི་ལྟར་ནམ་མཁའ་ཡོད་པ་དེ་བཞིན་དུ་ཁམས་ལྷག་མ་རྣམས་ཀྱང་རང་གི་མཚན་ཉིད་ཡོད་པའི་ཕྱིར་ཡོད་དོ། །

[Block 545]
བཤད་པ། ནམ་མཁའི་མཚན་ཉིད་ནི་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 546 [VERSE]]
ནམ་མཁའི་མཚན་ཉིད་སྔ་རོལ་ན། །
ནམ་མཁའ་ཅུང་ཟད་ཡོད་མ་ཡིན། །

[Block 547]
གལ་ཏེ་ནམ་མཁའི་མཚན་ཉིད་ཀྱི་སྔ་རོལ་ན་ནམ་མཁའ༌[^348]ཞེས་བྱ་བ་ཅུང་ཟད་ཅིག་ཡོད་ན་ནི་དེ་ལ་ནམ་མཁའ་འདིའི་མཚན་ཉིད་ནི་འདི་ཡིན་ནོ་ཞེ་ས་མཚན་ཉིད་བསྟན་པ་ཡང་རིགས་པ་ཞིག་ན༌[^349]ནམ་མཁའི་མཚན་ཉིད་ཀྱི་སྔ་རོལ་ན་ནམ་མཁའ་མེད་དོ། །

[Block 548]
ནམ་མཁའ་མེད་ན་ནམ་མཁའི་མཚན་ཉིད་ཅེས་བྱ་བ་དེ་ཇི་ལྟར་འཐད་པར་འགྱུར། ཅི་སྟེ་ནམ་མཁའི་མཚན་ཉིད་ཀྱི་སྔ་རོལ་ན་ནམ་མཁའ་ཡོད་དོ་ཞེས་དེ་ལྟར་རྟོག་ན། དེ་ལྟ་ན། གལ་ཏེ་མཚན་ལས་སྔ་གྱུར་ན། མཚན་ཉིད་མེད་པར་ཐལ་བར་འགྱུར། འདིར་སྨྲས་པ། མཚན་ཉིད་མེད་པ་ཡོད་དོ། །

[Block 549]
ཞེས༌[^350]བཤད་པ།

[Block 550 [VERSE]]
མཚན་ཉིད་མེད་པའི་དངོས་པོ་ནི། །
འགའ་ཡང་གང་ན་ཡོད་མ་ཡིན། །

[Block 551]
ཡང་ཞེས་བྱ་བའི་སྒྲ་ནི་ཉིད་ཅེས་བྱ་བའི་དོན་ཏེ། མཚན་ཉིད་མེད་པའི་དངོས་པོ་ནི་འགའ་ཡང་ཡོད་པ་མ་ཡིན་པ་ཉིད་དེ། གཞུང་ལུགས་གང་དུ་ཡང་མ་བསྟན་ཏོ། །

[Block 552]
འོ་ན་ད།

[Block 553 [VERSE]]
མཚན་ཉིད་མེད་པའི་དངོས་མེད་ན། །
མཚན་ཉིད་གང་དུ་འཇུག་པར་འགྱུར། །

[Block 554]
དེ་བསྟན་པར་རིགས་སོ། །

[Block 555]
འདི་ལྟར། མཚན་ཉིད་མེད་ལ་མཚན་ཉིད་ནི། །མི་འཇུག་དེ་ལྟར་གང་གི་ཕྱིར་མཚན་ཉིད་མེད་པའི་དངོས་པོ་འགའ་ཡང་ཡོད་པ་མ་ཡིན་པ་དེའི་ཕྱིར་མཚན་ཉིད་མེད་པའི་དངོས་པོ་མེད་ན་དེ་གཞི་མེད་པ་ལ་མཚན་ཉིད་འཇུག་པར་མི་འཐད་དོ། །

[Block 556]
འོ་ན་མཚན་ཉིད་དང་བཅས་པའི་དངོས་པོ་ལ་མཚན་ཉིད་འཇུག་པར་འགྱུར་རོ་སྙམ་ན། བཤད་པ། མཚན་ཉིད་བཅས་ལ་མིན། མཚན་ཉིད་དང་བཅས་པའི་དངོས་པོ་ལ་ཡང་མཚན་ཉིད་འཇུག་པར་མི་འཐད་དེ། དགོས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 557]
དངོས་པོ་རང་གི་མཚན་ཉིད་དང་བཅས་པར༌[^351]རབ་ཏུ་གྲུབ་པ་ལ་ཡང་མཚན་ཉིད་ཀྱིས་ཅི་ཞིག་བྱ། དེ་ལྟ་ན་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་ཏེ། དེ་ནམ་ཡང་མཚན་ཉིད་དང་བཅས་པ་མ་ཡིན་པར་མི་འགྱུར་ཞིང་། རྟག་ཏུ་མཚན་ཉིད་འཇུག་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 558]
དེ་ཡང་མི་འདོད་དེ། དེ་ལྟ་བས་ན་མཚན་ཉིད་དང་བཅས་པའི་དངོས་པོ་ལ་ཡང་མཚན་ཉིད་འཇུག་པར་མི་འཐད་དོ། །

[Block 559]
དེ་ལ་འདི་སྙམ་དུ་མཚན་ཉིད་དང་བཅས་པ་དང་མཚན་ཉིད་མེད་པ་དག་ལས་གཞན་པ་ལ་འཇུག་པར་སེམས་ན། བཤད་པ།

[Block 560 [VERSE]]
མཚན་བཅས་མཚན་ཉིད་མེད་པ་ལས། །
གཞན་ལའང་འཇུག་པར་མི་འགྱུར་རོ། །

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
--- END BLOCKS ---
