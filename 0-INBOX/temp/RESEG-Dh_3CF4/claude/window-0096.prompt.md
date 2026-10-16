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
[Block 3361]
ནམ་ཞིག་བདེ་ཞེས་བྱ་བ་ནི་བསྒྲུབ༌[^2151]ཅིང་བསྲུང་ལ་སོགས༌[^2152]པའི་ཚེ་ན་སྡུག་བསྔལ་བའི་ཕྱིར་ནམ་ཞིག་བདེ་བ་ཡིན་ཏེ། དེས་ན་ཡང་རྣམ་པ་གསུམ་གྱིས་བདེ་བ་མེད་དོ། །

[Block 3362]
ཇི་ལྟར་དེ་ལ་འཇིག་རྟེན་པ་རྣམས་བདེ་བའི་བློ་འབྱུང་ཞེ་ན། སྨྲས་པ། ཡོངས་སུ་རྟོགས་པའི༌[^2153]དབང་གིས་བདེ་བ་འབྱུང་བ་ཡིན་གྱི། ངོ་བོ་ཉིད་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 3363]
དེ་ལྟར་རེ་ཞིག་བདེ་བ་ཡིད་ཀྱིས༌[^2154]ཡོངས་སུ་རྟོགས་པའི༌[^2155]མཐུ་ཡིན་པར་བསྟན་ནས། ཡུལ་རྣམས་ལ་རྨོངས་པས་ཉེ་བར་སྤྱོད་པ་ཞེས་བྱ་བ་ཡིན་ཏེ། དབང་པོ་ལྔའི་ཡུལ་གྱི་ཉེ་བར་སྤྱོད་པའི་བདེ་བ་ནི་དེ་ལ་རྣམ་པར་རྟོག་པ་མེད་པས༌[^2156]ཇི་ལྟར་བདེ་བར་འགྱུར་ཏེ་དེ་ལ་བདེ་བའི་རྣམ་པར་རྟོག་པ་མེད་པས་སོ། །

[Block 3364]
རྣམ་པར་རྟོག་པ་ཙམ་ཡང་མངོན་པར༌[^2157]ཤེས་པ་ལྔ་དང་ལྡན་པས་ན་དེ་ཉིད་སྨྲས་པ། རྨ་གཡའ་ཕྲུགས་པའི་བདེ་བ་བཞིན་དུ་ཟད། ཅེས་བྱ་བ་ཡིན་ཏེ། རྨ་གཡའ་བ་ལ་ཕྲུགས་པའི་བདེ་བ་འབྱུང་བ་དེ་བཞིན་དུ་ཡུལ་རྣམས་ལ་ཡང་བརྟེན་པས་ཀྱང༌[^2158]བདེ་བ་བཞིན་ནོ། །

[Block 3365]
ཆོས་ཀྱི་ལམ་ནི་རབ་ཏུ་ཞི་བ་ཡིན། །ཞེས་བྱ་བ་གང་སྔར་བཤད་པའི་རབ་ཏུ་ཞི་བ་ཡང་གཉིས་པ་བཤད་པ་ལས།

[Block 3366]
[^2159] འདིར་ཁྱིམ་ན་གནས་ན་ཉོན་མོངས་པ་རབ་ཏུ་ཞི་བར་མི་འགྱུར་ཞིང་མི་བཟློག༌[^2160]པར་བརྟན་པའི༌[^2161]ཕྱིར། གཞན་ཡང་ཕལ་ཆེར་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་བརྩམས་པ་ཡིན་ནོ། །

[Block 3367]
འདིའི་བསྡུས་པའི་དོན་ནི་ཕུན་སུམ་ཚོགས་པའི་གནས་སྐབས་དང་། རྒུད་པའི་གནས་སྐབས་གཉི་ག་ན་ཡང་ཉོན་མོངས་པ་ཉེ་བར་ཞི་བ་མེད་པར་བསྟན་ཏོ། །

[Block 3368]
ཚིགས་བཅད་ཕྱེད་དང་པོས་ནི་ཕུན་སུམ་ཚོགས་པའི་གནས་སྐབས་སུ་ཉོན་མོངས་པ་ཉེ་བར་མ་ཞི་བར་བསྟན་ཏོ། །

[Block 3369]
གཉིས་པའི་ཕྱེད་ཀྱི་ཚིག་རྐང་དང་པོས་ནི་རྒུད་པའི་གནས་སྐབས་བསྟན་ཏོ། །

[Block 3370]
དེ་ན་ཞེས་བྱ་བ་ནི་ཁྱིམ་དེ་ན་སྟེ་ཕུན་སུམ་ཚོགས་པ་དང་། རྒུད༌[^2162]པའི་གནས་སྐབས་གཉི་ག་ན་ཡང་ཉེ་བར་ཞི་བ་མེད་དེ། དེ་གཉིས་མ་གཏོགས་པའི་གནས་སྐབས་གསུམ་པ་ནི་མེད་པའི་ཕྱིར། ནམ་ཞིག་རབ་ཏུ་ཞི་བར་འགྱུར། །ཞེས་བསྟན་ཏོ། །

[Block 3371]
དྲེགས་དང་ང་རྒྱལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་སྔར་བཤད་པ་ཐམས་ཅད་ཀྱི་དོན་མཇུག༌[^2163]བསྡུ་བ་ཡིན་ཏེ། དྲེགས་དང་ང་རྒྱལ་གཏི་མུག་སྦྲུལ་གྱི་ཚང་། །ཞེས་བྱ་བ་ནི་ཕལ་ཆེར་ཁྱིམ་ན༌[^2164]འབྱོར་ན་ཞེས་བྱ་བའི་ཚིགས་བཅད་བསྟན་པ་དེའི་ནམ་ཞིག་རབ་ཏུ་ཞི་བར་འགྱུར་ཞེས་པའི༌[^2165]མཇུག་བསྡུ་བ་ཡིན་ནོ། །

[Block 3372]
དྲེགས་དང་ང་རྒྱལ་གཏི་མུག་སྦྲུལ་གྱི་ཚང་བཞིན་དུ་གནས་དང་གཞིར་གྱུར་པ་སྟེ། དེ་བས༌[^2166]ན། རབ་ཏུ་ཞི་ལ་དགའ་བའི་བདེ་འཇིག་པ།[^2167] །ཞེས་བྱ་བ་ཡིན་ཏེ། དགའ་བའི་བདེ་བ་འཇིག་པ་སྟེ། ཚང་དང་གནས་བཞིན་དུ་སྡུག་བསྔལ་དྲག་པོའི་གཞིར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3373]
འདིས་ནི་གང་སྔར་བསྟན་པའི་བསྒྲུབ་ཅིང་བསྲུང་ལ་སོགས་པའི་སྡུག་བསྔལ་ཞེས་བྱ་བ་དེའི་མཇུག་བསྡུ་བ་ཡིན་ནོ། །

[Block 3374]
རབ་ཏུ་ཞི་ལ་དགའ་བའི་བདེ་འཇིག་པ། །ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རབ་ཏུ་ཞི་བ་བདེ་བ་ཡིན་ཞེ་ན། བདེ་བ་བསྟན་པའི་ཕྱིར་སྐྱེ་བོ་ཆོག་ཤེས་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། བདེ་བ་ཡང་རྣམ་པ་གཉིས་ཏེ། ལུས་དང་སེམས་ཀྱི་དབང་དུ་བྱས་པའོ།[^2168] །སེམས་ཀྱི་བདེ་བའི་དབང་དུ་བྱས་ནས། སྐྱེ་བོ་ཆོག་ཤེས་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 3375]
ཡོ་བྱད་རྣམས་ཀྱིས༌[^2169]ཆོག་ཤེས་པའི་འཚོ་བ་ནི་ཆོས་གོས་ལ་སོགས་པ་ངན༌[^2170]ངོན་ཙམ་གྱིས་ཆོག་ཤེས་པའི་ཕྱིར་རོ། །

[Block 3376]
ཆོག་ཤེས་པའི་སྐྱེ་བོ་ནི་དཀའ་ཐུབ༌[^2171]ཅན་གྱི་སྐྱེ་བོའོ།[^2172] །ཆོག་ཤེས་པའི་སྐྱེ་བོ་རྣམས་ནི་ཁྱིམ་བཞིན་དུ་ནགས་ན་དེ་བཞིན་ནོ། །

[Block 3377]
རབ་ཏུ་དབེན་པའི་བདེ་བ་ནི་ལུས་དང་། སེམས་ཀྱི་རབ་ཏུ་དབེན་པའི་བདེ་བ་ཡིན་ཏེ། སེམས་དབེན་པའི་བདེ་བས་སེམས་དགའ་བར་གྱུར་པ་ཡིན་ཏེ། འདིས་ནི༌[^2173]ཡིད་དགའ་བར༌[^2174]བསྟན་ཏོ། །

[Block 3378]
དེ་ཉིད་ཀྱི་ཕྱིར་ཡིད་བདེ་བའི་དབང་དུ་བྱས་ཏེ། དེ་འདྲ་ལྷ་ཡི་ཡུལ་ནའང་མེད། །ཅེས་བྱ་བ་ནི་མིའི་འཇིག་རྟེན་ན་ལྷ་ག་ལ་ཡོད་ཅེས་བྱ་བ་ཡིན་ནོ། །

[Block 3379]
ལུས་ཀྱི་བདེ་བའི་དབང་དུ་བྱས་ནས། དེ་བས་ཚལ་ན་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 3380]
[^2175]ཚིགས་བཅད་འདིའི་དང་པོའི་ཕྱེད་ཀྱིས་ནི་ཟས་དང་། གནས་མལ་དང་། ཆོས་གོས་དམན་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 3381]
འཚོ་བ་སྒྲུབ་པ་ཉིད་ཀྱང་འདི་ལྟར་མི་སྒྲུབ་སྟེ། ཆོས་མིན་འདྲེས་པ་ཞེས་བྱ་བ་སྟེ་སྔར་བསྟན་པའི་བྱ་བས༌[^2176]སོ། །

[Block 3382]
བདེ་བ་ནི་ཁྱིམ་གྱི་བདེ་བའོ། །

[Block 3383]
མི་འདོད་པ་ནི་དུག་དང་འདྲེས་པའི་བཟའ་བ་འདྲ་བ་སྟེ། ཟས་དང་བཏུང་བ་དང་ཁྱིམ་གྱི་འཚོ་བས་བསྒྲུབས་ཤིང་བསྐྱེད་པའི་ཁྱིམ་གྱི་བདེ་བ་དུག་ཆེན་བོ་དང་འདྲེས་པའི་ཟས་དང་འདྲ་བ་དེ་ནི༌[^2177]ཆོས་མ་ཡིན་པ་དང་འདྲེས་པའི་ཕྱིར་རོ། །

[Block 3384]
བདག་ལ་ཕན་པར་འདོད་པ་ནི་བློ་དང་ལྡན་པའོ། །

[Block 3385]
བཀུར་སྟིའི་བྱ་བ་ཁྱད་པར་ཅན་གྱིས་ཞེས་བྱ་བ་ནི་མངོན་དུ་སྨྲ་བ་དང་། ཕྱག་ལ་སོགས་པའོ། །

[Block 3386]
འདོད་པ་ལས་སླར་ལྡོག་གོ་ཞེས་བྱ་བ་ནི་ཕྱིས་ཡང་འདོད་པ་ལ་འཇུག་པར་མི་བྱེད་པའོ། །

[Block 3387]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་རྒྱལ་རིགས་ཕྱུག་པོའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 3388 [HEADING]]
## པདྨའི་རྩ་བའི་སྐྱེས་པའི་རབས། ^20-0

[Block 3389]
འཕྱས་ཀྱི་གནས་ཞེས་བྱ་བ་ནི་རྗེས་སུ་བྱེད་པ་ལྟ་བུའོ། །

[Block 3390]
གནོད་པ་ལྟ་བུར་ཞེས་བྱ་བ་ནི་ཉེ་བར་མཚོན་པ༌[^2178]ལྟ་བུའོ། །

[Block 3391]
དེའི་གཟུགས་དང་ཡོན་ཏན་དང་མཐུན་པ་ཞེས་བྱ་བ་ནི་དེ་དང་མཉམ་པ་སྟེ། རྟག་ཏུ་རྗེས་སུ་འབྲང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3392]
རིག་བྱེད་ཀྱི་ཡན་ལག་ཅེས་བྱ་བ་ནི་སོ་མ་ནི་བཤད་ཅེས་བྱ་བའི་རིག་བྱེད་དོ། །

[Block 3393]
བདག་ནི་རབ་ཏུ་འབྱུང་བར་འདོད། །ཅེས་བྱ་བ་འགྲོ་བར་འགྱུར་རོ། །

[Block 3394]
ལམ་གང་གིས་ཤེ་ན། དེ་ཉིད་སྨྲས་པ། དེ་བས་ན༌[^2179]ཕན་པའི་ལམ་བཟང་པོས་ཞེས་བྱ་བ་ཡིན་ཏེ། དགེ་བ་དང་ལེགས་པའི་ལམ་ཡིན་པས༌[^2180]ལམ་བཟང་པོ་སྟེ། ལམ་འདིས་ཐམས་ཅད་དུ་འབྱུང་ངོ་ཞེས་བྱ་བའོ། །

[Block 3395]
རིག་བྱེད་སློབ་བ་ལ་ནི་འགྲུས། །ཞེས་བྱ་བ་ནི་རིག་བྱེད་སློབ་པ་ནི་བྲམ་ཟེའི་ལུས༌[^2181]སུ་བཤད་དོ། །

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
--- END BLOCKS ---
