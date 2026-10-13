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
[Block 771]
སྐྱེ་འཇིག་བསྟན་ཕྱིར་མྱང༌[^573]འདས་ཀྱི། །ལམ་བསྟན་མ་ཡིན་ཞེས་སོ། །

[Block 772]
སླར་ཡང་ཅིའི་ཕྱིར་ན་སྐྱེ་འཇིག་བསྟན་པ་ལས་ཐར་པ་མེད་ཅེས་ཉེ་བར་བསྟན་པར༌[^574]མྱ་ངན་ལས་འདས་པའི་ལམ་བསྟན་པར་ཡང་མི་འཐད་དོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པ། སྟོང་ཉིད་ཕྱིར་ཞེས་པའོ། །

[Block 773]
སྐྱེ་བ་དང་འཇིག་པ་དག་སྟོང་ན་ཇི་ལྟར༌[^575]དག་བསྟན་པ༌[^576]མྱ་ངན་ལས་འདས་པའི་ལམ་བསྟན་པར་འགྱུར། སླར་ཡང་ཉེ་བར་དམིགས་བཞིན་པ་སྐྱེ་བོ་ཐམས་ཅད་ལ་གྲགས་པའི་སྐྱེ་བ་དང་འཇིག་པ་དག་ཇི་ལྟར་སྟོང་པ་ཉིད། ཇི་ལྟར་ཉེ་བར་མ་དམིགས་པ་དེ་དག་ཀྱང་སྟོང་པ་ཉིད་ལ་དེ་ལྟར་བསྟན་པའི་ཕྱིར་གསུངས་པ། འདི་དག་ཕན་ཚུན་བཟློག་པ་རུ།[^577] །མཐོང་བ་ཕྱིན་ཅི་ལོག་ལས་ཡིན། བདེན་ཏེ། སྐྱེ་བ་དང་འཇིག་པ་དག་སྟོང་པ་ཉིད་ཀྱི་ཕྱིར། དེ་དག་སྟོང་པ་ཉིད་ཡིན་ཀྱང་གང་འཇིག་རྟེན་པས་མཐོང་བ་ཕྱིན་ཅི་ལོག་པས་འཇུག་པའོ། །

[Block 774]
དེ་དག་འདི་ལྟར་ཇི་ལྟར་རྟོགས་ཤེ་ན། ཕན་ཚུན་བཟློག་པ་ལས་ཏེ། ཕྱིན་ཅི་ལོག༌[^578]པས་ན་ཕན་ཚུན་བཟློག་པ་སྟེ། གཞན་དུ་འགྱུར་བ་ཐོབ༌[^579]པའོ། །

[Block 775]
གལ་ཏེ་སྐྱེ་བ་དང་འཇིག་པ་དག་རང་གི་ངོ་བོས་ཡོད་ན་འདི་དག་ཕན་ཚུན་བྱས་པས་གཞན་དུ་འགྱུར་བར་མི་འགྱུར་ཏེ། སྐྱེ་བ་ལས་གཞན་པ་མ་སྐྱེས་པ་ལ་འཇིག་པ་མེད་ལ། སྐྱེ་བའི་དུས་ན་ཡང་སྐྱེ་བའི་དུས་དང་འགལ་བའི་འཇིག་པ་མི་རིགས་པའི་ཕྱིར་དང་། འཇིག་པ་དང་བྲལ་བ་ཡང་སྐྱེ་བ་མེད་པའི་ཕྱིར་དང་། འཇིག་པའི་དུས་སུ་ཡང་དེ་དང་འགལ་བའི་སྐྱེ་བ་མི་རུང་བའི་ཕྱིར་དང་། ཕན་ཚུན་ལས་དུས་གཅིག་ཏུ་སྐྱེ་བ་ཐོབ་པ༌[^580]འགལ་བ་དང་། ཕན་ཚུན་མེད་པས་འདི་དག་གསལ་བའི༌[^581]ཕྱིར་ཕན་ཚུན་བཟློག་པར་འགྱུར་རོ། །

[Block 776]
སྐྱེ་བ་ནི་སྐྱེ་བའི་རང་གི་ངོ་བོ་དང་བྲལ་བའི་ཕྱིར་ཕྱིན་ཅི་ལོག་གོ། །

[Block 777]
ཡང་ན་འགག་པ་ལ་མ་ལྟོས་པར་སྐྱེ་བར་མི་འགྱུར་རོ་ཞེས་བྱའོ། །

[Block 778]
སྐྱེ་བའི་ཕྱིན་ཅི་ལོག་ནི་རང་གི་ངོ་བོས་མ་གྲུབ་པ་དང་འགག་པ་ལ་ལྟོས་པའི་ཕྱིར་དང་། འདི་ལྟར་འགག་པ་ཡང་བརྗོད་དེ། གང་ཡང་འདི་དག་ཕན་ཚུན་བཟློག་པ་ཕན་ཚུན་བྱས་པས་འགྲུབ་ལ། དེ་འདི་ལྟར་རང་གི་ངོ་བོས་མ་གྲུབ་པ་དག་གང་མཐོང་བ་དེ་འཇིག་རྟེན་པའི་ཕྱིན་ཅི་ལོག་ཅེས་ཤེས་པར་བྱའོ། །

[Block 779]
གང་ཡང་དེ་དག་དེ་ལྟ་བས་ན་དེས་ན་སྐྱེ་བ་དང་འཇིག་པ་དག་སྟོང་པའོ། །

[Block 780]
གང་གི་ཚེ་དེ་དག་སྟོང་པ་ཉིད་ན་དེའི་སྐྱེ་བ་དང་འཇིག་པ་བསྟན་པ་ལས་མྱ་ངན་ལས་འདས་པར་འགྱུར་རོ་ཞེས་ཉེ་བར་བསྟན་པའི་མྱ་ངན་ལས་འདས་པའི་ལམ་བསྟན་པར་མི་འཐད་དོ། །

[Block 781]
བྱིས་པའི་སྐྱེ་བོས་རྟོགས་པའི་དོན་དུ་དེས་མཐོང་བའི་རྗེས་སུ་འཇུག་པས་བཅོམ་ལྡན་འདས་ཀྱིས་སྐྱེ་བ་དང་འཇིག་པ་གསུངས་པར་ཤེས་པར་བྱའོ། །

[Block 782]
ཇི་ལྟར༌[^582]དུ།

[Block 783 [VERSE]]
[^583]སྐྱེ་བ་ཤེས་པས་འཇིག་པ་ཤེས། །
འཇིག་པ་ཤེས་པས་མི་རྟག་ཤེས། །
མི་རྟག་ཉིད་ལ་འཇུག་ཤེས་པས། །
དེས་ནི་ཆོས་ཀྱང་རྟོགས་པར་འགྱུར། །

[Block 784]
ཞེས་སོ། །

[Block 785]
འདིར་སྨྲས་པ།

[Block 786 [HEADING]]
### ཚིགས་བཅད་ཉེར་བཞི་པ། ^1-24-0

[Block 787 [VERSE]]
སྐྱེ་མེད་འགག་པ་མེད་ཅེ་ན། །
ཅི་ཞིག་འགགས་པས་མྱ་ངན་འདའ། །

[Block 788]
གང་ཞིག་སྐྱེ་བ་དང་འཇིག་པ་མེད་ན་དེའི་ཚེ་སྡུག་བསྔལ་མེད་ལ་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་དག་སྐྱེས་པ་མི་རྟག་པས་སྡུག་བསྔལ་ལ། དེ་འགགས་པ་ལས་མྱ་ངན་ལས་འདས་པའོ། །

[Block 789]
གང་གི་ཚེ་སྐྱེ་བ་དང་འགགས་པ༌[^584]གང་ཡང་མེད་པས་སྡུག་བསྔལ་མེད་པ་དེའི་ཚེ་ཅི་ཞིག་འགགས་པས༌[^585]མྱ་ངན་ལས་འདས་པར་འགྱུར། འདི་ལྟར་སྡུག་བསྔལ་འགག་པ༌[^586]ལས་མྱ་ངན་ལས་འདས་པ་ཡང་ཡོད་ལ། དེའི་ཕྱིར་སྐྱེ་བ་དང་འཇིག་པ་དག་ཡོད་དོ་ཞེ་ན། སྨྲས་པ། འདི་ལ་སྐྱོན་མེད་དེ། གང་གི་ཕྱིར་འགགས་པ་ལས་མྱ་ངན་ལས་འདས་པར་རྣམ་པར་གཞག་པ་མ་ཡིན་ལ། དེ་ནི་སྡུག་བསྔལ་མེད་པ་ཉིད་དེ།

[Block 790]
སྐྱེ་བ་མེད་ཅིང་འགག་མེད་པའི། །ངོ་བོ་གང་ཞིག་ཐར་མིན་ནམ། །

[Block 791]
ངེས་པར་ཡང་འདི་ལྟར༌[^587]ཁས་བླང་བར༌[^588]བྱའོ། །

[Block 792]
གཞན་དུ་ན།

[Block 793 [HEADING]]
### ཚིགས་བཅད་ཉེར་ལྔ་པ། ^1-25-0

[Block 794 [VERSE]]
གལ་ཏེ་འགགས་ལས་མྱང་འདས་ཆད། །
གལ་ཏེ་ཅིག༌[^589]ཤོས་ལྟར་ན་རྟག །
དེ་ཕྱིར་དངོས་པོ་དངོས་མེད་དག །
མྱ་ངན་འདས་པར་རུང་མ་ཡིན། །

[Block 795]
གལ་ཏེ་སྡུག་བསྔལ་རང་བཞིན་གྱིས་མ་སྐྱེས་པ་དང་མ་འགགས་པར་མི་འདོད་ལ། སྡུག་བསྔལ་གྱི་ངོ་བོའི་རྒྱུན་ལས་ལོག་པ་ལ་མྱ་ངན་ལས༌[^590]འདས་པར་ཡོངས་སུ་རྟོགས༌[^591]ན། དེ་ནི་སྡུག་བསྔལ་རྒྱུན་ཆད་པའི་རང་བཞིན་གྱི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་ཆད་པར་འགྱུར་རོ་ཞེས་བྱ་ལ། མྱ་ངན་ལས་འདས་པ་ཆད་པར་འགྱུར་བ་མི་འཐད་དེ། མཐར་འཛིན་པར་ལྟ་བར་ཐལ་བ་དང་། ངོ་བོ་ཉིད་ཀྱིས་མ་གྲུབ་པ་ལས་རྒྱུན་ཆད་པའི་མྱ་ངན་ལས་འདས་པ་དེ་ཕྱིན་ཅི་ལོག་ཏུ་འགྱུར་ལ། མྱ་ངན་ལས་འདས་པ་ཕྱིན་ཅི་ལོག་མ་ཡིན་པའི་ཕྱིར། སྡུག་བསྔལ་རྒྱུན་ཆད་པའི་རང་བཞིན་མྱ་ངན་ལས་འདས་པར་མི་འཐད་དོ། །

[Block 796]
ཡང་ན་སྐྱོན་འདི་དག་ཡོངས་སུ་སྤང་བར་འདོད་ནས། དེ་ལ་ཅིག་ཤོས་ཁས་ལེན་ན། དེའི་ཚེ་སྡུག་བསྔལ་མ་འགགས་པའི་རང་བཞིན་ཉིད་ཀྱི་ཕྱིར། ཐེར་ཟུག་པས་མྱ་ངན་ལས་འདས་པ༌[^592]དེ་རང་བཞིན་དུ་འགྱུར་ལ། སྡུག་བསྔལ་རྟག་པའི་རང་བཞིན་མྱ་ངན་ལས་འདས་པར་འགྱུར་བར༌[^593]མི་རུང་སྟེ། དེ་ནི་སྡུག་བསྔལ་ཟད་པའི་མཚན་ཉིད་དུ་ཉེ་བར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 797]
གང་གི་ཚེ་འདི་ལྟར་དངོས་པོ་དང༌[^594]དངོས་པོ་མེད་པ་དག་མི་རུང་བས། དེའི་ཕྱིར་སྡུག་བསྔལ་རང་བཞིན་གྱིས་གང་མ་སྐྱེས་ཤིང་མ་འགགས་པ་དེ་ཉིད་ཐར་པ་ཞེས་རིགས་སོ། །

[Block 798]
འདིར་སྨྲས་པ། སྡུག་བསྔལ་ལས་ལོག་པའི་རང་བཞིན་མྱ་ངན༌[^595]ལས་འདས་པ་མ་ཡིན་ཏེ། གལ་ཏེ་འདི་ལྟར་འགྱུར་ན་དེའི་ཚེ་སྡུག་བསྔལ་ལས་ལོག་པའི་རང་བཞིན་ནི་ཅི་ཡང་མ་ཡིན་པའི་ཕྱིར། མྱ་ངན་ལས༌[^596]འདས་པ་ཞེས་བྱ་བ་ཅི་ཡང་མ་ཡིན་པར་འགྱུར་ལ། ཅི་ཡང་མ་ཡིན་པ་མྱ་ངན་ལས་འདས་པར་འགྱུར་བར་མི་རིགས་ཏེ། ལམ་གྱི་བདེན་པས་ཐོབ་བྱ། སྐྱེ་བ་འགགས་པར་གྱུར་པའི་ཆུ་སྐྱེགས་པའི་སྐྱེགས་ཀྱི་གནས་ལྟ་བུ་སྡུག་བསྔལ་ལས་དོན་གཞན་དུ་གྱུར་པ་ལ་འགོག་པ་ཞེས་བརྗོད་དོ། །

[Block 799]
གལ་ཏེ་དེ༌[^597]དོན་གཞན་དུ་གྱུར་པ་མ་ཡིན་ན། བདེན་པ་བཞི་རྣམ་པར་གཞག་པ་མི་འབྱུང་ལ། དེས་ན་འགོག་པ་སྡུག་བསྔལ་རྟག་པའི་རང་བཞིན་མ་ཡིན་ལ། སྡུག་བསྔལ་ལོག་པའི་རང་བཞིན་ཡང་མ་ཡིན་ཏེ། སྡུག་བསྔལ་ལས་དོན་གཞན་དུ་གྱུར་པའི་ཕྱིར་ཞེས་པའི་ཕྱིར་ཞེས་པའོ།

[Block 800]
[^598] །འདིར་གསུངས་པ།

[Block 801 [HEADING]]
### ཚིགས་བཅད་ཉེར་དྲུག་པ། ^1-26-0

[Block 802 [VERSE]]
གལ་ཏེ་འགོག་པར་འགའ་གནས་ན། །
དངོས་པོ་ལས་གཞན་དེ་ཡོད་འགྱུར། །
དངོས་པོ་མེད་ཕྱིར་འདི་མེད་ལ། །
དངོས་པོ་མེད་ཕྱིར་དེ་ཡང་མེད། །

[Block 803]
གལ་ཏེ་སྡུག་བསྔལ་གྱི་དངོས་པོ་ལས་གཞན་དུ་སྟེ། དེ་ལས་ཐ་དད་པའི་འགོག་པར་གྱུར་ན། རྟག་པར་གནས་པར་གྱུར་ཏེ། དེ་དངོས་པོ་ལས་ཀྱང་གཞན་དུ་འགྱུར་ལ། དེ་ནི་དངོས་པོ་ལས་གཞན་དུ་ཡོད་པ་ཉིད་འཐད་པ་མ་ཡིན་ཏེ། སྡུག་བསྔལ་ལས་གཞན་དུ་དེ་འགགས་པ་རྣམ་པར་གཞག་པར་མི་ནུས་སོ། །

[Block 804]
གལ་ཏེ་ཡང་སྡུག་བསྔལ་ལས་ཐ་དད་ན་འགོག་པ་རྟག་པར་འགྱུར་ལ། དེར༌[^599]གྱུར་ན་འཇིག་རྟེན་པ་ཐམས་ཅད་ལ་སྡུག་བསྔལ་ལོག་པར་འགྱུར་རོ། །

[Block 805]
སྡུག་བསྔལ་ལས་ལོག་པ་དེས་འཐོབ་པོ༌[^600]ཞེ་ན། ཐོབ་པར་གྱུར་ན་གང་གིས་སྡུག་བསྔལ་སྐྱེས་པ་འགག་པར་བྱས་ནས༌[^601]འདིའི་ཁྱད་པར་ཅི་ཞིག་སྐྱེད་པར་བྱེད། དེ་ཐོབ་པའི་རྒྱུད་ལ་སྐྱེའོ་ཞེ་ན། ཕྱིས་ཅི་ཞིག་འདིའི་ཁྱད་པར་སྐྱེ་བ་གང་གིས་དེ་ཐོབ་པའི་རྒྱུད་ལ་སྐྱེ་ན། དུས་ཐམས་ཅད་དུ་དེ་ཐོབ་པའི་རྒྱུད་ལ་སྐྱེ་བར་འགྱུར་བའམ། ནམ་ཡང་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 806]
དེ་ལས་ལམ་བསྒོམས༌[^602]པ་འཇིག་རྟེན་པ་ཐམས་ཅད་ཀྱིས་མ་བཙལ༌[^603]བར་ཡང་མྱ་ངན་ལས་འདའ་བར་འགྱུར་རོ། །

[Block 807]
དེའི་ཕྱིར་ངེས་པར་སྡུག་བསྔལ་ལ་ལྟོས་པ་དང་བཅས་པའི་རང་བཞིན་གྱིས་དེ་འབྱུང་བར་འགྱུར་ལ། དེ་ལ་ཡང་སྡུག་བསྔལ་མི་སྲིད་པའོ། །

[Block 808]
དེས་ན།

[Block 809 [VERSE]]
དངོས་པོ་མེད་ཕྱིར་འདི་མེད་དེ། །
སྡུག་བསྔལ་མེད་པས་དེ་མེད་དོ། །

[Block 810]
ཞེས་པའི་དོན་ཏོ།[^604] །
--- END BLOCKS ---
