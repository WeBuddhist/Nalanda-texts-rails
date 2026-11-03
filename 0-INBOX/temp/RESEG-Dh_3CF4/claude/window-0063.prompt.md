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
དེ་ལྟར་བྱས་ན་ནོར་ཆེན་དང་། །ཞེས་བྱ་བ་ནི་བུའི་གླུད༌[^1397]ཀྱི་ཕྱིར་ཐོབ་པར་འགྱུར་བའོ། །

[Block 2207]
ཆོས་རྣམས་དང་ཡང་ལྡན་པར་འགྱུར། །ཞེས་བྱ་བ་ནི་ནོར་ཆེན་པོ་དེ་ཉིད་ཀྱིས་ཆོས་བྱེད་ནུས་པའི་ཕྱིར་དང་། བྱིས་པའི་ཉོན་མོངས་པ་མེད་པའི་ཡང་ཕྱིར་རོ། །

[Block 2208]
སྦྲུལ་གདུག་པ་དང་འདྲ་བའི་དྲུང་དུ་ཞེས་བྱ་བ་ནི་སྦྲུལ་གདུག་པ་ལྟ་བུར་བསྙེན་པར་དཀའ་བས་སོ། །

[Block 2209]
མི་དགའ་བ་ཉིད་ཀྱི་སྐྱེས་པ་ཡིན་པས་མི་དགའ་བའི་སྐྱེས་སོ། །

[Block 2210]
དེ་ལྟ་བུའི་མཚན་ཉིད་དང་ལྡན་པའི་རྒྱལ་པོའི་དྲུང་དུ་འགྲོ་བའི་ཉེས་དམིགས་བསྟན་པའི་ཕྱིར་རྒྱལ་པོས་བདག་ལ་འདི་གཉིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2211]
བྲམ་ཟེ་མོའི་གཡོག་ཏུ་བདག་ནི་ཁྲིད་དེ་མཆི་ཞེས་བྱ་བ་ནི་རྒྱལ་པོའི་གམ༌[^1398]དུ་མི་འགྲོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2212]
དོན་ཡོངས་སུ་མ་རྫོགས་པར་ཞེས་བྱ་བ་ནི་ད་ཁྱོད་ཀྱིས་ཇི་ལྟར་དགའ་བ་དེ་དེ༌[^1399]བཞིན་དུ་གྱིས་ཤིག་པ་སྟེ། དེ་ལྟར་དོན་ཡོངས་སུ་མ་རྫོགས་པའོ། །

[Block 2213]
གཡོག་ལེགས་པར་བྱོས་ཞེས་བྱ་བ་ནི་བག་ཡོད་པར་ཡོངས་སུ་སྤྱད་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 2214]
དེའི་བསྒྲིམས་པའི་མཐུ་ཞེས་བྱ་བས་ནི་འབད་པས༌[^1400]རྗེས་སུ་འཇུག་པ་སྟེ། དེས་ན་འབད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2215]
མདོར་སྨྲས་ནས་ཞེས་བྱ་བ་ནི་རྒྱལ་བར་གྱུར་ཅིག་ཅེས་སོ། །

[Block 2216]
བྲལ་བའི་སྡུག་བསྔལ་ཉིད་ཁུར་ཆེན་པོ་ཡིན་པས་བྲལ་བའི་སྡུག་བསྔལ་གྱི་ཁུར་རོ། །

[Block 2217]
དེས་གདུངས་པའི་སྙིང་གང་ཡིན་པ་དེ་ནི་བྲལ་བའི་སྡུག་བསྔལ་གྱིས་གདུངས་པའོ། །

[Block 2218 [VERSE]]
ཡབ་གཅིག་ཡུམ་ཡང་སླད་རོལ་འབྱུང་། །
ཁྱོད་ཀྱང་བདག་ཅག་གཏོང་བར་བཞེད། །

[Block 2219]
ཅེས་བྱ་བ་ནི་གང་གི་ཚེ་མ་སླད་རོལ་དུ་འབྱུང་བ་དེའི་ཚེ་སྦྱིན་པར་བཞེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2220]
སྡུག་བསྔལ་གྱི་མྱོང་བ་ནི་སྡུག་བསྔལ་མྱོང་བའོ། །

[Block 2221]
དེ་ཉིད་དང་པོར་སྡུག་བསྔལ་མྱོང་བ་གང་ཡིན་པ་དེ་ནི་སྡུག་བསྔལ་དང་པོ༌[^1401]མྱོང་བ་དེའོ།[^1402] །དེ་བས་ན་སྐད་ཕྱུང་སྟེ་ཞེས་བྱ་བ་ནི་སྒྲ་དང་བཅས་པའོ། །

[Block 2222]
བྲམ་ཟེ་ཞེས་བསྟན་པ་ལ། གལ་ཏེ་བྲམ་ཟེ་ཡིན་ན་ནི་གང་གི་ཕྱིར་འདི་ནི་བརྩེ་བ་མེད་པ་སྟེ། དེ་བས་ན་འདི་ནི་བྲམ་ཟེ་མ་ཡིན་ཏེ། བྲམ་ཟེའི་མཚན་ཉིད་ནི་ཆོས་དང་ལྡན་པ་ཉིད་དེ་དེ་མེད་པས་སོ། །

[Block 2223]
དེ་ལྟ་ན་འདི་གང་ཞིག་ཡིན་ཞེ་ན་གནོད་སྦྱིན་ཞེས་སྨོས་སོ། །

[Block 2224]
ཅིའི་ཕྱིར་ཞེ་ན། བརྩེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2225]
བྲམ་ཟེར་བསྒྱུར་ནས་ནི་ཞེས་བྱ་བ་ནི་ཆ་བྱད་དོ། །

[Block 2226]
གནོད་སྦྱིན་གྱིས་ཅིའི་ཕྱིར་ཁྲིད་པ་བཞིན༌[^1403]ཞེ་ན་བཟའ་བའི་ཕྱིར་རོ། །

[Block 2227]
བྲམ་ཟེ་བདག་ལ་བརྡེག་པ་འདི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་ནི་བདག་ཉིད་དེ་དང་བྲལ་བའི་སྡུག་བསྔལ་གྱི་དབང་དུ་བྱས་པའོ། །

[Block 2228]
དཀའ་ཐུབ་ནགས་ཚལ་སྟོང་པ་ན། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གཉིས་ཀྱིས༌[^1404]བདག་ཉིད་དང་བྲལ་བའི་སྡུག་བསྔལ་གྱིས༌[^1405]མའི་དབང་དུ་བྱས་པའོ། །

[Block 2229]
གླང་པོ་ཆེ་ལྟ་བུ་ཡིན་པས་གླང་ཆེན་ཏེ། གླང་པོ་ཆེ་བྱས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2230]
དེ་བཞིན་དུ་ཤིང་རྟ་དང་། རྟ་པ་དང་། རྐང་ཐང་ཡང་ངོ་། ། ཕྱེད་ཙམ་ཡུམ་ལ་ཕུལ་ན་ནི། །ཞེས་བྱ་བས༌[^1406]ནི་ཕྱེད་ནི་ཁྱོད་ཉིད་ལ་ཞེས་བྱ་བ་ཡིན་ནོ། །ཅིའི་ཕྱིར་འདི་སྦྱིན་ཞེ་ན།

[Block 2231 [VERSE]]
མྱ་ངན་བསལ་བའི༌[^1407]ཕྱིར་རོ། །
འཕྲིན་གྱིས་ཡུམ༌[^1408]ལ་ཕྱག་འཚལ་ཞིང་། །

[Block 2232]
ཞེས་བྱ་བ་ཅི་ཞེ་ན། ཞལ་ནི་མཐོང་བ་རབ་ཏུ་དཀའ་བ་ཉིད་དེ། ཐུགས་ངན་མཛད་ལས་བཟློག་ཏུ་གསོལ། །ད་ཡང་ཞལ་མཐོང་དཀའ་བའི་ཕྱིར་ཏེ། ཞལ་མཐོང་བ་མི་སྲིད་པ་ལ་མྱ་ངན་དོན་མེད་པའི་ཕྱིར་རོ། །

[Block 2233]
བྲམ་ཟེ་ངན་པ༌[^1409]ངོ་མི་ཚ། །ཞེས་བྱ་བ་ནི་མ་བསྟན་པ་རྗེས་སུ་བསྟན་པ་སྟེ། གཞན་དུ་ན་བྲམ་ཟེ་ཁོ་ན་ཞེས་མི་བརྗོད་ཅིང་ཚིག་དེ་ཡང་སྩལ༌[^1410]བ་མེད་པས་སོ། །

[Block 2234]
ལྷམ་ཡང་མེད་པར་རྐང་གིས་འདོང་། །ཞེས་བྱ་བ་འདི་ནི་ལམ་གྱི་སྡུག་བསྔལ་གྱི་དབང་དུ་བྱས་པའོ། །

[Block 2235]
ལམ་དེའི་སྡུག་བསྔལ་ཡང་རྒྱུ་གསུམ་གྱིས་འབྱུང་བ་ཡིན་ཏེ། ལམ་གྱིས་དུབ་པ་སོ་བ་མེད་པ་དང་། གནས་ཀྱི་ཁྱད་པར་དང་གཞན་གྱི་དབང་དུ་བྱས་པས༌[^1411]སོ། །

[Block 2236]
ལྷམ་ཡང་མེད་པར་རྐང་གིས་འདོང་། །ཞེས་བྱ་བ་འདིས་ནི་ལམ་གྱི་ངལ་སོ་བ་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2237]
རབ་ཏུ་གཞོན་པས་ངལ་མི་བཟོད། །ཅེས་བྱ་བ་འདིས་ནི་གནས་ཀྱི་ཁྱད་པར་བསྟན་ཏོ། །

[Block 2238]
དེའི་བྲན་གཡོག་བྱེད་པ་ཞེས་བྱ་བ་འདིས་ནི་རང་བཞིན༌[^1412]མེད་པ་ཉིད་དུ་བསྟན་ཏེ། དེ་ལྟར་ཡོངས་སུ་ངལ་སོར་མེད་པའི་དབང་དུ་བྱས་ནས། ལམ་གྱིས་ངལ་ཞིང་དུབ་པ་ལ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2239]
དང་པོའི་ཕྱེད་ཀྱིས་ནི་ལམ་གྱིས་དུབ་པའི་ངལ་སོ་བ་མེད་པ་ལས་བརྩམས་སོ། །

[Block 2240]
ཕྱེད་གཉིས་པས་ནི་ལྷན་ཅིག་སྐྱེས་པའི་བཀྲེས་པ་དང་སྐོམ་པའི་སྡུག་བསྔལ་གསོ༌[^1413]བ་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2241]
བདག་ནི་བརྟན་པར་བྱེད་འདོད་ཀྱང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་དོན་ནི་སོ་སོར་རྟོག་པའི་སྟོབས་ཡོད་ཀྱང་ངོ་། །བུ་ནི་བྱིས་པ་སྟེ་སོ་སོར་རྟོག་པ་མེད་པས་སོ། །

[Block 2242]
རེ་ཞིག་བདག་འདི་ལྟ་བུར་ནི་སྡུག་བསྔལ་ན༌[^1414]ཞེས་བྱ་བ་བསྟན་པ་ལ་དེའི་སྡུག་བསྔལ་བསྟན་པའི་ཕྱིར།

[Block 2243 [VERSE]]
ཀྱེ་མའོ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་འདི༌[^1415]སྨོས་སོ། །
བསྟན་པར༌[^1416]བྱེད་འདོད་ཀྱང་ཞེས་བྱ་བ་བསྟན་པ་ལ། །

[Block 2244]
ཇི་ལྟར་བསྟན་པར༌[^1417]བྱེད་པར༌[^1418]འདོད་པ་ཡིན། །ཞེས་པ་དེ་ལས་བརྩམས་ཏེ། དམ་པ་རྣམས་ཀྱི༌[^1419]ཆོས་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་ཕྱེད་འོག་མའོ། །

[Block 2245]
མི་དགའ༌[^1420]འབྱུང་བ་ནི་མི་དགའ་བ་དག་འབྱུང་བའོ། །
--- END BLOCKS ---
