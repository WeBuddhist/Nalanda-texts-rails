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

[Block 1371]
བམ་པོ་དྲུག་པ།

[Block 1372 [HEADING]]
### ཟབ་པ་ཉིད་ཀྱི་ཁྱད་པར། ^6-4-0

[Block 1373]
ཟབ་པ་ཉིད་ནི་གང་བྱང་ཆུབ་སེམས་དཔའ་ཐབས་ལ་མཁས་པའི་རྣམ་པ་དེ་ལྟ་བུས་ཞེས་བྱ་བ་དེ་ལ། བྱང་ཆུབ་སེམས་དཔའ་ཇི་ལྟ་བ་དེ་ལྟ་བུའི་ཐབས་ལ་མཁས་པའི་རྣམ་པའི་ནུས་པ་ཅན་དུ་འགྱུར་བ་དེ་བསྟན་པར་བྱ་སྟེ། གལ་ཏེ་རེ་ཞིག་འདི་ལྟར་ཤེས་ཏེ། གང་ཟག་འདི་ནི་འདིར་མི་དགེ་བ་མཚམས་མེད་པ་ལ་སོགས་པ་དང་ལྡན་པར་བྱའོ༌[^886]ཞེས་གལ་ཏེ་ཕ་རོལ་གྱི་སེམས་ཤེས་པར་གྱུར་ན། གལ་ཏེ་དེ་ལས་བཟློག་པར་བྱ་བའི་ཐབས་གཞན་མེད་ན། འདི་ངེས་པར་འདི་ལྟར་བསད་ན་ནི་བདེ་འགྲོར་འགྲོ་བར་འགྱུར་ལ། ངེས་པར་ལས་འདི་བྱས་ན་ནི་ངེས་པ་ཁོ་ནར་ངན་འགྲོར་འགྲོ་བར་འགྱུར་བར་ཤེས་ཤིང་དེ་ལྟ་བུར་རིག་པར་གྱུར་ན། གང་འདི་ལྟར་སེམས་བསྐྱེད་པར་བྱ་སྟེ། འདི་ལྟར༌[^887]ཡང་བདག་གིས་ལས་འདི་བྱས་པས་བདག་ངན་སོང་དུ་འགྲོ་བ་དེ་ནི་འདོད་ཀྱི། འདི་ད་ལྟར་གྱི་སྡུག་བསྔལ་ཅུང་ཟད་ལ་སྦྱར་བས་མ་འོངས་པའི་བདེ་བ་ཐོབ་པར་འགྱུར་བར་བྱའོ་ཞེས་དེས་འདི་ལྟར་སྨན་པ་དང་འདྲ་བའི་སེམས་བསྐྱེད་ནས་བསད་པར་གྱུར་ཀྱང་བསོད་ནམས་མ་ཡིན་པ་མེད་ཀྱི། བསོད་ནམས་ཉིད་མང་དུ་འཕེལ་བར་འགྱུར་ཏེ། གང་བསོད་ནམས་ཉིད་མང་དུ་འཕེལ་བར་འགྱུར་བ་དེས་ན་མྱུར་དུ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་རྗེས་སུ་ཐོབ་པར་འགྱུར་བ་སྟེ། འདི་ལྟ་བུ་ནི་ཤིན་ཏུ་ཟབ་པའོ། །

[Block 1374]
གང་ཡང་སྤྲུལ་པའི་ལུས་དང་ངག་གི་ལས་ཀྱང་བྱང་ཆུབ་སེམས་དཔའི་ཟབ་པའི་ཚུལ་ཁྲིམས་སུ༌[^888]རིག་པར་བྱ་སྟེ། དེས་རྒྱལ་སྲིད་ཀྱང་བྱེད་ཅིང་སེམས་ཅན་ལ་གཙེ་བ༌[^889]སྣ་ཚོགས་བསྟན་ནས་སེམས་ཅན་འདུལ་བ་ལ་འགོད་དོ་ཞེས་བྱ་བ་ལ། གང་ཡང༌[^890]སྤྲུལ་པའི་ངོ་བོ་ཉིད་ནི་སྤྲུལ་པ་སྟེ། འདི་ལྟར་དེ་ཡང་རྒྱལ་པོ་མེ་ཡིས་གཞོན་ནུ་ནོར་བཟངས༌[^891]ལ་ཇི་ལྟར་བསྟན་པ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 1375]
སྐྱེས་པའི་རབས་སྣ་ཚོགས་བསྟན་པས་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཐམས་ཅད་སྒྲོལ་གྱི་སྐྱེས་པའི་རབས་འབྱུང་བ་ལྟ་བུ་སྟེ། དེར་བྱང་ཆུབ་སེམས་དཔས་བྲམ་ཟེ་ལ་བུ་སྦྱིན་པར་གཏོང་བ༌[^892]དེ་ནི་སྤྲུལ་པ་ཡིན་ཏེ། སེམས་ཅན་གཞན་ལ་གནོད་པ་བྱེད་པས་སེམས་ཅན་གཞན་ལ་ཕན་འདོགས་པ་ནི་མ་ཡིན་ན༌[^893]ཡང་། གང་གི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་ཅན་གཞན་ལ་གནོད་པ་བྱས་ནས་སེམས་ཅན་གཞན་ལ་ཕན་འདོགས་པར་བྱེད་པ་འདི་ལྟ་བུ་ནི་ཟབ་པ་ཡིན་ནོ། །

[Block 1376]
ཁྱད་པར་རྣམ་པ་བཞི་པོ་དེ་དག་ཉིད་ནི་ཡང་འདུལ་བ་བསྒྲགས་པ་ཞེས་བྱ་བ་ཤིན་ཏུ་རྒྱས་པའི་མདོ་སྡེ་ལས་བརྒྱ་སྟོང་དུ་མར་བསྟན་ཏོ། །

[Block 1377 [HEADING]]
## ལྷག་པའི་སེམས། ^7-0

[Block 1378 [HEADING]]
### དམིགས་པས་རབ་ཏུ་དབྱེ་བ། ^7-1-0

[Block 1379]
ལྷག་པའི་སེམས་ལས་བརྩམས་ནས་ཐེག་པ་ཆེན་པོའི་ཆོས་ལས༌[^894]དམིགས་པ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཐེག་པ་ཆེན་པོའི་ཆོས་ལ་དམིགས་ཀྱི། ཉན་ཐོས་རྣམས་ནི་མ་ཡིན་ནོ། །

[Block 1380 [HEADING]]
### སྣ་ཚོགས་ཉིད་ཀྱིས་རབ་ཏུ་དབྱེ་བ། ^7-2-0

[Block 1381]
ཐེག་པ་ཆེན་པོ་སྣང་བ་དང་། བསོད་ནམས་ཐམས་ཅད་ཡང་དག་པར་བསགས་པ་དང་། ཏིང་ངེ་འཛིན་གྱི་རྒྱལ་པོ་ཞེས་བྱ་བ་ལ། ཏིང་ངེ་འཛིན་སྨོས་པ་ནི་འདི་ལྟ་བུའི་ཏིང་ངེ་འཛིན་སྣ་ཚོགས་ལས་གང་གི་ཕྱིར་ཉན་ཐོས་རྣམས་ལ་ནི་གཅིག་ཙམ་ཡང་མེད་དོ། །

[Block 1382 [HEADING]]
### གཉེན་པོས་རབ་ཏུ་དབྱེ་བ། ^7-3-0

[Block 1383]
གཉེན་པོས་རབ་ཏུ་དབྱེ་བ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་སྒྲིབ་པ་ཐམས་ཅད་ཀྱི་གཉེན་པོར་རྣམ་པར་གནས་པ་སྟེ། ཇི་ལྟར་ཁྱེའུ་རགས་པ་ནི་ཕྲ་མོས༌[^895]འབྱིན་པར་བྱེད་པ་དེ་བཞིན་དུ་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལ་རྣམ་པར་གནས་པའི་ཀུན་ནས་ཉོན་མོངས་པའི་ས་བོན་བག་ཆགས་ཞེས་བྱ་བ་རགས་པ་ནི་གཉེན་པོ་ཕྲ་མོས་འབྱིན་པར་བྱེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1384 [HEADING]]
### ལས་སུ་རུང་བ་ཉིད་ཀྱིས་རབ་ཏུ་དབྱེ་བ། ^7-4-0

[Block 1385]
ལས་སུ་རུང་བ་ཉིད་ཀྱིས་རབ་ཏུ་དབྱེ་བ་ཞེས་བྱ་བ༌[^896]ནི་ལས་སུ་རུང་བ་བསམ་གཏན་གང༌[^897]ལ་བདེ་བར་གནས་ན༌[^898]གང་དུ་སེམས་ཅན་གྱི་དོན་མཐོང་བ་དེར་སྐྱེ་བར་འགྱུར་བ་སྟེ། དེར་ཡང་བསམ་གཏན་ཉམས་པར་མི་འགྱུར་རོ། །

[Block 1386]
དེ་ལྟ་བུ་ནི་ཉན་ཐོས་རྣམས་ལ་མེད་དོ། །

[Block 1387 [HEADING]]
### མངོན་པར་སྒྲུབ་པས་རབ་ཏུ་དབྱེ་བ། ^7-5-0

[Block 1388]
མངོན་པར་སྒྲུབ་པས་རབ་ཏུ་དབྱེ་བ་དང་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་དུ་ཐོགས་པ་མེད་པ་ནི་མངོན་པར་ཤེས་པ་བསམ་གཏན་གྱིས་མངོན་པར་སྒྲུབ་པར་བྱེད་པའོ། །

[Block 1389 [HEADING]]
### ལས་ཀྱིས་རབ་ཏུ་དབྱེ་བ། ^7-6-0

[Block 1390 [HEADING]]
#### རྫུ་འཕྲུལ་ཆེན་པོ་མངོན་པར་སྒྲུབ་པ། ^7-6-1-0

[Block 1391]
ལས་ཀྱིས་རབ་ཏུ་དབྱེ་བ་ཞེས་བྱ་བ་ལ། གཡོ་བར་བྱེད་པ་ནི་འཇིག་རྟེན་གྱི་ཁམས་རྣམས་གཡོ་བར་བྱེད་པའོ་འབར་བར་བྱེད་པ་ནི་དེ་དག་ཉིད་འབར་བར་བྱེད་པའོ། །

[Block 1392]
ཁྱབ་པར་བྱེད་པ་ནི་འོད་ཀྱིས་ཁྱབ་པར་བྱེད་པར་བལྟ་བར་བྱའོ། །

[Block 1393]
སྟོན་པ་ནི་གང་གཞན་གྱིས་མི་ནུས་པ་དེའི་འོད་ཀྱིས་གཞན༌[^899]འཇིག་རྟེན་གྱི་ཁམས་དུ་མའི་སངས་རྒྱས་ལ་སོགས་པ་མཐོང་བར་བྱེད་པའོ། །

[Block 1394]
གཞན་གྱི་དངོས་པོར་བསྒྱུར་བ་ནི་ས་ལ་སོགས་པ་རྣམས་ཆུ་ཉིད་ལ་སོགས་པར་བསྒྱུར་བར་བལྟ་བར་བྱའོ། །

[Block 1395]
འགྲོ་བ་ནི་སྐད་ཅིག་གཅིག་ལ་འཇིག་རྟེན་གྱི་ཁམས་དུ་མར་འགྲོ་བའོ། །

[Block 1396]
འོང་བ་ཉིད་ནི་དེ་དག་ཉིད་ནས་སོ། །

[Block 1397]
སྡུད་པ་ནི་རྡུལ་ཕྲ་རབ་གཅིག་གི་ནང་དུ་འཇིག་རྟེན་གྱི་ཁམས་དུ་མ་ཆུད་པར་བྱས་ན་ཡང་དེ་ལ་འཕེལ་བ་མེད་པའོ། །

[Block 1398]
རྒྱས་པར་བྱེད་པ་ནི་རྡུལ་ཕྲ་རབ་གཅིག་གིས་འཇིག་རྟེན་གྱི་ཁམས་ཚད་མེད་པ་རྣམས་འགེངས་པར་བྱེད་པའོ། །

[Block 1399]
གཟུགས་ཐམས་ཅད་ལུས༌[^900]སུ་འཇུག་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ལུས་ལ་བྱ་བ་རྣམ་པ་སྣ་ཚོགས་སུ་དུ༌[^901]མ་ཐམས་ཅད་སྟོན་པའོ། །

[Block 1400]
སྐལ་པ་མཉམ་པས་འགྲོ་བ་ནི་ཇི་ལྟར་གདུལ་བྱའི་དོན་དུ་སུམ་ཅུ་རྩ་གསུམ་པ་རྣམས་ལ་ཁ་དོག་དང་དབྱིབས་དག་དེ་དང་མཐུན་པས་མཉམ་པར་འགྲོ་བ་སྟེ། དེ་བཞིན་དུ་ཐམས་ཅད་དུ་སྦྱར་རོ། །

[Block 1401]
སྣང་བར་བྱེད་པ་ནི་རབ་ཏུ་གསལ་བར་བྱེད་པའོ། །

[Block 1402]
མི་སྣང་བར་བྱེད་པ་ནི་རབ་ཏུ་མི་སྣང་བའོ། །

[Block 1403]
དབང་ཉིད་དུ་བྱེད་པ་ནི་ཇི་ལྟར་བདུད་སངས་རྒྱས་ཉིད་དུ་བྱེད་པ་ལྟ་བུའོ། །

[Block 1404]
གཞན་གྱི་རྫུ་འཕྲུལ་རབ་ཏུ་འཇོམས་པ་ནི་གཞན་གྱི་རྫུ་འཕྲུལ་ཟིལ་གྱིས་གནོན་པར་བྱེད་པའོ། །

[Block 1405]
སྤོབས་པ་སྦྱིན་པ་ནི་འདྲི་བ་ཉིད་ལའོ། །
--- END BLOCKS ---
