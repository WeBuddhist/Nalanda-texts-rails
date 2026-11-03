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
[Block 3221]
འདིར༌[^3156]ཉེ་བར་ཞི་བ་ནི་དགོས་པ་ཡིན་ཏེ། དེ་བས་ན་རང་ལ་བསྒྲུབ་པ༌[^3157]ལ་དེ༌[^3158]བྱ་བ་ཉིད་དུ་ནི་རིགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་བསྟན་ཏེ། འོ་ན་འགྱེད་པ་མང་པོ་དག་བྱུང་ན་ཅིའི་ཕྱིར༌[^3159]འགྱེད་པ་གཉིས་ཞེས་གཉིས་ཀྱི་ཚིག་ཏུ་བྱས་ཤེ་ན། བདེན་མོད་ཀྱི་དེ་ནི་ཕྱོགས་གཉིས་སུ་རྣམ་པར་གནས་པས་དེ་ལ་གཉིས་ཉིད་དུ་བྱུང་བ་ཉིད་དོ། །

[Block 3222]
ཚོགས་པར་དབྱུང་བ་ཇི་ལྟ་བུ་དག་གིས་སོ་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་དག་གིས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3223]
དགེ་སློང་ཇི་ལྟ་བུ་དག་གིས་ཤེ་ན། དེའི་ཕྱིར་འགྲང་བ༌[^3160]དག་གིས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །སུ་འགྲང་བ༌[^3161]དག་གིས་ཤེ་ན། དེའི་ཕྱིར། དེ་གཉིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ་འགྱེད་པ་དེ་གཉིས་སོ། །ཇི་སྙེད་དག་གིས་ཤེ་ན། དེའི་ཕྱིར་གཅིག་ཡན་ཆད་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ཡན་ཆད་ཀྱི་སྒྲ་བྲི་བར༌[^3162]རིག་པར་བྱ་སྟེ་གཅིག་ཡན་ཆད་དུ༌[^3163]རུང་བར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3224]
ཡང་དགེ་སློང་གཅིག་གམ་དུ་མ་ཇི་ལྟ་བུ་ལ་དེ་གཉིས་ཀྱིས་འགྲང་བར༌[^3164]བྱ་ཞེ་ན། དེའི་ཕྱིར་གཟུ་བོ་དག་ལ་བགྲང་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕྱོགས་གཉིས་ཀའི་དབུས་ན་གནས་པ་གཅིག་གམ་དུ་མ་ཕྱོགས་ཀྱི་ཁོངས་སུ་མི་བསྡུ་ཞིང་གཟུ་བོ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3225]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི་སོ་སོར་ཐར་པའི་སྐབས་ཀྱི་རྩོད་པ་ཞི་བར་བྱ་བའི་ཞུ་བའི་གཞུང་ཁ་ཅིག་ལས།

[Block 3226]
དགེ་སློང་གཟུ་བོ་གང་ཞེ་ན་ཕྱོགས་ཅིག་ཤོས་སུ་ཡང་མ༌[^3165]སོང་ལ་གཉིས་པར༌[^3166]མ་སོང་བ་གང་ཡིན་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3227]
དེ་དག་དགེ་འདུན་གྱི་གཏན་དུ་བསྒོའོ༌[^3167]ཞེས་བྱ་བ་ནི། གཟུ་བོ་དེ་དག་དགེ་འདུན་གནས་དེར་གཏན་ཏུ་དགེ་འདུན་ཐམས་ཅད་ཀྱིས་བསྐོ་བ་ནི་རྩོད་པ་བྱུང་བ་རྣམས་རྣམ་པར་ཞི་བར་བྱ་བའི་ཕྱིར་ཡིན་གྱི། རྩོད་པ་གཅིག་གི་ཕྱིར་འཕྲལ་ལ་བསྐོ་བའི་ཕྱིར་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3228]
འདིར་འཐབ་མོ་མི་བསྐྱེད་པར༌[^3168]བསྐོ་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གཟུ་བོ་བསྐོ་བ་འདིར་གང་ཞིག་འདི་ལྟ་བུ་བསྐོ་བར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 3229]
ངོ་ཚ་ཤེས་ཤིང་བསླབ་པ༌[^3169]འདོད་པའོ་ཞེས་བྱ་བ་ནི་འདིར་ངོ་ཚ་ཤེས་པ་ཞེས་བྱ་བ་བསླབ་པའི་གཞི་ཡང་དག་པར་བླངས་པ་ཐམས་ཅད་ལ་བག་རྐྱོང་བ༌[^3170]ཞུམ་པར་བྱེད་པ་ཡིན་གྱི་ཕན་པར༌[^3171]འགྱུར་བ་ཙམ་ཉི་ཚེར་མ་ཟད་དོ། །

[Block 3230]
མ་མོ་ལས་འདི་སྐད་གསུངས་ཏེ། དེ་དགེ་སློང་ཆོས་ཉི་ཤུ་རྩ་གཉིས་དང་ལྡན་པ་བཙལ༌[^3172]བར་བྱ་སྟེ། ཉི་ཤུ་རྩ་གཉིས་གང་ཞེ་ན་ཅི་ཚེ་དང་ལྡན་པ་དེ་ལ་ཚུལ་ཁྲིམས་དང་ལྡན་ཞིང་དང་པོ་ནས་ཕུན་སུམ་ཚོགས་པ་དང་ངོ་ཚ་ཤེས་ཤིང་འགྱོད་པ་དང་ལྡན༌[^3173]ལ་སྡོམ་པ༌[^3174]དང་བསླབ་པ་འདོད་པ་དང་། འདུལ་བ་ལ་ཤིན་ཏུ་རྣམ་པར་ངེས་ཤིང་ཐོས་པ་འཛིན་ལ་ཐོས་པ་བསགས་པ་དང་། ལུང་ཐོན་པ་དང་། རྩོད་པ་ལ་མཁས་པ་དང་། རྩོད་པ་ཀུན་ནས་སློང་བ་ལ་མཁས་པ་དང་། རྩོད་པའི་བྱེ་བྲག་ལ་མཁས་པ་དང་། རྩོད་པ་འགོག་པ་ལ་མཁས་པ་དང་། རྩོད་པ་འགགས༌[^3175]ནས་ཕྱིས་མི་འབྱུང་བ་ལ་མཁས་པ་དང་། བསྟན་བཅོས་ལ་མཁས་པ་དང་། གཞི༌[^3176]ལྷག་པར་སྤྱོད་པ་ལ་མཁས་ཤིང་ཉེས་རྩོམ་མེད་པར་སྨྲ་བ་དང་། ཉེས་རྩོམ་བྱེད་དུ་མི་འཇུག་པ་དང་། ལུས་དང་ངག་གིས་མི་འཇུག་པ་དང་། སྨྲ་བར་བྱེད་ཅིང་སྨྲ་བ་བརྡ་ཕྲད་པར་བྱེད་པ་དང་། གོ་བར་བྱེད་ཅིང་གོ་བ༌[^3177]བརྡ་ཕྲད་པར་བྱེད་པ་དང་། རྣམ་པར་རིག་པར་བྱེད་ཅིང་རྣམ་པར་རིག་པར་བྱ་བ་བརྡ་ཕྲད་པར་བྱེད་པ་དང་། ངེས་པར་རྟོགས་པར་བྱེད་ཅིང་ངེས་པར་བརྟགས་པ་བརྡ་ཕྲད་པར་བྱེད་པ་དང་། འདུན་པས་འགྲོ་བ་མ་ཡིན་པ་དང་། ཞེ་སྡང་གིས་འགྲོ་བ་མ་ཡིན་པ་དང་། གཏི་མུག་གིས་འགྲོ་བ་མ་ཡིན་པ་དང་། འཇིགས་པས་འགྲོ་བ་མ་ཡིན་པ་སྟེ། གཟུ་བོའི་ཆོས་ཉིད༌[^3178]ཉི་ཤུ་རྩ་གཉིས་པོ་དེ་དག་དང༌[^3179]ལྡན་པའི་ཆོས་ཀྱི་ལོངས་སྤྱོད་དམ། ཟང་ཟིང་གི་ལོངས་སྤྱོད་ཀྱི༌[^3180]ཕྱོགས་གཉིས་ཀ་ལ་མི་བརྟེན༌[^3181]པ་ཡིན་ནོ་ཞེས་གསུངས་པ་དེ་དག་འདིར་བསྡུས་པར་ཤེས་པར་བྱའོ། །

[Block 3231]
འདུལ་བ༌[^3182]ལ་ཤིན་ཏུ་རྣམ་པར་ངེས་པའོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་དང་ལྟུང་བ་མ་ཡིན་པ་ལ་མཁས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3232]
རྩོད་པའི་འབྱུང་བ་སྤྱོད་པ་ལ་མཁས་པའོ་ཞེས་བྱ་བ་ནི་རྩོད་པ༌[^3183]ལ་མཁས་པ་དང་། རྩོད་པ་ཀུན་ནས༌[^3184]སློང་བ་ལ་མཁས་པ་དང་། རྩོད་པའི་བྱེ་བྲག་ལ་མཁས་པ་དང་། རྩོད་པ་འགོག་པ་ལ་མཁས་པ་དང་། རྩོད་པ་འགགས་ནས་ཕྱིར་མི་འབྱུང་བ་ལ་མཁས་པ་ནི༌[^3185]འབྱུང་བ་སྤྱོད་པ་ལ་མཁས་པའོ། །

[Block 3233]
སྤྱོད་པ༌[^3186]ལ་མཁས་པ་ཞེས་བྱ་བ་ནི་འདི༌[^3187]རྗེས་སུ་སྒྲུབ་པ༌[^3188]དང་འདི་བྱེད་པར་འགྱུར་བ་ལ་མཁས་པ་ཞེས་བྱ་བའོ། །

[Block 3234]
ཐོབ་པའི༌[^3189]གཞི་ལ་སོགས་པ་གསུམ་པོ་རང་གི་རྣམ་པར་ངེས་པ༌[^3190]ལ་ཇི་སྲིད་དུ་རྣམ་པར་ཞེན་པའི་ཞེས་བྱ་བ་འདི་ལ་རྗེས་སུ་ཞུགས་པར་རིག་པར་བྱའོ། །

[Block 3235]
རྣམ་པར་ཞེན་པའོ་ཞེས་བྱ་བ་ནི་དོན་རྣམ་པར་ངེས་པས་མི་འགྱུར་ཏེ་དེས་ནི་བསྟན་བཅོས་ལ་མཁས་པ་བསྡུས་སོ། །

[Block 3236]
བརྟན་ཞིང་ཉེས་རྩོམ་མེད་པར་འཇུག་པའོ་ཞེས་བྱ་བ་ལ། བརྟན་པ་ནི་བརྟེན༌[^3191]པའོ། །

[Block 3237]
ལུས་དང༌[^3192]ངག་གིས་མི་འཇུག་པ༌[^3193]བསྡུས་སོ།[^3194] །ཉེས་རྩོམ་མེད་པར་འཇུག་པའོ་ཞེས་བྱ་བ་ནི་ཉེས་རྩོམ་མེད་པར༌[^3195]སྨྲ་བ་དང་ཉེས་རྩོམ་བྱེད་དུ་མི་འཇུག་པ་བསྡུས་སོ་སྙམ་པའོ༌[^3196]ཞེས་བྱ་བ་ནི། འདུན་པ་དང་ཞེ་སྡང་དང་འཇིགས་པས་མི་འགྲོ་བ་བསྟན་ཏོ། །

[Block 3238]
བརྡ་ཕྲད་པའོ་ཞེས་བྱ་བ་ནི་གཞན་གྱིས་བསྒོ་བ་བརྡ་ཕྲད་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་བརྡ་ཕྲད་པར་བྱ་བ་སྟེ་དེས་ནི་སྨྲ་བ་བརྡ་ཕྲད་པར་བྱེད་པ་དང་ཞེས་བྱ་བ་ནས་ངེས་པར་རྟོགས་པར་བྱེད་པ་ཞེས་བྱ་བའི་ཚིག་འོག་མ༌[^3197]བཞི་བསྡུས་སོ། །

[Block 3239]
བརྡ་སྤྲོད་པར་བྱེད་པའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ཕ་རོལ་པོ་ལ་བརྡ་ཕྲད་པར་བྱེད༌[^3198]ནུས་པ་དེ་ནི་མཁས་པའོ། །

[Block 3240]
བརྡ་སྤྲོད་པར་བྱེད་ནུས་པ༌[^3199]ཞེས་བྱ་བ་ལ་སོགས་པ་སྔ་མའི་ཚིག་བཞི་པོ་རྣམས་བསྡུ་བའོ། །

[Block 3241]
མཁས་པ་ཞེས་བྱ་བ་ནི་རྨོངས་པ་མེད་ཅིང་མཁས་པ་སྟེ༌[^3200]དེས་ནི་གཏི་མུག་གིས་འགྲོ་བ་མ་ཡིན་པ་ཞེས་བྱ་བ་ཡན་ཆད་ཐམས་ཅད་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 3242]
དེ་དག་གིས་ཉེ་བར་མ་ཞི་ན་དགེ་འདུན་ལ་དབུལ་ལོ་ཞེས་བྱ་བ་ནི་གཟུ་བོ་དེ་དག་གིས་རྩོད་པ་དེ༌[^3201]ཉེ་བར་མ་ཞི་ན་དགེ་འདུན་ལ་དབུལ་བར་བྱའོ། །

[Block 3243]
དེས་མ་ནུས་ན་གསལ་བ་དག་བསྐོའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་དེས་རྩོད་པ༌[^3202]ཉེ་བར་ཞི་བར་བྱེད་མ་ནུས་ན་དགེ་སློང་གསལ་བ་དག་བསྐོ་བར་བྱའོ། །

[Block 3244]
འདིའི་བསྐྲད་པའི་རྣམ་པ་ཡིན་ཏེ། ཇི་ལྟར་བསྐྲད་པ་སྐྱེ་བོ་ཆེན་པོས་སྒྲུབ་པར་མི་ནུས་ན་དེ་བཞིན་དུ་འདིར་དོན་སྒྲུབ་པའོ། །ཇི་ཙམ་དུ་གསལ་བ་དག་བསྐོ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་གྱི་ཚད་ལས་མི་ཉུང་བ་དག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སོང་ནས་དགེ་འདུན་ཚང་བ་ཇི་སྙེད་པ་དག་བསྐོའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3245]
སྡེ་ཚན་དེས་མི་ནུས་ན་རང་གིས་གསལ་བ་དག་བསྐོ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གཟུ་བོའི་སྡེ་ཚན་ནམ་གསལ་བའི་སྡེ་ཚན་ནམ། གསལ་བའི་ཡང་གསལ་བའི་སྡེ་ཚན་གང་ཡང་རུང་བས་རྩོད་པ་དེ་ཉེ་བར་ཞི་བར་མ་ནུས་ན། སྡེ་ཚན་དེ་རང་གིས་གསལ་བ་དག་བསྐོ་བར་རིགས་པ་ཉིད་ཡིན་ཏེ༌[^3203]ཆོས་དང་ལྡན་པ་དེ་ནི་མཉམ་པ་སྟེ། སྡེ་ཚན་དེ་རྣམས་ཀྱིས་ཀྱང༌[^3204]རང་གིས་གསལ་བ་དག་བྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3246]
དགེ་འདུན་གྱི་ཚད་ལས༌[^3205]མི་ཉུང་བ་དག་གོ་ཞེས་སྔར་སྨོས་པའི་བདག་པོའི་དབང་གིས་ཤེས་པར་བྱའོ། །

[Block 3247]
འདིར་གཞུང་ནི་ཁ་ཅིག་ལས་གཟུ་བོ་རྣམས་ཀྱིས་གསལ་བ་དག་བསྐོ་བར་གསུངས་ཏེ། གལ་ཏེ་དགེ་སློང་གཟུ་བོ་དག་གིས་རྩོད་པ་དེ་ཉེ་བར༌[^3206]ཞི་བར་བྱེད་མ་ནུས་ན་དགེ་སློང་གཟུ་བོ་རྣམས་ཀྱིས་དགེ་སློང་གསལ་བ་དག་བསྐོ་བར་བྱའོ་ཞེས་གསུངས་པ་དང་། ཁ་ཅིག་ལས་དགེ་འདུན་ལས་གསལ་བ་དག་བསྐོ་བར་གསུངས་ཏེ་གལ་ཏེ་དགེ་འདུན་གྱིས་རྩོད་པ་དེ་ཉེ་བར་ཞི་བར་བྱེད་མ་ནུས་ན་དགེ་འདུན་གྱིས༌[^3207]དགེ་སློང་གསལ་བ་དག་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ཏེ། འདིར་དེ་གཉིས་ཀ་ཡང་སྦྱར་བའི་དོན་གྲུབ་པ༌[^3208]ཞེས་བྱ་བ་དེ་གཉིས་ཀ་ཡང་ཁོངས་སུ་བསྡུ་བར་བྱའོ། །

[Block 3248]
ཁ་ཅིག་ལས་འདིར་གསལ་བ་དང་གསལ་བའི་གསལ་བ་རྣམས་བྱེད་པ༌[^3209]འབྱུང་བ་ཡིན་ནོ། །

[Block 3249]
གཞན་དག་ནི་གསལ་བ་དང་གསལ་བའི་གསལ་བ་འདིར་དེ་གཉིས་ཀའི་དཔེ་ཙམ་འདིར་ཞེས་བྱ་བ་དེས་འདི་རིག་པར་བྱའོ། །

[Block 3250]
མི་ནུས༌[^3210]ཤིང་གཞན་མི་བྱེད་ན་གང་ལས་བླངས་པ་དེ་ལ་དབུལ་ལོ་ཞེས་བྱ་བ་ནི་གང་དུ་རང་ལས་གཞན་གྱི་ཚོགས་མི་བྱེད་ཅིང་དེས་ཉེ་བར་ཞི་བར་མི་ནུས་ན་དེའི་ཚེ་དང་པོ་རྩོད་པ་དེ་གང་ལས་བླངས་པ་དེ་ཉིད་ལ་ཕྱིར་དབུལ་བར་བྱ་བ་སྟེ་གསལ་བའི་ཡང་གསལ་བ་དག་གིས་ནི་གསལ་བ་དག་ལའོ། །

[Block 3251]
གསལ་བ་དག་གིས་ནི་གཟུ་བོ་དག་གམ༌[^3211]དགེ་འདུན་དག་ལའོ། །

[Block 3252]
གཟུ་བོ་དག་གིས་ནི་རྒོལ་བ་དང་ཕྱིར་རྒོལ་བ་དག་ལའོ། །

[Block 3253]
གནས་བརྟན་དག་གིས་རྩོད་པ་སྦེད་པ༌[^3212]ལའོ། །

[Block 3254]
དེས་ནི་དགེ་འདུན་ལའོ། །

[Block 3255]
ཕྱིར་འོངས་ན་དགེ་འདུན་གཞི༌[^3213]བོས་རྩོད་པ་སྦེད་པ་བསྐོའོ་ཞེས་བྱ་བ་ནི་གསལ་བ་དག་ལས་རྩོད་པ་དེ་ཕྱིར་འོངས་ན་དགེ་འདུན་གཞི་བོས༌[^3214]རྩོད་པ་སྦེད་པ་བསྐོ་བར་བྱ༌[^3215]སྟེ། དེ་ཡང་དགེ་འདུན་གྱིས་སྤྲོ་བར་བྱས་ནས་གསོལ་བ་དང་གཉིས་ཀྱི་ལས༌[^3216]ཀྱིས་བསྐོ་བར་བྱའོ། །

[Block 3256]
དེས་ན༌[^3217]གནས་བརྟན་དང་བཅས་ཤིང་སོ་སོར་ཐར་པ་དང་བཅས་པའི་དགེ་འདུན་གཞན་ལ་དབུལ་ལོ་ཞེས་བྱ་བ་ནི་རྩོད་པ་སྦེད་པ་དེ༌[^3218]གནས་བརྟན་དང་བཅས་པ་སོ་སོར་ཐར་པ་དང་བཅས་པའི་དགེ་འདུན་ལ་དབུལ་བར་བྱའོ། །

[Block 3257]
སྔར་བྱུང་བ་བརྗོད་དེ་དུས་ཟླ་བ༌[^3219]གསུམ་དུ་དབུལ་ལོ་ཞེས་བྱ་བ་ནི་འདིར་ཁ་ཅིག་ནི་ཟླ་བ་དྲུག་གི་བར་དུ་བརྟན༌[^3220]ནས་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་དུ་སྨོས་པ་ཡིན་ཏེ་མདོ་སྡེ་འཛིན་པ་ལ་སོགས་པ་རྣམས་ལ་ལོ་གཅིག་གི་བར་དུ་བརྟེན༌[^3221]ནས་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3258]
ཤིན་ཏུ་ཡུན་རིང་པོར་འདིར་མང་པོ་རྣམས་ལ་འདི༌[^3222]ཀུན་ནས་ཉོན་མོངས་པར་རིགས༌[^3223]པ་མ་ཡིན་ནོ། །

[Block 3259]
དེ་བས་ན་དེ་ལ་མ་བརྟེན་ནོ། །

[Block 3260]
དེ་ནི་དེའི་འོ་ཞེས་བྱ་བ་ནི་དེ་ནི་རྩོད་པ་སྦེད་པར་བསྐོས་པ་དེའི་ཡིན་པ་སྟེ། དབུལ་བའི་བདག་ཉིད་ཀྱི་ལས་དེ་ནི་དབུལ་བ་ཐམས་ཅད་བསྡུས་པའི༌[^3224]ཕྱིར་མདོ་འདི་བྱས་སོ། །
--- END BLOCKS ---
