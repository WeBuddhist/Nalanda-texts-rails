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
ཆོས་ཀྱི་འཁོར་ལོ་གཉིས་པ་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་ཡང་དག་པར་ཞུགས་པ་རྣམས་ལ་ཆོས་ཀྱི་འཁོར་ལོ་དང་པོ་བསྐོར་བ་ལ་ལྟོས༌[^2022]ན་གཉིས་པ་སྟེ། ཐེག་པ་ཆེན་པོ་དྲང་བའི་དོན་གྱི་མདོ་བཤད་པ་ཐམས་ཅད་སྤྱིར་གཟུང་ངོ་། །ཐེག་པ་ཆེན་པོ་ཐམས་ཅད་ལ་ཡང་དག་པར་ཞུགས་པ་རྣམས་ལ་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་རྣམ་པར་དག་པའི་ལམ་གཅིག་པ་དང་། རྣམ་པར་དག་པ་གཅིག་པ་དང་། ཐེག་པ་གཅིག་ཏུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2067]
ལེགས་པར་རྣམ་པར་ཕྱེ་བ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་ངེས་པའི་དོན་བསྟན་པའོ། །

[Block 2068]
གཅིག་ཏུ་ངོ་མཚར་རྨད་དུ་བྱུང་བ་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཐམས་ཅད་ཀྱི་ཚུལ་གྱིས་མཐོང་བ་དང་། སློབ་པ་དང་མི་སློབ་པའི་ལས༌[^2023]སྐྱེ་བས་འཇིག་རྟེན་ཐམས་ཅད་དང་མི་མཐུན་པའི་ཕྱིར་རོ། །

[Block 2069]
ཆོས་ཀྱི་འཁོར་ལོ་གསུམ་པ་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་རྣམས་ལ་དྲང་བའི་དོན་གྱི་ཆོས་ཀྱི་འཁོར་ལོ་གཉིས་པ་བསྐོར་བ་ལ་ལྟོས༌[^2024]ན་གསུམ་པ་སྟེ། སྐབས་འདིར་དོན་དམ་པ་ངེས་པའི་དོན་དམ་པ་བསྟན་པ་འདི་ཉིད་ཡིན་པར་སྦྱར་རོ། །

[Block 2070]
བླ་ན་མ་མཆིས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་བཞི་ནི་ངེས་པའི་དོན་ཡིན་པས་དེ་ལས་གཞན་དུ་དྲང་བ་མེད་པའི་ཕྱིར་ཏེ། དེ་ནི་ངེས་པའི་དོན་གྱི་ཆེ་བ་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 2071 [HEADING]]
###### **བསོད་ནམས་འཕེལ་བའི་ཆེ་བ་ཉིད་བསྟན་པ།** ^4-2-3-2-3-2-0

[Block 2072]
དེའི་འོག་ཏུ་བསོད་ནམས་ཆེ་བའི་འཕེལ་བ་ཉིད་བསྟན་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། བསོད་ནམས་འཕེལ་བའི་ཆེ་བ་ཉིད་བསྟན་པ་ཞེས་བྱ་བ་ནི་དོན་དམ་པ་ངེས་པའི་དོན་བསྟན་པ་འདི་ལ་ཆོས་སྤྱོད་པ་རྣམ་པ་བཅུའི་རིམ་གྱིས་སྦྱོར་བར་བྱེད་པ་ནི་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པ་དང་། བསོད་ནམས་རྒྱ་ཆེན་པོ་བསྐྱེད་པའི་ལམ་དང་། སྦྱོར་བའི་ལམ་དང་། སྒྲིབ་པ་རྣམ་པར་དག་པའི་ལམ་ཡིན་པས། འབྲས་བུ་བླ་ན་མེད་པའི་བྱང་ཆུབ་སྐྱེད་པར་བྱེད་པའི་ཕྱིར་དང་། ངེས་པའི་དོན་བསྟན་པ་འདི་ལ་རིགས་ཀྱི་བུ་འམ། རིགས་ཀྱི་བུ་མོ་གང་དག་ཆོས་སྤྱོད་པ་རྣམ་པ་བཅུའི་རིམ་གྱིས་སྦྱོར་བར་བྱེད་པ་དེ་དག་ལ་སྤྱོད་པ་རེ་རེའི་སྒོ་ནས་ཀྱང་བསོད་ནམས་དཔག་ཏུ་མེད་པ་གྲངས་མེད་པ་སྐྱེ་བའི་ཆེ་བ་ཉིད་བསྟན་པ་གང་ཡིན་པའོ། །

[Block 2073]
དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། བཅོམ་ལྡན་འདས་ཆོས་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མ་མཆིས་པ་ཉིད་ལས་བརྩམས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2074]
ཐོས་ནས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཆོས་སྤྱོད་པ་བཅུ་པོ་དག་བསྟན་ཏེ། ཅི་རིགས་པར༌[^2025]སྦྱར་རོ། །

[Block 2075]
བརྒྱའི་ཆར་ཡང་ཉེ་བར་མི་འགྲོ་ཞིང་། སྟོང་གི་ཆ་དང་། འབུམ་གྱི་ཆ་ཞེས༌[^2026]བྱ་བ་ནི་འཇིག་རྟེན་ན་མང་བར་གྲགས་པའི་སྒོ་ནས་མཚོན་པ་ཡིན་ནོ། །

[Block 2076]
གྲངས་ཞེས་བྱ་བ་ནི་མཚུངས་པར་རྩི་བ་ཉིད་དེ། དཔེར་ན་རི་བོ་གངས་ཅན་དང་ཅིག་ཤོས་འབིགས་བྱེད་ཅེས་བྱ་བ་ནི་མཚུངས་པར་རྩི་བའི་གྲངས་སུ་རིགས་ཀྱི། རི་བོ་གངས་ཅན་དང་ཡུངས་འབྲུ་ནི་མཚུངས་པར་རྩི་བའི་གྲངས་སུ་མི་རིགས་པར་བལྟའོ། །

[Block 2077]
ཆ་ཞེས་བྱ་བ་ནི་ཡན་ལག་སྟེ།[^2027] དེ་ཡང་རང་བཞིན་འདྲ་བ་ཡིན་ཏེ། དཔེར་ན་རྩེ་མོ་ཅན་རྣམས་ཀྱི་རྩེ་མོ་ནི་ཆེ་བ་ཡིན་གྱི། རྩྭའི་རྩེ་མོ་ནི་དེ་དག་གི་ཆ་མ་ཡིན་པ་བཞིན་ནོ། །

[Block 2078]
བགྲང་བ་ཞེས་བྱ་བ་ནི་དེ་ཡང་མཚུངས་པ་ཡིན་ཏེ། དཔེར་ན་རི་རབ་དང་གངས་རི་ཞེས་བགྲང་གི །རི་རབ་དང་ཡུངས་འབྲུ་ཞེས་ནི་མི་བགྲང་བ་བཞིན་ནོ། །

[Block 2079]
དཔེ་ཞེས་བྱ་བ་ནི་འདྲ་བ་ཉིད་དེ། དཔེར་ན་བ་ལང་དང་འདྲ་བ་ལ་བ་ལང་ཞེས་བྱའི། སྦྲང་མ་ལ་མ་ཡིན་པ་བཞིན་ནོ། །

[Block 2080]
རྒྱུར་ཡང་ཞེས་བྱ་བ་ནི་དེའི་རྒྱུའི་དངོས་པོར་ཡང་མི་བཟོད་པ་སྟེ། དེ་ནི་བསོད་ནམས་སྐྱེ་བའི་ཆེ་བ་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 2081 [HEADING]]
###### **ངེས་པའི་ཚིག་གི་ཆེ་བ་ཉིད་བསྟན་པ།** ^4-2-3-2-3-3-0

[Block 2082]
དེའི་འོག་ཏུ་ངེས་པའི་ཚིག་གི༌[^2028]ཆེ་བ་ཉིད་བསྟན་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། ངེས་པའི་ཚིག་གི་ཆེ་བ་ཉིད་བསྟན་པ་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མེད་པའི་མཚན་ཉིད་བསྟན་པའི་ལེའུ་འདིའི་མིང་དོན་དམ་པ་ངེས་པའི་དོན་བསྟན་པ་ཞེས་ངེས་པའི་ཚིག་ཏུ༌[^2029]བསྟན་པ་གང༌[^2030]ཡིན་པའོ། །

[Block 2083]
དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། བཅོམ་ལྡན་འདས་དགོངས་པ་ངེས་པར་འགྲེལ་བའི་ཆོས་ཀྱི་རྣམ་གྲངས་འདིར་བསྟན་པ་འདིའི་མིང་ཅི་ལགས། འདི་ཇི་ལྟར་གཟུང་བར་བགྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2084]
དགོངས་པ་ངེས་པར་འགྲེལ་བའི་ཆོས་ཀྱི་རྣམ་གྲངས་འདིར་ཞེས་བྱ་བ་ནི་ངེས་པའི་དོན་བསྟན་པའི་མདོ་སྡེ་འདིའི་ལུས་རྣམ་པར་གཞག་པ་སྤྱི་ལ་སྙེགས་སོ། །

[Block 2085]
བསྟན་པ་འདིའི་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མེད་པའི་མཚན་ཉིད་བསྟན་པའི་ལེའུ་འདི་ཉི༌[^2031]ཚེ་དང་སྦྱར་རོ། །

[Block 2086]
དོན་དམ་པ་ངེས་པའི་དོན་བསྟན་པ་ཞེས་བྱ་བ་ལ། དོན་དམ་པ་ཞེས་བྱ་བ་ནི་དམ་པའི་དོན་ཅེས་བྱ་བར་སྦྱར་ཏེ། དམ་པ་ནི་ཡང་དག་པའི་ཤེས་པ་འཇིག་རྟེན་པ༌[^2032]དང་། འཇིག་རྟེན་ལས་འདས་པའོ། །

[Block 2087]
དོན་ནི་དེའི་ཡུལ་ཀུན་ནས་ཉོན་མོངས་པའི་མཚན་ཉིད་ཀྱི་ཆོས་དང་། རྣམ་པར་བྱང་བའི་མཚན་ཉིད་ཀྱི་ཆོས་སོ། །

[Block 2088]
འདི་དོན་དམ་པ་ངེས་པའི་དོན་བསྟན་པ་ཞེས་བྱ་བར་ཟུང་ཤིག༌[^2033]ཅེས་བྱ་བ་ནི་མིང་དེ་ལྟར་ཟུང་ཤིག༌[^2034]ཅེས་བྱ་བའི་ཐ་ཚིག་སྟེ། དེ་ནི་ངེས་པའི་ཚིག༌[^2035]གི་ཆེ་བ་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 2089 [HEADING]]
###### **འབྲས་བུ་ཐོབ་པའི་ཆེ་བ་ཉིད་བསྟན་པ།** ^4-2-3-2-3-4-0

[Block 2090]
དེའི་འོག་ཏུ་འབྲས་བུ་འཐོབ་པའི་ཆེ་བ་ཉིད་བསྟན་པ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས༌[^2036]སེམས་ཅན་རྣམས་ལ་ཆོས་བསྟན་པའི་འབྲས་བུའི་ཕན་ཡོན་རྒྱ་ཆེ་བ་རྣམ་པ་ལྔ་བསྟན་པ་གང་ཡིན་པ་སྟེ། ལྔ་གང་ཞེ་ན་དེ་དག་ལས་སེམས་ཅན་ཁ་ཅིག་ནི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པར་འགྱུར་བ་དང་། དེ་དག་ལས༌[^2037]སེམས་ཅན་ཁ་ཅིག་ནི་དམ་པའི་ཆོས་བསྟན་པ་དེ་ཉིད་ཀྱི་ཚེ་ཆོས་རྣམས་ལ་ཆོས་ཀྱི་མིག་རྡུལ་མེད་ཅིང་དྲི་མ་དང་བྲལ་བ་བསྐྱེད་པར་འགྱུར་བ་དང་། དེ་དག་ལས༌[^2038]སེམས་ཅན་ཁ་ཅིག་ནི་དམ་པའི་ཆོས་བསྟན་པའི་མོད་ལ་ཟག་པ་ཟད་པར་འགྱུར་བ་དང་། དེ་དག་ལས་སེམས་ཅན་ཁ་ཅིག་ནི་དམ་པའི་ཆོས་ཐོས་པ་དེ་ཉིད་ཀྱི་མོད་ལ་བྱང་ཆུབ་སེམས་དཔའི་བཟོད་པའི་མཆོག་ཐོབ་པར་འགྱུར་བ་དང་། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་དམ་པའི་ཆོས་བསྟན་པས་ལུང་འབོགས་པ་དང་། ཁ་ཐོན༌[^2039]བྱེད་པ་དང་། ཡང་དག་པར་སྒྲུབ་པ༌[^2040]གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་ཚུལ་གྱིས༌[^2041]དམ་པའི་ཆོས་ཀྱི་ཚུལ་ཡུན་རིང་དུ་གནས་པར་བྱེད་པ་སྟེ། བསྟན་པའི་འབྲས་བུའི་ཕན་ཡོན་རྒྱ་ཆེ་བ་ལྔ་པོ་དེ་དག་བསྟན་པ་ནི་འབྲས་བུ་ཐོབ་པའི་ཕན་ཡོན་གྱི་ཆེ་བ་ཉིད་བསྟན་པ་ཞེས་བྱའོ། །

[Block 2091]
དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། དོན་དམ་པ་ངེས་པའི་དོན་བསྟན་པ་འདི་བཤད་པ་ན་སྲོག་ཆགས་དྲུག་འབུམ་ནི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་སེམས་སྐྱེས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བསྟན་པའི་འབྲས་བུའི་ཕན་ཡོན་རྒྱ་ཆེ་བ་ལྔ་པོ་དེ་དག་ལས་དང་པོ་བཞི་ནི་དཀྱུས་ཀྱི་ཚིག་བཞི་དང་གོ་རིམ༌[^2042]བཞིན་དུ་སྦྱར་རོ། །

[Block 2092]
ལྔ་པ་ནི་མདོ་སྡེ་ཐམས་ཅད་ཀྱི་མཇུག་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེ་སྐད་ཅེས་བཀའ་སྩལ་ནས། ལྷ་ལ་སོགས་པའི༌[^2043]འཇིག་རྟེན་ཡི་རང་སྟེ། མངོན་པར་དགའོ༌[^2044]ཞེས་འབྱུང་བའི་སྐབས་དང་སྦྱར་ཏེ། སྐབས་འདིར་དམིགས་ཀྱིས༌[^2045]མ་སྨོས་ཀྱང་མཇུག་ནས་འབྱུང་བ་ཉིད་སྐབས་འདིར་སྦྱར་བར་བྱའོ། །

[Block 2093]
དེ་ལ་རྣམ་པ་ལྔ་པོ་དེ་དག་གི་རྣམ་པར་གཞག་པ་ཇི་ལྟ་བུ་ཞེ་ན། དེ་ནི་རྣམ་པ་གཉིས་ཏེ། གང་ཟག་གི་དབང་དུ་བྱས་པ་དང་། ཆོས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 2094]
དེ་ལ་གང་ཟག་གི༌[^2046]དབང་དུ་བྱས་པ་ཡང་རིགས་དང་། བསམ་པ་ལ་སོགས་པའི་དབང་གིས་རྣམ་པ་གཉིས་ཏེ། ཉན་ཐོས་ཀྱི་ཐེག་པ་པའི༌[^2047]གང་ཟག་དང་། ཐེག་པ་ཆེན་པོ་པའི་གང་ཟག་གོ། །

[Block 2095]
ཉན་ཐོས་ཀྱི་ཐེག་པ་པའི༌[^2048]གང་ཟག་ཀྱང་རྒྱུད་ཀྱི་དབང་གིས་རྣམ་པ་གཉིས་ཏེ། མཐོང་བའི་ལམ་སྐྱེ་བ་དང་། བསྒོམ་པའི་ལམ་གྱིས་མི་སློབ་པའི་ས་མན་ཆད་འཐོབ་པ་སྟེ། དཀྱུས་ཀྱི་ཚིག་བར་མ་གཉིས་དང་གོ་རིམ༌[^2049]བཞིན་ནོ། །

[Block 2096]
ཐེག་པ་ཆེན་པོ་པའི་གང་ཟག་ཀྱང་སེམས་མ་བསྐྱེད་པ་དང་། བསྐྱེད་པའི་དབང་གིས་རྣམ་པ་གཉིས་ཏེ། སེམས་མ་བསྐྱེད་པ་ནི་ཀུན་རྫོབ་ཀྱི་སེམས་དང་། དོན་དམ་པའི་སེམས་མ་བསྐྱེད་པ་སྐྱེད་པར་བྱེད་དེ། སེམས་བསྐྱེད་པ་ནི་མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པར་འགྱུར་ཏེ། དཀྱུས་ཀྱི་ཚིག་དང་པོ་དང་། ཐ་མ་གཉིས་དང་གོ་རིམ༌[^2050]བཞིན་དུ་སྦྱར་རོ། །

[Block 2097]
ཆོས་ཀྱི་དབང་དུ་བྱས་པ་ནི་བདེ་བར་གཤེགས་པའི་བསྟན་པ་ཡུན་རིང་དུ་གནས་པ་སྟེ། ཚིག་ཐ་མས་བསྟན་ཏོ། །

[Block 2098]
དེ་ལ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་སེམས་སྐྱེས་སོ་ཞེས་བྱ་བ་ནི་ཀུན་རྫོབ་ཀྱི་སེམས་དང་། དོན་དམ་པའི་སེམས་སྐྱེས་པ་ཅི་རིགས་པར༌[^2051]སྦྱར་རོ། །

[Block 2099]
ཆོས་རྣམས་ལ་ཆོས་ཀྱི་མིག་རྡུལ་མེད་ཅིང་དྲི་མ་དང་བྲལ་བ་རྣམ་པར་དག་གོ་ཞེས་བྱ་བ་ལ་ཆོས་རྣམས་ལ་ཞེས་བྱ་བ་ནི་བདེན་པ་བཞིའི་ཆོས་རྣམས་ལའོ། །

[Block 2100]
ཆོས་ཀྱི་མིག་ཅེས་བྱ་བ་ནི་མཐོང་བའི་ལམ་གྱི༌[^2052]ཤེས་པའོ། །

[Block 2101]
རྡུལ་མེད་ཅིང་ཞེས་བྱ་བ་ནི་བར་ཆད་མེད་པའི་ལམ་གྱི༌[^2053]ཤེས་པའོ། །

[Block 2102]
དྲི་མ་དང་བྲལ་བ་རྣམས༌[^2054]བྱ་བ་ནི་རྣམ་པར་གྲོལ་བའི་ལམ་གྱི་ཤེས་པའོ། །

[Block 2103]
རྣམ་པར་དག་གོ་ཞེས་བྱ་བ་ནི་ཐོབ་བོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2104]
ལེན་པ་མེད་པར་ཟག་པ་རྣམས་ལས་སེམས་རྣམ་པར་གྲོལ་ལོ་ཞེས་བྱ་བ་ལ་ལེན་པ་མེད་པར་ཞེས་བྱ་བ་ནི་མི་སྐྱེ་བ་ཤེས་པའོ། །

[Block 2105]
ཟག་པ་རྣམས་ལས་སེམས་རྣམ་པར་གྲོལ་ལོ་ཞེས་བྱ་བ་ནི་ཟད་པ་ཤེས་པའོ། །
--- END BLOCKS ---
