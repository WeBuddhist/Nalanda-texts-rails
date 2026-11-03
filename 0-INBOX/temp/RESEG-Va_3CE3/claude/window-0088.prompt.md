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
དང་པོ་ཉིད་ནས་རང་བཞིན་གྱིས་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་འདོད་ལ།[^2298] ཇི་ལྟར་འདོད་པ་བཞིན་དུ་འཐོབ་པའོ། །

[Block 3082]
དམན་པ་ཞེས་བྱ་བ་ནི། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་བྱང་ཆུབ་པོ། །དམན་པར་ཤེས་ནས་དེ་ཙམ་གྱིས་ཆོག་པར་མི་འཛིན་ཅེས་བྱ་བ་ནི་འཕགས་པའི་གང་ཟག་ཏུ་འགྱུར་ཏེ། ཉན་ཐོས་ཉིད་ཐོབ་ནས་ཕྱིས་སངས་རྒྱས་སུ་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3083]
སྐྱེ་བ་མ་མཆིས་པས་ཇི་ལྟར་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བ་ནི་འཁོར་བར་སྐྱེས་ན་ནི་བྱང་ཆུབ་ཀྱི་ཚོགས་ཡོངས་སུ་རྫོགས་པར་བྱ་ནུས་སོ་སྙམ་དུ་དགོངས་པའོ། །

[Block 3084]
[^2299]དེའི་སྐྱེ་བ་ལགས་པར་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་མ༌[^2300]སྩལ་ཏོ་ཞེས་བྱ་བ་ནི། རྒྱུན་དུ་ཞུགས་པ་ནི་འདིར་སྲིད་པ་བརྒྱད་པ་མི་སྐྱེད༌[^2301]དོ། །

[Block 3085]
ལན་ཅིག་ཕྱིར་འོང་བ་ནི་འདིར་སྲིད་པ་གཅིག་ལེན་ཏོ། །

[Block 3086]
ཕྱིར་མི་འོང་བ་ནི་འདིར་སྲིད་པ་གཅིག་ཀྱང་མི་ལེན་ཏོ། །

[Block 3087]
དགྲ་བཅོམ་པ་ནི་ཐམས་ཅད་དུ་ཡང་སྲིད་པ་མི་ལེན་ཏེ་དེ་ལྟར་སྐྱེ་བ་བཀག་གོ། །

[Block 3088 [HEADING]]
### སྐྱེ་བ་རྣམ་པ་གསུམ། ^2-6-0

[Block 3089]
བྱམས་པ་དེའི་སྐྱེ་བ་ལས་དང་ཉོན་མོངས་པའི་དབང་གིས་འགྱུར་བར་ནི་ང་མི་འདོགས་ཀྱི། དེའི་སྐྱེ་བ་བསམ་གྱིས་མི་ཁྱབ་པ་དང་། སྤྲུལ་པ་དང་ཡོངས་སུ་བསྔོས་པའོ་ཞེས༌[^2302]འདོགས་སོ་ཞེས་བྱ་བ་ལ། ལས་དང་ཉོན་མོངས་པའི་དབང་གིས་སྐྱེ་བ་ཞེས་བྱ་བ་དེ་ནི་རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པ་ལ་བྱའོ། །

[Block 3090]
སྐྱེ་བ་རྣམ་པ་གསུམ་པོ་དག་ལ་ནི་དཔྱད་པ༌[^2303]མེད་དོ། །

[Block 3091]
དེ་དག་ལ་ནི་སྐྱེ་བ་རྣམ་པ་གསུམ་ཡོད་དེ། བསམ་གྱིས་མི་ཁྱབ་པའི་སྐྱེ་བ་དང་སྤྲུལ་པའི་སྐྱེ་བ་དང་། སྨོན་ལམ་གྱི་སྐྱེ་བའོ། །

[Block 3092 [HEADING]]
#### བསམ་གྱིས་མི་ཁྱབ་པའི་སྐྱེ་བ། ^2-6-1-0

[Block 3093]
དེ་ལ་གང་ཉན་ཐོས་ཀྱི་རིགས་མ་ངེས་པ་དེ་དག་ནི། གལ་ཏེ་དེ་བཞིན་གཤེགས་པ་དང་ཉེ་བར་གྱུར་ན། དེའི་ཚེ་དེ་བཞིན་གཤེགས་པས་དེ་དག་གི་རིགས་ཀྱི་ཁྱད་པར་ལ་གཟིགས་ནས། ཇི་ལྟར་དེ༌[^2304]བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ལ་འདོད་པ་བསྐྱེད་པ༌[^2305]དེ་ལྟ་བུའི་ཆོས་བཤད་པ་མཛད་ནས། དེ་ལྟ་བུའི་ལམ་ལ་སྦྱོར་ཏེ།[^2306] འདོད་པ་དེ་ཡོངས་སུ་མ་བཏང་བར་ཡང་དག་པའི་མཐའ་མངོན་སུམ་དུ་བྱས་ནས།[^2307] རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་སོགས་པ་ཐོབ་པར་བྱེད་དོ། །

[Block 3094]
དེ་ལྟར་སངས་རྒྱས་རྣམས་ཐབས་མཁས་པའི་ཕྱིར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཚུལ་གྱིས་དེ་དག་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ལམ་ལ་བཀོད་ནས། སློབ་པའམ་མི་སློབ་པར་གྱུར་པ༌[^2308]ལ། བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ལ་འདོད་པ་མ་བཏང་བས་མྱ་ངན་ལས་འདས་པ་མངོན་དུ་བྱེད་ཀྱང་ངེས་པའི་ཉན་ཐོས་ལྟར། དེ་ལ་ཤིན་ཏུ་དྲག་པོའི་མོས་པ་མི་སྐྱེད༌[^2309]དེ། དཔེར་ན་ལ་ལ་ཞིག་གྲོང་ངམ་གྲོང་ཁྱེར་ལ་ལྟ་བ་ན། དེ་ཉིད་དུ་གནས་པར་བྱའོ་སྙམ་དུ་བསམས་ཏེ་བལྟས་ན་ནི། དེར་མོས་པར༌[^2310]མོས་པ་གཞན་དུ་འགྱུར་རོ། །

[Block 3095]
གཞན་དུ་འགྲོའོ་སྙམ་དུ་བསམས་ཏེ། བལྟས་ན་ནི་བློ་གཞན་དུ་འགྱུར་རོ། །

[Block 3096]
དེ་བཞིན་དུ་འདིར་ཡང་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་འདོད་ན༌[^2311]ནི། མྱ་ངན་ལས་འདས་པ་ལ་འདོད་པ་རྣམ་པ་གཞན་དུ་འགྱུར་ལ། ངེས་པའི་ཉན་ཐོས་རྣམས་ཀྱང་རྣམ་པ་གཞན་དུ་འགྱུར་རོ། །

[Block 3097]
དེ་བས་ན་ཉོན་མོངས་པ་སྤངས་ཀྱང་ལ་ལ་བག་ཆགས་ལ་སོགས་པའི་དབང་གིས་ཁྱད་པར་དུ་འགྱུར་ཏེ། སྙིང་རྗེའི་བསམ་པའི་དབང་གིས་ཀྱང་། དེ་དག་འཁོར་བས་ཤིན་ཏུ་སྐྱོ་བར་མི་འགྱུར་ལ། སེམས་ཅན་ལ་ཕན་པ་བྱེད་པར་འདོད་པ་རྣམས་ནི་བུ་གཞོན་ནུ་མི་གཙང་བའི་དོང་དུ་ལྟུང་བ་འབྱིན་པར་འདོད་པས་མི་གཙང་བའི་དོང་ལ་བལྟ༌[^2312]ཡང་། དེས་སྐྱོ་བར་མི་འགྱུར་བ་བཞིན་ནོ། །

[Block 3098]
སློབ་པའམ་མི་སློབ་པ་དེ་ལྟ་བུར་གྱུར་པ་དེ་དག་ནི་དེ་བཞིན་གཤེགས་པའི་མན་ངག་གིས་འཇིག་རྟེན་ལས་འདས་པ་ཟག་པ་མེད་པ། འཕགས་པའི་ལམ་ལ་སོགས་པའི་དགེ་བའི་རྩ་བ་རྣམས་འདི་ལྟར་ཡོངས་སུ་སྔོ་བར༌[^2313]བྱེད་དེ། གང་བདག༌[^2314]གི་དགེ་བའི་རྩ་བ་འཇིག་རྟེན་ལས་འདས་པ་ཟག་པ་མེད་པ་དེ་དག་ཐམས་ཅད་སེམས་ཅན་ལ་ཕན་པའི་ཕྱིར་འཁོར་བར་སྐྱེ་བ་ལ་མངོན་དུ་ཕྱོགས་པར་གྱུར་ཅིག་ཅེས་ཡོངས་སུ་བསྔོའོ། །

[Block 3099]
དེ་དག་དེ་ལྟར་ཡོངས་སུ་བསྔོས་པའི་དབང་གིས་ལམ་ལ་སོགས་པ་ཟག་པ་མེད་པའི་དགེ་བ་རྣམས་ཀྱིས་འཁོར་བར་སྐྱེ་བར་བྱེད་དེ། དེ་དག་ལ་ཡང་ལྷན་ཅིག་བྱེད་པའི་རྐྱེན་དུ་གྱུར་པ་ཉོན་མོངས་པ་དང་འདྲ་བའི་དགེ་བའི་ཆོས་རྣམས་ཡོད་དེ། འདི་ལྟར་མདོ་སྡེ་གཞན་དག་ལས་བློ་གྲོས་རྒྱ་མཚོ་འཁོར་བའི་རྒྱུན་བྱེད་ལ། དགེ་བའི་རྩ་བ་དང་མཚུངས་པར་ལྡན་པའི་ཉོན་མོངས་པ་དེ་དག་གང་ཞེ་ན། འདི་ལྟ་སྟེ་བསོད་ནམས་ཀྱི་ཚོགས་བཙལ་བས་ཡོངས་སུ་མི་ངོམས་པ་དང་། བསམས་བཞིན་དུ་སྲིད་པར་སྐྱེ་བ་ཡོངས་སུ་འཛིན་པ་དང་། སངས་རྒྱས་དང་ཕྲད་པར་སྨོན་པ་དང་། སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱ་བ་ལ་ཡོངས་སུ་མི་སྐྱོ་བ་དང་། དམ་པའི་ཆོས་ཡོངས་སུ་འཛིན་པ་ལ་བརྩོན་པ་དང་། སེམས་ཅན་གྱི་བྱ་བ་ཅི་ཡོད་སྙམ་པ་ལ་སྤྲོ་བ་དང་། ཆོས་འདོད་པའི་བག་ལ་ཉལ་མི་འདོར་བ་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྦྱོར་བ་རྣམས་ཡོངས་སུ་མི་གཏོང་བའོ། །

[Block 3100]
བློ་གྲོས་རྒྱ་མཚོ་དེ་དག་ནི་དགེ་བའི་རྩ་བ་དང་མཚུངས་པར་ལྡན་པའི་ཉོན་མོངས་པ་རྣམས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་དེ་དག་གིས་འདྲེ༌[^2315]ཡང་། ཉོན་མོངས་པའི་སྐྱོན་རྣམས་ཀྱིས༌[^2316]མི་གོས་སོ། །

[Block 3101]
གསོལ་པ་བཅོམ་ལྡན་འདས་དགེ་བའི་རྩ་བ་ལགས་ན་ཅིའི་སླད་དུ་ཉོན་མོངས་པ་རྣམས་ཞེས་བགྱི། བཀའ་སྩལ་པ། བློ་གྲོས་རྒྱ་མཚོ་འདི་ལྟར་ཉོན་མོངས་པ་དེ་ལྟ་བུ༌[^2317]དག་གིས་བྱང་ཆུབ་སེམས་དཔའ་ཁམས་གསུམ་དང་འདྲེ་ཞིང་། ཁམས་གསུམ་པ་ནི་ཉོན་མོངས་པ་ལས་བྱུང་བ་ཡིན་པས་དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་ནི་ཐབས་མཁས་པ་དང་། དགེ་བའི་རྩ་བའི་སྟོབས་བསྐྱེད་པས༌[^2318]བསམས་བཞིན་དུ་ཁམས་གསུམ་དུ་འདྲེའོ།[^2319] །དེའི་ཕྱིར་དགེ་བའི་རྩ་བ་དང་མཚུངས་པར་ལྡན་པའི་ཉོན་མོངས་པ་ཞེས་བྱ་སྟེ། ཁམས་གསུམ་དུ་འདྲེས་པས༌[^2320]དེ་སྐད་བྱའི༌[^2321]སེམས་ཉེ་བར་ཉོན་མོངས་པས་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 3102]
དེ་བས་ན་དེ་ལྟར་ཡོངས་སུ་བསྔོས་པའི་མཐུས་ཟག་པ་མེད་པའི་དགེ་བའི༌[^2322]རྩ་བ་རྣམས་ཀྱིས་སྲིད་པར་སྐྱེའོ་ཞེས་བྱའོ། །

[Block 3103 [HEADING]]
#### སྤྲུལ་པའི་སྐྱེ་བ། ^2-6-2-0

[Block 3104]
ཕྱིར་མི་འོང་བ་འམ། དགྲ་བཅོམ་པ་ལ་ལ་ཏིང་ངེ་འཛིན་གྱི་སྟོབས་བསྐྱེད་པས། མངོན་པར་ཤེས་པ་ཁྱད་པར་ཅན་དང་ལྡན་པའི་ཕྱིར་སྤྲུལ་པ་རྣམ་པ་སྣ་ཚོགས་ཀྱིས་སྐྱེ་བ་བསྟན་ནས། སེམས་ཅན་རྣམས་ཀྱི་དོན་དཔག་ཏུ་མེད་པ་བྱེད་ཅིང་། བྱང་ཆུབ་ཀྱི་ཚོགས་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་དེ་ནི་སྤྲུལ་པའི་སྐྱེ་བ་ཞེས་བྱའོ། །

[Block 3105 [HEADING]]
#### སྨོན་ལམ་གྱི་སྐྱེ་བ། ^2-6-3-0

[Block 3106]
ལ་ལ་ནི་དགེ་བའི་བཤེས་གཉེན་ལ་བརྟེན་པའི་མཐུས། དེ་ལྟ་བུའི་སྨོན་ལམ་གྱི་ཁྱད་པར་དག་ཐོག་མ་ནས་བསྩགས་པར་གྱུར་ཏེ། དེ་དག་གི་སྨོན་ལམ་དེ་དག་རྣམ་པར་སྨིན་པའི་བདག་ཉིད་དུ་གྱུར་ནས་ཡོངས་སུ་བསྔོས་པའི་སྐྱེ་བ་དག་སྒྲུབ་པར་བྱེད་དེ། དེ་ནི་ཡོངས་སུ་བསྔོས་པའི་སྐྱེ་བ་ཞེས་བྱའོ། །

[Block 3107]
འོ་ན་དེ་དག་ཅིའི་ཕྱིར་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་སོགས་པ་མ་ཐོབ་པར། བྱང་ཆུབ་ཀྱི་ཕྱོགས༌[^2323]ཡོངས་སུ་རྫོགས་པར་མི་བྱེད་ཅེ་ན། [^2324]མེད་པའི་ཕྱིར་ཏེ། འདི་ལྟར་དེ་དག་ནི་ཉོན་མོངས་པ་ཤས་ཆེ་ལ་དབང་པོ་རྟུལ༌[^2325]ཏེ། དབང་པོ་སྦྱང་བར་བྱ་བ་དང་། ཉོན་མོངས་པ་སྤངས་པ་མེད་པར་བྱང་ཆུབ་ཀྱི་ཚོགས་ཡོངས་སུ་རྫོགས་པར་བྱེད་མི་ནུས་ཏེ། དེ་བས་ན་དེ་བཞིན་གཤེགས་པ་ཐབས་མཁས་པས་དེ་དག་ལ་དེ་ལྟ་བུའི་མཐུ་མཆོག་དང་ལྡན་པར་མཛད་དོ། །

[Block 3108]
ཇི་སྐད་དུ་མདོ་སྡེ་གཞན་དག་ལས།

[Block 3109]
བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པས་ཉན་ཐོས་རྣམས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ལུང་བསྟན་པ་དེ་དག་ཇི་ལྟར་བལྟ་བར་བགྱི། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རིགས་ཀྱི་བུ་ངས་ཉན་ཐོས་རྣམས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ལུང་བསྟན་པ་གང་ཡིན་པ་དེ་དག་ནི། རིགས་ལ་བལྟས་ཏེ་ལུང་བསྟན་པའོ། །

[Block 3110]
གསོལ་པ་བཅོམ་ལྡན་འདས། ཉན་ཐོས་ཟག་པ་མ་མཆིས་པ་སྲིད་པར་ཀུན་དུ་སྦྱོར་བ་རྒྱུན་བཅད་པ་རྣམས་རིགས་མཆིས་སུ་ལགས་ཀྱང་ཇི་ལྟར་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འགྱུར། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རིགས་ཀྱི་བུ་དེ་བས་དཔེ་བསྟན་གྱི༌[^2326]ཉོན་ཅིག །རིགས་ཀྱི་བུ་འདི་ལྟ་སྟེ་དཔེར་ན་རྒྱལ་པོ་རྒྱལ་རིགས་སྤྱི་བོ་ནས་དབང་བསྐུར་བ་ལ་བུ་ཞིག་ཡོད་དེ།

[Block 3111]
དེ་ཡང་བཟོའི༌[^2327]གནས་ཐམས་ཅད་ལ་སློབ་པ་ལས།

[Block 3112]
དེ༌[^2328]དབང་པོ་རྟུལ༌[^2329]ཞིང་དབང་པོ་རྣོ་བ་མ་ཡིན་པས། ཕྱིས་བསླབ་པར་བྱ་བ་གང་ཡིན་པ་དེ་ནི་སྔར་སློབ། སྔར་བསླབ་པར་བྱ་བ་གང་ཡིན་པ་དེ་ནི་ཕྱིས་སློབ་པར་བྱེད་ན། རིགས་ཀྱི་བུ་དེ་ཇི་སྙམ་དུ་སེམས། ཅིའི་རྒྱུ་དེས་རྒྱལ་པོའི་བུ་མ་ཡིན་ཞེས་བྱ་བའམ། གསོལ་པ་བཅོམ་ལྡན་འདས་དེ་ནི་མ་ལགས་སོ། །

[Block 3113]
བདེ་བར་གཤེགས་པ་དེ་ནི་མ་ལགས་ཏེ། བཅོམ་ལྡན་འདས་དེ་རྒྱལ་པོའི་བུ་ཉིད་ལགས་སོ་ཞེས་བགྱིའོ། །

[Block 3114]
རིགས་ཀྱི་བུ་དེ་དེ༌[^2330]བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་དབང་པོ་རྟུལ་པོ༌[^2331]རིགས་དང་ལྡན་པ་རྣམ་པ་བསྒོམ༌[^2332]པའི་ལམ་གྱིས་སྔར་ཉོན་མོངས་པ་རྣམས་ཟད་པར་བྱས་ནས། ཕྱིས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར༌[^2333]འཚང་རྒྱ་བར་བྱེད་ན། རིགས་ཀྱི་བུ་དེ་ཇི་སྙམ་དུ་སེམས་རྒྱུ་དེས་མངོན་པར་རྫོགས་པར་སངས་མ་རྒྱས་ཞེས་བྱ་བའམ། གསོལ་པ་བཅོམ་ལྡན་འདས་དེ་ནི་མ་ལགས་སོ། །

[Block 3115]
བདེ་བར་གཤེགས་པ་དེ་ནི་མ་ལགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ལྟ་བུའོ། །

[Block 3116]
དེ་བས་ན་དེ་ལྟར་སྐྱེ་བ་རྣམ་པ་གསུམ་གྱི་དབང་གིས་སྐྱེས་ནས་བྱང་ཆུབ་ཀྱི་ཚོགས་ཡོངས་སུ་རྫོགས་པར་བྱེད་དོ། །

[Block 3117 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 3118 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 3119]
འཕགས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འབུམ་པ་དང་། ཉི་ཁྲི་ལྔ་སྟོང་པ་དང་། ཁྲི་བརྒྱད་སྟོང་པ་རྒྱ་ཆེར་བཤད་པ་རྫོགས་སོ།། །།

[Block 3120 [HEADING]]
### འགྱུར་བྱང། ^b-2-0
--- END BLOCKS ---
