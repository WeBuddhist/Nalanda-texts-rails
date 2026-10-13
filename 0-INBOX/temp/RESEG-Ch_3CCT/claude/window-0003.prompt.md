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
[Block 106 [VERSE]]
ས་ནོན་སྤྱོད་དང་ལས་ལ་མཁས། །
ཡོན་ཏན་མཆོག་དང་ལྡན་པའོ། །

[Block 107]
ཞེས་པ་དུས་དེར་སློབ་དཔོན་ལྟ་བ་དང་སྤྱོད་པ་དང་དབང་དང་དམ་ཚིག་དང་ལྡན་པ། ཉོན་མོངས་པ་མེད་པ། ཤིན་ཏུ་ཉོན་མོངས་པ་མེད་པ། གཟུགས་མཆོག་ཏུ་བཟང་བ། རིགས་མཐོ་བ། སྐད་སྙན་པ། སྙན་པར་གྲགས་པ། ཐམས་ཅད་ཀྱིས་བསྟོད་པ། ཡང་དག་པའི་ཚོར་བ་དང་། དྲན་པ་དང་། དད་པ་དང་། ངོ་ཚ་ཤེས་པ་དང་། ཁྲེལ་ཡོད་པ་དང་། མ་ཆགས་པ་དང་། ཞེ་སྡང་མེད་པ་དང་། གཏི་མུག་མེད་པ་དང་། རྣམ་པར་མི་འཚེ་བ་དང་། ཤིན་ཏུ་སྦྱངས་པ་དང་། བག་ཡོད་པ་དང་། བརྩོན་འགྲུས་ལ་སོགས་པ་དང་ལྡན་པ་དང་། མོས་པའི་ས་དང་། དྲོད་དང་། རྩེ་མོ་དང་། བཟོད་པ་དང་། ཆོས་ཀྱི་མཆོག་བཅུ་གཉིས་ལ་གནས་པ་དང་རབ་ཏུ་དགའ་བ་དང་། དྲི་མ་མེད་པ་དང་། འོད་འཕྲོ་བ་དང་། འོད་བྱེད་པ་ནས། ཀུན་ཏུ་འོད་ཀྱི་བར་ལ་གནས་པ། བརྡ་དང་བརྡའི་ལན༌[^41]ལ་མཁས་པ། གར་དང་ཕྱག་རྒྱ་དང་། མཆོད་པ་དང་། གཡབ་མོ་དང་། གླུ་དང་གླུའི་ལན་ལ་མཁས་པ། ཞི་བ་དང་། རྒྱས་པ་དང་། དབང་དང་། རེངས་པ་དང་། བཅུག་པ༌[^42]དང་། བསད་པ་དང་། དབྱེ་བ་དང་། གསོ་བ་དང་། དགུག་པ་དང་། སྲེག་པ་དང་། འབར་བ་དང་། སྟེག་པ་དང་། འཁྱུད་པ་དང་། འཇིབ་པ་དང་། དེ་ལ་སོགས་པ་འདོད་ཆགས་ཀྱི་སྤྱོད་པ་དང་། འདོད་ཆགས་དང་བྲལ་བའི་སྤྱོད་པ་ལ་མཁས་པ། རིག་པའི་གནས་དང་གསོ་བའི་ཆོ་ག་ལ་མཁས་པའོ། །

[Block 108]
སློབ་དཔོན་དེས་སློབ་མ་ཅི་འདྲ་བ་ཅིག༌[^43]ལ་བསྐུར་བ༌[^44]མི་ཤེས་ནས་དྲིས་པ་དང་། ལན་དུ། སློབ་མའང་དགེ་བས་བརྒྱན་པ་དང་།

[Block 109 [VERSE]]
གསང་བ་འཇིགས་མེད་ཚོད་རིག་ཅིང་། །
བླ་མའི་ཡིད་དུ་འོང་བ་དང་། །
ཐེག་ཆེན་སྣོད་དུ་རུང་བའོ། །

[Block 110]
ཞེས་པ༌[^45]བུམ་པའི་དབང་བསྐུར་བའི༌[^46]སློབ་མའང་དད་པ་དང་དམ་ཚིག་དང་མོས་པ་དང་དྲན་པ་ལ་སོགས་པས་བརྒྱན་པ་གསང་བ་ལ་འཇིགས་པ་མེད་ཅིང་མཆོག་ཏུ་དེ་ལ་དད་པ་དང་། སྦྱོར་བ་ལ་སོགས་པ༌[^47]ཚོད་རིག་པ། བླ་མ་ལ་ཚུལ་མ་ཡིན་པའི་སྤྱོད་པ་མི་བྱེད་པ་ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་ཡིན་པ། གསང་བ་འདུས་པའི་དཀྱིལ་འཁོར་དུ་དབང་བསྐུར་བའི་སྐལ་བ་དང་ལྡན་པ་སྟེ། མཚན་ཉིད་མདོར་བསྡུས་པ་འདི་རྣམས་དང་ལྡན་པ་ལ་སློབ་དཔོན་གྱིས་དབང་བསྐུར་བར་གསུངས་སོ། །

[Block 111]
རྫས་གང་ལ་བྱ་བའང་གང་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར།

[Block 112 [VERSE]]
རྫས་ནི་ཐུན་མོང་ཁྱད་པར་གྱིས། །
རྣམ་པ་གཉིས་སུ་ཤེས་པར་བྱ། །

[Block 113]
ཞེས་པ་ནི་ཕྱིའི་བུམ་པའི་རྫས་ནི་སྨན་དང་འབྲུ་དང་དྲི་དང་རིན་པོ་ཆེ་དང་མར་དང་ལན་ཚྭ༌[^48]ལ་སོགས་པ་ལ་བྱའོ། །

[Block 114]
ནང་གི་བུམ་པའི་རྫས་གང་ཡིན་ཞེ་ན། དེའི་སྟེང་དུ་བདུད་རྩི་ལྔ་དང་། ཤ་ལྔའོ། །

[Block 115]
སྦས་པ་ཐབས་ཀྱི་བུམ་པའི་རྫས་གང་ཞེ་ན། སློབ་དཔོན་གྱི་ཆུའོ། །ཤེས་རབ་ཀྱིའང་དེ་ཉིད་དོ། །

[Block 116]
གཞན་ཡང་བསྟན་པ།

[Block 117 [VERSE]]
དབུ་རྒྱན་རྡོ་རྗེ་དྲིལ་བུ་དང་། །
ཕྲེང་བ་མིང་ཡང་རྫས་སུ་འདོད། །

[Block 118]
ཅེས་པ་ནི་རྡོ་རྗེ་དང་དྲིལ་བུ་དང་ཕྲེང་བ་དང་མིང་ཡང་རྫས་སུ་ཤེས་པར་བྱའོ། །

[Block 119]
དབང་འདིའི་རིམ་པའང་ཇི་ལྟར་བསྐུར་ཞེ་ན། འདི་ཡང་།

[Block 120 [VERSE]]
ཕྲེང་བ་ཆུ་ལ་སོགས་པ་རྣམས། །
ཅི་རིགས་བསྐུར་བ་རིམ་པ་ཡིན། །

[Block 121]
ཞེས་པ་ནི་དང་པོར་སློབ་མ་ལ་ཕྲེང་བའི་དབང་བྱིན་པས་སྣོད་དུ་རུང་བར་བྱས་ནས་ཕྱིས་ནི་ཆུའི་དབང་བསྐུར་བར་བྱ་སྟེ། དེའང་དང་པོར་བྱང་ཆུབ་ཏུ༌[^49]སེམས་བསྐྱེད་པ་དང་། གསོལ་བ་གདབ་པ་དང་། གནང་བ་སྦྱིན་པ་དང་། ནམ་མཁའི་ལྷ་མོ་བསྐུལ་བ་དང་། ཆུའི་དབང་བསྐུར་བ་དང་། བསམ་པ་དང་། འབྲས་བུ་དང་། ལམ་གྱིས་ཤེས་པར་བྱའོ། །

[Block 122]
ཆུ་ལ་ཇི་ལྟ་བ་དེ་ལྟར་དབུ་རྒྱན་དང་། རྡོ་རྗེ་དང་། དྲིལ་བུ་དང་། མིང་གི་དབང་ལའང་ཤེས་པར་བྱ་སྟེ། དེ་དག་གི་ཡང་རྫས་དང་སྔགས་དང་ལྷའི་ཁ་དོག་ལ་སོགས་པ་ཤེས་པར་བྱའོ། །

[Block 123]
ཐབས་ཀྱང་ཇི་ལྟ་བུ་ཞིག་གིས་བསྐུར་ཞེ་ན།

[Block 124 [VERSE]]
སློབ་དཔོན་དང་ནི་སློབ་མ་ཡི། །
བསམ་མཐུན་དེ་ཐབས་དམ་པའོ། །
གར་དང་ཕྱག་རྒྱ་གླུ་ལ་སོགས། །
དེ་ཡང་ཐབས་སུ་ཡང་དག་འདོད། །

[Block 125]
ཅེས་པ་ནི་གང་གི་ཚེ་ཆུ་ལ་སོགས་པས་དབང་བསྐུར་བའི་དུས་སུའང་སློབ་དཔོན་གྱི་བསམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་སློབ་མས་ཀྱང་དེ་ལྟར་བྱེད་པ་འདི་ཡང་ཐབས་སོ། །

[Block 126]
གཞན་ཡང་བུམ་པའི་ཆུ་བླུགས་པ་ལ་སོགས་པའི་དུས་སུ། གར་བསྒྱུར་བ་དང་། ཕྱག་རྒྱ་བྱེད་པ་དང་། རྡོ་རྗེའི༌[^50]གླུ་ལེན་པ་དང་། དུང་དང་པི་ཝང་དང་། གླིང་བུ་དང་། ཁར་རྔ༌[^51]དང་། པ་ཊ་ཧའི་རྔ་ལ་སོགས་པ་བརྡུང་ཞིང་། མཆོད་པའི་ཚོགས་ཆེན་པོ་དང་ལྡན་པར་བྱེད་པ་འདིའང་ཐབས་སོ། །

[Block 127]
ཐབས་མེད་འབྲས་བུ་མེད་གྱུར་ཀྱང་།

[Block 128 [VERSE]]
སྤོང་མེད་དེ་ཡི་རྒྱུ་མེད་ཕྱིར། །
མཁས་པ་རྣམས་ནི་གང་ཞིག་གིས། །
ཐབས་ནི་བསྙད་པར་བྱ་བ་ཡིན། །

[Block 129]
གནས་ཀྱང་གང་དང་གང་དུ་བསྐུར་ཞེ་ན། །

[Block 130 [VERSE]]
ཆུ་ནི་སྤྱི་བོར་བསྐུར་བྱ་སྟེ། །
བཞི་ནི་ཕྱོགས་བཞིར་བསྐུར་བར་བྱ། །
ཕྲེང་བའི་དབང་ཡང་སྤྱི་བོར་ཏེ། །
མཁས་པས་འདི་དག་གནས་སུ་གསུངས། །

[Block 131]
ཞེས་པ་ལས་དང་པོ་ཕྲེང་བའི་དབང་ནི་སྤྱི་བོར་ཏེ། འདིས་སྣོད་དུ་རུང་བར་བྱས་ནས་ཆུ་ནི་སྤྱི་བོར་བསྐུར་བར་བྱའོ། །

[Block 132]
དབུ་རྒྱན་ནི་རྣ་ལྟག༌[^52]གཡས་སུའོ། །

[Block 133]
རྡོ་རྗེ་ནི་ལྟག་པར་བསྐུར་བར་བྱའོ། །

[Block 134]
དྲིལ་བུ་ནི་ལྟག་པ་གཡོན་དུ་བསྐུར་བར་བྱའོ། །

[Block 135 [VERSE]]
མིང་ནི་དཔྲལ་བར་བསྐུར་བར་བྱའོ། །
དཀྱིལ་འཁོར་ཡང་གང་དུ་བསྐུར་ཞེ་ན།
དཀྱིལ་འཁོར་སློབ་མ་རབ་འབྲིང་གིས། །
མེ་ཏོག་རྡུལ་ཚོན་ཕྱིར་དུ་གསུངས། །

[Block 136]
ཞེས་པ་སློབ་མ་རབ་དང་ལྡན་པ་ནི་མེ་ཏོག་གི་དཀྱིལ་འཁོར་དུའོ། །

[Block 137]
འབྲིང་ནི་སྐུའོ། །

[Block 138]
ཐ་མ་ནི་རྡུལ་ཚོན་གྱི་དཀྱིལ་འཁོར་དུ་དབང་བསྐུར་རོ། །

[Block 139]
ཡང་ན་སློབ་དཔོན་གྱི་དབང་དུ་སྟེ།

[Block 140 [VERSE]]
རབ་དང་འབྲིང་དང་ཐ་མའི་སློབ་དཔོན་གྱིས། །
དཀྱིལ་འཁོར་གསུམ་དུ་དབང་བསྐུར་བར་བྱའོ། །

[Block 141]
དཀྱིལ་འཁོར་ཉིད་ཀྱང་སའི་ཆ་མཉམ་པ་ལ། བྱི་དོར་བྱས་ཏེ་མེ་ཏོག་བཀྲམ་པ་འདི་ནི་མེ་ཏོག་གི་དཀྱིལ་འཁོར་རོ། །

[Block 142]
ཆག་ཆག་བཏབ་སྟེ་སོ་སོའི་གནས་སུ་དྲིའི་ཐིག་ལེ་བྱས་པ་ལ། རས་ལ་སོགས་པ་ལ་ཁ་དོག་དང་དབྱིབས་དང་རྒྱན་དང་ལྡན་པའི་སྐུ་བྲིས་ཏེ། ལྷག་པར་གནས་པ་བྱས་ནས་སོ་སོའི་གནས་སུ་བཀོད་པ་འདི་ནི་སྐུའིའོ། །

[Block 143]
ཡི་གེ་དང་ཕྱག་མཚན་དུ་བྱ་བའང་ཅི་རིགས་པའོ། །

[Block 144]
རྡུལ་ཚོན་གྱི་དཀྱིལ་འཁོར་ཡང་སའི་ཆ་མཉམ་པ་ལ་ཐིག་བཏབ་སྟེ། དཀར་པོ་ལ་སོགས་པའི་ཚོན་རིན་པོ་ཆེ་ལས་བྱུང་བའམ། འབྲུ་ལས་བྱུང༌[^53]བའམ། སའི་ཁམས་ལས་བྱུང་བ་བྱིན་གྱིས་བརླབས་ཏེ། དེས་མ་འདྲེས་ཤིང་སྐྱོན་དང་བྲལ་བ་བྲིས་ལ། སྐུ་གསུང་ཐུགས་གང་ཡང་རུང་བའི་ལྷ་བཀོད་དེ། དེར་དབང་བསྐུར་བ་འདི་ནི་དཀྱིལ་འཁོར་དུ་ཤེས་པར་བྱའོ། །

[Block 145]
དཀྱིལ་འཁོར་དེར་འཇུག་པའང་ཇི་ལྟར་འཇུག་ཅེ་ན།
--- END BLOCKS ---
