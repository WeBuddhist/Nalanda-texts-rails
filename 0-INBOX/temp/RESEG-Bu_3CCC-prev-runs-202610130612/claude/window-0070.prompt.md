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
[Block 2451]
གང་གི་ཕྱིར་དེ་བཞིན་གཤེགས་པའི་ངོ་བོ་ཉིད་གང་ཡིན་པ་དེ་ནི་འགྲོ་བ་འདིའི་ངོ་བོ་ཉིད་ཀྱང་ཡིན་པ་དེའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་བརྟགས་པ་འདི་ཉིད་ཀྱིས་འགྲོ་བ་འདི་དག་ཀྱང་བརྟགས་པ་ཡིན་ནོ། །

[Block 2452]
སྨྲས་པ། དེ་བཞིན་གཤེགས་པའི་ངོ་བོ་ཉིད་གང་ཡིན། བཤད་པ།

[Block 2453]
དེ་བཞིན་གཤེགས་པ་དངོས་ཉིད་མེད། །འགྲོ་འདི་ངོ་བོ་ཉིད་མེད་དོ། །ཇི་ལྟར་ཞེ་ན། གང་གི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་ཕུང་པོ་རྣམས་ལ་བརྟེན་ནས་གདགས་པར་བྱ་བ་ཡིན་གྱི་རང་ལས་རབ་ཏུ་གྲུབ་པ་མེད་པ་དེའི་ཕྱིར་ངོ་བོ་ཉིད་མེད་དོ། །

[Block 2454]
འགྲོ་བ་འདི་དག་ཀྱང་དེ་དང་དེ་དག་ལ་བརྟེན༌[^1615]ནས་གདགས་པར་བྱ་བ་ཡིན་གྱི་འདི་དག་ལ་རང་ལས་རབ་ཏུ་གྲུབ་པ༌[^1616]ཅུང་ཟད་ཀྱང་མེད་པས་དེའི་ཕྱིར་འགྲོ་བ་ཡང་དེ་བཞིན་གཤེགས་པ་བཞིན་དུ་ངོ་བོ་ཉིད་མེད་དོ། །

[Block 2455]
ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་འདི་ལ་ཡང་།

[Block 2456 [VERSE]]
རྟག་དང་མི་རྟག་ལ་སོགས་བཞི། །
ཞི་བ་འདི་ལ་ག་ལ་ཡོད། །
མཐའ་དང་མཐའ་མེད་ལ་སོགས་བཞི། །
ཞི་བ་འདི་ལ་ག་ལ་ཡོད། །

[Block 2457]
ཅེས་བཤད་དོ། །

[Block 2458]
སྨྲས་པ། དེ་ལྟ་མ་ཡིན་ཏེ། འདུས་བྱས་ནི་གཅིག་ཏུ་མི་རྟག་པ་ཞེས་བརྗོད་ལ། དེ་བཞིན་གཤེགས་པ་ནི་མི་རྟག་པ་ཞེས་མི་བརྗོད་པས་དེ་ལ།

[Block 2459 [VERSE]]
དེ་བཞིན་གཤེགས་པའི་དངོས་ཉིད་གང་། །
དེ་ནི་འགྲོ་འདིའི་ངོ་བོ་ཉིད། །

[Block 2460]
ཅེས་བྱ་བར་ཇི་ལྟར་འཐད། བཤད་པ། དེ་ནི་འོག་ནས་ཀྱང་།

[Block 2461 [VERSE]]
སངས་རྒྱས་རྣམས་ཀྱིས༌[^1617]ཆོས་བསྟན་པ། །
བདེན་པ་གཉིས་ལ་ཡང་དག་བརྟེན། །
འཇིག་རྟེན་ཀུན་རྫོབ་བདེན་པ་དང་། །
དམ་པའི་དོན་གྱི༌[^1618]བདེན་པའོ། །

[Block 2462]
ཞེས་འབྱུང་བས་དེ་ལ་འཇིག་རྟེན་གྱི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་གང་གིས་བུམ་པ་ཡོད་དོ་སབ་མ་ཡོད་དོ་ཞེས་བརྗོད་པ་དེ་ཉིད་ཀྱིས་བུམ་པ་ཆག་གོ་སབ་མ་ཚིག་གོ་ཞེས་དེ་དག་མི་རྟག་པར་ཡང་བརྗོད་དོ། །

[Block 2463]
གང་གི་ཚེ་དེ་ཁོ་ན་སབ་མ་ཙམ་པ་དེའི་ཚེ་ནི་བུམ་པ་དང་སབ་མ་དག་བརྟེན་ནས་གདགས་པར་བྱ་བ་ཡིན་པས་མི་འཐད་ན་དེ་དག་ཆག་པ་དང་ཚིག་པ་ལྟ་འཐད་པར་ག་ལ་འགྱུར། གཞན་ཡང་དེ་བཞིན་གཤེགས་པ་ཡང་འཇིག་རྟེན་གྱི་ཀུན་རྫོབ་ཀྱི་དབང་གིས་དེ་བཞིན་གཤེགས་པ་བགྲེས་སོ། །

[Block 2464]
དེ་བཞིན་གཤེགས་པ་མྱ་ངན་ལས་འདས་སོ། །ཞེས་མི་རྟག་པར་ཡང་བརྗོད་དོ། །

[Block 2465]
གང་གི་ཚེ་དོན་དམ་པར་བསམ་པ་དེའི་ཚེ་ནི་དེ་བཞིན་གཤེགས་པ་ཉིད་མི་འཐད་ན་བགྲས་པ༌[^1619]དང་མྱ་ངན་ལས་འདས་པ་དག་ལྟ་འཐད་པར་ག་ལ་འགྱུར་ཏེ། དེའི་ཕྱིར་དེ་བཞིན་གཤེགས་པའི་ངོ་བོ་ཉིད་གང་ཡིན་པ་དེ་ནི་འགྲོ་བ་འདིའི་ངོ་བོ་ཉིད་ཀྱང་ཡིན་ནོ། །

[Block 2466]
དེ་ལྟ་བས་ན་སེམས་ཅན་གྱི་འཇིག་རྟེན་བརྟགས་པས་འདུ་བྱེད་ཀྱི་འཇིག་རྟེན་ཡང་བརྟགས་པར་གྲུབ་པོ། །དེ་བཞིན་གཤེགས་པ་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་ཉི་ཤུ་གཉིས་པའོ།། །།

[Block 2467 [HEADING]]
## ཕྱིན་ཅི་ལོག་བརྟག་པ། ^23-0

[Block 2468]
དབུ་མའི་རྩ་བའི་འགྲེལ་པ་བུད་དྷ་པཱ་ལི་ཏ། བམ་པོ་དགུ་པ། འདིར་སྨྲས་པ།

[Block 2469 [VERSE]]
འདོད་ཆགས་ཞེ་སྡང་གཏི་མུག་རྣམས། །
ཀུན་ཏུ་རྟོག་ལས་འབྱུང་བར་གསུངས། །
སྡུག་དང་མི་སྡུག་ཕྱིན་ཅི་ལོག །
བརྟེན་པ་འདི་ལས་ཀུན་ཏུ་འབྱུང་། །

[Block 2470]
འདི་ལ་འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་རྣམས་ནི་ཀུན་ཏུ་རྟོག་པ་ལས་འབྱུང་བར་མདོ་སྡེ་དག་ལས་རྒྱ་ཆེར་གསུངས་ཏེ། སྡུག་པ་དང་མི་སྡུག་པའི་ཕྱིན་ཅི་ལོག་ལ་བརྟེན་པ་ཉིད་ལས་ཀུན་ཏུ་འབྱུང་བས། དེའི་ཕྱིར་འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་རྣམས་ནི་ཡོད་པ་ཡིན་ནོ། །

[Block 2471]
འདིར་བཤད་པ།

[Block 2472 [VERSE]]
གང་དག་སྡུག་དང་མི་སྡུག་པའི། །
ཕྱིན་ཅི་ལོག་ལ་བརྟེན་འབྱུང་བ། །
དེ་དག་ངོ་བོ་ཉིད་ལས་མེད། །
དེ་ཕྱིར་ཉོན་མོངས་ཡང་དག་མེད། །

[Block 2473]
གང་དག་ད་ལྟར་སྡུག་པ་དང་མི་སྡུག་པའི་ཕྱིན་ཅི་ལོག་ལ་བརྟེན་ནས་ཀུན་ཏུ་རྟོག་པ་ལས་འབྱུང་བ་དེ་དག་ནི་ངོ་བོ་ཉིད་ལས་མེད་པས་དེའི་ཕྱིར་ཉོན་མོངས་པ་རྣམས་ཡང་དག་པར་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2474]
ཡང་གཞན་ཡང་།

[Block 2475 [VERSE]]
བདག་གི་ཡོད་ཉིད་མེད་ཉིད་ནི། །
ཇི་ལྟ་བུར་ཡང་འགྲུབ་པ་མེད། །
དེ་མེད་ཉོན་མོངས་རྣམས་ཀྱི་ནི། །
ཡོད་ཉིད་མེད་ཉིད་ཇི་ལྟར་འགྲུབ། །

[Block 2476]
བདག་གི་ཡོད་པ་ཉིད་དང་མེད་པ་ཉིད་ནི་རྣམ་པ་གང་གིས་ཀྱང་ཇི་ལྟ་བུར་ཡང་འགྲུབ་པ་མེད་དོ། །

[Block 2477]
བདག་དེ་མེད་ན་ཉོན་མོངས་པ་རྣམས་ཀྱི་ཡོད་པ་ཉིད་དང་མེད་པ་ཉིད་ཇི་ལྟར་འགྲུབ་པར་འགྱུར། ཅིའི་ཕྱིར་ཞེ་ན།

[Block 2478 [VERSE]]
ཉོན་མོངས་དེ་དག་གང་གི་ཡིན། །
དེ་ཡང་འགྲུབ་པ་ཡོད་མ་ཡིན། །

[Block 2479]
ཉོན་མོངས་པ་དེ་དག་ནི་འགའ་ཞིག་གི་ཡིན་ཏེ་ཉོན་མོངས་པ་དེ་དག་གང་གི་ཡིན་པ་དེ་ཡང་རྣམ་པ་ཐམས་ཅད་དུ་འགྲུབ་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2480]
གལ་ཏེ་གང་མེད་ཅི་ཞིག་ཡོད། །ཉོན་མོངས་ཅུང་ཟད་ཡོད་མ་ཡིན། གལ་ཏེ་ཉོན་མོངས་པ་དེ་དག་གང་གི་ཡིན་པ་དེ་ཡང་འགྲུབ་པ་ཡོད་པ་མ་ཡིན་ན། གང་མེད་ན་ཅི་ཞིག་ཡོད་དེ་ཉོན་མོངས་པ་ཅུང་ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2481]
ཅི་སྟེ་གང་ཡང་མེད་པར་ཉོན་མོངས་པ་རྣམས་ཡོད་དེ་དེ་རྣམས་ནི་སུའི་ཡང་མ་ཡིན་ནོ་སྙམ་ན་དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 2482 [VERSE]]
རང་ལུས་ལྟ་བཞིན་ཉོན་མོངས་རྣམས། །
ཉོན་མོངས་ཅན་ལ་རྣམ་ལྔར་མེད། །
རང་ལུས་ལྟ་བཞིན་ཉོན་མོངས་ཅན། །
ཉོན་མོངས་པ་ལ་རྣམ་ལྔར་མེད། །

[Block 2483]
ཇི་ལྟར་རང་གི་ལུས་ལ་ལྟ་བ་ཕུང་པོ་ལྔ་པོ་དག་ལ་རྣམ་པ་ལྔར་ཡོད་པ་མ་ཡིན་པ་དེ་བཞིན་དུ་ཉོན་མོངས་པ་རྣམས་ཀྱང་ཉོན་མོངས་པ་ཅན་གྱི་སེམས་ལ་རྣམ་པ་ལྔར་ཡོད་པ་མ་ཡིན། ཇི་ལྟར་རང་གི་ལུས་ལ་ལྟ་བ་ཕུང་པོ་ལྔ་པོ་དག་རྣམ་པ་ལྔར་ཡོད་པ་མ་ཡིན་པ་དེ་བཞིན་དུ་ཉོན་མོངས་པ་ཅན་གྱི་སེམས་ཀྱང་ཉོན་མོངས་པ་རྣམས་ལ་རྣམ་པ་ལྔར་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2484]
ཡང་གཞན་ཡང་།

[Block 2485 [VERSE]]
སྡུག་དང་མི་སྡུག་ཕྱིན་ཅི་ལོག །
ངོ་བོ་ཉིད་ལས་ཡོད་མིན་པ། །
སྡུག་དང་མི་སྡུག་ཕྱིན་ཅི་ལོག །
བརྟེན༌[^1620]ནས་ཉོན་མོངས་གང་དག་ཡིན། །

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
--- END BLOCKS ---
