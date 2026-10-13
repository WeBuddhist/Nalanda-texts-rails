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
[Block 246]
ཇི་སྐད་དུ་མདོ་ལས་གསུངས་པ་གང་ཞིག་གང་ན་མེད་པ་དེ་ནི༌[^215]སྟོང་ལ་གང་ཡང་འདིར་ལྷག་མ་དེ་ནི་ཡོད་པ་ལ་འདིར་ཡོད་དོ་ཞེས་ཡང་དག་པ༌[^216]ཇི་ལྟ་བ་བཞིན་རབ་ཏུ༌[^217]ཤེས་སོ་ཞེས་འདི་སྐད་སྨྲ་ན་སྟོང་པ་ཉིད་ལ་ཕྱིན་ཅི་མ་ལོག་པར་ཞུགས་པའོ། །

[Block 247]
གང་དུ་དགེ་སྦྱོང༌[^218]ངམ་བྲམ་ཟེ་དག་དེ་ཡང་གང་ཞིག་གིས་སྟོང་པ་མི་འདོད་ན་དེ་ནི་སྟོང་པ་ལས་ཕྱིན་ཅི་ལོག་ཏུ་ཞུགས་པའོ་ཞེས་སོ། །

[Block 248]
འོ་ན་གལ་ཏེ་གཞན་དབང་གི་རང་བཞིན་ནི་ངོ་བོ་ཉིད༌[^219]དུ་ཡོད་པའི་ཕྱིར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 249]
སུ་ཞིག་འདི་སྐད་སྨྲ། སྐྱེ་བ་ལས་སྔ་རོལ་དུ༌[^220]གཞན་དབང་གི་རང་བཞིན་ཡོད་དོ་ཞེས་སོ། །

[Block 250]
སྐྱེས་ནས་འདིའི་རང་བཞིན་ཡོད་དོ་ཞེས་བརྗོད་དོ། །

[Block 251]
སྨྲས་པ། གང་ཞིག་སྐྱེ་བ་ལས་སྔ་རོལ་ཏུ༌[^221]འདིའི་རང་བཞིན་མེད་ན་ཅིར་འགྱུར་བའི༌[^222]འདིའི་སྐྱེ་བ་ཡོད་པ་ཡིན། སྐྱེས་ནས་ཡོད་པ་ལ་འདི་ནི་ཡོད་པའོ་ཞེས་རུང་གི་མ་སྐྱེས་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 252]
སྐྱེས་པ་ཉིད་ཀྱང་ངེས་པར་གཟུང་བར་མི་ནུས་ན་ཁྱད་པར་བརྟག་པར༌[^223]ནུས་པ་མ་ཡིན་ནོ། །

[Block 253]
ཕ་རོལ་པོས་འདི་ཞེས་པ་དེ་ལས་སྐྱེ་བཞིན་པའོ་ཞེས་པའི་ཁྱད་པར་ངེས་པར་གཟུང་བར་མི་ནུས་ལ། དེའི་ཕྱིར་འདིའི་སྐྱེ་བ་མེད་ལ་མ་སྐྱེས་པ་ལ་ཅི་ཡོད་ལ༌[^224]ཉིད་ནི་ག་ལ་ཞིག་ཅེས་བྱ་སྟེ། འདི་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 254]
གལ་ཏེ་འདི་ཡོད་པ་མ་ཡིན་ན་རྒྱུ་མཚན་མེད་པས་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་མེད་པར་འགྱུར་རོ། །

[Block 255]
གལ་ཏེ་རེ་ཞིག་འདི་ཡོད་པར་གྱུར་ན། མུ་སྟེགས་བྱེད་ཀྱིས་བརྟགས་པའི་བདག་ཀྱང་ཡོད་པར་འགྱུར་ལ། དེ་ནི་ཚིག་ཙམ་གྱིས་སྨྲ་བའོ།[^225] །གལ་ཏེ་ཁོ་བོ་ཅག་གི་བདག་མེད་པར་གྱུར་ན། བཅིང་བ༌[^226]དང་གྲོལ་བ་ལ་སོགས་པ་མི་འགྲུབ་བོ་ཞེ་ན། འདི་ནི་རེ་ཞིག་བདག་ཡོད་པར་ཡང་མི་འཐད་དེ། འདི་གཉིས་ནི་རིགས་པ་དང་འགལ་བའི་ཕྱིར་རོ། །

[Block 256]
འདི་ལྟར་གཞན་དབང་དངོས་པོར་ཡོད་ན་ནང་གི་བྱེད་པའི་སྐྱེས་བུ་ཡང་ཡོད་ལ། འདི་ནི་མ་དཔྱད་པའི་ཡོད་པའོ་ཞེས་བྱ་སྟེ། འཇིག་རྟེན་པ་ལ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 257]
དེའི་ཕྱིར་གལ་ཏེ་རིགས་པ་དང་འགལ་བ་གཅིག་པོ་ཡོད་ཅིང་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པའི་རྒྱུར་རྟོག་ན་གཉིས་པ་ཡང་བརྟག་པར་བྱའོ། །

[Block 258]
དེའི་ཕྱིར་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པའི་རྒྱུ་དངོས་པོའི་རང་བཞིན༌[^227]ཡིན་ནོ། །

[Block 259]
དེ་ལྟ་ན་གང་ཞིག་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ།

[Block 260]
གང་ཡང་འདིར་ལྷག་མ་ཡོད་པ་དེ་ནི་ཡོད་དོ་ཞེས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ་ཞེས་ཐོས་པ་དེ་ཇི་ལྟར་གསུངས།

[Block 261]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ནི་དངོས་པོར་གྱུར་པ་བྱས་པ་སྟེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཕྱིར་གཟུགས་བརྙན་བཞིན༌[^228]མེད་ལ། གང་ཞིག་བྱིས་པ་རྣམས་དངོས་པོར་མངོན་པར་ཞེན་པའི་གནས་སུ་གྱུར་པ་དེ་ཡང་བྱིས་པའི་སྐྱེ་བོའི་བློའི་སྤྱོད་ཡུལ་ལ་རྣམ་པ་དེ་ལྟ་བུའི་དངོས་པོར་གྱུར་པ་བརྫུན་པ་སླུ་བའི༌[^229]ཆོས་ཅན་ནི་ཡོད་ལ་དེའི་རང་བཞིན་ནི་མེད་དོ། །

[Block 262]
དེའི་ཕྱིར་གང་གང་ན་མེད་པ་དེ་ནི་དེས་སྟོང་ངོ་ཞེས་བྱའོ། །

[Block 263]
བརྫུན་གྱིས་སླུ༌[^230]བའི་ཆོས་ཅན་དངོས་པོར་གྱུར་པ་ལ་རང་བཞིན་མེད་པས་དེའི་ཕྱིར་དངོས་པོར་གྱུར་པ་དེ་དེའི་རང་བཞིན་གྱིས་སྟོང་ངོ་། །གང་ཡང་འདིར་ལྷག་མ་ཞེས་པ་ནི་བརྫུན་པ་སླུ་བའི༌[^231]ཆོས་ཅན་རང་གི་མཚན་ཉིད་མ་གྲུབ་པ། བྱིས་པའི་སྐྱེ་བོའི་བློའི་སྤྱོད་ཡུལ་ཕྱིན་ཅི་ལོག་ལས་མ་གྲོལ་བ་ནི་ཡོད་དེ། ཇི་སྐད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ། སྒྱུ་མའི་རྣམ་པ་དེ་ནི་ཡོད་དོ། །

[Block 264]
བྱིས་པ་རྣམས་ཀྱི་བརྗོད་པ་དེ་ནི་ཡོད་དོ། །

[Block 265]
རྨོངས་པ་ཆགས་པ་དེ་ནི་ཡོད་དོ། །

[Block 266]
དེ་ལྟར་གང་ཅུང་ཟད་ཙམ་དེ་ནི་ཡོད་དོ་ཞེས་སོ། །

[Block 267]
དེའི་ཕྱིར་དེ་ལྟར་བརྟགས་པས་དཔྱོད་པ་པོས་བརྫུན་པ་སླུ་བའི༌[^232]ཆོས་ཅན་དངོས་པོར་གྱུར་པ་མངོན་དུ་ཤེས་པས། འཇིག་རྟེན་པའི་ལས་ཀྱི་འབྲས་བུ་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ལ་སོགས་པ་རྣམས་བརྫུན་པའི་དངོས་པོའི་རྒྱུ་མཚན་ཅན་ལ་གནོད་པ་མ་ཡིན་ནོ། །

[Block 268]
དེ་ལ་མི་གནོད་པས་ཆད་པར་སྨྲ་བའམ་མེད་པ་ཉིད༌[^233]མི་ལྟུང་ལ། རང་བཞིན་ལ་སྒྲོ་མ་བཏགས་པས་ཕྱིན་ཅི་མ་ལོག་པ་ལ་གནས་ཏེ་ཕྱིན་ཅི་ལོག་གིས་བསྐྱེད་པའི་འཁོར་བ་ངེས་པར་སྤོང་ཞིང་རྟག་པར་སྨྲ་བར་མི་ལྟུང་ངོ་། །འདིར་ཡང་ཐོག་མ་ཉིད་དུ་འཐད་པ་དང་བཅས་པས་དོན་ཆེན་པོར་ཡང་འགྱུར་ལ། གཞན་དུ་རང་བཞིན་ཡོད་པ་ཉིད་ནི་འཐད་པ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 269]
ཅི་སླར་རང་བཞིན་མེད་པ་དངོས་པོར་གྱུར་པ་ལ་བརྟེན་ནས་སྐྱེ་བར་འགྱུར་རམ། ཕྱིན་ཅི་ལོག་བདག་ཉིད་ངན་པ་ལ་རྣམ་པར་རོལ་པའི་གོ་འཕང་ལ་ཞུགས་པས་ད་གདོད་སྨོས་པ་ཉིད་ལས༌[^234]རྒྱས་པ་གསལ་བར་རྟེན་ཅིང་འབྲེལ་པ༌[^235]རང་བཞིན་མེད་པ་སྒྲུབ་བྱེད་ཀྱི་མིང་ཐོས་པ༌[^236]ལྟ་བུར་རློམ་སེམས་ནས་འདྲི་བ་ལ་འཇུག་པ་ཀྱེ་མ་ངོ་མཚར་ཏོ། །

[Block 270]
ཇི་སྐད་དུ་སྨོས་པའི་དཔྱད་པ་རྣམས་སེམས་ལ་གྱིས་ཤིག །ལུང་འདི་ལས་ཀྱང་འདི་གསལ་བར་བྱེད་པས་སེམས་ལ་ཞོག་ཤིག །[^237]ཇི་སྐད་དུ།

[Block 271 [VERSE]]
བྲག་ཕུག་རི་དང་རྫོང་དང་ཆུ་ཀླུང་ལ། །
གང་ཞིག་བརྗོད་པ་ལ་བརྟེན་བྲག་ཅ༌[^238]བཞིན། །
འདུས་བྱས་འདི་ཀུན་སྒྱུ་མ་ལྟ་བུ་དང་། །
སྨིག་རྒྱུ་དང་མཚུངས་འགྲོ་ཀུན་ཤེས་པར་གྱིས། །

[Block 272]
ཞེས་སོ། །

[Block 273]
དེའི་ཕྱིར་གང་ཞིག་གང་ན་མེད་པ་དེ་ནི་དེས་སྟོང་པ༌[^239]ཉིད་དུ་སྨྲ་བ་རྣམས་ཀྱིས་དེ་ལྟར་ཡང་དོན་རྣམ་པར་ཕྱེ་བའི་ཕྱིར་དེ་རྣམས་སྟོང་པ་ཉིད་ལ་ཕྱིན་ཅི་ལོག་ཏུ་ཁོང་དུ་ཆུད་པ་མ་ཡིན་ནོ། །

[Block 274]
གང་ཡང་ཚིགས་སུ་བཅད་པ་འདི་སྐད་དུ།

[Block 275 [VERSE]]
ཀུན་བརྟགས་དངོས་པོ་ཡོད་མིན་ཞིང་། །
གཞན་གྱི་དབང་ནི་ཡོད་པ་ན། །
སྒྲོ་འདོགས་པ་དང་སྐུར་འདེབས་པའི། །

[Block 276]
མཐར་རྟོགས་པ༌[^240]ནི་ཕུང་བར་འགྱུར།[^241] །ཞེས་པ་དེ་ཡང་ཇི་སྐད་དུ་སྨོས་པའི་བཤད་པས་ལེགས་པར་བཤད་པར་འགྱུར་ཏེ། རང་བཞིན་དུ་བརྟགས་པ་མེད་ལ། གཞན་དབང་ཡང་བརྫུན་པ་སླུ་བའི༌[^242]ཆོས་ཅན་བྱས་པ་རང་བཞིན་མེད་པ་ཡོད་པ་ལ། གང་ཞིག་དེའི་ཚེ་རང་བཞིན་མེད་པ་ལ་སྒྲོ་འདོགས་པར་བྱེད་པ་དང་སྒྱུ་མ་དང་མཚུངས་པ་བྱས་པ་ནི་མེད་དོ་ཞེས་སྨྲ་བ་དེ་ནི་ངེས་པར་ཕུང་བར་འགྱུར་རོ། །

[Block 277]
རྟག་པ་དང་ཆད་པའི་མཐའི་ཕྱོགས་ནས༌[^243]གནས་པས་ངེས་པར་ངན་འགྲོར་ལྟུང་བས། འདི་ལྟར་རྣམ་རིག་ཏུ་སྨྲ་བ་དེ་རྣམས་ལ་སྟོང་པ་ཉིད་ཕྱིན༌[^244]ཅི་ལོག་པར་རྟོགས་པ་མེད་དོ་ཞེས་བྱ་སྟེ། དེ་རྣམས་ནི་མཁས་པ་རྣམས་ཀྱི༌[^245]ཚད་མར་བརྗོད་པར་མི་རིགས་སོ། །

[Block 278]
དེ་ལྟར་ཡང་བདག་དང་བདག་གི་བས་སྟོང་པར་བསྒྲུབས་པས་མིག་རང་བཞིན་མེད་པར་བསྒྲུབས་ནས། སླར་ཡང་མིག་གི་རང་བཞིན་སྟོང་པར་བསྒྲུབ་པའི༌[^246]ཕྱིར་གསུངས་པ། རྟག་པ་བརྟན་པ་ཐེར་ཟུག་པ་ཡོངས་སུ་མི༌[^247]འགྱུར་བའི་ཆོས་ཅན་མ་ཡིན་པས་མིག་སྟོང་ངོ་ཞེས་པར་འབྲེལ་ཏོ། །

[Block 279]
དེ་བཞིན་དུ་ཡང་བདག་གི་སྒྲས་ནི་རང་བཞིན་གྱི་རྣམ་གྲངས་ཀྱི་ཕྱིར་སྐྱོན་མེད་དོ། །

[Block 280]
དེ་ལ་མི་རྟག་པ་དང་བྲལ་བས་རྟག་པའོ། །

[Block 281]
མི་གཡོ་བའི་ཕྱིར་བརྟན་པའོ། །

[Block 282]
གནས་སྐབས་ཐམས་ཅད་དུ་གནས་པའི་ཕྱིར་ཐེར་ཟུག་པའོ། །

[Block 283]
གཞན་དུ་མི་འགྱུར་བས་ཡོངས་སུ་འགྱུར་བའི་ཆོས་ཅན་མ་ཡིན་པའོ་ཞེས་བྱ་སྟེ། འདི་རྣམས་ནི་རང་བཞིན་གྱི་མིང་གི་བྱེ་བྲག་ཡིན་གྱི་ནང་གི་བྱེད་པའི་སྐྱེས་བུའི་ནི་མ་ཡིན་ཏེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྐྱེན་འདི་པ་ཙམ་ལ་རྣམ་པར་གནས་པས་ན་སྔར་ཉིད་དུ་དེ་དག་བཀག་པའི་ཕྱིར་རོ། །

[Block 284]
ཇི་སྐད་དུ་སྟོང་པ་ཉིད་དོན་དམ་པའི་མདོ་ལས།

[Block 285]
མིག་སྐྱེས་བཞིན་པ་གང་དུ་ཡང་འབྱུང་བར་མི་འགྱུར་རོ། །
--- END BLOCKS ---
