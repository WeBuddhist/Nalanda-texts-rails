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
[Block 4306]
དེ་ལས་གཞན་པ་ལས་བརྩམས་པ་ནི་གཉིས་ཏེ། དེ་ལྟ་བས་ན་ལྟ་བ་འདི་དག་གི་གོ་རིམས་ནི་འདི་ཡིན་ནོ། །

[Block 4307]
སྐྱེ་བོ་སྡིག་པ་ཅན་རྣམས་དང་བསྟེན་པ༌[^2759]ཞེས་བྱ་བ་འདིས་ནི་རྐྱེན་བསྟན་ཏོ། །

[Block 4308]
བློ་གཞན་གྱི་དྲིང་ལ་འཇོག་པས་ཞེས་བྱ་བ་འདིས་ནི་རྒྱུ་བསྟན་ཏོ། །

[Block 4309]
ལྟ་བས་བྱས་པ་ཉིད་གཡང་སར་ལྷུང་བ་ཉིད་ཡིན་པས་ལྟ་བ་ངན་པའི་གཡང་སར་ལྟུང་བ་ཞེས་བརྗོད་དོ། །

[Block 4310]
[^2760]ངན་སོང་གི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4311]
དེ་ལ་བརྩེ་བར་གྱུར་ཏེ་ཞེས་བྱ་བའི་རྒྱུའི་དབང་དུ་བྱས་ནས། ཡོན་ཏན་གོམས་པས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4312]
དེ་ལས་བཟློག་པའི་ཐབས་ཞེས་བྱ་བ་ནི་བཟློག་པའི་ཆེད་དུའོ། །

[Block 4313]
དུལ་ཞིང་བརྟན་པ་དང་རྒྱ་ཆེ་བའི་ཆ་བྱད་ཡོད་པའི་སྐྱེ་བོ་གང་ཡིན་པ་དེ་ནི་དུལ་ཞིང་བརྟན་ལ་རྒྱ་ཆེ་བའི་ཆ་བྱད་ཀྱི་སྐྱེ་བོ་སྟེ༌[^2761]ཕྱོགས་ན་འཁོད་པའོ། །

[Block 4314]
སྙན་པར་སྨྲ་བ་དང་། བསྙེན་བཀུར་བ་དང་། སྟན་གདིང་བ་བྱས་པ་ནི་སྙན་པར་སྨྲ་བ་དང་། བསྙེན་བཀུར་བ་དང་། སྟན་གདིང་བ་བྱས་པའོ། །

[Block 4315]
སྙན་པར་སྨྲ་བ་དང་། བསྙེན་བཀུར༌[^2762]དང་། སྟན་གདིང་བ་གང་ཡིན་པ་དེ་ཉིད་ནི། སྙན་པར་སྨྲ་བ་དང་། བསྙེན་བཀུར༌[^2763]དང་། སྟན་གདིང་བ་བྱས་པའོ། །

[Block 4316]
ཨེ་མ་འོ་ཁྱོད་ཀྱི་ཆོས་ལ་དགའ་བ་ལ་ལྟོས་ཞེས༌[^2764]བྱ་བ་ཡིན་ཏེ། དགའ་བ་ནི་ཅིའི་ཕྱིར་ཞེ་ན། དཀའ་ཐུབ་ཀྱི་ནགས་ན་འདུག་བཞིན་དུ་སྤྲེའུ་ཆེན་པོ་མེད་པར་བྱས་པའོ། །

[Block 4317]
ཨེ་མའོ་རྩོལ་ཕོད་ཅེས་བྱ་བ་ནི་སྤྲེའུ་ཆེན་པོ་བསད་པས་སོ། །

[Block 4318]
མཐུ་ཆེ་བ་ཞེས་བྱ་བ་ནི་ནུས་པ་སྟེ། གཅིག་ཏུ་དཀའ་ཐུབ་སྤྱད་པས་ལུས་ཉམ་ཆུང་ཡང་སོང་བའི་ཕྱིར་རོ། །

[Block 4319]
འགྲོ་བའི་ངོ་བོ་ཉིད་ཀྱིས༌[^2765]དེ་བཞིན་ཁྱེད་ཟེར་ན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི་འགྲོ་བ་འདི་དག་ངོ་བོ་ཉིད་ཀྱིས་ཡིན་ན། སྤྲེའུ་བསད་པ་ཡང་ངོ་བོ་ཉིད་ཀྱིས་ཡིན་ནོ། །ཞེས་བྱ་བའི་དབང་དུ་བྱས་ནས། དེ་སྟེ༌[^2766]སྡིག་པ་ཡོད་ན་ནི། །[^2767]ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། གལ་ཏེ་སྡིག་པ་ཡོད་ན་ནི་འགྲོ་བ་འདི་ཉིད༌[^2768]ལ་རྒྱུ་ཡོད་པ་ཉིད་དུ་བསྟན་ཏེ། གྲུབ་པ་ཉིད་ཀྱི་དབང་དུ་བྱས་ནའོ། །

[Block 4320]
དེ་ལ་རེ་ཞིག་དམ་བཅས་པ་དང་། སྡིག་པ་ཡོད་དོ་ཞེས་ཟེར་བ་ནི་ཕན་ཚུན་འགལ་བ་ཉིད་དུ་བསྟན་ནས། ད་ནི་དཔེ་མ་གྲུབ་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། གལ་ཏེ་པདྨའི་སྡོང་བུ་སྐྱེ་ལ་སོགས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4321]
པདྨའི་སྡོང་བུ་སྐྱེ་བ་ལ་སོགས་པ་དེ་རྒྱུ་མེད་པ་ཉིད་ཡིན་ན། ཅིའི་ཕྱིར་རྟག་ཏུ་མི་འབྱུང་། པདྨའི་ལོ་མ་སྐྱེ་བ་ལ་སོགས་པའི་རྒྱུ་ནི་ཅི་ཞིག་ཡིན་ཞེ་ན། ཆུ་ལ་སོགས་པའི་རྐྱེན་ཡོད་པ་དང་། ས་བོན་གྱི་རྒྱུས་བྱས་པ་ཡིན་ཏེ། ཇི་ལྟར་ཤེས་ཤེ་ན། མེད་པ་ལས་བྱུང་བའི༌[^2769]ཕྱིར་ཏེ། ཆུ་ལ་སོགས་པ་ཡོད་པ་དང་། པདྨའི་སྡོང་བུ༌[^2770]ལ་སོགས་པ་ཡོད་པར་འགྱུར་ལ། ཆུ་དང་། ས་བོན་ལ་སོགས་པ་མེད་ན་ནི་མི་འབྱུང་བ་ཡིན་ཏེ། དེ་ནི་གང་གི་ཕྱིར། རྒྱུ་དང་རྒྱུ་ཅན་གྱི་མཚན་ཉིད་གཏན་ཚིགས་ཀྱིས་མཁས་པ་དག་དེ་ལྟར་འདོད་དོ། །

[Block 4322]
གང་ལ་རྒྱུ་མེད་པར་འབྱུང་བ་དང་། གང་འབྱུང་བ་དང་། གང་དུ་མི་འབྱུང་བ་དེ་ནི་རྒྱུ་དང་བཅས་པ་དང་། རྒྱུ་མེད་པ་ཡིན་ཏེ། གང་ཞིག་ཁ་ཅིག་ཏུ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་ཡིན་ཏེ། དེ་ལ་རེ་ཞིག་གང་ཞིག༌[^2771]ཁ་ཅིག་ཏུ་ནི་ཞེས་བྱ་བ་ནི༌[^2772]ཚིགས་བཅད་འདིས་ནི། ཕྱོགས་སྔ་མ་དང་འགལ་བར་བསྟན་ཏོ། །

[Block 4323]
ཚིགས་བཅད་གཉིས་པས་ནི་གྲུབ་པའི་མཐའ་དང་འགལ་བར་བསྟན་ཏོ། །

[Block 4324]
གསུམ་པས་ནི་དཔེ་མ་གྲུབ་པ་བསྟན་ཏེ། རྒྱུ་ཡང་ཡོད་པ་མ་ཡིན་ཞེས་ནི་རྟག་ཏུ་སྨྲ། ཞེས་བྱ་བའི་ཚིགས་བཅད༌[^2773]གསུམ་གྱིས་ནི། རང་གི་གནས་སྐབས་ཀྱི་དབང་དུ་བྱས་པ་སྟེ། མ་མཐོང་བས་ཞེས་བྱ་བ་ནི་མ་ཤེས་པས་སོ། །

[Block 4325]
དེ་ཉིད་ཀྱིས་ཞེས་བྱ་བ་ནི་རྒྱུ་མ་མཐོང་བ་ཉིད་ཀྱིས་སོ། །

[Block 4326]
ཐམས་ཅད་རྒྱུ་མེད་སྨྲ་ན་ནི། །ཞེས་བྱ་བ་ནི་གང་དག་རྒྱུ་མཐོང་བ་དེ་དག་ལ་ཡང་རྒྱུ་མེད་པར་སྟོན་པ་སྟེ། རྒྱུ་དང་བཅས་པར་མངོན་དུ་མཐོང་བཞིན་དུ། །ཞེས་བྱ་བ་ཡིན་ཏེ། གང་དག་རྒྱུ་ཡོད་པ་དེ་དག་ནི་རྒྱུ་ཡོད་པ་ཉིད་དུ་མངོན་སུམ་དུ་དམིགས་པ་ཡིན་ནོ། །

[Block 4327]
དེ་ལ༌[^2774]སྡང་བས་འགལ་བའི་ཚིག་ངན་སྨྲས་པར་འགྱུར། །ཞེས་བྱ་བ་ནི་འགལ་བས་ཚིག་ངན་སྨྲ་བར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་འགལ་བའི་ཚིག་ངན་སྨྲ་བར་འགྱུར་བའོ། །

[Block 4328]
ཚིག་ངན་པ་ནི་འདིར་བདག་གི་དམ་བཅས་པ་ལ་གཟུང་སྟེ། བདག་ཉིད་ཀྱི་དམ་བཅས་པའི་ཚིག་དང་འགལ་ཞེས་བྱ་བའི་དོན་ཏེ། མངོན་སུམ་དང་འགལ་བའོ། །

[Block 4329]
དམ་བཅས་པ་ངན་པ་སྔ་མའི་དོན་རྣམ་པར་བཅད་པའི་ཕྱིར། འགལ་ཞིང་ངན་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4330]
ད་ནི་མངོན་སུམ་དང་འགལ་བ་དམ་བཅས་པ་ངན་པར་བསྟན་ཏོ། །

[Block 4331]
གང་ཞིག་ཁ་ཅིག་ཏུ་ནི་རྒྱུ་རྐྱེན་མ་མཐོང་བས། །ཞེས་བྱ་བ༌[^2775]བསྟན་པ་ལ། ཇི་ལྟར་རྒྱུ་ཡོད་བཞིན་དུ་མ་རྟོགས་པ། །ཞེས་བྱ་བ་ཡིན་ཏེ།

[Block 4332 [VERSE]]
རྒྱུ་ཡོད་བཞིན་དུ་མ་རྟོགས་པ་བསྟན་པའི་ཕྱིར། །
གལ་ཏེ་གང་ནའང་རྒྱུ་ནི་ཡོད་པར་མ་མཐོང་ན། །

[Block 4333]
ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། གང་གི་རྒྱུ་མ་མཐོང་བ་དེ་ལ་འདིར་རྒྱུ་མེད་ཅེས་སྨྲ་བར་མི་རིགས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། ཡོད་བཞིན་དུ་ཡང་རྐྱེན་གཞན་གྱིས་མི༌[^2776]མཐོང་བར་སྣང་སྟེ། ཇི་ལྟར་མཚན་མོ་ཉི་མའི་དཀྱིལ་འཁོར་ཡོད་ཀྱང་ཤིན་ཏུ་སྐལ་བར༌[^2777]གནས་པའི་ཕྱིར། རྐྱེན་གཞན་གྱིས་མ་མཐོང་བ་ཡིན་ཏེ། མི་དམིགས་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 4334]
དེ་དག་རྒྱུ་དང་བཅས་པར་མངོན་དུ་མཐོང་བཞིན་དུ། །ཞེས་བྱ་བ་བསྟན་པ་ལ། ཇི་ལྟར་མངོན་སུམ་དུ་རྒྱུ་དང་བཅས་པ་མཐོང་ཞེས་པ་དེ་བསྟན་པའི་ཕྱིར། ཡིད་དུ་འོང་བའི་ཡུལ་ནི་བདེ་བ་འདོད་པའི་ཕྱིར་ཏེ། རྟེན་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4335]
དེ་དང་འགལ་བ་ལ༌[^2778]ནི་བདེ་བ་དང་འགལ་བ་སྟེ། ཡིད་དུ་མི་འོང་བའི་ཡུལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4336]
དེའི་ཕྱིར་ཡང་། རྒྱལ་པོ་དག་ལ་རྟེན་པར་བྱེད། ཅེས་བྱ་བ་ནི་ཡིད་དུ་འོང་བའི་ཡུལ་ལ་བརྟེན་པའོ། །

[Block 4337]
ཡང་ན་བདེ་བ་འདོད་པའི་ཕྱིར་རོ། །

[Block 4338]
དེའི་ཕྱིར་དེ་ལ་སྡང་བས་འགལ་བའི་ཚིག་ངན་སྨྲས་པར་གྱུར་པའོ། །

[Block 4339]
དེ་བསྟན་པའི་ཕྱིར།[^2779] གལ་ཏེ་དངོས་པོ་རྣམས་དེ་ལྟ་ཡིན༌[^2780]ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། དེ་ལྟ་ཡིན་ན༌[^2781]ཞེས་བྱ་བ་ནི་རྒྱུ་དང་ལྡན་པ་ཡིན་ན་ཕྱོགས་མ་གྲུབ་པ་ཡང་ཡིན་པས། དངོས་པོ་རྣམས་ཀྱི་རྒྱུ་ཁས་མི་ལེན་པ་སྟེ། སྤྲེའུ་བསད་པ་ལ་ཉེས་པ་མེད་པའི་མཇུག༌[^2782]བསྡུ་བའི་ཕྱིར། གལ་ཏེ་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་རྒྱུ་སྟེན་པ༌[^2783]ཡིན་ནོ། །

[Block 4340]
གལ་ཏེ་ཞེས་བྱ་བ་ནི་དངོས་པོ་རྣམས་རྒྱུ་དང་ལྡན་པ་ཉིད་དུ་གྲུབ་ཀྱང་། ཇི་ལྟར་དངོས་པོ་གཞན་རྒྱུ་མེད་པ་དེ་བཞིན་དུ་སྤྲེའུ་བསད་པ་ལ་ཡང་རྒྱུ་མེད་པ་ཡིན་ཏེ། དེ་ལྟ་ཡིན་ན་ནི༌[^2784]ཅིའི་ཕྱིར་བདག་ལ་སྨོད་པར༌[^2785]བྱེད་ཅེས་པའོ། །

[Block 4341]
ཁྱོད་ནི་ཇི་ལྟར་བདག་ལ་སེམས་མི་དགའ། །ཞེས༌[^2786]བྱ་བ་ལ། སེམས་མི་དགའ་བ་དེ་ཉིད་བསྟན་པའི་ཕྱིར། གཞན་གྱི་ཉེས་པ༌[^2787]བདག་ལ་ཅི་ཕྱིར༌[^2788]བསྒོ།[^2789] །ཅེས་བྱ་བ་ཡིན་ཏེ། གཞན་གྱི་ཉེས་པ་ནི་དབང་ཕྱུག་གི་ཉེས་པས་སོ། །

[Block 4342]
སྡིག་པ་ཆེན་པོ་མ་ལུས་པ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི། སྤྲེའུ་བསད་པས་ནི་སྡིག་པ་ཉིད་དུ་ཁས་ལེན་པའི་ཕྱོགས་སྔ་མ་དང་འགལ་བའི་ཉེས་བ་ཉིད༌[^2790]བསྟན་ཏོ། །

[Block 4343]
དེ་སྟེ་སྤྲ༌[^2791]ཆེན་དཔའ་བོ་དེ་ཤི་བ། །ཞེས་བྱ་བ་འདིས་ནི་གྲུབ་པའི་མཐའི་སྐྱོན་བསྟན་ཏོ། །

[Block 4344]
ཡང་ན་དེ༌[^2792]གཉིས་གཅིག་ལ་གཅིག་འགལ་བའི་སྐྱོན་བསྟན་ཏོ། །

[Block 4345]
དབང་ཕྱུག་འགྲོ་བ་ཐམས་ཅད་ཀྱི་བྱེད་པ་པོ་ཉིད་ཡིན་ན་ནི༌[^2793]སྐྱེས་བུ་བྱེད་པའི་རྩོལ་བ་ཐམས་ཅད་དོན་མེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལས་བརྩམས་ཏེ། དབང་ཕྱུག་ལ་ནི་རེ་བ་ཡིས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །
--- END BLOCKS ---
