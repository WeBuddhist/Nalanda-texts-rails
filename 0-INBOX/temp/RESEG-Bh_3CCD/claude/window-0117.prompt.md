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
[Block 4096]
དེ་ཉིད་ཀྱི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2535]ཆ་དང་ཆ་ཙམ་གྱི༌[^2536]རྣམ་པར་རྟོག་པ༌[^2537]ཡང་སྤོང་བའི་ཕྱིར་སྟོང་པ་ཉིད་ནི་རྣམ་པ་བཅོ་བརྒྱད་དུ༌[^2538]གསུངས་ཏེ།

[Block 4097 [VERSE]]
ལྟ་བས་བྱས་པའི་སྐྱོན་ཀུན་ནི། །
སྤོང་ཕྱིར་སྟོང་པ་ཉིད་གསུངས་སོ། །

[Block 4098]
ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 4099]
གལ་ཏེ་ནུས་པ་ཐམས་ཅད་དང་བྲལ་བའི་མཚན་ཉིད་ཅན་སྟོང་པ་ཉིད་ཡིན་ན།

[Block 4100]
དེའི་ཚེ་བཅོམ་ལྡན་འདས་ཀྱིས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས།

[Block 4101]
གཟུགས་སྟོང་པ་ཉིད་དང་སྟོང་པ་ཉིད་གཟུགས་སོ་ཞེས་གསུངས་ཏེ། མེད་པར་དགག་པའི་ཕྱོགས་ནི་དོན་གྱི་བྱ་བ་བྱེད་པའི་དངོས་པོ་དང་ལྷན་ཅིག༌[^2539]ཏུ་དེའི་བདག་ཉིད་ཀྱི་འབྲེལ་པ་ཇི་ལྟར་ཡིན་ཞེ་ན། སྨྲས་པ། མེད་པར་དགག་པའི་བདག་ཉིད་ཅན་སྟོང་པ་ཉིད་ཡིན་ཏེ། གང་གི་ཕྱིར་སྟོང་པ་ཉིད་དང་དངོས་པོ་དག་ནི་དེའི་བདག་ཉིད་ཀྱིས་དངོས་པོ་ནི་སྟོང་པ་ཡིན་ནོ་ཞེས་རྟོགས་པ་དང་། སྟོང་པ་ཡང་དངོས་པོ་ཡིན་ནོ་ཞེས་རྟོགས་པས་དངོས་པོ་ནི་གུད་ན་མེད་དོ། །

[Block 4102]
གལ་ཏེ་དེ་ལྟར་ཡིན་ན། [^2540]དོན་གྱི་བྱ་བ་བྱེད་པའི་དངོས་པོ་སྟོང་པ་ཉིད་དང་འགལ་བར་གྱུར་པས་ཇི་ལྟར་རྟོགས་ཤེ་ན། སྨྲས་པ། དོན་དམ་པ་དོན་གྱི་བྱ་བ་བྱེད་པ་མ་ཡིན་ཏེ། འཁྲུལ་པས་དེ་ལྟར་སྣང་བའི་ཕྱིར་རོ། །

[Block 4103]
དཔེར་ན་མྱ་ངམ་གྱི་སའི་བྱེ་མ་ཉི་མའི་འོད་ཟེར་གྱི༌[^2541]ཚོགས་དང་ཕྲད་པས་ཆུ་ལྟར་སྣང་བའི་རི་བོའི་རྩེ་ནས་ཤིན་དུ་དགའ་བས་འོངས་པའི་རི་དགས་རྣམས་ཀྱི་སྐོམ་པ་སེལ་བར་མི་བྱེད་ཀྱི་འོན་ཀྱང་རྨོས་པ༌[^2542]དེ་རྣམས་རྣམ་པར་སླུ་བར་བྱེད་དོ། །

[Block 4104]
དེ་བཞིན་དུ་དངོས་པོ་འདི་རྣམས་ཀྱིས་དངོས་པོ་ལས་མངོན་པར་ཞེན་པ་འཁྲུལ་པ་མེད་པའི༌[^2543]སེམས་ཀྱི་རྒྱུ་དང་ལྡན་པ་ཐོག༌[^2544]མ་མེད་པའི་མ་རིག་པའི་བག་ཆགས་ཀྱིས་ཡེ་ཤེས་ཀྱི་མིག་བཙུམས་པ་རྣམས་ཀྱིས་དོན་གྱི་བྱ་བ་མི་བྱེད་དོ། །

[Block 4105]
དེ་རྣམས་ཀྱི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་དེ་ཁོ་ན་ཉིད་མངོན་དུ་བྱེད་པའི་མཚན་ཉིད་ཅན་གྱི་དོན་གྱི་བྱ་བ་གང་ཡིན་པ་དེ་ནི་རྣལ་འབྱོར་པ་རྣམས་ཀྱིས་རྟོགས་པར་བྱ་བ་ཡིན་གྱི་བག་ཆགས་རགས་པས་བློའི་མེ་ལོང་བསྒྲིབས་པ་བདག་ཅག་ལྟ་བུ་ལ་མི་སྣང་སྟེ། མི་ཤེས་པའི་དྲི་མ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 4106]
ཇི་སྐད་དུ།

[Block 4107 [VERSE]]
སོས་ཀའི་དུས་སུ་སྨིག་རྒྱུ་ནི། །
ཇི་ལྟར་སེམས་འཁྲུལ་གཡོ་བ་སྟེ། །
རི་དགས་རྣམས་ཀྱིས་ཆུར་འཛིན་པ། །
དེ་ལ་ཆུ་ངོམས༌[^2545]ཡོད་པ་མིན། །

[Block 4108]
ཞེས་འབྱུང་ངོ་། །

[Block 4109]
དེ་བཞིན་དུ་ཡང་།

[Block 4110 [VERSE]]
ཕྲ་བར་གཟིགས་པའི་སངས་རྒྱས་ཀྱིས། །
ཕྲ་ཕྱིར་དེ་ནི་རང་རིག་ཡིན། །
རང་གནས་ཀྱང་ནི་བདག་འདྲ་བས། །
བློ་རགས་ཕྱིར་ནི་མ་མཐོང་ངོ་། །

[Block 4111 [VERSE]]
རྣལ་འབྱོར་རིག་པར༌[^2546]ནམ་ཡང་ནི། །
ཐར་པའི་འདུ་ཤེས་རིང་མི་བྱ། །
བརྟགས་པའི་ངང་ཚུལ་རང་བདག་ཉིད། །
སྟོང་པར་མཐོང་ན་ཐར་པ་ཡིན། །

[Block 4112]
ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 4113]
དེ་བས་ན་དེའི་བདག་ཉིད་ཀྱི་དགག་པས་དངོས་པོ་རྣམས་སྟོང་པ་ཉིད་ཡིན་ནོ། །

[Block 4114]
དེ་ཡང་མེད་པར་དགག་པའི་བདག་ཉིད་ཡིན་པས་སྟོང་པ་ཉིད་ལ་མངོན་པར་ཞེན་པ་མེད་དོ། །

[Block 4115]
དེས་ནི་སྟོང་པ་ཉིད་ཅེས་བྱ་བ་རྣམ་པར་ཐར་པའི་སྒོ་དང་པོ་བསྟན་ཏོ། །

[Block 4116]
མཚན་མ་བཟློག་པར་བྱ་བའི་ཕྱིར་ཞེས་པ་ནི། རྣམ་པར་ཐར་པའི་སྒོ་གཉིས་པ་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 4117]
གང༌[^2547]ཡང་རྒྱུ་དང་འབྲས་བུ་ཞེས་པ་ནི་རྒྱུ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡན་ལག་བཅུ་གཉིས་ཀྱི་མཚན་ཉིད་ཉོན་མོངས་པ་དང་ལས་དང་སྐྱེ་བ་ཞེས་བྱའོ། །

[Block 4118]
འབྲས་བུ་ནི་སེམས་ཅན་གྱི་ཁམས་རིགས་བཞིའི་དབྱེ་བས་ཕྱེ་བར་གྱུར་པ༌[^2548]མཐོ་རིས་དང་ངན་སོང་ཞེས་གྲགས་པ༌[^2549]འགྲོ་བ་དྲུག་གོ། །

[Block 4119]
དེ་རྣམས་ཀྱི་རྣམ་པ་ནི་སོ་སོར་སྣང་བའོ། །

[Block 4120]
མངོན་པར་ཞེན་པ་ནི་རྒྱུ་འདི་དག་དང་འབྲས་བུ་འདི་དག་ཅེས་རྟོག་པ༌[^2550]དང་ཐ་སྙད་དོ། །

[Block 4121]
དེ་ཉིད་ཀྱང་རིགས་པ་མ་ཡིན་ཏེ་ཞེས་པ་ནི་རིགས་པས་མི་འགྲུབ་པོ། །རྒྱུ་དང་འབྲས་བུ་གཉིས་སུ་མེད་པའི་ཕྱིར་ནི་བྱ་བ་དང་བྱེད་པ་དག་གཉིས་སུ་མེད་པ་སྟེ་རྒྱུ་ནི་རང་བཞིན་གྱིས༌[^2551]ངོ་བོ་མེད་པ་དང་། འབྲས་བུ་ཡང་རང་བཞིན་གྱིས་ངོ་བོ་མེད་པའོ། །

[Block 4122]
ཇི་སྐད་དུ། སྒྱུ་མ་རྨི་ལམ་སྨིག་རྒྱུ་ཆུ་ཟླ་དང་མཚུངས་སྲིད་པ་འདི་དག་གསུམ། །ཡོད་པ་མ་ཡིན་འགག་ཕྱིར་སྐྱེ་ཕྱིར་གཞན་མིན་གཉིས་མིན་མིན། །སྐྱེ་དང་གནས་དང་འཇིག་པ་དང་བྲལ་དངོས་པོ་དེ་རྣམས་དེ་བས་ན། །གཞི་མེད་བློ་ཅན་ལ་ནི་འཁོར་དང་ཐར་པའི་དབྱེ་བ་མེད། །ཅེས་འབྱུང་ངོ་། །

[Block 4123 [VERSE]]
གང་ཞིག་རྒྱུ་མེད་མི་འབྱུང་བ། །
རྐྱེན་མེད་པས་ནི་གནས་པ་མེད། །
རྐྱེན་དང་བྲལ་བས་གང་བྲལ་བ། །
དེ་ཡོད་ཅེས་ནི་ཇི་ལྟར་རྟོགས། །

[Block 4124 [VERSE]]
རྒྱུ་ཟད་པས་ནི་གང་ཟད་པ། །
ཟད་པ་ཞེས་བྱ་ཉེ་བར་བསྟན། །
གང་ཞིག་ངོ་བོར་མ་ཟད་པ། །
དེ་ནི་ཟད་ཅེས་ཇི་ལྟར་བརྗོད། །

[Block 4125 [VERSE]]
དེ་ནི་གང་གིས་ཡོངས་ཤེས་ཏེ། །
རྟེན་འབྲེལ་འབྱུང་བ་ཐོབ་པས་ན། །
རྟེན་ནམ༌[^2552]སྐྱེས་པ་མ་སྐྱེས་པ། །
དེ་ཉིད་རིག་པ་མཆོག་གིས་གསུངས། །

[Block 4126 [VERSE]]
དེ་ལྟར་གང་ཡང་མི་བསྐྱེད་ཅིང་། །
ཅུང་ཟད་འགག་པར་མི་འགྱུར་ཏེ། །
སྐྱེ་བ་དང་ནི་འཇིག་པའི་ལམ། །
དགོངས་པའི་དོན་དུ་ཉེ་བར་བསྟན། །

[Block 4127 [VERSE]]
སྐྱེ་བ་སྐྱེས༌[^2553]པས་འཇིག་ཤེས་ཏེ། །
འཇིག་ཤེས་པས་ནི་མི་རྟག་ཤེས། །
མི་རྟག་པ་ལ་འཇུག་ཤེས་པས། །
དམ་པའི་ཆོས་ནི་འབྱུང་བར་འགྱུར། །

[Block 4128]
ཞེས་འབྱུང་ངོ་། །དེ་བཞིན་དུ།

[Block 4129 [VERSE]]
བདེན་པ་གཅིག་ནི་གྲུབ་པར་མ་གཟིགས་པས། །
བྱང་ཆུབ་ཐོབ་པས་བཞི་ནི་ག་ལ་གཟིགས། །

[Block 4130]
ཞེས་འབྱུང་ངོ་། །

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
--- END BLOCKS ---
