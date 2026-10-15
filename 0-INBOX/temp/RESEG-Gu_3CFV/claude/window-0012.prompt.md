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
[Block 421]
དེའི་ཕྱིར་མ་ཡིན་པར་དགེ་འདུན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལ་བརྟེན་ནས་དགེ་འདུན་སྤྱན་དྲངས་པ་དེའི་མེད་པ་ཉིད་ན་དེའི་ཕྱིར་རྣམ་པར་གཅད་པར༌[^262]བྱ་བ་ལ་མངོན་པར་བརྟེན་པ་ཉིད་ཀྱི་ཕྱིར་གཞན་ལ་ནི་མེད་པ་ཉིད་དོ། །

[Block 422]
འདིར་ཁུངས་ནི་གང་གི་ཕྱིར་འཕགས་པ་ལེགས་འོངས་ཀྱི་ཕྱིར་ཏེ། གང་དེ་ལ་བརྟེན་ན་ཆུ་སྲིན་བྱིས་པ་གསོད་ཀྱི་རི་པ་རྣམས་ཀྱིས༌[^263]དགེ་འདུན་སྤྱན་འདྲེན་པ་ལ་བྲམ་ཟེ་སྤྱན་དྲངས་པར་གྱུར་པས་བྲམ་ཟེ་རྣམས་འོངས་ནས་བྱིས་པ་གསོད་པའི་རི་པའི་བྲམ་ཟེ་དང་ཁྱིམ་བདག་རྣམས་ཀྱིས༌[^264]སངས་རྒྱས་ལ་སོགས་པ་དགེ་སློང་གི་དགེ་འདུན་ཞག་བདུན་བཤོས་ལ་སྤྱན་དྲངས་པས་དེའི་ཚེ་ངས་དང་དུ་མ་བླངས་སོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེའི་ཕྱིར་མདོ་འདི་བྱས་སོ། །

[Block 423]
དགག་དབྱེ་སོ་སོར་རྗེས་སུ་གནང་བ་དང་སྦྱར་བར་བྱའོ། །

[Block 424]
གཞན་དུ་ལྔ་པོ་འཇོག་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མགྲོན་དུ་བོས་པ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 425]
སིལ་བུ་དག་ལས་དང་པོ་ལྔ་པོ་ཞེས་བྱ་བ་འདི་བརྗོད་པ་ཡིན་ཏེ། དེ་བས་ན་གཞུང་ནི་ཡི་གེ་གཞན་ལས་དགེ་སློང་བཅའ་བ་དང་བཟའ་བའི་ཟན་གཉིས་དང་མགྲོན་དུ་བོས་པས་གཅིག་དགེ་སློང་ལ་རྣམ་པར་རྟོག་པར་བྱེད་ན་ལྟུང་བ་མེད་དོ། །

[Block 426]
དགེ་སློང་མ་ལ་རྣམ་པར་རྟོག་པར༌[^265]བྱེད་ན་ལྟུང་བ་མེད་དོ། །

[Block 427]
དེ་བཞིན་དུ་དགེ་སློབ་མ་དང་དགེ་ཚུལ་མ་ལ་རྣམ་པར༌[^266]རྟོག་པར་བྱེད་ན་ཡང་ལྟུང་བ་མེད་དོ། །

[Block 428]
དེ་བཞིན་དུ་སྡེ་པ་ལྔ་པོ་ཐམས་ཅད་ལ་རྣམ་པར་རྟོག་པར་བྱེད་ན་ཡང་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 429]
སིལ་བུ་དག་ལས་ཀྱང་དགེ་སློང་དང་དགེ་སློང་མ་དང་དགེ་སློབ་མ་དང་དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་རྣམས་ལས་འདིར་ལྔ་ཉིད་ཀྱི་ཚིག་གིས་གསུངས་སོ། །

[Block 430]
འཕགས་པ་འདི་བྱེད་པར་མི་རིགས་སོ་ཞེ་ན་འདིར་བརྗོད་པར་བྱ་སྟེ། དེ་ནི་ཆོས་དང་ལྡན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཅི་གཞན་ལ་བོས་པས་གཟུང་བར་འདོད་པ་ཉིད་མེད་པ་ལ་འདི་རིགས་པ་ཉིད་ཡིན་ནམ་འོན་ཏེ་ཡོད་པ་ལ་ཡང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གཞན་བླང་བ༌[^267]ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མགྲོན་དུ་བོས་པ་གཞན་བླང་བ་ཡོད་པ་ལ་འཇོག་པ་ལ་ཆོས་དང་ལྡན་པ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 431]
མུ་གེ་བྱུང་ན་མགྲོན་དུ་བོས་པ་ཇི་སྙེད་བྱུང་བ་དག་བདག་གིར་བྱའོ་ཞེས་བྱ་བ་ནི་སྔ་མ་སྔ༌[^268]མ་བཞག་ཀྱང་ཇི་སྙེད་བྱུང་བ་དེ་སྙེད་རྣམས་ལའོ། །

[Block 432]
ཟོས་ནས་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མགྲོན་དུ་བོས་པ་ཇི་སྙེད་བྱུང་བའི་སྤྱན་དྲངས་པ་རྣམས་ལའོ། །

[Block 433]
སྦྱིན་དུ་ཡང་རུང་ངོ་ཞེས་བྱ་བ་ནི་ལྔ་པོ་ལྔ་པོ་ཞེས་སྔར་བསྟན་པའི་རྗེས་སུ་འབྲེངས་ཏེ་ཤེས་པར་བྱའོ། །

[Block 434]
སྦྱིན་པ་པོ་མངོན་པར་མི་དགའ་བར་འགྱུར་བ་ལྟ་ན་ཁམ་གཉིས་སམ་གསུམ་ཟོས་པའི་འོག་ཏུ་ཁྱིམ་བདག་དགེ་སློང་འདི་བསོད་སྙོམས་ཀྱིས༌[^269]ཕོངས་པ་ཡིན་གྱི༌[^270]རྗེས་སུ་ཡི་རང་བར་གྱིས་ཤིག་དང་འདི་ལ་སྦྱིན་པར་བྱའོ་ཞེས་མངོན་པར་དགའ་བར་བྱས་ནས་སོ་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་པོ་དེ་ལྔ་པོ་དག་ལ་སྦྱིན་པའོ། །

[Block 435]
ཡང་ཡང་ཟ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 436]
འདུག་གནས་སུ་ཟ་བའི་ལྟུང་བྱེད་ལ་བྱེད་པ་པོ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཆོས་འདི་པའི་མ་ཡིན་པ་བདག་པོ་ཁྱིམ་པ་དང་བཅས་པ་ཡ་མཚན་ཅན་ཐམས་ཅད་མ་ཡིན་པའི་འདུག་གནས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆོས་འདི་ལ༌[^271]ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་ཆོས་འདུལ་བར་བྱ་བ་གང་ཡིན་པ་དེ་ནི་ཆོས་འདི་པའོ། །

[Block 437]
དེ་ལས་གཞན་པ་ནི་ཆོས་འདི་པ་མ་ཡིན་པའོ། །

[Block 438]
བདག་པོ་ཁྱིམ་པ་དང་བཅས་པ་ཞེས་བྱ་བ་ནི། བདག་པོ་ཁྱིམ་པ་དང་ལྷན་ཅིག་འཇུག་པ་གང་ཡིན་པ་དེ་ནི་བདག་པོ་ཁྱིམ་པ་དང་བཅས་པའི་འདུག་གནས་སོ། །

[Block 439]
རང་བཞིན་ཅན་ཡང་བདག་ཏུ་བྱས་ནས་སྦྱིན་པའམ་བྱེད་དུ་འཇུག་པ་ལ་འདིར་ཉེས་པ་རྣམ་པར་གཞག་པའོ། །

[Block 440]
དེ་བས་ན་ཁྱིམ་པས་བྱེད་དུ་འཇུག་པ་ཞེས་བྱ་བའི་ཚིག་གོ། །

[Block 441]
ཡ་མཚན་ཅན་ཐམས་ཅད་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི༌[^272]ཡ་མཚན་ཅན་ཐམས་ཅད་ལ་འདིར་ཆོས་འདི་པ་ཉིད་ཀྱང༌[^273]ཡོད་པས་ཉེས་པ་བྱེད་པ་པོ་ཉིད་མ་ཡིན་ནོ། །

[Block 442]
འདུག་གནས་སོ་ཞེས་བྱ་བ་ནི་འདི་ལས་འདིར་བྱེད་པ་པོ་རྣམས་ཞེས་བྱ་བ་འདི་ལས་ཡོངས་སུ་གྱུར་པ་ལ་སོ་སོར་ཉེ་བར་གནས་པའོ། །

[Block 443]
ལྟུང་བ་འབྱིན་པར་བྱེད་པ་ཇི་ལྟ་བུ་ལ་དེ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མི་ན་བ་ལའོ་ཞེས་སྦྱིན་བདག་གིས་མ་བསྟབས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ནི་ཡིད་ཀྱི་བྱ་བ་སྟེ་དེ་ལ་ཡོངས་སུ་ལོངས་སྤྱོད་པ་མ་ཡིན་པ་རྣམས་ལ་མ་བསྟབས་པ་གང་ཡིན་པ་འདི་དེར་ཡ་མཚན་ཅན་ཐམས་ཅད་དང་འདྲ་བར་འདིར་ཉེས་པ་མི་སྐྱེད༌[^274]པའོ། །

[Block 444]
ཕྱིར་མི་འབྱུང་བ་ལ་ཆོ་ག་འདི་དང་ལྡན་པ་སྟེ། ཕྱིར༌[^275]འབྱུང་བ་ལ་ནི་སྦྱིན་བདག་ཕྱུག་པོ་མེད་པས་བསྟབས་པ༌[^276]ཉིད་ལ་ཡང་དངོས་གཞི་ཁོ་ན་སྟེ་གཞན་ལ་བརྟེན་པ་ནི་འདིར་སྐྱོན་ཡིན་ཏེ། དེ་ཡོངས་སུ་གསལ་བའི་དོན་དུ་བསླབ་པའི་གཞི་འདི་ཡིན་ནོ། །

[Block 445]
འདིར་གང་དུ་གང༌[^277]ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཟོས་ན་ཟོས་པ་ལ་དངོས་གཞིའོ། །

[Block 446]
གནས་ན་ཞག་ལོན་པ་ལ་ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་བསོད་སྙོམས་གཅིག་ཟ་ཞིང་གཉིས་པ་ཟ་བ་ལ་དངོས་གཞིའི་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 447]
ཞག་གཅིག་ལོན་པའི་ཉི་མ་གཉིས་པ་ལ་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 448]
ཉི་མ་དང་པོ་ལ་ནི་གནས་པ་དང་ཟོས་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 449]
འདིར་གཞུང་ནི་དེར་གནས༌[^278]པ་ན་ཉེས་བྱས་སུ་འགྱུར་ལ། དེར་ཟ་བ་ལ་ལྟུང་བྱེད་དུ་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ཏེ། ཉི་མ་གཉིས་པ་ལ་གནས་པ་དང་ཟ་བའི་དབང་དུ་མཛད་ནས་ཚིག་འདི་གསུངས་སོ། །

[Block 450]
འདུག་གནས་གཅིག་ཏུ་ཞག་ལོན་པའི་དགེ་སློང་མི་ན་བས་བསོད་སྙོམས་གཅིག་བཟའ་བར་བྱའོ། །

[Block 451]
དེའི་ཕྱིར་དང་པོ་འདི་དག་ལ་རྗེས་སུ་གནང་བ་ཉིད་ཡིན་པས་དེ་བས་ན་འདིར་ཉེ་བར་བཏགས་པའོ། །

[Block 452]
བདག་པོ་མེད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཆོས་འདི་པའི་མ་ཡིན་པ་ཡ་མཚན་ཅན་ཐམས་ཅད་མ་ཡིན་པའི་འདུག་གནས་དེ་བདག་པོ་མེད་པ་ཡིན་ན་ཡང་ཉེས་བྱས་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 453]
འདི་ལ་རབ་ཏུ་བྱུང་བ་འདི་པ་ནི་མུ་སྟེགས་ཅན་དང་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདིར་འདི་ལ་མུ་སྟེགས་ཅན་དང་འདྲ་བ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 454]
ཇི་ལྟར་མུ་སྟེགས་ཅན་རབ་ཏུ་བྱུང་བའི་བདག་པོ་ཡིན་པའི་འདུག་གནས་དེ་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཡིན་པ་དེ་བཞིན་དུ་རབ་ཏུ་བྱུང་བ་འདི་པ་བདག་པོ་ཡིན་ལ་ཆོས་འདི་པ་ཡ་མཚན་ཅན་ཐམས་ཅད་མ་ཡིན་པའི་འདུག་གནས་ཀྱང་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཡིན་ཏེ། འདིར་ནི་ལྟུང་བ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 455]
འདིར་གཞུང་ནི་དགེ་སློང་རབ་ཏུ་བྱུང་བས་འདུག་གནས་བགྱིད་དུ་སྩལ་བ༌[^279]དེར་དགེ་སློང་གིས་གདུགས་གཅིག་ལས་ལྷག་པར་གནས་ཤིང་བསོད་སྙོམས་གཅིག་ལས་ལྷག་པར་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 456]
ཉེ་དུས་ཀྱང་ངོ༌[^280]ཞེས་བྱ་བ་མུ་སྟེགས་ཅན་དང་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 457]
འདིར་གཞུང་ནི་བདག་པོ་ཉེ་དུས་བགྱིད་དུ་སྩལ་པ༌[^281]ལགས་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་ཀྱི་བྱེད་པ་པོར་འགྱུར་རོ། །

[Block 458]
ཁ་ཅིག་ནི་འདི་དག་ལ་ལྟུང་བ་མེད་ཅེས་ཟེར་ཏེ་དེ་ནི༌[^282]མི་རིགས་སོ། །

[Block 459]
གང་ཡང་རུང་བ་གཅིག་རབ་ཏུ་བྱུང་བ་ལ་བརྟེན་པའི་དོན་འཛིན་པ་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 460]
འདུག་གནས་གཅིག་ཏུ་ཟ་བའི་ལྟུང་བྱེད་དོ།། །།
--- END BLOCKS ---
