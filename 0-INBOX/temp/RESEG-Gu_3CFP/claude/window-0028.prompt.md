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
[Block 981]
ཐམས་ཅད་སྦྱིན་པ་འདིའི་བསྡུས་པའི་དོན་དང་གོ་རིམ་བཤད་པར་བྱ་སྟེ། དེ་ལ་ཐམས་ཅད་སྦྱིན་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལས་བརྩམས་ནས་ཇི་ལྟར་ངན་སོང་ཐམས་ཅད་ལས་ཤིན་ཏུ་འདས་པ་ཐོབ་པ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 982]
དེ་ལ་ཟང་ཟིང་གི་སྦྱིན་པ་ནི་མདོར་བསྡུ་ན༌[^735]རྣམ་པ་གསུམ་སྟེ། ཡོད་ཅིང་བདོག་བཞིན་དུ༌[^736]ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ཡོད་ཅིང་བདོག་བཞིན་དུ་ཞེས་བྱ་བ་དང་། འདི་དང་གཞན་རྒྱས་པར་དབྱེ་བར་བྱ༌[^737]བ་ནས་བརྩམས་ནས་ཡང་དག་པར་སྦྱིན་པའི་ཆོས་དག་ཡོད་བཞིན་དུ་ཞེས་བྱ་བ་དང་། ཤེས་རབ་ཅན་གྱི་སྦྱིན་པ་ཡིན་པར་རིག་པར་བྱ་ཞེས་བྱ༌[^738]བའི་བར་དུའོ། །

[Block 983]
མེད་ཅིང་མི་བདོག་ཅེས་བྱ་བ་ནི་སྦྱིན་པར་བྱ་བའི་ཆོས་མེད་ཅིང་མི་བདོག་ནའོ། །

[Block 984]
བསམ་པ་དག་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ནས་ཚེ་རབས་ཐམས་ཅད་དུ་ལོངས་སྤྱོད་ཟད་མི་ཤེས་པ་ཐོབ་ཅེས་བྱ་བ་དང་། དེ་བཞིན་དུ་དེས་ཆོས་ཀྱི་སྦྱིན་པ་ཉེ་བར་སྦྱིན་པར་བྱེད་པ་ན་མུ་སྟེགས་ཅན་གླགས་ཚོལ་བ་ལ་མི་སྦྱིན་ཞེས་བྱ་བ་ནས་བརྩམས་ནས་ཆོས་ཀྱི་སྦྱིན་པ་ལས་བརྩམས་ནས་ཤེས་རབ་དང་ལྡན་པའི་སྦྱིན་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བའི་བར་དང་། སོ་སོ་ཡང་དག་པར༌[^739]རིག་པ་ལ་བརྟེན་པ་དང་། ཐམས་ཅད་སྦྱིན་པའི་ཆོས་དང་། ཟང་ཟིང་དང་མི་འཇིགས་པ་ལས་བརྩམས་ནས་རབ་ཏུ་དབྱེ་བ་ཡང་ཅི་ལྟ་བ་བཞིན་དུ༌[^740]རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བའི་བར་དུ་སྟེ། ལྷག་པའི་བསམ་པ་ལ་བརྟེན་པ་ཞེས་བྱ་བ་ནི་གནོད་པ་བྱེད་པའི་སེམས་ཅན་ལ་ཞེས་བྱ་བ་ནས་བརྩམས༌[^741]ནས་གྲོགས་བཤེས་རྣམས་ཀྱི་བར་ལ་བཏང་སྙོམས་ཀྱི་བསམ་པ་བྱེད་པའོ། །

[Block 985]
སྦྱིན་པ་ལ་ཉེ་བར་བརྟེན་པ་ནི་སྦྱིན་པའི་གེགས༌[^742]ཡོད་ན་ཡང་ངོ་། །སྦྱིན་པ་ལ་གེགས༌[^743]བྱེད་པའི་གཉེན་པོ་ལས་ཀྱང་བརྩམས་ནས་གཉེན་པོའི་ཤེས་པ་ཐ་མ་འདིས་ནི་བསོད་ནམས་ཀྱི་འབྲས་བུ་ཡང་དག་པར༌[^744]ཡོངས་སུ་འཛིན་པར་བྱེད་དོ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 986]
ལྷག་པའི་བསམ་པས་མོས་པའི་སྦྱིན་པ་ལ་བརྟེན་པ་ཞེས་བྱ་བ་ནི་ནང་གི་བདག་ཉིད་དོ། །

[Block 987]
དབེན་བར་སོང་ཞེས་བྱ་བ་འདི་ལས་བརྩམས་ནས་འདི་ནི་བྱང་ཆུབ་སེམས་དཔའ༌[^745]ཤེས་རབ་ཆེན་པོ་དང་ལྡན་པ་སྦྱིན་པ་ལ་བརྟེན་པ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 988]
དཀའ་བའི་སྦྱིན་པ་ནི་མདོར༌[^746]བསྡུ་ན་རྒྱུ་གསུམ་གྱིས་ཏེ། དགའ་བའི་སྦྱིན་པ་ཉིད་དང་། བདག་ལ་ཆགས་པས་སམ། སྦྱིན་པའི་རྫས་ལ་མངོན་པར་ཆགས་པས་སམ། སྔར་སྐྱེ་བ་གཞན་དུ་སྦྱིན་པ་ལ་གོམས་པར་མ་བྱས་པའོ། །

[Block 989]
དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་བདག་ཉིད་ལ་གནོད་པ་བྱས་ཏེ་ཞེས་བྱ་བ་ནི་སྦྱིན་པར་བྱ་བའི་རྫས་ཆུང་ངུ་ལས་ཀྱང་བགོ་བཤའ་བྱས་ནས་སྦྱིན་པར་བྱེད་པ་སྟེ། དེ་ལྟ་བུར་བདག་ཉིད་གོམས་པར་བྱེད༌[^747]པའོ། །

[Block 990]
སྡུག་བསྔལ་དང་དུ་བླངས་ནས་ཞེས་བྱ་བ་ནི་གལ་ཏེ་སྦྱིན་པར་བྱ་བའི་རྫས་ཆུང་ན༌[^748]ཡང་ཐམས་ཅད་སྦྱིན་པར་བྱེད་པ་སྟེ། དེ་ལྟར་བདག་ཉིད་ཀྱིས་སྡུག་བསྔལ་དང་དུ་བླངས་པར་གྱུར་པའོ། །

[Block 991]
སྡུག་པའི་དངོས་པོ་ཞེས་བྱ་བ་ལ། རྒྱུ་གསུམ་གྱིས་སྦྱིན་པར་བྱ་བའི་དངོས་པོ་སེམས་ཅན་དུ་གྲགས་པ་སྡུག་པར་གྱུར་པ་ཡིན་ཏེ། སྐྱེ་བ་གཞན་དུ་བརྩེ་བར་བྱས་པའམ། མཐོང་བའི་ཆོས་ལ་ཡུན་རིང་དུ་ཡང་དག་པར་འདྲིས་པའམ། དེ་དག་མེད་ན་ཡང་ཤས་ཆེར་ཕན་པ་བྱས་པ་ཉིད་དོ། །

[Block 992]
སེམས་ཅན་མ་ཡིན་པའི་དངོས་པོའི༌[^749]མཆོག་ཡིན་པའི་ཕྱིར་འཛིན་པ་དམ་པོ་འབྱུང་བར་འགྱུར་བའོ། །ཇི་ལྟར་ན་མཆོག་ཡིན་ཞེ་ན། སྨྲས་པ། སྐྱོན་མེད་པའི་ཕྱིར་དང་། རབ་མཆོག་ཉིད་ཀྱི་ཕྱིར་ཏེ། དངོས་པོ་རྣམ་པ་དེ་གཉི་ག་ལ་མངོན་པར་ཞེན་པ་བསལ་ནས༌[^750]སྦྱིན་པར་བྱེད་དོ། །

[Block 993]
ཆགས༌[^751]ཆེན་པོས་བསྒྲུབས་པ་ཞེས་བྱ་བ་ནི་སྔོན་སྦྱིན་པ་ལ་གོམས་པར་མ་བྱས་པས་ཚེགས་ཆེན་པོས་བསྒྲུབས་པའི་ཕྱིར་རོ། །

[Block 994]
ཐམས་ཅད་ཀྱི་སྒོ་ནས་སྦྱིན་པའི་བསྡུས་པའི་དོན་ནི་རྣམ་པ་བཞི་སྟེ། སྦྱིན་པ་གང་ཡིན་པ་དང་། གང་ལ་སྦྱིན་པ་དང་། གང་དུ་གང་གིས་སྦྱིན་པར་བྱེད་པ་སྟེ༌[^752]རང་གི་འམ་གཞན་གྱི་ལ༌[^753]གསོལ་བ་བཏབ་ནས་བསྐུལ་བའོ། །

[Block 995]
དེ་ལ་རང་གི་ལ་ཇི་ལྟར་ཞེ་ན། གང་གིས་ཇི་ལྟར་གཞན་གྱི༌[^754]བསྐུལ་བ་མེད་པར་ཆོས་དང་མཐུན་པར་རྙེད་པའོ། །

[Block 996]
ཕ་དང་མ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་འབྲེལ་པ་དང་། ཕན་པ༌[^755]བྱེད་པར་འདོད་པ་དེ་དག་ལའོ། །

[Block 997]
སྐྱེས་བུ་དམ་པའི་སྦྱིན་པ་རྣམ་པ་ལྔའི་བསྡུས་པའི་དོན་ནི་གཏོང་བ་ཉིད་ཕུན་སུམ་ཚོགས་པ་དང་། སྒྲུབ་པ་པོ་ཕུན་སུམ་ཚོགས་པ་དང་། སྦྱིན་པའི་རྫས་ཕུན་སུམ་ཚོགས་པར་གསུངས་ཏེ། དད་པ་ཞེས་བྱ་བ་ནི་ཟང་ཟིང་མེད་པའི་སེམས་ཉིད་དེ། གཏོང་བ་ཉིད༌[^756]ཕུན་སུམ་ཚོགས་པའོ། །

[Block 998]
ཡོངས་སུ་གཏོང་བ་པོ་ནི་རྒྱུ་ཕུན་སུམ་ཚོགས་པར་འགྱུར་ཏེ། འདི་ལྟར་ཡོངས་སུ་གཏོང་བ་ནི༌[^757]ལེན་པ་པོ་ལ་བཀུར་སྟི་བྱས་ནས་འདི་ལྟར་ཡིད་ཀྱིས་དགའ་བ་སྐྱེས་པར་བྱེད་པའོ། །

[Block 999]
རང་གི་ལག་པ་ཞེས་བྱ་བ་ནི་དེ་ལྟ་བུར་ཡོངས་སུ་བཏང༌[^758]བ་ནི༌[^759]བདག་མི་ཁེངས་པར་སྦྱིན་པའོ། །

[Block 1000]
དུས་སུ་ཡོངས་སུ་གཏོང་བ་ནི་འདོད་པའི་དངོས་པོས༌[^760]ཡོངས་སུ་འཛིན་པའོ། །

[Block 1001]
གཞན་ལ་མི་གནོད་པར་ཞེས་བྱ་བ་འདིས་ནི་ལྷག་པའི་རྫས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ལུང་ལས་དག་པར་བསྟན་པ་དག་གོ། །

[Block 1002]
རྣམ་པ་ཐམས་ཅད་ཀྱི་སྦྱིན་པའི་བསྡུས་པའི་དོན་ནི་མི་བརྟེན་པར་སྦྱིན་པ་ལ་སོགས་པས༌[^761]ནི་མདོའི་དུམ་བུའི་དོན་བཤད་པ་ཡིན་ཏེ། གྲོལ་བར་གཏོང་བ་དང་། རབ་ཏུ་ལག་བརྐྱང་བ་དང་། ལྷག་པར་མཐོང་བ༌[^762]ལ་དགའ་བ་དང་། ལྷག་པར་མཆོད་སྦྱིན༌[^763]ལ་དགའ་བ་དང་། གཏོང་བ་ཕུན་སུམ་ཚོགས་པ་དང་། བགོ་བཤའ་བྱེད་པ་ལ་དགའ་བ་ཞེས་བྱ་བ་སྟེ། མི་བརྟེན་པར་སྦྱིན་པ་ལ་སོགས་པ་རྣམ་པར་སྨིན་པ་ལ་མི་རེ་བ་རྣམས་དང་གོ་རིམ་བཞིན་དུ་སྦྱར་བར་ཤེས་པར་བྱའོ། །

[Block 1003]
གཏོང་བ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་ནི་སྣོད་ལ་སྦྱིན་པའོ། །

[Block 1004]
བགོ་བཤའ་བྱེད་པ་ཞེས་བྱ་བ་ནི་སྣོད་མ་ཡིན་པ་ལ་སྦྱིན་པ་སྟེ། འདི་དག་གིས་ནི་རྣམ་པ་གང་གིས་སྦྱིན་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་པའི་སྦྱིན་བདག་གི་ཡོན་ཏན་རྣམས་བསྟན་པ་ཡིན་ནོ། །

[Block 1005]
ད་ནི་རྣམ་པ་ཐམས་ཅད་ཀྱི་སྦྱིན་པ་ཕུན་སུམ་ཚོགས་པར་འགྱུར་བའི་དབང་དུ་བྱས་པ་ནི་ཀུན་ལ་སྦྱིན་པ་ལ་སོགས་པ་སྦྱིན་པ་བཞི་ནི་ཐམས་ཅད་སྦྱིན་པ་ཉིད་ཀྱི་བྱེ་བྲག་གོ། །

[Block 1006]
ཕོངས་ཤིང་འདོད་པ་ལ་སྦྱིན་པ་ཞེས་བྱ་བ་ལ། དོན་གྱིས་ཕོངས་པ༌[^764]ནི་ཕོངས༌[^765]པའོ། །

[Block 1007]
གང་ལ་དོན་གྱིས་ཕོངས་པ༌[^766]ཡོད་པ་དེ་ནི་ཕོངས༌[^767]ཤིང་འདོད་པ་སྟེ། ཕོངས་ཤིང་འདོད་པ་ཉིད་ནི༌[^768]ཕོངས་ཤིང་འདོད་པའོ། །

[Block 1008]
དེ་ལ་སྦྱིན་པ་ནི་ཕོངས་ཤིང་འདོད་པ་ལ་སྦྱིན་པའོ། །གང་གིས་ཕོངས་ཤིང་འདོད་ཅེ་ན། ཟས་ལ་སོགས་པས་ཏེ། རྣམ་པ་བརྒྱད་ཀྱིས་ཕོངས་ཤིང་འདོད་པ་ལ་སྦྱིན་པ་ནི་མདོར་བསྡུས་པའི་དོན་བསྟན་པ་ཡིན་ནོ། །

[Block 1009]
ལུས་སྐྱེས་པ་རྣམས་ནི་འདི་དག་ཉིད་འདོད་པ་ཡིན་གྱི། འཇིག་རྟེན་པ་རྣམས་དེ་ལས་གཞན་པ༌[^769]ནི་མི་འདོད་པས་ལུས་ལ་ལྟོས་ནས་རྣམ་པ་ལྔ་སྟེ། ལྷན་ཅིག་སྐྱེས་པའི་སྡུག་བསྔལ་བཟློག་པར་འདོད་པ་དང་། ལུས་ལ་ཕན་པ་འདུ་བྱེད་པའི་ཡོ་བྱད་འདོད་པ་དང་། སྤྱོད་ལམ་གྱི་སྡུག་བསྔལ་མི་འབྱུང་བར་འདོད་པ་དང་། ལུས་ལ་ཕན་པ་བྱེད་པའི་ཡོ་བྱད་འདོད་པ་དང་། ལུས་ལ་གནོད་པ་སྐྱོབ་པར་བྱེད་པ་འདོད་པ་ཞེས་བྱ་བ་སྟེ། དེ་ལ་ལྷན་ཅིག་སྐྱེས་པའི་སྡུག་བསྔལ་བཟློག་པར༌[^770]བྱེད་པ་ལ༌[^771]ཕན་པ་འདོད་པ་དེ་དག་ཟས་དང་སྐོམ་གྱིས་ཕོངས་ཤིང་འདོད་པར་གྱུར་པ་ལ་ཟས་དང་སྐོམ་ལ་སོགས་པ་སྦྱིན་པར་བྱེད་དོ། །

[Block 1010]
ལུས་ཀྱིས་འགྲོ་བའི་སྡུག་བསྔལ་བསལ་བར་འདོད་པའི་དོན་དུ་བཞོན་པ༌[^772]སྦྱིན་པ་སྦྱིན་པར་བྱེད་དོ། །

[Block 1011]
ལུས་ལ་ཕན་པ་བྱེད་པའི་ཡོ་བྱད་ཀྱང༌[^773]རྣམ་པ་བཞི་སྟེ། གསང་བའི་གནས་དགབ་པའི་ཡོ་བྱད་དང་། རྒྱུན་དུ་བྱ་བའི་ཡོ་བྱད་དང་། ཟས་ལ་ཉེ་བར་སྤྱད་པ་ལ་སོགས་པ་སྣ་ཚོགས་ཀྱི་སྣོད་སྤྱད་དང་། མལ་སྟན་ལ་སོགས་པ་ཡོ་བྱད་རྣམ་པ་སྣ་ཚོགས་དང་། དྲི་དང་ཕྲེང་བ་དང་བསྐུ་བ་དང་བྱུག་པའི་ཡོ་བྱད་ཅེས་བྱ་བའོ། །

[Block 1012]
དེ་འདོད་པ་རྣམས་དེ་དག་མ་ཐོབ་པས་ཉོན་མོངས་པར་གྱུར་པ་དེ་རྣམས་ལ་ཡོ་བྱད་དེ་དག་སྦྱིན་པར་བྱེད་དེ། གྲང་བ་དང་། དྲོ་བ་དང་། རླུང་དང་། ཚ་བ་དང་། ཆར་འབབ་པའི་སྡུག་བསྔལ་ཡོངས་སུ་སྤང་བར་འདོད་པ་དང་། མིག་གིས་མཐོང་བར་འདོད་པ༌[^774]སྡུག་བསྔལ་གྱི་གནོད་པ་མི་མཉམ་པ་དག་ཉེ་བར་བསལ་བར་འདོད་པ་དེ་དག་ལ་རྟེན༌[^775]དང་སྣང་བ་དག་སྦྱིན་པར་བྱེད་དོ། །

[Block 1013]
གང་དག་མིག་གིས་མཐོང་བར༌[^776]བྱས་ནས་གནོད་པ་ཡོངས་སུ་སྤང་བར་འདོད་པ་རྣམས་སྣང་བ་མེད་པས་གནོད་པར་གྱུར་པ་དག་ལ་སྣང་བ་སྦྱིན་པར་བྱེད་དེ། [^777]ཐོས་པ་ལ་སོགས་པས༌[^778]གཞན་གྱིས་མཐོན་དམན༌[^779]ལ་སོགས་པ་སྤོང་བ་ལ་ཇི་ལྟར་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སྣང་བས་བྱེད་པ་ལྟར། རྣམ་པར་ཤེས་པ་དེ་དག་འབྱུང་བ་ལ་ལྷན་ཅིག་བྱེད་པའི་རྒྱུ་གཞན་ནི་མེད་དོ། །

[Block 1014]
དེ་ལྟ་བས་ན་སྣང་བ་ཞེས་སྨོས་པས་ནི་མཐོན་དམན༌[^780]ལ་སོགས་པའི་གནོད་པས་ལུས་ལ་གནོད་པ་སྤོང་བ་ཡིན་ནོ། །

[Block 1015]
ཀུན་དུ་འཛིན་པ་ཡོངས་སུ་བཏང་ཞེས་བྱ༌[^781]བ་ནི། [^782]སེམས་ཀྱིས་འཛིན་པ་གང་གིས་སེམས་ཀུན་དུ་བཟུང་བར༌[^783]གྱུར་པ་སྟེ། དེ་ལྟར་བྱས་ནས་སེམས་ཀྱི་ཀུན་དུ་འཛིན་པ་ཞེས་བྱའོ། །

[Block 1016]
སེར་སྣ་དང་གསོག་འཇོག་གི་དྲི་མ་བསལ་ནས་བཟང་པོ་དང་གཙང་མ་དང་། རུང་བ་ཞེས་བྱ་བ་འདི་དག་གི་བསྡུས་པའི་དོན་ནི་གང་སྦྱིན་པ་དང་། ཇི་ལྟར་སྦྱིན་པའོ། །

[Block 1017]
གང་སྦྱིན་ཞེ་ན། བཟང་པོ་དང་། གཙང་མ་དང་། རུང་བའོ། །ཇི་ལྟར་ཞེ་ན། བཟང་པོས་ལུས་ཚིམ་པར་བྱེད་ཅིང་། གཙང་བ་དང་། རུང་བས་སེམས་འཛིན་པར་བྱེད་དོ། །

[Block 1018]
སེར་སྣའི་དྲི་མ་བསལ་བས་ནི་སྦྱིན་བདག་གིས་འདི་དང་གཞན་དུ་རྣམ་པར་སྨིན་པ་ལ༌[^784]ལོངས་སྤྱོད་ཆེན་པོ་འཐོབ༌[^785]བོ། །

[Block 1019]
གསོག་འཇོག་གི་དྲི་མ་བསལ་བས་ནི་འདི་དང་གཞན་དུ་ལོངས་སྤྱོད་རྣམས་ལ་འཛིན་པ་མེད་པར་གྱུར༌[^786]ཏེ། རྒྱུ་མཐུན་པའི་འབྲས་བུའོ། །

[Block 1020]
དེ་ལ་ཟང་ཟིང་དང་མི་འཇིགས་པའི་སྦྱིན་པ་རབ་ཏུ་དབྱེ་བ་དང་བཅས་པ༌[^787]ཞེས་བྱ་བ་ལ། ཟང་ཟིང་གི༌[^788]སྦྱིན་པ་ཉིད་ནི་འདིར་དབྱེ་བ་དང་བསླབ་པ༌[^789]ཡིན་གྱི། མི་འཇིགས་པའི་སྦྱིན་པ་ལ་ནི་འདིར་དབྱེ་བ་མེད་དོ། །
--- END BLOCKS ---
