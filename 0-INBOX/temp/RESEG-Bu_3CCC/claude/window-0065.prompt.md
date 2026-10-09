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

[Block 2281]
དེ་ལྟ་བས་ན་དངོས་པོ་མེད་པ་ཡང་དངོས༌[^1515]མེད་པ་ལས་སྐྱེ་བ་མེད་དོ། །

[Block 2282]
ཡང་གཞན་ཡང་། འདི་ལྟར་གལ་ཏེ་དངོས་པོ་སྐྱེ་བར་འགྱུར་ན་དེ་བདག་ལས་སམ་གཞན་ལས་སམ་གཉི་ག་ལས་སྐྱེ་བར་འགྱུར་གྲང་ན། དེ་ལ་དངོས་པོ་བདག་ལས་མི་སྐྱེ་སྟེ། །

[Block 2283 [VERSE]]
གཞན་ལས་སྐྱེ་བ་ཉིད་མ་ཡིན། །
བདག་དང་གཞན་ལས་སྐྱེ་བ་ནི། །
ཡོད་མིན་ཇི་ལྟར་སྐྱེ་བར་འགྱུར། །

[Block 2284]
རེ་ཞིག་དངོས་པོ་ནི་བདག་ལས་སྐྱེ་བ་མེད་དེ། རང་གི་བདག་ཉིད་ཀྱིས་ཡོད་པ་ལ་ནི་ཡང་སྐྱེ་བར་བརྟག་པ་དོན་མེད་པ་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་དང་། ཐུག་པ་མེད་པར་ཐལ་བའི་སྐྱོན་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2285]
རང་གི་བདག་ཉིད་ཀྱིས་མེད་པ་ལ་ནི་བདག་ལས་ཞེས་བྱ་བའི་ཚིག་ཀྱང་མི་འཐད་པའི་ཕྱིར་ཏེ། དེ་ལྟ་བས་ན་དངོས་པོ༌[^1516]ནི་བདག་ལས་སྐྱེ་བ་མེད་དོ། །

[Block 2286]
དངོས་པོ་ནི་གནས༌[^1517]ལས་ཀྱང་སྐྱེ་བ་མེད་དེ། དངོས་པོ་མ་སྐྱེས་ཤིང་མེད་པ་ལ་གཞན་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 2287]
འདི་ལྟར་འགའ་ཞིག་ཡོད་ན་གཞན་ཡང་ཡོད་པར་འགྱུར་ན་དེ་ཡང་མེད་དེ། དེ་མེད་ན་གཞན་ཡོད་པར་ག་ལ་འགྱུར། ཅི་སྟེ་འགྱུར་ན་ནི་དེ་ཉིད་དངོས་པོ་ཡིན་པས་ཡོད་པ་དེ་ལ་ཡང་སྐྱེ་བར༌[^1518]ཅི་བྱ་སྟེ། སྐྱེ་བར་བརྟགས་པ་དོན་མེད་པ་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2288]
དེ་ལྟ་བས་ན་མ་སྐྱེས་པས་གཞན་མེད་པ་ཁོ་ནའི་ཕྱིར་དངོས་པོ་ནི་གཞན་ལས་སྐྱེ་བ་མེད་དོ།[^1519] དངོས་པོ་ནི་བདག་དང་གཞན་ལས་ཀྱང་སྐྱེ་བ་མེད་དེ། ཇི་སྐད་བསྟན་པའི་སྐྱོན་གཉི་གར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2289]
དེ་ལྟ་བས་ན་དངོས་པོ་ནི་གཉི་ག་ལས་ཀྱང་སྐྱེ་བ་མེད་དོ། །

[Block 2290]
དངོས་པོ་གང་བདག་དང་གཞན་དང་གཉི་ག་ལས་སྐྱེ་བ་མེད་པ་དེ་དག་གཞན་གང་ལས་སྐྱེ་བར་སེམས། དེ་ལྟ་བས་ན་དངོས་པོ་མི་འཐད་དོ། །

[Block 2291]
དངོས་པོ་ཡོད་པ་མ་ཡིན་ན་གང་གི་དངོས་པོ་མེད་པར༌[^1520]འགྱུར། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་ཡོད་པ་མ་ཡིན་ན་གཞི་མེད་པར་འབྱུང་བ་དང་འཇིག་པ་དག་ཇི་ལྟར་ཡོད་པར་གྱུར་ན། ཡང་གཞན་ཡང་།

[Block 2292 [VERSE]]
དངོས་པོ་ཡོད་པར་ཁས་བླངས་ན། །
རྟག་དང་ཆད་པར་ལྟ་བར་ནི། །
ཐལ་བར་འགྱུར་ཏེ་དངོས་དེ་ནི། །
རྟག་དང་མི་རྟག་འགྱུར་ཕྱིར་རོ། །

[Block 2293]
དངོས་པོ༌[^1521]ལྟ་བ་ཡོད་ན་སྐྱོན་ཆེན་པོ་གཞན་འདིར་ཡང་འགྱུར་ཏེ། གང་གི་ཕྱིར་དངོས་པོ་དེ་ཡོད་པར་ཁས་བླངས་ན་རྟག་པ་དང་ཆད་པར་ལྟ་བར་ཐལ་བར་འགྱུར་རོ། །ཇི་ལྟར་ཞེ་ན། འདི་ལྟར་ཡོད་པ༌[^1522]དེ་ནི་རྟག་པ་དང་མི་རྟག་པའི་ཕྱིར་ཏེ། དངོས་པོ་གང་ཡིན་པ་དེ་ཡོད་པར་ཁས་ལེན་ན་དེ་རྟག་པའམ། མི་རྟག་པར་འགྱུར་ཏེ། དེ་ལས་གཞན་དུ་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 2294]
དེ་ལྟར༌[^1523]རེ་ཞིག་གལ་ཏེ་དངོས་པོ་དེ་རྟག་ན་ནི་རྟག་པའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་ལ། འོན་ཏེ་མི་རྟག་ན་ནི་ཆད་པའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་བས་དེ་ཡང་མི་འདོད་དེ་སྐྱོན་ཆེ་བའི་ཕྱིར་རོ། །

[Block 2295]
སྨྲས་པ།

[Block 2296 [VERSE]]
དངོས་པོ་ཡོད་པར་ཁས་བླངས་ཀྱང་། །
ཆད་པར་མི་འགྱུར་རྟག་མི་འགྱུར། །

[Block 2297]
འདི་ལྟར་དངོས་པོ་ཡོད་པར་ཁས་བླངས་ཀྱང་། །རྟག་པར་ལྟ་བར་ཐལ་བར་ཡང་མི་འགྱུར་ལ། ཆད་པར་ལྟ་བར་ཐལ་བར་ཡང་མི་འགྱུར་ཏེ། ཁྱོད་གཞུང་ལུགས་གསལ་བར་མི་ཤེས་པས་དེ་ལྟར་སེམས་པར་ཟད་དོ། །

[Block 2298]
འདི་ལྟར་གལ་ཏེ་དངོས་པོ་ཡོད་པར་ཁས་བླངས་ན། རྟག་པ་དང་ཆད་པའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་ན། དེ་ལྟ་ན་སྲིད་པ་མི་འཐད་པར་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། རྟག་པ་ནི་ངེས་པར་གནས་པའི་ཕྱིར་དང་། ཆད་པ་ནི་མི་འཇུག་པའི་ཕྱིར་རོ། །

[Block 2299]
དངོས་པོར་ལྟ་བ་ཡོད་ན་ཡང་སྲིད་པ་འཐད་པས་དེའི་ཕྱིར་རྟག་པ་དང་ཆད་པར་ལྟ་བའི་སྐྱོན་དུ་ཐལ་བར་མི་འགྱུར་རོ། །

[Block 2300]
དེ་ཇི་ལྟར་ཞེ་ན།

[Block 2301 [VERSE]]
འབྲས་བུ་རྒྱུ་ཡི་འབྱུང་འཇིག་གི །
རྒྱུན་དེ་སྲིད་པ་ཡིན་ཕྱིར་རོ། །

[Block 2302]
འདི་ལྟར་འབྲས་བུ་དང་རྒྱུའི་འབྱུང་བ་དང་འཇིག་པའི་རྒྱུན་གང་ཡིན་པ་དེ་ནི་སྲིད་པ་ཡིན་ཏེ། དེ་ལ་གང་གི་ཕྱིར་རྒྱུ་འཇིག་པར་འགྱུར་བ་དེའི་ཕྱིར་རྟག་པའི་སྐྱོན་དུ་ཐལ་བར་མི་འགྱུར་ལ། གང་གི་ཕྱིར་རྒྱུ་འགག་བཞིན་པ་ལས་འབྲས་བུ་འབྱུང་བར་འགྱུར་བ་དེའི་ཕྱིར་ཆད་པའི་སྐྱོན་དུ་ཐལ་བར་མི་འགྱུར་ཏེ། དེའི་ཕྱིར་དེ་ལྟར་དངོས་པོ་ཡོད་པར་ཁས་བླངས་ཀྱང་སྲིད་པ་ཡོད་པའི་ཕྱིར་རྟག་པ་དང་ཆད་པའི་སྐྱོན་དུ་ཐལ་བར་མི་འགྱུར་རོ། །

[Block 2303]
བཤད་པ། གལ་ཏེ་འབྲས་བུའི་འབྱུང་འཇིག་གི །

[Block 2304 [VERSE]]
རྒྱུན་དེ་སྲིད་པ་ཡིན་གྱུར་ན། །
འཇིག་ལ་ཡང་སྐྱེ་མེད་པའི་ཕྱིར། །
རྒྱུ་ནི་ཆད་པར་ཐལ་བར་འགྱུར། །

[Block 2305]
གལ་ཏེ་འབྲས་བུ་དང་རྒྱུའི་འབྱུང་བ་དང་འཇིག་པའི་རྒྱུན་གང་ཡིན་པ་དེ་སྲིད་པ་ཡིན་པར་གྱུར་ན། དེ་ལྟ་ན་ཡང་ཁྱོད་ལ་ཆད་པ་ཁོ་ནར་ཐལ་བར་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། འཇིག་པ་ལ་ཡང་སྐྱེ་བ་མེད་པའི་ཕྱིར་ཏེ། འདི་ལྟར་རྒྱུ་འགགས་པ་ལ་ཡང་སྐྱེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2306]
དེ་ལྟར་རྒྱུ་འགགས་པ་ལ་ཡང་སྐྱེ་བ་མེད་པའི་ཕྱིར། རྒྱུ་ཆད་པ་ཁོ་ནར་ཐལ་བར་འགྱུར་རོ། །

[Block 2307]
སྨྲས་པ། མི་འགྱུར་ཏེ་རྒྱུ་ལམ༌[^1524]འབྲས་བུ་གཞན་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2308]
འདི་ལྟར་རྒྱུ་ལས་འབྲས་བུ་གཞན་ཉིད་ཡིན་པར་མི་འཐད་དོ། །

[Block 2309]
ཁྱོད་ཀྱིས་ཀྱང་།

[Block 2310 [VERSE]]
གང་ལ༌[^1525]བརྟེན་ཏེ་གང་འབྱུང་བ། །
དེ་ནི་རེ་ཞིག་དེ་ཉིད་མིན། །
དེ་ལས་གཞན་པའང་མ་ཡིན་ཕྱིར། །
དེ་ཕྱིར་ཆད་མིན་རྟག་མ་ཡིན། །

[Block 2311]
ཞེས་སྨྲས་པས། དེས་ན་རྒྱུ་ལས་འབྲས་བུ་གཞན་ཉིད་མ་ཡིན་པའི་ཕྱིར་རྒྱུ་ཆད་པར་མི་འགྱུར་རོ། །

[Block 2312]
བཤད་པ། ཁོ་བོས་དེ་སྐད་སྨྲ༌[^1526]མོད་ཀྱི་ཁྱོད་ཀྱིས་དེའི་རྟེན༌[^1527]གྱི་དེ་ཁོ་ན་ཁོང་དུ་མ་ཆུད་དེ། འདི་ལྟར་གལ་ཏེ་དངོས་པོ་འགག་ཅིང་དངོས་པོ་ཉིད་སྐྱེ་བར་འགྱུར་ན། དེ་གཉིས་དེ་ཉིད་དམ་གཞན་ཉིད་དུ་ཇི་ལྟར་མི་འགྱུར། འདི་ལྟར་གལ་ཏེ་རེ་ཞིག་རྒྱུས་རྒྱུའི་གནས་སྐབས་སྤངས་ཏེ་འབྲས་བུའི་གནས་སྐབས་སུ་འཕོ་བར་གྱུར་ན་ནི། དེ་ལྟ་ན་དེ་ཉིད་རྒྱུ་ཡིན་ཏེ། དེའི་གནས་སྐབས་གཞན་དང་གཞན་དུ་གྱུར་པ་འབའ་ཞིག་ཏུ་ཟད་དོ། །

[Block 2313]
དཔེར་ན་བྲོ་གར་མཁན་གྱིས་ཆ་ལུགས་གཞན་སྤངས་ཏེ། ཆ་ལུགས་གཞན་ལེན་པར་བྱེད་པ་དེ་ལ་ཆ་ལུགས་ཐ་དད་པ་ཉིད་དུ་འགྱུར་བ་འབའ་ཞིག་ཏུ་ཟད་ཀྱི་བྲོ་གར་མཁན་ལ་ཐ་དད་པ་མེད་པ༌[^1528]དེ་ཆ་ལུགས་ཐ་དད་པར་གྱུར་ཀྱང་། དེ་ཉིད་བྲོ་གར་མཁན་ཡིན་པ་དེ་བཞིན་དུ། གནས་སྐབས་གཞན་དུ་འཕོས་སུ་ཟིན་ཀྱང་། དེ་ཉིད་རྒྱུ་ཡིན་ན་ཇི་ལྟར་དེ་ཉིད་ཡིན་པར་མི་འགྱུར། ཅི་སྟེ་ཡང་འདི་སྙམ་དུ་རྒྱུ་ནི་གནས་སྐབས་གཞན་དུ་མི་འཕོ་བར་རྒྱུ་འགག་པར་འགྱུར་ཏེ། རྒྱུ་འགགས་པ་ན་འབྲས་བུ་སྐྱེ་བར་འགྱུར་བར་སེམས་ན། དེ་ལྟ་ན་ཡང་གང་གི་ཚེ་གཞན་འགགས་པ་ལ་གཞན་སྐྱེས་པ་དེའི་ཚེ་ཇི་ལྟར་གཞན་ཉིད་དུ་མི་འགྱུར། ཁོ་བོ་ཅག་ལ་ནི་དངོས་པོ་ལ༌[^1529]བརྟེན་ནས་གདགས་པ་ངོ་བོ་ཉིད་སྟོང་པ་སྒྱུ་མ་དང་སྨིག་རྒྱུ་དང་གཟུགས་བརྙན་ལྟ་བུ་རྣམས་ལ་དངོས་པོ་དེ་གང་གིར་འགྱུར་ཏེ༌[^1530]དངོས་པོ་དེ་གང་ལས་གཞན་དུ་འགྱུར་ཏེ་དེ་ཉིད་དང་གཞན་ཉིད་དུ་འགྱུར་བ་མེད་དོ། །

[Block 2314]
དེ་ལྟ་བས་ན་དངོས་པོར་ལྟ་བ་ཡོད་ན་རྒྱུ་འགགས་པ་ཡང་སྐྱེ་བ་མེད་པའི་ཕྱིར་རྒྱུན་ཆད་པ་ཁོ་ནར་ཐལ་བར་འགྱུར་རོ། །

[Block 2315]
ཡང་གཞན་ཡང་།
--- END BLOCKS ---
