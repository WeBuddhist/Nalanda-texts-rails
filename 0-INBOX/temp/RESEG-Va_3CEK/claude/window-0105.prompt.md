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
[Block 3676]
སྡུག་བསྔལ་ལ་ཐར་པ་ཡིན་ནོ་སྙམ་དུ་ལྟ་བ་སྤྱད་པ་རྣམས་ཀྱི་གཉེན་པོར་ཞི་བའི་རྣམ་པ་ཡིན་ནོ། །

[Block 3677]
བསམ་གཏན་གྱི་བདེ་བ་གྱ་ནོམ་པ་ཡིན་པར་ལྟ་བ་སྤྱད་པ་རྣམས་ཀྱི་གཉེན་པོར་གྱ་ནོམ་པ་ཡིན་ནོ། །

[Block 3678]
ཡང་དང་ཡང་ཡོངས་སུ་ཉམས་པར་འགྱུར་བའི་སྒོ་ནས་ཐར་པ་ནི་གཏན་དུ་མ་ཡིན་ནོ་སྙམ་དུ་ལྟ་བ་སྤྱད་པ་རྣམས་ཀྱི་གཉེན་པོར་ངེས་པར་འབྱུང་བའི་རྣམ་པ་ཡིན་ནོ། །

[Block 3679]
ལམ་མེད་དོ་སྙམ་པ་དང་། ལམ་འདི་ཡིན་ནོ་སྙམ་པ་དང་། གཞན་ཡང་ལམ་ཡིན་ནོ་སྙམ་པ་དང་། ལམ་འདི་ཡང་ལྷག༌[^2566]གོ་སྙམ་དུ་ལྟ་བར༌[^2567]སྤྱད་པ་རྣམས་ཀྱི༌[^2568]གཉེན་པོར་གོ་རིམས་བཞིན་དུ་ལམ་དང་། རིགས་པ་དང་། སྒྲུབ་པ་དང་། ངེས་པར་འབྱིན་པའི་རྣམ་པ་དག་ཡིན་ནོ། །

[Block 3680 [HEADING]]
### རྣམ་པ་ཞེས་བྱ་བའི་ཆོས། ^4-6-0

[Block 3681]
རྣམ་པ་ཞེས་བྱ་བའི་ཆོས་འདི་ཅི་ཞེ་ན། རྣམ་པ་ཤེས་རབ། དེ་ལྟ་ན་ནི་འོ་ན་ཤེས་རབ་གཞན་དང་མཚུངས་པར་མི་ལྡན་པའི་ཕྱིར། ཤེས་རབ་རྣམ་པ་དང་བཅས་པར་མི་འགྱུར་གྱི། འདི་ལྟར་རྣམ་པ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བ་ཐམས་ཅད་ཀྱི་དམིགས་པ་འཛིན་པའི་བྱེ་བྲག་ནི༌[^2569]རྣམ་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རིགས་པར་འགྱུར་རོ། །

[Block 3682]
ཡང་ཅི་ཤེས་རབ་ཁོ་ནས་འཛིན་པར་བྱེད་དམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 3683]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། དེ་དང་བཅས་པའི་དམིགས་པ་དང་བཅས་པས་འཛིན་པར་བྱེད། ཤེས་རབ་དང་། དམིགས་པ་དང་བཅས་པའི་ཆོས་གཞན་ཐམས་ཅད་ཀྱིས་ཀྱང་འཛིན་པར་བྱེད་དོ། །

[Block 3684]
ཡོད་པ་ཐམས་ཅད་གཟུང་བྱ་ཡིན།[^2570] །གང་ཅི་ཡོད་ཀྱང་རུང་ཐམས་ཅད་གཟུང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 3685]
དེ་ལྟར་བྱས་ན་ཤེས་རབ་ནི་རྣམ་པ་ཡང་ཡིན། འཛིན་པར་བྱེད་པ་ཡང་ཡིན། གཟུང་བར་བྱ་བ་ཡང་ཡིན་ནོ། །

[Block 3686]
དམིགས་པ་དང་བཅས་པ་གཞན་ནི་འཛིན་པར་བྱེད་པ་དང་། གཟུང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 3687]
དམིགས་པ་མེད་པ་རྣམས་ནི་གཟུང་བར་བྱ་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 3688 [HEADING]]
### ཤེས་པ་བཅུ་པོའི་དགེ་བ་ལ་སོགས་པའི་བྱེ་བྲག། ^4-7-0

[Block 3689]
འདི་མན་ཆད་ནི་ཤེས་པ་བཅུ་པོ་འདི་དག་གི་དགེ་བ་ལ་སོགས་པའི་བྱེ་བྲག་བསྟན་པར་བྱ་སྟེ།

[Block 3690 [HEADING]]
#### དགེ་བ་ལ་སོགས་པ། ^4-7-1-0

[Block 3691]
དང་པོ་རྣམ་གསུམ་གཞན་རྣམས་དགེ །ཀུན་རྫོབ་ཤེས་པ་ནི་ཚིགས་སུ་བཅད་པའི་དང་པོ་ནི༌[^2571]ཡོད་པའི་ཕྱིར་དང་པོ་སྟེ། དེ་ནི༌[^2572]དགེ་བ་དང་མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པ་དང་རྣམ་པ་གསུམ་ཡིན་ནོ། །ཤེས་པ་གཞན་དགུ་ནི་དགེ་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 3692 [HEADING]]
#### ས། ^4-7-2-0

[Block 3693]
དང་པོ་ས་རྣམས་ཐམས་ཅད་ན། འདོད་པའི་ཁམས་ནས་སྲིད་པའི་རྩེ་མོའི་བར་ན་ཡོད་དོ། །

[Block 3694]
དྲུག་ན་ཆོས་ཤེས་བྱ། ཆོས་ཤེས་པ་ནི་བསམ་གཏན་བཞི་དང་། མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་ན་ཡོད་དོ། །

[Block 3695]
དགུ་ན་རྗེས་ཤེས་བྱ་བ། རྗེས་སུ་ཤེས་པ་ནི་ས་དྲུག་པོ་དེ་དག་ཉིད་དང་གཟུགས་མེད་པ་གསུམ་ན་ཡོད་དོ། །

[Block 3696]
དེ་བཞིན་དུ་དྲུག །སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་དང་། འགོག་པ་དང་། ལམ་དང་། ཟད་པ་དང་། མི་སྐྱེ་བ་ཤེས་པ་རྣམས་ཀྱང་བྱེ་བྲག་མེད་པར་ནི་ས་དགུ་པོ་དེ་དག་ཉིད་ན་ཡོད་དོ། །

[Block 3697]
དབྱེ་བ༌[^2573]ནི་ཆོས་ཤེས་པས་བསྡུས་པ་རྣམས་ནི་ས་དྲུག་ན་ཡོད་དོ། །

[Block 3698]
རྗེས་སུ་ཤེས་པས་བསྡུས་པ་རྣམས་ནི་ས་དགུ་ན་ཡོད་དོ། །

[Block 3699]
[^2574]གཞན་ཡིད་ཤེས་པ་བསམ་གཏན་བཞི། །ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ནི་བསམ་གཏན་བཞི་ཁོ་ན་ན༌[^2575]ཡོད་ཀྱི་གཞན་ན་མེད་དོ། །

[Block 3700 [HEADING]]
#### རྟེན། ^4-7-3-0

[Block 3701]
དེ་ན༌[^2576]འདོད་དང་གཟུགས་རྟེན་ཅན། །ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དེ་ནི་འདོད་པ་དང་གཟུགས་ཀྱི་ཁམས་དག་ཏུ་མངོན་སུམ་དུ་བྱེད་དོ། །

[Block 3702]
ཆོས་ཤེས་བྱ་བ་འདོད་རྟེན་ཅན། །ཆོས་ཤེས་པ་ནི་འདོད་པའི༌[^2577]ཁམས་ཀྱི་རྟེན་ཅན་ཁོ་ན་ཡིན་གྱི། གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དག་ཏུ་ནི་མངོན་སུམ་དུ་མི་བྱེད་དོ། །

[Block 3703]
ཁམས་གསུམ་པ་ཡི་རྟེན་ཅན་གཞན། །གཞན་གང་ཞེ་ན། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དང་། ཆོས་ཤེས་པ་མ་གཏོགས་པའོ། །

[Block 3704]
ས་དག༌[^2578]དང་རྟེན་བཤད་ཟིན་ཏོ། །

[Block 3705 [HEADING]]
#### དྲན་པ་ཉེ་བར་གཞག་པ། ^4-7-4-0

[Block 3706]
དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་ཀྱིས་བསྡུས་པ་བརྗོད་པར་བྱ་སྟེ། དེ་སྨྲས་པ། འགོག་བློ་དྲན་པ་ཉེར་གཞག་པ།[^2579] །གཅིག་སྟེ་བློ་དང་ཤེས་རབ་དང་། །ཤེས་པ་ཞེས་བྱ་བ་ནི་རྣམ་གྲངས་ཡིན་ནོ། །

[Block 3707]
འགོག་པ་ཤེས་པ་ནི་གཅིག་སྟེ། ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་ཡིན་ནོ། །

[Block 3708]
ཕ་རོལ་གྱི༌[^2580]སེམས་བློ་ནི་གསུམ་མོ། །

[Block 3709]
ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ནི་གསུམ་སྟེ།[^2581] ཚོར་བ་དང་། སེམས་དང་། ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་ཡིན་ནོ། །

[Block 3710]
ལྷག་མ་བཞི་ཡིན་ནོ། །

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
--- END BLOCKS ---
