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
བདེ་བ་དང་། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་ཡང་མ་ཡིན་པ་ལ་ནི་གཟུགས་ཀྱི་སྲེད་པའོ། །

[Block 3047]
བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་ཡང་མ་ཡིན་པ་ལ་ནི་གཟུགས་མེད་པའི་སྲེད་པའོ། །

[Block 3048]
དེའི་འོག་ཏུ་ཚོར་བ་ཡིད་དུ་འོང་བ་ལ་སྲེད་པ་ལས་འདོད་པ་ལ་སོགས་པ་ཉེ་བར་ལེན་ཏེ། དེ་ལ་འདོད་པ་རྣམས་ནི་འདོད་པའི་ཡོན་ཏན་ལྔ་དག་གོ། །

[Block 3049]
ལྟ་བ་དག་ནི་དྲུག་ཅུ་རྩ་གཉིས་ཏེ། ཚངས་པའི་དྲ་བ་ལས་ཇི་སྐད་འབྱུང་བ་བཞིན་ནོ། །

[Block 3050]
ཚུལ་ཁྲིམས་ནི་འཆལ་པའི་ཚུལ་ཁྲིམས་སྤོང་བའོ། །

[Block 3051]
བརྟུལ་ཞུགས་ནི་ཁྱི་དང་བ་ལང་གི་བརྟུལ་ཞུགས་ལ་སོགས་པ་དང་། ཇི་སྐད་དུ་གཅེར་བུ་པ་ལ་སོགས་པ་རྣམས་ནི་སྒྲེན་མོ་གོས་མེད་པ་ཡིན་ནོ་ཞེས་རྒྱས་པར་གསུངས་པ་ལྟ་བུ་དང་། བྲམ་ཟེ་དང་། ཕྱུགས་བདག་པ་དང་། ཀུན་ཏུ་རྒྱུ་ལ་སོགས་པ་དག་དབྱུ་གུ་དང་གཡང་གཞི་དང་། རལ་བུ་དང་། ཐལ་བ་དང་། དབྱུ་གུ་གསུམ་དང་སྒྲེ་བོ་ལ་སོགས་པ་ཡང་དག་པར་ལེན་པའོ། །

[Block 3052]
བདག་ཏུ་སྨྲ་བ་ནི་ལུས་ཏེ། དེ་ལ་བདག་ཏུ་སྨྲ་བ་ཡོད་པས་ན་བདག་ཏུ་སྨྲ་བའོ། །

[Block 3053]
གཞན་དག་ན་རེ་བདག་ཏུ་ལྟ་བ་དང་། ངའོ་སྙམ་པའི་ང་རྒྱལ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། འདི་གཉིས་ཇི་ལྟར་ན༌[^1731]བདག་ཏུ་སྨྲ་བ་ཉིད་ཡིན་ནོ་ཞེ་ན་འདི་གཉིས་ཀྱང༌[^1732]བདག་གོ་ཞེས་སྨྲ་བའི་ཕྱིར་རོ། །

[Block 3054]
བདག་མེད་པའི་ཕྱིར་བདག་ཏུ་སྨྲ་བ་ཉེ་བར་ལེན་པ་ཞེས་བྱ་སྟེ། ཇི་སྐད་དུ་དགེ་སློང་དག་བདག་དང་བདག་གི་ཞེས་བྱ་བ་ནི་བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་ཐོས་པ་དང་མི་ལྡན་པ་བཏགས་པའི་རྗེས་སུ་ལྷུང་བར་ཟད་ཀྱི། འདི་ལ་བདག་གམ་བདག་གི་ནི་མེད་དོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 3055]
དེ་དག་ཉེ་བར་ལེན་པ་ནི་དེ་དག་ལ་འདུན་པ་དང་། འདོད་ཆགས་གང་ཡིན་པ་སྟེ། བཅོམ་ལྡན་འདས་ཀྱིས་ཐམས་ཅད་ལས་ཇི་སྐད་དུ་ཉེ་བར་ལེན་པ་གང་ཞེ་ན། འདི་ལ་འདུན་པའི་འདོད་ཆགས་གང་ཡིན་པའོ་ཞེས་བཤད་པ་ལྟ་བུའོ། །

[Block 3056]
ཡང་ལེན་པའི་རྐྱེན་གྱིས་ཡང་སྲིད་པའི༌[^1733]ལ་སོགས་པར་བྱེད་པ་དེ་ནི་སྲིད་པ་ཡིན་ཏེ་མདོ་ལས།

[Block 3057]
ཀུན་དགའ་བོ་ཚེ་ཕྱི་མ་ལ་ཡང་སྲིད་པ་མངོན་པར་འགྲུབ་པར་བྱེད་པའི་ལས་གང་ཡིན་པ་དེ་ནི་འདིར༌[^1734]སྲིད་པ་ཡང༌[^1735]ཡིན་ནོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 3058]
སྲིད་པའི་རྐྱེན་གྱིས་རྣམ་པར་ཤེས་པ་འཇུག་པའི་ཚུལ་དུ་མ་འོངས་པའི་སྐྱེ་བ་ནི་སྐྱེ་བ་ཡིན་ཏེ།[^1736] ཕུང་པོ་ལྔ་པོ༌[^1737]ཡིན་ནོ། །

[Block 3059]
སྐྱེ་བ་ཡོད་ན་རྒ་ཤི་འབྱུང་སྟེ། མདོ་ལས་ཇི་སྐད་བསྟན་པ་ལྟ་བུའོ། །

[Block 3060]
དེ་ལྟར་འདི་འབའ་ཞིག་ཅེས་བྱ་བ་ནི་བདག་དང་བདག་གི་དང་བྲལ་བའོ། །

[Block 3061]
སྡུག་བསྔལ་གྱི་ཕུང་པོ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་གྱི་ཚོགས་ཐོག་མ་དང་ཐ་མ་མེད་པའོ། །

[Block 3062]
ཡང་དག་པར་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བ་ནི་སྐྱེ་བའོ། །

[Block 3063]
བྱེ་བྲག་ཏུ་སྨྲ་བའི་ལུགས་ནི་སྔར་བཤད་པ་གང་ཡིན་པ་དེ་ཁོ་ན་ཡིན་ནོ། །

[Block 3064 [HEADING]]
##### མ་རིག་པ། ^3-1-11-10-0

[Block 3065]
ཡང་མ་རིག་པ་ཞེས་བྱ་བའི་དོན་གང་ཡིན། རིག་པ་མ་ཡིན་པ་གང་ཡིན་པའོ། །

[Block 3066]
མིག་ལ་སོགས་པ་དག་ལ་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 3067]
འོ་ན་ནི་རིག་པ་མེད་པ་ཡིན་ནོ། །

[Block 3068]
དེ་ལྟ་ན༌[^1738]ཅི་ཡང་མ་ཡིན་པར་འགྱུར་ཏེ། དེ་ཡང་རིག་པ༌[^1739]མ་ཡིན་ནོ། །

[Block 3069]
དེ་ལྟ་བས་ན།

[Block 3070 [VERSE]]
རིག་པའི་མི་མཐུན་ཕྱོགས་ཆོས་གཞན། །
མ་རིག་མི་མཛའ་བརྫུན་སོགས་བཞིན། །

[Block 3071]
ཇི་ལྟར་མཛའ་བོ་ཞེས༌[^1740]བཟློག་ན་དེའི་མི་མཐུན་པའི་ས༌[^1741]ཕྱོགས་སུ་གྱུར་པ་མི་མཛའ་བ་འགའ་ཞིག་ཡོད་ཀྱི། མཛའ་བོ་ལས་གཞན་པ་གང་ཡིན་པ་ཡང་མ་ཡིན་ལ། མཛའ་བོ་མེད་པ་ཡང་མ་ཡིན་པ་དང་། བདེན་པ་ཞེས་བྱ་བ་ནི་བདེན་པའོ། །

[Block 3072]
དེ་མི་མཐུན་པའི་ཕྱོགས་སུ་གྱུར་པའི་ཚིག་ནི་མི་བདེན་པ་ཡིན་པ་དང་། ཆོས་མ་ཡིན་པ་དང་། དོན་མ་ཡིན་པ་དང་། [^1742]བྱ་བ་མ་ཡིན་པ་ལ་སོགས་པ་ཡང༌[^1743]ཆོས་ལ་སོགས་པའི་མི་མཐུན་པར་གྱུར་པ་དེ་བཞིན་དུ་མ་རིག་པ་ཡང་རིག་པའི་མི་མཐུན་པར་གྱུར་པ་ཆོས་གཞན་ཞིག་ཏུ་བལྟ་བར་བྱའོ། །

[Block 3073]
འདི་ག་ལས་ཤེ་ན།

[Block 3074 [VERSE]]
རྐྱེན་གྱི་དངོས་པོར་བསྟན་པའི་ཕྱིར་རོ། །
གཞན་ཡང་ཀུན་སྦྱོར་སོགས་ཀྱི༌[^1744]ཕྱིར། །

[Block 3075]
མདོ་དག་ལས་མ་རིག་པ་ནི་ཀུན་ཏུ་སྦྱོར་བ་དང་། འཆིང་བ་དང་། ཕྲ་རྒྱས་དང་། ཆུ་བོ་དང་། སྦྱོར་བ་ཞེས་བྱའོ་ཞེས་གསུངས་ཏེ། མེད་པ་ཙམ་ནི་དེ་ལྟ་བུ་ཡིན་པར་འོངས་པ༌[^1745]མ་ཡིན་ལ་མིག་ལ་སོགས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 3076]
དེ་ལྟ་བས་ན་མ་རིག་པ་ནི༌[^1746]ཆོས་གཞན་ཁོ་ན་ཞིག་ཡིན་ནོ། །

[Block 3077]
འོ་ན་ནི་དཔེར་ན་ཆུང་མ་ངན་པ་ལ་ཆུང་མ་མ་ཡིན་ཞེས་བྱ་བ་དང་། བུ་ངན་པ་ལ་བུ་མ་ཡིན་པ༌[^1747]ཞེས་བྱ་བ་ལྟར་མ་རིག་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 3078]
གལ་ཏེ། ཤེས་རབ་ངན་པའོ་མིན་ལྟ་ཕྱིར། །སྨད་པའི་ཤེས་རབ་ནི་ཉོན་མོངས་པ་ཅན་ཡིན་ན་དེ་ཡང་ལྟ་བའི་རང་བཞིན་ཡིན་པས་མ་རིག་པ་ཡིན་པར་མི་རུང་ངོ་། །འོ་ན་ནི་གང་ལྟ་བའི་རང་བཞིན་མ་ཡིན་པ་དེ་ཡིན་པར་འགྱུར་རོ། །

[Block 3079]
དེ་ཡང་ཡིན་པར་མི་འོས་སོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ལྟ་བ་དེ་དང་མཚུངས་ལྡན་ཕྱིར། །གལ་ཏེ་མ་རིག་པ་ཤེས་རབ་ཡིན་པར་གྱུར་ན་ཤེས་རབ་ཀྱི༌[^1748]རྫས་ཉིད༌[^1749]མཚུངས་པར་མི་ལྡན་པའི་ཕྱིར་ལྟ་བ་དེ་དང་མཚུངས་པར་ལྡན་པར་མི་འགྱུར་རོ། །ཤེས་རབ་ཉོན་མོངས་བསྟན་ཕྱིར་རོ། །ཞེས་བྱ་བ་འདི་ལས་ཀྱང་འགྲུབ་སྟེ།

[Block 3080]
མདོ་ལས།

[Block 3081]
འདོད་ཆགས་ཀྱིས་ཉེ་བར་ཉོན་མོངས་པ་ཅན་དུ་གྱུར་པའི་སེམས་ནི་རྣམ་པར་མི་འགྲོལ་ལོ། །

[Block 3082]
མ་རིག་པས་ཉེ་བར་ཉོན་མོངས་པ་ཅན་དུ་གྱུར་པའི་ཤེས་རབ་ནི་རྣམ་པར་མི་འདག་གོ་ཞེས་གསུངས་ཏེ། ཤེས་རབ་དེ་ཉིད་ཤེས་རབ་དེའི་ཉོན་མོངས་པ་འདོད་ཆགས༌[^1750]རིགས་པ་མ་ཡིན་པས་ཇི་ལྟར་སེམས་ཀྱིས༌[^1751]ཉེ་བར་ཉོན་མོངས་པ་འདོད་ཆགས་རིགས་ཐ་དད་པ་གཞན་ཡིན་པ་ལྟར་ཤེས་རབ་ཀྱི༌[^1752]མ་རིག་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 3083]
ཡང་ཅིའི་ཕྱིར་འདི་ལྟར་ཤེས་རབ་ཉོན་མོངས་པ་ཅན་དང་། ཤེས་རབ་དགེ་བ་འདྲེས༌[^1753]ན་རྣམ་པར་མི་འདག་པས་དེའི་ཕྱིར་འདི་དེའི་ཉེ་བའི་ཉོན་མོངས་པ་ཡིན་པར་མི་འདོད། འདོད་ཆགས་ཀྱིས་ཉེ་བར་ཉོན་མོངས་པ་ཅན་དུ་གྱུར་པའི་སེམས་རྣམ་པར་མི་འགྲོལ་བ་གང་ཡིན་པ་དེ་ཡང་གདོན་མི་ཟ་བར་འདོད་ཆགས་ཀྱིས་ཀུན་ནས་དཀྲིས་པ་ཡིན་ནམ་ཅི། གང་རྣམ་པར་མི་འགྲོལ་བ་དེ་ནི་འདོད་ཆགས་ཀྱིས་དེ་ལྟར་ཉེ་བར་བཅོམ་པ་ཡིན་ལ། བག་ཆགས༌[^1754]རྣམ་པར་བཟློག་པ་ནི་རྣམ་པར་གྲོལ་བར་འགྱུར་རོ། །

[Block 3084]
དེ་བཞིན་དུ་མ་རིག་པས་ཉེ་བར་ཉོན་མོངས་པ་ཅན་དུ་གྱུར་པའི་ཤེས་རབ་རྣམ་པར་མི་འདག་པས་མ་རིག་པས་ཉེ་བར་བཅོམ་པ་ཡིན་པར་ཡོངས་སུ་བརྟག་པར་བྱའོ། །

[Block 3085]
ཡོངས་སུ་རྟོག་པ་ལ་ནི་སུ་ཞིག་བཟློག་སྟེ། མ་རིག་པ་རིགས་གཞན་ཁོ་ན་ཞིག་ཡོད་དོ་ཞེས་བརྗོད་དོ། །
--- END BLOCKS ---
