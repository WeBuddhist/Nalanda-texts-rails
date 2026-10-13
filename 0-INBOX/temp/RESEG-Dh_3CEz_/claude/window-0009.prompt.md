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
[Block 316 [HEADING]]
###### **དེ་ཁོ་ན་ཉིད་དང་སྦྱར་བ།** ^1-1-5-2-1-2-3-1-2-2-3-0

[Block 317]
དེ་ཁོ་ན་ཉིད་དང་སྦྱར་བ་ལ་ཡང་ཐུན་མོང་དང་ཁྱད་པར་རོ། །

[Block 318 [HEADING]]
###### **ཐུན་མོང།** ^1-1-5-2-1-2-3-1-2-2-3-1-0

[Block 319]
ཐུན་མོང་ནི་བདེན་པ་བཞི་དང་སྡེ་པ་བཞི་སྟེ་སྡེ་པ་མཆོག་ཏུ་སྡོམ་པའོ། །

[Block 320 [HEADING]]
###### **ཁྱད་པར།** ^1-1-5-2-1-2-3-1-2-2-3-2-0

[Block 321]
ཁྱད་པར་ནི་མཆོག་དང༌[^175]མཆོག་མ་ཡིན་པ་སྟེ། དེ་ཡང་མཆོག་ནི་སྐད་ཅིག་དང་དགའ་བ་བཞིའི་བདེ་བ་མཆོག་ཏུ་སྡོམ་པའོ། །མཆོག་མ་ཡིན་པ་ནི་དེ་ཁོ་ན་ཉིད་བཞི་བདེ་བ་མཆོག་ཏུ་སྡོམ་པས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 322 [HEADING]]
###### **བརྟག་པ་ཕྱི་མའི་ཚུལ་དུ་རྒྱུ་མཚན་བསྟན་པ།** ^1-1-5-2-1-2-3-2-0

[Block 323]
བརྟག་པ་ཕྱི་མའི་ཚུལ་དུ་རྒྱུ༌[^176]མཚན་བསྟན་པ་ལ་གཉིས་ཏེ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་དང་། སངས་རྒྱས་སོ། །

[Block 324 [HEADING]]
###### **ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས།** ^1-1-5-2-1-2-3-2-1-0

[Block 325]
དེ་ལ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ནི་འཁོར་ལོ་བཞི་སྐུ་བཞིར་གྲུབ་པ་དེ།[^177] འབྲས་བུ་བཞི་དང་སྡེ་པ་བཞི་དང་། རྣམ་པར་གཞག་པའི་རྒྱུ་མཚན་གྱིས་སྡེ་པ་མཆོག་ཏུ་སྡོམ་པ་དང་།

[Block 326 [HEADING]]
###### **སངས་རྒྱས།** ^1-1-5-2-1-2-3-2-2-0

[Block 327]
སངས་རྒྱས་ནི་ས་བཅུའི་བྱང་ཆུབ་སེམས་དཔའ་སྟེ། མིར་སྐྱེ་བ་དག་པའི་ཚུལ་གདོད་མ་ནས་སངས་རྒྱས་ཡིན་པས་བདེ་བ་མཆོག་ཏུ་སྡོམ་པས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 328 [HEADING]]
###### **མངོན་པར་རྟོགས་པ།** ^1-1-5-2-1-2-3-1-3-0

[Block 329]
མངོན་པར་རྟོགས་པ་ལ་གཉིས་ཏེ། །

[Block 330 [HEADING]]
###### **ཉམས་སུ་ལེན་པ་རླུང་ལ་བསླབ་པ་དང་གཏུམ་མོ་སྦར་བ།** ^1-1-5-2-1-2-4-0

[Block 331]
རྣམ་པར་རྟོག་པའི་གཉེན་པོ་སྟེང་སྒོ་རླུང་ལ་བསླབ་པ་དང་། ཉོན་མོངས་པའི་གཉེན་པོར་བྱང་ཆུབ་སེམས་ལ་བསླབ་པའོ། །

[Block 332 [HEADING]]
###### **རླུང་ལ་བསླབ་པ།** ^1-1-5-2-1-2-4-1-0

[Block 333]
རླུང་ལ་གཉིས་ཏེ། ཤེས་པར་བྱ་བ་དང་། བསྒོམ༌[^178]པའོ། །

[Block 334 [HEADING]]
###### **ཤེས་པར་བྱ་བ།** ^1-1-5-2-1-2-4-1-1-0

[Block 335]
[^179]དེ་ལ་ཤེས་པ་ནི་ཕྱི་དག་པར་ཤེས་པ་དང་ནང་དག་པར་ཤེས་པའོ། །

[Block 336 [HEADING]]
###### **ཕྱི་དག་པར་ཤེས་པ།** ^1-1-5-2-1-2-4-1-1-1-0

[Block 337]
དེ་ལ་ཕྱི་ནི་རྒྱལ་པོའི་ཕོ་བྲང་དང་དགེ་འདུན་གྱི་གནས་དག་ན་དབྱུ་གུ་དང་ཆུ་ཚོད་ལ་སོགས་ཏེ་རླུང་དུ་སྦྱར་བའོ། །

[Block 338 [HEADING]]
###### **ནང་དག་པར་ཤེས་པ།** ^1-1-5-2-1-2-4-1-1-2-0

[Block 339]
ནང་གི་ལྟེ་བ་སྤྲུལ་པའི་འཁོར་ལོ་ལ་སོགས་པ་འདབ་མའི་གྲངས་སྦྱར་བའོ། །

[Block 340 [HEADING]]
###### **བསྒོམ་པ།** ^1-1-5-2-1-2-4-1-2-0

[Block 341]
དེ་དག་རྣམ་པར་དག་པའི་རང་བཞིན་དུ་ཤེས་ནས་རླུང་ལ་བསྒོམ་པ་སྟེ། ཟླ་བ་ཉི་མ་ཨཱ་ལི་ཀཱ་ལི་ཉིན་མཚན་གཉིས་ལ་ཐུན་བཞི་བཞི་བརྒྱད་དུ་འབྱུང་ངོ་། །རེ་མོས་འབྱུང་བའི་འཕོ་བ་ནི་ཐུན་ཕྱེད་ཕྱེད་ནས་ཏེ་བཅུ་དྲུག་གོ། །དེ་རེ་རེ་ལ་ཡང་ཐབས་དང་ཤེས་རབ་ཀྱི་ཆས༌[^180]ཆུ་ཚོད་སུམ་ཅུ་རྩ་གཉིས་སོ། །ཡང་ཟླ་ཉི་གང་ཡང་རུང་བ་གཅིག་ལས་བྱུང་བ༌[^181]བཞི་རིམ་གྱིས་འབྱུང་བས་དབྱུ་གུ་དྲུག་ཅུ་རྩ་བཞིའོ། །དེ་ལྟར་རླུང་ལས་སུ་རུང་ནས་གྲངས་ཀྱི་རྩིས་ནི་གཞན་དུ་ཤེས་པར་བྱའོ། །བསླབ་པ་ནི་གྲངས་ལ་བཅུ་དང་བརྒྱའི་བར་དུ་བསླབ་པ་དང་།རླུང་ལྷན་ཅིག་སྐྱེས་པར་སྦྱོར་བའོ། །

[Block 342 [HEADING]]
###### **བྱང་ཆུབ་སེམས་ལ་བསླབ་པ།** ^1-1-5-2-1-2-4-2-0

[Block 343]
བྱང་ཆུབ་སེམས་ལ་བསླབ་པ་ལ༌[^182]གཉིས་ཏེ། སྒྲའི་དབྱེ་བ་དང་བཤད་ཚུལ་སྦྱོར་བའོ། །

[Block 344 [HEADING]]
###### **སྒྲའི་དབྱེ་བ།** ^1-1-5-2-1-2-4-2-1-0

[Block 345]
དེ་ལ་སྒྲའི་དབྱེ་བ་གང་དུ་འཛག་ནི༌[^183]ལྟེ་བ་སྟེ་གཉིས་པའི་དོན་ཏོ། །གང་འཛག་ན་རི་བོང་ཅན་ཏེ་དང་པོའི་དོན་ཏོ། །གང་ལས་འཛག་ན་ཧཾ་ལས་ཏེ་ལྔ་པའི་དོན་ཏོ། །གང་གིས་འཛག་ན་གཏུམ་མོ་སྦར་བ་སྟེ། གསུམ་པའི་དོན་ཏོ། །གང་གི་ཕྱིར་འཛག་ན་དེ་བཞིན་གཤེགས་པ་ལ་སོགས་པ་བསྲེགས་པའི༌[^184]དོན་ཏེ་བཞི་པའི་དོན་ཏོ། །

[Block 346 [HEADING]]
###### **བཤད་ཚུལ་སྦྱོར་བ།** ^1-1-5-2-1-2-4-2-2-0

[Block 347]
བཤད་པའི་ཚུལ་སྦྱར་བ་ལ་ཡང་གཉིས་ཏེ། བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པའོ། །

[Block 348 [HEADING]]
###### **བསྐྱེད་པའི་རིམ་པ།** ^1-1-5-2-1-2-4-2-2-1-0

[Block 349]
དེ་ལ་བསྐྱེད་པ་ལ་ཡང་ལྟེ་བར་ནི་སྣ་ཚོགས་པདྨའོ། །གཏུམ་མོ་ནི་རང་གི་རིག་མའོ། །ཨཱ་ལི་ཟླ་བ་ཅན་རྡོ་རྗེ་སེམས་དཔའོ། །འབར་བ་ནི་དེ་གཉིས་རྗེས་སུ་ཆགས་པའོ། །དེ་བཞིན་གཤེགས་པ་ནི་ཕུང་པོ་ལྔ་སྟེ།རྡོ་རྗེ་སེམས་དཔའ་ལ་ཡོད་པའོ། །སྤྱན་ལ་སོགས་པ་ནི་འབྱུང་བ་ལྔ་སྟེ་རིག་མ་ལ་ཡོད་པའོ། །བསྲེགས་པ་ནི་ཆགས་པས་ཞུ་བའོ། །རི་བོང་ཅན་ནི་ཁུ་བའི་མིང་གི་རྣམ་གྲངས་སོ། །འཛག་པ་ནི་ཐིག་ལེ་བཞི་ཆད་པའོ། །ཧཾ་ནི་བསྐུལ་བའི་གླུའོ། །

[Block 350 [HEADING]]
###### **རྫོགས་པའི་རིམ་པ།** ^1-1-5-2-1-2-4-2-2-2-0

[Block 351]
རྫོགས་པའི་རིམ་པ་ལ་གསུམ་སྟེ། གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་དང་། རང་ལུས་ཐབས་དང་ལྡན་པ་དང་གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོའོ། །

[Block 352 [HEADING]]
###### **གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ།** ^1-1-5-2-1-2-4-2-2-2-1-0

[Block 353]
དེ་ལ་ཤེས་རབ་ལ་བརྟེན་པ༌[^185]ཡང་ཙཎྜ་ལཱི་ཉི་མ། ཨཱ་ལི་ནི་ཟླ་བའོ། །ལྟེ་བ་ནི་རིན་པོ་ཆེའི་ཟེ་འབྲུ་དང་བྱ་རོག་གི་གདོང་ཅན་ནོ། །འབར་པ་ནི་ཆགས་པས་བསྐྱེད་པའོ། །དེ་བཞིན་གཤེགས་པ་ལྔ་ནི་ལུས་ཅན་གྱིས་བསྡུས་པ་བཅུད་ཀྱི་འཇིག་རྟེན་ནོ། །སྤྱན་ལ་སོགས་པ་ནི་འབྱུང་བས་བསྡུས་པ་སྣོད་ཀྱི་འཇིག་རྟེན་ནོ། །བསྲེགས་པ་ནི་ཐ་མལ་པ་མི་དམིགས་པར་འཇུ་བར་བྱེད་པའོ། །རི་བོང་ཅན་ནི་ཞུ་བའོ། །ཧཾ་ནི་བདེ་བ་ཆེན་པོའི་གནས་ལ་ཡོད་པའོ། །འཛག་པ་ནི་དེ་ལ་རྒྱུ་བའོ། །

[Block 354 [HEADING]]
###### **རང་ལུས་ཐབས་དང་ལྡན་པ།** ^1-1-5-2-1-2-4-2-2-2-2-0

[Block 355]
རང་ལུས་ཐབས་ཀྱི་བསྒོམ་པ་རྩ་དང་འཁོར་ལོར་གནས་པ་དེ་ཡང་ལྟེ་བར་ཨཾ་ལས་རླུང་དང་མེ་སྦར་ཏེ༌[^186]འོད་ཟེར་ལངས་པས་དེ་བཞིན་གཤེགས་པ་ལྔ་བསྲེགས་ཏེ། རྣམ་པ་དང་དོན་དང་མིང་རྣམས་ཀྱང་བསྲེགས་པའོ། །མགྲིན་པར་སྤྱན་ལ་སོགས་པ་ཡང་རྣམ་པ་དང་། དོན་དང་མིང་རྣམས་བསྲེགས་ནས་སྨིན་ཕྲག་ནས་བྱུང་ནས༌[^187]དེ་བཞིན་གཤེགས་པ་རྣམས་འོད་ཟེར་དུ་བཀུག་སྟེ་ཧཾ་ལ་ཐིམ་པས་ཆ་དང་ཆ་མེད་དུ་སོང་ནས་སུམ་ཅུ་རྩ་གཉིས་མཐའ་བདེ་བ་འབྱུང་བ་དང་ཧཾ་ཞུ་ནས་རྐན་ལ་སོགས་པར་ཁྱབ་པར་བྱས༌[^188]ཏེ་དྲི་ཆེན་བུ་ག་ནས་བྱུང་ནས། དེ་ནས་མགྲིན་པར་སོང་སྟེ་ངལ་བསོས་རང་གི་ཡི་གེ་རྣམས་གསོས། སྙིང་གར་དབུགས་ཕྱུང་སྟེ་སྔ་མ་བཞིན་བྱས། ལྟེ་བའི་ཨཾ་དེ་སོས་ཀའི་གླང་པོ་ཚད་པས་གདུངས་པ་ལ་བུམ་པ་བརྒྱ་ཡིས་ཁྲུས་གསོལ་བའམ། བཙུན་མོ་རྒྱན་གྱིས༌[^189]བརྒྱན་པ་འདོད་པས་གདུངས་པ་ལ་ཚིམ་པར་བྱས་པ་ལྟར་བདེ་བ་དང་དགའ་བར་འགྱུར་རོ། །
--- END BLOCKS ---
