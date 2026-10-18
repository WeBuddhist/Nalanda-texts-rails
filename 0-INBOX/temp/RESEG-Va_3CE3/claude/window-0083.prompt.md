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
[Block 2906]
དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་ཅུང་ཟད་ཀྱང་མེད་པའོ། །

[Block 2907]
འདི་ནི་དེ་བཞིན་གཤེགས་པའི་ཁྱུ་མཆོག་ཏུ་གྱུར་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་མཛད་པ་ནི་རྣམ་པར་རིག་པར་བྱ་བ་ཙམ་དུ་ཟད་དེ། གལ་ཏེ་སེམས་ཅན་རྣམས་བདག་ཉིད་ཀྱིས་ཤེས་པར་གྱུར་ན། དེ་བཞིན་གཤེགས་པ་མི་དམིགས༌[^2107]སོ་ཞེས་སྟོན་ཏོ། །

[Block 2908]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་སྟོང་པ་ལགས་ཞེས་བྱ་བ་ནི་ཅི་ཞིག་མེད་པས་སྟོང་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2909]
དེ་ལ་འདུ་བྱེད༌[^2108]པ་གང་ཡིན་པ་དེས་སྟོང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལ་གང་འདུས་བྱས་སོ་ཞེས་འདུ་བྱེད༌[^2109]པ་མཚན་མར་འཛིན་པའི་བདག་ཉིད་དེ་མེད་པས་སྟོང་པའོ། །

[Block 2910]
རབ་འབྱོར་ལ་ལ་ཞིག་གི༌[^2110]སྤྲུལ་པ་སྤྲུལ་ན༌[^2111]ཞེས་བྱ་བ་ནི། སྤྲུལ་པ་འདི་སྤྲུལ་པ་གཞན་པ་གཞན༌[^2112]དག་སྤྲུལ་པ་བྱེད་དོ་ཞེས་བྱ་བ་དེ༌[^2113]སྟོང་པ་མ་ཡིན་པའི་དངོས་པོ་ཅུང་ཟད་ཀྱང་ཡོད་དམ་ཞེས་བྱ་བ་སྟེ། གང་གི་ཚེ་སྤྲུལ་པ་ཞིག་སྤྲུལ་པ་གཞན་སྤྲུལ་པར་བྱེད་པ་དེའི་ཚེ། སྤྲུལ་པ་དེ་ལ་སྟོང་པ་མ་ཡིན་པའི་ངོ་བོ་ཉིད་ཅི་ཡང་ཡོད་དམ་ཞེས་སྨྲས་པའོ། །

[Block 2911]
རབ་འབྱོར་དེ་ཇི་སྙམ་དུ་སེམས་རྣམ་པར་སྦས་སམ་ཞེས་བྱ་བ་ནི་འདི་ནི་སྤྲུལ་པའོ། །

[Block 2912]
འདི་ནི་སྟོང་པ་ཉིད་དོ་ཞེས་བྱ་བ་དེ་ཅི་སྟོང་པ་ཉིད་ཀྱིས་རབ་ཏུ་བསྒྲིབས་སམ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2913]
ལ་ལ་ནི་ཉན་ཐོས་ཀྱིས་སྤྲུལ་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ། ཚིག་རྣམ་པ་བཞིས་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་འཇིག་རྟེན་པ་དང་། འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་རྣམས་བསྟན་ཏོ། །

[Block 2914]
ཉོན་མོངས་པས་སྤྲུལ་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་དང་སྲོག་ལ་སོགས་པ་བསྟན་པའོ། །

[Block 2915]
ལས་ཀྱིས་སྤྲུལ་པ་ཞེས་བྱ་བ་ནི་ཕུང་པོ་དང་། ཁམས་དང་སྐྱེ་མཆེད་ལ་སོགས་པ་བསྟན་པའོ། །

[Block 2916]
བསྐྱེད་པའམ་བཀག་པ་ཞེས་བྱ་བ་ནི་འདུས་བྱས་ཀྱི་ཆོས་རྣམས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2917]
མི་སླུ་བའི༌[^2114]ཆོས་ཅན་མྱ་ངན་ལས་འདས་པ་ཞེས་བྱ་བ་ལ་མྱ་ངན་ལས་འདས་པ༌[^2115]ནི་བསླུ་བར་བྱ་བའམ་དོར་བའམ། ཡོངས་སུ་ཉམས་པར་འགྱུར་བའི་ཆོས་རྣམས་མེད་ཅིང་། བསྣན་པར་བྱ་བ༌[^2116]ཡང་མེད་པའི་ཕྱིར་མི་སླུ་བའི་ཆོས་ཅན་ཞེས་བྱ་བའོ།

[Block 2918]
[^2117] །གང་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་སྟོང་པ་ཉིད་ལས་ཀྱང་མི་གཡོ་ལ༌[^2118]གཉིས་ཀྱིས་ཀྱང་མི་གོས་ཞེས་བཀའ་སྩལ་པ་ལྟར་ན་ཞེས་བྱ་བས་འདི་སྐད་བསྟན་པར་འགྱུར་ཏེ། སྟོང་པ་ཉིད་ལས་མི་གཡོ་ཞེས་གསུངས་པས་སྟོང་པ་ཉིད་ནི་མི་གཡོའི། དེ་ལས་གཞན་པ་དག་ནི་གཡོའོ་ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 2919]
གཉིས་ཀྱིས་ཀྱང་མི་གོས་སོ་ཞེས་གསུངས་པས་ནི་ཡོད་པ་དང་། མེད་པ་གཉིས་ཀྱིས་མི་གོས་སོ་ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 2920]
དེ་ལ་གལ་ཏེ་མྱ་ངན་ལས་འདས་པ་ཞེས་བྱ་བའི་ཆོས་འགའ་ཞིག་ཡོད་ན་ནི་སྟོང་པ་ཉིད་ལས་མ་གཏོགས་པ་གཞན་ཞིག་ཡོད་པར་འགྱུར་ཏེ། ཡོད་པས་གོས་པར་ཡང་འགྱུར་རོ། །

[Block 2921]
དེ་བས་ན་ཚིག་དེ་བརྩན་པར་བྱས་ནས་མྱ་ངན་ལས་འདས་པ་ཡང་སྤྲུལ་པ་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱ་བར་འགྱུར་རོ། །

[Block 2922]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་མྱ་ངན་ལས༌[^2119]འདས་པ་ཞེས་བྱ་བའི་ཆོས་གཞན་དངོས་པོའི་བདག་ཉིད་དུ་ནི་གང་ཡང་མེད་པས་དེ་ཡང་སྟོང་པ་ཉིད་ཡིན་པར་རབ་འབྱོར་དེ་དེ་བཞིན་ནོ། །

[Block 2923]
དེ་དེ་བཞིན་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྟོན་ཏོ། །

[Block 2924]
བཅོམ་ལྡན་འདས་ལས་དང་པོ་པ་ལ་ཇི་ལྟར་གདམས་པར་བགྱི་ཞེས་བྱ་བ་ནི་ད་ལྟར་ཟབ་པའི་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་ཡོངས་སུ་ཤེས་པར་ནུས་པའི་གདམས་པ་ཞུས་པའོ། །

[Block 2925]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་འདི་སྐད་བཀའ་སྩལ་ཏེ། གལ་ཏེ་སྔོན་དངོས་པོ་ཡོད་པར་གྱུར་ལ་ཕྱིས་རྣལ་འབྱོར་པ་དག་གིས༌[^2120]ཤེས་པའི་མཐུས་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་ཀྱིས་དངོས་པོ་མེད་པར་བྱས་ན༌[^2121]ནི་དེ་ལྟ་ན། ལས་དང་པོ་པ་དཀའ་བ་སྤྱོད་པར་འགྱུར་བ་ཞིག་ན། འདི་ལྟར་དངོས་པོ་ཡང༌[^2122]དངོས་པོའི་བདག་ཉིད་དུ་ཀུན་བརྟགས་པའི༌[^2123]ཡིན་པས་མེད་དོ། །

[Block 2926]
དངོས་པོ་མེད་པ༌[^2124]རི་བོང་གི་རྭ་ལྟ་བུ་ཡང་མ་ཡིན་ནོ། །

[Block 2927]
རང་གི་དངོས་པོ་ཡང༌[^2125]གང་ཡང་རུང་བའི་རང་དབང་ཅན་མེད་དོ། །

[Block 2928]
གཞན་གྱི་དངོས་པོ་ཡང་རྒྱུ་དང་རྐྱེན་ལ་སོགས་པའི་དབང་གིས་ཡོད་པ་མ་ཡིན་ན། དེ་ལ་ངོ་བོ་ཉིད་ཅེས་བྱ་བའི་ཆོས་གཞན་གང་ཡང་ཡོད་པར་ག་ལ་འགྱུར། དེ་བས་ན་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་ཀྱང་ངོ་བོ་ཉིད་ཀྱིས་སོ་ཞེས་ཤེས་པས་ཉེས་པ་མེད་དོ།། །།

[Block 2929]
བམ་པོ་ཉི་ཤུ༌[^2126]

[Block 2930 [HEADING]]
## ཉི་ཁྲི་ལྔ་སྟོང་པ་ལས་འབྱུང་བ་བཤད་པ། ^2-0

[Block 2931]
བདུན་པ་སྟེ་ཐ་མ། དེ༌[^2127]ལྟར་བཅོམ་ལྡན་འདས་མ་འབུམ་པའི་བཤད་པ་ཡོངས་སུ་རྫོགས་པར་བྱས་ནས། ད་ནི་ཉི་ཁྲི་ལྔ་སྟོང་པ་ལས་གང་འབྱུང་བ་དེ་བཤད་པར་བྱའོ། །

[Block 2932 [HEADING]]
### ཆོས་ཐམས་ཅད་མིང་ཙམ་དུ་ཟད་པ། ^2-1-0

[Block 2933]
དེ་ནས་འཕགས་པ་བྱམས་པས་མ་འོངས་པའི་སྐྱེ་བོ་རྣམས་ཀྱི་དོན་དང་། དེའི་ཚེ་འདུས་པའི་འཁོར་གྱི་འདུལ་བ་རྣམས་ཀྱི་དོན་དུ་བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པ། བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་ལ་སློབ་པར་འཚལ་བས་གཟུགས་ལ་ཇི་ལྟར་བསླབ་པར་བགྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་ཞུས་སོ། །

[Block 2934]
ཆོས་ཐམས་ཅད་ལ་ཚུལ་བཞིན་དུ་ཡོངས་སུ་ཤེས་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་སྟེ། དེ་བས་ན་བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་ལ་སློབ་པར་འདོད་པས་གཟུགས་ལ་སོགས་པ་ནས། སངས་རྒྱས་ཀྱི་ཆོས་ཀྱི་མཐར་ཐུག་པའི་བར་དག་ལ་ཇི་ལྟར་བསླབ་པར་བགྱི་ཞེས་ཞུས་པའོ། །

[Block 2935]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་སྟོང་པ་ཉིད་ལ་སློབ་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པའོ་ཞེས་བསྟན་པའི་ཕྱིར། གཟུགས་མིང་ཙམ་ཞེས་བྱ་བ་ནས། སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཀྱི་བར་དུ་མིང་ཙམ་མོ་ཞེས་བྱ་བར་བསླབ་པར་བྱའོ་ཞེས་བྱ་བའི་བར་དག་གིས་ཆོས་ཐམས་ཅད་མིང་ཙམ་དུ་ཟད་པར་གསུངས་སོ། །

[Block 2936]
བཅོམ་ལྡན་འདས་གང་གི་ཚེ། འདི་ལྟ་སྟེ་གཟུགས་ཞེས་བགྱི་བའི་མིང་འདི་དངོས་པོ་དང་བཅས་པར་དམིགས་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་སྟོན་ཏེ། གཟུགས་དང་ཚོར་བ་ཞེས་བྱ་བ་ལ་སོགས་པའི་མིང་བརྗོད་པ་ནི༌[^2128]མིང་ཙམ་འབའ་ཞིག་སྟོན་པ་མ་ཡིན་གྱི། མིང་སྨོས་པ་སྔོན་དུ་བཏང་བས་དངོས་པོའི་རྣམ་པ་འབའ་ཞིག་བློ་ལ་གཞག་ནས་དངོས་པོ་སྟོན་ན། དེ་ལ་ཇི་ལྟར་གཟུགས་ལ་སོགས་པ་མིང་ཙམ་ཡིན་ཞེས་ཞུས་པའོ། །

[Block 2937]
མིང་དེ་དངོས་པོ་མེད་པ་ཞིག་ཡིན་ན་ནི་མིང་ཙམ་ཞེས་བྱ་བ་དེ་ཡང་མི་རིགས་པར་འགྱུར་རམ། གཟུགས་ལ་སོགས་པར་དངོས་པོ་མེད་པར་མི༌[^2129]འབའ་ཞིག་ཡོད་དུ་ཟིན་ན་ཅི་ལ་གནས་ཤིང་གནས་གང་གིས་མིང་དེ་འཇུག་པར་འགྱུར་ཏེ། མིང་དེ་ཡང་མེད་པར་འགྱུར་རོ། །

[Block 2938]
དེ་བས་ན་མིང་ཙམ་ཞེས་བྱ་བ་ཡང་མི་རིགས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2939]
འདི་ལྟ་སྟེ། གཟུགས་ཞེས་བྱ་བ་འདི་ནི་འདུ་བྱེད་ཀྱི་མཚན་མའི་དངོས་པོ་དེ་དང་དེ་ལ་གློ་བུར་དུ་མིང་བཏགས་པའོ༌[^2130]ཞེས་བྱ་བ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་བཀའ་སྩལ་པ་སྟེ་གཟུགས་ལ་སོགས་པ་ནི་མིང་གི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ། །

[Block 2940]
གལ་ཏེ་མིང་གི་ངོ་བོ་ཉིད་ཡིན་དུ་ཟིན་ན་བརྗོད་པ་ཙམ་གྱིས་འབྲེལ་པས༌[^2131]མི་ཤེས་པ་རྣམས་ཀྱང་དངོས་པོ་དེ་དག་གི་ངོ་བོ་ཉིད་དང་། ཁྱད་པར་རྣམ་པ་སྣ་ཚོགས་རྟོགས་པར་གྱུར་པའི༌[^2132]རིགས་ན་དེ་དག་རྟོགས་པ་ཡང་མ་ཡིན་ཏེ། དེ་བས་ནི༌[^2133]མིང་ཡང་གཞན་ལ། གཟུགས་ལ་སོགས་པའི་དངོས་པོ་ཡང་གཞན་ཏེ། ཐ་སྙད་དུ་རུང་བར་བྱ་བའི་ཕྱིར་དངོས་པོ་དེ་དང་དེ་དག་ལ་ཕྱིས་མིང་དེ་འབྱུང་བ༌[^2134]ཙམ་དུ་ཟད་དོ། །

[Block 2941]
[^2135]དེ་བས་ན་གཟུགས་ལ་སོགས་པའི་མིང་གི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ། །

[Block 2942]
གློ་བུར་ཞེས་བྱ་བ་ནི་ཕྱིས་བྱུང་བ་སྟེ། བཅོས་མའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2943]
འདུ་བྱེད་ཀྱི་མཚན་མའི་དངོས་པོ༌[^2136]ཞེས་བྱ་བ་ནི་རྒྱུ་དང་རྐྱེན་ལས་བྱུང་བའི་ཕྱིར་འདུ་བྱེད་དོ། །

[Block 2944]
རྣམ་པར་ཤེས་པ་ལ་སྣང་བའི་ཕྱིར་མཚན་མའོ། །

[Block 2945]
དངོས་པོའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་དངོས་པོ་སྟེ། འདུ་བྱེད་ཀྱི་ཆོས་སུ་སྣང་བའི་གཞི་ལ། དངོས་པོ་ཞེས་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །
--- END BLOCKS ---
