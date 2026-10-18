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
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་པ་ནས་བང་མཛོད་མང་པོ་དང་ལྡན་ཏེ་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་གཅིག་པོ་འདི་ཡོན་ཏན་བསམ་གྱིས་མི་ཁྱབ་པ་དང་ལྡན་ཏེ། སེམས་ཅན་རྣམ་པ་སྣ་ཚོགས་ཀྱི་རིགས་ཅན་ཐམས་ཅད་ཀྱིས་དེ་ལ་ལོངས་སྤྱོད་དུ་ཟིན་གྱིས་ཀྱང་མི་ཟད་པ་བསྟན་ཏོ། །

[Block 2172]
མདོ་ལས་སེམས་ཅན་ཀུན་ཐམས་ཅད་མཁྱེན་གྱི་ཡེ་ཤེས་དང་ལྡན་པའི་ཆོས་ཞེས་པ་ནས་གཞུང་འདིས་ཀྱང་དེ་ལྟ་བུར་རིག་པར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་འདིས་བསྡུས་པ་བསྟན་ཏེ་ཐེག་པ་གཅིག་པོ༌[^1838]སྟོན་པའི་རིགས་པ༌[^1839]དང་། རྒྱུ་དང་རྐྱེན་གྱི༌[^1840]ཐེག་པ་རྣམ་གསུམ་དུ་སྟོན་པའི་བྱེ་བྲག་དང༌[^1841]གཏན་ཚིགས་བསྟན་པས་འབྲས་བུ་བླ་ན་མེད་པ་ནི་གཅིག་ཏུ་ཟད་པར་བཤད་པ་ཡིན་ནོ།། །།

[Block 2173]
དམ་པའི་ཆོས་པུཎྜ་རཱི་ཀའི་འགྲེལ་པ། བམ་པོ་དྲུག་པ།

[Block 2174 [HEADING]]
###### ཚིགས་སུ་བཅད་པ། ^4-3-5-4-2-0

[Block 2175]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་ཚེ་ཚིགས་སུ་བཅད་པ་འདི་དག་གསུངས་སོ་ཞེས་པ་ནས། ཀ་བའི་རྩ་བ་རུལ་བར་འགྱུར། །ཞེས༌[^1842]པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་བརྒྱ་དང༌[^1843]དྲུག་ཅུ་རྩ་ལྔ་ཞིག་ཡོད་པ་ལས་དུམ་བུ་གཉིས་སུ་དབྱེ་སྟེ། དང་པོར་ཚིགས་བཅད་བརྒྱ་དང་དྲུག༌[^1844]ཅུ་རྩ་ཕྱེད་དང་ལྔས་ནི་ཆོས་དང་དཔེར་སྦྱར་བ་སྔར་སྨོས་པ་རྣམས་བསྟན་ཏེ། ཤཱ་རིའི་བུ་ཁྱོད་ལ་སོགས་པ་ཐམས་ཅད་ངའི་སྲས་ཡིན་ཞེས་པ་ལ་སོགས་པའོ། །

[Block 2176]
དེའི་འོག་ཏུ་ཚིགས་བཅད་བརྒྱད་ཅུ་ཞིག་འབྱུང་བ་དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ལ་དད་པ་བསྐྱེད་ཅིང་གཟུད༌[^1845]པའི་དོན་དུ་བསྟན་པའོ། །

[Block 2177 [HEADING]]
###### **ཆོས་དང་དཔེར་སྦྱར་བ།** ^4-3-5-4-2-1-0

[Block 2178 [HEADING]]
###### **དཔེ།** ^4-3-5-4-2-1-1-0

[Block 2179]
དང་པོ་ལ་ཡང་རྣམ་པ་གསུམ་སྟེ། ཚིགས་བཅད་དྲུག་ཅུ་རྩ་ལྔས་ནི་དཔེ་བསྟན། དེའི་འོག་གི་ཚིགས་སུ་བཅད་པ་བརྒྱད་ཀྱིས་ནི་དཔེ་དང་དོན་དུ་སྦྱར། དེའི་འོག་མ་ཚིགས་སུ་བཅད་པ་གཅིག་གིས༌[^1846]བསྡུས་པའི་དོན་བསྟན་པའོ།[^1847] །དང་པོའི་ཚིགས་སུ་བཅད་པ་དྲུག་ཅུ་རྩ་ལྔས་དཔེ་བསྟན་པ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཚིགས་བཅད་ལྔ་བཅུ་རྩ་གསུམ་གྱིས་ནི་བཀྲི་བའི་དཔེ་བསྟན། དེའི་འོག་མ་ཚིགས་སུ་བཅད་པ་བཅུ་གཉིས་ཀྱིས་ནི་ངེས་པའི་དོན་བསྟན།

[Block 2180 [HEADING]]
###### **བཀྲི་བའི་དཔེ།** ^4-3-5-4-2-1-1-1-0

[Block 2181]
དང་པོ་ལ་ཡང་རྣམ་པ་བཞིར་དབྱེ་སྟེ།

[Block 2182 [HEADING]]
###### **འཇིག་རྟེན་གསུམ་ན་དེ་བཞིན་གཤེགས་པ་བཞུགས་པའི་དཔེ།** ^4-3-5-4-2-1-1-1-1-0

[Block 2183]
དང་པོ་ཚིགས་སུ་བཅད་པ་ཕྱེད་ཀྱིས་ནི་འཇིག་རྟེན་གསུམ་ན་དེ་བཞིན་གཤེགས་པ་བཞུགས་པའི་དཔེ་བསྟན། དེའི་འོག་ཏུ་ཚིགས་སུ་བཅད་པ་སུམ་ཅུ་རྩ་ཕྱེད་དང་གསུམ་གྱིས་འགྲོ་བ་ལྔ་རྣམས་གཡང་ཟ་ཞིང་བག་ཚ་བའི་དཔེ་བསྟན། དེའི་འོག་མ་ཚིགས་སུ་བཅད་པ་བཅུ་བཞིས་ནི་ཐབས་རྣམ་པ་སྣ་ཚོགས་བཤམས་པའི་དཔེ་བསྟན། དེའི་འོག་གི་ཚིགས་བཅད་ཕྱེད་དང་བཅུ་བདུན་གྱིས་ནི་གསུང་རབ་ལ་བརྟེན་ནས་ཉོན་མོངས་པའི་ས་ནས་འབྱུང་བའི་དཔེ་བསྟན་ཏེ། འདི་ལ་ཁྱིམ་ཆེན་པོ་ཞེས་པ་ནི་ཇི་ལྟར་སྔར་དོན་རྣམ་པ་གསུམ་དུ་བསྟན་པ་བཞིན་ཏེ།

[Block 2184 [HEADING]]
###### **འགྲོ་བ་ལྔ་གཡང་ཟ་ཞིང་བག་ཚ་བའི་དཔེ།** ^4-3-5-4-2-1-1-1-2-0

[Block 2185]
ཚིགས་སུ་བཅད་པ་སུམ་ཅུ་རྩ་ཕྱེད་དང་གསུམ་གྱིས་ནི་འགྲོ་བ་ལྔ་གཡང་ཟ་བ་བསྟན་པ་ལ་སྔར་ཚིག་ལྷུག་པས་རྣམ་པ་བཞིར་ཕྱེ་སྟེ། ད་འདིར་ཚིགས་སུ་བཅད་པ་ལ་རྣམ་པ་གསུམ་དུ་དབྱེའོ། །

[Block 2186 [HEADING]]
###### **ཁང་པ་འདྲུམས་ཤིང་རུལ་པ།** ^4-3-5-4-2-1-1-1-2-1-0

[Block 2187 [HEADING]]
###### **ཁམས་གསུམ་དང་ཕུང་པོ་ལྔ་མི་རྟག་པ།** ^4-3-5-4-2-1-1-1-2-1-1-0

[Block 2188]
དང་པོའི༌[^1848]ཚིགས་བཅད་གསུམ་གྱིས་ནི་ཁང་པ་འདྲུམས་ཤིང་རུལ་པ་བསྟན། དེའི་འོག་གི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་དེ་ན་གནས་པ་མང་བར་བསྟན། དེའི་འོག་མའི་ཚིགས་བཅད་ཉི་ཤུ་རྩ་དགུས་ནི་ཕྱོགས་ཐམས་ཅད་ནས་གནོད་པ་སྣ་ཚོགས་གཡོ་བ་བསྟན། ཁང་པ་འདྲུམས་པ་ལ་ཡང་རྣམ་པ་གཉིས་སུ་ཕྱེ་སྟེ། ཚིགས་སུ་བཅད་པ་བཅུ་བཞིས་ནི་ཁམས་གསུམ་དང་ཕུང་པོ་ལྔ་རྣམས་མི་རྟག་པ་བསྟན། དེའི་འོག་གི་ཚིགས་བཅད་ལྔས་ནི་གཟུགས་ཀྱི་ཕུང་པོ་མི་རྟག་པ་དང་། བདག་མེད་པ་དང་མི་གཙང་བ་དང་སྟོང་པའི་དོན་བསྟན། ཁང་པ་རྙིང་པ་འདྲུམས་ཞེས་པ་ནི་རྣམ་པར་ཤེས་པའི་ཕུང་པོ་སྐད་ཅིག་མ་གཅིག་ལ་སྐྱེ་ཞིང་འཇིག་པ་སྒྱུ་མ་དང་འདྲ་བའི་དོན་བསྟན་ཏོ། །

[Block 2189]
ཁང་ཁྱིམ་ཆེ་ཞེས་པ་ནི་གཟུགས་ཀྱི་ཕུང་པོ་མི་རྟག་པ་དབུ་བའི་གོང་བུ་དང་འདྲའོ། །

[Block 2190]
ཀ་བའི་རྩ་བ་རུལ་པ་ཞེས་པ་ནི་འདུ་བྱེད་ཀྱི་ཕུང་པོ་སྐད་ཅིག་མ་གཅིག་ལ་སྐྱེ་ཞིང་འཇིག་པ་བྱ་བ་བཏང་བས་མེད་པ་ལ་གནས་པ་ནི་ཆུ་ཤིང་གི་སྡོང་པོ་དང༌[^1849]འདྲའོ། །

[Block 2191]
ཁྱམས་རྣམས་ཞིག་ཅེས་པ་ནི་ཚོར་བའི་ཕུང་པོ་མི་རྟག་པས་བདེ་བ་དང་བྲལ་བ་སྟེ་ཆུ་བུར་དང༌[^1850]འདྲ་བར་བསྟན་པའོ། །

[Block 2192 [HEADING]]
###### **གཟུགས་ཀྱི་ཕུང་པོ་མི་རྟག་པ་དང་བདག་མེད་པ་དང་མི་གཙང་བ་དང་སྟོང་པ།** ^4-3-5-4-2-1-1-1-2-1-2-0

[Block 2193]
མདོ་ལས།

[Block 2194]
ཁང་ཐོག་དང་ནི་སྐར་ཁུང་སྐབས་རེར་བྲལ། །ཞེས་པ་ནས། རྩྭས༌[^1851]གཡོགས་ཐམས་ཅད་འབྲུལ་ཞིང་འཛག །ཞེས་པའི༌[^1852]བར་དུ་ནི་འདུ་ཤེས་ཀྱི་ཕུང་པོ་མི་རྟག་པ་བསྟན་ཏེ། ཚིགས་སུ་བཅད་པ་འདི་ལྔས་ཀྱང་གཟུགས་ཀྱི་ཕུང་པོ་མི་རྟག་པ་ལ་སོགས་པ་བསྟན་པའི་ཕྱིར་ཏེ། ཚིགས་བཅད་གསུམ་གྱིས་ནི་མི་རྟག་པ་བསྟན། ཚིགས་སུ་བཅད་པ་གཅིག་གིས་ནི་བདག་མེད་པ་བསྟན། ཡང་གཅིག་གིས་ནི་མི་གཙང་བ་བསྟན་ཏེ། དེ་གསུམ་གྱི་ཕྱིར་སྟོང་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2195]
སྐྱོང་ནུལ༌[^1853]ཞིག་ཞེས༌[^1854]པ་ནི་ཤ་དང་བྲལ་བའི་དོན། རེ་ལྡེ་ནི་པགས་པ་དང་བྲལ་བའི་དོན། ཁ་རན་རྙིངས༌[^1855]ཞེས་པ་ནི་རུས་པ་དང་ཆུ་རྒྱུས་སུ་བྲལ་བའི་དོན། གཙུག་ལག་དང་མདོ་གཞན་དག་ལས་ཀྱང་། ལུས་འདི་ནི་མཁར་དང་ཁང་པ་འདྲ་བར་གནས་པ་སྟེ། རྣམ་པར་ཤེས་པ་བརྒྱད་ནི་མཁར་ལྟ་བུའོ། །

[Block 2196]
ཆུ་རྒྱུས་ནི་གཟུངས་ལྟ་བུའོ། །

[Block 2197]
ཤ་ནི་སྐྱོང་ནུལ༌[^1856]ལྟ་བུའོ། །

[Block 2198]
ཤིང་དང་རྡོ་ལ་སོགས་པ་ནི་རུས་པ་ལྟ་བུར་གནས་པའོ། །

[Block 2199]
འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་དང་མ་རིག་པ་ལ་སོགས་པས་གླགས་ཤིང་བརྟན་པར་གནས་པའོ། །

[Block 2200 [HEADING]]
###### **དེ་ན་གནས་པ་མང་བ།** ^4-3-5-4-2-1-1-1-2-2-0

[Block 2201]
མདོ་ལས་བརྒྱ་ཕྲག་ལྔ་དག་ལས་ནི་མི་ཉུང་བ། དེ་ན་དེ་དག་གི་ཡང་གནས་གྱུར་ལ་ཞེས་པ་ནི་མང་དུ་གནས་པའི་དོན་བསྟན་ཏོ། །

[Block 2202]
མདོ་ལས།

[Block 2203]
ཁང་ཕྲན་མང་པོ་ཤིན་ཏུ་དོག་པ་རྣམས། ། ཞེས་པ་ནས། རབ་རྩིག་པ་དག་ཀྱང་དེ་བཞིན་ཞིག །ཞེས་པའི༌[^1857]བར་དུ་ནི་འདིས་ནི་དབང་པོ་མེད་ཅིང་མི་གཙང་བའི་གནས་ལུས་འདི་རྫས་སུམ་ཅུ་རྩ་དྲུག་གིས་གླགས་ཤིང་ཁྱབ་པར་བྱས་པའི་དོན་བསྟན་ཏོ། །

[Block 2204 [HEADING]]
###### **ཕྱོགས་ཐམས་ཅད་ནས་གནོད་པ་སྣ་ཚོགས་གཡོ་བ།** ^4-3-5-4-2-1-1-1-2-3-0

[Block 2205]
མདོ་ལས།

[Block 2206]
དེ་གནས༌[^1858]བྱ་རྒོད་བྱེ་བ་དག་དང་ནི། །ཞེས་པ་ནས། མི་མ་ཡིན་མང་གནས་དང་གནས་དག་ན། །ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པ་ཉི་ཤུ་རྩ་དགུས་ཕྱོགས་སྣ་ཚོགས་ནས་གནོད་པའི་ལྟས་ངན་པ༌[^1859]མང་དུ་འབྱུང་བ་བསྟན་ཏེ། དེ་ལ་ཡང་རྣམ་པ་གསུམ་དུ་དབྱེའོ། །

[Block 2207]
དང་པོ་ཚིག༌[^1860]ཕྱེད་དང་བཅོ་བརྒྱད་ཀྱིས་ནི་འདྲེ་དང་སྲིན་བུ་རྣམས་བསྟན། དེའི་འོག་ཏུ་ཚིག༌[^1861]ཕྱེད་དང་བཅུ་གཅིག་གིས་ནི་དེ་དག་འབྱུང་བའི་གནས་བསྟན། ཚིགས་བཅད་གཅིག་གིས་ནི་བསྡུས་པའི་དོན་བསྟན་ཏེ། དེ་དག་ཀྱང་ཉོན་མོངས་པ་བཅུའི་མཚན་ཉིད་ལྟས་ངན་གྱི་དོན་དུ་བསྟན་ཏེ། འགྲོ་བ་རྣམས་དེ་ལ་འཇིགས་ཤིང་སྐྱོ་བ་དང་། སྤོང་དུ་གཞུག་པའི་ཕྱིར་བསྟན་ཏོ། །

[Block 2208 [HEADING]]
###### **འདྲེ་དང་སྲིན་བུ།** ^4-3-5-4-2-1-1-1-2-3-1-0

[Block 2209]
སྲོག་ཆགས་སྔ་མའི་ལྟས་ཀྱིས་ནི་གདུག་པ༌[^1862]ཆུང་ཞིང་གནོད་པ་བགས་ཀྱིས་བྱེད་པའི་དོན་ཏེ། འདོད་ཆགས་ལ་སོགས་པ་ལྔ་དང་སྦྱར་རོ། །

[Block 2210]
དེའི་འོག་མ་འདྲེ་གདོན་མཐུ་ཆེ་ལ་གནོད་པ་མྱུར་བར༌[^1863]བྱེད་པའི་དཔེས་ནི་ལྟ་བ་རྣམ་པ༌[^1864]ལྔ་བསྟན༌[^1865]ཏོ། །
--- END BLOCKS ---
