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
གཟུགས་ན་བཟོ་མ་གཏོགས་པའོ། །

[Block 2347]
གཟུགས་ཀྱི་ཁམས༌[^1235]ནི་རྣམ་པ་གསུམ༌[^1236]དབྱེ་སྟེ། དེ་ན་བཟོ་མེད་པའི་ཕྱིར་བཟོའི་གནས་པ་མ་གཏོགས་སོ། །

[Block 2348]
དེ་ལྟར་ན་སེམས་བཅུ་གཉིས་པོ་དེ་དག་ནི་ཡང་དགེ་བ་དྲུག་དང་། མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་བདུན༌[^1237]དུ་ཕྱེ་ནས་ཉི་ཤུར་འགྱུར་རོ། །

[Block 2349]
གཟུགས་མེད་པའི་ཁམས་ན་ནི་སྤྱོད་ལམ༌[^1238]ལ་སོགས་པ་མེད་པའི་ཕྱིར་སྤྱོད་ལམ་པ་ལ་སོགས་པའི་སེམས་མེད་དོ། །

[Block 2350]
དེ་དག་གི་དམིགས་པ་ནི་གཟུགས་དང་། དྲི་དང་རོ་དང་རེག་བྱ་རྣམས་ཡིན་ནོ། །

[Block 2351]
བཟོའི་གནས་པ༌[^1239]ནི་སྒྲ་ཡང་ཡིན་ནོ། །

[Block 2352]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དག་ཁོ་ན་ཡིན་ནོ། །

[Block 2353]
སྤྱོད་ལམ་པ་དང་། བཟོའི་གནས་པ་དག་གི་སྦྱོར་བ་པ་ནི་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་ཡིན་ནོ། །

[Block 2354]
གཞན་དག་ན་རེ་བཟོའི་གནས་པས་མངོན་པར་བསྒྲུབས་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་སྐྱེ་མཆེད་བཅུ་གཉིས་ལ་དམིགས་པ་ཡང་ཡོད་དོ་ཞེས་ཟེར་རོ། །

[Block 2355 [HEADING]]
###### སེམས་ཉི་ཤུ་པོ་གང་གི་མཇུག་ཐོགས་སུ་གང་འབྱུང་བ། ^2-5-6-2-1-0

[Block 2356 [HEADING]]
###### **འདོད་པ་ན་སྤྱོད་པའི་བརྒྱད།** ^2-5-6-2-1-1-0

[Block 2357]
ཡང་སེམས་ཉི་ཤུ་པོ་འདི་དག་ལས་གང་གི་མཇུག་ཐོགས་སུ་གང་ཞིག་འབྱུང་ཞེ་ན། རེ་ཞིག་འདོད་པ་ན་སྤྱོད་པའི་བརྒྱད་ལས་སྦྱོར་བ་ལས་བྱུང་བའི་མཇུག་ཐོགས་སུ༌[^1240]ནི་སེམས་བཅུ་འབྱུང་སྟེ། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་ས་པ་བདུན་དང་། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། སློབ་པ་དང་། མི་སློབ་པའོ། །

[Block 2358]
དེ་ནི་བརྒྱད་ཀྱི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། རང་གི་དགེ་བ་དང་། ཉོན་མོངས་པ་ཅན་དག་དང་། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། ཉོན་མོངས་པ༌[^1241]ཅན་དག་དང་། སློབ་པ་དང་། མི་སློབ་པ་དག་ལས་སོ། །

[Block 2359]
སྐྱེས་ནས་ཐོབ་པའི་མཇུག་ཐོགས་སུ་ནི་དགུ་སྟེ། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་ས་པ་བདུན་དང་། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་གོ། །

[Block 2360]
དེ་ནི་བཅུ་གཅིག་གི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། སྔ་མ་བཞིན་དུ་རང་གི་བདུན་དང་། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། ཉོན་མོངས་པ་ཅན་དག་དང་། སློབ་པ་དང་། མི་སློབ་པ་དག་ལས་སོ། །

[Block 2361]
མི་དགེ་བ་དང་། བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་མཇུག་ཐོགས་སུ་ནི་བདུན་ཏེ། སྔ་མ་བཞིན་དུ་རང་གི་དག་ཁོ་ནའོ། །

[Block 2362]
དེ་དག་ནི་སེམས་བཅུ་བཞིའི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། རང་གི་བདུན་དང་། སྦྱོར་བ་ལས་བྱུང་བ་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དག་མ་གཏོགས་པ་གཟུགས་ན་སྤྱོད་པ་བཞི་དང་། སྦྱོར་བ་ལས་བྱུང་བ་མ་གཏོགས་པ་གཟུགས་མེད་པ་ན་སྤྱོད་པ་གསུམ་ལས་སོ། །

[Block 2363]
སྤྱོད་ལམ་པ་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པའི་མཇུག་ཐོགས་སུ་ནི་བརྒྱད་དེ། སྦྱོར་བ་ལས་བྱུང་བ་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དག་མ་གཏོགས་པ་རང་གི་ས་པ་དྲུག་དང་། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་གོ། །

[Block 2364]
དེ་དག་ནི་སེམས་བདུན་གྱི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། སྔ་མ་བཞིན་དུ་རང་གི་བདུན་ཁོ་ན་ལས་སོ། །

[Block 2365]
བཟོའི་གནས་པའི་མཇུག་ཐོགས་སུ་ནི་དྲུག་སྟེ། སྦྱོར་བ་ལས་བྱུང་བ་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དག་མ་གཏོགས་པ་རང་གི་རྣམས་ཁོ་ནའོ། །

[Block 2366]
དེ་ནི་བདུན་གྱི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་དག་ཁོ་ན་ལས་སོ། །

[Block 2367]
མངོན་པར་ཤེས་པའི་འབྲས་བུའི་མཇུག་ཐོགས་སུ་ནི་གཉིས་ཏེ། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དང་རང་གི་དྲུག༌[^1242]དང་། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བའོ། །

[Block 2368]
དེ་ཡང་དེ་གཉིས་ཁོ་ན་ལས་སོ། །

[Block 2369 [HEADING]]
###### **གཟུགས་ན་སྤྱོད་པའི་དྲུག།** ^2-5-6-2-1-2-0

[Block 2370]
ད་ནི་གཟུགས་ན་སྤྱོད་པའི་དྲུག་གི་བརྗོད་པར་བྱ་སྟེ། སྦྱོར་བ་ལས་བྱུང་བའི་མཇུག་ཐོགས་སུ་ནི་བཅུ་གཉིས་ཏེ། འདོད་པ་ན་སྤྱོད་པའི་དགེ་བ་དག༌[^1243]དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དང་། རང་གི་དྲུག་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། སློབ་པ་དང་། མི་སློབ་པའོ། །

[Block 2371]
དེ་ན་སེམས་བཅུའི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། འདོད་པ་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དག་དང་། སྤྱོད་ལམ་པ་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པའི་དག་མ་གཏོགས་པ་རང་གི་བཞི་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པ༌[^1244]སྦྱོར་བ་ལས་བྱུང་བ་དང་། ཉོན་མོངས་པ་ཅན་དག་དང་། སློབ་པ་དང་། མི་སློབ་པ་དག་ལས་སོ། །

[Block 2372]
སྐྱེས་ནས་ཐོབ་པའི་མཇུག་ཐོགས་སུ་ནི་བརྒྱད་དེ། འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་ལྔ་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་ནོ། །

[Block 2373]
དེ་ནི་ལྔ་ལས་ཏེ། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་དག་ཁོ་ན་ལས་སོ། །

[Block 2374]
ཉོན་མོངས་པ་ཅན་གྱི་མཇུག་ཐོགས་སུ་ནི་དགུ་སྟེ། འདོད་པ་ན་སྤྱོད་པའི་དགེ་བ་དག་དང་། ཉོན་མོངས་པ་ཅན་དག་སྟེ༌[^1245]བཞི་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་ལྔའོ། །

[Block 2375]
དེ་ནི་སེམས་བཅུ་གཅིག་གི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། འདོད་པ་ན་སྤྱོད་པའི་སྐྱེས་ནས་ཐོབ་པ་དང་། སྤྱོད་ལམ་པ་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དག་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་ལྔ་དང་། སྦྱོར་བ་ལས་བྱུང་བ་མ་གཏོགས་པ་གཟུགས་མེད་པ་ན་སྤྱོད་པ་གསུམ་ལས་སོ། །

[Block 2376]
སྤྱོད་ལམ་པའི་མཇུག་ཐོགས་སུ་ནི་བདུན་ཏེ། འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་དང་། སྦྱོར་བ་ལས་བྱུང་བ་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་བཞི་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་ནོ། །

[Block 2377]
དེ་ནི་ལྔའི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་དག་ཁོ་ན་ལས་སོ། །

[Block 2378]
རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་ཡང་དེ་དང་འདྲ་བར་བརྗོད་པར་བྱའོ། །

[Block 2379]
མངོན་པར་ཤེས་པའི་འབྲས་བུའི་མཇུག་ཐོགས་སུ་ནི་གཉིས་ཏེ། རང་གི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དག་ཁོ་ནའོ། །

[Block 2380]
དེ་ཡང་དེ་དག་ཁོ་ན་ལས་སོ། །

[Block 2381 [HEADING]]
###### **གཟུགས་མེད་པ་ན་སྤྱོད་པའི་བཞི།** ^2-5-6-2-1-3-0

[Block 2382]
ད་ནི་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་བཞི༌[^1246]བརྗོད་པར་བྱ་སྟེ། སྦྱོར་བ་ལས་བྱུང་བའི་མཇུག་ཐོགས་སུ་ནི་བདུན་ཏེ། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། རང་གི་བཞི་དང་། སློབ་པ་དང་། མི་སློབ་པའོ། །

[Block 2383]
དེ་ནི་སེམས་དྲུག་གི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་མ་གཏོགས་པ་རང་གི་གསུམ་དང་། སློབ་པ་དང་མི་སློབ་པ་དག་ལས་སོ། །

[Block 2384]
སྐྱེས་ནས་ཐོབ་པའི་མཇུག་ཐོགས་སུ་ནི་བདུན་ཏེ། རང་གི་བཞི་དང་། ས་འོག་མ་པའི་ཉོན་མོངས་པ་ཅན་དག་གོ། །

[Block 2385]
དེ་ནི་བཞི་ལས་ཏེ། རང་གི་དག་ཁོ་ན་ལས་སོ། །
--- END BLOCKS ---
