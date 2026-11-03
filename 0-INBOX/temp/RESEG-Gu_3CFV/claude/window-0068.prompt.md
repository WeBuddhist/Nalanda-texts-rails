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
[Block 2381]
ལག་པ་མི་སྒྲེལ་བར་རོ་ཞེས་བྱ་བ་ནི་ལག་པ་སྦྲེལ་བ་བཀག་པ་མ་སྦྲེལ་བའི་རྣམ་པས་གང་ཞིག་སྦྲེལ་བ་ཞེས་བྱ་བར་རྟོགས་པའོ། །

[Block 2382]
ཁྱིམ་གཞན་དུ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ལེགས་པར་བགོས་ཤིང་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིའི་མཐར་ཐུག་པར་སྦྱར་བར་བྱའོ། །

[Block 2383]
དེར་མ་བསྒོ་བར་སྟན་ལ་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་དེར་ཞེས༌[^1501]བྱ་བ་ནི་ཁྱིམ་གྱི་ནང་དུའོ། །

[Block 2384]
སྟན་ལ་མ་བརྟགས༌[^1502]པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདུག་པར་མི་བྱའོ། །

[Block 2385]
ལུས་ཐམས་ཅད་ཀྱི་ལྗིད་ཀྱིས་མི་དབབ༌[^1503]པར་རོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་གཞན་དེ་སྟན་ལ་ཟོན་ཡོད་པར་དལ་བུས་ལུས་ཕབ་སྟེ་འདུག་པར་བྱའི། གྱ་ཚོམ་དུ་ལུས་ཐམས་ཅད་ཀྱི་ལྗིད༌[^1504]ཀྱིས་ཕབ་སྟེ་ཁྲིག་ཅེས༌[^1505]བྱ་བར་འདུག་པར་མི་བྱ་སྟེ། གང་གི་ཕྱིར་དལ་བུ་དལ་བུས་སྟན་ལ་འདུག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2386]
རྐང་པ་མི་བསྣོལ་བར་རོ། །

[Block 2387]
བརླ་མི་བསྣོལ་བར་རོ། །

[Block 2388]
ལོང་བུའི་སྟེང་དུ་ལོང་བུ་མི་གཞག་པར་རོ་ཞེས་བྱ་བ་ལ། མི༌[^1506]བསྣོལ་བར་རོ་ཞེས་བྱ་བ་འདི་གཉིས་ཀ་ལ་སྦྱར་བར་བྱའོ། །

[Block 2389]
རྐང་པ་མི་དགུག་པར་རོ། །

[Block 2390]
རྐང་པ་མི་གདང་བར་རོ། །

[Block 2391]
མདོམས༌[^1507]མི་སྣང་བར་རོ་ཞེས་བྱ་བ་འདིས་ནི་བརླ་གཉིས་སམ་བྱིན་པ་གཉིས་སམ་རྐང་པ་གཉིས༌[^1508]སམ་ཡང་ན་ཐམས་ཅད་ཀྱང་རུང་སྟེ། ཐད་ཀར་གདངས་ཏེ་འདུག་པར་མི་བྱ་བ་བསྟན་ཏོ། །

[Block 2392]
ལག་པ་འགྲམ་པ་ལ་བརྟེན་ཏེ༌[^1509]མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས་རྣམ་པ་འདི་ལ་རྣམ་འབྱེད་དུ་གྱུར་པ་དང་མདོར་གྱུར་པའི་གཞུང་མཐོང་བར༌[^1510]ཡིན་ནོ། །

[Block 2393]
སྟན་ཐབས་བསྐུར་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྟན་གང་ལ་འདུག་འདུག་པ་དེ་རྒྱབ་ཀྱིས་ཁུར་ཞིང་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་དེ་འདི་ཡང་དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས་སོ། །

[Block 2394]
ཐམས་ཅད་དུ་ལེགས་པར་ཟས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གྲོང་ཁྱེར་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་འོན་ཀྱང༌[^1511]འདི་ནི་གཞན་འོག་མ་རྣམས་ཐམས་ཅད་ལ་སློབ་པ༌[^1512]རྣམས་ཀྱི་དབང་དུ་བྱས་པ་ཡིན་ནོ། །

[Block 2395]
བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དོན་ལ་ཡང་བསླབ་པ་ནི་འདི་ཡིན་ནོ། །

[Block 2396]
དེ་ལྟ་བས་ན་གཞན་གྱི་དོན་ཅན་གྱི་ཚིག་གིས་བསྟན་པའོ། །

[Block 2397]
མུ་དང་ཁ་ད་ཆད་དུ་མ་ཡིན་པར་རོ་ཞེས་བྱ་བ་ལ་མུ་ཞེས་བྱ་བའི་སྒྲ་ནི་ཁ་ལོགས་ཀྱི་མུ་ལ་བྱ་སྟེ། ཅི་ནས་ཀྱང་མུ་དང་ཁ་ད་ཆད་དུ་འགྱུར་བ་དེ་ལྟར་བླང་བར་མི་བྱ་སྟེ་འདི་ནི་འཇུག་པའི་ལམ་ཞེས་བྱ་བའི་འཇུག་པ་འདིས་སོ། །

[Block 2398]
ཇི་ལྟར་དེ་དང་མཉམ་པ་གཞན་འགྱུར་བ་དེ་ལྟར་བླང་བར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2399]
མ་ཆོག་པ་ཉིད་ཇི་སྙེད་པ་ཉིད་ལ་མ་ཆོག་པར་བཏགས་པ༌[^1513]དེ་སྙེད་པ་ཉིད་ནི་འདིར་ལྟུང་བ་མེད་པར་བྱས་པ་ཉིད་ལ་མཐར་ཐུག་པར་རིག་པར་བྱའོ། །

[Block 2400]
མཐེ་བོའི་ལྟོ་གང་གིས་མུ་ལ་རེག་པར་མི༌[^1514]བྱ་ཞེས་བྱ་བ་དང་འགལ་བར་འདི་ལྟར་ཤེས་པར་བྱ་བ་མ་ཡིན་ཏེ། དེ་ནི་དོན་ལ་ལྷུང་བཟེད་ཀྱི་ཚད་ལ་རིགས་པ་མ་ཡིན་པས་དེའི་ཕྱིར་ཚིག་འདིའོ། །

[Block 2401]
ཚོད་མ་དང་མཉམ་པ་མ་ཡིན་པར་རོ་ཞེས་བྱ་བ་ནི་བཟའ་བ་གང་ལ་ཚོད་མ་དང་མཉམ་པ་དེ་ནི་ཚོད་མ་དང་མཉམ་པ་སྟེ། དེ་ལྟར་བླང་བར་མི་བྱའོ། །

[Block 2402]
འདིར་ཚོད་མ་ཞེས་བྱ་བ་ནི་བྱ་ན་ཐམས་ཅད་ཀྱི་དཔེ་ཡིན་ནོ། །

[Block 2403]
ཚོད་མ་ཇི་ཙམ་གྱི་མུ་དང་ཁ་ད་ཆད་དུ་འགྱུར་བ་སྟེ། འདིར་དགག་པ་ནི་མ་ཡིན་ཏེ་དེ་བས་ན་ཚིག་འདིའོ། །

[Block 2404]
སྔ་མ་ཁོ་ནས་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་འདིར་ཐམས་ཅད་གྲུབ་ཅིང་སྨིན་པར་བཟའ་བར་བྱ་བ་ཐམས་ཅད་བསོད་སྙོམས་ཉིད་དུ་བསྟན་པ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2405]
དེའི་ཕྱིར༌[^1515]ལུས་དང་སྦྱར་བས་རང་ལ་དགོས་པའི་ཚད་ལས་ལྷག་པར་ཚོད་མ་ལེན་པ་དེ་བཀག་པ་ཡིན་ནོ། །

[Block 2406]
འདིར་ཚོད་མ་སྨོས་པ་ནི་མཚོན་པ་ཙམ་ཡིན༌[^1516]གྱི། ཚོད་མ་ལ་ཡང་རྣམ་པ་འདི་ཡིན་ཏེ། དེ་ལྟར་ཡང་འདིར་གཞུང་ནི་མ་མོ་ལས་ཇི་ཙམ་གྱིས་དེ་འཚོ་བར༌[^1517]གྱུར་པ་དེ་ལས་ལྷག་པར་ལེན་ཏམ༌[^1518]ཟ་ན་ཐ་ན་ཁམ་གཅིག་ཙམ༌[^1519]དུ་ཟིན་ཀྱང་དད་པས་སྦྱིན་པར་བྱ་བ་ཆུད་གསན་པར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2407]
མ་མོ་ལས་གང་གི་ཚེ་ཚོད་འཛིན་པར་མི་ནུས་སམ་ཕྱིར་བཟློག་པར༌[^1520]མི་ནུས་པས། ཡོན་བདག་གིས་ནན་གྱིས་བླུགས་པ་དང་རྗེས་སུ་སྙིང་བརྩེ་བས་ལེན་ན་དེའི་ཚེ་འབྲས་ཆན་ལ་སོགས་པ་ལྷག་པར་ལེན་ཅིང་གཞན་ནམ་སུ་ཡང་རུང་བ་ལ་སྦྱིན་ནོ་སྙམ་པ་དེ་ལ་ནི་ལྟུང་བ་མེད་པར་རིག་པར་བྱའོ། །

[Block 2408]
མཐར་ཆགས་སུའོ་ཞེས་བྱ་བ་ནི་སྟན་ལ་ཅི་ལྟར་འདུག་པའི་གྲལ་གྱི་རིམ་པ་བཞིན་དུ་ཟན་བླང་བར་བྱའོ། །

[Block 2409]
འདིར་རྒན་རིམས་སུ་བྱ་བ་ནི་མ་ཡིན་གྱི་དེ་བས་ན་ཇི་ལྟར་རྒན་རིམས་ཀྱིས་འདུག་པ་ལ་ཉེས་པ་འདི་མི་བསྐྱེད་པའོ། །

[Block 2410]
འདིར་ཉེས་དམིགས་འདི་ནི་མཉམ་པ་ཡིན་ཏེ། གང་དུ་ཐ་སྙད་འདིའོ། །

[Block 2411]
དེ་ནི་སྔོན་དྲུག་སྡེ་རྣམས་ཟན་ཟ་བ་ན་ཚོད་མ་འཕྲལ་དུ་བྲིམ་པ༌[^1521]མི་ནོད་པར་འོག་ཏུ་ཐག་རིང་དུ་ཐལ་བ་དང་འདོད་པས༌[^1522]བྲིམ་པ༌[^1523]འཁྲུགས་ཤིང་ལོང་ལོང་དུ་གྱུར་པའི་ཉེས་དམིགས་དེ་ལྟ་བུ་བསལ་བའི་ཕྱིར་རོ། །

[Block 2412]
ལྷུང་བཟེད་ལ་ལྟ༌[^1524]ཞིང་ངོ་ཞེས་བྱ་བ་ལ་འདིར་ལྷུང་བཟེད་ལ་བལྟ་བ་ཞེས་བྱ་བ་ནི་འདིར་ཡིད་ཀྱིས༌[^1525]བལྟ་བ་ལ་བྱའོ།[^1526] །མིག་གི༌[^1527]དབང་པོས་ནི་མ་ཡིན་ནོ། །

[Block 2413]
དེ་ལྟ་བས་ན་ལྷུང་བཟེད་དང་འབྲེལ་པའི་ཡིད་ཀྱིས་ཟས་ལེགས་པར་བླང་བར་བྱ་བ་ཡིན་གྱི། ཐ་སྙད་ལས་བྱུང་བ་ནི་གཉའ་ཤིང་གང་ཙམ་དུ་ལྟ་བའི༌[^1528]སྐབས་སུ་བཀག་ཟིན་ཏོ།[^1529] །བཅའ་བ་དང་བཟའ་བ་མ་འོངས་པར་ལྷུང་བཟེད་མི་བཟེད༌[^1530]པར་རོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་དོ། །

[Block 2414]
སྟེང་དུ་བཟུང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བཅའ་བ་དང་བཟའ་བ་ལ་ལྷུང་བཟེད་དོ། །

[Block 2415]
ལེགས་པར་ཟས་བཟའ་བར་བྱའོ། །

[Block 2416]
ཁམ་ཧ་ཅང་ཆུང་བར༌[^1531]མ་ཡིན་པར་རོ། །

[Block 2417]
ཁམ་ཧ་ཅང་ཆེ་བར་མ་ཡིན་པར་རོ་ཞེས་བྱ་བ་ལ། ཁམ་ཞེས་བྱ་བ་ནི་ཁར་ཁམ་ཚད་དུ་གཞུག་ཅིང་མིད་པར་བྱ་བའི་ཕྱིར་ཁམ་ཞེས་བྱ་བ་སྟེ་དེ་བས་ན་ཁམ་རན་པར་རོ། །

[Block 2418]
ཁམ་མ་གཟས༌[^1532]པར་ཁ་མི་གདང་ངོ་། །ཁ་ཁམ་གྱིས་བཀང་སྟེ་མི་སྨྲ་བར་བྱའོ། །

[Block 2419]
ཡང་འདོད་པའི་ཕྱིར་འབྲས་ཆན་གྱིས་ཚོད་མ་མི་དགབ༌[^1533]ཚོད་མས་འབྲས་ཆན༌[^1534]མི་དགབ་པར༌[^1535]རོ། །

[Block 2420]
ཙུག་ཙུག་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཙུག་ཙུག་ཟེར་ཞིང་ཟས་བཟའ་བར་མི་བྱའོ། །
--- END BLOCKS ---
