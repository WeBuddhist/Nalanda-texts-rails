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
[Block 3151]
དེ་ཉིད་ཀྱི་ཕྱིར་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལས་ཡོངས་སུ་ཉམས་པ་མེད་དོ། །

[Block 3152]
དེ་ལྟར་བྱས་ན་ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་ནི་རྣམ་པ་གསུམ་ཡིན་ཏེ།[^2164] དེའི་སོ་ན་གནས་པ་བཞིན་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ༌[^2165]དང་། དབང་པོ་འཕོ་བའམ།[^2166] ཡོངས་སུ་ཉམས་ནས་སློབ་པ་ཉིད་དུ་འགྱུར་བའོ། །

[Block 3153]
འཆི་བར་སེམས་པའི་ཆོས་ཅན་ནི་བཞི་སྟེ། གསུམ་པོ་དེ་དག་ཉིད་དང་། ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་གྱི་རིགས་སུ་སླར་འོང་བའོ། །

[Block 3154]
དེ་བཞིན་དུ༌[^2167]གསུམ་ལ་ཡང་རེ་རེ་བསྐྱེད་དེ། གོ་རིམས་བཞིན་དུ་རྣམ་པ་ལྔ་དང་དྲུག་དང་བདུན་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3155]
དེ་སློབ་པར་གྱུར་ན་གང་གི་རིགས་དང་པོ་གང་ཡིན་པ་དེ་ཁོ་ན་ལ་གནས་ཀྱི་གཞན་དག༌[^2168]ལ་ནི་མ་ཡིན་ནོ། །

[Block 3156]
དེ་ལྟ་མ་ཡིན་ན་རིགས་ཁྱད་པར་ཅན་རྙེད་པའི་ཕྱིར་དེ་འཕེལ་བ་ཁོ་ནར་འགྱུར་གྱི་ཡོངས་སུ་ཉམས་པར་ནི་མི་འགྱུར་རོ། །

[Block 3157 [HEADING]]
###### འབྲས་བུ་དང་པོ་ལས་ཡོངས་སུ་ཉམས་པ་མེད་པ། ^3-2-12-3-1-0

[Block 3158]
ཅིའི་ཕྱིར་འབྲས་བུ་དང་པོ་ལས་ཡོངས་སུ་ཉམས་པ་མེད་ཅེ་ན། མཐོང་བས་སྤང་བར༌[^2169]བྱ་བ་རྣམས་གཞི༌[^2170]མེད་པའི་ཕྱིར་ཏེ། དེ་དག་ནི་འཇིག་ཚོགས་ལ་ལྟ་བའི་རྩ་བ་ཅན་ཡིན་པའི་ཕྱིར་བདག་གི་གཞི་ལ་འཇུག་པ་ཅན༌[^2171]ཡིན་ན་བདག་དེ་ཡང་མེད་དོ། །

[Block 3159]
འོ་ན་མེད་པ་ལ་དམིགས་པར་འགྱུར་རོ་ཞེ་ན། བདེན་པ་ལ་དམིགས་པའི་ཕྱིར་མེད་པ་ལ་དམིགས་པ་ནི་མ་ཡིན་གྱི་ཕྱིན་ཅི་ལོག་ཏེ༌[^2172]དམིགས་པ་དག་ནི༌[^2173]ཡིན་ནོ། །

[Block 3160]
དེ་ལྟ་མ་ཡིན་པའི་ཉོན་མོངས་པ་གང་ཞིག་ཡིན་ཞེ་ན། ཁྱད་པར་ཡོད་དེ། བདག་ཏུ་ལྟ་བ་ནི་བདག་མེད་བཞིན་དུ་གཟུགས་ལ་སོགས་པའི་དངོས་པོ་ལ་བྱེད་པ་པོ་དང་ཚོར་བ་པོ་དང༌[^2174]དབང་བསྒྱུར་བ་ཉིད་དུ་བདག་ཡང་དག་པ་མ་ཡིན་པ་སྒྲོ་འདོགས་པར་བྱེད་ལ། མཐར་འཛིན་པ་ལ་སོགས་པ་ཡང་དེའི་གཞི་ལ་ཞུགས་པ་ཡིན་པས་གཞི་མེད་པ་དག་ཅེས་བྱའོ། །

[Block 3161]
བསྒོམ་པས་སྤང་བར་བྱ་བ་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། ང་རྒྱལ་དང་། མ་རིག་པ་རྣམ་པ༌[^2175]ནི་གཟུགས་ལ་སོགས་པའི་དངོས་པོ་ལ་ཆགས་པ༌[^2176]དང་། ཀུན་ནས་མནར་སེམས་དང་། ཁེངས་པ་དང་། མི་གསལ་བའི་ངོ་བོར་ཞུགས་པ་འབའ་ཞིག་ཏུ་ཟད་པས་གཞི་དང་བཅས་པ་དག་ཅེས་བྱ་སྟེ། གང་ལ་དེ་དག་འཇུག་པར་འགྱུར་བ་སྡུག་པ་ལ་སོགས་པ་ཙམ་དེ་ནི་ཡོད་ཀྱི། བདག་ལ་སོགས་པ་ནི་བག་ཀྱང་མེད་དོ། །

[Block 3162]
གཞན་དག་ནི་འདི་སྐད་ཅེས་ཟེར་ཏེ། འདི་ལྟར་བསྒོམ་པས༌[^2177]སྤང་བར་བྱ་བ་རྣམས་ལ་ནི་གཞི་ཡིད་དུ་འོང་བ་དང་ཡིད་དུ་མི་འོང་བའི་མཚན་ཉིད་སོ་སོར་ངེས་པ་ཡོད་ཀྱི། མཐོང་བས་སྤང་བར༌[^2178]བྱ་བ་རྣམས་ལ་ནི་བདག་ལ་སོགས་པའི་མཚན་ཉིད་མེད་དེ། དེ་ལྟ་བས་ན་གཞི་སོ་སོར་ངེས་པ༌[^2179]མེད་པ་དག་ཅེས་བྱའོ། །

[Block 3163]
གཞན་ཡང་འཕགས་པ་ངེས་པར་མི་རྟོག་པ་ལ་དྲན་པ་ཉམས་པས་ཉོན་མོངས་པ་རྣམས་སྐྱེ་བར་འགྱུར་གྱི་ངེས་པར་རྟོག་པ༌[^2180]ལ་ནི་མ་ཡིན་ཏེ། ཐག་པ་ལ་སྦྲུལ་གྱི་འདུ་ཤེས་བཞིན་ནོ། །

[Block 3164]
ངེས་པར་མི་རྟོག་པ༌[^2181]ལ་ནི་བདག་ཏུ་ལྟ་བ་ལ་སོགས་པ་འབྱུང་བར་མི་རུང་སྟེ། ཀུན་དུ་རྟོག་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3165]
དེ་ལྟ་བས་ན་མཐོང་བས་སྤང་བར་བྱ་བ་སྤངས་པས་ས་དང་པོ༌[^2182]ལས་ཡོངས་སུ་ཉམས་པ་མེད་དོ། །

[Block 3166 [HEADING]]
###### དགྲ་བཅོམ་པ་ཉིད་ལས་ཡོངས་སུ་ཉམས་པ་མེད་པ། ^3-2-12-3-2-0

[Block 3167]
མདོ་སྡེ་པ་རྣམས་ན་རེ་དགྲ་བཅོམ་པ་ཉིད་ལས་ཀྱང་ཡོངས་སུ་ཉམས་པ་མེད་དོ་ཞེས་ཟེར་ཏེ། དེ་ཉིད་རིགས་པ་ཡིན་ནོ། །

[Block 3168]
འདི་ཇི་ལྟར་ཁོང་དུ་ཆུད་ཅེ་ན། ལུང་དང་རིགས་པ་ལས་སོ། །

[Block 3169 [HEADING]]
###### **ལུང།** ^3-2-12-3-2-1-0

[Block 3170]
ལུང་ལས་ཇི་ལྟ་བུ་ཞེ་ན། དགེ་སློང་དག་འཕགས་པའི་ཤེས་རབ་ཀྱིས་སྤངས་པ་གང་ཡིན་པ་དེ་ནི་སྤངས་པ་ཡིན་ནོ་ཞེས་གསུངས་པ་དང་། སློབ་པ་ལ་བག་ཡོད་པ་ལ་བག་ཡོད་པར་བྱའོ་ཞེས་དང་སྨྲའོ༌[^2183]གསུངས་ཀྱི་དགྲ་བཅོམ་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3171]
ཀུན་དགའ་བོ་དགྲ་བཅོམ་པ་ལ་ཡང་རྙེད་པ་དང་བཀུར་སྟིས་བར་ཆད་བྱེད་པ་ཡིན་པར་ང་སྨྲའོ་ཞེས་གསུངས་པའི་མདོ་དེ་ལས་ནི་མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པ་ཙམ་ཁོ་ན་ལས་ཡོངས་སུ་ཉམས་པར་འགྱུར་བར་གསུངས་པར་ཟད་དེ། འདིས༌[^2184]སེམས་རྣམ་པར་གྲོལ་བ་མི་གཡོ་བ་ལུས་ཀྱིས་མངོན་སུམ་དུ༌[^2185]བྱས་པ་གང་ཡིན་པ་དེ་ལས་ནི་རྣམ་གྲངས་གང་གིས་ཀྱང་ཡོངས་སུ་ཉམས་པར་འགྱུར་བར་ང་མི་སྨྲའོ་ཞེས་གསུངས་སོ། །

[Block 3172]
གལ་ཏེ་དུས་དང་སྦྱོར་བ་ལ་ཡོད་དོ་ཞེ་ན། ཁོ་བོ་ཅག་ཀྱང་དེ་སྐད་ཅེས་ནི་ཟེར་རོ། །

[Block 3173]
ཅི་དེ་དགྲ་བཅོམ་པ་ཉིད་ཡིན་ནམ། འོན་ཏེ་བསམ་གཏན་པ་རྣམས་ཡིན་ཞེས་བྱ་བ་དཔྱད་པར་བྱས་ཏེ། བསམ་གཏན་དངོས་གཞིའི་ཏིང་ངེ་འཛིན་ནི་དུས་སུ་མངོན་སུམ་དུ་འགྱུར་བའི་ཕྱིར་རྣམ་པར་གྲོལ་བ་དུས་དང་སྦྱོར་བ་ཞེས་ཀྱང་བྱ་ལ་མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པར་བྱ་བའི་ཕྱིར་ཡང་དང་ཡང་དུ་བཙལ་བར༌[^2186]བྱ་བ་ཡིན་པའི་ཕྱིར་ཡིད་དུ་འོང་བ་ཞེས་ཀྱང་བྱའོ། །

[Block 3174]
གཞན་དག་ན་རེ་རོ་མྱང་བར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 3175]
དགྲ་བཅོམ་པ་ཉིད་ཀྱི་རྣམ་པར་གྲོལ་བ་ནི་རྟག་ཏུ་རྗེས་སུ་འབྲེལ་བའི་ཕྱིར་དུས་དང་སྦྱོར་བ༌[^2187]ཡིན་པར་ཡང་མི་རུང་ལ། ཡང་དོན་དུ་གཉེར་བར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་ཡིད་དུ་འོང་བ་ཡང་མ་ཡིན་ནོ། །

[Block 3176]
གལ་ཏེ་ཡང་དགྲ་བཅོམ་པ་ཉིད་ལས་ཡོངས་སུ་ཉམས་པ་སྲིད་པ་ཞིག་ཏུ་གྱུར་ན། ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པར༌[^2188]ལྷག་པའི་སེམས་ལས་བྱུང་བ་དག་ཁོ་ན་ལས་ཡོངས་སུ་ཉམས་པར་འགྱུར་བར་གསུངས་པར་གྱུར༌[^2189]ཏེ། དེའི་ཕྱིར་དགྲ་བཅོམ་པ་ཐམས་ཅད་ཀྱི་རྣམ་པར་གྲོལ་བ་ནི་མི་གཡོ་བ་ཡིན་པར་ཁོང་དུ་ཆུད་དོ། །

[Block 3177]
མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པ་དག་ལས་ནི་ལ་ལ་ནི༌[^2190]རྙེད་པ་དང་བཀུར་སྟིས་གཡེན་སྤྱོ་བའི་ཉེས་པས་དབང་ཉམས་པའི་ཕྱིར་ཡོངས་སུ་ཉམས་པར་འགྱུར་ཏེ། དབང་པོ་རྟུལ་པོ་གང་ཡིན་པའོ། །

[Block 3178]
ལ་ལ་ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་ཏེ། དབང་པོ་རྣོན་པོ་གང་ཡིན་པའོ། །

[Block 3179]
དེ་ལ་གང་ཞིག་ཡོངས་སུ་ཉམས་པར་འགྱུར་བ་དེ་ནི་ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་ཡིན་ལ། གང་ཞིག་ཡོངས་སུ་ཉམས་པར་མི༌[^2191]འགྱུར་བ་དེ་ནི་ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་བའི་ཆོས་ཅན་ཡིན་ཏེ། དེ་བཞིན་དུ་འཆི་བར་སེམས་པའི་ཆོས་ཅན་ལ་སོགས་པ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 3180]
ཡོངས་སུ་མི་ཉམས་པའི་ཆོས་ཅན་དང་། གནས་པ་ལས་མི་བསྐྱོད་པ་དང་། མི་གཡོ་བའི་ཆོས་ཅན་རྣམས་ལ༌[^2192]ཁྱད་པར་ཅི་ཡོད་ཅེ་ན། ཡོངས་སུ་མི་ཉམས་པའི་ཆོས་ཅན་ནི་སྦྱངས་པ་ལས་གྱུར་པ་ནི༌[^2193]མ་ཡིན་ལ། མི་གཡོ་བའི་ཆོས་ཅན་ནི་སྦྱངས་པ་ལས་གྱུར་པ་ཡིན་ཏེ། དེ་གཉིས་ནི་ཏིང་ངེ་འཛིན་གྱི་ཁྱད་པར་གང་ཁོ་ན་སྐྱེད་པར་བྱེད་པ་དེ་ལས་ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་རོ། །

[Block 3181]
གནས་པ་ལས་མི་བསྐྱོད༌[^2194]པ་ནི་ཡོན་ཏན་གང་ཁོ་ན་ལ༌[^2195]གནས་པ་དེ་ལས་ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་བ་འབའ་ཞིག་ཏུ་ཟད་ཀྱི། གཞན་ཡང་སྐྱེད་པར་མི་བྱེད་པའམ། སྐྱེད་པར་བྱེད་ན་ཡང་དེ་ལས་གཡོ་བར་འགྱུར་བ་ཡིན་པས་འདི་ནི་ཁྱད་པར་ཡིན་པར་མངོན་ནོ། །

[Block 3182]
ཚེ་དང་ལྡན་པ་གནག་ཚོགས་ཅན་སློབ་པར་གྱུར་པ་ཧ་ཅང་རོ་མྱང་བའི་ཕྱིར་དང་། དབང་པོ་རྟུལ་པོ་ཡིན་པའི་ཕྱིར་སེམས་རྣམ་པར་གྲོལ་བ་དུས་དང་སྦྱོར་བ་པ་ལས་ཡང་དང་ཡང་དུ་ཡོངས་སུ་ཉམས་པ་དང་། ཡི་ཆད་ནས་ལུས་དང་སྲོག་ལ་མི་ལྟ་བར་མཚོན་གྱིས་འདེབས་པར་བྱེད་ལ། འཆི་བའི་དུས་ཁོ་ནར་དགྲ་བཅོམ་པ་ཉིད་ཐོབ་ཅིང་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པར་ཡང་གྱུར་ཏེ། དེ་ལྟ་བས་ན་དེ་ཡང་དགྲ་བཅོམ་པ་ཉིད་ལས་ཡོངས་སུ་ཉམས་པ༌[^2196]མ་ཡིན་ནོ། །

[Block 3183]
བཅུ་ལས་འཕྲོས་པ་ལས་ཀྱང་བསྐྱེད་པར་བྱ་བའི་ཆོས་ནི་གཅིག་སྟེ། སེམས་རྣམ་པར་གྲོལ་བ་དུས་དང་སྦྱོར་བ་པ་ཡིད་དུ་འོང་བ་ཡིན་ནོ། །

[Block 3184]
མངོན་སུམ་དུ་བྱ་བའི་ཆོས་ནི་གཅིག་སྟེ། སེམས་རྣམ་པར་གྲོལ་བ༌[^2197]མི་གཡོ་བ་ཡིན་ནོ་ཞེས་གསུངས་ཏེ། གལ་ཏེ་སེམས་རྣམ་པར་གྲོལ་བ་དུས་དང་སྦྱོར་བ་པ་ཡིད་དུ་འོང་བ་དགྲ་བཅོམ་པ་ཉིད་ཁོ་ན༌[^2198]ཡིན་པར་གྱུར་ན། ཅིའི་ཕྱིར་བཅུ་ཚན་དེ་ཁོ་ན་ལས་དགྲ་བཅོམ་པ་ཉིད་ལན་གཉིས་སུ་སྨོས་པར་འགྱུར། དགྲ་བཅོམ་པ་ཉིད་བསྐྱེད་པར་བྱ་བ་ཡིན་པར་ནི་གང་དུ་ཡང་མ་གསུངས་སོ། །

[Block 3185]
འོ་ན་ཅི་ཞེ་ན། མངོན་སུམ་དུ་བྱ་བ་ཡིན་ནོ། །

[Block 3186]
དབང་པོ་རྟུལ་པོས་བསྡུས་པའི་དགྲ་བཅོམ་པ་ཉིད་བསྐྱེད་པར་བྱ་བ་ཡིན་ནོ་ཞེ་ན། ཡང་འདིས་ཅི་ཞིག་ཤེས་པར་བྱ་བ་ཡིན། རེ་ཞིག་གལ་ཏེ་བསྐྱེད་པར་བྱ་བར་ནུས་པ་ཡིན་ནོ་ཞེ་ན་ནི། གཞན་ཡང་ནུས་སོ། །

[Block 3187]
འོན་ཏེ་བསྐྱེད་པར་འོས་པ་ཡིན་ནོ་ཞེ་ན་ནི་གཞན་ཆེས་ཤིན་ཏུ་འོས་པ༌[^2199]ཡིན་ཏེ། དེ་ལྟ་བས་ན་རྣམ་པར་གྲོལ་བ༌[^2200]དུས་དང་སྦྱོར་བ་པ་ནི་དགྲ་བཅོམ་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 3188]
འོ་ན་དུས་ཀྱིས་རྣམ་པར་གྲོལ་བའི་དགྲ་བཅོམ་པ་ཞེས་ཇི་སྐད་ཅེས༌[^2201]བྱ་ཞེ་ན། གང་ཞིག་དབང་པོ་རྟུལ་པོའི༌[^2202]ཕྱིར་ཏིང་ངེ་འཛིན་མངོན་སུམ་དུ་འགྱུར་བ་དུས་ལ་ལྟོས༌[^2203]པ་ཡིན་ནོ། །

[Block 3189]
བཟློག་པ་ནི་དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བ་ཡིན་ནོ། །

[Block 3190]
ཆོས་མངོན་པ་ལས་ཀྱང་། གནས་གསུམ་གྱིས་འདོད་པའི་འདོད་ཆགས་ཀྱི་ཕྲ་རྒྱས་སྐྱེ་བར་འགྱུར་ཏེ། འདོད་པའི་འདོད་ཆགས་ཀྱི་ཕྲ་རྒྱས་མ་སྤངས་ཤིང་ཡོངས་སུ་མ་ཤེས་པ་ཡིན། འདོད་པའི་འདོད་ཆགས་ཀྱི་ཀུན་ནས་དཀྲིས་པར་གྱུར་པའི་ཆོས་རྣམས་ཀྱང་སྣང་བར་གྱུར་པ་ཡིན། དེ་ལ་ཡང་ཚུལ་བཞིན༌[^2204]མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ཡིན་ཞེས་གསུངས་སོ། །
--- END BLOCKS ---
