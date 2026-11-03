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
[Block 3571]
མཚན་གྱུར་པ་ནི་དེའི་ཞིང་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་དེའི་ཞིང་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3572]
ཞིང་ཉིད་གང་ཡིན་པ་དེ་ནི་ལྟུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3573]
དེ་བས་ན་མཚན་གྱུར་པ་ཞེས་བྱ་བ་ནི་མཚན་མ་སྔ་མ་ཉིད་སྦྱོར་བ་ཙམ་གྱི༌[^2342]དབང་གིས་བསྒྲུབ་པར་གྱུར་པའི་ལྟུང་བྱེད་དོ། །

[Block 3574]
གང་ཞིག་ལྟུང་བ་ལ་དེའི་མཚན་མ་ཉིད་ཞིང༌[^2343]དུ་གྱུར་པ་ན་གལ་ཏེ་དེ་ཉིད་ལ་ཞིང་ཉིད་གང་གི་དོན་དུ་སྦྱོར་བ་དང་བཅས་པ་ད༌[^2344]ཉིད་དོ། །

[Block 3575]
གལ་ཏེ་ན་སྨད་པ་ཉིད་ཡིན་ན་སྨད་པའོ། །

[Block 3576]
འདི་ལ་དམིགས་ཀྱིས་བསལ་བ་བྱས་པ་ནི་ན་སྨད་པའི་དོན་གྱི་སྦྱོར་བ་གང་ཡིན་པ་ཉིད་ལས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྟུང་བ་ན་སྨད་པ་ཉིད་དོན་ཡིན་ཏེ། མཚན་མ་གཞན་གཏོགས་པའི་སྦྱོར་བ་ལས་མཚན་གྱུར་པ་དེ་ལ་ནི་ལྟུང་བ་གང་གི་སྦྱོར་བ་བྱས་པའི་ལྟུང་བ་དེ་ཉིད་ཉེས་བྱས་སོ། །

[Block 3577]
འདི་ལྟ་སྟེ་དཔེར་ན་དགེ་སློང་གཉིས་ཁྲི་གཅིག་ལ་རེག་པ་དང་བཅས་བཞིན་དུ་དགེ་སློང་མ་ཉིད་དུ་གྱུར་པ་ན་སྐྱ་རེངས་མ་ཤར་བའི་མདུན་རོལ་དུ་ཉལ་བ་ལ་ཉེས་བྱས་ཁོ་ནར་ཟད་ཀྱིས་ལྟུང་བྱེད་དུ་ནི་མི་འགྱུར་བ་ལྟ་བུའོ། །

[Block 3578]
བྱས་པ་ནི༌[^2345]དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མཚན་མ་གྱུར་པའི་གནས་སྐབས་སུ་ཁ་ན་མ་ཐོ་བ་གང་བྱས་པ་དེ་ནི། ཕྱིས་མཚན་གྱུར་ན་ཡང་ཁ་ན་མ་ཐོ་བ་གང་ཡིན་པ་དེའི་མཚན་གྱུར་པ་ཉིད་ལ་ཞིང་ཉིད་ནི་དེའི་ཁ་ན་མ་ཐོ་བ་ཉིད་དོ། །

[Block 3579]
དགེ་འདུན་ལྷག་མར་གཏོགས་པའི་སྦོམ་པོར་འགྱུར་ཏེ། དགེ་སློང་ཉིད་དུ་གྱུར་པའི་དགེ་སློང་མ་ལ་རེག་པའི་ཕམ་པ་གང་ཡིན་པ་དེའི་སྦྱོར་བ་ལ་ཉེས་བྱས་ཉིད་དོ། །

[Block 3580]
སྦོམ་པོ་ཉིད་ནི་ལུས་བཀན་པར་གྱུར་པའི་ཕམ་པར་གྱུར་པ་ཉིད་ལའོ། །

[Block 3581]
འཆབ་པའི་ཕམ་པར་གྱུར་པ་ལ་ནི་ཉེས་བྱས་ཉིད་དེ་ལྟུང་བྱེད་དུ་འགྱུར་བ་ཉིད་ལ་ནི་མ་ཡིན་ཏེ། མཚན་ཐ་དད་དུ་གྱུར་པ་འཆབ་པ་ལ་དེའི་ཚེ་འདི་ཡོད་པའི་ཕྱིར་རོ། །

[Block 3582]
རྗེས་སུ་ཕྱོགས་པའི་ལྟུང་བྱེད་གང་ཡིན་པ་དེ་ཉིད་འབྱིན་བཞིན་དུ་མཚན་གྱུར་ཅིང་དགེ་སློང་མར་གྱུར་ན་རྗེས་སུ་ཕྱོགས་པའི་ལྟུང་བྱེད་ནི་མཚན་ཐ་དད་པ་ལའོ། །

[Block 3583]
འདིར་དགེ་སློང་མ་ལ་ན་སྨད་པར་གྱུར་པ་ཉིད་ཁུ་བ་འབྱིན་པ་དགེ་འདུན་ལྷག་མ་དགེ་སློང་མ་ཉིད་དུ་གྱུར་པ་ལ་ལྟུང་བྱེད་ཅེས་བྱའོ། །

[Block 3584]
ན་སྨད་པ་ནི་རང་གི་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མཚན་གྱུར་པ་གཞན་ཉིད་ལ་ནི༌[^2346]ན་སྨད་པ་ཉིད་དེ་ཁ་ན་མ་ཐོ་བ་བྱས་པ་ཡིན་པ་དེ་གྱུར་པ་ལ། མཚན་གྱུར་ན་རང་གི་ཁ་ན་མ་ཐོ་བ་ཉིད་དུ་འགྱུར་ཏེ། ལྟུང་བྱེད་ཁོ་ནར་འགྱུར་རོ། །

[Block 3585]
དགེ་སློང་དུ་གྱུར་ན་ཁུ་བ་འབྱིན་པའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ། །

[Block 3586]
ཇི་ལྟར་རྗེས་སུ་མཐུན་པའི་མཚན༌[^2347]གྱུར་པའི་དབང་གིས་ནི༌[^2348]ན་སྨད་པ་མི་རིགས་པ༌[^2349]དེ་བཞིན་དུ་ལྷག་མ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 3587]
ལྷག་པར་སྤྱོད་པ་འདི་ལས་རྣམ་པར་གཞག་པའོ། །

[Block 3588]
འདིར་དེའི་ལྷག་པར་སྤྱོད་པ་མེད་པ་དེ་བས་ན་འདིས༌[^2350]ཤེས་པའོ། །

[Block 3589]
ཞག་བཅུར་མ་ལོན་པ་ནི་ཆ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདི་ནི་ཡོད་པ་ལ་སྟེ། ཞག་བཅུ་མ་ལོན་པའི་བདག་ཉིད་ཀྱི་དུས་ཡོད་པ་ལ་དེའི་མཚན་གྱུར་ཏེ། འཆང་བའི་དུས་གང་ཡིན་པ་དེ་ལ་ཆ་ཉིད་དོ།[^2351] །དེ་ཉིད་ནི་དེའི་དུས་ཉིད་མ་ཡིན་ནོ། །

[Block 3590]
འདིར་ཡོངས་སུ་རྫོགས་པ་ལ་ཇི་ལྟར་རྙེད་པའི་དེ་ཉིད་དོ། །

[Block 3591]
འདིའི་ཡུལ་ནི་ལྷུང་བཟེད་འཆང་བ་སྟེ། གཞན་དུ་ཆོ་ག་ཐ་དད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 3592]
འདིར་དུ་མ་ལ་སོགས་པ་དགུའི༌[^2352]མཐར་ཐུག་པའི་ཞག་རྣམས་ལས་འདས་ན་དེ་དགེ་སློང་མ་ཉིད་དུ་གྱུར་ན། ཞག་དགུ་པོ་དེ་དག་ཞག་གཅིག་པོའི་ཁོངས་སུ་གཏོགས་པས་དོན་མེད་པ་ཉིད་ཐོབ་པར་བྱེད་པའོ། །

[Block 3593]
འདིར་གཞུང་ནི་བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་ལྷུང་བཟེད་རྙེད་པ་ན་མཚན་གྱུར་ཏེ་དགེ་སློང་མར་གྱུར་ནས་དགུང་གཅིག་ལས་ལྷག་པར༌[^2353]འཆང་ན་ལྟུང་བ་ཅིར་འགྱུར། སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ། །

[Block 3594]
དགེ་སློང་གིས༌[^2354]དུས་དང་ལྷན་ཅིག་ཏུ་ལྷག་པར་འཆང་བ་ནི། དགུང་གཅིག་གི་ཆ་ལས་གྱུར་པ་ཉིད་ཀྱིས་ལྷག་པར་གནས་པས་སྨོས་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3595]
འདིར་ཡང་ལྷན་ཅིག་རྙེད་པ་འཆང་བ་ལ་བཙུན་པ་དགེ་སློང་གིས་ལྷུང་བཟེད་ལྷག་པ་དགུང་གཅིག་ལས་ལྷག་པར་འཆང་བ་ལས་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་བ་མཆིས་སམ། ཡོད་དེ་དགེ་སློང་གིས་ལྷུང་བཟེད་རྙེད་པ་ན་མཚན་གྱུར་ཏེ་དགེ་སློང་མར་གྱུར་ནའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3596]
རིགས་ལ༌[^2355]ནི་ཕན་ཚུན་གནས་ཐོབ་པ་ཉིད་འདིར་ཞག་བཅུ་དང་ཞག་གཅིག་ལ་འཆང་བ་འདི་ཐུན་མོང་བ་ཉིད་དོ། །

[Block 3597]
ཞིང་མ་ཡིན་པ་ཉིད་ལས་ནི་ཉམས་སོ་ཞེས་བྱ་བ་ནི་མཚན་གྱུར་པ༌[^2356]གང་ལ་དེའི་མཚན་གྱུར་པ་ཉིད་ལ་ལྟུང་བའི་ཞིང་མ་ཡིན་པ་ཉིད་དོ། །

[Block 3598]
ཐུན་མོང་མ་ཡིན་པ་སྔར་གནང་བ་མ་ཐོབ་པར་འཁོར་ཉེ་བར་འཇོག་པ་ལའོ། །

[Block 3599]
ཤམ་ཐབས་རྐེད་པ་སྣང་བ་བགོ་བར་མི་བྱའོ་ཞེས་བྱ་བའི་བསླབ་པ་ལ་སོགས་པ་ལས་འདས་ཏེ་སྔོན་གྱི་མཚན་མ་ཉིད་དུ་བྱས་པ་ནི་མ་གཏོགས་པའོ། །

[Block 3600]
འདིར་གཞུང་ནི། གཏམ་གྱི་གཞི་ལས་དགེ་སློང་ལྟུང་བ་ཐུན་མོང་མ་ཡིན་པ་སྡེ་བཞི་པོ་དག་བྱུང་བ་དེ་མཚན་གྱུར་ཏེ། དགེ་སློང་མར་གྱུར་པ་ལྟུང་བ་དེ་དག་ལས་འབྱུང་བར་བརྗོད་པར་བྱའོ། །

[Block 3601]
དགེ་སློང་མ་ལྟུང་བ་ཐུན་མོང་མ་ཡིན་པ་སྡེ་ལྔ་པོ་དག་བྱུང་བ་དེ་མཚན་གྱུར་ཏེ་དགེ་སློང་དུ་གྱུར་ན་དེ་དག་ལས་བྱུང་བར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3602]
དེ་ལ་ཉེས་པ་བཅས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དེ་ཉིད་ཞིང་མ་ཡིན་པ་ཉིད་ལ་ནི་ཉམས་སོ་ཞེས་བྱ་བ་སྨོས་པ་དེ་ལ་ནི་འཆབ་པའི་ཉེས་པ་དོགས་པར་མི་བྱའོ། །

[Block 3603]
མཚན་ཐ་དད་པ་མ་ཡིན་པའི་དོན་དུ་ནི་འདི་སྐྱེས་པ་སྟེ། དེའི་ཕྱིར་མཚན་གཞན་གྱུར་པ་དེ་དང་མཉམ་པ་ནི་འདིར་ཞིང་ཉིད་མ་ཡིན་ནོ། །

[Block 3604]
མགུ་བ་སྤྱད་པ་ནི་དོན་མེད་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྣམ་པ་ཐམས་ཅད་དང༌[^2357]རྣམ་པ་ཐམས་ཅད་མ་ཡིན་པ་ཞེས་བྱ་བ་བྱེ་བྲག་མ་སྨོས་པས་རྟོགས་པར་བྱའོ། །

[Block 3605]
འདིར་གཞུང་ནི་སྤོ་བའི་གཞིའི་ཞུ་བ་ལས།

[Block 3606]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་དབྱུང་བ་ལ་སོགས་པ༌[^2358]ཐུག་པ་མཚན་གྱུར་ཏེ༌[^2359]དགེ་སློང་མར་གྱུར་ན། ཅི་དེས་གཉིས་ཀའི་དགེ་འདུན་ལ་ཟླ་བ་ཕྱེད་མགུ་བ་སྤྱད་པ་སྤྱད་པར་བགྱིད༌[^2360]འཚལ་ལམ། སྤྱད་པར་བྱ་དགོས་སོ། །

[Block 3607]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་མ་གཉིས་ཀའི་དགེ་འདུན་ལ་མགུ་བ་སྤྱོད་པ་མཚན་གྱུར་ཏེ། དགེ་སློང་དུ་གྱུར་ན་ཅི་དེས་དགེ་འདུན་ལ་ཞག་དྲུག་མགུ་བ་སྤྱད་པ་སྤྱད་པར་བགྱིད་འཚལ་ལམ། སྤྱད་པར་བྱ་དགོས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3608]
མདོ་སྔ་མ་ཤོས་ཀྱིས་ནི་ལུས་ཀྱི་ཉེས་པ་བཅབས་པ༌[^2361]ཉམས་པ་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 3609]
ཕྱི་མའི༌[^2362]སྤྱད་པ༌[^2363]ཡང་སྤྱད་པར་བྱ་བ་ཉིད་དོ། །

[Block 3610]
ཡང་གང་གི་ཕྱིར་བྱས་པ་ནི་དེ་ཉིད་ཡིན་ནོ། །
--- END BLOCKS ---
