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
[Block 596]
རབ་ཏུ་བྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་འདི་རྣམས་ལ་ཡང་བསྡུ་བར་མི་བྱ་ཞེས་བྱ་བ་ཉེ་བར་སྟོན་པར་བྱེད་ཅིང་རིགས་དང་ལུས་ལ་སྐྱོན་ཆགས་པ་རབ་ཏུ་བྱུང་བ་ནི་ཉེ་བར་གཞག་པར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རིགས་ལ་སྐྱོན་ཆགས་པ་ཤིང་རྟ་མཁན་པོ་ལ་སོགས་པ་ཟན་བཟའ་བར་མི་བྱ་བ་རྣམས་སོ། །

[Block 597]
ལུས་ལ་སྐྱོན་ཆགས་པ་ནི་དབྱིབས་དང་ཁ་དོག་ལས་ཏེ་ལག་རྡུམ་ལ་སོགས་པའོ། །

[Block 598]
ཉེ་བར་གཞག་པར་མི་བྱ་བ་ནི་གནས་སྦྱིན་པ་གཅིག་པུར་མ་ཟད་ཀྱི༌[^420]གནས་ཁང་གི་ཡང་ནང་དུ་མི་སྦྱིན་པ་དང་རྗེས་སུ་འབྲང་བའི་འཁོར་ཉིད་ཀྱིས་སོ། །

[Block 599]
དེ་ལྟར་ཡང་དགེ་སློང་གིས༌[^421]འཁོར་སུན་འབྱིན་པའི་འཁོར་ཉེ་བར་གཞག་པར་མི་བྱ་སྟེ། ཉེ་བར་འཇོག་པར་འགྱུར༌[^422]ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་ན། ཇི་ཙམ་གྱིས་ན་འཁོར་སུན་འབྱིན་པའི་འཁོར་ཡིན་པར་བརྗོད་པར་བྱ་ཞེ་ན། རིགས་ལས་དང་ཁ་དོག་ལས་དང་དབྱིབས་ལས་ཏེ། ཇི་ལྟར་རིགས་ལས་ཤེ༌[^423]ན་ཤིང་རྟ་མཁན་དང་གདོལ་པ་དང་གཡུང་པོའི་རིགས་ལས་སོ། །

[Block 600]
ཇི་ལྟར་རིགས་དང་དབྱིབས་ལས་ཤེ༌[^424]ན་སྐྲ་སེར་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིར་སྨོས་སོ། །

[Block 601]
དུ་མ་མཁན་པོ་གཅིག་པས་གསུམ་མན་ཆད་ཚིག་གཅིག་གིས་བསྙེན་པར་རྫོགས་པར་བྱར་རུང་ངོ་ཞེས་བྱ་བ་ལ། དུ་མ་ཞེས་བྱ་བ་ནི་གཉིས་ལ་སོགས་པའོ། །

[Block 602]
མཁན་པོ་གཅིག་པ་འདི་ལ་ཡོད་པས་ན་མཁན་པོ་གཅིག་པ་སྟེ་དེ་ལའོ། །

[Block 603]
ཚིག་གཅིག་གིས་ཞེས་བྱ་བ་ནི་གསོལ་བ་གཅིག་གིས་སོ། །

[Block 604]
དུ་མ་ཇི་ཙམ་གྱིས་ཤེས་ཤེ་ན། འདིར་གསུམ་མན་ཆད་ཅེས་སྨོས་ཏེ་གསུམ་མན་ཆད་རིགས་པ་ཡིན་གྱི༌[^425]གཞན་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 605]
ལུང་ལས་ཀྱང་། ཚོགས་ཀྱིས་ཚོགས་ཀྱི་ལས་རྣམས་མི་བྱའོ་ཞེས་གསུངས་པ༌[^426]ལ། ཁ་ཅིག་ནི་མཁན་པོའི་བྱེ་བྲག་ཁས་བླངས་པའི་གཞུང་འདི་ལ་བྱེད་པ་ཡིན་ནོ། །

[Block 606]
ཉེ་བ་འཁོར་གྱིས་ཞུས་པ་ལས་ཀྱང་། བཙུན་པ་དུས་གཅིག་དང་སྐད་ཅིག་ཉིད་ལ་ལས་བྱེད་པ་པོ་གཅིག་ཅིག༌[^427]གིས་གསོལ་བ་གཅིག་གིས་ལས་གཉིས་བགྱི་བ་དང་བགྱིས་པར་བརྗོད་པ་དང་། དགེ་འདུན་ཡང་དེས་འགལ་ཚབས་ཅན་དུ་མི་འགྱུར་བ་མཆིས་སམ། ཉེ་བ་འཁོར་ཡོད་དེ། དེ་ལས༌[^428]བྱེད་པ་པོའི་དགེ་སློང་སྟོབས་དང་ལྡན་པར་གྱུར་ན་མཁན་པོ་རྣམས་དང་། བསྙེན་པར་རྫོགས་པར་འདོད་པ་རྣམས་ཀྱི་མིང་ཡོངས་སུ་བརྗོད་ནུས་ཤིང་གསོལ་བ་ཉམས་པར་མི་འགྱུར་བ་ལས༌[^429]ཀྱང་བྱེད་ནའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 607]
འཕགས་པ་ཉེ་བ་འཁོར་དགེ་ཚུལ་སྦྱིན་བྱེད་དང་སྐྱོང་བྱེད་མཉེས་གཤིན་པ་དང་བཅས་པ་དེ་གཉིས་ཕན་ཚུན་སེམས་རྗེས་སུ་བསྲུངས་པས་ཅིག་ཅར་བསྙེན་པར་རྫོགས་པར་བྱ་བ་ཡིན་ཏེ། དེ་བས་ན་སོ་སོར་བསྙེན་པར་རྫོགས་པར་མི་བྱའོ། །

[Block 608]
རྒྱུ་འདིས་མཁན་པོ་གཅིག་གིས་དུ་མ་བསྙེན་པར་རྫོགས་པར་གནང་བ་ལ་རྒྱུ་འདི་ལས་མཁན་པོ་གཅིག་ལ་དུ་མ་ཁས་ལེན་པ་འདི་ནི་གླེང་གཞི་ལས་མཐོང་བ་ཡིན་ཏེ། དེ་བས་ན་དེ་ལྟར་ཁས་མ༌[^430]བླངས་པ་ལ་འདི་ཡང་དགོས་པ་མ་ཡིན་ནོ། །

[Block 609]
དུས་མཉམ་པ་རྣམས་ནི་གཅིག་ལ་གཅིག་ཕྱག༌[^431]མི་བྱའོ་ཞེས་བྱ་བ་ནི་དུས་གཅིག་ཏུ་ལས་གཅིག་བརྗོད་པས་བསྙེན་པར་རྫོགས་པའམ། སོ་སོར་བསྙེན་པར་རྫོགས་པ་གང་དག་གིས་དུས་མཉམ་པ་དེ་རྣམས་ལ་ཕན་ཚུན་དུ་ཕྱག་བྱེད་པ་མེད་པ་སྟེ། ཕྱག་ཅེས་བྱ་བ་ནི་ཕྱག་གོ། །

[Block 610]
སྔར་འོངས་པ་དང་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དུས་མཉམ་པ་རྣམས་ཀྱང་རྙེད་པ་དང་ལས་སུ་བསྐོ་བ་དང་ལྡན་པ་ལ་སོགས་པའི་གནས་གང་ཞིག་ལ་དང་པོ་འོངས་པ་དེ་ལ་རྙེད་པ་བླངས་པ༌[^432]ལ་དང་པོ་ཉིད་དེ། ཇི་ལྟར་འོངས་པས་རྙེད་པ་བླང་བར་བྱའོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 611]
ལས་སུ་བསྐོ་བ་ལ་གང་ཞིག་ཕྱིས་འོངས་པ་དེས་དང་པོར་བྱ་བ་ཉིད་དེ། ཕྱིས་འོངས་པས་ལས་སུ་བསྐོ་བ་དང་པོ་ཞེས་བྱ་བ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 612]
དོན་ནི་འདི་ཡིན་ཏེ། རྙེད་པ་བླང་བ་ལ་དང་པོར༌[^433]གནས་ཡང་དག་པར་ཐོབ་པ་ལ་དང་པོ་ཉིད་དེ་ལས་སུ་བསྐོ་བར་བྱེད་པ་ལ། ཕྱིས་གནས་ཡང་དག་པར་ཐོབ་པ་ལ་དང་པོ་ཉིད་ཅེས་བྱ་བའོ། །

[Block 613]
དགོན་པ་བས་སྐྲ་སོར་གཉིས་ལས་ལྷག་པར་མི་གཞག་གོ། །

[Block 614]
གྲོང་མཐའ་བས་ནི་དེའི་འོག་མ་ཉིད་ལས་མི་གཞག་གོ་ཞེས་བྱ་བ་ལ༌[^434]འོག་མའི་དངོས་པོ་ནི༌[^435]འོག་མ་ཉིད་དེ། སོར་གཉིས་པོ་འདིའི་འོག་གི་དངོས་པོ་ལས་ལྷག་པར་སོར་ཕྱེད་དང་གཉིས་ཀྱི་ཚད་ཉིད་ཡང་དག་པར་ཐོབ་པ་སྟེ། ཇི་སྲིད་དུ་གཞག་པར་མི་བྱ་ཞེས་བྱ་བ་འདིར་ཤེས་པར་འགྱུར་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 615]
འདིར་གཞུང་ནི། དགེ་སློང་དགོན་པ་བས་སྐྲ་སོར་གཉིས་སུ་གཞག་པར་བྱ་ལ། གྲང་མཐའ་བས་ནི་དེའི་འོག་མའོ་ཞེས་གསུངས་སོ། །

[Block 616]
ཁ་ཅིག་ནི་སོར་གཉིས་བསྐོར་བ་ཞེས་བྱ་བ་སོར་གཉིས་ཀྱི་གནས་ལ་སྨྲ་བ་ཡིན་ཏེ། གལ་ཏེ་འདོན་པ་འདི་ལ་སོར་གཉིས་པའི་ཚད་ཀྱིས་བསྐོར་བ༌[^436]གང་རྣམས་ཞེས་བྱ་བའི་དོན་ཏེ། སྔོན་གྱི་འདོན་པ་ལས་དོན་གཞན་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 617]
འོན་ཏེ་སོར་གཉིས་པ་བསྐོར་བ༌[^437]ཡིན་ན༌[^438]ནི་རིགས་པ་མ་ཡིན་ཏེ། འདི་ཙམ་རིང་པོ་ཉིད་ལ་རྟགས་མི་གནང་བར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་དང་། གླེང་གཞིའི༌[^439]སྐྱོན་གང་གིས་ཀྱང་བསླབ་པའི་གཞི་འདི་བརྟགས་པ་དེའི་སྐྱོན་ལས་བྱུང་བ་ལ་ཡང་གནས་སྐབས་དེ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 618]
གང་གི་ཕྱིར་སོར་ལྔ་ལས་ལྷག་པའི་ཚད་ནི་འདི་ཡིན་ཏེ། རབ་ཏུ་བྱུང་བའི་དུས་ན་འབྱུང་བའི་སྐྲ་བྲེག་པའི་ཆོ་ག་ལས་གཞན་དུ་ཡང་སྐྲ་བྲེག་པ་ལ་སོགས་པ་ལ་བྱ་བ་ཉིད་དུ་རིགས་པ་ཡིན་ཏེ། དེ་བས་ན་གནས་འདི་ལ་རྣམ་པར་ཞུགས་པའོ། །

[Block 619]
སྐྲ་བ་ལང་གི༌[^440]འདྲ་བར་མི་བྲེག་གོ། །

[Block 620]
རྨའི་ཐན་ཀོར་ནི་མ་གཏོགས་སོ། །

[Block 621]
གཙུག་ཕུད་བྱེད་དུ་མི་གཞུག་གོ། །

[Block 622]
མདོམས༌[^441]ཀྱི་སྤུ་བྲེག་ཏུ་མི་གཞུག་གོ་ཞེས་བྱ་བ་ནི་བྱེད་དུ་མི་གཞུག་གོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 623]
མདོམས་གྱི༌[^442]ཕྱོགས་ནི་གསང་བའི་གནས་སོ། །

[Block 624]
རྨའི་ཆེད་དུ་གཞན་གྱིས་མི་འཚོ་ན་མཁས་པ་གནས་བརྟན་གནས་བརྟན་དག་ལ་དྲིས་ཏེ་འབྲེག་ཏུ་གཞུག་གོ་ཞེས་བྱ་བ་ལ། མི་འཚོ་ན་ནི་གཞན་གྱིས༌[^443]ཞེས་བྱ་བ་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ་བསྐ་བ་ལྔས་བཀྲུ་བར་བྱའོ། །

[Block 625]
དེའི་འོག་ཏུ་གལ་ཏེ་འཚོ་བར་མ་གྱུར་ན་མདོ་སྡེ་འཛིན་པ་དང་འདུལ་བ་འཛིན་པ་དང་། མ་མོ་འཛིན་པའི་དགེ་སློང་རྣམས་ལ་དྲིས་ཏེ་མདོམས༌[^444]ཀྱི་སྤུ་བྲེག་ཏུ་གཞུག་གོ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ནི་འདིར་གཞུང་ཡིན་ནོ། །

[Block 626]
དེ་ལ་དཔེ་ཡིན་ཏེ། སྦྱང་བའི་ཆོ་ག་འདི་རིགས་པ་ཡིན་ཞེས་བྱ་བ་རྣམ་པ་གཞན་རྣམས་ཀྱང་གསོ་བར་བྱེད་པ་ལ་བསྡུས་པ་ཡིན་ཏེ། དགེ་སློང་གནས་བརྟན་གནས་བརྟན་དག་ལ་བལྟས་ནས་རྨའི་ཆེད་དམ་སྲོག་ཆགས་རྣམས་ཀྱི་ཆེད་དུ་གནོད་པ་མེད་པའི་ས་ཕྱོགས་སུ་སྤུའི་ལས་བྱེད་དུ་གཞུག་གོ་ཞེས་བྱ་བ་འདིར་གཞན་རྣམས་ཀྱི་གཞུང་ནི་དེ་ལ་མངོན་སུམ་དུ་རིག་པར་བྱས་པར་གྱུར་པ་ཞེས་བྱ་བ་འདིའི་ལྷག་མའོ། །

[Block 627]
རྒན་པ་གཉིས་དག་གིས་མངོན་སུམ་པ་ཉིད་ཀྱི་ཚུལ་ཁྲིམས་ཉིད་དང༌[^445]ཆོས་འདུལ་བ༌[^446]མངོན་པར་ཤེས་པ་ཉིད་ཀྱིས་སོ། །

[Block 628]
འདི་གཉིས་ཀ་ཡང་ལྟ་བ་སོན་པས་བསྡུས་པའོ། །

[Block 629]
བསྡུས་པ་ནི་རྣམ་པར་ཤེས་པའོ། །

[Block 630]
སྡེ་སྣོད་འཛིན་པ་ཉིད་ཀྱི་ཚིག་ནི་ཤེས་པ༌[^447]པོ་ལ་རག་ལུས་པར་ཤེས་སོ། །

[Block 631]
སྲོགས་ཆགས༌[^448]ཀྱི་ཆེད་ནི་འདིར་རྨ་ལ་གནས་པའི་སྲོག་ཆགས་རྣམས་ལ་དགོངས་པར་རིགས་པ༌[^449]ཡིན་ཏེ། ཤིག་ལ་སོགས་པའི་དགོངས་པ་ནི་མ་ཡིན་ནོ། །

[Block 632]
འདི་ལ་ཡང་རྨའི་ཆེད་ཉིད་ཀྱི་ནང་དུ་བསྡུས་པ༌[^450]ཉིད་དེའི་ཕྱིར་མ་བཟུང་ངོ་། །བྱིན་པའི་སྤུ་བྲེག་པ་ཡང་དེའི་ཕྱིར་མ་ཡིན་པར་བྱེད་དུ་མི་གཞུག་གོ་ཞེས་བྱ་བ་ལ། དེའི་ཕྱིར་མ་ཡིན་པ་ནི་རྨའི་ཕྱིར་མ་ཡིན་པའོ། །

[Block 633]
བྱིན་པའི་སྤུ་བྲེག་པ་ནི་ཡན་ལག་གི་སྤུའོ། །

[Block 634]
ལུས་གཞན་གྱི་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མདོམས༌[^451]དང་བྱིན་པ་དག་ལས་གཞན་པའི་ལུས་ནི་མགྲིན་པ་མན་ཆད་གང་ཞིག་ལུས་ཀྱི་ཐ་སྙད་དེ་ལ༌[^452]ཡང་སྤུ་བྲེག་པའི་ལས་འདི་བཀག་པའོ། །

[Block 635]
དེ་བས་ན་འདིར་སྐྲ་དང་ཁ་སྤུ་དག་ལ་ཡང་བྱ་བ་ཉིད་བཀག་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
