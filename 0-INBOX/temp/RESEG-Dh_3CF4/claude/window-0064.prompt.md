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

[Block 2246]
དེ་བརྟན་པའི་ངང་ཚུལ་གང་ཡིན་པ་དེ་ནི་མི་དགའ་བ་འབྱུང་བའི་ཚུལ་ལོ། །

[Block 2247]
ཡང་དང་ཡང་བོས་ཏེ་དེ་གཉིས་ལན་མེད་པས་ཞེས་བྱ་བ་ནི༌[^1421]མ་ཐོས་པ་སྟེ་བོད་པས་དེ་གཉིས་གཅིག་གིས་ཀྱང་མ་ཐོས་པའོ། །

[Block 2248]
དེ་གཉིས་ནི་དེ་དག་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2249]
རྩེ་རྩེ་ངལ་ནས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི༌[^1422]ནི་འཚོ་བའི་གནས་སྐབས་ན་ཡང་མ་མཐོང་བས་བྲལ་བའི་སྡུག་བསྔལ་གྱི་དབང་དུ་བྱས་པའོ། །

[Block 2250]
རྩེ་རྩེ་བ་ལས་བྱུང་བའི་ངལ་བ་ནི་རྩེ་རྩེ་ངལ་བའོ། །

[Block 2251]
དེ་ལས་སྐྱེས་པའི་གཉིད་གང་ཡིན་པ༌[^1423]དེ་ནི་རྩེ་རྩེ་ངལ་ནས་སྐྱེས་པའི་གཉིད་དོ། །

[Block 2252]
བདག་འོངས་མཆིས་པས༌[^1424]ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་འཆི་བའི་གནས༌[^1425]སྐབས་ལ་རྣམ་པར་རྟོག་པའི་དབང་དུ་བྱས་པའོ། །

[Block 2253]
གང་གི་ཕྱིར་དེ་གཉིས་ཤི་བ་ནི་མ་ཡིན་ཏེ། དེ་བསད་མཐོང་ན་འདི་ལྟར་སྒྲ་མི་འབྱིན་པའོ། །

[Block 2254]
བྱའི་སྒྲ་མེད་པར་ཡང་འཆི་བ་སྲིད་དོ་ཞེས་རྣམ་པར་རྟོག་པ་ལས་བརྩམས་ནས། འབབ་ཆུ་དྲག་པོ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་འོག་མའོ། །

[Block 2255]
འདི་ལ་ལྟས་བཟང་པོ་ཡོད་པ་མ་ཡིན་པ་ནི་ལྟས་ངན་པའོ། །

[Block 2256]
ལྟས་ངན་པས་བཟློག་པའི་དགའ་བའི་སེམས་གང་ཡིན་པ་དེ་ནི་སྙིང་འདི་ཡང་ལྟས་ངན་པས་དགའ་བ་ནི་བཟློག་པའོ། །

[Block 2257]
གས་པ་ནི་ཟག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2258]
དགའ་བར་བྱ་རིགས་ཞེས་བྱ་བ་ནི་དགའ་བར༌[^1426]ཐོས་པར་རིགས་པའོ། །

[Block 2259]
ཆེད་ཀར༌[^1427]ཞེས་བྱ་བ་ནི་མངོན་པར་གནོད་པའི་ཕྱིར་རོ། །

[Block 2260]
ཀྱི་ཧུད་བདག་ནི་བསད་ཀྱིས་མེད། །ཅེས་བྱ་བ་ནི་ཤི་བའི་དོན་ཏོ། །

[Block 2261]
[^1428]ཟད་པའམ་ཤི་བས་བདག་ཉིད་ཀྱང་ངེས་པར་འཆི་བའི་ཕྱིར་བསད་ཅེས་བསྟན་ཏོ། །

[Block 2262]
བརྟན་པ༌[^1429]མེད་དུ་དོགས་པས་ན། །ཞེས་བྱ་བ་ནི་གལ་ཏེ་བརྟན་པ༌[^1430]མེད་དུ་དོགས་པས་འཆི་པར་འགྱུར་རོ་ཞེས་དོགས་པའི་དོན་ཏོ། །

[Block 2263]
རྒས་པ་དང་དབུལ་བ་ནི་རྒས་ཤིང་དབུལ་བའོ། །

[Block 2264]
དེ་ཉིད་ཀྱི་སྡུག་བསྔལ་ནི་རྒས་ཤིང་དབུལ་བའི་སྡུག་བསྔལ་ཏེ། དེས་སྡུག་བསྔལ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2265]
འདིས་ནི་སྙིང་རྗེའི་དོན༌[^1431]བསྟན་ཏོ། །

[Block 2266]
བྲམ་ཟེ་ཞེས་བྱ་བ་འདིས་ནི་ཡོན་ཏན་གྱི་ཞིང་དུ་བསྟན་ཏོ། །

[Block 2267]
ཡང་ན་རྒས་ཤིང་དབུལ་བའི་སྡུག་བསྔལ་གྱིས་ཉེན་པ་ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་བ་ཉིད་དོ། །

[Block 2268]
བྲམ་ཟེ་ཞེས་བྱ་བ་ནི་སློང་བ་ཉིད་དུ་བསྟན་ཏེ། [^1432]སློང་བས་འཚོ་བ་དེ་བས་ན༌[^1433]བྲམ་ཟེ་ཞེས་བརྗོད་དོ། །

[Block 2269]
ང་གན་འོངས་ཞེས་བྱ་བ་ནི་རྟེན་མེད་པ་ཉིད་དེ། གང་གཞན་དུ་མི་རྙེད་པར་བྱེད་པའི་གནས་འདི་ན་འོངས་ཤིང་སྤྱོད་པ་སྟེ། གང་གི་ཕྱིར་བདག་ལ་སློང་བ་དེ་བས་ན་དེ་རྟེན་མེད་པས་དེས་རྟོགས་པར་བྱའོ། །

[Block 2270]
བུ་ལ་མ་བལྟས་ན་ཇི་ལྟར་ཁྱོད་ལ་བལྟ་བར་བྱ་ཞེ་ན། སྨྲས་པ། མྱ་ངན་གདུང་བར་མ་བྱེད་ལ། །ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2271]
དེ་ལྟ་ན་ཅི་ཞིག་བྱ་བ་ཡིན་ཞེ་ན། བུ་ཡི༌[^1434]མྱ་ངན་གདུང་སྙིང་ལ། །མཚོན་གྱིས་འདེབས་པ་ཞེས་སྨོས་ཏེ་མཚོན་དང་འདྲ་བའི་ཕྱིར་རོ། །

[Block 2272]
དེ་ལ་མྱ་ངན་གྱིས་ཡོངས་སུ་གདུངས་ན་ཅིའི་ཕྱིར་བུ་བྱིན་ཞེས་བྱ་བ་ཡིན་ཞེ་ན། ཚིག་གི་སྐབས་ཤེས་པར་བྱས་ནས། བསླངས་པར་གྱུར་ན་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2273]
བུ་ཤིར་དོགས་དེ་སྙིང་བཙོས་པ་ལས་ཞེས་བྱ་བ་ནི་བུ་ཤིར་དོགས་པའི་སྙིང་གི་གདུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2274]
འདི་ལྟར་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་ཏེ། གང་གིས་སྐབས་མ་རྙེད་པ་དེ་ནི་སྐབས་མ་རྙེད་པའོ། །

[Block 2275]
དེ་གང་ཞེ་ན་འཇུངས་པའོ། །

[Block 2276]
བྲག་ཅའི་སྒྲའི་ཁྱབ་པའི་སྒྲ་གང་ཡིན་པའི་རྔ་སྒྲ་ཆེན་པོའི་སྒྲ་དེ་ནི་ཁྱབ་པའི་བྲག་ཅ་དང་སྒྲ་བརྙན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2277]
གསལ་བའི་ཚིག་དང་འབྲུ་གང་ཡིན་པའི་ནམ་མཁའ་དེ་ནི་ཚིག་འབྲུ་གསལ་བའི་ནམ་མཁའ་ལའོ། །

[Block 2278]
གཡོ་བ་གང་ལ་ཡོད་པ་དེ་ནི་གཡོ་བ་ཅན་ཏེ་རབ་ཏུ་གཡོ་བ་ཅན་ནོ། །

[Block 2279]
རིའི་ནུ་མ་གཡོ་བ་ཅན་གང་ཡིན་པ་དེ་ནི་རིའི་ནུ་མ་གཡོ་བ་ཅན་ནོ། །

[Block 2280]
ནམ་མཁའ་ནི་མཐོ་རིས་སོ། །
--- END BLOCKS ---
