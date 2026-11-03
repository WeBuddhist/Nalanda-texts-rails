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
རྒྱ་ཆེན་པོ་དང་། ཆེན་པོར་གྱུར་པ་ཞེས་བྱ་བ་བར་མར་གྱུར་པའི་སེམས་ཀྱང་རབ་ཏུ་མཁྱེན་ཏེ། འདི་ལྟ་སྟེ་གཟུགས་ཀྱི་ཁམས་སུ་སྐྱེས་པའི་སེམས་ཅན་ཐམས་ཅད་ཀྱིའོ། །

[Block 597]
ཚད་མེད་པའི་སེམས་ཀྱང་རབ་ཏུ་མཁྱེན་ཏེ། གྱ་ནོམ་པའི་སེམས་མཁྱེན་པ་འདི་ལྟ་སྟེ་གཟུགས་མེད་པའི་ཁམས་སུ་སྐྱེས་པ་ཐམས་ཅད་ཀྱིའོ། །

[Block 598]
གསུམ་པོ་འདི་དག་ལྟར་འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་ཀྱི་བདེ་བ་དང་མཚུངས་པར་ལྡན་པའམ། སྡུག་བསྔལ་དང་མཚུངས་པར་ལྡན་པའམ། སྡུག་བསྔལ་ཡང་མ་ཡིན་བདེ་བ་ཡང་མ་ཡིན་པའི་ཚོར་བ་དང་། མཚུངས་པར་ལྡན་པའི་སེམས་ཀྱང་མཁྱེན་ཏོ། །

[Block 599]
ཕ་རོལ་གྱི་སེམས་མཁྱེན་པ་གཅིག་གིས་སེམས་ཅན་གཅིག་གང་གི༌[^438]སེམས་གང་ཡིན་པ་དང་། ཇི་ལྟ་བུ་དང་། ཇི་འདྲ་བ་དང་། ཇི་སྙེད་ཉེ་བར་གནས་པ་དེ་ཡང་ཅིག་ཅར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ༌[^439]རབ་ཏུ་མཁྱེན་ཏོ། །

[Block 600]
གང་དག་གི་ཡིན་པ་ན་ནི་སེམས་ཅན་གཞན་གྱིའོ། །

[Block 601]
གང་ཡིན་ན་ནི་སེམས་སོ། །

[Block 602]
ཇི་ལྟ་བུ་ཡིན་ན་ནི་ཉོན་མོངས་པ་དང་རྗེས་སུ་འབྲེལ་པ་བག་ལ་ཉལ་དང་བཅས་པ་ཉིད་དང་། ཉོན་མོངས་པ་དང་མ་འབྲེལ་ཞིང་བག་ལ་ཉལ་མེད་པ་ཉིད་དང་། ཉོན་མོངས་པས་ཀུན་ནས་དཀྲིས་པ་ཉིད་དང་། ཉོན་མོངས་པས་ཀུན་ནས་དཀྲིས་པ་དང༌[^440]བྲལ་བ་ཉིད་དོ། །

[Block 603]
ཇི་འདྲ་བ་ཞིག་ན་ནི། ཉོན་མོངས་པ་དང་བཅས་པ་དང་། ཉོན་མོངས་པ་མེད་པའོ། །

[Block 604]
ཇི་སྙེད་ཅེས་བྱ་བ་ནི། དམན་པའམ། གྱ་ནོམ་པ་སྟེ། དེ་ལྟ་བུའི་ཕ་རོལ་གྱི་སེམས་མཁྱེན་པ་གཅིག་ཁོ་ནས། སེམས་ཅན་མང་པོ་གང་དག་གི་སེམས་གང་ཡིན་པ་དང་། ཇི་ལྟ་བུ་དང་། ཇི་འདྲ་བ་དང་། ཇི་སྙེད་ཉེ་བར་གནས་པ་ཞེས་བྱ་བ་ནི། འདི་ཡང་འདི་ལྟར་དོན་གྱི་ཤུགས་ཀྱིས་རྟོགས་པར་བྱ་སྟེ། དེ་ཡང་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་མངོན་པར་ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 605]
ཟག་པ་ཟད་པ་མཁྱེན་པ་བདུན་པའི༌[^441]དོན་ནི། ཟག་པ་ཟད་པ་ལ༌[^442]མཁྱེན་པ་ནི་ཟག་པ་ཟད་པ་ལ་མཁྱེན་པའམ། ཟག་པ་ཟད་པའི་ཕྱིར་མཁྱེན་པ་ནི་ཟག་པ་ཟད་པ་མཁྱེན་པ་སྟེ། དེ་བཞིན་དུ་རྣམ་པ་བཞི་ཡིན་ལ། ཟག་པ་ཟད་པ་ལ་མཁྱེན་པའི་དབང་དུ་བྱས་པ་ནི། ཉོན་མོངས་པ་རྣམས་ཟད་པ་ཐོབ་པ་ཟག་པ་ཟད་པ་བདག་གིས་སམ། གཞན་དག་གིས་ཐོབ་པའམ་མ་ཐོབ་པ་ཡང་རུང་། ཟག་པ་ཟད་པའི་ཐབས་བདག་དང་གཞན་གྱི་ཡང༌[^443]དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་མཁྱེན་ཏོ། །

[Block 606]
ཐབས་ཇི་ལྟ་བ་ཡང་ཡང༌[^444]དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་མཁྱེན་ཏོ། །

[Block 607]
ཟག་པ་ཟད་པ་མཁྱེན་པ་འདིའི་དབང་དུ་བྱས་པ་ནི། གཞན་དག་གིས་ཟག་པ་ཟད་པ་ཐོབ་པའི་མངོན་པའི་ང་རྒྱལ་ཡང་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་མཁྱེན་ཅེས་བྱ་བའོ། །གང་གི༌[^445]དོན་དུ་མཁྱེན་ཅེ་ན། དེ་ལ་སོགས་པའི་དབང་དུ་བྱས་པ་ནི། ཟག་པ་ཟད་པ་མཁྱེན་པ་དེས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 608]
སྦྱིན་པ་ལ་སོགས་པའི་ཆོས་འདི་རྣམས་ཀྱི་མཐུའི་དོན་གྱི༌[^446]བསྡུས་པའི་དོན་ནི་རྣམ་པ་བཞི་སྟེ། འབྲས་བུ་ལས་བསྟན་པར་འགྱུར་རོ། །ཇི་ལྟར་གང་ཞེ་ན། མི་མཐུན་པའི་ཕྱོགས་སྤངས་པ༌[^447]བྲལ་བའི་འབྲས་བུ་དང་། ཚོགས་ཡོངས་སུ་སྨིན་པའི་སྐྱེས་བུའི་བྱེད་པའི་འབྲས་བུ་དང་། བདག་དང་གཞན་རྗེས་སུ་འཛིན་པའི་བདག་པོའི་འབྲས་བུ་དང་། འདི་ལྟར་མ་འོངས་པ་ནི༌[^448]འབྲས་བུ་སྦྱིན་པའི་འབྲས་བུ་རྣམ་པ་གཉིས་པོ་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་དང་། རྒྱུ་མཐུན་པའི་འབྲས་བུའོ། །

[Block 609]
སྦྱིན་པའི་མི་མཐུན་པའི་ཕྱོགས་སེར་སྣ་ཡང་སྤོང༌[^449]ངོ་ཞེས་བྱ་བ་ནི་བྲལ་བའི་འབྲས་བུའོ། །

[Block 610]
བདག་ཉིད་ཀྱི་བྱང་ཆུབ་ཀྱི་ཚོགས་སུ་གྱུར་པ་ཡང་ཡིན་ལ་ཞེས་བྱ་བ་ནི།

[Block 611 [VERSE]]
སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་སྟེ། །
གང་གི་སྟོབས་ལས་གང་སྐྱེས་པ།
དེ་ཡི་སྐྱེས་བུ་བྱེད་ལས་བྱུང་། །

[Block 612]
ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 613]
བསྡུ་བའི་དངོས་པོ་སྦྱིན་པས་ཀྱང་སེམས་ཅན་རྣམས་ཡོངས་སུ་སྨིན་པར་བྱེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དབང་གི་འབྲས་བུའོ། །

[Block 614]
ཕ་རོལ་དུ་ཡང་གང་དང་གང་དུ་སྐྱེས་པར་ཕྱུག་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་རྣམ་པར་སྨིན་པའི་འབྲས་བུའོ། །

[Block 615]
སྦྱིན་པ་ལ་ཡང་མོས་པར་འགྱུར་ཏེ་ཞེས་བྱ་བ་ནི། རྒྱུ་མཐུན་པའི་འབྲས་བུའོ། །

[Block 616]
དེ་བཞིན་དུ་ཚུལ་ཁྲིམས་ལ་སོགས་པའི་ཆོས་གཞན་དག་ལ་ཡང་ཇི་ལྟར་རིགས་པར་བརྗོད་པར་བྱའོ། །

[Block 617]
ཚིག་དང་རྟོག་པ་ནི་ཚིག་གི་རྟོག་པ་སྟེ། དེ་ཉིད་ཉོན་མོངས་པའོ། །

[Block 618]
ཡང་ན་ཚིག་ཀུན་ནས་སློང་བར་བྱེད་པའི་རྟོག་པ་ནི་ཚིག་གི་རྟོག་པ་སྟེ། ཚིག་གི་རྟོག་པ་ཅན་གྱི་མཚན་ཉིད་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པ་འདོད་པའི༌[^450]ཁམས་ལ་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་རབ་ཏུ་རྟོག་པའི་རྟོག་པའོ། །

[Block 619]
བསམ་གཏན་གཉིས་པ་ན་ནི་དགའ་བའོ། །

[Block 620]
བསམ་གཏན་གསུམ་པ་ན་ནི་བདེ་བ་དང་། [^451]

[Block 621]
བཞི་པ་ན་ནི་གཟུགས་ཀྱི་འདུ་ཤེས་ལ་སོགས་པ་སྟེ། གཟུགས་ཀྱི་འདུ་ཤེས་དང་། ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ཀྱི་ནམ་མཁའི་འདུ་ཤེས་དང་། རྣམ་ཤེས་མཐའ་ཡས་སྐྱེ་མཆེད་ཀྱི་རྣམ་པར་ཤེས་པ་མཐའ་ཡས་སོ་སྙམ་པའི་འདུ་ཤེས་དང་། ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ཀྱི་ཅི་ཡང་མེད་དོ་ཞེས་བྱ་བའི་འདུ་ཤེས་སོ། །

[Block 622]
འདུ་ཤེས་མེད་འདུ་ཤེས་མེད་མིན་གྱི་སྐྱེ་མཆེད་རྣམ་པར་དག་པའི་ལྷར་སྐྱེས་པའི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་ནི་ཡེ་ཤེས་རྣམ་པར་དག་པའོ། །

[Block 623]
མངོན་པར་ཤེས་པ་མངོན་པར་སྒྲུབ་པ་ནི་རྒྱུ་མཐུན་པའི་འབྲས་བུའོ། །

[Block 624]
དགེ་བའི་རྩ་བ་ཐམས་ཅད་ཡོངས་སུ་འཛིན་པ་ཉིད་དུ་ཡང་དག་པར་བྱེད་པས་རྒྱུ་མཐུན་པའི་འབྲས་བུ་སྟེ། རྒྱུ་མཐུན་རྒྱུ་དང་འདྲ་བའོ་ཞེས་བྱ་བས་སོ། །

[Block 625]
མ་འོངས་པ་ན་སྒྲིབ་པ་རྣམ་པ་གཉི་ག་ཡང་མངོན་དུ་འབྲེལ་བར༌[^452]བྱེད་པས། རྣམ་པ་ཐམས་ཅད་དུ་རྟེན་ཡོངས་སུ་གྱུར་པ་ཉིད་འདི་ཙམ་ནི་རྣམ་པར་སྨིན་པའི་འབྲས་བུའོ། །

[Block 626]
རང་བཞིན་གྱིས༌[^453]ཚེ་རབས་དགོངས་པ་ཞེས་བྱ་བ་ནི། གཞན་དག་གི༌[^454]ཁྱད་པར་ཅན་གྱི་དོན་གྱི་ཚེ་རབས་དགོངས་པའོ། །

[Block 627]
རང་བཞིན་སྨོས་པ་ནི་གཞན་ལ་ཕན་པའི་སྨོན་ལམ༌[^455]བཏབ་པར་དེ་འབྱུང་བར་བྱེད་པའི་ལས་བྱས་པས་བྱུང་བ་སྟེ། འདི་ནི་ཡང་སྨོན་ལམ་ལ་སོགས་པ་མེད་པར་འབྱུང་བའོ། །

[Block 628]
ཡུན་རིང་པོ་ལ་སོགས་པར་སྡུག་བསྔལ་ལ་མི་མཇེད་པ་ནི་ཇི་སྲིད་དུ་བདག་དང་གཞན་གྱི་དོན་མ་བསྒྲུབ་པར་ཏེ། གང་གི་ཚེ་གཞན་གྱི་དོན་ཡང་དག་པར་བསྒྲུབ་པར༌[^456]གྱུར་པ་དེས༌[^457]དགའ་བའམ། ཡང་ན་སེམས་ཅན་གྱི་དོན་དུ་སེམས་ཅན་ལ་དམིགས་ནས། ཡུན་རིང་པོ་ལ་སོགས་པར་འཁོར་བའི་སྡུག་བསྔལ་ལས་མི་མཇེད་པའོ། །

[Block 629]
ད་ནི་འདི་ལྟར་ཡང་སེམས་ཅན་གྱི་དོན་བསྒྲུབ་པའི་ཞེས་བྱའོ།[^458] །སེམས་ཅན་གྱི་དོན་ལ་དམིགས་ནས་བརྩམས་པའི་སྡུག་བསྔལ་གང་ཡིན་པ་དེས་དགའ་བའོ། །

[Block 630]
བལྟམ་ཁ་དང་བལྟམས་པ་ལས༌[^459]ཞེས་བྱ་བ་ལ་བལྟམ་ཁ་དང་བལྟམས་པ་ལས་གཞན་མཁྱེན་བཞིན་གང་ཡིན་ཞེ་ན། ཡང་དག་པར་མཁྱེན་བཞིན་དུ་ཡུམ་གྱི་ལྷུམས་སུ་གཤེགས་པ་དང་། བལྟམ་པ་དང་དེ་ནི་རྗེས་ཀྱི་བྱིས་པའི་གནས་སྐབས་ན་ཡང་ངོ་། །དམ་པ་རབ་མཆོག་ཅེས་སྨོས་པ་ནི། འཁོར་ལོས་སྒྱུར་བའི༌[^460]མཚན་གྱི་ཁྱད་པར་དང་ལྡན་པའི་རྒྱན་ནོ། །

[Block 631]
བྱས་པ་སྦྱངས་པ༌[^461]མ་མཛད་པའི་ངང་ཚུལ་འདི་ལ་ཡོད་པས་བྱས་པ་སྦྱངས་པ་མ་མཛད་པ་སྟེ། སྦྱངས་པ་མ་མཛད་པར་བདག་ཉིད་ཀྱིས་བྱ་བ་རྣམས་ལ་མཁས་པའོ། །

[Block 632]
བྱང་ཆུབ་སེམས་དཔའི་སའི་གཞིའི་རྣལ་འབྱོར་གྱི་གནས་ལས།

[Block 633]
མཐུའི་ལེའུ་རིམ་པར་ཕྱེ་བ་སྟེ་ལྔ་པའོ།། །།

[Block 634]
ཡོངས་སུ་སྨིན་པར་ནི་མདོར་བསྡུ་ན་རྣམ་པ་བཅུ༌[^462]དྲུག་ཅེས་བྱ་བའི་དོན་ནི། ཡོངས་སུ་སྨིན་པ་ནི་ཅི། གང་གིས།[^463] གང་དུ། ཅི་ཞིག་ཡོངས་སུ་སྨིན་པར་འགྱུར། གང་གི༌[^464]གང་ཞིག་གིས་ཡོངས་སུ་སྨིན་པར་བྱེད། ཡོངས་སུ་སྨིན་པའི་མཚན་ཉིད་ནི༌[^465]ཇི་ལྟ་བུར་འབྱུང་ཞེས་བྱ་བའོ། །

[Block 635]
དེ་ལ་ཡོངས་སུ་ངེས་པར་ཅི་ཞིག་ཡོངས་སུ༌[^466]སྨིན་པའི་ངོ་བོ་ཉིད་ནི་ཡོངས་སུ་སྨིན་པའམ། ཡོངས་སུ་སྨིན་པ་གང་ལ་བརྟེན་ནས་འཇུག་སྙམ༌[^467]ནས། དེ་ལ་འདི་ཡོངས་སུ་སྨིན་པར་བྱ་བས་ནི།[^468] ཡོངས་སུ་སྨིན་པའམ། འདི་དག་ལ་ཡོངས་སུ་སྨིན་པར་བྱ་བས་ཏེ། ཉན་ཐོས་ཀྱི་ཐེག་པ་པ་ལ་སོགས་པའོ། །
--- END BLOCKS ---
