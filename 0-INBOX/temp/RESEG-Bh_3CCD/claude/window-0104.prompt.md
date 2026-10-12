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
[Block 3641]
ལེན་པ་ནི་བཞི་སྟེ། འདོད་པ་དང་། ལྟ་བ་དང་། ཚུལ་ཁྲིམས་དང་། བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་དང་། བདག་ཏུ་སྨྲ་བའི་ལེན་པའོ། །

[Block 3642]
དེ་ལ་འདོད་པའི་ལེན་པ་ནི་རྫས་ཉི་ཤུ་རྩ་བཞིའོ། །

[Block 3643]
གཟུགས་དང་གཟུགས་མེད་པ་ན༌[^2293]གནས་པའི་ཉོན་མོངས་པ་ནི་བདག་ཏུ་ལྟ་བའི་ལེན་པ་སྟེ། རྫས་སུམ་ཅུ་རྩ་བརྒྱད་དོ། །

[Block 3644]
ལྟ་བའི་ལེན་པ་ནི་རྫས་སུམ་ཅུའོ། །

[Block 3645]
ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་ལེན་པ་ནི་རྫས་སུ༌[^2294]དྲུག་གོ། །

[Block 3646]
གཟུང་བར༌[^2295]བྱེད་པས་ན་ལེན་པའི་དོན་ཏོ། །

[Block 3647]
མདུད་པ་བཞི་སྟེ། མནར་སེམས་དང་། གནོད་སེམས་དང་། ཚུལ་ཁྲིམས་དང་། བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་དང་། འདི་བདེན་པ་ཞེས་མངོན་པར་ཞེན་པ་ནི་ལུས་ཀྱི་མདུད་པའོ། །

[Block 3648]
སྒྲིབ་པ་ལྔ་སྟེ། འདོད་པ་ལ་འདུན་པ་དང་། གནོད་སེམས་དང་། གཉིད་དང་རྨུགས་པ་དང་། རྒོད་འགྱོད་དང་། ཐེ་ཚོམ་མོ། །

[Block 3649]
མཐོང་བའི་ལམ་དུ་ཤེས་པ་བཅུ་ནི་ཆོས་ཤེས་པ་དང་། རྗེས་སུ་འགྲོ་བ་ཤེས་པ་དང་། ཀུན་རྫོབ་ཀྱི་ཤེས་པ་དང་། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དང་། སྡུག་བསྔལ་ཤེས་པ་དང་། ཀུན་འབྱུང་བ་ཤེས་པ་དང་། འགོག་པ་ཤེས་པ་དང་། ལམ་ཤེས་པ་དང་། ཟད་པ༌[^2296]ཤེས་པ་དང་། མི་སྐྱེ་བ་ཤེས་པའོ། །

[Block 3650]
བཟོད་པ་བརྒྱད་དེ། སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་དང་། དེ་བཞིན་དུ་སྡུག་བསྔལ་ལ་རྗེས་སུ་འགྲོ་བ་ཤེས་པའི་བཟོད་པ་དང་། དེ་བཞིན་དུ་ཀུན་འབྱུང་བ༌[^2297]དང་། འགོག་པ་དང་། ལམ་དང་ལམ་གྱི་བདེན་པ་རྣམས་ལ་ཤེས་པར་བྱའོ། །

[Block 3651]
སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་སྐྱེ་བར་གྱུར་པས་འདོད་པ་ཐོབ་པའི་སྡུག་བསྔལ་གྱི་མཐོང་བས་སྤོང་བ་ཉོན་མོངས་པ་ཐོབ་པ་ལ་བརྟེན་ཏེ་འགོག་པར་འགྱུར་རོ། །

[Block 3652]
ཆོས་ཤེས་པ་ཡང་དེ་རྣམས་ཀྱི་དེ༌[^2298]ཁོ་ན་མྱ་ངན་ལས་འདས་པ་ཐོབ་པ་ལ་བརྟེན་ཏེ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3653]
སྡུག་བསྔལ་ཉིད་རྗེས་སུ་འགྲོ་བའི་ཤེས་པའི་བཟོད་པ་སྐྱེ་བར༌[^2299]འགྱུར་བས་གཟུགས་དང་གཟུགས་མེད་པ་ན་གནས་པའི་སྡུག་བསྔལ་མཐོང་བས་སྤོང་བའི་ཉོན་མོངས་པ་ཐོབ་པ་བླངས་ཏེ་འགོག་པར་འགྱུར་རོ། །

[Block 3654]
རྗེས་སུ་འགྲོ་བ་ཤེས་པ་ཡང་དེ་རྣམས་ཀྱི་མྱ་ངན་ལས་འདས་པའི་ཐོབ་པ་བླངས་ཏེ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3655]
དེ་ལ་བཟོད་པ་རྣམས་ནི་བར་ཆད་མེད་པའི་ལམ་མོ། །ཤེས་པ་ནི་གྲོལ་བའི་ལམ་མོ། །

[Block 3656]
དེ་ལྟར་ཀུན་འབྱུང་བ་དང་། འགོག་པ་དང་། ལམ་རྣམས་སུ་སེམས་བཞི་བཞིར་ཤེས་པར་བྱའོ། །

[Block 3657]
སེམས་རྣམ་པ་བཅུ་དྲུག་གིས་བག་ལ་ཉལ་བརྒྱད་ཅུ་རྩ་བརྒྱད་སྤངས་པས་བདེན་པ་བཞི་པོ་མངོན༌[^2300]དུ་གྱུར་པ་དང་། རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ཡང་ཐོབ་པར་འགྱུར་རོ། །

[Block 3658]
བསྒོམ་པས་སྤང་བར་བྱ་བ་བཅུ་ལྷག་པར༌[^2301]གྱུར་པ་ནི་འདོད་པ་ན་གནས་པ་བཞི་དང་། གཟུགས་དང་གཟུགས་མེད་པ་ལ་གནས་པ་གསུམ་གསུམ་མོ། །

[Block 3659]
དེ་ལ་འདོད་པ་ན་གནས་པ་ནི་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་དང་། ང་རྒྱལ་དང་། མ་རིག་པ་གཅིག་ཏུ་བྱས་ཏེ། རྣམ་པ་དགུར་འགྱུར་ཏེ། དམན་པ་དང་། བར་པ་དང་། རབ་ཀྱི་དབྱེ་བས་སོ། །

[Block 3660]
དེ་ལ༌[^2302]རབ་ཀྱི་རབ༌[^2303]ཉོན་མོངས་པ་ལ་དམན་པའི་ཡང་དམན་པ་འཕགས་པའི་ལམ་ནི་གཉེན་པོ་ཡིན་ནོ། །

[Block 3661]
ཉོན་མོངས་པའི་རྣམ་པ་དྲུག་སྤངས་པ་ལན་ཅིག་ཕྱིར་འོང་བའོ། །

[Block 3662]
རྣམ་པ་དགུ་པོ་སྤངས་པས་ཕྱིར་མི་ལྡོག་པའོ། །

[Block 3663]
ཇི་ལྟར་འདོད་པ་ན་གནས་པའི་ཉོན་མོངས་པ་རྣམ་པ་དགུ་དང་། དེ་རྣམས་ཀྱི་ཡང་བར་ཆད་མེད་པ་དང་། རྣམ་པར་གྲོལ་བའི་ལམ་ཞེས་བྱ་བ་དགུ་གཉེན་པོ་ཡིན་པ་དེ་བཞིན་དུ་ཡང་ས་རེ་རེ་ལ་ཉོན་མོངས་པ་རྣམ་པ་དགུ་དགུ་དང་། དེ་རྣམས་ཀྱི་གཉེན་པོ་ཡང་དེ་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 3664]
དེའི་ཕྱིར་སྔ་མ་སྔ་མ་སྤོང་བས༌[^2304]ཕྱི་མ་ཕྱི་མ་ཉེས་པ༌[^2305]རྣམས་མི་གནས་པས་སྲིད་པའི་རྩེ་མོ་པ་དམན་ཡང་དམན༌[^2306]པ་ཉོན་མོངས་པའི་རྣམ་པ་རབ་ཏུ་སྤངས་པས་དགྲ་བཅོམ་པར་འགྱུར་རོ། །

[Block 3665]
འབྲས་བུ་བཞིའི་བར་ན་གནས་པ་རྣམས་ནི་ལམ་དུ་ཞུགས་པར་ཤེས་པར་བྱའོ། །

[Block 3666]
སྡུག་བསྔལ་བ་ལ་སོགས་པ་འཕགས་པའི་བདེན་པ༌[^2307]བཞིའི་ཡུལ་ཅན་སྐད་ཅིག་མ་བཅོ་ལྔའི་བདག་ཉིད་མཐོང་བའི་ལམ་དང་། བཅུ་དྲུག་པ་བསྒོམ་པའི་ལམ་གྱིས་མདོར་བསྡུས་ཏེ་ལམ་གཉིས་ཀྱིས་ཉོན་མོངས་པ་རབ་ཏུ་སྤངས་པར་འགྱུར་རོ། །

[Block 3667]
ཇི་སྐད་དུ།

[Block 3668 [VERSE]]
མ་མཐོང་མཐོང་ཕྱིར་མཐོང་བའི་ལམ། །
དེར་ནི་སྐད་ཅིག་བཅོ་ལྔ་ཡིན། །
བཅུ་དྲུག་པ་ནི་བསྒོམ་པའི་ལམ། །

[Block 3669]
ཞེས་བྱ་བ་ལ་སོགས་པ་འབྱུང་ངོ་། །དེའི་ཕྱིར་མཐོང་བ་དང་བསྒོམ་པའི་ལམ་ལ་དམིགས་པའི་ཤེས་རབ་དེ་ལྟ་བུས་ཉོན་མོངས་པ་རྣམས་མཐར་བྱེད་པས་ན་ཤེས་རབ༌[^2308]མཐར་བྱེད་དོ། །

[Block 3670]
དྲང་བའི་དོན་ནི་མི་མཐུན་པ་དང་གཉེན་པོའི་ལམ་བརྗོད་དོ།[^2309] །

[Block 3671]
རྣམ་པར་རྟོག་པའི་བདག་ཉིད་ཅན་ནི་ཤེས་རབ་སྟེ་ཞེས་པ་ལ། རྟོག་པ་ནི་གསུམ་སྟེ། སྣང་བ་དང་། སྣང་བ་མཆེད་པ་དང་། སྣང་བ་ཐོབ་པའོ། །

[Block 3672]
དེ་རྣམས་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས༌[^2310]འོད་གསལ་བར་འཇུག་པས་མཐར་བྱེད་པས་ཤེས་རབ་མཐར་བྱེད་དོ། །

[Block 3673]
ངེས་པའི་དོན་ནི་སེམས་རྣམ་པར་དག་པ་བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3674]
རྡོ་རྗེ་དམ་ཚིག་གིས་ཞེས་པ་ནི་ཁྲོ་བོའི་གཟུགས་དང་ཧ་ཧ་དགོད་པ་དང་གསོད་པ་ལ་སོགས་པ་དྲག་པོ་ལས་ཀྱི་རབ་འབྱམས་རྣམས་ཀྱིས་སོ། །

[Block 3675]
གདུག་པ་ནི་བརྒྱ་བྱིན་ལ་སོགས་པ་ཕྱོགས་སྐྱོང་བ་རྣམས་སོ། །

[Block 3676]
དེ་རྣམས་སྐྲག་པར༌[^2311]མཛད་པ་ནི་དགུག་པ་དང་ཕུར་བུས་གདབ་པ་དང་། བརྡུང་བའི་མཚན་ཉིད་དོ། །

[Block 3677]
ཡང་ན་ཞེས་བྱ་བ་འདིས་ཕྱོགས་གཞན་བཤད་པ་ཡིན་ཏེ། འཇིག་རྟེན་པའི་མཁའ་འགྲོ་མ་རྣམས་ནི། ཨུ་མ་དང་། བདེ་ཕྱོགས་མ་དང་། དཔལ་མོ་དང་། གྲགས་པ་མ་ལ་སོགས་པའོ། །

[Block 3678]
དེ་རྣམས་སྐྲག་པར་མཛད་པ་ནི་ནན༌[^2312]གྱིས་ཕྲོགས་ཏེ་ལོངས་སྤྱོད་པའོ། །

[Block 3679]
ཁྲོ་བོའི་གཟུགས་ཀྱིས་དེ་དག་གདུལ་བའི་ཕྱིར་རོ། །

[Block 3680]
ཇི་སྐད་དུ།
--- END BLOCKS ---
