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
[Block 3711]
འགོག་པ་དང་། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དག་ལས་གཞན་པའི་ཤེས་པ་རྣམས་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་ཆར་ཡིན་ནོ། །

[Block 3712 [HEADING]]
#### ཤེས་པའི་དམིགས་པ་ཤེས་པ། ^4-7-5-0

[Block 3713]
ཤེས་པ་གང་གིས་དམིགས་པ༌[^2582]ཤེས་པ་དུ་ཞིག་ཡིན་ཞེ་ན། [^2583]ཆོས་བློའི་སྤྱོད་ཡུལ་དགུ་ཡིན་ནོ། །

[Block 3714]
ཆོས་ཤེས་པའི༌[^2584]དམིགས་པ༌[^2585]ནི་ཤེས་པ་དགུ་ཡིན་ཏེ། རྗེས་སུ་ཤེས་པ་མ་གཏོགས་སོ། །

[Block 3715]
ལམ་རྗེས་བློ་ཡི་དགུ་ཡིན་ནོ། །

[Block 3716]
རྗེས་སུ་ཤེས་པའི་དམིགས་པ་ཡང་ཤེས་པ་དགུ༌[^2586]ཡིན་ཏེ། ཆོས༌[^2587]ཤེས་པ་མ་གཏོགས་སོ། །

[Block 3717]
ལམ་ཤེས་པའི་དམིགས་པ་ཡང་དགུ་ཡིན་ཏེ། ཀུན་རྫོབ་ཤེས་པ་མ་གཏོགས་སོ། །

[Block 3718]
སྡུག་བསྔལ་རྒྱུ་བློའི་གཉིས་ཡིན་ནོ། སྡུག་བསྔལ་དང་ཀུན་འབྱུང་ཤེས་པ་དག་གི༌[^2588]དམིགས་པ་དག༌[^2589]ནི་གཉིས་ཏེ། ཀུན་རྫོབ་དང་གཞན་གྱི་སེམས་ཤེས་པ་ཡིན་ནོ། །

[Block 3719]
བཞི་ཡི་བཅུ་ཡིན། ཀུན་རྫོབ་ཤེས་པ་དང་། གཞན་གྱི་སེམས་ཤེས་པ་དང་། ཟད་པ་ཤེས་པ་དང་། མི་སྐྱེ་བ་ཤེས་པ་རྣམས་ཀྱི་དམིགས་པ་ནི་ཤེས་པ་བཅུ་ཆར་ཡང༌[^2590]ཡིན་ནོ། །

[Block 3720]
གཅིག་གི་མིན། འགོག་པ་ཤེས་པ་ནི༌[^2591]གཅིག་པུའི་དམིགས་པ་ནི་ཤེས་པ༌[^2592]མ་ཡིན་པ་ཉིད་དོ། །

[Block 3721 [HEADING]]
#### ཆོས་བཅུ་སྦྱར་བ། ^4-7-6-0

[Block 3722]
ཆོས་བཅུ་དག་ནི་སྦྱར་བར་བྱ། བཅུ་གང་དག་ཅེ་ན།

[Block 3723 [VERSE]]
ཁམས་གསུམ་པ་དང་དྲི་མེད་ཆོས། །
འདུས་མ་བྱས་རྣམས་གཉིས་གཉིས་སོ། །

[Block 3724]
ཆོས་འདུས་བྱས་རྣམས་ལ་འདོད་པ་དང་། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་དང་། ཟག་པ་མེད་པ་རྣམས་མཚུངས་པར་ལྡན་པ་དང་ལྡན་པ་མ་ཡིན་པའི་བྱེ་བྲག་གིས་རྣམ་པ་བརྒྱད་དུ་བྱའོ། །

[Block 3725]
འདུས་མ་བྱས་རྣམས་ལ་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པའི་བྱེ་བྲག་གིས་རྣམ་པ་གཉིས་སུ་བྱའོ། །

[Block 3726]
ཆོས་བཅུ་པོ་འདི་དག་ཇི་ལྟར་སྦྱར་བར་བྱ་ཞེ་ན། ཤེས་པ་གང་གིས་དམིགས་པ་དུ་ཞིག་ཡིན་ཞེས་སྦྱར་བར་བྱ་སྟེ། དེ་ལ་ཀུན་རྫོབ་ཤེས་པའི་དམིགས་པ་ནི༌[^2593]ཆོས་བཅུ་པོ་ཐམས་ཅད་ཡིན་ནོ། །

[Block 3727]
ཆོས་ཤེས་པ་ནི་ལྔ་སྟེ། འདོད་པ་ན་སྤྱོད་པ་དང་། ཟག་པ་མེད་པ་དང་། གཞི་དང་། འདུས་མ་བྱས་དགེ་བ་ཡིན་ནོ། །

[Block 3728]
རྗེས་སུ་ཤེས་པ༌[^2594]ནི་བདུན་ཏེ། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་དང་། ཟག་པ་མེད་པ་དང་། དྲུག་དང་། འདུས་མ་བྱས་དགེ་བ་ཡིན་ནོ། །

[Block 3729]
སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་ཤེས་པ་དག་གི་ནི་དྲུག་སྟེ། འདོད་པ་དང་། གཟུགས་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པ་རྣམས་ཡིན་ནོ། །

[Block 3730]
འགོག་པ་ཤེས་པའི་ནི་གཅིག་སྟེ། འདུས་མ་བྱས་དགེ་བ༌[^2595]ཁོ་ན༌[^2596]ཡིན་ནོ། །

[Block 3731]
ལམ་ཤེས་པའི་ནི་གཉིས་ཏེ། ཟག་པ་མེད་པ་དག་ཡིན་ནོ། །

[Block 3732]
གཞན་གྱི་སེམས་ཤེས་པའི་ནི་གསུམ་སྟེ། འདོད་པ་དང་། གཟུགས༌[^2597]ན་སྤྱོད་པ་དང་། ཟག་པ་མེད་པ་དང་མཚུངས་པར་ལྡན་པ་རྣམས་ཡིན་ནོ། །

[Block 3733]
ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་དག་གི་དམིགས་པ་ནི་ཆོས་དགུ་ཡིན་ཏེ། འདུས་མ་བྱས་ལུང་དུ་མ་བསྟན་པ་མ་གཏོགས་སོ། །

[Block 3734 [HEADING]]
#### ཤེས་པ་གཅིག་གིས་ཆོས་ཐམས་ཅད་ཤེས་པ། ^4-7-7-0

[Block 3735]
ཤེས་པ་གཅིག་གིས་ཆོས་ཐམས་ཅད་ཤེས་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན། མེད་དོ། །

[Block 3736]
འོན་ཀྱང་།

[Block 3737 [VERSE]]
ཀུན་རྫོབ་གཅིག་པུས་རང་ཚོགས་ལས། །
གཞན་ནི་བདག་མེད་ཉིད་རིགས་འགྱུར། །

[Block 3738]
ཀུན་རྫོབ་ཤེས་པས་ནི་རང་གི་ཚོགས་ལས་གཞན་པའི་ཆོས་ཐམས་ཅད་ནི་བདག་མེད་པའོ་ཞེས་བདག་མེད་པ་ཉིད་དུ་ཤེས་པར་འགྱུར་རོ། །

[Block 3739]
དེའི་རང་གི་ཚོགས་ནི་རང་གི་ངོ་བོ་དང་དེ་དང་ལྷན་ཅིག་ཏུ་འབྱུང་བའི་ཆོས་རྣམས་ཡིན་ཏེ། [^2598]དེ་དག་ནི་ཡུལ་དང་ཡུལ་ཅན༌[^2599]ཐ་དད་པའི་ཕྱིར་དང་། དམིགས་པ་གཅིག་པའི་ཕྱིར་དང་། ཧ་ཅང་ཉེ་བའི་ཕྱིར་མི་འཛིན་ཏོ། །

[Block 3740]
དེ་ཡང་འདོད་པ་ན་སྤྱོད་པ་ནི་ཐོས་པ་དང་། བསམ་པ་ལས་བྱུང་བ་ཡིན་ནོ། །

[Block 3741]
གཟུགས་ན་སྤྱོད་པ་ནི་ཐོས་པ་ལས་བྱུང་བ་ཡིན་ནོ། །

[Block 3742]
བསྒོམ་པ་ལས་བྱུང་བ་ནི་མ་ཡིན་ཏེ། [^2600]དེ་ནི་ས་རྣམ་པར་ཆད་པ་ལས་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3743]
དེ་ལྟ་མ་ཡིན་ན་ཐམས་ཅད་ལས་ཅིག་ཅར་འདོད་ཆགས་དང་བྲལ་བར་འགྱུར་རོ། །

[Block 3744]
འདི་ནི་རྫོགས་སོ།། །།

[Block 3745 [HEADING]]
### ཤེས་པ་དུ་དང་ལྡན་པ། ^4-8-0

[Block 3746]
གང་ཞིག་ཤེས་པ་དུ་དང་ལྡན། །ཞེས་བྱ་བ་འདི་བརྗོད་པར་བྱ་སྟེ། རེ་ཞིག་སོ་སོའི་སྐྱེ་བོ་ནི་ཀུན་རྫོབ་ཤེས་པ་གཅིག་པུ་དང་ལྡན་ནོ། །

[Block 3747]
འདོད་ཆགས་དང་བྲལ་བ་ཞིག་ཡིན་ན་ནི་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དང་ཡང་ལྡན་ནོ། །

[Block 3748]
འཕགས་པ་ནི།

[Block 3749 [VERSE]]
ཟག་མེད་སྐད་ཅིག་དང་པོ་ལ། །
ཆགས་ཅན་ཤེས་པ་གཅིག་དང་ལྡན། །

[Block 3750]
འདོད་པ་ལས་འདོད་ཆགས་དང་མ་བྲལ་བ་ཞིག་ཡིན་ན། སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་ལ་ཀུན་རྫོབ་ཤེས་པ་གཅིག་ཁོ་ན་དང་ལྡན་པ་ཡིན་ནོ། །
--- END BLOCKS ---
