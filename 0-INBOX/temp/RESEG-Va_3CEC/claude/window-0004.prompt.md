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
གནས་པར་བྱེད་ཅེས་བྱ་བ་ནི་མི་ཉམས་པར་བྱེད་པ༌[^139]བསྟན་ཏེ། དགེ་བའི་རྩ་བ་སྐྱེས་ཤིང་བྱུང་བ་གོང་ནས་གོང་དུ་ཁྱད་པར་དུ་འབོགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 142 [HEADING]]
###### **འབྲས་བུ་གཞན་དུ་མི་འགྱུར་བར་བྱེད་པ།** ^1-1-2-6-3-3-0

[Block 143]
བྱང་ཆུབ་ཏུ་ཡོངས་སུ་བསྔོ་བ་ཞེས་བྱ་བས་འབྲས་བུ་གཞན་དུ་མི་འགྱུར་བར་བྱེད་པ་བསྟན་ཏེ། དེ་ལྟར་བྱུང་བའི་དུས་སུ་དགེ་བ་བྱས་ཏེ་གནས་པར་གྱུར་པ་རྣམས་ལྷ་དང་ཀླུ་ལ་སོགས་པའི་འབྲས་བུ་ཐོབ་པར་མི་བསྔོའི། བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པར་བསྔོ་བའི་ཕྱིར་རོ། །

[Block 144 [HEADING]]
##### སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པ། ^1-1-2-7-0

[Block 145]
དུས་གསུམ་གྱི་བསོད་ནམས་ཀྱི་ཚོགས་ཅི་བྱས་པས་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པ་ནི་དུས་གསུམ་ལ་མཁས་པ་ཡིན་ནོ་ཞེས་བསྟན་པར་བཞེད་ནས། གཞན་ཡང་གང་སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་སྨིན་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 146]
སེམས་ཅན་ཐམས་ཅད་ཅེས་བྱ་བས་ནི་རིགས་ལྔ་དང་ལྡན་པའི་གང་ཟག་རྣམས་བསྡུས་ཏེ། དེ་དག་སོ་སོའི་ཐེག་པ་དང་། ལྷ་དང་མིའི་བདེ་འགྲོར་འགོག་པ་ནི་ཡོངས་སུ་སྨིན་པར་བྱ་བ་སྟེ། ཕྱིར་ཞེས་བྱ་བ་ནི་དེའི་ཆེད་དུའོ། །

[Block 147]
འདས་པའི་བསོད་ནམས་ཀྱི་ཚོགས༌[^140]དྲན༌[^141]ནས་ཞེས་བྱ་བ་ནི་བདག་གི་སྔོན་དགེ་བ་འདི་དང་འདི་བྱས་སོ་ཞེས་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་ལ་སོགས་པ་བསོད་ནམས་ཀྱི་ཚོགས་ཅི༌[^142]བྱས་པ་མ་བརྗེད་པ་ནི་དྲན་པའོ། །

[Block 148]
སེམས་ཅན་གང་དག་ཇི་ལྟ་བུར་ཡོངས་སུ་སྨིན་པ་དང༌[^143]བྱ་བ་དེ་དག་ཐམས་ཅད་དེ་བཞིན་དུ་ཡོངས་སུ་སྨིན་པར་བྱེད་ཅེས་བྱ་བས་སྔོན་བྱས་པའི་བསོད་ནམས་དེ་དག་དྲན་པ་ཙམ་དུ་མ་ཟད་ཀྱི། བསོད་ནམས་དེ་དག་གི་མཐུས་སེམས་ཅན༌[^144]ཇི་སྙེད་ཅིག་ཇི་ལྟར་སྨིན་པར་བྱ་བ་དེ་དག་ཐམས་ཅད་དེ་བཞིན་དུ་སྨིན་པར་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 149]
མ་འོངས་པའི་དུས་ཀྱི་སེམས་ཅན་གང་དག་སངས་རྒྱས་མཉེས་པར་བྱ་བས་ཡོངས་སུ་སྨིན་པར་བྱ་བ་དེ་དག་ཐམས་ཅད་དེ་བཞིན་དུ་ཡོངས་སུ་སྨིན་པར་བྱེད་ཅེས་བྱ་བ་ནི་སངས་རྒྱས་མཉེས་པར་བྱ་བའི་སྒོ་ནས་མ་འོངས་པའི་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱ་བ་ནི་མ་འོངས་པའི་དུས་ཀྱི་སེམས་ཅན་གང་དག་སངས་རྒྱས་མཉེས་པར་བྱ་བས་ཡོངས་སུ་སྨིན་པར་བྱ་བ་ཞེས་བྱ་སྟེ། དེ་ནི་འདི་སྐད་དུ། དེ་བཞིན་གཤེགས་པ་དེ་དག་གི་དྲུང་དུ་སོང་ནས་དམ་པའི་ཆོས་མཉན་པ་དང་། བསམ་པ་དང་། བསྒོམ་པ་ལ་སོགས་པ་སྒྲུབ་པའི་མཆོད་པ་དང་། མཉེས་པར་བྱས་ནས། དེ་ལ་བརྟེན་ཏེ་སེམས་ཅན་ཇི་སྙེད་ཅིག་ཡོད་པ༌[^145]ཇི་ལྟར་ཡོངས་སུ་སྨིན་པར་བྱ་བ༌[^146]དེ་སྙེད་ཅིག་དེ་བཞིན་ཡོངས་སུ་སྨིན་པར་བྱེད་ཅེས་བྱ་བ་སྟོན༌[^147]ཏོ། །

[Block 150]
ད་ལྟར༌[^148]བྱུང་བའི་སེམས་ཅན་རྣམས་ལ་ཆོས་བསྟན་པའམ། རྫུ་འཕྲུལ་གྱི༌[^149]ཆོ་འཕྲུལ་གྱིས་ཡོངས་སུ་སྨིན་པར་བྱ་བ་དེ་དག་ཐམས་ཅད་ཀྱང་དེ་བཞིན་དུ་ཡོངས་སུ་སྨིན་པར་བྱེད་དེ་ཞེས་བྱ་བ་ལ། ཆོ་འཕྲུལ་གྱི་སྒྲ་གཉི་ག་དང་སྦྱར་ཏེ། ཆོས་བསྟན་པའི་ཆོ་འཕྲུལ་དང་། རྫུ་འཕྲུལ་གྱི་ཆོ་འཕྲུལ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 151 [HEADING]]
###### ཆོས་བསྟན་པའི་ཆོ་འཕྲུལ། ^1-1-2-7-1-0

[Block 152]
དེ་ལ་ཆོས་བསྟན་པའི་ཆོ་འཕྲུལ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཀུན་བརྗོད་པའི་ཆོ་འཕྲུལ་དང་། རྗེས་སུ་བསྟན་པའི་ཆོ་འཕྲུལ་ལོ། །

[Block 153 [HEADING]]
###### **ཀུན་བརྗོད་པའི་ཆོ་འཕྲུལ།** ^1-1-2-7-1-1-0

[Block 154]
དེ་ལ་ཀུན་བརྗོད་པའི་ཆོ་འཕྲུལ་ནི་སེམས་ཅན་རྣམས་ཀྱི༌[^150]ཁམས་དང་རང་བཞིན་དང་བག་ལ་ཉལ་རྣམས་ལ་བཏགས༌[^151]ནས་དེ་དག་ལ་དེ་བཞིན་དུ་བརྗོད་པའོ། །

[Block 155 [HEADING]]
###### **རྗེས་སུ་བསྟན་པའི་ཆོ་འཕྲུལ།** ^1-1-2-7-1-2-0

[Block 156]
རྗེས་སུ་བསྟན་པའི་ཆོ་འཕྲུལ་ནི་དེ་ལྟར་གདུལ་བྱ་དེ་དག་བརྡ་སྤྲད་ནས་བསྟན་པ་ལ་བཙུད་དེ། འདི་ནི་སྡུག་བསྔལ་གྱི་བདེན་པ། འདི་ནི་ཀུན་འབྱུང་གི་བདེན་པ། འདི་ནི་འགོག་པའི་བདེན་པ། འདི་ནི་ལམ་གྱི་བདེན་པའོ་ཞེས་བདེན་པ་བཞི་ལ་སོགས་པ་འཆད་པའོ། །

[Block 157 [HEADING]]
###### རྫུ་འཕྲུལ་གྱི་ཆོ་འཕྲུལ། ^1-1-2-7-2-0

[Block 158]
རྫུ་འཕྲུལ་གྱི་ཆོ་འཕྲུལ་ནི་དབང་ལྔ་དང་ལྡན་པ་སྟེ། གཅིག་ཏུ་གྱུར་ནས་མང་པོར་འགྱུར་བ་དང་། མང་པོར་གྱུར་ནས་གཅིག་ཏུ་འགྱུར་བ་དང་། སྣང་བ་དང་མི་སྣང་བ་ལ་དབང་བས་སྤྲུལ་པ་ལ་དབང་བ་དང་། རྩིག་པ་ལ་ཡང་ཐད་ཀར་འགྲོ། ར་བ་ལ་ཡང་ཐད་ཀར་འགྲོ་བ་ལ་སོགས་པ་ལ་དབང་བས་འགྲོ་བ་ལ་དབང་བ་དང་། ནམ་མཁའ་ལ་མངོན་དུ་འཕགས་ཏེ་སྤྱོད་ལམ་རྣམ་བཞི་བྱེད་པ་དང་། ཆུ་ལ་ཡང་མི་ནུབ་པར་འགྲོ་སྟེ། ས་ཆེན་པོ་ལ་བྱ་བ་བཞིན་བྱེད་པ་ལ་དབང་བས་གནས་པ་ལ་དབང་བ་དང་། མིའི་འགྲོ་བ་འདི་ན་གནས་བཞིན་དུ་ལྷའི་འགྲོ་བར་གཏོགས་པ། ཟླ་བ་དང་། ཉི་མ་འདི་གཉིས་འདི་ལྟར་རྫུ་འཕྲུལ་ཆེ་བ། འདི་ལྟར་མཐུ་ཆེ་བ་འདི་ལྟར་གཟི་བརྗིད་ཆེ་བ་ལའང་ལག་པས་འཛིན་ཅིང་ཀུན་དུ་ཉུག་པར་བྱེད་པས་ལུས་ལ་དབང་བ་དང་། ཚངས་པའི་འཇིག་རྟེན་གྱི་བར་དུ་སེམས་ཅན་རྣམས་ལ་ལུས་ཀྱི༌[^152]དབང་སྒྱུར་བས་ཁམས་ཁྱད་པར་ཅན་ལ་དབང་བ་སྟེ། དེ་ལྟར་དབང་ལྔ་དང་ལྡན་པས་གདུལ་བྱའི༌[^153]སེམས་ཅན་འདུན་པར་བྱེད་པ་ནི་རྫུ་འཕྲུལ་གྱི་ཆོ་འཕྲུལ་ལོ། །

[Block 159]
ད་ལྟར་གྱི་སེམས་ཅན་ཁ་ཅིག་ཆོས་བསྟན་པའི་ཆོ་འཕྲུལ་གྱིས་ཡོངས་སུ་སྨིན་པར་བྱ་བ་ཡིན། སེམས་ཅན་ཁ་ཅིག་རྫུ་འཕྲུལ་གྱི་ཆོ་འཕྲུལ་གྱིས་ཡོངས་སུ་སྨིན་པར་བྱ་བ་ཡིན་ཏེ། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཆོ་འཕྲུལ་གང་གིས་སེམས་ཅན་གང་ཡོངས་སུ་སྨིན་པར་བྱ་བ་ཆོ་འཕྲུལ་དེས་སེམས་ཅན་དེ་ཡོངས་སུ་སྨིན་པར་བྱེད་དོ།[^154] །དེ་བས་ན་སེམས་ཅན༌[^155]ཡོངས་སུ་སྨིན་པར་བྱ་བ་དེ་དག་ཐམས་ཅད་ཀྱང་དེ་བཞིན་དུ་ཡོངས་སུ་སྨིན་པར་བྱེད་དོ་ཞེས་གསུངས་སོ། །

[Block 160 [HEADING]]
##### དུས་གསུམ་ལ་མཁས་པའི་དོན་བསྡུས་ཏེ་བསྟན་པ། ^1-1-2-8-0

[Block 161]
དུས་གསུམ་ལ་མཁས་པ་གོང་དུ་བཤད་པ་རྣམས་ཀྱི་དོན་བསྡུས་ཏེ། བསྟན་པར་བཞེད་ནས། [^156]གང་དུས་གསུམ་འདི་དག་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ་གང་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དང་སྦྱར་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་གང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 162]
དུས་གསུམ་འདི་དག་ཅེས་བྱ་བ་ནི་གོང་དུ་བཤད་པའི་འདས་པ་དང་། མ་འོངས་པ་དང་། ད་ལྟར་གྱི༌[^157]དུས་དག་ལའོ། །

[Block 163]
མ་ཆགས་པས་ཡོངས་སུ་རྫོགས་པར་བྱེད་ཅེས་བྱ་བའི་ཚིག་གོང་མའི་ཚིག༌[^158]གསུམ་ཆར་དང་ཡང་སྦྱར་ཏེ། བདག་གི་དོན་ལ་མ་ཆགས་པས་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་དང་། གཞན་གྱི་དོན་ལ་མ་ཆགས་པས་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་དང་། བྱང་ཆུབ་ཀྱི་དོན་ལ་མ་ཆགས་པས་ཡོངས་སུ་རྫོགས་པར་བྱེད་ཅེས་བྱ་བར༌[^159]སྦྱར་རོ། །

[Block 164 [HEADING]]
###### བདག་གི་དོན། ^1-1-2-8-1-0

[Block 165]
དེ་ལ་བདག་ཡོངས་སུ་སྨིན་པར་འགྱུར་བ་འམ། བདག་ལ་ཕན་པར་འགྱུར་བའི་དོན་ནི་བདག་གི་དོན་ཏེ། དེ་ཡང་སྤངས་པ་དང་སྒྲུབ་པའི་མཚན་ཉིད་རྣམ་པ་གཉིས་སོ། །

[Block 166 [HEADING]]
###### **སྤངས་པ།** ^1-1-2-8-1-1-0

[Block 167]
དེ་ལ་སྤངས་པ༌[^160]ཡང་རྣམ་པ་གསུམ་སྟེ།[^161] ཉོན་མོངས་པ་སྤང་བ༌[^162]དང་། སྡུག་བསྔལ་སྤང་བ༌[^163]དང་། ཤིན་ཏུ་སྤང་བའོ། །

[Block 168 [HEADING]]
###### **ཉོན་མོངས་པ་སྤང་བ།** ^1-1-2-8-1-1-1-0

[Block 169]
དེ་ལ་ཉོན་མོངས་པ་སྤང་བ༌[^164]ནི་འཇིག་རྟེན་གྱི་ལམ་ས་གོང་མ་ལ་ཞི་བར་ལྟ་ཞིང་། ས་འོག་མ་ལ་སྐྱོན་དུ་ལྟ་བས་ཅུང་ཟད་མེད་པའི་སྐྱེ་མཆེད་མན་ཆད་ཀྱིས༌[^165]ཉོན་མོངས་པ་ཐང་ཅིག་རྩེ་བཅིལ་བ་དང་། འཇིག་རྟེན་ལས་འདས་པ་མཐོང་བ་དང་བསྒོམ་པའི་ལམ་གྱིས་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པའི་བག་ཆགས་ཀྱང་མ་ལུས་པར་བཏོན་པའོ། །

[Block 170 [HEADING]]
###### **སྡུག་བསྔལ་སྤངས་པ།** ^1-1-2-8-1-1-2-0

[Block 171]
[^166]དེ་ལ་སྡུག་བསྔལ་སྤངས་པ་ནི་ངན་སོང་གསུམ་དུ་སྐྱེ་བའི་སྡུག་བསྔལ་དང་། ཁམས་གསུམ་དུ་སྐྱེ་བའི་སྡུག་བསྔལ་མ་ལུས་པར་སྤངས་པའོ། །

[Block 172 [HEADING]]
###### **ཤིན་ཏུ་སྤངས་པ།** ^1-1-2-8-1-1-3-0

[Block 173]
ཤིན་ཏུ་སྤངས་པ་ནི༌[^167]ཉོན་མོངས་པ་དང་སྡུག་བསྔལ་སྤངས་པ་དེ་དག་ལན་ཅིག་སྤངས་ནས་ཕྱིས་ཅི་ནས་ཀྱང་དེའི་སེམས་ཀྱི༌[^168]རྒྱུད་ལ་མི་སྐྱེ་བར་བྱེད་པའོ། །

[Block 174 [HEADING]]
###### **སྒྲུབ་པ།** ^1-1-2-8-1-2-0

[Block 175]
དེ་ལ་སྒྲུབ་པ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། འཇིག་རྟེན་གྱི་བདེ་བ་སྒྲུབ་པ་དང་། འཇིག་རྟེན་ལས་འདས་པའི་བདེ་བ་སྒྲུབ་པའོ། །

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
--- END BLOCKS ---
