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

[Block 4171]
དངོས་པོ་རྣམས་འཇིག་པ་ནི་རྒྱུ་མེད་པ་ལས་བྱུང་བ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། བྱ་བའི་རྒྱུ་ཡིན་ན་འཇིག་པ་ཡང་མེད་པ་ཡིན་པས་མེད་པ་གང་ཡིན་པ་དེ་ལ་ནི་ཅི་ཞིག་བྱར་ཡོད། རྒྱུ་མེད་པ་ལས་བྱུང་བའི་འཇིག་པ་དེ་ནི་དངོས་པོ་སྐྱེད་པ༌[^2412]ཙམ་ལ་མ་ཡིན་ན་ཕྱིས་ཀྱང་མི་འབྱུང་སྟེ།[^2413] དངོས་པོ་མཚུངས་པའི་ཕྱིར་རོ། །

[Block 4172]
འོན་ཏེ་གཞན་དུ་གྱུར་པ་ཡིན་ནོ་ཞེ་ན། དེ་ཉིད་གཞན་དུ་གྱུར་པ༌[^2414]ནི་རིགས་པ་མ་ཡིན་ཏེ། དེ་ཉིད་དེ་དང་མཚན་ཉིད་མི་མཐུན་པར་ནི་མི་རུང་ངོ་། །ཤིང་ལ་སོགས་པ་དག་མེ་དང་འབྲེལ་པ་ལས་འཇིག་པར་ཡང་མཐོང་ལ་མཐོང་བ་ལས་བརླིང་བའི་ཚད་མ་ཡང་མེད་པས་ཐམས་ཅད་ཀྱི་འཇིག་པ་ནི་རྒྱུ་མེད་པ་ལས་བྱུང་བ་མ་ཡིན་ནོ་ཞེ་ན། རེ་ཞིག་ཁྱོད་ཤིང་ལ༌[^2415]སོགས་པ་དག་མེ་དང་འབྲེལ་པ་ལས་འཇིག་པར་བལྟ་བར་བྱའོ༌[^2416]ཞེས་བྱ་བ་ཇི་ལྟ་བུར་སེམས། དེ་ཡོད་ན་དེ་དག་ལ༌[^2417]ཡང་མི་སྣང་བའི་ཕྱིར་རོ། །

[Block 4173]
རེ་ཞིག་འདི་དཔྱད་པར་བྱ་སྟེ། ཅི་མེ་དང་འབྲེལ་པ་ལས་ཤིང་ལ་སོགས་པ་ཞིག་སྟེ། དེའི་ཕྱིར་མི་སྣང་བ་ཞིག་ཡིན་ནམ། འོན་ཏེ་རང་ཉིད་ཞིག་ལ༌[^2418]གཞན་དག་ཀྱང་མ་སྐྱེས་པས་དེའི་ཕྱིར་མི་སྣང་སྟེ་དཔེར་ན་རླུང་དང་ཕྲད་པ་ལས་མར་མེ་དང་ལག་པ་དང་ཕྲད་པ་ལས་དྲིལ་བུའི་སྒྲ་ལྟ་བུ་ཞིག་ཡིན། དེ་ལྟ་བས་ན་དོན་འདི་ནི་རྗེས་སུ་དཔག་པས་བསྒྲུབ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 4174]
འདི་ལ་རྗེས་སུ་དཔག་པ་གང་ཞེ་ན། རེ་ཞིག་མེད་པ་ནི་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་ཞེས་ནི་བཤད་ཟིན་ཏོ། །

[Block 4175]
ཡང་ན། [^2419]རྒྱུ་མེད་པ་ལས་འགའ་མི་འབྱུང་། །གལ་ཏེ་འཇིག་པ་རྒྱུ་དང་ལྡན་པ་ཞིག་ཏུ་གྱུར་ན་སྐྱེ་བ་བཞིན་དུ་འགའ་ཡང་རྒྱུ་མེད་པ་ལས་མི་འགྱུར་བ་ཞིག་ན་སྐད་ཅིག་མ་བློ་དང་སྒྲ་དང་མེ་ལྕེ་དག་འཇིག་པ་རྒྱུ་མེད་པ་ལས་བྱུང་བ་ཡང་མཐོང་བས་འདི་རྒྱུ་ལ་ལྟོས་པ་མ་ཡིན་ནོ། །

[Block 4176]
གང་ཞིག་བློ་ཡང་བློ་གཞན་གྱིས་འཇིག་ལ་སྒྲ་ཡང་སྒྲ་གཞན་གྱིས་འཇིག་གོ་སྙམ་དུ་སེམས་པ་དེ་ནི་རིགས་པ་མ་ཡིན་ཏེ། བློ་གཉིས་ཕྲད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 4177]
ཐེ་ཚོམ་ཅན་དང༌[^2420]ངེས་པའི་ཤེས་པ་དག་དང་། བདེ་བ་དང་སྡུག་བསྔལ་བ་དག་དང་། འདོད་ཆགས་དང་ཞེ་སྡང་དག་ཕྲད་པར་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 4178]
གང་གི་ཚེ་བློ་དང་སྒྲ་གསལ་བ་ཉིད༌[^2421]དག་གི་མཇུག་ཐོགས་སུ་བློ་དང་སྒྲ་མི་གསལ་བ་འབྱུང་བ་དེའི་ཚེ་ཇི་ལྟར་ན་མི་གསལ་བ་རིགས་མཐུན་པའི་ཆོས་ཀྱི༌[^2422]གསལ་བ་འཇིག་པར་འགྱུར། གང་ཡང་གནས་པའི་རྒྱུ་མེད་པའམ། ཆོས་དང་ཆོས་མ་ཡིན་པའི་དབང་གིས་མེ་ལྕེ་དག་འཇིག་གོ་སྙམ་དུ་སེམས་པ་དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། མེད་པ་ནི་རྒྱུ་ཡིན་པར་འོས་པ་མ་ཡིན་ནོ། །

[Block 4179]
སྐྱེ་བ་དང་འཇིག་པའི་རྒྱུ༌[^2423]ཆོས་དང་ཆོས་མ་ཡིན་པ་དག་ཀྱང་སྐད་ཅིག་སྐད་ཅིག་ཉིད་ལ་འཇུག་པ་ཐོབ་པ་དང་བགེགས་བྱེད༌[^2424]པར་འོས་པ་མ་ཡིན་ནོ། །

[Block 4180]
རྒྱུ་ཡོངས་སུ་བརྟགས་པ་འདི་ཡང་འདུས་བྱས་ཐམས་ཅད་ལ་བྱ་བར་ནུས་པས་བརྩད་མི་དགོས་སོ། །

[Block 4181]
གལ་ཏེ་ཤིང་ལ་སོགས་པ་དག་འཇིག་པ་མེ་དང་འབྲེལ་པའི་རྒྱུ་ལས་བྱུང་བ་ཞིག་ཡིན་ན་དེ་ལྟ་ན་ནི་ཚོས་བྱེད་ལས་སྐྱེས་པ་རྣམས་ཀྱི་ཚོས་པ་དང་། ཆེས་ཚོས་པ་དང་། ཆེས་ཆེར་ཚོས་པ་བྱུང་བ་ལ། རྒྱུ་ཡང་འཇིག་པ་པོར་འགྱུར་རོ། །

[Block 4182]
རྒྱུ་ཉིད་འཇིག་པ་པོར་འགྱུར་བ༌[^2425]ཇི་ལྟ་ཞེ་ན། མེ་དང་འབྲེལ་བ་གང་ལས་ཚོས་བྱེད་ལས་སྐྱེས་པ་འབྱུང་བ༌[^2426]དེ་ཉིད་དམ་དེ་དང་འདྲ་བ་ལས་ཚོས་པ་དང་། ཆེས་ཚོས་པ་དང་། ཆེས་ཆེར་ཚོས་པ་བྱུང་ན་དེ་དག་འཇིག་པས་རྒྱུ་ཉིད་དེ་དག་གི་འཇིག་པ་པོར་འགྱུར་བའམ། ཡང་ན་རྒྱུ་བྱེ་བྲག་མེད་པར་འགྱུར་རོ། །

[Block 4183]
གང་ལས་སམ། གང་དག༌[^2427]འདྲ་བ་ལས་དེ་དག་འབྱུང་བ༌[^2428]ཉིད་དམ། དེ་དང་འདྲ་བ་ལས་ཡང་མེད་པར་འགྱུར་བ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 4184]
[^2429]རེ་ཞིག་མེ་ལྕེ་གཞན་དག་ལས༌[^2430]རྒྱུ་ཐ་དད་པར་ཡོངས་སུ་བརྟག་པར་ནི་བྱ་ལ་རེག་ན། ཐལ་བ་དང་ཁ་བ་དང་རྩྭ་དང་ཉི་མ་དང་ཆུ་དང་ས་དང་འབྲེལ་པ་ལས་སྨིན་བྱེད་ལས་སྐྱེས་པའི་བྱེ་བྲག་བྱུང་བ་ལ་གང་ལ་བརྟག་པར་བྱ། འོ་ན་གང༌[^2431]ཆུ་བསྐོལ་བ་ཟད་པར་འགྱུར་བ་དེ་ལ་མེ་དང་འབྲེལ་པ་དག་ཅི་ཞིག་བྱེད་ཅེ་ན། མཐུའི་སྒོ་ནས་མེའི་ཁམས་འཕེལ་བར་བྱེད་ཅིང་དེའི་མཐུས་ན་ཆུའི་ཚོགས་ཉམ་ཆུང་ཞིང་ཉམ་ཆུང་བར་འགྱུར་ལ་ཤིན་ཏུ་ཉམ་ཆུང་བའི་བར་དུ་གྱུར་པ་དང་། མཇུག་ཏུ་རྒྱུན་ཡང་རྒྱུན་ཆགས་པར་མི་བྱེད་དེ། འདི་ལ་མེ་དང་འབྲེལ་པ་དག་གིས་ནི་འདི་བྱེད་དོ། །

[Block 4185]
དེ་ལྟ་བས་ན་དངོས་པོ་རྣམས་འཇིག་པ་ལ་རྒྱུ༌[^2432]ནི༌[^2433]མེད་ཀྱི་རང་ཉིད་འཇིག་པའི་ངང་ཅན་ཡིན་པའི་ཕྱིར་འཇིག་པ་ན་བྱུང་བ་ཙམ་གྱིས་འཇིག་པའི་ཕྱིར་འདི་དག་སྐད་ཅིག་མ་ལ་འཇིག་པར་ཡང་གྲུབ་ལ་སྐད་ཅིག་མ་ལ་འཇིག་པའི་ཕྱིར་འགྲོ་བ་ཡང་མེད་དོ། །

[Block 4186]
ཡུལ་གཞན་དག་ཏུ་འདབ་ཆགས་པར་འབྱུང་བ་ལས༌[^2434]འགྲོ་བར་མངོན་པའི་ང་རྒྱལ་བྱེད་པར་ཟད་དེ་རྩྭའི་མེ་བཞིན་ནོ། །

[Block 4187]
འགྲོ་བ་མེད་ན་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་དེ་དབྱིབས་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 4188]
མདོ་སྡེ་པ་རྣམས་ན་རེ་དབྱིབས་ནི་རྫས་སུ་མེད་དེ། ཕྱོགས་གཅིག་གི་སྒོར་ཁ་དོག་ཕལ་ཆེར་བྱུང་བ་ལ་གཟུགས་རིང་པོར༌[^2435]ཞེས་འདོགས་པར་བྱེད། དེ་ཉིད་ལ་ལྟོས་ནས་ཉུང་ངུར་བྱུང་བ་ལ་ཐུང་ངུ་ཞེས་འདོགས་པར་བྱེད། ཕྱོགས་བཞིར་མང་པོར་བྱུང་བ་ལ་གྲུ་བཞི་ཞེས་འདོགས་པར་བྱེད། ཐམས་ཅད་དུ་མཉམ་པ༌[^2436]ན་ལྷམ་པ་ཞེས་འདོགས་པར་བྱེད་དེ། ཐམས་ཅད་ཀྱང་དེ་དང་འདྲའོ། །

[Block 4189]
དཔེར་ན་མགལ་མེ་ཕྱོགས་གཞན་གཅིག་ཏུ་མྱུར་དུ་འདབ་ཆགས་པར་སྣང་བ་ནི་རིང་པོའོ་སྙམ་དུ་ཤེས་ལ། ཐམས་ཅད་དུ་སྣང་ན་ཟླུམ་པོའོ་སྙམ་དུ་ཤེས་ཀྱི་དབྱིབས་རྫས་སུ༌[^2437]གཞན་ཡོད་པ་ནི་མ་ཡིན་པ་བཞིན་ནོ། །

[Block 4190]
གལ་ཏེ་ཡོད་ན་ནི། གཉིས་གཟུང་འགྱུར། མིག་གིས་མཐོང་ན་ཡང་རིང་པོའོ་སྙམ་དུ་ཤེས་པར་འགྱུར་ལ། ལུས་ཀྱི་དབང་པོ༌[^2438]རེག་ན་ཡང་ཤེས་པར་འགྱུར་བས་འདི་དབང་པོ་གཉིས་ཀྱི༌[^2439]གཟུང་བར་འགྱུར་བ་ཞིག་ན། གཟུགས་ཀྱི་སྐྱེ་མཆེད་ལ་ནི་གཉིས་ཀྱིས་འཛིན་པ་མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 4191]
ཡང་ན༌[^2440]ཇི་ལྟར་རེག་བྱ་ལ་རིང་པོ་ལ་སོགས་པར་འཛིན་པ་ལྟར་ཁ་དོག་ལ་ཡང་དེ་བཞིན་དུ་ཡིད་ཆེས་པར་བྱའོ། །

[Block 4192]
དེ་ལ་ནི་རེག་བྱ་དང་ལྷན་ཅིག་སྤྱོད་པའི་ཕྱིར་དྲན་པ་ཙམ་ཡིན་གྱི་མངོན་སུམ་དུ་འཛིན་པ་ནི་མ་ཡིན་གྱི།[^2441] དཔེར་ན་མེའི་གཟུགས་མཐོང་ནས་དེའི་ཚ་བའི་དྲན་པ་འབྱུང་བ་དང་། མེ་ཏོག་གི་དྲི་བསྣམས་ནས་དེའི་ཁ་དོག་གི་དྲན་པ་འབྱུང་བ༌[^2442]བཞིན་ནོ་ཞེ་ན།[^2443] འདི་ལ་ནི་འཁྲུལ་པ་མེད་པའི་ཕྱིར་གཞན་གྱིས་གཞན་དྲན་པར་རིགས་ཀྱི་གང་ལས་འདི་ངེས་པར་དྲན་པར་འགྱུར་བ་རེག་བྱ་ལས༌[^2444]ནི་ཅུང་ཟད་ཀྱང་དབྱིབས་གང་ལ་ཡང་ངེས་པར་མེད་དོ། །

[Block 4193]
འོན་ཏེ་ལྷན་ཅིག་སྤྱོད་པར་ངེས་པ་མེད་ཀྱང་ངེས་པར་དབྱིབས་དྲན་པར་འགྱུར་ན་ནི་ཁ་དོག་ཀྱང་འགྱུར་རོ། །

[Block 4194]
ཡང་ན་ནི་ཁ་དོག་བཞིན་དུ་དབྱིབས་ཀྱང་ངེས་པར་མི་འགྱུར་བ་ཞིག་ན་དེ་ལྟ་ཡང་མ་ཡིན་པར༌[^2445]རེག་བྱ་ལས་འདི་དྲན་པར་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 4195]
རི་མོས༌[^2446]བཀྲམ་པ་ལ༌[^2447]དབྱིབས་དུ༌[^2448]མ་སྣང་བའི་ཕྱིར་མང་པོ་ཡང་ཕྱོགས་གཅིག་པར་འགྱུར་བ་ཞིག་ན་དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། ཁ་དོག་བཞིན་ནོ། །

[Block 4196]
དེ་ལྟ་བས་ན་དབྱིབས་ནི་རྫས་སུ་མེད་དོ། །

[Block 4197]
གང་ཡང་ཐོགས་པ་དང་བཅས་པའི་གཟུགས་ཅུང་ཟད་ཡོད་པ་དེ་ནི་གདོན་མི་ཟ་བར་རྡུལ་ཕྲ་རབ་ལ་ཡོད་པ་ཡིན་ན་དེ་རྡུལ་ལ་མེད་དེ། [^2449]རིང་པོ་ལ་སོགས་པའི་དབྱིབས་ནི་རྡུལ་ཕྲ་རབ་ལ་མེད་དོ། །

[Block 4198]
དེ་ལྟ་བས་ན་དབྱིབས་ནི༌[^2450]མང་པོ་དེ་ལྟར་གནས་པ་དག་ཁོ་ན་ལ་རིང་པོ་ལ་སོགས་པ་འདོགས་པར་ཟད་དོ། །

[Block 4199]
འོན་ཏེ་དབྱིབས་ཀྱི་རྡུལ་ཕྲ་རབ་དག་ཁོ་ན་དེ་ལྟར་གནས་པ་ལ་རིང་པོ་ལ་སོགས་པའི༌[^2451]མིང་འདོགས་པར་འདོད་ན་ནི་དེ་དག་མ་གྲུབ་པའི་ཕྱིར་དེ་ནི་ཕྱོགས་འཛིན་པ་འབའ་ཞིག་ཏུ་ཟད་དོ། །

[Block 4200]
རང་གི་མཚན་ཉིད་རྣམས་གྲུབ་ན་ནི་དེ་དག་བསགས་པ་རུང་བར་འགྱུར་ན་དབྱིབས་ཀྱི་ཡན་ལག་རྣམས་ནི་ཁ་དོག་ལ་སོགས་པ་དེ༌[^2452]བཞིན་དུ་རང་གི་ངོ་བོར༌[^2453]གྲུབ་པ་ཡང་མེད་ན་དེ་དག་བསགས་པ་ལྟ་ཞིག་ག་ལ་ཡོད། འོ་ན་གང་ཁམ་པའི་སྣོད་རྣམས་ཁ་དོག་ཀྱང་ཐ་མི་དད་པ་ལ་དབྱིབས་ཀྱང་ཐ་དད་པར་སྣང་ངོ་ཞེ་ན། ཇི་ལྟར་གནས་པར་གྱུར་པའི་ཁ་དོག་ལ་རིང་པོ་ལ་སོགས་པར་མིང་འདོགས་པར་ཟད་དོ་ཞེས་མ་བཤད་དམ། དཔེར་ན་གྲོག༌[^2454]མ་ལ་སོགས་པ་ཐ་མི་དད་བཞིན་དུ་འཁོར་ལོ་ལ་སོགས་པ་ཐ་དད་པར་འདོགས་པ་ལྟར་དབྱིབས་ཀྱང་དེ་དང་འདྲའོ། །

[Block 4201]
འོ་ན་གང་མུན་ཁུང་དང་ཐག་རིང་པོ་ནས་སྡོང་དུམ་ལ་སོགས་པའི་ཁ་དོག་མ་མཐོང་བར་རིང་པོ་ལ་སོགས་པ་མཐོང་བར་འགྱུར་རོ༌[^2455]ཞེ་ན། དེ་དག་གི༌[^2456]དེ་ཁ་དོག་མི་གསལ་བ༌[^2457]ཁོ་ན་མཐོང་ནས་རིང་པོ་ལ་སོགས་པར་ཡོངས་སུ་རྟོག་པར་བྱེད་དེ། ཕྲེང་བ་དང་དམག་ལ་སོགས་པ༌[^2458]ལ་ཡོངས་སུ་རྟོག་པ་བཞིན་ནོ། །

[Block 4202]
དེ་ནི་གདོན་མི་ཟ་བར་དེ་ལྟར་ཤེས་པར་བྱ་སྟེ། གང་རེས་འགའ་ཡོངས་སུ་ཆད་པ་ངེས་པར་མི་ཟིན་པ་ནི་ཚོགས་པ་ཙམ་དང་མི་གསལ་བ་སྣང་བ་ཡིན་ནོ། །

[Block 4203]
ཡང་ད་ནི་མདོ་སྡེ་པ་ཁྱེད་རྣམས་ཀྱི་ལུགས་ཀྱིས་ལུས་ཀྱི་འགྲོ་བ་དང་དབྱིབས་ཀྱང་བསལ༌[^2459]ནས་གང་ལ་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་དུ་འདོགས་པར་བྱེད་ཅེ་ན། དེ་དག་ནི་དབྱིབས་ཁོ་ན་ལ་ལུས་ཀྱིས༌[^2460]རྣམ་པར་རིག་བྱེད་འདོགས་པར་བྱེད་ལ་རྫས་སུ་ནི་མ་ཡིན་ནོ། །

[Block 4204]
དེ་ལ༌[^2461]འདོགས་པར་བྱེད་པ་ན་ཇི་ལྟར་ལུས་ཀྱི་ལས་སུ་འདོགས་པར་བྱེད་ཅེ་ན། ལུས་ལ་བརྟེན་པའི་ལས་ནི་ལུས་ཀྱི་ལས་ཏེ། དེ་དང་དེར་ལུས་འཇུག་པར་བྱེད་པའི་སེམས་པ་གང་ཡིན་པའོ། །

[Block 4205]
དེ་བཞིན་དུ་ངག་དང་ཡིད་ཀྱི་ལས་དག་ལ༌[^2462]ཡང་ཅི་རིགས་པར་རིག་པར་བྱའོ། །
--- END BLOCKS ---
