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
[Block 3151]
གཞན་རབ་ཏུ་བྱུང་བ་འདི་པ་དང་། ཕྱི་རོལ་པའི་རབ་ཏུ་བྱུང་བ་དབང་བ་ཉིད་ལ་འདིར་ཉེས་བྱས་སུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3152]
གང་གི་ཚེ་དངོས་གཞིར་གྱུར་པའི་སོང་བའི་མཐར་ཐུག་པ༌[^2021]ཡོངས་སུ་རྫོགས་པའི་བདག་ཉིད་ལ་དངོས་གཞིའི་དུས་སུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྤངས་པའི་ཉེ་འཁོར་གྱི་མཐའ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྔར་གནས་མལ་སྤངས་ཏེ་འགྲོ་བའི་ཉེ་འཁོར་གྱི་མཐར་ཐུག་ན་རྫོགས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3153]
ཁྱིམ་པ་ལ་ལོག་ཐབས་བྱེད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 3154]
ད་འདི་མན་ཆད་ནི་ཁྱིམ་པ་མོའི་བཟོ་སྟོན་པའི་ལྟུང་བྱེད་གསུམ་སྟེ། གང་ལ་དེ་རྣམས་ཀྱི་དབང་པོར༌[^2022]འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྐུད་པ་འཁལ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྒྱུད་ཀྱི་རང་གཞན་གང་ཡང་རུང་བ་བསྒྲུབ་པ་བྱས་ན་སྐུད་པ་འཁལ་བ་ཉིད་ཡིན་ཏེ། རི་མོ་ཙམ་བྱས་པ་ལ་རི་མོ་བྱས་པ་ཉིད་སྨོས་པར་རྟོགས་པའོ། །

[Block 3155]
འདི་ལྟར་རྣམ་པར་འབྱེད་པ་ལས།

[Block 3156]
བདུན་པོ་དག་ལས་གང་ཡང་རུང་བ་ཞེས་གསུངས་མོད་ཀྱི། དེ་ནི་དཔེ་ཙམ་དུ་ཟད་དེ་རུང་བ་མ་ཡིན་པའི་སྐུད་པ་འཁལ་བ་ལ་ཡང་ཐམས་ཅད་དུ་བཟོ་སྟོན་པའི་ཉེས་པ་འདྲ་བའི་ཕྱིར། འདི་ནི་ཐམས་ཅད་མཉམ་པ་ཡིན་ནོ། །

[Block 3157]
དེ་བས་ན་ཐམས་ཅད་དུ་སྐུད་པ་ལ་ཀུན་ནས་བརྟེན་པའོ། །

[Block 3158]
རྒྱ་ཅང་དང་ལྕག་པོད༌[^2023]ཀྱི་དོན་དུ་དབེན་པའི་ཕྱོགས་སུ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་དེའི་ཆེད་དུ་ཆོས་དང་ལྡན་པའི་དགོས་པའི་དབང་གིས་ཚངས་པར་སྤྱོད་པ་དང་བཅས་པའི་འཇར་བ༌[^2024]བཞིན་དུ་འདི་ལ་ཉེས་པ་མེད་པ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 3159]
དབེན་པའི་ཞེས་བྱ་བ་ནི་དབེན་པའི་ས་ཕྱོགས་སུ་དང་བ་མི་སྐྱེ་བའི་དངོས་པོ་བྱས་པས་ཞེས་བྱ་བ་འདི་ལ་སྤྲོས་པ༌[^2025]འདིའོ། །

[Block 3160]
གང་ཞིག་ཁྱིམ་པ་མོའི་བཟོ་སྟོན་པའི་ལྟུང་བྱེད་གསུམ་ཞེས་སྨོས་པ་དེ་རྣམས་ལས་ཕྱི་མ་གཉིས་པོ་སྤངས་ནས་རང་བཞིན་གྱི་རྣམ་པར་འགྱུར་བའི་དངོས་པོ་འདི་ལྟར་སྐུད་པ་དང་གོས་གཉིས་ནི་སྣམ་བུ་བྱ་བའི་རྒྱུ་དང༌[^2026]འབྲས་བུའི་ངོ་བོ་ཉིད་དུ་འབྲེལ་པའི་ཕྱིར་དང་། རྣམ་པར་བསྒྲུབ་པར༌[^2027]འདྲ་བའི་ཕྱིར་བཟོ་བསྟན་པའི་ལྟུང་བྱེད་དང་པོ་འདི་དང་མངོན་པར་འབྲེལ་པའི་དབང་གིས་དེ་ལས་ཕྱི་མ་བདག་ཏུ་མི་བྱེད་པ་ལ་དགེ་སློང་མའི་ཚོགས་ཀྱི་གོས་བདག་གིར་བྱེད་པ་འདི་རྣམ་པར་གཞག་པའོ། །

[Block 3161]
དེའི་རྗེས་སུ་གཞན་བྱས་པ་ལ་ཟས་འཚོང་བ་ཞེས་བྱ་བ་འདི་ལ་ཐོ་འཚམས༌[^2028]པར་བྱེད་པས། ཇི་ལྟར་དགེ་སློང་མའི་ཚོགས་ཀྱི་གོས་བདག་གིར་བྱེད་པ་དེ་དང་འདྲ་བའི་ཕྱིར་རྣམ་པར་གཞག་པའོ། །

[Block 3162]
ད་ནི་དེ་གཉིས་ཀྱི་དང་པོ་ཇེ་བསྟན་པར་བྱ་སྟེ། གང་ལ་དགེ་སློང་མའི་ཚོགས་ཀྱི་གོས་བདག་གིར་བྱེད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མའི་ཚོགས་ཀྱི་གོས་བདག་གིར་བྱེད་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ནི་དགེ་སློང་མ་སྦོམ་དགའ་མོས་བཙུན་མོ་ཕྲེང་ལྡན་མ་ལ་བཅོམ་ལྡན་འདས་ཀྱིས་བདག་ཅག་ལ་རྨེ་གབ་བཅང་བར་རྗེས་སུ་གནང་ན་བདག་ཅག་ལ་དེ་མི་བདོག་པས། དེ་ཁྱེད་ཀྱིས༌[^2029]བཙལ་བར༌[^2030]རིགས་སོ་ཞེས་སྨྲས་པ་དང་། དེས་གོས་ཀྱི་སྒྲོམ་ཐམས་ཅད་དགེ་སློང་མ་རྣམས་ལ་བྱིན་པ༌[^2031]དེ་སྦོམ་དགའ་མོས་བདག་གིར་བྱས་སོ། །

[Block 3163]
དེས་ན་དགེ་སློང་མ་རབ་ཏུ་མང་པོ་དག་གིས་བཙུན་མོ་ཕྲེང་ལྡན་མ་ལ་སྨྲས་པ། བདག་ཅག་ལ་རྨེ་གབ་ཀྱི་གོས་བྱིན་ཅིག །དེས་སྨྲས་པ། དགེ་སློང་མ་ཐམས་ཅད་ལ་བདག་གིས་བྱིན་ནོ། །

[Block 3164]
དེ་རྣམས་ཀྱིས་སྨྲས་པ་དང་། [^2032]གང་གིས་ཁྱེར་ཞེས་ཟེར་རོ། །

[Block 3165]
དེས་སྨྲས་པ། སྦོམ་དགའ་མོས་ཁྱེར་རོ། །

[Block 3166]
དེ་ནས་དགེ་སློང་མ་དེ་རྣམས་ཀྱིས་སྦོམ་དགའ་མོ་ལ་བླངས་པ་དང་། དེས་མ་སྟེར་བའི་གླེང་གཞི་ལས་བཅས་པ་ཡིན་ནོ། །

[Block 3167]
གཞག་པའི་རྫས་འདི་ལ་སྦྱིན་པར་བྱའོ་སྙམ་ནས་མ་འོངས་པ་བདག་ཏུ་བྱེད་པ་ལ་གལ་ཏེ་དངོས་པོ་ཡོངས་སུ་ཚང་ན་ཕམ་པར་འགྱུར་རོ། །

[Block 3168]
གལ་ཏེ་མ་ཡིན་ན་ལྟུང་བ་སྦོམ་པོར་འགྱུར་རོམ། [^2033]དེ་བས་ན་འདིར་མ་ཐོབ་པ་ཞེས་བྱ་བ་ཡོངས་སུ་བརྟགས་པ་སྟེ། མ་འོངས་པ་མ་ཡིན་པ་འདིར་བདག་ཏུ་བྱེད་པས་བསྔོས་པའི་རང་བཞིན་དུ་འགྱུར་བ་འདིར་འཇུག་པ་བསྟན་པ་ཞེས་བྱ་བ་རྫོགས་པར་བྱའོ། །

[Block 3169]
འདིར་ཚོགས་ཞེས་བྱ་བའི་སྒྲ་ནི་དགེ་འདུན་ལ་བྱ་སྟེ། དེ་དང་མ་བྲལ་བའི་ཕྱིར་ཡང་ཡོངས་སུ་རྫོགས་པར་འགྱུར་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3170]
དེ་ལྟར་ཡང་རྣམ་པར་འབྱེད་པ་ལས།

[Block 3171]
ཚོགས་ཀྱི་གོས་ནི་དགེ་འདུན་གྱིའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3172]
དགེ་སློང་མ་གཅིག་གམ་གཉིས་སམ་གསུམ་པོ་འདིའི་རྗེས་སུ་འབྲངས་ནས་ཁ་ན་མ་ཐོ་བ་ཤིན་ཏུ་ཆུང་བ་ཉིད་དོ། །

[Block 3173]
དེ་དག་ཀྱང་བསླུ་བའི་རྣམ་པ་དང་འདྲ་བའི་ཕྱིར་སྔ་མ་ཉིད་དང་འབྲེལ་པར་ཤེས་པར་བྱའོ། །

[Block 3174]
དགེ་སློང་མའི་ཚོགས་ཀྱི་གོས་བདག་གིར་བྱེད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 3175]
གཉིས་པ་ནི་ཟས་བཙོང་བ་བྱས་པ་ལའོ་ཞེས་བྱ་བ་སྟེ། ཟས་དེ་དག་ཇི་ཙམ་བྱས་ཀྱང་རུང་སྟེ་བྱས་པ་ཉིད་ཡིན་ཏེ་བྱེ་བྲག་མ་སྨོས་པར་ཤེས་པའོ། །

[Block 3176]
ཐ་སྙད་འདི་རྫོགས་པའི་དུས་ནི་དངོས་གཞིའི་དུས་སུ་རིག་པར་བྱའོ། །

[Block 3177]
ཀུན་དུ་སྤྱོད་པ་ཙམ་ཉིད་ལ་ཁ་ན་མ་ཐོ་བ༌[^2034]ནི་ཡིན་ཏེ། རྙེད་པ་བསྒྲུབ་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3178]
དེ་ཁོ་ན་ཉིད་ཡོད་པ་ལ་འདིར་སྤངས་པའི༌[^2035]ལྟུང་བྱེད་ཀྱི་ཁ་ན་མ་ཐོ་བ་གཞན་བསྐྱེད་པར་རིག་པར་བྱའོ། །

[Block 3179]
སྐབས་སུ་སྤྱད་པའི་ལྟུང་བྱེད་གཉིས་བསྟན་ནས། ད་ནི་ཁྱིམ་པ་མོ་ལ་བཟོ་སྟོན་པའི་ལྟུང་བྱེད་གཉིས་པོ་གང་ཡིན་པ་དེ་བརྗོད་པར་བྱ་སྟེ།[^2036] དེའི་ཕྱིར་ཁྱིམ་གྱི་བྱ་བ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ། བྱས་པ་ལའོ༌[^2037]བྱ་བའི་རྗེས་སྙེགས༌[^2038]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་ཏེ། དེ་དག་ཇི་ཙམ་བྱས་ཀྱང་རུང་སྟེ་བྱས་པ་ཉིད་ཡིན་ནོ། །

[Block 3180]
ཁྱིམ་དུ་ཆུས་ཆག་ཆག་གདབ་པ་དང་ཕྱག་དར་བྱས་པས་དག་པར་བྱས་པ་དང་། རྫ་ལས་བྱས་པའི་སྣོད་རྣམས་བཤལ་བ་དང་། བཟའ་བ་དང་བཏུང་བ་དང་། བལྡག་པ་ལ་སོགས་པའི་སྒྲུབ་པ་བསྒྲུབ་པར་བྱས་ཏེ་གཡོ་བ་དང་། ལག་པ་དང་རྐང་པ་ལ་སོགས་པ་བཀྲུ་བ་དང་། རིགས་ཀྱི་ལྷ་རྣམས་མཆོད་པ་དང་། བདུག་སྤོས་དང་གཏོར་མའི་ལས་བྱ་བ་ནི་ཁྱིམ་གྱི་བྱ་བའི་ངོ་བོ་གླེང་གཞི་ལས་འབྱུང་བ་ཡིན་ཏེ། བལྟ་བ་དང་དྲུག་པ༌[^2039]དང་། སྐམ་པ་དང་། བཏག་པ་དང་། ཤིང་ལམ་བཀྲུ་བ་དང་། གཞག་པ་དང་། མལ་ཆ་དང་། སྟན་སྤྲུག་པ་དང་། གཞག་པ་དང་། བཤམས་པ་ལ་སོགས་པ་རྣམས་དང་། མཆིལ་ལྷམ་དང་ཁྲུས་རས་འབུལ་བ་དང་། གོས་གཟུང་བ༌[^2040]དང་། ཁྲུས་ཀྱི་གོས་འབུལ་བ་དང་། བཙིར་བ་དང་ཞུགས་པའི་སྐྱེ་བོ་ལ་ཆུ་དང་དྲི་འབུལ་བ་དང་། ཀུན་ནས་འཇུག་ཏུ་བཅུག་པ་དང་། སྣོད་བཀྲུ་བ་ལ་སོགས་པ་ཡང་དེ་ཞེས་བྱ་བར་གྲགས་པའི་ཕྱིར་རྟོགས་པར་བྱའོ། །

[Block 3181]
རྗེན་པ་འཚོད་པ༌[^2041]ལ་སོགས་པ་ཆོ་གའི་ཡུལ་ཡིན་པས་ལྷག་མ་འདི་རྣམས་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 3182]
ཆང་གི་ལས་མི་བྱའོ་ཞེས་བྱ་བ་ནི། མནན་པ་ལ་སོགས་པ་ཆང་གི་ཡོ་བྱད་དེ་ལ་ཉེ་བར་མཁོ་བའི་ལས་མི་བྱའོ། །

[Block 3183]
བསླབ་པའི་བྱེ་བྲག་དང་འབྲེལ་བའི་ལས་འདི་རེས་འགའ་ཙམ་ཡིན་ཏེ། དེ་ལ་རེས་འགའ་ཙམ་འབྱུང་བ་ཡིན་ནོ། །

[Block 3184]
བཟའ་བ་སྐམ་པོ་འཚོད་པ༌[^2042]ལྟར་འདི་ལ་ཁྱིམ་གྱི་བྱ་བ་ལ་ཁོངས་སུ་མ་འདུས་པའི་ཕྱིར་ཆོ་ག་འདི་བསྟན་པ་ཡིན་ནོ། །

[Block 3185]
མདོ་འདི་དང་མདོ་འོག་མ་ནི་ཕྲན་ཚེགས་དག་ལས་འབྱུང་ངོ་། །ཆང་ཁང་བྱེད་དུ་མི་གཞུག་གོ་ཞེས་བྱ་བ་ནི་གཞན་བྱེད་དུ་འཇུག་པ་བཀག་པ་སྟེ། རང་གིས་བྱེད་པ་ནི་ཆེས་ཤིན་ཏུ་ལྕི་བ་དེ་བས་ན་འདི་ལ༌[^2043]ཡང་དེས་བཀག་པ་ཐོབ་པར་བྱེད་པ་ཉིད་དོ། །

[Block 3186]
ཁྱིམ་པ་མོའི་བཟོ་སྟོན་པའི་ལྟུང་བྱེད་གསུམ་པ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་རྗེན་པ་འཚོད་པའིའོ༌[^2044]ཞེས་བྱ་བ་སྨོས་ཏེ། མི་སྙི་བ་རྣམས་ཀྱི་སུམ་ཆ་བངས་པ་ཉིད་ཀྱི་མདུན་རོལ་དུ་དེ་ཉིད་ཡིན་ཏེ་མ༌[^2045]ཚོས་པའི་ཕྱིར་རོ། །

[Block 3187]
སྙི་བ་རྣམས་ཀྱི་ཁ་དོག་གྱུར་པའིའོ།[^2046] །ཁུ་བ་རྣམས་ཀྱི་ནི་ལན་གཉིས་ཁོལ་བར་གྱུར་པའིའོ་ཞེས་སྨོས་པ་ཡིན་ཏེ། འདི་རྗེན་པ་ཉིད་ཀྱི་ཕྱིར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3188]
གང་ཡང་རུང་བ་ལ་དེ་བཏགས་པའི་དབང་གིས་མེ་ལས་ཁྱད་པར་བསྒྲུབ་པ་ཉིད་ལ་འཚོད་པ༌[^2047]ལས་སྐྱེས་པ་ཉིད་རྩོམ་པ་གཅིག་པར་གྱུར་པ་ཉིད་ཀྱིས་ཆ་གཞན་དེར་ཞུགས་པའོ།[^2048] །བཏགས་པ༌[^2049]ལ་ནི་སྦྱོར་བ་ཉིད་དེ་སྔ་མ་ལ་དེ་སྦྱོར་བ་མ་ཡིན་པའི་སྦྱོར་བ་ཉིད་དོ། །

[Block 3189]
དགེ་སློང་གི་དགེ་འདུན་དང་། མཁན་པོ་དང་། སློབ་དཔོན་དང་། ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་རྣམས་ཀྱི་ཕྱིར་དབེན་པའི་ཕྱོགས་སུ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་ཚིག་ནི། སློབ་དཔོན་གང་ལ་ངེས་པ་ཉེ་བར་གཞག་པར་བྱ་བ་ཉིད་ནི་དེའམ་གཞན་ལ་ཡང་ངོ་། །ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་རྣམས་ཀྱི་ཞེས་བྱ་བ་ནི། རྣམ་པ་འདི་ལ་མངོན་པར་བརྟེན་ནས་འདིར་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་དང་བཅས་པ་ཉིད་ཀྱི་ཚིག་གིས་བཟུང་བ་བསྒྲུབ་པ་ཡོད་པ་ལ་ཐ་དད་པའི་ཞེས་སྨོས་སོ། །

[Block 3190]
དེ་བས་ན་འདི་ནི་མཚོན་པ་ཙམ་ཡིན་ཏེ། སློབ་དཔོན་ཡང་འདིས༌[^2050]འཕངས་པ་ཉིད་ཡིན་ནོ། །
--- END BLOCKS ---
