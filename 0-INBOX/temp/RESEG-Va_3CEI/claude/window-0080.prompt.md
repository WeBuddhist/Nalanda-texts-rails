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
[Block 2801]
དེ་ལྟར་རོ་གཅིག་གིས་སོ་སོར་སྨིན་པ་དང་། ཤིང་དང་འབྲས་བུ་སོ་སོར་བརླན་པ་ཡང༌[^2389]བདག༌[^2390]སོ་སོ་ནས་སེམས་པ༌[^2391]མེད་དོ། །

[Block 2802]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེ་ན། འོད་སྲུངས་ཞེས་པ་ནས་ཇི་ལྟ་བ་བཞིན་དུ་གཟིགས་སོ་ཞེས་པའི་བར་དུ་ནི་དེ་ལའང་སེམས་ཅན་གྱི་སྤྱོད་པ་སྤྱིར་མཁྱེན་པ་དང་། སོ་སོར་མཁྱེན་པ་དང་། མཁྱེན་པ་དེ་གཉིས་བསྡུ་བའོ། །

[Block 2803]
སེམས་ཅན་དེ་དག་ཅི་ལྟ་བ་བཞིན་དུ་མཁྱེན་པ་ནི་འདུས་བྱས་སམ། འདུས་མ་བྱས་ཀྱི་ཚུལ་དུའམ། སྤྱོད་པའམ། སེམས་ཀྱི་སྒོ་ནས་ཇི་ལྟ་བ་བཞིན་དུ་མཁྱེན་པའོ། །

[Block 2804]
ཅི་ལ་སེམས་ཞེས་པ་དག་ནི་མཁྱེན་པ་སོ་སོར་སྨོས་པ་སྟེ། ཤེས་རབ་རྣམ་གསུམ་གྱི་སྒོ་ནས་རང་བཞིན་མཁྱེན་པ་དང་། སྤྱོད་པ་དང་། དངོས་པོ་མཁྱེན་པ་དང་། སྤྱོད་པ་གང་གིས་འབྲས་བུ་ཅི་འཐོབ་པ༌[^2392]དང་། ལུང་གང་གིས་འབྲས་བུ༌[^2393]ཅི་སྒྲུབ་པ་སྟེ། ཆོས་དེ་བཞིའི་རིམ་པ་བཅོམ་ལྡན་འདས་ཀྱིས་མཁྱེན་ཞེས་པའོ། །

[Block 2805]
མངོན་སུམ་དུ་གཟིགས་པ་དང་། ཇི་ལྟ་བ་བཞིན་དུ་གཟིགས་པ་ནི་མཁྱེན་པ་དེ་དག་བསྡུ་བ་སྟེ། སེམས་ཅན་གྱི་གཞི་དང་། སེམས་ཀྱི༌[^2394]སྤྱོད་པ་མཚན་མ་དང་། དངོས་པོ་དང་། རང་བཞིན་མ་ལུས་པར་གཟིགས་པའི་ཕྱིར་གཟིགས་པའོ། །

[Block 2806]
མདོ་ལས་དེ་དང་དེ་དག་ན་གནས་པའི་སེམས་ཅན་དེ་རྣམས་ཞེས་པ་ནས་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་གློ་བུར་དུ་མི་སྟོན་ཏོ་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པའི་མཁྱེན་པ་དང་། སེམས་ཅན་གྱི་མཁྱེན་པ་ཤེས་པ་དེ་གཉིས་བསྡུ་བའི་ཁྱད་པར་བསྟན་པ་སྟེ། དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ཟབ་པ་དང་། སེམས་ཅན་གྱི་ཤེས་པ་ཆུང་བར་གྱུར་པས། དེ་བཞིན་གཤེགས་པའི་བསྟན་པ༌[^2395]ཟབ་མོའི་གནས་མ་ཡིན་པར་བསྟན་པའོ། །

[Block 2807]
མདོ་ལས་འོད་སྲུངས་དེ་བཞིན་གཤེགས་པས་ལྡེམ་པོ་ངག་ནི་བཤད་པ་ལ་ཞེས་པ་ནས་ལྡེམ་པོ་ངག་ནི་ཤེས་པར་དཀའོ་ཞེས་པའི་བར་དུ་ནི་འོད་སྲུངས་ཆེན་པོས་ཟབ་མོ་འདི་ཤེས་ཀྱི་གཞན་གྱིས་མི་ཤེས་ཏེ། མཚན་ཉིད་ནི་འོག་ནས་སྟོན་ཏོ། །

[Block 2808 [HEADING]]
##### ཚིགས་སུ་བཅད་པས་དོན་གོང་མ་བཟླས་ཏེ་སྟོན་པ། ^4-5-4-4-0

[Block 2809]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2396]དེའི་ཚེ་ཞེས་པ་ནས་ཤིན་ཏུ་དད་པ་ཤེས་ནས་སུ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་སུ་བཅད་པས་དོན་གོང་མ༌[^2397]རྣམས་བཟླས་ཏེ་སྟོན་པ་ལ། ཚིགས་བཅད་ལྔ་བཅུ་རྩ་གཅིག་གིས་ནི་གོང་མའི་དོན་བཟླས་འོག་མ་གཅིག་གིས་ནི་བསྡུས་པའི་དོན་བསྟན་ཏོ། །

[Block 2810]
ཆོས་རྒྱལ་ཞེས་པ་ནི་ཆོས་ལ་མངའ་བརྙེས་པས་ཆོས་ཅི་སྟོན་པ་འཁྲུལ་པ་མི་མངའ་བའི་ཕྱིར་ཆོས་ཀྱི་རྒྱལ་པོའོ། །

[Block 2811]
འབྱུང་བ་འཇོམས་ཞེས་པ་ནི་འཇིག་རྟེན་གསུམ་འཇོམས་པའམ། སྲིད་པ་བཞི་དང་ལྔ་འཇོམས་ཞེས་པའི་དོན་ཏོ། །

[Block 2812]
ཡང་ན་ཚིགས་བཅད་བཞི་པོ་འདི་ལ་ཆོས་ཀྱི་སྐུ་དང་། རྫོགས་པ༌[^2398]ལོངས་སྤྱོད་པའི་སྐུ་དང་། སྤྲུལ་པའི་སྐུ་རིམ་པ་བཞིན་དུ་སེམས་ཅན་གྱི་དོན་མཛད་པར་སྦྱར་རོ། །

[Block 2813]
མདོ་ལས།

[Block 2814]
དབང་པོ༌[^2399]ཆེན་པོ་བློ་བརྟན༌[^2400]པ། །ཞེས་པ་ནས། སྲོག༌[^2401]ཆགས་རྣམས་ལ་མི་སྨྲའོ། །ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པ༌[^2402]ཆོས་སྟོན་པ་ངོ་མཚར་དུ་བྱ་བ་སྟེ། བཀྲི་བ་དང་ངེས་པའི་དོན་བཤད་པ་ལ་སོ་སོའི་དབང་པོ་དང་སྦྱར་ཏེ། གཟོད་འཆད་ཀྱི་གློ་བུར་དུ་མི་གསུང་ཞེས་པའི་དོན་ཏོ། །

[Block 2815]
མདོ་ལས།

[Block 2816]
ཡེ་ཤེས་དེ་ནི་ཆུད་དཀའ་བ། །ཞེས་པ་ནས། །དེ་ལྟ་བས་ན་འཁོར་བའོ། །ཞེས་པའི་བར་དུ་ནི་སོ་སོ་ནས་ཐེ་ཚོམ་དང་། དོགས་པ་སྐྱེ་བས་ཆུད་དཀའ་བས་མ་བཤད་ཅེས་པའི་དོན་ཏོ། །

[Block 2817]
མདོ་ལས་བཤད་པ་ཚིག་འདྲ་ཡུལ་དང་ཞེས་པ་ནས། ལྟ་བ་དག་ནི་དྲང་པོར་བྱ། །ཞེས་པའི་བར་དུ་ནི་སེམས་ཅན་རྣམས་དེ་བཞིན་གཤེགས་པའི་གསུང་དང་བྱིན་གྱི་རླབས༌[^2403]ཀྱིས་མ་བསྟན་པར་རང་གིས་རིག་པའི་བློ་མི་སྐྱེ་བས་ཡང་དག་པའི་དོན་བཅོམ་ལྡན་འདས་ཀྱིས་རྣམ་པར་ཕྱེ་བས་སེམས་ཅན་རྣམས་དབང་པོ་ཇི་ལྟ་བ་བཞིན་དུ་དོན་རྟོགས་ཤིང་རིག་པ་སྐྱེ་ཞེས་པའི་དོན་ཏོ། །

[Block 2818]
མདོ་ལས།

[Block 2819]
འོད་སྲུངས་སྤྲིན༌[^2404]ནི་ཇི་ལྟ་བུ།[^2405] །ཞེས་པ་ནས། ཐམས་ཅད་དུ་ནི་ཆུ་ཡང་གཏོང་། ། ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པ་འཇིག་རྟེན་དུ་འབྱུང༌[^2406]སྟེ། ཆོས་སྟོན་པ་ཡང་ཇི་ལྟར་འཇིག་རྟེན་དུ་བྱུང་སྟེ༌[^2407]ཆར་འབབ་པ་ཀླུའི་རྒྱལ་པོས་ཞག་བདུན་གྱི་བར་དུ་སྤྲིན་བསྡུས་ནས་ཆར༌[^2408]འབེབས་པ་བཞིན་དུ་ཐུགས་རྗེ་ཆེན་པོའི་སྤྲིན་ཕྱོགས་བཅུ་ཐམས་ཅད་དུ་ཁེབས་པར་མཛད་དེ། སེམས་ཅན་གྱི་དབང་པོ་སྨིན་པའི་དུས་དང་སྦྱོར་ཞིང་ཆོས་སྟོན་ཏོ། །

[Block 2820]
སྤྲིན་དེ་ཡང་གློག་གི་ཕྲེང་བ་དང་བཅས་པ་འབྲུག་གི་སྒྲ་གྲག་པ༌[^2409]ཉི་མའི་འོད་སྒྲིབ་པ། དཀྱིལ་འཁོར་ཐམས་ཅད་བསིལ་བར་བྱེད་པ་ལག་གིས༌[^2410]བརྙབ་ཏུ༌[^2411]རུང་བ་འདྲ་བར་འདུག་པ་བཞིན་དེ་བཞིན་གཤེགས་པའི་འོད་ཀྱིས་ཕྱོགས་བཅུར་སྣང་བར་མཛད་པ། ཆོས་ཀྱི་འབྲུག་སྒྲ་སྒྲོགས༌[^2412]པས་བདུད་དང་ལོག་པར་ལྟ་བ་རྣམས་དངང༌[^2413]བར་མཛད་པ། ཐུགས་རྗེའི་སྤྲིན་གྱིས་ཕྱོགས་ཐམས་ཅད་དུ་ཁེབས་པས་འགྲོ་བ་དགའ་བར་མཛད་པ། ལོག་པའི་ཉི་མ་འཆར་བ་ཟིལ་གྱིས་གནོན་པ། སྡུག་བསྔལ་གྱི་གནས་ཐམས་ཅད་བསལ་ཏེ། མྱ་ངན་ལས་འདས་པའི་གནས་བསིལ་བར་མཛད་པ། ཐུགས་རྗེའི་ལྷུན་ལུས་དང་སེམས་འདུན་པའི་ལག་གིས་བརྙབ་ཏུ་རུང་བ་ཙམ་དུ་སེམས་པའོ། །

[Block 2821]
མདོ་ལས།

[Block 2822]
དེ་ནི་སྙོམས་པར༌[^2414]འབེབས་པ་ཡང་།[^2415] །ཞེས་པ་ནས། སྡོང༌[^2416]པོར་གྱུར་པ་གང༌[^2417]ཡང་རུང་།[^2418] །ཞེས་པའི་བར་དུ་ནི་སོ་སོར་སྨིན་པར་བྱེད་པ་ལ་ཡོན་ཏན་གྱི་ཆར་འབེབས་པ་དང་། དངོས་པོ་སོ་སོར་སྐྱེས་པ་དང་། སྐྱེས་པ་རྣམས་དོན་དུ་འགྱུར་བར་མཛད་པ་སྟེ། མཐོ་དམན༌[^2419]མེད་པར་སྙོམས་པའི་ཐུགས་རྗེས་ཀུན་གྱི༌[^2420]དོན་མཛད་ཅེས་པར་སྦྱར་རོ། །

[Block 2823]
མདོ་ལས།

[Block 2824]
དེ་དང་སྨན་ལྗོངས༌[^2421]རྣམས་ནས་སམ། །ཞེས་པ་ནས། འབྲས་བུ་མེ་ཏོག་རྣམས་ཀྱང་དེ་བཞིན་འཕེལ།[^2422] །ཞེས་པའི་བར་དུ་ནི་བརླན་པར་བྱ་བའི་དངོས་པོ་བསྟན་ཏེ། དེ་ཡང་སྤྱི་དང་ཁྱད་པར་དུ་དབྱེ་བའོ། །

[Block 2825]
ཐེག་པ་རྣམ་གསུམ་རིགས་སོ་སོར་སྨིན་པ་ནི་སྡོང་པོ་དང་ཡལ་ག༌[^2423]མེ་ཏོག་བཞིན་ནོ། །

[Block 2826]
མདོ་ལས།

[Block 2827]
སྤྲིན་གྱི་ཆར་གྱིས་མང་པོ་སྨན་རྣམས་ལ། །ཞེས་པ་ནས། དེ་ནི་ཆར་པ་རོ་གཅིག་ཕབ་པའོ། །ཞེས་པའི་བར་དུ་ནི་བརླན་པར་བྱ་བ་རྣམས་དོན་དུ་སྒྲུབ་སྟེ། སོ་སོར་སྨིན་པར་བྱེད་པའི་དཔེའོ། །

[Block 2828 [HEADING]]
###### དཔེ་དང་དོན་དུ་སྦྱོར་བ། ^4-5-4-4-1-0

[Block 2829]
མདོ་ལས།

[Block 2830]
དེ་བཞིན་འོད་སྲུངས་སངས་རྒྱས་འཇིག་རྟེན་འདིར། །ཞེས་པ་ནས། སྲོག་ཆགས་ལ་ནི་ཡང་དག་སྤྱོད་པ་སྟོན།[^2424] །ཞེས་པའི་བར་དུ་ནི༌[^2425]དཔེ་དང་དོན་དུ་སྦྱར་བ་སྟེ། ཚིག་དང་པོ་གཉིས་ཀྱིས་ནི་སྦྱོར་བ་བསྟན། གཞན་གྱིས་ནི་འབྲས་བུ་མི་མཐུན་པ་བསྟན་ཏེ། འདི་ནི་དང་པོའོ། །

[Block 2831 [HEADING]]
###### འབྲས་བུ་མི་མཐུན་པ། ^4-5-4-4-2-0

[Block 2832]
མདོ་ལས།

[Block 2833 [HEADING]]
###### **ཆེད་དུ་བསྒྲགས་པ།** ^4-5-4-4-2-1-0

[Block 2834]
དེ་ལྟར་དྲང་སྲོང་ཆེན་པོ་ཡང་དག་སྒྲོག །ཅེས་པ་ནས། ངས་ནི་འདོད་དང་མྱ་ངན་འདའ་བ་སྦྱིན། །ཞེས་པའི་བར་དུ༌[^2426]འདིས་ནི་འབྲས་བུ་སོ་སོར་བརླན་པ་བསྟན་ཏེ། འདི་མན་ཆད་ཆེད་དུ་བསྒྲགས་པ་དང་།[^2427] འཁོར་བསྡུ་བ་དང་ཕན་གདགས་ཤིང་དྲང་བ་ཐོས་པ་རྣམས་ཕན་པ་འཐོབ་པ་དང་། དེ་ཐོས་ནས་འདུ་བ་སྟེ་འདི་ནི་དང་པོའོ། །

[Block 2835]
རིགས་ཡོད་དུ་ཟིན་གྱིས་ཀྱང་དམ་པའི་ཆོས་ཀྱིས་མ་བརླན་པའི་ཕྱིར་ལུས་བསྐམས་པའོ། །

[Block 2836 [HEADING]]
###### **འཁོར་བསྡུ་བ།** ^4-5-4-4-2-2-0

[Block 2837]
མདོ་ལས།

[Block 2838]
ལྷ་དང་མི༌[^2428]ཚོགས་རྣམས་ཀྱང་ང༌[^2429]ལ་ཉོན། ངལ་ལྟ་བའི་ཕྱིར་ནི་ཉེ་བར་གཤེགས། །ཞེས་པས༌[^2430]འཁོར་བསྡུ་བའོ། །

[Block 2839 [HEADING]]
###### **ཕན་གདགས་ཤིང་དྲང་བ།** ^4-5-4-4-2-3-0

[Block 2840]
མདོ་ལས།
--- END BLOCKS ---
