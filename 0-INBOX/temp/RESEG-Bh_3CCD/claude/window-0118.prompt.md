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
[Block 4131 [VERSE]]
རྗེ་བཙུན་རིན་ཆེན་ཏཱ་ལ་ལས་ཀྱང་། །
ཇི་ལྟར་རློན་པ་ཆུ་ཤིང་སྡོང་བུ་ནི། །
སྙིང་པོ་འདོད་པའི་སྐྱེས་བུས་རྣམ་པར་དཔྱོད། །
ཕྱི་དང་ནང་ན་སྙིང་པོ་དེ་མེད་པ། །

[Block 4132]
ཆོས་རྣམས་ཐམས་ཅད་དེ་ལྟར་ཤེས་པར་གྱིས། །ཞེས་འབྱུང་ངོ་། །ཡང་ན་རྒྱུ་ནི་ཕ་རོལ་པ༌[^2554]རྣམས་ཀྱིས་ཡོངས་སུ་བརྟགས་པ་བདག་དང་དབང་ཕྱུག་ལ་སོགས་པའོ། །

[Block 4133]
དེ་རྣམས་རྣམ་པར་དཔྱད་ན་འགྲུབ་པར་མི་འགྱུར་ཏེ། ངོ་བོ་མེད་པའི་ཕྱིར་རོ། །

[Block 4134]
འབྲས་བུ་ཡང་དེ་ཁོ་ན་ཉིད་ཉི་ཤུ་རྩ་བཞིའི་རང་བཞིན་རྣམ་པར་དཔྱད་ན་མི་འགྲུབ་སྟེ། རྒྱུ་རྣམས་མེད་པའི་ཕྱིར་རོ། །

[Block 4135]
དེ་རྣམས་མེད་པ་ཁོ་ན་སྔར་བཤད་ཟིན་ཏོ། །

[Block 4136]
རྒྱུ་མ་གྲུབ་ན་འབྲས་བུ་གང་ལས་འབྱུང་བར་འགྱུར་ཏེ། རྒྱུ་མེད་པས་འབྲས་བུ་མེད་པའི་ཕྱིར་རོ། །

[Block 4137]
དེ་བས་ན་བདག་དང་དབང་ཕྱུག་ལ་སོགས་པའི་རྒྱུ་ཡིས་སྤྲུལ་པ་བསྟན་པ་དང་། གཡོ་བ་ལ་སོགས་པའི་སེམས་ཅན་སྣོད་དུ་གྱུར་པ་ཁམས་གསུམ་གྱི་ནང་ན་གནས་པའི་དངོས་པོའི་ཚོགས་ནི་དོན་དམ་པར་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 4138]
ཇི་སྐད་དུ།

[Block 4139 [VERSE]]
བདག་དང་ཆོས་སུ་ཉེར་བརྟགས་པའི། །
གང་ཞིག་རྣམ་པ་དུ་མ་འཇུག །
[^2555]དེ་ཡང་རྣམ་ཤེས་གཡོས་འགྱུར་བ། །

[Block 4140]
ཞེས་འབྱུང་ངོ་། །དེ་བཞིན་དུ།

[Block 4141 [VERSE]]
བདག་ཅེས་བྱ་བ་དངོས་པོ་མེད། །
བྱེད་པ་པོ་ཞེས་ག་ལས་བརྗོད། །
ཆོས་ཅན་ཡོད་ན་འཇིག་རྟེན་པས། །
ཆོས་རྣམས་ལ་ནི་བསམ་པ་འགྱུར། །

[Block 4142 [VERSE]]
ཕུང་པོ་བདག་མིན་དེར་དེ་མིན། །
དེ་ལ་དེ་མིན་དེ་མེད་མིན། །
བདག་དང་ཕུང་པོ་མེ་ཤིང་བཞིན། །
འདྲེས་མིན་བདག་དེས་ཇི་ལྟར་ཡོད། །

[Block 4143]
ཅེས་འབྱུང་བས་སོ། །

[Block 4144]
དབང་ཕྱུག་ལ་སོགས་པའི་དགག་པའི་སྒོ་དེས་མཚན་མ་མེད་པ༌[^2556]ཞེས་བྱ་བ་རྣམ་པར་ཐར་པ་གཉིས་པ་བསྟན་ཏོ། །

[Block 4145]
སྨོན་པ་བཟློག་པའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པས་རང་དབང་གི་རྣམ་པར་རྟོག་པ་ཡོངས་སུ་དགག་པར་བྱ་བའི་ཕྱིར་བཤད་པར་བྱ་སྟེ། དེ་ལྟར་ཞེས་བྱ་བ་ནི་དངོས་པོ་དང་དེའི་བྱེད་པ་པོ་ཚད་མ་མེད་པས་བཀག་ན་དེའི་དོན་དང་བྲལ་བའི་རྣམ་པར་རྟོག་པ་ཡང་མི་འགྲུབ་པོ། །དེ་ལྟར་ཕྱི་རོལ་གྱི་རྣམ་པ་ཞེས་པ་ནི་རྣམ་པར་རིག་པ་སྨྲ་བ་རྣམས་ཀྱིས་འདི་ལྟར་ཁས་བླངས་ཏེ། རྣམ་པར་ཤེས་པ་འབའ་ཞིག་ཏུ་འདི་སྣང་བ་ཡིན་གྱི༌[^2557]དོན་ནི་མེད་དེ། གཅིག་དང་དུ་མ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 4146]
ཇི་ལྟར་སྣང་བ་རྣམ་པ་སྣ་ཚོགས་པ་མཐའ་ཡས་པ་སྤྲོས་པའི་ངོ་བོའི་དངོས་པོའི་ཚོགས་ནི་རྣམ་པར་ཤེས་པའི་སོ་སོར་སྣང་བ་ཡིན་ནོ། །

[Block 4147]
འདི་ལྟ་སྟེ། གང་དང་གང་རང་གི་སྣང་བའི་རང་བཞིན་དེ་ནི་ཡོད་དེ། །[^2558]གང་རང་སྣང་བ་མ་ཡིན་པ་དེ་ནི་མེད་དོ། །

[Block 4148]
གཟུགས་ལ་སོགས་པ་དངོས་པོ་རྣམས་ནི་གཞན་གྱི་སྣང་བ་ཡིན་ནོ། །

[Block 4149]
གང་གིས་དེ་རྣམས་སྣང་བར་བྱ་བ་དེ་ཉིད་རྣམ་པར་ཤེས་པ་དོན་དམ་པར་ཡོད་ལ། ཕྱི་རོལ་གྱི་དོན་ནི་འཁྲུལ་པས་བརྟགས་པར་བྱས་ཏེ། རྣམ་པར་ཤེས་པ་ནི་དོན་གྱི་རྣམ་པ་ཡིན་པའི་ཕྱིར་ཟླ་བ་གཉིས་སོ་སོར་སྣང་བའི་ཤེས་པ་བཞིན་ནོ། །

[Block 4150]
གལ་ཏེ་ཕྱི་རོལ་གྱི༌[^2559]དོན་དམ་པར་ཡོད་པར་འགྱུར་ན་དེའི་ཚེ་བུད་མེད་ཀྱི༌[^2560]རོས་མི་རྟག༌[^2561]པའི་ཤེས་པ་འདི༌[^2562]ཉིད་སྐྱེ་བ་ཡིན་གྱི་ཐ་དད་པ་ནི་མ་ཡིན་ནོ། །

[Block 4151 [VERSE]]
བུད་མེད་རོ་ནི་གཅིག་པུ་ལ། །
དགེ་སློང་འདོད་པ་ཁྱི་རྣམས་ཀྱིས། །
རོ་དང་འདོད་མ་བཟའ་བ་ཞེས། །
རྣམ་པར་རྟོག་པ་གསུམ་བྱུང་ངོ་། །

[Block 4152]
ཞེས་དང་། དེ་བཞིན་དུ།

[Block 4153 [VERSE]]
ཉིན་དང་མཚན་མོ་སྣང་བའི་དོན། །
ལོང་བ་ཡི་ནི་འདྲ་བ་ན། །
ནང་པར་ཤེས་བྱ་སྒྲ་ཐོས་པས། །
སྣང་བ་དང་བཅས་འདྲ་བར་འགྱུར། །

[Block 4154 [VERSE]]
མི་གཙང་བ་ཡི་རི་དགས་ཀྱིས། །
མེ་ཟ་དུག་ནི་དུག་བྱི་བས། །
ཟོས་ཀྱང་ཤི་བར་མི་འགྱུར་རོ། །
སྲོག་ནི་ཐར་བྱེད་རྫས་ཀྱིས་སོ། །

[Block 4155 [VERSE]]
བྱིས་པ་རྣམས་ཀྱིས་ཡང་དང་ཡང་། །
གང་དང་གང་ནི་བསྒོམ༌[^2563]བྱ་བ། །
གོམས་པའི་སྟོབས་ཀྱིས༌[^2564]སྦྱོར་བ་ཡིས། །
དེ་དང་དེ་ནི་མདུན་དུ་སྣང་། །

[Block 4156 [VERSE]]
གོས་ཀྱི་རྣམ་པས་བཀབ་པ་ཡང་། །
མ་གོམས་པས་ནི་ཡན་ལག་གནོད། །
གངས་ཀྱི་ཚོགས་ནི་མ་རུངས་པས། །
མིག་ལ་མི་གནོད་ངོ་མཚར་ཆེ། །

[Block 4157 [VERSE]]
གོམས་པའི་སྦྱར་བའི་ནུས་པ་ཡིས། །
ཀོ་བ་ལག་པས་མཉེས་བྱེད་པའི། །
ལྷམ་མཁན་གྱི༌[^2565]ནི་དྲི་མི་ཞིམ། །
གནོད་པར༌[^2566]བྱེད་པར་མི་འགྱུར་རོ། །

[Block 4158 [VERSE]]
དང་པོར་ལུས་ཅན་རྣམས་ཀྱིས་ནི། །
དུག་རྣམས་ཟོས་ན༌[^2567]ཤི་བར་འགྱུར། །
དེ་ཉིད་གོམས་པའི་སྦྱོར་བ་ཡིས། །
མཐར་ནི་བཅུད་ཀྱིས་ལེན་པར་འགྱུར། །

[Block 4159 [VERSE]]
གལ་ཏེ་འབྱུང་བ་འདི་རྣམས་ནི། །
ཤེས་པའི་ངོ་བོར་མི་རྟག་ན། །
རྐང་ལག་ལ་སོགས་བྱ་བ་རྣམས། །
བྱ་བ་གཞན་ལ་ཇི་ལྟར་འཇུག །

[Block 4160 [VERSE]]
ཕ་མའི་ཁྲག་དང་ཁུ་བ་ལས། །
མགོ་ལག་ལ་སོགས་ཇི་ལྟར་འགྱུར། །
ས་བོན་ལས་སྐྱེས་ཡལ་ག་ཅན། །
ཇི་ལྟར་ཞིང་རྣམས་སྐྱེ་བར་འགྱུར། །

[Block 4161 [VERSE]]
སྒྲ་ནི་ཁ་ལས་བྱུང་བ་དང་། །
རྫ་རྔ་ལས་ཀྱང་ཇི་ལྟར་བྱུང་། །
དེ་ཡི་རྒྱུ་རྣམས་རེ་རེ་ལ། །
རང་བཞིན་མེད་པ༌[^2568]མཐོང་ཕྱིར་རོ། །

[Block 4162 [VERSE]]
བྱ་རྣམས་ནམ་མཁར༌[^2569]འགྲོ་བ་དང་། །
མུན་ཁུང་ལ་ཡང་དོན་མཐོང་བ། །
ཁང་པར་བྱི་བ་ལ་སོགས་པས། །
མཚོ་ལ་སོགས་པར་ཉས་དོན་མཐོང་། །

[Block 4163 [VERSE]]
སྦྲུལ་རྣམས་ཀྱི༌[^2570]ནི་མིག་དག་གིས། །
ཐོས་པ་དང་ནི་མཐོང་བར་འགྱུར། །
དེ་བཞིན་འཁོར་བར་དུ་མ་ནི། །
གཞན་དང་གཞན་གྱིས་འགལ་བར་སྣང་། །

[Block 4164 [VERSE]]
གནས་དང་དབྱིབས་ནི་མ་མཐོང་བའི། །
གོམས་པའི་དབང་གིས་སྒྲ་ཐོས་ནས། །
ཡེ་ཤེས་རྟོགས་པ་རྣམས་མེད་ན། །
འབེན་ལ་མདའ་རྣམས་ཇི་ལྟར་ཕབ། །

[Block 4165 [VERSE]]
བརྗོད་པ་ཡང་ནི་མ་གོམས་པས། །
ཇི་ལྟར་ཁ་ཐོན་འབྱུང་བར་འགྱུར། །
གལ་ཏེ་རྣམ་རིག་རྒྱུན་བཞིན་དུ། །
རབ་ཏུ་རྒྱུ་བར་མི་འགྱུར་རོ། །

[Block 4166 [VERSE]]
རི་བོའི་ཚོགས་ནི་མཐོ་བ་དང་། །
རྒྱ་མཚོ་ཆེན་པོ་དཀྱིལ་མེད་པ། །
རྡུལ་ནི་ཕྲ་རབ་གཡོ༌[^2571]བསྡུས་ནས། །
ལས་བྱེད་གང་གིས་བྱེད་པ་ཡིན། །

[Block 4167 [VERSE]]
ལྕགས་ལ་སོགས་པ་དགུག་པའི་ཕྱིར། །
རྡོ་ནི་ཁབ་ལེན་ལ་སོགས་དང་། །
སྔགས་རྣམས་དང་ནི་སྨན་རྣམས་ཀྱི། །
ནུས་པ་གང་གིས་བྱས་པ་ཡིན། །

[Block 4168 [VERSE]]
དེ་བསམ༌[^2572]རིག་སྣ་ཚོགས་པས། །
ཅོག་ཆུང༌[^2573]གིས༌[^2574]ནི་སྐད་རྒྱས་བཞིན། །
ཇི་ལྟར་འདི་དག་ཐམས་ཅད་སྣང་། །
སེམས་ཉིད་ཀྱི༌[^2575]ནི་སྤྲུལ་པ་ཡིན། །

[Block 4169 [VERSE]]
ཟད་པར་སྐྱེ་མཆེད་སྒོམ་པ༌[^2576]ནི། །
རྣལ་འབྱོར་པ་ཡིས་ཇི་ལྟར་སྦྱར། །
བརྟན་པའི་རང་བཞིན་དངོས་པོ་རྣམས། །
གཞན་དང་གཞན་དུ་བཞག་པ་མེད། །

[Block 4170 [VERSE]]
ཤེལ་དང་འདྲ་བ་དུ་མ་ནི། །
དེ་ལྟར་འཁྲུལ་པས་སྦྱར་བར་རིགས། །
བག་ཆགས་ཆུ་ལ་ཏིལ་མར་བཞིན། །
སེམས་ཉིད་འདི་ནི་ཁྱབ་པར་འགྱུར། །
--- END BLOCKS ---
