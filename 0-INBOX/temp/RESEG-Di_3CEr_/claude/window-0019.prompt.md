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
གང་གི་ཕྱིར་ཐ་དད་རྣམས་ཀྱི་རྗེས་སུ་འགྲོ་བ་བོར༌[^510]ཚོད་ལ་སོགས་པས་གཙོ་བོ་དང་སྐྱེས་བུ་རྟོགས་པར་བྱེད་པས་ན༌[^511]དེ་ཉིད་གཙུག་ཕུད་ཅན་གྱི་དོན་བསྒྲུབས་པས་ཏེ།[^512] དེའི་ཕྱིར་གཙོ་བོ་ཡོད་པ་ཉིད་ལ་སོགས་པ་རྟོགས་པར་བྱེད་པའི་གཏན་ཚིགས་ཡིན་གྱི། བསྐྱེད༌[^513]བྱ་སྐྱེད་བྱེད་ཀྱི་དངོས་པོ་ནི་མ་ཡིན་ནོ། །

[Block 667]
འདི་ལྟར་གཙོ་བོ་ཡོད་པ་ཉིད་ལ་སོགས་པ་དང་རྗེས་སུ༌[^514]འགྲོ་བ་ལ་སོགས་པ་དེ་རྗེས་སུ་བསྒྲུབས༌[^515]ན་ནི།

[Block 668 [VERSE]]
དེ་བཞིན་ནོར་དང་ནོར་ཅན་ལ། །
མཚོན་ནས་གསལ་བྱེད་མ་ཡིན་ཉིད། །
འབྲེལ་བ་ལས་ཀྱང་དེ་མཚོན་ཕྱིར། །
འབྲེལ་མེད་ཉིད་དུ་ཡང་དག་བརྗོད། །

[Block 669]
འབྲེལ་བ་ཅིག་ཤོས་ལ་ནི་ཆ་འགའ་ཞིག་ལས་རྟགས་དང་རྟགས་ཅན་དུ་འགྱུར་གྱི་གང་ནོར་དང་ནོར་ཅན་ལ་སོགས་པ་ལ་ནི་མ་ཡིན་ཏེ། འདི་ལྟར་རྣམ་པ་ཐམས་ཅད་དུ་ཕན་ཚུན་གཟུང་བ་དང་འཛིན་པར་འགྱུར་བས་ནའོ། །

[Block 670]
ནོར་ལ་སོགས་པ་ནི་ཆ་གང་གི་སྒོ་ནས་ཀྱང་གསལ་བྱེད་ཉིད་མ་མཐོང་ངོ་། །དེའི་ཕྱིར་འབྲེལ་པ་གཞན་ཉིད་ལས་དོན་བརྗོད་པ་ཡིན་ནོ། །

[Block 671]
གཞན་ཡང་།

[Block 672 [VERSE]]
ནོར་དང་ནོར་ཅན་ལ་སོགས་ཙམ། །
རྟགས་ཅན་འཛིན་པ་ཡིན་ན་ནི། །
འབྲེལ་བ་ལས་གཞན་ཤེས་པས༌[^516]ན། །
རྣམ་པ་ཀུན་ཏུ་འཛིན་པར་འགྱུར། །

[Block 673]
ནོར་གྱི་ཆ་ནས་ནོར་ཅན་ཉིད་ཙམ་གསལ་བར་བྱེད་ཅིང་རྟགས་ཅན་གོ་བར་བྱེད་པ་ཡིན་ན་ནི་འབྲེལ་བའི་སྒོ་ནས་འཛིན་པ་པོར་ནས་རྟགས་གཞན་ལས་ནོར་གྱི་དོན་བརྗོད་པར༌[^517]ནུས་པ་མ་ཡིན་ནོ། །

[Block 674]
དེ་ལས་ཤིན་ཏུ་འདས་ན་ཡང་བདག་ཉིད་ཐམས་ཅད་ནས་རྟགས་ཅན་འཛིན་པར་འགྱུར་རོ་ཞེས༌[^518]ཐལ་འགྱུར་སེམས་པས་ཆོག་གོ། །

[Block 675]
དེ་ལྟར་རེ་ཞིག་གཙོ་བོ་དང་རྗེས་སུ་འགྲོ་བ་ལ་སོགས་པ་རྒྱུ་དང་རྒྱུ་ཅན་ཉིད་ཀྱི་བསྐྱེད་པར་བྱ་བ་དང་སྐྱེད་པར་བྱེད་པ་པོའི་དངོས་པོ་མ་ཡིན་ནོ། །

[Block 676]
གསལ་བྱ་གསལ་བྱེད་ཀྱི་དངོས་པོའོ།[^519] །གལ་ཏེ་གཅིག་ཡིན་རྣམ་བདུན་མིན། །

[Block 677]
གསལ་བྱ་གསལ་བྱེད་ཀྱི་དངོས་པོ་ཉིད་ཡིན་ན་ནི་ནོར་དང་ནོར་ཅན་ལ་སོགས་པའི་ཐ་དད་པ༌[^520]ལས་དེ་དག་རྣམ་པ་བདུན་དུ་དབྱེ་བར་མི་བྱའོ། །

[Block 678]
དེའི་གཅིག་ཁོ་ན་གསལ་བྱེད་མ་ཡིན་པ་མ་ཡིན་དུ་ཆུག་ན། ཅིག་ཤོས་རྣམས་ནི་གསལ་བྱེད་དུ་མི་འགྱུར་རོ། །

[Block 679]
རྒྱུ་དང་རྒྱུ་ཅན་གྱི་དངོས་པོ་ལས་ཐ་དད་པ་ཡིན་པའི་ཕྱིར་འབྲེལ་བ་གཞན་ཉེ་བར་དམིགས་པ་ཉིད་འདིར་འདིའི་གསལ་བར་བྱེད་པར་འགྱུར་རོ། །

[Block 680]
དེའི་ཕྱིར་རྗེས་སུ་དཔོག་པར་བྱེད་པའི་རྒྱུ་གཞན་ནི་དོན་མེད་དོ་ཞེས་སྔར་བརྗོད་ཟིན་ཏོ། །

[Block 681]
རྒྱུ་དང་རྒྱུ་ཅན་གྱི་དངོས་པོའི་ཞེས་ཀྱང་བརྗོད་པར་མི་བྱ་སྟེ། གང་གི་ཕྱིར་རྗེས་སུ་དཔོག་པར་བྱེད་པའི་རྒྱུ་ཉིད་ནི་གསལ་བར་བྱེད་པ་ཉིད་ཡིན་པས་ནའོ། །

[Block 682]
རྒྱུ་ཅན་ཉིད་ཅེས་པ་ནི་གསལ་བར་བྱ་བ་གསལ་བར་བྱེད་པ་ཉིད་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 683 [HEADING]]
##### ལྷན་ཅིག་རྒྱུ་བའི་དངོས་པོ། ^2-5-1-3-0

[Block 684]
གང་ཡང་ལྷན་ཅིག་རྒྱུ་བའི་དངོས་པོའི་འབྲེལ་བ་ནི་གཙོ་བོ་ལ་སོགས་པ་དང་རྗེས་སུ་འགྲོ་བའི་ཞེས་པ༌[^521]ལའང་། གལ་ཏེ་གཅིག་ཡིན་རྣམ་བདུན་མིན། །ཞེས་པ་དེ་ཉིད་ཀྱི༌[^522]ལན་གདབ་པོ། །གང་ལྷན་ཅིག་ཏུ་རྒྱུ་བ་དེ་གཅིག་པུ་མེད་ན་མི་འབྱུང་བ་ཉིད་ཡིན་ན་ནི་ནོར་དང་ནོར་ཅན་ལ་སོགས་པ་ལྷན་ཅིག་རྒྱུ་བ་མ་ཡིན་པས་དེ་དག་ལས་རྗེས་དཔག༌[^523]མ་ཡིན་པར་འགྱུར་རོ། །

[Block 685]
ལྷན་ཅིག་རྒྱུ་བའི་དངོས་པོ་ལས་ལྷག་མ་དང་ལྡན་པའི་རྗེས་སུ་དཔག་པ་སྲིད་དོ་ཞེས་པ་ནི་མ་ཡིན་ཏེ། དེས་དབང་པོ་ལས་འདས་པའི་དོན་ཇི་ལྟར་ཁོང་དུ་ཆུད། དེའི་ཕྱིར་དེ་ལྟ་བུའི་འབྲེལ་བ་ནི་རྗེས་སུ་དཔག་པའི་རྒྱུ་མ་ཡིན་ནོ། །

[Block 686 [HEADING]]
#### བྱེ་བྲག་མཐོང་བ་དང་སྤྱི་མཐོང་བ། ^2-5-2-0

[Block 687]
གང་ཡང་རྗེས་སུ་དཔག་པ་ནི་རྣམ་པ་གཉིས་ཏེ། བྱེ་བྲག་མཐོང་བ་དང་སྤྱི་མཐོང་བའོ་ཞེས་བརྗོད་པ་དེ་ལ་རེ་ཞིག་བྱེ་བྲག་མཐོང་བ་ནི་རྗེས་སུ་དཔག་པ་ཉིད་དུ་མི་འདོད་དོ། །

[Block 688]
[^524]ཅིའི་ཕྱིར་ཞེ་ན། དེ་དྲན་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 689]
སྔར་ཉམས་སུ་མྱོང་བའི་དྲན་པ་གཞག་ནས༌[^525]ཤེས་པ་གཞན་ལ་དེ་འདི་ཉིད་ཡིན་ནོ་ཞེས་པ་ནི་རྗེས་སུ་དཔག་པ་མ༌[^526]ཡིན་ནོ། །

[Block 690]
སྤྱིར་མཐོང་བ་ནི་རྣམ་པ་གཉིས་པོ་ཞེས་པ༌[^527]འདི་ལ་རེ་རེའམ་གཉིས་ཀ་ཡང་རུང་སྟེ། ངེས་པར་གཟུང་བ་རིགས་པ་མིན། །ཇི་ལྟ་བུར་ཞེས་པར༌[^528]གཟུང་བར་བྱ་བ་གལ་ཏེ་རེ་ཞིག་སྤྱིར༌[^529]མཐོང་པ་ཁོ་ན་རྣམ་པ༌[^530]གཉིས་སོ་ཞེས་པ་དེ་ལྟ་ན་ནི། འབྲས་བུ་དང་རྒྱུ་དག་ལས་ཡང་ནས་ཡང་དུ་རྗེས་སུ་དཔོག་པ་མེད་པར་འགྱུར་རོ། །

[Block 691]
ཅི་སྟེ་སྤྱིར༌[^531]མཐོང་བ་རྣམ་པ་གཉིས་ཁོ་ན་ཡིན་ན་ནི་ནོར་དང་ནོར་ཅན་དང༌[^532]ལྷན་ཅིག་ཏུ་རྒྱུ་བ་དང་། གནོད་བྱ་གནོད་བྱེད་ཀྱི་འབྲེལ་པ༌[^533]ཅན་དེ་རྣམས་ཀྱི་དང་པོ་ནི་རྗེས་སུ་དཔག་པར་མི་འགྱུར་རོ། །

[Block 692]
དེ་དག་ནི་རྒྱུ་འབྲས་ཀྱི་དང་པོ་མ་ཡིན་ཞིང་བྱེ་བྲག་འཛིན་པ་ཡང༌[^534]མ་ཡིན་ནོ། །

[Block 693]
དེ་སྐད་དུ། ཡང་སྨྲས་པ།

[Block 694 [VERSE]]
འབྲེལ་བ་བདུན་དུ་བསྟན་པ་དང་། །
རྗེས་སུ་དཔག་པ་གཉིས་ཉིད་དང་། །
དེ་སྔོན་སོང་བའི་རྗེས་དཔག་གསུམ། །
འདི་དག་གང་གི་ཁོངས་སུ་བསྡུ། །

[Block 695]
གལ་ཏེ་ཡང་འདི་ལྟར་ནོར་བདག་ནི༌[^535]བྱེད་པ་པོ་ཡིན་ཞིང་ནོར་ནི་བྱ་བ་མ༌[^536]ཡིན་ནོ། །

[Block 696]
རྗེས་སུ་གཟུང་བར་བྱ་བ་དང་འཛིན་པར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེ་ན།[^537] དེ་ནི་མ་ཡིན་ཏེ། འབྲེལ་པ་གཞན་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 697]
ཐམས་ཅད་དུ་ཤེས་པར་བྱ་བ་དང་ཤེས་པར་བྱེད་པ་ཉིད་དུ་ཁས་ལེན་པར་བྱེད་པ་ཡིན་ན་ནི་ཕན་འདོགས་པ༌[^538]ཡིན་པའི༌[^539]ཕྱིར་རོ། །

[Block 698]
དེ་དག་ནི་གཉིས་སོ་ཞེས་ངེས་པར་བཟུང་བ་དེ་དག་ངེས་པར་གཟུང་བར༌[^540]མི་བྱ་སྟེ། འབྲས་བུ་མེད་པའི༌[^541]ཕྱིར། སྤྱིར་མཐོང་བ་ནི་རྣམ་པ་གཉིས་སོ་ཞེས་པའི་ཚིག་གི་འབྲས་བུ་ཅི་ཞིག་ཡིན། གལ་ཏེ་གཞན་ལ་ཡང་རྣམ་པ་གཉིས་ཡོད་པ་དེ་ལྟ༌[^542]ན་ནི་རྣམ་པ་མང་པོ་ཉིད་དུ་འགྱུར་རོ། །

[Block 699 [HEADING]]
#### དེ་སྔོན་སོང་བའི་རྗེས་དཔག་གསུམ། ^2-5-3-0

[Block 700]
གང་ཡང་ཇི་སྐད་དུ་སྔ་མ་དང་ལྡན་པའི་རྗེས་སུ་དཔག་པ༌[^543]འཁྲུལ་པ་ཅན་ནོ་ཞེས་བརྗོད་པ་དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། འབྲེལ་པ་ཅན་རྣམས་ལ་འཁྲུལ་པ༌[^544]མེད་པའི་ཕྱིར་རོ། །

[Block 701]
རྒྱུ་ལ༌[^545]ནི་གེགས་བྱེད་པ་ལ་སོགས་པ་ཡང་སྲིད་ལ་འབྲས་བུ་མེད་པར་ཡང་འབྱུང་བའི་ཕྱིར་འཁྲུལ་པས་ན་རྗེས་སུ་དཔག་པ་མ་ཡིན་ནོ། །

[Block 702]
གལ་ཏེ་རྒྱུ་ཉིད༌[^546]རྗེས་སུ་དཔག༌[^547]པར་བྱེད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རྗེས་སུ་དཔག་པ༌[^548]ཉེ་བར་བརྟགས་ནས་བརྗོད་པར་བྱའོ་ཞེ་ན།[^549] དེ་ལྟར་ཡང་རིགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་གལ་ཏེ་འཁྲུལ་ན་ནི། དེ་རྟགས་མིན། ཅིའི་ཕྱིར་ཞེ་ན། དེ་ལས་ནི་དོན་དེའི་རྟགས་མ་ཡིན་ཏེ། ཐེ་ཚོམ་བསྐྱེད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 703]
དེའི་ཕྱིར་འདིར་རྗེས་སུ་དཔག་པ་ཉེ་བར་གདགས་པ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 704]
རྒྱུ་ལ་འབྲས་བུའི་ཤེས་པ་དེ་འབྱུང་བ་སྲིད་ཀྱང་རྟགས་འཁྲུལ་པར་ངོ་ཤེས་པའི་ཕྱིར་རོ། །

[Block 705]
འཁྲུལ་པར་བརྗོད་དོ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། དེའི་ཚེ་དེའི་རྒྱུ་མ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
