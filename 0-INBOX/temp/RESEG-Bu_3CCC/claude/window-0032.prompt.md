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
[Block 1121]
དེ་ལྟ་བས་ན་ལྟ་བ་ལ་སོགས་པ་རེ་རེའི་སྔ་རོལ་ན་ཡོད་པ་དང་། ལྟ་བ་ལ་སོགས་པ་གཞན་དང་གཞན་གྱིས་གསལ་བར་བྱེད་དོ་ཞེས་གང་སྨྲས་པ་དེ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1122]
སྨྲས་པ། ལྟ༌[^687]ལ་སོགས་པ་དག་གི་སྔ་རོལ་ན་བདག་ཡོད་པ་ཉིད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལ་མིང་དང་གཟུགས་ཀྱི་རྐྱེན་གྱིས་སྐྱེ་མཆེད་དྲུག་ཅེས་གསུངས་ལ། གཟུགས་ཞེས་བྱ་བ་ནི་འབྱུང་བ་ཆེན་པོ་བཞི་པོ་དག་ཡིན་པས་དེའི་ཕྱིར་འབྱུང་བའི་རྐྱེན་གྱིས་སྐྱེ་མཆེད་དྲུག་འབྱུང་ལ། འབྱུང་བ་དེ་དག་ཀྱང་བདག་གི་ཉེ་བར་བླང་བ་ཡིན་ནོ། །

[Block 1123]
དེ་ལྟ་བས་ན། འབྱུང་བ་ཉེ་བར་ལེན་པ་པོ་འབྱུང་བས་གསལ་བར་བྱས་པའི་བདག་གནས་པ་ཡོད་ན་སྐྱེ་མཆེད་དྲུག་འབྱུང་ཞིང་རིམ་གྱིས་ཚོར་བ་ལ་སོགས་པ་དག་ཀྱང་འབྱུང་བས་དེས༌[^688]ན་ལྟ་བ་ལ་སོགས་པ་དག་གི་སྔ་རོལ་ན་དངོས་པོ་གནས་པ་ཡོད་དོ་ཞེས་བྱ་བ་དེ་འཐད་དོ། །

[Block 1124]
བཤད་པ།

[Block 1125 [VERSE]]
ལྟ་དང་ཉན་ལ་སོགས་པ་དང་། །
ཚོར་བ་དག་ལ་སོགས་པ་ཡང་། །
གང་ལས་འགྱུར་བའི་འབྱུང་དེ་ལའང་། །
དེ་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1126]
ལྟ་དང་ཉན་ལ་སོགས་པ་དང་། །ཚོར་བ་ལ་སོགས་པ་དག་རིམ་གྱིས་གང་དག་ལས་འགྱུར་བའི་འབྱུང་བ་དེ་དག་ལ་ཡང་ཁྱོད་ཀྱིས་བརྟགས་པའི་དངོས་པོ་དེ་ནི་ཡོད་པ་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། འབྱུང་བ་ཉེ་བར་ལེན་པ་པོ་ཡིན་པའི་ཕྱིར་ཏེ། འབྱུང་བ་ཉེ་བར་ལེན་པ་པོ་དེ་ཡང་འབྱུང་བ་དག་གི་སྔ་རོལ་ན་གསལ་བར་བྱེད་པ་མེད་པས་མི་འཐད་དོ། །

[Block 1127]
གང་འབྱུང་བ་དག་གི་སྔ་རོལ་ན་ཡོད་པ་མ་ཡིན་པ་དེ་ཇི་ལྟར་འབྱུང་བ་དག་གི་ཉེ་བར་ལེན་པ་པོར་འགྱུར། དེ་ལྟ་བས་ན་འབྱུང་བ་དག་ལ་ཡང་དེ་ཡོད་པ་མ་ཡིན་ན་ལྟ་བ་ལ་སོགས་པ་དག་གི་སྔ་རོལ་ན་ཡོད་པར་ག་ལ་འགྱུར།

[Block 1128]
སྨྲས་པ། ལྟ་བ་ལ་སོགས་པ་དག་གི་སྔ་རོལ་ན་དེ་ཡོད་ཀྱང་རུང་མེད་ཀྱང་རུང་སྟེ། ཡོད་ནི་རེ་ཞིག་ལྟ་བ་ལ་སོགས་པ་དག་ནི་ཡོད་དེ། ཁྱོད་ཀྱིས༌[^689]སྔར།

[Block 1129 [VERSE]]
ཅི་མེད་གང་ཞིག་ག་ལ༌[^690]ཡོད། །
གང་མེད་ཅི་ཞིག་ག་ལ་ཡོད། །

[Block 1130]
ཅེས་སྨྲས་པས། དེའི་ཕྱིར་ལྟ་བ་ལ་སོགས་པ་ཅི་ཞིག་པོ་དག་ཡོད་དོ། །

[Block 1131]
གང་ཞིག་མེད་ན་ཅི་ཞིག་ཀྱང་མེད་པས་དེའི་ཕྱིར་ལྟ་བ་ལ་སོགས་པ་ཅི་ཞིག་པོ་དག་གང་གི་ཡིན་པའི་དངོས་པོ་གང་ཞིག་པོ་དེ་ཡང་ཡོད་དོ། །

[Block 1132]
བཤད་པ། གང་མེད་ཅི་ཞིག་ག་ལ་ཡོད། །ཅེས་བྱ་བ་དེས་དེའི་ལན་བཏབ་ཟིན་ཏོ། །ཇི་ལྟར་ཞེ་ན།

[Block 1133 [VERSE]]
ལྟ་དང་ཉན་ལ་སོགས་པ་དང་། །
ཚོར་བ་དག་ལ་སོགས་པ་ཡང་། །
གང་གི་ཡིན་པ་གལ་ཏེ་མེད། །
དེ་དག་ཀྱང་ནི་ཡོད་མ་ཡིན། །

[Block 1134]
ལྟ་བ་ལ་སོགས་པ་ཅི་ཞིག་པོ་དག་གི༌[^691]སྔ་རོལ་ན་དངོས་པོ་གང་ཞིག་པོ་མེད་དོ་ཞེས་བྱ་བ་དེ་ནི་སྔར་བསྟན་ཟིན་ཏོ། །

[Block 1135]
གང་མེད་ཅི་ཞིག་ག་ལ་ཡོད་ཅེས་བྱ་བ་དེ་ཡང་བསྟན་ཟིན་ཏེ། དེའི་ཕྱིར་གལ་ཏེ་ལྟ་བ་ལ་སོགས་པ་ཅི་ཞིག་པོ་དག་རབ་ཏུ་སྒྲུབ་པར་བྱེད་ཅིང་ལྟ་བ་ལ་སོགས་པ་དག་གང་གི་ཡིན་པར་འགྱུར་བ་གང་ཞིག་པོ་དེ་ཉིད་མེད་ན། ལྟ་བ་ལ་སོགས་པ་དག་རབ་ཏུ་འགྲུབ་པར་ག་ལ་འགྱུར་ཏེ། གང་གི་ལྟ་བ་ལ་སོགས་པར་འགྱུར། དེ་ལྟ་བས་ན་དངོས་པོ་གང་ཞིག་པོ་མེད་པའི་ཕྱིར། ལྟ་བ་ལ་སོགས་པ་ཅི་ཞིག་པོ་དག༌[^692]ཀྱང་མེད་ལ། ལྟ་བ་ལ་སོགས་པ་ཅི་ཞིག་པོ་དག་མེད་ན་ཁྱོད་ཀྱི་དངོས་པོ་གང་ཞིག༌[^693]ཡོད་པར་ག་ལ་འགྱུར།

[Block 1136]
སྨྲས་པ། ཅི་ཁྱོད་ཀྱི་དངོས་པོ་གང་ཞིག་པོ་མེད་པ༌[^694]དེ་ཤིན་ཏུ་ངེས་པ༌[^695]ཡིན་ནམ། བཤད་པ།

[Block 1137 [VERSE]]
གང་ཞིག་ལྟ་ལ་སོགས་པ་ཡི། །
སྔ་རོལ་ད་ལྟར་ཕྱི་ན་མེད། །
དེ་ལ་ཡོད་དོ་མེད་དོ་ཞེས། །
རྟོག་པ་དག་ནི་ལྡོག་པར་འགྱུར། །

[Block 1138]
གང་ཞིག་པོ་ལྟ་བ་ལ་སོགས་པ་དག་གི་སྔ་རོལ༌[^696]དང་ལྟ་བ་ལ་སོགས་པ་དག་དང་། ད་ལྟར་ལྷན་ཅིག་དང་། ལྟ་བ་ལ་སོགས་པ་དག་གི་ཕྱི་དུས་རྣམ་པ་ཐམས་ཅད་དུ་བཙལ་ན། དེ་འདིའོ་ཞེས་རང་གིས་རབ་ཏུ་གྲུབ་པ་མེད་པ་དེ་ལ་ལྟ་བ་ལ་སོགས་པ་དག་གིས་ཡོད་དོ་མེད༌[^697]དོ་ཞེས་གདགས་པའི་རྟོག་པ་དག་ལྡོག་པར་འགྱུར་ཏེ། རེ་ཞིག་རང་ཉིད་རབ་ཏུ་མ་གྲུབ་པའི་ཕྱིར་དེ༌[^698]ཡོད་དོ་ཞེས་ཇི་སྐད་བརྗོད་པར་ནུས། ལྟ་བ་ལ་སོགས་པ་དག་གིས༌[^699]གསལ་བར་བྱེད་པའི་ཕྱིར་དེ་མེད་དོ་ཞེས་ཀྱང་ཇི་སྐད་བརྗོད་པར་ནུས་ཏེ། དེའི་ཕྱིར་དེ་ལ་ཡོད་དོ་མེད་དོ་ཞེས་རྟོག་པ་དག་མི་འཐད་དོ། །

[Block 1139]
དེ་ལྟ་བས་ན་བྱེད་པ་པོ་དང་ལས་དག་བཞིན་དུ་ཉེ་བར་ལེན་པ་དེ་ཡང་གདགས་པར་ཟད་ཀྱི། དེ་མ་གཏོགས་པར་འགྲུབ་པ་གཞན་མི་འཐད་དོ། །

[Block 1140]
ཉེ་བར་ལེན་པ་པོ་དང་ཉེ་བར་བླང་བ་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་དགུ་པའོ།། །།

[Block 1141 [HEADING]]
## མེ་དང་བུད་ཤིང་བརྟག་པ། ^10-0

[Block 1142]
སྨྲས་པ། མེ་དང་བུད་ཤིང་དག་བཞིན་དུ། ཉེ་བར་ལེན་པ་པོ་དང་ཉེ་བར་བླང་བ་དག་རབ་ཏུ་འགྲུབ་ཀྱི། བྱེད་པ་པོ་དང་ལས་དག་བཞིན་དུ་རབ་ཏུ་མི་འགྲུབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 1143]
བཤད་པ། གལ་ཏེ་མེ༌[^700]བུད་ཤིང་རབ་ཏུ་གྲུབ་ན་ནི་དེ་དག་ཀྱང་རབ་ཏུ་འགྲུབ་པར་འགྱུར་གྲང་ན། གང་གི་ཚེ་མེ་དང་བུད་ཤིང་དག་བྱེད་པ་པོ་དང་ལས་དག་ཁོ་ན་བཞིན་དུ་རབ་ཏུ་མི་འགྲུབ་པ་དེའི་ཚེ་ཉེ་བར་ལེན་པ་པོ་དང་། ཉེ་བར་བླང་བ་དག་ཇི་ལྟར་རབ་ཏུ་འགྲུབ་པར་འགྱུར། གལ་ཏེ་མེ་དང་བུད་ཤིང་དག་ངོ་བོ་ཉིད་ཀྱིས་རབ་ཏུ་གྲུབ་པར་གྱུར་ན། གཅིག་པ་ཉིད་དམ་གཞན་ཉིད་དུ་རབ་ཏུ་འགྲུབ་པར་འགྱུར་གྲང་ན། གཉི་ག་ལྟར་ཡང་མི་འཐད་དོ། །

[Block 1144]
ཇི་ལྟར་ཞེ་ན།

[Block 1145 [VERSE]]
བུད་ཤིང་གང༌[^701]དེ་མེ་ཡིན་ན། །
བྱེད་པ་པོ་དང་ལས་གཅིག་འགྱུར། །

[Block 1146]
གལ་ཏེ་རེ་ཞིག་བུད་ཤིང་གང་ཁོ་ན་ཡིན་པ་དེ་ཉིད་མེ་ཡིན་པར་རབ་ཏུ་རྟོག་ན། དེ་ལྟ་ན་བྱེད་པ་པོ་དང་ལས་གཅིག་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་ཏེ། དེ་ལ་མེ་ནི་སྲེག་པར་བྱེད་པའོ་ཞེས་བྱ་བ་དག་མི་སྲིད་པར་འགྱུར་རོ། །

[Block 1147]
ཅི་སྟེ་གཅིག་པ་ཉིད་ཡིན་ཡང་དེ་དག་སྲིད་ན་ནི་མེ་ནི་སྲེག་པར་བྱེད་པའོ། །

[Block 1148]
བུད་ཤིང་ནི་བསྲེག་པར༌[^702]བྱ་བའོ་ཞེས་བྱ་བ་དག་ཀྱང་སྲིད་པར་འགྱུར་བ་ཞིག་ན་མི་སྲིད་པས་དེ་ལྟ་བས་ན་དེ་གཉིས་གཅིག་པ་ཉིད༌[^703]མི་འཐད་དོ། །

[Block 1149]
དེ་ལ་བུད་ཤིང་ལས་མེ་གཞན་ཉིད་ཡིན་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 1150 [VERSE]]
གལ་ཏེ་ཤིང་ལས་མེ་གཞན་ན། །
ཤིང་མེད་པར་ཡང་འབྱུང་བར་འགྱུར། །

[Block 1151]
གལ་ཏེ་བུད་ཤིང་ལས་མེ་གཞན་ཉིད་ཡིན་པར་གྱུར་ན། བུད་ཤིང་མེད་ཅིང་བུད་ཤིང་མ་གཏོགས་པར༌[^704]ཁོ་ནར་ཡང་མི་འབྱུང་བར་འགྱུར་བ་ཞིག་ན། བུད་ཤིང་མེད་པར་མེ༌[^705]འབྱུང་བས་དེ་ལྟ་བས་ན་དེ་ཉིད་གཞན་ཉིད་དུ་ཡང་མི་འཐད་དོ། །

[Block 1152]
ཡང་གཞན་ཡང་།

[Block 1153 [VERSE]]
རྟག་ཏུ་འབར་བ་ཉིད་དུ་འགྱུར། །
འབར་བྱེད་མེད་པའི་རྒྱུ་ལས་བྱུང་། །
རྩོམ་པ་དོན་མེད་ཉིད་དུ་འགྱུར། །
དེ་ལྟར་ཡིན་ན་ལས་ཀྱང་མེད། །

[Block 1154]
གལ་ཏེ་བུད་ཤིང་ལས་མེ་གཞན་ཉིད་ཡིན་པར་གྱུར་ན་རྟག་ཏུ་འབར་ན༌[^706]ཉིད་དུ་འགྱུར་ཏེ། འདི་ལྟར་འབར་བྱེད་མེད་པའི་རྒྱུ་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 1155]
དེའི་འབར་བར་བྱེད་པའི་རྒྱུ་གང་ཡིན་པ་དེ་ནི་འབར་བྱེད་ཀྱི་རྒྱུའོ། །

[Block 1156]
འབར་བར་བྱེད་པའི་རྒྱུ་མེད་པ་ནི་འབར་བྱེད་མེད་པའི་རྒྱུ་ལས་བྱུང་བ་སྟེ། འབར་བར་བྱེད་པ་མེད་པ་ཁོ་ནར་མེ་འབྱུང་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1157]
རྩོམ་པ་དོན་མེད་པ་ཉིད་དུ་ཡང་འགྱུར་རོ། །

[Block 1158]
དེ་ལྟ་ཡིན་ན་ལས་མེད་པའི་མེར་ཡང་འགྱུར་ཏེ། མེ་ཞེས་བྱ་བ་འདི་ནི་སྲེག་པར་བྱེད་པའོ་ཞེས་བྱ་བ་དེ་ལྟ་བུའི་ལས་བསྟན་དུ་མེད་པར་ཡང་འགྱུར་རོ། །

[Block 1159]
སྨྲས་པ། མེ་འབར་བྱེད་མེད་པའི་རྒྱུ་ལས་བྱུང་བར་འགྱུར་རོ་ཞེས་གང་བཤད་པ་དེ་ཇི་ལྟ་བུ། བཤད་པ།

[Block 1160 [VERSE]]
གཞན་ལ་ལྟོས་པ་མེད་པའི་ཕྱིར། །
འབར་བྱེད་མེད་པའི་རྒྱུ་ལས་བྱུང་། །
--- END BLOCKS ---
