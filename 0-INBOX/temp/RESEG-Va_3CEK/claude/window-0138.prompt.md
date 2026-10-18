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
[Block 4831]
གལ་ཏེ་དེ་ལྟ་ན་ནི་ཅིའི་ཕྱིར་བདག་ནི་འདས་པའི་དུས་ན་གཟུགས་འདི་ལྟ་བུ་དང་ལྡན་པར་གྱུར་ཏོ་ཞེས་གསུངས།

[Block 4832]
གང་དག་དེ་ལྟར་རྣམ་པ་དུ་མ་རྗེས་སུ་དྲན་པ་ཞེས་བྱ་བ༌[^3427]རབ་ཏུ་སྟོན་པར་བྱེད་དོ། །

[Block 4833]
གལ་ཏེ་གང་ཟག་གཟུགས་དང་ལྡན་པར་ལྟ་བར་གྱུར་ན་འཇིག་ཚོགས་ལ་ལྟ་བར་ཐལ་བར་འགྱུར་བས་འདི་ལ་ནི་མ་བཏོན༌[^3428]པ་ཁོ་ན་སྐྱབས་ཡིན་ནོ། །

[Block 4834]
དེ་ལྟ་བས་ན་གང་ཟག་ནི་བཏགས་པའི་ཡོད་པ་ཡིན་ཏེ། ཕུང་པོ་དང་རྒྱུན་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 4835 [HEADING]]
#### སངས་རྒྱས་ཐམས་ཅད་མཁྱེན་པ། ^6-2-7-0

[Block 4836]
གལ་ཏེ་དེ་ལྟར་ན་འོ་ན་ནི་སངས་རྒྱས་ཐམས་ཅད་མཁྱེན་པ་མ་ཡིན་པར་འགྱུར་ཏེ། ཐམས་ཅད་ཤེས་པར་འགྱུར་བའི་སེམས་སམ༌[^3429]སེམས་ལས་བྱུང་བ་གང་ཡིན་པ་དེ་ནི་ཅུང་ཟད་ཀྱང་མེད་དེ། སྐད་ཅིག་མ་ཡིན་པའི་ཕྱིར༌[^3430]གང་ཟག་གིས་ནི་ཤེས་པར་འགྱུར་རོ། །

[Block 4837]
དེ་ལྟ་ན་ནི་འོ་ན་སེམས་འཇིག་པ་ན་གང་ཟག་མི་འཇིག་པར་ཁས་བླངས་པའི་ཕྱིར་འདི་རྟག་པ་ཉིད་དུ་ཁས་བླངས་པ་ཡིན་ནོ། །

[Block 4838]
ཁོ་བོ་ཅག་ནི་ཐམས་ཅད༌[^3431]མཁྱེན་པ་མངོན་སུམ་དུ་གྱུར་པའི་ཕྱིར་སངས་རྒྱས་ཐམས་ཅད་མཁྱེན་པ་ཡིན་པར་ནི་མི་སྨྲའོ། །

[Block 4839]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། མཐུ་ཡོད་པའི་ཕྱིར་ཏེ། སངས་རྒྱས་ཞེས་བྱ་བའི་རྒྱུད་གང་ཡིན་པ་དེ་ལ་གང་དུ་བཞེད་པར་གཏང་བ་ཙམ་གྱིས་ཕྱིན་ཅི་མ་ལོག་པའི་མཁྱེན་པ་སྐྱེ་བ་གང་ཡིན་པའི་མཐུ་འདི་ཡོད་དོ། །

[Block 4840]
འདིར་སྨྲས་པ།

[Block 4841 [VERSE]]
རྒྱུན་གྱིས་སྤྱོད་པའི་ཕྱིར་ན་དཔེར། །
མེ་ཡིས་ཐམས་ཅད་སྲེག་འདོད་ལྟ། །
དེ་བཞིན་ཐམས་ཅད་མཁྱེན་འདོད་བྱའི། །
ཅིག་ཅར་ཐམས་ཅད་མཁྱེན་ཕྱིར་མིན། །

[Block 4842]
འདི་ཇི་ལྟར་ཁོང་དུ་ཆུད་ཅེ་ན། འདས་པ་ལ་སོགས་པ་གསུངས་པའི་ཕྱིར་ཏེ།

[Block 4843 [VERSE]]
རྫོགས་སངས་རྒྱས་འདས་གང་དག་དང་། །
སངས་རྒྱས་མ་བྱོན་གང་དག་དང་། །
ད་ལྟའི་རྫོགས་སངས་རྒྱས་གང་ཡིན། །
མང་པོ་རྣམས་ནི༌[^3432]མྱ་ངན་སེལ། །

[Block 4844]
ཞེས་གསུངས་སོ། །

[Block 4845]
ཁྱེད་ཅག་ཀྱང་ཕུང་པོ་རྣམས་ཁོ་ན་དུས་གསུམ་པ་ཡིན་པར་འདོད་ཀྱི་གང་ཟག་ནི་མ་ཡིན་ནོ། །

[Block 4846 [HEADING]]
#### ཁུར་དང་ཁུར་ཁྱེར་བ། ^6-2-8-0

[Block 4847]
གལ་ཏེ་ཕུང་པོ་རྣམས་ཁོ་ན་གང་ཟག་ཡིན་ན་ཅིའི་ཕྱིར་དགེ་སློང་དག་ཁྱེད་ལ་ཁུར་ཡང་བསྟན་ཏོ། །

[Block 4848]
ཁུར་ལེན་པ་དང་། ཁུར་འདོར་བ་དང་།

[Block 4849]
ཁུར་ཁྱེར་བ་ཡང་བསྟན་གྱི༌[^3433]ཞེས་གསུངས།

[Block 4850]
ཅིའི་ཕྱིར་གསུངས་པར༌[^3434]མི་བྱ། ཁུར་ཉིད་ཁུར་ཁྱེར་བ་ཡིན་པར་ནི་རིགས་པ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་ལྟ་བུ་མི་སྣང་བའི་ཕྱིར་རོ། །

[Block 4851]
བརྗོད་པར་བྱ་བ་མ་ཡིན་པ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་ལྟ་བུ་མི་སྣང་བའི་ཕྱིར་རོ། །

[Block 4852]
ཁུར༌[^3435]ལེན་པ་ཡང་ཕུང་པོས་མ་བསྡུས་པར་ཡང༌[^3436]ཐལ་བར༌[^3437]འགྱུར་རོ། །

[Block 4853]
ཁུར་ཁྱེར་བ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཅི་ནས་ཚེ་དང་ལྡན་པ་མིང་འདི་ཞེས་བྱ་བ་ནས་ཡུན་ནི་འདི་སྲིད་ཅིག་གནས་ནས་ཚེའི་མཐའ་ནི་འདི་ཙམ་ཞིག་གོ་ཞེས་བྱ་བའི་བར་གང་ཡིན་པ་དེ་ཉིད་ཤེས་པར་འགྱུར་ཞིང་། རྟག་པའམ་གང་ཟག་ཅེས་བྱ་བ་གཞན་དུ་ཤེས་པར་མི་འགྱུར་བ་དོན་དེ༌[^3438]ཁོ་ནའི་ཕྱིར་བསྟན་ཏེ་ཕུང་པོ་སྔ་མ་རྣམས་ཁོ་ན་ཕུང་པོ་ཕྱི་མ་རྣམས་ལ་གནོད་པར་བྱེད་པ་ཡིན་པས་ཁུར་དང༌[^3439]ཁུར་ཁྱེར་བ་ཞེས་བཤད་པ་ཡིན་ནོ། །

[Block 4854 [HEADING]]
#### སེམས་ཅན་སྐྱེ་བ་པ་མེད་དོ་ཞེས་ཟེར་བ་ལོག་པར་ལྟ་བ། ^6-2-9-0

[Block 4855]
གང་ཟག་ནི་ཡོད་པ་ཉིད་དེ། འདི་ལྟར་སེམས་ཅན་སྐྱེ་བ་པ་མེད་དོ་ཞེས་ཟེར་བ་ནི་ལོག་པར་ལྟ་བ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 4856]
སེམས་ཅན་སྐྱེ་བ་པ་མེད་དོ་ཞེས་སུ་ཟེར། ཇི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་རྣམ་པར་ཕྱེ་བ་ལྟར་ཡོད་དོ། །ཞེས་ཟེར་རོ། །

[Block 4857]
དེ་ལྟ་བས་ན་འདི་ནི་གང་ཞིག་ཕ་རོལ་དུ་སྐྱེ་བ་པ་སེམས་ཅན་ཞེས་བྱ་བ་ཕུང་པོའི་རྒྱུན་ལ་སེམས་ཅན་སྐྱེ་བ་པ་མེད་དོ་ཞེས་སྐུར་པ་འདེབས་པ་དེའི་ལོག་པར་ལྟ་བ་ཡིན་ཏེ། ཕུང་པོ་རྣམས་ནི་སྐྱེ་བ་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4858]
གང་ཟག༌[^3440]ལ་སྐུར་པ་འདེབས་པ༌[^3441]འདི་ལོག་པར་ལྟ་བ་ཡིན་ན་ཡང་ཅི་ཞིག་གིས་སྤང་བར་བྱ་བར་འགྱུར། འདི་བདེན་པ་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་པར་ཡང་མི་རུང་ལ་བསྒོམ་པས་སྤང་བར་བྱ་བ་ཡིན་པར་ཡང་མི་རུང་སྟེ། གང་ཟག་བདེན་པ་རྣམས་ཀྱི་ཁོངས་སུ་མ་གཏོགས་པའི་ཕྱིར་རོ། །

[Block 4859 [HEADING]]
#### གང་ཟག་གཅིག་པུ་སྐྱེ་བ་ན་སྐྱེ་བ། ^6-2-10-0

[Block 4860]
གལ་ཏེ་འཇིག་རྟེན་ན་ཡང་གང་ཟག་གཅིག་པུ་སྐྱེ་བ་ན་སྐྱེའོ་ཞེས་གསུངས་པའི་ཕྱིར་ཕུང་པོ་རྣམས་མ་ཡིན་ནོ་ཞེ་ན་མ་ཡིན་ཏེ། སྤྱི་ལ་ཡང་གཅིག་ཉེ་བར་འདོགས་པའི་ཕྱིར་ཏིལ་གཅིག་དང་། འབྲས་ཐུག་པོ་ཆེ་གཅིག་ཅེས་བྱ་བ་ལྟ་བུ་དང་། ཕུང་པོ་གཅིག་དང་། ཚིག་གཅིག་ཅེས་བྱ་བ་བཞིན་ནོ། །

[Block 4861]
ཡང་ན་གང་ཟག་འདུས་བྱས་ཡིན་ནོ་ཞེས་བྱ་བར་བརྗོད་པར་བྱ་སྟེ། སྐྱེ་བ་དང་ལྡན་པ་ཉིད་དུ་ཁས་བླངས་པའི་ཕྱིར་རོ། །

[Block 4862]
དེ་ནི་ཇི་ལྟར་ཕུང་པོ་རྣམས་སྔོན་མེད་པ་ལས་བྱུང་བ༌[^3442]དེ་ལྟར་སྐྱེ་བ་ནི་མ་ཡིན་ནོ། །

[Block 4863]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། ཕུང་པོ་གཞན་ལེན་པའི་ཕྱིར་ཏེ། དཔེར་ན་རིག་པ༌[^3443]བླངས་པའི་ཕྱིར་མཆོད་སྦྱིན་པ་སྐྱེས་སོ། །

[Block 4864]
བརྡ་སྤྲོད་པ་པ་སྐྱེས་སོ་ཞེས་བྱ་བ་དང་། རྟགས་བླངས༌[^3444]པའི་ཕྱིར་དགེ་སློང་སྐྱེས་སོ། །

[Block 4865]
ཀུན་དུ་རྒྱུ་སྐྱེས་སོ་ཞེས་བྱ་བ་དང་། གནས་སྐབས་གཞན་བླངས་པའི༌[^3445]ཕྱིར་རྒ་བ་སྐྱེས་སོ། །

[Block 4866]
ན་བ་སྐྱེས་སོ་ཞེས་བྱ་བ་བཞིན༌[^3446]ནོ། །

[Block 4867]
མ་ཡིན་ཏེ། བཀག་པའི་ཕྱིར་རོ། །

[Block 4868]
བཅོམ་ལྡན་འདས་ཀྱིས་དོན་དམ་པ་སྟོང་པ་ཉིད་ཀྱི་མདོ་ཁོ་ན་ལས།

[Block 4869]
དགེ་སློང་དག་ལས་ནི་ཡོད་དོ། །

[Block 4870]
རྣམ་པར་སྨིན་པ་ནི་ཡོད་དོ། །
--- END BLOCKS ---
