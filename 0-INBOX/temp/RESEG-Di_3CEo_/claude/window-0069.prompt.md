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

[Block 2421]
སློབ་པ་ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན་པ་ནི་འབྲས་བུ་ལྔ་ཆར་ཡིན་ནོ། །

[Block 2422 [VERSE]]
མཐོང་བས་སྤང་བྱའི་དེ་ལ་སོགས། །
གསུམ་དང་བཞི་དང་གཅིག་ཡིན་ནོ། །

[Block 2423]
མཐོང་བས་སྤང་བར་བྱ་བའི་ལས་ཀྱི་འབྲས་བུ་མཐོང་བས་སྤང་བར་བྱ་བའི་ཆོས་ནི་གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང་། བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་སོ། །

[Block 2424]
བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི་བཞི་སྟེ། བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་སོ། །

[Block 2425]
སྤང་བར་བྱ་བ་མ་ཡིན་པ་ནི་གཅིག་སྟེ། བདག་པོའི་འབྲས་བུའོ། །

[Block 2426 [VERSE]]
བསྒོམ་པས་སྤང་བར་བྱ༌[^969]ལས་ཀྱི། །
དེ་དག་གཉིས་དང་བཞི་དང་གསུམ།[^970] །

[Block 2427]
བསྒོམ་པས་སྤང་བར་བྱ་བའི་ལས་ཀྱི་འབྲས་བུ་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་། བདག་པོའི་འབྲས་བུ་དག་གོ། །

[Block 2428]
བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི༌[^971]བཞི་སྟེ། བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་པའོ། །

[Block 2429]
སྤང་བར་བྱ་བ་མ་ཡིན་པ་ནི་གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང་། རྒྱུ་མཐུན་པའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 2430 [VERSE]]
སྤང་བྱ་མིན་པའི་དེ་དག་གཅིག །
གཉིས་དང་བཞི་སྟེ་གོ་རིམས་བཞིན། །

[Block 2431]
སྤང་བར་བྱ་བ་མ་ཡིན་པའི་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་གཅིག་སྟེ། བདག་པོས༌[^972]འབྲས་བུའོ། །

[Block 2432]
བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་། བདག་པོའི་འབྲས་བུའོ། །

[Block 2433]
སྤང་བར་བྱ་བ་མ་ཡིན་པ་ནི་བཞི་སྟེ། རྣམ་པར་སྨིན་པའི་འབྲས་བུ་མ་གཏོགས་པའོ། །

[Block 2434]
ཡང་རིགས་པ་མ་ཡིན་པས་བསྐྱེད་པ་ལ་སོགས་པའི་ལས་གསུམ་གསུངས་པ་དེ་བརྗོད་པར་བྱ་སྟེ།

[Block 2435 [VERSE]]
རིགས་མིན་བསྐྱེད་པ་ཉོན་མོངས་ཅན། །
ཁ་ཅིག་ཆོ་ག་ཉམས་པའང་ཞེའོ། །

[Block 2436]
ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ཡང་རིགས་པ་མ་ཡིན་པ་བྱེད་པའི་ཕྱིར་ཆོ་ག་ཉམས་པ་ནི་རིགས་པ་མ་ཡིན་པས་བསྐྱེད་པའོ། །

[Block 2437]
བཟློག་པ་ནི་རིགས་པས་བསྐྱེད་པའོ། །

[Block 2438]
དེ་གཉིས་མ་ཡིན་པ་ནི་རིགས་པ་ཡང་མ་ཡིན་ལ་རིགས་པ་མ་ཡིན་པ་ཡང་མ་ཡིན་པས་བསྐྱེད་པའོ། །

[Block 2439 [HEADING]]
#### ལས་གཅིག་གིས་སྐྱེ་བ་འཕེན་པ། ^4-3-11-0

[Block 2440]
ཅི་ལས་གཅིག་གིས་སྐྱེ་བ་གཅིག་ཁོ་ན་འཕེན་ནམ། འོན་ཏེ་དུ་མ་ཡང་འཕེན། དེ་བཞིན་དུ་ལས་དུ་མས་ཀྱང་སྐྱེ་བ་གཅིག་ཁོ་ན་འཕེན་ནམ། འོན་ཏེ་དུ་མ་ཁོ་ན་ཞིག་འཕེན་ཅེ་ན། འདི་ནི་གྲུབ་པའི་མཐའ་ཡིན་ཏེ། གཅིག་གིས་སྐྱེ་བ་གཅིག་འཕེན་ནོ། །

[Block 2441]
ལས་གཅིག་ཁོ་ནས་སྐྱེ་བ་གཅིག་ཁོ་ན་འཕེན་ཏོ།[^973] །

[Block 2442]
ལས་གཅིག་གིས་འཕངས་པའི་ལས་ནི། ཡོངས་རྫོགས་བྱེད་པ་དུ་མ་ཡིན་པར་འདོད་དེ། དཔེར་ན་རི་མོ་མཁན་གྱི་རི་མོ༌[^974]གཅིག་གིས་གཟུགས་ཀྱིས་བཅད་ནས་མང་པོས་ཡོངས་སུ༌[^975]རྫོགས་པར་བྱེད་པ་དང་འདྲའོ། །

[Block 2443]
ལས་འབའ་ཞིག་སྐྱེ་བ་འཕེན་པར་བྱེད་པ་ཡང་མ་ཡིན་ཏེ། འོན་ཀྱང་རྣམ་པར་སྨིན་པ་དང་བཅས་པ་གཞན་ཡང་ངོ་། །རྣམ་པ་ཐམས་ཅད་དུ།

[Block 2444 [VERSE]]
སེམས་མེད་སྙོམས་པར་འཇུག་པ་དག །
འཕེན་བྱེད་མ་ཡིན་འཐོབ་པའང་མིན། །

[Block 2445]
རྣམ་པར་སྨིན་པ་དང་བཅས་པའི་སེམས་མེད་པའི་སྙོམས་པར་འཇུག་པ་དག་གིས་ཀྱང་རིས་མཐུན་པ་འཕེན་པར་བྱེད་དེ།

[Block 2446 [VERSE]]
ལས་དང་ལྷན་ཅིག་མི་འབྱུང་བའི་ཕྱིར་རོ། །
ཐོབ་པ་རྣམས་ཀྱིས་ཀྱང་མ་ཡིན་ཏེ།
ལས་དང་འབྲས་བུ་མི་གཅིག་པའི་ཕྱིར་རོ། །

[Block 2447 [HEADING]]
#### སྒྲིབ་པ་གསུམ། ^4-3-12-0

[Block 2448]
སྒྲིབ་པ་གསུམ་གསུངས་པ་དེ་དག་གི་རང་བཞིན་ཅི་ཞེ་ན།

[Block 2449 [VERSE]]
མཚམས་མེད་པ་ཡི་ལས་རྣམས་དང་། །
ཉོན་མོངས་ཤས་ཆེ་ངན་འགྲོ་དང་།
འདུ་ཤེས་མེད་པའི་སེམས་ཅན་དང་། །
སྒྲ་མི་སྙན་སྒྲིབ་གསུམ་དུ་འདོད། །

[Block 2450]
མཚམས་མེད་པ་ལྔ་ནི་ལས་ཀྱི་སྒྲིབ་པ་ཡིན་ནོ། །

[Block 2451]
ཉོན་མོངས་པ་ཤས་ཆེ་བ་རྒྱུན་དུ་འབྱུང་བ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པའོ། །

[Block 2452]
ངན་སོང་རྣམ་པ་གསུམ་དང་མི་དང་ལྷའི་ཕྱོགས་གཅིག་ན༌[^976]རྣམ་པར་སྨིན་པའི་སྒྲིབ་པའོ། །

[Block 2453]
ཡང་སྒྲིབ་པ་འདི་དག་པས༌[^977]གང་ཞིག་འགྲོ་བ་གང་དག་ན་ཡོད་པར་རིག་པར་བྱ་ཞེ་ན། རེ་ཞིག་གཅིག་ཏུ།

[Block 2454 [VERSE]]
མཚམས་མེད་གླིང་གསུམ་དག་ན་ཡོད། །
སྒྲ་མི་སྙན་མ་གཏོགས་པའོ། །

[Block 2455]
དེ་དག་ན་ཡང་སྐྱེས་པ་དང་བུད་མེད་རྣམས་ཁོ་ན་ལ་སྟེ།
--- END BLOCKS ---
