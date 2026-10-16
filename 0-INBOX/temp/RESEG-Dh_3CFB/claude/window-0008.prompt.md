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
དགག་པའི་ཡུལ་ཅན་གྱི་ཐ་སྙད་ཀྱི་གཏན་ཚིགས་ལ་དེའི་གཏན་ཚིགས་ཞེས་བཤད་དེ། དེ་ལྟ་བུའི་མི་དམིགས་པ་ནི་རང་ཉིད་ཀྱིས་དགག་པའི༌[^171]ངོ་བོ་ཡིན་པའི་ཕྱིར། རྒྱུ་དང་ཁྱད་པར༌[^172]བྱེད་པ་མི་དམིགས་པ་ནི་གཉི་གའི་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 282 [VERSE]]
དེ་ལྟར་མི་དམིགས་འདི་རྣམ་གསུམ། །
བཤད་ཀྱང་རྣམ་པ་དུ་མ་སྟེ། །
དེ་དང་དེ་འགལ་ལ་སོགས་པ། །
མི༌[^173]རྟོགས་རྟོགས་དབྱེའི་སྦྱོར་སྒོ་ནས། །

[Block 283]
དགག་པའི་གཏན་ཚིགས་ནི་རྣམ་པ་གསུམ་ཁོ་ན་སྟེ། རྒྱུ་དང་ཁྱབ་པར་བྱེད་པ་དེ་ལྟར་ངེས་པ་དང་། རང་གི་བདག་ཉིད་དམིགས་སུ་ཡོད་པ་མི་དམིགས་པའོ། །

[Block 284]
དེ་ནི་སྦྱོར་བའི་དབང་གིས་དེ་དང་འགལ་བ་ལ་སོགས་པ་མ་རྟོགས་པ་དང་། རྟོགས་པའི་དབྱེ་བའི་སྒོ་ནས་རྣམ་པ་དུ་མར་བཤད་དེ། དེ་མ་རྟོགས་པ་དང་། དེ་དང་འགལ་བ་རྟོགས་པ་དང་། འགལ་བའི་འབྲས་བུ་རྟོགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་དབྱེ་བའི་སྦྱོར་བ་དག་གིས་སྔར་ཇི་སྐད་བཤད་པ་བཞིན་ནོ། །

[Block 285 [VERSE]]
རྒྱུ་དང་འབྲས་བུའི་དངོས་པོ་འམ། །
རང་བཞིན་ངེས་པར་འབྱེད་པ༌[^174]ལས། །
མེད་ན་མི་འབྱུང་ངེས་པ་སྟེ། །
མ་མཐོང་ལས་མིན་མཐོང་ལས་མིན། །

[Block 286 [VERSE]]
གཞན་དུ་གཞན་ནི་གཞན་དག་དང་། །
ངེས་པར་ཡོད་པའི་ངེས་པ་གང་། །
དོན་གཞན་རྒྱུ་མཚན་ཅན་གྱི་ཆོས། །
ཡིན་ན༌[^175]གོས་ལ་ཚོན་བཞིན་ནོ། །

[Block 287]
བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པ་དག་གོ། །

[Block 288]
[^176]གཞན་ཡང་།

[Block 289 [VERSE]]
ཆོས་དོན་གཞན་གྱི༌[^177]རྒྱུ་མཚན་ཅན། །
ཡིན་པར་གྱུར་ན་དེ་གཞན་ཉིད། །

[Block 290]
དེ་གྲུབ་ན་མ་གྲུབ་པའམ་རྒྱུ་ཐ་དད་པ་ནི་དེའི་རང་བཞིན་དུ་རིགས་པ༌[^178]མ་ཡིན་ནོ། །

[Block 291]
དངོས་པོ་རྣམས་ཀྱི་ཐ་དད་པའམ། རྒྱུ་ཐ་དད་པ་ནི་འདི་ཁོ་ན་ཡིན་ཏེ། ཆོས་འགལ་བ་གནས་པའམ། རྒྱུ་ཐ་དད་པ་ཡིན་ནོ། །

[Block 292]
གལ་ཏེ་དེ་དག་ཀྱང་ཐ་དད་པར་བྱེད་པ༌[^179]ཡིན་ན་གང་ཡང་གང་ལས་ཀྱང་ཐ་དད་པར་བྱེད་པ་མེད་པས་རིལ་རྫས་གཅིག་ཏུ་འགྱུར་རོ། །

[Block 293]
དེས་ན་ལྷན་ཅིག་སྐྱེ་བ་དང་འཇིག་པ་དག་དང་ཐམས་ཅད་ལ་ཐམས་ཅད་ཉེ་བར་སྦྱར་བར་འགྱུར་རོ། །

[Block 294]
དེ་ལྟ་མ་ཡིན་ན་གཅིག་ཅེས་བྱ་བ་ཉིད་དུ་མི་འགྱུར་བའམ། མིང་ཐ་དད་པར་ཟད་དེ། དོན་ཁས་བླངས་ནས་དེ་སྐད་དུ་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 295]
རྒྱུ་དོན་ཐ་དད་པ་ཉིད་མེད་ཀྱང་དངོས་པོའི་དུས་ན། མི་རྟག་པ༌[^180]ཉིད་མ་གྲུབ་པའི་ཕྱིར་དེའི་རང་བཞིན་མ་ཡིན་པར་མཚུངས་པ་མ་ཡིན་ནམ་ཞེ་ན། མི་རྟག་པ་ཉིད་ཅེས་བྱ་བ་གང་ཕྱིས༌[^181]འགྲུབ་པར་འགྱུར་པ་གཞན་ནི་འགའ་ཡང་མེད་པ་ཡིན་ཏེ། དངོས་པོ་སྐད་ཅིག་མར་གནས་པའི་ཆོས་ཁོ་ན༌[^182]མི་རྟག་པ་ཉིད་ཡིན་ནོ། །

[Block 296]
ཆོས་དང་ཆོས་ཅན་གྱི༌[^183]ཚིག་ཐ་དད་པ་ལ་ཡང་རྒྱུ་མཚན་བཤད་པར་བྱའོ། །

[Block 297]
རང་གི་རྒྱུ་ཁོ་ན་ལས་དེ་ལྟར་སྐྱེ་བའི་ཕྱིར་འདིའི་རང་བཞིན་སྐད་ཅིག་མར་གནས་པའི་ཆོས་ཉིད་དེ་ནི་མཐོང༌[^184]བཞིན་དུ་ཡང་བློ་གཞན་པ༌[^185]ཡོད་པ་དམིགས་པས་རྟག་ཏུ་དེ་ལྟར་ཡོད་པར་དགོས་པས་བསླུས་པའམ། འདྲ་གཞན་འབྱུང་བས་བསླུས་པས༌[^186]མི་རྟོགས་སོ། །

[Block 298]
སྐད་ཅིག་མ་ཐ་མ་མཐོང་བ་རྣམས་ལ་ངེས་པའི་ཕྱིར། ཕྱིས་འདི་མི་དམིགས་པས་མི་གནས་པར་རྟོགས་པའི་ཕྱིར་དེའི་ཚེ་ངེས་པའི་དུས་ཡིན་པས་མི་རྟག་པ་ཉིད་དུ་རྣམ་པར་གཞག་གོ། །

[Block 299]
འབྲས་བུ་བསྐྱེད་པའི་ནུས་པ་རྒྱུའི་དངོས་པོ་ཉིད་ཡིན་ཡང་འབྲས་བུ་མ་མཐོང་བ་རྒྱུ་མཐོང༌[^187]དུ་ཟིན་ཀྱང་དེའི་ངོ་བོ་མ་རྟོགས་པས་འབྲས་བུ་མཐོང་བས་རྟོགས་པ་བཞིན་ནོ། །

[Block 300]
དེ་ལྟ་མ་ཡིན་ན་གཞན་གྱི་རྒྱུ་མཚན་ཉིད་ཡིན་ནམ། རྒྱུ་མཚན་མེད་པ་ཅན་ཉིད་ཡིན་ཡང་རུང་སྟེ། མི་རྟག་པ༌[^188]ཉིད་དོན་གཞན་ཁོ་ནར་འགྱུར་རོ། །

[Block 301]
དེ་ལྟ་ན་ནི་དངོས་པོ་དེ༌[^189]དང་ལྡན་པར་མི་འགྱུར་ཏེ། དེ་ལ་མི་དགོས་པའི་ཕྱིར་རོ། །

[Block 302]
འོན་ཏེ་དགོས་ན་ནི་དེ་ཉིད་འདིའི་རང་གི་བདག་ཉིད་དུ་གྱུར་པའི་མི་རྟག་པ་ཉིད་ཡིན་པས་གཞན་གྱིས་ཅི་ཞིག་བྱ། རང་བཞིན་གྱིས་མི་གཡོ་བ་ནི་དོན་གཞན་དང་ལྡན་ཡང་དེའི་ངོ་བོར་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 303]
མི་རྟག་པ་ཉིད་དམ་ཆོས་གཞན་དེ་ཡང་དོན་གཞན་ལས་འབྱུང་བ་ན་རྒྱུ་ཡིན་པའམ། འབྲས་བུ་ཡིན་པ་ཞིག་ཏུ་འགྱུར་གྲང་ན། རྒྱུ་དང་འབྲས་བུ་མ་ཡིན་པ་ནི་འབྲེལ་པ་མེད་པའི་ཕྱིར། དེ་ལ་ཡོད་པར་རྗེས་སུ་དཔག་པར་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 304]
དེ་ལ།

[Block 305 [VERSE]]
ཕྱིས་འབྱུང་ཕྱིར་ན་རྒྱུ་ཉིད་མིན། །
འབྲས་བུ་ན་ཡང་ག་ལ་ངེས། །

[Block 306]
དེ་དངོས་པོ་གྲུབ་ནས་ཕྱིས་དོན་གཞན་ལས་འབྱུང་ན་ཇི་ལྟར་དེའི་རྒྱུ་ཡིན།[^190] འབྲས་བུ་ཡང་རྒྱུ་ལ་གདོན་མི་ཟ་བ་མ་ཡིན་པས་དེའི་གོ་བར་བྱེད་པའི་གཏན་ཚིགས་མ་ངེས་པ་ཉིད་ཡིན་ནོ། །

[Block 307]
དེའི་ཕྱིར་དོན༌[^191]གཞན་གྱི་རྒྱུ་མཚན་ཅན་གྱི་ཆོས་ནི་དངོས་པོ་ལ་གདོན་མི་ཟ་བར་ཡོད་པ་མ་ཡིན་པས་རྗེས་སུ་དཔག་ཏུ་མེད་དོ། །

[Block 308 [HEADING]]
## འབྲས་བུ་རྒྱུ་མེད་ན་མི་འབྱུང་བ། ^3-0

[Block 309]
འོ་ན་གལ་ཏེ་མཐོང་བ་དང་མ་མཐོང་བ་དག་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་རྟོགས་པའི་རྟེན་མ་ཡིན་ན་ཇི་ལྟར་དུ་བས་མེར༌[^192]འཁྲུལ་ལོ་ཞེས་བྱ་བར་རྟོགས་ཤེ་ན། འདི་ལྟར།

[Block 310 [VERSE]]
མེ་ཡི༌[^193]འབྲས་བུ་དུ་བ་སྟེ། །
འབྲས་བུའི་ཆོས་ཀྱི་རྗེས༌[^194]འཇུག་ཕྱིར། །

[Block 311]
དེའི་མཚན་ཉིད་ཀྱིར་གྱུར་པ་མི་དམིགས་པ་ལས་གང་དག་དམིགས་ན་དམིགས་ལ། དེ་ལས་གཅིག་མེད་ན་ཡང་མི་དམིགས་པ་གང་ཡིན་པ་དེ་ནི་དེའི་འབྲས་བུ་ཡིན་ཏེ།

[Block 312 [VERSE]]
དེ་ཡང་དུ་བ་ལས་ཡོད་དོ། །
དེ་མེད་པར་ནི་དེ་ཡོད་ན། །
རྒྱུ་དང་ལྡན་པ་ལས་འདས་འགྱུར། །

[Block 313]
ལན་ཅིག་དེ་ལྟར་མཐོང་བས་ཀྱང་འབྲས་བུ་གྲུབ་སྟེ། འབྲས་བུ་ཉིད་མ་ཡིན་ན། རྒྱུ་མ་ཡིན་པ་ལས་ལན་ཅིག་ཀྱང་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 314]
འབྲས་བུ་ཡང་རང་གི་རྒྱུ་མེད་པར་ཡོད་ན་ནི་རྒྱུ་དང་མི་ལྡན་པ་ཁོ་ནར་འགྱུར་ཏེ། གང་ཞིག་གང་མེད་པར་ཡོད་པ་དེ་ནི་དེའི་རྒྱུ་མ་ཡིན་ནོ། །

[Block 315]
མེ་མེད་པར་ཡང་དུ་བ་ཡོད་དེ།[^195] དེས་ན་དེའི་རྒྱུ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 316]
གལ་ཏེ་གཞན་གྱི་རྒྱུ་ཅན་ཡིན་པའི་ཕྱིར། རྒྱུ་མེད་པ་ཅན་ཉིད་མ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟ་མ་ཡིན་ཏེ། དེ་ལ་ཡང་མཚུངས་པའི་ཕྱིར་ཏེ། དེ་མེད་ན་ཡང་མེ་ཡོད་ན་ཡོད་པས་སོ། །

[Block 317]
ཡང་དེའམ་གཞན་ཡང་རུང་། དེ་བསྐྱེད་པའི་རང་བཞིན་མ་ཡིན་པ་ལས་ནི་ཇི་ལྟར་འབྱུང་བར་འགྱུར་ཏེ། དེའི་རང་གིས༌[^196]དེའི་རང་བཞིན་མ་ཡིན་པས་མི་བསྐྱེད་པའི་ཕྱིར་རོ།[^197] །དེ་རྒྱུ་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 318]
དེ་ཉིད་ནི་མ་ཡིན་པ་ཁོ་ན་སྟེ། དེ་དང་འདྲ་བ་འབྱུང་བའི་ཕྱིར་རོ་ཞེ་ན། མི་འདྲ་བ་ལས་འབྱུང་བ་ཇི་ལྟར་དེ་དང་འདྲ་བས༌[^198]ཡིན་ཏེ། དེ་ནི་དེ་དང་འདྲ་བ་ལ་མ་བྱུང༌[^199]བའི་ཕྱིར་དེ་དང་འདྲ་བར་འགྱུར་རོ། །

[Block 319]
མི་འདྲ་བ་ལས་དེ་དང་འདྲ་བ་འགྱུར༌[^200]ན་ནི། དེ་དག་གི་ནུས་པ་མ་ངེས་པའི་ཕྱིར་རྒྱུའི་ཐ་དད་པ་ཐ་དད་པར་བྱེད་པ་མ་ཡིན་པས། མཐའ་དག་གི་སྣ་ཚོགས་ཉིད་རྒྱུ་མེད་པ་ཅན་དུ་འགྱུར་བའམ། ཐམས་ཅད་ལས་ཐམས་ཅད་སྐྱེ་པར་འགྱུར་རོ། །

[Block 320]
དེ་ལྟ་བས་ན་རྒྱུའི་ཐ་དད་པ་དང་ཐ་དད་པ་མ་ཡིན་པ་དག་གིས་འབྲས་བུ་ཐ་དད་པ་དང་ཐ་དད་པ་མ་ཡིན་པ་དག་ཡིན་ནོ། །
--- END BLOCKS ---
