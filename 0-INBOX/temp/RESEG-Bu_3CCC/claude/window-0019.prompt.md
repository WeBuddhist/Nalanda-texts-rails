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
[Block 666]
ཐ་དད་པ་ཉིད་གཉི་ག་ལ་ཡོད་པར་ནི་འདོད་ལ་རག་གོ། །

[Block 667]
གལ་ཏེ་ཐ་དད་པ་ཉིད་གཉི་ག་ལ་ཡོད་པ་ལ་ལྷན་ཅིག་ཉིད་དུ་རྟོག་ན་དེ་ལྟར༌[^401]ན་འདོད་ཆགས་དང་ཆགས་པ་དག་ལ་ཅི་ཞིག་རབ་ཏུ་བསྒྲུབ་པ་ཡིན། གང་གི་ཚེ་དེ་ལྟར་ཡང་རྟོག་ན་དེ་གཉིས་ཐ་དད་པ་ཉིད་དུ་གྲུབ་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 668]
དེས་ན་ཐ་དད་པ་ཉིད་དུ་རབ་ཏུ་གྲུབ་པའི་ཕྱིར་དེ་གཉིས་ལྷན་ཅིག་ཉིད་དུ་རྟོག་པར་འགྱུར་རོ། །

[Block 669 [VERSE]]
གལ་ཏེ་འདོད་ཆགས་ཆགས་པ་དག །
ཐ་དད་ཉིད་དུ་གྲུབ་འགྱུར༌[^402]ན། །
དེ་གཉིས་ལྷན་ཅིག་ཉིད་དུ་ནི། །
ཅི་ཡི་ཕྱིར་ན་ཡོངས་སུ་རྟོག །

[Block 670]
ཉིད་དུ་ཞེས་བྱ་བའི་སྒྲ་ནི་ཁོ་ནར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 671]
གལ་ཏེ་འདི་སྙམ་དུ་འདོད་ཆགས་དང་ཆགས་པ་དག་ཐ་དད་པའི་དངོས་པོར་གྲུབ་པ་ཉིད་དུ་སེམས་ན། དེ་གཉིས་ལ་ལྷན་ཅིག་གི་དངོས་པོ་ཐ་དད་པའི་དངོས་པོ་དང་མི་མཐུན་པ་དེ་ནི་མེད་པར་ཅིའི་ཕྱིར་ཡོངས་སུ་རྟོག་པར་བྱེད་གང་གི་ཚེ་ཐ་དད་པའི་དངོས་པོར་གྲུབ་ན་ལྷན་ཅིག་གི་དངོས་པོར་བརྟགས་སུ་ཟིན་ཀྱང་། འདོད་ཆགས་དང་ཆགས་པ་དག་ལྡོག་པར་འགྱུར་བའམ། འཇུག་པར་འགྱུར་བ་ཅུང་ཟད་ཙམ་ཡང༌[^403]མེད་དོ། །

[Block 672]
འདི་ལྟར་ཆགས་པ་ལ་འདོད་ཆགས་ཀྱིས་ཡང་ཅི་ཞིག་བྱར་ཡོད་དེ། དེ་ལྟ༌[^404]བས་ན་ལྷན་ཅིག་གི་དངོས་པོར་བརྟགས་སུ་ཟིན་ཀྱང་ཐ་དད་པ་ཉིད་ཀྱི་སྐྱོན་ཆགས་པ་ཁོ་ནའི་ཕྱིར་ལྷན་ཅིག་གི་དངོས་པོར་བརྟག་པ༌[^405]དོན་མེད་པར་འགྱུར་ཏེ། ཚིག་ཟིན་པ་ལ་ཆུས་འདེབས་པ་བཞིན་ནོ། །

[Block 673 [VERSE]]
ཐ་དད་གྲུབ་པར་མ་གྱུར་པས། །
དེ་ཕྱིར་ལྷན་ཅིག་འདོད་བྱེད་དམ། །
ལྷན་ཅིག་རབ་ཏུ་བསྒྲུབ་པའི་ཕྱིར། །
ཐ་དད་ཉིད་དུ་ཡང་འདོད་དམ། །

[Block 674]
འདོད་ཆགས་དང་ཆགས་པ་དག་ཐ་དད་པ་ཉིད་དུ་ནི་དགོས་པ་མེད་པའི་ཕྱིར་གྲུབ་པར་མ་གྱུར་པས་དེ་རབ་ཏུ་བསྒྲུབ་པའི་ཕྱིར་ལྷན་ཅིག་ཉིད་དུ་འདོད་པར་བྱེད་ལ། ལྷན་ཅིག་ཉིད་དུ་ཡང་གཅིག་པ་ཉིད་ཀྱི་སྐྱོན་ཆགས་པའི་ཕྱིར་མ་གྲུབ་པས་དེ་རབ་ཏུ་བསྒྲུབ་པའི་ཕྱིར་ཡང་ཐ་དད་པ་ཉིད་དུ་ཡང་འདོད་པར་བྱེད་པ་ཁྱོད་ནི་གོས་ངན་པ་ལྷགས་པ༌[^406]ཆེན་པོས་ཉེན་པ་བསྐུམས་ནས་བསྐུམས་པ་ཡང་བརྣགས༌[^407]མི་བཟོད་པས་ཡང་སྐྱོང་བར༌[^408]བྱེད་པ་དང་འདྲ་བའོ།[^409] །

[Block 675 [VERSE]]
ཐ་དད་དངོས་པོ་མ་གྲུབ་པས། །
ལྷན་ཅིག་དངོས་པོ་འགྲུབ་མི་འགྱུར། །
ཐ་དད་དངོས་པོ་གང་ཞིག་ལ། །
ལྷན་ཅིག་དངོས་པོར་འདོད་པར་བྱེད། །

[Block 676]
འདི་ལ་སོ་སོ་ལ་ཐ་དད་པའི་དངོས་པོ་ཡོད་དམ་དེ་གཉིས་ལྷན་ཅིག་འབྱུང་བ་ལ་ཡོད་གྲང་ན། འདོད་ཆགས་དང་ཆགས་པ་ཐ་དད་དུ་གྱུར་པ་དག་ལ་ནི་འདི་ནི་འདོད་ཆགས་སོ། །

[Block 677]
འདི་ནི་འདིས་ཆགས་སོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་རྣམ་པ་ཐམས་ཅད་དུ་མི་སྲིད་དོ། །

[Block 678]
ཐ་དད་པའི་དངོས་པོར་རབ་ཏུ་གྲུབ་པ་མེད་ན་ལྷན་ཅིག་གི་དངོས་པོ་འགྲུབ་པར་མི་འགྱུར་རོ། །

[Block 679]
འདི་ལྟར་ཁྱོད་ནི་ཐ་དད་པའི་དངོས་པོ་ཡོད་ན་དེ་གཉིས་ཀྱི་ལྷན་ཅིག་གི་དངོས་པོ་ཡོད་པར་འདོད་ན། ཐ་དད་པའི་དངོས་པོ་དེ་ཡང་རྣམ་པ་ཐམས་ཅད་དུ་མི་འགྲུབ་པོ། །ཐ་དད་པའི་དངོས་པོ་མེད་ན་ཁྱོད་ཀྱི་ལྷན་ཅིག་གི་དངོས་པོ་ཡོད་པར་ག་ལ་འགྱུར། འོ་ན་ཐ་དད་པའི་དངོས་པོ་གང་ཞིག་ཡོད་ན་འདོད་ཆགས་དང་ཆགས་པ་དག་ལྷན་ཅིག་གི་དངོས་པོར་འདོད་པ་ཅི་རེ་རེ་ལ་ཡོད་དམ། འོན་ཏེ་གཉི་ག་ལྷན་ཅིག་བྱུང་བ་ལ་ཡོད་དམ་འོན་ཏེ་ཁྱོད་ཀྱིས་རང་དགར་ཐ་དད་པའི་དངོས་པོ་གཞན་ཞིག་བརྟགས་ཀྱང་རུང་སྟེ། ཐ་དད་པ་གང་ཡོད་ན་འདོད་ཆགས་དང་ཆགས་པ་དག་ལྷན་ཅིག་གི་དངོས་པོར་འདོད་པ་དེ་སྨྲོས་ཤིག །

[Block 680 [VERSE]]
དེ་ལྟར་འདོད་ཆགས་ཆགས་པ་དག །
ལྷན་ཅིག་ལྷན་ཅིག་མིན་མི་འགྲུབ། །
འདོད་ཆགས་བཞིན་དུ་ཆོས་རྣམས་ཀུན། །
ལྷན་ཅིག་ལྷན་ཅིག་མིན་མི་འགྲུབ། །

[Block 681 [VERSE]]
གལ་ཏེ་འདོད་ཆགས་སྔ་རོལ་ན། །
འདོད་ཆགས་མེད་པའི་ཆགས་ཡོད་ན། །
དེ་ལ་བརྟེན་ནས་འདོད་ཆགས་ཡོད། །
ཆགས་ཡོད་འདོད་ཆགས་ཡོད་པར་འགྱུར། །

[Block 682]
ཞེས་བྱ་བ་ལ་སོགས་པ་གང་དག་སྔར་འདས་པའི་རྣམ་པ་དེ་དག་གིས་དེ་ལྟར་འདོད་ཆགས་རྣམས་ཆགས་པ་དང་ལྷན་ཅིག་གམ་ཆགས་པ་མེད་པར་ཡང་འགྲུབ་པ་མེད་དོ། །

[Block 683]
ཇི་ལྟར་འདོད་ཆགས་ཆགས་པ་དང་ལྷན་ཅིག་གམ་ཆགས་པ་མེད་པ་ཡང་འགྲུབ་པ་མེད་པ་དེ་བཞིན་དུ་ཆོས་ཐམས་ཅད་ཀྱང་འགའ་ཞིག་དང་ལྷན་ཅིག་གམ་འགའ་ཡང་མེད་པར་ཡང་འགྲུབ་པ་མེད་དོ། །

[Block 684]
འདོད་ཆགས་དང་ཆགས་པ་བརྟག་པ་ཞེས་བྱ་སྟེ་རབ་ཏུ་བྱེད་པ་དྲུག་པའོ།། །།

[Block 685 [HEADING]]
## སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་བརྟག་པ། ^7-0

[Block 686]
འདིར་སྨྲས་པ། ཁྱོད་ཀྱིས་འདོད་ཆགས་དང་ཆགས་པ་བརྟག་པ་དེ་བྱས་པས་ཁོ་བོའི་ཡིད་སྟོང་པ་ཉིད་ཉན་པ་ལ་སྤྲོ་བར་བྱས་ཀྱི།[^410] དེའི་ཕྱིར་དེ་ནི༌[^411]འདུས་བྱས་ཀྱི་མཚན་ཉིད་བརྟག་པར་བྱ་བའི་རིགས་སོ། །

[Block 687]
བཤད་པ། དེ་ལྟར་བྱའོ། །

[Block 688]
འདིར་སྨྲས་པ། འདི་ལ་སྐྱེ་བ་དང་། གནས་པ་དང་འཇིག་པ༌[^412]དག་འདུས་བྱས་ཀྱི་སྤྱིའི་མཚན་ཉིད་དུ་བསྟན་ཏེ། མེད་པ་ལ་ནི་མཚན་ཉིད་བསྟན་པར་མི་རིགས་པས་མཚན་ཉིད་ཡོད་པའི་ཕྱིར་འདུས་བྱས་ཡོད་དོ། །

[Block 689]
བཤད་པ། འདུས་བྱས་ཀྱི་མཚན་ཉིད་མི་འཐད་པས་དེ་ཡོད་པའི་ཕྱིར་འདུས་བྱས་ཡོད་པར་ག་ལ་འགྱུར། གལ་ཏེ་ཇི་ལྟར་ཞེ་ན། སྔར།

[Block 690 [VERSE]]
མཚན་ཉིད་མེད་ལ་མཚན་ཉིད་ནི། །
མི་འཇུག་མཚན་ཉིད་བཅས་ལ་མིན། །

[Block 691]
ཞེས་བསྟན་པས་བཀག་ཟིན་པའི་ཕྱིར་རོ། །

[Block 692]
ཡང་གཞན་ཡང་།

[Block 693 [VERSE]]
གལ་ཏེ་སྐྱེ་བ་འདུས་བྱས་ན། །
དེ་ལ་མཚན་ཉིད་གསུམ་ལྡན་འགྱུར། །
ཅི་སྟེ་སྐྱེ་བ་འདུས་མ་བྱས། །
ཇི་ལྟར་འདུས་བྱས་མཚན་ཉིད་ཡིན། །

[Block 694]
ཞེས་བྱ་བ་འདི་ནི། གལ་ཏེ་སྐྱེ་བ་འདུས་བྱས་ན།[^413] །ཇི་ལྟར་འདུས་བྱས་མཚན་ཉིད་ཡིན། །ཞེས་ཕྱོགས་གོང་མ་དང་ཡང་སྦྱར་རོ། །

[Block 695]
སྐྱེ་བ་འདུས་བྱས་ཀྱི་མཚན་ཉིད་བསྟན་པ་གང་ཡིན་པ་དེ་ཡང་འདུས་བྱས་སམ་འདུས་མ་བྱས་ཤིག་ཏུ་བརྟག་གྲང་ན། དེ་ལ་རེ་ཞིག་འདུས་བྱས་སུ་ཡོངས་སུ་རྟོག་ན། སྐྱེ་བ་དེ་ཡང་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པའི་མཚན་ཉིད་ཀྱིས་མཚན་ཉིད་གསུམ་དང་ལྡན་པར་འགྱུར་ཏེ། འདུས་བྱས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 696]
མཚན་ཉིད་གསུམ་དང་ལྡན་པར་འགྱུར་བ་ནི། མཚན་ཉིད་གསུམ་པོ་དག་ཚོགས་པར་འགྱུར་བའོ། །

[Block 697]
སྨྲས་པ། དེ་ཡང་མཚན་ཉིད་གསུམ་དང་ལྡན་ནོ། །ཇི་ལྟར་འདུས་བྱས་མཚན་ཉིད་ཡིན། གལ་ཏེ་སྐྱེ་བ་ཡང་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པའི་མཚན་ཉིད་དང་ལྡན། གནས་པ་ཡང་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པའི་མཚན་ཉིད་དང་ལྡན། འཇིག་པ་ཡང་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པའི་མཚན་ཉིད་དང་ལྡན་ན་མཚན་ཉིད་མཚུངས་པའི་ཕྱིར་མཚན་ཉིད་རྣམས་ལ་ཁྱད་པར་ཡོད་པར་འགྱུར་རོ། །

[Block 698]
ཁྱད་པར་མེད་ན་འདི་ནི་སྐྱེ་བའོ། །

[Block 699]
འདི་ནི་གནས་པའོ། །

[Block 700]
འདི་ནི་འཇིག་པའོ། །ཞེས་བྱ་བ་དེ་དག་ཡོད་པར་ག་ལ་འགྱུར།

[Block 701]
སྨྲས་པ། དེ་ནི་ཉེས་པར་མི་འགྱུར་ཏེ། ཇི་ལྟར་སྤྱིར་འདུས་བྱས་ཀྱི་མཚན་ཉིད་ཡིན་དུ་ཟིན་ཀྱང་ཁྱད་པར་གྱི་མཚན་ཉིད་ལ་ལྟོས་ནས་འདི་ནི་བུམ་པའོ། །

[Block 702]
འདི་ནི་སྣམ་བུའོ། །ཞེས་བྱ་བ་དེ་དག་ཡོད་པ་དེ་བཞིན་དུ་འདིར་ཡང་ཁྱད་པར་གྱི་མཚན་ཉིད་ལ་ལྟོས་ནས་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དག་རབ་ཏུ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 703]
ཁྱད་པར་དེ་གང་ཞེ་ན། སྐྱེད་པར་བྱེད་པ་དང་། གནས་པར་བྱེད་པ་དང་། འཇིག་པར་བྱེད་པ་དག་གོ། །

[Block 704]
བཤད་པ། དེ་ནི་མི་འཐད་དོ།[^414] །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་བུམ་པ་སྐྱེད་པར་བྱེད་པ་དང་། མངོན་པར་འགྲུབ་པར་བྱེད་པ་གང་ཡིན་པ་དེས་ནི་གཞན་ཅི་ཡང་སྐྱེད་པར་མི་བྱེད་ལ། བུམ་པ་གནས་པར་བྱེད་པས་ཀྱང་གཞན་ཅི་ཡང་གནས་པར་མི་བྱེད་ཅིང་། བུམ་པ་འཇིག་པར་བྱེད་པས་ཀྱང་གཞན་ཅི་ཡང་འཇིག་པར་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 705]
སྨྲས་པ། དེ་དག་གིས༌[^415]བུམ་པ་ཉིད་སྐྱེ་བ་དང་གནས་པ་དང་། འཇིག་པར་བྱེད་པས་ཉེས་པ་མེད་དོ། །
--- END BLOCKS ---
