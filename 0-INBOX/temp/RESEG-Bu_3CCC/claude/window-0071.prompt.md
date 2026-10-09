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
[Block 2486]
སྡུག་པ་དང་མི་སྡུག་པའི་ཕྱིན་ཅི་ལོག་དག་ངོ་བོ་ཉིད་ལས་ཡོད་པ་མ་ཡིན་པ་དེའི་ཚེ། སྡུག་པ་དང་མི་སྡུག་པའི་ཕྱིན་ཅི་ལོག་དག་ནི་ཡང་དག་པ་མ་ཡིན་ནོ། །

[Block 2487]
གང་ཡང་དག་པ་མ་ཡིན་པ་དེ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། སྡུག་པ་དང་མི་སྡུག་པའི་ཕྱིན་ཅི་ལོག་དེ་དག་ཡོད་པ་མ༌[^1621]ཡིན་ན་དེ་དག་ལ་བརྟེན་ནས་འབྱུང་བའི་ཉོན་མོངས་པ་དེ་དག་མ་ཡིན་ཏེ། དེ་དག་གི་རྒྱུ་ཅན་ཉོན་མོངས་པ་རྣམས་ཇི་ལྟར་ཡོད་པར་འགྱུར།

[Block 2488]
སྨྲས་པ།

[Block 2489 [VERSE]]
གཟུགས་སྒྲ་རོ་དང་རེག་བྱ་དང་། །
དྲི་དང་ཆོས་དག་རྣམ་དྲུག་ནི། །
གཞི་སྟེ་འདོད་ཆགས་ཞེ་སྡང་དང་། །

[Block 2490]
གཏི་མུག་གི༌[^1622]ནི་ཡིན་པར༌[^1623]བརྟགས།[^1624] །གཟུགས་དང་སྒྲ་དང་རོ་དང་རེག་པ་དང་དྲི་དང་ཆོས་དག་རྣམ་པ་དྲུག་ནི་འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་གི་གཞི་ཡིན་པར་རྣམ་པར་བརྟགས་ཏེ།[^1625] གཞི་དེ་དག་ཡོད་ན་སྡུག་པ་དང་མི་སྡུག་པའི་ཕྱིན་ཅི་ལོག་དག་ཀུན་ཏུ་འབྱུང་བས་དེའི་ཕྱིར་སྡུག་པ་དང་མི་སྡུག་པའི་ཕྱིན་ཅི་ལོག་དག་ལ་བརྟེན་ནས་འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་རྣམས་འབྱུང་ངོ་། །

[Block 2491]
འདིར་བཤད་པ།

[Block 2492 [VERSE]]
གཟུགས་སྒྲ་རོ་དང་རེག་པ་དང་། །
དྲི་དང་ཆོས་དག་འབའ་ཞིག་པ། །
དྲི་ཟའི་གྲོང་ཁྱེར་ལྟ་བུ་དང་། །
སྨིག་རྒྱུ་རྨི་ལམ་འདྲ་བ་ཡིན། །

[Block 2493 [VERSE]]
སྒྱུ་མའི་སྐྱེས་བུ་ལྟ་བུ་དང་། །
གཟུགས་བརྙན་འདྲ་བ་དེ་དག་ལ། །
སྡུག་པ་དང་ནི་མི་སྡུག་པ། །
འབྱུང་བར་ཡང་ནི་ག་ལ་འགྱུར། །

[Block 2494]
གཟུགས་དང་། སྒྲ་དང་། རོ་དང་། རེག་པ་དང་། དྲི་དང་། ཆོས་དག་ནི་འབའ་ཞིག་པ་བྲལ་བ་ཅི་ཡང་མེད་པ་མ་འདྲེས་པ་ངོ་བོ་ཉིད་མེད་པ་སྟེ། དྲི་ཟའི་གྲོང་ཁྱེར་ལྟ་བུ་དང་སྨིག་རྒྱུ་དང་རྨི་ལམ་འདྲ་བ་ཡིན་པས། སྒྱུ་མའི་སྐྱེས་བུ་ལྟ༌[^1626]བུ་དང་གཟུགས་བརྙན་དང༌[^1627]འདྲ་བ་དེ་དག་ལ་སྡུག་པ་དང་མི་སྡུག་པ་འབྱུང་བར་ག་ལ་འགྱུར།

[Block 2495]
ཡང་གཞན་ཡང་། གང་ལ་བརྟེན་ནས༌[^1628]སྡུག་པ་ཞེས།[^1629] །

[Block 2496 [VERSE]]
མི་སྡུག་པར་ནི་གདགས་བྱ་བ། །
སྡུག་པ་མི་ལྟོས༌[^1630]ཡོད་མིན་པས། །
དེ་ཕྱིར་སྡུག་པ་འཐད་མ་ཡིན། །

[Block 2497]
གང་ལ་བརྟེན་ནས་མི་སྡུག་པ་མི་སྡུག་པར་གདགས་པར་བྱའི་སྡུག་པ་མི་སྡུག་པ་ལ་མ་ལྟོས་པའི་སྔ་རོལ་ན་ཡོད་པ་མ་ཡིན་པས་དེའི་ཕྱིར་སྡུག་པ་འཐད་པ་མ་ཡིན་ནོ། །

[Block 2498]
གང་ལ་བརྟེན་ནས་མི༌[^1631]སྡུག་པ།[^1632] །

[Block 2499 [VERSE]]
སྡུག་པ་ཞེས་ནི་གདགས་བྱ་བ། །
མི་སྡུག་མི་ལྟོས༌[^1633]ཡོད་མིན་པས། །
དེ་ཕྱིར་མི་སྡུག་འཐད་མ་ཡིན། །

[Block 2500]
གང་ལ་བརྟེན་ནས་སྡུག་པ་སྡུག་པར་གདགས་པར་བྱའི་མི་སྡུག་པ༌[^1634]སྡུག་པ་ལ་མ་ལྟོས་པའི་སྔ་རོལ་ན་ཡོད་པ་མ་ཡིན་པས་དེའི་ཕྱིར་མི་སྡུག་པ་འཐད་པ་མ་ཡིན་ནོ། །

[Block 2501 [VERSE]]
སྡུག་པ་ཡོད་པ་མ་ཡིན་ན། །
འདོད་ཆགས་འབྱུང་བར་ག་ལ་འགྱུར། །
མི་སྡུག་ཡོད་པ་མ་ཡིན་ན། །
ཞེ་སྡང་འབྱུང་བར་ག་ལ་འགྱུར། །

[Block 2502]
སྡུག་པ་ཡོད་པ་མ་ཡིན་ན་འདོད་ཆགས་འབྱུང་བར་ག་ལ་འགྱུར་ཞིང་། མི་སྡུག་པ་ཡོད་པ་མ་ཡིན་ན་ཞེ་སྡང་འབྱུང་བར་ག་ལ་ཡང་འགྱུར། འདིར་སྨྲས་པ། མདོ་སྡེ་ལས་རྟག་པ་ལ་སོགས་པ་ཕྱིན་ཅི་ལོག་བཞི་ཡོད་པར་གསུངས་པས་དེ་དག་ཡོད་པའི་ཕྱིར་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་ཡང་ཡོད་དོ། །

[Block 2503]
དེ་ལ་གང་མི་རྟག་པ་ལ་རྟག་པ་ཞེས་འཛིན་པ་དེ་ནི་ཕྱིན་ཅི་ལོག་ཡིན་ལ། གང་མི་རྟག་པ་ལ་མི་རྟག་པ་ཞེས་བྱ་བར་འཛིན་པ་དེ་ནི་ཕྱིན་ཅི་ལོག་མ་ཡིན་ཏེ། ལྷག་མ་རྣམས་ལ་ཡང་དེ་བཞིན་ནོ། །

[Block 2504]
འདིར་བཤད་པ།

[Block 2505 [VERSE]]
གལ་ཏེ་མི་རྟག་རྟག་པ་ཞེས། །
དེ་ལྟར་འཛིན་པ་ལོག་ཡིན་ན། །
སྟོང་ལ་རྟག་པ་ཡོད་མིན་པས། །
འཛིན་པ་ཇི་ལྟར་ལོག་མ་ཡིན། །

[Block 2506]
གལ་ཏེ་མི་རྟག་པ་ལ་རྟག་པ་ཞེས་དེ་ལྟར་འཛིན་པ་ཕྱིན་ཅི་ལོག་མ༌[^1635]ཡིན་ནོ་སྙམ་དུ་སེམས་ན་དེ་ལ་བཤད་པར་བྱ་སྟེ། ངོ་བོ་ཉིད་སྟོང་པ་ལ་མི༌[^1636]རྟག་པ༌[^1637]ཅུང་ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་པས་དེ་མེད་ན་དེ་ལྟར་འཛིན་པ་ཇི་ལྟར་ཕྱིན་ཅི་ལོག་མ་ཡིན་པར་འགྱུར།

[Block 2507 [VERSE]]
ལྷག་མ་རྣམས་ལ་ཡང་དེ་བཞིན་ནོ། །
གལ་ཏེ་མི་རྟག་མི་རྟག་ཅེས། །
དེ་ལྟར་འཛིན་པ་ལོག་མིན་པ། །
སྟོང་ལ་མི་རྟག་ཡོད་མིན་པས། །

[Block 2508]
འཛིན་པ་ཇི་ལྟར་ལོག་མ་ཡིན། །གལ་ཏེ་མི་རྟག་པ་ལ་མི་རྟག་པ་ཞེས་དེ་ལྟར་འཛིན་པ་ཕྱིན་ཅི་ལོག་མ་ཡིན་ནོ་སྙམ་དུ་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ། ངོ་བོ་ཉིད་སྟོང་པ་ལ་མི་རྟག་པ་ཅུང་ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་པས་དེ་མེད་ན་དེ་ལྟར་འཛིན་པ་ཇི་ལྟར་ཕྱིན་ཅི་ལོག་མ་ཡིན་པར་འགྱུར།

[Block 2509 [VERSE]]
ལྷག་མ་རྣམས་ལ་ཡང་དེ་བཞིན་ནོ། །
གང་གིས་འཛིན་དང་འཛིན་གང་དང་། །
འཛིན་པ་པོ་དང་གང་གཟུང་བ། །
ཐམས་ཅད་ཉེ་བར་ཞི་བ་སྟེ། །
དེ་ཕྱིར་འཛིན་པ་ཡོད་མ་ཡིན། །

[Block 2510]
གང་གིས་འཛིན་པ་ནི་བྱེད་པར་གྱུར་པས་སོ། །

[Block 2511]
འཛིན་པ་གང་ཡིན་པ་ནི་དངོས་པོར་གྱུར་པའོ། །

[Block 2512]
འཛིན་པ་པོ་གང་ཡིན་པ་ནི་བྱེད་པ་པོར་གྱུར་པའོ། །

[Block 2513]
གང་གཟུང་བ་ནི་ལས་སུ་གྱུར་པའོ། །

[Block 2514]
དེ་དག་ཐམས་ཅད་ཉེ་བར་ཞི་བ་ནི་ངོ་བོ་ཉིད་ལས་ཉེ་བར་ཞི་བ་སྟེ། དེ་དག་ཇི་ལྟ་བ་དེ་ལྟར་སོང་བ་དང་མ་སོང་བ་དང་བགོམ་པ་བརྟག་པ༌[^1638]རྒྱས་པར་བཤད་ཟིན་པས། དེའི་ཕྱིར་འཛིན་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2515 [VERSE]]
ལོག་པའམ་ཡང་དག་ཉིད་དུ་ནི། །
འཛིན་པ་ཡོད་པ་མ་ཡིན་ན། །
གང་ལ་ཕྱིན་ཅི་ལོག་ཡོད་ཅིང་། །
གང་ལ་ཕྱིན་ཅི་མ་ལོག་ཡོད། །

[Block 2516]
ལོག་པའམ་ཡང་དག་པ་ཉིད་དུ་འཛིན་པ་དེ་དག་ཡོད་པ་མ་ཡིན་ན་གང་ལ་ཕྱིན་ཅི་ལོག་ཡོད་པར་འགྱུར་ཞིང་གང་ལ་ཕྱིན་ཅི་མ་ལོག་པ་ཡོད་པར་འགྱུར། ཡང་གཞན་ཡང་།

[Block 2517 [VERSE]]
ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་ལ། །
ཕྱིན་ཅི་ལོག་དག་མི་སྲིད་དོ། །
ཕྱིན་ཅི་ལོག་ཏུ་མ་གྱུར་ལའང་། །
ཕྱིན་ཅི་ལོག་དག་མི་སྲིད་དོ། །

[Block 2518 [VERSE]]
ཕྱིན་ཅི་ལོག་ཏུ་འགྱུར་བཞིན་ལའང་། །
ཕྱིན་ཅི་ལོག་དག་མི་སྲིད་དོ། །

[Block 2519]
ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་ལ་ཕྱིན་ཅི་ལོག་དག་མི་སྲིད་ཅིང་། ཕྱིན་ཅི་ལོག་ཏུ་མ་གྱུར་པ་ལ་ཡང་མི་སྲིད། ཕྱིན་ཅི་ལོག་ཏུ་འགྱུར་བཞིན་པ་ལ་ཡང་མི་སྲིད་དེ། ཇི་ལྟར་མི་སྲིད་པ་དེ་ལྟར་ནི་སོང་བ་དང་། མ་སོང་བ་དང་བགོམ་པ་བརྟག་པའི་རབ་ཏུ་བྱེད་པར་རྒྱས་པར་བསྟན་པ་བཞིན་དུ་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 2520 [VERSE]]
གང་ལ་ཕྱིན་ཅི་ལོག་སྲིད་པ། །
བདག་ཉིད་ཀྱིས་ནི་རྣམ་པར་དཔྱོད། །

[Block 2521]
ད་གང་ལ་ཕྱིན་ཅི་ལོག་དག་སྲིད་པ་བདག་ཉིད་ཀྱིས་རྣམ་པར་དཔྱོད་ཅིག །

[Block 2522]
ཡང་གཞན་ཡང་།

[Block 2523 [VERSE]]
ཕྱིན་ཅི་ལོག་རྣམས་མ་སྐྱེས་ན། །
ཇི་ལྟ་བུར་ན་ཡོད་པར་འགྱུར། །
ཕྱིན་ཅི་ལོག་རྣམས་སྐྱེ་མེད་ན། །
ཕྱིན་ཅི་ལོག་ཅན་ག་ལ་ཡོད། །

[Block 2524]
ཕྱིན་ཅི་ལོག་གང་དག་ངོ་བོ་ཉིད་ལས་མ་སྐྱེས་པ་དེ་དག་ཇི་ལྟ་བུར་ན་ཡོད་པར་འགྱུར། ད་ཕྱིན་ཅི་ལོག་དེ་རྣམས་ངོ་བོ་ཉིད་ལས་སྐྱེ་བ་མེད་ན་ཕྱིན་ཅི་ལོག་ཅན་ཡོད་པར་ག་ལ་འགྱུར།

[Block 2525 [VERSE]]
དངོས་པོ་བདག་ལས་མི་སྐྱེ་སྟེ། །
གཞན་ལས་སྐྱེ་བ་ཉིད་མ་ཡིན། །
བདག་དང་གཞན་ལས་ཀྱང་མིན་ན། །
ཕྱིན་ཅི་ལོག་ཅན་ག་ལ་ཡོད། །
--- END BLOCKS ---
