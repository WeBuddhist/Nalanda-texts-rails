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

[Block 4171]
གློག་དང་འབྲུག་སྒྲ་ཆར་པ་དང་།

[Block 4172 [VERSE]]
སྤྲིན་དང་རླུང་དང་ཐོག་རྣམས་ནི། །
སེམས་ཙམ་ཡོད་པར་མེད་པ་ན། །
ནམ་མཁའི་དཀྱིལ་ལ་གྲུབ་མི་འགྱུར། །
དངོས་པོ་རྣམས་ཀྱི་བདག་ཉིད་ཀྱིས།[^2577] །

[Block 4173 [VERSE]]
ངོ་བོ་ཁ་ཅིག་རབ་གྲུབ་ན། །
མདུད་པའི་དབྱེ་བས་དེ་རྣམས་ཀྱི། །
དབྱེ་བ་དུ་མ་སྣང་མི་འགྱུར། །
ཁ་ཅིག་མཛེས་མ་གཞོན་ནུ་མ། །

[Block 4174 [VERSE]]
གཞན་ལ་དེ་ཉིད་དར་ལ་བབ། །
ལ་ལ་ཡི༌[^2578]ནི་ཚོན་པོ་སྟེ། །
ཁ་ཅིག་ལ་ནི་ཤ་ཕྲ་སྔོ། །
གང་ཚེ་སེམས་ཉིད་བུད་མེད་ཀྱི། །

[Block 4175 [VERSE]]
རྣམ་པ་ཉིད་དུ་སྐྱེས་གྱུར་ན། །
དེ་ཚེ་རང་སེམས་འདོད་ཅན་གྱིས། །
བདག་ཉིད་བདག་གིས་གང་གིས་སྤྱོད། །
རྣམ་པ་ཐམས་ཅད་བདག་རང་བཞིན། །

[Block 4176 [VERSE]]
བློ་དང་ལྡན་པས་ཐམས་ཅད་ནི། །
ཡུལ་རྣམས་ཉེ་བར་སྤྱོད་པའི་ཕྱིར། །
བྱིས་པ་བཞིན་དུ་མི་འཇུག་གོ། །
ལག་པས་ལག་པ་བཟུང༌[^2579]ནས་ནི། །

[Block 4177 [VERSE]]
རྨི་ལམ་འཁྲུལ་པ་བདག་ཉིད་ཀྱིས། །
རྐུན་མ་བདག་གིས་འཛིན༌[^2580]ཤེས་པའི།[^2581] །
རྣམ་པར་སྨྲ་བ་གཞན་གྱིས་སྨོད། །
སྐམ་པོ་རྩྭ་ལ་ཕྱུགས་རྣམས་ནི། །

[Block 4178 [VERSE]]
བཟའ་བའི་སེམས་ནི་མི་རྣམས་མིན། །
ཨེ་མ་འོ་རྣམ་པར་རྟོག་པ་འདི།[^2582] །
རྣལ་འབྱོར་པས་ཀྱང་བསམ་མི་ཁྱབ། །
མ་དྲན་པ་དང་ལུས་རེག་དང་། །

[Block 4179 [VERSE]]
[^2583]གཉིད་ལོག་པ་དང་རླུང་རྣམས་ཀྱིས། །
ཉ་དང་བྱ་དང་ཁྱི་དང་སྦྲུལ། །
སེམས་ཅན་དེ་དག་འཚོ་བར་འགྱུར། །
དབེན་ས་བརླག༌[^2584]ཤ་ཁྱི་དང་འདྲ། །

[Block 4180 [VERSE]]
རང་གི་འཁོར་དང་ཁྱབ་པ་སྟེ། །
གནོད་བྱེད་དང་ནི་གནོད་སྦྱིན་མོས།[^2585] །
ལས་སྣ་ཚོགས་པས་མཐོང་བར་འགྱུར། །
བཤང་གཅིས་ཁྱབ་པ་རྣག་རྒྱུ་བ། །

[Block 4181 [VERSE]]
ཡི་དགས་རྣམས་ཀྱིས་ཆུ་བོར་མཐོང་། །
དང་བ་དང་ནི་བསིལ་བའི་ཆུ། །
མིས་དེ་མཐོང་དང་བཏུང་བར་འགྱུར། །
འབྲས་བུ་འདོད་དང་མི་འདོད་པའི། །

[Block 4182 [VERSE]]
རྣམ་པ་ལས་ཀྱིས་ཡོངས་གནས་པ། །
རྣམ་ཤེས་དེ་དང་དེ་ཉིད་ཀྱིས། །
སྟོང་པའི་དོན་ལ་འཇུག་པར་འགྱུར། །
ཀྱེ་མའོ་ཡུལ་ནི་སྣ་ཚོགས་པ། །

[Block 4183 [VERSE]]
དུས་གཅིག་དུ་ནི་རྣམ་པ་མང་། །
རོལ་མོའི་ཚོགས་ཀྱི་སྒྲ་བཞིན་དུ། །
རྟོག་པ་ཉིད་དུ་རྗེས་འགྲོར་འགྱུར། །
གལ་ཏེ་དོན་ཡོད་དེ་མེད་པས། །

[Block 4184 [VERSE]]
དོན་གྱི་བྱ་བ་བྱེད་མི་འགྱུར། །
སྐྱུར་རྫས་གཞན་གྱིས༌[^2586]ཟོས་པ་ན། །
གཞན་གྱི་ཁ་ནས་ཁ་ཆུ་འབྱུང་། །
མཚན་མོར་ཁ་ཅིག་འབྲས་བུ་ནི། །

[Block 4185 [VERSE]]
ཟོས་པས་གཞན་ལ་སྨྲ་བྱེད་ན། །
གལ་ཏེ་སྐྱུར་ཟོས༌[^2587]དེས་སྨྲས་ན། །
ཉན་པོར་འགྱུར་བར་མི་འགྱུར་རམ། །
རྨི་ལམ་འདོད་པའི་མོ་ཕྲད་པས། །

[Block 4186 [VERSE]]
བདེ་བའི་ཕུན་སུམ་ཚོགས་རྒྱུ་མེད། །
དོན་མེད་པས་ཀྱང་ཁུ་བ་ནི། །
ཇི་ལྟར་ཤོར་བར་མི་འགྱུར་རམ། །
གོམས་པའི་སྟོབས་ཀྱིས་རྨི་ལམ་དུ། །

[Block 4187 [VERSE]]
མཐོང་ཡང་གལ་ཏེ་ཡོད་ཟེར་ན། །
བུ་མོའི་ལྟོ་ལས་བུ་སྐྱེས་པ། །
མཐོང་བ་ཞེས་བྱ་རིགས་པ་མིན། །
ཡུལ་རིངས༌[^2588]ལམ་དང་རི་རྣམས་དང་། །

[Block 4188 [VERSE]]
ཡུལ་རྣམས་ཁང་པའི་ནང་དུ་ནི། །
ཐ་དད་པ་ནི་རབ་མཐོང་བས། །
རྨི་ལམ་མཐོང་བ་དོན་མེད་པའོ། །

[Block 4189]
ཐེག་པ་ཆེན་པོའི་རྣལ་འབྱོར་སྤྱོད་པའི་གཞུང་ལ་འཇུག་པ་སློབ་དཔོན་ཀམ་པ་ལའི་ཞལ་སྔ་ལ་སོགས་པས་དཔེ་རྣམས་བསྟན་ཏོ། །

[Block 4190]
རྣམ་རིག་གི་རང་བཞིན་གྱི་ཆོས་ཐམས་ཅད་རྣམ་པར་གཞག་པའི༌[^2589]ཕྱིར་རོ། །

[Block 4191]
དེ་ཕྱིའི་རྣམ་པ་ཅན་གྱི་རྣམ་པར་ཤེས་པ་ཡིན་གྱི། །དོན་འཁྲུལ་པའི་རང་བཞིན་དུ་སྣང་ངོ་། །དོན་སྣང་བ་ཡང་གསུམ་སྟེ། ཡོད་པར་སྣང་བ་དང་།

[Block 4192 [VERSE]]
མེད་པར་སྣང་བ་དང་ལོག་པར་སྣང་བའོ། །
དེ་ལ་ཡོད་པར་སྣང་བ་ནི་དཔེར་ན།
བྱེ་མ་ནི་སྨིག་རྒྱུའི་རྣམ་པས་སོ། །

[Block 4193]
མེད་པར་སྣང་བ་ནི་རབ་རིབ་ཅན་གྱིས༌[^2590]སྐྲ་ཤད་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 4194]
ལོག་པར་སྣང་བ་ནི་དུང་དཀར་པོ༌[^2591]སེར་པོ་ལྟར་སྣང་བ་བཞིན་ནོ། །

[Block 4195]
དེ་ལྟར་སྣང་བ་གསུམ་གྱི་དབང་གིས་ཕྱི་རོལ་གྱི་དོན་མེད་པ་ཡང་རྨོངས་པའི་བློ་ཅན་གྱིས་གཟུང་བར༌[^2592]འགྱུར་རོ། །

[Block 4196]
སྨོན་པའི་འབྲས་བུ་ཞེས་པ་ནི་དེ་ཉིད་རྣམ་པར་རིག་པའི་རང་བཞིན་ཕྱི་རོལ་གྱི་དོན་སྣང་བའི་ཕྱིར་རོ། །

[Block 4197]
དེ་ཡང་མེད་དེ་ཞེས་པ་ལ་ཕྱི་དང་ནང་གི་ངོ་བོ་མེད་དོ། །

[Block 4198]
སྨོན་ལམ་ལ་སོགས་པའི་ཉེ་བར་དམིགས་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་པ་ནི། འདུན་པ་ནི་སྨོན་ལམ་སྟེ། ཕྱིའི་རྣམ་པ་ཉིད་དུ་མངོན་པར་ཞེན་པའོ། །

[Block 4199]
དེའི་ཉེ་བར་དམིགས་པ་ནི་གཟུང་བ་འཛིན་པའི་ཚུལ་གྱིས་གཟུང་བའོ། །

[Block 4200]
མེད་པ་ནི་དེའི་ངོ་བོ་མེད་པའི་ཕྱིར་རོ། །

[Block 4201]
ཇི་སྐད་དུ།

[Block 4202 [VERSE]]
ཡང་དག་མ་ཡིན་ཀུན་རྟོག་ཡོད། །
དེ་ལ་གཉིས་པོ་ཡོད་མ་ཡིན། །
དེ་ལ་སྟོང་པ་ཉིད་ཡོད་དེ། །
དེ་ལ་ཡོད་ན༌[^2593]དེ་ཡོད་དོ། །

[Block 4203 [VERSE]]
ཡོད་དང་མེད་དང་ཡོད་པའི་ཕྱིར། །
དེ་ཡང་དབུ་མའི་ལམ་ཡིན་ནོ། །

[Block 4204]
ཞེས་འབྱུང་ངོ་། །དེ་བས་ན་ཕྱི་རོལ་གྱི་དངོས་པོ་ལྟ་བུར་བསྒོམ་པ་དམིགས་སུ་མེད་ཅིང་ཡོད་པ་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནི་རྣམ་པར་ཤེས་པའི་རྣམ་པ་དངོས་པོ་སོ་སོར་སྣང་བའི་རྟོག་པ་ནི་མེད་དོ། །

[Block 4205]
སེམས་ཀྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །ཞེས་པ་ནི་སེམས་ཉིད་སོ་སོར་སྣང་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
