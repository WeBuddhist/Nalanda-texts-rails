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
དེ་ལས་ལམ་བསྒོམས༌[^602]པ་འཇིག་རྟེན་པ་ཐམས་ཅད་ཀྱིས་མ་བཙལ༌[^603]བར་ཡང་མྱ་ངན་ལས་འདའ་བར་འགྱུར་རོ། །

[Block 807]
དེའི་ཕྱིར་ངེས་པར་སྡུག་བསྔལ་ལ་ལྟོས་པ་དང་བཅས་པའི་རང་བཞིན་གྱིས་དེ་འབྱུང་བར་འགྱུར་ལ། དེ་ལ་ཡང་སྡུག་བསྔལ་མི་སྲིད་པའོ། །

[Block 808]
དེས་ན།

[Block 809 [VERSE]]
དངོས་པོ་མེད་ཕྱིར་འདི་མེད་དེ། །
སྡུག་བསྔལ་མེད་པས་དེ་མེད་དོ། །

[Block 810]
ཞེས་པའི་དོན་ཏོ།[^604] །

[Block 811]
ཡང་གཞན་ཞིག་གིས་སྨྲས་པ། གལ་ཏེ་སྡུག་བསྔལ་འགགས་པ་སྟེ། སྡུག་བསྔལ་མེད་པའི་རང་བཞིན་དངོས་པོར་གྱུར་པ་མྱ་ངན་ལས་འདས་པར་འགྱུར་ན་སྐྱོན་འདིར་འགྱུར་ན། རྣམ་པ་དེ་ལྟ་བུ་ནི་མེད་དོ། །

[Block 812]
འོན་ཀྱང་འདི༌[^605]དེ་ནི་སྡུག་བསྔལ་ལས་ལོག་པ་ཙམ་མོ་ཞེ་ན། སྨྲས་པ། འདི་ལྟར་བརྟགས་པས་ཀྱང་མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་མི་འགྱུར་ཏེ། སྡུག་བསྔལ་གྱི་དངོས་པོར་ཡོད་ན་སྡུག་བསྔལ་དང་ལྡན་པར་འགྱུར་ལ། སྡུག་བསྔལ༌[^606]ཡང་མི་སྲིད་ན་དེ༌[^607]མེད་པ་ག་ལ་ཞིག་ཅེས་བྱའོ། །

[Block 813]
དངོས་པོ་མེད་པའི་རང་བཞིན་ཡང་མྱ་ངན་ལས་འདས་པའོ་ཞེ་ན། དེས་ན་དངོས་པོ་མེད་པས་ནི་དངོས་པོ་མེད་པའི་ཕྱིར་ལ། དེ་ཡང་མེད་དེ། དངོས་པོ༌[^608]མེད་པར་གྱུར་པས་མེད་པའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་མེད་དོ་ཞེས་པའི་དོན་ཏོ། །

[Block 814]
ཡང་ན་འདིའི་དོན་གཞན་ཏེ། གལ་ཏེ་འགོག་པ་ཞེས་བྱ་བ་དངོས་པོའི་རང་གི་ངོ་བོ་གྲུབ་པར་གྱུར་ན། དེ་སྡུག་བསྔལ་ལ་མི་ལྟོས་པས་ཀྱང་འབྱུང་སྟེ། རང་གི་མཚན་ཉིད་ཀྱིས་གྲུབ་པའི་ཕྱིར་ལ། འབྱུང་བ་ཡང་མ་ཡིན་ཏེ། དེས་ན་འགོག་པའི་རང་གི་ངོ་བོ་གྲུབ་པ་མེད་དོ། །

[Block 815]
ཡང་ན་གལ་ཏེ་འདོད་ན་ཡང་ངེས་པར་དེ་ནི་དངོས་པོའི་རང་བཞིན་གྱིས་སམ། དངོས་པོ་མེད་པའི་རང་བཞིན་གྱིས་འབྱུང་བར་འགྱུར། གལ་ཏེ་དངོས་པོའི་རང་བཞིན་དུ་འདོད་ན།

[Block 816 [VERSE]]
དེ་ནི་དངོས་པོ་བཀག་པའི་ཕྱིར། །
དངོས་པོ་མེད་ཕྱིར་དེ་ཡང་མེད། །

[Block 817]
ཡང་ན་དངོས་པོ་མེད་པའི་རང་བཞིན་ཡིན་ན། འདི་ལྟར་དངོས་པོ༌[^609]མེད་ཀྱང་བཀག་པའི་ཕྱིར་ཏེ། འགག་པ༌[^610]ཉིད་དངོས་པོ་མེད་པའི་ཕྱིར། [^611]དངོས་པོ་མེད་པས་ཡོད་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་གསུངས་པ། དངོས་པོ་མེད་ཕྱིར་དེ་ཡང་མེད། །ཅེས་སོ། །

[Block 818]
འདིར་སྨྲས་པ། མྱ་ངན་ལས་འདས་པ་ཡོད་པ་ཉིད་དེ། དེའི་ཚེ༌[^612]མཚན་ཉིད་ཡོད་པའི་ཕྱིར་རོ། །

[Block 819]
ཡོད་བཞིན་པ་མ་ཡིན་པའི་མོ་གཤམ་གྱི་བུ་ལ་མཚན་ཉིད་ཡོད་པ་མ་ཡིན་ལ། མྱ་ངན་ལས་འདས་པ་ལ་མཚན་ཉིད་ཡོད་དེ་སོ་སོར་བརྟགས་པའི་འགོག་པ་གང་བྲལ་བའོ་ཞེས་པའི་ཚིག་ལས་སོ། །

[Block 820]
སྨྲས་པ། མྱ་ངན་ལས་འདས་པ་དེའི་མཚན་ཉིད་ཡོད་ན་ཡོད་པར་འགྱུར་ན། ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 821 [HEADING]]
### ཚིགས་བཅད་ཉེར་བདུན་པ། ^1-27-0

[Block 822 [VERSE]]
མཚན་གཞི་ལས་གཞན་མཚན་ཉིད་ལས། །
མཚན་གཞི་གྲུབ་པས་རང་མ་གྲུབ། །
ཕན་ཚུན་ལས་ཀྱང་མ་གྲུབ་ཅིང་། །
མ་གྲུབ་མ་གྲུབ་སྒྲུབ་བྱེད་མིན། །

[Block 823]
འདིར་གལ་ཏེ་མཚན་ཉིད་ཅེས་བྱ་བའི་ངོ་བོ་ཅུང་ཟད་གྲུབ་པར་གྱུར་ན། དེ་མཚན་གཞི་ལ་མི་ལྟོས་པར་འགྱུར་ལ། མཚན་གཞི་ལ་མ་ལྟོས་པའི་མཚན་ཉིད་རྒྱུ་མེད་པ་ཐོབ་པར་འགྱུར་ལ། རྒྱུ་མེད་པར་ཡང་མི་རིགས་སོ་ཞེས་བྱ་སྟེ། དེས་ན་ངེས་པར་མཚན་གཞི་ལས་མཚན་ཉིད་གྲུབ་པས། མཚན་གཞིའི་རྒྱུ་ཅན་གྱི་མཚན་ཉིད་མ་གྲུབ་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 824]
ཡང་ན་འདི་སྙམ་དུ་སེམས་ཏེ། མཚན་གཞི་ལ་ལྟོས་ནས་མཚན་ཉིད་གྲུབ་པར་ཡོད་དོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་མཚན་གཞི་མཚན་ཉིད་ལ་མ༌[^613]ལྟོས་པར་ཡོད་ན། དེ་ལ་ལྟོས་ནས་མཚན་ཉིད་ཡོད་ལ། ལྟོས་པ་མེད་པའི་མཚན་གཞི་མི་སྲིད་ལ། མཚན་ཉིད་དང་བྲལ་བའི་མཚན་གཞི་རྒྱུ་མེད་པར་ཐལ་བས། དེས་ན་མཚན་གཞི་ཡང་དེའི་མཚན་ཉིད་ལས་གྲུབ་པས། རང་ལས་མ་གྲུབ་སྟེ། མཚན་ཉིད་དང་མཚན་གཞི་ངོ་བོ་ཉིད་ཀྱིས་མ་གྲུབ་བོ་ཞེས་པའི་དོན་ཏོ། །

[Block 825]
ཡང་ན་འདི་སྙམ་དུ་སེམས་ཏེ། གལ་ཏེ་ཡང་མཚན་གཞི་དང་མཚན་ཉིད་དག་རང་ལས་མ་གྲུབ་ཀྱང་། དེ་ལྟ་ན་ཡང་ཕན་ཚུན་ལྟོས་ནས་གྲུབ་པས་ཡོད་དོ་ཞེ་ན། སྨྲས་པ། ཕན་ཚུན་ལས་ཀྱང་མ་གྲུབ་ཅིང་། ཕན་ཚུན་ལྟོས་པས༌[^614]གྲུབ་པ་མེད་དོ་ཞེས་པའི་དོན་ཏོ། །

[Block 826]
ཡང་ཅིའི་ཕྱིར་ཕན་ཚུན་ལྟོས་པས་གྲུབ་པ་མེད་ཅེ་ན། གསུངས་པ། མ་གྲུབ་མ་གྲུབ་སྒྲུབ་བྱེད་མིན། །ཞེས་པའོ། །

[Block 827]
འདིར་མཚན༌[^615]གཞི་ལ་བརྟེན་པའི་ཕྱིར་ཉིད༌[^616]མཚན་གཞི་ལ༌[^617]རྟེན་དུ་གྲུབ་པར་འདོད་ན།[^618] མཚན་གཞི་ལས་གཞན་དུ་མཚན་གཞིའི་མཚན་ཉིད་མི་འཐད་པས། མཚན་ཉིད་ཀྱིས་བརྟེན་པས་མཚན་གཞི་གྲུབ་བོ་ཞེས་བྱ་ལ། དེ་ལྟར་ཕན་ཚུན་ལྟོས་པས་མཚན་གཞི་དང་མཚན་ཉིད་གྲུབ་པ་རྣམ་པར་གཞག་པར་གྱུར་པ་འདི་དག་དཔྱད་པར་བྱ་སྟེ། གལ་ཏེ་མཚན་གཞི་ལ་ལྟོས་ནས་མཚན་ཉིད་རྣམ་པར་འཇོག་པས་དེ་ཉིད་ཀྱིས་ན་རེ་ཞིག་མཚན་གཞི་མཚན་ཉིད་ལ་མ་ལྟོས་པར་ངོ་བོ་ཉིད་ཀྱིས་མེད་ལ། དེ་ནི་རང་ཉིད་མ་གྲུབ་པས་མེད་པས་ཇི་ལྟར་གཞན་མཚན་ཉིད་འགྲུབ་པར་བྱེད། དེ་བཞིན་དུ་མཚན་གཞི་ལ་ཡང་སྦྱར་རོ།[^619] །དེ་ནི་འདི་ལྟར་མཚན་གཞིའམ་མཚན་ཉིད་དག་མ་གྲུབ་པ་མ་གྲུབ་པའི་མཚན་གཞིའམ་མཚན་ཉིད་གྲུབ་པར་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་སྟེ། དེས་ན་མཚན་གཞི་དང་མཚན་ཉིད་དག་མེད་དོ། །

[Block 828]
གང་གི་ཚེ་མཚན་གཞི་དང་མཚན་ཉིད་དག་མེད་པ་དེའི་ཚེ་མཚན་ཉིད་ཡོད་པའི་མྱ་ངན་ལས་འདས་པ་ག་ལ་འགྲུབ་ཅེས་བྱ་སྟེ། འདི་ནི་མི་རིགས་སོ། །

[Block 829]
མཚན་གཞི་དང་མཚན་ཉིད་ལ་དཔྱད་པའི་རིམ་པས་ཕན་ཚུན་ལྟོས་པས་གྲུབ་པའི་དངོས་པོ་ལྷག་མ་རྣམས་ཀྱང་མ་གྲུབ་པར་བདེ་བླག་ཏུ་ཁོང་དུ་ཆུད་པར་གཟིགས་ནས། དེ་ལེགས་པར་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 830 [HEADING]]
### ཚིགས་བཅད་ཉེར་བརྒྱད་པ། ^1-28-0

[Block 831 [VERSE]]
འདིས་ནི་རྒྱུ་དང་འབྲས་བུ་དང་། །
ཚོར་དང་ཚོར་བ་པོ་སོགས་དང་། །
བལྟ་བྱ་ལྟ་བ་པོ་ལ་སོགས། །
དེས་གང་ཅུང་ཟད་མ་ལུས་བཤད། །

[Block 832]
མཚན་གཞི་དང་མཚན་ཉིད་དག་མ་གྲུབ་པའི་རིམ་པ་འདིས། རྒྱུ་དང་འབྲས་བུ་ལ་སོགས་པ་ཡང་མ་གྲུབ་པར་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 833]
བྱས་པ་ནི་འབྲས་བུ།[^620] བྱེད་པ་ནི་རྒྱུའོ། །

[Block 834]
མྱོང་བར་གྱུར་པས་ཚོར་བ་སྟེ། ལས་ལ་ལུགས་བྱས་ནས༌[^621]ཚོར་བ་ལ་ཚོར་བར་གསུངས་སོ། །

[Block 835]
ཚོར་བ་པོ་ནི་ཉམས་སུ་མྱོང་བ་ཡང་ཚོར་བ་དང་ཚོར་བ་པོ་སྟེ། ཚོར་བ་དང་ཚོར་བ༌[^622]པོའོ། །

[Block 836]
དེ༌[^623]ཚོར་བ་དང་ཚོར་བ་པོ་དག་ལྷན་ཅིག་འཇུག་པས་ཚོར་བ༌[^624]དང་ཚོར་བ་པོ་ཞེས་བྱའོ། །

[Block 837]
སོགས་པའི་སྒྲས་འདུ་ཤེས་དང་འདུ་ཤེས་པར་བྱ་བ་ལ་སོགས་པ་གཟུང་ངོ་། །བལྟ་བྱ་དང་ལྟ་བ་པོ་ལ་སོགས་པ་གང་ཅུང་ཟད་ཀྱང་ཞེས་པ་ལ་སོགས་པའི་སྒྲས་ཐོས་པ་དང་ཐོས་པ་པོ་ལ་སོགས་པ་ལྔ་པོ་རྣམས་ཀྱི་གཉིས་གཉིས་པ་གཟུང་ལ། གང་ཅུང་ཟད་ཅེས་པ་འདིས་ཕན་ཚུན་ལྟོས་ནས་གྲུབ་པའི་གཉིས་གཉིས་པའི་དངོས་པོ་རྣམས་གཟུང་ངོ་།[^625] །དངོས་པོ་འདི་དག་ཐམས་ཅད་ཀྱང་མཚན་གཞི་དང་མཚན་ཉིད་དག་མ་གྲུབ་པའི་རིམ་པས་མ་གྲུབ་པར་སྦྱར་རོ། །

[Block 838]
རབ་ཏུ་བྱེད་པ་འདིར་ཡང་རེ་རེའི་དངོས་པོའི་གྲངས་འཇུག་པ་ལ་དཔྱད་པའི་རིམ་པའི་སྐབས་ཡིན་པའི་ཕྱིར། རེ་ཞིག་ཐོག་མར་དངོས་པོ་གཅིག་རྣམ་པར་དཔྱད་དེ། འདི་ལྟར་རང་བཞིན་ནོ། །

[Block 839]
དེའི་རྗེས་ལ་རྒྱུ་གཅིག་པུ་ཉིད་དེ། འབྲས་བུ་ཡོད་ན་འབྲས་ལྡན་ལ། ། ཞེས་པ་ལ་སོགས་པའོ། །

[Block 840]
དེ་ཡང་མ་རིག་པ་ལ་སོགས་པའི་རིམ་པས་རྣམ་པ་མང་པོ་རྣམ་པར་དཔྱད་ལ། དེའི་རྗེས་ལ། མ་རིག་འདུ་བྱེད་མེད་མི་འབྱུང་། །ཞེས་པ་དེ་ནས་བརྩམས་ནས་འདིའི་བར་དུ་གཉིས་གཉིས་པའི་དངོས་པོ་ཕན་ཚུན་ལྟོས་པས་གནས་པ་རྣམས་དཔྱད་ལ། འདི་ལས་གཞན་པས། ལྟོས་པ་དང་བཅས་པའི་གསུམ་གྱི་གྲངས་ཀྱིས་ཡོངས་སུ་བཅད་པའི་དངོས་པོ་རྣམས་རྣམ་པར་དཔྱད་པ་བརྩམ་པར་བྱའོ། །

[Block 841]
གང་འདི་སྐད་དུ།

[Block 842 [VERSE]]
དངོས་པོ་ཡོད་ན་རྟག་པ་ཉིད། །
མེད་ན་ངེས་པར་ཆད་པ་ཉིད། །
དངོས་པོར་གྱུར་ན་དེ་གཉིས་ལ། །
དེ་ཕྱིར་དངོས་པོ་ཁས་མི་བླང་། །

[Block 843]
ཞེས་པ་དེ་ནི་མི་འཐད་དེ། །གལ་ཏེ་དངོས་པོ་ཁས་མི་ལེན་ན་དེའི་ཚེ་དུས་གསུམ་མེད་ལ། དུས་གསུམ་ཡོད་པས་དེའི་ཕྱིར་དངོས་པོ་ཡོད་དེ། དུས་གསུམ་གྱི་རྒྱུ་མཚན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 844]
འདིར་སྐྱེས་ལ་མ་འགགས་པའི་དངོས་པོ་ངོ་བོ་ཉིད་ཀྱིས་གནས་བཞིན་པའི་ཕྱིར་དང་། ཡོད་བཞིན་པའི་ཕྱིར་ད་ལྟར་བའི་སྒྲས་བརྗོད་པར་བྱ་བར་འགྱུར་རོ། །

[Block 845]
ད་ལྟར་བའི་གནས་སྐབས་མ་ཐོབ་པ་ལ་མ་འོངས་པ་ཞེས་བརྗོད་ལ། ད་ལྟར་བའི་གནས་སྐབས་ལས་འདས་པ་ཉིད་ལ་འདས་པ་ཞེས་བརྗོད་དོ། །
--- END BLOCKS ---
