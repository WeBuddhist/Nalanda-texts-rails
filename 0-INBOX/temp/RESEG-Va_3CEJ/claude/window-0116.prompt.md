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
[Block 4061]
དེ་ནས་ཞིང་རྣམས་བགོས་ཏེ་དེ༌[^2312]བདག་གིས༌[^2313]ནི་ཀུན་ཏུ་བཟུང་ནས་གཞན་གྱི་ལ་ནི་དབྲོག་པར་རྩོམ་སྟེ།[^2314] ཆོམ་རྐུན་གྱི་རྩོམ་པ་དང་པོ་ནི་དེ་ཡིན་ནོ། །

[Block 4062]
དེ་དག་གིས་དེ་དག་དགག་པའི་ཕྱིར་འདུས་ནས་མིའི་ཁྱད་པར་གང་ཡང་རུང་བ་ཞིག་ཞིང་རྣམས་སྲུང་བར་དྲུག་ཤས་བསྟབས་ཏེ། དེ་ལ་ཞིང་རྣམས་ཀྱི་དཔོན་པོ༌[^2315]རྒྱལ་རིགས་རྒྱལ་རིགས་ཞེས་བྱ་བའི་མིང་བྱུང་ངོ་། །སྐྱེ་བོའི་ཚོགས་ཕལ་པོ་ཆེས་བཀུར་བ་དང་། སྐྱེ་དགུ་ཡང་དགའ་བར་བྱེད་པས་རྒྱལ་པོ་མང་པོས་བཀུར་བ༌[^2316]ཞེས་བྱ་བའི་མིང་བྱུང་སྟེ། རྒྱལ་པོ་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་རྩོམ་པ་ནི་དེ་ཡིན་ནོ། །

[Block 4063]
དེ་ལ་གང་དག་ཁྱིམ་དག་ནས་ཡིད་ཕྱིར་ཕྱོགས་པ་དེ་དག་ལ་ནི་བྲམ་ཟེ་ཞེས་བྱ་བའི་མིང་བྱུང་ངོ་། །དེ་ནས་གང་ཡང་རུང་བའི་རྒྱལ་པོ་ཞིག་གིས་ཆགས་པས༌[^2317]སེམས་ཅན་རྣམས་ལ་མ་བགོས་པ་དང་རྐུན་པོ་མང་དུ་གྱུར་ཏེ། [^2318]དེ་དག་ལ་མཚོན་གྱིས་འདེབས་པར་གྱུར་ཏོ། །

[Block 4064]
དེ་ནས་གཞན་དག་ན་རེ་ཡང་བདག་ཅག་གིས་དེ་ལྟ་བུ་བགྱིས་པ་མ་མཆིས་སོ་ཞེས་བརྫུན་དུ་སྨྲ་བར་བརྩམས་སོ། །

[Block 4065 [VERSE]]
དེ་ནས་ལས་ཀྱི་ལམ་ལྷག་པས། །
ཚེ་ཐུང་ལོ་ནི་བཅུ་ཡིན་ནོ། །

[Block 4066]
དེ་ན༌[^2319]དེ་ལྟར་ལས་ཀྱི་ལམ་རྣམས་འཕེལ་བ་དང་མི་རྣམས་ཀྱི་ཚེ་ཁད་ཀྱིས་ཐུང་ངུར་གྱུར་ཏེ། ཐ་མར་མི་ཚེ་ལོ་བཅུ་པར་འགྱུར་རོ། །

[Block 4067]
དེའི་ཕྱིར་ཕུང་ཁྲོལ་གྱི་ཆུ་བོ་འདི་མཐའ་དག་གི་རྩ་བའི་སྐྱེ་གནས་ནི་ཆོས་གཉིས་ཏེ། རོ་ལ་ཆགས་པ་དང་། ལེ་ལོའོ། །

[Block 4068 [HEADING]]
##### བར་གྱི་བསྐལ་པ་ཚར་ཕྱིན་པ། ^3-2-5-10-0

[Block 4069 [HEADING]]
###### མཚོན། ^3-2-5-10-1-0

[Block 4070]
མི་རྣམས་ཀྱི་ཚེ་ལོ་བཅུ་པ་ན་བར་གྱི་བསྐལ་པ་ཚར་ཕྱིན་པ་ཡིན་ནོ། །ཇི་ལྟར་ཡིན་ཞེ་ན།

[Block 4071 [VERSE]]
བསྐལ་པ་མཚོན་དང་ནད་དང་ནི། །
མུ་གེ་དག་གིས་ཚར་ཕྱིན་ཏོ། །

[Block 4072]
བར་གྱི་བསྐལ་པ་ནི་མཚོན་དང་། ནད་དང་། མུ་གེ་དང་གསུམ་གྱིས་ཚར་ཕྱིན་ཏོ། །

[Block 4073]
བར་གྱི་བསྐལ་པ་ཚར་ཕྱིན་པའི་ཚེ་མི་རྣམས་ཚེ་ལོ༌[^2320]

[Block 4074]
བཅུ་པ་དང་། ཆོས་མ་ཡིན་པ་ལ་འདོད་ཆགས་ཀྱིས་ཆགས་པ་དང་། ཡ་ང་བ་ལ་ཆགས་པས༌[^2321]ཟིལ་གྱིས་ནོན་པ་དང་། ལོག་པའི་ཆོས་ཀྱིས་ཀུན་ནས་དཀྲིས་པར་འགྱུར་རོ། །

[Block 4075]
དེ་དག་གིས༌[^2322]གནོད་སེམས་ཡོངས་སུ༌[^2323]སྐྱེ་བར་འགྱུར་བ་ན་སེམས་ཅན༌[^2324]གཅིག་གིས་གཅིག་མཐོང་ན་དཔེར་ན་ད་ལྟར་རི་དགས་ཀྱི་རྔོན་པས་དགོན་པའི་རི་དགས་མཐོང་བ་བཞིན་དུ་གནོད་པ་མི་བཟད་པའི་སེམས་གནོད་པའི༌[^2325]སེམས་ཉེ་བར་གནས་པར་འགྱུར་ལ། དེ་དག་གིས་ཤིང་ངམ་ཐོང་བ་ཡང་རུང་གང་དང་གང་བླངས་པ་དེ༌[^2326]དག་གི་མཚོན་ཆ་རྣོན་པོ་འབྱུང་བར་འགྱུར་ཞིང་དེ་དག་གཅིག་ལ་གཅིག་སྲོག་གཅོད་པར་བྱེད་དོ། །

[Block 4076 [HEADING]]
###### ནད། ^3-2-5-10-2-0

[Block 4077]
ཡང་མི་ཚེ་ལོ་བཅུ་པ་རྣམས་ལ་བར་གྱི་བསྐལ་པ་ཚར་ཕྱིན་པའི་ཚེ་ཉེས་པ༌[^2327]དག་ཉིད་ཀྱིས༌[^2328]མི་མ་ཡིན་པ་རྣམས་ཀྱིས་ཡམས་ཀྱི་ནད་དག་གཏོང་བར་བྱེད་དོ། །

[Block 4078]
དེ་དག་ལ༌[^2329]གང་ལས་འཆི་བར་འགྱུར་ཞིང་གསོར་མི་རུང་བའི་ནད་དག་འབྱུང་བར་འགྱུར་རོ། །

[Block 4079 [HEADING]]
###### མུ་གེ། ^3-2-5-10-3-0

[Block 4080]
ཡང་མི་ཚེ་ལོ་བཅུ་པ་རྣམས་ལ་ཉེས་པ༌[^2330]དག་ཉིད་ཀྱིས༌[^2331]ལྷས་ཆར་པ་མི་འབེབས་ཏེ། དེས་ན་མུ་གེ་གབ་ཙེ༌[^2332]ཞེས་བྱ་བ་དང་། རུས་གོང་དཀར་པོ་ཞེས་བྱ་བ་དང་། ཐུར་མས་འཚོ་བ་ཞེས་བྱ་བའི་མུ་གེ་འབྱུང་བར་འགྱུར་རོ། །ཇི་ལྟར་གབ་ཙེ་ཡིན་ཞེ་ན། རྒྱུ་གཉིས་ཀྱིས་ཡིན་ཏེ། དེང་སང་འདུ་བ་གང་ཡིན་པ་དེ་ནི་དེའི་ཚེ་གབ་ཙེ་ཞེས་བྱ་བ། གབ་ཙེ་ལ་ཡང་གབ་ཙེ་ཞེས་བྱ་སྟེ། བཀྲེས་པ་དང་། ཉམ་ཆུང་བས་བཀྲེས་པའི་མི༌[^2333]དག་འདུ་ཞིང་འདུས་ནས་འཆི་བར་འགྱུར་བ་དང་། མ་འོངས་པའི་སྐྱེ་བོ་རྣམས་ལ་ཕན་གདགས་པའི་ཕྱིར་གབ་ཙེ་དག་གི་ནང་དུ་ས་བོན་དག་འཇོག་པར་བྱེད་དེ། དེའི་ཕྱིར་མུ་གེ་དེ་ནི་གབ་ཙེ་ཞེས་བྱའོ། །ཇི་ལྟར་ན༌[^2334]རུས་གོང་དཀར་པོ་ཡིན་ཞེ་ན། རྒྱུ་གཉིས་ཀྱིས་ཡིན་ཏེ། ལུས་སྐམས་ཤིང་རྩུབ་པོ་དེ་དག་ཤི་བ་དང་མྱུར་བ་ཁོ་ན༌[^2335]རུས་པ་དཀར་པོར་གྱུར་པ༌[^2336]དང་། བཀྲེས་པས་ཉེན་པ་དེ༌[^2337]རྣམས་ཀྱི་རུས་གོང་དཀར་པོ་དེ་དག་བསྡུས་ཏེ་བསྐོལ་ནས་འཐུང་བར་བྱེད་པའོ། ། ཇི་ལྟར་ན་ཐུར་མས་འཚོ་བ་ཡིན་ཞེ་ན། རྒྱུ་གཉིས་ཀྱིས་ཡིན་ཏེ། སེམས་ཅན་དེ་དག་ཐུར་མས་བསྒོ་བས་ཁྱིམ་དག་ཏུ་དེ་རིང་ནི་ཁྱིམ་བདག་ཟ་བའི་རེས་ལ་བབ་བོ། །

[Block 4081]
སང་ནི་ཁྱིམ་བདག་མོ་ཞེས་བྱ༌[^2338]དེ་ལྟ་བུ་ལ་སོགས་པས་ཟས་འགྱེད་པར་བྱེད་པ་དང་། འབྲུའི་གནས་ཀྱི་གསེབ་དག་ནས་འབྲུ་དག་ཐུར་མས་བྲུས་ཏེ། ཆུ་མང་པོར་བསྐོལ་ནས་བསྐོལ་བ་དེ་འཐུང་བར་བྱེད་དོ། །

[Block 4082]
འདི་སྐད་དུ་གང་གིས་ཉི་མ་འགའ་ཞིག་སྲོག་གཅོད་པ་སྤངས་པ་ལེགས་པར་བསྲུངས་པ༌[^2339]དང་། དགེ་འདུན་ལ་ཨ་རུ་ར་འགའ་དང་། བསོད་སྙོམས་འགའ་ཞིག་གུས་པར་བྱས་ཏེ། ཕུལ་བ་དེ་ནི་མཚོན་དང་། ནད་དང་། མུ་གེ་དང་། བར་གྱི་བསྐལ་པ་དེ་དག་ཏུ་སྐྱེ་བར་མི་འགྱུར་རོ་ཞེས་བརྗོད་དོ། །

[Block 4083]
ཡང་སེམས་ཅན་དེ་དག་ལ་མཚོན་གྱིས་གསོད་པ་དང་། ནད་དང་། མུ་གེ་དག་དུས་ཇི་སྲིད་དུ་འདུ༌[^2340]ཞེ་ན།

[Block 4084 [VERSE]]
ཞག་རྣམས་དང་ནི་ཟླ་བ་དང་། །
ལོ་བདུན་དག་ཏུ་གོ་རིམས་བཞིན། །

[Block 4085]
མཚོན་ཆས་གསོད་པ་ཞག་བདུན་དུ་འབྱུང་ངོ་། །ནད་ནི་ཟླ་བ་བདུན་དང་ཞག་བདུན་དུའོ།[^2341] །མུ་གེ་ནི་ལོ་བདུན་དང་ཟླ་བ་བདུན་དང༌[^2342]ཞག་བདུན་དུའོ། །

[Block 4086]
དང་ཞེས་བྱ་བ་ནི་བསྡུས་པའི་དོན་ཏོ། །

[Block 4087]
དེའི་ཚེ་ན་གླིང་གཉིས་སུ་ནི་དེ་དག་དང༌[^2343]འདྲ་བ་དག་འབྱུང་སྟེ། གནོད་སེམས་ལྷག་པར་འགྱུར་བ་ཡིན། །ཁ་དོག་ངན་པ་དང་། ཉམ་ཆུང་བ་དང་། བཀྲེས་པ་དང་སྐོམ་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 4088 [HEADING]]
##### མེ་དང་ཆུ་དང་རླུང་གིས་འཇིག་པ། ^3-2-5-11-0

[Block 4089]
དེ་བཞིན་དུ་འཇིག་པ་གཞན་དག༌[^2344]ལ་ཡང་ཅི་རིགས་པར༌[^2345]བྱའོ་ཞེས་གང་བཤད་པ་འཇུག་པ་དེ་དག་དུ་ཞེ་ན།

[Block 4090 [VERSE]]
མེ་དང་ཆུ་དང་རླུང་དག་གིས། །
འཇིག་པ་དག་ནི་ཡང་གསུམ་ཡིན། །

[Block 4091]
དེའི་ཚེ་སེམས་ཅན་རྣམས་བསམ་གཏན་གཅིག་ཏུ་འདུ་བས་ན་འཇིག་པ་ཡིན་ནོ། །

[Block 4092]
ཉི་མ་བདུན་གྱིས་ནི་མེས་འཇིག་པ་ཡིན་ནོ། །

[Block 4093]
ཆར་གྱི་ཆུས་ནི་ཆུས་འཇིག་པའོ།[^2346] །རླུང་རབ་ཏུ་འཁྲུགས་པས་ནི་རླུང་གིས་འཇིག་པ་ཡིན་ཏེ། དེ་དག་གིས་ནི་སྣོད་རྣམས་ཀྱི་ཆ་ཤས་ཕྲ་མོ་ཡང་མི༌[^2347]ལུས་པར་བྱེད་དོ། །

[Block 4094]
འདི་ལ་མུ་སྟེགས་བྱེད་ཁ་ཅིག་ནི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་རྟག་པ་ཡིན་པས་དེའི་ཚེ་དེ་དག་ལུས་སོ་ཞེས་བྱ་བར་འདོད་དོ། །

[Block 4095]
དེ་དག་ཅིའི་ཕྱིར་དེ་ལྟར་འདོད་ཅེ་ན། རགས་པ་རྣམས་རྒྱུ་མེད་པ་ཅན་དུ་འབྱུང་བར་འགྱུར་ན་མི་རུང་ངོ་སྙམ་མོ། །

[Block 4096]
སེམས་ཅན་རྣམས་ཀྱི་ལས་ལས་སྐྱེས་པའི་མཐུའི་བྱེ་བྲག་ཅན་གྱིས་རླུང་གི༌[^2348]ས་བོན་ཡིན་ནོ་ཞེས་མ་བཤད་དམ། ཡང་ན་འཇིག་པའི་རླུང་གི་རྩེ་མོ་ནི་དེའི་ཕྱིར༌[^2349]རྒྱུ་ཡིན་པར་འགྱུར་རོ། །

[Block 4097]
ས་སྟོན་པའི་སྡེའི་མདོ་ལས་ནི་རླུང་གིས་འཇིག་རྟེན་གྱི་ཁམས་གཞན་དག་ནས་ས་བོན་དག་ཁྱེར་ཏེ་འོང་ངོ༌[^2350]ཞེས་འབྱུང་ངོ་། །དེ་ལྟར༌[^2351]ཡིན་ཡང་དེ་དག་ས་བོན་ལ་སོགས་པ་ལས་མྱུ་གུ་ལ་སོགས་པ་སྐྱེ་བར་ནི་མི་འདོད་དོ། །

[Block 4098]
འོ་ན་ཇི༌[^2352]ཞེ་ན། རང་གི་ཡན་ལག་དག་ཁོ་ན་ལས་སྐྱེ་བ༌[^2353]ལ། དེ་དག་ཀྱང་རང་གི་ཁོ་ན་དག་ལས་སྐྱེ་སྟེ། རྡུལ་ཕྲ་རབ་དག་ལས་སྐྱེ་བའི༌[^2354]བར་དུ་ཡང་དེ་དང་འདྲའོ་ཞེས་སོ།

[Block 4099]
[^2355] །ད་ནི་མྱུ་གུ་ལ་སོགས་པ་དག་ལས་ས་བོན་ལ་སོགས་པའི་ནུས་པ་ཅི་ཞིག་ཡོད་ཅེ་ན། དེའི་རྡུལ་ཕྲ་རབ་རྣམས་ཕྲད་པ་ལས་མ་གཏོགས་པར་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 4100]
ཡང་ཅིའི་ཕྱིར་དེ་དག་དེ་ལྟར་འདོད་ཅེ་ན། རིགས་མི་མཐུན་པ་ལས་སྐྱེ་བར་ནི་རིགས་པ་མ་ཡིན་ནོ་སྙམ་མོ། །ཅིའི་ཕྱིར་མི་རིགས་ཤེ་ན། ངེས་པ་མེད་པར་འགྱུར་རོ། །
--- END BLOCKS ---
