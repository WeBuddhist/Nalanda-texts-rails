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
[Block 4131]
དེ་ནི་ལུས་ཀྱི་མཁྲང་པོ་ཟད་པར་མེད་པའི་ཕྱིར་སྡུག་བསྔལ་གྱི་དབང་པོ་འགགས་སོ་ཞེས་གསུངས་སོ། །

[Block 4132]
བསམ་གཏན་གསུམ་པ་ལ༌[^2381]ནི་དབུགས་རྔུབ་པ་དང་དབུགས་འབྱུང༌[^2382]བ་དག་སྟེ། དེ་དག་ཀྱང་རླུང་ཁོ་ན་ཡིན་པས་སྙོམས་པར་འཇུག་པའི་བསམ་གཏན་གང་ན་ནང་གི་སྐྱོན་ཇི་ལྟ་བར་སྐྱེ་བའི་བསམ་གཏན་དེ་ན༌[^2383]ཕྱི་རོལ་གྱི་ཡང་དེ་ལྟ་བུ་ཡིན་ནོ། །ཅིའི་ཕྱིར་སས་འཇིག་པ་མ་ཡིན་ཞེ་ན། སྣོད་ཅེས་བྱ་བ་ནི་ས་ཁོ་ན་ཡིན་ལ་དེ་ནི་མེ་དང་ཆུ་དང་རླུང་དག་དང་མི་མཐུན་གྱི་ས་དང་ནི་མ་ཡིན་ནོ། །

[Block 4133]
བསམ་གཏན་བཞི་པ་ནི་ཇི་ལྟར་མི་འཇིག་ཅེ་ན།

[Block 4134]
བཞི་པ་ན་མེད་མི་གཡོའི་ཕྱིར། །བཅོམ་ལྡན་འདས་ཀྱིས་བསམ་གཏན་བཞི་པ་ནི་ནང་གི་སྐྱོན་དང་བྲལ་བའི་ཕྱིར་མི་གཡོ་བ་ཞེས་གསུངས་ཏེ། དེའི་ཕྱིར་དེའི་ཕྱིའི་སྐྱོན་ཡང་མི་འཇུག་པས་དེ་ན༌[^2384]འཇིག་པ་མེད་དོ། །

[Block 4135]
གཞན་དག་ན་རེ་གནས་གཙང་མའི་མཐུས༌[^2385]ཡིན་ཏེ། དེ་དག་གིས་གཟུགས་མེད་པ་དག་ཏུ་འཇུག་པར་ཡང་མི་ནུས་ལ། གཞན་དུ་ཡང་འགྲོ་བར་མི་ནུས་སོ་ཞེས་ཟེར་རོ། །

[Block 4136]
འོ་ན་བསམ་གཏན་བཞི་པའི་སྣོད་རྟག་པར་འགྱུར་རོ་ཞེ་ན།

[Block 4137 [VERSE]]
མི་རྟག་དེ་ཡི་གཞལ་མེད་ཁང་། །
སེམས་ཅན་བཅས་ཏེ་འབྱུང་འཇིག་ཕྱིར། །

[Block 4138]
བསམ་གཏན་བཞི་པ་ནི་ས་གཞི༌[^2386]གཅིག་ཏུ་འབྲེལ་པ་མ་ཡིན་ནོ། །

[Block 4139]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། གནས་གཞན་དུ་རྣམ་པར་ཆད་པ་ཡིན་ཏེ་སྐར་མ་བཞིན་ནོ། །

[Block 4140]
དེ་ན་སེམས་ཅན་གང་དང་གང་སྐྱེ་བའམ་འཆི་འཕོ་ཡང་རུང་སྟེ། དེ་ནི་གཞལ་མེད་ཁང་དང་བཅས་ཏེ་སྐྱེ་ཞིང་འཆི་འཕོ་བས་དེ་ལ་རྟག་པ་ཉིད་མེད༌[^2387]དོ། །

[Block 4141]
ཡང་འཇིག་པ་དེ་དག་གོ་རིམས་གང་གིས༌[^2388]འབྱུང་ཞེ་ན། རེ་ཞིག་བར་ཆད་མེད་པར་ནི། །མེ་ཡིས་བདུན་ནོ། །

[Block 4142]
མེས་འཇིག་པ་བདུན་འབྱུང་ངོ་། །དེའི་འོག་ཏུ༌[^2389]ནི། ཆུ་ཡིས་གཅིག །མེས་འཇིག་པ་བདུན་གྱི༌[^2390]མཇུག་ཐོགས་སུ་ཆུ་དག་གིས་འཇིག་པ་འབྱུང་ངོ་། །དེ་ལྟར་ཆུ་བདུན་ཐལ་ནས་ཀྱང་། མེ་ཡིས་བདུན་ནོ། །

[Block 4143]
རིམ་པ་དེས་ན་ཆུས་འཇིག་པ་བདུན་ཐལ་ནས་ཡང་མེས་འཇིག་པ་བདུན་འབྱུང་ངོ་། །དེ་ནས་ནི། མཇུག་ཏུ་རླུང་གིས་འཇིག་པ་ཡིན། །དེ་ནས་ནི་མཇུག་ཏུ་རླུང་གིས༌[^2391]འཇིག་པ་གཅིག་འབྱུང་ངོ་། །ཅིའི་ཕྱིར་ཞེ་ན། སེམས་ཅན་དེ་དག་གི་སྙོམས་པར་འཇུག་པའི་ཁྱད་པར་ལས་ལུས་དག་གནས་པའི་ཁྱད་པར་ཇི་ལྟ་བར་སྣོད་རྣམས་ཀྱང་དེ་བཞིན་ནོ། །

[Block 4144]
དེ་དག་ནི༌[^2392]མེས་འཇིག་པ་ལྔ་བཅུ་རྩ་དྲུག་དང་། ཆུས་འཇིག་པ་བདུན་དང་རླུང་གིས་འཇིག་པ་གཅིག་ཡིན་ཏེ། དེ་ལྟར་བཤད་ནས༌[^2393]བཏགས་པའི་བཤད་པ་དགེ་རྒྱས་ཀྱི་ལྷ་རྣམས་ཀྱི་ཚེའི་ཚད་ནི་བསྐལ་པ་དྲུག་ཅུ་རྩ་བཞིའི་ཞེས་བྱ་བ་ལེགས་པར་དྲངས་པ་ཡིན་ནོ། །

[Block 4145]
ཆོས་མངོན་པའི་མཛོད་ཀྱི་བཤད་པ་ལས་འཇིག་རྟེན་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་གསུམ་།[^2394] །།

[Block 4146 [HEADING]]
## ལས་བསྟན་པ། ^4-0

[Block 4147]
ཡང་སེམས་ཅན་དང་སྣོད་ཀྱི་འཇིག་རྟེན་རྣམ་པ་མང་པོ་སྣ་ཚོགས་པ་བཤད་པ་གང་ཡིན་པ་དེ་སུས་བྱས་ཤེ་ན། སུས་ཀྱང་བློ་སྔོན་དུ་བཏང་སྟེ་བྱས་པ་ནི་མེད་དོ། །

[Block 4148]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། སེམས་ཅན་རྣམས་ཀྱི། ལས་ལས་འཇིག་རྟེན་སྣ་ཚོགས་སྐྱེས། །གལ་ཏེ་ལས་ལས་སྐྱེས་ནས༌[^2395]ཅིའི་ཕྱིར་སེམས་ཅན་རྣམས་ཀྱི་ལས་དག་གིས་གུར་གུམ་དང་། ཙན་དན་ལ་སོགས་པ་ཆེས་དགའ་དགའ་ལྟ་བུར་སྐྱེས་པར༌[^2396]འགྱུར་ལ་དེ་དག་གི་ལུས་ནི་མ་ཡིན་ཞེ་ན། སེམས་ཅན་འདྲེན་མར་བྱེད་པ་རྣམས་ཀྱི་ལས་དེ་ལྟ་བུ་དག་ཁོ་ན༌[^2397]གང་རྨ་ལྟ་བུར་གྱུར་པའི་ལུས་དག་དང་། དེའི་ཚེ༌[^2398]གཉེན་པོར་གྱུར་པ་ལོངས་སྤྱོད་དགའ་དགའ་ལྟ་བུ་དག་ཀྱང༌[^2399]སྐྱེའི། ལྷ་འདྲེན་མར་བྱེད་པ་མ་ཡིན་པ་རྣམས་ཀྱི་ནི་གཉི་ག་ཡང་དགའ་དགའ་ལྟ་བུ་དག་ཡིན་ནོ། །

[Block 4149]
ལས་དེ་ཡང་གང་ཞིག་ཅེ་ན། དེ་ནི་སེམས་པ་དང་དེས་བྱས། །མདོ༌[^2400]ལས་ནི་གཉིས་ཏེ། སེམས་པ་དང་བསམས་པའི༌[^2401]ལས་སོ་ཞེས་གང་གསུངས་པ་ལ། བསམས་པ༌[^2402]གང་ཡིན་པ་དེ་ནི། སེམས་པས་བྱས་པ་དེ་ཡིན་ནོ། །

[Block 4150]
ལས་གཉིས་པོ་དེ་དག་ནི་གསུམ་ཡིན་ཏེ། ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས་རྣམས་སོ། །

[Block 4151]
ལས་འདི་དག་ཇི་ལྟར་རྣམ་པར་གཞག་ཅི་རྟེན་ལས་སམ། འོན་ཏེ་ངོ་བོ་ཉིད་ལས་སམ། འོན་ཏེ་ཀུན་ནས་སློང་བ་ལས་གལ་ཏེ་རྟེན་ལས་ཡིན་ན་ནི་ཐམས་ཅད་ལུས་ལ་བརྟེན་པའི་ཕྱིར་ལུས་ཀྱི་ལས་གཅིག་པུར་འགྱུར་རོ། །

[Block 4152]
གལ་ཏེ་ངོ་བོ་ཉིད་ལས་ཡིན་ན་ནི་དེ་དག་གི་ལས་གཅིག་པུར་འགྱུར་རོ། །

[Block 4153]
གལ་ཏེ་ཀུན་ནས་སློང་བ་ལས་ཡིན་ན་ནི་ཐམས་ཅད་ཀྱང་ཡིད་ཀྱི༌[^2403]ཀུན་ནས་བསླང་བའི་ཕྱིར་ཡིད་ཀྱི་ལས་གཅིག་པུར་འགྱུར་རོ་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་རྒྱུ་གསུམ་གྱིས་གོ་རིམས་བཞིན་དུ་གསུམ་རྣམ་པར་གཞག་གོ་ཞེས་ཟེར་རོ། །

[Block 4154 [HEADING]]
### ཡིད་ཀྱི་ལས། ^4-1-0

[Block 4155]
དེ་ལ། སེམས་པ་ཡིད་ཀྱི་ལས་ཡིན་ནོ། །

[Block 4156]
སེམས་པ་ནི་ཡིད་ཀྱི་ལས་ཡིན་ནོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4157 [HEADING]]
### ལུས་དང་ངག་གི་ལས། ^4-2-0

[Block 4158]
དེས་བསྐྱེད་ལུས་དང་ངག་གི་ལས། །

[Block 4159]
སེམས་ལས་སྐྱེས༌[^2404]པ་གང་ཡིན་པ་བསམས་པའི༌[^2405]ལས་ཞེས་གསུངས་པ་དེ་དག་ནི་ལུས་དང་ངག་གི་ལས་སུ་རིག་པར་བྱའོ། །

[Block 4160 [HEADING]]
#### རྣམ་པར་རིག་བྱེད། ^4-2-1-0

[Block 4161]
དེ་དག་རྣམ་རིག་རྣམ་རིག་མིན། །ལུས་དང་ངག་གི་ལས་དེ་དག་ནི་སོ་སོར་རྣམ་པར་རིག་བྱེད་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་རང་བཞིན་དག་ཏུ་རིག་པར་བྱའོ། །

[Block 4162 [HEADING]]
##### ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད། ^4-2-1-1-0

[Block 4163]
དེ་ལའང་། [^2406]ལུས་རྣམ༌[^2407]རིག་བྱེད་དབྱིབས་སུ་འདོད། །སེམས་ཀྱི་དབང་གིས་ལུས་དེ་དང་དེ་ལྟར་གནས་པ་ནི་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་ཡིན་ནོ། །

[Block 4164]
གཞན་དག་ན་རེ་འགྲོ་བ་ཡིན་ཏེ། ལུས་གཡོ་བ་ལས་ཡིན་གྱི་མིག་གཡོ་བ་ནི་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་ཏེ། དེ་དག་ལ། འགྲོ་མིན་གང་ཕྱིར་འདུས་བྱས་ནི། །

[Block 4165 [VERSE]]
སྐད་ཅིག་པ་ཡིན་ཞེས་བྱ་བ་བརྗོད་དོ། །
སྐད་ཅིག་ཅེས་བྱ་བ་འདི་ཅི་ཞེ་ན།
བདག་ཉིད་དུ་རེད་མ་ཐག་ཏུ་འཇིག་པའོ། །

[Block 4166]
དེ་འདི་ལ་ཡོད་པས་ན༌[^2408]སྐད་ཅིག་པ་སྟེ་དབྱུག་པ༌[^2409]བཞིན་ནོ། །

[Block 4167]
འདུས་བྱས་ཐམས་ཅད་བདག་ཉིད་ཐོབ་པ་ལས་ཕན་ཆད་དུ་མེད་པའི་ཕྱིར་གང་དུ་སྐྱེས་པ་དེ་ཉིད་དུ་འཇིག་པར་འགྱུར་རོ། །

[Block 4168]
དེ་ནི་ཡུལ་གཞན་དུ་འཕོ་བར་རིག་པ༌[^2410]མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་ལུས་ཀྱི་ལས་ནི་འགྲོ་བ་མ་ཡིན་ནོ། །

[Block 4169]
གལ་ཏེ་ཐམས་ཅད་སྐད་ཅིག་པར་གྲུབ་པར་གྱུར་ན་ནི་དེ་དེ་ལྟ་ཡིན་ནོ། །

[Block 4170]
འདིའི༌[^2411]གྲུབ་པ་ཁོ་ནར་ཁོང་དུ་ཆུད་པར་གྱིས་ཤིག །ག་ལས་ཤེ་ན། འདུས་བྱས་ནི་གདོན་མི་ཟ་བར་འཇིག་ཕྱིར་རོ། །
--- END BLOCKS ---
