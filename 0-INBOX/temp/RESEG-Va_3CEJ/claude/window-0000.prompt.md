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
### ༄༅། །ཆོས་མངོན་པའི་མཛོད་ཀྱི་བཤད་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ཨ་བྷི་དྷརྨྨ་ཀོ་ཥཾ་བྷཱ་ཥྱཾ། བོད་སྐད་དུ། ཆོས་མངོན་པའི་མཛོད་ཀྱི་བཤད་པ།

[Block 4 [VERSE]]
འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་ལ་ཕྱག་འཚལ་ལོ། །
གང་ཞིག་ཀུན་ལ་མུན་པ་གཏན་བཅོམ་ཞིང་། །
འཁོར་བའི་འདམ་ལས་འགྲོ་བ་དྲངས་མཛད་པ། །
དོན་བཞིན་སྟོན་པ་དེ་ལ་ཕྱག་འཚལ་ནས། །

[Block 5]
ཆོས་མངོན་མཛོད་ཀྱི་བསྟན་བཅོས་རབ་བཤད་བྱ། །བསྟན་བཅོས་བྱེད་པར་འདོད་པས་རང་གི་སྟོན་པའི་ཆེ་བའི་བདག་ཉིད་ཤེས་པར་བྱ་བའི་ཕྱིར་དེ་ལ་ཡོན་ཏན་བརྗོད་པ་སྔོན་དུ་འགྲོ་བའི་ཕྱག་འཚལ་བ་རྩོམ༌[^1]མོ། །

[Block 6]
གང་ཞིག་ཅེས་བྱ་བ་ནི། སངས་རྒྱས་བཅོམ་ལྡན་འདས༌[^2]ཀྱི་དབང་དུ་བྱས་ནས་སྨྲས་པའོ། །

[Block 7]
འདིའི་འམ་འདིས༌[^3]མུན་པ་བཅོམ་པས་མུན་པ་བཅོམ་པའོ། །

[Block 8]
ཐམས་ཅད་ལ་མུན་པ་རྣམ་པ་ཐམས་ཅད་དུ་བཅོམ་པས་ཀུན་ལ་མུན་པ་གཏན་བཅོམ་པའོ། །

[Block 9]
མི་ཤེས་པ་ནི་ཡང་དག་པའི་དོན་མཐོང་བ་ལ་བགེགས་སུ་གྱུར་པའི་ཕྱིར་མུན་པ་སྟེ། དེ་ཡང་སངས་རྒྱས་བཅོམ་ལྡན་འདས༌[^4]ཀྱིས་གཉེན་པོ་བརྙེས་ནས་ཤེས་བྱ་ཐམས་ཅད་ལ་ཕྱིས་མི་སྐྱེ་བའི་ཆོས་ཅན་དུ་གྱུར་པའི་ཕྱིར་གཏན་ནས་ཡེ་བཅོམ་པ་སྟེ། དེའི་ཕྱིར་འདིའི༌[^5]ནི་ཀུན་ལ་མུན་པ་གཏན་བཅོམ་པའོ། །

[Block 10]
དེ༌[^6]རང་སངས་རྒྱས་དང་ཉན་ཐོས་རྣམས་ཀྱང་ཉོན་མོངས་པ་ཅན་གྱི་རྨོངས་པ༌[^7]དང་བྲལ་བའི་ཕྱིར་ཀུན་ལ་མུན་པ་བཅོམ་པར་ནི་འདོད་མོད་ཀྱི་གཏན་ནས་ནི་མ་ཡིན་ཏེ་འདི་ལྟར་དེ་དག་ལ་སངས་རྒྱས་ཀྱི་ཆོས་དང་། ཡུལ་དང་། དུས་ཤིན་ཏུ་བསྐལ་པ་དང་། དོན་རབ་ཏུ་དབྱེ་བ་མཐའ་ཡས་པ་རྣམས་ལ་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་མི༌[^8]ཤེས་པ་ཡོད་པ་ཉིད་དོ། །

[Block 11]
དེ་ལྟར་བདག་ལ་ཕན་པ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པས་ཡང་དག་པར་བསྟོད་ནས། ཡང་བཅོམ་ལྡན་འདས་དེ་ཉིད་ལ་གཞན་ལ་ཕན་པ་སྒྲུབ་པ༌[^9]ཕུན་སུམ་ཚོགས་པས་ཡང་དག་པར་བསྟོད་པ་ནི། འཁོར་བའི་འདམ་ལས་འགྲོ་བ་དྲངས་མཛད་པ། །ཞེས་བྱ་བ་སྟེ། འཁོར་བ་ནི་འགྲོ་བ་ཀུན་ཏུ་ཆགས་པའི༌[^10]གནས་ཡིན་པའི་ཕྱིར་དང་། བརྒལ་བར༌[^11]དཀའ་བའི་ཕྱིར་འདམ་ལྟ་བུ་ཡིན་ཏེ། འགྲོ་བ་དེར་བྱིང་བ་སྐྱབས་མེད་པ་ལ་བཅོམ་ལྡན་འདས་ཐུགས་བརྩེ་བ་དང་ལྡན་པས་དམ་པའི་ཆོས་སྟོན་པའི་ཕྱག་བརྐྱང་བ་དག་གིས་སྐལ་བ་ཇི་ལྟ་བ་བཞིན་དུ་དྲངས་སོ། །

[Block 12]
དོན་ཇི་ལྟ་བ་བཞིན་ཕྱིན་ཅི་མ་ལོག་པར་སྟོན་པས་ན་དོན་བཞིན་སྟོན་པའོ། །

[Block 13]
འདིས་ནི་འདིའི་གཞན་ལ་ཕན་པ་སྒྲུབ་པའི་ཐབས་སྟོན་ཏེ། དེ་ནི་སྟོན་པ་ན༌[^12]ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་སྟོན་པས་འཁོར་བའི་འདམ་ལས་འགྲོ་བ་དྲངས་ཀྱི་རྫུ་འཕྲུལ་དང་། དམ་པ་སྦྱིན་པའི་མཐུས་ནི་མ་ཡིན་ནོ། །

[Block 14]
དེ་ལྟར་བདག་དང་གཞན་ལ་ཕན་པ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་དེ་ལྟ་བུ་དང་ལྡན་པ་གང་ཡིན་པ་དེ་ལ་ཕྱག་འཚལ་ནས་ཞེས་བྱ་བ་ནི་མགོས་བཏུད་ནས་སོ། །

[Block 15]
དོན་བཞིན་སྟོན་པ་དེ་ལ་ཕྱག་འཚལ་ནས་ཅི་ཞིག་བྱ་ཞེ་ན། བསྟན་བཅོས་རབ་བཤད་བྱ་ཞེས་བྱ་བ༌[^13]སྨོས་ཏེ།[^14] སློབ་མ་འཆོས་པས་ན་བསྟན་བཅོས་སོ། །

[Block 16]
བསྟན་བཅོས་གང་ཞེ་ན། ཆོས་མངོན་མཛོད་ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 17]
ཆོས་མངོན་པ་ཞེས་བྱ་བ་འདི་གང་ཞེ་ན། ཆོས་མངོན་ཤེས་རབ་དྲི་མེད་རྗེས་འབྲང་བཅས། །ཞེས་བྱ་བ་སྟེ། དེ་ལ་ཤེས་རབ་ཅེས་བྱ་བ་ནི། ཆོས་རབ་ཏུ་རྣམ་པར་འབྱེད་པའོ། །

[Block 18]
དྲི་མེད་ཅེས་བྱ་བ་ནི་གང་ཟག་པ་མེད་པའོ། །

[Block 19]
རྗེས་འབྲང་བཅས༌[^15]ཞེས་བྱ་བ་ནི་འཁོར་དང་བཅས་པ་སྟེ། དེ་ལྟར་ན་ཟག་པ་མེད་པའི་ཕུང་པོ་ལྔ་པོ་ལ་ཆོས་མངོན་པ་ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 20]
རེ་ཞིག་འདི་ནི་དོན་དམ་པའི་ཆོས་མངོན་པའོ། །

[Block 21]
བརྡར་བཏགས་པ་ནི། དེ་ཐོབ་བྱའི༌[^16]ཕྱིར་གང་དང་བསྟན་བཅོས་གང་ཞེས་བྱ་བ༌[^17]སྟེ། གང་དང་ཞེས་བྱ་བ་ནི་ཐོས་པ་དང་བསམས་པ་དང་བསྒོམས་པ་ལས་བྱུང་བའི་ཤེས་རབ་གང༌[^18]ཟག་པ་དང་བཅས་པ་དང་། སྐྱེས་ནས་ཐོབ་པ་རྗེས་སུ་འབྲང་བ་དང་བཅས་པའོ། །

[Block 22]
བསྟན་བཅོས་གང་ཞེས་བྱ་བ་ནི་དེ་ཡང་ཟག་པ་མེད་པའི༌[^19]ཤེས་རབ་ཐོབ་པར་བྱ་བའི་ཕྱིར་དེའི་ཚོགས་སུ་གྱུར་པས་ཆོས་མངོན་པ་ཞེས་བྱའོ། །

[Block 23]
ངེས་པའི་ཚིག་ཏུ་རང་གི་མཚན་ཉིད་འཛིན་པའི་ཕྱིར༌[^20]ཆོས་ཏེ། དེ་ལྟ་བས་ན་འདི་ནི་དོན་དམ་པའི་ཆོས་མྱ་ངན་ལས་འདས་པ་འམ། ཆོས་ཀྱི་མཚན་ཉིད་ལ་མངོན་དུ་ཕྱོགས་པའི་ཕྱིར་ཆོས་མངོན་པའོ། །

[Block 24]
ཆོས་མངོན་པ་བཤད་ཟིན་ཏོ། །

[Block 25]
བསྟན་བཅོས་འདི་ཇི་ལྟར་ན་ཆོས་མངོན་པའི་མཛོད་ཡིན་ཞེ་ན། འདིར་དེ་དོན་དུ་ཡང་དག་ཆུད་ཕྱིར་རམ། འདི་ཡི་གནས་དེ་ཡིན་པས་ཆོས་མངོན་མཛོད་ཅེས་བྱ་བ༌[^21]སྨོས་ཏེ། ཆོས་མངོན་པའི་བསྟན་བཅོས་ཞེས་བྱ་བ་དེ་ཇི་ལྟར་གཅེས་གཅེས་རྣམས་དོན་དུ་འདིར་ཆུད་དེ། དེ་ལྟ་བས་ན་བསྟན་བཅོས་འདི་ནི་དེའི་མཛོད་ལྟ་བུ་ཡིན་ནོ། །

[Block 26]
ཡང་ན་དེ་ལས་འདི་ཕྱུང་བས་ཆོས་མངོན་པ་དེ་བསྟན་བཅོས་འདིའི་གནས་ལྟ་བུ་ཡིན་ནོ། །

[Block 27]
དེའི་ཕྱིར་ཆོས་མངོན་པ་དེ་ཉིད་འདིའི་མཛོད་ཡིན་ཏེ། དེ་ལྟ་བས་ན་བསྟན་བཅོས་འདི་ནི་ཆོས༌[^22]མངོན་པའི་མཛོད་ཡིན་ནོ། །

[Block 28]
ཡང་ཅིའི་ཕྱིར་ཆོས་མངོན་པ་བསྟན། འདི་དང་པོ་ཉིད་དུ་སུས༌[^23]བསྟན་ན། འདི་ལྟར་སློབ་དཔོན་ཆོས་མངོན་པའི་མཛོད་འཆད་པར་གུས་ཤེ་ན།

[Block 29 [VERSE]]
ཆོས་རྣམས་རབ་ཏུ་རྣམ་འབྱེད་མེད་པར་ཉོན་མོངས་རྣམས། །
གང་ཕྱིར་ཉེ་བར་ཞི་བར་བྱ་བའི་ཐབས་མེད་ལ། །
ཉོན་མོངས་པས་ཀྱང་འཇིག་རྟེན་སྲིད་མཚོ་འདིར་འཁྱམས་ཏེ། །
དེ་བས་དེ་ཕྱིར་འདི་ནི་སྟོན་པས་གསུངས་སོ་ལོ། །

[Block 30]
ཞེས་བྱ་བ་སྨོས་ཏེ། གང་གི་ཕྱིར་ཆོས་རྣམས༌[^24]རབ་ཏུ་རྣམ་པར་འབྱེད་པ་མེད་པར་ཉོན་མོངས་པ་ཉེ་བར་ཞི་བར་བྱ་བའི་ཐབས་མེད་ལ། ཉོན་མོངས་པ་རྣམས་ཀྱིས་ཀྱང་འཇིག་རྟེན་འཁོར་བའི་རྒྱ་མཚོ་ཆེན་པོ་འདིར་འཁྱམ་པར་བྱེད་པ་དེའི་ཕྱིར་ཆོས་རྣམས་རབ་ཏུ་རྣམ་པར་འབྱེད་པར་འདོད་པ་དེའི་དོན་དུ་སྟོན་པ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས་ཆོས་མངོན་པ་གསུངས་སོ་ལོ། །

[Block 31]
ཆོས་མངོན་པ་བསྟན་པ་མེད་པར་ནི་སློབ་མས་ཆོས་རབ་ཏུ་རྣམ་པར་འབྱེད་པར༌[^25]མི་ནུས་སོ། །

[Block 32]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་དེ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་སིལ༌[^26]བུར་བཤད་ལ། བཙུན་པ་ཀཱ་ཏྱཱའི་བུ་ལ་སོགས་པས་བསྡུས་ནས་བཞག་སྟེ། བཙུན་པ་ཆོས་སྐྱོབ་ཀྱིས་ཆེད་དུ་བརྗོད་པའི་སྡེ། སྡེ་ཚན་དུ་བྱས་པ་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 33 [HEADING]]
## ཁམས་བསྟན་པ། ^1-0

[Block 34 [HEADING]]
### ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད། ^1-1-0

[Block 35 [HEADING]]
#### ཟག་བཅས་ཟག་པ་མེད་ཆོས་རྣམས། ^1-1-1-0

[Block 36]
གང་དག་ཆོས་མངོན་པ་བསྟན་པས་རབ་ཏུ་རྣམ་པར་དབྱེ་བར་བྱ་བའི་ཆོས་དེ་དག་ཀྱང་གང་ཞེ་ན། ཟག་བཅས་ཟག་པ་མེད་ཆོས་རྣམས། །ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ནི་ཆོས་རྣམས་ཐམས་ཅད་མདོར་བསྡུས་ཏེ་བསྟན་པའོ། །

[Block 37 [HEADING]]
##### ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས། ^1-1-1-1-0

[Block 38]
དེ་ལ་ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་གང་ཞེ་ན། ལམ་མ་གཏོགས་པ་འདུས་བྱས་རྣམས། །ཟག་བཅས་ཞེས་བྱ་བ༌[^27]སྟེ། ལམ་གྱི་བདེན་པ་མ་གཏོགས་པ་འདུས་བྱས་ཀྱི་ཆོས་གཞན་རྣམས༌[^28]ནི་ཟག་པ་དང་བཅས་པ་དག་གོ། །ཅིའི་ཕྱིར་ཞེ་ན། གང་ཕྱིར་དེ་དག་ལ། །ཟག་རྣམས་ཀུན་ཏུ་རྒྱས་པར་འགྱུར། །ཞེས་བྱ་བ༌[^29]སྟེ། འགོག་པ་དང་ལམ་གྱི་བདེན་པ་ལ་དམིགས་པས་ཀྱང༌[^30]ཟག་པ་སྐྱེ་བར་ནི་འདོད་མོད་ཀྱི། དེ་གཉིས་ལ་རྒྱས་པར་མི་འགྱུར་བས་དེ་གཉིས་ཟག་པ་དང་བཅས་པ་ཉིད་དུ་ཐལ་བ་མེད་དོ། །

[Block 39]
ཇི་ལྟར་རྒྱས་པར་མི་འགྱུར་བ་དེ་ནི་འོག་ནས་ཕྲ་རྒྱས་བསྟན་པ་ཉིད་དུ་བསྟན་པར་བྱའོ། །

[Block 40]
ཟག་པ་དང་བཅས་པ་དག་བཤད་ཟིན་ཏོ། །
--- END BLOCKS ---
