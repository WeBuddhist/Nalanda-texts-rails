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
མི་བརྒྱན་པ་ནི་རྒྱན༌[^41]ནར་མ་མ༌[^42]གཏོགས་ཏེ་རྒྱན་ནར་མ་ནི་མཚར་གཅིག་རྒྱགས་པར་མི་བྱེད་དོ། །

[Block 72]
ནམ་ནངས་ཀྱི་བར་དུ་མནོད་པར་བྱ་བ་ནི་ཉི་མ་ཤར་གྱི་བར་དུའོ། །

[Block 73]
ཡན་ལག་བརྒྱད་ཚང་བར་མནོད་པར༌[^43]བྱ་བའི༌[^44]ཡན་ལག་མ་ཚང་བར་ནི་མ་ཡིན་ནོ། །

[Block 74]
ནང་པར་ནི་རེ་ཞིག་ཉི་མ་ཤར་བའི་ཚེ་སྟེ། ཉིན་ཞག་པའི་སྡོམ་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 75]
གང་གིས་ཚེས་བརྒྱད་ལ་རྟག་ཏུ་བསྙེན་གནས་ལ་གནས་པར་བྱའོ་ཞེས་སྔོན་ཡང་དག་པར་བླང་བར་བྱས་པ་དེ༌[^45]ནི་ཟས་ཟོས་ནས་ཀྱང་མནོད་པར༌[^46]བྱའོ། །

[Block 76]
གཞན་ལས་མནོད་པར༌[^47]བྱའི་བདག་ཉིད་ལས་ནི་མ་ཡིན་ཏེ། གཞན་ལ་ལྟོས་པས་ནི་རྐྱེན་ཡོད་ཀྱང་མི་འདའ་བར་བྱ་བའི་ཕྱིར་དང་།[^48] དེ་ལས་གཞན་དུ་མནོས་པ་ནི་ལེགས་པར་སྤྱད་པ་ཙམ་དུ་འགྱུར་གྱི་བསྙེན་གནས་ཀྱི་སྡོམ་པ་ནི་མ་ཡིན་ནོ། །

[Block 77]
དེ་ལྟར་བྱས་ན་ཤན་པ་དང་བྱི་བོ་བྱེད་པ་དག་གིས༌[^49]མཚན་མོ་དང་ཉིན་མོའི་བསྙེན་གནས་དག་ཀྱང་འབྲས་བུ་ཡོད་པར་རུང་ངོ་། །འདིས་དགྲ་བཅོམ་པ་དག་དང་ཉེ་བར་གནས་པར་བྱེད་པས་ན་བསྙེན་གནས་ཏེ། དེ་དག་གི་རྗེས་སུ་སློབ་པའི་ཕྱིར་རོ། །

[Block 78]
གཞན་དག་ན་རེ་འདིས་ཇི༌[^50]སྲིད་འཚོའི་བར་གྱི་སྡོམ་པ་དང་ཉེ་བར་གནས་པར་བྱེད་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 79]
ཡང་ན་དགེ་བའི་རྩ་བ་ཆུང་ངུ་རྣམས་ཀྱི་དགེ་བའི་རྩ་བ་གསོས་འདེབས་པའི་ཕྱིར་ཏེ།

[Block 80 [VERSE]]
གང༌[^51]ཕྱིར་ཡིད་ཀྱི་དགེ་བ་གསོས་འདེབས་དེ་ཡི༌[^52]ཕྱིར། །
འདི་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་གསོ་སྦྱོང་བཤད་ཅེས་གྲག །

[Block 81]
ཞེས༌[^53]འབྱུང་བས་ན་གསོ་སྦྱོང་ཡིན་ནོ། །

[Block 82 [HEADING]]
### བསྙེན་གནས་ཀྱི་ཡན་ལག་བརྒྱད། ^1-8-0

[Block 83]
ཅིའི་ཕྱིར་ཡན་ལག་བརྒྱད་ནོད་ཅེ་ན།

[Block 84 [VERSE]]
ཚུལ་ཁྲིམས་ཡན་ལག་བག་ཡོད་པའི། །
ཡན་ལག་བརྟུལ་ཞུགས་ཡན་ལག་སྟེ། །
བཞི་གཅིག་དེ་བཞིན་གསུམ་རིམ་བཞིན། །

[Block 85]
རེ་ཞིག་བརྫུན་དུ་སྨྲ་བ་སྤོང་བའི་བར་བཞི་ནི་རང་བཞིན་གྱི་ཁ་ན་མ་ཐོ་བ་སྤོང་བའི་ཕྱིར༌[^54]ཚུལ་ཁྲིམས་ཀྱི་ཡན་ལག་ཡིན་ནོ། །

[Block 86]
མྱོས་པར་འགྱུར་བའི་བཏུང་བ་སྤོང་བ་གཅིག་པུ་ནི་བག་ཡོད་པའི་ཡན་ལག་སྟེ་མྱོས་པར་འགྱུར་བ་འཐུང་བ༌[^55]ནི་ཚུལ་ཁྲིམས་རྫོགས་ཀྱང་བག་མེད་པར་འགྱུར་རོ། །

[Block 87]
དུས་མ་ཡིན་པའི་ཟས་སྤོང་བའི་བར་གསུམ་ནི་སྐྱེ་བོའི༌[^56]རྗེས་སུ་མཐུན་པའི་ཕྱིར་བརྟུལ་ཞུགས་ཀྱི་ཡན་ལག་ཡིན་ནོ། །

[Block 88]
ཅི་བག་ཡོད་པའི་ཡན་ལག་དང་། བརྟུལ་ཞུགས་ཀྱི་ཡན་ལག་འདི་དག་མ་མནོས་པས་ཅིར་འགྱུར་ཞེ་ན། དེ་ཡིས་དྲན་ཉམས༌[^57]དྲེགས་པར་འགྱུར། །མྱོས་པར་འགྱུར་བ་འཐུངས་པས་ནི་བྱ་བ་དང་བྱ་བ་མ་ཡིན་པའི་དྲན་པ་ཉམས་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 89]
ཁྲི་སྟན་མཐོན་པོ་དང་ཁྲི་སྟན་ཆེན་པོ་དང་། གར་དང་གླུ་ལ་སོགས་པ་བསྟེན་པས་ནི་དྲེགས་པར་འགྱུར་ལ། དྲེགས་པར་གྱུར་པ་ལ་ནི་འཆལ་པའི་ཚུལ་ཁྲིམས་ཐག་མི་རིང་བར་འགྱུར་རོ། །

[Block 90]
དུས་སུ་ཟ་ཞིང་ཟས་ནར་མའི་དུས་སུ་ཡོངས་སུ་སྤངས་པ་ལས་ནི་བསྙེན་གནས་ཀྱི་དྲན་པ་དང་། སྐྱོ་བའི་དྲན་པ་ཉེ་བར་གནས་པར་འགྱུར་ཏེ། དེ་མེད་ན་གཉི་ག་ཡང་མེད་དོ། །

[Block 91]
ཡང་ཁ་ཅིག་ནི་དུས་མ་ཡིན་པའི་ཟས་སྤོང་བ་ཁོ་ན་འདིར་བསྙེན་གནས་ཡིན་ལ། ལྷག་མ་རྣམས་ནི་འདིའི་ཡན་ལག་ཡིན་ཏེ་གར་དང་གླུ་དང་རོལ་མོ་དང་། སྤོས་དང་མེ་ཏོག་ཕྲེང་དང་བྱུག་པ་ནི༌[^58]འདིར་གཉིས་སུ་བྱའོ་སྙམ་དུ་སེམས་སོ། །

[Block 92]
དེ་ལྟར༌[^59]ཡིན་ན་ནི་དུས་མ་ཡིན་པའི་ཟས་སྤོང་བ་བཀའ་སྩལ་ནས་ཡན་ལག་བརྒྱད་པ་འདིས་འཕགས་པ་དགྲ་བཅོམ་པ་དེ་དག་གི་བསླབ་པ་ལ་རྗེས་སུ་སློབ་བོ། །

[Block 93]
རྗེས་སུ་བགྱིད་དོ་ཞེས་གསུངས་པའི་མདོའི་ཚིག་མི་རུང་བར་འགྱུར་རོ། །

[Block 94]
འོ་ན་ཡན་ལག་བརྒྱད་པོ་འདི་དག་གང་གི་ཡིན་པའི་བསྙེན་གནས་གཞན་དེ་གང་ཞིག་ཡིན་བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་འདུས་པའི་ཡན་ལག་རྣམས་ནི་ཡན་ལག་ཡིན་ཏེ། ཤིང་རྟའི་ཡན་ལག་དང་དཔུང་གི་ཚོགས་ཡན་ལག་བཞི་པ་དང་། ཕྱེ་མ་ཡན་ལག་ལྔ་པ་ཇི་ལྟ་བུར༌[^60]བསྙེན་གནས་ཡན་ལག་བརྒྱད་པ་ཡང་དེ་དང་འདྲ་བར་བལྟ་བར་བྱའོ། །

[Block 95]
དུས་མ་ཡིན་པའི་ཟས་སྤོང་བ་ནི་བསྙེན་གནས་ཀྱང་ཡིན་ལ། བསྙེན་གནས༌[^61]ཀྱི་ཡན་ལག་ཀྱང་ཡིན་ཏེ། དཔེར་ན་ཡང་དག་པའི་ལྟ་བ་ལམ་ཡང་ཡིན་ལ་ལམ་གྱི་ཡན་ལག་ཀྱང་ཡིན་པ་དང་། ཆོས་རྣམ་པར་འབྱེད་པ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་བྱང་ཆུབ༌[^62]ཀྱང་ཡིན་ལ་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཀྱང་ཡིན་པ་དང་། ཏིང་ངེ་འཛིན་བསམ་གཏན་ཀྱང་ཡིན་ལ་བསམ་གཏན་གྱི་ཡན་ལག་ཀྱང་ཡིན་པ་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 96]
དེ་དག་ཉིད་ཡང་དག་པའི་ལྟ་བ་ལ་སོགས་པ་དེ་དག་ཉིད་ཀྱི་ཡན་ལག་ཉིད་དུ་རུང་བ་ནི་མ་ཡིན་ནོ། །

[Block 97]
གལ་ཏེ་ཡང་དག་པའི་ལྟ་བ་ལ་སོགས་པ་སྔ་མ་རྣམས་ཕྱི་མ་རྣམས་ཀྱི་ཡན་ལག་ཏུ་འགྱུར་ན་ནི་སྐད་ཅིག་མ་དང་པོ་ལ༌[^63]སྐྱེས་པའི་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པར་མི་འགྱུར་རོ། །

[Block 98 [HEADING]]
### གཞན་ལའང་བསྙེན་གནས་ཡོད་པ། ^1-9-0

[Block 99]
ཡང་ཅི་བསྙེན་གནས་འདི་དགེ་བསྙེན་ཁོ་ན་ལ་ཡོད་དམ། འོན་ཏེ་གཞན་ལ་ཡང་ཡོད་ཅེ་ན། གཞན་ལའང་བསྙེན་གནས་ཡོད་མོད་ཀྱི། སྐྱབས་སུ་མ་སོང་བ་ལ་མེད། །དགེ་བསྙེན་མ་ཡིན་པ་ལ་ཡང་གང་ཞིག་ཉིན་ཞག་དེ་ལ་སངས་རྒྱས་དང་ཆོས་དང་དགེ་འདུན་ལ་སྐྱབས་སུ་སོང་སྟེ། བསྙེན་གནས་ནོད་པ་དེ་ལ་བསྙེན་གནས་ཀྱི་སྡོམ་པ་སྐྱེ་བར༌[^64]འགྱུར་ཏེ། གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 100]
མི་ཤེས་པ་ནི་མ་གཏོགས་སོ། །

[Block 101 [HEADING]]
### སྐྱབས་སུ་འགྲོ་བ་ཁོ་ནས་དགེ་བསྙེན་དུ་འགྱུར་བ། ^1-10-0

[Block 102]
མདོ་ལས།

[Block 103]
མིང་ཆེན༌[^65]འདི་ལྟར་ཁྱིམ་པ་གོས་དཀར་པོ་བགོས་པ༌[^66]སྐྱེས་པ་ཕོའི་དབང་པོ་དང་ལྡན་པ་ཞིག་སངས་རྒྱས་ལ་སྐྱབས་སུ་འགྲོ་ཆོས་དང་དགེ་འདུན་ལ་སྐྱབས་སུ་འགྲོ་ཞིང་། བདག་ལ་དགེ་བསྙེན་དུ་གཟུང་དུ་གསོལ་ཞེས་ཚིག་ཏུ་ཡང་སྨྲ་ན་འདི་ཙམ་གྱིས་དགེ་བསྙེན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་དེ་ཅི་སྐྱབས་སུ་འགྲོ་བ་ཁོ་ནས་དགེ་བསྙེན་དུ་འགྱུར་རམ་ཞེ་ན། ཉི་འོག་པ་རྣམས་ན་རེ་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 104]
ཁ་ཆེ་བ་རྣམས་ན་རེ༌[^67]སྡོམ་པ་མེད་པར་མི་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 105]
འོ་ན་གང་མདོ་ལས་གསུངས་པ་ཇི་ལྟ་བུ་ཞེ་ན། འདི་ལ་འགལ་བ་མེད་དེ། འདི་ལྟར་དགེ་བསྙེན་ཉིད་དུ་ཁས་བླངས་པ་དེ༌[^68]ཁོ་ན་འདིའི་སྡོམ་པ་སྐྱེ་བར་འགྱུར་ཏེ། གང་གི་ཚེ་བདག་ལ་དགེ་བསྙེན་དུ་གཟུང་དུ་གསོལ། དེང་སླན་ཆད་ནམ་ཇི་སྲིད༌[^69]འཚོའི་བར་དུ་སྲོག་གཅོད་པ་སྤོང་ངོ་ཞེས་དགེ་བསྙེན་དུ་ཁས་བླངས་པ་ཁོ་ནས་འདིའི་དགེ་བསྙེན་གྱི་སྡོམ་པ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 106]
སྲོག་གཅོད་པ་སྤོང་བ༌[^70]ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། བར་གྱི་ཚིག་མི་མངོན་པར་བྱས་པའི་ཕྱིར་རོ། །

[Block 107]
སྡོམ་པ་ཐོབ་ཀྱང་བསླབ་པའི་གཞི་རྣམས་ཤེས་པར་བྱ་བའི་ཕྱིར་བསྟན་པ་དགེ་སློང་བཞིན། །ཇི་ལྟར་དགེ་སློང་དང་དགེ་སྦྱོང་གི་སྡོམ་པ་ཐོབ་ཟིན་ཀྱང་ཤེས་པར་བྱ་བའི་ཕྱིར་ཁྱོད་ཀྱི༌[^71]འདི་དང་འདི་ལྟར་དུ༌[^72]བསྡམ་མོ་ཞེས་བསླབ་པའི་གཞི་རྣམས་ཡང་འཛིན་དུ་འཇུག་པ་ལྟར་དགེ་བསྙེན་ཡང་དེ་དང་འདྲ་བས་སྡོམ་པ་མེད་པའི་དགེ་བསྙེན་ནི་མེད་དོ། །

[Block 108 [HEADING]]
### སྣ་གཅིག་སྤྱོད་པ་ལ་སོགས་པའི་དགེ་བསྙེན། ^1-11-0

[Block 109 [VERSE]]
གལ་ཏེ་ཐམས་ཅད་སྡོམ༌[^73]ཡིན་ན། །
སྣ་གཅིག་སྤྱོད་སོགས་ཇི་ལྟ་བུ། །

[Block 110]
གལ་ཏེ་དགེ་བསྙེན་ཐམས་ཅད་དགེ་བསྙེན་གྱི་སྡོམ་པ་ལ་གནས་པ་ཡིན་ན་བཅོམ་ལྡན་འདས་ཀྱིས་སྣ་གཅིག་སྤྱོད་པ་དང་། ཕྱོགས་གཅིག་སྤྱོད་པ་དང་། ཕལ་ཆེར་སྤྱོད་པ་དང་། ཡོངས་སུ་རྫོགས་པར་སྤྱོད་པའི་དགེ་བསྙེན་ཞེས་གསུངས་པ་ཇི་ལྟ་བུ་ཡིན། དེ་བསྲུང་བ་ལ་གསུངས་ཞེས་གྲགས། །གང་ཞིག་བསླབ་པའི་གཞི་གང་སྲུང་བར༌[^74]བྱེད་པ་ནི་དེ་སྤྱོད་པ་ཞེས་གསུངས་པར་ཟད་ཀྱི་ཐམས་ཅད་ཀྱང་སྡོམ་པ་ལ་གནས་པར་ནི་འདྲའོ། །
--- END BLOCKS ---
