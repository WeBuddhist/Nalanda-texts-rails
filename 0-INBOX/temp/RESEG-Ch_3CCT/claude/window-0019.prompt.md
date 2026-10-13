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

[Block 671]
ཞེས་པ་གོ་སླའོ། །

[Block 672 [VERSE]]
སྔོན་དུ་འགྲོ་བ་གང་ཡིན་ཞེ་ན། །
བསྐྱེད་པ་ཁམས་བཅོས་སྔོན་དུ་འགྲོ། །

[Block 673]
ཞེས་པ་རྡོ་རྗེ་བཟླས་པའི་སྔོན་དུ་ཁམས་བཅོས་པ་དང་། བསྐྱེད་པའི་རིམ་པ་ལ་བསླབ་པར་བྱ་བ་འདི་ནི་སྔོན་དུ་འགྲོ་བའོ། །

[Block 674]
འདིའི་རྟེན་ཡང་གང་ཡིན་ཞེ་ན།

[Block 675 [VERSE]]
བསྐྱེད་པ་ཡི་ནི་སྦྱོར་བ་ལ། །
བརྟེན་ནས་བཟླས་པར་བྱ་བ་ཡིན། །

[Block 676]
ཞེས་པ་རྡོ་རྗེ་བཟླས་པའི་རྟེན༌[^281]ནི་བསྐྱེད་པའི་རིམ་པ་སྟེ། འདི་ལ་བརྟེན་ནས་འདི་བྱེད་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 677]
ཚིག་འཁྱལ༌[^282]ལ་སོགས་མི་མཐུན་ཕྱོགས། །ཞེས་པ་ཚིག་ཀྱལ་པ༌[^283]དང་། ངག་རྩུབ་མོ་དང་ཕྲ་མ་དང་བརྫུན་ལ་སོགས་པ་འདི་ནི་བཟླས་པ༌[^284]མི་མཐུན་པའི་ཕྱོགས་སོ། །

[Block 678]
དེའི་གཉེན་པོ་ནི་འདི་ཉིད་དེའི་གཉེན་པོའོ་ཞེས་པ་འགལ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 679]
སའི་ཁྱད་པར་ཡང་གང་ཡིན་ཞེ་ན།

[Block 680 [VERSE]]
གང་ཞིག་འདི་ལ་རྟག་གནས་ནས། །
ས་བརྒྱད་པ་ལ་གནས་པར་བྱེད། །

[Block 681]
ཅེས་པ་རྡོ་རྗེ་བཟླས་པ་ལ་གནས་པའི་རྣལ་འབྱོར་པ་ས་བརྒྱད་པ་བཟོད་པ༌[^285]འབྲིང་ལ་གནས་པའོ། །

[Block 682]
དེ་དང་འབྲེལ་བའི་དངོས་གྲུབ་ཀྱང་གང་ཡིན་ཞེ་ན།

[Block 683 [VERSE]]
ཁ་དོག་ལྔ་ལ་དམིགས་པ་ཡིས། །
ལས་བཞི་དེ་དང་འབྲེལ་པ་འགྲུབ། །

[Block 684]
ཅེས་པ་ཞི་བ་ལ་སོགས་པའི་ལས་དང་བསྲུང་བ་དང་། འཕེལ་བ་ལ་སོགས་པ་འབྱུང་བར་འགྱུར་རོ། །

[Block 685 [VERSE]]
འབྱུང་ལ༌[^286]གང་ཞིག་གནས་པ་ཡིས། །
ཐུན་མོང་གཞན་ནི་འགྲུབ་འགྱུར་ཏེ།
འཇུག་དང་གནས་པའི་སྦྱོར་བ་ཡིས། །
འདི་ཡི༌[^287]སྲིད་པ་འགྲུབ་པར་འགྱུར། །

[Block 686]
ཞེས་པ་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 687]
དེ་ཡང་སྤྱོད་པ་གང་དང་འབྲེལ་པ་ཡིན་ཞེ་ན།

[Block 688 [VERSE]]
བྱུག་པ་དང་ནི་དེར་འབྲེལ་ལོ། །
བསླབ་པ་སྤྱོད་པར་འབྲེལ་པ་ཡིན། །

[Block 689]
ཞེས་པ་ཤ་ཆེན་པོ་ལ་སོགས་པ་བྱིན་གྱིས་བརླབས་ཏེ་བཟའ་བ་དང་། འདི་དག་གིས༌[^288]བྱུག་པ༌[^289]བྱའོ། །

[Block 690]
ས་མཚམས་ཀྱང་གང་ནས་གང་དུ་ཡིན་ཞེ་ན།

[Block 691 [VERSE]]
བསྐྱེད་ལ་བརྟེན་ནས་སེམས་ལ་དམིགས། །
བར་དུ་རྡོ་རྗེ་བཟླས་པ་ཡིན། །

[Block 692]
ཞེས་པ༌[^290]

[Block 693]
དང་པོ་བསྐྱེད་པའི་རིམ་པ་ནས་བརྩམས་ནས་དེ་གོམས་ནས་སེམས་ལ་དམིགས་པའི་བར་དུ་རྡོ་རྗེ་བཟླས་པའོ། །

[Block 694]
འབྲས་བུ་གང་འབྱུང་ཞེ་ན།

[Block 695 [VERSE]]
ངག་གི་དབང་ཕྱུག་སྦྱོར་བ་ཡང་། །
རྡོ་རྗེ་བཟླས་པ་འདི་ཡིས་འགྲུབ། །

[Block 696]
ཅེས་པ་འདི་ཡིས་ངག་གི༌[^291]དབང་ཕྱུག་ཡན་ལག་རྒྱ་མཚོའམ། ཡན་ལག་དྲུག་ཅུའི་དབྱངས་ལ་སོགས་པ་ཐོབ་པར་འགྱུར་རོ། །

[Block 697]
གོམས་པའི་ཚད་ཅི་ཞེ་ན།

[Block 698 [VERSE]]
གང་གིས་རླུང་རྣམས་གསལ་བ་ནི། །
ཉམས་སུ་མྱོང་བ་གོམས་པའི་ཚད། །

[Block 699]
ཅེས་པ་ཁ་དོག་དང༌[^292]དབྱིབས་དང་གྲངས་གང་དུ་གསལ་བ་དེ་ནི་གོམས་པའི་ཚད་དོ། །

[Block 700]
མཐར་ཕྱིན་པའི་ཚད་ཀྱང་གང་ཡིན་ཞེ་ན།

[Block 701 [VERSE]]
གནས་འཕོ་བ༌[^293]དང་དུ་མར་བྱེད། །
འདི་ནི་མཐར་ཕྱིན་ཚད་ཡིན་ནོ། །

[Block 702]
ཞེས་པ་ཕྲ་བའི་རླུང་རགས་པ་དང་། རགས་པའི་རླུང་ཕྲ་བར་བྱེད་པ་དང་། ཕྲ་བའི་རླུང་དང་རགས་པ་བཞིན༌[^294]དུ་མ་དང་དེ་ལས་བཟློག་པ༌[^295]ཤེས་པ་འདིའི་དུས༌[^296]སུ་དབུགས་ནང་དུ་བསྡུས་ན་གནོད་པ་མི་འབྱུང་བའོ། །

[Block 703]
གཞན་ནི།

[Block 704 [VERSE]]
གང་ཞིག་དང་པོ་གཉིས་པ་དང་། །
གསུམ་པའི་གང་ཟག་དབང་དག་ཏུ། །
དབྱིབས་དང་རླུང་དང་སྒྱུ་མར་དམིགས། །
རིགས་ཅན་ལ་ནི་འབྲས་བུ་སྐྱེ། །

[Block 705 [VERSE]]
ཀློག་དང་ཁ་དོག༌[^297]སྦྱོར་བ་མེད། །
ཕྲེང་བ་མི་དགོས༌[^298]བགྲང་མི་དགོས། །
འོན་ཀྱང་རླུང་ལ་བརྟེན་པའི་ཕྱིར། །
འདི་ནི་བཟླས་པར་བཤད་པ་སྟེ། །
--- END BLOCKS ---
