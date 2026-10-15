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
[Block 491]
གཟུགས་ལ་སོགས་པའི་དངོས་པོ་ཞེས་བྱ་བ་ནི། མངོན་སུམ་ཉིད༌[^323]དུ་དམིགས་པའོ། །

[Block 492]
ཡོད་པ་མ་ཡིན་པ་ལ་སྒྲོ་འདོགས་པའི་ཉེས་པ་ཇི་སྙེད་པ་དེ་དག་ནི་ཐོག་མ་ཉིད་དུ་དཔྱད་ཅིང་གསལ་བར་བྱས་ལ་དཀྲོལ༌[^324]ཞིང་བསྟན་ཟིན་ཞེས་བྱ་བ་ནི། དུ་མའི་བདག་ཉིད་དུ་ཇི་ལྟར་འགྱུར་ཏེ། བརྗོད་པའི་སྔ་རོལ་ན་ནི་བདག་མེད་ནའོ། །

[Block 493]
དེ་ལས་བརྗོད་པར་ཇི་ལྟར་འབྱུང་སྟེ། རེ་ཞིག་སྔ་རོལ་ན་ནི་བློ་མེད་དེ། བཏགས་པ་ལ་གནས་པའི་དངོས་པོ་ཙམ་གྱི་ངོ་བོ་མེད་པས་བཏགས་པ་དེ་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་མེད་ན། བཏགས་པ་ཡང་ཡོད་དམ་མེད་པ་ཞིག་ཅེ་ན། བཏགས་པ་ཡོད་པ་ཉིད་ན་ནི་བཏགས་པ་ཙམ་གྱི་དངོས་པོར་ཡོད་དོ་ཞེས་སྦྱར་བར་མི་བྱ་སྟེ། དེ༌[^325]ཡོད་པའི་ཕྱིར་རོ། །

[Block 494]
ཡང་ན་བཏགས་པར་ཡོད་པ་དེ་ཡང་མེད་དོ་ཞེས་བྱ༌[^326]ཟེར་ན་ནི་དེ་ཁོ་ན་ཉིད་དང་བཏགས་པ་ཙམ་ལ༌[^327]ཡང་སྐུར་པ་བཏབ་པར་འགྱུར་རོ། །

[Block 495]
བཏགས་པ་དང་དེ་ཁོ་ན་ཉིད་ལ་སྐུར་པ་འདེབས་པ་དེ༌[^328]ནི།

[Block 496 [VERSE]]
མེད་པ་པའི་གཙོ་བོར་རིག་པར་བྱའོ། །
ཕུང་བར་མི་བྱེད་ཅིང་ཞེས་བྱ་བ་ནི།
ངན་སོང་དག་ཏུ་ལྟུང་བར་མི་བྱེད་པའོ། །

[Block 497]
སླུ་བར་མི་བྱེད་ཅེས་བྱ་བ་ནི། བདེ་འགྲོར་འགྲོ་བ་ལས་སོ། །

[Block 498]
ཆོས་ལ་འགོད་པར་བྱེད་ཅེས་བྱ་བ་ནི། སྦྱིན་པ་ལ་སོགས་པ་ལའོ། །

[Block 499]
བདེན་པ༌[^329]ལ་ཡང་འགོད་པར་བྱེད་ཅེས་བྱ་བ་ནི། ཀུན་རྫོབ་ཀྱི་བདེན་པའམ། ཡང་ན་དོན་དམ་པའི་བདེན་པ་ལ་ཡང་སྟེ་རིམ་གྱིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 500]
བསླབ་པའི་གཞི་དག་ལ་ཡང་གཡེལ་བར་མི་འགྱུར་ཞེས་བྱ་བ་ནི། ལས་དང་ལས་ཀྱི་འབྲས་བུ་ཉམས་པར་མི་བྱེད་པའོ། །

[Block 501]
གང་གིས་སྟོང་པ་ཞེས་བྱ་བ་ནི། ཀུན་དུ་བརྟགས་པའི༌[^330]ངོ་བོ་བརྟགས་པ༌[^331]ཙམ་མོ། །

[Block 502]
གང་གིས་གང་སྟོང་པ་ཞེས་བྱ་བ་ནི། གང་གིས་སྟོང་པ་ཉིད༌[^332]དེ་ཁོ་ན་དེ་ཡང་མི་བདེན་པའི་ངོ་བོ་ཉིད་དེ། ཀུན་དུ་བརྟགས་པའི༌[^333]ངོ་བོ་ཡང་བསལ་ལ། གང་སྟོང་པའི་ངོ་བོ་ནི་དེའི་རང་བཞིན་ཉིད་དེ། སྟོང་པ་ཉིད་ཅེས་བརྗོད་དོ། །

[Block 503]
ཐམས་ཅད་མེད་ན་ནི་གང་དུ་ཅི་ཞིག་གང་གིས་སྟོང་པར་འགྱུར་ཏེ་ཞེས་བྱ་བ་ལ། གང་དུ་ཞེས་བྱ་བ་ནི་གཟུགས་ལ་སོགས་པར་རོ། །

[Block 504]
ཅི་ཞིག་ཅེས་བྱ་བ་ནི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 505]
གང་གིས་ཞེས་བྱ་བ་ནི་ཀུན་དུ་བརྟགས་པའི༌[^334]ངོ་བོས་སོ། །

[Block 506]
དེས་དེ་ཉིད་སྟོང་པ་ཉིད་དུ་འགྱུར་དུ་མི་རུང་ངོ་ཞེས་བྱ་བ་ལ། དེས་ཞེས་བྱ་བ་ནི་ཀུན་ཏུ་བརྟགས་པའི༌[^335]ངོ་བོ་དེས་སོ། །

[Block 507]
དེ་ཉིད་ཅེས་བྱ་བ་ཡང་ཀུན་དུ་བརྟགས་པ༌[^336]དེ་ཉིད་དོ། །

[Block 508]
གང་གི༌[^337]ཕྱིར་གང་ལ་གང་མེད་པ་དེ་ནི་དེས༌[^338]སྟོང་པར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་མཐོང་བ༌[^339]ཞེས་བྱ་བ་ནི། དེ་ནི་ཡོད་པ་མ་ཡིན་པ་ལ་ཡང་སྒྲོ་མི་འདོགས་ལ། ཡང་དག་པ་ལ༌[^340]སྐུར་པ་མི་འདེབས་སོ་ཞེས་བྱ་བ་སྟེ། བཏགས་པའི་ཚིག་གི་བདག་ཉིད་ཀྱི་སྒྲོ་འདོགས་པ་དང་། ཡང་དག་པ་ལ་སྐུར་པ་མི་འདེབས་པའོ། །

[Block 509]
དེ་ལ་དངོས་པོ་ནི་གཟུགས་ལ་སོགས་པ་ལ་གཟུགས་ཞེས་བྱ་བ་ལ་སོགས་པར་བཏགས༌[^341]པ་ཙམ་པས་དེས་ན་འདི་ལྟར་ལྷག་པར་ཡང་མི་བྱེད་ལ་ཉུང་བར་ཡང་མི་བྱེད་དོ། །

[Block 510]
འདོར་བར་ཡང་མི་བྱེད་ལ་སྣོན་པར་ཡང་མི་བྱེད་དོ་ཞེས་བྱ་བའོ།

[Block 511]
[^342] །ཐམས་ཅད་དུ་དབང་ཐོབ་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བ་ལ། ཐམས་ཅད་ཅེས་བྱ་བ་གང་ཞེ་ན། ཕྱི་རོལ་གྱི་དངོས་པོ་ཤེས་བྱ༌[^343]དང་ནང་གི་བདག་ཉིད་ཅན་ཞེས་བྱ་བའོ། །

[Block 512]
དེ་ལ་ཕྱི་རོལ་གྱི་དངོས་པོ་ནི་རྣམ་པ་གཉིས་ཏེ། ཡོད་པའི་དངོས་པོ་འབྱུང་བ་ལ་དབང་བསྒྱུར་བ༌[^344]དང་ཡོད་པའི་དངོས་པོ་ལས་གཞན་པ་ལ་དབང་བསྒྱུར༌[^345]བའོ། །

[Block 513]
ནང་གི་བདག་ཉིད་ཅན་ཡང་རྣམ་པ་གཉིས་ཏེ། ཇི་སྲིད་དུ་འདོད་པ་དེ་སྲིད་གནས་པ་དང་གནོད་པ་མེད་པར་དགའ་མགུར་འཆི་འཕོ་བ་ལ་ཡང་ཞེས་བྱ་བའོ། །

[Block 514]
བྱ་བ་དེ་དག་ཀྱང་གང་ཞེ་ན་ཞེས་བྱ་བ་ནི་བྱ་བ་རྣམས་ཀྱི་བསྡུས་པའི་དོན་ཞེས་བྱ་བའི་དོན་ཏེ། རེ་ཞིག་དང་པོ་ནི་བདག་གི་བདེ་བ་ཀུན་ནས་ཉོན་མོངས་པ་ཅན་ནོ། །

[Block 515]
དེ་བཞིན་དུ་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པའི་བྱ་བ་ཡང་རྣམ་པ་བཞི་སྟེ། བྱེད་པ་ནི་བྱ་བའོ། །

[Block 516]
བདག་གི་རྒྱུད་ཡོངས་སུ་སྨིན་པ་དང་། གཞན་གྱི་རྒྱུད་ཡོངས་སུ་སྨིན་པ་དང་། དམ་པའི་ཆོས་གཟུང་བ་དང་། དེའི་མི་མཐུན་པའི༌[^346]ཕྱོགས་ཕས་ཀྱི་རྒོལ་བ་རྣམ་པར་ཚར་གཅོད་པའོ། །

[Block 517]
དེ་ཁོ་ནའི་དོན་རིམ་པར་ཕྱེ་ན་བསྡུས་པ་དང་། དགོས་པ་དང་། གོ་རིམ་མོམོ། །

[Block 518]
བདེ་བ༌[^347]བསྡུས་པ་ནི་འདི་ལྟར་རེ་ཞིག་ལེའུ་འདིས་བསྡུས༌[^348]པ་ནི། འདི་ཞེས་བྱ་བའམ། དོན་བསྡུས་པ་ནི་འདི་དག་གོ་ཞེས་བསྟན་ཏོ། ། ཅིའི་ཕྱིར་དོན་བསྡུས་པ་འདི་དག་གོ་ཞེས་བསྟན་ཞེ་ན།

[Block 519 [VERSE]]
དགོས་པ་བརྗོད་པར་བྱ་བའོ། །
གོ་རིམ་གང་ཞེས་བྱ་བས་ནི།
གོ་རིམ་བརྗོད་པར་བྱ་བའོ། །

[Block 520]
དང་པོ་རེ་ཞིག་ཁོ་ནའི་དོན་གྱིས་བསྡུས་པའི་དོན་ནི་རྣམ་པའི་བྱེ་བྲག་གིས༌[^349]རྣམ་པར་གཞག་པ༌[^350]སྟེ། དེ་ཁོ་ན་དེའི་དོན་ནི་གང་། གང་གི་ཞེས་བྱ་བ་ལ། ཡང་དག་པར་མཐོང་བའི་དོན་ཏེ། གང་གི་ཞེས་བྱ་བ་འདིས་ནི་ཇི་སྙེད་ཡོད་པའིའོ། །

[Block 521]
དེ་ཁོ་ན་དེའི་དོན་ནི། གང་ཞེས་བྱ་བས་ནི་ཇི་ལྟར་ཡོད་པ་ཡང་དག་པར་བསྟན༌[^351]ཏོ། །

[Block 522]
རྣམ་པའི་བྱེ་བྲག་བསྟན་པ་རྣམས་ཇི་ལྟ་བ་བཞིན་དེ་དག་རྟོགས་ཤེ་ན། མངོན་པར་རྟོགས་པའི་ཐབས་ཀྱིས༌[^352]ཚིག་དེ་དག་གིས་རྟོགས་ཏེ། ཐོས་པ་དང་བསམ་པ་དང་བསྒོམ་པ་དག་གིས་ཏེ། འཇིག་རྟེན་ལ་གྲགས་པའི་དེ་ཁོ་ན་ནི་ཐོས་པས་རྟོགས་ཏེ། འཇིག་རྟེན་པ་ཐམས་ཅད་དག་གིས་དངོས་པོ་གང་ལ་བརྡ་དང་ཀུན་རྫོབ་དང་འདྲིས་པའི་རྗེས་སུ་འགྲོ་བས་ཞུགས་པའི་བློས། ལྟ་བ་མཚུངས་པར་འགྱུར་ཏེ།[^353] མདོར་བསྡུས་ནས་ཀུན་རྫོབ་ཏུ་འདི་ནི་འདི་ཡིན་གྱི། འདི་ལྟར་འདི་ནི་གཞན་དུ་མ་ཡིན་ནོ་ཞེས་ངེས་པར་མོས་པའི་སྤྱོད་ཡུལ་གང་འཇིག་རྟེན་པའི་དངོས་པོ་ཐམས་ཅད་གཅིག་ནས་གཅིག་ཏུ་འོངས་པའི་མིང་གིས་རང་གི་རྣམ་པར་རྟོག་པ༌[^354]ལ་གྲགས་པ་མ་ཡིན་པས། མ་དཔྱད་མ་བརྟགས་པར་བཟུང་བའི༌[^355]མོས་པས་འཇིག་རྟེན་པའི་གྲགས་པ་ལས་དེ་ཁོ་ན་ཞེས་བྱ་བའི་ཚིག་ལས་གཅིག་ནས་གཅིག་ཏུ་འོངས་པའི་མིང་ཐོབ་པ་ཉིད་ནི་ཐོས་པས་འཐོབ་པའོ།[^356] །

[Block 523]
རིགས་པའི་གྲགས་པའི་དེ་ཁོ་ན་ནི། དམ་པ་རིགས་པའི་དོན་ལ་མཁས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཞེས་བྱ་བ་སྨྲས་ནས། མངོན་སུམ་དང་རྗེས་སུ་དཔག་པ་དང་ཡིད་ཆེས་པའི་ལུང་གི་ཚད་མ་ལ་བརྟེན་ནས། ལེགས་པར༌[^357]དཔྱད་ཅིང་ངེས་པའི་ཤེས་པའི་སྤྱོད་ཡུལ་གྱི་ཤེས་བྱའི་དངོས་པོ་འཐད་པ་སྒྲུབ་པའི་རིགས་པས་རབ་ཏུ་བསྒྲུབས་ཤིང་རྣམ་པར་གཞག་པ་དེ་ནི་འདི་སྐད་དུ་བརྗོད་དེ། རིགས་པས་གྲགས་པའི་དེ་ཁོ་ན་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 524]
ཉོན་མོངས་པའི་སྒྲིབ་པ་རྣམ་པར་དག་པའི་ཤེས་པའི་སྤྱོད་ཡུལ་གྱི་དེ་ཁོ་ན་དང་ཤེས་བྱའི་སྒྲིབ་པ་རྣམ་པར་དག་པའི་ཤེས་བྱའི༌[^358]སྤྱོད་ཡུལ་གྱི་དེ་ཁོ་ན་ནི་བསྒོམས་པས་རྟོགས་པར་བྱ་བ་སྟེ། གཉི་ག་ཡང་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དེ་ཐོབ་པར་བྱེད་པའི་ཐབས་ཉེ་བར་བསྟན་པས་ཤེས་པར་བྱ་བ་སྟེ། ཕུང་པོ་ལས་མ༌[^359]གཏོགས་པའི་གང་ཟག་མེད་པར་ལྟ་བ་གོམས་པ་ལས་བྱུང་ངོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །ཤེས་བྱའི་སྒྲིབ་པ་རྣམ་པར་དག་པའི་ཤེས་པའི་སྤྱོད་ཡུལ་གྱི་དེ་ཁོ་ན་རྣམ་པར་གཞག་པ་ནི་གཉིས་སུ་མེད་པའི་རང་བཞིན་ཏེ། དེ་ཁོ་ན་དེ་བསྒྲུབ་པ་ནི་གཉིས་སུ་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་ཡེ་ཤེས་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏེ། བསྒོམས་པས༌[^360]རྟོགས་པར་བྱ་བའི་ཤེས་བྱའི་སྒྲིབ་པ་རྣམ་པར་དག་པའི་ཤེས་པའི་སྤྱོད་ཡུལ་གྱི་དེ་ཁོ་ན་རྣམ་པར་གཞག་པ་ནི་གཉིས་སུ་མེད་པའི་རང་བཞིན་ཏེ། དེ་ཁོ་ན་དེ་བསྒྲུབ་པ༌[^361]ནི་གཉིས་སུ་མེད་པ་རྣམ་པར་གཞག་པས་སོ། །

[Block 525]
དབུ་མའི་ལམ་མཐའ་གཉིས་སྤངས༌[^362]པ་བླ་ན་མེད་པ་ཞེས་བྱ་སྟེ་ཞེས་བྱ་བས་ནི་གསུང་རབ་ཀྱི་དོན་གྱི་དབུ་མའི་ལམ་བསྟན་པས་དོན་ཆེན་པོ་ཉིད་གསལ་བར་བྱས་པའི་གོང་ན་མེད་པའི་རྒྱུ་ཡང་དག་པར་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 526]
གཉི་ག་དག་གི་རྒྱུ་སྟེ། གང་གི་ཕྱིར་དེ་ཁོ་ན་དེ་ལ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་ཡེ་ཤེས་ཤིན་ཏུ་རྣམ་པར་དག་པར་རིག་པར་བྱའོ་ཞེས་བརྗོད་པས་དེ་ལྟ་བུའི་རྒྱུ་རྣམས་ཀྱི༌[^363]གོང་ན་མེད་པ་ཉིད་དོ། །

[Block 527]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ནི་ཡང་སློབ་པའི་ལམ་གྱིས་རབ་ཏུ་ཕྱེ་བ་ཡིན་པར་རིག་པར་བྱ་སྟེ་ཞེས་བྱ་བའི་ཚིག་གིས་ནི་གོང་ན་མེད་པ་གཉིས་པ༌[^364]ཉིད་ཀྱི་རྒྱུ་སྟེ། གང་གི་ཕྱིར་ཡང་དེའི་རྒྱུ་ཡིན་པས་ཤེས་རབ་དེ་ནི་བྱང་ཆུབ་སེམས་དཔའི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཐོབ་པར་བྱ་བའི་ཐབས་ཆེན་པོ་ཡིན་ཏེ། ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཐོབ་པའི༌[^365]ཐབས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 528]
འདིའི་སློབ་པའི་ལམ་གྱིས་རབ་ཏུ་ཕྱེ་བའི་བླ་ན་མེད་པ་ཉིད་ནི་དེའི་ཐབས་ཆེན་པོ་ཉིད་དོ། །

[Block 529]
རབ་ཏུ་བསྒྲུབ་པ༌[^366]ནི་དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པའི་གཞུང་གིས་བསྟན་ཏོ། །

[Block 530]
འདི་ལྟར་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཡོངས་སུ་སྨིན་པར་འགྱུར་ལ། འདི་ལྟར་ཐབས་འདིས་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཡོངས་སུ་སྨིན་པར་འགྱུར་བ་དེས་ན་གང་གི་ཕྱིར་གཞན་དུ་མ་ཡིན་པས་མི་མཐུན་པ་དང་གཉེན་པོའི་དངོས་པོ་རབ་ཏུ་བསྒྲུབ་པས་མཐའ་གཅིག་ཏུ་བྱས་པའི་དོན་ཏེ། སྟོང་པ་ཉིད་མཆོག་ལ་མོས་པ་བསྒོམ་པ་ཇི་སྙེད་པ་དེ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སློབ་པའི་ལམ་གྱིས་བསྡུས་པའི་ཐབས་ཆེན་པོ་ཞེས་བརྗོད་དེ་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
