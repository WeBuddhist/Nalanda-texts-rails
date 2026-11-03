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
འདིར་མདོ་སྔ་མ་དང་འདི་གཉིས་ཀྱི་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་རེ་ཞིག་དགེ་སློང་གི་ཀུན་དགའ་ར་བའི་ཕྱི་རོལ་དུ་རང་གི་ལག་པས་བཅའ་བ་དང་བཟའ་བ་བླངས་ཏེ་འཚལ་བར་བགྱིད་ཅིང་། ཆོམ་རྐུན་པ་དག་ཀྱང་སླར་བཟློག་པར་བགྱིད། སྦྱིན་པ་པོ་དང་སྦྱིན་བདག་ཀྱང་བདེ་བར་ཀུན་དགའ་ར་བར་འཇུག་པར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ་ཞེས་བྱ་བ་གསུངས་པ་ནི་མདོ་སྔ་མའི་གཞུང་ཡིན་ནོ། །

[Block 2347]
བཤུལ་གྱི་ཕྱེད་དུ་མཆིས་ཏེ་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 2348]
འཇིགས་པ་དང་བཅས་པའི་གནས་ལས་གཞན་དུ་གྱུར་པ་ཉིད་དུ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་ནི་ཟ་བ་ལ་ཡང་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བའི་རྗེས་སུ༌[^1483]བསྙགས་པའི་ཕྱིར་སྨོས་སོ། །

[Block 2349]
སོ་སོར་བཤགས་པར་བྱ་བ་གསུམ་པོ་རྣམས་ལ་ཡང་རང་གིས་ཤེས་པ་མ་སྨོས་པས་སྤྲིང་ཡིག་ལ་སོགས་པ་དང་མངགས་པས་བླངས་པ་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 2350]
ནགས་བརྟག༌[^1484]པ་ལས་གྱུར་པའི་སོ་སོར་བཤགས་པར་བྱ་བ་སྟེ་བཞི་པའོ། །

[Block 2351]
སོ་སོར་བཤགས་པ་རྣམས་རྫོགས་སོ།། །།

[Block 2352 [HEADING]]
## དགེ་སློང་གི་རྣམ་པར་འབྱེད་པ། ^3-0

[Block 2353]
ཤམ་ཐབས་ཅི་ནས་ཀྱང་ཟླུམ་པོར་འདུག་པར་འགྱུར་བ་དེ་ལྟར་བགོ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། འདུག་པ་ཞེས་བྱ་བ་ནི་མཉམ་པར་འདུག་པའོ། །

[Block 2354]
ཧ་ཅང་རྩེངས་པ་མ་ཡིན་པར་ཡང་ངོ་། །ཧ་ཅང་འཇོལ་བ་མ་ཡིན་པར་རོ་ཞེས་བྱ་བ་ནི་ཟླུམ་པོར་ཞེས་བྱ་བ་འདི་ལ་མ་བསམས་པར་གྱུར་པ་འདི་མཆོག་ཏུ་གྱུར་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གཞན་དང་འབྲེལ་པ་ཞེས་བྱ་བའི་དོན་འདི་ཤེས་པར་བྱ་བའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 2355]
གྲྭ་གླང་པོ་ཆེའི་སྣ་ལྟར་ནར་བ་མ་ཡིན་པར་རོ་ཞེས་བྱ་བ་ལ། གྲྭ་ཞེས་བྱ་བ་ནི་ཕྱོགས་གཅིག་སྟེ་འོག་མ་ལ་ཡང་འདི་དང་འབྲེལ་བར་རིག་པར་བྱའོ། །

[Block 2356]
གླང་པོ་ཆེའི་སྣ་ལྟར་ཞེས་བྱ་བ་འདི་ལ་འདིར་ཁ་ཚར་དང་ཕུན་ཚར་གྱི་མཐའ་མ་བཅད་པའི་གྲྭ་དག་ལ་ཤིན་ཏུ་འབྱུང་བའོ། །

[Block 2357]
གོང་དུ་མ་ལྟེབས་པར༌[^1485]རོ་ཞེས་བྱ་བ་ནི་ལྟེ་བའི་གོང་རོལ་དུ་ལྟེབས་ཤིང༌[^1486]གནས་པའོ། །

[Block 2358]
སྦྲུལ་མགོའི་གདེངས་ཀ་ལྟར་ཕྱིར་བྱུང་བ་མ་ཡིན་པར་རོ་ཞེས་བྱ་བའི་རྣམ་པ་འདི༌[^1487]ནི་མདུན་གྱི་ནང་ན༌[^1488]འབྲེལ་པའི་རིམ་པ་ལ་གོང་དུ་མ་ལྟེབས་པར༌[^1489]རོ་ཞེས་བྱ་བའི་རྣམ་པ་འདི་དག་རིག་པར་བྱའོ། །

[Block 2359]
ཕུར་མ་ལྟར་འདུག་པ་མ་ཡིན་པར་རོ་ཞེས་བྱ་བ་ནི། འདི་ནི་སྟེང་གི་ཁ་ལོགས་ན་གནས་པའི་རྣམ་པ་ཡིན་གྱི། གློ་ནས་ཕྱི་རོལ་གྱི་རིམ་པ་དང་འབྲེལ་པ་ནི་མ་ཡིན་པའོ། །

[Block 2360]
ཆོས་གོས་ཅི་ནས་ཀྱང༌[^1490]

[Block 2361]
དང་པོ་གསུམ་ལྟར་འགྱུར་བ་དེ་ལྟར་བགོ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། ཆོས་གོས་ཞེས་བྱ་བ་ནི་བླ་གོས་དང་སྣམ་སྦྱར་རོ། །

[Block 2362]
ཤམ་ཐབས་བྱིན་གྱིས་བརླབས་པ་ལ་སོགས་པ་དག་ལ་ཡང་རྣམ་པ་འདི་དག་རིག་པར་བྱའོ། །

[Block 2363]
དང་པོ་གསུམ་ཞེས་བྱ་བ་ནི་ཟླུམ་པོར་འདུག་པ་དང་ཧ་ཅང་རྩེངས་པ་མ་ཡིན་པ་དང་། ཧ་ཅང་འཇོལ་བ་མ་ཡིན་པ་ཞེས་བྱ་བ་དེ་དག་གོ། །

[Block 2364]
ཤིན་ཏུ་བསྡམས་ཤིང་ཁྱིམ་གཞན་དུ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་རྣམ་པར་རབ་ཏུ་བརྟག་པ་ལ་ངེས་པར་སྦྱར་བ་སྟེ། ལེགས་པར་བགོས་ཤིང་ངོ་། །སྐྲ་བསྐྱུང་ཞིང་ངོ་། །མིག་གཡེང་བར་མི་བྱ་ཞིང་ངོ་། །གཉའ་ཤིང་གང༌[^1491]ཙམ་དུ་བལྟ་ཞིང་ངོ་ཞེས་བྱ་བ་ནི་མིག་གི་དབང་པོ་གཡེང་བར་མི་བྱ་ཞེས༌[^1492]བྱ་བའི་དོན་ཏོ། །

[Block 2365]
དེ་ལྟར་ཡོད་པར་འགྱུར་བ་མ་ངེས་པས་ཐམས་ཅད་དུ་བལྟ་བར་བྱ་བའམ་སྙམ་པའི་ཐལ་བ༌[^1493]སྤངས་པའི༌[^1494]ཕྱིར་གཉའ་ཤིང་གང་ཙམ་དུ་བལྟ་ཞིང་ངོ་། །མགོ་མི་གཡོགས་པའི༌[^1495]རྣམ་པས་སོ། །

[Block 2366]
མི་བརྫེ་བར༌[^1496]རོ་ཞེས་བྱ་བ་སྟེ། རྣམ་པས་སོ་ཞེས་བྱ་བ་ནས་བརྫེས་ཏེ་འགྲོ་བར་མི་བྱ་ཞེས༌[^1497]བྱ་བའི་དོན་དུ་སྦྱར་བར་བྱའོ། །

[Block 2367]
དེ་ལྟ་བས་ན་ཐ་མལ་པར་གནས་པ་ཆར་པ་ལ་སོགས་པའི་གནོད་པ་བྱུང་ཡང་ཤམ་ཐབས་དང་ཆོས་གོས་བརྫེས་ཏེ་འགྲོ་བར་མི་བྱ་སྟེ། སྲོག་གི་བར་ཆད་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 2368]
མཉམ་པའི་གནས་སྐབས་སུ་ཤིན་ཏུ་མཆོག་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ཉིད་ཀྱིས་གྲུབ་པའི་ཕྱིར་མི༌[^1498]གཟར་བར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སོ་སོར་གཟར་ཏེ་སྟེང་དུ་བགོས་ཏེ་གཟར་བ་ནི་ཆོས་གོས་ཀྱི་དངོས་པོའོ། །

[Block 2369]
དགེ་སློང་དག་ལ་ནི་ཕྲག་པ་གཡོན་པར་གཟར་བ་ཉིད་ཡིན་ལ། གང་ཞིག་དེ་རྣམས་ལ་ངོས་གཉིས་ཀར་སོར་བཅུ་གཉིས་ཀྱི་རྣམ་པ་ཉིད་ཀྱིས་མི་གཟར་བའོ། །

[Block 2370]
གཉའ་གོང་དུ་མི་བསྣོལ་བར་རོ་ཞེས་བྱ་བ་ནི་དལ་བའམ་ཤིན་ཏུ་མྱུར་བར་ལག་པ་བརྐྱང་ཞིང་གཉའ་བ་ལ་སོགས་པར་དཔུང་པའམ་ལག་ངར་གཞག་པས། གང་ཞིག་ཀུན་ནས་འདུག་པས་ལག་པ་ཕན་ཚུན་བསྣོལ་ཞིང་དེ་ལྟར་བྱས་ནས་ནི་མ་ཡིན་ནོ། །

[Block 2371]
ལྟག་པར་མི་བསྣོལ་བར་རོ་ཞེས་བྱ་བ་ནི་ལྟག་པའི་ཕྱོགས་སུ་ལག་པ་ཕན་ཚུན་ནས་སྤྲད་དེ་སོར་མོ་བསྣོལ་བ་ནི་ལྟག་པར་བསྣོལ་བ་ཞེས་བྱ་སྟེ། དེ་ལྟར་མི་བསྣོལ་བར་རོ། །

[Block 2372]
མི་བརྐྱང་བར་རོ་ཞེས་བྱ་བ་ནི་སྒྱིད་པ་གཉིས་ཀས་སམ། གཉིས་ཀས་མ་ཡིན་པས་བརྐྱང་བསྐུམ་བྱེད་ཅིང་འགྲོ་བར་མི་བྱའོ། །

[Block 2373]
མི་མཆོང་བར་རོ་ཞེས་བྱ་བ་ནི་མཆོང་ཞིང་མཆོང་ཞིང་འགྲོ་བར་མི་བྱའོ། །

[Block 2374]
ཙོག་པུས་མ་ཡིན་པར་རོ་ཞེས་བྱ་བ་ནི་ཙོག་པུས་འགྲོ་བར་མི་བྱའོ། །

[Block 2375]
བྲང་བས་མ་ཡིན་པར་རོ་ཞེས་བྱ་བ་ནི་བྲང་བས་འདིས་བྱས་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། བྲང་བས་བྱས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2376]
དཀུར་མི་བརྟེན་པར་རོ་ཞེས་བྱ་བ་ནི་ལག་པ་གཉིས་རྐེད་པའི་ཕྱོགས་སུ་བརྟེན་ཏེ་གྲུ་མོའི་ཕྱོགས་སུ་སྨྱུང་སྨྱུང་པོར་བྱས་ཏེ་འགྲོ་བར་མི་བྱའོ། །

[Block 2377]
ལུས་མི་བསྒྱུར་བར་རོ་ཞེས་བྱ་བ་ནི་གང་དུ་འགྲོ་བ་དེར་ལུས་བསྒྱུར་ཞིང་འགྲོ་བ་ནི་ལུས་བསྒྱུར་ཞིང་འགྲོ་བ་ཞེས་བྱ་སྟེ་དེ་ནི་བྱ་བའི་བྱེ་བྲག་ཡིན་པས་དེ་ལ་འབྲེལ་བ་དེ་འདིས་ནི་འོག་མ་དག་ཀྱང་བཤད་པའོ། །

[Block 2378]
ལག་པ་མི་ཀྱོག་པར་རོ། །

[Block 2379]
མགོ་མི་སྒྱུར་བར༌[^1499]རོ། །

[Block 2380]
ཕྲག་པ་མི་སྤྲད་པར་རོ་ཞེས་བྱ་བ་ནི་ཕྲག་པ་གཉིས༌[^1500]སྤྲད་པས་མ་ཡིན་ནོ། །

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
--- END BLOCKS ---
