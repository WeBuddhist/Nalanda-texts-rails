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
[Block 281]
ངོ་བོ་ཉིད་མི་འགྱུར་བས་རྟག་གོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 282]
དངོས་པོ་སྐྱེ་བ་དེའི་རང་བཞིན་མེད་པ་ལས་འབྱུང་བ་ཁས་ལེན་ན་ནི།

[Block 283 [VERSE]]
རྩོམ་པ་ཡོད་ན་ངེས་པར་ཡང་། །
ལྟ་བར་གྱུར་པ་ཡོངས་སུ་འཛིན། །

[Block 284]
མེད་པ་ལས་དངོས་པོ་རྣམས་རྐྱེན་མི༌[^197]རྒྱུ་མེད་པ་ཁོ་ན་ལས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 285]
དེ་བས་ན་རྒྱུ་མེད་པར་ལྟ་བ་དེ་ཡང་དེ་བཞིན་དུ་ཡོད་ལ་དེ་ཡང་འབྲེལ་ན་ནི་ཆད་པར་ལྟ་བའི་སྐྱོན་དུ་ཡང་འགྱུར་རོ། །

[Block 286]
ནམ་ཞིག་འདི་ལ་རྟེན་ཅིང་འབྲེལ་བར་གང་འབྱུང་བ། །དེ་ལ་སྔོན་དང་ཐ་མ་ཅི། །ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་པའི་ཕྱིར་ཏེ། འདི་ལྟར་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བས་འདི་ནི་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་པའོ། །

[Block 287]
དེས་ན་ཐེ་ཚོམ་མེད་པར།

[Block 288 [VERSE]]
སྔོན་དང་ཕྱི་མའི༌[^198]མཐའ་སྤངས་པས། །
འགྲོ་བ་སྒྱུ་མ་བཞིན་དུ་སྣང་། །

[Block 289]
ཇི་ལྟར་སྒྱུ་མ་མཁན་གྱིས་སྒྱུ་མ་སྒྲུབ་པའི་སྔགས་ཀྱི་སྦྱོར་བ་ལས༌[^199]གླང་པོ་ཆེ་དང་རྟ་དང་མི་ལ་སོགས་པ་བྱུང་བ་རྣམས་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་ན་གླང་པོ་ཆེ་ལ་སོགས་པར་སྣང་སྟེ། དེ་དག་ལ་གླང་པོ་ཆེ་ཡང་དག་པ་ལ་སོགས་པ་ལྟར་སྔོན་དང་ཐ་མའི་རྟོག་པ་མི་འབྱུང་བ་དེ་བཞིན་དུ་གླང་པོ་ཆེ་ཡང་དག་པ་ལ་སོགས་པར་འདོད་པ་རྣམས་ཀྱང་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བས་སྔོན་དང་ཕྱི་མའི་མཐར་བརྟག་པ༌[^200]མི་རིགས་ཏེ་དེ་ལྟར་ན།

[Block 290 [VERSE]]
སྔོན་དང་ཕྱི་མའི་མཐའ་སྤངས་པ། །
འགྲོ་བ་སྒྱུ་མ་བཞིན་དུ་སྣང་། །

[Block 291]
སྐྱེས་ནས་སྐད་ཅིག་ཀྱང་མི་སྡོད་པར་འགྲོ་བས་འགྲོ་བར་བྱའོ།[^201] །སླུ་བའི༌[^202]བདག་ཉིད་པས་སྒྱུ་མ་སྟེ། དེའི་ངོ་བོ་ཉིད་ལ་རྨོངས་པ་རྣམས་ལ་ལོག་པར་སྣང་བས་སླུ་བ༌[^203]ཡིན་ནོ། །

[Block 292 [HEADING]]
### ཚིགས་བཅད་བཅུ་དྲུག་པ། ^1-17-0

[Block 293 [VERSE]]
དེའི་སླུ་བ༌[^204]ཉིད་བསྟན་པའི་ཕྱིར། །
གང་ཚེ་སྒྱུ་མ་བྱུང་ཞེ་འམ། །
གང་གི་ཚེ་ན་འཇིག་འགྱུར་ཞེས། །
སྒྱུ་མ་ཤེས་པ་དེར་མི་རྨོངས། །
སྒྱུ་མ་མི་ཤེས་ཡོངས་སུ་སྐོམ། །

[Block 294]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 295]
ཇི་ལྟར་སྒྱུ་མ་མཁན་གྱི་སྔགས་ཀྱི་རྐྱེན་ལས་བྱུང་བའི་བུད་མེད་ན་ཆུང་སྒྱུ་ཐབས་རྣམས་ལེགས་པར་བསླབས་པ་ལྟ་བུ་དབྱིབས་དང་སྤྱོད་ལམ་ཤིན་ཏུ་མཛེས་པ་ཚུལ་ཤིན་ཏུ༌[^205]མཛེས་ཤིང་གཞོགས་སྟེགས༌[^206]ལ་མཁས་པ་ཕུན་སུམ་ཚོགས་པ་ཡིད་འཕྲོག་པ་དག་ནི་དེའི་ངོ་བོ་ཉིད་ལ་མི་མཁས་པ་འདོད་པ་ལ་ཞེན་པ་རྣམས་ལ་ན་ཆུང་ཡང་དག་པ་བཞིན་དུ་མཆོག་ཏུ་དགའ་བའི་གནས་སུ་འགྱུར་ཏེ། དེ་ལ་ཇི་ལྟར་མི་མཁས་པ་ངག་རྣམ་པར་རྟོག་པ་ལྟར་རང་བཞིན་མེད་དེ་དེའི་ངོ་བོ་ཉིད་ལ་མཁས་པ་སྒྱུ་མ་མཁན་ནི་སྒྱུ་མ་ཡང་དག་པ་མ་ཡིན་པར་སྣང་བ་ཁོང་དུ་ཆུད་པས་དེ་ལྟར་ཡང་རྨོངས་པའི་སེམས་མི་འབྱུང་ངོ་། །དེ་བཞིན་དུ་འདིར་ཡང་སྒྱུ་མ་མཁན་ལྟ་བུའི་རྣལ་འབྱོར་པ་མཁས་པ་རྣམས་ཀྱིས།

[Block 296 [HEADING]]
### ཚིགས་བཅད་བཅུ་བདུན་པ། ^1-18-0

[Block 297 [VERSE]]
སྲིད་པ་སྨིག་རྒྱུ་སྒྱུ༌[^207]འདྲ་བར། །
བློ་ཡིས་མཐོང་བར་གྱུར་ན་ནི། །
སྔོན་གྱི་མཐའ་འམ་ཕྱི་མའི་མཐར།

[Block 298]
[^208] །ལྟ་བས་ཡོངས་སུ་བསླད་མི་འགྱུར། །རྣལ་འབྱོར་པས་སྲིད་པ་འདུས་བྱས་མ་ལུས་པ་སྒྱུ་མ་དང་སྨིག་རྒྱུ་བ་ལྟ་བུར་བློ་ཡང་དག་པའི་བསམ་པ་སོ་སོ༌[^209]རང་གི་ཤེས་རབ་ཀྱིས༌[^210]མཐོང་ན་དོན་དམ༌[^211]པའི་ངོ་བོ་ཉིད་དུ་གང་ཡང་མི་དམིགས་པས་དངོས་པོའི་རང་བཞིན་གང་ཡིན་པ་དེ་ལ་སྔོན་གྱི་མཐའ་འམ། ཕྱི་མའི་མཐར་ཡོངས་སུ་བསླད་པར་མི་འགྱུར་ཏེ། བློ་ཕྱིན་ཅི་ལོག་པར་མི་འགྱུར་རོ། །

[Block 299]
དེ་བས་ན་འཕགས་པའི་སྐྱེ་བོར་ཐམས་ཅད་གཤེགས་ཤིང་རྗེས་སུ་གཤེགས་པ་ངོ་བོ་ཉིད་མེད་པའི་ལམ་འདི་བོར་ནས་བདག༌[^212]ནི་སྒྱུ་མའི་བུད་མེད་ལ་མི་མཁས་པ་དག་བཞིན་དུ།

[Block 300 [HEADING]]
### ཚིགས་བཅད་བཅོ་བརྒྱད་པ། ^1-19-0

[Block 301 [VERSE]]
གང་དག་གིས་ནི་འདུས་བྱས་ལ། །
སྐྱེ་དང་འགག་པར་རྣམ་བརྟག༌[^213]པ། །
དེ་དག་རྟེན་འབྱུང་འཁོར་ལོ་ཡི། །
འགྲོ་བ་ཤིན་ཏུ་མི་ཤེས་སོ། །

[Block 302]
རང་གི་མཚན་ཉིད་སྐྱེ། རང་གི་མཚན་ཉིད་འགག་གོ་ཞེས་དེ་ལྟར་གང་དག་རང་གི་མཚན་ཉིད་སྐྱེ་ཞིང་འགག་པའི་ཚུལ་གྱིས་འདུས་བྱས་ཀྱི་སྐྱེ་བ༌[^214]དང་འགག་པ་ཡོངས་སུ་བརྟགས་པ་དག་གིས་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་འཁོར་ལོ་ལ་ཐོག་མ་དང་དབུས་དང་། ཐ་མ་དང་བྲལ་བ་མགལ་མེ་བསྐོར་བ་ལྟ་བུའི་འགྲོ་བ་འཇུག་པ༌[^215]ཤིན་ཏུ་མི་ཤེས་ཏེ།[^216] འདུས་བྱས་རང་བཞིན་ཡོད་པ་སྐྱེ་ཞིང་འཇིག་མི་སྲིད་པ་ལ་སྐྱེ་བ་དང་འཇིག་པ་རྟོག་པས་དེ་དག་གིས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་འཁོར་ལོ་ཁོང་དུ་ཆུད་ཅེས་བྱའོ། །

[Block 303]
རང་གི་མཚན་ཉིད་དུ་སྐྱེ་བར་ཁས་བླངས་ན་ཅིའི་ཕྱིར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་དོན་ཁོང་དུ་ཆུད་པ་མ་ཡིན་ཞེས་ཟེར་བ་དེ་ལ།

[Block 304 [HEADING]]
### ཚིགས་བཅད་བཅུ་དགུ་པ། ^1-20-0

[Block 305 [VERSE]]
དེ་དང་དེ་བརྟེན་གང་བྱུང༌[^217]བ། །
རང་བཞིན་དུ་ནི་དེ་མ༌[^218]སྐྱེས། །
རང་བཞིན་དུ་ནི་གང་མ་སྐྱེས། །
དེ་ནི་སྐྱེས༌[^219]ཞེས་ཇི་སྐད་བྱ། །

[Block 306]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 307]
དེ་དང་དེ་བརྟེན་ཞེས་བྱ་བ་ནི་དེ་དང་དེ་ལ་ལྟོས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 308]
དེ་དང་དེ་ཞེས་བྱ་བ་སྤྱིར་བསྙག་པ་ཐམས་ཅད་བསྡུ་བའི་སྤྱིའི༌[^220]ཚིག་འདིས་ནང་གི་མ་རིག་པ་ལ་སོགས་པ་དང་ཕྱིའི་རླུང་གི་དཀྱིལ་འཁོར་ལ་སོགས་པ་མ་ལུས་པ་དག་འདུ་བྱེད་ལ་སོགས་པ་དང་ཆུའི་དཀྱིལ་འཁོར་ལ་སོགས་པ་སྐྱེ་བ་ལ་རྒྱུའི་དངོས་པོར་གནས་པར་གྱུར་ཏེ། རྒྱུ་དེ་དང་དེ་ལ་བརྟེན་ནས་གང་སྐྱེ་བ་དེ་གལ་ཏེ་རང་གི་ངོ་བོས༌[^221]གྲུབ་པ་ཞིག་ཡིན་ན་ནི་དེ་ཡོད་པར་གྱུར་པས་གྲུབ་པའི་ངོ་བོའི་དུས་བཞིན་དུ་སྐྱེ་བའི་རྒྱུ་ལ་མི་ལྟོས་པར་འགྱུར་རོ། །

[Block 309]
ཅི་སྟེ་སྐྱེ་བ་དེ་སྔོན་རང་གི་ངོ་བོ༌[^222]མེད་ན་ནི་སྐྱེས་པ་དེ་ཡང་གཟུགས་བརྙན་བཞིན་དུ་ངོ་བོ་ཉིད་ཀྱིས་ཡོད་པ་མ་ཡིན་པར་མངོན་པས།

[Block 310]
དེ་དང་དེ་བརྟེན་གང་བྱུང་བ། །རང་བཞིན་དུ་ནི་དེ་མ་སྐྱེས། །ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 311]
ཅི་སྐྱེ་བ་ངོ་བོ་ཉིད་ཀྱིས་མེད་ཀྱང་བླ༌[^223]སྟེ་ཐ་སྙད་དུ་གཟུགས་སྐྱེས་སོ། །

[Block 312]
ཚོར་བ་སྐྱེས་སོ་ཞེས་བྱ་བས་སྐྱེ་བ་ཡོད་དོ་སྙམ་དུ་སེམས་ན་ནི་ཀྱེ་མ་ལམ་ལོག་པར་སོང་དུ་གདོན་མི་ཟའོ། །

[Block 313]
མཁས་པས་ནི་གཟུ་བོ༌[^224]ལྟ་བུའི་བློས་རྣམ་པར་དཔྱད་པའི་རིགས་པ་སྙམ།

[Block 314 [VERSE]]
རང་བཞིན་དུ་ནི་གང་མ་སྐྱེས། །
དེ་ནི་སྐྱེས་ཞེས་ཇི་སྐད་བྱ། །

[Block 315]
སའི་རང་གི་མཚན་ཉིད་ནི་ཕྲ་བ༌[^225]སྟེ། གལ་ཏེ་དེ་རང་གི་མཚན་ཉིད་དུ་མ་སྐྱེས་པར་སེམས་ན་དེ་གཤེར་བའི་མཚན་ཉིད་དུ་སྐྱེས་ས༌[^226]ཞེས་བརྟག་ཏུ་ནི་མི་རུང་ན། དེ་གཞན་གང་ཅི་ཞིག་ཏུ་སྐྱེ་བར་བརྟག །དེ་བས་ན་བདག་དང་གཞན་ལས་སྐྱེ་མི་སྲིད་པས་སྐྱེ་བ་མེད༌[^227]གྲུབ་བོ། །

[Block 316]
དེ་ལྟར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལ་སྐྱེ་བ་མི་སྲིད་པ་ཅི་བསྟན་ནས།[^228] ད་ནི་འགག་པ་མི་སྲིད་པར་བསྟན་པར་བཞེད་ནས།

[Block 317 [HEADING]]
### ཚིགས་བཅད་ཉི་ཤུ་པ། ^1-21-0

[Block 318 [VERSE]]
རྒྱུ་ཟད་པ་ཡིས༌[^229]ཞི་བ་ནི། །
ཟད་ཅེས་བྱ་བར་མངོན་པ་སྟེ། །
རང་བཞིན་དུ་ནི་གང་མ་ཟད། །
དེ་ལ་ཟད་ཅེས་ཇི་སྐད་བརྗོད། །

[Block 319]
ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 320]
སྐྱེས་པའི་དངོས་པོ་སྐྱེ་བ་ཡོད་ན་འཇིག་ལ་དངོས་པོའི་གནས་པ་ཡང་རྐྱེན་གྱི་ཁོ་ན་ལས་ཏེ་གནས་པའི་རྐྱེན་མེད་ན་འཇིག་པར་འགྱུར་བས་དེ་ལྟར༌[^230]ན་འཇིག་རྟེན་ན་རྒྱུ་ཟད་ནས་ཞི་བ་དང་མྱ་ངན་ལས་འདས༌[^231]པ་གང་ཡིན་པ་དེ་ཉིད་ཞི་བ་ཞེས་བྱ་བར་དམིགས་ཏེ། གང་ཡང་གནས་པའི་རྐྱེན་མེད་ན་ཟད་པར་འགྱུར་བ་དེ་གནས་པའི་རྐྱེན་མེད་པ་ལ་རག་ལས་པས་རང་གི་ངོ་བོར་གྲུབ་པ་མེད་པར་ཁོང་དུ་ཆུད་ནས།
--- END BLOCKS ---
