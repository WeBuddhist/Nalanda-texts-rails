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
[Block 3536]
མི་སྐྱོ་ལུང་ལས་འདིར་རྩོམ་ཞིང་། དེར་མཐར་ཕྱིན་ཞེས་འབྱུང་ཕྱིར་རོ། །

[Block 3537]
གཟུགས་ན་སྤྱོད་པའི་སོ་སོའི་སྐྱེ་བོ་རྣམས་ནི་སྙོམས་པར་འཇུག་པའི་བདེ་བ་ལ་ཆགས་པའི་ཕྱིར་དང་། ཀུན་དུ་མི་སྐྱོ་བའི་ཕྱིར་རོ། །

[Block 3538]
ཕྱིར་མི་འོང་བ༌[^1398]ལྔ་ནི་འདི༌[^1399]རྩོམ་པ་ནི་ལམ་རྩོམ་པ་སྟེ་དེར་མཐར་ཕྱིན་པར་འགྱུར་རོ། །

[Block 3539]
དེ་བས་ན་དེ་ལ་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་མེད་དེ།[^1400] །འདི་སྐད་དུ།

[Block 3540 [VERSE]]
གལ་ཏེ་མི་གཡོའི་ཟད་ཤེས་ལས། །
མི་སྐྱེའི་བློ་གྲོས་ཞེས་བཤད་དེ། །

[Block 3541 [HEADING]]
#### དགྲ་བཅོམ་དྲུག། ^6-2-6-0

[Block 3542]
ཅི་དགྲ་བཅོམ་པ་ལ་ཡང་དབྱེ་བ་ཡོད་དམ་ཞེ་ན། སྨྲས་པ། ཡོད་དེ། དགྲ་བཅོམ་དྲུག་འདོད། །

[Block 3543 [VERSE]]
ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་དང་། །
འཆི་བར་སེམས་པའི་ཆོས་ཅན་དང་། །
རྗེས་སུ་བསྲུང་བའི་ཆོས་ཅན་དང་། །
གནས་པ་ལས་མི་བསྐྱོད་པ་དང་། །

[Block 3544]
རྟོགས་པའི་སྐལ་བ་ཅན་དང་། མི་གཡོ་བའི་ཆོས་ཅན་ནོ། །

[Block 3545]
དེ་དག་ལས།

[Block 3546 [VERSE]]
ལྔ་ནི་དད་པའི་མོས་ལས་སྐྱེས། །
མི་གཡོ་བའི་ཆོས་ཅན་མ་གཏོགས་པའོ། །
དེ་དག་རྣམ༌[^1401]གྲོལ་དུས་དང་སྦྱོར། །

[Block 3547]
ལྔ་པོ་དེ་དག་གི་རྣམ་པར་གྲོལ་བ་ནི་དུས་དང་སྦྱོར་བས་ཕངས་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ།

[Block 3548 [VERSE]]
རྟག་ཏུ་རྗེས་སུ་སྲུང་བའི་ཕྱིར་རོ། །
མི་གཡོའི་ཆོས་ཅན་མི་གཡོ་བ། །

[Block 3549]
ཡོངས་སུ་ཉམས་པའི་སྒོ་ནས་གཡོ་བར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 3550]
དེའི་ཕྱིར༌[^1402]དེ་དུས་མི་སྦྱོར་གྲོལ། །དེ་ཉིད་ཀྱི་ཕྱིར་དེ་ནི་དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བ་ཞེས་བྱ་སྟེ། ཡོངས་སུ་ཉམས་པ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 3551]
དེ་ནི་མཐོང་ཐོབ་རྒྱུ་ལས་བྱུང་། །མི་གཡོ་བའི་ཆོས་ཅན་དེ་ནི་མཐོང་བས་ཐོབ་པ་སྔོན་དུ་འགྲོ་བ་ཡིན་པར་རིག་པར་བྱ་སྟེ། ཅི་དགྲ་བཅོམ་པ་འདི་དག་དང་པོ་ཁོ་ན་ནས་དེ་དག་གི་རིགས་ཅན་ཞིག༌[^1403]ཡིན་ནམ། འོན་ཏེ་ཕྱིས་ཡིན་ཞེ་ན།

[Block 3552 [VERSE]]
ཁ་ཅིག་དང་པོ་ནས་དེའི་རིགས།
ཁ་ཅིག་སྦྱངས་པ་ལས་གྱུར་ཏོ། །

[Block 3553]
ཁ་ཅིག་ནི་དང་པོ་ཉིད་ནས་ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་གྱི་རིགས་ཅན་ཡིན་ལ། ཁ་ཅིག་ནི་ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་དུ་གྱུར་པ་ལས་དབང་པོ་རྣམས་སྦྱངས་པས་འཆི་བར་སེམས་པའི་ཆོས་ཅན་དུ་གྱུར་པ་ཡིན་ཏེ། མི་གཡོ་བའི་ཆོས་ཅན་གྱི་བར་དུ་ཡང་དེ་དང་འདྲའོ། །

[Block 3554]
དེ་ལ་ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་ནི་ཡོངས་སུ་ཉམས་པར་འགྱུར་བའི་སྐལ་བ་དང་ལྡན་གྱི་འཆི་བར་སེམས་པའི་ཆོས་ཅན་ལ་སོགས་པ་ནི་མ་ཡིན་པ་གང་ཡིན་པའོ། །

[Block 3555]
འཆི་བར་སེམས་པའི་ཆོས་ཅན་ནི་འཆི་བར་སེམས་པར་གྱུར་པའི་སྐལ་བ་ཅན་གང་ཡིན་པའོ། །

[Block 3556]
རྗེས་སུ་སྲུང་བའི་ཆོས་ཅན་ནི་རྗེས་སུ་སྲུང་བའི་སྐལ་བ་ཅན་གང་ཡིན་པའོ། །

[Block 3557]
གནས་པ་ལས་མི་བསྐྱོད་པ༌[^1404]ནི་ཡོངས་སུ་ཉམས་པར་འགྱུར་བའི་རྐྱེན་སྟོབས་དང་ལྡན་པ་མེད་ན་རྗེས་སུ་མ་བསྲུངས་ཀྱང་གནས་པར་འགྱུར་བའི་སྐལ་བ་ཅན་ཡིན་ཞིང་ཉམས་པར་མི་འགྱུར་བ་དང་། མངོན་པར་བརྩོན་པ་མེད་ན་འཕེལ་བར་ཡང་མི་འགྱུར་བའི་སྐལ་བ་ཅན་གང་ཡིན་པའོ། །

[Block 3558]
རྟོགས་པའི་སྐལ་བ་ཅན་ནི་མི་གཡོ་བ༌[^1405]རྟོགས་པར་འགྱུར་བའི་སྐལ་བ་ཅན་གང་ཡིན་པའོ། །

[Block 3559]
མི་གཡོ་བའི་ཆོས་ཅན་ནི་ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་བའི་སྐལ་བ་ཅན་གང་ཡིན་པའོ། །

[Block 3560]
འདི་དག་གང་ཞིག༌[^1406]གང་ལས་ཡོངས་སུ་ཉམས་ཤེ་ན། བཞི་ནི་རིགས་ལས་ལྔ་འབྲས་ལས། །

[Block 3561]
ཉམས་འགྱུར། འཆི་བར་སེམས་པའི་ཆོས་ཅན་ལ་སོགས་པ་བཞི་ནི་རིགས་ལས་ཡོངས་སུ་ཉམས་པར་འགྱུར་རོ། །

[Block 3562]
ལྔ་ནི་འབྲས་བུ་ལས་སོ། །

[Block 3563]
དེ་དག་ཀྱང་།

[Block 3564]
དང་པོ་ལས་མ་ཡིན། གང་གི་རིགས་དང་པོ་གང་ཡིན་པ་དང་། གང་གི་འབྲས་བུ་དང་པོ་གང་ཡིན་པ་དེ་ལས་ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་རོ། །

[Block 3565]
ཅི་དགྲ་བཅོམ་པ་དེ་དག་ཁོ་ན་རིགས་དྲུག་དང་ལྡན་ནམ། འོན་ཏེ་གཞན་དག་ཀྱང་ཞེ་ན། སློབ་དང་འཕགས་མིན་རིགས་དྲུག་ལྡན། །སློབ་པ་དང་། སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱང་རིགས་དྲུག་དང་ལྡན་ནོ། །

[Block 3566]
གཞན་ཡང་། མཐོང་བ་ལ་ནི་འཕོ་བ་མེད། །མཐོང་བའི་ལམ་ལས་གཞན་པ་ལ་དབང་པོ་འཕོ་བ་ཡོད་དོ། །

[Block 3567]
དེ་ཡང་།

[Block 3568 [HEADING]]
#### ཡོངས་ཉམས་རྣམ་པ་གསུམ། ^6-2-7-0

[Block 3569 [VERSE]]
ཐོབ་དང་མ་ཐོབ་ཉེར་སྤྱད་ལས། །
ཡོངས་ཉམས་རྣམ་པ་གསུམ་ཤེས༌[^1407]བྱ། །

[Block 3570]
གལ་ཏེ་ཡོན་ཏན་ཐོབ་པ་ལས་ཡོངས་སུ་ཉམས་ན་ཐོབ་པ་ལས་ཡོངས་སུ་ཉམས་པ་ཡིན་ནོ། །

[Block 3571]
གལ་ཏེ་ཡོན་ཏན་ཐོབ་པར་བྱ་བ་མ་ཐོབ་ན་མ་ཐོབ་པ་ལས་ཡོངས་སུ་ཉམས་པའོ། །

[Block 3572]
གལ་ཏེ་ཡོན་ཏན་ཐོབ་པ་མངོན་སུམ་དུ་མི་བྱེད་ན་ཉེ་བར་སྤྱད་པ་ལས་ཡོངས་སུ་ཉམས་པའོ། །

[Block 3573]
ཡོངས་སུ་ཉམས་པ་འདི་རྣམས་ལས་ནི།

[Block 3574 [VERSE]]
སྟོན༌[^1408]ལ་ཐ་མ་མི་གཡོ་ལ། །
བར་མ་འང༌[^1409]གཞན་ལ་རྣམ་གསུམ་མོ། །

[Block 3575]
བཅོམ་ལྡན་འདས་ལ་ནི་ཉེ་བར་སྤྱད་པ་ལས་ཡོངས་སུ་ཉམས་པ་ཁོ་ན་མངའི་གཞན་ནི༌[^1410]མི་མངའོ། །
--- END BLOCKS ---
