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
ཀཽ་ཤཱམྦཱི་དང་། སྐྱ་བོ་དང་། དམར་བ་དང་གང་ཟག་དང་ཀུན་ནས་གནས་པའི་གཞི་རྣམས་ནི་ཕྱིར་བཅོས་པའི་གཞི་ལ་སོགས་པའི་མིང་རྣམས་ཀྱིས་གསུངས་པ་ཡིན་ཏེ། མིང་གཞན་འཇུག་པའི་དགོངས་པ་ནི་རིམ་པ་དེ་ཉིད་ལས་བཤད་པར་བྱའོ། །

[Block 37]
ངེས་པར་འབྱེད་པ་ལ་སོགས་པ་ལ་རྗེས་སུ་ཉེ་བར་གནས་པ་རྣམས་ལ་ཡོངས་སུ་འདུལ་བར་བྱེད་པ་ནི་རིགས་པའི་ངོ་བོ་ཉིད་ཡིན་ཏེ། དེའི་རྗེས་ལ་ཡོངས་སུ་སྦྱོང་བའི༌[^26]གཞི་བསྟན་པ་ཡིན་ནོ། །

[Block 38]
གསོ་སྦྱོང་གཞག་པའི་གཞིའི་མིང་གཞན་འདི་འཆད་པར་འགྱུར་བའི་དོན་དུ་ཤེས་པ་རྣམས་ལ་འཇུག་པ་ཞེས་བྱ་བ་དེའི་རྗེས་སུ་ལས་བྱེ་བ༌[^27]དང་། འཁོར་ལོ་བྱེ་བའི་གཞི་དག་བསྟན་པ་ཡིན་ནོ། །

[Block 39]
ཐ་སྙད་ལ་བསྟེན་པའི༌[^28]ཆོ་ག་འདིའི་རྗེས་སུ་རིགས་པ་ཡིན་ཞེས་བྱ་བ་འདིའི་དོན་ལ་རྩོད་པའི་གཞི་བསྟན་པ་ཡིན་ནོ། །

[Block 40]
གནས་གང་དུ་འདི་ཐམས་ཅད་དང་དགེ་བའི་ཕྱོགས་གཞན་རྗེས་སུ་སྒྲུབ་པར་བྱེད་པ་དེ་ལ་བརྟེན་པའི་ཆོ་ག་འདི་ལས་རིགས་པ་ཡིན་ཏེ། དེའི་རྗེས་ལ་གནས་མལ་གྱི་གཞི་བསྟན་པ་ཡིན་ནོ། །

[Block 41]
ཕྲན་ཚེགས་ལ་སོགས་པ་རྣམས་ཀྱང་འདི་རྣམས་ཀྱིས༌[^29]རབ་ཏུ་དབྱེ་བར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་འདི་རྣམས་ལས་ལྷག་པ་ཉིད་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་སོ་སོར་མདོར་བྱས་པ་མ་ཡིན་ནོ། །

[Block 42]
གང་དུ་གང་གི་སྦྱོར་བ་ནི་དེ་ཉིད་ལས་ངེས་པར་བསྡུས་པ་ཡིན་ནོ། །

[Block 43]
མཁན་པོ་དང་སློབ་དཔོན་དག་གིས་རྗེས་སུ་གནང་བས་མཐར་ཕྱིན་པ་ནི་རབ་ཏུ་བྱུང་བ་དང་། བསྙེན་པར་རྫོགས་པའི་ཆོ་ག་སྟེ། དེ་ཉེ་བར་བསྟན་པའི་དོན་དུ། དགེ་འདུན་ཐམས་ཅད་འདུས་པ་ནི་ཆ་ལུགས་འདི་བཞིན་དུ་བྱས། རྒན་རིམས་ལ་ཕྱག་འཚལ་ནས། ཐལ་མོ་སྦྱར་ཙོག་ཙོག་པོར་འདུག་ཅིང་གསོལ་བ་བཏབ་པར་གྱུར་པ་གསུམ་དང་། གསོལ་བ་དང་བཞིའི་ལས་ཀྱིས་ཅིག་ཅར་རབ་ཏུ་བྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་ཉེ་བར་བསྒྲུབས་པར་གྱུར་པ་ལྟ་བུ་ནི། སྔོན་གྱི་ཆོ་གའོ་ཞེས་བྱ་བ་གསུངས་ཏེ། འཁོར་དུ་དགེ་འདུན་གྱི་ཕྱོགས་གཅིག་བསྡུས་པ་དགག་པའི་དོན་དུ་ཐམས་ཅད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 44]
འཁོར་དུ་གནས་པ་ཡང་དགེ་འདུན་གྱི་ཕྱོགས་གཅིག་ལ་ནི་མ་ཡིན་ཏེ། འོན་ཀྱང་དེའི་ནང་དུ་མཚམས་ན་གནས་པ་ཐམས་ཅད་དོ། །

[Block 45]
འདིས་ཆ་ལུགས་འདི་བཞིན་བྱས་པ་ནི་ཆ་ལུགས་འདི་བཞིན་དུ་བྱས་པའོ། །

[Block 46]
འདི་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་བསྟན་པ་ལ་དགེ་སློང་གི་ཆ་ལུགས་འདི་བཞིན་ཏེ་སྐྲ་དང་ཁ་སྤུ་བྲེགས་པའི་དགེ་སློང་གི་ཆ་ལུགས་ཀྱིས༌[^30]ཆོས་གོས་གསུམ་གྱོན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 47]
ཕྱག་འཚལ་ནས་ཞེས་བྱ་བ་ནི་རྒན་རིམས་ལ་ཞེས་བྱའོ། །

[Block 48]
ཇི་སྐད་དུ་འཆད་པར་འགྱུར་བ་སྟེ། དེ་ལ་འདིར་མངོན་པར་འབྲེལ་པ་ནི་རྒན་རིམས་ལ་ཕྱག་འཚལ་ནས་ཡན་ལག་ལྔས་ཕྱག་བྱས་ཏེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 49]
ཐལ་མོ་སྦྱར་བ་ཞེས་བྱ་བ་ནི་ཐལ་མོ་སྦྱར་བའོ། །

[Block 50]
ཙོག་ཙོག་པོར་འདུག་ཅིང་ཞེས་བྱ་བ་ནི་ཙོག་ཙོག་པོ༌[^31]ཉིད་ཀྱིས་གནས་པ་སྟེ། སྟན་ལ་ཉེ་བར་འདུག་པས་ནི་མ་ཡིན་ནོ། །གང་དུ་གནས་ཤེ་ན། རྒན་རིམས་ལ་ཞེས་བྱ་བའོ། །

[Block 51]
འོ་ན་རྒན་རིམས་ལ་ཙོག་ཙོག་པོ་ཉིད་ཀྱིས་འདུག་ལ། ཐལ་མོ་སྦྱར་བ་ཉིད་ཅེས་བྱ་བ་འདིས་ནི་དགེ་འདུན་ལ་རག་ལས་པའི་ལས་ལ་ངེས་པ་ཡིན་ཏེ། ལས་ཐམས་ཅད་ལ་དབང་དུ་བྱེད་པའི་མདོར་བྱས་པ་སྟེ།

[Block 52]
དེ་ཉིད་ཀྱི་ཕྱིར་འདིར༌[^32]ཡང་ལས་ཉིད་ཀྱི་ཕྱིར་གསུམ་པོ་འདིས་ཐོབ་པར་གྱུར་པ་ལ་ཅིའི་ཕྱིར་སླར་ཚིག་ད༌[^33]ལྟར་བྱུང་བའི་ཆོ་ག་དབང་དུ་བྱེད་པ་ཉིད་ཀྱིས་ཐལ་མོ་སྦྱར་ཞེས་པ་ལ་སོགས་པ་ངེས་པ་ལས།

[Block 53]
འདིར་འདི་ལ་བསྒྲུབས་པར༌[^34]གྱུར་པ་ལྟ་བུ་ནི་སྔོན་གྱི་ཆོ་ག་ཞེས་བྱ་བའི་ཚིག་ཡོད་པ་མ༌[^35]ཡིན་ནོ། །

[Block 54]
གསོལ་བ་བཏབ་པར་གྱུར་པ་ཞེས་པ་ནི་ཅི་ཞིག་ཅེ་ན།

[Block 55 [VERSE]]
རབ་ཏུ་འབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་དག་གོ། །
སླར་གསོལ་བ་བཏབ་པ་ནི་བཙུན་པ་རྣམས་གསོན་ཅིག །

[Block 56]
དགེ་འདུན་གྱིས༌[^36]བདག་མིང་འདི་ཞེས་བགྱི་བ། ལེགས་པར་གསུངས་པའི་ཆོས་འདུལ་བ་ལ་རབ་ཏུ་འབྱུང་བ་ཉིད་དང་། བསྙེན་པར་རྫོགས་པ་དགེ་སློང་གི་དངོས་པོ་བདག་འདོད་ཅེས་བྱ་བ་ནི་རྒྱ་ཆེར་བཤད་པའོ། །

[Block 57]
སྔགས་འདིས་ལན་གསུམ་གྱི་བར་དུ་གསོལ་བ་བཏབ་པའོ། །

[Block 58]
གསོལ་བ་དང་བཞིའི་ལས་ཀྱིས་ཞེས་བྱ་བ་ནི་ལན་གསུམ་དུ་བརྗོད་པས་གསོལ་བ་དང་བཞིའི་ལས་གང་ཞིག་ལ་ཡོད་པ་དེ་ནི་གསོལ་བ་དང་བཞིའི་ལས་དེ་ཉིད་ཀྱིས་སོ། །

[Block 59]
ཅིག་ཅར་རབ་ཏུ་འབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་དག་ཅེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བ་ཉིད་དང་བསྙེན་པར་རྫོགས་པ་དུས་མཉམ་དུ་ཡིན་གྱི༌[^37]རིམ་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 60]
ཉེ་བར་བསྒྲུབས་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་དུ་གྱུར་པའི་དགེ་སློང་རྣམས་སོ། །

[Block 61]
དེ་ལྟར་ན་ཡང་སྔགས་ནི་དགེ་འདུན་བཙུན་པ་རྣམས་གསན་དུ་གསོལ། བདག་མིང་འདི་ཞེས་བགྱི་བ་ལེགས་པར་གསུངས་པའི་ཆོས་འདུལ་བ་ལ་རབ་ཏུ་འབྱུང་བ་ཉིད་དང་བསྙེན་པར་རྫོགས་པ་དགེ་སློང་གི་དངོས་པོར་འདོད་ཅིང་གསོལ་ན། བདག་མིང་འདི་ཞེས་བགྱི་བ་དགེ་འདུན་གྱིས་རབ་ཏུ་འབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་མཛད་དོ་ཞེས་བྱ་བའོ། །

[Block 62]
ལྟ་བུ་ནི་སྔོན་གྱི་ཆོ་གས་ཏེ། ལྟ་བུའི་སྒྲ་ནི་རབ་ཏུ་དབྱེ་བ་རྗོད་པར༌[^38]བྱེད་པའོ། །

[Block 63]
སྔོན་གྱི་ཆོ་ག་ཞེས་བྱ་བ་ནི་ད་ལྟར་བྱུང་བའི་ཆོ་ག་ལས་སྔ་རོལ་དུ་འདི་ལྟ་བུའི་རབ་ཏུ་དབྱེ་བ་ཅན་རབ་ཏུ་བྱུང་བ་ཉིད་དང་བསྙེན་པར་རྫོགས་པའི་ཆོ་ག་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 64]
ཅི་འོ་ན་ད་ལྟར་བྱུང་བའི་ཆོ་ག་ཉིད་བཅོམ་ལྡན་འདས་ཀྱིས་སྔོན་རོལ༌[^39]དུ་ཅིའི་ཕྱིར་མ་གསུངས།

[Block 65]
ཡང་ན་སྔོན་གྱི་ཆོ་ག་འདི་སླར་ཅིའི་ཕྱིར་མ་གསུངས་ཤེ་ན་གང་ག་ཕྱིར་དེའི་ཚེ་ན་རྣམ་པར་དག་པའི་སེམས་ཅན་རྣམས་ནི་རྟོགས་པ་པོ་ཡིན་ཏེ། དེ་རྣམས་ལ་རིམ་གྱིས་རྣམ་པར་ངེས་པ་ཉིད་མ་ཡིན་ཏེ། གཞན་དག་ལ་བརྟེན་ནས་མ་ཡིན་པ་དང་། ཡོངས་སུ་སློབ་པར་བྱེད་པས་སམ། འདི་རྣམས་ནི་དམན་པ་མ་ཡིན་ཏེ། བསོད་ནམས་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་མི་ལེགས་པ་སྒྲུབ་པ་མ་ཡིན་ཏེ། འོན་ཏེ་སྒྲུབ་པ་ལ་རང་ཉིད་ཀྱིས་འདི་རྣམས་ལ་རྩེ་བར༌[^40]བྱེད་པ་རྣམས་ཡོད་པ་ཡིན་ཏེ། བར་དུ་གཅོད་པར་བྱེད་པའི་ཆོས་རྣམས་ལ་ནི་དེའི་ཚེ་ན་ལྟུང་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 66]
དེ་བཞིན་དུ་གསལ་བར་བྱེད་པ་རྣམས་ལ་ལྟུང་བ་མེད་པའི་ཕྱིར་ཞེས་བྱ་བ་སྟེ། དེ་བས་ན་སྔོན་གྱི་ཆོ་ག་བརྗོད་པའོ། །

[Block 67]
གང་གི་ཚེ་རྣམ་པ་གཞན་དུ་ཡང་འདི་རྣམས་འབྱུང་བ་དེའི་ཚེ་ཕྱི་མ་ཐམས་ཅད་ལ་ཉེ་བར་མི་མཁོ་བ་འགའ་ཡང་མ་ཡིན་ཏེ། དེ་བས་ན་འདིར་ཉེ་བར་བརྟགས་པ་འདིས་ཅི་ཞིག་བྱའོ། །

[Block 68]
གལ་ཏེ་ཆོ་ག་འདིས་ད་ལྟར་ཐ་སྙད་མ་ཡིན་ཏེ། དེ་ལྟར་ན་ཡང་འདི་ལ་ཕྱི་མ་ལས་གཞན་ཉིད་ནི༌[^41]ཡོད་པ་མ་ཡིན་ཏེ། གང་ཞིག་ཕྱི་མ་ལས་ཁྱད་པར་དེ་ནི་འདིའི་ཆ་ལག་ཙམ་ཡིན་ནོ། །

[Block 69]
དེ་ལ་འདི་ནི་སྔགས་དང་རྒྱུད་ཡིན་ཏེ། འདི་ཙམ་ཉིད་དེའི་ཚེ་ཡོད་པར་འགྱུར་ཏེ། འདུལ་བའི་དབང་གིས་གཞན་འདིར་འདིའི་ཆོ་ག་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བའི་དོན་ནི་བསྒྲགས་པའི་དོན་དུ་ཉེ་བར་བཏགས་པའོ། །

[Block 70]
དེ་ལྟར་ན་དགོས་པ་དང་བཅས་པ་ནི་སྔོན་གྱི་ཆོ་ག་ཉེ་བར་བསྟན་པའོ། །

[Block 71]
[^42]

[Block 72]
དེ་ནི་ད་ལྟར་བྱུང་བའི་ཆོ་ག་བརྗོད་པར་བྱ་སྟེ། རབ་ཏུ་འབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་དེའི་ཕྱིར་དགེ་སློང་འགའ་ཞིག་ལ་མཁན་པོ་ཉིད་དུ་གནས་པ་ལའོ་ཞེས་བྱ་བ་སྟེ། དགེ་སློང་འགའ་ཞིག་ལ་ཞེས་བྱ་བ་ནི་གདོན་མི་ཟ་བར་འགའ་ཞིག་ལ་བརྟེན་ནས་རབ་ཏུ་འབྱུང་བ་ཉིད་དེ་ལ༌[^43]བསྙེན་པར་རྫོགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་རབ་ཏུ་བསྟན་པའི་དོན་དུ་འགའ་ཞིག་ཅེས་བྱ་བའི་ཚིག་གོ། །ཇི་ལྟར་བརྟེན་ནས་ཤེ༌[^44]ན། སྨྲས་པ། མཁན་པོ་ཉིད་དུའོ། །ཅིའི་དོན་དུ་བརྟེན་པ་ལ་ཞེས་བྱ་ཞེ་ན། སྨྲས་པ། དེའི་ཕྱིར་ཞེས་བྱ་བ་སྟེ། རབ་ཏུ་འབྱུང་བ༌[^45]ཉིད་དང་བསྙེན་པར་རྫོགས་པ་ལ་ལྟོས་པ༌[^46]ལའོ། །

[Block 73]
འདིའི་རྒྱུ་མཚན་གྱི་བདུན་པ་སྟེ། འདི་རྣམས་ལ་རབ་ཏུ་འབྱུང་བ༌[^47]ཉིད་དང་བསྙེན་པར་རྫོགས་པའི་རྒྱུ་མཚན་གྱིས༌[^48]མཁན་པོ་ཉིད་ཀྱིས་དགེ་སློང་འགའ་ཞིག་ལ་བརྟེན་པ་ལས༌[^49]རབ་ཏུ་འབྱུང་བ༌[^50]ཉིད་དང་བསྙེན་པར་རྫོགས་པ་དག་ཏུ༌[^51]འགྱུར་གྱི། ཇི་ལྟར་སྔོན་གྱི་ཆོ་ག་ལྟར་འགའ་ཞིག་ལ་མ་བརྟེན་པ་ཉིད་ཀྱིས་ནི་མ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 74]
འདིར༌[^52]སླར་རབ་ཏུ་བྱུང་བ་ཉིད་ནི་གང་ཞིག་དེ་ལ་འོས་པའི་ཚུལ་ཁྲིམས་དགེ་ཚུལ་གྱི༌[^53]སྡོམ་པ་དེས་རྗེས་སུ་ཆགས་པར་རིག་པར་བྱའོ། །

[Block 75]
རབ་ཏུ་འབྱུང་བ༌[^54]ཉིད་དང་དགེ་ཚུལ་གྱི་སྡོམ་པ་དག་གཉིས་པོ་འདི་ཡང་བརྟེན་པ་ལའོ། །
--- END BLOCKS ---
