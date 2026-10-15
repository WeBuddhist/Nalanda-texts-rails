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
[Block 491]
དེ་ཁས་ལེན་པ་ཉིད་ལ་གང་དུ་འདི་ནོར༌[^431]དང་འདྲ་བར་འགྱུར་བ་དེའི་ཁོངས་སུ་ཡོ་བྱད་གཏོགས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 492]
དེའི་ཕྱིར་ནོར་དང་འདྲ་བས་གཞན་ན༌[^432]འདུག་པ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་ན་འདུག་པས་ཀྱང་ཤི་བའི་ཡོ་བྱད་ཀྱི་ནོར་དང་འདྲ་བའི་གང་ཟག་དྲུང་ན་འདུག་པས་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 493]
བསྐུར་བ་སྐུར་བར༌[^433]བྱ་བས་མ་སྤངས་པ་ནི་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བསྐུར་བའི་དངོས་པོ་མ་སྤངས་པ་ནི་གང་གིས་སྐུར་བར་བྱེད་པས་བསྐུར་བར་བྱ་བ་ནི། དེ་ཉིད་ཡིན་ཏེ་བསྐུར་བར་བྱ་བ་དང་བཅས་པ་ཉིད་དོ། །

[Block 494]
སྤངས་པ་ནི་སྐུར་བར་བྱེད་པ་ཉིད་ཀྱིའོ་ཞེས་བྱ་བ་ནི་སྐུར་བར༌[^434]བྱེད་པ༌[^435]ནི་སྐུར་བར་བྱེད་པ་ཉིད་དེ་དངོས་པོ་ནི་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི༌[^436]དོན་ཏོ། །

[Block 495]
དེས་སྤངས་ན་ཡང་ངོ་ཞེས་བྱ་བ་ལ། དེས་ཞེས་བྱ་བ༌[^437]ནི་སྐུར་བར་བྱེད་པ་དེས་སོ། །

[Block 496]
གང་ལ་སྟེ༌[^438]གང་ལ་སྐུར་བར༌[^439]བྱེད་པ་དེ་ནི་སྤང་བར་འགྱུར་རོ། །

[Block 497]
འདིར་སྐུར་བར༌[^440]བྱེད་པ་སྤངས་པ་ནི་བཤད་པ་ལ་སྐུར་བར༌[^441]བྱེད་པ༌[^442]སྤངས་བར་མི་འགྱུར་རོ། །

[Block 498]
གལ་ཏེ་འདིས་སྔ་མ་བཟུང་ན་འདིས་བདག་ལ་ཅི་ཞིག་བྱ་ཞེས་བདག་གིས་འདི་སྤངས་སོ་ཞེས་བྱ་བ་སྟེ། དེ་ལྟར་ཡང་སྐུར་བར༌[^443]བྱེད་པ་ཉིད་ཀྱི་དེ་དང་འབྲེལ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 499]
འདིར་གཞུང་ནི། དགེ་སློང་གིས་དགེ་སློང་ལ་ཆོས་གོས་དག་བསྐུར་ནས་གང་ལ་བསྐུར་བ་དེས་སྤངས་ནས། གང་གིས་བསྐུར་བ་དེས་ཀྱང་སྤང༌[^444]ན་གང་ལ་བསྐུར་བ་དེ་ཡིར་བྱིན་གྱིས༌[^445]རློབ་ན་ནི་བྱིན་གྱིས་མ་བརླབས་པ་ཡིན་ནོ། །

[Block 500]
གང་གིས་བསྐུར་བ་དེ་ཡིར་བྱིན་གྱིས་རློབ༌[^446]པར་བྱེད་ན་ནི་བྱིན་གྱིས་བརླབས་པ་ཡིན་ཏེ། ལེགས་པར་བྱིན་གྱིས་བརླབས་པ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། འདི་མི་རིགས་པར་ཤེས་པར་མི་བྱ་སྟེ། གང་གི་ཕྱིར་དེ་ལྟ་བུར་གྱུར་པའི་འཇུག་པ་ལ་མི་དགོས་པའི༌[^447]མི་གཙང་བ་ལ་བདག་གིས་འདི་དོར་རོ་སྙམ་པ་དེ་ལྟ་བུའི་བློ་དང་འདྲའོ། །

[Block 501]
དེའི་དགོས་པ་ནི་བདག་པོ་སོ་སོ་སོ༌[^448]སོར་བྱེད་ཅིང་དེ་ལ་ཡིད་བརྟེན༌[^449]ནས་རྣམ་པར་གཞག་པ་ཤི་བའི་ཡོ་བྱད་དུ་བྱིན་གྱིས་རློབ་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 502]
ཕྱི་རོལ་དུ་ཡང་མཚམས་ཀྱི་ནང་དུ་འདུ་ཤེས་པ་དག་གིས་འབའ་ཞིག་གིས་བྱིན་གྱིས་རློབ་པ་མི་འཆགས་སོ་ཞེས་བྱ་བ་ལ། ཕྱི་རོལ་དུ་ཡང་ཞེས་བྱ་བ་ནི་ནང་དུ་མ་བྱས་པ་ལ་སོགས་པ་བྱིན་གྱིས་བརླབ་པའོ། །

[Block 503]
མི་འཆགས་སོ་ཞེས་བྱ་བ་ལ་ཡང་གི་སྒྲ་འདི་ནི་མ་གྲགས་སོ། །

[Block 504]
ནང་དུ་འདུ་ཤེས་པ་དག་གིས་ཞེས་བྱ་བ་མཚམས་ཀྱི་ཞེས་བྱ་བར་སྦྱར་ཏེ། མཚམས་ཀྱི་ནང་དུ་འདུ་ཤེས་པ་དག་གིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 505]
འབའ་ཞིག་གིས་བྱིན་གྱིས་བརླབས་པ༌[^450]ཞེས་བྱ་བ་འབའ་ཞིག་དག་གིས་བྱིན་གྱིས་བརླབ༌[^451]པོ། །མཚམས་ཀྱི་ནང་དུ་འདུ་ཤེས་པ་རྣམས་ལ་ཕྱི་རོལ་དུ་ཡང་བྱིན་གྱིས་རློབ་པར་བྱེད་པ་ནི་འབའ་ཞིག་གིས་ཞེས་བྱ་བ་མི་མཐུན་པ་དག་གིས་བྱིན་གྱིས་རློབ་པར་བྱེད་ན་མི་འཆགས་སོ། །

[Block 506]
མི་འཆགས་པར་མི་བྱའོ་ཞེས་སྤྱིར་བསྟན་པ་དེས་འདི་ལ་ཉེས་བྱས་སུ་ཤེས་པར་བྱའོ། །

[Block 507]
ཡིད༌[^452]གཉིས་ཟ་བ་ལ་ཡང་ཡིད་གཉིས་ནི་མཚམས་ཀྱི་ནང་དུ་དེ་སྨོས་པ་ཞེས་བྱ་བར་རིག་པར༌[^453]བྱའོ། །

[Block 508]
གང༌[^454]ཞིག་ཕྱི་རོལ་དུ་མཚམས་ཀྱི་ནང་དུ་འདུ་ཤེས་པའམ་ཡིད་གཉིས་ཟ་བས་རྐུ་སེམས་ཀྱིས་བྱིན་གྱིས་རློབ་པར་བྱེད་ན་རྐུ་སེམས་དེ་ལ་ཉེས་པ་སྦོམ་པོར་བྱས་པར་འགྱུར་རོ། །

[Block 509]
དེའི་ཕྱིར་རྐུ་སེམས་ལ་ཉེས་པ་སྦོམ་པོར་རིག་པར་བྱའོ། །

[Block 510]
བཙུན་པ་གང་ཞིག་མཚམས་ཀྱི་ནང་དུ་རྐུ་སེམས་ཀྱིས་སྔར་ཕྲོགས་པ་ཉིད་ཀྱི་ཕྱིར་ཉེས་པ་སྦོམ་པོར་བྱས་ན་ནི་དངོས་པོ་ལས་རྣམ་པར་གཞག་གོ། །

[Block 511]
དབྱུང་བ༌[^455]དང་རིམ་གྲོ་དང་ཆོས་མཉན་པ་དང་ཡོན་བཤད་པ་མ་བྱས་པར་བྱིན་གྱིས་བརླབ་པར་མི་བྱའོ། །

[Block 512]
ལྷུང་བཟེད་དང་ཆོས་གོས་ཁྱིམ་གཞན་ན་འདུག་པ་ཉིད་ནི་ཁྱིམ་བདག་གིས་གང་ལ་བྱིན་པ་དེ་དབང་བ་ཉིད་ཡིན་ནོ། །

[Block 513]
གལ་ཏེ་དབང་ཞིང་དེས་ཕོངས་པ་ཡིན་ནའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། གླེང་གཞི་རྣམས་ལས་དེ་མཐར་ཐུག་པའོ། །

[Block 514]
ཁྱིམ་བདག་གིས་གང་ལ་བྱིན་པ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་ཡོངས་སུ་མ་སྨོས་པས་གཅིག་དང་དུ་མ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 515]
གལ་ཏེ་འདི་ཁྱིམ་པ་དང་མུ་སྟེགས་པའི་རབ་ཏུ་བྱུང་བ་དང་། འདི་པའི་རབ་ཏུ་བྱུང་བའམ་མཚམས་ཐ་དད་པ་གཞན་ལ་བྱིན་པར་གྱུར་ན་ཅི་དེ་ལ་ཡང་དབང་བ་ཉིད་དམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་དབང་ཞིང་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 516]
གང་ལ་རྙེད་པ་དེ་ཡོད་ན་གལ་ཏེ་དབང་བ་དེ་ལ་བྱིན་པར་གྱུར་ན་ཅི་དེ་ལ་ཡང་རྙེད་པ་ཙམ་གྱི༌[^456]དབང་གིས་དེ་དབང་བ་ཉིད་ཡིན་ནམ་ཞེ་ན། ཕོངས་པ་ཡིན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི། མེད་དེ་འདིར་ཡང་ཆོ་ག་འདི་སྦྱར་བ་ཞེས་བྱ་བ་དེ་བས་ན་དེ་ལ་མངོན་པར་བརྟེན་པའོ། །

[Block 517]
གལ་ཏེ་ཁྱིམ་བདག་སྦྱིན་པའི་ཕྱིར་འཇུག་པར་མི་བྱེད་ན། དེའི་ཚེ་སུ་དབང་བ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྦྱིན་པར་མི་བྱེད་ན་བླངས་པ་དང་ལྡན་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཡང་དབང་ཞིང་དེས་ཕོངས་པའོ་ཞེས་བྱ་བ་དབང་དུ་བྱ་བ་དང་སྦྱར་བར་རིག་པར་བྱའོ། །

[Block 518]
དུ་མ་ལ༌[^457]ཡང་ཞེས་བྱ་བ་ནི་ཁྱད་པར་ཡོངས་སུ་མ་བཟུང་བར་རིག་པར་བྱའོ། །

[Block 519]
དེ་ཡང་འདི་ཅིག་ཅར་བླངས་པ་ལ་ཤེས་པར་བྱའོ། །

[Block 520]
གཞན་ཡང་བརྗོད་པར་བྱ་སྟེ། མཐར་གྱིས་ནི་དང་པོའི༌[^458]ཞེས་བྱ་བ་ནི་བླངས་པ་དང་ལྡན་པའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 521]
གང་ཞིག་དང་པོར་བླངས་པ་དེ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ།[^459] །གང་དུ༌[^460]ཡོངས་སུ་འཛིན་པ་པོ་མེད་པ་ཉིད་དེ་ཙམ་ལ་བརྟེན་ནས། གང་ཟག་གང་ལ་ཡང་བྱེ་བྲག་ཏུ་མ་བྱས་པར་སུ་ཁྱེར་བ་ཁྱེར་ཅིག་སྙམ་དུ་བོར་བར་གྱུར་ན་དེ་ལ་སུ་དབང་བ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མེད་པ་ཉིད་ཡིན་ཞིང་མ་བསྔོས་པར་བོར་ན་སོང་བ་དང་ལྡན་པའོ། །

[Block 522]
དེ་ནི་མཐར་གྱིས་དང་འདྲའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་ལྟར་མཐར་གྱིས་སློང་བ་དང་པོར་གང་གིས་བླངས་པ་དབང་བ་དང་འདྲ་བར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 523]
བུ་ལོན་པ་བྱུང་ན་དེ་ལ་གཞལ་བར་བྱ་བའི་ཚད་ཀྱི་ཤི་བའི་ཡོ་བྱད་དེ་དབང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་དེ་ལ་གཞལ་བར་བྱ་བའི༌[^461]ཚད་ཀྱི་ཞེས་བྱ་བ་ནི། གང་ཞིག་བུ་ལོན་པ་དེ་ཤི་བ་དེས་གཞལ་བར་བྱ་བའི་རྫས་ཀྱི་ཚད་ཀྱི༌[^462]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 524]
དེ་དབང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི༌[^463]བུ་ལོན་པ་ཉིད་དབང་བ་ཉིད༌[^464]ཡིན་ནོ། །

[Block 525]
མ་བགོས་པར་བྱུང་ན་དེ་ལ་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་རྣམས་ཀྱིས་དེ་གཞལ་བར་བྱ་བ་ཡིན་གྱི། བགོས་པའི་འོག་ཏུ་བྱུང་ན་ནི་དེ་ལ་མི་གཞལ་བར་བྱ་བ་ཉིད་དོ་སྙམ་དུ་དོགས་པ་བསལ་བའི་ཕྱིར་བགོས་ན་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཞལ་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 526]
དེ་དང་ལྷན་ཅིག་རྣམ་པར་གཞག་པ་དེ་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་དམ་བླང་བར་བྱ་བ་ཉིད་གང་ཡིན་པ་སྟེ། དེ་ཉིད་ནི༌[^465]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཤི་བ་དེ་དང་བུ་ལོན་དེད་པ་དང་། བུ་ལོན་འཇལ་བར་ལྷན་ཅིག་གང་ཞིག་གནས་པ་དེ་ལ་འདིར་དགེ་སློང་རྣམས་ཀྱིས་གཞལ་བར་བྱ་བའམ། བསླང་བར༌[^466]བྱ་བ་ཉིད་དེ་དེ་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 527]
གང་ཞིག་དེས་བུ་ལོན་པའི་དྲུང་ནས་བླངས་པ་དེ་བུ་ལོན་ཆགས་པ་ལ་སྦྱིན་པའོ། །

[Block 528]
ཀཱཪྵཱ་པ་ཎ་རྣམས་དབུལ་བར་བྱའོ་ཞེས་བྱ་བས་ཀཱཪྵཱ་པ་ཎ་རྣམས་བཟུང་བ་དེ་རྣམས་ཉིད་གཞལ་བར་བྱའོ། །

[Block 529]
རས་ཡུག་ཆེན་བླངས་ཏེ་རིན་སྦྱིན་པར་བྱའོ་ཞེས་འཐམས་པ༌[^467]ལ་ནི་རིན་སྦྱིན་པར་བྱའི་རས་ཡུག་ཆེན་དངོས་སྦྱིན་པར་མི་བྱ་བ་དང་། ཐ་ག་པ་ལ་རས་ཡུག་ཆེན་གྱི་དོན་དུ་རྒྱུ་སྤུན་གཏད་པ་ལས་ནི་རས་ཡུག་ཆེན་བླང་བར་བྱའི། [^468]རྒྱུ་སྤུན་བླང་བར་མི་བྱ་བ་ལྟ་བུའོ། །

[Block 530]
འདིར་གཞུང་ནི། དགེ་སློང་གིས་ཕྲ་བ་བསླངས་པ་དང་། དེ་ན་རེ་འཕགས་པ་དག་བདག་གིས་དེ་ལ་སྦོམ་པོ་དབུལ་བར༌[^469]བགྱི་བ་ལགས་སོ་ཞེས་ཟེར་ནས།[^470] བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་དག་དགེ་སློང་ཤི་བ་ཅི་འདྲ་བ་གཏད་པ་དེ་འདྲ་བ་བསླང་བར༌[^471]བྱའོ་ཞེས་གསུངས་པ་དེ་ནི་ཐ༌[^472]སྙད་ཀྱི་ཆོ་གས་ངེས་པར་དེ་བླང་བ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
