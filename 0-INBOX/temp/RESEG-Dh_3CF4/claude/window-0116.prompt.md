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
ཤུགས་འབྱིན་སྨོད་པར་འགྱུར་ལགས་སམ། །ཞེས་བྱ་བ་ནི་དེའི༌[^2623]ཡོན་ཏན་ཐོས་ན་མཁས་པའི་ཕྱིར་རོ། །

[Block 4062]
[^2624]མི་བཟོད་པ་ཡིན་པས། ཤུགས་འབྱིན་པ་ཡིན་ཏེ༌[^2625]སྨོད་པར་འགྱུར་རོ། །ཞེས་སྟོན་ཏོ། །

[Block 4063]
དི་རིང་བདག་ཀྱང་བདེ་ཞེས་བྱ་བ་ནི་ཅིའི་ཕྱིར་ཞེ་ན། ཕྲད་པས་ཡུན་རིང་པོར་བསམས་པ་འབྱོར་ཅིང་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 4064]
ཐམས་ཅད་དུ་ཡང་བདེ་ཞེས་བྱ་བ་ཡང་དེ་དང་ཕྲད་པས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 4065]
ངང་པ་དེ་རིང་བདག་ཀྱང་བདེ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་སྔར་བཤད་པའི་དྲི་བ་མཐའ་དག་གི་ལན་ཡིན་ནོ། །

[Block 4066]
ཁྱོད་ནི་རྙི་ཡིས་ཟིན་པ་ན། །ཞེས་བྱ་བ་དང་། དེ་ལྟར་རྔོན་པ་འདི་དག་ནི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ནི་དགའ་བར་གྱུར་པའི་གཏམ་ལས་བརྩམས་པའོ། །

[Block 4067]
འདི་ཡིས་སྣད་པར་མ་བྱས་སམ། །ཞེས་བྱ་བ་སྨོས་པ་ལ། སྣད་པར་བྱེད་པའི་རྒྱུ་དེ་ཉིད་ཀྱིས༌[^2626]སྒྲུབ་པའི་ཕྱིར་སྨྲས་པ། ཁྱོད་ནི་རྙི་ཡིས་ཟིན་པ་ཡི། །[^2627]ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་ཕྱེ་སྟེ། དགའ་བས་སེམས་གཡེངས་པར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4068]
དགའ་བས་སེམས་གཡེངས་པ་ཉིད་ཀྱི་རྒྱུ་ཡང་བསྟན་པའི་ཕྱིར། དེ་ལྟར་རྔོན་པ་འདི་དག་གིས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་ཕྱེད་དོ། །

[Block 4069]
བྱ་རྣམས་ཟིན་ཅིང་སྣང་གྱུར་ན། །ཞེས་བྱ་བ་ནི་བྱ་རྣམས་དབང་དུ་གྱུར་ཅིང་ཐོབ་ན་གནོད་པ་ཉིད་དུ་དགའ་བ་ཡིན་ནོ། །

[Block 4070]
དགའ་བས་སེམས་ནི་གཡེངས་གྱུར་ནས། །ཞེས་བྱ་བ་ནི་དགའ་བ་བསྙེམས་པས༌[^2628]དེ་ལ་ངན་པ་དག་ཀྱང་སྤྱོད་པར་འགྱུར་ཏེ། བསྙེམས་པའི༌[^2629]དབང་གིས་སོ། །

[Block 4071]
འདི་ལྟ་བུར་ནི་ཉམས་ཉེས༌[^2630]ཀྱང་། །ཞེས་བྱ་བ་ནི་རྙིའི་དབང་དུ་གྱུར་ཀྱང་ངོ་། །དགྲ་བཞིན་དུ་ནི་གནོད་པ་མ་བགྱིས་སོ། །ཞེས་བྱ་བ་ནི་དབྱིག་པ་ལ་སོགས་པས་མ་བརྡེགས་པས་སོ། །

[Block 4072]
འོ་སྐོལ་གཉིས་ཀ་དགྱེས་བགྱིས་པས། །ཞེས་བྱ་བ་ནི་སྔར་ངང་པའི་རྒྱལ་པོ་བཏང་བས་བཞིན་བཟངས་ངང་པའི་རྒྱལ་པོ་ཁྱེད༌[^2631]ཀྱང་དགའ་བར་བྱས་ལ། འདིར་ཁྱེར་ཏེ་འོངས་པས་བདག་ཅག་ཀྱང་དགའ་བར་བྱས་ཏེ། དེས་ན་བདག་ངང་པའི་རྒྱལ་པོ་བཞིན་བཟངས་ཀྱང་དགའ་བར་བྱས་པ་སྟེ། དེ་ལྟར་གཉི་ག་དགའ་བར་བྱས་པ་གང་ཡིན་པའོ། །

[Block 4073]
མང་བ༌[^2632]ནི་སྤངས༌[^2633]པའོ། །

[Block 4074]
ནོར་རྒྱ་ཆེར་བྱིན་ཏེ་ཞེས་བྱ་བ་ནི་རེ་རེའི་རྣམ་པ་ཡང་མང་པོ་ཡིན་པར་སྟོན་ཏོ། །

[Block 4075]
ཅི་བཞེད་དེ་དག་ཅེས་བྱ་བ་ནི་དངོས་སུ་སྨོས་པ་བཟུང་སྟེ། ནོར་དེའི་དམིགས་ཀྱིས་དབྱེ་བའི་ཚུལ་མེད་པར་རོ། །

[Block 4076]
ཅི་དང་ཞེས་བྱ་བ་ནི་དེ་དང་འཚམ་པའི༌[^2634]ཐབས་སྟོན་པ་ཡིན་ནོ། །

[Block 4077]
དེ་ཞེས་བྱ་བ་ནི་ལོངས་སྤྱོད་བདོག་པའོ། །

[Block 4078]
དེ་བས་ན་མཛའ་བོའི་ཕན་ཡོན་ཆེ་བའི་སྤོབས་པ་གང་ཡིན་པ་དེ་ནི་སྤོབས་པ་ཕན་ཡོན་ཆེ་བའོ། །

[Block 4079]
བཞིན་བཟངས་སྨྲར་གཞུག་པར་འདོད་པ་གང་ཡིན་པ་དེ་ནི་བཞིན་བཟངས་སྨྲར་གཞུག་པར་འདོད་པའོ། །

[Block 4080]
གསར་དུ་བཤེས་པ་གང་ཡིན་པ་དེ་ནི་གསར་དུ་བཤེས་པའོ། །སུ་དང་གསར་དུ་བཤེས་ཤེ་ན། སྐྱེ་བོ་མ་འདྲིས་པས་ཞེས་བྱ་བ་ཡིན་ཏེ། མ་འདྲིས་པ་དེ་ལ་རབ་ཏུ་སྤོབས་ཤིང་སྨྲ་བ་དང་བག་དབབ་པ་ནི་མི་རུང་བ་ཡིན་པས་སོ། །

[Block 4081]
བཀའ་མཆིད་ཉིད་གསུང་ཡིན་པས་བཀའ་མཆིད་གསུང་བའོ། །

[Block 4082]
ཚུལ༌[^2635]ནི་དེ་མ་ལགས་ཞེས་བྱ་བ་ནི་བཀའ་མཆིད་དེ་ལྟ་བུའི་ནང་དུ་འཇུག་ཅིང་སྤྱི་བརྟོལ༌[^2636]བསྐྱེད་པའི་ཚུལ་དང་། ལམ་མ་ཡིན་ཏེ། ཚུལ་མ་ཡིན་པའི་ལམ་དེས་སོ། །

[Block 4083]
བཟོད་པར་གསོལ་བ་ནི་མི་སྨྲ་བར་འདུག་པ་དེ་ལའོ། །

[Block 4084]
ཁྱོད་ཀྱི་ཡོན་ཏན་གཏམ་སྙན་མི་རྣམས་ཟེར་བའི་རིགས། །ཞེས་བྱ་བ་ལ། ཅིའི་ཕྱིར་རིགས་ཤེ་ན། སྨྲས་པ། འདི་ལྟ་བུར་ཁྱོད་དུལ་བའི་ཕྱིར་རོ། །

[Block 4085]
ངང་པའི་བདག་པོ་དང་ཡང་གྲོགས་པོར་འཐམས་པའི་རིགས་ཏེ། གྲོགས་པོར་འཐམས་པ་ཅིའི་ཕྱིར་རིགས་ཤེ་ན། འདི་ལྟ་བུར་ཁྱོད་དུལ་བ་དང་ཚུལ་མཁས་པས་སོ། །

[Block 4086]
རབ་ཏུ་མཛའ་བར་འདོད་པ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་གཅུགས༌[^2637]པར་འདོད་པ་ཞེས་བྱ་བའི་དོན་ཏེ། །ཇི་ལྟར་དེ་བས་བདག་ཅག་མཛའ་བ་འདི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་བསྟན་པ་དེ་བཞིན་དུ་གཟུང་ངོ་། །བྱམས་པའི་འཇུག་པ་ནི་བྱམས་པར་འགྱུར་བའོ།[^2638] །ཇི་ལྟར་བྱམས་པར་གྱུར་པ་ཡིན་ཞེ་ན། ཇི་སྐད་དུ་སྔར་བཤད་པའི། ཁྱེད༌[^2639]གཉིས་ཁྱེད་དུ་བདག་གི་ཁྱིམ་དུ་བྱོན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་བསྟན་ཏོ། །

[Block 4087]
དང་པོ་བཤེས་པར་གྱུར་པ་ནའང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་ནི་བྱམས་པར་གྱུར༌[^2640]བར་ཤེས་ནས་དེ་ལ་མགུ་བར་བྱེད་པ་དེ་བསྟན་ཏོ། །

[Block 4088]
རབ་ཏུ་མཛའ་བར་འདོད་པ་ཞེས་བྱ་བ་དེ་སྒྲུབ་པའི་ཕྱིར། བཀུར་སྟི་བྱ་བའི་ཆོ་ག་འདིས། །ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 4089]
ཅི་དང་ཅི་བཞེད་དེ་དག་བདག་ལ་གསུངས། །ཞེས་བྱ་བ་དེའི་ལན་ནི། བདག་ཉིད་དོན་དུ་མི་གཉེར་བར་བསྟན་པའི་ཕྱིར། དགོས་པ་ལྟ་ཞིག་ཆེད་ཆེ་ཅི་ཞིག་མཆིས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 4090]
ཆེད་ཆེ་མཆིས་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱི་སྲོག་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་རོ། །

[Block 4091]
ཅི་ཞིག་མཆིས་ཞེས་བྱ་བ་ནི་གཞན་གང་དོན་དུ་མི་གཉེར་བར་འདོད་པའོ། །

[Block 4092]
ཁྱོད་ལ་བདག་བརྟེན་པ་གང་ཡིན་པ་དེ་ལྟ་ཡིན་པས་སོ། །

[Block 4093]
ཅི་དང་ཅི་བཞེད་དེ་དག་བདག་ལ་གསུངས། །ཞེས་བྱ་བ་ཡང་གོམས་པའི་ཡོན་ཏན་ཡིན་ཏེ། གཞན་དག་ཏུ་མགྲོན་དག་ལ་སྤྱད་པ་ཉིད་ཡིན་པའི་ཕྱིར། མགྲོན་ལ་དགའ་བའི་ཕྱིར་ཞེས་བྱ་བ་བདག་ལ་འདི་ལྟར་གྱུར་པའོ། །

[Block 4094]
ཡོན་ཏན་ལ་དགའ་བ་ནི་ཡོན་ཏན་འདོད་པ་སྟེ་དེ་ཡོན་ཏན་འདོད་པ་གཉིས་ཀྱི༌[^2641]ཡོན་ཏན་ལ་དགའ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4095]
གང་གི་ཕྱིར་ཡོན་ཏན་འདོད་པ་དེ་བས་ན་མགྲོན་ལ་དགའ་བ་ཡིན་ཏེ། ཡོན་ཏན་དང་མགྲོན་ལ་དགའ་བའོ། །

[Block 4096]
ཡོན་ཏན་ལ་དགའ་བ་ཉིད་བསྟན་པའི་ཕྱིར། འབངས་ལ་ཕན་ཕྱིར་ཞེས་བྱ་བའི༌[^2642]ཚིགས་བཅད་ཡིན་ཏེ། ཁྱོད་ལྟ་ལགས་ཀྱང་མོད་ཅེས་བྱ་བ་ནི་མགྲོན་ལ་དགའ་བའི་ཕྱིར་རོ། །

[Block 4097]
རང་བཞིན་དུལ་བ་ཞེས་བྱ་བ་ནི་ངང་གིས་སེམས་སྦྱངས་པ་གང་ཡིན་པ་དེ་ནི་རང་བཞིན་དུལ་བ་སྟེ། མི་བཟོད་པ་སྤངས་པས་རང་བཞིན་དུལ་བར་གྱུར་པའོ། །

[Block 4098]
གལ་ཏེ་མི་བཟོད་པ་སྤངས་སོ་ཞེས་བསྟན་ན་ཅིའི་ཕྱིར་སའི་བདག་པོ་བྱེད་པར་འགྱུར་ཞེ་ན། སྨྲས་པ། འབངས་ལ་ཕན་ཕྱིར་རྒྱལ་པོའི་ཚུལ་འཛིན་པ། །ཞེས་བྱ་བ༌[^2643]སྨོས་ཏེ། འདིས་ནི་བདག་ཉིད་ཀྱི་ཉེ་བར་ལོངས་སྤྱོད་པའི་ཕྱིར་མ་ཡིན་པར་སྟོན་ཏོ། །

[Block 4099]
རང་གི་ངང་གིས་ཞེས་བྱ་བ་ནི་འབད་པ་མེད་པར་གོམས་པ་སྟེ། དེ་ལ་ཡོན་ཏན་རྣམས་གནས་པར་སྟོན་ཏོ། །

[Block 4100]
དེ་བས་ཞེས་བྱ་བ་ནི་རྒྱུན་མི་འཆད་པའི་ཚུལ་གྱིས་ཡིན་ཏེ་དེས་ནི་བདག་ཉིད་ཀྱི་ཚུལ་བསྟན་ཏོ། །
--- END BLOCKS ---
