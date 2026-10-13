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
[Block 176]
དེ་སྐད་དུ་ཡང་།

[Block 177 [VERSE]]
འཕགས་པས་བརྟེན་པ་འདི་ལྟ་བུ། །
དངོས་པོས་རྟོགས་པ་མ་ཡིན་ཞིང་། །
རྒྱུ་མཚན་མེད་པས༌[^152]རྣམ་ཤེས་ནི། །
ནམ་ཡང་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 178]
འཕགས་པ་ལྷས་ཀྱང་གསུངས་པ།

[Block 179 [VERSE]]
སྲིད་པའི་ས་བོན་རྣམ་པར་ཤེས། །
ཡུལ་ནི་དེ་ཡི་སྤྱོད་ཡུལ་ལ། །
མཐོང་བའི་ཡུལ་རྣམས་བདག་མེད་ཕྱིར། །
སྲིད་པའི་ས་བོན་འགག་པར་འགྱུར། །

[Block 180]
ཞེས་སོ། །

[Block 181]
དེའི་ཕྱིར་རྒྱུ་མཚན་གྱི་སྒོ་ཅན་གྱི་རྣམ་པར་ཤེས་པ་ནི་རྒྱུ་མཚན་མེད་པའི་ཕྱིར་མོ་གཤམ་གྱི་བུ་འབའ་ཞིག་པ་དམིགས་པ་མ་ཡིན་ནོ་ཞེས་རིགས་སོ།[^153] །གལ་ཏེ་གང་གི་དངོས་པོ་མེད་པ་རྣམ་པར་ཤེས་པས་དམིགས༌[^154]ནའོ། །

[Block 182]
སུ་ཞིག་འདི་སྐད་སྨྲ། དངོས་པོ་མེད་པ་འདི་ནི་རྣམ་པར་ཤེས་པས་དམིགས་པར་བྱ་བའོ་ཞེས་པ་འདི་སྐད་དུ་བརྗོད་པར་བྱ་སྟེ། དངོས་པོའི་སྒོ་ལ་མི་ལྟོས་པར་དངོས་པོ་མེད་པ་འབའ་ཞིག་རྣམ་པར་ཤེས་པས་མི་དམིགས་སོ་ཞེས་བྱ་སྟེ། དཔེར་ན་སྔོན་པོའི་རྣམ་པར་ཤེས་པ་སེར་པོ་ལ་སོགས་པ་ལ་མི་ལྟོས་པ་བཞིན། ཇི་ལྟར་ན་དངོས་པོའི་སྒོ་ཅན་ཡིན། སླར་ཡང་འདིའི་གཏན་མེད་ཀྱི་རྣམ་པར་ཤེས་པ་མོ་གཤམ་གྱི་བུའི་སྒྲ་ལ་ལྟོས་པ་བཞིན་ནོ། །

[Block 183]
འདིར་སྒྲ་འགའ་ཞིག་ནི་དོན་དང་བཅས་པའོ། །

[Block 184]
འགའ་ཞིག་དོན་མེད་པའོ། །

[Block 185]
དོན་དང་བཅས་པ་ནི་ལྷ༌[^155]སྦྱིན་ལ་སོགས་པའི་སྒྲའོ། །

[Block 186]
ལྷ༌[^156]སྦྱིན་ནི་འཇིག་རྟེན་ན་ཟ་བའི་བྱ་བ་རྫོགས་པའི་རྒྱུར་དམིགས་པས༌[^157]དོན་དེས་ན་ལྷ༌[^158]སྦྱིན་གྱི་སྒྲ་དོན་དང་ལྡན་པའོ། །

[Block 187]
མོ་གཤམ་གྱི་བུ་བསྟན་ཀྱང་འཇིག་རྟེན་པ་ལ་མི་དམིགས་ལ། དམིགས་པ་མ་ཡིན་པ་ནི་དངོས་པོ་ཞེས་རྣམ་པར་མི་འཇིག་གོ། །

[Block 188]
དེའི་ཕྱིར་མོ་གཤམ་གྱི་བུའི་སྒྲ་འདི་ཡང་བསྒྲུབ་བྱའི་དོན་གྱིས་སྟོང་པའོ། །

[Block 189]
རྣམ་པར་ཤེས་པ་ཡང་སྒྲའི་དོན་མངོན་པར་ཤེས་པ་རྣམས་ལ་དོན་གྱིས་སྟོང་པའི་སྒྲ་ལ་དམིགས་པའོ། །

[Block 190]
དོན་དངོས་པོ་མེད་པའི་སྒོ་ནས་དོན་མེད་པ་ཉིད་དུ་ངེས་པར་འགྱུར་ལ། དེ་ལ་འདིའི་སྒྲའི་དོན་ཡུལ་འགའ་ཞིག་ན་མེད་ཅིང་དུས་ནམ་ཞིག་ན་མེད་ལ་རྟོགས་པ་པོ་འགའ་ཞིག་ལ་སྣང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་སྟེ།[^159] ཐམས་ཅད་དུ༌[^160]དམིགས་པས་གཏན་མེད་ཅེས་འཇིག་རྟེན་དུ་རྣམ་པར་འཇོག་གོ། །

[Block 191]
དེ་ཡང་འདིའི་གཏན་མེད་ནི་སྒྲའི་དངོས་པོ་ལ་བརྟེན་ཏེ། སྒྲའི་དོན་མི་དམིགས་པའི་སྒོ་ནས་ཡོངས་སུ་བརྟགས་ལ། དེ་བཞིན་དུ་དངོས་པོ་ལ་བརྟེན་ནས་སྔ་ན་མེད་པ༌[^161]དང་གཅིག་ལ་གཅིག་མེད་པ་པ༌[^162]རྣམས་འཇིག་རྟེན་པས་རྣམ་པར་བརྟགས་སོ། །

[Block 192]
དེ་ལ་ད་ལྟ༌[^163]བའི་དངོས་པོ་ལ་ལྟོས་ནས་དེའི་སྐྱེ་བའི་སྔོན་རོལ་གྱི་གནས་སྐབས་ལ་སྔ་ན་མེད་པ་ཞེས་རྣམ་པར་འཇོག་ལ། ནམ་ཡང་དངོས་པོ་མི་སྲིད་པ་དེ་ནི་སྔ་ན་མེད་པ་མ་ཡིན་ཏེ། འདི་ལྟ་སྟེ་མོ་གཤམ་གྱི་བུ་ལྟ་བུའོ། །

[Block 193]
ད་ལྟར་བའི་དངོས་པོའི་རང་བཞིན་ནི་མི་རྟག་པའི་ཕྱིར། གང་ཞིག་འཇིག་པའི་གནས་སྐབས་སམ། མི་རྟག་པ་ཉིད་ལ་ཞིག་ནས་མེད་པ་ཞེས་བྱའོ། །

[Block 194]
གཅིག་ལ་གཅིག་མེད་པ་ཡང་གསལ་བར་དངོས་པོ་ལ་བརྟེན་པ་ཉིད་དོ་ཞེས་བྱ་སྟེ། དངོས་པོ་མེད་པ་ཞེས་བྱ་བ་དངོས་པོ་ལ་ལྟོས་པ༌[^164]འབའ་ཞིག་པ་རྣམ་པར་ཤེས་པས་འཛིན་པ་ནི་མདོ༌[^165]དེ་ཉིད་ཀྱིས་ན། འཕགས་པ་ལྷས་གསུངས་པ།

[Block 195 [VERSE]]
དངོས་པོ་མེད་ན་དངོས་མེད་ནི། །
ཤེས་པ་སྲིད་པ་མ་ཡིན་ལ། །
དངོས་པོ་མེད་ན༌[^166]དངོས་མེད་ནི། །
གྲུབ་པར་འགྱུར་བ་ག་ལ་ཞིག །

[Block 196]
ཅེས༌[^167]གསུངས་སོ། །

[Block 197]
དེ་ཉིད་ཀྱིས་ན་གང་དུ་མྱ་ངན་ལས་འདས་པའམ། མྱ་ངན་ལས་འདས་པ་དང་མཚུངས་པའི་ཆོས་ཀྱི་རང་བཞིན་ཁོང་དུ་ཆུད་པ་ན། དེ་ལ་དངོས་པོ་མེད་པ་ཡང་ཉེ་བར་ལེན་པ་མེད་པས་མེད་དོ་ཞེས་བྱ་སྟེ། རྣམ་པ་ཐམས་ཅད་དུ་དངོས་པོ་དང་དངོས་པོ་མེད་པ་ལ་ཀུན་དུ་འཛིན་པ་ཟད་པས་རྣམ་པར་ཤེས་པ་སྐྱེ་བ་མེད་པ་དང་མྱ་ངན་ལས་འདས་པ་འགོག་པ་རྣལ་འབྱོར་པ་རྣམས་ཀྱིས་ཐོབ་པར་འགྱུར་རོ། །

[Block 198]
དེའི་ཕྱིར་འདིར་དངོས་པོ་མེད་པ་འབའ་ཞིག་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་མེད་ལ། དེ་ལས་ཀྱང་བདག་མ་གྲུབ་པས་ངར་འཛིན་པའི་བརྗོད་པ་དངོས་པོ་མེད་པའོ་ཞེས་འདིར༌[^168]གྲུབ་བོ། །

[Block 199]
འོ་ན་ཆོས་འདི་དག་ནི་རང་རིག་པས་མྱོང་བ་འདི་ལྟ་སྟེ་ངར་འཛིན་པ་དང་ང་ཡིར་འཛིན་པའོ། །

[Block 200]
གལ་ཏེ་དེ་དག་དམིགས་པར་བྱ་བར་མེད་ཀྱང་དེ་ལྟ་ན་ཡང་ཉམས་སུ་མྱོང་བའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་ངར་འཛིན་པ་དང་ང་ཡིར་འཛིན་པ་འདི་དག་ནི་མེད་པའོ་ཞེས་བརྗོད་པར་མི་ནུས་སོ་ཞེ་ན། ཅི་བྱང་ཕྱོགས་སུ་ཁ་བལྟས་སམ། འོན་ཏེ་གཞན་དུ་ཁ་བལྟས་པ་ཡིན། འདི་ནི་ཤར་གྱི་ཕྱོགས་སོ་ཞེས་ཉམས་སུ་མྱོང་བ་མ་ཡིན་ནམ། བྱང་ལ་སོགས་པའི་ཕྱོགས་འདི་རྣམས་ཤར་ཕྱོགས་སུ་འགྱུར་བ༌[^169]མི་རིགས་ལ། རབ་རིབ་ཅན་གྱིས་སྐྲ་དང་སྦྲང་བུ་ལ་སོགས་པའི་དོན་མེད་ཀྱང་རང་གིས་ཅིའི་ཕྱིར་ཉམས་སུ་མ་མྱོང་། འདི་དག་སེམས་ཅན་གཞན་ལས་འབྱུང་བ༌[^170]མ་ཡིན་ནོ་ཞེས་བྱ་སྟེ། ཉམས་སུ་མྱོང་བ་ཙམ་གྱིས་ཡང་དག་པའི་དོན་གྱི་དངོས་པོར་རྣམ་པར་གཞག་པར་མི་ནུས་སོ། །

[Block 201]
དེའི་ཕྱིར་གལ་ཏེ་རང་ཉིད་ཀྱིས་ངར་འཛིན་པ་དང་ང་ཡིར་འཛིན་པ༌[^171]ཉམས་སུ་མྱོང་ཡང་དེ་ལྟ་ན་ཡང་ཡོད་པར་ལུང་དང་རིགས་པ་དང་འགལ་བས་མེད་དོ་ཞེས་བྱའོ། །

[Block 202]
དེའི་ཕྱིར་འཇིག་རྟེན་པའི་ང་དང་ང་ཡིར་འཛིན་པ་ཡང་དེ་བཞིན་གཤེགས་པའི་ང་དང་ང་ཡིར་འཛིན་པ་དང་མཚུངས་སོ་ཞེས་བྱ་སྟེ། ཆོས་ཐམས་ཅད་མིང་ཙམ་དུ་གྲུབ་བོ། །

[Block 203]
འདིར་སྨྲས་པ། གལ་ཏེ་དེ་ལྟར་བདག་མེད་ཀྱང་། །རེ་ཞིག་དེ་དང་འགལ་བའི་བདག་མེད་པ་ཡོད་ལ། དེ་བཞིན་དུ་བདག་གི་རང་བཞིན་དང་འགལ་བས་ཆོས་ཐམས་ཅད་ནི་བདག་མེད་པར་ཁས་བླངས་སོ། །

[Block 204]
ཇི་སྐད་དུ། བཅོམ་ལྡན་འདས་ཀྱིས་ཆོས་ཐམས་ཅད་བདག་མེད་པའོ་ཞེས་གསུངས་པས་བདག་ནི་མི༌[^172]རྟག་པ་མ་སྐྱེས་པ་ངར་འཛིན་པའི་ཡུལ་ཏེ། ཆོས་ཐམས་ཅད་ནི་དེ་ལྟ་མ་ཡིན་ནོ་ཞེས་སོ། །

[Block 205]
དེའི་ཕྱིར༌[^173]བདག་གི་རང་བཞིན་དང་འགལ་བའི་བདག་མེད་པའི་རང་བཞིན་གྱི་ཕྱིར་རམ། བདག་དང་བྲལ་བའི་ཕྱིར་ཆོས་ཐམས་ཅད་ནི་བདག་མེད་པའོ། །

[Block 206]
དེ་ཡང་ཡོད་ལ༌[^174]དེའི་ཕྱིར་བདག་གི་ཆོས་མེད་པས་ཆོས་ཐམས་ཅད་མིང་ཙམ་མ་ཡིན་ནོ་ཞེ་ན། སྨྲས་པ། ཅི་ཁྱོད་ནི་བདག་མེད་པ་ལ་ཕྱིན་ཅི་ལོག་ཏུ་སྒྲོ་འདོགས་པར་བྱེད། མུ་སྟེགས་བྱེད་ཀྱིས་ཡོངས་སུ་བརྟགས་པའི་བདག་གི༌[^175]དངོས་པོ་མེད་པ་དང་། དེའི་རང་བཞིན་མ་ཡིན་པ་ཉིད་ཀྱིས་ཆོས་ཐམས་ཅད་བདག་མེད་པ་ཉིད་དུ་རྣམ་པར་གཞག་པ་མ་ཡིན་ནོ། །

[Block 207]
དེ་ལྟ་ན་ཇི་ལྟར་འདིར་བདག་མེད་པ་ཡིན། ཉེ་བར་ལེན་པ་ལ་བཏགས་ནས་སམ། རང་བཞིན་གྱི་རྣམ་གྲངས་ལ་བདག་མེད་པ་ཉིད་དུ་བསྟན་པ་ན་དོན་ཆེན་པོ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 208]
དེ་ལ་ཕུང་པོ་ལ་བརྟེན་ནས་བཏགས་པའི་གང་ཟག་ལ་བདག་ཅེས་བརྗོད་དེ། འཇིག་རྟེན་པའི་ངར་འཛིན་པའི༌[^176]ཕྱིར་རོ། །

[Block 209]
མུ་སྟེགས་བྱེད་ཀྱིས་ཡོངས་སུ་བརྟགས་པ་ནི་མ་ཡིན་ཏེ། དེ་ཡང་མུན་ནག་གི་ནང་དུ་གྱུར་པའི་སྐྱེས་བུའི་རྣམ་པ་ལ་ཡོངས་སུ་བརྟགས་པ་བཞིན་དུ་ཉུང་ཟད་ཀྱིས་ཤིན་ཏུ་ཕྱིན་ཅི་ལོག་པས་ཡོངས་སུ་བརྟགས་ཀྱི། འདི་ནི་མ་ལུས་པའི་འགྲོ་བས་ཡོངས་སུ་བརྟགས་པ་མ་ཡིན་ནོ། །

[Block 210]
གང་དུ་ཕུང་པོ་ལ་བརྟེན་ནས་འགྲོ་བ་མ་ལུས་པ་ང་ཡིར་འཛིན་པའི༌[^177]ཡིན་ལ། དེ་ནི་མངོན་པར་ཞེན་པའི་གནས་སུ་གྱུར་པའི་ཕྱིར་འདིར་བསལ་བར་བྱའོ། །

[Block 211]
བདག་བརྟགས་པ༌[^178]ནི་འཇིག་རྟེན་པའི་ཐ་སྙད་ཀྱི༌[^179]རྣམ་པར་གཞག་པ་ཉིད་ལས་ཤིན་ཏུ་བསལ་བའི་ཕྱིར་དེ་ནི་དེ་ཁོ་ན་ཉིད་ལ་དཔྱོད་པའི་དབང་དུ་བྱས་ཀྱི། དེ་སེལ་བའི་དབང་དུ་བྱས་པ་མ་ཡིན།[^180] གལ་ཏེ་མུ་སྟེགས་བྱེད་ཀྱིས་ཡོངས་སུ་བརྟགས་པའི་བདག་འདིར་འགེགས་པར་མི་བྱེད་ན།

[Block 212]
དེ་ལྟ་ན་བཅོམ་ལྡན་འདས་ཀྱིས་ཅི་ཞིག་དགག་པའི་དོན་དུ་འདི་སྐད་གསུངས།

[Block 213]
མིག་ནི་བདག་དང་བདག་གི་བརྟག༌[^181]པ་བརྟེན་པ་ཐེར་ཟུག་པ་ཡོངས་སུ་འགྱུར་བའི་ཆོས་ཅན་མ་ཡིན་པས་སྟོང་པར་གྲུབ་བོ་ཞེས་སོ། །

[Block 214]
མིག་ལ་བརྟེན་ནས་བཏགས་པའི་བདག་གིས་སྟོང་པ་དང་རང་བཞིན་གྱིས༌[^182]སྟོང་པ་ཉིད་དུ་ལུང་འདིས་གསལ་བར་མཛད་ཀྱི། ནང་གི་བྱེད་པའི་སྐྱེས་བུ་དང་བྲལ་བ་ནི་མ་ཡིན་ནོ། །

[Block 215]
དེ་ལ་མིག་ནི་བདག་གིས་སྟོང་ངོ་ཞེས་པ་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལ་བརྟེན་ནས་གང་ཞིག་ལ་བཏགས་ལ་བདག་དེ་ནི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལ་རྣམ་པ་ལྔས་མེད་ཀྱང་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལ་བརྟེན་ནས་འདོགས་ལ། དེ་ཡང་མེད་པ་ཉིད་དེ། མིག་ལ་སོགས་པ་སོ་སོ་ལ་རྣམ་པ་ལྔས་ཀྱང་མེད་པ་ཉིད་དུ་ཁོང་དུ་ཆུད་པར་བྱའོ་ཞེས་ཐར་པ་འདོད་པ་རྣམས་ལ་བཅོམ་ལྡན་འདས་གདམས་པ་སྟོན་པར་བཞེད་པ་ཉིད་ཀྱིས་མིག་ནི་བདག་གིས་སྟོང་པར་གྲུབ་པོ་ཞེས་གསུངས་སོ། །
--- END BLOCKS ---
