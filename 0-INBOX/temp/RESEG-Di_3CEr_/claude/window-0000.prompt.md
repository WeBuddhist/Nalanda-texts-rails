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
### ༄༅། །ཚད་མ་ཀུན་ལས་བཏུས་པའི་འགྲེལ་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། པྲ་མཱ་ཎ་ས་མུཙྪཱ་ཡ་བྲྀཏྟི། བོད་སྐད་དུ། ཚད་མ་ཀུན་ལས་བཏུས་པའི་འགྲེལ་པ། སངས་རྒྱས་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [VERSE]]
ཚད་མར་གྱུར་པ་འགྲོ་ལ་ཕན་པར་བཞེད། །
སྟོན་པ་བདེ་གཤེགས་སྐྱོབ་ལ་ཕྱག་འཚལ་ནས། །
ཚད་མར་སྒྲུབ་ཕྱིར་རང་གི་གཞུང་ཀུན་ལས། །
བཏུས་ཏེ་སྣ་ཚོགས་འཐོར་རྣམས་འདིར་གཅིག་བྱ། །

[Block 5 [HEADING]]
## མངོན་སུམ་གྱི་ལེའུ། ^1-0

[Block 6 [HEADING]]
### བསྟོད་པ་བརྗོད་པ། ^1-1-0

[Block 7]
འདིར་ཡང་རབ་ཏུ་བྱེད་པའི་དང་པོར་རྒྱུ་དང་འབྲས་བུ་ཕུན་སུམ༌[^1]ཚོགས་པས་ཚད་མར་གྱུར་པ་ཉིད་ཀྱིས་བཅོམ་ལྡན་འདས་ལ་བསྟོད་པ་བརྗོད་པ་ནི་གུས་པ་བསྐྱེད་པར་བྱ་བའི་དོན་དུའོ། །

[Block 8]
དེ་ལ་རྒྱུ་ནི་བསམ་པ་དང་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 9]
བསམ་པ་ནི་འགྲོ་བ་ལ་ཕན་པར་བཞེད་པའོ། །

[Block 10]
སྦྱོར་བ་ནི་འགྲོ་བ་ལ་བསྟན་པ་སྟོན་པའོ། །

[Block 11]
འབྲས་བུ་ནི་རང་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 12]
རང་དོན་ཕུན་སུམ་ཚོགས་པ་ནི་བདེ་བར་གཤེགས་པ་ཉིད་ཀྱིས་ཏེ། དོན་གསུམ་ཉེ་བར་བླང་བར༌[^2]བྱའོ། །

[Block 13]
རབ་ཏུ་མཛེས་པའི་དོན་ནི་སྐྱེས་བུ་གཟུགས་ལེགས་པ་བཞིན་ནོ། །

[Block 14]
ཕྱིར་མི་ལྡོག་པའི་དོན་ནི་རིམས་ནད་ལེགས་པར་བྱང་པ་བཞིན་ནོ། །

[Block 15]
མ་ལུས་པའི་དོན་ནི་བུམ་པ་ལེགས་པར་གང་བ་བཞིན་ནོ།[^3] །

[Block 16]
དོན་གསུམ་པོ་དེ་ཡང་ཕྱི་རོལ་པའི༌[^4]འདོད་ཆགས་དང་བྲལ་བ་དང་། སློབ་པ་དང་། མི་སློབ་པ་རྣམས་ལས་རང་དོན་ཕུན་སུམ་ཚོགས་པ་ཁྱད་པར་དུ་བྱ་བའི་ཕྱིར་རོ། །

[Block 17]
གཞན་དོན་ཕུན་སུམ་ཚོགས་པ་ནི་སྒྲོལ་བའི་དོན་གྱིས་ན་སྐྱོབ་པ་ཉིད་དོ། །

[Block 18]
དེ་ལྟ་བུའི་ཡོན་ཏན་ཅན་གྱི་སྟོན་པ་ལ་ཕྱག་འཚལ་ནས། ཚད་མ་བསྒྲུབ་པར་བྱ་བའི་ཕྱིར་རང་གི་རབ་ཏུ་བྱེད་པ་རིགས་པའི༌[^5]སྒོ་ལ་སོགས་པ་རྣམས་ལས་འདིར་གཅིག་ཏུ་བཏུས་ཏེ། ཚད་མ་ཀུན་ལས་བཏུས་པ་བརྩམ་པར་བྱའོ། །

[Block 19]
གཞན་གྱི་ཚད་མ་དགག་པར་བྱ་བའི་ཕྱིར་དང་། རང་གི་ཚད་མའི་ཡོན་ཏན་བརྗོད་པར་བྱ་བའི་ཕྱིར་ཏེ།[^6] གང་གི་ཕྱིར་གཞལ་བྱ་རྟོགས་པ་ནི་ཚད་མ་ལ་རག་ལས་པ་ཡིན་ལ།[^7] འདི་ལ་ཡང་ལོག་པར་རྟོག་པ༌[^8]མང་བས་ནའོ། །

[Block 20 [HEADING]]
### ཚད་མ་གཉིས་ཁོ་ན། ^1-2-0

[Block 21]
དེ་ལ། མངོན་སུམ་དང་ནི་རྗེས་སུ་དཔག །ཚད་མ་གཉིས་ཁོ་ནའོ། །གང་གི་ཕྱིར་ཞེ་ན། མཚན་ཉིད་གཉིས་གཞལ་བྱ། རང་དང་སྤྱིའི༌[^9]མཚན་ཉིད་དག་ལས་གཞན་པའི་མཚན་ཉིད་གཞལ་བར་བྱ་བ་གཞན་ནི་མེད་དོ། །

[Block 22]
རང་གི་མཚན་ཉིད་ཀྱི་ཡུལ་ཅན་ནི་མངོན་སུམ་ལ། སྤྱིའི་མཚན་ཉིད་ཀྱི་ཡུལ་ཅན་ནི་རྗེས་སུ་དཔག་པའོ་ཞེས་ཤེས་པའོ། །

[Block 23]
གལ་ཏེ་འདི་མི་རྟག་ཅེས་བྱ་བ་ལ་སོགས་པའི་རྣམ་པས་ཁ་དོག་ལ་སོགས་པ་འཛིན་པ་དང་། ལན་ཅིག་མ་ཡིན་པ་འཛིན༌[^10]དེ་ཇི་ལྟར་ཞེ་ན། དེ་ལྟར་འཛིན་པ་ནི་ཡོད་མོད་ཀྱིས༌[^11]འོན་ཀྱང་གཞལ་བྱ་དེའི་རབ་སྦྱོར་བས། དེ་ལ་རབ་སྦྱོར་ཚད་མ་གཞན་མ་ཡིན། རང་དང་སྤྱིའི་མཚན་ཉིད་ཐ་སྙད༌[^12]དུ་མ་བྱས་པ་དང་ཁ་དོག་ཉིད་དག་ལས་ཁ་དོག་ལ་སོགས་པ་གཟུང༌[^13]ནས་སྤྱིའི་མཚན་ཉིད་ནི་ཁ་དོག་ལ་སོགས་པ་མི་རྟག་གོ་ཞེས་མི་རྟག་པ་ཉིད་ལ་སོགས་པར་ཡིད་ཀྱིས་རབ་ཏུ་སྦྱོར་བར་བྱེད་དོ། །

[Block 24]
དེའི་ཕྱིར་ཚད་མ་གཞན་མ་ཡིན་ནོ། །

[Block 25]
ཡང་ཡང་ཤེས་པའང་མ་ཡིན་ཏེ། གང་ལན་ཅིག་མ་ཡིན་པར་དོན་དེ་ཉིད་སོ་སོར་ངོ་ཤེས་པ་ཡོད་མོད། དེ་ལྟར་ན་ཡང་ཚད་མ་གཞན་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། ཐུག་པ་མེད་འགྱུར། གལ་ཏེ་ཤེས་པ་ཐམས་ཅད་ཚད་མ་ཉིད་དུ་འདོད་པ་དེ་ལྟ་ན་ནི་ཚད་མ་ཐུག་པ་མེད་པ་ཉིད་དུ༌[^14]འགྱུར་ཏེ། དྲན་སོགས་བཞིན། དྲན་པ་ནི་དྲན་པ་ཉིད་དོ། །

[Block 26]
དཔེར་ན་དྲན་པ་དང་། འདོད་པ་དང་། ཞེ་སྡང་ལ་སོགས་པ་སྔར་རྟོག་པའི༌[^15]དོན་ལ་ཚད་མ་གཞན་མ་ཡིན་པ་བཞིན་ནོ། །

[Block 27 [HEADING]]
### མངོན་སུམ་རྟོག་དང་བྲལ་བ། ^1-3-0

[Block 28]
དེ་ལ། མངོན་སུམ་རྟོག་དང་བྲལ་བའོ། །ཤེས་པ་གང་ལ་རྟོག་པ་མེད་པ་དེ༌[^16]མངོན་སུམ་མོ། །

[Block 29 [HEADING]]
#### རྟོག་པ། ^1-3-1-0

[Block 30]
རྟོག་པ་ཞེས་བྱ་བ་འདི་ཇི་ལྟ་བུ་ཞིག་ཡིན་ཞེ་ན། མིང་དང་རིགས་སོགས༌[^17]སུ་སྦྱོར་བའོ། །

[Block 31]
འདོད་རྒྱལ་བའི་སྒྲ་རྣམས་ལ་མིང་གི་ཁྱད་པར་དུ༌[^18]བྱས་ནས༌[^19]རྗོད་པར་བྱེད་དེ། ལྷ་སྦྱིན་ཞེས་བྱ་བ་དང་། རིགས་ཀྱི་སྒྲ་རྣམས་ལ་ཅི་སྟེ་བ་ལང་ཞེས་བྱ་བ་དང་། ཡོན་ཏན་གྱི་སྒྲ་རྣམས་ལ་ཡོན་ཏན་གྱིས་ཏེ་དཀར་པོ་ཞེས་བྱ་བ་དང་། བྱ་བའི་སྒྲ་རྣམས་ལ་བྱ་བའི་སྒོ་ནས་ཏེ་འཚེད་པ༌[^20]ཞེས་བྱ་བ་དང་། རྫས་ཀྱི་སྒྲ་རྣམས་ལ་རྫས་ཀྱི་སྒོ་ནས་ཏེ། དབྱུག་པ་ཅན་རྭ་ཅན་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 32]
འདི་ལ་ཁ་ཅིག་ན་རེ་འབྲེལ་པ་ཁྱད་པར༌[^21]དུ་བྱས་པའི་སྒྲ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 33]
གཞན་དག་ནི་དོན་གྱིས་སྟོང་པའི་སྒྲ་འབའ་ཞིག་གིས་དོན་རྣམས་ཁྱད་པར་དུ༌[^22]བྱས་ཤིང་བརྗོད་དོ་ཞེས་འདོད་དོ། །

[Block 34]
གང་ལ་རྟོག་པ་དེ་དག་མེད་པ་དེ་མངོན་སུམ་མོ། །

[Block 35 [HEADING]]
#### དེ་ཡི་ཐ་སྙད་དབང་པོ་ལས། ^1-3-2-0

[Block 36]
ཅི་གང་གི་ཕྱིར་གཉིས་ལ་བརྟེན་ནས། སྐྱེས་པའི༌[^23]རྣམ་པར་ཤེས་པའི་དབང་པོ་ལ་བརྟེན་པའོ་ཞེས་བརྗོད་ཀྱི་ཡུལ་ལ་བརྟེན་པ་མ༌[^24]ཡིན་ཞེ་ན།

[Block 37 [VERSE]]
ཐུན་མོང་མིན་པའི༌[^25]རྒྱུའི་ཕྱིར། །
དེ་ཡི་ཐ་སྙད་དབང་པོ་ལས། །

[Block 38]
ཡུལ་གཟུགས་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 39]
འདི་ལྟར་ཡུལ་ནི་རྒྱུད་གཞན་གྱི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་ཡང་ཐུན་མོང་ཡིན་ནོ། །

[Block 40]
ཐུན་མོང་མ་ཡིན་པ་ལ་ཐ་སྙད་བྱེད་པ་ཡང་མཐོང་སྟེ། དཔེར་ན་རྔའི་སྒྲ་ནས་ཀྱི་མྱུ་གུ་ཞེས་པ་བཞིན་ནོ། །
--- END BLOCKS ---
