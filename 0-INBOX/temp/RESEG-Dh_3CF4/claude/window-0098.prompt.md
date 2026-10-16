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
[Block 3431]
བསམ་གཏན་ལ་གཞོལ་བས་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་ཡིད་བསམ་གཏན་ལ་སྦྱོར་བས་གནས་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་པའོ། །

[Block 3432]
བྱ་བ་ངན་པ་དང་མ་འབྲེལ་ཞིང་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་བརྟུལ་ཞུགས་དང་། བཟླས་བརྗོད་དང་སྦྱིན་སྲེག་གི༌[^2203]ཆོ་ག་བྱེད་ཀྱི་ལས་གཞན་མི་བྱེད་པས་སོ། །

[Block 3433]
གདུང་བ་མེད་ལ་ཞེས་བྱ་བ་ནི་བསྟན་པའི་ལམ་ལ་དགའ་བར་སྟོན་ཏོ། །

[Block 3434]
རབ་ཏུ་ཞི་བ་ལ་མངོན་པར་དགའ་ཞིང་འཁོད་པར༌[^2204]ཞེས་བྱ་བ་ནི་སྤྱོད་ཡུལ་ལ་སོགས་པའི་གནས་པའོ། །

[Block 3435]
རྩོལ་བ་མེད་པར་ཞེས་བྱ་བ་འདིས་ནི་བྱ་བ་ངན་པ༌[^2205]མ་འབྲེལ་ཞིང་གདུང་བ་མེད་པ་རབ་ཏུ་ཞི་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 3436]
ཡོན་ཏན་རེ་བ་སྙིང་ལ་ཞེས་བྱ་བ་ནི་ཕྱི་རོལ་གྱི་འཇུག་པ་སྟོན་པའི་ཕྱིར་ཏེ། སྙིང་གི་ཡོན་ཏན་ལ་རེ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3437]
པདྨའི་རྩ་བའི་ཆ་དང་པོ་མི་སྣང་བར་བྱས་སོ་ཞེས་བྱ་བ་ལ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་མི་སྣང་བར་བྱས་པ་བསྟན་པའི་ཕྱིར། སྡུག་བསྔལ་བྱུང་བར་གྱུར་པ་ལ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་པ་ཡིན་ཏེ། བདེ་བ་སྡུག་བསྔལ་གཉིས་ཡོད་པ་དང་མེད་པར་གྱུར་ཀྱང་བྱང་ཆུབ་སེམས་དཔའ་ལ་ནི་བློ་དང་ལྡན་པའི་ཕྱིར་མི་སྣང་བར་བྱས་ཀྱང་མི་གཡོ་ཞིང་དེ་ལྟར་ཤེས་པར་འགྱུར་བས་སོ། །

[Block 3438]
དེ་ལྟར་མི་སྣང་བར་བྱས་པས་དེ་ལ་སེམས་འཁྲུགས་པས་ཤི་ཡང་སླ༌[^2206]ཞེས་བྱ་བ་ནི་སྐྱེ་བ་དུ་མར་མི་སྡུག་པའི་རྣམ་པར་སྨིན་པའི་རྒྱུར་འགྱུར་བའི༌[^2207]ཕྱིར་རོ། །

[Block 3439]
སེམས་འཁྲུགས་པ་ནི་ཚེ་ཟད་པ་ཡིན་ཏེ། ཚེ་ཟད་པ་དེའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3440]
སྲོག་གི་ཕྱིར་ཡང་ཞེས་བྱ་བ་ནི་སྲོག་གི་ཆེད་དུ་ཡང་ངོ་། །གལ་ཏེ་འཁྲུགས་ཤིང་གསོན་པར༌[^2208]རུང་ངོ་ཞེས་འགའ་ཞིག་སྨྲ་ན་ནི། དེའི་ཚེ་འཁྲུགས་པར་གྱུར་ན་དེ་མ་ཐག་འཆི་བ་ལྟ་བུ་སྟེ། འཆི་བར་ཉེ་བར་འགྲོ་བ་ཡིན་ཏེ། དེས་སེམས་འཁྲུགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3441]
དེས་ན་སེམས་འཁྲུགས༌[^2209]བཞིན་དུ་འཚོ་བ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3442]
འགྲམ་པ་དང་མིག་ནི་ཀོང་ཞེས་བྱ་བས་དབྱིབས་འགྱུར་བ་ཉིད་དོ། །

[Block 3443]
བཞིན་གྱི་མདངས་ནི་ངན་ཞེས་བྱ་བ་ནི་མདོག་འགྱུར་བའོ། །

[Block 3444]
སྐད་ཀྱི་གདངས་ཟབ་མོ་ནི་ཆུང་ཞེས་བྱ་བས་ནི་སྒྲ་འགྱུར་བའོ། །

[Block 3445]
ཉམ་དམས་ཀྱང་བརྟན་པ༌[^2210]དང་རབ་ཏུ་ཞི་བའི་ཡོན་ཏན་ཞེས་བྱ་བ་འདིས་ནི་རྣམ་པར་རིག་བྱེད་མ་འགྱུར་བར་བསྟན་ཏོ། །

[Block 3446]
དེ་ལྟར་ཕྱི་རོལ་གྱི་ཡུལ་གྱིས༌[^2211]མཐོང་བ་སྟེ། མིག་དང་རྣ་བའི་དབང་པོ་གཉིས༌[^2212]ཀྱིས་མདོག་དང་དབྱིབས་རྣམ་པར་རིག་པ་ཡིན་ནོ། །

[Block 3447]
རིད་པར༌[^2213]གྱུར་པའི་རྒྱུ་དེ་ལ་དྲིས་སོ་ཞེས་བྱ་བ་ནི་ཅིའི་ཕྱིར་རིད་པའི་རྒྱུ་དེ་ལ་དྲིས་ཤེ་ན། རིད་པ་དང་འབྲེལ་པར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3448]
འགྱུར་བ་གཞན་དག་ནི་མི་རིགས་པའི་ཕྱིར་ཏེ། དྲི་བ་གཞན་དག་ནི་མ་བརྗོད་ཀྱང་གྲུབ་པ་ཉིད་དེ། དེ་ལས་གཞན་དུ་འགྱུར་བའི་རྒྱུའོ། །

[Block 3449]
ཇི་ལྟར་གྱུར་པ་ཞེས་བྱ་བ་ནི་དང་པོའི་གནས་ན་པདྨའི་རྩ་བ་ནི་མེད་དེ། [^2214]པདྨའི་ལོ་མ་ནི་རྒྱན་འཁྲུགས་ཤིང་འདུག་པར་མཐོང་ཞེས་བྱ་བ་དེ་དག་བསྟན་པར་གྱུར་པའོ། །

[Block 3450]
ཆོས་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་པདྨའི་རྩ་བ་ཁྱེར་བའོ། །ཤེས་པ་འཇུག་པའི་ཡུལ་ཡང་བསྒྲིབས་ཞེས་བྱ་བ་ནི་ཤེས་པ་འཇུག་པ་ཡིན་པས་ཤེས་པ་འཇུག་པའོ། །ཤེས་པ་འཇུག་པར་བྱེད་པའི་ཡུལ་ནི་ཤེས་པ་འཇུག་པའི་ཡུལ་ལོ། །ཤེས་པ་འཇུག་པའི་ཡུལ་བསྒྲིབས་པ་གང་ཡིན་པ་དེ་ནི་ཤེས་པ་འཇུག་པའི་ཡུལ་བསྒྲིབས་པ་སྟེ། མངོན་པར་ཤེས་པ་ལས༌[^2215]བྱུང་བའི་ལྷའི་མིག་གིས་མཐོང་བའི་ཡུལ་དེ་བསྒྲིབས་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། བརྒྱ་བྱིན་གྱི་མཐུ་ལས་བྱུང་བའི་རྫུ་འཕྲུལ་གྱི༌[^2216]ཁྱད་པར་གྱིས་མངོན་པར་ཤེས་བ་ལས་བྱུང་བའི་མིག་གི་ཡུལ་ཡང་མི་སྣང་བར་བྱེད་ནུས་པས་སོ། །

[Block 3451]
ཅི་ལས་གྱུར་ཞེས་བྱ་བ་ནི་གང་གིས་འདི་ལྟར་བྱས་ཞེས་པའོ། །

[Block 3452]
འདི་ཞེས་བྱ་བ་ནི་པདྨའི་རྩ་བ་མེད་པའོ། །

[Block 3453]
རང་གི་ཡིད་ལ་གཅགས་པ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེ་ཉམ་ཐག་པའི་རྒྱུས་སོ། །

[Block 3454]
བདག་ཉིད་གཙང་བ་ཞེས་བྱ་བ་ནི་བདག་ཉིད་པདྨའི་རྩ་བ་མ༌[^2217]ཁྱེར་བའོ། །

[Block 3455]
འདིར་ཚིགས་བཅད་བཅུ་གཅིག་གིས་མནའ་ཁྱད་པར་ཅན་བོར་བ་སྟེ། རབ་དང་། འབྲིང་དང་། ཐ་མ་རྣམས་ཀྱི་འདོད་པའི་ཉེས་དམིགས་བསྟན་པའི་ཕྱིར་ཇི་ལྟར་རིགས་པར་སྦྱར་ཏེ།

[Block 3456]
དང་པོ་གསུམ་གྱིས༌[^2218]མནའ་ཁྱད་པར་ཅན་བོར་བ་ནི་ཐ་མའི་དབང་དུ་བྱས་པའོ། །

[Block 3457]
ཁྱོད་ཀྱི་རྩ་བ་བརྐམ་པས་གང་ཁྱེར་བ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི་རབ་ཀྱི༌[^2219]དབང་དུ་བྱས་པའོ། །

[Block 3458]
ཁྱོད་ལྟའི༌[^2220]རྩ་བ་གང་ཁྱེར་བ། །ཞེས་བྱ་བ་ནས། ཁྱོད་ལྟ་བུ་ཡི་རྩ་བ་ལ་ཆགས་གང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གསུམ་ནི་འབྲིང་གི་དབང་དུ་བྱས་པའོ། །

[Block 3459]
རྩ་བའི་ཕྱིར་ནི་བདག་ཉིད་ཆུད་གསོན་པ། ཞེས་བྱ་བ་དང་། གང་གིས་རྩ་བ་མཐོང་ལ་ཆོས་མ་མཐོང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ནི་ཐ་མའི་དབང་དུ་བྱས་པའོ། །

[Block 3460]
དམ་པའི་མཆོག་ཏུ་གྱུར་ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི་རབ་ཀྱི་གནས་སྐབས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 3461]
གནོད་སྦྱིན་དང་། གླང་པོ་ཆེ་དང་། སྤྲེའུ་རྣམས་ཀྱིས་ཀྱང་འདོད་པའི་ཉེས་དམིགས་བསྟན་པའི་ཕྱིར་ཏེ། དེ་དག་ནི་འདོད་ཆགས་དང་མ་བྲལ་བའི་ཕྱིར་གནས་སྐབས་དང་རྗེས་སུ་མཐུན་པའི་མནའ་གསུམ་བོར་བ་ཡིན་ནོ། །

[Block 3462]
གང་ཞིག་མ་བརླག་པར་ནི་བརླག༌[^2221]ཅེའམ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་བར་མའི་དབང་དུ་བྱས་པའོ། །

[Block 3463]
གང་དག་ཐོབ་ཕྱིར་ཡིད་ལ་རྩོལ་བྱེད་ཅིང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ནི་མཐོང་བའི་ཆོས་ཀྱི་བདེ་བ་འདོད་པའི་དབང་དུ་བྱས་པའོ། །

[Block 3464]
དཀའ་ཐུབ་འབད་པས་གང་དག་ཐོབ་འདོད་པའི། །ཞེས་བྱ་བའི་ཕྱེད་འོག་མས་ནི༌[^2222]འཇིག་རྟེན་ཕ་རོལ་གྱི་བདེ་བ་འདོད་པའི་དབང་དུ་བྱ་བའོ།[^2223] །འདོད་པའི་ཕྱིར་ནི་འཇིག་རྟེན་བཅིངས་ཤིང་གསོད་པར༌[^2224]འགྱུར། །ཞེས་བྱ་བ་དང་། གང་གིས་མཛའ་བོ་རྣམས་དང་མྱུར་དུ་འཁོན༌[^2225]འབྱུང་འགྱུར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་གཉིས་དང་། དེ་བས་རབ་དང་འབྲིང་དང་ཐ་མ་རྣམས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་རྣམ་པ་གསུམ་གྱི་འདོད་པའི་ཉེས་དམིགས་མདོར་བསྡུས་ནས་བསྟན་པ་སྟེ། ཐ་མའི་འདོད་པའི་ཉེས་དམིགས་ཀྱི་དབང་དུ་བྱས་པ་ནི། འདོད་པའི་ཕྱིར་ནི་འཇིག་རྟེན་བཅིངས་ཤིང་གསོད་པར་འགྱུར། །ཞེས་བྱ་བ་ཕྱེད་དོ། །

[Block 3465]
རབ་ཀྱི་དབང་དུ་བྱས་པ་ནི། རྒྱལ་པོ་རྣམས་ཀྱང་འདོད་པའི་ཕྱིར། །ཞེས་བྱ་བ་ཕྱེད་འོག་མའོ། །

[Block 3466]
འབྲིང་གི་དབང་དུ་བྱས་པ་ནི།

[Block 3467 [VERSE]]
གང་གིས་མཛའ་བོ་རྣམས་དང་མྱུར་དུ་འཁོན༌[^2226]འབྱུང་འགྱུར། །
ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་འོག་མ་ཡིན་ནོ། །
འདི་དང་ཕ་རོལ་དུ་ཡང་འདོད་པས་གསོད་པར༌[^2227]བྱེད། །

[Block 3468]
ཅེས་བྱ་བ་ནི། གྲགས་པ་ཉམས་ཤིང་ཕྱི་མ་ལ་ཡང་སྡུག་བསྔལ་མྱོང་། །ཞེས་བྱ་བ་ཚིགས་བཅད་དེའི་དབང་དུ་བྱས་པ་སྟེ། གྲགས་པ་ཉམས་པ་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཉེས་དམིགས་སོ། །

[Block 3469]
སྡུག་བསྔལ་མྱོང་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཉེས་དམིགས་སོ། །

[Block 3470]
བདག་ལ་ཕན་འདོད་སྦྲུལ་གདུག་ཁྲོས་པ་བཞིན། །ཞེས་བྱ་བ་ནི་དུས་རྟག་ཏུ་ཕུང་ཁྲོལ་གྱི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
