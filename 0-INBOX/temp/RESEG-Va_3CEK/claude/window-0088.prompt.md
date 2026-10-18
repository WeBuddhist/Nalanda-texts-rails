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
[Block 3081]
འཁོར་ལོ་འདི་ནི་དེའི་ཡིན་པས་ན་ཚངས་པའི་འཁོར་ལོ༌[^2128]སྟེ། དེས་བསྐོར་བའི་ཕྱིར་རོ། །

[Block 3082 [HEADING]]
##### ཆོས་ཀྱི་འཁོར་ལོ། ^3-2-11-6-0

[Block 3083]
ཆོས་ཀྱི་འཁོར་ལོ་མཐོང་བའི་ལམ། རྒྱུ་བས་ན་འཁོར་ལོའོ། །

[Block 3084]
དེ་དང་ཆོས་མཐུན་པའི་ཕྱིར་མཐོང་བའི་ལམ་ནི་ཆོས་ཀྱི་འཁོར་ལོ་ཡིན་ནོ། །

[Block 3085]
འདིའི་ཆོས་མཐུན་པ་ཇི་ལྟ་བུ་ཞེ་ན། མྱུར་བར་འགྲོ་སོགས་རྩིབས་སོགས་ཀྱིས། མྱུར་དུ་འགྲོ་བའི་ཕྱིར་དང་། འདོར་བ་དང་འཇུག་པའི་ཕྱིར་དང་། མ་རྒྱལ་བ་རྒྱལ་བར་བྱེད་པ་དང་རྒྱལ་བ་རྣལ་དུ་དགོད་པའི༌[^2129]ཕྱིར་དང་། འཕར་བ་དང་འབབ་པའི་ཕྱིར་ཏེ། མྱུར་བར་འགྲོ་བ་ལ་སོགས་པ༌[^2130]ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 3086]
བཙུན་པ་དབྱངས་སྒྲོགས་ན་རེ་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་ནི་རྩིབས་ལ་སོགས་པ་དང་ཆོས་མཐུན་པའི་ཕྱིར་འཁོར་ལོ་ཞེས་བྱ་སྟེ། ཡང་དག་པའི་ལྟ་བ་དང་རྟོག་པ་དང་རྩོལ་བ་དང་དྲན་པ་རྣམས་ནི་རྩིབས་ལྟ་བུ་ཡིན་ནོ། །

[Block 3087]
ཡང་དག་པའི་ངག་དང་ལས་ཀྱི་མཐའ་དང་འཚོ་བ་རྣམས་ནི་ལྟེ་བ་ལྟ་བུ་ཡིན་ནོ། །

[Block 3088]
ཏིང་ངེ་འཛིན་ནི་མུ་ཁྱུད་ལྟ་བུ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3089]
མཐོང་བའི་ལམ་ཆོས་ཀྱི་འཁོར་ལོ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ག་ལས་ཤེ་ན་འཕགས་པ་ཀཽཎྜི་ནྱ་ལ་དེ་སྐྱེས་པ་ན་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་ཏོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3090]
ཇི་ལྟར་ན་དེ་ལན་གསུམ་དུ་བཟླས་པ་དང་རྣམ་པ་བཅུ་གཉིས་ཡིན་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ། འདི་ནི་སྡུག་བསྔལ་འཕགས་པའི་བདེན་པའོ། །

[Block 3091]
དེ་ཡོངས་སུ་ཤེས་པར་བྱའོ། །

[Block 3092]
དེ་ཡོངས་སུ་ཤེས་སོ་ཞེས་བྱ་བ་འདི་དག་ནི་ལན་གསུམ་དུ་བཟླས་པ་ཡིན་ནོ། །

[Block 3093]
བཟླས་པ་རེ་རེ་ལ་མིག་སྐྱེས་སོ། །ཤེས་པ་དང་རིགས་པ༌[^2131]དང་བློ་སྐྱེས་སོ་ཞེས་བྱ་བ་འདི་དག་ནི་རྣམ་པ་བཅུ་གཉིས་ཡིན་ཏེ། བདེན་པ་རེ་རེ་ལ་ཡང་དེ་དང་འདྲའོ། །

[Block 3094]
གསུམ་ཚན་དང་བཅུ་གཉིས་སུ་ཆོས་མཐུན་པའི་ཕྱིར་ལན་གསུམ་དུ་བཟླས་ཏེ། རྣམ་པ་བཅུ་གཉིས་ཞེས་བཤད་དེ། གཉིས་དང་། གནས་བདུན་ལ་མཁས་པ་བསྟན་པ་བཞིན་ནོ། །

[Block 3095]
བཟླས་པ་འདི་དག་གིས་ནི་གྲངས་བཞིན་དུ་མཐོང་བ་དང་བསྒོམ་པ་དང་མི་སློབ་པའི་ལམ་རྣམས་བསྟན་ཏོ་ཞེས་ཟེར་རོ། །

[Block 3096]
གལ་ཏེ་དེ་ལྟ་ན་འོ་ན་ནི༌[^2132]མཐོང་བའི་ལམ་ཁོ་ན་ལ་ལན་གསུམ་དུ་བཟླས་པ་ཡང་མ་ཡིན་ལ་རྣམ་པ་བཅུ་གཉིས་ཀྱང་མ་ཡིན་ན་ཇི་ལྟར་ན་མཐོང་བའི་ལམ་འདི་ཆོས་ཀྱི་འཁོར་ལོར་རྣམ་པར་གཞག །དེ་ལྟ་བས་ན་ཆོས་ཀྱི་རྣམ་གྲངས་དེ་ཉིད་ཆོས་ཀྱི་འཁོར་ལོ་ཡང་ཡིན་ལན་གསུམ་དུ༌[^2133]བཟླས་པ་དང་རྣམ་པ་བཅུ་གཉིས་ཀྱང་ཡིན་པར་རུང་ངོ་། །ཇི་ལྟར་ན་ལན་གསུམ་དུ་བཟླས་པ་ཡིན་ཞེ་ན། བདེན་པ་རྣམས་ལན་གསུམ་དུ་བཟླས་པའི་ཕྱིར་རོ། །ཇི་ལྟར་ན་རྣམ་པ་བཅུ་གཉིས་ཡིན་ཞེ་ན། བདེན་པ་རྣམས་ལ་སྡུག་བསྔལ་དང་། [^2134]ཀུན་འབྱུང་། འགོག་པ། ལམ་ཞེས་བྱ་བ་དང་། ཡོངས་སུ་ཤེས་པར་བྱ། སྤང་བར་བྱ། མངོན་སུམ་དུ་བྱ། བསྒོམ་པར་བྱ་ཞེས་བྱ་བ་དང་། །ཡོངས་སུ་ཤེས་སྤངས། མངོན་སུམ་དུ་བྱས། བསྒོམས་ཞེས་བྱ་བ་རྣམ་པ་གསུམ་དུ་བྱས་པའི་ཕྱིར་རོ། །

[Block 3097]
དེ་བསྐོར་བ་ནི་གཞན་གྱིས་རྒྱུད་ལ་གོ་བར་བྱེད་པ་སྟེ། དོན་ཤེས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3098]
ཡང་ན་འཕགས་པའི་ལམ་ཐམས་ཅད་ཀྱང་གདུལ་བྱའི་རྒྱུད་ལ་འཇུག་པའི་ཕྱིར་ཆོས་ཀྱི་འཁོར་ལོ་ཡིན་ཏེ། དེ་ནི་གཞན་གྱི༌[^2135]རྒྱུད་ལ་མཐོང་བའི་ལམ་བསྐྱེད་པའི་ཕྱིར་བསྐོར་བར་བརྩམས་པ་ཡིན་པས་དེའི་ཕྱིར་བསྐོར་བ་ཞེས་བྱའོ། །

[Block 3099 [HEADING]]
##### ཁམས་གང་དུ་འབྲས་བུ་འཐོབ་པ། ^3-2-11-7-0

[Block 3100]
ཡང་ཁམས་གང་དུ་དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་དུ་དག་ཅིག་འཐོབ་ཅེ་ན། འདོད་པར་གསུམ་ཐོབ།[^2136] གསུམ་ནི་འདོད་པའི་ཁམས་ཁོ་ནར་འཐོབ་ཀྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 3101]
ཐ་མ་ནི། གསུམ་དུ། དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་ཐ་མ་ནི་དགྲ་བཅོམ་པ་ཉིད་དེ། དེ་ནི༌[^2137]ཁམས་གསུམ་དུ་འཐོབ་པོ། །རེ་ཞིག་འབྲས་བུ་གཉིས་ནི་འདོད་ཆགས་དང་མ༌[^2138]བྲལ་བས་ཐོབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་གོང་མར་མི་འཐོབ་པར་ཡང་རིགས་ན་གསུམ་པ་གོ། །ཅིའི་ཕྱིར་མི་འཐོབ་ཅེ་ན། གོང་ན་མཐོང་ལམ་མེད། འདོད་པའི་ཁམས་ལས་གང༌[^2139]ན་ནི་མཐོང་བའི་ལམ༌[^2140]མེད་ལ། དེ་མེད་པར་ཡང་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ཐོབ་པ་མེད་པས་ཞེས་བྱ་བ་འདི་ནི་གཏན་ཚིགས་ཡིན་ནོ། །ཅིའི་ཕྱིར་དེ་ན་མཐོང་བའི་ལམ་མེད་ཅེ་ན། རེ་ཞིག་གཟུགས་མེད་པའི་ཁམས་ན་ནི་ཉན་པ་མེད་པ་དང་། ཁམས་འོག་མ་ལ་མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3102]
གཟུགས་ཀྱི་ཁམས་ན་ནི།

[Block 3103 [VERSE]]
མི་སྐྱེ༌[^2141]ལུང་ལས་འདིར་རྩོམ་ཞིང་། །
དེར་མཐར་ཕྱིན་ཞེས་འབྱུང་ཕྱིར་རོ། །

[Block 3104]
གཟུགས་ན་སྤྱོད་པའི་སོ་སོའི་སྐྱེ་བོ་རྣམས་ནི་སྙོམས་པར་འཇུག་པའི་བདེ་བ་ལ་ཆགས་པའི་ཕྱིར་དང་། སྡུག་བསྔལ་གྱི་ཚོར་བ་མེད་པའི་ཕྱིར་ཀུན་དུ་སྐྱོ་བར་མི་འགྱུར་ལ། སྐྱོ་བ་མེད་པར་ཡང་འཕགས་པའི་ལམ་ཐོབ་པར༌[^2142]མི་འགྱུར་ཏེ། འདི་ནི་རེ་ཞིག་རིགས་པ་ཡིན་ནོ། །

[Block 3105]
ལུང་ཡང་། བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བས་ན༌[^2143]གོང་དུ་འཕོ་བའི་བར་གང་ཟག་ལྔ་ནི་འདིར་རྩོམ་ཞིང་དེར་མཐར་ཕྱིན་པར་འགྱུར་རོ་ཞེས་གསུངས་པ་འདི་ཡིན་ནོ། །

[Block 3106]
རྩོམ་པ༌[^2144]ཞེས་བྱ་བ་ནི༌[^2145]ལམ་རྩོམ་པ༌[^2146]ཡིན་ཏེ། མྱ་ངན་ལས་འདས་པའི་ཐབས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3107 [HEADING]]
#### དགྲ་བཅོམ་པ་དྲུག། ^3-2-12-0

[Block 3108]
འདི་སྐད་དུ།

[Block 3109 [VERSE]]
གལ་ཏེ་མི་གཡོའི་ཟད་ཤེས་ལ། །
མི་སྐྱེ༌[^2147]བློ་གྲོས་ཞེས་བཤད༌[^2148]དེ། །

[Block 3110]
ཅི་དགྲ་བཅོམ་པ་ལ་ཡང་དབྱེ་བ་ཡོད་དམ་ཞེ་ན་སྨྲས་པ་ཡོད་དེ། དགྲ་བཅོམ་དྲུག་འདོད། མདོ་ལས་དགྲ་བཅོམ་པ༌[^2149]དྲུག་གསུངས་ཏེ། ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་དང་། འཆི་བར་སེམས་པའི་ཆོས་ཅན་དང་། རྗེས་སུ་སྲུང་བའི་ཆོས་ཅན་དང་། གནས་པ་ལས་མི་བསྐྱོད་པ༌[^2150]དང་། རྟོགས་པའི་སྐལ་བ་ཅན་དང་། མི་གཡོ་བའི་ཆོས་ཅན་ནོ། །

[Block 3111]
དེ་དག་ལས།

[Block 3112 [HEADING]]
##### དུས་ཀྱི་རྣམ་པར་གྲོལ་བ་དང་དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བ། ^3-2-12-1-0

[Block 3113]
ལྔ་ནི་དད་པས་མོས་ལས་སྐྱེས། །མི་གཡོ་བའི་ཆོས་ཅན་མ་གཏོགས་པ་གཞན་ལྔ་ནི་དད་པས་མོས་པ་སྔོན་དུ་འགྲོ་བ་དག་ཡིན་ནོ། །

[Block 3114]
དེ་དག་རྣམ་གྲོལ་དུས་དང་སྦྱོར། །ལྔ་པོ་འདི་དག་གི་སེམས་ཀྱི་རྣམ་པར་གྲོལ་བ་ནི་དུས་དང་སྦྱོར་བས༌[^2151]འཕངས་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ། རྟག་ཏུ་རྗེས་སུ་སྲུང་བའི་ཕྱིར་རོ། །

[Block 3115]
དེ་ཉིད་ཀྱི་ཕྱིར་འདི་དག་ནི་དུས་ཀྱི་རྣམ་པར་གྲོལ་བ་ཞེས་བྱའོ། །

[Block 3116]
འདི་དག་ནི་དུས་ལ་ལྟོས་པ་ཡང་ཡིན་ལ་རྣམ་པར་གྲོལ་བ་ཡང་ཡིན་པས༌[^2152]དུས་ཀྱི༌[^2153]རྣམ་པར་གྲོལ་བ་དག་སྟེ། བར་གྱི་ཚིག་མི་མངོན་པར་བྱས་པའི་ཕྱིར་མར་གྱི་བུམ་པ་བཞིན་ནོ། །

[Block 3117]
འདི་དག་གི་ཏིང་ངེ་འཛིན་མངོན་སུམ་དུ་གྱུར་པ༌[^2154]ནི་ཡོ་བྱད་དང་ནད་མེད་པ་དང་ཡུལ་གྱི་བྱེ་བྲག་ལ་ལྟོས་པའི་ཕྱིར་དུས་ལ་ལྟོས་པ་ཡིན་ནོ། །

[Block 3118]
མི་གཡོའི་ཆོས་ཅན་མི་གཡོ་བ། །མི་གཡོ་བའི་ཆོས་ཅན་གྱི་རྣམ་པར་གྲོལ་བ་ནི་ཡོངས་སུ་མི་ཉམས་པའི་སྒོ་ནས་གཡོ་བར་མི་ནུས་པའི་ཕྱིར་མི་གཡོ་བ་ཡིན་ནོ། །

[Block 3119]
དེའི་ཕྱིར་དེ་དུས་མི་སྦྱོར་གྲོལ། །དེ་ཉིད་ཀྱི་ཕྱིར་དེ་ནི་དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བ་ཞེས་བྱ་བ་སྟེ། དེ་ནི་འདོད་དགུར་ཏིང་ངེ་འཛིན་མངོན༌[^2155]སུམ་དུ་གྱུར་པའི་ཕྱིར་དུས་ལ་མི་ལྟོས་པར་རྣམ་པར་གྲོལ་བ་ཡིན་ནོ། །

[Block 3120]
ཡང་ན་ཡོངས་སུ་ཉམས་པ་སྲིད་པ་དང་། མི་སྲིད་པའི་སྒོ་ནས་དུས་གཞན་གྱི་བར་དང་། གཏན་དུ་རྣམ་པར་གྲོལ་བའི་ཕྱིར་དུས་ཀྱི༌[^2156]རྣམ་པར་གྲོལ་བ་དང་། དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བ་ཉིད་ཡིན་ནོ། །
--- END BLOCKS ---
