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
[Block 4831]
ཤིན་ཏུ་དགག་དབྱེ་མཛད་དོ་ཞེས་བྱ་བ༌[^3387]ནི་ཁོ་བོ་ཅག་གིས་འདི་ལ་ཐེ་ཚོམ་པར་ཞེས་བྱ་བ་དེ་ལྟར་བསྒྲུབ་པའོ། །

[Block 4832]
རང་གི་རྫས་གང་ཡང༌[^3388]རུང་བ་ཐ་ན་ཁབ་ཙམ་གྱིས་ཀྱང་དགེ་འདུན་ལ་རྫས་ཀྱི་དགག་དབྱེ་བརྩམ་པར༌[^3389]བྱ་སྟེ། དེ་བླངས་ནས་ཚིག་གིས་སོ་ཞེས་བྱ་བ་ལ། རང་གིས་ཞེས་བྱ་བ་ནི་དགག་དབྱེ་བྱེད་པོ༌[^3390]བདག་ཉིད་དོ། །

[Block 4833]
ཇི་ལྟར་བྱ་ཞེ་ན་དེའི་ཕྱིར་དེ་བླངས་ནས་ཚིག་གིས་སོ་ཞེས༌[^3391]སྨོས་ཏེ། དེ་བླངས་ནས་ཐ་ན་ཞེས་བྱ་བ་ནི་རང་གིས་ཁབ་ལ་སོགས་པའོ། །གང་ལ་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་ལ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྒན་པའི་མཐའ་ལོགས་སུ་འདུག་སྟེ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 4834]
ཚིག་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་བཙུན་པ། རྫས་ཇི་ལྟ་བུས་ཀྱང་དབྱར་གནས་པའི་དགེ་སློང་གི་དགེ་འདུན་ལ་དགག་དབྱེ་བགྱིར༌[^3392]རུང་ངོ་ཞེས་བྱ་བས་སོ། །

[Block 4835]
དེའི་འོག་ཏུ་དགེ་ཚུལ་རྣམས་ལ་དགག་དབྱེ་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ཞེས་བྱ་བ་ནི་རྫས་ཀྱི་དགག་དབྱེ་བྱས་པ་དེའི་འོག་ཏུ༌[^3393]ཏུའོ། །

[Block 4836]
དེའི་འོག་ཏུ་དགེ་སློང་མ་རྣམས་ལའོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་དགེ་ཚུལ་རྣམས་ལ་དགག་དབྱེ་བྱས་པའི་འོག་ཏུ་དགེ་སློང་མ་རྣམས་ལ་དགག་དབྱེ་བྱའོ། །

[Block 4837]
རང་གི་ཕྱོགས་མ་རྫོགས་པར་ཕྱོགས་གཞན་ལ་འཇུག་པར༌[^3394]མི་རིགས་པ་ཞེས་བྱ་བའི་རྒྱུ་དེ་མཐོང་བ་ཡིན་ནོ། །

[Block 4838]
ཚིག་འདི་ནི་ཕྱོགས་གཞན་དུ་གཙོ་བོ་ཡིན་གྱི་བསྙེན་པར་རྫོགས་པའི་རྒྱུ་མཚན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 4839]
དེ་ལྟ་བས་ན་དགེ་སློང་མ་དང་དགེ་ཚུལ་མ་རྣམས་ལ་འདི་མ་བསྡུས་པ་མ་ཡིན་ནོ། །

[Block 4840]
བྱིན་གྱིས་བརླབས་ཏེ་སོང་བས་དེར་སྔར་དགག་དབྱེ་བྱེད་པ་ན་བྱས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། དགེ་སློང་གང་གཞན་དུ་སོང་བ་དེ་རྣམས་ཀྱི༌[^3395]དགག་དབྱེ་ནི་དེའི་འོག་ཏུ༌[^3396]དགག་དབྱེའོ། །

[Block 4841]
བྱིན་གྱིས་བརླབ་པར༌[^3397]བྱས་ནས་འགྲོ་བར་གྱུར་པ་ལ་སྔ་མ་གནས་པར་ཁས་བླངས་པའི་དབང་གིས་སམ་ཚེས་གྲངས་ནོར་བའི་དབང་གིས་འམ༌[^3398]གང་ཟག་འཐབ་ཀྲལ་ཅན་འོང་བར་གྲགས་པའི་དབང་གིས་གནས་དེར་དགག་དབྱེའི་དུས་པས་སྔར་ཚོགས་ཏེ་དེ་དག་དང་ལྷན་ཅིག་དགག་དབྱེ་བྱས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4842]
གང་དུ་གནས་པར་ཁས་བླངས་པ་དེ༌[^3399]ཉིད་དུ་དགག་དབྱེ་ངེས་པར་འཆགས་ཀྱི་གཞན་དུ་ན་མི་འཆགས༌[^3400]སོ་སྙམ་དུ་དོགས་པ་བསལ་བའི་ཕྱིར་མདོར་བྱས་སོ། །

[Block 4843]
འདིར་གཞུང་ནི། བཙུན་པ། རེ་ཞིག་དགག་དབྱེའི་གདུགས་ཀྱི་ལྷག་མ་བཅུ་མཆིས་ཤིང་དགེ་སློང་དེ་ཡང་བསྐོས་ཏེ། མཚམས་ཀྱི་སླད་དུ་མཆིས་ན་དེ་ནས་གདུགས་བདུན་ན་དགག་དབྱེ་བྱུང་ནས་དེ༌[^3401]དེར་དགག་དབྱེ་བགྱིད་ན་དགག་དབྱེ་བགྱིས་ཞེས་བགྱིའམ་ཉེ་བ༌[^3402]འཁོར་དགག་དབྱེ་བྱས༌[^3403]ཞེས་བྱའོ། །

[Block 4844]
བཙུན་པ་རེ་ཞིག་དགག་དབྱེའི་གདུགས་ཀྱི་ལྷག་མ་བདུན་མཆིས་ཤིང་དགེ་སློང་དེ་ཡང་བྱིན་གྱིས་བརླབས་ཏེ། མཚམས་ཀྱི་ཕྱི་རོལ་དུ་མཆིས་ན༌[^3404]གང་དུ་མཆིས་པ་དེར་གདུགས་བཞི་ལ་དགག་དབྱེ་བགྱིས་ན་དགག་དབྱེ་བགྱིས་ཞེས་བགྱིའམ་ཉེ་བ༌[^3405]འཁོར་དགག་དབྱེ་བྱས་ཞེས་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4845]
བུད་མེད་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདིར་དགག་དབྱེ་བྱེད་པ་པོ་ཉིད་ལ་ཉེ་བར་འབབ་པའོ། །

[Block 4846]
བུད་མེད་ལ་ཞེས་བྱ་བ་འདིས་ཀྱང་བུད་མེད་ལ་དགག་དབྱེ་བྱེད་པ་མ་ཡིན་པ་ནི་དགག་དབྱེ་བྱས་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4847]
དགག་དབྱེ་བྱེད་པ་པོ་ཉིད་ཀྱི་ཚིག་ནི་འདི་ཡིན་ཏེ། དགེ་འདུན་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དང་པོའི་ཚིག་གིས་རྟོགས་པའོ། །

[Block 4848]
སྐྱེས་པའི་ཕྱིར་ཆོ་ག་ནི་འདི་ཡིན་ནོ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་བུད་མེད་ཀྱི་མཚན་ལ་སྐྱེས་པའི་དགག་དབྱེ་བྱས་པ་ཉིད་གང་ཡིན་པ་དེ་ནི་འགྱུར་བའི་དབང་གིས་མཚན་སྒྲུབ་པ་ཡིན་ཏེ། དེ་ནི་དགག་དབྱེ་བྱས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4849]
འདིར་གཞུང་ནི། དགེ་སློང་དགག་དབྱེ་བྱེད་པ་མཚན་གྱུར་ན། དགག་དབྱེ་བྱས་པ་མ་ཡིན་པར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4850]
གནས་པར་མི་ནུས་པ་ཉིད་ཡིན་ན་སྤྱོད་ཡུལ་དུ༌[^3406]གྱུར་པའི་དགེ་སློང་ལ་ཚོགས་ཀྱི༌[^3407]དགག་དབྱེས་གོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་སྐྱེ་གནས་འཁྲུགས་པ༌[^3408]ཞེས་སྨོས་པ་ཡིན་ཏེ། རྒྱལ་པོ་ལ་སོགས་པ་ཕ་རོལ་གྱི་གནོད་པ་རྣམས་ལ༌[^3409]འདི་ཡོད་པ་སྟེ། དེའི་རིགས་ཅན་གཞན་རྣམས་ལ་ཡང་ཡོད་པའོ། །

[Block 4851]
དེར་གནས་པར་རིགས་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་འདི་ལ་མཚོན་པ་ཙམ་ཉིད་ཡིན་ཏེ། དེ་བས་ན་འདི་ལྟར་མདོར་བྱས་སོ། །

[Block 4852]
སྤྱོད་ཡུལ་དུ་གྱུར་པ་ཞེས་བྱ་བ་ལ་ཕན་ཚུན་དུ་མཆོད་ནས་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་གཞན་དག་གི༌[^3410]འདོད་པའོ། །

[Block 4853]
དེ་ལ་ཐམས་ཅད་ཀྱིས་ཕན་ཚུན་དུ་ཞེས་དོན་འདི་རིགས་པ་ཡིན་ཏེ། མི་ནུས་པ་ཉིད་ཀྱི༌[^3411]ཕྱིར། གང་གིས་གང་མཐོང་བ་དེས་དེ་བལྟ་བར༌[^3412]བྱའོ་ཞེས་བྱ་བ་འདིར་དོན་འདི་རྟོགས་པར་བྱའོ། །

[Block 4854]
འདིར་ཡང་སྤྱོད་ཡུལ་ཐོབ་པ་ཉིད་ལ་དེ་བརྟན་པ་ཞེས་བྱ་བ་རྟོགས་པར་བྱ་ཏེ། ངེས་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ཉིད་འབྲེལ་པའོ། །

[Block 4855]
དགེ་འདུན་ལ་རྫས་ཀྱི་དགག་དབྱེ་ཞེས་བྱ་བ་ནི་སྔགས་མཚོན་པའོ། །

[Block 4856]
སྔགས་འདི་ལ་རྣམ་པ་གང་ཀླགས་པ་དེས་ལྟ་བར༌[^3413]བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4857]
དེ་ལ་དོན་གྱི་སྔགས་དེས་ཞེས་བྱ་བ་ཐོབ་པ་ཡིན་ནོ། །

[Block 4858]
འདིར་སྔགས་ནི་ཚེ་དང་ལྡན་པ་དེང་ནི་དགེ་འདུན༌[^3414]དགག་དབྱེ་མཛད་དེ། བདག་དེ་སྲིད་དུ་དེང་དགེ་འདུན་ལ་དགག་དབྱེ་བགྱིད་དོ་ཞེས་བྱ་བའོ། །

[Block 4859]
སྐྱེ་བའི་གནས་འཁྲུགས་པ་ལ་སོགས་པའི་ཉེ་བར་འཚེད་པས་མི་ནུས་པ་ཉིད་ལ་གནས་པའི་ཕྱིར་སྤྱོད་ཡུལ་ཐོབ་པའི་དགེ་སློང་དགེ་འདུན་གྱི་དགག་དབྱེ་བལྟ་བར་བྱའོ༌[^3415]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4860]
དབྱར་གྱི་ནང་དུ་བྱ་བས་འགྲོ་དགོས་ན་དགག་དབྱེ་བྱའོ་ཞེས་བྱ་བ་ནི་ཁས་བླངས་པ་བསལ་བར་གྱུར་པ་དེའི་ངོ་བོ་ཅུང་ཟད་སྐྱེས་པར་གྱུར་ན་གནས་པའི་ཕྱིར་མི་རིགས་པ་དབྱར་རལ་བ་རིགས་པའི་བྱ་བ་དེས་འགྲོ་བར་བྱེད་ཅིང་རང་དགར་འགྲོ་བ་མ་ཡིན་ཏེ། གལ་ཏེ་དབྱར་གྱི་ནང་དུ་དགག་དབྱེ་བྱེད་པ་ལ་མི་རིགས་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4861]
འདིར་གཞུང་ནི་བཙུན་པ་འདི་ལྟར་དགེ་སློང་ཁྲིམས་ལུགས༌[^3416]སུ་བགྱི་བ༌[^3417]འདི་ལྟ་བུ་བགྱིས༌[^3418]ན་དབྱར་གནས་པར་ཁས་ལེན་པར་བགྱིད་དོ། །

[Block 4862]
ཚེ་དང་ལྡན་པ་བདག༌[^3419]གལ་ཏེ་བདག་དབྱར་གྱི་ནང་དུ་ཉེ་དུའི་གན་དུ་འགྲོ་བའི་དགག་དབྱེ་སྦྱིན་པ་ལྟ༌[^3420]ན། བདག་དབྱར་གནས་པར་ཁས་ལེན་ཏོ་ཞེས་འཆི༌[^3421]ན། བཙུན་པ། དགག་དབྱེ་སྩལ་བར་བགྱི་འམ།[^3422] ཉེ་བ༌[^3423]འཁོར་སྦྱིན་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4863]
དེ་ལ་རྒྱུ་མཚན་མེད་པར་དབྱར་རལ་བར་མི་རིགས་ཏེ། ཉེ་དུའི་དྲུང་དུ་འགྲོ་བ་རྒྱུ་མཚན་གཅིག་པུར་ནི་མ་ཟད་དེ་རིགས་པ་མེད་པར་ཡང་དབྱར་གྱི་ནང་དུ་དགག་དབྱེ་མ་བྱས་པ་ཉིད་ལ་དགེ་འདུན་གྱི་ཁྲིམས་སུ་བྱ་བ་མི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 4864]
དེ་ལྟ་བས་ན་ཇི་ལྟར་ཆོ་ག་འདི་ལ་སྐྱེད་པ༌[^3424]མ་ཡིན་པ་དེ་བཞིན་དུ་རྣམ་པར་གཞག་པ༌[^3425]རིགས་སོ། །

[Block 4865]
རྣམ་པ་གསུམ་གྱིས་མདོར་བྱས་པ་གནས་ཏེ། དེའི་ཕྱིར་འདི་ལྟར་མདོར་བྱས་སོ། །

[Block 4866]
གཞི་འམ་གང་ཟག་གམ་གཉིས་ཀ་བཞག་ནས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དགག་དབྱེ་བྱར་རུང་སྟེ་གཞིའི་སྒྲས་ནི་ལྟུང་བ་ཞེས་སྨོས་སོ། །

[Block 4867]
ཕམ་པར་འགྱུར་བ་ལས་ལྟུང་བྱེད་ཀྱི་སྡེ་ཚན༌[^3426]གཞན་དུ་གཞག་པའོ། །

[Block 4868]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི། གལ་ཏེ་དགེ་འདུན་ལྷག་མ་ཤེས་ན་བྱིན་གྱིས་བརླབས་ཏེ་དགག་དབྱེ་བྱའོ། །

[Block 4869]
ཕམ་པར་འགྱུར་བར་ཤེས་ན་ནི་བསྙིལ་བར༌[^3427]གསུངས་པས་བསྙིལ༌[^3428]ཏེ་དགག་དབྱེ་བྱའོ། །

[Block 4870]
དེ་ལས་གཞན་པ་དག་ཤེས་ན་ནི་བཤགས་ཏེ་དགག་དབྱེ་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
