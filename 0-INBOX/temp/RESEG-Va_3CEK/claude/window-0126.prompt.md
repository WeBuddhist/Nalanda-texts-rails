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
འདིའི་མཚན་ཉིད་ཅི་ཞེ་ན། དེ་ནི་གོ་རིམས་བཞིན་དུ།

[Block 4412 [VERSE]]
ཉོན་མོངས་སྐྱེ་དང་རང་ས་དང་། །
གོང་དང་ཟག་མེད་རྗེས་མཐུན་པའོ། །

[Block 4413 [HEADING]]
#### ཉམས་པའི་ཆ་དང་མཐུན་པ། ^5-4-1-0

[Block 4414]
ཉམས་པའི་ཆ་དང་མཐུན་པ་ནི་ཉོན་མོངས་པ་སྐྱེ་བ་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 4415 [HEADING]]
#### གནས་པའི་ཆ་དང་མཐུན་པ། ^5-4-2-0

[Block 4416]
གནས་པའི་ཆ་དང་མཐུན་པ་ནི་རང་གི་ས་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 4417 [HEADING]]
#### ཁྱད་པར་ཅན་གྱི་ཆ་དང་མཐུན་པ། ^5-4-3-0

[Block 4418]
ཁྱད་པར་ཅན༌[^3190]གྱི་ཆ་དང་རྗེས་སུ༌[^3191]མཐུན་པ་ནི་ས་གོང་མ་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 4419 [HEADING]]
#### ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ། ^5-4-4-0

[Block 4420]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་ནི་ཟག་པ་མེད་པའི་རྗེས་སུ་མཐུན་པ་སྟེ། ཟག་པ་མེད་པ་ནི་དེ་ལས་སྐྱེའོ། །

[Block 4421 [HEADING]]
### བཞི་པོ་དེ་དག་གི་མཇུག་ཐོགས་སུ་སྐྱེ་བ། ^5-5-0

[Block 4422]
ཡང་བཞི་པོ་དེ་དག་ལས་གང་གི་མཇུག་ཐོགས་སུ་དུ་ཞིག་སྐྱེ་ཞེ་ན།

[Block 4423 [VERSE]]
ཉམས་ཆ་མཐུན་སོགས་མཇུག་ཐོགས་སུ། །
གཉིས་དང་གསུམ་དང་གསུམ་དང་གཅིག །

[Block 4424]
ཉམས་པའི་ཆ་དང་མཐུན་པ་ནི་ཉམས་པ་དང་བརྟེན་པའོ། །

[Block 4425]
དེའི་མཇུག་ཐོགས་སུ་ནི་གཉིས་སྐྱེ་སྟེ། ཉམས་པ་དང་གནས་པའི་ཆ་དང་མཐུན་པ་དག་གོ། །

[Block 4426]
གནས་པའི་ཆ་དང་མཐུན་པའི་མཇུག༌[^3192]ཐོགས་སུ་ནི་གསུམ་སྟེ། ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་མ་གཏོགས་སོ། །

[Block 4427]
ཁྱད་པར་ཅན༌[^3193]གྱི་ཆ་དང་མཐུན་པའི་མཇུག་ཐོགས་སུ་ནི་གསུམ་སྟེ། ཉམས་པའི་ཆ་དང་མཐུན་པ་མ་གཏོགས་སོ། །

[Block 4428]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པའི་མཇུག་ཐོགས་སུ་ནི་གཅིག་སྟེ། དེ་གཅིག་པུ་སྐྱེའོ། །

[Block 4429 [HEADING]]
### ཐོད་རྒལ་གྱི་སྙོམས་པར་འཇུག་པ། ^5-6-0

[Block 4430]
ཐོད་རྒལ་གྱི་སྙོམས་པར་འཇུག་པ་ཇི་ལྟར་སྐྱེ་ཞེ་ན།

[Block 4431 [VERSE]]
ས་བརྒྱད་རྣམ་གཉིས་འབྲེལ་པ་དང་། །
གཅིག་རྒལ་སོང་ཞིང་འོངས་ནས་ནི། །
རིས་མི༌[^3194]མཐུན་པ་གསུམ་པར་འགྲོ། །
ཐོད་རྒལ་གྱི༌[^3195]ནི་སྙོམས་འཇུག་ཡིན། །

[Block 4432]
ས་བརྒྱད་ཅེས་བྱ་བ་ནི་བསམ་གཏན་དང་། གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པ་རྣམས་སོ། །

[Block 4433]
རྣམ་གཉིས་ཞེས་བྱ་བ་ནི་ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པའོ། །

[Block 4434]
འབྲེལ་པ་དང་ཞེས་བྱ་བ་ནི་གོ་རིམས་བཞིན་དུའོ། །

[Block 4435]
གཅིག་རྒལ་ཞེས་བྱ་བ་ནི་རེ་རེ་རྒལ་ནས་སོ། །

[Block 4436]
སོང་ཞིང་ཞེས་བྱ་བ་ནི་ལུགས་དང་མཐུན་པར་སྙོམས་པར་ཞུགས་ནས་སོ། །

[Block 4437]
འོངས་ནས་ཞེས་བྱ་བ་ནི་ལུགས་དང་མི་མཐུན་པར་སྙོམས་པར་ཞུགས་ནས་སོ། །

[Block 4438]
ཟག་པ་དང་བཅས་པའི་ས་བརྒྱད་དང་ཟག་པ་མེད་པའི་ས་བདུན་ལུགས་དང་མཐུན་པ་དང་ལུགས་དང་མི་མཐུན་པའི༌[^3196]སྙོམས་པར་འཇུག་པའི་སྒོ་ནས་བྱང་བར་བྱས་ནས། ཕྱིས་ཟག་པ་དང་བཅས་པའི་བསམ་གཏན་དང་པོ་ནས་ཟག་པ་དང་བཅས་པའི་གསུམ་པ་ལ་སྙོམས་པར་འཇུག་ཅིང་། དེ་ནས་ནི་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ། དེ་ནས་ནི་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ལ་སྙོམས་པར་འཇུག་གོ། །

[Block 4439]
དེ་བཞིན་དུ་ལུགས་དང་མི་མཐུན་པ་ཡང་བྱང་བར་བྱས་ནས་ཟག་པ་མེད་པ་རྣམས་ཀྱང་རེ་རེ་རྒལ་ཞིང་ལུགས་དང་མཐུན་པ་དང་ལུགས་དང་མི་མཐུན་པར་སྙོམས་པར་འཇུག་པ་ནི་ཐོད་རྒལ་དུ་སྙོམས་པར་འཇུག་པའི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 4440]
གང་གི་ཚེ་ཟག་པ་དང་བཅས་པ་དང་པོ་ནས་ཟག་པ་མེད་པའི་བསམ་གཏན་གསུམ་པ་ལ་སྙོམས་པར་འཇུག་ཅིང་། དེ་ནས་ནི་ཟག་པ་དང་བཅས་པའི་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ། དེ་ནས་ནི་ཟག་པ་མེད་པའི་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ལ་སྙོམས་པར་འཇུག་ཅིང་། དེ་བཞིན་དུ་ལུགས་དང་མི་མཐུན་པར་ཡང་སྙོམས་པར་འཇུག་པ་དེའི་ཚེ་རིས་མི་མཐུན་པའི་རྫས་གསུམ་པར་འགྲོ་བའི་ཕྱིར་མངོན་པར་གྲུབ་པ་ཡིན་ནོ། །

[Block 4441]
ཤིན་ཏུ་རིང་བའི་ཕྱིར་བཞི་པ་ལ་ནི་སྙོམས་པར་མི་འཇུག་གོ། །

[Block 4442]
དེ་ཡང་གླིང་གསུམ་དུ་དུས་དང་མི་སྦྱོར་བར༌[^3197]རྣམ་པར་གྲོལ་བའི་དགྲ་བཅོམ་པ་ཁོ་ནས་སྐྱེད་པར་བྱེད་དེ། [^3198]ཉོན་མོངས་པ་མེད་པའི་ཕྱིར་དང་། ཏིང་ངེ་འཛིན་ལ་དབང་བའི་ཕྱིར་རོ། །

[Block 4443]
མཐོང་བས་འཐོབ་པ་ནི་གལ་ཏེ་དབང་པོ་རྣོན་པོ་ཡིན་པའི་ཕྱིར་ཏིང་ངེ་འཛིན་ལ་དབང་བ་ཡིན༌[^3199]ཡང་ཉོན་མོངས་པ་མེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 4444]
དུས་ཀྱིས༌[^3200]རྣམ་པར་གྲོལ་བ་ནི་གལ་ཏེ་ཉོན་མོངས་པ་མེད་པ་ཡིན་ཡང་། ཏིང་ངེ་འཛིན་ལ་དབང་བ་ནི་མ་ཡིན་ནོ། །

[Block 4445 [HEADING]]
### བསམ་གཏན་དང་གཟུགས་མེད་པ་མངོན་སུམ་དུ་བྱེད་པའི་རྟེན། ^5-7-0

[Block 4446]
རྟེན་གང་གིས་བསམ་གཏན་དང་གཟུགས་མེད་པ་དུ་ཞིག་མངོན་སུམ་དུ་བྱེད་ཅེ་ན། བསམ་གཏན་གཟུགས་མེད་རང་དང་ནི། །འོག་སའི་རྟེན་ཅན་སྲིད་པའི་རྩེ་མོར་ཡང་མངོན་སུམ་དུ་བྱེད་ལ་འོག་མ་འདོད་པའི་ཁམས་ཀྱི་བར་དུ་ཡང་མངོན་སུམ་དུ་བྱེད་དོ། །

[Block 4447]
དེ་བཞིན་དུ་ལྷག༌[^3201]མ་རྣམས་ཀྱང་རང་གི་ས་དང་ས་འོག་མར་མངོན་སུམ་དུ་བྱེད་དོ། །

[Block 4448]
ཅིའི་ཕྱིར་གོང་དུ་སྐྱེས་པ་སྙོམས་པར་འཇུག་པ་འོག་མ་མངོན་སུམ༌[^3202]དུ་མི་བྱེད་ཅེ་ན། འདི་ལྟར་དེ་ལ་འོག་དགོས་མེད། །དེ་ལ་ནི་སྙོམས་པར་འཇུག་པ་འོག་མའི་རྫས་ཀྱིས་ཅུང་ཟད་ཀྱང་དགོས་པ༌[^3203]མི་བྱེད་དེ་དམན་པའི་ཕྱིར་རོ། །

[Block 4449]
སྤྱིར་བསྟན་པ་བྱས་ནས་དམིགས་ཀྱིས་སྟོན་པར་བྱེད་དེ།

[Block 4450 [VERSE]]
སྲིད་རྩེར་འཕགས་པ༌[^3204]ཅི་ཡང་མེད། །
མངོན་སུམ་བྱས་ནས་ཟག་པ་ཟད། །
--- END BLOCKS ---
