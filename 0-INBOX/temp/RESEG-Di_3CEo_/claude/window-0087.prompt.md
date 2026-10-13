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
[Block 3046]
འདི༌[^1204]གཉིས་ཀྱི་བྱ་བ་ཡང༌[^1205]གཅིག་སྟེ། འདི་གཉིས་ཀས༌[^1206]ཀྱང་སེམས་རྣམ་པར་མ་ཞི་བར་བྱེད་དོ། །གང་གི་ཚེ་ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱང་སྒྲིབ་པ་ཡིན་ན། ཅིའི་ཕྱིར་ལྔ་ཁོ་ནར་བཤད་ཅེ་ན། ཕུང་པོ་གནོད་བྱེད་དང་། ཐེ་ཚོམ་ཕྱིར་ན་ལྔ་ཉིད་དོ། །

[Block 3047]
འདོད་པ་ལ་འདུན་པ་དང་། གནོད་སེམས་དག་གིས་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་ལ་དང་། རྨུགས་པ་དང་། གཉིད་དག་གིས་ནི་ཤེས་རབ་ཀྱི་ཕུང་པོ་ལ་དང་། རྒོད་པ་དང་འགྱོད་པས་ནི་ཏིང་ངེ་འཛིན་གྱི་ཕུང་པོ་ལ་གནོད་པར་བྱེད་པའོ། །

[Block 3048]
ཏིང་ངེ་འཛིན་དང་ཤེས་རབ་དག་མེད་ན་བདེན་པ་དག་ལ་ཐེ་ཚོམ་ཟ་བར་འགྱུར་ཏེ། དེའི་ཕྱིར་སྔར་བཤད་ཟིན་ཏོ། །

[Block 3049 [HEADING]]
### ཉོན་མོངས་པ་སྤོང་བ། ^5-17-0

[Block 3050]
འདི་དཔྱད་པར་བྱ་སྟེ། སྐལ་བ་མི་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་རྣམས་དང་། འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ཟག་པ་དང་བཅས་པ་ལ་དམིགས་པ་རྣམས་གང་གི་ཚེ་དམིགས་པ་ཡོངས་སུ་ཤེས་པ་དེའི་ཚེ་སྤོང་བར་མི་འགྱུར་ལ། གང་གི་ཚེ་སྤོང་བར་འགྱུར་བ་དེའི་ཚེ་ནི་དམིགས་པ་ཡོངས་སུ་མི་ཤེས་ན་ཇི་ལྟར་དེ་དག་སྤོང་ཞེ་ན། ཉོན་མོངས་པ་རྣམས་ནི་དམིགས་པ་ཡོངས་སུ་ཤེས་པས་ཟད་པར་ངེས་པ་མ་ཡིན་ནོ། །

[Block 3051]
འོན་ཀྱང་།

[Block 3052 [VERSE]]
དམིགས་པ་ཡོངས་སུ་ཤེས་པ་དང་། །
དེ་ལ་དམིགས་པ་ཡང་དག་པར། །
ཟད་དང་དམིགས་པ་སྤངས་པས་སོ། །

[Block 3053]
དེ་ལ་དམིགས་པ་ཡོངས་སུ་ཤེས་པས་ནི་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་མཐོང་བས་སྤང་བར་བྱ་བ་རང་གི་ས་ལ་དམིགས་པ་རྣམས་དང་། ཟག་པ་མེད་པ་ལ་དམིགས་པའོ། །

[Block 3054]
དེ་ལ་དམིགས་པ་རྣམས་ཡང་དག་པར་ཟད་པས་ནི་སྐལ་བ་མི་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་རྣམས་སོ། །

[Block 3055]
དེ་ལ༌[^1207]དམིགས་པ་ནི་སྐལ་བ་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་དག་ཡིན་པས་དེ་སྤང༌[^1208]ན་དེ་དག་ཀྱང་སྤངས་པ་ཡིན་ནོ། །

[Block 3056]
དམིགས་པ་སྤངས་པས་ནི་འགོག་པ་དང་ལམ་མཐོབ་བས་སྤང་བར་བྱ་བ་ཟག་པ་དང་བཅས་པ་ལ་དམིགས་པ་རྣམས་ཟད་པར་འགྱུར་རོ། །

[Block 3057]
ཟག་པ་མེད་པ་ལ་དམིགས་པ་དེ་དག་ནི་དེ་དག་གིས་དམིགས་པ་ཡིན་པས་དེ་དག་སྤངས་ན་དེ་དག་ཀྱང་སྤངས་པར་འགྱུར་རོ། །

[Block 3058]
དེ་ལྟར་རེ་ཞིག་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས༌[^1209]ཡིན་ནོ། །

[Block 3059]
བསྒོམ་པས་སྤང་བར་བྱ་བ་རྣམས་ནི། གཉེན་པོ་སྐྱེས་པས༌[^1210]ཟད་པར་འགྱུར། །ཉོན་མོངས་པའི་རྣམ་པ་གང་གི་གཉེན་པོ་ལམ༌[^1211]གང་ཡིན་པ་དེ་སྐྱེས་པས་སྤོང་བར་བྱེད་དོ། །

[Block 3060]
དེ་ཡང་ནི་ཆེན་པོའི་ཆེན་པོའི་ནི་ཆུང་ངུའི་ཆུང་ངུས་ཞེས་བྱ་བ་ལ་སོགས་པས་འཆད་པར་འགྱུར་རོ། །

[Block 3061 [HEADING]]
#### གཉེན་པོ་རྣམ་པ་བཞི། ^5-17-1-0

[Block 3062]
གཉེན་པོ་ཡང་རྣམ་པ་དུ་ཞིག་ཅེ་ན། སྨྲས་པ།

[Block 3063 [VERSE]]
གཉེན་པོ་རྣམ་ལ་ཞི་སྤོང་བ་དང་། །
གཞི་དང་སྲིད་ཉིད་རྣམ་པར་ནི། །

[Block 3064]
སུན་འབྱིན་ཞེས་བྱ། །སྤོང་བའི་གཉེན་པོ༌[^1212]བར་ཆད་མེད་པའི་ལམ་མོ། །

[Block 3065]
གཞིའི་གཉེན་པོ་ནི་དེ་ཡན་ཆད་ཀྱི་གཉེན་པོ་གང་ཡིན་པའོ། །

[Block 3066]
ཐག་བསྲིང་བའི་ངོ་བོའི་གཉེན་པོ་ནི་རྣམ་པར་གྲོལ་བའི་ལམ་མན་ཆད་ཀྱི་གཉེན་པོ་གང་ཡིན་པའོ། །

[Block 3067]
སུན་འབྱིན་པའི་གཉེན་པོ་ནི་ལམ་གང་གིས་ཁམས་དེ་ལ་སྐྱོན་དུ་མཐོང་ནས་རྣམ་པར་སུན་འབྱིན་པར་བྱེད་པའོ། །

[Block 3068]
ཉོན་མོངས་པ་སྤོང་བ་ན་གང་ལས་སྤང་བར་བྱ་ཞེ་ན།

[Block 3069]
དམིགས་པ་ལས།

[Block 3070]
ཉོན་མོངས་པ་ནི་སྤང་བྱར་འདོད། །མཚུངས་པར་ལྡན་པ་ལས་ཉོན་མོངས་པ་རྣམ་པར་དབྱེ་བར་མི་ནུས་ལ། དམིགས་པ་ལས་ནི་ནུས་སོ། །

[Block 3071 [HEADING]]
#### རིང་བ་བཞི། ^5-17-2-0

[Block 3072]
ཐག་བསྲིང་བའི་ངོ་བོ་ཞེས་བྱ་བར་སྔར་བཤད་པ་དེ་བསྟན་པར་བྱ་སྟེ།

[Block 3073 [VERSE]]
མཚན་ཉིད་དང་ནི་མི་མཐུན་ཕྱོགས། །
ཡུལ་རྣམས་ཆད་དང་དུས་ཀྱིས་ཏེ། །
འབྱུང་དང་ཚུལ་ཁྲིམས་ཕྱོགས་དང་ནི། །
དུས་གཉིས་རིང་བ་ཉིད་ལྟ་བུའོ། །

[Block 3074]
མཚན་ཉིད་ཀྱིས་རིང་བ་ནི་དཔེར་ན་འབྱུང་བ༌[^1213]ཆེན་པོ་རྣམས་ལྷན་ཅིག་སྐྱེས་པ་ཡིན་ཡང་མཚན་ཉིད་མི་མཐུན་པས་རིང་བ་ལྟ་བུའོ། །

[Block 3075]
གཉེན་པོས་རིང་བ་ནི་དཔེར་ན་འཆལ་བའི་ཚུལ་ཁྲིམས་ལས་ཚུལ་ཁྲིམས་ལྟ་བུའོ། །

[Block 3076]
ཡུལ་གྱིས་རིང་བ་ནི་བསྐལ་པའི༌[^1214]ཡུལ་རྣམས་ཡུལ༌[^1215]རྣམ་པར་ཆད་པས་སོ། །

[Block 3077]
དུས་ཀྱིས༌[^1216]རིང་བ་ནི་དཔེར་ན་འདས་པ་དང་མ་འོངས་པ་ལྟ་བུའོ། །

[Block 3078 [HEADING]]
#### བྲལ་བའི་ཐོབ་པ། ^5-17-3-0

[Block 3079]
ཅི་ལམ་ཁྱད་པར་དུ་འགྲོ་བའི་ཕྱིར་ཉོན་མོངས་པ་རྣམས་ཀྱི་སྤངས་པ་ཡང་དང་ཡང་དུ་ཁྱད་པར་དུ་འགྱུར་རམ་ཞེ་ན། དེ་ནི་མེད་དེ། ཉོན་མོངས་པ་ཐམས་ཅད་ནི། ལན་ཅིག་ཏུ་ཟད། གང་གིས་སྤོང་བའི་ལམ་གང་ཡིན་པ་དེ་ཁོ་ནས་ཟད་པ་ཡིན་ནོ། །

[Block 3080]
དེ་དག་གི །བྲལ་བའི་ཐོབ་པ་ཡང་དང་ཡང་དུས་དུ་ཞིག་ཏུ་ཞེ་ན། སྨྲས་པ། དྲུག་ཏུ་སྟེ།

[Block 3081 [VERSE]]
གཉེན་པོ་སྐྱེ༌[^1217]དང་འབྲས༌[^1218]ཐོབ་དང་། །
དབང་པོ་རྣམ་པར་འཕེལ་རྣམས་སུ། །

[Block 3082]
གཉེན་པོ་ནི་རྣམ་པར་གྲོལ་བའི་ལམ་མོ། །

[Block 3083 [VERSE]]
འབྲས་བུ་དག་ནི་དགེ་སྦྱོང་གི་འབྲས་བུ་དག་གོ། །
དབང་པོ་རྣམ་པར་འཕེལ་བ་ནི་དབང་པོ་འཕོ་བའོ། །
དུས་དེ་དག་ཏུ་ཉོན་མོངས་པ་བྲལ་བ་ཐོབ་པོ། །

[Block 3084]
བྲལ་བ་དེ་ཡང་ནི་གནས་སྐབས་དེ་དང་དེ་དག་ཏུ་ཡོངས་སུ་ཤེས་པ་ཞེས་བྱ་བའི་མིང་འཐོབ་བོ། །

[Block 3085 [HEADING]]
### ཡོངས་སུ་ཤེས་པ་དགུ། ^5-18-0
--- END BLOCKS ---
