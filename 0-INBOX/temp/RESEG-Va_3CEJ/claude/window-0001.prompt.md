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

[Block 41 [HEADING]]
##### ཟག་པ་མེད་པའི་ཆོས་རྣམས། ^1-1-1-2-0

[Block 42]
ཟག་པ་མེད་པ་རྣམས་གང་ཞེ་ན།

[Block 43 [VERSE]]
ཟག་མེད་ལམ་གྱི་བདེན་པ་དང་། །
འདུས་མ་བྱས་རྣམ་གསུམ་ཡང་སྟེ། །

[Block 44]
ཞེས་བྱ་བའོ།

[Block 45]
[^31] །རྣམ་གསུམ་གང་ཞེ་ན། ནམ་མཁའ་དང་ནི་འགོག་པ་གཉིས། །ཞེས་བྱ་བ་སྟེ། གཉིས་གང་ཞེ་ན། སོ་སོར་བརྟགས་པས་འགོག་པ་དང་། སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་སྟེ། དེ་ལྟར་ནམ་མཁའ་ལ་སོགས་པ་འདུས་མ་བྱས་རྣམ་པ་གསུམ་པོ་དེ་དང་། ལམ་གྱི་བདེན་པ་ནི་ཟག་པ་མེད་པའི་ཆོས་རྣམས་ཏེ། དེ་དག་ལ་ཟག་པ་རྒྱས་པར་འགྱུར་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 46 [HEADING]]
###### ནམ་མཁའ། ^1-1-1-2-1-0

[Block 47]
འདུས་མ་བྱས་རྣམ་པ་གསུམ་པོ་བསྟན་པ་གང་ཡིན་པ་དེ་ལ་ནམ་མཁའ་མི་སྒྲིབ་པ། ནམ་མཁའ་ནི་སྒྲིབ་པ་མེད་པའི་རང་བཞིན་ཏེ་གང་ན་གཟུགས་ཀྱི་གོ་ཡོད་པའོ། །

[Block 48 [HEADING]]
###### སོ་སོར་བརྟགས་པས་འགོག་པ། ^1-1-1-2-2-0

[Block 49]
སོ་སོར་བརྟགས་པས་འགོག་པ་དང༌[^32]བྲལ་བའོ། །

[Block 50]
གང་ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་དང་བྲལ་བ་དེ་ནི༌[^33]སོ་སོར་བརྟགས་པས་འགོག་པའོ། །

[Block 51]
སྡུག་བསྔལ་ལ་སོགས་པ་འཕགས་པའི་བདེན་པ་རྣམས་ལ་སོ་སོར་རྟོག་པ་ནི་སོ་སོར་བརྟགས་པ་སྟེ་ཤེས་རབ་ཀྱི་བྱེ་བྲག་གོ། །

[Block 52]
དེས་ཐོབ་པར་བྱ་བའི་འགོག་པ་ནི་སོ་སོར་བརྟགས་པས་འགོག་པའོ། །

[Block 53]
བར་གྱི་ཚིག་མི་མངོན་པར་བྱ་བ་སྟེ། དཔེར་ན་བ་ལང་དག་དང་ལྡན་པའི་ཤིང་རྟ་ལ་བ་ལང་གི་ཤིང་རྟ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 54]
ཅི་ཟག་པ་དང་བཅས་པའི་ཆོས་ཐམས་ཅད་ཀྱི་སོ་སོར་བརྟགས་པས་འགོག་པ་གཅིག་ཁོ་ན་འམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 55]
འོ་ན་ཇི་ལྟ་བུ༌[^34]ཞེ་ན། སོ་སོ་སོ་སོ་ཡིན། ལྡན་པའི་རྫས་རྣམས་ཇི་སྙེད་པ་བྲལ་བའི་རྫས་རྣམས་ཀྱང་དེ་སྙེད་དོ། །

[Block 56]
དེ་ལྟ་མ་ཡིན་ན་སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བའི་ཉོན་མོངས་པའི་འགོག་པ་མངོན་སུམ་དུ་བྱས་པས་ཉོན་མོངས་པ་ཐམས་ཅད་འགོག་པ་མངོན་སུམ་དུ་བྱེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 57]
དེ་ལྟ་མ་ཡིན་ན་ལྷག་མའི་གཉེན་པོ་བསྒོམ་པ་དོན་མེད་པར་འགྱུར་རོ། །

[Block 58]
འོ་ན་འགོག་པ་ནི་འདྲ་བ་མ་ཡིན་ནོ་ཞེས་བཤད་པ་འདིའི་དོན་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན། ཚིག་དེའི་དོན་ནི་འདི་འདྲ་བའི་རྒྱུ་གང་ཡང་མ་ཡིན་ལ། འདི་ཡང་གང་གི་འདྲ་བའི་རྒྱུ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 59]
[^35]འདི་ལ་འདྲ་བ་གང་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 60]
སོ་སོར་བརྟགས་པས་འགོག་པ་བཤད་ཟིན་ཏོ། །

[Block 61 [HEADING]]
###### སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ། ^1-1-1-2-3-0

[Block 62 [VERSE]]
སྐྱེ་ལ་གཏན་དུ་བགེགས༌[^36]བྱེད་པ། །
འགོག་གཞན་སོ་སོར་བརྟགས་མིན་པས། །

[Block 63]
ཆོས་མ་འོངས་པ་རྣམས་སྐྱེ་བ་ལ་གཏན་དུ་བགེགས༌[^37]སུ་གྱུར་པ་བྲལ་བ་ལས་གཞན་པའི་འགོག་པ་གང་ཡིན་པ་དེ་ནི་སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་སྟེ། འདི་སོ་སོར་བརྟགས་པས་འཐོབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 64]
འོ་ན་ཅི་ཞེ་ན། རྐྱེན་མ་ཚང་བ་ལས༌[^38]ཐོབ་སྟེ། དཔེར་ན་མིག་དང་ཡིད་གཟུགས་གཅིག་ལ་ཡེངས་པའི་གཟུགས་གཞན་པ༌[^39]རྣམས་དང་སྒྲ་དང་དྲི་དང་རོ་དང་རེག་བྱ་གང་ཡིན་པ་དག་ནི་འདས་པར་འགྱུར་ལ། དེ་དག་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་པོ་དག་ནི་ཡང་སྐྱེ་བར་ཡང༌[^40]མི་ནུས་ཏེ། དེ་དག་འདས་པའི་ཡུལ་ལ་དམིགས་པའི་མཐུ་མེད་པའི་ཕྱིར་རོ། །

[Block 65]
དེའི་ཕྱིར་དེ་དག་གི་སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་དེ་ནི་རྐྱེན་མ་ཚང་བས་འཐོབ་བོ། །

[Block 66]
འདིར་མུ་བཞིར་འགྱུར་ཏེ། གང་དག་གིས༌[^41]སོ་སོར་བརྟགས་པས་འགོག་པ་ཁོ་ན་འཐོབ་པའི་ཆོས་དེ་དག་ཀྱང་ཡོད་དེ། འདི་ལྟ་སྟེ། ཟག་པ་དང་བཅས་པ་འདས་པ་དང་ད་ལྟར་བྱུང་བ་དང་འབྱུང་བའི་ཆོས་ཅན་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 67]
གང་དག་གིས༌[^42]སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་ཁོ་ན་འཐོབ་པ་ཡང་ཡོད་དེ། འདི་ལྟ་སྟེ། ཟག་པ་མེད་པའི་འདུས་བྱས་མི༌[^43]སྐྱེ་བའི་ཆོས་ཅན་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 68]
གང་དག་གིས༌[^44]གཉི་ག་འཐོབ་པ་ཡང་ཡོད་དེ། འདི་ལྟ་སྟེ། ཟག་པ་དང་བཅས་པ་མི་སྐྱེ་བའི་ཆོས་ཅན་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 69]
གང་དག་གིས༌[^45]གཉི་ག་མི་འཐོབ་པ་ཡང་ཡོད་དེ། འདི་ལྟ་སྟེ། ཟག་པ་མེད་པ་འདས་པ་དང་ད་ལྟར་བྱུང་བ་དང་འབྱུང་བའི་ཆོས་ཅན་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 70]
འདུས་མ་བྱས་རྣམ་པ་གསུམ་བཤད་ཟིན་ཏོ། །

[Block 71 [HEADING]]
#### འདུས་བྱས་ཀྱི་ཆོས་རྣམས། ^1-1-2-0

[Block 72]
ལམ་མ་གཏོགས་པ་འདུས་བྱས་རྣམས། །ཟག་བཅས་ཞེས་གང་སྨྲས་པའི་འདུས་བྱས་དེ་དག་གང་ཞེ་ན།

[Block 73 [VERSE]]
འདུས་བྱས་ཆོས་རྣམས་དེ་དག་ཀྱང་། །
གཟུགས་ལ་སོགས་པ་ཕུང་པོ་ལྔ། །

[Block 74]
གཟུགས་ཀྱི་ཕུང་པོ་དང་། ཚོར་བའི་ཕུང་པོ་དང་། འདུ་ཤེས་ཀྱི་ཕུང་པོ་དང་། འདུ་བྱེད་ཀྱི་ཕུང་པོ་དང་། རྣམ་པར་ཤེས་པའི་ཕུང་པོ་ཞེས་བྱ་བ་དེ་དག་ནི་འདུས་བྱས་ཀྱི་ཆོས་རྣམས་སོ། །

[Block 75]
རྐྱེན་རྣམས་འདུས་ཤིང་ཕྲད་ནས་བྱས་པ་དག་ནི་འདུས་བྱས་རྣམས་ཏེ། རྐྱེན་གཅིག་གིས་བསྐྱེད་པ་ནི་འགའ་ཡང་མེད་དོ། །
--- END BLOCKS ---
