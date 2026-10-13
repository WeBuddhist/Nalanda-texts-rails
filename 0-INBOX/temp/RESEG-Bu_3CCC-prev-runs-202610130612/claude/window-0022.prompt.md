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
[Block 771]
གཞན་དག་སྣང་བར་བྱེད་དོ་ཞེས་གང་སྨྲས་པ་དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། མར་མེ་གཞན༌[^453]བདག་ཉིད་དག་ལ་འཇུག་པ་དེ༌[^454]ཡང་མུན་པ་མེད་དེ། མུན་པ་མེད་པའི་ཕྱིར་དེ་དག་ལ་ཡང་མི་སྣང་བ་མེད་དོ། །

[Block 772]
འོ་ན་རང་དང་གཞན་གྱི་བདག་ཉིད་དག་ལ་མི་སྣང་བ་མེད་ན། མར་མེས་ཅི་ཞིག་སྣང་བར་བྱེད། དེ་སྨྲོས་ཤིག །

[Block 773]
སྨྲས་པ། མུན་པ་སེལ་བས་སྣང་བྱེད་ཡིན། འདི་ན་མར་མེ་སྐྱེ་བཞིན་པས་མུན་པ་སེལ་ཅིང་སྣང་བར་བྱེད་པས་སྣང་བར་བྱེད་པ་ཡིན་ཏེ། དེ་ལ་མུན་པ་སེལ་བར་བྱེད་པ་གང་ཡིན་པ་དེ་མར་མེ་རང་དང་གཞན་གྱི་བདག་ཉིད་དག་སྣང་བར་བྱེད་པ་ཡིན་ནོ་ཞེས་སྨྲས་པ༌[^455]དེའི་ཕྱིར།

[Block 774 [VERSE]]
མར་མེ་དང་ནི་གང་དག་ན། །
འདུ་བྱེད༌[^456]པ་ན་མུན་པ་མེད། །

[Block 775]
ཅེས་ཀྱང༌[^457]བཤད་པས་མར་མེ་སྐྱེ་བཞིན་པས་མུན་པ་སེལ་བའི་ཕྱིར་དེས་ན་མར་མེ་རང་དང་གཞན་གྱི་བདག་ཉིད་དག་ལ་མུན་པ་མེད་དོ།[^458] །མུན་པ་མེད་པའི་ཕྱིར་སྣང་བར་བྱེད་པ་ཉིད་ཡིན་ནོ། །

[Block 776]
དེ་ལྟར་མུན་པ་སེལ་བར་བྱེད་པའི་ཕྱིར་མར་མེས་ནི་རང་དང་གཞན་གྱི་བདག་ཉིད་དག་སྣང་བར་བྱེད་དོ། །

[Block 777]
མར་མེ་ཇི་ལྟ་བ་དེ་བཞིན་དུ་སྐྱེ་བས་ཀྱང་རང་དང་གཞན་གྱི་བདག་ཉིད་དེ༌[^459]དག་སྐྱེད་པར་བྱེད་དོ་ཞེས་བྱ་བ་དེ་རིགས་པ་ཡིན་ནོ། །

[Block 778]
བཤད་པ། མར་མེ་སྐྱེ་བཞིན་པས་མུན་པ་སེལ་བར་བྱེད་དོ། །ཞེས་ཟེར་བ་དེ༌[^460]སྨྲོས་ཤིག །

[Block 779 [VERSE]]
ཇི་ལྟར་མར་མེ་སྐྱེ་བཞིན་པས། །
མུན་པ་སེལ་བར་བྱེད་པ་ཡིན། །
གང་ཚེ་མར་མེ་སྐྱེ་བཞིན་པ། །
མུན་པ་དང་ནི་ཕྲད་པ་མེད། །

[Block 780]
གང་ཚེ་མར་མེ་དང་མུན་པ་དག་གཅིག་ནི༌[^461]མི་སྲིད་པའི་ཕྱིར་མར་མེ་སྐྱེ་བཞིན་པ་མུན་པ་དང་ཕྲད་པ་མེད་པ་དེའི་ཕྱིར༌[^462]ཇི་ལྟར་མར་མེ་སྐྱེ་བཞིན་པ་མུན་པ་དང་མ་ཕྲད་པ་དེས་མུན་པ་སེལ་བར་བྱེད།

[Block 781 [VERSE]]
མར་མེ་ཕྲད་པ་མེད་པར་ཡང་། །
གལ་ཏེ་མུན་པ་སེལ་བྱེད་ན། །
འཇིག་རྟེན་ཀུན་ན་གནས་པའི་མུན། །
འདི་ན་འདུག་པ་དེས་སེལ༌[^463]འགྱུར། །

[Block 782]
ཅི་སྟེ་མར་མེ༌[^464]ཕྲད་པ་ཉིད་དུ་ཡང་མུན་པ་སེལ་བར་བྱེད་ན་ནི་དེ་ལྟར་ན་འཇིག་རྟེན་ཀུན་ན་གནས་པའི་མུན་པ་དག་ཀྱང་མར་མེ་འདི་ན་འདུག་པ་དེས་བསལ་བར་འགྱུར་ཏེ། མ་ཕྲད་པ༌[^465]འདྲ་བ་ལས་ལ་ལ་ནི་སེལ་བར་བྱེད་ལ། ལ་ལ་ནི་སེལ་བར་མི་བྱེད་པ་དེ་ལ་ཁྱད་པར་ཅི་ཡོད།

[Block 783]
ཡང་གཞན་ཡང་།

[Block 784 [VERSE]]
མར་མེ་རང་དང་གཞན་གྱི་དངོས། །
གལ་ཏེ་སྣང་བར་བྱེད་གྱུར་ན། །
མུན་པའང་རང་དང་གཞན་གྱི་དངོས། །
སྒྲིབ་པར་འགྱུར་བར་ཐེ་ཚོམ་མེད། །

[Block 785]
འདི་ན་མར་མེ་ནི་མུན་པའི་གཉེན་པོར་གནས་པ་ཡིན་པས་དེས་ན་གལ་ཏེ་མར་མེས་རང་དང་གཞན་གྱི་དངོས་པོ་དག་སྣང་བར་བྱེད་པར་གྱུར་ན། མུན་པས་ཀྱང་རང་དང་གཞན་གྱི་དངོས་པོ་དག་སྒྲིབ་པར་ཐལ་བར་འགྱུར་བ་འདི་ལ་ཐེ་ཚོམ་མེད་པ་ཞིག་ན་མུན་པས་ནི་རང་དང་གཞན་གྱི་དངོས་པོ་དག་སྒྲིབ་པར་མི་བྱེད་དོ། །

[Block 786]
གལ་ཏེ་སྒྲིབ་པར་བྱེད་ན་ནི་གཞན་བཞིན་དུ་མུན་པ་ཉིད་ཀྱང་མི་དམིགས་པར་འགྱུར་རོ། །

[Block 787]
མུན་པ་མི་དམིགས་ན་ནི་དངོས་པོ་རྣམས་རྟག་ཏུ་སྣང་བར་འགྱུར་བ་ཞིག་ན། དངོས་པོ་རྣམས་རྟག་ཏུ་མི་སྣང་བས་དེའི་ཕྱིར་མུན་པས་ནི་རང་དང་གཞན་གྱི་དངོས་པོ་དག་སྒྲིབ་པར་མི་བྱེད་དོ། །

[Block 788]
དེ་ལྟ་ཡིན་ན་མུན་པའི་གཉེན་པོར་མར་མེས་ཀྱང་རང་དང་གཞན་གྱི་དངོས་པོ་དག་སྣང་བར་མི་བྱེད་པས་དེ་ལ་མར་མེ་བཞིན་དུ་སྐྱེ་བས་ཀྱང་རང་དང་གཞན་གྱི་བདག་ཉིད་དག་ཀྱང༌[^466]སྐྱེད་པར་བྱེད་དོ། །ཞེས་གང་སྨྲས་པ་དེ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 789]
ཡང་གཞན་ཡང་། གལ་ཏེ་སྐྱེ་བས་རང་གི་བདག་ཉིད་སྐྱེད་པར་བྱེད་ན་སྐྱེས་པས་སམ། མ་སྐྱེས་པ་ཞིག་གིས་སྐྱེད་པར་སྐྱེད༌[^467]གྲང་ན། གཉི་གས་ཀྱང་མི་འཐད་དོ། །ཇི་ལྟར་ཞེ་ན། སྐྱེ་བ་འདི་ནི་མ་སྐྱེས་པས། །རང་གི་བདག་ཉིད་ཇི་ལྟར་སྐྱེད།[^468] །སྐྱེ་བ་འདི་མ་སྐྱེས་ཤིང་མེད་པས་རང་གི་བདག་ཉིད་ཇི་ལྟར་སྐྱེད་པར་བྱེད། ཡང་ན་འདི་མ་སྐྱེས་ཤིང་མེད་པའི་བདག་ཉིད་སུ་ཞིག་གིས་སྐྱེད་པར་བྱེད། ཅི་སྟེ་མེད་པས་ཀྱང་བདག་ཉིད་མེད་པ་སྐྱེས༌[^469]ན་ནི་རི་བོང་གི་རྭས་ཀྱང་བདག་ཉིད་སྐྱེད་པར་བྱེད་པ་ཞིག་ན་སྐྱེད་པར་མི་བྱེད་དོ། །

[Block 790]
དེ་ལྟ་བས་ན་སྐྱེ་བ་མ་སྐྱེས་པས་བདག་ཉིད་སྐྱེད་པར་མི་བྱེད་དོ། །

[Block 791]
དེ་ལ་འདི་སྙམ་དུ་སྐྱེ་བ་སྐྱེས་པས་བདག་ཉིད་སྐྱེད་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 792 [VERSE]]
ཅི་སྟེ་སྐྱེས་པས་སྐྱེད་བྱེད་ན། །
སྐྱེས་ན་ཅི་ཞིག་བསྐྱེད་དུ་ཡོད། །

[Block 793]
གལ་ཏེ་སྐྱེ་བ་སྐྱེས་པ་ཉིད་ཡིན་ན་སྐྱེ་བ་སྐྱེས་པས་བདག་ཉིད་སྐྱེད་པར་བྱེད་དོ། །ཞེས་བྱ་བ་འཐད་པའི༌[^470]དོན་མེད་པ་འདི་ཅིའི་ཕྱིར་བྱེད་དེ། སྐྱེས་ཟིན་པ་ལ་ཡང་སྐྱེ་བས་ཅི་བྱ། དེ་ལྟར་ན་རེ་ཞིག་སྐྱེས་པས༌[^471]བདག་ཉིད་སྐྱེད་པར་མི་བྱེད་དོ། །

[Block 794]
སྐྱེ་བས་གཞན་སྐྱེད་པར་བྱེད་དོ། །ཞེས་གང་སྨྲས་པ་དེ་ཡང་མི་འཐད་དེ། འདི་ལྟར་གལ་ཏེ་སྐྱེ་བས་གཞན་སྐྱེད་པར་བྱེད་ན་སྐྱེ་བས་བསྐྱེད་པར་བྱ་བ་གཞན་དེ་སྐྱེས་པའམ་མ་སྐྱེས་པའམ། སྐྱེ་བཞིན་པ་ཞིག་སྐྱེད་པར་བྱེད་གྲང་ན། དེ་ལ།

[Block 795 [VERSE]]
སྐྱེས་དང་མ་སྐྱེས་སྐྱེ་བཞིན་པ། །
ཇི་ལྟ་བུར་ཡང་སྐྱེད་མི་བྱེད། །

[Block 796]
སྐྱེ་བ་ནི་ཇི་ལྟར་ཡང་སྐྱེད་པར་མི་འཐད་དོ། །

[Block 797]
མ་སྐྱེས་པ་ཡང་སྐྱེད་པར་མི་བྱེད་ལ། སྐྱེ་བཞིན་པ་ཡང་སྐྱེད་པར་མི་བྱེད་དོ། །

[Block 798]
ཇི་ལྟར་ཞེ་ན། བཤད་པ།

[Block 799 [VERSE]]
སོང་དང་མ་སོང་བགོམ་པ་ཡིས། །
དེ་དག་རྣམ་པར་བཤད་པ་ཡིན། །

[Block 800]
ཇི་ལྟར་སོང་བ་ལ་འགྲོ་བ་མེད་དེ། འགྲོ་བའི་བྱ་བ་འདས་ཟིན་པའི་ཕྱིར་རོ། །ཞེས་བྱ་བ་དེ་བཞིན་དུ་སྐྱེས་པ་ཡང་སྐྱེད་པར་མི་བྱེད་དེ་སྐྱེ་བའི་བྱ་བ་འདས་ཟིན་པའི་ཕྱིར་རོ། །

[Block 801]
སྐྱེས་པ་ལ་ཡང་སྐྱེ་བའི་བྱ་བ་མེད་དེ། ཅི་སྟེ་ཡང་སྐྱེས་པར༌[^472]འགྱུར་ན་ནི་ནམ་ཡང་མི་སྐྱེད་པར་མི་འགྱུར་བས་དེ༌[^473]ནི་མི་འདོད་དེ། དེའི་ཕྱིར་སྐྱེས་པ་སྐྱེད་པར་མི་བྱེད་དོ། །

[Block 802]
མ་སྐྱེས་པ་ཡང་སྐྱེད་པར་མི་བྱེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། མེད་པའི་ཕྱིར་རོ། །

[Block 803]
མ་སྐྱེས་པ་ལ་གང་སྐྱེད་པར༌[^474]འགྱུར་བ་ཅི་ཞིག་ཡོད། ཅི་སྟེ་མེད་ཀྱང་སྐྱེད་པར༌[^475]འགྱུར་ན་ནི་རི་བོང་གི་རྭ་ཡང་སྐྱེད་པར༌[^476]འགྱུར་བ་ཞིག་ན་སྐྱེད་པར༌[^477]མི་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་སྐྱེས་པ་ཡང་སྐྱེད་པར་མི་བྱེད་དོ། །

[Block 804]
དེ་ནི་སྐྱེ་བཞིན་པ་ཡང་སྐྱེད་པར་མི་བྱེད་དེ། སྐྱེས་པ་དང་མ་སྐྱེས་པ་མ་གཏོགས་པར་སྐྱེ་བཞིན་པ་མེད་པའི་ཕྱིར་དང་། སྐྱེ་བ་གཉིས་སུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་ཏེ། གང་དང་ལྡན་པས་སྐྱེ་བཞིན་པ་ཞེས་བྱ་བར་འགྱུར་བ་དང་། གང་དང་ལྡན་པས་སྐྱེད་པར་བྱེད་དོ། །ཞེས་བརྗོད་པར། [^478]ཡང་གཞན་ཡང་། འདི་ལ་སྐྱེ་བཞིན་པ་ཞེས་བྱ་བ་ནི་གང་གི་ཅུང་ཟད་ནི་སྐྱེས་ཅུང་ཟད་ནི་མ་སྐྱེས་པའམ། ཡང་ན་དེ་ལས་གཞན་པ་སྐྱེས་པའམ། མ་སྐྱེས་པ་ཞིག་ཡིན་གྲང༌[^479]ན། དེ་ལ་གལ་ཏེ་སྐྱེས་པ་དང་མ་སྐྱེས་པ་དེ་སྐྱེ་བས་སྐྱེད་པར་བྱེད་ན་རེ་ཞིག་དེའི་གང་ཅུང་ཟད་སྐྱེད་པ་དེ་ནི་སྐྱེ་བ་དེས་བསྐྱེད་པ་མ་ཡིན་ལ། སྐྱེས་པ་དེ་སྐྱེ་བཞིན་པ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་སྐྱེས་ན་སྐྱེ་བཞིན་པ་མ་ཡིན་ཞིང་སྐྱེ་བཞིན་པ་སྐྱེད་པར་བྱེད་དོ། །ཞེས་ཀྱང་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 805]
གལ་ཏེ་ཅུང་ཟད་སྐྱེས་པ་དེ་སྐྱེ་བ་མེད་པ་ཁོ་ནར་སྐྱེས་ན་ནི། དེའི་ལྷག་མ་ཡང་དེ་བཞིན་དུ་སྐྱེ་བ་མེད་པ་ཁོ་ནར་སྐྱེ་བར་འགྱུར་བར་ངེས་སོ། །

[Block 806]
ཡང་ན་དེའི་གང་ཅུང་ཟད་ནི་སྐྱེ་བ་མེད་པ་ཁོ་ནར་སྐྱེས་ལ་ཅུང་ཟད་ནི་སྐྱེ་བས་སྐྱེད་པར་བྱེད་པ་ལ་ཁྱད་པར་ཅི་ཡོད་པ་བརྗོད་དགོས་སོ། །

[Block 807]
ཅི་སྟེ་དེའི་གང་ཅུང་ཟད་སྐྱེས་པ་དེ་ཡང་སྐྱེ་བ་ཁོ་ནས་བསྐྱེད་ན་ནི་དེ་ལྟ་ན་མ་སྐྱེས་པ་སྐྱེ་བས་སྐྱེད་པར༌[^480]བྱེད་ཀྱི། སྐྱེ་བཞིན་པ་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 808]
ཡང་གཞན་ཡང་། དེའི་གང་ཅུང་ཟད་སྐྱེས་པ་དེ་ནི་སྐྱེ་བས་སྐྱེད་པར་མི་བྱེད་དེ། སྐྱེས་ཟིན་པའི་ཕྱིར་རོ། །

[Block 809]
དེས་ན་དེའི་ལྷག་མ་མ་སྐྱེས་པ་གང་ཞིག་ཡིན་པ་དེ་སྐྱེ་བས་སྐྱེད་པར་བྱེད་དོ། །ཞེས་བྱ་བར་འགྱུར་ཏེ། དེ་ལ་སྐྱེ་བཞིན་པ་སྐྱེད་པར་བྱེད་དོ་ཞེས་གང༌[^481]སྨྲས་པ་དེ་ཉམས་པར་གྱུར་ཏོ། །

[Block 810]
ཅི་སྟེ་དེའི༌[^482]ཅུང་ཟད་སྐྱེས་པ་དེ་ཡང༌[^483]སྐྱེད་པར་བྱེད་ན་ནི་དེ་ལ་སྐྱེ་བ་གཉིས་ཀྱིས་བྱས་པའི་ཁྱད་པར་ཅན་དུ་འགྱུར་བ་ཞིག་ན་མི་འགྱུར་ཏེ། སྐྱེས་ཟིན་པ་དེ་ལ་ནི་ཡང་སྐྱེད་པའི༌[^484]ཕྱིར་བྱ་བ་འགའ་ཡང་རྩོམ་པར་མི་བྱེད་པས་དེའི་ཕྱིར་དེ་ནི་ཡང་སྐྱེད་པར་མི་བྱེད་དོ། །
--- END BLOCKS ---
