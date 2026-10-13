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
དཀྱིལ་འཁོར་ཡང་གང་དུ་ཞེ་ན།

[Block 352 [VERSE]]
དཀྱིལ་འཁོར་ལུས་དང་བྷ་གར་སྦྱོར། །
རྒྱལ་བའི་ཡུམ་གྱི་ཚུལ་འཆང་བའོ། །

[Block 353]
ཞེས་པ་དཀྱིལ་འཁོར་ལུས་སུ་བྱས་པ་ནི། །གསང་བའི་དབང་བཞིན་ནོ། །

[Block 354]
བྷ་ག་ལ་ནི་རྩ་དང་བྱང་ཆུབ་སེམས་རྟེན་དང་བརྟེན་པའི་ཚུལ་དུ་དཀྱིལ་འཁོར་རོ། །

[Block 355]
དེར་འཇུག་པའི་རིམ་པ་ཡང་།

[Block 356 [VERSE]]
གང་ཞིག་རས་དམར་པོ་གཡོགས་ནས། །
གསོལ་གདབ་སྡོམ་པ་སྦྱིན་པ་དང་། །
གང་ཞིག་ལུས་ཀྱི་དཀྱིལ་འཁོར་བསྟན། །
སྦྱོར་བ་ཡེ་ཤེས་དབབ་པ་དང་། །

[Block 357 [VERSE]]
མཐོང་བ་དྲི་བ་ལ་སོགས་པ། །
སྦྱོར་བ་འདིས་ནི་འཇུག་པར་བྱེད། །

[Block 358]
ཅེས་པ་འདི་ནི་བཤད་ཟིན་ཏོ། །

[Block 359]
འདིའི་ཡང་སྔོན་དུ་འགྲོ་བའི་རིམ་པ་གང་ཡིན་ཞེ་ན། གང་གིས་རིག་མ་སྦྱང་བ་དང་།

[Block 360 [VERSE]]
བསླང་དང་བྱིན་གྱིས་བརླབ་ལ་སོགས། །
སྦྱོར་བ་འདས་པ་ཇི་བཞིན་ཏེ། །
གང༌[^188]གིས་གསང་བའི་པདྨ་ནས། །
གླང་པོའི་ལག་པས་རྩ་རྣམས་བསླང་། །

[Block 361 [VERSE]]
གང་གིས་ནམ་མཁའ་གང་གྱུར་ནས། །
སྦྱོར་བ་བཟློག་པའི་བདག་ཉིད་ཅན། །
དགའ་བ་ལ་སོགས་རིམ་གྱིས་སྐྱེ། །

[Block 362]
ཞེས་པ་འདི་ནི་བཤད་ཟིན་ཏོ། །

[Block 363 [VERSE]]
འདིའི་རྟགས་ཀྱང་གང་ཡིན་ཞེ་ན། །
སྨིག་རྒྱུ་དུ་བ་སྲིན་བུ་མེ། །
མར་མེ་མཁའ་སྣང་རྣམ་པ་ལྔ། །

[Block 364]
ཞེས་པ་དབབ་པ་དང་བཟློག་པའི་དུས་སུ། །ལས་དང་པོ་པས་ནི་སྨིག་རྒྱུ་ལྟ་བུའོ། །

[Block 365]
གཉིས་པ་ལ་ནི་དུ་བ་ལྟ་བུ་འབྱུང་ངོ་། །

[Block 366]
གསུམ་པ་ལ་ནི་སྲིན་བུ་མེ་ཁྱེར་ལྟ་བུ་འབྱུང༌[^189]ངོ་། །

[Block 367]
བཞི་པ་ལ་ནི་མེ་ལྟ་བུ་འབྱུང་ངོ་། །

[Block 368]
ལྔ་པ་ལ་ནི་མཁའ་སྣང་ལྟ་བུ་འབྱུང་ངོ་། །

[Block 369]
དེ་བས་ན།

[Block 370 [VERSE]]
མཁས་པས་རྟགས་ལ་བརྟེན་ནས་ནི། །
བླ་མེད་དངོས་གྲུབ་འགྲུབ་པར་བྱེད། །

[Block 371]
ཅེས་འབྱུང་བ་ལྟ་བུའོ། །

[Block 372]
འོ་ན་འདིའི་བརྡ་ཡང་གང་ཡིན་ཞེ་ན།

[Block 373 [VERSE]]
སྦོམ་པོས་དབང་མོ་མནན་པ་ནི། །
གསུམ་པའི་བརྡ་རུ་ཤེས་པར་བྱ། །

[Block 374]
ཞེས་པ་ལ་སྦོམ་པོ་ནི་མཐེ་བོའོ། །

[Block 375]
དབང་མོ་ནི་སྲིན་ལག་གོ། །

[Block 376]
གང་གིས་དེ་མནན་པ༌[^190]ནི་དེའི་བརྡའོ། །

[Block 377]
གཞན་ཡང་། གང་གིས་གཡས་པའི་སོར་མོ་ཡིས།[^191] །

[Block 378 [VERSE]]
གཡོན་པའི་སྟེང་དུ་གཞག་པ༌[^192]ནི། །
གང་ཞིག་གསུམ་པའི་སྦྱོར་བ་ཡིས། །
ཐབས་མཆོག་འདི་ཡིན་གཞན་དུ་མིན། །

[Block 379]
ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 380]
འདིའི་དུས་ཀྱི་བསམ་གཏན་ཇི་ལྟར་བྱ་ཞེ་ན།

[Block 381 [VERSE]]
བསྐྱོད་པའི་སྟོབས་ཀྱིས་མེ་སྦར་བས། །
བདེ་ཆེན་ས་བོན་འགུགས་པའོ། །

[Block 382]
ཞེས་པ་གང་གིས་རིག་མ་དང་གཉིས་སུ་མེད་པར་བྱས་ཏེ། ལག་པ་སྟེང་འོག༌[^193]འདོད་ཆགས་ཀྱི་ཆོས་དང་། ལྟེ་བ་ནས་མེ་སྦར་བའི་སྟོབས་ཀྱིས༌[^194]བདེ་བ་ཆེན་པོའི་གནས་ནས་བྱང་ཆུབ་ཀྱི་སེམས་དབབ་སྟེ། དགའ་བ་བཞི་རིམ་གྱིས་སྐྱེ་བ་ནི་གང་གི་སྦྱོར་བ་བྱེད་པ་སྟེ་འདི་ནི་དགོས་པའོ། །

[Block 383]
འོ་ན་ནུས་པ་ཅི་ཡོད་ཅེ་ན།

[Block 384 [VERSE]]
སེམས་ཀྱི་དྲི་མ་འཁྲུ་བ་དང་། །
སྡིག་པ་དག་པ་ནུས་པའོ། །

[Block 385]
ཞེས་པ། ཤེས་རབ་ཡེ་ཤེས་ཀྱི་ནུས་པའང་སེམས་ཀྱི་དྲི་མ་འཁྲུ་བར་བྱེད་པའོ། །

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
--- END BLOCKS ---
