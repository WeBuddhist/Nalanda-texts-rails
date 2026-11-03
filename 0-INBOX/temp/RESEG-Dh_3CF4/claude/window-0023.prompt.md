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
དེའི་རྒྱུ་ནི་ལོངས་སྤྱོད་དོ། །

[Block 807]
དེའི་གཞིར་གྱུར་པ་ནི་སྦྱིན་པར་བྱ་བ་ཡིན་ཏེ། སྦྱིན་པའི་དངོས་པོ་དམ་པའོ། །

[Block 808]
འདིས་ནི་སྦྱིན་པའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། སྦྱིན་པ་ཐམས་ཅད་བྱིན་པར་སྟོན་ཏོ། །

[Block 809]
དེ་དག་གིས་ནི་གང་དག་ལ་སྦྱིན་པ་དང་གང་གི་ཕྱིར་སྦྱིན་པ་དེ་བསྟན་པ་ཡིན་ནོ། །

[Block 810]
བདེ་བའི་རྒྱུ་དང་གཞིར་གྱུར་པ་ཞེས་བྱ་བ་ལ། ཚུལ་ཁྲིམས་དང་གསོ་སྦྱོང་ནི་བདེ་བའི་རྒྱུ་སྟེ། ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུ་མངོན་པར་མཐོ་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 811]
དེའི་གཞིར་གྱུར་པ་ནི་ཚུལ་ཁྲིམས་ངན་པ་མ་ཡིན་པ་དེ་དག་གོ། །

[Block 812]
ཡང་གང་སྲོག་གཅོད་པ་ལ་སོགས་པ་ལས་ལྡོག་པའི་མཚན་ཉིད་དོ། །

[Block 813]
མུ་སྟེགས་ལ་སོགས་པ་གཞན་དག་ནི་རང་གི་བཏགས་པའི་ཚུལ་ཁྲིམས་ཞེས་བྱ་བའི༌[^456]དོན་ཏོ། །

[Block 814]
འདིས་ནི་བསླབ་པའི་གཞི་ལྔ་འཛིན་པར་བསྟན་ཏོ། །

[Block 815]
གསོ་སྦྱོང་དང་ངེས་པར་གནས་པ་དག་ཀྱང་ཡང་དག་པར་ལེན་ཏེ། གསོ་སྦྱོང་ངན་པ་མ་ཡིན་པ་ནི་ཡན་ལག་བརྒྱད་པ་སྟེ། བདེ་བའི་རྒྱུ་དང་གཞིར་གྱུར་པ་ཞེས་བྱ་བ་དང་སྦྱར་རོ།[^457] །བསོད་ནམས་ཀྱི་མཐུ་བསྒྲགས་པ་ཞེས་བྱ་བ་ལ། བསོད་ནམས་ནི་དགེ་བ་དང་ཆོས་སོ། །

[Block 816]
དེའི་མཐུ་ནི་འབྲས་བུ་ཆེན་པོར་གྱུར་པ་ཡིན་པས་དེ་བསྒྲགས་པས་ཏེ། [^458]བསོད་ནམས་ཀྱི་མཐུ་བསྒྲགས་པའི་རྒྱུས་སོ། །

[Block 817]
ལེགས་པར་དགོད་པར་འདོད་པས་དང་བའི་སེམས་ཀྱིས་ཞེས་བྱ་བ་ནི་བསོད་ནམས་ཀྱི་འབྲས་བུ་མངོན་སུམ་དུ་བསྟན་པས་སོ། །

[Block 818]
དོན་ངེས་པ་ཞེས་བྱ་བ་ནི་མི་འགྱུར་བ་ཉིད་ཀྱི་དོན་ཏོ། །

[Block 819]
བདེ་བར་གཤེགས་ལ༌[^459]བཀུར་སྟི་ཞེས་བྱ་བ་ལ། མཛེས་པར་གཤེགས་པས་ན་བདེ་བར་གཤེགས་པ་སྟེ། འདིའི་ལམ་དུ་ཞུགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 820]
དེ་ལ་བཀུར་སྟི་ནི་སྦྱིན་པ༌[^460]དང་། ཉེ་བར་འགྲོ་བ་དང་རིམ་གྲོ་ལ་སོགས་པའི་མཚན་ཉིད་དོ། །

[Block 821]
མེད་ཅེས་ཐོས་ཞེས་བྱ་བའི་སྒྲ་ནི་མཐོང་བར་འགྱུར་བ་མེད་བ་སྟེ། གང་ཐོས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 822]
སྔོན་ཞེས་བྱ་བ་ནི་སྐྱེ་བ་གཞན་དག་ཏུའོ། །

[Block 823]
ཟན་དྲོན་ཁེངས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་བསྡུས་པའི་དོན་ནི་དངོས་པོ་དང་། ཚད་དང་། ལེགས་པར་མ་སྦྱར་བ་སྟེ། སྦྱིན་པའི་དངོས་པོ་ཤིན་ཏུ་ཞན་པ་ཡིན་པས་དེ་སྐད་བསྟན་ཏོ། །

[Block 824]
ལན་ཚྭ་མེད་པ་ཞེས་བྱ་བ་འདིས་ནི་རོ་དམན་པའོ། །

[Block 825]
ཁེངས་པ་ཞེས་བྱ་བ་ནི་ཚོད་མ༌[^461]མེད་པ་སྟེ། འདིས༌[^462]ནི་རེག་བྱ་ཞེན༌[^463]པའོ། །

[Block 826]
རྩུབ་པ་ཞེས་བྱ་བ༌[^464]ནི་སྣུམ་མེད་པའོ། །

[Block 827]
འདིས་ནི་དྲི༌[^465]དམན་པའོ། །

[Block 828]
འདི་དག་གིས་ནི་ལེགས་པར་མ་སྦྱར་བ་བསྟན་པ་ཡིན་ནོ། །

[Block 829]
དེ་དག་ཉེ་བར་བླངས་པའི་ཚུལ་ཡིན་ཏེ། དེས་ན་དེའི་ཕུན་སུམ་ཚོགས་པ་མེད་པར་གྱུར་པའོ། །

[Block 830]
ཟན་དྲོན་ཞེས་སྨོས་པས་ནི་དངོས་པོ་སྟེ་ངན་པའོ། །

[Block 831]
ཆང་གཅིག་ཞེས་པས་ནི་ཆུང་བ་སྟེ་ཚད་དོ། །

[Block 832]
དེ་གཉིས་ཀྱིས་ནི༌[^466]ཕུན་སུམ་ཚོགས་པ་དང་བྲལ་བར་ཡང་སྟོན་ཏོ། །

[Block 833]
འབྲས་བུ་འབྱོར་པ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་ཁ་དོག་ལ་སོགས་པ་ཕུན་སུམ་ཚོགས་པའི་དངོས་པོ་སྟེ། གཟུགས་བཟང་བར་གྱུར་པ་དང་། གྲགས་པ་དང་ལྡན་པ་དང་། དགའ་བར་གྱུར་པ་དང་། གཞོན་ཤ་ཆགས་པ་དང་། བདེ་བའི་རེག་པ་དང་ལྡན་པའོ། །

[Block 834]
དེ་ལྟར་སྦྱིན་པའི་དངོས་པོ་ནི་ཁ་དོག་ལ་སོགས་པ་མེད་ཀྱང་བདེ་བར་གཤེགས་པ་ལ་བཀུར་སྟི་བྱས་པས་ནི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་བཤད་པ་ཡིན་ནོ། །

[Block 835]
ཡང་ན་མཐོ་རིས་ཀྱི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 836]
ཕྱི་རོལ་གྱི་དངོས་པོའི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་དང་། ནང་གི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་སྟེ། དེ་ལས་ནང་གི་ཕུན་སུམ་ཚོགས་པའི་དངོས་པོའི་དབང་དུ་བྱས་ནས་སྦྱིན་པའི་དངོས་པོ་ཁ་དོག་ལ་སོགས་པ་མེད་ཀྱང་གཟུགས་མཛེས་པར་འགྱུར་བ༌[^467]དང་། དྲི་དང་བྲལ་བ་ཡིན་ཡང་གྲགས་པ་ཆེ་བ་དང་། རེག་བྱ་ཕུན་སུམ་ཚོགས་པ་མེད་ཀྱང་བདེ་བའི་རེག་པ་དང་ལྡན་པ་སྟེ། འདི་ནི་ནང༌[^468]གི་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 837]
ཡང་ན་ནང་གི་ནི་ཟླ་མེད་པ་ཡིན་པས་དེ་ནི་ཐམས་ཅད་ཀྱི༌[^469]མངོན་སུམ་དུ་གྱུར་པས་བརྗོད་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 838]
ད་ནི་ཕྱི་རོལ་གྱི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པའི་དབང་དུ་བྱས་ནས། ཤིང་རྟ་སྣ་ཚོགས་རྟ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཤིང་རྟ་དང་། རྟ་དང་གླང་པོ་ཆེ་སྨོས་པས་ནི་ནུས་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 839]
ས་ཆེན་འདི་ནི་ཞེས་བྱ་བ་འདིས་ཡུལ་མི་དང་། མཁར་དང་། གྲོགས་པོ་དང་། མཛའ་བཤེས་ལ་སོགས་པ་གཟུང་ངོ་། །ནོར་མང་ཞེས་བྱ་བ་འདིས་ནི་མཛོད་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 840]
དཔལ་ཡང་རྗེས་ཆགས་བཙུན་མོ་རྒྱ་ཆེན་ལྡན་ཞེས་བྱ་བ་འདིས་ནི་ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 841]
ལོངས་སྤྱོད་པའི་དངོས་པོ་ཡང་རྣམ་པ་གཉིས་ཏེ། རྫས་ལ་ཉེ་བར་ལོངས་སྤྱོད་པའི་དངོས་པོ་དང་། འཁྲིག་པ་ལ་ཉེ་བར་ལོངས་སྤྱོད་པའི་དངོས་པོར་བཤད་དེ། དེ་གཉིས་ཀྱང་གོ་རིམས་ཇི་ལྟ་བ་བཞིན་དུ་རང་བཞིན་གྱིས༌[^470]ཕུན་སུམ་ཚོགས་པ་དང་། ཉེ་བར་ལོངས་སྤྱོད་པའི་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 842]
འབྲས་བུ་གྲུབ་པ་བཟང་པོ་ཞེས་བྱ་བ་ནི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་སྟེ། བཟང་པོ་ནི་མཛེས་པའོ། །

[Block 843]
ཟན་དྲོན་ཆང་གཅིག་ཅེས་བྱ་བ་ནི་སྔར་བཤད་པས་མཚོན་པར་བྱའོ། །

[Block 844]
བློན་པོ་ཆེན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཉིད་སྨོས་པ་ནི་ཐག་ཉེ་བ་ན་སྤྱོད་པ་དང་། རིགས་མཐོ་བ་ཕུན་སུམ་ཚོགས་པ་དང་། གློ་བ་ཉེ་ཞིང་ཞུ་བར་ནུས་པའོ། །

[Block 845]
སྨྲ་བའི་སྤོབས་པ་ནི་སྨྲ་བར་ནུས་པའོ། །
--- END BLOCKS ---
