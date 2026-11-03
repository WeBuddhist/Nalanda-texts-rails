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
[Block 4376]
དེ་སྨྲ་བའི་ཕྱིར་གསོལ་བ་འདེབས་པ་མི་གདོན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་ཆོས་མཉན་པའི་ཕྱིར་ཆོས་ལའོ། །

[Block 4377]
མི་ནུས་པ་ལ་སོགས་པ་ཡིན་ན༌[^3058]གསོལ་བ་འདེབས་པ་ལ་ཤད་ཀྱིས་སྦྱང་བར་བྱའོ་ཞེས་བྱ་བ་ནི། ན་སྟེ་མི་ནུས་པའམ་བྱ་བ་གཞན་གྱིས་བྲེལ་བར་གྱུར་པ་ཡིན་ན་བྱ་བ་གཞན་ལ་རྩེ་གཅིག་པ་ལ་སོགས་པ་མ་ཡིན་པ་ལ་ནི་སོགས་པའི་སྒྲས་དྲངས༌[^3059]པའོ། །

[Block 4378]
སྨྲ་བ་པོ་མེད་ན་རིམ་གྱིས་དྲན་པར་བྱ་ཞིང་ཐ་ན་ཚིགས་སུ་བཅད་པ་རེ་རེ་ཙམ་ཡང་སྨྲ་བར་བྱའོ། །

[Block 4379]
དེར་མར་མེ་གཟུགས་སོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་ཆོས་ཉན་ས་དེར་རོ། །

[Block 4380]
ཁྱམས་སུ་ཆོས་མཉན་པའི་གྲལ་ནི་ཟླ་ཁམ་གྱི་རྣམ་པ་ལྟ་བུའམ་རྫིང་བུའི་རྣམ་པ་ལྟ་བུར༌[^3060]བཤམ་པར་བྱའོ་ཞེས་བྱ་བ་ནི། འདིར་དེའི་དོན་ནི་ཐུན་མོང་དུ་དཔེ་ཙམ་དུ་ཟད་དེ་མི་གནོད་པ་གཞན་དག་ཀྱང་རུང་སྟེ། དེ་བས་ན་ངེས་པ་མེད་དོ། །

[Block 4381]
བླ་གབ་མེད་པར་ཆོས་ཉན་ན་བླ་རེ༌[^3061]གདགས་སོ། །

[Block 4382]
རླུང་དང་ཆར་འབབ་ན་བརྟུལ༌[^3062]ལོ་ཞེས་བྱ་བ་ནི་བླ་རེའོ། །

[Block 4383]
དེར་ཆོས་ཉན་པ་དག་དོར་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་རླུང་དང་ཆར་འབབ་པ་དེར་རོ། །

[Block 4384]
དེར་གནས་བརྟན་དང་པོར་འདུག་སྟེ་ཡུད་ཙམ་ཞིག་ཀྱང༌[^3063]མི་སྨྲ་བར་བསྡད་ནས་ཆོས་སྨྲ་བར་བྱ་བའམ༌[^3064]གཞན་ལ་དགེ་སློང་ཆོས་སྨྲོས་ཤིག་ཅེས་གསོལ་བ་བྱའོ་ཞེས་བྱ་བ་ལ། གནས་བརྟན་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་གནས་བརྟན་ནོ། །

[Block 4385]
འདིར་མི་སྨྲ་བར་བསྡད་ནས་ཞེས་བྱ་བ་ནི་ཀུ་ཅོ་སྤང་བའི་དོན་དུའོ།[^3065] །

[Block 4386]
དང་པོ་འདུག་སྟེ་ཞེས་བྱ་བ་ནི་ཆོས་ཉན་དུ་གཞུག་པར་རྩོམ་པའི་དང་པོར་རོ། །

[Block 4387]
དེར་ཞེས་བྱ་བ་ནི་ཆོས་ཉན་པ་ལའོ། །

[Block 4388]
གསོལ་བ་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་བརྟན་གྱིས་ཆོས་སྟོན་པ་པོ་ལ་ཆོས་བསྟན་པར་གསོལ་བ་གདབ་ཅིང་གཞན་ཆོས་སྨྲར་གཞུག་པར་བྱའོ། །

[Block 4389]
སྨྲ་བ༌[^3066]ན་སེམས་གཏད་དེ་ཆོས་ཡིན་ན་སྤྲོ་བར་བྱའོ། །

[Block 4390]
གལ་ཏེ་མ་ཡིན་ན་བཟློག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། སེམས་གཏད་དེ་ཞེས་བྱ་བ་ནི་སེམས་གཏོད་དུ་གཞུག་པའོ། །

[Block 4391]
གལ་ཏེ་ཆོས་ཡིན་ན་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཆོས་སྨྲས་པ༌[^3067]ཡིན་ནའོ། །

[Block 4392]
དེར་ཁྱིམ་པ་ལྷགས་པ་རྣམས་ལ་ཆོས་དང་ལྡན་པའི་གཏམ་བྱའོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་ཆོས་ཉན་པ་དེ་ལའོ། །

[Block 4393]
ཆོས་ཉན་པའི་མཐར་ཐུག་པ་ལ་འགོར་བར་གྱུར་ན་རྩོམ་པ་ལ་ཤུགས་ཀྱིས་བསྒྲུབ་པར་བྱའོ། །

[Block 4394]
མུ་སྟེགས་ཅན་ཀླན༌[^3068]ཀ་ཚོལ་ཞིང་གནས་ན་ལེགས་པར་ཚར་བཅད་ཅིང་ཁྲོ་བ་མི་བསྟན་པར་བཟོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། གནས་བརྟན་གྱིས་ཞེས་བྱ་བར་སྦྱར་རོ། །གང་དུ་འདིར་བཟོད་པར་བྱ༌[^3069]ཞེ་ན། དེའི་ཕྱིར་སྟོན་པས་འཁོར་ཁྲིད་དེ་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ཚུར་ཤོག་བདག་གིས་བསྟན་པར་བྱའོ་ཞེས་བྱ་བའོ།

[Block 4395]
[^3070] །སྟོན་པས་ཞེས་བྱ་བ་ནི་གནས་བརྟན་གྱི༌[^3071]དབང་དུ་བྱས་པ་ལ་དེ་དག་བཟློག་པ་པོར་རིག་པར་བྱའོ། །

[Block 4396]
དེ་དག་འགྲོ་ན་ཆོས་ཀྱི་སྒོར་གཟུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི། དེ་ཚོལ་བས་གཞག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4397]
རྗེ་ས་དང་བཅས་པ་དང་། གུས་པ་དང་བཅས་པ་དང་སེམས་དམའ་བས་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི། འཁོར་ལ་ཞེས་བྱ་བ་དབང་དུ་བྱ་བར་གཏོགས་པ་སྟེ། རྗེ་ས་དང་བཅས་པ་དང་གུས་པ་དང་བཅས་པ་དང་སེམས་དམའ་བས་སོ། །

[Block 4398]
གུས་པར་བྱ་སྟེ་བསྟན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་ལ་འཇིགས་པའི་གནས་ཉིད་དུ་ལྟ༌[^3072]བའོ། །

[Block 4399]
སེམས་དམའ་བ་ཞེས་བྱ་བ་ནི་རྒྱགས་པ་དང་ང་རྒྱལ་ངེས་པར་བཅོམ་པ་ཉིད་ཀྱིས་སོ། །

[Block 4400]
གུས་པར་བྱ་སྟེ་བརྟན་པར༌[^3073]བྱའོ་ཞེས་བྱ་བ་ནི། ཆོས་ལ་གུས་པ་དང་བཅས་པ་དང་བརྟན་པ༌[^3074]དང་ཡིད་མི་གཡེང་བས་རིགས་པ་དང་གྲོལ་བའི་ཚིག་དག་གིས་སོ། །

[Block 4401]
དོན་ཇི་ལྟ་བ་བཞིན་དུ་ཐོགས་པ་མེད་པར་བརྗོད་པ་དག་གིས་སོ། །

[Block 4402]
མ་འདྲེས་པར་རོ་ཞེས་བྱ་བ་ནི་གཏམ་གཞན་དང་མ་འདྲེས་པར་རོ། །

[Block 4403]
འབྲེལ་པར་རོ་ཞེས་བྱ་བ་ནི། ཚིག་སྔ་མའི་དོན་དང་ཚིག་ཕྱི༌[^3075]མའི་དོན་འབྲེལ་བ་དང་བཅས་ཤིང་སྐབས་སུ་བར་མ་ཆད་པར་ཕ་རོལ་གྱི་ངག་གིས་སྦྱོར་བས་སོ། །

[Block 4404]
བྱམས་པ་དང་སྙིང་རྗེ་དང་ཟང་ཟིང་མེད་པའི་སེམས་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི། བྱམས་པའི་སེམས་དང་སྙིང་རྗེའི་སེམས་དང་ཟང་ཟིང་མེད་པའི་སེམས་ཀྱིས་སོ། །

[Block 4405]
བྱམས་པའི་སེམས་ཞེས་བྱ་བ་ནི། འཇམ་པའི་སེམས་དང་ཁོང་ཁྲོ་བ་དང་བྲལ་ཞིང་མཛའ་བཤེས་དང་ལྡན་པའི་སེམས་ཀྱིས་སོ། །

[Block 4406]
སྙིང་རྗེའི་སེམས་ཀྱིས་ཞེས་བྱ་བ་ནི། ཕན་པ་ཉེ་བར་བསྒྲུབ་པར་འདོད་པས་དམ་པ་སྔོན་དུ་བཏང་བས་སོ། །

[Block 4407]
ཟང་ཟིང་མེད་པའི་སེམས་ཀྱིས་ཞེས་བྱ་བ་ནི། སོ་སོར་བསྔགས་པ་བཞིན་དེའི་རྒྱུས་དེ་ལས་སམ་གཞན་ལ་རྙེད་པ་དང་བཀུར་སྟི་དང་རིམ་གྲོའམ་བྱ་བ་གཞན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4408]
རངས་པ་དང་མོས་པ་དང་དགའ་བར་བྱེད་པས་སོ་ཞེས་བྱ་བ་ནི་ཞུམ་པ་དང་ལྷག་པར་མི་མོས་པས་མི་རིགས་པར་བྱེད་པ་ཉིད་ཀྱི་གཉེན་པོས་སོ། །

[Block 4409]
དོན་གྱི་དབང་གིས་མ་རྫོགས་ན་གཞག༌[^3076]པར་བྱའོ་ཞེས་བྱ་བ་ནི། མ༌[^3077]ནུས་པ་ལ་སོགས་པ་སྟེ་དེའི་དབང་གིས་སོ། །

[Block 4410]
འདི་ལ་མི་རིགས་པ་མེད་པར་ཤེས་པར་བྱའོ། །

[Block 4411]
དེ་བས་ན་འདི་དང་མདོ་ཕྱི་མ་དང་ཡང་དག་པར་བསྟན་པའོ། །

[Block 4412]
དབྱངས་ཀྱིས་ཆོས་སྨྲ་བར་བྱའོ། །

[Block 4413]
ལངས་ནས་རྣམ་པར་དབྱེ་བར་བྱའོ། །

[Block 4414]
[^3078]དོན་བསྡུས་ཏེ་བརྗོད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་བར་བྱའོ། །

[Block 4415]
ཆོས་ལ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ༌[^3079]ལ་སོགས་པ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །
--- END BLOCKS ---
