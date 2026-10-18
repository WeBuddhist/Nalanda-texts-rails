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
[Block 3641]
དགེ་བའི་ཕྱིར་གྱ་ནོམ་པའོ། །

[Block 3642]
ཡིད་བརྟན་པའི༌[^2546]མཆོག་ཡིན་པའི་ཕྱིར་ངེས་པར་འབྱུང་བའོ། །

[Block 3643]
ལམ་ངན་པའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་ལམ་མོ། །

[Block 3644]
རིགས་པ་མ་ཡིན་པའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་རིགས་པའོ། །

[Block 3645]
མྱ་ངན་ལས་འདས་པའི་གྲོང་དང་། མི་འགལ་བའི་དོན་གྱིས་སྒྲུབ་པའོ། །

[Block 3646]
སྲིད་པ་ཐམས་ཅད་ཀྱི་གཉེན་པོ་ཡིན་པའི་ཕྱིར་ངེས་པར་འབྱིན་པར་བྱེད་པའོ། །

[Block 3647]
ཇི་ལྟར་འདོད་པ་བརྗོད་པར་བྱ་སྟེ་སྐྱེ་བ་དང་འཇིག་པའི་ཆོས་ཅན་ཡིན་པའི་ཕྱིར་མི་རྟག་པའོ། །

[Block 3648]
མི་མཐུན་པར་གྱུར་པའི་ཕྱིར་སྡུག་བསྔལ་བའོ། །

[Block 3649]
བདག་དང་བྲལ་བའི་ཕྱིར་སྟོང་བའོ། །

[Block 3650]
བདག་ཉིད་ཀྱིས་བདག་མ་ཡིན་པའི་ཕྱིར་བདག་མེད་པའོ། །

[Block 3651]
རྒྱུ་དང་། ཀུན་འབྱུང་བ་དང་། རབ་ཏུ་སྐྱེ་བ་དང་། རྐྱེན་ཉིད་ནི་གང་མདོ་ལས་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ་འདི་དག་ནི་འདུན་པའི་རྩ་བ་ཅན། འདུན་པ་ལས་ཀུན་འབྱུང་བ། འདུན་པ་དང་འདྲ་བ། འདུན་པ་ལས་རབ་ཏུ་སྐྱེ་བ་དག་ཡིན་ནོ་ཞེས་གསུངས་པ་ཁོ་ན་ཡིན་ཏེ། རབ་ཏུ་སྐྱེ་བ་ཞེས་བྱ་བའི་སྒྲ་ཐ་མར་གདོན་པ་འབའ་ཞིག་ཏུ་ཟད་དོ། །

[Block 3652]
ཡང་འདི་དག་ལ་ཁྱད་པར་ཅི་ཡོད་ཅེ་ན། འདུན་པ་ནི་རྣམ་པ་བཞི་སྟེ། ངའོ་སྙམ་པ་ནི་བྱེ་བྲག་མེད་པར་ལུས་པ༌[^2547]འདུན་པ་ཡིན་ནོ། །

[Block 3653]
གྱུར་ཅིག་སྙམ་པ་ནི་བྱེ་བྲག་ཏུ་མེད་པར་ཡང་སྲིད་པ་ལ་འདུན་པ་ཡིན་ནོ། །

[Block 3654]
འདི་ལྟ་བུར་གྱུར་ཅིག་སྙམ་པ་ནི། བྱེ་བྲག་ཏུ་ཡང་སྲིད་པ་ལ་འདུན་པ་ཡིན་ནོ། །

[Block 3655]
བཞི་པ་ནི་ཉིང་མཚམས་སྦྱོར་བའི་འཆིང་བ་ལ་འདུན་པ་ཡིན་ནོ། །

[Block 3656]
ཡང་ན་ལས་མངོན་པར་འདུ་བྱེད་པ་ལ་འདུན་པ་ཡིན་ནོ། །

[Block 3657]
དེ་ལ་དང་པོ་ནི་སྡུག་བསྔལ་གྱི་དང་པོའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རྩ་བའི་རྒྱུ་ཡིན་ཏེ། འབྲས་བུའི་ས་བོན་བཞིན་ནོ། །

[Block 3658]
གཉིས་པ་ནི་ཀུན་འབྱུང་བ་ཡིན་ཏེ། དེས་དེ་ཡང་དག་པར་འགྲུབ་པའི་ཕྱིར། འབྲས་བུའི་མྱུ་གུ་ལ་སོགས་པ་སྐྱེ་བ་བཞིན་ནོ། །

[Block 3659]
གསུམ་པ་ནི་དེ་དང་འདྲ་བའི་སྡུག་བསྔལ་གྱི་རྐྱེན་ཡིན༌[^2548]ཏེ། འབྲས་བུའི་ཞིང་དང་ཆུ་དང་ལུད་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 3660]
ཞིང་ལ་སོགས་པའི་དབང་གིས་ནི་འབྲས་བུའི་དྲི་དང་རོ་དང་། ནུས་པ་དང་། སྨིན་པ་དང་མཐུ་དང་ལྡན༌[^2549]པར་འགྱུར་རོ། །

[Block 3661]
བཞི་པ་ནི་རབ་ཏུ་སྐྱེ་བ་སྟེ། དེ་ཁོ་ན་ལས༌[^2550]དེ་སྐྱེ་བའི་ཕྱིར་འབྲས་བུའི་ཐ་མ་མེ་ཏོག་བཞིན་ནོ། །

[Block 3662]
ཡང་ན་སྲེད་པ་རྣམ་པར་སྤྱད་པ་རྣམས་ཀྱི༌[^2551]འདུན་པ་བཞི་ནི་སྲེད་པའི་བྱེ་བྲག༌[^2552]རྣམས་ལས་ལྔ་ཚན་གཉིས་དང་། བཞི་ཚན་གཉིས་ཡིན་ཏེ། དགེ་སློང་དག་ངའོ་སྙམ་པ་ཡོད་ན་ང་འདི་ལྟ་བུའོ་སྙམ་པ་འབྱུང་བར་འགྱུར་ཞིང་། ང་ནི༌[^2553]འདི་འདྲའོ་སྙམ་པ་དང་། ང་དེ་ལྟ༌[^2554]མ་ཡིན་ནོ་སྙམ་པ་དང་། ང་བཟང་ངོ་སྙམ་པ་དང་། ང་ངན་ནོ་སྙམ་པ་འབྱུང་བར་འགྱུར་རོ། །

[Block 3663]
དེ་ལ་འབྱུང་བར་འགྱུར་བར་བྱའོ་སྙམ་པར༌[^2555]འགྱུར་ཞིང་། དེ་ལ་འབྱུང་བར་འགྱུར་བར་མི༌[^2556]བྱའོ་སྙམ་པ་དང་། འདི་ལྟ་བུར་འབྱུང་བར་འགྱུར་བར་བྱའོ་སྙམ་པ་དང་། འདི་འདྲ་བར་འབྱུང་བར་འགྱུར༌[^2557]བར་བྱའོ་སྙམ་པ་དང་། དེ་ལྟ་མ་ཡིན་པར་འབྱུང་བར་འགྱུར་བར་བྱའོ་སྙམ་པ་འབྱུང་བར་འགྱུར་རོ། །

[Block 3664]
དེ་ལ་གྱུར་ཅིག་སྙམ་པ་འབྱུང་བར་འགྱུར་ཞིང་། དེ་ལ་འདི་ལྟ་བུར་གྱུར་ཅིག་སྙམ་པ་དང་། དེ་འདྲ་བར་གྱུར་ཅིག་སྙམ་པ་དང་། དེ་ལྟ་མ་ཡིན་པར་གྱུར་ཅིག་སྙམ་པ་དང་། གྱུར་ཀྱང་ཅི་མ་རུང་སྙམ་པ་དང་། འདི་ལྟ་བུར་གྱུར་ཀྱང་ཅི་མ་རུང་སྙམ་པ་དང་། འདི༌[^2558]འདྲ་བར་གྱུར་ཀྱང་ཅི་མ་རུང་སྙམ་པ་དང་། དེ་ལྟ་མ་ཡིན་པར་གྱུར་ཀྱང་ཅི་མ་རུང་སྙམ་པ༌[^2559]འབྱུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3665]
འཇུག་པ་མེད་པའི་ཕྱིར་འགོག་པའོ། །

[Block 3666]
སྡུག་བསྔལ་མེད་པའི་ཕྱིར་ཞི་བ་སྟེ། དགེ་སློང་དག་དེ་ལྟར་ན་འདུ་བྱེད་རྣམས་ནི་སྡུག་བསྔལ་བའོ། །

[Block 3667]
མྱ་ངན་ལས་འདས་པ་ནི་ཞི་བའོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3668]
གོང་ན་མེད་པའི་ཕྱིར་གྱ་ནོམ་པའོ། །

[Block 3669]
ཡང་ཕྱིར་མི་ལྡོག་པའི་ཕྱིར་ངེས་པར་འབྱུང་བའོ། །

[Block 3670]
ལམ་ལྟ་བུར་གྱུར་པའི་ཕྱིར་ལམ་མོ། །

[Block 3671]
ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ༌[^2560]ཞུགས་པའི་ཕྱིར་རིགས་པའོ། །

[Block 3672]
སོ་སོར་ངེས་པའི་ཕྱིར་སྒྲུབ་པ་སྟེ། ཇི་སྐད་དུ་མཐོང་བ་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་འདི་ལམ༌[^2561]ཡིན་གྱི་གཞན་ནི་མེད་དོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 3673]
གཏན་དུ་ངེས་པར་འབྱུང་བར་བྱེད་པའི་ཕྱིར་ངེས་པར་འབྱིན་པའོ། །

[Block 3674]
ཡང་ན་རྟག་པ་དང་། བདེ་བ་དང་། བདག་གི་དང་། བདག་ཏུ་ལྟ་བ་སྤྱད་པ་རྣམས་ཀྱི་གཉེན་པོར་གོ་རིམས་བཞིན་དུ་མི་རྟག་པ་དང་། སྡུག་བསྔལ་བ་དང་། སྟོང་པ་དང་། བདག་མེད་པའི་རྣམ༌[^2562]པ་དག༌[^2563]ཡིན་ནོ། །

[Block 3675]
རྒྱུ་མེད་པ་དང་། རྒྱུ་གཅིག་པུ་དང་། འགྱུར་བ་དང་། བློ་སྔར་བཏང་བ་དང་། ལྟ་བ༌[^2564]སྤྱད་པ་རྣམས་ཀྱི་གཉེན་པོར་གོ་རིམས་བཞིན་དུ་རྒྱུ་དང་། ཀུན་འབྱུང་བ་དང་། རབ་ཏུ་སྐྱེ་བ་དང་། རྐྱེན་གྱི་རྣམ་པ་དག་ཡིན་ནོ།[^2565] །ཐར་པ་མེད་དོ་སྙམ་དུ་ལྟ་བ་སྤྱད་པ་རྣམས་ཀྱི་གཉེན་པོར་འགོག་པའི་རྣམ་པ་ཡིན་ནོ། །

[Block 3676]
སྡུག་བསྔལ་ལ་ཐར་པ་ཡིན་ནོ་སྙམ་དུ་ལྟ་བ་སྤྱད་པ་རྣམས་ཀྱི་གཉེན་པོར་ཞི་བའི་རྣམ་པ་ཡིན་ནོ། །

[Block 3677]
བསམ་གཏན་གྱི་བདེ་བ་གྱ་ནོམ་པ་ཡིན་པར་ལྟ་བ་སྤྱད་པ་རྣམས་ཀྱི་གཉེན་པོར་གྱ་ནོམ་པ་ཡིན་ནོ། །

[Block 3678]
ཡང་དང་ཡང་ཡོངས་སུ་ཉམས་པར་འགྱུར་བའི་སྒོ་ནས་ཐར་པ་ནི་གཏན་དུ་མ་ཡིན་ནོ་སྙམ་དུ་ལྟ་བ་སྤྱད་པ་རྣམས་ཀྱི་གཉེན་པོར་ངེས་པར་འབྱུང་བའི་རྣམ་པ་ཡིན་ནོ། །

[Block 3679]
ལམ་མེད་དོ་སྙམ་པ་དང་། ལམ་འདི་ཡིན་ནོ་སྙམ་པ་དང་། གཞན་ཡང་ལམ་ཡིན་ནོ་སྙམ་པ་དང་། ལམ་འདི་ཡང་ལྷག༌[^2566]གོ་སྙམ་དུ་ལྟ་བར༌[^2567]སྤྱད་པ་རྣམས་ཀྱི༌[^2568]གཉེན་པོར་གོ་རིམས་བཞིན་དུ་ལམ་དང་། རིགས་པ་དང་། སྒྲུབ་པ་དང་། ངེས་པར་འབྱིན་པའི་རྣམ་པ་དག་ཡིན་ནོ། །

[Block 3680 [HEADING]]
### རྣམ་པ་ཞེས་བྱ་བའི་ཆོས། ^4-6-0
--- END BLOCKS ---
