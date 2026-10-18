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
[Block 176 [HEADING]]
###### **འཇིག་རྟེན་གྱི་བདེ་བ་སྒྲུབ་པ།** ^1-1-2-8-1-2-1-0

[Block 177]
འཇིག་རྟེན་གྱི་བདེ་བ་སྒྲུབ་པ་ནི་ཇི་སྲིད་དུ་འཇིག་རྟེན་ལས་འདས་པའི་བདེ་བ་མ་ཐོབ་ཀྱི་བར་དུ་ལྷ་དང་མིའི༌[^169]བདེ་འགྲོར་སྐྱེ་བར་བྱེད་པའོ། །

[Block 178 [HEADING]]
###### **འཇིག་རྟེན་ལས་འདས་པའི་བདེ་བ།** ^1-1-2-8-1-2-2-0

[Block 179]
འཇིག་རྟེན་ལས་འདས་པའི་བདེ་བ་ཡང་རྣམ་པ་གཉིས་ཏེ། བླ་ན་ཡོད་པ་དང་། བླ་ན་མེད་པའོ། །

[Block 180 [HEADING]]
###### **བླ་ན་ཡོད་པ།** ^1-1-2-8-1-2-2-1-0

[Block 181]
དེ་ལ་བླ་ན་ཡོད་པ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི༌[^170]ཐེག་པ་ལ་བརྟེན་ནས་ཕུང་པོ་ལྷག་མ་དང་བཅས་པ་དང་། ཕུང་པོ༌[^171]ལྷག་མ་ཡང་མ་ལུས་པ་སྤངས་པའི་མྱ་ངན་ལས་འདས་པ་འཐོབ་བོ།[^172] །

[Block 182 [HEADING]]
###### **བླ་ན་མེད་པ།** ^1-1-2-8-1-2-2-2-0

[Block 183]
བླ་ན་མེད་པ་ནི་ཐེག་པ་ཆེན་པོ་ལ་བརྟེན་ནས་བདག་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པའི་རྟེན་དུ་གྱུར་པ་ནི༌[^173]མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་འཐོབ༌[^174]པའོ། །

[Block 184 [HEADING]]
###### གཞན་གྱི་དོན། ^1-1-2-8-2-0

[Block 185]
སེམས་ཅན་གཞན་ཡོངས་སུ་སྨིན་པར་བྱས་པ་འམ། གཞན་ལ་ཕན་པར་བྱས་པའི་དོན་ནི་གཞན་གྱི་དོན་ཏེ། དེ་ཡང་སྤང་བ༌[^175]དང་སྒྲུབ་པ་ལ་བཀོད་པ་གོང་མ་བཞིན་དུ་རྣམ་པ་གཉིས་སུ་རིག་པར་བྱའོ། །

[Block 186 [HEADING]]
###### བྱང་ཆུབ་ཀྱི་དོན། ^1-1-2-8-3-0

[Block 187]
བྱང་ཆུབ་ཉིད་དོན་དམ་པས་ན་བྱང་ཆུབ་ཀྱི་དོན་ཏོ།[^176] །བྱང་ཆུབ་ཀྱི་སྒྲས་འདིར་བྱང་ཆུབ་རྣམ་པ་གསུམ་ལ་བྱ་བར་རིག་པར་བྱ་སྟེ། དེ་དག་ནི་འཕགས་པའི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 188]
ཡང་ན་སྟོབས་དང་མི་འཇིགས་པ༌[^177]དང་། མ་འདྲེས་པ་ལ་སོགས་པ་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཡོངས་སུ་སྨིན་པར་བྱ་བའི་ཕྱིར་འཕགས་པའི་ལམ་སྒོམ་པར་བྱེད་པ་ནི་བྱང་ཆུབ་ཀྱི་དོན་ཅེས་བྱའོ། །

[Block 189]
མ་ཆགས་པས་ཡོངས་སུ་རྫོགས་པར་བྱེད་ཅེས་བྱ་བ་ནི་བདག་དང་གཞན་དང་བྱང་ཆུབ་ཀྱི་དོན་རྣམ་པ་གསུམ་ཆར་ལ་ཡང་དངོས་པོར་འཛིན་པ་མེད་ཅིང་། འཁོར་གསུམ་ཡོངས་སུ་དག་པའི་ཚུལ་གྱིས་མཐར་ཕྱིན་པར་བྱེད་པ་དེ་ནི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 190 [HEADING]]
#### ཐེག་པ་ཀུན་ལ་མཁས་པ། ^1-1-3-0

[Block 191]
དུས་གསུམ་ལ་མཁས་པ་བཤད་པའི་འོག་ཏུ་ཐེག་པ་ཀུན་ལ་མཁས་པ་བསྟན་པས་ཇི་ལྟར་བསྟན་པ་བཞིན་དུ་བཤད་པར་བཞེད་ནས། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་ཐམས་ཅད་ལ་མཁས་པ་གང་ཞེ་ན་ཞེས་དྲིས་ཏེ། ཐེག་པ་ཐམས་ཅད་ལ་མཁས་པ་ནི་ཐེག་པ་ཀུན་ལ་མཁས་པ་སྟེ། ཐེག་པ་ཐམས་ཅད་ཀྱི་རྒྱུ་དང་རང་བཞིན་དང་འབྲས་བུ་ཕྱིན་ཅི་མ་ལོག་པར་རྟོགས་པའོ། །

[Block 192]
དེ་ལ་ཐེག་པ་ཐམས་ཅད་ནི་བསྡུས་ན་རྣམ་པ་གཉིས་ཏེ། འཇིག་རྟེན་ལས་འདས་པའི་ཐེག་པ་དང་། འཇིག་རྟེན་གྱི་ཐེག་པའོ། །

[Block 193 [HEADING]]
##### འཇིག་རྟེན་ལས་འདས་པའི་ཐེག་པ། ^1-1-3-1-0

[Block 194]
འཇིག་རྟེན་ལས་འདས་པའི་ཐེག་པ་བསྟན་པ༌[^178]བཞེད་ནས། གསུམ་པོ་འདི་དག་ནི་ཐེག་པ་སྟེ། ངེས་པར་འབྱིན་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་། བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་འདི་གསུམ་ནི་འཇིག་རྟེན་ལས་འདས་པའི་ཐེག་པ་ཞེས་བྱ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན་འཁོར་བ་ལས༌[^179]འབྱིན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 195 [HEADING]]
##### འཇིག་རྟེན་གྱི་ཐེག་པ། ^1-1-3-2-0

[Block 196]
འཇིག་རྟེན་གྱི་ཐེག་པ་བསྟན་པར་བཞེད་ནས། གཞན་ཡང་ཐེག་པ་གཉིས་ཏེ། གཉིས་གང་ཞེ་ན། ལྷའི་ཐེག་པ་དང་མིའི་ཐེག་པའོ་ཞེས་བྱ་བ་གསུངས་པའོ། །

[Block 197]
དེ་ལ་ལྷ་རྣམས་ཀྱི་ཐེག་པ་ཡིན་པས་ན་ལྷའི་ཐེག་པ་དང་། མི་རྣམས་ཀྱི་ཐེག་པ་ཡིན་པས་ན་མིའི་ཐེག་པ་འམ། ལྷར་འགྱུར་བའི་ཐེག་པ་དང་། མིར་འགྱུར་བའི་ཐེག་པ་ནི་ལྷའི་ཐེག་པ་དང་མིའི་ཐེག་པ་ཞེས་བྱའོ། །

[Block 198]
དེ་ལ་ལྷའི་སྒྲས་ནི་རྒྱལ་ཆེན་བཞི་ལ་སོགས་པ་འདོད་པའི་ཁམས་ཀྱི་ལྷ་དྲུག་དང་། གཟུགས་ཀྱི་ཁམས་ཀྱི་ལྷ་དང་། ནམ་མཁའ་མཐའ་ཡས་ལ་སོགས་པ་གཟུགས་མེད་པའི་ཁམས་ཀྱི་ལྷ་རྣམས་བསྡུའོ།[^180] །ཐེག་པའི་སྒྲས་ནི་བསོད་ནམས་སུ་ཉེ་བར་འགྲོ་བའི་འདུ་བྱེད་སྲོག་གཅོད་པ་ལས་ཕྱིར་ལོག་པ་ལ་སོགས་པ་དགེ་བ་བཅུའི་ལས་ཀྱི་ལམ་དང་། རྟོག་པ་དང་བཅས་དཔྱོད་པ་དང་བཅས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཟག་པ་དང་བཅས་པའི་གཟུགས་ཀྱི་ཁམས་ཀྱི་བསམ་གཏན་བཞི་དང་། ནམ་མཁའ༌[^181]མཐའ་ཡས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གཟུགས་མེད་པའི་ཁམས་ཀྱི་སྙོམས་པར་འཇུག་པ་བཞི་མི་གཡོ་བ་ཉེ་བར་འགྲོ་བའི་མཚན་ཉིད་རྣམས་བསྡུས་ཏེ། འདུ་བྱེད་དེ་གཉིས་ཀྱིས་ལྷའི་གནས་དེ་དག་ཐོབ་པར་བྱེད་ཅིང་དེར་འགྲོ་བས་ན་ལྷའི་ཐེག་པ་ཞེས་བྱའོ། །

[Block 199]
མིའི་སྒྲས་ནི་གླིང་བཞི་ན་གནས་པའི་སྐྱེས་པ་དང་བུད་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་བསྡུས་ཏེ། ཐེག་པའི་སྒྲས་ནི་དགེ་བ་བཅུའི་ལས་ཀྱི་རང་བཞིན་བསོད་ནམས་སུ་ཉེ་བར་འགྲོ་བའི༌[^182]འདུ་བྱེད་ལ་བྱའོ། །

[Block 200]
ཁ་ཅིག་ན་རེ་བསོད་ནམས་མ་ཡིན་པར་ཉེ་བར་འགྲོ་བ་སྲོག་གཅོད་པ་ལ་སོགས་པ་མི་དགེ་བའི་ལས་ཀྱི་ལམ་བཅུ་པོ་རྣམས་ཀྱིས་ཀྱང་ངན་སོང་གསུམ་དུ་འགྲོ་ཞིང་སྐྱེ་བར་བྱེད་པས༌[^183]འདིས་འགྲོ་བ་དང་འདིར་འགྲོ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཐེག་པར་བསྟན་པའི་མཚན་ཉིད་ཡོང་ན་འདིར་འཇིག་རྟེན་པའི་ཐེག་པའི་ནང་དུ་ངན་སོང་གསུམ་རྣམས་ཅིའི་ཕྱིར་ཐེག་པ་མ་བསྡུས་ཤེ་ན། ཐེག་པ་ཞེས་བྱ་བའི་དོན་ནི་རྒྱུས་བདེ་བ་སྐྱེད་པར་བྱེད་པ་དང་། འབྲས་བུའི་ཚེ་འཕགས་པའི་བདེན་པ་རྟོགས་པའི་སྣོད་དུ་རུང་བ་ལ་བྱ་སྟེ། མི་དགེ་བ་བཅུའི་ལས་ཀྱི་ལམ་རྣམས་ལ་འདིས་འགྲོ་བ་དང་འདིར་འགྲོ་བ་ཞེས་བྱ་བ་བསྟན་དུ་རུང་ཡང་མི་དགེ་བའི་ལས་ཀྱི་ལམ་གྱི་རྒྱུ་ཉིད་སྡུག་བསྔལ་སྐྱེད་པར་བྱེད་པ་དང་། འབྲས་བུའི་ཚེ་ན་ཡང་འཕགས་པའི་བདེན་པ་རྟོགས་པའི་སྣོད་དུ་མི་རུང་བས་ན་ཐེག་པ་ཞེས་མི་བྱའོ། །

[Block 201 [HEADING]]
##### ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་མཁས་པ། ^1-1-3-3-0

[Block 202]
ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་བསྟན་པར་བཞེད་ནས་དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་གང་ཞེ་ན་ཞེས་དྲིས་པ་ལ་སོགས་པའོ། །

[Block 203]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་མཁས་པར་བྱ་བའི་ཉན་ཐོས་ཀྱི་ཐེག་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་སྟེ། ཉན་ཐོས་ཀྱི་ཐེག་པ་གང་ཞེ་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 204]
འདིས་འགྲོ་བས་ན་ཐེག་པ་སྟེ། གང་གིས་འགྲོ་ཞེ་ན། ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་ལ་སོགས་པས་འགྲོ་བས་ཐེག་པའི་སྒྲ་ནི་བསླབ་པ་གསུམ་ལ་བྱའོ། །

[Block 205]
ཡང་ན་འདིར་འགྲོ་བས་ན་ཐེག་པ་སྟེ། དེས་ནི་རྣམ་པར་གྲོལ་བ་དང་། རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་མཐོང་བའི་ཕུང་པོ་ལ་ཐེག་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 206]
ཐེག་པ་དེའི་མཚན་ཉིད་དང་། རྒྱུ་ལ་སོགས་པ་ཕྱིན་ཅི་མ་ལོག་པར་རྟོགས་པ༌[^184]ནི་ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་སྟེ། དེའང་འོག་ནས་འཆད་དོ། །

[Block 207 [HEADING]]
###### ཉན་ཐོས་ཀྱི་ཐེག་པ་རྣམ་པ་དྲུག། ^1-1-3-3-1-0

[Block 208]
དེ་ལ་ཉན་ཐོས་ཀྱི་ཐེག་པ་ཡང་རྣམ་པ་དྲུག་ཏུ་རིག་པར་བྱ་སྟེ། རྟེན་དང་། དམིགས་པ་དང་། རྒྱུ་དང་། སྒྲུབ་པ་དང་། འབྲས་བུ་དང་། དེ་རབ་ཏུ་རིག་པའོ། །

[Block 209 [HEADING]]
###### **རྟེན།** ^1-1-3-3-1-1-0

[Block 210]
སངས་རྒྱས་བྱུང་བ་མེད་པར་ཉན་ཐོས་ཀྱི་ཐེག་པ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི་དགའ་ལྡན་གྱི་ཕོ་བྲང་ནས་བྱང་ཆུབ་སེམས་དཔའ་འཆི་འཕོ་བ་བསྟན་ཏེ། ཡུམ་གྱི་ལྷུམས་སུ་བལྟམས་པ་དང་། བཙས་པ་དང་། གཞོན་ནུ་ལ་སོགས་པའི་རིམ་པས་སེམས་ཅན་གྱི་དོན་དུ་ཐབས་ཀྱི་སྤྱོད་པ་རྣམ་པ་སྣ་ཚོགས་མཛད་ནས་ཁབ་ནས་བྱུང་སྟེ་དཀའ་བར་སྤྱད་པ་ལ་སོགས་པས་བསྟན་ནས་མངོན་པར་སངས་རྒྱས་པ་ནི་སངས་རྒྱས་འབྱུང་བ་ཞེས་བྱ་སྟེ། སངས་རྒྱས་འབྱུང་བ་ལ་བརྟེན་པ་མེད་པར་ཉན་ཐོས་ཀྱི་ཐེག་པ་འབྱུང་བ་ཡང་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 211]
འདིས་ནི་རྟེན་བསྟན་པ་ཡིན་ནོ། །

[Block 212 [HEADING]]
###### **དམིགས་པ།** ^1-1-3-3-1-2-0

[Block 213]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནི་རྒྱུ་འདྲི་བ་སྟེ། སངས་རྒྱས་འབྱུང་བ་མེད་པར་ཉན་ཐོས་ཀྱི་ཐེག་པ་ཡང་ཅིའི་ཕྱིར་མེད་ཅེ་ན༌[^185]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 214]
དེའི་ལན་དུ་ཉན་ཐོས་རྣམས་ཀྱི་ཡང་དག་པར་ལྟ་བ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྒྲའི་རྗེས་སུ་འགྲོ་བ་ཞེས་བྱ་བ་གསུངས་ཏེ། གང་ཆོས་ཐམས་ཅད་ལ་གང་ཟག་གི་དངོས་པོ་མེད་དེ། གང་ཟག་ལ་བདག་མེད་པ་ཡང་དག་པའི་ཡེ་ཤེས་ཀྱིས་ཁོང་དུ་ཆུད་པ་ནི་ཉན་ཐོས་རྣམས་ཀྱི་ཡང་དག་པར་ལྟ༌[^186]བའོ། །

[Block 215]
ཡང་དག་པའི་ལྟ་བ་དེ༌[^187]ཡང་སངས་རྒྱས་སམ། མཁན་པོའམ་སློབ་དཔོན་གྱིས་བཤད་པའི་སྒྲ་མཉན་ནས་གང་ཟག་ལ་བདག་མེད་པར་དམིགས་པར་བྱེད་པས་ན༌[^188]ཕ་རོལ་གྱི་སྒྲའི་རྗེས་སུ་འགྲོ་བ་ཞེས་བྱ་སྟེ། འདིས་ནི་དམིགས་པར་སྨྲ་བ་ཡིན་ནོ། །
--- END BLOCKS ---
