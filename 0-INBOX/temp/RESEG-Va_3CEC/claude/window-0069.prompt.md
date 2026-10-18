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
རྗེས་སུ་ལྟ་ཞིང་གནས་པས་ཞེས་བྱ་བ་ནི་ཤེས་རབ་དང་ཏིང་ངེ་འཛིན་གྱིས་སོ། །ཤེས་པ་བསྐྱེད༌[^2101]ཅེས་བྱ་བ་ནི་སྐྱེ་བ་ལ་སྐྱེ་བར་ཤེས་པ་དང་། འཇིག་པ་ལ་འཇིག་པར་ཤེས་པ་དང་། གནས་པ་ལ་གནས་པར་ཤེས་པ་བསྐྱེད་པར་བྱའོ། །

[Block 2417]
ཚོར་བ་ལ་ཚོར་བའི་རྗེས་སུ་ལྟ་ཞིང་དྲན་པ་ཉེ་བར་གཞག་པ་མདོར་བསྡུས་ཏེ་བསྟན་པའི་ཕྱིར། གང་སེམས་ཅན་ཐམས་ཅད་ཀྱི༌[^2102]ཚོར་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཤེས་པའི་ཚིག་སྐྱེ་བ་ལ་སོགས་པ་ཀུན་དང་སྦྱར་རོ། །

[Block 2418]
དགེ་བའི་རྒྱུ་ལས་བྱུང་བའི་ཚོར་བ་གང་ཡིན་པ་ཤེས་པ་དང་། མི་དགེ་བའི་རྒྱུ་ལས་བྱུང་བའི་ཚོར་བ་གང་ཡིན་པ་ཤེས་པའོ། །

[Block 2419]
ཚོར་བ་དྲན་པ་ཉེ་བར་གཞག་པ༌[^2103]བསྒོམ་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 2420 [HEADING]]
#### སེམས་དྲན་པ་ཉེ་བར་གཞག་པ། ^8-1-3-0

[Block 2421]
རབ་ཏུ་གནས་པའི་བྱང་ཆུབ་སེམསེམས་དཔའ་གང་ན་ཞེས༌[^2104]གང་སེམས་དྲན་པ་ཉེ་བར་གཞག་པ༌[^2105]ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། རྣམ་པར་ཤེས་པའི་གནས་ཐམས་ཅད་ལས་འདས་པ་ཡང་ཐོབ་ལ། བྱང་ཆུབ་སེམས་དཔའི་ཏིང་ངེ་འཛིན་ཚད་མེད་པ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའོ། །

[Block 2422]
དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་སེམས་ལ་སེམས་ཀྱི༌[^2106]རྗེས་སུ་ལྟ་བ་དྲན་པ་ཉེ་བར་གཞག་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས༌[^2107]བསྒོམ་པར་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 2423]
བྱང་ཆུབ་སེམས་དཔའ་དེའི་བྱང་ཆུབ་ཀྱི་སེམས་མ་བརྗེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། ཉན་ཐོས་དང་རང་སངས་རྒྱས་དག་སེམས་དྲན་པ་ཉེ་བར་གཞག་པ་ན་བདག་གི་སེམས་མི་རྟག་པ་ལ་སོགས་པ་དྲན་པ་ཉེ་བར་འཇོག་པ་ལྟ་བུ་ནི་མ་ཡིན་གྱི། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཐོག་མར་བྱང་ཆུབ་ཏུ་སེམས་ཇི་ལྟར་བསྐྱེད་པའི་བྱང་ཆུབ་ཀྱི་སེམས་དེ་མི་བརྗེད་པའི་གཟུངས་ཀྱིས་དྲན་པས་མི་བརྗེད་པ་དང་། དྲན་པ་ཉིད་མ་ཉམས་པར་བསྲུང་བ༌[^2108]དང་། བསྲུངས་པ་ཉིད་མི་མཐུན་པའི་ཕྱོགས་ལ་མི་གཡེང་བར་བྱེད་པ་ནི་སེམས་དྲན་པ་ཉེ་བར་འཇོག་པ་ཞེས་བྱའོ། །

[Block 2424]
བྱང་ཆུབ་ཀྱི་སེམས་མི་བརྗེད་པ་དེ་ཇི་རྟག་པའི་ཕྱིར་དེ་ལྟ་བུ་ཞིག་ནས་མཉམ་པ༌[^2109]ལ། དེའི་ཕྱིར་དེ་སེམས་ལ་འང་ཇི་ལྟར་རྟོག་གོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་ཞེས་བྱ་བ་ནི་སེམས་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེ་འམ། བྱང་ཆུབ་ཀྱི་སེམས་མ་བརྗེད་པའི་བྱང་ཆུབ༌[^2110]སེམས་དཔའ་དེའོ། །

[Block 2425]
སེམས་ལ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ལའོ། །

[Block 2426]
འདི་ལྟར་རྟོག་ཅེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་དེ་ལ་འོག་ནས་འབྱུང་བ་ལྟར་རྟོག་པའོ། །ཇི་ལྟར་རྟོག་ཅེ་ན། དེའི་ཕྱིར་སེམས་ནི་སྐྱེས༌[^2111]ནས་ཞིག་ཅིང་ཞུ་སྟེ་མི་གནས་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སེམས་ནི་སེམས་ཉིད་དམ་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 2427]
སྐྱེས་ནས་ཞེས་བྱ་བ་ནི་སྐྱེས་མ་ཐག་ཏུའོ། །

[Block 2428]
ཞིག་ཅིང་ཞུ་སྟེ༌[^2112]ཞེས་བྱ་བ་ནི་དོན་གཅིག་སྟེ་དེ་མ་ཐག་ཏུ་ཞིག་པའོ། །

[Block 2429]
མི་གནས་པ་ནི་ཅུང་ཟད་ཀྱང་འདུག་པའི་མཐུ་མེད་པ་སྟེ་དེ་བས་ན་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2430]
ནང་ན་ཡང་མི་འདུག་ཕྱི་རོལ་ན་ཡང་མི་འཕྲོས། གཉི་ག་མེད་པར་ཡང་མི་དམིགས་ཞེས་བྱ་བ་ནི་སེམས་དེ་སྐད་ཅིག་མའི་རང་བཞིན་སྐྱེས་མ་ཐག་ཏུ་འཇིག་ཅིང་དེངས་པའི་ངོ་བོ་ཉིད་དེ། ཞིག་ནས་ཀྱང་མེད་པར་འགྱུར་བའི་ནང་གི་དངོས་པོ་རྣམས་ལ་ཡང་མི་གནས། ཕྱི་རོལ་གྱི་ཡུལ་རྣམས་ལ་ཡང་མ་འཕོས།[^2113] དེ་གཉིས་ཀ་མ་ཡིན་པ་གཞན་ཕྱི་ནང་གཉིས་ཀྱི་བར་ན་ཡང་མི་དམིགས་མི་གནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2431]
གང་དག་གི་བྱང་ཆུབ་ཀྱི་སེམས་དང་པོ་བསྐྱེད་པ༌[^2114]དེ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། གོང་དུ་བཤད་པར་ཡང་མ་ཟད་ཀྱི། འདི་ལྟར་ཡང་ཁོང་དུ་ཆུད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2432]
སྐྱེས་པ་ནི་འདས་པའི་དུས་སུ་སྐྱེས་ཟིན་ཏོ། །

[Block 2433]
ཟད་ཅིང་འགག་པ་ལ་སོགས་པ་ནི་དོན་གཅིག་སྟེ་མེད་པར་གྱུར་པར་སྟོན་པའོ། །

[Block 2434]
ཟད་པ་ནི་རྒྱུ་མེད་པའོ། །

[Block 2435]
འགག་པ༌[^2115]ནི་རང་བཞིན་གྱིས༌[^2116]མེད་པའོ། །

[Block 2436]
ཡལ་བ་ནི་མེད་པར་གྱུར་ནས་ཀྱང་གང་དུ་ཡང་གནས་པར་མ་གྱུར་ཏེ་དེ་བས་ན་མེད་པར་གྱུར་པ་ཞེས་བྱའོ། །

[Block 2437]
ཡུལ་དང་ཕྱོགས་ན་མི་གནས་ཏེ་དེ་ནི་གདགས་པར་མི་ནུས་སོ་ཞེས་བྱ་བ་ལ། ཐོག་མར་སེམས་བསྐྱེད་དེ་དེ་སྐད་ཅིག་མ་རེ་རེ་ལ་ཡང་ཟད་ཅིང་འགགས་ཏེ་གཞན་དང་གཞན་དུ་གྱུར་ལ། ཡལ་ཞིང་མེད་པར་གྱུར་པས་དངོས་པོ་མེད་པའི་ཕྱིར་ཡུལ་དང་། ཕྱོགས་ན་མི་གནས། མིང་དང་མཚན་མར་གདགས་སུ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2438]
སེམས་གང་དག༌[^2117]གིས་བྱང་ཆུབ་ཀྱི་ཕྱིར་དགེ་བའི་རྩ་བ་རྣམས་ཡང་དག་པར་བསྒྲུབས་པ་དེ་དག་ཀྱང་ཟད་ཅིང་འགགས་ཏེ་ཡལ་ཞིང་མེད་པར་གྱུར་པས་ཞེས༌[^2118]བྱ༌[^2119]ལ། སེམས་གང་དག་གིས་ནི་དགེ་བའི་རྩ་བའི་རྒྱུར་འགྱུར་བའི་སེམས་བསྐྱེད་བ་གང་གིས་སོ། །

[Block 2439]
བྱང་ཆུབ་ཀྱི་ཕྱིར་ནི་འབྲས་བུ་དེ་ཐོབ་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2440]
དགེ་བའི་རྩ་བ༌[^2120]བསྒྲུབས་པ་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་བསྒྲུབས༌[^2121]པའོ། །

[Block 2441]
བྱང་ཆུབ་ཀྱི་སེམས་ཉིད་གོང་དུ་སྨོས་པའི་ཚུལ་གྱིས་དོན་དམ་པར་ངོ་བོ་ཉིད་མེད་པས། དེ་ལས་བྱུང་བའི་དགེ་བའི་རྩ་བ་རྣམས་ཀྱང་ཡལ་ཞིང་མེད་པར་གྱུར་པས་སེམས་བཞིན་དུ་ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་ཡུལ་དང་ཕྱོགས་ན་མི་གནས་ཤིང་མིང་དང་མཚན་མར་གདགས་པར་མི་ནུས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2442]
སེམས་གང་དག་གིས༌[^2122]དགེ་བའི་རྩ་བ་དེ་དག་བྱང་ཆུབ་ཏུ་བསྔོས་པ་དེ་དག་ཀྱང་དེའི་རང་བཞིན་དེའི་མཚན་ཉིད་དེ་ཞེས་བྱ་བ་ལ་སེམས་གང་གིས་ནི་དགེ་བའི་རྩ་བའི་རྒྱུར་གྱུར་པའི་བྱང་ཆུབ་ཀྱི་སེམས་བསྐྱེད་པས་སོ། །

[Block 2443]
བྱང་ཆུབ་ཏུ་བསྔོས་པས་ཀྱང་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཏུ་བསྔོས་པའི་འོག་ཏུ་འཕེལ་བར་གྱུར་པའི་དགེ་བའི་རྩ་བ་དེ་དག་གོ། །

[Block 2444]
དེ་ནི་འདི་སྐད་དུ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས་བསྐྱེད་པའི་དགེ་བའི་རྩ་བ་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་བསྔོས་པ་དེ་དག་ཀྱང་སེམས་དང་འདྲ་བར་ཟད་ཅིང་འགགས་ཏེ། ཡལ་ཞིང་མེད་པར་འགྱུར་བའི་མཚན་ཉིད་ལས༌[^2123]ཡུལ་དང་ཕྱོགས་ན་མི་གནས་ཤིང་གདགས་པར་མི་ནུས་སོ་ཞེས་བྱ་བར་སྟོན་ཏོ། །

[Block 2445]
སེམས་ཀྱིས༌[^2124]སེམས་མི་ཤེས་སོ་ཞེས་བྱ་བ་ནི། སེམས་དེ་རང་བཞིན་མེད་པས་ཤེས་པར་བྱེད་པ་དང་། ཤེས་པར་བྱ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2446]
དེ་བཞིན་དུ་འོག་མ་ལ་ཡང་སྦྱར་རོ། །

[Block 2447]
སེམས་ཀྱིས༌[^2125]སེམས་ཀྱི་མཚམས་མི་སྦྱོར་བ་ནི་འདས་པའི་སེམས་དེ་མ་འོངས་པར་མི་འཕོ་ཞིང་། མ་འོངས་པའི་སེམས་དང་མཚམས་མི་སྦྱོར་བའོ། །

[Block 2448]
དེ་ལ་གང་གིས་བདག་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་བྱ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་མངོན་པར་འཚང་རྒྱ་བར་འགྱུར་བའི་བྱང་ཆུབ་ཀྱི་སེམས་དང་། དགེ་བའི་རྩ་བའི་སེམས་ལ་སོགས་པ་གོང་དུ་སྨོས་པ་ལྟ་བུའི་ཚུལ་གྱིས་བརྟགས་ན་གང་ཡང་རང་བཞིན་དུ་གྲུབ་པ་ནི༌[^2126]མེད་པས་བྱང་ཆུབ་ཀྱི་སེམས་གང་ཡིན་པ་དེ་དགེ་བའི་རྩ་བའི་སེམས་དང་ལྷན་ཅིག་མི་གནས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2449]
སེམས་ལ་རྟོག་པའི་རྣམ་པ་གཞན་བསྟན་པའི་ཕྱིར། ཡང་དེ་འདི་སྙམ་དུ་སེམས་ཏེ་རྒྱུ་དང་འབྲས་བུ་ཆུད་མི་ཟ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2450]
དེ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེའོ། །

[Block 2451]
དེ་ལྟར་སེམས་ཀྱི་རང་བཞིན་སྟོང་ཡང་ཀུན་རྫོབ་ཏུ་རྒྱུ་གང་སྤྱད་པའི་འབྲས་བུ་དེ་བཞིན་དུ་ཐོབ་པར་འགྱུར་ཏེ་ཆུད་མི་ཟ་བར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་གཅིག་ཁོ་ནར་ངེས་པར་མི་མངོན་པ་དེ་ནི་བལྟ་དཀའ་བས་ཤིན་ཏུ་ཟབ་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2452]
སེམས་ཀྱི་ཆོས་ཉིད་དེ་ལྟ་བུ་ཡིན་དུ་ཟིན་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དོན་དམ་པར་སེམས་དེ་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་དུ་ཟིན་ཀྱང་ཀུན་རྫོབ་ཏུ་རྒྱུ་དང་རྐྱེན་རྣམས་ཚོགས་ན་མེད་པར་མི་འགྱུར་ལ། རྒྱུ་རྐྱེན་ཚོགས་པ་ལས་འབྱུང་བ༌[^2127]དེ་དག་ཀྱང་མུ་སྟེགས་ཅན་གྱི༌[^2128]བྱེད་པ་པོ་ལ་སོགས་པ་མེད་པས་དེ་དག་གིས་ཀྱང་བསྐྱོད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2453]
དེ་དག་ཇི་ལྟར་འདོད་པ་བཞིན་རྣམ་པར་བསྒྲུབ་པ༌[^2129]ཞེས་བྱ་བ་ནི་དེ་ལྟར་བྱེད་པ་པོ་ལ་སོགས་པ་མེད་པར་ཡང་རྒྱུ་རྐྱེན་ཚོགས་པ་ལས་ཀུན་རྫོབ་ཏུ་སྐྱེ་ཞིང་འབྱུང་བས་ན་རྒྱུ་གང་དང་གང་གིས་འབྲས་བུ་གང་དང་གང་སྒྲུབ་པ་དེ་དག་ཇི་ལྟར་འདོད་པ་བཞིན་དུ་གྲུབ་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2454]
བདག་གིས་ཀྱང༌[^2130]རྣམ་པར་བསྒྲུབ་པ་ལ་བརྩོན་པར་བྱ་ཞེས་བྱ་བ་ནི༌[^2131]ཇི་ལྟར་འདོད་པ་བཞིན་འབྲས་བུ་འགྲུབ་པས་བདག་གིས་ཀྱང་བདོག་པ་ཐམས་ཅད་ཡོངས་སུ་གཏང་བ༌[^2132]ལ་སོགས་པའི་འབྲས་བུ་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་བྱ་བའི་ཕྱིར་བསྔོ་བ་ལ་སོགས་པ་ལ་བརྩོན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2455]
སེམས་ཀྱི་ཆོས་ཉིད་འདི་ཡང་མི་སྤོང་ངོ་ཞེས་བྱ་བ་ནི་དེ་དག་ཀུན་རྫོབ་ཏུ་སྒྲུབ་པ༌[^2133]ལ་བརྩོན་པར་བྱེད་ཀྱང་། དོན་དམ་པར་སེམས་ཀྱི་ཆོས་ཉིད་མ་སྐྱེས་པ་ཡང་མི་སྤོང་བ་འམ། དེ་ཡང་ཉམས་པར་མི་བྱེད་པའོ། །
--- END BLOCKS ---
