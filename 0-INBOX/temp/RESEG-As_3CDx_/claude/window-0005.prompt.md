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
##### རང་བཞིན་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-6-0

[Block 177]
དེ་ལྟར་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས་དེའི་རང་བཞིན་ཅི་འདྲ་ཞེ་ན། དེའི་ཕྱིར་རང་བཞིན་ཕུན་སུམ་ཚོགས་པའི་དབང་དུ་མཛད་ནས་ཤིན་ཏུ་རྣམ་པར་དག་ཅིང་དབང་སྒྱུར་བའི་རྣམ་པར་རིག་པའི་མཚན་ཉིད་ཅེས་བྱ་བ་གསུངས་ཏེ། དེའི་རང་བཞིན་ནི་ཤིན་ཏུ་རྣམ་པར་དག་ཅིང་དབང་སྒྱུར་བའི་རྣམ་པར་རིག་པའི་མཚན་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 178]
དེ་ལ་ཤིན་ཏུ་རྣམ་པར་དག་ཅིང་ཞེས་བྱ་བ་ནི་གནས་ཕུན་སུམ་ཚོགས་པར་སྣང་བའི་རྣམ་པར་རིག་པ་དེ་ཉིད་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱི་བར་དུ་ཤིན་ཏུ་སྦྱང་བ༌[^134]བྱས་ཏེ། ཡང་དག་པ་མ་ཡིན་པའི་ཀུན་དུ་རྟོག་པ་བསལ་ཞིང་གཟུང༌[^135]བ་དང་འཛིན་པ་རྣམ་པར་སྤངས་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་ཤིན་ཏུ་རྣམ་པར་དག་པ་ཡིན་ནོ། །

[Block 179]
དབང་སྒྱུར་བ་ཞེས་བྱ་བ་ནི་ཟད་པར་གྱི་སྐྱེ་མཆེད་ལ་སོགས་པ་གྲུབ་པའི་རྣལ་འབྱོར་པ་དངོས་པོ་རྣམས་ལ་འདོད་དགུར་དབང་སྒྱུར་བ་དང་འདྲ་བར་ཤིན་ཏུ་རྣམ་པར་དག་པའི་རྣམ་པར་རིག་པ་དེས་རྣམ་པར་རིག་པ་ཙམ་གྱི་སྤྱོད་ཡུལ་རྣམ་པར་རིག་པའི་ངོ་བོ་ཉིད་དེ་ལ་དགྱེས་དགུར་དབང་སྒྱུར་ཞིང་མངའ་མཛད་པའི་དོན་ཏོ། །

[Block 180]
རྣམ་པར་རིག་པའི་མཚན་ཉིད་ཅེས་བྱ་བ་ནི་གནས་ཀྱི་རྣམ་པ་ལྟ་བུར་སྣང་བ་དེ་ཉིད་ཀྱི་སེམས་ཀྱི་རྣམ་པར་རིག་པ་ཙམ་གྱི་མཚན་ཉིད་ཡིན་ཏེ། རྣམ་པར་རིག་པ་ལས༌[^136]གཞན་པའི་ཕྱི་རོལ་ན་རིན་པོ་ཆེ་ལ་སོགས་པའི་དངོས་པོ་གཞན་མེད་པའི་ཐ་ཚིག་གོ། །

[Block 181]
སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱི་སྤྱོད་ཡུལ་དུ་སྣང་བ་ལུས་ལོངས་སྤྱོད་དང་། གནས་ཀྱི་རྣམ་པར་སྣང་བ་དག་ཀྱང་རང་རང་གི་རྣམ་པར་རིག་པའི་མཚན་ཉིད་ཡིན་མོད་ཀྱི་དེ་ནི་ཡང་དག་པ་མ་ཡིན་པའི་ཀུན་དུ་རྟོག་པས་བསྐྱེད་པ་གཟུང་བ༌[^137]དང་འཛིན་པའི་རྣམ་པར་སྣང་བ་ཡིན་པས་ཤིན་ཏུ་རྣམ་པར་དག་ཅིང་དབང་སྒྱུར་བ་མ་ཡིན་གྱི། འདི་ནི་དེ་ལས་བཟློག་པ༌[^138]ཡིན་པས་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པ་ཞེས་བྱའོ། །

[Block 182]
ཤིན་ཏུ་རྣམ་པར་དག་ཅིང་དབང་སྒྱུར་བའི་རྣམ་པར་རིག་པའི་མཚན་ཉིད་འདི་ནི་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་ལྟར་བསྟན་པ་དེའི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་ཞེས་ཀྱང་བྱ་སྟེ། དེ་ལ་ཅིའི་ཕྱིར་འབྲས་བུ༌[^139]ཞེས་བྱ་ཞེ༌[^140]ན། རྣམ་པར་རིག་པ་ལས་ཐ་མི་དད་ཀྱང་ཡུལ་གྱི་རྣམ་པ་ལྟ་བུར་སྣང་བས་འབྲས་བུ་ཞེས་བྱ་སྟེ། དཔེར་ན་ཟད་པར་སྔོན་པོ་ལ་སོགས་པར་སྙོམས་པར་ཞུགས་པ་རྣམས་ཀྱིས་དེའི་རྣམ་པའི་རྣམ་པར་རིག་པ་ལ་སྣང་བ་བཞིན་ཏེ། དེ་ནི་རང་བཞིན་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 183 [HEADING]]
##### བདག་པོ་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-7-0

[Block 184]
དེ་ལྟར་རང་བཞིན་ཕུན་སུམ་ཚོགས༌[^141]པ་བསྟན་ནས། གནས་ནི་བདག་པོས་ཡོངས་སུ་ཟིན་པ་ཡིན་པའི་ཕྱིར་དེའི་བདག་པོ་གང་ཞེ་ན། དེའི་ཕྱིར་བདག་པོ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། དེ་བཞིན་གཤེགས་པའི་གནས་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ནི་བདག་པོའི་ཁྱད་པར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི་གནས་ཡིན་གྱི་གཞན་གྱི་མ་ཡིན་ནོ། །

[Block 185]
ཡང་ན་དེས་དེ་བྱིན་གྱིས་བརླབས་ཏེ་ཟིན་པ་དང་། ཡོངས་སུ་བཟུང་བ་ཡིན་གྱི་གཞན་གྱི༌[^142]མ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 186]
[^143]དེ་ནི་བདག་པོ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 187 [HEADING]]
##### ཞམ་འབྲིང་བ་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-8-0

[Block 188]
དེ་ལྟར་བདག་པོ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། བདག་པོས་ནི་ཞམ་འབྲིང་བ་ཡོངས་སུ་ཟིན་པའི་ཕྱིར་བདག་པོ་ཕུན་སུམ་ཚོགས་པ་ལ་ཞམ་འབྲིང་བ་ཡང་དགོས་པས་དེའི་ཕྱིར་ཞམ་འབྲིང་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། བྱང་ཆུབ་སེམས་དཔའ་དཔག་ཏུ་མེད་པའི་དགེ་འདུན་དང་ལྡན་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ལྟར་བདག་པོ་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པའི་གནས་དེ་ནི་ཞམ་འབྲིང་བ་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པ་ཡང་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 189]
ཞམ་འབྲིང་བ་ཞེས་བྱ་བ་ནི་གང་གི་རྗེས་སུ་གང་འགྲོ་བ་དེ་ནི་དེའི་ཞམ་འབྲིང་བ་ཞེས་བྱ༌[^144]སྟེ། བྱང་ཆུབ་སེམས་དཔའ་གྲངས་ལས་འདས་པ་དག་དེ་ན་ཡོད་པའི་དོན་ཏོ། །

[Block 190]
འོ་ན་ཞམ་འབྲིང་བ་ཉན་ཐོས་ལ་སོགས་པ་དག་མ་སྨོས་པར་ཅིའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའི་དགེ་འདུན་ཉི་ཚེ་སྨོས་ཤེ་ན། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་བདུད་བཞི་ལ་སོགས་པ་དགྲའི་རྣམ་པ་ཐམས་ཅད་ཕྱིར་བཟློག༌[^145]ནུས་པས་དེ་དག་ནི་དེའི་ཞམ་འབྲིང་བ་ཡིན་གྱི་ཉན་ཐོས་ལ་སོགས་པས་ནི་དེ་ལྟ་མ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ནི་ཞམ་འབྲིང་བ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 191 [HEADING]]
##### ཕྱོགས་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-9-0

[Block 192]
དེ་ལྟར་ཞམ་འབྲིང་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། ཞམ་འབྲིང་བ་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པ་ལ་ཕྱོགས་ཕུན་སུམ་ཚོགས་པ་ཡང་དགོས་པས། དེའི་ཕྱིར་ཕྱོགས་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ལྷ་དང་། ཀླུ་དང་། གནོད་སྦྱིན་དང་། དྲི་ཟ་དང་། ལྷ་མ་ཡིན་དང་། ནམ་མཁའ་ལྡིང་དང་། མི་འམ་ཅི་དང་། ལྟོ་འཕྱེ་ཆེན་པོ་དང་། མི་དང་མི་མ་ཡིན་པ་མཐའ་ཡས་པ་རྣམ་པར་རྒྱུ་བ་ཞེས་བྱ་བ་གསུངས་ཏེ། ལྷ་ལ་སོགས་པ་ཉིད་དེ་ན༌[^146]ཕྱོགས་ཡིན་ཏེ་གཞན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 193]
གནས་དེ་ནི་ཁམས་གསུམ་པ་ལས་ཡང་དག་པར་འདས་པའི་སྤྱོད་ཡུལ་ཡིན་ནོ་ཞེས་སྔར་བསྟན་པ་ལ་ལྷ་ལ་སོགས་པ་དེ་དག་ནི་ཁམས་གསུམ་པར་གཏོགས་པ་ཡིན་ན། དེར་ཇི་ལྟར་ལྷ་ལ་སོགས་པ་ཕྱོགས་སུ་འགྱུར་རོ་ཞེ་ན། ལྷ་ལ་སོགས་པ་འདི་དག་ཀྱང་གནས་ཕུན་སུམ་ཚོགས་པའི་ཁྱད་པར་དེ་ལྟ་བུར་སྣང་བའི་རྣམ་པར་རིག་པ་མཐོང་བར་ནུས་པ་ཤ་སྟག་ཡིན་པས་འགལ་བ་མེད་དོ། །

[Block 194]
ཡང་ན་ལྷ་ལ་སོགས་པ་དེ་ལྟ་བུ་བསྟན་པས་འདུལ་བའི་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱ་བའི་ཕྱིར་དེ་དག་ལྟ་བུར་སྤྲུལ་པ་སྟེ། དཔེར་ན་རྒྱལ་པོ་ཀ་པི་ན་གདུལ་བའི༌[^147]ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས༌[^148]འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོའི་འཁོར་བསྟན་པ་བཞིན་ནོ། །

[Block 195]
ཡང་ན་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་དེ་བཞིན་གཤེགས་པ་ལ་མཆོད་པ་བྱ་བའི་དོན་དུ་རང་རང་གི་ལུས་ལྷ་ལ་སོགས་པའི་ཆ་བྱད་སྣ་ཚོགས་དང་ལྡན་པར་སྤྲུལ་པ་ཡིན་པས་ཉེས་པ་མེད་དེ། [^149]དེ་ནི་ཕྱོགས་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 196 [HEADING]]
##### ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-10-0

[Block 197]
དེ་ལྟར་ཕྱོགས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས་ཕྱོགས་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པ་དེ་དག་ལོངས་སྤྱོད་ཇི་ལྟ་བུར་བསྟན་ཏེ་གནས་ཤེ་ན། དེའི་ཕྱིར་ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཆོས་ཀྱི་རོའི་དགའ་བ་དང་བདེ་བ་ཆེན་པོའི་ལོངས་སྤྱོད་ཀྱིས༌[^150]བསྟན་ཏེ་དེ་ན་གནས་སོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 198]
སྟོན་པ་ཞེས་བྱ་བ་ནི། ཟས་དེ་གནས་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 199]
ཆོས་ཀྱི་རོའི་དགའ་བ་དང་བདེ་བ་ཆེན་པོ་དེས་ཀྱང་དེ་དག་གནས་པར་འགྱུར་བའི་ཕྱིར་དེ་ནི་དེ་དག་གི་སྟོན་པ་ཡིན་ནོ། །

[Block 200]
འོ་ན་གནས་དེ་ནི་ཁམས་གསུམ་ལས༌[^151]ཡང་དག་པར་འདས་པའི་སྤྱོད་ཡུལ་ཡིན་ནོ་ཞེས་སྔར་བསྟན། དེ་ན་ཟས་ཡོད་པར་ཇི་ལྟར་འགྱུར། གལ་ཏེ་ཟག་པ་མེད་པའི་ཆོས་དེ་དག་གི་ཟས་ཡིན་ནོ་ཞེ་ན། དེ་ཡང་མི་རུང་ངོ་། །[^152]ཟས་ནི་སྲིད་པ་གསོ་བར༌[^153]བྱེད་པ་ཡིན་གྱི་དེ་ནི་སྲིད་པ་གཅོད་པར༌[^154]བྱེད་པ་ཡིན་པས་དེ་དག་ཟས་ཀྱིས་གནས་ཞེས་བྱར་མི་རུང་ངོ་ཞེ་ན། དེ་ནི་དཔེར་ན་གཟུགས་ལ་སོགས་པའི་ཁམས་སུ་འཕགས་པ་དག་ཟག་པ་མེད་པའི་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་པ་ན་དེས་དེ་དག་གི༌[^155]ལུས་གནས་པར་གྱུར་པ་དང་འདྲ་བར་ཟག་པ་མེད་པའི་ཆོས་ནི་དེ་དག་གི་ཟས་དང་འདྲ་བར་སྟོན་པ་ཡིན་པས༌[^156]འགལ་བ་མེད་དོ། །

[Block 201]
གལ་ཏེ་འཕགས་པ་དག་གཟུགས་ལ་སོགས་པའི་གནས་སུ་ཟག་པ་མེད་པའི་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་པ་ནི་ཟག་པ་མེད་པའི༌[^157]ཏིང་ངེ་འཛིན་དེས་གནས་པ་མ་ཡིན་གྱི་སྔོན་འདས་པའི༌[^158]དུས་སུ་ཟས་གང་ཡང་རུང་བ་སྟོན་པའི་ཟས༌[^159]ད་ལྟར་གནས་པ་ཡིན་པས་དཔེ་དེ་མི་རུང་ངོ་ཞེ་ན། དེ་དག་འདས་པའི་ཟས་དང་ལྡན་ཞེས་བྱར་མི་རུང་སྟེ། འདས་པ་ནི་མེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 202]
དེ་དང་འདྲ་བར་འདིར་ཡང་གལ་ཏེ་དེ་དག་དེ་ན་ཟག་པ་མེད་པའི་ཆོས་ཀྱི་རོའི་དགའ་བ་དང་བདེ་བ་ཆེན་པོས་བསྟན་པ་མ་ཡིན་གྱི་འདས་པའི་དུས་ཀྱི་ཟས་གཞན་གྱིས་བསྟན་ཏེ་གནས་པར་གྱུར་ན་མེད་པས་བསྟན་ཏེ་གནས་པའི་སྐྱོན་དུ་འགྱུར་བས། དེའི་ཕྱིར་དེ་དག་ནི་འདས་པའི་ཟས་ཀྱིས་བསྟན་ཏེ་གནས་པ་མ་ཡིན་གྱི་ཆོས་ཀྱི་རོའི་དགའ་བ་དང་བདེ་བ་ཆེན་པོས༌[^160]བསྟན་པ་ཡིན་ཏེ། དེ་ནི་ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 203 [HEADING]]
##### བྱ་བ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-11-0

[Block 204]
དེ་ལྟར་ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པ་དེའི་ཕྲིན་ལས་ཅི་མཛད་ཅེ་ན། དེའི་ཕྱིར་བྱ་བ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། སེམས་ཅན་གྱི་དོན་ཐམས་ཅད་ཡང་དག་པར་ཐོབ་པར་བྱེད་པར་ཉེ་བར་གནས་པ་ཞེས་བྱ་བ༌[^161]གསུངས་ཏེ། སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བྱ་བ་ཐམས་ཅད་ཡང་དག་པར་ཐོབ་པར་བྱེད་པས་དེའི་ཉེ་བར་གནས་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 205]
དོན་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་ཕན་པ་དང་བདེ་བའི་དོན་ཏོ། །

[Block 206]
ཚེ་འདི་ལ་ཕན་པ་དང་ཚེ་ཕྱི་མ་ལ་བདེ་བའོ། །

[Block 207]
ཡང་ན་འཇིག་རྟེན་པའི་དོན་ནི་ཕན་པའོ། །

[Block 208]
འཇིག་རྟེན་ལས་འདས་པའི་དོན་ནི་བདེ་བའོ། །

[Block 209]
འོ་ན་གནས་དེ་ནི་མི་གཡོ་བའི་མཚན་ཉིད་དེ་མངོན་པར་འདུ་བྱེད་པ་མེད་པ༌[^162]ཡིན་ན། [^163]ཇི་ལྟར་ན་སེམས་ཅན་གྱི་དོན་ཐམས་ཅད་ཡང་དག་པར་ཐོབ་པར་བྱེད་ཅེ་ན། དེ་ནི་དཔེར་ན་འཕགས་པ་རྣམས་ཞི་བའི་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་ཀྱང་སྔོན་གྱི་མངོན་པར་འདུ་བྱེད་པའི་དབང་གིས་སེམས་ཅན་གྱི་དོན་མཛད་པ་རྒྱུན་མི་འཆད་པ་དང་འདྲ་བར་བལྟ་བར༌[^164]བྱ་སྟེ། དེ་ནི་བྱ་བ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 210 [HEADING]]
##### འཚེ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-12-0

[Block 211]
དེ་ལྟར་བྱ་བ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། བྱ་བ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་དེ་ལ་འཚེ་བ་མེད་པ་ཡང་དགོས་པས་དེའི་ཕྱིར་འཚེ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཉོན་མོངས་པའི་དྲི་མའི་གནོད་པ་ཐམས་ཅད་དང་བྲལ་བ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ནི་རང་གི༌[^165]ནང་གི་རྒྱུད་ལས་བྱུང་བའི་གནོད་པ་མེད་པར་སྟོན་ཏོ། །

[Block 212]
དེ་ལ་ཉོན་མོངས་པ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་ལ་སོགས་པའོ། །

[Block 213]
དྲི་མ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་དེ་དག་ཉིད་དྲི་མའོ། །

[Block 214]
གནོད་པ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པའི་དྲི་མ་ལས་བྱུང་བའི་གནོད་པ་སྟེ་སྡུག་བསྔལ་སྣ་ཚོགས་སོ། །

[Block 215]
ཉོན་མོངས་པའི་དྲི་མ་དེ་དག་ནི་གནོད་པའི་རྒྱུ་ཡིན་ཏེ། དེ་དག་མེད་པས་དེ་ལས་བྱུང་བའི་གནོད་པ་ཡང་མེད་དོ། །
--- END BLOCKS ---
