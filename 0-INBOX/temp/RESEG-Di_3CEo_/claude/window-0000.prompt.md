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
## ༄༅། །ཆོས་མངོན་པའི་འགྲེལ་པ་གནད་ཀྱི་སྒྲོན་མ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ཨ་བྷི་དྷརྨ་མརྨ་པྲ་དཱི་པ་ནཱ༌[^1]མ་བྲྀཏྟི།[^2] བོད་སྐད་དུ། ཆོས་མངོན་པའི་འགྲེལ་པ་གནད་ཀྱི་སྒྲོན་མ་ཞེས་བྱ་བ། སངས་རྒྱས་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [HEADING]]
## ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་བསྟན་པ། ^1-0

[Block 5 [HEADING]]
### ཕྱག་འཚལ་བ། ^1-1-0

[Block 6 [VERSE]]
གང་ཞིག་ཀུན་ལ་མུན་པ་གཏན་བཅོམ་ཞིང་། །
འཁོར་བའི་འདམ་ལས་འགྲོ་བ་དྲངས་མཛད་པ། །
དོན་བཞིན་སྟོན་པ་དེ་ལ་ཕྱག་འཚལ་ནས། །
ཆོས་མངོན་མཛོད་ཀྱི་བསྟན་བཅོས་རབ་བཤད་བྱ། །

[Block 7]
བསྟན་བཅོས་བྱེད་པར་འདོད་པས་རང་གི་སྟོན་པའི་ཆེ་བའི་བདག་ཉིད་ཤེས་པར་བྱ་བའི་ཕྱིར། དེ་ལ་ཡོན་ཏན་བརྗོད་པ་སྔོན་དུ་འགྲོ་བས་ཕྱག་འཚལ་བ་རྩོམ་སྟེ། གང་ཞིག་ཅེས་བྱ་བ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི་དབང་དུ་བྱས་ནས་སྨྲས་པའོ། །

[Block 8]
འདིའི་འམ་འདིས་མུན་པ་བཅོམ་པས་མུན་པ་བཅོམ་པའོ། །

[Block 9]
ཐམས་ཅད་ལ་མུན་པ་རྣམ་པ་ཐམས་ཅད་དུ་བཅོམ་པས་ཀུན་ལ་མུན་པ་གཏན་བཅོམ་པའོ། །

[Block 10]
མི་ཤེས་པ་ནི་ཡང་དག་པའི་དོན་མཐོང་བ་ལ་བགེགས་སུ་གྱུར་པའི་ཕྱིར་མུན་པ་སྟེ། དེ་ཡང་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^3]གཉེན་པོ་བརྙེས་ནས་ཤེས་བྱ་ཐམས་ཅད་ལ་ཕྱིས་མི་སྐྱེ་བའི་ཆོས་ཅན་དུ་གྱུར་པའི་ཕྱིར་གཏན་ནས་ཡེ་བཅོམ་པ་སྟེ། དེའི་ཕྱིར་ཀུན་ལ་མུན་པ་གཏན་བཅོམ་པའོ། །

[Block 11]
རང་སངས་རྒྱས་དང་ཉན་ཐོས་རྣམས་ཀྱང་ཉོན་མོངས་པ་ཅན་གྱི་རྨོངས་པ་དང་བྲལ་བའི་ཕྱིར་ཀུན་ལ་མུན་པ་བཅོམ་པར་ནི་འདོད་མོད་ཀྱི་གཏན་ནས་ནི་མ་ཡིན་ཏེ། འདི་ལྟར་དེ་དག་ལ་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་མི་ཤེས་པ་ཡོད་པ་ཉིད་དོ། །

[Block 12]
འཁོར་བའི་འདམ་ལས་འགྲོ་བ་དྲངས་མཛད་པ། །ཞེས་བྱ་བ་ནི་གཞན་ལ་ཕན་པ་སྒྲུབ་པས་བསྟོད༌[^4]པའོ། །

[Block 13]
འཁོར་བ་ནི་འགྲོ་བ་ཀུན་དུ་ཆགས་པའི་གནས་ཡིན་པའི་ཕྱིར་དང་། རྒལ་བར༌[^5]དཀའ་བ་ཡིན་པའི་ཕྱིར་འདམ་ལྟ་བུ་ཡིན་ཏེ། འགྲོ་བ་དེར་བྱིང་བ་དྲངས་སོ། །

[Block 14]
དོན་བཞིན་སྟོན་པ་ཞེས་བྱ་བ་ནི་འདིས་འདིའི་གཞན་ལ་ཕན་པ་སྒྲུབ་པའི་ཐབས་སྟོན་ཏེ། དེ་ནི་སྟོན་པ་ན་ཡང་དག་པའི༌[^6]ལྟ་བ་བཞིན་དུ་སྟོན་པས་འཁོར་བའི་འདམ་ལས་འགྲོ་བ་དྲངས་ཀྱི། རྫུ་འཕྲུལ་དང་དམ་པ་སྦྱིན་པའི་མཐུས་ནི་མ་ཡིན་ནོ། །

[Block 15]
དེ་ལ་ཕྱག་འཚལ་ནས་ཞེས་བྱ་བ་ནི་དུས་དང༌[^7]པོར་བྱ་བ་བརྗོད་ནས་བསྟན་བཅོས་རབ་བཤད་བྱ་ཞེས་སྨྲས་ཏེ། བསྟན་བཅོས་གང་ཞེ་ན། ཆོས་མངོན་པ༌[^8]མཛོད་ཅེས་བྱ་བའོ།[^9] །

[Block 16 [HEADING]]
### ཆོས་མངོན་པ། ^1-2-0

[Block 17]
ཆོས་མངོན་པ༌[^10]ཞེས་བྱ་བ་ནི༌[^11]གང་ཞེ་ན།

[Block 18 [VERSE]]
ཆོས་མངོན་ཤེས་རབ་དྲི་མེད་རྗེས་འབྲང་བཅས། །
ཤེས་རབ་ནི་ཆོས་རབ་ཏུ་རྣམ་པར་འབྱེད་པའོ། །
དྲི་མེད་ཅེས་བྱ་བ་ནི་ཟག་པ་མེད་པའོ། །

[Block 19]
རྗེས་འབྲང་བཅས་ཞེས་བྱ་བ་ནི་འཁོར་དང་བཅས་པའོ། །

[Block 20]
དེ་ལྟར་ན་ཟག་པ་མེད་པའི་ཕུང་པོ་ལྔ་ནི་ཆོས་མངོན་པ་ཞེས་བརྗོད་པར་འགྱུར་རོ། །

[Block 21]
རེ་ཞིག་འདི་ནི་དོན་དམ་པའི་ཆོས་མངོན་པའོ། །

[Block 22]
བརྡར་བཏགས་པ༌[^12]ཡང་། དེ་ཐོབ་བྱ་ཕྱིར་གང་དང་བསྟན་བཅོས་གང་། །གང་དང་ནི་ཐོས་པ་དང་བསམས་པ་དང་བསྒོམས་པ༌[^13]ལས་བྱུང་བའི་ཤེས་རབ་ཟག་པ་དང་བཅས་པ་དང་། སྐྱེས་ནས་ཐོབ་པ་རྗེས་སུ་འབྲང་བ་དང་བཅས་པའོ། །

[Block 23]
བསྟན་བཅོས་གང་ཞེས་བྱ་བ་ནི་ཤེས་རབ་དེ་ཐོབ་པར་བྱ་བའི་ཕྱིར་དེ་ཡང་དེའི་ཚོགས་སུ་གྱུར་པས་ཆོས་མངོན་པ་ཞེས་བརྗོད་དོ། །

[Block 24]
ངེས་པའི་ཚིག་ཏུ་ན་རང་གི་མཚན་ཉིད་འཛིན་པའི་ཕྱིར་ཆོས་ཏེ། དེ་ལྟ་བས་ན་འདི་ནི་དོན་དམ་པའི་ཆོས་མྱ་ངན་ལས་འདས་པའམ། ཆོས་ཀྱི༌[^14]མཚན་ཉིད་ལ་མངོན་དུ་ཕྱོགས་པའི་ཕྱིར་ཆོས་མངོན་པའོ། །

[Block 25 [HEADING]]
### ཆོས་མངོན་པའི་མཛོད། ^1-3-0

[Block 26]
བསྟན་བཅོས་འདི་ཇི་ལྟར་ན་ཆོས་མངོན་པའི་མཛོད་ཡིན་ཞེ་ན།

[Block 27 [VERSE]]
འདིར་དེ་དོན་དུ་ཡང་དག་ཆུད་ཕྱིར་རམ། །
འདི་ཡི་གནས་དེ་ཡིན་པས་ཆོས་མངོན་མཛོད། །

[Block 28]
ཅེས་བྱ་བ་ཆོས་མངོན་པའི་བསྟན་བཅོས་འདི་ནི་དེའི་མཛོད་ལྟ་བུ་ཡིན་ནོ། །

[Block 29]
ཡང་ན་དེ་ལས་འདི་ཕྱུང་བས་ཆོས་མངོན་པ་དེ་བསྟན་བཅོས་འདིའི་གནས་ལྟ་བུ་ཡིན་ནོ། །

[Block 30]
དེའི་ཕྱིར་ཆོས་མངོན་པ་དེ་ཉིད་འདིའི་མཛོད་ཡིན་ཏེ། དེ་ལྟ་བས་ན་བསྟན་བཅོས་འདི་ནི་ཆོས་མངོན་པའི་མཛོད་ཡིན་ནོ། །

[Block 31 [HEADING]]
### ཆོས་མངོན་པ་བསྟན་པ། ^1-4-0

[Block 32]
ཡང་ན༌[^15]ཅིའི་ཕྱིར་ཆོས་མངོན་པ་བསྟན་པའམ་འདི་དང་པོ་ཉིད་དུ་སུས་བསྟན་ཞེ་ན། གསུངས་པ།

[Block 33 [VERSE]]
ཆོས་རྣམས་རབ་ཏུ་རྣམ༌[^16]འབྱེད་མེད་པར་ཉོན་མོངས་རྣམས། །
གང་ཕྱིར་ཉེ་བར་ཞི་བར་བྱ་བའི་ཐབས་མེད་ལ། །
ཉོན་མོངས་པས་ཀྱང་འཇིག་རྟེན་སྲིད་མཚོ་འདིར་འཁྱམས་ཏེ། །
དེ་བས་དེ༌[^17]ཕྱིར་འདི་ནི་སྟོན་པས་གསུངས་སོ་ལོ། །

[Block 34]
གང་གི་ཕྱིར་ཆོས་རབ་ཏུ་རྣམ་པར་འབྱེད་པ་མེད་པར་ཉོན་མོངས་པ་ཉེ་བར་ཞི་བར་བྱ་བའི་ཐབས་མེད་ལ། ཉོན་མོངས་པ་རྣམས་ཀྱིས་ཀྱང་འཇིག་རྟེན་འཁོར་བར་འཁྱམ་པར༌[^18]བྱེད་པ་སྟེ། དེའི་ཕྱིར་ནི་ཆོས་རབ་ཏུ་རྣམ་པར་འབྱེད་པ་དེའི་དོན་དུ་སྟོན་པས་ནི་སངས་རྒྱས་ཀྱི༌[^19]ཆོས་མངོན་པ་གསུངས་སོ་ལོ། །

[Block 35]
ཆོས་མངོན་པ༌[^20]བསྟན་པ་མེད་པར་ནི་སློབ་མས་ཆོས་རབ་ཏུ་རྣམ་པར༌[^21]དབྱེ་བར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 36 [HEADING]]
### ཆོས་ཐམས་ཅད་མདོར་བསྡུས་ཏེ་བསྟན་པ། ^1-5-0

[Block 37]
ཆོས་དེ་དག་ཀྱང་གང་ཞེ་ན། ཟག་བཅས་ཟག་པ་མེད་ཆོས་རྣམས། །ཞེས་བྱ་བ་སྨོས་ཏེ། [^22]འདི་ནི་ཆོས་ཐམས་ཅད་མདོར་བསྡུས་ཏེ་བསྟན་པའོ། །

[Block 38 [HEADING]]
#### ཟག་པ་དང་བཅས་པའི་ཆོས། ^1-5-1-0

[Block 39]
དེ་ལ་ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་གང་ཞེ་ན། ལམ་མ་གཏོགས་པའི་འདུས་བྱས་རྣམས། །ཟག་བཅས་ཞེས་སྨོས་སོ། །

[Block 40]
ལམ་གྱི་བདེན་པ་མ་གཏོགས་པ་འདུས་བྱས་ཀྱི་ཆོས་གཞན་རྣམས་ནི་ཟག་པ་དང་བཅས་པ་དག་གོ། །ཅིའི་ཕྱིར་ཞེ་ན། གང་གི་ཕྱིར་དེ་དག་ལ། ཟས༌[^23]རྣམས་ཀུན་དུ་རྒྱས་པར་འགྱུར། །ཞེས་བྱ་སྟེ། འདི་རྣམས་ལ་ཟག་པ་རྣམས་རྒྱས་པར་འགྱུར་ཏེ། འགོག་པ་དང་ལམ་གྱི་བདེན་པ་དག་ལ་དམིགས་པ་ཡིན་དུ་ཟིན་ཀྱང་རྒྱས་པར་ནི་མི་འགྱུར་རོ། །
--- END BLOCKS ---
