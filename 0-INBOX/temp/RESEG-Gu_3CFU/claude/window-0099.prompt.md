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
[Block 3466]
མཚན་མི་མཐུན་པ་ལ་སྐུར་བ་འདེབས་པ་དང་ལྟ་བ་མི་མཐུན་པ་ལ་སྐུར་བ་འདེབས་པ་ལའང་དགེ་འདུན་ལྷག་མའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3467]
འདིར༌[^2396]ཞུ་བ་ལས་མཚན་དང་ལྟ་བ་ཡན་ལག་མ་ཡིན་པ་ཉིད་ལ་གཞུང་ནི་དགེ་སློང་གིས་དགེ་སློང་མ་ལ་གཞི་མེད་པའི་ཕམ་པར་འགྱུར་བའི་ཆོས་ཀྱིས་སྐུར་བ་འདེབས་ན་དགེ་འདུན་ལྷག་མའོ། །

[Block 3468]
དེ་བཞིན་དུ་དགེ་སློང་མས་དགེ་སློང་ལ་གཞི་མེད་པའི་ཕམ་པར་འགྱུར་བའི་ཆོས་ཀྱིས་སྐུར་པ་འདེབས་ན་དགེ་འདུན་ལྷག་མའོ་ཞེས་གསུངས་སོ། །

[Block 3469]
ཉམས་པ་ལ་སྐུར་བ་འདེབས་པ་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་རྫོགས་པ་ཞེས་བྱ་བ་ལས་ན་ཁས་ལེན་པ་དང་མི་ལེན་པ་ཉིད་ཀྱི་ཐ་དད་པ་ལ་འདྲ་བའི་ཁ་ན་མ་ཐོ་བ་འདིར་རྣམ་པར་གཞག་གོ། །

[Block 3470]
ཤིན་ཏུ་སླར་ཁྲོས་པའི་འཇུག་པ་འདི་ཤིན་ཏུ་ཡང་སྒོར་གྱུར་པ་དགེ་སྦྱོང་གི་རིགས་ལ་སྐུར་པ་འདེབས་པ་ཞེས་བྱ་བ་དང་། ཉམས་པ་དང་མཚན་ཐ་དད་པའི་ཡུལ་ལ་ཡང་ལྟུང་བ་མཚུངས་པ་ཉིད་དུ་འདི་ལ་རྣམ་པར་གཞག་པའོ། །

[Block 3471]
བརྫུན་དུ་སྨྲ་བའོ༌[^2397]ཞེས་བྱ་བ་ནི་གཞི་མེད་པ་ཞེས་བྱ་བའི་ཚིག་གིས་མ་ཡིན་ནོ། །

[Block 3472]
མ་གྲགས་པའི་ཤེས་པས་ཉེ་བར་དམིགས་པར་བྱ་བ་གོ་བར་བྱེད་པ་ལ་ཡིད་མ་ཆེས་པའི་ཐོས་པས་བདག་གིས་ཐོས་སོ། །

[Block 3473]
བདག་ནི་ཡིད་ཆེས་པས་མ་ཡིན་ཞེས་བྱ་བ་འདི་ལྟར་དགེ་འདུན་ལྷག་མ་སྐྱེད་པར༌[^2398]གྱུར་ཏམ་ཞེས་བྱ་བའོ། །

[Block 3474]
གང་ཡང་རུང་བ་ལ་གོ་བར་བྱས་ནའོ་ཞེས་བྱ་བ་ནི་མིའི་འགྲོ་བ་ཐམས་ཅད་ལ་གླེང་བ་འབའ་ཞིག་གིས་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3475]
སྐུར་བ་འདེབས་པ་ལ་ཁ་ན་མ་ཐོ་བ་འདིའོ། །

[Block 3476]
གཞན་ལ་སྨྲ་བ་ནི་སྐུར་པ་འདེབས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 3477]
ལྟུང་བའི་ཕྲེང་བ་ལ་ཡང་བདག་གིས་མཐོང་ངོ་ཞེས་བྱ་བ་སྲིད་པ་ཙམ་ལ་འབྱུང་བ་སྟེ། ཁྱོད་ནི་བདག་གིས་མཐོང་ངོ་ཞེས་བྱ་བ་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་འདི་ཤེས་པའོ། །

[Block 3478]
གང་ལ་ལྟུང་བ་ཉིད་ལ་སྐྱོན་ཞེས་བྱ་བ་མ་བསྟན་པ་མེད་པ་རྒོད་བག་གི་བློས་དེ་ལ་འདི་བདག་གིས༌[^2399]བྱེད་ཅིང་མཐོང་ངོ༌[^2400]ཞེས་བྱ་བ་འཇུག་པའོ། །

[Block 3479]
གང་ལ་འདིར་སྐྱོན་གཞན་ཡིན་གྱི༌[^2401]ཕམ་པ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་བློ་སྒྲུབ་པ་གཞན་ལ་དེས་ཉམས་པ་ལ་འཇུག་པ་སྟེ། འཕོ་བར་གྱུར་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3480]
འདིར་གང་ལ་སྐྱོན་ཡོད་པ་ཞེས་བྱ་བ་འདི་ཙམ་གྱི་བློ་འདི་ནི་འདི་མ༌[^2402]ཡིན༌[^2403]ཞེས་བྱ་བ་དེ་ལ་ཡང་རྣམ་པ་གཞན་ཉིད་དེ་ཉམས་པར་གྱུར་པ་ནི་མ་ཡིན་ནོ། །

[Block 3481]
དེ་བས་ན་འདིར་བསམ་པ་གང་ཡང་རུང་བ་དེས་ཅི་ཞིག་བྱ་ཞེས་བྱ་བ་སུ་ཞིག་ལ་གོ་བར་བྱས་ན་དེ་བས་ན་ལྟོས་པ་དེར་བརྗོད་པར་བྱའོ། །

[Block 3482]
ཉམས་པར་འདུན་པས་སོ་ཞེས་བྱ་བ་ནི་ཁྲོས་པར་མ་གྱུར་ཅིག་ཅེས་བྱ་བ་བྱུང་རྒྱལ་གྱིས་སྨྲས་པས་བརྡ་བྱས་པ་ལ་ཕམ་པ་འདི་ཞེས་བྱ་བ་བརྫུན་དུ་སྨྲས་པ་ལས་འཕོ་བར་འཇུག་པའི༌[^2404]འདུན་པ་མེད་པའོ། །

[Block 3483]
ཉམས་པ་ཉིད་དུ་སྲིད་པ་དང་འབྲེལ་པ་འདི་ཡིན་ཏེ། ཉམས་པ་ཉིད་ལས་གཞན་ནི་འདིར་ཉམས་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 3484]
དེ་བས་ན་འདི་ལྟ་བུའི་འདུན་པས་བརྫུན་པར་གཞན་ལ་གོ་བར་བྱེད་པ་གང་ཡིན་པ་དེ་ལ་འདིར་ལྷག་མའི་ལྟུང་བྱེད་དོ། །

[Block 3485]
ཉམས་པར་མ་གྱུར་པའི་བརྗོད་པ་རྣམས་གང་ཡིན་པ་དེ་རྣམས་ལ་ནི་གང་དུ་དགེ་འདུན་གྱི་ལྷག་མའི་བློ་ཡོད་པ་དེ་ལ་ལྟུང་བྱེད་དོ། །

[Block 3486]
གཞན་ལ་ནི་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 3487]
གང་དུ་དོགས་པ་འཇུག་པ་འདི་ཕམ་པ་ཞེས་བྱ་བར་མ་གྱུར་ཏམ་སྙམ་དུ་ཡིད་གཉིས་སུ་གྱུར་པས་དེ་ལ་བསྐྱེད་པའོ། །

[Block 3488]
དེ༌[^2405]གཞི་གཞན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་གིས༌[^2406]སྨྲ་བ་དེ་འདིར་ནི་ཞེས་བྱ་བར་བརྗོད་དོ། །

[Block 3489]
གཞི་དེ་ལས་གཞི་གཞན་གང་ཡིན་པ་དེ་ལ་ནི་འདིར་གཞི་མ་ཡིན་ནོ། །

[Block 3490]
འདི་ལྟ་སྟེ་དཔེར་ན་མཐོང་བས་སྨྲ་བ་ཡོད་པར་གྱུར་པ་ལ་མཐོང་བ་དེ་ལས་གཞན་དོགས་པའི་གཞི་མ༌[^2407]ཐོས་པ་གང་ཡིན་པ་དེ་ནི་མཐོང་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3491]
གཞི་གཞན་ཡོད་པར་གྱུར་ཀྱང་གང་གིས་སྨྲ་བ་དེ་མེད་པ་ལ་འདིར་དགེ་འདུན་གྱི་ལྷག་མ་ཡོད་པར་གྱུར་ཏེ་ཞེས་བྱ་བ་འདི་ལ་བྱེད་དུ་འཇུག་པའི་ཚིག་གིས་སྟོན་པའོ། །

[Block 3492]
གལ་ཏེ་གཞི་གཞན་གང་ཡིན་པ་དེ་ཉིད་དེའི་གཞིར་འགྱུར་ན། གཞི་གཞན་ཡོད་པས་ཀྱང་གཞི་གང་གིས་གླེང་བའི་གཞི་དེས་དགེ་འདུན་ལྷག་མ་ཡོད་པར་མི་འགྱུར་ཏེ། འདི་ནི་ཡོད་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3493]
འདིར་གཞུང་ནི་ཐོས་པ་ལ་ཡིད་ཆེས་ནས་སྨྲས་པ། བདག་གིས་མཐོང་ངོ་ཞེས་ཡིད་ཆེས་པར་བྱེད་པ་དང་། ཐོས་པ་ལ་ཡིད་མ༌[^2408]ཆེས་པས་སྨྲས་པ། བདག་གིས་མཐོང་ངོ་ཞེས་སྨྲས་པ་དང་ཐོས་པ་ལ་དོགས༌[^2409]ཏེ། མཐོང་བར་བརྗོད་པ་དང་། མི་དོགས་ཏེ་མཐོང་བར་བརྗོད་པ་དང་། དོགས་པར་གྱུར་པས་སྨྲས་པ། བདག་གིས་མཐོང་ངོ་ཞེས་སྨྲ་ན་བརྗོད་དོ་ཅོག་དགེ་འདུན་ལྷག་མའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3494]
བརྗོད་པ་ནི་ཡོད་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མི་འདྲ་བ་ནི་མེད་པ་ཉིད་དུ་བལྟ་བར་བྱ་སྟེ། གང་ཞིག་མི་དྲན་པས་བརྗེད་པ་ལ་ནི་ཉེས་པས་འདིར༌[^2410]བརྗོད་པའོ། །

[Block 3495]
འདིར་གཞུང་ནི་འདིས་མཐོང་བར་གྱུར་པ་བརྗེད་བཞིན་དུ་དང་། འདིས་ཐོས་པར་གྱུར་ཏེ། དེ་ཡང་བརྗེད་བཞིན་དུ་དང་། འདིས་དོགས་པར་གྱུར་ཏེ་དེ་ཡང་བརྗེད་བཞིན་དུ་དེས་འདུ་ཤེས་བསྒྱུར་བ་དང་བཅས་པས་ཇི་སྲིད་དུ་མཐོང་ངོ་། །དེ་ཡང་མི་བརྗེད་པ་དང་སྨྲས་པ་ཐོས་ཏེ་འདི་ཡང་མ་བརྗེད་པ་དང་དོགས་སོ་ཞེས་དེ་ཡང་མ་བརྗེད་པའོ་ཞེས་ཟེར་ན། བརྗོད་དོ་ཅོག༌[^2411]ལ་དགེ་འདུན་ལྷག་མའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3496]
དོན་གྱི་དེ་ཉིད་ནི་མི་བརྫུན་པར་སྨྲ་བ་ཉིད་ཀྱི་རྒྱུ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་པ་ལ་ཇི་ལྟར་སྨྲ་བ་དེ་ཉིད་མེད་པ་ནི་འདིར་རྒྱུ་ཡིན་ཏེ་དོན་ལ་མ་ཡིན་ནོ། །

[Block 3497]
དེ་ཉིད་ཡོད་ཀྱང་དོན་ལ་བསམས་པ་ཉིད་ནི་འདུ་ཤེས་པ་ཉིད་སྨྲ་བ་ལ་བརྫུན་དུ་སྨྲ་བ་ཉིད་དོ། །

[Block 3498]
མ་བསམས་པར་འདུ་ཤེས་པ་མེད་པར་གྱུར་པ་ལ་སྨྲ་བ་ལ་བདེན་པ་ཉིད་དོ། །

[Block 3499]
གཞི་གཞན་གྱིས་མི་དྲན་པས་བརྗོད་པ་ལ་དགེ་འདུན་གྱི་ལྷག་མ་ཞེས་བྱ་བའོ།

[Block 3500]
[^2412] །འདི་དང་འདི་བརྗོད་པ་ལ་ལྟུང་བའི་རྒྱུར་བརྗོད་པ་ནི་མ་དག་པས་སྐུར་བ་བཏབ་པ་ལ་དགེ་འདུན་གྱི་ལྷག་མར་བརྗོད་པས་བསྡུས་པའོ། །

[Block 3501]
ཞེ་སྡང་བས་མ་གཏོགས་ཞེས་བྱ་བ་འདི་དང་འོག་ཏུ་བརྗོད་པ་དེའི་ཡན་ལག་ཉིད་ནི་མ་ཡིན་ཏེ། སྐུར་བ་འདེབས་པ་ལ་འདིར་སྐྱོན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3502]
བརྗོད་པ་ཡོད་པར་གྱུར་ཅིག་ཅེས་བྱ་བ་ཡང་ཀུན་ནས་རྒོལ་བའམ་རྣམ་པ་གཞན་གྱིས་སྐུར་བ་འདེབས་པ་དང་། སྐུར་བ་འདེབས་པ་ཉིད་ཀྱིས་ཅི་སྟེ་འཇུག་པའི་རྒྱུ་རྗེས་སུ་འགྲོ་བ་ཙམ་འདི་དཔེ་ཉིད་ཀྱིས༌[^2413]ཕལ་ཆེ་བ་ཉིད་ལ་བརྟེན་ནས་ཕལ་ཆེར་སྐུར་བ་འདེབས་པ་འཇུག་པ་ལ་ཞེ་སྡང་གི་རྒྱུ་སྐྱེས་པའི་དབང་གིས་འདིར་གསུངས་པ་ཡིན་གྱི་ཡན་ལག་ཉིད་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 3503]
གཞི་མེད་པའི་དགེ་འདུན་ལྷག་མའོ།། །།

[Block 3504]
ད༌[^2414]ནི་གཞན་གྱི་ཆ་དང་མཐུན་པའི་དགེ་འདུན་ལྷག་མ་ལ་འདི་ཉིད་ཆོ་ག་མ་ལུས་པ་ཁས་བླངས་ནས་བརྫུན་དུ་སྨྲ་བས་སོ་ཞེས་སྨོས་པའི་གནས་སུ་འདི་འཐོབ་པས་དེའི་བྱེ་བྲག་འགའ་ཞིག་འདིར་བརྗོད་པར་བྱ་སྟེ། བརྗོད་པར་བྱ་བ་གཞན་ལ་གནས་པའི་ཚིག་གིས་བརྫུན་ནའོ་ཞེས་བྱ་བ་འདི་ཕམ་པར་འགྱུར་བའི་ལས་འདིས་ལྷག་པར་སྤྱོད་པ་ཞེས་བྱ་བ་བརྗོད་པར་བྱ་བ་འདིས༌[^2415]ལས་གཞན་དུ་དེའི་ཡན་ལག་ཏུ་གྱུར་པའི་རྣམ་པར་བྲལ་བ་བརྗོད་པར་བྱ་བ་ལ་གནས་པ་གང་ལ་ཡོད་པ་དེ་ནི་བརྗོད་པར་བྱ་བ་གཞན་ལ་གནས་པའི་ཚིག་གོ། །

[Block 3505]
འདི་ལྟ་སྟེ་དཔེར་ན་ཁོ་བོ་ཅག་གིས་ཚེ་དང་ལྡན་པ་གྱད་བུ་ནོར་མཐོང་ངོ་། །དགེ་སློང་མ་ཨུཏྤ་ལའི་མདོག་ཅན་མཐོང་ངོ་། །མི་ཚངས་པར་སྤྱོད་པ་འཁྲིག་པའི་ཆོས་བསྟེན་པ༌[^2416]མཐོང་ངོ་ཞེས་གང་གི་ཕྱིར་སྒྲ་དེ་གསུམ་གཅིག་ལ་གཅིག་སྦྱར་བ་དེ་བཞིན་དུ་འདི་རྣམས་ཀྱིས་བརྗོད་པར་བྱ་བའི་དོན་རྣམ་པར་བྲལ་བ་དེའི་ཆར་གྱུར་པའི་ཕམ་པའི་ལས་འདིས་ལྷག་པར་སྤྱོད་པ་དེ་བས་ན་དེ་ལྟར་དེའི་ཆ་དང་རྣམ་པར་བྲལ་བ་སོ་སོར་གྱུར་པ་འདིས༌[^2417]ཞེས་བྱ་བ་བྱས་ནས་སོ། །
--- END BLOCKS ---
