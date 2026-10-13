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

[Block 3821 [HEADING]]
#### ས། ^7-4-2-0

[Block 3822]
དངོས་པོ༌[^1499]ས་རྣམས་ཐམས༌[^1500]ཅད་ན་འདོད་པའི་ཁམས་ནས་སྲིད་པའི་རྩེ་མོའི་བར་རོ། །

[Block 3823]
དྲུག་ན༌[^1501]ཆོས་ཤེས་བྱ། བསམ་གཏན་བཞི་དང་། མི་ལྕོགས་པ༌[^1502]མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་ནའོ། །

[Block 3824]
དགུ་ན། རྗེས་ཤེས༌[^1503]བྱ་བ། དྲུག་ལ་གཟུགས་མེད་པ་གསུམ་བསྣན་ནས་སོ། །

[Block 3825]
དེ་བཞིན་དྲུག །སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་དང་། འགོག་པ་དང་། ལམ་དང་། ཟད་པ་དང་། མི་སྐྱེ་བ་ཤེས་པ་རྣམས་ཀྱང་ས་དགུ་པོ་དེ་དག་ཉིད་ནའོ། །

[Block 3826]
གཞན་ཡིད་ཤེས་པ་བསམ་གཏན་བཞི། །ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ནི་བསམ་གཏན་བཞི་ནའོ། །

[Block 3827 [HEADING]]
#### རྟེན། ^7-4-3-0

[Block 3828]
དེ་ནི་འདོད་དང་གཟུགས་རྟེན༌[^1504]ཅན། །འདོད་པ་དང་གཟུགས་ཀྱི་ཁམས་སུ་དེ་མངོན་སུམ་དུ་བྱེད་དོ། །

[Block 3829 [VERSE]]
ཆོས་ཤེས་བྱ་བ་འདོད་རྟེན་ཅན། །
ཁམས་གསུམ་པ་ཡིན་རྟེན་ཅན་གཞན། །

[Block 3830]
ཕ་རོལ་གྱི་སེམས་དང་། ཆོས་ཤེས་པ་མ་གཏོགས་པ་ཁམས་གསུམ་དུ་མངོན་སུམ་དུ་བྱེད་དོ། །

[Block 3831]
ས་དང་རྟེན༌[^1505]བཤད་ཟིན་ཏོ། །

[Block 3832 [HEADING]]
#### དྲན་པ་ཉེ་བར་གཞག་པ། ^7-4-4-0

[Block 3833]
དྲན་པ་ཉེ་བར་གཞག་པའི་བསྡུས་པ་བརྗོད་པར་བྱ་སྟེ། འགོག་བློ་དྲན་པ་ཉེར་གཞག་པ། །གཅིག་སྟེ། འགོག་པ་ཤེས་པ་གཅིག་ནི་ཆོས་དྲན་པ་ཉེ་བར་གཞག་པའོ། །

[Block 3834]
ཕ་རོལ་སེམས་བློ་ནི། གསུམ་མོ། །

[Block 3835]
ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ནི་གསུམ་སྟེ། ཚོར་བ་དང་། སེམས་དང་། ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་ཡིན་ནོ། །

[Block 3836]
ལྷག་མ་བཞི་ཡིན་ནོ། །

[Block 3837]
འགོག་པ་དང་། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དག་ལས་གཞན་རྣམས་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་ཆར༌[^1506]རོ། །

[Block 3838 [HEADING]]
#### ཤེས་པ་གང་གི་དམིགས་པ་ཤེས་པ་དུ། ^7-4-5-0

[Block 3839]
ཤེས་པ་གང་གི་དམིགས་པ་ཤེས་པ་དུ་ཡིན་ཞེ་ན།

[Block 3840 [VERSE]]
ཆོས་བློའི་སྤྱོད་ཡུལ་དགུ་ཡིན་ནོ། །
རྗེས་སུ་ཤེས་པ་མ་གཏོགས་པའོ། །
ལམ་རྗེས་བློ་ཡི་དགུ་ཡིན་ནོ། །
གོ་རིམས་བཞིན་དུ་ཀུན་རྫོབ་དང་། །

[Block 3841]
ཆོས་ཤེས་པ་ལས་གཞན་པའོ། །

[Block 3842]
སྡུག་བསྔལ་རྒྱུ་བློའི་གཉིས་ཡིན་ནོ། །

[Block 3843]
ཀུན་རྫོབ་དང་། གཞན་གྱི་སེམས་ཤེས་པ་དག་གོ། །

[Block 3844]
བཞི་ཡི་བཅུ་ཡིན། ཀུན་རྫོབ་དང་། གཞན་གྱི་སེམས་ཤེས་པ་དང་། ཟད་པ་དང་། མི་སྐྱེ་བ་ཤེས་པ་རྣམས་ཀྱི་དམིགས་པ་བཅུ་ཀའོ། །

[Block 3845]
གཅིག་གི་མིན། འགོག་པ་ཤེས་པའི་དམིགས་པ་ནི་ཤེས་པ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 3846 [HEADING]]
#### ཆོས་བཅུ་སྦྱར་བ། ^7-4-6-0

[Block 3847]
ཆོས་བཅུ་དག་ནི་སྦྱར་བར་བྱ། །བཅུ་གང་ཞེ་ན།

[Block 3848 [VERSE]]
ཁམས་གསུམ་པ་དང་དྲི་མེད་ཆོས། །
འདུས་མ་བྱས་རྣམས་གཉིས་གཉིས་སོ། །

[Block 3849]
ཆོས་འདུས་མ་བྱས་རྣམས་ལ་འདོད་པ་དང་། གཟུགས་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པ་དང་། ཟག་པ་མེད་པ་རྣམས་མཚུངས་པར་ལྡན་པ་དང་། ལྡན་པ་མ་ཡིན་པའི་བྱེ་བྲག་གིས་རྣམ་པ་བརྒྱད་དུ་བྱའོ། །

[Block 3850]
འདུས་མ་བྱས་རྣམས་ལ་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པའི་བྱེ་བྲག་གིས་རྣམ་པ་གཉིས་སུ་བྱའོ། །

[Block 3851]
ཆོས་བཅུ་པོ་འདི་དག་ཇི་ལྟར་སྦྱར་བར་བྱ་ཞེ་ན། ཤེས་པ་གང་གི་དམིགས་པ་དུ་ཞིག་ཡིན་ཞེས་སྦྱར་བར་བྱ་ཞེ་ན། དེ་ལ་ཀུན་རྫོབ་ཤེས་པའི་དམིགས་པ་ནི་ཆོས་བཅུ་པོ་ཐམས་ཅད་ཡིན་ནོ། །

[Block 3852]
ཆོས་ཤེས་པའི་ནི་ལྔ་སྟེ། འདོད་པ་ན་སྤྱོད་པ་དང་། ཟག་པ་མེད་པ་བཞི་དང་། འདུས་མ་བྱས་དགེ་བ་ཡིན་ནོ། །

[Block 3853]
རྗེས་སུ་ཤེས་པ་ནི་བདུན་ཏེ། གཟུགས་དང་། གཟུགས་མེད་པ་ན༌[^1507]སྤྱོད་པ་དང་། ཟག་པ་མེད་པ་དྲུག་དང་། འདུས་མ་བྱས་དགེ་བ་ཡིན་ནོ། །

[Block 3854]
སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་ཤེས་པ་དག་གི་ནི་དྲུག་སྟེ། འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་རྣམས་སོ། །

[Block 3855]
འགོག་པ་ཤེས་པ་ནི་གཅིག་སྟེ།
--- END BLOCKS ---
