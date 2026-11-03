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
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེས་པ་ནས་ཐེག་པ་གཅིག་ལས༌[^1030]བརྩམས་ཏེ་ཆོས་བཤད་པ་དེ་ཡང་ཐམས་ཅད་མཁྱེན་པའི་མཐའི་བར་དུ་ཞེས་པ་ནི་དུས་གསུམ་གྱི་སངས་རྒྱས་ཀྱི་ཆོས་ལུགས་བསྟན་པ་སྟེ་འདི་ལ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 1017 [HEADING]]
###### **འདས་པ།** ^4-2-10-1-4-2-1-0

[Block 1018]
སྔར་དུས་གསུམ་གྱི་ཆོས་སོ་སོར་བསྟན་པ་ཐམས་ཅད་དང་མཐུན་པ་སྟེ་སྔ་མ་ལ༌[^1031]ཡང་རྣམ་པ་གསུམ་སྟེ། འདས་པ་དང་མ་འོངས་པ་དང་ད་ལྟར་དང་གསུམ་མོ། །

[Block 1019 [HEADING]]
###### **ཆོས་ལུགས་མཐུན་པ།** ^4-2-10-1-4-2-1-1-0

[Block 1020]
གསུམ་པོ༌[^1032]ལ་ཡང་གཉིས་གཉིས་ཏེ། སངས་རྒྱས་ཀྱི་ཆོས་བསྟན་པའི་ཆོས་ལུགས་མཐུན་པ་དང་། སེམས་ཅན་གྱི་དོན་བྱས་པའི་འབྲས་བུ༌[^1033]མཐུན་པ་སྟེ། འདི་ནི་འདས་པའི་སངས་རྒྱས་ཀྱི་ཆོས་ལུགས་དང་མཐུན་པར་བསྟན་པའོ། །

[Block 1021]
སྔར་རྒྱུ༌[^1034]རྐྱེན་རྣམ་པ་མང་པོས་ཐབས་སུ་བསྟན་པ་ནི་ཕྱིས་སངས་རྒྱས་ཀྱི་ཐེག་པ་གཅིག་ཐོབ་པར་བྱ་བའི་ཕྱིར་བསྟན་ཏོ། །

[Block 1022]
འགྲེལ་པ་ལས༌[^1035]ཐབས་ནི་སྦྱོར་བ་སྟེ་ཐེག་པ་ཆུང་ངུའི་ཕུང་པོ་དང་ཁམས་དང་། སྐྱེ་མཆེད་ལ་རྟོག་ཅིང་སྡུག་བསྔལ་ལས་སྐྱོ་བ་དང་སྡུག་བསྔལ་སྤང་བ་དང་། རྣམ་པར་གྲོལ་བ་ཐོབ་པར་བྱེད་པ་ཐེག་པ་ཆེན་པོའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་དང་། བསྡུ་བ་རྣམ་བཞིས་བདག་དང་གཞན་གྱི་དོན་བྱེད་པ་གཉེན་པོའི་ཆོས་རྣམས་སོ། །

[Block 1023]
རྒྱུ་ཞེས་བྱ་བ་ནི་འགྲེལ་པ་ལས་སྔར་དོན་དྲུག་སྨོས་པ་ལས་གཉིས་པའི་ནང་ནས་བཤད་པ་བཞིན་ནོ། །

[Block 1024]
སྔར་རྒྱུ་དང་རྐྱེན་རྣམ་པ་སྣ་ཚོགས་ཞེས་སྨོས་པ་ནི་ཐེག་པ་གསུམ་ཡང་ཚིག་དང་མིང་དུ་བཏགས་པ་ཙམ་དུ་ཟད་དེ་ཡང་དག་པའི་དོན་ཡོད་པ་མ་ཡིན་ལ། ཡང་དག་པའི་དོན་ལ་བཤད་དུ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1025]
དཔེ་ཞེས་བྱ་བ་ནི་དཔེར་ན་བ་ལ་འོ་མ་དང་ཞོ་དང་མར་དང་ཞུན་མར་དང་མར་གྱི་སྙིང་པོ་ཡོད་པ་དང་འདྲ་སྟེ། དེ་ལ་ཐེག་པ་ཆུང་ངུ་ནི་འོ་མ་ལྟ་བུ་ཡིན་ནོ། །

[Block 1026]
ཐེག་པ་ཆེན་པོ་ནི་མར་གྱི་སྙིང་པོ་ལྟ་བུ་ཡིན་ནོ། །

[Block 1027]
དཔེ་འདིས་ན་ཐེག་པ་ཆེན་པོ་བླ་ན་མེད་པ་བསྟན་ཏེ། ཉན་ཐོས་ལ་སོགས་པ་ཡང་ཐེག་པ་ཆེན་པོ༌[^1036]བླ་ན་མེད་པ་དང་མཐུན་པར་བསྟན་ཏོ། །

[Block 1028]
ཉན་ཐོས་དང་མཐུན་པ་བསྟན་པ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི༌[^1037]ཆོས་ཀྱི་སྐུ་ཉིད་སེམས་ཅན་དང་རང་སངས་རྒྱས་ལ་སོགས་པར་ཆོས་ཀྱི་སྐུར་མཉམ་ཞིང་ཁྱད་པར་མེད་པར་བསྟན་པ་སྟེ། དཔེ་འདི་དང་སྦྱར་ན་སེམས་ཅན་ནི་བ་ལྟ་བུ་ཉན་ཐོས་ནི་འོ་མ་ལྟ་བུ། རང་སངས་རྒྱས་ནི་ཞོ་ལྟ་བུ། བྱང་ཆུབ་སེམས་དཔའ་ནི་མར་ལྟ་བུ། བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་ནི་ཞུན༌[^1038]མར་ལྟ་བུ། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ནི་མར་གྱི་སྙིང་པོ་ལྟ་བུ་སྟེ། མར་གྱི་སྙིང་པོ་མཆོག་དམ་པ་ཡིན་པ་ལྟར་སངས་རྒྱས་ཀྱི་ཐེག་པ་གཅིག་ཀྱང་དེ་དང་འདྲ་སྟེ། བའི་འོ་མ་གཅིག་ལས་མར་གྱི་སྙིང་པོའི་བར་དུ་འགྱུར་བའི་ཕྱིར་སེམས་ཅན་ལས་སངས་རྒྱས་ཀྱི་བར་དུ་མཚན་མ་ཐ་དད་ཀྱང་རང་བཞིན་ནི་མཉམ་སྟེ་གཉིས་སུ་མེད་དོ། །

[Block 1029 [HEADING]]
###### **འབྲས་བུ་མཐུན་པ།** ^4-2-10-1-4-2-1-2-0

[Block 1030]
མདོ་ལས་དེ་ནི་སེམས་ཅན་རྣམས་ཞེས་པ་ནས་བྱང་ཆུབ་ཐོབ་པར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་འདས་པའི་སེམས་ཅན་གྱི་དོན་བྱས་པའི་འབྲས་བུ་མཐུན་པར་བསྟན་པ་སྟེ། སྔར་ཐེག་པ་གཉིས་ཀྱིས་དོན་བྱས་ནས་ཕྱིས་སངས་རྒྱས་སུ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་འཐོབ་པ་བསྟན་ཏེ། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ནི་སངས་རྒྱས་ཀྱི་ཡང་དག་པའི་ཡེ་ཤེས་སོ། །

[Block 1031]
རྣམ་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་སྟེ། ཡང་དག་པ་ནི་གླང་པོའི་ཤིང་རྟ་ལྟ་བུ།

[Block 1032 [HEADING]]
###### **མ་འོངས་པ།** ^4-2-10-1-4-2-2-0

[Block 1033 [HEADING]]
###### **ཆོས་ལུགས་མཐུན་པ།** ^4-2-10-1-4-2-2-1-0

[Block 1034]
མདོ་ལས་འདི་ལྟར་ཤཱ་རིའི་བུ་མ་འོངས་པའི་དུས་ཞེས་པ་ནས་ཐམས་ཅད་མཁྱེན་པའི་མཐའི་བར་དུ་ཞེས་པའི་བར་དུ་ནི་མ་འོངས་པའི༌[^1039]སངས་རྒྱས་རྣམས་ཀྱི་ཆོས་ལུགས་མཐུན་པ་བསྟན་ཏོ། །

[Block 1035 [HEADING]]
###### **འབྲས་བུ་མཐུན་པ།** ^4-2-10-1-4-2-2-2-0

[Block 1036]
མདོ་ལས་དེ་ནི་སེམས་ཅན་རྣམས་ཞེས་པ་ནས་བྱང་ཆུབ་ཐོབ་པར༌[^1040]འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་མ་འོངས་པའི་སེམས་ཅན་གདུལ་བར༌[^1041]འགྱུར་བའི་འབྲས་བུ་མཐུན་པར་བསྟན་པའོ། །

[Block 1037 [HEADING]]
###### **ད་ལྟར།** ^4-2-10-1-4-2-3-0

[Block 1038 [HEADING]]
###### **ཆོས་ལུགས་མཐུན་པ།** ^4-2-10-1-4-2-3-1-0

[Block 1039]
མདོ་ལས་ཤཱ་རིའི་བུ་ད་ལྟར་གྱི་དུས་ན་ཞེས་པ་ནས་ཐམས་ཅད་མཁྱེན་པའི་ཆོས་འཆད་དོ་ཞེས་པའི་བར་དུ་ནི་ད་ལྟར་གྱི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཆོས་ལུགས་མཐུན་པར་བསྟན་པ་སྟེ། དོན་དང་ཕན་པ་དང་བདེ་བ་ནི་བདེ་བར་བྱེད་པའི་དོན་ཏེ། བདེ་བ་ནི་བདེ་བ་བྱིན་པའོ། །

[Block 1040]
སྡུག་བསྔལ་ལས་བཏོན༌[^1042]ཏེ་བདེ་བ་བྱིན་པ་དང་ཡེ་ཤེས་དང་བསོད་ནམས་བྱིན་པ་དང་། འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་འབྲས་བུ་བྱིན་པ་དང་། འབྲས་བུ་ཆུང་ངུ་དང༌[^1043]ཆེན་པོ་བྱིན་པར་གོ་རིམས་བཞིན་སྦྱར་རོ། །

[Block 1041 [HEADING]]
###### **འབྲས་བུ་མཐུན་པ།** ^4-2-10-1-4-2-3-2-0

[Block 1042]
མདོ་ལས་ཤཱ་རིའི་བུ་ང་ཡང་ཞེས་པ་ནས་ཐམས་ཅད་མཁྱེན་པ་ཞེས་པའི་བར་དུ་ནི་ད་ལྟར་གྱི་སེམས་ཅན་ཐམས་ཅད་འབྲས་བུ་ཐོབ་པ༌[^1044]མཐུན་པར་བསྟན་པའོ། །

[Block 1043]
མདོ་ལས་དེ་ནི་སེམས་ཅན་རྣམས་ཞེས་པ་ནས་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་སེམས་ཅན་རྣམས་ལ་ཆོས་འཆད་པ་ཡང་ཐེག་པ་གཅིག་ལས༌[^1045]བརྩམས་ཏེ་དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་མཐོང་བ་ཉིད་ལ་འཛུད་པ༌[^1046]དང་སྟོན་པ་དང་འཇུག་པ་དང་ཆུད་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1044]
འཛུད་པ་ནི་མུ་སྟེགས་ཅན་དག་ལོག་པར་ལྟ་བ་ལས་བཟློག་སྟེ་ཡང་དག་པའི་ཆོས་ལ་ཞུགས་པའོ། །

[Block 1045]
ཆུད་པར་བྱེད་པ་ནི་ཉན་ཐོས་པ་དག་བྱང་ཆུབ་ཆེན་པོ་ཆུད་པར་བྱེད་ཅིང་། ཆུང་ངུ་ལས་བཟློག་ནས་ཆེན་པོ་ཆུད་པར་བྱེད་པའོ། །

[Block 1046]
འགྲེལ་པ་ལས་འཛུད་པ་ནི་བླ་ན་མེད་པའི་དོན་ཏོ། །

[Block 1047]
སྟོན་པ་ནི་མཐུན་པའི་དོན་ཏེ་ཐེ་ཙོམ་ཡོད་ན་བསྒོམ༌[^1047]ཞིང་སྤྱོད་པའོ། །

[Block 1048]
འཇུག་པ་ནི་མི་ཤེས་པའི་དོན་ཏེ། སེམས་མ་བསྐྱེད་པ༌[^1048]བསྐྱེད་པ༌[^1049]དང་མུ་སྟེགས་ཅན་དག་དམ་པའི་དོན་ལ་གཞུག༌[^1050]པའི་ཕྱིར་རོ། །

[Block 1049]
ཆུད་པར་བྱེད་པ་ནི་ཕྱིར་མི་ལྡོག་པའི་ས་ལ་ཆུད་པར་བྱེད་པ༌[^1051]དང་སེམས་བསྐྱེད་པ་དག་ཆོས་ཆུད་པ་དང་ཉན་ཐོས་པ་དག་བྱང་ཆུབ་ཆེན་པོ་ཆུད་པར་བྱེད་པའོ། །

[Block 1050]
མདོ་ལས་དེ་ནི་སེམས་ཅན་རྣམས་ཞེས་པ་ནས་བྱང་ཆུབ་ཐོབ་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི༌[^1052]

[Block 1051 [HEADING]]
###### **ད་ལྟར་ངས་བསྟན་པའི་ཆོས་ལུགས།** ^4-2-10-1-4-3-0

[Block 1052]
ང་ཡང་ཆོས་ལུགས་འདི་ལ་བརྟེན་ཏེ། ཐམས་ཅད་ཀྱི་ཆོས་ཀྱང་དེའོ་ཞེས་བསྟན་པ་སྟེ། སངས་རྒྱས་ཉག་གཅིག་ལ་སྣ་ཚོགས་མཁྱེན་པའི་སྟོབས་མངའ་བས་སེམས་ཅན་གྱི་དབང་པོ་སྣ་ཚོགས་མཁྱེན་ཅིང་ཡེ་ཤེས་ཀྱི་སྟོབས༌[^1053]ཤིན་ཏུ་མོས་པ་མཁྱེན་ཏེ་མོས་པའི༌[^1054]ནི་སྤྱོད་པ་ལ་མོས་པའོ། །

[Block 1053]
ཁམས་སྣ་ཚོགས་མཁྱེན་པའི་སྟོབས་མངའ་བས་རང་བཞིན་མཁྱེན་ཏེ། རིགས་མ་ངེས་པའི་ཁམས་སུ་གཏོགས་པ་མོས་པ་བསྐྱེད་པའི་ཕྱིར་སྔར་ཐེག་པ་གསུམ་ཐབས་ཙམ་དུ་གསུངས་ནས། ཕྱིས་མཐར་ཕྱིན་པའི་ཐེག་པ༌[^1055]གསུངས་ཏེ། སོ་སོའི་སྐྱེ་བོ༌[^1056]དག་སངས་རྒྱས་ཀྱི་ཐེག་པ་གཅིག་ཐོབ་པ་དང་རྣམ་པ༌[^1057]ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བའི་ཕྱིར་མདོ་ལས་ཐེག་པ་གཅིག་ལས༌[^1058]བརྩམས་ཏེ་ཐམས་ཅད་མཁྱེན་པའི་མཐའི་བར་དུ་གསུངས་སོ། །

[Block 1054 [HEADING]]
###### འཛིན་པ་རྣམ་གཉིས་བསྩལ་བ། ^4-2-10-1-5-0

[Block 1055]
མདོ་ལས་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་ཐེག་པ་གཉིས་སུ་གདགས་པ་ཡང་མེད་ན་གསུམ་དུ་ལྟ་ཅི་སྨོས་ཞེས་པའི་བར་དུ་ནི་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་གཉིས་པ་ཡང་མེད་ན་ཉན་ཐོས་ཀྱི་ཐེག་པ་གསུམ་པ་ཡོད་པ་ལྟ་ཅི་སྨོས་ཞེས་བསྟན་པ་སྟེ། མདོ་ལས་རའི་ཤིང་རྟ་དང་རི་དགས་ཀྱི་ཤིང་རྟ་དང་། གླང་པོ་ཆེའི་ཤིང་རྟ་འདོད་པའི་ཕྱིར་མེ་འབར་བའི་གྲོང་ཁྱེར་ལས་བྱུང་བ་ནི་ཐེག་པ་གཉིས་བསལ་བར༌[^1059]ཟད་ཀྱི་གླང་པོ་ཆེའི་ཐེག་པ་ཡང་བསལ་བ་མ་ཡིན་ཏེ་དེ་བས་ནི༌[^1060]འདི་ལ་ཐེག་པ་གཉིས་ཀྱི་མྱ་ངན་ལས་འདའ་བ་དང་མཐར་ཕྱིན་པ་མེད་དོ་ཞེས་གསུངས་སོ། །
--- END BLOCKS ---
