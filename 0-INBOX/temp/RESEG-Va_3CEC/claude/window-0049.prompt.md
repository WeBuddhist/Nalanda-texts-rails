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

[Block 1721]
ངེས་པའི་ཚིག་སོ་སོ༌[^1507]ཡང་དག་པར་རིག་པ་རྣམ་གྲངས་གཞན་བསྟན་པའི་ཕྱིར། གཞན་ཡང་ངེས་པའི་ཚིག་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1722]
ཆོས་ཐམས་ཅད་འགོག་པ་ལ་ཚིག་གི༌[^1508]ཆོས་ཤེས་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་སྐྱེ་བ་མེད་པའི་མཚན་ཉིད་ལ་ངེས་པའི་ཚིག་དེས་བསྟན་ན་སྐྱེ་བ་མེད་པའི་རང་བཞིན་ཤེས་པར་བྱེད་དེ། དེ་ནི་ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་ཞེས་བྱའོ། །

[Block 1723]
དེའི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེའི་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1724]
ཐོགས་པ་མེད་པ་ཞེས་བྱ་བ་ནི་བསྟན་པར་བྱ་བ་ཐམས་ཅད་སྟོན་པའི་ཕྱིར་རོ། །

[Block 1725]
འཁྲུལ་པ་མེད་པ་ཞེས་བྱ་བ་ནི་མ་ནོར་ཅིང་ཕྱིན་ཅི་མ་ལོག་པར་སྟོན་པས་སོ། །

[Block 1726]
ཤིན་ཏུ་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་ནི་གང་བསྟན་པ་དེ་ཡང་གཏན་ལ་འབེབས་པས་སོ། །

[Block 1727]
ཟློས་པ་མེད་པའི་ཚིག་ནི་ཡང་ནས་ཡང་དུ་མི་ཟློས༌[^1509]པའི་ཕྱིར་རོ། །

[Block 1728]
མི་དྲག་པ་ནི་ཉན་པ་རྣམས་ཀྱི་རྣ་བའི་དབང་པོ་ལ་གནོད་པར་མི་བྱེད་པས་སོ། །

[Block 1729]
མ་རྟབས་པ༌[^1510]ནི་ཚིག་མྱུར་བ་དང་། དུམ་དུམ་པོར་སྨྲ་བ་མེད་པས་སོ། །

[Block 1730]
ཟུར་ཕྱིན་པ་ནི་ཚིག་དང་ཡི་གེ༌[^1511]གསལ་བར་སྨྲ་བས་སོ། །

[Block 1731]
རྣམ་པར་གསལ་བ་ནི་ཚིག་དང་ཡི་གེ་མ་ཆད་པར་སྨྲ་བའི་ཕྱིར་རོ། །

[Block 1732]
དོན་དང་ཡི་གེས་བསྐོར་བ་ནི་དོན་བཟང་པོ་དང་ཡི་གེ་བཟང་པོ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 1733]
ཇི་ལྟ་བ་བཞིན་དུ་འཁོར་ཚིམ་པར་བྱེད་པ་ནི་སོ་སོའི་སྐད་དང་སྒྲས་སོ་སོའི་བསམ་པ་ཚིམ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1734]
རྣམ་པ་སྣ་ཚོགས་པ་ནི་ཆོས་གཅིག་ལ་ཡང་རྣམ་གྲངས་དུ་མས་འཆད་པའི་ཕྱིར་རོ། །

[Block 1735]
ཟབ་མོ་ནི་དོན་ཟབ་མོ་རྟོགས་པར་བྱེད་པའམ། དོན་ཟབ་མོ་དང་མཐུན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1736]
ཟབ་པར་སྣང་བ་ནི་ངེས་པའི་ཚིག་དེ་ཉིད་གཞན་གྱིས་ཤེས་པར་དཀའ་བས་སོ། །

[Block 1737]
ཀུན་རྫོབ་དང་དོན་དམ་པས་བརྒྱན་པ་ནི་ཀུན་རྫོབ་དང་དོན་དམ་པར་འཁྲུགས༌[^1512]པའི་ཆོས་སྟོན་པའི་ཕྱིར་རོ། །

[Block 1738]
རང་གི་སེམས་རྟོག་པ༌[^1513]ནི་བདག་རང་གི་སེམས་ཀྱིས༌[^1514]དངོས་པོ་ཅི་འདྲ་བ་ཕྱིན་ཅི་མ་ལོག་པར་ཤེས་པའོ། །ཤེས་པ་རྟོགས་པ་ནི་བདག་གི༌[^1515]དོན་དང་ཚིག་གི་ཤེས་པ་དེ་ཉིད་རང་གིས་རྟོགས༌[^1516]པའོ། །

[Block 1739]
ལྟ་བ་རྟོགས་པ་ནི༌[^1517]རང་གི༌[^1518]ལྟ་བའི་གྲུབ་པའི་མཐའ་གང་ཡིན་པ་ཤེས་པའོ། །

[Block 1740]
སངས་རྒྱས་ཀྱིས༌[^1519]བཀའ་སྩལ་པ་ནི། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱང་དེ་ཁོ་ན་སྐད་གསུངས་པའི་ཕྱིར་རོ། །

[Block 1741]
སེམས་ཅན་ཐམས་ཅད་མགུ་བར་བྱེད་པ་ནི། ངེས་པའི་ཚིག་དེས་སེམས་ཅན་རྣམས་དད་པ་སྐྱེད་པའི་ཕྱིར་རོ།[^1520] །ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་བཤད་ཟིན་ཏོ།། །།

[Block 1742 [HEADING]]
### བརྗོད་པ་ཤེས་པ། ^5-4-0

[Block 1743]
བརྗོད་པ་ཤེས་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་སྤོབས་པ་སོ་སོ་ཡང་དག་པར་རིག་པ་གང་ཞེ་ན༌[^1521]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1744]
དེ་ཡང་རྣམ་པ་གསུམ་གྱིས་རིག་པར༌[^1522]བྱ་སྟེ། སྤོབས་པ་གང་ཡིན་པ་དང་། གང་ལ་སྤོབས་པ་དང་། ཇི་ལྟར་སྤོབས་པའོ། །

[Block 1745]
དེ་ལ་འདི་ལྟ་སྟེ། ཆགས་པ་མེད་པར་ལུང༌[^1523]བསྒོ་བ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། འབྲས་བུ་ཡོད་པ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་སྤོབས་པ་གང་ཡིན་པ་བསྟན་ཏོ། །

[Block 1746]
ཇི་ལྟར་དྲིས་པ་བཞིན་དུ་སྤོབས་པ་དང་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་ཀྱི་སྤྱོད་པ་ཚིམ་པར་བྱ་བ་ལ་སྤོབས་པ་སྟེ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^1524]གང་ལ་སྤོབས་པ་བསྟན་ཏོ།[^1525] །མི་དོར༌[^1526]མི་ལྐུགས༌[^1527]ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཡང་དག་པར་སྡུག་བསྔལ་ཟད་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་ཇི་ལྟར་སྤོབས་པ་བསྟན་ཏོ། །

[Block 1747 [HEADING]]
#### སྤོབས་པ་གང་ཡིན་པ། ^5-4-1-0

[Block 1748]
ཆགས་པ་མེད་པར་ལུང་བསྒོ་བ་བསྟན་པ་ཤེས་པ་ཞེས་བྱ་བ་ལ། དྲིས་པའི་ལན་ལྡོན་པ༌[^1528]ལ་ལུང་བསྒོ་བ་བསྟན་པ་ཤེས་པ་ཞེས་བྱ་སྟེ། ཆོས་དང་དོན་གང་དང་གང་དྲིས་པ་དེ་དང་དེ་དག་བསྟན་པ་ལ། བསམ་མི་དགོས་པར་ཤེས་པ་ནི༌[^1529]ཆགས་པ་མེད་པའོ། །

[Block 1749]
ཕྱད་པར༌[^1530]ལུང་བསྒོ་བ་བསྟན་པ་ཤེས་པ་ཞེས་བྱ་བ་ནི་དུས་གཅིག་ཏུ་སོ་སོ་ནས་མི་མཐུན་པ་དུ༌[^1531]མ་དྲིས་ཀྱང་ཕྱད་པར༌[^1532]བསྟན་པའི་ཕྱིར་རོ། །

[Block 1750]
ཐོགས་པ་མེད་པར་ལུང་བསྒོ་བ་བསྟན་པ་ཤེས་པ་ཞེས་བྱ་བ་ནི་པས་ཀྱི་རྒོལ་བ་ལ་སོགས་པས་ཟིལ་གྱིས་མི་ནོན་ཅིང་ཐགས་ཐོགས་མེད་པའོ། །

[Block 1751]
ཡང་ན་ཆོས་ཁ་ཅིག་སྟོན་ནུས་པ་ཁ་ཅིག་སྟོན་མི་ནུས་པ་ནི་ཆགས་པ་སྟེ། [^1533]བྱང་ཆུབ་སེམས་དཔའ་ནི་ཐམས་ཅད་སྟོན་པའི་ཕྱིར༌[^1534]ཆགས་པ་མེད་པར་ལུང་བསྒོ་བ་བསྟན་པ་ཤེས་པའོ། །

[Block 1752]
རྒྱུ་འགའ་ཞིག་ལ་བརྟེན་ནས་སྟོན་པ་ནི་ཐོགས་པ་སྟེ། གང་ལ་ཡང་མི་རྟེན་པར༌[^1535]སྟོན་པས་ཐོགས་པ་མེད་པར་ལུང་བསྒོ་བ་བསྟན་པ་ཤེས་པ་ཞེས་བྱའོ། །

[Block 1753]
མྱུར་བའི་སྤོབས་པ་ཞེས་བྱ་བ་ནི་གཞན་གྱིས༌[^1536]དྲིས་ན་མགོ་རྨོངས་པ་མེད་ཅིང་མྱུར་དུ་ལན་ལྡོན༌[^1537]ལ། ཆོས་ཀྱི་དོན་ལ་མྱུར་དུ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 1754]
ལ་གོར་དུ་སྤོབས་པ་ནི་ཟུར་ཙམ་དྲིས་པས་ཀྱང་གང་འདྲི་བའི་དོན་མ་ལུས་པ་སྟོན༌[^1538]པའི་ཕྱིར་རོ། །

[Block 1755]
མགྱོགས་པའི་སྤོབས་པ་ནི་དོན་ཕྲ་ཞིང་ཟབ་པ་རྟོག་པར༌[^1539]བྱེད་པས་སོ། །
--- END BLOCKS ---
