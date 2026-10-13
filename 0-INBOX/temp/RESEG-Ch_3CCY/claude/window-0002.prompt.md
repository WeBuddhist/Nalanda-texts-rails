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
ཇི་ལྟར་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་གནས་པ་ལ་སོགས་པ་མ་གྲུབ༌[^56]ལ། དེ་བཞིན་དུ་དམན་པ་དང་མཉམ་པ་དང་ཁྱད་པར་ཅན་རྣམས་ཀྱང་ངོ་། །དེ་ལ་དམན་པ་ནི་ཁྱད་པར་ཅན་མ་ཡིན་པ་སྟེ། འདི་ལྟ་སྟེ་ཉོན་མོངས་པའོ། །

[Block 72]
ཁྱད་པར་ཅན་ནི་དགེ་བ་སྟེ། འདི་ལྟ་སྟེ་དགེ་བ་ལ་སོགས་པའོ། །

[Block 73]
མཉམ་པ་ནི་བར་མ་སྟེ་ལུང་དུ༌[^57]མ་བསྟན་པ་འདི་ལྟ་སྟེ། མིག་ལ་སོགས་པ་རྣམས་སོ་ཞེས་བྱ་བའོ། །

[Block 74]
འདི་དག་ནི་ཉེ་བར་བསྟན་པ་ཙམ་སྟེ། འདི་ལྟར་ཁྱད་པར་ཐམས་ཅད་འདིར་གནས་པ་ལ་སོགས་པ་མ་གྲུབ་པས་མ་གྲུབ་པར་ཁོང་དུ་ཆུད་པར་བྱ་བ་ཐ་སྙད་ཀྱི་དབང་གིས་བརྗོད་པས་ལུང་གི་གནོད་པ་སྤང་བར་བྱའོ། །

[Block 75]
ངང་གི་སྒྲའི་དོན་ལ་འམ་གྱི་སྒྲའོ། །

[Block 76]
དེ་ཡང་མ་སྨོས་པ་རྣམས་སྡུད་པའོ་ཞེས་བྱ་སྟེ། རྣམ་པར་བརྟགས་པ་ཐམས་ཅད་དགག་པ་གནས་པ་ལ་སོགས་པ་དགག་པའི་སྒོ་ནས་གསུངས་པ་ལ། ལུང་གིས་གནོད་པ་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་དབང་གིས་གསུངས་པས་སྤང་བར་བྱོས་ཤིག །སླར་ཡང་འདི་དག་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་ངོར་འཇུག་པས༌[^58]མཛད་པའི་དགོས་པ་ཅི་ཞེ་ན། འདི་ལ་དགོས་པ་ཆེ་སྟེ། འཇིག་རྟེན་པའི་ཐ་སྙད་ཁས་མ་བླངས་ན་འཇིག་རྟེན་པ་དང་མི་མཐུན་པས་རྟག་ཏུ་འཇིག་རྟེན་པའི་ལོག་རྟོགས༌[^59]ལས་བཟློག་པར་ནུས་པ་མ་ཡིན་ཏེ། ཀླ་ཀློ་བཞིན་ནོ། །

[Block 77]
ཀླ་ཀློ་འཕགས་པའི་སྐད་མི་ཤེས་པ་ལ་འཕགས་པའི་སྐད་འགའ་ཞིག༌[^60]ལས་བཟློག་པར་མི་ནུས་ལ། ཀླ་ཀློའི་སྐད༌[^61]རྗེས་སུ་མཐུན་པས་བདེ་བླག་ཏུ་བཟློག་པར་འགྱུར་རོ། །

[Block 78]
ཡང་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་ཇི་ལྟར་རྟོགས་པའི་ཆོས་ཉིད་ལ་གནས་པར་གྱུར་ན། དེའི་ཚེ་སངས་རྒྱས་པ་དེ་རྣམས་ལ་དགོས་པ་མེད་པར་འགྱུར་ཏེ། ཆོས་ཉིད་ལ་གནས་པ་རྣམས་གཞན་གྱི་དོན་མི་མཛད་པའི་ཕྱིར་རོ། །

[Block 79]
ཆོས་ཉིད་ལ་གནས་པ་དེ་རྣམས་ནི།

[Block 80 [VERSE]]
བརྗོད་པར་བྱ་བ་ལྡོག་པས་ན། །
སེམས་ཀྱི་སྤྱོད་ཡུལ་ལྡོག་པ་སྟེ། །
མ་སྐྱེས་པ་དང་མ་འགགས་པའི། །
ཆོས་ཉིད་མྱ་ངན་འདས་དང་མཚུངས། །

[Block 81]
ལུང་ལས་ཀྱང་གསུངས་པ།

[Block 82 [VERSE]]
སངས་རྒྱས་འགའ་ཡང་མི་ཤེས་ཤིང་། །
ཡང་ན་སངས་རྒྱས་ཆོས་ཉིད་མིན། །
འཇིག་རྟེན་རྣམ་འདྲེན་འཇིག་རྟེན་དུ། །
གལ་ཏེ་འཇིག་རྟེན་རྗེས་འཇུག་མིན། །

[Block 83]
ཞེས་སོ། །

[Block 84]
ཡང་ན་རང་གིས་རྟོགས་པའི་ཆོས་ཉིད་ཁོ་ན་སྒྲོ་བཏགས་ནས་རྗོད་བྱེད་དང་བརྗོད་བྱའི་ཐ་སྙད་ལ་གནས་ཏེ་ཉེ་བར་སྟོན་པར་མ་གྱུར་ན། དེ་ཡང་འཇིག་རྟེན་པའི་དོན་སྒྲུབ་པར༌[^62]མི་ནུས་ལ། ཇི་སྐད་དུ་ལུང་བཞི།[^63] བམ་པོ་གྱ་དྲུག་པ།[^64] དེ་ནས་བཅོམ་ལྡན་འདས་སངས་རྒྱས་ནས་རིང་པོ་མ་ལོན་པ་ན་འདི་སྐད་གསུངས་ཏེ། བདག་གིས་ཆོས་ཉིད་ཟབ་མོ་ཟབ་མོར་སྣང་བ་མཐོང་དཀའ་བ་རྟོགས་དཀའ་བ་བརྟག་དཀའ་བ། བརྟག་པའི་སྤྱོད་ཡུལ་མ་ཡིན་པ་ཕྲ་བ་མཛངས་པ༌[^65]མཁས་པ་སྒྲིན་པོས་ཤེས་པར་བྱ་བ་ཁོང་དུ་ཆུད་དེ། དེ་བདག་གིས་གལ་ཏེ་གཞན་ལ་བསྟན་པར་གྱུར་ཀྱང་གཞན་གྱིས་ཤེས་པར་མི་འགྱུར་གྱི། དེའི་ཚེ་བདག་ནི་ཉམས་པར་འགྱུར། ལ་བར་འགྱུར། སེམས་མི་སྤྲོ་བར་འགྱུར། གང་དུ་བདག་ཉིད་གཅིག་པུ་ཞིག །དགོན་པ་དབེན་པ༌[^66]མཐོང་བའི་ཆོས་ལ་བདེ་བས་གནས་པའི་རྣལ་འབྱོར༌[^67]དང་ལྡན་པས་བདེ་བར་གནས་པར་འགྱུར་རོ། །

[Block 85]
དེ་ནས་མི་མཇེད་ཀྱི་བདག་པོ་ཚངས་པའི༌[^68]འཇིག་རྟེན་ན་གནས་པས་འདི་སྐད་སྨྲས་སོ། །

[Block 86]
ཀྱེ་མ་འཇིག་རྟེན་འདི་དག་ནི་བརླག་གོ། །

[Block 87]
ད་ནི་གང་དུ༌[^69]ན་འགའ་ཞིག་ཏུ། དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་འགའ་ཞིག་འཇིག་རྟེན་དུ་འབྱུང་བ་ནི་འདི་ལྟ་སྟེ། ཨུ་དུམ་བཱ་རའི་མེ་ཏོག་བཞིན་ལ། དེ་ནི་དེ་སང་ན་བཅོམ་ལྡན་འདས་ཆོག་ཤེས་པ་ལ་གནས་པ༌[^70]ཐུགས་སྤྲོ་བར་འགྱུར་གྱི། ཆོས་འཆད་པ་ལ་ནི་མ་ཡིན་པས་བདག་ནི་གང་དུ་བཅོམ་ལྡན་འདས་ཀྱི་ཐད་དུ་དོང་ལ་གསོལ་བ་གདབ་པར་བྱའོ། །

[Block 88]
དེ་ནས་མི་མཇེད་ཀྱི་བདག་པོ་ཚངས་པས་འདི་ལྟ་སྟེ། སྐྱེས་བུ་སྟོབས་དང་ལྡན་པའི་ལག་པ་བསྐུམ་པ་ལས་བརྐྱང་བའམ། བརྐྱང་བ་ལས་བསྐུམ་པ་བཞིན་མི་མཇེད་ཀྱི་བདག་པོ་ཚངས་པའི་འཇིག་རྟེན་དུ་མི་སྣང་བར་གྱུར་ནས། བཅོམ་ལྡན་འདས་ཀྱི་མདུན་དུ་འཁོད་པར་གྱུར་ཏོ། །

[Block 89]
དེ་ནས་མི་མཇེད་ཀྱི་བདག་པོ་ཚངས་པས་དེའི་ཚེ་ན་ཚིགས་སུ་བཅད་པ་འདི་དག་སྨྲས་སོ། །

[Block 90 [VERSE]]
མ་ག་དྷཱར་ནི་སྔོན་ཆད་མ་བྱུང་ཆོས། །
བརྗོད་བྲལ་དྲི་མར་བཅས་པ་རྗེས་སུ་རིག །
[^71]ཉོན་མོངས་མེད་ཅིང་རྡུལ་དང་བྲལ་བའི་ཆོས། །
བདུད་རྩིའི་སྒོ་མོ་གསལ་བར་མཛད་དུ་གསོལ། །

[Block 91]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་ཚེ་ཚིགས་སུ་བཅད་པ་འདི་དག་བཀའ་སྩལ་ཏོ། །

[Block 92 [VERSE]]
ཚངས་པ་བདག་གིས་ཚོགས་ཆེན་པོས། །
སྲིད་པའི་འདོད་ཆགས་ཡོངས་བསྲབས་ཤིང་། །
ཐ་བ་བཅོམ་ནས༌[^72]རྟོགས་པ་ཡི། །
ཆོས་འདི་རྟོགས་པར་སླ་མ་ཡིན། །

[Block 93 [VERSE]]
རྒྱུན་ལས་བཟློག་པ་ལྟ་བུའི་ལམ། །
ཟབ་མོ་ཤིན་ཏུ་མཐོང་བ༌[^73]དཀའ། །
སྲིད་པའི་འདོད༌[^74]ཆགས་མུན་པ་ཡི། །
ཕུང་པོས་བསྒྲིབས་པས་མཐོང་བ༌[^75]མིན། །

[Block 94]
ཞེས་གསུངས་སོ། །

[Block 95]
དེའི་ཕྱིར་ན་ངེས་པར་འདི་རྣམས་ཀྱིས་ཇི་ལྟར་གནས་པའི་འཇིག་རྟེན་གྱི་ཐ་སྙད་ནི་འཇིག་རྟེན་པའི་དོན་བྱེད་པའི་ཐབས་ཀྱི་ཕྱིར་ཐོག་མ་ཉིད་དུ་ཁས་བླང་བར་བྱ་སྟེ། འཇིག་རྟེན་པས་རྟོགས་པའི་ཐབས་སུ་གྱུར་པ་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཁས་མ་བླངས་པར་འཇིག་རྟེན་པས་རྟོགས་པར་བྱེད༌[^76]ནུས་པ་མ་ཡིན་ནོ། །

[Block 96]
ཡང་ཇི་ལྟར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རང་ཉིད་ཀྱིས་དངོས་པོར་གྱུར་པ་ཅུང་ཟད་མ་དམིགས་ཀྱང་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་རྗེས་སུ་མཐུན་པ་འབའ་ཞིག་གིས་ཉེ་བར་སྟོན་པར་མཛད་ཅེ་ན། འདི་ནི་རབ་ཏུ་གྲགས་པའི་དཔེ་གཅིག་ཙམ་སློབ་དཔོན་གྱིས༌[^77]བརྗོད་པར༌[^78]འདོད་པའི་དོན་བསྒྲུབ་པའི་ཕྱིར་ཉེ་བར་བསྡུ་བར་བྱའོ། །

[Block 97]
ངར་འཛིན་པ་དང་ང་ཡིར་འཛིན་པ་མེད་པའི་བདེ་བར་གཤེགས་པས་འཇིག་རྟེན་པའི་ངོར་འཇུག་ཏུ༌[^79]དང་ངའི་ཞེས་པས་སྐད་གཞན་ཇི་ལྟ་བ་དེ་ལྟར་གསུངས་ཏེ།[^80] དེ་ལ་ངའོ་ཞེས་པས་བདག་ཏུ་མངོན་པར་ཞེན་པ་ནི་ངར་འཛིན་པའོ། །

[Block 98]
བདག་གི་འོ་ངའི་འོ་ཞེས་མངོན་པར་ཞེན་པ་ནི་ང་ཡིར་འཛིན་པའོ། །

[Block 99]
ང༌[^81]དང་ང་ཡིར་འཛིན་པ་འདི་གཉིས་ཀྱང་འཇིག་ཚོགས་ལ་ལྟ་བའི་ཡན་ལག་སྟེ། དེ་ལས་བདག་དང་བདག་གིར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 100]
དེ་ལ་འཇིག་ཚོགས་སུ་ལྟ་བ་འདི་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས་རབ་ཏུ་སྤངས་པའི་ཕྱིར། སྤངས་པས་ན་བདེ་བར་གཤེགས་པ་ལ་ངར་འཛིན་པ་དང་ང་ཡིར་འཛིན་པའི༌[^82]ཕྱིར་རོ། །

[Block 101]
དེ་ལ་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་སྟོབས་ཀྱིས་མངོན་པར་འདོད་པའི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་ཉེ་བར་ལོངས་སྤྱོད་པར་དགོངས་པའི་དུས་སུ་ཉེ་བར་བཏུད་པ་གང་ཞིག་ལ་ཉེ་བར་ལོངས་སྤྱོད་པ་དང་ལྡན་ཞིང་། ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་སྟོབས་ཀྱིས་ཉེས་པ་མ་ལུས་པ་དང་བྲལ་ཞིང་། ཡོན་ཏན་དང་ལྡན་པའི་ལམ་གྱིས་ཐོབ་པ༌[^83]མཐའ་ཡས་པའི་སེམས་ཅན༌[^84]ཕན་འདོགས་པའི་ཕྱིར་མཛེས་པར་གཤེགས་པས་ན་བདེ་བར་གཤེགས་པའམ་སངས་རྒྱས་ནི་ཆོས་ཐམས་ཅད་ལ་སྒྲིབ་པ་མེད་པར་རྣམ་པ་ཐམས་ཅད་མཁྱེན༌[^85]པའི་ཡེ་ཤེས་ཀྱིས་ཡང་དག་པར་རྟོགས་པའི་ཕྱིར་མཛེས་པར་གཤེགས་པས་བདེ་བར་གཤེགས་པའོ། །

[Block 102]
ཕྱིར་མི་ལྡོག་པའི་ཕྱིར་མཐར་ཐུག་པར་གཤེགས་པས་ཏེ་རིམས་ནད་ལེགས་པར་བྱང་བ་བཞིན་ནམ། ཐོག་མ་དང་བར་དང་ཐ་མར་གཅིག་ཏུ་དགེ་བའི་ཆོས་སྟོན་པ་ལ་མཛེས་པར་གཤེགས་པའི་ཕྱིར་བདེ་བར་གཤེགས་པའོ། །

[Block 103]
ངེས་པའི་ཚིག་གི་ཚུལ་གྱིས་བདེ་བར་གཤེགས་པ་ངར་འཛིན་པ་དང་ང་ཡིར་འཛིན་པ་ཤིན་ཏུ་སྤངས་པས་གནས་ཀྱང་ང་དང་ངའི་ཞེས་གསུངས་ཏེ།

[Block 104]
ཇི་སྐད་དུ་ལུང་ལས།

[Block 105]
དགེ་སློང་དག་ངའི་ལྷའི་མིག་རྣམ་པར་དག་པ་མི་ལས་འདས་པས་མཐོང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ་དང་། དེ་བཞིན་གཤེགས་པས་དགེ་སློང་དག་ང་ནི་གཅིག་པུ༌[^86]དབེན་པ་ཞིག༌[^87]ན་གནས་པ་ན་ཞེས་པས༌[^88]འདིར་ང་ཡི་བ་གསུངས་སོ། །

[Block 106]
བདག་ཉིད་ལ་ང་དང་ང་ཡིར་འཛིན་པ་མེད་ཀྱང་ང་དང་ང་ཡི༌[^89]ཞེས་པ་གསུངས་པས་འཇིག་རྟེན་པས་རྟོགས་པའི་ཐབས་སུ་འགྱུར་བའི་ཕྱིར་འཇིག་རྟེན་པ་ལ་ལྟོས་ནས་ང༌[^90]དང་ང་ཡི་ཞེས་གསུངས་ལ། འདི་ལྟར་གཙུག་ན་ནོར་བུའི་རྟོགས་པ་བརྗོད་པ་ལ་སོགས་པར་བྱ་དཀའ་བ་བརྒྱ་ཕྲག་གསུངས་པ་དེ་གང་ཞིག་དེའི་ཚེ་ལོང་བ་ཆེན་པོར་གྱུར་པ་དང་གང་དུ་འདི་ལྟར་བྱ་དཀའ་བ་བརྒྱ་ཕྲག་གསུངས་ཤེ་ན། དེ་དག་གོ་བར་འདོད་པའི་འཇིག་རྟེན་པ་ལ་གལ་ཏེ་ང་ཉིད་དེའི་ཚེ་ན་ཞེས་མ་གསུངས་ན་འཇིག་རྟེན་པས་རྟོགས་པར་འདོད་པའི་དོན་མི་རྟོགས་པར་འགྱུར་བའམ།[^91] དེ་བཞིན་གཤེགས་པའི་སྤྱོད་པ་ལ་ངོ་མཚར་བར་ཡང་མི་འགྱུར་རོ། །

[Block 107]
དེ་བཞིན་དུ་ང་ཡིར་འཛིན་པ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 108]
གང་ཡང་འདི་ལྟར་ང་དང་ང་ཡིར་འཛིན་པ་མེད་ཀྱང་འཇིག་རྟེན་པའི་ངོར་འཇུག་ཏུ༌[^92]ང་དང་ང་ཡིར་འཛིན་པ་ཡོད་པ་ལྟ་བུར་མཚོན་ནོ། །

[Block 109]
དེ་བཞིན་དུ་དངོས་པོར་གྱུར་པ་གཞན་གསུང་བ་ན་ཡང་དངོས་པོ་དེའི་རང་བཞིན་ལྟ་བུར་མཚོན་པར་ཁས་བླང་བར༌[^93]བྱའོ། །

[Block 110]
དེའི་ཕྱིར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱིས་གསུངས་པས་དངོས་པོ་ཡོད་པ་མ་ཡིན་པ་ཉིད་དེ་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་རྗེས་སུ་འཇུག་པས་གསུངས་པའོ༌[^94]ཞེས་ཤེས་པར་བྱའོ། །
--- END BLOCKS ---
