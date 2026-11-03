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
[Block 2066]
འདིར་ཡིན་ན་འབྱུང་བར་མི་འགྱུར་བས་དེའི་ཕྱིར་འབྱུང་བ་མེད་པ༌[^1074]ཞེས་བྱ་བ༌[^1075]དེ་ལྟར་ཅི་སྟེ་མི་འདོད་ཅེ་ན།

[Block 2067]
བདུན་པ་འདི་ནི་ནུས་པ་མེད་པར་ལྟའོ། །

[Block 2068]
འདིར་ཡིན་ན་འབྱུང་བར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ཇི་སྐད་དུ་བཤད་པ་ཡིན། གལ་ཏེ་ཡོད་ན་ཞེས་བྱ་བར་སྦྱར་ན་ནི༌[^1076]མྱ་ངན་ལས་འདས་པ་ནི་མི༌[^1077]རྟག་པའི་ཕྱིར་རྟག་ཏུ་མི་འབྱུང་བ་ཁོ་ནར་ཐལ་བར་འགྱུར་རོ། །

[Block 2069]
འོན་ཏེ་ཐོབ་ན་ཞེས་བྱ་བར་སྦྱར་ན་ནི་གང་ཁོ་ནས་དེ་འཐོབ་པར་ཡོངས་སུ་རྟོག་པ་དེ་ཉིད་ཡོད་དམ་ཐོབ་ན་སྡུག་བསྔལ་མི་འབྱུང་བར་འདོད་པར་གྱིས་ཤིག །དེ་ལྟར་ན།

[Block 2070 [VERSE]]
མར་མེ་ཤི་བར་གྱུར་པ་ལྟར། །
དེ་ཡི་སེམས་ཀྱི་རྣམ་པར་ཐར། །

[Block 2071]
ཞེས་གསུངས་པའི་དཔེ་འདི་ཡང་ལེགས་པར་དྲངས་པ་ཡིན་ཏེ། ཇི་ལྟར་མར་མེ་ཤི་བ༌[^1078]མེད་པ་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས༌[^1079]སེམས་ཀྱི་རྣམ་པར་ཐར་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 2072]
ཆོས་མངོན་པ་ལས་ཀྱང་དངོས་པོ་མེད་པའི་ཆོས་རྣམས་གང་ཞེ་ན། འདུས་མ་བྱས་ཀྱི་ཆོས་དག་ཡིན་ནོ་ཞེས་གསུངས་ཏེ། དངོས་པོ་མེད་པ་ནི་ལུས་མེད་པ་དང་། རང་གི་ངོ་བོ་མེད་པ་ནི་ཞེས་བཤད་པ་ཡིན་ནོ། །

[Block 2073]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་འདིའི་དོན་ནི་འདི༌[^1080]མ་ཡིན་ནོ། །

[Block 2074]
འོ་ན་ཅི་ཞེ་ན། དངོས་པོ་ནི་རྣམ་པ་ལྔ་སྟེ། རང་བཞིན་གྱི་དངོས་པོ་ནི་ཇི་སྐད་དུ་དེ་དངོས་པོ་གང་ཞིག་ཐོབ་པའི་དངོས་པོ་དེ་དང་ལྡན་ནོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 2075]
དམིགས་པའི་དངོས་པོ་ནི་ཇི་སྐད་དུ་ཆོས་ཐམས་ཅད་དངོས་པོ་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་པས་ཤེས་པར་བྱ་བ་ཡིན་ནོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 2076]
ལྡན་པའི་དངོས་པོ༌[^1081]ཇི་སྐད་དུ་དངོས་པོ་གང་ལ་རྗེས་སུ་ཆགས་པའི་ཀུན་ནས་དཀྲིས་པ་དང༌[^1082]ལྡན་པ་དེ༌[^1083]ཡང་ཁོང་ཁྲོ་བའི་ཀུན་ནས་བཀྲིས་པ༌[^1084]དང་ཡང་ལྡན་ནོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 2077]
རྒྱུའི་དངོས་པོ་ནི་ཇི༌[^1085]སྐད་དུ་དངོས་པོ་དང་བཅས་པའི་ཆོས་རྣམས་གང་ཞེ་ན། འདུས་བྱས་ཀྱི་ཆོས་རྣམས་སོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 2078]
ཡོངས་སུ་གཟུང་བའི༌[^1086]དངོས་པོ་ནི་ཇི་སྐད་དུ་ཞིང་གི་དངོས་པོ་དང་། ཁྱིམ་གྱི་དངོས་པོ་ཞེས་གསུངས་པ་ལྟ་བུ་སྟེ། དེ་ལ་འདིར་ནི་རྒྱུའི་དངོས་པོའི༌[^1087]སྒྲར་གསུངས་པ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་འདུས་མ་བྱས་རྫས་སུ་ཡོད་པ་ཁོ་ན་ཡིན་ལ༌[^1088]དེ་ལ་ཡང་རྒྱུ་དང་འབྲས་བུ་དག་ནི་མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 2079]
རེ་ཞིག་དེ་ནི་རྫོགས་སོ།། །།

[Block 2080 [HEADING]]
##### འབྲས་བུ་གང་ཞིག་རྒྱུ་གང་གི་ཡིན་པ། ^2-4-2-2-0

[Block 2081]
ཡང་འབྲས་བུ་འདི་དག་ལས་འབྲས་བུ་གང་ཞིག་རྒྱུ་གང་གི་ཡིན་ཞེ་ན། རྣམ་སྨིན་འབྲས་བུ་ཐ་མའི་ཡིན། །རྣམ་པར་སྨིན་པའི་རྒྱུ་ནི་ཐ་མར་བསྟན་པའི་ཕྱིར་ཐ་མ་སྟེ། རྣམ་པར་སྨིན་པའི་འབྲས་བུ་ནི་དེ༌[^1089]ཡིན་ནོ། །

[Block 2082]
བདག་པོའི་འབྲས་བུ་དང་པོའི་ཡིན། །བྱེད་རྒྱུའི་རྒྱུ་ནི་དང་པོར་བསྟན་པའི་ཕྱིར་དང་པོ་སྟེ་བདག་པོའི་འབྲས་བུ་ནི་དེའི་ཡིན་ནོ། །

[Block 2083]
བདག་པོའི་འབྲས་བུ་ནི་བདག་པོ༌[^1090]ཡིན་ནོ། །

[Block 2084]
མི་སྒྲིབ་པའི་དངོས་པོ་ཙམ་དུ་གནས་པ་གོ་ཅི་ཞིག་དབང་བྱེད་ཅེ་ན། དེ་ཉིད་དབང་བྱེད་པ་ཡིན་ནོ། །

[Block 2085]
བྱེད་རྒྱུའི་རྒྱུ་ལ་སྐྱེད་པའི་དངོས་པོ་ཡང་ཡོད་དེ། འདི་ལྟ་སྟེ་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་པོ་དག་ལ་སྐྱེ་མཆེད་བཅུ་ལྟ་བུ་དང་། སྣོད་ཀྱི་འཇིག་རྟེན་ལ་ལས་རྣམས་ལྟ་བུའོ། །

[Block 2086]
རྣ་བ་ལ་སོགས་པ་ལ་ཡང་མིག་གི་རྣམ་པར་ཤེས་པ་བསྐྱེད་པ༌[^1091]ལ་བརྒྱུད་པས༌[^1092]དབང་བྱེད་པ་ཡོད་དེ། ཐོས་ནས་ལྟ་བར་འདོད་པ་འབྱུང་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པར་སྦྱར་བར་བྱའོ། །

[Block 2087]
རྒྱུ་མཐུན་སྐལ་མཉམ་ཀུན་འགྲོ་བའི། །འདི་གཉིས་དང་འདྲ་བའི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རྒྱུ་མཐུན་པའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 2088]
སྐྱེས་བུ་པ་ནི་གཉིས་ཀྱི་ཡིན། །སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་ནི་ལྷན་ཅིག་འབྱུང་བ་དང་མཚུངས་པར་ལྡན་པའི་རྒྱུ་དག་གི་ཡིན་ནོ། །

[Block 2089]
སྐྱེས་བུའི་ངོ་བོ་ལས་མི་གཞན་པའི་ཕྱིར་སྐྱེས་བུ་བྱེད་པ་ནི་སྐྱེས་བུ་ཉིད་ཡིན་ནོ། །

[Block 2090]
དེའི་འབྲས་བུ་ནི་སྐྱེས་བུ་ཡིན༌[^1093]པའོ། །

[Block 2091]
སྐྱེས་བུ་བྱེད་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞིག་ཅེ་ན། ཆོས་གང་གི་བྱེད་པ་གང་ཡིན་པ་དེ་སྐྱེས་བུའི་བྱེད་པ་ལྟ་བུ་ནི་སྐྱེས་བུ་བྱེད་པ་སྟེ། དཔེར་ན་སྨན་བྱ་རོག་རྐང༌[^1094]དང་། མི་གླང་པོ་ཆེ་མྱོས་པ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 2092]
ཅི་གཞན་དག་ལ་ཡང་སྐྱེས་བུ་བྱེད༌[^1095]པའི་འབྲས་བུ་ཡོད་དམ། འོན་ཏེ་གཉིས་ཁོ་ནའི་ཡིན་ཞེ་ན། རྣམ་པར་སྨིན་པའི་རྒྱུ་མ་གཏོགས་པ་གཞན་དག་ལ་ཡང་ཡོད་དེ། འདི་ལྟར་སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་ནི་ལྷན་ཅིག་འབྱུང་བ་དང་དེ་མ་ཐག་ཏུ་འབྱུང་བ་ཡིན་ན་རྣམ་པར་སྨིན་པ་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 2093]
གཞན་དག་ན་རེ་དེ་ལ་ཡང་སྐྱེས་བུའི༌[^1096]བྱེད་པའི་འབྲས་བུའི༌[^1097]སྐལ་བ་ནི་ཡོད་དོ། །

[Block 2094]
[^1098]དཔེར་ན་ཞིང་པ་རྣམས་ཀྱི་འབྲས་བུ་ལྟ་བུའོ་ཞེས་ཟེར་རོ། །

[Block 2095 [HEADING]]
##### རྣམ་པར་སྨིན་པའི་འབྲས་བུ་ནས་བདག་པོའི་འབྲས་བུའི་བར་ཅི་ཡིན་པ། ^2-4-2-3-0

[Block 2096 [HEADING]]
###### རྣམ་པར་སྨིན་པའི་འབྲས་བུ། ^2-4-2-3-1-0

[Block 2097]
ཡང་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་ཞེས་བྱ་བ་འདི་ནི༌[^1099]ཅི་ཡིན། བདག་པོའི་འབྲས་བུའི་བར་དུ་ཅི་ཞིག་ཡིན་ཞེ་ན། རྣམ་སྨིན་ལུང་དུ་མ་བསྟན་ཆོས། །རྣམ་པར་སྨིན་པ་ནི་མ་བསྒྲིབས༌[^1100]ལ་ལུང་དུ་མ་བསྟན་པའི་ཆོས་ཡིན་ནོ། །

[Block 2098]
སེམས་ཅན་དུ་སྟོན་པ་མ་ཡིན་པ་ཡང་ཡོད་པས་དེའི་ཕྱིར། སེམས་ཅན་བརྗོད་ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 2099]
རྒྱས་པ་ལས་བྱུང་བ་དང་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་ཡང་ཡོད་པས་དེའི་ཕྱིར། ལུང་བསྟན་ཕྱིས་བྱུང་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་བ་དང་མི་དགེ་བ་ནི་རྣམ་པར་སྨིན་པའི་ཕྱིར་ལུང་དུ་བསྟན་པས་ལུང་དུ་བསྟན༌[^1101]པའོ། །

[Block 2100]
གང་ཞིག་དེ་ལས་དུས་ཕྱི༌[^1102]མ་ལ་འབྱུང༌[^1103]ཞིང་དེ་མ་ཐག་ཏུ་མ་ཡིན་པ་དེ་ནི་རྣམ་པར་སྨིན་པ་སྟེ། འདི་ནི་རྣམ་པར་སྨིན་པའི་མཚན་ཉིད་ཡིན་ནོ། །

[Block 2101]
ཅིའི་ཕྱིར་སེམས་ཅན་དུ་སྟོན་པ་མ་ཡིན་པའི་དོན་ལས་ལས་སྐྱེས་པ་རྣམ་པར་སྨིན་པ་མ་ཡིན་ནམ༌[^1104]ཞེ་ན། ཐུན་མོང་བའི༌[^1105]ཕྱིར་ཏེ། དེ་ནི་གཞན་གྱིས་ཀྱང་དེ་བཞིན་དུ༌[^1106]ཡོངས་སུ་སྤྱད་པར་ནུས་སོ། །

[Block 2102]
རྣམ་པར་སྨིན་པ་ནི་ཐུན་མོང༌[^1107]མ་ཡིན་པའི་སྟེ། གཞན་གྱིས་བྱས་པའི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་གཞན་གྱིས་མྱོང་བར་ནི་མེད་དོ། །

[Block 2103]
བདག་པོའི་འབྲས་བུ་ཅིའི་ཕྱིར་མྱོང་ཞེ་ན། ཐུན་མོང་གི་ལས་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 2104 [HEADING]]
###### རྒྱུ་མཐུན་པའི་འབྲས་བུ། ^2-4-2-3-2-0

[Block 2105]
རྒྱུ་མཐུན་རྒྱུ་དང་འདྲ་བའོ། །
--- END BLOCKS ---
