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
[Block 631 [VERSE]]
རྡོ་རྗེ་ལ་ནི་དམིགས་པ་དང་། །
རྡོ་རྗེ་ཡིས༌[^274]དང་རྡོ་རྗེའི་ཕྱིར། །

[Block 632]
རྡོ་རྗེ་འབྱུང་དང་རྡོ་རྗེ་སྤོང་།[^275] །རྡོ་རྗེ་འཇོམས་དང་རྡོ་རྗེ་བྲལ། །ཞེས་པ་རྡོ་རྗེ་བཟླས་པ་ནི་འོད་ལྔའི་སྦྱོར་བས་སོ། །

[Block 633]
རྡོ་རྗེར༌[^276]ཞེས་པ་གང་ཡིན་ཞེ་ན།

[Block 634 [VERSE]]
དངོས་པོ་ཐམས་ཅད་རྡོ་རྗེ་ཡི། །
ངོ་བོར་བྱས་ཏེ་ཟློས༌[^277]ཕྱིར་དང་། །

[Block 635]
ཞེས་པ་ནི་གཟུང་བ་དང་འཛིན་པའི་རྣམ་པ་ཐམས་ཅད་རྡོ་རྗེའི་བཟླས་པའི་ངོ་བོར་བྱས་པའི་ཕྱིར་རོ། །

[Block 636]
རྡོ་རྗེ་ལ་དམིགས་པ་ཞེས་བྱ་བའང་གང་ཞེ་ན།

[Block 637 [VERSE]]
གང་ཚེ་སྐུ་གསུང་ཐུགས་དག་ལ། །
དམིགས་པ་དེ་ལ་དེ་སྐད་དོ། །

[Block 638]
ཞེས་པ་སྐུ་གསུང་ཐུགས་རྡོ་རྗེ་དང་འདྲ་བ་ལ། དམིགས་པ་གང་ཡིན་པ་དང་། གཞན་ཡང་འོག་གི་དབང་དུའང་དེ་བཞིན་ནོ། །

[Block 639]
རྡོ་རྗེ་ཡིས་ཞེས་པ་བཤད་པ།

[Block 640 [VERSE]]
རྡོ་རྗེའི་འོད་ཟེར་འབར་བ་ཡིས། །
གང་དུ་འབྲས་ཐོབ་དེ་ཕྱིར་རོ། །

[Block 641]
ཞེས་པ་འོད་ཟེར་དང་བ་ཐག་དང་ཕྲེང་བ་འདི་ནི་རྡོ་རྗེ་དང་འདྲ་བ་སྟེ། དེས་འབྲས་བུ་ཐོབ་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 642]
རྡོ་རྗེ་ཡི་ཕྱིར་ཞེས་བཤད་པ།

[Block 643 [VERSE]]
གང་ཞིག་མཆོག་ནི་ཐོབ་བྱའི་ཕྱིར། །
བཟླས་པ་གང་ཡིན་དེ་ཁོ་ན། །

[Block 644]
ཞེས་པ་ནི། རྡོ་རྗེ་ནི་ཆོས་ཀྱི་དབྱིངས་ཏེ། དེ་ཐོབ་པར་བྱེད་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 645]
རྡོ་རྗེ་ལས་བྱུང་བ་ནི།

[Block 646 [VERSE]]
སྙིང་ག་དང་ནི་རྩ་བ་ནས། །
གང་ཞིག་འབྱུང་བར་བྱེད་པ་དང་། །

[Block 647]
ཞེས་པ་སྙིང་གའི་ས་བོན་དང་། རྡོ་རྗེ་རྩ་བའི་ས་བོན་དེ་དག་ལས་བྱུང་བ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 648]
རྡོ་རྗེ་སྤོང་བ་དང་རྡོ་རྗེ་འཇོམས་པ་བཤད་པ། །

[Block 649 [VERSE]]
རྟོག་པ་རྡོ་རྗེ་དང་འདྲ་བ། །
གང་གིས་འཇོམས་པར་བྱེད་པ་དང་། །

[Block 650]
ཞེས་པ་རྣམ་པར་རྟོག་པའང་འཇིག་པར་དཀའ་བ་ཉིད་ཀྱི་ཕྱིར་ཏེ། དེ་འཇོམས་པའི་བཟླས་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 651]
འདིའི་བཟླས་པའང་གང་ཡིན་དུ་ཞེ་ན།

[Block 652 [VERSE]]
རྡོ་རྗེ་བཟླས་དང་ནང་གི་དང་། །
ཟབ་མོ་གསང་བའི་བཟླས་པ་ནི། །
རྣམ་གྲངས་ཡིན་པར་ཤེས་པར་བྱ། །

[Block 653]
ཞེས་པ་ངེས་པའི་ཚིག་དང་། མི་བརྟན་པའི་ཕྱིར་དང་། རྟོག་པར༌[^278]དཀའ་བ་ཉིད་དང་། བྱང་ཆུབ་སེམས་དང་ལྡན་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 654]
འདིའང་ཆོས་དུ་དང་ལྡན་ཞེ་ན། ངེས་པའི་ཚིག་རྣམས་ངག་གི་རྟོག་པ་སྦྱོང་། །ཞེས་པ་བཤད་ཟིན་ཏོ། །

[Block 655 [VERSE]]
འདི་ཡིས་གཞན་ལ་ཐལ་འགྱུར་བ། །
སེལ་ཕྱིར་དེ་དག་བརྗོད་པར་བྱ། །

[Block 656]
ཞེས་པ་ནི་ཅི་རིགས་སུ་བཤད་དོ། །

[Block 657]
རྒྱུའང་གང་ཡིན་ཞེ་ན།

[Block 658 [VERSE]]
ཏིང་འཛིན་ཟས་ལ་སོགས་པ་རྣམས། །
འབྲས་བུ་སྐྱེད་པར་བྱེད་ཕྱིར་རྒྱུ། །

[Block 659]
ཞེས་པ་གང་དུ་ཏིང་ངེ་འཛིན་ཟས་སྐོམ་དང་། དུས་ཉིད་དང་། ཡུལ་ལ་སོགས་པ་དག་གིས་འབྲས་བུ་སྐྱེད་པར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 660]
དུས་གང་གི་ཚེ་ན།

[Block 661 [VERSE]]
བསྐྱེད་པ་མཐར་ཕྱིན་སེམས་ལ་དམིགས། །
འདི་ལ་གཞོལ་བ་དེ་ཡི་དུས། །

[Block 662]
ཞེས་པ་གང་གིས་བསྐྱེད་པའི་རིམ་པ་མཐར་ཕྱིན་པ་དང་སེམས་ལ་དམིགས་པ་མཐར་ཕྱིན་པ༌[^279]ལས་གཞོལ་བའི་དུས་སུའོ། །

[Block 663]
འདིའི་མཚན་ཉིད་ཀྱང་གང་ཞེ་ན།

[Block 664 [VERSE]]
སྐྱོན་རྣམས་སྤངས་ཤིང་ཡོན་ཏན་ལྡན། །
འདི་ནི་མཚན་ཉིད་ཅེས་སུ་བཤད། །

[Block 665]
ཅེས་པ་གང་གིས་སྤང་བ་དང་བླང་བ་དག་དང་བྲལ་ཞིང་ལྡན་པ་འདི་ནི་འདིའི་མཚན་ཉིད་དོ། །

[Block 666]
དམིགས་པ་གང་ཡིན་ཞེ་ན།

[Block 667 [VERSE]]
གང་ཞིག་དབྱེ་བའི་རྣམ་པ་བཞིན། །
འོད་དང་བ་ཐག་ཕྲེང་བ་དང་། །
ཡི་གེ་གསུམ་གྱི་རྣམ་པའམ། །
ཡང་ན་ཐབས་དང་ཤེས་རབ་བོ། །

[Block 668]
ཞེས་པ་གང་གིས་འོད་དང་བ་ཐག༌[^280]ཐིག་ལེའི་ཕྲེང་བ་དང་། རྩེ་མོ་ལ་ཨོཾ་ཨཱཿཧཱུཾ་དང་། །ཨཱ་ལི་ཀཱ་ལིའི་ཕྲེང་བ་ལ་དམིགས་པ་འདི་ནི་འདིའི་དམིགས་པའོ། །

[Block 669]
དམིགས་པ་ལ་སེམས་འཛིན་པའི་རྒྱུའམ་གྲོགས་གང་ཡིན་ཞེ་ན།

[Block 670 [VERSE]]
གང་དུ་ཚོགས་ལ་སོགས་པ་རྣམས། །
འདི་ཡི་སྒྲུབ་པའི་གྲོགས་སུ་འགྱུར། །
--- END BLOCKS ---
