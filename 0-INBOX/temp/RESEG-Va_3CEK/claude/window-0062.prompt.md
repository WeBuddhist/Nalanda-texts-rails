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
[Block 2171]
ཆོས་དང་རྗེས་སུ་ཤེས་པ་གཞན་དག་ལ་ནི་གསུམ་པོ་ཐམས་ཅད་ཡོད་པས། དེའི་ཕྱིར་གནས་སྐབས་དེ་དང་དེ་དག་ཏུ་དེ༌[^1592]སྤངས་པའི་ཡོངས་སུ་ཤེས་པའི་མིང་འཐོབ་པོ། །ཤེས་པའི་འབྲས་བུ་སྤངས་པ་ནི་རྒྱུ་གསུམ་པོ་དེ་དང་།

[Block 2172 [VERSE]]
བཞི་པ་ཁམས་ལས་འདས་པ་ལས། །
ཡོངས་སུ་ཤེས་པའི་མིང་འཐོབ་སྟེ། །

[Block 2173]
ཁམས་མཐའ་དག་ལས་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར། གང་གི་ཚེ་ཁམས་ལས་ཡང་དག་པར་འདའ་བ་ནའོ། །

[Block 2174]
གཉིས་པ༌[^1593]ཀུན་དུ་སྦྱོར་བ་དང་བྲལ་བ་རྒྱུ་ལྔ་པ་དེ༌[^1594]སྨྲས་པ། རྣམ་པ་གང་ཞིག་སྤངས་ལ་གལ་ཏེ་དེ་ལ་དམིགས་པའི་ཉོན་མོངས་པ་གཞན་དང་བྲལ་བར་གྱུར་ནའོ་ཞེས་བྱ་བ་ནི། དེ་ནི༌[^1595]རྒྱུ་གཉི་ག་ཡང་དག་པར་བཅོམ་པ་དང་། ཁམས་ལས་ཡང་དག་པར་འདས་པ་ལས་གཞན་མ་ཡིན་པར༌[^1596]མི་བརྗོད་དོ། །

[Block 2175 [HEADING]]
##### ཡོངས་སུ་ཤེས་པ་དུ་ཞིག་དང་ལྡན་པ། ^2-38-2-4-0

[Block 2176]
གང་ཞིག་ཡོངས་སུ་ཤེས་པ་དུ་ཞིག་དང་ལྡན་ཞེ་ན། གཅིག་ལ་གནས༌[^1597]མིན་མཐོང་ལ་གནས་པ་ནི། །ལྔ་པའི་བར་དང་ཡང་དག་ལྡན། །རེ་ཞིག་སོ་སོའི་སྐྱེ་བོ༌[^1598]མི་ལྡན་པ་ཁོ་ནའོ། །

[Block 2177]
འཕགས་པ་མཐོང་བའི༌[^1599]ལམ་ལ་གནས་པ་ཡང་། ཀུན་འབྱུང་བ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་ལ་གནས་པའི་བར་དུ་མི་ལྡན་པ་ཉིད་དོ། །

[Block 2178]
ཀུན་འབྱུང་བ༌[^1600]ལ་ཆོས་ཤེས་པ་ནི་གཅིག་དང་ལྡན་ནོ། །

[Block 2179]
ཀུན་འབྱུང་བ༌[^1601]ལ་རྗེས་སུ་ཤེས་པ་ནི་གཉིས་དང་ལྡན་ནོ། །

[Block 2180]
འགོག་པ་ལ་ཆོས་ཤེས་པ༌[^1602]ནི་གསུམ་དང་ལྡན་ནོ། །

[Block 2181]
འགོག་པ་ལ་རྗེས་སུ་ཤེས་པ་ནི་བཞི་དང་ལྡན་ནོ། །

[Block 2182]
ལམ་ལ་ཆོས་ཤེས་པ་ནི་ལྔ་དང་ལྡན་ནོ། །

[Block 2183]
བསྒོམ་པ༌[^1603]ལ་གནས་པ་དྲུག་གམ་ནི། གཅིག་གམ་ཡང་ན་གཉིས་དང་ངོ་། །འཕགས་པའི་གང་ཟག་བསྒོམ་པའི་ལམ་ལ་གནས་པ་ལམ་ལ་རྗེས་སུ་ཤེས་པ་ལ་གནས་པ་ཇི་སྲིད་དུ། འདོད་པ་ལ་འདོད་ཆགས་དང་བྲལ་བ་མ་འཐོབ༌[^1604]པའམ། དེ་ལས་ཡོངས་སུ་ཉམས་པ་ནི་ཡོངས་སུ་ཤེས་པ་དྲུག་དང་ལྡན་ནོ། །

[Block 2184]
སྔོན་ནམ་ཕྱིས་འདོད་པ་ལ་འདོད་ཆགས་དང་བྲལ་བ་ཐོབ་པ༌[^1605]ནི། ཐ་མའི་ཆ་དང་མཐུན་པས༌[^1606]སྤངས་པའི་ཡོངས་སུ་ཤེས་པ་གཅིག་པུ་དང་ལྡན་ནོ། །

[Block 2185]
དགྲ་བཅོམ་པ་ཉིད་ཐོབ་པ་ནི། ཀུན་དུ་སྦྱོར་བ་ཐམས་ཅད་ཡོངས་སུ་གཏུགས་པའི་ཡོངས་སུ་ཤེས་པ་གཅིག་ཁོ་ན་དང་ལྡན་ནོ། །

[Block 2186]
གཟུགས་ཀྱི༌[^1607]སྤྱོད་པས༌[^1608]ཀུན་ནས་དཀྲིས་པས་ཡོངས་སུ་ཉམས་ནས། ཡང་ཐ་མའི་ཆ་དང་མཐུན་པ་སྤངས་པའི་ཡོངས་སུ་ཤེས་པ་གཅིག་དང་ལྡན་ནོ། །

[Block 2187]
གཟུགས་ཀྱི་འདོད་ཆགས་དང་བྲལ་བ་ཐོབ་པ་ནི། ཐ་མའི་ཆ་དང་མཐུན་པ་སྤངས་པ་དང་། གཟུགས་ཀྱི་འདོད་ཆགས་ཟད་པའི་ཡོངས་སུ་ཤེས་པ་གཉིས་དང་ལྡན་ནོ། །

[Block 2188]
གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཀུན་ནས་དཀྲིས་པས་ཡོངས་སུ་ཉམས་པ་ཡང་གཉིས་པོ་དེ་དག་དང་ལྡན་ནོ། །

[Block 2189]
ཅིའི་ཕྱིར། ཕྱིར་མི༌[^1609]འོང་བ་དང་། དགྲ་བཅོམ་པ་དག་གི་ཡོངས་སུ་ཤེས་པ་གཅིག་ཁོ་ནར་རྣམ་པར་གཞག་གི །མང་དུ་ནི་མ་ཡིན་ཞེ་ན། འདི་ལྟར་ཁམས་ལས་འདོད་ཆགས་དང༌[^1610]བྲལ་བ་དང་།

[Block 2190 [VERSE]]
འབྲས་བུ་ཐོབ་ཕྱིར་དེ་དག་བསྡོམས། །
ཡོངས་སུ་ཤེས་པ་རྣམས་སྡོམ་ཞིང་། །
གཅིག་ཏུ་རྣམ་པར་འཇོག་པ་ནི། །

[Block 2191]
ཁམས་ལས་འདོད་ཆགས་དང་བྲལ་བ་དང་། འབྲས་བུ་ཐོབ་པ༌[^1611]དང་རྒྱུ་གཉིས་ཀྱིས་ཡིན་ལ། དེ་གཉི་ག་ཡང་གནས་སྐབས་དེ་གཉིས་ན་སྲིད་པས། དེའི་ཕྱིར་སྤང་པ༌[^1612]ཐམས་ཅད་བསྡོམས་ཏེ་ཡོངས་སུ་ཤེས་པ་གཅིག་ཤེས༌[^1613]བྱའོ། །

[Block 2192 [HEADING]]
##### ཡོངས་སུ་ཤེས་པ་གཏོང་བ་དང་འཐོབ་པ། ^2-38-2-5-0

[Block 2193]
ཡང་གང་ཞིག་གིས་ཡོངས་སུ་ཤེས་པ་དུ་ཞིག་ཡོངས་སུ་གཏོང་ངམ། འཐོབ་ཅེ་ན།

[Block 2194 [VERSE]]
ལ་ལ་གཅིག་གཉིས་ལྔ་དང་དྲུག །
གཏོང་སྟེ་ཐོབ་པ༌[^1614]ལྔ་མིན་ནོ། །

[Block 2195]
དགྲ་བཅོམ་པ་ཉིད་དམ།

[Block 2196]
འདོད་པ་ལ་འདོད་ཆགས་དང་བྲལ་བ་ལས།

[Block 2197]
ཡོངས་སུ་ཉམས་ན་གཅིག་གཏོང༌[^1615]ངོ་། །ཕྱིར་མི་འོང་བ་གཟུགས་ཀྱི་འདོད་ཆགས་དང་བྲལ་བ་ཞིག །འདོད་པ་ལ་འདོད་ཆགས་དང་བྲལ་བ་ལས་ཡོངས་སུ་ཉམས་ན། ཡོངས་སུ་ཤེས་པ་ཉིད༌[^1616]གཏོང་ངོ་། །འདོད་ཆགས་དང་བྲལ་བ་སྔོན་དུ་འགྲོ་བ། ལམ་ལ་རྗེས་སུ་ཤེས་པ་ལ་གནས་པ་ལ་ནི་ལྔ་སྟོང༌[^1617]སྟེ། དེ་ནི་ཐ་མའི་ཆ་དང་མཐུན་པ་སྤངས་པའི་ཡོངས་སུ་ཤེས་པ་འཐོབ་པ༌[^1618]ན། ཡོངས་སུ་ཤེས་པ་སྔ་མ་ལྔ་གཏོང་ངོ་། །མཐར་གྱི་ས་པ་ལ༌[^1619]འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བར་བྱེད་པས་ནི། ཡོངས་སུ་ཤེས་པ་དྲུག་གཏོང་ངོ་། །དེ་བཞིན་དུ་ཐོབ་པ༌[^1620]ཡང་ལ་ལས་ནི་ཡོངས་སུ་ཤེས་པ་གཅིག་ཁོ་ན༌[^1621]འཐོབ་སྟེ། གང་ལ་ལ་ཞིག་གིས་སྔོན་མེད་པ་འཐོབ་བོ།[^1622] །ལ་ལས་ནི་གཉིས་ཏེ།

[Block 2198]
གང་ཞིག་གཟུགས་མེད་པའི་ཁམས་ལས།

[Block 2199]
འདོད་ཆགས་དང་བྲལ་བ་འབའ་ཞིག་ལས་ཡོངས་སུ་ཉམས་པས་སོ།[^1623] །ཁ་ཅིག་གིས་ནི་དྲུག་སྟེ། གང་ཞིག་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ལས་ཡོངས་སུ་ཉམས་པའོ། །

[Block 2200]
ལྔ་འཐོབ་པ་ནི༌[^1624]འགའ་ཡང་མེད་པ་ཉིད་དོ། །

[Block 2201]
ཡོངས་སུ་ཤེས་པའི་སྐབས་རྫོགས་སོ།། །།

[Block 2202]
ཆོས་མངོན་པའི་མཛོད་ཀྱི་བཤད་པ་ལས།

[Block 2203]
ཕྲ་རྒྱས་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི༌[^1625]གནས་ལྔ་པའོ།། །།

[Block 2204]
[^1626]སརྦ་མངྒཱ་ལཾ།། །།[^1627]

[Block 2205 [HEADING]]
## ལམ་དང་གང་ཟག་བསྟན་པ། ^3-0

[Block 2206 [HEADING]]
### མཐོང་བ་དང་བསྒོམ་པའི་ལམ། ^3-1-0

[Block 2207]
༄༅༅། །ཇི་སྐད་དུ་སྤངས་པ་ནི་ཡོངས་སུ་ཤེས་པའི་མིང་འཐོབ་པོ་ཞེས་བཤད་པ་དེ་ཡང་།

[Block 2208 [VERSE]]
བདེན་པ་མཐོང་དང་བསྒོམ་པ༌[^1628]ལས། །
ཉོན་མོངས་སྤངས་པ་ཞེས་བཤད་པ། །

[Block 2209 [HEADING]]
#### ལམ་ཟག་པ་མེད་པ་དང་ཟག་པ་དང་བཅས་པ། ^3-1-1-0

[Block 2210]
ཉོན་མོངས་པ་རྣམས་མཐོང་བས་སྤང་བར་བྱ་བ་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བ་ཡིན་ནོ་ཞེས་རྒྱས་པར་བཤད་པ། ད་ནི་མཐོང་བ་དང་བསྒོམ་པའི་ལམ་དེ་དག་ཅི་ཟག་པ་མེད་པའམ། ཟག་པ་དང་བཅས་པ་ཞེས་བརྗོད་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་འདི་དག༌[^1629]བརྗོད་དེ།
--- END BLOCKS ---
