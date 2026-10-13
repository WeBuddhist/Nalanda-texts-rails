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
[Block 2346]
དེ་ནས་བདེ་བ་ཆེན་པོ་ལ་ཐེ་ཚོམ་དྲི་བའི་ཕྱིར། རྡོ་རྗེ་སྙིང་པོས་གསོལ་པ། རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་ནི་དབང་ལས་ཐོབ་ཅིང་དཀྱིལ་འཁོར་དུ་གནས་པའི་བདེ་ཆེན་ནོ། །

[Block 2347]
སཏྭ་སུ་ཁ་སྟེ་དམ་པའམ་དེའི་བདེ་བ་ནི་རྫོགས་རིམ་གྱི་བདེ་ཆེན་ནོ། །

[Block 2348]
དེ་ནས་བསྐྱེད་པ་ཡིས༌[^1011]ནི་ཅི་ཞིག་འཚལ་དུ་འབྲེལ་ཅིའི་ཕྱིར་ཞེ་ན།

[Block 2349 [VERSE]]
རྫོགས་པ་བསྒོམ་པ་མེད་པའི་ཕྱིར་རོ། །
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ནི་ལན་དུའོ། །

[Block 2350]
ཨེ་མ་ནི་ཨ་ཧོ་སྟེ་དེ་ལྟར་ཡིན་ནའང་ངོ་མཚར་བའོ། །

[Block 2351]
བྱང་ཆུབ་སེམས་དཔའི་ཆེ་བ་ནི་གུས་པའི་ཚུལ་དུ་བོད་པའོ། །

[Block 2352 [VERSE]]
འདི་ནི་ཞེས་པ་ནི་འདི་ལ་སྟེ་རྫོགས་རིམ་ལའོ། །
དད་པའི་ཤུགས་ཀྱིས༌[^1012]ཉམས་པ་ནི༌[^1013]རྫོགས་རིམ་ཉིད་ཉམས་པའོ། །

[Block 2353]
ཅིའི་ཕྱིར་ཞེ་ན་ལུས་ཀྱི་དངོས་མེད་ནི་བསྐྱེད་རིམ་གྱིས་རྣམ་པ༌[^1014]གསལ་བ་དང་བཅས་པའི་ལུས་སོ། །

[Block 2354]
གང་ལས་བདེ་ནི་ལྔ་པ་ཡིན་ཡང་བདུན་པའི་དོན་ཏེ། དེ་ནས༌[^1015]རྟེན་མེད་པའི་ཕྱིར་བརྟེན་པའི་བདེ་བ་སྨྲ་བར་མི་ནུས་པའོ། །

[Block 2355]
ཁྱབ་བྱ་ཁྱབ་བྱེད་ཚུལ་ནི་ཕན་ཚུན་དུའོ། །

[Block 2356]
བདེ་བས་འགྲོ་བ་ཁྱབ་པ་ནི་གསུམ་དང་གཉིས་པ་ཡིན༌[^1016]པས་འགྲོ་བ་ཡང་བདེ་བ་ཁྱབ་པ་ཉིད་དོ། །

[Block 2357]
ཇི་ལྟར་ནི་དཔེའོ། །

[Block 2358]
མེ་ཏོག་ནི་རྟེན་ནོ། །

[Block 2359]
དྲི་ནི་བརྟེན་པའོ། །

[Block 2360 [VERSE]]
མེ་ཏོག་དངོས་མེད་ནི་བརྟེན་པའི་ཕྱིར་རོ། །
ཤེས་མི་འགྱུར་ནི་བརྟེན་པ་འདྲི་མི་ཤེས་པའོ། །

[Block 2361]
དེ་བཞིན་ནི་དཔེ་ལས་འབྱུང་བའོ། །

[Block 2362 [VERSE]]
གཟུགས་ལ་སོགས་པ༌[^1017]དངོས་མེད་ནི་རྟེན་མེད༌[^1018]པའི་ཕྱིར་རོ། །
བདེ་བ་ཉིད་ཀྱང་མི་དམིགས་པ་ནི་རྟེན་དམིགས་ཞེས༌[^1019]པའོ། །

[Block 2363]
རྫོགས་རིམ་ལ་རྟེན་མེད་པ་ནི་ཐབས་ལ༌[^1020]བདེ་བ་མི་འབྱུང་བ་བསྟན་ནས་མི་རྟོག་པར་མི་འབྱུང་བར་བསྟན་པའི་ཕྱིར། དངོས་པོ་ནི་སྐྱེ་བའམ་ཆགས་པའོ། །

[Block 2364 [VERSE]]
ད་ནི་བདག་ཏུ་མི་དམིགས་པའམ་མི་རྟོག་པའོ། །
དངོས་པོ་མེད་པ་བསྡུ་བའམ་ཐིམ་པའོ། །

[Block 2365]
ད་ནི་ཡང་མི་རྟོག་པའོ། །ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་རྟོགས་པའི༌[^1021]ཕྱིར་རོ་ཞེས་བྱ་བ་བདེ་བ་དེ་དག་ནི་རྨི་ལམ་ལྟར་རྟོགས་པའི༌[^1022]ཕྱིར་བུདྡྷ་རྟོགས་པ་འམ་སངས་རྒྱས་ཡིན༌[^1023]ལ། ད་སྟེ་མི་རྟོག་པ༌[^1024]རྟོགས་པའོ། །

[Block 2366]
དེ་བཞིན་དུ་དངོས་པོ་མེད་པར་ཡང་ལྷག་མ་སྟེ་ཁོད་ནས་དྲང་ངོ་། །དེས་ནི་འདི་སྐད༌[^1025]འཆད་པར་འགྱུར་ཏེ། བསྐྱེད་རིམ་དངོས་པོ་ལ་དངོས་པོ་མེད་པ་བརྟེན་པའི༌[^1026]བདེ་བ་མི་འབྱུང་ལ། དེ་ལྷན་ཅིག་ཚོལ་བའི༌[^1027]མི་རྟོག་པ་དང་རྟོག་པ་གསལ་བ་ཡང་མི་འབྱུང་བའོ། །

[Block 2367]
དེའི་ཕྱིར་གང་ཞིག་དམ་པ་སུ་ཞིག་གོ། །

[Block 2368]
ལེ་ལོས༌[^1028]བསྣུན་པའམ་བཅོས་མ་ནི་རྟེན་གྱི་ཆོས་ལ་དགའ་བ་སེམས་པའོ། །

[Block 2369]
རྨོངས་པ་ནི་རྟེན་པའི༌[^1029]ཆོས་སུམ་ཤེས་པའོ། །

[Block 2370]
ད་མི་ཤེས་པ་ནི་རྟོག་པ་མེད་པས་སངས་རྒྱས་མ་ཡིན་པའོ། །

[Block 2371]
དེ་ཡང་སྐྱེད་པ༌[^1030]ལྷའི་རྣམ་པས་ཆོག་པས་ལུས་ཅི་དགོས་ཤེ་ན། དེའི་ཕྱིར་གཉུག་མའི་ལུས་བསྟན་པ་ནི། བཙུན་མོ་བྷ་ག་བདེ་ཆེན་དུ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ་དེ་ཡང་བཤད་ཚུལ་སོ་སོར་སྦྱར་ཏེ། སྔོན་དུ་འགྲོ་བའི་ཆོ་ག་རྣམས་སྔ་མ་བཞིན་བྱས་ལ། ཨེའི་རྣམ་པའི་ཆ་བྱད་ཅེས་བྱ་བ་ནི་ཆོས་ཀྱི་འབྱུང་གནས་གཞལ་ཡས་ཁང་གི་རྣམ་པ་དང་བཅས་པར་བསྒོམ། སངས་རྒྱས་རིན་ཆེན་ཟ་མ་ཏོག་ནི་རྒྱུའི་རྡོ་རྗེ་འཆང་བ༌[^1031]དང་། འབྲས་བུའི་ཧེ་རུ་ཀར་གྱུར་པ་དང་། འཁོར་བསྐྱེད་པ་དང་སེམས་དཔའ་སུམ་བརྩེགས་བསྒོམ་པ་སྟེ། ཟ་མ་ཏོག་ཅེས་བྱ་སྟེ་རྟེན་དང་བརྟེན་པའི་དཀྱིལ་འཁོར་རོ། །

[Block 2372]
བདེ་བ་ཅན་དུ་གནས་སམ་བཞུགས། །ཞེས་པ་ནི་ཡེ་ཤེས་ཀྱི་འཁོར་ལོ་དགུག་པ་ནས་བཟླས་པའི་མཐར་ཐུག་པའི་བར་དུ་བསྐྱེད་པའི་རིམ་པ་ལྟར་སྦྱར་རོ། །

[Block 2373]
ཡང་རྡོ་རྗེ་བཙུན་མོ་ནི་གཟུགས་དང་ལང་ཚོ་ལ་སོགས་པ་དང་ལྡན་པའོ། །

[Block 2374]
བྷ་ག་ནི་བྱ་རོག་གི་གདོང་ཅན་ཏེ་ཡེ་ཤེས་ཀྱི༌[^1032]སྐལ་བ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2375]
ཨེའི་རྣམ་པའི་ཆ་བྱད་གཟུགས་ནི་གསང་བའི་གནས་ཀྱི་སྤྱིའོ། །

[Block 2376]
སངས་རྒྱས་རིན་ཆེན་ཟ་མ་ཏོག་ནི་དེ་དང་འབྲེལ་བའི་ཐབས་ཀྱི་གནས་སོ། །

[Block 2377]
བདེ་བ་ཅན་ནི༌[^1033]ཞུ་བ་དེའོ། །

[Block 2378 [VERSE]]
རྟག་ཏུ་གནས་བཞུགས་ནི་གནས་གཉིས་དང་འབྲེལ་ལོ། །
དེ་དག་གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པའོ། །
ཡང་རྡོ་རྗེ་བཙུན་མོ་ནི་རྡོ་རྗེ་ལུས་ཀྱི་རྩའོ། །

[Block 2379 [VERSE]]
བྷ་ག་ནི་ཡེ་ཤེས་སོ། །
ཨེའི་རྣམ་པ་ནི་སྐྱེ་གནས་སོ། །
སངས་རྒྱས་རིན་ཆེན་ནི་བདེ་ཆེན་ནོ། །

[Block 2380]
ཟ་མ་ཏོག་ནི་སྣོད་ཡིན་པས་ཟ་མ་ཏོག་དང་འདྲའོ། །

[Block 2381]
བདེ་བ་ཅན་ནི་ཞུ་བ་དེའོ། །

[Block 2382 [VERSE]]
རྟག་ཏུ་ཞུགས༌[^1034]སམ་གནས་པ་ནི་བྱོན་ཏེ་གནས་པའོ། །
དེ་ནི་རང་ལུས་ཐབས་ལ་བརྟེན་པའོ། །

[Block 2383]
ཡང་རྡོ་རྗེ་བཙུན་མོ་ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པའོ། །

[Block 2384]
བྷ་གར་ནི་གནས་བཟང་པོ་དེར་འཇུག་པ་དང་ལྡོག་པའོ། །

[Block 2385 [VERSE]]
ཨེའི་རྣམ་པ་ནི་སའི་དཀྱིལ་དུ་ཟུག་པའོ། །
སངས་རྒྱས་རིན་ཆེན་ནི་ནམ་མཁའི་དཀྱིལ་དུ་ཟུག་པའོ། །
--- END BLOCKS ---
