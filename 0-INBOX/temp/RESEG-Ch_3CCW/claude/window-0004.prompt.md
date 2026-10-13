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
[Block 141]
དེ་བས་ན་མྱ་ངན་ལས་འདས་པ་ཡང་ཀུན་རྫོབ་ཀྱི་བདེན་པར་ཡོངས་སུ་བརྟགས་པ་ཡིན་ནོ། །

[Block 142]
གལ་ཏེ་དེ་ལྟར་ན་མྱ་ངན་ལས་འདས་པ་དོན་དམ་པའི་བདེན་པའོ་ཞེས་ཇི་སྐད་དུ་བཤད། དེའི་བདག་ཉིད་དུ་འཇིག་རྟེན་ལ་མི་སླུ་བའི༌[^92]ཕྱིར་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱིས་དོན་དམ་པའི་བདེན་པ་ཞེས་བཤད་དོ། །

[Block 143]
སླུ་བ༌[^93]འདུས་བྱས་གང་ཡིན་པ་དེ་ནི་དོན་དམ་པའི་བདེན་པ་མ་ཡིན་ནོ། །

[Block 144]
བདེན་པ་གསུམ་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དེ་ངོ་བོ་ཉིད་ཡོད་པར་སྣང་བས་བྱིས་པ་རྣམས་ལ་སླུ་བའི༌[^94]ཕྱིར་ཀུན་རྫོབ་ཀྱི་བདེན་པར་རྣམ་པར་གཞག་གོ། །

[Block 145]
འོ་ན་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་དག་འདི་ལྟ་སྟེ། མི་སླུ་བའི་ཆོས་ཅན་མྱ་ངན་ལས་འདས་པ་འདི་ནི་བདེན་པའི་མཆོག་གཅིག་པུའོ་ཞེས་གསུངས་པ་དེ་ཇི་ལྟ་བུ། ཇི་ལྟར་འདུས་བྱས་ལོག་པར་སྣང་བས་བྱིས་པ་རྣམས་ལ་སླུ་བ༌[^95]དེ་བཞིན་དུ་མྱ་ངན་ལས་འདས་པ་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། རྟག་པར་སྐྱེ་བ་མེད་པའི་རང་གི་ངོ་བོར་གནས་པའི་ཕྱིར་དེ་ནི་བྱིས་པ་རྣམས་ལ་འདུས་བྱས་ལྟར་སྐྱེ་བའི་ངོ་བོར་ནམ་ཡང་མི་སྣང་ངོ་། །དེ་བས་ན་མྱ་ངན་ལས་འདས་པ་ནི་རྟག་ཏུ་མྱ་ངན་ལས་འདས་པ་ཉིད་དུ་གནས་པས་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱིས་དོན་དམ་པའི་བདེན་པ་ཞེས་བཤད་དོ། །

[Block 146]
འཕགས་པ་དོན་དམ་པ་གཟིགས་པ་ལ་གནས་པ་རྣམས་ནི་འཁོར་བའམ་མྱ་ངན་ལས་འདས་པ་མི་དམིགས་ཏེ་དེའི་ཕྱིར་ཡང་དག༌[^96]མཐོང་བ་འཇིག་རྟེན་དང་མྱ་ངན་ལས་འདས་པར་རློམ་སེམས་མེད་ཅེས་བྱ་བ་གྲུབ་པོ། །ཅིའི་ཕྱིར་འཕགས་པ་དོན་དམ་པ་གཟིགས་པ་ལ་གནས་པ་དག་འཁོར་བའམ༌[^97]དོན་དམ་པ་དམིགས་པར་མི་འགྱུར་ཞེ་ན། འདི་ལྟར།

[Block 147 [HEADING]]
### ཚིགས་བཅད་དྲུག་པ། ^1-7-0

[Block 148 [VERSE]]
སྲིད་པ་དང་ནི་མྱ་ངན་འདས། །
དེ་གཉིས་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 149]
སྲིད་པ་ནི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་རྣམས་ཏེ། དེ་དག་ཀྱང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཕྱིར་གཟུགས་བརྙན་བཞིན་དུ་ངོ་བོ་ཉིད་ཀྱིས་མེད་པའོ། །

[Block 150]
དེ་དག་མེད་ན་དེའི་དངོས་པོ་མེད་པ་ཡང་ཤིན་ཏུ་མེད་པའི་ཕྱིར་དེ་གཉིས་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བཤད་དོ། །

[Block 151]
མེད་པ་མཐོང་བ་ནི་དེ་ཁོ་ན་མཐོང་བ་མ་ཡིན་ཏེ་རབ་རིབ་ཅན་ལ་སོགས་པས་ཀྱང་དེ་ཁོ་ན་མཐོང་བར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 152]
འཕགས་པ་རྣམས་ནི་དེ་ཁོ་ན་གཟིགས་པ་ཡིན་ཏེ། མེད་པའི་རང་གི་ངོ་བོ་གཟིགས༌[^98]པས་མི་འོས་སོ། །

[Block 153]
གལ་ཏེ་མྱ་ངན་ལས་འདས་པ་ཅི་ཡང་མེད་པ་ཞིག་ཡིན་ན། འཕགས་པ་རྣམས་མྱ་ངན་ལས་འདས་པ་ཐོབ་བོ་ཞེས་རྣམ་པར་གཞག་པ་དེ་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 154 [VERSE]]
སྲིད་པ་ཡོངས་སུ་ཤེས་པ་ནི། །
མྱ་ངན་འདས་ཞེས་བརྗོད་པ་ཡིན། །

[Block 155]
ཞེས་བྱ་བ་སྨོས༌[^99]སོ། །

[Block 156]
སྲིད་པ་དེ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་སྐྱེ་བ་མེད་པ་ཡོངས་སུ་མི་ཤེས་པའི་ཚུལ་གྱིས་ཡོངས་སུ་ཤེས་པ་གང་ཡིན་པ་དེ་ཉིད་མཚན་མ་ཐམས་ཅད་རབ་ཏུ་ཞི་བའི་ངོ་བོ་ཡིན་པས་ཐ་སྙད་ཀྱི་བདེན་པ་དང་སྦྱར་ནས་མྱ་ངན་ལས་འདས་པ་ཞེས་བྱ་བ་རང་གི་ངོ་བོར་གྲུབ་པ་ནི་གང་ཡང་མེད་པར་ཤེས་པར་བྱའོ། །

[Block 157]
ཇི་ལྟར་མི་རྟག་པ་ཉིད་དངོས་པོ་མེད་པའི་ངོ་བོ་རང་བཞིན་གྱིས་ཡོངས་སུ་གྲུབ་པ་མེད་པ་དེ་དངོས་པོ་ལ་མ་ལྟོས་པར་ངོ་བོ་ཉིད་ཀྱིས་ཡོངས་སུ་གྲུབ་པར་རྣམ་པར་གཞག་མི་ནུས་པ་དེ་བཞིན་དུ་མཁས་པ་ཡང་སྒྱུ་མ་བྱས་པ་ལྟ་བུའི་དངོས་པོ་ལ་མ་ལྟོས་པར་མྱ་ངན་ལས་འདས་པ་ཞེས་བྱ་བ་རང་བཞིན་གྱིས་གྲུབ་པ་གང་ཡང་ཡོངས་སུ་བརྟག་པར་མི་ནུས་སོ་ཞེས་བསྟན་པའི་ཕྱིར།

[Block 158 [HEADING]]
### ཚིགས་བཅད་བདུན་པ། ^1-8-0

[Block 159 [VERSE]]
དང་པོ༌[^100]སྐྱེས་པ་ཞིག་པ་ལ། །
ཇི་ལྟར་འགོག་པ་བརྟག་པ༌[^101]བཞིན། །
དེ་བཞིན་སྒྱུ་མ་བྱས་པ་ལྟར། །
མཁས་པ་དག་གིས་འགོག༌[^102]པར་དགོངས། །

[Block 160]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 161]
ཇི་ལྟར་དངོས་པོ་སྐྱེས་པའི་མི་རྟག་པ་ཉིད་དེ་མེད་པར་གྱུར་པས་རྣམ་པར་གཞག་པས་རང་གི་ངོ་བོར་གྲུབ་པ་མེད་དོ། །

[Block 162]
ཡོད་པ་ཞིག་ཡིན་ན་ནི་དངོས་པོ་ལ་མི་ལྟོས་པར་རང་གི་ངོ་བོ་མཐོང་བར་འགྱུར་རོ། །

[Block 163]
དེ་བཞིན་དུ་འཕགས་པ་ཡང་འགོག་པ་ཞེས་བྱ་བ་རང་གི་ངོ་བོར་གྲུབ་པ་གང་ཡང་མི་དམིགས་ཏེ། ཤེས་རབ་ཀྱིས་རྣམ་པར་དཔྱད་ན། སྒྱུ་མ་བྱས་པའི་གླང་པོ་ཆེ་ལྟར་ངོ་བོ་ཉིད་མེད་པ་རང་བཞིན་གྱིས་མ་སྐྱེས་པ་གང་ཡིན་པ་དེ་མྱ་ངན་ལས་འདས་པའོ། །

[Block 164]
དེ་ཡང་སྒྱུ་མ་བྱས་པ་ལྟ་བུ་ཞེས་བྱ་བ་དེ་ཉིད་ལ་བརྟེན་ནས་མྱ་ངན་ལས་འདས་པར་རྣམ་པར་གཞག་པ༌[^103]ན། འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱིས་མི་རྟག་པ་ཉིད་རྣམ་པར་འཇོག་གོ། །

[Block 165]
དེས་ན་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ཞེས་བྱ་བ་ངོ་བོ་ཉིད་མེད་པར་གྲུབ་པོ། །དེ་ལྟར་ན་དངོས་པོའི་ངོ་བོ་ཉིད་ཡོངས་སུ་ཤེས་ནས་མི་དམིགས་པ་གང་ཡིན་པ་དེ་ཉིད་མྱ་ངན་ལས་འདས་པར་གདོན་མི་ཟ་བར་ཤེས་པར་བྱའོ། །

[Block 166 [HEADING]]
### ཚིགས་བཅད་བརྒྱད་པ། ^1-9-0

[Block 167]
དེ་བཞིན་དུ་ན། རྣམ་པར་འཇིག་པས་འགོག་འགྱུར་གྱི།[^104] །འདུས་བྱས་ཤེས་པས་མ་ཡིན་ནོ།[^105] །

[Block 168 [VERSE]]
དེ་ནི་སུ་ལ་མངོན་སུམ་འགྱུར། །
ཞིག་ཅེས་པ་དེ་ཇི་ལྟ་བུ། །

[Block 169]
གལ་ཏེ་སྒྱུ་མ་བྱས་པ་བཞིན་དུ་ཆོས་ཐམས་ཅད་མི་དམིགས་པའི་དུས་ན་སྐྱེ་བ་མེད་པ་གང་ཡིན་པ་དེ་མྱ་ངན་ལས་འདས་པ་མ་ཡིན་གྱི། གཟུགས་ལ་སོགས་པའི་རང་གི་ངོ་བོའི་མཚན་ཉིད་དངོས་པོའི་རང་བཞིན་རྒྱུ་རྐྱེན་ལས་དང་ཉོན་མོངས་པ་དང་མི་ལྡན་པས་ཕྱིས་མི་སྐྱེ་བ་གང་ཡིན་པ་དེ་མྱ་ངན་ལས་འདས་པ་སྙམ་དུ་སེམས་ན༌[^106]གལ་ཏེ་དེ་ལྟར་གྱུར་ན་དངོས་པོའི་རང་གི་ངོ་བོའི་མཚན་ཉིད་ཞིག་ནས་རྒྱུན་ཆད་པའི་ཚུལ་གྱིས་མྱ་ངན་ལས་འདས་པར་གྱུར་ཏེ། འདུས་བྱས་ཡོངས་སུ་ཤེས་པས་ནི་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 170]
གལ་ཏེ་འདི་ཉིད་འདོད་པ་ཡིན་པས་ན་ཉེས་པ་མེད་དོ་ཞེ་ན་ཡང་འདི་འཐད་པ་མ་ཡིན་ཏེ། འདི་ལྟར་དེ་ཁོ་ན་མཐོང་བས་འགོག་པ་མངོན་སུམ་དུ་བྱ་དགོས་ན་འགོག་པ་དེ་ལྟ་བུ་དེ་ནི་ཕུང་པོ་མ་འགགས་པའི༌[^107]ཚེ་ནི་མེད་པ། འགགས་ནས་ནི་སུ་ཡང་མེད་ན་འགོག་པ་དེ་སུ་ལ་མངོན་སུམ་དུ་འགྱུར། ཕུང་པོའི་རྒྱུན་ཡོད་པའི་དུས་ན་ནི་དེ་ཁོ་ན་མཐོང་བའི་དུས་གང་ཟག་འཕགས་པ་ཤཱ་རིའི་བུ་ལ་སོགས་པ་ཡོད་པས་འགོག་པ༌[^108]དེ་མངོན་སུམ་ཞེས་བྱ་བ་དེ་རིགས་སོ། །

[Block 171]
གལ་ཏེ་དེའི་ཚེ་དེས་ཅི་མཐོང་ན་དེའི་ཚེ་ཅི་ཞིག་དེ་ལ་མངོན་སུམ་དུ་འགྱུར། བཤད་པ། མ་མཐོང་དུ་ཟིན་ཀྱང་རྣམ་པར་ཤེས་པས་དེའི་རྣམ་པར་རིག་པས་མངོན་སུམ་དུ་ཞེས་གདགས་སོ། །

[Block 172]
གཞན་དག་གིས་ཀྱང་ཡུལ་རང་གི་མཚན་ཉིད་ཀྱི་རྣམ་པ་དང་མཐུན་པས་སྔོན་པོ་ལ་སོགས་པར་སྣང་བའི་རྣམ་པར་ཤེས་པ་གཞན་ཡང་མངོན་སུམ་དུ་བསྟན་ཏོ། །

[Block 173]
འདི་ལ་ཡང་དེ་དང་མཐུན་པ་ཡོད་པས་དེ་མངོན་སུམ་ཞེས་བྱ་བ་དེ་འགལ་བ་མེད་དོ། །

[Block 174]
སྡུག་བསྔལ་འགོག་པ་མངོན་སུམ་དུ་འགྱུར་ཞེས་བྱ་བར་དངོས་པོའི་རང་གི་མཚན་ཉིད་ནི་མངོན་སུམ་གྱི་ཡུལ་ཡིན་པར་ཁས་བླངས་པས་དངོས་པོ་མེད་པ་ནི་མངོན་སུམ་གྱི་ཤེས་པས་རིག་པར༌[^109]མི་རུང་སྟེ། སྡུག་བསྔལ་འགོག་པ་ནི་མངོན་སུམ་དུ་མི་འདོད་ན་འགོག་པ་ཤེས་པས་འགོག་པའི་བདེན་པས༌[^110]ཇི་ལྟར་མངོན་སུམ་དུ་བྱ། སྡུག་བསྔལ་མི་སྐྱེ༌[^111]ཙམ་ཡང་དངོས་པོའི་ངོ་བོར་མི་རུང་ངོ་། །གང་སྡུག་བསྔལ་མི་སྐྱེ༌[^112]ཙམ་འགོག་པ་ཡིན་པར་མི་འདོད༌[^113]ཀྱང་སྡུག་བསྔལ་མི་སྐྱེ༌[^114]ཙམ་ལས་དོན་གཞན་དུ་གྱུར་པའི་འགོག་པ་རང་གི་ངོ་བོས༌[^115]གྲུབ་པ་བསྟན་པར་མི་ནུས་སོ། །

[Block 175]
འགོག་པ་ཤེས་པ་ཟག་པ་མེད་པ་ནི་མངོན་སུམ་དུ་འདོད་ན། དེ་ཡང་དེ་ལྟར་གྱུར་པས་དེ་ནི་མངོན་སུམ་དུ་མི་འགྱུར་རོ། །

[Block 176]
གལ་ཏེ་འགོག་པ་ཤེས་པ་མངོན་སུམ་དུ་གྱུར་ན་ནི་དེའི་ཚེ་དེས་ཡོངས་སུ་བཅད་པའི་འགོག་པ་ཡང་འགགས་པས་མངོན་སུམ་ཉིད་དུ་ཁྱོད་ཀྱི་གཞུང་ལྟར་ན་ཀོ་བུམ་པ་ཤེས་པ་མངོན་སུམ་དུ་མི་འདོད་ན་སྔོན་པོ་ལ་སོགས་པ་ལྟར་བུམ་པ་མངོན་སུམ་དུ་མི་རུང་བ་དེ་བཞིན་དུ་འགོག་པ་ཡང་མི་འགྱུར་རོ། །

[Block 177]
རྣལ་འབྱོར་པ་རྣམས་ཀྱི་བླ་མས་བསྟན་པ་ལས་སྐྱེས་པ་རྣམ་པར་རྟོག་པ་དང་མ་འདྲེས་པ་གཅིག་ཏུ་ཡུལ་སྒྲོ་བཏགས་པ་མེད་པ་དོན་ཙམ་མཐོང་བ་གང་ཡིན་པ་དེ་ཡང་འགག་པ༌[^116]ལ་མི་སྲིད་དོ། །

[Block 178]
རང་གི་མཚན་ཉིད་དངོས་པོར་ཡོད་པ་གང་ཡིན་པ་དེ་ཉིད་སྤྱིའི་མཚན་ཉིད་ཀྱིས་གོམས་པར་བྱས་ན་ནི་རིམ་གྱིས་བསྒོམས་པ་ལས་བྱུང་བའི་ཡེ་ཤེས་སྐྱེ་ཞེས་གྲགས་ཏེ།[^117] རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་དེའི་གཟུང་བའི༌[^118]དངོས་པོ་གང་ཡིན་པ་དེ་ཡང་སྒྲོ་བཏགས་པ་མེད་པའི་ངོ་བོ༌[^119]ཡིན་པས་ན་རང་གི་མཚན་ཉིད་ཁོ་ནའོ། །

[Block 179]
འདི་ལྟར་མི་རྟག་པ་ཉིད་ཁོང་དུ་ཆུད་ན་ཐོག་མ་དང་ཐ་མའི་ཕྱོགས་ཀྱིས་སྟོང་པ་དངོས་པོ་ཙམ་ཁོང་དུ་ཆུད་དོ། །

[Block 180]
དེ་བས་ན་དེ་ཡང་ཡུལ་གྱི་རང་གི་མཚན་ཉིད་ཡིན་པས་སྔོན་པོ་ལ་སོགས་པ་ཙམ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་བཞིན་དུ་མངོན་སུམ་ཉིད་དོ་ཞེ་ན། འོན་ཀྱང་དཔྱོད་ན་རང་དང་སྤྱིའི་མཚན་ཉིད་ཐ་དད་པར་ཁས་བླངས་པས་སྤྱིའི་མཚན་ཉིད་ཀྱི་རྣམ་པ་ལ་སྒོམ་པའི་སྦྱོར་བ་གྲུབ་པའི་ངོ་བོའི་ཡུལ་རང་གི་མཚན་ཉིད་དུ་མི་འཐད་དེ། ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་དེའི་ཚིག་དེ་འབྲེལ་པ༌[^120]མེད་དོ། །
--- END BLOCKS ---
