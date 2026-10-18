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
[Block 4061]
འོ་ན་དེ་དག་ཇི་ལྟར་བསམ་གཏན་བཞིའི་ས་པར་གྲུབ་ཅེ་ན། རྟེན་གྱི་དབང་གིས་དེའི་ས་བསྟན་པའི་ཕྱིར་ཏེ། དེའི་རྟེན༌[^2907]མིག་དང་རྣ་བ་ནི༌[^2908]བསམ་གཏན་བཞིའི༌[^2909]ས་པ་ཡིན་ནོ། །

[Block 4062]
ཡང་ན་བར་ཆད་མེད་པའི་ལམ་གྱི་དབང་གིས་སོ། །

[Block 4063]
གཞན་བཞི་ནི་དགེ་བ་དག་ཡིན་ནོ། །

[Block 4064]
འོ་ན་རབ་ཏུ་བྱེད་པ་ལས་མངོན་པར་ཤེས་པ་གང་ཞེ་ན། ཤེས་པ་དགེ་བ་ཡིན་ནོ་ཞེས་གང༌[^2910]བཤད་པ་ཇི་ལྟ་བུ་ཞེ་ན། དེ་ནི་གཙོ་བོའམ་ཕལ༌[^2911]ཆེ་བ་བསྟན་པ་ཡིན་ནོ། །

[Block 4065 [HEADING]]
### རིག་པ་གསུམ། ^4-15-0

[Block 4066]
མངོན་པར་ཤེས་པ་འདི་རྣམས་ལས། །

[Block 4067]
གསུམ་ནི་རིག་པ། སྔོན་གྱི་གནས་དང་། འཆི་འཕོ་བ་དང་སྐྱེ་བ་དང་། ཟག་པ་ཟད་པ་ཤེས་པ་མངོན་སུམ༌[^2912]དུ་བྱ་བ་རྣམས་ནི་མི་སློབ་པའི་རིག་པ་གསུམ་ཞེས་བྱའོ། །

[Block 4068]
ཅིའི་ཕྱིར་དེ་དག་ཁོ་ན་ཡིན་གྱི་གཞན་དག༌[^2913]མ་ཡིན་ཞེ་ན། སྔོན༌[^2914]མཐའ་སོགས། མ་རིག་པ་ནི༌[^2915]བཟློག་ཕྱིར་རོ། །

[Block 4069]
འདི་དག་གིས་ནི་གོ་རིམས་བཞིན་དུ༌[^2916]སྔོན་གྱི་མཐའ་དང་། ཕྱི་མའི་མཐའ་དང་། བར་ལ་ཀུན་དུ་རྨོངས་པ་ཟློག་པར་བྱེད་དོ། །

[Block 4070]
དེ་དག་ལས་ཀྱང་དོན་དམ་པར་མི་སློབ་ཐ་མ། ཟག་པ་ཟད་པ་མངོན་དུ་བྱ་བ་ཁོ་ན་མི་སློབ་པའི་རིག་པ་ཡིན་ནོ། །

[Block 4071]
གཉིས་ནི་དེའི། རྒྱུད་ལས་སྐྱེས་ཕྱིར་དེ་ཞེས་བྱ། །གཞན་གཉིས་ནི་མི་སློབ་པའི་རྒྱུད་ལས་སྐྱེས་པའི་ཕྱིར་མི་སློབ་པ་ཞེས་བྱའི་དེ་གཉིས་ནི་སློབ་པ་ཡང་མ་ཡིན་ལ་མི་སློབ་པ་ཡང་མ་ཡིན་ནོ། །

[Block 4072]
མངོན་པར་ཤེས་པ་འདི་དག་སློབ་པའི་ཡིན་པར་མི་འདོད་དམ་ཞེ༌[^2917]ན་གང་གི་ཕྱིར་སློབ་པའི་རིག་པ་དག་ཅེས་མི་བྱ་ཞེ་ན།

[Block 4073 [VERSE]]
སློབ་ལ་འདོད་དེ་མ་རིག་དང་། །
བཅས་རྒྱུད་ཕྱིར་ན་རིག་མ་བཤད། །

[Block 4074]
རྒྱུད་མ་རིག་པ་དང་བཅས་བཞིན་དུ་རིག་པ༌[^2918]རྣམ་པར་གཞག་ཏུ་ནི་མི་རུང་སྟེ། ཡང་མ་རིག་པས་ཟིལ་གྱིས་གནོན་པའི་ཕྱིར་རོ། །

[Block 4075 [HEADING]]
### ཆོ་འཕྲུལ་གསུམ། ^4-16-0

[Block 4076 [VERSE]]
མངོན་པར་ཤེས་པ་འདི་དག་ལས། །
དང་པོ་གསུམ་པ་དྲུག་པ་ནི། །
ཆོ་འཕྲུལ་རྣམས་ཡིན༌[^2919]རྫུ་འཕྲུལ་དང་། །

[Block 4077]
སེམས་ཀྱི་རྣམ་གྲངས་དང་། ཟག་པ་ཟད་པའི་མངོན་པར་ཤེས་པ་རྣམས་ནི་གོ་རིམས་བཞིན་དུ་ཆོ་འཕྲུལ་གསུམ་ཡིན་ཏེ། རྫུ་འཕྲུལ་དང་ཀུན་རྫོབ་པ་དང་རྗེས་སུ་བསྟན་པའི་ཆོ་འཕྲུལ་རྣམས་ཡིན་ནོ། །

[Block 4078]
[^2920]

[Block 4079]
དང་པོ་ཉིད་དུ་གདུལ་བྱའི་ཡིད་ཤིན་ཏུ་འཕྲོག་པར་བྱེད་པའི་ཕྱིར་ཆོ་འཕྲུལ་དག་ཡིན་པ་འམ། འདི་དག་གིས་ཞེ༌[^2921]འགྲས་པ་དང་། བར་མར་གནས་པ་རྣམས་ཀྱི་ཡིད་འཕྲོག་པར་བྱེད་པས་ན་ཆོ་འཕྲུལ་དག་ཡིན་ནོ། །

[Block 4080]
འདི་དག་གི་ནང་ན། བསྟན་པ་མཆོག །

[Block 4081 [VERSE]]
རྗེས་སུ་བསྟན་པའི་ཆོ་འཕྲུལ་ནི། །
མི་འཁྲུལ་ཕྱིར་དང༌[^2922]ཕན་པ་དང་། །
ཡིད་འོང༌[^2923]འབྲས་ལ་སྦྱོར་བྱེད་ཕྱིར། །

[Block 4082]
མཆོག་ཡིན་ནོ། །

[Block 4083]
རྫུ་འཕྲུལ་དང་ཀུན་བརྗོད་པ་དག་ནི་རིག་སྔགས་ཀྱིས་ཀྱང་། བྱེད་དེ། གྷན་དྷ་རི་ཞེས་བྱ་བའི་རིག་སྔགས་གང་གིས་ན་ནམ་མཁའ་ལ་འགྲོ་བ་དང་། རྟོག་བྱེད་ཅེས་བྱ་བའི་རིག༌[^2924]སྔགས་གང་གིས་ན་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ཡང་ཡོད་མོད༌[^2925]ཀྱི་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རྗེས་སུ་བསྟན་པ་ནི་གཞན་གྱིས༌[^2926]བྱ་བར་མི་ནུས་པས༌[^2927]མི་འཁྲུལ་པའི་ཕྱིར་འདི་ནི་གཙོ་བོ་ཡིན་ནོ། །

[Block 4084]
དེ་གཉིས་ཀྱིས་ནི་གཏོད་པ༌[^2928]ཙམ་དུ་ཟད་ཀྱི་རྗེས་སུ་བསྟན་པའི་ཆོ་འཕྲུལ་གྱིས་ནི་ཐབས༌[^2929]ཉེ་བར་བསྟན་པའི་སྒོ་ནས་ཕན་པ་དང་། ཡིད་དུ་འོང་བའི་འབྲས་བུ་ལ་སྦྱོར་བས་འདི་ཉིད་མཆོག་ཡིན་ནོ། །

[Block 4085 [HEADING]]
### རྫུ་འཕྲུལ། ^4-17-0

[Block 4086]
རྫུ་འཕྲུལ་ཞེས་བྱ་བ་འདི་ཅི་ཡིན་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ཀྱིས༌[^2930]ནི། རྫུ་འཕྲུལ་ཏིང་ངེ་འཛིན། འདིས་འབྱོར་པར་བྱེད་པས་ན་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4087 [HEADING]]
#### འགྲོ་བ། ^4-17-1-0

[Block 4088]
དེས་ཅི་ཞིག་ཡང་དག་པར་འབྱོར་པར་འགྱུར་ཞེ་ན། དེ་ལས་ནི། སྤྲུལ་དང་འགྲོ་བ་སྟེ། དེ་ལ་འགྲོ་བ་ནི་རྣམ་པ་གསུམ་སྟེ། ལུས་ཀྱིས་ཕྱིན་བྱེད༌[^2931]དང་། མོས་པ་ལས་བྱུང་བ་དང་། ཡིད་མགྱོགས་པའོ། །

[Block 4089 [HEADING]]
##### ཡིད་མགྱོགས་ཀྱི་འགྲོ་བ། ^4-17-1-1-0

[Block 4090]
སྟོན་པ་ལ། ཡིད་མགྱོགས་འགྲོ་བ་དང་།[^2932] ཡིད་བཞིན་དུ་མགྱོགས་པས་ནི༌[^2933]ཡིད་མགྱོགས་ཀྱི་འགྲོ་བ་སྟེ། དེ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཁོ་ན་ཡིན་གྱི་གཞན་གྱི་ནི་མ་ཡིན་ནོ། །

[Block 4091]
ཡུལ་ཐག་ཤིན་ཏུ་རིང་པོར་ཡང་ཐུགས་བསྐྱེད་པའི་དུས་ཀྱི་བྱོན་པའི་ཕྱིར་རོ། །

[Block 4092]
དེ་ཉིད་ཀྱི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་སངས་རྒྱས༌[^2934]ཀྱི་ཡུལ་ནི་བསམ་གྱིས་མི་ཁྱབ་པོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 4093]
འགྲོ་བ་གཞན་དག་ནི་མ་བཤད་ཀྱང་སངས་རྒྱས་ལ་མངའ་བར་གྲུབ་པོ། །

[Block 4094 [HEADING]]
##### ལུས་ཕྱིན་བྱེད་ཀྱི་འགྲོ་བ། ^4-17-1-2-0

[Block 4095]
གཞན་དག་ལ། ཕྱིན་བྱེད་མོས་པ་ལས་བྱུང་ཡང་། །ཉན་ཐོས་དང་རང་སངས་རྒྱས་རྣམས་ལ་ནི་ལུས་ཕྱིན་བྱེད་ཀྱི་འགྲོ་བ་ཡང་ཡོད་དེ། བྱ་བཞིན་དུ་རིམ་གྱིས༌[^2935]ལུས་ཕྱིན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 4096 [HEADING]]
##### མོས་པ་ལས་བྱུང་བ། ^4-17-1-3-0

[Block 4097]
མོས་པ་ལས་བྱུང་བ་ཡང་ཡོད་དེ། ཐག་རིང་པོ་ལ་ཉེ་བར་མོས་ནས་མྱུར་དུ་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 4098 [HEADING]]
#### སྤྲུལ་པ། ^4-17-2-0

[Block 4099]
སྤྲུལ་པ་ནི་རྣམ་པ་གཉིས་ཏེ། འདོད་པ་ན་སྤྱོད་པ་དང་། གཟུགས་ན་སྤྱོད་པའོ། །

[Block 4100 [HEADING]]
##### འདོད་པར་གཏོགས་པའི་སྤྲུལ་པ། ^4-17-2-1-0
--- END BLOCKS ---
