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
རང་གི་སེམས་བརྟན་པ་ནི་ཡིད་མི་གཡོ་བར་རོ། །

[Block 2277]
རྡོ་རྗེ་སྙིང་པོས་གསོལ་ཞེས་པ་ནི་གཞན་ལ་ཇི་ལྟར་རིགས་པའོ། །

[Block 2278]
བདག་མེད་རྣལ་འབྱོར་ནི་བདག་མེད་པར་བསྒོམས་པར༌[^990]ལྡན་པའི་བུད་མེད་དོ། །

[Block 2279]
ཕྱག་རྒྱ་ཉིད་ཅེས་ཇི་ལྟར་ཞེས་པ༌[^991]ནི་སྤོང་བ་སྟེ། རང་ཉིད་ཕྱག་རྒྱ་ཡིན་ན། དེའི་རྒྱུ་མཚན་བསྟན་པའི་ཕྱིར་ཕྱག་རྒྱ་ནི་རང་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2280]
ཕྱག་རྒྱ་གཉིས་ནི་ཡང་ཕྱག་རྒྱ་ལ་བརྟེན་པའི་དངོས་གྲུབ་ཇི་ལྟར་འགྱུར་ཞེས་པ་ནི་ཐབས་ལ་མ་བརྟེན་པས་སྤོང་བའི་སྒྲའོ། །

[Block 2281]
ཕྱག་རྒྱ་ཞེས་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོའི༌[^992]སྟེ་དབྱེར་མེད་དོ། །

[Block 2282]
བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ་ནི་དེའི་ཡན་ལག་གོ། །

[Block 2283]
བུད་མེད་གཟུགས་ནི་སྤང་ཞེས་པ་ནི་ཕྱག་རྒྱའི་རྟེན་རྣམ་པར་བསྒྱུར་བ་སྟེ་བསྟན་པའོ། །

[Block 2284 [VERSE]]
དེ་བཤད་པ་སྟེ་ནུ་མ་སྤང་བར་འབྲེལ་ལོ། །
བོ་ལར་བསྒྱུར་ཏེ་ཇི་ལྟར་ཞེ་ན།
ཀཀྐོ་ལ་དབུས་གནས་ནི་དབུས་ནས་སྐྱེས་པའོ། །

[Block 2285]
འགྲམ་གཉིས་ནི་མཁུར་བའོ། །

[Block 2286]
དྲིལ་བུ་ནི་འབྲས་བུའོ། །

[Block 2287]
ཟེའུ་འབྲུ་ནི་ཀོན་ཏའོ། །

[Block 2288 [VERSE]]
བོ་ལ་ནི་རིན་པོ་ཆེའི་ཕོ་བྲང་ངོ་། །
དེ་ནས་སྐྱེས་བུ་ཉིད་དུ་འབྲེལ་ལོ། །

[Block 2289]
ཇི་ལྟར་ཞེ་ན་འབད་པ་མེད་པར་སྐྱེས་བུར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། གསལ་བར་ནུས་པའི་ཕྱིར་རོ། །

[Block 2290]
འདི་ལས་སྐྱེས་བུར་འགྱུར་བ་དེ་ལས་སོ། །

[Block 2291]
ཕྱག་རྒྱའི་དངོས་གྲུབ་ཕྱག་རྒྱ་ཆེན་པོ་སྒྲུབ་པར་བྱེད་ནུས་པ་ཁོ་ནའོ། །

[Block 2292]
ཡང་སྤངས་གཞན་ཞེས་པ་ནི་བདག་གཟུགས་བསྒྱུར་ཏེ་གཞན་ཞེས་པ་ནི་ཀཀྐོ་ལ་ལས་གཞན་པའོ། །

[Block 2293]
བཅོམ་ལྡན་འདས་ཀྱི་གཟུགས་ནི་ཧེ་རུ་ཀའོ། །

[Block 2294]
བསྟན་པ་དེ་བཤད་པའི་ཕྱིར་ལྷག་མ་ཞེས་པ་སྟེ་བོ་ལླ༌[^993]ལས་གཞན་པའི་སྐུའོ། །

[Block 2295]
བདག་ཉིད་ཆེན་པོ༌[^994]སྒེག་པ་ལ་སོགས་པའི་ཉམས་སོ། །

[Block 2296]
དགའ་ཆེན་ཧེ་རུ་ཀའི་གཟུགས་ནི་ཐབས་བདེ་བ་དང་ལྡན་པའོ། །

[Block 2297 [VERSE]]
ཧེ་རུ་ཀ་སྦྱོར་ནི་སྐུ་གསུང་ཐུགས་སུའོ། །
དེ་ནས་གསལ་བར་ནུས་པའི་རྣལ་འབྱོར་དུ་འབྲེལ་ལོ། །
ཤིན་ཏུ་གོམས་པ་ལས་བྱུང་བའི་ཕྱིར་རོ། །
འདི་ལས་ནི་ཧེ་རུ་ཀར་བསྒྱུར་བ་དེ་ལས་སོ། །

[Block 2298]
ཕྱག་རྒྱའི་དངོས་གྲུབ་ནི་ཕྱག་རྒྱ་ཆེན་པོར༌[^995]བསྒྱུར་ནུས་པ་ཁོ་ནའོ། །

[Block 2299]
ད་ནི་སྐྱེ་བ༌[^996]དག་པར་བསྟན་པའི་ཕྱིར། སྐྱེ་དང་འཇིག་པ་ནི་ཚོགས་གཉིས་སམ། ཨཱ་ལི་ཀཱ་ལི་ལས་སམ།[^997] ཟླ་བ་ཉི་མའམ། བྱང་ཆུབ་པར་བསྐྱེད་པའམ། རྗེས་སུ་ཆགས་པར་ཞུ་བ་ལ་སོགས་པའོ། །

[Block 2300]
ཐབས་དང་ཤེས་རབ་མི་འཆིང་མི་གནོད་ཅེས་པ་ནི་དེ་རྣམས་ཐབས་དང་ཤེས་རབ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2301]
བསྟན་པ་དེ་བཤད་པའི་ཕྱིར་ཐབས་ནི་འབྱུང་བ་ཞེས་བྱ་བ་ནི་སྐྱེ་བ་སྟེ། བསོད་ནམས་ཀྱི་ཚོགས་དང་། ཀཱ་ལི་དང་། ཉི་མ་དང་། བྱང་ཆུབ་པ་ལྔས་བསྐྱེད་པ་ལ་སོགས་པའོ། །

[Block 2302]
དེའི་ཕྱིར་དེ་རྣམས་ནི་ཐབས་ཡིན་པས་མྱ་ངན་ལས་འདས་པ་མཐར་ཕྱིན་པ་ནི་ལྷག་མའོ། །

[Block 2303]
ཡང་འཇིག་པ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་དང་ཨཱ་ལི་ཀཱ་ལི་དང་ཟླ་བ་དང་རྗེས་སུ་ཆགས་པས་ཞུ་བ་ལ་སོགས་པ་ཀུན་ནས་གང་ཡང་རུང་བའོ། །ཤེས་རབ་ནི་འདི་རྣམས་ཀྱི་རང་བཞིན་ཡིན་པས་སྲིད་པ་མཐར་བྱེད་པའོ། །

[Block 2304]
དེ་དག་བསྡུས་པའི་ཕྱིར།

[Block 2305 [VERSE]]
དེ་ནས་ཞེས་པ་ནི་ཤེས་རབ་ཡིན་པས་ནའོ། །
འདི་ལ་ནི་ཡེ་ཤེས་ལ་སོགས་པས་ནའོ། །

[Block 2306]
དེ་ཉིད་ལས་ནི་ཞེས་པ་ནི་བསོད་ནམས་ཚོགས་ལ་སོགས་པའོ། །

[Block 2307 [VERSE]]
དེས་ན་ཞེས་པ་ལྷག་མ་སྟེ་ཐབས་ཡིན་པས་སོ། །
གང་ལའམ་ལ་ལ་ནི་ཐ་མལ་པའི་ཚེ་ནའོ། །

[Block 2308]
འཇིག་པས་འཇིག་པའམ་ཟད་པར་འགྱུར་ཞེས་པ་ནི་ཞིག་ནས་མེད་པར་རོ། །

[Block 2309]
འཇིག་པའི་དངོས་པོ་ནི་གདོད་མ་ནས་ཤེས་རབ་ཡིན་པས་འཇིག་པའི་རྒྱུ་མེད་པའོ། །

[Block 2310]
ཟག་པ་མེད་པ༌[^998]ནི་ཞིག་ནས་ཟད་པ་ཡིན་པས་སོ། །

[Block 2311]
དེ་བཞིན་དུ་ཡང་ཐབས་སྐྱེ་བ་ལ་ཡང་ལྷག་མ་ཁོང་ནས་ཕྱུང་སྟེ་ཤེས་པར་བྱ་སྟེ། ལ་ལ་སྐྱེ་བ་སྐྱེ་བར་འགྱུར། །ཞེས་འབྱུང་སྟེ།

[Block 2312 [VERSE]]
[^999]ཉོན་མོངས་པའི་སྐྱེ་བ་ཡིན་པས་སོ། །
སྐྱེ་བའི་དངོས་མེད་ཟད་པར་འགྱུར། །

[Block 2313]
ཞེས་པ་ཐབས་དང་ཤེས་རབ་ཀྱིས་སྐྱེ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2314]
དེ་དག་གིས་ནི་བསྐྱེད་པའི་རིམ་པ་ཐབས་ཀྱི་ཆོ་ག་དག་པར་བྱས་ནས། བསྐྱེད་པ་ལྷའི་མཚན་མ་དག་པའི་ཕྱིར་བསྐྱེད་པའི་རིམ་པ་ནི་རྣལ་འབྱོར་འདིས༌[^1000]ལས་དང་པོ་ནས་བཟུང༌[^1001]བའོ། །

[Block 2315 [VERSE]]
བརྟུལ་ཞུགས་ཅན་ནི་བསྐྱེད་རིམ་མཐར་ཕྱིན༌[^1002]པའི་བར་གྱིས་སོ། །
སྤྲོས་པ་ནི་ཁ་དོག་དང་མཚན་མ་ལ་སོགས་པའོ། །
--- END BLOCKS ---
