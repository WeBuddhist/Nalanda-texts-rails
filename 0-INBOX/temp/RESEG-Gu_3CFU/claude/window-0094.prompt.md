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
[Block 3291]
འདི་རྣམས་བསྟེན་པ་ལ་མོའི་དབང་པོའམ་ཕོའི་དབང་པོ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་བས་ན་ཟ་མ་ལ་སོགས་པ་མི་བསྟེན་པ་རྣམས་སོ། །

[Block 3292]
འདིར་གཞུང་ནི་བུད་མེད་ཉོས་པ་ལ་སྨྱན་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3293]
མཐུན་པའི་སྨྱན་བྱེད་ན་དགེ་སློང་གིས་སྤྲིང་བ་མནོས་ཏེ་ལན་གྲངས་མང་པོ་འཕྲིན༌[^2267]ཕར་སྐྱེལ་བ་དང་ཚུར་སྐྱེལ་བར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3294]
བདག་གི་སྨྱན་བྱེད་པ་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱི་ཕྱིར་བདག་ཉིད་སྨྱན་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3295]
ཕྲིན་ཕར་སྐྱེལ་བའི་ཚིག་ལ་བདག་ཉིད་ལ་སྨྱན་བྱེད་པ་ལ་སྦོམ་པོའི་ཚིག་འདིའོ། །

[Block 3296]
ནོད་པ་དང་ཚུར་སྐྱེལ་བ་དག་འདིར་མེད་པའི་ཕྱིར་དང་ཕྲད་པ་ལ་ཡང་ཕམ་པར་འགྱུར་གྱི། ལྷག་མ་མེད་པའི་ཕྱིར་མི་བསྟེན་པའི་མཐའ་ཅན་རྣམས་ལ་ནོད་པ་ལ་སོགས་པའི་ཚིག༌[^2268]གསུམ་པོ་འདི་ཡོད་པ་ལ་སྦོམ་པོ་སྟེ། འདི་ལྟར་ཕྲད་པ་འཇུག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 3297]
ངེས་པ་དང་མི་བསྟེན་པ་དག་སྦོམ་པོའོ། །

[Block 3298]
མངལ་མེད་པ་དག་ལ་ཁུངས་གཞན་གྱི་དབང་ཉིད་ཀྱི་ཕྱིར་རྙེད་པ་འཇུག་པ་ཡང་ནམ་མཁའི་ཞགས་པ་བཞིན་དུ་མི་འཇུག་པ་ཉིད་དུ་ཡིད་ལ་ངེས་པར་འབྲེལ་པ་ཡིན་ནོ། །

[Block 3299]
ངེས་པར་སྐྱེས་པ་ཉིད་ལ་སླར་འདིར་ཁུངས་དྲང་བར་བྱ་སྟེ། འདི་ལ་ཁྱོད་ཀྱིས་ནུ་མོ་འདི་སྦྱིན་པར་བྱ་སྟེ་གཞན་ལ་ནི་སྦྱིན་པར་མི་བྱའོ་ཞེས་ཟེར་རོ། །

[Block 3300]
ཉོས་པ་དང་མཐུན་པ་དག་ལ་ཕྲད་པ་ལ་ཡང་དེའི་དབང་ཉིད་ཀྱིས་ཐོབ་པའི་རྣམ་པ་ཉིད་ཀྱི་ཕྱིར་སྦོམ་པོ་ཉིད་དེ་དགེ་འདུན་ལྷག་མ་ནི་མ་ཡིན་ནོ། །

[Block 3301]
སྐད་སྦྱར་བ་ཉིད་སྟོན་ནའོ་ཞེས་བྱ་བ་ནི་འདིར༌[^2269]ཤུགས་ཀྱིས་ཕྲད་པའི་དོན་དུ་ཞེས་བྱ་བ་འོག་ཏུ་ཡང་རྟོགས་པར་བྱའོ། །

[Block 3302]
སྟོན་པ་ཡོད་པར་གྱུར་པ་ལ་སྐད་སྦྱར་བ་གང་ཡིན་པ་ཕྲད་པའི་དོན་དུ་དེར་སྦོམ་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3303]
འདིར་གཞུང་ནི་སྐྱེས་པས་བུད་མེད་དང་ལྷན་ཅིག་བརྡ་བགྱིས་ནས་དེས༌[^2270]དགེ་སློང་ལ་འདི་སྐད་ཅེས་འཕགས་པ་བུད་མེད་ཅིག་མཐོང་ངམ་ཞེས་མཆི་བ་ལ། དེས་འདི་སྐད་ཅེས་རྩིག་པ་འདིའི་དྲུང་ན་འདུག་གོ་ཞེས་བགྱིས་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་པ་སྦོམ་པོར་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3304]
འཐབ་ཀྲོལ་གྱིས་འཕྲོག་ཏུ་བཅུག་ནའོ་ཞེས་བྱ་བ་ལ་འདི་ནི་སྨྱན་བྱེད་པ་ལ་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་འདིར་དངོས་གཞི་མི་སྐྱེད༌[^2271]པའོ། །

[Block 3305]
འདིར་གཞུང་ནི་འཐབ་ཀྲོལ་ཅན་གྱིས་འཕྲོག་ཏུ་བཅུག་ན་ཉེས་པ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་རོ༌[^2272]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3306]
ཆུང་མ་འམ་བུད་མེད་ཆེ་གེ་མོ་ཉོས་ཤིག་ཅེས་ཟེར་ནའོ་ཞེས་བྱ་བ་ནི་གཞུང་ཁ་ཅིག་ལས་འདི་ཉོས་ཤིག་ཅེས་མཆི་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3307]
གཞུང་ཁ་ཅིག་ལས་བུད་མེད་ཆེ་གེ་མོ་ཉོས་ཤིག་ཅེས་མཆི་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་འདི་གཉིས་ཀ་ཡང་རིགས་པར༌[^2273]འགྱུར་བ༌[^2274]ཉིད་ཀྱི་ཕྱིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 3308]
བུད་མེད་ཅེས་ཟེར་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ཉོས་ཤིག་ཅེས་བྱ་བར་སྦྱར་རོ། །

[Block 3309]
འདིར་བཙུན་པ་དགེ་སློང་གིས་འདི་སྐད་ཅེས་བུད་མེད་ཉོས་ཤིག་ཅེས་བགྱི་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་བྱས་སུའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3310]
ཚིག་འདི་ནི་ཤིན་ཏུ་མ་ངེས་པའི་ཁྱད་པར་དང་ལྡན་པ་སྟེ། ཁྱད་པར་མངོན་པར་ངེས་པར་བསྟེན་པ༌[^2275]རྒུད་པ་ལ་ཤིན་ཏུ་བསྟན་པ༌[^2276]ཉིད་ཅེས་བྱ་བ་འདི་ལྟར་སྨད་པའོ། །

[Block 3311]
རྙེད་མོད་ཅེས་བྱ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་སྨྲས་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^2277]པའི་ཕྱིར་རོ། །

[Block 3312]
འདིར་གཞུང་ནི་བཙུན་པ་རེ་ཞིག་སྐྱེས་པས་བུད་མེད་དང་ལྷན་ཅིག་བརྡ་བགྱིད་པ་ན་དགེ་སློང་དེར་མཆིས་ནས་འདི་སྐད་ཅེས་རྙེད་མོད་ཅེས་མཆིས་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3313]
དེ་ལ་ཅིའི་ཕྱིར་ཁྱེའུ་འདི་མི་སྤྲད་ཅེས་བྱ་བ་ལ་སོགས་པའི་རྣམ་པ་ཚིག་འདི་སྟེ། དེ་བས་ན་ཉེས་པ༌[^2278]སྦོམ་པོར་སྨྲས་པས་ཉམས་པ་ཉིད་ཤེས་ནས་ཉེས་བྱས་ཞེས་བྱ་བ་མདོར་བྱས་པ་ཡིན་ནོ། །

[Block 3314]
གང་གི་ཕྱིར་འདི་ནི་ངེས་པ་མ་ཡིན་ཏེ། བརྗོད་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ན་སྨད་པ་ཉིད་འདིར་རབ་ཏུ་སྦྱར་བའོ། །

[Block 3315]
སྨྱན་བྱེད་པ་ཞུ་བའི་སྐབས་སོ།། །།

[Block 3316]
བྱིན་པ་ལས་དོར་བྱས་པ་སྤྲད་པས་ནི་སྦོམ་པོའོ་ཞེས་བྱ་བ་ལ། བྱིན་པ་ལས་དོར་བྱས་པ་ཞེས་བྱ་བ་ནི་སྔར་བྱིན་ཟིན་པ་ཉིད་ལ་ཕྱིས༌[^2279]དོར་བྱེད་དེ་བུ་མོ་འདི་ངས༌[^2280]མ་བྱིན་ནོ་ཞེས་འདའ་བར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་སྤྲད་ཅིང་སླར་སྦྱིན༌[^2281]དུ་བཅུག་ནས་ཕྲད་ན་སྦོམ་པོའོ། །

[Block 3317]
ཆོས་ཀྱི་ཕུང་པོ་མངོན་དུ་བཏང་སྟེ་བོས་པས་སོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་མཆོད་སྟོན་གསོལ་བ་ལ་སོགས་པ་ཆོས་ཀྱི་ཕུང་པོ་བསོད་སྙོམས་ཀྱི་རྒྱུ་མཚན་གྱི་ཕྱིར་བུད་མེད་ཀྱིས་སྐྱེས་པ་ལ་མངགས་པའི་ཚིག་གིས་གཞན་བོས་ནས་དེས་ཕྲད་ན་སྦོམ་པོའོ། །

[Block 3318]
འདིར་གཞུང་ནི་འཕགས་པ་ཁྱིམ་བདག་ཆེ་གེ་མོ་ལ་འདི་སྐད་ཅེས་ཚུར་ཤོག་ཤིག༌[^2282]ཅེས་སྨྲ་ནུས་སམ། དེས་སྨྲས་པ། གལ་ཏེ་ཁྱོད་དགེ་འདུན་ལ་མཆོད་སྟོན་བྱེད་པ་ལྟ་ན་ནུས་ཏེ་དེར་དེ་བོད་དོ། །

[Block 3319]
དེས་དེ་ལ་རྒྱུ་བྱིན་པ་དང་དགེ་སློང་དེས་མཆོད་སྟོན་བཤམས་ནས་ཁྱིམ་བདག་དེ་འབོད་པ་བཏང་བ་དང་། དེ་གཉིས་ཕྲད་པར་གྱུར་ནས༌[^2283]དགེ་སློང་དེ་འགྱོད་པ་སྐྱེས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3320]
དོན་གཞན་དང་ལྡན་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ་ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་འབོད་ན་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^2284]པའི་ཕྱིར་ཏེ། ཆོས་ཀྱི་ཕུང་པོ་ལས་གཞན་པའི་དོན་ནི་ཁྱོད་ཀྱི་ཁྱིམ་མི་མོ་འདི་ཡིན་ཏེ། སྐྱེ་བོ་འདི་ཡང་དོན༌[^2285]ཐམས་ཅད་ལ་སྐྱོང་བ༌[^2286]ཞེས་བྱ་བ་ལ་སོགས་པ་ཉེ་བར་དགོངས་ནས་བོས་ཏེ་ཕྲད་ན་སྦོམ་པོའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3321]
འདིར་གཞུང་ནི་འཕགས་པ་སྣ་ཆེན་པོ་ལ་གཏོགས་པ་ཆེ་གེ་མོ་ལ་འདི་སྐད་ཅེས། འདི་ནི་ཁྱོད་ཀྱི་ཁྱིམ་མོ་འདི་ནི་ཁྱོད་ཀྱི་མི་སྟེ། དོན་ཐམས་ཅད་ལ་བསྐྱང་བར༌[^2287]བྱ་དགོས་ཀྱིས་ཚུར་ཤོག་ཤིག༌[^2288]ཅེས་སྨྲ་ནུས་སམ། དེས་ནུས་སོ་ཞེས་སྨྲས་ནས་སོང་སྟེ། སྨྲས་པ་དང་དེ་གཉིས་ཕྲད་པར་གྱུར་ནས་དགེ་སློང་འགྱོད་པ་སྐྱེས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3322]
གཞན་ཞེས་བྱ་བས་སྐྱོན་ཆགས་པ་མེད་པར་སེམས་ཅན་ལ་བསྣུན་པ་ཡང་མ༌[^2289]འཕངས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གཞུང་ལས་ཀ་བ་ལ་བསྣུན་པས་བསྣུན་པར་མི་བྱའོ་ཞེས་བྱ་བ་འདི་འམ་གཞན་ལ༌[^2290]ལ་གང་ཡིན་པ་ཞེས་བྱ་བའི་ཚིག་དེས་སྐྱོན་ཆགས་པ་མེད་པར་བརྡེག་པ༌[^2291]པོའི་བསྣུན་པ་སྟེར་དུ་འཇུག་པ་ལ་སེམས་ཅན་ལ་འཕངས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 3323]
ཇི་ལྟར་ཤིང་ལ་སོགས་པ་ལ་བསྣུན་པས་བསྣུན་པ་ལ་ཉེས་བྱས་སུ་འགྱུར་བ་བཞིན་དུ་སྐྱོན་ཆགས་པ་མེད་པའི་སེམས་ཀྱིས་སེམས་ཅན་ལ་བསྣུན་པས་སྣུན་པར༌[^2292]བྱེད་པ་ལས་ཀྱང་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3324]
སྐྱོན་ཆགས་པ་མེད་པའི་སེམས་ཀྱིས་སེམས་ཅན་ལ་སྣུན་པར༌[^2293]བྱེད་པ་གང་ཡིན་པ་དེ་ལ་ནི་ལྟུང་བར་གསུངས་པ་ཡིན་ནོ། །

[Block 3325]
ལྟུང་བ་ལ་འདིར་གཞུང་ནི་ཁྱིམ་བདག་གིས༌[^2294]བུད་མེད་ལ་སྨྲས་པ་ཁོ་བོ་ལ་སྐབས་ཕྱེ་ཤིག །[^2295]དེས་སྨྲས་པ། ཁོ་མོ་མི་ཁོམ་མོ། །

[Block 3326]
སྨྲས་པ་ཁྱོད་དུས་གང་གི་ཚེ་ཁོམ་པར་འགྱུར་བ་ཁོ་བོས་ཇི་ལྟར་ཤེས་པར་བྱ། སྨྲས་པ། ཁོ་མོའི་ཁྱིམ་ན་དགེ་སློང་ཁྱིམ་དུ་ཉེ་བར་འགྲོ་བ་ཡོད་དེ། དེས་ཁྱེད་ཀྱི༌[^2296]རྒྱབ་ཏུ་ཁུ་ཚུར་སྣུན་པར༌[^2297]བྱེད་ནའོ། །

[Block 3327]
དེ་ནས་དགེ་སློང་དེ་ཁྱིམ་དེར་ཞུགས་པ་ན་དེ་ལ་བུད་མེད་དེས་སྨྲས་པ། འཕགས་པ་ཁྱིམ་བདག་ཆེ་གེ་མོའི་རྒྱབ་ཏུ་ཁུ་ཚུར་བསྣུན་ནུས་སམ། དེས་ནུས་སོ་ཞེས་སྨྲས་ཏེ། དེ༌[^2298]སོང་ནས་ཁྱིམ་བདག་དེའི་རྒྱབ་ཏུ་ཁུ་ཚུར་བསྣུན་པ་དང་། དེས་སྨྲས་པ། [^2299]བཙུན་པ་ལ༌[^2300]ལེགས་སོ་ལེགས་སོ་དོན་གྲུབ་བོ། །

[Block 3328]
དེས་སྨྲས་པ། འདི་ཅི་ཞིག་ཡིན། སྨྲས་པ། བརྡའོ། །

[Block 3329]
དགེ་སློང་དེ་འགྱོད་པ་སྐྱེས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་འདུན་ལྷག་མའི་ལྟུང་བར་མི་འགྱུར་ཏེ། ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3330]
སྨྱན་བྱེད་པའི་འདུལ་བྱེད་རྣམས་སོ།། །།
--- END BLOCKS ---
