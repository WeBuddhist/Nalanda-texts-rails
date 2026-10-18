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
[Block 2311]
ལོངས་སྤྱོད་སྣ་ཚོགས་ནི་བཟའ་བ་དུ་མ་དང་། བཏུང་བ༌[^2014]དུ་མའི་དངོས་པོ་བྱེད་པས་སོ། །

[Block 2312]
ཡོངས་སུ་སྤྱོད་པར་གྱུར་པ་ནི་གནས་ལ་སོགས་པར་གྱུར་པས་སོ། །

[Block 2313]
ལོངས་སྤྱོད་དུ་གྱུར་པ༌[^2015]ནི་བཟའ་བ་ལ་སོགས་པར་འགྱུར་བར་རོ། །

[Block 2314]
དེས་དོན་གྱི་དབང་ནི༌[^2016]མཐོང་ནས་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་སེམས་དཔའ་དེས་ལུས་དེ་ལ་གོང་དུ་བཤད་པ་ལྟ་བུའི་དོན་གྱི་དབང་མཐོང་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2315]
ལུས་ལ་སྡུག་བསྔལ་བར་ཡང་རྟོག་ཅིང་ཞེས་བྱ་བ་ནི་ལུས་སྐྱེ་བ་དང་། རྒ་བ་དང་། ན་བ་དང་། འཆི་བ་ལ་སོགས་པའི་སྡུག་བསྔལ་རྣམ་པ་དུ་མ་དང་ལྡན་པར་རྟོག་པའོ། །

[Block 2316]
སེམས་ཅན་ལ་ལྟ་བའི་ཕྱིར་ལུས་ཀྱི་སྡུག་བསྔལ་གྱིས་ཀྱང་མི་སྐྱོ་ཞེས་བྱ་བ་ནི་དེ་ལྟ་མོད་ཀྱི། སེམས་ཅན་ལ་སྙིང་རྗེ་བའི་ཕྱིར་སྡུག་བསྔལ་དང་ལྡན་པའི་ལུས་ཀྱིས་ཀྱང་སྐྱོ་བ་མེད་དེ། ལུས་འདོར༌[^2017]བར་མི་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2317]
ཡང་ན་སྡུག་བསྔལ་བར་རྟོག་པ་ནི་སྡུག་བསྔལ་གསུམ་དང་བརྒྱད་ལ་སོགས་པ་གྲངས་མེད་པ་དང་ལྡན་པར་རྟོག་པའོ། །

[Block 2318]
ལུས་ལ་མི་རྟག་པར་རྟོག་པ་ནི་ལུས་འདི་སྐྱེ་བ་དང་། རྒ་བ་དང་། འཆི་བ་དང་ལྡན་པར་རྟོག་པའོ། །

[Block 2319]
ཤི་འཕོས་པས་ཀྱང་ཡོངས་སུ་མི་སྐྱོ་ཞེས་བྱ་བ་ནི་དེ་ལྟ༌[^2018]མོད་ཀྱི། སེམས་ཅན་གྱི་དོན་དུ་འཁོར་བར་སྐྱེ་ཞིང་འཆི་འཕོ་བསྟན་པས་ཀྱང་མི་སྐྱོ་སྟེ། སྐྱེ་བ་དང་འཆི་འཕོ༌[^2019]ཡང་མི་གཏོང་བའོ། །

[Block 2320]
ལུས་ལ་བདག་མེད་པར་རྟོག་ཅིང་ཞེས་བྱ་བ་ནི་ལུས་འདི་ལ་མུ་སྟེགས་ཀྱིས༌[^2020]བརྟགས་པའི་བདག་དང་། སེམས་ཅན་མེད་པ་ཡང་ཁོང་དུ་ཆུད་ཅིང་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2321]
སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་སྨིན་པར་བྱ་བའི་ཕྱིར་ཡང་མི་སྐྱོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་བདག་དང་སེམས་ཅན་མེད་པར་ཡང་རྟོག་མོད་ཀྱི། སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱ་བའི་ཕྱིར་ཡང་མི་སྐྱོ་སྟེ། སེམས་ཅན་གྱི་དོན་ཀྱང་མི་གཏོང་ངོ་། །ལུས་ལ་ཞི་བར༌[^2021]རྟོག་ཅིང་ཞེས་བྱ་བ་ནི་ལུས་འདི་ཆོས་ཀྱི་དངོས་པོས་ཀྱང་སྟོང་པར་ཁོང་དུ་ཆུད་ཅིང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2322]
ལུས་ཞི་བའི་ཕྱིར་བཏང་སྙོམས་སུ་ཡང་མི་ལྟུང་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་སྟོང་པ་ཉིད་དུ་ཡང་མི་ལྟུང་བ་འམ། ལུས་དང་སེམས་སྦྱང་བར༌[^2022]བྱ་བའི་ཕྱིར་དང་། དགེ་བའི་རྩ་བ་བསགས་པའི་ཕྱིར་བཏང༌[^2023]སྙོམས་སུ་ཡང་མི་འཇོག་པའོ། །

[Block 2323]
དབེན་པར་ཡང་རྟོག་ཅེས་བྱ་བ་ནི་མྱ་ངན་ལས་འདས་པའི་རང་བཞིན་ཡིན་པར་ཁོང་དུ་ཆུད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2324]
མི་ལྟུང་ཞེས་བྱ་བ་ནི་དེ་དག་ལ་མི་གནས་ཤིང་དེ་དག་མངོན་སུམ་དུ་མི་བྱེད་པ་སྟེ། སླ་བ་དང་གོང་དུ་བཤད་པ་རྣམས་ནི་མ་བཤད་དོ། །

[Block 2325]
ཚོར་བ་མེད་པ་ནི་དགེ་བ་དང་མི་དགེ་བའི་འབྲས་བུ་བདེ་བ་དང་། སྡུག་བསྔལ་བ་ལ་སོགས་པ་མྱོང་བར་བྱེད་པའི་ཚོར་བ་པོ་མེད་པའོ། །

[Block 2326]
བྱེད་པ་མེད་པ་ནི་དབང་ཕྱུག་ལ་སོགས་པ་ལུས་སྐྱེད་པར་བྱེད་པའི་བྱེད་པ་པོ༌[^2024]མེད་པའོ། །

[Block 2327]
བདག་པོ་མེད་པ་ནི་ནང་ན་གནས་པའི་སྐྱེས་བུ་མེད་པའོ། །

[Block 2328]
ལུས་འཛིན་པ་མེད་པ་ནི་དེ་ལས་གཞན་པའི་བདག་ལུས་ལ་བྱིན་གྱིས་བརླབ་པ༌[^2025]མེད་པ་སྟེ། ཚིག་དེ་དག་གིས་གང་ཟག་གི་དངོས་པོ་མེད་པར་བསྟན་ཏོ། །

[Block 2329]
ལུས་དབྱེར་མེད་པ་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་ཆོས་ཉིད་ལ་ཐ་དད་པ་མེད་པས་སོ། །

[Block 2330]
ལུས་རོ་གཅིག་པ་ནི་ལུས་ཀྱི་ཆོས་ཉིད་ཐམས་ཅད་སྟོང་པ་ཉིད་དུ་རོ་གཅིག་པས་སོ། །

[Block 2331]
ལུས་ནམ་མཁའི་ངོ་བོ་ཉིད་ཅེས་བྱ་བ་ནི་ཇི་ལྟར་ནམ་མཁའ་དངོས་པོ་མེད་ཅིང་ཐམས་ཅད་དུ་སོང་བ་དེ་བཞིན་དུ་ལུས་ཀྱང་དངོས་པོ་མེད་ཅིང་ཐམས་ཅད་དུ་སོང་བའི་ཕྱིར་རོ། །

[Block 2332]
ལུས་རང་བཞིན་གྱིས་ཡོངས་སུ་མྱ་ངན་ལས་འདས་ཞེས་བྱ་བ་ནི་རང་བཞིན་གྱིས་ཉོན་མོངས་པ་དང་། ཤེས་བྱའི་སྒྲིབ་པའི༌[^2026]དྲི་མ་དང་མ་འདྲེས་པ་སྟེ། ཚིག་དེ་དག་གིས་ནི་ཆོས་ཀྱི་དངོས་པོ་མེད་པར་བསྟན་ཏོ། །

[Block 2333]
མི་ལྟུང་བ་ནི་སྟོང་པའི་ཆོས་དེ་མངོན་སུམ་དུ་མི་བྱེད་པའོ། །

[Block 2334]
དེ་ཞེས་བྱ་བ་ནི་ལུས་དྲན་པ་ཉེ་བར་གཞག་པ༌[^2027]ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེའོ། །

[Block 2335]
ལུས་རྫས་དང་སྙིང་པོ་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་ཞེས་བྱ་བ་ལ་དེ་ལྟར་ལྟ་ཞིང་གནས་པ་ན་ལུས་འདི་ལ་རྫས་ཡོད་པ་དང་། སྙིང་པོ་ཡོད་པར་མི་མཐོང་བའོ། །

[Block 2336]
དེ༌[^2028]ལ་རྫས་ཡོད་པར་མི་མཐོང་བ་ནི་དངོས་པོ་ཡོད་པར་མི་མཐོང་བའོ། །

[Block 2337]
སྙིང་པོ་ཡོད་པར་མི་མཐོང་བ་ནི་མཆོག་དང་དམ་པ་ཡིན་པར་མི་མཐོང་བའོ། །

[Block 2338]
དེ་ནང་གི་ལུས་ལ་ལུས་ཀྱི་རྗེས་སུ་ལྟ་ཞིང་གནས་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེ་ཞེས་བྱ་བའི༌[^2029]དོན་ཏོ། །

[Block 2339]
ནང་གི་ལུས་ནི་བདག་གི་རྒྱུད་དུ་གཏོགས༌[^2030]པའི་ལུས་སོ། །

[Block 2340]
ལུས་ལ་ལུས་ཀྱི་རྗེས་སུ་ལྟ་བ་ནི་གོང་དུ་བཤད་པ་ལྟར་བདག་གི་ལུས་ལ་ཤེས་རབ་ཀྱིས་སྟོང་པ་དང་། བདག་མེད་པར་ལྟ༌[^2031]བའོ། །

[Block 2341]
གནས་པ་ནི་དེའི་འོག་ཏུ་ཏིང་ངེ་འཛིན་གྱིས་རྩེ་གཅིག་ཏུ་འཇོག་པའོ། །

[Block 2342]
གནས་པས་ཞེས་བྱ་བ་ནི་གནས་པའི་ཕྱིར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2343]
དེ་བས་ན་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2344]
ནང་ན་གནས་པའི་ཉོན་མོངས་པ་རྣམས་ཀྱི༌[^2032]སྐབས་མི་འབྱེད༌[^2033]དོ་ཞེས་བྱ་བ་ནི་ལུས་ལ་བདག་ཏུ་ལྟ་བ་ལ་སོགས་པའི་ཉོན་མོངས་པ་རྣམས་སྐྱེ་བའི་སྐབས་མེད་པར་བྱེད་པའོ། །

[Block 2345]
ཕྱི་རོལ་གྱི༌[^2034]ནི་སེམས་ཅན༌[^2035]གཞན་གྱི་རྒྱུད་དུ་གཏོགས་པའི་ལུས་སོ། །

[Block 2346]
ལུས་ཀྱི༌[^2036]རྗེས་སུ་ལྟ་བ་ནི་གོང་མ་བཞིན་དུ་གཞན་གྱི༌[^2037]ལུས་ལ་དངོས་པོ་མེད་པ་དང་། སྟོང་པར་ལྟ་བའོ། །

[Block 2347]
ཕྱི་རོལ་གྱི༌[^2038]རྗེས་སུ་སོང་བའི་ཉོན་མོངས་པ་དང་། ལྷན་ཅིག་མི་གནས་པ་ནི་གཞན་གྱི༌[^2039]ལུས་ལ་དམིགས་པ་ལས་བྱུང་བའི་འདོད་ཆགས་དང་ཞེ་སྡང་ལ་སོགས་པའི་ཉོན་མོངས་པས་མ༌[^2040]གོས་པའོ། །

[Block 2348]
དེ་ལུས་ཉོན་མོངས་པ༌[^2041]ཅན་མ་ཡིན་པས་ཡོངས་སུ་དག་པའི་ལུས་ཀྱི་ལས་དང་ལྡན་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཉོན་མོངས་པའི་དབང་དུ་མ་གྱུར་པས་སྡིག་པ་མི་དགེ་བའི་ཆོས་མི་སྤྱོད་པའི་ལུས་ཀྱི༌[^2042]ལས་དང་ལྡན་པའོ། །

[Block 2349 [HEADING]]
###### **སྤྲུལ་པའི་སྐུ།** ^8-1-1-5-2-3-0

[Block 2350]
ལྷ་དང་མིའི་ནང་ན་མཚན་གྱིས་ལེགས་པར་བརྒྱན་པའི་ལུས་ཐོབ་ཅེས་བྱ་བ་ནི་དེ་དག་གི་ནང་ན་ཡང་མཚན་ཐམས་ཅད་ཚང་བས་བརྒྱན་པའི་ལུས་སྤྲུལ་པའི་སྐུ་འཐོབ་པའོ། །
--- END BLOCKS ---
