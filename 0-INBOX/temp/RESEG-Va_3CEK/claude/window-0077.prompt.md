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
[Block 2696]
འོན་ཏེ་ཐམས་ཅད་བདག་མེད་པའི་རྣམ་པར་མཐོང་ངོ་ཞེས་ཟེར་ན་ནི། འོ་ན་ནི་བདེན་པ་རྣམས་ལ་སྡུག་བསྔལ་ལ་སོགས་པར་མཐོང་བར་མི་འགྱུར་བས་དེ་ལྟ་བས༌[^1858]ན། འཕགས་པ་ཉན་ཐོས་སྡུག་བསྔལ་ལ་སྡུག་བསྔལ་དུ་ཡིད་ལ་བྱེད་པའམ། ཀུན་འབྱུང་ལ་ཀུན་འབྱུང་དུ་ཡིད་ལ་བྱེད་པའམ། ལམ་ལ་ལམ་གྱི་བར་དུ་ཡིད་ལ་བྱེད་པའི༌[^1859]ཟག་པ་མེད་པའི་ཡིད་ལ་བྱེད་པ་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་རྣམས་རྣམ་པར་འབྱེད་པ་གང་ཡིན་པ་ཞེས་གསུངས་པའི་མདོ་དང་འགལ་ལོ། །

[Block 2697]
གལ་ཏེ་དེ་ལྟ་བུ་ནི་བསྒོམ་པའི་ལམ་མ༌[^1860]ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། ཇི་ལྟར་མཐོང་བ་བཞིན་བསྒོམ་པའི་ཕྱིར་རོ། །

[Block 2698]
འོན་ཏེ་གཅིག་མཐོང་བས་ལྷག་མ་རྣམས་ལྔ༌[^1861]དབང་ཐོབ་པའི་ཕྱིར་མངོན་པར་རྟོགས་པ་གཅིག་ཁོ་ན༌[^1862]ཞེས་ཟེར་ན་ནི་ཉེས་པ་མེད་དེ་བར་སྐབས་སུ་ལྡན་པ༌[^1863]ཡོད་དམ་མེད་ཅེས་དཔྱད་པར་བྱ་བ་ཡིན་ནོ། །

[Block 2699]
འོན་ཏེ་སྡུག་བསྔལ་ཁོ་ན་ཡོངས་སུ་ཤེས་ན་ཀུན་འབྱུང་ཡང་སྤོངས༌[^1864]ལ་འགོག་པ་ཡང་མངོན་སུམ་དུ་བྱེད་ཅིང་ལམ་ཡང་སྒོམ་པར་བྱེད་པས་དེའི་ཕྱིར་མངོན་པར་རྟོགས་པ་གཅིག་གོ་ཞེས་ཟེར་ན་དེ་ལྟ་ན་ཡང་ཉེས་པ་མེད་དེ། གཅིག་མཐོང་ན་ལྷག་མ་རྣམས་ཀྱང༌[^1865]བྱ་བའི་མངོན་པར་རྟོགས་པ་ཡིན་ནོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2700]
མདོ་ལས་མཐོང་བའི་མངོན་པར་རྟོགས་པའི་ཕྱིར་བདེན་པ་རྣམས་རིམ་གྱིས༌[^1866]མངོན་པར་རྟོགས་པར་གསུངས་པར་མངོན་ཏེ། ཁྱིམ་བདག་བདེན་པ་རྣམས༌[^1867]མངོན་པར་རྟོགས་པ་གཅིག་པ་ནི་མེད་པ་ཉིད་དེ། འོན་ཀྱང་མཐར་གྱིས་མངོན་པར་རྟོགས་སོ་ཞེས་རྒྱས་པར་གསུངས་པ་དཔེ་དང་བཅས་པའི་མདོ་གསུམ་ཁུངས་སུ་ཡོད་དོ། །

[Block 2701]
གལ་ཏེ་མདོ་ལས།

[Block 2702]
གང་ཞིག་སྡུག་བསྔལ་ལ་ནེམ་ནུར་མེད་ཅིང་ཐེ་ཚོམ་མེད་པ་དེ་ནི་སངས་རྒྱས་ལ་ཡང་ཞེས་གསུངས་པས་མངོན་པར་རྟོགས་པ་གཅིག་གོ་ཞེས་ཟེར་ན། མ་ཡིན་ཏེ། ཀུན་དུ་མི་འབྱུང་བ་དང་། གདོན་མི་ཟ་བར་སྤོང་བ་ལས་དགོངས་ཏེ་གསུངས་པའི་ཕྱིར་རོ། །

[Block 2703]
མངོན་པར་རྟོགས་པ་སེམས་བཅུ་དྲུག་པར་བཤད་པ་གང་ཡིན་པ་དེ་ནི་ཆོས་མཆོག་དང་ས་གཅིག །ཆོས་ཀྱི་མཆོག་ས་གང་ཡིན་པ་སེམས་བཅུ་དྲུག་པོ་འདི་དག་ཀྱང་དེའི་ས་པ་སྟེ། དེ་དག་ནི་ས་དྲུག་པའོ་ཞེས་སྔར་བཤད་ཟིན་ཏོ། །

[Block 2704 [HEADING]]
###### བར་ཆད་མེད་པ་དང་རྣམ་པར་གྲོལ་བའི་ལམ། ^3-1-3-8-3-0

[Block 2705]
ཅིའི་ཕྱིར་གདོན་མི་ཟ་བར་བཟོད་པ་དག་དང་། ཤེས་པ་དག་ཡིན་ཞེ་ན།

[Block 2706 [VERSE]]
བཟོད་དང་ཤེས་པ་གོ་རིམས་བཞིན། །
བར་ཆད་མེད་དང་རྣམ་གྲོལ་ལམ། །

[Block 2707]
བཟོད་པ་རྣམས་ནི་ཉོན་མོངས་པའི་ཐོབ་པ་རྣམ་པར་གཅོད་པ་ལ་བར་ཆད་བྱ་བར་མི་ནུས་པའི་ཕྱིར་བར་ཆད་མེད་པའི་ལམ་དག་ཡིན་ནོ། །ཤེས་པ་རྣམས་ནི་ཉོན་མོངས་པའི་ཐོབ་པ་ལས་རྣམ་པར་གྲོལ་བ་རྣམས་ལ་བྲལ་བའི་ཐོབ་པ་དང་ལྷན་ཅིག་སྐྱེ་བའི་ཕྱིར་རྣམ་པར་གྲོལ་བའི་ལམ་དག་ཡིན་ཏེ། དེའི་ཕྱིར་གཉི་ག་ཡང་ཡིན་པར་འགྱུར་ཏེ། གཉིས་ཀྱིས་རྐུན་པོ་འབྱིན་པ་དང་སྒོ་གཅོད་པ་བཞིན་ནོ། །

[Block 2708]
གལ་ཏེ་བར་ཆད་མེད་པའི་ལམ་གཉིས་པ་ཁོ་ན་བྲལ་བའི་ཐོབ་པ་དང་ལྷན་ཅིག་སྐྱེ་བར་གྱུར༌[^1868]ན་ནི༌[^1869]དམིགས་པ་དེ་ཁོ་ན་ལ་ཐེ་ཚོམ་སྤངས་པའི་ཤེས་པ་སྐྱེ་བར་མི་འགྱུར་རོ། །

[Block 2709]
གལ་ཏེ་བཟོད་པ་རྣམས་ཀྱིས་ཉོན་མོངས་པ་སྤངས་པའི༌[^1870]ཕྱིར་བསྟན་བཅོས་ལས་ཀུན་དུ་སྦྱོར་བའི་རིས་དགུ་ཞེས་འབྱུང་བ་དང་འགལ་ལོ་ཞེ་ན། མ་ཡིན་ཏེ། བཟོད་པ་རྣམས་ནི་ཤེས་པའི་འཁོར་ཡིན་པའི་ཕྱིར་རྒྱལ་པོའི་འཁོར་གྱིས་བྱས་པ་ལས་རྒྱལ་པོས་བྱས་སོ་ཞེས་ཐ་སྙད་འདོགས་པ་བཞིན་ནོ། །

[Block 2710 [HEADING]]
###### སྐད་ཅིག་བཅོ་ལྔ་མཐོང་བའི་ལམ། ^3-1-3-8-4-0

[Block 2711]
ཅི་སེམས་བཅུ་དྲུག་པོ་ཐམས་ཅད་བདེན་པ་མ་མཐོང་བ༌[^1871]མཐོང་བའི་ཕྱིར་མཐོང་བའི་ལམ་ཡིན་ནམ༌[^1872]ཞེ་ན། སྨྲས་པ། མ་ཡིན༌[^1873]ནོ། །

[Block 2712]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 2713 [VERSE]]
དེ་ལས༌[^1874]སྐད་ཅིག་བཅོ་ལྔ་ནི། །
མ་མཐོང་མཐོང་ཕྱིར་མཐོང་བའི་ལམ། །

[Block 2714]
སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་ནས་བཟུང་སྟེ་ལམ་ལ་རྗེས་སུ་ཤེས་པའི་བཟོད་པའི་བར་གྱི་སྐད་ཅིག་མ་བཅོ་ལྔ་པོ་དེ་དག་ནི་མཐོང་བའི་ལམ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། བདེན་པ་མ་མཐོང་བ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2715]
བཅུ་དྲུག་པ་ལ་ནི་སྔོན་མ་མཐོང་བ་བལྟ༌[^1875]བར་བྱ་བ་མེད་ཀྱི་ཇི་ལྟར་མཐོང་བ་ནི༌[^1876]གོམས་པར་བྱེད་པའི་ཕྱིར་བསྒོམ་པའི༌[^1877]ལམ་ཁོ་ན་ཡིན་ནོ། །

[Block 2716]
དེས་ཀྱང་ལམ་ལ་རྗེས་སུ་ཤེས་པའི་བཟོད་པ་མ་མཐོང་བ་མཐོང་བ་མ་ཡིན་ནམ་ཞེ་ན། བདེན་པའི་ཕྱིར་བསམ་གཏན་གྱི་སྐད་ཅིག་མ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2717]
སྐད་ཅིག་མ༌[^1878]གཅིག་མ་མཐོང་བས་ནི་བདེན་པ་མ༌[^1879]མཐོང་བ་མ་ཡིན་ཏེ། དཔེར་ན་ཉག་མ་གཅིག་མ་བརྔས་པས་ཞིང་མ་བརྔས་པ་མ་ཡིན་པ་བཞིན་ནོ། །

[Block 2718]
འབྲས་བུ་ཡིན་པའི་ཕྱིར་དང་། ཤེས་པ་བརྒྱད་དང་རྣམ་པ་བཅུ་དྲུག་ཐོབ་པའི་ཕྱིར་དང་། ལམ་སྔ་མ་རྣམ་པར་ཉམས་པའི་ཕྱིར་དང་། རྒྱུན་ཆགས་པ་ཡིན་པའི་ཕྱིར་ལམ་ལ་རྗེས་སུ་ཤེས་པ་ནི་བསྒོམ་པའི་ལམ་ཡིན་ནོ། །

[Block 2719]
ཡོངས་སུ་མ་ཉམས་པ་ནི་མཐོང་བས་སྤང་བར་བྱ་བའི་སྤངས་པ་ཡང་དག་པར་འཛིན་པའི་ཕྱིར་རོ། །

[Block 2720]
གལ་ཏེ་དེ་ཉིད་ཀྱི་ཕྱིར་མཐོང་བའི་ལམ་ཡིན་ཞེ་ན། མ་ཡིན་ཏེ། ཧ་ཅང་ཐལ་བར་འགྱུར་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་ཤེས་པ་བདུན་མཐོང་བའི་ལམ་ཡིན་ཞེ་ན། མཐོང་བ་མ་རྫོགས་པའི་ཕྱིར་ཏེ། བདེན་པ་མཐོང་བ་ཐམས་ཅད་མ་རྫོགས་པས་དེའི་བར་མར་གྱུར་པའི་ཕྱིར་དེ་དག་ཀྱང་མཐོང་བའི་ལམ་ཡིན་ནོ། །

[Block 2721]
མཐོང་བའི་ལམ་དང་བསྒོམ་པའི་ལམ་ཇི་ལྟར་སྐྱེ་བ་བཤད་ཟིན་ཏོ། །

[Block 2722 [HEADING]]
### འཕགས་པའི་ལམ་སྐྱེས་པའི་གང་ཟག་རྣམ་པར་གཞག་པ། ^3-2-0

[Block 2723]
ད་ནི་ཇི་ལྟར་ན་འཕགས་པའི་ལམ་སྐྱེས་པའི་གང་ཟག་རྣམས་རྣམ་པར་གཞག་པ་དེ་བཞིན་དུ་བཤད་པར་བྱ་སྟེ། མཐོང་བའི་ལམ་གྱི་རང་བཞིན་གྱི་སྐད་ཅིག་མ་བཅོ་ལྔར་བཤད་པ་གང་དག་ཡིན་པ།

[Block 2724 [HEADING]]
#### དད་པས་རྗེས་སུ་འབྲང་བ་དང་ཆོས་ཀྱིས་རྗེས་སུ་འབྲང་བ། ^3-2-1-0

[Block 2725 [VERSE]]
དབང་པོ་རྣོ་རྟུལ་དེ་དག་ཏུ། །
དད་དང་ཆོས་ཀྱིས་རྗེས་འབྲང་བ། །

[Block 2726]
ཡིན་པར་རིག་པར་བྱ་སྟེ། དབང་པོ་རྟུལ་པོ་དེ་དག་ལ་གནས་པ་ནི་དད་པས༌[^1880]རྗེས་སུ་འབྲང་བ་ཞེས་བྱའོ། །

[Block 2727]
དབང་པོ་རྣོན་པོ་ནི་ཆོས་ཀྱིས༌[^1881]རྗེས་སུ་འབྲང་བ་ཞེས་བྱའོ། །

[Block 2728]
དད་པས་རྗེས་སུ་འབྲང་བས་ན་དད་པས་རྗེས་སུ་འབྲང་བའོ། །

[Block 2729]
དེ་འདི་ལ་ཡོད་པས་སམ། འདི་དད་པས་རྗེས་སུ་འབྲང་བའི་ངང་ཚུལ་ཅན་ཡིན་པས་ན་དད་པས་རྗེས་སུ་འབྲང་བ་སྟེ། སྔོན་གཞན་གྱི་དྲིང་གིས་དོན་གྱི་རྗེས་སུ་འབྲང་བའི་ཕྱིར་རོ། །

[Block 2730]
ཆོས་ཀྱིས༌[^1882]རྗེས་སུ་འབྲང་བ༌[^1883]ཡང་དེ་དང་འདྲ་སྟེ། སྔོན་བདག་ཉིད་ཁོ་ནས་མདོ་ལ་སོགས་པའི་ཆོས་ཀྱི་དོན་གྱི་རྗེས་སུ་འབྲང་བའི་ཕྱིར་རོ། །

[Block 2731 [HEADING]]
#### འབྲས་བུ་དང་པོ་ལ་ཞུགས་པ། ^3-2-2-0

[Block 2732]
དེ་གཉིས་ནི།

[Block 2733 [VERSE]]
བསྒོམ་པས༌[^1884]སྤང་བྱ་མ་སྤངས་ན། །
འབྲས་བུ་དང་པོ་ལ་ཞུགས་པ། །

[Block 2734]
འབྲས་བུ་རྣམས་ཀྱི་དང་པོ་ནི་འབྲས་བུ་དང་པོ་སྟེ། རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུའོ། །

[Block 2735]
དེ་ནི་འབྲས་བུ་ཐོབ་པར་བྱ་བ་ཐམས་ཅད་ཀྱི་དང་པོ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
