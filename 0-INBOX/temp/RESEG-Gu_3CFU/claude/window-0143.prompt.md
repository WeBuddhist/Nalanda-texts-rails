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
[Block 5006]
ཇི་ལྟར་ཉམས་པ་དང་གཅོད་པ་དང་རུང་བ་ལ་སོགས་པ་ཉིད་ཀྱིས༌[^3388]ཅིར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཇི་ལྟར་ཡང་རུང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཉིད་བསྟན་པའི་ཕྱིར་སྤྲུལ་པས༌[^3389]ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 5007]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས༌[^3390]ཤིང་ཏོག་རྣམས་སྤྲུག་ཅིང་གློག་པར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། གལ་ཏེ་ཤིང་ཏོག་སྨིན་པ་དག་ཡིན་ན་ནི་ཉེས་བྱས་སོ། །

[Block 5008]
ཇི་སྟེ་མ་སྨིན་པ་དག་ཡིན་ན་ནི་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5009]
རྩ་བ་དང་འདམ༌[^3391]རྫབ་དང་ས་རྡུལ་ལ་སོགས་པ་དག་གིས་མནན་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་རན་ནམ་འདམ་རྫབ་བམ་ས་རྡུལ་གྱིས༌[^3392]ཤིང་ལྗོན་པ་ཉམས་པར་གྱུར་ཅིག །རྣམ་པར་ཉམས་པར༌[^3393]གྱུར་ཅིག་ཅེས་གནོན་པར་བགྱིད་ཅིང་རྩྭ༌[^3394]སྔོན་པོ་ས་རྡུལ་ལམ་ཕྱེ་མའམ་གཞན་གང་ཡང་རུང་བས་འགེབས་པར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5010]
འདིར་སྦྱོར་བ་ཙམ་ལ་དགོངས་ནས་ཤིང་ལ་སོགས་པ་མནན་པ་ལ་སོགས་པ་ལ་ཉེས་བྱས་ཀྱི་ཚིག་གོ། །

[Block 5011]
འདིར་འདམ་རྫབ་ཀྱི་ཚིག་གིས་བཟུང་བའོ། །

[Block 5012]
ཁུ་ཚན་ལ་སོགས་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། ཁུ་ཚུན༌[^3395]ཞེས་བྱ་བ་ནི་འུ་ཤ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཁུ་བ་ཚབ་གཏོར་བའོ། །

[Block 5013]
སོགས་པ་ཞེས་བྱ་བའི་སྒྲས་ནི་འཆག་པ་དང་ཡལ་ག་ལ་སོགས་པ་འདྲེན་པ་དང་དཀྱིལ་འཁོར་དང་སྐྱང་ནུལ་ལ་སོགས་པ་དག་ཀྱང་བསྡུའོ། །

[Block 5014]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་སྔོའི་ཕྱོགས་སུ་འུ་ཤ་ཚ་བ་འཐོར་ཞིང་སྙིང་པོ་འཐོར་བར་བྱེད་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 5015]
རླུང་དང་ཉི་མ་ལ་འཇོག་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས་དགེ་སློང་མས་ས་བོན་གྱི་རིགས་ལྔ་པོ་འདི་དག་ཉམས་པར་གྱུར་ཅེས་རླུང་དང་ཉི་མ་ལ་འཇོག་པར་བྱེད་ན་གལ་ཏེ་ས་བོན་རྣམ་པར་ཉམས་པ་ནི་ལྟུང་བྱེད་དོ། །

[Block 5016]
ཇི་སྟེ་རྣམ་པར་མ་ཉམས་ན་ནི་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5017]
ས་གཞི་སྐམ་པོར་ཡང་ངོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་དགེ་སློང་གིས་ས་བོན་གྱི་རིགས་ལྔ་པོ་དག་ཉམས་པར་གྱུར་ཅིག་ཅེས་ས་གཞི་སྐམ་པོར་འཇོག་པར་བྱེད་ན་གལ་ཏེ་ས་བོན་ཉམས་ན་ནི་ལྔར་འགྱུར་རོ། །

[Block 5018]
གལ་ཏེ་རྣམ་པར་མ་ཉམས་ན་ནི་ཉེས་བྱས་ལྔར་འགྱུར༌[^3396]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5019]
བསམ་པ་ཇི་ལྟ་བུས་ཤེ་ན། དེའི་ཕྱིར་དེར༌[^3397]འདུན་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉམས་པར་འདུན་པས་སོ། །ཅི་རང་ཁོ་ནས་སམ་ཞེ་ན། དེའི་ཕྱིར་རང་ངམ་གཞན་གྱིས་ཀྱང་རུང་ངོ་ཞེས་བྱ་བ་སྨོས་སོ།[^3398] །འདིར་གནས་སྐབས་གང་ལ་ཁ་ན་མ་ཐོ་བ་ཇི་ལྟ་བུ་དག་ཉམས་པ་ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཉམས་པར་འགྱུར༌[^3399]ཞེ་ན་དངོས་གཞི་དག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉམས་པར་གྱུར་པ་ནི་དངོས་གཞིའི་ལྟུང་བ་དག་ཀྱང་འབྱུང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5020]
སྦྱོར་བ་གཅིག་གི༌[^3400]དབང་གིས་ས་བོན་མང་པོ་དག་ཉམས་པར་བྱེད་ན་ཅི་གཅིག་གམ་མང་པོ་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཉམས་པར་བྱ་བའི་གྲངས་དག་གིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉམས་པར་བྱ་བ་འདི་རྣམས་ལ་གྲངས་ཡོད་པས་ཞེས་བྱ་བ་འདིར་བསྡུའོ། །

[Block 5021]
ཇི་ལྟར་ཉམས་པར་བྱ་བ་དག་གི་གྲངས་ཀྱིས་ལྟུང་བ་རྣམ་པར་གཞག་པར་བསྟན་ཅིང་། སྡོང་པོ་དང་ཡལ་ག་དང་འདབ་མ་ལས་གྲངས་རྣམ་པར་གཞག་པར་བྱ་འམ་ཞེ་ན། དེའི་ཕྱིར་སྡོང་བུ་ལས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྡོང་བུ་རྩ་བ་ལས༌[^3401]ཤིང་ལྗོན་པ་གཅོད་པར་བྱེད་ན་ཡང་ཡལ་ག་ཕྲ་མོ་དང་འདབ་མ་དུ་མ༌[^3402]ཉིད་ཡོད་དུ་ཟིན༌[^3403]ཀྱང་ལྟུང་བ་གཅིག་ཁོ་ནར་འགྱུར་ཏེ། དེ་བཞིན་དུ་ཡལ་ག་དག་རང་གི་སྡོང་བུ་ལས་བཅད་པ༌[^3404]ལ་ཡལ་ག་ཕྲ་མོ་དང་འདབ་མ་མང་པོ་ཉིད་ཡོད་པ་དང་། ཡལ་ག་ཕྲ་མོ་དག་རང་གི་སྡོང་པོ་ལས་བཅད་པ་ལ་འདབ་མ་མང་པོ་ཉིད་ཡོད་པ་དང་། འདབ་མ་དག་རང་གི་སྡོང་བུ་ལས་བཅད་པ་ལས་འདབ་མ་བདུན་པ་ལྟར་འདབ་མ་མང་པོ་ཉིད་ཡོད་པ་དང་། ཨེ་རན་ཏའི་འདབ་མ་ལྟར་ཡལ་ག་མང་པོ་ཉིད་ཡོད་དུ་ཟིན་ཀྱང་དེ་ལྟ་མོད་ཀྱི་ལྟུང་བྱེད་གཅིག༌[^3405]ཁོ་ནར་འགྱུར་རོ། །

[Block 5022]
སྡོང་བུ་ཞེས་བྱ་བ་ནི་འདིར་འོག་མའི་ཆའི་དཔེ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་འདབ་མའི་ཡལ་ག་བཅད་པ་དང་། ལྕུག་མའི་མགོ་ལྕོགས་བཅད་ན་ཡང་འདིར་དངོས་གཞི་སྟོན་པ་ཉིད་དོ། །

[Block 5023]
སྡོང་བུའི་ངོས་ནས་འདབ་མ་ལ་ཅུང་ཟད་བརྩེགས་པ་དང་། འདབ་མའི་རིམ་པ་ནས་ཅུང་ཟད་བརྩེགས་པ་ནི་སྦྱོར་བའི་ཉེས་བྱས་ཏེ། དངོས་གཞིའི༌[^3406]ནི་མ་ཡིན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 5024]
འདིར་གཞུང་ནི་དགེ་སློང་གིས༌[^3407]ཤིང་ལྗོན་པ་གཅིག་སྦྱོར་བ་གཅིག་གིས་བཅད་ན་ཉེས་བྱས་གཅིག་དང་ལྟུང་བྱེད་གཅིག །དགེ་སློང་གིས་ཤིང་ལྗོན་པ་གཅིག་སྦྱོར་བ་གཉིས་ཀྱིས་གཅོད་ན་ཉེས་བྱས་གཉིས་དང་ལྟུང་བྱེད་གཅིག་གོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 5025]
སྐྱེ་བའི་ཕྱིར་མདོ་རྣམ་པར་བཤད་ནས་མདོ་དེ་ཉིད་ལས་ས་བོན་གྱི་ཕྱིར་འདི་ལྟར་ཤེས་པར་བྱ་སྟེ། ཇི་ལྟར་ཞེ་ན་གང་ཞིག་ཉམས་པར་བྱ་བའི་གྲངས་དག་གིའོ་ཞེས་སྨོས་པས་གཞན་ས་བོན་དུ་གྱུར་པ་གང་ཕྱོགས་གཅིག༌[^3408]པ་དེ་བས་ན་མ་ཡིན་ཞེས་སྨོས་པ་ནི་སྡོང་བུ་ལས་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 5026]
སྡོང་བུ་ཐམས་ཅད་ལ་གཅིག་པ་ཉིད་མངོན་པར་བརྟེན་པས་འདིར་གཟུགས་ཐམས་ཅད་སྡོང་བུ་ཉིད་ཀྱིས་བརྗོད་པར་རིག་པར་བྱ་སྟེ། རྩ་བ་དང་འབྲས་བུ་དག་ལ་ནི་འདི་མེད་པ་མ་ཡིན་ནོ། །

[Block 5027]
དེ་བས་ན་འདི་དག་ལ་འདིས་མ་བསྡུས་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 5028]
གཟུགས་ཐ་དད་པ་རྣམས་ལ་སྦུབས་དང་ཡལ་ག་དག་ལ་འདི་གནས་པའོ། །

[Block 5029]
གང་ཞིག་ཐོ༌[^3409]གུ་དང་རྩེ་མོ་དག་ལའོ། །

[Block 5030]
དེ་ལས་བྱུང་བའི་འབྲས་བུ་རྣམས་ལ་གཅིག་པ་ཉིད་དུ་མངོན་པར་བརྟེན་པ་ལ་བྱས་པ་ཉིད་དེ་ཕྱོགས་གཅིག་ཏུ་གྱུར་པའི་ས་བོན་ཉམས་པས་ས་བོན་ཉམས་པ་མ་ཡིན་ནོ། །

[Block 5031]
དེ་བས་ན་ས་བོན་གྱི་ཕྱོགས་གཅིག་ཉམས་པ་ལ་ཡང་དངོས་གཞི་སྟེ། ཐམས་ཅད་ཉམས་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 5032]
སྦྱོར་བ་ལ་ནི་ཉེས་བྱས་དག་ཏུའོ་ཞེས་བྱ་བ་ནི་སླར་ཅི་ཞིག་ཉམས་པར་བྱ་བའི་གྲངས་ཀྱིས་འདི་རྣམས་ཀྱི་ཐ་དད་པ་ཡིན་ནམ་མ་ཡིན་ཞེ་ན། [^3410]དེའི་ཕྱིར་འདི་ལ་བསྣུན་པ་རེ་རེ་ལས་དེ་ཐ་དད་པ་ཡིན་གྱི་དངོས་པོ་ལས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ལ་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་ལའོ། །

[Block 5033]
དེ་ཞེས་བྱ་བ་ནི་བསྣུན་པ་ལའོ། །

[Block 5034]
བསྣུན་པ༌[^3411]རེ་རེ་ལ་དེ་ཐ་དད་པ་སྟེ། དངོས་པོ་ཐ་དད་པ་ལས་ནི་མ་ཡིན་ནོ། །

[Block 5035]
བསྣུན་པ་ཇི་སྙེད་པ་དེ་ཁོ་ན་ཉིད་ཀྱི་སྦྱོར་བ་དག་ཏུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5036]
བཏོན་ན་བསྐྱེད་པར་བྱ་བ་ཉིད་ཡིན་དུ་ཟིན་ཀྱང་མཐའ་ཉིད་དེ་ཞེས་བྱ་བ་ནི་ཤིང་ལྗོན་པ་ལ་སོགས་པ་རང་གི༌[^3412]གནས་ནས་བཏོན་པ་གང་ཡིན་པ་དེ་ལ་མཐའ་ཉིད་དེ༌[^3413]སྐྱེར་རུང་བའི་ཆོས་ཉིད་ཡོད་དུ་ཟིན་ཀྱང་ཉམས་པ་ལས་སྐྱེ་བ་ཉིད་དེ། དེའི་ཚེ་ཉམས་པ་ལས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5037]
སྐྱེར་མི་རུང་བ་ཉིད་ཡོད་ཀྱང་སྔར་གྱི་རྣམ་པ་ཉིད་ཀྱིས༌[^3414]སོ་སོར་བརྗོད་པ་ལ་འདི་ཉེ་བར་མ་སོན་པར་གྱུར་པ་དང་རོ་ཉིད་དུ་གྱུར་པའི་བྱེ་བྲག་ཡོད་དེ་ཞེས་བྱ་བ་ཤེས་བཞིན་པའོ། །

[Block 5038]
སྐྱེར་རུང་བ་ཉིད་ལ་ནི་རྙེད་པ༌[^3415]ཉིད་ཡོད་དུ་ཟིན་ཀྱང་རོ་ཉིད་དུ་གྱུར་པའི་བྱེ་བྲག་མེད་དོ་ཞེས་བྱ་བ་ཡིན་ལ་ངེས་པར་ཐིམ་པ་ཡིན་ནོ། །

[Block 5039]
དེ་བས་ན་འདིར་མདོ་འདི་བྱས་པའོ། །

[Block 5040]
ཉ་ལྕིབས་དང་ཉ་ཚང་དག་ཆུ་ནས་བཏོན་པ༌[^3416]ནི་དེ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། ཉ་ལྕིབས་དང་ཉ་ཚང་དག་ཆུ་ནས་བཏོན་པ་ནི་དེ་ཉིད་དོ། །

[Block 5041]
ཆུ་ནས་འདི་དག་ལ་བཏོན་པ་དང་རྗེས་སུ་བཟུང་བ་དེ་ལ་དེའི་ཚེ་ན་གཅོད་པ་ཞེས་བྱ་བའོ།

[Block 5042]
[^3417] །དེའི་ཚེ་ན་འདི་དག་ལ་རོ་ཉིད་ཁས་བླངས་པའོ། །

[Block 5043]
གང་ཞིག་སླར་བཅུག་པ༌[^3418]དག་ལ་དེ་ལྟ༌[^3419]ཉིད་དུ་རྗེས་སུ་འཇུག་པས་དེ་ཡང་ས་བོན་ཉིད་ལ་རྗེས་སུ་འཇུག་པ་ཉིད་ཀྱིས་ཉ་ལྕིབས་དང་ཉ་ཚང་དག་ལ་གང་ཞིག་ས་དང་མ་འབྲེལ་པས་ཆུའི༌[^3420]སྟེང་དུ་སྐྱེས་པ་དེ་ལ་འདི་བཤད་པའོ། །

[Block 5044]
ཚི་གུ༌[^3421]མ་བཅོམ་པར་རིལ་མིད་བྱེད་པ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཚི་གུ༌[^3422]མ་བཅོམ་པ་ཞེས་བྱ་བ་ནི་སོ་རྣམས་ཀྱིས་དུམ་བུར་མ་བྱས་པ་ལ་གང་ཞིག་རིལ་མིད་བྱེད་པ་ནི་ཟ་བར་བྱེད་པ་ལ་ཕྱེད་ཅེས་བྱ་བའི་ཚིག་སྨོས་པས་ནི་ཉེས་བྱས་ཡིན་པར་གོ་བར་བྱེད་དོ། །

[Block 5045]
ཕྱེད་ཀྱི༌[^3423]ཚིག་གིས༌[^3424]ཐམས་ཅད་དུ་ལྟུང་བ་གཅོད་པར་གྱུར་པའི་ཉེས་བྱས་སྟོན་པར་བྱེད་པའོ། །
--- END BLOCKS ---
