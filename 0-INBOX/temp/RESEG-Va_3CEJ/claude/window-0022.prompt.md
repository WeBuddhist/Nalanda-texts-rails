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
[Block 771]
གལ་ཏེ་མིག་ཡུལ་དང་མ་ཕྲད་པ་ཡིན་ན་ཅིའི་ཕྱིར་ཐག་རིང་བ་དང་བར་དུ་ཆོད་པ་མ་ཕྲད་པ་ཐམས་ཅད་མི་མཐོང་ཞེ་ན། རེ་ཞིག་ཁབ་ལོང་གིས་ཀྱང་ལྕགས་མ་ཕྲད་པ་ཐམས་ཅད་ཇི་ལྟར་མི་འདྲེན། ཡུལ་དང་ཕྲད་པ་ཉིད་ཅིག་ཡིན་ན་ཡང་ཅིའི་ཕྱིར་མིག་སྨན་ནམ་ཐུར་མ་ཕྲད་པ་ཐམས་ཅད་མི་མཐོང་སྟེ་དེ་ནི་མཚུངས་སོ། །

[Block 772]
ཇི་ལྟར་ཡང་སྣ་ལ་སོགས་པ་ཡུལ་དང་ཕྲད་པ་ཡིན་ཡང་ལྷན་ཅིག་སྐྱེས་པའི་དྲི་ལ་སོགས་པ་མི་འཛིན་པའི་ཕྱིར་ཐམས་ཅད་ནི་མ་ཡིན་པ་དེ་བཞིན་དུ། མིག་ཀྱང་མ་ཕྲད་པ་ཡིན་མོད་ཀྱི་ཐམས་ཅད་ནི་མ་ཡིན་ནོ། །

[Block 773]
ཡིད་ནི་གཟུགས་ཅན་མ་ཡིན་པའི་ཕྱིར་ཕྲད་པ་ཉིད་དུ་མི་ནུས་སོ། །

[Block 774]
ཡང་ཁ་ཅིག་ནི་རྣ་བའི་ནང་དུ་ཡང་སྒྲ་ཐོས་པའི་ཕྱིར། རྣ་བ་ནི་ཡུལ་དང་ཕྲད་པ་དང་མ་ཕྲད་པ་ཡང་ཡིན་པར་སེམས་སོ། །

[Block 775]
ལྷག་མ་སྣ་དང་ལྕེ་དང་ལུས་ཞེས་བྱ་བ། གསུམ་གཞན་དུ།

[Block 776 [VERSE]]
ཡུལ་དང་ཕྲད་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །
སྣ་ཇི་ལྟར་ཡུལ་དང་ཕྲད་པ་ཡིན་ཞེ་ན།
དབུགས་མ་བརྔུབས་པར་དྲི་མི་འཛིན་པའི་ཕྱིར་རོ། །

[Block 777]
ཕྲད་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན། འདབ་ཆགས་པར་འབྱུང་བའོ། །

[Block 778]
ཅི་རྡུལ་ཕྲ་རབ་རྣམས་ཕན་ཚུན་རེག་གམ་འོན་ཏེ་མི་རེག་ཅེ་ན། ཁ་ཆེ་བ་རྣམས་ན་རེ་མི་རེག་གོ་ཞེས་ཟེར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། རེ་ཞིག་གལ་ཏེ་བདག་ཉིད་ཐམས་ཅད་ཀྱིས་རེག་པར་འགྱུར་ན་ནི་རྫས་རྣམས་འདྲེས་པར་འགྱུར་རོ། །

[Block 779]
འོན་ཏེ་ཕྱོགས་གཅིག་གིས་རེག་ན་ནི་ཆ་ཤས་དང་བཅས་པ་དག་ཏུ་ཐལ་བར་འགྱུར་བ་ཞིག་ན་རྡུལ་ཕྲ་རབ་རྣམས་ནི་ཆ་ཤས་མེད་པ་ཡིན་ནོ། །

[Block 780]
འོ་ན་ཇི་ལྟར་སྒྲ་མངོན་པར་འགྲུབ་པར་འགྱུར་ཞེ་ན། དེ་ཉིད་ཀྱི་ཕྱིར་ཏེ། གལ་ཏེ་རེག་པར་གྱུར་ན་ལག་པས་ལག་པ་ལ་བསྣུན་ན་འབྱིང་བར་འགྱུར་ལ། རྡོ་བས་རྡོ་བ་ལ་བསྣུན་ན་ཡང་འབྱིང་བར་འགྱུར་རོ། །

[Block 781]
ཇི་ལྟར་བསགས་པ་ལ་བརྒྱབ་ན་ཞིགས༌[^334]པར་མི་འགྱུར་ཞེ་ན། རླུང་གི་ཁམས་ཀྱིས་བཟུང་བའི་ཕྱིར་རོ། །

[Block 782]
རླུང་གི་ཁམས་ཁ་ཅིག་ནི་འཇིག་པར་ཞུགས་པ་ཡིན་ཏེ་དཔེར་ན་འཇིག་པའི་ཚེ༌[^335]ལྟ་བུའོ། །

[Block 783]
ཁ་ཅིག་ནི་འཛིན་པར་ཞུགས་པ་ཡིན་ཏེ་དཔེར་ན་ཆགས་པའི་ཚེ༌[^336]ལྟ་བུའོ། །

[Block 784]
ད་ནི་ཇི་ལྟར༌[^337]འདབ་ཆགས་པར་ཕྲད་པས་གསུམ་པོ་ཡུལ་དང་ཕྲད་པ་ཞེས་བྱ་ཞེ་ན། དེ་དག་གི་དབུས་ན་ཅུང་ཟད་ཀྱང་མེད་པ་གང་ཡིན་པ་དེ་ཁོ་ན་འདབ་ཆགས་པ་ཉིད་ཡིན་ནོ། །

[Block 785]
ཡང་འདུས་པ་རྣམས་ནི་ཆ་ཤས་དང་བཅས་པ་ཡིན་པའི་ཕྱིར་རེག་པར་འགྱུར་བས་ཉེས་པ་མེད་དོ། །

[Block 786]
དེ་ལྟར་བྱས་ན་བྱེ་བྲག་ཏུ་བཤད་པ་ལས།

[Block 787]
ཅི་རེག་པའི་རྒྱུ་ཅན་གྱི་རེག་པ་ཞིག་སྐྱེས་པ་འམ། འོན་ཏེ་མ་རེག་པའི་རྒྱུ་ཅན་ཞིག་སྐྱེ་ཞེས་དྲིས་ནས་སྨྲས་པ། རྒྱུའི་ཕྱིར་རེས་འགའ་ནི་རེག་པའི་རྒྱུ་ཅན་གྱི་མ་རེག་པ་སྐྱེ་སྟེ། གང་གི་ཚེ་རྣམ་པར་ཞིགས་པ་ནའོ། །

[Block 788]
རེས་འགའ་ནི་མ་རེག་པའི་རྒྱུ་ཅན་གྱི་རེག་པ་སྐྱེ་སྟེ། གང་གི་ཚེ་བསགས་པར་འགྱུར་བ་ནའོ། །

[Block 789]
རེས་འགའ་ནི་རེག་པའི་རྒྱུ་ཅན་གྱི་རེག་པ་སྐྱེ་སྟེ། གང་གི་ཚེ་བསགས་པ་དང་ལྡན་པ་བསགས་པ་ཁོ་ནའོ། །

[Block 790]
རེས་འགའ་ནི་མ་རེག་པའི་རྒྱུ་ཅན་གྱི་མ་རེག་པ་སྐྱེ་སྟེ་དཔེར་ན་ཉི་ཟེར་གྱི་རྡུལ་ལྟ་བུའོ་ཞེས་འབྱུང་བའི་གཞུང་འདི་ཡང་འཐད་པར་འགྱུར་རོ། །

[Block 791]
བཙུན་པ་དབྱིག་བཤེས་ན་རེ་ནི་རྡུལ་ཕྲ་རབ་རྣམས་རེག་པར་གྱུར་ན་ནི་སྐད་ཅིག་མ་ཕྱི་མར་གནས་པར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 792]
བཙུན་པ་ན་རེ་ནི་རེག་པ་ནི་མེད་ཀྱི་འདབ་ཆགས་པ༌[^338]ལ་རེག་གོ་སྙམ་དུ་འདུ་ཤེས་པར་ཟད་དོ་ཞེས་ཟེར་ཏེ། བཙུན་པའི་ལུགས་འདོད་པར་བྱའོ། །

[Block 793]
དེ་ལྟ་མ་ཡིན་ན་ནི༌[^339]རྡུལ་ཕྲ་རབ་བར་དང་བཅས་པ་རྣམས་ཀྱིས༌[^340]བར་སྟོང་པ་དག་ཏུ་འགྲོ་བ་ལ་སུ་ཞིག་འགོག་ན་འདི་ལྟར་ཐོགས་པ་དང་བཅས་པ་དག་ཏུ་འདོད། རྡུལ་ཕྲ་རབ་རྣམས་ལས་བསགས་པ་དག་གཞན་པ་ཡང་མ་ཡིན་པས་དེ་དག་ཁོ་ན་བསགས་པ་ལ་རེག་པ་ཡིན་ཏེ་དཔེར་ན་གཟུགས་སུ་རུང་བ་ལྟ་བུའོ། །

[Block 794]
གལ་ཏེ་རྡུལ་ཕྲ་རབ་ལ་ཕྱོགས་ཆ་ཐ་དད་པར་རྟོག༌[^341]ན་ནི་རེག་གམ་མ་རེག་ཀྱང་རུང་སྟེ། ཆ་ཤས་དང་བཅས་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 795]
གལ་ཏེ་མ་ཡིན་ན་ནི། རེག་ཀྱང་ཐལ་བར༌[^342]མི་འགྱུར་རོ། །

[Block 796 [HEADING]]
##### ཡུལ་མཉམ་པ་དང་མི་མཉམ་པ་འཛིན་པ། ^1-3-19-3-0

[Block 797]
ཡང་ཅིའི༌[^343]མིག་ལ་སོགས་པ་འདི་དག་གིས་བདག་ཉིད་ཀྱི་ཚད་དང་མཉམ་པའི་དོན་ལ་མགལ་མེའི་འཁོར་ལོ༌[^344]ལ་སོགས་པ་བཞིན་དུ་མྱུར་དུ་འཇུག་པས་རི་ལ་སོགས་པ་འཛིན་ཏམ། འོན་ཏེ་མཉམ་པ་དང་མི་མཉམ་པ་ཞིག་ལ་འཛིན་ཅེ་ན། རེ་ཞིག་གང་དག་ཡུལ་དང་ཕྲད་པར་བཤད་པ། སྣ་ལ་སོགས་པ་གསུམ་པོ་དེ་དག་རྣམས་ཀྱིས་ནི། ཡུལ་ནི་མཉམ་པར་འཛིན་པར་འདོད། །དབང་པོའི༌[^345]རྡུལ་ཕྲ་རབ་རྣམས་ཇི་སྙེད་པ་དེ་སྙེད་ཀྱི༌[^346]ཡུལ་གྱི་རྡུལ་ཕྲ་རབ་རྣམས་དང་ཕྲད་ནས་རྣམ་པར་ཤེས་པ་སྐྱེད་དོ། །

[Block 798]
མིག་དང་རྣ་བ་དག་གིས་ནི་མ་ངེས་ཏེ། རེས་འགའ་ནི་ཆུང་སྟེ་གང་གི་ཚེ་སྐྲའི་རྩེ་མོ་མཐོང་བ་ནའོ། །

[Block 799]
རེས་འགའ་ནི་མཉམ་སྟེ་གང་གི་ཚེ་རྒུན་འབྲུམ༌[^347]མཐོང་བ་ནའོ། །

[Block 800]
རེས་འགའ་ནི་ཆེ་སྟེ་གང་གི་ཚེ་མིག་ཕྱེ་བ་ཙམ་གྱིས་རི་ཆེན་པོ་མཐོང་བ་ནའོ། །

[Block 801]
དེ་བཞིན་དུ་རྣ་བས་སྦྲང་བུ་དང་འབྲུག་ལ་སོགས་པའི་སྒྲ་ཐོས་པ་ལ༌[^348]ཡང་སྦྱར་བར་བྱའོ། །

[Block 802]
ཡིད་ནི་ལུས་ཅན་མ་ཡིན་པ་ཁོ་ན་བས་འདིའི་ཚད་ཡོངས་སུ་ཆད་པ་ནི་མི་སྤྱད༌[^349]དོ། །

[Block 803 [HEADING]]
##### དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ཇི་ལྟར་གནས་པ། ^1-3-19-4-0

[Block 804]
ཡང་མིག་གི་དབང་པོ་ལ་སོགས་པ་འདི་དག་གི་རྡུལ་ཕྲ་རབ་རྣམས་ཇི་ལྟར་གནས་ཤེ་ན། རེ་ཞིག་མིག་གི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་མིག་གི་འབྲས་བུ་ལ། གོ་སྙོད་ཀྱི་མེ་ཏོག་བཞིན་དུ་གནས་ཏེ། ཁ་དོག་དང་བཅས༌[^350]བཀབ་པས༌[^351]གྱེས་པར་མི་འགྱུར་རོ། །

[Block 805]
གཞན་དག་ན་རེ་གོང་བུ་བཞིན་དུ་བླ་འོག་ན་གནས་ཏེ། ཤེལ་བཞིན་དུ་དང་བའི་ཕྱིར་ཕན་ཚུན་མི་སྒྲིབ་པོ་ཞེས་ཟེར་རོ། །

[Block 806]
རྣ་བའི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་རྣ་བའི་བུ་གའི༌[^352]ནང་ན་གནས་སོ། །

[Block 807]
སྣའི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་མཚུལ་པའི་ནང་ན་གནས་ཏེ། དབང་པོ་དང་པོ་གསུམ་ནི་ཕྲེང་བ་བཞིན་དུ་གནས་སོ། །

[Block 808]
ལྕེའི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་ཟླ་བ་ཁམ་པ་ལྟ་བུ་ཡིན་ཏེ། ལྕེའི་དབུས་ན་སྐྲའི་རྩེ་མོའི་ཁྱོན་ཙམ་ཞིག་ལྕེའི་དབང་པོའི་རྡུལ་ཕྲ་རབ་དག་གིས་མ་ཁེབས་སོ་ཞེས་གྲག་གོ། །

[Block 809]
ལུས་ཀྱི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་ལུས་བཞིན་དུ་གནས་སོ། །

[Block 810]
མོའི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་རྔའི་སྦུབས་ལྟ་བུ་ཡིན་ནོ། །
--- END BLOCKS ---
