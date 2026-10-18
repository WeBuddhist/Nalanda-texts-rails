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
[Block 316]
མདོ་ལས་རྟག་ཏུ་བརྩོན་པ༌[^379]བྱང་ཆུབ་སེམས་དཔའ་དང་། མི་གཏོང་བརྩོན་བའི༌[^380]བྱང་ཆུབ་སེམས་དཔའ་ནི་བདག་གི་དོན་སྤྱོད་པ་དང་། གཞན་གྱི་དོན་ལ་བརྩོན་པ་སྟེ་རིམ་པ་བཞིན་ནོ། །

[Block 317]
ལག་ན་རིན་ཆེན་དང་རབ་ཏུ་སྦྱིན་པའི་བྱང་ཆུབ་སེམས་དཔའ་དག་ནི་སེམས་ཅན་དབུལ་བ་དང་ནད་ཀྱིས༌[^381]ཉོན་མོངས་པ་རྣམས་ལ་ཅི་རིགས་པར་ཕན་འདོགས་པའི་ཕྱིར་མཚན་གསོལ་བའོ། །

[Block 318]
རིན་ཆེན་ཟླ་བ་དང་ཟླ་རྒྱལ་དག་ནི་སེམས་ཅན་རྣམས་ཀྱི་མ་རིག་པའི་མུན་པ་སེལ་བའི་སྒོ་ནས་མཚན་གསོལ་བའོ། །

[Block 319]
གནོན་པ་ཆེན་པོ་བྱང་ཆུབ་སེམས་དཔའ་དག་ནི་སེམས་ཅན་འདུལ་བ་དང་མཐའ་ཡས་པའི་སེམས་ཅན་མཐུ་ཆེ་ཆུང་གིས༌[^382]སྒྲོལ་བའོ། །

[Block 320]
འཇིག་རྟེན་གསུམ་གནོན་བྱང་ཆུབ་སེམས་དཔའ་དང་། བཟང་སྐྱོང་བྱང་ཆུབ་སེམས་དཔའ་ནི་འཇིག་རྟེན་སྒྲོལ་བ་དང་། དམ་པའི་ཆོས་བསྲུང༌[^383]བ་ལས་མཚན་གསོལ་ཏོ། །

[Block 321]
བྱམས་པ་ལ་སོགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་དོན་ལས་བཏགས་པ༌[^384]སྟེ། སྡུག་བསྔལ་གྱི་ས་ནས་འདོན་པའི་བྱང་ཆུབ་སེམས་དཔའ༌[^385]རིན་པོ་ཆེ་སེམས་ཅན་ལ་བསྟབས༌[^386]ཤིང་མྱ་ངན་ལས་འདས་པའི་ཞི་བ་ལ་འཇོག་པ་ལས་བཏགས་སོ། །

[Block 322]
དེ་ལ་སོགས་པ་དང་ཐབས་ཅིག་ཏུ་བཞུགས་པ་ནི་བསྡུས་པའི་ཚིག་གོ། །

[Block 323 [HEADING]]
###### ཕྱིའི་འཁོར། ^4-1-5-5-4-0

[Block 324]
མདོ་ལས་བརྒྱ་བྱིན་ལྷའི་དབང་པོའི་འཁོར་ལྷའི་སྲས་པོ་སྟོང་ཕྲག་ཉི་ཤུ་ནི་གོང་དུ་ཕྱིའི་འཁོར་དང་ནང་གི་འཁོར་དུ་སྨོས་པ་གཉིས་ལ། ནང་གི་འཁོར་ལྔ་ནི་གོང་དུ་བསྟན་པ་ཡིན། ཕྱིའི་འཁོར་བཅུ་ལ་མི་དང་མི་མ་ཡིན་པར་དབྱེ་བ་དང་། མི་མ་ཡིན་པ་ལའང་ལྷ་དང་། ལྷ་མ་ཡིན་དུ་དབྱེ་བ་དང་། ལྷ་ལ་ཡང་འདོད་པ་དང་གཟུགས་ཀྱི་ལྷར་དབྱེ་བ་དང་། འདོད་ཁམས་ཀྱི་ལྷ་ལ་ཡང་བརྒྱ་བྱིན་དང་། རྒྱལ་པོ་ཆེན་པོ་བཞི་དང་། དབང་ཕྱུག་དང་གསུམ་མོ། །

[Block 325 [HEADING]]
###### **འདོད་ཁམས་ཀྱི་ལྷ།** ^4-1-5-5-4-1-0

[Block 326]
དེ་ལ་འདི་ནི་དང་པོ་སྟེ། ས་ལ་གནས་པ་དང་ནམ་མཁའ་ལ་གནས་པར་དབྱེའོ། །

[Block 327 [HEADING]]
###### **ས་ལ་གནས་པ།** ^4-1-5-5-4-1-1-0

[Block 328]
ས་ལ་གནས་པ་ནི་བརྒྱ་བྱིན་དང་། རྒྱལ་པོ་ཆེན་པོ་བཞི་སྟེ། བརྒྱ་བྱིན་ནི་རི་རབ་ཀྱི་རྩེ་ལ་གནས་ཤིང་སུམ་ཅུ་རྩ་གསུམ་ལྷའི་རྒྱལ་པོའོ། །

[Block 329]
མདོ་ལས་ཟླ་བ་ལྷའི་སྲས་པོ་ཞེས་པ་ནས། སྟོང་ཕྲག་ཉི་ཤུ་དང་ཐབས་ཅིག་གོ་ཞེས་པའི་བར་ནི་འོད་ཅན་དེ་གསུམ་ནི་རྒྱལ་པོ་ཆེན་པོ་བཞིའི་ཁམས་སུ་གཏོགས་ཏེ། ཉི་མ་ལྷའི་སྲས་པོ་ནི་འཕགས་པ་སྤྱན་རས་གཟིགས། ཟླ་བ་ལྷའི་སྲས་པོ་ནི་འཕགས་པ་མཐུ་ཆེན་པོ་ཐོབ་པ། ནམ་མཁའི་མཛོད་བྱང་ཆུབ་སེམས་དཔའ་ནི་རིན་ཆེན་འོད་བྱང་ཆུབ་སེམས་དཔའ་ཡིན་པར་མདོ་ལས་འཆད་དོ། །

[Block 330]
ཉི་མ་ནི་དཔག་ཚད་ལྔ་བཅུས་འཁོར། ཟླ་བ་ནི་དེ་བཞིན་ནོ། །

[Block 331]
སྐར་མ་ནི་ཆུ་ཤེལ་ལས་བྱས་ཏེ། ནང་གི་ཆེན་པོ་ལ་རྒྱང་གྲགས་བཅོ་བརྒྱད་ཀྱིས༌[^387]འཁོར། ནང་གི་ཆུང་ངུ་ནི་རྒྱང་གྲགས་བཞིས་འཁོར་ཞེས་འཆད་དེ། དེ་དག་ཐམས་ཅད་ཀྱང་ནམ་མཁའ་ལ་རྒྱུ་ཞིང་གླིང་བཞི་འཁོར་བར་རྒྱུ་ལ་རྒྱུ་བའི་ས་ནི་རི་རབ་ཀྱི་རྐེད་ནས་འཁོར་རོ། །

[Block 332 [HEADING]]
###### **ནམ་མཁའ་ལ་གནས་པ།** ^4-1-5-5-4-1-2-0

[Block 333]
མདོ་ལས་ལྷའི་དབང་པོ་ཆེན་པོ་ལྷའི་སྲས་པོའི་འཁོར་དང་ཐབས་ཅིག་ཏུ་བཞུགས་ཞེས་པ་ནི་ནམ་མཁའ་ལ་གནས་པའི་ལྷ་སྟེ། མཚེ་མ་རྣམས་དང་དགའ་ལྡན་གྱི་ལྷ་ནི་དབང་ཕྱུག་ལྷའི་སྲས་པོ་སྟེ། དགེ་བའི་རྣམ་པར་སྨིན་པ་ཆེ་བའི་ཕྱིར་གོང་ནས་གོང་དུ་འབྲས་བུ་དམ་པ་འབྱུང་བའི་ལྷའི་ཡིད་བཞིན་གྱི་ཤིང་ལས་ཅི་འདོད་པ་ལེན་ཅིང་དབང་སྒྱུར་བས་བདག་དང་གཞན་གྱི་ལོངས་སྤྱོད་རྫོགས་པའོ། །

[Block 334 [HEADING]]
###### **གཟུགས་ཀྱི་ཁམས་ཀྱི་ལྷ།** ^4-1-5-5-4-2-0

[Block 335]
མདོ་ལས་ཚངས་པ་མི་མཇེད་ཀྱི་བདག་པོ་ཚངས་པའི་འཁོར་དང་ཐབས་ཅིག་ཅེས་པ་ནི་དེ་དག་གཟུགས་ཀྱི་ཁམས་ཀྱི་ལྷ་རྣམས་ཏེ། བསམ་གཏན་གྱི་རིམ་པས་གནས་ཤིང་ལྷའི་རྒྱལ་པོ་དེ་གཞན་ལ་ཕན་པ་དང་བདེ་བ༌[^388]བྱེད་པས་མི་སྐྱོ་ཞིང་ཐུབ་པ་ཉམས་སུ་ལེན་པས་མི་མཇེད་པའོ། །

[Block 336 [HEADING]]
###### **ལྷ་མ་ཡིན་པའི་འཁོར་ལྔ།** ^4-1-5-5-4-3-0

[Block 337 [HEADING]]
###### **ཀླུའི་འཁོར།** ^4-1-5-5-4-3-1-0

[Block 338]
མདོ་ལས་ཀླུའི་རྒྱལ་པོ་བརྒྱད་འཁོར་མང་པོ་དང་ཐབས་ཅིག་ཏུ་བཞུགས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ལྷ་མ་ཡིན་པའི་འཁོར་ལྔ་ལས་དང་པོ་སྟེ་ཀླུའི་འཁོར་རོ། །

[Block 339]
དགའ་བོ་དང་བསྙེན་དགའ་བོ༌[^389]ནི་སྔོན་སྤུན་ཡིན་ཏེ། དགེ་བའི་སེམས་ཀྱིས༌[^390]ཆར་དང་རླུང་དུས་སུ་འབེབས་པའི་རྒྱལ་པོ་སྟེ། གཞན་ཡང་སོ་སོའི༌[^391]ཡོན་ཏན་དང་མཐུ་ལས་མིང་དུ་བཏགས་པའོ། །

[Block 340 [HEADING]]
###### **མིའམ་ཅི།** ^4-1-5-5-4-3-2-0

[Block 341]
མདོ་ལས་མིའམ་ཅིའི་རྒྱལ་པོ་བཞིའི་འཁོར་དང་ཐབས་ཅིག་ཏུ་བཞུགས་ཞེས་པ་ནི་སྒྲ་སྙན་པའི་ཡོན་ཏན་དང་ལྡན་པ་དག་གོ། །

[Block 342 [HEADING]]
###### **དྲི་ཟ།** ^4-1-5-5-4-3-3-0

[Block 343]
མདོ་ལས་དྲི་ཟའི་རིགས་ཀྱི་འཁོར་རྣམས་དང་ཐབས་ཅིག་ཏུ་བཞུགས་ཞེས་པ་ནི་དེ་དག་རྒྱུ་ཞིང་གར་དང་རོལ་མོའི་སྒྲ་སྙན་པ་འབྱིན་ཅིང་དྲིས་འཚོ་བར་བྱེད་པའོ། །

[Block 344 [HEADING]]
###### **ལྷ་མ་ཡིན།** ^4-1-5-5-4-3-4-0

[Block 345]
མདོ་ལས་ལྷ་མ་ཡིན་གྱི་དབང་པོའི་འཁོར་བཞི་རྣམས་དང་ཐབས་ཅིག་ཅེས་པ་ནི་ལྷའི་སྤྱོད་པ་མེད་དེ། གཡོ་དང་སྒྱུས་སྤྱོད་པ་མང་བས་ལྷ་མ་ཡིན་ཏེ། ཇི་ལྟར་མིའི་གཞུང་ཉམས་པ་ལ་མི་མ་ཡིན་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 346]
རྣལ་འབྱོར་སྤྱོད་པའི་གཞུང་ལས་ནི་ལྷའི་ཁམས་སུ་བཤད་དོ། །

[Block 347]
གཞན་ལས་ནི་ཡི་དགས་དང་བྱོལ་སོང་གི་ཁམས་སུ་གཏོགས་པར་ཡང་འཆད་དོ། །

[Block 348 [HEADING]]
###### **འདབ་བཟངས།** ^4-1-5-5-4-3-5-0

[Block 349]
མདོ་ལས་འདབ་བཟངས་ཀྱི་དབང་པོ་འཁོར་བཞི་དང་ཐབས་ཅིག་ཏུ་བཞུགས་ཞེས་པ་ནི་འདབ་བཟངས་ནི༌[^392]སྐྱེ་བ་རྣམ་པ་བཞི༌[^393]ལས་སྐྱེ་སྟེ། ཀླུའི་རིགས་ཀྱང་རྣམ་པ་བཞི་ལས་སྐྱེ་སྟེ།[^394] འདབ་བཟངས༌[^395]འདི་ཟས་སུ་ཀླུ་ཟའོ། །

[Block 350]
ཟ་བའི་ཐབས་ནི་འདབ་བཟངས༌[^396]འདི་འདབ་མས་རྒྱ་མཚོ་ལ་སླེབས་པས་ཀླུ་རྣམས་ཐོན་པ་ལ་ཟ་སྟེ། ཀླུ་བསོད་ནམས་དང་ལྡན་པ་དེ་བཞིན་གཤེགས་པའི་འཁོར་དུ་སྐྱེས་པ་རྣམས་འདབ་བཟངས་ཀྱིས་མི་གསོད༌[^397]པར་ཚད་མེད་པ་བཞིའི་སེམས་ཀྱིས་བསྐྱབ་པའི་ཕྱིར་ཏེ། དགེ་སློང་དག་སུ་འཚེ་བ་ཐམས་ཅད་ལས་ཐར་བར་འདོད་པའི་ཕྱིར་ཚད་མེད་པ་བཞི་ལ་བརྟེན་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 351 [HEADING]]
###### **མིའི་རྒྱལ་པོའི་འཁོར།** ^4-1-5-5-4-4-0

[Block 352]
མདོ་ལས་ལུས་འཕགས་མོའི་བུ་མ་སྐྱེས་དགྲ་དང་ཐབས་ཅིག་གོ་ཞེས་པ་ནི་མིའི་རྒྱལ་པོའི་འཁོར་བསྟན་ཏེ་རྒྱལ་པོ་སྨོས་པ་ནི་གཙོ་བོས་བསྡུས་པའི༌[^398]ཕྱིར་ཏེ། མ་སྐྱེས་དགྲའི་གླེང་གཞི་ནི་མ་བཙས་པའི་སྔ་རོལ་ཏུ་ཕ་བསད་པའི་བསམ་པ་དང་བཅས་པའི་ཕྱིར་མ་སྐྱེས་པར་ཕའི་དགྲར་གྱུར་པ་སྟེ། དེས་ཕ་བསད་པ་དེ་ཉན་ཐོས་པའི་གཞུང་དུ་སྡིག་པ་བཤགས་པས་སེམས་ཅན་དམྱལ་བར་ཕོ་ལོང་བརྡབས་པ་ཙམ་ཞིག་སྐྱེས་ཏེ། ཕྱིས་རང་སངས་རྒྱས་ཀྱི་འབྲས་བུ་ཐོབ་པར༌[^399]ཡང་འཆད་ཐེག་པ་ཆེན་པོ་ལས་ནི་ཆོས་ཟབ་མོ་རྟོགས་པའི་བཤགས་པས་སེམས་ཅན་དམྱལ་བར་མ་ལྷུང་བར་ཡང་འཆད་དེ། ཞིབ་ཏུ་མྱ་ངན་ལས་འདས་པ་ཆེན་པོའི་མདོ་ལས་གསུངས་པ་བཞིན་ནོ། །

[Block 353 [HEADING]]
###### འཁོར་བཞི། ^4-1-5-5-5-0

[Block 354]
མདོ་ལས་ཡང༌[^400]དེའི་ཚེ་བཅོམ་ལྡན་འདས་འཁོར་བཞིས་བསྐོར་ཏེ། མཆོད་པ་དང་རིམ་གྲོ་བྱས་ཞེས་པའི་བར་དུ་ནི་འཁོར་ཕུན་སུམ་ཚོགས་པ༌[^401]བཞིར་ཕྱེ་བ་ལ། གསུམ་ནི་བསྟན་ཟིན། འདི་བཞི་པ་སྟེ། འཁོར་བཞི་ལ་བདུད་དང་ཚངས་པ་དང་། དགེ་སློང་དང་བྲམ་ཟེའི་འཁོར་ཞེས་ཀྱང་འཆད། ཡང་འཁོར་རྣམ་པ་བཞི་སྟེ། ཉན་ཐོས་པའི་འཁོར་ཤཱ་རིའི་བུ་དང་། བྱང་ཆུབ་སེམས་དཔའ་བྱམས་པ་ལྟ་བུ་ཆོས་གླེང་བའི་འཁོར་དང་། དབང་པོ་སྨིན་པ་དེ་ཆོས་རྟོགས་པའི༌[^402]འཁོར་དང་། དགེ་བའི་རྒྱུ་ལ་སོགས་པའི་འཁོར་དང་། མ་འོངས་པ་ན་ཆུད་པར་འགྱུར་བའི་འཁོར་རོ། །

[Block 355]
ཡང་འཁོར་བཞི་སྟེ། དགེ་སློང་དང་། དགེ་སློང་མ་དང་། དགེ་བསྙེན་དང་། དགེ་བསྙེན་མའི་འཁོར་རོ། །
--- END BLOCKS ---
