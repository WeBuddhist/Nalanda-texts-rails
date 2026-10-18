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
[Block 2801]
ཆོས་ཐམས་ཅད་གནས་པ་མེད་པ་ཞེས་བྱ་བ་ནི་མི་གནས་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2802]
འཇུག་པ་མེད་པ་ནི་ངེས་པར་འབྱུང་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2803]
དེ་དག་གིས་ནི་ཆོས་འདི་དག་ལས་གང་ལ་གནས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ཡང་དག་པར་འཇུག་ཅེས་གང་སྨྲས་པ་དེ་ལ་གནས་ཏེ་ཞེས་བྱ་བ་དང་། འཇུག་པ་ཞེས་བྱ་བ་འདིས༌[^2017]གཉིས་ཉེ་བར་བརྟགས་པ༌[^2018]སྟོན་ཏོ། །

[Block 2804 [HEADING]]
###### སྒྲིབ་པ་མེད་པ། ^1-2-7-56-4-0

[Block 2805]
དེས་ཆོས་གང་ལ་སྒྲིབ་པ་ཡང་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་སྟེ་ཞེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་ལ་ཆགས་པའོ། །

[Block 2806]
དེས་ཆོས་ཐམས་ཅད་སྒྲིབ་པ་མེད་པར་ཡང་དག་པར་རྗེས་སུ་མཐོང་ངོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་སྟོང་པར་མཐོང་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2807 [HEADING]]
##### རང་བཞིན་སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་ཉིད། ^1-2-7-57-0

[Block 2808]
དེའི་འོག་ཏུ་གང་ལ་བདག་མི་དམིགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་རང་བཞིན་སྟོང་པ་ཉིད་ཀྱི༌[^2019]ངོ་བོ་ཉིད་སྟོན་ཏེ། དེ་ལ་འདི་ནི༌[^2020]རང་བཞིན་སྟོང་པ་ཉིད་དོ། །

[Block 2809]
རང་བཞིན་སྟོང་པ་ཉིད་ཅེས་བྱ་བ་ནི་གང་ཟག་ལ་བདག་མེད་པ་དང་། ཆོས་ལ་བདག་མེད་པ་ཡང་བསྟན་ཏེ། བདག་མེད་པ་དེ་གཉིས་ཀྱང་དེ་བཞིན་གཤེགས་པས་སྤྲུལ་པའི་དགེ་སློང་དང་། དགེ་སློང་མའི་དཔེས་བསྒྲུབ་པའོ། །

[Block 2810]
ཕྱིན་ཅི་ལོག་གང་ཡིན་པ་དེ་ཉིད་ཕྱིན་ཅི་ལོག་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་གནས་དེ་ཉིད་སྔོན་ཀུན་བརྟགས་པའི་གནས་སྐབས་ན་ནི་ཕྱིན་ཅི་ལོག་ཅེས་བྱའོ། །

[Block 2811]
ཡོངས་སུ་དག་པའི་གནས་སྐབས་ན་ནི་ཕྱིན་ཅི་མ་ལོག་པའོ། །

[Block 2812]
རྟོག་པའི་རྒྱུ་མཐུན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཀུན་རྟོག༌[^2021]པའི་འབྲས་བུ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2813]
དེ་ཡང་དེ་ལ་དོན་དམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་ནི་མ་ཡིན་ཞེས་བྱ་བ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་ཡང་ཀུན་བརྟགས་པ༌[^2022]ཡིན་གྱི། དོན་དམ་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། རང་བཞིན་སྟོང་པ་ཉིད་དེ་ཡང་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 2814]
རང་བཞིན་སྟོང་པ་ཉིད་དེ་ཡང་སྔོན་གྱི་མཐར་ཡང་རང་བཞིན་སྟོང་པ་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པས་དུས་གསུམ་ཅར་དུ་ཡང་སྟོང་པ་ཉིད་ཡིན་ནོ་ཞེས་སྟོན་ཏོ། །

[Block 2815]
འདི་ལྟར་རང་བཞིན་སྟོང་པ་ཉིད་ཀྱི་ཆོས་རྣམས་ལ་ཡང་སྤྱོད་ཅིང་རང་བཞིན་སྟོང་པ་ཉིད་དེ་ཡང་རྣམ་པར་འཁྲུག་པར་མི་བགྱིད་པ་དེ་ངོ་མཚར་ཏོ་ཞེས་བྱ་བ་ནི་ཡོད་པ་མ་ཡིན་པའི་ཆོས་རྣམས་ལ་སྤྱོད་ན། འཁྲུགས༌[^2023]པར་འགྱུར་བར་དགོངས་པའོ། །

[Block 2816]
དེ་བས་ན་གཟུགས་ཀྱང་གཞན་མ་ཡིན་རང་བཞིན་སྟོང་པ་ཉིད་ཀྱང་གཞན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་གསོལ་ཏེ་འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་ལ་སྤྱོད་པ་ན་གཟུགས་ལ་སོགས་པ་དེ་དག་གཞན་ལ་རང་བཞིན་སྟོང་པ་ཉིད་ཀྱང་གཞན་ནོ་ཞེས་བྱ་བ་མེད་ཀྱི། གཟུགས་ལ་སོགས་པ་དེ་དག་ཉིད་སྟོང་པ་ཉིད་དུ་མཐོང་བ་དེ་ངོ་མཚར་ཏོ་ཞེས་བྱའོ། །

[Block 2817]
གཟུགས་ཉིད་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་དུ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འགྱུར་ཞེས་བྱ་བ་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་དུས་ན་གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་མངོན་པར་རྫོགས་པར་རྟོགས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2818]
དེ་དག་ལ་ཐ་དད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2819]
གཞན་དུ་ན་ལྷ་དང་བཅས། བདུད་དང་བཅས། ཚངས་པ་དང་བཅས་པའི་འཇིག་རྟེན་ཞེས་བྱ་བ་ལ། གཞན་དུ་ན་ཞེས་བྱ་བ་ནི་གཅིག་ཁོ་ནར་ཏེ་ཞེས་བྱ་བ་སྟེ། འཇིག་རྟེན་པ་རྣམས་གཅིག་ཁོ་ནར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་མི་ཤེས་ཏེ། མི་ཤེས་པས། དེ་ལ་མངོན་པར་ཞེན་ནས་ལས་བསགས་ཏེ། གཟུགས་ལ་སོགས་པའི་རྣམ་པར་སྨིན་པ༌[^2024]ཡོངས་སུ་འཛིན་ཅིང་ཉེ་བར་ལེན་ཏོ། །

[Block 2820]
ཉེ་བར་ལེན་པའི་རྒྱུས་ཀྱང་སྲིད་པར་འགྱུར་ཏེ། སྡུག་བསྔལ་ལས་ཡོངས་སུ་མི་འགྲོལ་ལོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2821]
རང་བཞིན་སྟོང་པ་ཉིད་ནི་སྟོང་པའམ་མི་སྟོང་པ་ཞེས་བྱ་བར་གཟུགས་རྣམ་པར་འཁྲུག་པར༌[^2025]མི་བྱེད་དོ་ཞེས་བྱ་བ་ནི་གཉིས་སུ་འདུ་ཤེས་པས་གཟུགས་སྟོང་པ་ཉིད་རྣམ་པར་འཁྲུག་པར༌[^2026]མི་བྱེད་དོ་ཞེས་བྱ་བ་སྟེ། གཉིས་སུ་མེད་པའི་ཕྱིར་རོ། །

[Block 2822]
དེ་དག་ལ་གང་འདི་ལྟར་འདི་ནི་གཟུགས་སོ། །

[Block 2823]
འདི་ནི་སྟོང་པའོ་ཞེས་རྣམ་པར་འཁྲུག་པར་བྱེད་པ་དེ་ལྟ་བུའི་རང་བཞིན་མེད་དོ་ཞེས་བྱ་བ་ནི། དངོས་པོའི་བདག་ཉིད་ཀྱི་ངོ་བོ་ཉིད་མེད་པའོ། །

[Block 2824]
བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་གཉིས་སུ་དབྱེ་བས་བྱང་ཆུབ་དང་གཟུགས་ལ་མི་སྤྱོད་དོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ལ་གཉིས་སུ་བྱས་ནས་གཟུགས་ལ་མི་སྤྱོད་དེ། བྱང་ཆུབ་སེམས་དཔའ་བྱང་ཆུབ་ལ་སྤྱོད་ཅེས་བྱ་བར་བྱང་ཆུབ་སེམས་དཔའ་དང་། བྱང་ཆུབ་ཀྱང་གཉིས་སུ་བྱས་ནས་གཟུགས་ལ་མི་སྤྱོད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2825]
རབ་འབྱོར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ནི་བདག་བྱང་ཆུབ་དང་གཟུགས་ལ་སྤྱོད་དོ་སྙམ་དུ་མི་སེམས་སོ་ཞེས་བྱ་བ་ནི་བདག་བྱང་ཆུབ་ལ་སྤྱོད་དོ་སྙམ་ནས་གཉིས་སུ་བྱས་ཏེ་གཟུགས་ལ་མི་སྤྱོད་པའོ། །

[Block 2826]
འཛིན་པ་ལ་སྤྱོད་ཅེས་བྱ་བ་ནི་མཚན་མ་ལ་སྤྱོད་པའོ། །

[Block 2827]
གཟུགས་ཀྱི་རང་བཞིན་ལ་གནས་ཏེ་ཞེས་བྱ་བ་ནི་གཟུགས་ཀྱི་སྟོང་པ་ཉིད་ལ་གནས་པའོ། །

[Block 2828]
དེ་ཡང་འཇིག་རྟེན་གྱི་ཐ་སྙད་དུ་བཏགས་པ་ཉེ་བར་བཟུང་ནས་ཞེས་བྱ་བ་ནི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཀྱང་དོན་དམ་པར་མེད་དོ་ཞེས་བསྟན་པའོ། །

[Block 2829]
ཆོས་དེ་དག་ཉིད་ལ་སྤྱོད་ཅེས་བྱ་བ་ནི་སྦྱིན་པ་དང་། སྦྱིན་བདག་ལ་སོགས་པ་མི་དམིགས་སུ་ཟིན་ཀྱང་སྦྱིན་པ་ལ་སོགས་པ་དེ་དག་ཉིད་ལ་སྤྱོད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2830]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཚེ། བྱང་ཆུབ་ཀྱི་ལམ་ལ་བརྩོན་པར་བགྱིད་པ་ལགས་ཞེས་བྱ་བ་ནི་གལ་ཏེ་བྱང་ཆུབ་ཀྱི་ལམ་ཐམས་ཅད་ཡོད་པ་མ་ཡིན་ནོ༌[^2027]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2831]
གཟུགས་མི་སྦྱོར་མི་འབྱེད་དེ་ཞེས་བྱ་བ་ནི་གཟུགས་ལ་སོགས་པ་མེད་པའི་ཕྱིར་རོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཇི་ལྟར་མངོན་པར་འགྲུབ་པར་འགྱུར་ཞེས་བྱ་བ་ནི་དེ་མེད་པའི་ཕྱིར་རོ། །

[Block 2832]
ཐབས་མཁས་པ་བཤད་པ་དང་། གཟུང་དུ་མེད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བཤད་པ་དག་ནི་གོ་སླའོ། །

[Block 2833]
ཇི་ལྟར་བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་མངོན་པར་ཞེན་པར་གྱུར་པ་ལྟ་བུའི་དངོས་པོ་ཡོད་པར་གྱུར་ཏམ། ཡོད་པར་འགྱུར་རམ་ཞེས་སྨོས་པ་ནི་དུས་གསུམ་ཅར་གྱི་སྨོས་པའོ། །

[Block 2834]
གལ་ཏེ་སྔོན་དངོས་པོ་ཡོད་པར་གྱུར༌[^2028]ལ་ཞེས་བྱ་བ་ནི་སྔོན་ནི་དེ་དག༌[^2029]ཐམས་ཅད་ཡོད་པར་བཟུང་ལ། ཕྱིས་མེད་པར་བཟུང་ན་ནི་ཉེས་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2835]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོའི་ལམ་གང་ལགས་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱ་བ་དང་། སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་བྱ་བས་བསྡུས་པའི་ལམ་ཞུས་པའོ། །

[Block 2836]
དེའི་འོག་ཏུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་བཤད་པ་དང་། ལམ་བཤད་པ་དང་། ཆོས་ཐམས་ཅད་ལ་བསླབ་པར༌[^2030]བཤད་པ་དང་། མི་གནས༌[^2031]བཤད་པ་རྣམས་ནི་གཞུང་གི་རྗེས་སུ་བསྙགས་ཏེ་གཟུང་ངོ་། །བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཐམས་ཅད་སྐྱེ་བ་མ་མཆིས་པ་ལགས་ན། འོ་ན་ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་བྱང་ཆུབ་ཀྱི་ལམ་སྐྱེས་པར༌[^2032]བགྱིད་ཅེས་བྱ་བ་ནི་མ་སྐྱེས་པ་རྣམས་བསྐྱེད་པར་བྱ་ཞེས་བྱ་བའི༌[^2033]ཚིག་མི་རིགས་སོ་སྙམ་དུ་དགོངས་པའོ། །

[Block 2837]
ཆོས་ཐམས་ཅད་ནི་མ་སྐྱེས་པ་སྟེ། དེ་ཡང་ཇི་ལྟ་བུ་ཞེ་ན་གང་དག་མངོན་པར་འདུ་མི་བྱེད་པ་དེ་དག་ལ་ནི་ཆོས་ཐམས་ཅད་མ་སྐྱེས་པའོ་ཞེས་བྱ་བ༌[^2034]གང་དག་རྣམ་པར་མི་རྟོག་པའི་ཏིང་ངེ་འཛིན་ལ་གནས་ནས་བསོད་ནམས་དང༌[^2035]བསོད་ནམས་མ་ཡིན་པ་ལ་སོགས་པ་ཅི་ཡང་མངོན་པར་འདུ་མི་བྱེད་པ་དེ་དག་ཉིད་ལ་ནི་མ་སྐྱེས་པའོ། །

[Block 2838]
བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་གང་དག་ཡོངས་སུ་མི་ཤེས་པས་མངོན་པར་འདུ་བྱེད་པ་དེ་དག་ལ་ནི་ཆོས་ཐམས་ཅད་སྐྱེས་པ་ཉིད་དོ་ཞེས་གསུངས་པའོ། །

[Block 2839]
བཅོམ་ལྡན་འདས་འོ་ན་དེ་བཞིན་གཤེགས་པ་རྣམས་བྱུང་ཡང་རུང་དེ་བཞིན་གཤེགས་པ་རྣམས་མ༌[^2036]བྱུང་ཡང་རུང་ཞེས་བྱ་བ་ལ་སོགས་པས་གནས་བརྟན་གྱིས་འདི་སྐད་ཞུས་ཏེ། ཆོས་ཉིད་ནི་དུས་ཐམས་ཅད་དུ་རྣམ་པ་ཐམས་ཅད་དུ་ཕྱིན་ཅི་མ་ལོག་པའི་མཚན་ཉིད་ཡིན་ན། དེ་བྱིས་པ་རྣམས་ལ་ནི་སྐྱེ་བའི་ཆོས་ཅན་དུ་འགྱུར་ལ། མཁས་པ་རྣམས་ལ་ནི་མི་འགྱུར་བ་དེ་ཇི་ལྟར་རིགས་པར་འགྱུར་ཞེས་བྱའོ། །

[Block 2840]
དེ་སྐད༌[^2037]གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་རབ་འབྱོར་དེ་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི༌[^2038]བསྟན་ཏེ། ཆོས་ཉིད་ལ་ནི་ནམ་ཡང་ཕྱིན་ཅི་ལོག་ཡོད་པ་མ་ཡིན་གྱི། བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱིས༌[^2039]ཡོངས་སུ་མི་ཤེས་པའི་ཉེས་པས་ཀུན་བརྟགས་པའི་ཆོས་རྣམས་སྐྱེ་བར་འགྱུར་རོ་ཞེས་ཀུན་བརྟགས་པ་རྣམས་ཀྱི་ཀུན་བརྟགས་པ་ཉིད་སྐྱེ་བ་ལས་དགོངས་ཏེ་བཤད་ཀྱི། ཆོས་ཉིད་ལས་དགོངས་པ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
