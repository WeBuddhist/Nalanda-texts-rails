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
ནང་དུ་འཚེད་པ་དང་སྨིག་པ་དག་ལ་སྒྲུབ་པ་གང་ཡིན་ཞེ་ན། གནས་སུ་འདི་དག་ལ་མི་མཐུན་པ་ཉིད་དོ། །

[Block 4062]
དེ་ལྟ་བས་ན་ཇི་སྲིད་གནས་ཀྱི་བློ་ཡོད་པ་དེ་སྲིད་དུ་ཞེས་བྱའོ། །

[Block 4063]
དེ་ཡང་ཕྱི༌[^2815]རོལ་འདོམ་གང་དང་བཅས་པའོ། །

[Block 4064]
གཞི་མེད་པའི་གནས་སུ་ཇི་ལྟར་བྱ་ཞེ་ན། ཇི་སྲིད་དུ་དེར༌[^2816]ལྷག་པར་གནས་པའི་ངོ་བོས་སྒྲུབ་པར༌[^2817]བྱེད་པ་དེ་སྲིད༌[^2818]སྤང་བར་བྱའོ། །

[Block 4065]
དགེ་སློང་གྲོང་དག་ཏུ་དགེ་སློང་རྣམས་ཀྱི༌[^2819]དོན་དུ་ཉེ་བར་མི༌[^2820]མཁོ་བའི་གནས་རྣམས་གང་ཡིན་པར་བྱེད་པ་དེ་རྣམས་ལ༌[^2821]ཇི་ལྟར་བྱ་ཞེ་ན། གང་ཞིག་དེར་དགེ་སློང་རྣམས་ཀྱི་གནས་དོན་དུ་དེ་ཉེ་འཁོར་དང་བཅས་པ་སྤང་བར་བྱའོ། །

[Block 4066]
དེ་བཞིན་དུ་གཞན་ལ་ཡང་ངོ་། །ཝ་ནས་ཆུ་འཛག་པ་གང་དུ་བབ་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། ཝ་ནས་ཆུ་འཛག་པ་རྣམས་ཀྱི་ནི་སྨྱུག་མ་བཞིན་དུ་གཙུག་ལག་ཁང་གི་ཁོངས་སུ་གཏོགས་པ་ཉིད་ཡིན་ནོ། །

[Block 4067]
དེ་བས་ན་ཁྱམས་བཞིན་དུ་དེའི་འོག་ཆ་འདི་ཞུགས་པའོ། །

[Block 4068]
ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་གལ༌[^2822]གཉིས་སུ་བཏགས་པ༌[^2823]མ་ཡིན་གྱི། གང་དུ་ཝ་ནས་ཆུ་འཛག་པ་ཡོད་པ་དེ་ལ་ནི་འདི་ཡིན་ནོ། །

[Block 4069]
གཞན་ལ་ནི་རྩིག་པ་ཞེས་བྱ་བ་བསྟན་པའི་དོན་དུའོ། །

[Block 4070]
མཚམས་དེའམ་འདི་ཞེས་བྱ་བ་ཝ་ནས་ཆུ་འཛག་པའི་ཝ་ཡིན་ནོ། །

[Block 4071]
གྲོང་ལ་ཉེན་ཀོར་གྱི་མཐའ་ཚུན་ཆད་དོ་ཞེས་བྱ་བ་ནི།[^2824] གྲོང་ལ་སྔར་འབྲལ་བའི་སྐབས་སུ་གྲོང་གི་ཉེན་ཀོར་བསྟེན་པ་གང་ཡིན་པ༌[^2825]དེའི་མཐའ་ཚུན་ཆད་མཚམས་ཡིན་ཏེ། འདིར་གཞུང་ནི་ལུང་སིལ་བུ་དག་ལས་གསུངས་པ་ཡིན་ནོ། །

[Block 4072]
དགོན་པ་ལ་ནི་ཕྱོགས་ཕྱོགས༌[^2826]སུ་རྒྱང་གྲགས་ཀྱི་མཐའ་ཚུན་ཆད་དོ་ཞེས་བྱ་བ་ནི། དགོན་པ་ལ་དབུས་ནས་བརྩམས་ཏེ་ཞེས་བྱ་བ༌[^2827]བསྟན་པའི་ཕྱིར་ཕྱོགས་ཕྱོགས་སུ་ཞེས་སྨོས་སོ། །

[Block 4073]
གསོ་སྦྱོང་གི་གཞི་ལས་གནས་ཀྱི་སྐབས་སོ།། །།

[Block 4074]
འདིར་གསོ་སྦྱོང་དང་དགག་དབྱེའི་དོན་དུ་མཛད་དེ་འདུན་པ་འབུལ་བ་གསུངས་མོད་ཀྱི་ཚོགས་པར་གཏོགས་པ་གཞན་ཐམས་ཅད་ལ་ཡང་ཡོད་པས། ལས་ཐམས་ཅད་ལ་རྣམ་པར་གནས་པ་དེ་བས་ན་ཐམས་ཅད་ཀྱི་དབང་དུ་བྱ་སྟེ་བསྟན་པའི་ཕྱིར། འདུན་པ་འབུལ་བས་ལས་དེ་དང་མཐུན་པ་འགྲུབ་པོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་དང་ཞེས་བྱ་བ་ནི་འདུན་པ་འབུལ་བར་བྱེད་པ་གང་ཡིན་པའི་གང་ཟག་དེས་སོ། །

[Block 4075]
མཚམས་བཅད་པའི་ལས་ནི་མི་འགྲུབ་བོ་ཞེས་བྱ་བ་ནི། འདུན་པ་འབུལ་བར༌[^2828]བྱེད་པ་དེའི་ཚོགས་པ་མཐུན་པ་མི་འགྲུབ་བོ། །

[Block 4076]
འདིར་གཞུང་ནི་ཉེ་བ༌[^2829]འཁོར་ལས་ཐམས་ཅད་ལ་འདུན་པ་དང་བཅས་པ་ཡིན་ཏེ། མཚམས་བཅད་པ་ནི་མ་གཏོགས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4077]
གླེང་གཞི་དག་ལས་དེ་ལ་སོགས་པ་འདུན་པ་འབུལ་བ་ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 4078]
བསླབ་པ་བྱིན་པ་ལས་དེ་བླང་དུ་རུང་ངོ་ཞེས་བྱ་བ་ནི། འདིར་དེ་ཞེས་བྱ་བའི༌[^2830]སྒྲ་ནི་འདུན་པ་བཟང་ངོ་། །བསླབ་པ་བྱིན་པ་ལས་འདུན་པ་བླང་བ་སུ་ལ་རུང་ཞེ་ན། དེའི་ཕྱིར་དེ་ལ་དགེ་སློང་གི༌[^2831]འདུ་ཤེས་ཉེ་བར་གཞག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསླབ་པ་བྱིན་པ་དེ་ལ་དགེ་སློང་གི་འདུ་ཤེས་ཉེ་བར་གཞག་པ་དེ་ལ་དགེ་སློང་གི་འདུ་ཤེས་སོ། །

[Block 4079]
དེ་ཉེ་བར་གནས་པ་གང་གིས་དེ་ལས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4080]
དབུལ་དུ་མི་རུང་ངོ་ཞེས་བྱ་བ་ནི་བསླབ་པ་བྱིན་པ་དེ་ལ་འདུན་པ་དབུལ་དུ་མི་རུང་སྟེ། དགེ་འདུན་དུ་གྱུར་པ་འདིར་ཡང་མ་ཡིན་ཞེས་བྱ་བ་བྱེ་བྲག་མེད་པར་གཏོགས་པའོ། །

[Block 4081]
ཡོངས་སུ་དག་པ་དང་དགག་དབྱེ་དག་ལ་ཡང་འདིས་བྱས་པར་འགྱུར་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4082]
སྨྱོས་པའི་གནང་བ་ཐོབ་པས་ནི་མི་མཐུན་པ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 4083]
ཡོངས་སུ་དག་པ་ཕུལ་བ་དང་ཡང་གཅིག་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། འགྲུབ་བོ་ཞེས་བྱ་བའི་རྗེས་བསྙེག༌[^2832]པའི་ཕྱིར་ཡང་ཞེས་བྱ་བའི་སྒྲ་སྨོས་ཏེ། གང་དང་ལྷན་ཅིག་པ་ཉིད་ཅེས་བྱ་བ་འདི་ལ་དགེ་འདུན་དང་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པའོ། །

[Block 4084]
དོན་གང་ལ་གཅིག་ཉིད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གསོ་སྦྱོང་དང་དགག་དབྱེ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཅིག་པ་ཉིད་དུ་འགྱུར་ཞེས་བྱ་བར་སྦྱར་རོ། །ཅི་ཞིག་བྱས་པས་ཤེ་ན། དེའི་ཕྱིར་དེ་ཕུལ་བས་སོ། །

[Block 4085]
ཡོངས་སུ་དག་པ་དང་དགག་དབྱེ་ཕུལ་བས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4086]
དེ་བཞིན་དུ་དེ་གཉིས་ལའོ་ཞེས་བྱ་བ་ལ། དེ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་དག་པ་དང་དགག་དབྱེ་འབུལ་བ་དག་གིས་སོ། །

[Block 4087]
དེ་གཉིས་ལ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་དང་དགག་དབྱེ་ལའོ། །

[Block 4088]
རྟོགས་པ་པོ་ལ་ཆོ་ག་འདི་ལེགས་པ་ཉིད་དུ་བསྟན་གྱི་དགེ་འདུན་དུ་ལོངས་པས༌[^2833]ནི་མ་ཡིན་ནོ། །

[Block 4089]
དེ་བརྗོད་པར་བྱ་སྟེ། ཆོ་ག་ནོད་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡོངས་སུ་དག་པ་དང་དགག་དབྱེ་ཕྲལ་བས༌[^2834]གསོ་སྦྱོང་དང་དགག་དབྱེ་གཉིས་བྱ་བའི་ཆོ་གའོ། །

[Block 4090]
ཚོགས་ཐ་དད་པས་འདུན་པ་ལ་སོགས་པས་མཐུན་པར་བྱ་སྟེ། ལས་བྱེད་པ་ལ་མི་རུང་བ་ཉིད༌[^2835]དོ་ཞེས་བྱ་བ་ནི། བཀོད་པ་སྣ་ཚོགས་པ་བཅིངས་པར་གྱུར་པ་ཉིད་ཀྱིས་དེ་ལ་མི་རིགས་པའི་བློ་སྐྱེ་བ་སྟེ། དེ་བསལ་བའི་དོན་དུ་འདིའོ། །

[Block 4091]
འདིར་ཁ་ན་མ་ཐོ་བ་མེད་པའི་འདུན་པ་ལ་སོགས་པ་འབུལ་བའི་སྐབས་མ་ཡིན་པར་ཤེས་པར་མི་བྱ་སྟེ། འདི་ནད་པ་ལ་སོགས་པ་དབང་པོ་ཉིད་རིགས་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4092]
འདིར་གཞུང་ནི༌[^2836]ཞུ་བ་ལས།

[Block 4093]
བཙུན་པ་དགེ་སློང་ཕྱོགས་གཅིག་ན་མཆིས་པས་གནས་བཞི་པོ་དག་ཏུ་སོ་སོར༌[^2837]ཐར་པའི་མདོ་བཏོན་པ་ལ་གསོ་སྦྱོང་ཡང་བགྱིས་པར་འགྱུར་ཞིང་། དགེ་སློང་དེ་དག་ལ་ཡང་འགལ་ཚབས་ཅན་དུ་མི་འགྱུར་བ༌[^2838]མཆིས་སམ། ཉེ་བ༌[^2839]འཁོར་ཡོད་དེ། འདི་ལྟར་སོ་སོར་ཐར་བའི་མདོ་འདོན་པའི་དགེ་སློང་གི་གནས་བཞི༌[^2840]པོ་དག་ཅིག་ཅར་དུ་ཤིང་ངམ། དབྱུག་པའམ། རེ་ལྡེས་མནན་ཏེ་སོ་སོར་ཐར་པའི་མདོ་འདོན་ནའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 4094]
བརྗོད་པར་བྱ་བ་རྩོམ་པ་འདྲ་བ་རྣམས་ཅིག་ཅར་བརྗོད་པ་ལ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི་མི་རུང་བ་མེད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4095]
ཅིག་ཅར་ཞེས་བྱ་བ་ནི་ཐབས་ཅིག༌[^2841]གིས་བསྒྲུབ་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4096]
འདུན་པ་དང་ཡོངས་སུ་དག་པ་གཉིས་ལྷན་ཅིག་ཏུ་འདུན་པ་དང་དགག་དབྱེ་དག་ལ་ཡང་བརྗོད་དོ། །

[Block 4097]
བརྗོད་པ་ཡང་རིག་པར་བགྱིད་དོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 4098]
བརྗོད་པར་བྱ་བ་རྩོམ་པ་འདྲ་བ་རྣམས་ཞེས་སྤྱིར་སྨོས་པ་གང་ཡིན་པ་དེ་ལ་རིག་པ༌[^2842]ནི་འདུན་པ་དང་ཡོངས་སུ་དག་པ་དང་། འདུན་པ་དང༌[^2843]དགག་དབྱེ་དག་ཀྱང་བརྗོད་པ་ཡང༌[^2844]རིག་པར་བགྱིད་དོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་རྣམས་ཀྱིས་ནི་ཡུལ་གྱི་བྱེ་བྲག་ལ་བཅས་པ་ཞེས་བྱ་བ་དེ་ལྟ་བུར་གཞན་རྣམས་ལ་ཡང་འདིར་ཁོངས་སུ་བསྡུ་བའི་ཕྱིར་འདི་བསྟན་པ་ཡིན་ནོ། །

[Block 4099]
གཅིག་གིས་དུ་མའི་དེ་དག་ལེན་པ་ལ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི། མི་རུང་བ་ཞེས་བྱ་བར་སྦྱར་ཏེ། དགེ་སློང་གཅིག་གིས་དགེ་སློང་དུ་མའི་རྒྱུད་དུ་གཏོགས་པའི་འདུན་པ་དང་། དགག་དབྱེ་ལ་སོགས་པ་ལེན་པ༌[^2845]ཡང་མི་རུང་བ་མེད་དོ། །

[Block 4100]
འདི་ལ་བརྗོད་ནུས་པའི་ཚིག་གིས་གཟུང་ངོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་དགེ་སློང་དུ་མའི་རྒྱུད་དུ་གཏོགས་པའི་འདུན་པ་ལ་སོགས་པ༌[^2846]ལེན་པ་འདི་ལ་གྲངས་ཀྱི་བྱེ་བྲག་ཡོངས་སུ་ཆད་པ་མེད་དོ། །
--- END BLOCKS ---
