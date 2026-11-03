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
[Block 3186]
གང་ཞིག་འདིར་ཆོས་སྨྲ་བ་རྣམས་ཉུང་ལ་ཅིག་ཤོས་ཚད་པ་ཉིད་ལ་དགེ་སློང་གཉིས་ཀ་ལ་གཅིག་ལ་གཅིག་གི༌[^3110]ཕྱོགས་དང་གཞན་ལ་གཞན་གྱི་ཕྱོགས་པའི་ཕང༌[^3111]ལ་སོགས་པའི་ཕུལ་བ་དེ་ལ་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་གཉིས་ཀའི་ན་གཉིས་ཀའི་འོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་ཕྱོགས་གཉིས་ཀའི་དགེ་སློང་དག་གི་ཕྱོགས་གཅིག་དང་འབྲེལ་པ་ཅན་གཅིག་དང་། ཕྱོགས་གཞན་དང་འབྲེལ་པ་ཅན་གཞན་གྱི་ཕང་བ༌[^3112]ལ་སོགས་པར་ཕུལ་ན་ཕྱོགས་གཉིས་ཀ་དབང་བ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3187]
དེ་ལ་ཕྱོགས་གཉིས་ཀས་དབང་བ་ཉིད་ལ་ནི༌[^3113]ཅི་ཕྱོགས་བརྒྱ་ལ་གང་ཟག་གི་ལ༌[^3114]བགོ་བར་བྱ་བ་འམ་ཞེ་ན་དེའི་ཕྱིར། དེ་ལ་གང་ཟག་ལས་ཆ་ཉིད་ཡིན་གྱི་དགེ་འདུན་ལས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཟག་ཇི་སྙེད་ཡོད་པ་དེ་སྙེད་ཀྱི་ཆ་ཉིད་དུ་བྱའོ་ཞེས་བྱ་བའི༌[^3115]དོན་ཏོ། །

[Block 3188]
ལས་བྱེ་བའི་གཞི་ཞུ་བ་དང་བྲམ་ཟེའི་བུ་མོའི་སྐབས་སོ། །

[Block 3189]
ལས་བྱེ་བའི་གཞི་རྫོགས་སོ།། །།

[Block 3190 [HEADING]]
## རྩོད་པའི་གཞི། ^11-0

[Block 3191]
འཁོར་ལོ་བྱེ་བའི༌[^3116]བདག་ཉིད་དགེ་འདུན་གྱི་དབྱེན་ལ་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར། དགེ་འདུན་གྱི་དབྱེན་ནི་ཆོས་ལས་ཐ་དད་པར་དངོས་པོར་གསོལ་བས་སམ། དོན་དེས་ཚུལ་ཤིང་ལེན་དུ་འཇུག་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཆོས་ཞེས་བྱ་བ་ནི་ཐར་པའི་ལམ་ཡང་དག་པར༌[^3117]གྱུར་པ་སྟེ། དགེ་འདུན་གྱི་དབྱེན་ནི་ཆོས་ལས་ཐ་དད་པའི་དངོས་པོར་ཞེས་པའམ་གསོལ་བའི་བདག་ཉིད་ཀྱི་ལས་ཀྱིས་སོ། །

[Block 3192]
དོན་དེས་ཚུལ་ཤིང་ལེན་དུ་འཇུག་པས་དབྱེན་བྱེད་པའོ། །

[Block 3193]
དེ་ལས་ཐ་དད་པའི་དངོས་པོས་གང་དག་ལ་དེ་འདོད་པའི་ཚུལ་ཤིང་ལོང་ཤིག༌[^3118]ཅེས་བྱ་བའི་དོན་འདིས་ལེན་དུ་འཇུག་པའོ། །

[Block 3194]
དབྱེ་བར་བྱ་བ་དག་དགེ་འདུན་གྱི་ཚད་ཉིད་མ་ཡིན་པ་དང་མཚམས་ཀྱི་ནང་ན་གཞན་དགེ་འདུན༌[^3119]ཚད་དག་ཀྱང་མེད་པ་ཉིད་ཡིན་ནོ། །

[Block 3195]
དེ་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་འདིར་དགེ་འདུན་གྱི་ཚད་ནི་བཞི་ལ་སོགས་པ་ཡན་ཆད་དོ། །

[Block 3196]
དབྱེ་བར་བྱ་བའི་དགེ་འདུན་གྱི་ཚད་དག་ཀྱང་མེད་པ་ཉིད་ཡིན་ན་དགེ་འདུན་གྱི༌[^3120]དབྱེན་དེ་མི་འཆགས་སོ། །

[Block 3197]
དབྱེ་བར་བྱེད་པ་པོ་ལས་དབྱེ་བར་བྱ་བ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 3198]
དེ་ལྟ་བས་ན༌[^3121]ལྷན་ཅིག་ཏུ་འདི་རྣམས་ལ་དགེ་འདུན་གྱི་ཚད་ཉིད་རྟེན་པར༌[^3122]ཤེས་པར་བྱའོ། །

[Block 3199]
ཕྱོགས་གཞན་དུ་གྱུར་པའི་དགེ་འདུན་གྱི་ཚད་གཞན་རྣམས་ལ་མཚམས་ཀྱི་ནང་དུ་དགེ་འདུན་རྣམས་མེད་པ་ཉིད་ལ་དགེ་འདུན་གྱི་དབྱེན་མི་འཆགས་པའོ། །ཅི་འབྱེད་པ་ཐམས་ཅད་ལ་མཚམས་མེད་པར་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་ཆོས་དང་ཆོས་མ་ཡིན་པ་གཉིས་ཀ་དེ་བཞིན་ཉིད༌[^3123]དུ་ཤེས་ན་མཚམས་མེད་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆོས་ཀྱང་ཆོས་ཉིད་དུ་ཤེས་ལ་ཆོས་མ་ཡིན་པ་ཡང་ཆོས་མ་ཡིན་པ་ཉིད་དུ་འདུ་ཤེས་བཞིན་དུ་དགེ་འདུན་འབྱེད་པར་བྱེད་ན་དེ་ལ་མཚམས་མེད་པའི་ཁ་ན་མ་ཐོ་བར་འགྱུར་གྱི་ཆོས་ལ་ཆོས་མ་ཡིན་པར་འདུ་ཤེས་པ་དང་། ཆོས་མ་ཡིན་པ་ལ་ཆོས་སུ་འདུ་ཤེས་པ་ལ་ནི་མ་ཡིན་ཏེ། དེ་ལ་བསམ་པས་ལོག་པར་སྒྲུབ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 3200]
དབྱེ་བ་ལ་ཆོས་སུ་འདུ་ཤེས་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་མཚམས་མེད་པ་ཉིད་དུ་འགྱུར་རོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། [^3124]ཕུང་པོའི་ལྷག་མ་མེད་པ་ཆུད་ཟ་བ་དེ་ལས་བཟློག༌[^3125]ཅིང་དབྱེན་བྱེད་པས་འགྲོ་བ་རྣམས་ཐར་པ་ལས་བཟློག་པ༌[^3126]གང་ཡིན་པ་དེ་ནི་འདོད་པའི་ཁམས་ཀྱི་དབང་ཕྱུག་ལ་ཕན་པ་ཆེན་པོ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པའི་རྣམ་པར་འབྱེད་པ༌[^3127]ལ་ཆོས་སུ་འདུ་ཤེས་པས། དགེ་འདུན་གྱི༌[^3128]དབྱེན་བྱེད་ན་དེས་ནི༌[^3129]ཆོས་དང་ཆོས་མ་ཡིན་པ་དག་དེ་བཞིན་དུ་ཤེས་པ་ཡིན་པས་མཚམས་མེད་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3201]
ཡིད་གཉིས་ནི་འདུ་ཤེས་པ་དང་འདྲ་བར༌[^3130]དེའི་ཕྱིར་འདི་ལ་ཡིད་གཉིས་ཟ་བ་ན་ཡང་དེ་མཚམས་མེད་པར་འགྱུར་བར་རིག་པར་བྱའོ། །

[Block 3202]
འཁོར་ལོ་བྱེ་བའི་གཞིའོ།། །།

[Block 3203]
རྩོད་པ་ནི་རྣམ་པ་བཞི་སྟེ། འགྱེད་པའི་རྩོད་པ་དང་། མི་གདམས་པའི་ཕྱིར་རྩོད་པ་དང་། ལྟུང་བའི་ཕྱིར་རྩོད་པ་དང་། བྱ་བའི་ཕྱིར་རྩོད་པ་སྟེ། རྩོད་པ་བཞི་པོ་གང་དག་ཡིན་པ་དེ་དག་གི་རང་གི་ངོ་བོ་ངེས་པར་གཟུང་བའི༌[^3131]ཕྱིར་འཁྲུག་ལོང་གི་རྒྱུ་བཞིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚིག་གི་ཕྱིར་སེམས་གཞོལ་བ་གང་ཡིན་པ་དེ་ནི་འདིར་འཁྲུག་ལོང་ཞེས་བྱའི་ཁྲོ་བ་ནི་མ་ཡིན་ནོ། །

[Block 3204]
འདིར་ཚིག་ཅེས་བྱ་བ་ནི་དགྲ་བོས་མི་མཐུན་པར་སྨྲ་བ་ཡིན་པར་དགོངས་ཀྱི༌[^3132]ཚིག་ཙམ་ནི་མ་ཡིན་ཏེ། དེའི་ཕྱིར་དེ་ལ་འཁྲུག་ལོང་ཉིད་དུ་ཉེ་བར་གདགས་སོ། །

[Block 3205]
གཙུག་ལག་ལས་དེ་ལ་བརྟེན་ཏེ་འཐབ་པ་དང་མཚང༌[^3133]འདྲུ་བ་དང་རྩོད་པ་དང་འགྱེད་པ་གང་ཡིན་པ་དེ་འགྱེད་པའི༌[^3134]ཕྱིར་རྩོད་པ་ཞེས་གསུངས་ཏེ། འཁྲུག་ལོང་ནི་འདིའི་འཁོར་དུ་གྱུར་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3206]
ཡང་དག་པར་འཁྲུག་ལོང་ཉིད་རྩོད་པ་ཡིན་ཏེ། འདི་ལྟར་རྩོད་པའི་གཞི་ཡིན་པས་གཞིར་གྱུར་པའི་དངོས་པོར་ནི་འགྱེད་པའི་ཕྱིར་རྩོད་པ་ཡིན་པར་རིགས་པ་ཡིན་ནོ། །

[Block 3207]
དངོས་པོའི་དེ་བཞིན་ཉིད་ལ་ལོག་པར་སྒྲུབ་པ༌[^3135]དང་། སྤོང་བ་དང་ལྟུང་བ་དང་བཅས་པ་ཉིད་དང་ལས་ལ་མཐུན་པ་མི་སྦྱིན་པའོ་ཞེས་བྱ་བ་ནི་ཆོས་ཡིན་ནོ་ཞེ་འམ་ཆོས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་ལྟར་དངོས་པོ་རྣམས་ཀྱི་དེ་བཞིན་ཉིད་ཀྱི༌[^3136]ངོ་བོ་ལས༌[^3137]ལོག་པར་བསྒྲུབ་པ་དེ་ནི་འཁྲུག་ལོང་གི་རྒྱུ་དང་པོ་ཡིན་ནོ། །

[Block 3208]
འདི་ལྟར་དངོས་པོའི་རྣམ་པ་ལ་སྤྱོད་པ་ལས་ཀྱང་འགྱེད་པ་འབྱུང་བའི་ཕྱིར་ཏེ། ཅིའི་ཕྱིར་ཁྱོད་ཀྱིས་བླངས་ཤེའམ་བྱིན་ཞེ་འམ་ལས་སུ་བསྐོས་པ་ནི་མ་བྱས་ཞེས་འགྱེད་པ༌[^3138]ཡིན་པ་དེ་ཡང་དངོས་པོའི་དེ་བཞིན་ཉིད་ཡིན་ནམ་མ་ཡིན་ཏེ་འདི་ནི་བྱ་བའོ༌[^3139]ཞེའམ་བྱ་བ་མ་ཡིན་ནོ་ཞེས་ཞུགས་པའི་ཕྱིར་རོ་ཞེ་ན། འདི་ལྟ་སྟེ། དེ་ལྟ་བུའི་རིགས་ཅན་འདིར་མ་བསྡུས་པས༌[^3140]ཤེས་པར་མི་བྱའོ། །

[Block 3209]
སྤོང་བ་ཞེས་བྱ་བ་ནི་གདམས་ངག་ལ་སོགས་པ་འཇོག་པར་འགྱུར་བས་གཞན་སྤོང་བ་སྟེ་དེ་ནི་འཁྲུག་ལོང་གི་རྒྱུ་གཉིས་པ་ཡིན་ནོ། །

[Block 3210]
རྒྱུ་དེ་ལས་མི་གདམས་པའི་ཕྱིར་རྩོད་པ་འདི་བརྗོད་པའོ། །

[Block 3211]
ལྟུང་བ་དང་བཅས་པ་ཉིད་ཅེས་བྱ་བ་ནི་འཁྲུག་ལོང་གི་རྒྱུ་གསུམ་པ་ཡིན་ཏེ་དེ་ལས་ལྟུང་བའི་ཕྱིར་རྩོད་པ་འབྱུང་ངོ་། །ལས་ལ་མཐུན་པ་མི་སྦྱིན་པ་ཞེས་བྱ་བ་ནི་གསོལ་བ་ལ་སོགས་པའི་ལས་ལ་མཐུན་པ་མི་སྦྱིན་པ་སྟེ༌[^3141]དེ་ནི་འཁྲུག་ལོང་གི་རྒྱུ་བཞི་པ་ཡིན་ཏེ། དེ་བས་ན་བྱ་བའི་ཕྱིར་རྩོད་པ་ཞེས་བྱ་བའི་ཚིག་འདི་འབྱུང་ངོ་། །རྒྱུ་དང་པོ་ལས་བྱུང་བ་ནི༌[^3142]རྒྱུ་དག་ཅིག་ཏུ་བྱ་བས་ཉེ་བར་ཞི་བའོ་ཞེས་བྱ་བ་ནི།

[Block 3212]
དང་པོ་ཞེས་བྱ་བ་དངོས་པོའི་དེ་བཞིན་ཉིད་ལ་ལོག་པར་སྒྲུབ་པ་ཞེས་བྱ་བ་དེའི་རྒྱུ་འཁྲུག་ལོང་གང་ལ་དེ་ནི་རྒྱུད་གཅིག་ཏུ་བྱས་པས་ཉེ་བར་ཞི་བར་འགྱུར་ཏེ་མངོན་སུམ་གྱིས་འདུལ་བར༌[^3143]འགྱུར་ཞེས་བྱ་བ་ཡང་དེ་ཡིན་ནོ། །

[Block 3213]
གང་ཞིག་སླར་ངོ་བོ་ཉིད་ཚོལ་དུ་གཞུག་པས་གཞན་བལྟ་བར༌[^3144]བྱའོ། །

[Block 3214]
རྒྱུད་ཅེས་བྱ་བ་ནི་ངེས་པར་རྟོགས་པས་ཏེ་དངོས་པོ་གང་ལ་ངེས་པར་རྟོགས་པ་གཅིག་ཡོད༌[^3145]པའི་དངོས་པོ་དེ་ནི་རྒྱུད་གཅིག༌[^3146]བྱ་བ་སྟེ་ངེས་པ་སྐྱེས་པས༌[^3147]མཐའ་གཅིག་ཏུ་བྱ་བ་དེས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3215]
རྒྱུ་གཉིས་པ་ལས་བྱུང་བ་ནི་འདི་དང་དག་པ་སྦྱིན་པས་སོ་ཞེས་བྱ་བ་ནི་སྤོང་བའི་རྒྱུ་འཁྲུག་ལོང་ལ་གཅིག་ཏུ་ཞེས་བྱ་བ་སྨོས་པ་འདི་དང་དག་པ་སྦྱིན་པས་ཉེ་བར་ཞི་བར་འགྱུར་ཏེ། དྲན་པས་འདུལ་བ་དང་། མ་མྱོས་པས་འདུལ་བ་ཞེས་བྱ་བ་ཡང་དེ་བཞིན་ནོ། །

[Block 3216]
རྒྱུ་གསུམ་པ་ལས་བྱུང་བ་ནི་ཕྱིར་བཅོས་པ་དང་ངེས་པར་འཛིན་པ་ལ་སྦྱར་བ་ཉིད་སྦྱིན་པས་སོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་དང་བཅས་པ་ཉིད་ཅེས་བྱ་བ་ལས་བྱུང་བའི་རྒྱུ་འཁྲུག་ལོང་ཕྱིར་བཅོས་པ་ཞེས་བྱ་བ་བཤགས་པས་ཉེ་བར་ཞི་བར་བྱ་བ་དང་། ངེས་པར་འཛིན་པ་ལ་སྦྱར་བ༌[^3148]ཉིད་སྦྱིན་པས༌[^3149]ངེས་པར་འབྱུང་བར་གཏོགས་པའི་ངེས་པས༌[^3150]སྦྱར་བ་ཉིད་དོ། །

[Block 3217]
དེ་སྦྱིན་པས་དེའི་ངོ་བོ་ཉིད་ཚོལ་དུ་གཞུག་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3218]
ཐ་མའི་ནི་སྦྱིན་དུ་གཞུག་པས་སོ་ཞེས་བྱ་བས་ནི་མཐུན་པར་མི་སྦྱིན་པ་ཞེས་བྱ་བའི་རྒྱུ་ལས་བྱུང་བའི༌[^3151]འཁྲུག་ལོང་སྦྱིན་དུ་གཞུག་པས་ཕྱིར་བཅོས་པའོ། །

[Block 3219]
མཐུན་པ་སྦྱིན་པས་མཐུན་པ་ཉིད་དུ་གྱུར་ན་བྱ་བའི་ཕྱིར་རྩོད་པ་ཉེ་བར་ཞི་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3220]
འོ་ན་རྒྱུད་གཅིག་ཏུ་བྱ་བས༌[^3152]ཉེ་བར་ཞི་བར་བྱའོ་ཞེས་གང་བསྟན་པ་དེ་ཇི་ལྟར་རྒྱུད་གཅིག་ཏུ་བྱ་ཞེ་ན། དེའི་ཕྱིར་འགྱེད་པ་གཉིས་རང་གིས༌[^3153]མི་ནུས་ན་ཚོགས་པར་དབྱུང་བ་དག་གིས་ལེགས་པར་བསྒྲུབ་པོ༌[^3154]ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་འགྱེད་པར་བྱེད་པ་དེ་གཉིས་རང་གིས་རྩོད་པ་དེ་ཉེ་བར་ཞི་བར་བྱེད་མི་ནུས་ན་ཚོགས་པར་དབྱུང་བ་དག་གིས༌[^3155]དོན་དེ་ལེགས་པར་བསྒྲུབ་ཅིང་མཐའ་གཅིག་ཏུ་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

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
--- END BLOCKS ---
