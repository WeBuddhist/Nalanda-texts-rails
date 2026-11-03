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
[Block 4306]
དགེ་སློང་དག་དེ་ལྟ་བས་ན་ཇི་ལྟར་ཆུ་ཀླུང་ཡིད་འོང་ལྡན་གྱི་ངོགས་ཀྱི་དགེ་སློང་དག་གིས༌[^2985]བརྩོན་འགྲུས་བརྩམས་པ་དེ་ལྟར་གདོས་བུ་དང་ཕོ་ལོང་གི་སྦྱོར་བས་བརྩོན་འགྲུས་བརྩམ་པར༌[^2986]བྱའོ་ཞེས་བྱ་བ་ཕྱི་མ་ལས་ཀྱང་དགེ་སློང་གིས་བརྩོན་འགྲུས་གློད་པར་མི་བྱའོ། །

[Block 4307]
བརྩོན་འགྲུས་གློད༌[^2987]པར་བྱེད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4308]
གང་དུ་འདི་ལས་འོག༌[^2988]ཏུ་གཞུང༌[^2989]མ་བཤད་པ་དེར་ཡང་གཞུང་འདི་ཕྲན་ཚེགས་དག་ལས་རིག་པར་བྱའོ། །

[Block 4309]
བརྩོན་འགྲུས་གློད་པར༌[^2990]མི་བྱའོ། །

[Block 4310]
འདི་ནི་མདོ་འདི༌[^2991]ལས་གསུངས་པ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་འདིར་དགེ་སློང་ཉིན་མོ་འདུག་པ༌[^2992]དང་འཆག་པ་དག་གིས་སྒྲིབ་པར་འགྱུར་བའི་ཆོས་རྣམས་ལས་སེམས་ཡོངས་སུ་སྦྱོང་བར་བྱེད་ཅིང་མཚན་མོའི་ཐུན་དང་པོ་ལ་འདུག་པ་དང་འཆག་པ་དག་གིས་སྒྲིབ་པར་འགྱུར་བའི་ཆོས་རྣམས་ལས་སེམས་ཡོངས་སུ་སྦྱོང་བར་བྱེད་ཅིང་ནམ་གྱི་གུང་ཐུན་ལ་གཙུག་ལག་ཁང་གི་ཕྱི་རོལ་དུ་རྐང་པ་བཀྲུས་ནས་གཙུག་ལག་ཁང་དུ་ཞུགས་ཏེ། གློ་གཡས་པ་ཕབ་སྟེ་རྐང་པ་རྐང་པའི་སྟེང་དུ་བཞག་ནས་སྣང་བའི་འདུ་ཤེས་དང་ལྡན་པས་དྲན་པ་དང་ཤེས་བཞིན་དང་ལྡན་པས་དབུགས་དབྱུང་བ་མ་ཡིན་པའི་འདུ་ཤེས་སུ་བྱེད་ཅིང་། དེ་མཚན་མོའི་ཐུན་ཐ་མ་ལ་མྱུར་བ་མྱུར་བར་རབ་ཏུ་སད་ནས་འདུག་པ་དང་། འཆག་པ་དག་གིས་སྒྲིབ་པར་འགྱུར་བའི་ཆོས་རྣམས་ལས་སེམས་ཡོངས་སུ་སྦྱོང་བར་བྱེད་ཅིང་། དེ་ཙམ་གྱིས་དགེ་སློང་བརྩོན་འགྲུས་བརྩམས་པར་འགྱུར་རོ། །

[Block 4311]
དེ་ཙམ་གྱིས་ཡང་དེ་བཞིན་གཤེགས་པས་དགེ་སློང་བརྩོན་འགྲུས་བརྩམས་པར་ཤེས་པ༌[^2993]ནས་གང་དུ་བཀའ་བསྒོ་བ་ཞེས་གང་ཞིག་མདོ་སྡེ་ལས་བརྩོན་འགྲུས་དང་ལྡན་པ་ཞེས་འདིར་རྟོགས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4312]
འདིར་ཉལ་བ་ལ་མ་མོ་ལས་ལྷག་པར་འདོན་པ་དེ་འདི་བསྡུ་བར་བྱ་སྟེ། ལུས་དང་སེམས་དང་གོས་མ༌[^2994]འཕྱར་བར་ཉལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ལུས་དང་སེམས་དང་གོས་དག་རེ་རེ་ལ་མི་འཕྱར་བར་ཞེས་སོ་སོར་སྦྱར་བར་བྱའོ། །

[Block 4313]
མི་ན་བས༌[^2995]ཉིན་མོ་ཉལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། འདིར་ངལ་བ་ཡང་ན་བ་སྟེ། ལུས་ཉམ་ཆུང་བར༌[^2996]ཞེས་བྱ་བར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 4314]
[^2997]གང་དག་དེའི་བར་དུ་གཉིད་ཀྱིས་སྙོམ་པ་བརྣགས་མི་ཐུབ་པ་ཉིད་ཡིན་ན། གཉིད་ཀྱི༌[^2998]སྙོམ་པ་བསང་བའི་ཕྱིར་དེས་དེ་ཙམ་ཞིག་བསྟེན་པར༌[^2999]བྱ་ཞེས་བྱ་བ་ནི་རྩ་བའི་གཞི་ལས་ཤེས་པར་བྱའོ། །

[Block 4315]
ཟས་ཀྱིས་སྙོམ་པ༌[^3000]བརྣགས་མི་བཟོད་པ་ཞིག་ཡིན་ན་ཡང་དེ་བསང་བའི་ཕྱིར་དེ་ཙམ་ཞིག་བསྟེན་པར་བྱའོ། །

[Block 4316]
འདི་ལ་ཡང་དེ་ལྟ་བུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4317]
མདོ་སྡེ་ལས་ཀྱང་མེར་འཇུག་གི་བུས་ནི་དཔྱིད་རྣམས་ཀྱི་ཟླ་བ་ཐ་མ་ལ་ཡུད་ཙམ་ཞིག་ཟད་ཀྱིས༌[^3001]སྙོམ་པ་བསང་བར་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4318]
རོ་རྒྱབ་ན་བས་པུས༌[^3002]འཁྱུད་བཅང་བར་བྱའོ། །

[Block 4319]
དབང་པོ་རྣམས་ནང་དུ་བསྡུས་པ་དང་། ཡིད་ཕྱི་རོལ་དུ་མ་སོང་བ་དང་། གསལ་བ་དང་དྲང་པོས་མི་ཐོགས་པར་བཅག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། ཕྱི་རོལ་དུ་མ་སོང་བའི་ཞེས་བྱ་བ་ནི་ཡུལ་རྣམས་ལ་མ་སོང་བ་སྟེ། ཁ་ཕྱིར་ཕྱོགས་པ་ཉིད་ཀྱིས་ཕྱིར༌[^3003]འགྲོ་བ་འདི་ལ་ཕྱི་རོལ་དུ་འགྲོ་བའི་བདག་ཉིད་ཅན་སའི་དབྱིངས་ལ་སོགས་པ་རྣམས་ཀྱིས་ཀྱང་འདིར་ཡུལ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 4320]
གསལ་བ་ཞེས་བྱ་བ་ནི་སེམས་དང་བ་དང་རབ་ཏུ་ཟིན་པའི་ལུས་ཀྱིས་སོ། །

[Block 4321]
དྲང་པོར་ཞེས་བྱ་བ་ནི་གོམ་པ་ཡ་ཡོ་མེད་པས་སོ། །

[Block 4322]
མི་ནུས་ན་ཐ་གུ་བྲེལ༌[^3004]ཏེའོ་ཞེས་བྱ་བ་ནི། དྲང་པོར་འཆག་མི་ནུས་ན་ཐ་གུ་སྦྲེལ་ཏེ་བཅག་པར་བྱའོ། །

[Block 4323]
ཁ་ཏོན་པའི་འཆགས་ནི་ཁྲུ་བཅུ་གཉིས་སོ། །

[Block 4324]
སྤོང་བ་པ་ནི་བཅོ་བརྒྱད་དོ། །

[Block 4325]
དེ་ཐ་གུས་གཞལ་ཏེ་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་འཆག་པའོ། །

[Block 4326]
དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 4327]
འདིར་གཞུང་ནི་བསླབ་པའི་གཞི་ལས།

[Block 4328]
དེ་དག་གིས་འཆག་པ༌[^3005]ཇི་ལྟ་བུ་མི༌[^3006]ཤེས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྤོང་བའི་ས་ནི་ཁྲུ་བཅོ་བརྒྱད་དོ། །

[Block 4329]
ཁ་ཏོན་བྱེད་པ་ནི་ཁྲུ་བཅུ་གཉིས་ཏེ། དེ་དག༌[^3007]ཐ་གུས་གཞལ་ཏེ་བཅག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4330]
ཐ་གུས་གཞལ་ཏེ་བྱའོ་ཞེས་བྱ་བ་ནི་རྒྱས་པ་ལས།

[Block 4331]
གཞན་འདིར་རང་དང་གཞན་དག་ལ་རིགས་དག་པ་གཞག་པ༌[^3008]རྣམ་པ་གང་ཞིག་ཆོས་བསྟན་པའོ། །

[Block 4332]
གསོ་སྦྱོང་གི་ཉི་མ་ལ་བྱ་བ་ཉིད་འདི་ལ་ཡོད་དེ་དེ་བས་ན༌[^3009]འདིར་གཏོགས་པའི་ཆོ་ག་བརྗོད་པར་བྱ་སྟེ། དགེ་སློང་གིས༌[^3010]ཆོས་བཤད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། འདི་ཐོག་མར་བྱས་པའི་ངག༌[^3011]ཅུང་ཟད་ཅེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 4333]
འདི་ཐོག་མ་ཞེས་བྱ་བ་ནི་རྒན་པོའི་མཐར་ཐུག་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 4334]
དེས་ཚེས་བཅོ་ལྔ་ཞེས་བྱ་བའི་མཐར་ཟླ་བ་ཕྱེད་པའི་རྣམ་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་དོར་བར་བྱའོ་ཞེས་བྱ་བའི་མཐར་ཡང་འདིར་གཞུང་ནི་རྣམ་པར༌[^3012]འབྱེད་པ་ལས།

[Block 4335]
འདིར་ཉར་བྱེད་པ་ཞེས་བྱ་བ་ཕྲན་ཚེགས་རྣམས་ལས་སོ། །

[Block 4336]
གལ་ཏེ་མ་བསྐུལ་བར་དེའི་སྒོ་ནས་ངེས་པར་འབྱུང་བ་མ་ཡིན་ཞེས་བྱ་བ་འདི༌[^3013]རབ་ཏུ་བྱུང་བའི་གཞི་ལས་སོ། །

[Block 4337]
འདིར་ལྷག་མ་གང་ཞིག་བྱེད་པ༌[^3014]མཚམས་སྦྱར་བ་མཐའི༌[^3015]རྣམ་པས་སོ། །

[Block 4338]
དེ་ལ་མ་མོ་འདུག་སྟེའོ། །

[Block 4339]
གལ་ཏེ་དུ་མ་ཉིད་ཡིན་ན་གཅིག་གིས་སོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཆོས་སྟོན་པ་དུ་མ་ཉིད་ཡོད་ན་འདི་པའི་དགེ་སློང་གི་འཁོར་དུ་གཏོགས་པ་རྣམས་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པའོ། །

[Block 4340]
ཆོས་འདི་པའི་རབ་ཏུ་བྱུང་བ་ཐམས་ཅད་ལ་མཚན་ཐ་དད་པ་ལ༌[^3016]ཡང་སྡོམ་པ་མཆོག་དང་མཆོག་མ་ཡིན་པ་ལ་ཆོས་འདི་པའི་དགེ་སྦྱོང་གི་འཁོར་དུ་གཏོགས་པ་ཞེས་བྱ་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 4341]
རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་མ་རྫོགས་པ་ལ་ཡང་ཆོ་ག་འདི་རྣམ་པར་གཞག་པའོ། །

[Block 4342]
གང་ཡང་རུང་བས་སོ་ཞེས་བྱ་བ་ནི་གསར་བུ་དང་། མཚན་མི་མཐུན་པ་དང་། རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་མ༌[^3017]རྫོགས་པ་དག་གིས་ཀྱང་བྱར་རུང་སྟེ། རྒན་པོ་འབའ་ཞིག་གིས་ནི་བྱ་བར་མ་ཟད་དེ་བསྙེན་པར༌[^3018]རྫོགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4343]
དེ་དག་གི་ནང་ན་ཆོས་སྟོན་པ་དུ་མ་ཡོད་དུ་ཟིན་ཀྱང་གང་ལ་སྟོན་པར་བྱེད་པ་ཐམས་ཅད་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4344]
མ་གསོལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བསྟན་པར་མི་བྱའོ། །

[Block 4345]
གལ་ཏེ་དེའི་ཚེ༌[^3019]ཚིག་གིས་བྱུང་བ་མ་ཡིན་ནའོ་ཞེས་བྱ་བ་ནི། གང་གི་ཚིག་གིས་དགེ་འདུན་སྤྱན་དྲངས་པ་ལ་སོགས་པ་མ༌[^3020]གསོལ་བར་ཡང་ཆོས་བསྟན་པར་བྱ་སྟེ། སྟོན་པ་དེ༌[^3021]བཞིན་དུ་འདིར་འདི་འབྱུང་བ་ཡིན་ཏེ། འདི་ལྟར་མདུན་གྱིས༌[^3022]བལྟས་པར་གྱུར་པས་མདུན་གྱིས་བལྟས་པ་ཉིད་དེ་དགེ་སློང་དེ་རྣམས་དང་མཐུན་པ་ཉིད་དོ། །
--- END BLOCKS ---
