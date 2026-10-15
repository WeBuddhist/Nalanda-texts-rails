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
དགེ་འདུན་ལ་འདུན་པ་ལ་སོགས་པ་ཕུལ་བ་ནི་ཕུལ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། གང་ཟག་ལ་འདུན་པ་ལ་སོགས་པའི་ཚིག་ལྷུག་པ་ལས་ཕུལ་བ་གསུངས་པ་ཡིན་ཏེ། དེ་བས་ན་དགེ་འདུན་ལ་ཕུལ་བ་ཉིད་ལ་མ་ཕུལ་བ་ཉིད་དུ་ལ་ལ་ཞིག་དོགས་པར་འགྱུར་པ་དེ་བས་ན། དེ་བཟློག་པའི༌[^3124]དོན་དུ་འདི་གསུངས་པ་ཡིན་ནོ། །

[Block 4482]
དེ་ལས་གང་ཡང་རུང་བས་དེ་བརྗོད་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ལས་ཞེས་བྱ་བ༌[^3125]ནི་དགེ་འདུན་ལས་སོ། །

[Block 4483]
གང་དུ་འདི་ལ་ཕུལ་བ་དེ་ཡོད་པར་འགྱུར་རོ། །

[Block 4484]
དེ་བརྗོད་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལ་འདུན་པ་ལ་སོགས་པ་ཕུལ་བ་དེའོ། །

[Block 4485]
འོ་ན་བརྗོད་པ་འདི་དོན་མེད་པ་ཁོ་ན་ཡིན་ཏེ། འདིར་སྨྲ་བ་པོ་འབྱུང་བ་ནི་མི་རིགས་པ་ཁོ་ན་སྟེ། གང་གི་ཕྱིར་གོ་བ་བསྐྱེད་པའི་དོན་དུ་འདི༌[^3126]ནི་མངོན་སུམ་ཉིད་དུ༌[^3127]ཕུལ་བ་པོས་གོ་བ་བསྐྱེད་དོ་ཞེ་ན། དེ་ནི་བདེན་མོད་ཀྱི་འོན་ཀྱང་ཆོ་ག་ལ་འཇུག་པ་ལ་ཕུལ་བ་མ་བྱས་པ་ཉིད་དོ། །

[Block 4486]
དེ་ལྟ་བས་ན་འདིར་དེ་ཐོབ་པའོ། །

[Block 4487]
མཚམས་ཀྱི་ཕྱི་རོལ་ན་གནས་པས་དེ་འབུལ་བ་དང་འབུལ་དུ་གཞུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་འདུན་པ་ལ་སོགས་པའོ། །

[Block 4488]
མི་ཆགས་པ་མི་བྱའོ་ཞེས་བྱ་བ་དེའི་འདི་སྤྲོས་པ་ཡིན་ནོ། །

[Block 4489]
མཚམས་གཞན་ན་གནས་པ་ནི་གང་ལ་ཡང་ཡན་ལག་ཉིད་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་དེས་འདིར་མི་འཆགས་པ་བྱས་པ་ཉིད་ཡིན་ནོ། །

[Block 4490]
བརྒྱུད་པས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འབུལ་བ་དང་འབུལ་དུ་གཞུག་པར་བྱ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4491]
ལེན་པར་བྱེད་པས་གཞན་ལ་ཕུལ་བ་དེས་ཀྱང་གཞན་ཞིག་ལ་འབུལ་བ་ནི་བརྒྱུད་པ་ཡིན་ནོ། །

[Block 4492]
ན་བ་དང་དབང་མེད་པ་དང་སྲོག་དང་ཚངས་པར་སྤྱོད་པའི་བར་ཆད་ཀྱིས་འཇིགས་པ་ལས་གཞན༌[^3128]པས་འབུལ་བ་ལ་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་འདུན་པ་ལ་སོགས་པ་འདི་རྣམས་གཞན༌[^3129]ལ་འབུལ་བ་ལ་ནི་ཉེས་བྱས་སུ་འགྱུར་ཏེ། འབུལ་བ་མི་འཆགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 4493]
དེ་ཙམ་གྱི་དབང་གིས་དགེ་བའི་ཕྱོགས་ཀྱི་བར་ཆད་འབྱུང་བར་འགྱུར་བ་དེ་ཡང་འདིར་ཚངས་པར་སྤྱོད་པའི་བར་ཆད་ཡིན་པར་རིག་པར་བྱ་སྟེ་ཞེས་བྱ་བའི་སྒྲས༌[^3130]བསྡུས་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 4494]
དེ་ལྟར་ཡང་བཅོམ་ལྡན་འདས་ཀྱི༌[^3131]ཉན་ཐོས་ཀྱི་དགེ་འདུན་ནི་དོན་ཉུང་བ་བྱ་བ་ཉུང་བ་ཡིན་པས་ཞེས་བྱ་བ་ནི་མ་འོངས་པ་ལ་རྒྱུ་བསྟན་པ་ཡིན་ནོ། །

[Block 4495]
དེ་བས་ན་དེ་ཙམ་ཉིད་ཀྱིས་ཀྱང་འདིར་ཕུལ་བ་ཉིད་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 4496]
མ་བརྗོད་ན་ནི་མ་གུས་པ་ལས་སོ་ཞེས་བྱ་བ་ནི་འདུན་པ་ལ་སོགས་པ་བླངས་པ་མ་བརྗོད་ན་ནི་མ་གུས་པའི་ལྟུང་བྱེད་ཀྱི་རྗེས་སུ་མཐུན་པ་ལས་ཉེས་བྱས་སུ་འགྱུར་བའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4497]
དེས་འཇིགས་པས་མཚམས་ཀྱི་ཕྱི་རོལ་ནས་ཁྱེར་ཏེ་འོངས་པ་ལ་ནི་ཉེས་པ་མེད་དོ༌[^3132]ཞེས་བྱ་བ་ལ། དེས་ཞེས་བྱ་བ་ནི་སྲོག་དང་ཚངས་པར་སྤྱོད་པའི་བར་ཆད་ཀྱིས་འཇིགས་པས་དགྲ་དང་ཕྲད་པ་ལ་སོགས་པས་ཡིད་ལ་བྱེད་པ་འཇོམས་པ་གང་ཡིན་པ་དེ་ཡང་འདིར་ཚངས་པར་སྤྱོད་པའི་བར་ཆད་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 4498]
དགེ་སྐོས་ཀྱིས་གསོ་སྦྱོང་གི་ཚེ་ཚུལ་ཤིང་བྲིམ་པས༌[^3133]དགེ་སློང་རྣམས་བགྲང་བར་བྱའོ། །

[Block 4499]
ལེགས་པར་ཐོན་པས་གདོན་ཏེ་ཚིག་ཕྱེད་ཀྱང་མ་འཁྲུལ་བ་ཉིད་ནའོ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་ལའོ། །

[Block 4500]
སོ་སོར་ཐར་པ་བཏོན་པས་ནི་གསོ་སྦྱོང་ལས་བཏོན་པ་ཉིད་དོ། །

[Block 4501]
དེ་བས་ན་སོ་སོར་ཐར་པ་ལས་ཞེས་བྱ་བ་འདིར་སྐྱེས་པ་ཉིད་དོ། །

[Block 4502]
བྱེད་པ་པོ་གང་ལ་བསྟན་པ་འདི་ལས་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་སོ། །

[Block 4503]
མི་ནུས་པ་ཉིད་ཡིན་ན་གཉིས་པའི་འོ་ཞེས་བྱ་བ་ནི་གནས་བརྟན་གྱིས་བཏོན་པའོ། །

[Block 4504]
དེས་ཀྱང་གསུམ་པའི་འོ་ཞེས་བྱ་བ་ནི།

[Block 4505]
གཉིས་པ་དེས་ཀྱང་མི་ནུས་པ་ཉིད་ཡིན་ན་གསུམ་པས་བསྟན་པར་བྱའོ། །

[Block 4506]
དེས་ཀྱང་ན་རེས་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི།

[Block 4507]
གསུམ་པ་དེས་ཀྱང་མི་ནུས་པ་ཉིད་ཡིན་ན་རེས་ཀྱིས་གདོན་པར་བྱའོ། །

[Block 4508]
འདིར་དགེ་འདུན་གྱིས་གནས་བརྟན་ལ་སྟོན་པའི་གནས་པ་ཐོབ་པ་ཉིད་ཇི་ལྟར་ཡང་འདིར་མཐའ་གཉིས་དང་བྲལ་བ༌[^3134]དེ་ལྟར་རྣམ་པར་གནས་པ་དེའི༌[^3135]འོག་ཏུ་ཞེས་བྱ་བ་ལ། གསུམ་པོ་དེ་ལས་འོག་ཏུ་ཚིག་གདོན་པར༌[^3136]མི་ནུས་ནའོ། །

[Block 4509]
མི་ནུས་ན་གཞན་ལ་བཅོལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། རེས་བབ་པའི་ཚེ་འདོན་མི་ནུས་ན་གདོན་པ་གཞན་ལ་བཅོལ་བར་བྱའོ། །

[Block 4510]
མ་བཏུབ་ན་དགེ་འདུན་གྱིས་སོ་ཞེས་བྱ་བ་ནི། མ་བཏུབ་ན་དགེ་འདུན་གྱིས་བཅོལ་བར་བྱའོ།[^3137] །རྟག་ཏུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱིས་བཅོལ་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4511]
རྡུགས་ན་ལྷག༌[^3138]མ་གཞན་གྱིས་སོ་ཞེས་བྱ་བར་སྦྱར་རོ།[^3139] །གདོན་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4512]
དུམ་བུ༌[^3140]འཛིན་པ་ཉིད་ཡིན་ན་ཇི་སྙེད་ཀྱིས༌[^3141]འགྲུབ་པ་དག་གིས་སོ་ཞེས་བྱ་བ་ནི་ཇི་སྙེད་ཀྱིས་གདོན་པ༌[^3142]འགྲུབ་པར་འགྱུར་བ་སྟེ་དེ་སྙེད་ཀྱིས་ནི༌[^3143]རྗེས་སུ་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4513]
འཇིགས་པ་དང་བཅས་པ་ཉིད་ཡིན་ན་གནས་མཛེས་པར་འདོད་པས་གྲོང་དང་མི་ཉེ་བར་གསོ་སྦྱོང་བྱར་མི་རུང་ངོ་ཞེས་བྱ་བ་ནི། སིལ་བུ་དག་ལས་འདི་དང་པོར་བྱས་ཏེ། ཁྱིམ་བདག་དང་རྒྱལ་པོ་དག་ལ་སོགས་པའི་མཐར་ཐུག་པའོ། །

[Block 4514]
གཞན་ནི་ཞུ་བ་ལས་ཏེ། འདི་ནི་ལས་ཀྱི་སྦྱོར་བ་གཞན་ལ༌[^3144]ཡང་དཔེ་ཙམ་དུ་ཟད་དོ། །

[Block 4515]
འགྲོན་པ་མི་སྡོད་ན༌[^3145]འགྲོ་བ་བཞིན་དུ་བྱའོ་ཞེས་བྱ་བ་ནི་མཆོང་བ་བཞིན་དུ་དེ་ཡིད་ལ་འདྲེས་པར་གྱུར་ན། གང་ཞིག་འགྲོ་བའི་བྱ་བ་རྣམས་ཀྱིས་ལས་བྱེད་པའོ། །

[Block 4516]
དེ་ལྟ་བས་ན་མི་སྲིད་པ་ལས་གཞན་དུ་འགྱུར་བ་ཉིད་ལ་དེ་རྗེས་སུ་གནང་བའོ། །

[Block 4517]
སྒྲ་མི་འདོད་ན་མདོར་བསྡུས་པས་སོ་ཞེས་བྱ་བ་ནི། གང་དག་འདིར་སྦྱར་བ་དེ་དག་སྒྲ་མི་འདོད་ན་མདོར་བསྡུས་པས་གསོ་སྦྱོང་བྱ་བའོ།[^3146] །དེ་ཙམ་ཡང་ན་བྱིན་གྱིས་བརླབ་པོ་ཞེས་བྱ་བ་ནི་མདོར་བསྡུས་པས་བྱ་བ༌[^3147]ལ་སྒྲ་ཇི་ཙམ་འབྱུང་བར་འགྱུར་བའི་སྒྲ་དེ་ཙམ་ཡང་འགྲོན་པ་དག་གིས་མི་འདོད་ན་སོ་སོ་ནས་བྱིན་གྱིས་བརླབ་པར་བྱ་སྟེ། འཁོར་དང་བཅས་པ་ལ་སྒྲ༌[^3148]ལས་གྲོལ་བ་མེད་པས་སོ་སོ་ནས་ཞེས་བྱ་བར་བསྒྲུབ་པར་བྱའོ། །

[Block 4518]
དད་པ་ཅན་དང་གཙོ་བོ་དག་དགའ་བར་འགྱུར་བལྟ་ན་ཆོ་ག་རྗེས་སུ་བསྒྲུབ་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་དོ། །

[Block 4519]
དྲུང་དུ་གསོ་སྦྱོང་བྱས༌[^3149]པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། གནས་མལ་གྱི་གཞིར་གཏོགས་པ་ལས་འདིར་གཉིས་པོ་དེ་དག་གྲངས་སོ། །

[Block 4520]
ཕོངས་པའི་ཚེ་ཁྱིམ་པའི་དྲུང་དུ་བཤགས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཆོམ་རྐུན་པ་དག་ལ་དེ་སྐད་གསུངས་པ་ཡིན་མོད་ཀྱི། ཁྱིམ་པ་གཞན་དག་ལ་ཡང་རུང་བ་ཉིད་ཡིན་པའི་ཕྱིར་འདི་རྣམ་པར་གཞག་གོ། །
--- END BLOCKS ---
