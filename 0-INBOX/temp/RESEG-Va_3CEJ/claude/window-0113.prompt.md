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
སྟོབས་འཁོར་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་བརྡ་ཤེས་སོ། །

[Block 3957]
བརྡ་ཤེས་ཕྲག་བཅུ་ལ་ནི་བརྡ་ཤེས་ཆེན་པོའོ། །

[Block 3958]
བརྡ་ཤེས་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་རྣམ་འབྱུང་ངོ་། །རྣམ་འབྱུང་ཕྲག་བཅུ་ལ་ནི་རྣམ་འབྱུང་ཆེན་པོའོ། །

[Block 3959]
རྣམ་འབྱུང་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་སྟོབས་མིག་གོ། །

[Block 3960]
སྟོབས་མིག་ཕྲག་བཅུ་ལ་ནི་སྟོབས་མིག་ཆེན་པོའོ། །

[Block 3961]
སྟོབས་མིག་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་གྲངས་མེད་པ་སྟེ། བར་གྱི་གནས༌[^2235]བརྒྱད་ནི་མ་རྙེད་དོ། །

[Block 3962]
དེ་ལྟར་ན་གནས་གཞན་དྲུག་ཅུར་ཕྱིན་པ་དེ་དག་ཏུ་ཕྱིན་པའི་བསྐལ་པ་ནི། བསྐལ་པ་གྲངས་མེད་པ་ཞེས་བྱའོ། །

[Block 3963]
དེ་ནས་ཡང་བཟློག་ནས་བགྲང་སྟེ། དེ་ལྟར་ན་གྲངས་མེད་པ་གསུམ་ཞེས་བྱ་བའི་རྣམ་པ་ཐམས་ཅད་དུ་ཡོངས་སུ་བགྲང་བར་མི་ནུས་པས་ནི་མ་ཡིན་ནོ། །

[Block 3964]
འོ་ན་ཡང༌[^2236]བྱང་ཆུབ་སེམས་དཔའ་སྨོན་ལམ་བཏབ་པ་རྣམས་དུས་རིང་པོ་ཁོ་ནས་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འགྱུར་རམ་ཞེ་ན། ཅི་དེ་དེ༌[^2237]ལྟར་འགྱུར་རམ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས༌[^2238]ནི་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་དུ་དཀའ་བ་བརྒྱ་སྟོང་གིས་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཆེན་པོ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གིས་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འགྱུར་རོ། །

[Block 3965]
གལ་ཏེ་ཐར་པའི་གོ་སྐབས་གཞན་དེ་ལྟ་མ་ཡིན་པ་ཡང་ཡོད་ན་གོ། དེ་དག་ཅིའི་ཕྱིར་འབད་པ་འདི་སྙེད་ཅིག་རྩོམ་པར་བྱེད་ཅེ་ན། དེ་དག་ནི་ཇི་ལྟར་ན་གཞན་དག་ཀྱང་སྡུག་བསྔལ་གྱི་ཆུ་བོ་ཆེན་པོ་ལས་ཡོངས་སུ་བསྐྱབ་པར་ནུས་པར་འགྱུར་སྙམ་དུ་གཞན་གྱི་དོན་དུ་འབད་པ་རྩོམ་པར་བྱེད་དོ། །

[Block 3966]
འདི་དག་གི་གཞན་གྱི་དོན་གྱིས་བདག་གི་དོན་དུ་འགྱུར་བ་གང་ཡིན༌[^2239]ཞེ་ན། དེ་དག་གི་གཞན་གྱི་དོན་གང༌[^2240]ཡིན་པ་དེ་ཉིད་བདག་གི་དོན་ཏེ། [^2241]དེ་འདོད་པའི་ཕྱིར་རོ། །

[Block 3967]
ད་ནི་སུ་ཞིག་འདི་ལ་དད་པར་འགྱུར་ཞེ་ན། བདག་གསོ་བར་བྱེད་པའི་སྙིང་རྗེ་མེད་པ་རྣམས་ཀྱིས་འདི་ལ་དད་པར་དཀའ་བ་ནི་བདེན་ནོ། །

[Block 3968]
སྙིང་རྗེ་ཅན༌[^2242]རྣམས་ཀྱིས་དད་པར་བྱས་ཟིན་པ་ཡིན་ཏེ། དཔེར་ན་འདི་ན་སྙིང་རྗེ་མེད་པ་ལ་གོམས་པ་ཁ་ཅིག་རང་གི་དོན་མེད་བཞིན་དུ་ཡང་གཞན་ཉོན་མོངས་པ་ལ་མངོན་པར་དགའ་བ་དམིགས་པ་དེ་བཞིན་དུ་སྙིང་རྗེ་ལ་གོམས་པ་དག་རང་གི་དོན་མེད་བཞིན་དུ་ཡང་གཞན་ལ་ཕན་པར་བྱ་བ་ལ་མངོན་པར་དགའ་བ་ཡོད་དོ་སྙམ་དུ་ཡིད་ཆེས་པར་བྱའོ། །

[Block 3969]
ཡང་དཔེར་ན་འདུས་བྱས་ཀྱི་མཚན་ཉིད་མངོན་པར་མི་ཤེས་པ་དག་གོམས་པའི་དབང་གིས་འདུས་བྱས་བདག་མེད་པར་གྱུར་པ་དག་ལ་བདག་ཏུ་ཆགས་པ་བསྐྱེད་ནས་རྒྱུ་དེས་སྡུག་བསྔལ་དག་ཉམས་སུ་མྱོང་བར་འགྱུར་བ་དེ་བཞིན་དུ་གོམས་པའི་དབང་གིས་དེ་དག་ལས་བདག་ཏུ་ཆགས་པ་བཟློག་ནས། གཞན་དག་ལ་ལྟ་བ་བསྐྱེད་དེ། རྒྱུ་དེས་སྡུག་བསྔལ་དག་མྱོང་བར་འགྱུར་རོ་སྙམ་དུ་ཡིད་ཆེས་པར་བྱའོ། །

[Block 3970]
གང་གཞན་དག་གི་སྡུག་བསྔལ་གྱིས་སྡུག་བསྔལ་བར་འགྱུར་ཞིང་། གཞན་དག་གི་བདེ་བས་བདེ་བར་འགྱུར་གྱི། བདག་ཉིད་ཀྱི་ནི་མ་ཡིན་པ་དེ་ལྟ་བུའི་རིགས་གཞན་ཁོ་ན་ཡང་འགྲུབ་སྟེ། དེ་ལྟ་ནི་རང་གི་དོན་དུ་མི་བལྟའོ། །

[Block 3971]
འདིར་སྨྲས་པ། དམན་པ་དེ་དང་དེའི་ཐབས་ཀྱིས་རང་གི་རྒྱུད་དུ་གཏོགས་པའི་བདེ་བ་དོན་དུ་གཉེར། འབྲིང་པོ་སྡུག་བསྔལ་ལྡོག་པ་ཁོ་ནའོ། །

[Block 3972]
བདེ་མིན་གང་ཕྱིར་དེ་ནི་སྡུག་བསྔལ་གནས་ཡིན་ཕྱིར། །དམ་པ་རང་གི་རྒྱུད་ལ་ཡོད་པའི་སྡུག་བསྔལ་རྣམས་ཀྱིས་གཞན་དག་ལ་ནི་བདེ་བ་དང་། །སྡུག་བསྔལ༌[^2243]གཏན་ལྡོག་ཁོ་ན་དོན་གཉེར་གང་ཕྱིར་དེ་ཡི་སྡུག་བསྔལ་གྱིས་དེ་སྡུག་བསྔལ་ཕྱིར། །

[Block 3973 [HEADING]]
##### སངས་རྒྱས་འབྱུང་བ། ^3-2-5-6-0

[Block 3974]
ཡང་ཅི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཡར་སྐྱེ་བའི་ཚེ་འབྱུང་ངམ། འོན་ཏེ་མར་འགྲིབ་པའི་ཚེ་འབྱུང་ཞེ་ན། མར་ནི་འགྲིབ་པ་ཡི། བརྒྱ་ཡི་བར་ལ་དེ་དག་འབྱུང་། །སྐྱེ་དགུ་རྣམས་ཀྱི་ཚེ་ལོ་བརྒྱད་ཁྲི་བ༌[^2244]མར་འགྲིབ་པ་ནས་བརྩམས་པ་ནས་མི་རྣམས་ཀྱི་ཚེ་ལོ་བརྒྱ་པ་ཡིན་པའི་བར་འདིར་སངས་རྒྱས་རྣམས་འབྱུང་བར་འགྱུར་རོ། །

[Block 3975]
ཅིའི་ཕྱིར་ཡང་སྐྱེ་བའི་དུས་སུ་ནི་མ་ཡིན་ཞེ་ན། དེའི་ཚེ་སེམས་ཅན་རྣམས་སྐྱོ་བར་དཀའ་བའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་བརྒྱ་ལས་མར་འགྲིབ་པའི་ཚེ་མ་ཡིན་ཞེ་ན། དེའི་ཚེ་སྙིགས་མ་ལྔ་པོ་འདི་ལྟ་སྟེ། ཚེའི་སྙིགས་མ་དང་། དུས་ཀྱི་སྙིགས་མ་དང་། ཉོན་མོངས་པའི་སྙིགས་མ་དང་། ལྟ་བའི་སྙིགས་མ་དང་། སེམས་ཅན་གྱི་སྙིགས་མ་ཤིན་ཏུ་ལྷག་པ་ཡིན་ཏེ། མར་འགྲིབ་པའི་འོག་ཏུ་ནི་ཚེ་ལ་སོགས་པ་ཐ་ཆད་ཡིན་ནོ། །

[Block 3976]
ངན་སྙིགས་སུ་གྱུར་པའི༌[^2245]ཕྱིར་སྙིགས་མ་དག་ཅེས་བྱའོ། །

[Block 3977]
གཉིས་ཀྱིས་ནི་གོ་རིམས་བཞིན་དུ་སྲོག་དང་ཡོ་བྱད་རྒུད་པར་བྱེད་དོ། །

[Block 3978]
གཉིས་ཀྱིས་ནི་འདོད་པའི་བསོད་ཉམས་དང་བདག་ངལ་བ་ལ་སོགས༌[^2246]པའམ། ཡང་ན་ཁྱིམ་པའམ༌[^2247]རབ་ཏུ་བྱུང་བའི་ཕྱོགས་ཀྱི་དབང་དུ་བྱས་ནས་དགེ་བའི་ཕྱོགས་རྒུད་པར་བྱེད་དོ། །

[Block 3979]
གཅིག་གིས་ནི་ལུས་རྒུད་པར་བྱེད་དོ། །

[Block 3980]
[^2248]བོང་ཚོད་དང་། གཟུགས་དང་། ནད་མེད་པ༌[^2249]དང་། སྟོབས་དང་། བློ་དང་། དྲན་པ་དང་། བརྩོན་འགྲུས་དང་། བརྟན་པ་ཉམས་པའི་ཕྱིར་རོ། །

[Block 3981 [HEADING]]
##### རང་སངས་རྒྱས། ^3-2-5-7-0

[Block 3982]
ཡང་རང་སངས་རྒྱས་རྣམས་དུས་གང་དུ་འབྱུང་ཞེ་ན། རང་སངས་རྒྱས་རྣམས་གཉི་ག་ལ། ཡར་སྐྱེ་བ་ལ་ཡང་འབྱུང་། མར་འགྲིབ་པ་ན༌[^2250]ཡང་འབྱུང་ངོ་། །རང་སངས་རྒྱས་རྣམས་ནི་རྣམ་པ་གཉིས་ཏེ། ཚོགས་ཤིང་སྤྱོད་པ་རྣམས་དང་། བསེ་རུ་ལྟ་བུ་རྣམས་སོ། །

[Block 3983 [HEADING]]
###### ཚོགས་ཤིང་སྤྱོད་པ། ^3-2-5-7-1-0

[Block 3984]
དེ་ལ་ཚོགས་ཤིང་སྤྱོད་པ་རྣམས་ནི་ཉན་ཐོས་ཀྱི་རིགས་སུ་གྱུར་པ་སྔོན་དུ་འགྲོ་བའི་རང་རྒྱལ་བ་རྣམས་ཞེས་བྱའོ། །

[Block 3985]
གཞན་དག་ན་རེ་སོ་སོའི་སྐྱེ་བོ་སྔོན་དུ་འགྲོ་བ་དག་ཀྱང་ཡོད་དེ། གང་དག་གཞན་དུ་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་བསྐྱེད་པ་ཚེ་འདི་ལ་བདག་ཉིད་ཀྱིས་ལམ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱའོ་ཞེས་ཟེར་ཞིང་། འདི་སྐད་དུ་རེ་ཞིག་རི་ལ་དཀའ་ཐུབ་ཅན་ལྔ་བརྒྱ་ཞིག་དཀའ་ཐུབ་དྲག་པོ་དག་གིས་གདུང་བར་བྱས་པ་ན་རང་སངས་རྒྱས་དང་ལྷན་ཅིག་གནས་གནས་པའི་སྤྲེའུ་ཞིག་དང་ཕྲད་ནས་དེའི་སྤྱོད་ལམ་བསྟན་པས་རང་སངས་རྒྱས་ཀྱི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ཀྱི༌[^2251]བར་དུ་གྲག་གོ་ཞེས་སྔོན་གྱི་གཏམ་འདོན་པར་བྱེད་དོ།[^2252] །འཕགས་པ་དག་ཅིག་ཡིན་ན་ནི་དཀའ་ཐུབ་དྲག་པོ་དག་གིས་གདུང་བར་མི་འགྱུར་རོ་ཞེའོ། །

[Block 3986 [HEADING]]
###### བསེ་རུ་ལྟ་བུ། ^3-2-5-7-2-0

[Block 3987]
བསེ་རུ་ལྟ་བུ་རྣམས་ནི་རེ་རེ་གནས་པ་དག་ཡིན་ནོ། །

[Block 3988]
རང་སངས་རྒྱས་དེ་དག་ལས།

[Block 3989]
བསེ་རུ་བསྐལ་པ་བརྒྱའི་རྒྱུས་བསྐལ་པ་ཆེན་པོ་བརྒྱར་བྱང་ཆུབ་ཀྱི་ཚོགས་དག་ལ་སྤྱོད་པས་བསེ་རུ་ལྟ་བུར་འགྱུར་རོ། །

[Block 3990]
ལུང་མེད་པར་བདག་གཅིག་པུའི་ཕྱིར་སངས་རྒྱས་པས་རང་སངས་རྒྱས་དག་སྟེ། དེ་དག༌[^2253]ནི་བདག་ཉིད་འདུལ་བར་བྱེད་ཀྱི་གཞན་དག་ནི་མ་ཡིན་ནོ། །

[Block 3991]
འདི་ལ་རྒྱུ་ཅི་ཞིག་ཡོད། རེ་ཞིག་སོ་སོ་ཡང་དག་པར་རིག་པ་ཐོབ་པའི་ཕྱིར་ཆོས་སྟོན་པར་མི་སྤྱོད་པ་ཡང་མ་ཡིན་ལ། དེ་དག་གིས་སྔོན་གྱི་སངས་རྒྱས་རྣམས་ཀྱི་བསྟན་པ་རྗེས་སུ་དྲན་ནས་ཡང་ཆོས་སྟོན་པར་སྤྱོད་དོ། །

[Block 3992]
ཐུགས་རྗེ་མེད་པར༌[^2254]ཡང་མ་ཡིན་ཏེ། སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་གདགས་པའི་དོན་དུ་རྫུ་འཕྲུལ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 3993]
སེམས་ཅན་རྣམས་སྐལ་བ་དང་མི་ལྡན་པའི་ཕྱིར་ཡང་མ་ཡིན་ཏེ། འདི་ལྟར་འཇིག་རྟེན་པའི་ལམ་གྱིས་འདོད་ཆགས་དང་བྲལ་བ་དག་ཀྱང་ཡོད་དོ། །

[Block 3994]
འོ་ན་ཇི་ལྟ་ཞེ་ན། སྔོན་གོམས་པའི་དབང་གིས་བསོད་སྙོམས༌[^2255]ལ་མོས་པའི་ཕྱིར་སེམས་ཅན་རྣམས་ཆོས་ཟབ་མོ་འཛིན་དུ་འཇུག་པའི་དོན་དུ་བྱེད་པར་མི་སྤྲོ་སྟེ། སྐྱེ་དགུ་རྒྱུན་ཕྱོགས་སུ་འགྲོ་བ་རྣམས་ནི་རྒྱུན་ཕྱོགས་ལས་བཟློག་པར་བཀྲི་བར་དཀའོ། །

[Block 3995]
རྣམ་པར་གཡེང་བ་དང་འདུ་འཛིས་སྐྲག་པས་འཁོར་ཡོངས་སུ་གཟུང་བར༌[^2256]འགྱུར་བ་སྤང་བའི༌[^2257]ཕྱིར་རོ། །
--- END BLOCKS ---
