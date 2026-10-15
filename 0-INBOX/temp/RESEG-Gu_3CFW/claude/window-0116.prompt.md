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
[Block 4061]
རྐྱེན་དེ་ལྟ་བུ་དག་བྱུང་ན༌[^4173]བསྒོ་སྟེ་འགྲོ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4062]
ཚངས་པ་མཚུངས་པར་སྤྱོད་པ༌[^4174]ལ་དབེན་པའི་ཕྱོགས་སུ་འདྲེག་མཁན་གྱི་བྱ་བ་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གིས་དགེ་སློང་ལ་དང་། དགེ་སློང་མས་དགེ་སློང་མ་ལའོ། །

[Block 4063]
ཁྲིའུ༌[^4175]ཡན་ལག་ཆག་པ་བཅོས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་ངོ་ཞེས་བྱ་བ་ཡང་དབེན་པའི་ཕྱོགས་སུ་བྱ་བའོ། །

[Block 4064]
འདིར་ཁྲི་ཞེས་སྨོས་པ་ནི་ཁྲིའུ་ལ་སོགས་པ་གཞན་དག་གི་དཔེ་ཡིན་ཏེ། ཁྲིའུ་ལ་སོགས་པ་གཞན་རྣམས་ལ་ཡང་འདི་རིགས་པའི་ཕྱིར་རོ། །

[Block 4065]
ཕྲེང་བའི་རིམ་པ་དག་བརྒྱུ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་དབེན་པའི་ཕྱོགས་སུ་བྱ་བའོ། །

[Block 4066]
དཀོན་མཆོག་མཆོད་པར་གྱུར་པ་སེམས་ཅན་གྱི་གཟུགས་མ་ཡིན་པའི་རི་མོ་འདྲི་བ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་དབེན་པའི་ཕྱོགས་སུ་བྱའོ། །

[Block 4067]
སེམས་ཅན་གྱི་གཟུགས་མ་ཡིན་པ་ཞེས་སྨོས༌[^4176]པ་ནི་འདབ་མ་དང་མྱུ་གུ་ལ་སོགས་པ་དག་བསྡུས་སོ། །

[Block 4068]
དེའི་ཕྱིར་འདྲི་བ་ནི་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེའི་ཕྱིར་འདྲི་བ་ཞེས་བྱ་བ་ནི་བྲི་བའི་ཕྱིར་རི་མོར༌[^4177]བྲི་བ་ཉིད་དོ། །

[Block 4069]
དེའི་ཕྱིར་འདྲི་བ་ནི་འདྲི་བར་རྩོམ་པ་ལ་ནི་ཉེས་པར་འགྱུར་ལ། སེམས་ཅན་གྱི་གཟུགས་མ་ཡིན་པ་ལ་ནི་ཉེས་པར་མི་འགྱུར་བའོ། །

[Block 4070]
རྗེས་སུ་བསྒྲུབ་པའི་སྐབས་བཤད་ཟིན་ཏོ། །

[Block 4071]
[^4178]ཤི་བའི་སྐབས་དང་གཞག་པའི་སྐབས་ལས་གཞན་པའི་རྗེས་སུ་བསྒྲུབ་པའི་སྐབས་རྫོགས་སོ།། །།

[Block 4072]
ད་ནི་ཤི་བའི་སྐབས་དང་གཞག་པའི་སྐབས་སུ་འཇུག་པ་གཞན་ཡིན་པས་དེ་ལྟར་གྱུར་པའི་སློབ་པ་ལ་ཤི་བ་ལ་གང་བྱ་བ་དེ་བརྗོད་པར་བྱ་སྟེ། ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་ཤི་བའི་ལུས་ལ་མཆོད་པ་བྱའོ། །

[Block 4073]
དེ་བསྲེག་པར་བྱའོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་ལུས་ལ་མཆོད་པར་བྱ་སྟེ་བསྲེག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །ཅི་གདོན་མི་ཟ་བར་སྲེག་པ་ཁོ་ན་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར། གལ་ཏེ་སྲོག་ཆགས་དང་བཅས་པའི་རྨ་མེད་པ་ཉིད་ཡིན་ནའོ། །

[Block 4074]
སོ་སོར་བརྟག་པས་ངེས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་ལ་སྲོག་ཆགས་ཡོད་དམ་མེད་པའོ། །

[Block 4075]
འདིར་བསྲེག་པ་ཉིད་ནི་རྣམ་པ་གཅིག་ཉིད་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར། བརྐོ་བའམ་ཆུ་ཀླུང་ལ་བསྐུར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ས་བརྐོས་པར་གཞུག་པའམ་ཆུ་ཀླུང་ལ་བསྐུར་བར་བྱའོ། །

[Block 4076]
མི་རུང་ན་ཚང་ཚིང་གི་དབུས་སུ་གཞུག་གོ་ཞེས་བྱ་བ་ནི་བརྒྱ་ལ༌[^4179]སྲོག་ཆགས་དང་བཅས་ཤིང་བསྲེགས་ན་སྲོག་ཆགས་མང་པོ་དག་འཆི་བ་ལྟ་ནའོ། །

[Block 4077]
སྤྱོད་ལམ་གང་གིས་གཞག་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གློ་གཡས་པས་བསྙལ༌[^4180]ཏེ་མགོ་བྱང་ཕྱོགས་སུ་བསྟན་ཏོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4078]
སྔས་སུ་རྩྭའི་ཆུན་པོ་གཞུག་གོ། །

[Block 4079]
རྩྭ་དག་གམ་ལོ་མ་དག་གིས་གཡོགས་སོ། །

[Block 4080]
ཆོས་མཉན་པ་དང་ཡོན་བཤད་པ་དག་བྱའོ། །

[Block 4081]
རེག་པ་དག་གིས་གོས་དང་བཅས་ཏེ་ཁྲུས་བྱའོ། །

[Block 4082]
གཞན་དག་གིས་ནི་རྐང་ལག་བཀྲུའོ་ཞེས་བྱ་བ་ནི༌[^4181]རོ་ལ་མ་རེག་པ་དག་གིས་སོ། །

[Block 4083]
མཆོད་རྟེན་ལ་ཕྱག་བྱས་ཏེ་འཇུག་པར་བྱའོ། །

[Block 4084]
མཆོད་རྟེན་ནི་རྣམ་པ་གཉིས་ཏེ། གཙང་ཁང་ཅན་ཉིད་དང་། ཀ་བ་ལྟ་བུ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། འདི་ནི་མ་མོ་དག་ལས་སོ། །

[Block 4085]
དེ་རབ་ཏུ་བྱུང་བ་རྣམས་ལ་འོས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་དེའོ། །

[Block 4086]
ཅི་ཐམས་ཅད་ལའམ་ཞེ་ན་དེའི་ཕྱིར། གལ་ཏེ་དགེ་བ་ཡིན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་བྱུང་བ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4087]
སོ་སོའི་སྐྱེ་བོ་དགེ་བ་ཡིན་ན་མཆོད་རྟེན་དབུ་མེད་པ་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4088]
གང་ཞིག་འཕགས་པ་ལས་གཞན་པ་དགེ་བ་ཉིད་སྒྲུབ་པ་རྣམས་ལ་དེའི་ཕྱིར་མདོ་འདི་ཡིན་ནོ། །

[Block 4089]
སངས་རྒྱས་རྣམས་ཀྱི་ནི་རྣམ་པ་ཐམས་ཅད་དོ་ཞེས་བྱ་བ་སྨོས་ན། རྣམ་པ་དེ་དག་གང་ཡིན་སྙམ་ན་དེ་ལ༌[^4182]བརྗོད་པར་བྱ་སྟེ་དེའི་ཕྱིར། རྣམ་པ་ནི༌[^4183]བང་རིམ་བཞི་དང་འདབ་མ་དང་པུ་ཤུ་དང་སྲོག་ཤིང་དང་། གདུགས་བཅུ་གསུམ་དང་ཆར་ཁབ༌[^4184]དག་གོ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་གྱི་རྣམ་པ་ཐམས་ཅད་རྫོགས་པའོ། །

[Block 4090]
རང་སངས་རྒྱས་རྣམས་ཀྱི་ནི༌[^4185]ཆར་ཁབ༌[^4186]མེད་པའོ་ཞེས་བྱ་བ་ནི་རྣམ་པ་དེ་དག་ལས་ཆར་ཁབ༌[^4187]འབའ་ཞིག་མེད་པ་དང༌[^4188]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4091]
དེ་ཡང་བསེ་རུ་ལྟ་བུའི་ཕྱིར་གསུངས་པ་ཡིན་གྱི་ཚོགས་ན་སྤྱོད་པ་ནི་དགྲ་བཅོམ་པའི་ཆོ་གའི་རྣམ་པ་ལྟ་བུས་རིག་པར་བྱའོ། །

[Block 4092]
འདིར་གཞུང་ནི་རང་སངས་རྒྱས་ཀྱི༌[^4189]ཆར་ཁབ༌[^4190]མེད་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4093]
ཉན་ཐོས་རྣམས་ཀྱི༌[^4191]ནི་འབྲས་བུའི་ཚད་དག་གིས་དེའི་གདུགས་གཅིག་ལྷག་པའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་དགྲ་བཅོམ་པའི་ནི་གདུགས་ལྔའོ། །

[Block 4094]
ཕྱིར་མི་འོང་བའི་ནི་གདུགས་བཞིའོ། །

[Block 4095]
ལན་ཅིག་ཕྱིར་འོང་བའི་ནི་གདུགས་གསུམ་མོ། །

[Block 4096]
རྒྱུན་དུ་ཞུགས་པའི་ནི་གདུགས་གཉིས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4097]
དེའི་ཞེས་བྱ་བ་ནི་གདུགས་དེའི་འོ། །

[Block 4098]
མཆོད་རྟེན༌[^4192]ཡོངས་སུ་རྫོགས་པར་གྱུར་པའི་གདུགས་ནི་ལྷག་མ་རྣམས་ལས་བྱེ་བྲག་ཏུ་གྱུར་པ་ཉིད་དོ་ཞེས་བྱ་བའི་དགོངས་པ་ཡང༌[^4193]མཐོང་བ་ཡིན་ནོ། །

[Block 4099]
འདིར་འབྲས་བུ་རྣམས་ནི་རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པ༌[^4194]རྣམས་སོ། །

[Block 4100]
གང་གི༌[^4195]འབྲས་བུ་རྣམས་ཇི་སྙེད་ཐོབ་པ་དེ༌[^4196]སྙེད་ལས་གདུགས་རེ་རེས་ལྷག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
