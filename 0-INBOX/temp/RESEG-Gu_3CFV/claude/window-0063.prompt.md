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
གཞན་གྱིས་ནི་དེ་དག་ངེས་པར་སྦྱར་བ་གཅིག་གམ་དུ་མར་བྱས་པ་ལ་ལྷག་མ་སྒྲུབ་པར་བྱེད་ཅིང་ཉེས་བྱས་སོ་ཞེས་བྱ་བའོ། །

[Block 2207]
ཁང་པའམ་གཙུག་ལག་ཁང་དང་གདིང་བ་རྣམས་ལས་བརྩམས་པ་མཐར་བྱས་པ་ལ་ན་སྨད་པའི་ཚིག་གིས་རིག་པར་བྱའོ། །

[Block 2208]
ཅི་སླར་རྐང་པ་དེ་དག་གི་ཚད་གང་ཡིན་པ་གང་གིས་བྱེད་དམ་བྱེད་དུ་བཅུག་པ་ལ་ལྟུང་བྱེད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེ་དག་གི་ཆད་ནི་བུ་གར་གཞུག་པའི་ཕྱོགས་མ་གཏོགས་པར་ཁྲུ་གང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུ་གར་གཞུག་པ་ཞེས་བྱ་བའི་ཕྱོགས་དག་མ་གཏོགས་པར་ལྷག་མ་འདི་རྣམས་ཀྱི་ཚད་ཁྲུ་གང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2209]
གལ་ཏེ་གང་ཡོད་ན་འདི་ལ་གང་ཡོད་པར་གྱུར་ན་འདི་གལ་ཏེ་གང་ལས་གཏོགས་པའི་ཕྱོགས་ལས་བརྩམས་ཏེ། ཆ་ཕྱེད་ལ་བུ་གར་གཞུག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2210]
ཁྲུ་ཅི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་བདེ་བར་གཤེགས་པའི་སུམ་ཆས་སོ་ཞེས་བྱ་བ༌[^1398]སྨོས་ཏེ། བདེ་བར་གཤེགས་པའི་ཁྲུའི་སུམ་ཆར་གྱུར་པས་ཀྱང་ངོ་། །བསླབ་པའི་གཞི་རྣམས་ལ་བདེ་བར་གཤེགས་པའི་ཁྲུ་ཆ་གསུམ་དུ་གྱུར་པའི་ཁྲུ་ཚད་ཀྱི་རྣམ་པར་གཞག་པ་དེ་བས་ན་འདི་ལྟར་འདི་ལ་དེ་རྣམས་ལ་འབྲེལ་པ༌[^1399]རྣམ་པར་གཞག་པས་རྟོགས་པའོ། །

[Block 2211]
འོག་མ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བསླབ་པའི་གཞི་འོག་མ་ཤིང་བལ་གྱིས་གོས་པར་བྱ་བ་དང་བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ཀྱི་ཚད་ལས་གྱུར་པ་ཞེས་བྱ་བའི་བསླབ་པའི་གཞི་ལ་ཚད་མངོན་པར་བསྟན་པས་བར་མ་གསུམ་ལ་འདིའི་སྐབས༌[^1400]ཡིན་ནོ་ཞེས་བྱ་བ་རྣམ་པར་གཞག་པའོ། །

[Block 2212]
རང་གི་ལུས་ཀྱི་ཚད་དང་རྗེས་སུ་མཐུན་པར་གདིང་བ་ལས་གྱུར་པ་དང་། གཡན་པ་དགབ་པ་ལས་གྱུར་པ་དང་། དབྱར་གྱི་རས་ཆེན་ལས་གྱུར་པ་རྣམས་ལ་ཚད་ཀྱི་ཆོས་གོས་བཞིན་དུ་རྣམ་པར་གཞག་པར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2213]
དེའི་ཕྱིར་བར་མ་དང་རྗེས་སུ་མཐུན་པར་བདེ་བར་གཤེགས་པའི་ཚད་ཀྱི་རྗེས་སུ་འགྲོ་བས་གང་ཟག་གི༌[^1401]དབང་དུ་བྱས་ཏེ། བདེ་བར་གཤེགས་པའི་ཚད་ལ་སོགས་པར་བརྟེན་པ་ནི༌[^1402]རྟོགས་པར་བྱའོ། །

[Block 2214]
ཁྲིའི་རྐང་པ་འཆོས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 2215]
[^1403]

[Block 2216]
གང་ལ་ཤིང་བལ་གྱིས་གོས་པར་བྱ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཤིང་བལ་གྱིས་གོས་པར་བྱས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་འདུན་གྱི་ཁྲིའམ་ཁྲིའུ་དག་ལ་ཞེས་བྱ་བ་ནི་གོང་དུ་བསྟན་ཟིན་ཏོ། །

[Block 2217]
ཅི་རང་ཉིད་ཀྱིས་གོས་པར་བྱས་པ་ལའམ་ཞེ་ན། དེའི་ཕྱིར་རང་ངམ་བསྐོས་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2218]
འདིར་ཤིང་བལ་ཇི་ལྟ་བུ་ཡིན་པར་རིག་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཤིང་བལ་ནི་ལྔ་སྟེ། ཤམ་ལའི༌[^1404]དང་། ཨརྐའི་དང་། ཀ་ཤའི༌[^1405]དང་། སྤྲ༌[^1406]བའི་དང་། ཨེར་ཀའི་འོ༌[^1407]ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ནི་འདྲེས་པས་ཉམས་པར་བྱེད་པ་སྟེ། ཚིག་དེ་དག་ནི་གོས་དང་ལུས་མ་རུངས་པར་གྱུར་པ་དགག་པའི་ཕྱིར་རོ། །

[Block 2219]
ཤིང་བལ་གྱིས་གོས་པར་བྱས་པའི་ལྟུང་བྱེད་དོ། །

[Block 2220]
ཚད་ལས་ལྷག་པར་བྱེད་དམ་བྱེད་དུ་འཇུག་ན་རྐང་པའི་བསླབ་པའི་གཞི་ལས་བསླབ་པའི་གཞི་གསུམ་པ་ཞེས་བྱ་བར་བརྗོད་དོ། །

[Block 2221]
དེ་ལ་གང་གིས་ཞེས་བྱ་བ་ལྟོས་པ༌[^1408]ལ་བརྗོད་པར་བྱ་སྟེ་གདིང་བའིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ཚད་གང་ཞེ་ན། དེའི་ཕྱིར་འདིའི་ཚད་ནི་སྲིད་དུ་ཁྲུ་གསུམ་མོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2222]
མི་ཆོག་ན་ཁྲུ་ཕྱེད་དང་དོ་མན་ཆད་བཀྱེད༌[^1409]དོ་ཞེས་བྱ་བ་ནི་གང་ལ་ཁྲུ་གསུམ་གྱིས་མི་ཆོག་པ་དེས་ཇི་ཙམ་བཀྱེད་པས༌[^1410]དོན་འགྲུབ་པ་དེ་ཙམ་བཀྱེད་པར༌[^1411]བྱ་སྟེ། ཁྲུ་ཕྱེད་དང་དོ་མན་ཆད་བཀྱེད་པར༌[^1412]བྱའོ། །

[Block 2223]
ཆེན་པོ་དང་བར་མ་དང་ཁྲུ་ཕྱེད་ལས་བསྒྲུབ་པར་མི༌[^1413]བྱ་བའི་དོན་ཏོ། །

[Block 2224]
འདིའི་ཞེང་དུ་ནི་ཁྲུ་དོ་དང་སོར་དྲུག་གོ་ཞེས་བྱ་བ་ནི་འདིའི་ཚད་ཅེས༌[^1414]བྱ་བ་དང་སྦྱར་རོ། །

[Block 2225]
དེ་ཆུང་ངུ་ལ་བྱིན་གྱིས་རློབ་ན་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་གདིང་བ་དེའོ། །

[Block 2226]
འོག་མ་གཉིས་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གཡན་པ་དགབ་པ་ལས་གྱུར་པ་དང་། དབྱར་གྱི་རས་ཆེན་ལས་གྱུར་པ་ཞེས་བྱ་བ་གཉིས་ལ་ཡང་ཚད་པས་ཆུང་བ་ལ་བྱིན་གྱིས་བརླབས་པ་ལ་ཉེས་བྱས་སུ་འགྱུར་བའོ། །

[Block 2227]
བྲམ་ཟེའི་བུ་མོ་ལས་མདོ་གཉིས་པོ་འདི་ཡིན་ཏེ། འོག་མ་གཉིས་ལ་དེར་ཚིག་སྦྱར་ཏེ། དབྱར་གྱི་རས་ཆེན་ཆུང་ངུ་ལ་བྱིན་གྱིས་རློབ་ན་ཉེས་བྱས་སོ། །

[Block 2228]
དེ་བཞིན་དུ་གཡན་པ་དགབ་པ་ཡང་དེ་དང་འདྲའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེའི་རྗེས་སུ་འབྲང་བས་གདིང་བ་ལ་ཡང་དེ་སྐད་ཅེས་སྨྲས་སོ།[^1415] །གཞན་འདི་ཚད༌[^1416]ལས་འདས་པའི་རྣམ་པར་གཞག་པ༌[^1417]ནི་ཉེས་བྱས་འདི་གཞན་དུ་རིག་པར་བྱ་སྟེ། འདིར་གཏོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2229]
གདིང་བ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དོ། །

[Block 2230]
[^1418]

[Block 2231]
ཚད་ལས་ལྷག་པར་བྱེད་དམ་བྱེད་དུ་འཇུག་པ་ལ་ལྟུང་བྱེད་བཞི་པ་གང་ཡིན་པ་བརྗོད་པ། དེ་ལ་གང་གིས་ཞེས་བྱ་བ་ལ་ལྟོས་ནས་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་གཡན་པ་དགབ་པའི་འོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2232]
དེའི་ཚད་ཇི་ཙམ་ཞེ་ན། དེའི་ཕྱིར་ཁྲུ་དྲུག་དང་གསུམ་མོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྲིད་དུ་ནི་ཁྲུ་དྲུག་གོ། །

[Block 2233]
ཞེང་དུ་ནི་གསུམ་མོ། །

[Block 2234]
གཡན་པ་དགབ་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དོ། །

[Block 2235]
ལྔ་པ་གང་གིས་ཚད་ལས་ལྷག་པར་བྱེད་དམ་བྱེད༌[^1419]དུ་འཇུག་ན་ལྟུང་བྱེད་དོ། །

[Block 2236]
དེ་ལ་གང་ཞིག་ཞེས་བྱ་བ་འདི་ལ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དབྱར་གྱི་རས་ཆེན་གྱིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ཚད་ཇི་ཙམ་ཞེ་ན། དེའི་ཕྱིར་དགུ་དང་གསུམ་དང་སོར་བཅོ་བརྒྱད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྲུ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2237]
སྲིད་དུ་ནི་ཁྲུ་དགུའོ། །

[Block 2238]
ཞེང་དུ་ནི་ཁྲུ་གསུམ་དང་སོར་བཅོ་བརྒྱད་དོ། །

[Block 2239]
དབྱར་གྱི་རས་ཆེན་ལས་གྱུར་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 2240]
སྟོན་པ་རང་གི་ཁྲུ་ལྔ་དང་གསུམ་པའི་ཆོས་གོས་སོ་ཞེས་བྱ་བ་ནི་གང་དུ་བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ཀྱི་ཚད་ལས་གྱུར་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དེའི་ལུས་ཙམ་མེད་པར་དེའི་ཚད་དམ་ལྷག་པའི་ཆོས་གོས་བྱེད་དམ་བྱེད་དུ་འཇུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ཀྱི་ཚད་དམ། དེ་ལས་ལྷག་པར་བྱེད་དམ་བྱེད་དུ་བཅུག་པ་ལའོ། །

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
--- END BLOCKS ---
