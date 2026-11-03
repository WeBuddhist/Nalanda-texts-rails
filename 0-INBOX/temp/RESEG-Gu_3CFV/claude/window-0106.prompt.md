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
[Block 3711]
མི་གསད་པར༌[^2455]བྱའོ་སྙམ་པ་ལས༌[^2456]མི་མ་ཡིན་པ་བསད་པ་དང་། མི་མ་ཡིན་པ་གསད་པར༌[^2457]བྱའོ་སྙམ་པ་ལས་མི་བསད་པ་ལ་སོགས་པ་ནི་སྦྱོར་བའི་ལྟུང་བ་ཁོ་ན་ཡིན་གྱི་དངོས་གཞིར་མི་འགྱུར་རོ། །

[Block 3712]
དེ་བཞིན་དུ་དུད་འགྲོ་བསད་དོ་སྙམ་པ༌[^2458]ལས་མི་བསད་ན་ཡང་ཉེས་བྱས་སོ། །

[Block 3713]
རྩིག་པ་དང་།

[Block 3714]
ཀ་བ་དང་ཤིང་ལྗོན་པ་ལ་སོགས་པ་སེམས་མེད་པ་གཅད་དོ་སྙམ་པ་ལས།

[Block 3715]
མ་ལ་སོགས་པ་བསད་ན་ཡང་སྦྱོར་བའི་ཉེས་བྱས་སོ། །

[Block 3716]
ཀ་བ་ལ་བརྡེག་པར་མི་བྱ་ཞེས་བྱ་བའི་མཚན་ཉིད་དེར་གཏོགས་པའི་སྦྱོར་བའི་ཉེས་བྱས་སོ། །

[Block 3717]
མི་ལ་སོགས་པ་བསད་པ་ལ་ནི་སྦྱོར་བར་ཡང་མི་འགྱུར་ལ། དངོས་གཞིར་ཡང་མི་འགྱུར་རོ། །

[Block 3718]
མི་ཚངས་པར་སྤྱོད་པ་དང་ཁུ་བ་འབྱིན་པ་གཉིས་ལ་ནི་དེར་མ་ཟད་དོ་ཞེས་བྱ་བ་ནི། གཉིས་པོ་དེ་དག་ལ་ནི་བསམ་པ་འབའ་ཞིག་ཡན་ལག་མ་ཡིན་པར་མ་ཟད་ཀྱི། བསམ་པས༌[^2459]མ་ཡིན་པའི་དོན་གཞན་བུད་མེད་ལ་སོགས་པ་བསྟེན་པ༌[^2460]ལ་ཡང་ཕམ་པའོ། །

[Block 3719]
བསམ་པ་མ་ཡིན་པའི་བྲམ་ཟེའི་བུ་མོས་ཡན་ལག་ལ་དྲུད་པས་ཁུ་བ་བྱུང་བ་ལ་ཡང་དགེ་འདུན་ལྷག་མར་འགྱུར་ལ། སེམས་ཅན་དུ་བགྲང་བ་མ་ཡིན་པ་ལ་ཡང་སྦོམ་པོར་འགྱུར་རོ། །

[Block 3720]
རེག་པ་བདག་གིར༌[^2461]བྱེད་པ་འདི་གཉིས་པ༌[^2462]དེ་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3721]
མི་བདེན་པ་ལ་ནི་ཉན་པ་པོ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་དེར་མ་ཟད་དོ་ཞེས་བྱ་བའི་རྗེས་བསྙག་པའི༌[^2463]ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3722]
མི་བདེན་པ་ལ་ཞེས་བརྫུན་དུ་སྨྲ་བའི་ཡུལ་ཡང་བསམས་པ་ཡན་ལག་ཡིན་པར་མ་ཟད་ཀྱི། མ་བསམས་པ་ཡང་ཡན་ལག་ཡིན་ཏེ། ཉན་པ་པོ་མ་བསམས་པ་གཞན་ལ་ཡང་མི་ཆོས་བླ་མར་འགྱུར་བའི་བརྫུན་དུ་སྨྲས་ན༌[^2464]དེ་ཡང་ཕམ་པར་འགྱུར་ལ། གཞན་དག་ལ་ནི་ལྟུང་བྱེད་དུ་འགྱུར་རོ། །

[Block 3723]
ཡན་ལག་ཐམས་ཅད་དང་དུ་བླང་དུ་རུང་བ་དག་ནི་བསྟེན་པའི༌[^2465]ཕྱིར་མཐུ་དང་ལྡན་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མི་ཚངས་པར་སྤྱོད་པ་དང་ལུས་ཀྱི་རེག༌[^2466]པ་ལ་སོགས་པའི་ཡུལ་ལ་དེ་བསྟེན་པའི་ཕྱིར་དང་མཐུ་དང་ལྡན་པ་ཉིད་ཡིན་པར་ཁས་བླངས་པ་དེ་ནི་དེའི་ངོ་བོའོ། །

[Block 3724]
འོག་མ་དག་ལ་ནི་གཞན་ལ་ནི༌[^2467]སྨད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདི་མན་ཆད་ནས་འོག་གི་མདོ་ལས་རྫུ་འཕྲུལ་གྱི་ཆོས་ཅན་ཉིད་མ་ཡིན་པ་ནི་རེག་པ་མ་ཡིན་པའི་ཡན་ལག་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཕྱིར༌[^2468]བསྟན་པ་རྫོགས་པའི་བར་གྱི་མདོ་འོག་མ་དག་ལས་དེ་གཞན་ལ་ན་སྨད་པ་ཉིད་དོ། །

[Block 3725]
དུ་མ་མ་ཚང་བ་ལ་ནི་དེ་བས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལས་ཀྱང་མ་ཚང་བས་ཡན་ལག་ཏུ་མ་ཚང་བ་ལ་ནི་ན་སྨད་པ་དེ་བས་ཀྱང་ན་སྨད་དོ། །

[Block 3726]
འདི་ལྟ་སྟེ་དཔེར་ན་ལུས་ཀྱི་རེག་པ་དང་། ག་ག་ཚིལ་བྱེད་པའི་ཁ་ན་མ་ཐོ་བ་ཉིད༌[^2469]གཉིས་ལ་རེག་པར་བྱེད་པ་དང་། རེག་པར་བྱེད་པའི་ལུས་གཉིས་ཀ་ལ་ཡན་ལག་ཡིན་པས་རྣམ་པར་འགྱུར་བ་གཅིག་པ་འདི་ལ་དེ་མ་ཐག་པའི་ཚིག་གོ། །

[Block 3727]
དེ་མ་ཐག་པ་དེ་ལས་གཞན་ཞེས་བྱ་བ༌[^2470]འདི་དང་སྔ་མ་བྱེད་པའོ། །

[Block 3728]
རྣམ་པར་འགྱུར་བ་གཉིས་ཀ་ལ་ཡང་འདིས་ན་སྨད་པར་བྱས་པའོ། །

[Block 3729]
མི་ལ་དུད་འགྲོ་ཡང་ངོ་ཞེས་བྱ་བ་ནི༌[^2471]མིའི་གནས་སུ་དུད༌[^2472]འགྲོ་ཞེས་སྨོས་པ་ལ༌[^2473]ཡང་ན་སྨད་པ་དེ་སྦྱོར་རོ། །

[Block 3730]
དུད་འགྲོ་དང་འབྲེལ་པ་ལ་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 3731]
འདི་སྨྲ་བ་དང་བདག་ཉིད་ཀྱི་ཀུན་དུ་སྤྱོད་པ་བསྔགས་པ་ལ་ཉེས་བྱས་སུ་འགྱུར་གྱི། ཇི་ལྟར་མི་མ་ཡིན་པ་མཐུ་མེད་པ་དང་ལྷན་ཅིག་ཏུ་ལུས་ཀྱི་རེག་པ་ལ་སོགས་པ་བྱེད་པ་ལ་ན་སྨད་དེ། སྦོམ་པོར་འགྱུར་བ་ལྟ་བུ་མ་ཡིན་ཏེ། དེ་བས་ཀྱང་ན་སྨད་པ་ཉིད་ཡིན་པའོ། །

[Block 3732]
དེ་བཞིན་དུ་རྫུ་འཕྲུལ་གྱི་ཆོས་ཅན་ཉིད་མ་ཡིན་པ་ནི་རེག་པ་མ་ཡིན་པའི་ཡན་ལག་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདི་བསྟེན་པ་ལ་དེ་ནི་རེག་པ་མ་ཡིན་པའི་ཡན་ལག་ཡིན་ནོ། །

[Block 3733]
འདིར་གཞུང་ནི། འདུལ་བྱེད་དག་ལས་འདི་ནི་དེའི་རིམ་པ་ཞེས་བྱ་བ་འདིས་ནི་འདིར་བསྡུས་པའོ། །

[Block 3734]
སྨྲ་བའི་སྐབས་ནས་རྫུ་འཕྲུལ་གྱིས་རྣམ་པར་འཕྲུལ་པའི་ཆོས་ཅན་མོ་ལ་སྨྲས་ན་སྦོམ་པོར་འགྱུར་རོ། །

[Block 3735]
རྫུ་འཕྲུལ་གྱིས་རྣམ་པར་འཕྲུལ་བའི་ཆོས་ཅན་མོ་མ༌[^2474]ཡིན་པས་སྨྲ་ན་དགེ་འདུན་ལྷག་མའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3736]
དེ་ལ་དང་པོ་རྫུ་འཕྲུལ་རྣམ་པར་འཕྲུལ་པའི་ཆོས་ཅན་ལ་མེད་པས་ན་སྨད་པ༌[^2475]འདི་ཤེས་སོ་ཞེས་བྱ་བ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3737]
དེ་བས་ན་གཅིག་ལ་རེག་པས་འདིར་རེག་པ་སྤང་བ་ཉིད་ཀྱི་ཕྱིར་ཆོས་འདི་ལ་འཇུག་པའི་སྦྱོར་བ་འདི་གཞན་འགའ་ཞིག་བསྟེན་པ༌[^2476]དང་འབྲེལ་པ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ཐམས་ཅད་དུ་འདུ༌[^2477]ཤེས་པའོ། །

[Block 3738]
སྨྲ་བ་ལ༌[^2478]སོགས་པ་རྣམས་ལ་རྫུ་འཕྲུལ་གྱིས་རྣམ་པར་འཕྲུལ་པའི་ཆོས་ཅན་ལ་ནི་སྦོམ་པོར་འགྱུར་རོ། །

[Block 3739]
རེག་པ་ལ་ནི་དགེ་འདུན་ལྷག་མ་ཁོ་ནར་འགྱུར་རོ། །

[Block 3740]
རེག་པར་བྱ་བ་ཉིད་ནི་མ་ཉམས་པའོ་ཞེས་བྱ་བ་ནི་བསྟེན་པར༌[^2479]བྱ་བའི་ལུས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3741]
འདིར་ལུས་ཀྱི་རེག་པའི་བདེ་བ་ཉམས་སུ་མྱོང་བ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོའི་རྣམ་པར་གཞག་པ་འདིའོ། །

[Block 3742]
འདིར་དཔེར་ན་རྨ་དང་ནད་ལ༌[^2480]སོགས་པས་ཉམས་པས་མཚན་མི་མཐུན་པའི་ཡན་ལག་གིས༌[^2481]ལུས་ལ་རེག་ན་སྦོམ་པོར་འགྱུར་རོ། །

[Block 3743]
ཤུ་བ་དང་གཡན་པ་ཅན་དང་ཁྱི་རྔོ་ཅན་གྱིས་རེག་ན་ཡང་དེ་བཞིན་དུ་སྦོམ་པོའོ། །

[Block 3744]
བདག་ཉིད་ཀྱི༌[^2482]ལུས་དེ་ལྟར་འགྱུར༌[^2483]ན་ནི་ཉེས་བྱས་སོ། །

[Block 3745]
རྣམ་པར་བསྔོས་པ༌[^2484]ལ་འཁྱུད་པ་ལ་ནི་སྦོམ་པོའོ། །

[Block 3746]
དེ་བཞིན་དུ་རྣམ་པར་རྣགས་པ༌[^2485]མོ་དང་། རྣམ་པར་འབུས་གཞིག་པ༌[^2486]མོ་དང་། རྣམ་པར་བམ་པ་མོ་དང་། རྣམ་པར་ཟོས་པ་མོ་དང་། རྣམ་པར་དམར་བ་མོ་དང་། རྣམ་པར་འཐོར་བ་མོ་ནས་མི་ཚངས་པར་སྤྱོད་པའི་ཕམ་པར་འགྱུར་བ་འབྱུང་བ་དེ་ཙམ་གྱི་བར་དུ་འདིར་དམ་དུམ༌[^2487]དུ་འཐོར་བ་ཉིད་ཡིན་པ་ཁས་བླངས་པར་རིགས་སོ། །

[Block 3747]
མཐུ་དང་ལྡན་པ་ཉིད་ཡན་ལག་ཉིད་ཡིན་པ་དེ་བས་ན་འདིར་རོ་ཉིད་ལ་ནི་ན༌[^2488]སྨད་པ་མེད་པའི་ཕྱིར། དེས་ན་རྣམ་པར་བསྔོས་པ་ལ་སོགས་པ་དག་ལ་སྦོམ་པོར་གསུངས་སོ། །

[Block 3748]
ག་ག་ཚིལ་བྱེད་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། སོར་མོས་ག་ག་ཚིལ་བྱེད་པ་ལ་ཡང་རེག་པར་བྱ་བ་ལ་ཡན་ལག་ཉིད་ནི་མ་ཉམས་པའོ་ཞེས་བྱ་བའི་རྗེས༌[^2489]སྙེག་པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3749]
འདི་ཡང་འདི་ལྟ་བུའི་ཡན་ལག་རྣམས་ལ༌[^2490]ག་ག་ཚིལ་བྱེད་པ་ལ་ནི་ན་སྨད་པ་ཉིད་དོ། །

[Block 3750]
གཉིས་ཀའི་ལུས་ཇི་སྙེད་བསྟན་པ་དེ་ལྟ་བུ་ཉིད་ལ་ཉམས་པ་ལ་སོགས་པ་རྣམ་པར་གྱུར་པ་ལ་འདིར་དོན་ཉིད་ཀྱི་ཕྱིར། དེ་ལྟ་བུའི་རེག་པར་བྱ་བ་ལ་ཡོངས་སུ་མ་རྫོགས་པ་གྲུབ་པ་ལ་དེ་ལྟ་བུའི་རེག་པར་བྱ་བ་ལས་ཀྱང་གྲུབ་པའོ། །
--- END BLOCKS ---
