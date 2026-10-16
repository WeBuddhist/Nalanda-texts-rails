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
དོན་དེ་ནི་གཞན་གྱིས་བསྒྲུབ་པའི༌[^526]ཕྱིར་རོ། །

[Block 667]
དེ་ལ་ཁས་བླངས་པ་ཡང་གདོན་མི་ཟ་བར་བྱ་དགོས་པའི་ཕྱིར་རོ། །

[Block 668]
གཞན་ཡང་།

[Block 669 [VERSE]]
དེ་ལས་གཞན་པ་ཡོངས་སྤངས་ནས། །
འཇུག་འགྱུར་ཞེས་ཀྱང་སྒྲ་བརྗོད་དེ། །
དེ་ཡིས་དེ་དག་རྣམས་ལས་འདི། །
རྣམ་མི་གཅོད་པ༌[^527]དེ་ཇི་ལྟར། །

[Block 670]
འདི་དོན་རྣམས་ལ་སྒྲ་སྦྱོར་བ་ན་མི་འདོད་པ་ཡོངས་སུ་སྤངས་ནས་འཇུག་པར་འགྱུར་སྙམ་ནས་སྦྱོར་ཏེ། དེ་དང་གཞན་ལ་ཡང་འཇུག་ཏུ་སྣང་ལ། འཇུག་པ་དང་ལྡོག་པ༌[^528]ཡང་འཇུག་ཏུ་སྣང་ན་ནི་མིང་སྨོས་པ་དོན་མེད་པའི་ཕྱིར་རོ། །

[Block 671]
གཞན་ལས་ལྡོག་པ་མི་བརྗོད་ན་ནི་གཅིག་བརྗོད་པ་ལ་མི་གུས་པའི་ཕྱིར། བརྗོད་པར་བྱ་བ་མ་ཡིན་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 672]
དེ་ལྟ་བས་ན་གདོན་མི་ཟ་བར་རྣམ་པར་བཅད་པ་བརྗོད༌[^529]དགོས་སོ། །

[Block 673]
དེ་ཡང་དེ་ལས་གཞན་པ་དག་ལ་ཐ་མི་དད་པ་ཡིན་ལ་རིགས་ཀྱི་ཆོས་ཀྱང་ཡོད་དོ། །

[Block 674]
དེ་ངེས་པར་ཁས་བླང་བ་ཅན་དང་། གདོན་མི་ཟ་བར་བརྗོད་པ་ཅན་དང་། རིགས་ཀྱི་དོན་རབ་ཏུ་སྒྲུབ་པ༌[^530]ཡོངས་སུ་བོར་ནས་དོན་གཞན་དུ་རྟོག་པ༌[^531]ནི་དོན་མེད་པ་ལ་གཙིགས་པོ་ཆེར་འཛིན་པ་འབའ་ཞིག་ཏུ་ཟད་དོ། །

[Block 675]
དེ་ལྟར་བརྟགས་པ་བཞིན་དུ་དེ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 676]
རྣམ་པར་གཅོད་པར་མི་བྱེད་པ་ནི་མ་ཡིན་གྱི་འཇུག་པའི་ཡུལ་བརྗོད་པས་རིགས༌[^532]སྨྲས་སོ་ཞེ་ན།

[Block 677 [VERSE]]
གལ་ཏེ་འདི་ལ་རྣམ་གཅོད་ཡོད། །
སྒྲ་རྣམས་དགོས་པ་དེ་ཙམ་དུ། །
ཟད་པ་མིན་ནམ་ཁྱེད་ལ་དེར། །
སྤྱི་གཞན་གྱིས་ནི་ཅི་ཞིག་བྱ། །

[Block 678]
འཇུག་པའི་ཡུལ་རབ་ཏུ་སྟོན་ཏོ་ཞེས་སྨྲས་པ་མ་ཡིན་ནམ་ཞེ་ན། དེ་སྐད་ནི་སྨྲས་ན་རིགས་པར་ནི་མ་སྨྲས་ཏེ། འདི་ལྟར་དེ་ནི་འཇུག་པར་རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་དེ་སྐད་དུ་བསྟན་ཟིན་ཏོ། །

[Block 679]
དེའི་སྒོ་ནས་མ་བརྗོད་པ་ལ་འཇུག་པ་ལ་ཡང་བསལ༌[^533]ཟིན་ཏེ། [^534]དེ་དང་ལྡན་པ་བརྗོད་ན་ནི་བར་དུ་གཅོད་པ་ཡོད་དོ། །

[Block 680]
རིགས་དང་དེ་དང་ལྡན་པ་དག་འཇུག་པའི་ཡུལ་ཉིད་ཡིན་ན་ལྡོག་པ་དང་། དེ་དང་ལྡན་པ་དག་ཡིན་པར་ཅི་སྟེ་མི་འདོད། གལ་ཏེ་ལྡོག་པ་དངོས་པོ་མེད་པ་ཉིད་ཀྱིས་སྒྲུབ་པ་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེ་ན། དེ་ནི་རིགས་པ༌[^535]ཡང་མཚུངས་སོ། །

[Block 681]
གལ་ཏེ་དེ་དང་ལྡན་པས་བསྒྲུབ་པའི༌[^536]ཕྱིར་ཉེས་པ་མེད་དོ་ཞེ་ན། དེ་ནི་ལྡོག་པ་དང་ལྡན་པར་ཡང་མཚུངས་སོ། །

[Block 682]
ལྡོག་པ་སྨྲ་བ་རྣམས་ཀྱི་ལྟར་ན་སྒྲའི་ཤེས་པ་དངོས་པོ་མི་འཛིན་པ་ཉིད་ཡིན་ཏེ། དེ་ནི་འཁྲུལ་པའི་དབང་གིས་བྱེད་པ་པོ་མ་ཡིན་པ་ལ་ཡང་བྱེད་པ་པོར་ལྷག་པར་ཞེན་པས་འཇུག་པར༌[^537]བྱེད་དོ། །

[Block 683]
དངོས་པོ་འཐོབ་པ་ནི་དངོས་པོ་ལས་སྐྱེ་བས༌[^538]དེ་དང་འབྲེལ་པ་ཡིན་ན་འགྱུར་གྱི་གཞན་དུ་མི་འགྱུར་བ་ཁོ་ནའོ། །

[Block 684]
གལ་ཏེ་དངོས་པོ་ལས་སྐྱེ་བའི༌[^539]ཕྱིར་མི་འཁྲུལ་པར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་མི་སྣང་བ་དེར་ལྷག་པར་ཞེན་པའི་ཕྱིར་དང་། འོད་ལ་ནོར་བུར་འཁྲུལ་བར་སྣང་བས་འཁྲུལ་པའི་ཕྱིར་རོ། །

[Block 685]
གལ་ཏེ་འཁྲུལ་པའི་ཕྱིར་དངོས་པོ་ཐོབ་པ་མ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། ཇི་སྐད་བཤད་པ་ལྟ་བུ་ཁོ་ནས་འཁྲུལ་པའི་ཕྱིར་རོ། །

[Block 686]
འཁྲུལ་པའི་མཚན་ཉིད་ནི་ལོག་པར་སྣང་བ་ཡིན་ལ། ཐོབ་པར་བྱེད་པ་ནི་དེ་མེད་ན་མི་འབྱུང་བ་ཉིད་ཀྱིས་ཡིན་གྱི། སྣང་བ་ལ་ལྟོས་པས༌[^540]ནི་མ་ཡིན་ནོ། །

[Block 687]
དངོས་པོ་ལ་ངོ་བོ་ཇི་ལྟ་བ་བཞིན་སེམས་གཏད་པས༌[^541]འཇུག་ན་ནི་གཟུང་བར་བྱ་བ་སྤྱི་དོན་བྱེད་པར་རུང་བ་མ་ཡིན་པའི་ཕྱིར། དེ་ལ་ནི་འཇུག་པར་མི་འགྱུར་རོ། །

[Block 688]
གཞན་ལ་ཡང་འཇུག་ན་ནི་ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 689]
དེ་དང་ལྡན་པ་འཛིན་ན་ཡང་སྤྱི་དོན་མེད་པ་ལ་སོགས་པར་བཤད་ཟིན་ཏོ། །

[Block 690]
གལ་ཏེ་རིགས་གཟུང་ན་ཡང་འབྲེལ་པའི་ཕྱིར་རོ། །

[Block 691]
འདྲེས༌[^542]པར་སྣང་བའི་བློས་འཇུག་པར་བྱེད་དོ་ཞེ་ན། དེའི་ཚེ་གཅིག་གི་ཡང་རང་གི་ངོ་བོར་གནས་པ་མ་བཟུང་བའི་ཕྱིར། རིགས་ཀྱང་མ་ཡིན་ལ་དེ་དང་ལྡན་པ་ཡང་མ་ཡིན་པས་གཞན་གྱི་སྨྲ་བ་ཁོ་ན་ལ་བརྟེན་པར་འགྱུར་རོ། །

[Block 692]
དེ་ལྟ་ན་ནི་འོ་ན་རྗེས་སུ་འགྲོ་བ་འགའ༌[^543]ཡང་མེད་པའི་ཕྱིར། རང་བཞིན་གྱིས་ཐ་དད་པའི་དོན་རྣམས་ལ་དེ་ཉིད་འདི་ཡིན་ནོ། །ཞེས་ངོ་ཤེས་པར་ཡང་མི་འགྱུར་རོ་ཞེ་ན། ཉེས་པ་མེད་དེ། འདི་ལྟར།[^544] །

[Block 693 [VERSE]]
ཐ་དད་ཀྱང་ནི་ཤེས་སོགས་དོན། །
བྱ་བ་དེ་དང་དེ་བྱེད་པའི། །
དེ་རྣམས་མཐོང་ནས་གཞན་མཐོང་ཡང་། །
དེ་ལས་གཞན་དང་བྲལ་བ་ཡི། །
ཡུལ་ཅན་གྱི་ནི་སྒྲ་རྣམས་ཀྱིས། །
ལྷན་ཅིག་སྦྱོར༌[^545]ནས་ངོ་ཤེས་བྱེད། །

[Block 694]
འདི་ནི་བཤད་ཟིན་ཏེ། དངོས་པོ་ཐ་དད་ཀྱང་དོན་འདྲ་བ་དག་བྱེད་པ་ཡིན་ཏེ། མིག་ལ་སོགས་པ་བཞིན་ནོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 695]
དེ་དག་ལ་ཤེས་པ་ལ་སོགས་པའི་དོན་བྱེད་པ་གཅིག་པ་དེ་མཐོང་བ་ལ་གཞན་དག་ལས་ཐ་དད་པའི་དངོས་པོ་རྣམས་ཀྱི༌[^546]ཆོས་ཉིད་ཁོ་ནས་དེ་ཉིད་འདི་ཡིན་ནོ༌[^547]སྙམ་པའི་ཤེས་པ་དེ་ལས་ལྡོག་པའི་ཡུལ་ཅན་གྱི་སྒྲ་དང་འབྲེལ་པ་ཁྱད་པར་བསྲེས་པ་རང་ཉམས་སུ་མྱོང་བའི་བག་ཆགས་སད་པས་སྐྱེད་པར་བྱེད་དོ། །

[Block 696]
དེ་ལྟ་མ་ཡིན་ན་བློ་ཁྱད་པར་ཅན་བསྲེ་བ་ཅན་དུ་མི་འགྱུར་ཏེ། དཔེར་ན་ལྟུང༌[^548]ལ་བརྒྱུས་པ་དག་ལྟ་བུའོ། །

[Block 697]
དེ་ལ་ལྟུང་བ་གཅིག་དང་ལྡན་པ་ཡང་གཞན་ལ་དེ་ཉིད་འདི༌[^549]ཡིན་ནོ་སྙམ་དུ་མི་སེམས་ཀྱི། འོན་ཀྱང་དེ་འདི་ལ་ཡོད་དོ་སྙམ་མོ། །

[Block 698]
ངོ་ཤེས་པ་ནི་དེ་ལྟ་ཡང་མ་ཡིན་ནོ། །

[Block 699]
འོ་ན་ཅི་ཞེ་ན། དེ་ཉིད་འདི་ཡིན་ནོ་སྙམ་པ་ཡིན་ནོ། །

[Block 700]
དེ་བས་ན་གཅིག་ཅིག་ཏུ་མ་མཐོང་བ་ལ་ཡང་ཁྱད་པར་བསྲེ་བ་དང་ལྡན་པར་རིགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 701]
འཁྲུལ་པའི་དབང་གིས་དེ་ལྟར་སྣང་བ་ལ་ནི་འགལ་བ་མེད་དོ། །

[Block 702]
གལ་ཏེ་རྒྱུ་མཚན་མེད་པའི་ཕྱིར་འཁྲུལ་པར་རིགས་པ་མ་ཡིན་ནོ་ཞེ་ན། དངོས་པོ་དོན་དེ་གཅིག་བྱེད་པ་དེ་དག་ཉིད༌[^550]ཉམས་སུ་མྱོང་བའི་སྒོ་ནས་རང་བཞིན་གྱིས༌[^551]འཁྲུལ་པའི་འབྲས་བུ་ཅན་གྱི་རྣམ་པར་རྟོག་པའི་བག་ཆགས་ཀྱི་རྒྱུ་ཡིན་པའི་ཕྱིར་རྒྱུ་མཚན་ཡིན་ནོ། །

[Block 703]
སྨིག་རྒྱུ་ལ་སོགས་པ་ལ་ཆུ་ལ་སོགས་པར་འཁྲུལ་པའི་རྒྱུ་ཡང་ཐ་དད་ཀྱང་རྣམ་པ་ཐ་མི་དད་པར་བསྙེམས་པའི༌[^552]ཤེས་པའི་རྒྱུ་མཚན་ཉམས་སུ་མྱོང་བ་སྐྱེད་པར་བྱེད་པའི་ངོ་བོ་དེ་དག་ཉིད་ཡིན་ནོ། །

[Block 704]
དེ་ལ་གང་དེ་ལྟར་ཤེས་པར་འགྱུར་བ་གཞན་སྤྱི་ནི་ཅུང་ཟད་ཀྱང་མེད་པ་ཁོ་ནའོ། །

[Block 705]
འོན་ཏེ་ཡོད་ན་ནི་དོན་ཡོད་པ་འཛིན་པའི་བློ་འཁྲུལ་པར་མི་འགྱུར་རོ། །
--- END BLOCKS ---
