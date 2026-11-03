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
[Block 5461]
འདི་ལྟར་བུམ་པ་ལ་སོགས་པ་ལ་གློ་བུར༌[^3476]གྱི་དབྱེ་བ་མ་མཐོང་བའི་ཕྱིར། ཇི་ལྟར་ནམ་མཁའ་ལྟ་བུའོ། །

[Block 5462]
འོན་ཀྱང་ལྷག་མ་ནི་སྐྱེ་བ་གཞན་ལ་གོམས་པའི་ཁྱད་པར་ཡིན་ཏེ། དེ་བས་ན་འཇིག་རྟེན་ཕ་རོལ་ཡོད་དོ། །

[Block 5463]
སྐྱེས་མ་ཐག་ཏུ་སེམས་ཅན་གྱི་སྐྱེ་བའི་རྒྱུ་སྲེད་པས་བྱས་པའི་བྱ་བ་ལ་འཇུག་པར་སྣང་བ་ལས་བརྩམས་ཏེ། བློའི་མཐུ་སྟོབས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5464]
བློའི་མཐུ་སྟོབས་ཞེས༌[^3477]བྱ་བ་ནི། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 5465]
བླུན་པའི་དབང་པོ་རྣམས་ཀྱང་ཞེས་བྱ་བ་ནི་དབང་པོ་ལྔའི་རྣམ་པར་ཤེས་པའོ། །

[Block 5466]
མ་བསྟན་པར་ཞེས་བྱ་བ་ནི་གཞན་གྱིས་བསྟན་པ་མེད་པར་རོ། །

[Block 5467]
བཙས་མ་ཐག་ཏུ་ཞེས་བྱ་བ་ནི་སྐྱེས་མ་ཐག་ཏུའོ། །

[Block 5468]
བློའི་མཐུ་སྟོབས་གསལ་བ༌[^3478]མེད་ཅེས་བྱ་བ་དེ་བསྒྲུབ་པའི་ཕྱིར། ཁ་ཟས་ཟ་བར་རྩོལ་བར་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། དང་པོའི་ཆོས་བསྒྲུབ་པར་བྱའོ། །

[Block 5469]
སྲིད་པ་གཞན་ལ་ཁ་ཟས་ཟ་བར་རྩོལ་བར་བྱས་པ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། གཞན་གྱིས༌[^3479]བསྟན་པ་མེད་པར་སྐྱེས་མ་ཐག་ཏུ་ནུ་ཞོ་འཐུང་བར་རྩོལ་བར་སྣང་བའི་ཕྱིར་ཏེ། གོམས་པའི་ཆོས་རྣམས་ལ་འབད་པ་མེད་པར་འཇུག་པ་བཞིན་ནོ། །

[Block 5470]
གལ་ཏེ་རྩོལ་བ་མེད་པར་བྱ་བ་ལ་འཇུག་པ་མེད་དེ། སྲིད་པ་གཞན་ལ་གོམས་པའི་བྱ་བ་མེད་པར་མི་འབྱུང་བ་ཡིན་ནོ་ཞེ་ན་ནི་པདྨ་རྣམས་ཀྱང་ཁ་བྱེ་བ་དང་། ཟུམས་པ་དག་སྲིད་པ་གཞན་ལ་གོམས་པའི་རྒྱུ་དང་བཅས་པར་ཁྱེད་ཀྱི་གཞུང་ལ་གྲུབ་པར་འགྱུར་རོ། །

[Block 5471]
འོན་ཏེ་དེ་ལྟར་མི་འདོད་ན་ནི་ཞེས་བྱ་བ་ནི་དེ་དག་དེ་ལྟ་མ་ཡིན་པ་ལྟ་ན་ནི་སྲིད་པ་གཞན་ལ་གོམས་པར་བྱས་པའི་རྟགས་ཀྱིས་སྐྱེས་མ་ཐག་ཏུ་ཡང་ནུ་ཞོ་འཐུང་བ་རྩོལ་བ་མི་འགྲུབ་པའོ།[^3480] །ལན་དུ་དུས་ངེས་པ་དང་། མ་ངེས་པ་ལས་འགྱུར་བར་སྣང་སྟེ། ནུབ་མོ་ཁ་འབྱེ་བ་མ་ཡིན་ཏེ། ནུབ་མོ་ཁ་ཟུམས་ཤིང་ཉིན་པར་ནི་སྦ་བ་ཡིན་ཏེ། དེ་བས་ན་པདྨ་ཁ་བྱེ་བ་དང་། ཟུམས་པ་ནི་དུས་ངེས་པར་སྣང་ལ། དེ་ལྟར་བྱིས་པའི་རྩོལ་བ་ནི་མི་སྣང་ངོ་། །པདྨ་ལ་ནི་ཉི་མའི་འོད་ཟེར་འབབ་པའི་རྒྱུས་པདྨ་ཁ་འབྱེ་བ་ཡིན་གྱི། བྱིས་པ་ནུ་ཞོ་འཐུང༌[^3481]བའི་རྩོལ་བ་ནི། རང་གིས་བྱས་པར་སྣང་བ་ཡིན་ཏེ། དེ་བས་ན་མི་འདྲ་བ་ཉིད་དོ། །

[Block 5472]
ལོག་པར་ལྟ་བ་ལ་བློ་ཞེན་ཅིང་ཞེས་བྱ་བ་འདིས་ནི། བསམ་པ་ཉམས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5473]
སྡིག་ཆེ་བས་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་ཉམས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5474]
སྤྱི་བརྟོལ་ཆེ་བ་ལ་གོམས་ཤིང་འཛེམ་དོགས༌[^3482]མེད་ལ་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་ཉམས་པ་དེ་ཉིད་སྟོན་པ༌[^3483]ཡིན་ནོ། །

[Block 5475]
ལོག་པར་ལྟ་བའི་དུག་གི་སྒྲེགས་པ་དང་འདྲ་བར། །ཞེས་བྱ་བ་ནི་བསམ་པ་ཉམས་པའི་རྒྱུ་ཉིད་དོ་ཞེས་བསྟན་པ་དེ་ཉིད་དོ། །

[Block 5476]
བཞི་པོ་འདི་དག་དང་ལྡན་པའི་བསམ་པ་ཉམས་པ་ལ་ནི་སྦྱིན་པའི་དངོས་པོ་མ་ཚང་བ་ཉིད་དེ། བདག་ཉིད་ངན༌[^3484]པ་ཞེས་བྱ་བ་འདིས་ནི་བསམ་པ་ཉམས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5477]
གང་གི་ཕྱིར་བསམ་པ་ཉམས་ན་ནི། སྦྱིན་པའི་དངོས་པོ་ཡོད་ཀྱང་བུ་ལོན་སྦྱིན་པར་མི་བྱེད་པའོ། །

[Block 5478]
རྒྱུ་གསུམ་གྱིས་ཀྱང་སྦྱིན་པ་སྦྱིན་པར་མི་བྱེད་དེ། སྐྱེས་ཤིང་སྐྱེས༌[^3485]ཤིང་ནོར་ཟ་བ་དང་། ནོར་བསྐྱེད་པ༌[^3486]ལ་མཁས་པ་དང་། མཁས་པ་ཡིན་ཡང་ལེ་ལོ་དང་ལྡན་པའོ། །

[Block 5479]
དེ་ཉིད་ཟད་པའི་མཐའ་ཞེས་བྱ་བ་ནི་ཕྱིས་མི་འཐོབ་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 5480]
ངོ་ཚ་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཁྲེལ་ཡོད་པ་སྟེ། འཇིག་རྟེན་གྱི་ཁ་ན་མ་ཐོ་བས་འཇིགས་པས་བུ་ལོན་འཇལ་བར་བྱེད་པའོ། །

[Block 5481]
རིགས་བཙུན་ཞིང་ཡོན་ཏན་དང་ལྡན་པ་གང་ཡིན་པ་དེ་ནི་རིགས༌[^3487]བཙུན་ཞིང་ཡོན་ཏན༌[^3488]དང་ལྡན་པའོ། །

[Block 5482]
རིགས་བཙུན་ཞེས་སྨོས་པས་ནི་བརྐམ་པའི་ཉེས་པ་མེད་པར་སྟོན༌[^3489]ཏེ། ཆེ་བ་ཉིད་དང་མཐུན་པར་སྤྱོད་པའི་ཕྱིར་རོ། །

[Block 5483]
ཡོན་ཏན་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་ལེ་ལོའི་གཉེན་པོ་སྟེ། ལེ་ལོ་མེད་པའོ། །

[Block 5484]
མཁས་པ་ལ་ནི་མི་མཁས་པའི་གཉེན་པོའོ། །

[Block 5485]
དབེན་ཡང་ཞེས་བྱ་བ་ནི་མངོན་སུམ་མ་ཡིན་པར་ཡང་དེ་ལ་འཇལ་བར་བྱེད་དེ། དེ་ལ་དབུལ་བ་ཡིན་པས་འཇལ་བ་སྟེ། གང་གི་ནོར་གང་ཡིན་པ་དེའི་ནོར་འཇལ་བ་དེ་ནི༌[^3490]དབུལ་པོའོ། །

[Block 5486]
ལྟ་བ་ངན་པ༌[^3491]སྤྱོད་པ་ཞེས་བྱ་བ་འདིས་ནི་བསམ་པ་དང་། སྦྱོར་བ་རྒུད་པ་ཉིད་དུ་སྟོན་ཏེ། [^3492]འདིས་ནི་རང་བཞིན་ངན་པ་ཞེས་བྱ་བ་དེ་བསྟན་ཏོ། །

[Block 5487]
མི་བཟད་པའི་བདག་གི་ལས་ཞེས་བྱ་བ་ནི་མི་དགེ་བའི་ལས་ཀྱི་ལམ་མོ། །

[Block 5488]
སེམས་ཉམས་ཞེས་བྱ་བ་ནི་ཡིད་སྡུག་བསྔལ་གྱིས་ཉེན་པའོ། །

[Block 5489]
ནད་ཀྱིས་གདུངས་པ་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་སྡུག་བསྔལ་གྱིས་གདུངས་པའོ། །

[Block 5490]
དེ་ལ་ཉི་ཟླའི་འོད་ཟེར་ཞེས་བྱ་བ་དང་། མེད་པར་ལྟ་བ་ཚེ་རབས༌[^3493]ཕྱི་མ་ལ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ནི་གྲང་བའི་དམྱལ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 5491]
མུན་ནག་ཅེས་བྱ་བ་ནི་མུན་ནག་འཁྲིགས་པ་ཉིད་ཀྱིས་གཡོགས་པས་སོ། །

[Block 5492]
དེ་ངེས་པར་གཟུང་བའི་ཕྱིར་མུན་ནག་ཐིབས་པོ་དུ་བ་དཀུ་བའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ།[^3494] །ཡང་སོས་ཞེས་བྱ་བ་ཚ་བའི་དམྱལ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 5493]
མེ་མུར་འབར་བ་དམྱལ་བའི་ནང་ན་གཞན་དག་ནི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། མེ་མར་མུར་ཞེས་བྱ་བ་ནི་ཉེ་འཁོར་བ་ཡིན་ཏེ། སྔར་གཙོ་བོའི་དམྱལ་བ་བཤད་ནས། ཕྱིས་ཕྱི་རོལ་གྱི་ཉེ་འཁོར་གྱི་དམྱལ་བ་བསྟན་པའོ། །

[Block 5494]
ཉེ་འཁོར་བ་དེ་ཡང་རྣམ་པ་བཞི་སྟེ། །མེ་མར་མུར་དང་། རོ་མྱགས་ཀྱི་འདམ་དང་། སྤུ་གྲིའི་ལམ་དང་། ཆུ་བོ་རབ་མེད་དེ་བཞི་པོ་དེ་ལས་ཉེ་འཁོར་བའི་དམྱལ་བ་མེ་མར་མུར་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 5495]
དེ་ལས་ཐར་པར་འདོད་པ་ནི་དེ་འདོད་པའོ། །

[Block 5496]
དེས་ན་ཐིག་ནག་ཅེས་བྱ་བའི་དམྱལ་བ་དེའི་དབང་དུ་བྱས་ནས། ལ་ལ་གཤིན་རྗེའི༌[^3495]གཤེད་མ༌[^3496]མ་རུངས་པས། །[^3497]ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་སྨོས་སོ། །

[Block 5497]
འབར་བའི་མེ་འདྲ་བའི་གླང་དང་། ལྕགས་དེ་གཉིས་ཀྱིས་དབང་མེད་པར་བྱས་པ་ནི། གླང་ལྕགས་མེ་ལྟར་འབར་བས་དབང་མེད༌[^3498]བྱས་པའོ། །

[Block 5498]
བསྡུས་འཇོམས་རི་ཡིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་དམྱལ་བ་བསྡུས་འཇོམས་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པ་སྟེ། བསྡུས་འཇོམས་ཞེས་བྱ་བ་རི་གཉིས་ཕྲད་པ་ནི་བསྡུས་འཇོམས་རིའོ། །

[Block 5499]
དེར་ལུས་གཟིར་བ་གང་ཡིན་པ་དེ་ནི་བསྡུས་འཇོམས་རི་ཡིས་ཁ་ཅིག་ལུས་ཀྱང་གཟིར་བའོ། །

[Block 5500]
དེ་ཡིས་བརྫིས་པ་སྟེ། བསྡུས་འཇོམས༌[^3499]རི་བོས་བརྫིས་པའོ། །
--- END BLOCKS ---
