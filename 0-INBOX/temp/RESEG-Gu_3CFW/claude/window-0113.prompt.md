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
[Block 3956]
[^4066]དེ་བཞིན་དུ་རྗེས་སུ་གནང་བར་བྱ་བའམ་ཞེ་ན། དེའི་ཕྱིར་དྲི་བ་ཞེ་འགྲས་པ་མེད་པ་ཉིད་ངེས་པར་ཤེས་པར་བྱས་ཏེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དྲི་བ་གང་གིས་དེ་ལ་ཞེ་འགྲས་པ་མེད་ཅིང་དྲི་བ་དེ་ཤུགས་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 3957]
གནས་ཀྱི༌[^4067]ཡང་དག་པར་སྦྱོར་བའི་སྐབས་བཤད་ཟིན་ཏོ།། །།

[Block 3958]
ད་ནི་སྦ་བའི་རྣམ་པར་གཞག་པ་དང་ཡོངས་སུ་བསྐྱབ་པའི་སྐབས་བརྗོད་པར་བྱ་སྟེ། འཕྲེད་གཏན་དང་གནམ་གཟེར་དང་། འཁོར་གཏན་དང་སྒོ་ལྕགས་དང་ལྡེ་མིག་ཀྱོག་པོ་དག་གཙུག་ལག་ཁང་བསྡམས་པའི༌[^4068]ཕྱིར་ཡང་དག་པར་སྦྱར་རོ་ཞེས་བྱ་བ་ལ།

[Block 3959]
འདིར་གཞུང་ནི་སིལ༌[^4069]བུ་དག་ལས།

[Block 3960]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་དག་ལྔ་པོ་འདི་དག་ནི་སྡོམ་པར་བྱེད་པ་དག་ཡིན་ཏེ་ལྔ་གང་ཞེ་ན། འཕྲེད་གཏན་དང་གནམ་གཟེར༌[^4070]དང་འཁོར་གཏན་དང་སྒོ་ལྕགས་དང་ལྡེ་མིག་ཀྱོག་པོ༌[^4071]སྟེ། དེ་དག་གཙུག་ལག་ཁང་ན་བདོག་ན་དེ་དག་ཐམས་ཅད་དགེ་སྐོས་ཀྱིས་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་དང་། རྣམ་པར་འབྱེད་པ་ལས་ཀྱང་དགེ་འདུན་གྱི༌[^4072]གནས་བརྟན་དགེ་སློང་གིས་དགེ་སྐོས་ལ་ཚེ་དང་ལྡན་པ་ཁྱོད་ཀྱིས་སྒོ་བཅད་དམ། གཙུག་ལག་ཁང་སོ་སོར་བརྟགས་སམ་ཞེས་བྲི་བར་བྱའོ་ཞེས་གསུངས་པ་དང་མ་མོ་ལས་ཀྱང་། བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་རྣམས་ལ་གནས་མལ་བསྲུང་བའི་ཕྱིར་ལྡེ་མིག་འཁྱོག་པོ་རྗེས་སུ་གནང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3961]
དགེ་སྐོས་ཀྱིས་དགོངས་ཀར་གཙུག་ལག་ཁང་སོ་སོར་བསྡམས་ནས་སོ་སོར་བརྟག་པར༌[^4073]བྱའོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་བསྡམས་ནས་དགོངས་ཀར༌[^4074]སོ་སོར་བརྟག་པར་བྱ་སྟེ། གཙུག་ལག་ཁང་ཞེས་བྱ་བ་དང་སྦྱར་བར་བྱའོ། །

[Block 3962]
སྒོ་བསྡམས་ནས་དེའི་ཞེས་བྱ་བ༌[^4075]རིག་པར་བྱའོ། །

[Block 3963]
འཇིགས་པ་དང་བཅས་པ་ཉིད་ཡིན་ན་ཐུན་པ༌[^4076]ཉིད་ཀྱིས་མེལ་ཚེ་བྱའོ། །

[Block 3964]
དེར་གྱུར་པས་ཉལ་བ་དང་སྙོམས་པར་ཞུགས་པ་དག་སྤང་ངོ་ཞེས་བྱ་བ་ལ། དེར་གྱུར་པ་ཞེས་བྱ་བ་ནི་མེལ་ཚེའི་ཐུན་པར༌[^4077]གྱུར་པས་གནས་པའོ། །

[Block 3965]
དང་པོར་སྤང་བར་བྱ་བའི་སྒྲ་མི་བྱེད་པ་ངེས་པར་རྟོགས་པར༌[^4078]བྱའོ། །

[Block 3966]
གཞན་དུ་ན་ཡིད་རྟོན་པ་ལ་འཁུས་པར་འགྱུར་རོ། །

[Block 3967]
དེ་དག་ལ་འཁུ་བ་ཡོད་པ་ཞེས་བྱ་བ་འདིར་ངེས་པར་རྣམ་པར་གཞག་གོ། །

[Block 3968]
དེར་དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་དགེ་སྐོས་ལ་དམ་གཞག་བྱས་པ་ཉིད་དྲི་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་བསྡམས་པ་ལ་སོགས་པ་དེར་རོ། །

[Block 3969]
དམ་གཞག་བྱས་པ་ཉིད་ཅེས་བྱ་བ་ནི་བྱ་བ་དང་བྱེད་པ་ལ་ངེས་པར་སྦྱར་བ་དག་གོ། །

[Block 3970]
གལ་ཏེ་ཡང་དག་པར་སྦྱོར་བ་དག་གིས་མ་བསྡམས་པ་ཉིད་ན་གཙུག་ལག་ཁང་བརླག་ན་དགེ་སྐོས་འཇལ་དུ་གཞུག་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ཡང་དག་པར་སྦྱར་བ་ཞེས་བྱ་བ་ནི་འཕྲེད་གཏན་ལ་སོགས་པ་རྣམས་ཀྱིས་སོ། །

[Block 3971]
འཇལ་དུ་གཞུག་པར་བྱ་བ་ནི་བརླག་པའི་དངོས་པོ་དེའོ། །

[Block 3972]
དེ་དག་ཇི་ཙམ་ཉམས་པར་བྱས་པ་དེ་ཙམ་གྱི་ཆ་དག༌[^4079]གོ་ཞེས་བྱ་བ་ནི་བསྡམས་པའི་ཕྱིར་ཡང་དག་པར་སྦྱོར་བ་སུ་དག་ལས་གཅིག་གམ་དུ་མ་འམ་མང་པོས་བསྡམས་པ་མ་བསྒྲུབས་ཤིང་ཉམས་པར་བྱས༌[^4080]ན་ཡང་དག་པར་སྦྱོར་བ༌[^4081]དེ༌[^4082]དག་གི་ཆ་དག་དགེ་སྐོས་འཇལ་དུ་གཞུག་པར་བྱ་བ་ཉིད་ཡིན་ཏེ། གལ་ཏེ་གཅིག་གིས་མ་བསྡམས་ན་གཅིག་གི་ཆ་འཇལ་དུ་གཞུག་གོ། །

[Block 3973]
ཇི་དེ་གཉིས་ཀྱིས༌[^4083]མ་བསྡམས་ན་གཉིས་ཀྱི༌[^4084]ཆ་འཇལ་དུ་གཞུག་པའོ། །

[Block 3974]
ཇི་སྲིད་དུ་ལྔ་ཆར་གྱིས་མ་བསྡམས་ན་སྐྱིན་པ༌[^4085]རིལ་གྱིས་འཇལ་དུ་གཞུག་གོ། །

[Block 3975]
ལྡེ་མིག་འཁྱོག་པོ་དང་སྒོ་ལྕགས་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཀྱིས་སོ། །

[Block 3976]
སྡོམ་པ༌[^4086]ཇི་སྙེད་ཡོད་པ་དག་གིས་སྒོ་མ་བསྡམས་པར་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འཕྲེད༌[^4087]གཏན་ལ་སོགས་པར་སྡོམ༌[^4088]པར་བྱེད་པ་ཇི་སྙེད་ཡོད་པ་དེ་དག་ཐམས་ཅད་ཀྱིས༌[^4089]སྒོ་མ་བསྡམས་པར་གཞན་དུ་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3977]
གལ་ཏེ་གནས་སྟོང་པར་ཞུགས་པར་གྱུར་ན་དེར་ཆག་ཆག་ལ་སོགས་པ་བྱའོ་ཞེས་བྱ་བ་ནི་འདི་ནི་ཡོངས་སུ་བསྐྱང་བའི་རྣམ་པ་སྟེ་དེས་ན་འདིར་ནི་དེ༌[^4090]ཞུགས་པའོ། །

[Block 3978]
སྣོད་སྤྱད་ཙམ་པ་འཁོས༌[^4091]སུ་དབབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་ཇི་ལྟ་བ་བཞིན་དུ་བསྡུ་སྐྱོག་བྱ་ཞིང་འཁོས༌[^4092]སུ་དབབ་པར་བྱ་བའོ། །

[Block 3979]
གལ་ཏེ་དེ་བཟོད་ན་བྱི་དོར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་བཀྲུ་བཤལ་ལ་སོགས་པ་བྱི་དོར་བྱ་བ་དེ་བཟོད་ཅིང་འོས་པ་ཡིན་ན་བྱི་དོར་བྱ་སྟེ་འཁོས་སུ་དབབ་པར་བྱའོ། །

[Block 3980]
གལ་ཏེ་རུང་པར་བྱེད་པ་ཡོད་ན་སྔོ་སྲབ་པར་བྱེད་དུ་གཞུག་གོ། །

[Block 3981]
གལ་ཏེ་དེར་ཁྱིམ་པ་དག་ལྷགས༌[^4093]ན་དེ་དག་ལ་ཆོས་དང་ལྡན་པའི་གཏམ་དང་ནུས་པའི་ཆོས་གཞན་ཡང་བྱའོ་ཞེས་བྱ་བ་ལ། གཞན་ཡང་ཞེས་བྱ་བ་ནི་ཟས་སྐོམ་དང་དབྱར་གཟིགས༌[^4094]ལ་སོགས་པའོ། །

[Block 3982]
གནས་ཀྱི་གཞིའི་ནང་གི་སྐབས་བཤད་ཟིན་ཏོ།། །།

[Block 3983]
ད་ནི་ཕྱིའི་སྐབས་བརྗོད་པར་བྱ་སྟེ། ཤིང་ལྗོན་པ་བསྐྱེད་པ་མི་རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། འདིར་ཤིང་ལྗོན་པ་ཞེས་བྱ་བ་ནི་ནགས་མ་དང་གེལ་བ་དང་འཁྲི་ཤིང་དང་ཏཱ་ལ་ལ་སོགས་པ་དག་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 3984]
དེ་སྐྱེད༌[^4095]ནས་མི་བསྐྱང་བར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ན། ཤིང་ལྗོན་པ་བསྐྱེད་ནས་དུས་ཇི་སྲིད་དུ་བསྐྱང་བར་བྱ་ཞེ་ན་དེའི་ཕྱིར། དེའི་ཤིང་ལྗོན་པ་ནི་མེ་ཏོག་ཆགས་ཀྱི་བར་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མེ་ཏོག་གི་ཤིང་ལྗོན་པ་ནི༌[^4096]མེ་ཏོག་ཆགས་ཀྱི་བར་དུ་བསྐྱང་བར་བྱའོ། །

[Block 3985]
གཞན་ནི་འབྲས་བུའི་བར་དུའོ༌[^4097]ཞེས་བྱ་བ་ནི་འབྲས་བུའི་ཤིང་ལྗོན་པ་ནི་འབྲས་བུ་ཆགས་ཀྱི་བར་དུ་བསྐྱང་བར་བྱའོ། །

[Block 3986]
གང་ལ་མེ་ཏོག་དང་འབྲས་བུ་གཉིས་ཀ་ཡང་གྲུབ་པའི་ཤིང་ལྗོན་པ་དེ་ལ་ནི་གང་གི་དོན་དང་ལྡན་པ་ཉིད་དུ་ཆེས་གྲགས་པ་དེས་རྣམ་པར་གཞག་གོ། །

[Block 3987]
ཡུན་རིང་པ་ཉིད་ན་ལོ་ལྔར་རོ་ཞེས་བྱ་བ་ནི་མེ་ཏོག་དང་འབྲས་བུ་ཆགས་པ་དེ་གཉིས་ནི་ཡུན་རིང་བ་ཉིད་ལོ་ལྔར་བསྐྱང་བར་བྱའོ། །

[Block 3988]
འདི་ལ་དགེ་སློང་བསྐོས་པ་ནི་རང་ཉིད་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཤིང་ལྗོན་པ་བསྐྱེད་པ་བསྐྱང་བ་འདི་ལ་དགེ་སློང་གཞན་ལ་བཅོལ༌[^4098]ཞིང་བསྐོས་པ་ནི་རང་ཉིད་དང་འདྲ་སྟེ། དགེ་སློང་བསྐོས་པས་བསྐྱང་བར༌[^4099]བྱས་ན་རང་ཉིད་ཀྱིས༌[^4100]བསྐྱང་བ༌[^4101]བྱས་པ་དང་འདྲ་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3989]
འདིར་གཞུང་ནི་དགེ་སློང་ཀུན་དགའ་ར་བ་བསྐྱེད་པས་ལོ་ལྔ་གར་ཡང་འགྲོ་བར་མི་བྱའོ། །

[Block 3990]
གལ་ཏེ་འགྲོ་ན་དགེ་སློང་ལ་རྗེས་སུ་གཏད་དེ་འགྲོ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3991]
ཅི་དེ་དང་རྩེ་གཅིག་པ་ཉིད་ཀྱིས་བཅུ་པའི་བདག་ཉིད་ཀྱིས་བསྐྱང་བར་ཇི་ལྟར་བྱ་ཞེ་ན། དེའི་ཕྱིར། ལག་པ་དག་དང་རྐང་པ་དག་བཀྲུ་བ་དང་སོ་ཤིང་དོར་བ་དང་ལྷུང་བཟེད་བཀྲུ་བ་དང་ཁྲུས་བྱས་པ༌[^4102]ནི་བཅུ་པ་ཡིན་ནོ། །

[Block 3992]
གྲང་བ་སྐྱོབ་པའི་ཕྱིར་ཁང་བུའི་སྦུབས༌[^4103]བྱའོ། །

[Block 3993]
དབུགས་དབྱུང་བའི་ཕྱིར་དེ་ལ་སྐར་ཁུང་གདོད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལ་ཞེས་བྱ་བ་ནི་ཁང་བུའི་སྦུབས་དེ་ལའོ། །

[Block 3994]
གཡོགས་མས་དགབ་བོ་ཞེས་བྱ་བ་ནི་གྲང་བ་བསྐྱབ་པའི༌[^4104]ཕྱིར་ཁོ་ནར་ཁང་བུའི་སྦུབས་དེ་གཡོགས་པར་བྱ་བའོ། །

[Block 3995]
སོ་ག་མི་ཚ་བར་བྱ་བའི་ཕྱིར་བསལ༌[^4105]ལོ་ཞེས་བྱ་བ་ནི་སོ་ག༌[^4106]ཤིང་ལྗོན་པ་དེ་མི་ཚ་བར་བྱ་བའི་ཕྱིར་གཡོགས་མ་དེ་བསལ་བར་བྱ་བའོ། །
--- END BLOCKS ---
