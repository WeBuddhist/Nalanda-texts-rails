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

[Block 601]
སྨྲས་པ། འདི་ལ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱིས༌[^367]ཆོས་བསྟན་པ་དག་ནི་ཕལ་ཆེར་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་དག་ལ་བརྟེན་པ་ཡིན་ན་དེ་ལ་གལ་ཏེ་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་དག་མེད་པ་ཉིད་ཡིན་པ་དེ་དག་དོན་མེད་པ་ཉིད་དུ་མི་འགྱུར་རམ་དེ་དག་དོན་མེད་པ་ཉིད་དུ་མི་རིགས་ན་དེ་ཅི་ལྟ་བུ་ཞིག །བཤད་པ། ཁོ་བོས་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་དག་མེད་པ་ཉིད་དུ་མི་སྨྲའི། དེ་དག་ཡོད་པ་ཉིད་དུ་སྨྲ་བ་སེལ་བར་བྱེད་དོ། །

[Block 602]
དེ་གཉི་ག་ཡང་སྐྱོན་དུ་ཆེ་སྟེ། འདི་ལྟར་འོག་ནས་ཀྱང་།

[Block 603 [VERSE]]
ཡོད་ཅེས་བྱ་བརྟག་པར་འཛིན། །
མེད་ཅེས་བྱ་བ་ཆད་པར་ལྟ། །
དེ་ཕྱིར་ཡོད་དང་མེད་པ་ལ། །
མཁས་པས་གནས་པར་མི་བྱའོ། །

[Block 604]
ཞེས་འབྱུང་ངོ་། །

[Block 605]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ཀ་ཏྱ་ན༌[^368]འཇིག་རྟེན་འདི་ནི་གཉིས་ལ་གནས་ཏེ། ཕལ་ཆེར་ཡོད་པ་ཉིད་དང་། མེད་པ་ཉིད་ལ་གནས་སོ་ཞེས་བཀའ་སྩལ་ཏོ། །

[Block 606]
དེའི་ཕྱིར་ཁོ་བོ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བས་ཡོད་པ་ཉིད་དང་མེད་པ་ཉིད་ཀྱི་སྐྱོན་དང་བྲལ་བ་ཆད་པ་མ་ཡིན༌[^369]རྟག་པ་མ་ཡིན་པ་རྗེས་སུ་རབ་ཏུ་སྟོན་པ༌[^370]མེད་པ་ཉིད་དུ་མི་སྨྲའོ། །

[Block 607]
དེ་ལྟ་བས་ན་ཁོ་བོ་ཅག་ལ་ཕུང་པོ་དང་། ཁམས་དང་སྐྱེ་མཆེད་དག་ལ་བརྟེན་པའི་ཆོས་སྟོན་པ་དག་དོན་མེད་པ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 608 [VERSE]]
བློ་ཆུང་གང་དག་དངོས་རྣམས་ལ། །
ཡོད་པ་ཉིད་དང་མེད་ཉིད་དུ། །
ལྟ་བ་དེ༌[^371]ནི་བལྟ༌[^372]བྱ་བ། །
ཉེ་བར་ཞི་བ་ཞི་མི་མཐོང་། །

[Block 609]
བློ་ཆུང་ངུ་གང་དག་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མཆོག་ཏུ་ཟབ་པ་མ་རྟོགས༌[^373]པ་ན་དངོས་པོ་རྣམས་ལ་ཡོད་པ་ཉིད་དང་། མེད་པ་ཉིད་དུ་རྗེས་སུ་ལྟ་བ་ཆད་པ་དང་རྟག་པར་ལྟ་བས་བློ་གྲོས་ཀྱི་མིག་བསྒྲིབས་པ༌[^374]དེ་དག་གིས་ནི་མྱ་ངན་ལས་འདས་པ་ལྟ་བར༌[^375]བྱ་བ་ཉེ་བར་ཞི་ཞིང་ཞི་བ་མི་མཐོང་ངོ་། །དེའི་ཕྱིར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་མ་མཐོང་བ་སྤྲོས་པ་ལ་མངོན་པར་དགའ་བའི་ཡིད་དང་ལྡན་པ་དེ་དག་གི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་དག་ལ་བརྟེན་པའི་ཆོས་སྟོན་པ་དག་ནི༌[^376]དོན་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 610]
དེ་ལྟ་བས་ན་འདི་ནི་དོན་དམ་པ་ཡིན་གྱིས་མ་འཇིགས་ཤིག །

[Block 611]
སྨྲས་པ། ཅིའི་ཕྱིར་ནམ་མཁའི་ཁམས་གང་ཡིན་པ་དེ་དང་པོར་བརྟགས། ཁམས་བསྟན་པ་ལ་དང་པོར་སའི་ཁམས་བསྟན་པས་སའི་ཁམས༌[^377]ཉིད་དང་པོ༌[^378]བརྟག་པར་བྱ་བའི་རིགས་སོ། །

[Block 612]
བཤད་པ། གྲགས་པའི་དོན་གྱིས་མ་གྲགས་པའི་དོན་རབ་ཏུ་བསྒྲུབ་པར་བྱ་སྟེ། འཇིག་རྟེན་ནི་ཕལ་ཆེར་ནམ་མཁའ་ལ་ཅི་ཡང་མ་ཡིན་པར་མོས་ཏེ། འདི་ལྟར་སྨྲ་བ་པོ་དག་ན་རེ་སྤྲོས་པ་དེ་དག་ཐམས་ཅད་ནི་ནམ་མཁའོ། །ཞེས་ཟེར་བས་དེ་དག་ཐམས་ཅད་ནི༌[^379]ཅི་ཡང་མ་ཡིན་ནོ། །ཞེས་བྱ་བར་བསམ་མོ།[^380] །དེའི་ཕྱིར་ཁམས་ལྷག་མ་ལྔ་པོ་དག་ཀྱང་ནམ་མཁའ་དང་མཚུངས་པར་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བའི་དཔེ་བསྟན་པའི་ཕྱིར་ནམ་མཁའ་སྟོང་པ་ཉིད་དུ་གྲུབ་པ་དང་པོར་བསྟན་ཏོ། །

[Block 613]
ཁམས་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་ལྔ་པའོ།། །།

[Block 614 [HEADING]]
## འདོད་ཆགས་དང་ཆགས་པ་བརྟག་པ། ^6-0

[Block 615]
འདིར༌[^381]སྨྲས་པ། ཁྱོད་ཀྱིས་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་དག་གི་སྟོང་པ་ཉིད་རྗེས་སུ་རབ་ཏུ་བསྟན་པས་ཁོ་བོ་སྟོང་པ་ཉིད་ཉན་འདོད་པར་གྱུར་གྱིས། དེའི་ཕྱིར་ད་ནི་འདོད་ཆགས་དང་ཆགས་པ་བརྟག་པར་བྱ་བའི་རིགས་སོ། །

[Block 616]
བཤད་པ་དེ་ལྟར་བྱའོ། །

[Block 617]
སྨྲས་པ། འདི་ལ་དེ་དང་དེར་འདོད་ཆགས་དང་ཆགས་པ་སྤངས་པ༌[^382]བསྟན། འདོད་ཆགས་ཉེ་བར་ཞི་བར་བྱ་བའི་ཕྱིར་རིགས་པ༌[^383]ཡང་བསྟན་ཏོ། །

[Block 618]
མེད་ན་ནི་ཉེ་བར་ཞི་བར་བྱ་བའི་རིགས་པ་ཡང༌[^384]བསྟན་པའི་མི་རིགས་ཏེ། འདི་ལྟར་སྦྲུལ་གྱིས་མ་ཟིན་ན་གསང་སྔགས་དང་སྨན་གྱི་བྱ་བ་མེད་དོ། །

[Block 619]
དེ་ལྟ་བས་ན་འདོད་ཆགས་དང་ཆགས་པ་དག་ནི་ཡོད་དོ། །

[Block 620]
བཤད་པ། འདོད་ཆགས་དང་ཆགས་པ་དག་ནི་མི་སྲིད་དོ། །ཇི་ལྟར་ཞེ་ན།

[Block 621 [VERSE]]
གལ་ཏེ་འདོད་ཆགས་སྔ་རོལ་ན། །
འདོད་ཆགས་མེད་པའི་ཆགས་ཡོད་ན། །
དེ་ལ་བརྟེན་ནས་འདོད་ཆགས་ཡོད། །
ཆགས་ཡོད་འདོད་ཆགས་ཡོད་པར་འགྱུར། །

[Block 622]
གལ་ཏེ་འདོད་ཆགས་ཀྱི་སྔ་རོལ་ན་ཆགས་པ་འདོད་ཆགས་མེད་པ་འདོད་ཆགས་ལས་གཞན་དུ་གྱུར་པ་འགའ་ཞིག་ཡོད་ན་ནི་དེ་ལ་བརྟེན་ནས་འདོད་ཆགས་ཡོད་པར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། ཆགས་ཡོད་འདོད་ཆགས་ཡོད་པར་འགྱུར། །འདི་ལྟར་ཆགས་པ་ཡོད་ན་འདོད་ཆགས་ཀྱང་འདིའོ་ཞེས་འཐད་པར་འགྱུར་རོ། །

[Block 623]
ཆགས་པ་མེད་ན་དེ་སུའི་འདོད་ཆགས་སུ་འགྱུར་ཏེ། འདི་ལྟར་གཞི་མེད་པ་ལ་འདོད་ཆགས་མི་འཐད་པས་དེའི་ཕྱིར་ཆགས་པ་མེད་ན་འདོད་ཆགས་མི་འཐད་དོ། །

[Block 624]
སྨྲས་པ། ཆགས་པ་ཡོད་ན་འདོད་ཆགས་ཡོད་དོ། །

[Block 625]
འདིར་བཤད་པ།

[Block 626 [VERSE]]
ཆགས་པ་ཡོད་པར་གྱུར་ན་ཡང་། །
འདོད་ཆགས་ཡོད་པར་ག་ལ་འགྱུར། །

[Block 627]
ཁྱོད་ཀྱི་ཆགས་པ་ཡོད་པར་གྱུར་ན་ཡང་། འདོད་ཆགས་ཡོད་པ་ཉིད་དུ་ག་ལ་འགྱུར་ཏེ། འདི་ལྟར་ཆགས་པ་ལ་འདོད་ཆགས་ཀྱི་བྱ་བ་ཅི་ཡང་མེད་དོ། །

[Block 628]
ཆགས་པར་མི་བྱེད་ན་ནི་ཇི་ལྟར་འདོད་ཆགས་ཡིན་པར་འགྱུར། ཅི་སྟེ་འགྱུར་ན་ནི་གང་ཡང་འདོད་ཆགས་མ་ཡིན་པ་ཉིད་དུ་མི་འགྱུར་བས་དེ་ནི་མི་འདོད་དེ། དེའི་ཕྱིར་ཆགས་པ་ཡོད་པར་གྱུར༌[^385]ན་ཡང་འདོད་ཆགས་མི་འཐད་དོ། །

[Block 629]
སྨྲས་པ། རེ་ཞིག་ཆགས་པ་ནི་ཡོད་དེ། དེ་ཡང་འདོད་ཆགས་མེད་ན་མི་འབྱུང་བས་འདོད་ཆགས་ཀྱང་རབ་ཏུ་གྲུབ་པ་ཉིད་དོ། །

[Block 630]
བཤད་པ།

[Block 631 [VERSE]]
ཆགས་པ་ལ་ཡང༌[^386]འདོད་ཆགས་ནི། །
ཡོད་དམ་མེད་ཀྱང་རིམ་པ་མཚུངས། །
ཆགས་པ་ཡོད་པར་ཡོངས་བརྟགས༌[^387]ན། །

[Block 632]
འདོད་ཆགས་ཡོད་དམ་མེད་ཀྱང་རུང་སྟེ་ཆགས་པ་ལ་ཡང་འདོད་ཆགས་མི་འཐད་པ་དེ་ཉིད་དང་རིམ་པ་མཚུངས་སོ། །ཇི་ལྟར་ཞེ་ན།

[Block 633 [VERSE]]
གལ་ཏེ་ཆགས་པའི་སྔ་རོལ་ན། །
ཆགས་མེད་འདོད་ཆགས་ཡོད་ན་ནི། །
དེ་ལ་བརྟེན་ནས་ཆགས་པ་ཡོད། །
འདོད་ཆགས་ཡོད་ན་ཆགས་ཡོད་འགྱུར། །

[Block 634]
གལ་ཏེ་ཆགས་པའི་སྔ་རོལ་ན་འདོད་ཆགས་ཆགས་པ་མེད་པ་ཆགས་པ་ལས་གཞན་དུ་འགྱུར་བ་འགའ་ཞིག་ཡོད་ན་ནི། དེ་ལ་བརྟེན་ནས་ཆགས་པ་ཡོད་པར་འགྱུར་རོ། །

[Block 635]
ཅིའི་ཕྱིར་ཞེ་ན། འདོད་ཆགས་ཡོད་ན་ཆགས་ཡོད་འགྱུར། །འདི་ལྟར་འདོད་ཆགས་ཡོད་ན་ཆགས་པ་ཡང་འདིས་འདི་ཆགས་སོ་ཞེས་འཐད་པར་འགྱུར་རོ། །
--- END BLOCKS ---
