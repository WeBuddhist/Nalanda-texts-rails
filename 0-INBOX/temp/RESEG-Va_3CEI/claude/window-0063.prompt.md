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

[Block 2211 [HEADING]]
###### **ཉེས་པའི་སྐྱོན་བསྡུ་བ།** ^4-3-5-4-2-1-1-1-2-3-1-1-0

[Block 2212]
དེའི་འོག་གི་ཚིགས་བཅད་ཕྱེད་དང་གཉིས་ཀྱིས༌[^1866]ནི་ཉེས་པའི་སྐྱོན་བསྡུ་བ་བསྟན། དེ་ལ་ཡང་རྣམ་པ་གཉིས་སུ་ཕྱེ་སྟེ། ཚིག་ཕྱེད་དང་དྲུག་གིས་ནི་སོ་སོའི་མཚན་ཉིད་ཅི་འདྲ་བ་བསྟན། དེའི་འོག་མ་ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་བསྡུས་པའི་དོན་བསྟན།

[Block 2213]
དང་པོ་ལ་ཡང་རྣམ་པ་ལྔར་དབྱེ་སྟེ། དང་པོའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་འདོད་ཆགས་ཀྱི་དཔེ་བསྟན། དེའི་འོག་མ་ཚིགས་བཅད་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་ཞེ་སྡང་གི་དཔེ་བསྟན། དེའི་འོག་མ་ཚིགས་བཅད་གཅིག་གིས་ནི་གཏི་མུག་གི་དཔེ་བསྟན། དེའི་འོག་མ་གཅིག་གིས་ནི་ཐེ་ཚོམ་གྱི་དཔེ་བསྟན། གཅིག་གིས་ནི་ང་རྒྱལ་གྱི་དཔེ་བསྟན་ཏོ། །

[Block 2214 [HEADING]]
###### **འདོད་ཆགས།** ^4-3-5-4-2-1-1-1-2-3-1-1-1-0

[Block 2215]
འདོད་ཆགས་ལ་རྣམ་པ་བཞི་སྟེ་མངོན་དུ་ཆགས་པ་དང་། ཆགས་པར་འགྱུར་བ་དང་། ཆགས་པ་དང་ཞེན་པ་གཉིས་དང༌[^1867]ལྡན་པ་དང་། ཡུལ་དེ་དང་དེ་ལ་དགའ་ཞིང་ཆགས་པ་རྣམ་པ་བཞི་སྟེ། བྱ་རྒོད་དང་ཕུག་རོན་ལ་སོགས་པ་རིམ་པར་སྦྱར་རོ། །

[Block 2216]
བྱ་དེ་དག་འདོད་ཆགས་ཆེ་བའི་ཕྱིར་འདོད་ཆགས་བཞི་དང་བརྒྱད་དུ་སྦྱར་རོ། །

[Block 2217 [HEADING]]
###### **ཞེ་སྡང།** ^4-3-5-4-2-1-1-1-2-3-1-1-2-0

[Block 2218]
ཞེ་སྡང་ལ་ཡང་དཔེ་རྣམ་པ་བཅུ་གཅིག་སྟེ། སྦྲུལ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 2219]
དེ་ལ་ཞེ་སྡང་རྣམ་པ་བཅུ་ནི་དེའི་ལུས་ཀྱི་ཕྱིར་ཞེ་སྡང་བ་དང་། ཡིད་དུ་འོང་བའི་སེམས་ཅན་གྱི་ཕྱིར་ཞེ་སྡང་བ་དང་། ཡིད་དུ་མི་འོང་བའི་ཕྱིར་ཞེ་སྡང་བ་དང་། འདས་པའི་དགྲ་ལ་ཞེ་སྡང་བ་དང་། ད་ལྟར་གྱི་དགྲ་ལ་ཞེ་སྡང་བ་དང་། མ་འོངས་པའི་དགྲ་ལ་ཞེ་སྡང་བ་དང་། ཡིད་དུ་མི་འོང་བའི་སྤྱོད་ཡུལ་ལ་ཞེ་སྡང་བ་དང་། ཕྲག་དོག་པའི་ཕྱིར་ཞེ་སྡང་བ་དང་། སྔོན་གྱི་བག་ཆགས་ཀྱི་ཕྱིར་ཞེ་སྡང་བ་དང་། གཞན་གྱི་ཉོན་མོངས་པ་མཐོང་བས་ཞེ་སྡང་བའོ། །

[Block 2220 [HEADING]]
###### **གཏི་མུག།** ^4-3-5-4-2-1-1-1-2-3-1-1-3-0

[Block 2221]
མདོ་ལས།

[Block 2222]
བཤང་གཅིས་རབ་ཏུ་སྨེ་བར་བྱས། །ཞེས་པ་དག་ནི་རྫས་སུམ་ཅུ་རྩ་དྲུག་གིས༌[^1868]གླགས་པ་གཏི་མུག་གི་ཕུང་པོ་ཡིན་པ་སྟེ། སྐྱོ་བ་དང་སྤང་བར༌[^1869]བྱ་བ་ཡིན་གྱི་དགའ་བའི་གནས་མ་ཡིན་པར་བསྟན་པའོ། །

[Block 2223 [HEADING]]
###### **ཐེ་ཚོམ།** ^4-3-5-4-2-1-1-1-2-3-1-1-4-0

[Block 2224]
སྤྱང་ཀི་དང་ཁྱི་དང་ཝ་ནི་ཁམས་གསུམ་མམ་དུས་གསུམ་དུ་སྦྱར་རོ། །

[Block 2225 [HEADING]]
###### **ང་རྒྱལ།** ^4-3-5-4-2-1-1-1-2-3-1-1-5-0

[Block 2226]
མདོ་ལས།

[Block 2227]
མི་ཡི་རོ་ལ་རབ་ཏུ་ཟ། །ཞེས་པ་ནི་ང་རྒྱལ་བསྟན་ཏེ། ང་རྒྱལ་གྱིས༌[^1870]རྙེད་པ་ལ་འཐབ་ཅིང་རྩོད་ཅེས་པའི་དོན་ཏོ། །

[Block 2228 [HEADING]]
###### **ལྟ་བ་རྣམ་ལྔ།** ^4-3-5-4-2-1-1-1-2-3-1-2-0

[Block 2229]
མདོ་ལས།

[Block 2230 [HEADING]]
###### **ལོག་པར་ལྟ་བ།** ^4-3-5-4-2-1-1-1-2-3-1-2-1-0

[Block 2231 [VERSE]]
གནས་དང་གནས་ན་རྣམ་པར་འཆའ་ཞིང་ཟ། །
འཐབ་མོ་བྱེད་དེ་རབ་ཏུ་སྒྲ་ཡང་འབྱིན། །
རྣམ་པ་དེ་འདྲས་ཁྱིམ་དེ་ཤིན་ཏུ་འཇིགས། །

[Block 2232]
ཤིན་ཏུ་སེམས་གཏུམ་གནོད་སྦྱིན་དེ་ན་འཁོད། མི་ཡི་རོ་དག་ལ་ཡང་རྣམ་འདྲེན་ཞིང་། །ཞེས་པ་ནི་ཚིག་འདི་དག་གིས་ནམ་མཁའ་ལ་གནས་པའི་འདྲེ་གདོན༌[^1871]གྱི་དཔེ་ལྟ་བ་རྣམ་ལྔ་བསྟན་ཏེ། དེ་ལ་ཚིག་དང་པོ་གསུམ་གྱིས་ནི་ལོག་པར་ལྟ་བའི༌[^1872]དཔེ་བསྟན། དེའི་འོག་མ་ཚིག་ཕྱེད་ཀྱིས་ནི་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་ཀྱི་དཔེ་བསྟན། དེའི་འོག་མས་ནི་འཇིག་ཚོགས་ལ་ལྟ་བའི་དཔེ་བསྟན། དེའི་འོག་མས་ནི་ལྟ་བ་བསྙེམས་པའི་དཔེ་བསྟན། དེའི་འོག་མས༌[^1873]མཐར་ལྟ་བ་བསྟན་ཏོ། །

[Block 2233]
ཡང་ལྟ་བ་དེ་དག་ལ་དང་པོར་ལྟ་བ་སྤྱིའི་མཚན་ཉིད་བསྟན། དེའི་འོག་ཏུ་ལྟ་བ་སོ་སོའི་མཚན་ཉིད་དང་སྤྱོད་པ་བསྟན། གནོད་སྦྱིན་ལ་སོགས་པ་སེམས་གཏུམ་པོ་དེ་དག་ལོག་པར་ལྟ་བས་དགེ་བ་དེ་དག༌[^1874]ཐམས་ཅད་ཀྱི་རྩ་བ་མེད་པར་བྱེད་པ་ཉིད་གནོད་སྦྱིན་མིའི་རོ་ལ་འབྲང་བ་བཞིན་ནོ། །

[Block 2234]
མདོ་ལས།

[Block 2235]
སྦྲུལ་དང་རྐང་བརྒྱ་པ་དང་གཅན་གཟན༌[^1875]རྣམས། །ཞེས་པ་ནས། ཞིག་པའི་ཁྱིམ་དེར་ནི་ཡང་གནས་འཆའ་སྟེ། །ཞེས་པའི་བར་དུ་ནི་ལོག་པར་ལྟ་བས་ཉོན་མོངས་པ་ཐམས་ཅད་བསྐྱེད་པའི༌[^1876]ཕྱིར་དཔེར་སེམས་ཅན་གཏུམ་པོ་གདུག་པ་དེ་དག་གིས་བསྟན་ཏེ། སྐྱེ་ཞིང་འཕེལ་བའི་གནས་སུ་གྱུར་པ་ཕྲུ་གུ་གློག་པ་ཞེས་སྨོས་སོ། །

[Block 2236 [HEADING]]
###### **ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་བསྙེམས་པ།** ^4-3-5-4-2-1-1-1-2-3-1-2-2-0

[Block 2237]
མདོ་ལས།

[Block 2238]
ཇི་ཙམ་གནོད་སྦྱིན་དེ་དག་འགྲངས༌[^1877]གྱུར་པ། །ཞེས་པ་ནས། འཁང་དུ་བཅུག་པ་དེ༌[^1878]ལ་དགའ་བར་བྱེད། །ཞེས་པའི༌[^1879]བར་དུ་ནི་ལོག་པར་ལྟ་བ་ལ་སོགས་ཏེ་ལྟ་བ་རྣམ་ལྔས་རྒྱས་ཤིང་འཕེལ་བར་གྱུར་པ་ཉིད་འགྲངས༌[^1880]པར་གྱུར་པ་སྟེ། སྒོ་གསུམ་ནས་སྤྱོད་པ་རྣམ་པ༌[^1881]གཞན་གྱིས་འཇིགས་སུ་རུང་བའི་ཕྱིར༌[^1882]དང་། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་བསྙེམས་པ་དང་། བརྟུལ་ཞུགས་བསྙེམས་པས༌[^1883]སེམས་ཅན་གཙེས་པའི་འཁང་པས་བདག་དགའ་བར་བྱེད་པ་བཞིན་དུ་ཚུལ་ཁྲིམས་དང་། བརྟུལ་ཞུགས་བསྙེམས་པས་མཐོ་རིས་བགྲོད་པའང་དེ་དང་འདྲའོ། །

[Block 2239]
མཐོ་གང་ཚད་དང་དེ་བཞིན་ཁྲུ་གང་ཚད། །ཞེས་པ༌[^1884]ནི་ཚུལ་ཁྲིམས་བསྙེམས་པ་དང་། བརྟུལ་ཞུགས་བསྙེམས་པ་གཙོ་ཡིན་པར་འཛིན་པས་འཇིག་རྟེན་ལས་འདས་པའི་དོན་ཚོལ་བ་ཉིད་དོ། །

[Block 2240]
མདོ་ལས།

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
--- END BLOCKS ---
