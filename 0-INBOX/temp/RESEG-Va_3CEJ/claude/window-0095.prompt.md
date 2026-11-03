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
[Block 3326]
ཡང་ཟས་དུ་ཞིག་ནི་སེམས་ཅན་བྱུང་བ་རྣམས་གནས་པར་བྱེད་པ་ཡིན། དུ་ཞིག་ནི་སྲིད་པ་ཚོལ་བ་རྣམས་ལ་ཕན་འདོགས་པར་བྱེད་པ་ཡིན་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་ཐམས་ཅད་ཀྱང་གཉི་ག་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3327]
ཁམ་གྱི་ཟས་ཀྱང་དེ་ལ་ཆགས་པ་རྣམས་ཀྱི་ཡང་འབྱུང་བར་བྱེད་པ་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་ཟས་བཞི་ནི་ནད་དང་། འབྲས་དང་། ཟུག་རྔུའི་རྩ་བ་ཡིན་ནོ། །

[Block 3328]
རྒ་ཤིའི་རྐྱེན་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 3329]
ཡིད་ལ་སེམས་པ་ཡང་འདིར་གནས་པར་བྱེད་པ་ཡིན་པར་སྣང་སྟེ། འདི་སྐད་དུ་ལོ་ཉེས་ཀྱིས་ཉེན་པའི་ཕ་ཞིག་གིས་ཐལ་བའི་རྐྱལ་བ་ཁ་ཐུར་མས་གཏུར་ཏེ་ཕྱེ་ཡིན་ནོ། །

[Block 3330]
བར་དུ་བུ༌[^1898]གཉིས་ཤིག་ཡིད་ཆེས་པར་བྱས་པ་དང་། དེ་གཉིས་ཀྱང་དེ་ལ་རྟོག་པར་བྱེད་ཅིང་རིང་མོ་ཞིག་ཏུ་གནས་པར་གྱུར་ཏོ། །

[Block 3331]
གཅིག་གིས་ཁ་ཕྱེ་ནས་ཐལ་བ་ཡིན་ནོ་སྙམ་སྟེ་རེ་བ་མེད་པར་གྱུར་པ་དང་ཤིའོ། །

[Block 3332]
ཡང་རྒྱ་མཚོར་གྲུ་ཆག་པའི་མི་ཞིག་ཐང་ཡིན་ནོ་སྙམ་ནས་དབུ་བའི་ཕུང་པོ་ཆེན་པོ་ཞིག་གི་དྲུང་དུ་སོང་སྟེ། དེ་ལ་ཀུན་དུ་བསྣམས༌[^1899]ནས་རེ་བ་མེད་པ་དང་ཤིའོ་ཞེས་གྲག་གོ་ཞེས་བརྗོད་དོ། །

[Block 3333]
འགྲོ་བའི་རྣམ་གྲངས་ལས་ཀྱང་རྒྱ་མཚོ་ཆེན་པོ་ནས་སྲོག་ཆགས་ཆེ་ལོང་རྣམས་ཆུ༌[^1900]ནང་ནས་སྐམ་ལ་འཐོན་ཏེ་བྱེ་མ་ཅན་གྱི་ཐང་ལ་སྒོ་ང་རྣམས་བཞག་ནས་བྱེ་མས་བཀབ་སྟེ་སླར་ཡང་རྒྱ་མཚོའི་ནང་དུ་འགྲོའོ། །

[Block 3334]
དེ་ལ༌[^1901]མ་གང་དག་གིས་སྒོ་ང་ལས་བརྩམས་ཏེ་དྲན་པས་མ་བརྗེད་པའི་སྒོ་ང་དེ་དག་ནི་འདྲུལ་བར་མི་འགྱུར་རོ། །

[Block 3335]
གང་དག་གིས་བརྗེད་པ་དེ་དག་ནི་འདྲུལ་བར་འགྱུར་རོ་ཞེས་བཤད་དེ། གཞན་གྱི་ཟས་ཀྱིས་ཟས་དང་བཅས་པར་འགྱུར་དུ་འོང་བའི་ཕྱིར་དེ་ནི་མི་བརྗོད་ཀྱི། འདི་སྐད་དུ་སྒོ་ང་གང་དག་གིས་མ་ལས་བརྩམས་ནས་དྲན་པས་མི་བརྗེད་པས༌[^1902]དེ་དག་ནི་རེག་པའི་གནས་སྐབས་དེ་དྲན་པས་འདྲུལ་བར་མི་འགྱུར་ལ། གང་དག་གིས་བརྗེད་པ་དེ་དག་ནི་འདྲུལ་བར་འགྱུར་རོ་ཞེས་ནི་བརྗོད༌[^1903]དོ། །

[Block 3336 [HEADING]]
##### ཟས་བཞིར་གསུངས་པ། ^3-1-12-4-0

[Block 3337]
ཡང་ཅིའི་ཕྱིར་ཟས་བཞི་ཁོ་ན་ཡིན་ནོ། །

[Block 3338]
[^1904]ཟག་པ་དང་བཅས་པའི་ཆོས་ཐམས་ཅད་སྲིད་པ་རྣམས་གསོ་བར་བྱེད་པ་དག་མ་ཡིན་ནམ་ཞེ་ན། དེ་ནི་དེ་ལྟ་ན༌[^1905]ཡིན་མོད་ཀྱི་འོན་ཀྱང་གཙོ་བོར་བཤད་དེ། འདི་ལ་གནས་དང་ནི།

[Block 3339 [VERSE]]
རྟེན་པ་རྒྱས་པའི་དོན་དུ་གཉིས། །
སྲིད་གཞན་འཕེན་དང་འགྲུབ་པ་ཡི། །
དོན་དུ་གཉིས་ཏེ་གོ་རིམས་བཞིན། །

[Block 3340]
གནས་ནི་དབང་པོ་དང་བཅས་པའི་ལུས་སོ། །

[Block 3341]
དེ་རྒྱས་པར་བྱེད་པ་ནི་ཁམ་གྱི་ཟས་སོ། །

[Block 3342]
རྟེན་པ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བའི་ཆོས་རྣམས་སོ། །

[Block 3343]
དེ་དག་རྒྱས་པར་བྱེད་པ་ནི་རེག་པ་སྟེ། རེ་ཞིག་འདི་གཉིས་ནི་འདིར་སྐྱེས་པའི་སྲིད་པ་གསོ་བར་བྱ་བ༌[^1906]གཙོ་བོ་ཡིན་ནོ། །

[Block 3344]
ཡིད་ལ་སེམས་པས་ནི་ཡང་སྲིད་པ་འཕེན་པར་བྱེད་དོ། །

[Block 3345]
འཕངས་ཟིན་པ་ནི་ལས་ཀྱིས་ཡོངས་སུ་བསྒོས་པའི་རྣམ་པར་ཤེས་པའི་ས་བོན་ལས་མངོན་པར་འགྲུབ་པས་འདི་གཉིས་ནི་མ་སྐྱེས་པའི་སྲིད་པ་སྐྱེས་པ༌[^1907]ལ་གཙོ་བོར་ཡིན་ནོ། །

[Block 3346]
[^1908]དེའི་ཕྱིར་བཞིར་གསུངས་སོ། །

[Block 3347]
སྔ་མ་གཉིས་ནི་སྐྱེས་ཟིན་པ་གསོ་བར་བྱེད་པ་ཡིན་པའི་ཕྱིར་མ་མ་ལྟ་བུ་དག་ཡིན་ནོ། །

[Block 3348]
ཕྱི་མ་གཉིས་ནི་སྐྱེད་པར་བྱེད་པ་མ༌[^1909]ཡིན་པའི་ཕྱིར་མ་ལྟ་བུ་དག་ཡིན་ནོ། །གང་ལ་ལ་ཁམ་ཡིན་པ་དེ་ཐམས་ཅད་ཟས་ཀྱང་ཡིན་ནམ་ཞེ་ན། ཁམ་ཡིན་ལ་ཟས་མ་ཡིན་པ་ཡང་ཡོད་དོ་ཞེས་བྱ་བ་མུ་བཞི་སྟེ། མུ་དང་པོ་ནི་ཁམ་གང་ལ་བརྟེན་ནས་དབང་པོ་རྣམས་ཉམས་པར་འགྱུར་ལ། འབྱུང་བ་ཆེན་པོ་རྣམས་ཀྱང་ཡོངས་སུ་འཇིག་པར་འགྱུར་བའོ། །

[Block 3349]
མུ་གཉིས་པ་ནི་ཟས་གསུམ་པ༌[^1910]དག་གོ། །

[Block 3350]
གསུམ་པ་ནི་ཁམ་གང་ལ་བརྟེན་ནས་དབང་པོ་རྣམས་རྒྱས་པར་འགྱུར་ཞིང་འབྱུང་བ་ཆེན་པོ་རྣམས་ཀྱང་འཕེལ་བར་འགྱུར་བའོ། །

[Block 3351]
བཞི་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 3352]
དེ་བཞིན་དུ་རེག་པ་ལ་སོགས་པས་ཀྱང༌[^1911]ཅི་རིགས་པར་མུ་བཞིར༌[^1912]བྱའོ། །

[Block 3353]
རེག་པ་ལ་སོགས་པ་ལ་བརྟེན་ནས་དབང་པོ་རྣམས་རྒྱས་པར་འགྱུར་ཞིང་འབྱུང་བ་རྣམས་ཀྱང་འཕེལ་བར་འགྱུར་བ༌[^1913]དེ་དག་ཟས་ཀྱང་མ་ཡིན་པ་ལྟ་ཡོད་དམ་ཞེ་ན། ཡོད་དེ། གཞན་གྱི་ས་པ་དང་། ཟག་པ་མེད་པ་རྣམས་སོ། །

[Block 3354]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ། གང་ཞིག་ཟོས་ནས་ཟ་བ་པོ་ལ་གནོད་པར་བྱེད་པ་དེ་ལ༌[^1914]ཡང་དང་པོ་ཕན་འདོགས་པའི་ཕྱིར་ཟས་ཡིན་ནོ། །

[Block 3355]
ཟས་ནི་དུས་གཉིས་སུ་ཟས་ཀྱི་བྱ་བ་བྱེད་དེ། ཡོངས་སུ་ལོངས་སྤྱོད་པའི་ཚེ་དང་། འཇུ་བའི་ཚེའོ་ཞེས་ཟེར་རོ། །

[Block 3356]
འགྲོ་བ་གང་ན་ཟས་དུ་ཞིག་ཡོད་ཅེ་ན། ཐམས་ཅད་ན་ཐམས་ཅད་ཡོད་དེ། སྐྱེ་གནས་དག་ན་ཡང་དེ་དང་འདྲའོ། །

[Block 3357]
དམྱལ་བ་དག་ན་ཁམ་གྱི་ཟས་ཇི་ལྟ་བུ་ཞེ་ན། ལྕགས་ཀྱི་ཐུ་ལུམ་འབར་བ་དང་། ཟངས་ཞུན་མ་ཡིན་ནོ། །

[Block 3358]
གལ་ཏེ་གནོད་པར་བྱེད་པ་ཡང་ཟས་ཡིན་ན་ནི་མུ་བཞི་ལ་ཡང་གནོད་པར་འགྱུར་ལ་རབ་ཏུ་བྱེད་པའི་གཞུང་ཁམ་གྱི་ཟས་གང་ཞེ་ན། ཁམ་གང་ལ་བརྟེན་ནས་དབང་པོ་རྣམས་རྒྱས་པར་འབྱུང༌[^1915]ཞིང་འགྱུར་བ༌[^1916]ཆེན་པོ་རྣམས་ཀྱང་འཕེལ་བ་དང་འཚོ་བ༌[^1917]དང་ཉེ་བར་འཚོ་བར་འགྱུར་བའོ་ཞེས་བྱ་བ་ནས། རྣམ་པར་ཤེས་པའི་བར་དུ་རྒྱས་པར་གསུངས་པ་ལ་ཡང་གནོད་པར་འགྱུར་རོ་ཞེ་ན། རྒྱས་པར་འགྱུར་བའི་ཟས་ལ་དགོངས་ཏེ་གསུངས་པའི་ཕྱིར་འགལ་བ་མེད་དོ། །

[Block 3359]
ཉམས་པར་འགྱུར་བའི་ཟས་ནི་དམྱལ་བ་དག་ཏུ་ཟས་ཀྱི་མཚན་ཉིད་ཐོབ་པའི་ཕྱིར་ཏེ། དེས་ཀྱང་བཀྲེས་པ་དང་སྐོམ་པ་དག་འཇོམས་པར་ནུས་པའི་ཕྱིར་རོ། །

[Block 3360]
གཞན་ཡང་ཉི་ཚེ་བའི་དམྱལ་བ་དག་ན་མི་དང་འདྲ་བར་ཁམ་གྱི་ཟས་ཡོད་པའི་ཕྱིར་འགྲོ་བ་ལྔ་པ་ཉིད་དུ་རིགས་སོ། །

[Block 3361 [HEADING]]
##### འཛམ་བུའི་ཚལ་ན་འདུག་པའི་སོ་སོའི་སྐྱེ་བོ། ^3-1-12-5-0

[Block 3362]
བཅོམ་ལྡན་འདས་ཀྱིས། གང་གིས་ཕྱིའི༌[^1918]དྲང་སྲོང་འདོད་པ་དག༌[^1919]ལས་འདོད་ཆགས་དང་བྲལ་བ་བརྒྱ་ལ་ཟས་བྱིན་པ་བས་གང་གིས་འཛམ་བུའི་ཚལ་ན་འདུག་པའི་སོ་སོའི་སྐྱེ་བོ་གཅིག་ལ་བྱིན་ན་སྦྱིན་པ༌[^1920]དེ་བས་སྦྱིན་པ་འདི་འབྲས་བུ་ཆེས་ཆེའོ་ཞེས་གསུངས་པ། འཛམ་བུའི་ཚལ་ན་འདུག་པའི་སོ་སོའི་སྐྱེ་བོ་ཞེས་བྱ་བ་ནི༌[^1921]གང་ཞེ་ན། ཁ་ཅིག་ན་རེ་འཛམ་བུའི་གླིང་ན་གནས་པ་ལྟོ༌[^1922]དང་ལྡན་པ་དག་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3363]
དེ་ནི་རིགས་པ༌[^1923]མ་ཡིན་ཏེ། གཅིག་ཅེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3364]
སོ་སོའི་སྐྱེ་བོ་མང་པོ་ལ་ཟས་བྱིན་ན་བསོད་ནམས་མང་པོར་འགྱུར་གྱི་འདོད་ཆགས་དང་བྲལ་བ་ཉུང་ངུ་ལ་ཟས་བྱིན་པས༌[^1924]ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་གང་ཡིན་པ༌[^1925]འདི་ལ་ཁྱད་པར་ཅི་ཞིག་ཡོད། གཞན་དག་ན་རེ་བྱང་ཆུབ་སེམས་དཔའ་ཉེ་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3365]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་དེ་སྐད་དུ་མི་བརྗོད་དེ། དེ་ལ་བྱིན་ན་དགྲ་བཅོམ་པ་བྱེ་བ་ལ་བྱིན་པ་བས་བསོད་ནམས་ཆེས་མང་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
