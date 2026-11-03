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
[Block 1961]
ཡོངས་སུ་བྱང་བའི་བྱང་ཆུབ་སེམས་དཔའ༌[^1727]བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱང་མི་ཟད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་དག་མི་ཟད་པ་ཡང་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱིས་སྤྱད་པའི༌[^1728]ཡུལ་སྦྱིན་པ་ལ་སོགས་པ་མི་ཟད་པའི་ཕྱིར་རོ། །

[Block 1962]
ཡོངས་སུ་བྱང་བའི་བྱང་ཆུབ་སེམས་དཔའ་ཡང་རྣམ་པ་གཉིས་ཏེ། རྟག་པར་ཕོངས་པ་མེད་པ་དང་། ཐེ་ཚོམ༌[^1729]ཐམས་ཅད་གཅོད་པའོ། །

[Block 1963]
ཚོགས་གཉིས་ཀྱིས་བསྡུས་པའི་དོན་ཚོགས་ཀྱི་ལམ་བསྟན་པར་ཡང་སྦྱར་རོ། །

[Block 1964]
དེ་ལ་རྟག་པ༌[^1730]ཕོངས་པ་མེད་པ་གང་ཞེ་ན།

[Block 1965 [VERSE]]
གང་གིས་བསོད་ནམས་ཀྱི་ཚོགས་བསགས་པའོ། །
ཐེ་ཚོམ༌[^1731]ཐམས་ཅད་གཅོད་པ་གང་ཞེ་ན།
གང་གིས་ཡེ་ཤེས་ཀྱི་ཚོགས་བསགས་པའོ། །

[Block 1966 [HEADING]]
### བསོད་ནམས་ཀྱི་ཚོགས་མི་ཟད་པ། ^7-1-0

[Block 1967]
རྟག་པར་ཕོངས་པ་མེད་པའི་དབང་དུ་བྱས་ནས། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི༌[^1732]བསོད་ནམས་ཀྱི༌[^1733]ཚོགས་མི་ཟད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1968]
འདི་ལྟ་སྟེ་སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་དངོས་པོ་དང་ཞེས་བྱ་བ་ནི་གང་གིས། གང་ལ་གང་། ཇི་ལྟར། གང་གི་ཕྱིར། སྦྱིན་པ་ནི་སྦྱིན་པའི་བསོད་ནམས་བྱ་བའི་དངོས་པོའོ། །

[Block 1969]
དེ་ལ་གང་སྦྱིན་པ་ནི། ཕྱི་དང་ནང་གི་དངོས་པོ་སྦྱིན་པའོ། །

[Block 1970]
གང་གིས༌[^1734]སྦྱིན་པ་ནི་འདོད་མ་ཆགས་པ་ལ་སོགས་པའི་སེམས་ཀྱིས་སྦྱིན་པའོ། །

[Block 1971]
གང་ལ་སྦྱིན་པ་ནི་ཡོན་ཏན་ཅན༌[^1735]གྱི་ཞིང་དང་། ཕན་བཏགས་པའི་ཞིང་དང་། སྡུག་བསྔལ་བའི་ཞིང་ལ་སྦྱིན་པའོ། །

[Block 1972]
ཇི་ལྟར་སྦྱིན་པ་ནི་རང་གི་ལག་ནས་དུས་སུ་གུས་པར་བྱས་ཏེ༌[^1736]སྦྱིན་པའོ། །

[Block 1973]
གང་གི༌[^1737]ཕྱིར་སྦྱིན་པ་ནི་མཆོད་པ་དང་ཕན་པར་འདོད་པའི་ཕྱིར་སྦྱིན་པའོ། །

[Block 1974]
ཚུལ་ཁྲིམས་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་དངོས་པོ་ཞེས་བྱ་བ་ཡན་ལག་དྲུག་དང་ལྡན་པའི་ཚུལ་ཁྲིམས་ནི་ཚུལ་ཁྲིམས་ལས་བསོད་ནམས་བྱ་བའི་དངོས་པོ་སྟེ། ཡན་ལག་དྲུག་པོ་གང་ཞེ་ན། ཚུལ་ཁྲིམས་དང་ལྡན་པར་གནས་པ་དང་། སོ་སོར༌[^1738]ཐར་པའི་སྡོམ་པས་བསྡོམས་པ༌[^1739]དང་། ཆོ་ག་དང་སྤྱོད་ཡུལ་ཕུན་སུམ་ཚོགས་པ་དང་ཁ་ན་མ་ཐོ་བ་ཕྲ་རབ་ཙམ་ལ་ཡང་འཇིག་པར་ལྟ་བ་དང་། བསླབ་པའི་གཞི༌[^1740]རྣམས་ཡང་དག་པར་བླངས་ནས་སློབ་པ་ཞེས་གསུངས་སོ། །

[Block 1975]
བསྒོམས་པ༌[^1741]ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་དངོས་པོ་ནི་གང་བསམ་གཏན་དང་སྙོམས་པར་འཇུག་པའི་མཚན་ཉིད་མཉམ་པར་གཞག་པའི་དགེ་བ་རྣམས་སོ། །

[Block 1976]
ཡང་ན་ཆོས་རྣམས་ཡང་ནས་ཡང་དུ་སེམས་ལ་གོམས་ཤིང་འདྲིས་པར་བྱས་པ་ལས་བྱུང་བའི་བསོད་ནམས་ནི་བསྒོམས་པ་ལས་བྱུང་བའི་བསོད་ནམས༌[^1742]བྱ་བའི་དངོས་པོའོ། །

[Block 1977]
བྱམས་པའི་སེམས་ལ་སྙོམས་པར་འཇུག་པ་ནི་བྱམས་པ་གྲུབ་པར་བྱ་བའི་ཕྱིར་བྱམས་པའི་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་འཇུག་པ་ལས་བྱུང་བའམ། བྱམས་པའི་སེམས་ཀྱིས་སེམས་ཅན་ཐམས་ཅད་ལ་སྙོམས་པར་བྱེད་པ་ལས་བྱུང་བའི་བསོད་ནམས་སོ། །

[Block 1978]
དེ་བཞིན་དུ་སྙིང་རྗེ་ལ་སོགས་པ་མིང་གིས་སྨོས་པ་དགེ་བ་སྤྱད་པ༌[^1743]ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཞེས་བྱའོ། །

[Block 1979]
སྙིང་རྗེ་ཆེན་པོ་སྦྱོར་བ༌[^1744]དང་ཞེས་བྱ་བ་ནི་སྙིང་རྗེ་ཆེན་པོ་ཐོབ་པར་བྱ༌[^1745]བའི་ཕྱིར། ཏིང་ངེ་འཛིན་དུ་ཞུགས་པ་ལས་བྱུང་བའི་བསོད་ནམས་སམ། སྙིང་རྗེ་ཆེན་པོས་སེམས་ཅན་ཐམས་ཅད་ཀྱི༌[^1746]སྡུག་བསྔལ་བསལ་བར་བྱའོ་ཞེས་དམིགས་པ་ལས་བྱུང་བའི་བསོད་ནམས་སོ། །

[Block 1980]
དགེ་བ་ཐམས་ཅད་རྩོམ་པ་ཞེས་བྱ་བ་ནི་འདོད་མ་ཆགས་པ་ལ་སོགས་པ་བྱས་ཤིང་བྱེད་པ་ལས་བྱུང་བའི་བསོད་ནམས་སོ། །

[Block 1981]
བདག་དང་གཞན་གྱི་སྡིག་པ་བཤགས་པ་ཞེས་བྱ་བ་ནི་བདག་གིས་འདོད་ཆགས་དང་། ཞེ་སྡང་དང་། གཏི་མུག་གི་དབང་གིས༌[^1747]ལུས་དང་ངག་དང་ཡིད་གསུམ་གྱི་སྒོ་ནས། སྲོག་གཅོད་པ༌[^1748]ལ་སོགས་པ་བྱས་པ་བཤགས་པ་དང་། གཞན་གྱིས་བྱས་པ་འཆགས་སུ་བཅུག་པའི་རྒྱུ་ལས་བྱུང་བའི་བསོད་ནམས་སོ། །

[Block 1982]
སེམས་དང་པོ་བསྐྱེད་པ་ཞེས་བྱ་བ་ནི་མོས་པས་སྤྱོད་པའི་དུས་ན་དང་པོ་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་འམ། ས་དང་པོ་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སོ། །

[Block 1983]
ཕྱིར་མི་ལྡོག་པ་ནི༌[^1749]ས་བརྒྱད་པ་དང་དགུ་པ་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སོ། །

[Block 1984]
སྐྱེ་བ་གཅིག་གིས་ཐོགས་པ་ནི་ས་བཅུ་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སོ། །

[Block 1985]
དུས་གསུམ་དུ་ཡང་དག་པར་སྒྲུབ་པ་ཞེས་བྱ་བ་ནི་འཕགས་པ་དེ་དག་གིས་དུས་གསུམ་དུ་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་ལ་སོགས་པའི་བསོད་ནམས་བྱས་པའོ། །

[Block 1986]
དེ་དག་གི༌[^1750]བསོད་ནམས་ལ་རྗེས་སུ་ཡི་རང་བའི་རྒྱུ་ལས་བྱུང་བའི་བསོད་ནམས་ལ་ཡང་བསོད་ནམས་ཀྱི་ཚོགས་ཞེས་བྱའོ། །

[Block 1987]
བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་ཞེས་བྱ་བའི་སྐབས་སུ་ནི་འཕགས་པ་དེ་དག་གིས་རང་རང་གི༌[^1751]ཐེག་པའི་འབྲས་བུ་ཐོབ་པར་བྱ་བའི་ཕྱིར་སོ་སོའི་སྤྱོད་པ་བརྩམས་པར༌[^1752]བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའོ། །

[Block 1988]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི༌[^1753]དགེ་བའི་རྩ་བ་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་ལ་མངའ་བ་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་དང་སྟོབས་དང་མི་འཇིགས་པ༌[^1754]ལ་སོགས་པའི་དགེ་བ་རྣམས་སོ། །

[Block 1989]
རྗེས་སུ་ཡི་རང་བ་དང་ལྡན་པ་ཞེས་བྱ་བ་ལ། རྗེས་སུ་ཡི་རང་བ་ནི་དེ་དག་གི་དགེ་བའི་རྩ་བ་དང་། དགའ་བ་དང་མོས་པ་སྐྱེད་པའོ།[^1755] །ལྡན་པ་ནི་དེའི་རྒྱུ་ལས་བྱུང་བས་སོ།[^1756] །ཆོས་ཀྱི་སྦྱིན་པར་གསོལ་བ་ནི་ཆོས་བཤད་ཅིང་ཆོས་ཀྱི༌[^1757]འཁོར་ལོ་བསྐོར་བར་གསོལ་བའོ། །

[Block 1990]
སྐུ་ཚེ་བསྲིང༌[^1758]བར་གསོལ་བ་ནི་སེམས་ཅན་གྱི་དོན་དུ་མྱ་ངན་ལས་མི་འདའ་ཞིང་ད་དུང་འཇིག་རྟེན་དུ་བཞུགས་པར་གསོལ་བའོ། །

[Block 1991]
བྱང་ཆུབ་ཏུ་བསྔོ་བ་དང་ལྡན་པ་ནི་དགེ་བའི་རྩ་བ་ལ་རྗེས་སུ་ཡི་རང་བ་དང་། ཆོས་བཤད་པར་བསྐུལ་བ་དང་བཞུགས་པར་གསོལ་བ་བཏབ་པ་ལས་བྱུང་བའི་དགེ་བའི་རྩ་བ་བསགས་པ་རྣམས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པར་བྱ་བའི་ཕྱིར་བསྔོས་པ་ལས་སྐྱེས་པའི་བསོད་ནམས་ཀྱིས༌[^1759]ཚོགས་སོ། །

[Block 1992]
ཕ་རོལ་ཏུ་ཕྱིན་པའི་ལམ་སྟོན་པ་དང་ཞེས་བྱ་བ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་བཤད་ནས་དེ་ཉིད་སྤྱོད་པ་ལ་བཙུད་པའོ། །

[Block 1993]
ཡང་དག་པར་སྡུད་པ་ནི་ལོངས་སྤྱོད་ཐམས་ཅད་ལ་བཀོད་པ་ནས་དགེ་བ་ལ་བཞག་པའོ། །

[Block 1994]
གཡོ་བ་མེད་པར་རིམ་གྲོ་བྱེད་པ་ནི་སྙིང་ཐག་པ་ནས་གྲོགས་བྱེད་པའོ། །

[Block 1995]
མཐུ་ཆུང་བ་ལ་བཟོད་པས་བརྟེན་པ༌[^1760]ནི་སེམས་ཅན་དམན་པ་ཞན་པ་རྣམས་ཀྱིས་གནོད་པ་བྱས་ཀྱང་སླར་གནོད་པར༌[^1761]མི་བྱེད་ཅིང་ཁོང་ཁྲོ་བ་མི་སྐྱེ་བའོ། །

[Block 1996]
ལྟུང་བ་མི་འཆབ་པ་ནི་ཚུལ་ཁྲིམས་ཡང་དག་པར་བླངས་པ་ལས་ཉམས་པར་གྱུར་པ་རྣམས་གཞན་ལ་མཐོལ་བའོ། །

[Block 1997]
སྡིག་པ་འཆགས་པ་ནི་མཚམས་མེད་པ་ལ་སོགས་པའི་སྡིག་པ་བྱས་པ་འགྱོད་པའི་ཡིད་ཀྱིས༌[^1762]འཆགས་པའོ། །

[Block 1998]
བཞུགས་པ་ནི་ད་དུང་འཇིག་རྟེན་ན༌[^1763]བཞུགས་པའོ། །

[Block 1999]
མྱ་ངན་ལས་འདས་པ་ནི་སངས་རྒྱས་ཀྱི་བྱ་བ་མཛད་ནས་མྱ་ངན་ལས་འདས་པའོ། །

[Block 2000]
མཆོད་པ་ནི་གདུགས་དང་རྒྱལ་མཚན་དང་ན་བཟའ་ལ་སོགས་པས་མཆོད་པའོ། །
--- END BLOCKS ---
