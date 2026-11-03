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
[Block 3046]
བཅོམ་ལྡན་འདས་ཀྱི་གན་དུ་འགྲོ་བ་ཡང་སོ་སོའི་འཁོར་དང་གཉེན་དུ་བཅས་ཏེ་དོང་བ་བསྟན་ཏོ། །

[Block 3047]
མདོ་ལས་འདི་ལྟར་དགེ་སློང་རྣམས་རྒྱལ་བུ་གཞོན་ནུ་བཅུ་དྲུག་པོ་དེ་དག་ཅེས་པ་ནས་གང་ན་བ༌[^2570]དེར་དོང་ངོ་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཀྱི་གན་དུ་ཆས་པ་བསྟན་ཏོ། །

[Block 3048 [HEADING]]
###### **བསྟོད་དེ་མངོན་པར་གསོལ་བ།** ^4-7-6-1-1-2-0

[Block 3049]
མདོ་ལས་བཅོམ་ལྡན་འདས་འདི་ལ་བཀུར་སྟི་བྱས་ཞེས་པ་ནས། ཁྱོད་ནི་རབ་ཞི་ཟག་པ་མེད་ལ་གནས་ནས་ཞེས་པའི་བར་དུ་ནི་ཕྱག་འཚལ་བ་ནི་ལུས་ཀྱིས༌[^2571]ཕྱག་འཚལ་བ་དང་། ངག་གིས་བསྟོད་དེ་ཕྱག་འཚལ་བའོ། །

[Block 3050]
བཅོམ་ལྡན་འདས་ལ་བསྟོད་པ་ཡང་དགོངས་པའི་སྨོན་ལམ་རྫོགས་པའི་སྒོ་ནས་བསྟོད་པ་དང་། སྔོན་མཛད་པའི་ཡོན་ཏན་གྱི་སྒོ་ནས་བསྟོད་པའོ། །

[Block 3051]
སྟན་གཅིག་དེ་ལ་བཞུགས༌[^2572]ཏེ་ཞེས་པ་ནི་རྣམ་པ་བཅུ་སྟེ། འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོའི་ཚུལ་དུ་བཞུགས་པ་སྟེ་དགེ་བ་བཅུ་ལ་གནས་པ་དང་། རྒྱལ་པོ་བཞིའི་ཚུལ་དུ་བཞུགས༌[^2573]པ་སྟེ། འཇིག་རྟེན་པ་ཐམས་ཅད་ཀྱིས་དེ་བཞིན་གཤེགས་པའི་ཆོས་སྤྱད་པ་ལ་རང་དབང་ཡོད་པར་མོས་པས་གནས་པ་དང་། བརྒྱ་བྱིན་གྱི་ཚུལ་དུ་བཞུགས་པ༌[^2574]སྟེ་སེམས་ཅན་ཐམས་ཅད་ལ་དབང་དུ་གྱུར་པས་བཞུགས་པ་དང་། ཚངས་པའི་ཚུལ་གྱིས་བཞུགས་པ་སྟེ།[^2575] བདག་དང་གཞན་གྱི༌[^2576]སེམས་ལ་དབང་དུ་གྱུར་པས་བཞུགས་པ་དང་། སེང་གེ་བཞིན་ཟབ་མོ་སྟོན་པ་ལ་བསྙེངས་པ་མེད་པས་བཞུགས་པ་དང་། ཡང་དག་པའི་ཆོས་ལ་བཞུགས་པ་སྟེ། གཟུངས་དང་མཐུ་སྟོན་པར་བཞེད་པས་བཞུགས་པ་དང་། ཤིན་ཏུ་བརྟན་པའི་ཏིང་ངེ་འཛིན་དུ་བཞུགས་པ་སྟེ། བྱང་ཆུབ་ཆེན་པོའི་མཐའ་ལ་བཞུགས་པ་དང་། ཐུགས་རྗེ་ཆེན་པོ་ལ་གནས་པས་སེམས་ཅན་ཐམས་ཅད་དགའ་བ་བསྐྱེད་པ༌[^2577]དང་། ཐུགས་རྗེ་ཆེན་པོ་ལ་བཞུགས་པ་སྟེ། ཉོན་མོངས་པའི་སྡུག་བསྔལ་ཐམས་ཅད་བཟོད་པར་བཞུགས་པ༌[^2578]དང་། རྡོ་རྗེ་ལ་བཞུགས་པ་སྟེ། བདུད་དང་ལོག་པར་ལྟ་བ་ཐམས་ཅད་འཇོམས་པས་བཞུགས་པའོ། །

[Block 3052]
དེ་ལ་འདི་ནི་ཤིན་ཏུ་བརྟན་པའི༌[^2579]ཏིང་ངེ་འཛིན་དང་རྡོ་རྗེ་ལ་བཞུགས་པ་དང་སྦྱར་རོ། །

[Block 3053]
ཞི་བ་ཞེས་པ་ནི་སེམས་ཞི་བའོ། །

[Block 3054]
མི་གཡོ་བ་ཞེས་པ༌[^2580]ནི་ལུས་མི་གཡོ་བའོ། །

[Block 3055]
མདོ་ལས།

[Block 3056]
དགེ་བ་དང་ནི་བདེ་བ་དགའ་བ་དང་། །ཞེས་པ་ནས།[^2581] མི་དབང་སེང་གེ་བདག་ཅག་དགེ་བར་སྐྱེས། །ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་མངོན་པར་བྱང་ཆུབ་པས་འགྲོ་བ་ཐམས་ཅད་དགའ་བ་སྐྱེས་ཞེས་པའི་དོན་ཏོ། །

[Block 3057]
མདོ་ལས།

[Block 3058]
སྐྱེ་དགུ་འདི་ཀུན་མགོན་མེད་སྡུག་བསྔལ་བ། །ཞེས་པ་ནས། དེ་ན་རྒྱལ་བའི་སྒྲ་ཡང་ཐོས་པ་མེད། །ཅེས་པའི་བར་དུ་ནི་སེམས་ཅན་རྣམས་སྡིག་པའི་གྲོགས་པོ་དང་བསྟེན་པ༌[^2582]དང་། དགེ་བའི་བཤེས་གཉེན་དང་ཕྲད་པར་སྟོན་ཏོ། །

[Block 3059]
སྡུག་བསྔལ་ཞེས་པ་ནི་སྡུག་བསྔལ་གྱི་བདེན་པའོ། །

[Block 3060]
མི་ཤེས་ཞེས་པ་ནི་ལམ་གྱི་བདེན་པའོ། །

[Block 3061]
མུན་གནག་ཞེས༌[^2583]པ་ནི་ཀུན་འབྱུང་གི་བདེན་པའོ། །

[Block 3062]
ཐར་པ་ཞེས་པ་ནི་འགོག་པའི་བདེན་པ་སྟེ། དེ་མ་སྤངས་ཏེ༌[^2584]མངོན་དུ་མ་བྱས༌[^2585]ཞེས་པའི་དོན་ཏོ། །

[Block 3063]
མདོ་ལས།

[Block 3064]
འཇིག་རྟེན་རིག་པ༌[^2586]ཁྱོད་ཀྱིས་དེང༌[^2587]ཐོབ་པ། །ཞེས་པ་ནས། མགོན་པོ་ཁྱོད་ལ་རབ་ཏུ་སྐྱབས་སུ་མཆི། །ཞེས་པའི་བར་དུ་ནི་དགེ་བའི་བཤེས་གཉེན་དང་ཕྲད་པ་བསྟན་པའོ། །

[Block 3065]
མདོ་ལས་དེ་ལྟར་དགེ་སློང་རྣམས་ཞེས་པ་ནས་ཚིགས་སུ་བཅད་པ་འདི་སྐད་གསོལ་ཏོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་གསོལ་བའོ། །

[Block 3066]
ཕན་པ་ཞེས་པ་ནི་ལེགས་པ་བསྟབས༌[^2588]པའོ། །

[Block 3067]
བདེ་བ་ཞེས་པ་ནི་སྡུག་བསྔལ་ལས་གདོན་པའི་ཕྱིར་ཆོས་བཤད་དུ་གསོལ་ཞེས་པའོ། །

[Block 3068]
མདོ་ལས་བསོད་ནམས་བརྒྱའི༌[^2589]མཚན་ཅན་ཞེས་པ་ནས་འཇིག་རྟེན་རྣམས་ལ་ཤོད་ཅིག་ཅེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ལ་ཕྱི་ནང་གི་ཡོན་ཏན་ཐམས་ཅད་ཚང་པའི་ཕྱིར་ཆོས་བཤད་པར་གསོལ་བ་དང་། ཕན་པ་ཆེན་པོ་ཐོབ་པ་དང་། དེ་བཞིན་གཤེགས་པའི་མཁྱེན་པ་བསྒྲགས་པའི་ཕྱིར་ཆོས་བཤད་པར༌[^2590]གསོལ་བའོ། །

[Block 3069]
མདོ་ལས་བདག་ཅག་རྣམས་དང་ཞེས་པ་ནས་སེམས་ཅན་འདི་རྣམས་ཀྱིས་ནི་ཐོབ་པར་རོ་ཞེས་པའི་བར་དུ་ནི་ཕན་པ་ཆེན་པོ་ཐོབ་པའི་ཕྱིར་ཆོས་བཤད་པར་གསོལ་པའོ། །

[Block 3070]
མདོ་ལས་ཀུན་མཁྱེན་པ་ནི་ཞེས་པ་ནས་དམ་པ་རབ་ཏུ་བསྐོར་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པའི་མཁྱེན་པ་བསྒྲགས་པའི་ཕྱིར་གསོལ་པ་སྟེ། མོས་པ་སྣ་ཚོགས་མཁྱེན་པ་དང་། ལམ་སྣ་ཚོགས་མཁྱེན་པ་དང་། དབང་པོ་རབ་འབྲིང་མཁྱེན་པ་དང་། སྔོན༌[^2591]གྱི་གནས་མཁྱེན་པ་ལ་སོགས་ཏེ་མཁྱེན་པ་འདི་དག་དང་ལྡན་ཞེས་པའོ། །

[Block 3071 [HEADING]]
###### ལྷ་ཚངས་པས་མཆོད་དེ་གསོལ་བ། ^4-7-6-1-2-0

[Block 3072]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཞེས་པ་ནས་སྣང་བ་ཆེན་པོས་ཁྱབ་པར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་ཚངས་པའི་རྒྱལ་པོས་མཆོད་དེ་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་གསོལ་བའོ། །

[Block 3073]
དེའི་ཚེ་ན་ས་གཡོ་བ་དང་། འོད་ཀྱིས༌[^2592]སྣང་བར་བྱས་པའོ། །

[Block 3074]
མདོ་ལས་འཇིག་རྟེན་ཐམས་ཅད་ཀྱི་བར་གྱི་འཇིག་རྟེན་ན་ཞེས་པ་ནས་ཕན་ཚུན་དུ་སྨྲའོ་ཞེས་པའི་བར་དུ་འཁོར་ཡུག༌[^2593]ཆེན་པོས་བསྐོར་བའི་རི་བྲགས་ཀྱི་ཕུགས༌[^2594]ན་གནས་པའི་སེམས་ཅན་སྣང་བར་བྱས་པའོ། །

[Block 3075]
མདོ་ལས་འཇིག་རྟེན་གྱི་ཁམས་དེ་ཐམས་ཅད་དང་ཞེས་པ་ནས་སྣང་བ་ཆེན་པོ་བྱུང་བར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ༌[^2595]ཚངས་པའི་གཞལ་མེད་ཁང་ལ་སོགས་པ་གཡོ་བར་བྱས་པའོ། །

[Block 3076]
མདོ་ལས་དེ་ནས་ཤར་ཕྱོགས་ཀྱི་འཇིག་རྟེན་གྱི་ཁམས་ཞེས་པ་ནས་ཚིགས་སུ་བཅད་དེ་སྨྲས་པ་ཞེས་པའི་བར་དུ་ནི་དེ་དག་ཆོས་ཉན་པ་ཡང་དང་པོ་འོད་ཀྱིས་བསྐུལ་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱི་གན་དུ་ཕྱིན་པ་དང་། ཆོས་བཤད་པར་གསོལ་པ་དང་། ཅང་མི་གསུང་བར༌[^2596]གནང་བར་ཤེས་པ་སྟེ། བསམ་གཏན་ལ་གནས་པའི་ལྷ་ཐམས་ཅད་ལྷགས་ཞེས་པའོ། །

[Block 3077]
མདོ་ལས།

[Block 3078]
བདག་ཅག་ཐམས་ཅད་དེ་རིང་ཤིན་ཏུ་དགའ། །ཞེས་པ་ནས། འདི་ལྟར་ཕྱོགས་བཅུ་ཀུན་ཏུ་དེང་དཔལ་འབར། །ཞེས་པའི་བར་དུ་ནི་ལྷ་རྣམས་ཀྱིས་བསྟོད་དེ་ཆོས་བཤད་པར་གསོལ་བའོ། །

[Block 3079]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཞེས་པ་ནས། ནུབ་ཕྱོགས་སུ་དོང་ནས་མཐོང་བ་ཞེས་པའི་བར་དུ་ནི་འོད་གང་ནས་འབྱུང་བ་ལོགས་སུ་ཚོལ་ཞིང་དོང་བ་བསྟན་ཏོ།[^2597] །མདོ་ལས་དེ་ནས༌[^2598]དགེ་སློང་རྣམས་ཞེས་པ་ནས་གཞལ་མེད་ཁང་བཅོམ་ལྡན་འདས་དེ་ལ་ཕུལ་ཞེས་པའི་བར་དུ་ནི་ལྷའི་གཞལ་མེད་ཁང་བཞེས་པར་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཅང་མི་གསུང་བས་གནང་བར་ཤེས་པ་དང་། ཚངས་པ་རྣམས་གཟེངས་བསྟོད་ཅིང་དགེ་བ་ལ་དགོད་པ༌[^2599]སྟེ། འོས་འོས་སུ་སྦྱར་རོ། །

[Block 3080]
མདོ་ལས།

[Block 3081]
ཚད་མེད་རྒྱལ་བ་ངོ་མཚར་འགྱུར།[^2600] །ཞེས་པ་ནས། འཇིག་རྟེན་རིག་པ་ཇི་ལྟར་དགྱེས་བཞིན་སྤྱོད། །ཞེས་པའི༌[^2601]བར་དུ་ནི་གཞལ་མེད་ཁང་དབུལ་བ་དང་། བསྟོད་དེ་ཕྱག་འཚལ་བའོ། །

[Block 3082]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཚངས་པ་ཆེན་པོ་དེ་དག་ཅེས་པ་ནས་དེ་བཞིན་གཤེགས་པ༌[^2602]ལ་གསོལ་བ་ལགས་ཞེས་པའི་བར་དུ་ནི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་གསོལ་བའོ། །

[Block 3083]
མདོ་ལས་དགེ་སློང་དག་དེ་ནས་ཚངས་པ་ཆེན་པོ་ཞེས་པ་ནས། དེ་ནས་དགེ་སློང་རྣམས་བཅོམ་ལྡན་འདས་དེས་ཚངས་པ་དེ་རྣམས་ལ་ཅང་མི་གསུང་བར་དེ་ན་བཞུགས་སོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་བཤད་པར་གནང༌[^2603]བའོ། །

[Block 3084]
དེ་ནས་ཡང་དགེ་སློང་རྣམས་ཞེས་པ་ནས་ཕན་ཚུན་དོང་ཞིང་སྨྲའོ་ཞེས་པའི་བར་དུ་ནི་ཚངས་པ་རྣམས་ལ་བསྐུལ་བའོ། །

[Block 3085]
དེ་ནས་དགེ་སློང་རྣམས་ཞེས་པ་ནས་གདོན་མི་ཟ་བར་འབྱུང་བར་འགྱུར་ཞེས་པའི་བར་དུ་ནི་ལྷ་རྣམས་ཀྱིས་གསོལ་བའོ། །
--- END BLOCKS ---
