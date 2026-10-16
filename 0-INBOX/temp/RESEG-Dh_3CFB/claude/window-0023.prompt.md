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
[Block 806]
དེའི་ཕྱིར༌[^656]གཞན་སེལ་ཡུལ་ཅན་དེ།[^657] །དེ་བྱེད་བརྟེན་པའི་ངོ་བོའི་བྱེད།[^658] །ངོ་བོ་ཉིད་གཅིག་དང་བྲལ་བའི་དོན་རྣམས་ལ་དེ་སྒྲོ་བཏགས་ནས་སྐྱེ་བའི་བློ་ཕྱིན་ཅི་ལོག་ཏུ་སྣང་བའི་ཕྱིར་བྱ་བ་བྱེད་པ་མ་ཡིན་ཡང་དེ་བྱེད་པ་ལྟ་བུར༌[^659]ལྷག་པར་ཞེན་པའི་དངོས་པོ་ཐ་དད་པའི་ངོ་བོ་ཙམ་གྱིས་ས་བོན་ཅན༌[^660]མཚུངས་པ་ཉིད་དུ་ལྷག་པར་ཞེན་པ༌[^661]ཕྱིན་ཅི་ལོག་པ་བསྐྱེད་པའི་མཉན་པ་ཡང་དེ་ལས་གཞན་པའི་ཡོངས་སུ་སྤོང་བའི་ཡན་ལག་གི་ངོ་བོའི་ཕྱིར། དོན་དམ་པར་དེ་ལས་ཐ་དད་པའི་དོན་དག་ལ་མི་སླུ་བ་ཞེས་བྱའོ། །

[Block 807]
འདི་ལྟར་ཐ་དད་པ་དེ་ནི་དེ་དག་ལ་ཡང་དག་པ་ཡིན་ཏེ། རྣམ་པ༌[^662]ཐམས་ཅད་དུ་འདའ་བར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 808]
ཐ་དད་པའམ་ཐ་མི་དད་པ་ནི་མ་ཡིན་ཏེ། རྣམ་པ་ཐམས་ཅད་དུ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 809]
དེ་དངོས་པོ་ལ་འགོད་ན་ནི་སྒྲ་དང་ཤེས་པ་དག་ལས་དངོས་པོ་ཐག་བསྲིངས་པ་ཁོ་ནར་འགྱུར་ཏེ། དེའི་ཡུལ་དུ་འདོད་པ༌[^663]མེད་པའི་ཕྱིར་དང་། དངོས་པོའི་ཆོས་གཞན་ཡང་འགགས་ལ༌[^664]ཡང་རེག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 810]
དེ་ཉིད་ཀྱི་ཕྱིར་མཉན་པ་དེ་ནི་གཞན་སེལ་བའི་ཡུལ་ཅན་ཞེས་བྱ༌[^665]སྟེ། གཞན་ལོག་པའི་དོན་རྣམས་ལ་བྱེ་བྲག་མེད་པར་ལྡོག་པའི་ཁྱད་པར་ལ་བརྟེན་ནས་བཀོད་པའི༌[^666]ཕྱིར་དང་། ཐ་སྙད་ལ་ཡང་གཞན་སྤངས་ནས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 811 [VERSE]]
ཤིང་མ་ཡིན་ལས་ལྡོག་པ་ནི། །
ཤིང་དོན་འཛིན་ན་གཉིས་པོ་ནི། །
ཕན་ཚུན་བརྟེན་པ་ཡིན་པས་གཅིག །
འཛིན་པ་མེད་ན་གཉིས་མི་འཛིན། །

[Block 812 [VERSE]]
དེ་ཡི་ཕྱིར་ན་བརྡར་གདགས་པ། །
མི་སྲེད་དོ་ཞེས་ཁ་ཅིག་སྨྲ། །

[Block 813]
ཁ་ཅིག་ན་རེ་གལ་ཏེ་ཤིང་ནི་ཤིང་མ་ཡིན་པ་དག་ལས་ཐ་དད་པ་ཡིན་ན། དེ་ནི་ཤིང་མ་ཡིན་པ་འཛིན་པ་མེད་པར་དེ་ལྟར་གཟུང་བར་མི་ནུས་པའི་ཕྱིར་དང་། ཤིང་མ་ཤེས་པ་ཅན་གྱིས་དེ་རྣམ་པར་གཅོད་པའི་ངོ་བོ་ཤིང་མ་ཡིན་པ་ཡང་ཡོངས་སུ་མི་ཤེས་བའི་ཕྱིར། བློ་ལ་མི་གནས་པའི་དོན་ལ་བརྡར་གདགས་པར་མི་ནུས་སོ་ཞེས་འཛིན་ཏོ། །

[Block 814 [VERSE]]
དེ་དག་གི་ནི་བརྡར་འདོགས་ལ། །
ཤིང་མིན་རྣམ་བར་གཅོད་དམ་ཅི། །

[Block 815]
གང་དག་དེ་ལྟར་སྤྱོད༌[^667]དངོས་པོ་ཅིག༌[^668]ཁས་བླངས་ནས་གཞན་རྣམ་པར་གཅོད་པས་བརྡར་འདོགས་པ་ལ་ཕན་ཚུན་བརྟེན་པ་ཡིན་པར་རྒོལ་བ་དེ་དག་གི་དེ་ལ་ཡང་བརྡར་བྱེད་པ་ན། ཤིང་མ་ཡིན་པ་རྣམ༌[^669]གཅོད་དམ། །འོན་ཏེ་མ་ཡིན་ཏེ།

[Block 816 [VERSE]]
[^670]གལ་ཏེ་རྣམ་གཅོད་ཤིང་གི་དོན། །
འཛིན་པ་མེད་ན་ཇི་ལྟར་ཤེས། །

[Block 817]
དེའི་ཚེ་རྟོགས་པ་པོས་ཤིང་ཡང་མི་ཤེས་ཤིང་མ་ཡིན་པ་ཡང་མི་ཤེས་ཏེ་དེ་ཤེས་པར་བྱ་བ་ཁོ་ནའི་ཕྱིར། དེ་དོན་དུ་གཉེར་བ་ཞིག་ཏུ་ཉེ་བར་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 818]
དེ་མི་ཤེས་པ་དེས་ཇི་ལྟར་བརྡ་ལ་ཤིང་མ་ཡིན་པ་རྣམ་པར་གཅད་པ༌[^671]རྟོགས་པར་འགྱུར།

[Block 819]
མི་རྟོགས་ན་ཡང་དེ་ལས་གཞན་པ་ཡོངས་སུ་མ་སྤངས་པ་ཅན་འགོད་པ་དང་ལྡན་པའི་སྒྲ་ལས།

[Block 820 [VERSE]]
བརྡ་ལས་དེ་དག་མི་སེལ་ན། །
ཐ་སྙད་འདོགས་པར་བྱེད་པ་རྣམས། །
དེ་ཡོངས་སྤངས་ནས་འཇུག་པར༌[^672]ནི། །
མི་འགྱུར་ཤིང་གི་ཁྱད་པར་བཞིན། །

[Block 821]
བརྡའི་ཚེ་གཞན་རྣམ་པར་མ་བཅད་པར༌[^673]བཀོད་པའི་སྒྲ་ལས་ཐ་སྙད་ཀྱི་ཚེ་ཤིང་མ་ཡིན་པ་ཡོངས་སུ་སྤངས་ནས་འཇུག་པར་རིགས་པ་མ་ཡིན་ཏེ། ཤིང་ཤ་པ་ལ་སོགས་པ་ཁྱད་པར་བཞིན་ནོ། །

[Block 822]
འོན་ཏེ། གལ་ཏེ་གཞན་བཀག་མི་བསྒྲུབ༌[^674]པར། །མདུན་ནས་གཅིག་ཅིག་རབ་བསྟན་ནས། འདི་ཤིང་ཡིན་ཞེས་བརྡར་བྱེད་པ།[^675] །

[Block 823 [VERSE]]
ཐ་སྙད་འདོགས་པའི་ཚེ་ན་ཡང་། །
དེ་རྟོགས་འགྱུར་ཏེ༌[^676]དེ་ཡི་ཕྱིར། །
ཉེས་པ་འདི་ནི་མེད་སྙམ་ན། །

[Block 824]
སྤྱི་དངོས་པོར་སྨྲ་བ་ནི་འགའ་ཞིག་རྣམ་པར་བཅད་པས་ཅུང་ཟད་ཅིག་བརྗོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 825]
འོ་ན་ཅི་ཞེ་ན། མདུན་ན་འདུག་པའི་དངོས་པོ་གཅིག་ཅིག༌[^677]ཡང་དག་པར་བསྟན་ནས་འདི་ནི་ཤིང་ཡིན་ནོ་ཞེས་བརྡར་བྱེད་ལ། འདིས་བརྡའི་དུས་ན་དེ་ལྟར་མཐོང་བའི་དོན་ཁོ་ནའམ། དེ་དང་འབྲེལ་པ་ཅན་ནི་ཐ་སྙད་ཀྱི་ཚེ་ཡང་རྟོགས་པར་འགྱུར་བས་ཐལ་བར་འགྱུར་བ་མཚུངས་པ་མ་ཡིན་ནོ་ཞེ་ན། མི་མཚུངས་པ་མ་ཡིན་ཏེ། འདི་ལྟར་དེ་ལ་ཡང་།

[Block 826 [VERSE]]
འདི་ཡང་ཤིང་འདི་ཁོ་ན་ཞེས། །
བྱ་བར་ཐལ་བར་ལྡོག་པ་མེད། །

[Block 827]
གཅིག་རབ་ཏུ་བསྟན་ནས་འདི་ནི་ཤིང་ཡིན་ནོ་ཞེས་སྨྲ་བ་ཡང་འདི་ཡང་ཡིན་ནོ་ཞེའམ། འདི་ཁོ་ན་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚུལ་གཉིས་ལས་ནི་མི་གདའ༌[^678]ལ། དེ་དག་ལ་ཡང་ཉེས་པ་དེ་ཉིད་ཡོད་དོ། །

[Block 828]
མཐོང་བ་ལས་བཟློག་པ་ནི་ཉེས་པར༌[^679]སླ་བའི་ཕྱིར་ཉེས་པ་མེད་དོ། །

[Block 829]
གཅིག་འགའ་ཞིག་མཐོང་ཞིང་གཞན་ལ་དེའི་རྣམ་པས་དབེན་པའི་བློ་ཉམས་སུ་མྱོང་བ་ལ་ནི་ཇི་ལྟར་ཉམས་སུ་མྱོང་བ་བཞིན་དེ་ལས་གཞན་ནོ་སྙམ་པ་ཆོས་མི་མཐུན་པ་ངེས་པ་དེ་ལས་འབྱེད་པ་སྐྱེའོ། །

[Block 830]
དེས་ནི་དེ་ཁོ་ན་ཤིང་ཡིན་ནོ་ཞེས་རབ་ཏུ་བསྟན་ནས་བྱེ་བྲག་ཏུ༌[^680]ཤེས་པར་བྱ་སྟེ། གང་ཁོ་ན་ལ་དེ་མི་སྣང་བ་དེ་ཁོ་ན་ཤིང་མ་ཡིན་པར་རང་ཉིད་ཀྱིས་རྟོགས་པར་འགྱུར་རོ། །

[Block 831]
རྣམ་པར་གཅོད་པ་སྨྲ་བ་ལ་ནི་འདི་མི་སྲིད་དེ། གཅིག་ན་མཐོང་བའི་ངོ་བོ་ནི་གང་ལ་ཡང་རྗེས་སུ་འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 832]
མཐོང་བར་རྟོགས་ན་ནི་གསལ་བ༌[^681]གཞན་པ༌[^682]ཡང་དེ་ལྟར་རྟོགས་པར་མི་འགྱུར་རོ་ཞེ་ན། དེ་ལྟར༌[^683]ན་འོ་ན་ནི་འདི་ནི་དེ་ལ་ཡང་མཚུངས་ཏེ། འདི་ལྟར།

[Block 833 [VERSE]]
གཅིག་རྟོགས་ཤེས༌[^684]བྱའི་ཤེས་པ་ནི། །
གཅིག་ལ་གནས་པའི་རྟོགས་པས་སོ། །
དེ་དང་དེ་མིན་རྒྱུ་དོན་རྣམས། །
བདག་ཉིད་རྣམ་པར་འབྱེད་པར་བྱེད། །

[Block 834]
འདི་ནི་གོང་དུ་ཇི་ལྟར་དངོས་པོ་འདི་དག་རང་བཞིན་གྱིས༌[^685]ཐ་དད་ཀྱང་ཁ་ཅིག་ཤེས་པ་ལ་སོགས་པའི་འབྲས་བུ་གཅིག་བྱེད་ཀྱི་གཞན་དག་ནི་མ་ཡིན་པ༌[^686]ལྟར་བཤད་ཟིན་ཏེ། འདིས་དེ་རྣམས་བདག་ཉིད་ཀྱིས་རྣམ་པར་ཕྱེ་ནས། དེའི་རྒྱུ་དང་དེའི་རྒྱུ་མ་ཡིན་པ་དག་རྟོགས་པར་འགྱུར་རོ། །

[Block 835]
དེའི།

[Block 836 [VERSE]]
བློ་དེ་ལ་ནི་ཡོད་པའི་དངོས། །
བློའི་རྒྱུ་ཉིད་དུ་སྣང་བ་དང་། །
རྒྱུ་མིན་ངོ་བོ་བྲལ་བ་དང་། །
ངོ་བོ་གཅིག་འདྲར་བདག་ཉིད་ཀྱིས། །

[Block 837 [VERSE]]
ཐ་དད་པར༌[^687]ནི་ཤེས་འགྱུར་བར། །
ཐ་དད་པ་ཡི༌[^688]སྐད་སྦྱོར་ཏེ། །
དེ་ལས་དེ་རྟོགས་འགྱུར་བའི་བློ། །
འཁྲུལ་པས་དངོས་པོ་གཅིག་ལྟར་རྟོགས། །

[Block 838]
དེ་རྣམས་ནི་རང་བཞིན་ཁོ་ནས་རྐྱེན་གྱི༌[^689]དབང་གི༌[^690]རྣམ་པར་རྟོག་པ་དེ་ལྟ་བུའི་རྒྱུ་རྣམས་ཀྱི་རྗེས་སུ་འགྲོ་བའི་ཕྱིར་ཏེ། དེ་མཐོང་བའི་བློ་ལ་ཡོད་པར་ཤེས་པ་དེའི་རྒྱུ་ཉིད་དང་། དེ་ལས་གཞན་པ་ལས་ལྡོག་པས། །དེ་ལྟ་བུ་མ་ཡིན་ན་ཡང་དེ་ལྟ་བུར་ལྷག་པར་ཞེན་པ།[^691] ཕྱི་དང་ནང་གི་སྙམ་ནས༌[^692]ཁྱད་པར་རྣམ་པར་མ་ཕྱེ་བ་ཅན༌[^693]རྣམས་རྣམ་པར་རྟོག་པ་ལ་རྣམ་པར་གནས་པས་རྟོག་པའི་རྗེས་སུ་འབྲངས་ཏེ། འདི་དག་ནི་ཤིང་ཡིན་ནོ་ཞེས་རང་དང་གཞན་གྱི་རྣམ་པར་རྟོག་པ་ལ་གཅིག་ཏུ་སྣང་བ་ཀུན་དུ་བསྟན་ནས་རྣམ་པར་ཤེས་པ་དེའི་རྒྱུ་ཡིན་པར་ཐ་དད་པར་ཤེས་པར་འགྱུར་སྙམ་ནས་དེའི་རྒྱུ་མ་ཡིན་པ་དག་ལས་ཐ་དད་པ་ལ༌[^694]དེ་སྐད་སྦྱོར་ཏེ། དེ་ལས་དེ་རྟོགས་པའི་བློ་རྣམ་པར་རྟོག་པ་ཅན་ནི་འཁྲུལ་པའི་དབང་ཁོ་ནས་དངོས་པོ་གཅིག་ཅིག་འཛིན་པ་ལྟ་བུར་སྣང་ངོ་། །དེ་ལ་ཐ་དད་པ་མཐོང་བ༌[^695]ཡང་གང་ཞིག་མཐོང་བ་དང་མ་མཐོང་བ་དག་གི༌[^696]ཤིང་དང་ཤིང་མ་ཡིན་པ་འདི་རྣམ་པར་འབྱེད་པར་བྱེད་པ་དངོས་པོ་ལྟར་རུང་བ་ཅིག་ནི་མེད་དེ། དེ་ནི་ཡལ་ག་ལ་སོགས་པ་སྣང་བ་ལས༌[^697]ཐ་དད་པར་ཁར་བ་ཐོགས་པ་ལ་ཁར་བ་བཞིན་དུ་མི་འཛིན་པའི་ཕྱིར་དང་། གཞན་ལས་ཐ་དད་པར་མ་བཟུང་བར་མི་མངོན་པའི་ཕྱིར་རོ། །

[Block 839]
རྣམ་པ་གཅིག་ལ་མཐོང་བ་ཡང་གཞན་ལ་བལྟ་བར༌[^698]མི་ནུས་པའི་ཕྱིར། དེ་དང་དེ་མ་ཡིན་པ་དག་ཤིང་དང་ཤིང་མ་ཡིན་པ་ཉིད་ཡིན་ན། གསལ་བ་གཅིག་ཁོ་ན་ཤིང་ཡིན་པར་འགྱུར་རོ། །

[Block 840]
བུམ་པ་ལ་སོགས་པའི་སྒྲ་ལ་ནི་དོན་གཞན། རྣམ་པར་གཅོད་པ་ཡོད་གྲང་ན། །ཞེས་བྱ་བ༌[^699]ལ་སོགས་པའི་ཚིག་ལ་གོ་ཇི་ལྟར་ཡོད། གང་ལས་ཐ་དད་པར་འགྱུར་བ་ཞེས་བྱ་བ༌[^700]མ་ཡིན་པ་ནི་ཅུང་ཟད་ཀྱང་མེད་དེ། དེ་ལས་ཐ་དད་པ་ཡུལ་དུ་བྱེད་པ་ཉིད་ཀྱིས༌[^701]དེ་ཤེས་བྱ་ཡིན་ནོ༌[^702]ཞེ་ན། དེ་ནི་ཉེས་པ༌[^703]མེད་དེ། འདི་ལྟར།

[Block 841 [VERSE]]
བློ་དོན་འགའ་ལས་རྣམ་བཟློག་ནས། །
དོན་འགའ་ཞིག་ལ་འཇུག་བྱའི་ཕྱིར། །
སྒྲ་ནི་རབ་ཏུ་སྦྱོར་བྱེད་དེ། །
དེའི་དོན་ངེས་པར་བཟུང་ཕྱིར་རོ། །

[Block 842 [VERSE]]
གཞན་དུ་སྦྱོར་བ་དོན་མེད་འགྱུར། །
དེས་ན་ཤེས་བྱ་ལ་སོགས་ཚིག །
ཐ་སྙད་དུ་ནི་རྟོགས་རྣམས་ལའང་། །
རྣམ་པར་གཅོད་པ་འགའ་ཞིག་ཡོད། །

[Block 843]
སྒྲ༌[^704]རབ་ཏུ་སྦྱོར་བར་བྱེད་པ་ཐམས་ཅད་ནི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་དག་ལས་མི་འདའ་སྟེ། དེ་ནི་འཇུག་པ་དང་ལྡོག་པའི་དོན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 844]
གལ་ཏེ་འདིས་འགའི་བློ་གང་ལས་ཀྱང་ལྡོག་པར་མི་བྱེད་པའམ། འཇུག་པར་མི་བྱེད་ན་ཇི་ལྟ་བ་བཞིན་དུ་གནང་བའི་ཕྱིར། ཐ་སྙད་ཐམས་ཅད་ལ་འགའ་ཡང་ཐ་སྙད་གདགས་པར་མི་འགྱུར་ཏེ། ཐ་སྙད་ནི་ངེས་པར་གཟུང་བ་མེད་ན་མེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 845]
དཔེར་ན་བུམ་པས་ཆུ་འོན་ཅིག་ཅེས་བྱ་བ་ལྟ་བུ་ལ། གལ་ཏེ་བུམ་པ་དང་སྙིམ་པས་ཆུ་ཅི་འདྲ་ཡང་རུང་བ་ཞིག་བླང་བར་འདོད་པར་གྱུར་ན་ནི། ཆུ་འོན་ཅིག་ཅེས་བྱ་བ་ཁོ་ན་བརྗོད་པར་བྱ་བར་འགྱུར་གྱི། བུམ་པས་ཞེས་བྱ་བ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
