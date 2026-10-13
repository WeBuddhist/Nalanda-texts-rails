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
[Block 3186 [VERSE]]
རྙེད་པ་ལ་སྲེད་ཆོག་མི་ཤེས། །
མ་རྙེད་ལ་འདོད་འདོད་ཆེན་ཅན། །

[Block 3187]
ཆོས་གོས་ལ་སོགས་པ་རྙེད་པ་ལ༌[^1252]ཡང་དང་ཡང་དུ་འདོད་པ་ནི་ཆོག་མི་ཤེས་པ་ཡིན་ལ། མ་རྙེད་པ༌[^1253]དག་ལ་དེ་འདོད་པ་ནི་འདོད་ཆེན་ཅན་ཡིན་ནོ། །

[Block 3188]
བཟློག་པ་དེ་ཡི་གཉེན་པོ་དག །ཆོག་ཤེས་པ་དང་འདོད་པ་ཆུང་བ་དག་གོ། །

[Block 3189]
དེ་གཉིས་ཁམས་གསུམ་གཏོགས་དྲི་མེད། །དེའི་གཉེན་པོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཆོག་མི་ཤེས་པ་དང་། འདོད་ཆེན་ཅན་ནི་འདོད་པ་ན་སྤྱོད་པ་ཁོ་ན་འདོད་ཆེན་ཆུང་བ་དང་། ཆོག་ཤེས་པ་འདི་གཉིས་ཀྱི་རང་བཞིན་ཅི་ཞེ་ན། མ་ཆགས་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་དག་ནི་མ་ཆགས་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 3190]
འཕགས་རིགས། མ་ཆགས་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདི་དག་ལས་འཕགས་པ་རྣམས་སྐྱེ་བས་ན་འཕགས་པའི་རིགས་བཞིའོ། །

[Block 3191]
དེ་དག་ལས།

[Block 3192 [VERSE]]
གསུམ་ནི་ཆོག་ཤེས་བདག་ཉིད་དོ། །
དང་པོ་གསུམ་པོ་ཆོས་གོས་དང་། །

[Block 3193]
བསོད་སྙོམས་དང་། མལ་སྟན་གྱིས་ཆོག་ཤེས་པའོ། །

[Block 3194]
འཕགས་པའི་རིགས་བཞི་པ་ནི་སྤོང་བ་དང་བསྒོམ་པ་དག་ལ་དགའ་བ་ཉིད་ཡིན་ནོ། །

[Block 3195]
བཅོམ་ལྡན་འདས་ཀྱིས་འཕགས་པའི་རིགས་བཞིས་ཅི་ཞིག་བསྟན་ཞེ་ན། གསུམ་གྱིས་ཚུལ་བསྟན་ཐ་མ༌[^1254]ལས། །

[Block 3196]
རང་གི་ཚུལ་དང་ལས་ཀྱི་མཐའ་ཡོངས་སུ་སྤངས་པ་དག་ལ་གཉིས་བཅས་ཏེ། གསུམ་གྱིས་ནི་ཚུལ་དང་། བཞི་པས་ནི་ལས་སོ། །

[Block 3197]
བཅས་པ་དེ་ཡང་། སྲེད་པ་སྐྱེ་བའི་གཉེན་པོའི་ཕྱིར། །སྲེད་པ་སྐྱེ་བ་བཞི་སྟེ། ཆོས་གོས་ལ་སོགས་པ་གསུམ་དང་། སྲེད་པ༌[^1255]མེད་པ་ལ་བཞི་པའོ། །

[Block 3198]
དེ་དག་གི་གཉེན་པོར་འཕགས་པའི་རིགས་བཞི་བསྟན་ཏེ།

[Block 3199 [VERSE]]
བདག་གིར་བདག་འཛིན་དངོས་འདོད་པ། །
དེ་ཡི་དུས་དང་གཏན་བཞིའི་ཕྱིར། །

[Block 3200]
བདག་གིར་འཛིན་པའི་དངོས་པོ་ནི་ཆོས་གོས་ལ་སོགས་པའོ། །

[Block 3201]
བདག་ཏུ་འཛིན་པའི་དངོས་པོ་ནི་ལུས་སོ། །

[Block 3202]
དེ་དག་ལ་འདོད་པ་ནི་སྲེད་པའོ། །

[Block 3203]
དེ་ལ་བདག་གིར་འཛིན་པའི་དངོས་པོ་ལ་འདོད་པ་དེའི་དུས་སུ་ཞི་བར་བྱེད་པ་གསུམ་མོ།[^1256] །

[Block 3204]
གཉིས་ཀ་ལ་འདོད་པ་གཏན༌[^1257]དུ་ཞི་བར་བྱེད་པ་ནི་བཞི་པའོ། །

[Block 3205 [HEADING]]
#### འཇུག་པའི་སྒོ་གཉིས། ^6-1-4-0

[Block 3206]
དེ་ལྟར་སྣོད་དུ་གྱུར་པ་དེ་ཇི་ལྟར་ན་བསྒོམ་པ་དེ་ལ་འཇུག་པ་ཡིན་ཞེ་ན།

[Block 3207 [VERSE]]
དེ་ལ་འཇུག་པ་མི་སྡུག་དང་། །
དབུགས་རྔུབ་འབྱུང་བ་དྲན་པ་ཡིན།[^1258] །
འདོད་ཆགས་རྣམ་རྟོག་ལྷག་རྣམས་སོ། །

[Block 3208]
གང་ཞིག་འདོད་ཆགས་ཉེ་བ་དང་ཤིན་ཏུ་སྤྱད་པ་དེ་ནི་མི་སྡུག་པས་འཇུག་གོ། །

[Block 3209]
གང་ཞིག་རྣམ་པར་རྟོག་པ་སྤྱད་པ་དེ་ནི་དབུགས་རྔུབ་པ་དང་འབྱུང་བ་དྲན་པས་འཇུག་གོ། །

[Block 3210 [HEADING]]
##### མི་སྡུག་པ། ^6-1-4-1-0

[Block 3211]
དེ་ལ་འདོད་ཆགས་ནི་རྣམ་པ་བཞི་སྟེ། ཁ་དོག་གི་འདོད་ཆགས་དང་། དབྱིབས་ཀྱི་འདོད་ཆགས་དང་། རེག་པའི་འདོད་ཆགས་དང་། བསྙེན་བཀུར་གྱི་འདོད་ཆགས་སོ། །

[Block 3212]
དེ་དག་ལ་བྱེ་བྲག་མེད་པར་ཤིས་པ་ནི། ཀེང་རུས་ཆགས་བཅས་ཐམས་ཅད་ལ། །རུས་པའི༌[^1259]ཀེང་རུས་ལ་ནི་ཆགས་པའི་བཞི༌[^1260]རྣམ་པ་བཞི་པོ་འདི་དག་ཐམས་ཅད་མེད་དོ། །

[Block 3213]
དེ་ཡང་མི་སྡུག་པ་བསྒོམ་པའི་རྣལ་འབྱོར་སྤྱོད་པ་དེ་ནི་རྣམ་པ་གསུམ་དུ་བརྗོད་དེ། ལས་དང་པོ་པ་དང་། ཡོངས་སུ་སྦྱང་བ་བྱས་པ་དང་། ཡིད་ལ་བྱེད་པ་རྫོགས་པའོ། །

[Block 3214]
དེ་ལ།

[Block 3215 [VERSE]]
རུས་པ་རྒྱ་མཚོའི་བར་དུ་ནི། །
སྤྲོ་ཞིང་སྡུད་པས་ལས་དང་པོ། །

[Block 3216]
མི་སྡུག་པ་བསྒོམ་པར་འདོད་པས་ནི་རང་གི་ཡན་ལག་ལ་སེམས་གཏོད་དེ། དེ་དེར་ཤ་མྱགས་ཤིང་ཟགས་པར་མོས་པ་ན༌[^1261]རིམ་གྱིས་རུས་པ་རྣམ་པར་སྦྱོང་བར་བྱེད་པས༌[^1262]ཐམས་ཅད་རུས་པའི་ཀེང་རུས་སུ་ལྟ་ཞིང་དེ་བཞིན་དུ་ཡང་གཉིས་པ་ལ་མོས་པ་བྱེད་པ་ནས། གཙུག་ལག་ཁང་དང་། ཀུན་དགའ་ར་བ་དང་། གྲོང་དང་། ཞིང་གི་བར་ནས་རིམ་གྱིས་རྒྱ་མཚོའི་མཐའ༌[^1263]ཀླས་པའི་བར་གྱི་ས་གཞི་རུས་པའི་ཀེང་རུས་ཀྱིས་གང་བར་མོས་པར་བྱེད་དོ། །

[Block 3217]
ཡང་མོས་པ་འཕེལ་བར་བྱ་བའི་དོན་དུ་ཡང་སྡུད་ན་སེམས་བསྡུ་བའི་ཕྱིར་ཀེང་རུས་གཅིག་བུ་ཁོ་ན་ལ་མོས་པའི་བར་དུ་སྡུད༌[^1264]དེ། འདི་ཙམ་གྱིས་ན་ལས་དང་པོ་པའི་རྣལ་འབྱོར་སྤྱོད་པ་ཡོངས་སུ་རྫོགས་པ་ཡིན་ནོ། །

[Block 3218 [VERSE]]
ཀེང༌[^1265]རུས་ནས་ནི་ཐོད་ཕྱེད་བར། །
བཏང་བས་སྦྱང་བ༌[^1266]བྱས་པར་བཤད།[^1267] །

[Block 3219]
དེ་ཡང་སེམས་བསྡུས་པ་ཁྱད་པར་དུ་བྱེད་པའི༌[^1268]ཕྱིར་རུས་པའི་ཀེང་རུས་དེ་ལས་རྐང་པའི་རུས་པ་རྣམས་བོར་ནས་ལྷག་མ་ཡིད་ལ་བྱེད་ཅིང་། དེ་བཞིན་དུ་རིམ་གྱིས་ཐོད་པའི་ཕྱེད་ཀྱི་བར་པོར་ནས་ཡིད་ལ་བྱེད་པ་འདི་ནི་ཡོངས་སུ་སྦྱང་བ་བྱས་པ་ཡིན་ནོ། །

[Block 3220 [VERSE]]
སྨིན་མའི་བར་དུ་སེམས་འཛིན་པས། །
ཡིད་ལ་བྱེད་པ་རྫོགས་པ་ཡིན། །

[Block 3221]
དེ་ཐོད་པའི་ཕྱེད་ཀྱང་བར༌[^1269]ནས་སྨིན་མ་གཉིས་ཀྱི་བར་དུ་སེམས་འཛིན་པ་འདི་ནི་ཡིད་ལ་བྱེད་པ་རྫོགས་པའོ། །

[Block 3222]
ཡང་མི་སྡུག་པ་འདིའི་རང་བཞིན་ཅི་ཞིག་ཡིན། ས་ནི་དུ་བ་ཞིག་ཡིན། དམིགས་པ་ནི་ཅི་ཞིག་ཡིན། གང་དུ་ནི་སྐྱེད་པར་བྱེད་ཅེ་ན། གོ་རིམས་བཞིན་དུ།

[Block 3223 [VERSE]]
མི་སྡུག་མ་ཆགས་ས་བཅུ་དང་། །
དམིགས་པ་འདོད་སྣང་མི་སྐྱེད་དོ། །

[Block 3224]
མི་སྡུག་པ་འདིའི་རང་བཞིན་ནི་མ་ཆགས་པའོ། །

[Block 3225]
ས་ནི་བཅུ་པ་སྟེ། བསམ་གཏན་བཞི་ཡི་ཉེར་བསྡོགས་དང་། །བསམ་གཏན་ཁྱད་པར་ཅན་དང་བཅས་པ་དང་། འདོད་པའི་ཁམས་ན་ཡོད་དོ། །
--- END BLOCKS ---
