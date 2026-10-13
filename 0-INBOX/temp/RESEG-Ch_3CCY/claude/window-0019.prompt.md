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
དེ་ལྟར་རེ་ཞིག་དངོས་པོ་མེད་ན་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་ཏེ། ཇི་ལྟར་ཡང་དངོས་པོ་མེད་ན་དངོས་པོ་མེད་པ་ཡང་མི་འཐད་ན། དེ་ལྟར་རྟག་པར་དངོས་པོ་དང་དངོས་པོ་མེད་པ་ཡང་མེད་ན་མེད་དོ་ཞེས་བྱ་བ་འདི་དང་འབྲེལ་ཏོ། །

[Block 667]
དངོས་པོ་དང་དངོས་པོ༌[^519]མེད་པ་ནི༌[^520]དངོས་པོ་ཡོད་པ་དང་དངོས་པོ་མེད་པ་ཞེས་བྱ་སྟེ། མི་རྟག་པ་ལ་བརྗོད་དོ། །

[Block 668]
དངོས་པོ་མེད་པ་དེ་ཡང་རྟག་ཏུ་དངོས་པོ་མེད་ན་མེད་ལ། གལ་ཏེ་ཡོད་ན་སྐྱེ་བ་མེད་པར་ཡང་རྣམ་པར་འཇིག་པར་འགྱུར་རོ། །

[Block 669]
དེ་ལས་ཀྱང་འདུས་མ་བྱས་ཀྱང་འགྱུར་ལ། མ་སྐྱེས་པ་ཡང་འཆི་བར་འགྱུར་རོ། །

[Block 670]
དེ་ནི་འདི་ལྟར་དངོས་པོ་མེད་ན་དངོས་པོ་མེད་པ་ཡང་མེད་ལ། གང་གི་ཚེ་དངོས་པོ་མེད་པ་དག་དེ་ལྟར་དཔྱད་བཞིན་པས་ཅིག་ཅར་རམ་ཐ་དད་པར་གྲུབ་པ་མེད་པས་དེའི་ཚེ་དེ་དག་གི་རང་བཞིན་མ་གྲུབ་ན་དངོས་པོ་འཇུག་པ་མེད་དོ། །

[Block 671]
ཡང་ན་གལ་ཏེ་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་ཏུ་འཇུག་པར་མི་འགྱུར་ཡང་། དེ་ལྟ༌[^521]ན་ཡང་རེ་ཞིག་དེའི་རྟེན་དངོས་པོ་ཡོད་ལ། དེ་ཡོད་པས་བརྟེན་པའི༌[^522]དངོས་པོ་དང་དངོས་པོ་མེད་པ་ཡང་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། གང་གི་ཚེ་དངོས་པོ་ཡང་སྐྱེ་བ་མེད་ན་མེད་དོ་ཞེས་བརྗོད་པ་དེའི་ཚེ་དངོས་པོ་མེད་པ་ལས་དངོས་པོ་མི་སྲིད་དོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དངོས་པོ་མེད་པའི་མཚན་ཉིད་ཀྱི་མི་རྟག་པ་ལས་གཞན་དུ་སྟེ། དེ་མེད་པར་དངོས་པོ་སྲིད་དངོས་པོ་ཡོད་པ་ཉིད་ལ་དེ་ཡང་མེད་དོ་ཞེས་གསུངས་པར་འགྱུར་རོ། །

[Block 672]
གང་གི་ཚེ་དངོས་པོ་མེད་ན་དེའི་ཚེ་དེ་ལ་བརྟེན་པའི་སྐྱེ་བ་དང་འཇིག་པ་ག་ལ་འབྱུང་། དེ་དག་མེད་ན་དངོས་པོའི་མཚན་ཉིད་ལས་གྲོལ་བས་དངོས་པོ་མེད་དོ་ཞེས་གྲུབ་བོ།། །།

[Block 673]
འདིར་སྨྲས་པ། གལ་ཏེ་དངོས་པོའི་མཚན་ཉིད་མེད་ན་དངོས་པོ་མེད་ལ། འདི་ལྟར་དངོས་པོའི་མཚན་ཉིད་དང་འགལ་བའི་དངོས་པོ་མེད་པ་རེ་ཞིག་ཡོད་ལ། དེ་ཡོད་ན་དངོས་པོ་ཡང་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་དེ་དང་འགལ་བའི་དངོས་པོ་མེད་པ་ཡོད་ན་དངོས་པོ་ཡོད་པར་འགྱུར་ལ། དེ་ཡང་མེད་དོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 674 [HEADING]]
### ཚིགས་བཅད་ཉི་ཤུ་པ། ^1-20-0

[Block 675 [VERSE]]
དངོས་པོ་མེད་ན་དངོས་མེད་མིན། །
རང་ལས་མིན་ཞིང་གཞན་ལས་མིན། །
དེ་ཕྱིར་དངོས་པོ་དངོས་མེད་ཅིང་། །
དངོས་པོ༌[^523]མེད་པས་དེ་དག་མེད། །

[Block 676]
གང་གི་ཚེ་མི་རྟག་པ་དང་བྲལ་བའི་དངོས་པོ་བྲལ་བའི་དངོས་པོ༌[^524]མེད་དོ་ཞེས་བརྗོད་ལ། དེའི་ཚེ་དངོས་པོ་མེད་ན་དེ་ལས་བཟློག་པའི་དངོས་མེད་ཇི་ལྟར་འབྱུང་བར་འགྱུར། དེའི་ཕྱིར་དངོས་མེད་ཀྱང་མེད་དེ། ཇི་སྐད་དུ་སྨོས་པའི་རིགས་པས་དངོས་པོ་མེད་པ་འབའ་ཞིག་ཏུ་མ་ཟད༌[^525]དངོས་མེད་ཀྱང་མེད་དོ། །

[Block 677]
གཞན་ཡང་རིགས་པ་འདིས་དངོས་པོ་དངོས་པོ་མེད་པས་དངོས་པོ་མེད་པ་ཡང་མེད་དོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 678 [VERSE]]
རང་ལས་མིན་ཞིང་གཞན་ལས་མིན། །
དེ་ཕྱིར་དངོས་པོ་དངོས་མེད་ཅིང་། །

[Block 679]
ཞེས་སོ། །

[Block 680]
གལ་ཏེ་དངོས་པོ་འགའ་ཞིག་ཡོད་ན་རང་ལས་སྐྱེ་བའམ་གཞན་ལས་སྐྱེ་བར་འགྱུར། དེ་ལ་རང་གི་བདག་ཉིད་ནི་རེ་ཞིག་སྐྱེས་བཞིན་པའི་དངོས་པོའི་རང་བཞིན་ལ་སྐྱེ་བ་མེད་དེ། རང་ཞེས་བྱ་བ་བྱུང་བའི་རྣམ་པར་བྱེད་པའི་མཐའ་ཅན་སོ་སོའི་རང་བཞིན་གྱིས་བསྡུས་པ་ཡོད་པ་ཐོབ་པ་འབྲས་བུ་སྐྱེད་པར་རུང་བའི་དངོས་པོ་ལ་བརྗོད་དོ། །

[Block 681]
སྐྱེད་པ་ཞེས་བྱ་བ་ཡང་ཡོད་པ་མཐོང་བའོ།[^526] །གང་ཁོ་ནའི་དངོས་པོ་འདི་རང་ངོ་ཞེས་གྲུབ་པའི་ངོ་བོ་ཉིད་ལ་བརྗོད་ལ། དེ་ཉིད་འདི་ནི་སྐྱེད་པའོ་ཞེས་སྐྱེད་པའི་བྱ་བ་དང་ལྡན་པ་འགལ་ཏེ། འདིའི་དངོས་པོ་གཅིག་ཉིད་ལ་དེ་གལ་ཏེ་རྫོགས་པའི་རང་བཞིན་དུ་གྲུབ་ན་འདི་དེ་དང་འགལ་བའི་སྐྱེ་བཞིན་པའི་རང་བཞིན༌[^527]དུ་བརྗོད་པར་ཇི་ལྟར་འཐད། ཡང་ན་སྐྱེད་བཞིན་པའི་རང་བཞིན་དུ་བརྗོད་ན༌[^528]ཇི་ལྟར་གྲུབ་པའི་རང་བཞིན་དུ་བརྗོད་པར་ནུས། དེའི་ཕྱིར་གལ་ཏེ་དེ༌[^529]བཞིན་ཞེས་བརྗོད་ན་སྐྱེད་དོ་ཞེས་བརྗོད་པར་མི་བྱ་ལ། ཡང་ན་སྐྱེད་པ་ཞེས་བརྗོད་ན་དེ་ལ་རང་ཞེས་རྣམ་པར་མི་གཞག་གོ། །

[Block 682]
དངོས་པོར་གྱུར་པ་གཅིག་ནི་རང་ལ་ལྟོས༌[^530]ནས་གཅིག་ལ་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོར་ཡང་མི་འཐད་དོ་ཞེས་བྱ་སྟེ་དེས་ན་རང་ལས་མ་ཡིན་ནོ། །

[Block 683]
གཞན་དུ་རྣམ་པར་གཞག་པ་ནི་དངོས་པོ་གཞན་ཉེ་བ་ལ་ལྟོས་པའི་ཕྱིར་ལ་དེའི་འབྲས་བུ་ཞེས་བྱ་བའི་དངོས་པོ་མ་རྫོགས་པའི་ཕྱིར་དེ་ལ་ལྟོས་ནས་འགའ་ཡང་གཞན་ཉིད་དུ་ཡོད་པ་མ་ཡིན་ཞེས་བྱ་སྟེ། རྒྱུའི་གཞན་ཉིད་མེད་པ་ཉིད་ཀྱིས་ན་གཞན་ལས་ཀྱང་སྐྱེ་བ་མེད་དོ། །

[Block 684]
སྐྱེ་བ་མེད་པར་འགྱུར་བས་དངོས་པོ་ཡང་མེད་དོ་ཞེས་གསུངས་པ། དེ་ཕྱིར་དངོས་པོ་དངོས་མེད་ཅིང་། །ཞེས་སོ། །

[Block 685]
གང་གི་ཚེ་རིགས་པ་འདིས་དངོས་པོ་ཡང་དངོས་པོ༌[^531]མེད་པས་དེའི་ཚེ་དེ་མེད་ན་དངོས་པོ་མེད་པའི་དངོས་མེད་ཀྱང་མེད་དོ་ཞེས་གསུངས་པ། དངོས་མེད་མེད་པས་དེ་དག་མེད། །ཅེས་སོ། །

[Block 686]
དེ་ལས་གང་ཞིག་སྨོས་པ་ནི་གལ་ཏེ་དངོས་པོ་མེད་ན་ཡང་རེ་ཞིག་དངོས་པོ་མེད་པ་ཡོད་པས་དངོས་པོ་ཡང་འབྱུང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་ནི་མ་ཡིན་ཏེ། གང་གི་ཚེ་དེ་ལྟར་དངོས་པོ་ཡང་དངོས་པོ་མེད་པར་གྱུར་པས་དངོས་པོ་མེད་པ་ཡང་མེད་ལ། དེའི་ཚེ་ཡོད་པ་དང་མེད་པ་ཉིད་དུ་སྨྲ་བར་ཁས་མི་ལེན་པའི་ཕྱིར་དངོས་པོ་རྣམས་ཀྱི་ཡོད་པ་དང་མེད་པ་དག་ཡོངས་སུ་སྤངས་ནས། དབུ་མའི་རྟོགས་པ་ཕྱིན་ཅི་མ་ལོག་པར་བཤད་པར་འགྱུར་རོ། །

[Block 687]
གང་ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དངོས་པོ་ཙམ་ཞིག་ལ། གཟུང་བ་དང་འཛིན་པ༌[^532]ཁས་བླངས་པས་སྒྲོ་འདོགས་ལ། གཟུང་བ་དང་འཛིན་པ་མེད་པས་དབུ་མའི་རྟོགས་པར་བརྗོད་ལ། གཞན་དབང་དངོས་པོ་ཙམ་དུ་ཡོད་པའི་ཕྱིར་མེད་པ་ཉིད་དུ་ལྟ་བ་ཡང་དག་པ་མ་ཡིན་པར་འཛིན་པའོ། །

[Block 688]
ཀུན་བརྟགས་གཟུང་བ་དང་འཛིན་པ་ཉིད་མེད་པས་ཡོད་པ་ཉིད་དུ་ལྟ་བ་ཡང་ཡང་དག་པ་མ་ཡིན་པར་འཛིན་པའོ་ཞེས་བྱའོ། །

[Block 689]
དངོས་པོ་མེད་པ་ཁས་བླངས་པ་དེ་དག་གིས་ཡོད་པ་ཉིད་དང་མེད་པ་ཉིད་ཡོངས་སུ་སྤོང་བར་མི་ནུས་པའོ། །

[Block 690]
གཞན་དབང་དངོས༌[^533]ཙམ་ཁས་བླངས་པར་གྱུར་པ་དེ་དག་གི་ཡོད་པར་ལྟ་བ་ཁ་ན་མ་ཐོ་བ་མེད་པའོ། །

[Block 691]
ཀུན་དུ་བརྟགས་པ་གཟུང་བ་དང་འཛིན་པ་མི་སྲིད་པར་ཁས་བླངས་པར་གྱུར་ན། དེ་དག་ཀྱང་མེད་པར་ལྟ་བ་ཁ་ན་མ་ཐོ་བ་མེད་པའོ་ཞེས་བྱ་བ་དེ་རྣམས་ཀྱིས༌[^534]ཡོད་པ་ཉིད་དང་མེད་པ་ཉིད་དུ་ལྟ་བ་གང་ལ༌[^535]སྤངས་ཞེས་བྱ་སྟེ། ངེས་པར་འདི་རྣམས་འཁོར་བ་ཉིད་ལས་མི་ལྡོག་གོ། །

[Block 692]
དངོས་པོ་འབའ་ཞིག་ཁས་བླངས་ན་ཡང་ཡོད་པ་དང་མེད་པ་ཉིད་དུ་སྨྲ་བ་ལས་མ་འདས་ལ་རྟག་པ་དང་ཆད་པར་སྨྲ་བ་ཡང་ཐོབ་པར་འགྱུར་རོ། །

[Block 693]
གང་གི་ཕྱིར།

[Block 694 [HEADING]]
### ཚིགས་བཅད་ཉེར་གཅིག་པ། ^1-21-0

[Block 695 [VERSE]]
དངོས་པོ་ཡོད་ན་རྟག་པ་ཉིད། །
མེད་ནའང་ངེས་པར་ཆད་པ་ལ། །
དངོས་པོར་གྱུར་ནའང་དེ་གཉིས་ཏེ། །
དེས་ན་དངོས་པོ་ཁས་མི་བླང་། །

[Block 696]
དངོས་པོ་ཁས་བླངས་པར་གྱུར་ན་དེའི་རང་བཞིན་ཡོད་བཞིན་པས་སླར་ཡང་གཞན་དུ་གྱུར་པ་མི་སྲིད་པས་དུས་ཐམས་ཅད་དུ་ཡོད་པར་འགྱུར་བས། དངོས་པོ་དེ་རྟག་པར་ཁས་བླང་བར་བྱའོ། །

[Block 697]
གལ་ཏེ་རྟག་པར་ཁས་བླངས་ན་དེའི་ཚེ་ཐེར་ཟུག་ཐོབ་པར་འགྱུར་ཏེ། དུས་ཐམས་ཅད་དུ་གནས་པའི་ཕྱིར་རོ། །

[Block 698]
ཡང་ན་གལ་ཏེ་འཇིག་པར་གྱུར་ན་དེའི་ཚེ་དངོས་པོ་མེད་པར་ཁས་བླངས་པར་གྱུར་པས་འདི་ནི་མེད་པ་ཐོབ་པར་འགྱུར་རོ། །

[Block 699]
དེ་ལས་ཀྱང་སྔར་བྱུང་ལ་ད་ནི་མེད་དོ་ཞེས་པའི་དོན་ཁས་བླངས་པར་གྱུར་པས་ཆད་པར་ལྟ་བ་ཐོབ་སྟེ། ཞིག་པ་ནི་སླར་ཡང་མི་འཇུག་པས་སོ། །

[Block 700]
རྟག་པ་དང་ཆད་པའི་མཐར་འཛིན་པ་ལས་མཐར་འཛིན་པའི་ལྟ་བ་རིགས་པས༌[^536]ཐོབ་ལ། རིགས་པའི་སྟོབས་ལས་འོངས་པས་སྤང་བྱར་མི་འགྱུར་ཏེ། ཡང་དག་པའི་ལྟ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 701]
དེ་ལས་མཐའ་གཉིས་སྤངས་ནས་ཞུགས་པའི་ལན༌[^537]འདི་ཡང་ཕྱིན་ཅི་ལོག་ཉིད་དུ་འགྱུར་ལ། གང་གི་ཚེ་རིགས་པས་དཔྱད་ན་དངོས་པོ་རྣམ་པ་ཐམས་ཅད་དུ་མེད་ན་དེའི་ཚེ་དེའི་ཡུལ་རྟག་པ་དང་ཆད་པར་ཡོངས་སུ་བརྟགས་པས༌[^538]ཡང་དག་པའི་ལྟ་བ་མ་ཡིན་ནོ་ཞེས་འཐད་དོ། །

[Block 702]
གང་ཡང་ཡང་དག་པའི་ལྟ་བ་མ་ཡིན་པ་དེ་ནི་ངེས་པར་སྤང་བར་བྱ་ལ། དེ་སྤོང་བའི་ཐབས་ཀྱང་རང་བཞིན་ཁས་མ་བླངས་པ་ཡིན་ནོ་ཞེས་བྱ་སྟེ། དངོས་པོ་བཀག་པས་མྱ་ངན་ལས་འདས་པར་འགྲོ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིར་ཐར་པར༌[^539]འདོད་པ་རྣམས་ཀྱིས་ཁས་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བར་འགྱུར་རོ། །

[Block 703]
འདིར་སྨྲས་པ། བདག་དང་བདག་གི་བའི་རྣམ་པ་ནི་འཇིག་ཚོགས་སུ་ལྟ་བ་ལ། གང་གི་ཚེ་བདག༌[^540]ཉིད་དུ་དམིགས་པ་དེ་ཉིད་རྟག་པ་དང་ཆད་པའི་མཐར་ཡོངས་སུ་བརྟགས་པ་ལས་མཐར་འཛིན་པའི་ལྟ་བ་སྐྱེད་ལ། དེ་ཡང་སྤང་བྱ་ལ་ཆོས་ཙམ་ནི་རྟག་པ་དང་ཆད་པའི་ལྟ་བར་མི་དམིགས་སོ་ཞེས་བྱ་སྟེ། དེས་ན་གལ་ཏེ་ཡང་ཕུང་པོ་རྣམས་མྱ་ངན་ལས་འདས་ནས་སླར་མི་འཇུག་ན། དེ་ལྟ་ན་ཡང་ལྟ་བ་དེ་ནི་ཆད་པར་ལྟ་བ་མ་ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 704]
འོ་ན་འཇིག་ཚོགས་སུ་ལྟ་བ་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་ལ་བདག་དང་བདག་གི་བའི་རྣམ་པར་དམིགས༌[^541]ལ། དེ་ལྟ་ན་ཡང་མུ་སྟེགས་བྱེད་ཀྱིས་བརྟགས་པའི་བདག་གི་རྣམ་པར་དམིགས་བཞིན་པ་ན་དེའི་དབང་གིས་འདུ་བྱེད་རྣམས་ལ་ཡང་བདག་གི་བའི་རྣམ་པར་དམིགས་པས་འཇུག་གོ། །

[Block 705]
འོ་ན་འདི་ཡང་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་ལ་དམིགས་པར་འགྱུར་གྱི། ཁྱད་པར་ནི་འདི་དག་སྟེ། གང་དུ་དེ་དག་ལ་བདག་དང་བདག་གི་བའི་རྣམ་པར་དམིགས་ནས་ཡོངས་སུ་འཛིན་ཅིང་དེ་ལས་ཀྱང་མཐར་འཛིན་པར་ལྟ་བས་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ་དེ་ཉིད་ལ་རྟག་པ་དང་ཆད་པའི་རྣམ་པས་དམིགས་སོ་ཞེས་བྱའོ། །
--- END BLOCKS ---
