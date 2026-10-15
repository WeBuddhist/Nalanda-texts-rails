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
[Block 3606]
དམག་གི་ནང་ན་གནས་པ་ལ་ཉེས་པ་དང་ལྡན་པ་ཉིད་དོ། །

[Block 3607]
དེ་བས་ན་ཉིན་མོ་ཡང་འདིར་གནས་པར་སྦྱོར་བ་ལ་ཞུགས་པའོ། །

[Block 3608]
དེའི་དང་པོ་ནི་སྐྱ་རེངས༌[^2474]

[Block 3609]
དང་པོ་དེའིའོ༌[^2475]ཞེས་བྱ་བ་ལ༌[^2476]ཉིན་མཚན་དེའི་དང་པོ་ནི་སྐྱ་རེངས༌[^2477]

[Block 3610]
དང་པོ་གང་ཡིན་པ་དེ༌[^2478]ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3611]
ཞག་ནི་ཉིན་མཚན་གྱི་དང་པོ་སྟེ། ངེས་པར་འབྱུང་བར་འགྱུར་བ༌[^2479]ངོ་བོ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3612]
ཉིན་མོ་དང་མཚན་མོ་ལ་སྣང་བ་ནི་ཞག་གི་ངོ་བོའོ། །

[Block 3613]
སྐྱ་རེངས༌[^2480]

[Block 3614]
དང་པོ་ལ་སོགས་པ་ཡང་ཉིན་མོ་ལ་སོགས་པའི་སྣང་བ་ལ་དང་པོ་ཞེས་བྱ་བ་འདི་ལྟར་མདོ་བྱས་པའོ། །

[Block 3615]
ལས་ལ་ནི་འདས་ན་ཉི་མ་ཤར་བའི་འོ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་དང་དགག་དབྱེ་དང་། དེ་གཉིས་ལ་ལྷག་པར་གནས་པ་དང་། དབྱར་ཁས་བླངས་པ་དང་སྲ་བརྐྱང་འདིང་བའི༌[^2481]སྒོ་རྣམས་ལ་ཚེས་ཀྱི་ཁྱད་པར་དང་འབྲེལ་བའི་ལས་རྣམས་ལ་དུས་འདའ་བར་ཡོད་པར་གྱུར་པ་ལ་ཉི་མ་འབྱུང་བའི་དང་པོ་ནི་ཉིན་མོ་དང་མཚན་མོ་སྐྱ་རེངས༌[^2482]ཤར་བའི་བར་དུ་འདའ་བར་བྱེད་པ་ལ་དུས་ཀྱི་བྱ་བ་ཉིད་ཅེས་བྱ་བའོ། །

[Block 3616]
དོན་འདྲི་བ་ལ་འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 3617]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་སྐྱ་རེངས༌[^2483]ཤར་བ་དང་བདག་ཅག་གིས་གསོ་སྦྱོང་མ་བྱས་སོ་སྙམ་དུ་དྲན་པ་སླར་རྙེད་པར་གྱུར་ནས། དེ་དག་དེའི་ཚེ་ན་གསོ་སྦྱོང༌[^2484]བགྱིད་ཅིང་སོ་སོར་ཐར་པ་འདོན་པར་བགྱིད་ན་དགེ་འདུན་གྱིས་གསོ་སྦྱོང་བགྱིས་པ་དང་སོ་སོར་ཐར་པ་བཏོན་པ་ཞེས་བགྱི་འམ། ཉེ་བ་འཁོར་དགེ་སློང་དེ་རྣམས་ཀྱིས་གསོ་སྦྱོང་བྱས་པ་དང༌[^2485]སོ་སོར་ཐར་པ་བཏོན་ཞེས༌[^2486]བྱ་བ་ནི་འདྲ་བ་ཉིད་ཀྱི་ཕྱིར་དགག་དབྱེ་ལས་འདི་ཤེས་པའོ། །

[Block 3618]
སྤང་བ་ལ་ནི་འདུ་ཤེས་ལས་གཙོ་ཆེར་རང་གི་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དངོས་པོ་ལས་ཇི་ལྟར་མ་བྱིན་པར་ལེན་པ་དང་། ཤི་བའི་ཡོ་བྱད་གཉིས་ནི་ཉེ་བར་དགོས་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་ནི་རང་ཉིད་མ་ཡིན་པ་ཤེས་པར་བྱེད་པའི་བདག་པོ་ལ་ཡང་སྐྱེ་བ་ཉིད་བདག་ཏུ་བྱ་བ་འདི་ལ་ཡང་དག་པར་ཤེས་པ་ཉིད་དེ་དེ་བཞིན་དུ་སྤང་བའི་ལྟུང་བྱེད་ལ༌[^2487]ཡང་ཤེས་པར༌[^2488]གྱུར་པ་ཡོད་དུ་ཟིན་ན་དངོས་གཞི་སྐྱེས་པ་སྟེ་མ༌[^2489]ཤེས་པར་གྱུར་པ་ལ་ནི་གཙོ་ཆེར་རང་ཉིད་ཀྱི་འདུ་ཤེས་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 3619]
དོན་ཇི་ལྟ་བ་ཉིད་ན༌[^2490]དངོས་གཞི་སྟེ་དོན་ཇི་ལྟ་བ༌[^2491]མ་ཡིན་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3620]
རང་གི་མ་ཡིན་པ་ལ་རང་གི་བློ་ཡོད་པ་ལ་ཉེས་བྱས་བསྐྱེད་པ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 3621]
རང་གི་ཡིན་པ་ལ་ནི་དངོས་གཞི་སྟེ། རང་གི་མ་ཡིན་པ་ལ་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་འདི་འདུ་ཤེས་པ་བཞིན་དུ་སོམ་ཉི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3622]
འདིར་གཞུང་ནི་ཀོ་ལྤགས་ཀྱི་གཞི་ལས་དགེ་སློང་གིས་དགེ་སློང་ལ་ཆོས་གོས་དག་བསྐུར་ཞིང་འདི་ནས་བཏང་ལ་དེར་མ་བྱིན་པ་དག་ལ་ནི་གང་ལ༌[^2492]ཡང་སྤང་བར་མི་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3623]
མ་ཐོབ་པ་གང་ལ་བཏང་བ་དེ་ལ་ནི་སྤང་བའི་ལྟུང་བྱེད་མི་བསྐྱེད་པར༌[^2493]བསྟན་པ་ནི་འདུ་ཤེས་པར་མི་འགྱུར་བ་ཉིད་ཀྱི་ཕྱིར་འདིར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3624]
དེ་ནི་བསྔོས་པ་ཉིད་ན་བྲལ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གཞན་ལ་བྲལ་བ་ཉིད་འདི་ལ་སྤང་བའི་ལྟུང་བྱེད་མ་བྱས་པའི་ཕྱིར་རང་ཉིད་ལ་གང་དུ་བསྔོས་པ་ཉིད་དེས་འདུ་ཤེས་པ་ཉིད་ལ་ཡང་སྟོང༌[^2494]པ་ཉིད་ལ་རྣམ་པར་མ་བརྟགས་སུ་ཟིན་ཀྱང་སུ་ཞིག་ལ་ཞེས་བྱ་བ་བྱེ་བྲག་ཡོངས་སུ་མ་བཟུང་བར་ཤེས་པར་བྱའོ། །

[Block 3625]
གང་ཞིག་འདི་ནི་ཀོ་ལྤགས་ཀྱི་གཞི་ལས་གང་གིས་བཏང་བ་དེར་སྤང་བའི་ལྟུང་བྱེད་མི་བསྐྱེད་པར་བརྗོད་པའོ། །

[Block 3626]
འདིར་ལུང་ནི་འོ་ན་འདི་ཤི་བའི་ཡོ་བྱད་ལ་ཇི་ལྟར་འདིར་དངོས་པོ་ལས་རང་ཉིད་རྣམ་པར་གཞག་གི་འདུ་ཤེས་ལས་མ་ཡིན་ནོ། །

[Block 3627]
རབ་ཏུ་བྱུང་བའི་དོན་དུ་ངེས་པར་བྱ་བ་ཡང་དེ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དངོས་པོ་ཉིད་ཅེས་བྱ་བའི་དོན་ལ་ལྟུང་བ་མེད་དོ། །

[Block 3628]
རབ་ཏུ་བྱུང་བ་ལ་ལྟོས་པའི་དོན་དུ་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་འཛིན་པར་བྱེད་ཅེས་བྱ་བ་གང་ཞིག་ཙམ་ལ་བརྗོད་པ་དེ་ལའང་བཤད་པའོ། །

[Block 3629]
ཆོས་གོས་ལས་ཀྱང་རྣམ་པར་བརྟགས་ནའོ་ཞེས་བྱ་བ་ནི་མ་བླངས་པ་ཉིད་ལ་རྣམ་པར་བརྟགས་པ་ལས་ཆོས་གོས་ལས་ཀྱང་རང་གི་ཉིད་དང་འབྲལ་བ་སྟོན་ཏོ། །

[Block 3630]
འདི་ལ་རྗེས་སུ་ཞུགས་པ་ཉིད་ཀྱང་ཉམས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རང་ཉིད་ཀྱིས༌[^2495]རྗེས་སུ་འཇུག་པ་ཉིད་གང་ཡིན་པ་དེ་ལ་འདིར་མ་བླངས་པ་ཉིད་ལ་སོགས་པས་བྲལ་བ་ཉིད་ལ་ཉམས་པ་ཉིད་དོ། །

[Block 3631]
རང་བཞིན་ལས་ཉམས་ན་ཡང་ངོ་ཞེས་བྱ་བའི༌[^2496]སྒྲ་ནི་རྗེས་སུ་ཞུགས་པ་ཉིད་ཉམས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་རྗེས་སུ་སྙེགས༌[^2497]པའི་ཕྱིར་རོ། །

[Block 3632]
འདིར་གཞུང་ནི་ཉེ་བ་འཁོར་གྱིས་ཞུས་པ་ལས་བཙུན་པ་དགེ་སློང་གིས་ཆོས་གོས་རྙེད་ནས་དགུང་ལྔ་ལགས་ལས༌[^2498]སེམས་རྣམ་པར་འཁྲུགས་པར་གྱུར་ནས་དེའི་དགུང་བཅུ་པོ་སླད་མ་གང་ཚུན་ཆད་ནས་བགྲང་བར་བགྱི། ཉེ་བ་འཁོར་གང་ཚུན་ཆད་ནས་རང་གི་སེམས་ཕྱིར་རྙེད་པ་ནས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3633]
རང་གི་སེམས་སོ་སོར་རྙེད་པ་ནས་བརྩམས་ཏེ་འདིར་བགྲང་བའི་ཚིག་གང་ཡིན་པས་ཞག་ལྔ་པོ་ཡང་འདའ་བར་བྱེད་པ་ལ་ཉེ་བར་བསྡུ་བའོ། །

[Block 3634]
འདིར་ནི་འདི་ལ་བསྟན་པའོ། །

[Block 3635]
དེ་ཡོད་ན་དངོས་པོ་དེ་ལྟ་བུ་གཞན་ལ་ཡང་འབྱུང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་ཞུགས་པ་ཉིད་དེ་ཡོད་ཅིང་གཞན་དུ་དེའི་དངོས་པོ་དང་གང་གི༌[^2499]རྣམ་པའི་དངོས་པོ་ལ་དེ་དང་རྗེས་སུ་འཇུག་པ་ཉིད་དོ། །

[Block 3636]
ཡོད་པའི་རྣམ་པའི་དངོས་པོ་ལ་ཆོས་གོས་ཞག་བཅུ་པར་གཏོགས་པ་ནི་ཞག་བཅུ་པའི་ཆོས་གོས་ལ་འབྱུང་བ་ཉིད་དོ། །

[Block 3637]
ཟླ་བ་གཅིག་པར་གཏོགས་པ༌[^2500]ནི་ཟླ་བ་གཅིག་པ་ལའོ། །

[Block 3638]
[^2501]སྨན་ཞག་བདུན་པར་གཏོགས་པ༌[^2502]ནི་སྨན་ཞག་བདུན་པ་ལ་འབྱུང་བ་ཉིད་ཙམ་ལ་སྐྱེས་པ་ཉིད་དོ། །

[Block 3639]
གང་གི་ཕྱིར་ཕྱིས་འབྱུང་བ་རྣམས་ལ་དང་པོའི་དུས་འདའ་བ་ཉིད་ནི་སྤང་བའི་ལྟུང་བྱེད་བརྗོད་པའོ། །

[Block 3640]
དེ་ཉིད་ལ་ཞག་བཅུའི་ནང་རོལ་དུ་སྟེ་དེ་བས་ན་སྐྱོན་མེད་དོ། །

[Block 3641]
འདིར་ལུང་ནི་སྦྱོར་བ་ནི་ཡོངས་སུ་དག་པ་ཉིད་དེ། འདིར་རྒྱུན༌[^2503]ལ་དེར་འཛིན་པ་མ་ཡིན་ནོ། །

[Block 3642]
སྦྱོར་བ་དེས་དེ་དང་འབྲེལ་བའི་རྫས་ཀྱི་ཁྱད་པར་བུམ་པ་དང་སྣམ་བུ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 3643]
ཞག་བདུན་པ་ལ་ནི་རིགས་མཐུན་པ་ལའོ་ཞེས་བྱ་བ་ནི་རྫས་ཀྱི་རིགས་འདྲ་བ་ལ་ཞག་བདུན་པའི་དོན་དུ་ལྷག་པར་གནས་པ་ལ་རྗེས་སུ་འཇུག་པ་ཉིད་ཡོད་པ་འདི་ལ་སྐྱེས་པ་ཉིད་དོ། །

[Block 3644]
འདིར་རྣམ་པར་འབྱེད་པའི་གཞུང་འགའ་ཞིག་ལས་མར་དང་འབྲེལ་བ་ནི་མར་ལའོ། །

[Block 3645]
འབྲུ་མར་དང་འབྲེལ་པ་ནི་འབྲུ་མར་ལའོ། །
--- END BLOCKS ---
