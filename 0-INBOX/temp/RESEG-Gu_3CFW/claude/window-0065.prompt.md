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
ཕལ་ཆེ་བ་ལ་རབ་ཏུ་གྲགས་པ་ལ་བརྟེན་པའོ། །

[Block 2277]
དབྱུང་བར་བྱ་བ་ལ་ཡང་དེའི་རྗེས་སུ་འབྲངས་ནས་ཆོ་གའི་སྐྱོན་ཤེས་པར་བྱའོ། །

[Block 2278]
འགལ་བའི་ཟླ་ནི་བྱིན་གྱིས་བརླབས༌[^2059]པའམ། དབྱུང་བར་བྱ་བ་དག་གཞན་དུ་གནས་པས་མི་རིགས་སོ། །

[Block 2279]
དེ་ལྟ་བས་ན་གང་གི་མདུན་དུ་བྱིན་གྱིས་བརླབ་པའམ་དབྱུང་བར་བྱ་བ་དེ་ལ་ཡང་སྤྱོད་ལམ་དེ་ཁོ་ན་དང་འདྲའོ། །

[Block 2280]
འགྲེངས་ཏེ༌[^2060]འདུག་པ༌[^2061]རྣམས་ཀྱིས་དུས་སུའོ། །

[Block 2281]
ལྷུང་བཟེད་དང་ཆོས་གོས་བྱིན་གྱིས་བརླབ་པའི༌[^2062]ཕྱིར་རིགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2282]
མ་དད་པ་ཉིད་ཀྱིས་དེ་ཡིད༌[^2063]ལ་ཆགས་པར་འགྱུར་རོ། །

[Block 2283]
དེ་ལྟ་བས་ན་དེ་ལ་བརྟེན་ནས་གནས་པ་ལས་བསྙེན་པར་རྫོགས་པ་ནི་མཁན་པོས་བྱས་སོ། །

[Block 2284]
དེ་བས་ན་ལྟུང་བ་དང་བཅས་པར་རིག་པར་བྱའོ། །

[Block 2285]
འདིར་རྫས་ཀྱི་སྒྲས་ནི་གསོ་སྦྱོང་གི་ཉི་མ་དང་། དགག་དབྱེ་དང་ལྟུང་བ་བྱིན་གྱིས་བརླབ་པ་དང་། ཕྱིར་བཅོས་པའི་དོན་དུ་འགྲེངས་ཏེ༌[^2064]འདུད་པ་དང༌[^2065]བཅས་པ་ཉིད་ཀྱིས་སོ། །

[Block 2286]
གསོ་སྦྱོང་དང་དགག་དབྱེ་དག་བྱིན་གྱིས་བརླབ་པའི་ཕྱིར་ཙོག་པུར་འདུག་སྟེ་བྱ་བར་གསུངས་པས་དེ་གཉིས་ཀ༌[^2066]ཡང་འདུག་སྟེ་བྱའོ། །

[Block 2287]
དེས་ན་གཅིག་དང་བཅས་པ་ལ་ནི་དེ་ལ་ངེས་པ་དང་ལྡན་པའི་ཆོ་གས་ཤེས་པར་བྱའོ། །

[Block 2288]
གཅིག་པུར་ལྟུང་བ་བྱིན་གྱིས་བརླབ་པ་ནི་ལས་བྱེད་པ་པོས་ད་ལྟར༌[^2067]བྱ་བ་ཉིད་ལ་མི་འཐད་པས་འདིར་སྤྱོད་ལམ་རྣམ་པར་མ་འཁྲུགས་པས་ཇི་ལྟར་གནས་པས་དགེ་འདུན་ལས་ཕྱི་རོལ་དུ་དགག་དབྱེ་བྱིན་གྱིས་བརླབ་པ་ཉིད་ཀྱང་འདུག་སྟེ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 2289]
ཆོས་གོས་དབྱུང་བ་དང་བྱིན་གྱིས་བརླབ་པ་དག་ལ་ཡང་འདུག་པ་གཅིག་པུས་བྱ་བ་རིག་པར་འགྱུར་བ་མཐོང་བ་ཡིན་ནོ། །

[Block 2290]
གསོ་སྦྱོང་གི་ལས་ལ་ཡང་དེ་ལྟ་བུའི་ངོ་བོའི་རྐྱེན་རྣམས་ལ་འགྲོ་བ་རྣམས་ཀྱིས་བྱེད་པར་གསུངས་པ་དེ་བས་ན། དེ་ལྟ་བུའི་ངོ་བོའི་རྐྱེན་རྣམས་ལ་གསོ་སྦྱོང་བྱིན་གྱིས་བརླབ་པ་ལ་སོགས་པ་ཐམས་ཅད་དུ་འགལ་ཟླ་དང་འགྲོ་བ་མ་ཡིན་པ་ལ་ཡང་བྱེད་པ་ཉིད་རིག་པར་བྱའོ། །

[Block 2291]
གསོ་སྦྱོང་ལ་ནི་གཅིག་པུ་བྱིན་གྱིས་བརླབ་པ་འགྲོ་བ་ཉིད་ལ་དེར་སྨོས་པ་ཉིད་དོ། །

[Block 2292]
ཁ་ཅིག་ནི་དེའི་ངོ་བོའི་རྐྱེན་རྣམས་སུ་འགྱུར་ཏེ། གང་དུ་མི་འདུག་པ་རྣམས་ཀྱིས་གནས་པར་རིགས་པ་ཡིན་ཏེ་འདུག་པ་རྣམས་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 2293]
འདུག༌[^2068]པའམ་མི་གནས་པ་རྣམས་ཀྱིས་དེར་ཡང་ནུས་པ༌[^2069]དེ་ལྟ་བུར་གྱུར་པ་ཉིད་ལ་བྱ་བ་བྱེད་པ་འགྲོ་བ་བཞིན་དུ་དོར་བར༌[^2070]མི་རིགས་པ་དེ་བས་ན། དེ་ལྟ་བུའི་ངོ་བོའི་རྐྱེན་རྣམས་ལ་གང་ལ་འགྲོ་བ་ཉིད་ལ་བྱ་བ་ཉིད་འདུག་པ་ལ་ཡང་དེའི་རྫས་བྱིན་གྱིས་བརླབ་པ་དང་། བཏང་བ་དག་ནི་འདུག་པ་ལ་ཡང་རིག་པར་བྱའོ། །

[Block 2294]
རྣམ་པར་བརྟག་པ་ནི་དེ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གོས་རྣམ་པར་བརྟག་པ་ནི་བྱིན་གྱིས་བརླབ་པ་ཉིད་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2295]
དེས་ན༌[^2071]རྣམ་པར་བརྟག་པ་དེ་ལ་ཡང་ཆོ་ག་བཞིན་དུ་ཤེས་པར་བྱའི་མ་བྱས་པ་ཉིད་ནི་ཤེས་པར་མི་བྱའོ། །

[Block 2296]
འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས།

[Block 2297]
འདི་ལྟར་རྣམ་པར་བརྟག་པར་བྱ་སྟེ། དགེ་སློང་གི་མདུན་དུ་འགྲེངས་ཏེ།[^2072] བཙུན་པ་དགོངས་སུ་གསོལ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 2298]
དེ་ལ་བཟུང་སྟེ་ཞེས་བྱ་བ་ནི་ལག་པས་རྫས་དེ་བཟུང༌[^2073]སྟེ་བྱིན་གྱིས་རློབ་པར་བྱེད་པ་གཉིས་ཀས་དེ་ལྟར་བྱའོ། །

[Block 2299]
འདི་ནི་གོས་ཀྱི་དོན༌[^2074]ལྷུང་བཟེད་དང་སྨན་བྱིན་གྱིས་བརླབ་པའི་ཕྱིར། ལྷུང་བཟེད་དང་སྨན༌[^2075]ལག་པ་གཡོན་པར་གཞག་པ་སྟེ། ལག་པ་གཡས་པས་བཀབ་ནས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱིན་གྱིས་རློབ་དུ་འཇུག་པ་དང་བྱིན་གྱིས་རློབ་པ་གཉིས༌[^2076]ཀར་སྨན་དང་། ལྷུང་བཟེད་བྱིན་གྱིས་བརླབ་པ་ལ་གྲགས་པའོ། །

[Block 2300]
བྱིན་གྱིས་རློབ་པར་བྱེད་པ་བཞིན་དུ་དེའི་ཕྱི་རོལ་དུ་ལག་པ་དག་གིས་སོ། །

[Block 2301]
དེ་ཉིད་ལ་གང་གིས་བྱིན་གྱིས་རློབ་པའི་བདག་ཉིད་ཅན་མངོན་པར་བརྟེན་པ་བྱིན་གྱིས་རློབ་པར་བྱེད་པ་དེས་ལུས་ཀྱིས་མངོན་པར་བརྟེན་པ་རིགས་པ༌[^2077]ནི་འདིར་ཡན་ལག་ཉིད་དོ། །

[Block 2302]
[^2078]ཅིག་ཤོས་ཀྱིས་གང་ཞིག༌[^2079]གི་མི་རིགས་པ་དེ་འདིར་ཡན་ལག་ཉིད་ལ་ཞེས་བྱ་བ་སྣོད་དུ་མི་རུང་བ་ཉིད་ཀྱི་ཕྱིར་དང་དགོས་པ་གནང་དུ་མི་རུང་བ་ཉིད་ཀྱི་ཕྱིར་དེ་ལ་མ་བརྟེན་པའོ། །

[Block 2303]
དབྱུང་བར་བྱ་བ་ལ་ཡང་རྫས་ཀྱི་ཆོ་ག༌[^2080]འདིའི་རྗེས་སུ་འབྲང་བར༌[^2081]ཤེས་པར་བྱའོ། །

[Block 2304]
ལྷུང་བཟེད་ཀྱི་དབྱུང་བ་ནི་ལག་པས་སྟེང་ནས་གཡོགས་པ་བཏང་སྟེ། ལག་པ་ཡ་རེས་ཁ་ནས་བཟུང་སྟེ་བྱ་བ་ནི་རིགས་པ་ཡིན་ནོ། །

[Block 2305]
གཟུང་བར༌[^2082]བྱ་བ་མ་ཡིན་པ་ཉིད་ལ་ནི་མདུན་དུ་བཞག་སྟེའོ་ཞེས་བྱ་བ་ནི་གཟུང་བར༌[^2083]བྱ་བའི་རྫས་ཉིད་མ་ཡིན་པ་ནི་འདི་ལྟ་སྟེ། གསེར་དངུལ་ལ་སོགས་པའི་སྒྲམ་བུ་མདུན་དུ་བཞག་སྟེ་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 2306]
ལས་ནི་འདུག་པ་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་གསོལ་བ་ལ་སོགས་པའི་ལས་ཐམས་ཅད་འདུག་པ་ཉིད་ཀྱིས་བྱའི༌[^2084]སྤྱོད་ལམ་གཞན་གྱིས༌[^2085]ནི་མི་བྱའོ། །

[Block 2307]
དགག་དབྱེ་བྱེད་པ་པོ་ལ་མངོན་སུམ་དུ་ཆོ་ག་བརྗོད་པ་ཡིན་ནོ། །

[Block 2308]
བརྗོད་པ་པོ་ལ་ཡང༌[^2086]དགག་དབྱེ་བྱེད་པ་ལ་སྔར༌[^2087]གསུངས་པ་ཉིད་ཀྱི་ཆོ་ག་རིག་ས༌[^2088]པར་བྱའོ། །

[Block 2309]
ལྷག་མའི་དོན་དུ་མདོ་འདི་ཤེས་པར་བྱའོ། །

[Block 2310]
གསོལ་བ་དང་ལས་བརྗོད་པའི་བསྟན་པ་རྣམས་ནི་མི་བྱེད་པའི༌[^2089]ཁ་སྐོང་བར་བྱེད་པ་རྣམས་ཀྱི༌[^2090]དགག་དབྱེ་ཕྱེ་བ་ལས་ཁ་སྐོང་དུ༌[^2091]བྱེད་པ་གཞན༌[^2092]རྣམས་ཞེས་བྱ༌[^2093]བའོ། །

[Block 2311]
དགེ་འདུན་ནམ་གཅིག་ཁོ་ན་ལ་མ་བརྟེན་པ་ནི་གང་ཟག་དགེ་སློང་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ་གང་དུ་འདིར་དགེ་འདུན་ནམ་གང་ཟག་གསོལ་བར་བྱ་བ་ལ་མི་བརྟེན་པར༌[^2094]ནི་འདི་ལྟ་སྟེ། གནས་ལ་སོགས་པའི༌[^2095]མིང་བརྗོད་པ༌[^2096]སྟེ། གྲོང་དུ་ཞུགས་པའི་དོན་དུའོ། །

[Block 2312]
ལྟ་བ་དག་དང་། དེ་ལས་གཞན་དུ་གཅིག་པུ་བྱ་བ་ཉིད་ལ་འདི་ལྟ་སྟེ། རྫས་བྱིན་གྱིས་བརླབ་པ་དང་། ཉིན་ཞག་བྱིན་གྱིས་བརླབ་པ་ལ་གང་ཟག་གི་དེར་གསོལ་བར་བྱ་བ་ཉིད་ཤེས་པར་བྱའོ། །

[Block 2313]
དགེ་སློང་གཞན་ལ་བརྗོད་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་ལ་སོགས་པ༌[^2097]ཉིད་ཡིན་གྱི་གཞན་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2314]
ཆོས་གོས་དབྱུང་བ་དང་བྱིན་གྱིས་བརླབ་པ་ནི་ཉེ་བར་མི་གནས་ན་ཡིད་ཀྱིས་རྣམ་པར་བརྟགས་པས་འཆགས་སོ་ཞེས་བྱ་བ་ལ་ཉེ་བར་མི་གནས་ན་ཞེས་བྱ་བ་ནི་དབང་དུ་བྱ་བ་ཉིད་ཀྱི་ཕྱིར་དགེ་སློང་ལའོ། །

[Block 2315]
འདིར་ཆོས་གོས་ཉེ་བར་མི་གནས་ན་རྣམ་པར་བརྟག་པ་དང་བྱིན་གྱིས་བརླབ་པ་དག་བྱའོ། །
--- END BLOCKS ---
