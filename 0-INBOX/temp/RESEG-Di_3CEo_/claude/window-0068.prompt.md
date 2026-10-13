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
འདི་ནི་རྫོགས་སོ། །

[Block 2382 [HEADING]]
#### འབྲས་བུ་ལྔ། ^4-3-10-0

[Block 2383]
གོང་དུ་འབྲས་བུ་ལྔ་བཤད་པ་གང་དག་ཡིན་པ་དེ་དག་ལས་ལས་གང་ཞིག་འབྲས་བུ་དུ་ཞིག་གི་འབྲས་བུ་དང་བཅས་པ་ཡིན་ཞེ་ན། དྲིར་བཅས་སྤོང་བའི་ལམ་དག་གི །ལས་ནི་ལྔ་ཡིས་འབྲས་བུར་བཅས། །ལས་དེ་ནི་འབྲས་བུ་ལྔས་འབྲས་བུ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 2384]
དྲི་མེད་བཞི་ཡིས། བར་ཆད་མེད་པའི་ལམ་ཟག་པ་མེད་པའི་ལས་ནི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་མ་གཏོགས་པ་འབྲས་བུ་བཞིས་འབྲས་བུ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 2385]
ཟག་བཅས་གཞན། དགེ་དང་མི་དགེ་གང༌[^956]ཡིན་པའང་། །སྤོང་བའི་ལམ་ལས་གཞན་པའི་ལས་དགེ་བ་ཟག་པ་དང་བཅས་པ་གང་ཡིན་པ་དང་། མི་དགེ་བ་གང་ཡིན་པ་དེ་ཡང་འབྲས་བུ་བཞིས་འབྲས་བུ༌[^957]དང་བཅས་པ་ཡིན་ཏེ།

[Block 2386 [VERSE]]
བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་སོ། །
ཟག་པ་མེད་པ་ལྷག་མ་དང་། །
ལུང་བསྟན་མིན་གང་གསུམ་གྱིས་སོ། །

[Block 2387]
སྤོང་བའི་ལམ་ལས་གཞན་པའི་ལམ་ཟག་པ་མེད་པ་དང་ལུང་དུ་མ་བསྟན་པའི་ལས་གང་ཡིན་པ་ནི་འབྲས་བུ་གསུམ་གྱིས་ཏེ། རྣམ་པར་སྨིན་པ་དང་བྲལ་བའི་འབྲས་བུ་དག༌[^958]མ་གཏོགས་སོ། །

[Block 2388 [VERSE]]
དགེ་བའི་དགེ་ལ་སོགས་པ་ནི། །
བཞི་དང་གཉིས་དང་དེ་བཞིན་གསུམ། །

[Block 2389]
ལས་དགེ་བའི་འབྲས་བུ་ཆོས་དགེ་བ་བཞི་སྟེ། རྣམ་པར་སྨིན་པའི་འབྲས་བུ་མ་གཏོགས་སོ།[^959] །

[Block 2390]
མི་དགེ་བ་ནི་གཉིས་ཏེ། །སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི་འབྲས་བུའོ། །

[Block 2391]
ལུང་དུ་མ་བསྟན་པའི་གསུམ་སྟེ། རྒྱུ་མཐུན་པ་དང་བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་པའོ། །

[Block 2392 [VERSE]]
མི་དགེའི་དགེ་སོགས་གཉིས་དང་ནི། །
གསུམ་དང་བཞི་སྟེ་རིམ་པ་བཞིན། །

[Block 2393]
ལས་མི་དགེ་བའི་འབྲས་བུ་ཆོས་དགེ་བ༌[^960]ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་། བདག་པོའི་འབྲས་བུ་དག་གོ། །

[Block 2394]
མི་དགེ་བ་ནི་གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང་བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་སོ། །

[Block 2395]
ལུང་དུ་མ་བསྟན་པ་ནི་བཞི་སྟེ། བྲལ་བ་མ་གཏོགས་སོ། །

[Block 2396 [VERSE]]
ལུང་བསྟན་མིན་གྱི་དགེ་ལ་སོགས། །
དེ་དག་གཉིས་དང་གསུམ་དང་གསུམ། །

[Block 2397]
[^961]ལུང་དུ་མ་བསྟན་པའི་འབྲས་བུ་ཆོས་དགེ་བ་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་། བདག་པོའི་འབྲས་བུའོ། །

[Block 2398]
མི་དགེ་བ་གསུམ་ཏེ།[^962] བྲལ་བ་དང་། རྣམ་པར་སྨིན་པ་མ་གཏོགས་པའོ། །

[Block 2399]
ལུང་དུ་མ་བསྟན་པའི་ཆོས་གསུམ་ནི་དེ་དག་ཁོ་ན་ཡིན་ནོ། །

[Block 2400]
འདས་པའི་ཐམས་ཅད་བཞི་ཡིན་ནོ། །

[Block 2401]
འདས་པའི་ལས་ཀྱི་འབྲས་བུ་དུས་གསུམ་པའི་ཆོས་ནི་བཞི་སྟེ།

[Block 2402 [VERSE]]
བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་སོ། །
བར་མ་ཡི་ནི་མ་འོངས་པ་འང་། །

[Block 2403]
ད་ལྟར་བྱུང་བའི་འབྲས་བུ་ཆོས་མ་འོངས་པ་འང་བཞི་སྟེ། དེ་དག་ཉིད་དོ། །

[Block 2404]
བར་མ་གཉིས་སོ། །

[Block 2405]
ད་ལྟར་བྱུང་བའི་ཆོས་ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི་འབྲས་བུ་དག་གོ། །

[Block 2406]
མ་སྐྱེས་པའི་འབྲས་བུ་མ་འོངས་གསུམ་ཡིན་ནོ། །

[Block 2407]
རྒྱུ་མཐུན་པ་དང་།

[Block 2408 [VERSE]]
བྲལ་བའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །
རང་གི་ས་པ་བཞི༌[^963]ཡིན་ནོ། །
བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་སོ། །
གཞན་གྱི་ས་པ་གསུམ་དང་གཉིས། །

[Block 2409]
གལ་ཏེ་གཞན་གྱི་ས་པའི་ཆོས་ཟག་པ་མེད་པ་ཞིག་ཡིན་ན་ནི་འབྲས་བུ་གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང་། བྲལ་བའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 2410]
གལ་ཏེ་ཟག་པ་དང་བཅས་པ་ཞིག་ཡིན་ན་ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི་འབྲས་བུ་དག་གོ། །

[Block 2411]
སློབ་པའི་སློབ་ལ་སོགས་པ་གསུམ། །སློབ་པའི་ལས་ཀྱི་འབྲས་བུ་སློབ་པའི་ཆོས་གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང་བྲལ་བའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 2412]
མི་སློབ་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 2413]
སློབ་པའི༌[^964]ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན་པ་ཡང༌[^965]གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང་རྒྱུ་མཐུན་པའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 2414 [VERSE]]
མི་སློབ་ལས་ཀྱི་འབྲས་བུ་ནི། །
སློབ་པ་ཡི༌[^966]ནི་ཆོས་ལ་སོགས། །
གཅིག་དང་གསུམ་དང་གཉིས་ཡིན་ནོ། །

[Block 2415]
མི་སློབ་པའི་ལས་ཀྱི་འབྲས་བུ་སློབ་པའི་ཆོས་ནི་གཅིག་སྟེ། བདག་པོའི་འབྲས་བུའོ། །

[Block 2416]
མི་སློབ་པ་ནི་གསུམ་སྟེ། །རྣམ་པར་སྨིན་པ་དང་བྲལ་བའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 2417]
སློབ་པའི༌[^967]ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན་པ་ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་།

[Block 2418 [VERSE]]
བདག་པོའི་འབྲས་བུ་དག་གོ། །
དེ་ལས་གཞན་པའི་འབྲས་བུ་ནི། །
སློབ་སོགས་གཉིས་དང་གཉིས་དང་ལྔ། །

[Block 2419]
སློབ་པ་ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན་པའི་ལས་ཀྱི་འབྲས་བུ་སྤོང་བའི༌[^968]ཆོས་ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་། བདག་པོའི་འབྲས་བུ་དག་གོ། །

[Block 2420]
མི་སློབ་པ་ཡང་དེ་དང་འདྲའོ། །
--- END BLOCKS ---
