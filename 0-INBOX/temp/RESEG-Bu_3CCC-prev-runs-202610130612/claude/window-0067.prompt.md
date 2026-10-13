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
སྨྲས་པ། སྲིད་པའི་རྒྱུན་ནི་ཡོད་པ་ཁོ་ན་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2347]
དེ་བཞིན་གཤེགས་པ་ནི་བཅོམ་ལྡན་འདས་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཡོད་དོ། །

[Block 2348]
དེས་བསྐལ་པ་གྲངས་མེད་པ་དག་གིས་བྱང་ཆུབ་ཡང་དག་པར་བསྒྲུབས༌[^1549]ཏེ། དེ་ལྟར་ཡང་མདོ་སྡེ་གཞན་དག་ལས་དེའི་ཚེ་དེའི་དུས་ན་ང་བྲམ་ཟེའི་ཁྱེའུ་མིག་བཟང་ཞེས་བྱ་བར་གྱུར་ཏོ། །

[Block 2349]
དེའི་ཚེ་དེའི་དུས་ན་ང་རྒྱལ་པོ་ང་ལས༌[^1550]ནུ་ཞེས་བྱ་བར་གྱུར་ཏོ་ཞེས་གསུངས་ཏེ། སྲིད་པའི་རྒྱུན་མེད་ན་དེ་མི་འཐད་པས་དེའི་ཕྱིར་སྲིད་པའི་རྒྱུན་ནི་ཡོད་པ་ཁོ་ནའོ། །

[Block 2350]
བཤད་པ། གལ་ཏེ་དེ་བཞིན་གཤེགས་པ་ཉིད་འཐད་ན་ནི། སྲིད་པའི་རྒྱུན་ཡང་ཡོད་པར་འགྱུར་གྲང་ན། དེ་བཞིན་གཤེགས་པ་ཉིད་མི་འཐད་པས་དེའི་སྲིད་པའི་རྒྱུན་ཡོད་པར་ག་ལ་འགྱུར། ཇི་ལྟར་ཞེ་ན། འདི་ལ་གལ་ཏེ་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་བ་འགའ་ཞིག་ཡོད་པར་གྱུར་ན། དེ་ཕུང་པོ་རྣམས་ཉིད་དམ། ཕུང་པོ་རྣམས་ལས་གཞན་ཞིག་ཡིན་གྲང་ན། དེ་ལ།

[Block 2351 [VERSE]]
སྐུ་མིན་སྐུ་ལས་གཞན་མ་ཡིན། །
དེ་ལ་སྐུ་མེད་དེ་དེར་མེད། །
དེ་བཞིན་གཤེགས་པ་སྐུ་ལྡན་མིན། །
དེ་བཞིན་གཤེགས་པ་གང་ཞིག་ཡིན། །

[Block 2352]
རེ་ཞིག་ཕུང་པོ་རྣམས་ཉིད་དེ་བཞིན་གཤེགས་པ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། ཕུང་པོ་རྣམས་འབྱུང་བ་དང་འཇིག་པའི་ཆོས་ཅན་ཡིན་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་མི་རྟག་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་དང་། ཉེ་བར་ལེན་པ་པོ་དང་། ཉེ་བར་ལེན་པ་དག་གཅིག་པ་ཉིད་དུ་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 2353]
ཕུང་པོ་རྣམས་ལས་དེ་བཞིན་གཤེགས་པ་གཞན་པ་ཕུང་པོ་མེད་པའི་ཆོས་ལོགས་ཤིག་ན་ཡང་མེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། ཕུང་པོ་མི་རྟག་པ་རྣམས་ལས་ཆོས་མི་མཐུན་པའི་ཕྱིར་རྟག་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་དང་། གཞན་ཉིད་ཡིན་ན་གཟུང༌[^1551]དུ་ཡོད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་ཏེ། གཟུང་དུ་ཡང་མེད་པས་དེའི་ཕྱིར་ཕུང་པོ་རྣམས་ལས་དེ་བཞིན་གཤེགས་པ་གཞན་ཡང་མ་ཡིན་ནོ། །

[Block 2354]
དེ་བཞིན་གཤེགས་པ་ལ་ཕུང་པོ་རྣམས་གངས་ལ༌[^1552]ཤིང་ལྗོན་པའི་ནགས་ཚལ་བཞིན་དུ་མེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། རྟེན་དང་བརྟེན་པ་གཞན་མ་ཡིན་པའི་ཕྱིར་མི་རྟག་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2355]
ཕུང་པོ་རྣམས་ལ་ཡང་དེ་བཞིན་གཤེགས་པ་ཤིང་ལྗོན་པའི་ནགས་ཚལ་ན་སེང་གེ་བཞིན་དུ་མེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། སྐྱོན་བསྟན་མ་ཐག་པ་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2356]
དེ་བཞིན་གཤེགས་པ་ཕུང་པོ་རྣམས་དང་ཤིང་ལྗོན་པའི༌[^1553]སྙིང་པོ་དང་ལྡན་པ་བཞིན་དུ་ལྡན་པ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། ཕུང་པོ་རྣམས་ལས་གཞན་མ་ཡིན་པའི་ཕྱིར་མི་རྟག་པ་ཉིད་ཀྱི་སྐྱོན་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2357]
དེ་ལྟར་རྣམ་པ་ལྔས་བཙལ་ན་དེ་བཞིན་གཤེགས་པ་ཉེ་བར་ལེན་པ་ལ་མི་སྲིད་ན། ཁྱོད་ཀྱིས་གང་གིས་སྲིད་པའི་རྒྱུན་ཡོད་པར་ཡོངས་སུ་བརྟགས༌[^1554]པའི་དེ་བཞིན་གཤེགས་པ་དེ་གང་ཞིག་ཡིན་པ་སྨྲོས་ཤིག །

[Block 2358]
སྨྲས་པ། ཅི་ཁོ་བོ་ཕུང་པོ་རྣམས་ཉིད་དེ་བཞིན་གཤེགས་པའམ། ཕུང་པོ་རྣམས་ལས་དེ་བཞིན་གཤེགས་པ་གཞན་ནོ་ཞེས་སྨྲའམ། ཅིའི་ཕྱིར་ཁྱོད་ཁོ་བོ་ལ་རྟག་པའམ་མི་རྟག་པར་ཐལ་བར་འགྱུར་བའི་སྐྱོན་འདོགས་པར་བྱེད། ཁོ་བོ་ནི་ཕུང་པོ་རྣམས་ལ་བརྟེན་ནས་དེ་བཞིན་གཤེགས་པ་གདགས་པར་བྱ་བ་ཡིན་པར་སྨྲ་བས། བརྟེན་ནས་གདགས་པར་བྱ་བ་ནི། །ཉེ་བར་ལེན་པ་ལས་དེ་ཉིད་དམ་གཞན་ཉིད་དུ་མི་སྨྲའོ། །

[Block 2359]
དེའི་ཕྱིར་དེ་ཉིད་དུ་བརྗོད་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་མི་རྟག་པ་ཉིད་ཀྱི་སྐྱོན་དུ་མི་འགྱུར་ལ་གཞན་ཉིད་དུ་བརྗོད་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རྟག་པ་ཉིད་ཀྱི་སྐྱོན་དུ་མི་འགྱུར་རོ། །

[Block 2360]
བཤད་པ། ཅི་ཁྱོད་ལེགས་པར་སྦྱར་བའི་ཕྱེད་ཀྱིས་གར་བྱེད་དམ། ཁྱོད་བརྟེན་ནས་དེ་བཞིན་གཤེགས་པ་གདགས་པར་ཡང་སྨྲ་ལ། དེ་བཞིན་གཤེགས་པ་ངོ་བོ་ཉིད་ལས་ཡང་འགྲུབ་པར་ཡང་འདོད་ཀོ། །འོ་ན།

[Block 2361 [VERSE]]
གལ་ཏེ་སངས་རྒྱས་ཕུང་པོ་ལ། །
བརྟེན་ནས་ངོ་བོ་ཉིད་ལས་མེད། །

[Block 2362]
གལ་ཏེ་སངས་རྒྱས་ཕུང་པོ་རྣམས་ལ་བརྟེན་ནས་གདགས་པར་བྱ་བ་ཡིན་ན། དེའི་དོན་ནི་སངས་རྒྱས་ངོ་བོ་ཉིད་ལས་མེད་པ་མ་ཡིན་ནམ།

[Block 2363]
འདི་ལྟར་ངོ་བོ་ཉིད་ལས་ཡོད་པ་ལ་ནི་ཡང༌[^1555]བརྟེན་ནས་གདགས་པས་ཅི་བྱ་སྟེ། དེའི་ངོ་བོ་ཉིད་གང་ཁོ་ན་ཡིན་པ་དེ་ཁོ་ནས་གདགས་པར་བྱ་བར་འགྱུར་རོ། །

[Block 2364]
གང་གི་ཕྱིར་དེ་ངོ་བོ་ཉིད་མེད་པ་དེའི་ཕྱིར་ཉེ་བར་ལེན་པས་གང༌[^1556]གདགས་པར་བྱ་བ༌[^1557]སྟེ། དེ་ལྟ་བས་ན་དེ་བཞིན་གཤེགས་པ་ངོ་བོ་ཉིད་ལས་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2365 [VERSE]]
ངོ་བོ་ཉིད་ལས་གང་མེད་པ། །
དེ་གཞན་དངོས་ལས་ག་ལ་ཡོད། །

[Block 2366]
དེ་བཞིན་གཤེགས་པ་གང་ངོ་བོ་ཉིད་ལས་མེད་པ་དེ་དག་གཞན་གང་ལས་ཡོད་པར་སེམས་ན། [^1558]སྨྲས་པ། གཞན་གྱི་དངོས་པོ་ལས་ཏེ། དེ་བཞིན་གཤེགས་པ་ནི་ཉེ་བར་ལེན་པ་གཞན་དུ་གྱུར༌[^1559]ལ་བརྟེན་ནས་གདགས་པར་བྱ་བ་ཡིན་པས་དེའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་གཞན་གྱི་དངོས་པོ་ལས་ཡོད་དོ། །

[Block 2367]
བཤད་པ།

[Block 2368 [VERSE]]
གང་ཞིག་གཞན་གྱི་དངོས་བརྟེན་ནས། །
དེ་དག་ཉིད་དུ་མི་འཐད་དོ། །

[Block 2369]
གང་ཞིག་གཞན་གྱི་དངོས་པོ་ལ་བརྟེན་ནས་གདགས་པར་བྱ་བ༌[^1560]དེ་ནི་བདག་ཉིད་ཡོད་དོ་ཞེས་བརྗོད་པར་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན།

[Block 2370 [VERSE]]
རང་ལས་མ་གྲུབ་པའི་ཕྱིར་རོ། །
གང་ཞིག་བདག་ཉིད་མེད་པ་དེ། །
ཇི་ལྟར་དེ་བཞིན་གཤེགས་པར་འགྱུར། །

[Block 2371]
དེ་བཞིན་གཤེགས་པ་གང་ཞིག་རང་གི་བདག་ཉིད་མེད་པ་དེ་ཉིད་ཉེ་བར་ལེན་པ་གཞན་དུ་གྱུར་པས་གདགས་པར་བྱ་ན་ཇི་ལྟར་དེ་བཞིན་གཤེགས་པར་འགྱུར། གལ་ཏེ་དེ་རང་གི་བདག་ཉིད་མེད་པར་ཉེ་བར་ལེན་པ་ལ་བརྟེན་ནས་བདག་ཉིད་ཡོད་པར་འགྱུར་ན་ནི། དེ་ལྟ་ན་ཉེ་བར་ལེན་པ་ལ་བརྟེན་ཏེ་སྐྱེས་པར་འགྱུར་བས་དེ་ཡང་མི་འདོད་དེ། མི་རྟག་པ་ཉིད་ལ་སོགས་པའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2372]
ཡང་གཞན་ཡང་།

[Block 2373 [VERSE]]
གལ་ཏེ་ངོ་བོ་ཉིད་མེད་ན། །
གཞན་དངོས་ཡོད་པར་ཇི་ལྟར་འགྱུར། །
ངོ་བོ་ཉིད་དང་གཞན་དངོས་དག །
མ་གཏོགས་དེ་བཞིན་གཤེགས་དེ་གང་། །

[Block 2374]
གལ་ཏེ་དེ་བཞིན་གཤེགས་པ་ངོ་བོ་ཉིད་མེད་དེ། ངོ་བོ་ཉིད་ཡོད་པ་མ་ཡིན་ན། གཞན་གྱི༌[^1561]དངོས་པོ་ཡོད་པར་ག་ལ་འགྱུར། འདི་ལྟར་གང་ངོ་བོ་ཉིད་ལས་གཞན་ཡིན་པ་དེ་གཞན་གྱི་དངོས་པོ་ཞེས་བྱ་ན། ངོ་བོ་ཉིད་མེད་པ་དེ་གང་ལས་གཞན་གྱི་དངོས་པོར་འགྱུར། དེ་ལྟ་བས་ན་གཞན་གྱི༌[^1562]དངོས་པོ་ཡང་ཡོད་པ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 2375]
འོ་ན༌[^1563]ངོ་བོ་ཉིད་དང་གཞན་གྱི་དངོས་པོ་དག་མ་གཏོགས་པར་དེ་བཞིན་གཤེགས་པ་དེ་གང༌[^1564]ཡིན་པ་དང་གང་གིས་གདགས་པར་བྱ་བ་དེ་སྨྲོས་ཤིག །

[Block 2376]
སྨྲས་པ། ཁྱོད་བརྟེན་ནས་གདགས་པར་བྱ་བའི་དོན་རྣམ་པར་མི་ཤེས་པར་མི་རིགས་པ་མང་པོ་དེ་སྙེད་ཅིག་སྨྲ་སྟེ། གཞན་གྱི་ཚིག་ལ་ཅོ་འདྲི་བ་ཙམ་གྱིས་ནི་དེ་ཁོ་ནའི་དོན་ཡོངས་སུ་ཤེས་པར་མི་ནུས་སོ། །

[Block 2377]
དེ་བཞིན་གཤེགས་པ་རྣམས་ལ་བརྟེན་ནས་གདགས་པར་བྱ་བ་གང་ཡིན་པ་དེ་ལ་ཅི་དེ་བཞིན་གཤེགས་པ་ངོ་བོ་ཉིད་ལས་ཡོད་དམ་འོན་ཏེ་གཞན་གྱི༌[^1565]དངོས་པོ་ལས་ཡོད་ཅེས་བྱ་བའི་ཚིག་དེའི་གླན་ཀར་མི་འགྱུར་རོ། །

[Block 2378]
བཤད་པ། འཇིག་རྟེན་ན།

[Block 2379]
འདྲེ་ཡིས་བྱ་བ་གང་ཡིན་པ། །དེ་ནི་བྱིས་པ་དག་བྱེད་དོ། །ཞེས་བརྗོད་པ་དེ་ནི་བདེན་པ་ཁོ་ན་སྟེ།[^1566] ཁོ་བོ་ནི་བརྟེན་ནས་གདགས་པར་བྱ་བའི་དོན་རྣམ་པར་མི་ཤེས་པ་ཡིན་ལ། ཁྱོད་ནི་མ་ཡིན་པ་ལྟ་ཞིག །ཁྱོད་ཀྱིས་གང་དག་ལ་དེ་བཞིན་གཤེགས་པ་ཡོད་པ་ཉིད་དུ་ཡོངས་སུ་བརྟགས༌[^1567]པའི་ཕུང་པོ་རྣམས་ནི་ཉེ་བར་ལེན་པ་ཉིད་དུ་མི་འཐད་དོ། །

[Block 2380]
དེ་ཇི་ལྟར་ཞེ་ན།

[Block 2381 [VERSE]]
གལ་ཏེ་ཕུང་པོ་མ་བརྟེན་པར། །
དེ་བཞིན་གཤེགས་པ་འགའ་ཡོད་ན། །
དེ་ནི་ད་གདོད་རྟེན༌[^1568]འགྱུར་ཞིང་། །
བརྟེན་ནས་དེ་ལས་འགྱུར་ལ་རག །

[Block 2382]
གལ་ཏེ་ཕུང་པོ་རྣམས་ཉེ་བར་ལེན་པ་པོའི༌[^1569]སྔ་རོལ་ན། དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་བ་འགའ་ཞིག་ཡོད་ཅིང་། དེ་ཕུང་པོ་རྣམས་ཉེ་བར་ལེན་པར་འགྱུར་ན་ནི། དེ་ལྟ་ན་ནི་དེ་བཞིན་གཤེགས་པ་བརྟེན་ནས་ཡོད་པར་འགྱུར་ལ་རག་གོ། །

[Block 2383]
དེ་ཡང་སྐྱེས་པར་གྱུར་ལ་ཕུང་པོ་རྣམས་ཀྱིས་དེ་གསལ་བ་ཙམ་ཞིག་བྱེད་པར་འགྱུར་དུ་ནི།

[Block 2384 [VERSE]]
ཕུང་པོ་རྣམས་ལ་མ་བརྟེན་པར། །
དེ་བཞིན་གཤེགས་པ་འགའ་ཡང་མེད། །
གང་ཞིག་མ་བརྟེན་ཡོད་མིན་པ། །
དེས༌[^1570]ནི་ཇི་ལྟར་ཉེར་ལེན་འགྱུར། །

[Block 2385]
ཕུང་པོ་རྣམས་ལ་མ་བརྟེན་པར་དེ་བཞིན་གཤེགས་པ་འགའ་ཡང་མི་འཐད་དེ། གང་ཕུང་པོ་རྣམས་ལ་མ་བརྟེན་པར་མེད་ན། མེད་པ་དེས་ཇི་ལྟར་ཕུང་པོ་རྣམས་ཉེ་བར་ལེན་པར་འགྱུར།
--- END BLOCKS ---
