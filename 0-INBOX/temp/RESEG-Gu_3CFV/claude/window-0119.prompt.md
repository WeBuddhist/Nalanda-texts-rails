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
[Block 4166]
མཚན་མོ་གཅིག་ཆད་པ་དང་། གཞན་དུ་གསོ་སྦྱོང་ཞེས་བྱ་བ་འདིས་བསྟན་པའི་དོན་དུ་ཟླ་བ་ངོ་དེའི་ཚེས་གྲངས་གང་ལ་མཐར་ཐུག་པ་ལ༌[^2887]དེང་དགེ་འདུན་གྱི་གསོ་སྦྱོང་བཅུ་བཞི་པ་ལགས་ཏེ། བདག་དགེ་སློང་མིང་འདི་ཞེས་བགྱི་བའི་གསོ་སྦྱོང་བཅུ་བཞི་པ་ལགས་པས་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 4167]
དེ་ཡང་མཚན་མོ་གཅིག་ཆད་པས་དེ་གསོ་སྦྱོང་ཞེས་བྱ་བ་བསྟན་པའི་དོན་དུའོ། །

[Block 4168]
ཟླ་བ་ཕྱེད་ཕྱེད་ཅེས་བྱ་བའི་ལན་གཉིས་སུ་སྨྲ་བ་ནི་འདིར་ཟླ་བ་ཕྱེད་ཕྱེད་ཅེས་བྱ་བའི་དོན་དུའོ། །

[Block 4169]
སོ་སོར་ཐར་པའི་མདོ་གདོན་པས་སོ་ཞེས་བྱ་བ་ནི། འདིར་གསོ་སྦྱོང་གིས་ཚུལ་ཁྲིམས་གསོ་བར་བྱེད་པ་ཡོད་པས། དེ་དག་བཙལ་བའི་ཕྱིར་སོ་སོར་ཐར་པའི་མདོ་གདོན༌[^2888]པས་སོ། །

[Block 4170]
དྲན་པ་ཙམ་གྱིས་བྱས་པ་དང་། མ་བྱས་པ་ལ་སོ་སོར༌[^2889]བརྟག་པའོ། །

[Block 4171]
སེམས་དྲང་པོར་བསྒྲུབ་པ་དང་། བྱེ་བྲག་ཉེ་བར་བསྒྲུབ་པ་ལ་རྣམ་པར་ངེས་པ་ཀུན་ནས་ལྡང་བས་རང་གི་ངོ་བོ་དང་འབྲས་བུ་ལས་འདས་པར་བྱེད་ཅིང༌[^2890]ཐ་དད་པར་བྱེད་པ་རྣམས་ཀྱིས་ཚུལ་ཁྲིམས་ལའོ། །

[Block 4172]
དེ་ལྟར་རྣམ་པ་འདི་རྣམས་ཀྱིས་ཀྱང་ཚུལ་ཁྲིམས་གསོ་བར་བྱེད་པ་ཡོད་པས་བྱེ་བྲག་འདི་ཡོངས་སུ་བཟུང་བའོ། །

[Block 4173]
སོ་སོར་ཐར་པའི་མདོ་གདོན་པས་སོ་ཞེས་བྱ་བ་ནི། འདུལ་བར་གཏོགས་པ་མ་ལུས་པ་སྟོན་པ་དང་། མ་ལུས་པ་བསྟན་པའི་སྐབས་བཟློག་པའི་དོན་དུ་དགའ་བ་སྤྱོད་པ་འདི་ལ་ཞེས་བྱ་བ་རྒྱལ་བའི་བསྟན་པ་ལྷག་མ་རྣམ་པར་གཞག་པའོ། །

[Block 4174]
ཡང་ན་སླར་ཡང་། གཞན་དག་ཆོས་དང་རྗེས་སུ་མཐུན་པ་འོངས་པར་གྱུར་ནའོ། །

[Block 4175]
དེར་ཁྱེད་ཅག་གིས་བཅས་པ་དང་རྗེས་སུ་བཅས་པ་ལས་ཡང་དག་པར་དགའ་བར་གྱུར་པ་དང་རྗེས་སུ་བསྟན་པར་གྱུར་པ་རྣམས་ཀྱིས་བསླབ་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4176]
དགག་དབྱེ་བྱས་ན་འདི་མ་གྲུབ་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། དེས་དག༌[^2891]པར་སྤྱད་ནས་དེ་བྱིན་པས་གསོ་སྦྱོང་གི་ཚུལ་ཁྲིམས་རྒྱས་པར་བྱེད་པའོ། །

[Block 4177]
དགག་དབྱེ་བྱས་ནས་སླར་གསོ་སྦྱོང་མི་བྱའོ་ཞེས་བྱ་བ་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 4178]
དེ་གཉིས་ནི་ཚུལ་ཁྲིམས་དག་པར་བྱེད་པ་སྟེ། དེ་བས་ན་དགག་དབྱེ་བྱས་པས་གསོ་སྦྱོང་འགྲུབ་པ་ཉིད་དོ། །

[Block 4179]
འདིར་གཞུང་ནི།

[Block 4180]
ཕྲན་ཚེགས་དག་ལས།

[Block 4181]
དགེ་སློང་དག་དགག་དབྱེ་བྱས་ནས་གསོ་སྦྱོང་བྱེད་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགག་དབྱེ་བྱས་ནས་གསོ་སྦྱོང་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4182]
གསོལ་བ་དང་། རྣམ་པར་གཞག་པ་འཛིན་དུ་གཞུག་པ་སྔར་བྱ་ཞིང་དེ་གདོན་ཏོ་ཞེས་བྱ་བ་ནི་དང་པོར་གསོལ་བ་སྔོན་དུ་འགྲོ་བས་རྣམ་པར་གཞག་པས་འཛིན་དུ་གཞུག་པར་བྱས་ནས་དེའི་རྗེས་ལ་སོ་སོར་ཐར་པའི་མདོ་གདོན་པའོ། །

[Block 4183]
རྣམ་པར་གཞག་པ་འཛིན་དུ་གཞུག་པ་ནི་སོ་སོར་ཐར་པའི་མདོ་ལས་ཚེ་དང་ལྡན་པ་དག་བདག་ཅག་གསོ་སྦྱོང་བྱ་སྟེ། སོ་སོར་ཐར་པའི་མདོ་གདོན་པ་གདོན་གྱིས་ཁྱེད་ཅག་སུ་ལ་ལྟུང་བ་ཡོད་པ་ཅེས༌[^2892]མཐོལ་ཅིག་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 4184]
གླེང་གཞི་གདོན་པ་དང་གསོལ་བ་ནི་ཚིག་ཏུ་བརྗོད་པ་ཉིད་ཀྱིས་བསྒྲུབ་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། འདི་གཉིས་ནི་ཚིག་ཏུ་བརྗོད་པ་ཉིད་ཀྱིས་བསྒྲུབ་པར་བྱ་བ་ཉིད་ཡིན་གྱི། ཐོས་པ་བསྒྲགས་པས་བསྒྲུབ་པར་བྱ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 4185]
ལྷག་མ་ནི་ཐོས་པ་བསྒྲུབས་པས༌[^2893]ཀྱང་ངོ་ཞེས་བྱ་བ་ནི། གླེང་གཞི་གདོན་པ་དང་། གསོལ་བའི་ལྷག་མ་དག་འདི་ཐོས་པ་བསྒྲགས་པས་བསྒྲུབ་པར་བྱ་བ་རུང་བ་ཉིད་ཡིན་ནོ། །

[Block 4186]
ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་ཚིག་ཏུ་བརྗོད་པ་བསྒྲུབ་པར་བྱ་བ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4187]
བརྩམས་པའི་སྡེ་ཚན་ནི་རྫོགས་པར་བྱ་དགོས་སོ་ཞེས་བྱ་བ་ནི། ཕམ་པར༌[^2894]གྱུར་པའི་སྡེ་ཚན་ལ་ཅུང་ཟད་བཏོན་ནས་ལྷག་མ་དེ་དག་དང་ལྡན་པར་རྟོགས་པ་ནི་ཐོས་པ་བསྒྲགས་པས་ཞེས་བྱ་བའི་དེ་ནི་མི་བྱའོ། །

[Block 4188]
དེ་བཞིན་དུ༌[^2895]དགེ་འདུན་ལྷག་མའི་སྡེ་ཚན་དང་མ་ངེས་པའི་སྡེ་ཚན་ལས་ཀྱང་མི་བྱའོ། །

[Block 4189]
དེ་ལྟར་འཕྲོག༌[^2896]འཇོག་པ་ཉིད་སྐྱེ་བར་འགྱུར་ཏེ། འཕྲོག༌[^2897]འཇོག་པ་ནི་དམན་པར་བྱ་བ་ཉིད་དོ། །

[Block 4190]
བཞི་པ་ལ་རེག་ན་རིལ་གྱིས་སོ་ཞེས་བྱ་བ་ནི། ལྟུང་བྱེད་ཀྱི་བདག་ཉིད་ཀྱི་སྡེ་ཚན་བཞི་པ་ལས་རེག་ན་ཐམས་ཅད་རྫོགས་པར་བྱའོ། །

[Block 4191]
སོ་སོར་བཤགས་པར༌[^2898]བྱ་བ་ལ་སོགས་པ་ལ་ཡང་འདིར་ཐོས་པ་བསྒྲགས་པར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4192]
བྱས་པ་ཐོབ་པ་ལ་མཐར་ཐུག་པ་མ་ཡིན་པ་གཏོང་བ་ལེགས་པ་ཉིད་དུ་ཡིད༌[^2899]ལ་ངེས་པར་འབྲེལ་བ་མ་ཡིན་ཏེ། དེ་བས་ན་འདི་རྣམ་པར་གཞག་པའོ། །

[Block 4193]
སོ་སོར་ཐར་པའི་མདོ་གདོན་པ་ལྔ་པོ་འདི་རྣམས་ལ་གླེང་གཞི་ཚིག་ཏུ༌[^2900]བརྗོད་པས་བཏོན་ནས་ལྷག་མ་བསྒྲགས་པས་བསྒྲུབ་པར་བྱར་རུང་ངོ་། །དེ་བཞིན་དུ་ཕམ་པར་འགྱུར་བ་རྣམས་སམ། དགེ་འདུན་ལྷག་མ་རྣམས་སམ། མ་ངེས་པ་དག་ཏུ་ཚིག་ཏུ་བརྗོད་པས་བཏོན་ནས༌[^2901]ལྷག་མ་ཐོས་པ་བསྒྲགས༌[^2902]པས་བསྒྲུབ༌[^2903]ཏུ་ཡང་རུང་བ་ཡང་ལྔ་པའོ། །

[Block 4194]
འདི་ལ་ཟླ་བ་ཕྱེད་འདས་པའི་སོ་སོར་བརྟག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་ལའོ། །

[Block 4195]
ཟླ་བ་ཕྱེད་འདས་པའི་ཉེས་པ་དག་ལ་ཅི་བྱུང་བ་དེ་དག་སོ་སོར་བརྟག་པར་བྱའོ། །གང་གི་ཚེ་ཞེ་ན། འདུ་བར་འགྱུར་བ་དེར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་རྣམས་སོ་སོར་ཐར་པའི་མདོ་གདོན་པའི་ཕྱིར་འདུ་བ་གང་ཡིན་པ་དེ་འདུ་བའི་མདུན་རོལ་དུ་འདུ་བ་ལ་སྦྱོར་བའི་ཚེ། ལྷག་མ་ནི་ཚོགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4196]
ཅི་སོ་སོར་བརྟགས་ནས་ལྟུང་བ་ཕྱིར་མ་བཅོས་པ་ཁོ་ནར་འདུག་པར་བྱ་བའམ་ཞེ་ན། དེའི་ཕྱིར༌[^2904]ཤེས་པ་ཕྱིར་བཅོས་ཏེ་ཐམས་ཅད་དུ་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྟུང་བ་ངེས་པར་ཤེས་པའམ། ཡིད་གཉིས་དང་བཅས་པ་ཤེས་པ་ཕྱིར་བཅོས་ཏེ། དགག་དབྱེ་ལ་སོགས་པའི་ལས་ཐམས་ཅད་འདུག་པར་བྱའོ། །

[Block 4197]
གསོ་སྦྱོང་ཉིད་ལ་ཡིད་གཉིས་ཀྱིས་ནི་མ་ཡིན་ཏེ། དེ་ལ་དགེ་སློང་མདོ་སྡེ་དང་འདུལ་བ་དང་མ་མོ་འཛིན་པ་རྣམས་ལ་དྲིས་ནས་ཡིད་གཉིས་དང་བྲལ་པར་བྱས་ཏེ། ཕྱིར་བཅོས་པ་ཞེས་བྱ་བ་ནི་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 4198]
འདུག་པ་ན་དྲན་ནམ་ཡིད་གཉིས་ཟ་ན་དྲུང་ན་མོ་ལ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་དེར་འདུག་པ་འདི་ལ་ལྟུང་བའི་ཡུལ་ཅན་དྲན་པ་བཅོས་སུ་ཡོད་པར་གྱུར་ན། གང་ཞིག་དྲུང་ན་འདུག་པའི་དགེ་སློང་དེ་ལ་བྱིན་གྱིས་བརླབ་པར་བྱ་སྟེ། མདུན་ནས་བྱའི་གློ་ནས་མི་བྱའོ། །

[Block 4199]
དེ་ན་ངེས་པ་ལས་ཤེས་པའོ། །

[Block 4200]
[^2905]ཤིན་ཏུ་འདའ་བར་བྱེད་པས་དགོས་པ་མེད་པ་དེ་བས་ན་འདི་བརྟེན་པའོ། །

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
--- END BLOCKS ---
