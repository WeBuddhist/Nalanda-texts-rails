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
[Block 456 [VERSE]]
རྣམ་པར་རྟོག་པ་མེད་པ་ཡི། །
དགེ་བའི་ལས་ཀྱི་རྣམ་སྨིན་ནི། །
སེམས་ཀྱི་ཚོར་བ་ཁོ་ནར་འདོད། །

[Block 457]
རྣམ་པར་རྟོག་པ་མེད་པའི་ལས་ནི་བསམ་གཏན་ཁྱད་པར་ཅན་ནས་སྲིད་པའི་རྩེ་མོའི་བར་དག་ན་ཡོད་དེ། དགེ་བའི་ལས་རྣམ་པར་རྟོག་པ་མེད་པ་དེའི་རྣམ་པར་སྨིན་པ་ནི་སེམས་ཀྱི་ཚོར་བ་ཁོ་ན་ཡིན་ནོ། །ཅིའི་ཕྱིར་ལུས་ཀྱི་མ་ཡིན་ཞེ་ན། དེ་ནི་གདོན་མི་ཟ་བར་རྟོག་པ་དང་དཔྱོད་པ་དང་དཔྱད་པ༌[^324]ཡིན་པའི་ཕྱིར་རོ། །

[Block 458]
མི་དགེ་བ༌[^325]ནི་ལུས་ཀྱི་ཡིན། །མི་དགེ་བའི༌[^326]ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ནི་ལུས་ཀྱི་ཚོར་བ་ཁོ་ན་ཡིན་ནོ། །ཅིའི་ཕྱིར་སེམས་ཀྱི་མ་ཡིན་ཞེ་ན། དེའི་རྣམ་པར་སྨིན་པ་ནི་སྡུག་བསྔལ་གྱི་ཚོར་བ་ཡིན་ལ། སེམས་ཀྱི་སྡུག་བསྔལ་གྱི་ཚོར་བ་ནི་ཡིད་མི་བདེ་བ་ཡིན་ཏེ། ཡིད་མི་བདེ་བ་ནི་རྣམ་པར་སྨིན་པ་མ་ཡིན་ནོ་ཞེས་དེ་ནི་བཤད་ཟིན་ཏོ། །

[Block 459 [HEADING]]
### སེམས་གཡེང་བ། ^1-32-0

[Block 460]
འོ་ན་སེམས་ཅན་རྣམས་ཀྱི་སེམས་གཡེང་བར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་སེམས་གང་ཞིག་ལ་གནས་པ་ཡིན། རྒྱུ་ནི་ཅི་ཞིག་གིས་འགྱུར་ཞེ་ན།

[Block 461]
གཡེང་བའི༌[^327]སེམས་ནི་ཡིད་སེམས་ལས།

[Block 462]
[^328] །ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 463]
རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་ལ་གནས་པ་ལ་ནི་གཡེང་བ༌[^329]མེད་དེ།

[Block 464 [VERSE]]
རྣམ་པར་མི་རྟོག་པའི་ཕྱིར་རོ། །
དེ་ནི་ལས་ཀྱི་རྣམ་སྨིན་སྐྱེས། །

[Block 465]
གཡེང་བའི༌[^330]སེམས་དེ་ནི་སེམས་ཅན་རྣམས་ཀྱི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་ཡིན་ཏེ། རྫས་དང་གསང་སྔགས་ཀྱི་སྦྱོར་བས་ཕ་རོལ་གྱི་སེམས་གཡེང་བར་བྱེད་པའམ། མི་འདོད་བཞིན་དུ་དུག་དང་མྱོས་པར་འགྱུར་བ་ལྡུད་པའམ། རི་དགས་ལ་སོགས་པ་སྐྲག་པར་བྱེད་པའམ། ནགས་མེས་གཏོང་བའམ། གཡང་དུ་འདོར་བར་བྱེད་པ་འམ། གཞན་གང་ཡང་རུང་བས་ཕ་རོལ་པོ་དག་གི་སེམས་ཉམས་པར་བྱེད་པ་དེ་དག་ལས་དེའི་རྣམ་པར་སྨིན་པས་ཚེ་ཕྱི་མ་ལ་སེམས་གཡེང་བར༌[^331]འགྱུར་རོ། །

[Block 466]
སྐྲག་གནོད་མ་མཉམ༌[^332]མྱ་ངན་གྱིས། །རེ་ཞིག་སྐྲག་པས་ཇི་ལྟ་བུ་ཞེ་ན། མི་མ་ཡིན་པ་གཟུགས་མི་སྡུག་པས་མིའི་གན་དུ་ཉེ་བར་འོངས་ལ་དེ་དག་གིས་སྐྲག་པ་རྣམས་སེམས་གཡེང་བར༌[^333]འགྱུར་རོ། །

[Block 467]
གནོད་པས༌[^334]ཇི་ལྟ་བུ་ཞེ་ན། མི་མ་ཡིན་པ་དེ་དག་ཉིད་དུ༌[^335]འཁྲུགས་ནས་གནད་དུ་སྣུན་པར་བྱེད་པས་སོ། །

[Block 468]
འབྱུང་བ་ཆེན་པོ་མ་མཉམ་པས་ཇི་ལྟ་བུ་ཞེ་ན། རླུང་དང་མཁྲིས་པ་དང་བད་ཀན་དག་འཁྲུགས་པར་གྱུར་པའོ། །

[Block 469]
མྱ་ངན་གྱིས༌[^336]ཇི་ལྟ་བུ་ཞེ་ན། དཔེར་ན་གནས་བྱེད་ཀྱི་བུ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 470]
གལ་ཏེ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་གཡེང་བར༌[^337]འགྱུར་ལ། སེམས་གཡེངས་པ་ཡང་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་ཡིན་པ་ཡིན་ན་གོ། །

[Block 471]
ཇི་ལྟར་ན༌[^338]སེམས་ཀྱི་ཚོར་བ་རྣམ་པར་སྨིན་པ་མ་ཡིན་པར་འགྱུར་ཞེ་ན། སེམས་དེ་ཉིད་རྣམ་པར་སྨིན་པ་ཡིན་ནོ་ཞེས་ནི་མི་ཟེར་རོ། །

[Block 472]
དེ་ལྟ་མོད་ཀྱི་འབྱུང་བ་ཆེན་པོ་རྣམས་འཁྲུགས་པ་གང་ཡིན་པ་དེ་རྣམ་པར་སྨིན་པ་ཡིན་ལ་དེ་ལས་སྐྱེས་པས་དེའི་ཕྱིར་རྣམ་པར་སྨིན་པ་ཡིན་ཏེ། ལས་ལས་སྐྱེས་པའི་ཁམས་རྣམས་འཁྲུགས་པས་སེམས་འཁྲུགས་པ་དང་། དབང་མེད་པ་དང་། དྲན་པ་ཉམས་པར་འགྱུར་བས་ན་སེམས་གཡེངས་པ་ཞེས་བྱའོ། །

[Block 473]
དེ་ལྟར་ན་དེ༌[^339]ནི་སེམས་གཡེངས་ལ་རྣམ་པར་མ་གཡེངས་པ་ཡང་ཡོད་ཅེས་བྱ་བར་མུ་བཞིར་རུང་སྟེ། རེ་ཞིག་གཡེངས་ལ་རྣམ་པར་མ་གཡེངས་པ་ནི་སེམས༌[^340]ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའོ། །

[Block 474]
རྣམ་པར་གཡེངས་ལ་སེམས་མ་གཡེངས་པ་ནི་སེམས་རྣལ་དུ་འདུག་པའི་ཉོན་མོངས་པ་ཅན་ནོ། །

[Block 475]
གཉི་ག་ཡིན་པ་ནི་སེམས་གཡེངས་པའི་ཉོན་མོངས་པ་ཅན་ནོ། །

[Block 476]
གཉི་ག་མ་ཡིན་པ་ནི་སེམས་རྣལ་དུ་འདུག་པའི་ཉོན་མོངས་པ་ཅན༌[^341]མ་ཡིན་པའོ། །

[Block 477]
སེམས་ཅན་གང་དག་གི་སེམས་གཡེངས༌[^342]པར་འགྱུར་ཞེ་ན། སྒྲ་མི་སྙན་མིན༌[^343]འདོད་ལྡན་རྣམས། །སྒྲ་མི་སྙན་མ་ཡིན་པ་འདོད་པ་དང་ལྡན་པ་རྣམས་ནི་ལྷ་དག་གི་ནང་ན་ཡང་ལྷ་སྨྱོན་པ་ཡོད་ན་མི་དང་དུད་འགྲོ་དང་ཡི་དགས་ཀྱི་ནང་ན་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། དམྱལ་བ་རྣམས་ནི་རྟག་ཏུ་སེམས་གཡེངས༌[^344]པ་ཁོ་ན་ཡིན་ཏེ། གནོད་པ་སྣ་ཚོགས་སྟོང་ཕྲག་དག་གིས་གནད་གཅོད་པའི༌[^345]ཚོར་བ་དྲག་པོ་དག་གིས་མངོན་པར་ཉེན་པ་དེ་དག་ནི་རེ་ཞིག་བདག་ཉིད་ཀྱང་མི་དྲན་ན་བྱ་བ་དང་བྱ་བ་མ་ཡིན་པ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཏེ། འདིར་ཀྱི་ཧུད་སེམས་ཞེས་སྨྲེ་སྔགས་འདོན་པའི་དམྱལ་བ་དཔེར་བྱའོ། །

[Block 478]
སངས་རྒྱས་མ་གཏོགས་པའི་འཕགས་པ་རྣམས་ལ་ཡང་འབྱུང་བ་མ་མཉམ་པས༌[^346]སེམས་གཡེང་བ་ཡོད་དོ། །

[Block 479]
ལས་ཀྱིས་ནི་མ་ཡིན་ཏེ། ངེས་པ་ནི་སྔོན་རྣམ་པར་སྨིན་ཟིན་པའི་ཕྱིར་རོ། །

[Block 480]
མ་ངེས་པ་ནི་རྣམ་པར་མི་སྨིན་པའི་ཕྱིར་རོ། །

[Block 481]
འཇིགས་པས་ཀྱང་མ་ཡིན་ཏེ། འཇིགས་པ་ལྔ་ལས་ཡང་དག་པར་འདས་པའི་ཕྱིར་རོ། །

[Block 482]
གནོད་པས་ཀྱང་མ་ཡིན་ཏེ། མི་མ་ཡིན་པ་འཁྲུགས་པའི་རྒྱུ་མི་མཛེས་པ་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 483]
མྱ་ངན་གྱིས་ཀྱང་མ་ཡིན་ཏེ། ཆོས་ཉིད་མངོན་པར་ཤེས་པའི་ཕྱིར་རོ། །

[Block 484 [HEADING]]
### ཡོན་པོ་དང་ཉེས་པ་དང་སྙིགས་མ། ^1-33-0

[Block 485]
མདོ་ལས།

[Block 486]
ཡོན་པོ་གསུམ་གསུངས་ཏེ། ལུས་ཀྱི་ཡོན་པོ་དང་། ངག་གི་ཡོན་པོ་དང་། ཡིད་ཀྱི་ཡོན་པོའོ། །

[Block 487]
[^347]ཉེས་པ་གསུམ་སྟེ། ལུས་ཀྱི་ཉེས་པ་དང་། ངག་གི་ཉེས་པ་དང་། ཡིད་ཀྱི་ཉེས་པའོ། །

[Block 488]
སྙིགས་མ་གསུམ་སྟེ། ལུས་ཀྱི་སྙིགས་མ་དང་། ངག་གི་སྙིགས་མ་དང་། ཡིད་ཀྱི་སྙིགས་མའོ། །

[Block 489]
དེ་ལ།

[Block 490 [VERSE]]
ཡོན་པོ༌[^348]སྙིགས་མར་གསུངས་པ་ནི། །
དེ་དག་ཀྱང་རིམ་བཞིན་དུ།
གཡོ་དང་ཞེ་སྡང་འདོད་ཆགས་སྐྱེས། །

[Block 491]
ལུས་ཀྱི༌[^349]གཡོ་ལས་སྐྱེས་པ་ནི་གྱ་གྱུའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་པའི་ཕྱིར་ལུས་ཀྱི་ཡོན་པོ་ཞེས་བཤད་དེ་ངག་དང་ཡིད་ཀྱི་ཡོན་པོ་ཡང་དེ་དང་འདྲའོ། །

[Block 492]
ལུས་ཀྱི་ལས་ཞེ་སྡང་ལས་སྐྱེས་པ་ནི་སྡང་བའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་པའི་ཕྱིར་ལུས་ཀྱི་ཉེས་པ་ཞེས་བཤད་དེ། ངག་དང་ཡིད་ཀྱི་ཉེས་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 493]
ལུས་ཀྱི་ལས་འདོད་ཆགས་ལས་སྐྱེས་པ་ནི་ཆགས་པའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་པའི་ཕྱིར་ལུས་ཀྱི་སྙིགས་མ་ཞེས་བཤད་དེ། ངག་དང་ཡིད་ཀྱི་སྙིགས་མ་ཡང་དེ་དང་འདྲའོ། །

[Block 494 [HEADING]]
### དཀར་ནག་ལ་སོགས་པའི་ལས་རྣམ་པ་བཞི། ^1-34-0

[Block 495 [VERSE]]
དཀར་ནག་ལ་སོགས་བྱེ་བྲག་གིས། །
ལས་ནི་རྣམ་པ་བཞི་ཡིན་ནོ། །
--- END BLOCKS ---
