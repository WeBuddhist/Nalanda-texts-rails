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

[Block 531 [HEADING]]
### ཚིགས་བཅད་བཅུ་གཉིས་པ། ^1-12-0

[Block 532 [VERSE]]
གང་ཞིག་རང་ཉིད་རང་བཞིན་གྱིས། །
མ་གྲུབ་དེས་གཞན་ཇི་ལྟར་བསྐྱེད། །
དེའི་ཕྱིར༌[^419]གཞན་ལས་གྲུབ་པ་ཡི། །
རྐྱེན་གཞན་དག་ནི་སྐྱེད་བྱེད་མིན། །

[Block 533]
གང་ཡང་དེའི་ཚེ་འབྲས་བུ་ལ་མ་ལྟོས་པར་རང་གི་ངོ་བོ་མི་འགྲུབ་ལ། དེ་ཇི་ལྟར་རང་ཉིད་གྲུབ་པ་མེད་པར་འབྲས་བུ་སྐྱེད་པར་བྱེད། གལ་ཏེ་སྐྱེད་ན་མོ་གཤམ་གྱི་བུ་མོ་ཡང་བུ་སྐྱེད་པར་འགྱུར་ལ། དེའི་ཕྱིར༌[^420]གཞན་ལས་གྲུབ་པ་ཡི། ། རྐྱེན་གཞན་དག་ནི་སྐྱེད་བྱེད་མིན།[^421] །རང་ལས་ཐ་དད་པ་གཞན་དུ་གྱུར་པ་ནི་འབྲས་བུ་ལ་དེ་ལ༌[^422]ལྟོས་ནས་གྲུབ་པའི་མ་རིག་པ་ལ་སོགས་པའི་རྐྱེན་གྱིས་རང་ལས་ཐ་དད་པའི་འབྲས་བུ་འདུ་བྱེད་ལ་སོགས་པའི་སྐྱེད་བྱེད་མ་ཡིན་ནོ། །

[Block 534]
ཕན་ཚུན་མི་ལྟོས་པར་གྲུབ་པར་ཡོད་པར་གྱུར་ན། རྒྱུ་ལས་གཞན་པ་འབྲས་བུ༌[^423]ལས་གཞན་པ་རྒྱུའི༌[^424]ཞེས་འཐད་པར་འགྱུར་ལ། རྒྱུ་དང་འབྲས་བུ་དག་ཕན་ཚུན་མ་ལྟོས་པར་གྲུབ་པ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བསྒྲུབས་ཟིན་ཏོ། །

[Block 535]
དེས་ན་མ་རིག་པ་ལས་འདུ་བྱེད་རྣམས་གཞན་ཉིད་དུ་མ་གྲུབ་པས་འདུ་བྱེད་རྣམས་ལ་མ་ལྟོས་པར་མ་རིག་པ་གཞན་ཉིད་དུ་གྲུབ་པར་འགྱུར་རོ་ཞེས་བརྗོད་པར་མི་ནུས་སོ། །

[Block 536]
དེ་ལྟར་འདུ་བྱེད་ལ་སོགས་པ་ལས་མ་རིག་པ་ལ་སོགས་པ་གཞན་ཉིད་དུ་མ་གྲུབ་ན། མ་རིག་པ་ལ་བརྟེན་ནས་བྱུང་བའི་འདུ་བྱེད་རྣམས་གཞན་ཉིད་དུ་གྲུབ་བོ་ཞེས་རྣམ་པར་གཞག་པར་མི་ནུས་སོ། །

[Block 537]
གང་ཞིག་དེ་ལྟར།

[Block 538 [VERSE]]
དེའི་ཕྱིར༌[^425]གཞན་ལས་གྲུབ་པ་ཡི། །
རྐྱེན་གཞན་དག་ནི་སྐྱེད་བྱེད་མིན། །

[Block 539]
དེས་ན་འདིར་མ་རིག་པ་ལ་བརྟེན་ནས་འདུ་བྱེད་ལ། འདུ་བྱེད་ལ་ལྟོས་ནས་མ་རིག་པའོ་ཞེས་རྣམ་པར་གཞག་པས་རེ་ཞིག་རྒྱུ་དང་འབྲས་བུ་དག་གཅིག་ཉིད་མ་ཡིན་ནོ་ཞེས་སྨོས་པར་འགྱུར་རོ། །

[Block 540]
དེ་ཉིད་ཀྱིས་དེ་ཉིད་སྐྱེད་པ་མེད་དོ་ཞེས་བྱས་ནས། ཕན་ཚུན་ལྟོས་པས་རྒྱུ་དང་འབྲས་བུ་དག་གྲུབ་པར་གྱུར་ལ། ཕན་ཚུན་ལྟོས་པས་རང་གི་ངོ་བོ་གྲུབ་པ་མེད་པས་རྒྱུ་དང་འབྲས་བུ་དག་གཞན་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བརྗོད་པར་འགྱུར་རོ། །

[Block 541]
དེ་ཉིད་ཀྱིས་ན་གཅིག་པ་དང་གཞན་པ་དག་མེད་པས་རྟག་པ་དང་ཆད་པའི་མཐར་སྨྲ་བ་དང་བྲལ་བའི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་གྲུབ་པ་ཡོངས་སུ་སྐྱེའོ། །

[Block 542]
ཇི་སྐད་དུ།

[Block 543 [VERSE]]
བརྟེན་ནས་བྱུང་བ་གང་དང་གང་། །
རེ་ཞིག་དེ་ཉིད་དེས་མི་བསྐྱེད། །
གཞན་ལས་ཀྱང་མིན་དེ་ཡི་ཕྱིར། །
རྟག་མིན་ཆད་པ་ཡང་མ་ཡིན། །

[Block 544]
ཞེས་བྱ་སྟེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རང་བཞིན་མེད་པར་ཡང་ཤིན་ཏུ་གསལ་བར་ཁོང་དུ་ཆུད་པར་བྱས་པར་འགྱུར་རོ། །

[Block 545]
ཇི་སྐད་དུ།

[Block 546 [VERSE]]
གཅིག་ཉིད་གཞན་ཉིད་དང་བྲལ་བ། །
འགྲོ་བ་སྒྲ་བརྙན་ལྟ་བུ་སྟེ། །
འཕོ་དང་འཇིག་པ་བྲལ་བ་ཡི། །
རྟོགས་ལྡན་ཁྱོད་ལ་མི་སྨོད་དོ། །

[Block 547]
ཞེས་གསུངས་སོ། །

[Block 548]
གལ་ཏེ་ཡང་དེ་ལྟར་རྒྱུ་དང་འབྲས་བུ་དག་ཕན་ཚུན་ལྟོས་པ་ཅན་དུ་གྲུབ་པར་རྣམ་པར་བཞག་ལ། དེ་ལྟ་ན་ཡང་ཕན་ཚུན་ལྟོས་པ་ཅན་དུ་གྲུབ་པས་དེ་དག་ཀྱང་བུ་དང་ཕ་བཞིན་དུ་གྲུབ་པར་འགྱུར་རོ་ཞེ་ན། གསུངས་པ།

[Block 549 [HEADING]]
### ཚིགས་བཅད་བཅུ་གསུམ་པ། ^1-13-0

[Block 550 [VERSE]]
ཕ་ནི་བུ་མིན་བུ་ཕ་མིན། །
དེ་དག་ཕན་ཚུན་མེད་མིན་ཞིང་། །
དེ་གཉིས་ཅིག་ཅར་ཡང་མེད་ལྟར། །
དེ་ལྟར་ཡན་ལག་བཅུ་གཉིས་སོ། །

[Block 551]
ཕ་ཉིད་བུ་མ་ཡིན་ཏེ། ཕ་ཞེས་བྱ་བ་སྐྱེད་བྱེད་ལ། དེ་ཇི་ལྟར་བསྐྱེད་བྱར་འགྱུར། བུ་ཡང་ཕ་མིན་ཏེ། བུ་ནི་བསྐྱེད་བྱ་ལ། དེ་ཇི་ལྟར་སྐྱེད་བྱེད་དུ་འགྱུར། དེ་ལྟར་རེ་ཞིག་ཕ་ཉིད་བུ་མ་ཡིན་ལ་བུ་ཉིད་ཕ་མ་ཡིན་ནོ། །

[Block 552]
ཐ་མི་དད་པ་མ་ཡིན་པའི་ཕྱིར་དེ་གཉིས་ཕན་ཚུན་མེད་པ་མིན་ཏེ། བུ་མེད་ན་ཕ་འཐད་པ་མ་ཡིན་ཏེ། སྐྱེད་པར་བྱེད་པའི་ལས་ཀྱིས་ཕ་ཉིད་དུ་འཐད་པའི་ཕྱིར། བུ་མེད་ན་ཅི་ཞིག་སྐྱེད་པར་བྱེད་པས་ཕ་ཉིད་དུ་འགྱུར། ཕ་ཡང་བུ་མེད་ན་མི་འགྲུབ་པས། ཕ་མེད་ན་བུ་ཡང་མི་འཐད་དོ་ཞེས་བྱ་བས། དེ་གཉིས་ཕན་ཚུན་མེད་མིན་ཞིང་། །དེ་གཉིས་ཅིག༌[^426]ཅར་ཡང་མེད་ལྟར་ཏེ། དེ་གཉིས་ཅིག༌[^427]ཅར་ན་བ་ལང་གི་རྭ་གཡས་པ་དང་གཡོན་པ་བཞིན་པས་བསྐྱེད་བྱ་སྐྱེད་བྱེད་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 553]
ཇི་ལྟར་ཕ་དང་བུ་དག་མ་གྲུབ་པ་དེ་བཞིན་དུ་ཡན་ལག་བཅུ་གཉིས་ཀྱི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡང་མ་གྲུབ་སྟེ། མ་རིག་པ་ཉིད་འདུ་བྱེད་མ་ཡིན་ལ། འདུ་བྱེད་ཉིད་མ་རིག་པ་མ་ཡིན་ཞིང་།

[Block 554 [VERSE]]
དེ་གཉིས་ཕན་ཚུན་མེད་མིན་ཞིང་། །
དེ་གཉིས་ཅིག་ཅར་ཡང་མ་ཡིན། །

[Block 555]
ཞེས་བྱ་བས་ཐམས་ཅད་ལ་མཚུངས་པར་སྦྱར་བར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 556]
གལ་ཏེ་མ་རིག་པ་དང་འདུ་བྱེད་དག་རང་གི་ངོ་བོ་མ་གྲུབ་ན། དེ་ནི་མ་རིག་པ་ལ་བརྟེན་ནས་འདུ་བྱེད་རྣམས་སྐྱེ་བ་མི་འཐད་དེ། མེད་བཞིན་པའི་མོ་གཤམ་གྱི་བུ་ལ་བརྟེན་ནས། དེའི་བུ་འབྱུང་བ་མ་ཡིན་ནོ་ཞེས་བརྗོད་དོ། །

[Block 557]
གལ་ཏེ་མ་རིག་པ་དང་འདུ་བྱེད་དག་རང་གི་ངོ་བོ་གྲུབ་པར་གྱུར་ན། དེ་ནི་འདི་དག་ད་ལྟ༌[^428]བ་བཞིན་པས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 558]
མོ་གཤམ་གྱི་བུ་ལ་ཡང་བརྟེན་ནས་འབྱུང་བ་མ་ཡིན་ཞིང་། མ་རིག་པ་ལ་བརྟེན་ནས་འདུ་བྱེད་འབྱུང་ངོ་ཞེས་བྱ་སྟེ། དེས་ན་མོ་གཤམ་གྱི་བུ་ལྟ་བུ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་དོན་མ་ཡིན་ནོ། །

[Block 559]
འོ་ན་གཉི་ག་ཡང་རང་བཞིན་གྱིས་མ་སྐྱེས་པར་མཉམ་ལ། དེ་ལྟ་ན་ཡང་ཕྱིན་ཅི་ལོག་ལ་ལྟོས་ནས་མ་རིག་པ་ལ་སོགས་པ་ལ་བརྟེན་ནས་སྐྱེ་བ་ཡོད་ལ། མོ་གཤམ་གྱི་བུ་ལ་ཕྱིན་ཅི་ལོག་ལ་ཡང་དེ་ལ་བརྟེན་ནས་སྐྱེ་བར་མི་རྟོག༌[^429]པའི་ཕྱིར་རོ། །

[Block 560]
ཡང་ཅིའི་ཕྱིར་གཉི་ག་ཡང་མཚུངས་པར་རང་བཞིན་གྱིས་མ་སྐྱེས་པ་ལ་གཅིག་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བར་མཐོང་ལ་ཅིག༌[^430]ཤོས་ནི་མ་ཡིན་འདི་ནི་འཇིག་རྟེན་པ་ཁོ་ན་ལ་དྲི་བར་བྱའི། ཁོ་བོ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 561]
དེ་ཉིད་ཀྱིས་ན་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་འཇིག་རྟེན་གྱི་ཕྱིན་ཅི་ལོག་ལས་སོ། །

[Block 562]
གང་དག་རང་བཞིན་གྱིས་མ་སྐྱེས་པར་མཉམ་པ་ཁ་ཅིག་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བར་མཐོང་ལ་ཅིག༌[^431]ཤོས་ནི་མ་ཡིན་ནོ། །

[Block 563]
རིགས་པས་ནི་མོ་གཤམ་གྱི་བུ་བཞིན་དུ་ཆོས་ཐམས་ཅད་ཡོངས་སུ་མ་བརྟགས་ལ། ཅུང་ཟད་རྟོག་པར་བྱེད་པས་ན། ཕྱིན་ཅི་ལོག་ཏུ་རྣམ་པར་གཞག་སྟེ། འདི་ལྟར་རབ་རིབ་ཅན་གྱིས༌[^432]ཡང་དག་པ་མ་ཡིན་པའི་སྐྲ་ལ་ཡོངས་སུ་རྟོག་པ་མི་འཐད་པས། ཇི་ལྟར་རབ་རིབ་མེད་པ་རྣམས་ཀྱིས་བརྟགས་པ་ལས་ཕྱིན་ཅི་ལོག་ཏུ་མཐོང་བ་ཞེས་བརྗོད་དོ། །

[Block 564]
དེ་ཉིད་ཀྱིས་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་སྨན་པ་ཆེན་པོ་ལྟར་རང་བཞིན་མེད་པ་སྐྱེ་བོ་རྣམས་ལ་སྟོན་པར་མཛད་དེ། གང་ཞིག་དེའི་རྒྱུ་ཡོད་པ་མ་ཡིན་པ་ལ་དོན་དུ་རྟོག་པའི་རྣམ་པར་རྟོག་པ་ཕྱིན་ཅི་ལོག་གི་མཚན་ཉིད་ལས་བཟློག་པར་མཛད་དོ། །

[Block 565]
རྣམ་པར་རྟོག་པ་ལས་ཡོངས་སུ་བཟློག་ནས་ཡང་ཆོས་རྣམས་ཀྱི་ཆོས་ཉིད་ཇི་ལྟ་བ་དེ་ལྟ་བུ་ལ་གནས་སོ། །
--- END BLOCKS ---
