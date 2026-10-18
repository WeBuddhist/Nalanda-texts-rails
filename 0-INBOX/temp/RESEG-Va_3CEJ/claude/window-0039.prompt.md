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
རྟོག་པ་གཉིས་པ་ལྟར་ན་ནི་བདག་དང་གཞན་ལ་ལྟོས་པ་དག་ལས་འཛེམ་པ་དག་ཡིན་ནོ། །

[Block 1367 [HEADING]]
###### དགའ་བ་དང་གུས་པ། ^2-2-2-3-2-0

[Block 1368]
དགའ་བ་དང་གུས་པ་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཞིག་ཡོད་ཅེ་ན། དགའ་དང་ཞེས་བྱ་བ་སྨོས་ཏེ། དགའ་བ་ནི་རྣམ་པ་གཉིས་ཏེ། ཉོན་མོངས་པ་ཅན་དང་། ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའོ། །

[Block 1369]
དེ་ལ་ཉོན་མོངས་པ་ཅན༌[^595]ནི་སྲིད་པ༌[^596]སྟེ། དཔེར་ན་བུ་དང་ཆུང་མ་ལ་སོགས་པ་དག་ལ་དགའ་བ་ལྟ་བུའོ། །

[Block 1370]
ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ནི་དད་པ་སྟེ། དཔེར་ན་སྟོན་པ་དང་བླ་མ་དང་ཡོན་ཏན་ཅན་རྣམས་ལ་དགའ་བ་ལྟ་བུའོ། །

[Block 1371]
དད་པ་ཡིན་ལ་དགའ་བ་མ་ཡིན་པ་ཡང་ཡོད་དེ། སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ་ལ་དམིགས་པའི་དད་པ་ལྟ་བུའོ། །

[Block 1372]
དགའ་བ་ཡིན་ལ་དད་པ་མ་ཡིན་པ་ཡང་ཡོད་དེ། དགའ་བ་ཉོན་མོངས་པ་ཅན་ལྟ་བུའོ། །

[Block 1373]
གཉི་ག་ཡིན་པ་ནི་འགོག་པ་དང་ལམ་ལ་དམིགས་པའི་དད་པ་ལྟ་བུའོ། །

[Block 1374]
གཉི་ག་མ་ཡིན་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 1375]
གང་ཟག་དག་ལ་ལྟོས་ནས༌[^597]ནི་དགའ་བ་ཡིན་ལ་གུས་པ་མ་ཡིན་པ་ནི་བུ་དང་ཆུང་མ་དང་། ལྷན་ཅིག་གནས་པ་དང་། ཉེ་གནས་དག་ལ་དགའ་བ་ལྟ་བུའོ། །

[Block 1376]
གུས་པ་ཡིན་ལ་དགའ་བ་མ་ཡིན་པ་ནི་བླ་མ་གཞན་དག་ལ་གུས་པ་ལྟ་བུའོ། །

[Block 1377]
གཉི་ག་ཡིན་པ་ནི་རང་གི་བླ་མ་དག་ལ་གུས་པ་ལྟ་བུའོ། །

[Block 1378]
དེ༌[^598]གཉི་ག་མ་ཡིན་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 1379]
གཞན་དག་ན་རེ་དད་པ་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་ལ་ཡིད་ཆེས་པ་ཡིན་ལ། དེ་སྔོན་དུ་འགྲོ་བའི་དགའ་བ་ནི་དགའ་བ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་དེ་ཉིད་དགའ་བ༌[^599]ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1380]
གུས་ཉིད་ངོ་ཚ་ཤེས། གུས་པ་ནི་ངོ་ཚ་ཤེས་པ་ཇི་སྐད་བཤད་པ་ཡིན་ནོ། །

[Block 1381]
གཞན་དག་ན་རེ་གུས་པ་ཞེས་བྱ་བ་ནི་བཀུར་བ་དང་བཅས་པ་ཉིད་ཡིན༌[^600]ལ། དེ་སྔོན་དུ་འགྲོ་བའི་འཛེམ་པ་ནི་ངོ་ཚ་ཤེས་པ་ཡིན་ཏེ། དེའི་ཕྱིར་གུས་པ་ཉིད་ངོ་ཚ་ཤེས་པ་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1382]
དེ་གཉིས་འདོད་དང་གཟུགས་དག་ན། །གཟུགས་མེད་པའི་ཁམས་ན་ནི་དགའ་བ་དང་གུས་པ་དག་མེད་དོ། །

[Block 1383]
དད་པ་དང་ངོ་ཚ་ཤེས་པ་དགེ་བའི་ས་མང་པོ་པ་ཡིན་པའི་ཕྱིར་དེ་ན་ཡང་ཡོད་པ་མ་ཡིན་ནམ་ཞེ་ན། དད་པ་ནི་རྣམ་པ་གཉིས་ཏེ། ཆོས་དག་དང་གང་ཟག་ལ་དད་པ་ཡིན་ལ། བཀུར་བ་དང་བཅས་པ་ཉིད་ཀྱང་དེ་དང་འདྲའོ། །

[Block 1384]
དེ་ལ་གང་དག་གང་ཟག་ལ་དམིགས་པའི་དད་པ་དང་ངོ་ཚ་ཤེས་པ་དེ་དག་དེ་ན་མེད་དེ། འདིར་ནི་དགའ་བ་དང་གུས་པ་དེ་དག་ལ་བསམས་པ༌[^601]ཡིན་ནོ། །

[Block 1385 [HEADING]]
###### རྟོག་པ་དང་དཔྱོད་པ། ^2-2-2-3-3-0

[Block 1386]
རྟོག་པ་དང་དཔྱོད་པ་དག་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཞིག༌[^602]ཡོད་ཅེ་ན། རྟོག་དང་དཔྱོད་པ་རྩིང་ཞིབ་ཉིད། །གང་གི་ཞེ་ན། སེམས་ཀྱིའོ་ཞེས་འོག་ནས་འཆད་དེ། རྟོག་པ་ནི་སེམས་རྩིང་བའོ། །

[Block 1387]
དཔྱོད་པ་ནི་སེམས་ཞིབ་པའོ། །

[Block 1388]
སེམས་གཅིག་ལ་དེ་གཉིས་ཇི་ལྟར་ལྡན་ཞེ་ན། ཁ་ཅིག་ན་རེ་དཔེར་ན་མར་སར་ཆུ་དག་གི་ནང་དུ་བོར་བ་སྟེང་ནས་ཉི་མའི་འོད་ཟེར་དག་གིས་རེག་ན་ཧ་ཅང་ཡང་མི་འཁྱག་ལ། ཧ་ཅང་ཡང་མི་འཇུ་བ་དེ་བཞིན་དུ། སེམས་ཀྱང་རྟོག་པ་དང་དཔྱོད་པ་དང་ལྡན་པའི་ཕྱིར་ཧ་ཅང་ཞིབ་པར་ཡང་མི་འགྱུར། ཧ་ཅང་རྩིང་བར་ཡང་མི་འགྱུར་ལ། དེ་ལ་གཉི་གའི་བྱ་བ་ཡང་ཡོད་དོ་ཞེས་ཟེར་རོ། །

[Block 1389]
དེ་ལྟ་ན་ནི་ཇི་ལྟར་ཉི་མ་དང་ཆུ་མར་སར་འཁྱག་པ་ཉིད་དང་འཇུ་བ་ཉིད་དག་གི༌[^603]རྒྱུ་མཚན་ཉིད༌[^604]ཡིན་གྱི་དེ་དག་གི་ངོ་བོ་ཉིད་ནི་མ་ཡིན་པ་ལྟར་རྟོག་པ་དང་དཔྱོད་པ་དག་ཀྱང་རྩིང་བ་དང་ཞིབ་པ་ཉིད་དག་གི་རྒྱུ་མཚན་དུ་གྱུར་པ་ཡིན་ནོ། །

[Block 1390]
རྩིང་བ་དང་ཞིབ་པ་ས་དང་རྣམ་པའི་བྱེ་བྲག་གིས་ལྟོས་པ་ཅན་ཡང་ཡིན་པས་སྲིད་པའི་རྩེ་མོའི་བར་དུ་རྟོག་པ་དང་། དཔྱོད་པ་དག་ཡོད་པར་འགྱུར་རོ། །

[Block 1391]
རྩིང་བ་དང་ཞིབ་པ་ཉིད་ཀྱིས་རང་བཞིན་ཐ་དད་པར་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1392]
གཞན་དག་ན་རེ་མདོ་ལས་རྟོག་པ་དང་དཔྱོད་པ་དག་ནི་ངག་མངོན་པར་འདུ་བྱེད་པ་ཡིན་པར་གསུངས་ཏེ། བརྟགས་ཤིང་དཔྱད་ནས་ཚིག་ཏུ་སྨྲའི་མ་བརྟགས་མ་དཔྱད་པར་ནི་མ་ཡིན་ནོ་ཞེས་འབྱུང་ངོ་། །དེ་ལ་རྩིང་བ་གང་དག་ཡིན་པ་དེ་དག་ནི་རྟོག་པ་ཡིན་ནོ། །

[Block 1393]
ཞིབ་པ་གང་དག་ཡིན་པ་དེ་དག་ནི་དཔྱོད་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1394]
གལ་ཏེ་སེམས་རྩེ་གཅིག་ལ་རྩིང་བ་ཡང་ཆོས་གཞན་ཡིན། ཞིབ་པ་ཡང་ཆོས༌[^605]གཞན་ཡིན་ན་འདི་ལ་འགལ་བ་ཅི་ཞིག་ཡོད། གལ་ཏེ་ཚོར་བ་དང་འདུ་ཤེས་བཞིན་དུ་རིགས་ཐ་དད་པ་ཞིག་ཡིན་ན་ནི་འགལ་བ་མེད་དོ། །

[Block 1395]
རིགས་གཅིག་པ་ནི་ཆུང་ངུ་དང་ཆེན་པོ་ཉིད་ཅིག་ཅར་འབྱུང་བ་མི་སྲིད་དོ། །

[Block 1396]
རིགས་ཐ་དད་པ་ཡང་ཡོད་དོ། །

[Block 1397]
འོ་ན་ནི་དེ་བརྗོད་པར་བྱ་དགོས་སོ། །

[Block 1398]
དེ་བརྗོད་པར་ནི༌[^606]དཀའ་སྟེ། དེའི་ཕྱིར་ཆུང་ངུ་དང་ཆེན་པོའི༌[^607]ཉིད་ཀྱིས་གསལ་བར་འགྱུར་རོ། །

[Block 1399]
དེ་ལྟ་ན་ནི་གསལ་བར་མི་འགྱུར་ཏེ། [^608]རིགས་རེ་རེ་ལ་ཡང་ཆུང་ངུ་དང་ཆེན་པོ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1400]
གཞན་དག་ན་རེ་སེམས་གཅིག་ལ་རྟོག་པ་དང་དཔྱོད་པ་དག་མི་འབྱུང་བ་ཉིད་དོ་ཞེས་ཟེར་རོ། །

[Block 1401]
ད་ནི་ཇི་ལྟར་བསམ་གཏན་དང་པོ་ཡན་ལག་ལྔ་པར་བཤད་ཅེ་ན། ས་ལས་དེ་ཡན་ལག་ལྔ་པར་བཤད་ཀྱི་སྐད་ཅིག་ལས་ནི་མ་ཡིན་ནོ། །

[Block 1402 [HEADING]]
###### ང་རྒྱལ་དང་རྒྱགས་པ། ^2-2-2-3-4-0

[Block 1403]
ང་རྒྱལ་དང་རྒྱགས་པ་དག་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཞིག་ཡོད་ཅེ་ན།

[Block 1404 [VERSE]]
ང་རྒྱལ་ཁེངས་པ་རྒྱགས་པ་ནི། །
རང་གི་ཆོས་ལ་ཆགས་པ་ཡི། །
སེམས་ནི་ཡོངས་སུ་གཏུགས་པའོ། །

[Block 1405]
ཕ་རོལ་པོ་ལས་གང་ཡང་རུང་བའི་ཁྱད་པར་ཞིག་ཡོངས་སུ་བརྟགས་ནས་སེམས་ཁེངས་པ་ནི་ང་རྒྱལ་ལོ། །
--- END BLOCKS ---
