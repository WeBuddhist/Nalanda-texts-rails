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
ཉི་མ་ནུབ་ནུབ་ཀྱི་བར་དུ་སྟོན་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 282]
དགེ་སློང་མས་ཆོས་འདྲི་བ༌[^201]ལ་མི་འཇིགས་པར་བྱ་བའི་ཕྱིར་དགེ་སློང་ལ་ཟས་དབུལ་བར༌[^202]བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མས་ཆོས་དྲི་བ་ལ་མི་འཇིགས་པར་བྱ་བའི་ཕྱིར་དགེ་སློང་ལ་ཟང་ཟིང་དབུལ་བར་བྱའོ། །

[Block 283]
རྒྱ་ཅང་དང༌[^203]ཤུར་བུ་དང་ལྕག་པོད༌[^204]དང་ཤུར་བུ་ཕྲེའུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དབུལ་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 284]
དགེ་སློང་གིས་དེ་དག་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་དག་ཅེས་བྱ་བ་ལ་སོགས་པ་གོས་འཛིན་པ་དགག་པ་དང་འབྲེལ་པའི་དོན་ལ་དམིགས་ཀྱིས་བསལ་བ༌[^205]ལྡེ་མིག༌[^206]ཀྱོག་པོ་ལ་སོགས་པ་བཟུང་ངོ་། །ཅི་ཞིག་རྗེས་སུ་བསྒྲུབ་ན་ཟས་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་སྟོན་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་དེ་ལྟར་གྱུར་པ་མ་ཡིན་པ་ལ་ཟས་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་དགེ་སློང་མ་ལ་སྟོན་ཏོ་ཞེས་སྨྲས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལྟ་བུར་གྱུར་པ་མ་ཡིན་པ་ལ་ཞེས་བྱ་བ་ནི་ཟས་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་སྟོན་པར་བྱེད་པ་པོ་མ་ཡིན་པ་ལའོ། །

[Block 285]
འདིར་བདེན་པ་ཉིད་དུ་རྣམ་པར་གཞག་པར་རིགས་པ་ཡིན་ཏེ། འདུ་ཤེས་ཙམ་ལས་ནི་མ་ཡིན་ནོ། །

[Block 286]
བརྫུན་དུ་སྨྲ་བ་བཀག་པ་ཉིད་ཀྱི་ཕྱིར་དགག་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་ཐལ་བའི་ཕྱིར་རོ། །

[Block 287]
འདིར་གཞུང་ནི་ཟས་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་དགེ་སློང་མ་ལ་སྟོན་པ་བདེན་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 288]
ཟས་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་སྟོན་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 289]
ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །གང་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མ་ཉེ་དུ་མ་ཡིན་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 290]
ཅི་ཞིག་རྗེས་སུ་བསྒྲུབ་པ་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གོས་བྱེད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་མཐར་ཐུག་ན་དངོས་གཞི་སྟེ། མདུན་རོལ་དུ་ནི་སྦྱོར་བ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 291]
གོས་འཚེམ་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 292]
ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་དང་། དགེ་སློང་མ་ཉེ་དུ་མ་ཡིན་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་འདིར་ཁས་བླངས་ནས་རྗེས་སུ་བསྒྲུབ་པ་འདིའི༌[^207]བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བ་འདི་ལ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་གོས་བྱིན་ནའོ་ཞེས་བྱ་བ་ནི་གོས་བྱིན་ནའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །ཇི་ལྟ་བུ་ཞིག་བྱིན་ཞེ་ན། དེའི་ཕྱིར་གོས་འབུལ་བ་མ་ཡིན་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་འདུན་ལ་གོས་འབུལ་བ་མ་གཏོགས་པར་སྦྱིན་པར༌[^208]བྱེད་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 293]
ཅི་འདི་ལྟ་བུར་གྱུར་པ་ཐམས་ཅད་ལ་སྦྱིན་ན་ལྟུང་བྱེད་དུ་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་བོར་རླག་བྱུང་བ་དང་། ལེགས་པར་སྨྲས་པ་དང་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་དང་། བརྗེ་བའི་ཕྱིར་མ་ཡིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དོན་འདི་རྣམས་ལ་སྦྱིན་པ་གང་ཡིན་པ་དེ་ལ་ནི་ཉེས་པ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 294]
གོས་སྦྱིན་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 295]
ལམ་བརྒྱགས༌[^209]བསྐུར་བར་བྱའོ། །

[Block 296]
རྩེ་རྒོད་དང་རྩེ་རྒོད་མོ་དང་དགེ་ཚུལ་དང་། དགེ་ཚུལ་མ་དག་གིས་སོ། །

[Block 297]
དགེ་སློང་དང་དགེ་སློང་མ་རྣམས་གཅིག་གི་ལམ་བརྒྱགས༌[^210]གཅིག་གིས་བསྐུར་དུ་རུང་ངོ་། །གཅིག་གིས་གཅིག་གི་བྱིན་ལེན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་དང་དགེ་སློང་མ་རྣམས་ལ་གཅིག་གི༌[^211]བྱིན་ལེན་ཡང་གཅིག་གིས་བྱར་རུང་སྟེ། རིགས་པ་ལས་མི་འདའ་བར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 298]
འདིར་གཞུང་ནི་དགེ་སློང་མ་རྣམས་ལ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 299]
ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་ན་བ་ལམ་དུ་དོར་བར་མི་བྱའོ། །

[Block 300]
དེ་བསྐུར་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ནད་པ་དེའོ། །

[Block 301]
དགེ་སློང་མ་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་རྣམས་ཀྱིས་ཀྱང་ལམ་དུ་དོར་བར་མི་བྱ་བ་དང་། དེ་བསྐུར་བར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 302]
འདི་ནི་མི་ནུས་པ་ཉིད་ཀྱི་ཕྱིར་དགེ་སློང་མ་རྣམས་ཀྱི་མིང་འདི་མི་བྱ་ཞེས་བྱ་བ་དོགས་པ་བསལ་བའི་དོན་དུའོ། །

[Block 303]
དེ་ལ་ཕན་ཚུན་དུ་གྲོགས་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་དང་དགེ་སློང་མ་རྣམས་ཀྱིས་སོ། །

[Block 304]
དེ་ལ་ཞེས་བྱ་བ་ནི་ནད་པ་བསྐུར་བ་ལའོ། །ཇི་ལྟར་བྱ༌[^212]ཞེ་ན། དེའི་ཕྱིར་མགོ་ལོགས་ནས་གཟུང་བས༌[^213]སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མགོ་བོའི་མཐའ་མ་ཕྱོགས་གཞན་ནས་གཟུང་བར༌[^214]བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 305]
གྲོང་དུ་ཕྱིན་པ་ཉིད་སོང་ན་ཡང་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་སྟེ། ཅི་དུས་ཐམས་ཅད་དུ་འགྲོ་བ་ལ་ཉེས་པ་མེད་དམ་ཞེ་ན། དེའི་ཕྱིར་ནད་པའི་སྨན་དང་ཟན་ལེགས་པར་སྦྱར་ཏེ་རང་བཞིན་མཐུན་པའི་ནད་གཡོག་གཅིག་དང་བཞག་ནས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཐུན་པའི་ཞེས་བྱ་བ་ནི་མཚན་འདྲ་བ་ཉིད་ཀྱིས་ཏེ་སྐྱེས་པ་ལ་སྐྱེས་པ་དང་བུད་མེད་ལ་བུད་མེད་གཞག་པར་བྱ་ཞེས་བྱ༌[^215]བའི་དོན་ཏོ། །གང་ལ་ལྷན་ཅིག་འགྲོ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་འཇིགས་པ་དང་བཅས་པའི་ལམ་ཉིད་དུ་འགྲོན་ཐབས་ཅིག་ཏུ་ཞུགས་ཤིང་ཐ་མི་དད་པར་འགྲོ་བ་ཉིད་མ་གཏོགས་པར་དགེ་སློང་མ་གཅིག་དང་ཡང་ལམ་ནས་འདའ་ཞིང་འགྲོ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འཇིགས་པ་དང་བཅས་པའི་ལམ་ཉིད་དུ་གང་ཞིག༌[^216]འགྲོན་ཐབས་ཅིག༌[^217]ཏུ་བདག་པོ་དང་བཅས་པའི་གཅིག་པའི་དངོས་པོ་མེད་པར་འགྲོ་བ་དེ་ལས་གཞན་པ་ལའོ། །

[Block 306]
དགེ་སློང་མ་གཅིག་ལ་ཡང་འགྲོ་བ་གཅིག་ཉིད་ཡོད་པ་ལ་ལམ་ལས་འདའ་བར༌[^218]བྱེད་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 307]
འདིར་དགེ་སློང་གི་འགྲོན་ཐབས་ཀྱི་ཚིག་ནི་རིགས་ཙམ་མཚོན་པར་གནས་པ་ཡིན་ནོ། །

[Block 308]
དེའི་ཕྱིར་དགེ་སློང་མ་གཅིག་ལ་ཡང་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 309]
ལམ་དུ༌[^219]འཇིགས་པ་དང་བཅས་པ་ཉིད་ལ་ཡང་བཅད་ནས་འགྲོ་བ་རིགས་པ་དང་ལྡན་པ་ཉིད་དོ། །

[Block 310]
དེ་བས་ན་འགྲོན་ཐབས་ཅིག༌[^220]ཏུ་འདོང་ཞིང་འགྲོགས་པ་ཙམ་ལ་ཉེས་པ་མེད་པ༌[^221]ཉིད་དུ་བསྟན་ནོ། །

[Block 311]
འཇིགས་པ་དང་བཅས་པ་ཉིད་ཡིན་ན་གྲོགས༌[^222]མེད་པར་ཅིག་ཅར་ཉིད་དུ་འགྲོ་བ་ཞེས་བྱ་བ་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 312]
འདིར་ཇི་སྲིད་དུ་འདས་ན་ཞེ་ན་དེའི་ཕྱིར་རྒྱང་གྲགས་རེ་རེའོ། །

[Block 313]
དེའི་ཕྱེད་རེ་རེར་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་རྒྱང་གྲགས་རེ་རེར་དངོས་གཞི་སྟེ། རྒྱང་གྲགས་ཕྱེད་ཕྱེད་དུ་ནི་ཉེས་བྱས་སོ། །

[Block 314]
བསལ་བ་ཉིད་ཀྱི་དོན་དུ་འདི་ལམ་དུ་འགྲོ་བ་ལ་རྒྱང་གྲགས་ཀྱི་བདག་ཉིད་དེ་སྦྱོར་བའི་ཕྱེད་ཅེས་བྱ་བར་གྲུབ་བོ། །

[Block 315]
དགེ་སློང་མ་དང་ལམ་དུ་ལྷན་ཅིག་འགྲོ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 316]
ཅི་ཞིག་གྲུར༌[^223]འཇུག་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་འགྲམ་གཉིས་འཇིགས་པ་དང་བཅས་པ་ཉིད་མ་གཏོགས་པར་འཐམས་ནས་ཅིག་ཅར་གྲུ་གཅིག་གི་ལམ་ལས་འདས་ཤིང་འགྲོ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཐད་ཀར་ཕ་རོལ་དུ་འགྲོ་བ་མ་གཏོགས་སོ། །

[Block 317]
ལམ་ལས་འདས་ཤིང་རྒྱང་གྲགས་རེ་རེ་དང་རྒྱང་གྲགས་ཕྱེད་དུ་ཉེས་བྱས་སུ༌[^224]ཞེས་བྱ་བར༌[^225]སྦྱར་རོ། །

[Block 318]
དགེ་སློང་མ་གཅིག་གིས་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པ་འདི་ལ་དོན་གྱིས་གསུམ་པར༌[^226]འགྱུར་བ་དང་ལྷན་ཅིག་ཏུ་འདི་དོན་གྱིས་ཐོབ་པའོ། །

[Block 319]
འགྲམ་གཉིས༌[^227]འཇིགས་པ་དང་བཅས་པ་ཉིད་ལས་གང་ཞིག་འདའ་ཞིང་འགྲོ་ནའོ། །

[Block 320]
འཐམས་ནས་དེ་མ་གཏོགས་པར་དགེ་སློང་མ་དང་ལྷན་ཅིག་ཏུ་དེའི་ཕྱིར་ཞུགས་པ་ན་ཡོ་བ་དང་གཏིབ་ཆད་པ་དང་རྦ་ཀློང་དང་ལས་བཟུར་བ་དང་རུ་སྐྱ་དང་གདོས་པ་ཆག་པ་དང་རུ་སྐྱ་འཛིན་པའི་དབང་གིས་འཇུག་པ་གཞན་དུ༌[^228]སོང་བ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡོ་བ་ལ་སོགས་པ་ལས་བཟུང་བའི་དབང་གིས་རུ་སྐྱ་དང་གདོས་པའི་དབང་ངམ། རུ་སྐྱ་འཛིན་པའི་དབང་གིས་ཐད་ཀར་ཕ་རོལ་དུ་འགྲོ་བའི་དོན་དུ་ཞུགས་པ་ཡོད་པ་ལས་འཇུག་པ་གཞན་དུ་སོང་བ་ལ་ཉེས་པ་མེད་དོ། །
--- END BLOCKS ---
