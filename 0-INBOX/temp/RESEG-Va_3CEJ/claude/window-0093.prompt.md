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
[Block 3256 [VERSE]]
འདིར་ནི་ཉོན་མོངས་ས་བོན་བཞིན། །
ཀླུ་བཞིན་རྩྭ་བཞིན་ལྗོན་ཤིང་བཞིན། །
དེ་བཞིན་ཤུན་པ་བཞིན་དུ་འདོད། །

[Block 3257]
འདིའི་ས་བོན་ལ་སོགས་པ་དང་ཆོས་མཐུན་པ་གང་ཞིག་ཡིན་ཞེ་ན། དཔེར་ན་ས་བོན་ལས་སྡོང་བུ་དང་། ལོ་མ་ལ་སོགས་པ་སྐྱེ་བར་འགྱུར་བ་དེ་བཞིན་དུ། ཉོན་མོངས་པ་ལས་ཀྱང་ཉོན་མོངས་པ་དང་ལས་དང་གཞི་རྣམས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3258]
དཔེར་ན་ཀླུ་གནས་པའི་མཚོ་ནི་སྐམ་པར་མི་འགྱུར་བ་ལྟར། ཉོན་མོངས་པའི་ཀླན་ཀ༌[^1861]གནས་པའི་སྐྱེ་བའི་མཚོ་ཡང་དེ་དང་འདྲའོ། །

[Block 3259]
དཔེར་ན་ནགས་ཚལ་རྩ་བ་ནས་མ་ཕྱུང་བ་རྣམས་ནི་བཅད༌[^1862]ཀྱང་སླར་སྐྱེ་བར་འགྱུར་བ་ལྟར། ཉོན་མོངས་པ་རྩ་བ་ནས་མ་བཏོན་པའི་འགྲོ་བ་རྣམས་ཀྱང་དེ་དང་འདྲའོ། །

[Block 3260]
དཔེར་ན་ཤིང་ལྗོན་པ་རྣམས་དུས་དུས་སུ་མེ་ཏོག་དང་འབྲས་བུ་རྣམས་སྐྱེད་པར་བྱེད་པ་དེ་བཞིན་དུ། ཉོན་མོངས་པ་རྣམས་ཀྱང་ལན་ཅིག་མ་ཡིན་པར་ཉོན་མོངས་པ་དང་ལས་དང་གཞི་རྣམས་ཀྱི་རྒྱུ་ཡིན་ནོ། །

[Block 3261]
དཔེར་ན་ཤུན་པ་དང་བཅས་པའི་འབྲས༌[^1863]ཐུག་པོ་ཆེ་རྣམས༌[^1864]ནི་སྐྱེ་བར་ནུས་ཀྱི་འབའ་ཞིག་དག་ནི་མ་ཡིན་པ་དེ་བཞིན་དུ། ཉོན་མོངས་པའི་ཐོབ་པའི་ཤུན་པ་དང་བཅས་པའི་ལས་སྐྱེ་བ་གཞན་དུ་སྐྱེ་བར་ནུས་ཀྱི་འབའ་ཞིག་ནི་མ་ཡིན་ནོ། །

[Block 3262]
དེ་ལྟར་ན༌[^1865]རེ་ཞིག་ཉོན་མོངས་པ་ས་བོན་ལ་སོགས་པ་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 3263 [HEADING]]
###### ཤུན་པ་དང་བཅས་པའི་འབྲས་བུ་ལྟ་བུའི་ལས། ^3-1-11-15-2-0

[Block 3264 [VERSE]]
ལས་ནི་ཤུན་བཅས་འབྲས་དང་འདྲ། །
དེ་བཞིན་སྨན་དང༌[^1866]མེ་ཏོག་བཞིན། །

[Block 3265]
འདི་ལ་ཤུན་པ་ཡོད་པས་ན་ཤུན་པ་དང་བཅས་པ་སྟེ། ཤུན་པ་ལྟ་བུའི་ཉོན་མོངས་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 3266]
ད་ནི་ཤུན་པ་དང་བཅས་པའི་འབྲས་བུ༌[^1867]ལྟ་བུའི་ལས་བརྗོད་པར་བྱའོ། །

[Block 3267]
དཔེར་ན་འབྲུ་དང་སྨན་དག་འབྲས་བུ་སྨིན་པ་མཐར་ཕྱིན་པ་དང་ལྡན་པ་དེ་བཞིན་དུ་ལས་རྣམས་ཀྱང་རྣམ་པར་སྨིན༌[^1868]ནས་ཡང་རྣམ་པར་སྨིན་པ་མངོན་པར་མི་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 3268]
དཔེར་ན་མེ་ཏོག་འབྲས་བུ་བསྐྱེད་པར་བྱ་བ་ལ་ཉེ་བའི་རྒྱུ་ཡིན་པ་ལྟར་ལས་རྣམས་ཀྱང་རྣམ་པར་སྨིན་པ་བསྐྱེད་པར་བྱ་བ་ལ་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 3269 [HEADING]]
###### གཞི་བཟའ་བཏུང་གྲུབ་པ་བཞིན། ^3-1-11-15-3-0

[Block 3270]
གཞི་ནི་བཟའ་བཏུང་གྲུབ་པ་བཞིན། །དཔེར་ན་བཟའ་བ་དང་བཏུང་བ་གྲུབ་ཟིན་པ་ཡོངས་སུ་ལོངས་སྤྱད་པར་བྱ་བ་འབའ་ཞིག་ཡིན་གྱི་ཡང་བསྐྱེད་པར་བྱ་བ་མ་ཡིན་པ་ལྟར་རྣམ་པར་སྨིན་པ་ཞེས་བྱ་བའི་གཞི་ཡང་དེ་དང་འདྲ་སྟེ། རྣམ་པར་སྨིན་པ་ལས་ཚེ་རབས་གཞན་དག་ཏུ་རྣམ་པར་སྨིན་པ་གཞན་དང་འབྲེལ་པ་ནི་མེད་དེ། [^1869]གལ་ཏེ་འབྲེལ་པར་འགྱུར༌[^1870]ན་ནི་ཐར་པར་ཡང་མི་འགྱུར་རོ། །

[Block 3271 [HEADING]]
##### སྲིད་པ་བཞི། ^3-1-11-16-0

[Block 3272]
ཡང་ཚེའི་རྒྱུན་དེ་དེ་ལྟར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ན་འདི་ལྟ་སྟེ་སྲིད་པ་བར་མ་དང་། སྐྱེ་བའི་སྲིད་པ་དང་། དུས་སྔ་མའི་སྲིད་པ་དང་། འཆི་བའི༌[^1871]སྲིད་པ་དང་། སྲིད་པ་བཞི་ལས་མི་འདའ་སྟེ། དེ་དག་ནི་བཤད་ཟིན་ཏོ། །

[Block 3273]
སྲིད་པ་བཞི་པོ་དེ་དག་ལས་གཅིག་ཏུ།

[Block 3274 [VERSE]]
སྐྱེ་བའི་སྲིད་པ་ཉོན་མོངས་ཅན། །
ཉོན་མོངས་པ་གང་གིས་ཤེ་ན།
རང་གི་ས་པའི་ཉོན་མོངས་ཀུན། །

[Block 3275]
ཆོས་མངོན་པ་པ་རྣམས་ན་རེ་སྐྱེ་བའི་སྲིད་པ་ས་གང་ཡིན་པ་དེའི་ས་པའི་ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱི་ས༌[^1872]ཡིན་པ་ཉིད་དེ། གང་གིས་ཉིང་མཚམས་སྦྱོར་བར་དགག་པར་བྱ་བའི་ཉོན་མོངས་པ་དེ་ནི་མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 3276]
ཉོན་མོངས་པ་ཅན་རྣམས་ཁོ་ནས་ཡིན་གྱི་ཀུན་ནས་དཀྲིས་པ་ཆིག་རྐྱ་ཐུབ་པ་རྣམས་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 3277]
གནས་སྐབས་དེ་ཞན་པ་ཡིན་མོད་ཀྱི། གང་ཞིག་གིས་གང་ལ་ཡང་དང་ཡང་དུ་དང་། ཉེ་བར་དཔྱད་པ་དེ་ལ་ནི་དེའི་ཚེ་ཉོན་མོངས་པ་དེ་ཉིད་ཉེ་བར་གནས་པར་འགྱུར་ཏེ། སྔོན་འཕངས་པའི་ཕྱིར་རོ། །

[Block 3278]
སྲིད་པ་བར་མ༌[^1873]ཉིང་མཚམས་སྦྱོར་བ་ཡང་དེ་བཞིན་དུ་གདོན་མི་ཟ་བར་ཉོན་མོངས་པ་ཅན་དུ་རིག་པར་བྱའོ། །

[Block 3279]
གཞན་རྣམ༌[^1874]གསུམ་མོ། །

[Block 3280]
སྲིད་པ་བར་མ་ལ་སོགས་པ་སྲིད་པ་གཞན་གསུམ་ནི་དགེ་བ་དང་། ཉོན་མོངས་པ་ཅན་དང་། ལུང་དུ་མ་བསྟན་པ་དང་གསུམ་ཆར་ཡིན་ནོ། །

[Block 3281]
ཡང་སྲིད་པ་འདི་རྣམས་ལས་གང་ཞིག་གང་དང་ལྡན་ཞེ་ན། གཟུགས་མེད་གསུམ། སྲིད་པ་བར་མ་མ་གཏོགས་ཏེ། གཟུགས་མེད་པའི་ཁམས་ནི་གང་དུ་ཕྱིན་པར་བྱ་བའི་ཕྱིར་སྲིད་པ་བར་མ་མངོན་པར་འགྲུབ་པར་འགྱུར་བ་ནས༌[^1875]གཞན་དུ་ན༌[^1876]ཡོངས་སུ་ཆད་པ་ནི་མེད་དོ། །

[Block 3282]
འདོད་པ་དང་གཟུགས་ཀྱི་ཁམས་དག་གིས་ནི་ཆད་པ་མ་སྨོས་པས་སྲིད་པ་བཞི་པོ་ཐམས་ཅད་ཡོད་དོ་ཞེས་བྱ་བར་གནས་པར༌[^1877]བྱས་པ་ཡིན་ནོ། །

[Block 3283]
སེམས་ཅན་རྣམས་ཀྱི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཇི་ལྟ་བ་བཞིན་རྒྱས་པར་བཤད་ཟིན་ཏོ། །

[Block 3284 [HEADING]]
#### འགྲོ་བ་ཟས་ཀྱིས་གནས་པ། ^3-1-12-0

[Block 3285]
ཡང་སེམས་ཅན་རྣམས་ཇི་ལྟར་གནས་པ་ཡིན་ཞེ་ན། འགྲོ་བ་ཟས་ཀྱིས་གནས་པ་ཡིན། །བཅོམ་ལྡན་འདས་ཉིད༌[^1878]ཀྱིས་མངོན་པར་མཁྱེན་ཅིང་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས་ཆོས་གཅིག་བཀའ་སྩལ་པ་འདི་ལྟ་སྟེ། སེམས་ཅན་ཐམས་ཅད་ནི་ཟས་ཀྱིས་གནས་པའོ་ཞེས་བྱ་བ་ནི་མདོའི་ཚིག༌[^1879]ཡིན་ནོ། །

[Block 3286 [HEADING]]
##### ཁམ་གྱི་ཟས། ^3-1-12-1-0

[Block 3287]
ཟས་རྣམས་ཀྱང་གང་དག་ཅེ་ན། ཟས་ནི་བཞི་སྟེ། ཁམ་གྱི་ཟས་ནི་རགས་པ་དང་ཕྲ་བའོ། །

[Block 3288]
ཕྲ་བ་ནི་སྲིད་པ་བར་མ༌[^1880]རྣམས་ཀྱི་ཡིན་ཏེ། དྲི་ཟ་བའི་ཕྱིར་རོ། །

[Block 3289]
ལྷ་རྣམས་དང་། བསྐལ་པ་དང་པོ་པ་རྣམས་ཀྱི་ཡང་ཡིན་ཏེ། བྱེ་མ་དག་གི་ནང་དུ་ཏིལ་མར་བླུགས་པ་བཞིན་དུ་ཡན་ལག་རྣམས་ཀྱི་ནང་དུ་འཇུག་པས་རྒྱུ་མཐུན་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 3290]
ཡང་ན་ཕྲ་མོ་རྣམས་ཀྱི་ཡིན་པས་ཕྲ་མོ་སྟེ། བྱིས་པ་དང་། དྲོད་གཤེར་ལས་སྐྱེ་བ་ལ་སོགས་པའིའོ། །

[Block 3291]
རེག་པ༌[^1881]ནི་གཉིས་པའོ། །

[Block 3292]
ཡིད་ལ་སེམས་པ༌[^1882]ནི་གསུམ་པའོ། །

[Block 3293 [VERSE]]
རྣམ་པར་ཤེས་པའི་ཟས་ནི་བཞི་པའོ། །
དེ་ལ་ཁམ་གྱི་ཟས་ནི་འདོད་པ་ན། །

[Block 3294]
གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དག་ན་ནི་མེད་དོ། །

[Block 3295]
[^1883]དེའི་འདོད་ཆགས་དང་བྲལ་བ་དག༌[^1884]དེར་སྐྱེ་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
