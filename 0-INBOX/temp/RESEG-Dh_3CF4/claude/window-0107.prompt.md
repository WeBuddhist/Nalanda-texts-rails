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
[Block 3746]
ཡང་ན་སྐྱེས་པར་སྣང་བ་དེ་གང་ཡིན་ཞེ་ན། དགེ་བ་སྟེ་མཁས་པའོ། །

[Block 3747]
དེས་ན་སྐྱེས་བུ་ཡང་མི་མངོན་པ་དེ་ནི་དགེ་བ་ཡིན་ཏེ། མཁས་པ་འང་བདག་ཉིད་ལ་ཕན་པའོ། །

[Block 3748]
འདི་ནི་ཁྲོ་བའི་རང་གི་ངོ་བོའོ། །

[Block 3749]
མ་གྱུར་ཏོ་ཞེས་བྱ་བ་ནི་ཤོར་བར་མ་གྱུར་པའོ། །ཇི་ལྟར་མ་ཤོར་བ་ཡིན་ཞེ་ན། འདོད་པ་ནི༌[^2434]སྤྱོད་པའི་ཉོན་མོངས་པ་སྤངས་པའི་ཕྱིར། ནན་གྱིས་མ་བཏང་བ་སྟེ་ནང་ཉིད་དུ་དེ་འགག་པའོ། །

[Block 3750]
བདག་ལ་གནོད་པ་ཞེས་བྱ་བ་ནི་ལུས་ལ་གནས་ཤིང་བདག་ལ་གནོད་པ་སྟེ། ཁྲོ་བའི་རང་བཞིན་དང་ལས་ལ་ཚིགས་བཅད་བདུན་གྱིས་བསྟན་པ་ལ། སྐྱེས་ན་གང་ཞིག་མི་མངོན་ལ། །ཞེས་བྱ་བའི་ཕྱེད་འོག་མས་ནི་བདག་ལ་གནོད་པའི་ལས་བསྟན་ཏོ། །

[Block 3751]
ཚིགས་བཅད་གཉིས་པས་ནི་དགྲ་དགའ་བར་འགྱུར་བའི༌[^2435]ལས་བསྟན་ཏོ། །

[Block 3752]
གང་ཞིག་སྐྱེས་པར་གྱུར་ན་ནི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་དགེ་བ་སྔ་ན་མེད་པ་མི་བསྒྲུབ་པར་བསྟན་ཏོ། །

[Block 3753]
གང་གི༌[^2436]ཟིལ་ནོན་དགེ་བ་གཏོང༌[^2437]འགྱུར་བ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་སྔར་བསྐྱེད་པའི་དགེ་བ་རྣམས་ཁྲོ་བས་འཇིགས་པར་བསྟན་ཏོ། །

[Block 3754]
གཙུབ་ཤིང་གཙུབས་པས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་གཙུབ་ཤིང་གཙུབས་པ་བཞིན་དུ་ལོག་པར་རྟོགས་པས་བདག་ཉིད་བཅོམ་པར་གྱུར་པ་ཡིན་ནོ། །

[Block 3755]
གལ་ཏེ་གཞན་དག་ལ་གནོད་པ་བྱེད་པར་ནུས་པ་ཡིན་ན་ཡང་དེའི་གྲགས་པ་ཉམས་པར་འགྱུར་རོ་ཞེས་བསྟན་པ་ནི། བདག་ཉིད་འབར་ཞིང་ཚིག་པའི་མེ་འདྲ་བ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ཀྱིས་སོ། །

[Block 3756]
ཁྲོ་བའི་ལས་ནི་འདི་དག་ཏུ་བསྟན་ཏེ། བདག་ལ་གནོད་པ་དང་། སྐྱེས་པར་གྱུར་ན་དགྲ་རྣམས་དགའ་བར་འགྱུར་བ་དང་། སྐྱེས་པ་ཉིད་ཀྱིས༌[^2438]དགེ་བ་མ་སྐྱེས་པ་རྣམས་ཀྱི་བར་དུ་གཅོད་པར་བྱེད་པ་དང་། དེ་རབ་ཏུ་འཕེལ་བས་དགེ་བ་བསྒྲུབ་པ༌[^2439]རྣམས་ཡོངས་སུ་ཉམས་པར་བྱེད་པ་དང་། དེའི་འོག་ཏུ་ལོག་པར་རྟོགས་པ་ལས་འབར་བར་གྱུར་པས་བདག་ཉིད་ཕུང་བར་འགྱུར་བ་དང་། གཞན་དག་ལ་གནོད་པར་བྱེད་པར་ནུས་ཀྱང་རེ་ཞིག་གྲགས་པ་ཉམས་པའི་རྒྱུར་འགྱུར་བ་ཡང་ཡིན་ཏེ། འདི་དག་གིས་ནི༌[^2440]མཐོང་བའི་ཆོས་ཀྱི་ཉེས་དམིགས་བསྟན་ནོ། །

[Block 3757]
ཁྲོ་བ་ལ་ཉེས་དམིགས་ཆེན་པོ་འདི་ལྟ་བུ་གཞན་དག་ཀྱང་ཡོད་དོ༌[^2441]ཞེས་བྱ་བ་ལས་བརྩམས་ནས་མཐོང་བའི་ཆོས་དང་། འཇིག་རྟེན་ཕ་རོལ་གྱི་ཉེས་དམིགས་བསྟན་པའི་ཕྱིར་ཚིགས་བཅད་བཞི་སྨོས་ཏེ། ཁྲོ་བའི་མེ་ཡིས་བཞིན་མདོག་ཅེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་མིང་དང་། གཟུགས་གཉིས་འགྱུར་བའི་སྡུག་བསྔལ་བསྐྱེད་པ་ཡིན་ཏེ། གཉིས་ཀའི་རྒུད་པའི་སྡུག་བསྔལ་བསྟན་པའི་དབང་དུ་བྱས་པའོ། །

[Block 3758]
མཛེས་པར་བྱེད་པའི་རྒྱུ་རྒྱན་གྱིས་བརྒྱན་པར་བྱས་ཀྱང་ལུས་ཀྱི་གཟུགས་མི་མཛེས་པའི་རྒྱུར་གྱུར་པའི་ཕྱིར་དང་། བདེ་བའི་རྒྱུ་མལ་སྟན་བཟང་པོ་ལ་ཉལ་ཡང་སྡུག་བསྔལ་གྱི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3759]
བདག་ལ་ཕན་པའི་དོན་བསྒྲུབ༌[^2442]ཅེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་བདག་ཉིད་ཀྱི་དགེ་བ་སྤངས་ཤིང་མི་དགེ་བའི་རྒྱུ་རྩོམ་པ་ལས་བརྩམས་པ་སྟེ། བདག་གི་ཕན་པ་ནི་བདག་ལ་ཕན་པའོ། །

[Block 3760]
བདག་ལ་ཕན་པ་སྒྲུབ་པ་ནི་བདག་ལ་ཕན་པའི་སྒྲུབ་པའོ། །

[Block 3761]
འདིའི་དོན་ནི་བདག་ལ་ཕན་པ་བསྒྲུབ་པའི༌[^2443]དོན་ནོ། །

[Block 3762]
མི་དགེ་བའི་ལས་ནི་ལམ་ངན་པ་སྟེ། བདག་ལ་ཕན་བསྒྲུབ་པའི་དོན་བརྗེད་པ༌[^2444]ལས་ལམ་ངན་པར་འགྲོ་བའོ། །

[Block 3763]
བདག་ལ་ཕན་པ་སྒྲུབ་པའི་དོན་བརྗེད༌[^2445]ཅིང་ལམ་ངན་པར་འགྲོ་བས་ནི༌[^2446]ཉམས་པར་འགྱུར་ཏེ་ལོག་པའི་ལམ་གྱིས་སོ། །

[Block 3764]
སྒྲུབ༌[^2447]གྲགས་པ་ཉིད་དོན་གྲུབ་པ་ཡིན་པས་གྲགས་པ་དོན་གྲུབ་པའོ།[^2448] །ཡང་ན་གྲགས་པ༌[^2449]གྲུབ་པ་དང༌[^2450]དོན་གྲུབ་པ་དེ་གཉིས་ནི་གྲགས་པ་དོན་གྲུབ་པའོ། །

[Block 3765]
གྲགས་པ་དང་དོན་གྲུབ་པ་ལས་ཉམས་པ་དེས་ན་མི་དགེ་བའི་ལས་ཀྱི་ལམ་རབ་ཏུ་འཇུག་པ་ཉིད་དོ། །

[Block 3766]
གཞན་གྱིས་བཟློག་བཞིན་དུ་ཡང་དེ་ལ་བརྟེན་ཅིང་གྲོགས་བཤེས༌[^2451]དང་། འཁོན༌[^2452]དང་བཅས་པར་འགྱུར་བ་ལས་བརྩམས་ནས། མཛའ་བཤེས་དག་གིས་རབ་ཏུ་གཅུགས༌[^2453]ཀྱང་ཞེས་བྱ་བ་ཡིན་ཏེ། འདིས་ནི་རེ་ཞིག་མཐོང་བའི་ཆོས་ཀྱི་ཉེས་དམིགས་བསྟན་ཏོ། །

[Block 3767]
ད་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཉེས་དམིགས་ཀྱི་དབང་དུ་བྱས་ནས། ཁྲོ་བས་སྡིག་པའི་ལས་ནི་གོམས་བྱས་པས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། སྡིག་པའི་ལས་ནི་གོམས་བྱས་པས། །ཞེས་བྱ་བ་འདིས་ནི་སྡིག་པའི་ལས་བྱས་ཤིང་བསགས་པར་བསྟན་ཏོ། །

[Block 3768]
གནོད་པ་དྲག་པོས་ཤར་གཉེར་གང་ཡིན་པ་དེ་ནི། གནོད་པ་ཆེན་པོ་བྱས་པས་ཤར་གཉེར་བའོ། །

[Block 3769]
འདིས་ནི་གང་སྔར་བསྟན་པའི་དགྲ་རྣམས་དགའ་བར་འགྱུར་ཞེས་བྱ་བ་དེ་སྒྲུབ་པ་ཡིན་ནོ། །

[Block 3770]
ཁྲོ་བ་འདི་ནི་ནང་གི་དགྲ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་གང་སྔར་བསྟན་པའི་གང་ཞིག་སྐྱེས་ན་མི་མངོན་པ། ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གཉིས་ཀྱི་བསྡུས་པའི་དོན་ཡིན་ཏེ། ནང་གི་དགྲར་གྱུར་པ་ནི་སྔར་བཤད་པའི་བདག་ལ་གནོད་པ་ཞེས་བྱ་བའི་རྒྱུར་གྱུར་པས་སོ། །

[Block 3771]
དེ་ཡི་མཐུ་ནི་འཕྲོ་བ་དག །ཅེས་བྱ་བ་ནི་ཕྱི་རོལ་དུ་མི་འཕྲོ་བར་བྱས་པ་སྟེ། དེས་ན་མ་བཏང་བ་ཞེས་བྱ་བའི་ཚིགས་བཅད་དོ། །

[Block 3772]
ཁྲོ་བའི་མེ་ཡིས་བཞིན་མདོག་ཉམས་གྱུར་ན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་བཞིའི་བསྡུས་པའི་དོན་ནི། ཕུང་བར་བྱེད་པའི་དགྲ་བོ་དེ། །ཞེས་བྱ་བའོ། །

[Block 3773]
འདི་ནི་འདིའི་ཚིག་གིས་ནི་ཉེས་དམིགས་ཆེན་པོའི་ཕྱིར་ཚིགས་བཅད་ལྔ་ཡང་ཡིན་ནོ། །

[Block 3774]
ཡང་ན་ཚིགས་བཅད་བཅུ་གཅིག་པོ་ཐམས་ཅད་ལ་བསྡུས་པའི་དོན་གྱི་ཚིགས་བཅད་གཉིས་ཏེ། དང་པོའི་ཚིགས་བཅད་ཀྱི། ཁྲོ་བ་འདི་ནི་ནང་གི་དགྲ། །ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཤེས་ནས་བསྟན་པའོ། །

[Block 3775]
ཁྲོ་བ་དེའི་མཐུ་ནི་འཕྲོ་བ་ཞེས་བྱ་བ་ནི་འཕེལ་བར་མི་གཞུག་ཅིང་ནང་ཉིད་དུ་གནས་པར་བྱ་བ་སྟེ། དེ་བས་ན། ཁྲོ་བ་གཡོས་ཀྱང་མ་ཤོར་ཏོ། །ཞེས་བྱ་བ་ནི་ཕྱི་རོལ་ཏུ་མ་ཤོར་ཏོ། །

[Block 3776]
དེ་བས་ན་ནང་གི་དགྲར་ཤེས་པའི་ཕྱིར། ཕུང་བར་བྱེད་པའི་དགྲ་བོ་དེ། །ཞེས་བྱ་བ་སྨོས་ཏེ། མཐོང་བའི་ཕྱིར༌[^2454]ཆོས་དང་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཕུང་བར་བྱེད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་ཏེ། གང་སྔར་བཤད་པ་དག་གོ། །

[Block 3777]
ཡལ་བར་འདོར༌[^2455]ཞེས་བྱ་བས་ནི་དེའི་རང་བཞིན་གྱི་རྒྱུ་བསྟན་པ་ཡིན་ནོ། །

[Block 3778]
མ་ཕྲད་པས་ནི་ཁྱོད་ཀྱི་ཡོན་ཏན་མི་ཤེས་བའི་ཕྱིར་རོ། །

[Block 3779]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་གཙུག་ཕུད་བྱང་ཆུབ་ཀྱི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 3780 [HEADING]]
## ངང་པའི་སྐྱེས་པའི་རབས། ^24-0

[Block 3781]
བརྒྱ་སྟོང་ཕྲག་དུ་མ་གྲངས་མང་པོའི་ཞེས་བྱ་བ་ནི། སྟོང་ཕྲག་དུ་མས་རྒྱ་ཆེ་བའི་གྲངས་གང་ཡིན་པ་དེ་ནི་དེའི་བརྒྱ་ཕྲག་དུ་མས་གྲངས་མང་པོའོ། །

[Block 3782]
དེ་བས་ན་ངང་པའི་ཁྱུ་ཆེན་པོ་ཡིན་ནོ། །

[Block 3783]
རིགས་པ་དང་མི་རིགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྐང་གིས་ནི་སྙན་ངག་གི་གཙུག་ལག་ཏུ་བསྟན་པའི་བློན་པོའི་རང་བཞིན་གྱི་ཡོན་ཏན་ཉི་ཤུ་རྩ་ལྔ་དང་ལྡན་པ་སྟེ། བདག་ཉིད་ཀྱི་ཕུན་སུམ་ཚོགས་པ་ཡིན་པར་ཅི་རིགས་པར་གཟུང་ངོ་། །དེ་དག་ལས་ཀྱང་ཁྱད་པར་དུ་གྱུར་པ་སྟེ། དེ་རྣམས་ཀྱི༌[^2456]དཔོན་པོར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3784]
རིགས་པ་དང་མི་རིགས་པ་ཡོངས་སུ་ཤེས་པར་བྱ་བ་ལ་མཁས་པ་ཞེས་བྱ་བ་འདིས་ནི་ཤེས་རབ་ཅན་དུ་བསྟན་ཏོ། །

[Block 3785]
ཡུན་རིང་པོར༌[^2457]ཡང་དྲན་པའི་མཐུ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་ཡུན་རིང་པོར་བྱས་པ་དང་། ཡུན་རིང་པོར་སྨྲས་པ་དང་། ཡུན་རིང་དུ་བསམས་པ་དང་། ཡུན་རིང་དུ་ཐོབ་པ་རྣམས་དྲན་པའོ། །
--- END BLOCKS ---
