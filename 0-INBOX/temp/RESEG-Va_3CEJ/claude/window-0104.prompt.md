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
[Block 3641 [VERSE]]
དེ་དག་གི་ནི་ཕྱོགས་བཞི་ན། །
ཉི་ཤུས་བཅད་ན་ས་གཞི་བཟང་། །

[Block 3642]
སྐྱེད་མོས་ཚལ་དེ་དག་གི་ཕྱོགས་བཞི་དཔག་ཚད་ཉི་ཤུས་བཅད་པ་ན་ལྷ་རྣམས་ཀྱི་རྩེ་བའི་གནས་ས་གཞི་བཟང་པོ་ཕན་ཚུན་འགྲན་པ་ལྟ་བུར་མཛེས་པ་དང་ལྡན་པ་བཞི་ཡོད་དོ། །

[Block 3643]
གྲོང་ཁྱེར་གྱི་ཕྱི་རོལ་གྱི་ངོས།

[Block 3644 [VERSE]]
བྱང་ཤར་མཚམས་ན་ཡོངས་འདུ་སྟེ། །
ལྷོ་ནུབ་མཚམས་ན་ཆོས་བཟང་ངོ་། །

[Block 3645]
ཤིང་ས་བརྟོལ་ཡོངས་འདུ་ཞེས་བྱ་བ་སུམ་ཅུ་རྩ་གསུམ་པའི་ལྷ་རྣམས་ཀྱི་འདོད་པའི་དགའ་བ་མཆོག་གི་གནས་ཞིག་ཡོད་དེ། དེའི་རྩ་བ་ནི་དཔག་ཚད་ལྔ་བཅུ་ཟུག་གོ །གནམ་འཕང་དུ་ནི་དཔག་ཚད་བརྒྱ་འཕགས་སོ། །

[Block 3646]
ཡལ་ག་དང་། འདབ་མ་དང་། ལོ་མ་ནི་དཔག་ཚད་ལྔ་བཅུར་ཁྱབ་པར་གནས་སོ། །

[Block 3647]
དེའི་མེ་ཏོག་དང་། འདབ་མ་ཐམས་ཅད་རྒྱས་པའི་དྲི་ངད་རྫི་ཕྱོགས་སུ་ནི་དཔག་ཚད་བརྒྱར་ལྡང་ངོ་། །རྫི༌[^2086]ཕྱོགས་མ་ཡིན་པར་ནི་དཔག་ཚད་ལྔ་བཅུར་ལྡང་ངོ་། །རེ་ཞིག་རྫི་ཕྱོགས་སུ་ནི་རིགས༌[^2087]ན་རྫི་ཕྱོགས་མ་ཡིན་པར་གོ་ཇི་ལྟར་ཞེ་ན། ཁ་ཅིག་ན་རེ་ཤིང་ལས་མི་འདའ་བ་ལས་དགོངས་ཏེ་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 3648]
དེ་རྫི་ཕྱོགས་སུ་མ་ཡིན་པར་འགྲོ་བ་མ་ཡིན་གྱི། དྲི་དེ་ཉིད་ཀྱི་ཕུན་སུམ་ཚོགས་པ་ལྷའི་རླུང་ཆུང་ངུ་དག་གིས་བཀག་བཞིན་དུ་ཡང་དྲི་གཞན་གྱི་རྒྱུན་འབྱུང་བ་དེ་ལྟ་བུར་འདོད་པར་བྱའོ། །

[Block 3649]
རྒྱུན་ཆུང་བ་དང་། ཆེས་ཆུང་བ་དང་། ཆེས་ཤིན་ཏུ་ཆུང་བར་འགྱུར་བའི་ཕྱིར་མྱུར་བ་ཁོ་ནར་ཀུན་དུ་ཆད་པར་འགྱུར༌[^2088]ཏེ། དེ་བཞིན་དུ་ལམ་རིང་པོར་མི་འགྲོའོ། །

[Block 3650]
ཇི༌[^2089]མེ་ཏོག་གི་དྲིའི་རྒྱུན་དེ་རང་གི་འབྱུང་བ་ཁོ་ན་ལ་བརྟེན་ནས་འཇུག་གམ། འོན་ཏེ་རླུང་ལ་བརྟེན༌[^2090]ནས་ཀྱང་སྐྱེ་ཞེ་ན། སློབ་དཔོན་གྱི་འདོད་པ་ནི་དེ་ལ་ངེས་པ་མེད་དེ། གཉི་ག་ལྟར་ཡིན་པའོ། །

[Block 3651]
འོ་ན་བཅོམ་ལྡན་འདས་ཀྱིས།

[Block 3652 [VERSE]]
མེ་ཏོག་དྲི་ནི་རྫི་ཕྱོགས་མིན་མི་འགྲོ། །
རྩ་བའམ་རྒྱ་སྤོས་ཙན་དན་ཡང་མ་ཡིན། །
མཁས་རྣམས་དྲི་ནི་རྫི་ཕྱོགས་མིན་འགྲོ་སྟེ། །
སྐྱེས་བུ་དམ་པ་ཕྱོགས་རྣམས་ཀུན་དུ་འགྲོ། །

[Block 3653]
ཞེས་གང་གསུངས་པ་ཇི་ལྟར་དྲང་ཞེ་ན། མིའི་མེ་ཏོག་གི་དྲིའི་དབང་དུ་བྱས་ནས་གསུངས་པ་ཡིན་ནོ། །

[Block 3654]
དེ་ནི་འཇིག་རྟེན་ན་གྲགས་པ་ཡིན་ཏེ། དེ་ལ་མཐུ་དེ་ལྟ་བུ་ནི་མེད་དོ། །

[Block 3655]
ས་སྟོན་སྡེ་རྣམས༌[^2091]རྫི་ཕྱོགས་སུ་ནི་དཔག་ཚད་བརྒྱར་དྲིའི་ངད་ལྡང་ངོ་། །རླུང་མེད་ན་ནི་དཔག་ཚད་ལྔ་བཅུར་ལྡང་ངོ་ཞེས་འདོན་ཏོ། །

[Block 3656]
ལྷོ་ནུབ་ཀྱི་ཕྱོགས་ཆ་ན་གང་དུ་ལྷ་རྣམས་འཁོད་ནས་བྱ་བ་དང་བྱ་བ་མ་ཡིན་པ་འགྲོ་བར་བྱེད་པ་ལྷའི་འདུན་ས་ཆོས་བཟངས༌[^2092]ཞེས་བྱ་བ་ཡོད་དོ། །

[Block 3657]
རེ་ཞིག་དེ་ནི་སུམ་ཅུ་རྩ་གསུམ་པ་རྣམས་ཀྱི་སྣོད་གནས་པ་ཡིན་ནོ། །

[Block 3658 [HEADING]]
##### གཞལ་མེད་ཁང་ན་གནས་པའི་ལྷ། ^3-2-1-14-0

[Block 3659]
དེའི་སྟེང་ལྷ་རྣམས་གཞལ་མེད་ཁང་། །སུམ་ཅུ་རྩ་གསུམ་གྱི་སྟེང་གི་ལྷ་རྣམས་ནི་གཞལ་ཡས་ཁང་དག་ན་གནས་ཏེ། དེ་དག་ཀྱང་འཐབ་བྲལ་རྣམས་དང་། དགའ་ལྡན་རྣམས་དང་། འཕྲུལ་དགའ་རྣམས་དང་། གཞན་འཕྲུལ་དབང་བྱེད་རྣམས་དང་། སྔར་བཤད་པ་ཚངས་རིས་ལ་སོགས་པ་གནས་གཞན་བཅུ་དྲུག་ཏུ་གཏོགས་པ་རྣམས་ཏེ། དེ་ལྟར་ན་གང་དག་གི༌[^2093]སྣོད་མངོན་པ་ནི༌[^2094]མདོར་བསྡུ་ན་ལྷའི་རིས་ཉི་ཤུ་རྩ་གཉིས་པོ་དེ་དག་ཡིན་ནོ། །

[Block 3660 [HEADING]]
##### འདོད་པ་ན་སྤྱོད་པའི་ལྷའི་རིས་དྲུག། ^3-2-1-15-0

[Block 3661]
འདོད་པ་སྤྱོད་པ་དྲུག་ཡིན་ནོ། །

[Block 3662]
དེ་དག་ལས་འདོད་པ་ན་སྤྱོད་པའི་ལྷའི་རིས་དྲུག་པོ་འདི་ལྟ་སྟེ། རྒྱལ་ཆེན་བཞིའི་རིས་ནས་གཞན་འཕྲུལ་དབང་བྱེད་ཀྱི་བར་རྣམས་ནི་འདོད་པ་དག་ལ་སྤྱོད་ཀྱི་ལྷག་མ་རྣམས་ནི་མ་ཡིན་ནོ། །

[Block 3663]
དེ་དག་ཀྱང་།

[Block 3664 [VERSE]]
གཉིས་གཉིས་འཁྱུད་དང་ལག་བཅངས་དང་། །
དགོད་དང་བལྟས་པས་འཁྲིག་པ་ཡིན། །

[Block 3665]
ས་དང་འབྲེལ་པར་གནས་པ་རྒྱལ་ཆེན་བཞི་པ་དང་། སུམ་ཅུ་རྩ་གསུམ་པ་རྣམས་ནི་མི་རྣམས་ཇི་ལྟ་བ་བཞིན་དུ་གཉིས་གཉིས་ཀྱིས་འཁྲིག་གོ། །

[Block 3666]
དེ་དག་ལ་ཡང་ཁུ་ཆུ་མེད་པའི་ཕྱིར་རླུང་བཏང་བས་ཡོངས་སུ་གདུང་བ་དང་བྲལ་ལོ། །

[Block 3667]
འཐབ་བྲལ་བ་རྣམས་ནི་འཁྱུད་པས་འཁྲིག་པ་ཡིན་ཏེ། འཁྱུད་པ་ཙམ་གྱིས་ཡོངས་སུ་གདུང་བ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 3668]
དགའ་ལྡན་པ་རྣམས་ནི་ལག་བཅངས་བྱས་པས་སོ། །

[Block 3669]
འཕྲུལ་དགའ་བ་རྣམས་ནི་དགོད་པས་སོ། །

[Block 3670]
གཞན་འཕྲུལ་དབང་བྱེད་པ་རྣམས་ནི་བལྟས་པས་སོ། །

[Block 3671]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་ཐམས་ཅད་ཀྱང་གཉིས་ཀྱིས༌[^2095]གཉིས་སྤྲོད་པས༌[^2096]ཡིན་ནོ། །

[Block 3672]
བརྟགས་པ་ལས་བཤད་པ་ནི་དུས་ཀྱི་ཚད་ཡིན་ཏེ། ཇི་ཙམ་ཇི་ཙམ་དུ་ཡུལ་རྣམས་ཆེས་ཤས་ཆེ་བ་དེ་ཙམ་དེ་ཙམ་དུ་འདོད་ཆགས་ཀྱང་ཆེས་ཤས་ཆེའོ་ཞེས་ཟེར་རོ། །

[Block 3673]
ལྷ་འམ་ལྷ་མོ་གང་གི་པང་དུ་ལྷ་གཞོན་ནུ་འམ་ལྷའི་བུ་མོ་སྐྱེ་བར་འགྱུར་བ་དེ་ནི་དེ༌[^2097]གཉིས་ཀྱི་བུ་ཡང་ཡིན་ལ། དེའི་བུ་མོ་ཡང་ཡིན་ནོ། །

[Block 3674]
བོང་ཚོད་ཇི་ཙམ་དུ་སྐྱེ་ཞེ་ན།

[Block 3675 [VERSE]]
བྱིས་པ་ལོ་ལྔ་ལོན་པ་ནས། །
ལོ་བཅུ་ལོན་པ་ལྟ་བུའི་བར། །

[Block 3676]
དེ་དག་ཏུ་སྐྱེ། ལྷའི་རིས་དེ༌[^2098]དག་ཏུ་གྲངས་བཞིན་ཏེ། དེ་དག་ཀྱང་མྱུར་བ་ཉིད་དུ་སྐྱེའོ། །

[Block 3677]
གཟུགས་ཅན་རྣམས། ཀུན་རྫོགས་གོས་དང་བཅས་པ་ཉིད། །གཟུགས་ན་སྤྱོད་པའི་ལྷ་རྣམས་ནི་ལུས་ཀུན་རྫོགས་པ་དང་གོས་གྱོན་བཞིན་དུ་སྐྱེའོ། །

[Block 3678]
ལྷ་ཐམས་ཅད་ཀྱང་འཕགས་པའི་སྐད་དུ་སྨྲའོ། །

[Block 3679 [HEADING]]
##### འདོད་པ་སྐྱེ་བ་གསུམ། ^3-2-1-16-0

[Block 3680]
དེ་ལ་འདོད་པ་སྐྱེ་བ་གསུམ་པོ་ནི། །
--- END BLOCKS ---
