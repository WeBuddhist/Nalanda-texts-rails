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
[Block 1 [HEADING]]
### ༄༅། །འཕགས་པ་བློ་གྲོས་མི་ཟད་པས་བསྟན་པ་རྒྱ་ཆེར་འགྲེལ་པ།༼སྨད་ཆ།༽

[Block 2 [HEADING]]
## ཤེས་རབ་མི་ཟད་པ། ^1-0

[Block 3 [HEADING]]
### ཤེས་རབ་ཀྱི་ཡུལ། ^1-1-0

[Block 4 [HEADING]]
#### རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལ་མཁས་པ། ^1-1-1-0

[Block 5]
ལྷག་མ་རྣམས་ནི་སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པར་བསྡུའོ། །

[Block 6 [HEADING]]
##### ལུགས་དང་མཐུན་པར་འབྱུང་བ། ^1-1-1-1-0

[Block 7 [HEADING]]
###### བདག་མེད་པའི་རྐྱེན་ལས་བྱུང་བའི་མཚན་ཉིད། ^1-1-1-1-1-0

[Block 8]
བདག་མེད་པའི་རྐྱེན་ལས་བྱུང་བའི་མཚན་ཉིད་བསྟན་པའི་ཕྱིར་གཡོ་བ་མེད་པ། བྱེད་པ་མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། གཡོ་བ་མེད་པ་ནི་མ་རིག་པ་ཡང་འདི་ལྟར་བདག་གིས་འདུ་བྱེད་བསྐྱེད་དོ་སྙམ་དུ་མི་སེམས་ལ། །འདུ་བྱེད་ཀྱང་འདི་ལྟར་བདག་ནི་མ་རིག་པས་བསྐྱེད༌[^1]དོ་སྙམ་དུ་སེམས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 9]
བྱེད་པ་མེད་པ་ནི་མ་རིག་པ་ལ་སོགས་པ་སྐྱེད་པའི་རྐྱེན་ཙམ་བྱེད་པ་ཡིན་ཡང་འདུ་བྱེད་སྐྱེད་པ་ལ་བྱེད་པ་པོའི་མཚན་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 10]
བདག་པོ་མེད་པ་ཞེས་བྱ་བ་ནི་དེ་དག་ལ་དབང་ཕྱུག་ལ་སོགས་པ་དབང་བྱེད་པར་གྱུར་པའི་མཚན་ཉིད་ཀྱི་བདག་པོ་གང་ཡང་མེད་པའི་ཕྱིར་རོ། །

[Block 11]
ཡོངས་སུ་འཛིན་པ་མེད་པ་ཞེས་བྱ་བ་ནི་བདག་དང་སེམས་ཅན་དང་གང་ཟག་ལ་སོགས་པ་སྙིང་པོར་གྱུར་པ་གང་གིས་ཀྱང་བྱིན་གྱིས་མ་བརླབས་པའི་ཕྱིར་རོ། །

[Block 12]
ཆོས་ཇི་ལྟར་གནས་པ་བཞིན་དུ་འབྱུང་སྟེ་ཞེས་བྱ་བ་ནི་རྒྱུ་གང་ཡིན་པ་ལས་འབྲས་བུ་གང་འབྱུང་བ་ནི་ཆོས་ཇི་ལྟར་གནས་པ་བཞིན་དུ་འབྱུང་བ་ཞེས་བྱ་སྟེ། དབང་ཕྱུག་ལ་སོགས་པ་ལས་འདུ་བྱེད་མི་འབྱུང་གི་མ་རིག་པའི་རྒྱུ་ལས་འདུ་བྱེད་འབྱུང་བའོ། །

[Block 13]
གང་འདི་ལ་ཤེས་པ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་འདི་ལ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཞེས་བྱ་བའི་སྒྲ་དྲངས་ཏེ། གང་ཚུལ་བཞིན་མ་ཡིན་པ་ཀུན་འབྱུང་བ་ལས་མ་རིག་པ་ཀུན་འབྱུང་བ་ལས༌[^2]སྐྱེ་བ་ཀུན་འབྱུང་བ་ལས་རྒ་ཤི་ལ་སོགས་པ་ཀུན་འབྱུང་བར་ཟད་ཀྱི་དེ་ལས་གཞན་པའི་གཡོ་བ་པོ་དང་། བྱེད་པ་པོ་ལ་སོགས་པ་མེད་པར་ཤེས་པ་འདི་ནི་བྱང་ཆུབ་སེམས་དཔའི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལ་མཁས་པ་རྣམས་ཞེས་བྱའོ། །

[Block 14 [HEADING]]
###### རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལ་མཁས་པའི་རྣམ་གྲངས་གཞན། ^1-1-1-1-2-0

[Block 15]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལ་མཁས་པའི་རྣམ་གྲངས་གཞན་ཡང་བསྟན་པར་བཞེད་ནས། གཞན་ཡང་གང་དགེ་བའི་རྒྱུ་ལས་བྱུང་བ་འམ་མི་དགེ་བའི་རྒྱུ་ལས་བྱུང་བ་འམ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 16]
དགེ་བ་ནི་སྲོག་གཅོད་པ་ལས་ཕྱིར་ལྡོག་པ་ལ་སོགས་པ་དགེ་བ་བཅུའི་ལས་ཀྱི་ལམ་རྣམས་སོ། །

[Block 17]
རྒྱུ་དེ་ལས་བྱུང་བ་ནི་འདོད་པའི་ཁམས་སུ་ལྷ་དང་མིར་སྐྱེ་བའོ། །

[Block 18]
མི་དགེ་བ་ནི་སྲོག་གཅོད་པ་མི་དགེ་བ་བཅུའི་ལས་ཀྱི་ལམ་རྣམས་སོ། །

[Block 19]
རྒྱུ་དེ་ལས་བྱུང་བ་ནི་འདོད་པའི་ཁམས་སུ་ངན་སོང་གསུམ་དུ་སྐྱེ་བའོ། །

[Block 20]
མི་གཡོ་བ་ནི་བསམ་གཏན་དང་སྙོམས་པར་འཇུག་པ་རྣམས་སོ། །

[Block 21]
རྒྱུ་དེ་ལས་བྱུང་བ་ནི་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་སུ་སྐྱེ་བའོ། །

[Block 22]
ཁམས་གཉིས་ཀྱི་ལས་ལ་ཅིའི་ཕྱིར་མི་གཡོ་བའི་ལས་ཞེས༌[^3]བྱ་ཞེ་ན། དེ་དག་གི་ལས་སེམས་རྩེ་གཅིག་པའི་མཚན་ཉིད་ལ་རྣམ་པར་རྟོག་པའི་རླུང་གིས་བསྐྱོད་པར་མི་ནུས་པས་ན་མི་གཡོ་བ་ཞེས་བྱའོ། །

[Block 23]
ཡང་ན་ཇི་ལྟར་འདོད་པ་ན༌[^4]སྤྱོད་པའི་ལས་འགྲོ་བ་གཞན་དུ་འགྲོ་བ་ཡིན་ཡང་དེ་མ་ཡིན་པ་རྐྱེན་གཞན་གྱི་དབང་གིས་བསྐྱོད་དེ། འགྲོ་བ་དེ་རྣམ་པར་སྨིན་པ་བཞིན་དུ་རྣམ་པར་སྨིན་ལ་གཡོ་བ་མེད་པས་ན་མི་གཡོ་བ་ཞེས་བྱའོ། །

[Block 24]
དེའི་དོན་ནི་དེ༌[^5]ཡིན་ཏེ། འདོད་པ་ན་སྤྱོད་པའི་སེམས་ཅན་གྱི་ལས་བྱས་པས་སྦྱིན་པ་ཡོངས་སུ་བཏང་ནས་མིའི་ནང་དུ་མིའི་ལོངས་སྤྱོད་མྱོང་བར་འགྱུར་བ་ལས་མི་དེ་ཉིད་ཀྱིས༌[^6]ཚུལ་ཁྲིམས་ཉམས་པ་ལ་སོགས་པའི་ལས་བྱས་པའི་དབང་གིས་མིར་སྐྱེ་བའི་རྣམ་པར་སྨིན་པ་བསྐྱོད་ནས་རྒྱལ་པོ་འམ་བློན་པོའི་བ་ལང་ངམ་རྟར་སྐྱེ་བ་ལྟ་བུར་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་ཀྱི་ལས་ལ་རྣམ་པར་སྨིན་པ་གཡོ་བ་མེད་པས་ན་མི་གཡོ་བ་ཞེས་བྱའོ། །

[Block 25]
འཁོར་བར་སྐྱེ་བའི་རྒྱུ་ནི་འཁོར་བའི་རྒྱུ་སྟེ། འདི་ལྟར་དགེ་བ་དང་མི་དགེ་བ་དང་མི་གཡོ་བའི་ལས་ཟག་པ་དང་བཅས་པ་རྣམས་སོ། །

[Block 26]
རྒྱུ་དེ་ལས་བྱུང་བ་ནི་འཁོར་བ་ཉིད་དོ། །

[Block 27]
མྱ་ངན་ལས་འདས་པར་གྱུར་པའི་རྒྱུ་ནི་མྱ་ངན་ལས་འདས་པའི་རྒྱུ་སྟེ། འཕགས་པའི་ལམ་རྣམས་སོ། །

[Block 28]
དེ་ལས་བྱུང་བ་ནི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 29]
དེ་ལས་མྱ་ངན་ལས་འདས་པའང་རྣམ་པ་གཉིས་ཏེ། [^7]ཆ་གཅིག་སྤངས་པའི་མྱ་ངན་ལས་འདས་པ་དང་། ཆ་གཉིས་སྤངས་པའི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 30]
དེ་ལ་ཆ་གཅིག་སྤངས་པའི་མྱ་ངན་ལས་འདས་པ་ནི་མཐོང་བ་དང་བསྒོམ་པས༌[^8]སྤང་བར༌[^9]བྱ་བའི་ཉོན་མོངས་པའི་ཆ་སྤངས་ཏེ། ཕུང་པོའི་ལྷག་མ་དང་བཅས་པའི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 31]
ཆ་གཉིས་སྤངས་པའི་མྱ་ངན་ལས་འདས་པ་ནི་ཇི་ལྟར་ཉོན་མོངས་པའི་ཆ་སྤངས་པ་བཞིན་དུ་ཕུང་པོའི་ཆ་ཡང་སྤངས་པ་སྟེ། ཕུང་པོའི་ལྷག་མ༌[^10]ཡང་མ་ལུས་པར་སྤངས་པའི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 32]
དེ་དག་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་གོང་དུ་བཤད་པའི་དགེ་བའི་རྒྱུ་དང་། མི་དགེ་བའི་རྒྱུ་དང་། མི་གཡོ་བའི་རྒྱུ་དང་། འཁོར་བའི་རྒྱུ་དང་། མྱ་ངན་ལས་འདས་པའི་རྒྱུ་ལས་བྱུང་བ་དེ་དག་ཐམས་ཅད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 33]
སེམས་ཅན་གང་དབང་པོའི་རྒྱུ་ལ་འཇུག་པ་ཚད་མར་བྱེད་པ་དེ་ནི་དབང་པོའི་རྒྱུ་ལས་བྱུང་ཞིང་། ལས་ཀྱི་རྒྱུ་ལས་བྱུང་བ་སྟེ་འབྲས་བུའི་རྒྱུ་གྲུབ་པར་བྱེད་དོ་ཞེས་བྱ་བ་ལ། དབང་པོ་ཉིད་དགེ་བ་དང་། མི་དགེ་བ་དང་། འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་རྣམས་བྱེད་པ་དང་འགྲུབ་པའི་རྒྱུ་ཡིན་པས་ན༌[^11]དབང་པོའི་རྒྱུ་སྟེ། དེ་ལྟར་དབང་པོའི་རྒྱུ་ལས་ཆོས་དེ་དག་འབྱུང་གི་བྱེད་པ་པོ་ལ་སོགས་པས་བྱས་པ་མ་ཡིན་པ༌[^12]ཤེས་པ་ནི་དབང་པོའི༌[^13]རྒྱུ་ལས་འཇུག་པ་ཚད་མར་བྱེད་པ་སྟེ། དེ་དག་ནི་དགེ་བ་དང་མི་དགེ་བ་དང་། འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ཀུན་ཀྱང་དབང་པོ་དང་ལས་ཀྱི་རྒྱུ་ལས་བྱུང་ཞིང་དགེ་བ་ལ་སོགས་པ་འབྲས་བུའི་རྒྱུ་དབང་པོ་ལས་གྲུབ་པར་བྱེད་དོ་ཞེས་ཟིན་པའི་ཆོས་རྣམས་ལ་ཡང་ཤེས་ལ་མ་ཟིན་པའང་ལས་ཀྱི་རྒྱུ་ལས་འབྱུང་བར་ཤེས་ན་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལ་མཁས་པ་ཡིན་པར་སྦྱར་རོ། །

[Block 34]
གང་དེ་ལྟར་རྒྱུ་ཀུན་འབྱུང་བ་ལས་སྐྱེ་བ་ལ་མཁས་པ་ཞེས་བྱ་བ་ནི་གང་གོང་དུ་བཤད་པ་ལྟར་རྒྱུ་སྨིན་པར་གྱུར་པ་ལས་འབྲས་བུ་སྐྱེ་བར་ཤེས་པ་འདི་ནི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 35 [HEADING]]
##### ལུགས་ལས་བཟློག་པའི་མཚན་ཉིད། ^1-1-1-2-0

[Block 36]
དེ་ལྟར་ལུགས་དང་མཐུན་པའི་མཚན་ཉིད་བསྟན་ནས། ལུགས་ལས་བཟློག་པའི་མཚན་ཉིད་བསྟན་པའི་ཕྱིར། གཞན་ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་མཚན་ཉིད་ལ་མཁས་པ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པའོ། །

[Block 37]
འདི་ལྟ་སྟེ་ཤིང་མེད་ན་མེ་དང་དུ་བ་མི་འབྱུང་བ་དང་། ས་བོན་མེད་ན་མྱུ་གུ་མི་སྐྱེ་བ་བཞིན་དུ་ཉོན་མོངས་པ་འགགས༌[^14]ན་དེ་ལས་སྐྱེས་པའི་འབྲས་བུ་མི་འབྱུང་བའི་ཕྱིར་ཚུལ་བཞིན་མ་ཡིན་པ་འགགས་པས་མ་རིག་པ་འགག་ཅེས་བྱའོ།[^15] །

[Block 38]
ཇི་ལྟར་མ་རིག་པ་ལ་སོགས་པ་འགགས་པ་ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་བྱ་ཞེ༌[^16]ན། སྨྲས་པ། ཉེས་པ་མེད་དེ། འདི་ལ་གཏན་མེད་པར་དགག་པ་ལ་ནི་མ་རིག་པ་ལ་སོགས་པ་འགག་གོ་ཞེས་མི་བྱའི་དཔེར་ན་མར་མེའི་རྐྱེན་གྱིས་མུན་པ་འགགས་ན་སྣང་བ་ཉིད་སྐྱེ་བ་དང་། སྨན་བཅུད་ཀྱི༌[^17]ལེན་ཟོས་ན་ནད་མེད་པ་ལ་བདེ་བ་སྐྱེ་བ་དེ་བཞིན་དུ་ལམ་བསྒོམས་པའི་མཐུས་མ་རིག་པ་དང་མི་མཐུན་པ་གང་རིག་པ་སྐྱེ་བར་འགྱུར་བ༌[^18]དེ་ནི་མ་རིག་པ་འགགས་པ་ཞེས་བྱ་སྟེ། དེ་ལྟར་གོང་ནས་གོང་དུ་འདུ་བྱེད་ལ་སོགས་པ་དང་མི་མཐུན་པའི་གནས་འབྱུང་བ་ལ་འདུ་བྱེད་ལ་སོགས་པ་འགགས་པར་བལྟའོ། །

[Block 39 [HEADING]]
##### མཐུན་པའི་རྒྱུ་ལས་བྱུང་བ་དང་མི་མཐུན་པའི་རྒྱུ་ལས་མི་འབྱུང་བ། ^1-1-1-3-0

[Block 40 [HEADING]]
###### མཐུན་པའི་རྒྱུ་ལས་བྱུང་བ། ^1-1-1-3-1-0
--- END BLOCKS ---
