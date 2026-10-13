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
[Block 1541]
དེ་མེད་ན་ཕྲད་པར་བྱེད་པ་མེད་པ༌[^999]ཕྲད་པ་པོ་ཡོད་པར་ཇི་ལྟར་འགྱུར། དེའི་ཕྱིར་དེ་ལྟར་རིགས་པ་སྔོན་དུ་བཏང་སྟེ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་བརྟགས་ན།

[Block 1542 [VERSE]]
ཕྲད་བཞིན་པ་དང་ཕྲད་པ་དང་། །
ཕྲད་པ་པོ་ཡང་ཡོད་མ་ཡིན། །

[Block 1543]
དེ་དག་མེད་ན་ཁྱོད་ཀྱི་ཕྲད་པ་བསྟན་པའི་གཏན་ཚིགས་ལས་བྱུང་བའི་དངོས་པོའི་ངོ་བོ་ཉིད་འགྲུབ་པར་ག་ལ་འགྱུར། ཕྲད་པ་བརྟགས་པ༌[^1000]ཞེས་བྱ་བ་སྟེ། རབ་ཏུ་བྱེད་པ་བཅུ་བཞི་པའོ།། །།

[Block 1544 [HEADING]]
## དངོས་པོ་དང་དངོས་པོ་མེད་པ་བརྟག་པ། ^15-0

[Block 1545]
སྨྲས་པ། ཁྱོད་དངོས་པོ་ཡོད་པ་མི་དམིགས་པའི་ཕྱིར་དངོས་པོ་འདི་དག་ངོ་བོ་ཉིད་མེད་པ་ཡིན་པར་སེམས་ཤིང་། དངོས་པོ་རྣམས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་བྱ་བར་ཡང་ཡོད༌[^1001]ལ་དངོས་པོ་རྣམས་ངོ་བོ་ཉིད་མེད་པར་ཡང་སྨྲ་ན། ཇི་ལྟར་དངོས་པོ་བྱུང་བ་ཡང་ཡིན་ལ། ངོ་བོ་ཉིད་མེད་པ་ཡང་ཡིན་པར་འགྱུར། གལ་ཏེ་རྒྱུ་དང་རྐྱེན་རྣམས་ལས་དངོས་པོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་ཁོ་ན་མི་འབྱུང་ན། དེ་ལས་གཞན་ཅི་ཞིག་འབྱུང་བར་འགྱུར།[^1002] གལ་ཏེ་རྒྱུ་སྤུན་དག་ལས་སྣམ་བུའི་ངོ་བོ་ཉིད་ཁོ་ན་མི་འབྱུང་ན་ཅི་རྒྱུ་སྤུན་གྱི་ངོ་བོ་ཉིད་དག༌[^1003]ཁོ་ན་འབྱུང་ངམ། ཅི་སྟེ་ཅི་ཡང་མི་འབྱུང་ན་ནི་འབྱུང་ཞེས་ཀྱང་ཇི་སྐད་དུ་བརྗོད།[^1004] །

[Block 1546]
བཤད་པ། ཅི་ཁྱོད་རྟ་ལ་ཞོན་བཞིན་ཉིད༌[^1005]དུ་རྟ་མ་མཐོང་ངམ། ཁྱོད་དངོས་པོ་རྣམས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་ཀྱང་སྨྲ་ལ། དེ་དག་གང་གི་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ཀྱང་མ་མཐོང་ཀོ། །དེ་ནི་རེ་ཞིག་བློ་རྩིང་བ་རྣམས་ཀྱིས་ཀྱང་བདེ་བླག་ཏུ་ཤེས་པར་འགྱུར་ཏེ།

[Block 1547 [VERSE]]
ངོ་བོ་ཉིད་ནི་རྒྱུ་རྐྱེན་ལས། །
འབྱུང་བར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1548]
འདི་ལ་བདག་གི་དངོས་པོ་ནི་ངོ་བོ་ཉིད་ཅེས་བྱ་བ༌[^1006]སྟེ། བདག་གི་དངོས་པོ་ཡོད་པ་ནི་ཡང་རྒྱུ་དང་རྐྱེན་རྣམས་ལས་འབྱུང་བར་མི་རིགས་ཏེ། འདི་ལྟར་ཡོད་པ་ལ་ཡང་བྱ་བ་ཅི་ཡོད་བྱ་བ་མེད་ན་རྒྱུ་དང་རྐྱེན་རྣམས་ཀྱིས་ཅི་བྱ། ཅི་སྟེ་དེ་རྒྱུ་དང་རྐྱེན་རྣམས་ལས་འབྱུང་ན། དེ་ལྟ་ན། རྒྱུ་དང་རྐྱེན་ལས་བྱུང་བ་ཡི།[^1007] །ངོ་བོ་ཉིད་ནི་བྱས་པར་འགྱུར། །དེ་ཡང་མི་འཐད་དོ། །

[Block 1549]
སྨྲས་པ། ངོ་བོ་ཉིད་ནི་བྱས་པ་ཁོ་ན་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་སྣམ་བུའི་དངོས་པོ་སྔོན་མ་བྱུང་བ་ཕྱིས༌[^1008]བྱེད་པའི་ཕྱིར་རོ། །

[Block 1550]
བཤད་པ།

[Block 1551 [VERSE]]
ངོ་བོ་ཉིད་ནི་བྱས་པ་ཞེས། །
ཇི་ལྟ་བུར་ན༌[^1009]རུང་བར་འགྱུར། །

[Block 1552]
ངོ་བོ་ཉིད་བྱས་པ་ཞེས་བྱ་བར་ཇི་ལྟར་རུང་བར་འགྱུར་ཏེ། སྨྲས་པ། [^1010]གང་གི་ཚེ་དོན་དེ་དག་དགག་པ་མི་མཐུན་པ་ཡིན་ཏེ། གལ་ཏེ་ངོ་བོ་ཉིད་ཡིན་ན་ནི་བྱས་པ་མ་ཡིན་ལ་ཅི་སྟེ་བྱས་པ་ཡིན་ན་ནི། ངོ་བོ་ཉིད་མ་ཡིན་པ་དེའི་ཚེ་ངོ་བོ་ཉིད་ཀྱང་ཡིན་ལ་བྱས་པ་ཡང་ཡིན་ནོ། །ཞེས་སེམས་དང་བཅས་པ་སུ་ཞིག་དེ་ལྟར་འཛིན་པར་འགྱུར། །

[Block 1553]
སྨྲས་པ། ཁྱོད་ངོ་བོ་ཉིད་རིགས་པ་གང་དང་ལྡན་པར་སེམས། བཤད་པ།

[Block 1554 [VERSE]]
ངོ་བོ་ཉིད་ནི་བཅོས༌[^1011]མིན་དང་། །
གཞན་ལ་ལྟོས་པ་མེད་པ་ཡིན། །

[Block 1555]
གང་བྱ་བས་བསྒྲུབ་པར་མི་འགྱུར་བ་དང་། རྒྱུ་དང་རྐྱེན་ལ་ཡང་ལྟོས་པར༌[^1012]མི་འགྱུར་བ༌[^1013]རང་ཉིད་ཀྱི་ངོ་བོ་ཉིད༌[^1014]མི་འགྱུར་བར་འཇུག་པ་དེ་ནི་ངོ་བོ་ཉིད་ཀྱིས༌[^1015]རིགས་པ་ཡིན་ནོ། །

[Block 1556]
གང་བྱས་པས༌[^1016]བསྒྲུབ་པར་འགྱུར་བ་དང་རྒྱུ་དང་རྐྱེན་ལ་ཡང་ལྟོས་པར་འགྱུར་བ་དེ་ནི་གཞན་ལ་རག་ལས་པས༌[^1017]གཞན་ལ་ལྟོས་པ༌[^1018]རང་གི་བདག་ཉིད་ཀྱིས་རབ་ཏུ་མ་གྲུབ་པ་ཡིན་པས་ངོ་བོ་ཉིད་ཅེས་བྱ་བར་ཇི་ལྟར་འཐད་པར་འགྱུར། སྨྲས་པ། གང་ལ་ལྟོས་ནས་དེ་དངོས་པོར་འགྱུར་བའི་གཞན་གྱི༌[^1019]དངོས་པོ་ནི་རེ་ཞིག་ཡོད་དོ། །

[Block 1557]
གཞན་གྱི་དངོས་པོ་རབ་ཏུ་གྲུབ་ན། ངོ་བོ་ཉིད་ཀྱང་རབ་ཏུ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 1558]
བཤད་པ། གཉེན་པོ་ལ་བརྟེན་ནས་ཀྱང་ངོ་བོ་ཉིད་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། གཞན་གྱི་དངོས་པོ་མི་འཐད་པའི་ཕྱིར་ཏེ།

[Block 1559 [VERSE]]
ངོ་བོ་ཉིད་ནི་ཡོད་མིན་ན། །
གཞན་གྱི་དངོས་པོ་ག་ལ་ཡོད། །

[Block 1560]
གལ་ཏེ་ངོ་བོ་ཉིད་རབ་ཏུ་གྲུབ་པར་གྱུར་ན་ནི་དེས་ན་དེའི་གཉེན་པོ་གཞན་གྱི་དངོས་པོ་ཡང་ཡོད་པར་འགྱུར་བ་ཞིག་ན། ངོ་བོ་ཉིད་མི་འཐད་དེ་ངོ་བོ་ཉིད་ཡོད་པ་མ་ཡིན་ན་གཞན་གྱི་དངོས་པོ་ག་ལ་ཡོད། དེ་གཞན་གྱི་དངོས་པོ་མེད་ན་དེའི་གཉེན་པོ་ངོ་བོ་ཉིད་འཐད་པར་ག་ལ་འགྱུར། ཡང་གཞན་ཡང་། ངོ་བོ་ཉིད་ཀྱང་གཞན་ལ་གཞན་གྱི་དངོས་པོ་ཡང་གཞན་ནི་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 1561 [VERSE]]
གཞན་གྱི་དངོས་པོའི་ངོ་བོ་ཉིད། །
གཞན་གྱི་དངོས་པོ་ཡིན་ཞེས་བརྗོད། །

[Block 1562]
འདི་ལྟར་གཞན་གྱི་དངོས་པོའི་ངོ་བོ་ཉིད་གང་ཡིན་པ་དེ་གཞན་གྱི་དངོས་པོ་ཞེས་བརྗོད་པ་ཡིན་པས། དེའི་ཕྱིར་གལ་ཏེ་གཞན་གྱི་དངོས་པོ་དེའི་ངོ་བོ་ཉིད་མེད་པ་ཁོ་ན་ཡིན་ན་གང་གིས་དེ་ཡོད་པར་འགྱུར། དེའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱང་གཞན་ལ་གཞན་གྱི་དངོས་པོ་ཡང་གཞན་ཞེས་བྱ་བར་མི་འཐད་དོ། །

[Block 1563]
དེ་ལྟ་ན་གཉེན་པོ་ཉིད་མེད་དེ། གཅིག་པ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1564]
གཉེན་པོ་མེད་ན་ཇི་ལྟར་གཉེན་པོ་ལ་བརྟེན་ནས་འགྲུབ་པར་འགྱུར། སྨྲས་པ། དངོས་པོའི་ངོ་བོ་ཉིད་ཡོད་དོ། །

[Block 1565]
མེད་དོ། །ཞེས་བྱ་བ་འདིས། ཁོ་བོ་ལ་ཅི་བྱར༌[^1020]ཡོད་རེ་ཞིག་དངོས་པོ༌[^1021]ཡོད་དོ། །

[Block 1566]
བཤད་པ།

[Block 1567 [VERSE]]
ངོ་བོ་ཉིད་དང་གཞན་དངོས་དག །
མ་གཏོགས་དངོས་པོ་ག་ལ་ཡོད། །
ངོ་བོ་ཉིད་དང་གཞན་དངོས་དག །
ཡོད་ན་དངོས་པོ༌[^1022]འགྲུབ་པར་འགྱུར། །

[Block 1568]
གལ་ཏེ་དངོས་པོ་འགའ་ཞིག་ཡོད་པར་འགྱུར༌[^1023]ན། ངོ་བོ་ཉིད་དང༌[^1024]གཞན་གྱི་དངོས་པོ་ཞིག་ཡིན་གྲང་སྟེ། དེའི་ཕྱིར་ངོ་བོ་ཉིད་དང་གཞན་གྱི་དངོས་པོ༌[^1025]དག་ཡོད་ན་དངོས་པོ་འགྲུབ་པར་འགྱུར་ན། གང་གི་ཚེ་ངོ་བོ་ཉིད་ཀྱང་མེད་ལ། གཞན་གྱི་དངོས་པོ་ཡང་མེད་པ་དེའི་ཚེ་ངོ་བོ་ཉིད་དང་གཞན་གྱི་དངོས་པོ་དག་མ་གཏོགས་པའི་དངོས་པོ་བརྗོད་པར་བྱ་བ་མ་ཡིན་པ་རང་དང་གཞན་དུ་མ་གྱུར་པ་འབའ་ཞིག་པ་དེ་ཡོད་པར་ག་ལ་འགྱུར།

[Block 1569]
སྨྲས་པ། དེ་ལྟ་ན་དངོས་པོ་རྣམས་ཀྱི་དངོས་པོ་མེད་པ་ཡོད་དེ། དངོས་པོ་མེད་པ་ཡང་མ་ལྟོས་པར་བྱེད་པས་གང་གི་ཕྱིར༌[^1026]དངོས་པོ་མེད་པར་འགྱུར་བའི་དངོས་པོ་ཡང་ཡོད་དེ། བཤད་པ། དེ་ལྟ་ན་ཡང་དངོས་པོ་རབ་ཏུ་འགྲུབ་པར་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་མེད་པ་རབ་ཏུ་མ་གྲུབ་པའི་ཕྱིར་ཏེ།

[Block 1570 [VERSE]]
ངོ་བོ་ཉིད་དང་གཞན་དངོས་དག །
མ་གཏོགས་དངོས་པོ་ག་ལ་ཡོད། །

[Block 1571]
ཅེས་སྨྲས་ཟིན་ཏོ། །

[Block 1572]
དེའི་ཕྱིར།

[Block 1573 [VERSE]]
གལ་ཏེ་དངོས་པོ་མ་གྲུབ་ན། །
དངོས་མེད་འགྲུབ་པར་མི་འགྱུར་རོ། །

[Block 1574]
གལ་ཏེ་དངོས་པོ་ཉིད་འགའ་ཡང་རབ་ཏུ་མ་གྲུབ་ན་དངོས་པོ་མེད་པ་འགྲུབ་པར་མི་འགྱུར་བ་ཉིད་དོ་ཞེས་སྨྲས་པ་ཉིད་མ་ཡིན་ནམ། ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1575 [VERSE]]
དངོས་པོ་གཞན་དུ་འགྱུར་བ་ནི། །
དངོས་མེད་ཡིན་པར་སྐྱེ་བོ་སྨྲ། །

[Block 1576]
འདི་ལྟར་དངོས་པོ་གཞན་དུ་འགྱུར་བ་གང་ཡིན་པ་དེ་དངོས་པོ་མེད་པ་ཡིན་ནོ། །ཞེས་སྐྱེ་བོ་དག་སྨྲ་ན། དངོས་པོ་དེ་ཡང་མེད་དེ། དེ་མེད་ན་དངོས་པོ་མེད་པ་དེ་གང་གི་ཡིན་པར་འགྱུར། དངོས་པོ་མེད་པ༌[^1027]ན་ཁྱོད་ཀྱི་དེའི་གཉེན་པོ་དངོས་པོ་འཐད་པར་ག་ལ་འགྱུར།

[Block 1577]
སྨྲས་པ། འདི་ལ་དེ་ཁོ་ན་མཐོང་བས་ཐར་པར་འགྱུར་རོ། །ཞེས་བྱ་ཞིང་། དེ་ཁོ་ན༌[^1028]ཞེས་བྱ་བ་ཡང་དེའི་དངོས་པོ་ནི་དེ་ཁོ་ན་སྟེ།[^1029] དངོས་པོའི་ངོ་བོ་ཉིད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1578]
དེ་ལ་གལ་ཏེ་དངོས་པོའི་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ཡིན་ན་དེ་ལྟ་ན་ཁྱོད་ལ་དེ་ཁོ་ན་མཐོང་བ་མི་འཐད་པར་མི་འགྱུར་རམ། དེ་ཁོ་ན་མཐོང་བ་མེད་ན་ཐར་པ་འཐད་པར༌[^1030]ཇི་ལྟར་འགྱུར། དེ་ལྟ་བས་ན་དངོས་པོ་རྣམས་ངོ་བོ་ཉིད་མེད་པ་ཞེས་བྱ་བར་ལྟ་བ་དེ་ནི་བཟང་པོ་མ་ཡིན་ནོ། །

[Block 1579]
བཤད་པ། ལོག་པར་མ་འཛིན་ཅིག །

[Block 1580 [VERSE]]
གང་དག་དངོས་ཉིད་གཞན་དངོས་དང་། །
དངོས་དང་དངོས་མེད་ཉིད་ལྟ་བ། །
དེ་དག་སངས་རྒྱས་བསྟན་པ་ལ། །
དེ་ཉིད་མཐོང་བ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
