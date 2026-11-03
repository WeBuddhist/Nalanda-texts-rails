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
ཉི་མའི་འོད་ཀྱིས་ཞེས་བྱ་བ་དང་། བསྒྲགས་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2312]
ཁྱོད་ཀྱི་ཡོན་ཏན་ཆགས་པའི་གཏམ་དག་གིས། །ཞེས་བྱ་བ་ལ་ཆགས་པའི་གཏམ་གང་ཡིན་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར། ཁྱོད་ཀྱི་སྤྱོད་པ་ཞེས་ཚིགས་བཅད་བརྩམས་སོ། །ཇི་ལྟར་ཆགས་པའི་གཏམ་ཡིན་ཞེ་ན། ཆགས་པའི་གཏམ་ཉིད་དུ་ཚིགས་བཅད་ཕྱེད་འོག་མས་བསྟན་ཏོ། །

[Block 2313 [VERSE]]
ཁྱོད་ཀྱི་སྤྱོད་པ་མི་ལས༌[^1461]འདས། །
ཞེས་བྱ་བ་གང་ཡིན་ཞེ་ན།
ཚིགས་བཅད་ཕྱེད་འོག་མས་བསྟན་ཏོ། །

[Block 2314]
གནོད་སྦྱིན་དྲི་ཟ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^1462]གཤོལ་མདའ་འཛིན་ལ་སོགས་པའི་རི་དག་གི་བར་ན་གནས་པའོ། །

[Block 2315]
ལྟོས་འགྲོ་ཞེས་བྱ་བ་སྨོས་པས་ནི་སའི་འོག་ན་གནས་པ་པ་དང་། རྒྱ་མཚོ་ན་གནས་པ་གཟུང་ངོ་། །སུམ་ཅུ་རྩ༌[^1463]

[Block 2316]
གསུམ་པ་བརྒྱ་བྱིན་ཞེས་བྱ་བ་འདི༌[^1464]ནི་རི་རབ་ལ་གནས་པ་སྟེ། འདི་ལྟར་ལྷོ་ཕྱོགས་སུ་ཞེས་བྱ་བ་གང་སྔར་བསྟན་པ་སྟོན་པ་ཡིན་ནོ། །

[Block 2317 [VERSE]]
བུ་དང་བྲལ་བར་མ་སེམས་ཤིག །
ཅེས་བྱ་བ་ཅིའི་ཕྱིར་ཞེ་ན།
ཕ་ནི་བུ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2318]
རྒྱལ་སྲིད་ཉམས་པའི་མྱ་ངན་མ་བྱེད་ཅིག །ཅེས་བྱ་བ་ནི་གང་གི་ཕྱིར། ཁྱོད་ཀྱིས་མགོན་བྱས་དགོས་བཅས་རྒྱལ་སྲིད་ཅེས་བྱའོ། །

[Block 2319]
འདིར་ཁ་ཅིག་རྒོལ་ཏེ། བྲམ་ཟེ་ལ་ནི་བྱང་ཆུབ་སེམས་དཔའ་སྙིང་བརྩེ་བར་བྱེད་ལ། དམན་པས་ངུ་ཞིང་སྡུག་པའི་བུ་གཉིས་ཅིའི་ཕྱིར་གཏོང་ཞེས་གྲུབ་པའི་མཐའ་ཡོངས་སུ་མ་ཤེས་པ་ཉིད་རྒོལ་ལོ། །

[Block 2320]
དེས་མཆོད་པ་ནི་བདག་ཉིད་སྔོན་བྱང་ཆུབ་སེམས་དཔའི་དུས་སུ་བྱང་ཆུབ་སེམས་དཔས་དུས་གཅིག་ཏུ་ཚོགས་བསགས་པར་བྱའོ་ཞེས༌[^1465]འདི་ལྟར་དགོངས་པ་ཡིན་ཏེ། བདག་ཉིད་བཏང་བ་མ་ཡིན་པར་ཇི་ལྟར་ཚོགས་ཡོངས་སུ་རྫོགས་པར་འགྱུར། དེ་ལྟར་བྱང་ཆུབ་སེམས་དཔའ༌[^1466]ནི་ཚོགས་ཆེན་པོ་དེ་དག་ལས་སྐྱེས་པའོ། །

[Block 2321]
དེ་ལྟར་ན་ཅིའི་ཕྱིར་ངུ་བར་བྱེད་ཅེ་ན་ཆོས་ནི་གཉིས་ཏེ། དོན་དམ་པར་བསྟན་པ་དང་། ཀུན་རྫོབ་ཏུ་བསྟན་པའོ། །

[Block 2322]
འདི་ནི་ཀུན་རྫོབ་ཏུ་བསྟན་པ་སྟེ། ཉམ་ང་བ་དག་ཡིད་དང་བ་བསྐྱེད་པར༌[^1467]བྱ་བའི་ཕྱིར་རོ། །

[Block 2323]
སྐྱེས་པའི་རབས་འདི་ཉིད་དུ་ཡང་སློབ་དཔོན་གྱིས་བཤད་པ་སྦྱིན་པའི་གེགས༌[^1468]སུ་འགྱུར་དུ་མ་དོགས་ཤིག །འདི་ནི་ང་ཡི་ཆོས་སྤྱོད་གྲོགས་ཡིན་ནོ། །ཞེས་བྱ་བ་དང་། སྦྱིན་ལ་དགའ་བ་གོམས་བྱས་ཤིང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་མི་སྦྱིན་པར་མི་བྱ་བ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་རྩོད་པ་མེད་པ་ཉིད་དོ། །

[Block 2324]
སྤྱོད་པ་དེ་ལ་ཕྱོགས་པ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་དེ་ལ་སོགས་པའི་སེམས་ཅན་ལ་སྟེ། སྨོན་ལམ༌[^1469]བཏབ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2325]
བརྙས་པ་མི་བྱ་ཞེས་བྱ་བ་ནི་ཟིལ་གྱིས་གནོན་པར་མི་བྱ་བ་སྟེ། མོས་པ་སྤྱོད་པ་ལ་གནས་པ་ལའོ།[^1470] །གནོད་པ་མི་བྱ་བ་ནི་སར་ཆུད་པའི་སེམས་ཅན་གྱི་ཁྱད་པར་གྱི་ཡོན་ཏན་དང་ལྡན་པར་ཐོས་པས་དེ་ལ༌[^1471]མི་མོས་པར་མི་བྱའོ། །

[Block 2326]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་ཐམས་ཅད་སྒྲོལ་གྱི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 2327 [HEADING]]
## མཆོད་སྦྱིན་གྱི་སྐྱེས་པའི་རབས། ^10-0

[Block 2328]
རང་གི་བསོད་ནམས་ཀྱི་མཐུ་ཐོབ་པ་ཞེས་བྱ་བ་འདིས་ནི་སྐལ་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 2329]
རྒྱལ་ཕྲན་ཐམས་ཅད་ཕྱག་འཚལ་བ། །ཞེས་བྱ་བ་འདིས་ནི་སྤྲོ་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 2330]
བདག་དང་གཞན་གྱི་འཁོར་ལ་སོགས་པའི་གནོད་པ་རབ་ཏུ་ཞི་བས་འཚེ་བ༌[^1472]མེད་པ་ཞེས་བྱ་བ་འདིས་ནི་གསང་ཚིག་གི་ནུས་པ་བསྟན་ཏོ། །

[Block 2331]
གདུགས་ཟླ་མེད་པ་བགོ་སྐལ་གྱི་རིམ་པས་ཐོབ་པ་ཞེས་བྱ་བ་འདིས་ནི་གཙོ་བོའི་ནུས་པ་བསྟན་ཏོ། །

[Block 2332]
ཆོས་ཀྱི་དོན་གཅིག་ཏུ་སྦྱངས་པར་གྱུར་ཏེ། ཇི་ལྟ་བུ༌[^1473]ཞེ་ན། ཐུབ་པ་བཞིན་དུ་ཞེས་སྨོས་སོ། །ཇི་ལྟར་ཆོས་དོན་གཅིག་ཏུ་སྤྱོད་པ་ཡིན་ཞེ་ན། དངོས་པོ་ཀུན་གྱིས་འགྲོ་ལ་ཕན་བྱེད་པ། །ཞེས་སྨོས་ཏེ། དངོས་པོ་ཐམས་ཅད་ཀྱིས༌[^1474]ཕན་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་དེ་ལྟར་གྱུར་པ་ཡིན་ཞེ་ན། དབང་པོ་ཐུལ་བའི་ཕྱིར་དང་། འབྲས་བུ་སྨད་པ་སྤྱད་པ་ལ་མ་ཆགས་པའི་ཕྱིར་རོ། །

[Block 2333]
ཡང་ན་དངོས་པོ་ཀུན་གྱིས་ཕན་པ༌[^1475]བྱེད་པར་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དབང་པོ་ཐུལ་བའི་ཕྱིར་དང་། ཆོས་དོན་གཅིག་ཏུ༌[^1476]བྱེད་པས་འབྲས་བུ་སྨད་པ་སྤྱད་པ་ལ་མ་ཆགས་པའི་ཕྱིར་ཏེ། འདིས་ནི་ནོར༌[^1477]གྱི་འདོད་པ་ལ་ཆགས་པ་མེད་པར༌[^1478]བསྟན་ཏེ། འབྲས་བུ་ཞེས་སྨོས་པས་སོ། །ཇི་ལྟ་བུ་ཞེ་ན། ཐུབ་པ་བཞིན་ནོ། །

[Block 2334]
ཆོས་དོན་གཅིག་ཏུ་བྱེད་ཅེས་བྱ་བ་དེའི་རྒྱུ་ཡང་བསྟན་པ་ཡིན་ཏེ། རང་གི་དོན་ལས་བརྩམས་པའོ། །

[Block 2335]
ད་ནི་གཞན༌[^1479]གྱི་རྒྱུ་ལས་ཀྱང་སྨྲས་པ་ཡིན་ཏེ། གཞན་གྱི་མཚན་ཉིད་ལས་བརྩམས་ནས། སྐྱེ་དགུ་རྣམས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2336]
གཙོ་བོ་རྣམས་ཀྱི་སྤྱོད་པ་ནི་གཙོ་བོའི་སྤྱོད་པའོ། །

[Block 2337]
དེའི་རྗེས་ནི་གཙོ་བོའི་སྤྱོད་པའི་རྗེས་ཏེ། སྒྲུབ་པ་གང་ལ་ཡོད་པའི་རང་བཞིན་ནི་གཙོ་བོའི་རྗེས་སྤྱོད་རང་བཞིན་ནོ། །

[Block 2338]
གཙོ་བོ་ནི་ཁྱད་པར་དུ་གྱུར་པའོ། །

[Block 2339]
སྔར་བསྟན་པའི་ཆོས་དོན་གཅིག་ཏུ་སྤྱོད་པ་དང་། དངོས་པོ་ཀུན་གྱིས༌[^1480]འགྲོ་ལ་ཕན་བྱེད་པ། །ཞེས་པ༌[^1481]དེ་གཉི་ག་བསྟན་པའི་ཕྱིར། ནོར་ཡང་བྱིན་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2340]
ཚིགས་བཅད་འདིས་ནི་བདག་དང་གཞན་གྱི༌[^1482]དོན་ལས་བརྩམས་ཏེ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་བསྟན་ཏོ། །

[Block 2341]
སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པས་ནི་བདག་གི་དོན་ཕུན་སུམ་ཚོགས་པ་སྟེ། སྦྱིན་པ་ལ་སོགས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་གསུམ་ནི་ལོངས་སྤྱོད་ཀྱི་བདག་ཉིད་སྲིད་པའི་གཡོག་འཁོར་ཕུན་སུམ་ཚོགས་པའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 2342]
འགྲོ་བའི་དོན་ཡང་སྤྱོད་ཅེས་བྱ་བ་འདིས་ནི་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 2343]
འགྲོ་ལ་ཕན་སེམས་མཐོང་ན་ཞི་བར་སྣང་། །ཞེས་བྱ་བ་ནི་སྐྱེ་དགུ་རྣམས་ལ་ཕན་པས་ན་འགྲོ་ལ་ཕན་པའོ། །

[Block 2344]
འགྲོ་བའི་དོན་ལ་ཕན་པའི་ལྷག་པའི་བསམ་པ་ཡོད་པ་ནི་འགྲོ་ལ་ཕན་པའི་སེམས་སོ། །

[Block 2345]
དེ་མཐོང་ན་ཞི་བར་སྣང་བ་གང་ཡིན་པ་དེ་ནི་འགྲོ་ལ་ཕན་སེམས་མཐོང་ན་ཞི་བར་སྣང་བ་སྟེ། འདིས་ནི་བསམ་གཏན་དང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 2346]
སེམས་ཞེས་བྱ་བ་སྨོས་པས་ནི་ཐབས་ལ༌[^1483]མཁས་པའི་རྣམ་པ་སྟེ། མཁས་པའི་རྣམ་པ་ནི་ཤེས་རབ་སྟེ། དེ་ཡང་སེམས་རྩེ་གཅིག་པས་བྱས་པར་བསྟན་པའི་ཕྱིར་གཉི་ག་སྨོས་སོ། །

[Block 2347]
དོན་ཡང་སྤྱོད་ཅེས་བྱ་བ་འདིས་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 2348]
འགྲོ་ལ་ཕན་སེམས་ཞེས་བྱ་བ་འདིས༌[^1484]ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། བསམ་གཏན་དང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་གཉིས་ཀྱིས་སོ། །

[Block 2349]
བག་མེད་པའི་དབང་གིས་ཁ་ཅིག་ཏུ་ཐན་པ་འབྱུང་བས་འཁྲུག་ཅིང་གནོད་པར་གྱུར་ཏོ་ཞེས་བྱ་བ་ལ། ཆར་འབབ་མི་མཁས་པས་ཁ་ཅིག་ཏུ་ཐན་པ་འབྱུང་བ་དེས་འཁྲུགས༌[^1485]པའོ། །

[Block 2350]
གང་དག་ཅེ་ན། སེམས་ཅན་རྣམས་སོ། །
--- END BLOCKS ---
