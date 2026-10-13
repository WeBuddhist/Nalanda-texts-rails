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
[Block 421]
འོ་ན་འདིའི་གླེང་གཞི་འང་གང་ཡིན་ཞེ་ན།

[Block 422 [VERSE]]
གང་ཞིག་གསང་བའི་ཡི་གེ་ལ། །
མཐོང་མེད་དུས་ལས་བསླང་གྱུར་ནས། །
ཡི་གེ་རང་བཞིན་མེད་གསུངས་པ། །
འདི་ནི་བཞི་པའི་གླེང་གཞི་ཡིན། །

[Block 423]
ཞེས་པ།

[Block 424 [VERSE]]
གང་གི༌[^207]འཁོར་ན་གནས་པ་གང་ཞིག་གིས། །
རང་བྱུང་ཡི་གེ་མཐོང་བའི་སྐལ་བ་མེད། །

[Block 425]
ཅེས་གསུངས་པ་དང་བཅས་ནས་ངུས་པ་དང་། རིགས་དྲུག་པ་རྡོ་རྗེ་འཆང་གིས་བརྒྱལ་བ་བསླང་སྟེ། ཡི་གེ་ཐམས་ཅད་དབེན་པ་ཉིད་དང་། སྟོང་པ་ཉིད་དང་། ཞི་བ་ཉིད་དང་། གྱ་ནོམ་པ་ཉིད་ལ་སོགས་པ་བསྟན་པ་ནི་གླེང་གཞིའོ། །

[Block 426]
གནས་ཀྱང་གང་ཡིན་ཞེ་ན།

[Block 427 [VERSE]]
མི་རྟོག་རྟོག་བྲལ་འདུས་མ་བྱས། །
རྒྱལ་བ་ཐམས་ཅད་རྟེན་ཕྱིར་གནས། །

[Block 428]
ཞེས་པ་ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས་རྣམ་པར་དག་པ་འདི་ལ་གང་དང་གང་གིས་བརྟེན་པར་བྱ་བ་ཡིན་པས་གནས་སུ་ཤེས་པར་བྱའོ། །

[Block 429]
དེའི་དུས་ཀྱང་གང་ཞེ་ན།

[Block 430 [VERSE]]
བླང་དོར་མེད་པ་དུས་ཀྱི་མཆོག །
སྔོན་མེད་ཕྱིས་མེད་གདོད་ནས་བྱུང་། །

[Block 431]
ཞེས་པ་ཆོས་ཐམས་ཅད་གཅིག་དང་དུ་མ་དང་བྲལ་བ་རང་བཞིན་གྱིས་རྣམ་པར་དག་པ་གང་གིས་རྟོགས་པ༌[^208]དེ་ནི་འདས་པའི་དུས་ཀྱང་མི་དམིགས། མ་འོངས་པ་དང་། ད་ལྟར་གྱི་དུས་མི་དམིགས། དུས་གསུམ་པོ་བླང་བ་མ་ཡིན། །སྤང་བ་མ་ཡིན། གཉིས་ཀ་མ་ཡིན་པའང་མ་ཡིན་པ་འདི་ནི་ཡང་དག་པའི་དུས་སོ། །

[Block 432]
གང་གིས་བདེ་སྟེར་སློབ་དཔོན་མཆོག །ཅེས་པ་ནི་གང་ལ་གང་གིས་བདེ་བ་སྟེར་བ་འདི་ནི་སློབ་དཔོན་ཏེ་ཀླུ་སྒྲུབ་བཞིན་ནོ། །

[Block 433]
མི་རྟོག་པའི་ཤེས་པས་ཀྱང་གང་ཞིག་གི༌[^209]རགས་པ་དང་ཕྲ་བའི་རྟོག་པ་བཟློག་ནས་དེས་བདེ་བ་ཐོབ་པར་བྱེད་པའི་ཕྱིར་དེ་ལ་དེ༌[^210]སྐད་ཅེས་བྱའོ། །ཅིའི་ཕྱིར་སློབ་མར་བརྟག་ཅེ་ན།

[Block 434 [VERSE]]
ཀུན་གྱི་ཐུགས་ཀྱི་སྲས་གྱུར་ཕྱིར། །
བསླབ་པར་བྱ་བའི་སློབ་མ་ཡིན། །

[Block 435]
ཞེས་པ་གང་ལ་ཡེ་ཤེས་དྲི་མ་མེད་པ་ཡོད་པ་དེ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྲས་ཡིན་ཏེ། རྡོ་རྗེ་ཆོས་བཞིན་ནོ། །

[Block 436]
འདིའི་རྒྱུའང་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 437 [VERSE]]
ཏིང་འཛིན་ཤེས་རབ་ཁྱད་པར་ཅན། །
མི་རྟོག་ཤེས་པ་བསྐྱེད་ཕྱིར་རྒྱུ། །

[Block 438]
ཞེས་པ་ནི་གོང་དུ་བཤད་ཟིན་ཏོ། །

[Block 439]
དཀྱིལ་འཁོར་ཡང་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 440 [VERSE]]
སྙིང་པོ་ལེན་པར་བྱེད་པའི་ཕྱིར། །
ཡེ་ཤེས་རྒྱུར་བཅས་དཀྱིལ་འཁོར་རོ། །

[Block 441]
ཞེས་པ་སྙིང་པོ་ནི་སངས་རྒྱས་ཀྱི་སྐུ་དང་ཡེ་ཤེས་ཏེ་འདིས་ལེན་པར་བྱེད་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 442]
གང་གིས་སྔོན་དུ་གྱུར་པ་ཡིས།[^211] །སྦྱོར་བ་འདི་རུ་ཞུགས་པ་ཡིན། །ཞེས་པ་གང་གིས་རྟོག་པ་ཐམས་ཅད་དང་བྲལ་བའི་ཡེ་ཤེས་ཁོང་དུ་ཆུད་པ་དེ་ནི་དཀྱིལ་འཁོར༌[^212]དུ་ཞུགས་པའོ། །

[Block 443 [VERSE]]
གང་གིས༌[^213]ཟབ་པའི་མན་ངག་རྣམས། །
མཉན་པ་དང་ནི་བསམ་པ་དང་། །
བསྒོམ་པ་ཡི་ནི་རིམ་གྱིས་ཀྱང་། །
བླ་མེད་དཀྱིལ་འཁོར་ནང་དུ་འཇུག །

[Block 444]
ཅེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 445]
འདིའི་སྔོན་དུ་འགྲོ་བའང་གང་ཡིན་ཞེ་ན།

[Block 446 [VERSE]]
དབང་གསུམ་མན་ངག་དང་བཅས་དང་། །
སློབ་པ་སྔོན་དུ་འགྲོ་བ་ཡིན། །

[Block 447]
ཞེས་པ་བུམ་པ་དང་། གསང་བ་དང་། ཤེས་རབ་ཡེ་ཤེས་དང་། དེ་དང་འབྲེལ་བའི་མན་ངག་ནི་སྤྱིའི་སྔོན་དུ་འགྲོ་བའོ། །

[Block 448]
གང་གིས་ཟབ་མོའི་མན་ངག་འདི་ནི་བྱེ་བྲག་གི་སྔོན་དུ་འགྲོ་བ་ཡིན་ནོ། །

[Block 449]
དབང་བསྐུར་བའི་རིམ་པ་ནི།

[Block 450 [VERSE]]
རིམ་དང་རིམ་མིན་གཉིས་དང་བྲལ། །
འདི་ནི་དོན་དམ་རིམ་པའོ། །

[Block 451]
ཞེས་པ་རིམ་པ་གང་དང་གང་གི་རྣམ་པ་དང་བྲལ་ཞིང་རིམ་པ་མེད་པའང་དམིགས་སུ་མེད་དེ་འདི་ནི་ཡང་དག་པའི་རིམ་པའོ། །

[Block 452]
ལོག་པའི་རྟོག་པ་ཀུན་དང་བྲལ། །ཐམས་ཅད་སྤྲོས་པ་ཉེ་བར་ཞི། ཞེས་པ་གཟུགས་ལ་སོགས་པ་ཐམས་ཅད་ཀྱི་སྤྲོས་པ་དང་བྲལ་ནས་རྣམ་པར་རྟོག་པ་གང་ལའང་མི་གནས་པར་བྱེད་པ་འདི་ནི་ཐབས་སོ། །

[Block 453 [VERSE]]
སྟེང་སོགས་རང་བྱུང་ཡི་གེ་ལ། །
འབར་བའི་མེ་ཡིས་བཞུ༌[^214]བྱས་ཏེ། །
གང་ཞིག་དགའ་བར་རབ་ཏུ་སྐྱེ། །
རྟོག་བྲལ་ཐབས་ཀྱི་དམ་པའོ། །

[Block 454 [VERSE]]
གང་ཞིག་དབང་གསུམ་རྫོགས་བྱས་ནས། །
མཚན་ལྡན་བུ་མོ་བསྟེན་པ་དང་། །
འདི་ལས་བདེ་བ་མྱོང་བའང་། །
རྒྱལ་བས་ཐབས་སུ་བཤད་པ་ཡིན། །

[Block 455]
ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 456 [VERSE]]
འདིའི་རྫས་ཀྱང་གང་ཡིན་ཞེ་ན། །
རྒྱུ་ལ་བྱང་ཆུབ་སེམས་ཡིན་ཏེ། །
རྟེན་མེད་རྫས་རྣམས་ཀུན་དང་བྲལ། །

[Block 457]
ཞེས་པ་ནི་གོ་སླའོ། །

[Block 458 [VERSE]]
གང་གིས་གང་ལ་མི་གཡོ་བར། །
དེ་ཉིད་ལ་དམིགས་དགོས་པ་ཡིན། །

[Block 459]
ཞེས་པ་ནི་གང་གིས་རྟོག་པ་ཐམས་ཅད་སྤངས་ཏེ། མི་རྟོག་པའི་ཤེས་པ་འདི་ལ་ཡང་དང་ཡང་དུ་སེམས་གཏོད་པ་ནི་འདིའི་དགོས་པའོ། །གང་གིས་གང་ལ་གནས་པ་འདིའི་རྟགས་ཀྱང་གང་ཞིག་ཡིན་ཞེ་ན། ནམ་མཁའ་བཞིན་དང་མྱུར་བ་དང་། དལ་དང་མི་གཡོ་ལ་སོགས་རྟགས། ཞེས་པ་ལས་དང་པོ་པ་ལ་བརྟེན་པ༌[^215]གཞན་འགགས་ཏེ་སྟེང་གི་ནམ་མཁའ་བཞིན་དུ་འགྱུར་རོ། །

[Block 460]
ཁ་ཅིག་ལ་ནི་སྨིག་རྒྱུ་བཞིན། །ཞེས་པ་མྱུར་ལ་རྟོག་པ་མེད་པ་འབྱུང་ངོ་། །ཁ་ཅིག་ལ་ནི་དལ་བ་དང་མི་གཡོ་བ་ལ་རྟོག་པ་མེད་པར་འབྱུང་བ་འདི་ནི་རྟགས་སོ། །
--- END BLOCKS ---
