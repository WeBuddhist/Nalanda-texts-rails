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
[Block 4131]
དེར་རྟ་བབས་བསྒྲེང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དེར་ཞེས༌[^4218]བྱ་བ་ནི་གཙང་ཁང་གི་མུ་ཁྱུད་དེར་རོ། །

[Block 4132]
སྒོ་ཡབ་བྱའོ་ཞེས་བྱ་བ་ནི་སྒོ་ཡབ་བྱ་བའོ། །

[Block 4133]
གཙང་ཁང་གི༌[^4219]མུ་ཁྱུད་དེའི་མདུན་རོལ་དུ་སྒོ་ཡབ་ཀྱི་ཁྱམས་བྱ་བ་སྟེ་སྒོའི་དྲུང་དུ་ཁང་པ་བྱའོ། །

[Block 4134]
དེ་ལ་ལན་ཀན་གྱིས་བསྐོར་རོ་ཞེས་བྱ་བ་ལ།[^4220] དེ་ལ་ཞེས་བྱ་བ༌[^4221]ནི་སྒོ་ཡབ་དེ་ལའོ། །

[Block 4135]
ཀ་བ་རྣམས་བཙག༌[^4222]གིས་བསྐུའོ། །

[Block 4136]
རྩིག་པ་དག་རྒྱ་སྐྱེགས་ཀྱིས་བྲིའོ།[^4223] །དྲིས་དབང་བསྐུར་བ་དབུལ་ལོ་ཞེས་བྱ་བ་ནི་ཆོས་དང་མཐུན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4137]
འབྲུ་མར་དང་བ་བླ་དང་ཙནྡན་དང་གུར་གུམ་གྱིས༌[^4224]ཆག་ཆག་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་འབུལ་བ་ཆོས་དང་མཐུན་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4138]
གཟེར་བུ་མི་གདབ་བོ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་ལ་གོས་ལ་སོགས་པ་སྤྱད་པའི་ཕྱིར་གཟེར་བུ་གདབ་པར་མི་བྱ་བའོ། །

[Block 4139]
བརྩིག་པའི༌[^4225]ཚེ་ཕྲེང་བ་ལ་སོགས་པ་གདགས་པའི་ཕྱིར་ཟུངས་ཐག༌[^4226]གཞུག་གོ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་ལའོ། །

[Block 4140]
མི་དབུག་གོ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་ལ་ཟུངས་གཞུག༌[^4227]པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 4141]
སྟེང་དུ་མར་མེ༌[^4228]མི་གཟུགས་སོ། །

[Block 4142]
མཆོད་པ་བྱ་བའི་ཕྱིར་ཁྱིམ་པ་དག་འཛེག་ཏུ་གཞུག་གོ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་ལའོ། །

[Block 4143]
མེད་ན་དགེ་ཚུལ་དག་དྲིའི་ཆུས་རྐང་པ་བཀྲུས་ཏེའོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་མེད་ནའོ། །

[Block 4144]
གལ་ཏེ་དེ་མ་བྱས་ན་དྲི་དག་གིས་དྲིལ་ཕྱིས་བྱས་ཏེའམ་གོས་ཀྱིས་དཀྲིས་ཏེ་སྟོན་པའི་འདུ་ཤེས་མངོན་དུ་བྱས་ནས་དོན་གྱི་བརྣབ་སེམས་ཀྱི༌[^4229]དྲན་པ་དག་གིས་སོ་ཞེས་བྱ་བ་ལ། གལ་ཏེ་དེ༌[^4230]མ་བྱས་ན་ཞེས་བྱ་བ་ནི་དྲིའི་ཆུ་དང་གཞན་གྱིས་སོ། །

[Block 4145]
གལ་ཏེ་དྲིའི་ཆུས་རྐང་པ་བཀྲུ་བ་དག་མ་བྱས་ན་དེའི་ཕྱིར་དྲི་དག་གིས་རྐང་པ་དྲིལ་ཕྱིས་བྱ་སྟེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4146]
དོན་གྱི་ཞེས་བྱ་བ་ནི་མཆོད་པར་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་དེ་ལའོ། །

[Block 4147]
དྲན་པ་དག་གིས་སོ་ཞེས་བྱ་བ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་ཀྱིས་སོ། །

[Block 4148]
དེ་དག་ཀྱང་མེད་ན་དགེ་སློང་དག་གིས་དེ་བཞིན་དུའོ་ཞེས་བྱ་བ་ནི་དགེ་ཚུལ་དེ་དག་ཀྱང་མེད་ན་དགེ་སློང་དག་གིས་དྲིའི་ཆུས་རྐང་པ་བཀྲུ་བ་ལ་སོགས་པའི་རྣམ་པ་ཇི་སྐད་བསྟན་པ་བཞིན་བྱ་སྟེ་འཛེག་པར་བྱའོ། །

[Block 4149]
དེའི་ཆེད་དུ་ཐག་པས་གདགས་སོ་ཞེས་བྱ་བ་ལ། དེའི་ཆེད་དུ་ཞེས་བྱ་བ་ནི་འཛེག་པ་དེའི་ཆེད་དུའོ། །

[Block 4150]
རིན་པོ་ཆེ་ལས་བྱས་པའི་ཕྲེང་བ་དབུལ་ལོ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་ལའོ། །

[Block 4151]
འཇིག་པར་བྱེད་པ་ཟློག༌[^4231]པའི་ཕྱིར་དབུ་གཡོགས་གཡོགས་སོ༌[^4232]ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་ལའོ། །

[Block 4152]
མུན་ནག༌[^4233]མི་གནས་པར༌[^4234]བྱ་བའི་ཕྱིར་དེ་ལ་སྒོ་གདོད་དོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་དབུ་གཡོགས་ཏེ་དེ་ལའོ། །

[Block 4153]
སངས་རྒྱས་ཀྱི་སྐུ་གཟུགས་བྱའོ་ཞེས་བྱ་བ་ནི་ཆོས་དང་མཐུན་པ་ཉིད་ཡིན་པའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4154]
དེ་ལ་དུས་སྟོན་བྱའོ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་སྐུ་གཟུགས་དེ་ལའོ། །

[Block 4155]
བལྟམས་པ་དང་གཙུག་པུད་དང་དབུ་སྐྲ་དང་བྱང་ཆུབ་པའི་དུས་སྟོན་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་བྱའོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས་པའི་ཕྱིར་ཀྱང་ངོ་ཞེས༌[^4235]སྒྲ་སྨོས་སོ། །

[Block 4156]
དུས་སྟོན་ཞེས་བྱ་བའི་སྒྲས་ནི་བལྟམས་པ་ལ་སོགས་པ་དང་སོ་སོར་སྦྱར་རོ། །

[Block 4157]
དེ་གྲོང་ཁྱེར་དུ་གཤེགས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་སྐུ་གཟུགས་དེའོ།[^4236] །འདི་ལ་དགེ་སློང་གིས་བསྐུར་དུ་རུང་ངོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་གྲོང་ཁྱེར་དུ་ཞུགས་པ་འདི་ལས་ཏེ། སངས་རྒྱས་ཀྱི་སྐུ་གཟུགས་བསྐུར་བ་དེ༌[^4237]ལའོ། །

[Block 4158]
དེ་ནི་གསར་བུ་དག་ལ་འབབ་བོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་བསྐུར་བ་དེའོ། །

[Block 4159]
སྡེ་པ་ལྔ་པོ་དག་གིས་ཞབས་འབྲིང་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་ལ་སོགས་པ་དག་གིས་སོ། །

[Block 4160]
མཆོད་ཡོན་དུ་བྱ་བ་ནི་རྒན་པ་དག་གིས་གཟུང་ངོ་། །དེ་ལ་རོལ་མོ་བྱེད་པ་དག་གིས་རོལ་མོ་བྱ་བ་དང་། བཀུར་སྟི་ཆེན་པོ་གཞན་ཡང་བཟང་ངོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་སྐུ་གཟུགས་གྲོང་ཁྱེར་དུ་གཤེགས་པར་བྱ་བ་དེ་ལའོ། །

[Block 4161]
རོལ་མོ་བྱེད་དུ་གཞུག་པའི་ཕྱིར་ཀྱེ་མི་དག་སྟོན་པ་ལ་མཆོད་པར་གྱིས་ཤིག་ཅེས་བྱ་བ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་དོ་ཞེས་སྨོས་ནས། ཇི་ལྟར་བསྒྲགས་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ལམ་པོ་ཆེ་དང་ལམ་སྲང་དང་བཞི་མདོ་དང་སུམ་མདོ་དག་ཏུ་སང་ངམ་གནང༌[^4238]འབྱུང་བར་འགྱུར་བ་ཉིད་ནི༌[^4239]ཡི་གེར༌[^4240]བྲིས་པས་བསྒྲགས་པར༌[^4241]བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4162]
ཇི་ལྟར་ཡི་གེར་བྲི་བར་བྱ་ཞེ་ན་དེའི་ཕྱིར་དེ་ལྟར་སངས་རྒྱས་གཤེགས་པར་འགྱུར་རོ་ཞེས་གྲོ་ག་ལ་སོགས་པ་ལ༌[^4242]བྲིས་པ་གླང་པོ་ཆེའི་བཤུལ༌[^4243]སྟེང་དུ་གདུགས་དང་། རྒྱལ་མཚན་དང་། བ་དན་ལ་སོགས་པས་ཡོངས་སུ་བསྐོར་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལྟར་སངས་རྒྱས་གཤེགས་པར་འགྱུར་རོ་ཞེས༌[^4244]སྨོས་པ་ལ་སྙེགས༌[^4245]པའོ། །

[Block 4163]
བྱང་ཆུབ་སེམས་དཔའི་སྐུ་གཟུགས་བྱ་བ་ཆོས་དང་ལྡན་ནོ། །

[Block 4164]
དེ་རྒྱལ་མཚན་དག་གིས་བསྐོར་རོ། །

[Block 4165]
ལན་ཀན་གྱིས་བསྐོར་རོ། །

[Block 4166]
ལྕགས་ཀྱི༌[^4246]ཀ་བ་དག་གིས་སོ། །

[Block 4167]
དེ་དག་ལ་བ་དན་གདགས་སོ་ཞེས་བྱ་བ་ནི་ལྕགས་ཀྱི་ཀ་བ་དེ་དག་ལ་བ་དན་དག་གདགས་པ་ནི་ཆོས་དང་མཐུན་པའོ། །

[Block 4168]
རྗེས་སུ་འགྲོ་བ་བྱའོ། །

[Block 4169]
རྐང་རྒྱན་དང་རྣ་རྒྱན་མ་གཏོགས་པའི་རྒྱན་གདགས་སོ། །

[Block 4170]
སངས་རྒྱས་ཀྱི་སྐུ་གཟུགས་བརྙན་དང་བདག་པོ་གཞན་ལ་དེ་གཉིས་མ་གཏོགས་པའི་ཆོས་དང་མཐུན་པ་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པར་བྱའོ། །
--- END BLOCKS ---
