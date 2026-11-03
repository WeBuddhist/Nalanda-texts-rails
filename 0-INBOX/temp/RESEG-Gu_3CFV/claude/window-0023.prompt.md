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
ཨ་མྲ་ཞིམ་པོ་དག་ལོགས་ཤིག་ཏུ་བསལ༌[^484]ཏེ་བྲིམ་པར་བྱའོ་ཞེས་བྱ་བ་ལ་མདོ་སྔ་མ་འདི་སྙོམས་པར་བསལ་བའི་དོན་དུའོ། །

[Block 807]
འདི་རྣམས་ནི་རྒན་པ་ཉིད་མ་ཡིན་ཏེ། དེ་བས་ན་སྤྲོས་པ་འདི་ནི་རྒན་པ་དང་གཞོན་པ་དང་བར་མ་དག་ལ་ཤེས་པར་མི་བྱའོ། །

[Block 808]
འདྲིམ་པར་བྱེད་པ་ཡི༌[^485]ནི་མཁན་པོའམ་སློབ་དཔོན་གྱིས་མནོད་པར་བྱའོ། །

[Block 809]
མི་འཐོབ་པ་འཐོབ་ན་དྲུང་དུ་འདུག་པས་སོ་ཞེས་བྱ་བ་གལ་ཏེ་མཁན་པོའམ་སློབ་དཔོན་གྱིས་འདྲིམ་པར་བྱེད་པས་མི་ཐོབ་པ་ཐོབ་པ༌[^486]མི་རིགས་པ་ནི་གནས་གཞན་མ་ཡིན་པས་འདི་ལ་བྱིན་ལེན་དུ་བྱ་བའོ། །

[Block 810]
འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། འདྲིམ་པར་བྱེད་པའི་སྐལ་བ་ནི་མཁན་པོ་དང་སློབ་དཔོན་དག་གིས་མནོད་པར་བྱའོ། །

[Block 811]
དེ་དག་གིས་བཟང་པོ་དག་ཐོབ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་དག་གི་དྲུང་དུ་འདུག་པ་དག་གིས་མནོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 812]
དུ་མ་ཉིད་ཡིན་ན་སྟན་ལས་མ་འཕགས་པས་ཇི་ཙམ་ལེན་ནུས་པའོ་ཞེས་བྱ་བ་ནི། གང་གི་དོན་དུ་དེ་མ་ཐག་པའི་གནས་ལ་གཟུང་བར༌[^487]བྱ་བ་ཉིད་ནི་དེ་དག་དུ་མ་ལ་སྟན་ལས་མ་འཕགས་པར་ཇི་ཙམ་ལེན་ནུས་པ་དེ་ཙམ་མནོད་པར་བྱ་ཞིང་དེ་མ་ཐག་པའི་གནས་དང་ལྡན་པས་གཟུང་བར༌[^488]བྱའོ། །

[Block 813]
འདྲིལ་བ་ལ་ནི་རང་གནས་ལས་མ་འཕགས་པས་ལེན་ནུས་པ་ཉིད་ཡིན་ན། བྱིན་ལེན་མ་ཞིག་གོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་བྱིན་ལེན་བྱས་པའི་ཟས་འདྲིལ་ཅིང་གནས་ནས་གུད་དུ་སོང་བ་གང་ཡིན་པ་དེ་ནི་སྟན་ལས་མ་འཕགས་པས་ལེན་ནུས་པ་ཉིད་ཡིན་ན་བྱིན་ལེན་མ་ཞིག་པ་ཡིན་ལ་གཞན་དུ་ན་ཞིག་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 814]
སྦྲང་བུ་དང་གྲོག་སྦུར་ལ་སོགས་པ་དག་གིས་རེག་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བྱིན་ལེན་མ་ཞིག་པའོ། །

[Block 815]
སོགས་པའི་སྒྲས་ནི་བྱིའུ་ཕྲུག་བྱུང་མ་ཐག་པའི་ཚད་པས་ཀྱང་ཆུང་བའི་སྐྱེ་བ་ཕྲ་མོ་དག་བསྡུའོ། །

[Block 816]
དགེ་སློང་གིས་མ་བཏང་བ་ལ་གཞན་གྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གིས་འཛིན་པ་མ་བཏང་བ་ལ་སྦྲང་བུ་དང་གྲོག་སྦུར་ལ་སོགས་པ་གཞན་གྱིས་རེག་པས་ཀྱང་བྱིན་ལེན་མ་ཞིག་པའོ། །

[Block 817]
འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་ཉིད་ཀྱིས་བྱིན་ལེན་བྱ་ཞིང་དེ་ལ་བགོ་བཤའ་བྱ་སྟེ་བཟའ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 818]
བྱི་བས་ནི་གཞིག་པར་བྱེད་དོ་ཞེས་བྱ་བ་ནི། བྱི་བས་རེག་པས་ནི་བྱིན་ལེན་ཞིག་པར་བྱེད་དོ། །

[Block 819]
འདིར་གཞུང་ནི་དེ་ལྟར་དེར་སྦྲང་བུ་དང་གྲོག་སྦུར་དང་བྱི་བའི་བར་དག་ལྷུང་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བྱི་མངས་ལ་སོགས་པའི་བྱི་བ་དག་གིས་རེག་པ་ནི་བྱིན་ལེན་བྱ་སྟེ་བཟའ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 820]
བྱིན་ལེན་བྱས་པའི་བྱིན་ལེན་སྟོབས་པ་ནི་མི་རིགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རེག་པར་མ་གྱུར་ཏམ་འོན་ཏེ་བྱིན་ལེན་བྱས་པ་མ་ཡིན་སྙམ་པའི་ཐེ་ཚོམ་བསལ་བའི་ཕྱིར་རོ། །

[Block 821]
བྱིན་ལེན་བྱས་པ་ལ་སླར་བྱིན་ལེན་བྱེད་པ་ནི་རིགས་པ་དང་མི་ལྡན་པ་མ་ཡིན་ནོ། །ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །གང་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བྱིན་ལེན་མ་བསྟབས་པ་ཉིད་ལའོ། །

[Block 822]
ཆུ་དང་སོ་ཤིང་མ་གཏོགས་པ་བཟའ་བར་བྱ་བའི་འོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆུ་དང་སོ་ཤིང་མ་གཏོགས་པའི་བཟའ་བར་བྱ་བ་ལའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 823]
འདིར་ཆུ་དང་སོ་ཤིང་ཞེས་བྱ་བ་སྨོས་པ་ནི༌[^489]དཔེ་ཙམ་དུ་ཟས༌[^490]དེ་ཁ་སྦྱང་བའི༌[^491]ཐོ་རངས་ཀྱི་ཆུ་དང་བའི་ལྕི་སྐམ་དང་ལྕི་བ་དག་ཀྱང་འདིས་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 824]
དེ་ཡང་ཁ་སྦྱང་བའི་ཟས་ཀྱི་ཕྱིར་སོ་ཤིང་ལ་འདི་ནི་ཉེས་པ་མེད་པ་ཉིད་ཡིན་གྱི་མགུལ་དུ་མིད་པའི་ཕྱིར་ནི་མ་ཡིན་ནོ། །

[Block 825]
དེར་བྱིན་ལེན་མ་བྱས་པ་ཉིད་མགུལ་དུ་མིད་པ་ལ་ནི་ལྟུང་བྱེད་ཁོ་ནར་འགྱུར་རོ། །

[Block 826]
མགུལ་ནས་ཁའི་ཆ་ཐ་དད་པར་གྱུར་པས་བཟའ་བ་གང་ཡིན་པའི༌[^492]དེ་ལ་ནི་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་བྱ་བ་ཡང་དེའི་ཕྱིར་ཤེས་པར་བྱའོ། །

[Block 827]
གཟུགས་དང་མི་ལྡན་པ་ལ་ཡང་བློས་བཟའ་བར་འགྱུར་བ་ཡིན་ཏེ། དེ་ལྟར་ཡང་རེག་པ་དང་ཡིད་ཀྱིས་ཀུན་དུ་སེམས་པ༌[^493]བཟའ་བ་ཉིད་ཀྱིས༌[^494]མངོན་པར་བརྗོད་པའོ། །

[Block 828]
བཟའ་བ་ཡང་གང་ཞིག་བློ་འདི་རྣམས་ཉེ་བར་འཚོ་བར་བྱེད་པ་དེ་ཞེས་བྱ་བ་ནུས་པར་བྱའོ།[^495] །དེ་བས་ན་ཁྱད་པར་བསྟན་པར་བྱ་བའི་ཕྱིར་ཁར་རོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 829]
ཇི་ཞིག་རྗེས་སུ་བསྒྲུབ་ན་འདིའི་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཟོས་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཅི་ཡུལ་ཐམས་ཅད་དུའམ་ཞེ་ན། དེའི་ཕྱིར་བྱང་གི་སྒྲ་མི་སྙན་མ་གཏོགས་པར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཞུ་བ་ལས་བྱང་གི་སྒྲ་མི་སྙན་གྱི་གླིང་ན་ཟས་མ་བྱིན་པར་ཁའི་སྒོ་ནས་ཟ་བར་བྱེད་དེ། གལ་ཏེ་བྱང་གི་སྒྲ་མི་སྙན་པའི་དུས་སུ་བྱིན་གྱིས་བརླབས༌[^496]ན་ནི་ལྟུང་བ་མེད་དོ། །

[Block 830]
ཇི་སྟེ་བྱིན་གྱིས་མི་རློབ་ན་ནི་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 831]
ནད་པས་བསྙེན་པར་རྫོགས་པ་མེད་ན་བསྙེན་པར་མ་རྫོགས་པ་ལ་ཟན་མནོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ནད་པའི་ཁར་ཟན་མནོད་པ་ལ་འདི་ཡིན་གྱི་རྗེས་སུ་གནང་བའི་དངོས་པོ་ལ་ནི་དེ་བསྙེན་པར་རྫོགས་པ་ལ་གནང་བ་མ་ཡིན་པས་བཏང་བ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་འདི་མི་བྱ་བ་ཉིད་དོ། །

[Block 832]
བསྙེན་པར་མ་རྫོགས་པས་བཟའ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། ནད་པ་ཁོ་ན་སྟེ་གཏོང་བར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་འདི་མི་བྱ་བ་ཤེས་པར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 833]
འདིར་གཞུང་ནི་བསྙེན་པར་མ་རྫོགས་པ་དང་ལྷན་ཅིག་ཉལ་བའི་ལྟུང་བྱེད་ཀྱི་ཆོ་ག་གཉིས་པོ་དག་གོ། །

[Block 834]
བྱིན་ལེན་མ་བྱས་པར་ཟ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 835]
འོ་མ་དང་ཞོ་དང་མར་དང་ཉ་ཤ་དང་ཤ་སྐམ་ལྟ་བུ་ནི་ཁ་ཟས་བསོད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྣམ་པ་དེ་ལྟ་བུ་དག་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 836]
དེ་ནི་བྱེད་པ་པོའོ་ཞེས་བྱ་བ་ལ་འདི་ནི་ཟས་བསོད་པ་སྟེ། དེ་ནི་ལྟུང་བ་འདིའི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 837]
སྦྱིན་པར་བྱེད་པ་ཉེ་དུ་མ་ཡིན་པ་ཁྱིམ་པ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། ཉེ་དུར་མ་གྱུར་པའི་ཁྱིམ་པ་ནི་ཉེ་དུ་མ་ཡིན་པའི་ཁྱིམ་པ་སྟེ་དེའི་དངོས་པོ་ནི་དེ་ཉིད་དོ། །

[Block 838]
འདིར་སྦྱིན་པ་པོའི་བྱེད་པ་པོ་གཞན་གྲོགས་སུ་གྱུར་པ་ནི་ཟས་བསོད་པ་འདི་ལའོ། །

[Block 839]
ཉེ་དུ་མ་ཡིན་པ་ཞེས་སྨོས་པ་ལ། གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་དགེ་སློང་གིས་བྲོ་མ་འཆལ༌[^497]བར་བདག་ཉིད་ཀྱིས་སླད་དུ་ཁྱིམ་དག་ནས༌[^498]ཟས་བསོད་པ་བླངས་ཏེ་འཆའ་འམ་འཆའ་བ་ལ་ལྟུང་བར་ཡང་མི་འགྱུར་བ་མཆིས་སམ་ཡོད་དེ་ཉེ་དུ་ལས་བླངས་ཏེ་ཟ་ན་ལྟུང་བ་མེད་དོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 840]
རབ་ཏུ་བྱུང་བ་གང་ལ་ཉེས་བྱས་བྱེད་པ་ཉིད་མ་ཡིན་པ་ཉིད་ལྟུང་བའི་རྟགས་འདི་ཡིན་ཞེས་བྱ་བ་འདིར་ཁྱིམ་པའི་ཚིག་གིས་འདི་འབྱུང་བར་རིག་པར་བྱའོ། །

[Block 841]
གང་གི་ཚེ་དེ་གཉིས་ལྟུང་བ་འདི་ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རང་གིས་བླངས་ཏེ་ཟོས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གིས་བླངས་ཏེ་ཟོས་ནའོ། །

[Block 842]
མི་ན་བས་བླངས་པ་དང་སློང་དུ༌[^499]བཅུག་པ་ཉིད་དེ་ལ༌[^500]ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བ་ནི༌[^501]མི་ན་བས་རང་གིས་བླངས་པ་ཙམ་ལ་ཡང་དེ་གཉིས་ཉེས་བྱས་ཁོ་ནའི་བྱེད་པ་པོ་ཡིན་ལ་མིན་བར་གཞན་སློང་དུ་བཅུག་པ་ཉིད་ཡིན༌[^502]ན་སློང་དུ་བཅུག་ཏེ་ཟོས་པ་དེ་ལ་ནི་དེ་གཉིས་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 843]
མི་ན་བར་སློང་དུ་བཅུག་པ་ལ་ནི་ཉེས་བྱས་ཕྲ་མོར་འགྱུར་རོ། །

[Block 844]
ཅི་མི་ན་བར༌[^503]ཐམས་ཅད་ལ་དེ་གཉིས་ཁ་ན་མ་ཐོ་བ་འདིའི་བྱེད་པ་པོ༌[^504]ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཅི་བདེར་བསྟབས་པ་མ་བྱས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་སློང་བར་བྱེད་པ་དེས་མ་བྱས་པ་དེས་ནི་ཅི་བདེར་བསྟབས་པ་མ་བྱས་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 845]
འདིར་གཞུང་ནི་དགེ་སློང་བསོད་སྙོམས་ལ་རྒྱུ་ཞིང་ཁྱིམ་དག་ཏུ་འགྲོ་བ་ན་བུད་མེད་ཀྱི་ཡུལ་ཟས་ཐོགས་ཏེ་ཕྱིར་བྱུང་བའི་ཚེ་དགེ་སློང་ཅང་མི་སྨྲ་བར་སྡོད་པ་ན་བུད་མེད་ཀྱི་ཡུལ་ན་རེ་འཕགས་པ་ཅི་བཞེད་ཅེས་འདྲི་ན་བསྟབས་པར་བརྗོད་པར་བྱ་སྟེ། ཅི་འདོད་པ་དེ་བླང་བར་བྱ་བ་ལ་ལྟུང་བ་མེད་དོ། །
--- END BLOCKS ---
