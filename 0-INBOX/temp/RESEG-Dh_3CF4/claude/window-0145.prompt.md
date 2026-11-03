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
[Block 5076]
ཉམས་ཉེས༌[^3259]རབ་ཏུ་ཆེ་བ་དང་། །ཕོངས་ནས་མྱ་ངན་བྱེད་པ་ཞེས་བྱ་བ་ལ་ཉམས་ཉེས༌[^3260]པ༌[^3261]རབ་ཏུ་ཆེ་བ་ནི་རྒྱལ་པོའི་དཔུང་གི་ཚོགས་ཀྱིས་ཟིལ་གྱིས་མནན་པས་སོ། །

[Block 5077]
དེས་བྱས་པའི་ཕོངས་པ་ནི་ཉམས་ཉེས༌[^3262]རབ་ཏུ་ཆེར་བྱུང་བས་ཕོངས་པའོ། །

[Block 5078]
ཉམས་ཉེས༌[^3263]རབ་ཏུ་ཆེར་བྱུང་ཞིང་ཕོངས་པས་བྱས་པའི་མྱ་ངན་ནི་ཉམས་ཉེས༌[^3264]རབ་ཏུ་ཆེར་བྱུང་ཞིང་། ཕོངས་ནས་མྱ་ངན་བྱེད་པའོ། །

[Block 5079]
ཉམས་ཉེས༌[^3265]རབ་ཏུ་ཆེར་བྱུང་ཞིང་ཕོངས༌[^3266]ནས་མྱ་ངན་བྱེད་པ་དེ་ཉིད་ཀྱི་རྒྱུ་བསྟན་པའི་ཕྱིར། དེ་བས་གཞུ་རྣམས་བཀང་ནས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། དེ་བས་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར། སྡུག་བསྔལ་རབ་ཏུ་བྱུང་བ་ཉིད་དེ། དེའི་ཕྱིར། མདེའུ་རྩེ་མོ་རྣོན་པོ་དག་འཕེན་པ་རྣམས་ཀྱིས་འཇིགས་པ་གང་ཡིན་པ་དེ་དག་ལས་འཇིགས་པའི་སྒྲ་གང་ཡིན་པ་དེ་ནི་སྒྲ་འཇིགས་པའོ། །

[Block 5080]
སྒྲ༌[^3267]འཇིགས་པའི་གཞུ་རྒྱུད་གང་ཡིན་པ་དེ་ནི། གཞུ་རྒྱུད་སྒྲ་འཇིགས་སོ། །

[Block 5081]
ཕོངས་པ་དང་། མྱ་ངན་བྱེད་པ་དེ་བསྟན་པའི་ཕྱིར། བདག་གི་འཁོར་ནི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5082]
རབ་ཏུ་སྐྲག་པའི་སེམས་ཡིན་པས་ཕོངས་པའོ། །

[Block 5083]
ངུ་ཞིང་འབོད་པས་ཞེས་བྱ་བ་འདིས་ནི་མྱ་ངན་བྱེད་པའོ། །

[Block 5084]
ས་ཁྱོན༌[^3268]ལེགས་པར་བརྟགས་པ་གང་ཡིན་པ་དེ་ནི་ས་ཁྱོན༌[^3269]ཚད་ནི་ལེགས་པར་བརྟགས་པའོ། །

[Block 5085]
རྩ་བཅས་ཞེས་བྱ་བས་ནི་སྔར་བཤད་པའི་རྩ་བ་དང་ལྡན་པའོ། །

[Block 5086]
བདག་གི་བདེ་བ་ཁྱད་དུ་བསད་པ་དེ་ལ་ཁྱོད་ཀྱིས༌[^3270]ཡོན་ཏན་ཅི་ཞིག་འཐོབ་ཅེས་བཤད་པ་ལ། དེའི་ཡོན་ཏན་བསྟན་པའི་ཕྱིར། གང་རྣམས་རྒྱལ་པོ་བདག་གིས་ཡུན་རིང་བྱས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5087]
བདག་གི་ལུས་ལྟ་སྣད་པར་གྱུར་ཀྱང་རུང་། །ཞེས་བྱ་བ་ནི་བདག་གི་ལུས་འདི་ལ་རྨ་ཡོད་པར་གྱུར་ཀྱང་རུང་ཞེས་བྱ་བ་ཡིན་ཏེ།

[Block 5088 [VERSE]]
འདིས་ནི་བདེ་བ་ཁྱད་དུ་གསོད་པར་སྟོན༌[^3271]ཏོ། །
དེ་བས་སེམས་ནི་རབ་ཏུ་དགའ་བར་གྱུར། །

[Block 5089]
ཅེས་བྱ་བ་ནི།

[Block 5090 [VERSE]]
ཡིད་གྱི་བདེ་བ་འཐོབ་པ་སྟེ། །
ཡོན་ཏན་འདི་ཐོབ་པ་ཡིན་ནོ། །

[Block 5091]
དེ་བས་ན་ཡིད༌[^3272]དགའ་བ་ཐོབ་བ་དེའི་རྒྱུ་བསྟན་པའི༌[^3273]ཕྱིར་སྨྲས་པ། བདག་གིས་དེ་དག་སྡུག་བསྔལ་རྣམ་པར་བཟློག །ཅེས་བྱ་བ་ཉིད་ཀྱིས་སོ། །

[Block 5092]
དེ་བས་ན་དེའི་ཕྱིར་དྲེགས་པའི་དགྲ་རྣམས་གཡུལ་ངོར་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་པ་ཡིན་ཏེ། འདིས་ནི་ལུས་ཀྱི་སྡུག་བསྔལ་བ་ཡང་མེད་པར་བསྟན་ཏོ། །

[Block 5093]
རྨ་ཙམ་ཉི་ཚེའམ། རྨ་ལས་བྱུང་བའི༌[^3274]སྡུག་བསྔལ་ཙམ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། ཇི་ལྟར་དཔའ་བོ་རྣམས་ཀྱིས་རྨ་བྱུང་བ་ཡང་། དགྲ་ཕམ་བར་བྱས་པའི་ཕྱིར་བཟོད་པ་ཡིན་ཏེ། མངོན་པར་འདོད་པའི་དོན་བསྒྲུབ་པའི་ཕྱིར། དགའ་བཞིན་དུ་རྨ་ལ་བཟོད་པའི་ཕྱིར་རོ། །

[Block 5094]
དེ་བས་ན་རྨ་ལས་བྱུང་བའི་སྡུག་བསྔལ་བ་ཡང་མེད་དེ། བདེ་བ་འབའ་ཞིག་ཡིན་ནོ། །

[Block 5095]
ལུས་སྣད་པ་དེའི་སྡུག་བསྔལ་མེད་དེ། བདེ་བ་ཉིད་དུ་བསྟན་ན། དཔའ་བོ་རྣམས་རྨའི་སྡུག་བསྔལ་དགའ༌[^3275]བཞིན་དུ་བཟོད་པ་ལྟར་བདག་ཉིད་རྨ་དེ་ལ་དེ༌[^3276]ཇི་ལྟར་དགའ་བཞིན་དུ་བཟོད་ཅེ་ན། དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། རིགས༌[^3277]མཐུན་རྣམས་ཀྱིས་རབ་ཏུ་གུས་བྱས་ནས།[^3278] །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5096]
[^3279]དབང་ཕྱུག་བདེ་བ་ཐོབ་པར་གྱུར་པའི༌[^3280]བུ་ལོན་འཁོར༌[^3281]བར་གྱུར་པའི་ཕྱིར་ཏེ། དེས་ན་དེའི་ཕྱིར་དགའ་བཞིན་བཟོད་བར་བྱ་བའོ། །

[Block 5097]
དེ་བས་ན་བདག་ཉིད་མཛའ་བ་དང་བྲལ་བའམ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་སྔར་བཤད་པའི་དོན་གྱི་མཇུག་སྡུད་པ༌[^3282]ཡིན་ཏེ། དེ་བས་ན་ཞེས་བྱ་བས་ནི་བུ་ལོན་འཁོར༌[^3283]བའི་ཕྱིར་རོ། །

[Block 5098]
དེ་ཙམ་ཉི་ཚེར་ཡང་མ་ཟད་དེ། འདི་ལྟར་ཡོན་ཏན་ཁྱད་པར་ཅན་འཐོབ་པའི་ཕྱིར་རོ། །

[Block 5099]
དེ་ཡོན་ཏན་དེ་གང་ཡིན་ཞེ་ན། དེ་ཉིད་སྨྲས་པ། སྔོན་དུ་ཕན་བཏགས་བུ་ལོན་འཁོར༌[^3284]བས་མགུ། ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། འཁོར་གྱི༌[^3285]སྔོན་དུ་ཕན་བཏགས་པ་ལ་ཡང་དག་སྒྲུབ་པའི་ཕན་ཡོན་ཏེ། བདག་ཉིད་མགུ་བ་དང་། མྱ་ངན་ཞི་བ་ནི་བདག་དང་འབྲེལ་པའི་ཕན་ཡོན་ནོ། །

[Block 5100]
ད་ལྟར་བྱུང་བའི་གྲགས་པ་དྲི་མ་མེད་པ་འཐོབ་པ་དང་། རྒྱལ་པོས་མཆོད་པ་བྱས་ཞེས་བྱ་བ་འདིས༌[^3286]གཉིས་ནི། གཞན་དང་འབྲེལ་བའི་ལུས་དང་། ངག་གི་ཕན་ཡོན་ནོ། །

[Block 5101]
འཆི་ལ་འཇིགས་པ་མེད་ཅེས་བྱ་བ་ནི། དུས་གཞན་གྱི་ཕན་ཡོན་ནོ། །

[Block 5102]
དེ་དང་མི་མཐུན་པའི་ཕྱོགས་ཞེས་བྱ་བ་ནི། བུ་ལོན་འཁོར་བ༌[^3287]ལ་སོགས་པ་མེད་པ། དམ་པས་ཕན་བཏགས་དྲིན་ཡང་དྲན་པར་གྱུར། །ཞེས་བྱ་བ་ནི། དེ་དག་གཞན་དང་འབྲེལ་བའི་ཡིད་ཀྱི་ཕན་ཡོན་ནོ། །

[Block 5103]
དེ་དང་མི་མཐུན་པའི་ཕྱོགས་ཞེས་བྱ་བ་ནི་བུ་ལོན་འཁོར་བ༌[^3288]ལ་སོགས་པ་མེད་པ་ཉིད་ནི་དེ་དང་མི་མཐུན་པའི་ཕྱོགས་ཏེ་སྐྱོན་ནོ། །

[Block 5104]
ཡོན་ཏན་མེད་པ་ནི་བུ་ལོན་འཁོར་བ་ལ་སོགས་པའི་ཡོན་ཏན་མེད་པའོ། །

[Block 5105 [VERSE]]
གྲགས་པ་མེད་པར་གྱུར་པ་ནི། །
སྔར་ཐོབ་པའི་གྲགས་པ་རྣམས་ཉམས་བའོ། །

[Block 5106]
ཉེས་པ་འབྱུང་བའི་གནས་སུ་གྱུར་པ་རྣམས། །ཞེས་བྱ་བ་ནི་ཡོན་ཏན་གྱི་མི་མཐུན་པའི་ཕྱོགས་སྔར་བཤད་པ་དག་སྟེ། ཡོན་ཏན་མེད་པའོ། །

[Block 5107]
བརྟན་པ་ཞེས་བྱ་བ་ནི་སྔོན་དུ་ཕན་བཏགས་བུ་ལོན་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་སོ། །

[Block 5108]
སྐྱོན༌[^3289]གྱི་མཐུ་ཞེས་བྱ་བ་ནི། བདག་པོ་སྙིང་རྗེ་མེད་ལ་རྟེན༌[^3290]བཅས་ནས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་འོག་མ་དང་། ཡོན་ཏན་མེད་ཅིང་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་སོ། །

[Block 5109]
གཞོན་པའི༌[^3291]དཔུང་དང་། ལྗོངས་དང་། བློན་པོ་དང་ཞེས་བྱ་བ་ཡིན་ཏེ། བདེ་བ་དང་ལྡན་པར་དོན་སྒྲུབས་ཤིག་བའོ། །

[Block 5110]
མགོན་མེད་འབངས་དང་། དགེ་སྦྱོང་བྲམ་ཟེ་རྣམས་ཀྱང་བདེ་བ་དང་ལྡན་པར་མཛོད་ཅིག་པའོ། །

[Block 5111]
ཆོས་འཕེལ་བར་བྱས་ན་ནི། བདེ་བ་གཉིས་དང་ལྡན་པར་འགྱུར་ཏེ། གྲགས་པ་འཕེལ་བ་དང་། སྲིད་འཕེལ་བའོ། །

[Block 5112]
འདི་ནི་འདིར་བདེ་བའོ། །

[Block 5113]
ཡང་ན་གཉི་ག་ལ་ཡང་བདེ་བར་འགྱུར་བའོ། །

[Block 5114]
སློབ་དཔོན་དཔའ་བོས༌[^3292]མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་སྤྲེའུའི་རྒྱལ་པོའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 5115 [HEADING]]
## བཟོད་པར་སྨྲ་བའི་སྐྱེས་པའི་རབས། ^30-0
--- END BLOCKS ---
