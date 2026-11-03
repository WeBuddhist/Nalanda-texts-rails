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
ཅི་བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ཀྱི་ཚད་ཐམས་ཅད་ལ་བྱེད་དམ་བྱེད་དུ་བཅུག་པ་ལ་ལྟུང་བྱེད་དུ་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་དེའི་ལུས་ཙམ་མེད་པར་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་བདེ་བར་གཤེགས་པའི་སྐུའི་ཚད་ཙམ་གྱི་ལུས་མེད་པ་དེས་སོ། །

[Block 2242]
བདེ་བར་གཤེགས་པའི་སྐུའི་ཚད་ཀྱི་ལུས་ཡོད་པ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 2243]
དེའི་འོག་ཏུ་ལྷག་པ་ལ་ནི་ཅི་རིགས་པར་ཁ་ན་མ་ཐོ་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2244]
གང་ལ་བདེ་བར་གཤེགས་པའི་སྐུའི་ཚད་ཙམ་གྱི་ལུས་མེད་པ་དེས་དེ་ལ་ཆོས་གོས་ཀྱི་ཚད་ལ་སོགས་པ་བྱེད་དམ་བྱེད་དུ་བཅུག་པ་ལ་ལྟུང་བྱེད་དོ། །

[Block 2245]
བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ལས་ནི་ཆུང་ལ་རང་གི་ལུས་ལས༌[^1420]ནི་ཆེ་བའི་ཆོས་གོས་བྱེད་དམ་བྱེད་དུ་བཅུག་པ་ལ་ཉེས་བྱས་སོ། །

[Block 2246]
གང་ལ་བདེ་བར་གཤེགས་པའི་སྐུའི་ཚད་ཙམ་མམ། དེ་ལས་ལྷག་པའི་ལུས་ཡོད་པ་དེས་རང་གི་ཁྲུ་སུམ་འགྱུར་ལ་སོགས་པ་བྱེད་དམ་བྱེད་དུ་བཅུག་ན་ལྟུང་བྱེད་དེ་སུམ་འགྱུར་དུ་མ་ཆོག་པ་ལ་ཉེས་བྱས་ཞེས་བྱ་བར་འདིར་རྣམ་པར་གཞག་པར་རྟོགས་པར་བྱའོ། །

[Block 2247]
འདིར་གཞུང་ནི་གཏམ་གྱི་གཞི་ལས་ཚད་དང་ལྡན་པར་བགྱིད་པ་ལ༌[^1421]ལྟུང་བར་འགྱུར་བ་དང་། ཚད་དང་ལྡན་པར་མི་བགྱིད་པ་ལ་ལྟུང་བར་མི་འགྱུར་བ་འགའ་མཆིས་སམ། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཡོད་དེ། བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ཀྱི་ཚད་དུ་བྱེད་ན་ལྟུང་བྱེད་དོ། །

[Block 2248]
དཀྱིལ་འཁོར་གྱི་ཚད་དུ་བྱེད་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2249]
དེ་བཅང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། [^1422]དེ་ཞེས་བྱ་བ་ནི་བདེ་བར་གཤེགས་པའི་ཆོས་གོས་སམ་བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ལས་ལྷག་པ་བྱེ་བྲག་མ་སྨོས་པའི་ཕྱིར་རོ། །

[Block 2250]
ལུས་དང་འབྲེལ་པས་སམ་གཞན་ཡང་རུང་སྟེ། བྱིན་གྱིས་བརླབས་ནས་སམ་རྣམ་པར་བརྟགས་ནས་སམ། རྣམ་པར་མ་བརྟགས་པར་བཅང་བར་མི་བྱའོ། །

[Block 2251]
འདིར་གཞུང་ནི་གོས་ཀྱི་གཞི་ལས་བཙུན་པ་བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ཙམ་ལས་དེ་འདིར་གསུངས་པ་ཡིན་ཏེ། དེ་ནི་ཆོ་གའི་རྗེས་སུ་འབྲང་བར་འོག་མ་ཡང་ཁོངས་སུ་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 2252]
བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ཀྱི་ཚད་ལས་གྱུར་པའི་ལྟུང་བྱེད་དོ།[^1423] །ལྟུང་བྱེད་འབའ་ཞིག་ཏུ་གྱུར་པ་རྣམས་རྫོགས་སོ།། །།

[Block 2253 [HEADING]]
## དགེ་སློང་གི་སོ་སོར་བཤགས་པ་རྣམས། ^2-0

[Block 2254]
དགེ་སློང་མ་ལས་བསོད་སྙོམས་ལེན་པའི་སོ་སོར་བཤགས་པར་བྱ་བ་ལ་བྱེད་པ་པོ་ཉིད་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཤེས་གཙོ་བོ༌[^1424]ཞེས་བྱ་བ་སྨོས་ཏེ། འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ༌[^1425]ཡིན་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མ་ཉེ་དུ་མ་ཡིན་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2255]
ཅི་ཞིག་རྗེས་སུ་སྒྲུབ༌[^1426]ན་དེ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རང་གིས་མི་འདྲིམ༌[^1427]པར་བསྒྲུབས་པའི་བཅའ་བ་དང་བཟའ་བ་བདག་ཉིད་གྲོང་ན་འདུག་པས་བླངས་ཏེ་ཟོས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མ་གྲོང་ངམ་གཞན་གང་ཡང་རུང་བ་ན་འདུག་པས་རང་གི་ལག་གིས་མི་འདྲིམ་པའི་རྣམ་པས་དགེ་སློང་བདག་ཉིད་གྲོང་ན་འདུག་པས་རང་གི་ལག་གིས་བླངས་ཏེ་བཅའ་བ་དང་བཟའ་བ་དག་ཞེས་པའི་དོན་ཏོ།[^1428] །རང་གིས་ཞེས་བྱ་བ་ནི། བྱིན་ལེན་བྱེད་པ་པོ་ལ་སྨོས་སོ། །

[Block 2256]
རང་གི་ལག་གིས་ཞེས་བྱ་བ་ནི་སྦྱིན་བདག་ཉིད་མ་ཡིན་པས་ཏེ། དེའི་རྗེས་སུ་འབྲངས་ནས་འདི་བྱས་པ་ཡིན་ནོ། །

[Block 2257]
རྗེས་སུ་མཐུན་པ་གཞན་ལ་ལེན་པ་ལ་ཀུན་ནས་ཆགས་པའི་དམིགས་ཀྱིས་བསལ་བ་ཞེས་བྱ་བ་རང་གི་གཟུང༌[^1429]བ་ལ་ཡོངས་སུ་ཤེས་པའོ། །

[Block 2258]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་རེ་ཞིག་དགེ་སློང་མའི་དབྱར་ཁང་ན་མཆིས་པ་ན༌[^1430]དགེ་སློང་མ་གྲོང་ན་གནས་པས་མཆིས་སམ་བཅའ་བ་དང་བཟའ་བ་རྩོལ་ལ། དེས་དེ་ན་མཆིས་པ་ལས་ལེན་ཅིང་བླངས་ནས་འཚལ་བར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2259]
དེ་བས་ན་འདིར་ལེན་པ་པོ་གྲོང་ན་གནས་པའི་ཉིད་རྟེན་ཏོ། །

[Block 2260]
སྦྱིན་པ་མོ་ལ་ནི་ཁྱད་པར་མེད་དོ། །

[Block 2261]
གཉིས་ཀ་ལ་ཡང་འདིའི་ཡན་ལག་ཉིད་ལ་འདིར་ཉེས་བྱས་སུ་རྣམ་པར་གཞག་པའོ། །

[Block 2262]
གང་ཞིག་ལམ་ལ་བརྟེན་པས་གྲོང་དུ་བསོད་སྙོམས་ཀྱི་ཕྱིར་ཞུགས་པ་ནི་ཞེས་བྱ་བ་གསུངས་ན་དགེ་སློང་ལ་གྲོང་ན་གནས་པ་ཉིད་འདི་ལ་བསྟན་པའི་དོན་དུ་ཚུལ་འདི་ཞུ་བའི་གཞུང་འདི་ཉིད་ལས་ཤེས་པར་བྱའོ། །

[Block 2263]
གང་ཞིག་འདི་རྫས་ཞེས་བྱ་བའི་ཚིག་འདི་ལས་རང་གིས༌[^1431]མི་འདྲིམ་པར་ཞེས་བྱ་བ་མདོར་བྱས་པས་བསོད་སྙོམས་སྡུད་པ་ལ་འདི་བསྟན་པ་ཡིན་གྱི་མི་མཐུན་པའི་རྣམ་པ་ཉིད་ཀྱང་འདིར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2264]
དབྱར་ཁང་ནི་གྲོང་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་གཞུང་ནི་ཞུ་བ་ལས།

[Block 2265]
ལྟུང་བ་མེད་དོ་ཞེས་སྔར་བསྟན་མ་ཐག་པ་ཡིན་ནོ། །

[Block 2266]
དགེ་སློང་གི་གནས་ཀྱང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གྲོང་ཉིད་མ་ཡིན་པའོ། །

[Block 2267]
འདིར་གཞུང་ནི་ཞུ་བ་ལ་སོགས་པའི་གཞུང་ཁ་ཅིག་ལས།

[Block 2268]
བཙུན་པ་རེ་ཞིག་གནས་ཙམ་དུ་འཛིན་པ་ཡོད་དེ་དགེ་སློང་དག་དགེ་སློང་མ་ཉེ་དུ་མ་ཡིན་པའི་ཁྱིམ་གཞན་དུ་ཞུགས་པ་ལས་བཅའ་བ་དང་བཟའ་བ་བླངས་ཏེ་འཆོས་ཤིང་འཚལ་ན་ལྟུང་བར་མི་འགྱུར་བ་འགའ༌[^1432]མཆིས་སམ། ཡོད་དེ་དགེ་སློང་གནས་ན་འདུག་པས་དགེ་སློང་མའི་ཁྱིམ་གཞན་ན་འདུག་པ་ལས་ལེན་ནའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2269]
དགེ་སློང་མའི་གནས་ལས་དགེ་སློང་གི་གནས་ལ་དགོས་པའི་ཁྱད་པར་འདི་ཡོད་པ་མ་ཡིན་ཏེ། དེ་བས་ན་སྔ་མ་ལས་ཀྱང་འདི་ཐོབ་པའོ། །

[Block 2270]
ནམ་མཁའ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གྲོང་གི་སྟེང་གི་ནམ་མཁའ་ལ་འདུག་པ་བླངས་ཏེ་ཟ་ན་ཉེས་བྱས་སུ་འགྱུར་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2271]
འཇོག་པར་བྱེད་པ་ཉེ་བར་མི་གནས་ན་གཞག་པ་ལེན་པ་ནི་དེ་ལས་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་ནི་འཇོག་པར་བྱེད་པས་བཟའ་བར་བྱ་བ་གང་ཡིན་པ་འཇོག་པར་བྱེད་པ་ཉེ་བར་མི་གནས་པ་ལ་དེ་ལེན་པར་བྱེད་ཀྱང་འཇོག་པར་བྱེད་པ་དེའི་དྲུང་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2272]
འདིར་གཞུང་ནི་དགེ་སློང་མས་གྲོང་དུ་བཞག་པར་གྱུར་པ་དགེ་སློང་གིས་ཡིད་གཅུགས༌[^1433]པས་བླངས་ཏེ་ཟ་བར་བྱེད་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2273]
གལ་ཏེ་ཡིད་གཅུགས་པ༌[^1434]མེད་པས་ལེན་ན་ནི་ཁ་ན་མ་ཐོ་བ་འདིར་མི་འགྱུར་ཏེ། འོན་ཀྱང་མ་བྱིན་པར་ལེན་པར་གཏོགས་པའོ། །

[Block 2274]
དེ་ལྟ་བས་ན་ཡིད་ཆེས་པའི་ཚིག་འདི་ལ་བྱེད་པའོ། །

[Block 2275]
དགེ་སློང་མ་ལས་ཟས་ལེན་པའི་སོ་སོར་བཤགས་པར་བྱ་བ་སྟེ་དང་པོའོ།། །།

[Block 2276]
བཤགས་པར་བྱ་བ་གཉིས་པ་ལ་བྱེད་པ་པོ༌[^1435]གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེའམ་དགེ་སློང་གཞན་དག་ལ་བཟའ་བའམ་བཏུང་བ་འམ་སྲན་ཚོད་དམ། བཅའ་བའམ་ཡང་བྱིན་ཅིག་ཅེས་བྱ་བ་ལ་སོགས་པས་བསྐོ་ཤམ་བྱེད་པ་ལ་ཞུགས་པའི་དགེ་སློང་མ་འདུག་པ་ནི་བྱེད་པ་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སོགས་པ་ཞེས་བྱ་བའི་སྒྲས་ནི་ཟས་ལྷག་མ་དག་སྟོབས་པ་ཡང་བསྡུས༌[^1436]པའི་ཕྱིར་རོ། །

[Block 2277]
བསྐོ་ཤམ་བྱེད་པ་ཞེས་བྱ་བ་འདིས་འདི་ལ་འབྲེལ་པ་ཡིན་ཏེ། དེའི་འདི་ངོ་བོ་ཉིད་བརྗོད་པ་ཡིན་ནོ། །

[Block 2278]
བསྐོ་ཤམ་བྱེད་པ་ལ་ཞུགས་པའི་དགེ་སློང་མ་འདུག་པ་ལ་ནི་དེ་བས་ན་ཚིག་འདིའོ། །

[Block 2279]
དེའམ༌[^1437]དགེ་སློང་གཞན་ལ་ཞེས་བྱ་བ་ལ། དེའམ༌[^1438]ཞེས་བྱ་བ་ལྟུང་བ་འབྱིན་པ་པོ་ཉིད་ལ་མངོན་པར་བརྟེན་པའི་དགེ་སློང་གཟུང་བའོ། །

[Block 2280]
ཅི་དགེ་སློང་མ་དེ་ལྟ་བུར་གྱུར་པ་ཐམས་ཅད་ཀྱི་འདུག་པ་དེ་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་དེའི་ཚིག་གིས་སམ། དེའི་ཉེ་དུས་མགྲོན་དུ་བོས་པ་མ་ཡིན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་བསྐོ་ཤམ་བྱེད་པ་ལ་ཞུགས་པའི་དགེ་སློང་མ་དེ་ལ་ཉེ་དུས་མགྲོན་དུ་བོས་པ་མ་ཡིན་ནའོ། །
--- END BLOCKS ---
