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
[Block 2206]
འདི་ལྟར་གལ་ཏེ་དུས་ལ་སོགས་པ་དག་མེད་པར་འགྱུར༌[^1473]ན། འོ་ན་དེ་ལྟ་ན་ཁྱད་པར་མེད་པས་དུས་ཐམས་ཅད་དུ་ཐམས་ཅད་ནས་ཐམས་ཅད་ཀྱང་། འབྱུང་བ་དང་འཇིག་པ་དག་ཏུ་འགྱུར་བ་ཞིག་ན་དེ་ལྟར་ཡང་མི་འགྱུར་བས། དེའི་ཕྱིར་དུས་ལ་སོགས་པ་དག་ནི་ཡོད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2207]
བཤད་པ། གལ་ཏེ་འགའ་ཞིག་ལ་འབྱུང་བ་དང་འཇིག་པ་དག་ཉིད་ཡོད་པར་གྱུར་ན་ནི། དུས་ལ་སོགས་པ་དག་ཀྱང་ཡོད་པར་འགྱུར་བ་ཞིག་ན། གང་གི་ཚེ།

[Block 2208 [VERSE]]
འཇིག་པ་འབྱུང་བ་མེད་པར་རམ། །
ལྷན་ཅིག་ཡོད་པ་ཉིད་མ་ཡིན། །
འབྱུང་བ་འཇིག་པ་མེད་པར་རམ། །
ལྷན་ཅིག་ཡོད་པ་ཉིད་མ་ཡིན། །

[Block 2209]
དེའི་ཚེ་གལ་ཏེ་འབྱུང་བ་དང་འཇིག་པ་དག་ཡོད་པར་གྱུར་ན། ཕན་ཚུན་མེད་པར་རམ་ལྷན་ཅིག་ཏུ་འགྱུར་གྲང་ན། གང་གི་ཚེ་གཉི་ག་ལྟར་ཡང་མི་འཐད་པ་དེའི་ཚེ་དེ་དག་གི་རྒྱུ་ཅན་གྱི་དུས་ལ་སོགས་པ་དག་ཇི་ལྟར་ཡོད་པར་གྱུར།[^1474] དེ་ཇི་ལྟར་ཞེ་ན། མི་འཐད་པའི་ཕྱིར་ཏེ།

[Block 2210 [VERSE]]
འཇིག་པ་འབྱུང་བ་མེད་པར་ནི། །
ཇི་ལྟ༌[^1475]བུར་ན་ཡོད་པར་འགྱུར། །
འཆི་བ་སྐྱེ་བ་མེད་པ་ལྟར། །
འཇིག་པ་འབྱུང་བ་མེད་པར་མེད། །

[Block 2211]
འདི་ལྟར་འཇིག་པ་འབྱུང་བ་མེད་པར་ཇི་ལྟར་ཡོད་པར་འགྱུར་ཏེ། གང་གི་ཚེ་འགའ་ཞིག་བྱུང་ན་འཇིག་པར་འགྱུར་གྱི་གཞི་མེད་པར་འཇིག་པར་མི་འགྱུར་ཏེ། དཔེར་ན་སྐྱེ་བ་ཡོད་ན་འཆི་བར་འགྱུར་གྱི་མ་སྐྱེས་པ་ལ་འཆི་བ་མེད་པ་དེ་བཞིན་དུ། འབྱུང་བ་ཡོད་ན་འཇིག་པར་འགྱུར་གྱི། འབྱུང་བ་མེད་པར་འཇིག་པར་མི་འགྱུར་རོ། །

[Block 2212]
དེ་ལ་འདི་སྙམ་དུ་འཇིག་པ་ནི་འབྱུང་བ་དང་ལྷན་ཅིག་ཡོད་པ་ཉིད་ཡིན་གྱི་འབྱུང་བ་མེད་པར་ནི་མ་ཡིན་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 2213 [VERSE]]
འཇིག་པ་འབྱུང་དང་ལྷན་ཅིག་ཏུ། །
ཇི་ལྟར་ཡོད་པ་ཉིད་དུ་འགྱུར། །
འཆི་བ་སྐྱེ༌[^1476]དང་དུས་གཅིག་ཏུ། །
ཡོད་པ་ཉིད་ནི་མ་ཡིན་བཞིན། །

[Block 2214]
འདི་ལྟར་འཇིག་པ་འབྱུང་བ་དང་ལྷན་ཅིག་ཇི་ལྟར་ཡོད་པར་འགྱུར་ཏེ། གང་གི་ཚེ་ན༌[^1477]དོན་དེ་གཉིས་ཕན་ཚུན་མི་མཐུན་པ་དག་ཡིན་པ་དེའི་ཚེ་དེ་གཉིས་གཅིག༌[^1478]ལ་ལྷན་ཅིག་ཡོད་པར༌[^1479]མི་འཐད་དེ། དཔེར་ན་འཆི་བ་ནི་སྐྱེ་བ་དང་ཕན་ཚུན་མི་མཐུན་པ་དེའི་ཕྱིར་དུས་གཅིག་ན་ཡོད་པ་ཉིད་མ་ཡིན་པ་དེ་བཞིན་དུ། འཇིག་པ་ཡང་འབྱུང་བ་དང་མི་མཐུན་པའི་ཕྱིར་ལྷན་ཅིག་ཡོད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2215]
སྨྲས་པ། གལ་ཏེ་འཇིག་པ་བྱུང་བ༌[^1480]མེད་པར་ཡང་མི་འཐད་ལ་ལྷན་ཅིག་ཏུ་ཡང་མི་འཐད་པས་འཇིག་པ་མེད་དུ་ཟིན་ཀྱང་། རེ་ཞིག་འབྱུང་བ་ནི་ཡོད་དེ། དེ་ཡོད་པའི་ཕྱིར་དུས་ལ་སོགས་པ་དག་ཀྱང་ཡོད་དོ། །

[Block 2216]
བཤད༌[^1481]པ།

[Block 2217 [VERSE]]
འབྱུང་བ་འཇིག་པ་མེད་པར་ནི། །
ཇི་ལྟར་ཡོད་པ་ཉིད་དུ་འགྱུར། །
དངོས་པོ་རྣམས་ལ་མི་རྟག༌[^1482]ཉིད། །
ནམ་ཡང་མེད་པ་མ་ཡིན་ནོ། །

[Block 2218]
འདི་ལྟར་འབྱུང་བ་འཇིག་པ་མེད་པར་ཇི་ལྟར་ཡོད་པ་ཉིད་དུ་འགྱུར་ཏེ། དངོས་པོ་རྣམས་ལ་མི་རྟག་པ་ཉིད་ནམ་ཡང་མེད་པ་མ་ཡིན་པས། འདི་ལྟར་འབྱུང་བ་འཇིག་པ་མེད་པར་ཇི་ལྟར་ཡོད་པ་ཉིད་དུ་འགྱུར། གང་གི་ཚེ་དངོས་པོ་ཐམས་ཅད་མི་རྟག་པ་ཉིད་ཀྱིས་མི་རྟག་པ་དང་རྗེས་སུ་འབྲེལ་པ་དེའི་ཚེ་དངོས་པོ་རྣམས་ལ་མི་རྟག་པ་ཉིད་ནམ་ཡང་མེད་པ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 2219]
འདི་ལྟར་གལ་ཏེ་དངོས་པོ་སྐད་ཅིག་ཙམ་ཞིག་མི་རྟག་པ་ཉིད་དང་བྲལ་བར་འགྱུར་ན་ནི་དེ་ལྟར་ན་ཡུན་རིང་དུ༌[^1483]བྲལ་བར་འགྱུར་ཏེ། དེ་ལྟར༌[^1484]ན་ཡང་རྟག་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བས་དེ་ཡང་མི་འདོད་དོ། །

[Block 2220]
དེ་ལྟ་བས་ན་དངོས་པོ་རྣམས་ནི་རྟག་ཏུ་མི་རྟག་པ་ཉིད་དང་རྗེས་སུ་འབྲེལ་པས། འབྱུང་བ་འཇིག་པ་མེད་པར་ཡོད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2221]
དེ་ལ་འདི་སྙམ་དུ་འབྱུང་བ་ནི་འཇིག་པ་དང་ལྷན་ཅིག་ཡོད་པ་ཉིད་ཡིན་གྱི་འཇིག་པ་མེད་པར་ནི་མ་ཡིན་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 2222 [VERSE]]
འབྱུང་བ་འཇིག་དང་ལྷན་ཅིག་ཏུ། །
ཇི་ལྟར་ཡོད་པ་ཉིད་དུ་འགྱུར། །
སྐྱེ་བ་འཆི་དང་དུས་གཅིག་ཏུ། །
ཡོད་པ་ཉིད་དུ་མི་རིགས་བཞིན། །

[Block 2223]
འདི་ལྟར་འབྱུང་བ་དང༌[^1485]འཇིག་པ་དང་ལྷན་ཅིག་ཇི་ལྟར་ཡོད་པར་འགྱུར་ཏེ། གང་གི་ཚེ་དོན་དེ་གཉིས་ཕན་ཚུན་མི་མཐུན་པ་དག་ཡིན་པ་དེའི་ཚེ་དེ་གཉིས་གཅིག་ལ་ལྷན་ཅིག་ཡོད་པ༌[^1486]མི་འཐད་དེ། དཔེར་ན་སྐྱེ་བ་ནི་འཆི་བ་དང་ཕན་ཚུན་མི་མཐུན་པའི་ཕྱིར་དུས་གཅིག་ན་ཡོད་པ་མ་ཡིན་པ་དེ་བཞིན་དུ། འབྱུང་བ་ཡང་འཇིག་པ་དང་མི་མཐུན་པའི་ཕྱིར་ལྷན་ཅིག་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2224]
དེའི་ཕྱིར་དེ་ལྟར་ཡོངས་སུ་བརྟགས་ན་འབྱུང་བ་དང་འཇིག་པ་དག་ཕན་ཚུན་མེད་པར་རམ། ཕན་ཚུན་ལྷན་ཅིག་ཏུ་འགྲུབ་པར་མི་འཐད་པས།

[Block 2225 [VERSE]]
གང་དག་ཕན་ཚུན་ལྷན་ཅིག་གམ། །
ཕན་ཚུན་ལྷན་ཅིག་མ་ཡིན་པར། །
གྲུབ་པ་ཡོད་པ་མ་ཡིན་པ། །
དེ་དག་འགྲུབ་པ་ཇི་ལྟར་ཡོད། །

[Block 2226]
འབྱུང་བ་དང་འཇིག་པ་གང་དག་ཕན་ཚུན་ལྷན་ཅིག་གམ། ཕན་ཚུན་ལྷན་ཅིག་མ་ཡིན་པར་གྲུབ་པ་ཡོད་པ་མ་ཡིན་པ་དེ་དག་དང་རྣམ་པ་གཞན་གང་གིས་འགྲུབ་པ་ཡོད་པར་སེམས། དེ་ལྟ་བས་ན་འབྱུང་བ་དང་འཇིག་པ༌[^1487]དག་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2227]
དེ་དག་མེད་ན་དུས་ལ་སོགས་པ་དག་ཡོད་པར་ག་ལ་འགྱུར། སྨྲས་པ། གནས་པ་ཡོད་པས་སྐྱོན་མེད་དེ། འདི་ལ་འབྱུང་བ་དང་འཇིག་པ་དག་གི་བར་ན་གནས་པ་ཡོད་དེ། གནས་པ་ཡོད་པས་འབྱུང་བ༌[^1488]དང་འཇིག་པ་དག་གང་ཡང་རུང་བ་མེད་པར་ཡང་ཡོད་པ་མ་ཡིན་ལ། འབྱུང་བ་དང་འཇིག་པ་དག་དུས་གཅིག་ཏུ་ཡང་མི་འགྱུར་བས་དེའི་ཕྱིར་སྐྱོན་མེད་དོ། །

[Block 2228]
བཤད་པ། དེ་ཡང་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་རྣམས་ནི་མི་རྟག་པ་ཉིད་དང་། རྗེས་སུ་འབྲེལ་པ་ཡིན་པས་དངོས་པོ་འགའ་ཡང་རང་གི་གནས་ན་སྐད་ཅིག་ཙམ་ཡང་མི་སྡོད་པའི་ཕྱིར་རོ། །

[Block 2229]
དེའི་ཕྱིར། ཟད་ལ་འབྱུང་བ་ཡོད་མ་ཡིན། གང་གི་ཕྱིར་དངོས་པོ་རྣམས་མི་རྟག་པ་ཉིད་དང་ནམ་ཡང་མ་འབྲེལ༌[^1489]ཏེ་རྟག་ཏུ་མི་རྟག་པ་ཉིད་དང་རྗེས་སུ་འབྲེལ་པ་དེའི་ཕྱིར་དངོས་པོ་ཟད་པར་འགྱུར་བ་ལ་འབྱུང་བ་ཡོད་པ་མ་ཡིན་པ་ཉིད་དེ། འབྱུང་བ་མེད་ན་གནས་པ་ཡོད་པར་ག་ལ་འགྱུར།

[Block 2230]
སྨྲས་པ། འབྱུང་བའི་དུས་ན་ཟད་པར་མི་འགྱུར་བས་དེའི་ཕྱིར་འབྱུང་བ་ཡོད་དོ། །

[Block 2231]
འབྱུང་བ་གནས་པར་འགྱུར་ཞིང་གནས་པ་ཕྱིས་འཇིག་པར་འགྱུར་རོ། །

[Block 2232]
བཤད་པ། མ་ཟད་པ་ལའང་འབྱུང་བ་མེད། །གང་ཟད་པའི་མཚན་ཉིད་དང་བྲལ་བ་དེ་ལ་ཡང་འབྱུང་བ་མེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2233]
འདི་ལྟར་དངོས་པོ་ནི་ཟད་པའི་མཚན་ཉིད་ཅན་ཡིན་པས་དེའི་ཕྱིར་གང་ཟད་པའི་མཚན་ཉིད་དང་བྲལ་བ་དེ་དངོས་པོ་ཉིད་མ་ཡིན་ནོ། །

[Block 2234]
གང་དངོས་པོ་མ་ཡིན་པ་དེ་ལ༌[^1490]ཇི་ལྟར་འབྱུང་བར་འགྱུར་ཏེ། དེ་ལ་དེ་ལྟར༌[^1491]འབྱུང་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་སྙད་ཉིད་ཀྱང་མེད་པས། དེའི་ཕྱིར་མ་ཟད་པ་ལའང་འབྱུང་བ་མེད་དོ། །

[Block 2235 [VERSE]]
ཟད་ལ་འཇིག་པ་ཡོད་མ་ཡིན། །
མ་ཟད་པ་ལ་འང་འཇིག་པ་མེད། །

[Block 2236]
དེ་ལྟར་གང་གི་ཕྱིར་ཟད་པ་ལ་འབྱུང་བ་མི་འཐད་ལ་འབྱུང་བ་མེད་ན༌[^1492]གནས་པ་ཉིད་ཀྱང་མེད་པ་དེའི་ཕྱིར་མ་བྱུང་བ་དང་མི་གནས་པ་འདི༌[^1493]ཟད་པ་ལ་འཇིག་པ་ཡོད་པ་མ་ཡིན་ལ། མ་ཟད་པ་ལ༌[^1494]ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2237]
འབྱུང་བ་དང་འཇིག་པ་གང་དག་ཟད་པ་ལ་ཡོད་པ་མ་ཡིན་ལ། མ་ཟད་པ་ལ་ཡང་ཡོད་པ་མ་ཡིན་པ་དེ་དག༌[^1495]གཞན་གང་ཞིག་ལ་ཡོད་པར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་འབྱུང་བ་ཡང་ཡོད་པ་མ་ཡིན་ལ། འཇིག་པ་ཡང་ཡོད་པ༌[^1496]མ་ཡིན་ནོ། །

[Block 2238]
སྨྲས་པ། རེ་ཞིག་དངོས་པོ་རྣམས་ནི་ཡོད་དེ་མ་བྱུང་བ་ནི་དངོས་པོར་མི་འཐད་པས་འབྱུང་བ་ཡང་རབ་ཏུ་གྲུབ་པ་ཉིད་དོ། །

[Block 2239]
གང་ལས་བྱུང༌[^1497]བ་ཡོད་པ་དེ་ལ་འཇིག་པ་ཡང་ངེས་པར་ཡོད་པས་འཇིག་པ་ཡང་རབ་ཏུ་གྲུབ་པ་ཉིད་དོ། །

[Block 2240]
བཤད་པ། ཅི་ཁྱོད་ཤིང་བི་དུ་ལའི་ཤིང་ཏོག་དག་འདོད་དམ། ཁྱོད་འབྱུང་བ་དང་འཇིག་པ་དག་ཡོད་པ་མ་ཡིན་པར་དངོས་པོ་ཡོད་པར་འདོད་ཀོ །འབྱུང་བ་དང་འཇིག་པ་དག་བསལ་བས་དངོས་པོ་ཡང་བསལ་བ་ཉིད་མ་ཡིན་ནམ། དེ་ཇི་ལྟར་ཞེ་ན། གང་གི་ཕྱིར།

[Block 2241 [VERSE]]
འབྱུང་དང་འཇིག་པ་མེད་པར་ནི། །
དངོས་པོ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2242]
འདི་ལྟར་གལ་ཏེ་དངོས་པོ་འབའ་ཞིག་ཡོད་པར་གྱུར་ན་དེ་འབྱུང༌[^1498]བའི་ཆོས་ཅན་ནམ། འཇིག་པའི་ཆོས་ཅན་ཞིག་ཡིན་གྲང་ན། གང་གི་ཚེ་འབྱུང་བ་དང་འཇིག་པ་དག་མི་འཐད་པ་ཡིན་པ་དེའི་ཚེ། དངོས་པོ་ཡོད་དོ་ཞེས་བྱ་བ་དེ་ཇི་ལྟར་འཐད་པར་འགྱུར།

[Block 2243 [VERSE]]
དངོས་པོ་ཡོད་པ་མ་ཡིན་པར། །
འབྱུང་དང་འཇིག་པ་ཡོད་མ་ཡིན། །

[Block 2244]
དེ་ལྟར་གང་གི་ཕྱིར་ཡོངས་སུ་བརྟགས༌[^1499]ན་དངོས་པོ་ཉིད་མི་འཐད་པ་དེའི་ཕྱིར་དངོས་པོ་ཡོད་པ་མ་ཡིན་པར་གཞི་མེད་པའི་འབྱུང་བ༌[^1500]དང་འཇིག་པ་དག་ཡོད་པ་མ་ཡིན་པས། དེ་ལ་དངོས་པོ་ཡོད་ན་འབྱུང་བ་དང་འཇིག་པ་དག་ཀྱང་རབ་ཏུ་གྲུབ་པ་ཉིད་དོ་ཞེས་གང་སྨྲས་པ་དེ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2245]
ཡང་གཞན་ཡང་། འདི་ལ་གལ་ཏེ་འབྱུང་བ་དང་འཇིག་པ་དག་ཡོད་པར་གྱུར་ན། དེ་དག་དངོས་པོ་ངོ་བོ་ཉིད་སྟོང་པའམ་མི་སྟོང་པ་ལ་ཡོད་པར་འགྱུར་གྲང་ན། དེ་ལ།
--- END BLOCKS ---
