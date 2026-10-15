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
[Block 4796]
ཚུན་ཆད་དུ་ཞེས་བྱ་བ་ནི་ཆོས་དང་ལྡན་པའི་གཏམ་རྣམ་པར་གཏན་ལ་དབབ་པས་ཇི་སྲིད་དགག་དབྱེའི་ལས་རྩོམ་པ་ལ་ཐུག་པ་དེ་ཚུན་ཆད་དུ་མཚན་མོ་འདའ་བར་བྱའོ། །

[Block 4797]
དེ་ལ་ཡང་གང་གི་ཞེ་ན། དེའི་ཕྱིར་དགག་དབྱེའི་ལས་ནི་སྐྱ་རེངས་འཆར་བའི་མདུན་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལྟར་དགག་དབྱེའི་ལས་བྱའོ། །

[Block 4798]
ཇི་ལྟར་སྐྱ་རེངས་དང་པོ་མ་ཤར་བར༌[^3365]ལས་ཐམས་ཅད་ཟིན་པ་དེ་ལྟར་དགག་དབྱེའི་ལས་བྱའོ། །

[Block 4799]
མཐར་ཐུག་པའི་ཆ༌[^3366]དང་ལྡན་པའི་སྐྱ་རེངས་ཀྱི་ལས་ལ་མི་བྱ་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4800]
དགེ་སློང་དགག་དབྱེའི་བྱེད་པ་བསྐོ་བར་བྱའོ། །

[Block 4801]
མི་ནུས་ན་དུ་མའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་མང་བ་ཉིད་ཀྱི་ཕྱིར་དགག་དབྱེའི་བྱེད་པ་གཅིག་གིས་མི་ནུས་ན་དགག་དབྱེ་བྱེད་པ་དུ་མ་ཡང་ཤེས་པར་བྱ་བའི་དོན་ཏོ།[^3367] །དགག་དབྱེ་བྱ་བའི་ཕྱིར་གཞན་གྱི་དགེ་འདུན་ལ་གསོལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གསོལ་བའི་ལས་བྱ་བའོ། །

[Block 4802]
འདི་ལ་གྲལ་གྱི་ཆ་ལས་བྱར་རུང་ངོ་ཞེས་བྱ་བ་ནི་གྲལ་གྱི་ཚར་གཅིག་ལ་དགག་དབྱེ་བྱེད་པ༌[^3368]དུ་མ་དག་གིས་ལས་བྱེད་པར་རིགས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4803]
རྩྭ་དཱུར་བ་བྲིམ་པ་དང་མདུན་དུ་འདུག་པ་ཡང་འདིའི་ཡུལ་ཡིན་ནོ། །

[Block 4804]
དེས་རྩྭ་དཱུར་བ་བྲིམ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགག་དབྱེ་བྱེད་པ་དེས་ཉེ་བར་མི་གནས་པ་རྣམས་ལ་བྲིམ་པ༌[^3369]ཡོད་པ་མ་ཡིན་ཏེ། དེར་བྲིམ་པའི༌[^3370]རྣམ་པར་གཞག་པ་རྗེས་སུ་སྐྱོང་བའི་དོན་དུ་ངེས་པར་འདིར་ཉེ་གནས་ཀྱི་ཕྱིར་རྩྭ་དཱུར་བ་འབད་པ་དང་ལྡན་པས་གནས་པར་བྱའོ་ཞེས་བྱ་བའི༌[^3371]དོན་གྱིས་ཐོབ་པར་བྱའོ། །

[Block 4805]
དགག་དབྱེའི་ཕྱིར་གཞན་གྱིས་དགེ་འདུན་ལ་གསོལ་བར་བྱའི༌[^3372]དགག་དབྱེ་བྱེད་པ་པོས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་དགོངས་པའོ། །

[Block 4806]
དགག་དབྱེ་བྱས་ཟིན་གྱི་བར་དུ་དགེ་སློང་རེ་རེའི་མདུན་དུ་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དགག་དབྱེ་བྱས་ཟིན་གྱི་བར་དུ་ཞེས་བྱ་བ་ནི་དགག་དབྱེ་རྗེས་སུ་བསྒྲུབ་པ་ཐམས་ཅད་ལ་ཁྱབ་པ་འདི་ཡིན་ཏེ། དེ་ལ་ཇི་སྲིད་དུ་དགེ་སློང་དེས་དགག་དབྱེ་བྱས་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4807]
མདུན་དུ་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་གཞན་དུ་གནས་པ་དེ་ལྟར་ཁོ་ནར་རོ། །

[Block 4808]
གཞན་རྗེས་སུ་མི་མཐུན་པ་ཉིད་ཀྱིས་ཕྱིར་ཚོལ་བ་པོ་ལའོ། །

[Block 4809]
དེ་ལ་དགག་དབྱེ་གོ་བར་བྱ་བ་ནི་ལན་གསུམ་མོ་ཞེས་བྱ་བ་ནི་དགག་དབྱེ་བྱེད་པ་མདུན་ན་གནས་པ་དེ་ལ་དགེ་སློང་རེ་རེས་ཀྱང་དགག་དབྱེ་བྱ་བའི་སྔགས་ལན་གསུམ་བརྗོད་པར་བྱའོ། །

[Block 4810]
དགེ་འདུན་བཙུན་པ་རྣམས་དགོངས་སུ་གསོལ་ཞེས་བྱ་བ་འདིར་ཁ་ཅིག་འདིར༌[^3373]དགག་དབྱེའི་སྔགས་རྩོམ་པ་ན་བཏོན༌[^3374]ནས། ཚེ་དང་ལྡན་པ་དགོངས་སུ་གསོལ། གནས་གསུམ་གྱིས་དགེ་འདུན་ལ་དགག་དབྱེ་བགྱིད༌[^3375]དེ་ཞེས་བྱ་བ་དེ་ཡང་། དགེ་འདུན་བཙུན་པ་རྣམས་ལ་གནས་གསུམ་གྱིས་དགག་དབྱེ་བགྱིད་དོ་ཞེས་བྱ་བའོ། །

[Block 4811]
དེར་མདུན་དུ་འདུག་པ་དགོས་པ་མེད་པ་དེ་ལྟ་བས་ན་དེ་ལ་མི་བརྟེན༌[^3376]པའོ། །

[Block 4812]
རྒན་པའི་མཐར་འདུག་སྟེ། འདི་ལ་འདི་ལྟར་རིགས་པ་ཡིན་ཏེ། དགག་དབྱེ་བྱེད་པ་པོས་འདི་ལྟར་གོ་བར་བྱ་བར་རིགས་པ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་དེ་ཉིད་ལ་དགོངས་སུ་གསོལ་ཞེས་བྱ་བར་རིགས་པ་ཡིན་ནོ། །

[Block 4813]
དེ་ཉིད་ཀྱིས་ནད་པ་ངལ་བ་དང་གནས་མལ་ཕན་ཕུན༌[^3377]དུ་འགྱུར་བ་དང་། དུས་ལས་ཡོལ་བ་དང་། གནོད་པ་འབྱུང་ན་གཉིས་སོ་ཞེས་བྱ་བ་ལ་གཉིས་སོ་ཞེས་བྱ་བ་ནི། གོ་བར་བྱའོ། །

[Block 4814]
ནད་པ་ཞེས་བྱ་བ་ནི་གཞང་འབྲུམ་གྱི་ནད་ལ་འདིར་ནད་པར་བརྗོད་དོ། །

[Block 4815]
དུས༌[^3378]ལས་ཡོལ་བ་ཞེས་བྱ་བ་ནི། ལོ་གཅིག་གིས༌[^3379]དུས་ལས་ཡོལ་བར་གྲགས་པ་སྟེ། ཆོས་སྙན་པ་སྨྲ་བ་དང་། ཆོས་དང་ལྡན་པའི་གཏམ་རྣམ་པར་གཏན་ལ་འབེབས་པ་དང་། རྩོད་པ་ཉེ་བར་ཞི་བར་བྱེད་པས་ཀྱང་འགའ༌[^3380]ཞིག་མང་དུ་མཚན་མོ་འདའ་བར་བྱེད་པ་དང་། གནོད་པ་འབྱུང་བ་ནི་ཉམ་ང་བ་འབྱུང་བ་སྟེ། རྒྱལ་པོ་དང་ཆོམ་རྐུན་དང་གྲོང་བའི་མི་དང་མི་མ་ཡིན་པའི་གདུག་པ་དང་རླུང་དང་མེ་དང་ཆུ་ལ་སོགས་པའི་གནོད་པས་སྲོག་དང་དགེ་སྦྱོང་གི་ཚུལ་དང་། ཚངས་པར་སྤྱོད་པའི་བར་ཆད་ཀྱི་གནས་འདི་ལའོ། །

[Block 4816]
དེར་རླུང་ལ་སོགས་པ་གསུམ་གྱིས་ཀྱང་འདུག་པ་ལས་འདའ་བར་འགྱུར་རོ། །

[Block 4817]
དེ་འདིར་ཁོངས་སུ་བསྡུ་བར་མི་རིགས་སོ། །

[Block 4818]
ཐམས་ཅད་ཉམས་པར་འགྱུར་བས་ཡང་དག་པར་གོ་བར་བྱ་བ་ཁོངས་སུ་བསྡུ་བར་རིགས་པའོ། །

[Block 4819]
རླུང་ལ་སོགས་པས་ཀྱང་དེ་བསྒྲུབ་པ་ཡིན་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 4820]
མཐར་འཛིན་པ་འཇུག་པ་ལ་དུས་ལས་འདའ་བར་བསྲུང་བར་བྱ་བ་མ་ཡིན་པའོ། །

[Block 4821]
ཆོས་དང་ལྡན་པའི་དོན་ལ་གང་གིས་ཀྱང་བརྩམས་ཏེ་མཐར་འཛིན་པ་ནི་མི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 4822]
སངས་རྒྱས་ཀྱི་མཆོད་པ་ལ་སོགས་པ་གཞན་འདིར་ཐམས་ཅད་ལ་གོ་བར་བྱེད་པ་མ་སྐྱེས༌[^3381]པ་ལ་བར་ཆད་བྱེད་པ༌[^3382]ཡོད་པ་ཡིན་ཏེ། ཚངས་པར་སྤྱོད་པའི་གནས་རྗེས་སུ་དྲན་པ་དང་ཤེས་བཞིན་གྱི་ངོ་བོ་ལ་དེའི་ཕྱིར་འདིར་གནོད་པ་ལ་འགའ་ཞིག་མ་བཟུང་བ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 4823]
འདི་ལ་རྒྱུ་མཚན་གཞན་སྡིག་པ་དང་ཕྱེ་མ་ལེབ་ལ་སོགས་པ་ཡང་ཡོད་དེ། དེ་བས་ན་འདིར་གཞང་འབྲུམ་ལ་སོགས་པའི་ཚིག་འདི་དཔེ་ཙམ་དུ་ཟད་དེ་ཞེས་བྱ་བར་ཤེས་ནས་འདི་ལྟར་མདོར་བྱས་སོ། །

[Block 4824]
དེ་ཙམ་གྱིས་ན་ཡང་ལན་གཅིག་གོ་ཞེས་བྱ་བ་ནི་ལན་གཉིས་བཟླས་པ་དེ་ཙམ་གྱིས་ཀྱང་ནད་པ་ངལ་བ་ལ་སོགས་པ་འབྱུང་བར་འགྱུར་ལ་ལྟ་ན་དགག་དབྱེ་གོ་བར་བྱ་བའི་སྔགས་ལན་གཅིག་བཟླས་པར་བྱའོ། །

[Block 4825]
དེས་གྲལ་རྫོགས་ན་གཞན་ལའོ་ཞེས་བྱ་བ༌[^3383]ལ། དེས་ཞེས་བྱ་བ་ནི་དགག་དབྱེ་བྱེད་པ་དེས་སོ། །

[Block 4826]
གཞན་ལའོ་ཞེས་བྱ་བ་ནི། དགག་དབྱེ་བྱེད་པ་གཞན་གཅིག་ལ་དགག་དབྱེ་གོ་བར་བྱེད་པའོ། །གང་གི་ཚེ་ཞེ་ན། དེའི་ཕྱིར་གྲལ་རྫོགས་ན་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4827]
དེར་དེ་གཞན་ལའོ་ཞེས་བྱ་བ་ནི་དགག་དབྱེ་བྱེད་པ་གཞན་དེ་མེད་ན་དགག་དབྱེ་བྱེད་པ་དེས་སོ། །

[Block 4828]
[^3384]དགེ་སློང་གཞན་གཅིག་གིས་མདུན་དུ་དགག་དབྱེ་གོ་བར་བྱའོ། །

[Block 4829]
དགེ་འདུན་ཐམས་ཅད་ཀྱི༌[^3385]དགག་དབྱེ་བྱས་པ་དེ་ཉིད་དགེ་འདུན་ལ་གོ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཉིད་ཅེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་དགག་དབྱེ་བྱས་པ་ཉིད་ལ་དགག་དབྱེ་བྱེད་པ་པོས་གོ་བར་བྱའོ། །

[Block 4830]
ཐམས་ཅད་ཀྱིས་ལེགས་པར་དགག་དབྱེ་མཛད་དོ།[^3386] །ཤིན་ཏུ་དགག་དབྱེ་མཛད་དོ་ཞེས་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ལ་ཐམས་ཅད་ཀྱིས་ཞེས་བྱ་བ་ནི་དགེ་སློང་འདུས་པ་ཐམས་ཅད་ཀྱིས་སོ། །

[Block 4831]
ཤིན་ཏུ་དགག་དབྱེ་མཛད་དོ་ཞེས་བྱ་བ༌[^3387]ནི་ཁོ་བོ་ཅག་གིས་འདི་ལ་ཐེ་ཚོམ་པར་ཞེས་བྱ་བ་དེ་ལྟར་བསྒྲུབ་པའོ། །

[Block 4832]
རང་གི་རྫས་གང་ཡང༌[^3388]རུང་བ་ཐ་ན་ཁབ་ཙམ་གྱིས་ཀྱང་དགེ་འདུན་ལ་རྫས་ཀྱི་དགག་དབྱེ་བརྩམ་པར༌[^3389]བྱ་སྟེ། དེ་བླངས་ནས་ཚིག་གིས་སོ་ཞེས་བྱ་བ་ལ། རང་གིས་ཞེས་བྱ་བ་ནི་དགག་དབྱེ་བྱེད་པོ༌[^3390]བདག་ཉིད་དོ། །

[Block 4833]
ཇི་ལྟར་བྱ་ཞེ་ན་དེའི་ཕྱིར་དེ་བླངས་ནས་ཚིག་གིས་སོ་ཞེས༌[^3391]སྨོས་ཏེ། དེ་བླངས་ནས་ཐ་ན་ཞེས་བྱ་བ་ནི་རང་གིས་ཁབ་ལ་སོགས་པའོ། །གང་ལ་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་ལ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྒན་པའི་མཐའ་ལོགས་སུ་འདུག་སྟེ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 4834]
ཚིག་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་བཙུན་པ། རྫས་ཇི་ལྟ་བུས་ཀྱང་དབྱར་གནས་པའི་དགེ་སློང་གི་དགེ་འདུན་ལ་དགག་དབྱེ་བགྱིར༌[^3392]རུང་ངོ་ཞེས་བྱ་བས་སོ། །

[Block 4835]
དེའི་འོག་ཏུ་དགེ་ཚུལ་རྣམས་ལ་དགག་དབྱེ་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ཞེས་བྱ་བ་ནི་རྫས་ཀྱི་དགག་དབྱེ་བྱས་པ་དེའི་འོག་ཏུ༌[^3393]ཏུའོ། །
--- END BLOCKS ---
