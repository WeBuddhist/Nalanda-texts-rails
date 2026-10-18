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
[Block 4551]
དགའ་བ་ནི་ཡིད་བདེ་བའི་རང་བཞིན༌[^3268]ནོ། །

[Block 4552]
བཏང་སྙོམས་མ་ཆགས།

[Block 4553 [VERSE]]
བཏང་སྙོམས་ནི་མ་ཆགས་པའི་བདག་ཉིད་ཡིན་ནོ། །
ཇི་ལྟར་ན་གནོད་སེམས་ཀྱི་གཉེན་པོ་ཡིན་ཞེ་ན།
དེ་ནི་ཆགས་པས་དྲངས་པ་ཡིན་པའི་ཕྱིར་རོ། །
འདི་ནི་གཉི་གའི་རང་བཞིན་ཡིན་ན་རུང་ངོ་། །

[Block 4554 [HEADING]]
##### ཚད་མེད་པའི་རྣམ་པ། ^5-17-1-3-0

[Block 4555]
བྱམས་པ་ལ་སོགས་པ་འདི་དག་གི་རྣམ་པ་ནི།

[Block 4556 [VERSE]]
ཀྱེ་མ་བདེར་གྱུར་སྡུག་བསྔལ་དང་། །
དགར་གྱུར་སེམས་ཅན་རྣམས་སྙོམས་པ། །

[Block 4557]
ཀྱེ་མ་སེམས་ཅན་རྣམས་བདེ་བར་གྱུར་ཅིག་སྙམ་དུ་ཡིད་ལ༌[^3269]བྱེད་ཅིང་བྱམས་པ་ལ་སྙོམས་པར་འཇུག་གོ། །

[Block 4558]
ཀྱེ་མ་སེམས་ཅན་རྣམས་ནི་སྡུག་བསྔལ་ལོ་སྙམ་དུ་ཡིད་ལ་བྱེད་ཅིང་སྙིང་རྗེ་ལ་སྙོམས་པར་འཇུག་གོ། །

[Block 4559]
ཀྱེ་མ་སེམས་ཅན་རྣམས་ཡིད་བདེ༌[^3270]བར་གྱུར་ཅིག་སྙམ་དུ་ཡིད་ལ༌[^3271]བྱེད་ཅིང་དགའ་བ་ལ་སྙོམས་པར་འཇུག་གོ། །

[Block 4560]
སེམས་ཅན་རྣམས་མཉམ་མོ་སྙམ་དུ་དེ་ལྟར་ཡིད་ལ་བྱེད་ཅིང་བཏང་སྙོམས་ལ་སྙོམས་པར་འཇུག་སྟེ། བར་མར་གནས༌[^3272]པའི་ཕྱིར་རོ། །

[Block 4561]
དེ་དང་མི་ལྡན་པ་རྣམས་ལ་བདེ་བར་མོས་པའི་ཕྱིར་ཇི་ལྟར་ན་ཕྱིན་ཅི་ལོག་ཉིད་དུ་མི་འགྱུར་ཞེ་ན། གྱུར་ཅིག་སྙམ་དུ་སེམས་པའི་ཕྱིར་རོ། །

[Block 4562]
ཡང་ན་བསམ་པ་ཕྱིན་ཅི་མ་ལོག་པའི་ཕྱིར་ཏེ། མོས་པར་འདུ་ཤེས་པའི་ཕྱིར་རོ། །

[Block 4563]
ཡང་ན་དེ་ལྟར་ཕྱིན་ཅི་ལོག་པ་ཉིད་ཡིན་ན་ཡང་ཉེས་པ་ཅི་ཞིག་ཡོད། གལ་ཏེ་མི་དགེ་བ་ཉིད་ཡིན་ནོ་ཞེ་ན་ནི། མ་ཡིན་ཏེ། གནོད་སེམས་ལ་སོགས་པའི་གཉེན་པོ་ཡིན་པས་དགེ་བའི་རྩ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4564]
འདི་དག་གི་རྣམ་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 4565 [HEADING]]
##### ཚད་མེད་པའི་དམིགས་པ། ^5-17-1-4-0

[Block 4566]
སྤྱོད་ཡུལ་འདོད་པའི་སེམས་ཅན་རྣམས། །འདི་དག་གི་དམིགས་པ་ནི་འདོད་པ་ན་སྤྱོད་པའི་སེམས་ཅན་རྣམས་ཡིན་ཏེ། དེ་ལ་དམིགས་པའི་གནོད་སེམས་ལ་སོགས་པའི་གཉེན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4567]
ཕྱོགས་གཅིག་ཏུ་མོས་ནས་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་ནི་སྣོད་ཀྱི་སྣོད་ན་གནས་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 4568 [HEADING]]
##### ཚད་མེད་པའི་ས། ^5-17-1-5-0

[Block 4569]
དེ་དག་ས་དུ་པ་ཞིག་ཡིན་ཞེ་ན། དགའ་བ་བསམ་གཏན་གཉིས་ན་ཡོད།[^3273] །དགའ་བ་ནི་བསམ་གཏན་དང་པོ་དང་གཉིས་པ་ན་ཡོད་དེ། ཡིད་བདེ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4570]
གཞན་ནི་དྲུག་ན། ཚད་མེད་པ་གཞན་གསུམ་ནི༌[^3274]ས་དྲུག་པོ་མི་ལྕོགས་པ༌[^3275]མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། བསམ་གཏན་རྣམས་ན་ཡོད་དོ། །

[Block 4571]
ཁ་ཅིག་ལྔ། ཁ་ཅིག་ནི་འདི་དག༌[^3276]མི་ལྕོགས་པ་མེད་པ་མ་གཏོགས་པ་ལྔ་ན་ཡོད་པར་འདོད་དོ། །

[Block 4572]
གཞན་དག་ན་རེ་འདོད་པའི་ཁམས་དང་ཉེར་བསྡོགས་རྣམས་བསྣན་ནས་བཅུ་ན་ཡོད་དོ་ཞེས་ཟེར་ཏེ། །མཉམ་པར་བཞག་པ་དང་མཉམ་པར༌[^3277]བཞག་པ་མ་ཡིན་པ་དང་། དངོས་གཞི་དང་།

[Block 4573]
སྦྱོར་བ་སྨོས་པའི་ཕྱིར་རོ། །

[Block 4574 [HEADING]]
##### ཚད་མེད་པས་ཉོན་མོངས་པ་མི་སྤོང་བ། ^5-17-1-6-0

[Block 4575]
གནོད་སེམས་ལ་སོགས་གཉེན་པོའི་ཕྱིར། །

[Block 4576]
ཞེས་གང་བཤད་པ། ཅི་ཚད་མེད་པ་རྣམས་ཀྱིས་ཀྱང་ཉོན་མོངས་པ་སྤོང་བ་ཡིན་ནམ་ཞེ་ན། དེ་ཡིས་མི་སྤོང་། བསམ་གཏན་དངོས་གཞིའི་ས་པ་ཡིན་པའི་ཕྱིར་དང་། མོས་པ་ཡིན༌[^3278]ལ་བྱེད་པའི་ཕྱིར་དང་། སེམས་ཅན་ལ་དམིགས་པ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་དག་གི་སྦྱོར་བས་གནོད་སེམས་ལ་སོགས་པ་རྣམ་པར་གནོན་པའི་ཕྱིར་དང་། སྤངས་པ་ཐག་སྲིང་བར་བྱེད་པའི་ཕྱིར་དེ་དག་གི་གཉེན་པོ་ཉིད་དུ་བཤད་དོ། །

[Block 4577]
བྱམས་པ་ལ་སོགས་པ་འདོད་པའི་ཁམས་དང་མི་ལྕོགས་པ་མེད་པའི་ས་པ་རྣམས་ནི་དངོས་གཞིའི་ཚད་མེད་པ་དང་འདྲ་བ་དག་ཡོད་དོ། །

[Block 4578]
[^3279]དེ་དག་གིས་དེ་རྣམས་རྣམ་པར་མནན་ནས་སྤོང་བའི་ལམ་རྣམས་ཀྱིས་རབ་ཏུ་སྤོང་བར་བྱེད་དོ། །

[Block 4579]
དེ་ནས་འདོད་ཆགས་དང་བྲལ་བའི་གནས་སྐབས་ན་ནི་དངོས་གཞིའི་ཚད་མེད་པ་རྙེད་པའི་ཕྱིར༌[^3280]རྐྱེན་སྟོབས་དང་ལྡན་པ་རྙེད་ཀྱང་དེ་དག་གིས་མི་བརྫི་བ༌[^3281]ཡིན་ནོ། །

[Block 4580 [HEADING]]
##### ལས་དང་པོ་པ་བྱམས་པ་ལ་སྦྱོར་བ། ^5-17-1-7-0

[Block 4581]
ཡང་ལས་དང་པོ་པ་བྱམས་པ་ལ་ཇི་ལྟར་སྦྱོར་ཞེ་ན། ཇི་ལྟར་བདག་ཉིད་ཀྱི་བདེ་བ་ཉམས་པ༌[^3282]ཡོད་པའམ། གཞན་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་འཕགས་པ་དགྲ་བཅོམ་པའི་ཐོས་པ་དེ་བཞིན་དུ་ཀྱེ་མ་སེམས་ཅན་རྣམས་ནི༌[^3283]དེ་ལྟར་བདེ་བར་གྱུར་ཅིག་ཅེས་སེམས་ཅན་རྣམས་ལ་བདེ་བར་མོས་པར་བྱེད་དོ། །

[Block 4582]
གལ་ཏེ་ཉོན་མོངས་པའི་འཇུག་པ་ཤས་ཆེ་བའི་ཕྱིར་མི་ནུས་ན་དེས་མཛའ་པོའི་ཕྱོགས་ལ༌[^3284]རྣམ་པ་གསུམ་དུ་ཕྱེ་ནས་ཆེན་པོ་ལ་བདེ་བ་དེ་མོས་པར་བྱེད་དོ། །

[Block 4583]
དེ་ནས་འབྲིང་དང་ཆུང་ངུ་ལ་བདེ་བ་དེ༌[^3285]མོས་པར་བྱེད་དོ། །

[Block 4584]
གལ་ཏེ་དེ་དག་ལ་བྱམས་པ་མཉམ་པ་ཐོབ་ན་དེའི་འོག་ཏུ་ཐ་མལ་པའི་ཕྱོགས་ལ་མོས་པར་བྱེད་དོ། །

[Block 4585]
དེའི་འོག་ཏུ་དགྲ་བོའི་ཕྱོགས་ལ་རྣམ་པ་གསུམ་དུ་ཕྱེ་ནས་ཆུང་ངུ་ལ་བདེ་བ་དེ་མོས་པར་བྱེད་དོ། །

[Block 4586]
དེ་ནས་འབྲིང་དང་ཆེན་པོ་ལ་མོས་པར་བྱེད་དོ། །

[Block 4587]
གལ་ཏེ་དེ་ལ་མཛའ་བོ་ཆེན་པོའི་ཕྱོགས་བཞིན་དུ་བདེ་བར་མོས་པ་མི་ལྡོག་པར་གྱུར་ན་དེའི་འོག་ཏུ་རིམ་གྱིས་ཁྱིམ་དང་གྲོང་དང་ཡུལ་འཁོར་གྱི་བར་དུ་བདེ་བར་མོས་པར་བྱས་ནས་ཕྱོགས་གཅིག་ནས་འཇིག་རྟེན་ཐམས་ཅད་ཀྱི་བར་དུ་བྱམས་པ་རྒྱས་པར་བྱེད་དོ། །

[Block 4588]
གང་ཞིག་ཐམས་ཅད་དུ་ཡོན་ཏན་འཛིན་པ་དེ་ནི་བྱམས་པ་མྱུར་དུ་སྐྱེད་པར་བྱེད་དོ། །

[Block 4589]
སྔོན་གྱི་བསོད་ནམས་དང་བསོད་ནམས་མ་ཡིན་པའི་འབྲས་བུ་སྣང་བའི་སྒོ་ནས་དགེ་བའི་རྩ་བ་ཀུན་དུ་ཆད་པ་ལ་ཡང་ཡོན་ཏན་གཟུང་བར༌[^3286]ནུས་ལ། རང་སངས་རྒྱས་ལ༌[^3287]ཡང་སྐྱོན་གཟུང་བར༌[^3288]ནུས་སོ། །

[Block 4590]
སྙིང་རྗེ་དང་དགའ་བ་ལ་ཡང་དེ་བཞིན་དུ་སེམས་ཅན་སྡུག་བསྔལ་བ༌[^3289]རྣམ་པ་མང་པོའི་ཆུ་བོར་བྱིང་བ་འདི་དག་སྡུག་བསྔལ་ལས་མྱུར་དུ་ཐར་ཀྱང་ཅི་མ་རུང་། མངོན་པར་དགའ་བར་གྱུར་ཀྱང་ཅི་མ་རུང་སྙམ་དུ་མོས་ཤིང་དགའ་བ་ལ༌[^3290]སྦྱོར་བར་བྱེད་དོ། །
--- END BLOCKS ---
