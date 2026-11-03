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
དུལ་བ་ལ་སོགས་པ་ཞེས་བྱ་བ་ལ། སོགས་པ་སྨོས་པས་ནི་ཚུལ་ཁྲིམས་དང་། སྦྱིན་པ་དང་། བཟོད་པ་དང་། བརྩོན་འགྲུས་ཏེ་བསོད་ནམས་ཀྱི་ཚོགས་ཡོངས་སུ་གཟུང༌[^2671]ངོ་། །ཡོན་ཏན་བཟང་ཞིང་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་གྱི་ལམ་ལ་རྗེས་སུ་དགའ་བ་སྟེ། དེའི་ཡོན་ཏན་ལ་རྗེས་སུ་དགའ་བར་འབངས་ཀྱང་བསླབས༌[^2672]པའོ། །

[Block 4132]
དེས་ན་རྒྱལ་པོ་ཅི་ཞིག་ཏུ་འགྱུར་ཞེ་ན། དེའི་ཕན་ཡོན་འབངས་ལ་ཕན་གདགས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4133]
འབངས་ལ་ཕན་གདགས་པ་ནི་རྒྱལ་པོའི་དོན་གྱི་མཆོག་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། ཚེ་རབས་གཉི་གའི་བདེ་བའི་ཕྱིར་རོ། །

[Block 4134]
འཇིག་རྟེན་འདིར་ནི་གྲགས་པ་ལ་སོགས་པ་འཐོབ་པར་འགྱུར་རོ། །

[Block 4135]
འཇིག་རྟེན་ཕ་རོལ་དུ་ནི་བདེ་འགྲོར༌[^2673]འགྲོ་བས་ཕན་པའོ། །

[Block 4136]
འདི་ཡིན་ཞེས་བྱ་བ་ནི་ཆོས་ལ་དགའ་བ་སྟེ། རྒྱལ་པོའི་ཆོས་ལ་དགའ་བ་དེས་སྐྱེ་དགུ་ལ་ཕན་པར་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། རྒྱལ་པོའི་རྗེས་སུ་འབངས་ཀྱང་སྤྱོད་པའི་ཕྱིར་རོ། །

[Block 4137]
དེ་བས་ཆོས་བཞིན་ས་ལ་ཞེས་བྱ་བ་ནི་སྐྱེ་དགུ་ལ་ཕན་པ་དེས་ནི་འཇིག་རྟེན་གཉི་ག་ལ་ཕན་པའི་ཕྱིར་རོ། །

[Block 4138]
གནས་པར་བྱེད་པ་ཡིན་པས་གནས་པར་གྱུར་པ་སྟེ། དེ་བས་ན་འདི་དག་གིས་ནི་དེའི་དྲུང་ན་གནས་པའི་ཕན་ཡོན་བསྟན་ཏོ། །

[Block 4139]
བཀུར་སྟི་དང་ཚིག་སྙན་པ་ནི་བཀུར་སྟི་དང་ཚིག་སྙན་པ་དག་གོ། །

[Block 4140]
དེའི་སྦྱོར་བ་ནི་བཀུར་སྟི་དང་ཚིག་སྙན་པའི་སྦྱོར་བའོ། །

[Block 4141]
རལ་གྲི་དང་དྲི་མ་མེད་པ་ནི་རལ་གྲི་དྲི་མ་མེད་པའོ། །

[Block 4142]
དེ་ལྟར་སྔོ་བ་ནི་རལ་གྲི་དྲི་མ་མེད་པ་ལྟར་སྔོ་བའོ། །

[Block 4143]
ཡང་ན་རལ་གྲི་དྲི་མ་མེད་པས་སྔོ་བ་ནི་རལ་གྲི་དྲི་མ་མེད་པ་ལྟར་སྔོ་བའོ། །

[Block 4144]
སྟོན་ཀ་མཛེས་པ་ནི་སྟོན་གྱི་མཛེས་པའོ། །

[Block 4145]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་ངང་པའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 4146 [HEADING]]
## བྱང་ཆུབ་ཆེན་པོའི་སྐྱེས་པའི་རབས། ^25-0

[Block 4147]
སྐྱེས་བུ་དམ་པ་རྣམས་ནི་རིམ་གྲོ་མ་བྱས་ཀྱང་སྙིང་བརྩེ་བ་ལྷོད་པར་མི་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། བཟོད་པ་ལ་གོམས་པའི་ཕྱིར་རོ། །

[Block 4148]
ཕན་བཏགས་པ་ལ་ཡང་སྙིང་བརྩེ་བ་ལྷོད་པར་མི་འགྱུར་ཏེ། དྲིན་ཏུ་གཟོ་བའི་ཕྱིར་རོ། །

[Block 4149]
འདིར་དེ་གཉིས་ཀྱང་ཇི་ལྟར་རིགས་པ་བཞིན་དུ་སྦྱར་རོ། །

[Block 4150]
རིག་པའི་གནས་རྣམས་ཀྱི་གོ་རིམས་གང་ཡིན་པ་དེ་ནི་རིག་པའི་གནས་རྣམས་ཀྱི་གོ་རིམས་ཏེ། རྒྱུན་མི་འཆད་པར་ཕ་རོལ་ཏུ་འགྲོ་བ་ཡིན་པའི་ཕྱིར་རིག་པའི༌[^2674]གནས་ཀྱི་རིམ་པའོ། །

[Block 4151]
མཁས་པར་བྱ་བ་རྣམས་ལ་དེ་མཁས་པར༌[^2675]བྱས་པ་སྟེ། སྒྱུ་རྩལ་རྣམས་ལ་ནི༌[^2676]མཁས་པར་བྱ་བ་ཉི་ཚེར་ཟད་ཀྱི། ལས་ཀྱིས༌[^2677]སྒྲུབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 4152]
རབ་ཏུ་བྱུང་ནས་ཀྱང་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བ་ལ་བརྟེན་པ་ཡིན་པས་རབ་ཏུ་བྱུང་བའོ། །

[Block 4153]
རབ་ཏུ་བྱུང་བ་དང་འཇིག་རྟེན་ལ་ཕན་འདོགས་པ་གཉིས་ཀྱིས་ནི་བདག་དང་གཞན་ལ་ཕན་པ་སྒྲུབ་པའི་ཡོན་ཏན་དང་མཐུན་པ་ཉིད་དེ། དེས་ཆོས་ཀྱི་གཙུག་ལག་ལྷག་མ་རྣམས་འཛིན་པའོ། །

[Block 4154]
སློབ་དཔོན་གྱི་གོ་འཕང་ནི་གཞན་གྱིས་ཉེ་བར་འཚོ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4155]
དེ་བསོད་ནམས་དང་ལྡན་ཞིང་ཞེས་བྱ་བ་འདིས་ནི་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རབ་ཏུ་བསྒོམ་པ་ཉིད་དུ་སྟོན་ཏེ། འདི་ལྟར་སྦྱིན་པས་ནི་གཟུགས་བཟང་བ་ལ་སོགས་པའི་ཡོན་ཏན་དུ་འགྱུར་རོ། །

[Block 4156]
ཚུལ་ཁྲིམས་ཀྱིས་ནི་མངོན་དུ་བསྡུ་བ་ལ་སོགས་པའི་བཀུར་སྟིའི་བདེ་བ་འབྱུང་ངོ་། །བཟོད་པས་ནི་སྐྱེ་བོ་མང་པོའི་འཁོར་སྙིང་ཉེ་བ་ཉིད་དུ་འགྱུར་རོ། །ཤེས་རྒྱ་ཆེ་བས་ཞེས་བྱ་བ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་ཡོངས་སུ་བསགས་པའི་ཕྱིར་རོ། །

[Block 4157]
འདི་གཉིས་ཀྱིས་ནི་རྒྱུ་དང་འབྲས་བུ་བསྟན་ཏོ། །

[Block 4158]
འཇིག་རྟེན་གྱི་སྤྱོད་ཚུལ་ལ་མཁས་པ་དང་ཡོན་ཏན་དང་ལྡན་པས༌[^2678]ཞེས་བྱ་བ༌[^2679]ནི་བདག་དང་གཞན་ལ་ཕན་པའི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པར་བསྟན་ཏོ། །

[Block 4159]
ཡང་ན༌[^2680]གང་གིས་སྣ་ཚོགས་པ་ཉིད་ཀྱི་རྣམ་པའི་རྒྱུ་བསྟན་ཏེ། བསོད་ནམས་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 4160]
བསོད་ནམས་ཆེན་པོ་དང་ལྡན་པ་ལ་ནི་རྒྱལ་པོ་དང་རྒྱལ་པོའི་བློན་པོ་རྣམས་བཀུར་སྟི་བྱེད་པ་ཡིན་ནོ། །ཤེས་པ་རྒྱ་ཆེ་བའི་ཕྱིར་ནི་མཁས་པ་རྣམས་ཀྱིས་བཀུར་སྟི་བྱ་བ་ཡིན་ནོ། །

[Block 4161]
འཇིག་རྟེན་གྱི་སྤྱོད་ཚུལ་ལ་མཁས་པས་ནི་བྲམ་ཟེ་དང་། ཁྱིམ་པ་རྣམས་ཀྱིས་བཀུར་སྟི་བྱ་བ་ཡིན་ནོ། །

[Block 4162]
ནན་ཏན་ཆེ་བའི་ཡོན་ཏན་དང་ལྡན་པས་ནི་གཞན་མུ་སྟེགས་ཅན་རྣམས་དང་རབ་ཏུ་བྱུང་བ་རྣམས་ཀྱིས་བཀུར་སྟི་བྱ་བ་ཡིན་ནོ། །

[Block 4163]
ལས་སུ་དྲན་པར་བྱེད་པ་ཡིན་ཏེ། ཡིད་ཀྱི་ལས་ཀྱིས་སོ། །

[Block 4164]
ཡོན་ཏན་ཞེས་བྱ་བ་ནི་བློ་ཁྱད་པར་དུ་འཕགས་པ་ལས་གྱུར་པའི་ཡོན་ཏན་ནོ། །

[Block 4165]
བསོད་ནམས་ཉིད་གཞི་ཡིན་པས་བསོད་ནམས་གཞིའོ། །

[Block 4166]
བསོད་ནམས་ཀྱི་གཞི་ལས་ཐོབ་ཅིང་འབར་བ་གང་ཡིན་པ་དེ་ནི་བསོད་ནམས་ཀྱི་གཞི་ལས་འབར་བའོ། །

[Block 4167]
བསོད་ནམས་ཞེས་སྨོས་པས་ནི་གང་སྔར་བསྟན་པའི་བསོད་ནམས་དང་ལྡན་པའི་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་ཏོ། །

[Block 4168]
ནན་ཏན་སྒྲུབ་པའི་བྱིན་གྱིས་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་བདག་གི་སྒྲུབ་པ་སྟེ། ནན་ཏན་ཆེ་བའི་ཡོན་ཏན་ཞེས་བྱ་བ་དང་། གཞན་གྱི་སྒྲུབ་པ་སྟེ་འཇིག་རྟེན་གྱི་ཚུལ་ལ་མཁས་པ་ཞེས་བྱ་བ་དེ་གཉི་ག་ནི་ནན་ཏན༌[^2681]སྒྲུབ་པའི་བྱིན་གྱིས་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4169]
ཡང་ན་ཡོན་ཏན་ཞེས་སྨོས་པས་ནི་འཇིག་རྟེན་གྱི་སྤྱོད་ཡུལ་ལ་མཁས་པ་ཞེས་བྱ་བ་དེ་གཟུང༌[^2682]ངོ་། །ཡོན་ཏན་སྒྲུབ་པའི་བྱིན་གྱིས་ཞེས་བྱ་བ༌[^2683]ནི་སྔར་བསྟན་པའི་ནན་ཏན་ཆེ་བ་ཡིན་པར་བསྟན༌[^2684]ཏོ། །

[Block 4170]
དགྲ་ཡང་རང་གི་གྲགས་པ་བསྲུང་བའི༌[^2685]ཕྱིར། །ཞེས་བྱ་བ་ནི་ཡོན་ཏན་དང་ལྡན་པ་ལ་བསྙེན་བཀུར་བྱེད་པས་སོ། །
--- END BLOCKS ---
