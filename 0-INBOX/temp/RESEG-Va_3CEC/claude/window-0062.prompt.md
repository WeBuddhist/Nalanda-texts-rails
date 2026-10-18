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
བསྟན་པའི་བརྩོན་འགྲུས་ནི་ཇི་ལྟར་མཉན་ཅིང་བཟུང་བའི་ཆོས་གཞན་ལ་བསྟན་པ་ལ་འབད་པར་བྱེད་པའོ། །

[Block 2172]
ནན་ཏན་གྱི་བརྩོན་འགྲུས་ནི་མཉན་པ་དང་བཟུང་བའི་ཆོས་བསྒོམ་པར་བྱ་བ་ལ་འབད་པར་བྱེད་པའོ། །

[Block 2173]
དབེན་པ་ནི་ལུས་དབེན་པ་ལ་གནས་པ་ཚོལ་བའོ། །

[Block 2174]
རྩེ་གཅིག་པ་ནི་སེམས་དབེན་པ་ལ་ཚོལ་བའོ། །

[Block 2175]
བསམ་གཏན་དང་མངོན་པར་ཤེས་པ་ཚོལ་བ་ནི་བསམ་གཏན་ལ་བརྟེན་ནས་མངོན་པར་ཤེས་པ་ལྔ་ཐོབ་པར་བྱེད་པའོ། །

[Block 2176]
སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ལ་རྟོན་པ་ནི་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བའི་ཕྱིར་སྒོམ་གྱི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་མི་ཚོལ་བའོ། །

[Block 2177]
དེ་ལ་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ནི་བདག་མེད་པ་གཉིས་ཁོང་དུ་ཆུད་པའི་མཚན་ཉིད་དོ། །

[Block 2178]
ཆད་པ་ལ་མི་གནས་པ་ནི་ཆད་པར་མི་ལྟ་བའོ། །

[Block 2179]
རྟག་པ་ལ་མི་འཇུག་པ་ནི་རྟག་པར་མི་འཛིན་པའོ། །

[Block 2180]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དང་མི་འགལ་བ་ནི་ཆོས་ཐམས་ཅད་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་མཚན་ཉིད་དུ་ཁོང་དུ་ཆུད་པའོ། །

[Block 2181]
བདག་མེད་པ་ལ་བཟོད་པ་ནི་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་ལ་སྐྲག་པ་མེད་པའོ། །

[Block 2182]
འཇིག་རྟེན་གྱི་རྗེས་སུ་འཇུག་པ་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་དང་སེམས་ཅན་གྱི་འཇིག་རྟེན་ཇི་ལྟར་གནས་པ་བཞིན་དུ་གཉི་ག་དང་མཐུན་པར་བྱེད་པའོ། །

[Block 2183]
ཡང་ན་འཇིག་རྟེན་གྱི་སྒྲས་སྣོད་ཀྱི་འཇིག་རྟེན་དང་མཐུན་པར་བྱེད་པ་བསྟན་ཏོ། །

[Block 2184]
སེམས་ཅན་གྱི་རྗེས་སུ་འཇུག་པ་ནི་སེམས་ཅན་རྣམས་ཀྱི་སེམས་དང་སྤྱོད་པ་རྣམས་དང་མཐུན་པར་བྱེད་པའོ། །

[Block 2185]
ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པ་ནི་དམ་པའི་ཆོས་དང་མི་འགལ་བར་བྱེད་པའམ། སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པའི་ཐབས་སྣ་ཚོགས་བསྒྲུབ༌[^1886]པའོ། །

[Block 2186]
ཡེ་ཤེས་ཀྱི་རྗེས་སུ་འཇུག་པ་ནི་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པ་དང་། མཐུན་པའི་ལམ་སྒྲུབ་པར་བྱེད་པའོ། །

[Block 2187]
ཕ་རོལ་ཏུ་ཕྱིན་པའི་ལམ་ནི་སྦྱིན་པ་ལ་སོགས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གོ། །

[Block 2188]
སའི་ལམ་ནི་ས་བཅུ་རྣམས་སོ། །

[Block 2189]
བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ལམ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་སུམ་ཅུ་རྩ་བདུན་རྣམས་ཏེ་དེ་དག་ཉིད་བྱང་ཆུབ་ཐོབ༌[^1887]པར་བྱེད་པའམ། བྱང་ཆུབ་ཏུ་ཕྱིན་པར་བྱེད་པས་ན་ལམ་ཞེས་བྱའོ། །

[Block 2190]
ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཀྱི་ལམ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ས་དང་བྱང་ཆུབ་ཀྱི་ཕྱོགས་རྣམས་མཐར་ཕྱིན་ཏེ། ཡོངས་སུ་རྫོགས་ན་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་འཐོབ་པས་དེ་མ་ཐག་པའི་ལམ་ལ་བྱའོ། །

[Block 2191]
ཐོས་པས་མི་ངོམས་པ་ནི་ཐོས་པ་མང་པོས་ཆོག་མི་ཤེས་པའོ། །

[Block 2192]
བསྟན་པས༌[^1888]མི་ངོམས་པ་ནི་གཞན་ལ་ཆོས་བསྟན་པས་སྐྱོ་བ་མེད་ཅིང་ཆོག་མི་ཤེས་པའོ། །

[Block 2193]
དཔྱོད་པས་མི་ངོམས་པ་ནི་ཆོས་ཀྱི་མཚན་ཉིད་ལས་ཡང་ནས་ཡང་དུ་བརྟག་ཅིང་དཔྱོད་པ་ལ་ཆོག་མི་ཤེས་པའོ། །ཤེས་པས་མི་ངོམས་པ་ནི་ཆོས་ཀྱི་དོན་ཁོང་དུ་ཆུད་པར་བྱ་བ་དང་། བསམ་པ༌[^1889]དང་བསྒོམ་པ་ལ་ཆོག་མི་ཤེས་པའོ། །

[Block 2194 [HEADING]]
#### ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་རྣམ་གྲངས་གཞན། ^7-2-4-0

[Block 2195]
ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་རྣམ་གྲངས་གཞན་བསྟན་པའི་ཕྱིར། གཞན་ཡང་ཡེ་ཤེས་ཀྱི་ཚོགས་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ།[^1890] སེམས་ཅན་ཐམས་ཅད་ཀྱི་རྗེས་སུ་འགྲོ་བ་ནི་སྙིང་རྗེ་ཆེན་པོའི་གཟུགས་ཀྱིས༌[^1891]སེམས་ཅན་གྱི་དོན་དུ་འཁོར་བ་མ་སྤངས་པའོ། །

[Block 2196]
ཆོས་ཐམས་ཅད་ཀྱི་རྗེས་སུ་འགྲོ་བ་ནི་དེ་ལྟར་འཁོར་བ་མ་སྤངས་ཀྱང་མྱ་ངན་ལས་འདའ་པ༌[^1892]དང་ཡང་མི་འགལ་ཞིང་། མྱ་ངན་ལས་འདའ་བ༌[^1893]ཡང་མ་ཉམས་པ་སྟེ་མདོར་ན་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་བསྟན་པའོ། །

[Block 2197]
སྦྱིན་པ་ལས་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སེམས་ཅན་གྱི༌[^1894]རྗེས་སུ་འགྲོ་བ་དང་། ཆོས་ཀྱི་རྗེས་སུ་འགྲོ་བ་ཡང་གཞན་མ་ཡིན་གྱི་སྦྱིན་པ་ལ་སོགས༌[^1895]ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་པོ་འདི་རྣམས་ཏེ། །འདི་དག་སྤྱོད་པའི་ཚེ་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་དང་མཐུན་པར་བྱེད་པ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་སུ་ལྟའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2198]
དེ་བཞིན་དུ་བྱམས་པ་ལ་སོགས་པ་ཚད་མེད་པ་བཞི་ལ་ཡང་སྦྱར་རོ། །

[Block 2199]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནི་འདྲི་བ་སྟེ་གོང་དུ་བཤད་པའི་ཆོས་དེ་རྣམས་ཅིའི་ཕྱིར་ཡེ་ཤེས་ཀྱི་ཚོགས་སུ་འགྱུར་ཞེ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2200]
བྱང་ཆུབ་སེམས་དཔའི་རྩོམ་པ་ཇི་སྙེད་པ་དེ་དག་ཐམས་ཅད་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་གྲུབ་པ་ཞེས་བྱ་བ་ལ་བྱང་ཆུབ་སེམས་དཔའི་རྩོམ་པ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་དོན་ཉུང་ཞིང་བྱ་བ་ཉུང་བ་ལ་སོགས་པའི་གོང་དུ་སྨོས་པ་རྣམས་ལ་བྱ་སྟེ། དེ་རྣམས་ལས་ཀྱང་དན་ཉུང་བ་ནས་ཁྲེལ་ཡོད་པ་དང་ངོ་ཚ་ཤེས་པའི་བར་དུ་ནི་རྒྱུའི་རྩོམ་པའོ། །

[Block 2201]
ཡེ་ཤེས་ཀྱི་རྗེས་སུ་འགྲོ་བ་ལྷུར་བྱེད་པ་ནས་བརྩམས་ཏེ། མངོན་སུམ་དུ་ཤེས་པའི་བར་དུ་ནི་རང་བཞིན་གྱིས་རྩོམ༌[^1896]པའོ། །

[Block 2202]
ཡོན་ཏན་གཞན་ལ་རག་མ་ལུས་པ་ནས་བརྩམས་ཏེ། ལས་ཡོངས་སུ་དག་པའི་ཡེ་ཤེས་ཀྱི་བར་དུ་ནི་འབྲས་བུའི་རྩོམ་པ༌[^1897]སྟེ། མིང་གིས་སྨོས་པའི་རྩོམ་པ༌[^1898]དེ་དག་ཀུན་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ལ༌[^1899]དམིགས་པ་ལས་བྱུང་བ༌[^1900]ཡེ་ཤེས་ཀྱི་གྲུབ་པ་ཞེས་བྱའོ། །

[Block 2203]
གཉིས་སུ་ན་ཡེ་ཤེས་བསྒྲུབ་པ༌[^1901]ཞེས་ཀྱང་བྱ་སྟེ། རྩོམ་པ་དེ་དག་ཐམས་ཅད་ཀྱིས་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་སྒྲུབ་པའི༌[^1902]ཕྱིར་ཡེ་ཤེས་ཀྱི་ཚོགས་སོ། །

[Block 2204]
ཡེ་ཤེས་སྔོན་དུ་འགྲོ་བ་ནི་ཡེ་ཤེས་གཙོ་བོར་བྱེད་པའོ། །

[Block 2205]
ཡེ་ཤེས་ལ་རྟོན་པ་ནི་ཡེ་ཤེས་ཐོབ་པར་བྱ་བའི་ཕྱིར་སྒྲུབ་པའམ། ཡེ་ཤེས་དེ་ལ་རྟོན་པ་འམ་ཡེ་ཤེས་དང་མཐུན་པར་བྱེད་པའོ། །

[Block 2206]
ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ལ་གནས་པ་ནི་དེ་ལ་དམིགས་པའི་སྒོ་ནས་གནས་པའོ། །

[Block 2207]
ཡེ་ཤེས་དང་ལྡན་པ་ཐམས་ཅད་རྟོན་པ་ཡིན་ཞེས་པ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་ཏེ། ཤེས་པ་དང་ལྡན་པའི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་རྟོན་པ་ཡིན་ཏེ། དེ་ལ་བརྟེན་ཞིང་འདྲིས་པར༌[^1903]བྱེད་པའི་གནས་ཡིན་ཞེས༌[^1904]པའི་དོན་ཏོ། །

[Block 2208]
བདུད་ཐམས་ཅད་ཀྱིས་ཀྱང་ཞེས་བྱ་བ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་དང་ལྡན་པ་དེ་ལ་བདུད་ཐམས་ཅད་ཀྱིས་བར་ཆད་བྱ་བའི་སྐབས་མི་རྙེད་པར་འགྱུར་རོ། །

[Block 2209]
དེ་ལ་སངས་རྒྱས་ཀྱི་ཆོས་ཞེས་བྱ་བ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་དང་ལྡན་པའི་གང་ཟག་དེ་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཀྱི་སྣོད་དུ་འགྱུར་བའོ། །

[Block 2210]
སངས་རྒྱས་ཀྱི༌[^1905]བྱིན་གྱི་རླབས༌[^1906]ཞེས་བྱ་བ༌[^1907]ནི་ཡོན་ཏན་ལས་མི་ཉམས་པར་སངས་རྒྱས་ཀྱིས་བྱིན་གྱིས་བརླབ་པར་མཛད་པའོ། །
--- END BLOCKS ---
