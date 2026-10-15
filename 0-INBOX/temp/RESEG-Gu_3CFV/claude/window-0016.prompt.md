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
[Block 561]
རང་གི་ཕྱེད་ཡོལ་ནས་སྐྱ་རེངས་འཆར་བའི་བར་དུས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། རང་གི་ཞེས་བྱ་བ་ནི་ཕྱེད་ཡོལ་བ་དང་སྐྱ་རེངས་ཤར་གྱིས༌[^332]ཀྱང་འདི་ལ་འབྲེལ་པའོ། །

[Block 562]
རང་གི་ཕྱེད་ཡོལ་བའི་མཐར་ཐུག་པ་ལ་རང་གི༌[^333]སྐྱ་རེངས༌[^334]འབྱུང་བ་ལ་ཡང་བར་དུ་ཞེས་བྱ་བ་ནི་ཕྱེད་ཡོལ་མན་ཆད་ནས་སྐྱ་རེངས་འཆར་བའི་བར་གང་ཡིན་པ་དེ་ནི་འདིར་མངོན་པར་འདོད་པར་རིག་པར་བྱའོ། །

[Block 563]
འདིར་གཞུང་ནི་འཛམ་བུའི་གླིང་ལ་སོགས་པ་གནས་གང་ན་སོ་སོར་གནས་པ་དེ་ལ་རང་གི་ཞེས་བྱ་བར་འགྱུར་རོ། །

[Block 564]
དགེ་སློང་གིས༌[^335]དུས་མ་ལགས་པར་བཅའ་བར་བགྱི་བ་དང་བཟའ་བར་བགྱི་བ་འཚལ་བ་ལྟུང་བར་མི༌[^336]འགྱུར་བ་མཆིས་སམ། ཡོད་དེ་འཛམ་བུའི་གླིང་པའི་དུས་ཀྱིས་གླིང་གསུམ་པ་དག་ཏུ་ཟོས་ན་ལྟུང་བར་མི་འགྱུར་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 565]
དེ་ཉིད་ལ་ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་དུས་མ་ཡིན་པ་དེ་ཉིད་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 566]
ཅི་ཀུན་དུ༌[^337]སྤྱོད་ན་ཞེ་ན་དེའི་ཕྱིར་བཅའ་བར་བྱ་བ་དང་བཟའ་བར་བྱ་བ་ཟོས་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 567]
དུས་མ་ཡིན་པར་ཟ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 568]
གསོག་འཇོག་གི་ངོ་བོ་བསྟན་པར་བྱ་སྟེ། དེའི་ཕྱིར་སྔ་དྲོའི་ཟས་བྱིན་ལེན་བྱས་པ་ཕྱི་དྲོའི་ཟས་སུ་དང་དེ་ཐུན་ཚོད་ལས་འདས་པ་ལྟ་བུ་ནི་སོག་འཇོག༌[^338]བྱས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཕྱི་དྲོའི་ཟས་སུ་དང་སྔ་དྲོའི་ཟས་བྱིན་ལེན་བྱས་པ་ཕྱི་དྲོ་ཟོས་པ་ལ་སོགས་པ་སོག་འཇོག༌[^339]དང་བྱིན་ལེན་བྱས་པ་ཕྱི་དྲོའི་ཟས་སུ་དང་། དེ་ཐུན་ཚོད་ལས་འདས་པ་ལྟ་བུ་ནི་སོག་འཇོག༌[^340]བྱས་པ་ཉིད་ཡིན་ནོ། །

[Block 569]
དེ་ཉིད་ལ་ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་སོག་འཇོག༌[^341]བྱས་པ་དེ་ཉིད་ལའོ། །ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་བཅའ་བར་བྱ་བ་དང་བཟའ་བར་བྱ་བ་ཡང་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 570]
ལག་ཉར་བླངས་པ་མེད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདི་ནི་གླེང་གཞི་དག་ལས་ཡིན་ཏེ། བཟའ་བར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 571]
མཚམས་ཀྱི་ནང་དུ་བཙོས་པ་དང་ཞག་ལོན་པ་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་སྨན་གྱི་གཞི་ལས་འདི་དང་པོ་སྟེ།

[Block 572]
གཉིས་པ་ནི་ལྡང་བ་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 573]
མཚམས་ཀྱི་ནང་དུ་ཞེས་བྱ་བ་ནི་མཚམས་ཀྱི་ནང་རོལ་དུའོ། །

[Block 574]
འདིར་གཞུང་ནི་ནང་དུ་བཙོས་པ་གང་ཞེ་ན། གང་ཞིག་ཀུན་དགའ་ར་བའི་ནང་དུ་བློ་མཐུན་པར་མ་བསྐོས་ཤིང་རུང་བ་མ་ཡིན་པའི་ས་གཞིར་བཙོས་པ་གང་ཡིན་པ་དེའོ། །

[Block 575]
བཙོས་པ༌[^342]དང་བཞག་པ་ཞེས་བྱ་བ་ཇི་ཙམ་ཡིན་ཞེ་ན། གང་ཞིག་ཀུན་དགའ་ར་བའི་ནང་དུ་བློ་མཐུན་པར་མ་བསྐོས་ཤིང་རུང་བ་མ་ཡིན་པའི་ས་གཞིར་བཙོས་པ་དང་ཞག་ལོན་པ་གང་ཡིན་པའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དགེ་སློང་བསྙེན་པར་རྫོགས་པས་བཟའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་མ་མོ་ལས་འདིར་ཀུན་དགའ་ར་བའི་ནང་དུ་དོན་གྱིས་ཚོགས་བསྟན་པ་མཚམས་ཀྱི་ནང་དུ་ཞེས་བྱ་བ༌[^343]གསུངས་པ་ཡིན་ནོ། །

[Block 576]
གནས་ཀྱི་གཞི་ལས་ཀྱང་འདིར་ཀུན་དགའ་ར་བའི་སྒྲ་ནི་གྲགས་པ་སྟེ། དེས་ན༌[^344]དགེ་སློང་གིས་ཀུན་དགའ་ར་བའི་ཕྱི་རོལ་དུ་སོང་ནས་བཤགས་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 577]
ཀུན་དགའ་ར་བའི་ཕྱི་རོལ་དུ་བཅའ་བར་བྱ་བ་དང་བཟའ་བར་བྱ་བ་བླངས་ཏེ། ཀུན་དགའ་ར་བའི་ནང་དུ་བཟའ་བར་བྱའོ། །

[Block 578]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀུན་དགའ་ར་བའི་ནང་དུ་སྟེང་གི་སྒྲ་དང་སྒྲ་ཆེན་པོ་གསན་པར་གྱུར་ནས་དེ་བས་ན་དགེ་འདུན་གྱི་ཀུན་དགའ་ར་བ་ཞེས་བྱ་བ་གནས་ཀྱི་གཞི་ལ་འདི་གསུངས་པའོ། །

[Block 579]
གསོག་འཇོག་བྱེད༌[^345]པ་ཡོངས་སུ་བསལ་བ་འདི་ནི་ལན་ཏེ། གང་ཞིག་འདི་མཚམས་ཀྱི་ནང་དུ་བཙོས་པ་དང་ཞག་ལོན་པ་ཉིད་ནི་དོར་བའོ། །

[Block 580]
གནས་ཀྱི་གཞི་ལས་ཀྱང་གསོག་འཇོག་འབྱུང་བ་སྟེ་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 581]
དགེ་སློང་གིས༌[^346]བཙོས་པ་ལ་ཡང་གསོག་འཇོག་བྱེད་པ་དང་གཟི་བརྗིད་མེད་པའི་ཕྱིར་བོར་བ་ཉིད་དོ། །

[Block 582]
དེ་བས་ན་འདིར་ཡང་དགེ་སློང་གིས་བཙོས་པ་ལ་དགེ་སློང་ཉིད་ཀྱིས་བཟའ་བར་བྱ་བ་ཉིད་དང་དགེ་སློང་མས་བཙོས་པ་ལ་དགེ་སློང་མ་ཁོ་ནས་ཟ་བ་ཉིད་དོ༌[^347]ཞེས་བྱ་བ་འདིའི་རྣམ་པར་འབྱེད་པའོ། །

[Block 583]
གང་ཞིག་སྦྱིན་བདག་གིས་རུང་བ་མ་ཡིན་པའི་གཞིར་བཙོས་པའམ་ཞག་ཏུ་ལོན་པ་འབུལ་བར་བྱེད་པ་དེ་ལ་ནི་ལྟུང་བའི་ཉེས་པ་མེད་དོ། །

[Block 584]
འབུལ་བ་ནི་རང་འོངས་ནས་བརྟག་པར་བྱ་ཞེས་བྱ་བ་ཡང་ངེས་པ་ཡོད་དེ་བདག་ཏུ་བྱ་བའི་དོན་ཡོད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ཡང་འདི་ལས་རྟོགས་པར་བྱའོ། །

[Block 585]
དགེ་སློང་གིས་གྲོང་དག་ཏུ་དགེ་སློང་གི་དོན་དུ་དགོས་པའི་གནས་ལ་སོགས་པ་གང་དག་བྱེད་ཅིང་། དེ་དག་གི་ནང་དུ་གང་ཞིག་དགེ་སློང་རྣམས་ཀྱིས༌[^348]གནས་པ༌[^349]དེ་ལ་དགེ་སློང་རྣམས་ཀྱིས་གནས་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 586]
དེར་གནས་པ་བཏང་བ་ནི་དགེ་སློང་གི་གནས་ཀྱི་གཞི་ཉིད་དང༌[^350]བྲལ་བ་ཉིད་ཁོ་ན་ཡིན་ནོ། །

[Block 587]
འདི་ལ་ངེས་པར་བྱས་པ་དེ་ནི་གནས་ཉིད་དང་བྲལ་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 588]
དེ་བས་ན་འདིར་གནས་པར་མི་བྱ་ཞེས་བྱ་བ་ངེས་པར་བྱས་པ་གང་ཞིག་མི་འཇུག་པར་གནས་གཞན་གྱི་དབང་གིས་གཙུག་ལག་ཁང་དུ་ཞུགས་པ་ལ་དེ་དང་བྲལ་བ་ཉིད་འབྱུང་བར་འགྱུར་རོ། །

[Block 589]
གཞི་མ་ཡིན་པའི་ས་ཕྱོགས་ལ་ཡང་ལྷག་པར་གནས་པར་གྱུར་པ་ལ་གནས་ཀྱི་གཞི་ཉིད་དོ། །

[Block 590]
དེ་བས་ན་བདེ་བའི་དོན་དུ་འདའ་བར་གྱུར་པ་རྣམས་ལ་གཙུག་ལག་ཁང་སྟོང་པར་གནས་པ་ལ་གནས་ཉིད་ལས་སྐྱེས་པ་ཉིད་དོ། །

[Block 591]
མཚམས་གསུམ་པོ་ཉིད་ལ་གནས་ཀྱི་གཞི་དེ་གཏོགས་པར་བྱའོ། །

[Block 592]
དེར་ཡང་རང་བཞིན་ཅན་ཡིན་གྱི༌[^351]བཅོས་པ་མ༌[^352]ཡིན་ནོ། །

[Block 593]
སླར་འདིར་རྩིག་པ་ལ་སོགས་པའི་མཐའ་ནས་བརྩམས་ཏེ་ནང་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འདིར་རྗེན་པར་བཙོས་པ༌[^353]གང་ཡིན་པ་ནི་དེའོ་ཞེས་བྱ་བ་ནི་ནང་དུ་བཙོས་པ་དང་དགེ་སློང་གིས་བཙོས་པ༌[^354]དག་ལས་བྱིན་ལེན་བྱས་ནས་ཡང་བཙོ་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 594]
མི་སྙི་བ་རྣམས་ཀྱི་ནི་སུམ་ཆ་བངས་པ་ཉིད་ཀྱི་མདུན་རོལ་དུ་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་དེ་ཉིད་ཅེས་བྱ་བ་ནི་རྗེན་པ་ཉིད་དོ། །

[Block 595]
དེ་སྙི་བ་རྣམས་ཀྱི་ཞེས་བྱ་བ་ནི་འདིར་སྐམ་པོའི་ལོ་མ་དང་ཤ་དག་ལ་ཞུགས་པར་རིག་པར་བྱའོ། །

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
--- END BLOCKS ---
