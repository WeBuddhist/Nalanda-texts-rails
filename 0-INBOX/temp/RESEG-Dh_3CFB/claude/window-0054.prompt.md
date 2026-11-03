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
[Block 1891]
དེ་བས་ན་སྔར་བྱུང་བའི་ནུས་པ་འགགས་པའི་ཕྱིར། རྩིག་པ་ཡོད་ན་གཞན་སྐྱེ་བར་འདོད་པ་རྒྱུ་མེད་པས་མི་སྐྱེ་བའི་ཕྱིར་རྒྱུ་དང་བྲལ་བས༌[^1380]ཤེས་པ་མི་སྐྱེ་བ་དེ་ལྟར་ན་རྩིག་པ་ལ་སོགས་པ་ལ་སྒྲིབ་གཡོགས་ཞེས༌[^1381]བྱའོ། །

[Block 1892]
སྔར་རུང་བ་ལ་གེགས་བྱེད་པའི་ཕྱིར་ནི༌[^1382]མ་ཡིན་ཏེ། དེའི་རང་བཞིན་ལས་མ༌[^1383]འཕོས་པའི་ཕྱིར་རོ། །

[Block 1893]
ཡང་ན་དངོས་པོ་སྐད་ཅིག་མ་རྣམས་ཕན་ཚུན་ཕན་འདོགས་པ་ཡོད་དུ་ཟིན་ཀྱང་། ཐམས་ཅད་ཤེས་པ་མ་ཡིན་པས། །རྒྱུ་དང་རྐྱེན་གྱི་ནུས་པ་བསམ་གྱིས་མི་ཁྱབ་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1894]
དེ་བས་ན་གལ་ཏེ་དབང་པོ་དང་ཡུལ་གྱི་བར་ན་གནས་པའི་སྒྲིབ་གཡོགས་ངེས་དེ་ལ་རྣམ་པར་ཤེས་པ་སྐྱེད་པར་བྱེད་པ་དང་ཤིན་ཏུ་མི་མཐུན་པའི་བྱེ་བྲག་གིས་ཕུལ་དུ་བྱུང་བ༌[^1384]ཅན་དུ་བྱེད༌[^1385]ཟིན་ཀྱང་། སྒྲིབ་གཡོགས་ཀྱི་བྱེ་བྲག་གིས་སྒྲ་ལ་སོགས་པ་མཉན་པ་གསལ་བ་དང་མི་གསལ་བ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1895]
དེ་ལྟ་མ་ཡིན་ན་འགའ་ཞིག་ལ་ཡང་ཐག་ཉེ་བ་ཡིན་དུ་ཟིན་ཀྱང་ཅུང་ཞིག་མེད་པ༌[^1386]ཐག་ཉེ་བ་མ་ཡིན་པ་དང་མཚུངས་པའི་ཕྱིར། འདིའི་འདི་ཞེས་ཉེ་བར་སྦྱར་བ་ནི་རྣམ་པར་རྟོག་པས་སྤྲུལ་པ་ཉིད་ཡིན་གྱི། དངོས་པོ་ལ་བརྟེན་པ་ཅན་ནི་མ་ཡིན་ནོ། །

[Block 1896]
སྒྲོ་བཏགས་པའི་རྗེས་སུ་བྱེད་པའི་ངང་ཚུལ་ཅན་ནི་དོན་བྱེད་པ་དག་མ་ཡིན་ཏེ། བྲམ་ཟེའི་ཁྱེའུ་ལ་མེ་ཉེ་བར་བཏགས་པ༌[^1387]ལས་འཚེད་པའི་ཕྱིར་བསྟེན་པ་མ་ཡིན་པ་ལྟ་བུའོ། །

[Block 1897]
དེ་བས་ན་རྟོགས་པ༌[^1388]ཡོད་དུ་ཟིན་ཀྱང་དངོས་པོ་དེ་ཡོངས་སུ་གྱུར་པ་ཅན་མ་ཡིན་པ་དག་ནི་རང་བཞིན་ཇི་ལྟ་བ་བཞིན་དུ་གནས་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1898]
དེ་བས་ན་སྒྲིབ་གཡོགས་ཡོད་དུ་ཟིན་ཀྱང་དབང་པོ་ལ་སོགས་པ་དག་ཤེས་པར་བྱེད་པར་འགྱུར་ན་དེ་ལྟ་ཡང་མ་ཡིན་ནོ། །

[Block 1899]
དེ་བས་ན་དེས་བྱ་བ༌[^1389]ཁྱད་པར་དེ་ལྟར་ཤེས་པར་འགྱུར་རོ། །

[Block 1900]
དེ་ལྟར༌[^1390]སྒྲ་རྟག་པ་རྣམས་འགའ་ཞིག་ཡོད་ན་ཡང་ཕུལ་དུ་བྱུང་བ་ཉམས་པ་མེད་པར་འགྱུར་རོ། །

[Block 1901]
དེ་བས་ན་གལ་ཏེ་དེ་རྣམས་ཤེས་པ་བསྐྱེད་པའི་རང་བཞིན་ཡིན་ན། ཐམས་ཅད་ཐམས་ཅད་ཀྱི་ཚེ་རང་གི་ཡུལ་གྱི་ཤེས་པ་ཐམས་ཅད་ཅིག་ཅར་བསྐྱེད་པར་འགྱུར་བའམ། འགའ་ཞིག་འགའ་ཞིག༌[^1391]གི་ཆེ་ཅུང་ཞིག་ཀྱང་བསྐྱེད་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་ནི་ངེས་པ་ཡིན་ནོ། །

[Block 1902]
གལ་ཏེ་ལྷན་ཅིག་བྱེད༌[^1392]འགའ་དང་། །བྲལ་ཉིད་ཕྱིར་ན་མཉན་པ༌[^1393]མེད། །

[Block 1903]
དེ་ལྟར་ནི༌[^1394]འགྱུར་ན་སྒྲིབ་གཡོགས་ལས་རྟག་ཏུ་སྒྲ་དག་མ་ཐོས་པར༌[^1395]ནི་མ་ཡིན་མོད་ཀྱི། འོན་ཀྱང་དེ་དག་རྟོགས་པ་ལས་ལྷན་ཅིག་བྱེད་པ་ངེས་པ་ཅུང་ཟད་ནི་ཡོད་དོ། །

[Block 1904]
དེ་ནི་འགའ་ཞིག་གི་ཚེ་འགའ་ཞིག་ཏུ་འགྱུར་རོ་ཞེས་དེ་དག་འགའ་ཞིག་གི་ཚེ་འགའ་ཞིག་ཏུ་དེ་བྱས་པ་ཐོས་པ་ཡིན་ནོ་ཞེ་ན།

[Block 1905 [VERSE]]
དེ་ལྟར་གཞན་ལྟོས་ཡིན་བླ་སྟེ། །
ངེས་པ་དག་ནི་འགལ་བ་ཡིན། །

[Block 1906]
ཁོ་བོ་ཅག་ནི་རྒྱུ་རྣམས་ནི༌[^1396]ལྷན་ཅིག་བྱེད་པ་དག༌[^1397]སྤོང་བ་མ་ཡིན་མོད་ཀྱི། འོན་ཀྱང་རྒྱུ་རྣམས་དེའི་སྐབས་ལ་ཕན་འདོགས་པར་བྱེད༌[^1398]ལ་ལྟོས་པ་ཁོ་ན་ཡིན་ཏེ། དེ་ལས་རྙེད་པའི་ཕུལ་དུ་བྱུང་བའི་འབྲས་བུ་ལ་ཉེ་བར་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 1907]
དེ་ལྟར་ན་གལ་ཏེ་སྒྲ་དག་ཀྱང་འགའ་ཞིག་ལ་ལྟོས་ནས་འབྲས་བུ༌[^1399]བྱེད་པར་འགྱུར་ན་བྱེད་ལ་རག་གོ། །

[Block 1908]
སྔ་མའི་རང་བཞིན་ངེས་པ་ཞེས་བྱ་བ་དེར་མི་འགྱུར་ཏེ། དེ་ནི་འཕོས་པའི་ཕྱིར་དང་། ལྟོས་པར་བྱ་བ་ལས་རང་བཞིན་གཞན་ཐོས་པའི་ཕྱིར་རོ། །

[Block 1909]
ཕན་འདོགས་པ་མ་ཡིན་པ་ནི་ལྟོས་པར་བྱ་བར་འགྱུར་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ནི་བཤད་ཟིན་ཏོ། །

[Block 1910]
ཕན་འདོགས་པར་བྱེད་པ་དོན་གཞན་ཉིད་ཡིན་ན། དེའི་ཞེས་འབྲེལ་པ་མེད་པ་ལ་སོགས་པ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 1911]
དེ་ཡང་ཤེས་བྱ་ཉིད་མ་ཡིན་ཏེ། ཕན་འདོགས་པ་ཉིད་ལས༌[^1400]ཤེས་པ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1912]
དེ་བས་ན་སྒྲ་དེ་དག་ནི་དབང་པོ་དང་ཕྲད་པ་དང་། བདག་ཉིད་དང་། གཞན་རྣམ་པར་ཤེས་པ་སྐྱེད་པར་བྱེད་པའི་རྟེན་རང་གི་ཤེས་པ་སྐྱེད་པར་བྱེད་པ་འགའ་ཞིག་ལ་ལྟོས་པ་མེད་པ་ཡིན་ཏེ། དེ་ལ་ཐམས་ཅད་ཅུང་ཟད་ཀྱང་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1913]
གཞན་ཡང་སྒྲ་དེ་དག་ཁྱབ་པར་བྱེད་པའམ། ཁྱབ་པར་བྱེད་པ་མ་ཡིན་པར་འགྱུར་གྲང༌[^1401]ན།

[Block 1914 [VERSE]]
གལ་ཏེ་དེ་དག་ཁྱབ་བྱེད་མིན། །
ཐམས་ཅད་དུ་ནི༌[^1402]དམིགས་མི་འགྱུར། །

[Block 1915]
ཡུལ་གཅིག་ལ་གནས་པ་དེས་སྟོང་པའི་ཡུལ་ལ་གནས་པས་ཇི་ལྟར་དམིགས་པར་འགྱུར། གལ་ཏེ་མ་ཕྲད་པར་འཛིན་པའི་ཕྱོགས་ལ་སྐྱོན་ཡོད་པ་མ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་ལ་ཡང་རྡོ་ཁབ་ལེན་ལ་སོགས་པ་དང་འདྲ་བར༌[^1403]ཡུལ་རུང་བ་ཉིད་ལ་གནས་པ་ཁྱད་པར་ཅན་ལ་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 1916]
དེ་ལྟར་མ་ཡིན་ན་ཐོས་པ༌[^1404]གསལ་བ་དང་མི་གསལ་བའི་ཁྱད་པར་དུ་མི་འགྱུར་རོ། །

[Block 1917]
དམིགས་པའི་རྐྱེན་ཡོད་ན་ཡང་ཡུལ་ཐམས་ཅད་ལ་འདྲ་བར་དམིགས་པར་འགྱུར་རོ། །

[Block 1918]
དེ་བས་ན་ཁྱབ་པར་བྱེད་པ་མ་ཡིན་པ་མ་ཡིན་ནོ། །

[Block 1919 [VERSE]]
གལ་ཏེ་ཁྱབ་ན་ཐམས་ཅད་ཀྱིས། །
ཅིག་ཅར་དམིགས་པ་དག་ཏུ་འགྱུར། །

[Block 1920]
སྒྲ་འགའ་ཞིག་ལ་ཡང་མེད་པ༌[^1405]མ་ཡིན་པའི་ཕྱིར། ཐམས་ཅད་ཡུལ་ཐམས་ཅད་ན་གནས་པ་དག་གིས་ཅིག་ཅར་དམིགས་པར་འགྱུར་ཏེ། དབང་པོ་རུང་བ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་དང་། ཡུལ་ཐག་ཉེ་བ་ཉིད་ཀྱི་ཕྱིར་དང་།

[Block 1921 [VERSE]]
གེགས་བྱེད་པ༌[^1406]མེད་པའི་ཕྱིར་རོ། །
འདུས་བྱས་དམིགས་པ་ཡིན་ན་ཡང་། །
འགྱུར་མེད་གང་གིས་ལེགས་པར་བྱེད། །

[Block 1922]
དེ་ལྟར་ནི༌[^1407]འགྱུར་ན་སྒྲ་ཐམས་ཅད་ཡོད་དུ་ཟིན་ཀྱང་། དམིགས་པར་འགྱུར་བ་མ་ཡིན་ཏེ། འདུས་བྱས་པ་ལེགས་པར་བྱས་པ༌[^1408]ཁོ་ནས་དམིགས་པའི་ཕྱིར་རོ་ཞེ་ན། དེ་ལ་འདུས་བྱས་པ་ནི་དམིགས་པ་མ་ཡིན་ཏེ། བསྒྱུར་བར་བྱ་བ་མ་ཡིན་པ་ཅན་ནི་འདུས་བྱས་པར༌[^1409]མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1923]
དབང་པོ་ལེགས་པར་བྱས་གྱུར་ན། །དེས་ཀྱང་མ་ལུས་ཐོས་པར་གྱུར།[^1410] །དེ་ལ་གལ་ཏེ་ལེགས་པར་བྱས་པས་དམིགས་པའི་ཕྱིར་དབང་པོ་ལེགས་པར་མ་བྱས་པས་དམིགས་པར་མི་འགྱུར་རོ། །

[Block 1924]
གང་གིས༌[^1411]དབང་པོ་ལེགས་པར་བྱས་པ་དེས་སྒྲ་རྣམ་པ༌[^1412]ཐམས་ཅད་ཅིག་ཅར་ཐོས་པར་འགྱུར་བ་དེ་ལྟར་ན་ཐལ་བར་འགྱུར་བ་ཉིད་མ་ལོག་པ་ཡིན་ནོ། །

[Block 1925 [VERSE]]
གལ་ཏེ་ལེགས་བྱས་ཁྱད་པར་ལས། །
ཐ་དད་ཕྱིར་དོན་གཅིག་ངེས་ཡིན། །
སྒྲ་ཡི་འདུས་པ་སྣ་ཚོགས་པའི། །
ཅ་ཅོ་ཇི་ལྟར་ཐོས་པར་འགྱུར། །

[Block 1926]
ཅི་སྟེ་ཡང་འདུས་བྱས་པ་སྒྲ་དག་ལ་སོ་སོར་ངེས་པར་འགྱུར་བ་ཡིན་ཏེ། དེ་ལ་འགའ་ཞིག་གིས་དབང་པོ་ལེགས་སོ་ལེགས༌[^1413]པར་བྱས་པ་འགའ་ཞིག་འཛིན་པར་བྱེད་པའི་ཕྱིར། སྒྲ་ཐམས་ཅད་ཅིག་ཅར་ཐོས་པ་མ་ཡིན་ནོ་ཞེ་ན། ལེགས་པར་བྱས་པའི་ཁྱད་པར་ལས་དབང་པོ་རྣམས་ཀྱིས་ཐོས་པ་ངེས་པ་ཡིན་ན་སྒྲའི་ཚོགས༌[^1414]པའི་ཅ་ཅོ་ཐོས་པར་མི་འགྱུར་རོ། །

[Block 1927]
ཅ་ཅོ་ཞེས་བྱ་བ་ནི་སྒྲ་གཅིག་མ་ཡིན་ཏེ། རང་བཞིན་ཐ་དད་པ་ཅན་དག་ཅིག་ཅར་ཐོས་པའི་ཕྱིར་རོ། །

[Block 1928]
ཐ་དད་པ་རྣམ་པར་གཞག་པ་ཡང་རང་བཞིན་ཐ་དད་པ་ལ་བརྟེན་པ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1929]
གལ་ཏེ་འཇུག་པ་མྱུར་བའི་ཕྱིར། ཅིག་ཅར་ཐོས་པ་འཁྲུལ་པ༌[^1415]ཡིན་ནོ་ཞེ་ན། གླིང་བུ་ལ་སོགས་པའི་སྒྲའི་རྒྱུན་གོ་བར་བྱེད་པའི་ཡན་ལག་འདུས་པ་ལས་འདྲེས་པར་གྱུར་པ་རྟོགས་པར་འགྱུར་རོ། །

[Block 1930]
འདི་འགོག༌[^1416]པར་བྱེད་པ༌[^1417]ལ་ཡང་འོག་ནས་འཆད་པར་འགྱུར་རོ། །
--- END BLOCKS ---
