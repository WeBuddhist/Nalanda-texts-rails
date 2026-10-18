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
[Block 3291]
རེག་པ༌[^1881]ནི་གཉིས་པའོ། །

[Block 3292]
ཡིད་ལ་སེམས་པ༌[^1882]ནི་གསུམ་པའོ། །

[Block 3293 [VERSE]]
རྣམ་པར་ཤེས་པའི་ཟས་ནི་བཞི་པའོ། །
དེ་ལ་ཁམ་གྱི་ཟས་ནི་འདོད་པ་ན། །

[Block 3294]
གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དག་ན་ནི་མེད་དོ། །

[Block 3295]
[^1883]དེའི་འདོད་ཆགས་དང་བྲལ་བ་དག༌[^1884]དེར་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 3296]
དེ་ཡང་། སྐྱེ་མཆེད་གསུམ་གྱི་བདག་ཉིད་དོ། །

[Block 3297]
འདོད་པ་ན་སྤྱོད་པའི་དྲི་དང་རོ་དང་རེག་བྱའི་སྐྱེ་མཆེད་རྣམས་ནི་སྣ་དང་། ལྕེ་དང་ལུས་ཀྱིས་ཁམ་དུ་བཅད་ནས་ཁམ་དུ་བྱས་ཏེ་མིད་པའི་ཕྱིར་ཐམས་ཅད་ཁམ་གྱི་ཟས་ཁོ་ན་ཡིན་ནོ། །

[Block 3298]
གྲིབ་མ་དང་། ཉི་མ་དང་། མེ་དང་། འོད་དག་ལ་ཡོད་པ་དེ་དག་ཇི་ལྟར་ཟས་ཉིད་ཡིན་ཞེ་ན། འདི་ནི་ཕལ་ཆེ་བར༌[^1885]བསྟན་པ་ཡིན་ནོ་ཞེས་གྲག་གོ། །

[Block 3299]
གང་དག་མི༌[^1886]མིད་ལ་གནས་པར་ཡང་བྱེད་པ་དེ་དག་ཀྱང་ཟས་ཕྲ་མོ་ཡིན་ཏེ། ཁྲུས་དང་ལུས་མཉེ་བ་བཞིན་ནོ། །ཅིའི་ཕྱིར་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ཟས་མ་ཡིན། །དེ་ཡང་ཁམ་དུ་བྱས་ནས་མིད་པར་ནི་བྱེད་དོ་ཞེ་ན།

[Block 3300 [VERSE]]
གཟུགས་ཀྱི་སྐྱེ་མཆེད་མ་ཡིན་དེས། །
རང་དབང་གྲོལ་ལ་མི་ཕན་ཕྱིར། །

[Block 3301]
ཟས་ཞེས་བྱ་བ་ནི་གང་དབང་པོ་དང་། འབྱུང་བ་ཆེན་པོ་རྣམས་ལ་ཕན་འདོགས་པར་བྱེད་པ་ཡིན་ན་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ནི་མེད་པའི་ཚེ་རང་གི་དབང་པོའམ། དེའི་འབྱུང་བ་ཆེན་པོ་རྣམས་ལ༌[^1887]ཕན་མི་འདོགས་ན་ཡུལ་མ་ཡིན་པའི་ཕྱིར་གཞན་དང་གཞན་དག་ལ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། གང་གི་ཚེ་མཐོང་བ་ན་བདེ་བ་དང་། ཡིད་བདེ་བར་བྱེད་པ་དེའི་ཚེ་ཡང་དེ་ལ་དམིགས་པའི༌[^1888]བདེ་བ་མྱོང་བར་འགྱུར་བའི་རེག་པ་ཟས་ཡིན་གྱི་གཟུགས་ནི་མ་ཡིན་ནོ། །

[Block 3302]
གྲོལ་བའི་ཕྱིར་མི་འོང་བ་དང་། དགྲ་བཅོམ་པ་ཟས་ཤིན་ཏུ་ཡིད་དུ་མི༌[^1889]འོང་བ་མཐོང་བ་རྣམས་ལ་ཡང་ཕན་འདོགས་པ་མེད་པའི་ཡང་ཕྱིར་རོ། །

[Block 3303 [HEADING]]
##### རེག་པ་དང་སེམས་པ་དང་རྣམ་པར་ཤེས་པའི་ཟས། ^3-1-12-2-0

[Block 3304 [VERSE]]
རེག་དང་སེམས་པ་རྣམ་ཤེས་ནི། །
ཟག་བཅས་ཟས་ཡིན་གསུམ་དག་ན། །

[Block 3305]
རེག་པ་གསུམ་འདུས་པ་ལས་བྱུང་བ་དང་། སེམས་པ་ཡིད་ཀྱི་ལས་དང་། རྣམ་པར་ཤེས་པ་ཟག་པ་དང་བཅས་པ་དག་ཁོ་ན་ཟས་ཡིན་ཏེ། ཁམས་གསུམ་ཆར་ན་ཡང་ཡོད་དེ། [^1890]ཅིའི་ཕྱིར་ཟག་པ་མེད་པ་རྣམས་མ་ཡིན་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་འདི་ལྟར་སྲིད་པ་གསོ་བར་བྱེད་པའི་དོན་ནི་ཟས་ཀྱི་དོན་ཡིན་ན་དེ་དག་ནི་སྲིད་པ་ཟད་པར་བྱ་བའི༌[^1891]ཕྱིར་སྐྱེས་པ་དག་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3306]
གཞན་ཡང་མདོ་ལས།

[Block 3307]
སེམས་ཅན་བྱུང་བ་རྣམས་གནས་པར་བྱེད་པ་དང་། འཚོ་བར་བྱེད་པ་དང་། སྲིད་པ་ཚོལ་བ་རྣམས་ལ་ཕན་པར་བྱེད་པ་ཡིན་ནོ་ཞེས་གསུངས་ནས༌[^1892]ཟག་པ་མེད་པའི་ཆོས་རྣམས་ནི་དེ་ལྟ་མ་ཡིན་པས་ཟས་དག་མ༌[^1893]ཡིན་ནོ། །

[Block 3308 [HEADING]]
##### སྲིད་པ་ཚོལ་བ། ^3-1-12-3-0

[Block 3309]
རེ་ཞིག་བྱུང་བ་ནི་སེམས་ཅན་སྐྱེས་པ་རྣམས་ཞེས༌[^1894]བྱ་བར་ཡང་ཤེས་ན། སྲིད་པ་ཚོལ་བ་རྣམས་གང་ཞེ་ན།

[Block 3310 [VERSE]]
ཡིད་ལས་བྱུང་དང་སྲིད་ཚོལ་དང་། །
དྲི་ཟ་སྲིད་པ་བར་མ་དང་། །

[Block 3311]
འགྲུབ་པའོ། །

[Block 3312]
བཅོམ་ལྡན་འདས་ཀྱིས་སྲིད་པ་བར་མ་ནི་བརྗོད་པ་འདི་དག་གིས་གསུངས་སོ། །

[Block 3313]
དེ་ནི་ཡིད་ལས་སྐྱེས་པའི་ཕྱིར་ཡིད་ལས་བྱུང་བ་ཞེས་བྱ་སྟེ། ཕྱིའི་ཁུ་ཆུ་དང་ཁྲག་ལ་སོགས་པས་ཅུང་ཟད་ཀྱང་རྒྱུར་བྱས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 3314]
སྲིད་པ་ཚོལ་བའི་ངང་ཚུལ་ཅན་ཡིན་པའི་ཕྱིར་སྲིད་པ་ཚོལ་བའོ། །

[Block 3315]
དྲི་ཟ་བའི་ཕྱིར་ན། དྲི་ཟའོ། །

[Block 3316]
སྐྱེ་བ་ལ་མངོན་དུ་ཕྱོགས་པའི་ཕྱིར་མངོན་པར་འགྲུབ་པ་སྟེ།

[Block 3317]
མདོ་ལས།

[Block 3318]
གནོད་པ་དང་བཅས་པའི་ལུས་མངོན་པར་གྲུབ་ནས་གནོད་པ་དང་བཅས་པའི་འཇིག་རྟེན་དུ་སྐྱེ་བར་འགྱུར་རོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3319]
དེ་བཞིན་དུ་མདོ་ལས།

[Block 3320]
གང་གིས༌[^1895]མངོན་པར་འགྲུབ་པའི་ཀུན་དུ་སྦྱོར་བ་ནི་སྤངས་ལ་སྐྱེ་བའི་ཀུན་དུ་སྦྱོར་བ་ནི་མ་ཡིན་པའི་གང་ཟག་ཀྱང་ཡོད་དོ་ཞེས་བྱ་བ་མུ་བཞི་གསུངས་པའི་ཕྱིར་ཏེ། མུ་དང་པོ་ནི་ཕྱིར་མི་འོང་བ་ཁམས་གཉིས་ལས་འདོད་ཆགས་དང་བྲལ་བའོ། །

[Block 3321]
གཉིས་པ་ནི་བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའོ། །

[Block 3322]
གསུམ་པ་ནི་དགྲ་བཅོམ་པའོ། །

[Block 3323]
བཞི་པ་ནི་རྣམ་པ་དེ༌[^1896]དག་མ་གཏོགས་པའོ། །

[Block 3324]
ཡང་ན༌[^1897]བྱུང་བ་ནི་དགྲ་བཅོམ་པའོ། །

[Block 3325]
སྲིད་པ་ཚོལ་བ་རྣམས་ནི་སྲིད་པ་དང་བཅས་པ་དག་གོ། །

[Block 3326]
ཡང་ཟས་དུ་ཞིག་ནི་སེམས་ཅན་བྱུང་བ་རྣམས་གནས་པར་བྱེད་པ་ཡིན། དུ་ཞིག་ནི་སྲིད་པ་ཚོལ་བ་རྣམས་ལ་ཕན་འདོགས་པར་བྱེད་པ་ཡིན་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་ཐམས་ཅད་ཀྱང་གཉི་ག་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3327]
ཁམ་གྱི་ཟས་ཀྱང་དེ་ལ་ཆགས་པ་རྣམས་ཀྱི་ཡང་འབྱུང་བར་བྱེད་པ་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་ཟས་བཞི་ནི་ནད་དང་། འབྲས་དང་། ཟུག་རྔུའི་རྩ་བ་ཡིན་ནོ། །

[Block 3328]
རྒ་ཤིའི་རྐྱེན་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 3329]
ཡིད་ལ་སེམས་པ་ཡང་འདིར་གནས་པར་བྱེད་པ་ཡིན་པར་སྣང་སྟེ། འདི་སྐད་དུ་ལོ་ཉེས་ཀྱིས་ཉེན་པའི་ཕ་ཞིག་གིས་ཐལ་བའི་རྐྱལ་བ་ཁ་ཐུར་མས་གཏུར་ཏེ་ཕྱེ་ཡིན་ནོ། །

[Block 3330]
བར་དུ་བུ༌[^1898]གཉིས་ཤིག་ཡིད་ཆེས་པར་བྱས་པ་དང་། དེ་གཉིས་ཀྱང་དེ་ལ་རྟོག་པར་བྱེད་ཅིང་རིང་མོ་ཞིག་ཏུ་གནས་པར་གྱུར་ཏོ། །
--- END BLOCKS ---
