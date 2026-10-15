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
གནས་སྐབས་གང་ལ་ཇི་ལྟ་བུའི་ཁ་ན་མ་ཐོ་བ་ལ་བྱེད་པ་པོ་རྣམས་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མཐར་ཐུག་ན་དངོས་གཞིའོ། །

[Block 37]
སྦྱོར་བ་ལ་ནི་ཉེས་བྱས་ཀྱིའོ། །

[Block 38]
རེ་ཞིག་གི་དུས་སུ་གཞན་འདུག་པའི་བར་དུ་ཡང་དེའིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའོ་ཞེས་བྱ་བ་ནི་ཉེས་བྱས་སོ། །

[Block 39]
འདིར་མཐར་ཐུག་ན་སྟེ་སྦྱོར་བ༌[^31]ནི་མ་ཡིན་ནོ། །

[Block 40]
རེ་ཞིག་གི་དུས་སུ་གཞན་འདུག་པའི༌[^32]དུས་ཡུན་ཅུང་ཟད་ཅིག་གོ། །

[Block 41]
འདུག་པའི་ཞེས་བྱ་བ་ནི་གནས་དེར་འདུག་པའི་སྟེ་མཐར་ཐུག་པ་ཡང་ཉེས་བྱས་འདི་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 42]
འདིར་གཞུང་ནི་ཞུ་བའི་ཡི་གེ་ཁ་ཅིག་ལས་འཆག་པའི་གནས་མལ་མནོས་པ་ལ་དགེ་སློང་རྣམས་ཀྱིས་དུས་ཅུང་ཟད་ཅིག་བླངས་ན་དགེ་འདུན་གྱིས་བཏིང་བ་དེ་ཡང་མི་སྡུད་དམ་སྡུད་དུ་མི་འཇུག་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 43]
གང་ཟག་གི་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་འདིར་ཉེས་བྱས་སོ། །

[Block 44]
འདིར་གཞུང་ནི་ཞུ་བ་དག་ལས་གང་ཟག་གི་གནས་མལ་ཡིན་ལ། དེ་དགེ་སློང་གིས་གདིང་དུ་བཅུག་ནས་དགེ་སློང་འདུག་པ་ལ་མ་བཅོལ་བར་དེ་ནས་འགྲོ་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 45]
འོག་མ་བཞི་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གདིང་བ་དང་སྐྲོད་པ་དང་ཕྱིས་གནོན་པ་དང་རྩ་བ་འབྱུང་བ་ལ་འདུག་པ་ཞེས་བྱ་བ་དག་ལ་ཡང་གང་ཟག་གི་གནས་སུ་ནི་ཉེས་བྱས་སོ། །

[Block 46]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་གང་ཟག་གི་གཙུག་ལག་ཁང་དུ་འདིང༌[^33]ན་ཉེས་བྱས་སོ། །

[Block 47]
གང་ཟག་གནས་མལ་ནས་སྐྲོད་ན་ཉེས་བྱས་སོ། །

[Block 48]
གང་ཟག་གི༌[^34]གཙུག་ལག་ཁང་གི་ཡིན་ལ་དེར་དགེ་སློང་གིས༌[^35]ཕྱིས་གནོན་བྱས་ཏེ་གནས་མལ་བཅས་ན་ཉེས་བྱས་སོ། །

[Block 49]
གང་ཟག་གི༌[^36]གཙུག་ལག་ཁང་གི་སྟེང་གི་ནམ་མཁའ་ལ་ཡང་ཐོག་བྱས་པར་ལྗིད་ཀྱིས་ཕབ་སྟེ་འདུག་གམ་ཉལ་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 50]
རེག་པར་བྱ་བ་ཉིད་མ་ཡིན་པ་ཉིད་ལ་ནི་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་གསེར་ལ་སོགས་པའི་རང་བཞིན་ཉིད་རེག་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་ནི་ཉེས་བྱས་སུ་ཡང་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 51]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་དགེ་སློང་འགའ་ཞིག་གིས་ཁྲིའམ་ཁྲིའུ་འམ་བླ་གབ༌[^37]མ་མཆིས་པར་བཞག་སྟེ། མ་བསྡུས་སམ་སྡུད་དུ་མ་བཅུག་པར་དེ་ནས་གཞན་དུ་མཆི༌[^38]ན་ལྟུང་བ་མི་འབྱུང་བ་འགའ་མཆིས་སམ། བཀའ་སྩལ་པ་ཡོད་དེ་རིན་པོ་ཆེ་ལས་བྱས་པ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 52]
འདིར་རེག་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་རིན་པོ་ཆེ་བཟུང་བ་ལ་གཙོ་བོ་སྟེ། དེ་བས་ན་འདིར་གཞན་དུ་ཉེ་བར་བཏགས་པ་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 53]
བསྡུ་བར༌[^39]བྱ་བ་བཏིང་སྟེ་བསོད་སྙོམས་ལ་ཞུགས་པ་ན། གལ་ཏེ་རླུང་དང་ཆར་པ་འོང་ན་གཙུག་ལག་ཁང་ན་འཁོད་པ་རྣམས་ཀྱིས་བསྡུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གུས་པར་བྱ་སྟེ་ཞུགས་པ་ཕྱིར་འོང་བར་བྱའོ། །

[Block 54]
བསྡུ་བར་བྱ་བ་བཏིང་སྟེ་གནས་མལ་དང་བསོད་སྙོམས་ལ་ཞུགས་པ་དང་རླུང་དང་ཆར་འབབ་པ་མཐོང་ན་གུས་པར་བྱ་སྟེ་མྱུར་དུ་ཕྱིར་འོང་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 55]
དེའི་དོན་ལ་ཉེས་པ་མེད་པ་དང་ན་སྨད་པ་མ་ཡིན་ན་ཞེས་བྱ་བ་ནི་བསོད་སྙོམས་ཀྱི་དོན་ཉིད༌[^40]དུ་ཞུགས་པ་དེ་ལ་གནས་མལ་དང་འབྲེལ་པའི༌[^41]ཡོངས་སུ་རྫོགས་པ་ཉིད་ནི་ཁ་ན་མ་ཐོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 56]
ན་སྨད་པ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་བསྡུ་བར་བྱ་བ་བཏིང་སྟེ་བསོད་སྙོམས་ལ་ཞུགས་པར་མི་བྱའོ། །

[Block 57]
འཇུག་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 58]
གང་གི་ཕྱིར་འགལ་ཚབས་ཅན་བཅས་པའི་ཚིག་ནི་ཇི་ལྟར་བརྗོད་པའི་སྐྱོན་ཡོད་པ་སྟོན་པར་བྱེད་པ་སྟེ། འདི་ན་སྨད་པའི་རྒྱུ་ཡང༌[^42]ཡོད་པ་མ་ཡིན་ཏེ་གང་གི་ཕྱིར་ན་སྨད་པར་འགྱུར། གལ་ཏེ་བརྗོད་པས་ལམ་རིང་དུ་འདས་སམ་ཕྱི་ནས་དྲན་པ་རྙེད་ན་ཕྱིན་ཆད་དེ་ལྟར་མི་བྱའོ་ཞེས་སེམས་བསྐྱེད་པར་བྱ་ཞིང་ཚིག་ཏུ་བརྗོད་པར་ཡང་བྱའོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་ལམ་རིང་པོར་མ་ཕྱིན་པར་སླར་དྲན་པ་རྙེད་ན་ནི་ཕྱིར༌[^43]ལོག་པར་བྱའོ་ཞེས་བྱ་བ་འདིར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 59]
གལ་ཏེ་དགེ་སློང་ལམ་ནས་ཚུར་འོང་བ་ཞིག་དང༌[^44]ཕྲད་པར་གྱུར་ན་བསྡུ་བའི་ཕྱིར་དེ་ལ་བཅོལ་བར་བྱའོ། །

[Block 60]
ཁས་བླངས་པས་སོན་པ་ཉིད་ན་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གནས་མལ་གྱི་གནས་སུ་སོན་པ་ཉིད་ལ་འདིར་ནི་གནས་མལ་ཡང་དག་པར་བསྒྲུབ་པ་ལ་སླར་བསྡུ་བར་བྱ་ཞེས་བྱ་བ་གང་ཞིག་གིས་ཁས་བླངས་པ་དེ་དེའི་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 61]
དེའི་ཞེས་བྱ་བ་འདི་ནི་ཤུགས་ཀྱིས་རྙེད་པར་བྱ་བ་སྟེ། དེ་བས་ན་མདོར་མ་བྱས་སོ། །

[Block 62]
འདིར་འདིའི༌[^45]གཞུང་ནི་གལ་ཏེ་དགེ་སློང་དེས་ཀྱང་དགེ་སློང་དེ་ལ་ཁས་བླངས་ནས་གནས་མལ་དེ་བསྡུ་བར་མི་བྱེད་ན་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 63]
ཚུར་འོང་བ་ཞིག་ལ་འདི་སྐད་སྨྲས་ཏེ། གཞན་དུ་ཡང་འདིའི་རྗེས་སུ་འབྲེངས་པས་འདི་ཤེས་པ་སྟེ། རིག་པ་ལ་ཡང་བྱེད་པ་པོ་ལ་གནས་པ་ལ་ནི་ལྟུང་བ་མེད་དེ། འདི་ནི་ཁས་བླངས་པ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 64]
གནས་ནས་འཕགས་པར་འགྱུར་བ་ན་ཉམ༌[^46]ང༌[^47]དང་ཕྲད་པར་མི་འགྱུར་བ་ལྟ་ན་གནས་མལ་བསྡུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བླ་གབ༌[^48]མེད་པ་འམ་གཡོགས་པ༌[^49]ལ་ཡང་ཞེས་བྱ་བ་བྱེ་བྲག་ཡོངས་སུ་འཛིན་པར་རྟོགས་པའོ། །

[Block 65]
འདིར་གཞུང་ནི་ཕྲན་ཚེགས་དག་ལས་དགེ་སློང་གིས༌[^50]གནས་མལ་བསྡུས་ནས་འགྲོ་བར་བྱའོ། །

[Block 66]
མི་སྡུད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 67]
ཉམ༌[^51]ང་བ་དང་ཕྲད་པར་མི་འགྱུར་བ་ལྟ་ན་ཞེས་སྨོས་པ་ནི་གནས་མལ་སྡུད་པར་བྱེད་པ་ན༌[^52]མཆིས་པའི་དབང་གིས་གལ་ཏེ་ན༌[^53]སྲོག་གི་བར་ཆད་ལ་སོགས་པས་འབྱུང་བར་དོགས་པ་དང་ཉམ༌[^54]ང་བ་ལ་གནས་པ་ཞེས་བྱ་བ་འདིའི་དོན་དུའོ། །

[Block 68]
གལ་ཏེ་དྲི་མ་ཅན་དུ་གྱུར་ན་སྤྲུག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་མ་མོ་ལས་དགེ་སློང་འགྲོ་བར་ཆས་པ་ཞེས་བྱ་བ་ནས་གནས་མལ་དྲི་མ་ཅན་དུ་གྱུར་པ་ན་སྤྲུག་པར་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 69]
དེ་དབུལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཉམ༌[^55]ང་བ་དང་ཕྲད་པར་གྱུར་པའི་གནས་མལ་ལོ། །

[Block 70]
ཡང་ན་བཅོལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཉམ༌[^56]མི་ང་བར་ཕྲད་པར་མི་འགྱུར་བར་ལྟ་ན་ཞེས་བྱ་བ་ནི་རྗེས་སུ་སྦྱར་རོ། །

[Block 71]
གང་ལ་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་ལའོ། །

[Block 72]
མེད་ན་དགེ་ཚུལ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མེད་ན་དགེ་ཚུལ་ལ་དེ་བཅོལ་བར་བྱའོ། །

[Block 73]
དེ་ཡང་མེད་ན་ཁྱིམ་བདག་ལའོ་ཞེས་བྱ་བ་ནི་དགེ་ཚུལ་དེ་ཡང་མེད་ན་ཁྱིམ་བདག་ལ་དེ་བཅོལ་བར་བྱའོ། །

[Block 74]
ཐམས་ཅད་མེད་ན་ཕྱོགས་བཞིར་རྣམ་པར་བལྟས་ཏེ་ལྡེ་མིག་སྦས་ནས་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བཅོལ་བར་བྱ་བ༌[^57]ཐམས་ཅད་མེད་ནའོ། །

[Block 75]
གལ་ཏེ་ལམ་ཁར་དགེ་སློང་མཐོང་ན་ཕྱོགས་དེ་དེ་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་དུ་ལྡེ་མིག་སྦས་པའོ། །
--- END BLOCKS ---
