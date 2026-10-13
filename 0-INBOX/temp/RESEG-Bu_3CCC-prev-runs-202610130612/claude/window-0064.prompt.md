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

[Block 2246 [VERSE]]
སྟོང་ལ་འབྱུང་དང་འཇིག་པ་དག །
འཐད་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 2247]
རེ་ཞིག་དངོས་པོ་ངོ་བོ་ཉིད་སྟོང་པ་ལ་འབྱུང་བ་དང་འཇིག་པ་དག་ཡོད་པར་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2248]
འདི་ལྟར་ངོ་བོ་ཉིད་ཡོད་པ་མ་ཡིན་པ་ལ་དེ་དག་གང་གིས་ཡོད་པར་འགྱུར། ངོ་བོ་ཉིད་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་གང་གི་འདིའོ་ཞེས་ཐ་སྙད༌[^1501]གདགས་པ་ཉིད་ཀྱང་ཡོད་པ་མ་ཡིན་པ་དེ་ལ་ཅི་ཞིག་འབྱུང་ངོ་ཞེའམ། ཅི་ཞིག་འཇིག་གོ་ཞེས་ཇི་སྐད་དུ་བརྗོད་པར་བྱ། དེ་ལྟ་བས་ན་སྟོང་པ་ལ་འབྱུང་བ་དང་འཇིག་པ་དག་འཐད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2249]
དེ་ལ་འདི་སྙམ་དུ་དངོས་པོ་ངོ་བོ་ཉིད་མི་སྟོང་བ་ལ་འབྱུང་བ་དང་འཇིག་པ་དག་ཡོད་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 2250 [VERSE]]
མི་སྟོང་པ་ལའང་འབྱུང་འཇིག་དག །
འཐད་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 2251]
དངོས་པོ་རང་གི་བདག་ཉིད་ཀྱིས་ཡོད་པར་འགྱུར་བ་མེད་པ་ལ་འབྱུང་བ་དང་འཇིག་པ་དག་ཡོད་པར་འཐད་པ་ཉིད་མ་ཡིན་ཏེ། འདི་ལྟར་རང་བཞིན་ནི་གཞན་དུ་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2252]
དེ་ལྟ་བས་ན་མི་སྟོང་པ་ལ་ཡང་འབྱུང་བ་དང་འཇིག་པ་དག་འཐད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2253]
ཡང་གཞན་ཡང་། འདི་ལ་གལ་ཏེ་འབྱུང་བ་དང་འཇིག་པ་དག་ཡོད་པར་གྱུར་ན། གཅིག་པ་ཉིད་དམ་གཞན་ཉིད་དུ་འགྱུར་གྲང་ན། དེ་ལ།

[Block 2254 [VERSE]]
འབྱུང་བ་དང་ནི་འཇིག་པ་དག །
གཅིག་པ་ཉིད་དུ་མི་འཐད་དོ། །
འབྱུང་བ་དང་ནི་འཇིག་པ་དག །
གཞན་ཉིད་དུ་ཡང་མི་འཐད་དོ། །

[Block 2255]
རེ་ཞིག་འབྱུང་བ་དང་འཇིག་པ་དག་གཅིག་པ་ཉིད་དུ་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་འབྱུང་བ་ནི་སྐྱེ་བ་ཡིན་ལ་འཇིག་པ་ནི་འགག་པ་སྟེ། དོན་ཐ་དད་པའི་ཕྱིར་མི་མཐུན་པ་དེ་གཉིས་ཇི་ལྟར་གཅིག་པ་ཉིད་དུ་འགྱུར། འབྱུང་བ་དང་འཇིག་པ་དག༌[^1502]གཞན་ཉིད་དུ་ཡང་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་ཐམས་ཅད་ནི་ཟད་པའི་བདག་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་ཏེ། འདི་ལྟར་དངོས་པོ་འགའ་ཡང་སྐད་ཅིག་ཙམ་ཡང་མི་རྟག་པ་ཉིད་དང་བྲལ་བ་མེད་པ་དེའི་ཕྱིར་དངོས་པོ་ཐམས་ཅད་ཟད་པའི་བདག་ཉིད་ཅན་ཡིན་ནོ། །

[Block 2256]
དངོས་པོ་ནི་ངོ་བོ་ཉིད་ལས་གཞན་ཉིད་དུ་མི་འཐད་པས་འབྱུང་བ་དང་འཇིག་པ་དག་གཞན་ཉིད་དུ་མི་འཐད་དོ། །

[Block 2257]
དེ་ལྟར་གང་གི་ཕྱིར་འབྱུང་བ་དང་འཇིག་པ་དག་གཅིག་པ་ཉིད་དང་གཞན་ཉིད་དུ་མི་འཐད་པའི་ཕྱིར་འབྱུང་བ་དང་།

[Block 2258 [VERSE]]
འཇིག་པ་དག་མི་འཐད་པ་ཉིད་དོ། །
འབྱུང་བ་དང་ནི་འཇིག་པ་དག །
མཐོང་ངོ་སྙམ་དུ་ཁྱོད་སེམས་ན། །

[Block 2259]
ཁྱོད་འདི་སྙམ་དུ་དངོས་པོ་རྣམས་ཀྱི་འབྱུང་བ་དང་འཇིག་པ་དག་མངོན་སུམ་ཉིད་དུ་མཐོང་བས་དེ་ལ་འཐད་པ་གཞན་ཅི་དགོས་སྙམ་དུ་སེམས་ནའོ། །

[Block 2260]
དེ་ནི་རིགས་པ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 2261 [VERSE]]
འབྱུང་བ་དང་ནི་འཇིག་པ་དག །
གཏི་མུག་ཉིད་ཀྱིས་མཐོང་བ་ཡིན། །

[Block 2262]
གཏི་མུག་གིས་སེམས་བསྒྲིབས་པ་མི་མཁས་པ་དག་འབྱུང་བ་དང་འཇིག་པ་དག་མཐོང་ངོ་སྙམ་དུ་དེ་ལྟར་སེམས་ཀྱི་འབྱུང་བ་དང་འཇིག་པ་དག་མཐོང་བར་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་གལ་ཏེ་འབྱུང་བ་དང་འཇིག་པ་དག་ཡོད་པར་འགྱུར༌[^1503]ན་དངོས་པོའམ་དངོས་པོ་མེད་པ་ལ་བརྟེན༌[^1504]གྲང་ན། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དེ་དག་ནི་ཡོད་པ་མ་ཡིན་ཏེ། དེ་དག་མེད་ན་གཞི་མེད་པའི་འབྱུང་བ་དང་། འཇིག་པ་དག་མཐོང་བར་ག་ལ་རིགས།

[Block 2263]
སྨྲས་པ། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་ཇི་ལྟར༌[^1505]ཡོད་པ་མ་ཡིན། བཤད་པ། འདི་ལ་གལ་ཏེ་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་ཡོད་པར་གྱུར་ན། དེ་དག་དངོས་པོ་ལས་སམ། དངོས་པོ་མེད་པ་ལས་སྐྱེ་གྲང་ན། དེ་ལ།

[Block 2264 [VERSE]]
དངོས་པོ་དངོས་ལས་མི་སྐྱེ་སྟེ། །
དངོས་མེད་དངོས་ལས་མི་སྐྱེའོ། །
དངོས་པོ་དངོས་ཡོད་མི་སྐྱེ་སྟེ། །
དངོས་མེད་དངོས་མེད་མི་སྐྱེའོ། །

[Block 2265]
དེ་ལ་རེ་ཞིག་དངོས་པོ་དངོས་པོ་ལས་སྐྱེ་བ་མེད་དེ། འདི་ལྟར་བུམ་པ་ནི་འཇིམ་པ་ངེས་པར་གནས་པ་ལས་མི་སྐྱེའོ། །

[Block 2266]
ཅི་སྟེ་བུམ་པ་ནི༌[^1506]འཇིམ་པ་བཅོས་པ་ལས་སྐྱེ་བར་སེམས་ན། དེ་ལྟར༌[^1507]ན་ཡང་འཇིམ་པ་བཅོས་ཤིང་འགགས་པ་ན། བུམ་པ་སྐྱེ་བས་དངོས་པོ་དངོས་པོ་ལས༌[^1508]སྐྱེ་བ་མ་ཡིན་ཏེ། འདི་ལྟར་འགགས་ཤིང་མེད་པ་ནི་དངོས་པོ་མ་ཡིན་ཏེ། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་དོན་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 2267]
ཅི་སྟེ་ཡང་འདི་སྙམ་དུ་འཇིམ་པའི་དངོས་པོ་ཉིད་བུམ་པ་ཡིན་པར་སེམས་ན། དེ་ལྟ་ན་ཡང་དངོས་པོ་དངོས་པོ་ལས་སྐྱེ་བ་མ་ཡིན་ཏེ། འཇིམ་པ་ལས་གཞན་པའི་དངོས་པོ་གཞན་མི་སྐྱེ་བའི་ཕྱིར་ཏེ། འཇིམ་པ་ཉིད་བུམ་པར་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 2268]
དེ་ལ་འདི་སྙམ་དུ་ཤིང་ཏོག་གི་དངོས་པོ་ཤིང་ལྗོན་པའི་དངོས་པོ་ལས་སྐྱེ་བར་སེམས་ན། དེ་ཡང་མི་རུང་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། ཤིང་ཏོག་ལས་ཤིང་ལྗོན་པ་གཞན་ཡིན་པར་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 2269]
དེ་ལྟར་རེ་ཞིག་དངོས་པོ་དངོས་པོ་ལས༌[^1509]སྐྱེ་བ་མེད་དོ། །

[Block 2270]
དངོས་པོ་མེད་པ་ཡང་དངོས་པོ་ལས༌[^1510]སྐྱེ་བ་མེད་དེ། འདི་ལྟར་བུམ་པ་ཆག་པ་ནི་བུམ་པ་ངེས་པར་གནས་པ་ལས་མི་སྐྱེ་སྟེ། ངེས་པར་གནས་པ་ལ་ཆག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2271]
བུམ་པ་ཆག་པ་བུམ་པའི་དངོས་པོ་ལས་ཀྱང་མི་སྐྱེ་སྟེ། ཆག་ཅིང་མེད་པ་ནི་དངོས་པོ་མེད་པའི་ཕྱིར་རོ། །

[Block 2272]
དེ་ལ་འདི་སྙམ་དུ་བུམ་པ་དངོས་པོ་མེད་པ་ཐོ་བའི་དངོས་པོ་ལས་སྐྱེ་བར་སེམས་ན་དེ༌[^1511]ཡང་མི་རུང་སྟེ། འདི་ལྟར་གལ་ཏེ་དངོས་པོ་མེད་པ་ཐོ་བ་ལས་སྐྱེ་བར་འགྱུར་ན་བུམ་པ་མེད་པར་ཡང་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2273]
གལ་ཏེ་དངོས་པོ་མེད་པ་སྐྱེ་ན་དངོས་པོ་མེད་པ་ཉིད་དུ་མི་འགྱུར་ཏེ། སྐྱེ་བ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2274]
སྐྱེ་བ་ཞེས་བྱ་བ་ཅི་ཡང་མེད་ན་ནི་སྐྱེའོ། །ཞེས་བྱ་བ་དེ་ལ་སུ་ཞིག་ཡིད་ཆེས་པར་རིགས། དེ་ལྟ་བས་ན་དངོས་པོ་མེད་པ་ཡང་དངོས་པོ་ལས་སྐྱེ་བ་མེད་དོ། །

[Block 2275]
དངོས་པོ་ཡང་དངོས་པོ་མེད་པ་ལས་སྐྱེ་བ་མེད་དེ། འདི་ལྟར་བུམ་པ་ནི་འཇིམ་པ་འགགས་པ༌[^1512]ལས་མི་སྐྱེ་སྟེ། འགགས་པ་ནི་མེད་པའི་ཕྱིར་རོ། །

[Block 2276]
ཅི་སྟེ་དངོས་པོ་འགགས་ཤིང་མེད་པ་ལས་སྐྱེ་བར་གྱུར་ན། དེ་ལྟ་ན་དངོས་པོ་སྐྱེ་བ་རྒྱུ་མེད་པ་ཅན་དུ་འགྱུར་བས་དེ༌[^1513]མི་འདོད་དེ། དུས་ཐམས་ཅད་དུ་ཐམས་ཅད་ལས་ཐམས་ཅད་སྐྱེ་བ་དང་རྩོམ་པ་ཐམས་ཅད་དོན་མེད་པ་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2277]
དེ་ལྟ་བས་ན་དངོས་པོ་ཡང་དངོས་པོ་མེད་པ་ལས་སྐྱེ་བ་མེད་དེ། དངོས་པོ་མེད་པ་ཡང་དངོས་པོ་མེད་པ་ལས་སྐྱེ་བ་མེད་དོ། །

[Block 2278]
འདི་ལྟར་དངོས་པོ་མེད་པ་བུམ་པའི་དངོས་པོ་མེད་པ་ལས་མི་སྐྱེ་སྟེ། བུམ་པའི་དངོས་པོ་མེད་པ་ནི་བུམ་པ་ལོག་པ་ཙམ་སྟེ། ཅི་ཡང་མེད་པའི་ཕྱིར་དང་བསྐྱེད་པར་བྱ་བའི་དོན་ནི་ཅི་ཞིག་གང༌[^1514]ཡིན་པའི་ཕྱིར་རོ། །

[Block 2279]
ཅི་སྟེ་ཅི་ཡང་མེད་པ་ཅི་ཡང་མེད་པ་ལས་སྐྱེ་བར་འགྱུར་ན་ནི་དེ་ལྟ་ན་རི་བོང་གི་རྭ་ཡང་རྟའི་རྭ་ལས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2280]
ཅི་སྟེ་དངོས་པོ་མེད་པ་ཅི་ཞིག་ཡིན་ན་ནི་ཅི་ཞིག་ཡིན་པའི་ཕྱིར་དངོས་པོ་ཉིད་ཡིན་གྱི་དངོས་པོ་མེད་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
