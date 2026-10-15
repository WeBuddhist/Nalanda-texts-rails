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
[Block 4481]
གཞན་ལ་ནི་ལྟུང་བ་མེད་ཅེས་བྱ་བ། ལྟུང་བའི་ཡུལ་ཉིད་ཀྱི་ཕྱིར་འདིའི་ཆོ་ག་བསྒྲུབ་པའོ། །

[Block 4482]
ཇི་ལྟ་བུ་ཞིག་ཡོད་པ་ཉིད་ན་ཞེ་ན་དེའི་ཕྱིར། ལྷན་པ་བཞི་མན་ཆད་ནས་དེ་དག་རུང་ཞིང་། ཡོངས་སུ་སྤྱད་བཟོད་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྷན་པ་བཞི་མན་ཆད་ནས་ནུས་པ་ཉིད་ཀྱིས་ལྷན་པ་འདི་ཙམ་རྣམས་ཀྱིས་དེ་ནས་བརྩམས་ཏེ། འདི་ལྟ་བུ་ཇི་སྲིད་ལྷུང་བཟེད་ཡོངས་སུ་ལོངས་སྤྱད་པར་ནུས་པ་དེའི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4483]
ཅུང་ཟད་སྐྱོན་མེད་པ་ཡང་ཤིན་ཏུ་སྙི་བ་ཉིད་ཀྱི་ཕྱིར་དང་། འཇམ་པའི་ས་གཞི་རང་བཞིན་ཉིད་ཀྱི་ཕྱིར་ཡོངས་སུ་ལོངས་སྤྱད་པར་བཟོད་པར་འགྱུར་བ་དེ་བཟློག་པའི་དོན་དུ་ཡོངས་སུ་སྤྱད་པར་བཟོད་པའོ་ཞེས་བྱ་བའི་བྱེ་བྲག་གོ། །

[Block 4484]
དེ་ཡོད་པ་ཉིད་ན་ཇི་ཞིག་ལྷག་པར་སྤྱད་ན་ཁ་ན་མ་ཐོ་བ་ཅི་འདྲ་བ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཁྱིམ་པ་ཉེ་དུ་མ་ཡིན་པ་ལས་བསླངས་པས་ཡོངས་སུ་བཙལ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱིམ་པ་ཉེ་དུ་མ་ཡིན་པ་ལས་བསླངས་ཏེ་ཡོངས་སུ་བཙལ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4485]
དེ་གཉིས་ནི་འོག་མ་གཉིས་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིའི་འོག་མ་བསླབ་པའི་གཞི་གཉིས་པོ་གང་དག་ཡིན་པ་དེ་དག་ལ་ཡང་ཉེ་དུ་མ་ཡིན་པ་དང་། ཁྱིམ་པ་ཉིད་ཅེས་བྱ་བ་འདི་གཉིས་རིག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4486]
ཐ་ག་པ་དང་། སྦྱིན་པ་དང་། གཞན་དག་ལའོ་ཞེས་བྱ་བ་ནི་ཐ་ག་པ་དང་། སྦྱིན་པ་དང་།[^3049] གཞན་དང་དེ་རྣམས་སོ། །

[Block 4487]
དེ་དག་ཉེ་དུ་མ་ཡིན་པ་དང་། ཁྱིམ་པ་མ་ཡིན་པ་རྣམས་ལ༌[^3050]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4488]
གཞན་གྱིས་བརྗོད་པའི་དོན་ལ་གཞན་ཞེས་བྱ་བའི་སྒྲས་དེ་བཟུང་བར་རིག་པར་བྱའོ། །

[Block 4489]
ཉེ་དུ་མ་ཡིན་པ་ལྟར་ཉེ་དུ་ལས་ནི་སྐྱེད༌[^3051]དང་ལྷུང་བཟེད་གཉིས་མ་གཏོགས་པ་ལ་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ལ། ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་སྐྱོན་མེད་པའོ། །

[Block 4490]
ཉེ་དུ་མ་ཡིན་པ་ལྟར་ཞེས་བྱ་བ་ནི་འདི་ནི་རྒྱུ་མཚན་གྱི་བདུན་པ་སྟེ། ཉེ་དུ་མ་ཡིན་པའི་རྒྱུ་མཚན་ཅན་གྱི་ཉེས་པ་བསོད་པ་སློང་བ་ལ་སོགས་པ་གང་ཡིན་པ་ཉེས་པ་དེ་ལ་ཉེ་དུའི་རྒྱུ་མཚན་ཉིད་ཀྱིས༌[^3052]ཡང་དག་པར་བརྟེན་པ་ལ་མེད་པའོ། །

[Block 4491]
འཕེལ་བ་དོར་ནས་འཕེལ་བ་བརྟེན་པ་ཉིད་ལ་ནི་འདི་ལྟ་སྟེ། མངོན་མཚན་ཅན༌[^3053]གྱི་སྤྱོད་པ་དང་ཉོ་ཚོང་གི་སྤྱོད་པ་དག་གིས་རྙེད་པ་གྲུབ་པ་དང་ལྷུང་བཟེད་ལ་ཡང་འདི་དག་ལ་ན་སྨད་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ།[^3054] །གང་ཞིག་ཉེ་དུས་བོས་པ་ལ་ལྟུང་བ་མེད་པའི་ཚིག་གོ། །

[Block 4492]
འདིར་གཞུང་ནི་འདི་ཡིན་ཏེ་གཅེར་བུ་པ་ལ་སྦྱིན་ན་ཉེ་དུ་ཡིན་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དང་། ཞུ་བ་ལས་ཀྱང་ཉེ་དུ་ལས་ཟས་བསོད་པ་བསླངས་ཏེ་རང་ཟ་བ་དང་གཅེར་བུ་པ་ལ་སྦྱིན་ཞིང་སྡིག་པ་ཅན་གྱི་ལྟ་བའི་རྣམ་པ་དང་བྲལ་བར་འདོད་པས་སྦྱིན་པར་བྱེད་ན་ལྟུང་བ་མེད་དོ། །

[Block 4493]
ཉེ་དུ་ཡིན་ན་ཡང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ༌[^3055]ཡིན་ནོ། །

[Block 4494]
ཞར་ལས་བྱུང་བ་བསྟན་ནས་གང་ཞིག་གང་གསུངས་པ། ཁྱིམ་པ་ཉེ་དུ་མ་ཡིན་པ་ལས་བསླངས་པས་ཡོངས་སུ་བཙལ་ནའོ་ཞེས་གང་སྨྲས་པའི་ལྟུང་བ་དེའི་སྐབས་སུ་གཏོགས་པ་བསྟན་པའི་ཕྱིར་འདིར་འདི་བརྗོད་པར་བྱ་སྟེ། ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་འཚོལ་བ་ཙམ་ལས་ཉེས་བྱས་སུ་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4495]
དེ་ལས་གྲུ་པ་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་ལ། དེ་ལས་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་ལས་བླངས་པ་བཙལ་ན་ཐོབ་པ་ལ་དངོས་གཞིའི་ཁ་ན་མ་ཐོ་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4496]
མེད་པ་ཉིད་ལ་ཡོད་པའི་བློ་ཅན་ལ་ནི་ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་བདག་ལ་ལྷུང་བཟེད་གཞན་ཡོད་དོ་སྙམ་པའི་བློ་གང་ཡིན་པ་འདི་ཡོད་ཅིང་དེའི་ཚེ་གལ་ཏེ་འཚོལ༌[^3056]བར་བྱེད་ན་རྙེད་པར་འགྱུར་བ་དང༌[^3057]ཡོད་པར༌[^3058]འགྱུར་བའི་ལྷུང་བཟེད་དག་གི༌[^3059]ནང་ནས་གཞན་དག་ལ་མེད་པ་ཉིད་ལ་ནི་མེད་པ་སྟེ། དབྱེ་བ་ལ་སོགས་པས་འགྱུར་ན་དེ་ལ་ལྷུང་བ༌[^3060]ལ་ན་སྨད་པ་ཉིད་དེ༌[^3061]དངོས་གཞིའི་ལྷུང་བ༌[^3062]ཉིད་ནི་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4497]
འདིར་གཞུང་ནི་དགེ་སློང་འགའ་ཞིག་ཡོད་དེ་ལྷུང་བཟེད་མཆིས་བཞིན་དུ་ལྷུང་བཟེད་གཞན་ལ་བསླངས་པར་གྱུར་ལ་ལྟུང་བར་མི་འགྱུར་བ་འགའ་ཞིག་མཆིས་སམ། བཀའ་སྩལ་པ་ཡོད་དེ། གལ་ཏེ་བསླངས་པ་དག་སྔ་ཕྱི་མེད་པར་ལྷུང་བཟེད་ཆག་པར༌[^3063]གྱུར་ན་ལྷུང་བ༌[^3064]མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4498]
འདིར་སྤང་བ་མེད་པ་ལ་དགོངས་ནས་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་པས་སྦྱོར་བ་མེད་པའི་དགོངས་པ་ཅན་ནི་མ་ཡིན་ནོ། །

[Block 4499]
འདིར་ན་སྨད་པའི་ཚིག་གིས་དངོས་གཞིའི་ཉེས་བྱས་སོ། །

[Block 4500]
སྦྱོར་བ་ལ༌[^3065]ནི་འདི་མ་ཆོག་པ་ཞེས་བྱ་བ་འདི་བསྟན་པའོ། །

[Block 4501]
རང་གི་ཡོ་བྱད་དག་གིས་སོ། །

[Block 4502]
དེ་དག་ཡོད་པ་ཉིད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡོ་བྱད་རྣམས་ལ་ན་སྨད་པ་ཉིད་ཅེས་བྱ་བར་སྦྱར་རོ། །

[Block 4503]
འདིར་གཉིས་ཀའི་ཡོ་བྱད་རྣམས་ཀྱིས་ལྷུང་བཟེད་གཞན་ཚོལ་བར་བྱེད་ན་ཉེས་བྱས་ཏེ། ཡོད་ཅིང་བདོག་པ་ཉིད་ན་ལྷུང་བཟེད་ཚོལ་བར་བྱེད་ན་ཉེས་བྱས་ཞེས་བྱ་བའོ། །

[Block 4504]
འདིར་ཡང་དངོས་གཞིའི་སླད་དུ་ལྟུང་བ་མེད་པར་བསྟན་ཏེ་སྦྱོར་བ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4505]
རྗེས་སུ་གནང་བའི་སློང་བ་གཞན་ལ་ཡང་རང་གི་རིན་ཐང་ཡོད་ན་འཇུག་པ་ལ་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་འདི་ལ་རྟོགས་པར་བྱའོ། །

[Block 4506]
བཟང་པོ་འདོད་པས་བརྗེ་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི། ལྷུང་བཟེད་བཟང་པོ་འདོད་པ་ལ་ནི་བཟང་པོ་འདོད་པ་སྟེ། ཚོལ་བར་བྱེད་པ་སྔོན་དུ་འགྲོ་བ་ཅན་གྱི་བཟང་པོ་དེའི་འདུན་པས་བརྗེ་བར་བྱེད་ན་ལྟུང་བ་ན་སྨད་པར་ཤེས་པར་བྱའོ། །

[Block 4507]
བརྗེ་བས་ལེན་ན༌[^3066]ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་གང་ཞིག་གསུངས་པ་ནི་བཟང་བ་འདོད་པ་མེད་པར་བརྗེ་བའི་དབང་དུ་བྱས་ཏེ་དེ་རིག་པར་བྱའོ། །

[Block 4508]
ཁྱིམ་པ་ཉེ་དུ་མ་ཡིན་པ་ལས་བསླངས་ཏེ་ཐོབ་ན་དངོས་གཞིའོ། །

[Block 4509]
མ་བསླངས་པར་བཙལ་ན་སྤངས་ནས་བརྗེ་བ་ཉེ་དུ་མ་ཡིན་པའི་ཁྱིམ་པ་འམ་གཞན་ལ་སྤངས་ཏེ་ཐོབ་པར་གྱུར་པ་ལ་བཟང་པོ་འདོད་པས་ཀྱང་བརྗེ་བ་ཐམས་ཅད་དུ་སྦྱོར་བ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 4510]
བཙལ་བ་མེད་པར་བརྗེ་བས་བཟང་པོ་འདོད་པ་ཉིད་མེད་པར་གྲུབ་ན་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་འདི་འདིར་གནས་པར་རིག་པར་བྱའོ། །

[Block 4511]
ཞག་བཅུ་ལས་འདའ་བར་བྱེད་པ་ལ་སྤང་བའི་ལྟུང་བྱེད་གཞན་དུ་ཤེས་པར་བྱའོ། །

[Block 4512]
འདི་ནི་དགེ་འདུན་ལ་སྤང་ངོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ལྷག་པ་འདི་ནི་ཇི་ལྟར་སྤང་བ་གཞན་གང་ཟག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4513]
ཅི་ལྷུང་བཟེད་ཐམས་ཅད་དགེ་འདུན་ལ་སྤང་བར་བྱ་བ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ་དེའི་ཕྱིར་དུ་མ་ཉིད་ཡིན་ན་མཆོག་ཏུ་འདོད་པ་གཅིག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྷུང་བཟེད་ལྷག་མ་དུ་མ་ཉིད་དུ༌[^3067]ཡིན་ན་མཆོག་ཏུ་འདོད་པ་གཅིག་དགེ་འདུན་ལ་སྤང་བར་བྱའོ། །

[Block 4514]
འོ་ན་ལྷག་མ་གཞན་སྤང་བར་བྱ་བ་འམ་མ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གཞན་ནི་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་སྤང་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། [^3068]གང་དུ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རབ་ཏུ་བྱུང་བ་འདི་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4515]
ཞུ་བ་ལས་ལྷུང་བཟེད་ལྷག་མ་རྣམས་ནི་དགེ་སློང་རྣམས་ལ་བགོ་བར༌[^3069]བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4516]
དགེ་སློང་ཞེས་སྨོས་པ་ནི་མཚོན་པ་ཙམ་དུ་ཟད་དེ་ཆོས་འདི་ལ་རབ་ཏུ་བྱུང་བ་ཐམས་ཅད་ཀྱང་སྤྱིར་བསྡུ་བའོ།[^3070] །དེ་ལ་ཐ་ཆད་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྤངས་པ་དེ་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4517]
གཞན་དུ་ན་ཡང་ལྷུང་བཟེད་ཐ་ཆད་གང་ཡིན་པ་དེ་འདི་ལ་སྦྱིན་པར་བྱའོ། །

[Block 4518]
འོན་ཏེ་དེ་ཉིད་དགེ་འདུན་དེ་ལ་ཐ་ཆད་འབྱུང་བར་འགྱུར་ན་དེ་ཉིད་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་དོ། །

[Block 4519]
བྲིམ་པས་བསྙིགས་པར༌[^3071]བྱའོ་ཞེས་བྱ་བ་ནི་ཐ་ཆད་དེ་དགེ་འདུན་དེ་ལས་སོ། །

[Block 4520]
བྱེད་པ་པོ་ཇི་ལྟ་བུས་བྲིམ་པས་དགེ་འདུན་ལས་ཐ་ཆད་དེ་བསྙིགས་པར༌[^3072]བྱ་ཞེ་ན་དེའི་ཕྱིར་བསྐོས་པས༌[^3073]སོ། །
--- END BLOCKS ---
