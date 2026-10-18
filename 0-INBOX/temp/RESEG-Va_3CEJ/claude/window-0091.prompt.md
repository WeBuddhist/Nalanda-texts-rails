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
[Block 3186]
ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་བཅོ་བརྒྱད་གང་ཞེ་ན། ཡིད་བདེ་བའི་ཉེ་བར་རྒྱུ་བ་དྲུག་དང་། ཡིད་མི་བདེ་བའི་ཉེ་བར་རྒྱུ་བ་དྲུག་དང་། བཏང་སྙོམས་ཀྱི་ཉེ་བར་རྒྱུ་བ་དྲུག་གོ། །

[Block 3187]
དེ་དག་ཇི་ལྟར་རྣམ་པར་བཞག །གལ་ཏེ་ངོ་བོ་ཉིད་ལས་ན༌[^1819]ནི་གསུམ་དུ་འགྱུར་ཏེ། ཡིད་བདེ་བ་དང་། ཡིད་མི་བདེ་བ་དང་། བཏང་སྙོམས་ཀྱི་ཉེ་བར་རྒྱུ་བ་དག་ཡིན་ནོ། །

[Block 3188]
འོན་ཏེ་མཚུངས་པར་ལྡན་པ་ལས་ན༌[^1820]ནི་ཡིད་དང་མཐུན་པར༌[^1821]ལྡན་པའི་ཕྱིར་གཅིག་ཏུ་འགྱུར་རོ། །

[Block 3189]
འོན་ཏེ་དམིགས་པ་ལས་ན་ནི་གཟུགས་ལ་སོགས་པ་ཡུལ་དྲུག་ལ་དམིགས་པའི་ཕྱིར་དྲུག་ཏུ་འགྱུར་རོ་ཞེ་ན། གསུམ་ཀར་ཡང་གཞག་སྟེ། དེ་དག་ལས་བཅོ་ལྔ་ནི་གཟུགས་ལ་སོགས་པ་ལ་ཉེ་བར་རྒྱུ་བ་ཡིན་ཏེ། གཟུགས་ལ་སོགས་པ་སོ་སོར་ངེས་པ་ལ་དམིགས་པའི་ཕྱིར་མ་འདྲེས་པ་ལ་དམིགས་པ་ཡིན་ནོ། །

[Block 3190]
ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་གསུམ་ནི་རྣམ་པ་གཉི་ག་ཡིན་ནོ། །

[Block 3191]
ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་ཞེས་བྱ་བའི་དོན་ཅི་ལྟར༌[^1822]ཞེ་ན། ཡིད་ལ་བརྟེན་ནས་ཡིད་བདེ་བ་ལ་སོགས་པ་དེ་དག་ཡུལ་ལ་ཉེ་བར་རྒྱུ་བའི་ཕྱིར་རོ་ཞེས་གྲག་གོ། །

[Block 3192]
གཞན་དག་ན་རེ། ཡུལ་དག་ལ་ཡིད་ཉེ་བར་རྒྱུ་བར་བྱེད་པའི་ཕྱིར་ཏེ། ཚོར་བའི་དབང་གིས་ཡིད་ཡུལ་དག་ལ་ཡང་དང་ཡང་དུ་རྣམ་པར་རྒྱུ་བའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 3193]
ལུས་ཀྱི་ཚོར་བ་ཅིའི་ཕྱིར་ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་མ་ཡིན་ཞེ་ན། འདི་ནི་ཡིད་ཁོ་ན་ལ་བརྟེན་པ་ཡང་མ་ཡིན་ལ། རྣམ་པར་མི་རྟོག་པའི་ཕྱིར་ཉེ་བར་རྒྱུ་བར་བྱེད་པ་ཡང་མ་ཡིན་པས་མི་རུང་ངོ་། །བསམ་གཏན་གསུམ་པའི་བདེ་བ་ཅིའི་ཕྱིར་ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བའི་ནང་དག་ཏུ་མ་སྨོས་ཤེ་ན།

[Block 3194]
དང་པོ་འདོད་པའི་ཁམས་ན་ཡིད་ཀྱི་ས་པའི་བདེ་བའི་དབང་པོ་མེད་པའི་ཕྱིར་དང་། དེའི་མི་མཐུན་པ་སྡུག་བསྔལ་གྱི་ཡིད༌[^1823]ཉེ་བར་རྒྱུ་བ་མེད་པའི་ཕྱིར་རོ་ཞེས་གྲག་གོ། །

[Block 3195]
གལ་ཏེ་འདི་དག་ཡིད་ཀྱི་ས་པ་ཁོ་ན་ཞིག་ཡིན་ན།

[Block 3196]
འོ་ན་མདོ་ལས།

[Block 3197]
མིག་གིས་གཟུགས་དག་མཐོང་ནས་ཡིད་བདེ་བའི་གནས་ལྟ་བུའི་གཟུགས་རྣམས་ལ་ཉེ་བར་རྒྱུའོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་གང་གསུངས་པ་དེ་ཇི་ལྟར་དྲང་། དེ་ནི་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔས་མངོན་པར་བསྒྲུབས་པ་ཉིད་ལ་དགོངས་ཏེ་གསུངས་པར་ཟད་ཀྱི། འདི་དག་ནི་ཡིད་ཀྱི་ས་པ་ཡིན་ཏེ། དཔེར་ན་མི་སྡུག་པ་ལྟ་བུ་མིག་གི་རྣམ་པར་ཤེས་པས་མངོན་པར་བསྒྲུབས་པ་ཡང་ཡིན་ལ། ཡིད་ཀྱི་ས་པ་ཡང་ཡིན་པ་བཞིན་ནོ། །

[Block 3198]
གཞན་ཡང་མཐོང་ནས་ཞེས་བྱ་བ་ནས་རེག་ནས་ཞེས་བྱ་བའི༌[^1824]བར་དུ་གསུངས་པའི་ཕྱིར་དེ་ནི་ཀླན་ཀར་མི་རུང་བ་ཉིད་དོ། །

[Block 3199]
གང་གིས་མ༌[^1825]མཐོང་བ་ནས་མ་རེག་པའི་བར་དུ་ཉེ་བར་རྒྱུ་བ་དེ་ཡང་ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་ཡིན་ནོ། །

[Block 3200]
གཞན་དུ་ན་འདོད་པའི་ཁམས་ན་གཟུགས་ཀྱི་ཁམས་ལ་དམིགས་པ་དག་ཀྱང་གཟུགས་ལ་སོགས་པ་ལ་ཉེ་བར་རྒྱུ་བ་ཡིན་པར་མི་འགྱུར་ལ། གཟུགས་ཀྱི་ཁམས་ན་འདོད་པའི་ཁམས་ལ་དམིགས་པ་དག་ཀྱང་དྲི་དང་རོ་དང་རེག་བྱ་ལ་ཉེ་བར་རྒྱུ་བ་ཡིན་པར་མི་འགྱུར་རོ། །

[Block 3201]
ཇི་ལྟར་ཆེས་གསལ་བ་དེ་ལྟར་བཤད་དེ། གང་གཟུགས་དག་མཐོང་ནས་སྒྲ་རྣམས་ལ་ཉེ་བར་རྒྱུ་བ་དེ་དག༌[^1826]ཡང་ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་ཡིན་མོད་ཀྱི་དབང་པོ་དང་དོན་རྣམ་པར་ཆད་པའི་སྒོ་ནས་ཇི་ལྟར་མི་འཆོལ་བ་དེ་ལྟར་བཤད་དོ། །

[Block 3202]
ཅི་གཟུགས་གང་ཡིད་བདེ་བའི་གནས་ལྟ་བུ་ཁོ་ན་ཡིན་པ་ནས་བཏང་སྙོམས་ཀྱི་གནས་ལྟ་བུ་ཁོ་ན་ཡིན་པའི་བར་ཡོད་དམ་ཞེ་ན། རྒྱུད་ངེས་པས་ནི་ཡོད་ཀྱི་དམིགས་པས་ནི་མ་ཡིན་ནོ། །

[Block 3203 [HEADING]]
###### **འདོད་པ་དང་ལྡན་པ།** ^3-1-11-13-2-1-0

[Block 3204]
ཡང་ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་འདི་དག་ལས་དུ་ཞིག་ནི་འདོད་པའི་ཁམས་དང་ལྡན་པ་ཡིན་དེ་དག་ལས་ཀྱང་དུ་ཞིག་གི་དམིགས་པ་ནི་ཅི་ཞིག་ཡིན། དེ་བཞིན་དུ་གཟུགས་མེད་པ་དང་ལྡན་པའི་བར་དུ་བརྗོད་པར་བྱ༌[^1827]ཞེ་ན། སྨྲས་པ། འདོད་པ༌[^1828]ཐམས་ཅད་རང་དམིགས་ཅན། །འདོད་པའི་ཁམས་ན་ནི་བཅོ་བརྒྱད་པོ་ཐམས་ཅད་ཡོད་ལ། དེ་དག་ཐམས་ཅད་ཀྱི་དམིགས་པ་ཡང་དེ་ཡིན་ནོ། །

[Block 3205]
དེ་དག་ཉིད་ཀྱི། སྤྱོད་ཡུལ་གཟུགས་ཅན་བཅུ་གཉིས་སོ། །

[Block 3206]
གཟུགས་ཀྱི་ཁམས་ནི་བཅུ་གཉིས་ཀྱི་དམིགས་པ་ཡིན་ནོ། །

[Block 3207]
དྲི་དང་རོ་ལ་ཉེ་བར་རྒྱུ་བ་དྲུག་མ་གཏོགས་པ་སྟེ། དེ་ལྟ་ན་དེ༌[^1829]གཉིས་མེད་པའི་ཕྱིར། [^1830]གོང་མ་གསུམ་གྱི། སྤྱོད་ཡུལ་ཞེས་བྱ་བར་སྦྱར་ཏེ། གཟུགས་མེད་པ་ནི་ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་གསུམ་གྱི་དམིགས་པ་ཡིན་ཏེ། དེ་ནས༌[^1831]གཟུགས་ལ་སོགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 3208]
འདོད་པ་དང་ལྡན་པ་བཤད་ཟིན་ཏོ། །

[Block 3209 [HEADING]]
###### **གཟུགས་དང་ལྡན་པ།** ^3-1-11-13-2-2-0

[Block 3210]
གཟུགས་དང་ལྡན་པ་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག །བསམ་གཏན་ནི། གཉིས་ན་བཅུ་གཉིས། ཡིད་མི་བདེ་བའི་ཉེ་བར་རྒྱུ་བ་རྣམས་མ་གཏོགས་སོ། །

[Block 3211]
བཅུ་གཉིས་པོ་དེ་དག་ཀྱང༌[^1832]འདོད་པར་འགྲོ་བས་ན་འདོད་འགྲོ་རྣམས་ཏེ། འདོད་པའི་ཁམས་ལ་དམིགས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3212]
ཡུལ་རྣམ་པར་འཛིན་པའི་དོན་ལ་ཡང་འགྲོ་བ་སྦྱོར་བ་མཐོང་སྟེ། འདི་ཇི་ལྟར་འགྲོ་ཞེ་ན། འདི་ནི་འདི་ལྟར་འགྲོའོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 3213]
རང་ལ་དམིགས་བརྒྱད། གཟུགས་ཀྱི་ཁམས་དེ་ཉིད་ནི་དེ་དག་གི་རང་བཞིན་ཡིན་ཏེ། དེ་ནི་ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་བརྒྱད་ཀྱི་དམིགས་པ་ཡིན་ཏེ། དྲི་དང་རོ་ལ་ཉེ་བར་རྒྱུ་བ་བཞི་མ་གཏོགས་སོ། །

[Block 3214]
གཟུགས་མེད་པ་གཉིས་ཀྱི༌[^1833]སྟེ། ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་དག་གི་དམིགས་པ་ཡིན་ནོ། །

[Block 3215]
བསམ་གཏན་གཉིས་ན་དྲུག །བསམ་གཏན་གསུམ་པ་དང་བཞི་པ་དག་ན་ནི་བཏང་སྙོམས་ཀྱི་ཉེ་བར་རྒྱུ་བ་དྲུག་ཁོ་ན་ཡོད་ཀྱི་གཞན་དག་ནི་མེད་དོ། །

[Block 3216]
དེ་དག་དྲུག་གི །དམིགས་པ་ནི་འདོད་པའོ། །

[Block 3217]
འདོད་པའི་ཁམས་ནི་དྲུག་ཅར་གྱི་ཡང་དམིགས་པ་ཡིན་ནོ། །

[Block 3218]
རང་གི༌[^1834]བཞིའི། གཟུགས་ཀྱི་ཁམས་ནི་བཞི༌[^1835]ཡིན་ཏེ། དེ་ན་དྲི་དང་རོ་མེད་པའི་ཕྱིར་རོ། །

[Block 3219]
གོང་མ་གཅིག་གི་དམིགས་པ་ཡིན། གཟུགས་མེད་པའི་ཁམས་ནི་ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་གཅིག་ཁོ་ནའི་དམིགས་པ་ཡིན་ནོ། །

[Block 3220]
གཟུགས་དང་ལྡན་པ་དག་བཤད་ཟིན་ཏོ། །

[Block 3221 [HEADING]]
###### **གཟུགས་མེད་པ་དང་ལྡན་པ།** ^3-1-11-13-2-3-0

[Block 3222]
ད་ནི་གཟུགས་མེད་པ་དང་ལྡན་པ་བརྗོད་པར་བྱ་སྟེ། གཟུགས་མེད་ཉེ་བར༌[^1836]བསྡོགས་ན་བཞི། །གཟུགས་མེད་པའི་ཉེ་བར༌[^1837]བསྡོགས་ནི་འདིར་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ཀྱི་ཉེ་བར་བསྡོགས་པ༌[^1838]ཡིན་ཏེ། དེ་ན་ནི་གཟུགས་དང་སྒྲ་དང་རེག་བྱ་དང་ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་བཞིའོ། །

[Block 3223]
དེ་དག་ཀྱང་། གཟུགས་སྒྲའོ།[^1839] །དེ་དག་གི་དམིགས་པ་ནི་བསམ་གཏན་བཞི་པ་ཡིན་ཏེ། གང་དག་གི་ལྟར་ན་དེ་རྣམ་པར་ཆད་པ་ལ་དམིགས་པ་ཡོད་པ་ཡིན་ནོ། །

[Block 3224]
གང་དག་གི་ལྟར་ན་ནི་དེ་དག༌[^1840]བཟླུམས་ཏེ་དམིགས་པ་དེ༌[^1841]དག་གི་ལྟར་ན་ནི་དེ་ན་ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་འདྲེས་པ་ལ་དམིགས་པ་གཅིག་ཁོ་ན་ཡོད་དོ། །

[Block 3225]
གོང་མར་འགྲོ་བ་གཅིག །དེ་ན་གཟུགས་མེད་པའི་ཁམས་ལ་དམིགས་པ་ནི་གཅིག་ཁོ་ན་སྟེ། ཆོས་ལ་ཉེ་བར་རྒྱུ་བའོ། །
--- END BLOCKS ---
