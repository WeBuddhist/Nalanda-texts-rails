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
[Block 3046 [HEADING]]
##### ཆོས་ཉིད་ཀྱི་གཟུགས། ^2-3-1-3-0

[Block 3047]
གང་ཆོས་ཉིད་ཀྱི་གཟུགས་བདག་མེད་པས་རབ་ཏུ་ཕྱེ་བ་དེ་ཇི་ག་གཟུགས་ཡིན་ནམ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གྲུབ་པ་ཆོས་ཉིད་ཀྱི༌[^2259]གཟུགས་དེ་མཚན་མ་ཐམས་ཅད་དང་བྲལ་བའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་ཀྱང་མ་ཡིན་ནོ། །

[Block 3048]
གཟུགས་ཀྱི་ཆོས་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་གཟུགས་མ་ཡིན་པ་ཡང་མ་ཡིན་ཏེ། དེ་བས་ན་ཆོས་ཉིད་ཀྱི་གཟུགས་དེ༌[^2260]ཉིད་ཀྱི་གཟུགས་ཀྱི་ཆོས་ཉིད་གང་ཡིན་པ་དེ་གཟུགས་མ་ཡིན་པ་ཡིན་ནམ་ཞེས་བྱ་བ་གསུངས་ཏེ། ཆོས་ཉིད་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་གཟུགས་ཀྱང་མ་ཡིན་གཟུགས་ཀྱི་ཆོས་ཉིད་ཡིན་པའི་ཕྱིར་གཟུགས་མ་ཡིན་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ནི་གཉིས་སུ་མེད་པའི་དོན་ཏོ། །

[Block 3049]
དེ་བས་ན་དེ་ནི་གཉིས་སུ་མེད་པའི་གྲངས་སུ་བྱས་པའོ་ཞེས་བྱ་བ་ནི། དེ་བཞིན་ཉིད་ཀྱི་གྲངས་སུ་བྱས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3050]
[^2261]དེ་བཞིན་དུ་སངས་རྒྱས་ཀྱི་ཆོས་ཀྱི་མཐར་ཐུག་གི་བར་དུ་གཉིས་སུ་མེད་པར་སྦྱར་བར༌[^2262]བྱའོ། །

[Block 3051 [HEADING]]
#### བདེན་པ་བཞི་པོ་དག་ལ་གཉིས་སུ་མེད་པའི་མཚན་ཉིད། ^2-3-2-0

[Block 3052]
དེ་ལྟར་གཟུགས་ལ་སོགས་པ་སངས་རྒྱས་ཀྱི་ཆོས་ཀྱི་མཐར་ཐུག་གི་བར་དུ་གཉིས་སུ་མེད་པར་བསྟན་ནས། དེའི་འོག་ཏུ་རྣམ་པ་གཞན་གྱིས་བདེན་པ༌[^2263]བཞི་པོ་དག་ལ་གཉིས་སུ་མེད་པའི་མཚན་ཉིད་བསྟན་པའི་ཕྱིར་གང་ཡོངས་སུ་ཤེས་པ་ཡང་མ་ཡིན། ཡོངས་སུ་མི་ཤེས་པ་ཡང་མ་ཡིན་པ་དེ་ཉིད་དེའི་ཡོངས་སུ་ཤེས་པའོ་ཞེས་བྱ་བ་གསུངས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་མཚན་ཉིད་མཉམ་པར་གཞག་པའི་ཡིད་ལ་བྱེད་པས་ཡོངས་སུ་ཤེས་པ་མ་ཡིན་གྱི། ཉན་ཐོས་ལྟར་མཉམ་པར་མ་བཞག༌[^2264]པར་ཡོངས་སུ་འདྲིས་པའི་ཤེས་པས་ནི་ཡོངས་སུ་ཤེས་ཏེ་ཇི་ལྟར་སྔར༌[^2265]བསྟན་པ་བཞིན་ནོ། །

[Block 3053]
དེ་བས་ན་དེ་ལྟར་ཤིན་ཏུ་ཡོངས་སུ་ཤེས་པ་མ་ཡིན་པ་འདི་ཉིད་དེའི་ཡོངས་སུ་ཤེས་པའོ། །

[Block 3054]
དེ་བཞིན་དུ་སྤང་བ༌[^2266]དང་། མངོན་སུམ་དུ་བྱ་བ་དང་། བསྒོམ་པ་རྣམས་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 3055 [HEADING]]
### བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་མྱ་ངན་ལས་འདས་པ། ^2-4-0

[Block 3056]
དེ་ལྟར་གཉིས་སུ་མེད་པའི་མཚན་ཉིད་ལ་མཁས་པ་དེ་འབྱུང་བ་ལ་མཁས་པར་བྱ་བ་བསྟན་པའི་ཕྱིར། བྱམས་པ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་མྱ་ངན་ལས་འདས་པ་ནི་ཟབ་པོ་མཆོག་ཏུ་ཟབ་པོ༌[^2267]ཞེས་བྱ་བས་མྱ་ངན་ལས་འདས་པ་སྟོན་ཏོ། །

[Block 3057]
ཇི་ལྟར་ཟབ་ཅེས༌[^2268]ཞུས་པ་དང་། འདི་ལྟར་མྱ་ངན་ལས་འདས་པ་ཡང་མ་ཡིན། མྱ་ངན་ལས་མ་འདས་པ་ཡང༌[^2269]མ་ཡིན་ཏེ། དེའི་ཕྱིར་ཟབ་པ་དང་། མཆོག་ཏུ་ཟབ་ཅེས༌[^2270]བྱའོ་ཞེས་བྱ་བས༌[^2271]བསྟན་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་མྱ་ངན་ལས་འདས་པ་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་ཡོངས་སུ་དག་པ་གནས་གྱུར་པ་ལ་བྱ་སྟེ། གནས་གྱུར་པ་དེ་ཡང་། འདི་ལྟར་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་ཐམས་ཅད་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པའི་ངོ་བོ་ཉིད་དང་། ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པའི་ངོ་བོ་ཉིད་ཡིན་ཏེ། དེའི་ཕྱིར་མྱ་ངན་ལས་འདས་པའོ། །

[Block 3058]
འདི་ལྟར་ཉན་ཐོས་དང་། རང་སངས་རྒྱས་དག་ལྟ་བུ་མ་ཡིན་གྱི༌[^2272]འཁོར་བ་ཡོད་ཀྱི་བར་དུ། སེམས་ཅན་གྱི་དོན་མཛད་དེ། དེའི་ཕྱིར་མྱ་ངན་ལས༌[^2273]འདས་པ་མ་ཡིན་ནོ། །

[Block 3059]
དེ་ནས་བྱམས་པས་གསོལ་པ། བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་གཞན་གྱི་དོན་ལས་བརྩམས་ཏེ། འཁོར་བ་ཡོངས་སུ་མི་གཏོང་ན། འདིས་ཇི་ལྟར་མྱ་ངན་ལས་འདས་པ་ཡོངས་སུ་བཏང་བར༌[^2274]མི་འགྱུར་ཞེས་བྱ་བ་ནི། གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་འཁོར་བ་ཡོད་ཀྱི་བར་དུ་སེམས་ཅན་གྱི་དོན་རྒྱུན་མི་གཅོད་པར་རྟག་ཏུ་འཁོར་བ་ཡོངས་སུ་མི་གཏོང་ན། དེ་ལྟ༌[^2275]ན་མྱ་ངན་ལས་འདས་པར་ཇི་ལྟར་འགྱུར་ཞེས་ཞུས་པའོ། །

[Block 3060]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བྱམས་པ་གཞན་གྱི་དོན་ལས་བརྩམས་ཏེ། འཁོར་བ་ཡོངས་སུ་མི་གཏོང་བས་མྱ་ངན་ལས་འདས་པ་འང་མ་ཡིན་ནོ། །

[Block 3061]
བདག་གི་དོན་ལས་བརྩམས་ཏེ་མྱ་ངན་ལས་འདས་པ་ཡོངས་སུ་མི་གཏོང་བས་མྱ་ངན་ལས༌[^2276]འདས་པ་འང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ། བཅོམ་ལྡན་འདས་ཀྱིས་ནི་གཞན་གྱི་དོན་ལས་བརྩམས་ནས། འཁོར་བ་ཡོངས་སུ་མི་གཏོང་ཞིང་ཕུང་པོ་མེད་པའི་མྱ་ངན་ལས་འདས་པ་མི་ལེན་ཏེ། དེ་བས་ན་མྱ་ངན་ལས་འདས་པ་འང་མ་ཡིན་ནོ། །

[Block 3062]
[^2277]བདག་གི༌[^2278]དོན་ལས་བརྩམས་ཏེ། བྱ་བ་བྱས་པའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་ཡོངས་སུ་མི་གཏོང་ཞིང་འཁོར་བ་ཡང་མི་ལེན་ཏེ། དེ་བས་ན་མྱ་ངན་ལས་འདས་པའོ་ཞེས་བྱ་བས་ཇི་སྐད་བསྟན་པར་འགྱུར་ཞེ་ན། ཆོས་ཀྱི་སྐུ་ལས་བརྩམས་ཏེ། དེ་བས་ན་མྱ་ངན་ལས་འདས་པའོ་ཞེས་བྱ་བས་ཇི་སྐད༌[^2279]བསྟན་པར་འགྱུར་ཞེ་ན། ཆོས་ཀྱི་སྐུ་ལས་བརྩམས་ཏེ་མྱ་ངན་ལས་འདས་པའོ། །

[Block 3063]
སྤྲུལ་པའི་སྐུ་དང་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུའི་དབང་གིས་ནི་མྱ་ངན་ལས་འདས་པ་མ་ཡིན་ནོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 3064]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་གཞན་གྱི་དོན་ལས་བརྩམས་ཏེ་འཁོར་བ་ཡོངས་སུ་མི་གཏོང་ན་འཁོར་བ་ཡོངས་སུ་མ༌[^2280]བཏང་བས་འདིས་ཇི་ལྟར་མྱ་ངན་ལས་འདས་པ་ཡོངས་སུ་བཏང་བར༌[^2281]མི་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་བསྟན་ཏེ། གལ་ཏེ་གཞན་གྱི་དོན་གྱི༌[^2282]ཕྱིར་འཁོར་བ་ཡོངས་སུ་མི་གཏོང་ན། འདིས་མྱ་ངན་ལས་འདས་པ་ཡོངས་སུ་བཏང་བར༌[^2283]འགྱུར་རོ། །

[Block 3065]
གལ་ཏེ་བདག་གི་དོན་དུ་མྱ་ངན་ལས་འདས་པ་ཡོངས་སུ་མི་གཏོང་ན་འདིས་འཁོར་བ་ཡོངས་སུ་བཏང་བར་འགྱུར་རོ། །

[Block 3066]
དེ་བས་ན་འཁོར་བའི་ཡོངས་སུ་མི་གཏོང་བ་དང་། གཏོང་བ་དང་། [^2284]མྱ་ངན་ལས་འདས་པ་དང་། མྱ་ངན་ལས་མ་འདས་པ་ཞེས་བྱ་བ་དེ་དག་འགལ་བ་ཡིན་ན། དེ་ཇི་ལྟར་མི་འགལ་བར་འགྱུར་ཞེས་ཞུས་པའོ། །

[Block 3067]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་འཁོར་བ་ལ་ཡང་འཁོར་བ་ཉིད་དུ་རྣམ་པར་མི་རྟོག་ཅེས་བྱ་བ་ལ་སོགས་པས་མི་འགལ་བར་སྟོན་ཏོ། །

[Block 3068]
[^2285]བྱང་ཆུབ་སེམས་དཔའ་ནི་ཆོས་ཐམས་ཅད་ལ་རྣམ་པར་མི་རྟོག༌[^2286]ཅིང་མཉམ་པ་ཉིད་ཙམ་དུ་མཐོང་བས། འཁོར་བ་ལ་འཁོར་བའོ་ཞེས་སྤྲོས་པ་དང་། མྱ་ངན་ལས་འདས་པ་ཡང་མྱ་ངན་ལས་འདས་པའོ་ཞེས་སྤྲོས་པས་སྤྲོས་པར་མི་བྱེད་དེ། དེ་བས་ན་མཉམ་པ་ཉིད་ལ་གནས་སོ། །

[Block 3069]
མཉམ་པ་ཉིད་ལ་གནས་པས་ན་གང་ལ་ཡང་ཉེས་དམིགས་སུ་མཐོང་བས་བློ་ཞུམ་པར་འགྱུར་བ་དང་། གང་ལ་ཡང་ཕན་ཡོན་དུ་མཐོང་བས་སྦྱོར་བར་འགྱུར་བ་དེ་ལྟ་བུ་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3070]
དེ་ནས་འཕགས་པ་བྱམས་པ་དེས་ཀྱང་མ་མགུ་ནས་བཅོམ་ལྡན་འདས་འོ་ན་བྱང་ཆུབ་སེམས་དཔའ་རྣམ་པར་མི་རྟོག་པའི་དབྱིངས་ལ་གནས་པས། འཁོར་བ་ཇི་ལྟར་མ་བཏང་བ་དེ་ལྟར་བླངས་པ་ཡང་མ་མཆིས་ཤིང་མྱ་ངན་ལས་འདས་པ་ཇི་ལྟར་མ་བཏང་བ་དེ་ལྟར་བླངས་པ་མ་མཆིས་པར་ཡང་མི་འགྱུར་ལགས་སམ། བཅོམ་ལྡན་འདས་གལ་ཏེ་བླངས་པ་མ་མཆིས་ན། ཇི་ལྟར་མ་བཏང་བ་ལགས་ཞེས་བྱ་བ་ཞུས་ཏེ། གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་འཁོར་བ་དང་། མྱ་ངན་ལས་འདས་པ་ལ་རྣམ་པར་མི་རྟོག་པས། མཉམ་པ་ཉིད༌[^2287]དམིགས་ན། དེ་ལྟ་ན་ནི་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་དག་གཏོང་བ་ཡང༌[^2288]མེད། ལེན་པ་ཡང་མེད་དོ་ཞེས་བྱ་ན། དེ་ལ་གལ་ཏེ་ལེན་པ་མེད་ན་ཇི་ལྟར་བཏང་བར༌[^2289]མི་འགྱུར་ཞེས་ཞུས་པའོ། །

[Block 3071]
བྱམས་པ་ད༌[^2290]ནི་འདི་ལྟར་འཁོར་བ་ལེན་ཏོ་ཞེའམ་མི་ལེན་ཏོ་ཞེས་མི་སྨྲའོ་ཞེས་བྱ་བས་འདི་སྐད་གསུངས་ཏེ། ང་ནི་འཁོར་བ་སྤོང་བ་དང་། མི་སྤོང་བའི་དབང་གིས་ལེན་པ་དང་། འདོར་བར་མི་སྨྲའི། དགོས་པ་ལ་ལྟོས༌[^2291]ནས་བྱ་བ་བྱེད་པའི་དབང་གིས་སྨྲ་སྟེ། འདི་ལྟར་མངོན་པར་ཤེས་པའི་མཐུས་དུས་ཐམས་ཅད་དུ་འཇིག་རྟེན་གྱི་ཁམས་མཐའ་ཡས་པ་རྣམས་སུ་སེམས་ཅན་གྱི་ཁམས༌[^2292]ཀྱི་དོན་ཤིན་ཏུ་རྒྱུན་མི་འབྱེད་པར༌[^2293]བྱེད་དེ།[^2294] དེའི་ཕྱིར་འཁོར་བ་ཡོངས་སུ་མི་གཏོང་ཞེས་སྨྲའི། འཁོར་བ་མི་སྤོང་བའི་ཕྱིར་ནི་མ་ཡིན་ནོ། །

[Block 3072]
འདི་ལྟར་སྟོང་པ་ཉིད་ཀྱི་དབྱིངས་དམིགས་སུ་མེད་པའི་དབྱིངས་ཉེ་བར་བཟུང་ནས། དེ་ལ་གནས་ཏེ། དེའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་ལེན་ཏོ་ཞེས་སྨྲའོ་ཞེས་བསྟན་པའོ། །

[Block 3073]
བཅོམ་ལྡན་འདས་རྣམ་པར་མི་རྟོག་པའི་མཚན་ཉིད་འདུས་པ་ཇི་ལྟར་བལྟ་བར་བགྱི་ཞེས་བྱ་བ་ནི། ཇི་ལྟར་རྣམ་པར་མི་རྟོག་པ་ཡོངས་སུ་རྫོགས་ཤིང་མཐར་ཕྱིན་པ་ལགས་ཞེས་ཞུས་པའོ། །

[Block 3074]
དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉིས་སུ་མེད་པ་ཞེས་བྱ་བ་ནི། ཡོད་ཅེས་བྱ་བའམ་མེད་ཅེས་བྱ་བའི་གཉིས་སུ༌[^2295]མེད་པའོ། །

[Block 3075]
སྤྲོས་པ་མེད་པ་ཞེས་བྱ་བ་ནི། ཆོས་དེ་རྣམས་ལ་རྣམ་པ་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 3076 [HEADING]]
### ཉན་ཐོས་ཐམས་ཅད་གཅིག་ཏུ་ངེས་པར་གཏན་དུ་མྱ་ངན་ལས་འདས་པ་ལ་གནས་པ། ^2-5-0

[Block 3077]
བཅོམ་ལྡན་འདས་ཅི་ལགས་ཉན་ཐོས་ཐམས་ཅད་གཅིག་ཏུ་ངེས་པར་གཏན་དུ་མྱ་ངན་ལས་འདས་པ་ལ་གནས་པ་ལགས་སམ་ཞེས་བྱ་བ་ནི། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་འཁོར་བ་མི༌[^2296]ལེན་ཏོ་ཞེས་འབྱུང་བས་ཉན་ཐོས་རྣམས་ལེན་པ་མེད་པར་ཤིན་ཏུ་མྱ་ངན་ལས་འདས་པ་ཉིད་དུ་འགྱུར་རོ་སྙམ་དུ་དགོངས་ནས་ཞུས་པའོ། །

[Block 3078]
སེམས་ཅན་རྣམས་ཀྱི་རིགས་དང་། རང་བཞིན་མང་དུ་དམིགས་ཞེས་བྱ་བ་ནི་སེམས་ཅན་རྣམས་ཀྱི་རིགས་རྣམས་དང་། རང་བཞིན་རྣམས་མང་བ་སྟེ་རིགས་ནི་རྣམ་པ་གསུམ་མོ། །

[Block 3079]
རང་བཞིན་ཡང་བསམ་པ་དང་། བག་ལ་ཉལ་དང་། མོས་པ་དང་། དབང་པོ་ལ་སོགས་པའི༌[^2297]བྱེ་བྲག་གིས་ཐ་དད་པ་རྣམས་སོ། །

[Block 3080]
བཟང་པོའི་བྱེ་བྲག་དོན་དུ་གཉེར་ཏེ། བཟང་པོའི་བྱེ་བྲག་ཉིད་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བ་ནི།

[Block 3081]
དང་པོ་ཉིད་ནས་རང་བཞིན་གྱིས་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་འདོད་ལ།[^2298] ཇི་ལྟར་འདོད་པ་བཞིན་དུ་འཐོབ་པའོ། །

[Block 3082]
དམན་པ་ཞེས་བྱ་བ་ནི། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་བྱང་ཆུབ་པོ། །དམན་པར་ཤེས་ནས་དེ་ཙམ་གྱིས་ཆོག་པར་མི་འཛིན་ཅེས་བྱ་བ་ནི་འཕགས་པའི་གང་ཟག་ཏུ་འགྱུར་ཏེ། ཉན་ཐོས་ཉིད་ཐོབ་ནས་ཕྱིས་སངས་རྒྱས་སུ་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3083]
སྐྱེ་བ་མ་མཆིས་པས་ཇི་ལྟར་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བ་ནི་འཁོར་བར་སྐྱེས་ན་ནི་བྱང་ཆུབ་ཀྱི་ཚོགས་ཡོངས་སུ་རྫོགས་པར་བྱ་ནུས་སོ་སྙམ་དུ་དགོངས་པའོ། །

[Block 3084]
[^2299]དེའི་སྐྱེ་བ་ལགས་པར་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་མ༌[^2300]སྩལ་ཏོ་ཞེས་བྱ་བ་ནི། རྒྱུན་དུ་ཞུགས་པ་ནི་འདིར་སྲིད་པ་བརྒྱད་པ་མི་སྐྱེད༌[^2301]དོ། །

[Block 3085]
ལན་ཅིག་ཕྱིར་འོང་བ་ནི་འདིར་སྲིད་པ་གཅིག་ལེན་ཏོ། །
--- END BLOCKS ---
