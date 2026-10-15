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
[Block 4621]
གཉིས་པོ་འདི་ལས་གཞན་དུ་ལྟུང་བ་འབྱུང་བར་འགྱུར་རོ། །

[Block 4622]
འཕྲོག་པའི་སྤང་བའོ།། །།

[Block 4623]
དགོན་པ༌[^3144]པའི་ཆོས་གོས་གཅིག༌[^3145]ལ་ནི་འཇིགས་པ་དང་བཅས་པ་ཉིད་ཡིན་ན་གྲོང་ཡང་རང་གི་གནས་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་དགོན་པ་ནི་འདིར་གནས་ཏེ་ཞེས་བྱ་བ་ནི་དགོན་པ་པ་ཞེས་བྱ་བའི་ཚིག་གིས་རྟོགས་པའོ། །

[Block 4624]
འདིར་ལོར་མ་ཚང་བ་ཉིད་ནི་འདིའི་བྱེ་བྲག་ཏུ་བྱུང་བ་ཡིན་ནོ། །

[Block 4625]
རྣམ་པར་འབྱེད་པ་ལས་ཀྱང་འདིའི་དོན་གསུངས་ཏེ། ལོ་ཕྱི་མ་ལ་ཉེ་བར་འབྲེལ་པར་འགྱུར་ཏེ། དེ་ནི་འདིར་རྟེན་པ༌[^3146]མ་ཡིན་ནོ། །

[Block 4626]
གང་གི་ཕྱིར་འདི་ལ་ལྟུང་བ་བསྟན་པའི་གནས་སྐབས་སུ་ཡང་དག་པར་རྟེན་པ༌[^3147]ཡོད་པ་མ་ཡིན་ནོ། །

[Block 4627]
འོ་ན་ཅིའི་ཕྱིར་དེ་བཟུང་ཞེ་ན། གླེང་གཞིའི་དབང་གིས་སྐབས་མ་ཡིན་པར་གྱུར་པའི་དོན་རྣམས་ལ་ཡང་བཟུང་བ་རྣམས་ཡོད་པར་འགྱུར་ཏེ། འདི་ལྟ་སྟེ་དཔེར་ན་རང་གིས་བླངས་པའི་སྐུད་པའི་ཞེས་བྱ་བ་དང་གཅིག་ཏུ་གོས་ཞེས་བྱ་བ་གང་གི་ཕྱིར་དེར་འབྲལ་བའི་ཉེས་པ་བསྐྱེད་པའོ། །

[Block 4628]
ཆོས་གོས་གཅིག་ལ་ནི་ཞེས་བྱ་བ་གང་གི་ཕྱིར་དེར་འབྲལ་བའི་ཉེས་པ་བསྐྱེད་པའོ། །

[Block 4629]
གྲོང་ཞེས་བྱ་བ་ནི་གང་ཞིག་དགོན་པ་དེའི་སྤྱོད་ཡུལ་དུ་གྱུར་པའི་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པའོ། །

[Block 4630]
འདིར་གཞུང་ནི་དེ་བས་ན་ཆོས་གོས་གསུམ་ལས་གང་ཡང་རུང་སྟེ། ཆོས་གོས་ཁྱིམ་གྱི་ནང་དུ་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4631]
དོན་གྱི་དབང་གིས་གྲོང་གཞན་དུ་འདུག་པ་དེ་ལས་ཞག་དྲུག་ཚུན་ཆད་དུ་དབྲལ་བར༌[^3148]བྱའོ་ཞེས་བྱ་བ་ལ་འདིར་དབྲལ༌[^3149]པར་བྱ་བ་ནི་འདུག་པའི་གནས་དང་། གྲོང་དེའི་ཕྱི་རོལ་གྱི་ཉེན་ཀོར༌[^3150]དུ་སྐྱ་རེངས༌[^3151]ཤར་བའོ། །

[Block 4632]
དེ་ལས་ཞེས་བྱ་བ་ནི་ཆོས་གོས་གཅིག་ལས་སོ། །

[Block 4633]
དེས་ཞེས་བྱ་བ་ནི་དགོན་པ་པ་སྟེ། གང་ཞིག་འདིའི་གྲོང་དུ་བརྗོད་པ་འདི་ལ་དེ་རྣམ་པ་གཞན་གྱིས༌[^3152]གྲོང་ཁྱེར་གཞན་དུ་འདུག་པ་ཞེས་བྱ་བའི་ཐ༌[^3153]ཚིག་གོ། །

[Block 4634]
སྐྱབས་དང་བཅས་པ་ཉིད་དང་དབེན་པའི་གནས་ཡོངས་སུ་བཟུང་བའི་དོན་དུའོ། །

[Block 4635]
དོན་གྱི་དབང་གིས་ཞེས་བྱ་བ་ནི། ཆོས་དང་ལྡན་པའི་དགོས་པའི་དབང་གིས་སོ། །

[Block 4636]
ཞག་དྲུག་ཚུན་ཆད་ཅེས་བྱ་བ་ནི་ཉིན་མཚན་དྲུག་པ་ཚུན་ཆད་དུའོ། །

[Block 4637]
ལྷག་པ་ལ་ནི་བག་ཡངས་མེད་དོ་ཞེས་བྱ་བ་ནི་ཞག་དྲུག་པ་ལས་ལྷག་པ་འདིར་བྲལ་བའི་ཆོ་ག་ལ་འཇུག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4638]
བག་ཡངས་ཀྱི་དབང་གིས༌[^3154]དུས་ཐམས་ཅད་དུ་འདིར་ཉེས་པ་དང་བྲལ་བ་ཉིད་དུ་ངེས་པ་ལ་འདི་གསུངས་སོ། །

[Block 4639]
དེའི་ཕྱིར་འདི་ལ་བསླབ་པའི་གཞི་ཁོངས་སུ་བསྡུ་བ་ཉིད་ཀྱིས་བགྲང་བའོ། །

[Block 4640]
འདི་ལ་ནི་དེའི་ཕྱོགས་གཅིག་ཏུ་གྱུར་པ་ཉིད་དོ། །

[Block 4641]
བར་ཆད་ཀྱི་དབང་གིས་མ་འོངས་པ་ལ་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི། བར་ཆད་ཀྱི་དབང་གིས་མ་འོངས་པ་ལ་ལྷག་པར་ཡང་བག་ཡངས་དང་བྲལ་བའི་ཆོ་ག་ལས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4642]
འདིར་བཙུན་པ་དགེ་སློང་དགོན་པ་བས་གྲོང་གཞན་དུ་ཆོས་གོས་བཞག་སྟེ་བགྱི་བ་འགའ་ཞིག་གི༌[^3155]སླད་དུ་མཚམས་ཀྱི་སླད་རོལ་དུ་མཆི་ཞིང་དེ་ཉིད་དུ་སླར་བཟློག་པར་བགྱིའོ་སྙམ་པ་ལས་གལ་ཏེ་དེ་ལ་བར་ཆད་འགའ་ཞིག་བྱུང་ནས་སླར་མཆི་བར་རྔོ་མ་ཐོགས༌[^3156]ན་ཆོས་གོས་དེ་དང་འབྲལ་ཞེས་བགྱི་བ་ལགས་སམ། ཉེ་བ་འཁོར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4643]
ཁ་ཅིག་འདི་ལྟར་རྣམ་པར་རྟོག་སྟེ་དགེ་སློང་དག་གིས་ཞག་དྲུག་ཕྱི༌[^3157]རོལ་དུ་འགྲོ་བར་བྱའོ་སྙམ་དུ་བརྣག་པ་སྔོན་དུ་བྱས་ཏེ་ཕྱི་རོལ་དུ་འགྲོ་ཞིང་ཞག་ལས་འདས་པ་ལ་ནི་འབྲལ་བའི་ཉེས་པ་མེད་པ་ཡིན་གྱི། གལ་ཏེ་དེ་ལྟར་བརྣག་པ་མ་བྱས་པར་ཉིན་གཅིག་གམ་མཚན་གཅིག་འགྲོ་བར་བརྣགས་ཏེ་སོང་བ་ལས་ཞག་དྲུག་འདས་པ་དེ་ལ་ནི་ཉེས་པ་ཁོ་ནར་འགྱུར་སྙམ་དུ་རྟོག་པ་དག་ཡོད་པས་དེ་བསལ་བའི་ཕྱིར་འདིར་ཞག་དྲུག་ཏུ་འགྲོ་བ༌[^3158]ཧ་ཅང་ཐལ་བ་ཉིད་ལ་ནི་བརྣག་པ་ཡན་ལག་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཞག་དྲུག་ཏུ་འགྲོ་བའི་དུས་དེ་ལ༌[^3159]བརྣག་པ་བྱས་ནས་ཞག་དྲུག་འབྲལ་བར་གྱུར་པ་ལ༌[^3160]ཉེས་པ་མེད་ཅེས་བྱ་བ་ནི་འདིར་རྣམ་པར་གཞག་པ་ཡོད་པ་མ་ཡིན་ཏེ། ཇི་ལྟར་ཡང་རུང་བར་འགྲོ་བ་ལ་ཉེས་པ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4644]
ཞག་དྲུག༌[^3161]ན་འབྲལ་བའི་སྤང་བའོ།། །།

[Block 4645]
བདག་ཉིད་གནས་པར༌[^3162]ཁས་བླངས་པས༌[^3163]ཁས་བླངས་པའི་ཉིན་མོའི་ཟླ་བ་སྔ་མའི་དང་པོ་ཚུན་ཅད༌[^3164]ནས་དབྱར་གྱི་རས་ཆེན་བཙལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་འདིའི་ལྟུང་བ་ཁས་བླངས་པའི་ཉིན་མོ་ནི༌[^3165]ཁས་བླངས་པའི་ཞག་གང་ཞིག་འདིས་ཉེ་བར་འཁོར་བའི་ཕྱིར་སྔ་མའམ་ཕྱི་མ་འམ༌[^3166]མངོན་པར་འདོད་པའི་ཉི་མའོ། །

[Block 4646]
དེའི་སྔ་མར་གྱུར་པའི་ཟླ་བ་གང་ཡིན་པ་དེའི་དང་པོ་གང་ཞིག་དེ་དང་པོར་བྱས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4647]
དབྱར་གནས་པའི་ཟླ་བ་ཕྱེད་ཀྱི་མཐར་དེ་གཟུང་བར༌[^3167]བྱའོ། །

[Block 4648]
རང་གི་སྔ་མའམ༌[^3168]ཕྱི་མ་ཁས་བླངས་པའི་དབང་གིས་འདིའི་དབྱར་གནས་པའི་གང་ཞིག་རྣམ་པར་གནས༌[^3169]པ་དེ་རྣམས་ལས་ལྷག་པར་གྱུར་པའི་ཟླ་བ་ཕྱེད་གང་ཡིན་པ་དེའི་ཐ་མའི་དུས་ཀྱི་བར་དུ་འཛིན་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4649]
གྲུབ་པའི་སྐད་ཅིག་མ་ཚུན་ཆད་ནས་དོན་གྱིས་གོ་བའོ། །

[Block 4650]
སྐྱ་རེངས༌[^3170]ཤར་བ་ནི་ཉིན་མོ་ལ་སོགས་པའི་བར་རོ། །

[Block 4651]
དེ་བས་ན་ཚེས་བཅུ་དྲུག་ལ་སྐྱ་རེངས༌[^3171]ཤར་བ་ལ་འདིར་ལྟུང་བྱེད་དོ། །

[Block 4652]
དབྱར་གྱི་རས་ཆེན་རྣམས་འདིར་བཟུང་བ་སྟེ། ལོ་དུས་རྣམས་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རང་གི་སྒྲས་རྟོགས་པར་བྱའོ། །

[Block 4653]
འདིར་མདོ་ནི་ཟླ་བ་ཕྱེད་ཀྱིས་ལྷག་པར་དབྱར་གནས་པ་རྣམས་ཀྱིས་བྱ་སྟེ་བཅང་བར་བྱ་ཞེས་བྱ་བའོ། །

[Block 4654]
འདིའི་རྣམ་པར་འབྱེད་པ་ནི་ཟླ་བ་ཕྱེད་དགོས་པ་ཞེས་བྱ་བ་དབྱར་གནས་བྱས་ཏེ་ཟླ་བ་ཕྱེད་ཀྱི༌[^3172]ལྷག་མ་ནི་ལྷག་པར༌[^3173]གྱུར་པ་འཆང་བའི་དུས་ན་བཅང་བར༌[^3174]བྱ་ཞེས་བྱ་བའི་མདོའི་ཚིག་འདི་ལ་དོན་འདིའོ། །

[Block 4655]
ཡི་གེ་ཁ་ཅིག་ལས་འདི་ཤིན་ཏུ་བསལ་བར་བརྗོད་པ་ཡིན་ཏེ།[^3175] བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་དབྱར་གྱི་གོས་རས་ཆེན་རུང་བ་མ་ཡིན་པ་འཆང་བར་བྱེད་དེ། ལྷག་མ་ཟླ་བ་ཕྱེད་དང་ལྔ༌[^3176]ལས་ལྷག་ན་ཅི་ལྟུང་བར་འགྱུར་རམ་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

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
--- END BLOCKS ---
