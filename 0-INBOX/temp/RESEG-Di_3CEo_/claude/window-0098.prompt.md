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
[Block 3431]
སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་སྐྱེས་ནས་དང་། མངོན་པར་འདུ་བྱེད་པ་དང་། མངོན་པར་འདུ་བྱེད་པ་མེད་པར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཕྱིར་རོ། །

[Block 3432]
གོང་དུ་འཕོ་བ་ནི་འཕར་བ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་སོ། །

[Block 3433]
དེ་དག༌[^1350]ནི་ཁྱད་པར་རྣམས། ལས་དབང་ཉོན་མོངས་བྱེ་བྲག་ལས། །

[Block 3434]
གསུམ་དང་དགུ་པོ་དེ་དག་གི་ཁྱད་པར་ནི་ལས་དང་། ཉོན་མོངས་པ་དང་། དབང་པོའི་བྱེ་བྲག་ལས་ཏེ། རེ་ཞིག་གསུམ་པོ་ནི་མངོན་པར་འགྲུབ་པ་དང་། སྐྱེས་པ་དང་། ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བའི་ལས་བསགས་པའི་ཕྱིར་དང་། ཉོན་མོངས་པ་ཀུན་དུ་སྤྱོད་པ་ཆུང་བ་དང་། འབྲིང་དང་། ཆེན་པོའི་ཕྱིར་དང་། དབང་པོ་ཆེན་པོ་དང་། འབྲིང་དང་། ཆུང་ངུའི་ཕྱིར་རོ། །

[Block 3435]
དགུ་པོ་དེ་དག་སོ་སོར་ཁྱད་པར་དེ་ཉིད་ཀྱི་ཕྱིར་ཅི་རིགས་པར་གསུམ་ཚན༌[^1351]

[Block 3436]
དང་པོ་གཉིས་ནི་གོང་མ་བཞིན་དུ་ཉོན་མོངས་པ་དང་དབང་པོའི་བྱེ་བྲག་ལས་སོ། །

[Block 3437]
གསུམ་ཚན༌[^1352]ཐ་མ་ནི་ལན་གྲངས་གཞན་ལ༌[^1353]མྱོང་བར་འགྱུར་བའི་ལས་ཀྱི་བྱེ་བྲག་ལས་ཀྱང་ངོ་། །འོ་ན་མདོ་ལས་སྐྱེས་བུ་དམ་པའི་འགྲོ་བ་བདུན་བསྟན་པ་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 3438 [VERSE]]
གོང་དུ་འཕོ་བ་མ་ཕྱེ་བར། །
དམ་པའི་འགྲོ་བ་བདུན་དུ་འདོད། །

[Block 3439]
དགུ་པོ་དེ་དག་ཁོ་ན་ལ་གོང་དུ་འགྲོ་བ་མ་ཕྱེ་བས་བདུན་དུ་འགྱུར་རོ། །

[Block 3440]
ཅིའི་ཕྱིར་འདི་དག་ཁོ་ན་སྐྱེས་བུ་དམ་པའི་འགྲོ་བ་ཡིན་ལ་སློབ་པའི་འགྲོ་བ་གཞན་དག་ནི་མ་ཡིན་ཞེ་ན།

[Block 3441 [VERSE]]
དམ་པ་དམ་མིན་འཇུག་མི་འཇུག །
སོན་པ༌[^1354]ཕྱིར་མི་འོང་ཕྱིར་དེ། །

[Block 3442]
འདི་དག་ནི་ལས་དགེ་བ་ཁོ་ན་ལ་འཇུག་གི་མི་དགེ་བ་ལ་ནི་མི་འཇུག་གོ། །

[Block 3443]
འདི་དག་ཏུ་སོན་པ་རྣམས་ལ་ཡང་། ཕྱིར་མི་འོང་བ་མེད་པ་དེའི་ཕྱིར་འདི་དག་ཁོ་ན་སྐྱེས་བུ་དམ་པའི་འགྲོ་བ་ཡིན་ནོ། །

[Block 3444]
ཅིའི་ཕྱིར་ཕྱིར་མི་འོང་བ་ཚེ་ཡོངས་སུ་གྱུར་པ་ལ་ཡང་དབྱེ་བ་འདི་ཡོད་དམ་ཞེ་ན། མེད་དེ། འདི་ལྟར།

[Block 3445 [VERSE]]
འདོད་པར་ཚེ་ཡོངས༌[^1355]གྱུར་པའི་འཕགས། །
ཁམས་གཞན་དུ་ནི་འགྲོ་བ་མེད། །

[Block 3446]
འདོད་པའི་ཁམས་སུ་ཚེ་ཡོངས་སུ་གྱུར་པའི་འཕགས་པ་ནི་ཁམས་གཞན་དུ་མི་འགྲོ་སྟེ། དེ་ཉིད་ལ་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ཐོབ་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཕྱིར་རོ། །

[Block 3447 [VERSE]]
དེ་དང་གོང་མར་སྐྱེས་པ་ནི། །
ཡོངས་ཉམས་དབང་པོ་འཕོ་མི་སྟེན། །

[Block 3448]
འདོད་པའི་ཁམས་སུ་ཚེ་ཡོངས་སུ་གྱུར་པའི་འཕགས་པ་དེ་དང་། ཁམས་གོང་མར་སྐྱེས་པའི་འཕགས་པ་ནི་དབང་པོ་རྣམས་ཀྱང་མི་འཕོ་ལ། ཇི་ལྟར་ཡང༌[^1356]ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་རོ། །

[Block 3449]
བསམ་གཏན་སྤེལ་ནས་འོག་མིན་འགྲོ། །ཞེས་གང་བཤད་པ་དེ་ཡང་དང་པོ་ཉིད་དུ་བསམ་གཏན་གང་སྤེལ་བར་བྱེད་ཅེ་ན། དང་པོར་བཞི་པ་སྤེལ་བར་བྱེད། །ཏིང་ངེ་འཛིན་དེ་ནི་ཐམས་ཅད་པས་ལས་སུ་རུང་བ་སྟེ། དེ་དག་གི་ཕུན་སུམ་ཚོགས་པ་ལ་སིམ་པའི་ཕྱིར་རོ། །

[Block 3450]
དེའི་ཡང་། སྐད་ཅིག་མ་ནི༌[^1357]བསྲེས་པས་འགྲུབ། །གང་གི་ཚེ་ཟག་པ་མེད་པའི་སྐད་ཅིག་མའི་མཇུག༌[^1358]ཐོགས་སུ་ཟག་པ་དང་བཅས་པ་དང་། ཟག་པ་དང་བཅས་པའི་མཇུག༌[^1359]ཐོགས་སུ་ཡང་ཟག་པ་མེད་པ་མངོན་སུམ་དུ་བྱེད་ལ། དེ་ལྟར་ཟག་པ་དང་བཅས་པའི་སྐད་ཅིག་མ་དང་། ཟག་པ་མེད་པ་དག་ཏུ་བསྲེས་པས་སྤེལ་མ་འགྲུབ་པ་ཡིན་ནོ། །

[Block 3451]
རྒྱུན་ཆགས་དང་ལྡན་པ་ལ་ཇི་སྲིད་དུ་སྐད་ཅིག་གཉིས་སྦྱོར་བ་དེ་ལྟར་བསམ་གཏན་བཞི་པ་སྤེལ་ནས་དེའི་སྟོབས་ཀྱིས་གཞན་དང་གཞན་དག་ཀྱང་སྤེལ་བར་བྱེད་དོ། །ཅིའི་ཕྱིར་བསམ་གཏན་སྤེལ་བར་བྱེད་ཅེ་ན།

[Block 3452 [VERSE]]
སྐྱེ་དང་གནས་པར་བྱ་ཕྱིར་དང་། །
ཉོན་མོངས་པས་ནི་འཇིགས་ཕྱིར་ཡང་། །

[Block 3453]
ཕྱིར་མི་འོང་བ་དབང་པོ་རྣོན་པོ་རྣམས་ནི་གནས་གཙང་མར་སྐྱེ་བར་བྱ་བའི་ཕྱིར་དང་། མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 3454]
དབང་པོ་རྟུལ་པོ་རྣམས་ནི་ཉོན་མོངས་པས་འཇིགས་པའི་ཡང་ཕྱིར་ཏེ། དེ་བཞིན་དུ་དགྲ་བཅོམ་པ་རྣམས་སྐྱེ་བ་མ་ཡིན་པས་གནས་གཙང་མར་སྐྱེ་བ་སྤངས་ནས་སོ། །

[Block 3455]
ཡང་ཅིའི་ཕྱིར་གནས་གཙང་མར་སྐྱེ་བ་ལྔ་ཁོ་ན་ཡིན་ཞེ་ན། བསམ་གཏན་བཞི་པ་སྤེལ་མར་བསྒོམ་པར་བཤད་པ་གང་ཡིན་པ།

[Block 3456 [VERSE]]
དེ་ནི་རྣམ་པ་ལྔ་ཡི་ཕྱིར། །
གནས་གཙང་སྐྱེ་བ་ལྔ་ཁོ་ན། །

[Block 3457]
སྤེལ་མར་བསྒོམ་པ་དེ་ནི་ཆུང་ངུ་དང་། འབྲིང་དང་། ཆེན་པོ་དང་། ཤིན་ཏུ་ཆེ་བ་དང་། ཤིན་ཏུ་ཆེས་ཆེ་བའི༌[^1360]བྱེ་བྲག་གིས་རྣམ་པ་ལྔ་ཡིན་ཏེ། ཕྱི་མ་རེ་རེ་ལ་གསུམ་གསུམ་དུ་སྤེལ་བར་བྱས་ནས་སོ། །

[Block 3458]
བར་མ་ཟག་པ་དང་བཅས་པ་ལས་སྐྱེའོ། །

[Block 3459 [VERSE]]
འགོག་པ་ཐོབ་པའི་ཕྱིར་མི་འོང་། །
ལུས་ཀྱི༌[^1361]མངོན་སུམ་བྱེད་པར་འདོད། །

[Block 3460]
ཕྱིར་མི་འོང་བ་གང་ལ་ལ་འགོག་པ་ཐོབ་པ༌[^1362]དེ་ནི་སེམས་མེད་པར་མྱ་ངན་ལས་འདས་པ་དང་འདྲ་བ་ལུས་ཀྱིས་མངོན་སུམ་དུ་བྱེད་པའི་ཕྱིར་ལུས་ཀྱིས་མངོན་སུམ་དུ་བྱེད་པ་ཞེས་བྱའོ། །

[Block 3461 [HEADING]]
##### དགྲ་བཅོམ་པ། ^6-2-2-4-0

[Block 3462 [VERSE]]
སྲིད་རྩེའི་བར་ཆ་བརྒྱད་ཟད་པ། །
དགྲ་བཅོམ་ཉིད་ལ་ཞུགས་པ་ཡིན། །

[Block 3463]
ཕྱིར་མི་འོང་བ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པ་སྟེ། ཡང་ཕྱིར་མི་འོང་བ་དེ་བསམ་གཏན་དང་པོའི་རྣམ་པ་གཅིག་ལས་འདོད་ཆགས་དང་བྲལ་བ་ནས་བཟུང་སྟེ། སྲིད་པའི་རྩེ་མོའི་བར་དུ་བརྒྱད་ཀྱི་བར་སྤངས་པས་དགྲ་བཅོམ་པ་ཉིད་བཞུགས༌[^1363]པ་ཡིན་ནོ། །

[Block 3464]
དགུ་པའི་བར་ཆད་མེད་ལམ་ཡང་། །དགྲ་བཅོམ་པ་ཉིད་ལ་ཞུགས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 3465]
དེ་ནི་རྡོ་རྗེ་ལྟ་བུ་ཡིན། །བར་ཆད་མེད་པའི་ལམ་དེ་ནི་ཕྲ་རྒྱས་ཐམས་ཅད་འཇོམས་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ཞེས་བྱའོ། །

[Block 3466]
ཡང་སྲིད་པའི་རྩེ་མོ་པའི་རྣམ་པ་དགུ་པར་བཤད་པ་གང་ཡིན་པ། དེ་ཟད་ཐོབ་དང་ཟག་པ་ཤེས། །

[Block 3467]
དང་པོ་ཉིད་དུ་ཟག་པ་ཐམས་ཅད་ཟད་པའི་ཐོབ་པ་དང་ལྷན་ཅིག་སྐྱེས་པའི་ཕྱིར་ཟད་པ་ཤེས་པ་ཡིན་ནོ། །

[Block 3468]
དེ་ཚེ་དེ་མི་སློབ་དགྲ་བཅོམ། །དགྲ་བཅོམ་པ་ཉིད་ལ་ཞུགས་པ་དེ་ཟད་པ་ཤེས་པ་སྐྱེས་ན་མི་སློབ་པ་དང་། དགྲ་བཅོམ་པའི་འབྲས་བུ་ཐོབ་པ་ཉིད་ཀྱི་ཕྱིར་དགྲ་བཅོམ་པའོ། །

[Block 3469]
འབྲས་བུ་གཞན་གྱི་ཕྱིར་བསླབ༌[^1364]པར་བྱ་བ་མེད་པའི་ཕྱིར་མི་སློབ༌[^1365]པའོ། །

[Block 3470 [HEADING]]
#### འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པས་འདོད་ཆགས་དང་བྲལ་བ། ^6-2-3-0
--- END BLOCKS ---
