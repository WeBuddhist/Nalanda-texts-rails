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
[Block 71]
འདི་ལ་ཕྱི་རོལ་པ་རྣམས་ཀྱི་བཞིན་དུ་ཚད་མ་ལས་འབྲས་བུ་དོན་གཞན་དུ་འགྱུར་བ་ནི་མེད་ཀྱི། འབྲས་བུར་གྱུར་པའི་ཤེས་པ་དེ་ཉིད་ཡུལ་གྱི་རྣམ་པ་ཅན་དུ་སྐྱེས་པ་དང་བྱ་བ་དང་བཅས་པར་རྟོགས་པ་དེ་ཉེ་བར་བླངས་ནས། ཚད་མ་ཉིད་དུ་འདོགས་པ༌[^33]སྟེ། བྱ་བ་མེད་པའང་མ་ཡིན་ནོ། །

[Block 72]
དཔེར་ན་འབྲས་བུ་རྒྱུ་དང་རྗེས་སུ་མཐུན་པར་སྐྱེས་པ་ལ་རྒྱུའི་གཟུགས་འཛིན་ཞེས་བརྗོད་དོ། །

[Block 73]
བྱ་བ་མེད་པར་ཡང་མ་ཡིན་པ་དེ་བཞིན་དུ་འདིར་ཡང་ཡིན་ནོ། །

[Block 74]
རང་རིག་ལ་ཡང་འདིར་འབྲས་བུ། །ཤེས་པ་ནི་སྣང་བ་གཉིས་ལས་སྐྱེས་ཏེ་རང་གི་སྣང་བ་དང་ཡུལ་གྱི་སྣང་བའོ། །

[Block 75]
སྣང་བ་དེ་གཉིས་ལས་གང་རང༌[^34]རིག་པ་དེ་ནི་འབྲས་བུར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་ཡི་ངོ་བོ་ལས་དོན་ངེས། གང་གི་ཚེ་ཤེས་པ་དོན་གྱི་ཡུལ་དང་བཅས་པའི༌[^35]དེའི་ཚེ། དེ་དང་རྗེས་སུ་མཐུན་པའི་རང་རིག་པ་འདོད་པའམ་མི་འདོད་པའི་དོན་རྟོགས་པར་བྱེད་དོ། །

[Block 76]
གང་གི་ཚེ་ཕྱི་རོལ་གྱི་དོན་འབའ་ཞིག་གཞལ་བྱར་བྱེད་པ་དེའི་ཚེ་ནི། ཡུལ་གྱི་སྣང་བ་འདི་ཉིད་འདི། །ཚད་མ་དེའི་ཚེ་ནི་ཤེས་པ་རང་རིག་པ་ཡིན་ཡང་ལྟོས་པ་མེད་པའི་རང་གི་ངོ་བོའི་དོན་གྱིས་སྣང་བ་འདི་ཚད་མའོ། །གང་གི་ཕྱིར་ཞེ་ན། དོན་དེ༌[^36]ཡིས་འཇལ་བར་བྱེད། ཇི་ལྟ་ཇི་ལྟར་དོན་གྱི་རྣམ་པ་དཀར་པོ་དང་དཀར་པོ་མ་ཡིན་པ་ལ་སོགས་པ་ཉིད་ཤེས་པ་ལ་སྣང་བ་ན་དེ་དང་དེའི་ངོ་བོའི༌[^37]ཡུལ་དང་བཅས་པར་འཇལ་བར་བྱེད་དེ། དེ་ལྟར༌[^38]རྣམ་པ་དུ་མ་རིག་པའི་ཤེས་པ་ཉེ་བར་བླངས་པ་དེ་ལྟ༌[^39]དེ་ལྟར་ཚད་མ་དང་གཞལ་བྱ་ཉིད་དུ་ཉེ་བར་འདོགས་པ་ཡིན་ཏེ། ཆོས་ཐམས་ཅད་ནི་བྱ་བ་དང་བྲལ་བ་ཡིན་པས་ནའོ། །

[Block 77]
དེ་ཉིད་སྨྲས་པ།

[Block 78 [VERSE]]
གང་ཚེ་རྣམ་པ་དེ་གཞལ་བྱ། །
ཚད་མ་དང་དེའི་འབྲས་བུ་ནི། །
འཛིན་རྣམས་རིགས༌[^40]པ་དེ་ཡི་ཕྱིར། །
དེ་གསུམ་ཐ་དད་དུ་མ་བྱས། །

[Block 79 [HEADING]]
#### ཤེས་པ་ཚུལ་གཉིས། ^1-3-8-0

[Block 80 [VERSE]]
ཅི་སྟེ་ཤེས་པ་ཚུལ་གཉིས་སོ། །
ཞེས་ཇི་ལྟར་རྟོགས་པར་བྱ་ཞེ་ན།
ཡུལ་ཤེས་པ་དང་དེའི་ཤེས་པའི།[^41] །
དབྱེ་བས་བློ་ཡི་ཚུལ་གཉིས་ཉིད།[^42] །

[Block 81]
ཡུལ་ནི་གཟུགས་ལ་སོགས་པ་སྟེ་གང་གིས་དེ་ཤེས་པ་ནི་དོན་དང་རང་སྣང་བའོ། །

[Block 82]
ཡུལ་ཤེས་པ་ནི་གང་ཡུལ་དང་རྗེས་སུ་མཐུན་པའི་ཤེས་པ་སྟེ། ཤེས་པ་དེ༌[^43]སྣང་བ་དང་། རང་སྣང་བའོ། །

[Block 83]
དེ་ལྟར་མ་ཡིན་ཏེ། གལ་ཏེ་གཟུགས་ཉིད་རང་ཤེས་པའམ་རང་གི་ངོ་བོར་འགྱུར་བ༌[^44]ནི་ཞེས་པ༌[^45]ཡང་ཡུལ་ཤེས་པ་དང་ཁྱད་པར་མེད་པར་འགྱུར་རོ། །

[Block 84]
ཕྱིས་རྗེས༌[^46]ལ་སྐྱེ་བའི་ཤེས་པ་ལ་ཡང་སྔར་རིང་དུ་འདས་པའི་ཡུལ་སྣང་བར་མི་འགྱུར་ཏེ། གང་གི་ཕྱིར་ཞེ་ན། དེ་ཡུལ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 85]
དེའི་ཕྱིར་ཤེས་པ་ལ་ཚུལ་གཉིས་ཡོད་པར་གྲུབ་བོ། །

[Block 86]
དུས་ཕྱིས་དྲན་པ་ལས་ཀྱང་སྟེ། ཚུལ་གཉིས་ཉིད་དོ་ཞེས་འབྲེལ་ཏོ། །

[Block 87]
གང་གི་ཕྱིར་ཡུལ་བཞིན༌[^47]དུ་ཤེས་པ་ལ་ཡང་དུས་ཕྱིས་མྱོང་བའི་དྲན་པ་སྐྱེ་སྟེ།[^48] དེའི་ཕྱིར་ཡང་ཤེས་པའི་ཚུལ་གཉིས་ཉིད་དུ་གྲུབ་པ་ཡིན་ནོ། །

[Block 88]
རང་རིག་པ་ཉིད་དུ་ཡང་ངོ་། །ཅིའི་ཕྱིར་ཞེ་ན། འདིར་མ་མྱོང་བ་མེད་ཕྱིར་རོ། །

[Block 89]
ཉམས་སུ་མ་མྱོང་བར་དོན་མཐོང་བའི་དྲན་པ་ནི་མེད་དོ། །

[Block 90]
གཟུགས་ལ་སོགས་པའི་དྲན་པ་བཞིན་ནོ། །

[Block 91]
ཅི་སྟེ་གཟུགས་ལ་སོགས་པ་བཞིན་དུ་ཤེས་པ༌[^49]ཡང་ཤེས་པ་གཞན་གྱིས་མྱོང་བ་ཡིན་ནོ་ཞེ་ན། [^50]དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། གང་གི༌[^51]ཕྱིར། ཤེས་པ་གཞན་གྱིས་ཉམས་མྱོང་ན། །ཐུག་མེད། ཐུག་པ་མེད་པ་ཞེས་བྱ་བ་ནི། ཤེས་པ་བཞིན༌[^52]གྱིས་མྱོང་བར་བྱེད་ནའོ། །ཇི་ལྟར་ཞེ་ན། དེ་ལའང་དྲན་པ་སྟེ། ཤེས་པ་གཞན་གྱིས་ཤེས་པ་དེ་ཉམས་སུ་མྱོང་བར་བྱེད་ན། དེ་ལ་ཡང་ཕྱིས་ཀྱི་དྲན་པ་མཐོང་དགོས་པས་སོ། །

[Block 92]
དེས་ན་དེ་ལ་ཡང་ཤེས་པ་གཞན་གྱིས་ཉམས་སུ་མྱོང་བ་ཡིན་ན་ནི་ཐུག་པ་མེད་པར་འགྱུར་རོ། །

[Block 93]
དེ་བཞིན་ཡུལ་གཞན་ལ་འཕོ་བ། །མེད་འགྱུར་དེ་ཡང་མཐོང་བ་ཉིད། །

[Block 94]
དེའི་ཕྱིར་གདོན་མི་ཟ་བར་རང་རིག་པའི་ཤེས་པ་ཁས་བླང་བར་བྱའོ། །

[Block 95]
དེ་ཡང་འབྲས་བུ་ཉིད་དུ་གནས་པར་གྲུབ། [^53]དེ་ལྟར་ན་མངོན་སུམ་རྟོག༌[^54]པ་དང་བྲལ་བ་ཡིན་ནོ། །

[Block 96]
[^55]དེའི་རྗེས་ལ༌[^56]

[Block 97 [HEADING]]
### གཞན་གྱིས་བྱས་པའི་མངོན་སུམ་བརྟག་པ། ^1-4-0

[Block 98]
གཞན་གྱིས་བྱས་པའི་མངོན་སུམ་བརྟག་པར་བྱ་སྟེ།

[Block 99 [HEADING]]
#### རྩོད་པ་བསྒྲུབ་པ། ^1-4-1-0

[Block 100 [VERSE]]
རྩོད་སྒྲུབ་སློབ་དཔོན་གྱིས༌[^57]མ་ཡིན། །
ངེས་པར་སྙིང་པོ་མེད་པར་དགོངས། །
གཞན་དུ་ཆ་ཤས་སུ་གསུང་འགྱུར། །
དེས་ན་ཁོ་བོས་བརྟག་པར་བྱའོ། །

[Block 101]
རྩོད་པ་བསྒྲུབ་པ༌[^58]ནི་སློབ་དཔོན་དབྱིག་གཉེན་གྱི་མ་ཡིན་ནོ། །

[Block 102]
གང་གི་ཕྱིར་རྩོད་པ་སྒྲུབ་པ་དེ་ལ་ནི་སློབ་དཔོན་གྱིས་སྙིང་པོ་མེད་པར་དགོངས་པ་སྟེ། དེ་ལྟ་མ་ཡིན་ན་ཆ་ཤས་ཅན་དུ་མཛད་པར་འགྱུར་རོ། །

[Block 103]
དེས་ན་ཁོ་བོས་ཀྱང་ཚད་མ་ལ་སོགས་པ་ཅུང་ཟད་ཅིག་བརྟག་པར་བྱའོ། །

[Block 104 [VERSE]]
དོན་དེ་ལས་སྐྱེས་པའི་རྣམ་ཤེས། །
མངོན་སུམ་ཡིན་ཞེས་བྱ་བ་འདིར། །
ཀུན་ལ་དོན་འདི་ཞེས་བརྗོད་ན། །
གང་དེ་དེ་འབའ་ཞིག་ལས་མིན། །

[Block 105]
གལ་ཏེ་ལ་དེ༌[^59]ཞེས་བྱ་བ་འདིས་རྐྱེན་ཀུན་བརྗོད་པ་ཡིན་ན་ནི་ཤེས་པ་གང་ཡུལ་གང་ལ་སྐྱེས་པ་དེའི་ཐ་སྙད་དུ་བྱའི། དེ་འབའ་ཞིག་ལས་ནི་མ་ཡིན་ནོ། །

[Block 106]
དམིགས་པའི་རྐྱེན་འབའ་ཞིག་ལས་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 107]
སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་གཞི༌[^60]ལས་སྐྱེ་བའོ༌[^61]ཞེས་གྲུབ་པའི་མཐའ་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 108 [VERSE]]
དམིགས་པའོ་ཞེ་ན་དྲན་སོགས་ཀྱི། །
ཤེས་པའང་གཞན་ལ་ལྟོས་མ་ཡིན། །

[Block 109]
གལ་ཏེ་དོན་དེ༌[^62]ལས་ཞེས་པ་འདིས་ཡུལ་ཙམ་ཡིན་ན་ནི་དྲན་པ་དང་། རྗེས་སུ་དཔག་པ་དང་མངོན་པར་འདོད་པ་ལ་སོགས་པའི་ཤེས་པ་ཡང་དམིགས་པར་བྱ་བ་གཞན་ལ་མི་ལྟོས་ཏེ། དུད་པ་ལ་སོགས་པ་དམིགས་ནས་མེ་ལ་སོགས་པའི་ཤེས་པ་སྐྱེ་བ་ནི་མ་ཡིན་ནོ། །

[Block 110]
གཟུགས་ལ་སོགས་པ་ཉིད་ལ་དམིགས་པ་ལ༌[^63]དོན་དུ་བརྗོད་པར་བྱ་གྲང་ན། ཅི་ཤེས་པ་སྐྱེ་བ་དེ་ལྟར་སྣང་བ་དེ་ལ་དེ་བཞིན་དུ་དམིགས་ནས་སྐྱེ་བ་ཡིན་ནམ། དེ་སྟེ་གཞན་དུ་སྣང་དུ་ཟིན་ཀྱང་ཇི་ལྟར་ཡོད་པའི་དེ་རྒྱུར་འགྱུར་བ་ཡིན་གྲང་། དེ་ལས་ཅིར་འགྱུར་ཞེ་ན། གལ་ཏེ་ཇི་ལྟ་བ་དེ་ལས་ཤེས་པ་སྐྱེ་ན་ནི་དེ་ལྟར་ན་བསགས་པ་ལ་དམིགས་པ་ཡིན་པའི་ཕྱིར་ལྔ་པོ་ཀུན་རྫོབ་པར་འགྱུར་ཏེ། དེ་ཉིད་ལ་དམིགས་པ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
