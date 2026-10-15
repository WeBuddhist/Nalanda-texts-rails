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
[Block 4901]
འདིར་ཁ་ཏོན་ཞུ་བ་སྨོས་པས་ཀློག་པ་ཡང་བསྡུས་པ་ཡིན་ནོ། །

[Block 4902]
བཙུན༌[^3319]མོ་ཕྲེང་ལྡན་མ་དང་དབྱར་ཚུལ་མ་གཉིས་ཀྱིས་ཀློག་པའི་ཕྱིར་ཅི་བཀླགས༌[^3320]ལགས་སམ་ཞེས་བྱ་བ་དང་ལྷོགས་ཤིག་ཅེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 4903]
དུས་ཁྲིམས་དབོག་པ་དང་ཡོན་བཤད་པ་གཉིས་ཀྱི་གཞུང་ནི་ཞུ་བའི་གཞུང་ཁ་ཅིག་ལས་ཡོན་བཤད་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 4904]
བསྙེན་གནས་ཡན་ལག་བརྒྱད་དང་ལྡན་པ་དབོག་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4905]
གནས་གཞན་དུ་ནི་སྔ་མ་མ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། གནས་གཞན་དུ་ཞེས་བྱ་བ་ནི་ཁང་བཟངས༌[^3321]ལ་སོགས་པར་སྟོན་པ་ལ་སྔ་མ་གནས་ཁང་ལ་སོགས་པར་བྱས་པ་དང་ལྷན་ཅིག་མ་བྱས་པ་ཉིད་དེ། དེ་ལ་ལྟུང་བ་རྣམ་པར་གཞག་པར་མི་བྱའོ་ཞེས་བྱ༌[^3322]བའི་དོན་ཏོ། །

[Block 4906]
སྟོན་པའོ།། །།

[Block 4907]
གང་དུ་འདོན་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བསྙེན་པར་མ་རྫོགས་པ་དང་ཅིག་ཅར་རམ་མཇུག་ཐོགས་སུ་སྟོན་བྱེད་དུ་གྱུར་པའི་ཆོས་དང་ཡི་གེ་ཡང་འདོན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་ལུང་ལས་གསལ་བར་གྱུར་པ་འམ་སྟོན་བྱེད་དུ་གྱུར་པ་ཉིད་ཀྱིས་མངོན་པར་འདོན༌[^3323]པའོ། །

[Block 4908]
བསྙེན་པར་མ་རྫོགས་པ་དང་ཅིག་ཅར་རམ༌[^3324]བསྙེན་པར་མ་རྫོགས་པ་ལས་གནས་ཀྱི་རྒྱུད་དུ་གྱུར་པའི་འདོན་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4909]
གནས་མ་ཡིན་པ་ལ་ཡང་སྟོན་བྱེད་དུ་འགྱུར་ཏེ། དེ་འདི༌[^3325]ལྟ་སྟེ་དཔེར་ན་འཕོང་གི་རིག་བྱེད༌[^3326]དེ་དེ་གསལ་བའི་དོན་དུ་ཆོས་ཞེས་བྱ་བའི་ཚིག་སྨོས་པ་ཡིན་ནོ། །

[Block 4910]
སྟོན་བྱེད་དུ་གྱུར་པ་ལས་བྱུང་བ་ལ་མཉམ་པར་སྦྱོར་བ་གཞན་ལས་ཡི་གེ་མ་ཡིན་པར་བྱས་པའི་ཆོས་དང་ལྡན་པ་དོན་ལ་ཆོས་སུ་འགྱུར་ཏེ། དེ་བསལ་བའི་སྟོན་བྱེད་དུ་གྱུར་པ་ཞེས་བྱ་བའི་ཚིག་གོ། །

[Block 4911]
དེ་ལྟར་གཉིས་ཀ་ཡང་ཆོས་འཇིག་པའོ། །

[Block 4912]
གང་ཅུང་ཟད་བློ་ལ་ཉེ་བར་སོན་པ་ཞེས་བྱ་བ་འདི་ལ་བཏགས༌[^3327]པའོ། །

[Block 4913]
སྟོན་བྱེད་དུ་གྱུར་པ་ལ་ཡང་འདི་ཡོངས་སུ་གྲུབ་པའི་སྐྱོན་དུ་གྱུར་པ་སྟེ་གཞན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4914]
སྟོན་བྱེད་དུ་གྱུར་པའི་དོན་ལ་ཡང་སྟོན་བྱེད་དུ་གྱུར་པ་གནས་ཡིན་ཏེ་དེར་གྱུར་པའོ། །

[Block 4915]
དེ་ལ་གནས་ནི་ཡང་དག་པའི་གནས་ཏེ། དེའི་རྒྱུ་ནི་བརྗོད་པར་འདོད་པའི་དོན་སྟོན་པའི་ཕྱིར་རབ་ཏུ་རྒྱས་པའི་ངོ་བོས་ཚིག་དང་ངག་གི༌[^3328]རྒྱུན་གྱིས་གནས་པའོ། །

[Block 4916]
དེ་ལྟ་བུར་གྱུར་པའི་དོན་འདོན་པ་ལ་ལྟུང་བྱེད་དོ། །

[Block 4917]
ཆོས་ལ་ཞེས་བྱ་བ་ནི་མིང་དང་ཚིག་གི་བདག་ཉིད་སངས་རྒྱས་ཀྱིས་གསུངས་པ་འམ་དེའི་ཉན་ཐོས་ཀྱིས་བཤད་པའོ། །

[Block 4918]
ཡི་གེ་ཡང་ཞེས་བྱ་བ་ནི་ཡིག་འབྲུ་ཙམ་ཡང་ངོ་། །འདིར་དེ་ལས་གཞན་པའི་འདོན་པ་ལ་རྩོམ་པ་གཅིག་པུར་འགྱུར་བ་ཉིད་ཀྱི་ཕྱིར་ལྟུང་བ་གཅིག་པུ་ཉིད་དོ། །

[Block 4919]
དེ་ལྟར་ཡང་ཚིག་ཅིག་ཅར་བརྗོད་ན་ལྟུང་བྱེད་དོ། །

[Block 4920]
ཚིག་སོ་སོར་བརྗོད་ན་ལྟུང་བྱེད་དོ། །

[Block 4921]
ཅིག་ཅར་ཡི་གེ་བརྗོད་ན་ལྟུང་བྱེད་དོ། །

[Block 4922]
མཇུག་ཐོགས་སུ་ཡི་གེ་བརྗོད་ན་ལྟུང་བྱེད་དོ་ཞེས་བྱ་བ༌[^3329]ལན་ཅིག་བརྩམ་པར་བྱས་ནས་ཚིག་ཅིག་ཅར་དང་། ལྷག་པའི་ཚིག་དང་ཅིག་ཅར་ཡི་གེ་དང་། ཡི་གེ་ལྷག་པར་རྗོད་པར་བྱེད་ན་ལྟུང་བྱེད་ཅེས་བྱ་བའོ། །

[Block 4923]
དེ་ལྟར་བསྡུས་ནས་ལྟུང་བྱེད་ལ་གཅིག་པ་ཉིད་གསུངས་སོ། །

[Block 4924]
ཧ་ཅང་ཐལ་བ་ལ་དམིགས་ཀྱིས་བསལ་བའི་ཕྱིར་མི་འདོད་བཞིན་དུ་གྲུབ་པ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལྟར་ཡང་གཞུང་ནི་ལྡབ་ལྡིབ་ཅན་དང་སྨྲ་མྱུར་བ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་འདིས་འདི་བསྡུས་པ་ཡིན་ནོ། །

[Block 4925]
རྗེས་སུ་ཉན་དུ་གཞུག་པར་བྱ་བ་འདོན་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བར་སྦྱར༌[^3330]རོ། །

[Block 4926]
རྗེས་སུ་ཉན་དུ་གཞུག་པར་བྱ་བ་ནི་གང་ཞིག་ཅིག་ཅར་རམ་ཐོག་མར་བརྗོད་པར་བྱ་བ་མ་ཡིན་པ་ཞེས་བྱ་བ་དེ་ཁྲེལ་དང་བཅས་པ་ཉིད་དོ། །

[Block 4927]
དེ་ལྟར་ངེས་པར་སྦྱོར་བ་ལ་དོགས་པ་དང་བཅས་པར་ཅིག་ཅར་རམ་འདས་པར་བྱས་ནས་འདོན་པ་ལ་ཡང་དག་པར་གནས་པ་སྟེ་རྒྱུད་པ་དེ་ལྟ་བུས་ནི་མ་ཡིན་ནོ། །

[Block 4928]
ཁ་ཏོན་ཞུ་བ་དང་སློབ་གཉེར་བསོད་པ༌[^3331]དང་། དམིགས་ཀྱིས་འདྲི་བ༌[^3332]ཡང་ངོ་ཞེས་བྱ་བ་ཡང་མ་གཏོགས་སོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4929]
ཐོག་མར་བཟུང་ཏེ་རང་དགར་འདོན་པ་ལ་རྒྱུད་པ་འདི་ཡང་དག་པར་གནས་པའོ། །

[Block 4930]
དེ་ལ་ཁ་ཏོན་ཞུ་བ་ཞེས་བྱ་བ་ནི་སྔར་སྟོན་པ་མི་བརྗེད་པར་བྱ་བའི་ཕྱིར་སྦྱོར་བའོ། །

[Block 4931]
སློབ་གཉེར་བསོད་པ༌[^3333]ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པ་ལ་བཟུང་བ་ཡོངས་སུ་རྫོགས་པར་ཟློས་ཤིང་འཆད་པར་འགྱུར་རོ། །

[Block 4932]
དམིགས་ཀྱིས་འདྲི་བ༌[^3334]ཞེས་བྱ་བ་ནི་ཕྱོགས་འགའ་ཞིག་དྲན་པར་བྱ་བའི་ཕྱིར་རམ་ཐེ་ཚོམ་བཅད་པའི་ཕྱིར་ཀུན་ནས་འཛིན་པར་བྱེད་པའོ། །

[Block 4933]
འདོན་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 4934]
དགེ་སློང་དང་དགེ་སློང༌[^3335]མ་སྡིག་ཅན་དག་ཁྱིམ་དུ་སོ་སོར་གོ་བར་བྱེད་པ་བསྐོ་བར་བྱའོ། །

[Block 4935]
ཁྱིམ་རྣམས་སུ་སོ་སོར་གོ་བར་བྱེད་པས་ཚེ་དང་ལྡན་པ་དག་ཉོན་ཅིག །ཁྱིམ་རྣམས་སུ་ཁྱིམས༌[^3336]སུན་འབྱིན་པར་བྱེད་པ་དང་། གནས་རྣམས་སུ་གནས་སུན་འབྱིན་པར་བྱེད་པ་དག་ཡོད་དེ། འདི་ལྟ་སྟེ་དཔེར་ན་འབྲས་སཱ་ལུའི་ཞིང་ཕུན་སུམ་ཚོགས་པ་ལ་སེར་བའི་འཁོར་ལོ་མི་བཟད་པ༌[^3337]བབ་ན༌[^3338]འདི་ལྟར་འབྲས་སཱ་ལུ་དེ་ཉིད་ཤིན་ཏེ་མ་དང་ཆུད་ཟ་བ་དང་ཚུལ་མ་ཡིན་པས་མ་རུང་བར་འགྱུར་བ་དང་བུ་རམ་ཤིང་གི་ཞིང་ཕུན་སུམ་ཚོགས་པ་ལ་ནད་ཀྱི་རིགས་དམར་པོ་ཞེས་བྱ་བ་བྱུང་ན་འདི་ལྟར་བུ་རམ་ཤིང་དེ་ཉིད་ཤིན་ཏེ་མ་དང་ཆུད་ཟ་བ་དང་ཚུལ་མ་ཡིན་པས་མ་རུང་བར་གྱུར་པ༌[^3339]ལྟ་བུ་དག་ཡོད་ཀྱི༌[^3340]ཚེ་དང་ལྡན་པ་དག་ཁྱེད་ཅག་དགེ་སློང་འདི་དང་དགེ་སློང་མ་འདིས་བསྟན་པའི་ཚོད་མ་འཛིན་ཅིག །འདི་ལྟར་དགེ་སློང་འདི་དང་དགེ་སློང་མ་འདི་ནི་ཡོས་ཚིག་པ་བཞིན་དུ་ཆོས་འདུལ་བ་འདི་ལ་སྐྱེར་མི་རུང་བའི་ཆོས་ཅན་ཡིན་གྱི་བཅོམ་ལྡན་འདས་དང་དགེ་སློང་གནས་བརྟན་རྣམས་ལ་ལྟོས་ཤིག་ཅེས་སྨྲ་བར་བྱའོ། །

[Block 4936]
མི་སྤྲོ་ན་གསོལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་དུ་སོ་སོར་གོ་བར་བྱེད་པ་དང་ཁྱིམ་རྣམས་སུ་སོ་སོར་གོ་བར་བྱེད་པ་མི་སྤྲོ་ན་ཐམས་ཅད་ཀྱིས་དགེ་སློང་དང་དགེ་སློང་མ་འདི་གཉིས་སྡིག་ཅན་ཡིན་ནོ་ཞེས་ཁྱིམ་དུ་སོ་སོར་གོ་བར་བྱེད་པ༌[^3341]ཞེས་བྱ་བ་དེའི་དོན་དུ་གསོལ་བར་བྱའོ། །ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 4937]
འདུ་ཤེས་གང་ལ་ཞེ་ན། དེའི་ཕྱིར་ཉན་པ་པོ་མི་ཤེས་པ་ཉིད་དང་བསྙེན་པར་མ་རྫོགས་པ་ཉིད་དག་དང་ལྡན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉན་པ་པོ་བསྙེན་པར་མ་རྫོགས་པ་ཉིད་ལ་ཕམ་པ་དང་དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་གང་ཡིན་པ་དེ་འདི་ལས་ཤེས་པ་ཡིན་ཏེ། དེ་ལ་ཡང་ཉན་པ་པོས་མི་ཤེས་པ་ཉིད་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4938]
ཅི་ཞིག་རྗེས་སུ་བསྒྲུབས་ན་གནས་ངན་ལེན་བརྗོད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4939]
བརྗོད་པར་བྱ་བ་ཅི་ཞིག་སྨྲས་པས་ཤེ་ན། དེའི་ཕྱིར་ཕམ་པར་འགྱུར་བ་དང་དགེ་འདུན་ལྷག་མ་དག་སོ་སོར་ཡང་རུང་བསྡུས་པ་ཡང་རུང་ངོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4940]
དོན་དུ་མ་ཉིད་ལ་ཚིག་ཐ་དད་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་དེའི་ཕྱིར་བསྡུས་པ་དེ་ཉིད་ལ་ལྟུང་བ་གཅིག་ཉིད་ཡིན་ཏེ་ཚིག་གཅིག་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
