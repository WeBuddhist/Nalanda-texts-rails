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
[Block 351]
གལ་ཏེ་ཡང་རྒྱུ་ལ་སོགས་པ་ལ་འབྲས་བུའི་རང་བཞིན་ཡོད་ན། དེ་དག་ལ་ཐམས་ཅད་ཀྱི་བདག་ཉིད་ཀྱིས་ཡོད་དམ་ཆ་ཤས་ཀྱིས་སོ། །

[Block 352]
དེ་ལ་རེ་ཞིག་གལ་ཏེ་ཐམས་ཅད་ཀྱིས༌[^298]བདག་ཏུ་རྟོག་ན་རྒྱུ་དང་རྐྱེན་རྣམས་མང་པོའི་ཕྱིར་འབྲས་བུ་དུ་མས་འཇུག་ལ། དེའི་ཕྱིར་རྒྱུ་ལ་སོགས་པ་སོ་སོ་ལ་འབྲས་བུ་མེད་ལ་རྒྱུ་དུ་མས་འབྲས་བུ་གཅིག་སྒྲུབ་པ་མ་ཡིན་ཞིང་། རྒྱུ་གཅིག་གིས་བསྒྲུབ་པར་བྱ་བ་ཉིད་དུ་འགྱུར་རོ། །

[Block 353]
དེའི་ཕྱིར་གང་ལ་གནས་པ་དེ་ཉིད་ལ༌[^299]འཇུག་པའི་ཕྱིར་དེ་ལྟར་རེ་ཞིག་ཐམས་ཅད་ཀྱི་བདག་ཉིད་ཀྱི་རྒྱུ་ལ་སོགས་པ་ལ་འབྲས་བུ་མི་གནས་སོ། །

[Block 354]
ད་ནི་ཆ་ཤས་ཀྱིས་ཀྱང་མི་གནས་ཏེ། འབྲས་བུ་གཅིག་དུམ་བུར་སྐྱེ་བར་ཐལ་བར་འགྱུར་ལ། རྒྱུ་ཐ་དད་པ་ན༌[^300]ཡང་རྒྱུ་དུ་མས་འབྲས་བུ་སྐྱེད་པར་ཐལ་ལོ། །

[Block 355]
གང་ཡང་རྒྱུ་ལ་སོགས་པ་ལ་མི་གནས་ན། དེ་རྒྱུ་ལ་སོགས་པ་ལས་མི་སྐྱེ་ལ་རྩ་བའི་རབ་བྱེད་དང་པོར་ཡང་ན་དེ་རྐྱེན་ལ་སོགས་པ་ལ་མེད་ཀྱང་དེ་རྣམས་ལས་འབྱུང་ན།

[Block 356]
རྐྱེན་མིན་ལས་ཀྱང་འབྲས་བུ་ནི། །ཅི་ཕྱིར་མངོན་པར་འབྱུང་མི་འགྱུར། །ཞེས་པའི་ཚིག་ལས་སོ། །

[Block 357]
གང་གི་ཚེ་འབྲས་བུ་རྒྱུ་ལ་སོགས་པ་ལ་མི་གནས་པའི་ཕྱིར་དེ་དེ་རྣམས་ལས་མི་སྐྱེ་ལ། དེའི་ཚེ་མ་སྐྱེས་པ་ལ་ཡོད་པ་ཉིད་མི་རུང་ངོ་། །གང་ཡང་དེ་ནི་ད་ལྟར༌[^301]ན་དེས་ན་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་མེད་པས་དངོས་པོ༌[^302]ཐམས་ཅད་མྱ་ངན་ལས་འདས་པ་དང་མཚུངས་པ་རང་བཞིན་གྱིས་སྟོང་པར་གྲུབ་བོ། །

[Block 358]
འདིར་ཁ་ཅིག་གིས་སྨྲས་པ། རྒྱུ་དང་རྐྱེན་གྱི་གྲངས་བཞིན་དུ་འབྲས་བུ་རྣམས་ཡོད་པར་ཁོ་བོ་ཅག་ཁས་མི་ལེན་ལ། དེའི་ཕྱིར་འབྲས་བུ་ཡོད་པ་ཉིད་ཀྱི་སྐྱོན་ཁོ་བོ་ལ་མེད་ཅིང་མེད་པ་ཉིད་ཀྱང་བརྗོད་པར་མི་ནུས་ཏེ། ཤིན་ཏུ་མི་འདྲ་བ་མེད་པའི་ཕྱིར། བུམ་པ་དང་ཐགས་མཁན་ལྟ་བུ་སཱ་ལུའི་ས་བོན་དང་སཱ་ལུའི་མྱུ་གུ་ལ་མེད་ལ། དེ་སྐྱེད་པའི་ནུས་པ་ཡོད་པའི་ཕྱིར་དེ་ལྟར་དེ་ནི་རྒྱུ་ལ་སོགས་པ་ལ་འབྲས་བུ་ཡོད་པ་དང་མེད་པ་ཉིད་ཀྱི་བསམ་པ་སྤངས་ཏེ་རྒྱུ་ལས་འབྲས་བུ་སྐྱེའོ་ཞེས་པ་འདིས་རེ་ཞིག་སྐྱེ་བ་གྲུབ་པར་རྣམ་པར་འཇོག་གོ། །

[Block 359]
སྐྱེ་བ་གྲུབ་པར་གནས་པས་འགག་པ༌[^303]གྲུབ་པར་འགྱུར་ཏེ། གནས་པ་ལ་སོགས་པ༌[^304]ནི་མིང་ཙམ་མ་ཡིན་པ་ཁོ་ནའོ། །

[Block 360]
སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དང་ལྡན་པས་དངོས་པོ་རྣམས་རང་བཞིན་མེད་པ་མ་ཡིན་ཏེ། རང་གི་མཚན་ཉིད་དུ་ཡོད་པའི་ཕྱིར་རོ་ཞེ༌[^305]ན། སྨྲས་པ། དེ་ལྟར་སྨྲས་པ་དེ་ནི་གང་ཅུང་ཟད་ཙམ་སྟེ། ཅིའི་ཕྱིར་ན། གང་ཞིག་དངོས་པོ་རྣམས་ཀྱི་རང་གི་མཚན་ཉིད་གྲུབ་པར་འདོད་ན། དེའི་རང་གི་མཚན་ཉིད་དེ། རྒྱུ་ལ་སོགས་པ་ལ་ཡོད་པའམ་མེད་པ་ཞིག །བརྟགས༌[^306]པ་གསུམ་པ་ནི་མེད་ལ། གལ་ཏེ་ཡང་རྒྱུ་ནི་འབྲས་བུ་སྐྱེད་པའི་ནུས་པ་ཅན་དུ་ཡོད་ན། དེ་ལྟ་ན་ཡང་རྒྱུ་ལ་འབྲས་བུའི་རང་གི་མཚན་ཉིད་ཡོད་པ་མ་ཡིན་ཏེ། དངོས་པོ་རྣམས་མ་བྱུང་བ་འབྱུང་བར་ཁས་བླངས་པའི་ཕྱིར་རོ། །

[Block 361]
དེ་ལྟ་ན་ཡང་སྐྱོན་དེ་ཉིད་ལས་ལོག་པ་མ་ཡིན་ནོ། །

[Block 362]
གཞན་ཡང་།

[Block 363 [HEADING]]
### ཚིགས་བཅད་བཞི་པ། ^1-4-0

[Block 364 [VERSE]]
ཡོད་པ་ཡོད་ཕྱིར་སྐྱེ་བ་མིན། །
མེད་པ་མེད་ཕྱིར་མི་སྐྱེ་ལ། །
ཆོས་མི་མཐུན་ཕྱིར་ཡོད་མེད་མིན། །
སྐྱེ་བ་མེད་པས་གནས་འགག་མེད། །

[Block 365]
གང་ཞིག་འདི་སྐད་དུ་སྨྲ་སྟེ། ཡོད་པ་དང་མེད་པའི་བསམ་པ་སྤངས་ནས་རྒྱུ་ལས་འབྲས་བུ་སྐྱེའོ་ཞེས་བྱ་སྟེ། འདིར་སྐྱེ་བ་གྲུབ་བོ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ན་དངོས་པོར་སྨྲ་བའི་དངོས་པོ་རྒྱུ་མཚན་ནི་ཡོད་པ་དང་མེད་པའོ། །

[Block 366]
ཅིའི་ཕྱིར་དེ་གཉིས་སུ་སྨྲ་བ་སྤངས་ནས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྟོང་པར་སྨྲ་བ་བཞིན་ནོ། །

[Block 367]
དེས་ན་གང་ཞིག་རྒྱུ་ལས་སྐྱེའོ་ཞེས་བརྗོད་ན། ཅི་དེ་ཡོད་པ་སྐྱེའམ། འོན་ཏེ་མེད་པ་སྐྱེ། གལ་ཏེ་རེ་ཞིག་ཡོད་ན། དེའི་ཚེ་འབྲས་བུ་དེ་ཡོད་པའི་དངོས་པོའི་ཕྱིར་རྟག་ཏུ་ཡོད་བཞིན་པ་ལ་སྟེ། ཡོད་བཞིན་པའི་ཕྱིར་ད་ལྟ༌[^307]བའི་རྣམ་པར་ཤེས་པ་བཞིན་སྐྱེ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་སྟེ། དེ་ལྟར་རེ་ཞིག་ཡོད་པ་སྐྱེ་བར་མི་འགྱུར་ཏེ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 368]
ཡང་ན་མེད་ན་མེད་བཞིན་པའི་རང་བཞིན༌[^308]གྱི་འབྲས་བུ་ནི༌[^309]དེ་ལྟ་ན་ཡང་མེད་པའི་ཕྱིར་འབྲས་བུ་རྟག་ཏུ་ཡོད་བཞིན་པ་མིན་ལ། ཡོད་བཞིན་པ་མ་ཡིན་པའི་ཕྱིར་རི་བོང་གི་རྭ་བཞིན་སྐྱེ་བ་མེད་དོ། །

[Block 369]
དེ་ལྟ་ན་ཡང་གཉིས་ཀྱི་ཚུལ་གྱིས་སྐྱེ་བར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། ཆོས་ནི༌[^310]མི་མཐུན་ཕྱིར་ཡོད༌[^311]མིན། །གང་ཞིག་འགལ་བའི་ཆོས་དེ་ནི་མི་མཐུན་པ་སྟེ། འགལ་བའི་ཆོས་ཀྱི་དངོས་པོ་ནི་ཆོས་མི་མཐུན་པའོ། །

[Block 370]
ཡོད་པ་དང་མེད་པ་དག་ཕན་ཚུན་འགལ་བ་གང་ལ་དེ་ཡོད་པ་དེ༌[^312]ཕན་ཚུན་འགལ་བའི་ཆོས་མི་མཐུན་པའི་དངོས་པོ་ལ་གང་ཞིག་སྐྱེ་བ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 371]
སྐྱེ་བ་ཡོད་ན་ཡོད་པར་འགྱུར་གྱི་སྐྱེ་བ་མེད་པ་ལ་གནས་པ་དང་འགག་པ་མི་འཐད་དོ་ཞེས་བྱ་སྟེ། གནས་པ་དང་སྐྱེ་བ་དང་འཇིག་པ་མེད་ཅིང་། དེ་ལས་གནས་པ་ལ་སོགས་པའི་ཚིག་དོན་གྱིས་སྟོང་པར་གྲུབ་ལ། གནས་པ་དང་སྐྱེ་བ་དང་འཇིག་པ་དང་བྲལ་བའི་དངོས་པོ་རྣམས་རང་གི་མཚན་ཉིད་ཡོད་པར་ག་ལ་འགྱུར་ཞེས་བྱ་སྟེ། དངོས་པོ་རྣམས་མྱ་ངན་ལས་འདས་པ་དང་མཚུངས་པར་རང་བཞིན་མེད་པར་གྲུབ་བོ། །

[Block 372]
འདིར་སྨྲས་པ། གལ་ཏེ་ཡང་དེ་ལྟར་ཡོད་པ་ལས་སྐྱེ་བའམ་མེད་པ་ལས་སྐྱེ་ཞེས་སྨྲ་བར་མི་ནུས་ཀྱང་དེ་ལྟ་ན་ཡང་སྐྱེའོ་ཞེས་བྱ་བ་འདི་ནི་རེ་ཞིག་སྐྱེ་བོ་བ་ལང་རྫི་མོའི་བར་ལ་གྲགས་པར་ཡོད་ལ། དེའི་ཕྱིར་སྐྱེ་བ་ལ་སོགས་པ་ཡོད་པའོ་ཞེས་བྱ་ལ་དེ་ཡོད་པས་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ཡོད་དོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་བསྐྱེད་པ་ཞེས་བྱ་བ་གཟུགས་ལ་སོགས་པའི་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ཡོད་ན་དེ་ལྟར་འགྱུར་ལ་འོན་ཀྱང་མེད་དེ་ཅིའི་ཕྱིར་ན་འདིར་བསྐྱེད་བྱ་ཅུང་ཟད་ཡོད་ན། དེ་སྐྱེད་པས༌[^313]ཡོད་པར་འགྱུར་གྱི། བསྐྱེད་བྱ་ཅུང་ཟད་ཀྱང་མེད་ལ། སྐྱེས་པ་དང་མ་སྐྱེས་པ་དང་སྐྱེ༌[^314]བཞིན་པའི་བསྐྱེད་པ༌[^315]མངོན་པར་འདོད་པ་རྣམས་ཀྱི་སྐྱེས་པ་དང་མ་སྐྱེས་པ་ང་སྐྱེས༌[^316]བཞིན་པའི་བསྐྱེད་བྱ་ཉིད་མི་སྲིད་དོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 373 [HEADING]]
### ཚིགས་བཅད་ལྔ་པ། ^1-5-0

[Block 374 [VERSE]]
སྐྱེས་པ་གང་ཞིག་བསྐྱེད་བྱ་མིན། །
མ་སྐྱེས་དེ་ཡང་བསྐྱེད་བྱ་མིན། །
སྐྱེས་པ་དང་ནི་མ་སྐྱེས༌[^317]པའི། །
སྐྱེ་བཞིན་པ་ཡང་བསྐྱེད་བྱ་མིན། །

[Block 375]
དེ་ལ་རེ་ཞིག་སྐྱེས་པ་ནི༌[^318]ཡོད་བཞིན་པའི་ཕྱིར་རོ།[^319] །ད་ལྟར་བ་བཞིན་བསྐྱེད་བྱ་མིན་ཏེ། སྐྱེ་བར་མི་རུང་བས་སོ། །

[Block 376]
ཡང་ན་བསྐྱེད་བྱ་དེ་དེ་ལྟར་ན་སྐྱེས་པ་མ་ཡིན་པ་དེ་སྐྱེ་བ་ལ་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 377]
ཡང་ན་སྐྱེས་པ་ཡང་བསྐྱེད་བྱར་འགྱུར་ན། དེའི་ཚེ་གྲུབ་པ་ལ་སྒྲུབ་པར་འགྱུར་ལ་ནམ་ཡང་བསྐྱེད་བྱ་མ་ཡིན་པར་མི་འགྱུར་རོ་ཞེས་བྱ་སྟེ། དེ་ལྟར་རེ་ཞིག་སྐྱེས་པ་བསྐྱེད༌[^320]བྱ་མིན་ནོ། །

[Block 378]
གང་མ་སྐྱེས་པ་དེ་དངོས་པོ་མ་ཐོབ་པའི་ཕྱིར་ཅིའི་ངོ་བོ་ཡང་མ་ཡིན་ལ་གང་ཞིག་ཅིའི་ངོ་བོ་ཡང་མ་ཡིན་པ་དེ་ནི་ངེས་པར་གཟུང་བའི་ངོ་བོར་མེད་པའི་ཕྱིར་འདི་ཞེས་བྱ་བ་དེ་ལས་སྐྱེའོ་ཞེས་པའི་བྱེ་བྲག་བསྟན་དུ་མེད་པས་མ་སྐྱེས་པ་ཡང་བསྐྱེད་བྱ་མིན་ནོ། །

[Block 379]
གཞན་ཡང་གང་མ་སྐྱེས་པ་དེ་ལ་རྟེན་མེད་པས་སྐྱེ་བའི་བྱ་བ་འཇུག་པ་ཉིད་མི་སྲིད་དོ་ཞེས་བྱ་སྟེ། མ་སྐྱེས་པ་བསྐྱེད་བྱ་མིན་ནོ། །

[Block 380]
འདིར་སྨྲས་པ། མ་སྐྱེས་པ་ཉིད་བསྐྱེད་བྱ་མིན་ལ་སྐྱེས་པ་ཐམས་ཅད་ཀྱང་མ་ཡིན་ནོ། །

[Block 381]
འོན་ཀྱང་གང་གིས༌[^321]རྒྱུ་རྐྱེན་གྱི་ཚོགས་པ་ཉེ་བ་ལས་མ་སྐྱེས་པ་དེ་ཉིད་བསྐྱེད་པར་བྱ་བའོ་ཞེ་ན། སྨྲས་པ། དེ་སུ་ཞིག་གི །རྒྱུ་དང་རྐྱེན་གང་གིས་བསྐྱེད་པར་བྱ་བའི་འོ། །

[Block 382]
སླར་ཡང་སུ་ཞིག་གིས་བསྐྱེད་པར་བྱ་ན། གང་དེའི་རྒྱུ་དང་རྐྱེན་གྱིས་སོ་ཞེས་བརྗོད་པ་ན་ཕན་ཚུན་བརྟེན་པ༌[^322]ཐོབ་པར་འགྱུར༌[^323]ན་ཕན་ཚུན༌[^324]དག་མ་གྲུབ་པས་གཉི་ག་ཡང་མེད་པའི་ཕྱིར་མ་སྐྱེས་པ་བསྐྱེད་བྱ་མིན། ང༌[^325]ནི་སྐྱེས༌[^326]བཞིན་པ་ཡང་བསྐྱེད་བྱ་མིན་ཏེ། ཅིའི་ཕྱིར་ནི༌[^327]སྐྱེ་བཞིན་པ་ནི་སྐྱེས་པ་དང་མ་སྐྱེས་པའི་ཕྱིར་འདིར་སྐྱེ་བཞིན་པ་ཞེས་བྱ་བ་གང་ཞིག་ཅུང་ཟད་སྐྱེས་ལ༌[^328]ཅུང་ཟད་མ༌[^329]སྐྱེས་པའོ། །

[Block 383]
གང་དེའི་ཅུང་ཟད་སྐྱེས་པ་དེ་དེ་བཞིན་དུ་བསྐྱེད་བྱ་མ་ཡིན་ཏེ། བཤད་པའི་སྐྱོན་ཡོད་པའི་ཕྱིར་རོ། །

[Block 384]
གང་འདིའི་མ་སྐྱེས་པ་ཡང་བསྐྱེད་བྱ་མ་ཡིན་ཏེ། སྨོས་པའི་སྐྱོན་ཡོད་པའི་ཕྱིར་རོ། །

[Block 385]
སྐྱེས་པ་དང་མ་སྐྱེས་པ་ཞེས་པ་སྐྱེས་པ་པ༌[^330]དང་མ་སྐྱེས་པའི་ཕྱིར་རོ་ཞེས་པའི་དོན་ཏེ། དང་པོའི་མཐའ་ཅན་གྱི༌[^331]གཏན་ཚིགས་སུ་བསྟན་པའི་ཕྱིར་དངོས་པོ་གཅིག་ལ་སྐྱེས་པ་དང་མ་སྐྱེས་པ་དུས་གཅིག་པ་མི་སྲིད་དོ་ཞེས་བྱ་སྟེ། དེ་ལྟར་གྱུར་པའི་དངོས་པོ་མི་སྲིད་པས་བསྐྱེད་བྱ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 386]
གང་གི་ཚེ་དེ་ལྟར་སྐྱེས་པ་བསྐྱེད་བྱ་མ་ཡིན་ལ་མ་སྐྱེས་པ་ཡང་བསྐྱེད་བྱ་མ་ཡིན་ཞིང་སྐྱེས་པ་དང་མ་སྐྱེས་པའི་སྐྱེ་བཞིན་པ་ཡང་བསྐྱེད་བྱ་མ་ཡིན་པས། དེའི་ཚེ་བསྐྱེད་བྱ་མེད་པས་འདི་དག་བསྐྱེད་པར་ག་ལ་འགྱུར་ཞེས་པ་དེ་ལྟར་འགྱུར་རོ། །

[Block 387]
གང་གི་ཚེ་བསྐྱེད་པ་ཞེས་བྱ་བ་དེ་ལ་མི་སྲིད་པ་དེའི་ཚེ་སྐྱེ་བ་མེད་དོ་ཞེས་བྱ་བ་གྲུབ་བོ། །

[Block 388]
འདིར་སྨྲས་པ། གལ་ཏེ་བསྐྱེད་བྱ་མི་སྲིད་ཀྱང་དེ་ལྟ་ན་ཡང་འབྲས་བུ་སྐྱེད་བྱེད་ཀྱི་རྒྱུ་རེ་ཞིག་ཡོད་ལ། བསྐྱེད་བྱ་མེད་ན་སྐྱེད་བྱེད་ཀྱང་མི་རུང་ངོ་ཞེས་བྱ་སྟེ། དེས་ན་བསྐྱེད་བྱ་ཡང་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན།[^332] སྨྲས་པ། གལ་ཏེ་སྐྱེད་བྱེད་ཀྱི་རྒྱུ་ཉིད་ཡོད་ན་བསྐྱེད་བྱ་ཡོད་པར་འགྱུར་ལ། ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པས།

[Block 389]
[^333]

[Block 390 [HEADING]]
### ཚིགས་བཅད་དྲུག་པ། ^1-6-0
--- END BLOCKS ---
