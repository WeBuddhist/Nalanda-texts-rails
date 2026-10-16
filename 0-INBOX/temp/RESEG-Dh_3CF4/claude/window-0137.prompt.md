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
[Block 4796]
དང་བ་ནི་དེའི་ཚེ་བདག་གིས་ཕྱུང་བར་རོ། །

[Block 4797]
དགྱེས་པ༌[^3106]དང་། དང་བ་དག་ནི། དགྱེས་པ༌[^3107]དང་དང་བ་དག་གོ། །

[Block 4798]
དེ་གཉིས་ཀྱིས་ཞལ་མངོན་དུ་ཕྱོགས་པ་ནི། དགྱེས་བཞིན༌[^3108]དང་བའི་ཞལ་གྱིས་མངོན་དུ་ཕྱོགས་པའོ། །

[Block 4799]
ཡང་ན་དགྱེས་ཤིང་དགའ་བས་ཞལ་མངོན་དུ་ཕྱོགས་པ་ནི།

[Block 4800 [VERSE]]
དགྱེས་ཤིང་དགའ་བས་ཞལ་མངོན་དུ་ཕྱོགས་པའོ། །
བདག་གི་སྲོག་ཀྱང་རི་དགས་ཁྱོད་དབང་ན། །

[Block 4801]
ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི་གང་དུ་འགྲོ་བར་བྱ་བ༌[^3109]དེའི་ཕན་ཡོན་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4802]
ནགས་ཚལ་རྔོན་པས་གང་ཞིང་ཞེས་བྱ་བ་ནི་འདི་དག་ཏུ་གནས་པ་དེའི་ཉེས་དམིགས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4803]
ཉེས་དམིགས་ཀྱང་རྣམ་པ་གཉིས་ཏེ། ལུས་དང་སེམས་ཀྱིའོ། །

[Block 4804]
དེ་ལ་སེམས་ཀྱི་ཉེས་དམིགས་ནི་འཇིགས་པ་དང་བཅས་པ་སྟེ། ཅིའི་ཕྱིར་འཇིགས་པ་དང་བཅས་པ་ཡིན༌[^3110]ཞེ་ན། ནགས་ཚལ་དེ་དག་རྔོན་པས་གང་བའི་ཕྱིར་རོ། །

[Block 4805]
ལུས་ཀྱི་ཉེས་དམིགས་ནི་གྲང་བ་དང་། ཚ་བ་དང་། ཆར་འབབ་པའི་སྡུག་བསྔལ་དང་ལྡན་པའི་ཕྱིར་ཏེ། གྲང་བ་དང་། ཚ་བ་དང་། ཆར་སྨོས་པས་ནི་དུས་ལས་བྱུང་བའི་ཉེས་དམིགས་སོ། །

[Block 4806]
སྩོགས་པ་སྨོས་པས༌[^3111]ནི་བཀྲེས་པ་དང་། སྐོམ་པ་ཡིན་ཏེ། ལྷན་ཅིག་སྐྱེས་པའི་སྡུག་བསྔལ་གཟུང༌[^3112]ངོ་། །བདག་གིས་ཁྱོད་བོར་ནས་ཞེས་བྱ་བ་ནི་ཕན་གདགས་པར་བྱས་པས་སོ། །

[Block 4807]
[^3113]ཁྱིམ་གྱི་གནས་ཡིན་པས་ཁྱིམ་ན་གནས་པ་སྟེ།[^3114] ཁྱིམ་དེས་མི་གནས་པའོ། ། ཅིའི་ཕྱིར་མི་གནས་ཤེ་ན། དེ་བསྟན་པའི་ཕྱིར། དེ་བས་མི་རྣམས་བདེ་བའང་གཞན་ལ་གསལ། །ཞེས་བྱ་བ་སྨོས་ཏེ། གཞན་ནི་རིགས༌[^3115]མི་མཐུན་པ་སྟེ། །རི་དྭགས་རིགས༌[^3116]དང་མཐུན་པའི་བདེ་བའང་གཞན། །ཞེས་བྱ་བའོ། །

[Block 4808]
དུད་འགྲོ་ལ་སྙིང་རྗེ་བྱ་བ་བསྟན་པ་སྟེ། དུད་འགྲོའི་རང་བཞིན་ཞེས་བྱ་བ་འདིས་ནི་དུད་འགྲོའི་ཉི་ཚེ་ལ་སྙིང་རྗེ་བྱ་བར་བསྟན་ཏོ། །

[Block 4809]
ཐམས་ཅད་ལ་སྙིང་རྗེ་བྱ་བར་བསྟན་པའི་ཕྱིར། བདེ༌[^3117]ལ་གནས་དང་སྡུག་བསྔལ་འབྲལ་འདོད་པ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་བཞི་སྨོས་སོ། །

[Block 4810]
བདེ་བའི་གནས་ཡིན་པས་བདེ༌[^3118]ལ་གནས་པ་སྟེ། དེ་ལ་སྡུག་བསྔལ་དང་མི་ལྡན་པ་ནི་བདེ་བ་ལ་གནས་པའོ། །

[Block 4811]
མེད་པར་བྱ་བའི་བློ་ནི་འབྲལ་བར་འདོད་པ་སྟེ། སྡུག་བསྔལ་དང་འབྲལ་བར་འདོད་པ་ཉིད་སྡུག་བསྔལ་བསལ་བར་འདོད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4812]
དེས་ན་དེའི་ཕྱིར་གང་ལ་བདག་ཉིད་གནས་པ་དང་། སྡུག་བསྔལ་དང་འབྲལ་བར་འདོད་པ་དེ་ལ་བློ་མཚུངས་པའི་ཕྱིར་རོ། །

[Block 4813]
ཅིའི་ཕྱིར་སྡུག་བསྔལ་དང་འབྲལ་བར་འདོད་པ་ཕྱིས་བཤད་ཅིང་སྔར་མ་བསྟན། སྡུག་བསྔལ་བསལ་བར༌[^3119]ཡང་དག་པར་འཛིན་དུ་འཇུག་པ་སྔར་བསྟན་ནས་ཕྱིས་བདེ་བ་ལ་གནས་པ་ལ་ཡང་དག་པར་འཛིན་དུ་འཇུག་པར་རིགས་སོ་ཞེ་ན། ཚུལ་དེས་རྗེས་སུ་བསྟན་པ་ནི་མ་ཡིན་ཏེ། འདི་ལྟར་བསྟན་པ་ནི་དང་པོ་དོན་དུ་གཉེར་བའི་དུས་སུ་ནི་བདེ་བ་ཐོག་མར་དོན་དུ་གཉེར་བ་ཡིན་ཏེ། དེའི་འོག་ཏུ་སྡུག་བསྔལ་མེད་པ་ཡིན་པས་བདེ་བ་ལ་གནས་པ་ཞེས་བྱ་བ་སྔར་བསྟན་ཏེ། སྡུག་བསྔལ་དང་བྲལ་བ་ཞེས་བྱ་བ་འོག་ཏུ་བསྟན་ཏོ། །

[Block 4814]
ཚིགས་བཅད་འདིའི་དང་པོ་ཕྱེད་ཀྱིས་ནི་ཡང་དག་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4815]
ཕྱེད་འོག་མས་ནི་ཡང་དག་པར་འཛིན་དུ་གཞུག་པའི་ཕྱིར་རོ། །

[Block 4816]
བདེ་བ་ལ་གནས་པ་ཞེས་བྱ་བ་འདི་བསྟན་པའི་ཕྱིར། གྲགས་པ་མེད་ཅིང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4817]
གཞན་དག་མི་འདོད་པར་བྱེད་པའི་ཉེས་དམིགས་དང་། དེ་སྤང་བར་བསྒྲུབ་པའི་དབང་དུ་བྱས་ནས་ཚིགས་བཅད་འདི་གཉིས་ཀྱིས༌[^3120]གོ་རིམས་བཞིན་དུ་སྦྱར་རོ། །

[Block 4818]
ཉེས་དམིགས་ཀྱང་རྣམ་པ་གཉིས་ཏེ། གྲགས་པ་མེད་པ་དང་། སྐྱེ་བོ་དམ་པས་སྨད་པ་སྟེ། འདི་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཉེས་དམིགས་སོ། །

[Block 4819]
སྡུག་བསྔལ་སྡིག་ལས་འབྱུང་བར་ཞེས་བྱ་བས་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཉེས་དམིགས་བསྟན་ཏེ། སྡིག་པ་དེའི་རྒྱུས་ངན་སོང་གི་སྡུག་བསྔལ་འབྱུང་བའི་ཕྱིར་རོ།[^3121] །དགྲ་བོའི་ཕྱོགས་བཞིན་སྡིག་པ་སྤང་བར་མཛོད། །ཅེས་བྱ་བ་ནི་དེ་སྤང་བར་བསྒྲུབ་པའི་དབང་དུ་བྱས་པ་སྟེ། དེ་ཡང་དགྲ་དང་འགྲོགས་པའོ། །

[Block 4820]
དགྲ་དག་ལས་གྲུབ༌[^3122]པ་ཡང་རྣམ་པ་གཉིས་ཏེ། གསད་པ༌[^3123]དང་། གཞོམ་པར་བྱ་བའོ། །

[Block 4821]
གཞོམ་པ་ནི་གནོད་པའི་ནང་དུ་འདུས་པ་ཡིན་ནོ། །

[Block 4822]
གྲོགས་པོ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། སྒྲུབ་པ་དང་། [^3124]གཞག་པའོ། །

[Block 4823]
དེ་ལས་སྡིག་པ་ལ་ཇི་ལྟར་བསྒྲུབ་བར་བྱ་ཞེ་ན། སྨྲས་པ། ཇི་ལྟར་དགྲ་ཆེན་པོ་ལས་ཐར་ཅིང་དེ་སྤང་བར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4824]
དེ་ནི་ནད་བཞིན་ཡལ་བར་དོར་མི་རིགས། །ཞེས་བྱ་བ་ནི་གྲོགས་པོ་ངན་པ་ལ་སྒྲུབ་པ་ཡིན་ཏེ། དེ་ཡང་སྡིག་པ་བྱེད་དུ་མི་གཞུག་སྟེ། དེ་གང་ཡིན་ཞེ་ན། གཞག་པར་བྱའོ། །

[Block 4825]
ཡལ་བར་མི་དོར་བ་ནི་དེའི༌[^3125]གནས་ལ་གཞག་པའི་དོན་ཏོ། །

[Block 4826]
འདི་སྐད་སྟོན་པ་ཡིན་ཏེ། གསད་པར་མ་ནུས་ཀྱང་གཞོམ་པར་བྱ་བ་དང་། ཇི་ལྟར་འཕགས་པ་རྣམས་ཀྱིས་གྲོགས་པོ་ལ་གཞག་པར་བྱ་བ་བཞིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4827]
གང་སྔར་བསྟན་པའི་བདེ་བ་ལ་གནས་པ༌[^3126]དང་སྡུག་བསྔལ་འབྲལ་བར༌[^3127]འདོད་པ།

[Block 4828 [VERSE]]
སེམས་ཅན་ཐམས་ཅད་མཚུངས་པ་མེད་པར་འདོད། །
ཅེས་བྱ་བ་དེ་ལ་བསྒྲུབ་པར་བྱ་བ།
དེ་བས་བདག་ཉིད་མི་འདོད༌[^3128]གང་ཡིན་པ། །
དེ་དག་གཞན་ལའང་བགྱི་བར་མི་རིགས་སོ། །

[Block 4829]
ཞེས་བྱ་བ་ཡིན་ཏེ། དེ་བས་ན་དོན་ལ་འཇུག་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 4830 [VERSE]]
དེ་བས༌[^3129]བདག་ཉིད་མི་འདོད་གང་ཡིན་པ། །
དེ་དག་གཞན་ལའང་བགྱི་བར་མི་རིགས་སོ། །

[Block 4831]
ཞེས་བྱ་བ་དེ་ལ། དེ་མི་འདོད་པ་ནི་ཅི། ཇི་ལྟར༌[^3130]བསྒྲུབ་པར་བྱ་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར། གང་ལ་བརྟེན་ནས་དཔལ་གྱི་གནས་གྱུར་པ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། དཔལ་གྱི་གནས་སུ་གྱུར་ཅེས་བྱ་བ་འདིས་ནི་སྦྱིན་པའི་འབྲས་བུ་བསྟན་ཏེ། གང་གི་ཕྱིར་སྦྱིན་པས་ནི་འབྲས་བུ་ལོངས་སྤྱོད་ཆེན་པོ་འཐོབ་པར་འགྱུར་ཏེ། གཞན་དག་གི་དབུལ་བ་བསལ་བས་བདག་ལ་ཡང་དབུལ་བའི་གཉེན་པོ་ལོངས་སྤྱོད་འབྱུང་བ་ཡིན་ཏེ། དེ་བས་ན་བདག་ཉིད་འདོད་པ་གཞན་ལ་སྤྱད་པ་ཡིན་ནོ། །

[Block 4832]
གང་ལ་བརྟེན་ནས༌[^3131]ཞེས་བྱ་བ་ནི་སྦྱིན་པ་གང་ལ་བརྟེན་ནས་སོ། །

[Block 4833]
འཇིག་རྟེན་བསྔགས་པ་ཞེས་བྱ་བ་འདིས་ནི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་བསྟན་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་འཇིག་རྟེན་པ་རྣམས་ལ་བཟོད་པ་བྱས་ནས་ནི་སྐྱེ་བོ་མང་པོ་དག་དགའ་བར་འགྱུར་ཏེ། གཡོག་འཁོར་མང་བར་ཡང་འགྱུར་རོ། །

[Block 4834]
གང་ལ་བརྟེན་ནས་ཞེས་བྱ་བ་ནི་བཟོད་པ་གང་ལ་བརྟེན་ནས་སོ། །

[Block 4835]
རྒྱལ་སྲིད་འཐོབ་འགྱུར་ཞེས་བྱ་བས་ནི་ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུ་བསྟན་ཏེ། གང་གི་ཕྱིར་རིགས་ལ་སོགས་པ་ཕུན་སུམ་ཚོགས་པ༌[^3132]ཁྱད་པར་དུ་གྱུར་བ་ལ་ནི་རྒྱལ༌[^3133]སྲིད་ཅེས་བརྗོད་དེ། རྒྱལ་སྲིད་ཐོབ་པ་དེ་ཡང་ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུའོ། །
--- END BLOCKS ---
