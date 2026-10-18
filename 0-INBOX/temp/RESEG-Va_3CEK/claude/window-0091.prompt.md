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

[Block 3191]
གལ་ཏེ་དེ་ལྟ་བུ་ནི་རྒྱུ་ཡོངས་སུ་ཚང་བ་ལས་སྐྱེས་པ་ཡིན་ནོ་ཞེ་ན། རྒྱུ་ཡོངས་སུ་མ་ཚང་བར་གོ་གང་ཞིག་སྐྱེ་ཞེ་ན། རེ་ཞིག་ལུང་ལས་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 3192 [HEADING]]
###### **རིགས་པ།** ^3-2-12-3-2-2-0

[Block 3193]
རིགས་པ་ལས་ཇི་ལྟ་བུ་ཞེ་ན། རེ་ཞིག་གལ་ཏེ༌[^2205]དགྲ་བཅོམ་པ་ལ་གང་གིས་ན་ཉོན་མོངས་པ་རྣམས་གཏན་ཏུ་མི་སྐྱེ་བའི་ཆོས་ཉིད་དུ་གྱུར་པ་དེ་ལྟ་བུའི་གཉེན་པོ་ཞིག་སྐྱེས་ན་ནི་ཇི་ལྟར་ན༌[^2206]ཡང་ཡོངས་སུ་ཉམས་པར་འགྱུར། འོན་ཏེ་མ་སྐྱེས་ཏེ་དེའི་ས་བོན་གྱི་ཆོས་ཉིད་གཏན་དུ་རྩ་ནས༌[^2207]མ་བཏོན༌[^2208]ན་ནི་ཇི་ལྟར་ཟག་པ་ཟད་པ་ཡིན། ཟག་པ་མ་ཟད་ན་ཡང་ཇི་ལྟར་དགྲ་བཅོམ་པ་ཉིད་ཡིན་ཏེ། རིགས་པ་ལས་ནི༌[^2209]དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 3194]
འོ་ན་ནི་གང་ལས་འདི་སྐད་དུ་འཕགས་པ་ཉན་ཐོས་ཐོས་པ་དང་ལྡན་པ་དེ་ལྟར་སྤྱོད་པ་དེ་ལྟར་གནས་པ༌[^2210]དེ་བརྒྱ་ལ་རེས་འགའ་ཞིག་དྲན་པ་ཉམས་པ་ལས་སྡིག་པ་མི་དགེ་བའི་རྣམ་པར་རྟོག་པ་དག་སྐྱེ་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་སོལ་བའི༌[^2211]ཕུང་པོ་ལྟ་བུའི་མདོའི་ལན་གདབ་དགོས་སོ། །

[Block 3195]
དེ་ནི་དེ་ལས་དགྲ་བཅོམ་པ༌[^2212]ཁོ་ན་ཡིན་པར་བསྟན་ཏེ། ཡུན་རིང་པོ༌[^2213]ནས་སེམས་དབེན་པ་ལ་གཞོལ་བ་ཡིན་ཞེས་བྱ་བ་ནས། མྱ་ངན་ལས་འདས་པ་ལ་བབ་པ་ཡིན་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3196]
གཞན་ལས་དེ་ནི་དགྲ་བཅོམ་པའི་སྟོབས་ཡིན་པར་ཡང་གསུངས་ལ། ཟག་པའི་གནས་ལྟ་བུའི་ཆོས་ཐམས་ཅད་ལས་ནི་བསིལ༌[^2214]བར་གྱུར་ཅིང་བསིལ་བར་གྱུར་པ་ཞེས་ཀྱང་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3197]
དེ་སྐད་དུ་འབྱུང་བ་ཡང་ཡོད་མོད་ཀྱི་ཇི་སྲིད་དུ་སྤྱོད་པ་ལེགས་པར་མ་རྟོགས་པ༌[^2215]དེ་སྲིད་དུ༌[^2216]སློབ་པ་དེ་ལྟར་སྤྱོད་པ་ལ༌[^2217]ཡང་ཉོན་མོངས་པ་འབྱུང་བ་སྲིད་པ་ཡོད་པས་སློབ་པའི་གནས་སྐབས་ཀྱི་དབང་དུ་མཛད་ནས་དེ་སྐད་དུ་གསུངས་པའི་ཕྱིར་ཉེས་པ་མེད་དོ། །

[Block 3198]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་དགྲ་བཅོམ་པ་ཉིད་ལས་ཀྱང་ཡོངས་སུ་ཉམས་པར་འགྱུར་བར་བརྗོད་དོ། །

[Block 3199 [HEADING]]
##### སློབ་པ་དང་འཕགས་པ་མ་ཡིན་པའི་རིགས་དྲུག། ^3-2-12-4-0

[Block 3200]
ཅི་དགྲ་བཅོམ་པ་དེ་དག་ཁོ་ན་རིགས་དྲུག་དང་ལྡན་ནམ། འོན་ཏེ་གཞན་དག་ཀྱང་རིགས་དྲུག་དང་ལྡན་ཞེ་ན། སློབ་དང་འཕགས་མིན་རིགས་དྲུག་ལྡན། །སློབ་པ་དང་སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱང་དེ་བཞིན་དུ་རིགས་དྲུག་དང་ལྡན་ཏེ། དགྲ་བཅོམ་པའི་རིགས་རྣམས་ནི་དེ་དག་སྔོན་དུ་འགྲོ་བ་ཡིན་ནོ། །

[Block 3201]
གཞན་ཡང་། མཐོང་བ་ལ་ནི་འཕོ་བ་མེད། །མཐོང་བའི་ལམ་ལས༌[^2218]གཞན་པ་ལ་དབང་པོ་འཕོ་བ་ཡོད་ཀྱི་སྦྱོར་བ་མི་སྲིད་པའི་ཕྱིར་མཐོང་བའི་ལམ་ལ༌[^2219]ནི་མ་ཡིན་ནོ། །

[Block 3202]
ལ་ལ་ནི་སོ་སོའི་སྐྱེ་བོའི་གནས་སྐབས་ན་དབང་པོ་རྣམས་འཕོའོ། །

[Block 3203]
ལ་ལ་ནི་དད་པས་མོས་པའི་གནས་སྐབས་ནའོ། །

[Block 3204 [HEADING]]
##### ཡོངས་སུ་ཉམས་པ་རྣམ་པ་གསུམ། ^3-2-12-5-0

[Block 3205]
མདོ་ལས་འདི་སྐད་དུ། འདིས་མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པ་ལྷག་པའི་སེམས་ལས་བྱུང་བ་བཞི་ཐོབ་པ་གང་དག་ཡིན་པ་དེ་ལས་གང་ཡང་རུང་བ་ཞིག་ལས་འདི་ཡོངས་སུ་ཉམས་པར་འགྱུར་བར་ནི་ང་སྨྲའི། འདི༌[^2220]གཅིག་པུས་སེམས་ཀྱི་རྣམ་པར་གྲོལ་བ་མི་གཡོ་བའི་བར་དུ་ལུས་ཀྱིས༌[^2221]མངོན་སུམ་དུ་བྱས་པ་གང་ཡིན་པ་དེ་ལས་ནི་འདིའི༌[^2222]རྣམ་གྲངས་གང་གིས་ཀྱང་ཡོངས་སུ་ཉམས་པར་འགྱུར་བར་ན༌[^2223]མི་སྨྲའོ་ཞེས་གང༌[^2224]གསུངས་པ་ཡང་ཇི་ལྟར་ན་མ༌[^2225]གཡོ་བའི་ཆོས་ཅན་མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པ་དག་ལས་ཡོངས་སུ་ཉམས་པར་འགྱུར་ཞེ་ན།

[Block 3206 [VERSE]]
ཐོབ་དང་མ་ཐོབ་ཉེར་སྤྱད་ལས། །
ཡོངས་ཉམས་རྣམ་པ་གསུམ་ཤེས་བྱ། །

[Block 3207]
གལ་ཏེ་ཡོན་ཏན་ཐོབ་པ་ལས་ཡོངས་སུ་ཉམས་ན་ཐོབ་པ་ལས་ཡོངས་སུ་ཉམས་པ་ཡིན་ནོ། །

[Block 3208]
གལ་ཏེ་ཡོན་ཏན་ཐོབ་པར་བྱ་བ་མ་ཐོབ་ན་མ་ཐོབ་པ་ལས་ཡོངས་སུ་ཉམས་པ་ཡིན་ནོ། །

[Block 3209]
གལ་ཏེ་ཡོན་ཏན་ཐོབ་པ་མངོན་སུམ་དུ་མི་བྱེད་ན་ཉེ་བར་སྤྱོད་པ༌[^2226]ལས་ཡོངས་སུ་ཉམས་པ་ཡིན་ནོ། །

[Block 3210 [VERSE]]
ཡོངས་སུ་ཉམས་པ་འདི་རྣམས་ལས། །
སྟོན་པ༌[^2227]ཐ་མ་མི་གཡོ་ལ། །
བར་མའང་གཞན་ལ་རྣམ་གསུམ་མོ། །

[Block 3211]
སངས་རྒྱས་ལ་ན༌[^2228]ཉེ་བར་སྤྱད་པ་ལས་ཡོངས་སུ་ཉམས་པ་ཁོ་ན་མངའི་གཞན་ནི་མི་མངའོ། །

[Block 3212]
མི་གཡོ་བའི་ཆོས་ཅན་ལ་ནི་དེ་དང་མ་ཐོབ་པ་ལས་ཡོངས་སུ་ཉམས་པ་ཡང་ཡོད་དེ། གང་ཟག་ཁྱད་པར་ཅན་གྱི་ཆོས་མ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 3213]
དགྲ་བཅོམ་པ་གཞན་ལ་ནི་ཐོབ་པ་ལས་ཡོངས་སུ་ཉམས་པ་ཡང་ཡོད་དོ། །

[Block 3214]
དེའི་ཕྱིར་མི་གཡོ་བའི་ཆོས་ཅན་ཉེ་བར་སྤྱད་པ་ལས་ཡོངས་སུ་ཉམས་པར་འགྱུར་བའི་ཕྱིར་མདོ་དང་མི་འགལ་ལོ། །

[Block 3215]
ཡོངས་སུ་མི་ཉམས་པར་སྨྲ་བ་ན་རེ་ཐམས་ཅད་ཀྱི་རྣམ་པར་གྲོལ་བ་ཟག་པ་མེད་པ་ནི་མི་གཡོ་བ་ཡིན་ལ། མི་གཡོ་བའི་ཆོས་ཅན་དུ་ཇི་ལྟར་རྣམ་པར་གཞག་པ་ནི་དེ་བཞིན་དུ་བཤད་ཟིན་པ༌[^2229]དེའི་ཕྱིར་འདི་ནི་ཀླན་ཀར་མི་རུང་ངོ་ཞེས་ཟེར་རོ། །

[Block 3216 [HEADING]]
##### འབྲས་ལས་ཉམས་པ་འཆི་བ་མེད་པ། ^3-2-12-6-0

[Block 3217]
ཡང་གང་ཞིག་དགྲ་བཅོམ་པའི་འབྲས་བུ་ལས་ཡོངས་སུ་ཉམས་ན་ཅི་དེ་ཡང་སྐྱེ་འམ་ཞེ་ན། དེ་ལྟ་བུ་ནི་མེད་དེ། [^2230]འདི་ལྟར། འབྲས་ལས་ཉམས་པ་འཆི་བ་མེད། །འབྲས་བུ་ལས་ཡོངས་སུ་ཉམས་པ་ནི་འགའ་ཡང་འཆི་བ་མེད་དེ།

[Block 3218]
མདོ་ལས།

[Block 3219]
དགེ་སློང་དག་འཕགས་པ་ཉན་ཐོས་ཐོས་པ་དང་ལྡན་པ་ལ་དྲན་པ་ཉམས་པ་ཆུང་ངུ་འབྱུང་མོད་ཀྱི་འོན་ཀྱང་ཡང་མྱུར་བ་ཁོ་ནར་ནུབ་པ་དང་ཡོངས་སུ་ཟད་པ་དང་ཡོངས་སུ་གཏུགས་པར་འགྱུར་རོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3220]
དེ་ལྟ་མ་ཡིན་ན་ཚངས་པར་སྤྱོད་པ་ཡིད་བརྟན་དུ་མི་རུང་བར་འགྱུར་རོ། །

[Block 3221]
འབྲས་བུ་གང་ཞིག་ལས་ཡོངས་སུ་ཉམས་པ་ནི་འབྲས་བུ་དེ་ལ་གནས་པས་བྱ་བ་མ་ཡིན་པ་གང་ཡིན་པའི། བྱ་བ་མ་ཡིན་དེ་མི་བྱེད། །ཡོངས་སུ་ཉམས་ཀྱང་འབྲས་བུ་དེ་དང་འགལ་བའི་བྱ་བ་མི་བྱེད་དེ། རྩལ་པོ་ཆེ་བྲེད་པ༌[^2231]རྡེག་མི་འཆའ་བ་བཞིན་ནོ། །

[Block 3222 [HEADING]]
##### དབང་པོ་འཕོ་བ། ^3-2-12-7-0

[Block 3223]
ཡང་དབང་པོ་རྣམས་འཕོ་བ་ལ་བར་ཆད་མེད་པ་དང་རྣམ་པར་གྲོལ་བའི་ལམ་དུ་དག་ཅིག་སྐྱེ་ཞེ་ན། མི་གཡོ་རྣམ་གྲོལ་བར་ཆད་མེད། །ལམ་དགུའོ། །

[Block 3224]
རྟོགས་པའི་སྐལ་བ་ཅན་ཞིག་མི་གཡོ་བའི་རིགས་ཅན་རྟོགས་པར་བྱེད་ན་བར་ཆད་མེད་པའི་ལམ་དགུ༌[^2232]དང་། རྣམ་པར་གྲོལ་བའི་ལམ་དགུ་སྐྱེ་སྟེ། དཔེར་ན་དགྲ་བཅོམ་པ་ཉིད་ཐོབ་པ་བཞིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། དབང་པོ་རྟུལ་པོའི་རིགས་དེ་ཤིན་ཏུ་བརྟེན༌[^2233]ཕྱིར་རོ། །

[Block 3225]
དེས་དབང་པོ་རྟུལ༌[^2234]པོའི་རིགས་དེ་ཤིན་ཏུ་གོམས་པར་བྱས་པ་ཡིན་པས་འབད་པ་ཆུང་ངུས་བཟློག་པར་མི་ནུས་ཏེ། སློབ་པ་དང་མི་སློབ་པའི་ལམ་དག་གིས་བརྟན་པོར་བྱས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
