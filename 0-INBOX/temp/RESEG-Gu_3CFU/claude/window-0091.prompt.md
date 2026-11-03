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
གང་གི་ཚེ་ན་སྤྲད་པར་བྱས་ནས་སྤྲིང་བ་མནོས་པ་དེ་ལ་གོ་བར་བྱས་པར་གྱུར་ན་དེའི་ཚེ་ན་གང་ཞིག་འདི་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་དམ་ངག་གི་རྣམ་པར་རིག་བྱེད་དམ་ཅང་མི་སྨྲ་བར་འཇུག་པ་གང་ཡིན་པས་ལན་སྟེར་བར་བྱེད་ན་བསྐུར་བ༌[^2183]པོ་ལ་མིག་གི་རྣམ་པར་ཤེས་པས་སམ་རྣ་བའི་རྣམ་པར་ཤེས་པས་སམ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་གྲངས་ཇི་ལྟ་བར་བསྐུར་བ་པོའི་ཁས་ལེན་པ་ལ་སྔ་མར་བརྗོད་པ་ལ་ཕྱང་ཡར་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3187]
ཇི་སྲིད་དུ་བསྟན་པར་འགྱུར་ཏེ། དབུས་དང་འབྲེལ་བའི་འཇུག་པ་དེ་གོ་བར་བྱེད་པ་ལ་བརྟེན་པའི་ལོ་རྒྱུས་ལ་དེའི་ཕྲིན་ལན་སྨྲ་བར་གོ་བར་བྱས་པའི་སྤྲིང་བར་བྱ་བས་བསྐུར་བ་པོ་འམ་སྨྲ་བ་པོ་འམ་གཞན་ལས་ཕྲིན་ལན། ཐོས་པ་དང་བྱས་པ་ཉིད་ལ་བསྐུར་བ་ལ་ཕྱང་ཡར་ཉིད་དོ། །

[Block 3188]
སྔ་མ་ལ་བརྗོད་ན་ཅི་ཡང་རུང་བའི་དོན་བསྒྲུབ་པ་ནི་འདིར་ཡན་ལག་གོ། །

[Block 3189]
དེ་ལྟར་འདི་ནི་མ་ཡིན་ཏེ་དེས༌[^2184]ན་བསྐུར་བར་བྱེད་པ་པོས༌[^2185]བསྒྲུབ་པར་འགྱུར་རོ། །

[Block 3190]
གང་གི་ཕྱིར་གལ་ཏེ་དེས་གོ་བར་མི་འགྱུར་ན་འདི་ནི་དེའི་ལན་སྟེར་བར་མི་འགྱུར་རོ། །

[Block 3191]
འདིར་གཞུང་ནི་དགེ་སློང་དེས་སྤྲིང་བ་རྣམ་པ་དེ་ལྟ་བུ་དེ་མནོས་ཏེ། ཕྲིན་ཕར་སྐྱེལ༌[^2186]བར་བྱེད་དམ་ཕྲིན་ཚུར་སྐྱེལ་བར་བྱེད་ན་དགེ་འདུན་ལྷག་མའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3192]
ཕྲིན༌[^2187]ཚུར་བསྐྱལ་བ་ལ་ལྟ་སྨོས་ཅི་དགོས་ཏེ་ཕྲིན༌[^2188]གཏོང་བ་ཙམ་ལ་ཡང་འདིར་དགེ་འདུན་གྱི་ལྷག་མའོ་ཞེས་བྱ་བ་འདིའི་དོན་ཏོ། །

[Block 3193]
གསུམ་པོ་དེ་དག་གི་བྱ་བ་ཉིད་ནི་ཐ་དད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདིར་རྗེས་སུ་བསྒྲུབ་པར་བྱ་བའི་ཚིགས་གསུམ་པོ༌[^2189]གང་དག་སྔར་བསྟན་པ་ནོད་པ་དང་གོ་བར་བྱེད་པ་དང་བརྗོད་པ་ཞེས་བྱ་བ་ཚིགས༌[^2190]དེ་དག་གི་བྱ་བ་ཉིད་ཅེས་བྱ་བ་ནི་རྗེས་སུ་བསྒྲུབ་པར་བྱ་བ་ཉིད་ནི་ཐ་དད་པ་ཉིད་དེ་སྦྱོར་བ་ཐ་དད་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3194]
དེ་བས་ན་སོ་སོར་འདི་རྣམས་ལ་སྦོམ་པོའི་ལྟུང་བའོ། །

[Block 3195]
དེ་ལྟར་ན་འདི་རྣམས་ལ་རེ་རེ་དག་ལ་སྦོམ་པོའི་ལྟུང་བའོ། །

[Block 3196]
[^2191]ཉེས་པ་སྦོམ་པོར་གསུངས་པ་གང་ཡིན་པ་དང་། ཕྱི་མ་མེད་ན་ཡང་ཚིགས་སྔ་མ་ལ་ཉེས་པ་སྦོམ་པོར་གསུངས་པ་གང་ཡིན་པ་དེའི་འདི་བསྡུ་བའོ། །

[Block 3197]
མི་ཉིད་ལ་མཐའི་བྱེད་པ་པོ་ཉིད་མ་ཡིན་པ་ཡང་སྦྱོར་བ་ཉིད་མ་ཡིན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་མི་ཉིད་ནི་མི་ཉིད་དོ། །

[Block 3198]
མིའི་འགྲོ་བ་པ༌[^2192]ཉིད་ཡོད་པར་གྱུར་པ་ལ་མངལ་ན་གནས་པ་དང་རྡེའུ་གསུམ་གཏོར་བ་ལ་སོགས་པར་ནོད་པ་དང་། ཕྲིན་ཕར་སྐྱེལ༌[^2193]ཚུར་སྐྱེལ་བ༌[^2194]རྣམས་ལ་ཡང་དག་པར་སྦྱོར་བ་མེད་པའི་ཕྱིར་སྤྲད་པར་བྱ་བ་ཐོབ་པ་ལ་མི་མཐུན་པ་མེད་པས་དངོས་གཞི་ལ་བྱེད་པ་པོ་ཉིད་མ་ཡིན་ཡང་དེ་ལ་གནོད་པ་ལ་སོགས་པ་ཚིགས་གསུམ་པོ་འདི་རྣམས་ཡོད་པར་གྱུར་པ་ལ་སྦྱོར་བ་ཉིད་མ་ཡིན༌[^2195]ཏེ། འདི་ལྟར་སྦྱོར་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 3199]
དེ་ལ་ཉེ་བ་འཁོར་གྱིས་ཞུས་པ་ལས།

[Block 3200]
མངལ་ན་གནས་པ་ལ་སོགས་པ་ལས་ཉེས་པ་སྦོམ་པོར་གསུངས་པ་དང་།

[Block 3201]
རྣམ་པར་འབྱེད་པ་ལས།

[Block 3202]
རྡེའུ་གཏོར་བ་དང་། ཆོ་ག་བཏང་བ་གཉིས་ཀྱིས་ཉེས་པ་སྦོམ་པོར་གསུངས་པ་དེ་དག་གིས་འདིར་ལུང་གི་དོན་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 3203]
གཉིས་ལ་སོགས་པ་རྣམས་ནི་དགེ་འདུན་ནས་བརྩམས་ཏེ་ཚིགས༌[^2196]འདི་རྣམས་ལ་ལྷན་ཅིག་པའི་དངོས་པོས༌[^2197]ཀུན་དུ་སྤྱོད་པ་ལ་དེའི་སྦྱོར་བ་རྣམས་ལ་ཡང་རེ་རེ་དག་ལ་ལྟུང་བ་རྣམས་བསྐྱེད་པ་དེ་བརྗོད་པར་བྱ་བ་སྟེ། དེའི་ཕྱིར་འབྲས་བུ་གཅིག་ལ༌[^2198]བྱེད་པ་པོ་སོ་སོ་ལ་བྱ་བ་རྫོགས་པར་བྱེད་པ༌[^2199]མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཅིག་པའི་དངོས་པོ་ནི་གཅིག་པ་ཉིད་དེ། འབྲས་བུ་གཅིག་པ་ཉིད་ནི་འབྲས་བུ་གཅིག་པ་ཉིད་དོ། །

[Block 3204]
ནོད་པ་ལ་སོགས་པའི་ཚིགས༌[^2200]ཐམས་ཅད་དང་ལྷན་ཅིག་པའི་དངོས་པོས་གང་ཟག་མང་པོ་རྣམས་ཀྱིས་ཀུན་དུ་སྤྱོད་པ་ལ་ཕྲད་པ་ཞེས་བྱ་བའི་ཐ་མི་དད་པར་འབྲས་བུ་གཅིག་ཅེས་བྱ་བ་འབྲས་བུ་གཅིག་པ་ཉིད་ཀྱིས༌[^2201]འདིར་རེ་རེ་ཡང་ལྟུང་བ་འདི་རྣམས་བསྐྱེད་པ་ལ་མི་སྦྱོར་བ་ཡིད་ལ་འབྲེལ་པར་གྱུར་ཅིང་འདྲེ་བར་མི་འགྱུར་ཏེ་ཞེས་བྱ་བ་འདི་ལྟར་འདི་བརྗོད་པའོ། །

[Block 3205]
འོན་ཀྱང་བྱེད་པ་པོ་དང་བྱེད་པའི་ཕྱིར་བྱ་བ་རྫོགས་པ་ཉིད་དེ་ཐམས་ཅད་ཀྱི་བདག་ཉིད་ཀྱིས་འབྲེལ་པ་ཉིད་དོ། །

[Block 3206]
ལྟུང་བའི་བྱེ་བྲག་དེ་ལྟ་བུར་གྱུར་པ་ལ་རྒྱུ་ཡིན་ཏེ། འབྲས་བུའི་དབྱེ་བ་ནི་མ་ཡིན་ནོ། །

[Block 3207]
གལ་ཏེ་དེ་ལ་འབྲས་བུ་གཅིག་པ་བྱེད་པ་པོ་རེ་རེ་ལ་བྱ་བ༌[^2202]རྫོགས་པར་གནས་པ་ལ་རྒྱུ་ཡིན་པར་གྱུར་ན་འདི་ནི་དེ་ལྟར་འགྱུར་བ་ཡིན་ཏེ། དེ་ནི་ཡོད་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3208]
འདིར་མངགས་པ་ནི་རང་ཉིད་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་གནས་ངན་ལེན་སྨྲ་བ་ལ་སོགས་པ་ལ་མངགས་པ་ལྟ་བུ་ནི་མ་ཡིན་ཏེ། དེར་མངགས་པས་བྱས་པ་མ་ཡིན་པ་མི༌[^2203]རང་གིས་བྱས་པ་འདྲ་བ་མ་ཡིན་པ་ལྟར་དེ་བཞིན་དུ་འདིར་མངགས་པ་གང་ཡིན་པ་དེ་རང་གིས་བྱས་པར་འགྱུར་རོ། །

[Block 3209]
སྤྲད་པར་བྱ་བ་ཉིད་ཀྱིས་དེ་མངགས་པ་སྦྱིན་པར་འགྱུར་རོ། །

[Block 3210]
གང་ཞིག་དེའི་མངགས་པས་སྤྲད་པར་བྱ་བ་ཉིད་ཀྱིས་བརྗོད་པར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་མངགས་པ་ཉིད་ལའོ། །

[Block 3211]
གང་དེ་བྱས་པར་འགྱུར་བ་ལ་མངགས་པ་གང་ཡིན་པ་ཞེས་བྱ་བ་ནི་འདིར༌[^2204]རྣམ་པར་གཞག་པའོ། །

[Block 3212]
མངགས་པའི་བདག་ཉིད་དུ་གྱུར་པ༌[^2205]དེ་མངགས་པ་ལ་རང་གི་མངགས་པ་ཉིད་ཁོ་བོ༌[^2206]ན་སྐྱེ་བར་འགྱུར་བ་ཡིན་གྱི་མངགས་པ་ཉིད་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 3213]
མངགས་པའི་མངགས་པ་ལ་སོགས་པ་ལ་ཡང་འདིས་བདག་ཉིད་ཀྱིས་བྱས་པར་རིག་པར་བྱའོ། །

[Block 3214]
དེ་གཉིས་ཀྱིས་བདག་པོ་དག་ནི་སྤྲད་པར་བྱ་བ་ཉིད་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་སྤྲད་པར་བྱ་བ་སྟེ། བདག་པོ་དབང་བྱེད་པ་ལ་དེར་ངེས་པར་སྦྱོར་བ་བཟློག་པ་དང་སྦྱིན་པ་དང་ཀུན་དུ་ཆད་པ་རྣམས་ལ་ཅི་རིགས་པར་སྤྲད་པར༌[^2207]བྱ་བ་ཉིད་དོ། །

[Block 3215]
འདིར་སྤྲད་པར་བྱ་བའི་ཁྱེའུ་དང་བུ་མོ་དེ་གཉིས་ཀྱི་བདག་པོ་ཕ་མ་ལ་སོགས་པ་གང་དག་ཡིན་པ་དེ་དག༌[^2208]ནི་དེ་ལ་བཟུང་བ་དང་སྨྲ་བ་གང་ཡིན་པ་དེར་སྤྲད་པར་བྱ་བ་ཉིད་ལས་དེ་དང་སྤྲད་པར་བྱ་བ་འམ་ཞེས་བྱ་བ་འདིར་ཤེས་པར་བྱའོ། །

[Block 3216]
གཞན་ལ་བྱས་པ་ཉིད་ནི༌[^2209]ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ལ་གཞན༌[^2210]ལ་ཞེས་བྱ་བ་ནི་བདག་པོ་མ་ཡིན་པ་ལའོ། །

[Block 3217]
སྤྲད་པར་བྱ་བ་དབང་དུ་མི་བྱེད་པ་ཉིད་གང་ཡིན་པ་དེ་ལས་མངགས་པ་སྤྲིང་བ་མནོད་པ་ལ་སོགས་པ་ལ་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3218]
སྤྲིང་ཡིག་དང་ལག་ཡིག་དང་ཡུལ་ཕྱོགས་དང་བརྡ་དང་མཚན་མ་རྣམས་ནི་ཚིག་ཉིད་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་འདིར་ཡོངས་སུ་ཐོབ་པ་བྱེད་པ་ཙམ་ལ་གཙོ་བ༌[^2211]ཉིད་དེ་འདིར་ཐོབ་པ་ལ་དོན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3219]
རྣམ་པ་ཐམས་ཅད་དུ་ཡང་ཕུན་སུམ་ཚོགས་པ་འདི་ཡོངས་སུ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 3220]
དེ་བས་ན་འདིར་སྤྲིང་ཡིག་ལ་སོགས་པ་རྣམས་ལ་ཚིག་ཏུ་གྱུར་པ་ཉིད་དེ་ན་སྨད་པར༌[^2212]བྱེད་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 3221]
ཇི་ལྟར་ཚིག་གིས་ཇི་ལྟར་བསྟན་པའི་དོན་ཡོངས་སུ་ཐོབ་པས་ལྟུང་བ་དེ་བཞིན་དུ་སྤྲིང་ཡིག་ལ་སོགས་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3222]
འདིར་མཚན་མ་ནི་གང་མཐོང་ནས་སོ་སོར་གོ་བ་སྟེ། དཔེར་ན་སྐྲ་དང་ཁ་སྤུ་བྲེགས་ནས་རིང་པོ་མ་ལོན་པ་འམ་གོས་དམར་སེར་གྱོན་པ་ཉིད་དམ་ཡན་ལག་དང་འབྲེལ་པའི་ཤིང་དཔུང་ཆད་ལྟ་བུའོ། །

[Block 3223]
ཡུལ་ནི་ས་ཕྱོགས་ཏེ་སྐྱེད་མོས་ཚལ་ལ་སོགས་པའོ། །

[Block 3224]
བརྡ་ནི་དངོས་པོ་ཅུང་ཟད་མ་ཡིན་པར་གྱུར་པའི་མཚན་མ་སྟེ། དཔེར་ན་སྔ་དྲོ་འམ་ཉི་མ་ཕྱེད༌[^2213]དམ་ཕྱི་དྲོ་ཞེས་བྱ་བའི་དུས་ཀྱི་རྣམ་པར་གཞག་པའོ། །

[Block 3225]
བརྡ་ནི་བརྡའི་ཡུལ་ཉིད་ཀྱི་ཕྱིར་འདིར་བརྡས་བརྗོད་པའོ། །
--- END BLOCKS ---
