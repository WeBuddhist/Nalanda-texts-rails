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
[Block 176]
གདིང་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 177]
སྐྲོད་པའི་ལྟུང་བྱེད་ལ་བྱེད་པ་པོ་ཉིད་གང་ཡིན་ཞེ་ན་དེའི་ཕྱིར་དགེ་སློང་ཉིད་དང་དགེ་འདུན་གྱི་གཙུག་ལག་ཁང་ཉིད་དག་ནི་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 178]
ཅི་བསམ་པ་ཐམས་ཅད་ཀྱིས་དེ་ཉིད་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན་དེའི་ཕྱིར། གལ་ཏེ་དེ་ལ་གནོད་པ་དང་དགེ་འདུན་འཁྲུག་པ་སྐྱེ་བ་ཉེ་བར་ཞི་བར་མི་འགྱུར་བའི་གཉེན་པོར་འདོད་པ་མ་ཡིན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་ཉིད་གང༌[^113]ལ་བྱེད་པ་པོ་ཉིད་དུ་བརྗོད་པ་དེ་ལ་སྲོག་གཏོང་བ་ལ་སོགས་པས་གནོད་པ་ནི་དེ་ལ་གནོད་པའོ། །

[Block 179]
དེ་ལ་གནོད་པ་དང་དགེ་འདུན༌[^114]འཁྲུག་པ་དག༌[^115]ལ་སྐྱེ་བ་དང་སྐྲོད་པ་གཉིས་ལ་ཉེ་བར་ཞི་བར་མི་འགྱུར་བར་དོགས་པ་ཡོད་པ་ལས་བསམ་པ་གཞན་ལ་འདི་དག་ལས་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 180]
དེ་གཉིས་གང་ལ་བྱེད་པ་པོ་ཉིད༌[^116]ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྐྲོད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །སུས་ཤེ༌[^117]ན། དེའི་ཕྱིར་གཞན་གྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། [^118]རང་ཉིད་གཅིག་པུ་ནི༌[^119]མ་ཡིན་ནོ། །

[Block 181]
གཞན་གྱིས་རྗེས་སུ་འཇུག་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི། གཞན་དག་བསྐོས་ནས་སྐྲོད་པར་བྱེད་ན་ལྟུང་བ་མེད་པའམ་ན་སྨད་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 182]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་སྐྲོད་པར་བྱེད་ན་གཉི་ག་ལ་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 183]
དགེ་སློབ༌[^120]མ་དང་དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་རྣམས་ཀྱིས་ནི་ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བ་ནི་འདི་རྣམས་སྐྲོད་པར་བྱེད་པ་རྣམས་ལ་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ། །

[Block 184]
འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་ལས་དགེ་སློང་གིས༌[^121]དགེ་སློབ་མ་དང་དགེ་ཚུལ་དང་དགེ་ཚུལ་མས་དགེ་སློང་སྐྲོད་པར་བྱེད་ན་ལྟུང་བྱེད་དོ། །

[Block 185]
དགེ་སློབ་མ་དང་དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་ལ་ནི་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 186]
དེ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་སློབ་མ་ལ་སོགས་པ་བསྐྲད་པར་བྱ་བ་རྣམས་ལ་སྐྲོད་ནའོ། །

[Block 187]
འདིར་གཞུང་ནི་ཕྲན་ཚེགས་རྣམས་ལས་དེར་དགེ་ཚུལ་དེའི་རྣམ་པས་ཅིག་ཤོས་དག་ལ་འདི་བསྡུ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 188]
བཞད་གད་ཀྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་སྐྲོད་ན་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ། །

[Block 189]
ཁྱིམ་པ་རྣམས་ལ་ནི༌[^122]བསོད་ནམས་མ་ཡིན་པ་མང་པོ་ཞེས་བྱ་བ་ནི་སྐྲོད་པར་བྱེད་པ་ཁྱིམ༌[^123]པ་རྣམས་ཡིན་ན་དེ་རྣམས་ལ་ནི་བསོད་ནམས་མ་ཡིན་པ་མང་པོར༌[^124]བྱེད་པ་པོ་ཉིད་ཡིན་ནོ། །

[Block 190]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་ཁྱིམ་པ་དང་ཁྱིམ་པ་མོས་དགེ་སློང་སྐྲོད་དུ་བཅུག་ན་ལྟུང་བྱེད་དོ། །

[Block 191]
ཁྱིམ་པ་དང་ཁྱིམ་པ་མོ་ལ་ནི་བསོད་ནམས་མ་ཡིན་པ་མང་དུ་བསྐྱེད་པར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 192]
སྐྲོད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 193]
ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མིང་ཅན་དུ་སྦྱོར་བ༌[^125]བྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་གྱི་གཙུག་ལག་ཁང་གི་གནས་སུ་དགེ་སློང་ཞུགས་པ་ཉིད་ལའོ་ཞེས་བྱ་བ༌[^126]སྨོས་ཏེ། དགེ་འདུན་གྱི་གཙུག་ལག་ཁང་གང་ཡང་རུང་བ་དང་འབྲེལ་པའི་གནས་རྟེན་པ་ཉིད་དུ་དགོས་པ་ལ་སའི་ཕྱོགས་གཞན་ལ་གཙུག་ལག་ཁང༌[^127]གི་གནས་ཉིད་དུ་བརྗོད་པའོ། །

[Block 194]
འདི་ལྟ་བུ་ལ་སྔར་ཁས་བླངས་པའི་དགེ་སློང་གིས་ཞུགས་པ་ཉིད་ལ་གང་དེ་ལ་ལྟུང་བ་འབྱིན་པར་བྱེད་པའི་འདུ་ཤེས་གནས་འདི་ན་དགེ་སློང་འདིས་གནས་འདིར་ལྷག་པར་གནས་སོ༌[^128]སྙམ་དུ་འདུ་ཤེས་འདི་ཡོད་པ་ལ་གནས་དེ་ལ་ནི་ལྟུང་བའི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ། །

[Block 195]
དེ་ལྟར་དགེ་སློང་གང་ཞིག་སླར་ཤེས་ཤིང་དགེ་འདུན་གྱི་གཙུག་ལག་ཁང་ན་དགེ་སློང་དག་སྔ༌[^129]ན་འཁོད་པར༌[^130]ཤེས་བཞིན་དུ་ཕྱིས་འོངས་ནས་ཕྱིས་གནོན་བྱེད་ན་ཞེས་བྱ་བ་ལ་སོགས་པའི་མདོ་གསུངས་པ་ཡིན་ནོ། །

[Block 196]
དེ་ལ་གང་དུ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན་དེའི་ཕྱིར་ན་བ་དང་འཇིགས་པའི་དབང་མ་གཏོགས་པར་ཕྱིས་གནོན་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕྱིས་གནོན་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་ནི་གཞན་ལ་མི་འདོད་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 197]
མ་གཏོགས་པར་ཞེས་བྱ་བ་ནི་ན་བ་དང་དེའི་དབང་ཉིད་ཀྱིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 198]
འདིར་གཞུང་ནི་གང་གི་ཚེ་ན་བའམ་འཇིགས་པར་གྱུར་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 199]
དེ་ནི་དཔེ་སྟེ་མཐོ་བཙམས་པར༌[^131]འདུན་པས་དགེ་སློང་ལ་མཐོ་བཙམས་པས༌[^132]ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། འདིར༌[^133]གཞུང་ནི་བར་སྡོམ་ལ།

[Block 200 [VERSE]]
[^134] ངན་དང་བསོད་དང་དྲང་ངོ༌[^135]དང་། །
ཆོལ་ཟངས༌[^136]དང་ནི་བཀྲུ་སྨན་དང་། །
རྣལ་འབྱོར་མཐུན་དང་ཁ་ཏོན་དང་། །
འཇིགས་དང་བཅས་དང་འཇིགས་མེད་དོ། །

[Block 201]
ཞེས་བྱ་བས་དགེ་སློང་གིས་དགེ་སློང་ལ་ཇི་ཙམ་ཅུང་ཟད་ཐོ་འཚམས༌[^137]པར་བྱེད་ན་ཐམས་ཅད་ལྟུང་བྱེད་དུ་འགྱུར་རོ༌[^138]ཞེས་བྱ་བ་དགེ་འདུན་གྱི་གཙུག་ལག་ཁང་དང་འབྲེལ་པའི་གནས་ཀྱི་སྒོ་ལ་རྗེས་སུ་མཐུན་པའི་ས་ཕྱོགས་སུ་ཡང་དག་པར་ཞུགས་པའམ་ཕོངས་པ༌[^139]བསྒྲུབ་པས་རྣམ་པར་འཚེ་བ་སྐྱེད་པའམ༌[^140]འགགས་པས་གང་ཞིག་ཐོ་འཚམས༌[^141]པར་བྱེད་ན་དེ་འདིར་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ་མདོར་བྱས་པ་ནི་བསླབ་པའི་གཞི་རྗེས་སུ་འབྲངས་པས་རྟོགས་པར་བྱའོ། །

[Block 202]
བསྒོ་བ་རྣ་ལ་གཟོན་པ་དང་སྐྲོད་པར་བྱེད་པ་དང་། དེས་ཚིག་དང་དགག་དབྱེ་དང་འདེབས་པར་བྱེད་པ་དང་། སྤྱོད་པ་དང་། བསྡིགས་པ་དང་། ཡོ་བྱད་འཇོག་པ་དང་། བསླབ་པའི་གཞི་རྣམས་ལ་གཞན་དུ་བསླབ་པའི་གཞི་ལས་ལྟུང་བ་ཐ་མི་དད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 203]
འདིར་ཡང་དགེ་འདུན་གྱི་གཙུག་ལག་ཁང་ལ་གནས་པ་རྟེན་པ༌[^142]དོན་མེད་པ་ཉིད་དུ་ཐལ་བའི་ཕྱིར་མ་སྨོས་པའི་ཆོ་ག་གཞན་ལ་རྣམ་པར་འཚེ་བ་ལ་ནི་ཉེས་བྱས་སུ་རྟོགས་པར་བྱའོ། །

[Block 204]
ཕྱིས་གནོན་གྱི་ལྟུང་བྱེད་དོ།། །།

[Block 205]
དགེ་འདུན་གྱི་གཙུག་ལག་ཁང་གི་སྟེང་གི་ཐོག་ཉིད་ནི་བྱེད་པ་པོ་ཞེས་བྱ་བ་ནི། དགེ་འདུན་གྱི་གཙུག་ལག་ཁང་གི་སྟེང་གི༌[^143]ཐོག་ཉིད་ནི་ལྟུང་བའི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ། །

[Block 206]
ཅི་རྣམ་པ་ཐམས་ཅད་ལ་དེ་བྱེད་པ་པོ་ཡིན་ནོ་ཞེ་ན་མ་ཡིན་ཏེ། གལ་ཏེ་བྱིན་གྱིས་གཞོལ་བ་ཉིད་དམ་སྤང་ལེབ་ཉིད་དམ། དེ་དང་འདྲ་བས་གཡོགས་པ༌[^144]ཉིད་མ་ཡིན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་དང་འདྲ་བ༌[^145]ཞེས་བྱ་བ་འདིས་ནི་སྤང་ལེབ་ཀྱི་རྣམ་པ་བཟུང་བ་ཡིན་ནོ། །

[Block 207]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི་བྱིན་གྱིས་གཞོལ་བ་ཡིན་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 208]
གལ་ཏེ་རྐང་པ་འབྱུང་བའི་གླགས་མེད་པ་ཞེས་བྱ་བ་འདི་འདིར་བསྡུས་པའི་དོན་དུ་རིག་པར་བྱའོ། །

[Block 209]
ཅི་འདི་ཉིད་གཅིག་ཏུ་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན་མ་ཡིན་ཏེ། འདིའི་ཕྱིར་གནོན་པར་འོས་པའི་རྩ་བ་ཕུར་བུ་ལྟ་བུ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྲི་དང་ཁྲིའུ་སྨོས་པ་འདིར་བྱས་ཏེ་ཁྲིའུ་དོར་ཅིག་ཅེས་བྱ་བ་འདིར་མཚོན་པ་ཙམ་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 210]
ཡོད་པ་ཉིད་ཀྱི་ཕྱིར་འདི་ལྟ་བུར་གྱུར་པ་གཞན་ལ་ཡང་འདི་ལྟ་སྟེ། ཁྲིའུ་རྐང་པ་དང་འདས་པ་དང་བཅས་པ་འདྲ་བ་ལ་ཉེས་དམིགས་འདྲ་བ་ཉིད་ཀྱིས༌[^146]དེར་ངེས་པར༌[^147]གནས་པ་ལ་སོགས་པ་སྟེ། དེའི་ཕྱིར་གནོན་པར་འོས་པ་ཞེས་བྱ་བའི་ཚིག་བྱས་སོ། །

[Block 211]
ཅི་གནས་སྐབས་ཐམས་ཅད་དུ་འདི་ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ནམ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་བཀན་པ་ཉིད་དང་རྐང་རྟེན་བཅུག་པ་ཉིད་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལས་ཐོག་ཉིད་དང་རྩ་བ་ཕུར་བུ་ལྟ་བུ་ཉིད་དེ་གཉིས་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གནོན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མནན་པར་འོས་པ་ཞེས་བྱ་བ་དབང་དུ་བྱེད་པ་ལས་ཤེས་པར་བྱེད་དོ། །

[Block 212]
མངོན་པར་འདུག་པར་བྱ་བའམ། མངོན་པར་འདུག་པ་ཞེས་བྱ་བ་འདིར་འདུག་པ་ཙམ་ནི་གཙོ་བོར་རྣམ་པར་གནས་པ་ཡིན་ཞེས་བྱ་བ་འདི་ལྟར་ཉེ་བར་བརྟག་པར༌[^148]བྱའོ། །

[Block 213]
ཅི་ཞིག་ཅི་ཡང་རུང་བ་ཉིད་ཀྱིས་དེ་གཉིས༌[^149]ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བའི་རྣམ་པས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 214]
འདིར་གཞུང་ནི་དགེ་སློང་གང་ཤེས་བཞིན་དུ་ཞེས་བྱ་བ་སྨོས་པ་ཡིན་ནོ། །

[Block 215]
རྣམ་པར་འབྱེད་པ་ལས་ཀྱང་འདིར་རང་ཉིད་ཀྱིས་རིག་པར་གྱུར་པའམ་གཞན་དག་གིས་བརྗོད་པས་སོ་ཞེས་གསུངས་སོ། །
--- END BLOCKS ---
