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
[Block 1086]
[^865]དོན་དམ་པའི་བདེན་པའི་མཚན་ཉིད་ཡོངས་སུ་ཤེས་པར་བྱ་བས་མདོ་སྡེའི་ལུས་རྣམ་པར་གཞག་པ་བསྟན་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1087 [HEADING]]
### ཀུན་རྫོབ་ཀྱི་བདེན་པའི་མཚན་ཉིད་ཡོངས་སུ་ཤེས་པར་བྱ་བ། ^4-2-0

[Block 1088]
དེ་ལྟར་དོན་དམ་པའི༌[^866]མཚན་ཉིད་ཡོངས་སུ་ཤེས་པར་བྱ་བས་མདོ་སྡེའི་ལུས་རྣམ་པར་གཞག་པ་བསྟན་ནས་ད་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པའི་མཚན་ཉིད་ཡོངས་སུ་ཤེས་པར་བྱ་བས་མདོ་སྡེའི་ལུས་རྣམ་པར་གཞག་པ་བསྟན་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱའོ། །

[Block 1089]
དེ་ལ་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ནི་མཚན་ཉིད་དྲུག་དང་ལྡན་པར་ཤེས་པར་བྱ་སྟེ། སེམས་ཀྱི་མཚན་ཉིད་དང་། ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་དང་། [^867]ཆོས་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མེད་པའི་མཚན་ཉིད་དང་། ཆོས་གདགས་པ་རྣམ་པར་གཞག་པ་ལས་བརྩམས་ནས་རྣལ་འབྱོར་གྱིས་ཡོངས་སུ་བསྡུས་པའི་ཞི་གནས་དང་། ལྷག་མཐོང་གི་ལམ་གྱི་རབ་ཏུ་དབྱེ་བ་དང་། ཐེག་པ་རྣམ་པར་གཞག་པ་ལས་བརྩམས་ནས། ཐེག་པ་ཇི༌[^868]ལྟ་བ་བཞིན་དུ་རྣམ་པར་དབྱེ་བ་བསྟན་པ་དང་། ཐེག་པ་གདགས་པ་རྣམ་པར་གཞག་པ་ཁོ་ན་ལས་བརྩམས་ནས་དེ་བཞིན་གཤེགས་པའི་བྱ་བ་སྒྲུབ་པའི༌[^869]རབ་ཏུ་དབྱེ་བ་བསྟན་ཏོ། །

[Block 1090]
དེ་དག་གོ་རིམ༌[^870]རྣམ་པར་གཞག་པ་ནི་དེ་ལྟར་དོན་དམ་པའི་བདེན་པའི་མཚན་ཉིད་དང་ལྡན་པའི་མདོ་བརྗོད་པར་བྱ་བའི་དོན་དང་། དགོས་པའི་འབྲས་བུ་དང་། ཐོབ་པར་བྱ་བའི་ཐབས་དང་ལྡན་པ་འདི་ལ་རྣལ་འབྱོར་དམ་པ། བདག་ལ་ཕན་པར་འདོད་པ་དང་། འགྲོ་བ་མཐའ་དག་གི་གཙོ་བོར་བྱེད་པ་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཀྱི་འབྲས་བུ་འདོད་པ་རྣམས་ཀྱི་དད་པ་མཆོག་གི་གནས༌[^871]ཡིན་པར་མོས་པ་བསྐྱེད་ཅིང་མི་གཡེལ་བར་ནན་ཏན་སྙིང་པོ་བསྒྲུབ་པར་བྱ་བ༌[^872]ན།

[Block 1091]
དང་པོ་ཁོ་ནར་སེམས་ཀྱི་གསང་བ་ལ་ཤིན་ཏུ་རྨོངས་པའི་གཉེན་པོར་སེམས་དང་ཡིད་ལ༌[^873]རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པར་བྱ་དགོས་པས་འདིར་དང་པོར་སེམས་ཀྱི་མཚན་ཉིད་བསྟན་ཏོ། །

[Block 1092]
དེའི་འོག་ཏུ་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལ་ཤིན་ཏུ་རྨོངས་པའི་གཉེན་པོར་ཀུན་བརྟགས་པ་དང་གཞན་གྱི་དབང་དང་ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་ལ་མཁས་པར་བྱ་དགོས་པས་འདིར་དེའི་འོག་ཏུ་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་བསྟན་ཏོ། །

[Block 1093]
དེའི་འོག་ཏུ་ཆོས་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མེད་པ་ལ་ཤིན་ཏུ་རྨོངས་པའི་མཚན་ཉིད་དང་། སྐྱེ་བ་དང་། དོན་དམ་པ་ངོ་བོ་ཉིད་མེད་པ་ལ་མཁས་པར་བྱ་དགོས་པས་འདིར་དེའི་འོག་ཏུ་ཆོས་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མེད་པའི་མཚན་ཉིད་བསྟན་ཏོ། །

[Block 1094]
དེའི་འོག་ཏུ་ངོ་བོ་ཉིད་མེད་པའི་དོན་དེ་ལ་རྣལ་འབྱོར་དུ་བྱ་བའི་ཐབས་དེ་ལ་ཤིན་ཏུ་རྨོངས་པའི་གཉེན་པོར་དང་པོ་སེམས་བསྐྱེད་པ་དང་། ཆོས་གདགས་པ་རྣམ་པར་གཞག་པའི་གནས་དང་། རྟེན་གྱི་རྒྱུ་ལ་བརྟེན་ཏེ་ཞི་གནས་དང་། ལྷག་མཐོང་ལ་མཁས་པར་བྱ་དགོས་པས་འདིར་དེའི་འོག་ཏུ་ཆོས་གདགས་པ་རྣམ་པར་གཞག་པ་ལས་བརྩམས་ནས་རྣལ་འབྱོར་གྱིས༌[^874]ཡོངས་སུ་བསྡུས་པའི་ཞི་གནས་དང་། ལྷག་མཐོང་གི་ལམ་གྱི་རབ་ཏུ་དབྱེ་བ་བསྟན་ཏོ། །

[Block 1095]
དེའི་འོག་ཏུ་ཞི་གནས་དང་ལྷག་མཐོང་གི་ཐེག་པ་དེ་ཉིད་ཀྱི་སྤྱོད་པ༌[^875]དང་། རྟོག་པ་ལ་ཤིན་ཏུ་རྨོངས་པའི་གཉེན་པོར་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་ངེས་པའི་དོན་ལ་མཁས་པར་བྱ་དགོས་པས་འདིར་དེའི་འོག་ཏུ་ཐེག་པ་རྣམ་པར་གཞག་པ་ལས་བརྩམས་ནས༌[^876]ཐེག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རྣམ་པར་དབྱེ་བ་བསྟན་ཏོ། །

[Block 1096]
དེའི་འོག་ཏུ་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཐེག་པའི་འབྲས་བུ་ལ་ཤིན་ཏུ་ཉོན་མོངས༌[^877]པའི་གཉེན་པོར་དེ་བཞིན་གཤེགས་པའི་སྐུ་དང་གསུང་དང་ཐུགས་ཀྱི་མཚན་ཉིད་ལ་མཁས་པར་བྱ་དགོས་པས་འདིར་དེའི་འོག་ཏུ་ཐེག་པ་གདགས་པ་རྣམ་པར་གཞག་པ་ཁོ་ན་ལས་བརྩམས་ནས་དེ་བཞིན་གཤེགས་པའི་བྱ་བ་སྒྲུབ་པའི༌[^878]རབ་ཏུ་དབྱེ་བ་བསྟན་ཏེ། བདེ་བར་གཤེགས་པའི་བསྟན་པ་བདེ་བར་བགྲོད་པར་བྱ་བའི་ཆོས་འདི་ལ་ཡོངས་སུ་ཤེས་པར་བྱ་བ་ནི་དེ་ཙམ་དུ་ཟད་དེ། དེས་ཐེག་པ་ཆེན་པོ༌[^879]མཐའ་དག་བསྡུས་པར༌[^880]རིག་པར་བྱའོ། །

[Block 1097 [HEADING]]
#### འཕགས་པ་བློ་གྲོས་ཡངས་པའི་ལེའུ། ^4-2-1-0

[Block 1098]
དེ་ལ་དང་པོར་སེམས་ཀྱི་མཚན་ཉིད་ཀྱི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཡོངས་སུ་ཤེས་པར་བྱ་བའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། དེ་ནས་བཅོམ་ལྡན་འདས་ལ་བྱང་ཆུབ་སེམས་དཔའ་བློ་གྲོས་ཡངས་པས༌[^881]ཞུ་བ་ཞུས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་འཕགས་པ་བློ་གྲོས་ཡངས་པའི་ལེའུ་ལྔ་པ་འདི་གསུངས་སོ། །

[Block 1099]
དེ་ལ་ལེའུ་ལྔ་པ་འདིའི་བསྡུས་པའི༌[^882]དོན་ནི་མདོར་བསྡུ་ན་སེམས་ཀྱི་མཚན་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 1100]
དེ་ལ་རྣམ་པར་དབྱེ་ན་རྣམ་པ་གཉིས་ཏེ། ཡོངས་སུ་ཞུས་པ་དང་། རྒྱ་ཆེ་བར་བསྟན་ཏོ། །

[Block 1101]
དེ་ལ་ཡོངས་སུ་ཞུས་པ་ནི། བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དང་ཡིད་དང་རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པ་ཞེས་བྱ་བ་ནས། ཇི་ཙམ་གྱིས་འདོགས་ལགས་ཞེས་གསུངས་པའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 1102]
རྒྱ་ཆེར་བསྟན་པ་ནི་དེ་སྐད་ཅེས་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བྱང་ཆུབ་སེམས་དཔའ་བློ་གྲོས་ཡངས་པ་ལ་འདི་སྐད་ཅེས་བཀའ་སྩལ་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལེའུ་འདི་ཉིད་ཀྱི་གཞུང་ལྷག་མ་ཐམས་ཅད་ཀྱིས་བསྟན་ཏོ། །

[Block 1103 [HEADING]]
##### ཡོངས་སུ་ཞུས་པ། ^4-2-1-1-0

[Block 1104]
དེ་ལ་དང་པོར་ཡོངས་སུ་ཞུས་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། ཡོངས་སུ་ཞུས་པ་ཞེས་བྱ་བ་ནི་སེམས་ཀྱི་གསང་བ་ལ་ཤིན་ཏུ་རྨོངས་པའི་གཉེན་པོར་སེམས་དང་ཡིད་དང་རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པ༌[^883]གླེང་བསླང་བའི་ཕྱིར་དང་པོར༌[^884]བཅོམ་ལྡན་འདས་ལ་འཕགས་པ་བློ་གྲོས་ཡངས་པས་ཞུ་བ་ཞུས་པ་གང་ཡིན་པའོ། །

[Block 1105]
དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དང་ཡིད་དང༌[^885]རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1106]
དེ་ལ་སེམས་ཞེས་བྱ་བ་ནི་ཀུན་གཞིའི༌[^886]རྣམ་པར་ཤེས་པའོ། །

[Block 1107]
ཡིད་ཅེས་བྱ་བ་ནི་ཉོན་མོངས་པ་ཅན་གྱི༌[^887]ཡིད་དང་། འགགས་མ་ཐག་པ་དང་གནས་སུ་གྱུར་པའི་རྣམ་པར་ཤེས་པ་ལ་བྱའོ། །

[Block 1108]
རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་འཇུག་པའི་རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་གོ། །

[Block 1109]
གསང་བ་ཞེས་བྱ་བ་ནི་དེ་དག་གི་ངོ་བོ་དང་། གནས་དང་། དམིགས་པ་དང་། གྲོགས་དང་། ལས་དང་། དེའི་ཡོད་པ་ཉིད་དང་། རབ་ཏུ་དབྱེ་བ་ནི་འདི་ལས་ཕྱི་རོལ་པ་དག་དང་། ཆོས་འདི་དག་ལས་ཀྱང་ཁ་ཅིག༌[^888]མི་ཤེས་པ་དག་དེ་ལ་རང་བཞིན་གྱིས་ལྐོག་ཏུ་གྱུར་པའོ། །

[Block 1110]
མཁས་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་ལུགས་ཤེས་པ། སོ་སོར་རྟོག་པའི་ཡེ་ཤེས་ཀྱིས་དེའི་སྤྱོད་ཡུལ་གྱི་གསང་བ་ལ་མཁས་པ་ཡིན་ནོ། །

[Block 1111]
ལན་གཉིས་སུ་བཟླས་པ་ནི་གྲགས་པའི་དོན་བསྟན་པའི་ཕྱིར་རོ་ཞེས་བགྱི་ན་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་དེ༌[^889]དང་དེ་དག་ལས་དེ་སྐད་ཅེས་གསུངས་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1112 [HEADING]]
###### ངོ་བོ་ཉིད། ^4-2-1-1-1-0

[Block 1113]
དེ་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དང་ཡིད་དང་རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པ་ཞེས་བྱ་བ་ནི་དེ་དག་གི་ངོ་བོ་ཉིད་དང་། གནས་དང་། དམིགས་པ་དང་། གྲོགས་དང་། ལས་ཀྱི་མཚན་ཉིད་ལ་མཁས་པ་དང་། ཀུན་གཞིའི་རྣམ་པར་ཤེས་པའི་ཡོད་པ་ཉིད་དང་། རབ་ཏུ་དབྱེ་བ་ལ༌[^890]མཁས་པ་ཡིན་ནོ་ཞེས་བསྟན་པ་དེ་ལ། དེ་དག་གི་ངོ་བོ་ཉིད་གང་ཞེ་ན། སེམས་དང་། ཡིད་དང་། རྣམ་པར་ཤེས་པ་གང་ཡིན་པ་སྟེ། དེ་ལ་སེམས་ཞེས་བྱ་བ་ནི་ས་བོན་ཐམས་ཅད་དང་ལྡན་པ་གནས་ཀྱི་དངོས་པོར་གྱུར་པ། གནས་ཀྱི་དངོས་པོར་གནས་པ། ལེན་པར་བྱེད་པ། རྣམ་པར་སྨིན་པས་བསྡུས་པ་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པ་གང་ཡིན་པའོ། །

[Block 1114]
ཡིད་ཅེས་བྱ་བ་ནི་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་མ་རིག་པ་དང་། བདག་ཏུ་ལྟ་བ་དང་། ངའོ་སྙམ་པའི་ང་རྒྱལ་དང་། སྲེད་པའི་མཚན་ཉིད་ཀྱི་ཉོན་མོངས་པ་རྣམ་པ་བཞི་དང་རྟག་ཏུ་ལྡན་པ་གང་ཡིན་པ་དང་། རྣམ་པར་ཤེས་པ་རྣམས་འགགས་མ་ཐག་པ་གང་ཡིན་པའོ། །

[Block 1115]
ཡང་ན་ཡིད་ཅེས་བྱ་བ་ནི་གནས་སུ་གྱུར་པའི་རྣམ་པར་ཤེས་པ་ལ་བྱ་སྟེ། གནས་ཀྱང་རྣམ་པ་བཞི་སྟེ། ས་བོན་གྱི་གནས་ནི་ཀུན་གཞིའི་རྣམ་པར་ཤེས་པའོ། །

[Block 1116]
འབྱུང་བའི་སྒོ་འབྱེད་པའི་གནས་ནི་རྣམ་པར་ཤེས་པ་རྣམས་འགགས་མ་ཐག་པའོ། །

[Block 1117]
འཆིང་བའི་གནས་ནི་ཉོན་མོངས༌[^891]ཅན་གྱི་ཡིད་དེ། [^892]དེ་མ་འགགས་ན་རྣམ་པར་རིག་པའི་འཆིང་བ་ནི༌[^893]གྲོལ་བའི་ཕྱིར་རོ། །

[Block 1118]
ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བའི་གནས་ནི་ཡིད་ཀྱི༌[^894]རྣམ་པར་ཤེས་པ་སྟེ། འདོད་ཆགས་ལ་སོགས་པ་དང་། དད་པ་ལ་སོགས་པའི་གནས་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ལྟར་ན་ཡིད་ཅེས་བྱ་བའི་སྒྲས་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་བསྡུས་པ་ཡང་བསྟན་ཏོ། །

[Block 1119]
རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་དབང་པོ་ལ་བརྟེན་ནས་དམིགས་པ་རྣམ་པར་རིག་པར་བྱེད་པས་ཉེ་བར་གནས་པ་འཇུག་པའི་རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་པོ་དག་གོ། །

[Block 1120 [HEADING]]
###### གནས། ^4-2-1-1-2-0

[Block 1121]
དེ་དག་གི་གནས་གང་ཞེ་ན། ཀུན་གཞིའི༌[^895]རྣམ་པར་ཤེས་པ་དང་། ཉོན་མོངས་པ་ཅན་གྱི༌[^896]ཡིད་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་གནས་ནི་གཉིས་ཏེ། ས་བོན་གྱི་གནས་ནི་ཀུན་གཞིའི༌[^897]རྣམ་པར་ཤེས་པ་ཉིད་དོ། །

[Block 1122]
དེ་མ་ཐག་པའི་གནས་ནི་ཡིད༌[^898]དོ། །

[Block 1123]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་གནས་ནི་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ཀྱང་ཡིན་ཏེ། འདི་ལྟར་དེ་མ་འགགས་ན་རྣམ་པར་རིག་པའི་འཆིང་བ་མི་འགྲོལ༌[^899]ལ། འགགས་ན་དེ་འགྲོལ་བའི་ཕྱིར་རོ། །

[Block 1124]
སྒོ་ལྔའི་རྣམ་པར་ཤེས་པའི་གནས་ནི་གསུམ་སྟེ། དབང་པོ་ནི་ལྷན་ཅིག་བྱུང་བའི་གནས་སོ། །

[Block 1125]
ཡིད་ནི་དེ་མ་ཐག་པའི་གནས་སོ། །
--- END BLOCKS ---
