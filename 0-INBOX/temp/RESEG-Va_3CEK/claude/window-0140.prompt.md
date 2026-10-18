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
[Block 4901]
འདི་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཀུན་དགའ་བོ་ཀུན་དུ་རྒྱུ་གནས་པ་དང་། རུས་མཐུན་པས་དྲི་བ་དྲིས་པ་དག་ཡོད་དོ་ཞེས་ལུང་བསྟན་ན་ནི་ཆོས་ཐམས་ཅད་བདག་མེད་པས་ཚིག་མ་ལེགས་པ་མ་ཡིན་ནམ། ཀུན་དགའ་བོ་ཀུན་དུ་རྒྱུ་གནས་པ་དང་རུས་མཐུན་པའི་དྲི་བ་དྲིས་པ་བདག་མེད་དོ་ཞེས་ལུང་བསྟན་ན་ནི་ཀུན་ཏུ་རྒྱུ་གནས་པ་དང་རུས་མཐུན་པའི་སྔ་ནས་ཀུན་དུ་རྨོངས་པ་ཡོད་པ་དག་གིས༌[^3463]བདག་སྔོན་ཡོད་པར་གྱུར་པ་ལས་ད་ནི་བདག་གི་དེ་ཡང་མེད་དོ་ཞེས་ཀུན་དུ་རྨོངས་པ༌[^3464]ཕྱིར་ཞིང་ཆེས་རྒྱས་པར་འགྱུར་བ་མ་ཡིན་ནམ། ཀུན་དགའ་བོ་བདག་ཡོད་ཅེས་བྱ་བ་ནི་རྟག་པའི་མཐར་འགྱུར་རོ། །

[Block 4902]
ཀུན་དགའ་བོ་བདག་མེད་ཅེས་བྱ་བ་ནི་ཆད་པའི་མཐར་འགྱུར་རོ་ཞེས་རྒྱས་པར་གསུངས་པ་གང་ཡིན་པ་འདི་ལས་ཀྱང་དེ་བཞིན་དུ་ངེས་པར་ཟུང༌[^3465]ཤིག །

[Block 4903]
འདིར་སྨྲས་པ།

[Block 4904 [VERSE]]
ལྟ་བའི༌[^3466]མཆེ་བས་སྨྲས་པ་དང་། །
ལས་རྣམས་འཇིག་པ་ལ༌[^3467]ལྟོས་ནས། །
སྟག་མོས་ཕྲུ་གུ་ཁྱེར་བ་ལྟར། །
རྒྱལ་བས་ཆོས་ནི་སྟོན་པར་མཛད། །

[Block 4905 [VERSE]]
བདག་ཡོད་ཉིད་དུ་ཁས་བླངས་ནས། །
ལྟ་བའི་མཆེ་བས་སྨས་པར༌[^3468]གྱུར། །
ཀུན་རྫོབ་རྟོག་པར་མ་གྱུར་ནས། །
དགེ་བ་ཕྲུ་གུ་ཉམས་བྱེད་འགྱུར། །

[Block 4906]
ཡང་སྨྲས་པ།

[Block 4907 [VERSE]]
མེད་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་སྲོག །
དེ་ཉིད་གཞན་དུ་མ་གསུངས་སོ། །
བརྟགས་པའང༌[^3469]མེད་དུ་འགྱུར་འོང་བས། །
མེད་དོ་ཞེས་ཀྱང་མ་གསུངས་སོ། །

[Block 4908]
ཕུང་པོའི་རྒྱུ་ནི་གང༌[^3470]ལ་དགེ །

[Block 4909 [VERSE]]
མི་དགེའི༌[^3471]འབྲས་བུ་ཡོད་པ་ཉིད། །
དེ་ལ་སྲོག་ཅེས་བྱ་སྟེ་དེ། །
སྲོག་མིང༌[^3472]བསྟན་པས་མེད་པར༌[^3473]འགྱུར། །
སྲོག་ཅེས་བྱ་བ་ཕུང་པོ་ལ། །

[Block 4910 [VERSE]]
བཏགས་ཙམ་ཞེས་ཀྱང་མ་གསུངས་ཏེ། །
དེ་ཚེའི་སྐྱེ་བོ་དེ་འདྲ་སྟེ། །
སྟོང་ཉིད་རྟོགས་པའི༌[^3474]སྐལ་ལྡན་མིན། །
འདི་ལྟར་གནས་པས་བདག་ཡོད་དམ། །

[Block 4911 [VERSE]]
མེད་ཅེས་དྲི་བ༌[^3475]འདྲི་བ་ཡི། །
བསམ་པ་ལ་ལྟོས་མ་གསུངས་ཏེ། །
ཡོད་ན་ཅི་ཕྱིར་ཡོད་མི་གསུངས། །

[Block 4912 [HEADING]]
#### འཇིག་རྟེན་རྟག་ཅེས་བྱ་བ་ལ་སོགས་པ་ལུང་མ་བསྟན་པ། ^6-2-12-0

[Block 4913]
འཇིག་རྟེན་རྟག་ཅེས་བྱ་བ་ལ་སོགས་པ་ཡང་འདྲི་བ་པོའི་བསམ་པ་ལ་ལྟོས་ནས་ལུང་མ་བསྟན་ཏེ། རེ་ཞིག་གལ་ཏེ་འཇིག་རྟེན་བདག་ཡིན་པར་འདོད་པར་གྱུར་ན་ནི་དེ་མེད་པའི་ཕྱིར་ལུང་མ༌[^3476]བསྟན་པ་རྣམ་པ་བཞི་ཆར་མི་རིགས་སོ། །

[Block 4914]
འོན་ཏེ་འཇིག་རྟེན་འཁོར་བ་ཐམས་ཅད་ཡིན་ནོ་ཞེ་ན་ནི་དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། འཇིག་རྟེན་རྟག་ན་འགའ་ཡང་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བར་མི་འགྱུར་རོ། །

[Block 4915]
མི་རྟག་ན་ནི་ཐམས་ཅད་ཆད་པར་འགྱུར་རོ། །

[Block 4916]
གཉི་ག་ལྟར་ཡིན་ན་ནི་ཁ་ཅིག་ནི་ངེས་པར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བར་འགྱུར་ལ་ཁ་ཅིག་ནི་མི་འགྱུར་རོ། །

[Block 4917]
གཉི་ག་ལྟར་མ་ཡིན་ན་ནི་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ཡང་མ་ཡིན། ཡོངས་སུ་མྱ་ངན་ལས་མི་འདའ་བ་ཡང་མ་ཡིན་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 4918]
དེའི་ཕྱིར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་ལམ་ལ་རག་ལུས་པའི་ཕྱིར་རྣམ་པ་བཞི་ཆར་ཡང་ངེས་པར་ལུང་མི་སྟོན་ཏེ། གཅེར་བུ་པའི༌[^3477]ཉན་ཐོས་ཀྱིས་བྱིའུ༌[^3478]བཟུང་བ་བཞིན་ནོ། །

[Block 4919]
དེ་ཉིད་ཀྱི་ཕྱིར་འཇིག་རྟེན་མཐའ་དང་ལྡན་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམ་པ་བཞི་ཡང་ལུང་མ་བསྟན་ཏེ། བཞི་ཚན་འདི་ནི་དོན་མཐུན་ནོ། །

[Block 4920]
འདི་ལྟར་ཀུན་དུ་རྒྱུ་སྨྲ་བྱེད་ཀྱིས་བཞི་ཚན་འདི་ཞུས་ནས་ཡང་ཅི་ལགས། འཇིག་རྟེན་ཐམས་ཅད་ལམ་འདི་ངེས་པར་འབྱུང་ངམ། འོན་ཏེ་འཇིག་རྟེན་ཕྱོགས་གཅིག་ལགས་ཞེས་ཞུས་པ་དང་། གནས་བརྟན་ཀུན་དགའ་བོས་སྨྲ་བྱེད་ཁྱོད་ཀྱིས་བཅོམ་ལྡན་འདས་ལ་དང་པོ་ཉིད་དུ་ཞུ་བ་ཞུས་པ་གང་ཡིན་པ་དེ་ཉིད་དེ་རྣམ་གྲངས་གཞན་གྱིས་འདྲི་འམ་ཞེས་སྨྲའོ། །

[Block 4921]
དེ་བཞིན་འོངས་པ་ཤི་ཕན་ཆད་ཡོད་དམ་ཞེས་བྱ་བ་བཞི་ཚན་འདི་ཡང་དྲི་བ༌[^3479]པོའི་བསམ་པ་ལ་ལྟོས་ནས་ལུང་མ་བསྟན་ཏེ། དེས་ནི་བདག་གྲོལ་བ་དེ་བཞིན་འོངས་པ་ཡིན་པར་བསམས་ནས་ཞུ་བ་ཞུས་སོ། །

[Block 4922 [HEADING]]
#### གང་ཟག་པ་རྣམས་ལ་བརྒལ་ཞིང་བརྟག་པ། ^6-2-13-0

[Block 4923]
གང་ཟག་པ་རྣམས་ལ་བརྒལ༌[^3480]ཞིང་བརྟག་པར་བྱ་སྟེ། བཅོམ་ལྡན་འདས་ཀྱིས་ཅིའི་ཕྱིར་གང་ཟག་གསོན་པོ་ནི་ཡོད་དོ་ཞེས་ལུང་སྟོན་ལ་ཤི་ཕན་ཆད་ནི་ལུང་མི་སྟོན། རྟག་པའི་ཉེས་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 4924]
འོ་ན་ནི་ཅིའི་ཕྱིར་བྱམས་པ་ཁྱོད་མ་འོངས་པའི་དུས་ན་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་སུ་འགྱུར་རོ་ཞེས༌[^3481]ལུང་སྟོན། ཅིའི་ཕྱིར་ཆེ་གེ་མོ་ཞིག༌[^3482]ཏུ་སྐྱེས་སོ་ཞེས་ཉན་ཐོས་འདས་པ་དུས་འདས་པ་སྐྱེ་བ་ལ་ལུང་སྟོན། དེ་ལྟ་ཡིན་ན་ནི་རྟག་པ་ཉིད་དུ་ཐལ་བར༌[^3483]འགྱུར་རོ། །

[Block 4925]
གལ་ཏེ་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་གང་ཟག་སྔར་གཟིགས་ལ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་ནས་ཀྱང་མི་གཟིགས་ཏེ། མི་མཁྱེན་པའི་ཕྱིར་ལུང་མི་སྟོན་ཏོ་ཞེ་ན་ནི། སྟོན་པའི་ཐམས་ཅད་མཁྱེན་པ་ཉིད་བསལ་བ་ཡིན་ནོ། །

[Block 4926]
ཡང་ན་ནི་དེ་མེད་དོ་ཞེས་ཁས་བླང་བར༌[^3484]བྱ་དགོས་སོ། །

[Block 4927]
འོན་ཏེ་གཟིགས་ན་ནི་མ་གསུངས་བཞིན་དུ་ཡང་དེ་ཡོད་པ་དང་རྟག་པ་ཞེས་བྱ་བར་གྲུབ་པ་ཡིན་ནོ། །

[Block 4928]
འོན་ཏེ་གཟིགས་སམ་མི་གཟིགས་ཞེས་བྱ་བ་འདི་ཡང་བརྗོད་པར་མི་བྱ་བ་ཡིན་ན།[^3485] དེ་ལྟ་ན་ནི་འོ་ན་བཅོམ་ལྡན་འདས་ཐམས་ཅད་མཁྱེན་པ་ཡིན་ནམ་མ་ཡིན་ཞེས་བྱ་བ་འདི་ཡང་རིམ་གྱིས་མི་བརྗོད་པར་གྱིས་ཤིག །གང་ཟག་ནི་ཡོད་པ་ཉིད་དེ། འདི་ལྟར་བདེན་པ་དང་། གནས་པར་བདག་གི་བདག་མེད་དོ་སྙམ་པ་ནི་ལྟ་བའི་གནས་སུ་གསུངས་སོ། །

[Block 4929]
ཡོད་དོ་སྙམ་པ་ཡང་ལྟ་བའི་གནས་སུ་གསུངས་ཏེ། དེ་ལྟ་བས་ན་འདི་ནི་ཁུངས་སུ་མི་རུང་ངོ་། །ཆོས་མངོན་པ་པ་རྣམས་ན་རེ་འདི་གཉི་ག་ཡང་མཐར་འཛིན་པ་ཡིན་ཏེ། རྟག་པ་དང་ཆད་པར་ལྟ་བས་བསྡུས་པ་དག་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 4930]
དེ་ཁོ་ན་བཞིན་དུ་རིགས་ཏེ་གནས་མ་བུའི༌[^3486]མདོ་ལས།

[Block 4931]
ཀུན་དགའ་བོ་བདག་ཡོད་ཅེས༌[^3487]བྱ་བ་ནི་རྟག་པར་འགྱུར་རོ། །

[Block 4932]
ཀུན་དགའ་བོ་བདག་མེད་ཅེས༌[^3488]བྱ་བ་ནི་ཆད་པར་འགྱུར་རོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4933 [HEADING]]
#### འཁོར་བ་འདི་སུའི་ཡིན་པ། ^6-2-14-0

[Block 4934]
གལ་ཏེ་ཡང༌[^3489]གང་ཟག་མེད་ན་འཁོར་བ་འདི་སུའི་ཡིན། འཁོར་བ་ཉིད་འཁོར་བར་རིག་པ༌[^3490]མ་ཡིན་ནོ། །

[Block 4935]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་སེམས་ཅན་མ་རིག་པའི༌[^3491]སྒྲིབ་པ་ཅན་ཀུན་དུ་རྒྱུ་བ༌[^3492]རྣམས་འཁོར་རོ་ཞེས་གསུངས་སོ། །

[Block 4936]
ཡང་གང་ཟག་ཇི་ལྟར་འཁོར་ཕུང་པོ་གཞན་འདོར་བ་དང་། ལེན་པའི་ཕྱིར་རོ། །

[Block 4937]
ཕྱོགས་འདི་ནི་ལན་བཏབ་ཟིན་ཏོ།[^3493] །ཇི་ལྟར་མེ༌[^3494]སྐད་ཅིག་མ་ཡིན་ཡང་རྒྱུན་གྱིས་དྲོ་བ༌[^3495]དེ་བཞིན་དུ་སྲེད་པ་ཉེ་བར་ལེན་པ་ཅན་སེམས་ཅན་ཞེས་བྱ་བ་ཕུང་པོའི་ཚོགས་འཁོར་རོ། །

[Block 4938 [HEADING]]
#### ང་ཉིད་དེའི་ཚེ་སྟོན་པར་གྱུར་ཏོ་ཞེས་གསུངས་པ། ^6-2-15-0

[Block 4939]
གལ་ཏེ་འདི་ཕུང་པོ་ཙམ༌[^3496]ཡིན་ན་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་ང་ཉིད༌[^3497]དེའི་ཚེ་དེའི༌[^3498]དུས་ན་མིག་བཟངས༌[^3499]ཞེས་བྱ་བའི་སྟོན་པར་གྱུར་ཏོ༌[^3500]ཞེས་གསུངས་སོ། །

[Block 4940]
ཅིའི་ཕྱིར་གསུང༌[^3501]བར༌[^3502]མི་འགྱུར། ཕུང་པོ་རྣམས་གཞན་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
