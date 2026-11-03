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
[Block 5216]
གཞན་ལ་ཕན་པ་མ་ཡིན་པས་མི་བཟོད་པར་བྱེད་པ་སྟེ། གཞན་མི་འདོད་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 5217]
བདག་ལ་ཡང་སྐྱེ་བ་གཞན་ལ་ཕན་པར་འགྱུར་བ་མེད་ཅིང་། རབ་ཏུ་སྡིག་པར་བྱེད་དེ། བདག་དང་གཞན་གྱི་ངན་སོང་གི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 5218]
དེ་དག་གིས་ཞེས་བྱ་བ་ནི་ཡིད་ལ༌[^3345]ཞེ་སྡང་ཡོད་པའོ། །

[Block 5219]
སྡིག་ལ་འཛེམ་པ་ནི་མི་འདོད་པའི་འབྲས་བུ་ལ་འཇིགས་པས་སོ། །

[Block 5220]
གཉེན་པོ་རྣམས་ལ༌[^3346]བརྟེན་ནས་ཞེས་བྱ་བ་ནི། བཟོད་པ་ལ་བརྟེན་པའོ། །

[Block 5221]
ཡིད་ལ་ཞེ་སྡང་ཡོད་པའི་གཉེན་པོ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། དགོན་པའི་མེ་ནི་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5222]
མ་དང་འདྲ་བ་ནི་ཡིད་ལ་ཞེ་སྡང་ཡོད་པ་སྟེ། བདག་དང་གཞན་ལ་གནོད་ཅིང་སྲེག་པའི་ཕྱིར་རོ། །

[Block 5223]
ཆུ་ཀླུང་ཆེན་པོ་དང་འདྲ་བ་ནི་བཟོད་པ་སྟེ། ཡིད་ལ་ཡོད་པའི་ཞེ་སྡང་གི་མེ་རབ་ཏུ་ཞི་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 5224]
བཟོད་པ་བསྟེན་ན་ཞི་བར་འགྱུར། །ཞེས་བྱ་བ་ལ། ཇི་ལྟར་བཟོད་པ་བསྟེན་ན་ཞི་བར་འགྱུར་བ་ཉིད་བསྟན་པའི་ཕྱིར། དེ་བས་དེའི་རྒྱུ་ཟིལ་གྱིས་མནན་པས་བཟོད་པ་སྡིག་པ་སྤོང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། སྡིག་པ་ཞེས་བྱ་བ་ནི་མི་དགེ་བའི་ལས་སོ། །

[Block 5225]
དེའི་རྒྱུ་ཟིལ་གྱིས་མནན་པས་ཞེས་བྱ་བ་ནི་སྡིག་པ་དེའི་རྒྱུ་སྟེ། དེའི་རྒྱུ་ནི་ཡིད་ལ་ཞེ་སྡང་ཡོད་པའོ། །

[Block 5226]
དེ་ཟིལ་གྱིས་མནན་པ༌[^3347]ནི་དེའི་གཉེན་པོ་བཟོད་བ་ལ་བརྟེན་པས༌[^3348]སོ། །

[Block 5227]
དེའི་ཕྱིར་ཞེས་བྱ་བས་ནི་སྡིག་པ་ཡོངས་སུ་སྤངས་པས་སོ། །

[Block 5228]
དགྲ་ཡང་འཕེལ་མི་འགྱུར་ཞེས༌[^3349]བྱ་བ་ནི་སྔར་སྐྱེས་པ་ཞི་བར་བྱེད་པ་དང་། སྔར་མ་སྐྱེས་པ་ཡིད་ལ་གནས་པའི་མི་དགེ་བ་ལ་འཇུག་པ་མེད་པ་སྟེ། མི་དགེ་བའི་བདག་ཉིད་གནོད་པ་ཉིད་དོ། །

[Block 5229]
འགའ་ཞིག་ཅེས་བྱ་བ་ནི་དགྲ་སྟེ། མི་མཐུན་པའི་ཕྱོགས་མགུ་བ༌[^3350]བསྐྱེད་པ་སྟེ། བདག་ཉིད་ལ་ཡིད་ཀྱིས་སོ། །

[Block 5230]
མཆོད་པར་འོས་པ་ནི་ལུས་དང་། ངག་གི་ལས་ཀྱིས་མཆོད་པ་ཐོབ་པར་བསྟན་ཏོ། །

[Block 5231]
བདེ་བའི་སྐལ་བ་དང་ལྡན་པར་འགྱུར་ཞེས་བྱ་བ་ནི། མཐོང་བའི་ཆོས་ཀྱི་གཞན་དང༌[^3351]འབྲེལ་པའི་བདེ་བ་སྟེ། མཆོད་པ་དང་། དགའ་བ་གཉིས་ཀྱིས་བདེ་བའི་སྐལ་བ་དང་ལྡན་པར་འགྱུར་བའོ། །

[Block 5232]
མཐོ་རིས༌[^3352]འགྲོ་བར་འགྱུར་ཞེས་བྱ་བ་ནི། འཇིག་རྟེན་ཕ་རོལ་དུ་བདེ་བ་འཐོབ་པ་ཡིན་ཏེ། དེ་བས་ན་སྐྱོན་འདི་མེད་པ་ཡིན་པས། བཟོད་པ་བསྟེན་ན་དེ་དག་གི༌[^3353]མཐུ་ཉིད་དུ་འགྱུར་རོ། །

[Block 5233]
གཞན་ཡང་ཀྱེ་བཙུན་མོ་ཞེས་བྱ་བ་ནི་བཟོད་པའི་རྣམ་པ་གཞན་བསྟན་པའི་ཕྱིར། དགེ་བའི་རང་བཞིན་ཅན་དུ༌[^3354]རབ་ཏུ་གྲགས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ལྔ་སྨོས་ཏེ། དེ་ལ་དགེ་བའི་རང་བཞིན་ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི་བཟོད་པའི་འབྲས་བུའི་རང་བཞིན་གྱི་གཉེན་པོ་དང་རྗེས་སུ་མཐུན་པའི་ཡོན་ཏན་གྱི༌[^3355]དབང་དུ་བྱས་པ་སྟེ། དགེ་བ་ཞེས་བྱ་བ་ལ་དགེ་བའི་རང་བཞིན་ནི༌[^3356]ཇི་ལྟ་བུ་ཡིན། ཇི་ལྟར་མ་ཆགས་པ་དང་། ཞེ་སྡང་མེད་པ་དང་། གཏི་མུག་མེད་པ་ཡིན་ནམ། འོན་ཏེ་མཚུངས་པར་ལྡན་པ་སྟེ། ཇི་ལྟར་ཚོར་བ་ལ་སོགས་པ་ཐམས་ཅད་དུ་འགྲོ་བ་རྣམས་དང་བཅས་པ་ཡིན་ནམ། འོན་ཏེ༌[^3357]ཀུན་ནས་བསླང་བ་སྟེ། ཇི་ལྟར་ལས་རྣམས་དང་བཅས་པ་ཡིན་ནམ། འོན་ཏེ་དོན་དམ་པའི་ཆོས་ཏེ། ཇི་ལྟར་མྱ་ངན་ལས་འདས་པ་ཡིན་ནམ་སྙམ་ན། ཇི་ལྟར་རང་བཞིན་གྱི་དགེ་བ་སྟེ། ཞེ་སྡང་མེད་པའི་མཚན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 5234]
རང་བཞིན་ཡང་ཡིན་ལ་ཁྱད་པར་ཡང་ཡིན་པས་རང་བཞིན་ཁྱད་པར་ཅན་ནོ། །

[Block 5235]
དེའི་རབ་ཏུ་གྲགས་པ་ནི་རབ་ཏུ་གྲགས་བ་ཁྱད་པར་ཅན་ནོ། །

[Block 5236]
འདིས་ནི་རང་བཞིན་གྱི་དགེ་བ་ཉིད་དུ་བསྟན་ཏེ། འདི་ནི་རེ་ཞིག་རང་བཞིན་གྱི་བཟོད་པ་ཡིན་ནོ། །

[Block 5237]
བསོད་ནམས་གྲགས་པ་དག་ཀྱང་རབ་ཏུ་འཕེལ། །ཞེས་བྱ་བ་བསོད་ནམས་རབ་ཏུ་འཕེལ་བ་ནི། འཇིག་རྟེན་ཕ་རོལ་དུ་འབྲས་བུ་བདེ་འགྲོར་འགྲོ་བའོ། །

[Block 5238 [VERSE]]
གྲགས་པ་རབ་ཏུ་འཕེལ་བ་ནི། །
མཐོང་བའི་ཆོས་ཀྱི་འབྲས་བུའོ། །

[Block 5239]
ཆུ་ཡིས་མ་བཀྲུས་པར་ཡང་དག་པར་འགྱུར། །ཞེས་བྱ་བ་འདིས་ནི།

[Block 5240 [VERSE]]
མི་དགེ་བ་ཐམས་ཅད་ཀྱི་གཉེན་པོ་ཉིད་དོ། །
ཡོན་ཏན་དེ་དང་དེ་དག་ཕུན་སུམ་ཚོགས། །

[Block 5241]
ཞེས་བྱ་བ་འདིས་ནི་ཡོན་ཏན་ཐམས་ཅད་དང་རྗེས་སུ་མཐུན་པ་ཉིད་དོ།[^3358] །དགེ་བའི་རང་བཞིན་ཅན༌[^3359]དུ་རབ་ཏུ་གྲགས། །ཞེས་བྱ་བ་བསྟན་པ་ལ་དགེ་བའི་རང་བཞིན་ཉིད་དུ་བསྟན་པར་འདོད་པའི་ཕྱིར། གཞན་ལ་གནོད་པ་རྟག་ཏུ་ཡོང་མི་ཤེས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5242]
ཆོས་ཉིད་ཅེས་བྱ་བ་ནི་རྟག་པའོ། །

[Block 5243]
ཡང་ན་ཆོས་ཉིད་ཀྱི་མཚན་ཉིད་ཇི་ལྟ་བུ་ཉིད་ཡིན་པ་དེ་ཉིད་བསྟན་པའི་ཕྱིར་སྨྲས་པ། གཞན་དག་ལ་ཉེ་བར་གནོད་པ་ནི༌[^3360]གནོད་པ་སྟེ། སྲོག་གཅོད་པ་ལ་སོགས་པ་མི་དགེ་བ་བཅུའི་ལས་ལ་མི་འཇུག་པའི་མཚན་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 5244]
གང་དག་གི་ཆོས་ཉིད་ཡིན་ཞེ་ན། སྙིང་སྟོབས་ཅན་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིའོ། །

[Block 5245]
ཆོས་ཉིད་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན། ཡིད་དུ་འོང་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 5246]
དེའི་མིང་ཇི་སྐད་དུ་བཏགས་ཤེ་ན། བཟོད་པ་ཞེས་བྱ་བའི་མིང་ཡིན་ཏེ། དེའི་མིང་ཡོན་ཏན་དང་ལྡན་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་སྨྲས་པ། ཡོན་ཏན་གྱིས་མངོན་པར་བསྒྲུབས་པ༌[^3361]ཉིད་དུ་མཛེས་པའི་མིང་གང་ཡིན་པ་དེ་ནི་ཡོན་ཏན་མངོན་བསྒྲུབས༌[^3362]བཟོད་པ་སྟེ། མཛེས་པའི་མིང་བདག་དང་། གཞན་གཉི་ག་ལ་མཛེས་པའི་ཕྱིར་བཟོད་པའོ། །

[Block 5247]
འཇིག་རྟེན་གྱི་དོན་བྱེད་པ་ནི། འཇིག་རྟེན་ལ་ཕན་པར་བྱེད་པ་སྟེ། འདིས་ནི་གཞན་ལ་ཕན་པའི་རྒྱུ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5248]
སྙིང་རྗེས་བཀའ་སྩལ་ཅེས་བྱ་བ་ནི། སྙིང་རྗེ་ཅན་གྱི་བཀའ་ཡིན་པས་སྙིང་རྗེས་བཀའ་སྩལ་པའོ། །

[Block 5249]
འདོད་ཆགས་མེད་པའི་རང་བཞིན་དང་། འདོད་ཆགས་མེད་པའི་མཚན་ཉིད་བཟོད་པ་གཞན་གྱི་དོན་བྱེད་པར་འཇུག་པ་ཡིན་ཏེ། དེ་ལྟར་བཟོད་པའི་རྒྱུ་བསྟན་ཏོ། །

[Block 5250]
བསོད་ནམས་གྲགས་པ་དག་ཀྱང་རབ་ཏུ་འཕེལ། །ཞེས་བྱ་བ་དེའི་དོན་རྗེས་སུ་བསྟན་པ་ནི་མ་བཤད་དེ། དེ་བས་དེའི་རྒྱུ་ཟིལ་གྱིས་མནན་པས་བཟོད་པས་སྡིག་པ་སྤོང་བ༌[^3363]ཞེས་བྱ་བའི་ཚིགས་བཅད་དེར་བསྟན་ཟིན་པའི་ཕྱིར་རོ། །

[Block 5251 [VERSE]]
ཆུ་ཡིས་མ་བཀྲུས་པར་ཡང་དག་པར་འགྱུར། །
ཞེས་བྱ་བ་འདིའི༌[^3364]རྗེས་སུ་བསྟན་པ་ནི།
མཐུ་དང་ལྡན་པ་རྣམས་ཀྱི་རྒྱན་ཡང་ཡིན། །

[Block 5252]
ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས༌[^3365]བསྟན་ཏེ། [^3366]གང་དག་འདི་རྣམ་པར་དག་པར་བྱེད་པ་ཡིན་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར་ཚིགས་བཅད་འདི་སྨོས་ཏེ། ཁྱིམ་པ་དང་། རབ་ཏུ་བྱུང་བ་རྣམས་ཀྱིའོ། །

[Block 5253]
ཁྱིམ་པ་རྣམས་ཀྱི་ནི། [^3367]མཐུ་དང་ལྡན་པ་རྣམས་ཀྱི་རྒྱན་ཡང་ཡིན། །ཞེས་བྱ་བ་ཡིན་ཏེ། གནོད་སེམས་ཀྱིས༌[^3368]དགོན་པའི་མེ་ལ་ཆུ་རྒྱུན་འབེབས་པའོ། །

[Block 5254]
དཀའ་ཐུབ་ཅན་གྱི་སྟོབས་མཆོག་ཕུན་སུམ་ཚོགས་པ་ཡོད་ན་ནི། གནོད་སེམས་དགོན་པའི་མེ་ལ་ཆུའི་རྒྱུན༌[^3369]འབེབས་པ་ཡིན་ཏེ། གནོད་སེམས་ཀྱི་དགོན་པའི་མེ་ལ་ཆུའི་རྒྱུན་འབེབས་ཞེས་བྱ་བ་ཡིན་ཏེ། གནོད་སེམས་ཀྱི་དགོན་པའི་མེ་ལ་ཆུའི་རྒྱུན་དང་འདྲ་བར་དེ་ཉེ་བར་ཞི་བ་སྟེ། དེ་བས་ན་གནོད་སེམས་དགོན་པའི་མེ་ལ་ཆུ་རྒྱུན་འབེབས་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 5255]
དེའི་ཕྱིར། གཉི་གའི་ཚེ་ལ་དོན་མེད་ཞི་བར་བྱེད། །ཅེས་བྱ་བ་སྨོས་ཏེ། དེ་བས་ན་ཆུ་ཡིས་མ་བཀྲུས་པར་ཡང་དག་པར་བྱེད་དེ། དོན་མེད་པར་ཉེ་བར་ཞི་བར་བྱེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
