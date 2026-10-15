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
[Block 4656]
དོན་མ་ཡིན་པ་ལ་ཡང་འདི་ལྟར་དུས་སུ་འཆང་བ་སྐྱེད་པར༌[^3177]འགྱུར་བ་འདི་ནི་མི་རིགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་འདི་མྱུར་བ་ཞེས་བྱ་བ་ཉིད་དུ་འཇུག་པར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 4657]
གང་ཞིག་ཆོ་ག་འདི་ལས་འདའ་བར་བྱེད་པ་ལ་ཁ་ན་མ་ཐོ་བ་དེ་བསྟན་པར་བྱ་སྟེ། དེའི་ཕྱིར་སྔོན་དང་ཕྱི་མ་གཉིས་ལས་དེ་མ་ཡིན་པའི་དུས་ནི་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཙལ་བའི་དུས་དང་བཅས་པ༌[^3178]ཇི་ལྟར་བསྟན་པ་ལས་སྔ་མ་དང་ཕྱི་མའི་དུས་དེ་དག་གི་དུས་ལྟུང་བའི་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །གང་དུ་ཕྱི་མ་ལ་བྱེད་པ་པོ་ཉིད་གང་དུ་སྔ་མ་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གཞན་དུ་འཆང་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རིགས་པ་ལས་མ་འདས་པའི་འཆང་བའི་དུས་ལས་གཞན་པའི་དུས་ཏེ། དེ་འཆང་བ་ཡོད་པ་ལ་དངོས་གཞིའི་ཁ་ན་མ་ཐོ་བའི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ། །

[Block 4658]
སྔར་བཙལ་བ་ལ་ནི་ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བ་ནི་བཙལ་བའི་དུས་སྔར་བསྟན་པ་བས་གང་ཞིག་གཞན་ནི་དུས་ཏེ། དེ་བཙལ་ན་བཙལ་བ་ཙམ་ལ་ཉེས་བྱས༌[^3179]འདི་ལ་བྱེད་པ་པོ་ཉིད་མ༌[^3180]ཡིན་ནོ། །

[Block 4659]
ད་ནི་དངོས་གཞི་ལ་དུ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གྲུབ་ན་མཐའིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་གི་ཚེ་བཙལ་བར་གྱུར་པ་ལ་དེ་གྲུབ་པར་གྱུར་ན་དེའི་ཚེ་དངོས་གཞི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4660]
རྙང་རྙིང་ལ་ནི་ན་སྨད་པ་མེད༌[^3181]དོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 4661]
དབྱར་གྱི་གོས་རས་ཆེན་རྙང་རྙིང་དུ་གྱུར་པ་ཞིག་ཟླ་བ་ཕྱེད་དང་ལྔ་ལས་ལྷག་པར་འཆང་ན་ཉེས་བྱས་སོ། །

[Block 4662]
དེ་བཞིན་དུ་དབྱར་གྱི་གོས་རས་ཆེན་བུག་རྡོལ་དུ་གྱུར་པ་ཞིག་ཧ་ཅང་མ་ཚོགས་ཏེ། ཚོལ་བར་བྱེད་ན་ཡང་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4663]
དེའི་རྗེས་སུ་འགྲོ་བ་ནི་ཁས་བླངས་པ་ཇི་ལྟ་བ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་འགྲོ་བ་ཁས་བླངས་པ་ནི་རྗེས་སུ་འགྲོ་བ་དང་འབྲེལ་པ་ལ་གང་ཅུང་ཟད་དེ་ཐམས་ཅད་ནི་ཁས་བླངས་པ་ཇི་ལྟ་བར་རིག་པར་བྱའོ། །

[Block 4664]
གལ་ཏེ་སྔར་ཁས་ལེན་ན་དེའི་དབང་གིས༌[^3182]དེ་ནས་དེའི་ཕྱི་མའོ། །

[Block 4665]
འདི་ལྟ་སྟེ་མཐའི་ཞག་བཅུ་ལ་བརྟད་པ༌[^3183]ལས་བྱུང་བའི་གོས་བླངས་སོ་སྙམ་པའི་ཞག་བཅུ་པ་ལ་ཕྱི་མ་ཉིད་ཉེས་པ་མ་ཡིན་པའི་འབྱུང་གནས་ཉིད་དུ་གྱུར་པ་དབྱར་གྱི་གོས་རས་ཆེན་གྱིས་དབྱར་གནས་པར་བྱ་བའི་ཚད་ལ་ལྟོས་ནས༌[^3184]དགག་དབྱེ་དང་སྲ་བརྐྱང་འདིང་བའོ།[^3185] །དབྱར་གྱི༌[^3186]རས་ཆེན་གྱི་སྤང་བའོ།། །།

[Block 4666]
བརྟད་པ་ལས་བྱུང་བའི་སྤང་བ་ལ་དོན་གང་ཞིག་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དབྱར་གྱི་རྙེད་པ་ནི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དབྱར་གནས་པའི་ཕྱིར་རྙེད་པ་གང་ཡིན་པ་ལ་སྟེ། གཞན་དབྱར་གྱི་རྙེད་པ་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4667]
འདིའི་བྱེད་པ་པོ་ཉིད་གང་དུ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དབྱར་གྱི་ནང་ལོགས་སུ་བདག་གིར་བྱེད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་དབྱར་གནས་པར་བྱ་བའི༌[^3187]ནང་རོལ་དུ་བདག་གིར་བྱེད་ནའོ་ཞེས་བྱ་བའི་དོན་ཏེ། །དེ་ལ་དམིགས་ཀྱིས་བསལ་བར་བྱ་བར་འདོད་ནས་བརྟད་པའི་དབང་གིས་མཐའ༌[^3188]ཞག་བཅུ་ལ་རྙེད་པ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཐའི་ཞག་བཅུ་ལ་བརྟད་པ་ཙམ་ཉེ་བར་བརྟགས་པས་བྱས་པ༌[^3189]ལ་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4668]
བརྟད་པ་ལས་བྱུང་བའི་གོས་ལྔ་པོ་ནད་པ་ལ་སྦྱིན་པ་དང་། ནད་པའི་ཕྱིར་སྦྱིན་པ་དང་། འཆི་བ་ལ་སྦྱིན་པ་དང་། འཆི་བའི་ཕྱིར་སྦྱིན་པ་དང་། འགྲོ་བར་ཆས་པ་ལ་སྦྱིན་པ་ཞེས་བྱ་བ་བརྟག་པ༌[^3190]ལས་བྱུང་བ་ལྔ་པོ་རྣམས་ལ་འདིར་བཟུང་ངོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་ནི་དཔེ་ཙམ་དུ་རྣམ་པར་གནས་པའོ། །

[Block 4669]
རྒྱལ་པོ་དང་ཆོམ་རྐུན་དང་རིགས་རྒྱུད་དང་ཆུ་ལ་སོགས་པས་ཁྱེར་དུ་དོགས་པ་དང་། ཡོངས་སུ་ཟད་པ་ཁས་བླངས་པ་ལྟ་བུ་སྐྱེས་པའི་ཞག་ལ་སོགས་པའི་སྐབས་སུ་བླང་བར་བྱེད་པ་པོའི་ཁོངས་སུ་བསྡུས་པ་མཆོད་གནས་བགོ་སྐལ་ལ་གཏོགས་པའི་འཆིར་དོགས་པ་ལ་སོགས་པ་དག་ཀྱང་འདི་རྣམ་པར་གཞག་པ་སྟེ། དེ་བས་ན་བརྟད་པ་ཙམ་ཉེ་བར་བརྟགས་པའོ། །

[Block 4670]
དེ་བགོས་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བརྟད་པའི་དབང་གིས་ཀྱང་རྙེད་པར་འགྱུར་བ་ལ་དབྱར་གྱི་ནང་ལོགས་སུ་བགོ་ན་ཡང་བྱེད་པ་པོ་ཉིད་ཡིན་པ་དང་། དབྱར་གྱི་རྙེད་པ་གཞན་གཅིག་པུ་ལ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4671]
འདིར་གཞུང་ནི་བླང་བར་བྱ་ཞིང་བླངས་ནས་ཀྱང་གོས་འགྱེད་པའི་དུས༌[^3191]ལ་མ་བབ་ཀྱི་བར་དུ་ཆོངས་ཤིག་ཅེས་བྱ་བ་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4672]
འདིར་བགོ་བར་མི་བྱ་བའི་ཚིག་ནི་མངོན་པར་འདོད་པ་སྟེ། རྣམ་པར་བགོས་པས་མ་ཡིན་ཞེས་བྱ་བར་རྟོགས་པའོ། །

[Block 4673]
བརྟད་པ་ལས་བྱུང་བའི་དབྱར་གྱི་རྙེད་པ་ལ་དབྱར་གྱི་ནང་ལོགས་སུ་བགོ་བར་མི་བྱ་བའི་རྣམ་པ་ལ་ཡང་བདག་ཏུ་སྤང་བའོ། །

[Block 4674]
བརྟད་པ་ལས་བྱུང་བའི་བགོ་བ་ལ་ཡང་བགོ་བ་ཉིད་དོ་ཞེས་བྱ་བ་འདིར་རྣམ་པར་གཞག་པའོ། །

[Block 4675]
གཙུག་ལག་ཁང་གང་དག་ན་ཆོས་གོས་ཀྱི་ཟོང་ངེས་པར་གྱུར་པ་ཡོད་པ་དེ་ལ་བསྒྲུབ་པ་གང་ཡིན་ཞེ་ན། བཟུང་བ་ཉིད་ན་དེ་བདག་ཏུ་བྱ་བ་ཉིད་དེ་མདུན་དུ་བྱ་བ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 4676]
མ༌[^3192]བགོས་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ཞེས་བྱ་བའི་རྗེས་སུ་སྦྱར་རོ། །

[Block 4677]
བརྟད་པའི་དབང་གིས་གཞན་དབྱར་གྱི་བཟུང་བ་ལ་མ་བགོས་པ་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4678]
དངོས་གཞི་བདག་གིར་བྱེད་པ་དང་། འགོད་པ་དང་མི་འགོད་པ་རྣམས་ལ་བྱེད་པ་པོ་ཉིད་འདིར་བརྗོད་པར་རིག་པར་བྱའོ། །

[Block 4679]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་དབྱར་གྱི་ནང་ཚུན་ཆད་དུ་དབྱར་གྱི་རྙེད་ལ༌[^3193]འགོད་པར་བྱེད་དམ་གོས་འགྱེད་པར་བྱེད་པའི་དུས་ལས་འདས་པའི་བར་དུ་འཆང་བར་བྱེད་ན་ཐམས་ཅད་དུ་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 4680]
མ་བགོས་ན་ཡང༌[^3194]བརྟད་པ་ལས་བྱུང་བ་ལས་གཞན་ལ་དབྱར་གྱི་ནང་རོལ་དག་ཏུ་མ་བྱས་པ་ལ་མདོའི་གཞུང་ཡང་རིག་པར་བྱའོ། །

[Block 4681]
ལྟུང་བ་མེད་པ་རྒྱས་པར་བཤད་པ་ཡང་བརྟད་པའི་དབང་གིས་ཞག་བཅུའི་མཐར་རྙེད་པར་གྱུར་པ་ལས༌[^3195]འདི་ལྟར་བླང་བར་བྱ་བ་ཉིད་ཅེས་བྱ་བ་བརྗོད་པའི་ཕྱིར་སྐྱེ་བར་འགྱུར་རོ། །

[Block 4682]
གཞན་དུ་ན་འོག་ནས་རྙེད་པར་གྱུར་པ་ལས༌[^3196]ཞེས་བྱ་བའོ། །

[Block 4683]
སྦྱིན་བདག་གི་ཚིག་གིས་དབང་མེད་ནའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་སྦྱིན་བདག་འདི་སྐད་ཅེས་རེ་ཞིག་ཁྱེད་ཅག་གིས་མ་བགོ་ཞིག །བདག་མཆིས་ནས་རང་གི་ལག་ནས་འབུལ་ལོ་ཞེས་ཟེར་ན། དེའི་དབང་གིས་མ་བགོས་ན་ཡང་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4684]
དུས་གང་གི་ཚེ་མ་བགོས་ན་ཞེ་ན། དེའི་ཕྱིར་དགག་དབྱེའི་ཉིན་མོའི་ཕྱི༌[^3197]དེ་ཉིན་པར་དེ་སྦེད་པར༌[^3198]མ་བསྐོས་པ་རྣམས་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགག་དབྱེའི་ཉིན་མོ་ཞེས་བྱ་བ་ནི་དེ་མ་ཐག་པའི་ཚེས་བཅུ་དྲུག་སྟེ། ཟླ་བ་གསུམ་གྱི་རྗེས་ལ་ཆོས་གོས་སྦེད་པར་བྱེད་པ་མ་བསྐོས་པའོ། །

[Block 4685]
འདི་རྣམས་ཀྱིས་མ་བསྐོས་པ་ལ་གལ་ཏེ་དེ་དང་འབྲེལ་པའི་ཁ་ན་མ་ཐོ་བ་གང་རྣམས་ཀྱིས་འདོད་པ་མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4686]
ཇི་སྲིད་དུ་གོས་འགྱེད་པའི་དུས་ལས་འདས་པའི་བར་དུ་བཅང་བར་བྱ་བ་སྨོས་ཏེ།[^3199] དེ་ལས་ལྷག་པར་འཆང་བར་བྱེད་ན་ཞེས་བྱ་བ་ནི་འདིར་མདོ་སྡེ་འགྱེད་པའི་དུས་ལས་ཐོབ་པའི་བར་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4687]
འགོད་པའི་དུས་ཐོབ་པ་ནི་ཟླ་བ་གསུམ་ལས་འདས་པར་བྱེད་པའོ། །

[Block 4688]
ཟླ་བ༌[^3200]གསུམ་ལས་གཞན་པའི་དུས་ནི་འགེད་པའི་དུས་སོ། །

[Block 4689]
དེ་ལྟར་ཡང་དེའི་རྣམ་པར་འབྱེད་པ་ལས་དགེ་སློང་གིས་གོས་འགེད་པའི་དུས་དང་སྐབས་མ་ཡིན་པ་གང་ཞེ་ན། སྲ་བརྐྱང་མ་བཏིང༌[^3201]བའི་གནས་ན་ནི་སྟོན་ཟླ་ཐ་ཆུངས༌[^3202]ཀྱི་ཉ་ཚུན་ཆད་དོ། །

[Block 4690]
སྲ་བརྐྱང་བཏིང་བའི་གནས་ན་ནི་སྟོན་ཟླ་ཐ་ཆུངས༌[^3203]ཉ་ཕྱིན་ཆད་ནས་དཔྱིད་ཟླ་འབྲིང་པོའི་ཉའི་བར་ཏེ། དེ་ནི་དགེ་སློང་གི་གོས་འགྱེད་པའི་དུས་མ་ཡིན་ནོ། །

[Block 4691]
ལྷག་མའི་དུས་ཞེས་བྱ་བ་ནི་ཁས་བླངས་པ་ཕྱི་མ་ཤོས༌[^3204]ངེས་པར་བྱས༌[^3205]ན་ནི་སྟོན་ཟླ་ཆུངས༌[^3206]ཉ་ཚུན་ཆད་དོ་ཞེས་གསུངས་སོ། །

[Block 4692]
ཁས་བླངས་པ་སྔ་མ་ལ་ནི་སྟོན་ཟླ་འབྲིང་པོའི་ཉ༌[^3207]ཚུན་ཆད་དུས་མ་ཡིན་ནོ། །

[Block 4693]
དེ་ནི་མི་བསྐོ་བར༌[^3208]མི་བྱའོ་ཞེས་བྱ་བ་ནི་བརྟད་པ་ལས་བྱུང་བའི་དུས་སུ་གཏང་བར༌[^3209]བྱ་བ་ཉིད་ལ་གོས་སྦེད་པ་མ་ཡིན་པ་འདི་བསམ་པར་མི་བྱའོ། །

[Block 4694]
ཞུ་བ་ལས་བསླབ་པའི་གཞི་འདི་ལ་རིམ་པ་ནི་འདི་ཡིན་ནོ། །

[Block 4695]
རྣམ་པར་འབྱེད་པ་ལས་ནི་འཕྲོག་པའི༌[^3210]བསླབ་པའི་གཞི་ལས་ནི་དེ་མ་ཐག་པའོ། །
--- END BLOCKS ---
