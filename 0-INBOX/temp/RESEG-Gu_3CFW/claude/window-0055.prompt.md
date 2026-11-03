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
སོ་སོར་ཐར་པ་འདོན་པ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་ངོ་། །དགག་དབྱེ་ཞེས་བྱ་བ་ནི་ལས་བརྗོད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1927]
ཐོས་པར་བྱ་བ་མ་ཡིན་པས་ཐོས་པ་ནི་མི་འཆགས་པར༌[^1679]མི་འགྱུར་རོ་ཞེས་བྱ་བ༌[^1680]ནི། གང་ཞིག་དེ་མ་ཡིན་པ་ལ་སོགས་པའི་དབང་དུ་བྱ་སྟེ། སྨོས་པ་དེ་ནི་དེ་དག་གིས་དེ༌[^1681]ཐོས་པར་བྱ་བ་མ་ཡིན་པས་དེ་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བ་ཙམ་དུ་འགྱུར་གྱི་མི་འཆགས་པར༌[^1682]མི་འགྱུར་རོ། །

[Block 1928]
དེ་ལྟར་ཡང་ཀུན་དགའ་བོ་ཁྱོད་ཀྱིས་རྒྱལ་པོ་གསོ་སྦྱོང་གི་ཕྱིར། སོ་སོར་ཐར་པ་འདོན་པ་ཉན་དུ་མ་བཅུག་པ་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1929]
མི་འཆགས་པ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལས་གང་འདི་ལ་འཆགས་པ༌[^1683]མེད་པ་དེ་ནི་མི་འཆགས་པ་སྟེ་ལས་དེ༌[^1684]མི་བྱའོ། །

[Block 1930]
གང་ཞིག་ཆོས་མ་ཡིན་པའི་ལས་རྣམས་ལ་དེས་ནི་དགེ་འདུན་ལ་ཡང་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་འདོད་པ་བས་ན༌[^1685]མདོ་འདིའོ། །

[Block 1931]
ད་ནི་ཆོ་ག་ལས་འདས་ན་ལས་མི༌[^1686]འཆགས་སོ་ཞེས་སྨྲས་པ་གང་ཡིན་པ་འདི་བརྗོད་པར་བྱ་སྟེ། ཆོས་མ་ཡིན་པས་མི་བྱའོ་ཞེས་བྱ་བ་ལ། ཆོས་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་གླེང་བར༌[^1687]མ་བྱས་དྲན་པར་མ་བྱས་པར་མཐུས་མངོན་སུམ་དུ་མ་གྱུར་པ་ནི་ཆོས་མ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1932]
མ་ཞི་བའི་གཞི་ལ་བརྟེན་ནས་སྐུལ་བ༌[^1688]པོས་དམ་བཅས་པ༌[^1689]ལ་མངོན་སུམ༌[^1690]དུ་རྟོག་པར་བྱེད་དེ། སྨོན་ལམ་གྱི༌[^1691]ལས་བྱེད་པ་ལ་སོགས་པ་ལས་ཀྱི༌[^1692]གཞི་ལས༌[^1693]གཞན་པ་ལ་གསུངས་པའི་ཆོ་ག་དེ་བསྡུས་པའི་མདོ་འདིའོ། །

[Block 1933]
མི་མཐུན་པ་དག་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལས་རྣམས་མི་བྱའོ། །

[Block 1934]
ཚོགས་ཀྱི་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལས་རྣམས་མི་བྱའོ། །

[Block 1935]
བཞི༌[^1694]ལ་སོགས་པའི་ལས་དག་བྱེད་ན་དགེ་འདུན་གྱི་དབྱེན་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1936]
དེ་ལྟ་བས་ན་འདི་སུན་ཕྱུང་བའོ། །

[Block 1937]
དགེ་འདུན་དུ་མ་གྱུར་པ་དག་གིས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལས་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱོར༌[^1695]རོ། །

[Block 1938]
ལས་གང་ལ་དུ་དག་དགེ་འདུན་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དབྱུང་བ་ལ་ནི་ཉི་ཤུ་ལ་སོགས་པ་ཉིད་དགེ་འདུན་ཡིན་ནོ། །

[Block 1939]
བསྙེན་པར་རྫོགས་པ་ལ་ནི་བཅུ་ལ་སོགས་པའོ། །

[Block 1940]
མཐའ་འཁོབ་དག་ཏུ་མེད་ན་ནི་འདུལ་བ་འཛིན་པ་དང་ལྔ་ལ་སོགས་པའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་བཅུ་ལ་སོགས་པ་མ་རྙེད་པ་ལ་ཆོ་ག་འདིའོ་ཞེས་བྱ་བ་ནི་བསྒྲུབ་པ་ནི་དངོས་གཞིའི་ཆོ་ག་ལ་བརྟེན་པ་ཉིད་རིགས་པ་དང་མཐུན་པའོ། །

[Block 1941]
དགེ་སློང་མ་རྣམས་ལ་ཡང་ཆོ་ག་འདི་ཡིན་ཏེ། དེ་རྣམས་ལ་ནི་ཡུལ་མཐའ་འཁོབ་ཏུ་འདུལ་བ་འཛིན་པར་གཏོགས་པའི་དྲུག་ལ་སོགས་པའི་ཚོགས་ལ་བཅུ་གཉིས་ཀྱི་ཚོགས་མ་རྙེད་ན་ཤེས་པར་བྱ་བ་ཉིད་དོ། །

[Block 1942]
ལྷག་མ་ལ་ནི་བཞི་ལ་སོགས་པའོ་ཞེས་བྱ་བ་ནི་དབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་བྱ་བའི་ལས་མ་གཏོགས་པ་དེ་དག་གི་ལྷག་མའི་ལས་ལ་ནི་དགེ་སློང་བཞི་ལ་སོགས་པ་དགེ་འདུན་ཉིད་དོ། །

[Block 1943]
དགེ་སློང་མ་རྣམས་ཀྱི༌[^1696]ལས་ནི་ཐ་དད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཡང་དགེ་སློང་རྣམས་ཀྱི་ལས་དག༌[^1697]ཀྱང་ཐ་དད་ལ་དགེ་སློང་མ་རྣམས་ཀྱི་ལས་ཀྱང་ཐ་དད་དོ་ཞེས་བྱ་བ་དེའི་བསྡུ་བ་འདིའོ། །

[Block 1944]
དགག་དབྱེ་ནི་དགེ་སློང་གི་དགེ་འདུན་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མའི་དགེ་འདུན་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི། གཉིས་ཀའི་དགེ་འདུན་ཚོགས་པ༌[^1698]དགེ་སློང་དགག་དབྱེ་བྱེད་པ་པོ་མདུན་དུ་གནས་པ་ལ་དགག་དབྱེ་བྱེད་པས་དེ་རྣམས་ཀྱི་དགག་དབྱེ་ཞེས་བྱ་བ་རྣམ་པར་གཞག་པའོ། །

[Block 1945]
གསོ་སྦྱོང་ནི་དེ་དང་མཐུན་པར༌[^1699]འགྲུབ་པ་རྣམས་ཀྱིས་སོ་ཞེས་བྱ་བ་ལ། དེ་དང་ཞེས་བྱ་བ་ནི་དགེ་སློང་གི་དགེ་འདུན་དེ་དང་སྟེ། དགེ་སློང་མ་རྣམས་ཀྱི་གསོ་སྦྱོང་ཐ་དད་པ་ཡིན་མོད་ཀྱི་གལ་ཏེ་དགེ་སློང་གི་དགེ་འདུན་དང་མཐུན་པར་གྱུར་པ་རྣམས་ཀྱི་འགྲུབ་ཀྱི་མ་གྱུར་པ་རྣམས་ཀྱི་ནི་མི་འགྲུབ༌[^1700]བོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1946]
དགེ་སློང་མ་རྣམས་ཀྱིས༌[^1701]ནི་གསོ་སྦྱོང་ཐ་དད་པ༌[^1702]བྱའོ། །

[Block 1947]
དགེ་སློང་མ་རྣམས་ཀྱིས་ཀྱང་ཐ་དད་པ་དགེ་སློང་མ་འདུན་པ་དང་གསོ་སྦྱོང་འབུལ་བ་དག་གིས་དབྱུང་བར་བྱ་ཞེས་བྱ་བ་དེ་ཙམ་ཞིག་འདིར་གསུངས་སོ། །

[Block 1948]
འདུན་པ་དང་གསོ་སྦྱོང་འབུལ་བ་དག་གིས་དབྱུང་བར་བྱ་ཞེས་བྱ་བ་ཚིག་དེ་ལས་ཤེས་པར་གྱུར་པའི་དོན་ལ་མདོ༌[^1703]དེ་བྱས་པ་སྟེ། གང་གི་ཕྱིར་ཚོགས་པ༌[^1704]མི་མཐུན་པ་ལས་གཞན་འདུན་པ་འབུལ་བ་ལས༌[^1705]དགོས་པ་མེད་དེ་གསོ་སྦྱོང་གི་ལས་འདིར་གསོ་སྦྱོང་གིས༌[^1706]གསུངས་པ། གསོ་སྦྱོང་འབུལ་བ་ལ་ཡང་ཚོགས་པ་དེ་ཉིད་མི་མཐུན་པའི་བདག་ཉིད་ཅན་གྱི་དགོས་པ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 1949]
ཇི་ལྟར་དེ་དག་གིས་དགེ་སློང་གི་དགེ་འདུན་དང་གསོ་སྦྱོང་མཐུན་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་འདུན་པ་དང་གསོ་སྦྱོང་འབུལ་བས་དེ་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འབུལ་བ་ཞེས་བྱ་བ་ནི་སྟོབས་པས་སོ། །

[Block 1950]
འདུན་པ་དང་གསོ་སྦྱོང་དགེ་སློང༌[^1707]མའི་དགེ་འདུན་གྱི་འདུན་པ་དང་། གསོ་སྦྱོང་དགེ་སློང་གི་དགེ་འདུན་ལ་དབུལ་བར༌[^1708]བྱ་བ་ནི་ཀུན་ནས་ཐོབ་པར་བྱ་སྟེ། དེ་ལྟར་ན་དེའི༌[^1709]ཚོགས་ལ་མཐུན་པ༌[^1710]འགྲུབ་པར་འགྱུར་རོ། །

[Block 1951]
འདི་ལ་གཉིས་ཀྱིས༌[^1711]བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་འདུན་པ་དང་གསོ་སྦྱོང་འབུལ་བ་འདི་ལའོ། །

[Block 1952]
གཉིས་ཀྱིས་ཞེས་བྱ་བ་ནི། དགེ་སློང་མ་གཉིས་ཀྱིས་བསྟབས་པར་བྱའོ་ཞེས་བྱ་བའི༌[^1712]དོན་ཏོ། །

[Block 1953]
དེ་གཉིས་ནུས་པ་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་འདུན་པ་དང་གསོ་སྦྱོང་འབུལ་བར་བྱེད་པ་དག་ལའོ། །

[Block 1954]
མེད་ན་གཅིག་གོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་གཉིས་ཀས༌[^1713]ནུས་པ་ཉིད་མེད་ན་ནི་གཅིག་གིས༌[^1714]ནུས་པ་ཉིད་ལ་ནི་འབུལ་བར་བརྟེན་པར་བྱ་བ་ཁོ་ན་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1955]
དགེ་སློང་གིས་དགེ་འདུན་གྱི་ལེན་པའི་དགེ་སློང་བསྐོ་བར༌[^1715]བྱའོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་འདུན་པ་དང་གསོ་སྦྱོང་དག་ལེན་པར་བྱེད་པ་དེ་བསྐོ་བར༌[^1716]བྱའོ། །

[Block 1956]
དེས་སྒོ་ཁང་དུ་བསྡད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ༌[^1717]ཞེས་བྱ་བ་ནི་ལེན་པར་བསྐོས་པའི༌[^1718]དགེ་སློང་དེས་སོ། །

[Block 1957]
འབྲོས་པ༌[^1719]ཤད་ཀྱིས༌[^1720]སྦྱང་ངོ་ཞེས་བྱ་བ་ནི་ལེན་པར་བསྐོས་པའི་དགེ་སློང་དེ་འཇིགས་པ་དང་བཅས་པའི་ཕྱིར་འབྲོས་པར་བྱེད་ན་དེ་ལ་དགེ་སློང་མ་དེ་གཉིས་ཀྱིས་ཤད་ཀྱིས་སྦྱང་བར་བྱའོ། །

[Block 1958]
དེས་ཀྱང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་དེ་གཉིས་འབྲོས་ནས་དགེ་སློང་དེས་ཀྱང་དེ་བཞིན་དུ་ཤད་ཀྱིས་སྦྱང་བར་བྱའོ། །

[Block 1959]
འབྲོས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་དེ་དང་འདུན་པ་དང་གསོ་སྦྱོང་འབུལ་བའི་དགེ་སློང་མ་དེ་གཉིས་ཀྱིས༌[^1721]འབྲོས་པར་མི་བྱའོ། །

[Block 1960]
མི་ཤེས་ན་མིང་རུས་དྲིའི༌[^1722]ཞེས་བྱ་བ་ནི་ལེན་པར་བྱེད་པའི་དགེ་སློང་དེ་མི་ཤེས་ན་འབུལ་བར་བྱེད་པའི་དགེ་སློང་མ་དེ་གཉིས་ཀྱིས་དེའི་མིང་རུས་དྲི་བར༌[^1723]བྱའོ། །

[Block 1961]
མགུ་བ་དང་དབྱུང་བ་ནི་གཉིས་ཀ་ཚོགས་པ་ལའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་གཉིས་ཀྱིས་མགུ་བར་བྱ་བ་དང་དབྱུང་བ་ནི་དགེ་སློང་མའི་དགེ་འདུན་འབའ་ཞིག་ལ་བྱ་བར་མ་ཟད་ཀྱི། གཉིས་ཀའི་དགེ་འདུན་ཚོགས་པ་དུས་གཅིག་ཏུ་གནས་གཅིག་ན་འཁོད་པ་དག་ལ་བྱའོ། །

[Block 1962]
བསྙེན་པར་རྫོགས་པར་བྱས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ཡང་གཉིས་ཀའི་དགེ་འདུན་ཚོགས་པ་ལ་བྱའོ། །

[Block 1963]
འདི་ལ་དེ་དག་གི་ཚོགས་ནི་བཅུ་གཉིས་སོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་བསྙེན་པར་རྫོགས་པར་བྱ་བ་འདི་ལ་དགེ་སློང་མ་དེ་དག་གི༌[^1724]ཚོགས་བཅུ་གཉིས་ཡན་ཆད་དོ། །

[Block 1964]
སྔོན་རོལ་གྱི་སྡོམ་པ་གཉིས་དང་། འཁོར་དང་འཁོར་མང་པོ་ཉེ་བར་གཞག་པའི་གནང་བ་སྦྱིན་པ་དང་བཅས་པའི་དགེ་འདུན་གྱི་མཐའོ་ཞེས་བྱ་བ་ནི་དེ་ནི༌[^1725]དགེ་སློང་མ་བསྙེན་པར་རྫོགས་པའི་སྔོན་རོལ་གྱི་སྡོམ་པ་གཉིས་པོ་བསླབ་པའི་སྡོམ་པ་དང་། ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པའི་སྡོམ་པ་སྦྱིན་པའོ། །

[Block 1965]
ཡང་འཁོར་ཉེ་བར་འཇོག་པའི་གནང་བ་དང་ལྷན་ཅིག་ཏུ་འཁོར་མང་པོ་ཉེ་བར་འཇོག་པའི་གནང་བ་དང་ལྷན་ཅིག་ཏུ་དེས་འདིར་བསྙེན་པར་རྫོགས་པ་དང་བཅས་པའི་དགེ་སློང་མའི་གྲངས་ཀྱི་མཐའ་ཡིན་ནོ། །
--- END BLOCKS ---
