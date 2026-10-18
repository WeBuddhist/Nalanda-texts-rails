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

[Block 1756]
འབྲས་བུ་ཡོད་པའི་སྤོབས་པ་ནི་དེའི་སྤོབས་པས་དེ་ཁོ་ན་རྟོགས༌[^1540]ཤིང་མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་བྱེད་པས་སོ། །

[Block 1757 [HEADING]]
#### གང་ལ་སྤོབས་པ། ^5-4-2-0

[Block 1758]
ཇི་ལྟར་དྲིས་པ་བཞིན་དུ་སྤོབས་པ་ནི་ཆོས་གང་དང་གང་དྲིས་པ་དེ་དང་དེ་དག་སྟོན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1759]
མི་འཕྲོགས་པའི་སྤོབས་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེའི་སྤོབས་པ་གཞན་གྱིས་ཟིལ་གྱིས་མི་ནོན་པའི་ཕྱིར་རོ། །

[Block 1760]
ཡོངས་སུ་མི་ཉམས་པའི་སྤོབས་པ་ནི་ནམས་ཀྱང་སྤོབས་པ་དེ་ལ་ཉམས་པ་མེད་པས་སོ། །

[Block 1761]
ཤིན་ཏུ་འབྲེལ་པའི་སྤོབས་པ་ནི་ཚིག་དང་དོན་དུ་འབྲེལ་པ་སྨྲ་བའི་ཕྱིར་རོ། །

[Block 1762]
རྟོགས་པའི་སྤོབས་པ་ནི་སྤོབས་པ་དེས་ཆོས་གང་དང་གང་བསྟན་པའི་ཆོས་དེ་དང་དེ་རྟོགས་པར་བྱེད་པས་སོ། །

[Block 1763]
ཆོས་ལ་དགའ་བའི་སྤོབས་པ་ནི་ཚིག་ཀྱལ་པ་སྤངས་ནས་རྟག་ཏུ་ཆོས་ཀྱི་གཏམ་ཤ་སྟག་སྨྲ་བའི་ཕྱིར་རོ། །

[Block 1764]
བཟོད་པའི་སྟོབས་ལ་གནས་པའི་སྤོབས་པ་ནི་ཚིག་རྩུབ་པོ་སྨྲས་ཀྱང་ཞེ་སྡང་མི་ལྡང་ཞིང་ཚིག་རྩུབ་པོ་མི་སྨྲ་བའི་ཕྱིར་རོ། །

[Block 1765]
ཟབ་པ་ལ་སྤོབས་པ་ནི་གཅིག༌[^1541]ཏུ་སྟོང་པ་ཉིད་ཀྱི་ཆོས་མ་ནོར་བར་སྟོན་པའི་ཕྱིར་རོ། །

[Block 1766]
སྣ་ཚོགས་ཀྱི་སྤོབས་པ་ནི་ཐ་སྙད་ཀྱི་གཏམ་སྣ་ཚོགས་སྟོན་པ་ལ་མཁས་པའི་ཕྱིར་རོ། །

[Block 1767]
ཀུན་རྫོབ་དང་དོན་དམ་པ་ལ་སྤོབས་པ་ནི་ཀུན་རྫོབ་དང་དོན་དམ་པར་བཅས་པའི་ཆོས་མ་ནོར་བར་སྟོན༌[^1542]པའི་ཕྱིར་རོ། །

[Block 1768]
སངས་རྒྱས་ཀྱི་ཆོས་ཞེས་བྱ་བ་ལ་སོགས་པས་སངས་རྒྱས་ཀྱིས་གསུངས་པའི༌[^1543]གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་ཀྱིས༌[^1544]ཚིག་སོ་སོར་ཕྱེ་སྟེ། བསྟན་པ་ལ་མཁས་ཤིང་ཐོགས་པ་མེད་པར་བསྟན་པའོ། །

[Block 1769]
གང་ངེས་པའི་ཚིག་ལ་རྟོགས་པས༌[^1545]ཚིག་གི་ཆོས་ཤེས་པ་ཞེས་བྱ་བ་ནི་སྤོབས་པ་དེས་ཐོགས་པ་དང་བཅས་པའི་ཕྱིར་གཟུགས་ཞེས་བྱ་བ་ལ་སོགས་པ་ངེས་པའི་ཚིག་གི་མཚན་ཉིད་ལ་རྟོགས་པས༌[^1546]ཚིག་ཏུ་བྱ་བའི་ཆོས་ཐམས་ཅད་ལ་མཁས་པའོ། །

[Block 1770]
འཇུག་པ་ཤེས་པའི་སྤོབས་པ་ཞེས་བྱ་བ་ནི་སྤོབས་པ་དེས༌[^1547]གོང་དུ༌[^1548]སྨོས་པ་དེ་དག་གི་མཚན་ཉིད་ལ་འཇུག །ཆོས་དེ་དག་གི་མཚན་ཉིད་རྟོག་པར༌[^1549]བྱེད་པའི་ཕྱིར་རོ། །

[Block 1771]
ཐེག་པ་ཐམས་ཅད་ལ་སྤོབས་པ་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཐམས་ཅད་སྟོན་པའི་ཕྱིར་རོ། །

[Block 1772]
ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་བསྟན་པས་ཞེས་བྱ་བ་ནི་སོ་སོ་གང་ལ་དད་པའི་ཆོས་དེ་དག་ཕྱིན་ཅི་མ་ལོག་པར་སྟོན་པས་སོ། །

[Block 1773 [HEADING]]
#### ཇི་ལྟར་སྤོབས་པ། ^5-4-3-0

[Block 1774]
མི་དོར་བ་ནི་ཚིག་ནོར་བ་མེད་པས་སོ། །

[Block 1775]
མི་ལྐུགས་པ༌[^1550]ནི་ཚིག་མི་གསལ་བ་མེད་པས་སོ། །

[Block 1776]
མི་བརླང་བའི་ཚིག་ནི་ཚིག་དང་ཡི་གེ་ཡིད་ལ་མི་འཐད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1777]
བསྟན་པ་ནི་ཆོས་རྣམས་ཕྱིན་ཅི་མ་ལོག་པར་སྟོན་པའི་ཕྱིར་རོ། །

[Block 1778]
མི་རྩུབ་པ་ནི་དོན་དམ་པར་ཁོང་དུ་ཆུད་པར་བྱ་བའི་ཐབས་སླ་བ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 1779]
ཡང་ན་མི་བརླང་བ་ནི་བསླབ་པ་ལས་འདས་ན༌[^1551]ཡང་དེ་ལས་གསོ་བའི་ཐབས་སྟོན་པའི་ཕྱིར་རོ། །

[Block 1780]
མི་རྩུབ་པ་ནི་མུ་སྟེགས་ཅན་གྱི་དཀའ་ཐུབ་བདག་ཉིད་ལ་དོན་མེད་པའི་ལམ་མི་སྟོན་པའི་ཕྱིར་རོ། །

[Block 1781]
འཇམ་པ་ནི་ཆོས་བཤད་པའི་དུས་ན་ཡང་འགྲོ་བ་རྣམས་ཀྱི་ཡིད་ཀྱི་དབང་པོ་ཚིམ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1782]
དག་པ་ནི་འཇིག་རྟེན་ལས་འདས་པའི་རྗེས་ལ་ཐོབ་པའི་ཡེ་ཤེས་དག་པས་བཤད་པའི་ཕྱིར་རོ། །

[Block 1783]
རབ་ཏུ་གྲོལ་བ༌[^1552]ནི་ཉོན་མོངས་པའི་བག་ཆགས་དང་བྲལ་ནས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 1784]
ཐོགས་པ་མེད་པ་ནི་ཚིག་དང་ཡི་གེ་ཟློས་པ་མི་སྨྲ་བའི་ཕྱིར་རོ། །

[Block 1785]
ཟུར་ཕྱིན་པ་ནི་ཚིག་དང་ཡི་གེ་ཟུར་ཆག་པ༌[^1553]མེད་པ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 1786]
ངེས་པའི་ཚིག་ནི་གཞན་ལ་ཞེ་གཅོད་པའི་ཚིག་མི་སྨྲ་བའི་ཕྱིར་རོ། །

[Block 1787]
མི་གཡོ་བའི་ཚིག་ནི་མུ་སྟེགས་ཅན་ལ་སོགས་པས་སྤ་བཀོང་བར༌[^1554]མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 1788]
ཡང་ན་འདུལ་བ་རྣམས་ཡོངས་སུ་སྨིན་པའི་དུས་ལས་མི་འདའ་བར་སྟོན་པས་ནི་མི་གཡོ་བའོ། །

[Block 1789]
བསྟོད་ཀྱང་འགྱིང་བའི་ཀུན་ནས་ཉོན་མོངས་པ་མི་སྐྱེ་བའི་ཕྱིར་མི་རྒོད་པའོ། །

[Block 1790]
སྨད་ཀྱང་ཞུམ་པའི་ཀུན་ནས་ཉོན་མོངས་པ་མི་སྐྱེ་བའི་ཕྱིར་ཞི་བའོ། །
--- END BLOCKS ---
