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

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

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
དམིགས་པ་དང་མི་དམིགས་པ་མཉམ་པ་ཉིད་ནི་མི་དམིགས་པ་སྟེ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་དམིགས་སུ་ཡོད་པ༌[^1654]དངོས་པོ༌[^1655]གང་ཡིན་པ་དང་། ཆོས་ཐམས་ཅད་དམིགས་སུ་མེད་པ་དངོས་པོ་མེད་པ་གང་ཡིན་པ་དེ་གཉི་ག་ཡང་མཚུངས་སོ། །

[Block 2347]
དེ་ཅིའི་ཕྱིར་ཞེ་ན། ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་ཏེ། དམིགས་སུ་ཡོད་པ་ནི་ཀུན་བརྟགས་པ་ཡིན་པས་ངོ་བོ་ཉིད་མེད་དོ། །

[Block 2348]
དམིགས་སུ་མེད་པ་ཡང་དངོས་པོ་མེད་པའི་བདག་ཉིད་ཡིན་པས་ངོ་བོ་ཉིད་མེད་དེ། དེ་བས་ན༌[^1656]གཉི་ག་ཡང་ངོ་བོ་ཉིད་མེད་པར་མཚུངས་ཏེ། དམིགས་སུ་ཡོད་པ་དང་། དམིགས་སུ་མེད་པ་དེ་གཉིས་ཀྱི༌[^1657]མཉམ་པ་ཉིད་ངོ་བོ་ཉིད་མེད་པ། གང་ཡིན་པ་དེ་ནི་དམིགས་སུ་མེད་པའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2349 [HEADING]]
##### ས་ནས་ས་ཡོངས་སུ་རྫོགས་པར་བྱ་བ། ^1-2-7-33-0

[Block 2350]
ཇི་ལྟར་ས་ནས་ས་ཡོངས་སུ་རྫོགས་པར་བགྱི། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཇི་ལྟར་ཐོབ་པར་བགྱི་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དམིགས་པ་ལ་ཆགས་པར་མ་གྱུར་ན། གོང་ནས་གོང་མའི་ས་དང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ལ་ཇི་ལྟར་བརྩོན་པར་བྱ་ཞེས་དགོངས་པའོ། །

[Block 2351]
རབ་འབྱོར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ༌[^1658]ཡང་དམིགས་སུ་མེད་ཅེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་བསྟན་ཏེ། དམིགས་པ་དང་བཅས་པའི་ངོ་བོ་ཉིད་ཀྱིས། ས་གོང་མའམ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་མི་འགྱུར་གྱི། ཇི་ལྟ་ཇི་ལྟར་དམིགས་སུ་མེད་པ་མཐུ་དང་ལྡན་པར་གྱུར་པ་དེ་ལྟ་དེ་ལྟར་ས་གཞན་ནས་གཞན་དུ་འཕར་བ་དང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་འགྱུར་ཏེ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། བྱང་ཆུབ་དང་། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་དམིགས་སུ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེས་སྟོན་ཏོ། །

[Block 2352 [HEADING]]
##### ཆོས་རྣམས་རབ་ཏུ་རྣམ་པར་དབྱེ་བ། ^1-2-7-34-0

[Block 2353]
ཆོས་ཐམས་ཅད་ངོ་བོ་ཉིད་དང་བྲལ་བ་ལ་ཇི་ལྟར་རབ་ཏུ་རྣམ་པར་དབྱེ་བར་བགྱི་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཆོས་ཐམས་ཅད་ངོ་བོ་ཉིད་དང་བལ་བ་ཡིན་ན། འདི་ནི་གཟུགས་སོ། །

[Block 2354]
འདི་ནི་ཚོར་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པར་རབ་ཏུ་རྣམ་པར་དབྱེ་བར༌[^1659]ཇི་ལྟར་བྱེད་ཅེས་བྱ་བའོ། །

[Block 2355]
རབ་འབྱོར་བྱང་ཆུབ་སེམས་དཔའ་ནི་ཇི་ལྟར་ན༌[^1660]བྱས་པས་གཟུགས་དམིགས་པར་འགྱུར་བ་དེ་ལྟར་ཆོས་རྣམས་རབ་ཏུ་རྣམ་པར་འབྱེད་པར་མི་བྱེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་བསྟན་ཏེ། བྱང་ཆུབ་སེམས་དཔས་ནི་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་མི་དམིགས་ཏེ། ཇི་ལྟ་ཇི་ལྟར་སྒྲུབ་པ་དེ་ལྟ་དེ་ལྟར་མི་དམིགས་སོ། །

[Block 2356]
དེ་བས་ན་དམིགས་སུ་མེད་པའི་དོན་ལ་རབ་ཏུ་འཇུག་གོ། །

[Block 2357]
[^1661]བཅོམ་ལྡན་འདས་གལ་ཏེ་གཟུགས་ཀྱང་མི་དམིགས་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་གསོལ་ཏེ། གལ་ཏེ་དམིགས་སུ་མེད་པའི་དོན་ལ་རབ་ཏུ་ཞུགས་པ་ཡིན་ན། ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པར་བྱ་བ་དང་། སྐྱོན་མེད་པར་འཇུག་པ་དང་། ཞིང་ཡོངས་སུ་དག་པར་བྱ་བ་དང་། སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱ་བ་དང་། མངོན་པར་བྱང་ཆུབ་པ་དང་། ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་དང་། སངས་རྒྱས་ཀྱི་མཛད་པ་དང་། སེམས་ཅན་རྣམ་པར་གྲོལ་བར་བྱ་བ་ལ་སོགས་པ་དམིགས་པའི་སྦྱོར་བ་རྣམས་ཇི་ལྟར་གྲུབ་པར་འགྱུར་ཞེས་ཞུས་པའོ། །

[Block 2358]
རབ་འབྱོར་བྱང་ཆུབ་སེམས་དཔའ་ནི་གཟུགས་ཀྱི་དོན་དུ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་མི་སྤྱོད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་བསྟན་ཏེ། བྱང་ཆུབ་སེམས་དཔས༌[^1662]ནི་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་ལ་མི་སྤྱོད་ཀྱི། ཆོས་ཐམས་ཅད་དམིགས་སུ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ༌[^1663]སྤྱོད་དོ་ཞེས་བྱ་བ་སྟེ། སྔར་བཤད་པའི་དམིགས་སུ་ཡོད་པ་ནི་ཀུན་རྫོབ་ཀྱི་ཐ་སྙད་ཡིན་གྱི། དོན་དམ་པར་ནི་མ་ཡིན་ནོ་ཞེས་བསྟན་པའོ། །

[Block 2359 [HEADING]]
##### ཐེག་པ་གསུམ་རྣམ་པར་དགོད་པ། ^1-2-7-35-0

[Block 2360]
མ་བྱས་པ༌[^1664]འགྱུར་བ་མེད་པ་ཞེས་བྱ་བའི་དོན་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 2361]
ཐེག་པ་གསུམ་པོ་དག་ཇི་ལྟར་རྣམ་པར་དགོད་པར་འགྱུར་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཆོས་ཐམས་ཅད་མ་བྱས་པ། འགྱུར་བ་མེད་པ་ཡིན་ན། ཐེག་པ་གསུམ་དུ་དབྱེ་བ་མེད་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2362]
རབ་འབྱོར་མ་བྱས་པ་དང་། འགྱུར་བ་མེད་པའི་ཆོས་རྣམས་ལ་ནི་རྣམ་པར་དགོད་པ་གང་ཡང་དམིགས་སུ་མེད་དེ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པའི་ཐེག་པ་རྣམ་པར་དགོད་པ་དག་དོན་དམ་པར་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་དགོངས་པའོ། །

[Block 2363]
འདིར་ཞུས་པ༌[^1665]དང་ལན་བཏབ་པ་དག་གོ་སླ་བས་རྣམ་པར་མ་བཀྲོལ༌[^1666]ལོ། །

[Block 2364]
ངས་ནི་འཇིག་རྟེན་གྱི་ཐ་སྙད་དུ་ཡང་དག་པ་མ་ཡིན་པ་ལས་འཛིན་པ་ལས་ཟློག་གི་དོན་དམ་པར་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དོན་དམ་པར་ཕུང་པོ་གསུམ་དུ་གཏོགས་པའི་སེམས་ཅན་གང་ཡང་དམིགས་སུ་མེད་ཀྱི། དེ་དག་ཡང་དག་པ༌[^1667]མ་ཡིན་པའི་ཆོས་རྣམས་ལ་ཡང་དག་པར་འཛིན་པ་ལས་འཇིག་རྟེན་གྱི་ཀུན་རྫོབ་ཏུ་སླར་ལྡོག་པར་ཟད་དེ། མིང་དེས་ཐ་སྙད་དུ་འདོགས་ཀྱི།[^1668] དོན་དམ་པར་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 2365 [HEADING]]
##### དེ་བཞིན་གཤེགས་པ་དོན་དམ་པ་ལ་བཞུགས་ཏེ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པ། ^1-2-7-36-0

[Block 2366]
བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་དོན་དམ་པ་ལ་བཞུགས་ཏེ། བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་སམ་ཞེས་ཞུས་པ་ལ། དོན་དམ་པར་གནས་མེད་པ་དང་། མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་བྱ་བ་མེད་པའི་ཕྱིར་རབ་འབྱོར་དེ་ནི་མ་ཡིན་ནོ་ཞེས་བསྩལ་བ༌[^1669]གསུངས་སོ། །

[Block 2367]
འོ་ན་རྫུ་འཕྲུལ་གྱི་རྣམ་གྲངས་ལ་བཞུགས་ཏེ་འམ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དོན་དམ་པ༌[^1670]ལ་མ་ཡིན་ན། འོ་ན་སྤྲུལ་པས་སམ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2368]
དེ་ཡང་ཤིན་ཏུ་མེད་པའི་ཕྱིར་ལན་གསུངས་ཏེ། བརྗོད་དུ་མེད་པའི་བདག་ཉིད་དང་། སོ་སོར༌[^1671]རང་གིས་རིག་པའི་རྣམ་པས་ཆོས་ཐམས་ཅད་རྟོགས་པ་ནི་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པའོ། །

[Block 2369]
འདིར་ཡང་ཅི་ཁྱོད་དོན་དམ་པ་ལ་ཞུགས༌[^1672]ཏེ་འམ་རྫུ་འཕྲུལ་གྱི་རྣམ་གྲངས་ལ་ཞུགས༌[^1673]ཏེ་འམ་ཞེས་ཅིའི་ཕྱིར་ཁྱོད་གནས་འདྲི་བར་བྱེད་ཅེས་དགོངས་པའོ། །

[Block 2370]
[^1674]དེ་ནི་འདུས་བྱས་ཀྱི་ཁམས་སམ༌[^1675]འདུས་མ་བྱས་ཀྱི་ཁམས་གང་ལ་ཡང་གནས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པས་བྱང་ཆུབ་ཀྱང༌[^1676]གང་ལ་ཡང་གནས་པ་མ་ཡིན་པར་བསྟན༌[^1677]ཏེ། དེ་བཞིན་གཤེགས་པས༌[^1678]སྤྲུལ་པའི་དཔེས་བསྟན་ཏོ། །

[Block 2371 [HEADING]]
##### དེ་བཞིན་གཤེགས་པ་དང་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་ལ་ཁྱད་པར་མེད་པ། ^1-2-7-37-0

[Block 2372]
རབ་འབྱོར་དེ་བཞིན་གཤེགས་པ་དང་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་ལ་ཁྱད་པར་མེད་དོ་ཞེས་བྱ་བ་དང་། དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་ལས་བྱེད་དོ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ན། གང་གི་ཚེ་བདག་ཅག་གི་བཅོམ་ལྡན་འདས་བྱམས་པ་ལ། ཁྱོད་ཀྱིས་ང་འདས་པའི་འོག་ཏུ་སངས་རྒྱས་ཀྱི་བྱ་བ་བྱས་ནས་སེམས་ཅན་རྣམས་ཀྱི་དོན་བྱོས་ཤིག་ཅེས་བྱ་བར་ལུང་བསྟན་དུ་འོས་པ་ལྟ་བུའི་བྱང་ཆུབ་སེམས་དཔའ་མ་གཟིགས་པ་དེའི་ཚེ། ཉིད་ཀྱི་སྐུ་དང་མཚུངས་པ་གཟུགས་ཕུན་སུམ་ཚོགས་པའི་སྤྲུལ་པ་སྤྲུལ་ནས་ཁྱོད་སངས་རྒྱས་ཀྱི་བྱ་བ་བྱོས་ཤིག་ཅེས་བཀའ་སྩལ་ཏེ། ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་དེའི་ཚེ། དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་དེ་འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་དུ་སངས་རྒྱས་ཀྱི༌[^1679]མཛད་པ་མཛད་དེ། སེམས་ཅན་རྣམས་ལ་ཕན་འདོགས་སོ། །

[Block 2373]
གང་གི་ཚེ་ལུང་བསྟན་དུ་འོས་པའི་བྱང་ཆུབ་སེམས་དཔའ་གཟིགས་པ་དེའི་ཚེ། སེམས་ཅན་རྣམས་དེའི་ལག་ཏུ་གཏད་ནས་ཉིད༌[^1680]ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་སྟོན་ཏེ། སྤྲུལ་པ་དེ་དང་། དེ་བཞིན་གཤེགས་པ་ལ༌[^1681]བྱེ་བྲག་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 2374]
ཆོས་ཉིད་དེ་ཉིད་ཀྱི༌[^1682]སྤྲུལ་པ་ཡང་ཞེས་བྱ་བ་ནི་གཉི་ག་ཡང་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པ་དང་། སེམས་ཅན་ལ་ཕན་པ་ཉིད་ཀྱི་ཕྱིར་བྱུང་བ་དང་། དེའི་མཛད་པ་མཛད་པའི་ཕྱིར་དེ་སྐད་དུ་བཤད་དོ། །

[Block 2375 [HEADING]]
##### མིང་དང་མཚན་མས་ཆོས་རྣམས་བསྟན་པ། ^1-2-7-38-0

[Block 2376]
དེའི་སླད་དུ༌[^1683]བཅོམ་ལྡན་འདས་ཀྱིས་ཆོས་རྣམས་ཀྱི་ཆོས་ཉིད་དཀྲུགས་པར་མ་གྱུར་ཏམ་ཞེས་བྱ་བ་ནི་མེད་པའི་ཆོས་རྣམས་ཡོད་པ་ཉིད་དུ་བཤད་པའི་ཕྱིར་རོ། །

[Block 2377]
རབ་འབྱོར་ངས་ནི་མིང་དང་མཚན་མས་ཆོས་རྣམས་བསྟན་ཏེ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་གྱི་ཐ་སྙད་དུ་བྱིས་པའི་ཡོངས་སུ་རྟོག་པ་ཞལ་གྱིས་བཞེས་ཀྱི་གཞན་དུ་སླ་བ༌[^1684]མ་ཡིན་པས་དེ་སྐད་བརྗོད་དོ། །

[Block 2378]
མིང་དང་མཚན་མ་ལ་མངོན་པར་ཞེན་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་པ་རྣམས་ལ། རྣམ་པ་གཞན་གྱིས་གོ་བར་བྱ་མི་ནུས་ཤིང་དཀའ་བའི་ཕྱིར་དེ་དང་མཐུན་པའི་ཀུན་རྫོབ་ཀྱི་ཐ་སྙད་དུ་བྱས་ཀྱི། མངོན་པར་ཞེན་པ་མེད་པས་ཉེས་པ་མེད་དོ། །

[Block 2379]
གལ་ཏེ་འདི་ནི་བདེན་པའོ་ཞེས་མངོན་པར་ཞེན་པ་དེའི་ཕྱིར་ཉེས་པར་འགྱུར་རོ་ཞེས་བསྟན་ཏོ། །

[Block 2380]
རབ་འབྱོར་རྣམ་པ༌[^1685]གལ་ཏེ་མིང་མིང་ལ་མངོན་པར་ཞེན་པར་འགྱུར་རམ། མཚན་མ་མཚན་མ་ལ་མངོན་པར་ཞེན་པར་འགྱུར་ན་ནི་ཞེས་བྱ་བ་ནི་གལ་ཏེ་མིང་མིང་ལ་མངོན་པར་ཞེན་པར་འགྱུར་རམ། མཚན་མ་མཚན་མ་ལ་མངོན་པར་ཞེན་པར་འགྱུར་ན། དེ་ལྟ་ན་ནི་སྟོང་པ་ཉིད་ཀྱང་སྟོང་པ་ཉིད་ལ་མངོན་པར་ཞེན་པར་འགྱུར་རོ། །

[Block 2381]
དེ་བཞིན་དུ་མཚན་མ་མེད་པ་ལ་སོགས་པ་ཡང་མངོན་པར་ཞེན་པར་འགྱུར་བ་ཞིག་ན། འདི་ལྟར་སྟོང་པ་ཉིད་ལ་སོགས་པ་ནི་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་མངོན་པར་ཞེན་པར་མི་འགྱུར་རོ། །

[Block 2382]
དེ་བཞིན་དུ་སངས་རྒྱས་དང་། ཉན་ཐོས་རྣམས་ཀྱང་མངོན་པར་ཞེན་པར་མི་འགྱུར་རོ་ཞེས་གསུངས་པའོ། །

[Block 2383]
རབ་འབྱོར་འདི་ལྟར་ཆོས་ཐམས་ཅད་མིང་དང་། མཚན་མ་ཙམ་དུ་ཟད་དོ༌[^1686]ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཆོས་ཐམས་ཅད་མིང་དང་། མཚན་མ་ཙམ་དུ་ཟད་ན། འཇིག་རྟེན་རྣམས་ཀྱིས་དེ་ལྟར་མི་ཤེས་ཏེ། དེ་བས་ན་དེ་དག་གིས་རྟོགས་པར་བྱ་བའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སྤྱོད་པར་འགྱུར་རོ། །

[Block 2384]
འདི་ལྟར་ཆོས་ཐམས་ཅད༌[^1687]མིང་དང་མཚན་མ་ཙམ་དུ་ཟད་དེ། དེའི་ཕྱིར་དེ་དག་རྟོགས་པས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་འགྱུར་རོ། །

[Block 2385]
གལ་ཏེ་ཆོས་འགའ་ཞིག་དངོས་པོ་ཡོད་ན། དེ་ལྟ་ན་ནི་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པར་མི་འགྱུར་རོ་ཞེས་བསྟན་པའོ། །
--- END BLOCKS ---
