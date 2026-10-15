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
[Block 3081]
ཡོངས་སུ་སྦྱོང་བའི་གཞིའོ།། །།

[Block 3082]
ཤེས་པ་དུ་མ་ཉིད་ཡིན༌[^2978]ན་གླེང་བ་ལ་སོགས་པ་ལ་འདོད་པས་སོ་ཞེས་བྱ་བ་ནི་ཤེས་པའི་དགེ་སློང༌[^2979]དུ་མ་ཉིད་ཡིན་ན་དེ་ལ་གླེང་བ་དང་དྲན་པར་བྱ་བ་དང་སྐབས་འབྱེད་དུ་གཞུག་པ་ལ་སོགས་པ༌[^2980]དེ་དག་རྒན་རིམ་གྱིས་འཇུག་པར་བྱ་བ་མ་ངེས་ཀྱིས་གླེང་བར་བྱ་བ༌[^2981]འདོད་པས་ཅི་དགར་འཇུག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3083]
འདིར་གཞུང་ནི་བརྫུན་དུ་སྨྲ་བའི་ལྟུང་བྱེད་ཀྱི་ཞུ་བ་ལས།

[Block 3084]
བཙུན་པ་དགེ་སློང་གི་དགེ་འདུན་གྱི༌[^2982]དབུས་སུ་བསླབ་པ་ལས་འདའ་བར་བགྱིད་ན་སུས་གླེང་བར་བགྱི། གང་འདོད་པས་སོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 3085]
དགག་དབྱེ་མ་ཡིན་པར་དེ་གཞག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགག་དབྱེའི་ལས་ཀྱི་དུས་མ་ཡིན་པ༌[^2983]གཞན་དུ་དགག་དབྱེ་དེ་གཞག་པར་མི་བྱའོ། །

[Block 3086]
གསོ་སྦྱོང་མ་ཡིན་པར་དེ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་གི་ལས་ཀྱི་དུས་མ་ཡིན་པར་གཞན་དུ་གསོ་སྦྱོང་དེ་གཞག་པར་མི་བྱའོ། །

[Block 3087]
འཇོག་པར་བྱེད་པ་བུད་མེད་ཉིད༌[^2984]ཀྱིས་གཞན་སྐྱེས་པའི་གཞག་པ་ཉིད་བྱེད་དམ་བྱས་པ་ཉིད་ན་གཞག་པ་ཉིད༌[^2985]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་དག་འཇོག་པར་བྱེད་པ་ཉིད་དམ་གཞག་པར་བྱས་པ་ཉིད་ཀྱི་འོག་ཏུ་གལ་ཏེ་མཚན་དེ་བུད་མེད་དུ་གྱུར་པ་ཉིད་ཀྱིས་འཇོག་པར་བྱེད་པ་བུད་མེད་ཡིན་ལ། ཅིག་ཤོས་སྐྱེས་པ་ཡིན་པར་གྱུར་ན་དེ་ལ་འཇོག་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་གཞག་པ་ཉིད་མ་ཡིན་ཏེ། དེ་ལྟ་ན་མི་འབྱུང་བ་ཁོ་ན་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3088]
སྐྱེས་པས་བུད་མེད་ཀྱི་འཇོག་པ་ནི་འབྱུང་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 3089]
མི་འབྱུང་བས་རྗེས་སུ་འཇུག་པ་མེད་དོ། །

[Block 3090]
དེ་ལྟ་བས་ན་བུད་མེད་ཀྱིས་འཇོག་ཏུ་བཅུག་ན་སྐྱེས་པ་ཉིད་དུ་གྱུར་ཀྱང་གཞན་པ༌[^2986]ཉིད༌[^2987]དགག་དབྱེའི་གཞི་ཞུ་བ་ལས།

[Block 3091]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས༌[^2988]དགེ་སློང་གི་དགག་དབྱེ་འཇོག་པར་བགྱིད་ཅིང་གང་གིས་བགྱི་བ་དེ་མཚན་གྱུར་ཏེ་དགེ་སློང་མར་གྱུར་ན་གཞག༌[^2989]པར་བགྱིའམ། ཉེ་བ༌[^2990]འཁོར་གཞག་པར་བརྗོད་པར་བྱའོ། །

[Block 3092]
འཇོག་པར་བགྱི་པ༌[^2991]གང་ལགས་པ༌[^2992]དེ་མཚན་གྱུར་ཏེ། དགེ་སློང་མར་གྱུར་ན་གཞག་པར་བརྗོད་པར་བགྱིའམ། ཉེ་བ༌[^2993]འཁོར་གཞག་པར་བརྗོད་པར་མི་བྱའོ། །

[Block 3093]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་མས་དགེ་སློང་མའི་དགག་དབྱེ་འཇོག་པར་བགྱིད་ཅིང་གང་གིས་འཇོག་པར་བགྱིད་པ་དེ་མཚན་གྱུར་ཏེ་དགེ་སློང་དུ་གྱུར་ན་གཞག་པར་བརྗོད་པར་བགྱིའམ། ཉེ་བ༌[^2994]འཁོར་གཞག་པར་བརྗོད་པར་མི་བྱའོ། །

[Block 3094]
འཇོག་པར་བགྱིད་པ་གང་ལགས༌[^2995]པ་དེ་མཚན་གྱུར་ཏེ་དགེ་སློང་དུ་གྱུར་ན་གཞག་པར་བརྗོད་པར་བགྱིའམ། ཉེ་བ༌[^2996]འཁོར་གཞག་པར༌[^2997]བརྗོད་པར་བྱའོ། །

[Block 3095]
དེ་བཞིན་དུ་དགེ་སློང་དང་དགེ་སློང་མས་དགག་དབྱེ་བྱེད་པ་ལ་ཡང་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3096]
རང་བཞིན་དུ་ཉམས་པས་ཀྱང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨྱོན་པ་ལ་སོགས་པས་གཞག་པ་ཉིད་ཀྱང་གཞག་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 3097]
ཚུལ་ཁྲིམས་མེད་པ་དང་གཅིག་པ་ཉིད་མ་ཡིན་པས་ཀྱང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཉམས་པའམ་རྣམ་པ་ཐམས་ཅད་དུ་གང་ལ་ཚུལ་ཁྲིམས་མེད་པ་དེ་ནི་ཚུལ་ཁྲིམས་མེད་པའོ། །

[Block 3098]
ཆོས་དང་ཆོས་མ་ཡིན་པའི་ཕྱོགས་སུ་གྱུར་པ་ཕན་ཚུན་བློ་གཅིག་པ་ཉིད་མ་ཡིན་པ་དེ་གཉིས་ཀྱིས་གཞག་པ་ཉིད་ཀྱང་གཞག་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 3099]
གཅིག་པ་ཉིད༌[^2998]མ་ཡིན་པའི་གཞུང་ནི་དགག་དབྱེའི་ཞུ་བ་ལས།

[Block 3100]
བཙུན་པ་རེ་ཞིག་ཁས་བླངས་པ་དག་གིས་ཁས་མ་བླངས་པ་དག་གི་དགག་དབྱེ་འཇོག་པར་བགྱིད་ན་གཞག་པར་བརྗོད་པར་བགྱིའམ། ཉེ་བ༌[^2999]འཁོར་གཞག་པར་བརྗོད་པར་མི་བྱའོ། །

[Block 3101]
བཙུན་པ་རེ་ཞིག་ཁས་མ་བླངས་པ་དག་གིས་ཁས་བླངས་པ་དག་གི་དགག་དབྱེ་འཇོག་པར་བགྱིད་ན་གཞག་པར་བརྗོད་པར་བགྱི་འམ། ཉེ་བ༌[^3000]འཁོར་གཞག་པར་བརྗོད་པར༌[^3001]མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3102]
དེ་གཉིས་ཀྱིས་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རང་བཞིན་ཉམས་པ་སྨྱོན་པ་ལ་སོགས་པ་ཞེས་བྱ་བ་དེ་དང་ཚུལ་ཁྲིམས་མེད་པ་དང་གཅིག་པ་ཉིད་མ་ཡིན་པས་གཞག་པ་ཉིད་ཀྱང་གཞག་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 3103]
ཡང་ཅིའི་ཕྱིར་གསོ་སྦྱོང་གཞག་པའི་གཞི་འདིའི་མིང་ཡོངས་སུ་སྦྱང་བའི་གཞི༌[^3002]ཞེས་གཞན་དུ་བྱས་ཤེ་ན། གཞི་འདིས་གདམས་ངག་གཞག་པ་དང་ཕུར་པ་དང་བཅས་པ་ལ་སོགས་པས་ལས་ཀྱིས་སྦྱང་བར་བྱ་བ་ཐམས་ཅད་བསྡུས་པ༌[^3003]ཡིན་གྱི། གསོ་སྦྱོང་གཞག་པ་འབའ་ཞིག༌[^3004]ཏུ་མ་ཟད་པས་ཞེས་བྱ་བ་འདི་སྒྲུབ་པས་དེ་ཤེས་པར་བྱའོ། །

[Block 3104]
རྣམ་པ་ཐམས་ཅད་དུ་མིང་དུ༌[^3005]གཞན་དུ་བྱས་པ་ནི་བཞི་པོ༌[^3006]ལ་ཡང་ཡོངས་སུ་སྦྱང་བའི་གཞི་ཞེས་པ་བདེ་བར་གཏོགས་པའི་དོན་དུའོ། །

[Block 3105]
ཡོངས་སུ་སྦྱང་བའི་གཞི་ཞུ་བའི་སྐབས་སོ། །

[Block 3106]
ཡོངས་སུ་སྦྱང་བའི་གཞི་རྫོགས་སོ།། །།

[Block 3107 [HEADING]]
## ལས་བྱེ་བའི་གཞི། ^10-0

[Block 3108]
དགེ་འདུན་ཐ་དད་པ་ཉིད་དུ་ནུས་པ་ལ་མི་འདོད་པར་གླེང་བ་དང་། གླེང་བར་བྱེད་པ༌[^3007]ན་ལོག་པར་མི་བྱའོ། །

[Block 3109]
འདའ་བར་བྱ་བ་གང་ན་མི་མཐུན་པ་ཡོད་པ་དེ་དང་ལྷན་ཅིག་ཏུ་འཁོད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་གང་དུ་འདའ་བར་བྱེད་པ་ནི་འདའ་བར་བྱེད་པའོ། །

[Block 3110]
འཐབ་ཀྲོལ་གྱི་སྐབས་བཅད་པའི་ཕྱིར་འདི་བཅའ་བ་མཛད་དོ། །

[Block 3111]
གཞན་དུ་ན་གོ་གཉིས་སམ་གསུམ་གྱི༌[^3008]བར་དུ་བཅད་དེའོ་ཞེས་བྱ་བ་ཡང་གནས་གང་ན་གང་ཟག་མི་མཐུན་པ་ཡོད་པ་དེ་དང་ལྷན་ཅིག་ཏུ་འདའ་བར་བྱེད་པ་ལས་གཞན་ལ་གོ་གཉིས་སམ་གསུམ་གྱི་བར་དུ་བཅད་དེ་སྟན༌[^3009]ལ་འཁོད་པར་བྱའོ། །

[Block 3112]
འདི་ནི་ལུས་ཀྱིས༌[^3010]ཕ་རོལ༌[^3011]གནོན་པ་དང༌[^3012]དེ་དང་དེ་རེག་པ་སྤང་བའི༌[^3013]ཕྱིར་རོ། །

[Block 3113]
འདའ་བར་བྱ་བ་ལ་ཡང་ལངས་ནས་དེ་ལ་ཕ་རོལ་གནོན་པའི་ཕྱིར་སྦྱོར་བ་ཞེས་བྱ་བ་དེར་དེ༌[^3014]མི་གནང་བའོ། །

[Block 3114]
དེས་ཅིག་ཤོས་དང་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ཡང་འདིར་གང་ཞིག་གང་ལ་ཞེས་བྱ་བའི་ཡུལ་ཉིད་ཀྱིས་སྨོས་པ་དེས་ཀྱང་དེ་དང་ལྷན་ཅིག་ཏུ་འཁོད་པར་མི་བྱ་བ་དང་དེ་ནི་དེ་ལྟ༌[^3015]ཉིད་དུ་བསྡུས་པ་སྟེ། གཉིས་སམ་གསུམ་གྱིས་བཅད་དེ་འཁོད་པར་བྱའོ། །

[Block 3115]
འདི་ནི་ལུས་ཀྱི་ལས་དེ་གལ་ཏེ་ཡང་འདི་ལ་མི་མཐུན་པ་དེས་ཀྱང་འགྲོགས་བཤེས་ཉིད་མ་ཡིན་པ་དེ་ལྟ་ན་ཡང་ལྟུང་བ་སྤང་བའི་ཕྱིར། དེ་གཉིས་ཀྱི༌[^3016]གཙུག་ལག་ཁང་བར་དུ་ཆོད་པ་སྦྱིན་པར་བྱ་བ་ཉིད་དང་མནོད་པ༌[^3017]བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མི་མཐུན་པ་དང་། ཅིག་ཤོས་དེ་གཉིས་ཀྱི་གཙུག་ལག་ཁང་ཞེས་བྱ་བ་གནས་པའི་གཞི་གཡོགས་པ་འམ། མ་གཡོགས་པ༌[^3018]བསྒྲུབ་པར་བྱ་བའི་དོན་དུ་གནས་ཁང་གིས་བར༌[^3019]དུ་ཆོད་པ་གནས་ཁང་བསྐོ་བས་ཀྱང་སྦྱིན་པར་བྱ་བ་ཉིད་ཡིན་ལ་རང་གིས་ཀྱང་མནོད་པར༌[^3020]བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 3116]
འདིར་སྦྱིན་པ་པོ་དང་མནོད་པ༌[^3021]པོས་ཀྱང་གཞན་དུ་བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་ལྟུང་བ་དང་ལྡན་པར༌[^3022]རིག་པར་བྱའོ། །

[Block 3117]
དགེ་འདུན་ཐམས་ཅད་ཀྱིས་གྲོས་བྱས་སམ་ལས༌[^3023]སུ་སྩལ༌[^3024]ཏེ་དེར་གནས་ཁང་སྦྱིན་པར་བྱེད་ན་ཡང་ཐམས་ཅད་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 3118]
འདིར་གནས་ཀྱི་གཞི་གཡོགས་པ་ནི་གཙུག་ལག་ཁང་ངོ་། །ཆོས་དང་འདུལ་བ་ལ་གལ་ཏེ་དེ་དང་ལྡན་པར་ཤེས་ནས་ཆོས་མ་ཡིན་པ་ལ་མངོན་པར་ཞེན་པ་ལ་དགེ་འདུན་མཐུན་པ་མེད་དོ་ཞེས་བྱ་བ་ལ་ཆོས་དང་ཞེས་བྱ་བ་ནི་དངོས་པོར་གཏོགས་པ་དང་སྤྱོད་པར་གཏོགས་པའི་ཆོ་གའོ། །

[Block 3119]
འདུལ་བ་ཞེས་བྱ་བ་ནི་བྱ་བ་དང་བྱ་བ་མ་ཡིན་པ་དག་ལ་བྱས་པ་དང་མ་བྱས་པ་ཉིད་དོ། །

[Block 3120]
དེ་དང་ལྡན་པར་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཆོས་དང་འདུལ་བའི་རྣམ་པ་ལ་མི་མཐུན་པ་ཉིད་དང་ལྡན་པའོ། །
--- END BLOCKS ---
