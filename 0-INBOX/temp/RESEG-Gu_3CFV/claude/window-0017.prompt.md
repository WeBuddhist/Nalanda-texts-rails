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
རྫས་སྙི་བ་ཉིད་ནི་ཕྱེ་མར་བྱས་པ་ཉིད་ན་ཡང་སྙི་བ་ཉིད་དང་བྲལ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 597]
དེ་བས་ན་འདིར་རྩྭ༌[^355]སྐོར་ཀ་ལ་སོགས་པ་རྣམས་ལ་འདིར་ཞུགས་པར་རིག་པར་བྱའོ། །

[Block 598]
སྙི་བ་རྣམས་ཀྱི་ནི་ཁ་དོག་གྱུར་པའོ་ཞེས་ཞེས་བྱ་བ་ནི་རྫས་སྙི་བ་རྣམས་ཀྱི་ཁ་དོག་གྱུར་པའི་མདུན་རོལ་དུ་དེ་ཉིད་ཡིན་ཏེ་རྗེན་པ་ཉིད་ཡིན་ནོ། །

[Block 599]
ཁུ་བ་རྣམས་ཀྱི་ནི་ལན་གཉིས་ཁོལ་བར་གྱུར་པ་ཉིད་ཀྱིའོ་ཞེས་བྱ་བ་ནི་མདུན་རོལ་དུ་དེ་ཉིད་ཅེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 600]
མེས༌[^356]རུང་བར་བྱས་པ་ནི་མ་བཙོས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། གང་གི་ཕྱིར་དེ་ལྟར་ཡིན་པ་དེ་བས་ན་མཚམས་ཀྱི་ནང་དུ་མེས་རུང་བ་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 601]
འདུག་པའི་གྲུབ་པ་ཉིད་སྐྱེ་བ་ལ་རག་ལས་པ་ལ་ནི་མ་ལོན་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདུག་པ་གང་གི་གྲུབ་པ་ཉིད་སྐྱེ་བ་ལ་རག་ལས་པ་འདུག་པའི་གྲུབ་པ་ཉིད་དོ། །

[Block 602]
དེར་སྐྱེ་བ་ལ་གང་ཞིག་འདི་མི་འབྲེལ་བའམ་སྐྱེ་བའི་རྒྱུན་དང་འབྲེལ་བའི་ཇི་ལྟར་སྐྱེ་བ་ཉིད་ལ་སྐྱེ་བའི་རྒྱུན་དང་བྲལ་བ་ལ་གང་ཞིག་དེར་གནས་པ་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 603]
དེ་ཉིད་ནི་འདི་ལྟར་གྱུར་པ་ཉིད་དོ། །

[Block 604]
གང་ཞིག་འདུག་པ་ལ་མ་ལོན་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ནང་དུ་ཞག་མ་ལོན་པ་ཉིད་དུ་མི་འགྱུར་ཞེས་བྱ་བ་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 605]
སྐྱེ་བའི་རྒྱུན་རུང་བ་མ་ཡིན་པའི་ས་ནས་བྱུང་བ་ལ་རུང་བའི་ས་ནས་བྱུང་བ་གང་ཡིན་པ་དེར་བསྒྲུབ་པ་གང་ཡིན་པའོ། །

[Block 606]
ནང་དུ་ཞག་མ་ལོན་པ་ཉིད་ཅེས་བྱ་བ་ནི་ས་བོན་ནང་དུ་ཞག་ལོན་པ་ཕྱི་རོལ་དུ་བཏབ་པ་ལས་སྐྱེས་པ་གང་ཡིན་པ་དེ་ལ་ཡང་ཆོ་ག་འདི་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཞེས་བསྟན་པ་ནི་དེ་དང་འཕེལ་བ་ཉིད་དམ། དེའི་གནས་སྐབས་གཞན་ཉིད་ཀྱིས་གང་དུ་ཡིད་ཆེས་པ་དེ་ལ་ནི་ཆོ་ག་འདི་ཡིན་ནོ། །

[Block 607]
སྐྱེ་བ་གཞན་ཉིད་དང་དེ་དང་འཕེལ་བ་ཉིད་དང་དེའི་གནས་སྐབས་གཞན་ཉིད་ཀྱི་ཆོ་ག་འདི་ཡིན་ནོ། །

[Block 608]
དེ་ལ་ཇི་ལྟར་ལུང་ལ་སོགས་པའི་ནང་དུ་བཞག་པ་ཞིང་ལ་གཏོར་བ་ལ་བཟའ་བར་མི་བྱ་བ་མ་ཡིན་པ་ནི་བྱེད་པ་པོ་ཉིད་མ་ཡིན་པ་དེ་བཞིན་དུ་འདི་ལ་ཞག་ལོན་པའི་བ་ལ་འོ་མ་བྱུང་བ་གང་ཡིན་པ་དེ་ཡང་བཟའ་བར་བྱ་བ་མ་ཡིན་པ་ཁོ་ན་སྟེ། འོ་མ་དེ་མཚམས་ཀྱི་ནང་ནས་བྱུང་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 609]
སྣོད་ཕྱོགས་ན་འདུག་པ་དེས་ཀྱང་ས་དེར་བཙོས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། སྣོད་རུང་བ་མ་ཡིན་པའི་ཕྱོགས་ན་འདུག་པ་ནི་དཔེར་ན་སར་གཞག་པའམ་རྒྱུད་ནས་སོ། །

[Block 610]
དཔེར་ན་སོལ་བ་རྣམས་ལ་བཞག་པའམ་རྩྭ༌[^357]ལ་སོགས་པ་གང་ཡང་རུང་བ་ལ་དེའི་ས་གཞི་ལ་བཙོས་པ་ཉིད་དང་མ་བཙོས་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 611]
འཚོད༌[^358]པར་བྱེད་པ་པོ༌[^359]དེ་ན་འདུག་པ་ཉིད་ཀྱིས་ནི་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི། གང་ཞིག་ས་དེ་ལ་བརྟེན་པ་ཉིད་ཀྱིས་ས་དེའི་བཙོས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 612]
མེ་ནི་སྣོད་མ་ཡིན་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། མེ་ཞེས་བྱ་བ་ནི་སོལ་བ་རྣམས་ལ་ཡིན་གྱི་འོད་འཕྲོ་བ་རྣམས་ལ་མ་ཡིན་ཏེ། ནམ་མཁའ་དང་འདྲ་བ་ཉིད༌[^360]ཡིན་པའི་ཕྱིར་རོ། །

[Block 613]
དེ་ལས་ཕྱུང་བ་དང་བྱུང་བ་དག་ནི་དེ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མེ་དེ་ལས་སམ་བོང་བ་ལ་སོགས་པ་སུ་ཞིག་གིས་ཕྱུང་བ་དང་རང་གིས་སམ་རླུང་ལ་སོགས་པའི་དབང་གིས་འབྱུང་བ་ལ་དེ་ཉིད་མ་ཡིན་ཏེ། གང་ལས་ཕྱུང་བ་དང་བྱུང་བ་དག་ལས་དེར་གྱུར་པ་ཉིད་དམ་ས་དེ་ལ༌[^361]བརྟེན་པ་ཉིད་དོ། །

[Block 614]
ཉེན་ཀོར་ནི་གནས་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། གནས་ཞེས་བྱ་བ་ནི་ངེས་གནས་པར་བྱ་བ་ཡིན་པས་ན་གནས་ཞེས་བྱ་བ་བརྗོད་དོ། །

[Block 615]
སྟེང་དུ་རྒྱུ་བ་གང་ཡིན་པ་གནས་ཀྱི་དེ་ཁོ་ན་ཉིད་ལ་དེར་མི་ཞུགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 616]
ལམ་ཇི་སྲིད་ཚུན་ཆད་འདིའི་དེ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འདོམ་གང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕྱི་རོལ་གྱི་རྩིག་པ་ལ་སོགས་པའི་ངོས་ནས་བརྩམས་ཏེ་དེ་དང་འདྲ་བ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་དུ་རྟོགས་པར་བྱའོ། །

[Block 617]
སྟེང་དུ་ནམ་མཁའ་ལ་སླེབ་པ་མན་ཆད་དོ་ཞེས་བྱ་བ་ནི་གནས་ཀྱི་སྟེང་གི་ནམ་མཁའ་ནི་ནམ་མཁའ་སྟེ། རྒྱུ་བ་དག་གིས་སླེབ་པར་ནུས་པ་དེ་ལ་ནི་གནས་ཉིད་དེ་སྟེང་དུ་ལག་པས་སླེབ་པ་ནི་ཡན་ལག་མ་ཡིན་ནོ། །

[Block 618]
དེ་བས་ན་མགོ་བོས་སླེབས་པར་གྱུར་པ་ནི་འདིར་མཐར་ཐུག་པ་ཉིད་དེ། དེ་འདིར༌[^362]མ་གཡོགས་པ་དང་མ་བཀབ་པའི་དབང་དུ་བྱས་ནས་བསྟན་པའོ། །

[Block 619]
བཀབ་པའི་དབང་དུ་བྱས་ནས་བསྟན་པ་ནི་ཀུན་ནས་མ་བཀབ་པ་ནི་མ་གཡོགས་པའོ། །

[Block 620]
ནང་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ནང་གི་ནམ་མཁའ་གང་ཡིན་པ་དེ་ཡང་གནས་ཉིད་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 621]
དེ་འདི་ཙམ་དུ་རུང་བ་ལ་རུང་བ༌[^363]ཉིད་དང་མི་རུང་བ་ལ་མི་རུང་བ༌[^364]ཉིད་ཀྱིས༌[^365]གནས་ཀྱི་གཞི་ལ་ཞུགས་པ་ཞེས་བྱ་བ་འདིའི་བྱེད་པའོ།[^366] །སྟེང་གི་ཡ་ཐོག་གཞན་ཡང་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། སྟེང་གི་ཡ་ཐོག་ཁ་ཁྱེར་གཞན་ཡང་འོག་ཁང་དེ་ཁོ་ན་ཉིད་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 622]
ནམ་མཁའི་དཀྱིལ་ནི་སྟེང་གི་ཡ་ཐོག་ཐམས་ཅད་ལ་མངོན་སུམ་དུ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 623]
དེའི་སྒོ་འོག་མ་རྣམས་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 624]
མ་འབྲེལ་པའི་ངོ་བོ་སྟེང་དུ་བསྒྲུབ་པ་དང་འཚེད་པ་ལ་སོགས་པའི་འོག་ཁང་གི་གནས་ཞེས་བྱ་བ་སྟེང་འོག་ཏུ་བསྒྲུབ་པ་དང་འཚེད་པ་ལ་སོགས་པའི་འོག་ཁང་གི་གནས་ཞེས་བྱ་བ་སྟེ་དེ་བས་ན་འདི་ཤེས་པའོ། །

[Block 625]
དེའི་ཕྱིར་རྟེན་ལས་རྣམ་པར་བཅད་ནས་ཕྱི་མ་ལ་རུང་བ་ཉིད་ཀྱིས་བློ་མཐུན་པར་མ་གྲགས་པ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 626]
འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས།

[Block 627]
བཙུན་པ་གང་འོག་ཁང་གི་རུང་བའི་ཁང་པ་ལགས་པ་དེའི་ཡང་ཐོག་ཀྱང་རུང་བའི་ཁང་པ་ལགས་སམ། ཉེ་བ་འཁོར་ཡང་ཐོག་ཀྱང་ཡིན་ཏེ། ངོས་དག་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 628]
གཞན་གནས་པ་ཉིད་ནི་གཞན་གྱི་གནས་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གནས་འདི་ལ་ཡང་གནས་ཤེས་པར་བྱ་བར་བརྗོད་དོ། །

[Block 629]
གཞན་པར་གྱུར་པ་ཉིད་ནི་གཞན་གྱི་གནས་ཉིད་མ་ཡིན་ནོ། །

[Block 630]
དཔེར་ན་ཁྱིམ་པས་བཟུང་བ་འམ་གནས་པར་གྱུར་ན་འདི་ལྟར་དགེ་སློང་དག་དེ་ཉིད་ན་གནས་སུ་ཟིན་ཀྱང་དེ་དགེ་སློང་གི་གནས་ཉིད་མ་ཡིན་པ་ལྟ་བུའོ། །

[Block 631]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 632]
བཙུན་པ་དེ་ཉིད་ན་དགེ་སློང་དང་བཅས་ཤིང་དེ་ཉིད་ན་ཁྱིམ་པ་དང་བཅས་ན་དེར་དགུང་དུ་ལགས་པ་དང་དེར་བསྒྲལ་བར་འཚལ་བར་བགྱི་འམ༌[^367]མི་བགྱི། ཉེ་བ་འཁོར་བཟའ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 633]
གནས་སྟོང་པར་བྱས་པ་ཞིག་ཏུ་གལ་ཏེ་དགེ་སློང་རེ་ཞིག་གནས་པར་གྱུར་ན་དེ་ཡང་དགེ་སློང་གནས་སུ་རུང་བ་ཉིད་ཡིན་ནོ། །

[Block 634]
ཁྱིམ་པའི་རྫས་མ་བཏོན༌[^368]ན་ནི་སྟོང་པར་བྱ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 635]
དགེ་ཚུལ་རྣམས་ཀྱི་གང་ཟག་གི་གནས་དང་། དགེ་ཚུལ་འཚོགས༌[^369]ས་སྤྱིར་དབང་བའི་གནས་དེ་ནི་དགེ་སློང་གི་གནས་ཉིད་མ་ཡིན་ནོ། །
--- END BLOCKS ---
