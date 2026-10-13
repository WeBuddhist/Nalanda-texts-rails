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
འདི་སྙམ་དུ་འདི་ནི་འགྲོ་བ་མ་ལུས་པའི་སྐྱབས་དང་དཔུང་གཉེན་ཡིན་ནོ་སྙམ་དུ་བླ་མ་ལ་སྟོན་པའི་འདུ་ཤེས་བསྐྱེད་ལ། ཁྲུས་བྱས་ཏེ་གོས་གཙང་མ་བགོས་ལ་བསམ་པ་བཟང་པོ་དང་ལྡན་པས་འདི་སྐད་དུ་རིགས་ཀྱི་བུ་ཁྱོད་མཁྱེན་པར་མཛད་དུ་གསོལ། བདག་འཁོར་བའི་གནས་འདིར་ཐོག་མ་མེད་པའི་དུས་ནས་སྡུག་བསྔལ་དུ་མས་གཙེས་ཤིང་ཤིན་ཏུ་ཉམ་ཐག་པར་གྱུར་ཏེ། མགོན་མ་མཆིས་པ། སྐྱབས་མ་མཆིས་པ། དཔུང་གཉེན་མ་མཆིས་པ། བདག་གི༌[^88]མགོན་དང་སྐྱབས་དང་དཔུང་གཉེན་མཛད་དུ་གསོལ་ཞེས་ལན་གསུམ་དུ་བྱའོ། །

[Block 177]
དེ་ནས་བླ་མ་དེས་འདི་སྐད་དུ་སྐྱེས་བུ་ཁྱོད་འཁོར་བ་ལས་སྐྱོ་ཞིང་ཡིད་བྱུང་བས་ཤིང་རྟ་ཆེན་པོའི་ལམ་ལ་འཇུག་པར་འདོད་པ་ཤིན་ཏུ་ལེགས་སོ། །

[Block 178]
འདི་ལྟར་ཤེས་པར་གྱིས་ཤིག །དཀོན་མཆོག་གསུམ་ཞེས་བྱ་བ་མགོན་མེད་པ་དང་། སྐྱབས་མེད་པ་དང་། དཔུང་གཉེན་མེད་པ་དག་གི༌[^89]མགོན་དང་། སྐྱབས་དང་དཔུང་གཉེན་དུ་གྱུར་པ་ཡོད་ཀྱི།[^90] ཁྱོད་དང་བའི་ཡིད་དང་། ཤིན་ཏུ་སྤྲོ་བའི་ཡིད་ཀྱིས་འགྲོ་བ་མཐའ་དག་ཡུལ་དུ་བྱས་ཏེ། དེ་ལས་སྐྱབས་སུ་འགྲོ་བ་གྱིས་ཤིག །དེ་ལ་སྲི༌[^91]ཞུ་དང་། བསྙེན་བཀུར་ཚུལ་བཞིན་དུ་བྱ་བའི་ཕྱིར་མཆོད་པའི་ཡོ་བྱད་འབྱོར་པ་ཅི་ཡོད་པས་ཚོགས་པར་གྱིས་ཤིག་ཅེས་བརྗོད་པར་བྱའོ། །

[Block 179]
དེ་ནས་སློབ་མ་དེས་པུས་མོ་གཉིས་ས་ལ་བཙུགས་ཤིང་ཐལ་མོ་སྦྱར་ནས་མེ་ཏོག་ཕུལ་ཏེ། འདི་སྐད་དུ།

[Block 180 [VERSE]]
སྐྱེས་བུ་གཙོ་བོ་དགོངས་སུ་གསོལ། །
ཐོག་མ་མེད་ནས་འདི་བར་དུ། །
བདག་ནི་འཁོར་བར་འཁོར་གྱུར་ཏེ། །
སྡུག་བསྔལ་རྣམས་ཀྱིས༌[^92]ཤིན་ཏུ་དུབ། །

[Block 181]
གང་གིས་སྡུག་བསྔལ་མཐར་འབྱིན་པའི། །ལམ་དེ་ཁྱོད་ཀྱིས་བསྟན་དུ་གསོལ། །ཞེས་ལན་གསུམ་དུ་བརྗོད་པར་བྱའོ། །

[Block 182]
དེ་ནས་བླ་མ་དེས་ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་ཀྱི་དཀོན་མཆོག་ཐམས་ཅད་ཡུལ་དུ་བྱས་ལ། ལུས་ཀྱི་བཀོད་པ་བརྗོད་དུ་མེད་པར་མོས་ལ། ལུས་རེ་རེ་ལ་མགོ་བརྗོད་དུ་མེད་པ་དང་། [^93]མགོ་རེ་རེ་ལ་ལྕེ་བརྗོད་དུ་མེད་པར་མོས་ཏེ། སྔར་བརྗོད་པའི་ལུས་དང་ངག་གི་མཆོད་པ་དང་། ཟང་ཟིང་གི་མཆོད་པ་རྒྱ་ཆེ་བ་དང་། སྡིག་པ་བཤགས་པ་དང་། རྗེས་སུ་ཡི་རང་བ་དང་། བསྐུལ་བ་དང་། གསོལ་བ་གདབ་པ་དང་། ཡོངས་སུ་བསྔོ་བ་དག་ནི་མཆོད་པ་རྣམ་པ་བདུན་ཞེས་བྱ་བ་ཡིན་ལ། མཆོད་པ་རྣམ་པ་བདུན་པོ་དེའི་རྗེས་ལ་སྐྱབས་སུ་འགྲོ་བ་བྱའོ། །

[Block 183 [HEADING]]
### བསླབ་པ། ^2-4-0

[Block 184]
དེ་ལྟར་སྐྱབས་སུ་སོང་བ་དེས་སྐྱབས་སུ་འགྲོ་བའི་བསླབ་པ་བསྲུང་བར་བྱ་སྟེ། ལྷ་གཞན་ལ་ཕྱག་མི་བཙལ་བ་དང་། གཞན་ལ་གནོད་པ་དང་འཚེ་བ་སྤང་བ་དང་། མུ་སྟེགས་ཅན་དང་མི་འགྲོགས་ཤིང་དེ་དག་ལ་བསྙེན་བཀུར་མི་བྱ་བ་དང་། དཀོན་མཆོག་གསུམ་གྱི་ཁྱད་པར་དང་། ཡོན་ཏན་རྗེས་སུ་དྲན་པས་ཡང་དང་ཡང་དུ་སྐྱབས་སུ་འགྲོ་བ་དང་། བཀའ་དྲིན་ཆེན་པོ་རྗེས་སུ་དྲན་པས་དུས་རྟག་ཏུ་མཆོད་པ་ལ་བརྩོན་ཞིང་བཟའ་བ་དང་བཏུང་བའི་ཕུད་ཀྱང་དབུལ་བ་དང་། སྙིང་རྗེ་རྗེས་སུ་དྲན་པས་འགྲོ་བ་གཞན་ཡང་ཚུལ་འདི་ལྟ་བུ་ལ་ཉེ་བར་དགོད་པ་དང་། བྱ་བ་གང་བྱེད་པ་དང་། དགོས་པ་ཅི་ཡོད་པ་ན་དཀོན་མཆོག་གསུམ་ལ་མཆོད་ནས་གསོལ་བ་འདེབས་ཤིང་འཇིག་རྟེན་པའི་ཐབས་གཞན་སྤང་བའོ།[^94] །

[Block 185 [HEADING]]
### ཕན་ཡོན། ^2-5-0

[Block 186]
ཕན་ཡོན་ནི་གསུམ་འཐོབ་སྟེ། འདི་ལྟར་རྒྱུའི་དུས་དང་། ལམ་གྱི་དུས་དང་། འབྲས་བུའི་དུས་སོ། །

[Block 187 [HEADING]]
#### དང་པོ་རྒྱུའི་དུས། ^2-5-1-0

[Block 188]
དང་པོ་ནི་ཚེ་རབས་འདི་དང་གཞན་གྱི་ཕན་ཡོན་ཏེ་བླ་མ་ལས་ཤེས་པར་བྱའོ། །

[Block 189]
དེ་ལྟར་སྐྱབས་སུ་སོང་བའི་ཕན་ཡོན་ཤེས་པ་དེས་ཉིན་ལན་གསུམ་དང་མཚན་ལན་གསུམ་དུ་སྐྱབས་སུ་འགྲོ་བར་བྱ་ཞིང་།[^95] དཀོན་མཆོག་གསུམ་ཐ་ན་བཞད་གད་ཀྱི་ཕྱིར་རམ། སྲོག་གི་ཕྱིར་གཏང་བར༌[^96]མི་བྱ་ཞིང་བསྲུང་བར་བྱའོ། །

[Block 190]
དེ་ལྟར་སྐྱབས་སུ་འགྲོ་བ་ཁྱད་པར་ཅན་བསྟན་ནས། ད་ནི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་བསྟན་པའི་ཕྱིར། དེ་ནས་སེམས་ཅན་ཐམས་ཅད་ལ་ཞེས་པ་ལ་སོགས་པ་ཚིག་རྐང་སུམ་ཅུ་རྩ་བཞིས་བསྟན་ཏེ། དེ་ནས་ཞེས་པ་ནི་སྐྱབས་སུ་འགྲོ་བ་བྱས་ནས་ཞེས་བྱའོ། །

[Block 191]
སེམས་ཅན་ཐམས་ཅད་ཅེས་པས་ནི་སེམས་བསྐྱེད་པའི་དམིགས་པ་བསྟན་ཏེ། དེ་ཡང་སེམས་ཅན་ནི་འདི་ཙམ་དུ་ཟད་དོ་ཞེས་ཚད་གཟུང་བར༌[^97]མི་ནུས་ཏེ། མདོ་ལས་གལ་ཏེ་ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི༌[^98]ཁམས་ཐམས་ཅད་ཆུའི་དཀྱིལ་འཁོར་དུ་གྱུར་ལ། སྐྱེས་བུ་ཞིག་གིས༌[^99]ལོ་བརྒྱ་ཕྲག་སྟོང་སྟོང་ན་སྤུའི་རྩེ་མོ་ཞིག་གིས༌[^100]ཆུ་དེ་ལས་འཐོར་བར་བྱེད་ན་ཆུའི་དཀྱིལ་འཁོར༌[^101]ནི་ཟད་པར་འགྱུར་གྱི།[^102] སེམས་ཅན་གྱི་ཁམས་ནི་ཟད་པར་འགྱུར་བ་མེད་དོ་ཞེས་གསུངས་པ་དང་། འཕགས་པ་ཀུན་དུ་བཟང་པོའི་སྤྱོད་པའི་སྨོན་ལམ་གྱི་རྒྱལ་པོ་ལས་ཀྱང་།

[Block 192]
ནམ་མཁའི་མཐར་ཐུག་གྱུར་པ་ཇི་ཙམ་པར། །སེམས་ཅན་མ་ལུས་མཐའ་ཡང་དེ་ཙམ་མོ། །ཞེས་གསུངས་སོ། །

[Block 193]
དེ་ལྟ་བུའི་སེམས་ཅན་ཡུལ་དུ་བྱས་ནས་སེམས་བསྐྱེད་པར་བྱའོ། །

[Block 194]
བྱམས་པའི་སེམས་ནི་སྔོན་འགྲོ་བས། །ཞེས་པ་ནི་མར་འདུ་ཤེས་པ་ལས་དྲིན་དུ་གཟོ་བའི༌[^103]སེམས་འབྱུང་བ་ནི་བྱམས་པའོ། །

[Block 195]
བྱམས་པའི་སེམས་ལས་སྙིང་རྗེའི་སེམས་འབྱུང་ལ་སྙིང་རྗེའི་སེམས་ལས་བྱང་ཆུབ་ཀྱི་སེམས་འབྱུང་བས་ན་བདག་གིས་འདིར། བྱམས་པའི་སེམས་ནི་སྔོན་འགྲོ་བས། །ཞེས་སྨྲས་སོ། །

[Block 196]
ཚིག་རྐང་པ་བདུན་ནི་དཀྱུས་ཇི་ལྟ་བ་ཉིད་དོ། །

[Block 197]
བྱང་ཆུབ་སེམས་ནི་བསྐྱེད་པར་བྱ། །ཞེས་བྱ་བ་ནི་གསུམ་ལ་སྐྱབས་སུ་འགྲོ་བ་བྱས་པའི་རྗེས༌[^104]ལ་ཡང་བདག་ལ་འབྱོར་པ་ཅི་ཡོད་པས་དཀོན་མཆོག་གསུམ་དང་བླ་མ་དགེ་བའི་བཤེས་གཉེན་ལ་མཆོད་པ་དབུལ་བ་ཚུལ་བཞིན་དུ་བྱས་ལ། བླ་མའི་སྤྱན་སྔར་མཎྜལ་བྱས་ཏེ། བསམ་པ་བཟང་པོ་གཡོ་སྒྱུ་དང་བྲལ་བས་བླ་མ་འདི་ནི་སངས་རྒྱས་མངོན་སུམ་ན་བཞུགས་པ་ཉིད་ཡིན་ནོ་སྙམ་དུ་བསམས་ལ། དུས་གསུམ་གྱི༌[^105]སངས་རྒྱས་ཐམས་ཅད་ཀྱིས་མཛད་པ་དེ་དག་མ་ལུས་པར་བདག་གིས་རྫོགས་པར་བྱའོ་ཞེས་བསམས་ལ། པུས་མོ་གཉིས་ས་ལ་བཙུགས་པས་མེ་ཏོག་ཕུལ་ལ། ཐལ་མོ་ལེགས་པར་སྦྱར་ལ་འདི་སྐད་དུ།

[Block 198 [VERSE]]
ཀུན་མཁྱེན་ཡེ་ཤེས་ཕུང་པོ་ཅན། །
སྲིད་པའི་འཁོར་ལོ་རྣམ་སྦྱོང་བ། །
ཁྱོད་ཞབས་པདྨ་སྤངས་ནས་ནི། །
གཙོ་བོ་གཞན་ལ་སྐྱབས་མ་མཆིས། །

[Block 199 [VERSE]]
འགྲོ་བའི་དཔའ་བོ་ཐུབ་ཆེན་གྱིས། །
བདག་ལ་བཀའ་དྲིན་སྩལ་དུ་གསོལ། །
བྱང་ཆུབ་སེམས་མཆོག་བླ་མེད་པ། །
དམ་པ་དེ་ནི་བདག་ལ་སྩོལ། །

[Block 200]
ཞེས་ལན་གསུམ་དུ་བརྗོད་པར་བྱའོ། །

[Block 201]
དེ་ནས་བླ་མ་དགེ་བའི་བཤེས་གཉེན་དེས་ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་ཀྱི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་དང་། བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ས་ཆེན་པོ་ལ་བཞུགས་པ་ཐམས་ཅད་དང་། སྔོན་དང་ད་ལྟར་གྱི༌[^106]བླ་མ་དགེ་བའི་བཤེས་གཉེན་དག་སྤྱན་དྲངས་ཏེ། དེ་དག་གི་སྤྱན་སྔར་འཕགས་པ་བཟང་པོ་སྤྱོད་པ་དང་། བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པའི་ཆོ་གས་རྒྱུད་ལེགས་པར་དག་པར་བྱའོ། །

[Block 202]
དེ་ལྟར་སྣོད་ཤིན་ཏུ་སྦྱངས་ནས་བླ་མ་ལ་སློབ་མ་དེས་ཡང་ལག་པ་མེ་ཏོག་དང་བཅས་པས་གསོལ་བ་གདབ་པར་བྱའོ། །

[Block 203]
བླ་མ་དེས་རྙེད་པ་དང་། བཀུར་སྟི་དང་། གྲགས་པ་དང་། སྒྲ་དང་། ཚིགས་སུ་བཅད་པ་དང་། ཟང་ཟིང་དང་བཅས་པའི་སེམས་མེད་པས་འདི་སྙམ་དུ། ཨེ་མ་ངོ་མཚར་རོ། །

[Block 204]
འཇིགས་པ་ཆེན་པོའི་དུས་འདིར་འདི་ལྟ་བུའི་སེམས་ཅན་དམ་པ་འབྱུང་བ་ནི་ངོ་མཚར་རོ་ཞེས་བསམ་པ་དང་། ལྷག་པའི་བསམ་པ་བཟང་པོས་ཆོ་ག་བྱའོ། །

[Block 205 [HEADING]]
## སྔོན་གྱི་སློབ་དཔོན་རྣམས་ཀྱི་དགོངས་པ་ཐ་དད་པ། ^3-0

[Block 206]
དེ་ཡང་འཛམ་བུའི་གླིང་ནི་སྔོན་གྱི་སློབ་དཔོན་རྣམས་ཀྱི་དགོངས་པ་ཐ་དད་པར་གྱུར་ཏེ། སློབ་དཔོན་རྒྱལ་པོ་ཨིནྡྲ་བྷཱུ་ཏི་དང་། སློབ་དཔོན་འཕགས་པ་ཀླུ་སྒྲུབ་དང་། སློབ་དཔོན་འཕགས་པ་ཤཱན་ཏ་དེ་བ་དང་།[^107] སློབ་དཔོན་འཕགས་པ་ཙནྡྲ་གོ་མི་དང་། སློབ་དཔོན་དཾཥྚྲ་སེ་ན་དང་། སློབ་དཔོན་དཔའ་བོ་དང་། སློབ་དཔོན་ཤཱན་ཏ་ར་ཏེ་ལ་སོགས་པ་མཁས་པ་ཆེན་པོ་དེ་དག་གི༌[^108]དགོངས་པ་ནི་འདི་ལྟར་ཐ་དད་པར་འགྱུར་ཏེ། དང་པོར་ནི་བྱང་ཆུབ་ཀྱི་སེམས་དེ་ཉིད་ལ་ཐ་དད་པར་གྱུར་ཏོ། །

[Block 207]
གཉིས་པར་ནི་བྱང་ཆུབ་ཀྱི་སེམས་དེའི་ཆོ་ག་ལ་ཐ་དད་པར་གྱུར་ཏོ། །

[Block 208]
གསུམ་པར་ནི་བྱང་ཆུབ་ཀྱི་སེམས་དེ་སྐྱེ་བའི་ཚུལ་ལའོ། །

[Block 209 [HEADING]]
### དང་པོ་བྱང་ཆུབ་ཀྱི་སེམས་དེ་ཉིད། ^3-1-0

[Block 210]
བཞི་པར་ནི་སེམས་དེའི་བསླབ་བྱའི་ཚུལ་ལ་ཐ་དད་པར་གྱུར་ཏེ། དོན་དང་པོ་དེ་ལ་སློབ་དཔོན་ཁ་ཅིག་གི་ཞལ་ནས་མོས་པས་སྤྱོད་པ་པ༌[^109]འཇིག་རྟེན་པའི་ལམ་གྱིས་བསྡུས་པའི་སེམས་དེ་ནི་སྨོན་པའི་སེམས་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 211]
ལ་ལའི་ཞལ་ནས་ནི༌[^110]ཇི་སྲིད་དམིགས་པ་དང་བཅས་པའི་སེམས་དེ་ནི་ཀུན་རྫོབ་ཀྱི་རྣམ་པ་སྟེ། སྨོན་པའི་སེམས་སོ་ཞེས་བཞེད་དོ། །

[Block 212]
གཞན་ནི་ཚོགས་ཀྱི་ལམ་པ་ཐར་པའི་ཆ་དང་མཐུན་པའི་དགེ་བའི་རྩ་བ་བསྐྱེད་པའི་སེམས་དེ་ནི་སྨོན་པའི་སེམས་ཡིན་ནོ་ཞེས་བཞེད་དོ། །

[Block 213]
ཁ་ཅིག་ནི་བསོད་ནམས་མངོན་པར་འདུ་བྱ་བ་དང་མི་ལྡན་པའི་སེམས་ནི་སྨོན་པའི་སེམས་ཡིན་ནོ་ཞེས་བཞེད་དོ། །

[Block 214]
ལ་ལ་ནི། འགྲོ་བར་འདོད་དང་འགྲོ་བ་ཡི། །ཞེས་པས་རྫོགས་པའི་བྱང་ཆུབ་ཡུལ་དུ་བྱེད་པ་ཙམ་དེ་ནི་སྨོན་པའི་སེམས་ཡིན་ནོ་ཞེས་བཞེད་དོ། །

[Block 215]
དེ་མ་ཡིན་པ་གཞན་ཡང་ཡོད་དེ་གཞུང་མངས་པར་འགྱུར་རོ། །
--- END BLOCKS ---
