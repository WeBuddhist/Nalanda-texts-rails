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
[Block 2801]
ཉོན་མོངས་པ་རྣམས་ནི་སེམས༌[^1764]རང་དབང་དུ་གྱུར་པ་ལས་ཀྱང་འབྱུང་སྟེ། སྔར་བསྟན་པ་ཐམས་ཅད་འདི་ལས་འབྱུང་བར་བསྟན་ཏོ། །

[Block 2802]
ཡང་ན་དོན་གཞན་དུ་ན་ཉོན་མོངས་པ་རྣམས་ནི་རྒྱུ་བཞིས་སྐྱེ་བར་འགྱུར་ཏེ། དབང་པོའི་སྒོ་མ་བསྡམས་པ་དང་། དེ་ནི༌[^1765]ཡུལ་མངོན་དུ་གྱུར་པ་དང་། ཡིད་ལ་བྱེད་པས་དེ་ལ་ལྟ་བ་དང་། རྒས་པས་ནི༌[^1766]མི་ནུས་པ་སྟེ། དེ་ལ་ནུས་པ་མ་ཚང་བས་སོ། །

[Block 2803]
ནང་ཡང་གཟུང༌[^1767]སྟེ། དེའི་རང་བཞིན་ཉིད་དོ། །

[Block 2804]
གཞན་དབང་ཡང་རང་ལ་ནུས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2805]
དེ་ལ་འདོད་ཆགས་ཅན་གྱི་མིག་གིས་ལྟ་ཞེས་བྱ་བའི་སྐབས་ཀྱིས་ནི་དེ་ལས་བཟློག་པ་ལ་ཡང་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2806]
སྐབས་ཞིག་ཏུ་ཞེས་བྱ་བ་ནི་གནས་སྐབས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 2807]
གྲགས་པ་མེད་པ༌[^1768]བྱེད་པ་དང་། རང་གི་དགེ་བ༌[^1769]ལོག་པར་སྤྱོད་པའི་སྐྱོན་གྱིས་འབྱོར་པ་མེད་པར་བྱེད་པ་སྟེ། ཁྱིམ་ཐབ༌[^1770]ཀྱི་དགེ་མཚན་ངན་པས་ཕུན་སུམ་ཚོགས་པའི་བགེགས་སུ་གྱུར་པས་སོ། །

[Block 2808]
སྨད་པ་ནི་མཚན་དང་བྲལ་བའོ། །

[Block 2809]
མཛེས་པ༌[^1771]མེད་པར་བྱེད་པ་ནི་ཟླ་བ་སྤྲིན་རུམ་དུ་ནུབ་པས་གནམ་སའི་བྱེ་བྲག་མི༌[^1772]མཛེས་པར་བྱེད་པ་ཡིན་ཏེ། གནམ་དང་ས་གཉིས་ཀྱི་བྱེ་བྲག་མེད་པར་བྱེད་པའོ། །

[Block 2810]
ངའི་རིགས་དང་མཐུན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེའི༌[^1773]མཚན་ངན་པའི་ཕྱིར་རོ། །

[Block 2811]
རེ་ཞིག་རིགས་དང་མཐུན་པར་འགྱུར་རོ་ཞེས་བསམས་ཏེ་དེ་ཉིད་ཀྱི་ཁྱད་པར་བསྟན་པའི་ཕྱིར་རིམ་གྱིས་ཞེས་བྱ་བ་ནི་དུས་ཕྱི༌[^1774]ཞིག་ན་ཞེས་བྱ་བའི༌[^1775]དོན་ཏེ། བློན་པོ་དེ་ལ་ཕྱིན་མ་ཐག་པ་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་འདི་ལྟར་སྟོན་པ་སྟེ། དེའི་ཚེ་ནི་རྒྱལ་པོས་མཐོང་བའི་ལམ་གྱི་གནས་སྐབས་ཀྱང་མེད་དེ། བག་མ་སར་པར༌[^1776]གྱུར་པའི་ཕྱིར་རོ། །

[Block 2812]
བདག་རང་གི་གྲོང་ཁྱེར་མཆོག་ཅེས་བྱ་བ་ནི་རྒྱལ་པོ་དེའི་ཀུ་མུ་ཏའི་དགའ་སྟོན་ལྟ་བ༌[^1777]ནི་སྐྱོན་མེད་པ་ཡིན་ཏེ། དེ་ལྟ་བའི༌[^1778]ཕྱིར་རོ། །

[Block 2813]
ཀུ་མུ་ཏའི་དགའ་སྟོན་མ་ཡིན་པ་གཞན་དུ་ན་བརྐམ་ཆགས་ཅན་དུ་འགྱུར་ཏེ། དེ་ཡོངས༌[^1779]སུ་བཅད་པའི༌[^1780]ཕྱིར་མཆོག་ཅེས་སྨོས་སོ། །

[Block 2814]
བལྟར་རུང་བའི་ཕྱིར་ནི་ཀུ་མུ་ཏའི་དགའ་སྟོན་བསྟན་ཏོ། །

[Block 2815]
ཕྱག་དར་བྱས་ཤིང་ཆག་ཆག་བཏབ་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྐྱང་པས་ནི་མིག་དང་། རྣ་བ་དང་། སྣའི་དབང་པོའི་ཡུལ་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏེ། [^1781]གྲོང་ཁྱེར་གྱི་མཆོག་དེའི་མེ་ཏོག་ཀུ་མུ་ཏ་དགའ་སྟོན་བྱེད་པ་ལས་ཏེ། ཇི་ལྟར་རིགས་པ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 2816]
མཚན་ངན་པ་མཐོང་བ་ནི་མཚན་ངན་པ་མཐོང་བའོ། །

[Block 2817]
དེས་ན་དྲན་པ་རྣམ་པར་གཡོ་བ་གང༌[^1782]ཡིན་པ་དེ་ནི་མཚན་ངན་པ་མཐོང་ན༌[^1783]འདིས་དྲན་པ་རྣམ་པར་གཡོ་བའོ། །

[Block 2818]
ཕོ་བྲང་སླས་གྱི༌[^1784]ནང་ན་ན་ཆུང་བཟང་མོ་ཞེས་བྱ་བ་དང་། བརྟན་པའི་ཡོན་ཏན་ཆེ་ལ་ངོ་ཚ་ཤེས། །ཞེས་བྱ་བའི༌[^1785]ཚིགས་བཅད་འདི་གཉིས་ཀྱི་བསྡུས་པའི་དོན་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེ་བདག་གི་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པ་ཡིན་ཡང་ཕུན་སུམ་ཚོགས་པ་དེ་དག་འཇིག་པའི་རྒྱུ་ཉིད་དུ་དེའི༌[^1786]གཟུགས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 2819]
ཚིམ་པར༌[^1787]ཞེས་བྱ་བ་ནི་ཇི་ལྟར་འདོད་པའོ། །

[Block 2820]
ཕོ་བྲང་སླས༌[^1788]ཀྱི་ནང་ན་ན་ཆུང་བཟང་མོའི་ཞེས་བྱ་བ་འདིས་ནི་འཇིག་རྟེན་པ་རྣམས་ལས་བུད་མེད་དེ་ཁྱད་པར་དུ་བསྟན་ཏོ། །

[Block 2821]
ལུས་བཟང་བ་དང་ཆས་པ༌[^1789]ནི་ལུས་བཟང་ཆས་སོ། །

[Block 2822]
ལུས་བཟང་ཞེས་སྨོས་པས་ནི་མདོག་དང་དབྱིབས་ཕུན་སུམ་ཚོགས་པ་གཟུང་ངོ་། །ཆས་པ་ཞེས་སྨོས་པས་ནི༌[^1790]སྤྱོད་པ་དང་ཉེ་བར་སྤྱོད་པ་གཟུང་ངོ་། །ཆགས་པ་ནི་རྣམ་པ་བཞི་སྟེ་ཁ་དོག་གི་ཆགས་པ་དང་དབྱིབས་ཀྱི་ཆགས་པ་དང་ཉེ་བར་སྤྱོད་པའི་ཆགས་པ་དང་། རག་པའི་ཆགས་པ་སྟེ། འདིར་རེག་པའི་འདོད་ཆགས་མ་སྨོས་པ་ནི་དེར་ཡུལ་དུ་མ་གྱུར་པས་སོ། །

[Block 2823]
ཁ་དོག་དང་དབྱིབས་དང་། སྤྱོད་ཡུལ་དུ་གྱུར་པའི་ཕྱིར་མཐོང་གྱུར་ཅིང་ཞེས་བྱ་བ་ཡིན་ཏེ། མཐོང་བར་གྱུར་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་པོ་དེས་ནི་བུད་མེད་ཀྱི་ལོངས་སྤྱོད་འཇིག་རྟེན་པ་ལས་ཁྱད་པར༌[^1791]དུ་གྱུར་པ་དང་ལྡན་པ་ཡིན་ཡང་བརྟན་པ་ཉམས་པར༌[^1792]ནུས་པ་སྟེ། དེ་དང་རྗེས་སུ་མཐུན་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 2824]
མ་འཕྱར་བ་ནི་མི་གཡོ་བ་སྟེ། མ་འཕྱར་བའི་སེམས་ཀྱི༌[^1793]ཡུལ་དུ་གྱུར་པའི་ཕྱིར་མ་འཕྱར་བ་སྟེ། འཕྱར་བ་མེད་པ་ནི་མ་འཕྱར་བའོ། །

[Block 2825]
ཆོས་ཀྱི་ལམ་ནི་ཆོས་ལམ་མོ། །

[Block 2826]
འདིར་ཆོས་ནི་མངོན་པར་མཐོ་བ་སྟེ་དེའི་ལམ་མོ། །

[Block 2827]
དབང་པོ་ཐུལ་བ་ནི་འཇིག་རྟེན་པ་སྟེ། འདི༌[^1794]ནི་ཆོས་གཙོ་བོར་བསྟན་ཏོ། །

[Block 2828]
བརྩོན་གྱུར་ཅིང་ཞེས་བྱ་བ་ནི་འབད་བ་དང་ལྡན་པ་སྟེ། བག་ཡོད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2829]
དབང་པོ་ཐུལ་བར་གྱུར་པ་ཞེས་བྱ་བ་འདིས་ནི་ལུགས་ཀྱི་བསྟན་བཅོས་ཀྱི་རྗེས་སུ་འཇུག་པའི་ཚུལ་གཙོར༌[^1795]བསྟན་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་བསྟན་བཅོས་ཐམས་ཅད་ཀྱི་ནང་ན་དབང་པོ་ཐུལ་བར་བྱེད་པ་ཞེས་བྱ་བའི་ཚིག་འདིས་སོ། །

[Block 2830]
བསྟན་པའི་ཡོན་ཏན་ཆེ་ལ་ངོ་ཚ་ཤེས། །ཞེས་བྱ་བ་འདིས་ནི་བདག་གི་དབང་དུ་བྱས་ཏེ། ངོ་ཚ་ཤེས་པ་དང་ལྡན་པ་དང་། གཞན་གྱི་དབང་དུ་བྱས་ནས་ཁྲེལ་ཡོད་པ་སྟེ། དེ་གཉིས་ཀྱིས་ནི་འཇིག་རྟེན་སྐྱོང་བའི་ཆོས་དང་ལྡན་པ་ཡིན་ཏེ། སྔར་བསྟན་པའི་འཁོར་གསུམ་ལས་མི་འདའ་བ་དང་།

[Block 2831 [VERSE]]
ཐེམ་སྐས་སུ་གྱུར་པ་ནི་ཆོས་འདི་གཉིས་སོ། །
གཞན་གྱི་བུད་མེད་ལྟ་བ་མ༌[^1796]སྨོས་ཀྱང་། །

[Block 2832]
ཞེས་བྱ་བ་ནི་སྐྱེ་བ་སྔ་མ་ལ་ཚུལ་ཁྲིམས་ལ་གོམས་པར་བསྟན་ཏེ། འདིས་ནི་རྒྱུ་ཕུན་སུམ་ཚོགས་བར་བསྟན་ཏོ། །

[Block 2833]
འདོད་ཆགས་ལངས་ཤིང་ཡ་མཚན་ཆེ་བར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་འདོད་ཆགས་ལངས་ཤིང་ཡ་མཚན་ཆེ་བ་སྟེ། འདིས་ནི་ངོ་ཚ་ཉམས་པར་བསྟན་ཏོ། །

[Block 2834]
བུད་མེད་དེ་ལ་ཞེས་བྱ་བ་ནི་ཕོ་བྲང་སླས༌[^1797]ཀྱི་ན་ཆུང་ཞེས་བྱ་བ་དག་ཀྱང་ཡོད་ཅིང་གཞན་གྱི་བུད་མེད་ལྟ་ལ་མ་སྨོས༌[^1798]ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ཡང་མིག་གིས་རིང་དུ་བལྟས་པ་སྟེ། འདིས་ནི་ཁྲེལ་ཡོད་པ་ཉམས་པར་བསྟན་ཏོ། །

[Block 2835]
འདི་ཅི་ཀུ་མུ་ཏ་ཡིན་ནམ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་བསྟན་པ་ནི་འདོད་ཆགས་ཀྱི་གནས་སྐབས་བཅུ་ལས་འདོད་ཆགས་ཀྱི་གནས་སྐབས་དང་པོ་བསྟན་པ་ཡིན་ཏེ། མི་ལུས་ལས་འདས་པའི་གཟུགས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2836]
དེ་ལ་གནས་པའི་རྣམ་པ་དེ་ནི་དེ་ལྟར་གྱུར་པའོ། །

[Block 2837]
སེམས་རྩེ་གཅིག་ཏུ་དམིགས་པ་ནི་རྩེ་གཅིག་པའོ། །

[Block 2838]
དེ་ལ་རྩེ་གཅིག་ཏུ་གྱུར་པའི་སེམས་གང་ཡིན་པ་དེ་ནི་དེ་ལ་སེམས་རྩེ་གཅིག་པའོ། །

[Block 2839]
རེ་ཐག་ཆད་པའི་ཡིད་གང་ཡིན་པ་དེ་ནི་རེ་ཐག་བཅད་པའི་སེམས་སོ། །

[Block 2840]
དེ་ལ་སེམས་ཆགས་པ༌[^1799]བཞིན་དུ་ཞེས་བྱ་བ་ནི་རྣམ་པར་ཆགས་པ་ལྡོག་པར་མ་གྱུར་ཏེ། འདོད་བཞིན་དུ་གཞན་གྱི་ཆུང་མ་ཡིན་ནོ་ཞེས་པས་སོ། །
--- END BLOCKS ---
