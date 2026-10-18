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
[Block 4446]
རྟེན་གང་གིས་བསམ་གཏན་དང་གཟུགས་མེད་པ་དུ་ཞིག་མངོན་སུམ་དུ་བྱེད་ཅེ་ན། བསམ་གཏན་གཟུགས་མེད་རང་དང་ནི། །འོག་སའི་རྟེན་ཅན་སྲིད་པའི་རྩེ་མོར་ཡང་མངོན་སུམ་དུ་བྱེད་ལ་འོག་མ་འདོད་པའི་ཁམས་ཀྱི་བར་དུ་ཡང་མངོན་སུམ་དུ་བྱེད་དོ། །

[Block 4447]
དེ་བཞིན་དུ་ལྷག༌[^3201]མ་རྣམས་ཀྱང་རང་གི་ས་དང་ས་འོག་མར་མངོན་སུམ་དུ་བྱེད་དོ། །

[Block 4448]
ཅིའི་ཕྱིར་གོང་དུ་སྐྱེས་པ་སྙོམས་པར་འཇུག་པ་འོག་མ་མངོན་སུམ༌[^3202]དུ་མི་བྱེད་ཅེ་ན། འདི་ལྟར་དེ་ལ་འོག་དགོས་མེད། །དེ་ལ་ནི་སྙོམས་པར་འཇུག་པ་འོག་མའི་རྫས་ཀྱིས་ཅུང་ཟད་ཀྱང་དགོས་པ༌[^3203]མི་བྱེད་དེ་དམན་པའི་ཕྱིར་རོ། །

[Block 4449]
སྤྱིར་བསྟན་པ་བྱས་ནས་དམིགས་ཀྱིས་སྟོན་པར་བྱེད་དེ།

[Block 4450 [VERSE]]
སྲིད་རྩེར་འཕགས་པ༌[^3204]ཅི་ཡང་མེད། །
མངོན་སུམ་བྱས་ནས་ཟག་པ་ཟད། །

[Block 4451]
འཕགས་པ་སྲིད་པའི་རྩེ་མོར་སྐྱེས་པ་ནི་ཟག་པ་མེད་པའི་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་མངོན་སུམ་དུ་བྱས་ནས་ཟག་པ་ཟད་པར་འགྱུར་རོ། །ཇི་ལྟར་ན་དེར་སྐྱེས་པ་དེ་མངོན་སུམ་དུ་བྱེད་ཅེ་ན། རང་གི་མེད་པའི་ཕྱིར་དང་། དེ་ཡང་ཉེ་བའི་ཕྱིར་རོ། །

[Block 4452 [HEADING]]
### བསམ་གཏན་དང་གཟུགས་མེད་པའི་དམིགས་པ། ^5-8-0

[Block 4453]
ཡང་བསམ་གཏན་དང་གཟུགས་མེད་པ་འདི་དག་གི་དམིགས་པ་ཅི་ཞིག་ཡིན་ཞེ་ན། སྲེད་བཅས་རང་གི་སྲིད་ལ་དམིགས། །རོ་མྱང་བ་དང་མཚུངས་པར་ལྡན་པ་རྣམས་ནི་རང་གི་ས་པའི་སྲིད་པ་ལ་དམིགས་སོ། །

[Block 4454]
སྲིད་པ་སྨོས་པ༌[^3205]ནི་ཟག་པ་དང་བཅས་པའི་དངོས་པོ་གཟུང༌[^3206]ངོ་། །འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་འོག་མ་ལ་ཡང་མི་དམིགས་སོ། །

[Block 4455]
ས་རྣམས་ནི་སྲིད་པས༌[^3207]ཡོངས་སུ་བཅད་པའི་ཕྱིར་གོང་མ་ལ་ཡང་མ་ཡིན་ནོ། །

[Block 4456]
དགེ་བ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་ཟག་པ་མེད་པ་ལ༌[^3208]ཡང་མ་ཡིན་ནོ། །

[Block 4457 [VERSE]]
བསམ་གཏན་དགེ་ཡུལ་ཡོད་དགུ་ཡིན། །
དགེ་བའི་བསམ་གཏན༌[^3209]དག་པ༌[^3210]དང་། །

[Block 4458]
ཟག་པ་མེད་པའི་བསམ་གཏན༌[^3211]དེའི་དམིགས་པ་ནི་འདུས་བྱས་སམ་འདུས་མ་བྱས༌[^3212]གང་ཅི་ཡོད་ཀྱང་རུང་བ་ཐམས་ཅད་ཡིན་ནོ། །

[Block 4459 [VERSE]]
གཟུགས་མེད་དངོས་གཞི༌[^3213]དགེ་རྣམས་ཀྱི། །
སྤྱོད་ཡུལ་ཟག་བཅས་འོག་མ་མིན། །

[Block 4460]
གཟུགས་མེད་པའི་དངོས་གཞི་དགེ་བ་རྣམས་ཀྱི་དམིགས་པ་ནི་ས་འོག་མ་པའི་ཟག་པ་དང་བཅས་པའི་དངོས་པོ་མ་ཡིན་ཏེ། རང་གི་ས་པ༌[^3214]དང་། ས་གོང་མ་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 4461]
དམིགས་པ་ཟག་པ་མེད་པ་ནི་རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པ་ཐམས་ཅད་ཡིན་གྱི་ཆོས་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པ་ཡང་མ་ཡིན་ལ་ས་འོག་མའི་འགོག་པ་ཡང་མ་ཡིན་ནོ། །

[Block 4462]
ཉེར་བསྡོགས་ཀྱི་བར་ཆད་མེད་པའི་ལམ་རྣམས་ཀྱི་དམིགས་པ་ནི་ས་འོག་མ་ཡིན་ནོ། །

[Block 4463 [HEADING]]
### ཉོན་མོངས་པ་རྣམས་སྤོང་བ། ^5-9-0

[Block 4464]
བསམ་གཏན་དང་གཟུགས་མེད་པ༌[^3215]རྣམ་པ་གསུམ་པོ་འདི་དག་ལས།

[Block 4465]
ཟག་པ་མེད་པས་ཉོན་མོངས་པ་རྣམས་སྤོང་ངོ་། །དག་པ་པས་ཀྱང་མི་སྤོང་ན། །ཉོན་མོངས་པ་ཅན་གྱིས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཏེ། འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་འོག་མ་ལ༌[^3216]ཡང་མ་ཡིན་ལ། དེ་ཉིད་དེའི་གཉེན་པོ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རང་གི་ས་ན་ཡོད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 4466]
ཆེས་ཁྱད་པར་དུ་འཕགས་པའི་ཕྱིར་གོང་མ་ཡང་མ་ཡིན་ནོ། །

[Block 4467]
ཉེར་བསྡོགས་དག་པས་ཀྱང་། གཟུགས་དང་གཟུགས་མེད་པའི་ཉེར་བསྡོགས་ནི་དག་པ་པས་ཀྱང་ཉོན་མོངས་པ་རྣམས་སྤོང་སྟེ། ས་འོག་མ་པའི༌[^3217]གཉེན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4468 [HEADING]]
### ཉེར་བསྡོགས་བརྒྱད། ^5-10-0

[Block 4469 [VERSE]]
ཉེར་བསྡོགས་དུ་ཞིག་ཡོད་ཅེ་ན། །
དེ་དག་ལ་ནི་ཉེར་བསྡོགས་བརྒྱད། །

[Block 4470]
རེ་རེ་ལ༌[^3218]གང་གིས་དེ་ལ་འཇུག་པ་རེ་རེ་ཡོད་དོ། །

[Block 4471]
ཅི་དེ་དག་ཀྱང་རྣམ་པ་གསུམ་ཡིན་ལ་དེ་དག་ལ་ཚོར་བ་ཡང༌[^3219]དེ་དང་འདྲ་བར་ཡོད་དམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ཏེ། དག་པ་བདེ་མིན་སྡུག་བསྔལ་མིན། །དེ་དག་ནི་དག་པ་པ་ཡང་ཡིན་ལ་བཏང་སྙོམས་ཀྱི་དབང་པོ་དང་མཚུངས་པར་ལྡན་པ་དག་ཀྱང་ཡིན་ཏེ། འབད་དེ་དྲང་བར་བྱ་བ་ཡིན་པའི་ཕྱིར་དང་། ས་འོག་མ་པ༌[^3220]ལས་ཡིད་འབྱུང་བ་དང་མ་བྲལ་བའི་ཕྱིར་དང་། འདོད་ཆགས་དང་བྲལ་བའི་ལམ་ཡིན་པའི་ཕྱིར་རོ་མྱང་བ་དང་མཚུངས་པར་ལྡན་པ་མ་ཡིན་ནོ། །

[Block 4472]
དང་པོ་འཕགས་པའང་། ཉེར་བསྡོགས་ཀྱི་དང་པོ་ནི་མི་ལྕོགས་པ་མེད་པ་སྟེ། དེ་ནི་དག་པ་པ་ཡང་ཡིན་ལ་ཟག་པ་མེད་པ་ཡང་ཡིན་ནོ། །

[Block 4473]
ཉེར་བསྡོགས་ཀྱི་སེམས་ཀྱིས་ཉིང་མཚམས་སྦྱོར་བ་ཉོན་མོངས་པ་ཅན་ཡིན་མོད་ཀྱི་མཉམ་པར་གཞག་པ་ལ་ནི༌[^3221]ཉོན་མོངས་པ་ཅན་ཉིད་དགག་གོ། །

[Block 4474]
ཁ་ཅིག་གསུམ། ཁ་ཅིག་ནི་མི་ལྕོགས་པ༌[^3222]མེད་པ་རོ་མྱང་བ་དང་མཚུངས་པར་ལྡན་པ་ཡང་འདོད་དོ། །

[Block 4475 [HEADING]]
### བསམ་གཏན་ཁྱད་པར་ཅན། ^5-11-0

[Block 4476]
ཉེར་བསྡོགས་ཞེས་ཀྱང་འབྱུང་། བསམ་གཏན་ཁྱད་པར་ཅན་ཞེས་ཀྱང་འབྱུང་ན། ཅི་འདིའི༌[^3223]དོན་གཅིག་པ་ཞིག་གམ། འོན་ཏེ་དོན་ཐ་དད་པ་ཞིག་ཡིན་ཞེ་ན། དོན་ཐ་དད་པ་ཡིན་ཏེ། ཉེར་བསྡོགས་ནི་འདོད་ཆགས་དང་བྲལ་བའི་ལམ་ཡིན་ལ། རྟོག་མེད་བསམ་གཏན་ཁྱད་པར་ཅན། །བསམ་གཏན་དང་པོ་ཁོ་ན་རྟོག་པ༌[^3224]དང་། །མཚུངས་པར་མི་ལྡན་པ་ནི་བསམ་གཏན་ཁྱད་པར་ཅན་ཡིན་ཏེ། བསམ་གཏན་གྱི་ཁྱད་པར་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4477]
དེ་ཉིད་ཀྱི་ཕྱིར་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པ་ན་རྣམ་པར་མི་གཞག༌[^3225]པ་སྟེ།

[Block 4478 [VERSE]]
ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །
བསམ་གཏན་ཁྱད་པར་ཅན་དེ་ནི། །

[Block 4479]
རྣམ་གསུམ། རོ་མྱང་བ་དང་མཚུངས་པར་ལྡན་པ་དང་དག་པ་པ་དང་ཟག་པ་མེད་པ་ཡིན་ནོ། །

[Block 4480]
དེ་བདེ་མིན་སྡུག་མིན། འདི་ལ་བདེ་བ་ཡང་མེད་པས༌[^3226]ན་བདེ་བ་ཡང་མ་ཡིན་པ༌[^3227]སྡུག་བསྔལ་ཡང་མ་ཡིན་པ་སྟེ། བཏང་སྙོམས་ཀྱི་དབང་པོ་དང་མཚུངས་པར་ལྡན་པ༌[^3228]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4481]
མངོན་པར་འདུ་བྱ་བ་དང་བཅས་པས༌[^3229]དྲང་བ་ཡིན་པའི་ཕྱིར། དགའ་བ་དང་མཚུངས་པར་ལྡན་པ་ཡང་མ་ཡིན་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་ལམ་དཀའ་བ་ཡིན་ནོ། །

[Block 4482]
འོ་ན་བསམ་གཏན་ཁྱད་པར་ཅན་དེའི་འབྲས་བུ་ཁྱད་པར་ཅན་གང་ཞིག་ཡིན་ཞེ་ན། དེ་ནི་ཚངས་ཆེན་འབྲས་བུ་ཅན། །བསམ་གཏན་ཁྱད་པར་ཅན་དེ་བསྒོམས་ནས་ཚངས་པ་ཆེན་པོར་འགྱུར་རོ། །

[Block 4483 [HEADING]]
### རྟོག་པ་དང་བཅས་པ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་གསུམ། ^5-12-0

[Block 4484 [HEADING]]
#### རྟོག་པ་མེད་ལ་དཔྱོད་པ་ཙམ། ^5-12-1-0

[Block 4485]
ཡང་ཏིང་ངེ་འཛིན་ཐམས་ཅད་མདོར་བསྡུས་ཏེ། མདོ་ལས་རྟོག་པ་དང་བཅས་ཤིང་དཔྱོད་པ་དང་བཅས་པའི་ཏིང་ངེ་འཛིན་དང་། རྟོག་པ་མེད་ལ་དཔྱོད་པ་ཙམ་དང་། རྟོག་པ་ཡང་མེད་ལ་དཔྱོད་པ་ཡང་མེད་པའི་ཏིང་ངེ་འཛིན་དང་ཏིང་ངེ་འཛིན་གསུམ་དུ༌[^3230]བཀའ་སྩལ་ཏེ། དེ་ལ་རེ་ཞིག་བསམ་གཏན་ཁྱད་པར་ཅན་ན༌[^3231]ནི། རྟོག་པ་ཙམ་ཞིག་བཀག་པའི་ཕྱིར་རྟོག་པ་མེད་ལ་དཔྱོད་པ་ཙམ་གྱི་ཏིང་ངེ་འཛིན་ཏོ་ཞེས་ཤེས་པར་བྱས་ཟིན་ཏོ། །
--- END BLOCKS ---
