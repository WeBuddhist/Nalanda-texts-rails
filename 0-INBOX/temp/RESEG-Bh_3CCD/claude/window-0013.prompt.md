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
[Block 456]
ན་མཿས་མནྟ་བུདྡྷེ་བྷྱོ་ཨོཾ་ཡ་མ་དཎྜཱ་ཡ་ནཱི་ལ་དནྜཱ་ཡ།

[Block 457]
ཏུ་རུ་ཏུ་རུ་མུ་རུ་མུ་རུ་སརྦ་དུཥྚན་མཱ་ར་ཡ་མཱ་ར་ཡ་ཧཱུཾ་ཕཊ། དབྱུག་སྔོན་ཅན་གྱིའོ། །

[Block 458]
ན་མཿས་མནྟ་བུདྡྷེ་བྷྱོ་ན་མོ་མ་ཧཱ་བ་ལཱ་ཡ་ཨུ་ཙུ་ཤྨ་ཀོ་དྷ་རཱ་ཛ་ཡ།

[Block 459]
སརྦ་ན་གཱ་ནཾ་ཧྲྀ་ད་ཡཾ་ཏཱ་ཌཱ་ཡ་ཧཱུཾ་ཕཊ། སྟོབས་པོ་ཆེའིའོ། །

[Block 460]
ན་མཿས་མནྟ་བུདྡྷེ་བྷྱོ་ན་མོ་ཨ་ཙ་ལ་ཀཱ་ཎ་ཙེཊྚ་ཙེཊྚ་མོཊྚ་མོཊྚ།

[Block 461]
གྷ་གྷ། གྷཱ་ཏ་ཡ་གྷཱ་ཏ་ཡ་ཧཱུཾ་ཕཊ། མི་གཡོ་མགོན་གྱིའོ། །

[Block 462]
ཨོཾ་ཊཀྐི་ཧཱུཾ་ཛ། འདོད་པའི་རྒྱལ་པོའིའོ། །

[Block 463]
ཨོཾ་སུཾ་བྷ་ནི་སུཾ་བྷ་ཧཱུཾ་ཧཱུཾ། ཨོཾ་གྲྀཧྞ་གྲྀཧྞ་ཧཱུཾ་ཧཱུཾ། གྲྀཧྞ་གྲྀཧྞཱ་པ་ཡ་གྲྀཧྞཱ་པ་ཡ༌[^328]ཧཱུཾ་ཧཱུཾ། ཨོཾ་ཨཱ་ན་ཡ་ཧོ་བྷ་ག་བཱན་བིདྱཱ་རཱ་ཛ་ཧཱུཾ་ཕཊ། གནོད་མཛེས་ཀྱི་རྒྱལ་པོ་ཡིའོ། །

[Block 464]
ན་མཿས་མནྟ་བུད་དྷཱ་ནཱཾ་ན་མ་ས་མནྟ་དྷརྨཱ་ནཾ་ན་མ་ས་མནྟ་སཾ་གྷཱ་ནཱཾ།

[Block 465]
ཨོཾ་སི་ཏཱ་ཏ་པ་ཏྲེ་ཨོཾ་བི་མ་ལེ་ཨོཾ་ཤཾ་ཀ་རེ། ཨོཾ་པྲ༌[^329]ཏྱཾ་གི་ར་བཛྲ་ཨུཥྞཱི་ཥ་ཙཀྲ་ཝརྟི་སརྦ་ཡནྟྲ་མནྟྲ་མཱུ་ལ་ཀརྨ་བནྡྷཱ་ནཱཾ་ཏེ་ཌ་ནཾ་ཀི༌[^330]ལ་ནཾ་ཝཱ། མ་མ་ཀྲྀ་ཏེ་ཡེ་ན་ཀེ་ན་ཙིཏྟ་ཀྲྀ་ཏནྟ་སརྦ་ནྟུ། ཚིནྡ་ཚིནྡ། བིནྡྷ་བིནྡྷ། ཙི་རི་ཙི་རི་གི་རི་གི་རི་མ་ར་མ་ར༌[^331]ཧཱུཾ་ཧཱུཾ་ཧཱུཾ་ཧཱུཾ་ཧཱུཾ་ཧཱུཾ་ཧཱུཾ་ཧཱུཾ་ཧཱུཾ་ཧཱུཾ་ཕཊ་ཕཊ་ཕཊ།

[Block 466 [VERSE]]
གཙུག་ཏོར་འཁོར་ལོས་སྒྱུར་བའིའོ།[^332] །
སྔགས་མཆོག་དམ་པ་དེ་རྣམས་ཀྱིས། །
གཏོར་མའི་སྣོད་ལ་སྔགས་བཏབ་ཅིང་།
ཤར་ལ་སོགས་པར་གཏོར་བྱས་ནས། །

[Block 467 [VERSE]]
རང་གི་གནས་སུ་འཇུག་པར་བྱ། །
གཏོར་མའི་སྦྱིན་པ་འདི་ཡིས་ནི། །
ཕྱོགས་བཅུར་གནས་པའི་འབྱུང་པོ་རྣམས། །
ཁྲོ་བོའི་རྒྱལ་པོ་ཚིམ་བྱས་པས།[^333] །

[Block 468 [VERSE]]
དེ་དག་མ་ལུས་ཚིམ་པར་འགྱུར། །
གང་ཕྱིར་ཁམས་གསུམ་ཐམས་ཅད་ནི། །
ཕྱོགས་བཅུ་པོས་ནི་ཡོངས་བསྐོར་བ། །
ཁྲོ་བོའི་རྒྱལ་པོ་རང་ནུས་པས། །

[Block 469 [VERSE]]
ཐམས་ཅད་རྟག་ཏུ་སྐྱོང་བར་བྱེད། །
རབ་གནས་མཐར་ནི་འདི་བྱས་པས། །
གཏོར་མ་ཡིས་ནི་བརྟན་པར༌[^334]འགྱུར། །
གཟུགས་བརྙན་རས་རིས༌[^335]མཆོད་རྟེན་སོགས། །

[Block 470 [VERSE]]
བསྐལ་པའི་བར་དུ་གནས་པར་འགྱུར། །
སྦྱིན་སྲེག༌[^336]མཐར་ནི་ལྷ་མོ་རྣམས། །
དེ་བཞིན་གཤེགས་པ་མཉེས་པར་འགྱུར། །
ཉལ་བའི་དུས་སུ་ཆོ་ག་བཞིན། །

[Block 471 [VERSE]]
གཏོར་མ་སྦྱིན་པ་འདི་ཉིད་ཀྱིས། །
རྨི་ལམ་ངན་པ་སྒྲུབ་པ་པོས། །
ནམ་ཡང་མཐོང་བར་མི་འགྱུར་རོ། །
རྣལ་འབྱོར་དབང་པོ་རྨི་ལམ་ནི། །

[Block 472]
བཟང་པོ་ཁོ་ནར་མཐོང་བར་འགྱུར། །ཞེས་ཁྲོ་བོའི་རྒྱལ་པོའི་གཏོར་མའི་ཆོ་གའོ། །

[Block 473 [HEADING]]
##### གཉིད་ལོག་པའི་ཆོ་ག། ^1-1-3-12-0

[Block 474]
དེའི་རྗེས་སུ་རང་དད་པའི་ལྷའི་ང་རྒྱལ་དང་ལྡན་པའི་རྣལ་འབྱོར་པས་རང་གི་སྙིང་གར་ཡི་གེ་ཁཾ་ཡོངས་སུ་གྱུར་པའི་སྣ་ཚོགས་རྡོ་རྗེའི་ཆང་ཟུངས་ལ་གནས་པའི་ཡི་གེ་ཁཾ་གི་ཐིག་ལེ་ལ་ངལ་བསོ་ཏེ། དེའི་རྗེས་སུ༌[^337]སྔར་བཤད་པའི་ཁྲོ་བོའི་རྒྱལ་པོའི་སྔགས་བཅུ་བརྗོད་ཅིང་སེ་གོལ་བརྡབས་ཏེ་ཕྱོགས་བཅིང་བར་བྱས་ལ་ཉལ་བར་བྱའོ། །

[Block 475]
དེའི་ཚེ་རྨི་ལམ་བཟང་པོ་མཐོང་བ༌[^338]སློབ་དཔོན་ལ་བཟླ་བར་བྱའོ། །

[Block 476]
དེ་མེད་ན་བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་མདུན་དུ་སྨྲ་བར་བྱ་ཡི༌[^339]གཞན་དུ་ནི་མ་ཡིན་ནོ།[^340] །

[Block 477]
ཐོ་རངས་ལྡང་བའི་དུས་སུ་ཁྱོད་ནི་རྡོ་རྗེ་ཐུགས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་བརྗོད་ཅིང་སྤྱན་ལ་སོགས་པ་རྣམས་ཀྱིས༌[^341]བདག་ལ་སད་པར་བྱེད་པར་བསམ་མོ། །

[Block 478]
སླར་ཡང་ཐོ་རངས་ནས་བརྩམས་ཏེ་སྔ་མ་བཞིན་དུ་གནས་གཟུང་བ༌[^342]ལ་སོགས་པ་སྔོན་དུ་འགྲོ་བར་བསྒོམ་པར་བྱའོ་ཞེས་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་དང་སྤྲུལ་པའི་སྐུ་བསྟན་པས་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པ་ཡང་བསྟན་ཏོ། །

[Block 479]
དེ་ལྟར་ཕུན་སུམ་ཚོགས་པ་གཉིས་ཀ་གཙོར་གྱུར་པའི་ཏིང་ངེ་འཛིན་གསུམ་གྱི་བདག་ཉིད་བསྐྱེད་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 480]
[^343]

[Block 481 [HEADING]]
### རྫོགས་པའི་རིམ་པ། ^1-2-0

[Block 482]
ད་ནི་རྫོགས་པའི་རིམ་པ་བཤད་པར་བྱ་སྟེ། དེ་ཡང་བསྐྱེད་པའི་རིམ་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པས་བསྒོམ་པར་བྱ་བ་འདི་ཡིན་ཏེ། དབང་པོ་རྣོ་བས་དབང་བ་དང་རང་བཞིན་གྱིས་གྲུབ་པའི་ཕྱིར་བསྐྱེད་པའི་རིམ་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རྟགས་ནི་འདི་དག་ཡིན་ཏེ། རང་གི་བདག་ཉིད་ཀྱིས་ཇི་བཞིན་བསྒོམས་པའི་རང་འདོད་པའི་ལྷའི་རྣམ་པ་གང་ཡིན་པ་དེ་མ་འཁྲུལ་ཞིང་གསལ་བར༌[^344]སྣང་བ་དང་། གཞན་རྣམས་ཀྱང་དེ་བཞིན་དུ་མངོན་པར་མཐོང་བ་དང་ལྡང་བ་དང་འདུག་པ་དང་ཉལ་བ་དང་འཆག་པའི་མཚན་ཉིད་སྤྱོད་ལམ་བཞི་པོའི་དུས་སུ་ལྷའི་རྣམ་པར་དག་པ་མཐོང་བ་དང་། ཞི་བ་དང་། རྒྱས་པ་དང་། དབང་དང་། དགུག་པ་དང་། རྣམ་པར་ལྡང་བ༌[^345]དང་། རེངས་པ་དང་། བསྐྲད་པ་དང་། མངོན་སྤྱོད་ཅེས་བྱ་བ་དངོས་གྲུབ་བརྒྱད་དང་། དེ་བཞིན་དུ་སྨན་མཆོག་དང་རོ་དང་བཅུད་ཀྱིས་ལེན་པ༌[^346]དང་། གསེར་འགྱུར་གྱི་རྩི༌[^347]སྦྱོར་བ་དང་། ནམ་མཁའ་ལྡིང་གི་སྦྱོར་བ་དང་། ས་འོག་གི་དངོས་གྲུབ་དང་། རོ་ལངས་དང་རལ་གྲི་དང་རི་ལུ༌[^348]དང་མིག་སྨན་དང་རྐང་མགྱོགས་དང་། འཁོར་ལོའི་རིག་པ་འཛིན་པ་ལ་སོགས་པ་དངོས་གྲུབ་རྣམ་པ་དུ་མ་གང་ཡིན་པ་དེ་རྣམས་གཞན་གྱི་དོན་དུ་མི་སླུ་བར༌[^349]འགྲུབ་པ་དང་། རང་གི་ལུས་ལ་ཨུཏྤ་ལ་སྔོན་པོའི་དྲི་བྲོ་བ་དང་། ཆོས་གོས་ལ་སོགས་པ་དང་རྡུལ་དང་ལུས་ལ་ཤིག་དང་འབུ་མེད་པ་དང་། ཕྱིའི་ཁམ་གྱི་ཟས་ལ་ལྟོས་པ༌[^350]མེད་པ་དང་། [^351]བཟའ་བཅའ་ཐོབ་ནས་ཀྱང་སྲེད་པ་མེད་པ་དང་། ཤིང་ཏོག་ལ་སོགས་པ་གང་ཅི་ཡང་རུང་བས་ཆོག་ཤེས་པ་དང་། ཡུལ་ལ་འདོད་པ་ཆུང་བ་དང་། མི་སློང་ཞིང་སྦྱིན་པ་གཏོང་བ་དང་། བཤང་བ་དང་གཅི་བ་ཆུང་བའོ། །

[Block 483]
ངེས་པ་ཅན་གྱི་རྟགས་དེ་དག་གིས་བསྐྱེད་པའི་རིམ་པའི་རྣལ་འབྱོར་ལ་མཐར་ཕྱིན་པར་ཤེས་པར་བྱའོ། །

[Block 484]
ཇི་སྐད་དུ།

[Block 485]
ལང་ཀར་གཤེགས་པ་ལས།

[Block 486]
དུ་བ་ལས་ནི་མེར་ཤེས་ཏེ།

[Block 487 [VERSE]]
ཆུ་སྐྱར་ལས་ནི་ཆུ་ཡིན་ནོ། །
བྱང་ཆུབ་སེམས་དཔའ་བློ་ལྡན་གྱིས། །
རིགས་ནི་མཚན་མ་རྣམས་ལས་ཤེས། །

[Block 488]
ཞེས་འབྱུང་ངོ་། །དེ་ལྟར་བསྐྱེད་པའི་རིམ་པ་མཐར་ཕྱིན་ནས་རྫོགས་པའི་རིམ་པ་ལ་གོམས་པར་བྱ་སྟེ།

[Block 489 [VERSE]]
རབ་ཏུ་བྱེད་པའི་མཁན་པོས་ཀྱང་། །
བསྐྱེད་པའི་རིམ་པ་ལེགས་གནས་ཤིང་། །
རྫོགས་པའི་རིམ་པ་འདོད་རྣམས་ལ། །
ཐབས་འདི་རྫོགས་པའི་སངས་རྒྱས་ཀྱིས། །

[Block 490]
སྐས་ཀྱི་རིམ་པ་ལྟ་བུར་གསུངས། །ཞེས་འབྱུང་ངོ་། །དེ་ལ་བསྐྱེད་པའི་རིམ་པ་ལ་ལེགས་པར་གནས་པ་གང་ཞེ་ན། གང་དང་པོའི་སྦྱོར་བ་ལ་སོགས་པའི་བསྒོམ་པའི་རིམ་པས། རིགས་བརྒྱའི་དབྱེ་བས་ལུས་རྣམ་པར་དབེན་པ་ལ་ཞུགས་པའོ། །

[Block 491]
རིགས་བརྒྱའི་དབྱེ་བ་ནི་གཟུགས་ཀྱི་ཕུང་པོའི་ཚོགས་ནི་རྣམ་པར་སྣང་མཛད་དོ། །

[Block 492]
ཚོར་བའི་ཕུང་པོའི་ཚོགས་ནི་རིན་ཆེན་འབྱུང་ལྡན་ནོ། །

[Block 493]
འདུ་ཤེས་ཀྱི་ཕུང་པོའི་ཚོགས་ནི་འོད་དཔག་ཏུ་མེད་པའོ། །

[Block 494]
འདུ་བྱེད་ཀྱི་ཕུང་པོའི་ཚོགས་ནི་དོན་ཡོད་གྲུབ་པའོ། །

[Block 495]
རྣམ་པར་ཤེས་པའི་ཕུང་པོའི་ཚོགས་ནི་མི་བསྐྱོད་པའོ། །
--- END BLOCKS ---
