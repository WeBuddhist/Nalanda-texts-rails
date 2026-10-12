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
[Block 1016]
གཞི་གང་ཞེ་ན་ཡུལ་གྱི་དངོས་པོ་ཉིད་དོ། །

[Block 1017]
སོ་སོར་རྟོག་པ་གང་ཞེ་ན་རིགས་པ༌[^487]དང་མི་རིགས་པ་གང་དུ་འཚོལ་བ༌[^488]དང་འདས་པ་སྟེ་སྤྱོད་པ་ཉིད་དོ། །

[Block 1018]
ངོ་ཚ་ཤེས་པ་གང་ཞེ་ན་བདག་གམ་ཆོས་ཀྱི་དབང་དུ་བྱས་ཏེ་ཁ་ན་མ་ཐོ་བ༌[^489]འཛེམ་པའོ། །

[Block 1019]
སྙིང་རྗེ་གང་ཞེ་ན་གང་ཞིག་གང་གིས༌[^490]རྣམ་པ་དང་བྲལ་བར་འདོད་པའོ། །

[Block 1020]
བརྩེ་བ་གང་ཞེ་ན་གང་ཞིག་གང་དང་བྲལ་ནས་དེ་དང་ཕྲད་པར་འདོད་པའོ། །

[Block 1021]
དོགས་པ་དང་བཅས་པ་གང་ཞེ་ན། སེམས་ངེས་པར་མི་གནས་པའོ། །

[Block 1022]
སྡུད་པ་གང་ཞེ་ན་གཞན་གྱི་གང་དག་ཡོངས་སུ་སྡུད་པའོ། །

[Block 1023]
སེར་སྣ་གང་ཞེ་ན་རང་གི་ཡིད་དུ་འོང་བ་བློས་ཡོངས་སུ་འཛིན་པའོ། །

[Block 1024]
རང་བཞིན་འདི་དག་སྣང་བ་ལས་འབྱུང་སྟེ་སེམས་ཅན་ཐམས་ཅད་གང་དུ་ཇི་ལྟར་གནས་པའི་རྩ་བར་བསྟན་པའོ། །

[Block 1025]
འདི་དག་ཡོངས་སུ་ཤེས་པས་ཀྱང་གང་ཞིག་ཡོངས་སུ་འདྲེ་བ་མེད་པའི་བསམ་གཏན་ཡོངས་སུ༌[^491]རྫོགས་པར་འགྱུར་བར་དགོངས་སོ། །

[Block 1026]
དེ་ནས་སྣང་བ་མཆེད་པ་བསྟན་པར་བྱ་སྟེ། དེ་ལ་སྣང་བ་མཆེད་པའི་མཚན་ཉིད་གང་ཞེ་ན། འོད་མ་འགྲེང་བ་ལྟར་མཛེས་ཤིང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ་འོད་མ་འགྲེང་བ་ནི་འོད་མ་འགྲེང་བ་སྟེ། གང་ལ་འོད་མ་འགྲེང་བ་དང་འདྲ་བའི་ཆོས་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1027]
ཆགས་ལ་སོགས་པ་རབ་བསྐྱེད་ལྡན། །ཞེས་པ་ནི་ཆགས་པ་ལ་སོགས་པ་བསྐྱེད་པ༌[^492]སྟེ་གང་ལ་གང་ཞིག་འབྱུང་བར་འགྱུར་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1028]
འདི་ལྟ་སྟེ་ཆགས་པ་དང་། ཆགས་པ་བར་མ་དང་། ཀུན་དུ་ཆགས་པ་དང་། དགའ་བ་དང་། དགའ་བ་བར་མ་དང་། ཀུན་དུ་དགའ་བ་དང་། རངས་པ་དང་། རངས་པ་བར་མ་དང་། ཀུན་དུ་རངས་པ་དང་། ངོ་མཚར་དང་དགོད་པ་དང་། ཚིམ་པ་དང་། འཁྱུད་པ་དང་། འོ་བྱེད་པ་དང་། འཛིན་པ༌[^493]དང་། བརྟན་པ་དང་། བརྩོན་པ་དང་། ཁེངས་པ་དང་། བྱ་བ་དང་། དབྲོག་པ་དང་། སྟོབས་དང་། སྤྲོ་བ་དང་། དགའ་བ་ལ་སྦྱོར་བ་དང་། དགའ་བ་ལ་སྦྱོར་བ༌[^494]བར་མ་དང་། ཤིན་ཏུ་དགའ་བ་ལ་སྦྱོར་བ་དང་། དྲག་པ་དང་། རྣམ་པར་སྒེག་པ་དང་། འགྲས་པ་དང་། དགེ་བ་དང་། ཚིག༌[^495]གསལ་བ་དང་། བདེན་པ་དང་། མི་བདེན་པ་དང་། ངེས་པ་དང་། ཉེ་བར་མི་ལེན་པ་དང་། སྦྱིན་པ་པོ་དང་། སྐུལ་བ་དང་། དཔའ་བ་དང་། ངོ་ཚ་མེད་པ་དང་། ཟིན་པ་དང་། གདུག་པ་དང་། མི་སྲུན་པ་དང་། གྱ་གྱུ་ཆེ་བ་སྟེ་མཚན་ཉིད་བཞི་བཅུ་པོ་འདི་དག་ནི་སྣང་བ་མཆེད་པའི་རང་བཞིན་ནོ། །

[Block 1029]
འདི་དག་གིས་བསྐྱེད་པ་དང་གང་གིས་ཡོངས་སུ་གནོན་པ་འདི་ནི་སྣང་བ་མཆེད་པ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 1030]
དེ་ལ་འདོད་པ་ལ་ཆགས་པ་གང་ཞེ་ན། མ་ཐོབ་པའི་ཡུལ་ལ་ཡིད་ཀུན་དུ་ཆགས་པའོ། །

[Block 1031]
ཆགས་པ་གང་ཞེ་ན། མ་བསྐལ་པའི་ཡུལ་ལ་ཡིད་ཀུན་དུ་ཆགས་པའོ། །

[Block 1032]
དགའ་བ་གང་ཞེ་ན། ཡིད་དུ་འོང་བའི་རྣམ་པས་སེམས་ཁེངས་པའོ། །

[Block 1033]
རངས་པ་གང་ཞེ་ན། གང་དགའ་བས་ཆེས་དགའ་བའོ། །

[Block 1034]
མགུ་བ་གང་ཞེ་ན། ཐོབ་པའི་བྱེ་བྲག་ལ་ལྟོས༌[^496]ནས་བདག་པོ་ལ་ཡོངས་སུ་བསྟོད་པའོ། །

[Block 1035]
ངོ་མཚར་གང་ཞེ་ན། མི་སྤྱོད་པ་ལ་མངོན་དུ་བྱས་པས་ཡ་མཚན་དུ་གྱུར་པའོ། །

[Block 1036]
དགོད་པ་གང་ཞེ་ན། གང་གིས་གང་ཞིག་ལ་གནས་པར་མི་བྱེད་ཅིང་སེམས་གཞན་དུ་འཕྲོ་བའོ། །

[Block 1037]
ཚིམ་པ་ནི་ཚོར་བ་བདེ་བ་གཞན་དུ་བསྟན་ནས་སོ། །

[Block 1038]
འཁྱུད་པ་ནི་ཡིད་དུ་འོང་བའི་ཡུལ་ལ་སེམས་ཀྱིས་ཀུན་དུ་ཞེན་པའོ། །

[Block 1039]
གཞན་ནི་གོ་སླའོ། །

[Block 1040]
བརྟན་པ་གང་ཞེ་ན་ངེས་པ་རྙེད་དེ་མི་གཡོ་བའོ། །

[Block 1041]
བརྩོན་འགྲུས་གང་ཞེ་ན་ལེ་ལོ་དང་བྲལ་བའོ། །

[Block 1042]
ང་རྒྱལ་གང་ཞེ་ན། མཐོ་བར་སེམས་པའོ། །

[Block 1043]
བྱ་བ་གང་ཞེ་ན་གང་ཞིག་ཡོངས་སུ་འགྲུབ་པར་བྱའོ། །

[Block 1044]
དབྲོག་པ་གང་ཞེ་ན་གཞན་གྱིས་བདག་གིར་བྱས་པ་ལེན་པའོ། །

[Block 1045]
སྟོབས་གང་ཞེ་ན། གྱད་དང་གཡུལ་འགྱེད་པའོ། །

[Block 1046]
སྤྲོ་བ་གང་ཞེ་ན་དགའ་བ་འབའ་ཞིག་ཡུལ་དུ་བྱས་ནས་བརྩོན་འགྲུས་དྲག་པོ་དང་ལྡན་པ་སྟེ། གོ་ཆ་ལ་སོགས་པ་ཡོངས་སུ་རྫོགས་པའི་སེམས་པ་འབྲས་བུ་དང་བཅས་པའོ། །

[Block 1047]
དགའ་བ་ལ་སྦྱོར་བ་གང་ཞེ་ན། དྲེགས་པ་ལས་བྱུང་བའི་སེམས་པས་མི་དགེ་བ་ལ་སོགས་པ་ལ་སྦྱོར་བའི་སེམས་པ་འབྲས་བུ་དང་བཅས་པའོ། །

[Block 1048]
ཞེ་འགྲས༌[^497]པ་གང་ཞེ་ན། རྩོད་པའི་རྒྱུ༌[^498]མེད་པར་འདོད་པའི་དབང་གིས་དམ་པ་དང་དམ་པ་མཆོག་དང་། དམན་པ་ལ་སོགས་པ་ལ་ཀུན་དུ་རྩོད་པར་སེམས་པའོ། །

[Block 1049]
སྒེག་པ་གང་ཞེ་ན། གང་གིས་འདོད་ཆགས་ཀྱི་ཡུལ་ལམ་ཞེ་སྡང་གི་ཡུལ་ཐོབ༌[^499]པར་བྱ་བ་དང་ཕྲད་པར་བྱ་བ་དང་། ཀུན་དུ་ཉམས་པར་བྱ་བའི་ཕྱིར་ཚུལ་འཆོས་པའོ། །

[Block 1050]
ཞེ་འགྲས་པ་གང་ཞེ་ན་གང་གིས་གང་ཞིག་དང་རྩོད་པ་སྔོན་དུ་སོང་བའམ། ཕྱིས་འབྱུང་བའི་བསམ་པ་དང་བཅས་ཏེ་སེམས་ཤིང་སེམས༌[^500]ལ་མདུད་པར་འཛིན་པས་འཁོན་དུ་འཛིན༌[^501]པ་ཉིད་དོ། །

[Block 1051]
དགེ་བ་གང་ཞེ་ན་མ་ཆགས་པ་དང་སྙིང་རྗེ་ལ་སོགས་པ་དང་མཚུངས་པའི་སེམས་ཀྱིས་བསླང་བའི་ལུས་དང༌[^502]ངག་གི་ལས་ཏེ་གང༌[^503]ཉེས་པ་གང་ཞིག་དང་བྲལ་བར་འགྱུར་རོ། །

[Block 1052]
ཚིག་གསལ་བ་གང་ཞེ་ན། ལྕེ་ལ་ཉེས་པ་མེད་ཅིང་ལུས་ཡོངས་སུ་དར་བས་ཆེད་དུ་སྨྲས་པའོ། །

[Block 1053]
བདེན་པ་གང་ཞེ་ན་དངོས་པོ་དང་མཐུན་པའི་ཚིག་ཏུ་བརྗོད་པའོ། །

[Block 1054]
མི་བདེན་པ་གང་ཞེ་ན། དངོས་པོ་དང་མི་མཐུན་པར་སྨྲ་བའོ། །

[Block 1055]
ངེས་པ་གང་ཞེ་ན་སོམ་ཉི་རྣམ་པར་སྤངས་པའི་སེམས་པ་དང༌[^504]དེའི་ལས་སོ། །
--- END BLOCKS ---
