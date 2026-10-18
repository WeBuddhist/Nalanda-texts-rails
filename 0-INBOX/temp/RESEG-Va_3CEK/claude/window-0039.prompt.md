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
[Block 1366 [HEADING]]
### ཕྲ་རྒྱས་དྲུག། ^2-1-0

[Block 1367]
ཕྲ་རྒྱས་དེ་དག་ཀྱང་དུ་ཞིག་ཅེ་ན། མདོར་བསྡུས༌[^953]ན། དྲུག་དྲུག་གང་ཞེ་ན།

[Block 1368 [VERSE]]
འདོད་ཆགས་དེ་བཞིན་ཁོང་ཁྲོ་དང་། །
ང་རྒྱལ་མ་རིག་ལྟ་བ་དང་། །

[Block 1369]
ཐེ་ཚོམ་ཡིན་ཏེ། དེ་བཞིན་ཞེས་སྨོས་པ༌[^954]ནི་འདོད་ཆགས་ཀྱི་དབང་གིས་གཞན་དག་དམིགས་པ་ལས༌[^955]རྒྱས་པར་གྱུར་པ་ཉིད༌[^956]ཤེས་པར་བྱ་བའི་ཕྱིར་ཏེ། དེ་ནི་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 1370 [HEADING]]
### ཕྲ་རྒྱས་བདུན། ^2-2-0

[Block 1371]
དེ་དྲུག་ཀྱང་། འདོད་ཆགས་དབྱེ་བས་བདུན་དུ་བཤད། །ཕྲ་རྒྱས་དྲུག་པོ་དེ་དག་ཀྱང་མདོ་ལས་འདོད་ཆགས་ཕྱེ་ནས་བདུན་དུ་བཤད་དེ། འདོད་པའི་འདོད་ཆགས་ཀྱི་ཕྲ་རྒྱས་དང་། ཁོང་ཁྲོ་བའི་ཕྲ་རྒྱས་དང་། སྲིད་པའི་འདོད་ཆགས་ཀྱི་ཕྲ་རྒྱས་དང་། ང་རྒྱལ་གྱི་ཕྲ་རྒྱས་དང་། མ་རིག་པའི་ཕྲ་རྒྱས་དང་། ལྟ་བའི་ཕྲ་རྒྱས་དང་། ཐེ་ཚོམ་གྱི་ཕྲ་རྒྱས་སོ། །

[Block 1372 [HEADING]]
### ཕྲ་རྒྱས་མཚུངས་པར་ལྡན་པ། ^2-3-0

[Block 1373]
ཇི་ལྟར་ཤེས་པར་བྱ། འདོད་པའི་འདོད་ཆགས་ཉིད་ཕྲ་རྒྱས་ཡིན་པས་འདོད་པའི་འདོད་ཆགས་ཀྱི་ཕྲ་རྒྱས་ཡིན་ནམ། འོན་ཏེ་འདོད་པའི་འདོད་ཆགས་ཀྱི་ཕྲ་རྒྱས་ཡིན། དེ་ལས་ཅིར་འགྱུར། གལ་ཏེ་འདོད་པའི་འདོད་ཆགས་ཉིད་ཕྲ་རྒྱས་ཡིན་ན་ནི། འདི་ན་ལ་ལས༌[^957]འདོད་པའི་འདོད་ཆགས་ཀྱིས༌[^958]ཀུན་ནས་དཀྲིས་པའི་སེམས་ཀྱི་ལས༌[^959]མང་དུ་མི་གནས་ལ། འདོད་པའི་འདོད་ཆགས་ཀྱིས༌[^960]ཀུན་ནས་དཀྲིས་པ༌[^961]བྱུང་ན་ཡང་ཕྱིས་ངེས་པར་འབྱུང་བ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་རབ་ཏུ་ཤེས་ཤིང་། དེའི་འདོད་པའི་འདོད་ཆགས་ཀྱིས༌[^962]ཀུན་ནས་དཀྲིས་པ་དེའི་མཐུས་ཡང་དག་པར་ཤིན་ཏུ༌[^963]ཀུན་ནས་འཇོམས་ཤིང་ཕྲ་རྒྱས་དང་བཅས་པར་སྤོང་བར་བྱེད་དོ་ཞེས་གསུངས་པའི་མདོ་དང་འགལ་ལོ། །

[Block 1374]
གལ་ཏེ་དེ༌[^964]འདོད་པའི་འདོད་ཆགས་ཀྱི་ཕྲ་རྒྱས་ཡིན་ན་ནི་ཕྲ་རྒྱས་ལྡན་པར༌[^965]མ་ཡིན་པར་ཐལ་བར་འགྱུར་བས་འདོད་པའི་འདོད་ཆགས་ཀྱི་ཕྲ་རྒྱས་ནི་དབང་པོ་གསུམ་དང་མཚུངས་པར་ལྡན་པ་ཡིན་ནོ་ཞེས་འབྱུང་བའི་ཆོས་མངོན་པ་དང་འགལ་ལོ། །

[Block 1375]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་འདོད་པའི་འདོད་ཆགས་ཉིད་ཕྲ་རྒྱས་ཡིན་ཏེ། ཐེ་ཚོམ་ཉིད་ཕྲ་རྒྱས་ཡིན་པའི་བར་དུ་ཡང་དེ་དང་འདྲའོ་ཞེས་ཟེར་རོ། །

[Block 1376]
དེ་ལྟ་ན་མདོ་དང་འགལ་ལོ་ཞེས་བཤད་པ་མ་ཡིན་ནམ། འགལ་བ་མེད་དེ། ཕྲ་རྒྱས་དང་བཅས་པ་ནི་རྗེས་སུ་འབྲེལ་བ་དང་བཅས་པ་ཞེས་བྱ་བའི་དོན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1377]
ཡང་ན་མདོ་ལས་ཕྲ་རྒྱས་ཞེས་བྱ་བའི་སྒྲ་འབྱུང་བ་ནི་ཐོབ་པ་ལ་ཉེ་བར་བཏགས་པ་ཡིན་ཏེ། དཔེར་ན་མེ་སྡུག་བསྔལ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 1378]
ཆོས་མངོན་པ་ལས་ཕྲ་རྒྱས་ཞེས་བྱ་བའི་སྒྲ་འབྱུང་བ་ནི་ཉོན་མོངས་པ་ཁོ་ན་ལ་མཚན་ཉིད་པ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་ཕྲ་རྒྱས་རྣམས་ནི་མཚུངས་པར་ལྡན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1379]
འདི་ཇི་ལྟར་ཤེས་ཤེ་ན། ཕྲ་རྒྱས་རྣམས་ནི།

[Block 1380 [VERSE]]
སེམས་ནི་ཉོན་མོངས་བྱེད༌[^966]ཕྱིར་དང་། །
སྒྲིབ་ཕྱིར་དགེ་དང་འགལ་ཕྱིར་དང་། །

[Block 1381]
གང་གི་ཕྱིར༌[^967]ཕྲ་རྒྱས་རྣམས་ཀྱི༌[^968]སེམས་ཉོན་མོངས་པ་ཅན་དུ་འགྱུར་བ་དང་། སྔོན་མེད་པའི་དགེ་བ་མི་སྐྱེ་བ་དང་། སྐྱེས་པ་ལས་ཀྱང་ཡོངས་སུ་ཉམས་པར་འགྱུར་བ་དེའི་ཕྱིར་ལྡན་པ་མ་ཡིན༌[^969]ནོ། །

[Block 1382]
འོན་ཏེ་ལྡན་པ་མ་ཡིན་པ་རྣམས་ཀྱིས་ཀྱང་དེ་ལྟར་འགྱུར་ན་ནི་དེ་དག་རྟག་ཏུ་ཉེ་བའི་ཕྱིར་དགེ་བ་ནམ་ཡང་དམིགས་པར་མི་འགྱུར་བ་ཞིག་ན་དམིགས་ཏེ། དེ་ལྟ་བས་ན་དགེ་བ་འང་དམིགས་པའི་ཕྱིར་ན་འདིར། ཕྲ་རྒྱས་ལྡན་པ་མ་ཡིན་མིན། །འདི་ནི་གཏན་ཚིགས་སུ་མི་རུང་སྟེ། འདི་ལྟར་གང་ཞིག་ཕྲ་རྒྱས་ལྡན་པ་མ་ཡིན་པར་འདོད་པ་དེ་ཡང་འདི་ཐམས་ཅད་ཕྲ་རྒྱས་ཀྱིས་བྱས་པར་ནི་མི་འདོད་ཀྱི་ཉོན་མོངས་པས༌[^970]བྱས་པ་ཁོ་ནར་འདོད་དོ། །

[Block 1383]
མདོ་སྡེ་པ་རྣམས་ཀྱི་ཇི་ལྟ༌[^971]བ་དེ་ལྟ་བུ་ནི་ལེགས་པ་ཡིན་ནོ། །

[Block 1384]
མདོ་སྡེ་པ་རྣམས་ཀྱི་ཇི་ལྟ་བུ་ཡིན༌[^972]ཞེ་ན། འདོད་པའི་འདོད་ཆགས་ཀྱི་ཕྲ་རྒྱས་ནི་འདོད་པའི་འདོད་ཆགས་ཀྱི་ཕྲ་རྒྱས་ཡིན་ལ། དེ་རྫས་གཞན་མ་ཡིན་པའི་ཕྱིར་ཕྲ་རྒྱས་ནི་མཚུངས་པར་ལྡན་པ་ཡང་མ་ཡིན་ལ། ལྡན་པ་མ་ཡིན་པ་ཡང་མ་ཡིན་གྱི། ཉོན་མོངས་པ་ཉལ་བ་ལ་ནི་ཕྲ་རྒྱས་ཞེས་བྱ་ལ། སད་པ་ལ་ནི་ཀུན་ནས་དཀྲིས་པ་ཞེས་བྱའོ། །

[Block 1385]
དེ་ལ་ཉལ་བ་གང་ཡིན་ཞེ་ན། མངོན་སུམ་དུ་མ་གྱུར་པར༌[^973]ས་བོན་གྱི་དངོས་པོས་རྗེས་སུ་འབྲེལ་ལོ།[^974] །སད་པ་གང་ཡིན་ཞེ་ན། མངོན་སུམ་དུ་འགྱུར་བའོ།[^975] །ས་བོན་གྱི་དངོས་པོ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན། ལུས་ཀྱི་ཉོན་མོངས་པ་ལས་སྐྱེས་པ་ཉོན་མོངས་པ་བསྐྱེད་པའི༌[^976]མཐུ་ཡིན་ཏེ། དཔེར་ན་ཉམས་སུ་མྱོང་བའི་ཤེས་པ་ལས་སྐྱེས་པ་དྲན་པ་བསྐྱེད་པའི༌[^977]མཐུ་དང་། ཡང་དཔེར་ན་མྱུ་གུ་ལ་སོགས་པ་སཱ་ལུའི་འབྲས་བུ་ལས་བསྐྱེད༌[^978]པའི་མཐུ་དང་འདྲའོ། །

[Block 1386]
གང་ཞིག་ཉོན་མོངས་པ་རྣམས་ཀྱི་ས་བོན་གྱི་དོན་དུ་ཕྲ་རྒྱས་ལྡན་པ་མ་ཡིན་པ་དོན་གཞན་དུ་རྟོག་པར༌[^979]བྱེད་པ་དེས་ན་དྲན་པའི་ས་བོན་ཡང་དོན་གཞན་དུ་བརྟག་པར་བྱ་བར་འགྱུར་རོ། །

[Block 1387]
འོ་ན་མདོ་ལས་ཉོན་མོངས་པ་ཉིད་ཕྲ་རྒྱས་སུ་གང་གསུངས་པ་དེ་ཇི་ལྟ་བུ་སྟེ། དྲུག་ཚན་དྲུག་པ་ལས་འདིའི་འདོད་པའི་འདོད་ཆགས་དེ་བདེ་བའི་ཚོར་བ་ལ༌[^980]རྒྱས་པར་འགྱུར་རོ། །

[Block 1388]
[^981]རྒྱས་པར་གསུངས་སོ་ཤེ་ན། འགྱུར་རོ་ཞེས་གསུངས་པའི་ཕྱིར། དེ་ཁོ་ན་ནི་ཕྲ་རྒྱས་མ་ཡིན་ནོ། །

[Block 1389]
འོ་ན་ནམ་འགྱུར་ཞེ་ན། གང་གི་ཚེ་ཉལ་བ་ན་འགྱུར་རོ། །

[Block 1390]
ཡང་ན་འདི་ནི་རྒྱུ་ལས་དེ༌[^982]ཉེ་བར་བཏགས་པ༌[^983]ཡིན་པར་བལྟ་བར་བྱའོ། །

[Block 1391 [HEADING]]
### སྲིད་པའི་འདོད་ཆགས། ^2-4-0

[Block 1392]
ཞར་ལ་འོངས་པ་བཞག་ནས་བསྟན་བཅོས་ལ་འཇུག་པར་བྱ་སྟེ། མདོ་ལས་འདོད་པའི་འདོད་ཆགས་དང་། སྲིད་པའི་འདོད་ཆགས་ཞེས་འདོད་ཆགས་ཆེ་བ༌[^984]གང་ཡིན་པ། སྲིད་པའི་འདོད་ཆགས་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན། ཁམས་གཉིས་ལས་སྐྱེས་སྲིད་འདོད་ཆགས། །གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་ལས་སྐྱེས་པའི་འདོད་ཆགས་ནི་སྲིད་པའི་འདོད་ཆགས་ཞེས་བཤད་དོ། །ཅིའི་ཕྱིར་དེ་སྐད་དུ་བཤད་ཅེ་ན།

[Block 1393 [VERSE]]
ཁ་ནི་ནང་དུ་བལྟས་ཕྱིར་དེར། །
ཐར་པའི་འདུ་ཤེས་བཟློག་ཕྱིར་བཤད། །

[Block 1394]
དེ་དག་ནི་ཕལ་ཆེར་སྙོམས་པར་འཇུག་པ་ལ་སྙོམས་པར་འཇུག་པའི༌[^985]འདོད་ཆགས་པ་ཡིན་ལ། དེ་ཡང་ཁ་ནང་དུ་བལྟས་པ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་ཁ་ཅིག་ཁམས་དེ་གཉིས་ལས་ཐར་པ་ཡིན་ནོ་སྙམ་པའི་འདུ་ཤེས་བཟློག་པའི་ཕྱིར་སྲིད་པའི་འདོད་ཆགས་ཞེས་བཤད་དོ་ཞེས་གྲག་གོ། །

[Block 1395]
ལུས་ཁོ་ན་སྲིད་པ་ཡིན་ལ་སེམས་ཅན་དེ་དག་ཀྱང་སྙོམས་པར་འཇུག་པ་རྟེན་དང་བཅས་པ་རོ་མྱོང་བར་བྱེད་པ་ན་འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་ལུས་ཁོ་ན་རོ་མྱོང་བར་བྱེད་པ་ཡིན་ཏེ། དེའི་ཕྱིར་འདོད་ཆགས་དེ་ནི་སྲིད་པའི་འདོད་ཆགས་ཞེས་བཤད་དོ། །

[Block 1396 [HEADING]]
### ཕྲ་རྒྱས་བཅུ། ^2-5-0

[Block 1397]
ཡང་ཆོས་མངོན་པ་ལས་ཕྲ་རྒྱས་དྲུག་པོ་དེ་ལས་བཅུར་ཡང༌[^986]འཆད་དེ། ཇི་ལྟར་བྱས་པས་ཤེ་ན།

[Block 1398 [VERSE]]
ལྟ་བ་ལྔ་སྟེ་འཇིག༌[^987]ཚོགས་དང་། །
ལོག་དང་མཐར་འཛིན་ལྟ་བ་དང་། །
ལྟ་བ་དང་ནི་ཚུལ་ཁྲིམས་དང་། །
བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་དང་བཅུ། །

[Block 1399]
ཕྲ་རྒྱས་དྲུག་ལས་ལྟ་བ༌[^988]རྣམ་པ་ལྔར་བྱས་ན་བཅུར་འགྱུར་ཏེ། ལྟ་བའི་རང་བཞིན་ལྔ་ནི་འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། ལོག༌[^989]པར་ལྟ་བ་དང་། མཐར་འཛིན༌[^990]པར་ལྟ་བ་དང་། ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་དང་། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པའོ། །

[Block 1400]
ལྟ་བའི་རང་བཞིན་མ་ཡིན་པ་ལྔ་ནི་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། ང་རྒྱལ་དང་། མ་རིག་པ་དང་། ཐེ་ཚོམ་མོ། །

[Block 1401 [HEADING]]
### ཕྲ་རྒྱས་དགུ་བཅུ་རྩ་བརྒྱད། ^2-6-0

[Block 1402]
ཡང་ཆོས་མངོན་པ་ལས་ཕྲ་རྒྱས་བཅུ་པོ་དེ་དག་ལས་འདོད་པ་ན་སྤྱོད་པ་སུམ་ཅུ་རྩ་དྲུག་དང་། གཟུགས་ན་སྤྱོད་པ་སུམ་ཅུ་རྩ་གཅིག་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པ་སུམ་ཅུ་རྩ་གཅིག་སྟེ། དགུ་བཅུ་རྩ་བརྒྱད་དུ་ཡང་འཆད་དོ། །ཇི་ལྟར་བྱས་པས་ཤེ་ན། ཕྲ་རྒྱས་དེ་དག་ནི་མདོར་བསྡུ་ན་ཁམས་གསུམ་པའི་མཐོང་བས་སྤང་བར་བྱ་བ་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 1403 [HEADING]]
#### འདོད་པ་ན་སྤྱོད་པ། ^2-6-1-0

[Block 1404]
དེ་ལ་རེ་ཞིག་འདོད་པའི་ཁམས་ན་སྤྱོད་པ་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་སུམ་ཅུ་རྩ་གཉིས་སོ། །

[Block 1405]
དེ་དག་གང་ཞེ་ན། དེ་དག་བཅུ་དང་བདུན་བདུན་བརྒྱད། །ལྟ་བ་གསུམ་གཉིས་མ་གཏོགས་པར།[^991] །
--- END BLOCKS ---
