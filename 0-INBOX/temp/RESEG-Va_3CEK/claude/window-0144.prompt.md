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
[Block 5041]
ལུས་ལ་དམིགས་པ་ཡིན་ན་ཅིའི་ཕྱིར་ཕ་རོལ་གྱི་ལུས་ལ་དམིགས་པ་ཡང་མ་ཡིན། འབྲེལ་པ་མེད་པའི་ཕྱིར་ཏེ། འདི་ནི་ལུས་སམ་སེམས་གང་དང་ལྷན་ཅིག་འབྲེལ་པ་དེ་ཁོ་ན་ལ་བདག་ཏུ་འཛིན་པ་འདི་འབྱུང་གི་གཞན་ལ་ནི་མ་ཡིན་ཏེ། འཁོར་བ་ཐོག་མ་མེད་པ་ནས་དེ་ལྟར་གོམས་པའི་ཕྱིར་རོ། །

[Block 5042]
འབྲེལ་པ་ཡང་གང་ཞིག་ཡིན། རྒྱུ་དང་འབྲས་བུའི་དངོས་པོའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 5043]
གལ་ཏེ་བདག་མེད་པ༌[^3570]ན་བདག་ཏུ་འཛིན་པ་ནི་སུའི་ཡིན། འདི་ནི་དྲུག་པ་འདིའི་དོན་ཇི་ལྟ་བུ་ཡིན་ཞེས་བྱ་བ་ནས་དེ་ནི་དྲན་པའི་རྒྱུ་གང་ཡིན་པ་དེ་ཁོ་ན༌[^3571]ཡིན་ནོ་ཞེས་བྱ་བའི་བར་དེ་ཉིད་འོངས་པ་ཡིན་ནོ། །

[Block 5044]
འདིའི་རྒྱུ་གང་ཞིག་ཡིན་ཞེ་ན། སྔོན་བདག་ཏུ་འཛིན་པས་ཡོངས་སུ་བསྒོས་པ་རང་གི་རྒྱུད་ཀྱི་ཡུལ་ཅན་མ་རིག་པ་དང་བཅས་པའི་སེམས་ཡིན་ནོ། །

[Block 5045 [HEADING]]
#### བདེ་བའམ་སྡུག་བསྔལ་བ། ^6-3-9-0

[Block 5046]
བདག་མེད་ན་བདེ་བའམ་སྡུག་བསྔལ་བ་སུ་ཞིག་ཡིན། རྟེན་གང༌[^3572]བདེ་བའམ་སྡུག་བསྔལ་བ་འབྱུང་བ་སྟེ། དཔེར་ན་ཤིང་ལྗོན་པ་མེ་ཏོག་ཆགས་སོ། །

[Block 5047]
ནགས་ཚལ་འབྲས་བུ་ཆགས་སོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 5048]
འདི་གཉིས་ཀྱི་རྟེན་གང་ཞེ་ན། སྐྱེ་མཆེད་དྲུག་ཡིན་ཏེ། ཇི་ལྟར་ཡིན་པ་དེ་ལྟར༌[^3573]ནི་བཤད་ཟིན་ཏོ། །

[Block 5049 [HEADING]]
#### ལས་རྣམས་ཀྱི་བྱེད་པ་པོ་དང་འབྲས་བུ་རྣམས་ཀྱི་ཟ་བ་པོ། ^6-3-10-0

[Block 5050]
བདག་མེད་ན་ལས་རྣམས༌[^3574]ཀྱི་བྱེད་པ་པོ་ནི་གང་ཡིན། འབྲས་བུ་རྣམས་ཀྱི་ཟ་བ་པོ་གང་ཡིན། བྱེད་པ་པོ་ཞེས་བྱ་བའམ། ཟ་བ་པོ་ཞེས་བྱ་བའི་ཚིག་གི་དོན་ཇི་ལྟ་བུ་བྱེད་པས་ན༌[^3575]བྱེད་པ་པོ་ཡིན་ལ། ཟ་བས་ན་ཟ་བ་པོ་ཡིན་ནོ། །

[Block 5051]
རྣམ་གྲངས་སྨྲས་སུ་ཟིན་གྱི༌[^3576]དོན་ནི་མ་ཡིན་ནོ། །

[Block 5052]
མཚན་ཉིད༌[^3577]རྣམས་ནི་བྱེད་པ་པོའི་མཚན་ཉིད་རང་དབང་ཅན་ནི་བྱེད་པ་པོ་ཡིན་ནོ་ཞེས་ཟེར་ན། འཇིག་རྟེན་ན་འབྲས་བུ་འགའ་ལ་ཡང་ལ་ལ་ཞིག་རང་དབང་ཡོད་པ་ལྟ་བུ་མཐོང་ངམ། མཐོང་སྟེ་ཁྲུས་དང་ཟ་བ་དང་འགྲོ་བ་ལ་སོགས་པ་ལ་ལྷས་བྱིན་ལྟ་བུའོ། །

[Block 5053]
ཁྱོད་ལྷས་བྱིན་གང་ཞིག་དཔེར་བརྗོད། གལ་ཏེ་བདག་ཡིན་ནོ་ཞེ་ན་ནི་དེ་ཉིད་བསྒྲུབ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 5054]
འོན་ཏེ་ཕུང་པོ་ལྔ༌[^3578]ཡིན་ནོ་ཞེ་ན་ནི་དེ་ཉིད་བྱེད་པ་པོ་ཡིན་ཏེ། ལས་འདི་ནི་རྣམ་པ་གསུམ་སྟེ། ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས་སོ། །

[Block 5055]
དེ་ལ་རེ་ཞིག་ལུས་དང༌[^3579]ངག་གི་ལས་ལ་སེམས་ཀྱི་གཞན་གྱི་དབང་གིས་འཇུག་གོ། །

[Block 5056]
སེམས་ཀྱང་ལུས་དང་ངག་ལ་རང་གི་རྒྱུའི་གཞན་གྱི་དབང་གིས་འཇུག་གོ། །

[Block 5057]
དེ་ཡང་དེ་དང་འདྲ་བས་གང་ལ་ཡང་རང་དབང་མེད་དེ། དངོས་པོ་ཐམས་ཅད་ནི་རྐྱེན་གྱི་གཞན་གྱི་དབང་གིས་འཇུག་གོ། །

[Block 5058]
བདག་ཀྱང་ལྟོས་པ་མེད་པར་རྒྱུ་ཉིད་དུ་ཁས་མི་ལེན་པའི་ཕྱིར་རོ། །

[Block 5059]
རང་དབང་ཅན་དུ་མི་འགྲུབ་བོ། །

[Block 5060]
དེ་ལྟ་བས་ན་དེ་ལྟ་བུའི་མཚན་ཉིད་ཀྱི་བྱེད་པ་པོ་ནི་འགའ་ཡང་མི་དམིགས་སོ། །

[Block 5061]
གང་ཞིག་གང་གི་རྒྱུའི་གཙོ་བོ་ཡིན་པ་དེ་ནི་དེའི་བྱེད་པ་པོ་ཞེས་བྱ་ན་བདག་ནི་གང་ལ་ཡང་རྒྱུ་ཡིན་པར་མི་སྣང་སྟེ། དེ་ལྟ་བས་ན་དེ་ནི་དེ་ལྟ་བུར་ཡང་བྱེད་པ་པོར་མི་རུང་ངོ་། །དྲན་པ་ལས་ནི་འདུན་པ་སྐྱེའོ། །

[Block 5062]
འདུན་པ་ལས་ནི་རྟོག་པ་སྐྱེའོ། །

[Block 5063]
རྣམ་པར་རྟོག་པ་ལས་ནི་རབ་ཏུ་འབད་པའོ། །

[Block 5064]
རབ་ཏུ་འབད་པ་ལས་ནི་རླུང་ངོ་། །དེ་ལས་ནི་ལས་འབྱུང་ན་འདི་ལ་བདག་ཅི་ཞིག་བྱེད། འབྲས་བུ་ལ་ཡང་གང་ལ་བདག་མེད་ན་ཟ་བ་པོར་བརྟགས་པའི༌[^3580]ཉེ་བར་སྤྱོད་པ་དེ་གང་ཞིག་ཡིན། གལ་ཏེ་དམིགས་པ་ཡིན་ནོ་ཞེ་ན། དམིགས་པ་ལ་བདག་གི་ནུས་པ་མེད་དེ། རྣམ་པར་ཤེས་པ་ལ་ནུས་པ་བཀག་པའི་ཕྱིར་རོ། །

[Block 5065 [HEADING]]
#### སེམས་ཅན་གྱི་རྟེན་མ་ཡིན་པ་ལ་སྡིག་པ་དང་བསོད་ནམས། ^6-3-11-0

[Block 5066]
བདག་མེད་ན་ཅིའི་ཕྱིར་སེམས་ཅན་གྱི་རྟེན་མ་ཡིན་པ་ལ་ཡང་སྡིག་པ་དང་བསོད་ནམས་ཉེ་བར་སྩོགས༌[^3581]པར་མི་འགྱུར། ཚོར་བའི་རྟེན་མ་ཡིན་པའི་ཕྱིར་ཏེ། དེའི་རྟེན་ནི་སྐྱེ་མཆེད་དྲུག་ཡིན་གྱི་བདག་མ་ཡིན་ནོ། །

[Block 5067]
ཇི་ལྟར་ཡིན་པ་དེ་ལྟར་ནི་བཤད་ཟིན་ཏོ། །

[Block 5068 [HEADING]]
#### ལས་ཞིག་ཟིན་པ་ལས་ཚེ་ཕྱི་མ་ལ་འབྲས་བུ་འབྱུང་བ། ^6-3-12-0

[Block 5069]
བདག་མེད་ན༌[^3582]ཇི་ལྟར་ན་ལས་ཞིག་ཟིན་པ་ལས་ཚེ་ཕྱི་མ་ལ་འབྲས་བུ་འབྱུང་། བདག་ཡོད་ན་ཡང་ཇི་ལྟར་ན་ལས་ཞིག་ཟིན་པ་ལས་ཚེ་ཕྱི་མ་ལ་འབྲས་བུ་འབྱུང་། དེ་ལ་བརྟེན་པའི༌[^3583]ཆོས་དང་ཆོས་མ་ཡིན་པ་ལས་འབྱུང་ངོ་། །ཚིག་གི་ལུགས་འདི་ནི་དཔེར་ན་གང་གི་རྟེན་གང་ཡིན་པ་ལྟ་བུ་ཞེས་ལན་བཏབ་ཟིན་ཏོ། །

[Block 5070]
དེ་ལྟ་བས་ན་ཆོས་དང་ཆོས་མ་ཡིན་པ་རྟེན་མེད་པ་ཁོ་ན་ལས་འབྱུང་ངོ་། །ཁོ་བོ་ཅག་ཀྱང་ལས་ཞིག་ཟིན་པ་ལ༌[^3584]ཚེ་ཕྱི་མ་ལ་འབྲས་བུ་འབྱུང་བར་མི་སྨྲའོ། །

[Block 5071]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་རྒྱུད་ཡོངས་སུ་འགྱུར་བའི་ཁྱད་པར་ལས་ཏེ། ས་བོན་དང་འབྲས་བུ་བཞིན་ནོ། །

[Block 5072]
དཔེར་ན་ས་བོན་ལས་འབྲས་བུ་འབྱུང་བ་ཞེས་བྱ་བ་དེ་ནི་ཞིག་པ་ལས་འབྱུང་བ་ཡང་མ་ཡིན་ལ་མཇུག་ཐོགས༌[^3585]ཁོ་ནར་འབྱུང་བ་ཡང་མ་ཡིན་ནོ། །

[Block 5073]
འོ་ན་ཅི་ཞེ་ན། རྒྱུད་ཡོངས་སུ་འགྱུར་བའི་ཁྱད་པར་ལས་ཏེ། མྱུ་གུ་དང་སྡོང་བུ་དང་། འདབ་མ་ལ་སོགས་པ་མེ་ཏོག་ལ་ཐུག་པ་རིམ་པ་རྫོགས་པ་ལས་འབྱུང་བ་བཞིན་ནོ། །

[Block 5074]
དེ་ནི་མེ་ཏོག་ལས་གྲུབ་པ་ཡིན་ན་ཅིའི་ཕྱིར་ས་བོན་དེའི་འབྲས་བུ་ཞེས་བྱ་ཞེ་ན། དེས་བརྒྱུད་པས་མེ་ཏོག་ལ་དེའི་ནུས་པ་བསྐྱེད་པས་སོ། །

[Block 5075]
གལ་ཏེ་ས་བོན༌[^3586]དེ་སྔོན་དུ་འགྲོ་བར་མ་གྱུར་ན་འབྲས་བུ་དེ་འདྲ་བ་སྐྱེད་པ༌[^3587]ལ་དེའི་ནུས་པ་ཡོད་པར་མི་འགྱུར་རོ། །

[Block 5076]
དེ་བཞིན་དུ་ལས་ལས་འབྲས་བུ་འབྱུང་ངོ་། །[^3588]ཞེས་བྱ་བ་དེ་ཡང༌[^3589]ལས༌[^3590]ཞིག་པ་ལས་ཀྱང་མི་འབྱུང་ལ། མཇུག་ཐོགས་སུ་ཡང་མ་ཡིན་ནོ། །

[Block 5077]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། རྒྱུད་ཡོངས་སུ་འགྱུར་བའི་ཁྱད་པར་ལས་སོ། །

[Block 5078]
རྒྱུད་ནི་ཅི་ཡིན། ཡོངས་སུ་འགྱུར་བ་ནི་ཅི་ཡིན། ཁྱད་པར་ནི་ཅི་ཡིན་ཞེ་ན། ལས་སྔོན་དུ་འགྲོ་བའི་སེམས་ཕྱིར་ཞིང་འབྱུང་བ་གང་ཡིན་པ་དེ་ནི་རྒྱུད་ཡིན་ནོ། །

[Block 5079]
དེ་གཞན་དང་གཞན་དུ་སྐྱེ་བ་ནི་ཡོངས་སུ་འགྱུར་བ་ཡིན་ནོ། །

[Block 5080]
དེའི༌[^3591]མཇུག་ཐོགས་སུ་འབྲས་བུ་སྐྱེད་ནུས་པ་གང་ཡིན་པ་དེ་ནི་ཡོངས་སུ་འགྱུར་བ་གཞན་ལས་ཁྱད་པར་དུ་འཕགས་པའི་ཕྱིར་ཡོངས་སུ་འགྱུར་བའི་ཁྱད་པར་ཡིན་ཏེ། [^3592]དཔེར་ན་ཡང་སྲིད་པའི་ཉེ་བར་ལེན་པ་དང་བཅས་པའི་འཆི་བའི་སེམས་ལྟ་བུའོ། །
--- END BLOCKS ---
