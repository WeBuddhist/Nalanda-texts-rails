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
[Block 3326]
ཅིག་ཤོས་དབུལ་བ་ཡང་ངོ་། །དགའ་བ་ཉིད་དུ་ཀུན་དུ་རྨོངས་པ་ནི་དགའ་བས་རྨོངས་པ་སྟེ། སྡུག་བསྔལ་ལ་བདེ་བར༌[^2122]ཕྱིན་ཅི་ལོག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3327]
སྡིག་པའི་འབྲས་བུ་སྨིན་པ་ཉིད། །ཅེས་བྱ་བ་ནི་སྐྱེ་བ་སྔ་མ་དག་ལ་རང་གི་གོམས་པས་སྡུག་བསྔལ་ལ་བདེ་བར་ཕྱིན་ཅི་ལོག་པའི་འབྲས་བུ་སྨིན་པའོ། །

[Block 3328]
འདིར་བྱར་རུང་ངོ་ཞེས་བྱ་བ་གལ་ཏེ་དེ་ལྟར་ཆོས་བརྙེས་པར་རུང་བ་ཞེས་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 3329]
ཆོས་ཀྱི་གཉེན་པོ་དང་འདོམ་པའི་ཕྱིར་ཏེ་ཆོས་དང་འགལ་བ་དང་།

[Block 3330 [VERSE]]
ཕྱོགས་རྣམ་པར་འཇིག་པའི་ཕྱིར་རོ། །
ལས་སུ་བྱ་བ་མང་ཆེས་པས། །

[Block 3331]
ཞེས་བྱ་བ་ནི་ཁྱིམ་གྱི་བདེ་བ་ཡིན་ནོ་སྙམ་ནས་ཁྱིམ་མ་བཏང་བས༌[^2123]ནི་ཆོས་བྱ་བར་འདོད་ཀྱང་ཁྱིམ་མ་བཏང་བར་ནི་གཞན་དུ་འགྱུར་བས་ཇི་ལྟར་ཆོས་བྱ་བར་མི་རུང་སྟེ། འདི་ནི་ཁྱིམ་གྱི་བདེ་བ་དེ་དང་དེ་ལ་མངོན་པར་ཞེན་པ་དེ་ལ་སྡུག་བསྔལ་ཡིན་པར་བསྟན་པར་བྱ་བའི་ཕྱིར། ལས་སུ་བྱ་བ་མང་ཆེས་པས། །ཞེས་བྱ་བ་འདི་བསྟན་པ་ཡིན་ནོ། །

[Block 3332]
ཆོས་ཀྱི་གཉེན་པོ་དང་འདོམ་པ་ཞེས་བྱ་བའི་དབང་དུ་མཛད་ནས། ཁྱིམ་གྱི་སོ་ནམ་བྱ་ན་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་བཞི་ཡིན་ཏེ། ཆོས་ཀྱི་གཉེན་པོའི་ཆོས་གང་ཡིན་ཞེ་ན། དེ་དང་མི་མཐུན་པར་གྲགས་པ། །ཞེས་བྱ་བའི་དོན་ཏེ། [^2124]ཁྱིམ་གྱི་སོ་ནམ་བྱ་ན་ནི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 3333]
ཁྱིམ་ན་ནོར་མེད་ན་ནི་སོ་ནམ་བྱ་བ་ཡིན་ནོ། །

[Block 3334]
སོ་ནམ་གྱི་བྱ་བ་བྱས་པར་གྱུར༌[^2125]ན་ནི་ཆོས་ཀྱི་དོན་ཉམས་པ་ཡིན་ནོ། །

[Block 3335]
དེ་ལྟར་ལུང་དུ་མ་བསྟན་པའི་ལས་ཀྱང་ཆོས་ཀྱི་གཉེན་པོ་ཡིན་པར་བསྟན་ཏོ། །

[Block 3336]
བརྫུན་དུ་མི་སྨྲ༌[^2126]མི་རུང་ཞིང་། །ཞེས་བྱ་བ་ནི་མི་དགེ་བ་དེ་ལ་འཇུག་པའི་དབང་དུ་བྱས་ནས་བརྫུན་དུ་སྨྲ་བཞེས་བྱ་བ་སྨོས་ཏེ། ངག་གི་ལས་ཀྱི་ལམ་གྱི་མི་དགེ་བ་བཞི་བཟུང༌[^2127]སྟེ། སྨྲ་བ་ཞེས་སྨོས་པས་དེ་ལ་གཞན་དག་ཀྱང་འགྲུབ་པོ། །ཉེས་པ་བྱེད་པ་ལ་ནན་ཏུར་ནི་ཞེས་བྱ་བ་ནི། སྲོག་གཅོད་པར༌[^2128]ནན་ཏུར་བྱ་བ་ཡིན་ཏེ། མི་དགེ་བའི་ལས་ཀྱི་ལམ་དག༌[^2129]ལས་སྲོག་གཅོད་པ་ཐོག་མར་སྨོས་པ་ཡིན་ཏེ། དེ་དང་པོར་སྨོས་པས་ལུས་ཀྱི་མི་དགེ་བའི་ལས་དག་ཀྱང་འགྲུབ་པོ།[^2130] །དེ་བས་ན་གཞན་ལ་ནན་ཏུར་ཞེས་བྱ་བས་མི་དགེ་བའི་ལམ་ལས་བཟློག༌[^2131]སྟེ། རལ་གྲི་དང་ཐལ་ལྕག་ལ་སོགས་པའི་མཚན་ཉིད་ཀྱིས་བཅད་ཅིང་ནན་ཏུར་བྱ་བ་ཡིན་ཏེ། གཞན་སླུ་བས༌[^2132]སྒྲུབ་པ་ལ་སོགས་པ་དེས་གཞན་དག་ལ་གནོད་པར་འགྱུར་བ་ཡིན་ཏེ་དེ་ལ་ནན་ཏན་དུ་བྱ་བའོ།[^2133] ། འདི་དག་གིས་ནི་འདི་ལྟར་སྟོན་ཏེ། ལུང་དུ་མ་བསྟན་པའི་ལས་ཀྱི་སོ་ནམ་གྱིས་ཀྱང་མི་དགེ་བའི་ལས་ཀྱི་ལམ་ཡང་དག་པར་འཛིན་པ་སྟེ། ལུས་དང་ངག་གི་ལས་ཀྱི་ནན་ཏུར་བྱ་བ་སྟེ། ལས་ཀྱི་ལམ་རྣམ་པར་སྤངས་པའི་མི་དགེ་བའི་ལས༌[^2134]བྱེད་པ་ལ་ནན་ཏུར་བྱའོ། །

[Block 3337]
ཡིད་ཀྱི༌[^2135]མི་དགེ་བ་གནོད་སེམས་ལ་སོགས་པ་ཡང་ཁྱིམ་ན་མེད་པ་མ་ཡིན་ནོ། །

[Block 3338]
སོ་ནམ་བྱ་བ་ལ་སོགས་པ་ལ་འཇུག་པའི་རྒྱུའི་དབང་དུ་བྱས་ནས། དེ་ལྟ་བས་ན་སྐྱེ་བོ་འདི་དག་ཅེས་བྱ་བ༌[^2136]ལ་སོགས་པའི་ཚིག་གོ། །

[Block 3339]
དེ་ལྟ་བས་ན་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་ཁྱིམ་གྱི་སོ་ནམ་མ་བྱས་པར་ཁྱིམ་མེད་དོ། །

[Block 3340]
ཁྱིམ་མེད་ན་བདེ་བ་མེད་དོ། །

[Block 3341]
དེ་སྒྲུབ་པ༌[^2137]ལ་འབད་པ་ཞེས་བྱ་བ་ནི་ཁྱིམ་གྱི་བདེ་བ་སྒྲུབ་པ༌[^2138]ལ་འབད་པ་སྟེ། ཁྱིམ་གྱི་བདེ་བ་སྒྲུབ་པའི་སོ་ནམ་ལ་སོགས་པའོ། །

[Block 3342]
ད་ནི་ཁྱིམ་ན་གནས་པས་ནི་ཆོས་དང་ཆོས་མ་ཡིན་པ་ཕན་ཚུན་འགལ་བས་རབ་ཏུ་དཀའ་བ་ཡིན་པའི་ཕྱིར་དེ་སྒྲུབ་པའི་དབང་དུ་བྱས་ནས། གལ་ཏེ་ཆོས་སྤྱོད་ཁྱིམ་གྱི་སོ་ནམ་འཆོར། །ཞེས་བྱ་བ་འདི་ཡིན་ནོ། །

[Block 3343]
གལ་ཏེ་ཆོས་སྤྱོད་པར་གྱུར་ཏེ་སོ་ནམ་ལ་སོགས་པ་མི་བྱེད་ན་ནི་ཁྱིམ་མེད་དེ། སོ་ནམ༌[^2139]འཆོར་བའི་ཕྱིར་ཇི་ལྟར་བསྟན་མ་ཐག་པའི་ཚིགས་སུ་བཅད་པ་བསྟན་པའོ། །

[Block 3344]
གལ་ཏེ་ཁྱིམ་ལ་མངོན་པར་ཕྱོགས་ན་ནི། །ཞེས་བྱ་བ་ནི་སོ་ནམ་ལ་སོགས་པ་བྱས་ནའོ། །

[Block 3345]
དེ་སྒྲུབ་པའི་ཕྱིར་སྨྲས་པ། ཆོས་ཀྱི་ལམ་ནི་རབ་ཏུ་ཞི་བ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་བསྟན་ཏེ། རབ་ཏུ་ཞི་བ་ནི་ཉོན་མོངས་པ་ཉེ་བར་ཞི་པའོ། །

[Block 3346]
ཡང་ན་རབ་ཏུ་ཞི་བ་ནི་སེམས་ཅན་གྱི་རྩོམ་པ་ལས་ལྡོག་པ་སྟེ། ཐར་པ་ནི་དོན་ཐམས་ཅད་ལས་ལྡོག་པ་ཡིན་ནོ་ཞེས་བྱ་བའི༌[^2140]ཚིག་གིས་སོ། །

[Block 3347]
དྲག་ཤུལ་ཅན་ཞེས་བྱ་བ་ནི་སྔར་བཤད་པའི་སོ་ནམ་ལ་སོགས་པའི་རིམ་པའོ། །

[Block 3348]
དེ་བས་ཆོས་དང་འགལ་བའི་སྐྱོན་ཡོད་ཕྱིར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་དོན་རྣམ་པར་གཞག་པ༌[^2141]ནི་སྔར་བཤད་པའི་དོན་ཁྱིམ་ན་གནས་པའི་བདེ་བ་དང་གཅིག་པ་མ་ཡིན་ནོ་ཞེས་པའོ། །

[Block 3349]
གཉིས་སུ་ན་ཁྱིམ་ནི་བདེ་བ་ཕྱོགས་གཅིག་ཏུ་མ་ངེས་པར་བསྟན་པའི་ཕྱིར་ངེས་པ་ཡོད་པ་མ་ཡིན་ཞེས་སྨོས་ཏེ། གཅིག་ཏུ་བདེ་བ་ཉིད་མ་ངེས་སོ། །

[Block 3350]
དེ་སྒྲུབ་པའི་ཕྱིར། གདོན་མི་ཟ་བར་གྲགས་པ་མེད་པར་འགྱུར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། གྲགས་པ་མེད་པར་འགྱུར་ཞེས་བྱ་བ་ནི་བདེ་བའི་རྒྱུ་འཇིག་རྟེན་པ་རྣམས་དགའ་བ་ལ་སོགས་པ་མེད་པར་བདེ་བ་འགྲུབ་པ་མེད་དོ། །

[Block 3351]
གདུང་བ་སྐྱེ་བ་ཞེས་བྱ་བ་ནི་འཆི་བའི་དུས་སུ་ཡིད་ལ་གཅགས༌[^2142]བཞིན་དུ་འཆི་བའི་ཕྱིར་རོ། །

[Block 3352]
ཡིད་ལ་གདུང་བ་སྐྱེ་བ༌[^2143]ལས་ནི་ངན་འགྲོར༌[^2144]སྐྱེ་བར་འགྱུར་ཏེ། འཇིག་རྟེན་ཕ་རོལ་དུ་ངན་སོང་གི་སྡུག་བསྔལ་འབྱུང་བའི་ཕྱིར་བདེ་བ་འགྲུབ་པ་མེད་དོ། །

[Block 3353]
བདེ་བའི་ཐབས་ཞེས་བྱ་བ་ནི། གང་གི་ཕྱིར་ཁྱིམ་དང་ཁྱིམ་ལ་གནས་པ་བདེ་བའི་རྒྱུའོ་ཞེས་མངོན་པར་ཞེན་པའི་དབང་དུ་བྱས་པ་ནི་ཁྱིམ་ལ་བདེ་བའི་ཐབས་ཞེས་བརྗོད་དོ། །

[Block 3354]
ངན་འགྲོ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་ངན་འགྲོ་བཞིན་དུའོ། །

[Block 3355]
ཁྱིམ་ན་གནས་པ་བདེ་བར་ནི་ག་ལ༌[^2145]བཤད་དེ། དེ་བས་ན་དད་པས་ཡིད་ཆེས་པར་བྱ་བ་ཡིན་པར་བདག་གིས་མ་མཐོང་ངོ་ཞེས་བཤད་པ་ནི་གཞན་གྱི་ལས་བྱེད་པ་དག་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་སོ། །

[Block 3356]
བཅིང་བ་དང་གསད་པ༌[^2146]དང་སྡུག་བསྔལ་ནི༌[^2147]བཅིང་ཞིང་གསད་པའི་སྡུག་བསྔལ་ལོ། །

[Block 3357]
དེ་དག་ཉིད་ཀྱི་གཞིར་གྱུར་པ་ཡིན་ཏེ། ཡོད་པར་གྱུར་ན་བཅིང་བ་དང་། གསད་པའི༌[^2148]སྡུག་བསྔལ་གྱི་གཞིར་གྱུར་པའོ། །

[Block 3358]
འདོད་པ་དེ་དག་གལ་ཏེ་ངོམས་པར་གྱུར་ན་མི་རུང་ན་དེ་ཡང་མེད་དེ། དེ་བསྟན་པའི་ཕྱིར་རྒྱལ་པོ་དག་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཡིན་ནོ། །

[Block 3359]
ཡངས་སུ་རྟོགས་པའི་དབང་དུ་བྱས་པའི་ཚིགས་བཅད་ནི། བསྒྲུབ་ཅིང་བསྲུང་བ་ལ་སོགས་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་དེའི་དོན་རྣམ་པར་འགྲེལ་ཏེ། འདི་ག་ལ་བདེ་ཞེས་བྱ་བ་ནི་བཅིངས་པ༌[^2149]དང་གསད་པའི༌[^2150]སྡུག་བསྔལ་གྱི་གཞིར་གྱུར་པས་ག་ལ་བདེ་སྟེ། དེ་བས་ན་ག་ལ་བདེའོ། །

[Block 3360]
ཇི་ལྟར་བདེ་ཞེས་བྱ་བ་ནི་རྒྱལ་པོ་དག་ཀྱང་འབྱོར་པས་ཆོག་པ་མེད་དེ། དེས་ན་ཇི་ལྟར་བདེ་བའོ། །

[Block 3361]
ནམ་ཞིག་བདེ་ཞེས་བྱ་བ་ནི་བསྒྲུབ༌[^2151]ཅིང་བསྲུང་ལ་སོགས༌[^2152]པའི་ཚེ་ན་སྡུག་བསྔལ་བའི་ཕྱིར་ནམ་ཞིག་བདེ་བ་ཡིན་ཏེ། དེས་ན་ཡང་རྣམ་པ་གསུམ་གྱིས་བདེ་བ་མེད་དོ། །

[Block 3362]
ཇི་ལྟར་དེ་ལ་འཇིག་རྟེན་པ་རྣམས་བདེ་བའི་བློ་འབྱུང་ཞེ་ན། སྨྲས་པ། ཡོངས་སུ་རྟོགས་པའི༌[^2153]དབང་གིས་བདེ་བ་འབྱུང་བ་ཡིན་གྱི། ངོ་བོ་ཉིད་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 3363]
དེ་ལྟར་རེ་ཞིག་བདེ་བ་ཡིད་ཀྱིས༌[^2154]ཡོངས་སུ་རྟོགས་པའི༌[^2155]མཐུ་ཡིན་པར་བསྟན་ནས། ཡུལ་རྣམས་ལ་རྨོངས་པས་ཉེ་བར་སྤྱོད་པ་ཞེས་བྱ་བ་ཡིན་ཏེ། དབང་པོ་ལྔའི་ཡུལ་གྱི་ཉེ་བར་སྤྱོད་པའི་བདེ་བ་ནི་དེ་ལ་རྣམ་པར་རྟོག་པ་མེད་པས༌[^2156]ཇི་ལྟར་བདེ་བར་འགྱུར་ཏེ་དེ་ལ་བདེ་བའི་རྣམ་པར་རྟོག་པ་མེད་པས་སོ། །

[Block 3364]
རྣམ་པར་རྟོག་པ་ཙམ་ཡང་མངོན་པར༌[^2157]ཤེས་པ་ལྔ་དང་ལྡན་པས་ན་དེ་ཉིད་སྨྲས་པ། རྨ་གཡའ་ཕྲུགས་པའི་བདེ་བ་བཞིན་དུ་ཟད། ཅེས་བྱ་བ་ཡིན་ཏེ། རྨ་གཡའ་བ་ལ་ཕྲུགས་པའི་བདེ་བ་འབྱུང་བ་དེ་བཞིན་དུ་ཡུལ་རྣམས་ལ་ཡང་བརྟེན་པས་ཀྱང༌[^2158]བདེ་བ་བཞིན་ནོ། །

[Block 3365]
ཆོས་ཀྱི་ལམ་ནི་རབ་ཏུ་ཞི་བ་ཡིན། །ཞེས་བྱ་བ་གང་སྔར་བཤད་པའི་རབ་ཏུ་ཞི་བ་ཡང་གཉིས་པ་བཤད་པ་ལས།
--- END BLOCKS ---
