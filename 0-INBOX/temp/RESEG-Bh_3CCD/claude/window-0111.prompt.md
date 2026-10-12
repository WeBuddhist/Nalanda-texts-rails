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
[Block 3886 [VERSE]]
བདག་ཡོད་པ་ནི་གཞན་གྱི་འདུ་ཤེས་ཏེ། །
རང་དང་གཞན་གྱི་དབྱེ་བས་ཆགས་སྡང་བྱུང་། །
དེ་གཉིས་ཕན་ཚུན་ཀུན་དུ་འབྲེལ་པ་ལས། །
སྐྱོན་རྣམས་ཐམས་ཅད་རབ་ཏུ་སྐྱེ་བར་འགྱུར། །

[Block 3887]
ཞེས་འབྱུང་ངོ་། །

[Block 3888]
ལེན་པ་ཡང་དེ་དག་རྒྱས་པའི་མཚན་ཉིད་ཕུང་པོ་སོ་སོར་ལེན་པའོ། །

[Block 3889]
དེ་ལྟར་ཉོན་མོངས་པ་དེ་དག་གོ། །

[Block 3890]
དེ་བཞིན་དུ་གཉིས་པ་དང་བཅུ་པ་སྟེ་འདུ་བྱེད་དང་སྲིད་པ་དག་ནི་ལས་སོ། །

[Block 3891]
དེ་ལ་འདུ་བྱེད་ནི་གཉིས་ཏེ། སེམས་དང་ལྡན་པ་དང་སེམས་དང་མི་ལྡན་པའོ། །

[Block 3892]
དེ་ལ་སེམས་དང་ལྡན་པ་ནི་རྣམ་པ་གསུམ་སྟེ། དགེ་བ་དང་། མི་དགེ་བ་དང་། ལུང་དུ་མ༌[^2415]བསྟན་པ་ནི་རྣམ་པ་གཉིས་ཏེ། བསྒྲིབས༌[^2416]ལ་ལུང་དུ་མ་བསྟན་པ་དང་། མ་བསྒྲིབས༌[^2417]ལ་ལུང་དུ་མ་བསྟན་པའོ། །

[Block 3893]
དེ་ལ་གང་ཉོན་མོངས་པ་དང་ལྡན་པ་དེ་ནི་བསྒྲིབས༌[^2418]ལ་ལུང་དུ་མ་བསྟན་པའོ། །

[Block 3894]
གང་དེ་དང་བྲལ་བ་དེ་ནི་མ་བསྒྲིབས༌[^2419]ལ་ལུང་དུ༌[^2420]བསྟན་པའོ། །

[Block 3895]
དེ་ལ་སེམས་དང་ལྡན་པ་ནི་སེམས་པ༌[^2421]དང་ཚོར་བ་དང་འདུ་ཤེས་དང་འདུན་པ་དང༌[^2422]རེག་པ་དང་། བློ་དང་དྲན་པ་དང་ཡིད་ལ་བྱེད་པ་དང་ལྷག་པར་མོས་པ་དང་། ཏིང་ངེ་འཛིན་དང་། དད་པ་དང་། ངོ་ཚ་དང་ཁྲེལ་དང་སེར་སྣ་མེད་པ་དང་ཞེ་སྡང་མེད་པ་དང་། གཏི་མུག་མེད་པ་དང་། བརྩོན་འགྲུས་དང་། སྦྱངས་པ་དང་བག་ཡོད་པ་དང་བཏང་སྙོམས་དང་རྣམ་པར་འཚེ་བ་མེད་པ་དང་། འདོད་ཆགས་ནས་བརྩམས་ཏེ་སྤྱོད་པའི་བར་དུ་ལྔ་བཅུ་རྩ་གཅིག་གོ། །

[Block 3896]
ཐོབ་པ་དང་མ་ཐོབ་པ་དང་། སྐལ་བ༌[^2423]མཚུངས་པ་དང་། འདུ་ཤེས་མེད་པ་དང་། འགོག་པའི་སྙོམས་པར་འཇུག་པ་དང་། འདུ་ཤེས་མ་ཡིན་པའི་སྙོམས་པར་ཞུགས་པ་དང་། སྲོག་གི་དབང་པོ་དང་། སྐྱེ་བ་དང་། གནས་པ་དང་། རྒ་བ་དང་། མི་རྟག་པ་དང་མིང་གི་ཚོགས་དང་ཚིག་གི་ཚོགས་དང་ཡི་གེའི་ཚོགས་ཏེ་སེམས་དང་མི་ལྡན་པ་ནི་བཅུ་བཞིའོ། །

[Block 3897]
སྲིད་པ་ནི་གསུམ་སྟེ། འཆི་བའི་སྲིད་པ་དང་། བར་མ་དོའི་སྲིད་པ་དང་། སྐྱེ་བའི་སྲིད་པའོ། །

[Block 3898]
དེ་དག་ནི་ལས་ཏེ། དགེ་བ་དང་མི་དགེ་བའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3899]
ལྷག་མ་བདུན་ནི་སྡུག་བསྔལ་ཅན་གྱི་རྣམ་གྲངས་ཏེ་སྐྱེ་བའོ། །

[Block 3900]
རྣམ་པར་ཤེས་པ་དང་མིང་དང་གཟུགས་དང་སྐྱེ་མཆེད་དྲུག་དང་རེག་པ་དང་ཚོར་བ་དང་སྐྱེ་བ་དང་། རྒ་ཤིའོ། །

[Block 3901]
དེ་ལ་རྣམ་པར་ཤེས་པ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་དང་། ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་། མིག་གི་རྣམ་པར་ཤེས་པ་དང་། རྣ་བའི་རྣམ་པར་ཤེས་པ་དང་། སྣའི་རྣམ་པར་ཤེས་པ་དང་། ལྕེའི་རྣམ་པར་ཤེས་པ་དང་། ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་སྟེ་བརྒྱད་དོ། །

[Block 3902]
ཡང་ན་ལྔ་སྟེ། ཀུན་གཞི་དང་། ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་དང་། རང་དང་གཞན་གྱི༌[^2424]རྒྱུད་ལ་གནས་པའི་དབང་པོའི་རྣམ་པར་ཤེས་པ་དང་། འཇུག་པའི་རྣམ་པར་ཤེས་པ་དང་། གཟུགས་ལ་སོགས་པའི་སོ་སོར་སྣང་བའི་རྣམ་པར་ཤེས་པའོ། །

[Block 3903]
ཡང་ན་གསུམ་སྟེ། རྣམ་པར་སྨིན་པའི་རྣམ་པར་ཤེས་པ་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་། འཇུག་པའི་རྣམ་པར་ཤེས་པའོ། །

[Block 3904]
འཇུག་པའི་རྣམ་པར་ཤེས་པ་དྲུག་པོ་གཅིག་ཏུ་བྱས་ཏེ། རྣམ་པར་ཤེས་པ་གཅིག་ཅེས་ལ་ལ་འདོད་དེ། ཇི་སྐད་དུ།

[Block 3905 [VERSE]]
དོན་དང་སེམས་ཅན་བདག་རྣམ་རིག །
སོ་སོར་སྣང་བ་རབ་སྐྱེ་བ། །
རྣམ་པར་ཤེས་པ་དེ་དོན་མེད། །
དེ་མེད་པས་ནི་དེ་ཡང་མེད། །

[Block 3906 [VERSE]]
གཅིག་ནི་རྐྱེན་གྱི་རྣམ་ཤེས་ཏེ། །
གཉིས་པ་ཉེ་བར་སྤྱོད་པ་ཅན། །
ལོངས་སྤྱོད་ཡོངས་སུ་སྤྱོད་པ་དང་།
སྐུལ་བྱེད་དེ་ལ་སེམས་ལས་བྱུང་། །

[Block 3907]
ཞེས་འབྱུང་ངོ་། །དེ་བཞིན་དུ་ཡང་།

[Block 3908 [VERSE]]
རྣམ་པར་སྨིན་པ་ངར་སེམས་དང་། །
ཡུལ་ལ་རྣམ་པར་རིག་པའོ། །

[Block 3909]
ཞེས་འབྱུང་ངོ་། །དེ་བཞིན་དུ།

[Block 3910 [VERSE]]
གཅིག་པུ་ཉིད་ནི་གཉིས་སུ་སྣང་། །
སེམས་ཉིད་རྣམ་པར་འཁྲུལ་པས་སོ། །
གཟུང་འཛིན་དག་གི་དབྱེ་བ་ཡིས།[^2425] །
ཤིན་ཏུ་མཁས་པས་ཅི་མིན་ནམ། །

[Block 3911]
ཞེས་བྱ་བ་ལ་སོགས་པ་འབྱུང་བས་སོ། །

[Block 3912]
མིང་དང་གཟུགས་ནི་རྣམ་པ་བཞི་སྟེ། ཚོར་བ་དང་འདུ་ཤེས་དང་འདུ་བྱེད་ནི་གཟུགས་མེད་པའི་ཕུང་པོའོ། །

[Block 3913]
གཟུགས་ནི་གཟུགས་ཀྱི་ཕུང་པོ་སྟེ། །དབང་པོ་དང་ཡུལ་དང་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་རྣམ་པ་བཅུ་གཅིག་གོ། །

[Block 3914]
དེ་ལྟར་ཕུང་པོ་བཞིའི་བདག་ཉིད་ཀྱི་མིང་དང་། གཟུགས་ཞེས་བྱའོ། །

[Block 3915]
སྐྱེ་མཆེད་དྲུག་སྟེ། མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་དང་། ཡིད་ཀྱི་སྐྱེ་མཆེད་དོ། །

[Block 3916]
དབང་པོ་དང་ཡུལ་དང་རྣམ་པར་ཤེས་པ་འདུས་པ་ལས་སྐྱེས་པ་ནི་རིག་པའོ། །

[Block 3917]
ཚོར་བ་ནི་མྱོང་བ་རྣམ་པ་གསུམ༌[^2426]སྟེ། བདེ་བ་དང་། སྡུག་བསྔལ་བ་དང་། བཏང་སྙོམས་ཀྱི་ངོ་བོ་ཉིད་དོ། །

[Block 3918]
དེ་ཡང་མིག་ལ་སོགས་པའི་དབྱེ་བས་རྣམ་པ་བཅོ་བརྒྱད་དུ་འགྱུར་རོ། །

[Block 3919]
སྐྱེ་བ་ཡང་རྣམ་པ་བཞི་སྟེ། སྒོ་ང་དང་། དྲོད་གཤེར་དང་། མངལ་དང་། རྫུས་ཏེ་སྐྱེས་པའོ། །

[Block 3920]
དམྱལ་བ་དང་། ཡི་དགས་དང་། བྱོལ་སོང་དང་། ལྷ་དང་། ལྷ་མ་ཡིན་དང་། མིའི་དབྱེ་བས་དྲུག་ཅེས་ལ་ལ་འདོད་དོ། །

[Block 3921]
ངན་སོང་དང་བདེ་འགྲོའི་དབྱེ་བས་གཉིས་སུ་ཡང་འདོད་དོ། །

[Block 3922]
རྒ་བ་ཡང་ནུས་པ་དང་བྲལ་བའི་མཚན་ཉིད་ཀྱི༌[^2427]ཆོས་སོ། །

[Block 3923]
ཤི་བ་ནི་ཕུང་པོ་འདོར་བས༌[^2428]རྣམ་པར་ཤེས་པའི་སྐད་ཅིག་མ་ཚོར་བ་ལ་གནས་པའི་ངོ་བོ་ཆོས་བདུན་པོ་དེ་དག་ནི་སྐྱེ་བ་སྟེ་སྐྱེས༌[^2429]པ་ལ་ནི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པའི་ཆོས་བདུན་དང་འབྲེལ་པའི་ཕྱིར་རོ། །

[Block 3924]
ཉོན་མོངས་པ་དང་ལས་དང་སྐྱེ་བ་འདི་དག་གིས་ཁམས་གསུམ་ན་གནས་པའི་སེམས་ཅན་གྱི་ཚོགས་ཟོ་ཆུན་གྱི་འཁྲུལ་འཁོར་བཞིན་དུ་འཁོར་བར་བྱེད་པས་འགྲོ་བ་གཅིག་ནས་གཅིག་ཏུ་ཐོབ་པར་གྱུར་ནས་ཉོན་མོངས་པ་ཚོན་པོ་མྱོང་བར་འགྱུར་རོ། །

[Block 3925 [VERSE]]
ཐལ་ཚན་གྱི་ཆུ་བོའི་མདོ་ལས་ཀྱང་། །
ནོར་ཕྲོགས་རྐུན་མ་ལས་ཀྱང་བདག་མི་འཇིགས། །
དེ་ཡིས་ནོར་ཕྲོགས་དེ་ཡང་ཡོད་མ་ཡིན། །
ཡིད་ལ་བསགས་ཤིང་བསགས་པའི་དག་པའི་ནོར། །
--- END BLOCKS ---
