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
[Block 4481]
མངོན་པར་འདུ་བྱ་བ་དང་བཅས་པས༌[^3229]དྲང་བ་ཡིན་པའི་ཕྱིར། དགའ་བ་དང་མཚུངས་པར་ལྡན་པ་ཡང་མ་ཡིན་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་ལམ་དཀའ་བ་ཡིན་ནོ། །

[Block 4482]
འོ་ན་བསམ་གཏན་ཁྱད་པར་ཅན་དེའི་འབྲས་བུ་ཁྱད་པར་ཅན་གང་ཞིག་ཡིན་ཞེ་ན། དེ་ནི་ཚངས་ཆེན་འབྲས་བུ་ཅན། །བསམ་གཏན་ཁྱད་པར་ཅན་དེ་བསྒོམས་ནས་ཚངས་པ་ཆེན་པོར་འགྱུར་རོ། །

[Block 4483 [HEADING]]
### རྟོག་པ་དང་བཅས་པ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་གསུམ། ^5-12-0

[Block 4484 [HEADING]]
#### རྟོག་པ་མེད་ལ་དཔྱོད་པ་ཙམ། ^5-12-1-0

[Block 4485]
ཡང་ཏིང་ངེ་འཛིན་ཐམས་ཅད་མདོར་བསྡུས་ཏེ། མདོ་ལས་རྟོག་པ་དང་བཅས་ཤིང་དཔྱོད་པ་དང་བཅས་པའི་ཏིང་ངེ་འཛིན་དང་། རྟོག་པ་མེད་ལ་དཔྱོད་པ་ཙམ་དང་། རྟོག་པ་ཡང་མེད་ལ་དཔྱོད་པ་ཡང་མེད་པའི་ཏིང་ངེ་འཛིན་དང་ཏིང་ངེ་འཛིན་གསུམ་དུ༌[^3230]བཀའ་སྩལ་ཏེ། དེ་ལ་རེ་ཞིག་བསམ་གཏན་ཁྱད་པར་ཅན་ན༌[^3231]ནི། རྟོག་པ་ཙམ་ཞིག་བཀག་པའི་ཕྱིར་རྟོག་པ་མེད་ལ་དཔྱོད་པ་ཙམ་གྱི་ཏིང་ངེ་འཛིན་ཏོ་ཞེས་ཤེས་པར་བྱས་ཟིན་ཏོ། །

[Block 4486 [HEADING]]
#### རྟོག་དཔྱོད་བཅས་པ། ^5-12-2-0

[Block 4487]
དེ་མན་ཆད་རྟོག་དཔྱོད་བཅས་པའི།[^3232] །ཏིང་ངེ་འཛིན། བསམ་གཏན་ཁྱད་པར་ཅན་དེ་མན་ཆད་ཀྱི་ཏིང་ངེ་འཛིན་བསམ་གཏན་དང་པོ་དང་། མི་ལྕོགས༌[^3233]པ་མེད་པ་ནི་རྟོག་པ་དང་བཅས་ཤིང་དཔྱོད་པ༌[^3234]དང་བཅས་པ་ཡིན་ནོ། །

[Block 4488 [HEADING]]
#### གཉི་ག་མེད་པ། ^5-12-3-0

[Block 4489 [VERSE]]
ཡན་ཆད་གཉི་ག་མེད༌[^3235]པས་ན། །
འདི་ན་གཉི་ག་མེད་པ་སྟེ། །

[Block 4490]
བསམ་གཏན་ཁྱད་པར་ཅན་ཡན་ཆད་ཀྱི་ཏིང་ངེ་འཛིན་བསམ་གཏན་གཉིས་པའི་ཉེར་བསྡོགས་ནས་སྲིད་པའི་རྩེ་མོའི་བར་ནི་རྟོག་པ་ཡང་མེད་ལ་དཔྱོད་པ་ཡང་མེད་པའོ། །

[Block 4491 [HEADING]]
### སྟོང་པ་ཉིད་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་གསུམ། ^5-13-0

[Block 4492 [HEADING]]
#### མཚན་མ་མེད་པ། ^5-13-1-0

[Block 4493]
ཡང་སྟོང་པ་ཉིད་ཀྱི་ཏིང་འཛིན༌[^3236]དང་། སྨོན་པ་མེད་པའི་ཏིང་ངེ་འཛིན་དང་། མཚན་མ་མེད་པའི་ཏིང་ངེ་འཛིན་དང་། ཏིང་ངེ་འཛིན་གསུམ་གསུངས་ཏེ། དེ་ལ། མཚན་མེད་ཞི་བའི་རྣམ་པ་དང་། །འགོག་པའི་རྣམ་པ་དག༌[^3237]དང་མཚུངས་པར་ལྡན་པའི་ཏིང་ངེ་འཛིན་ནི་མཚན་མ་མེད་པ་སྟེ། རྣམ་པ་བཞི་པ་ཡིན་ནོ། །

[Block 4494]
མྱ་ངན་ལས་འདས་པ་ནི་མཚན་མ་བཅུ་དང་བྲལ་བའི་ཕྱིར་མཚན་མ་མེད་པ་ཡིན་ལ། དེ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་ནི་མཚན་མ་མེད་པའི་ཏིང་ངེ་འཛིན་ཡིན་ཏེ། མཚན་མ་བཅུ་ནི་ཡུལ་ལྔ་དང་ཕོ་དང་མོ་དང་འདུས་བྱས་ཀྱི་མཚན་ཉིད་རྣམས་སོ། །

[Block 4495 [HEADING]]
#### སྟོང་པ་ཉིད། ^5-13-2-0

[Block 4496]
སྟོང་ཉིད་བདག་མེད་སྟོང་ཉིད་དུ། འཇུག་པའོ། །

[Block 4497]
བདག་མེད་པ་དང་སྟོང་པ་ཉིད་ཀྱི་རྣམ་པ་དག་དང་མཚུངས་པར་ལྡན་པའི་ཏིང་ངེ་འཛིན་ནི་སྟོང་པ་ཉིད་དེ། རྣམ་པ་གཉིས་པ་ཡིན་ནོ། །

[Block 4498 [HEADING]]
#### སྨོན་པ་མེད་པ། ^5-13-3-0

[Block 4499]
སྨོན་པ་མེད་པ་ནི། དེ་ལས་གཞན་བདེན་རྣམ་པ་དང་། །བདེན་པ་ལྷག་མའི་རྣམ་པ་དག་དང་མཚུངས་པར་ལྡན་པའི་ཏིང་ངེ་འཛིན་ནི་སྨོན་པ་མེད་པ་སྟེ། རྣམ་པ་བཅུ༌[^3238]ཡིན་ནོ། །

[Block 4500]
མི་རྟག་པ་དང་སྡུག་བསྔལ་བ་དང་དེའི་རྒྱུ་དག་གིས་ཡིད་འབྱུང་བའི་ཕྱིར་དང་། ལམ་ཡང་གདོན་མི་ཟ་བར་གཟིངས་ལྟ་བུར་དོར་བར་བྱ་བ་ཡིན་པ༌[^3239]ཉིད་ཀྱི༌[^3240]ཕྱིར་དེའི་རྣམ་པ་ཅན་གྱི་ཏིང་ངེ་འཛིན་ནི་སྨོན་པ་མེད་པ་ཡིན་ཏེ། དེ་ལས་འདའ་བར་མངོན་སུམ༌[^3241]དུ་ཕྱོགས་པའི་ཕྱིར་རོ། །

[Block 4501]
མྱ་ངན་ལས་འདས་པ་དང་འདྲ་བའི་ཕྱིར་སྟོང་པ་དང་བདག་མེད་པ་དག་གིས་ནི་ཡིད་མི་འབྱུང་ངོ་། །ཏིང་ངེ་འཛིན་རྣམ་པ་གསུམ་པོ་འདི་དག་ནི་རྣམ་པ༌[^3242]གཉིས་ཏེ། དག་དང་དྲི་མ༌[^3243]མེད། འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4502]
[^3244]དག་པ་པ་ཡང༌[^3245]ཡིན་ལ་ཟག་པ་མེད་པ་དག་ཀྱང་ཡིན་ཏེ། འཇིག་རྟེན་པ་རྣམས་ནི་ས་བཅུ་གཅིག་ན་ཡོད་དོ། །

[Block 4503]
འཇིག་རྟེན་ལས་འདས་པ་རྣམས་ནི་གང་ན་ལམ་ཡོད་པ་ན་ཡོད་དོ། །

[Block 4504 [HEADING]]
### རྣམ་པར་ཐར་པའི་སྒོ་གསུམ། ^5-14-0

[Block 4505]
དེ་དག །དྲི་མེད་རྣམ་ཐར་སྒོ་གསུམ་མོ། །

[Block 4506]
ཏིང་ངེ་འཛིན་གསུམ་པོ་དེ་དག་དྲི་མ་མེད་པ་ནི་ཐར་པའི་སྒོ་ཡིན་པའི་ཕྱིར་རྣམ་པར་ཐར་པའི་སྒོ་སྟོང་པ་ཉིད་དང་། རྣམ་པར༌[^3246]པའི་སྒོ་སྨོན་པ་མེད་པ་དང་། རྣམ་པར་ཐར་པའི་སྒོ་མཚན༌[^3247]མ་མེད་པ་སྟེ། རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་ཞེས་བྱའོ། །

[Block 4507]
ཡང་།

[Block 4508 [HEADING]]
### སྟོང་ཉིད་སྟོང་ཉིད་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་གསུམ། ^5-15-0

[Block 4509 [VERSE]]
སྟོང་ཉིད་སྟོང་ཉིད་ཅེས་ལ་སོགས། །
གཞན་ཡང་ཏིང་ངེ་འཛིན་གསུམ་མོ། །

[Block 4510]
ཞེས་བྱ་བ་སྟེ། སྟོང་པ་ཉིད་སྟོང་པ་ཉིད་དང་། སྨོན་པ་མེད་པ་སྨོན་པ་མེད་པ་དང་། མཚན་མ་མེད་པ་མཚན་མ་མེད་པའོ། །

[Block 4511]
སྟོང་པ་ཉིད་ལ་སོགས་པ་ལ་དམིགས་པའི་ཕྱིར་མིང་དེ་སྐད་ཅེས་བྱའོ། །

[Block 4512]
དེ་དག་ལས།

[Block 4513 [VERSE]]
[^3248] གཉིས་ནི་སྟོང་དང་མི་རྟག༌[^3249]པར། །
མི་སློབ་པ་ལ་དམིགས་པ་ཡིན། །

[Block 4514]
ཏིང་ངེ་འཛིན་གཞན་གཉིས་ནི་མི་སློབ་པའི་ཏིང་ངེ་འཛིན་ལ་དམིགས་པ་ཡིན་ཏེ། སྟོང་པ་ཉིད་སྟོང་པ་ཉིད་ནི་མི་སློབ་པའི་སྟོང་པ་ཉིད་ཀྱི་ཏིང་ངེ་འཛིན་ལ་སྟོང་པའི་རྣམ་པར་དམིགས་སོ། །

[Block 4515]
སྨོན་པ་མེད་པ་སྨོན་པ་མེད་པ་ཡང་མི་སློབ་པའི་སྨོན་པ་མེད་པ་ལ་མི་རྟག་པའི་རྣམ་པར་དམིགས་སོ། །

[Block 4516]
སྡུག་བསྔལ་བར་ཡང་མ་ཡིན་ལ་རྒྱུ་ལ་སོགས་པར༌[^3250]ཡང་མ་ཡིན་ཏེ། ཟག་པ་མེད་པ་ནི་དེའི་མཚན་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4517]
ལམ་གྱི་རྣམ་པ་རྣམས་སུ་ཡང་མ་ཡིན་ཏེ། སུན་དབྱུང་བར༌[^3251]བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4518 [VERSE]]
མཚན་མ་མེད་པ་མཚན་མེད་ནི། །
ཞི་བར་མ་བརྟགས་ཟད་པ་ལ། །

[Block 4519]
མཚན་མ་མེད་པ་མཚན་མ་མེད་པའི་ཏིང་ངེ་འཛིན་ནི་མི་སློབ་པའི་མཚན་མ་མེད་པའི་སོ་སོར་མ་བརྟགས་པས། འགོག་པ་ལ་ཞི་བའི་རྣམ་པར་དམིགས་ཏེ། [^3252]ཟག་པ་མེད་པ་ལ་སོ་སོར་བརྟགས་པས། འགོག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 4520]
འགོག་པ་དང་། གྱ་ནོམ་པ་དང་། ངེས་པར་འབྱུང་བའི་རྣམ་པར་ནི་མ་ཡིན་ཏེ། མི་རྟག་པ་ཉིད་ཀྱི་འགོག་པ་དང་། ཐུན་མོང་ཡིན༌[^3253]པ་ཉིད་ཀྱི་ཕྱིར་དང་། ལུང་དུ་མ་བསྟན་པའི་ཕྱིར་དང་། བྲལ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
