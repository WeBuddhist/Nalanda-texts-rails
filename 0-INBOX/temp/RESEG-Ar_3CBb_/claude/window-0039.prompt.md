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
དེས་ནི༌[^724]བྱེད་ཅེ་ན། གང་གིས་གང་ཞིག་ཀུན་དུ་སྣང་བར་གྱུར་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1367]
གཞན་ནི་གོ་སླའོ། །

[Block 1368]
དེ་ནས་གང་གིས་གང་ཞིག་ཡོངས་སུ་རྫོགས་པར་བསྟན་པ་ནི། གང་གིས་ལྷའི་འཁོར་ལོ་ཡོངས་སུ་རྫོགས་པ་སྟེ་དེ་ཉིད་དོ། །

[Block 1369]
དམ་ཚིག་རྡོ་རྗེ་ཞེས་བྱ་བ་གང་ཞིག་ཡིན་ཞེ་ན་དོན་ཡོད་པར་གྲུབ་པའོ་ཞེས་གང་ཞིག་ཡོངས་སུ་གྲུབ་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1370]
འོ་ན་སྒྲིབ་པ་རྣམ་པར་སེལ་བ་ལ་ཅིའི་ཕྱིར་དམ་ཚིག་རྡོ་རྗེའི་སྒྲར་བརྗོད་ཅེ་ན། འདིར་དེའི་རིགས་དང་ལྡན་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདིར་དོན་ཡོད་གྲུབ་པའི་རིགས་དང་ལྡན་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1371]
དེ་བས་ན་གཅིག༌[^725]ནི་དངོས་སུ་བརྗོད་པ་ཉིད་དོ། །

[Block 1372]
གཅིག༌[^726]ནི་བཏགས་ནས༌[^727]བསྟན་པ་ཉིད་དོ། །

[Block 1373]
རིགས་གཞན་ཡང་དེ་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 1374]
འདི་དག་གིས་ནི་བྱང་ཆུབ་སེམས་དཔའི་འཁོར་བསྟན་ཏོ། །

[Block 1375]
བྱང་ཆུབ་སེམས་དཔའི་འཁོར་ཁོ་ན་ལས་མ་གསུངས་སམ་ཞེ་ན་མ་ཡིན་པའི་ཕྱིར། བྱང་ཆུབ་སེམས་དཔའི་ཚོགས་འབའ་ཞིག་དང་ལྷན་ཅིག་བཞུགས་པར་མ་ཟད་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འོ་ན་གང་དང་བཞུགས་ཤེ་ན། དེ་བཞིན་གཤེགས་པ་རྣམས་དང་ཡང་ལྷན་ཅིག་ཏུ་བཞུགས་པ་སྟེ་བགྲང་བ༌[^728]ལས་འདས་ཞེས་བྱ་བ་ལྷག་མ་རྣམས་སོ། །

[Block 1376]
གཞན་ནི་གོ་སླའོ། །

[Block 1377]
རྡོ་རྗེ་འཆང་ཆེན་པོ་ཉིད་ཀྱི༌[^729]ཡན་ལག་གི་ཆ་ཤས་སུ་གྱུར་པ་ཞེས་པ་ནི་འཁོར་ཐམས་ཅད་གཙོ་བོ་ལས་ཐ་དད་དུ་འཇུག་པར་མི་འགྱུར་ཏེ། གང་གི་ཕྱིར་གང་ཞིག་གང་ལས་ཐ་དད་དུ་མེད་པར༌[^730]འགྱུར་བ་དེའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །གང་ལས་ཤེས་ཤེ་ན། འདི་ཉིད་ལས་ཞེས་པ་གསང་བ་འདུས་པའོ། །

[Block 1378]
མདོར་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་བཤད་ཟིན་ཏོ། །

[Block 1379]
དེ་བས་ན་ཞེས་པ་ནི་དེའི་ཕྱིར་ཞེས་པའོ། །

[Block 1380]
བཅོམ་ལྡན་འདས་དེ་ཉིད་ཀྱི་ཞེས་པ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1381]
རང་གི་སྐུའི་དཀྱིལ་འཁོར་སྤྲོས་ནས་ཞེས་པ་ནི་རང་གི་འཁོར་ཡོངས་སུ་རྫོགས་པའོ། །

[Block 1382]
དེས་ཅི་བྱེད་ཅེ་ན། དཀྱིལ་འཁོར་འཁོར་ལོ་ལྟ་བུས་འདུལ་བའི་སྐྱེ་བོ་རྣམས་དགའ་བར་བྱ་བའི་ཕྱིར་ཞེས་པའོ། །

[Block 1383]
གཞལ་ཡས་ཁང་གི་དབུས་སུ་བཞུགས། །ཞེས་པ་ནི་གོ་བར་མཛད༌[^731]དོ། །

[Block 1384]
དེ་ལྟར་ཞེས་པ་ནི་མཇུག་བསྡུ་བའི་ཐ་ཚིག་གོ། །

[Block 1385]
ད་ནི་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^732]ནི་འདོད་ཆགས་ཆེན་པོའི་སྤྱོད་པ་ཡོངས་སུ་རྫོགས་པར་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1386]
འདོད་ཆགས་ཀྱིས་འདོད་ཆགས་རབ་ཏུ་སྤང་བར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 1387]
བཤད་མ་ཐག་པ༌[^733]ནི་གོང་དུ་བཤད་པ་ཉིད་དོ། །

[Block 1388]
རང་གི་ས་བོན་གྱི་འོད་ཟེར་གྱི་ལྕགས་ཀྱུས་དྲངས་ཞེས་པ་ནི་སྙིང་ག་ནས་ཕྱུང་སྟེ་སླར་བསྡུ་བས༌[^734]བསྡུས་ཞེས་པའི་དོན་ཏོ། །

[Block 1389]
འདི་ཡང་གང་གི་ཕྱིར་གང་ཞིག་ལ༌[^735]བྱུང་ནས་གང་དུ་གནས་པར་འགྱུར་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1390]
དེ་ནས་ཅི་བྱེད་ཅེ་ན་བཅོམ་ལྡན་འདས་མཆོག་ཏུ་དགའ་བའི་བདེ་བས་ཚིམ་པར་བྱ་བའི་ཕྱིར་ཞེས་པ་ནི་གང་གི་བདེ་བས་གང་ཞིག་གང་དུ་གནས་པར་འགྱུར་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། གནས་སྐབས་སྔ་མ་ནི་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའི་དཀྱིལ་འཁོར་ཏེ་གང་གིས་དེ་ཡོངས་སུ་སྤངས་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1391]
འོ་ན་གང་དུ་འགྱུར་ཞེ་ན། ལྷའི་བུ་མོའི་གཟུགས་སུ་མངོན་པར་སྤྲུལ་ནས་ཞེས་པ་ནི་གང་གིས་ལྷའི་བུ་མོ་གང་དང་འདྲ་བར་ཀུན་དུ་མཛེས་པར་གྱུར་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1392]
ལྷའི་བུ་མོའི༌[^736]གཟུགས་སྣང་བ་ཡང་གང་དང་གང་ཡིན་ཞེ་ན་སའི་ཁམས་ནི་སངས་རྒྱས་སྤྱན་ལྟ་བུའོ་ཞེས་པ་ནི་ས་རྡོ་རྗེ་ལས་ཐ་དད་དུ་གནས་པའོ། །

[Block 1393]
འདིར་སའི་ཁམས་ཉིད་སངས་རྒྱས་སྤྱན་ལྟ་བུའོ་ཞེས་པ་ནི་གང་ཞིག་གང་ལས་ཐ་དད་དུ་གྱུར་པའོ། །

[Block 1394]
ཡང་ན་འདིར་སའི་ཁམས་ནི་སངས་རྒྱས་སྤྱན་ཉིད་ཅེས་པ༌[^737]ནི་གང་ཞིག་དང་འབྲེལ་པ་དེ་ལ་དེ་སྐད་ཅེས་ཅེས་བྱའོ། །

[Block 1395]
གཞན་ཡང་དེ་བཞིན་ནོ། །

[Block 1396]
འདོད་ཆགས་ཀྱང་ཡིན་ལ་ཆེན་པོ་ཡང་ཡིན་པས་གང་ཞིག་ཉོན་མོངས་པ་དང་བྲལ་བ་གང་ཡིན་པའི་ཆོས་ཉིད་དོ། །

[Block 1397]
འདོད་ཆགས་དང་བྲལ་བ་ལ་སོགས་པ་ཡང་གང་ཡིན་ཞེ་ན་ཉོན་མོངས་པ་དང་བྲལ་བའོ། །

[Block 1398]
གཞན་གོ་སླའོ། །

[Block 1399]
གཞན་ཡང་གང་ཞིག་ཕྱི་རོལ་གྱི་དེ་བཞིན་གཤེགས་པའི་འཁོར་དེ་དག་ཏུ་དམིགས་ཞེས་པ་ལ་སོགས་པའི་དོན་ནི། གང་གིས་གང་ཞིག་གང་དུ་འཛིན་པ་དེ་དང་དེ་སྤང་བར་བྱ་བའི་ཕྱིར་ཞེས་པའོ། །

[Block 1400]
བདག་ཉིད་སངས་རྒྱས་ཐམས་ཅད་དེ། །ཞེས་པ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་དང་སངས་རྒྱས་ཐམས་ཅད་ཐ་དད་དུ་མེད་ཅེས་པའོ། །

[Block 1401]
རྒྱལ་སྲས་ཐམས་ཅད་ཉིད་ཀྱང་ཡིན། །ཞེས་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་བདག་པོར་གྱུར་པ་ཡང་ཡིན་ཞེས་པ་སྟེ་ཐ་དད་དུ་མེད་པ་ཡིན་ནོ། །

[Block 1402]
ངེས་པ༌[^738]ནི་མ་ནོར་བའོ། །

[Block 1403]
ད་ནི་དེ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པའི་དགོས་པ་བཤད་པའི་ཕྱིར། ད་ནི་རྒྱུད་འདི་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སེམས་གཙོ་བོ་ཡིན་པ་ནི་ཏིང་ངེ་འཛིན་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1404]
མི་བསྐྱོད་པ་ནི་ཐུགས་ཀྱི་ངོ་བོའི་ཕྱིར་རོ། །

[Block 1405]
འདི་སྐད་དུ་སྟོན་ཏོ།[^739] །སེམས་སྣང་བ་དང་བཅས་པ་གང་གི་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་གིས་སྦྱངས་པས་ཐོབ་པ་དེ་ནི་དེའི་རིགས་ཏེ་དེ་བས་ན་དེ༌[^740]གཙོ་བོར་གྱུར་པ་ཉིད་དོ། །
--- END BLOCKS ---
