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
བར་སྐབས་སུ་ཡང་འཕགས་པའི་ལམ་མངོན་དུ་བྱེད་ཅིང་ཡོངས་སུ་མྱ་ངན་ལས་མི་འདའ་སྟེ། དེ་སྲིད་དུ་སྲིད་པ་མྱོང་བར་འགྱུར་བའི་ལས་ཀྱི་སྟོབས་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 2802]
སངས་རྒྱས་འབྱུང་བ་མེད་ན་ཁྱིམ་པ་ཁོ་ནར་དགྲ་བཅོམ་པ་ཉིད་འཐོབ་ན༌[^1924]ཁྱིམ་ན་ནི་མི་གནས་སོ། །

[Block 2803]
ཆོས་ཉིད་ཀྱིས་འཐོབ་པའི་དགེ་སློང་གི་མཚན་མ་ཡང་འཐོབ་བོ། །

[Block 2804]
གཞན་དག་ན་རེ། །དགེ་སྦྱོང་གཞན་གྱི་མཚན་མས་སོ་ཞེས་ཟེར་རོ། །ཅིའི་ཕྱིར་ལོག་པར་ལྟུང་བའི་ཆོས་ཅན་མ་ཡིན་ཞེ་ན། །དེར་འགྲོ་བའི་ལས་མི་སོགས་པའི༌[^1925]ཕྱིར་དང་། བསགས་པ་ཡང་སྦྱོར་བ་དང་བསམ་པ་དག་པའི་སྒོ་ནས་དགེ་བའི་རྩ་བ་སྟོབས་དང་ལྡན་པས་བསྒོས་པའི་ཕྱིར་རྒྱུད་རྣམ་པར་སྨིན་པ་དང་། མི་མཐུན་པ་བྱས་པའི་ཕྱིར་རོ། །

[Block 2805]
ངན་སོང་དུ་ངེས་པའི་ལས་ཡོད་ན་ནི་དེས་བཟོད་པ་ཡང་བསྐྱེད་པར་མི་འགྱུར་རོ། །

[Block 2806]
འདིར་སྨྲས་པ། མི་མཁས་པས་ནི་སྡིག་པ་ཆུང་ངུ་བྱས་ཀྱང་འོག་ཏུ་འགྲོ། །མཁས་པས་ཆེན་པོ་བྱས་ཀྱང་གནོད་པ་རབ་ཏུ་སྤོང་བར་འགྱུར། །ལྕགས་ཀྱི་གོང་བུ་ཆུང་ཡང་ཆུ་ཡི་གཏིང་དུ་འབྱིང་འགྱུར་ལ། །དེ་ཉིད་སྣོད་དུ་བྱས་ན་ཆེ་ཡང་སྟེང་དུ༌[^1926]འཕྱོ་བར་འགྱུར། །སྡུག་བསྔལ་གྱི་མཐར་བྱེད་དོ་ཞེས་བྱ་བ་སྡུག་བསྔལ་གྱི་མཐའ་གང་ཡིན་ཞེ་ན། གང་ཕན་ཆད་སྡུག་བསྔལ་མེད་པ་སྟེ། སྡུག་བསྔལ་གྱི་ཉིང་མཚམས་མི་སྦྱོར་བར་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2807]
ཡང་ན་མཐའ་ནི་མྱ་ངན་ལས་འདས་པ་ཡིན་ནོ། །

[Block 2808]
མྱ་ངན་ལས་འདས་པ་ཇི་ལྟར་བྱེད་ཅེ་ན། དེ་འཐོབ་པའི་བགེགས༌[^1927]བསལ་བའི་ཕྱིར་ཏེ་དཔེར་ན་སྨྲ་བ་པོ་འདུན་ཁང༌[^1928]རྡིབ༌[^1929]ལ་ནམ་མཁའ་གྱིས་ཞེས་འཛེར་བ་ལྟ་བུ༌[^1930]ཡིན་ནོ། །

[Block 2809]
མཆོག་ཏུ་ཐོགས་ན་ལན་བདུན་པ་གཞན་ཡང་ཡོད་མོད་ཀྱི་མ་ངེས་པས་མི་བརྗོད་དོ། །

[Block 2810]
རེ་ཞིག་འབྲས་བུ་ལ་གནས་པ་བསྒོས་པས༌[^1931]སྤང་བར་བྱ་བ་མ་ཟད་པ་མཆོག་ཏུ་ཐོགས་ན་ལན་བདུན་པ་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 2811 [HEADING]]
##### རིགས་ནས་རིགས་སུ་སྐྱེ་བ། ^3-2-8-3-0

[Block 2812 [VERSE]]
རྣམ་གསུམ་རྣམ་བཞི་ལས་གྲོལ་བ། །
ཚེ་གཉིས་གསུམ་དུ་རིགས་ནས་རིགས། །

[Block 2813]
རྒྱུན་དུ་ཞུགས་པ་དེ་ཉིད་རྒྱུ་གསུམ་གྱིས་ན་རིགས་ནས་རིགས་སུ་སྐྱེ་བ་ཡིན་ཏེ། ཉོན་མོངས་པ་སྤང་བ༌[^1932]ལས་ནི་ཉོན་མོངས་པའི་རྣམ་པ་གསུམ་མམ་བཞི་སྤང་བའི༌[^1933]ཕྱིར་རོ། །

[Block 2814]
དབང་པོ་ལྔས༌[^1934]ནི་དེའི་གཉེན་པོ་ཟག་པ་མེད་པའི་དབང་པོ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 2815]
སྐྱེ་བ་ལས་ནི་ཚེ་གཉིས་སམ་གསུམ༌[^1935]ལུས་པའི་ཕྱིར་རོ། །

[Block 2816]
ཚིགས་སུ་བཅད་པའི་ནང་དུ་གཉིས་ཤིག་སྨོས་པ་ནི།[^1936] རྒྱུན་དུ་ཞུགས་པ་ཕྱིས་ཉོན་མོངས་པ༌[^1937]སྤོང་བར་བྱེད་ན་དེའི་གཉེན་པོ་ཟག་པ་མེད་པའི་དབང་པོ་ཐོབ་པ་ནི་མ་སྨོས་ཀྱང་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2817]
སྐྱེ་བ་ནི་གལ་ཏེ༌[^1938]གོང་མའི་སྐལ་བ་དང་ལྡན་པའི་ཕྱིར་ཆེས་ཉུང་ངུར་ཡང་འགྱུར་བས་དེའི་ཕྱིར་འདི་སྨོས་སོ། །ཅིའི་ཕྱིར་རྣམ་པ་ལྔ་སྤངས་པའི་ཕྱིར་མ་ཡིན་ཞེ་ན། དེ་སྤངས་ན་དྲུག་པ་ཡང་གདོན་མི་ཟ་བར་སྤོང་བའི་ཕྱིར་ཏེ། དེའི་རྣམ་པ་གཅིག་གིས་ནི་བར་ཆད་གཅིག་པའི་བཞིན་དུ་འབྲས་བུ་ལ་བགེགས༌[^1939]བྱ་བར་མི་ནུས་ཏེ། ཁམས་ལས་མི་འདའ་བའི་ཕྱིར་རོ། །

[Block 2818 [HEADING]]
###### ལྷའི་རིགས་ནས་རིགས་སུ་སྐྱེ་བ། ^3-2-8-3-1-0

[Block 2819]
རིགས་ནས་རིགས་སུ་སྐྱེ་བ་དེ་ནི་རྣམ་པ་གཉིས་ཏེ། ལྷའི་རིགས་ནས་རིགས་སུ་སྐྱེ་བ་ནི་ལྷ་དག་གི་ནང་དུ་རིགས་གཉིས་སམ་གསུམ་དུ་འཁོར་ནས་ལྷའི་རིགས་དེའམ་གཞན་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་གང་ཡིན་པའོ། །

[Block 2820 [HEADING]]
###### མིའི་རིགས་ནས་རིགས་སུ་སྐྱེ་བ། ^3-2-8-3-2-0

[Block 2821]
མིའི་རིགས་ནས་རིགས་སུ་སྐྱེ་བ་ནི་མི་དག་གི་ནང་དུ་རིགས་གཉིས་སམ་གསུམ་དུ་འཁོར་ནས་གླིང་དེའམ་གཞན་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་གང་ཡིན་པའོ། །

[Block 2822 [HEADING]]
##### འབྲས་བུ་གཉིས་པ་ལ་ཞུགས་པ། ^3-2-8-4-0

[Block 2823 [VERSE]]
འབྲས་བུ་ལ་གནས་པ་དེ་ཉིད། །
རྣམ་པ་ལྔ་ཡི་བར་བཅོམ་པ། །
གཉིས་པ་ལ་ནི་ཞུགས་པ་ཡིན། །

[Block 2824]
འབྲས་བུ་ལ་གནས་པ་གང་གིས་རྣམ་པ་གཅིག་ནས་ལྔའི་བར་དུ་སྤངས་པ་ཡིན་ན་དེའི་འབྲས་བུ་གཉིས་པ་ལ་ཞུགས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2825 [HEADING]]
##### ལན་ཅིག་ཕྱིར་འོང་བ། ^3-2-8-5-0

[Block 2826 [VERSE]]
རྣམ་པ་དྲུག་པ་ཟད་གྱུར་པ། །
དེ་ནི་ལན་ཅིག་ཕྱིར་འོང་བ། །

[Block 2827]
དེ་ནི་འབྲས་བུ་གཉིས་པ་ཐོབ་པ་ཡིན་ཏེ། ལྷ་དག་གི་ནང་དུ་སོང་ནས་མིའི་འཇིག་རྟེན་དུ་ལན་ཅིག་ཕྱིར༌[^1940]འོང་བའི་ཕྱིར༌[^1941]འོང་བ་སྟེ། ཕན་ཆད་སྐྱེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2828]
འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་རྣམས་བསྲབས་པའི་ཕྱིར་ཞེས་འབྱུང་བ་ནི་ཆུང་ངུའི་རྣམ་པ་ལུས་པའི་ཕྱིར་རོ། །

[Block 2829 [HEADING]]
##### བར་ཆད་གཅིག་པ། ^3-2-8-6-0

[Block 2830 [VERSE]]
འབྲས་བུ་ལ་གནས་པ་དེ་ཉིད། །
ཉིས་ཆ༌[^1942]བདུན་དང༌[^1943]བརྒྱད་ཟད་པ། །
ཚེ་གཅིག་བར་ཆད༌[^1944]གཅིག་པ་དང་། །
གསུམ་པ་ལ་ནི་ཞུགས་པའང་ཡིན། །

[Block 2831]
ཡང་ལན་ཅིག་ཕྱིར་འོང་བ་དེ་ཉིད་རྒྱུ་གསུམ་གྱིས༌[^1945]བར་ཆད་གཅིག་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ། ཉོན་མོངས་པའི་རྣམ་པ་བདུན་ནམ་བརྒྱད་སྤངས་པའི་ཕྱིར་དང་། དེའི་གཉེན་པོ༌[^1946]ཟག་པ་མེད་པའི་དབང་པོ་ཐོབ་པའི་ཕྱིར་དང་། ཚེ་གཅིག་ལུས་པའི་ཕྱིར་རོ། །

[Block 2832]
ཇི་ལྟར་ན་འདིའི་རྣམ་པ་གཅིག་གིས་འབྲས་བུ་ལ་བགེགས་བྱེད༌[^1947]པར་ནུས་ཤེ་ན། ཁམས་ལས་འདའ་བའི་ཕྱིར་ཏེ། གོང་དུ་ལས་རྣམས་ནི་གནས་སྐབས་གསུམ་དུ་བགེགས་བྱེད་པའི༌[^1948]ཕྱིར་ཉེ་བར་གནས་སོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2833]
ལས་རྣམས་ཇི་ལྟ་བར་ཉོན་མོངས་པ་རྣམས་ཀྱང་དེ་དང་འདྲ་བར་རིག་པར་བྱ་སྟེ།[^1949] རྣམ་པར་སྨིན་པ་དང་རྒྱུ་མཐུན་པའི་འབྲས་བུའི་ས་ལས་འདའ་བའི་ཕྱིར་རོ། །

[Block 2834]
བར་ཆད་ཅེས་བྱ་བ་ནི་བར་ཆད་བྱེད་པའོ། །

[Block 2835]
དེའི་མྱ་ངན་ལས་འདའ་བ༌[^1950]ལ་ཚེ་གཅིག་གིས་ཆོད་པའི༌[^1951]ཕྱིར་རམ། ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ལ་ཉོན་མོངས་པའི༌[^1952]རྣམ་པ་གཅིག་གིས་ཆོད་པའི༌[^1953]ཕྱིར་འདི་ལ་བར་ཆད་གཅིག་ཡོད༌[^1954]པས་ན་བར་ཆད་གཅིག་པ་ཡིན་ནོ། །

[Block 2836]
རྣམ་པ་བདུན་དང་བརྒྱད་སྤངས་པ་དེ་ནི་འབྲས་བུ་གསུམ་པ་ལ་ཞུགས་པ་ཡིན་པར༌[^1955]རིག་པར་བྱའོ། །

[Block 2837]
སྔོན་རྣམ་པ་གསུམ་དང་བཞི་སྤངས་པའམ།

[Block 2838]
བདུན་པ་དང་བརྒྱད་པ་སྤངས་པ་འབྲས་བུ་ཐོབ་པ་ནི་ཇི་སྲིད་དུ་འབྲས་བུ་ཁྱད་པར་ཅན་གྱི་ལམ་མངོན་དུ་མ་བྱས་པ་དེ་སྲིད་དུ་རིགས་ནས་རིགས་སུ་སྐྱེ་བའམ་བར་ཆད་གཅིག་པ་མ་ཡིན་ནོ། །

[Block 2839 [HEADING]]
##### ཕྱིར་མི་འོང་བ། ^3-2-8-7-0

[Block 2840]
དེ་དགུ་ཟད་པས་ཕྱིར་མི་འོང་། །འབྲས་བུ་ལ་གནས་པ་དེ་ཉིད་རྣམ་པ་དགུ་སྤངས་པས་ཕྱིར་མི་འོང་བ་ཡིན་པར་རིག་པར༌[^1956]བྱ་སྟེ། འདོད་པའི་ཁམས་སུ་མི་འོང་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
