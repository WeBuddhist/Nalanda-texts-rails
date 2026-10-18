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
[Block 2346]
གསུམ་རིག་པ་ནི་སྔོན་གྱི་གནས་དྲན་པ་དང་། ལྷའི་སྤྱན་དང་། ཟག་པ་ཟད་པར་མཁྱེན་པའོ། །

[Block 2347]
མདོ་ལས།

[Block 2348]
མཁས་པ་རྣམས་ལ་དཔེ་མཆོག་འདི།[^1961] །ཞེས་པ་ནས། མི་མཆོག་ཐབས་མཁས༌[^1962]མ་གཏོགས་སོ། །ཞེས་པའི་བར་དུ་ནི། ཐེག་པ་མཆོག་ཡིན་པར་བསྟོད་ཅིང་བསྔགས་པ་སྟེ། ཐེག་པ་དེ་ཡང་ཚིགས་བཅད་དང་པོ་གཅིག་གིས་ནི་ཐེག་པ་དེ་ཡོན་ཏན་བཞི་དང་ལྡན་པར་བསྟན། དེའི་འོག་མ་གཅིག་གིས་ནི་འཕགས་པ་རྣམས་ཀྱི༌[^1963]བསྔགས་པ་བསྟན། དེའི་འོག་མ་གཅིག་གིས་ནི་ལོངས་སྤྱོད་དམ་པ་དང་ལྡན་པ་བསྟན། དེའི་འོག་མ་གཉིས་ཀྱིས་ནི་དགའ་བའི་མཆོག་ཡིན་པར་བསྟན་ཏོ། །

[Block 2349]
དེ་ལ་ཡོན་ཏན་བཞི་ནི་དམ་པ་ཁྱད་པར་ཅན་སྒྲིབ་པ་མེད་པས་རྣམ་པར་དག་པ་དང་། མཆོག་དམ་པ་ཡིན་པ་དང་།

[Block 2350 [VERSE]]
བླ་ན་མེད་པ་དང་ཟླ༌[^1964]མེད་པའོ། །
ཡངས་པའི་དངོས་པོ་ཕྱག་གི་གནས། །

[Block 2351]
ཞེས་པ་ནི་འཕགས་ལ༌[^1965]རྣམས་ཀྱི༌[^1966]བསྔགས་པའོ། །

[Block 2352]
འཕགས་པ་རྣམས་དེ་ལྟར་ན་མ་རབས་རྣམས་ལ་ཅི་སྨོས་ཞེས་སྦྱར་རོ། །

[Block 2353]
བསམ་གཏན་དང་སྟོབས་དང་ཏིང་ངེ་འཛིན་ཞེས་པ་ནི་ལོངས་སྤྱོད་ཀྱི་གནས་དམ་པ་ཡིན་པར་བསྟན་པའོ། །

[Block 2354]
ནུབ་དང་ཉིན་པར་ལོ་དང་བསྐལ་པ་འདའ་བར་བྱེད། །ཞེས་པ༌[^1967]ནི། ཐེག་པ་གཅིག་པོ་འདི་ལ་གནས་པ་ནི་གནས་པའི༌[^1968]དམ་པ་ཡིན་པར་བསྟན་ཏེ། བླ་ན་མེད་པའི་བྱང་ཆུབ་ཀྱི་སྙིང་པོ་ལ་རེག༌[^1969]པར་འགྱུར་ཞེས་པའི་དོན་ཏོ། །

[Block 2355]
དེ་ཡན་ཆད་བསྟན་པ་དང་། གཞུང་དང་སྤྱོད་པ་དང་། འབྲས་བུ་ཐམས་ཅད་ཐེག་པ་ཆེན་པོ་དང་ལྡན་པར་བསྟན་ཏོ། །

[Block 2356]
མི་མཆོག་ཐབས་མཁས་མ་གཏོགས་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ཐབས་མཁས་པ་དང་ལྡན་པས་སེམས་ཅན་རྣམས་རིམ་གྱིས༌[^1970]ཐེག་པ་གཅིག་པོ་ལ་དྲང་ཞིང་གཟུད༌[^1971]པའི་ཕྱིར་ཕྱོགས་བཅུ་གང་དུ་ཡང་ཐབས་ཀྱིས་རོལ་པ་མ་གཏོགས་པར་ཐེག་པ་གཉིས་དང་གསུམ་དུ་མ་བཤད་དོ། །

[Block 2357 [HEADING]]
###### **དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ལ་དད་པ་བསྐྱེད་ཅིང་གཟུད་པ།** ^4-3-5-4-2-2-0

[Block 2358]
མདོ་ལས།

[Block 2359 [HEADING]]
###### **དྲང་བ་དང་ངེས་པའི་དོན་ལ་འཇུག་པ།** ^4-3-5-4-2-2-1-0

[Block 2360]
ཁྱོད་ཀྱི་ཕ་ང་ཡི་བུ་ཁྱོད། །ཞེས་པ༌[^1972]ནས། བྱང་ཆུབ་སེམས་དཔའ་གང་མང་འདུལ། །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་མོས་བསྐྱེད༌[^1973]ཅིག་པར་བསྟན་པ་སྟེ། སྔར་ཚིགས་བཅད་བཅུ་བཞིས༌[^1974]དྲང་བ་དང་ངེས་པའི་དོན་ལ་འཇུག་པར་བསྟན། དེའི་འོག་མ༌[^1975]ཚིགས་བཅད་དྲུག་ཅུ་རྩ་དྲུག་གིས་ནི་བསླབ་པར་བྱ་བའི་གནས་བསྟན་ཏོ། །

[Block 2361]
དང་པོ་ལ་ཕ་བུ་ལ༌[^1976]བྱམས་པའི་དཔེས་སྡུག་བསྔལ་ལས་འདོན་པ་བཞིན་ངེས་པ་དང་དྲང་བའི་དོན་དངོས་སུ་སྟོན་པའོ། །

[Block 2362]
འདི་ལྟར་མྱ་ངན་ལས༌[^1977]འདས་པ་ངས་བསྟན་ཀྱང་ཞེས་པ་ནི། བཅོམ་ལྡན་འདས་ཀྱིས་ཡང་དག་པའི་དོན་སྔར་དྲང་བའི་ཚུལ་གྱིས་བསྟན་དུ་ཟིན་གྱིས་དེ་མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་མ་ཡིན་པས། ང་མྱ་ངན་ལས་འདས་པ་ཉིད་བསྟན་པའི་ཕྱིར་ངེས་པའི་དོན་བསྟན་ཏོ།[^1978] །ཀུན་ཉོན་ང་ཡི་སངས་རྒྱས་ཚུལ། །ཞེས་པའོ། །

[Block 2363]
ཚུལ་ནི་ཆོས་ཀྱི་སྐུ་ཉིད་དོ། །

[Block 2364]
སྒྲིབ་པ་རྣམ་གཉིས་དང་བྲལ་བའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་ཆེན་པོའི༌[^1979]མདོ་ལས།

[Block 2365]
བྱང་ཆུབ་སེམས་དཔའ་གང་མང་འདུལ། །ཞེས་པ་ནས། ལམ་རྣམས་བསྒོམས་ནས་ཐར་བར་འགྱུར། །ཞེས་པའི་བར་དུ་ནི་དེ་ལྟར་དྲང་བ་དང་། ངེས་པའི་དོན་བསྟན་པ་ཡང་བདེན་པ་བཞི་དང་སྦྱར་ཏེ་བསྟན་པའི་ཕྱིར་ཚིགས་སུ་བཅད་པ་འདི་དག་གསུངས་སོ། །

[Block 2366]
དང་པོའི༌[^1980]ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་སྡུག་བསྔལ་གྱི་བདེན་པ་བསྟན། དེའི་འོག་མ་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་ཀུན་འབྱུང་གི་བདེན་པ་བསྟན། ཡང་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་འགོག་པའི་བདེན་པ་བསྟན། དེའི་འོག་མ་གཅིག་གིས་ནི་ལམ་གྱི་བདེན་པ་བསྟན་ཏེ། འདོད་ངན་དེ་ལ་ཆགས་པར༌[^1981]གྱུར་པ་ནི་ཕྱི་ནང་གི་ཡུལ་ལ་དགའ་བར་བྱ་བ་དེ་ཐམས་ཅད་སྡུག་བསྔལ་ཉིད་ཡིན་པར་བསྟན་པས་འཇིག་རྟེན་གྱི་བདེན་པ་མ་སྤངས་པར་ཡང་དག་པའི་བདེན་པ་ཉིད་ལ་གཟུད་པའོ། །

[Block 2367]
གང་རྣམས་མི་ཤེས་སྡུག་བསྔལ་གྱི། །ཞེས་པ་ལ་སོགས་པ་ནི་ཀུན་འབྱུང་གི་བདེན་པ་བསྟན་ཏེ། སྡུག་བསྔལ་གྱི་རྒྱུ་ཀུན་འབྱུང་ལས་འབྱུང་ཞེས་པའི་དོན་ཏོ། །

[Block 2368]
སྡུག་བསྔལ་འབྱུང་བ་སྲེད་འདུས་པ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་འགོག་པའི་བདེན་པ་བསྟན༌[^1982]ཏེ། སྡུག་བསྔལ༌[^1983]སྐྱེ་བར་བྱེད་པའི་རྩ་བ་སྲེད་པ་ཡིན་ན། སྲེད་པ་དེ་ཡང་འགོག་པས་བཙལ༌[^1984]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2369]
གང་གིས༌[^1985]ཐར་ཞེས་པ་ལ་སོགས་པ་ནི་ལམ་གྱི་བདེན་པ་བསྟན་ཏེ། ལམ་བསྒོམས་པས་འགོག་པ་འགྲུབ་ཅེས་པའི་དོན་ཏོ། །

[Block 2370]
མདོ་ལས།

[Block 2371]
ཅི་ཐར་ཞེ་ན་ཤཱ་རིའི་བུ། །ཞེས་པ་ནས། འཇིག་རྟེན་འདིར་སྐྱེ་བདེ་བྱའི་ཕྱིར། །ཞེས་པ་ནི་དྲང་བ་དང་ངེས་པའི་དོན་གྱི༌[^1986]བདེན་པ་བཞི་བསྟན་པ་ཡང་འདི་མན་ཆད་ཚིག་བཞིས་ནི་དྲིས། ཚིག་བཞིས༌[^1987]ནི་ལན་བཏབ་པ་སྟེ། བདེན་པ་བཞི་དང་ཅི་རིགས་པ་དང༌[^1988]སྦྱར་རོ། །

[Block 2372]
མྱ་ངན་ལས་འདའ་བ་དང་། མ་འདས་པ་ཡང་དྲང་བའི་དོན་གྱི༌[^1989]ཐེག་པ་རྣམ༌[^1990]གཉིས་ལ་བསྟན་པ་དང་། ངེས་པའི་དོན་གྱིས་བླ་ན་མེད་པའི་ལམ་དང་སྦྱོར་བའོ། །

[Block 2373]
དེ་ལྟར་དགོངས་ཏེ་ཆོས་རྒྱལ་ཞེས་པའང་ངེས་པའི་དོན་ལ་མངོན་སུམ་དུ་གཟུད༌[^1991]པའི་ཕྱིར་འཇིག་རྟེན་ལ་བདེ་བའི་ཕྱིར་ཞེས་པ་དང་སྦྱར་རོ། །

[Block 2374]
ཆོས་རྒྱལ་ཞེས་པ་ནི་སེམས་ཅན་རྣམས་ལ་སོ་སོའི་དབང་པོ་ལ་སྦྱོར་ཞིང་ཆོས་ལ་མངའ་བརྙེས་པའི་ཕྱིར་ཆོས་རྒྱལ་ཞེས་བྱའོ། །

[Block 2375 [HEADING]]
###### **བསླབ་པར་བྱ་བའི་གནས།** ^4-3-5-4-2-2-2-0

[Block 2376]
མདོ་ལས།

[Block 2377 [HEADING]]
###### **སྣོད་མ་རྟོགས་པར་ཆོས་མ་གཏོད་ཅིག་པ།** ^4-3-5-4-2-2-2-1-0

[Block 2378]
འདི་ངའི་ཆོས་རྒྱལ་ཤཱ་རིའི་བུ། །ཞེས་པ་ནས། ཁྱོད་ཀྱི་མི་དེ་མི་ལྡོག་གཟུད། །ཅེས༌[^1992]པའི་བར་དུ་དེ་ནི། སྣོད་མ་རྟོགས་པར་ཆོས་མ་གཏོད་ཅིག་པར་བསྟན་པ་སྟེ། ཆོས་ཀྱི་ཕྱག་རྒྱ་ཞེས་པ་ནི། ཐེག་པ་གཅིག་པོའི་གཞུང་དམ་པ་ངེས་པ་ཉིད་ལ་བྱའོ། །

[Block 2379]
རྗེས་སུ་ཡི་རང་ཞེས་པ་ནི་མོས་པ་ཆེ་བའི་ཕྱིར་མི་ལྡོག་ཅེས་པ་སྟེ། ཡུན་རིང་པོ་ནས་དགེ་བའི་རྩ་བ་བསྐྱེད་པ་ས་ལ་གནས་པར་གྱུར་པའོ། །

[Block 2380]
ཐེག་པ་རྣམ་གཉིས་ལྟ་བུ་ལས་ཁྱད་པར་དུ་བསྟན་པའོ། །

[Block 2381]
མདོ་ལས་སྔོན་གྱི་དེ་བཞིན་གཤེགས་པ་དེས་མཐོང་ཞེས་པ་ནས། སངས་རྒྱས་ཀྱི་ས་འདི་མི་ཤེས༌[^1993]པའི་བར་དུ་དེ་དག་གིས་ནི་སྔོན་དེ་བཞིན་གཤེགས་པའི་བསྟན་པ་ལ་ཞུགས་ཤིང་ཐོས་པའི་རྒྱུས་འདི་ལ་འཇུག་ནུས་པར་བསྟན་པ་དང་། མདོ་འདི་ལ་དད་ཅིང་འཇུག་པ་ནི་དེས་ང་དང་ངའི་དགེ་འདུན་མཐོང་ཞེས་པ་ཡང་དཀོན་མཆོག་གསུམ་ཐ་མི་དད་པའི་མཚན་ཉིད་བསྟན་པའོ། །ཤེས་པ་ཆུང་བ་དང་དགེ་བའི་རྩ་བ་ཞན་པ་རྣམས་ཀྱིས་འཇུག་པར་མི་ནུས་པའི་ཕྱིར་བྱིས་པ་མྱོས་གྱུར་པ་ཞེས་གསུངས་སོ། །

[Block 2382]
ཐེག་པ་རྣམ་གཉིས་སུ་རིགས་ངེས་པ་རྣམས་ཀྱིས་ཀྱང་འཇུག༌[^1994]པའི་ཕྱིར་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ས་མ་ཡིན་ཞེས་གསུངས་སོ། །

[Block 2383]
མདོ་ལས།

[Block 2384]
ཤཱ་རིའི་བུ་ཁྱོད་ང་དང་འབྲང༌[^1995]ན་ཞེས་པ་ནས། འདི་དག་རང་རིག་ཡེ་ཤེས་མེད། །ཅེས་པའི་བར་དུ་ནི་རིགས་མ་ངེས་པའི་ཉན་ཐོས་རྣམས་ཀྱང་ངའི་གསུང་འདི་ཐོས་ནས་གདོད་དད་པ་སྐྱེ་ཞིང་རྗེས་སུ་འབྲང་བར་འགྱུར་ན་གཞན་ལྟ་ཅི་སྨོས་ཞེས་བསྟན་པའོ། །

[Block 2385 [HEADING]]
###### **བསྟན་དུ་མི་རུང་བ།** ^4-3-5-4-2-2-2-2-0
--- END BLOCKS ---
