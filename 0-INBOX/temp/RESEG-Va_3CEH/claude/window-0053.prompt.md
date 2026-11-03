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
[Block 1856 [HEADING]]
##### མཐུན་པའི་བསམ་པ། ^9-6-5-2-0

[Block 1857]
ཡང་བསམ་པ་གཉིས་པ་ནི་གང་དམ་པའི་ཆོས་པདྨ་དཀར་པོ་ལས་ཉན་ཐོས་ལུང་བསྟན་པ་དེ་དག་གིས་ནི་སངས་རྒྱས་ཀྱིས་ཀྱང་ཆོས་ཉིད་མཉམ་པ་ཉིད་ལ་དགོངས་ནས། ཆོས་ཀྱི་སྐུ་ཐོབ་པ་ཉིད༌[^1082]ཡིན་ནོ་ཞེས་བསམས་ནས་མཉམ་པ་ཉིད་ལ་དགོངས་པ་དང་། མཐུན་པའི་བསམ་པ་ཐོབ་པ་ནི་སངས་རྒྱས་ཀྱི་ཆོས་ཉིད་ཡང་དག་པར་ཐོབ་པ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 1858 [HEADING]]
#### སྤྲུལ་པའི་ཕྱིར། ^9-6-6-0

[Block 1859]
དོན་གཞན་ཡང་དེ་ལྟ་བུའི་མིང་ཅན་གྱི་བྱང་ཆུབ་སེམས་དཔའི་འཁོར་དེ་ལུང་བསྟན་པ་ཡིན་པས་སྤྲུལ་པའི་ཕྱིར་ཡང༌[^1083]ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་ལྟར་ངས་མངོན་པར་ཤེས་ཏེ། ང་ཉིད་ལན་བརྒྱ་སྟོང་དུ་མར་ཉན་ཐོས་ཀྱི་ཐེག་པར་མྱ་ངན་ལས་འདས་པར་གྱུར་ཏོ་ཞེས་པ་དེ༌[^1084]ལྟ་བུ་ལ་དགོངས་ནས་ཐེག་པ་གཅིག་ཉིད་དུ་བསྟན་ཏེ། གང་ཉན་ཐོས་ཀྱི་ཐེག་པས་གདུལ་བའི་སེམས་ཅན་རྣམས་མྱ་ངན་ལས་བཟླ་བའི་ཕྱིར་བསྟན་པ་ཡིན་ནོ། །

[Block 1860 [HEADING]]
#### མཐར་ཕྱིན་པ། ^9-6-7-0

[Block 1861]
མཐར་ཕྱིན་པས་ན་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཐེག་པ་འདིས་མཐར་ཕྱིན་པར་གྲོལ་བར་བྱ་བའི་ཐེག་པ་གཞན་ནི་མེད་པས་སངས་རྒྱས་ཀྱི་ཐེག་པ་འདི་ནི་ཉན་ཐོས་ལ་སོགས་པ་དེ་དག་ལས་ཁྱད་པར་དུ་འཕགས་པ་ཡིན་པས་དེ་ལས་དགོངས་ནས་ཀྱང་ཐེག་པ་གཅིག་ཉིད་དུ་བསྟན་ཏེ།[^1085]

[Block 1862 [HEADING]]
### གཅིག་ཉིད་དམ་མང་པོ་ཉིད་དུ་བལྟ་བ། ^9-7-0

[Block 1863 [HEADING]]
#### གཅིག་ཉིད་དུ་བལྟ་བ། ^9-7-1-0

[Block 1864]
ད་ནི་སངས་རྒྱས་ཐམས་ཅད་ཆོས་ཀྱི་སྐུ་མཉམ་པ་ཉིད་ཡིན་ན། ཡང་རྒྱུ་གང་གིས་གཅིག་ཉིད་དམ་མང་པོ་ཉིད་དུ་བལྟ་བར་བྱ་བ་དེ་བསྟན་པར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག་གཅིག་ཉིད་དུ་བལྟ་བར་བྱ་བ་ནི་དེ་དག་གཅིག༌[^1086]ཉིད་ནི་མཉམ་པ་ཉིད་ཡིན་ལ་སངས་རྒྱས་ཀྱང་དེའི་རང་བཞིན་ཡིན་པས་དེའི་ཕྱིར་དེ་ནི་གཅིག་ཉིད་ཡིན་ཏེ། ཆོས་ཀྱི་དབྱིངས་གཅིག་པ༌[^1087]ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 1865]
ཡང་གཅིག་ཉིད་དུ་བལྟ་བར་བྱ་སྟེ། གང་དུས་གཅིག་ལ་འཇིག་རྟེན་གྱི་ཁམས་གཅིག་ཏུ་སངས་རྒྱས་གཉིས་འབྱུང་བ་ནི་མི་སྲིད་པས་དེའི་ཕྱིར་ཡང་གཅིག་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 1866 [HEADING]]
#### མང་པོ་ཉིད་དང་གཅིག་ཉིད་ཚིགས་སུ་བཅད་པས་བསྟན་པ། ^9-7-2-0

[Block 1867 [HEADING]]
##### གཅིག་པ་ཉིད་དུ་བསྟན་པ། ^9-7-2-1-0

[Block 1868]
ཡང་མང་པོ་ཉིད་དང་གཅིག་ཉིད་ཚིགས་སུ་བཅད་པས་བསྟན་པ་ནི། ཁམས་གཅིག་ན་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་འབྱུང་སྟེ། ཁམས་གཅིག་ན་ནི་གཉིས་མེད་ཕྱིར། །ཞེས་བྱ་བའི་ཚིག་གིས་ནི་གཅིག་པ་ཉིད་དུ་བསྟན་པའི་དོན་ཏེ། གང་འཇིག་རྟེན་གྱི་ཁམས་གཅིག་ཏུ་སངས་རྒྱས་གཉིས་འབྱུང་བ་ནི་མི་སྲིད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1869 [HEADING]]
##### མང་པོ་ཉིད་དུ་བསྟན་པ། ^9-7-2-2-0

[Block 1870]
ལྷག་མས་ནི༌[^1088]མང་པོ་ཉིད་དུ་བསྟན་ཏེ། དཔག་མེད་ཅིག་ཅར་ཚོགས་བསགས་ཕྱིར། །ཞེས་བྱ་བ་ནི་གང་དུས་གཅིག་ཏུ་བྱང་ཆུབ་སེམས་དཔའ་མང་པོ་རྣམས་ཚོགས་ཡོངས་སུ་བསགས་པར་འགྱུར་ལ། གལ་ཏེ་དེ་དག་གིས་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་བསགས་ཀྱང་སངས་རྒྱས་ཉིད་ཐོབ་པར་མི་འགྱུར་ན་ཚོགས་བསགས་པ་དོན་མེད་པ༌[^1089]ཉིད་དུ་འགྱུར་རོ། །

[Block 1871]
དེའི་ཕྱིར་ན་མང་པོ་རྣམས་ཀྱིས་ཚོགས་ཡོངས་སུ་རྫོགས་པར༌[^1090]འགྲུབ་པས་སངས་རྒྱས་མང་པོ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 1872]
རིམ་གྱིས་འབྱུང་བར་མི་རིགས་ཕྱིར། །ཞེས་བྱ་བ་ནི་རིམ་གྱིས་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པར་ཡང་མི་འགྲུབ་སྟེ། གལ་ཏེ་གང་གི་ཕྱིར་ཚོགས་ཡོངས་སུ་རྫོགས་པར་གྱུར་པ་རྣམས་རིམ་གྱིས་གཞེས་པར༌[^1091]གྱུར་ན། དེ་དག་ཉིད་ཀྱི་རྗེས་སུ་རིམ་གྱིས་ཐོབ་པར་འགྱུར་ཏེ། གཞན་དག་ཀྱང་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པར་འགྱུར་བ་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ། དེ་དག་མང་བ་ཉིད་ཀྱི་ཕྱིར་རིམ་གྱིས་རིགས་པ་མ་ཡིན་ཏེ། གཞན་དག་ཀྱང་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འགྱུར་བས་སོ། །

[Block 1873]
དེའི་ཕྱིར་ན་ཡང་། སངས་རྒྱས་ཉིད་མང་པོ་ཡིན་ནོ། །

[Block 1874 [HEADING]]
### གཏན་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ། ^9-8-0

[Block 1875 [HEADING]]
#### གཏན་དུ་མྱ་ངན་ལས་འདས་པར་འགྱུར་བ། ^9-8-1-0

[Block 1876]
ཡང་ཁ་ཅིག་ནི་སངས་རྒྱས་རྣམས་ལ་གཏན་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་མེད་དོ་ཞེས་ཟེར་ལ། ཉན་ཐོས་ཀྱི་ཐེག་པ་པའི་སྡེ་པ་གཞན་དག་ནི་གཏན་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། འདི་ལྟར་དེ་དག་གཉི་གའི་དགོངས་པ་ཚིགས་སུ་བཅད་པས་སྟོན་པ༌[^1092]ནི། སྒྲིབ་པ་ཀུན་ལས་ངེས་གྲོལ་ཕྱིར། །ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱ་ཆེར་འབྱུང་སྟེ། དེ་ལ་གང་གི་ཕྱིར་སངས་རྒྱས་ནི་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་ཐམས་ཅད་ལས་རྣམ་པར་གྲོལ་བ་ཡིན་པའི་ཕྱིར་དེས་ན་གཏན་དུ་མྱ་ངན་ལས་འདས་པར་འགྱུར་བ་ཡིན་ཏེ། དགོངས་པ་དེའི་ཕྱིར་རོ། །

[Block 1877 [HEADING]]
#### གཏན་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་མ་ཡིན་པ། ^9-8-2-0

[Block 1878]
ཡང་གང་གི་ཕྱིར་མཛད་པ་རྣམས་ཀྱང་ཡོངས་སུ་མ་རྫོགས་པ་སྟེ་མ་སྨིན་པ་རྣམས་སྨིན་པར་བྱ་བ་དང་། སྨིན་པ་རྣམས་རྣམ་པར་གྲོལ་བར་བྱ་བ་དགོངས་པའི༌[^1093]ཕྱིར་དེའི༌[^1094]མཛད་པ་དེ་ལ་དགོངས་ནས་གཏན་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་མ་ཡིན་ན།[^1095] །དེ་ལྟ་མ་ཡིན་ཏེ། ཉན་ཐོས་བཞིན་དུ་གཏན་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་མ༌[^1096]ཡིན་ན་སྨོན་ལམ་བཏབ་པ་འབྲས་བུ་མེད་པར་འགྱུར་རོ། །

[Block 1879 [HEADING]]
### ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་ངོ་བོ་ཉིད་ཀྱི་སྐུ་མ་ཡིན་པ། ^9-9-0

[Block 1880 [HEADING]]
#### གཟུགས་ཀྱི་སྐུར་སྣང་བ། ^9-9-1-0

[Block 1881]
ད་ནི་གང་ལས་དགོངས་ནས་ངོ་བོ་ཉིད་ཀྱི་སྐུ་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་མ་ཡིན་ཞེ་ན། དེ་བསྟན་པར་བྱ་སྟེ། དེ་གཟུགས་ཀྱི་སྐུར་སྣང་བ་དང་ཞེས་བྱ་བ་ལ། སངས་རྒྱས་ནི་ཆོས་ཀྱི་སྐུ་ཡིན་ལ། དེ་ནི་གཟུགས་སུ་མཐོང་བའི་ཕྱིར། ཆོས་ཀྱི་སྐུ་མ་ཡིན་ཏེ། དེ་ལྟ་བུ་ནི་ཆོས་ཀྱི་སྐུ་མ་ཡིན་པས། དེའི་ཕྱིར་ན་ཆོས་ཀྱི་སྐུ་མ་ཡིན་ནོ། །

[Block 1882 [HEADING]]
#### ཐ་དད་པར་སྣང་བ། ^9-9-2-0

[Block 1883]
ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་དེ་ནི་སངས་རྒྱས་ཀྱི་འཁོར་གྱི་དཀྱིལ་འཁོར་ཚད་མེད་པ་དག་ན་ཐ་དད་པར་སྣང་ལ། ཆོས་ཀྱི་སྐུ་ལ་ནི་ཐ་དད་པ་མེད་དོ། །

[Block 1884]
དེའི་ཕྱིར་ཚུལ་འདིས་ཀྱང་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་ངོ་བོ་ཉིད་ཀྱི་སྐུ་མ་ཡིན་ནོ། །

[Block 1885 [HEADING]]
#### མོས་པ་ཇི་ལྟ་བ་བཞིན་དུ་མཐོང་བ། ^9-9-3-0

[Block 1886]
མོས་པ་ཇི་ལྟ་བ་བཞིན་དུ་ལོངས་སྤྱོད་རྫོགས་པ་མཐོང་བས་ཀྱང་།

[Block 1887]
[^1097]ཇི་ལྟར་མདོ་ལས།

[Block 1888]
ཁ་ཅིག་ནི་ཁ་དོག་སེར་པོ། ཁ་ཅིག་ནི་ཁ་དོག་སྔོན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1889]
དེ་བཞིན་དུ་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་ནི་མ་ངེས་པའི་ངོ་བོ་ཉིད་དུ་སྣང་བ་ཡིན་གྱི། ངོ་བོ་ཉིད་ཀྱི་སྐུ་ནི་མ་ངེས་པའི་ངོ་བོ་ཉིད་དུ་མི་རིགས་ཏེ། དེའི་ཕྱིར་ཚུལ་དེས་ཀྱང་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་ནི་ངོ་བོ་ཉིད་ཀྱི་སྐུ་མ་ཡིན་ནོ། །

[Block 1890 [HEADING]]
#### གཞན་དང་གཞན་དུ་མཐོང་བ། ^9-9-4-0

[Block 1891]
ཡང་ལོངས་སྤྱོད་རྫོགས་པ་དེ་ནི་གཅིག་ཉིད་ཡིན་ན་ཡང་གཞན་དང་གཞན་དུ་མཐོང་བར་འགྱུར་ལ། ཡང་དེ་ཉིད་ཁོ་ན་དེ་ལས་ཀྱང་གཞན་དུ་མཐོང་བར་འགྱུར་བས་དེ་ནི་གཡོ་བའི་ངོ་བོའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱི་སྐུ་ཡིན་པར་མི་རིགས་ཏེ། དེའི་ཕྱིར་ན་ཡང་ངོ་བོ་ཉིད་ཀྱི་སྐུ་མ་ཡིན་ནོ། །

[Block 1892 [HEADING]]
#### འཁོར་དང་རྟག་ཏུ་འདྲེས་པ། ^9-9-5-0

[Block 1893]
ཡང་ལོངས་སྤྱོད་རྫོགས་པ་དེ་ནི་ལྷ་ལ་སོགས་པའི་འཁོར་དང་རྟག་ཏུ་འདྲེས་ཤིང་བསྐོར་ནས་གནས་པ་ཡིན་གྱི། ངོ་བོ་ཉིད་ནི་འདྲེས་པར་མི་འགྱུར་ཏེ། དེའི་ཕྱིར་ན་ཡང་ངོ་བོ་ཉིད་ཀྱི་སྐུ་མ་ཡིན་ནོ། །

[Block 1894 [HEADING]]
#### ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཡོངས་སུ་གྱུར་པ། ^9-9-6-0

[Block 1895]
གང་ཡང་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཡོངས་སུ་གྱུར་པ་ནི་ངོ་བོ་ཉིད་ཡིན་ལ། གལ་ཏེ་དེ་དག་ངོ་བོ་ཉིད་གཅིག་པ་ཉིད་ཡིན་ན་དེ་ནི་ལོངས་སྤྱོད་རྫོགས་པ་ཡང་ཡིན་པས་འཇུག་པ༌[^1098]རྣམ་པར་ཤེས་པ་ཡོངས་སུ་གྱུར་པ་ལས་སྐུ་གང་མངོན་པར་འགྲུབ་པར་འགྱུར། དེའི་ཕྱིར་ན་ཡང་ལོངས་སྤྱོད་རྫོགས་པ་ནི་ངོ་བོ་ཉིད་མ་ཡིན་ཏེ། རྣམ་པ་དྲུག་པོ་དེ་དག་མི་རིགས་པའི་ཕྱིར་ན་ཡང་མི་རུང་ངོ་། །
--- END BLOCKS ---
