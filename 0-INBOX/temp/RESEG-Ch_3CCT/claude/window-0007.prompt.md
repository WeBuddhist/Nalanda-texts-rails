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
ཞེས་པ་རྩ་བའི་རྒྱུད་གསང་བ་འདུས་པ་ཞེས་བྱ་བ་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ཀྱི་དཀྱིལ་འཁོར་དུ་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས༌[^109]བདུད་རྩི་ལྔ་ལ་དངོས་སུ་སྤྱད་པའི་སྟོབས་ཀྱིས་འཁོར་བ༌[^110]ན་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དང་། ཉན་ཐོས༌[^111]འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ཤིན་ཏུ་སྐྲག་པའི་སྟོབས་ཀྱིས༌[^112]དངངས་པ་དང་ངུས་པ་དང་བརྒྱལ་བ་ལ། མི་བསྐྱོད་པ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་བསླངས༌[^113]ནས་དེ་དག་གི༌[^114]དོན་བསྟན་པ་འདི་ནི་བྱང་ཆུབ་སེམས་དཔའི་གསང་བའི་དབང་གི་གླེང་གཞིའོ། །

[Block 247]
[^115]དེ་ལ་གསང་བའི་དབང་གི་རྫས་གང་ལ་བྱ༌[^116]ཞེ་ན།

[Block 248 [VERSE]]
རྫས་ནི་དཀར་དམར་བཅུ་ཕྱེད་ལྡན། །
གང་དུ་འདི་ཡི་སྦྱོར་བ་བྱེད། །

[Block 249]
ཅེས་པ་ནི་བྱང་ཆུབ་ཀྱི༌[^117]སེམས་དཀར་དམར་དང་། དེ་ལས་གཞན་པའི༌[^118]དྲི་ཆེན་དང་། དྲི་ཆུ་དང་། ཤ་ཆེན་དང་། ཤེལ་ལ་སོགས་པ་འདི་དག་ནི་རྫས་ཏེ། འདི་ལ་བརྟེན་ནས་ངག་གི་རྣམ་པར་རྟོག་པ་ལྡོག་པར་བྱེད་དོ། །

[Block 250]
དེ་ཡང་གནས་གང་དུ་བསྐུར་ཞེ་ན།

[Block 251 [VERSE]]
གནས་ནི་སློབ་མའི་ལྕེ་གསུམ་ལ། །
སྦོམ་པོ་དབང་མོས་བླངས་ཏེ་སྦྱིན། །

[Block 252]
ཞེས་པ། མགྲིན་པ་དང་སྙིང་ག་དང་ལྟེ་བ་སྟེ། གང་གི་རོ་མྱོང་བར་བྱེད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 253]
འདིའི་རིམ་པའང་ཅི་ལྟར་ཡིན་ཞེ་ན།

[Block 254 [VERSE]]
རྡོ་རྗེ་པདྨ་སྙོམས་འཇུག་སྒྲ། །
ནོར་བུའི་ཆ་རྟེན༌[^119]ངག་ལ་སྦྱིན། །
ལྔའམ་དྲུག་དང་ལྡན་པ་ནི། །
གསང་བའི་དབང་གི་རིམ་པའོ། །

[Block 255]
ཞེས་པ་ནི་བདག་ཉིད་སྦྱོར་བའི་དབང་དུ་བྱས་ཏེ། ཤེས་རབ་མའི་ཆུས་རྡོ་རྗེ་བཀྲུས་པ་ནི་ཆུའི་དབང་ངོ་། །ནོར་བུའི་ཆ་ལ་བརྟེན་པ༌[^120]ནི་དབུ་རྒྱན་གྱི་དབང་ངོ་། །རྡོ་རྗེ་འཇུག་པ་ནི་རྡོ་རྗེའི་དབང་ངོ་། །ཅག་སྒྲ་ནི་དྲིལ་བུའི་དབང་ངོ་། །ཨ་ཧ་ཨ་ཧ་ཞེས་བྱ་བ་ནི་མིང་གི་དབང་ངོ་། །ཡང་ནི༌[^121]དཀར་དམར་སྤེལ་བ་ནི་ཕྲེང་བའི་དབང་ངོ་། །བུམ་པ༌[^122]གཉིས་ནས་འབྱུང་བས་ཆུའི་དབང་ངོ་། །ནོར་བུ་ལ་བརྟེན་པས༌[^123]དབུ་རྒྱན་གྱི་དབང་ངོ་། །རྡོ་རྗེ་ལ་རེག་པས་རྡོ་རྗེའི་དབང་ངོ་། །ཨ་ཧོ་སུ་ཁ་ཞེས་པ་དྲིལ་བུའི་དབང་ངོ་། །བབས་པའི་ཡི་གེ་ལ་མིང་བཏགས་པ༌[^124]ནི་མིང་གི་དབང་ངོ་། །ཡང་ན་འབྲལ་བ་མ་ཡིན་པ༌[^125]ཕྲེང་བའོ། །

[Block 256]
ཆུའི་ངོ་བོ་ཉིད་ཀྱིས་ཆུའི་དབང་ངོ་། །དགོས་པ་ཐམས་ཅད་འབྱུང་བར་བྱེད་པས་དབུ་རྒྱན་ནོ། །

[Block 257]
སེལ་བར་བྱེད་པ་ཉིད་ཀྱིས༌[^126]རྡོ་རྗེའོ། །

[Block 258]
སྒྲ་ཐམས་ཅད་དབང་བསྐུར་བར་བྱེད་པས་དྲིལ་བུའོ། །

[Block 259]
བདག་པོར་བསྟབས་པས་མིང་གི་དབང་ངོ་། །དེ་ལའང་ཐབས་ཇི་ལྟ་བུ་ཞིག་གིས་བསྐུར་ཞེ་ན།

[Block 260 [VERSE]]
གང་གིས་བཀྲ་ཤིས་བསྟོད་པ་ཡིས། །
ནམ་ཕྱེད་དུས་སུ་བསྐུར་བར་བྱེད། །

[Block 261]
ཅེས་པ༌[^127]རྣལ་འབྱོར་པ་དང་ཕྱག་རྒྱ་མ་གཉིས་སྙོམས་པར་ཞུགས་པའི་བྱང༌[^128]སེམས་དཀར་དམར་ཕབ་སྟེ་ཚོགས་ཀྱི་འཁོར་ལོ་ཆེན་པོ་བྱས་ལ། ནམ་ཕྱེད་ཀྱི་དུས་སུ་བརྩེ་བས་བྱང༌[^129]སེམས་རྡོ་རྗེའི་ཆ་ལ་བརྟེན་ནས༌[^130]བཀྲ་ཤིས་ཀྱི་ཚིགས་སུ་བཅད་པའི་བསྟོད་པས་སྨོན་ལམ་བཏབ་སྟེ། སློབ་མའི་ངག་ལ་བྱིན་ལ། སློབ་མས་ཀྱང་ཨ་ཧོ་མ་ཧཱ་སུ་ཁ་ཞེས་བཏུང་བར་བྱའོ། །

[Block 262]
དེ་ནས་སློབ་དཔོན་ལ་བསྟོད་པ་བྱས་པ་འདི་ནི་གསང་བའི་དབང་གི་ཐབས་སོ། །

[Block 263]
འོ་ན་དབང་བསྐུར་བའི་དཀྱིལ་འཁོར་ཡང་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན།

[Block 264 [VERSE]]
དཀྱིལ་འཁོར་ལུས་ཀྱི་སྦྱོར་བ་ལས། །
རྩ་ལ་སོགས་པ་ཚོགས་པའོ། །

[Block 265]
ཞེས་པ་ཕྱག་རྒྱ་མ་དང་རྡོ་རྗེ་སློབ་དཔོན་གྱི་ལུས་ལ་རྩ༌[^131]ནི་ཐིག་གི་ངོ་བོའོ། །

[Block 266]
རྐང་བརྒྱད་ནི་ཀ་བའོ།[^132] །སོ་དང་སེན་མོ་དང་བ་སྤུ་ནི་ཏྭ་ར་ནའོ། །

[Block 267]
ཁྲག་ལ་སོགས་པ་ནི་ས་ཚོན་གྱི་རང་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 268]
དེ་བས་ན་གསང་བའི་དཀྱིལ་འཁོར་ནི་གཉིས་སུ་ཤེས་པར་བྱའོ། །

[Block 269]
དེར་འཇུག་པའི་རིམ་པའང་ཇི་ལྟར་བྱ་ཞེ་ན།

[Block 270 [VERSE]]
རས་ཀྱིས༌[^133]ངོ་ཡང་དག་པར༌[^134]བྱ་སྟེ། །
རང་གི་བྱ་བ་རྫོགས་པར་བྱ། །

[Block 271]
ཞེས་པ་གང་གིས་སློབ་དཔོན་དང་ཕྱག་རྒྱ་མ་གཉིས༌[^135]སྙོམས་པར་འཇུག་པའི་དུས་སུ། བར་དུ་ཡོལ་བས་བཅད་དེ། རས་དམར་པོས་མིག་བཀབ་ལ། དང་པོར་གསོལ་བ་གདབ་པ་དང་། །ཕྱག་འཚལ་བ་ནས། ལུས་ཀྱི་དཀྱིལ་འཁོར་བསྟན་པ་དང་། །དེ་ཁོ་ན་ཉིད་ཀྱི་རིམ་པ་བསྟན་པའི་བར་དུའོ། །

[Block 272]
དེའི་སྔོན་དུ་བྱ་བའང་གང་ཞིག་ཅེ་ན། གང་གི༌[^136]བུམ་པའི་དབང་བསྐུར་ནས། །ཞེས་པ་ནི་བུམ་པའི་དབང་འདི་ནི་སྤྱིའི་སྔོན་དུ་འགྲོ་བའོ། །

[Block 273]
བྱེ་བྲག་གི་སྔོན་དུ་འགྲོ་བ་གང་ཡིན་ཞེ་ན།

[Block 274 [VERSE]]
རིག་མ་བརྟག་དང་བསླང་བ༌[^137]དང་། །
བྱིན་ནམ་མ་བྱིན་བརྟག་པ་དང་། །
སྦྱང་དང་སྐྱེ་དང་གཟུང་བ་དང་། །
བསྲུང་དང་གསང་བ་བརྟག་པ་དང་། །

[Block 275 [VERSE]]
དེ་ཡི་བགེགས་རྣམས་བསྐྲད་པ་དང་། །
བྱིན་རླབས༌[^138]དེ་ཡི་སྦྱོར་བ་ལ། །
སྟ་གོན་ཆོ་ག་རྫོགས་བྱས་ནས། །
རིག་མ་དབང་བསྐུར་སྦྱོར་བ་དང་། །

[Block 276 [VERSE]]
བདག་གིས་གནང་བ་ནོད་པ་དང་། །
ཕྱི་རོལ་དུ་ནི་སློབ་མ་ལ། །
གསང་བའི་དམ་ཚིག་སྦྱིན་པ་དང་། །
གསང་བའི་ལྷ་དང་རྫས་རྣམས་ཀུན། །

[Block 277 [VERSE]]
ཇི་ལྟར་སྟ་གོན་བྱ་བ་དང་། །
གང་ཞིག་དངོས་གྲུབ་ཆོ་ག་ཡི། །
སྦྱོར་བ་མཆོག་ནི་འདིར་ཤེས་བྱ། །

[Block 278]
ཞེས་པ་འདིས་ནི་ས་གཞི་བརྟག་པ་ལ་སོགས་པའི་སྦྱོར་བ་བཞིན་དུ་ཕྱག་རྒྱ་མའང་དུང་མོ་དང་དྲུག་མོ་ལ་སོགས་པ་བརྟག་པ་དང་། ཡུལ་གྱི་རྒྱལ་པོ་དང་ཕ་ལ་སོགས་པ་ལ་བསླང་བ་དང་། གཞན་ཡང་ཕྱིས་དངོས་གྲུབ་ཀྱི་སྦྱོར་བའང་རྨི་ལམ་དུ་བརྟག་པ་དང་། མཎྜལ་ལ་མེ་ཏོག་གི་གཅལ༌[^139]བཀྲམ་ལ་བརྟག་པ་དང་། དེ་ཉིད་ཡུམ་རྡོ་རྗེ་ཀུན་དུ་བཟང་མོའི་ངོ་བོར༌[^140]བསྐྱེད་པ་ལ་སོགས་པ་འདི་དག་ནི་སྔོན་དུ་བྱ་བའི་རིམ་པའོ། །

[Block 279]
རྟགས༌[^141]ཀྱི་སྦྱོར་བའང་གང་ཡིན་ཞེ་ན།

[Block 280 [VERSE]]
གང་གིས་མེ་ཏོག་དེར་འདོར་དང་། །
དེ་བཞིན་གཞན་ལའང་ལྟོས༌[^142]པའོ། །

[Block 281]
ཞེས་པ་ནི་གསང་བའི་དུས་སུ་མཐོང་བའི་འདྲི་བ༌[^143]དང་མེ་ཏོག་དོར་བ་དང་། ཡེ་ཤེས་དབབ་པའི་སྦྱོར་བས་སྨྲ་བ་ལ་སོགས་པ་འབྱུང་བར་ཤེས་པར་བྱའོ། །

[Block 282]
འདིའི་དུས་ཀྱི་བརྡའང་གང་ཡིན་ཞེ་ན། སྦོམ་པོས་དབང་མོ་མནན་པ་ནི། ཟླ་བ་ཉི་མའི་སྦྱོར་བའོ། །ཞེས་པ་གང་གིས་སྦོམ་པོས་དབང་མོ་མནན་པ་ནི་གསང་བའི་དབང་གི་བརྡ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 283]
གཞན་མ་གཡས་ཀྱི་སྦྱོར་བས་གཡོན་པ་ལ་བྱེད་པས་ཡང་ལ་ལ་དག་འདོད་དོ། །

[Block 284]
དེའི་དུས་སུའང་བསམ་གཏན་ཇི་ལྟར་བྱ་ཞེ་ན། སློབ་དཔོན་རིག་མ་ལྟར༌[^144]བསྒོམ་དང་། གང་གིས་བདེ་སྟེར་བསམ་གཏན་ཡིན། །ཞེས་པ་གསང་བའི་དབང་བསྐུར་བའི་དུས་ཀྱི་བསམ་གཏན་ཡང་དང་པོར་སློབ་དཔོན་རིག་མ་དང་བཅས་པ་ཐབས་དང་ཤེས་རབ་ཀྱི་སྐུར་གནས་པར་བྱ་སྟེ། དེ་ལས་བྱང་ཆུབ་སེམས་ཀྱི་ཆུས་བཀང་བའི་བུམ་པ་ཐོགས་པ་བསམ་གྱིས་མི་ཁྱབ་པ་བྱུང་ནས་སློབ་མའི་ལྕེ༌[^145]ལ་དབང་བསྐུར་བར་བྱའོ། །

[Block 285]
འོ་ན་དེས་བག་ཆགས་སམ་དྲི་མ་གང་འཁྲུ་བར་བྱེད་ན།
--- END BLOCKS ---
