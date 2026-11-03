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
[Block 4341]
ཡང་ན་ལྷའི་མིག་དང་རྣ་བ་དག་ཀྱང་དགེ་བ་ཉིད་དུ་ཐལ་བར་འགྱུར་བས་འདི་ལ་འབད་པར་བྱའོ།[^2612] །མཐོང་ནས༌[^2613]སྤང་བར་བྱ་བའི་སེམས་ནི་རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བར་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་གང་བཤད་པ། འོ་ན་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་ལོག་པར་ལྟ་བ་དེ་ལས་ནི་ལོག་པར་རྟོག་པ་དང་ལོག་པའི་ངག་དང་ལོག་པའི་ལས་ཀྱི་མཐའ་འབྱུང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་གསུངས་ཤེ་ན། འདི་ནི་འགལ་བ་མེད་དེ། འདི་ལྟར།

[Block 4342 [VERSE]]
ཀུན་སློང་རྣམ་གཉིས་རྒྱུ་དང་ནི། །
དེ་ཡི་དུས་ཀྱིས་སློང་ཞེས་བྱ། །

[Block 4343]
ཀུན་ནས་སློང་བ་ནི༌[^2614]རྣམ་པ་གཉིས་ཏེ། རྒྱུའི་ཀུན་ནས་སློང་བ་དང་། དེའི་དུས་ཀྱིས༌[^2615]ཀུན་ནས་སློང་བ་སྟེ། དེའི་དུས་ཁོ་ན་ན་དེ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 4344 [VERSE]]
གཉིས་ལས་དང་པོ་རབ་འཇུག་བྱེད། །
གཉིས་པ་རྗེས་སུ་འཇུག་བྱེད་ཡིན། །

[Block 4345]
རྒྱུའི་ཀུན་ནས་སློང་བ་ནི་འཕེན་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 4346]
དེའི་དུས་ཀྱིས༌[^2616]ཀུན་ནས་སློང་བ་ནི་བྱ་བའི་དུས་སུ་མཐུན་པར་འཇུག་པའི་ཕྱིར་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 4347]
ད་ནི་བྱ་བ་དེ་ལ་དེའི༌[^2617]ནུས་པ་ཅི་ཞིག་ཡོད། འཕངས་སུ་ཟིན་ཀྱང་དེ་མེད་ན་ཤི་བ་བཞིན་དུ་དེ་ཡོད་པར་མི་འགྱུར་རོ། །

[Block 4348]
འོ་ན་སེམས་མེད་པའི་སྡོམ་པ་སྐྱེ་བ་ལ་ཇི་ལྟར་ཡོད། འོ་ན་ནི་སེམས་དང་བཅས་པ་ལ་ཆེས་གསལ་བ་ཡིན་པས་ནུས་པ་ནི་དེ་ཡིན་ནོ། །

[Block 4349]
དེ་ལ་ཡང་། མཐོང་བས་སྤང་བྱའི་རྣམ་ཤེས་ནི། །རབ་ཏུ་འཇུག་བྱེད་ཡིན། མཐོང་བས་སྤང་བར་བྱ་བའི་སེམས་ནི་དེ་ཀུན་ནས་སློང་བར་བྱེད་པ་རྟོག་པ་དང་དཔྱོད་པ་དག་གི་གཞིར་གྱུར་པའི་ཕྱིར་རྣམ་པར་རིག་བྱེད་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡིན་གྱི། སེམས་ཁ་ཕྱིར་བལྟས་པའི་བྱ་བའི་དུས་ན་དེ་མེད་པའི་ཕྱིར་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 4350]
དེས་ཀུན་ནས་སློང་བའི༌[^2618]གཟུགས་ཀྱང་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་པར་འགྱུར་རོ། །

[Block 4351]
ཅིར་འགྱུར། ཆོས་མངོན་པ་ལ་གནོད་པར་འགྱུར་རོ། །

[Block 4352]
གཟུགས་ནི་རིག་པ་དང་མ་རིག་པ་དག་དང་མི་འགལ་བའི་ཕྱིར༌[^2619]མཐོང་བས་སྤང་བར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 4353]
ཕྱོགས་འདི་ནི་བསྒྲུབ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 4354]
འོ་ན་ནི་སེམས་དང༌[^2620]མཚུངས་པས་བསླང་བའི་ཕྱིར་འབྱུང་བ་རྣམས་ཀྱང་མཐོང་བས་སྤང་བར་བྱ་བར་འགྱུར་རོ། །

[Block 4355]
དེ་ལྟར་ནི་མི་འགྱུར་ཏེ། ཇི་ལྟར་དགེ་བ་དང་མི་དགེ་བ་དག་ཏུ་མི་འགྱུར་བ་བཞིན་ནོ། །

[Block 4356]
ཡང་ན་འགྱུར༌[^2621]དུ་ཟད་མོད། དེ་སྐད་བརྗོད་པ༌[^2622]ནི་མི་ནུས་ཏེ། ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་ཆོས་ནི་རིག་པ་དང་མ་རིག་པ་དག་དང་མི་འགལ་བའི་ཕྱིར་མཐོང་བས་སྤང་བར་བྱ་བ་ཡང་མ་ཡིན་ལ་སྤང་བར་བྱ་བ་མ་ཡིན་པ༌[^2623]ཡང་མ་ཡིན་ནོ། །

[Block 4357]
དེ་ལྟ་བས་ན་མདོ་ལས་རྒྱུའི་ཀུན་ནས་སློང་བའི་དབང་དུ་མཛད་ནས་གསུངས་པའི་ཕྱིར་མི་འགལ་ལོ། །

[Block 4358]
ཡིད་ནི། བསྒོམ་པས་སྤང་བྱ་གཉི་ག་ཡིན། །ཡིད་ཀྱི༌[^2624]རྣམ་པར་ཤེས་པ་བསྒོམ་པས༌[^2625]སྤང་བར་བྱ་བ་ནི་གཉི་ག་ཡིན་ཏེ། རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡང་ཡིན་ལ་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཡང་ཡིན་ནོ། །

[Block 4359]
ལྔ་ནི་རྗེས་སུ་འཇུག་བྱེད་ཡིན། །རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་ནི་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 4360]
དེ་ལྟ་བས་ན་འདི་ནི་མུ་བཞིར་འགྱུར་ཏེ། མཐོང་བས་སྤང་བར་བྱ་བའི་སེམས་ནི་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 4361]
རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་ནི་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 4362]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ༌[^2626]བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི་གཉི་ག་ཡིན་ནོ། །

[Block 4363]
ཟག་པ་མེད་པ་ནི་གཉི་ག་མ་ཡིན་ནོ། །

[Block 4364]
ཡང་ཅི་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཇི་ལྟ༌[^2627]བར་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཡང་དེ་དང་འདྲ་འམ༌[^2628]ཞེ་ན། འདི་ནི་ངེས་པ་མེད་དེ།

[Block 4365 [VERSE]]
རབ་ཏུ་འཇུག་བྱེད་དགེ་སོགས་ལས། །
རྗེས་འཇུག་བྱེད་ཀྱང་རྣམ་གསུམ་འགྱུར། །

[Block 4366]
རབ་ཏུ་འཇུག་པར་བྱེད་པ་དགེ་བ་ལས་ཀྱང་རྗེས་སུ་འཇུག་པར་བྱེད་པ་དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པར་འགྱུར་ལ། མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་ལ་ཡང་དེ་དང་འདྲའོ། །

[Block 4367]
ཐུབ་པའི་འདྲ་བའམ། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2629]ནི་རབ་ཏུ་འཇུག་པར་བྱེད་པ་དང་རྗེས་སུ་འཇུག་པར་བྱེད་པ་འདྲ་སྟེ། དགེ་བ་ལས་ཀྱང་དགེ་བ་ཡིན་ལ་ལུང་དུ་མ་བསྟན་པ་ལས་ཀྱང་ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 4368]
དེ་དགེ་བ། ཡང་ན་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ལུང་དུ་མ་བསྟན་པ་ལས་ཀྱང་རྗེས་སུ་འཇུག་པར་བྱེད་པ་དགེ་བར་འགྱུར་གྱི། རབ་ཏུ་འཇུག་པར་བྱེད་པ་དགེ་བ་ལས་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ལུང་དུ་མ་བསྟན་པར་ནི་ནམ་ཡང་མི་འགྱུར་ཏེ། སངས་རྒྱས་རྣམས་ཀྱི་སྟོབས༌[^2630]ནི་དམན་པར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 4369]
སྡེ་པ་གཞན་དག་ན་རེ་སངས་རྒྱས་རྣམས་ལ་ལུང་དུ་མ་བསྟན་པའི་སེམས་མེད་དེ། སངས་རྒྱས་རྣམས་ཀྱི་རྒྱུད་ནི་རྟག་ཏུ་མཉམ་པར་གཞག་པའི་ཕྱིར་དགེ་བར་རྒྱུད་གཅིག་པ་ནི༌[^2631]ཡིན་ནོ། །

[Block 4370]
མདོ་ལས་ཀྱང་།

[Block 4371 [VERSE]]
གླང་ཆེན་གཤེགས་ནའང་མཉམ་པར་གཞག །
གླང་ཆེན་བཞེངས༌[^2632]ནའང་མཉམ་པར་གཞག །
གླང་ཆེན་མནལ༌[^2633]ནའང་མཉམ་པར་གཞག །
བཞུགས་ནའང་མཉམ་པར་གཞག་པ་ཡིན། །

[Block 4372]
ཞེས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 4373]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་འདིའི་ཐུགས་མི་བཞེད་བཞིན་དུ་མི་འགྲོ་བའི་ཕྱིར་དེ་སྐད་གསུངས་ཀྱི་སངས་རྒྱས་རྣམས་ལ་ལུང་དུ་མ་བསྟན་པ་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དང་། སྤྱོད་ལམ་པ་དང་། སྤྲུལ་པའི་སེམས་ཀྱིས༌[^2634]མི་མངའ་བ་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 4374]
བསྒོམ་པས་སྤང་བར་བྱ་བའི་ཡིད་ནི་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡང་ཡིན་ལ་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཡང་ཡིན་ནོ་ཞེས་བཤད་པ་དེ་ཐམས་ཅད་ནི་དགེ་བ་དང་མི་དགེ་བ༌[^2635]དང་ལུང་དུ་མ་བསྟན་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 4375]
རྣམ་སྨིན་ལས་སྐྱེས་གཉི་ག་མིན། །རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པའི་སེམས་ནི་མངོན་པར་འདུ་བྱ་བ་མེད་པར་འཇུག་པ་ཉིད་ཀྱི་ཕྱིར་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡང་མ་ཡིན་ལ་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཡང་མ༌[^2636]ཡིན་ནོ། །

[Block 4376]
ད་ནི་ཅི་རབ་ཏུ་འཇུག་པར་བྱེད་པ༌[^2637]ཇི་ལྟ་བར་རྣམ་པར་རིག་བྱེད་ཀྱང་དེ་དང་འདྲ་འམ། འོན་ཏེ་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཇི་ལྟ་བ་བཞིན་དུ༌[^2638]ཡིན། དེ་ལས་ཅིར་འགྱུར། གལ་ཏེ་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཇི་ལྟ་བ་བཞིན་ཡིན༌[^2639]ནོ་ཞེ་ན་ནི་འཇིག་ཚོགས་དང་། མཐར་འཛིན་པར་ལྟ་བས་རབ་ཏུ་འཇུག་པའི་ཕྱིར་འདི་ནི་ཡང་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་རྣམ་པར་རིག་བྱེད་ཡོད་པར་འགྱུར་རོ། །

[Block 4377]
ཡང་ན་མཐོང་བས་སྤང་བར་བྱ་བ་ཐམས་ཅད་ནི་རབ་ཏུ་འཇུག་པར་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་ཁྱད་པར་དུ༌[^2640]བརྗོད་དགོས་སོ། །

[Block 4378]
གལ་ཏེ་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཇི་ལྟ་བ་བཞིན་ནོ་ཞེ་ན་ནི་སེམས་མི་དགེ་བ་ལུང་དུ་མ་བསྟན་པ་ཅན་གྱི་སོ་སོར་ཐར་པའི་རྣམ་པར་རིག་བྱེད་དགེ་བར་མི་འགྱུར་རོ། །

[Block 4379]
རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཇི་ལྟ་བར་རྣམ་པར་རིག་བྱེད་ཀྱང་དེ་དང་འདྲ་མོད་ཀྱི་བསྒོམ་པས་སྤང་བར་བྱ་བས་བར་དུ་གཅོད་པའི་ཕྱིར་མཐོང་བས་སྤང་བར་བྱ་བ་ཇི་ལྟ་བ་བཞིན་ནི་མ་ཡིན་ནོ། །

[Block 4380]
གལ་ཏེ་རྗེས་སུ་འཇུག་པར་བྱེད་པའི་དབང་གིས་དགེ་བ་ལ་སོགས་པ་ཉིད་མ་ཡིན་ན། འོ་ན་ནི་མདོ་ལས་རྒྱུའི་ཀུན་ནས་སློང་བ་ལས་དགོངས་ཏེ་གསུངས་ཀྱི་དེའི་དུས་ཀྱི་ཀུན་ནས་སློང་བ་ལས་ནི་མ་ཡིན་པས་དེའི་ཕྱིར་འདི་ནི་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་རྣམ་པར་རིག་བྱེད་མེད་དོ་ཞེས་བྱ་བ་འདི་བརྗོད་པར་མི་བྱའི་འདི་སྐད་དུ་གཞན་གྱིས་ཆོད་པའི་རྒྱུའི་ཀུན་ནས་སློང་བ་ལས་དགོངས་ནས་གསུངས་སོ་ཞེས་བརྗོད་པར་བྱའོ། །
--- END BLOCKS ---
