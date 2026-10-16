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
དེ་ལྟར་འདི་ལ་ཡང་ངེས་པའི་རྒྱུ་བརྗོད་པར་བྱ་བ་སྟེ། གང་གི་ཕྱིར་འགའ་ཞིག་འདི་ནི་འཇིག་པའི་བདག་ཉིད་ཅན་དུ་འབྱུང་བ༌[^1044]དག་ཡིན་ལ། འདིར་འགའ་ཞིག་ངེས་པར་བྱེད་པའི་རང་བཞིན་ནི་ཡོད་པ་མ་ཡིན་ཏེ། སྐྱེ་བ་དང་ལྡན་པ་ཐམས་ཅད་ནི་མི་རྟག་པ་ཉིད་དུ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1367]
གལ་ཏེ་སྐྱེ་བ་དང་ལྡན་པའི་རང་བཞིན་ནི་འཇིག་པ་ཅན་ཡིན་ནོ་ཞེ་ན། སྐྱེ་བ་ནི་འཇིག་པ་ཅན་གྱི༌[^1045]རང་བཞིན་གྱི་རྒྱུ་མ་ཡིན་ལ། རྒྱུ་མེད་པ་ཅན་གྱི་རང་བཞིན་ལ་ངེས་པ་མེད་པ་དེ་བས་ན། འདིར་རྒྱུ་ལས་རང་གི་ངོ་བོའི་རྣམ་པར་དབྱེ་བ་འགའ་ཞིག་ཀྱང་མེད་དེ། དེ་མེད་པའི་ཕྱིར་འབྲས་བུ་ལ་ཡང་ཡོད་པ་མ་ཡིན་པས་ན་མཚུངས་པ་མ་ཡིན་ནོ། །

[Block 1368]
འཇིག་པ་ལ་ལྟོས་པ་མེད་པའི་དེ་འདིས་འགའ་ཞིག་ལ་འགའ་ཞིག་གི་ཚེ་ཡོད་པ་འགལ་བ་ཅན་དེ་མེད་པའི་རང་བཞིན་དུ་སྒྲུབ་པར་བྱེད་དོ། །

[Block 1369]
གང་གི་ཕྱིར་རང་བཞིན་ལྟོས་པ་མེད་པ་དེ་ནི་གལ་ཏེ་འགའ་ཞིག་གི་ཚེའམ་འགའ་ཞིག་ལ་འགྱུར་ན་དུས་དང་རྫས་དེ་ལ་ལྟོས་པ་ཅན་ཡིན་པའི་ཕྱིར། ལྟོས་པ་མེད་པ་ཉིད་དུ་མི་འགྱུར་རོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 1370]
འོན་ཏེ་འཇིག་པའི་རང་བཞིན་དེ་ལྟོས་པ་མེད་པའི་ཕྱིར། རྒྱུ་མེད་པ་ཅན་དུ་འགྱུར་རོ། །

[Block 1371]
རྒྱུ་མེད་པ་ཅན་ཉིད་མ་ཡིན་ཏེ། ཡོད་པ་ཉིད༌[^1046]ཀྱི་རྒྱུའི་ངོ་བོ་ལས་དེ་ལྟར་སྐྱེ་བའི་ཕྱིར་དང་། ཡོད་པ་ཉིད་དུ་འགྱུར་བ་ནི་དེ་འདྲ་བ་ཉིད་ཀྱི་ངོ་བོ་མེད་པའི་ཕྱིར་རོ། །

[Block 1372]
གལ་ཏེ་གདོན་མི་ཟ་བར་ཡོད་པ་ཉིད་ནི་འགའ་ཞིག་ལས་ཀྱང་འབྱུང་བ་མ་ཡིན་ནོ་ཞེ་ན། འོ་ན་ཡོད་པ་ཉིད་ནི་གློ་བུར་བ་མ་ཡིན་པས་འདི་འགའ་ཞིག་ལ་འགའ་ཞིག་གི་ཚེ་འགའ་ཞིག་ཏུ་ལྡོག་པར་མི་འགྱུར་བས་དེ་ནི་ཅུང་ཞིག༌[^1047]འགའ་ཞིག་ལ་འབྲེལ་པ་མ་ཡིན་ནོ།[^1048] །གང་གང་ལ་ཅུང་ཞིག་རག་ལས་པ་མ་ཡིན་ནོ། །

[Block 1373]
གལ་ཏེ་ཡོད་པ་ཉིད་དེ་འདི་ནི་འགའ་ཞིག་ལ་རག་ལུས་པ་ཅན་མ་ཡིན་ནོ་ཞེ་ན། ངེས་པ་ཅན་དུ་མི་འགྱུར་རོ། །

[Block 1374]
དེ་བས་ན་འདི་ནི་འགའ་ཞིག་ཏུ་གློ་བུར་བ་མ་ཡིན་ནོ། །

[Block 1375]
འོ་ན་ད་ཇི་ལྟར་འཇིག་པ་རྒྱུ་མེད་པ་ཅན་དུ་བསྟན་ཞེ་ན། སྐྱེས་པ་དེའི་ངོ་བོ་ནི་གཞན་ལ་ལྟོས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1376]
འདིར་ཡང་འཇིག་པ་ཞེས་བྱ་བ་དངོས་པོ་ལས་གཞན་འགའ་ཞིག་ཀྱང་མེད་དེ་དངོས་པོ་ཉིད་འཇིག་པ་ཡིན་ལ། དེ་ཉིད་སྐད་ཅིག་མར་གནས་པའི་ངང་ཚུལ་ཅན་དུ་སྐྱེས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1377]
བླུན་པོ་དག་གིས་འདིའི་རང་བཞིན་དེ་ནི་ཕྱིས་ངེས་པར་འགྱུར་གྱི། སྔར༌[^1049]མ་ཡིན་ཏེ། མཐོང་ན་ཡང་། གསལ་བ་མེད༌[^1050]ཕྱིར་རོ། །ཞེས་བཤད་དོ། །

[Block 1378]
དེའི་དབང་གིས་མི་མཁས་པས་དུག་འགྱུར་བ་མཐོང་བས་འཇོག༌[^1051]པ་བཞིན་དུ་ཕྱིས་རྣམ་པར་འཇོག་པར་བྱེད་དེ། དེ་བས་ན་འཇིག༌[^1052]པ་འདི་ནི་ཡོད་པ་ཉིད་མ་གཏོགས་པར་གཞན་ལ་ལྟོས་པ་མེད་པའི་ཕྱིར། དེ་ལ་ཁྱབ་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1379]
འཇིག་པ་ལྟོས་པ་མེད་པ་དེ་ཡང་ཇི་ལྟར་རྟོགས་པར་འགྱུར་ཞེ༌[^1053]ན། དེ་རྒྱུ་ནུས་པ་མེད་པའི༌[^1054]ཕྱིར་ཡང་། མེད་པ་བྱེད་པའི་བྱ་བ་དགག་པའི་ཕྱིར་ཡང་གི་སྒྲ་སྨོས་སོ། ། ཇི་ལྟར་ནུས་པ་མེད་པ་ཡིན་ཞེ་ན། དངོས་པོ་གྲུབ་པ་ལ་ནི་བྱེད་པ་དེ་ལ་མི་བྱེད་ལ། གཞན་ལ་བྱེད་ན་ནི་དེ་ལ་ཅུང་ཞིག་ཀྱང་མ་ཡིན་པའི་ཕྱིར། དེ་དང་དེ་མ་ཡིན་པའི་ངོ་བོ་ལ་མི་བྱེད་པས་ཅུང་ཞིག་ཀྱང༌[^1055]མི་བྱེད་པ་ནི་ལྟོས་པ་མེད་པར་འགྱུར་རོ། །ཇི་ལྟར་བྱ་བ་འགོག་ཅེ་ན། འཇིག་པ་ཞེས་བྱ་བ་ནི་དེ་དག་གིས་དངོས་པོ་མེད་པ༌[^1056]ཡིན་པར་སེམས་སོ། །

[Block 1380]
དེ་བས༌[^1057]འཇིག་པའི་རྒྱུ་འདི་ནི་མེད་པར༌[^1058]བྱེད་དོ་ཞེས་བྱ་བ་འཐོབ་པོ། །དེ་ལ་གལ་ཏེ་མེད་པ་ཞེས་བྱ་བ་འགའ་ཞིག་འབྲས་བུའི་རང་བཞིན་དུ་འགྱུར་ན། དེ་ཉིད་དངོས་པོ་ཡིན་པའི་ཕྱིར་མེད་པར་མི་འགྱུར་རོ། །

[Block 1381]
དེ་བས་ན༌[^1059]མེད་པ་བྱེད་དོ་ཞེས་བྱ་བ་ནི་དངོས་པོ་མི་བྱེད་དོ་ཞེས་བྱ་བ་འདི་བྱ་བ་འགོག་པ་བྱེད་པར་འགྱུར་རོ། །

[Block 1382]
དེ་ལྟར་ན་ཡང་ཅུང་ཞིག་ཀྱང་མི་བྱེད་པ་འདི་ཅིའི་ཕྱིར་ལྡོག་པར་བྱ་བ་ཡིན་ཏེ། དངོས་པོ་ནི་འཇིག་པ་ལ་ལྟོས་པ་མེད་པར་གྲུབ་པ་ཡིན་ནོ། །

[Block 1383]
དེའི་ཕྱིར།

[Block 1384 [VERSE]]
གང་ཞེས་དེ་རང་བཞིན་གྱིས་འགྱུར། །
འདི་ལས་གཞན་པ་དག་ལ་ཡང་། །
རང་བཞིན་ཉིད་ཀྱིས་འགྱུར་བ་ཡིན། །

[Block 1385]
དེ༌[^1060]འདི་འགའ་ཞིག་ལ་ཡོད་པ་མཐོང་བ་ན་ལྟོས་པ་མེད་པ་ཉིད་ཀྱི་ཕྱིར། རང་བཞིན་གྱིས་འགྱུར་རོ། །

[Block 1386]
དེ་ལྟར་གཞན་དག་ལ་ཡང་རང་བཞིན་གྱིས་འབྱུང་བ་ཅན་ཡིན་ཏེ། ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 1387 [VERSE]]
འགའ་ཞིག་དངོས་པོའི་ཡུལ་ཅན་གྱི། །
རྗེས་དཔོག་གང་ཡིན་རྣམ་གཉིས་ཏེ། །
འབྲས་བུ་ངོ་བོ་དེས་དེ་དག །

[Block 1388]
རང་བསྒྲུབ༌[^1061]བྱ་ལ་འབྲེལ་ངེས་ཕྱིར། དེའི་ཕྱིར་དངོས་པོའི་ཡུལ་ཅན་གྱི་རྗེས་སུ་དཔོག་པ་ནི་རྣམ་པ་གཉིས་ཁོ་ན་སྟེ། འབྲས་བུའི་རྟགས་ཅན་དང་རང་བཞིན་གྱི་རྟགས་ཅན་ནོ། །

[Block 1389]
བདག་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་ཁྱད་པར་བྱེད་པ་བསྒྲུབ་པར་བྱ་བའི་རྟགས་ཅན་ལ་རྟགས་དེ་དག་རག་ལུས་པའི་ཕྱིར་གོང་དུ་ཇི་སྐད་བཤད་པ་ལྟ་བུའོ། །

[Block 1390 [HEADING]]
## མི་དམིགས་པའི་གཏན་ཚིགས། ^5-0

[Block 1391 [VERSE]]
འཇུག་པ་བློ་སྔོན་ཅན་ཉིད་ཕྱིར། །
དེ་ཡི་ངོ་བོ་མི་དམིགས་ན། །
འཇུག་པར་མི་བྱ༌[^1062]ཞེས་བྱ་བས། །
མི་དམིགས་པ་ནི་ཚད་མར་བཤད། །

[Block 1392]
གསུམ་པ་མི་དམིགས་པའི་གཏན་ཚིགས་ནི་བྱེ་བྲག་མེད་པར་དོན་འགའ་ཞིག་གིས༌[^1063]གོ་བར་བྱེད་པ་ཡིན་ནོ་ཞེས་བརྗོད་དོ། །

[Block 1393]
ཡོད་པར་ངེས་པ་དང་སྒྲ་དང་ཐ་སྙད་བཀག་པ་ནི༌[^1064]མི་དམིགས་པ་ཐམས་ཅད་ཁོ་ན་རྟགས་ཡིན་ནོ། །

[Block 1394]
ཡོད་པར་ངེས་པ་ལས་ནི་སྒྲ་དང་ཐ་སྙད་དག་འཇུག་པར་འགྱུར་བས་དེ་དག་ལ་འཇུག་པ་ཞེས་བྱ་བར་བཤད་དོ། །

[Block 1395]
དེ་ལྟར་ན་མི་དམིགས་པ་ཉིད་ནི་མེད་པ་རྣམས་ཀྱི་མེད་པ་ཡིན་ནོ་ཞེས་བཤད་དོ། །

[Block 1396]
དེ་ཡང་རྟོགས་པ་པོའི་དབང་གིས་ཡིན་གྱི་དངོས་པོའི་དབང་གིས་ནི་མ་ཡིན་ནོ། །

[Block 1397]
ཇི་སྲིད་འདི་ལ་རྟོགས་པ་མེད་པ་དེ་སྲིད་དུ་འདི་ལ་དངོས་པོ་དེའི་ཡོད་པ་མ་ཡིན་ཏེ། །ཡོད་པ་ཉིད་ཡིན་དུ་ཟིན་ཀྱང་དེས་དེའི་དོན་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1398]
དངོས་སུ་ནི་མི་དམིགས་པ་ཡིན་ན་ཡང་མེད་པ་དང་ཡོད་པ་མ་ཡིན་ཏེ། ཡོད་པ་ཉིད་ཡིན་ན་ཡང་རང་བཞིན་ལ་སོགས་པས་བསྐལ་པས་འགའ་ཞིག་ཏུ་མི་དམིགས་པའི་ཕྱིར་དང་། དེ་ནི་མེད་པ་དག་ལ་ཡང་མཚུངས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1399]
དེ་བས་ན་རྟོགས་པ་པོའི་ཚད་མ་མེད་པའི་ཕྱིར་དམིགས་པའི་མཚན་ཉིད་ཅན་གྱི་ཡོད་པ་ཉིད་དེ་ལྡོག་ཅིང་རང་གི་རྒྱུ་མཚན་ཅན་གྱི་སྒྲ་དང་ཐ་སྙད་དག་ལྡོག་པར་བྱེད་དོ། །

[Block 1400]
དེ་བས་ན་དམིགས་པའི་མཚན་ཉིད་ཀྱིར་གྱུར་པ་དག་མི་དམིགས་པ་དག་གང་ཡིན་པ་འདི་ཡང་དངོས་སུ་མེད་པ་ཉིད་ཀྱི་ངོ་བོ་ཡང་ཡིན་ཏེ། འཇུག་པར་མི་རུང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1401]
དེ་ཡང་ཡུལ་འདི་ལ༌[^1065]ཚད་མར་མཚུངས་སོ། །

[Block 1402]
མེད་པར་ངེས་པའི་འབྲས་བུ་ཅན་དེ་ཡང་ཡོད་པ་ཉིད་མ་ཡིན་དུ་ཟིན་ཀྱང་འདི་ཚད་མ་ཉིད་ཡིན་ཏེ། གང་དམིགས་སུ་རུང་བ་རྒྱུ་གཞན་ཚོགས་པ་དག་ཡོད་ན་མི་དམིགས་པ་སྲིད་པ་མ་ཡིན་ནོ། །

[Block 1403]
སྔ་མ་ནི་མེད་པ་ཉིད་སྒྲུབ་པར་བྱེད་པ་ཡང་མ་ཡིན་ཏེ།

[Block 1404 [VERSE]]
བསྟན་བཅོས་སྐབས་དང་འབྲེལ་མེད་དང་། །
དབང་པོ་ལས་འདས་རྟགས་ཅན་མིན། །
དོན་རྣམས་མང་པོ་དེ་དག་ནི། །
ཇི་ལྟར་མི་དམིགས་ཕྱིར་ན་མེད། །

[Block 1405]
དེ་མེད་པ་ཉིད་སྒྲུབ་པར་བྱེད་པ་ནི༌[^1066]མི་དམིགས་པ་ཙམ་གྱིས་དོན་ཐམས་ཅད་ལ་ཚད་མ་གསུམ་ལྡོག་པས་བསྒྲུབ་པར༌[^1067]འགྱུར་གྲང༌[^1068]ན། དེ་ལ་བསྟན་བཅོས་ལྡོག་པ་ནི་མེད་པ་ཉིད་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེ་ནི་སྐབས་འགའ་ཞིག་ལ་འཇུག་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
