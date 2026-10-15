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
[Block 281]
ཡང་དག་པར་སྡུག་བསྔལ་བ་ཞེས་བྱ་བ་ནི། ཚོར་བ་རྣམ་པ་གསུམ་པོ་དག་གིས༌[^163]སྡུག་བསྔལ་ལོ། །

[Block 282]
དེ་ལས་གཞན་པ་ལྷག་མ་རྣམས་ནི་གནོད་པ་མེད་པའི་བདེ་བ་ཞེས་བྱ་བ་ལ། མངོན་པར་འབྱུང་བའི་བདེ་བ་དང་། རབ་ཏུ་དབེན་པའི་བདེ་བ་དང་།

[Block 283 [VERSE]]
ཉེ་བར་ཞི་བའི་བདེ་བའོ། །
ཐ་མ་ཞེས་བྱ་བ་ནི།
རྫོགས་པར་བྱང་ཆུབ་པའི་བདེ་བའོ། །

[Block 284]
མངོན་པར་འབྱུང་བའི་བདེ་བ་ནི་དེ་དང་རྗེས་སུ་མཐུན་པ་ཉིད་ཡིན། རབ་ཏུ་དབེན་པའི་བདེ་བ་ནི་དེའི་ཕྱོགས་པ་ཉིད་ཡིན། ཉེ་བར་ཞི་བའི་བདེ་བ་ནི་དེ་འདྲེན་པར་བྱེད་པ་ཉིད་ཡིན་གྱི། དོན་དམ་པར་ནི་མ་ཡིན་ཏེ། དོན་དམ་པའི་ནི་ཐ་མ་ཉིད་དེ། གནོད་པ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 285]
བདེ་བ་འདོད་པ༌[^164]ཡིན་པར་ཤེས་པར་བྱའོ་ཞེས་བྱ་བ་ནི། བསམ་པས་སོ། །

[Block 286]
ཕན་པའི་སྦྱིན་པ༌[^165]གང་ཡིན་པ་དེ་བདེ་བ་སྦྱིན་པ་ཡང་ཡིན་པར་ཤེས་པར་བྱ་སྟེ་ཞེས་བྱ་བ་ནི། ཕན་པའི་རྒྱུའི་གནས་ཀྱི་སྦྱོར་བ་འདི་དག་ལས་འདི་ལྟར་དེའི་རྗེས་སུ་བྱུང་བའི་འབྲས་བུ་བདེ་བའི་གནས་བྱུང་བར༌[^166]རིག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 287]
གང་ཀུན་ནས་ཉོན་མོངས་པ་ཞེས་བྱ་བ་ནི། བདག་ཉིད་ཉོན་མོངས་པ་དང་མཚུངས་པར་ལྡན་པས་ཉོན་མོངས་པ་གཞན་གྱིས་ཉོན་མོངས་པའམ། བདག་ཉིད་ཉོན་མོངས་པ་དང་ལྡན་པ་དང་། ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་ཉིད་ནི། བདེ་བ་ཡང་མི་ཕན་པ་ཞེས་བྱ་བ༌[^167]སྟེ། དོན་མ་ཡིན་པ་སྐྱེད་པར་བྱེད་པའི་དོན་ཏོ། ། གང་གི་ཕྱིར་ཞེ་ན། སྨྲས་པ། མི་ཕན་པའི་ཕྱིར་ཏེ། མི་ཕན་པའི་ཕྱིར་མ་འོངས་པའི་སྡུག་བསྔལ་གྱི་རྒྱུའོ། །

[Block 288]
དེའི་ཕྱིར་དེ་ནི་མི་ཕན་པ་ཉིད་པས་ཐམས་ཅད་ཉོན་མོངས་པ་ཅན་ནམ། ཀུན་ནས་ཉོན་མོངས་པར་འགྱུར་རོ། །

[Block 289]
དབང་པོ་དང་། ཡུལ་དང་། རེག་པས་བསྡུས་པ་ནི་བདེ་བའི་རྒྱུའོ། །

[Block 290]
ཡང་ན་གང་དབང་པོ་དང་ཡུལ་དང་རེག་པས་བསྡུས་པའི་རྒྱུ་བདེ་བ་དང་ཚོར་བ་བདེ་བ་ནི་ཀུན་ནས་ཉོན་མོངས་པར་ཡང་འགྱུར་ཏེ། ཀུན་ནས་ཉོན་མོངས་པ་དེ་ནི་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་དང་མི་འཕྲོད་པ་སྟེ། མི་ཕན་པའི་ཕྱིར་རོ། །

[Block 291]
དཀར་པོའི་ཕྱོགས་ནི་བསྟན་པ་ལས་བཟློག་པར་རིག་པར་བྱའོ། །

[Block 292]
ཅི་ནུས་ཀྱིས་ཞེས་བྱ་བ་ནི་བསྒྲུབ་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ནུས་པ་དང་མཐུན་པར༌[^168]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 293]
ཅི་ལྕོགས་པ་ཞེས་བྱ་བ་ནི། སེམས་ཅན་གང་རྣམས་ལ་ཉེ་བར་བསྒྲུབ་པ་དེ་དག་ལ་སྟོབས་ཅི་ལྟ་བ་དང་མཐུན་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 294]
དེ་བཞིན་དུ་ཡང་དག་པར་སྤྱད་པར་བྱ། བསླབ་པར་བྱ། ཉམས་སུ་མྱོང་བར་བྱ་ཞེས་བྱ་བ་ནི། ཚོར་བ་བདེ་བ་དང་། དབང་པོ་དང་། ཡུལ་དང་། རེག་པས་བསྡུས་པ་གང་ཀུན་ནས་ཉོན་མོངས་པའམ། ཉོན་མོངས་པ་ཅན་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་དང་། མི་ཕན་པ་དང་། མི་འཕྲོད་པ་ལ་མི་བསླབ་པ་ཉིད་དོ། །

[Block 295]
གང་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་དང་། ཁ་ན་མ་ཐོ་བ་མེད་པ་དང་། ཕན་པ་དང་། འཕྲོད་པའི་ཚོར་བ་བདེ་བ་ནི། ཉམས་སུ་མྱོང་བར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 296]
ཚེ་རིང་ཞིང་ཞེས་བྱ་བ་ནི། ལས་གང་གིས་ཁུ་བ་དང་ཁྲག་གི་ནང་དུ་ཡང་དག་པར་བརྒྱལ་བའི་དུས་དང་། ཁྱད་པར་དུ་འཕགས་པའི༌[^169]དུས་ནས་འདི་སྙེད་ཅིག་འཚོ་བར་འགྱུར་རོ་ཞེས་བྱ་བ་སྟེ། དེ་ནི་ཚེ་ཞེས་ཀྱང་བརྗོད་ལ། སྲོག་ཅེས་ཀྱང་བྱའོ། །

[Block 297]
གང་ལ་ཚེ་དེ་རིང་བ་ཡོད་པ་དེ་ལ་ཚེ་རིང་བ་ཞེས་བྱ་སྟེ། དེའི་དངོས་པོ་ནི་ཚེ་རིང་བ་ཉིད་དོ། །

[Block 298]
ཡུན་རིང་དུ་གནས་པ་ཇི་ལྟ་བུ་ཞེ་ན། ལས་གང་གིས་དེའི་ཚེ་འཕངས་པ་དེ་ཡང་རྣམ་པ་གཉིས་ཡིན་ཏེ། བར་ཆད་དང་བཅས་པ་དང་། བར་ཆད་མེད་པའོ། །

[Block 299]
བར་ཆད་དང་བཅས་པ་ནི་ལས་གང་གིས༌[^170]ཚེ་འཕངས་པ་དེ་རྐྱེན་གྱི་དབང་གིས་རབ་ཏུ་འཆི་བ་སྲིད་པ་སྟེ། འཆི་བ་དེ་ནི་དུས་མ་ཡིན་པར་འཆི་བ་ཞེས་བྱའོ། །

[Block 300]
བར་ཆད་མེད་པ་ནི་གང་ལས་ཀྱིས་འཕངས་པའི་ཚེ་དེ་བར་མ་དོར་མི་འཆི་བ་སྟེ། ལས་གང་གིས་འཕངས་པ་དེ་དེས་ཇི་ལྟར་འཕངས་པ་བཞིན་གནས་པ་ཉིད་དེ། ཡུན་རིང་དུ་གནས་པ་ཉིད་དོ། །

[Block 301]
གཟུགས་བཟང་ཞིང་ཞེས་བྱ་བ་ལ། འདིར་བཟང་བའི་སྒྲ་ནི་མཆོད་པའི་དོན་གྱི་ཚིག་གི་ཕྲད་དེ། དཔེར་ན་མངོན་པར་དགའོ་ཞེས་བྱ་བ༌[^171]ལྟ་བུའོ། །

[Block 302]
གང་གིས་གཟུགས་ལ་མཆོད་པ་ཡོད་པ་དེ་གཟུགས་བཟང་བ་སྟེ། དེའི་གཟུགས་ལ་མཚན་ཕུན་སུམ་ཚོགས་པ་ཡོད་པས་མཆོད་པ་ཉིད་དེ། དེའི་གཟུགས་དེ་ལ་མཆོད་པར་འགྱུར་བས། དེའི་ངོ་བོ་ཉིད་ནི་གཟུགས་བཟང་བ་ཉིད་དོ། །

[Block 303]
བལྟ་ན་སྡུག་པ་ནི་མཐོང་ན་ཕན་པ་སྟེ། མིག་དང་མཐུན་པའོ། །

[Block 304]
ཡང་ན་མཐོང་བར༌[^172]བཟོད་པ་ནི་བལྟ་ན་སྡུག་པ་སྟེ། ཡང་དང་ཡང་དུ་བལྟ་བར་འདོད་པ་ཉིད་དོ། །

[Block 305]
རབ་ཏུ་དགའ་བ་དང་འདྲེན་པ་ནི་མཛེས་པ་ཉིད་དེ། སེམས་དགའ་ཞིང་དྲི་མ་མེད་པའོ། །

[Block 306]
དེའི་དངོས་པོ་ནི་མཛེས་པ་ཉིད་དོ། །

[Block 307]
ལོངས་སྤྱོད་ཆེ་བ་ཞེས་བྱ་བ་ལ། སྤྱད་པར་བྱ་བས་ན་ལོངས་སྤྱོད་ལ། དེ་ཆེན་པོ་ཡང་ཡིན་པས་ལོངས་སྤྱོད་ཆེན་པོའོ། །

[Block 308]
དེའི་དངོས་པོ་ནི་ལོངས་སྤྱོད་ཆེ་བ་ཉིད་དེ། སྣ་ཚོགས་ཀྱི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 309]
རྩ་འཇིང་ཆེ་བ་ཞེས་བྱ་བ་ནི། བཤེས་ཀྱི་ཕྱོགས་མང་ཞིང་ཆེ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 310]
འཁོར་ཕལ༌[^173]ཆེ་བ་ཡིན༌[^174]ཞེས་བྱ་བ་ནི། བུ་དང་ཆུང་མ་དང་བྲན་ཕོ་དང་བྲན་མོ་དང་། ལས་བྱེད་པ་ལ་སོགས་པའི་འཁོར་རོ། །

[Block 311]
ཡིད་བརྟན་དུ་རུང་ཞིང་ཡིད་ཆེས་པ་ཡིན་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་ཡིད་བརྟན་དུ་རུང་བ་ཡིན་ཞེ་ན། སྨྲས་པ། སེམས་ཅན་རྣམས་ཀྱི་རྩོད་པ་འབྱུང་ངོ་། །མཆོག༌[^175]ཏུ་ཚད་མར་གཞག་པར་འོས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 312]
ཡིད་ཆེས་པ་ཡིན༌[^176]ཞེས་བྱ་བ་ཇི་ལྟར༌[^177]ཞེ་ན། སྨྲས་པ། གཞལ་བླུགས༌[^178]ལ་གཡོ་བྱེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། གཞལ་བླུགས༌[^179]ལ་ཞེས་བྱ་བ་ནི་སྲང་ལའོ། །

[Block 313]
འཇལ་བ་ལ༌[^180]ཞེས་བྱ་བ་ནི། བྲེ་ཕུལ་ལ་སོགས་པ་སྟེ། སྲང་དང་བྲེ་ལ་སོགས་པའི་ཕྱི་རོལ་གྱི་ཉེ་བར་སྤྱད་པ་རྣམས་ཀྱིས་བསླུ་བའོ། །

[Block 314]
གཡོ་དང་སྒྱུ་ནི་ནང་གི་བདག་ཉིད་ཅན་ཏེ། དེ་དག་གིས་སླུ་བ༌[^181]མེད་པའོ། །

[Block 315]
ནོར་གཏམས་པ་ལ་དོར་མི་བྱེད་པ་ནི། ནོར་གཏམས་པ་ལ་མི་བསྙོན་པ་སྟེ། དེ་ལྟ་བུ་ནི་ཡིད་ཆེས་པའོ། །

[Block 316]
གཞི་དེས་ཞེས་བྱ་བ་ནི། ཡིད་བརྟན་དུ་རུང་བ་ཉིད་དང་། ཡིད་ཆེས་པ་ཉིད་ཀྱི་གཞི་དེས་ཚིག་གཟུང་བར་འོས་པར་འགྱུར་རོ། །

[Block 317]
གྲགས་པ་ཆེན་པོ་ནི་གྲགས་པར་འགྱུར་བ་སྟེ། ཅི་ལྟ་བུ་ཞེ་ན།

[Block 318 [VERSE]]
དཔའ་བ་ལ་སོགས་པ་དྲུག་གོ། །
སྙན་པ་ཇི་ལྟ་བུ་ཞེ་ན།
འཇིག་རྟེན་འདིར་གྲགས་པར་འགྱུར་བའོ། །

[Block 319]
ཇི་ལྟ་བུ་ཞེ་ན། བཟོ་དང་ལས་ཀྱི་གནས་རྣམ་པ་སྣ་ཚོགས་ལྷག་པར་རབ་དང་ཕུལ་དང༌[^182]ཞེས་བྱ་བ་ནས་བརྩམས་པའོ། །

[Block 320]
གཞི་དེས་བྱ་བ་ནི་གྲགས་པ་ཆེན་པོ་དང་སྙན་པས་འཇིག་རྟེན་དུ་ཤེས་པ་ཉིད་ཀྱི་གཞིའོ། །
--- END BLOCKS ---
