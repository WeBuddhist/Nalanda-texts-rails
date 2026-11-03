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
[Block 4201]
ལས་བྱེད་པས་ནི་སེམས་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་འཇུག་པ་ཉིད་ན་ལྟུང་བ་དྲན་ནམ། ཡིད་གཉིས་ཟ་ན་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4202]
ལས་བྱེད་པ་པོ་གང་ཞིག་དྲན་ནམ་དེ་ལ་ཡིད་གཉིས་ཟ་ན་ལྟུང་བྱེད་ཡུལ་དེས་དེ་རང་གི་སེམས་ཀྱིས་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4203]
འདིར་དུས་རིང་དུ་འདའ་བར་བྱེད་པ་ནི་མ་གུས་པ་སྐྱེས༌[^2906]པ་ཡིན་ཏེ། དེ་བས་ན་ལན་ཅིག་ཁོ་ནས་བྱིན་གྱིས་བརླབ་པ་ཡིན་གྱི་ལན་གསུམ་དུ་ནི་མ་ཡིན་ནོ། །

[Block 4204]
གལ་ཏེ་ཚེས་བཅོ་ལྔ་ལ་བདག་གཅིག་པུ་དེ་དང་མི་ལྡན་པར་ཤེས་ན་འགྲོགས་བཤེས་ལ་དྲང་པོར་འབད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་དགེ་སློང་གིས་གསོ་སྦྱོང་གི་ཉི་མ་བདག་གཅིག་པུ་ལྟུང་བ་དེ་དང་མི་ལྡན་ཞིང་། དགེ་འདུན་ཐམས་ཅད་ལྟུང་བ་མཐུན་པ་དང་ལྡན་པར་ཤེས་ན། གང་ཞིག་ཚེས་བཅོ་ལྔ་ལ་དགེ་འདུན་ཐམས་ཅད་ལྟུང་བ་མེད་པར་བསམ་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4205]
བཅོ་ལྔ་པ་ཁོ་ན་གསོ་སྦྱོང་བཅུ་བཞི་པ་ཞེས་བྱ་བར་གཟུང་བར༌[^2907]བྱ་བ་མ་ཡིན་པ་འདིར་སྒྲ་གཞན་གྱིས་འདིར་གསོ་སྦྱོང་དག་དང་། དགག་དབྱེའི་བར་ཆད་བསལ་བར་བྱ་བའི་སྐབས་ཀྱིས་འདིར་སྨོས་ཀྱི། དུས་གཞན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4206]
འདི་ལ་བྱ་བ་མ་ཡིན་པ་ཉིད་ན། ཇི་ལྟར་འབད་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཚེ་དང་ལྡན་པ་འདི་དང་འདི་ལྟར་བྱེད་པ་གང་ཡིན་པ་དེས་ཅིར་འགྱུར། ལྟུང་བ་དང་བཅས་པར་རོ། །

[Block 4207]
འོ་ན་ཚེ་དང་ལྡན་པས་ཀྱང་འདི་དང་འདི་ལྟར་བྱས་སམ་བྱས་སོ། །

[Block 4208]
འོ་ན་ཚེ་དང་ལྡན་པ་ཡང་ལྟུང་བ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 4209]
ཚེ་དང་ལྡན་པ་ཁོ་བོ་གཅིག་པུར་མ་ཟད་ཀྱི། དགེ་འདུན་ཐམས་ཅད་དོན་དེ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 4210]
ཀྱེ་ཚེ་དང་ལྡན་པ་ཇེ༌[^2908]ཁྱོད་རང་གི་ལྟུང་བ་ཆོས་བཞིན་དུ་ཕྱིར་གྱིས་ཤིག །དགེ་འདུན་ཐམས་ཅད་ཀྱིས༌[^2909]ཁྱེད་ལ་ཅི་འགྱུར་ཞེས་བྱ་བའི་རྩོམ་པས༌[^2910]མིག་ལམ་དུ་ལྷག་མ་འདོད་པ་རྣམས་འཆགས་སུ་གཞུག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྩོམ་པ་ཞེས་བྱ་བའི་ཚིག་འདི་དང་གཞན་རྣམས་ཐམས་ཅད་ཀྱིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4211]
འདི་ལ་མི་འདོད་པ༌[^2911]དེ་ལ་གླེང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་ལའོ། །

[Block 4212]
དེ་ལ་ཞེས་བྱ་བ་ནི་མཉེས་གཤིན་པ་དང་བཅས་པ་དེ་ལའོ། །

[Block 4213]
གསོ་སྦྱོང་དང་དགག་དབྱེའི་བར་ཆད་སྤང་བར་བྱ་བའི་ཕྱིར་བཀག་པ་ཡིན་ནོ། །

[Block 4214]
འོ་ན་གལ་ཏེ། འདི་ལྟར་དྲན་དུ་བཅུག་པ་མི་འདོད་ན་འདི་གསོ་སྦྱོང་ངམ། དགག་དབྱེ་མ་དག་པར་འགྱུར་རོ། །

[Block 4215]
དག་པ་རྣམས་ཀྱིས་ལས་རྣམས་ཉམས་སུ་མྱོང་བ་ལ་ཉེས་བྱས་གང་ཡིན་པ་དེ་ཇི་ལྟར་མི་འགྲུབ༌[^2912]ཅེས་བྱའོ། །

[Block 4216]
དེའི་ཕྱིར་མི་འདོད་པ་ཞེས་བྱ་བ་དམིགས་ཀྱིས་བསལ་བར་གྱུར་པའི་ཚིག་ལས་མ་གྲུབ་པ་ཡིན་ནོ། །

[Block 4217]
གལ་ཏེ་ཚེས་བཅོ་ལྔ་ལ་ཐམས་ཅད་ཀྱིས་ལྟུང་བ་ཤེས་སམ། ཡིད་གཉིས་སུ་གྱུར་ན་ལེན་པར་བྱེད་པ་བསྒྲུབ་པའི་ཕྱིར་དགེ་སློང་འགའ་ཞིག་ལ་ཕྱིར་བཅོས་པའི་དོན་དུ་གནས་གཞན་དུ་གཏང་བར༌[^2913]བྱའོ་ཞེས་བྱ་བ་ལ། རང་ཞེས་བྱ་བ་ནི་འདིར་བཞག་བཞིན་པའི་ཚིག་བླ་དགས་སོ། །

[Block 4218]
ལེན་པ་བྱེད་པ་བསྒྲུབ་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི། གང་དེ་རྣམས་ཀྱི་ལྟུང་བ་བསྟན་པ་དེ་ལེན་པར་བྱེད་པའི་དོན་དུའོ། །

[Block 4219]
གང་གི་ཕྱིར་དོན་འདི་ལྟར་བསྒྲུབ་པར་འགྱུར་རོ། །

[Block 4220]
མ་གྲུབ་ན་བྱིན་གྱིས་བརླབ་པའི་ཕྱིར། གསོལ་བ་བྱ་བ་འདོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། མ་གྲུབ་ན་ཞེས་བྱ་བ་ལ་ནི་ཆོ་ག་འདིའོ། །

[Block 4221]
ཇི་སྐད་དུ་བསྟན་པའི་ཆོ་ག་དེ་དགེ་སློང་གི་དགེ་འདུན་གྱིས་གསོལ་བས་ལྟུང་བ་བྱིན་གྱིས་བརླབས༌[^2914]ལ་གསོ་སྦྱོང་ངམ་དགག་དབྱེའི་ལས་མི་ཤོལ་བར་བྱའོ། །

[Block 4222]
གསོལ་བ་བྱ་བ་འདོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། སོ་སོར་བྱིན་གྱིས་བརླབ་པས་འདི་ལ་དག་པ་མི་འགྲུབ༌[^2915]པ་མ༌[^2916]ཡིན་ནོ། །

[Block 4223]
དེ་འདིར་བརྗོད་པར་མི་བྱ་ཞེས་བྱ་བ་འདིར་རྣམ་པ་འདི་ལ་བརྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་བསྟན་པའི་དོན་དུ་དེ་སྐད་བརྗོད་པའོ། །

[Block 4224]
བཞི་པས་ཉུང་བ་ཉིད་ལ་ཡང་གཙུག་ལག་ཁང་གི་བྱ་བ་གནས་པ་ཁོ་ན་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། [^2917]གཙུག་ལག་ཁང་གཅིག་ན། དགེ་སློང་གསུམ་མམ། གཉིས་སམ་གཅིག་ཁོ་ན་འདུག་ན་ཡང་དེས་ཕྱག་དར་ལ་སོགས་པ་གཙུག་ལག་ཁང་གི་བྱ་བ་གདོན་མི་ཟ་བར་བྱ་དགོས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4225]
འདུག་པ་པོ་རྣམས་ཀྱི་དོན་དུ་སྟན་རྣམས་གནང་བ་དེ་མེད་པས། དེའི་ཚེ་གཙུག་ལག་ཁང་གི་བྱ་བ་མ་ཡིན་སྙམ་པའི་དོགས་པ་བསལ་བའི་ཕྱིར། སྟན་ཐབས་ཉམས་པར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་འོངས༌[^2918]སྲིད་པས་དེའི་དོན་དུ་མེད་པར་བརྟེན་པར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བའི་བློ་གྲོས་སོ། །

[Block 4226]
ཆག་ཆག་དང་། ཕྱག་དར་དང་། ལྕི་བ་སར་པས་བྱུག་པ་བྱ་བ་དང་། སེང་གེའི་ཁྲི་བཤམ་པ་དང་། མར་མེ་གཟུགས་པ་དང་ཆོས་ཉན་དུ་གཞུག་པ་དག་བྱས་ལ་ཕྱོགས་ཆེས་མཐོན་པོར་འདུག་སྟེ། ཕྱོགས་བཞིར་རྣམ་པར་བལྟ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། འདི་ལྟར་ལྟ་བར་བྱེད་པ་རྣམས་ཀྱིས་བལྟ་བར་བྱ་སྟེ། གོ་རིམས་བསྟན་པའི་དོན་དུ་དེ་ལྟར་བསམས་པའོ། །

[Block 4227]
དགེ་སློང་དག་འོང་བ་སྣང་ན། ཀྱེ་ཚེ་དང་ལྡན་པ་མྱུར་བ་མྱུར་བར་ཤོག་ཤིག༌[^2919]དེང་དགེ་འདུན་གྱིས་གསོ་སྦྱོང་ངམ། དགག་དབྱེ་བཅོ་ལྔ་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དགག་དབྱེ་ལ་བཅོ་ལྔ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 4228]
འདི་ནི་མཚོན་པ་ཙམ་ཡིན་ཏེ། གསོ་སྦྱོང་བཅུ་བཞི་པ་དེ་བས་ན་འདི་ལ་མི་བྱ་བ་ཉིད་དུ་ཤེས་པར་མི་བྱའོ། །

[Block 4229]
བཞིར་མ་ཚང་ན་དུས་ཀྱི་བར་དུ་བསྡད་དེ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི། དགེ་སློང་བཞིར་མ་ཚང་ན། སྐྱ་རེངས་མ་ཤར་ཚུན་ཆད་དུ་བསྡད་དེ། དུས་སུ་མ་འོངས་ན་གསོ་སྦྱོང་དང་དགག་དབྱེ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4230]
འདི་ནི་མ་མོ་ལས་སོ། །

[Block 4231]
འབའ་ཞིག་ན་འདུག་སྟེའོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་གཅིག་པུ་འདུག་ན་སྟན་དེ་ལ་འདུག་སྟེ། དེས་གསོ་སྦྱོང་དང་དགག་དབྱེ་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 4232]
ལྷག་མ་གཞན་དང་བཅས་པ་ཉིད་ཡིན་ན་མདུན་དུའོ་ཞེས་བྱ་བ་ནི། གཞན་དང་བཅས་པ་ནི་གཞན་དང་ལྷན་ཅིག་གོ། །

[Block 4233]
གལ་ཏེ་གཉིས་པ་ཡོད་པར་གྱུར་ན་དེའི་མདུན་དུ་ཙོག་ཙོག་པོར་འདུག་སྟེ། གསོ་སྦྱོང་དང་དགག་དབྱེ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ངེས་པ་ལ་གཏོགས་པའོ། །

[Block 4234]
གསུམ་པ་ལ་ནི་རྣམ་པ་གཞན་དུ་བསྟན་པའི་ཕྱིར་གསུམ་ནི་འཁོད་དེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་ལྟར་དགེ་འདུན་གྲལ་རིམས༌[^2920]བཞིན་དུ་འཁོད་དེ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4235]
བཞིའི་དགག་དབྱེ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི། ཇི་ལྟར་དགེ་སློང་གསུམ་གྱིས་གསོ་སྦྱོང་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་བཞིན་དུ་བཞིའི༌[^2921]ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4236]
དེའི་ཚེ་གནས་ན་སོ་སོར་ཐར་པའི་མདོ་གདོན༌[^2922]ནུས་པ་མེད་པར་ཤེས་ན་གསོ་སྦྱོང་ལ་བསྡད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་ཚེ་ཞེས་བྱ་བ་ལ་ནི་གསོ་སྦྱོང་ལ་ལྟོས་པའི་གསོ་སྦྱོང་གི་དུས་ལ་གང་དུ་སྟོན་པ་པོ་མེད་པར་གྱུར་ན་ཞེས་བྱའོ། །

[Block 4237]
གང་ན༌[^2923]དེ་ལས་འདའ་བར༌[^2924]དེར་ཉེ་བར་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལས་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་ལའོ། །

[Block 4238]
མདོ་འདོན་ནུས་པ་མེད་པ་ལ་ནི་འདི་སྨོས་སོ། །

[Block 4239]
ཚོགས་པ་མེད་པ་ལ་ཡང་དེ་ཉིད་ཀྱི་ཕྱིར་འདིའི་ལྟུང་བ་སྟེ།[^2925] བར་ཆད་གཞན་གྱིས་བསྟན་པ་མེད་པ་ལ་དེ་བས་ན་འདི་ལྟར་བྱའོ། །

[Block 4240]
གནས་པར༌[^2926]ཁས་བླངས་པ་ཕྱི་མའི་གོང་མ་བསྲུང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ཁས་བླངས་པ་ཕྱི་མ་ཤོས་ཀྱིས་སྔ་མ་དེ་བསྲུང་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
