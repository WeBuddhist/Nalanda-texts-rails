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
[Block 526]
གང་གནས་པའི་རྐྱེན་ལ་རག་ལས་པ་དེ་གཟུགས་བརྙན་བཞིན་དུ་ངོ་བོ་ཉིད་མེད་པར་གྲུབ་པ་ཡང་རིགས་སོ། །

[Block 527]
གང་ངོ་བོ་ཉིད་དུ་གྲུབ་པ་དེ་ནི་རང་བཞིན་གྱིས་མི་འགྱུར་བས་གནས་པའི་རྐྱེན་མེད་ཀྱང་ལྡོག་པ་མི་རིགས་སོ། །

[Block 528]
གང་གནས་པའི་རྐྱེན་མེད་ན་ལྡོག་པ་དེ་ནི་གཟུགས་བརྙན་བཞིན་དུ་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་མེད་པར་འོས་སོ། །

[Block 529]
གང་དེ་ལྟར་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་མེད་པ་དེ་གཞན་གྱིས་ཇི་ལྟར་ཡོད་པར་ཁོང་དུ་ཆུད་པའི་རྒྱུ་མེད་པས་དེ་ཡོད་པ་ཉིད་དུ་མི་རིགས་སོ་ཞེས་བྱ་བར་དགོངས་སོ། །

[Block 530]
མུ་སྟེགས་ཅན་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་མི་སྨྲ་བ་རྣམས་ཀྱི་དངོས་པོ་རྣམས་ལ་ངོ་བོ་ཉིད་ཡོད་པར་མངོན་པར་ཞེན་པ་གང་ཡིན་པ་དེ་ནི་རང་གི་གྲུབ་པའི་མཐའ་ལས་བྱུང་བ༌[^324]དང་མི་འགལ་བས།

[Block 531 [HEADING]]
### ཚིགས་བཅད་བཞི་བཅུ་པ། ^1-41-0

[Block 532 [VERSE]]
གལ་ཏེ་ཡོད་པར་སྨྲ་བ་རྣམས། །
དངོས་ལ་ཞེན་པར་གནས་པ་ནི། །
ལམ་དེ་ཉིད་ལ་གནས་པ་སྟེ། །
དེ་ལ་ངོ་མཚར་ཅུང་ཟད་མེད། །

[Block 533]
གྲངས་ཅན་གྱིས་རང་གི་གྲུབ་པའི་མཐའ་ལས་ཡོན་ཏན་སྙིང་སྟོབས་དང་། རྡུལ་དང་མུན་པ་གསུམ་རྟག་པར་ལོབས་ལ། བྱེ་བྲག་པས་ཀྱང་རང་གི་གྲུབ་པའི་མཐའ་ལས་ས་དང་། ཆུ་དང་མེ་དང་རླུང་གི་རྡུལ་ཕྲ་རབ་ཡན་ལག་ཅན་མ་ལུས་པའི་དངོས་པོ་རྩོམ་པ་རྟག་པ་ཉིད་དུ་ལོབས་ནས་རྟག་པའི་དངོས་པོར་སྨྲ་བའི་ཕྱིར་གལ་ཏེ་དངོས་པོ་ལ་ཞེན་པར་གནས་པ་དང་ངོ་བོ་ཉིད་བཟུང་ནས་གནས་པ་དེ་ལ་ནི་བློ་མཆོག་དང་ལྡན་པ་དག་ངོ་མཚར་དུ་འཛིན་པ་ཅུང་ཟད་ཀྱང་མེད་དེ་ཡ་མཚན་དུ་བྱ་བ་ཅུང་ཟད་ཀྱང་མེད་པ་ཡིན་ནོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་མི་སྲིད་པའི་དངོས་པོ་ལ་བརྟེན་པ་ནི་འཇིག་རྟེན་ན་ངོ་མཚར་གྱི་རྒྱུ་ཡིན་ནོ། །

[Block 534]
སྲིད་པའི་དངོས་པོ་ལ་བརྟེན་པ་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། དེ་རིགས་པའི་ཕྱིར་རོ། །

[Block 535]
རང་གི་གྲུབ་པའི་མཐའ་ལས་ཡོད་པར་བསྟན་པ་སྟོན་ཞིང་ཁོང་དུ་ཆུད་པ་ལ་ནི་ངོ་མཚར་གྱི་རྒྱུ་མེད་པས་ངོ་མཚར་ཅུང་ཟད་ཀྱང་མེད་པར་རིགས་སོ། །

[Block 536]
བྱེ་བྲག་ཏུ་སྨྲ་བ་དང་། མདོ་སྡེ་པ་དང་། རྣམ་པར་ཤེས་པ་ཙམ་དུ་སྨྲ་བ་གྲུབ་པས༌[^325]མཐའ་ལས་ཡོད་པ་མི་སྲིད་པ་ཡོངས་སུ་སྟོན་པ་ནི་བློ་མཆོག་དང་ལྡན་པ་དག་ལ་མཆོག་ཏུ་ངོ་མཚར་བསྐྱེད་པ་ཡིན་ནོ། །

[Block 537]
དེ་དག་ལ།

[Block 538 [HEADING]]
### ཚིགས་བཅད་ཞེ་གཅིག་པ། ^1-42-0

[Block 539 [VERSE]]
[^326]སངས་རྒྱས་ལམ་ལ་བརྟེན་ནས་ནི། །
ཐམས་ཅད་མི་རྟག་སྨྲ་བ་རྣམས། །
རྩོད་པ་ཡིས་ནི་དངོས་པོ་ལ། །
ཆགས་གནས་གང་ཡིན་དེ་སྨད༌[^327]དོ། །

[Block 540]
རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ནི་སངས་རྒྱས་པའི་ལམ་ཡིན་ཏེ། དེ་ལ་བརྟེན་ནས་འདུ་བྱེད་དེ་དག་ཐམས་ཅད་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་ཕྱིར་མི་རྟག་པའོ། །ཞེས་དེ་སྐད་ཁས་ལེན་ཀྱང་དངོས་པོ་རྣམས་ཀྱི་རང་གི་ངོ་བོ་གྲུབ་པར་སྟོན་པར་འདོད་པ་དེ་སྟོང་པ་ཉིད་དུ་སྨྲ་བ་ལ་རྩོད་པར་བྱེད་ཅིང་དེ་མི་སྲིད་པའི་དངོས་པོ་ལ་བརྟེན་པ་ནི་ངོ་མཚར་ཆེ་བས་དེ་རྨད་དུ་གྱུར་པའོ། །

[Block 541]
ངོ་མཚར་ཆེ་བ་དེ་ཡང་འཇིག་རྟེན་ན་ཡ་མཚན་དུ་གྱུར་པས་རྨད་དུ་བྱུང་བ་ཞེས་བྱའོ། །

[Block 542]
དེ་ལྟར་ཐམས་ཅད་ཀྱང་མི་རྟག་པར་སྨྲ་བ༌[^328]ལ་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་ལམ་ཁས༌[^329]ལེན་པར་གྱུར་ཀྱང་དངོས་པོའི་ངོ་བོ་ཉིད་སྟོན་ཅིང༌[^330]རློམ་པར་གནས་པ་ནི་རྟ་དམུ༌[^331]རྒོད་བོང༌[^332]བུའི་སྤྱོད་པ་ལྟར་བཅོས་པ་བཞིན་དུ་མཁས་པ་དག་ལ་རབ་ཏུ་ངོ་མཚར་དུ་འགྱུར་རོ། །

[Block 543]
ཕྱག་བྱ་བར་འོས་པ༌[^333]མ་ཡིན་པ་ལ་ཕྱག་འཚལ་ལོ་ཞེས་བྱ་བའི་ཚིག་བཞིན་དུ་རྨད་དུ་བྱུང་བའི་སྒྲ་བསྟོད་པའི་ཚིག་འདི་ཡང་བསྟིང་བ་ཡིན་ནོ། །

[Block 544]
རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཁས་ལེན་པ་སངས་རྒྱས་པའི་ལམ་ལ་བརྟེན་པ་དག །

[Block 545 [HEADING]]
### ཚིགས་བཅད་ཞེ་གཉིས་པ། ^1-43-0

[Block 546 [VERSE]]
དེ་ནི་འདི་ཞེས་གང་དག་ལ། །
བརྟགས་ན་རབ་ཏུ་མི་དམིགས་ན། །
བདེན་པ་དེ་ནི་འདིའོ་ཞེས། །
རྩོད་པས་མཁས་པ་སུ་ཞིག་སྨྲ། །

[Block 547]
འདི་ལྟར་གཟུགས་དང་ཚོར་བ་དང་། རྣམ་པར་ཤེས་པ་དང་། འདུས་བྱས་གཞན་ཐམས་ཅད་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་པའོ། །

[Block 548]
གང་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་པ་དེའི་མཚན་མ་དམིགས་སུ་མེད་པའི་ཕྱིར་གཟུགས་དེ་ནི་འདིའོ། །

[Block 549]
ཚོར་བ་དེ་ནི་འདིའོ། །

[Block 550]
རྣམ་པར་ཤེས་པ་དེ་ནི་འདིའོ། །

[Block 551]
འདུས་བྱས་གཞན་དེ་ནི་འདིའོ་ཞེས་བློ་ལ་རྣམ་པ་ཐམས་ཅད་དུ་མི་སྣང་སྟེ། དེ་ལྟར་གང་གིས་ཀྱང་བྱེ་བྲག་ཏུ་མི་སྣང་བ་གང་ཡིན་པ་དེ༌[^334]ནི་འདིའོ་ཞེས་གཞན་ལ་བསྟན་པར་མི་ནུས་སོ། །

[Block 552]
གང་བསྟན་པར་མི་ནུས་པ་དེ་ལ་ཤེས་རབ་ཅན་དག་རྩོད་པ་སྨྲ་བ་ནི་མི་རིགས་སོ། །

[Block 553]
རྩོད་པ་ཞེས་བྱ་བ་ནི་གང་ལ་བདག་གི་ཕྱོགས་སྒྲུབ་པ་དང་། གཞན་གྱི་ཕྱོགས་གཞིག་པའོ། །

[Block 554]
དེ་ལྟར་དངོས་པོ་གང་ཡང་མི་དམིགས་ན་རང་གིས་ཁས་བླངས་པ་དངོས་པོ་བདེན་པ་གང་ཡིན་པ་དེ་ནི་འདིའོ་ཞེས་བསྟན་པར༌[^335]བྱ་བ་དེ་ཅུང་ཟད་ཀྱང་ཡོད་པར་ག་ལ་འགྱུར། གཞན་གྱིས་ཁས་བླངས་པའི་དངོས་པོ་བརྫུན་པ་གང་ཡིན་པ་དེ་ནི་འདིའོ་ཞེས་བསྟན་པར་བྱ་བ་དེ་ཡང་ཅུང་ཟད་ཀྱང་ཡོད་པར་ག་ལ་འགྱུར། དེ་ལྟར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་དོན་རང་བཞིན་གྱིས་སྐྱེ་བ་མེད་པའི་དོན་དུ་ཁོང་དུ་མ་ཆུད་པ་ཤིན་ཏུ་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་དག་གིས།

[Block 555 [HEADING]]
### ཚིགས་བཅད་ཞེ་གསུམ་པ། ^1-44-0

[Block 556 [VERSE]]
མ་བརྟན་པར༌[^336]ནི་གང་དག་གིས། །
བདག་གམ་འཇིག་རྟེན་མངོན་ཆགས་པ། །
རྟག་དང་མི་རྟག་སོགས་ལྟ་བས། །
ཀྱེ་མ་དེ་དག་འཕྲོགས་པ༌[^337]ཡིན། །

[Block 557]
གང་དག་ཕུང་པོ་ལྔ་གཟུགས་བརྙན་ལྟ་བུ་རང་བཞིན་མེད་པ་ལ་བརྟེན་ནས་བདག་ཏུ་མི་འདོགས་ཀྱི། སེམས་རང་གི་མཚན་ཉིད་དུ་གྲུབ་པ་ལ་བདག་གོ་ཞེས་རྣམ་པར་འཇོག་པ་དེ་དག་གདོན་མི་ཟ་བར་ལྟ་བའི་ཆུ་བོ་ཆེན་པོས་མྱ་ངན་ལས་འདས་པའི་ལམ་ལས་དེད་ཅིང་ཁྱེར་བར་འགྱུར་རོ། །ཇི་ལྟ༌[^338]ཞེ་ན། དེ་ལ༌[^339]སེམས་ངོ་བོ་ཉིད་དུ་གྲུབ་པར་འདོད་ན་ཡང་ན་ནི་རྟག་པར་འགྱུར། ཡང་ན་ནི་མི་རྟག་པར་འགྱུར་རོ། །

[Block 558]
གལ་ཏེ་རྟག་པར་འགྱུར་ན་དེའི་ཚེ་ཐེར་ཟུག་ཏུ་སྨྲ་བ་ཡིན་ནོ། །

[Block 559]
འོན་ཏེ་མི་རྟག་ན་དེའི་ཚེ་ཆད་པར་སྨྲ་བ་ཡིན་ཏེ། བྱུང་ནས་མེད་པར་གྱུར་པ་ནི་ཆད་པར་ལྟ་བ་ཡིན་ནོ། །

[Block 560]
དེ་ལྟར་དེ་དག་ཀྱེ་མ་ལྟ་བས་འཕྲོགས་པ་ཡིན་ནོ། །

[Block 561]
ཀྱེ་མ་ཞེས་བྱ་བའི་སྒྲ་ནི་སྨྲེ་སྔགས་འདོན་པའམ་ངེས་པར་རིག་པར་བྱའོ། །

[Block 562]
དེ་ལྟར་འཇིག་རྟེན་ཞེས་བྱ་བ་ཕུང་པོ་ལྔ་པོ་རང་གི་མཚན་ཉིད་ཀྱིས་གྲུབ་པར་འདོད་ན་ཡང་མཐུན་པར་སྐྱོན་དུ་འགྱུར་བར་སྦྱར་རོ། །

[Block 563]
ཡང་ན་འདི་ནི་དོན་གཞན་ཏེ། གངས་ཅན་ལ་སོགས་པ་གང་དག་མ་བརྟེན་པར་བདག་རྟག་པ་དང་། ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་དང་། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་མ་ཡིན་པ་དང་། འཇིག་རྟེན་ཡང་རང་བཞིན་གྱི་བདག་ཉིད་དང་། རང་བཞིན་ཡང་འགྱུར་བ་མེད་པའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ༌[^340]པར་ཞེན་ལ་འགྱུར་བའི་ཚོགས་ནི་ལྡོག་པར་འདོད་དོ། །

[Block 564]
གཞན་དག་ནི་གཞན་དུ་འདོད། ཀྱེ་མ་དེ་དག་ནི་གདོན་མི་ཟ་བར་རྟག་པ་དང་མི་རྟག་པ་ལ་སོགས་པའི་ལྟ་བ་རྣམས་ཀྱིས་འཕྲོགས་པར་འགྱུར་རོ། །

[Block 565]
རང་གི་སྡེ་པ་གང་དག་ཕུང་པོ་ལྔ་དང་བདག་བརྟེན་པར་ཁས་ལེན་ཀྱང་རྫས་སུ་ཡོད་པ་ཉིད་དུ་ཞུགས་པ་དང་གང་དག་མ་རིག་པ་དང་འདུ་བྱེད་ལ་སོགས་པ་རྒྱུ་དང་རྐྱེན་ཚོགས་པ་ལས་བྱུང་བ་ཡིན་ཡང་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་རྫས་སུ་ཡོད་པ་ཉིད་དུ་བརྗོད་པ་དེ་དག་ཀྱང་དེ་བཞིན་དུ་ལྟ་བ་ལོག་པར་ཞུགས་པ་ཡིན་པར་བསྟན་པའི་ཕྱིར།
--- END BLOCKS ---
