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
དེ་ལ་ལྔ་བརྒྱ་ཐམས་ཅད་ཀྱི་དང་པོ་ལ་དགྲ་བཅོམ་པ། ལྔ་བརྒྱ་གཉིས་པ་ལ་ཕྱིར་མི་འོང་བ། ལྔ་བརྒྱ་གསུམ་པ་ལ་རྒྱུན་ཏུ་ཞུགས་པ། ལྔ་བརྒྱ་བཞི་པ་ལ་ལྷག་མཐོང་།

[Block 1367]
ལྔ་པ་ལ་ཏིང་ངེ་འཛིན།

[Block 1368]
དྲུག་པ་ལ་ཚུལ་ཁྲིམས།

[Block 1369]
བདུན་པ་ལ་ཆོས་མངོན་པ།

[Block 1370]
བརྒྱད་པ་ལ་མདོ་སྡེ།

[Block 1371]
དགུ་པ་ལ་འདུལ་བ། ལྔ་བརྒྱ་བཅུ་པ་ལ་རྟགས་ཙམ་སྟེ། འདི་ཉིད་ལ་བརྒྱ་པ་ཐ་མ་ཞེས་བྱའོ། །

[Block 1372]
ཁ་ཅིག་ན་རེ་མི་རྣམས་ཀྱི་ཚེའི་ཚད་ནི་ལོ་ལྔ༌[^945]བརྒྱ་ཐུབ་སྟེ་དེ་ལ་ལོ་ལྔ་བཅུ་པ་སྔ་མ་ལ་ནི་མི་རྣམས་ཁ་དོག་དང་གཟུགས་དང་སྟོབས་དང་། ཤེས་རབ་ལ་སོགས་པ་མངོན་པར་འཕེལ་བ་ཡིན་ལ་ལྔ་བཅུ་པ་ཕྱི་མ་ལ་ནི་འགྲིབ་པ་ཡིན་ནོ། །

[Block 1373]
དེ་བཞིན་དུ་དུས་ཀྱི་མཐའ་བསྟན་པ༌[^946]འགྲིབ་པའི་དུས་ཀྱང་ལྔ་བཅུ་པ་ཕྱི་མ་དང་འདྲ་བས་ལྔ་བརྒྱ་པ་ཐ་མ་ཞེས་གདགས་སོ་ཞེས་ཟེར་རོ། །

[Block 1374 [HEADING]]
##### ཡོན་ཏན་གྱི་ཕན་ཡོན་ཐམས་ཅད། ^1-2-5-9-0

[Block 1375]
[^947]ཡོན་ཏན་གྱི་ཕན་ཡོན་ཐམས་ཅད་བསྟན་པ་ནི་བརྡ་ཕྲད་སླའོ། །

[Block 1376 [HEADING]]
##### བདུད་ཀྱི་ལས། ^1-2-5-10-0

[Block 1377]
བདུད་ཀྱི་ལས་རྣམས་ནི་སྤོབས་པ་ཕྱིས༌[^948]ཏེ་སྐྱེས་ན་ཐོགས་པར༌[^949]འགྱུར་བ་དང་། སྤོབས་པ་ཧ་ཅང་མྱུར་བར་སྐྱེས་ན་ང་རྒྱལ་ཅན་དུ་འགྱུར་བ་དང་། མ་གུས་པར་བྱེད་པ་དང་། གླལ་བ་དང་། དྲེགས་པའོ། །

[Block 1378]
རྒོད་ཅེས་བྱ་བ་ནི་ཆོས་འཆད་པའི་ཚེ་རྒོད་པའམ་ཕན་ཚུན་ཀྱལ་ཀ་བྱེད་པའོ། །

[Block 1379]
ཕན་ཚུན་སྟེག་ཅིང༌[^950]ཞེས་བྱ་བ་ནི་གཅིག་ལ་གཅིག་དགོད་བྲོ་བར་བྱེད༌[^951]པའོ། །

[Block 1380]
ཕན་ཚུན་བཤེས་གཉེན་པ༌[^952]ལ་ཆགས་ཞེས་བྱ་བ་ནི་ཕན་ཚུན་སེམས་བསྲུང་བའི་ཕྱིར་བྱེད་ཀྱི༌[^953]དད་པས་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1381]
ཡི་གེ་གཞན་ལ་ཆགས་ཤིང་ཚིག་གི་དོན་མི༌[^954]ཤེས་པ་ཞེས་ཀྱང་འབྱུང་ངོ་། །གླལ་ཞིང་འཛིན་ན་ཞེས་བྱ་བ་ལ༌[^955]གླལ་བ་ལ་སོགས་པ་འདི་ལྔ་ལས་སྔ་མ་ནི་ཡི་གེར་འབྲི་བའི༌[^956]ཚེ་ནའོ། །

[Block 1382]
འདིར་ནི་འཛིན་པའི་ཚེའོ། །

[Block 1383]
འགྲོ་བའི་སེམས་བསྐྱེད་པ་ཇི་སྙེད་བྱུང་བ། དེ་སྙེད་ཀྱི་བསྐལ་པ་ཡོངས་སུ་འཛིན་པར་འགྱུར་ཞེས་བྱ་བ་ནི་སླར་འགྲོ་བའི་སེམས་བསྐྱེད་པ་སྙེད་ཀྱི་བསྐལ་པར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ལ་བརྩོན་པར་བྱ་དགོས་ཏེ་འཆལ་བའི་ཤེས་རབ་ཡིན་པས་དེ་སྙེད་ཀྱི་བསྐལ་པས་ཡོངས་སུ་སྨིན་པར་འགྱུར་རོ། །

[Block 1384]
དེ་དག་ནི༌[^957]རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཤིང་གི་རྩ་བ་སྤངས་ཏེ་ཞེས་བྱ་བ་ནི་དཔེར་ན་ཤིང་གི་རྩ་བ་སྤངས་ཏེ་ཡལ་ག་དང་འདབ་མ་དང་། ལོ་མ་ལ་སྒྲུབ་པ་དག་དོན་ཇི་ལྟ་བ་བཞིན་དུ་མི་འགྲུབ་པ་དེ་བཞིན་དུ། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི༌[^958]ཤིང་ལྗོན་པ་མེད་པར་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཡལ་ག་དང་ལོ་མ་ལ་སོགས་པ་ལྟ་བུ་ཡང་ཐོབ་པར་མི་འགྱུར་རོ༌[^959]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1385]
ཇི་ལྟར་ཁྱི་རྗེ་བོའི་ཟན་ཞིམ་པོ་རྙེད༌[^960]སླ་བ་བོར་ཏེ༌[^961]མིའི་ཟན་བཙལ་ན་མི་རྙེད་པའམ། ཅུང་ཟད་ཅིག་རྙེད་པར་འགྱུར་བ་དེ་བཞིན་དུ་འདིར་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1386]
ཇི་ལྟར་ལ་ལ་ཞིག་གླང་པོ་ཆེ་རྙེད་ཀྱང་བོར་ཏེ། བདག་ནི་གླང་པོ་ཆེའི་རྗེས་འདོད་ཀྱི་གླང་པོ་ཆེ་ནི་མི་འདོད་དོ་ཞེས་ཟེར་བ་དེ་དཔྱས་སུ་འགྱུར་བ་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 1387]
བ་ལང་གི་རྗེས་ཀྱི༌[^962]དཔེ་དང་ཤིང་མཁན་རྣམ་པར་རྒྱལ་བའི་ཁང་པ༌[^963]དབུབ་པར་འདོད་པ་ཉི་མ་དང་ཟླ་བའི་གཞལ་མེད་ཁང་གི་དཀྱིལ་འཁོར་ཚོལ་ཞིང་རྣམ་པར་རྒྱལ་བའི་ཁང་པ་ཡང་འདི་ཙམ་མོ་ཞེས་བྱ་བའི་དཔེ་ཡང་དེ་བཞིན་ནོ། །

[Block 1388]
རབ་འབྱོར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་སྤོབས་པ་མེད་པས་ཞེས་བྱ་བ་ནི་རྣམ་པར་མི་རྟོག་པའི་ཕྱིར་རོ། །

[Block 1389]
བསམ་གྱིས་མི་ཁྱབ་པའོ་ཞེས་བྱ་བ་ནི་རྟོག་གེའི་སྤྱོད་ཡུལ་ལས་ཡང་དག་པར་འདས་པའི་ཕྱིར་རོ། །

[Block 1390]
སྐྱེ་བ་མེད་ཅིང་འགག་པ་མེད་པའོ་ཞེས་བྱ་བ་ནི་མི་འགྱུར་བར་ཡོངས་སུ་འགྲུབ་པར་ཡོངས་སུ་གྲུབ་པའི༌[^964]ཕྱིར་རོ། །

[Block 1391]
ཀུན་ནས་ཉོན་མོངས་པ་མེད་ཅིང་། རྣམ་པར་བྱང་བ་མེད་པའོ་ཞེས་བྱ་བ་ནི་རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པའི་ཕྱིར་རོ། །

[Block 1392]
འཁྲུགས་པ༌[^965]མེད་པའོ་ཞེས་བྱ་བ་ནི་རྟག་ཏུ་མཉམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 1393]
བརྗོད་དུ་མེད་པ་ནི་སོ་སོ་རང་གིས་རིག་པའི་ཕྱིར་རོ། །

[Block 1394]
སྨྲར་མེད་པ་ནི། སྒྲ་ལས་ཡང་དག་པར་འདས་པའི་ཕྱིར་རོ། །

[Block 1395]
རབ་ཏུ་བརྗོད་དུ་མེད་པ་ནི་རྣམ་པར་རྟོག་པ་དང་། རྣམ་པར་དཔྱོད་པ་ལས་ཡང་དག་པར༌[^966]འདས་པའི་ཕྱིར་རོ། །

[Block 1396]
དམིགས་སུ་མེད་པ་ནི་དངོས་པོར་དམིགས་པ་ཐམས་ཅད་དང་བྲལ་བའི་ཕྱིར་རོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་མོ་འདི་དངོས་པོ་མེད་ཅེས་བྱ་བར་འདུ་ཤེས་ན་དེ་ཡང་བདུད་ཀྱི་ལས་སོ་ཞེས་བྱ་བ་ནི་དངོས་པོ་མེད་པའི་འདུ་ཤེས་ཀྱི༌[^967]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བཤད་པ་ལ་རིམ་གྲོར་མི་བྱེད་པའི་ཉེས་པའོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ཡི་གེ་མ་མཆིས་པའོ་ཞེས་བྱ་བ་ནི་བརྗོད་དུ་མེད་པ་དང་། མཉན༌[^968]དུ་མེད་པའི་ཕྱིར་རོ། །

[Block 1397]
བདུད་ཀྱི་ལས་ལྷག་མ་རྣམས་ནི་བརྡ་ཕྲད་པར་སླའོ། །

[Block 1398 [HEADING]]
##### དེ་བཞིན་གཤེགས་པ་བསྐྱེད་པ། ^1-2-5-11-0

[Block 1399]
རབ་འབྱོར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདིས་དེ་བཞིན་གཤེགས་པའི་སྟོབས་བཅུ་བསྐྱེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^969]སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་བསྐྱེད་པའི༌[^970]ཕྱིར་དོན་དམ་པའི་དེ་བཞིན་གཤེགས་པ་བསྐྱེད་པ༌[^971]ཡིན་ནོ་ཞེས་སྟོན་ཏོ། །

[Block 1400 [HEADING]]
##### འཇིག་རྟེན་སྟོན་པ། ^1-2-5-12-0

[Block 1401]
འཇིག༌[^972]རྟེན་སྟོན་པ་ཞེས་བྱ་བ་ནི་རྣམ་པ་བཅུ་གཅིག་གིས་འཇིག་རྟེན་སྟོན་པར་བཤད་དེ། ཕུང་པོའི་འཇིག་རྟེན་སྟོན་པ་དང་། ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་བརྟགས་པ་དམིགས་སུ་མེད་པར་སྟོན་པ་དང་། སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་ཀྱི་སྤྱོད་པ་དང་། དབྱེ་བ་ལ་སོགས་པ་སྟོན་པ་དང་། ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་སྟོན་པ་དང་། ཆོས་ཐམས་ཅད༌[^973]མཚན་ཉིད་མེད་པའི་མཚན་ཉིད་དུ་སྟོན་པ་དང་། བྱས་པ་གཟོ་ཞིང་བྱས་པ་ཚོར་བའི་དབང་དང་། ཆོས་ཐམས་ཅད་ཤེས་པ་པོ་མེད་ཅིང་། མཐོང་བ་པོ་མེད་པར་སྟོན་པ་དང་། མ་མཐོང་བའི་ཆོས་ཐམས་ཅད་སྟོན་པ་དང་། འཇིག་རྟེན་སྟོང་པ་ཉིད་དུ་བརྗོད་པ༌[^974]རིག་པར་བྱེད་ཤེས་པར་བྱེད། རྣམ་པར་ཤེས་པར་བྱེད་སྟོན་པར་བྱེད་པའི་དབང་དང་། འཇིག་རྟེན་འདི་བསམ་གྱིས་མི་ཁྱབ་ཅིང་དབེན་ལ། ནང་ལ་སོགས་པ་སྟོང་ཞིང་ཞི་བར་སྟོན་པ་དང་། འཇིག་རྟེན་འདི་དང་འཇིག་རྟེན་ཕ་རོལ་པོའི་འདུ་ཤེས་མེད་པས་སོ། །

[Block 1402 [HEADING]]
###### ཕུང་པོའི་འཇིག་རྟེན་སྟོན་པ། ^1-2-5-12-1-0

[Block 1403]
དེ་ལ་རབ་འབྱོར་ཕུང་པོ་ལྔ་ནི་དེ་བཞིན་གཤེགས་པས་འཇིག་རྟེན་དུ་གསུངས་སོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཕུང་པོ་ལྔ་པོ་འདི་དག་འཇིག་པར་སྟོན་པ་མ་ཡིན། རབ་ཏུ་འཇིག་པར་སྟོན་པ་མ་ཡིན་ཏེ༌[^975]ཞེས་བྱ་བ་ལ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཕུང་པོའི་དེ་བཞིན་ཉིད་འབའ་ཞིག་མཐོང་གི་ཀུན་བརྟགས་པའི་ཕུང་པོ་ནི་མ་ཡིན་ནོ། །

[Block 1404]
འཇིག་པ་དང་རབ་ཏུ་འཇིག་པ་ཞེས་བྱ་བ་ནི་ཆུད་ཟ་བ་དང་མ་རུང་བར་འགྱུར་བ་ལ་བྱའོ། །

[Block 1405 [HEADING]]
###### ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་བརྟགས་པ་དམིགས་སུ་མེད་པར་སྟོན་པ། ^1-2-5-12-2-0
--- END BLOCKS ---
