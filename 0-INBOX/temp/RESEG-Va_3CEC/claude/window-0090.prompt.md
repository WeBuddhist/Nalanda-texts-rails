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
[Block 3151]
སྨོན་པ་མེད་པའི་དོན་ནི་སྡུག་བསྔལ་གྱི་དོན་ཏོ་ཞེས་བྱ་བ་དགའ་བའི་ཡུལ་མ་ཡིན་པའི་དོན་བསྟན་ཏེ། ཟག་པ་དང་བཅས་པའི་ཆོས་ཐམས་ཅད་ནི་སྡུག་བསྔལ་རྣམ་པ་སྣ་ཚོགས་སྐྱེ་བའི་རྒྱུ་དང་གཞི་ཡིན་པས་དེ་ལ་སྨོན་ཅིང་དགའ་བར་བྱ་བའི་ཡུལ་མ་ཡིན་ཏེ་དེ་ནི་སྡུག་བསྔལ་གྱི་དོན་ཏོ། །

[Block 3152 [HEADING]]
#### སྒྲ་ཙམ་དུ་ཟད་པའི་དོན། ^10-2-4-0

[Block 3153]
སྡུག་བསྔལ་གྱི་སྒྲ་རབ་ཏུ་བསྟན་པ༌[^2725]ཞེས་བྱ་བས་སྒྲ་ཙམ་དུ་ཟད་པའི་དོན་བསྟན༌[^2726]ཏེ། སྡུག་བསྔལ་ཞེའོ་ཞེས་བྱ་བའི་སྒྲས་བརྗོད་པ་ཉིད་སྡུག་བསྔལ་དུ་ཟད་ཀྱི་སྡུག་བསྔལ་གྱི་དངོས་པོ་གང་ཡང་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3154 [HEADING]]
#### རང་བཞིན་གྱིས་སྟོང་པའི་དོན། ^10-2-5-0

[Block 3155]
ནམ་མཁའ་རབ་ཏུ་བརྗོད་པའི་དོན་ནི་ཞེས་བྱ་བས་རང་བཞིན་གྱིས་སྟོང་པའི༌[^2727]དོན་བསྟན་ཏེ། གང་སྟོང་པ་དེ་ཉིད་སྡུག་བསྔལ་བ་སྟེ། ནམ་མཁའ་བཞིན་དུ་སྟོང་པར་བརྗོད་པའི་དོན་ཉིད་སྡུག་བསྔལ་བའི་དོན་ཏོ། །

[Block 3156 [HEADING]]
### ཆོས་ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ཤེས་པ། ^10-3-0

[Block 3157]
ཆོས་ཐམས་ཅད་ཀྱི་མཚན་ཉིད༌[^2728]ཤེས་པའི་དབང་དུ་བྱས་ནས་དེ་ལ་བདག་མེད་པའི་དོན་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3158]
བདག་ནི་ཤིན་ཏུ་བདག་མེད་པ་སྟེ་ཞེས་བྱ་བ་ལ། བདག་རྣམ་པ་གཉིས་ཏེ། གཞན་གྱིས་བརྟགས་པ་དང་། གཟུང་བ་དང་། འཛིན་པར་སྣང་བའོ། །

[Block 3159]
བདག་དེ་གཉིས་ལ་བདག་གི་དངོས་པོ་མེད་པས་ན་བདག་མེད་པའོ། །

[Block 3160]
གང་བདག་མེད་པའི་དོན་དེ་ནི་ཞེས་བྱ་བ་ནི་བདག་རྣམ་པ་གཉིས་མེད་དེ་སྟོང་པའི་དོན་དེ་ནི་གསོབ་བོ་ཞེས་བྱ་བ་ལ་སོགས་པར་སྦྱར་རོ། །

[Block 3161]
སྙིང་པོ་རང་བཞིན་མེད་པའི་ཕྱིར་གསོབ་བོ། །ཤེས་རབ་ཀྱི་མིག་གིས་བརྟག༌[^2729]མི་བཟོད་པའི་ཕྱིར་གསོག་གོ། །

[Block 3162]
སྣང་བ་ཙམ་ཡང་རྒྱུ་རྐྱེན་ལ་ལྟོས་པའི༌[^2730]ཕྱིར་ཡ༌[^2731]མ་བརླའོ།[^2732] །ཇི་ལྟར་སྣང་བ་ཀུན་ཡང་སྟོང་པ་ཡིན་པའི་ཕྱིར་སྟོང་པའོ། །

[Block 3163]
སྟོང་པའི་དོན་ནི་བདག་མེད་པའི་དོན་ཞེས་བྱ་བ་ལ། དེ་བས་ན་བདག་དང་ཆོས་གཉིས་ཀྱིས་སྟོང་པའི་དོན་གང་ཡིན་པ་དེ་ཉིད་བདག་མེད་པའི་དོན་ཏོ། །

[Block 3164 [HEADING]]
### ཞི་བའི་ང་རྒྱལ་མེད་པ། ^10-4-0

[Block 3165]
ཞི་བའི་ང་རྒྱལ་མེད༌[^2733]པའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཞི་བའི་དོན་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3166]
ཞི་བ་ནི་ཞི་བས་ཞི་བར་མི་འགྱུར་ཏེ། ཞི་བ་ཉིད་ཞི་བའོ་ཞེས་བྱ་བ་ལ། ཞི་བ་ཞེས་བྱ་བ་ནི་སྟོང་པའམ། མྱ་ངན་ལས་འདས་པ་ལ་བྱ་སྟེ། སྟོང་པའམ་མྱ་ངན་ལས་འདས་པའི་དེའི་རང་བཞིན་ཞི་བར་རྟོགས་པའི༌[^2734]ཡེ་ཤེས་ཀྱིས༌[^2735]ཞི་བ་དང་སྟོང་པར་བྱས་པ་ནི་མ་ཡིན་གྱི། ངོ་བོ་ཉིད་ཀྱིས་ཡེ་ནས་ཞི་ཞིང་སྟོང་པའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3167]
མ་ཞི་བ་ཡང་ཞི་བས་ཞི་བར་མི་འགྱུར་ཏེ༌[^2736]ཞེས་བྱ་བ་ནི་འཁོར་བའི་ཆོས་འདུས་བྱས་ཀྱི་དངོས་པོ་དེ་དག་ཀྱང་ཡེ་ཤེས་ཀྱིས་ཞི་བ་དང་སྟོང་པར་རྟོགས་ནས་ཞི་ཞིང་མེད་པར་བྱས་པ་ནི་མ་ཡིན་གྱི། [^2737]དེ་དག་ཀྱང་ཡེ་ནས་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་ཤིང་ཞི་བའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3168]
ཞི་བའོ་ཞེས་བྱ་བའི་སྒྲའི་དོན་བསྟན་པའི་ཕྱིར། གང་ཞི་བའི་དོན་དེ་ནི་མཚན་མ་ཐམས་ཅད་ཉེ་བར་ཞི་བ་ཞེས་གསུངས་ཏེ། ལས་དང་ཉོན་མོངས་པ་དང་། གཟུང་བ་དང་འཛིན་པའི་མཚན་མ་ཐམས་ཅད་ཞི་སྟེ་མེད་པ་དེ་ནི་ཞི་བ་ཞེས་བྱའོ། །

[Block 3169]
ཞི་བ་དངོས་གང་ཡིན་པ་བསྟན་པའི་ཕྱིར། ཞི་བ་ནི་མྱ་ངན་ལས་འདས་པ་ཞེས་གསུངས་ཏེ།[^2738] ཉོན་མོངས་པ་དང་ཕུང་པོ་སྤངས་པའི་མྱ་ངན་ལས་འདས་པ་སྟེ༌[^2739]ཞི་བའོ། །

[Block 3170]
ཆོས་ཀྱི་མདོ་བཞི་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 3171 [HEADING]]
## ལྷུན་གྱིས་གྲུབ་པའི་བྱང་ཆུབ་སེམས་དཔའ། ^11-0

[Block 3172]
ལྷུན་གྱིས་གྲུབ་པའི་བྱང་ཆུབ་སེམས་དཔའ་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^2740]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་གཅིག་པུ་བགྲོད་པའི་ལམ་མི་ཟད་པ་ཡིན་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། འདིས་བསྡུས་པའི་དོན་རང་བྱང་ཆུབ་པ་བསྟན་ཏོ། །

[Block 3173]
གཞན་ལ་མི་ལྟོས་པར༌[^2741]བདག་གཅིག་པུས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པར་བྱེད་པ་ནི་གཅིག་པུས༌[^2742]བགྲོད་པ་སྟེ། གང་དེ་ལྟར་བྱེད་པ་ཉིད་ལམ་ཡིན་ནོ། །

[Block 3174]
མི་ཟད་པ་ཡང་བགྲོད་ཅིང་ཐོབ་པར་བྱ་བའི་ཆོས་མི་ཟད་པའི་ཕྱིར་བགྲོད་པར་བྱེད་པ་དང་། ཐོབ་པར་བྱེད་པ་ཡང་མི་ཟད་པའོ། །

[Block 3175]
ལྷུན་གྱིས་གྲུབ་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡང་རྣམ་པ་བཞི་སྟེ། མི་གཡེང་བ་དང་། བཟོད་པ་ཐོབ་པ་དང་། མཉམ་པ་ཉིད་ལ་གནས་པ་དང་། སྒྲིབ་པ་མེད་པའོ། །

[Block 3176 [HEADING]]
### མི་གཡེང་བ། ^11-1-0

[Block 3177]
དེ་ལ་མི་གཡེང་བ་ནི། འཇིག་རྟེན་ལས་འདས་པ་དང་། འཇིག་རྟེན་པའི་ཡོན་ཏན་རྣམས་བདག་འབའ་ཞིག་གིས་ཐོབ་པར་བྱ་བའི་ཕྱིར་རྩོམ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། གཅིག་པུ་བགྲོད་པའི་ལམ་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3178]
གཅིག་པུ་བགྲོད་པའི་ལམ་ནི་ཐེག་པ་གཅིག་པའི་ལམ་སྟེ། ལམ་དེ་བསྒྲུབ་པར་བྱ་བ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་གཞན་སུ་ལ་ཡང༌[^2743]མི་རྟེན་པར༌[^2744]བདག་གཅིག་པུས་སྒྲུབ་པར་བྱེད་པའོ། །

[Block 3179]
ཐེག་པ་གཅིག་གི༌[^2745]ལམ་དངོས་གང་ཡིན་པ་བསྟན་པའི་ཕྱིར། གཅིག་པུ་བགྲོད་པའི་ལམ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3180]
བྱང་ཆུབ་ཏུ་གོ་ཆ་གྱོན་ཞེས་བྱ་བ་ནི་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པར་བྱ་བའི་ཕྱིར་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་ཅིང་བརྩོན་འགྲུས་རྩོམ་སྟེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3181]
བདག་གིས་རྩོན༌[^2746]འགྲུས་ནི་དགེ་བ་བྱེད་པ་ལ་སེམས་སྤྲོ་བའོ། །

[Block 3182]
མཐུ་ནི་བདུད་ལ་སོགས་པས་བར་ཆད་བྱེད་མི་ནུས་པའོ། །

[Block 3183]
སྟོབས་ནི་ལེ་ལོས༌[^2747]མི་ཚུགས་པའོ། །

[Block 3184]
གཞན་གྱི་གོ་སྐབས་མེད་པ་ཞེས་བྱ་བ་ནི། གཞན་གྱིས་གྲོགས་བྱ་མི་དགོས་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3185]
བདག་གི་མཐུ་སྟོབས་ཀྱིས་འཕགས་པ་ཞེས་བྱ་བ་ནི་བདག་གི༌[^2748]མཐུས་འབྱུང་ཞིང་ཀུན་ལ་ཁྱད་ཞུགས་པར་བྱ་སྟེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3186]
སེམས་ཅན་ཐམས་ཅད་ཀྱིས་ཡོངས་སུ་ཐོབ་པར་བྱ་བ་ནི་གང་རིག་པའི་གནས་དང་། བཟོའི་གནས་དང་། ལོངས་སྤྱོད་ལ་སོགས་པའོ། །

[Block 3187]
གང་འཕགས་པ་ཐམས་ཅད་དང་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་དང་། རང་སངས་རྒྱས་དང་། བྱང་ཆུབ་སེམས་དཔའ་ས་ལ་ཞུགས་པ་དང་། དེ་བཞིན་གཤེགས་པ་དག་གོ། །

[Block 3188]
ཐེག་པ་ལ་གསར་དུ་ཞུགས་པ་ནི་དང་པོ་ཉིད་དུ་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའམ། མོས་པས་སྤྱོད་པའི་ས་ལ་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སོ། །

[Block 3189]
ཐོབ་པར་བྱ་བ་ནི་དེ་དག་གིས༌[^2749]ཐོབ་པར་བྱ་བའི་ཡོན་ཏན་དྲན་བ་ཉེ་བར་གཞག་པ་དང་། ཡང་དག་པའི་སྤོང་བ་ལ་སོགས་པ་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི༌[^2750]ཆོས་སུམ་ཅུ་རྩ་བདུན་དང་། ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པའོ། །

[Block 3190 [HEADING]]
### བཟོད་པ་ཐོབ་པ། ^11-2-0
--- END BLOCKS ---
