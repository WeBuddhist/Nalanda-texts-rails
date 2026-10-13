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
[Block 491]
དེའི་ཕྱིར་ཕྱིན་ཅི་ལོག་བཞི་ལས་བྱུང་བའི་མ་རིག་པ་ཡོད་ལ། ཇི་ལྟར་མ་རིག་པ་ཕྱིན་ཅི་ལོག་བཞི་ལས་བྱུང་བ་ཡོད་པ་བཞིན་དུ་འདི་ལྟར་མ་རིག་པ་ལས་བྱུང་བའི་འདུ་བྱེད་ཀྱང་འབྱུང་བར་འགྱུར་ཞིང་། ཇི་སྲིད་དུ་སྐྱེ་བ་ལས་བྱུང་བའི་རྒ་ཤིའི་བར་དུ་འབྱུང་བར་འགྱུར་རོ། །

[Block 492]
དེས་ན་རྟེན༌[^401]ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཡན་ལག་སྲིད་པས་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཡོད་དོ་ཞེ་ན། དེ་ལ་མ་རིག་པའི་དབང་དུ་བྱས་ནས་སྨོས་པ། གལ་ཏེ་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཡོད་ན། དེ་ལས་བྱུང་བ་མ་རིག་པ་ཡོད་ལ། གང་གི་ཚེ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཉིད་མ་གྲུབ་ན། དེའི་ཚེ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཡན་ལག་ཏུ་གྱུར་པ་མ་རིག་པ་འབྱུང་བར་ག་ལ་འགྱུར། གཞན་ཡང་འདིར་མ་རིག་པ་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ལས་བྱུང་ན། ཕྱིན་ཅི་ལོག་ལས་འབྱུང་བར་བརྗོད་པར་བྱ་ལ། དེ་ལས་གལ་ཏེ་ཕྱིན་ཅི་ལོག་ཡོད་ན་དེའི་ཚེ་དེ་ལས་བྱུང་བའི་མ་རིག་པ་ཡང་ཡོད་ན། ཡོད་པ་ནི་མ་ཡིན་ནོ་ཞེས་བསྒྲུབས་པའི༌[^402]ཕྱིར་གསུངས་པ།

[Block 493 [HEADING]]
### ཚིགས་བཅད་དགུ་པ། ^1-9-0

[Block 494 [VERSE]]
མི་རྟག་རྟག་མིན་བདག་མེད་དང་། །
བདག་མིན་སྡུག་དང་མི་སྡུག་མིན། །
སྡུག་བསྔལ་བདེ་བ་མ་ཡིན་ཞིང་། །
དེའི་ཕྱིར༌[^403]ཕྱིན་ཅི་ལོག་རྣམས་མེད། །

[Block 495]
དེ་ལ་མི་རྟག་པ་ལ་རྟག་པར་འཛིན་པ༌[^404]ཕྱིན་ཅི་ལོག །[^405]ཅི་སླར་ཡང་དེ་མི་རྟག་པའི་དངོས་པོ་ལས་ཕྱིན་ཅི་ལོག་པ་རྟག་པ་ཁོང་དུ་ཆུད་པ་མེད་ན། ཡང་ཇི་ལྟར་མི་རྟག་པ་ལས་ཕྱིན་ཅི་ལོག་རྟག་པ་ཡིན། ཕྱིན་ཅི་ལོག་པས་ན་ཕྱིན་ཅི་ལོག་སྟེ་ལོག་རྟོགས་སོ། །

[Block 496]
གང་གི་ཚེ་མི་རྟག་པ་དེ་རྟག་པར་མི་འགྱུར་ཞིང་མི་རྟག་པ་ཡང་ཕྱིན་ཅི་ལོག་མ་ཡིན་ནོ། །

[Block 497]
མི་རྟག་པའི་དངོས་པོ་ནི་མི་རྟག་པ་ལས་ཕྱིན་ཅི་ལོག་རྟག་པ་ཉིད་དུ་ཐོབ་ནས་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་མ་ཡིན་ཏེ། འོན་ཀྱང་མི་རྟག་པ་ཉིད་ཀྱི་དངོས་པོ་དེ་གང་གི་ཚེ་ཇི་ལྟར་གནས་པའི་མི་རྟག་པ་ཉིད་དུ་ལོགས་སུ་བཞག་ནས་རྟག་པ་ཉིད་དུ་འཛིན་པ་དེའི་ཚེ། ཕྱིན་ཅི་ལོག་ཏུ་འཛིན་པས་ཕྱིན་ཅི་ལོག་ཅེས་བྱའོ། །

[Block 498]
སླར་ཡང་ཅི་ཞིག་ཕྱིན་ཅི་ལོག་འདིས་ཕྱིན་ཅི་ལོག་ཏུ་འཛིན། སྨྲས་པ། རྟག་པར་རོ། །

[Block 499]
སླར་ཡང་དེའི་ཚེ་ཇི་ལྟར་འདིས་རྟག་པར་འཛིན། རྣམ་པར་ཤེས་པ་དེའི་རྣམ་པར་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 500]
གལ་ཏེ་དེ་ལྟ་ན་འདི་ལྟར་དེའི་ཚེ། དེའི་རྣམ་པར་ཤེས་པ་དེ་མི་རྟག་པའི་དངོས་པོ་ལ་མ་ཡིན་ཏེ། དེ་དེའི་རྣམ་པར་མ་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 501]
དེས་ན་རྣམ་པར་ཤེས་པ་དེ་ཡང་མི་རྟག་པ་ལ་མ་ཡིན་ཏེ། ཡོད་པ་ལ་རྟག་པའི་རྣམ་པར་འཛིན་པས། རྟག་པར་འཛིན་པ་ཇི་ལྟར་ཕྱིན་ཅི་ལོག །སྨྲས་པ། དངོས་པོ་མི་རྟག་པར་གནས་པ་ལ་རྟག་པའི་རྣམ་པར་འཛིན་པས་ཕྱིན་ཅི་ལོག་པ་ཞེས་བྱའོ། །

[Block 502]
སླར་ཡང་དངོས་པོ་མི་རྟག་པའི་རྣམ་པར་གནས་སོ༌[^406]ཞེས་དེ་ཇི་ལྟར་དེ་ལྟར་རྟོགས། གང་ལ་གང་ལས་གང་གི་རྣམ་པར་ཤེས་པ་བསྐྱེད་པ་དེས་ན། རྣམ་པར་ཤེས་པ་ལ་གྲགས་པའི་རྣམ་པ་དེ་ལས་དངོས་པོ་རྣམ་པར་འཇོག་སྟེ། སྔོན་པོ་དང་སེར་པོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 503]
རྟག་པའི་རྣམ་པར་ཤེས་པ་ནི་གཞན་གྱི་རྣམ་པ༌[^407]མ་ཡིན་པའི་ཕྱིར། དེའི་ཚེ་མི་རྟག་པའི་རྣམ་པ་ན་དེའི་རྣམ་པར་ཤེས་པས་དངོས་པོ་གང་ཞིག༌[^408]འཛིན་པར་ག་ལ་འགྱུར། གཞན་ཞིག་ལ་དེའི་མི་རྟག་པ་བྱས་ནས་དངོས་པོ་མི་རྟག་གོ་ཞེ་ན། འདི་ནི་དེ་ལྟར་མ་ཡིན་ཏེ། དེ་ཉིད་དེའི་ཚེ་དེའི་མི་རྟག་པའོ། །

[Block 504]
གཞན་ཞིག་ན་དེའི་རྣམ༌[^409]པར་ཤེས་པ་མ་སྐྱེས་པའི་ཕྱིར་མི་སྣང་བ་ཉིད་ལ། དེ་ནི་དེའི་རྣམ་པའོ་ཞེས་འཐད་པ་མ་ཡིན་ལ་ཕྱིན་ཅི་ལོག་ལ་འཛིན་པ༌[^410]ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 505]
དེའི་ཕྱིར་རྟག་པའི་རྣམ་པ་ཕྱིན་ཅི་ལོག་མ་ཡིན་ཞིང་། རྟག་པ་དང་མི་རྟག་པ་ཞེས་བྱས་ནས་ཕྱིན་ཅི་ལོག་ཉིད་མེད་དེ།[^411] དེ་ལྟར་ནམ་ཡང་བདག་མེད་པ༌[^412]དང་བདག་ལ་མིན་ཞིང་། སྡུག་པ་དང་མི་སྡུག་པ༌[^413]ལ་ཡང་མ་ཡིན་ལ། བདེ་བ་དང་སྡུག་བསྔལ་ལ་ཡང་མིན་ནོ་ཞེས་རྒྱས་པར་བཤད་པར་བྱའོ། །

[Block 506]
དེས་ན་དེ་ལྟར་ཕྱིན་ཅི་ལོག་མེད་ལ་གང་གི་ཚེ་ཕྱིན་ཅི་ལོག་མི་སྲིད་པ་དེའི་ཚེ།

[Block 507 [HEADING]]
### ཚིགས་བཅད་བཅུ་པ། ^1-10-0

[Block 508 [VERSE]]
དེ་མེད་ཕྱིན་ཅི་ལོག་བཞི་ལས། །
སྐྱེས་པའི་མ་རིག་མི་སྲིད་ལ། །
དེ་མེད་འདུ་བྱེད་མི་འབྱུང་ཞིང་། །
ལྷག་མ་རྣམས་ཀྱང་དེ་བཞིན་ནོ། །

[Block 509]
དེ་ལ་གང་ཞིག་སྨོས་པའི་ཡན་ལག་བརྒྱུད་མ་རྣམས་ཀྱིས་རྒྱུ་བརྒྱུད་མར་བསྟན་པ་ཡོད་པས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡོད་དོ་ཞེས་པ་ཚུལ་འདིས་འཐད་པ་མ་ཡིན་ནོ། །

[Block 510]
གང་ཞིག་ཕྱིན་ཅི་ལོག་བཞི་ལས་བྱུང་བ་མ་རིག་པ་ཉིད་ལ་ཕྱིན་ཅི་ལོག་མེད་ན་མེད་དོ་ཞེས་བསྟན་ལ། དེ་ཉིད་ཀྱིས་འདུ་བྱེད་ལ་སོགས་པའི་ཡན་ལག་དགག་པ་གྲུབ་བོ། །

[Block 511]
གང་དུ་མ་རིག་པ་མེད་པར༌[^414]འདུ་བྱེད་རྣམས་མི་འབྱུང་ལ་དེ་བཞིན་དུ་རྣམ་པར་ཤེས་པ་མེད་པས་མིང་དང་གཟུགས་བཀག་པ་སྟེ། ཇི་སྲིད་དུ་སྐྱེ་བ་མེད་པས་རྒ་ཤི་མེད་དོ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 512]
དེ་ལྟར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མེད་ན།

[Block 513]
དེ་དག་གི༌[^415]རྒྱུ་བརྒྱུད་མར་བསྟན་པ་ལས།

[Block 514]
དེའི་ཡན་ལག་བརྒྱུད་མ་ག་ལ་ཞིག་དེས་ན་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྐྱེ་བ་མེད་དོ་ཞེས་གྲུབ་བོ། །

[Block 515]
འདིར་སྨྲས་པ། གལ་ཏེ་ན་ཡང་ཕྱིན་ཅི་ལོག་ལས་བྱུང་བའི་མ་རིག་པ་ཕྱིན་ཅི་ལོག་མེད་པས་མེད་དོ་ཞེས་སྨྲས་ན། དེ་ལྟ་ན་ཡང་འདིར་རེ་ཞིག་ཁོ་ནར་འདི་དག་མེད་དོ་ཞེས་རྣམ་པར་གཞག་པར་མི་ནུས་ཏེ། འདུ་བྱེད་སྐྱེད་པས་ན་དེའི་རྒྱུའི་དངོས་པོར་བསྟན་པའི་ཕྱིར་དང་། འདུ་བྱེད་རྣམས་ཀྱང་མ་རིག་པའི་འབྲས་བུར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 516]
དེ་སྐད་དུ་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ། མ་རིག་པའི་རྗེས་སུ་འགྲོ་བའི་གང་ཟག་འདི་དག་ནི་བསོད་ནམས་ཀྱི་འདུ་བྱེད་ཀྱང་མངོན་པར་འདུ་བྱེད་དོ། །

[Block 517]
བསོད་ནམས་མ་ཡིན་པའི་འདུ་བྱེད་ཀྱང་མངོན་པར་འདུ་བྱེད་དོ། །

[Block 518]
ལུང་དུ་མ་བསྟན་པའི་འདུ་བྱེད་ཀྱང་མངོན་པར་འདུ་བྱེད་དོ་ཞེས་སོ། །

[Block 519]
དེའི་ཕྱིར་མ་རིག་པ་དང་འདུ་བྱེད་དག་ཡོད་ལ། དེ་ཡོད་ན་གཞན་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཡན་ལག་རྣམས་གྲུབ་པས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡན་ལག་བཅུ་གཉིས་གྲུབ་བོ་ཞེས་བརྗོད་དོ། །

[Block 520]
གལ་ཏེ་མ་རིག་པ་དང་འདུ་བྱེད་དག་གི་རང་བཞིན་གྲུབ་པར་གྱུར་ན། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡན་ལག་བཅུ་གཉིས་ཡོད་ལ་ཡོད་པ་མ་ཡིན་ཏེ། ཇི་ལྟར་མེད་པ་དེ་ལྟར་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 521 [HEADING]]
### ཚིགས་བཅད་བཅུ་གཅིག་པ། ^1-11-0

[Block 522 [VERSE]]
མ་རིག་འདུ་བྱེད་མེད་མི་འབྱུང་། །
དེ་མེད་འདུ་བྱེད་མི་འབྱུང་ཞིང་། །
དེ་དག་ཕན་ཚུན་རྒྱུ་ཅན་ཏེ། །
རང་བཞིན་གྱིས་ཀྱང་མ་གྲུབ་བོ། །

[Block 523]
གལ་ཏེ་མ་རིག་པ་འདུ་བྱེད་རྣམས་ཀྱི་རྒྱུར་རྣམ་པར་གཞག་པ་ནི་འདི་ལྟར་འདུ་བྱེད་མེད་པའི་ཕྱིར་དེ་མེད་ལ་རྒྱུ་གང་ཞིག་རྒྱུ་ཉིད་དུ་འབྲས་བུ་དང་འབྲེལ་པ་བྱས་པ་ལས་ཡིན་གྱི་འབྲེལ་བ་མེད་ན་རྒྱུ་ཉིད་ནམ་ཡང་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 524]
ཡང་ན་འབྲས་བུ་ཉེ་བར་མ་བཟུང་བར༌[^416]འགའ་ཞིག་རྒྱུ་ཉིད་དུ་འགྱུར་ན། དེ་ལྟ་ན་འགའ་ཞིག་འགའ་ཞིག་གི་རྒྱུར་མི་འགྱུར་ལ། དེའི་ཕྱིར་རྒྱུའི་རྣམ་པར་གཞག་པ་འབྲས་བུ་མེད་ན་མ་ཡིན་ལ་རྒྱུ་ཡང་མ་རིག་པ་ནི་འདུ་བྱེད་རྣམས་ཀྱིའོ་ཞེས་བྱ་སྟེ། མ་རིག་པ་ནི་འདུ་བྱེད་མེད་ན་རྒྱུར་མི་འགྱུར་ལ། རྒྱུ་འབྲས་ཀྱི་དངོས་པོའི་སྐབས་ཡིན་པའི་ཕྱིར། རྒྱུའི་སྒྲ་མེད་ཀྱང་རྒྱུ་ཉིད་དུ་རྟོགས་པ་ཉིད་ཀྱི༌[^417]འབྲས་བུ་རྒྱུའི་སྒྲས་མ་གསུངས་སོ། །

[Block 525]
ཇི་ལྟར་འབྲས་བུ་ལ་མ་ལྟོས་པར་འགའ་ཞིག་རྒྱུ་ཉིད་མ་ཡིན་པའི་ཕྱིར་མ་རིག་པ་འདུ་བྱེད་མེད་ན་མི་འབྱུང་བ་བཞིན་འབྲས་བུ་ཡང་རྒྱུ་ལ་མ་ལྟོས༌[^418]ན། རྒྱུ་མེད་པ་ལས་མི་སྲིད་དོ་ཞེས་བྱ་བ་ནི། དེ་མེད་འདུ་བྱེད་མི་འབྱུང་ཞིང་། མ་རིག་པ་མེད་ན་འདུ་བྱེད་མི་འཐད་དེ་རྒྱུ་མེད་པར་ཐལ་བའི་ཕྱིར་རོ། །

[Block 526]
གང་ཡང་འདི་ལྟར་རྒྱུ་དང་འབྲས་བུ་དག་ཕན་ཚུན་མ་ལྟོས་པར་གྲུབ་པ་མེད་ལ། དེའི་ཕྱིར་དེ་དག་ཕན་ཚུན་རྒྱུ་ཅན་དང་། ངོ་བོ་ཉིད་ཀྱིས་ཀྱང་མ་གྲུབ་སྟེ། ཕ་རོལ་དང་ཚུ་རོལ་བཞིན་ནམ་རིང་པོ་དང་ཐུང་ངུ་བཞིན་རྒྱུ་དང་འབྲས་བུ་དག་ཕན་ཚུན་ལྟོས་པ་དང་བཅས་པའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་མེད་དོ། །

[Block 527]
གལ་ཏེ་རྒྱུ་དང་འབྲས་བུ་དག་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པར་གྱུར་ན། དེ་ནི་འབྲས་བུ་ལ་མི་ལྟོས་པར་རྒྱུར་འགྱུར་ན། དེ་ལས་ཀྱང་རྒྱུ་མེད་པ་ཉིད་དུ་འགྱུར་ཏེ། རྒྱུ་ནི་གང་ལས་འབྲས་བུའི་འཇུག་པའི་རྒྱུ་ཉིད་པས་རྒྱུའོ། །

[Block 528]
དེ་མེད་ན་རྒྱུ་མེད་པ་ཉིད་རྒྱུར་འགྱུར་ཏེ། རྒྱུ་མེད་པ་ཉིད་རྒྱུར་འཐད་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བས། དེས་ན་ངེས་པར་འབྲས་བུ་ལ་ལྟོས་ལ། འབྲས་བུ་ལ་ལྟོས་པའི་ཕྱིར་རང་ཉིད་མ་གྲུབ་བོ། །

[Block 529]
དེ་བཞིན་དུ་གལ་ཏེ་འབྲས་བུ་ངོ་བོས་གྲུབ་པར་གྱུར་ན། དེ་ནི་རྒྱུ་ལ་མི་ལྟོས་པར་འགྱུར་ལ། དེ་ཡང་རྒྱུ་ལ་མི་ལྟོས་ན། དེ་ནི་ནམ་མཁའི་མེ་ཏོག་བཞིན་དུ་འགྱུར་བས་དེའི་ཕྱིར་རྒྱུ་ལ་ལྟོས། རྒྱུ་ལ་ལྟོས་པའི་ཕྱིར་ངོ་བོ་ཉིད་མ་གྲུབ་བོ་ཞེས་གནས་སོ། །

[Block 530]
དེ་ནི་འདི་ལྟར་ཇི་སྐད་དུ་གསུངས་པའི་རིགས་པས།
--- END BLOCKS ---
