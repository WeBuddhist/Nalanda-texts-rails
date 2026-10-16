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
[Block 4411]
གཞན་དུ་ན་གཞུང་མི་བྱེད་དེ། སྡིག་པ་ཉིད་ཡིན་པས་སོ། །

[Block 4412]
ཇི་ལྟར་ཁས་བླང་བར་བྱ༌[^2840]ཞེས་བྱ་བ་ནི་ཁས་ལེན་པར་བྱེད་པའོ། །

[Block 4413]
སྡིག་པ་ལ་སྡིག་པ་མ་ཡིན་པའི་ལྟ་བས་གང་དེ་གྲགས་པ་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་སྡིག་པ་མི་བྱེད་དེ། ཇི་ལྟར་རིགས་པས་སྨྲ་བ་ཁས་ལེན་པར་བྱེད་ཅེས་པ་སྟེ། གྲགས་པ་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར། གཞུང་མི་བྱེད་ཅེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 4414]
གཞན་དུ་ན༌[^2841]བྱེད་པ་དེ་ནི་དོན་གྱིས་མི་འགྲུབ་པའོ། །

[Block 4415]
དེས་ན་དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། མི་ཡི་བདག་པོ་ལྟ་བ་བཟང་ངམ་ངན།[^2842] །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4416]
སྐལ་བ་མཉམ་པ་ནི་རིགས་མཐུན༌[^2843]པའོ། །

[Block 4417]
ལས་ཉིད་སྒྲུབ་པ་ཡིན་པས་ལས་ནི་སྒྲུབ་པའོ། །

[Block 4418]
རིགས་མཐུན་པའི་ལས་ཀྱིས༌[^2844]སྒྲུབ་པ་ནི་རིགས་མཐུན་ལས་ནི་སྒྲུབ་པའོ། །

[Block 4419]
དེ་དག་གི་རྒྱུ་ནི་རིགས་མཐུན་པའི་ལས་སྒྲུབ་པའི་རྒྱུའོ། །

[Block 4420]
གལ་ཏེ་ལྟ་བ་བཟང་ན་ནི་དགེ་བའི་ལས་སྒྲུབ་པའི་རྒྱུ་ཡིན་ལ། གལ་ཏེ་ལྟ་བ་ངན་ན་ནི་མི་དགེ་བའི་ལས་སྒྲུབ་པའི་རྒྱུ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། བརྟགས་ན་དགེ་བ་དང་། མི་དགེ་བའི་འཇུག་པའི་ཚིག་དང་སྤྱོད་པ་རྣམས༌[^2845]སྟོན་པའི་ཕྱིར་རོ། །

[Block 4421]
ལྟ་བ་དེ་ཡང་གང་ལས་ཐོབ་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ། དམ་པ་རྣམས་ལ་བརྟེན་ན་འདི་ཤེས་འགྱུར། །ཞེས་སྨོས་པ་ཡིན་ཏེ། འདི་ནི་ལྟ་བ་བཟང་པོའི་ཚུལ་ལོ། །

[Block 4422]
འདི་སྐྱེ་བོ་ངན་པ་རྣམས་རིང་དུ་སྤང་བ་ནི་ཐག་རིང་དུ་བྱ་བའོ། །

[Block 4423]
དམ་པ་མ་ཡིན་པ་ལ་བརྟེན་པས་ནི་ཚུལ་འདི་ལྟར་ཐོབ་པ་ཡིན་ཏེ། དེས་ན་དེ་ཉིད་སྨྲས་པ། མི་སྡོམ་པར་ཡང་སྡོམ་པའི་ཚུལ་འཛིན་པ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། མི་སྡོམ་པར་ཡང་ཞེས་བྱ་བ་ནི་སྡོམ་པའི་རྒྱུ་མེད་ཀྱང་མཐོང་བའི་ཡུལ་དུ་བྱེད་པའི་ཕྱིར། མི་སྡོམ་པར་ཡང་སྡོམ་པའི་ཚུལ་འཛིན་པ། །ཞེས་བྱའོ། སྡོམ་བརྩོན་དག་གི་ཆ་བྱད་ཡིན་པས་སྡོམ་པའི་ཚུལ་ལོ། །

[Block 4424]
དེ་འཆང་བའི་ཚུལ་གང་ལ་ཡོད་པ་དེ་ནི་སྡོམ་པའི་ཚུལ་འཛིན་པའོ། །

[Block 4425]
དགེ་སློང་སྲིན་པོ་དེ་རྣམས་ཀྱི་མཚན་ཉིད་ནི་ཅི༌[^2846]ཇི་ལྟར་ནི་དེ་དག་ཤེས་པར་བྱ་ཞེ་ན། དེ་སྨྲས་པ། རྒྱུ་མེད་སྨྲ༌[^2847]ལ་སོགས་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་སྨོས་ཏེ། སོགས་པའི་སྒྲས་ནི་དབང་ཕྱུག་རྒྱུར་སྨྲ་བ་དང་། ཐམས་ཅད་སྔོན་གྱི་ལས་ཀྱིས་བྱས་པར་སྨྲ་བ་དང་། ཆད་པར་སྨྲ་བ་དང་། རྒྱལ་པོའི་གཙུག་ལག༌[^2848]གི་གཞུང་སྨྲ་བ་རྣམས་ཀྱང་གཟུང་ངོ་། །དེ་དག་གི་ཁྱད་པར་གྱི་མཚན་ཉིད་ནི་ཇི་ལྟར་རྩུབ་པོས་བསྒོས་པ་ཞེས་བྱ་བ་ཅེ་སྤྱང༌[^2849]བཞིན་དུ་ཅེ་སྤྱང༌[^2850]གི་ཁྱད་པར་གྱི་མཚན་ཉིད་ཅན་དེས་ན་རླག་པར་བྱེད་པ་ཡིན་ཏེ། གང་གི་ཕྱིར། སྐྱེ་བོ་བྱིས་པ་དེ་རྣམས་དགེ་སློང་སྲིན་པོ་སའི་སྟེང་ན་རྒྱུ་བར༌[^2851]བྱེད་པས་སོ། །

[Block 4426]
དེའི་ཕྱིར་དོན་ནུས་པ་སྤྱད་ཅེས་བྱ་བ་ནི་དགོས་པའི་དོན་ཏོ། །

[Block 4427]
[^2852]དེའི་ལྟ་བ་ལས་བཟློག་པ་དེ་ནི་དོན་དུ་ནུས་པར་གྱུར་ནའོ། །

[Block 4428]
དེ་བས་མཁས་པས་དེ་དག་བསྟེན་མི་རིགས། །ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 4429]
དེ་ལྟར་ཡང་ཁྱད་པར་དུ་སྐྱེ་བོ་མི་མཐུན་པ་དག་གྲགས་པ་ཆེ་བར་གྱུར་ན་ཡང་མཛའ་བར་ནི་མི་བྱ་བ་ཉིད་དེ། ཁྱད་པར་ཀྱི་བྱ་བ་བསྟན་པའི་ཕྱིར། [^2853]སྐྱེ་བོ་མི་མཐུན་པ་དག་གྲགས་པ་ཆེར་གྱུར་ཀྱང་།[^2854] །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4430]
དགོས་པ་ཡོད་པར་གྱུར་ཀྱང་ཞེས་བྱ་བ་ནི་དགོས་པའི་དབང་གིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4431]
རྒྱུ་ལས་གྲུབ་པར་མཐོང༌[^2855]བཞིན་ལ། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་བདུན་གྱིས་ནི་ལྟ་བ་བཟང་ངན་བསྟན་པའི་ཕྱིར་ཏེ། དེ་ལས་གྲུབ་པར་མཐོང་བཞིན་ལ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་ལྟ་བ་བཟང་པོའི༌[^2856]ཕན་ཡོན་གྱི་དབང་དུ་བྱས་པ་སྟེ། སྔར་བཤད་པའི་ལྟ་བ་ངན་པ་རྣམ་པ་ལྔའི་མི་མཐུན་པའི་ཕྱོགས་བསྟན་པས་སྲོག་གཅོད་པ་ལ་སོགས་པ་བྱ་བ་མ་ཡིན་པ་མི་བྱེད་པའི་ཕན་ཡོན་ནོ། །

[Block 4432]
རྒྱུ་མེད་སྨྲ༌[^2857]དང་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི། ལྟ་བ་ངན་པའི༌[^2858]བྱ་བ་མ་ཡིན་པ་བྱེད་པའི་རྒྱུའི་ཉེས་དམིགས་བསྟན་པའི་དབང་དུ་བྱས་པ་སྟེ། གལ་ཏེ་བྱ་བ་མ་ཡིན་པ་མི་བྱེད་ཀྱང་གྲགས་པ་ཅུང་ཟད་ཀྱི་ཕྱིར་བྱེད་དོ། །

[Block 4433]
གཞན་དུ་ན་བྱ་བ་བྱེད་པ་ཉིད་སྣང་བའི་ཕྱིར་རོ། །

[Block 4434]
མི་ཡི་བདག་པོ་ལྟ་བ་བཟང་ངམ་ངན། །[^2859]ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་ལྟ་བ་བཟང་པོའམ་ངན་པ་ཡིན་ཏེ། དགེ་བ་དང་མི་དགེ་བའི་ལས་ཀྱི་རྒྱུ་ཉིད་རབ་ཏུ་སྒྲུབ་པའི་ཕྱིར་རོ། །

[Block 4435]
དེ་བས་ན་ལྟ་བ་བཟང་པོ་བསྟན་པའི༌[^2860]རིགས་ཞེས་བྱ་བའི་ཕྱེད་དང་པོས་ནི་སྔར་བསྟན་པའི་དོན་མཇུག༌[^2861]བསྡུ་བ་ཡིན་ནོ། །

[Block 4436]
ལྟ་བ་བཟང་པོ་དང་ངན་པ་གཉིས་སྤོང་བ༌[^2862]དང་བསྟེན་པར་བྱ་བ་བསྟན་པའི་ཕྱིར། སྐྱེ་བོ་ངན་པ་རིང་དུ་སྤོང་།[^2863] །ཞེས་བྱ་བ་ཕྱེད་འོག་མ་ཡིན་ཏེ། ལྟ་བ་བཟང་པོ་སྟེ་དམ་པ་ལ་བརྟེན་པས་ནི་དམ་པ་ཡོངས་སུ་ཤེས་པར་འགྱུར་བ་དེ་བསྟན་པ་ནི་དགེ་བའི་བཤེས་གཉེན་གང་ལ་བརྟེན་པའོ། །

[Block 4437]
གང་ཡོངས་སུ་སྤང་བ་ནི་མི༌[^2864]དགེ་བའི་བཤེས་གཉེན་ནི། མི་སྡོམ་པར་ཡང་སྡོམ་པའི་ཚུལ་འཛིན་པ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ཡིན་ཏེ། མི་དགེ་བའི་བཤེས་གཉེན་གང་ཡིན་པ་དེ་ཉིད་བསྟན་པའི་ཕྱིར། ས་ཡི་སྟེང་ན་དགེ་སློང་སྲིན་པོ་རྣམས། །ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4438]
རྒྱུ་མེད་སྨྲ་ལ་སོགས་པའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་མི་དགེ་བའི་བཤེས་གཉེན་དེའི་མཚན་ཉིད་བསྟན་པའི་དོན་ནོ། །

[Block 4439]
དེ་བས་མཁས་པས་ཞེས་བྱ་བ་འོག་མ་ཕྱེད་ཀྱིས་ནི་དེ་ལ་མི་དགེ་བ་མི་སྒྲུབ་པའི་ཁྱད་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4440]
མི་སྒྲུབ་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཡོངས་སུ་སྤང་བ་དང་། ལྟ་བ་ངན་པ་ལས་བཟློག་པའོ། །

[Block 4441]
སྐྱེ་བོ་མི༌[^2865]མཐུན་པ་དག་གྲགས་པ་ཆེར་གྱུར་ཀྱང་། །[^2866]ཞེས་བྱ་བ་སྨོས་པ་ལ། རྣམ་པ་ཐམས་ཅད་དུ་ཡང་བསྟེན་པར་བྱ་བ་མ་ཡིན་པའོ། །

[Block 4442]
དཔེ་བསྟན་པར་བྱ་བའི་ཕྱིར། དགུན་གྱི་དུས་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། རྣམ་པ་ཐམས་ཅད་དུ་སྐྱེ་བོ་མི་མཐུན་པ་དག་གྲགས་པ་ཐོབ་པར་གྱུར་ཀྱང་དེ་དང་མཛའ་བར་མི་བྱ་བ་ཡིན་ན་ནི༌[^2867]གཞན་དག་དེ་བཞིན་དུ་དགོས་པ་མེད་པར་གྱུར་པ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་པའོ། །

[Block 4443]
དེ་དཔེ་དང་བཅས་པའི་ཉེས་དམིགས་བསྟན་ནས། སྐྱེ་བོ་ཡོན་ཏན་སྤོང་བ་དེ་དག་སྤང་བ་དང་། ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་བཅུས་ནི་ཡང་དག་པར་འཛིན་དུ་གཞུག་པའི་དབང་དུ་བྱས་པ་སྟེ། གང་ལ་འཛིན་དུ་འཇུག་པར་བྱེད་ཅེ་ན། བདག་ཉིད་ཀྱི་ཕུན་སུམ་ཚོགས་པའི་རང་བཞིན་སྒྲུབ་པ༌[^2868]འཛིན་དུ་འཇུག་པར་བྱེད་དེ། དེ་ལ་བདག་གི་རང་བཞིན་ནི༌[^2869]སྐྱེ་བོ་ཡོན་ཏན་སྤོང་བ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་གསུམ་གྱིས་བསྟན་ཏེ། དེ་དག་ཅེས་བྱ་བ་ནི་ལྟ་བ་བཟང་པོ་ནི་དམ་པ་ལ་བརྟེན་པ་དང་།

[Block 4444]
དམ་པ་མ་ཡིན་པ་ཡུན་རིང་དུ་སྤངས་པ་ལས།

[Block 4445]
འཐོབ་པའི་ཕྱིར་དམ་པ༌[^2870]དང་དམ་པ་མ་ཡིན་པ༌[^2871]བསྟེན་པ་དང་། སྤང་བ་གཉིས་ཀྱིས་ལྟ་བ་བཟང་ངན་ཡོངས་སུ་མ་བསྐྱངས་པའི་ཕྱིར། སྨན་རྣམས་ཀུན་དང་འབྲལ་བར་འགྱུར་རོ། །

[Block 4446]
ཞིང་རྨེད་པ་ནི་དཔྱ་དབུལ་བའི་རྩ་བའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4447]
དེ་དག་ལ་ཚོང་ཟོང་སྣ་ཚོགས་ཞེས་བྱ་བ་འདི་སྨོས་ཏེ། མཁར་དང་། ནོར་གྱི་རང་བཞིན་ལས་བརྩམས་པ་སྟེ། སྣ་ཚོགས་པའི་ཚོང་ཟོང་གང་ཡིན་པ་དེ་དག་གོ། །

[Block 4448]
དེ་དག་གི་ཉོ་བ་དང་། འཚོང་བ་ནི་ཉོ་ཚོང་ངོ་། །རྣམ་པ་སྣ་ཚོགས་པའི་ཉོ་ཚོང་བྱེད་པ་ནི་ཚོང་ཟོང་སྣ་ཚོགས་ཉོ་ཚོང༌[^2872]བྱེད་པ་སྟེ། །དེ་ནི་ཚོང་པ་རྣམས་ཡིན་ཏེ། ཡུལ་གཞན་དང་། ཆུ་དང་། ཐང་དང་།

[Block 4449 [VERSE]]
ལེན་དུ་འགྲོ་བའི་དབང་དུ་བྱས་པའོ། །
ཕོ་བྲང་འཁོར་གྱི་མི་ཞེས་བྱ་བ་ནི།
གྲོང་ན་གནས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 4450]
ཤོ་གམ་གཅོད་ཅིང་དཔྱ་དབུལ་བ་ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཤོ་གམ་གཅོད་ཅིང་དཔྱ་དབུལ་བའི་ཐ་མལ་པའི་གྲོང་གི་མི་སྟེ། འདིས་ནི་རྫོང་གི་རང་བཞིན་བསྟན་ཏོ། །
--- END BLOCKS ---
