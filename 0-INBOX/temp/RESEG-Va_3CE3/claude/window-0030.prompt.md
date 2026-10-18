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
[Block 1051 [HEADING]]
###### ཡང་དག་པར་བསྔོ་བ། ^1-2-2-4-6-0

[Block 1052]
དེའི་འོག་ཏུ་དགེ་བའི་རྩ་བ་རྣམས་ལ་མཚན་མར་བྱས་ཏེ། ཡོངས་སུ་བསྔོ་ཞིང་འདས་པའི་སངས་རྒྱས་རྣམས་ལ་ཡང་འདས་པའི་ཡིད་ལ་བྱེད་པས་མཚན་མར་བྱེད་ཅིང་ཡུལ་ཡིན་པར་ཡིད་ལ་བྱེད་ན་ཕྱིན་ཅི་ལོག་ཏུ་འགྱུར་རོ། །

[Block 1053]
གལ་ཏེ་དགེ་བའི་རྩ་བ་དེ་དག་དང་། མངོན་པར་འདུ་བྱེད་པ་དེ་དག༌[^754]དང་། སེམས་བསྐྱེད་པ་དེ་དག་ཤེས་པར་མི་བྱེད་ཅིང་ཚད་མར་མི་བྱེད་ན་དེ་ཡང་དག་པར་བསྔོ་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དྲུག་པའོ། །

[Block 1054 [HEADING]]
###### དུག་མེད་པའི་ཡོངས་སུ་བསྔོ་བ། ^1-2-2-4-7-0

[Block 1055]
དེ་ནས་བྱང་ཆུབ་སེམས་དཔའ་བྱམས་པས་མཚན་མར་མི་བྱེད་པ་དང་། ཡོངས་སུ་བསྔོ་བ་གཉིས་མི་འགལ་བར་ཇི་ལྟར་རུང་སྙམ་ནས་དྲིས་པ་དང་། དེ་ནས་གནས་བརྟན་རབ་འབྱོར་གྱིས་དེ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཐབས་ལ་མཁས་པ་རྣམས་ཀྱི་ཡིན་ནོ་ཞེས་བྱ་བ་བསྟན་ཏོ། །

[Block 1056]
དེ་ནས་བྱང་ཆུབ་སེམས་དཔའ་བྱམས་པས་འདི་སྐད་བསྟན་ཏེ། དེ་ལ་ཡང་དག་པར་ཡོངས་སུ་བསྔོ་བར་འདོད་པའི་བྱང་ཆུབ་སེམས་དཔས་འདི་ལྟར་ཡོངས་སུ༌[^755]བརྟག་པར་བྱ་སྟེ། སངས་རྒྱས་དེ་དག་དང་། དགེ་བའི་རྩ་བ་དེ་དག་དང་། མངོན་པར་འདུ་བྱ་བ་དེ་དག་དང་། སེམས་དེ་དག་ཀྱང་ཡོད་པ་མ་ཡིན་ན། འོན་ཀྱང་བདག་ནི་དེ་དག་ཐམས་ཅད་མཚན་མར་བྱས་ནས་རྣམ་པར་རྟོག་པ་ལྟ་ཞིག །དེ་ལྟར་མཚན་མར་བྱས་ཤིང་རྣམ་པར་རྟོག་པས་ཡོངས་སུ་བསྔོ་བ་ནི་དེ་བཞིན་གཤེགས་པས་རྗེས་སུ་གནང་བ་མ་མཛད་དེ། དེ་ནི་ཁ་ཟས་ཞིམ་པོ་དུག༌[^756]དང་མཚུངས་སོ། །

[Block 1057]
དེ་བས་ན་དེ་ལྟར་ཡོངས་སུ་བསྔོ་བར་མི་བྱ་ཞིང་དེ་ལ་བསླབ་པར་ཡང་མི་བྱའོ། །

[Block 1058]
དེ་བས་ན་སངས་རྒྱས་ཉིད་ཚད་མར་བྱས་ལ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་དེ་དག་གིས་དེ་དག་ཐམས་ཅད་ཇི་ལྟར་མཁྱེན་པ་དེ་བཞིན་དུ་བདག་གིས་ཀྱང་ཡོངས་སུ་བསྔོའོ་ཞེས་ཡོངས་སུ་སྔོ་བར༌[^757]བྱེད་པ་དུག་མེད་པའི་ཡོངས་སུ་བསྔོ་བའི་འགྲེས་ནི་བདུན་པའོ། །

[Block 1059 [HEADING]]
###### དུས་གསུམ་དུ་མ་གཏོགས་པར་ཡིད་ལ་བྱེད་པས་ཡོངས་སུ་བསྔོ་བ། ^1-2-2-4-8-0

[Block 1060]
དེ་ནས་ཆོས་ཐམས་ཅད་ཁམས་གསུམ་དང་དུས་གསུམ་དུ་མ་གཏོགས་པར་ཡིད་ལ་བྱེད་པས་ཡོངས་སུ་བསྔོ་བ་ནི་དུག་མེད་པའོ། །

[Block 1061]
དེ་ལས་གཞན་དུ་ཡོངས་སུ་བསྔོ་བ་ནི་དུག་དང་བཅས་པའོ་ཞེས་བྱ་བ་ནི་བརྒྱད་པའོ། །

[Block 1062 [HEADING]]
###### སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ཀྱི་སྤྱོད་ཡུལ་གྱི་ཆོས་ཉིད་ཀྱིས་ཡོངས་སུ་བསྔོ་བ། ^1-2-2-4-9-0

[Block 1063]
དེ་ནས་ཡང་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ཀྱི་སྤྱོད་ཡུལ་གྱི་ཆོས་ཉིད་ཀྱིས་བདག་ཡོངས་སུ་བསྔོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དགུ་པའོ། །

[Block 1064 [HEADING]]
##### བསོད་ནམས་མང་དུ་འཕེལ་བ། ^1-2-2-5-0

[Block 1065 [HEADING]]
###### དགེ་བ་བཅུའི་ལས་ཀྱི་ལམ་ལ་སོགས་པའི་བསོད་ནམས་པས་མང་བ། ^1-2-2-5-1-0

[Block 1066]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་ཚིག་ལས་རྣམ་པ་མང་དུ་རྗེས་སུ་ཡི་རང་བར༌[^758]མཛད་ནས་རྣམ་པ་གསུམ་གྱིས་བསོད་ནམས་མང་དུ་འཕེལ་བར་བསྟན་པ་སྟོང་གསུམ་གྱི་སྟོང་ཆེན་པོའི་འཇིག་རྟེན་གྱི་ཁམས་ཀྱི་སེམས་ཅན་ཐམས་ཅད་ཀྱིས་དགེ་བ་བཅུའི༌[^759]ལས་ཀྱི་ལམ་དང་། བསམ་གཏན་དང་། ཚད་མེད་པ་དང་། གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པ་དང་། མངོན་པར་ཤེས་པ་ཐོབ་པ་རྣམས་ཀྱི་བསོད་ནམས་པས་ཆགས་པ་མེད་པའི་ཡོངས་སུ་བསྔོ་བ་འདི་བསོད་ནམས་ཆེས་མང་ངོ་ཞེས་བྱ་བ་ནི་གཅིག་གོ། །

[Block 1067 [HEADING]]
###### དགྲ་བཅོམ་པ་དང་རང་བྱང་ཆུབ་ལ་བསྙེན་བཀུར་བྱས་པའི་བསོད་ནམས་པས་ལྷག་པ། ^1-2-2-5-2-0

[Block 1068]
དེ་ལ་སེམས་ཅན་དེ་དག་ཐམས་ཅད་རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པ༌[^760]ནས། དགྲ་བཅོམ་པ་དང་། རང་བྱང་ཆུབ་ཀྱི་བར་དུ་གྱུར་པ་རྣམས་ལ་རྐྱེན་བཞིས་ཇི་སྲིད་འཚོའི་བར་དུ་བསྙེན་བཀུར་བྱས་པའི་བསོད་ནམས་པས་ལྷག་པ་ཞེས་བྱ་བ་ནི་གཉིས་པའོ། །

[Block 1069 [HEADING]]
###### བྱང་ཆུབ་སེམས་དཔར་གྱུར་པ་རྣམས་ལ་བསྙེན་བཀུར་བྱས་པའི་བསོད་ནམས་པས་ལྷག་པ། ^1-2-2-5-3-0

[Block 1070]
དེ་ཉིད་ལ་སེམས་ཅན་དེ་དག་ཐམས་ཅད་བྱང་ཆུབ་སེམས་དཔར་གྱུར་པ་རྣམས་ལ་ཕྱོགས་བཅུའི་སེམས་ཅན་ཐམས་ཅད་ཀྱིས་དེ་དག་རེ་རེ་ལ་ཡང་རྐྱེན་བཞི་དང་བདེ་བའི་ཡོ་བྱད་ཐམས་ཅད་ཀྱིས་བསྐལ་པ་གང་གཱའི་ཀླུང་གི་བྱེ་མ་སྐྱེད་དུ་བསྙེན་བཀུར་བྱས་པའི་བསོད་ནམས་ཀྱི་ཕུང་པོ་དེ་ལྟ་བུ་དེ་དག་པས་ཀྱང་ལྷག་གོ་ཞེས་བྱ་བ་ནི་གསུམ་པའོ། །

[Block 1071]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བསོད་ནམས་བགྱི་བའི་དངོས་པོ་དེ་ལ་གཟུགས་མཆིས་སུ་ལགས་ན་ནི་འཇིག་རྟེན་གྱི་ཁམས་གང་གཱའི་ཀླུང་གི་བྱེ་མ་སྙེད་དུ་ཡང་མི་ཤོང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་དེར་ཀུན་མི་ཆུད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1072]
དེའི་འོག་ཏུ་བསོད་ནམས་སྔ་མ་རྣམས་ནི་མཚན་མའི་འདུ་ཤེས་དང་། དམིགས་པའི་འདུ་ཤེས་ཅན་ཡིན་པས་དམན་པ་ཡིན་གྱི་ཡོངས་སུ་བསྔོ་བའི་བསོད་ནམས་ཀྱི་ཕུང་པོ་ལ་ནི་དེ་དག་མེད་པའི་ཕྱིར་དེ་བས་ལྷག་གོ་ཞེས་བྱ་བའི་འགྲེས་དང་། དེའི་འོག་ཏུ་འདོད་པ་ན་སྤྱོད་པ༌[^761]ལྷའི་བདག་པོ་ཐམས་ཅད་དང་། ལྷ་རྣམས་དང་ཚངས་པ་ཐམས་ཅད་ཀྱིས་མཆོད་པ་བྱས་པ་དང་། རབ་ཏུ་བསྔགས་པ་བརྗོད་པའི་འགྲེས་གཉིས་དང་། དེའི་འོག་ཏུ་སྟོང་གསུམ་གྱི་སྟོང་ཆེན་པོའི་འཇིག་རྟེན་གྱི་ཁམས་ཀྱི་སེམས་ཅན་ཐམས་ཅད་བྱང་ཆུབ་སེམས་དཔར་གྱུར་པ་རྣམས་ཀྱི་དམིགས་པ་དང་བཅས་པར་ཡོངས་སུ་བསྔོ་བའི་བསོད་ནམས་ཀྱི་ཕུང་པོ་བས་བྱང་ཆུབ་སེམས་དཔའ་གཅིག་གི་མི་དམིགས་པར༌[^762]ཡོངས་སུ་བསྔོ་བའི་བསོད་ནམས་ཀྱི་ཕུང་པོ་ལྷག་པར་ཆེ་བ་བསྟན་པའི་འགྲེས་སོ། །

[Block 1073]
མི་ལེན་མི་གཏོང་།[^763] མི་རློམ་མི་བརྙས༌[^764]ཤིང་དམིགས་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་དེ་རྣམས་དང་དགེ་བའི་རྩ་བ་རྣམས་དེ་བཞིན་ཉིད་དུ་དམན་པ་དང་ལྷག་པ་མེད་པའི་དོན་གྱི་དབང་གིས་མཉམ་པ་ཉིད་དུ་བསྟན་པའོ། །

[Block 1074]
དེ་བཞིན་དུ་སྐྱེ་བ་དང་། འགག་པ་དང་། ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བ་ལ་སོགས་པ་མེད་པའི་ཕྱིར་ཇི་ལྟར་སངས་རྒྱས་རྣམས་དང་། ཉན་ཐོས་དང་། རང་སངས་རྒྱས་དང་། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་དང་། སོ་སོའི་སྐྱེ་བོ་དེ་དག་དང་། དགེ་བའི་རྩ་བ་རྣམས་དང་། ཡོངས་སུ་བསྔོ་བའི་སེམས་ཀྱང་དེ་བཞིན་ཉིད་ལ་སོགས་པ་ལ་གནས་པ་དེ་བཞིན་དུ་བདག་ཀྱང་རྗེས་སུ་ཡི་རང་ངོ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་ཡི་རང་བ་གཅིག་པའོ། །

[Block 1075]
དེ་ནས་ཡང་ཆོས་ཐམས་ཅད་ནི་རྣམ་པར་གྲོལ་བར་མཚུངས་ཏེ། དེ་དང་མཚུངས་པས་ཆོས་ཐམས་ཅད་མཉམ་པའོ། །

[Block 1076]
ཆོས་ཐམས་ཅད་ངོ་བོ་ཉིད་ཀྱིས་དབེན་པའི་ཕྱིར་སྔོན་སོ་སོའི་སྐྱེ་བོའི་ཚེ་མ་བཅིངས༌[^765]མ་གྲོལ་བའོ། །

[Block 1077]
ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས་རྣམ་པར་དག་པའི་ཕྱིར་སྔར་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་དང་། ཕྱིས་རྣམ་པར་བྱང་བ་མེད་པའོ། །

[Block 1078]
ཆོས་ཐམས་ཅད་གཟོད་མ་ནས་ཞི་བའི་ཕྱིར་སྔར་རྒྱུ་དང་རྐྱེན་གྱི་དབང་གིས་སྐྱེ་བ་མེད་དོ། །

[Block 1079]
ངོ་བོ་ཉིད་མེད་པས་འབྱུང་བ་མེད་དོ། །

[Block 1080]
ཕྱིས་འགག་པ་མེད་ཅིང་འཕོ་བ་མེད་པ་དང༌[^766]འཇིག་པ་མེད་དོ། །

[Block 1081]
དེ་ལྟར་བཅིངས་པ་དང་གྲོལ་བ་མེད་པ་དང་། ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་དང་། རྣམ་པར་བྱང་བ་མེད་པ་དང་། སྐྱེ་བ་དང་འབྱུང་བ་དང་འགག་པ་མེད་པ་དང་། འཕོ་བ་དང་འཇིག་པ་མེད་པས་ཆོས་ཐམས་ཅད་མཉམ་མོ་ཞེས་སོ་སོར་རྟོག་ཅིང་རྗེས་སུ་ཡི་རང་བ་ནི་གཉིས་པའོ། །

[Block 1082]
དེ་ནས་ཡང་ཕྱོགས་བཅུའི་སངས་རྒྱས་ཐམས་ཅད་ལ་བདེ་བའི་ཡོ་བྱད་ཐམས་ཅད་ཀྱིས་བསྙེན་བཀུར་བྱས་པ་དང་། [^767]དམིགས་པ་དང་བཅས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གིས་བསོད་ནམས་བསགས་པས༌[^768]མི་དམིགས་པའི་ཚུལ་གྱིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྤྱད་པའི་བསོད་ནམས་ཀྱི་ཕུང་པོ་ཡོངས་སུ་བསྔོ་བའི་བསོད་ནམས་ཆེ་བར་བསྟན་པའི་འགྲེས་ཏེ། འདི་དག་ནི་རྗེས་སུ་ཡི་རང་བའི་འགྲེས་སོ། །

[Block 1083 [HEADING]]
#### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟོད་པ། ^1-2-3-0

[Block 1084]
དེ་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མཆོད་པ་དང་བཀླགས་པ་དང་སྦྱིན་པ་ལ་སོགས་པ་ལ་རྗེས་སུ་ཡི་རང་བ་དང་། ཡོངས་སུ་བསྔོས་པའི་བསོད་ནམས་རྒྱ་ཆེན་པོ་ཐོས་ནས་གནས་བརྟན་ཤཱ་རིའི་བུ་དད་པ་སྐྱེས་ཏེ་འཁོར་གཞན་རྣམས་དད་པ་བསྐྱེད་པའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཤིན་ཏུ་རྣམ་པར་དག་པའི་སླད་དུ་སྣང་བར་བགྱིད་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིག་བཅུ་བདུན་གྱིས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི༌[^769]བསྟོད་པ་ལ༌[^770]བརྩམས་སོ། །

[Block 1085]
ལན་གསུམ་དུ་བཟླས་ཏེ་ཆོས་ཀྱི་འཁོར་ལོ་རྣམ་པ་བཅུ་གཉིས་སུ་བསྐོར་བའོ་ཞེས་བྱ་བ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བདེན་པ་བཞིའི་ཆོས་ཀྱི་འཁོར་ལོ་ལན་གསུམ་དུ་བཟླས་ཏེ་རྣམ་པ་བཅུ་གཉིས་སུ་བསྐོར་ཞེས་བྱའོ། །

[Block 1086]
དེ་ལ་འདི་ནི་ལན་གསུམ་དུ་བཟླས་ནས་བསྐོར་བ་སྟེ། འདི་ནི་བདེན་པ་བཞིའོ་ཞེས་བྱ་བར་བདེན་པ་བཞིའི་ངོ་བོ་ཉིད་ཀྱི་ལེའུ་ཚིག༌[^771]ནི་གཅིག་གོ། །

[Block 1087]
བདེན་པ་བཞི་པོ་དེ་དག་ཉིད་ཡོངས་སུ་ཤེས་པར་བྱ་བ་དང་། སྤང་བར་བྱ་བ་དང་། མངོན་སུམ་དུ་བྱ་བ་དང་། བསྒོམ་པར་བྱ་བའི་ལེའུ་ཚིག༌[^772]ནི་བསྐོར་བ་གཉིས་སོ། །

[Block 1088]
བདེན་པ་བཞི་པོ་དེ་དག་ཉིད་བདག་གིས་ཡོངས་སུ་ཤེས་སོ། །

[Block 1089]
སྤངས་སོ། །

[Block 1090]
མངོན་སུམ་དུ་བྱས་སོ། །
--- END BLOCKS ---
