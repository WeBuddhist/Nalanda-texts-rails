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

[Block 3086]
གང་ཡང་ཉོན་མོངས་པ་ཅན༌[^1755]ཐམས་ཅད་མ་རིག་པ་ཡིན་ནོ་སྙམ་དུ་སེམས་པ་དེའི་ཡང་འདི་ཉིད་ཀྱིས༌[^1756]བསལ་བ་ཡིན་ཏེ། ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱི་རང་བཞིན་ཡིན་ན་ཀུན་ཏུ་སྦྱོར་བ་ལ་སོགས་པའི་ནང་དུ་ཡང་ལོགས་ཤིག་ཏུ་བཤད་པར་མི་འགྱུར་ཞིང་། ལྟ་བ་ལ་སོགས་པ་ཕན་ཚུན་མཚུངས་པར་ལྡན་པ་མེད་པའི་ཕྱིར་ལྟ་བ་འམ་ཉོན་མོངས་པ་གཞན་དང་ཡང༌[^1757]མཚུངས་པར་ལྡན་པར་མི་འགྱུར་ལ། སེམས་ཀྱང་མ་རིག་པས་ཉེ་བར་ཉོན་མོངས་པ་ཅན་དུ་གྱུར་པ་ཁོ་ནར་བཤད་པར་འགྱུར་རོ། །

[Block 3087]
འོན་ཏེ་བྱེ་བྲག་ཏུ་བྱ་བའི་ཕྱིར་དེ་སྐད་དུ་བཤད་དོ་ཞེས་བྱ་བར་འདོད་ན་ནི་ཤེས་རབ་ལ་ཡང་མ་རིག་པ་བྱེ་བྲག་ཏུ་བྱ་དགོས་པར་འགྱུར་རོ། །

[Block 3088]
མ་རིག་པ་ཆོས་གཞན་ཞིག་ཡིན་ལ༌[^1758]རག་ན་དེའི་རང་བཞིན་ཅི་ཡིན། བདེན་པ་དང་དཀོན་མཆོག་དང་། ལས་དང་འབྲས་བུ་རྣམས་མི་གསལ་བའོ། །

[Block 3089]
མི་གསལ་བ་ཞེས་བྱ་བ་འདི་ཅི་ཡིན་པ་འདི་ཡང་མི་ཤེས་སོ། །

[Block 3090]
གལ་ཏེ་གསལ་བ་མ་ཡིན་པ་ཞིག་གམ། གསལ་བ་མེད་པ་ཞིག་ཡིན་ན་ནི་མ་རིག་པ་ལ་ནི༌[^1759]ཇི་ལྟ་བ་དེ་ཁོ་ན་བཞིན་དུ་སྐྱོན་དུ་འགྱུར་རོ། །

[Block 3091]
འོན་ཏེ་གསལ་བའི་མི་མཐུན་པའི་ཕྱོགས་སུ་གྱུར་པ། ཆོས་གཞན་ཞིག་ཡིན་ནོ་ཞེ་ན་ཡང་དེ་བཞིན་དུ་དེ་ཅི་ཡིན་པ་འདི་མི་ཤེས་སོ་ཞེ་ན། ཆོས་རྣམས་བསྟན་པ་དེ་ལྟ་བུ་ཡང་ཡོད་དེ། དཔེར་ན་མིག་གང་ཞེ་ན། གཟུགས་དང་བ་མིག་གི་རྣམ་པར་ཤེས་པའི་རྟེན་གང་ཡིན་པའོ་ཞེས་གསུངས་པ་ལྟ་བུ་དང་། [^1760]བཙུན་པ་ཆོས་སྐྱོབ༌[^1761]ན་རེ་ངའོ་སྙམ་དུ་སེམས་ཅན་ལ་འཇུག་པ་ནི་མ་རིག་པའོ་ཞེས་ཟེར་རོ། །

[Block 3092]
ངའོ་སྙམ་པའི་ང་རྒྱལ་ལས་གཞན་པའི་འཇུག་པ་གང་ཞིག་ཡིན་ཞེ་ན། མདོ་ལས་བདག་གིས་དེ་ལྟར་ཤེས། །དེ་ལྟར་མཐོང་སྟེ། སྲེད་པ་ཐམས་ཅད་དང་། ལྟ་བ་ཐམས་ཅད་དང་། འཇུག་པ་ཐམས་ཅད་དང་། ངར་འཛིན་པ་དང་ང་ཡིར་འཛིན་པ་དང་ངའོ་སྙམ་པའི་ང་རྒྱལ་ལ་མངོན་པར་ཞེན་པའི་ཕྲ་རྒྱས་ཐམས་ཅད་སྤངས་ཤིང་ཡོངས་སུ་ཤེས་ནས་གྲིབ་མ་མེད་པར་མྱ་ངན་ལས་འདས་སོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་ཡིན་ནོ། །

[Block 3093]
འཇུག་པ་དེ་ཡོད་ཀྱང་དེ་ནི་མ་རིག་པ་འདི་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ག་ལས་ཤེ་ན་འདི་ལྟར༌[^1762]ཉོན་མོངས་པ་གཞན་ཡིན་ནོ་ཞེས་བརྗོད་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 3094]
ང་རྒྱལ་གཞན་ཡང་ཡོད་པ་ཁོ་ན་མ་ཡིན་ནམ་ཞེ་ན། འདི་ལ་དཔྱད་པར་ཆད་ན་བརྗོད་པ་མང་པོར་གྱུར༌[^1763]ཏེ། དེ་ལྟ་བས་ན་འདི་ནི་བཞག་གོ། །

[Block 3095 [HEADING]]
##### མིང་དང་གཟུགས། ^3-1-11-11-0

[Block 3096]
ཡང་མིང་དང་གཟུགས་ཞེས་བྱ་བ་འདིའི་དོན་ཅི་ཞེ་ན།

[Block 3097 [VERSE]]
གཟུགས་ནི་རྒྱ་ཆེར་བཤད་པ་ཡིན་ནོ། །
མིང་ནི་གཟུགས་ཅན་མིན་ཕུང་པོ། །

[Block 3098]
ཅིའི་ཕྱིར་ཞེ་ན། མིང་དང་དབང་པོ་དང་དོན་གྱི་དབང་གིས་དོན་རྣམས་ལ་གཞོལ་བས་ན་མིང་ངོ་། །མིང་གང་གི་དབང་གིས་ཤེ་ན། འཇིག་རྟེན་ན༌[^1764]གྲགས་པ་མིང་ཡིན༌[^1765]པ་སྟེ། དོན་དེ་དང་དེ་དག་གོ་བར་བྱེད་པ་བ་ལང་དང་། རྟ་དང་། གཟུགས་དང་། རོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 3099]
དེ་ཡང་ཅིའི་ཕྱིར་མིང་ཉིད་ཡིན་ཞེ་ན། འོན་ཏེ༌[^1766]དེ་དག་ལ་མིང་དེ་གཞོལ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3100]
གཞན་དག་ན་རེ་འདིར་ལུས་བོར་ནས་སྐྱེ་བ་གཞན་དུ་གཞོལ་བའི་ཕྱིར་མིང་ནི་གཟུགས་ཅན་མ་ཡིན་པའི་ཕུང་པོ་དག་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3101]
སྐྱེ་མཆེད་དྲུག་ནི་བཤད་ཟིན་ནོ། །

[Block 3102 [HEADING]]
##### རེག་པ། ^3-1-11-12-0

[Block 3103]
ད་ནི༌[^1767]རེག་པ་བརྗོད་པར་བྱ་སྟེ། [^1768]མིག་གི་འདུས་ཏེ་རེག་པ་ནས་ཡིད་ཀྱི་འདུས་ཏེ་རེག་པའི་བར་རོ། །

[Block 3104]
དེ་དག་ཀྱང་། འདུས་ཏེ་བྱུང་བ་ནི།[^1769] དབང་པོ་དང་ཡུལ་དང་རྣམ་པར་ཤེས་པ་དང་གསུམ་འདུས་པ་ལས་སྐྱེས་པའོ། །

[Block 3105]
རེ་ཞིག་ལྷན་ཅིག་སྐྱེ་བའི་ཕྱིར་དབང་པོ་ལྔ་ནི་དོན་དང་རྣམ་པར་ཤེས་པ་དག་དང་འདུ་བར་ཡང་རིགས་ན། ཡིད་ཀྱི་དབང་པོ་འགགས་པའི༌[^1770]ཆོས་དང་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་མ་འོངས་པ་དང་ད་ལྟར་གྱི་དག་དང་ཇི་ལྟར་འདུ༌[^1771]ཞེ་ན། རྒྱུ་དང་འབྲས་བུའི་དངོས་པོ་གང་ཡིན་པ་དེ་ཉིད་དེ་དག་གི་འདུ་བ་ཡིན་ནོ། །

[Block 3106]
ཡང་ན་གསུམ་པོ་དེ་དག་ཐམས་ཅད་ཀྱང་རེག་པ་བསྐྱེད་པར་བྱ་བ་ལ་མཐུན་པ་ཡིན་པའི་ཕྱིར་འབྲས་བུ་གཅིག་པའི་དོན་ནི་འདུ་བའི་དོན་ཏོ། །

[Block 3107]
འདི་ལ་སློབ་དཔོན་རྣམས་ཀྱི་བློ་ཐ་དད་པར་གྱུར་ཏེ། [^1772]ཁ་ཅིག་ན་རེ་འདུས་པ་ཉིད་རེག་པ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། འདིར་མདོའི་ཁུངས་དེ་ལྟར༌[^1773]ན་ཆོས་གསུམ་པོ་འདི་དག་འབྲེལ་ཅིང་འདུས་ལ་ཚོགས་པ་གང་ཡིན་པ་དེ་ནི་རེག་པ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡང་ཁྱེར་ཏེ་འོང་བར་བྱེད་དོ། །

[Block 3108]
ཁ་ཅིག་ན་རེ༌[^1774]སེམས་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་གཞན་ཁོ་ན་ཞིག་རེག་པ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། འདིར་མདོའི་ཁུངས་ཆོས་ཀྱི་རྣམ་གྲངས་དྲུག་ཚན་དྲུག་གང་ཞེ་ན། ནང་གི་སྐྱེ་མཆེད་དྲུག་དང་། ཕྱིའི་ཡུལ༌[^1775]དྲུག་དང་། རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་དང་། རེག་པའི་ཚོགས་དྲུག་དང་། ཚོར་བའི་ཚོགས་དྲུག་དང་། སྲེད་པའི་ཚོགས་དྲུག་གོ་ཞེས་གསུངས་པ་ཡང་ཁྱེར་ཏེ་འོང་བར་བྱེད་དོ། །

[Block 3109]
འདིར་ནི་རེག་པའི་ཚོགས་དབང་པོ་དང་དོན་དང་རྣམ་པར་ཤེས་པ་དག་ལས་ལོགས་ཤིག་ཏུ་བསྟན་ཏོ། །

[Block 3110]
དེ་ལ་གང་དག་འདུས་པ་ཉིད་རེག་པ༌[^1776]ཡིན་ནོ་ཞེས་ཟེར་བ་དེ་དག་ནི་འདི་སྐད་དུ་ལོགས་ཤིག་ཏུ་བསྟན་པའི་ཕྱིར་ལོགས་ཤིག་ན་ཡོད་པ་ཁོ་ན༌[^1777]ཡང་མ་ཡིན་ཏེ། ཚོར་བ་དང་སྲེད་པ་དག་ཀྱང་ཆོས་ཀྱི་སྐྱེ་མཆེད་ལས་ལོགས་ཤིག་ན་ཡོད་པར་འགྱུར་དུ་འོང་ངོ་ཞེས་ལན་འདེབས་པར་བྱེད་དོ། །

[Block 3111]
དེ་ནི་ཉེས་པ་མེད་པ༌[^1778]དེ་དག་ལས་མ༌[^1779]གཏོགས་པའི་ཆོས་ཀྱི་སྐྱེ་མཆེད་ཀྱང་ཡོད་པའི་ཕྱིར་རོ། །

[Block 3112]
དེ་ལྟ་བུར་འདིར་ལྷག་མ་གང་ཞིག་སྨོས་སུ་རུང་བ་རེག་པར་གྱུར་པ་གསུམ་ལས་གཞན་གསུམ་ནི་མེད་དོ། །

[Block 3113]
གལ་ཏེ་རྣམ་པར་ཤེས་པ་མེད་པའི་དབང་པོ་དང་དོན་དག་ཡོད་དུ་ཟིན་ཀྱང་དབང་པོ་དང་དོན་མེད་པའི་རྣམ་པར་ཤེས་པ་ནི༌[^1780]མེད་དོ། །

[Block 3114]
དེ་ལྟ་བས་ན་གསུམ་བསྟན་ཟིན་པས་ཡང་རེག་པ་སྨོས་པ་ནི་དོན་མེད་པར་འགྱུར་རོ། །

[Block 3115]
ཁ་ཅིག་ན་རེ་མིག་དང་གཟུགས་ཐམས་ཅད་ཀྱང་མིག་གི་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་ཀྱི་རྒྱུ་མ་ཡིན་ལ། མིག་གི་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་ཀྱང་མིག་དང་གཟུགས་ཐམས་ཅད་ཀྱི་འབྲས་བུ་མ་ཡིན་པས་དེའི་ཕྱིར་གང་དག་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོ་ཡིན་པ་དེ་དག་ནི་རེག་པའི་དངོས་པོར་རྣམ་པར་གཞག་གོ་ཞེས་ཟེར་རོ། །

[Block 3116]
གང་དེ༌[^1781]དག་རེག་པ་ནི་འདུས་པ་ལས་གཞན་ནོ་ཞེས་ཟེར་བ་དེའི༌[^1782]ཆོས་གསུམ་པོ་འདི་དག་འབྲེལ་ཞིང་འདུས་ལ་ཚོགས་པ་གང་ཡིན་པ་དེ་ནི་རེག་པ་ཡིན་ནོ་ཞེས་གསུངས་པའི་མདོ་འདི་ལ་ཇི་ལྟར་ལན་འདེབས་ཤེ་ན། དེ་སྐད་དུ་མི་འདོན་ཏོ། །

[Block 3117]
ཡང་ན་ནི་འདི་རྒྱུ་ལ་འབྲས་བུ་བཏགས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3118]
བརྗོད་པ་འདི་རྒྱ་ཆེ་བའི་རྣམ་པ་ཧ་ཅང་མང་པོར་འཕྲོ་བ་ཡིན་པས་ཞར་ལ་འོངས་པས་ཆོག་གོ། །

[Block 3119]
ཆོས་མངོན་པ༌[^1783]རྣམས་ན་རེ་རེག་པ་གཞན་ཁོ་ན་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3120 [VERSE]]
རེག་པ་དྲུག་པོ་དེ་དག་ལས། །
ལྔ་ནི་ཐོགས་པའི་རེག་པ་ཡིན། །
དྲུག་པ་བླ་དགས་ཚིག་ཅེས་བྱ། །
--- END BLOCKS ---
