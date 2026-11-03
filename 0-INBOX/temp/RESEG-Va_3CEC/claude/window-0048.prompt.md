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
[Block 1681]
ལྟ་བའི་འདོད་ཆགས་སྤྱོད་པ་ནི་ལྟ་བ་རྣམ་པ་སྣ་ཚོགས་ལ་ཆགས་པའོ། །

[Block 1682]
མི་བཟོད་པའི༌[^1482]འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་ཀྱི་ཤས་ཆེ་བས་དེའི་རྐྱེན་གྱིས༌[^1483]སེམས་ཀྱང་འཁྲུགས་ཤིང༌[^1484]ལུས་ཀྱི་སྤྱོད་པ་རྣམས་ཀྱང་གྱུར་པར་སྣང་བའོ། །

[Block 1683]
འཇམ་པའི་འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་ཤས་ཆུང་བས༌[^1485]དེའི་རྐྱེན་གྱིས་ལུས་དང་སེམས་འཁྲུག་པ་མེད་པའི་འདོད་ཆགས་ཅན་ནོ། །

[Block 1684]
ཡང་བའི་འདོད་ཆགས་སྤྱོད་པ་ནི་དེ་བས་ཀྱང་འདོད་ཆགས་ཤས་ཆུང་བས་འདོད་ཆགས་སྤངས་པར་སླ་བ་རྣམས་སོ། །

[Block 1685]
ཀུན་རྫོབ་ཀྱི་འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་ཀུན་རྫོབ་ཀྱི་ཐ་སྙད་མང་པོ་ལ་ཆགས་པ་རྣམས་སོ། །

[Block 1686]
སྦྱོར་བའི་འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པའི་ཆོས་ལ་ཆགས་པ་སྟེ། བསམ་པ༌[^1486]ལ་སོགས་པ་ཡང་དེ་བཞིན་ནོ། །

[Block 1687]
མཚན་ཉིད་ཀྱི་འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི། ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལ་ཆགས་པའོ། །

[Block 1688]
མཚན་ཉིད་མི་མཐུན་པའི་འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་ཁ་ཅིག་ཅི་ལ་ཆགས་པ་ཁ་ཅིག༌[^1487]ལ་ཆགས་ཏེ། འདོད་ཆགས་ཡོད་པ་མི་འདྲ་བའོ། །

[Block 1689]
རྣམ་པར་གཞག་པའི་འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི། གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་འཇིག་རྟེན་དུ་གཞག་པ་ལ་ཆགས་པའོ། །

[Block 1690]
སྔོན་གྱི་མཐའི་རྐྱེན་གྱིས༌[^1488]འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་ཆགས་པར་འགྱུར་བའི་ཡུལ་འདས་པ་རྣམས་དྲན་ནས་འདོད་ཆགས་སྐྱེ་བའོ། །

[Block 1691]
ཕྱི་མའི་མཐའི༌[^1489]རྐྱེན་གྱིས་འདོད་ཆགས་སྤྱོད་པ་ཞེས་བྱ་བ་ནི༌[^1490]མ་འོངས་པ་ན༌[^1491]ཡང་ཆགས་པར་འགྱུར་བའི༌[^1492]གཟུགས་འདི་འདྲ་བ༌[^1493]ཞིག་དང་ཕྲད་པར་གྱུར་ཅིག་ཅེས་དམིགས་པ་ལས་འདོད་ཆགས་འབྱུང་བའོ། །

[Block 1692]
ད་ལྟར་བྱུང་བའི་རྐྱེན་གྱིས༌[^1494]འདོད་ཆགས་པ་ཞེས་བྱ་བ་ནི། ད་ལྟར་འདོད་ཆགས་སྐྱེས་པའི༌[^1495]རྐྱེན་དང་ཕྲད་ནས་འདོད་ཆགས་སྐྱེས་པའོ། །

[Block 1693]
སེམས་ཅན་ནང་དུ་འདོད་ཆགས་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི། བསམ་གཏན་གྱི་རོ་ལ་ཆགས་ཤིང་འདོད་པ་ལྔའི་ཡོན་ཏན་ལ་ཆགས་པ་ཡོད་པའོ། །

[Block 1694]
ཡང་ན་ནང་དུ་སེམས་ལ་འདོད་ཆགས་འབྱུང་བའི་ཤས་ཆེ་ལ་ཕྱི་རོལ་དུ་འདོད་ཆགས་དང་འདྲ་བར་མི་སྣང་བའོ། །

[Block 1695]
སེམས་ཅན་ཕྱི་རོལ་དུ་འདོད་ཆགས་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཕྱིའི་འདོད་པའི་ཡོན་ཏན་ལ་ཆགས་པའི་ཤས་ཆེ་ལ་བསམ་གཏན་གྱི་རོ་ལ་ཆགས་པ་མེད་པའམ་ཕྱི་རོལ་གྱི་སྤྱོད་པ་འདོད་ཆགས་ཀྱི་ཤས་ཆེ་བ་འདྲ་བར་སྣང་ལ། སེམས་ལ་འདོད་ཆགས་ཀྱི་ཤས་ཆེ་བ་མ་ཡིན་པའོ། །

[Block 1696]
སེམས་ཅན་ནང་དུ་འདོད་ཆགས་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བསམ་གཏན་གྱི་རོ་ལ་ཡང་ཆགས་ཤིང་ཕྱིའི་ཡུལ་རྣམས་ལ་ཡང་ཆགས་པའམ། ནང་དུ་ཡང་འདོད་ཆགས་ཀྱི་ཤས་ཆེ་ཞིང་ཕྱི་རོལ་དུ་ཡང་འདོད་ཆགས་ཤས་ཆེ་བ་འདྲ་བར་སྣང་བའོ། །

[Block 1697]
དེ་ལས་བཟློག་ནས་སེམས་ཅན་ནང་དུ་ཡང་འདོད་ཆགས་མེད་ལ། ཕྱི་རོལ་དུ་ཡང་འདོད་ཆགས་མེད་པ་སྟེ། བསམ་གཏན་གྱི་རོ་དང་ཕྱིའི་ཡུལ་གཉི་ག་ལ་མ་ཆགས་པའོ། །

[Block 1698]
འཇུག་པ་སྟེ་ཞེས་བྱ་བ་ནི་ཆགས་པའི་ཡུལ་ལ་སེམས་འཇུག་པའམ། འདོད་ཆགས་སྤྱོད་པ་རྣམས་ཀྱི་ཚུལ་དང་རང་བཞིན་ནམ་རྣམ་པར་དབྱེ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1699]
འཇུག་པའི་སྒོ་འདིས་ཞེས་བྱ་བ་ནི་ཚུལ་འདིས་བསྒྲེས་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1700]
ཞེ་སྡང་དང་གཏི་མུག་སྤྱོད་པ་ལ་ཡང་འདོད་ཆགས་སྤྱོད་པའི་ཚུལ་བཞིན་དུ། བཅོས་མའི་ཞེ་སྡང་སྤྱོད་པ་ཞེས་བྱ་བ་ལ་སོགས་པར་སྦྱར་རོ། །

[Block 1701]
ཆ་མཉམ་པ་ལ་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་དང་ཞེ་སྡང་དང༌[^1496]གཏི་མུག་གསུམ་ཆར་ཡང་ཆེ་ཆུང་མེད་དེ་ཆ་མཉམ་པའོ། །

[Block 1702]
སེམས་ཀྱིས༌[^1497]འཇུག་པ་ཞེས་བྱ་བ་ནི་དང་པོ་ཉིད་དུ་འདོད་ཆགས་ཀྱི་སེམས་སྐྱེས་པ་ཤེས་པའོ། །

[Block 1703]
འབབ་པ་ཤེས་པ་ནི་འདོད་ཆགས་དངོས་སུ་སྤྱོད་པར་ཤེས་པའོ། །

[Block 1704]
སོ་སོ་ཅི་རིགས་པར་ཆོས་སྟོན་པ་ཤེས་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གང་ལ་ཆོས་གང་བསྟན་པར་ཤེས་པ་སྟེ། འདོད་ཆགས་ཅན་རྣམས་ལ་མི་གཙང་བ་བསྒོམ་པ་བསྟན་པར་བྱ་བ་ལ་སོགས་པ་ཤེས་པའོ། །

[Block 1705]
དུས་ལས་མི་འདའ་བར་ཤེས་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་སྨིན་པའི་དུས་དང་། ཆོས་བསྟན་པའི་དུས་ཤེས་ནས། དེ་བཞིན་དུ་སྨིན་པ་དང་ཆོས་སྟོན་པར་བྱེད་པའོ། །

[Block 1706]
སྣོད་ཀྱི་བྱེ་བྲག་ཇི་ལྟ་བ་བཞིན་ཤེས་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གང་ཆོས་གང་དང་ཐེག་པ་གང་གི་སྣོད་ཡིན་པར་ཤེས་པའོ། །

[Block 1707]
འབྲས་བུ་ཡོད་པར་ཆོས་བསྟན་པ་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཆོས་བསྟན་པ་རྣམས་ཀྱང་མཇུག་ཏུ་དོན་ཡོད་ཅིང་འབྲས་བུར༌[^1498]འགྱུར་བ་དེ་ལྟ་བུའི་ཆོས་བསྟན་པར་ཤེས་པའོ། །

[Block 1708]
མ་ཆད་མ་ལྷག་པར་ཆོས་བསྟན་པ་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཆོས་བསྟན་པ་དེ་དག་ལ་ཡང་བསྐྱེད་སྐུར་མེད་པར་བྱ་སྟེ་བསྟན་པ་ཤེས་པའོ། །

[Block 1709]
ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1710 [HEADING]]
### ཐ་སྙད་ཤེས་པ། ^5-3-0

[Block 1711]
ཐ་སྙད་ཤེས་པ་བསྟན་པའི་ཕྱིར། །དེ་ལ་ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1712]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྐད་ལ་འཇུག་པ་ཤེས་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་རྣམས་ཀྱི་སོ་སོའི་སྐད་གང་ཡིན་པ་ཤེས་པའོ། །

[Block 1713]
སྐད་ནི་སོ་སོའི་སྐད་རྣམས་སོ། །

[Block 1714]
སྒྲ་ནི་ངག་གི༌[^1499]གདངས་རྣམས་སོ། །

[Block 1715]
དབྱངས་ནི་གདངས་དེ་ཉིད་ཀྱིས༌[^1500]སྙན་པ་དང་། མི་སྙན་པའི་བྱེ་བྲག་གོ། །

[Block 1716]
ཚིག་གི་ལམ་ནི་སེམས་ཅན་སོ་སོའི་ཡི་གེ་རྣམས་སོ། །

[Block 1717]
ངེས་པའི་ཚིག་ནི༌[^1501]ཐོགས་པ་དང་བཅས་པས་གཟུགས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1718]
བརྡ་ནི་དོན་བརྡ་ཕྲད་པར་ནུས་པའི་ཚིག་རྐང་པ་ཚང་བའོ། །

[Block 1719]
སྤྱོད་པ་ནི་སེམས་ཅན་སོ་སོའི་སྤྱོད་པའམ་དོན་གང་ལ་མིང་གང་བཏགས་པའོ། །

[Block 1720]
གཞན་ཡང་ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པའི་སྤྱོད་པ་འདི་དག་ཅེས་བྱ་བ་ལ་སོགས་པ༌[^1502]ནི་ངེས་པའི་ཚིག་གི༌[^1503]གྲངས་གདགས་པ་རྣམ་པར་གཞག་པ་དང་། གང་ཟག་གདགས་པ་རྣམ་པར་གཞག་པ༌[^1504]དང་། དུས་གདགས་པ་རྣམ་པར་གཞག་པ་དང་། ཡི་གེའི་བརྡ་ཤེས་པ་གཅིག༌[^1505]གི་ཚོགས་ཀྱང་ཤེས་པ་མན་ཆད་མདོའི་ཚིག་གསུམ་གྱིས༌[^1506]གོ་རིམས་བཞིན་དུ་བསྟན་པར་ཤེས་པར་བྱའོ། །
--- END BLOCKS ---
