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
[Block 4271]
སོར་བཞི་དྲུག་ལ་ཁྲུ་གང་ངོ་། །ཁྲུ་ཕྱེད་དང་བཞི་ལ་ནི་མིའི་སྲིད་དོ། །

[Block 4272]
ཁྲུ་བཞི་ལ་གཞུ་གང་ངོ་། །དེ་ལྔ་བརྒྱ་ལ་རྒྱང་གྲགས་སོ་ཞེས་བྱ་བ་ནི་ནས་འབྲུ་དྲུག་གློས་གཞིབས་པ༌[^2908]ལ་སོར་གཅིག་ཏུ་རིག་པར་བྱ་སྟེ། འདིར་གཞུང་ནི་ནས་དྲུག་ལ་སོར་མོའི་ཚིགས་གཅིག་གོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4273]
སོར་མོ་གང་ཡིན་པའི་ཚིགས་ཀྱི་ཚིགས་ལ་ཞེས་བྱ་བ་ནི་འདི༌[^2909]བསྟན་པའི་དོན་དུ་འདིར་ཚིགས་ཀྱི་ཚིགས་རིག་པར༌[^2910]བྱའོ། །

[Block 4274]
འཇིགས་པ་དང་བཅས་པ་ཉིད་དུ་ནགས་ཁྲོད་དགོན་པ་བསྟེན་པ་ལ་དགེ་སློང་མས་དགོན་པར་གནས་པར་མི་བྱ་བ་གསུངས་པས་མངོན་པར་བསྟེན་པར་བྱ་བའི་དགོན་པའི་ངོ་བོ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དགོན་པའི་དང་པོ་ནི་དེའི་མཐའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྒྱང་གྲགས་ཀྱི་མཐར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4275]
ལུས་ཀྱིས༌[^2911]ཁུར་མི་བསྐུར༌[^2912]རོ་ཞེས་བྱ་བ་ལ་ལུས་ཀྱི་ཁུར་ཞེས་བྱ་བ་ཕྲག་གདང་གི་ཁུར་ལ་བྱ་སྟེ། ཕྲག་གདང་གིས༌[^2913]ཁུར་བསྐུར་བར༌[^2914]མི་བྱའོ། །

[Block 4276]
གློ་དང་རྒྱབ་དང་རྐེད་པ་དང་། མགོ་བོ་དག་གིས་མི་བསྐུར༌[^2915]རོ་ཞེས་བྱ་བར་རོ། །

[Block 4277]
ཁུར་བསྐུར་བ༌[^2916]ཐམས་ཅད་ལ་ནི་འདི་རྣམས་ཉིད་བཀག་པའོ། །

[Block 4278]
འདིར་ཐུན་མོང་མ་ཡིན་པ་ཉིད་དུ་དོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལུས་ཀྱིས༌[^2917]མི་བསྐུར༌[^2918]ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དགེ་སློང་མ་རྣམས་ཀྱིས་ཐུན་མོང་བ༌[^2919]ཡིན་པ་ཉིད་དུ་དོགས་པར༌[^2920]མི་བྱ་སྟེ། དགེ་སློང་མ་རྣམས་ཀྱིས་ཀྱང་འདི་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4279]
ཁུར་ཕྱེད་ལས༌[^2921]ལྷག་པ་བསྐུར་བར༌[^2922]མི་བྱའོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་མི་ཁུར་གང་ཡིན་དེ༌[^2923]དགེ་སློང་གཉིས་ཀྱིས་བསྐུར་བར༌[^2924]བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4280]
བལ་ཐོགས་པའི་སྤང་བའོ།། །།

[Block 4281]
འཁྲུར་འཇུག་པའི་སྤང་བ་ལ་ཚོག་གང་ཡིན་པ་དེ་ཉིད་ལས་བལ་རྨེལ་དུ་འཇུག་པའི་སྤང་བ་ལ་བརྟེན་ནས་བྱེ་བྲག་བརྗོད་པར་བྱ་སྟེ། ཆོས་གོས་རྙིང་པའི་གནས་སུ་ལུག་གི་བལ་དག་གོ། །

[Block 4282]
འཆག་པར་རྨེལ་བའོ་ཞེས་བྱ་བ་ནི་གནས་སུ་ཞེས་བྱ་བ་ཉིད་དུ་འཁྲུར་འཇུག་པའི་སྤང་བའི་སྐབས་སུ་འཁྲུར་འཇུག་པ་འམ་འཚེད་དུ་འཇུག༌[^2925]ནའོ་ཞེས་བྱ་བ་སྨོས་པ་དེ་འདིར་ནི་འཁྲུར་འཇུག་གམ་འཚེད་དུ་འཇུག་གམ་རྨེལ་དུ་བཅུག་ནའོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 4283]
གང་གི་ཕྱིར་དེ་ཉིད་འདིར་རྫོགས་པ་ནི་ལྟུང་བའི་བྱེད་པ་པོའི་གཞུང་ངོ་། །བལ་རྨེལ་དུ་འཇུག་པའི་སྤང་བའོ།། །།

[Block 4284]
ཅི་ཞིག་བྱས་ན་གསེར་དངུལ་ལ་རེག་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རིན་པོ་ཆེ་བདག་གིར་བྱས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་རྐང་པའི་དྲུང་ན་མོའི་རོ་མྱང་ངམ་ཐོབ་པའི་གནས་སམ་ས་ལེ་སྦྲམ་གྱི་རྫས་འདུག་པ་བདག་གིར་བྱེད་ན་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4285]
ལྕོགས་པ་ཉིད་ན་དེ་རྫོགས་སོ་ཞེས་བྱ་བ་ནི་ལྕོགས་པ་ཉིད་དུ་བདག་གིར་བྱ་བར་ནུས་པ་ཉིད་ལ་ཐོབ་པ་ལག་ཏུ་འོང་བར་རུང་བ་ཉིད་ལ་ལག་ཏུ་གྱུར་པ་མ་ཡིན་པ་ཉིད་ལ་སྟོན་པ་ན་བདག་གིར་བྱ་བ་དེ་ཡོངས་སུ་རྫོགས་པ་ཡིན་ནོ། །

[Block 4286]
དེ་བས་ཕ་ཟད་ན་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི། ལྕོགས་པ༌[^2926]ཉིད་ཀྱི་གནས་སྐབས་པས་གལ་ཏེ་རྫས་དེ་འདི་བླངས་པ་ལ་དངོས་གཞི་སྟེ། གལ་ཏེ་མ་ཡིན་ལྕོགས་པ༌[^2927]ཉིད་ཀྱི་གནས་སྐབས་ན་ཐོབ་པ་ན་དངོས་གཞི་སྟེ། ལེན་པ་པོའི་སྦྱོར་བ་ལ་ནི་ཁ་ན་མ་ཐོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4287]
འདིར་གཞུང་ནི་གང་ཞིག་འདི་ཐོབ་པའི་གནས་ལ་ས་ལེ་སྦྲམ་གྱི་རྫས་འཇུག་པ་བདག་གིར་བྱེད་ན་མ་ཐོབ་པའི་སྤང་བ་འདི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4288]
ཅི་ལྟར༌[^2928]བདག་གིར་བྱེད་པ་ཞེས་བྱ་བ་གཅིག་ཏུ་རྗེས་སུ་སྒྲུབ༌[^2929]ན་སྤང་བ་འདིར་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་རང་གི་རུང་བ་མ་བྱས་པ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གི་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དག་ལ་ལྟུང་བ་རྣམ་པར་གཞག་པས་སྤང་བའི་ལྟུང་བ་འདི་ལ་ཞིང་ཉིད་ཀྱི་ཕྱིར་མ་བྱས་པ་དང་འདྲ་བ་ལ་འཛིན་པ་གང་ཞིག་གསུངས་པ་འདི་ནི་འདིར་ལུང་ངོ་། །གང་གིས༌[^2930]བྱིན་པ་ལན་ཏམ༌[^2931]ལེན་དུ་འཇུག་པ་མེད་ན་འཛིན་པ་སྐྱེ་བར་མི་འགྱུར་རོ། །

[Block 4289]
འདིར་བདག་ཏུ་བྱས་པ་ནི་དེ་དང་རྗེས་སུ་མཐུན་པ་སྟེ། དེ་དང་རྗེས་སུ་མཐུན་པ་ནི་འཛིན་པ་བརྗོད་ཀྱིས༌[^2932]ངེས་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ་ཞེ་ན། འདི་ནི་འཐད་པ་མ་ཡིན་ཏེ། བདག་ཏུ་བྱ་བ༌[^2933]དང་དོར་བར་བྱ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4290]
རུང་བ་རྣམས་ལ་ནི་བདག་ཏུ་བྱ་བ་དང་དོར་བར་བྱ་བའི་ཕྱིར་རོ། །

[Block 4291]
གང་གི་ཕྱིར་བར་དུ་ཆད་པར་གྱུར་པ་འདི་རྣམས་ལ་བདག་ཏུ་བྱེད་པ་སྟེ། གང་ཞིག་དེའི་ལོགས་སུ་བྱེད་པར་འགྱུར་བ་ཉིད་དོ། །

[Block 4292]
དེ་བས་ན་འདིར་བདག་གིར་བྱ་བ་རྗེས་སུ་གནང་བ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 4293]
གང་ཞིག་འདིར་བླང་བར༌[^2934]བྱ་ཞིང་བླངས་ནས་ཀྱང་སྦྱིན་བདག་དེ་ཉིད་ལ་ཡིད་བརྟན་ཏེ་བཅང་བར་བྱ་བར་རྗེས་སུ་ངས་གནང་ངོ་ཞེས་གསུངས་པ་དེ་ནི་རུང་བ་དང་པོ་ཡིན་ནོ།[^2935] ། ཇི་ལྟར་འདིར་བདག་གིར་བྱེད་པ་མི་བསྐྱེད་པའོ། །

[Block 4294]
རུང་བར་བྱ༌[^2936]སྟེ་གཟུང་བར༌[^2937]བྱའོ་ཞེས་བྱ་བ་འདིའི་དོན་ནི་འདི་ཡིན་ནོ། །

[Block 4295]
འདུད་པའི་དོན་གྱིས་མངོན་པར་འབྲེལ་པར་གྱུར་པ་ཞེས་བྱ་བ་སྟེ། དེ་བས་ན་འདུད་པ་ཉིད་ཁས་ལེན་པ་ནི་འདིར་ལེན་པར་ཤེས་པར་བྱའོ། །

[Block 4296]
བདག་ཏུ་མ་བྱས་པ་ཉིད་ཀྱིས་འདུད་པར་བྱས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4297]
བདག་པོ་ཉིད་ཀྱིས༌[^2938]ལྷག་པོར་མོས་པ་དང་པོར་གཟུང༌[^2939]ནས་ལེན་པ་ལ་བྱ་བ་ཉིད་ནམ་ཡང་མ་བྱས་པ་དང་འདྲ་བ་ལ་ལེན་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 4298]
འཇུག་པ་གང་ལ་རང་གིར་མ་བྱས་པ་དང་འདྲ་བའི་རིན་པོ་ཆེ་མ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རེག་གམ་རེག་ཏུ་བཅུག་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཇི་ལྟར་རེག་པས་ཤེ་ན། དེའི་ཕྱིར་གང་ཡང་རུང་བས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕྱོགས་གཅིག་པར་རེག་ན་ཡང་ལོངས་ཤིག་ཁྱེར་ཅིག་ཞོག་ཅིག་ཅེས་བྱ་བ་ལྟ་བུ་དམིགས་ཀྱིས༌[^2940]མ་སྨྲས་པར་ཡང་རེ་ཞིག་ཅེས་བྱ་བ་དངོས་སུ་ཚིག་གིས་ཀྱང་མ་སྨྲས་ཤིང་། ཉེ་བར་གནས་པ་ལ་ཡང་གནས་གཞན་ན་གནས་པ་དེ་ལ་ཞེས་བྱ་བ་བསྟན་པས་ཉེ་བར་གནས་པ་ཉིད་ལ་འདི་ཞེས་བྱ་བའོ། །

[Block 4299]
སྙད་གདགས་སུ་རུང་བའི་ཟངས་མ་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་འདི་ལ་དམན་པའི་རིན་པོ་ཆེ་ཉིད་ཡོད་པའི་ཕྱིར་རོ། །

[Block 4300]
གཞན་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་སྙད་གདགས་སུ་རུང་བའི་ཟངས་མ་འདི་ལ་ནི་རྫས་ལས་རིན་པོ་ཆེ་ཉིད་མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4301]
ཞ་ཉེ་དང་ཁྲོ་ཆུ་དང་རོ་ཉེ་དང་ལྕགས་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདི་རྣམས་ཀྱང་རིན་པོ་ཆེ་ཉིད་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4302]
དགེ་ཚུལ་གཉིས་ཀྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི། དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་གཉིས་ཀྱིས༌[^2941]རིན་པོ་ཆེ་ལ་རེག་གམ་རེག་ཏུ་བཅུག་ན་ལྟུང་བ་མེད་དོ། །

[Block 4303]
གང༌[^2942]གི་རུང་བ་མ་བྱས་པ་ཡང་ངོ་ཞེས་སྨྲས་ན་རུང་བ་གང་ལ་བྱས་ན་རུང་བ༌[^2943]མ་ཡིན་པའི་རུང་བ་དེ་ཅི་འདྲ་བ་ཞིག་ཅེ་ན། དེའི་ཕྱིར་སྦྱིན་བདག་བདག་པོ་ཉིད་དུ་སྨོས་སུ་གཞུག་པ་དང་། ཞལ་ཏ་བྱེད་པ་བདག་པོ་ཉིད་དུ་ཁས་ལེན་དུ་གཞུག་པ་དང་། བྱིན་གྱིས༌[^2944]བརླབ་པ་ཞེས་བྱ་བ་ནི་རུང་བ་དག་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་རུང་བ་གསུམ་གྱི་གཞུང་ནི་དགེ་སློང་དག་དེ་ལྟ་བས་ན་རྗེས་སུ་ཤེས་པར་བྱ་སྟེ། ཆོས་གོས་ཀྱི་རིན་དག་རྙེད་པ་ན་བླང་བར་བྱ་ཞིང་བླངས་ནས་ཀྱང་སྦྱིན་བདག་དེ་ཉིད་ལ་ཡིད་བརྟན་ཏེ་བཅང་བར་བྱའོ། །

[Block 4304]
དེ་བཞིན་དུ་སྦྱིན་བདག་ཀྱང་སྤྲོ་བར་བྱའོ། །

[Block 4305]
བྱིན་གྱིས་བརླབ་པ་ཡང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པའི་གཞུང་ལས་གང་ཞིག་བདག་དགེ་སློང་མིང་འདི་ཞེས་བགྱི་བར༌[^2945]དངོས་པོ་རུང་བ་མ་ལགས་པ་འདིས་དངོས་པོ་རུང་བར་བསྒྲུབ་པར་བགྱི་ཞིང་དེ་ནི་བདག་གིར་བགྱིའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4306]
ལན་ཇི་ལྟ་བར་འདི་རྣམས་ལ་གཙོ་བོ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 4307]
གང་གི༌[^2946]ཕྱིར་སྦྱིན་བདག་གི་ཤིན་ཏུ་གསལ་བ་བདག་པོ་ཉིད་དུ་ལྷག་པར་མོས་པས་ཞལ་ཏ་བྱེད་པའི་བདག་པོ་ཉིད་དུ་ཁས་ལེན་པ་ལ་གཞན་གྱི་བློ་དང་གཞན་གྱི་རྣམ་པར་རིག་བྱེད་དང་བདག་གིར་བྱེད་པ་ཉིད་ལ་ཤིན་ཏུ་གསལ་བ་ཉིད་དོ། །

[Block 4308]
གང་ཞིག་འདིར་ཞལ་ཏ་བྱེད་པ་ལ་བདག་པོ་ཉིད་དུ་ཁྱོད་ཀྱིས་ཁས་ལེན་ཞིང་འདི་ལྟར་སྤྲོ་བར་བྱེད་པ་འདི་འདིར་བདག་པོ་ཉིད་དུ་ཁས་ལེན་པར་རིག་པར་བྱའོ། །

[Block 4309]
ཡང་ཅིའི་ཕྱིར་བདག་ཏུ་བྱ་བ་མ་ཡིན་པ་ལ་གོ་བར་བྱེད་པ་དང་། བྱིན་གྱིས་བརླབས་པ་ཡོངས་སུ་སྐྱོང་བ་ཉིད་ཀྱིས་བདག་གི་འདི་གཙུག་ལག་ཁང་ལ་སོགས་པ་དང་འདྲ་བར་བསྲུང་བ་དང་བྱིན་གྱིས་བརླབ་པར༌[^2947]བགྱིའོ། །

[Block 4310]
འདིར་བདག་གི་བློ་ནི་འདི་ཡིན་ཏེ་བདག་ཏུ་བྱ་བས་ནི་མ་ཡིན་གྱི། བདག་ལ་བདག་ཏུ་བྱ་བའི་དབང་གིས་བསྒྲུབ་པ་ཡང་མ་ཡིན་ཏེ། འདི་སྐད་ཅེས་ཚེ་དང་ལྡན་པ་དགོངས་སུ་གསོལ་ཞེས་བྱ་བའི་ངོ་བོ་ལས་གང་ཞིག་བདག་དགེ་སློང་མིང་འདི་ཞེས་བགྱི་བས་དངོས་པོ་རུང་བ་མ་ལགས་པ་འདི་རྙེད་དེ་ཞེས་བྱ་བའི་ཚིག་འདི་དེ་ཇི་ལྟར་བདག་ཏུ་བྱ་བ་རུང་བ་ཉིད་ཁས་ལེན་པ་ནི་འདིར་བསྒྲུབ་པ་སྟེ། བདག་ཏུ་བྱ་བ་འོངས་པའི་དོན་དང་སྦྱར་བ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
