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
གང་འདུས་མ༌[^1665]བྱས་སུ་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་དེ་བཞིན་ཉིད་སྟོང་པའི་མཚན་ཉིད་དུ་ཤེས་པ་ནི་ཡེ་ཤེས་སོ། །

[Block 1892]
རྣམ་པ༌[^1666]གཞན་བསྟན་པའི་ཕྱིར། གཞན་ལ་སྐྱེ་བ་དང་འཇིག་པ་ལ་གནས་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། མདོར་ན་གང་སྐྱེ་བ་ཡོད་པ་དང་འཇིག་པ༌[^1667]ཡོད་པའི་ཆོས་ལ་བརྟེན་པ་ནི་རྣམ་པར་ཤེས་པའོ། །

[Block 1893]
ཆོས་གང་མི་སྐྱེ་བ་དང་མི་འགག་པ་ལ་བརྟེན་ཅིང་སྐྱེ་བ་དང་འགོག་པ༌[^1668]མེད་པར་ཁོང་དུ་ཆུད་པ་ནི་ཡེ་ཤེས་སོ།། །།

[Block 1894 [HEADING]]
### ནན་ཏན་སྙིང་པོར་བྱེད་པ། ^6-3-0

[Block 1895]
ནན་ཏན་སྙིང་པོར་བྱེད་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་ངེས་པའི་དོན་གྱི་མདོ་སྡེ་ནི་གང་། དྲང་བའི་དོན་གྱི་མདོ་སྡེ་ནི་གང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ།[^1669] །མདོ་སྡེ་གང་དག་ལམ་ལ་འཇུག་པར་བསྟན་ཞེས་བྱ་བ་ལ་མདོ་སྡེ་གང་འཕགས་པའི་ལམ་གྱི་མཚན་ཉིད་བསྒོམ་པར་བྱ་བའམ། འཕགས་པའི་ལམ་གྱི་མཚན་ཉིད་རྟོགས་པར་བྱ་བའི་ཕྱིར། བཤད་པ་རྣམས་ནི་དྲང་བའི་དོན་གྱི་མདོ་སྡེ་ཞེས་བྱ་སྟེ། མྱ་ངན་ལས་འདས་པར་འདྲེན་པའི་ལམ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 1896]
མདོ་སྡེ་གང་དག་འབྲས་བུ་ལ་འཇུག་པ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་གང་ལ་མ་བསྒྲུབས་པའི་འབྲས་བུ་རྟོགས་པར་བྱ་བའི་ཕྱིར། གསུངས་པ་དེ་དག་ནི་ངེས་པའི༌[^1670]དོན་གྱི་མདོ་སྡེའོ། །

[Block 1897]
མདོ་སྡེ་གང་དག་ཀུན་རྫོབ་བསྒྲུབ་པར་བསྟན་པ་ཞེས་བྱ་བ་ལ། མདོ་སྡེ་གང་ཀུན་རྫོབ་ཀྱི་ཐ་སྙད་མང་པོ་ཐ་སྙད་ཙམ་དུ་ཡོད་པར་བསྒྲུབ་པའི༌[^1671]ཕྱིར་གསུངས་པ་དེ་དག་ནི་དྲང་བའི་དོན་གྱི༌[^1672]མདོ་སྡེའོ། །

[Block 1898]
མདོ་སྡེ་གང་དག་དོན་དམ་པར་བསྟན་པ་ཞེས་བྱ་བ་ལ་མདོ་སྡེ་གང་སྐྱེ་བ་མེད་པ་དང་འགག་པ་མེད་པའི་མཚན་ཉིད་དོན་དམ་པར་བསྟན་པའི་ཕྱིར་གསུངས་པ་དེ་དག་ནི་ངེས་པའི༌[^1673]དོན་གྱི་མདོ་སྡེའོ། །

[Block 1899]
མདོ་སྡེ་གང་དག་ལས་དང་བྱ་བ་ལ་འཇུག་པར་བསྟན་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་གང་ལས་དགེ་བ་བྱས་ན་འབྲས་བུ་ཡིད་དུ་འོང་བ༌[^1674]མྱོང་བར་འགྱུར། ལས་མི་དགེ་བ་བྱས་ན་འབྲས་བུ་ཡིད་དུ་མི་འོང་བ་མྱོང་བར་འགྱུར་བ་བསྟན་པ་དེ་དག་ནི་དྲང་བའི༌[^1675]དོན་གྱི་མདོ་སྡེའོ། །

[Block 1900]
མདོ་སྡེ་གང་དག་ལས་དང་ཉོན་མོངས་པ་ཟད་པར་བྱ་བའི་ཕྱིར་བསྟན་པ་ཞེས་བྱ་བ་ལ། མདོ་སྡེ་གང་ལས་ཟད་པར་བྱ་བ་དང་ཉོན་མོངས་པ་ཟད་པར་བྱ་བའི་ཕྱིར་དེ་དག་ཟད་པར་བྱ་བའི་ཐབས་རྣམ་པ༌[^1676]མང་པོ་བསྟན་པ་ནི༌[^1677]ངེས་པའི་དོན་གྱི་མདོ་སྡེའོ། །

[Block 1901]
མདོ་སྡེ་གང་དག་ཀུན་ནས་ཉོན་མོངས་པ་བཤད་པའི་ཕྱིར་བསྟན་པ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་གང་ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས་སུ་གྱུར་པའི་ཆོས་རྣམས་བཤད་བའི་ཕྱིར་བསྟན་པའི་མདོ་སྡེ་དེ་དག་ནི་དྲང་བའི་དོན་གྱི་མདོ་སྡེའོ། །

[Block 1902]
མདོ་སྡེ་གང་དག་རྣམ་པར་བྱང་བའི་ཡོངས་སུ་དག་པར་བྱ་བའི་ཕྱིར་བསྟན་པ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་གང་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམ་པར་བྱང་བའི་ཆོས་རྣམས་སྦྱངས་ཤིང༌[^1678]རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་གསུངས་པ་དེ་དག་ནི་ངེས་པའི་དོན་གྱི༌[^1679]མདོ་སྡེའོ། །

[Block 1903]
མདོ་སྡེ་གང་དག་འཁོར་བ་ལས་ཡིད་འབྱུང་བར་བསྟན་པ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་གང་འཁོར་བ་ལ་སྐྱོ་ཞིང་ཡིད་འབྱུང་བ་དང་། འཁོར་བ་ལ་ཆགས་པ་མེད་པར་བྱ་བའི་ཕྱིར་བསྟན་པ་དེ་དག་ནི་དྲང་བའི་དོན་གྱི་མདོ་སྡེའོ། །

[Block 1904]
མདོ་སྡེ་གང་དག་འཁོར་བ་དང་མྱ་ངན་ལས༌[^1680]འདས་པ་གཉིས་སུ་མེད་པ་ལ་འཇུག་པ་བསྟན་པ་ཞེས་བྱ་བ་ལ་མདོ་སྡེ་གང་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་གཉི་ག༌[^1681]ཡང་རང་བཞིན་མེད་པས་འཁོར་བ་སྤང་བར༌[^1682]ཡང་མི་བྱ། མྱ་ངན་ལས་འདས་པ་བླང་བར་ཡང་མི་བྱ་སྟེ། གཉི་ག་མཚན་ཉིད་གཅིག་ཏུ་འཇུག་པར་བསྟན་པ་དེ་དག་ནི་ངེས་པའི་དོན་གྱི་མདོ་སྡེའོ། །

[Block 1905]
མདོ་སྡེ་གང་དག་ཚིག་དང་ཡི་གེ་སྣ་ཚོགས་སུ་བསྟན་པ་ཞེས་བྱ་བ་ལས་མདོ་སྡེ་གང་སྤྱོད་པ་སྣ་ཚོགས་དང་། སྐྱེས་པའི་རབས་ལ་སོགས་པ་སེམས་ཅན་དྲང་བའི་དོན་དུ་ཚིག་དང་ཡི་གེ་སྣ་ཚོགས་སུ་སྙན་པར་སྦྱར་ཏེ། བསྟན་པ་ནི་དྲང་བའི་དོན་གྱི་མདོ་སྡེའོ། །

[Block 1906]
མདོ་སྡེ་གང་དག་ཟབ་མོ་མཐོང་བར་དཀའ་བ་ཁོང་དུ་ཆུད་པར་དཀའ་བ༌[^1683]ཞེས་བྱ་བ་ལ་མདོ་སྡེ་གང་གང་ཟག་དང་ཆོས་ལ་བདག་མེད་པའི་མཚན་ཉིད་སྟོང་པ་ཉིད་ཀྱི་རང་བཞིན་དམིགས་སུ་མེད་པར་མཐོང་བར་དཀའ་བ་ཁོང་དུ་ཆུད་པར་དཀའ་བར༌[^1684]བསྟན་པ་དེ་དག་ངེས་པའི་དོན་གྱི་མདོ་སྡེའོ། །

[Block 1907]
དེ་ལ་དམིགས་པ་ལ་གནས་པ་ཅན་རྣམས་ཀྱིས་ཤེས་པར་མི་ནུས་པས༌[^1685]ན་མཐོང་བར་དཀའ་བའོ། །

[Block 1908]
འཕགས་པ་ཉན་ཐོས་ལ་སོགས་པ་ཤེས་པ་ཕྱོགས་གཅིག་པ་རྣམས་ཀྱིས་ཤེས་པར་མི་ནུས་པས་ཁོང་དུ་ཆུད་པར་དཀའ་བའོ། །

[Block 1909]
མདོ་སྡེ་གང་དག་ཚིག༌[^1686]དང་ཡི་གེ་མང་ཞིང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་མདོ་སྡེ་གང་དག་ཚིག་དང་ཡི་གེ་མང་དུ་སྟོན་ཅིང་འཇིག་རྟེན་དགའ་བར་བྱ་བའི་ཕྱིར། འཇིག་རྟེན་གྱི་སྤྱོད་པ་དང་མཐུན་པར་བསྟན་པ་རྣམས་ནི་དྲང་བའི་དོན་གྱི་མདོ༌[^1687]སྡེའོ། །

[Block 1910]
མདོ་སྡེ་གང་དག་ཚིག་དང་ཡི་གེ་ཉུང་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་གང་ཚིག་དང་ཡི་གེའི་སྤྲོས་པ་ཉུང་ངུ་བྱས་ཏེ།[^1688] ཏིང་ངེ་འཛིན་དུ་བསྒོམ་པའི་མན་ངག་ཉི་ཚེ་ཙམ་དུ་སྟོན་པ་ནི་ངེས་པའི་དོན་གྱི་མདོ་སྡེའོ། །

[Block 1911]
སྒྲ་རྣམ་པ་སྣ་ཚོགས་སུ་བཤད་པ་ཞེས་བྱ་བ་ནི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལ་སོགས་པ་རྣམ་པ༌[^1689]སྣ་ཚོགས་སུ་བཤད་པའོ།། །།

[Block 1912]
[^1690]

[Block 1913 [HEADING]]
### གཞན་གྱི་དྲིང་ལ་མི་འཇོག་པ། ^6-4-0

[Block 1914]
གཞན་གྱི་དྲིང་ལ་མི་འཇོག་པར་བསྟན་པའི་ཕྱིར། དེ་ལ་ཆོས་ཉིད་ནི་གང་། གང་ཟག་ནི་གང་ཞེས་བྱ་བ་ལ༌[^1691]སོགས་པ་གསུངས་སོ། །

[Block 1915]
གང་ཟག་ཏུ་ལྟ་བ་ལ་གནས་ཏེ་གང་ཆོས་ཁ་ཅིག་ལ་རྩོམ་པ་ཞེས་བྱ་བ་ལ་གང་ཟག་རྣམ་པ་གཉིས་ཏེ། སློབ་པའི་གང་ཟག་དང་། མི་སློབ་པའི་གང་ཟག་གོ། །

[Block 1916]
དེ་ལ་སློབ་པ་དང་མི་སློབ་པའི་གང་ཟག་ཡོད་པར་ལྟ་བ་ལ་གནས་ནས་སློབ་པའི་གང་ཟག་ནི་ཡང་དག་པའི་ལྟ་བ་ལ་སོགས་པ་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་ལ་བརྩོན་པ༌[^1692]དང་། མི་སློབ་པའི་གང་ཟག་ནི༌[^1693]ཆོས་དེ་བརྒྱད་ཀྱི་སྟེང་དུ་རྣམ་པར་གྲོལ་བ་དང་། རྣམ་པར་གྲོལ་བ་ཡེ་ཤེས་མཐོང་བ་གཉིས་ཀྱིས་བསྟན་ཏེ་ཆོས་བཅུ་ལ་བརྩོན་པ་ནི། ཆོས་ཁ་ཅིག་ལ་རྩོམ་པ༌[^1694]ཞེས་བྱ་སྟེ། དེ་གཉིས་ནི་གང་ཟག་གོ། །

[Block 1917]
གང་ཟག་ཏུ་ལྟ་བ་དེའི་རྩོམ་པ་ཡོངས་སུ་ཤེས་པ་ཞེས་བྱ་བ་ནི་གང་ཟག་གི་རྩོམ་པ་གང༌[^1695]དུ་བཤད་པའི་ཆོས་རྣམས་དང་། གང་ཟག་ཉིད་དོན་དམ་པའི་མཚན་ཉིད་ཆོས་ཀྱི་དབྱིངས་ཉིད་ཕྱིན་ཅི་མ་ལོག་པར་ཤེས་པ་ནི་ཆོས་ཉིད་དོ། །

[Block 1918]
ཡང་ན་གང་ཟག་ཡོད་དོ་ཞེས་ལྟ་བ་གནས་ཏེ། གང་ཟག་དེ་ཐར་པ་དང་གྲོལ་བར་བྱ་བའི་ཕྱིར། སྦྱིན་པའམ། ཚུལ་ཁྲིམས་ལ་སོགས་པའི་ཆོས་ཁ་ཅིག་ལ་རྩོམ་པ་ནི་གང་ཟག་ཅེས་བྱའོ། །

[Block 1919]
གང་ཟག་དང་གང་ཟག་གི་དོན་དུ་བརྩམས་པའི་ཆོས་རྣམས་དངོས་པོ་མེད་པར་ཁོང་དུ་ཆུད་ནས། སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་ལ་རྩོམ་པ་ནི་ཆོས་ཉིད་ཅེས་བྱའོ། །

[Block 1920]
གང་ཟག་དང་ཆོས་ཉིད་ཀྱི་རྣམ་གྲངས་གཞན་ཡང་བསྟན་པའི་ཕྱིར། གཞན་ཡང་སོ་སོའི་སྐྱེ་བོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་ཟག་གི་རྣམ་གྲངས་སུ་གསུངས་པའོ། །

[Block 1921]
དེ་ལ་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་ལ་སོགས་པ་དགེ་བའི་ཕྱོགས་ལ་མ་ཞུགས་པ་རྣམས་ནི་སོ་སོའི་སྐྱེ་བོའི་གང་ཟག་གོ། །

[Block 1922]
སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་ལ་ཞུགས་ལ་སྤྱོད་པ་དེ་དག་མ་ཉམས་པ་རྣམས་ནི་སོ་སོའི་སྐྱེ་བོ་དགེ་བའི་གང་ཟག་གོ། །

[Block 1923]
ཚོགས་བསགས་པ་དབང་པོ་ཞན་ཏེ་མི་གཞན་གྱིས་བསྟན་པ་ལ་བརྟེན་ནས་བདེན་པ་རྟོགས་པར་བྱ་བའི་ཕྱིར་སྦྱོར་བ་ནི་དད་པས་རྗེས་སུ་འབྲང་བའི་གང་ཟག་གོ། །

[Block 1924]
ཚོགས་བསགས་པ་དབང་པོ་རྣོན་པོ་རང་གི་ཤེས་རབ་ཀྱིས་བདེན་པའི་དབང་དུ་བྱས་ཏེ།[^1696] གསུངས་པའི་ཆོས་རྟོགས་པ༌[^1697]ལ་བརྟེན་ནས་བདེན་པ་རྟོགས་པར་བྱ་བ་ལ་སྤྱོད་པ༌[^1698]ནི་ཆོས་ཀྱི་རྗེས་སུ་འབྲང་བའི་གང་ཟག་གོ། །

[Block 1925]
བརྒྱད་པའི་གང་ཟག་ནི་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ཐོབ་པར་བྱ་བའི་ཕྱིར། འཇུག་པ་སྟེ། གང་མཐོང་བའི་ལམ་སེམས་ཀྱི་སྐད་ཅིག་མ་བཅོ་ལྔ་ལ་གནས་པའོ། །

[Block 1926]
མཐོང་བའི་ལམ་སེམས་ཀྱི་སྐད་ཅིག་མ་བཅུ་དྲུག་ལ་གནས་པ་ནི། རྒྱུན་དུ་ཞུགས་པའི་གང་ཟག་གོ། །

[Block 1927]
གང་བསྒོམ་པའི་ལམ་འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་རྣམ་པ༌[^1699]དྲུག་སྤངས་པའི་ལམ་ལ་གནས་པ་ནི་ལན་ཅིག་ཕྱིར་འོང་བའི་གང་ཟག་གོ། །

[Block 1928]
གང་བསྒོམ་པའི་ལམ་འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པའི་རྣམ་པ་ཐམས་ཅད་སྤངས་པའི་ལམ་ལ་གནས་པ་ནི་ཕྱིར་མི་འོང་བའི་གང་ཟག་གོ། །

[Block 1929]
སྲིད་པའི་རྩེ་མོའི་ཉོན་མོངས་པ་རྣམ་པ་དགུ་ཆར་སྤངས་པའི་ལམ་ལ་གནས་པ་ནི་དགྲ་བཅོམ་པའི་གང་ཟག་གོ། །

[Block 1930]
སངས་རྒྱས་འཇིག་རྟེན་དུ་མ་བྱུང་བའི་ཚེ་འདོད་པའི་ཁམས་སུ་སྐྱེས་ནས་གཞན་གྱི་མན་ངག་མེད་པར་ཁམས་གསུམ་གྱི་ཉོན་མོངས་པ་ཐམས་ཅད་སྤངས་ཏེ་རང་བྱང་ཆུབ་མངོན་སུམ་དུ་བྱས་པ་ནི་རང་སངས་རྒྱས་ཀྱི་གང་ཟག་གོ། །
--- END BLOCKS ---
