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
[Block 3676]
ཕྱུང་བ་ཐམས་ཅད་ལ་མཐའ་ཉིད་མ་གཏོགས་པ་ནི་དགེ་འདུན་ལྷག་མའོ་ཞེས་བྱ་བ་ནི་དཔེར་ན་སྤྱད་མི་བཟོད་པའི་བུད་མེད་དང་ལྷན་ཅིག་ཉམས་པར་བྱེད་པ་དང་། མགོ་བཅད་པའི་ཁ་ལ་སོགས་པ་དག་ཏུ་ཉམས་པར་བྱེད་པ་ནི་སྦོམ་པོར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཞུ་བ་ཁ་ཅིག་དང་གཞན་དག་ལས་ཁུ་བ་འབྱིན་པའི་རྣམ་པ་གསུངས་པ༌[^2420]དག་གམ། དེ་ཐམས་ཅད་ལ་ཐ་མ་ཉིད་མེད་པ༌[^2421]ལ་ཁུ་བ་འབྱིན་པའི་འདུན་པས་ཁུ་བ་འབྱིན་པ་ལ་ཕམ་པ་ཉིད་མ་ཡིན་པ་ཐམས་ཅད་དུ་ནི་ཁུ་བ་འབྱིན་པའི་དགེ་འདུན་ལྷག་མར་ཤེས་པར་བྱའོ། །

[Block 3677]
མདོ་འདི་ནི་སྔར་དེའི་ཆ་ནི་དེར་གཏོགས་སོ་ཞེས་བསྟན་པ་དེའི་སྤྲོས་པ་འདི་ཡིན་ནོ། །

[Block 3678]
འདིར་གང་དག་དགེ་འདུན་གྱི་ལྷག་མར་མི་འགྱུར་ཏེ། མི་ཚངས་པར་སྤྱོད་པའི་སྐབས་ཉིད་ཀྱི་ཕྱིར་འདི་སྙམ་དུ་སེམས་པ་དེའི་བསམ་པ་བཟློག་པའི་ཕྱིར་སྨོས་སོ། །

[Block 3679]
སྦྱོར་བ་གང་ལ་ལྟུང་བ་རྣམ་པར་མ་བཞག་པ་དེ་ལ་ན་སྨད་པའི་ལྟུང་བ་རྣམ་པར་གཞག་པ་ཡང་ཡོད་དེ། གང་དུ་རྣམ་པར་གཞག་པ་དེར་ལྟུང་བྱེད་དོ། །

[Block 3680]
མི་ཚངས་པར་སྤྱོད་པའི་བསམ་པས་བུད་མེད་ཀྱི་ཚོགས་ལ་རེག་པ་ལ་ནི་དགེ་འདུན་ལྷག་མ་ཡིན་ཏེ། སྦྱོར་བ་དེར་གཏོགས་པ༌[^2422]གང་ཞེ་ན། གང་ནས་བརྩམས་ཏེ་དེ་དང་འདྲ་བའི་ཁུ་བ་འབྱིན་པའི་མཐར་ཐུག་པ་ཉིད་དེ་ནས་བརྩམས་ཏེ། དགེ་འདུན་ལྷག་མར་འགྱུར་བ་དང་། སྦྱོར་བ་སྔ་མ་ནི་ཕམ་པར་འགྱུར་བའི་སྦྱོར་བ༌[^2423]ཞེས་བྱའོ། །

[Block 3681]
དེ་ལྟར་དེ་ལ་ཉེས་པ་སྦོམ་པོ་གཉིས་སུ་འགྱུར་ཏེ། ཕམ་པར་འགྱུར་བ་དང་དགེ་འདུན་ལྷག་མར་འགྱུར་བའི་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 3682]
འདིར་གཞུང་ཁ་ཅིག་ལས།

[Block 3683]
གཞི་ཐམས་ཅད་ལ་འདི་འབྱུང་བ༌[^2424]ཡིན་ཏེ། བུད་མེད་ཇི་ལྟ་བུ་དང་མི་ཚངས་པར་སྤྱོད་པར་བགྱིད་ན་མཐར་འགྱུར་ལགས། ཡན་ལག་ཐམས་ཅད་དང་དུ་བླང་དུ་རུང་བ་གང་ཡིན་པ་དང་ངོ་། །དེ་བཞིན་དུ་དུད་འགྲོའི༌[^2425]སྐྱེ་གནས་ལ་ཡང་བརྗོད་པར་བྱའོ། །

[Block 3684]
གལ་ཏེ་དང་དུ་བླང་དུ་མི་རུང་ན་དེ་དང་ལྷན་ཅིག་ཉམས་པར་བྱེད་པ་དེ་ལ༌[^2426]ཁུ་བ་འབྱུང་ན་ནི་དགེ་འདུན་ལྷག་མར་འགྱུར་རོ། །

[Block 3685]
གལ་ཏེ་ཁུ་བ་མ་ཕྱུང་ན་ནི་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 3686]
གཞུང་གཞན་ལས་ཀྱང་རེ་ཞིག་ཇི་ཙམ་གྱིས་ན་སྦུབས་ཉམས་པར་བརྗོད་པར་བགྱིད།[^2427] གང་གི་ཕྱིར་དེའི་རྨའི་ཐན་ཀོར་ཉམས་པར་འགྱུར་ན་སྟེ། དེ་ཉམས་པར་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 3687]
ཁུ་བ་འབྱིན་པ་ན་ནི་དགེ་འདུན་ལྷག་མར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3688]
བྱ་བ་དུ་མའི་འབྲས་བུས་ལྟུང་བ་རྣམ་པར་མི་གཞག་གོ་ཞེས་བྱ་བ་ནི་བྱ་བ་འབྲས་བུ་ཐ་དད་པས་བར་དུ་ཆོད་པའི་འབྲས་བུ་ཐ་དད་པ་གྲུབ་པ་དུ་མ་དག་གིས་འབྲས་བུ་གཅིག་ཏུ་བསྡུས་པས་དངོས་གཞིའི་ལྟུང་བ་རྣམ་པར་མི་གཞག་སྟེ། དེ་དག་གི༌[^2428]འབྲས་བུ་ནི་ཐ་དད་པ་ཉིད་ཡིན་ནོ། །

[Block 3689]
དཔེར་ན་ཉུང་ངུ་ཉུང་ངུར་བརྐུས་པ་གཅིག་ཏུ་བསྡོམས་པས་མ་ཤ་ཀ་ལྔ་ལ་སོགས་པའི་ཚད་དུ་ཆོག་པ་གང་ཡིན་པ་དེས་ཕམ་པར་མི་འགྱུར་བ་ལྟ་བུ་དང་། ཁང་པ་ཆུང་ངུ་མ་བཞི་བསྡོམས༌[^2429]ནས་ཚད་ལས་ལྷག་པར་གྱུར་པ་གང་ཡིན་པ་དེས་དགེ་འདུན་ལྷག་མར་མི་འགྱུར་བ་ལྟ་བུ་དང་། དེ་བཞིན་དུ་གོས་ཀྱི་དུམ་བུ་ཚད་དུ་མི༌[^2430]ཆོག་པ་དུ་མ་ཚང་བར་བཅངས༌[^2431]ཏེ། དུས་ལས་འདས་པར་སྒྲུབ་པ་རྣམས་ལ་སྤང་བའི་ལྟུང་བྱེད་དུ་མི་འགྱུར་བ་ལྟ་བུ་དང་། ཉུང་ངུ་ཉུང་ངུ་ནས་རྫོགས་པར་གྱུར་པའི་དོན་རྣམས་ལ་དེ་བཞིན་དུ་ལམ་ན་བལ་ཐོགས་པ་ཡང་ཉིན་རེ་ཞིང་ཅུང་ཟད༌[^2432]ཅུང་ཟད་དུ་ཁྱེར་བའི་ལམ་སྤྱིར་བསྡོམས༌[^2433]པས་རྒྱང་གྲགས་ལས་འདའ་བའོ། །

[Block 3690]
དུས་གཞན་དང༌[^2434]གཞན་དུ་ཚིག་རེ་རེ་སྨྲས་པའི་ཚིག་རྣམས་སྤྱིར་བསྡོམས་པས༌[^2435]ཚིག་ལྔ་འམ་དྲུག་ལས་འདས་པར་ཆོས་སྟོན་པ་ལྟུང་བྱེད་དུ་མི་འགྱུར་བ་ལྟ་བུའོ། །

[Block 3691]
འདིར་གཞུང་ནི་མ་བྱིན་པར་ལེན་པ་ལས།

[Block 3692]
བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་གིས༌[^2436]མ་ཤ་ཀ་ལྔ་བརྐུས་ནས་མཐར་འགྱུར་རོ་ཞེས་གསུངས་པ་དེ་ལ། བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་བརྐུས་པ་དེ་ལ༌[^2437]མ་ཤ་ཀ་བརྒྱ་འམ་སྟོང་སྙེད་བརྐུས་ཀྱང་མཐར་མི་འགྱུར་བ་མཆིས་སམ། ཡོད་དེ་མ་ཤ་ཀ་བ་ནི༌[^2438]བཞི་རྐུ་ཞིང་ནམ་ཡང་ལྔ་མ་ཡིན་ཏེ། སྦྱོར་བ་ལ་ནི་ཉེས་པ་སྦོམ་པོ་རེ་རེར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3693]
བྱེ་བྲག་མེད་པའི་ཕྱིར་ཐམས་ཅད་ཀྱི་དབང་དུ་ཉེ་བར་སྦྱར་རོ། །

[Block 3694]
ཕྱེད་བྱས་པ་ལ་བྱེད་པ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ལ་འདིར་ཕྱེད་བྱས་པ་ལ༌[^2439]ཞེས་བྱ་བའི་ཕྱེད་ཀྱི་སྒྲ་ནི་ཡན་ལག་གི་ཚིག་སྟེ། ལས་བརྩམས་པ་ཕྱེད་བྱས་པ་དེ་ལ་བྱེད་པ་ཞེས་བྱ་བ་ལ་ལྷག་མ་སྒྲུབ་པར་བྱེད་པ་དེ་ལ་ཕྱེད་ཉིད་དོ།[^2440] །དེ་ལས་དེའི་སྒྲུབ་པ་ཕྱེད་བྱས་པ་ཉིད་ཡིན་ནོ། །

[Block 3695]
བྱ་བ་མ་བརྩམས་པ་ལ་ཉེས་པ་གང་ཡིན་པ་དེའི་རྗེས་ལ་དེའི་ཚིག་ཅེས༌[^2441]བྱ་བ་འདི་ལ་དེ་སྒྲུབ་པར་བྱེད་པའོ། །

[Block 3696]
དཔེར་ན་གོས་རྙིངས་པ༌[^2442]ཅུང་ཟད་བཅགས་པ་ཞིག་དགེ་སློང་མ་ཉེ་དུ་མ་ཡིན་པ་ལ་འཆག་ཏུ་བཅོལ་ན་ཉེས་བྱས་སུ་འགྱུར་བ་ལྟ་བུ་དང་། ལུག་གི་བལ་ཅུང་ཟད་བཀྲུས་སམ་ཕྱེད་བཀྲུ་བར་བྱས་པ་དག་རྨེལ་དུ་བཅོལ་ན་ཉེས་བྱས་སུ་འགྱུར་བ་ལྟ་བུ་དང་། འཁྲུར་བཅོལ་ཏམ་འཚེད་དུ་བཅོལ་བ་འདི་གཉིས་ཀ་དང་། བཀྲུས་པ་དང་བཙོས་པ༌[^2443]གཉིས་ཀ་དག་ལ་རང་བཞིན་རྣམ་པར་འགྱུར་བ་སྲིན་བལ་རྙིང་པ་དང་ལུག་གི་བལ་རྙིང་པ་དང་། ལུག་གི་བལ་རྙིང་པ་ནག་པོ་ལས་བྱས་ན་ཉེས་བྱས་སུ་འགྱུར་བ་ལྟ་བུའོ། །

[Block 3697]
ཁ་ན་མ་ཐོ་བ་ན་སྨད་པ་དག་གིས་ཆ་ཉིད་ནི་ན་སྨད་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་ལྟ་བུའི་ཁ་ན་མ་ཐོ་བ་དག་གི་ཆ་ནི་ན་སྨད་པ་ཉིད་ཡིན་ཏེ། ན་སྨད་པའི་ཆར་གྱུར་པ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 3698]
དཔེར་ན་ཉེས་པ་སྦོམ་པོ་དང་། ལྟུང་བྱེད་དང་། སོ་སོར་བཤགས་པར་བྱ་བ་དང་ཉེས་བྱས་རྣམས་ཀྱིས་སྐུར་བ་བཏབ་པ་ལས་ཉེས་བྱས་སུ་འགྱུར་བ་ལྟ་བུའོ། །

[Block 3699]
མཚམས་མེད་པ་གསུམ་པོ་ཕ་བསད་པ་དང་། མ་བསད་པ་དང་། དགྲ་བཅོམ་པ་བསད་པ་རྣམས་ཀྱིས་སྐུར་པ༌[^2444]འདེབས་པ་གང་ཡིན་པ་དེ་ལ་ནི་དགེ་འདུན་ལྷག་མར་འགྱུར་རོ། །

[Block 3700]
དགེ་འདུན་གྱི་དབྱེན་བྱེད་པ་དང་། དེ་བཞིན་གཤེགས་པ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་ཕྱུང་བའི་མཚམས་མེད་པ་གཉིས་པོ་དག་གིས་སྐུར་པ་འདེབས་པ་དེ༌[^2445]ལ་སྦོམ་པོའི་ལྟུང་བར་མི་འགྱུར་ཏེ། དེ་ལ་ནི་ཉེས་བྱས་ཉིད་ཡིན་ནོ། །

[Block 3701]
ཐམས་ཅད་ལ་ཐེ་ཚོམ་ཟ་བས་ཞུགས་པ་ནི་བསམ་པ་དང་བཅས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཐེ་ཚོམ་ཟ་བཞིན་དུ་འདི༌[^2446]ཡིན་ནམ་འོན་ཏེ་མ་ཡིན། འདི་བདག་གི་ཕ་ཡིན་ནམ་འོན་ཏེ་མ་ཡིན། འདི་དགྲ་བཅོམ་པ་ཡིན་ནམ་འོན་ཏེ་མ་ཡིན། འདི་དེ་ཡིན་ནམ་འོན་ཏེ་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པར་གཞི་ཐམས་ཅད་ལ་ཞུགས་པ་གང་ཡིན་པ་དེ་ནི་བསམ་པ་དང་བཅས་པས་གནས་པ་ཡིན་ནོ། །

[Block 3702]
གང་ཞིག་ཡང་དེའི་མདུན་དུ་སྟེ། ཐམས་ཅད་དུ་མ་ཡིན་ནོ། །

[Block 3703]
དེ་ལ་ཡང་དེའི་ཚེ་ན་གནས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3704]
བསམ་པ་དང་བཅས་པ་ནི་དགོས་པ༌[^2447]སྟེ་ངེས་པའི་བསམ་པའོ། །

[Block 3705]
ངེས་པར་འདི་ལ་དེར་ཡང་ཉེ་བར་མི་སྡུད་པ་ནི། གང་ཡང་དེ་ཡིན་ཡང་རུང་མ་ཡིན་ཡང་རུང་གིས་སྙམ་པའི་བསམ་པས་གནས་པ་སྟེ། དེ་འདི་ཡིན་ནམ་འོན་ཏེ་མ་ཡིན་སྙམ་ནས་གསོད་པ་ལ་ཇི་ལྟར་གསོད་པར་བྱེད་པ་ལ་ལྟུང་བྱེད་དོ། །

[Block 3706]
འདི་ནི་མི་ཁོ་ན་སྟེ། འདི་ནི་མི་མ་ཡིན་སྙམ་པས་གསོད་པ་ལ་ཕམ་པ་ཁོ་ན་ཡིན་ཏེ། འདི་ནི་མི་ཡིན་ཏེ་མི་མ་ཡིན་པ་མ་ཡིན་སྙམ་ནས། འདི་ནི་དགྲ་བཅོམ་པ་སྟེ། དགྲ་བཅོམ་པ་མ་ཡིན་པ་ནི་མ་ཡིན་ནོ་སྙམ་པས་མ་ལ་སོགས་པ་གསོད་པ་ལ་མཚམས་མེད་པའི་ལས་ཀྱང་ངོ་། །གང་ལ་བདག་ཆགས་པ་དེ་འདི་ཡིན་ནམ་འོན་ཏེ་མ་ཡིན། འདི་ནི་བུད་མེད་ཡིན་ནམ་འོན་ཏེ་མ་ཡིན་སྙམ་དུ་དངོས་པོ་ཇི་ལྟ་བར་འདུ་ཤེས་པར་མ་གྱུར་པའོ། །

[Block 3707]
སྦྱོར་བ་ལ་ནི་འདུ་ཤེས་ཡན་ལག་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་ལ༌[^2448]འདུ་ཤེས་ཡན་ལག་ཡིན་གྱི་དོན་ཉིད་མ་ཡིན་ཏེ། དཔེར་ན་དུད་འགྲོ་ནི་མིར་འདུ་ཤེས་པས་བསད་ན་དེའི༌[^2449]དོན་གྱི་སྦྱོར་བ་ལ་སྦོམ་པོ་ཉིད་དུ་འགྱུར་བ་དང་། མི་མ་ཡིན་པ་ལ་མིར་འདུ་ཤེས་པའི་ཕྱིར་དེ་ཉིད་ཀྱིས་བསད་ན་སྦྱོར་བ་སྦོམ་པོར་འགྱུར་བ་དང་། དེ་མ་བྱིན་པར་ལེན་པ་དང་། ཆོས་བླ་མ་དང་ལུས་ཀྱི་རེག་པ་ལ་སོགས་པ་དག་ལ་ཡང་དེ་བཞིན་དུ་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 3708]
བསམས་པ་ནི་དེ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ནམ་རྫས་ལ་བསམས་ཏེ། ཞུགས་པ་གང་ཡིན་པ་ལ་ནི་བསམས་པའི་དོན་གྱིས་རང་གི༌[^2450]ངོ་བོ་ཉིད་ཡན་ལག་དེ་ཉིད་དོ། །

[Block 3709]
གལ་ཏེ་དོན་དེ་ཉིད་ཡིན་ན་གང་ལ་བརྩམས་ཏེ། འཇུག༌[^2451]ཅིང་བསམས་ཏེ་ཞུགས་པའི་ཡན་ལག་དེ་ཉིད་ཡན་ལག་ཡིན་ནམ།[^2452] དེའི་ཚེ་དངོས་གཞིའི་ལྟུང་བ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 3710]
འདི་ལྟ་སྟེ་དཔེར་ན་གཉིས་འཁོད་པ་ལས་གཅིག་བསད་པར༌[^2453]བྱའོ་སྙམ་པ་ལས་ཅིག་ཤོས་བསད་པ་དང་། དགྲ་བཅོམ་པ་གསད་པར༌[^2454]བྱའོ་སྙམ་པ་ལས་དགྲ་བཅོམ་པ་མ་ཡིན་པ་བསད་པ་དང་། མ་ཞེས་བྱ་བ་ཕ་མ་གཉིས་དང་དགྲ་བཅོམ་པ་ལ་སོགས་པ་ཞེས་བྱ་བ་དགྲ་བཅོམ་པ་ལ་སོགས་པ་ལའོ། །

[Block 3711]
མི་གསད་པར༌[^2455]བྱའོ་སྙམ་པ་ལས༌[^2456]མི་མ་ཡིན་པ་བསད་པ་དང་། མི་མ་ཡིན་པ་གསད་པར༌[^2457]བྱའོ་སྙམ་པ་ལས་མི་བསད་པ་ལ་སོགས་པ་ནི་སྦྱོར་བའི་ལྟུང་བ་ཁོ་ན་ཡིན་གྱི་དངོས་གཞིར་མི་འགྱུར་རོ། །

[Block 3712]
དེ་བཞིན་དུ་དུད་འགྲོ་བསད་དོ་སྙམ་པ༌[^2458]ལས་མི་བསད་ན་ཡང་ཉེས་བྱས་སོ། །

[Block 3713]
རྩིག་པ་དང་།

[Block 3714]
ཀ་བ་དང་ཤིང་ལྗོན་པ་ལ་སོགས་པ་སེམས་མེད་པ་གཅད་དོ་སྙམ་པ་ལས།

[Block 3715]
མ་ལ་སོགས་པ་བསད་ན་ཡང་སྦྱོར་བའི་ཉེས་བྱས་སོ། །
--- END BLOCKS ---
