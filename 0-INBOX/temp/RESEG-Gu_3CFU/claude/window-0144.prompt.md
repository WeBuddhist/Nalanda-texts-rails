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
[Block 5041]
ཆུ་ནས་འདི་དག་ལ་བཏོན་པ་དང་རྗེས་སུ་བཟུང་བ་དེ་ལ་དེའི་ཚེ་ན་གཅོད་པ་ཞེས་བྱ་བའོ།

[Block 5042]
[^3417] །དེའི་ཚེ་ན་འདི་དག་ལ་རོ་ཉིད་ཁས་བླངས་པའོ། །

[Block 5043]
གང་ཞིག་སླར་བཅུག་པ༌[^3418]དག་ལ་དེ་ལྟ༌[^3419]ཉིད་དུ་རྗེས་སུ་འཇུག་པས་དེ་ཡང་ས་བོན་ཉིད་ལ་རྗེས་སུ་འཇུག་པ་ཉིད་ཀྱིས་ཉ་ལྕིབས་དང་ཉ་ཚང་དག་ལ་གང་ཞིག་ས་དང་མ་འབྲེལ་པས་ཆུའི༌[^3420]སྟེང་དུ་སྐྱེས་པ་དེ་ལ་འདི་བཤད་པའོ། །

[Block 5044]
ཚི་གུ༌[^3421]མ་བཅོམ་པར་རིལ་མིད་བྱེད་པ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཚི་གུ༌[^3422]མ་བཅོམ་པ་ཞེས་བྱ་བ་ནི་སོ་རྣམས་ཀྱིས་དུམ་བུར་མ་བྱས་པ་ལ་གང་ཞིག་རིལ་མིད་བྱེད་པ་ནི་ཟ་བར་བྱེད་པ་ལ་ཕྱེད་ཅེས་བྱ་བའི་ཚིག་སྨོས་པས་ནི་ཉེས་བྱས་ཡིན་པར་གོ་བར་བྱེད་དོ། །

[Block 5045]
ཕྱེད་ཀྱི༌[^3423]ཚིག་གིས༌[^3424]ཐམས་ཅད་དུ་ལྟུང་བ་གཅོད་པར་གྱུར་པའི་ཉེས་བྱས་སྟོན་པར་བྱེད་པའོ། །

[Block 5046]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས༌[^3425]རྒྱ་ཤུག༌[^3426]གི་ཚི་གུ༌[^3427]མ་བཅོམ་པར་རིལ་མིད་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5047]
འདི་ནི་ཚི་གུ༌[^3428]མ་བཅོམ་པ་ལྟར་ཉམས་པར་བྱེད་པ་དང་རིལ་མིད་བྱེད་པ་ཞེས་བྱ་བ་འདི་ལ་དོན་བྱས་པ་ཉིད་བཏབ་པ་དག་ལྟར་ལྟོར་བཅུག་པ་ལ་འདིར་བློས་ཡིན་གྱི་ཉམས་པའི་དོན་དུ་གཞག་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5048]
ལྟོ་བ་དང་འབྲེལ་པར་ཉམས་པ་ལ་འདིར་ལྟུང་བ་རྣམ་པར་གཞག་པར་མི་བྱ་བ༌[^3429]སྟེ། གང་ལ་འདིར་ཉམས་པའི་བློས་འབྱུང་བར་གྱུར་པ་དེ་ལ་དངོས་གཞིའི་ལྟུང་བ་བྱུང་བ་ཁོ་ན་ཡིན་ནོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 5049]
གལ་ཏེ་འདི་བཅད་པར་གྱུར་ན་ལེགས་སོ་ཞེས་སྨྲས་ན་བཏོན་པའི་འོ་ཞེས་བྱ་བ་ལ། བཏོན་པའི་འོ་ཞེས་བྱ་བ་ནི་བཏོན་པའི་ཕྱེད་ཅེས་བྱ་བར་སྦྱར་རོ། །

[Block 5050]
ལེགས་སོ་ཞེས་བྱ་བའི་བརྗོད་པ་འདི་ནི་བཏོན་པའི་ཕྱེད་ལ་འདི་ལྟར་བརྗོད་ཅིང་གཅོད་པར་བྱེད་ན༌[^3430]དངོས་གཞིའི་མཐའ་ཅན་གྱི་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5051]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 5052]
བཙུན་པ་དགེ་སློང་གིས༌[^3431]འདི་སྐད་ཅེས་འདིས་ཤིང་ལྗོན་པ་འདི་གཅད་པར༌[^3432]གྱུར་ན་ལེགས་སོ་སྟེས་སོ་ཞེས༌[^3433]མཆི་ཞིང་དེས་འགུམས་པར༌[^3434]བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5053]
རྫུ་འཕྲུལ་གྱིས་ན་མ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདི༌[^3435]ནི་རྣམ་པར་རོལ་པ་ཙམ་ཡིན་ཏེ་བྱ་བའི་ངོ་བོ་འཇུག་པ་འདི་མ་ཡིན་ཞེས་བྱ་བ་འདིས་ཤེས་པའོ། །

[Block 5054]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་རྫུ་འཕྲུལ་གྱིས་ཤིང་ལྗོན་པ་འགུམས་པར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེ་བ་འཁོར་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5055]
ས་བོན་ལ༌[^3436]ས་བོན་གཞན་ཉིད་དུ་འདུ་ཤེས་པ་ལ་འདི་དེ་དང་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རྩ་བའི་ས་བོན་ལ་སོགས་པ་ལ་སྡོང་བུའི་ས་བོན་ཉིད་དུ་འདུ༌[^3437]ཤེས་པ་ནི་དེ་དང་འདྲ་བ་ཉིད་དེ་ཕྱེད་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 5056]
འདིར་སྐྱོན་ནི་མཚུངས་ཏེ་སྲོག་གཅོད་པ་ལྟར་ན་སྨད་པ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5057]
སྐྱེ་བ་ལ་ཡང་ཆོ་ག་འདི་རྣམ་པར་གནས་པ་ཡིན་ཏེ། དེ་ཡང་འདིར་ས་བོན་ཉིད་ཀྱིས་བརྗོད་པར་རྟོགས་པར་བྱའོ། །

[Block 5058]
འདིར་ནི་རྩ་བ་ལ་སོགས་པའི་ས་བོན་ཉིད་ཡོད་པ་ཡིན་ཏེ། དེ་བས་ན་ས་བོན་སྐྱེ་བ་དག་ལ་ཡང་ཕན་ཚུན་ཉིད་དུ་ཕྱིན་ཅི་ལོག་སྟེ། འདི་ནི་དངོས་གཞིའི་ཁ་ན་མ་ཐོ་བ་སྟེ་མ༌[^3438]སྨད་པ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5059]
ཤུན་པ་དང་ཕྲི་དང་འདབ་མ་སྐྱ་བོ་དང་། མེ་ཏོག་ཁ་བྱེ་བ་དང་འབྲས་བུ་སྨིན་པ་རྣམས་ནི་ཕྱེད་ཤི་བ་ཉིད་དུ་རྗེས་སུ་ཐ་སྙད་གདགས་སོ་ཞེས་བྱ་བ་ནི་ཤུན་པ་དང་ཕྲི་དང་འདབ་མ་སྐྱ་བོ་དང་མེ་ཏོག་ཁ་བྱེ་བ་དང་། འབྲས་བུ་སྨིན་པ་དང་ཞེས་བྱ་བས༌[^3439]བསྡུ་བའོ། །

[Block 5060]
དེ་རྣམས་ནི་ཕྱེད་ཤི་བ་ཉིད་ཅེས་བྱ་བ་འདི་ལྟུང་བ་ན་སྨད་པ་ཉིད་དེ་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5061]
འདིར་རབ་ཏུ་གྲགས་པ་ལ་བློ་ལྟུང་བ་ནི་རྗེས་སུ་ཐ་སྙད་གདགས་པའོ། །

[Block 5062]
འདི་རྣམས་ལ་ཕྱེད༌[^3440]ཤི་བ་ཉིད་ནི་རབ་ཏུ་གྲགས་པ་ཁོ་ན་ཉིད་དེ༌[^3441]འདིར་སྟོན་བྱེད་ཀྱི་རྒྱུ་བཙལ་བར་བྱ་བ་ནི་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་འདི་ལས༌[^3442]འདི་ཡང་དག་པར་བསྟན་པའོ། །

[Block 5063]
དེ་དག་གི་རྩ་བར་གྱུར་པ་རང་བཞིན་ལས་མ་ཕྱེ་བ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་རང་བཞིན་ལས་ཕྱེ་བ་བྲལ་བ་དེ་ནི་འོག་ནས་ཤུན་པ་ལ་སོགས་པ་རྣམས་ལ་རྩ་བར་གྱུར་པ་དེ་ནི་ཕྱེད་ཤི་བ་ཉིད་དུ་རྗེས་སུ་ཐ་སྙད་གདགས་པ་མ་ཡིན་ཏེ། དེ་བས་ན་ཕྱོགས་ལས་འདི་རྣམས་སེལ་བར་བྱེད་པ་ལ་དངོས་གཞི་ཁོ་ནར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5064]
འདིར་ཤུན་པའི་གཞུང་ནི་ཤུན་པ་འཆུ་བར་བྱེད་ཅིང་སྙིང་པོ་དང་འབྲེལ་བ་འཆུ་བར་བྱེད་ན་ལྟུང་བྱེད་དུ་འགྱུར་རོ། །

[Block 5065]
སྙིང་པོ་དང་མ་འབྲེལ་པ་འཆུ་བར་བྱེད་ན་ནི་ཉེས་བྱས་སུ་འགྱུར་ཞེས་གསུངས་པ་ཡིན་ཏེ། ཕྲི་དང་འདབ་མ་སྐྱ་བོ་དང་མེ་ཏོག་ཁ་ཕྱེ་བ་དང་། འབྲས་བུ་སྨིན་པ་རྣམས་ལ་ཡང་འདི་ཉིད་རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བ་ཐམས་ཅད་ལས་གསུངས་སོ། །

[Block 5066]
འདབ་མ་དང་འབྲས་བུ་དག་ལ་འཇུག་པས་འཆུ་བ་ནི་དེ་དག་ཉིད་དང་ལྷན་ཅིག་ཆོས་མཚུངས་པ་ཡིན་ཏེ་སྨིན་པ་རྣམས་ཀྱི་ནི་སྨིན་པ་ཉིད་ཡིན་ལ་མ་སྨིན་པ་རྣམས་ཀྱི་ནི་མ་སྨིན་པ་ཉིད་ཡིན་ཏེ། དེ་དག་ཉིད་ཀྱི་ཕྱོགས་གཅིག་གྱུར་པ་ཉིད་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 5067]
གང་ཞིག་མེ་ཏོག་འཆུ་བའི༌[^3443]ངོ་བོ་ནི་མེ་ཏོག་ལ་འཇུག་པ་དེ་ལ་མེ་ཏོག་ཉིད་དེ་འཇུག་པར་གྱུར་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 5068]
དེ་བས་ན་འོག་ནས་གང་ཞིག་འདི་དག་ལ་དེ་ནི་འདི་རྣམས་ལ་འདིར་འཇུག་པ་འདི༌[^3444]བརྗོད་པར་རིག་པར་བྱའོ། །

[Block 5069]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་ཅིག་ཅར་འབྱུང་སྟེ་འཆུ་བ་གཅོད་ན་ཉེས་བྱས་སོ། །

[Block 5070]
ཕ་བོང་གི་དྲེག་པ་འཆུ་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5071]
འདིར་འཆུ་བ་ཞེས་བྱ་བའི་སྒྲས་ནི་ཨུཏྤ་ལ་ལ་སོགས་པ་ཁ་བྱེ་བའི་འཆུ་བ་དང་། འདབ་མའི་འཆུ་བ་བསྡུས་པ༌[^3445]རིག་པར་བྱའོ། །

[Block 5072]
འདིར་ཕ་བོང་གི་དྲེག་པ༌[^3446]ཞེས་བྱ་བ་ནི་རྡོའི་དྲེག་པ༌[^3447]ཡིན་པར་རིག་པར་བྱའི་སྲུ་སྲུ་ནི་མ་ཡིན་ནོ། །

[Block 5073]
ས་བོན་གྱི་ཁམས་བཏབ་པ་རྩ་བ་མ་སྐྱེས་པ་ནི་ཕྱེད་སྐྱེད་པ༌[^3448]ཉིད་དུའོ་ཞེས་བྱ་བ་ནི་ས་བོན་གྱི་ཁམས་བཏབ་པ་ལ་ད་དུང་རྩ་བ་མ་སྐྱེས་པ་ཉིད་དུ་རྗེས་སུ་ཐ་སྙད་གདགས་ཏེ། དེ་ལ་ནི་འདིར་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5074]
ས་འབུས་པ་དང་ཤ་མོ་དང་ཤ་བལ་དང་སྣོད་དང་གོས་ལ་སོགས་པའི་རླམ་རྣམས་ནི་ཕྱེད་སྐྱེས་པ༌[^3449]ཉིད་དུའོ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་ཐ་སྙད་གདགས་སོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 5075]
སྣོད་དང་གོས་ལ་སོགས་པ་རྣམས་ཀྱི་རླམ་གྱི་སྒྲ་དང༌[^3450]འབྲེལ་པ་ཡིན་གྱི། སྔ་མ་རྣམས་ཀྱིས་ཀྱང་མ་ཡིན་ནོ། །

[Block 5076]
འུ་ཤའི་ཁུ་ཚན་ལ་སོགས་པ་དབོ་བ་དང་འཆག་པ་དང་ཡལ་ག་ལ་སོགས་པ་འདྲེན་པ་དང་། དཀྱིལ་འཁོར་དང་སྐྱང་ནུལ་དག་ལ་དེ་དག་གི་བསམ་པ་ཉིད་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་དབོ་བ་ལ་སོགས་པའི་བསམ་པ་ཉིད་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5077]
མ་ཉམས་པའི་འདུན་པས་ལྟུང་བ་མེད་པ་ཉིད་དེ་ན་སྨད་པ་ནི་མ་ཡིན་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུ་མདོ་འདི་ཡིན་ནོ། །

[Block 5078]
རྟེན་ཉིད་ཀྱིས༌[^3451]ཡིན་ཏེ་དེ་བས་ན་འདིར་ལྟོས་པས་བསྲེག་པར་བྱ་བ་དང་འཐག་པར་བྱ་བ་ཉིད་ཀྱིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིར་ལྟུང་བ་མེད་པར་ཤེས་པའོ། །

[Block 5079]
ཕོངས་པའི་ཚེ་རྩྭ༌[^3452]ཀུ་ཤ་ལ་སོགས་པས་བཅིངས་པ་དེས་མི་ཐར་ན་བཅད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་གི་སྒྲས་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་འདིའི་རྗེས་སྙེགས༌[^3453]པའི་དོན་དུའོ། །

[Block 5080]
རྩྭ༌[^3454]ཀུ་ཤ་ལ་སོགས་པས་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས་གླེང་གཞིའི་དབང་གིས་རྩྭ༌[^3455]ཀུ་ཤ་རྣམས་ཉིད་ལ་འདི་གསུངས་ཏེ། སེམས་ཅན་གྱི་གྲངས་ལས་གཞན་ཐམས་ཅད་ལ་གཅོད་པར་བྱེད་པ་ལ་རྣམ་པར་གཞག་པ་བྱ་བ་ནི་སོགས་པའི་ཚིག་གོ། །
--- END BLOCKS ---
