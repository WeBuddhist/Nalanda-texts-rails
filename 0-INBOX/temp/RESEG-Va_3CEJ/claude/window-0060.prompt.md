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

[Block 2106]
རྒྱུ་དང་འདྲ་བའི་ཆོས་གང་ཡིན་པ་དེ་ནི་རྒྱུ་མཐུན་པའི་འབྲས་བུ་སྟེ། འདི་ལྟ་སྟེ་སྐལ་བ་མཉམ་པ་དང་ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ་དག་གི་ལྟ་བུའོ། །

[Block 2107]
གལ་ཏེ་ཀུན་ཏུ་འགྲོ་བའི་རྒྱུའི་འབྲས༌[^1108]བུ་ཡང་འདྲ་བ་ཡིན་ན་གོ་ཅིའི་ཕྱིར་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཁོ་ནར་མི་འདོད་ཅེ་ན། འདི་ལྟར་དེ་ནི་ས་དང༌[^1109]ཉོན་མོངས་པ་ཅན་ལས་འདྲ་བ་ཡིན་གྱི། རྣམ་པ་ལས་ཀྱང་འདྲ་བ་ནི་མ་ཡིན་ནོ། །

[Block 2108]
གང་ཞིག་རྣམ་པ་ལས་ཀྱང་འདྲ་བ་དེ་ནི༌[^1110]སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་པར་ཁས་ལེན་པ་ཉིད་དོ། །

[Block 2109]
དེ་ཉིད་ཀྱི་ཕྱིར་གང་ཞིག་གང་གི༌[^1111]སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་པ་དེ༌[^1112]ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ་ཡང་ཡིན་ནམ་ཞེ་ན། མུ་བཞིར་བྱ་སྟེ། མུ་དང་པོ་ནི་སྐལ་བ་མཉམ་པའི་རྒྱུ་ནི་ཀུན་ཏུ་འགྲོ་བ་མ་ཡིན་པའོ། །

[Block 2110]
གཉིས་པ་ནི་རིས་གཞན་པའི་ཀུན་ཏུ་འགྲོ་བའི་རྒྱུའོ། །

[Block 2111]
གསུམ་པ་ནི་རིས་གཅིག་པའི་ཀུན་ཏུ་འགྲོ་བའི་རྒྱུའོ། །

[Block 2112]
བཞི་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 2113 [HEADING]]
###### བྲལ་བའི་འབྲས་བུ། ^2-4-2-3-3-0

[Block 2114]
བྲལ་བ་བློ་ཡིས་ཟད་པའོ། །

[Block 2115]
ཟད་པ་ནི་འགོག་པའོ། །

[Block 2116]
བློ་ནི་ཤེས་རབ་སྟེ། དེས་ན་སོ་སོར་བརྟགས་པས༌[^1113]འགོག་པ་ནི་བྲལ་བའི་འབྲས་བུ་ཡིན་ནོ་ཞེས་བཤད་པར་འགྱུར་རོ། །

[Block 2117 [HEADING]]
###### སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ། ^2-4-2-3-4-0

[Block 2118 [VERSE]]
གང་གི་སྟོབས་ཀྱིས་གང་སྐྱེ་བའི། །
འབྲས༌[^1114]དེ་སྐྱེས་བུ་བྱེད་ལས་སྐྱེས། །

[Block 2119]
དཔེར་ན་ས་འོག་མ་པའི་སྦྱོར་བའི༌[^1115]སེམས་ཀྱིས་གོང་མ་པའི༌[^1116]ཏིང་ངེ་འཛིན་དང་། ཟག་པ་དང་བཅས་པའི་ཟག་པ་མེད་པ་དང་། བསམ་གཏན་གྱི་སེམས་ཀྱི་སྤྲུལ༌[^1117]པའི་སེམས་སོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 2120]
སོ་སོར་བརྟགས་པས་འགོག་པ་ནི་གང་གི་སྟོབས་ཀྱིས་འཐོབ་པ༌[^1118]ཞེས་བརྗོད་པར་བྱའོ། །

[Block 2121 [HEADING]]
###### བདག་པོའི་འབྲས་བུ། ^2-4-2-3-5-0

[Block 2122 [VERSE]]
སྔོན་བྱུང་མ་ཡིན་འདུས་བྱས་ནི། །
འདུས་བྱས་ཁོ་ནའི་བདག་པོའི་འབྲས། །

[Block 2123]
སྔར་བྱུང་བ་ལས་གཞན་པའི་འདུས་བྱས་ཀྱི་ཆོས་ནི་འདུས་བྱས་ཐམས་ཅད་ཀྱི་བདག་པོའི་འབྲས་བུ་ཡིན་ནོ།[^1119] །སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི་འབྲས་བུ་དག་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཞིག་ཡོད་ཅེ་ན། སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་ནི་བྱེད་པ༌[^1120]པོའི་ཡིན་ནོ། །

[Block 2124]
བདག་པོའི་འབྲས་བུ་ནི་བྱེད་པ་པོ་མ་ཡིན་པའི་ཡང་ཡིན་ཏེ། འདི་ལྟ་སྟེ། བཟོ་བོ་རྣམས་ཀྱི་བཟོ་ནི་སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་ཡང་ཡིན་ལ་བདག་པོའི་འབྲས་བུ་ཡང་ཡིན་ནོ། །

[Block 2125]
གཞན་དག་གི་ནི་བདག་པོའི་འབྲས་བུ་ཁོ་ན་ཡིན་ནོ། །

[Block 2126 [HEADING]]
##### རྒྱུ་གང་ཞིག་དུས་གང་དུ་འབྲས་བུ་འཛིན་པ་དང་འབྱིན་པ། ^2-4-2-4-0

[Block 2127]
ཡང་རྒྱུ་འདི་དག་ལས་རྒྱུ་གང་ཞིག་དུས་གང་དུ་འབྲས་བུ་འཛིན་ཏམ་འབྱིན་ཅེ་ན། ལྔ་པོ་ད་ལྟར་འབྲས་བུ་འཛིན། །ཡོངས་སུ་བཟུང་ཟིན་པའི་ཕྱིར་འདས་པ་རྣམས་ཀྱང་མ་ཡིན་ལ་སྐྱེས་བུ་བྱེད་པ་མ་ཡིན་པའི་ཕྱིར་མ་འོངས་པ་རྣམས་ཀྱང་མ་ཡིན་ནོ། །

[Block 2128]
བྱེད་རྒྱུའི་རྒྱུ་ཡང་དེ་དང་འདྲ་མོད་ཀྱི་དེ་ནི་འབྲས་བུ་དང་བཅས་པར་མ་ངེས་པས༌[^1121]མ་བརྗོད་དོ། །

[Block 2129]
གཉིས་ནི་རབ་ཏུ་འབྱིན་པར་བྱེད། །ལྷན་ཅིག་འབྱུང་བ་དང་མཚུངས་པར་ལྡན་པའི་རྒྱུ་དག་ནི་ད་ལྟར་འབྲས་བུ་འབྱིན་པར་བྱེད་དེ། འདི་གཉིས་ཀྱི་འབྲས་བུ་འཛིན་པ་དང་འབྱིན་པ་ནི་དུས་མཉམ་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2130]
ད་ལྟར་གྱི་དང་འདས་པ་དག །འབྲས་བུ་འབྱིན་པར་བྱེད་དེ། སྐལ་བ་མཉམ་པ་དང་ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ་དག་གོ། །

[Block 2131]
རེ་ཞིག་གང་འདས་པ་དག་ནི་རིགས་ནི་ད་ལྟར་གྱི་དག་གོ། །

[Block 2132]
རྒྱུ་མཐུན་པའི་འབྲས་བུ་ཇི་ལྟར་འབྱིན་ཅེ་ན། མཇུག་ཐོགས་སུ་བསྒྲུབ་པའི༌[^1122]ཕྱིར་ཏེ། འབྲས་བུ་གྲུབ་ན་ནི་དེ་དག་ཀྱང་འདས་པ་ཡིན་ལ་འབྲས་བུ་ཡང་བྱུང༌[^1123]ཟིན་པས་ཡང་དེ་ཉིད་མི་འབྱིན་ཏོ། །

[Block 2133]
དགེ་བའི་སྐལ་བ་མཉམ་པའི་རྒྱུ་འབྲས་བུ་འཛིན་ལ་མི་འབྱིན་པ་ཡོད་དམ་ཞེ་ན། མུ་བཞི་སྟེ། མུ་དང་པོ་ནི་དགེ་བའི་རྩ་བ་དག་ཀུན་ཏུ་གཅོད་པས་ཐམས་ཅད་ཀྱི་ཐ་མར་འདོར་བའི་ཐོབ་པ་གང་དག་ཡིན་པའོ། །

[Block 2134]
གཉིས་པ་ནི་དགེ་བའི་རྩ་བ་དག་གི་ཉིང་མཚམས་སྦྱོར་བས་ཐམས་ཅད་ཀྱི་དང་པོར༌[^1124]འཐོབ་པ་གང་དག་ཡིན་པའོ། །

[Block 2135]
འདི་སྐད་དུ་དེ་དག་ཉིད་ཀྱིས་ཉིང་མཚམས་སྦྱོར་བར་བྱེད་པའི་ཞེས་བརྗོད་པར་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 2136]
གསུམ་པ་ནི་དགེ་བའི་རྩ་བ་ཀུན་ཏུ་མ་ཆད་པའི་གནས་སྐབས་ལྷག་མ་རྣམས་སུའོ། །

[Block 2137]
བཞི་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 2138]
མི་དགེ་བའི་མུ་དང་པོ་ནི་འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བ་ཐོབ་པ་དང་ལྡན་པས་ཐམས་ཅད་ཀྱི་ཐ་མར་འདོར་བའི་ཐོབ་པ་གང་དག་ཡིན་པའོ། །

[Block 2139]
གཉིས་པ་ནི་འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བ་ལས་ཡོངས་སུ་ཉམས་པས་ཐམས་ཅད་ཀྱི་དང་པོར་འཐོབ་པ་གང་དག་ཡིན་པའོ། །

[Block 2140]
འདི་སྐད་དུ་དེ་དག་ཉིད་ཀྱིས་ཡོངས་སུ་ཉམས་པའི་ཞེས་བརྗོད་པར་བྱ་བ་ནི་ཡིན་ནོ། །
--- END BLOCKS ---
