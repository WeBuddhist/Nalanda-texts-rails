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
[Block 4656]
དེ་རྣམས་ལས།

[Block 4657]
[^3310] བརྒྱད་མ་ཆགས།

[Block 4658]
དང་པོ་བརྒྱད་ནི་མ་ཆགས་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 4659]
བསམ་གཏན་མཐའ་ན། བསམ་གཏན་བཞི་པ་ཁོ་ན་ན་ཡོད་དོ། །

[Block 4660]
སྤྱོད་ཡུལ་ནི། འདོད་པ། འདོད་པ་ན་སྤྱོད་པའི་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ཡིན་ནོ། །

[Block 4661]
ཁ་ཅིག་ན་རེ་རླུང་གི་ནི་རེག་བྱའི་སྐྱེ་མཆེད་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 4662]
དེ༌[^3311]གཉིས་ནི་གཟུགས་མེད་དག །ཟད་པར་གྱི་སྐྱེ་མཆེད་ཐ་མ་གཉིས་ནི་གཟུགས་མེད་པ་དག་པ་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 4663]
སྤྱོད་ཡུལ་རང་གི་ཕུང་པོ་བཞི། །འདི་གཉིས་ཀྱི་དམིགས་པ་ནི་རང་གི་ས་པའི་ཕུང་པོ་བཞི་ཡིན་ནོ། །

[Block 4664]
ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་རྣམས་ནི་རྣམ་པར་ཐར་པ་འཇུག་པ་ལས་བྱུང་བ་ཅན་ཡིན་ལ། ཟད་པར་གྱི༌[^3312]སྐྱེ་མཆེད་རྣམས་ནི་ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་འཇུག་པ་ལས་བྱུང་བ་ཅན་ཡིན་ཏེ། གོང་ནས་གོང་དུ་ཁྱད་པར་དུ་འཕགས་པའི་ཕྱིར་རོ། །

[Block 4665]
འགོག་པའི་རྣམ་པར་ཐར་པ་མ་གཏོགས་པ་རྣམ་པར་ཐར་པ་ལ་སོགས་པ་དེ་དག་ཐམས་ཅད་ནི་སོ་སོའི་སྐྱེ་བོ་དང་འཕགས་པའི་རྒྱུད་ལ་ཡོད་པ་དག་ཡིན་ནོ། །

[Block 4666 [HEADING]]
#### སྦྱོར་བ་ལས་བྱུང་བ་དང་འདོད་ཆགས་དང་བྲལ་བས་ཐོབ་པ། ^5-17-5-0

[Block 4667]
ཅི་རྣམ་པར་ཐར་པ་ལ་སོགས་པ་དེ་དག་སྦྱོར་བ་ལས་བྱུང་བ་ཡིན་ནམ་འདོད་ཆགས་དང་བྲལ་བས་ཐོབ་པ་ཡིན་ཞེས་བྱ་བའི་འདྲི་བ་འདི་ལ་འགོག་པ་བཤད་ཟིན། འགོག་པའི་རྣམ་པར་ཐར་པ་ནི་སྔར་རྣམ་པ་ཐམས་ཅད་དུ་བཤད་ཟིན་ཏོ། །

[Block 4668]
ལྷག་མ་ནི། འདོད་ཆགས་བྲལ་དང་སྦྱོར་བས་འཐོབ། །འགོག་པ་ལས་གཞན་པའི་རྣམ་པར་ཐར་པ་ལ་སོགས་པ་ནི་འདོད་ཆགས་དང་བྲལ་བས་ཐོབ་པ་ཡང་ཡིན་ལ་སྦྱོར་བ་ལས་བྱུང་བ་དག་ཀྱང༌[^3313]ཡིན་ཏེ།

[Block 4669 [VERSE]]
འདྲིས་པ་དང་མ་འདྲིས་པའི་ཕྱིར་རོ། །
གཟུགས་མེད་ཅེས་བྱ་ཁམས་གསུམ་གྱི། །
རྟེན་ཅན་ལྷག་མ་མི་ལས་སྐྱེ། །

[Block 4670]
གཟུགས་མེད་པའི་རྣམ་པར་ཐར་པ་དང་། གཟུགས་མེད་པའི་ཟད་པར་ནི་ཁམས་གསུམ་པའི་རྟེན་ཅན་དག་ཡིན་ནོ། །

[Block 4671]
ལྷག་མ་ནི་མིའི་རྟེན་ཅན་ཁོ་ན་ཡིན་ཏེ། ལུང་གི་མཐུས་སྐྱེད་པའི༌[^3314]ཕྱིར་རོ། །

[Block 4672 [HEADING]]
### རྒྱུ་དང་ལས་དང་ཆོས་ཉིད་ཀྱིས་སྙོམས་པར་འཇུག་པ་སྐྱེ་བ། ^5-18-0

[Block 4673]
ཇི་ལྟར་ན་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དག་ཏུ་གཟུགས་མེད་པ་དང་བསམ་གཏན་གྱི་ཁྱད་པར་སྐྱེ་ཞེ་ན། རྒྱུ་དང་ལས་དང་ཆོས་ཉིད་དང་། །རྒྱུ་གསུམ་གྱིས༌[^3315]བསམ་གཏན་དང་གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པ་རྣམས་སྐྱེ་སྟེ། དེ་ལ། ཁམས་གཉིས་དག་ཏུ་གཟུགས་མེད་པ། །རྒྱུ་དང་ལས་ཀྱི་སྟོབས་ཀྱིས་ཏེ།[^3316] །གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དག་ཏུ་གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པ་སྐྱེ་བ་རྒྱུའི་སྟོབས་ཀྱིས་ནི་ཉེ་བ་དང་ཡང་དང་ཡང་དུ་གོམས་པ་ལས་སོ། །

[Block 4674]
ལས་ཀྱི་སྟོབས་ཀྱིས་ནི་ས་གོང་མའི་ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཉེ་བར་གནས་པའི་ཕྱིར་ཏེ། འོག་མ་ལས་འདོད་ཆགས་དང་མ་བྲལ་བས་ནི་གོང་དུ་སྐྱེ་བར་མི་ནུས་སོ། །

[Block 4675]
གཟུགས་ཀྱི་ཁམས་སུ་བསམ་གཏན་རྣམས། །དེ་དག་དང་ཆོས་ཉིད་ཀྱིས་ཀྱང་། གཟུགས་ཀྱི་ཁམས་སུ་ནི་བསམ་གཏན་གཞན་རྒྱུ་དང་ལས་ཀྱི་སྟོབས་དེ་དག་དང་ཆོས་ཉིད་ཀྱིས་ཀྱང་སྐྱེ་སྟེ། འཇིག་པའི་ཚེ་ལྟ་བུའོ། །

[Block 4676]
དེའི་ཚེ་ནི༌[^3317]ས་འོག་མ་པའི་སེམས་ཅན་ཐམས་ཅད་དགེ་བའི་ཆོས་རྣམས་ཀྱི་འཇུག་པ་ཤས་ཆེ་བ་ཉིད་ཀྱི་ཕྱིར་བསམ་གཏན་དེ༌[^3318]སྐྱེད་པར་བྱེད་དོ། །

[Block 4677 [HEADING]]
### སྟོན་པའི་དམ་ཆོས་རྣམ་གཉིས། ^5-19-0

[Block 4678]
གང་ལ་ཆོས་རྣམས་ཀྱི་རྣམ་པ་ནི་དུ་ཡོད། [^3319]འདི་ལྟ་བུའི༌[^3320]མངོན་པའི་ཆོས་འདི་ཇི་སྲིད་དུ་གནས་ཤེ་ན། སྟོན་པའི་དམ་ཆོས་རྣམ་གཉིས་ཏེ། ལུང་དང་རྟོགས་པའི་བདག་ཉིད་དོ། །

[Block 4679]
དེ་ལ་ལུང་ནི་མདོ་སྡེ༌[^3321]དང་འདུལ་བ་དང་ཆོས་མངོན་པ་རྣམས་སོ། །

[Block 4680]
རྟོགས་པ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་རྣམས་ཏེ། དེ་ལྟར་ན་དམ་པའི་ཆོས་འདི་ནི་རྣམ་པ་གཉིས་ཡིན་ནོ། །

[Block 4681 [VERSE]]
དེ་འཛིན་བྱེད་པ་སྨྲ་བྱེད་དང་། །
སྒྲུབ་པར་བྱེད་པ་ཁོ་ན་ཡིན། །

[Block 4682]
ལུང་འཛིན་པར་བྱེད་པ་ནི་སྨྲ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 4683]
རྟོགས་པ༌[^3322]འཛིན་པར་བྱེད་པ་ནི་སྒྲུབ་པར་བྱེད་པ་ཡིན་ཏེ། དེའི་ཕྱིར་དེ་ཉིད་ཇི་སྲིད་དུ་གནས་པ་དེ་སྲིད་དུ་དམ་པའི་ཆོས་གནས་པར་རིག་པར་བྱའོ། །

[Block 4684]
དེ་དག་ཀྱང་ལོ་སྟོང་དུ་གནས་སོ་ཞེས་བཤད་དོ། །

[Block 4685]
གཞན་དག་ན་རེ་རྟོགས་པ་ནི་དེ་ལྟ་བུ་ཡིན་གྱི། ལུང་ནི་ཡུན་རིང་དུ་གནས་སོ་ཞེས་ཟེར་རོ། །

[Block 4686 [HEADING]]
### ཁ་ཆེ་བྱེ་བྲག་སྨྲ་བའི་ཚུལ་གྲུབ་བཤད་པ། ^5-20-0

[Block 4687]
ཅི་བསྟན་བཅོས་འདིར་ཆོས་མངོན་པ་བཤད་པ་གང་ཡིན་པའི་ཆོས་མངོན་པ་འདི་ཉིད་སྟོན་པས་བཤད་དམ་ཞེ་ན། བདག་གིས་མངོན་པའི་ཆོས་འདི་ཕལ་ཆེར་ནི།[^3323] །

[Block 4688 [VERSE]]
ཁ་ཆེ་བྱེ་བྲག་སྨྲ་བའི་ཚུལ་གྲུབ་བཤད། །
ཉེས་པར༌[^3324]ཟིན་གང་དེ་འདིར་བདག༌[^3325]གིས་ཉེས། །
དམ་ཆོས་ཚུལ་ལ་ཚད་མ་ཐུབ་རྣམས་ཡིན། །

[Block 4689]
བདག་གིས་ཆོས་མངོན་པ་འདི་ཕལ་ཆེར་ཁ་ཆེ་བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ཀྱི༌[^3326]ཚུལ་དུ་གྲུབ་པར་བཤད་པ་ཡིན་ནོ། །

[Block 4690]
འདི་ལ་བདག་གིས་ཉེས་པར་ཟིན་པ་གང་ཡིན་པ་དེ་ནི་བདག་གིས༌[^3327]ཉེས་པ་ཡིན་ཏེ། དམ་པའི་ཆོས་ཀྱི་ཚུལ་ལ་ནི་སངས་རྒྱས་རྣམས་ཁོ་ན་དང་།

[Block 4691 [VERSE]]
སངས་རྒྱས་ཀྱི་སྲས་རྣམས་ཚད་མ་ཡིན་ནོ། །
སྟོན་པ་འཇིག་རྟེན་མིག་ནི་ཟུམ་གྱུར་ཅིང་། །
དབང་གྱུར་སྐྱེ་བོ་ཕལ་ཆེར་ཟད་པ་ན། །

[Block 4692]
དེ་ཉིད་མ་མཐོང་རང་དགར་གྱུར་པ་ཡི།[^3328] །

[Block 4693 [VERSE]]
ངན་རྟོག་རྣམས་ཀྱིས་བསྟན་པ་འདི་དཀྲུགས་སོ། །
རང་བྱུང་རང་བྱུང་བསྟན་པ་གཅེས་འཛིན་རྣམས། །
མཆོག་ཏུ་ཞིར་གཤེགས་འགྲོ་མགོན་མེད་པ་ན། །
འདོམས་མེད་ཡོན་ཏན་འཇོམས་པར་བྱེད་པ་ཡི། །

[Block 4694 [VERSE]]
དྲི་མས་དགའ་མགུར་དེང་སང་འདི་ན་སྤྱོད། །
དེ་ལྟར་ཐུབ་པ་དག་གི༌[^3329]བསྟན་པ་ནི། །
ལྐོག་མར་སྲོག་ཕྱིན་འདྲ་དང་དྲི་མ་རྣམས། །
སྟོབས་དང་ལྡན་པའི་དུས་སུ་རིག་ནས་ནི། །

[Block 4695]
ཐར་པ་འདོད་པ་དག་གིས་བག་ཡོད་གྱིས། །ཆོས་མངོན་པའི་མཛོད་ཀྱི་བཤད་པ་ལས་སྙོམས་པར་འཇུག་པ་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་བརྒྱད་པའོ།། །།
--- END BLOCKS ---
