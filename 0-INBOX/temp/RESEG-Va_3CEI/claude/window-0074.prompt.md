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
[Block 2591]
མདོ་ལས་ཁྱོད་ཉོན་ཅིག་འདི་ནི་ཁོ་བོའི་སྙིང་གི་བུ་ཁོ་བོས་བསྐྱེད་པ༌[^2203]སྟེ་ཞེས་པ་ནི་སྔོན་གྱི་རྒྱལ་བུ་བཅུ་དྲུག་གི་ཚེ་ན་ངའི་བསྟན་པ་འདི་ལ་སེམས་བསྐྱེད་དེ་དགེ་བའི་རྩ་བ་བཙུགས་པས་ངའི་གསུང་ལས་སྐྱེས་པ༌[^2204]ངའི་ཆོས་ཀྱིས་བསྐྱེད་པ་ཡིན་པས་ཡང་དག་པའི་སྲས་ཞེས་བྱའོ། །

[Block 2592]
མདོ་ལས་གྲོང༌[^2205]ཁྱེར་གྱི་མིང་འདི་འཁྱམས་ནས༌[^2206]ལོ་ལྔ་བཅུ་ལོན་ཏེ་ཞེས་པ་ནི་འཁོར་བར་འཁོར་བ་བསྟན་ཏེ། གྲོང་ཁྱེར་ཞེས་པ་ནི་ཐེག་པ་ཆེན་པོའོ། །

[Block 2593]
ཐེག་པ་ཆེན་པོར་རིགས་ངེས་པ་དང་། དབང་པོ་རྣོན་པོ་རྣམས་ནི་ལན་ཅིག་སེམས་བསྐྱེད་པས་ཕྱིར༌[^2207]ལྡོག་པར་ཡང་མི་འགྱུར་ན། དབང་པོ་ཞན་པ་དང་། རིགས་མ་ངེས་པ་རྣམས་ལྡོག་ཅིང་ལྟུང་བར༌[^2208]འགྱུར་བ༌[^2209]ཡོད་དོ་བར་བསྟན་ཏོ། །

[Block 2594]
མདོ་ལས་འདིའི་མིང་ནི་འདི་ཞེས་བྱ་ཞེས་པ་ནས་དེ་ཀུན་ཀྱང་འདི་ཉིད་ཤེས་སོ་ཞེས་པའི་བར་དུ་ནི་སྔོན་ཡང་དེ་བཞིན་གཤེགས་པ་ངའི་བསྟན་པ་ལ་ཞུགས་པ༌[^2210]ལས་རབ་ཏུ༌[^2211]འཁྱམས་པ་དང་། དེ༌[^2212]ཡང་ཐེག་པ་ཆེན་པོ་ལ་ཞུགས་ཞེས་པའི་དོན་ཏེ།[^2213] ཇི་ལྟར་འཕགས་པ་ཤཱ་རིའི་བུ་བསྐལ་པ༌[^2214]དྲུག་ཅུའི་བར་དུ་ཐེག་པ་ཆུང་ངུ་སྤྱོད་སྤྱོད་པ་ལས་ད་ཐེག་པ་ཆེན་པོ་ལ་ཞུགས་པ་ཉིད་གྲོང་ཁྱེར་དེ་ན་གནས་པ་ཞེས་བྱའོ། །

[Block 2595]
ཚོལ༌[^2215]ཞེས་པ་ནི་ཐུགས་རྗེས་དགོངས་པའི་དོན་ཏོ། །

[Block 2596]
བྱང་ཆུབ་དང་མྱ་ངན་ལས་འདས་པའི་ནོར་ཐམས་ཅད་ནི་འདི་ལ་གཏད་པ་དང་།[^2216] བདག་གི་དོན་དུ་འགྱུར་བ་དང་། གཞན་ལ་ཕན་འདོགས་པའི་ཡོན་ཏན་ཐམས་ཅད་འདི་ལ་གཏད་དོ་ཞེས་པའོ། །

[Block 2597]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་མང་པོ་རྙེད་སྙམ་སེམས་སོ་ཞེས་པའི་བར་དུ་ནི་བུས་ཐོབ་པ་རྣམས༌[^2217]བསྟན་ཏེ། སངས་རྒྱས་ཀྱི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པར་རེ་བ་མེད་པ་ལས་རྙེད་ཅེས་པའི་དོན་ཏོ། །

[Block 2598 [HEADING]]
###### གཉི་ག་བསྡུས་ཏེ་གླེང་བ། ^4-4-2-1-3-0

[Block 2599]
མདོ་ལས་དེ་བཞིན་དུ་བཅོམ་ལྡན་འདས་བདག་ཅག་ནི་ཞེས་པ་ནས་ཇི་ལྟ་བ་བཞིན་ནོ་ཞེས་པའི་བར་དུ་ནི་མ་རབས་ཀྱིས་ནས་སེམས་བསྐྱེད༌[^2218]པ་ཙམ་ལ་གནས་པའི༌[^2219]ཕྱིར་སྲས་དང་འདྲ་ཞེས་སྨྲས་སོ། །

[Block 2600]
དམ་པའི་ཆོས་འདི་ཐོས་ཤིང་དབང་པོ་སྨིན་པར་གྱུར་པས། སྲས་ཡང་དག་ཅེས་པའི་དོན་ཏོ། །

[Block 2601]
མདོ་ལས་བཅོམ་ལྡན་འདས་བདག་ནི་སྡུག་བསྔལ་གསུམ་གྱིས་གཟིར་ཏོ་ཞེས་པ་ནས་སྡུག་བསྔལ་ལོ་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆེན་པོ་ལས་ལྡོག་པས་འཁོར་བའི་རྒྱུ་བསྟན་པའོ། །

[Block 2602]
སྡུག་བསྔལ་བའི་ཡང་སྡུག་བསྔལ་ནི་གནས་དང་། མཚན་ཉིད་དང་། སྤྱོད་ཡུལ་དང་། དབང་པོ་དང་ལྡན་པའི་ཆོས་ཐམས་ཅད་སྡུག་བསྔལ་ཏེ། ཕུང་པོ་ལྔའི་ཕྱོགས་གཅིག་ནི་སྡུག་བསྔལ་བའི་ཡང་སྡུག་བསྔལ་བ་སྟེ། ཡིད་དང་འགལ་བ་མི་མཐུན་པ་མྱོང་བ་ནི་སྡུག་བསྔལ་བའོ། །

[Block 2603]
སྡུག་བསྔལ་བརྒྱད་ལ་ལྔ་ནི་སྡུག་བསྔལ༌[^2220]བའོ། །

[Block 2604]
བདེ་བར་འཚོ་བའི༌[^2221]བདག་ཉིད་བདེ་བར་འཚོ་བའི༌[^2222]རྗེས་སུ་འབྲང་བ་ཡུལ་ལམ་དབང་པོའམ་ལྡན་པའི་ཆོས་རྣམས་འགྱུར་བས་སྡུག་བསྔལ་བསྐྱེད་པ༌[^2223]སྟེ། །ཕུང་པོ་ལྔའི་ཆ་གཅིག་ནི་འགྱུར་བའི་སྡུག་བསྔལ་ཏེ། སྡུག་བསྔལ་བརྒྱད་ལས་མཛའ་བ་དང་བྲལ་བ་དང་། འདོད་པ་མི་རྙེད་པའི་སྡུག་བསྔལ་ནི་འགྱུར་བའི་སྡུག་བསྔལ་ལོ། །

[Block 2605]
བཏང་སྙོམས་ཀྱི་ཚོར་བའི་རང་བཞིན་དང་། དེའི་རྗེས་སུ་འཇུག་པ་ཡུལ་དང་དབང་པོ་དང་ལྡན་པའི་ཆོས་རྣམས་མི་རྟག་པར་གནས་པའི་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་ཏེ། ཟག་པ་དང་བཅས་པའི་ཕུང་པོ་ལ༌[^2224]ཐམས་ཅད་ནི་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་བས་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་རྣམས་ཀྱང་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་ལོ་ཞེས་གསུངས་སོ། །

[Block 2606]
མདོ་ལས་འཁོར་བ་ན་ཆུང་ངུ་ལ་དད་པས་བདག་ཅག་བཅོམ་ལྡན་འདས་ཀྱིས་ཆོས་ངན་པ་མང་པོ་ཕྱག་དར་གྱི་ཕུང་པོ་དང་འདྲ་བའི་སེམས་སུ་བཅུག་སྟེ་ཞེས་པ་ནི་ཆུང་ངུ་ལ་ཕྱོགས་ཤིང་ཆེན་པོ་བསྒྲུབ་པར་མི་ནུས་པའོ། །

[Block 2607]
མདོ་ལས་དེ་རྣམས་ལ་ཞེས་པ་ནས་འཚོ་ཞིང་གསོལ་ཏེ་ཞེས་པའི་བར་དུ་སེམས་སུ་བཅུག་ཅེས་པ་ནི་བསྒོམ་པ་ལ་སེམས་པའོ། །

[Block 2608]
ཕྱག་དར་གྱི་ཕུང་པོ་ཞེས་པ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པའོ། །

[Block 2609]
རྩོལ་བ་ནི་བརྩོན་འགྲུས་ཀྱི་སེམས་ཀྱིས་གཅིག་ཏུ་འབད་པས་གཟོད༌[^2225]མྱ་ངན་ལས་འདས་པ་ཐོབ་ཅེས་པའི་དོན་ཏོ། །

[Block 2610]
ཉིན་གཅིག་གིས་སླ༌[^2226]ཞེས་པ་ནི་མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་ནི་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱིས༌[^2227]ཐོབ་པ་ཡིན་ན། བསྐལ་པ་དྲུག་ཅུས་བསྒྲུབས་པའི་རྣམ་པར་གྲོལ་བ་ནི་ཉི་མ་གཅིག་གིས་སླ༌[^2228]ཙམ་མོ་ཡང༌[^2229]ཡང་མྱ་ངན་ལས་འདས་པ་ལས་ཉོན་མོངས་པའི་སྒྲིབ་པ་སྤངས་ཤིང་ཡེ་ཤེས་ཆེན་པོ་ཐོབ་པ་མ་ཡིན་ཞེས་པའི་དོན་ཏོ། །

[Block 2611 [HEADING]]
###### **ཆོས་ཆུང་ངུ་ལ་དགའ་བའི་ཕྱིར་མ་བཤད་པས་རེ་བ་མེད་པ།** ^4-4-2-1-3-1-0

[Block 2612]
མདོ་ལས་བཅོམ་ལྡན་འདས་བདག་ཅག་མྱ་ངན་ལས་འདས་པ༌[^2230]དེ་སྙེད༌[^2231]ཅེས་པ་འདིས༌[^2232]མ་བསྟན་ཏེ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཐེག་པ་ཆེན་པོ་རེ་བའི་སེམས་མེད་པ་རྣམ་གསུམ་སྟེ། སྔར་ཉན་ཐོས་པ་ཆོས་ཆུང་ངུ་ལ་དགའ་བའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་མ་བཤད་པས་རེ་བ་མེད་པ་དང་། ཉན་ཐོས་པའི་མྱ་ངན་ལས་འདའ་བ༌[^2233]ཐོབ་པ་ཉིད་ཀྱིས་ཆོག་པར་སེམས་པའི་ཕྱིར་རེ་བ་མེད་པ་དང་། ཐེག་པ་ཆེན་པོ་བྱང་ཆུབ་སེམས་དཔའི་ཆེད་དུ་བཤད་ཀྱི་ཉན་ཐོས་པ་བདག་ཅག་གི་ཆེད་དུ་མ་བཤད་དོ་ཞེས་རེ་བ་མེད་པ་དང༌[^2234]གསུམ་ལས༌[^2235]འདི་ནི་དང་པོའོ། །

[Block 2613]
བགས༌[^2236]ཀྱིས་བཞག་སྟེ་ཞེས་པ་ནི་ཆུང་ངུ་ལ་མོས་པའི་སེམས་མ་སྤངས་ཤིང་དབང་པོ་མ་སྨིན་པའི་ཕྱིར་རེ་ཞིག་བཞག་ཅེས་པའི་དོན་ཏོ། །

[Block 2614 [HEADING]]
###### **ཉན་ཐོས་ཀྱི་མྱ་ངན་ལས་འདའ་བ་ཐོབ་པར་རེ་བ་མེད་པ།** ^4-4-2-1-3-2-0

[Block 2615]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཐབས་མཁས་པ་ཞེས་པ་ནས་བདག་ཅག་གིས༌[^2237]མང་དུ་བྱས་པར་ཤེས་སོ་ཞེས་པའི་བར་དུ་ནི་ཉན་ཐོས་ཀྱི་མྱ་ངན་ལས་འདའ་བ་ཐོབ་པར་རེ་བ་མེད་པ་བསྟན་ཏེ་ཐབས་མཁས་པས་ཡེ་ཤེས་ཀྱི་མཛོད༌[^2238]ཀྱི་ཉེ་མཚམས་སུ་བཀོད་པ་ནི་དང་པོ་དྲང་བའི་དོན་གྱིས་བསྟན་ནས་ཡང་དག་པའི་ཡེ་ཤེས་མཐོང་བ་དང་ཉེ་བར་བཞག་ཅེས་པའི་དོན་ཏོ། །

[Block 2616 [HEADING]]
###### **ཉན་ཐོས་ཀྱི་ཆེད་དུ་མ་བཤད་པས་རེ་བ་མེད་པ།** ^4-4-2-1-3-3-0

[Block 2617]
མདོ་ལས་བཅོམ་ལྡན་འདས་དེ་བདག་ཅག་གིས་ཞེས་པ་ནས། དེ་མི་འདོད་དོ་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆེན་པོ་བྱང་ཆུབ་སེམས་དཔའི་ཆེད་དུ་བསྟན་གྱི་ཉན་ཐོས་ཀྱི་ཆེད་དུ་མ་བཤད་པས་རེ་བ་མེད་པ༌[^2239]བསྟན་ཏེ། བྱང་ཆུབ་སེམས་དཔའི་ཆེད་དུ་བཅོམ་ལྡན་འདས་ཀྱི་བྱིན་གྱི་རླབས་ཀྱིས༌[^2240]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བཤད་པ་ཡང་ཉན་ཐོས་པའི་ཆེད་དུ༌[^2241]མ་ཡིན་པས་མི་འདོད་དོ་ཞེས་པའི་དོན་ཏོ། །

[Block 2618]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་པ༌[^2242]ནས་སྲས་ཡང་དག་པ་ཞེས་གསུངས་པའི་བར་དུ་ནི་སྔོན་ཉན་ཐོས་པའི་རྣམས་ལ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གསལ་བ་ཉིད་དུ་མ་བསྟན་མོད་ཀྱི་དེ་བཞིན་གཤེགས་པའི་རང་བཞིན་དང་རིགས་ཡོད་པས་སྔོན་ཡང་ཐབས་ཀྱིས་བསྟན་ཏོ་ཞེས་པའོ། །

[Block 2619]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཀྱི༌[^2243]ཞེས་པ་ནས་དེ་བཞིན་གཤེགས་པའི་སྲས་འདི་དག་བཞིན་ནོ་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པའི་སྲས་སུ་གྱུར་ཏེ། དེ་བཞིན་གཤེགས་པའི་སྲས་ཉིད་ཐོབ་ཅེས་པ་བསྟན་ཏོ། །

[Block 2620]
དེ་ཡང་བཅོམ་ལྡན་འདས་ཆོས་འཆད་པ་མི་མཛད་པ་དང་། མྱ་ངན་ལས་འདས་པ༌[^2244]ཉིད་ཐེག་པ་ཆེན་པོས་ཐོབ་པར་བསྟན་པ་ཡང་དེ་དག་གི་དོན་བསྡུ་བའོ། །

[Block 2621]
དེ་ལ་འདི་ནི་དང་པོ་དང་སྦྱར་རོ། །

[Block 2622]
རྒྱ་ཆེན་པོས་བྱང་ཆུབ༌[^2245]འཛུད་པ་ནི་གཉིས་པ་དང་སྦྱར་རོ། །

[Block 2623]
ཐམས་ཅད་མཁྱེན་པའི་རིན་པོ་ཆེ་ཐོབ་སྟེ། དེ་བཞིན་གཤེགས་པའི་སྲས་འདི་དག་བཞིན་ནོ་ཞེས་པ་ནི་གསུམ་པ༌[^2246]དང་སྦྱར་རོ། །

[Block 2624]
དེ་བཞིན་གཤེགས་པའི་སྲས་འདི་དག་བཞིན་ནོ་ཞེས་པ་ཡང་ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་ཐེག་པ་གཅིག་གི༌[^2247]རྒྱུས་འབྲས་བུ་ཆེན་པོ་ཐོབ་པ་བཞིན་འཕགས་པ་ཉན་ཐོས་པ་རྣམས་ཀྱང་དེ་བཞིན་དུ་འགྱུར་ཞེས་པའི་དོན་ཏོ།། །།

[Block 2625]
དམ་པའི་ཆོས་པུཎྜ་རཱི་ཀའི་འགྲེལ་པ། བམ་པོ་བདུན་པ།

[Block 2626 [HEADING]]
##### ཚིགས་སུ་བཅད་པས་གསོལ་བ། ^4-4-2-2-0

[Block 2627]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་འོད་སྲུངས་ཆེན་པོས་དེའི་ཚེ་ཚིགས་སུ་བཅད་པ་འདི་དག་གསོལ་ཏོ་ཞེས་འཕགས་པ་ཉན་ཐོས་ཆེན་པོ་བཞིས་དོན་འདི་ཆུད་པ་དང་། དྲིས་པར་འདྲ་ན་འདིར་འོད་སྲུངས་གཅིག་པུ་སྨོས་པ་དེ་ཅིའི་ཕྱིར་ཞེ་ན། འོད་སྲུངས་སྐུ་བགྲེས་པའི་ཕྱིར་གཙོར་སྨོས་པས་སོ། །

[Block 2628]
འདི་མན་ཆད་ཚིགས་བཅད་བརྒྱད་ཅུ་རྩ་དྲུག་ཅིག་ཡོད་པ་ལ། བདུན་ཅུ་རྩ་གསུམ་གྱིས་ནི་བཅོམ་ལྡན་འདས་ཀྱི་བཀའ་དྲིན་ཆེན་པོ་ལ་སོགས་པ་བསྟན། ཚིགས་བཅད་བཅུ་གསུམ་གྱིས་ནི་བཅོམ་ལྡན་འདས་ཀྱི་བཀའ༌[^2248]དྲིན་ཟབ་པ་བསྟན་ཏོ། །

[Block 2629 [HEADING]]
###### བཅོམ་ལྡན་འདས་ཀྱི་བཀའ་དྲིན་ཆེན་པོ། ^4-4-2-2-1-0

[Block 2630]
དུམ་བུ་དང་པོ་ལ་ཡང་གསུམ་དུ་དབྱེ་སྟེ།
--- END BLOCKS ---
