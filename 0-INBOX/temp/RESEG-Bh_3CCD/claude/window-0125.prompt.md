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
[Block 4376 [VERSE]]
ཇི་སྲིད་པ་ཡི༌[^2667]རྩེ་མོའི་བར། །
ཁམས་གསུམ་པ་རྣམས་འདི་དག་ནི། །
གང་ཞིག་ཐམས་ཅད་འདི་ལྟར་སྣང་། །
སེམས་ཉིད་ལས་ནི་ངེས་པར་བྱུང་། །

[Block 4377]
ཞེས་བཤད་པའི་ཕྱིར་རོ།[^2668] །

[Block 4378]
དེ་བཞིན་དུ་དབྱིག་གཉེན་གྱི་ཞལ་སྔ་ནས་ཀྱང་། །

[Block 4379 [VERSE]]
རྣམ་རིག་ཙམ་ནི་དོན་མེད་དེ། །
མེད་པའི་དོན་ནི་སྣང་བའི་ཕྱིར། །
ཇི་ལྟར་རབ་རིབ་ཅན་གྱིས་ནི། །
མེད་པའི་སྒྲ་ཟླ་སོགས་མཐོང་བཞིན། །

[Block 4380]
ཞེས་བཤད་དོ། །

[Block 4381]
དེ་ལྟར་རང་བཞིན་གྱིས་དག་པ་ཡང་གློ་བུར་གྱི་དྲི་མ་དང་ལྡན་པ་བཞིན་དུ་སྣང་སྟེ་མེ་ལོང་བཞིན་ནོ། །

[Block 4382]
དེའི་ངོ་བོ་ནི་ཉམས་པར་མི་འགྱུར་ཏེ། །མཚན་ཉིད་གསུམ་ཡོངས་སུ་དག་པས་དེའི་རང་བཞིན་རྣམ་པར་དཔྱད་པར་བྱའོ། །

[Block 4383]
འདི་ལྟ་སྟེ། ཀུན་བརྟགས་དང་གཞན་དབང་དང་ཡོངས་སུ་གྲུབ་པའོ། །

[Block 4384]
དེ་ལ་ཀུན་བརྟགས་ནི་ཕྱི་རོལ་གྱི་དོན་མེད་པ་ཡང་འདི་ཉིད་ཀྱིས་ཐ་སྙད་དུ་བྱ་བ་ཡིན་ཏེ། བུམ་པ་འདི་དང༌[^2669]སྣམ་བུ་འདི་ཞེས་པ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 4385]
གཞན་དབང་ནི་མེད་པ་དེ་ཉིད་གཟུང་བ་དང་འཛིན་པའི་ཚུལ་དུ་རྟོགས་པའོ། །

[Block 4386]
ཡོངས་སུ་གྲུབ་པ་ནི་གཟུང་བ་དང་འཛིན་པའི་ངོ་བོ་མེད་པས་འབའ་ཞིག་དྲི་མ་མེད་པ་མཐའ་ཡས་པ་ནམ་མཁའ་དང་འདྲ་བའི་ཡེ་ཤེས་མྱོང་བའོ། །

[Block 4387 [VERSE]]
གླང་པོ་ཞེས་དོན་དེ་རྣམ་པ། །
དེ་མེད་པ་ནི་མཁས་པ་ཡིས། །
ཀུན་བརྟགས༌[^2670]ལ་སོགས་རང་བཞིན་རྣམས། །
གྲངས་ནི་ཇི་བཞིན་ཤེས་པར་བྱ། །

[Block 4388]
ཞེས་འབྱུང་ངོ་། །

[Block 4389]
དེ་བཞིན་དུ།

[Block 4390 [VERSE]]
དང་པོ་ཡིས་ནི་མཚན་ཉིད་ཀྱིས། །
ངོ་བོ་མེད་པ་གཞན་དག་ཀྱང་། །
རང་ཉིད་དངོས་མེད་ཤེས་བྱ་བ། །
དེ་ཡི་ངོ་བོ་མེད་པར༌[^2671]བསྟན། །

[Block 4391 [VERSE]]
གང་ཕྱིར་ཆོས་རྣམས་དོན་དམ་པ། །
དེ་ཡང་དེ་བཞིན་ཉིད་ཡིན་ནོ། །
རྟག་ཏུ་དེ་བཞིན་ཡོད་པའི་ཕྱིར། །
དེ་ཉིད་རྣམ་རིག་ཙམ་ཉིད་དོ། །

[Block 4392]
ཞེས་འབྱུང་ངོ་། །མཚན་ཉིད་གསུམ་ཡོངས་སུ་བརྟགས་པས་སེམས་ཙམ་ཤེས་ནས་རྟག་པ་བདེ་བ་ཆོས་ཀྱི་སྐུའི་མཚན་ཉིད་རྣམ་པར་རིག་པ་ཙམ་དང་ཤེས་པ་དང་འདྲ་བ་རྣམ་པར་སྣང་བར་འགྱུར་རོ་ཞེས་བྱ་བས་ཐར་པ་དང་འཆིང་བའི་ཆ་དབྱེ་བའོ། །

[Block 4393 [VERSE]]
དེ་ནི་སེམས་མེད་མི་དམིགས་པ། །
འཇིག་རྟེན་ལས་འདས་ཡེ་ཤེས་ཏེ། །
གནས་ངན་ལན་གཉིས་སྤོང་བའི་ཕྱིར། །
དེ་ནི་གཞི་ནི་གནས་གྱུར་པའོ། །

[Block 4394 [VERSE]]
དེ་ཉིད་ཟག་པ་མེད་པའི་དབྱིངས། །
བསམ་གྱིས་མི་ཁྱབ་རྟག་པར་དགེ། །
བདེ་བ་རྣམ་པར་གྲོལ་བའི་སྐུ། །
ཐུབ་པ་ཆེན་པོའི་ཆོས་ཞེས་བྱ། །

[Block 4395]
ཞེས་འབྱུང་ངོ་། །འདིར་སྨྲས་པ། སེམས་ཙམ་ཞེས་བྱ་བ་དོན་དམ་པར་མེད་དེ། གང་གི་ཕྱིར་ཤེས་པས་ན་སེམས་སོ། །

[Block 4396]
རེ་ཞིག་ཁྱོད་ཉིད་ཀྱིས་ཕྱི་རོལ་གྱི་དངོས་པོ་བཀག་པར་བྱས་སོ། །

[Block 4397]
དེ་མེད་པས་ཅི་ཤེས་པས་སེམས་ཞེས་བྱ་སྟེ། གཟུང་བ་མེད་པས་འཛིན་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 4398]
དེ་བས་ན་སེམས་མེད༌[^2672]ན་དེའི་ཕྱི་རོལ་གྱི་སྣང་བ་གང་ལས་ཡིན་ཏེ། མོ་གཤམ་གྱི་བུ་འགྲོ་བ་དང་འོང་བ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 4399]
གཟོད་མ་ནས་མ་སྐྱེས་པའི་ངོ་བོའི་རང་བཞིན་དངོས་པོ་རྣམས་ལ་གང་དང་གང་གི་ལྷན་ཅིག་ཏུ་སྣང་བའམ་མི་སྣང་བ་ཡིན་ནོ། །

[Block 4400]
[^2673]གང་གིས་སེམས་ཉིད་དོན་གྱི་རྣམ་པ་ཞེས་བརྗོད་དེ། །དོན་ནི་སྒྱུ་མ་དང་སྨིག་རྒྱུ་ལ་སོགས་པ་བཞིན་དུ་བརྫུན་པ་ཡིན་པས་དེ་སེམས་ཀྱི་རྣམ་པ་ཉིད་ཇི་ལྟར་ཡིན། སེམས་ཀྱང་ཆ་ཆའི་དབྱེ་བས་རྣམ་པར་དཔྱད་ན་སྟོང་པ་ཉིད་ཀྱི་རང་བཞིན་ཡིན་པས་དེའི་དོན་གྱི་རྣམ་པ་ཇི་ལྟར་ཡིན་ནོ།[^2674] །

[Block 4401]
དེ་བས་ན་རྣམ་པར་ཤེས་པའི་བག་ཆགས་ཀྱི་གདོན་གྱིས་བཟུང་བའི༌[^2675]བློ་དང་ལྡན་པ་ཁྱོད་ཀྱིས༌[^2676]གཟུང་བ་དང་འཛིན་པའི་དབྱེ་བས་ཕྱི་ནང་གི་ཚུལ་དུ་བརྟགས་སོ། །

[Block 4402]
སེམས་མེད་པས་དེ་ལ་མཚན་ཉིད་གསུམ་གཞག་པ༌[^2677]ནི་ཇི་ལྟར༌[^2678]ཡིན། འབའ་ཞིག་ངོ་བོ་མེད་པའི་རང་བཞིན་གྱི་སེམས་ལ་མཚན་ཉིད་གསུམ་ནི་ག་ལས་འབྱུང་། དེ་ནི་དྲི་མ་དང་བཅས་པ་ཡང་མ་ཡིན་ཏེ།

[Block 4403 [VERSE]]
གང་ཞིག་རྣམ་པར་སྦྱང་བའི་ཕྱིར། །
མཚན་ཉིད་གསུམ་ནི་བསྒོམ་པར་བྱ། །
འབྱུང་བ་ལ་སོགས་རྣམ་ཤེས་ལ། །
བཤད་པ་གཞན་དག་འགག་པར་འགྱུར།[^2679] །

[Block 4404 [VERSE]]
ཡེ༌[^2680]ཤེས་པས་ནི་བྲལ་གྱུར་ན། །
ལོག་པར་རྟོག་པར་མ་ཡིན་ནམ། །
གང་ཚེ་དེ་ཉིད་ཁོ་ན་ལ། །
རྒྱལ་བས་མྱ་ངན་འདས་གསུངས་པ། །

[Block 4405 [VERSE]]
དེ་ཚེ་ལྷག་མ་བརྫུན་པ་ནི། །
མཁས་པ་གང་གིས་རྟོགས༌[^2681]པར་བྱེད། །

[Block 4406]
ཅེས་འབྱུང་ངོ་། །དེ་ཁོ་ན་ཉིད་གཅིག་ཁོ་ན་ནི་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་དེ་མྱ་ངན་འདས་པ་ཁོ་ནའོ། །

[Block 4407]
རྒྱལ་བས་གསུངས་པ་ནི་བསྟན་པའོ། །

[Block 4408]
དེ་ཚེ་ལྷག་མ་ནི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ཡོད་པའི་མཚན་ཉིད་དང་རྣམ་རིག་སྣང་བ་ཡང་བརྫུན་པ་ཉིད་དོ། །

[Block 4409]
དེ་ལྟར་མཁས་པ་གང་ནི་རིག་པ་དང་ལྡན་པས་རྟོགས་པར་ནི་དཔྱད་པར༌[^2682]བྱའོ། །

[Block 4410]
དེ་བས་ན་གཟོད་མ་ནས་གྲུབ་པ་སྨོས་པ༌[^2683]ཐམས་ཅད་དང་བྲལ་བ་དེ་ཁོ་ན་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་རྣམ་པར་ཤེས་པའི་རྣམ་པའི་དོན་དང་རྣམ་རིག་ཙམ་ཡང་མེད་དོ། །

[Block 4411]
དེ་བས་ན་གཟུང་བ་དང་འཛིན་པ་རྣམ་པར་སྤངས་པའོ། །

[Block 4412]
དེས་ནི་གང་ཟག་ལ་བདག་མེད་པ་དང་ཆོས་ལ་བདག་མེད་པ་ཉིད་བསྟན་ཏོ། །

[Block 4413]
དེས་ནི་རྣལ་འབྱོར་སྤྱོད་པ་རྣམས་ཀྱི་རྣམ་པ་དང་བཅས་པ་དང་། རྣམ་པ་མེད་པའི་རྣམ་རིག་ཙམ་གྱི་ཕྱོགས་སེལ་ཏོ། །

[Block 4414]
གཉིས་ཀ་ལ་བདག་མེད་པའི་མཚན་ཉིད་ཅན་གྱི་ཐེག་པ་ཆེན་པོའི༌[^2684]ཕྱོགས་བསྟན་པར་བྱ་བའི་ཕྱིར། ཆོས་བདག་མེད་པ་ནི་རང་བཞིན་གྱིས་འོད་གསལ་བ་སྟེ་ཞེས་པ་ལ། །ཆོས་ཐམས་ཅད་ནི་ཕུང་པོ་ལ་སོགས་པ་དང་རྣམ་རིག་ཙམ་སྟེ། དེ་དག་རང་བཞིན་གྱིས་བདག་མེད་པ་སྟེ་སྟོང་པའོ། །

[Block 4415]
སྒོམ་པ་ནི༌[^2685]འདི་ལ་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་ཡན་ལག་ཡིན་ཏེ། དེ་ལ་ཆོས་ཐམས་ཅད་སྟོང་པ་ཡིན་ཏེ། གཅིག་དང་དུ་མ་དང་བྲལ་བའི་ཕྱིར་ཏེ་གཟུགས་བརྙན༌[^2686]བཞིན་ནོ། །
--- END BLOCKS ---
