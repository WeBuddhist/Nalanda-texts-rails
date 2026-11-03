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
[Block 3396]
སེམས་རྣམ་པར་གྲོལ་བ་དང་། ཤེས་རབ་རྣམ་པར་གྲོལ་བ་དང་། རྣམ་པར་གྲོལ་བ་གཉིས་སུ་གསུངས་ཏེ། དེ་ཉིད་རྣམ་པར་གྲོལ་བའི་ཕུང་པོ་ཡིན་པར་ཡང་བལྟའོ། །

[Block 3397]
གཞན་དག་ན་རེ་མདོ་ལས།

[Block 3398]
སྟག་གི་བྱང་ཆུབ་ཀྱི་བུ་དག་རྣམ་པར་གྲོལ་བ་ཡོངས་སུ་དག་པ་གཙོ་བོ་གང་ཡིན་ཞེ་ན། འདི་ན༌[^2370]དགེ་སློང་འདོད་ཆགས་ལས་སེམས་འདོད་ཆགས་དང་བྲལ་ཞིང་རྣམ་པར་གྲོལ་བ་ཡིན། ཞེ་སྡང་དང་གཏི་མུག་ལས་སེམས་འདོད་ཆགས་དང་བྲལ་ཞིང་རྣམ་པར་གྲོལ་བ་ཡིན་ཏེ། འདི་ལྟར་རྣམ་པར་གྲོལ་བའི་ཕུང་པོ་ཡོངས་སུ་མ་རྫོགས་པ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའམ། ཡོངས་སུ་རྫོགས་པ་རྗེས་སུ་འཛིན་པར་བྱེད་པ་འདུན་པ་དང་བརྩོན་འགྲུས་གང་ཡིན་པ་ཞེས་རྒྱས་པར་གང་གསུངས་པ་ཇི་ལྟ་བུ། དེའི་ཕྱིར་རྣམ་པར་གྲོལ་བ་ནི་མོས་པ་ཁོ་ན་ཡིན་པར་མ་ཟད་དོ། །

[Block 3399]
[^2371]འོ་ན་ཅི་ཞེ་ན། དེ་ཁོ་ན་ཤེས་པས་འདོད་ཆགས་ལ་སོགས་པ་སྤངས་ནས་སེམས་དྲི་མ་མེད་པ་ཉིད་རྣམ་པར་གྲོལ་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ།[^2372] །ཡང་དག་པའི་རྣམ་པར་གྲོལ་བ་བཤད་ཟིན་ཏོ། །

[Block 3400 [HEADING]]
##### ཡང་དག་པའི་ཤེས་པ། ^3-2-19-2-0

[Block 3401]
ཡང་དག་པའི་ལྟ་བ་ལས་མ་གཏོགས་པ་ཡང་དག་པའི་ཤེས་པ་གང་ཞིག་ཡིན་ཞེ་ན། བྱང་ཆུབ་ཇི་སྐད་བཤད་ཤེས་པ། སྔར་བྱང་ཆུབ་ཇི་སྐད་དུ་བཤད་པ་གང་ཡིན་པ་དེ་ཉིད་འདིར་ཡང་དག་པའི་ཤེས་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ། འདི་ལྟ་སྟེ། ཟད་པ་ཤེས་པ་དང་མི་སྐྱེ་བ་ཤེས་པའོ། །

[Block 3402 [HEADING]]
#### སྒྲིབ་པ་ལས་རྣམ་པར་གྲོལ་བར་འགྱུར་བའི་སེམས། ^3-2-20-0

[Block 3403]
སེམས་གང་ཞིག་རྣམ་པར་གྲོལ་བར་འགྱུར། ཅི་འདས་པའམ་མ་འོངས་པའམ་ད་ལྟར་བྱུང་བ་ཡིན༌[^2373]ཞེ་ན། མི་སློབ་སེམས་ནི་སྐྱེ་འགྱུར་བ། །སྒྲིབ་པ་ལས་ནི་རྣམ་གྲོལ་འགྱུར།[^2374] །བསྟན་བཅོས་ལས་མི་སློབ་པའི་སེམས་མ་འོངས་པ་སྒྲིབ་པ་རྣམ༌[^2375]ལས་རྣམ་པར་གྲོལ་བར་འགྱུར་རོ་ཞེས་འབྱུང་ངོ་། །དེའི་སྒྲིབ་པ་ཡང་གང་ཞེ་ན། ཉོན་མོངས་པའི་ཐོབ་པ་ཡིན་ཏེ། དེ་སྐྱེ་བ་ལ་བགེགས་བྱེད༌[^2376]པའི་ཕྱིར་རོ། །

[Block 3404]
རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི་ཚེ་དེ་ཡང་སྤོང་བར་འགྱུར་ལ་མི་སློབ་པའི་སེམས་སྐྱེ་བར་འགྱུར་བ་དེ་ཡང་རྣམ་པར་གྲོལ་བར་འགྱུར་རོ། །

[Block 3405]
དེ་སྤངས་ནས་ནི་མི་སློབ་པའི་སེམས་དེ་ཡང་སྐྱེས་པ་དང་རྣམ་པར་གྲོལ་བ་ཡིན་ནོ། །

[Block 3406]
འོ་ན་སྐྱེ་བར་འགྱུར་བ་མ་ཡིན་པ་དང་། འཇིག་རྟེན་པ་གང་ཡིན་པ་ཇི་ལྟ་བུ་ཞེ་ན། དེ་དག་ཀྱང་རྣམ་པར་གྲོལ་བར་འགྱུར་མོད་ཀྱི་སྐྱེ་བར་ངེས་པ་གང་ཡིན་པ་དེ་ཁོ་ན་བཤད་དོ། །གང་ལས་འཇིག་རྟེན་པ་རྣམ་པར་གྲོལ་བར་འགྱུར་ཞེ་ན། སྐྱེ་བའི་སྒྲིབ་པ་དེ་ཉིད་ལས་སོ། །

[Block 3407]
མ་གྲོལ་བ༌[^2377]ལ་ཡང་འཇིག་རྟེན་པའི༌[^2378]སྐྱེ་བར་འགྱུར་བ་མ་ཡིན་ནམ་ཞེ་ན། དེ་ནི་དེ་དང་མི་འདྲའོ། །དེ་ཅི་འདྲ་ཞེ་ན། ཉོན་མོངས་པའི་ཐོབ་པ་དང་ལྷན་ཅིག་པ་ཡིན་ནོ། །

[Block 3408]
གནས་སྐབས་གང་ཡིན་པའི༌[^2379]ལམ་གྱིས་དེ་སྐྱེ་བའི་སྒྲིབ་པ་སྤོང་ཞེ་ན།

[Block 3409 [VERSE]]
འགག་པར་འགྱུར་བའི་ལམ་གྱིས་ནི། །
དེ་ཡི་སྒྲིབ་པ་རབ་ཏུ་སྤོང་། །

[Block 3410]
དེ་ལྟར་གྱི་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3411 [HEADING]]
#### ཁམས་གསུམ། ^3-2-21-0

[Block 3412]
རྣམ་པར་གྲོལ་བ་འདུས་མ་བྱས་སུ་བཤད་པ་གང་ཡིན་པ་དང་། ཁམས་གསུམ་པོ༌[^2380]སྤངས་པའི་ཁམས་དང་། འདོད་ཆགས་དང་བྲལ་བའི་ཁམས་དང་། འགོག་པའི་ཁམས་ཞེས་འབྱུང་བ་གང་ཡིན༌[^2381]དེ་དག་ལ་ཁྱད་པར་ཅི་ཡོད་ཅེ་ན། འདུས་མ་བྱས་ཉིད་ཁམས་ཞེས་བྱ། །རྣམ་པར་གྲོལ་བ་འདུས་མ་བྱས༌[^2382]དེ་ཉིད་ཁམས་གསུམ་ཡིན་ནོ། །

[Block 3413]
དེ་ལ། འདོད་ཆགས་ཀུན་ཟད་འདོད་ཆགས་བྲལ།[^2383] །འདོད་ཆགས་སྤངས་པ་ནི་འདོད་ཆགས་དང་བྲལ་བའི་ཁམས་ཡིན་ནོ། །

[Block 3414]
སྤངས་པའི་ཁམས་ནི་གཞན་དག་གོ། །

[Block 3415]
ཡང་དག་པར་ཟད་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདོད་ཆགས་ལས་གཞན་པའི་ཉོན་མོངས་པ་རྣམས་སྤངས་པ་ནི་སྤངས་པའི་ཁམས་ཡིན་ནོ། །

[Block 3416]
འགོག་པའི་ཁམས་ཞེས་བྱ་བ་གཞི། །ཡང་དག་པར་ཟད་པ་ཞེས་བྱ་བ་ཁོ་ནར་སྦྱར་ཏེ། ཉོན་མོངས་པ་ལས་མ༌[^2384]གཏོགས་པ་བཞི་སྤངས་པ་ནི༌[^2385]འགོག་པའི་ཁམས་ཡིན་ནོ། །

[Block 3417 [HEADING]]
#### ཡིད་འབྱུང་བ་དང་འདོད་ཆགས་དང་བྲལ་བ། ^3-2-22-0

[Block 3418]
དངོས་པོ་གང་གིས་ཡིད་འབྱུང་བར་འགྱུར་བའི་དངོས་པོ་དེས་འདོད་ཆགས་དང་བྲལ་བར་ཡང་འགྱུར་རམ་ཞེ་ན། མུ་བཞིའོ། །ཇི་ལྟར་བྱས་པས་ཤེ་ན། སྡུག་བསྔལ་རྒྱུ་བཟོད་ཤེས་རྣམས་ཀྱིས། །ཡིད་འབྱུང་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་ལ་བཟོད་པ་དང་ཤེས་པ་རྣམས་ཁོ་ནས་ཡིད་འབྱུང་བར་འགྱུར་གྱི༌[^2386]གཞན་དག་གིས་ནི་མ་ཡིན་ནོ། །

[Block 3419]
གང་གིས་སྤོང་འགྱུར་བ། ཀུན་གྱིས་འདོད་ཆགས་བྲལ་བར་འགྱུར། །སྡུག་བསྔལ་དང༌[^2387]ཀུན་འབྱུང་བ་དང་འགོག་པ་དང་ལམ་ལ་བཟོད་པ་དང་ཤེས་པ་གང་དག་གིས་ཉོན་མོངས་པ་སྤོང་བར་འགྱུར་བ་ཐམས་ཅད་ཀྱིས་ཀྱང་འདོད་ཆགས་དང་བྲལ་བར་འགྱུར་རོ། །

[Block 3420]
དེ་ལྟ་ན༌[^2388]ནི་མུ་བཞི་སྲིད། དེ་ལྟ་ན་མུ་བཞིར་གྲུབ༌[^2389]སྟེ། སྡུག་བསྔལ་དང་ཀུན་འབྱུང་ལ་བཟོད་པ་དང་ཤེས་པ་རྣམས་ཀྱིས་ཉོན་མོངས་པ་དག༌[^2390]མི་སྤོང་ན་ཡིད་འབྱུང་བ་ཁོ་ན་ཡིན་ཏེ། ཡིད་འབྱུང་བའི་དངོས་པོ་ཁོ་ན་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3421]
འགོག་པ་དང་ལམ་ལ་བཟོད་པ་དང་ཤེས་པ་རྣམས་ཀྱིས་ཉོན་མོངས་པ་དག་སྤོང་ན་འདོད་ཆགས་དང་བྲལ་བ་ཁོ་ན་ཡིན་ཏེ། མཆོག་ཏུ་དགའ་བའི་དངོས་པོ་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3422]
སྔ་མ་རྣམས་ཀྱིས་ཉོན་མོངས་པ་དག་སྤོང༌[^2391]ན་གཉི་ག་ཡིན་ནོ། །

[Block 3423]
ཕྱི་མ་རྣམས་ཀྱིས་ཉོན་མོངས་པ་དག་མི་སྤོང་ན་གཉི་ག་མ་ཡིན་ནོ། །

[Block 3424]
དེ་ལ་འདོད་ཆགས་དང་བྲལ་བ་ཞིག་བདེན་པ་རྣམས་ལ་ལྟ་ན་ཆོས་ཤེས་པ་དང་བཟོད་པ་རྣམས་ཀྱིས་ཉོན་མོངས་པ་དག་མི་སྤོང་ངོ་། །ཤེས་པ་རྣམས་ཀྱིས་ནི་སྦྱོར་བ་དང་རྣམ་པར་གྲོལ་བ་དང་ཁྱད་པར་ཅན་གྱི་ལམ་གྱིས༌[^2392]བསྡུས་པ་རྣམས་ཀྱིས་མི་སྤོང་ངོ་། །[^2393]ཆོས་མངོན་པ་མཛོད་ཀྱི༌[^2394]བཤད་པ་ལས་ལམ་དང་གང་ཟག་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་དྲུག་པའོ།། །།

[Block 3425 [HEADING]]
## ཡེ་ཤེས་བསྟན་པ། ^4-0

[Block 3426 [HEADING]]
### ཤེས་པ་དང་ལྟ་བ། ^4-1-0

[Block 3427]
བཟོད་པ་རྣམས་ཞེས་ཀྱང་འབྱུང་།[^2395] ཤེས་པ་རྣམས་ཞེས་ཀྱང་འབྱུང་། ཡང་དག་པའི་ལྟ་བ༌[^2396]ཞེས་ཀྱང་འབྱུང་། ཡང་དག་པའི་ཤེས་པ་ཞེས་ཀྱང་འབྱུང་ན་ཅི་བཟོད་པ་དག་ཡིན་ལ་ཤེས་པ་མ་ཡིན་ནམ། ཡང་དག་པའི་ཤེས་པ་ཡིན་ལ་ཡང་དག་པའི་ལྟ་བ་མ་ཡིན་ནམ་ཞེ་ན། དྲི་མེད་བཟོད་རྣམས་ཤེས་པ་ཡིན། །དེས༌[^2397]སྤང་བར་བྱ་བའི་ཕྲ་རྒྱས་ཐེ་ཚོམ་མ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 3428]
དེ་དག་ཡང་དག་པར་རྟོག་པའི༌[^2398]བདག་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་ལྟ་བ་དག་ཡིན་ནོ། །

[Block 3429]
ཇི་ལྟར་བཟོད་པ་རྣམས་ལྟ་བ་ཡིན་གྱི༌[^2399]ཤེས་པ་མ་ཡིན་པ་དེ་བཞིན་དུ། ཟད་དང་མི་སྐྱེའི༌[^2400]བློ་ལྟ་མིན། །ཟད་པ་ཤེས་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་ནི་ཡང་དག་པའི་རྟོག་པ༌[^2401]མེད་པ་དང་། ཡོངས་སུ་འཚོལ༌[^2402]བའི་བསམ་པ་ཅན་མ་ཡིན་པའི་ཕྱིར་ལྟ་བ་མ་ཡིན་ནོ། །

[Block 3430]
དེ་ལས་གཞན་འཕགས་བློ་གཉི་ག །བཟོད་པ་དང་ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་དག་ལས་གཞན་པ་ཟག་པ་མེད་པའི་ཤེས་རབ་ནི་ལྟ་བ་དང༌[^2403]ཤེས་པ་ཡང༌[^2404]ཡིན་ནོ། །

[Block 3431]
གཞན་ཤེས༌[^2405]འཇིག་རྟེན་པའི་ཤེས་རབ་ཐམས་ཅད་ནི་ཤེས་པ་ཁོ་ན༌[^2406]ཡིན་ནོ། །

[Block 3432]
དྲུག་ནི་ལྟ་བའང་ཡིན། །ལྟ་བ་ལྔ་དང་། འཇིག་རྟེན་པའི་ལྟ་བ་ཡང་དག་པའི་ལྟ་བ་སྟེ། འཇིག་རྟེན་པའི་ཤེས་པ་རྣམ་པ༌[^2407]དྲུག་ནི་ལྟ་བ་ཡིན་གྱི༌[^2408]གཞན་ནི་ལྟ་བ་མ་ཡིན་ནོ། །

[Block 3433]
འདི་དག་དང་གཞན་དག་ཀྱང་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 3434 [HEADING]]
### ཤེས་པ་བཅུ། ^4-2-0

[Block 3435]
ཇི་སྙེད་ཅིག་གིས་ཤེས་པ་ཐམས་ཅད་བསྡུས་ཤེ་ན། ཤེས་པ་བཅུས་བསྡུས་སོ། །
--- END BLOCKS ---
