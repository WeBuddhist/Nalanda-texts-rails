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
ཤིང་ལྗོན་པ་དང་རྫིང་བུ་དང་འཆག་ས་དག་དང་ངོ་ཞེས་བྱ་བ་ཡང་ལྡན་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཤིང་ལྗོན་པ་དང་ལྡན་པ་དང་རྫིང་བུ་དང་ལྡན་པ་དང་འཆག་ས་དང་ལྡན་པའི་གཞིར་གཙུག་ལག་ཁང་རབ་ཏུ་གནས་པར་བྱའོ། །

[Block 3607]
ཉེན་ཀོར༌[^3687]དང་ངོ་ཞེས་བྱ་བ་ནི་ཉེན་ཀོར༌[^3688]དང་ལྡན་པའི་གཙུག་ལག་ཁང་རབ་ཏུ་གནས་པར་བྱའོ། །

[Block 3608]
རྒྱུན་ལུགས་དང་ཀླག་ཅོར་དང་སྒྲ་དང་ཏུག༌[^3689]རིང་ཆུང་བར་རོ་ཞེས་བྱ་བ་ནི་རྒྱུན་ལུགས་ཉུང་བ་དང་ཀླག་ཅོར་ཆུང་བ་དང་སྒྲ་ཆུང་བ་དང་ཏུག༌[^3690]རིང་ཆུང་བར་གཙུག་ལག་ཁང་རབ་ཏུ་གནས་པར་བྱའོ། །

[Block 3609]
བྲམ་ཟེའི་ཀློག་པ་དང་འདུན་སའི་ཐ་སྙད་དང་གླང་པོ་ཆེ་དང་རྟ་ལ་སོགས་པའི་སྒྲ་ནི་སྒྲའོ། །

[Block 3610]
རྫ་རྔ་ལ་སོགས་པའི་སྒྲ་ནི་ཏུག༌[^3691]རིང་སྟེ་དེ་དག་ཆུང་བར་བྱའོ། །

[Block 3611]
སྦྱིན་པ་པོས་རྗེས་སུ་གནང་ན་གཙུག་ལག་ཁང་བྱ་བའི་དངོས་པོ་ལས༌[^3692]དེ་བྱ་བའི་སྤྱད་བྱའོ་ཞེས་བྱ་བ་ནི་སྦྱིན་བདག་གིས༌[^3693]རྗེས་སུ་གནང་ན་གཙུག་ལག་ཁང་བྱ་བའི་རྫས་གང་ཡིན་པ་དེ་ལ༌[^3694]ལག་གི་བླས་བྱ་བའི་སྤྱད༌[^3695]བྱ་བ་ལ་མི་རིགས་པ་མེད་པའོ། །

[Block 3612]
འདིར་གཞུང་ནི་གལ་ཏེ་ཁྱིམ་བདག་གིས་རྗེས་སུ་སྟེར་ན་དེ་ཉིད་ལས་སྤྱད་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3613]
དེ་གཞག་པའི་ཁང་པ་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་ལག་གི༌[^3696]བླས་བྱ་བའི་སྤྱད་དེ་གཞག་པའི་ཁང་པ་སྦྱིན་པར་བྱ་བ་དེ་དམིགས་ཀྱིས་བསལ་བའོ། །

[Block 3614]
དེ་ཞེས་བྱ་བ་ནི་སྤྱད་དེའོ།[^3697] །དེར་དགོས་པའི་འབྲུ་མར་ལ་སོགས་པ༌[^3698]ཚོད་རན་པར་ཉོའོ་ཞེས་བྱ་བ་ནི་འདིར་དེར་གྱི་སྒྲས་ནི་ལག་གི༌[^3699]བླས་ལས་བྱ་བ༌[^3700]དེ་བསྡུས་པའོ། །

[Block 3615]
ལག་གི༌[^3701]བླས་སྤྱི་བུངས་ཇི་འདྲ་བ་དེ་འདྲ་བར་བཟའོ༌[^3702]ཞེས་བྱ་བ་ནི་གང་དུ་དེ་འོས་པ་ཉིད་དེ་ལ་བསྡུས་པ་དེ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3616]
གང་དུ་དེའི་འོས་པ་ཉིད་ནི་གང་ཞིག་གཙུག་ལག་ཁང་ན་གནས་པ་དེ་ལས་སར་པ་བྱེད་དུ་འཇུག་པ་དེའི་གཙུག་ལག་ཁང་ལའོ། །

[Block 3617]
གནས་དེའི་གཙུག་ལག་ཁང་མེད་པ་ཉིད་ཡིན་ན་ཉེ༌[^3703]འཁོར་གྱི་གཙུག་ལག་ཁང་གིའོ་ཞེས་བྱ་བ་ནི་ཇི་ཙམ་པ་དེ་ཙམ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3618]
སྣུམ་བག་གི་རྙེད་པ་མནོད༌[^3704]དོ་ཞེས་བྱ་བ་ནི་འདིར༌[^3705]བྱ་ན་ཡང་དགེ་སློང་གི་ཐང་བཞིན་དུ་མནོད་པའོ༌[^3706]ཞེས་བྱ་བར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3619]
འདིར་དེ་འདྲ་བར་ཞེས་བྱ་བར༌[^3707]སྦྱར་བར་བྱའོ། །

[Block 3620]
གཙུག་ལག་ཁང་དག་གི༌[^3708]བརྩེགས་མ་ཉིད་ཀྱི་མཐའ་ནི་ལྔའོ།[^3709] །དགེ་སློང་མ་རྣམས་ཀྱི་ནི་གསུམ་མོ་ཞེས་བྱ་བ་ནི་མཐའོ། །

[Block 3621]
འདིར་གཞུང་ནི་སིལ༌[^3710]བུ་དག་ལས་དགེ་སློང་རྣམས་ཀྱི༌[^3711]གཙུག་ལག་ཁང་ནི་ལྔ་བརྩེགས་སུ་བྱའོ། །

[Block 3622]
དྲི་གཙང་ཁང་ནི་བདུན་བརྩེགས་སུ་བྱའོ། །

[Block 3623]
སྒོ་ཁང་གི་སྟེང་གི་བསིལ་ཁང་ཡང་བདུན་བརྩེགས་སོ། །

[Block 3624]
དགེ་སློང་མ་རྣམས་ཀྱི་གཙུག་ལག་ཁང་ནི་སུམ་བརྩེགས་སུ་བྱའོ། །

[Block 3625]
དྲི་གཙང་ཁང་ནི་ལྔ་བརྩེགས་སུ་སོ།[^3712] །སྒོ་ཁང་ནི༌[^3713]སྟེང་གི་བསིལ་ཁང་ཡང་ལྔ་བརྩེགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ༌[^3714]ཡིན་ནོ། །

[Block 3626]
དྲི་གཙང་ཁང་དང་སྒོ་ཁང༌[^3715]སྟེང་གི་བསིལ་ཁང་དག་ནི་བརྩེགས་མ་གཉིས་ཀྱིས་ལྷག་པར་བྱའོ། །

[Block 3627]
དེ་དག་ལྕི་བས་འཇིག་པ་ཉིད་ཡིན་ན་བརྩེགས་མ༌[^3716]བཤིག་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་དོ་ཞེས་བྱ་བ་ལ། དེ་དག་ཅེས་བྱ་བ་ནི་དགེ་སློང་དང་དགེ་སློང་མའི་གཙུག་ལག་ཁང་དེ་དག་ལྕི་བས་འཇིག་པ་ཉིད་ཡིན་ན། བརྩེགས་པ་བཤིགས་པ་ལ༌[^3717]ཁ་ན་མ་ཐོ་བ་མེད་པ་ཉིད་ཡིན་ཏེ། བརྩེགས་མ་ཇི་སྙེད་བཤིག་པ་གཅིག་གམ་དུ་མ་དེ་སྙེད་བཤིག་པར་བྱའོ། །

[Block 3628]
བདུན་སྟོབས་ཉིད་ཀྱིས་སེལ་བ་ཞེས་བྱ་བ་དང་ཁ་ན་མ་ཐོ་བ་མེད་པ་ཉིད་ཅེས༌[^3718]བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པ་སྟེ་གཙུག་ལག་ཁང་གིས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3629]
བརྩམས་པ་སྐྱེད་པའམ༌[^3719]བསྐྱུང་བར་བྱ་བའི་ཕྱིར་བཤིག་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་། ཁ་ན་མ་ཐོ་བ་མེད་དོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདིར་གཞུང་ནི་གལ་ཏེ་བྱེད་དུ་འཇུག་མི་ནུས་ན་བཤིག་སྟེ་ཆུང་ངུར་བྱེད་དུ་གཞུག༌[^3720]སྟེ་འདི་ལ་འགྱོད་པ་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3630]
མཆོད་རྟེན་དང་སྐུ་གཟུགས་དག་ནི་སྐྱེད་པ༌[^3721]ཉིད་ཀྱི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་བརྩམས་པ་བཤིག་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པ་སྟེ། དེ་གཉིས་བརྩམས་པ་བསྐྱུང་བའི་ཕྱིར་བཤིག་པ་ནི་ཁ་ན་མ་ཐོ་བར་འགྱུར་རོ། །

[Block 3631]
རྙིངས་པ་ཉིད་ཀྱི༌[^3722]ཕྱིར་ནི་ཟིན་ཀྱང་མཉམ་པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་ཀྱང་ངོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^3723]པའི་ཕྱིར་སྨོས་སོ། །

[Block 3632]
བརྩམས་པ་མ་ཟིན་པ་དེ་དག་སྐྱེད་པ༌[^3724]འབའ་ཞིག་གི༌[^3725]ཕྱིར་བཤིག་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པར་མ་ཟད་ཀྱི་སྔ་མ་དང་མཉམ་པར་བྱ་བའི༌[^3726]ཕྱིར་བཤིག་པ་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་མེད་པའོ། །

[Block 3633]
རྙིངས་པ་ལ༌[^3727]གང་ལ་ཕྱིར་བཅོས་པས་བསྐྱེད་པར་བྱ༌[^3728]མི་ནུས་པ་དེ་ལ་བསྙམས་པ༌[^3729]ལ་ཁ་ན་མ་ཐོ་བ་མེད་པ་འདི་གསུངས་པར་རིག་པར་བྱའོ། །

[Block 3634]
ཕྱོགས་གཅིག་ཕྱིར་བཅོས་པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་དང་སྐུ་གཟུགས་ཀྱི༌[^3730]ཕྱོགས་གཅིག་རྙིངས་པ་ཕྱིར་འཆོས་པར་བྱ་བའི་ཕྱིར་བཤིག་པ་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་མེད་པའོ། །

[Block 3635]
འདིར་གཞུང་ནི་མཆོད་རྟེན་དང་སྐུ་གཟུགས༌[^3731]དག་རྙིངས་པ་ན། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ཕྱིར་བཅོས་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3636]
མདོ་སྔ་མའི་གཞུང་ནི་སྐྱང་ནུལ་གྱི་སྐུ་གཟུགས་དག་རྙིངས་པར་གྱུར་པ་ན། དགེ་སློང་དག་འགྱོད་པས་ཕྱིར་འཆོས་པར་མི་བྱེད་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ལྷག་མ་འམ༌[^3732]མཉམ་པར་བྱའི་ཆུང་བ་ནི་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3637]
འདིར་མཆོད་རྟེན་དང་སྐུ་གཟུགས་དག་འདྲ་བ་ཉིད་དེ༌[^3733]གང་ཞིག་འདི་དག་གི་དེ་དག་ལས་དེ་ལྟ་བུའི་རིགས་ཅན་གྱི༌[^3734]ཚིག་དེ་ལས་གཞན་དུ་བརྗོད་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 3638]
དེ་ལྟ་བས་ན་འདི༌[^3735]གཉིས་ཀ་ལུང་གཉིས་ལས་ཤེས་པའོ། །

[Block 3639]
གདུགས་ལ་སོགས༌[^3736]བཅོས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རྙིངས་པ་ཕྱིར་བཅོས་པའི་ཕྱིར་མཆོད་རྟེན་དང་སྐུ་གཟུགས་དག་ལས་དབོག་པ༌[^3737]ལ་ཁ་ན་མ་ཐོ་བ་མེད་པའོ། །

[Block 3640]
སོགས་པ་ཞེས་བྱ་བའི་སྒྲས་ནི་ཆར་ཁབ་ལ་སོགས་པ་དག་ཀྱང་བསྡུའོ། །

[Block 3641]
གཞན་གདགས་པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རྙིངས་པ་ཕྱིར་བཅོས་པར་བྱ་བའི་ཕྱིར་འབོགས་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་སར་པ་གཞན་གདགས་པའི་ཕྱིར་འབོགས་པ་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་མེད་པའོ། །

[Block 3642]
དེའི་དོན་དུ་ཉེ་བར་མ་བཞག་པར་འགོག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་གདགས་པ་དེའི་དོན་དུ་གདུགས་ལ༌[^3738]སོགས་པ་ཉེ་བར་མ་བཞག༌[^3739]པར་སྔ་མ་དབོག༌[^3740]པར་མི་བྱའོ། །

[Block 3643]
འདིར་གཞུང་ནི་གཞན་དག་གིས༌[^3741]གདུགས་དག་ཕོག་པར་གྱུར་ནས་དེ་དག་རབ་ཏུ༌[^3742]དུས་བྱེད་པར་གྱུར་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཇི་སྲིད་དུ་གཞན་དག་ཉེ་བར་མ་བཞག་པ༌[^3743]དེ་སྲིད་དུ་དབོག་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3644]
སྐྱེས་པའི་རབས་ལ་སོགས་པའི་རི་མོ་དང་། སངས་རྒྱས་ཀྱི་བཀའི་ཡི་གེ་དག་ཀྱང་ཞེས་བྱ་བ་ནི་དེ་དག་ཀྱང་རྙིངས་པ་བཅོས་པའི་ཕྱིར་ཕྱིས་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པའོ། །ཅི་ཞིག་གི་ཕྱིར་ཕྱིས་པ་ལ་བྱ་ཞེ་ན། དེའི་ཕྱིར་བྱིད་པའི༌[^3744]བྱེ་བྲག་ཁོ་ན་བྱ་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱིད་པའི༌[^3745]བྱེ་བྲག་གང་ཡིན་པ་དེ་ཁོ་ན་བྲི་བའི་ཕྱིར་ཡིན་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 3645]
རྩོམ་པར་བྱེད་པས་མ་བྱས་ན༌[^3746]གཞན་གྱིས༌[^3747]ལྷག་མ་བྱའོ་ཞེས་བྱ་བ་ནི་གང་གིས་མཆོད་རྟེན་དང་གཙུག་ལག་ཁང་དག་རྩོམ་པར་བྱེད་པ་དེ༌[^3748]བརྩམས་ནས་མ༌[^3749]ཟིན་པར་མ་བྱས་ན་གཞན་གྱིས་དེའི་ལྷག་མ་བྱ་བ་ལ་མི་རིགས་པ༌[^3750]མེད་པའོ། །
--- END BLOCKS ---
