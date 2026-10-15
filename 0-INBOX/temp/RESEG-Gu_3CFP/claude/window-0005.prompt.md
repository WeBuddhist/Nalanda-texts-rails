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
སྒྲིབ་པ་གསུམ་པོ་འདི་དག་གིས་འཇུག་པར་དཀའ་བ་ཉིད་དེ། དེའི་བར་དུ་གཅོད་པས་སོ། །

[Block 177]
བག་མེད་པ་དང་། ལེ་ལོ་དང་། མ་དད་པ་ཤས་ཆེ་བ་རྣམས་ནི་སྒྲུབ་པའི་བར་དུ་གཅོད་པའོ། །

[Block 178]
བྱ་བ་ངན་པ་ལ་ཆགས་པ་ཉིད་དང་། བར་དུ་ཉམས་པ་དང་། ཐོབ་པར་བྱ་བ་དང་། ཐོབ་པར་བྱེད་པ་ལ་དད་པ་མེད་པ་དང་། བག་མེད་པས་མི་སྒྲུབ་པ་དང་། དེ་བཞིན་དུ་ལེ་ལོས་ཞུགས་སུ་ཟིན་ན་ཡང་བར་ནས་མངོན་པར་ལྡོག་པ་སྟེ། མ་དད་པའི་ཤས་ཆེ་བ་རྣམས་ཀྱིས་སྒྲུབ་པ་གཡེལ་བའོ། །

[Block 179]
སེམས་བསྐྱེད་པའི་རྐྱེན་བཞིའི་བསྡུས་པའི་དོན་ནི། བྱང་ཆུབ་སེམས་དཔའི་རིགས་ངེས་པ༌[^96]སེམས་བསྐྱེད་པའི་རྐྱེན་གཉིས་དང་། བྱང་ཆུབ་ཏུ་གྱུར་པའི་སེམས་བསྐྱེད་པའི་རྐྱེན་གཉིས་སོ། །

[Block 180]
བྱང་ཆུབ་སེམས་དཔའི་རིགས༌[^97]ངེས་པ་རྣམ་པ་གཉིས་ནི་རྒྱ་ཆེ་བ་ལ་མོས་པ་དང་། ཟབ་པ་ལ་མོས་པའོ། །

[Block 181]
བྱང་ཆུབ་ཏུ་འགྱུར་བ་རྣམ་པ་གཉིས་ནི། སློབ་པ༌[^98]དང་མི་སློབ་པ་ཞེས་བྱ་བའོ། །

[Block 182]
བཞི་པོ་དེ་རྣམས་ནི་སེམས་བསྐྱེད་པའི་རྐྱེན་ཉིད་པས། བཞི་པོ་འདི་དག་ནི་སེམས་བསྐྱེད༌[^99]པའི་རྐྱེན་དུ། སེམས་བསྐྱེད་པ་དང་། ཅི་ལྟར་འཚམ་པར་སྦྱར་རོ། །

[Block 183]
རྒྱུ་བཞིའི༌[^100]བསྡུས་པའི་དོན་ལ། རྒྱུ་གསུམ་ནི་ཆོས་ཉིད་ཀྱིས་ཐོབ་པ་དང་། ཕྱི་རོལ་གྱི་གཞན་གྱི་སྒྲའི་མཚན་མ་ལས༌[^101]དང་། ནང་གི་ཚུལ་བཞིན་ཡིད༌[^102]ལ་བྱེད་པས་བསྡུས་པའོ། །

[Block 184]
དེ་ཡང་རྣམ་པ་གཉིས་ཏེ། གཞན་སྡུག་བསྔལ་ལས་བསྒྲལ་བར་འདོད་པ་དང་། བདག་གི་རྒྱུད་དུ་གཏོགས་པའི་སྡུག་བསྔལ་གྱིས་མི་འཇིགས་པ་ཉིད་དེ། འཁོར་བའི་སྡུག་བསྔལ་སྐྱེ་བ་ལ་སོགས་པ་དང་། དཀའ་བ་སྤྱོད་པས་སྡུག་བསྔལ་ན་ཡང་ཚོགས་གཉིས་ཀུན་ནས་སོགས་པའོ། །

[Block 185]
བྱང་ཆུབ་སེམས་དཔའི་རིགས་ཕུན་སུམ་ཚོགས་པ་ནི་ཆོས་ཉིད་ཀྱི་ས་ཐོབ་པ་ཡིན་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་འདི་ནི་རིགས་ཕུན་སུམ་ཚོགས་པའི་དབྱེ་བ་ཡོད་པའི་རྒྱུ་རབ་ཏུ་བསྟན་པའི་དོན་དུ་གསུངས་སོ། །

[Block 186]
བླུན་པོ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་ལྷན་ཅིག་སྐྱེས་པའི་ཤེས་རབ་དང་ལྡན་པའོ། །

[Block 187]
ཡིད་རྟུལ་བའི་རང་བཞིན་ཅན་མ་ཡིན་ཞེས་བྱ་བ་ནི། མྱུར་དུ་འཛིན་པར་ནུས་པའོ། །

[Block 188]
མཁས་ཤིང་ཞེས་བྱ་བ་ནི་ཐོས་པ་ལས་བྱུང་བའི་ཤེས་རབ་དང་ལྡན་པའོ། །

[Block 189]
མཛངས་པ་ནི༌[^103]བསམས་པ་ལས་བྱུང་བའི་ཤེས་རབ་དང་ལྡན་པ་ཉིད་དོ། །

[Block 190]
བཤེས་གཉེན་ཕུན་སུམ་ཚོགས་པ་རྣམ་པ་བཞིའི་བསྡུས་པའི་དོན་ནི། ཤེས་རབ་ཕུན་སུམ་ཚོགས་པ་དང་། སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བསྟན་ཏོ། །

[Block 191]
སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་ཡང་རྣམ་པ་གསུམ་སྟེ། ཉོན་མོངས་པ་སྤྱོད་པ་ལས་ལྡོག་པར་སྦྱོར་བ་དང་། མི་དགེ་བའི་ལས་ཀྱི་ལམ་ལྡོག་པ་ལ་སྦྱོར་བ་དང་། དགེ་བའི་ལས་ལ་ནུས་པ་དང་ལྡན་པ་གོང་མ་གོང་མའི་ཁྱད་པ༌[^104]ལ་སྦྱོར་བ་སྟེ། བག་མེད་པའི་གནས་ལ་ཉེ་བར་སྦྱོར་བ་དང་། ཉེས་པར་སྤྱོད་པ་ལ་རྣམ་པར་སྦྱོར་བ་དང་། ཤིན་ཏུ་དམན་པ་ལ་དད་པ་དང་། འདུན་པ་དང་། དམ་འཆའ་བ་དང་། བརྩོན་འགྲུས་ཀྱི་ཐབས་དང་། ཡོན་ཏན་དུ་ཁས་ལེན་པ་ལ་སོགས་པའི་གཉེན་པོར་རིག་པར་བྱའོ། །

[Block 192]
རྒྱུ་བཞིས་བྱང་ཆུབ་སེམས་དཔའ་སྙིང་རྗེ་བའི་ཤས་ཆེ་བར་འགྱུར་ཏེ། རྒྱུ་བཞིའི་བསྡུས་པའི་དོན་ནི། གང་དུ་སྡུག་བསྔལ་བ་དང་། གང་གིས་སྡུག་བསྔལ་བ་དང་། གང་སྡུག་བསྔལ་གྱི་རྣམ་པ་ལ་ཉེ་བར་དམིགས་ནས་སྙིང་རྗེ་ཤས་ཆེ་བར་འགྱུར་བ་སྟེ། དེ་ལ་གང་གིས་སྡུག་བསྔལ་ཞེས་བྱ་བ་ནི་གཞན་རྣམས་བདག་གམ་གཉི་གའམ་གཞན་ཡང་ཇི་ལྟར་རིགས་པར་སྦྱར་རོ། །

[Block 193]
རང་བཞིན་གྱིས་སྙིང་སྟོབས་ཆེ་ཞིང་བརྟན་པ་དང་ལྡན་པས༌[^105]སྟོབས་དང་ལྡན་པ་ཡིན་ཞེས་བྱ་བ་ལ། བསྟན་པ༌[^106]ནི་དམན་པའི་སེམས་ཉོན་མོངས་པ་བཞིན་དུ་ངེས་པར་སྤོང་བ་སྟེ། ཉོན་མོངས་པའི་དབང་གིས་རྗེས་སུ་མི་འབྱུང་བའོ། །

[Block 194]
སྡུག་བསྔལ་གྱི་སེམས་མང་ཞིང་རབ་ཏུ་དྲག་པས་མི་འཇིགས་པའི་ངང་ཚུལ་ཉིད་ཀྱིས་ཡང་དག་པར༌[^107]སྦྱོར་བ་ལས༌[^108]མི་བསྐྱོད་པ་ནི་རང་བཞིན་གྱིས་སྙིང་སྟོབས་ཆེ་བ་དང་ལྡན་པ་ནི། སོ་སོར་རྟོག་པ་དང་ལྡན་པས་མཁས་པར་འགྱུར་ཏེ། ཐོས་པ་ལས་བྱུང་བའི་ཤེས་རབ་དང་ལྡན་པའོ། །

[Block 195]
ཡང་དག་པར་སེམས་པའི་ངང་ཚུལ་ཅན་ཞེས་བྱ་བ་ནི། བསམས་པ་ལས་བྱུང་བའི་ཤེས་རབ་དང་ལྡན་པའོ། །

[Block 196]
གང་ལ་སོ་སོ་སོ་སོར་རྟོག་པའི་སྟོབས་ཡོད་པ་དེ་ནི་སོ་སོར་རྟོག་པའི་སྟོབས་དང་ལྡན་པས་འཁོར་བའི་སྡུག་བསྔལ་ལ་མི་འཇིགས་པའོ། །

[Block 197]
གཞིའི༌[^109]རྒྱུའི་བསྡུས༌[^110]པའི་དོན་ནི་གང་ལ་མི་འཇིགས་པ་དང་། རྒྱུ་གང་གིས་མི་འཇིགས་པ་དང་ཞེས་བྱ་བ་སྟེ། སྙིང་སྟོབས་དང་ལྡན་པ་དང་། སོ་སོར་རྟོག་པ་དང་ལྡན་པ་དང་། [^111]རྒྱུ་གང་གིས་བྱང་ཆུབ་ལས་མི་གཡོ་བ་དང་། སེམས་ཅན་གྱི་སྡུག་བསྔལ་བསལ་བར་འདོད་པའོ། །

[Block 198]
སྡུག་བསྔལ་གྱི་རྒྱུ་བཞིའི་བསྡུས་པའི་དོན་ནི། སྡུག་བསྔལ་ཇི་སྙེད་ཡོད་པ་དང་། སྡུག་བསྔལ་ཇི་ལྟར་ཡོད་པའོ། །

[Block 199]
དེ་ལ་ཇི་སྙེད་ཡོད་པ་ནི༌[^112]ཡུན་རིང་བ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 200]
དེ་ལས་གཞན་པ་རྣམ་པ་གསུམ་ནི་ཇི་ལྟར་ཡོད་པའོ། །

[Block 201]
དེ་ཡང་རྣམ་པ་གསུམ་སྟེ། སྣ་ཚོགས་པ་ཉིད་དང་། དྲག་པ་ཉིད་དང་། བར་ཆད་མེད་པ་ཉིད་དོ། །

[Block 202]
སྟོབས་བཞིའི་བསྡུས༌[^113]དོན་ནི་རྣམ་པ་གཉིས་ཏེ། དགེ་བའི་ཆོས་གོམས་པ་དང་། རྒྱུད་དུ་གཏོགས་པའོ། །

[Block 203]
རྒྱུད་དུ་གཏོགས་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། བདག་དང་གཞན་གྱི༌[^114]བྱེ་བྲག་གིས་སོ། །

[Block 204]
དགེ་བའི་ཆོས་ལ་གོམས་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། འདས་པའི་དུས་ཀྱི་དང་། མཐོང་བའི་ཆོས་ཀྱི་དུས་ཀྱི་དབྱེ་བས་སོ། །

[Block 205]
བྱང་ཆུབ་སེམས་དཔའ་དང་པོ༌[^115]སེམས་བསྐྱེད་པ་བསྟན་པའི་ངོ་མཚར་རྨད་དུ་བྱུང་བའི་ཆོས་འཇིག་རྟེན་དང་ཐུན་མོང་མ་ཡིན་པའི་བསྡུས་པའི་དོན་ནི། སེམས་ཅན་ཐམས་ཅད་ཆུང་མ་ལྟར་ཡོངས་སུ་འཛིན་ན་ཡང་ཉོན་མོངས་པས་མི་གོས་པ་ནི་སྐྱེ་མཆེད་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 206]
དེ་ནས༌[^116]སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པས་བསམ་པ་དང་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པར་བྱས་ནས་དགེ་བའི་ཆོས་སྐྱེད་ཅིང་སྤེལ་ལོ། །

[Block 207]
དེ་ནས་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 208]
དེ་ནས་མཐོང་བའི་ཆོས་དང་ཚེ་ཕྱི་མའི་ཕན་ཡོན་ཏེ། ཚེ་ཕྱི་མའི་ནི། ངན་སོང་དུ་སྐྱེས་སུ་ཟིན་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 209]
ཡང་འབྲས་བུའི་ཁྱད་པར་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་འབྲས་བུ་ལས་ཤིན་ཏུ་ཁྱད་པར་དུ་འཕགས་པའོ། །

[Block 210]
དང་པོ་སེམས་བསྐྱེད་པའི་ལེའུ་འདིའི་བསྡུས་པའི་དོན་ནི།

[Block 211]
དང་པོ་སེམས་བསྐྱེད་པའི་མཚན་ཉིད་དང་། ཁྱད་པར་གྱི་མཚན་ཉིད་དང་། རྒྱུན་མི་འཆད་པར་སེམས་བསྐྱེད་པའི༌[^117]རྐྱེན་བཞི་དང་། རྒྱུ་བཞི་དང་། རྒྱུ་དང་སྟོབས་གང་དག་གིས་སེམས་བསྐྱེད་པ་བསྟན་པས༌[^118]དེའི་མི་མཐུན་པ་ལས་ལྡོག་པ་དང་།

[Block 212]
དང་པོ་སེམས་བསྐྱེད་པར་བསྟེན༌[^119]པའི་ངོ་མཚར་རྨད་དུ་བྱུང་བའི་ཆོས་དང་། དེའི་ཕན་ཡོན་ནི་རང་གི་མཚན་ཉིད་དང་། ཁྱད་པར་གྱི་མཚན་ཉིད་དང་། སྐྱེ་བའི་རྒྱུ་དང་རྐྱེན་དང་སྟོབས་དང་། དེ་ལ་རྨོངས་པ་རྣམས་ལ་བསྟན་པ་དང་། ངོ་མཚར་རྨད་དུ་བྱུང་བའི་ཆོས་ལ་སོགས་པས་རིགས་མ༌[^120]ངེས་པ་དང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་རིགས་ལ་ཞུགས་པ་རྣམས་རྣམ་པར་བཟློག་ནས་གཞུག་པའི་དོན་དང་། མ་ངེས་པའི་རིགས་ཅན་རྣམས་སངས་རྒྱས་ཉིད་ལ་རབ་ཏུ་དགོད་ཅིང་ངེས་པར་བཟུང་བ་དང་། བྱང་ཆུབ་སེམས་དཔའི༌[^121]རིགས་ཅན་བག་མེད་པ་དང་། ཞུམ་པ་དང་ཡང་དག་པར་རབ་ཏུ་ཞུགས་པ་རྣམས་ལ་གོ་རིམ་ཇི་ལྟ་བ་བཞིན་དུ་ཡང་དག་པར་བཟུང་བ་དང་། ཡང་དག་པར་གཟེངས་བསྟོད་པ་དང་། ཡང་དག་པར་མགུ་བར་བྱ་བའོ། །

[Block 213]
འབྲས་བུ་དང་བཅས་པའི་བསོད་ནམས་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའི་ཕན་ཡོན་མདོར་བསྡུས་པའི་དོན་ནི་མཐོང་བའི་ཆོས་ལ་བདག་གི་ལུས་ལ་གནོད་པ་མེད་པ་དང་། འཁོར་ལོས་སྒྱུར་བའི་རྫུ་འཕྲུལ་གྱི་ཡོན་ཏན་ཞེས་བྱ་བ་ལ་སོགས་པ་བསྟན་པ་ནི། མ་འོངས་པའི་དུས་སུ་ཐོབ་པའི་སྐྱེ་བ་ལ་བདག་དང་གཞན་གྱི་དོན་སྒྲུབ་ནུས༌[^122]པའི་ལུས་རབ་ཏུ་འཐོབ་པ་སྟེ། ཚེ་བརྗེས་པའི་འོག་ཏུ་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །

[Block 214]
མཐོང་བའི་ཆོས་ཉིད་ལ་བདག་ལ་གནོད་པའི་ལུས་དང་སེམས་ཀྱི་གནས་ངན་ལེན་དང༌[^123]ཉམས་སྨད་པའི་ཕྱིར་བདག་ལ་གནོད་པའི་ངོ་བོ་མེད་དོ། །

[Block 215]
དེའི་བསོད་ནམས་ཀྱི་དབང་གིས་གཞན་གྱིས་བྱས་པའི་སྔགས་ལ་སོགས་པས་གཞན་ལ་གནོད་པ་ཡང་མེད་དོ།[^124] །བྱང་ཆུབ་སེམས་དཔའི༌[^125]རིགས་ལ་གནས་པ་ནི་རང་བཞིན་གྱིས་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །
--- END BLOCKS ---
