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
[Block 2241]
དེ་དག་ཁྱི་རྣམས་རྐང་ནས་བཟུང་ནས་ནི། །ཞེས་པ་ནས། འཁང་དུ་བཅུག་པ་དེ་ལ་དགའ་བར་བྱེད། །ཞེས་པའི༌[^1885]བར་དུ་ནི་སྤྱོད་པའི་མཚན་ཉིད་སོ་སོར་དབྱེ་བ་སྟེ། མུ་སྟེགས་ཅན་ཐར་པ་ཚོལ་བ་ནི་ཡང་དག་པའི་ཆོས་མ་ཡིན་ཏེ། སྤྱོད་པ་ཁྱི་ལྟ་བུས་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་བསྙེམས་པ་ནི་ཁྱིའི་རྐང་པ་ནས་འཛིན་པའོ། །

[Block 2242]
རབ་ཏུ་མགྲིན་དགག་ཅས༌[^1886]པ་ནི་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་ཀྱིས༌[^1887]མྱ་ངན་ལས་འདས་པའི་གནས་བདེ་བ་ལ་གནས་པར་སེམས་པ་ཉིད་ཁྱིའི་མགྲིན་པ་ལ་རྫི་བ་དང་འདྲའོ། །

[Block 2243]
ལོག་པའི་བརྟུལ་ཞུགས་ཀྱིས་རྣམ་པར་གྲོལ་བའི་དགའ་བ་ཚོལ་བ་ནི་ཁྱི་འཁང་པས་དགའ་བར་བྱེད་པ་བཞིན་ནོ། །

[Block 2244 [HEADING]]
###### **འཇིག་ཚོགས་ལ་ལྟ་བ།** ^4-3-5-4-2-1-1-1-2-3-1-2-3-0

[Block 2245]
མདོ་ལས།

[Block 2246]
གཅེར་བུ་གནས་ཤིང༌[^1888]ཉམ་ཆུང་རིད་པ་ཡི། །ཞེས་པ་ནས། རབ་ཏུ་བཀྲེས༌[^1889]ཏེ་ཁ་ཟས་ཀུན་ཚོལ་ཞིང་། །ཞེས་པའི་བར་དུ་ནི་འཇིག་ཚོགས་སུ་ལྟ་བའི་དཔེ་སྟེ། ལྷན་ཅིག་སྐྱེས་པ་དང་བརྟགས་ཏེ་སྐྱེས་པ་ནི་ཆེ་ཞིང་རིང་བའོ། །

[Block 2247]
དགེ་བའི་རྒྱུ་མེད་པར་འཛེམ་པ་དང་། ངོ་ཚ་བ་མེད་པ་ནི་གཅེར༌[^1890]བུ་ལྟ་བུའོ། །

[Block 2248]
མ་རིག་པ་དང་བཅས་པས་སྒྲིབ་པ་ནི་གནས་པ་ཡང་དག་པའི་གཞུང་གི་ཤས་ཆུང་བའི་ཕྱིར་རིད་པའོ། །

[Block 2249]
ཕུང་པོ་ལྔ་ལ་དམ་དུ་འཛིན་པའི་ཕྱིར་དེར་གནས་པའོ། །

[Block 2250]
ཉོན་མོངས་པའི་ཆོས་རྣམས་ཀྱི་རྒྱུས་བདག་ཏུ་འཛིན་པ་སྐྱེ་ཞིང་འཕེལ་བར་གྱུར་པས་གནས་དང་གནས་སུ་བདག་ཏུ་ལྟ་བ་འཕེལ་བར་བྱེད་པ་ནི་རབ་ཏུ་བཀྲེས་ཏེ་ཟས་ཚོལ་བའོ། །

[Block 2251 [HEADING]]
###### **ལྟ་བ་བསྙེམས་པ།** ^4-3-5-4-2-1-1-1-2-3-1-2-4-0

[Block 2252]
མདོ་ལས།

[Block 2253]
ལ་ལ་བ་ལང༌[^1891]གདོང་ལ་ཁབ་ཀྱི་ཁ། །ཞེས་པ་ནི་ལྟ་བ་བསྙེམས་པའི་དཔེ་སྟེ། གཞན་གྱི་ལྟ་བ་བཟང་པོ་མི་ཆུད་མི་ལོམ་ཞེས་པའི་དོན་ཏོ། །

[Block 2254 [HEADING]]
###### **མཐར་ལྟ་བ།** ^4-3-5-4-2-1-1-1-2-3-1-2-5-0

[Block 2255]
མདོ་ལས།

[Block 2256]
མི་ཙམ་དང་ནི་དེ་བཞིན་ཁྱི་ཙམ་དང་། །ཞེས་པ་འདི་ནི་མཐར༌[^1892]འཛིན་པ་བསྟན་ཏེ། ཇི་ལྟར་གླང་གི་མགོ་ལ་རྭ་གཉིས་ཡོད་པ་དང་འདྲ་བར་ལྟ་བ་བསྙེམས་པ་རྣམས་ལ་འཛིན་པ་གཉིས་འབྱུང་སྟེ། རྟག་པར་འཛིན་པ་དང་། ཆད་པར་འཛིན་པ་གཉིས་ཏེ། ཆད་པར་འཛིན་པ་ནི་རྒྱུ་དང་། འབྲས་བུ་ཐམས་ཅད་སྤངས་པའི་ཕྱིར་སྡིག་པ་ཅན་མིའི་ཤ་ཟ་བ་བཞིན་ནོ། །

[Block 2257]
རྟག་པར་འཛིན་པ་ནི་སྡིག་པ་དེ་ཙམ་དུ་མི་ཆེ་བའི་ཕྱིར་ཁྱི་ཤ་ཟ་བ་བཞིན་ནོ། །

[Block 2258]
མདོ་ལས།

[Block 2259]
ལྷུག་པའི༌[^1893]སྒྲ༌[^1894]དེ་བཤིག་ཅིང་སྒྲ་ཡང་འབྱིན། །ཞེས་པ་ནས།

[Block 2260 [VERSE]]
ཟས་ལ་སྲེད་པས་རབ་ཏུ་གདུངས་པའི་ཕྱིར། །
དེ་ན་ཕྱོགས་བཞིར་རབ་ཏུ་ལྟ་བར་བྱེད། །

[Block 2261]
ཞེས་པ༌[^1895]ནི་སྤྱོད་པ་གཞན་རྣམས་ཀྱི་དཔེ་བསྟན་ཏེ། མཐར་ལྟ་བ་འདི་གཉིས་ལ་མུ་སྟེགས་ཀྱི༌[^1896]ལྟ་བ་སུམ་ཅུ་རྩ་བདུན་ཞིག་འདིར་བསྐྱེད་པའི་ཕྱིར་སྐྲ་འཛིངས་པ་ལྟ་བུའོ། །

[Block 2262]
ཡང་དག་པའི་ལུང་གི་ཟས་དང་བྲལ་བ་ཡང་དག་པའི་གཞུང་གི་ཆུ་མ་རྙེད་པ་བཀྲེས་པ་དང་སྐོམ་པས་ནང་གི་སེམས་གདུངས་པའི་ཕྱིར་ཕྱོགས་བཞིར་ལྟ་ཞིང་སྒྲ་འབྱིན་པའོ། །

[Block 2263 [HEADING]]
###### **བསྡུ་བ།** ^4-3-5-4-2-1-1-1-2-3-1-3-0

[Block 2264]
མདོ་ལས།

[Block 2265]
རྟག་ཏུ་སྐར་ཁུང་དང་མཐངས༌[^1897]དག་ནས་ཀྱང་། །ཞེས་ནས་ཀྱང་ཞེས༌[^1898]པ་ནས། དེ་ལྟར་ཁྱིམ་དེ་མི་བཟད་འཇིགས་འགྱུར༌[^1899]ལ། །ཞེས་པའི་བར་དུ་ནི་བསྡུ་བ་བསྟན་ཏེ། མུ་སྟེགས་ཅན་རྣམས་ཕྱིན་ཅི་ལོག་སྣ་ཚོགས་ཀྱིས་ལོག་པར་ལྟ་བ་ནི་དཔེར་གནོད་སྦྱིན་ལ་སོགས་པའི་གདོན་ལྟ་བུ་སྟེ། ཡང་དག་པའི་ལྟ་བ་སྤངས་ཤིང་ཤེས་པ་མེད་པས་ལོག་པ་ལ་ཞེན་པ་རྣམས་སྲེད་ཅིང་ཁ་ཟས་ཀྱི༌[^1900]མནར་བ་ལྟ་བུ་སྟེ། སྐྱེ་རྒ་ན་འཆིས་འཇིགས་པ་ལས་ནམ་དུ་ཡང་མི་ཐར་ཞེས་པའོ། །

[Block 2266]
མུ་སྟེགས་ཀྱི༌[^1901]སྤྱོད་པས་ཡང་དག་པའི་ལམ་ལ་ལྟ་བ་ནི་སྐར་ཁུང་ནས་ནམ་མཁར་ལ་ལྟ་བ༌[^1902]ཙམ་མོ། །

[Block 2267 [HEADING]]
###### **དེ་དག་འབྱུང་བའི་གནས།** ^4-3-5-4-2-1-1-1-2-3-2-0

[Block 2268]
མདོ་ལས།

[Block 2269]
ཆེ་ལ་མཐོ་ཞིང་རབ་ཏུ་མི་བརྟེན༌[^1903]ནོ། །ཞེས་པ་ནས། མེ་ལྕེ་སྟོང་སྙེད་ཀུན་ཏུ་འབར་བར་གྱུར། །ཞེས་པའི་བར་དུ་ནི་འདྲེ་གདོན་སྣ་ཚོགས་དང་། ལྟས༌[^1904]སྣ་ཚོགས་གནས་པའི་ས་བསྟན་པ་སྟེ། མི་གཅིག་ཅིག་ནི་ཡོངས་སུ་དབང་འགྱུར་ལ་ཞེས་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་མོས་པས་སྤྱོད་པའི་ས་ནས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པའི་བར་དུ་འཇིག་རྟེན་ལ་གནས་ཤིང་འགྲོ་བ་སྒྲོལ་བའི་དཔེ་སྟེ། མི་དེ་ཁྱིམ་གྱི་ཕྱི་རོལ་ཏུ༌[^1905]བྱུང་ཞེས་པ་ཡང་ཇི་ལྟར་ཁྱིམ་བདག་མེད་པའི་ཁང་པ་བཅོས༌[^1906]ཤིང་ལྟ་བ་མེད་པ་འདྲུམས་ཤིང༌[^1907]ཞིག་པར་གྱུར་པ་བཞིན། བཅོམ་ལྡན་འདས་མྱ་ངན་ལས་འདས་པའི་འོག་ཏུ་འཇིག་རྟེན་ན་ཆོས་ཀྱི་བདག་པོ་མེད་པས་ཁམས་གསུམ་སྟོངས་ཞེས་པའི་དོན་ཏོ། །

[Block 2270]
མེ་ལྕེ་འབར་ཞེས་པ་ཡང་ཉོན་མོངས་པ་སྣ་ཚོགས་མཆེད༌[^1908]པས་སྐྱེ་རྒ་ན་འཆིའི་བར་དུ་བཞི་མཆེད་ཅེས་པའི་དོན་ཏོ། །

[Block 2271]
མདོ་ལས།

[Block 2272]
འོད་མ་དང་ནི་ཤིང་དག་མེས་ཚིག་སྟེ། །ཞེས་པ་ནས། །ཀ་བ་དང་ནི་རྩིག་པ་དེ་བཞིན་འབར། །ཞེས་པའི་བར་དུ་ནི་གདུང་མ་ནི་ཚོར་བའི་ཕུང་པོའི་དོན། གྲལ་བུ་ནི་རུས་པའི་དོན་གཟུགས་ཀྱི་ཕུང་པོ་ནི་ཀ་བའི་དོན་ཏེ། སྐྱེ་བ་ལ་སོགས་པ་ཕུང་པོ་ལྔ་ཁྱབ་པའི་ཕྱིར་རྩིག༌[^1909]པའི་དོན་ཏོ། །

[Block 2273]
འཇིག་པ་ནི་འདུ་བྱེད་ཀྱི་ཕུང་པོ་མི་རྟག་པའི་དོན་ཏེ། སྤྱིར་ན་ཕུང་པོ་ལྔ་པོ་འདི་འཇིགས་སུ་རུང་བ་མི་བརྟན་པ༌[^1910]སྐྱེ་བ་དང་། རྒ་བ་དང་། ན་བ་དང་། ཤི་བས་ནམ་དུ་ཡང་འཇིགས་པར༌[^1911]འགྱུར་ཞེས་པའི་དོན་ཏོ། །

[Block 2274]
ཁང་པའི་ནང་ན་མེ་དང་སྲོག་ཆགས་གནས་པའི་དཔེ་འདི་གཉིས་ལ་བྱེ་བྲག་ཅི་ཡོད་ཅེ་ན། ལུས་དང་སེམས་ཚིག་པར་བྱེད་པས་མེའི་དཔེ་བསྟན། མ་རིག་པ་ལ་སོགས་པས་ཉོན་མོངས་པས་གློ་བུར་དུ་བྱུང་བ༌[^1912]ནི་སྲོག་ཆགས་སྣ་ཚོགས་ཀྱིས་འཇིགས་པར་བྱེད་པའི་དཔེ་སྟེ། རྣམ་པར་ཤེས་པ་ནི་ཕུང་པོ་བཞི་རྣམས་ཀྱི་གནས་སུ་གྱུར་པའི་ཕྱིར་ཁང་པ་ལྟ་བུར་བལྟའོ། །

[Block 2275]
མདོ་ལས།

[Block 2276]
གནོད་སྦྱིན་ཡི་དགས་འདི་དག་སྒྲ་ཡང་འབྱིན། །ཞེས་པ་ནས། དེ་ན་ཤ་ཟ་མང་པོ་ཕན་ཚུན་རྒྱུ། །ཞེས་པའི་བར་དུ་ནི་འདོད་པ་དང་གཟུགས་ཀྱི་ཁམས་ན་ལྟས་ངན་དང་འདྲེ་གདོན་སྣ་ཚོགས་བསྟན་པ་སྟེ། འདོད་པའི་ཁམས་ན་མུ་སྟེགས་ཅན་ཁྱིམ་ནས་བྱུང་བ་དང་ཁྱིམ་ནས་མ་བྱུང་བ་གཉི་ག་ཡང་སྲེད་པའི་ཉོན་མོངས་པས་ལས་དང་འཇིག་རྟེན་གྱི་ཟང་ཟིང་ལ་རྩོད་ཅིང་སྒྲ་འབྱིན་པ་དང་། ལོག་པར་ལྟ་བའི་ཉོན་མོངས་པས༌[^1913]ལུས་ཚིག་ཅིང་གདུག་པ་སྣ་ཚོགས་ཀྱིས་གཙེས་ཞེས་པའི་དོན་ཏོ། །

[Block 2277]
མདོ་ལས།

[Block 2278]
བསོད་ནམས་མེད་པ་མེ་ཡིས༌[^1914]ཀུན་ཚིག་ནས། །ཞེས་པ་ནས། ཚིག་པར་གྱུར་པ་དག་ལ་ཁྲག་གིས་འཐོར། །ཞེས་པའི་བར་དུ་ནི་གནས་དེ་ན་དག་པའི་བསམ་གཏན་གྱིས་ཉོན་མོངས་པ་ཆོམས་པའི་ཕྱིར་ཉོན་མོངས་པ༌[^1915]མི་སྐྱེ་མོད་ཀྱི་ཡང་དག་པའི་བསོད་ནམས་ཅན་མ་ཡིན་པས་བསོད་ནམས་ཞན་པ་སྟེ། ཉོན་མོངས་པ་འདོད་ཆགས་དང་གཏི་མུག་དང་། ང་རྒྱལ་དང་ཐེ་ཚོམ་དང་། འཇིག་ཚོགས་སུ་ལྟ་བ་ལ་སོགས་པའི་ཉོན་མོངས་པས་བསྲེགས་པའི་ཕྱིར་ཉོན་མོངས་པ་མ་སྤངས་པས་གཟུགས་མེད་པའི་ཁམས་ནའང་གནོད་པ་ཡོད་པའི་ཕྱིར་ཕན་ཚུན་སོས་འདེབས་ཞེས༌[^1916]པ་དང་། རང་གི་ལྟ་བ་དམ༌[^1917]པོར་འཛིན་པ་ནི་ཁྲག་གིས་འཐོར་བ་ལྟ་བུའོ། །

[Block 2279]
མདོ་ལས།

[Block 2280]
དེ་ན༌[^1918]དུས་བྱས་ཤི་ལ་སྤྱང་ཀི་དག །ཞེས་པ༌[^1919]ནས། འཇིག་རྟེན་དག་ན་ཕྱོགས་བཞིར་རབ་ཏུ་འཐུལ། །ཞེས་པའི་བར་དུ་ནི་ཉོན་མོངས་པ་ལས་ཐར་བར་ཚོལ་ཡང་ལྟ་བ་དམ་པོར་འཛིན་པའི་ཕྱིར་མི་འཐོར་བའི༌[^1920]དོན་དུ་བསྟན་པའི་དཔེ་སྟེ། སྤྱང་ཀི་དག་ཅེས་པ་ནི་འདོད་པའི་ཁམས་ཀྱི་ཉོན་མོངས་པ་གཞན་དག་ཀྱང་བསྡུ་བ་སྟེ། གཟུགས་ཀྱི་ཁམས་ན་འདོད་པ་ལ་སོགས་པའི་ཉོན་མོངས་པ་ནི། ཕན་ཚུན་ཟ་བ་འདྲ་བར་བསྟན། ཉོན་མོངས་པའི་དྲི་ང་བ་ཕྱོགས་བཞིར་འཐུལ་བ་ནི་བསམ་གཏན་བཞི་པ་རྣམས་ཀྱི་ཉོན་མོངས་པའི་དཔེ་བསྟན་ཏོ། །
--- END BLOCKS ---
