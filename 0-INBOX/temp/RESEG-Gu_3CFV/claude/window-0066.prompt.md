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
[Block 2311]
འདི་ལ་རྒན་པ་མི་འཇུག་ན་གསར་བུས་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དྲི་བ་འདི་ལ་རྒན་པས་འཇུག་པར་བྱའོ། །

[Block 2312]
དེ་མི་འཇུག་ན་གསར་བུས་འཇུག་པར་བྱའོ། །

[Block 2313]
གྲལ་རིམས་སུ་མ་ཕེབས་པར་འདྲིམ་དུ་འཇུག་པ་མ་བཟློག་པར༌[^1458]ཟ་བའི་སོ་སོར་བཤགས་པར་བྱ་བ་སྟེ་གཉིས་པའོ།། །།

[Block 2314]
དད་པ་ཅན་གལ་ཏེ་བྱིན་ན་དེ་ཕོངས་པར༌[^1459]འགྱུར་བ་ལྟ་ན་ཁྱིམ་གྱི་བསླབ་པའི་སྡོམ་པ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དད་པ་ཅན་ཞེས་བྱ་བ་ནི་ཁྱིམ་བདག་སྟེ། དེ་ལ་ཁྱིམ་གྱི་བསླབ་པའི་སྡོམ་པ་སྦྱིན་པར༌[^1460]བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2315]
གལ་ཏེ་སྦྱིན་ན་ཕོངས༌[^1461]པར་གྱུར་པ་ལྟ་ན་ཞེས་བྱ་བ་ནི་གལ་ཏེ་སྦྱིན་པ་བྱིན་ན་དད་པ་ཅན་དེ་ཡོ་བྱད་རྣམས་ཀྱིས་ཕོངས་པར་འགྱུར་བ་ལྟ་ན་དེ་ནས་སྡོམ་པ་སྦྱིན་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2316]
འདིར་ཕལ་ཆེར་ཁས་བླངས་ཏེ་སྐྱེ་བའི་དབང་གིས༌[^1462]བསླབ་པ་རྣམས་བརྗོད།[^1463] འདིར་ཕལ་ཆེར་འཕགས་པ་ལ་སྦྱིན་པ་ལ་དད་པ་འཇུག་པར་བྱེད་པར་འགྱུར་བ་ཡིན་ཏེ། དེ་བས་ན་སོ་སོའི་སྐྱེ་བོ་ལ་ཡང་ཆོ་ག་འདི་ཡིན་ནོ། །

[Block 2317]
དད་པ་ཅན་བཟང་པོ་དེ་དགེ་བའི་བསམ་པ་དང་ལྡན་པ་དེ་ལ་ཅུང་ཟད་མི་སྟེར་བ་དང་མི་འདོར་བར་ཡོངས་སུ་འདོར་མི་ཕོད་པ་ཡོད་པ་ཡིན་ཏེ། སངས་རྒྱས་ལ་ཞེས་བྱ་བ་ལ་སོགས་པས་དད་པ་ཙམ་གྱིས་འབུལ་བ་ཁས་བླངས་པས་ཤིན་ཏུ་བདེ་བླག་ཏུ་ཡང་སོ་སོའི་སྐྱེ་བོ་ལ་བསྲུང་བར་བྱ་བ་ཉིད་དུ་རྣམ་པར་ངེས་ཏེ་འདིར་དད་པ་ཙམ་ཞེས་སྨོས་པས་སློབ་བཞིན་པའི་དད་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2318]
ཁྱིམ་གྱི་ཞེས་བྱ་བ་ལ་ཁྱིམ་ལ་ལྷག་པར་གནས་པའི་བསླབ་པ་ནི་ཁྱིམ་གྱི་བསླབ་པའོ། །

[Block 2319]
དེའི་སྡོམ་པ་ནི་སྡོམ་པར་གྱུར་ཅིང་ངེས་པ་ཡིན་པས་དགེ་སློང་རྣམས་ལ་སྡོམ་པ་དེ་སྦྱིན་པར་བྱའོ། །ཇི་ལྟར་འཇུག་ཅིང་སྦྱིན་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གསོལ་བས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གསོལ་བ་འབའ་ཞིག་གི༌[^1464]ལས་ཀྱིས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཇི་ལྟར་བག་ཡངས་སུ་བྱ་ཞེ་ན། དེའི་ཕྱིར་བག་ཡངས་སུ་བྱ་བ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ཡང་གསོལ་བ་འབའ་ཞིག་གི༌[^1465]ལས་ཀྱིས་བྱ་བའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2320]
བྱིན་པ་དེའི་སེམས་རྟོགས་ནས་ཁྱིམ་དུ་འགྲོ་བ་དང་། སྟན་ལ་འདུག་པ་དང་ཆོས་བསྟན་པ་དག་བྱའོ་ཞེས་བྱ་བ་ལ་བྱིན་པ་དེའི་ཞེས་བྱ་བ་ནི་གང་ལ་ཁྱིམ་གྱི་བསླབ་པའི་སྡོམ་པ་དེ་བྱིན་པ་དེ་ནི་བྱིན་པ་དེ་ཞེས་བྱ་བ་སྟེ་དེའི་སེམས་རྟོགས་པས་སོ། །

[Block 2321]
ལྷུང་བཟེད་སྟོང་པས་འཇུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། བསླབ་པའི་སྡོམ་པ་བྱིན་པའི་ཁྱིམ་དུ་འཇུག་པར་མི་བྱའོ། །

[Block 2322]
དེའི་བྱིས་པ༌[^1466]སློང་བ་དག་ལ་བསོད་སྙོམ༌[^1467]ལས་སྣུམ་ཁུར་སྦྱིན་པར་བྱ་ཞིང་རིལ་གྱིས་ནི་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། རིལ་པོ་དང་རིལ་པོ་མ་ཡིན་པ་ཞེས་བྱ་བའི་ཁྱད་པར་མ་བརྗོད་པས་ཐལ་ཆེས་པ་ལ༌[^1468]རིལ་པོ༌[^1469]མ་ཡིན་པ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2323]
གང་དུ་ཁྱིམ་གྱི་བསླབ་པའི་སྡོམ་པ་འདི་ལ་བག་ཡངས་སུ་བྱའམ་ཞེ་ན། དེའི་ཕྱིར་འདོད་ན་བག་ཡངས་སུ་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་དད་པ་ཅན་དེ་བག་ཡངས་སུ་བྱ་བ་དེ་འདོད་པར་གྱུར་ན་དེའི་ཚེ་དེ་ལ་ཁྱིམ་གྱི་བསླབ་པའི་སྡོམ་པ་དེ་བག་ཡངས་སུ་བྱ་ཞིང་གཞིག་པར་བྱའོ། །

[Block 2324]
གང་ལ་བསླབ་པ་དྲལ་ཏེ་ཁྱིམ་དུ་འཇུག་པའི་སོ་སོར་བཤགས་པར་བྱ་བ་འབྱུང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དེའི་སྦྱིན་པའི་མདུན་དུ་མགྲོན་དུ་མ་བོས་པས། བསླབ་པའི་སྡོམ་པ་སྦྱིན་པའི་ཁྱིམ་ནས་བཅའ་བ་དང་བཟའ་བ་དག་བླངས་ཤིང་ཟོས་པ་ལས་ཏེ། ག་གོན་དང་ལ་ཕུག་དང་ལྡམ་ལྡུམ་མོད་པ་དག་ནི་མ་གཏོགས་སོ༌[^1470]ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་སྲིད་དུ་གཅིག་ཏུ་སྦྱིན་པ་ཉིད་དེ་སྲིད་དུ་འདིར་ཁྱིམ་གཅིག་པ་ཉིད་དོ། །

[Block 2325]
འདིར་ཁྱིམ་ནི་མཚོན་པ་ཙམ་ཡིན་ཏེ། ཡོངས་སུ་གཟུང་བ༌[^1471]མེད་པར་དགེ་སློང་ལ་སོགས་པས༌[^1472]སློབ་མ་ལ་སོགས་པ་གསོ་བར༌[^1473]བྱེད་པ་ལ་ཆོ་ག་འདི་ཡིན་ནོ། །

[Block 2326]
བསླབ་པའི་སྡོམ་པ་སྦྱིན་པའི་རིགས་པས་གཟུང༌[^1474]སྟེ། བཅའ་བར་བྱ་བ་དག་ཟ་བར་བྱེད་ན་ཞེས་བྱ་བ་དེ་ལྟར་འདི་འབྲེལ་པའོ། །

[Block 2327]
ཅི་འདི་ཐམས་ཅད་ལ་བཤགས་པར་བྱའོ་ཞེས་བྱ་བ་འདི༌[^1475]ལ་སྦྱིན་པའི་སྔ་རོལ་དུ་སྤྱན་མ་དྲངས་པ་ཞེས་བྱ་བའི་ཐ༌[^1476]ཚིག་གོ། །

[Block 2328]
བསླབ་པའི་སྦྱིན་པ་ལས་སྔ་རོལ་དུ་སྤྱན་དྲངས་པ་ལ་བསླབ་པ་བྱིན་ནས་ཟ་བར་བྱེད་པ་ལ་ལྟུང་བ་མེད་དོ། །ཅི་བཅའ་བར་བྱ་བ་ཐམས་ཅད་ཟ་བར་བྱེད་པ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ག་གོན་དང་ལ་ཕུག་དང་ལྡམ་ལྡུམ་མོད་པ་དག་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་རྣམས་ཟ་བར་བྱེད་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 2329]
འདི་ནི་ཧ་ཅང་ཡང་འདོད་པ་ཆེ་བ་ཡིན་ཏེ་གང་ཞིག་ཁྱད་པར་ཅན་གྱི་བསླབ་པ་ཉམས་པར་བྱས་ནས་འཇུག་པ་ཞེས་བྱ་བ་སྨོས་པ་ནི་ལྟུང་བ་རྣམ་པར་གཞག་པའོ། །

[Block 2330]
བསླབ་པ་དྲལ་ཏེ་ཁྱིམ་དུ་འཇུག་པའི་སོ་སོར་བཤགས་པར་བྱ་བ་སྟེ་གསུམ་པའོ།། །།

[Block 2331]
ནགས་ཉུལ་བའི་དགེ་སློང་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་གཞན་ལ་ཡིད་ཆེས་པར་བྱ་བ་མ་ཡིན་ཏེ། དེ་བས་ན་དགེ་སློང་ལ་འདི་ལྟར་བརྟེན་པའོ། །

[Block 2332]
དེ་གང་གི་ཕྱིར་བསྐོ་བ་དེའི་ལས་བསྟན་པའི་ཕྱིར་དེས་དཔག་ཚད་ཕྱེད་ཁོ་ར་ཁོར་ཡུག་ཏུ་བརྟག་པར་བྱའོ། །

[Block 2333]
འཇིགས་པ་དང་བཅས་པ་ཉིད་ཡིན་ན་དུད་བརྡ་བཏུལ་བར་བྱའོ། །

[Block 2334]
བ་དན་སྔོན་པོ་བསྒྲེང་བར་བྱའོ། །

[Block 2335]
འདབ་མའི་ཆང་བུ་ལམ་ཀར་གཞག་པར་བྱའོ། །

[Block 2336]
གཞན་དུ་ན་དཀར་པོ་དག་གོ། །

[Block 2337]
འདོད་པ་ཉིད་ཡིན་ན་ནི་དེ་ལ་ཁྱེའུ་སུས་དང་གྲོགས་དག་ཀྱང་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ནགས་ཉུལ་བ་དོན་དུ་གཉེར་བ་ཡོད་པར་གྱུར་ན་སྦྱིན་པར་བྱའོ། །ཤེས་གཙོའོ༌[^1477]ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །གང་ལ་འདུ་ཤེས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ནགས་མ་ཉུལ་བ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རེ་ཞིག་བདག་གི་དོན་ནི་གྲུབ་ཟིན་གྱི། དགེ་འདུན་གྱི་དང་སྦྱིན་པ་པོའི་གནོད་པ་བསྲུང་བ་འདིས་ཁོ་བོ་ལ་ཅི་ཞིག་བྱ༌[^1478]ཞེས་བྱ་བ་བདག་ཉིད་བཀང་བ་ཙམ་གྱིས་ཆོག་པར་འཛིན་ཅིང་འཇིགས་པ་དང་བཅས་པའི་གནས་སུ་ཟས་བླངས་ཏེ་ཟ་བ་ལ་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་རོ། །

[Block 2338]
དེ་ལྟར་ཡང་གཞུང་ནི་དགེ་འདུན་གྱི་དགོན་པའི་གནས་དོགས་པ་དང་བཅས་པར་གྲགས་པ། འཇིགས་པ་དང་བཅས་པར་གྲགས་པ། འཇིགས་པ་ཐ་དད་པས་འཇིགས་སུ་རུང་བ་དང་བཅས་པར་གྲགས་པ་ཞིག་ཏུ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2339]
དེ་བཞིན་དུ་བསྲུང་བ་བསྒྲུབ་པ་དང་།

[Block 2340]
འཇིགས་པའི་གནས་གཞན་ལ་འཇུག་པར་གྱུར་པ་ཉིད་ལ་ན་སྨད་པར་བརྗོད་པ་དེ་བས་ན་འཇིགས་པ་དང་བྲལ་བ་ཉིད་ཀྱིས་མ་ལུས་པར་ཤེས་པ་ཉིད་ལས།

[Block 2341]
འདིར་ནགས་ལ་ཞེས་བྱ་བ་འདིའི་དོན་རྟོགས་པར་བྱའོ། །

[Block 2342]
དགོན་པར་གྱུར་པ་ཉིད་ཙམ་ལས་དགོངས་ཏེ་གསུངས་པ་ཡིན་གྱི་ཤིང་ལྗོན་པའི་ཚོགས་ཐིབས་པོ་འབའ་ཞིག་ལ་མི་བྱའོ། །

[Block 2343]
འཇུག་པ་གང་ལ་འདི་བྱེད་པ་པོ་ཡིན་ཞེ་ན། ཀུན་དགའ་ར་བའི་ཕྱི་རོལ་གྱི་དགོན་པར་བཅའ་བ་དང་བཟའ་བ་བླངས་ཏེ་ཟོས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགོན་པ་ནས་རྒྱང་གྲགས་ཀྱི༌[^1479]མཐའ་གང་ཡིན་པ་དེ་ནི་གྲོང་དང་ཀུན་དགའ་ར་བ་ལ་སོགས་པ་དགེ་སློང་རྣམས་ཀྱི་སྤྱིལ་པོའི་གནས་སོ། །

[Block 2344]
དེའི་ཕྱི་རོལ་དུ་བཅའ་བར་བྱ་བ་དང་བཟའ་བར་བྱ་བ་དག་སོ་སོར་བླངས་ཏེ། གང་ཡང་རུང་བར༌[^1480]དེ་དག་ཟོས་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2345]
བསྲུང་བ་བསྒྲུབས་ན་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི། འཇིགས་པ་མེད་པ་ཉིད་དུ་བྱུལ་བས་དགོན་པའི་བསྲུང་བ་བསྒྲུབས་པར་གྱུར་པ༌[^1481]དེའི་ཚེ་བཅའ་བ་དང་། བཟའ་བ་དག་ཟོས་ན་ཕྱེད་ཉིད་དེ་མ་ཆོག་པས་ཉེས་བྱས་བྱེད་པ་ཉིད༌[^1482]ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

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
--- END BLOCKS ---
