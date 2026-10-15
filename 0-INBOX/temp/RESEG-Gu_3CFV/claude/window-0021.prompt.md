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
[Block 736]
མི་བྱ་བར་བརྗོད་པ་ཙམ་དུ་ཟད་པ་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 737]
བཟའ་བར་བྱ་བ་ནང་དུ་བཅུག་པའི་ཤིང་རྟ་ནི་རེག་པར་བྱ་བ་ཉིད་མ་ཡིན་ཏེ། མི་རེག་ཏུ་མི་རུང་བའི་རྐྱེན་དེ་ལྟ་བུ་དག་ཡོད་ན་དེའི་ཚེ་ཡང༌[^437]ཁ་ལོ་བའི་སྟན་གཅིག་པོ་སྟེ༌[^438]གཏོགས་པའི་ཤིང་རྟ་ལ་རེག་པར་བྱའོ། །

[Block 738]
འདིར་ཤིང་རྟ་ལ་རེག་པ་ལ་མི༌[^439]རུང་བ་ཉིད་ནི་མ་ཡིན་ཏེ། ཤིང་རྟ་དང་འབྲེལ༌[^440]པའི་ཟས་སུ་བྱ་བ་ལ་འདི་བསྟན་པའོ། །

[Block 739]
གང་བ༌[^441]ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འབྲས་ལ་སོགས་པས་ཁ་ལོ་བའི་སྟན་གྱིས་ཤིང་རྟ་ཉིད་སྤངས་པ་ཉིད་དོ། །

[Block 740]
ནད་པ་ཞོན་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཟས་ཀྱིས༌[^442]སྟོང་པའི་ཤིང་རྟ་དག༌[^443]ཡང་ཁ་ལོ་བའི་སྟན་སྤངས་པ་ཉིད་ཁོ་ནའོ། །

[Block 741]
གྲུ་ལ་ནི་རུ་སྐྱའོ་ཞེས་བྱ་བ་ནི་དེ་དང་འབྲེལ་པའི་བཟའ་བར་བྱ་བ་བཅུག་པའི་གྲུ་དང་དེ་དག༌[^444]འབྲེལ་པས་གང་བའི་གྲུ་དང་གྲུར་འཇུག་པ་ལ་རུ་སྐྱ་སྤངས་པ་ཉིད་དོ། །

[Block 742]
ན་བ་མེད་ཀྱང་འདིར་འཇུག་པ་རིགས་པ་ཞེས་གསུངས་པ་དེ་བས་ན་ན་བའི་སྒྲས་ནི་འདི་ལས་བཟློག་པས་ཤེས་པའོ། །

[Block 743]
དེ་འཛིན་པའི་སྟན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རུ་སྐྱ་འཛིན་པའི་དོན་ཅན་གྱི་སྟན་ལས༌[^445]དེ་འབྲེལ་པའི་ཁ་ཟས་སུ་བྱས་པ་ལ་རེག་པ་དང་གང་བ་དང་གྲུར་འཇུག་པ་ན་སྤང་བར་བྱ་བ་ཉིད་དོ། །

[Block 744]
དགེ་འདུན་གྱི་སྨན་དག་ལྡུད་པ༌[^446]ནི་བསྐྱམ་པ་དང་དབྱུང་བ་དང་གཟར་བུའི་ལས་དང་དབོག་པ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་ཟ་བ་ལ་སོགས་པ་སྨན་དག་དང་གང་ཟག་གི་ཡང་རུང་སྟེ། དེ་དག་ལྡུད་པ༌[^447]ན་བསྐྱམ་པ་ལ་སོགས་པའི་ཕྱིར་རེག་པ་ལ་ཡང་མི་རུང་བ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 745]
ཅི་དང་པོ་ཉིད་དུ་འདི་དག་རྣམ་པ་འདི་ལྟ་བུ་ཉིད་ལ་རེག་པར་བྱ་བ་ཉིད་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་དང་པོར་ཤིང་དབྲི་བ་དང་མེ་གསད་པ༌[^448]དང་གོས་ཀྱི་ཐུ་བ་ལ་སོགས་པས་རླུང་གཡབ་པས་འབད་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ།

[Block 746]
དང་པོ་ཁོ་ནར་ལུད་པ་ཞི་བར་བྱ་བའི་ཕྱིར་འདི་ལྟར་འབད་པར་བྱའོ། །

[Block 747]
དེ་ལྟར་གཉེན་པོར་བྱ་བ་མ་གྲུབ་པ་ལ་བསྐྱམ་པ་ལ་སོགས་པ་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 748]
གཉེན་པོ་བྱེད་པའི་ནུས་པ་མེད་ན་མ་རེག་པར་བསྐྱམ་པ་ལ་སོགས་པ་ལ་ཉེས་པ་མེད་ཅེས་བྱ་བ་འདིར་དེ་ལ་རྩེ་གཅིག་པ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 749]
དེ་བས་ན་འདི་ལྟར་ཤེས་པར་གྱུར་པ་ལ་གཉེན་པོར་བྱ་བ་མ་ཡིན་པ་ཉིད་དེ་དང་པོར་བསྐྱམ་པ་ལ་སོགས་པ་ཉེས་པ་མེད་ཅེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 750]
ཆུ་ཀླུང་རྒལ་བའི་ཕྱིར་རམ་ཁུར་ཚ་བ་སྙེག་པའི་ཕྱིར་ལག་ཉར་བླངས་པའི་ལམ་བརྒྱགས༌[^449]རུང་སྟེ། ཆོ་ག་མ་འབྱོར་ཏམ༌[^450]ལམ་བརྒྱགས༌[^451]གཞན་མེད་ནའོ་ཞེས་བྱ་བ་ནི། རུང་སྟེ་ཞེས་བྱ་བ་ནི་བཟར་རུང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 751]
ཆོ་ག་མ་འབྱོར་ཏམ༌[^452]ཞེས་བྱ་བ་ནི་གང་གིས་རེག་པ་ལ་བླངས་པ་ཉིད་མ་ཡིན་ན་དེས་ནི་ཆུ་ཀླུང་རྒལ་བ་དང་སྙེག་པ་འདི་དག་ལ་བྱ་བ་ཉིད་དོ། །

[Block 752]
དེས་གནས་པ་ལ་རང་གི་ཡན་ལག་གམ་དེ་དང་འབྲེལ་པ་གཞན་གྱིས་ཤེས་པར་བྱ་བ་འདི་ལ་བྱ་བ་ཉིད་དོ། །

[Block 753]
གཞན་མེད་ནའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གཞན་ཁུར་ཚ་བ་མེད་པར་གྱུར་ན་དེ་ལ་ཆོ་ག་མ་གྲུབ་པའི་དབང་གིས་འདིར་དོན་དུ་བསྐུར་བ༌[^453]ལ་རུང་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 754]
ཁུར་ཚ་བ་མེད་ན་སྦྱིན་བདག་སྤྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ལམ་བརྒྱགས༌[^454]དེ་ཁྱེར་བའི་ཁུར་ཚ་བ་གཞན་མེད་ན་དེ༌[^455]སྦྱིན་བདག་གིས་དེ་ལ་བསྐུར༌[^456]བར་སྤྲོ་བ་བསྐྱེད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 755]
ཁྱེར་བ་མེད་ན་རང་གིས་སོ་ཞེས་བྱ་བ་ནི་སྦྱིན་བདག་ལ་བཅོལ་བ་ཡང་མ་གྲུབ་ན། དེའི་ཚེ་རང་གིས་ལམ་བརྒྱགས་བསྐུར༌[^457]བར་བྱའོ། །

[Block 756]
དེ་ཉིད་ལས་སྦྱིན་པར་བརྗེ༌[^458]ཞིང་བླང་བ་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་ཁྱེར་དུ་གཞུག་པ་མ་གྲུབ་ཅིང་རང་གིས་ཁྱེར་བར་གྱུར་ན། རང་གིས་ཁྱེར་བ་དེ་ཉིད་ལས་གཞན་ལ་སྦྱིན་པས་ལམ་བརྒྱགས་བརྗེ༌[^459]ཞིང་བླང་བ་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 757]
འདི་ནི་གཞན་ལ་བསྒྲུབ་པ༌[^460]ལ་མི་བྱའོ། །

[Block 758]
དེ་ཡང་མ་གྲུབ་ན་དེ་བཟའ་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དེ་ཡང་དེ་ཉིད་ཀྱི་ཕྱིར་སྦྱིན་པས་བརྗེ༌[^461]ཞིང་བླང་བ་མ་གྲུབ་ན་རང་གིས་ཁྱེར་བ་དེ་ཡང་བཟའ་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 759]
བྱིན་ལེན་སྟོབས་པ་མེད་ན་བྱིན་ལེན་མ་བྱས་པ་དེ་འམ་གཞན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རང་གིས་ཁུར་བ་དེ་འམ་གཞན་བྱིན་ལེན་བྱས་པ་མེད་པར་གྱུར་ན་བྱིན་ལེན་མ་བྱས་པ་ཡང་བཟའ་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 760]
སླར་རང་གིས་ཁྱེར་བ་དང་བྱིན་ལེན་མ་བྱས་པ་དེ་གཉིས་གང་གིས་བཟའ་བར་བྱ་བ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཟན་བཅད་པར་བྱས་པའི་འོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་ཇི་ཙམ་བཟའ་བར་བྱ་བ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཉི་མ་དང་པོ་ལ་སྤར་གང་ངོ་། །

[Block 761]
གཉིས་པ་ལ་ནི་དོའོ། །

[Block 762]
གསུམ་པ་ལ་ནི་ཅི་ཙམ་གྱིས༌[^462]ཆོག་པའོ། །

[Block 763]
ཤིང་ཐོག༌[^463]རུང་བར་མ་བྱས་པ་དང་བྱིན་ལེན་མ་བྱས་པ་དང་། ལག་ཉར་བླངས་པ་དག་ཀྱང་དུས་མ་ཡིན་པར་ཡང་བཟའ་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་དག་ཐམས་ཅད་ཀྱང་གཞན་མ་གྲུབ་ན་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པ་ཉིད་ཡིན་ནོ། །

[Block 764]
དེ་དག་སུའི་བཟའ་བར་བྱ་བ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཟན་མེད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཟན་མེད་པར་གྱུར་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅི་གནས་སྐབས་ཐམས་ཅད་དུ་འམ་ཞེ་ན། དེའི་ཕྱིར་ཤིན་ཏུ་བཀྲེས་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཀྲེས་པ༌[^464]སྲོག་ལ་བབ་པ་ལ་ཐུག་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 765]
རྩ་བ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་དུས་མ་ཡིན་པར་བཟའ་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 766]
རང་གིས་ཀྱང་བཏོགས་པ༌[^465]ཉིད་དང་དབྱུང་བ་ཉིད་དང་བསྒྲུབ་པར་བྱ་བ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ཟས་མེད་པ་ཤིན་ཏུ་བཀྲེས་པ་ཉིད་ན་འབྲས་བུ་རྣམས་དང་རྩ་བ་རྣམས་ལའོ། །

[Block 767]
འདིར་གྲངས་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་པར་མི་བྱ་སྟེ། རྩ་བ་རྣམས་ལ་ཡང་བཏོགས་པ༌[^466]ཉིད་ཡོད་པའི་ཕྱིར་རོ། །

[Block 768]
དཔེར་ན་ཆུ་འགྲམ་དུ་སྐྱེས་པ་ངོས་ལྟུང་བ་རྣམས་ལྟ་བུའོ། །

[Block 769]
འབྲས་བུ་རྣམས་ལ་ཡང་བཏོན་པ་ཉིད་ཡོད་པའི་ཕྱིར་རོ། །

[Block 770]
དཔེར་ན་པ་ན་ས་ལ་སོགས་པ་རྣམས་ལྟ་བུའོ། །

[Block 771]
བྱིན་ལེན་མ་བསྟབས་པ་དང་རུང་བར་མ་བྱས་པ་དང་དུས་མ་ཡིན་པར་བཟའ་བ་ལ་སོགས་པ་རུང་བར་བྱ་བ་དག་ལ་ཐམས་ཅད་དུ་རྩོམ་འདོད་པ་ལ་སོགས་པ་ན་བྱང་གི་སྒྲ་མི་སྙན་ན་གྲགས་པའི་ཡིད་ལ་བྱེད་པ་བྱའོ་ཞེས་བྱ་བ་ནི་རང་གིས་བྱེད་པར་འདྲ་བ་ལ་རྣམ་པར་དག་པར་གྱུར་པའི་སྡེ་འདི་སྐས་ཀྱི་གདང་བུ་ལྟ་བུར་གྱུར་པ་སྟེ། བྱེ་བྲག་ཐོབ་པའི་ཕྱིར་དེ་དང་འདྲ་བའོ།[^467] །ཇི་ལྟར་མངོན་པར་འདུ་བྱེད་པས་ཀྱང་ཡིད་ལས་ངེས་པར་འབྱུང་བ་ཞེས་བྱ་བ་ནི་རྩོམ་འདོད་པ་ནའོ། །

[Block 772]
དེ་བས་ན་འདིར་ཐམས་ཅད་དུ་བྱང་གི་སྒྲ་མི་སྙན་ན་གྲགས་པའི་ཕྱིར་རྩོམ་འདོད་པ་ལ་སོགས་པའོ། །

[Block 773]
ཐམས་ཅད་དུ་ཞེས་བྱ་བ་ནི་རྩ་བ་དང་འབྲས་བུ་ལ་བརྟེན་པ་འདི་ཉིད་ལ་མ་ཡིན་ནོ། །

[Block 774]
འདིར་སོགས་པའི་སྒྲས་ནི་ལེན་པ་དང་ཉེ་བར་ལེན་པའི་དོན་དུ་རིག་པར་བྱའོ། །

[Block 775]
ལག་པ་བསྙལ་བ་དང་འདབ་མ་དག་ཡོད་ན་སྐྱོགས་ཀྱིས་སྐོམ་མི་བཏུང་ངོ་ཞེས་བྱ་བ་ནི་ཆུ་ཉུང་ཟད་ཉིད་དང་ལམ་འགྲོན་ཤོར་བ་ལ་སོགས་པས་ལག་པ་བསྙལ་བ་མེད་པའོ། །
--- END BLOCKS ---
