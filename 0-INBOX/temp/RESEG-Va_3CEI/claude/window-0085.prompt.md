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
[Block 2976 [HEADING]]
###### **སྔ་མའི་དུས།** ^4-6-4-2-3-1-1-1-0

[Block 2977]
ལུང་བསྟན་པ་ཡང་སྔ་མའི་དུས་དང་ཕྱི་མའི་དུས་སོ། །

[Block 2978 [HEADING]]
###### **སངས་རྒྱས་མངོན་དུ་བཞུགས་པ།** ^4-6-4-2-3-1-1-1-1-0

[Block 2979]
སྔ་མའི་དུས་ལ་ཡང་སངས་རྒྱས་མངོན་དུ་བཞུགས་པ་དང་། མྱ་ངན་ལས་འདས་པ་སྟེ། འདི་ནི་སྔོན་དུ༌[^2522]བཞུགས་པ་དང་སྦྱར་རོ། །

[Block 2980 [HEADING]]
###### **མྱ་ངན་ལས་འདས་པ།** ^4-6-4-2-3-1-1-1-2-0

[Block 2981]
མདོ་ལས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་དེ་དག་ཡོངས་སུ་མྱ་ངན་ལས་འདས་ནས་ཀྱང་ཞེས་པ་ནས་རྣམ་པ་མང་པོས་མཆོད་པ་བྱེད་དོ་ཞེས་པའི་བར་དུ་ནི། མྱ་ངན་ལས་འདས་པའི་འོག་ཏུ་བཀུར་སྟི་བྱེད་པ་སྟེ། སྔར་མཆོད་རྟེན༌[^2523]བརྩིགས་པ་དང་། དེའི་འོག་ཏུ་མཆོད་པ་བྱས་པའོ། །

[Block 2982 [HEADING]]
###### **ཕྱི་མའི་དུས།** ^4-6-4-2-3-1-1-2-0

[Block 2983]
མདོ་ལས་དེའི་ཕ་རོལ་གྱི༌[^2524]ཡང་ཕ་རོལ་ཏུ་ཞེས་པ་ནས་གསོལ་བར་བྱེད་དོ་ཞེས་པའི་བར་དུ་ནི་ཕྱི་མའི་རྒྱུ་བསྟན་ཏོ། །

[Block 2984 [HEADING]]
###### **འབྲས་བུ།** ^4-6-4-2-3-1-2-0

[Block 2985]
མདོ་ལས་དེའི་འོག་ཏུ་ལུས་ཐ་མ་ལ་ཞེས་པ་ནས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཏེ་ཞེས་པའི་བར་དུ་ནི་དངོས་སུ་འབྲས་བུ་བསྟན་པའོ། །

[Block 2986]
མདོ་ལས་དེའི་སངས་རྒྱས་ཀྱི་ཞིང་ཡིད་མངོན་པར་དགའ་བ་ཞེས་བྱ་བར་འགྱུར་ཞེས་པ་ནས་མེ་ཏོག་སིལ་མ༌[^2525]གཏོར་བ་ཞེས་པའི་བར་དུ་ནི་བསྐལ་པའི་མིང་དང་། རྒྱུའི་མིང་དང་། ཞིང་གི་མཚན་ཉིད་ཀྱི་རྒྱན་བསྟན་པའོ། །

[Block 2987]
མདོ་ལས་ཞིང་མང་པོས་རབ་ཏུ་གང་ཞེས་པ་ནས། དམ་པའི་ཆོས་ཀྱི་གཟུགས་བརྙན༌[^2526]གནས་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་དགེ་བ་མང་པོ༌[^2527]བསྐྱེད་པ་དང་། འཁོར་དང་། ཚེའི་ཚད་དང་གྲངས་བསྟན་པའོ། །

[Block 2988 [HEADING]]
###### **ཚིགས་སུ་བཅད་པས་བསྡུ་བ།** ^4-6-4-2-3-2-0

[Block 2989 [HEADING]]
###### **རྒྱུ།** ^4-6-4-2-3-2-1-0

[Block 2990]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱི༌[^2528]དེའི་ཚེ་ཞེས་པ་ནས་སིལ་སྙན་གྱིས་ནི་འཇིག་རྟེན་ཕན་སྐྱོང་བའོ༌[^2529]ཞེས་པའི་བར་དུ་ནི་འདིས་ཡོངས་སུ་ལུང་བསྟན་པ་སྟེ། སྔར་ནི་རྒྱུ་བསྟན་ཕྱིས་ནི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 2991]
རྒྱུ་བསྟན་པ་ལ་ཡང་སངས་རྒྱས་འཇིག་རྟེན་ན་བཞུགས་པ་དང་། འཇིག་རྟེན་ནས་འདས་པ་ལ་མཆོད་པ་བྱེད་པའོ། །

[Block 2992]
མྱ་ངན་ལས་འདས་ཞེས་པ་ནི་མྱ་ངན་ལས་འདས་པའི་འོག་ཏུ་མཆོད་པ་བྱེད་པའོ། །

[Block 2993 [HEADING]]
###### **འབྲས་བུ།** ^4-6-4-2-3-2-2-0

[Block 2994]
དེ་ནས་འདི་ལྟར་ཐ་མར་ལུས་ཀྱི་ཚེ་ཞེས་པ་ནས་འདི་མན་ཆད་བཤད་པའི་ཚུལ་གོང་མ་དག་དང་འདྲ་བར་དབྱེའོ།། །།

[Block 2995 [HEADING]]
### སྔོན་བྱུང་བའི་ལེའུ། ^4-7-0

[Block 2996]
འདི་མན་ཆད་སྔོན་བྱུང་བའི་ལེའུ་འཆད་དེ། སྔོན་དེ་བཞིན་གཤེགས་པས༌[^2530]སངས་རྒྱས་ཀྱི༌[^2531]མཛད་པ་མཛད་ཅིང་ཐེག་པ་ཆེན་པོའི་དོན་སྤྱོད་པ་དེ་བསྟན་ན་རྗེས་སུ་འཇུག་པ་བསྐྱེད་པའི༌[^2532]ཕྱིར་རྒྱུ་དེ་བསྟན་ཅིང་མོས་པ་སྐྱེ་བར་བྱ་བའི་ཕྱིར་ལེའུ་འདི་བསྟན་ཏོ། །

[Block 2997 [HEADING]]
#### ཅི་ལས་བཏགས་པ། ^4-7-1-0

[Block 2998]
འདི་ཅི་ལས་བཏགས་པ༌[^2533]དང་། དེའི་མིང་དང་། དེ་དྲིས་པའི་ལན་རྣམ་པ་གསུམ་ཞིག་སྟོན་ཏེ། འདིའི་ནང་ནས་སྔར་དབང་པོ་རྣོན་པོ་དང་བར་མ་ཆོས་ཐོས་པས་རྟོགས་པ་སྐྱེས་ཏེ་ལུང་བསྟན། དབང་པོ་ཐ་མ་རྣམས་ཆོས་ཐོས་ཀྱང་ད་དུང་རྟོགས་པ་མ་སྐྱེས་པ་རྣམས་སྔོན་ཐེག་པ་ཆེན་པོའི་སྤྱོད་པ་ལ་ཞུགས་པ་རྣམས་ཇི་ལྟར་སྤྱོད་པའི་དཔེ་བསྟན་ན། རྟོགས་པ་སྐྱེ་བར་འགྱུར་བས་སྤྲུལ་པའི་གྲོང་ཁྱེར་གྱི༌[^2534]དཔེ་བསྟན་པ་དང་། འགྲེལ་པ་ལས་སེམས་ཅན་ང་རྒྱལ་ཅན་བདུན་ཡོད་དེ། ང་རྒྱལ་གྱི་ཉོན་མོངས་པ་དེ་སྤང་བའི༌[^2535]ཕྱིར་འདི་གསུངས་ཏེ། ང་རྒྱལ་དེ་བདུན་ལས་ཀྱང༌[^2536]

[Block 2999]
བཞི་པ་ལྟ་བུ་བསམ་གཏན་སྤྱོད་ཅིང་འཇིག་རྟེན་གྱི་ཏིང་ངེ་འཛིན་ལ་གནས་པ་ཉིད་མྱ་ངན་ལས་འདས་པ་ཙམ་དུ་སེམས་པ་དེའི་གཉེན་པོར་སྤྲུལ་པའི་གྲོང་ཁྱེར་གྱི་དཔེ་བསྟན། ཏིང་ངེ་འཛིན་ལ་གནས་ཤིང་འབྲས་བུ་ཆུང་ངུས་ཆོག་པར་སེམས་པ་དེ་ལ་ཐེག་པ་ཆེན་པོའི་མྱ་ངན་ལས་འདས་པའི་གྲོང་ཁྱེར་ཆེན་པོ་ལ་ཐབས་ཀྱིས་གཟུད་པའི་ཕྱིར་སྔོན་གྱི་གཏམ་གྱི་གྲོང་ཁྱེར་གྱི་དཔེ་བསྟན་ན། སློབ་པ་ལ་གནས་པའི་མ་རབས་རྣམས་སྤྲུལ་པའི་གྲོང་ཁྱེར་བསྟི་བའི་གནས་ཙམ་དུ་བསྟན་ནས་ཀྱང་མྱ་ངན་ལས་འདས་པའི་གྲོང་ཁྱེར་ཆེན་པོ་རིན་པོ་ཆེའི་འབྱུང་གནས་ཉིད་དུ་གཟུད་པའི་ཕྱིར་དཔེ་འདི་བསྟན་ཏོ། །

[Block 3000]
བླ་ན་མེད་པ་བཅུ་བསྟན་པའི་ནང་ནས་གཉིས་པ་སྟེ། སྔོན་གྱི་སྤྱོད་པ་བླ་ན་མེད་པ་སྟོན་པ་དང་སྦྱར་ན་དེ་བཞིན་གཤེགས་པ་མངོན་པར་ཤེས་པ་ཆེན་པོའི་ཡེ་ཤེས་ཀྱི༌[^2537]ཟིལ་གྱིས་གནོན་པ་ཞེས་བྱ་བ་བྱང་ཆུབ་ཀྱི་སྤྱོད་པ་དགའ་བ༌[^2538]སྤྱོད་པའི་ཚེ་བསྐལ་པ་མང་པོ་ཞིག་ཏུ་སྤྱད་ནས་གཟོད༌[^2539]མངོན་པར་སངས་རྒྱས་པ་དང་སྦྱར་ན་ཐེག་པ་པའི༌[^2540]བྱང་ཆུབ་ཏུ་ཉེ་བས་ཐོབ་པ་ཉིད་བསྟི་བའི་གནས་ཡིན་པར་བསྟན་པའོ། །

[Block 3001]
ཡང་བླ་ན་མེད་པ་བཅུའི་གསུམ་པ་ལས་ལྷག་པའི་བརྩོན་འགྲུས་ཀྱི་མཐུས་བསྐྱེད་པ༌[^2541]དང་སྦྱར་ན༌[^2542]ཚོང་དཔོན་གྱི་དཔེས་དཀའ་བ་སྣ་ཚོགས་སྤྱད་ནས་དོན་གྲུབ་པ་བཞིན་དེ་བཞིན་གཤེགས་པའི་འབྲས་བུ་ཐོབ་པ་ཡང་དེ་དང་འདྲ་བར་སྦྱར་རོ། །

[Block 3002 [HEADING]]
#### མིང། ^4-7-2-0

[Block 3003]
ལེའུ་འདིའི་ནང་ནས་དེ་བཞིན་གཤེགས་པ་མངོན་པར་ཤེས་པ་ཆེན་པོའི་ཡེ་ཤེས་ཀྱི་ཟིལ་གྱིས་གནོན་པའི་སྤྱོད་པ་སྟོན་ན་བཅོམ་ལྡན་འདས་དེའི་མཚན་ལས་ལེའུ་འདིའི་མིང་དུ་གདགས་པའི་རིགས་ནས་སྤྲུལ་པའི་གྲོང་ཁྱེར་དང་སྔོན་བྱུང་བ་ཞེས་ཅིའི་ཕྱིར་གདགས།

[Block 3004 [HEADING]]
#### དྲིས་པའི་ལན། ^4-7-3-0

[Block 3005]
དེ་ནི་ལྷག་པའི་ང་རྒྱལ་ཅན་དག་མྱ་ངན་ལས་འདས་པ་ཉིད་ཐོབ་པར་སེམས་པའི༌[^2543]གཉེན་པོར་གྲོང་ཁྱེར་གྱི་དཔེས་ཆེད་དུ་བཟློག་པའི་ཕྱིར་དེ༌[^2544]བསྟན་པས་དོན་ལ་དྲིས༌[^2545]ཏེ་བཏགས་སོ། །

[Block 3006 [HEADING]]
#### དབང་པོ་ཐ་མ་ལ་བསྟན་པའི་གླེང་བ། ^4-7-4-0

[Block 3007 [HEADING]]
##### ཚིག་རྐྱང་པས་རྒྱས་པ་བསྟན་པ། ^4-7-4-1-0

[Block 3008 [HEADING]]
###### ཕྱོགས་སུ་བསྒོ་བ། ^4-7-4-1-1-0

[Block 3009]
མདོ་ལས་དགེ་སློང་རྣམས་སྔོན་འདས་པའི་དུས་ན་བྱུང་བ་ཞེས་པ་ནས་ཕ་རོལ་གྱི༌[^2546]ཡང་ཕ་རོལ་ན་ཞེས་པའི་བར་དུ་ནི་འདིས་དབང་པོ་ཐ་མ་ལ་བསྟན་པའི་གླེང་བ་སྟེ། སྔར་ཚིག་རྐྱང་པས་རྒྱས་པ༌[^2547]བསྟན། དེའི་འོག་ཏུ་ཚིགས་བཅད་ཀྱིས་བསྡུ་བ་སྟེ། དེ་ལ་ཡང་དང་པོར་ཕྱོགས་སུ་བསྒོ་བ་དང་། དེའི་འོག་ཏུ་དྲིས་པའི་ལན་ནོ། །

[Block 3010]
དང་པོ་ལ་ཡང་རྣམ་པ་བཞི་སྟེ། དུས་དང་། ཡུན་དང་། ཡུལ་དང་། བསྐལ་པ་སྟེ་འདི་ནི་དང་པོའོ། །

[Block 3011]
མདོ་ལས་འདི་ལྟར༌[^2548]སྔོན་དེའི་ཚེ་དེའི་དུས་ཞེས་པ་ནས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་སོ་ཞེས་པའི་བར་དུ་ནི་དངོས་སུ་བསྟན་པའོ། །

[Block 3012 [HEADING]]
###### དྲིས་པའི་ལན། ^4-7-4-1-2-0

[Block 3013]
མདོ་ལས་དགེ་སློང་དག་དེ་བཞིན་གཤེགས་པ་དེ་བྱུང་ནས་ཞེས་པ་ནས་སའི་ཁམས་དེ་ཐམས་ཅད་བཏགས༌[^2549]ན་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་དྲིས་པ་དང་། ལན་གདབ་པ་སྟེ། འདི་ནི་དྲིས༌[^2550]པའོ། །

[Block 3014]
མདོ་ལས་དགེ་སློང་རྣམས་དེ་ཡིད་ལ་ཇི་སྙམ་ཞེས་པ་ནས་བཅོམ་ལྡན་འདས་དེ་མ་ལགས་སོ་ཞེས་པའི་བར་དུ་ནི་དྲིས་པའི་ལན་བཏབ་པའོ། །

[Block 3015]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཀྱི༌[^2551]ཞེས་པ་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་བཞིན་ནོ་ཞེས་པའི་བར་དུ་ནི་འདིས་ནི་མངོན་པར་ཤེས་པ་ཆེན་པོ་སྟོན་ཏེ། ཡེ་ཤེས་ཀྱི་གཟིགས་པས་མཁྱེན་ཞེས་པའོ། །
--- END BLOCKS ---
