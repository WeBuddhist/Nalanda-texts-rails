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
མཛའ་བོ་དང་མགྲོན༌[^2182]དང་གཉེན་བཤེས་དང་། སློང་བ་རྣམས་ནི་རེ་ཐག་མི་གཅོད་ཅེས་བྱ་བ་ནི་སྦྱིན་པའི་ལས་ཀྱིས་སོ། །

[Block 3397]
ཆོས་ལ་གཞོལ་བ་ཞེས་བྱ་བ་ནི་འཚེ་བ་སྤངས་པའི་མཆོད་སྦྱིན་གྱི་ལས་སོ། །

[Block 3398]
འདུལ་བ་ལ་ནི་རྟག་ཏུ་འབད། །ཅེས་བྱ་བ་འདིས་ནི་ཆོས་ལ་གཞོལ་བར་བྱ་བ་ཉིད་བསྟན་ཏེ། འདི་དག་ནི་སླའོ། །

[Block 3399]
དེ་ལྟར༌[^2183]ཞེས་བྱ་བ་ནི། འདུལ་བ་ལ་ནི་རྟག་ཏུ་འབད། །ཅེས་བྱ་བ་ལ་སོགས་པ་གསུམ་ལ་ལེགས་པར་འཇུག་པས་སོ། །

[Block 3400]
རང་གི་ཆོས་ལ་འབད་པས་ནི་གྲགས་པ་དང་། སྲིད་དང་བདེ་བ་འགྲུབ་སྟེ། གསུམ་གྱི་དོན་ལ་ལེགས་པར་ཞུགས་ན་ནི་དགའ་བར་བྱེད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3401]
དེ་ལྟར་རེ་ཞིག་ཚེ་འདིའི་ཕན་ཡོན་བསྟན་ནས། ད་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཕན་ཡོན་བསྟན་ཏེ། འཇིག་རྟེན་ཕྱི་མ་ལ་ཡང་བདེ་བར་འགྱུར། །ཞེས་བྱ་བ་འདིས་སོ། །

[Block 3402]
ཕ་མ་གཉིས་དང་བྲལ་བ་ནི་ཕ་མ་དང་བྲལ་བའོ། །

[Block 3403]
ཕ་མ་དང་བྲལ་བས་བྱས་པའི་མྱ་ངན་ནི། ཕ་མ་དང་བྲལ་བའི་མྱ་ངན་ནོ། །

[Block 3404]
ཕ་མ་དང་བྲལ་བའི་མྱ་ངན་ཉིད་ཟུག་རྔུའི་རྨ་ཡིན་ཏེ། ཟུག་རྔུ་དེའི་རྨ་གང་ཡིན་པ་དེ་ལ། སྡུག་བསྔལ་གཞན་གྱིས་བསྣན༌[^2184]ཏེ་ཞེས་བྱ་བ་ནི་ཕ་མ་དང་བྲལ་བའི་སྡུག་བསྔལ་གྱི་སྟེང་དུ་བསྣན་པའོ། །

[Block 3405]
ཡང་ན་ཕ་དང་མ་དང་བྲལ་བའི་མྱ་ངན་ཉིད་ཟུག་རྔུ་ཡིན་བས་ཕ་མ་དང་བྲལ་བའི་མྱ་ངན་གྱི་ཟུག་རྔུའོ། །

[Block 3406]
དེས་བྱས་པའི་ཡིད་ཀྱི༌[^2185]རྨ་གང་ཡིན་པ་དེ་ནི་ཕ་མ་དང་བྲལ་བའི་མྱ་ངན་གྱི་ཟུག་རྔུའི་རྨ་སྟེ། དེ་ལ་ཡིད་ཅེས་བྱ་བ་ནི་ཚིག་གི༌[^2186]ལྷག་མའོ། །

[Block 3407]
དེ་བས་བསྟན་པའི༌[^2187]བློ་ཅན་འདི་བཏང་ལེགས། །ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བའི་བློའོ། །

[Block 3408]
འདིར་རྨ་ཞེས་བྱ་བ་ལ་ཡིད་ཅེས་བྱ་བ་ཡང་ཚིག་གི་ལམ་བསྟན་ཏོ།[^2188] །དེ་ལྟར་ཁྱོད༌[^2189]འདོད་ན་ཞེས་བྱ་བ་ནི་རབ་ཏུ་འབྱུང་བར་རོ། །

[Block 3409]
ཀུ་མུ་ཏ་མང་པོ་ཁ་འབུས་པ་ཡོད་པའི་མཚོ་གང་ཡིན་པ་དེ་ནི་ཀུ་མུ་ཏ་མང་པོ་ཁ་འབུས་པའི་མཚོའོ། །

[Block 3410]
བརྟུལ་ཞུགས་དང་སྡོམ་པ་ལ་འབད་ཅེས་བྱ་བས་ནི་ལུས་དང་ངག་གི་ལམ་བསྟན་ཏོ། །

[Block 3411]
ཡིད་བསམ་གཏན་ལ་སྦྱོར་ཞེས་བྱ་བས་ནི་ཡིད་ཀྱི་ལམ་བསྟན་ཏོ། །

[Block 3412]
བསམ་གཏན་གྱི་མན་ངག་ནི་བསམ་གཏན་མན་ངག་གོ། །

[Block 3413]
དེའི་ཕྱིར་འཇུག་པ་ནི་བསམ་གཏན་གྱི་མན་ངག་ལ་འཇུག་པའོ། །

[Block 3414]
དེ༌[^2190]ཇི་ལྟར་བསམ་གཏན་གྱི་མན་ངག་ལ་འཇུག་པའི་རྣམ་པས་བསམ་གཏན་བསྟན༌[^2191]པ་ཡིན་ཞེ་ན། འདོད་པའི་ཉེས་དམིགས་ཞེས་བྱ་བ་ལ་སོགས་པ་བརྩམས་པ༌[^2192]ཡིན་ཏེ། དབེན་པ་རྣམ་པར་བསྒོམ༌[^2193]པའི་ཕྱིར༌[^2194]བསམ་གཏན་དང་པོའི་ཉེས་དམིགས་བསྟན་པ་སྟེ། ཇི་ལྟར་མདོ་སྡེ་ཉིད་ལས་རིག་པར་བྱ་སྟེ། གསོག་དང་། བརྫུན་དང་། སླུ་བའི༌[^2195]ཆོས་ཅན་དང་། བྱིས་པ་འདྲིད་པར་བྱེད་པ་ཞེས་བྱ་བ་དང་། ཤིང་གི་འབྲས་བུ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 3415]
ཅིའི་ཕྱིར་འདོད་པའི་ཉེས་དམིགས་སྟོན་ཅེ་ན༌[^2196]སྨྲས་པ། འདོད་ཁམས་ལས༌[^2197]སྐྱོ་ཞིང་ཡིད་འབྱུང་བར་འགྱུར་བ་དང་། རབ་ཏུ་དབེན་པ་དང་། ཆོག་ཤེས་པའི་བསྔགས་པ་མང་དུ་འབྱུང་ཞེས་བྱ་བ་ཡིན་ཏེ། འདོད་པ་ལས་དབེན་པ་དང་། ཆོག་ཤེས་པའི་བསྔགས་པའི་ཡོན་ཏན་མང་པོ་བརྗོད་པའོ། །

[Block 3416]
དེའི་གཏམ་མང་པོ་གང་ཡིན་པ་དེ་ནི་རབ་ཏུ་དབེན་པ་དང་ཆོག་ཤེས་པའི་གཏམ་མང་པོ་འབྱུང་བའོ། །

[Block 3417]
དེ་ལྟར་འདོད་པ་ལས་རབ་ཏུ་དབེན་པའི་ཕན་ཡོན་བསྟན་ནས་ཚུལ་འཆོས་པ་དང་གཅམ་སྒྱུ་ལ༌[^2198]སོགས་པས་ནི་སྡིག་པ་མི་དགེ་བའི་ཆོས་རྣམས་ལས་དབེན་པའི་ཐབས་བསྟན་པ་ཡིན་ཏེ། ཚུལ་འཆོས་པ་ལ་སོགས་པའི་ཉེས་པ་བསྟན་པ་དེ་དག་ལས་རབ་ཏུ་དབེན་པར་གྱུར་པའོ། །

[Block 3418]
དེ་ལྟར་རེ་ཞིག་བསམ་གཏན་དང་པོའི་མན་ངག་ལ་འཇུག་པའི་གཏམ་བསྟན་ཏོ། །

[Block 3419]
ཉེ་བར་ཞི་བ་དང་རབ་ཏུ་ཞི་བ་ནི་ཉེ་བར་ཞི་བ་དང་རབ་ཏུ་ཞི་བའོ། །

[Block 3420]
དེ་གཉིས་ལམ་དུ་གྱུར་པ་ནི་ཉེ་བར་ཞི་བ་དང་རབ་ཏུ་དང་བའི་ལམ་དུ་གྱུར་པའོ། །

[Block 3421]
དེ་ལ་ཉེ་བར་ཞི་བ་ནི་ཉོན་མོངས་པ་ཉེ་བར་ཞི་བའོ། །

[Block 3422]
རབ་ཏུ་དང་བ༌[^2199]ནི་སེམས་ཀྱི་དད་པའོ། །

[Block 3423]
ཉོན་མོངས་པ་དང་ཉེ་བར་ཞི་བ་མངོན་སུམ་དུ་བསྟན་པ་དེས་ནི་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པའི་མན་ངག་ལ་འཇུག་པའི་གཏམ་བསྟན་པ་ཡིན་ནོ། །

[Block 3424]
ཆོས་ཀྱི་གཏམ་དེ་དང་དེ་ཞེས་བྱ་བ་ནི་འདིར་མ་བསྟན་པའི་ལྷག་མའི་ཆོས་ཀྱི་གཏམ་མ་ལུས་པར་བསྟན་ཏོ། །

[Block 3425]
དེ་བཞིན་དུ་གཡོག་བྱེད་ཅེས་བྱ་བ་ནི་ཇི་ལྟར་ཁྱིམ་ན་གནས་པའི་དུས་ལྟ་བུར་རོ། །

[Block 3426]
པདྨའི་ལོ་མ་ཆེན་པོ་ལ། །ཞེས་བྱ་བ་སྨོས་པ་ནི་བསམ་གཏན་གྱི་སྦྱོར་བ་དང་མཐུན་པའི་ཟས་ཙམ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3427]
སླར་སོང་ངོ་ཞེས་བྱ་བྱ་བའི༌[^2200]ཚིག་གིས་ནི་སྔར་བསྟན་པའི་ཞག་ལྔ་ཞིང་བྱང་ཆུབ་སེམས་དབའི་དྲུང་དུ་ཆོས་མཉན་པའི་ཕྱིར་འདུའོ་ཞེས་བྱ་བ་འདིའི་གནས་སྐབས་ཡོངས་སུ་མི་ཉམས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 3428]
དེ་ཉིད་ཀྱི་ཕྱིར་ཡང་རིང་པར་ཡང་ཡོངས་སུ་ཤེས་ནས་ཞེས་བྱ་བ་སྟེ། ཉི་མ་ལྔས་བར་དུ་ཆོད་པའི༌[^2201]ཕྱིར་རོ། །

[Block 3429]
ཚུལ་ཁྲིམས་དང་སྤྱོད་ཚུལ་དེ་ལྟར་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་དཀའ་ཐུབ་དང་། བཟླས་བརྗོད་དང་། སྦྱིན་སྲེག་གི་ཆོ་ག་དེ་ཉིད་བསྟན་པ་ཡིན་ཏེ། འདིར་ཡང་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་ནི་དོན་གཞན་མ་ཡིན་ཏེ། བཟླས་བརྗོད་དང་། སྦྱིན་སྲེག་ལ་སོགས་པ་བྱས་ནས་དུས་བསྟན་ཏེ། སླར་དོང་བ་ལ༌[^2202]སོགས་པའོ། །

[Block 3430]
རབ་ཏུ་དབེན་པ་ལ་དགའ་བ་ཞེས་བྱ་བ་ནི་ཞག་ལྔ་ཞིང་ལྔ་ཞིང་བྱང་ཆུབ་སེམས་དཔའི་གན་དུ་འོང་བའི་ཕྱིར་རོ། །

[Block 3431]
བསམ་གཏན་ལ་གཞོལ་བས་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་ཡིད་བསམ་གཏན་ལ་སྦྱོར་བས་གནས་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་པའོ། །

[Block 3432]
བྱ་བ་ངན་པ་དང་མ་འབྲེལ་ཞིང་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་བརྟུལ་ཞུགས་དང་། བཟླས་བརྗོད་དང་སྦྱིན་སྲེག་གི༌[^2203]ཆོ་ག་བྱེད་ཀྱི་ལས་གཞན་མི་བྱེད་པས་སོ། །

[Block 3433]
གདུང་བ་མེད་ལ་ཞེས་བྱ་བ་ནི་བསྟན་པའི་ལམ་ལ་དགའ་བར་སྟོན་ཏོ། །

[Block 3434]
རབ་ཏུ་ཞི་བ་ལ་མངོན་པར་དགའ་ཞིང་འཁོད་པར༌[^2204]ཞེས་བྱ་བ་ནི་སྤྱོད་ཡུལ་ལ་སོགས་པའི་གནས་པའོ། །

[Block 3435]
རྩོལ་བ་མེད་པར་ཞེས་བྱ་བ་འདིས་ནི་བྱ་བ་ངན་པ༌[^2205]མ་འབྲེལ་ཞིང་གདུང་བ་མེད་པ་རབ་ཏུ་ཞི་བ་ཉིད་དུ་བསྟན་ཏོ། །
--- END BLOCKS ---
