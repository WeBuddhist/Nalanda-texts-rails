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
[Block 4341]
རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་མ་རྫོགས་པ་ལ་ཡང་ཆོ་ག་འདི་རྣམ་པར་གཞག་པའོ། །

[Block 4342]
གང་ཡང་རུང་བས་སོ་ཞེས་བྱ་བ་ནི་གསར་བུ་དང་། མཚན་མི་མཐུན་པ་དང་། རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་མ༌[^3017]རྫོགས་པ་དག་གིས་ཀྱང་བྱར་རུང་སྟེ། རྒན་པོ་འབའ་ཞིག་གིས་ནི་བྱ་བར་མ་ཟད་དེ་བསྙེན་པར༌[^3018]རྫོགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4343]
དེ་དག་གི་ནང་ན་ཆོས་སྟོན་པ་དུ་མ་ཡོད་དུ་ཟིན་ཀྱང་གང་ལ་སྟོན་པར་བྱེད་པ་ཐམས་ཅད་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4344]
མ་གསོལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བསྟན་པར་མི་བྱའོ། །

[Block 4345]
གལ་ཏེ་དེའི་ཚེ༌[^3019]ཚིག་གིས་བྱུང་བ་མ་ཡིན་ནའོ་ཞེས་བྱ་བ་ནི། གང་གི་ཚིག་གིས་དགེ་འདུན་སྤྱན་དྲངས་པ་ལ་སོགས་པ་མ༌[^3020]གསོལ་བར་ཡང་ཆོས་བསྟན་པར་བྱ་སྟེ། སྟོན་པ་དེ༌[^3021]བཞིན་དུ་འདིར་འདི་འབྱུང་བ་ཡིན་ཏེ། འདི་ལྟར་མདུན་གྱིས༌[^3022]བལྟས་པར་གྱུར་པས་མདུན་གྱིས་བལྟས་པ་ཉིད་དེ་དགེ་སློང་དེ་རྣམས་དང་མཐུན་པ་ཉིད་དོ། །

[Block 4346]
འདིར་འབྱུང་བ་ནི་དཔེ་ཙམ་ཡིན་ཏེ། ཐམས་ཅད་དུ་དེའི་སྒོ་ནས་གནས་པ་ལ་ཆོག་འདི་ཡིན་ནོ། །

[Block 4347]
གནས་སྐབས་ཐམས་ཅད་ལ་ཡང་དགེ་འདུན་གྱི་གནས་བརྟན་གྱི་ཚིག་ལས་གྱུར་པ་ཉིད་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 4348]
གནས་པ་ལ་ནི་གནས་ཀྱིའོ། །

[Block 4349]
ཉེ་གནས་རྣམས་ལ་ནི་ཀློག་པའི་སློབ་དཔོན་གྱིའོ། །

[Block 4350]
དགེ་སློང་མ་རྣམས་ལ་དགེ་སློང༌[^3023]རྣམས་ཀྱིའོ། །

[Block 4351]
བསྙེན་པར་མ་རྫོགས་ཤིང་རབ་ཏུ་བྱུང་བ་རྣམས་ལ་ནི་བསྙེན་པར་རྫོགས་པ་ལ༌[^3024]སྟེ་གནས་སུ་གྱུར་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4352]
གསར་བུ་ལ་ཁ་ཟས་ཀྱི་མདུན་དུ་ཡོན་བཤད་པའི་དོན་དུ་ཁྲིའི་དྲུང་དུ་དེ་ནི་མ་གསོལ་བར་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 4353]
གྲྭས༌[^3025]མི་བྱའོ་ཞེས་བྱ་བ༌[^3026]ནི་གྲལ་བཅིངས་པའི་དབྱིབས་དང་ལང་ལོང་ཁྱད་པར་ཅན་མ་ཡིན་པར་གྱུར་པས་འཁོར་ལྷག་མའོ། །

[Block 4354]
འདིར་དེའི་མཐར་ཐུག་པ་ཡིན་ཏེ། འདི་ནི་དབྱིབས་སུ་འབྱིན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ནི་གྲྭ༌[^3027]ཕྱེད་ཀྱིས་མི་ཕྱེའོ་ཞེས་བྱ་བ་དེ་ལས་ཤེས་པར་བྱའོ། །

[Block 4355]
ཆོས་ཉན་པའི་གྲལ་གྱི་རྣམ་པ་ཁྱམས་སུ་ཟླ་ཁམ་གྱི་རྣམ་པ་ལྟ་བུ་འདི་རྗེས་སུ་གནང་བས། དེའི་ཕྱིར་ལང་ལོང་འདི་བཀག་པ་ཡིན་ཏེ། དགེ་སློང་དག་ལང་ལོང་དག་གིས་ཆོས་སྟོན་པར་བྱེད་པ་ན།[^3028] ཅ་ཅོར་གྱུར་པའི་ཕྱིར་རོ་ཞེས་གླེང་གཞི་ལས་གསུངས་པ་ཡིན་ནོ། །

[Block 4356]
འདི་ལས་ཀྱང་དེ་ནི་འདིར་མཐར་ཐུག་པ་ཞེས་བྱ་བར་གཏོགས་པའོ། །

[Block 4357]
གྲྭ་ཕྱེད༌[^3029]ཀྱིས་མི་བྱའོ་ཞེས་བྱ་བ་ལ།

[Block 4358]
འདིར་དེ་གཉིས་ཀྱི་གཞུང་ནི་མ་མོ་ལས།

[Block 4359]
གང་སྨྲ་བར་མི་བྱ་བ་གྲྭ༌[^3030]ཕྱེད་ཀྱིས་སྨྲ་བར་མི་བྱ་སྟེ། གང་ཞིག་སྨྲ་ན་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4360]
གཉིས་ཀྱིས་གཅིག་ཏུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི། གྲྭ༌[^3031]ཡང་རུང་གྲྭ༌[^3032]ཕྱེད་ཀྱང་རུང་འདི་ནི་སྤོངས་པ༌[^3033]ཡིན་ནོ། །

[Block 4361]
གལ་ཏེ་དུ་མ་ཉིད་དམ་གཅིག་ལ་ཞེས་བྱ་བ་འདི་ལ་འདིར་གཞུང་ནི། གཉིས་ཀྱིས་གྲྭ༌[^3034]གཅིག་ཏུ་སྨྲ་བར་མི་བྱའོ། །

[Block 4362]
གང་སྨྲ་བར་བྱེད་པ་དེ་ལ་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4363]
རྒན་རིམས་ཀྱིས༌[^3035]སོ་ཞེས་བྱ་བ་འདི་ལ་ཡང་། སྔར་གལ་ཏེ་དུ་མ་ཉིད་ཡིན་ན་གཅིག་གིས་སོ་ཞེས་སྨོས་པས་དེའི་རྗེས་སུ་སྦྱར་གྱི་བསྟན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལོག་གོ། །

[Block 4364]
དུ་མ༌[^3036]ཉིད་ལ་གནས་པས་རྒན་རིམས་ཀྱིས༌[^3037]བསྟན་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4365]
གལ་ཏེ་མང་བ་ཉིད་ཡིན་ན་སྟན་གཉིས་སམ་གསུམ་གཞག་སྟེའོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་རང་གི་འཁོར་མང་བ་ཉིད་དུ་གྱུར་ན་དེ་དག་གི་གོ་གཉིས་སམ་གསུམ་གོང་དུ་གཞག་ནས། དེས་རབས་དང་ཉེ་བར་གནས་པར་བྱའོ། །

[Block 4366]
ཅི་གང་ཡང་རུང་བས་སམ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་གལ་ཏེ་སྟན་དེ་དག་མ་ཐོབ་པ་ཡིན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་གིས་གཉིས་སམ་གསུམ་གྱིས༌[^3038]སྟན༌[^3039]དེ་དག་མི་ཐོབ་པ་ཡིན་ན། དེས་དེ་དག་དོར་ནས་གཞན་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4367]
གང་གིས་གཉིས་མི་ཐོབ་པ་དེས་ཀྱང་གཉིས་གཞག་པར་བྱ། གང་གིས་གཅིག་མི་ཐོབ་པ་དེས་ཀྱང་གཅིག་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་འདིའི་རྗེས་སུ་འབྲངས་ནས་ཤེས་པར་བྱའོ། །

[Block 4368]
སེང་གེའི་ཁྲི་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། གནས་ཤིང་བསྟན་པར་བྱའོ། །

[Block 4369]
མཆིལ་མའི་སྣོད་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་མཆིལ་མ་དོར་བའི་ཕྱིར་ཞེས་བྱ་བ་བརྗོད་པས་གོ་བའོ། །

[Block 4370]
འདིར་གཉིས་ཀ༌[^3040]ཡང་བརྩམས་པ་སྟེ། །ཆོས་སྨྲ་བ༌[^3041]ཁྲི་སྟན་ལོགས་ཤིག༌[^3042]ཏུ་སྤགས་པ༌[^3043]ལ་བལྟས༌[^3044]ནས་འདི་སྨོས་པ་སྟེ། སེང་གེའི་ཁྲི་ཙམ་ལ་ནི་མ་ཡིན་ན༌[^3045]ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4371]
སེང་གེའི་ཁྲི་ལ་དེ་སྨོས་ཀྱི་གཞན་ལ་ནི་ཤིན་ཏུ་དམན་པའི་སྐྱོན་འདི་ཞེས་བྱ་བ་བསྟེན༌[^3046]པའོ། །

[Block 4372]
དེར་གཅལ༌[^3047]བླུགས་སོ་ཞེས་བྱ་བ་ལ། མཆིལ་མའི་སྣོད་ནི་སྣོད་དུ་རིག་པར་བྱ་སྟེ། དེར་གཅལ་ཅི་བླུགས་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་བྱེ་མའམ་ཐལ་བའོ་ཞེས་བྱ་བ༌[^3048]སྨོས་ཏེ། དེ་གཉིས་ནི་དཔེ་ཙམ་དུ་ཟད་དོ།[^3049] །དོན་འདི་ལ་གཞན་ཡང་རུང་བའི་ཕྱིར་རོ། །

[Block 4373]
དེ་དུས་དུས་སུ་སྦྱང་བར༌[^3050]བྱའོ་ཞེས་བྱ་བ་ལ།[^3051] དེ་ཞེས་བྱ་བ་ནི་མཆིལ་མའི་སྣོད་དེའོ། །

[Block 4374]
ཚེས་བརྒྱད་དང་། བཅུ་བཞི་དང་། བཅོ་ལྔའི་ནུབ་མོ་ཆོས་མཉན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཚེས་བརྒྱད་དང་བཅུ་བཞི་ལ་ཞེས་བྱ་བ་དེ་ཙམ་འདིར་རེ་ཞིག་རྣམ་པར་འབྱེད་པ་ལས་མཐོང་བ་ཡིན་ཏེ། མ་མོ་ལས་ནི་ཚེས་བཅོ་ལྔའི་ཚིག༌[^3052]ཀྱང༌[^3053]འདིར་ཡོད་པ་ཡིན་ནོ། །

[Block 4375]
འདིར་ཆོས་ཉན་དུ་གཞུག་པ་རིགས་པ༌[^3054]ཡིན་ཏེ། དེ་ལ་ཡང་དེ་དུས་ཚིགས་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་དང་། ཤིན་ཏུ་གཙོ་བོ༌[^3055]ཉིད་ཀྱི་ཕྱིར་ཕྱི༌[^3056]མ་དུས་ཚིགས་ཀྱི་ཞག་དག་གིས་ཉམས་ཞེས་བྱ་བ་ངེས་པར་བྱས་ནས་འདི་སྐད་དུ། ནད་པས་དེ་མ་བྱས་པ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ནད་པས་དེ་ཆོས་མཉན་པ་དེ༌[^3057]མཉན་པ་དང་མ་བཏོན་པ་ལ་ཉེས་པ་མེད་པའོ། །

[Block 4376]
དེ་སྨྲ་བའི་ཕྱིར་གསོལ་བ་འདེབས་པ་མི་གདོན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་ཆོས་མཉན་པའི་ཕྱིར་ཆོས་ལའོ། །

[Block 4377]
མི་ནུས་པ་ལ་སོགས་པ་ཡིན་ན༌[^3058]གསོལ་བ་འདེབས་པ་ལ་ཤད་ཀྱིས་སྦྱང་བར་བྱའོ་ཞེས་བྱ་བ་ནི། ན་སྟེ་མི་ནུས་པའམ་བྱ་བ་གཞན་གྱིས་བྲེལ་བར་གྱུར་པ་ཡིན་ན་བྱ་བ་གཞན་ལ་རྩེ་གཅིག་པ་ལ་སོགས་པ་མ་ཡིན་པ་ལ་ནི་སོགས་པའི་སྒྲས་དྲངས༌[^3059]པའོ། །

[Block 4378]
སྨྲ་བ་པོ་མེད་ན་རིམ་གྱིས་དྲན་པར་བྱ་ཞིང་ཐ་ན་ཚིགས་སུ་བཅད་པ་རེ་རེ་ཙམ་ཡང་སྨྲ་བར་བྱའོ། །

[Block 4379]
དེར་མར་མེ་གཟུགས་སོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་ཆོས་ཉན་ས་དེར་རོ། །

[Block 4380]
ཁྱམས་སུ་ཆོས་མཉན་པའི་གྲལ་ནི་ཟླ་ཁམ་གྱི་རྣམ་པ་ལྟ་བུའམ་རྫིང་བུའི་རྣམ་པ་ལྟ་བུར༌[^3060]བཤམ་པར་བྱའོ་ཞེས་བྱ་བ་ནི། འདིར་དེའི་དོན་ནི་ཐུན་མོང་དུ་དཔེ་ཙམ་དུ་ཟད་དེ་མི་གནོད་པ་གཞན་དག་ཀྱང་རུང་སྟེ། དེ་བས་ན་ངེས་པ་མེད་དོ། །
--- END BLOCKS ---
