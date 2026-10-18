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
[Block 1331]
ཆོས་ཀྱི་རྣམ་གྲངས་དེ་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྡེ་སྣོད་ཀྱིས་བསྡུས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྡེ་སྣོད་ནི་ཐེག་པ་ཆེན་པོའི་ཆོས་ཐམས་ཅད་དོ། །

[Block 1332]
ས་བཅུ་པའི་ཆོས་ཀྱི་རྣམ་གྲངས་འདི་ཡང་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྡེ་སྣོད་ཉིད་ཡིན་གྱི་ཉན་ཐོས་ཀྱི་ནི་མ་ཡིན་ནོ། །

[Block 1333]
དེ་བསྡུས་པ་ཉིད་ཀྱི་ཡང༌[^868]ཕྱིར་ན་ཡང་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་བསྒོམ་པ༌[^869]ནི་ས་ཐམས་ཅད་ལ་འབྱུང་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1334]
སངས་རྒྱས་ཀྱི་ཞིང་རབ་འབྱམས་ཐམས་ཅད་དུ་སངས་རྒྱས་བྱུང་བ་ཐམས་ཅད་ཀྱིས་ཀྱང་རབ་ཏུ་བསྒོམས་པ་ཡིན་པའི༌[^870]ཕྱིར་ས་འདི་རྣམས་ནི་ཤིན་ཏུ་མཆོག་ཏུ་གྱུར་པ་ཉིད་ཡིན་པའི་ཕྱིར་ཆོས་ཀྱི་རྣམ་གྲངས་དེ་ནི་ཡུལ་གྱི་མཆོག་ཉིད་དུ་བསྟན་ལ་དང་པོར་བསྟན་པ་ཡང་ཡིན་ནོ། །

[Block 1335]
ཡང་ཡུལ་དེ་ནི་ཤིན་ཏུ་གནས་པར༌[^871]གྱུར་པ་ཡིན་པ་དང་། ཉེ་བ་ན་གནས་པའི་ཡུལ་གཞན་གྱི་གཙོ་བོར་གྱུར་པ་ཉིད་ཀྱིས་དེ་ནི་མཆོག་ཡིན་ནོ། །

[Block 1336 [HEADING]]
### གང་ཟག་ལྔ་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱིས་རྫོགས་པ། ^5-5-0

[Block 1337]
གང་ཟག་ལྔ་ནི་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱིས་རྫོགས་པར་འགྱུར་ཏེ་ཞེས་བྱ་བ་ལ། དེ་ལ་རེ་ཞིག་མོས་པས༌[^872]སྤྱོད་པས་ན་མོས་པས༌[^873]སྤྱོད་པ་སྟེ། དེ་ནི་མོས་པས༌[^874]སྤྱོད་པའི་ས་བསྐལ་པ་གྲངས་མེད་པ་གཅིག་གིས་རྫོགས་པར་འགྱུར་རོ། །

[Block 1338]
གང་ཡོངས་སུ་རྫོགས་པས་ནི་ལྷག་པའི་བསམ་པ་རྣམ་པར་དག་པ་དང་། དེ་ཁོ་ན་ཉིད་སོ་སོར་རིག་པར་འགྱུར་རོ། །

[Block 1339]
དེ་ནི་ཡང་ས་བཅུ་པོ་ཐམས་ཅད་དུ་ལྷག་པའི་བསམ་པ་རྣམ་པར་དག་པས་སྤྱོད་པར་འགྱུར་རོ། །

[Block 1340]
དེ་ནི་ཡང་ས་དྲུག་པ༌[^875]ལ་ནི་མཚན་མ་དང་བཅས་པར་སྤྱོད་དོ། །

[Block 1341]
བདུན་པ་ལ་ནི་མཚན་མ་མེད་པར་སྤྱོད་ཅིང་མངོན་པར་འདུ་བྱེད་པ་དང་བཅས་པ་ཡིན་ཏེ། གྲངས་མེད་པ་གཉིས་པས་གྲུབ་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1342]
བརྒྱད་པ་ལ་ཞུགས་པ་ནི་མངོན་པར་འདུ་བྱེད་པ་མེད་པ་ཡིན་ཏེ། མངོན་པར་འདུ་བྱེད་པ་མེད་པ་ལ་སྤྱོད་པ་ཡོངས་སུ་རྫོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1343]
མངོན་པར་འདུ་བྱེད་པ་མེད་པ་ལ་སྤྱོད་པ་ཡོངས་སུ་རྫོགས་པ་ཉིད་ནི་དགུ་པ་དང་བཅུ་པ་ལ་ཡིན་ཏེ།[^876] གང་ཟག་དེའི་ནི་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་པས་སོ། །

[Block 1344]
དེ་ལྟ་བུ་དག་ནི་གང་ཟག་གཅིག་ལ་རྒྱུན་དུ་ཞུགས་པ་དང་། ལན་ཅིག་ཕྱིར་འོང་བ་དང་། ཕྱིར་མི་འོང་བ་རྣམ་པར་གཞག་པ་བཞིན་དུ་རྣམ༌[^877]པར་གཞག་པའི་ཁྱད་པར་གཞན་རྣམ་པ་ལྔར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1345 [HEADING]]
### བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གང་ནས་བརྩམས་པ། ^5-6-0

[Block 1346]
གང་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱིས་བྱང་ཆུབ་སེམས་དཔའ་བསྒོམ་པ་རྫོགས་པར་འགྱུར་ཞེས་བསྟན་པ་དེ་ཐོག་མ་མེད་པའི་དུས་ནས་འཁོར་བ་ན་གནས་པའི་ཚེ་སྦྱིན་པ་ལ་སོགས་པ་བྱིན་པས་ཀྱང་འདི་ལྟར་སངས་རྒྱས་འབྱུང་བ་དང་ཕྲད་པར་གྱུར་པས་གང་དེ་ལྟ་བུའི་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་པོ་དེ་དང་པོ་གང་ནས་བརྩམས་ནས་བསྟན་པ་ཡིན་ཞེ་ན། དེ་ཚིགས་སུ་བཅད་པས་བསྟན་པར་བྱ་སྟེ། བཟང་དང་སྨོན་པའི་སྟོབས་ཅན་དང་། །ཞེས་བྱ་བ་ནི། དགེ་བའི་རྩ་བའི་སྟོབས་ཅན་དུ་འགྱུར་བ་དང་། སྨོན་ལམ་གྱི་སྟོབས་ཅན་དུ་འགྱུར་བའོ། །

[Block 1347]
དེ་ལ་དགེ་བའི་རྩ་བའི་སྟོབས་ཅན་ནི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་ཟིལ་གྱིས་གནོན་པར་མི་ནུས་པར་བལྟ་བར་བྱའོ། །

[Block 1348]
སྨོན་ལམ་གྱི་སྟོབས་ཀྱིས་ནི་རྟག་ཏུ་དགེ་བའི་བཤེས་གཉེན་དང་ཕྲད་པ་ཡིན་པར་བལྟ་བར་བྱའོ། །

[Block 1349]
སེམས་བརྟན་ཁྱད་པར་འགྲོ་བ༌[^878]ཞེས་བྱ་བ་ནི། སེམས་བསྐྱེད་པ་བརྟན་པ་ཅན་དུ་འགྱུར་བ་དང་ཁྱད་པར་དུ་འགྲོ་བར་འགྱུར་བའོ། །

[Block 1350]
དེ་ལ་སེམས་བསྐྱེད་པ་བརྟན་པ་ནི། དགེ་བའི་བཤེས་གཉེན་གྱི་དབང་གིས་བྱང་ཆུབ་ཀྱི་སེམས་ཡོངས་སུ་མི་གཏོང་བར་བལྟ་བར་བྱའོ། །

[Block 1351]
ཁྱད་པར་དུ་འགྲོ་བ་ཉིད་ནི་སྐྱེ་བ་གཞན་དང་གཞན་དུ་མཐོང་བའི་ཆོས་ཉིད་ལ་དགེ་བ་རྣམས་འཕེལ་བར་འགྱུར་ཞིང་ཉམས་པར་མི་འགྱུར་བར་བལྟ་བར་བྱའོ། །

[Block 1352]
ལྷག་མ་ནི་གོ་སླའོ། །

[Block 1353 [HEADING]]
## ལྷག་པའི་ཚུལ་ཁྲིམས། ^6-0

[Block 1354 [HEADING]]
### རབ་ཏུ་དབྱེ་བའི་ཁྱད་པར། ^6-1-0

[Block 1355]
ཇི་ལྟར་བྱས་ན་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བསླབ་པ་ཉན་ཐོས་ལ་སོགས་པ་དག་ལས་ཁྱད་པར་དུ་འཕགས་པ་ཡིན་ཞེ་ན། རབ་ཏུ་དབྱེ་བའི་ཁྱད་པར་དང་། །ཞེས་བྱ་བ་ལ། འདི་ལྟར་ཉན་ཐོས་རྣམས་ལ་ནི་སྡོམ་པའི་ཚུལ་ཁྲིམས་གཅིག་པུ་ཡོད་ཀྱི་དགེ་བའི་ཆོས་སྡུད༌[^879]པའི་ཚུལ་ཁྲིམས་ཀྱང་མ་ཡིན། སེམས་ཅན་གྱི་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས་ཀྱང་མ་ཡིན་ནོ། །

[Block 1356 [HEADING]]
### ཐུན་མོང་དང་ཐུན་མོང་མ་ཡིན་པའི་ཁྱད་པར། ^6-2-0

[Block 1357]
ཐུན་མོང་དང་ཐུན་མོང་མ་ཡིན་པའི་ཞེས་བྱ་བ་ལ། དེ་ལ་རང་བཞིན་གྱིས༌[^880]ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་སྲོག་གཅོད་པ་ལ་སོགས་པ་ནི་ཐུན་མོང་གིའོ། །

[Block 1358]
ས་བརྐོ་བ་དང་རྩྭ་གཅོད་པ་ལ་སོགས་པ་ནི་ཐུན་མོང་མ་ཡིན་པ་སྟེ། གང་ཡང་བཅས་པའི་ཁ་ན་མ་ཐོ་བའི་བསླབ་པ་ཕྱི་མ་རྣམས་སོ། །

[Block 1359]
ཉན་ཐོས་ཀྱི་ལྟུང་བར་འགྱུར་བ་དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་དབྱར་གྱི་ནང་དུ་ཉན་ཐོས་རྣམས་སོང་བར་གྱུར་ན་ལྟུང་བ་ཡིན་ནོ། །

[Block 1360]
སེམས་ཅན་གྱི་དོན་མཐོང་ལ་མ་སོང་ན་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ལྟུང་བ་ཡིན་ལ། སོང་ན་ནི་ལྟུང་བ་མེད་དོ། །

[Block 1361]
ཁ་ན་མ་ཐོ་བ་མེད་པར་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་འདོགས་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཐམས་ཅད་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པས་ཕན་འདོགས་པར་བྱེད་ཀྱི། ཇི་ལྟར་བུད་མེད་ཁྱེར་ལ་ཤོག་ཅེས་བྱ་བ་ལྟ་བུས་ནི་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་ཡང་དེ་ནི་གཞན་གྱིས་ཡོངས་སུ་གཟུང་བ༌[^881]ཡིན་པས་ཁ་ན་མ་ཐོ་བ་མེད་པར་ཡང་ཇི་ལྟར་འགྱུར། དེ་བས་ན་དེ་དང་འདྲ་བའི་དོན་གཞན་ཡང་ཡོངས་སུ་སྤངས་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པས་ཕན་གདགས་པར་བྱའོ། །

[Block 1362]
སེམས་ཀྱི་ལྟུང་བ་ཞེས་བྱ་བ་ནི་གང་འདོད་པ་དང་གནོད་སེམས་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ལྟུང་བ་ཡིན་གྱི། ཉན་ཐོས་རྣམས་ཀྱི་ནི་མ་ཡིན་ནོ། །

[Block 1363]
ལྷག་པའི་ཚུལ་ཁྲིམས་ཀྱི་བསླབ་པ་ལ་སོགས་པ་གསུམ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ངོ་བོ་ཉིད་ཡིན་ན། ཅིའི་ཕྱིར་དེ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས་ཐ་དད་དུ་རྣམ་པར་གཞག་པར་བྱ་ཞེ་ན། གང་གི་ཕྱིར་ཐ་དད་དུ་རྣམ་པར་གཞག་པར་བྱ་བ་དེ་བསྟན་པར་བྱ་སྟེ། འདི་ལྟར་བསླབ་པ་རྣམས་ཕན་ཚུན་རྒྱུའི་ངོ་བོ༌[^882]རྣམ་པར་གཞག་པར་བྱ་སྟེ། ཚུལ་ཁྲིམས་ལ་བརྟེན་ནས་ནི། བསམ་གཏན་བསྐྱེད་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1364]
བསམ་གཏན་ལ་བརྟེན་ནས་ནི་ཤེས་རབ་བསྐྱེད་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1365 [HEADING]]
### རྒྱ་ཆེ་བ་ཉིད་ཀྱི་ཁྱད་པར། ^6-3-0

[Block 1366]
སྣ་ཚོགས་དང་ཚད་མེད་པའི་བསླབ་པ་རྒྱ་ཆེ་བ་ཞེས་བྱ་བ་ནི། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བསླབ་པ་སྣ་ཚོགས་པ་དང་ཚད་མེད་པ་སྟེ། གང་གི་ཕྱིར་དེས་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པ་དང་། དེ་དག་ལ་ཕན་འདོགས་པ་ནི་དགོངས༌[^883]པའོ། །

[Block 1367]
བསོད་ནམས་ཚད་མེད་པ་ཡོངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་དེས་སེམས་ཅན་ཚད་མེད་པའི༌[^884]བསོད་ནམས་ཀྱི་ཚོགས་ཡོངས་སུ་འཛིན་གྱི་ཉན་ཐོས་རྣམས་ཀྱིས༌[^885]ནི་མ་ཡིན་ནོ། །

[Block 1368]
སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པ་དང་བདེ་བར་བྱ་བའི་བསམ་པ་ཡོངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་དེ་ལ་ཕན་པ་ལ་འགོད་པ་ནི་ཕན་པའི་བསམ་པའོ། །

[Block 1369]
གང་དགེ་བའི་རྩ་བ་འདི་ལ་འབྲས་བུ་ཅི་ཡོད་པ་དེ་གང་ཟག་འདིས་ཐོབ་པར་གྱུར་ཅིག་ཅེས་བྱ་བ་ནི་བདེ་བའི་བསམ་པའོ། །

[Block 1370]
བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ལ་བརྟེན་པ་རྒྱ་ཆེ་བ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་ཚུལ་ཁྲིམས་འདི་ནི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཀྱི་རྟེན་དུ་འགྱུར་གྱི་ཉན་ཐོས་རྣམས་ཀྱི་ནི་མ་ཡིན་ནོ།། །།
--- END BLOCKS ---
