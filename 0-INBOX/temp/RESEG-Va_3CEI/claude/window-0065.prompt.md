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

[Block 2281]
མདོ་ལས།

[Block 2282]
སྲིན་བུ་རྐང་བརྒྱ་པ་དག་འབྲོས་གྱུར་པ། ཞེས་པ་ནས། བཀྲེས་པ་དང་ནི་བསྲེགས་པས་ཤིན་ཏུ་གདུངས། །ཞེས་པའི་བར་དུ་ནི་འདིས་ཀྱང་གཟུགས་མེད་པའི་ཁམས་ཀྱི་ཉོན་མོངས་པ་བསྟན་པ་སྟེ། གཟུགས་མེད་པའི་ཁམས་འོག་མ་གསུམ་གྱི་འགོག་པའི་བསམ་གཏན་གྱི་མེས༌[^1921]ཁམས་གོང་མར་རྒྱུ་ཞེས་པའི་དོན་ཏོ། །

[Block 2283]
གྲུལ་བུམ་ཞེས་པ་ནི་མུ་སྟེགས་ཅན་གྱི་ལྟ་བ་མང་པོ་དམ་དུ་བཟུང་བས་བླ་མ་བླ་མའི་ས་ཚོལ་བར་སེམས་པ་སྟེ། ལྟ་བ་ངན་པའི་ཟན་ཟོས་པས་ཉོན་མོངས་པ་ཕྱིར་ཞིང་འཕེལ་ཞེས་པའི་དོན་ཏོ། །

[Block 2284]
མེ་ལྕེ་སྟོང་སྙེད་རབ་ཏུ་འབར། །ཞེས་པ་ནི་སྲིད་པའི་རྩེ་མོ་ལ་གནས་པའི་མུ་སྟེགས་ཅན་ཡང་དག་པའི་བསྟན་པའི༌[^1922]ཟས་དང་སྐོམ་གྱིས་གདུངས་པས་ཉོན་མོངས་པའི་མེས་ཚིག་ཅེས་པའི་དོན་ཏོ། །

[Block 2285 [HEADING]]
###### **ཐབས་རྣམ་པ་སྣ་ཚོགས་བཤམས་པའི་དཔེ།** ^4-3-5-4-2-1-1-1-3-0

[Block 2286]
མདོ་ལས།

[Block 2287]
ཁྱིམ་འདིའི་བདག་པོ་མི་དེ་ནི། །སྒོ་ནས༌[^1923]འདུག་ཅིང་ཤིན་ཏུ་རྣམ་པར་ལྟ། །ཞེས་པ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་རྩ་བ་བཅུ་བཞིས་དྲང་བའི་དོན་བསྟན་པའི་དཔེ་དང་། སྡུག་བསྔལ་བ་རྣམས་ལ་སྙིང་རྗེ་སྐྱེ་བའི་དཔེ་དང་། ངོ་མཚར་བསྟན་པའི་དཔེ་དང་། སྡུག་བསྔལ་གྱི་ས་ནས་གདོན་པའི་དཔེ་དང་། ཐེག་པ༌[^1924]གསུམ་བཤད་པའི་དཔེ་ལ། འདི་ནི་སྡུག་བསྔལ་བ་རྣམས་ལ་སྙིང་རྗེ་སྐྱེ་བའི་དཔེ་སྟེ། སྡུག་བསྔལ་བ་བསྟན་པ་ཚིག་གཉིས་ལ་ཡང་ཚིག་གོང་མས་ནི་སངས་རྒྱས་འཇིག་རྟེན་དུ་འབྱུང་བ་བསྟན་པའི་དཔེ། དེའི་འོག་མ་ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་སེམས་ཅན་སྡུག་བསྔལ་བ་རྣམས་ལ་སྙིང་རྗེ་བར་བྱ་བའི་དོན་བསྟན་པའོ། །

[Block 2288]
སྒོ་ན་འདུག་ཅེས་པ་ནི། སྡོད་པ་དང་འདུག་ཅེས་པའི་དོན་ཏེ། ཁང་པ་དེའི་ནང་ན་གནས་པའི་བུ་རྣམས་གདོན་པའི་སེམས་ཀྱིས་འདུག་པ་དང་། སྐྱབས་བྱ་བའི་སེམས་ཀྱིས་སྡོད་པ་དང་། [^1925]དབང་པོ་སྨིན་མ་ཐག་ཏུ་ཕན་གདགས་པར་སེམས་པས༌[^1926]སྡོད་པ་དང་། ཉོན་མོངས་པའི་གནས་ནས་བསླངས་ཏེ། གྲུབ་པའི་གནས་བདེ་བ་ལ་དགོད་པར་སེམས་པའོ། །

[Block 2289]
མདོ་ལས།

[Block 2290]
དེས་ཐོས་དེ་ན་དེ་ཡིས་བདག་གི༌[^1927]བུ། །ཞེས་པ་ནས། དེ་ལྟར་བ་བདག༌[^1928]ནི་མི་ཤེས་ཕྱིར། །ཞེས་པའི་བར་དུ་དཔེ་འདིས་ནི་སེམས་ཅན་ཉོན་མོངས་པའི་ས་ན་སྡུག་བསྔལ་བ་བསྟན་པ་སྟེ། ཞིབ་ཏུ༌[^1929]ཚིག་ལྷུག་པའི་ནང་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 2291]
ཐོས་པ་ཞེས་པའི༌[^1930]དུས་གསུམ་གྱི་དེ་བཞིན་གཤེགས་པས་སེམས་ཅན་སྡུག་བསྔལ་གྱི་ས་ན་གནས་པར་བཤད་པ་ཐོས་པ་དང་། བདག་ཉིད་ཀྱིས་སེམས་ཅན་སྡུག་བསྔལ་བར་མཐོང་བའོ། །

[Block 2292]
ཐོག་མ་མེད་པའི་དུས་ནས་འཛེམ་པ་དང་། ཁྲེལ་བ་མེད་པས་ཉོན་མོངས་པ་སྣ་ཚོགས་ལ་བག་མེད་པར་སྤྱོད་པ་དེ་ཉིད་བྱིས་པ་མི་ཤེས་པའོ། །

[Block 2293]
མདོ་ལས།

[Block 2294]
དེས་ཐོས་དེ་ནས་མྱུར་དུ་དེར་སོང་སྟེ། །ཞེས་པ་ནས། སྡུག་བསྔལ་ཆེན་པོ་དག་ནི་གཅིག་ཕྱིར་གཅིག །ཞེས་པའི་བར་དུ་ནི་སྙིང་རྗེ་སྐྱེ་བར་བསྟན་པ་སྟེ། སེམས་ཅན་འཁོར་བ་ན་གནས་པ་ནི་མེའི་ཁང་པར་ཞུགས་པ་བཞིན་ཏེ།

[Block 2295 [VERSE]]
མྱུར་དུ་མི་ཐར་ཅེས་པའི་དོན་ཏོ། །
དེ་ལ་ཁྱིམ་གྱི་ཉེས་པ་དེས་བརྗོད་འདི། །
སྡུག་བསྔལ་འདི་དག་མི་བཟད་རིགས་ཀྱི་བུ། །

[Block 2296]
ཞེས་པ་ནི་སྡུག་བསྔལ་འཇིགས་པ་ཆེན་པོ་དང་ལྡན་པར་བསྟན་པ་སྟེ། ཐེག་པ་ཆེན་པོས་བསྐྱེད་ཅིང༌[^1931]གདོན་ཞེས་པའི་དོན་ཏོ། །

[Block 2297]
གཅིག་ཕྱིར་གཅིག་ཅེས་པ་ནི་ཐོག་མ་མེད་པའི་དུས་ནས་གཅིག་གིས་གཅིག་སྡུད་ཅིང་ཉོན་མོངས་པའི༌[^1932]གནས་ན་སྐྱེ་བ་དང་རྒ་བ་དང་ན་བ་དང་ཤི་བ་རྒྱུན་མི་འཆད་ཅེས་པའི་དོན་ཏོ། །

[Block 2298]
མི་བཟད་ཅེས་པ་ནི་མུ་སྟེགས་ཅན་གྱི་ཁྱིམ་ནས་བྱུང་བ་དང་ཁྱིམ་ན་གནས་པ་གཞན་སླུ་བར༌[^1933]བྱེད་པ་མི་བཟད་ཅེས་པའི་དོན་ཏོ།[^1934]

[Block 2299]
།མདོ་ལས།

[Block 2300]
སྦྲུལ་དང་གནོད་སྦྱིན་གཏུམ་སེམས་དང་། །ཞེས་པ་ནས། མེ་མེད་ཟིན་ཀྱང་རབ་ཏུ་འཇིགས། །ཞེས་པའི་བར་དུ་ནི། སྦྲུལ་ནི་ཞེ་སྡང་ངོ་། །གནོད་སྦྱིན་ནི་ལས་ངན་པར་སྤྱོད་པའོ། །

[Block 2301]
གྲུལ་བུམ་ནི་ཚུལ་ཁྲིམས་ངན་པ་ལ་གནས་པའོ། །

[Block 2302]
ཝ་ནི་ཐེ་ཚོམ་དང་སྦྱར་རོ། །

[Block 2303]
ཁྱི་ནི་ང་རྒྱལ་དང་སྦྱར་རོ། །

[Block 2304]
བྱ་རྒོད་ནི་འདོད་ཅིང་བརྐམ་པ་དང་སྦྱར་རོ། །

[Block 2305]
དེ་ལྟ་བུའི་ཉོན་མོངས་པ་སྣ་ཚོགས་ཀྱིས་གཟིར་ཞེས་པའི་དོན་ཏོ། །

[Block 2306]
མདོ་ལས། །

[Block 2307]
དེ་འདྲའི༌[^1935]སྡུག་བསྔལ་འབའ་ཞིག་སྟེ། །ཞེས་པ་ནས། དེ༌[^1936]ཚེ་དེ་ཡི་ཐབས་བསམས་པ། །ཞེས་པའི་བར་དུ་ནི་ཐུགས་རྗེས་ཕན་འདོགས་པ་ཉིད་དང་སྦྱར་རོ། །

[Block 2308]
མདོ་ལས།

[Block 2309]
བྱིས་པ་དེ་དག་རྩེ་ལ་ཆགས། །ཞེས་པ་ནས། དགའ་བར་ལྷན་ཅིག་ཕྱིར་འཐོན། ཞེས་པའི་བར་དུ་ནི། འདི་མན་ཆད་ཐེག་པ་རྣམ་གསུམ་དང་སྦྱར་ཏེ། རི་དགས་དང་ར་དང་གླང་གི་བཞོན་པས༌[^1937]ཐེག་པ་རྣམ་པ༌[^1938]གསུམ་དང་སྦྱར་ཏེ་བསྟན་པའོ། །

[Block 2310]
དེ་ལ་ཡང་དང་པོར་བཞོན་པ་བྱིན་པར་ཁས་བླང་བ༌[^1939]དང་། བཞོན་པ་ཁྱིམ་གྱི་ཕྱི་རོལ་ན་ཡོད་པར་བསྟན་པ་དང་། བཞོན་པ་ཉིད་ཅི་དང་ཅི་འདྲ་བར༌[^1940]བསྟན་པའོ། །

[Block 2311]
བཞོན་པ་ང་ལ་ཡོད་ཅེས་པ་ནི་བཞོན་པ་སྦྱིན་པར་ཁས་བླངས་པའོ། །

[Block 2312]
རི་དགས་དང་ར་དང་གླང་ཞེས་པ་ནི་ཕྱི་རོལ་ན་ཡོད་པ་དང་དངོས་བསྟན་པའོ། །

[Block 2313]
འབྲས་བུ་ནི་རྒྱུའི་སྒོ་ནས་བྱུང་། གཞུང་ཉིད་ནི་བསྟན་པ་ལས་ཕྱི་རོལ་བས་ཕྱི་རོལ་ན་ཡོད་ཅེས་སྨྲས་སོ། །

[Block 2314]
བླ་ན་མེད་པའི་གནས༌[^1941]ཁམས་གསུམ་ལས་འདས་པའི་ཕྱིར་ཕྱི་རོལ་ན་ཡོད་ཅེས༌[^1942]བསྟན་ཏོ། །

[Block 2315]
ཁྱེད་ཅག་གི་ཕྱིར་ངས་བྱས་ཞེས་པ་ནི་བཞོན་པའི་དགོས་པ་བསྟན་ཏེ། མྱ་ངན་ལས་འདས་པའི་གནས་དམ་པ་ནི་འདུས་མ་བྱས་པ་ཡིན་མོད་ཀྱི་ཐེག་པ་ཉིད་འདུས་བྱས་ཡིན་པའི་ཕྱིར་བྱས་ཞེས་སྨྲས་སོ། །
--- END BLOCKS ---
