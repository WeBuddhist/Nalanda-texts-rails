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

[Block 1931]
དེ་བས་ན་དབང་པོ་ནི་གཅིག་རྟོགས་པར་ནུས་པ་སོ་སོར་ངེས་པ་ཡིན་པའི་ཕྱིར། ཅ་ཅོ་དུ་མའི་བདག་ཉིད་ཅན་ཐོས་པ་མ་ཡིན་ནོ། །

[Block 1932 [VERSE]]
དེ་ལ་གལ་ཏེ་སྒྲ་ཡན་གར། །
ཐོས་འགྱུར་རྗོད་བྱེད་དག་མ་ཡིན། །

[Block 1933]
ཅ་ཅོ་ལ་ཡི་གེ་དང་ཚིག་དག་ངག་དག་ནི་ཐོས་པ་མ་ཡིན་ཏེ། སྒྲ་ཙམ་ཡན་གར་བ་དག་ཐོས་པའི་ཕྱིར་རོ། །

[Block 1934]
རྗོད་པར༌[^1418]བྱེད་པ་ལ་དབང་པོ་སོ་སོར་ངེས་པའི་ནུས་པ་ཅན་ཡོད་པའི༌[^1419]སྒྲ་ཙམ་དག་ལ་ནི་མ་ཡིན།[^1420] དེ་ལ། སྒྲ་ལས་ཐ་དད་ཡོད་དོ་ཞེས།[^1421] །འདི་ལ་ཤིན་ཏུ་ཆེས་དད་བྱ། །ཁོ་བོ་ཅག་གིས་ནི་སྒྲ་ཙམ་དང་རྗོད་པར་བྱེད་པའི་སྒྲའི་ངོ་བོ་ཐ་དད་པ་མ་མཐོང་ངོ་། །དུས་གཅིག་གི་ཚེ་ཡི་གེའི་གོ་རིམས་ཐོས་པ་ན་སྒྲའི་བདག་ཉིད་གཅིག་ཁོ་ནར་ངེས་སོ། །

[Block 1935]
དེ་བས་ན་ངེས་པ་སྔོན་དུ་སོང་བ་ཅན་གྱི་ཐ་སྙད་ཡོངས་སུ་གཅད་པ༌[^1422]མེད་པར་ཇི་ལྟར་འཇུག་པར་འགྱུར། དེ་བས་ན་སྒྲའི་ཁྱད་པར་འདི་ཉིད་ཡི་གེ་ལ་སོགས་པ་ཞེས་བྱའོ། །

[Block 1936]
གཞན་ཡང་།

[Block 1937 [VERSE]]
སྒྲ་གཞན་དག་ནི་གནས་པ་ན། །
རྗོད་བྱེད་ཇི་ལྟར་ཐོས་པ་ཡིན། །

[Block 1938]
འདི་ལས་སྒྲ་ཙམ༌[^1423]ཐ་དད་པའི་ངོ་བོ་དང་ལྷན་ཅིག་གམ་ཐ་དད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1939]
མངོན་སུམ་གྱི་དོན་ལ་གཞན་གྱིས་བསྟན་པ་ཆེན་པོར་གྱུར་པ་མ་ཡིན་ནོ། །

[Block 1940]
དེ་བས་ན་འདིས་སྨྲ་བ་པོ་གཞན་དག་འདུག་པར་གྱུར་པ་ན། སྒྲ་འགའ་ཞིག་ཐོས་པ་དེའི་དམིགས་པའི་རྐྱེན་དག་དེ་ལས་གཞན་པ་སྒྲུབ་པ་ལ་ནུས་པ་མེད་པ༌[^1424]ངེས་པར་བྱེད་དོ། །

[Block 1941]
གལ་ཏེ་ནུས་པ་དག་ཏུ་འགྱུར་ན་དེ་སྒྲུབ་པར་བྱེད་པ་དེ་དམིགས་པར་འགྱུར་ན། དེའི་རང་བཞིན་ཅན་ཉིད་ཀྱི་རྐྱེན་དག་གིས་ཇི་ལྟར་ཅ་ཅོ་དོན་གཞན་དུ་གྱུར་པ་བྱེད་པར་འགྱུར་ཏེ། རྒྱུ་ཐ་དད་པ་མེད་པ་ལ་འབྲས་བུའི་ཐ་དད་པ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1942]
དེ་ནི་རྒྱུ་མེད་པ་ཅན་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ་ཞེས་བཤད་ཟིན་ཏེ། [^1425]ཅ་ཅོ་ལ་རྗོད་པར་བྱེད་པར་མ་ཐོས་པ་མ་ཡིན་ཏེ། ཚིག་དང་ངག་ཆོད་པ་དག་ཉེ་བར་མཚོན་པའི་ཕྱིར་རོ། །

[Block 1943 [VERSE]]
ཡང་ན་ནུས་པ་ངེས་པའི་ཕྱིར། །
ཐ་དད་སྒྲས་རྟོགས་ཇི་ལྟར་འགྱུར། །

[Block 1944]
དབང་པོ་ནུས་པ་སོ་སོར་ངེས་པ་ཅན་དེ་དག་གིས་ཀྱང་སྒྲ་སོ་སོ་ལ་ངེས་པའི་སྒྲ་ཙམ༌[^1426]ངོ་བོ་སྣ་ཚོགས་པ་ཐོས་པ་ན་སྒྲ་དག་ཉིད་མ་ཡིན་ཏེ། དེ་ལྟར་ན་སྒྲ་དག་ལ་དེ་དག་གིས་རྒྱབ་ཀྱིས་ཕྱོགས་པ་ཡིན། [^1427]རྗོད་པར་བྱེད་པ་དག་ལས་ཐ་དད་པར་སྒྲ་ཙམ་དག་གྲུབ་པ་མེད་དོ་ཞེས་བཤད་པ་གང་ཡིན་པ་ཇི་ལྟར་ན་མི་འགྲུབ་སྟེ། ཚིག་ལས་དོན་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 1945]
སྒྲ་ཙམ་གྱི་ཆ་ཤིན་ཏུ་ཆུང་བ་ལས་ནི་དོན་རྟོགས་པ་མ་ཡིན་ཞིང་དེ་གཞན་དང་འདྲེས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1946]
དེ་བས་ན༌[^1428]སྒྲ་ཙམ་གྱི་ངོ་བོ་མ་ལུས་པ་ཅན་གྱིས་བསྒྲུབ་པར་བྱ་བ་རྟོགས་པ་འདི་ནི། སྒྲ་ཙམ་ཆ་མ་ལུས་པ་ཅན་མ་ཡིན་པ་དག་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར། སྒྲའི་ངོ་བོ་གོ་རིམས་མེད་པ་ཅན་དུ་ཡོད་པ་ཅན་ཉིད་གྲུབ་པ་དང་། སྒྲ་ཙམ་གྱི་ཆ་གོ་རིམས་དང་ལྡན་པ་ཅན་གྲུབ༌[^1429]པ་ཡིན་ནོ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། གོ་རིམས་མེད་པ་ཅན་དུ་ནི་ཡི་གེ་གོ་རིམས་དང་ལྡན་པ་ལས་ཐ་དད་པ་སྔར་བཀག་པ་ཉིད་ཀྱི་ཕྱིར༌[^1430]དང་། དེ་ལྟར་ཐལ་ཆེས་པའི་ཕྱིར་རོ། །

[Block 1947]
ལས་ཀྱི་ཆ་དག་གི་སྔ་མ་དང་ཕྱི་མ་ལ་འབྲེལ་པ་མེད་པའི་ཕྱིར་དང་། ཆ་གཅིག་ལས་རྟོགས་པར་མི་འགྱུར་བའི་ཕྱིར། དེ་ལས་ཐ་དད་པ་ཅན་གྱི་ལག་པའི་བརྡ་ལ་སོགས་པ་དག་ལས་ཀྱི་བདག་ཉིད་ཀྱི་ངོ་བོ་མ་ལུས་པ་ཡང་གོ་བར་བྱེད་པའི་རྒྱུར་སྒྲ་དང་འདྲ་བར་ཁས་བླང་བར་བྱ་བ༌[^1431]ཡིན་པར་འགྱུར་རོ། །

[Block 1948]
བདག་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་བྱེད་པའི་སྦྱོར་བ་ལ་ཡི་གེའི་ཆའམ་ལས་ཀྱི་ཆ་ཐ་དད་པ་གོ་རིམས་བཞིན་དུ་འབྱུང་བ་ཅན་ཉིད་ཡིན་ན། གོ་རིམས་བཞིན་དུ་རྣམ་པར་རྟོག་པའི་ཡུལ་དག་གིས་བརྡ་ཇི་ལྟ་བ་བཞིན་དུ་དོན་རྟོགས་པ་སྐྱེད་དོ་ཞེས་བྱ་བ་ནི་རིགས་པ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 1949]
གཞན་ཡང་། ཉེས་པ་གང་དང་གང་དག་གིས།[^1432] །

[Block 1950 [VERSE]]
རྗོད་བྱེད་མིན་དེའང་སྒྲ་ཙམ་འདོད། །
སྒྲ་ཙམ་དག་གིས་གསལ་བ་ན། །
ཇི་ལྟར་རྗོད་བྱེད་ལ་དེ་མེད། །

[Block 1951]
གོ་རིམས་སུ་འབྱུང་བའི་སྒྲ་ཙམ་གྱི་ཆ་དག་གིས་གསལ་བ་རྗོད་པར་བྱེད་པས་བརྗོད་པ་ཡིན་ནོ་ལོ། །

[Block 1952]
དེ་ཡང་དེ་དག་གིས་ཅིག་ཅར་གསལ་བར་བྱེད་པ་མ་ཡིན་ཏེ། གོ་རིམས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1953]
ཆ་གཅིག་གིས་ཀྱང་མ་ཡིན་ཏེ། དེ་ལས་གཞན་པ་དོན་མེད་པར་ཐལ་བའི་ཕྱིར་དང་། ཡི་གེ་ཆ་གཅིག་གི༌[^1433]དུས་ན་ངོ་བོ་མ་ལུས་པ་ཉེ་བར་རིག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1954]
དེ་བས་ན་དམིགས་པ་ཚོགས་ཤིང་ཚང་བ་ཅན་མ་ཡིན་པ་འདིས་སྒྲ་ཙམ་དང་འདྲ་བར་དམིགས་པ་ཚང་བས་བསྒྲུབ་པར་བྱ་བའི་དོན་ཇི་ལྟར་བསྒྲུབ་པར༌[^1434]འགྱུར། ཤིན་ཏུ་དམིགས་སུ་མེད་པས༌[^1435]ཡོད་པ་དང་མེད་པ་དག་ནི། དམིགས་པས་བསྒྲུབ་པར་བྱ་བའི་དོན་དག་ལ་ཁྱད་པར་ཅི་ཞིག་ཡོད། ཐག་ཉེ་བ་ཙམ་གྱིས་སྒྲུབ་པར་བྱེད་པ་ཡང་མ་ཡིན་ཏེ། གསལ་བ་ལ་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 1955]
ཡོད་པ་དང་མེད་པའི་གོ་རིམས་བཞིན་དུ་འབྱུང་བའི་ངང་ཚུལ་ཅན་དེ་ཡང་མཚུངས་པ་ཉེ་བར་སྦྱོར་བའི་ཕྱིར། སྒྲ་ཙམ་དག་གིས་བསྒྲུབ་པར༌[^1436]ནུས་པ་མ་ཡིན་ན། དེ་ལ་ཡང་དེ་ལྟར་འགྱུར་བ་དེ་ལྟར་ན་གཞན་གྱིས་ཅི་ཞིག་བྱ། དེ་བས་ན་ཡི་གེ་དང་ངག༌[^1437]ནི་སྐྱེས་བུའི༌[^1438]མ་བྱས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1956 [VERSE]]
གལ་ཏེ་ཡི་གེའི་རིམ་པ་དག །
ཡིག་རྣམ༌[^1439]ཐ་དད་མེད་ཕྱིར་མིན། །

[Block 1957]
གལ་ཏེ་དོན་གཞན་དུ་གྱུར་པའི་སྒྲའི་ངོ་བོ་ཉིད་ཀྱི་ངག་ནི་སྐྱེས་བུས་མ་བྱས་པ་མ་ཡིན་ནོ། །

[Block 1958]
འོ་ན་ཅི་ཞེ་ན། ཁོ་བོ་ཅག་གི་ཡི་གེའི་གོ་རིམས་ཀྱི་མཚན་ཉིད་ཅན་ནི་ངག་ཡིན་ཏེ། དེ་ནི་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་དུ་བསྒྲུབ་པར་བྱ་བ་ཡིན་ཞེ་ན། མ་ཡིན་ཏེ། ཡི་གེ་རྣམས་ཀྱི་གོ་རིམས་དག་ལས་ཐ་དད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1959]
འདི་ནི་ཡི་གེ་དག་ལ་དོན་གཞན་མ་ཡིན་ཏེ། སྣང་བ་ཐ་དད་པར་དམིགས་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1960]
མི་སྣང་ན་ནི་དེ་ལས་རྟོགས་པ་མེད་པའི་ཕྱིར་དང་རྟགས༌[^1440]མེད་པའི་ཕྱིར་རོ། །

[Block 1961]
གོ་རིམས་ཐ་དད་པ་དང་ལྡན་པ་ཡང་མེད་ན་ནི་ཐམས་ཅད་དུ་ཡི་གེ་ཙམ་ལུས་པའི་ཕྱིར་སྔ་མ་བཞིན་དུ་ཐལ་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1962 [VERSE]]
དེ་དག་རྣམ་པར་གཞག་པའང་མེད། །
གོ་རིམས་གཞན་ནི་འགལ་ཕྱིར་རོ། །

[Block 1963]
གལ་ཏེ་ཡི་གེ་རྣམས་ཀྱི་གོ་རིམས་མ་བྱས་པ་ཡིན་ལ། དེ་དག་རིགས་མཚུངས་པ་མང་པོ་དག་མ་ཡིན་ན། གང་གིས་འགའ་ཞིག་རྣམ་པར༌[^1441]གནས་པའི་གོ་རིམས་ཅན་དུ་འགྱུར་ཞིང་། གཞན་དག་ཇི་ལྟར་འདོད་པ་བཞིན་དུ་གཞན་དུ་འགྱུར་བ༌[^1442]ཅན་དུ་འགྱུར། འོ་ན་ཅི་ཡིན་ཞེ་ན། འཇིག་རྟེན་གསུམ་ན་ཡི་གེ་ཨ་གཅིག་ཉིད་དང་དེ་བཞིན་དུ་ཡི་གེ༌[^1443]ཡང་ངོ་། །དེའི་ཚེ་ཨག་ནི་ཞེས་བྱ་བ་ཉིད་དུ་འགྱུར་གྱི། ག་གྷ་ན་ཞེས་བྱ་བ་མ་ཡིན་ཏེ། ཡི་གེ་ཨ་དང་ག་དག་ནི་སྔ་ཕྱིའི་ངོ་བོར་རྣམ་པར་གནས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1964]
རྒྱུ་ཡོངས་སུ་གྱུར་པ་ལས་ངེས་པ་དང་ལྡན་པའི་བྱས་པ་དག་གི་ཡང་གོ་རིམས་བཟློག་པར་བྱ་བར༌[^1444]ནུས་པ་མ་ཡིན་ཏེ། དཔེར་ན་ས་བོན་དང་མྱུ་གུ་དང་ལོ་མ་ལ་སོགས་པ་དང་དུས་དང་ལོ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 1965]
མ་བྱས་པ་གནས་སྐབས་དང་རང་བཞིན་བསྐྱོད་པ་ཅན་རྣམ་པ་འགའ་ཞིག་གིས་གནས་པ་དག་ཀྱང་ཅི་སྨོས་ཏེ། སྔ་མའི་གནས་སྐབས་དོར་བ་མེད་པ་རྣམ་པ་གཞན་དུ་མི་འགྱུར་བ་མི་རུང་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
