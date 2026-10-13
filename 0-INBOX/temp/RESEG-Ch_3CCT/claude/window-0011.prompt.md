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
[Block 386]
གཞན་ཡང་།

[Block 387 [VERSE]]
ས་ལ་མངོན་དུ་ཕྱོགས་པ་དང་། །
འོག་མའི་སྡིག་པ་སྦྱོང་བ་དང་།
གོང་དང་གོང་ལ་གནས་བྱེད་པ། །
འདི་ནི་ནུས་པ་ཞེས་སུ་བཤད། །

[Block 388]
ཅེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 389]
འོ་ན་དེ་ལ་མན་ངག་བསྟན་པར་བྱ་བ་གང་ཡིན་ཞེ་ན།

[Block 390 [VERSE]]
འཁོར་ལོ་ཕོ་ཉའི་སྦྱོར་བ་རྣམས། །
མཁས་པས་གང་འཕྲོད་དེ་ལ་བསྟན། །

[Block 391]
ཞེས་པ་འདི་ནི་འཁོར་ལོ་ལ་སོགས་པ་གང་ཞིག་གིས་སྣོད་བརྟགས་ཏེ། དེ་ལ་དེ་དང་འཕྲོད་པའི་མན་ངག་སྦྱིན་པར་བྱའོ། །

[Block 392]
འདི་ལྟ་སྟེ་འཁོར་ལོ་གཅིག་དང་གཉིས་དང་བཅུ་དང་བཅུ་དྲུག་གི་བར་དུ་དང་། ཕོ་ཉ་མོའི་རིགས་དུ་མ་ལ་བརྟེན་ནས། བྱང་ཆུབ་སེམས་ཀྱི་བདེ་བ་ཉམས་སུ་མྱོང་བར་བྱེད་པ་འདི་ལྟ་བུའི་མན་ངག་བསྟན་པར་བྱའོ། །

[Block 393]
དེ་འང༌[^195]ཚོགས་གང་དང་འབྲེལ་པ་ཡིན་ཞེ་ན། འདི་ཡིས༌[^196]ཟབ་པའི་ཚོགས་རྣམས་ལ། བརྟེན་ནས་ཡེ་ཤེས་སྐྱེ་བ་ཡིན། །ཞེས་པ་ཟབ་པའི་ཚོགས་ནི་རིག་མ་ལ༌[^197]བརྟེན་པ་སྟེ། འདི་ཡིས་དེའི་དགའ་བ་ལ་སོགས་པ་ཇི་བཞིན་དུ་འབྱུང་བའི་ཚོགས་ཀྱི་མན་ངག་བརྟེན་པར༌[^198]བྱའོ། །

[Block 394]
འོ་ན་དངོས་གྲུབ་གང་དང་འབྲེལ་ཞེ་ན། །

[Block 395 [VERSE]]
གསུམ་པ་ལ་ནི་མཆོག་འགྲུབ་པ། །
གང་ཞིག་འདི་ཡིས་བྱེད་པ་ཡིན། །

[Block 396]
ཞེས་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་དང་མན་ངག་ཏུ་འབྲེལ་པ་འདི་ནི་འབྲས་བུ་མཆོག་འགྲུབ་པ༌[^199]དང་། བླ་ན་མེད་པ་འགྲུབ་པར་བྱེད་པའོ། །

[Block 397]
དེ་འང་རྣལ་འབྱོར་གང་དང་འབྲེལ་བ་ཡིན་ཞེ་ན།

[Block 398 [VERSE]]
གང་ཞིག་འདི་ལ་རྟག་གནས་པ། །
ཉེ་བས་རྫོགས་པའི་རྣལ་འབྱོར་རོ། །

[Block 399]
ཞེས་པ་གང་ཞིག་རྫོགས་པའི་རིམ་པ་དང་ཉེ་བས་འདི་ནི་རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་རོ། །

[Block 400]
དེའང་རྒྱུད་གང་དང་འབྲེལ་པ་ཡིན་ཞེ་ན། །

[Block 401 [VERSE]]
འདི་ཡིས་ཟབ་པ་སྟོན་པ་ཡི། །
རྒྱུད་རྣམས་ཀུན་ལ་བརྟེན་པར་བྱ། །

[Block 402]
ཞེས་པ་གང་ཞིག་གིས་འདི་ལ་གནས་ནས་འདི་ཐོབ་པར་འདོད་པས། འདི་ཉེ་བར་སྟོན་པའི་རྒྱུད་རྣམས་ལ་བརྟེན་པ་དང་གནས་པར་བྱའོ། །

[Block 403 [VERSE]]
འདི་ལ་གནས་པའི་གང་ཟག་གིས། །
ཐབས་དང་ཤེས་རབ་ལ་སོགས་པ། །
ཟབ་པ་སྟོན་པའི་རྒྱུད་རྣམས་ལ། །
བརྟེན་དང་མཉན༌[^200]དང་བཤད་པར་བྱ། །

[Block 404]
ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 405]
དེ་ལྟར་ཤེས་རབ་ཡེ་ཤེས་དབང་བསྐུར་བ་རྒྱས་པར་བཤད་ནས། །ད་ནི་བཞི་པ་བཤད་པར་བྱ་སྟེ། དེ་ལ་བཞི་པའི་ངོ་བོ་གང་ཡིན་ཞེ་ན།

[Block 406 [VERSE]]
གང་ཞིག་བཞི་པའི་ངོ་བོ་ནི། །
རྣམ་པར་མི་རྟོག་ཡེ་ཤེས་སོ། །

[Block 407]
ཞེས་པ་དབང་བཞི་པའི་ངོ་བོ་ནི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཏེ། ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་བསྐུར་བའི༌[^201]འབྲས་བུར་གྱུར་པ་གང་ཡིན་པ་དེ་བཞི་པའོ། །

[Block 408]
འདིའི་དབྱེ་བའང་དུ་ཞིག་ཅེ་ན། རྟེན་ཅན་དང་ནི་རྟེན༌[^202]མེད་ཀྱི།[^203] །བཞི་པའི་དབང་ནི་གཉིས་སུ་ཤེས། །ཞེས་པ་གང་རིག་མ་དང་མ་བྲལ་བའི་དུས་ན་ཡེ་ཤེས་སྐྱེས་པ་དེ་ནི་རྟེན་ཅན་གྱི་བཞི་པའོ། །

[Block 409]
རྟེན་མེད་ཀྱི་བཞི་པ་ནི་རིག་མ་ལ་བརྟེན་པའི་ཕྱིས་གང་གི༌[^204]མན་ངག་ལས་སྐྱེས་པའི་ཡེ་ཤེས་ཏེ།

[Block 410 [VERSE]]
འདི་ལྟར་གཉིས་པ་ཁོ་ནའོ། །
འདི་ཅིའི་ཕྱིར་བཞི་པ་ཞེ་ན།
གང་དུ་གསུམ་པ་ལས་གཞན་ཕྱིར། །
དེ་ནི་བཞི་པའི་དབང་ཞེས་གྲགས། །

[Block 411]
ཞེས་གསུམ་པ་ལས་འདས་པའི་ཕྱིར་རོ། །

[Block 412 [VERSE]]
བཞི་པ་དང་ནི་མཐར་ཐུག་པ། །
མཆོག་དང་བླ་མེད་རྣམ་གྲངས་སོ། །

[Block 413]
ཞེས་པ་གསུམ་པ་ལས་འདས་པ་ཉིད་དང་། ཁྱད་པར་ཅན་ཡིན་པའི་ཕྱིར་དང་། གོང་ན་མེད་པ་ཉིད་འདི་ནི༌[^205]རྣམ་གྲངས་སོ། །

[Block 414]
འོ་ན་ཆོས་གང་དུ༌[^206]དང་ལྡན་ཞེ་ན། གང་ཞིག །

[Block 415 [VERSE]]
སངས་རྒྱས་ཡོན་ཏན་ཐམས་ཅད་དང་། །
ལྡན་པ་འདི་ནི་བཞི་པའི་དབང་། །

[Block 416]
ཞེས་བཤད་པ་སྤྱིའི་ཆོས་སོ། །

[Block 417]
བྱེ་བྲག་གི་ཆོས་ནི་གསལ་བ་དང་བདེ་བ་དང་མི་རྟོག་པ་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 418]
གཞན་སེལ་བ་ཞེས་བྱ་བའང་གང་ཡིན་ཞེ་ན།

[Block 419 [VERSE]]
དངོས་པོའི་རྟོག་ལས་བྱུང་བའི་ཆོས། །
ཐམས་ཅད་འདིས་ནི་སེལ་བར་བྱེད། །

[Block 420]
ཅེས་པ་གསལ་བ་ལ་སོགས་པ་འདིས་ནི་གང་ཞིག་མི་གསལ་བ་དང་། སྡུག་བསྔལ་བ་དང་། རྟོག་པ་སེལ་བར་བྱེད་དོ། །

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
--- END BLOCKS ---
