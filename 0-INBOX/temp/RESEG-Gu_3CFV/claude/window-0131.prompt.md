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
[Block 4586]
དེ་ནི་མི་རིགས་ཏེ་ནད་པས་བསྟེན་པར་བྱའི་གཞན་གྱིས་ནི་བཟའ་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4587]
སྒོ་ཁང་དང་ཐེམ་སྐས་ཀྱི་ལྐོག་དང་། ཁྱམས་དང་དཔོང༌[^3195]ས་དང་བཀད་ས་དང་བསྲོ་ཁང་གི་ར་བ་དག་ནི་བསྐོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ནི་མི་ཆོག་པ་ལ་བསྐོ་བར་བྱ། ཤེས་པར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4588]
འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 4589]
དགེ་སློང་དག་གནས་དྲུག་པོ་འདི་དག་ནི་བསྒོ་བར༌[^3196]མི་བྱ་བ་དག་སྟེ། སྒོ་ཁང་ཐམས་ཅད་དང་། ཐེམ་སྐས་ཀྱི་ལྐོག་དང་ཁྱམས་དང་དཔོང༌[^3197]སའི་ར་བ་དང་བཀད་སའི་ར་བ་དང་བསྲོ་ཁང༌[^3198]གི་ར་བ་དག་སྟེ། སྐོ་བར༌[^3199]བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4590]
མཚན་མོ་གནས་མལ་མི་བསྐོའོ་ཞེས་བྱ་བ་ནི་བསྐོ་བར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4591]
ཁྲི་ལ་སོགས་པ་ལ་ཡང་ཆོ་ག་འདི་ཉིད་ཡིན་ཏེ། གནས་ཁང་ཉིད་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ཉིད་ཀྱི་ཕྱིར་གནས་མལ་ཞེས་སྨོས་སོ། །

[Block 4592]
གནས་ཁང་གི༌[^3200]གཞིར་གྱུར་པའི་གནས་པའི་སྒྲ་འདི་གྲགས་པ་སྟེ། དེའི་ཕྱིར་ཤིང་ལྗོན་པའི་རྩ་བ་ལ་སོགས་པ་ལ་འདིས་ཆོ་ག་འདི་ལ་བྱས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 4593]
ནད་པ་འདུག་པའི་གནས་ཁང་གཞན་ལ་མི་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་གནས་ཁང་ཞེས་སྨོས་པས་ནི་ཁྲི་ལ་སོགས་པ་བཟློག་པའི་ཕྱིར་བསྟན་ཏོ། །

[Block 4594]
དེ་ཉིད་ཐོབ་པ་མེད་ན་མི་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཉིད་ཅེས་བྱ་བ་ནི་དེ་ལྷག་པར་གནས་པ་ཉིད་ལ་ཐོབ་པ་ལ་ཇི་ལྟར་རྒན་རིམས་སུ་མ་བྱས་པར་ནད་པ་ལ་གནས་ཁང༌[^3201]སྦྱིན་པར་མི་བྱའོ། །

[Block 4595]
འདིར་གཞུང་ནི། དགེ་སློང་ནད་པའི་གནས་ཁང་གཞན་ལ་བསྐོ་བར་མི་བྱའོ། །

[Block 4596]
བསྐོ་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ། །

[Block 4597]
འདིར་ནད་པ་ཞེས་བྱ་བ་ནི་སྦྱོར་མི་བཟོད་པ་ཡིན་པར་ཤེས་པར་བྱ་སྟེ། དེ་ལྟ་བས་ན་ནད་པ་སྦྱོར་མི་བཟོད་པ་ཞེས་བྱ་བ་དེ་ལས་རྟོགས་པར་བྱའོ། །

[Block 4598]
དེ་དང་དེའི་གཡོག་ལས་བྱེད་དུ་མི་གཞུག་གོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ༌[^3202]ནི་ནད་པ་དེའོ། །

[Block 4599]
དེའི་ཞེས་བྱ་བ་དེ༌[^3203]ནི་ནད་པ་དེའིའོ། །

[Block 4600]
མཛེ་ཅན་གྱིས་དགེ་འདུན་གྱི་གནས་མལ་ལ་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གོས་ཀྱི་གཞི་ལས་དེ་དང་པོར་བྱ་སྟེ། ནད་གཡོག་སྦྱིན་པས་འདི་ལ་སྙིང་བརྩེ་བར་བྱའོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 4601]
དེ་ལ་གནས་དབེན་པ་སྦྱིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་མཛེ་ཅན་ལའོ། །

[Block 4602]
འདིར་གནས་དབེན་པ་ཞེས་བྱ་བ་ནི་གཞན་དག་གིས་འདོད་པའོ། །

[Block 4603]
དེ་ལས་ཐ་དད་པར་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 4604]
དབེན་པར་དེ་ཉིད་ཀྱིས་གང་ཞིག་སྦ་བ་ཉིད་དེ་འདིར་རིགས་པ་ཡིན་ནོ། །

[Block 4605]
དགེ་འདུན་གྱིས༌[^3204]བསྟེན་པར་བྱ་བ་དང་བཅས་པ་ཐ་ན་ཁྱམས་དང་། ཁྱམས་གྲུ་བཞི་དང་། སྒོ་ཁང་དང་། བང་རིམ་དང་། འཆག་ས་དང་། ཤིང་དྲུང་གི་གནས་དེར་ཡང་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། བསྟེན་པ་ཞེས་བྱ་བ་ནི་བསྟེན་པ་ཡོད་པར་གྱུར་པ་ལ་དུས་དུས་སུ་བསྟེན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་གིས་ཡིན་ཞེ་ན། དགེ་འདུན་གྱིས་ཞེས་བྱ་བར་སྦྱར་ཏེ། རབ་ཏུ་བྱུང་བ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 4606]
གནས་པས་ཀུན་ནས་ལོངས་སྤྱོད་པ་ནི་བསྟན་པ་ཞེས་བརྗོད་པ་ཡིན་ནོ། །

[Block 4607]
བཤང་བ་དང་གཅི་བའི་སྐྱབས་གཉིས་སུ་འཇུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་དག་གིས་ཞེས་བྱ་བ་འཇུག་གོ། །

[Block 4608]
དེ་ལ༌[^3205]གཡོག་བསྐོ་བས་སྙིང་བརྩེ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ནད་ཡུན་རིང་ཞིང་ཆེ་བ་ཡིན་པའི་ཕྱིར་ནད་གཡོག་དེ་མེད་ན་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ། ཆོ་ག་འདི་ལ་འདིར་མ་སྦྱར་བ་གང་ཡིན་པའི་བརྡ་དེ་ལ་དེའི་དོགས་པ་བསལ་བའི་དོན་དུའོ། །

[Block 4609]
དུས་ཐམས་ཅད་དུ་དགོན་པ་པ་དག་ལ་ལྷུང་བཟེད་དང་ཆོས་གོས་གཞག་པའི་ཕྱིར་གནས་ཁང་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། དགེ་སློང་དགོན་པ་པ་དག་དང་གཙུག་ལག་ཁང་དུ་ལྷགས་ཏེ། གནས་ཁང་དག་རྙེད་པ་ན་དགེ་སློང་དག་ལས་མ་ཐོབ་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་ནས། གཙུག་ལག་ཁང་དུ་དགེ་སློང་དགོན་པ་པ་རྣམས་ཀྱི་ལྷུང་བཟེད་དང་། ཆོས་གོས༌[^3206]གང་དུ་འཇོག་པའི་གནས་ཁང་བསྐོ་བར་བྱའོ་ཞེས་གསུངས་པ་ལྟ་བུ་ཡིན་ནོ། །

[Block 4610]
དུས་ཐམས་ཅད་དུ་ཞེས་བྱ་བ་ནི་དབྱར་དག་ཉི་ཚེར་མ་ཟད་ཀྱི་གང་ཞིག་འདིར་སྨོས་པའི་གཞུང་ལས་དུས་ཀྱི་ཁྱད་པར་ལ་མ་བསྟེན་པ༌[^3207]དེ་བས་ན་མདོའི་ཚིག་འདི་སྨོས་ཏེ། དེའི་ཕྱིར་དབྱར་གནས་པར་ཁས་བླངས་པ་ན་ཁ་ཅིག་གློ་བུར་དུ་འོང་སྲིད་པས་གནས་དང་གནས་མལ་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དུས་ཐམས་ཅད་དུ་ཞེས་བྱ་བ་འདི་ལ་རྗེས་སུ་འཇུག་པ་མེད་པར་བསྟན་པའི་དོན་དུ་ནི་འདི་ཡིན་ཏེ། བྱེ་བྲག་ཡང༌[^3208]ཡོངས་སུ་མ་སྨོས་པའི་ཕྱིར། ཁས་བླངས་པ་གཉིས་ཀ་ལ་ཡང་སྔ་མ་དང་ཕྱི་མ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4611]
གཞི་ཞེས་བྱ་བ་ནི་གནས་ཀྱི་གཞིའོ། །

[Block 4612]
མང་པོ་དག་ལྷགས་ན་གནས་པ་གང་གིས་གཟོད་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གློ་བུར་བ་མང་པོ་དག་ལྷགས་ན་སྔར་གནས་པར་ཁས་བླངས་པ་དག་གིས་གནས་མལ་གཟོད་བསྐོ་བར་བྱའོ། །

[Block 4613]
གནས་པར་ཁས་བླངས་པ༌[^3209]ཕྱིན་ཆད་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སླར་བསྐོ་བ་གཉིས་པ་ལ་ཁས་བླངས་པ་ཕྱི་མ་ཤོས་གང་ཡིན་པ་ཞེས་བྱ་བ་དེ་ལས་ཡིད་ཆེས་པའོ། །

[Block 4614]
འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 4615]
དགེ་སློང་དག་ངས་དགེ་སློང་མ་འོངས་པ་རྣམས་ལ་བསྟེན༌[^3210]ནས་དབྱར་གནས་པར་ཁས་བླངས་པ་གཉིས་པ་བཅས་ཀྱི་གསུམ་པ་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4616]
མང་བ་ཉིད་ཡིན་ན་གཅིག་ལ་ཡང་གཉིས་ལ་སོགས་པ་ཁྱབ་པའི་བར་དག་གོ་ཞེས་བྱ་བ་ལ། གཉིས་ལ་སོགས་པ་ཞེས་བྱ་བ་ནི་གནས་ཀྱི་གཞི་ལ་སོགས་པ་ནས་ཐ་མ་བསྟན་པར་བྱེད་དེ་མང་བ་ཉིད་ཡིན་ན་ཞེས་བྱ་བ་སྟེ། བསྐོ་བར་བྱའོ་ཞེས་སྦྱར་རོ། །

[Block 4617]
ས་དེ་སྙེད་དུ་མང་བའི་གཞི་དག་ལ་རེ་རེ་ལ་བསྐོ་བར་བྱའོ། །

[Block 4618]
ཇི་སྙེད་པ་བསྐོ་བ་རྣམས་ལ་ཐམས་ཅད་ཀྱི༌[^3211]བསྐོ་བ་འགྲུབ་པར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4619]
ཞག་གཅིག་གི་དོན་དུ་གནས་མལ་མནོད་པར༌[^3212]མི་བྱའོ་ཞེས་བྱ་བ་ནི། གནས་མལ་ཞེས་སྨོས་པ་ནི་དཔེ་ཙམ་དུ་ཟད་དེ་གཙུག་ལག་ཁང་ལ་སོགས་པ་ཡང་གནས་པ་ཡིན་ནོ། །

[Block 4620]
འདིར་གཞུང་ནི།

[Block 4621]
ཕྲན་ཚེགས་དག་ལས།

[Block 4622]
དགེ་སློང་གིས་ཞག་གཅིག་གི་དོན་དུ་གནས་མལ་མནོད་པར༌[^3213]མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4623]
རྙེད་པ་འདོད་པས་གཙུག་ལག་ཁང་མི་མནོད༌[^3214]དོ་ཞེས་བྱ་བ་ནི་གནས་མལ་ལ་ཡང་འཕངས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 4624]
འདིར་གཞུང་ནི། དེ་ནས་དུས་གཞན་ཞིག་ན་དགེ་སློང་རྣམས་ལ༌[^3215]རྒན་རིམས་བཞིན་དུ་གནས་མལ་སྟོབས་པར་བྱེད་ན། བྲམ་ཟེ་ཞིག་གཙུག་ལག་ཁང་དུ་འོངས་ནས་དེས་དེ་མཐོང་བ་དང་། གང་གི་ཕྱིར་འདི་བཞིན་བགོ༌[^3216]བཤའ་བྱེད་པའི་ངང་ཚུལ་ཅན་ཤཱཀྱའི་སྲས་ཀྱི་དགེ་སློང་འདི་དག་ལ༌[^3217]སུ་ཞིག་མངོན་པར་དད་པར་མི་འགྱུར་སྙམ་དུ༌[^3218]དད་པ་སྐྱེས་པར་གྱུར་ནས། དེས་གཙུག་ལག་ཁང་བྱེད་དུ་བཅུག་སྟེ་དགེ་སློང་གི་དགེ་འདུན་ལ་ཕུལ་བ་དང་། དགེ་སློང་རྣམས་ཀྱིས་སྨྲས་པ། ཧ་ཅང་གཤེར་ཆེས་སོ་ཞེས་མི་ལེན་པ་དང་། དེས་ཕྲུས་འདེབས་སུ་བཅུག་སྟེ་ཕུལ་ལོ། །

[Block 4625]
དགེ་སློང་རྣམས་ཀྱིས་སྨྲས་པ། ཧ་ཅང་དགོན་དུང༌[^3219]ཆེས་སོ་ཞེས་མི་ལེན་པ་དང་། བྲམ་ཟེ་དེས་དེ་དག་རྙེད་པ་འདོད་པས་མི་ལེན་པར་རིག་ནས། བྲམ་ཟེ་དེས་ཤཱཀྱའི་སྲས་ཀྱི་དགེ་སློང་དག་གིས༌[^3220]རྙེད་པ་འདོད་པས་གཙུག་ལག་ཁང་ལེན་ཏོ་ཞེས་བྱ་བར་རྩོམ་པ་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་རྣམས་ཀྱིས་རྙེད་པ་འདོད་པས་གཙུག་ལག་ཁང་བླང་བར༌[^3221]མི་བྱ་སྟེ། འོན་ཀྱང་སྦྱིན་བདག་རྣམས་ལ་རྗེས་སུ་སྙིང་བརྩེ་བས་གཙུག་ལག་ཁང་རྣམས་བླང་བར་བྱའོ་ཞེས་གསུངས་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
