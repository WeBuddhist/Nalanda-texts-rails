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
[Block 3781]
སྡུག་བསྔལ་གྱི་བདེན་པ་ལ་སོགས་པ་རྣམས་ནི་རང་རང་གི་བདེན་པའི་རྣམ་པ་དག་ཏུ་འཇུག་པ་རེ་རེ་ཞིང་རྣམ་པ་བཞི་བཞི་ཡིན་ནོ། །

[Block 3782]
ཕ་རོལ་ཡིད་ཤེས་དྲི་མེད་ཀྱང་། །དེ་བཞིན་རྣམ་པ་བཞི་དང་ལྡན་པ་ཡིན་ཏེ། ལམ་ཤེས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3783]
དྲི་མ་དང་བཅས་ནི། ཤེས་བྱའི་རང་གི་མཚན་ཉིད་རྣམ། །ཟག་པ་དང་བཅས་པ་ནི་ཤེས་བྱ་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱི་རང་གི་མཚན་ཉིད་གང་ཡིན་པ་དེ་ནི་རྣམ་པ་འཛིན་པའོ། །

[Block 3784]
གཉིས་ཀ་ཡང་། རྫས་རེ་རེ་ཞིག་སྤྱོད་ཡུལ་ལོ། །

[Block 3785]
གང་གི་ཚེ་སེམས་འཛིན་པ་དེའི་ཚེ་སེམས་ལས་བྱུང་བ་རྣམས་མི་འཛིན་ལ། གང་གི་ཚེ་ཚོར་བ་འཛིན་པ་དེའི་ཚེ་འདུ་ཤེས་མི་འཛིན་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 3786 [VERSE]]
ལྷག་མ་རྣམ་པ་བཅུ་བཞི་ཅན། །
སྟོང་དང་བདག་མེད་མ་གཏོགས་སོ། །

[Block 3787]
ཟད་པ་དང་། མི་སྐྱེ་བའི་ཤེས་པ་དག་སྟེ། དེ་གཉིས་ནི་སྟོང་པ་དང་བདག་མེད་པའི་རྣམ་པ་དག་མ་གཏོགས་པ་རྣམ་པ་བཅུ་བཞི་ཡིན་ནོ། །

[Block 3788]
དོན་དམ་པ་བདག་ཡིན་ཀྱང་ཀུན་རྫོབ་ལ་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 3789]
ཅི་ཟག་པ་མེད་པ་ལ་རང་གི་མཚན་ཉིད་ཀྱི་རྣམ་པ་ཡོད་དམ། འོན་ཏེ་མེད་ཅེ་ན། དྲི་མེད་བཅུ་དྲུག་གཞན་རྣམ་མེད། །རྣམ་པ་བཅུ་དྲུག་མ་གཏོགས་པ་ཟག་པ༌[^1491]མེད་པའི་རྣམ་པ་མེད་དོ། །

[Block 3790]
གཞན་ཡོད་ཅེས་པ་བསྟན་བཅོས་ལ།[^1492] །གཞན་ཉི་འོག་པ་རྣམས་ན་རེ་ཡོད་ཅེས་ཟེར་རོ། །

[Block 3791]
བསྟན་བཅོས་ལས་འདི་སྐད་དུ། མི་ལྡན་པའི་སེམས་ཀྱིས་འདོད་པ་དང་ལྡན་པའི་ཆོས་རྣམས་ཤེས་པ་ན་འདི་ནི་གནས་ཡོད་དོ། །

[Block 3792]
འདི་ནི་གཞི་ཡོད་དོ། །

[Block 3793]
[^1493]ཅེས་བྱ་བར་ཤེས་པར་འགྱུར་བར་ཞེས་བྱ་བ་སྦྱོར་བར་བྱེད་པས་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བའི་བར་རོ། །

[Block 3794 [HEADING]]
#### རྫས་སུ་རྣམ་པ་བཅུ་དྲུག། ^7-3-1-0

[Block 3795]
ཡང་ཅི་རྣམ་པ་བཅུ་དྲུག་པོ་འདི་མིང་དུ་འམ་རྫས་སུ་ཡོད་ཅེ་ན། རྫས་སུ་རྣམ་པ་བཅུ་དྲུག་གོ། །

[Block 3796]
དེ་ལ་རྐྱེན་ལ་རག་ལུས་པའི་ཕྱིར་མི་རྟག་པའོ། །

[Block 3797]
གནོད་པའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་སྡུག་བསྔལ་པའོ། །

[Block 3798]
བདག་གིར་ལྟ་བའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་སྟོང་པའོ། །

[Block 3799]
བདག་ཏུ་ལྟ་བའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱི༌[^1494]བདག་མེད་པའོ། །

[Block 3800]
ས་བོན་གྱི་ཆོས་ཀྱི་ཚུལ་གྱི༌[^1495]རྒྱུའོ། །

[Block 3801]
འབྱུང་བའི་ཚུལ་གྱིས་ཀུན་འབྱུང་བའོ། །

[Block 3802]
འབྲེལ་བའི་ཚུལ་གྱིས་རབ་ཏུ་སྐྱེ་བའོ། །

[Block 3803]
མངོན་པར་འགྲུབ་པའི་དོན་གྱིས་རྐྱེན་ནོ། །

[Block 3804]
ཕུང་པོ་ཞིག་པའི་ཕྱིར་འགོག་པའོ། །

[Block 3805]
མེ་གསུམ་ཞི་བའི་ཕྱིར་ཞི་བའོ། །

[Block 3806]
འཚེ་བ་མེད་པའི་ཕྱིར་གྱ་ནོམ་པའོ། །

[Block 3807]
སྐྱོན་ཐམས་ཅད་དང་བྲལ་བའི་ཕྱིར་ངེས་པར་འབྱུང་བའོ། །

[Block 3808]
བགྲོད་པར་བྱ་བའི་དོན་གྱིས་ན་ལམ་མོ། །

[Block 3809]
རིགས་པ་དང་ལྡན་པའི་ཕྱིར་རིགས༌[^1496]པའོ། །

[Block 3810]
ཡང་དག་པར་བསྒྲུབ་པའི་དོན་གྱིས་སྒྲུབ༌[^1497]པའོ། །

[Block 3811]
ཤིན་ཏུ་ཡང་དག་པར་འདའ་བར་བྱེད་པའི་ཕྱིར་ངེས་པར་འབྱིན་པའོ། །

[Block 3812 [HEADING]]
#### རྣམ་པ་ཤེས་རབ། ^7-3-2-0

[Block 3813]
རྣམ་པ་ཞེས་བྱ་བའི་ཆོས་འདི་ཅི་ཞེ་ན། རྣམ་པ་ཤེས་རབ། ཡང་ཅི་ཤེས་རབ་ཁོ་ནས་འཛིན་པར་བྱེད་དམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 3814]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། དང་བཅས་པའི། དམིགས་པ་དང་བཅས་པར་འཛིན་པར་བྱེད། ཤེས་རབ་དང་། གཞན་ཡང་དམིགས་པ་དང་བཅས་པའི་ཆོས་རྣམས་ཀྱིས་འཛིན་པར་བྱེད་དོ། །

[Block 3815]
ཡོད་པ་ཐམས་ཅད་གཟུང་བྱ་ཡིན། །གང་ཅི་ཡོད་ཀྱང་རུང་ཐམས་ཅད་གཟུང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 3816 [HEADING]]
### ཤེས་པ་བཅུ་པོ་རྣམས་ཀྱི་དབྱེ་བ། ^7-4-0

[Block 3817 [HEADING]]
#### དགེ་བ་ལ་སོགས་པ། ^7-4-1-0

[Block 3818]
ཤེས་པ་བཅུ་པོ་རྣམས་ཀྱི༌[^1498]དགེ་བ་ལ་སོགས་པའི་དབྱེ་བ་བརྗོད་དེ།

[Block 3819]
དང་པོ་རྣམ་གསུམ། དགེ་བ་དང་མི་དགེ་བ་དང་། ལུང་མ་བསྟན་ནོ། །

[Block 3820]
གཞན་རྣམས་དགེ །ཤེས་པ་དགུ་པོ་ནི་དགེ་བ་ཁོ་ན་ཡིན་ནོ། །
--- END BLOCKS ---
