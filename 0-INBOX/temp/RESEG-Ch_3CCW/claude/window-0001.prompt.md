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
[Block 36 [HEADING]]
### ཚིགས་བཅད་དང་པོ། ^1-2-0

[Block 37 [VERSE]]
གང་བློ་ཡོད་དང་མེད་པ་ལས། །
རྣམ་པར་འདས་ཤིང་མི་གནས་པ། །
དེ་དག་ཟབ་མོ་དམིགས་མེད་པའི། །
རྐྱེན་གྱི་དོན་ལ་རྣམ་པར་བསྒོམ། །

[Block 38]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 39]
གང་དག་འདས་པའི་སྲིད་པ་ན་སྟོང་པ་ཉིད་ལ་གོམས་པ་དེ་དག་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྟོགས་ཤིང་སྟོང་པ་ཉིད་མཐོང་བའི་ས་བོན་ཡོད་པའི་ཕྱིར་མཐུ་ཆེ་བ་ཡིན་ཏེ། ད་ལྟར་གྱི་དུས་ན་སྐྱེས་པའི་གོམས་པ་མཚར་པོ་ཆེ་མེད་ཀྱང་སྐྱེ་བོ་བྱིས་པའི་བློའི་སྤྱོད་ཡུལ་མ་ཡིན་པ་ཡོད་པ་དང་མེད་པའི་མཐར་རྟོག་པས་རྙོག་པའི་དྲི་མས་མ་སྦགས་པ་རྟེན༌[^24]ཅིང་འབྲེལ་པར་འབྱུང་བ་ཟབ་མོ་འཕགས་པ་ཤཱ་རིའི་བུ་ལ་སོགས་པས་ཁོང་དུ་ཆུད་པར་དམིགས་ཏེ། ཇི་ལྟར་འཇིག་རྟེན་ལས་དང་ཉོན་མོངས་རྒྱུར་བྱས་བྱེད་རྒྱུ་ལྡན་འབྱུང་བ། །ལས་དང་ཉོན་མོངས་པ་དག་ལྡོག་རྒྱུ་དེ་ཡང་འདྲེན་པས་རབ་ཏུ་གསུངས། །

[Block 40]
གང་ན་སྐྱེ་དང་རྒ་དང་རྒུད་པའི་སྡུག་བསྔལ་ངེས་པར་མི་གནས་པ། །ཐར་པ་མཆོག་དེ་སྨྲ་བའི་ཁྱུ་མཆོག་དེ་ཡིས་རང་གིས༌[^25]མཁྱེན་དེ་གསུངས། །

[Block 41]
ཚིགས་སུ་བཅད་པ་དེ་འཕགས་པ་ཤཱ་རིའི་བུས་ཐོས་པ་ཙམ་གྱིས་དེ་ཁོ་ན་རྟོགས་ཤིང་འབྱུང་སྟེ། དེ་བས་ན་དེ་ལྟར༌[^26]སྔོན་གོམས་པའི་མཐུ་ཉིད་ཀྱིས་དེ་དག་གི་བློ་ཡོད་པ་དང་མེད་པར་མཐོང་བ་ལས་འདས་སོ། །

[Block 42]
མཐའ་གཉིས་དེ་ལས་ལྷག་པའི་དབུས་མེད་པའི་ཕྱིར་དེ་ལ་ཡང་གནས་པ་མེད་པས་མི་གནས་སོ། །

[Block 43]
སྐྱེ་བོ་བྱིས་པ་རྣམས་ལ་འཇིགས་པར་བྱེད་པ་དང་། དེ་དག་འཇུག་མི་ནུས་པའི་ཕྱིར་ཟབ་པའོ། །

[Block 44]
རང་བཞིན་གྱིས་མི་སྐྱེ་བས་ཡོད་པ་དང་མེད་པའི་མཐའ་དང་དབུས་ཡོངས་སུ་བརྟག་པའི་ཡུལ་དུ་དམིགས་པར་མི་ནུས་པའི་ཕྱིར་དམིགས་སུ་མེད་དོ། །

[Block 45]
འཕགས་པ་དེ་དག་ཀྱང་རྐྱེན་གྱི་དོན་ལ་རྣམ་པར་སྒོམ་ཞེས་བྱ་བ་ནི་ཡེ་ཤེས༌[^27]མངོན་སུམ་དུ་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 46]
འཕགས་པ་མ་ཡིན་པ་ཤིན་ཏུ་ཕྱིན་ཅི་ལོག་པ་དག་གིས་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་དོན་དེ་ལྟར་རྟོགས་པར་མི་ནུས་ཏེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་སྒྲ་ཉིད་ཀྱིས་རང་བཞིན་གྱིས་སྐྱེ་བར་མངོན་པར་ཞེན་པས་སྟོང་པ་ཉིད་དུ་སྨྲ་བ་ལ་ཕྱིར་རྒོལ་བ་དང་དེ་བསྟན་པའི་རིགས་པ་བཙལ་བ་ལ་བརྩོན་པའི་ཕྱིར་འདིར་སྨྲས་པ། འཐད་པ་གང་གིས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དམིགས་ཤིང་ཡོད་པ་ཡང་མེད་པར་བརྟག་ནུས་པ༌[^28]གང་གི་ཕྱིར་འཕགས་པ་དག་ཡོད་པ་དང་མེད་པར་རྟོགས་པ་ལས་འདས་པའི་བློས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཟབ་མོ་ལ་རྣམ་པར་སྒོམ་པ་ཇི་ཙམ་དུ་དངོས་པོ་དམིགས་སུ་ཡོད་པ་དག་མེད་པར་མི་རུང་ངོ་། །གལ་ཏེ་མེད་དུ་ཟིན་ན་དེའི་ཚེ་བོང་བུའི་རྭ་བཞིན་དུ་དེ་ཡང་དམིགས་པར་མི་འགྱུར་རོ། །

[Block 47]
འཇིག་རྟེན་ཕ་རོལ་ནས་འདི་འོང་བ༌[^29]དང་། འཇིག་རྟེན་འདི་ནས་འཇིག་རྟེན་ཕ་རོལ་དུ་འགྲོ་བར་བསྟན་པ་ལས་དང་འབྲས་བུ་འབྲེལ་པར་འབྱུང་སྟེ་འཁོར་བའི་རྒྱུད༌[^30]མི་འཆད་པར་བསྟན་པའི༌[^31]ཕྱིར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡན་ལག་བཅུ་གཉིས་ཚེ་རབས་གསུམ་དུ་བཤད་པ་ཡང་མི་རུང་བར་འགྱུར་རོ། །

[Block 48]
ཆོས་མངོན་པ་ལས་ཕུང་པོ་དང་སྐྱེ་མཆེད་དང་། ཁམས་རྣམས་ཀྱི་རང་དང་སྤྱིའི་མཚན་ཉིད་བཤད་པ་ཡང་མི་རུང་བར་འགྱུར་རོ། །

[Block 49]
དེ་དག་ཐམས་ཅད་ཇི་ལྟར་བཤད་པ་བཞིན་དུ་འདུག་སྟེ་ཡོད་ན་རུང་བས་དེའི་ཕྱིར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་འདི་ཡོད་པའོ། །

[Block 50]
བཤད་པ། གལ་ཏེ་ཁྱོད་ཀྱིས།

[Block 51 [HEADING]]
### ཚིགས་བཅད་གཉིས་པ། ^1-3-0

[Block 52 [VERSE]]
[^32] ཉེས་པ་ཐམས་ཅད་འབྱུང་བའི་གནས། །
མེད་པ་རྣམ་པར་བཟློག་ཟིན་གྱིས། །

[Block 53]
དེ་དག་དགག་པར་སྒྲུབ་པའི་ཁོ་བོའི་ཉོན་མོངས་པ་ཡང་ཁྱོད་ཀྱིས༌[^33]བཀག་པས་ན་ཁྱོད་ཀྱིས༌[^34]བྱས་ཏེ་བསྟངས་སོ།[^35] །ཡང་བདག་གིས།

[Block 54 [VERSE]]
[^36] རིགས་པ་གང་གིས་ཡོད་པ་ཡང་། །
བཟློག་པར་བྱ་བ་མཉན་པར་གྱིས། །

[Block 55]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་སྐབས་ཡིན་པར༌[^37]རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 56]
ཡང་ན་མེད༌[^38]པ་ཅན་ལས་དང་འབྲས་བུར་འབྲེལ་པ་ལ་སྐུར་པ་འདེབས་པས་མེད་པར་ལྟ་བ་ཁས་བླངས་པ་གང་ཡིན་པ་དེ་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་དགེ་བའི་རྩ་བ་མ་ལུས་པ་སུན་འབྱིན་པར་གྱུར་པས་ཉེས་པ་ཐམས་ཅད་འབྱུང་བའི་རྒྱུར་གྱུར་པ་དང་། མི་དགེ་བའི་ཆོས་ཐམས་ཅད་སྩོགས་པའི་རྒྱུར་གྱུར་པའི་ཕྱིར་ཉེས་པ་ཐམས་ཅད་ཀྱི་འབྱུང་གནས་ཏེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཚེ་རབས་གསུམ་པ་དང་། སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྤྱིའི་ལས་ཀྱིས་བསྐྱེད་པ༌[^39]སྣོད་ཀྱི་འཇིག་རྟེན་སྣ་ཚོགས་རྣམ་པར་གཞོག་པ་ན། དེའི༌[^40]ཆོས་མངོན་པ་ལས་རྣམ་པར་བཟློག་གོ། །

[Block 57]
དེ་བས་ན་དེ་ལྟར་ཕ་རོལ་དག་ལ་གསལ་བའི་ཕྱིར་དེ་ཡང་རིགས་པ༌[^41]མི་བཤད་དོ། །

[Block 58]
ཡོད་པ་བཟློག་པ་ནི་དགེ་སློང་དག་འདི་ལྟ་སྟེ། མི་སླུ་བའི༌[^42]ཆོས་ཅན་མྱ་ངན་ལས་འདས་པ་འདི་ནི་བདེན་པའི་མཆོག་གཅིག་པུའོ། །

[Block 59]
འདུ་བྱེད་ཐམས་ཅད་སྣོད་ཀྱི་འཇིག་རྟེན་མི༌[^43]བརྫུན་པ་བསླུ་བའི་ཆོས་ཅན་ནོ། །

[Block 60]
ཀྱེ་མ་འདུ་བྱེད་རྣམས་མི་རྟག །ཅེས་བྱ་བ་ལ་སོགས་པ་བཤད་པ་ན། བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་སོ། །

[Block 61]
དེ་ལྟ་མོད་ཀྱི་དེ་ཕྱིར་ཞིང་བཏུད་དེ་གཞུང་གཅིག་ཏུ་མ་གསུངས་ལ། བྱིས་པ་དག་ཡུན་རིང་པོ་ནས་ཡོད་པར་ལྟ་བ་ལ་གོམས་པས་དེའི་ཕྱིར་ཐུབ་པའི་དབང་པོའི་གསུང་རབ་དེ་དང་དེ་དག་ལས་བཤད་པའི་གསུང་རབ་ལས་བཏུས་ཏེ། རབ་ཏུ་བྱེད་པ་འདིར་བསྡུས་པ་ཉིད་ཀྱིས། །

[Block 62 [VERSE]]
རིགས་པ༌[^44]གང་གིས་ཡོད་པ་ཡང་། །
བཟློག་པར་བྱ་བ་མཉན་པར་གྱིས། །

[Block 63]
རིགས་པ༌[^45]དེ་དག་གང་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར།

[Block 64 [HEADING]]
### ཚིགས་བཅད་གསུམ་པ། ^1-4-0

[Block 65 [VERSE]]
ཇི་ལྟར་བྱིས་པས་རྣམ་བརྟགས་བཞིན། །
དངོས་པོ་དེ་སྟེ་བདེན་གྱུར་ན། །
དེ་དག་དངོས་མེད་རྣམ་ཐར་དུ། །
གང་ཕྱིར་མི་འདོད་རྒྱུ་དེ་ཅི། །

[Block 66]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 67]
བཅོམ་ལྡན་འདས་ཀྱིས་དེ་དོན་སོ་སོ་ཡང་དག་པར་རིག་པ་དང་། ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པ་ལས་མཆོག་ཏུ་དགའ་བ་སྐྱེའོ། །

[Block 68]
རབ་ཏུ་དགའ་བ་ལས་བདེ་བ་སྐྱེའོ། །

[Block 69]
ཡིད་བདེ་བ་ལས་ལུས་ཤིན་ཏུ་སྦྱངས་པར་འགྱུར་རོ། །

[Block 70]
ལུས་ཤིན་ཏུ་སྦྱངས་པ་ལས་བདེ་བ་མྱོང་བར་འགྱུར་རོ། །

[Block 71]
བདེ་བ་ལས་སེམས་རྩེ་གཅིག་ཏུ་འགྱུར་རོ། །

[Block 72]
སེམས་རྩེ་གཅིག་པ་ལས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་པར་འགྱུར་རོ། །

[Block 73]
ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་མཐོང་བར་འགྱུར་རོ། །

[Block 74]
ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་རབ་ཏུ་ཤེས། ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་རབ་ཏུ་མཐོང་ན་ཡིད་འབྱུང་བར་འགྱུར་རོ། །

[Block 75]
ཡིད་བྱུང་ན་མི་ཆགས་པར་འགྱུར་རོ། །
--- END BLOCKS ---
