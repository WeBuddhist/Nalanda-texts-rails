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
[Block 351 [VERSE]]
བློ་ཡི་སྐྱེ་བ་གཞན་ཡིན་ནོ།[^292] །
འཕྲོ་འདུ་རང་གི་རྒྱུ་ལས་ཏེ། །
ཚད་མ་འཕྲོད་པ་འདུ་བ་ལས། །
བྱེ་བྲག་པ་རྣམས་ཀྱི་ནི་བློ། །

[Block 352]
[^293]རང་གི་རྒྱུ་ལས་སྐྱེས་པའི་འབྲས་བུའི་ཆོས་འཕྲོད་པ་འདུ་བ་དང་ཡོད་པ་ལ་སོགས་པ་ཡིན་ལ་གལ་ཏེ་འཕྲོད་པ་འདུ་བ་དེ་ལས་དབང་པོའི་བློ་སྐྱེ་བར་འདོད་ན་ནི་འཕྲོད་པ་འདུ་བ་མངོན་སུམ་དུ་འགྱུར་ལ། དེ་ནི་རྟག་པ་ཡིན་པའི་ཕྱིར་འགའ་ཞིག་ཏུ་ཡང་སྐྱེ་བ་མ་ཡིན་ནོ། །

[Block 353]
དེའི་ཕྱིར་གཉིས་ཀའི་ལྟར་ཡང་ཚད་མ་དེ་སྦྱར་བར་མི་བྱའོ། །

[Block 354]
ཅི་སྟེ་གཞན་མིན་འདི་དོན་མེད། གལ་ཏེ་བློ་དང་སྐྱེ་བ་གཞན་ཉིད་མ་ཡིན་ན་ནི་དེ་ལྟར་ན་བློ་ཉིད་མངོན་སུམ་སྟེ། དེ་བས་ན་སྐྱེ་བ་སྨོས་པ་དོན་མེད་པར་འགྱུར་རོ། །

[Block 355 [VERSE]]
སྐྱེས་བུ་རྣམ་པར་གྱུར་ནས་བློ། །
བསྐྱེད་ན་མི་རྟག་པ་རུ་འགྱུར། །

[Block 356]
གལ་ཏེ་བློ་བསྐྱེད་པར་བྱ་བའི་ཕྱིར་སྐྱེས་བུ་སྔར་གྱི་གནས་སྐབས་ལས་རྣམ་པར་འགྱུར་ཏེ་གཞལ་བྱ་ལ་འཇུག་པར་བྱེད་དོ་ཞེས་བརྗོད་ན་ནི་དེ་ལྟར་ན་སྐྱེས་བུ་མི་རྟག་པར་འགྱུར་བའི་ཕྱིར་མི་འདོད་པ་ཐོབ་པར་འགྱུར་རོ། །ཅི་སྟེ་བདག་དེ་མི་འགྱུར་ན། །དེ་ལ་ཚད་མ་ཞེས་མི་སྦྱར། །

[Block 357]
སྐྱེས་བུ་ལ་འགྱུར་བ་མེད་ན་ནི་ཚད་མ་མ་ཡིན་པའི་གནས་སྐབས་དང་འདི་ལ་ཁྱད་པར་མེད་པའི་ཕྱིར་དེ་ལས་སྐྱེས་པའི་བློ་ཚད་མར་བྱེད་པ་ནི་མི་འཐད་པ་ཉིད་དོ། །

[Block 358]
དེ་ལྟར་ན་གཞན་དག་གིས༌[^294]འདོད་པའི་མངོན་སུམ་ནི་བསྒྲུབ་པར༌[^295]དཀའོ། །

[Block 359]
ཚད་མ་ཀུན་ལས་བཏུས་པ་ལས་མངོན་སུམ་གྱི་ལེའུ་སྟེ་དང་པོའོ།། །།

[Block 360 [HEADING]]
## རང་གི་དོན་གྱི་རྗེས་སུ་དཔག་པའི་ལེའུ། ^2-0

[Block 361]
རྗེས་དཔག་རྣམ་གཉིས་ཏེ། རང་གི་དོན་དང་། གཞན་གྱི་དོན་ནོ། །

[Block 362 [HEADING]]
### རང་གི་དོན་གྱི་རྗེས་སུ་དཔག་པ། ^2-1-0

[Block 363 [HEADING]]
#### ཚུལ་གསུམ་རྟགས་ལས་དོན་མཐོང་བ། ^2-1-1-0

[Block 364]
དེ་ལྟར་རང་དོན་ནི། [^296]ཚུལ་གསུམ་རྟགས་ལས་དོན་མཐོང་བའོ། །

[Block 365]
འཆད་པར་འགྱུར་བའི་མཚན་ཉིད་གསུམ་པའི་རྟགས་ལས་རྗེས་སུ་དཔག་པར་བྱ་བའི་དོན་མཐོང་བ་དེ་ནི་རང་གི་དོན་གྱི༌[^297]རྗེས་སུ༌[^298]དཔག་གོ། །

[Block 366 [HEADING]]
#### འབྲས་བུ་སྔར་བཞིན། ^2-1-2-0

[Block 367]
འདི་ཡང་འབྲས་བུ༌[^299]སྔར་བཞིན་ཏེ། ཇི་ལྟར་མངོན་སུམ་ལས་རྟོག་པ་གཉིས་ཉིད་ལས་འབྲས་བུར་བརྗོད་པ་དེ་བཞིན་དུ་འདི་ལ་ཡང་གལ་ཏེ་གཉིས་ཀ་ཡང་རྟོག་པའི་མཚན་ཉིད་ཅན་ཡིན་ན་འདི་གཉིས་ལ་བྱེ་བྲག་ཅི་ཞིག་ཡོད་ཅེ་ན། ཡུལ་དང་ནི། ངོ་བོ་མཚུངས་མིན་དེ་གཉིས་ཀྱི། །མངོན་སུམ་དང་རྗེས་སུ་དཔག་པ་གཉིས་ཀྱི་ཡུལ་ནི་ཐ་དད་པ་སྟེ། དེའི་རྣམ་པ་དང་བྱེ་བྲག་གི་སྒོ་ནས་སོ། །

[Block 368]
རང་གི་ངོ་བོ་ཡང་ཐ་དད་པ་ཡིན་ནོ། །

[Block 369 [HEADING]]
#### གཟུང་ཐ་དད་ཕྱིར་གཉིས་སུ་དབྱེ་བ། ^2-1-3-0

[Block 370]
གལ་ཏེ་ཅིའི་ཕྱིར་རྗེས་སུ་དཔག་པ་ཁོ་ན་གཉིས་སུ་དབྱེ་ཞེ་ན། འདིའི་ཕྱིར་ཏེ། རང་གི་མཚན་ཉིད་བསྟན་བྱ་ཡིན།[^300] གཟུང་ཐ་དད་ཕྱིར། །མངོན་སུམ་དང་རྗེས་སུ་དཔག་པ་དག་ནི་རང་གི་ངོ་བོ་བཞིན་དུ་གཟུང་བར་བྱ་བ་ཡང་ཐ་དད་པ་ཡིན་ནོ། །

[Block 371]
གལ་ཏེ་མངོན་སུམ་གྱི་དོན་ལ་ཐ་སྙད་དུ་བྱེད་ན་སྒྲ་དེ་གཉིས༌[^301]ཀྱི་སྒོ་ནས་རྗེས་སུ་དཔག་པར་འགྱུར་རོ། །

[Block 372]
གལ་ཏེ་ལ་ལར༌[^302]མངོན་སུམ་གྱི་དོན་ལ་རྗེས་སུ་དཔག་པ་འཇུག་པ་མཐོང་སྟེ། དཔེར་ན་གཟུགས་ལས༌[^303]རེག་བྱ་བཞིན་ནོ་ཞེ་ན། དེ་ལྟ༌[^304]ན་ནི་མཐོང་ན་དོན་དེ་ལ་མངོན་སུམ་བཞིན་དུ་རྗེས་སུ་དཔག་པ་ཞུགས་པ་ནི་མ་ཡིན་ནོ།[^305] །

[Block 373]
གང་གི་ཕྱིར་ཞེ་ན། དེ་ལས་གཞན། དེ་ལས་གཞན་ཞེས་བྱ་བ་ནི། སྔོན་མཐོང་བ་ཞུགས་པའི་རྒྱུ་ལས་རེག་བྱ་རྗེས་སུ་དཔོག་པ༌[^306]སྟེ། འདི་ལྟར་གཟུགས་དེ་ཉིད་མངོན་སུམ་གྱི་རྣམ་པ་དང་བྲལ་ནས་གཟུགས་ཀྱི་སྤྱི་ལ་རེག་བྱའི་སྤྱིའི་རྗེས་སུ་དཔོག་པ་ཡིན་ནོ། །

[Block 374]
མངོན་སུམ་དུ་བྱས་པའི་རེག་པར་བྱ་བའི་བྱེ་བྲག་ནི་བསྟན་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་ཚད་མ་གཉིས་ཀྱི་སྤྱོད་ཡུལ་གཅིག་པར་གྱུར་པ་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 375]
གལ་ཏེ་འདི་ལྟར་མཐོང་བ་ལ་སོགས་པ་ལ་མཐོང་བ་ལ་སོགས་པའི་ཐ་སྙད་དུ་བྱེད་པའི་ཕྱིར་ཇི་ལྟར་མངོན་སུམ་བསྟན་པར་བྱ་བ་ཡིན་ཞེ་ན། འདི་ལ་འགལ་བ་ཡོད་པ་མ་ཡིན་ཏེ། དེར་ཡང་།

[Block 376 [VERSE]]
མཐོང་སོགས་ཉིད་སྒོ་ནས་བསྟན་པ། །
རང་གི་ངོ་བོ་བརྗོད་པ་མིན།[^307] །

[Block 377]
མཐོང་ངོ་། །ཐོས་སོ། །ཤེས་སོ་ཞེས་བྱ་བའི་རྒྱུ་མཚན་གྱི་སྒྲའི་སྒོ་ནས་དོན་དེ་རྣམས་བརྗོད་པ་ཡིན་གྱི་རང་གི་ངོ་བོའི་སྒོ་ནས་ནི་མ་ཡིན་ཏེ། འདི་ལྟར་མིག་གི་རྣམ་པར་ཤེས་པས་མཐོང་བར་འགྱུར་བའི་དོན་ལ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་སྔོན་པོ་ཇི་ལྟ་བར་ཤེས་སོ། །

[Block 378]
འདི་སྔོན་པོའོ་ཞེས་བརྗོད་པར༌[^308]བྱེད་དོ། །

[Block 379]
དེར་ཡང་།

[Block 380]
མིང་ལས་ཤེས་ཕྱིར་རྣམ་པ་གཞན། །བསྟན་བྱ་ཡིད་ཀྱི་རྣམ་པ་གཉིས། །

[Block 381]
གང་གི་ཕྱིར་མིག་གི༌[^309]རྣམ་པར་ཤེས་པས་སྔོན་པོ་མ་ཡིན་པ་ལས་ལོག་པའི་དོན་ཉམས་སུ་མྱོང་བ་ལ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཐོབ་པར་ནུས་སོ་ཞེས་ཐ་སྙད་དུ་བྱེད་པ་ལ་ཡིད་ཀྱི་རྣམ་པ་གཉིས་སོ༌[^310]ཞེས་བརྗོད་དོ། །

[Block 382]
རང་གི་མཚན་ཉིད་བསྟན་བྱ་མིན། །ཞེས་བྱས་པས་ན་རྟོགས་པར་བྱ་བའི་དོན་གྱི་བདག་ཉིད་མངོན་སུམ་གྱི་ཡུལ་ཡིན་ཞིང་སྤྱི་རྗེས༌[^311]སུ་དཔག་པའི་ཡུལ་ཉིད་དུ་མངོན་པར་བརྗོད་པས་མངོན་པར་བརྗོད་དོ། །

[Block 383]
གལ་ཏེ་འདི་ལྟར་རྗེས་དཔག་ཐམས་ཅད་སྤྱིའི་ཡུལ་ཅན་ནོ་ཞེས་ནི་བརྗོད་པར་མི་བྱ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། སྤྱི་མ་ཡིན་ལའང་མཐོང་བའི་ཕྱིར། །སྤྱི་མ་ཡིན་ལའང་ཞེས་བྱ་བ་ནི༌[^312]མཐོང་བའི་རླུང་ལ་སོགས་པའི་རང་བཞིན་རེག་བྱ་ལ་སོགས་པས་རྗེས་སུ་དཔོག་པའོ། །

[Block 384]
དེ་སྐད་དུ་ཡང་རེག་བྱ་ནི་རེག་བྱ་མཐོང་བ་རྣམས་ཀྱི༌[^313]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པས་བརྗོད་དོ་ཞེ་ན། དེ་མིན་མཚོན་བྱ་སྤྱི་ཡིན༌[^314]ཕྱིར། །རླུང་ལ་སོགས་པ༌[^315]དེ་རྗེས་སུ་དཔག་པ་ནི་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་རེག་བྱ་ལ་སོགས་པའི་ཡོན་ཏན་ཉིད་ཀྱི༌[^316]རྟེན་ཉིད་ཀྱི་ཕྱིར་མཚོན་པའི་ཕྱིར་རམ། ཡང་ན་རླུང་ལ་སོགས་པའི་རང་བཞིན་ཁྱད་པར་ཅན་དུ་རྗེས་སུ་དཔག་པ་ནི་མ་ཡིན་གྱི། གང་གི་ཕྱིར་རྫས་ཉིད་ཙམ་གྱི་སྤྱི་དེ་ལ་རེག་བྱ་ལ་སོགས་པ་རྣམས་ཀྱི་རྟེན་རྫས་ཉིད་དུ་མཚོན་པར་བྱ་བ༌[^317]ཡིན་པའི་ཕྱིར་རོ། །

[Block 385]
གལ་ཏེ་ཀུན་གྱི་རྗེས་ཐོགས་ལས། །

[Block 386]
གྲུབ་སྟེ་འདི་ལྟར་ཀུན་གྱི་རྗེས་ཐོགས་ལས་རླུང་ལ་སོགས་པའི་རང་བཞིན་རྗེས་སུ་དཔག་པར་གྲུབ་པའོ། །

[Block 387]
དེ་སྐད་དུ་ཡང་རེག་བྱ་ནི་མཐོང་བ་རྣམས་ཀྱི་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བརྗོད་དོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་ཡོད་པར་མ་གྲུབ་པའི་ཕྱིར་དང་། ལྡོག་པ་ཡང་མཚུངས་པའི་ཕྱིར་རོ། །

[Block 388]
རླུང་ལ་སོགས་པ་ཡོད་པར་གྲུབ་ན་ནི་མི་ལྡོག་པ་ཡང་སྲིད་དེ། ཡོན་ཏན་གྱི་བྱེ་བྲག་དང་འབྲེལ་པ་ལས་ཡོན་ཏན་གྱི་སྤྱི་བོར་ནས་ཡོན་ཏན་གྱི་བྱེ་བྲག་གིས༌[^318]རྫས་ཀྱི་བྱེ་བྲག་རྗེས་སུ་དཔོག་པར༌[^319]བྱེད་ལ། རེག་ན་ཡོད་པར་ནི་གྲུབ་པ་མེད་དོ།[^320] །

[Block 389]
ས་ལ་སོགས་པ་ལས་ལོག་པ་དང་ཡང་མཚུངས་པར་འགྱུར་ཏེ། ཡོན་ཏན་གྱི་བྱེ་བྲག་མ་མཐོང་ཞིང་མ་མཐོང་བ༌[^321]ཙམ་གྱིས་མཐོང་བ་ལས་ལོག་པར་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 390]
དེ་ལྟར་ཡང་རིགས་པ་མ་ཡིན་ཏེ།
--- END BLOCKS ---
