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
[Block 2556]
དབུལ་པོའི་གནས་སུ་སོང་ཞེས་པ་ནི་ཐེག་པ་རྣམ་གཉིས་ཀྱི་ཡོན་ཏན་ཆུང་ངུ་ལ་ཞུགས་པའོ། །

[Block 2557]
ཟས་ཚོལ་ཞེས་པ་ནི་ཟག་པ་མེད་པའི་ཆོས་ལ་ཞུགས་པའོ། །

[Block 2558]
མདོ་ལས་དེ་ནས་ཁྱིམ་བདག་དེས་མི་དབུལ་པོ་དེ་དགུག་པའི་སླད་དུ་ཞེས་པ་ནས་ལས་བྱེད་དུ་ཆུག་ཅེས་པའི་བར་དུ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་བསྒོམ་དུ་གཞུག་ཅིང་རྣམ་པར་གྲོལ་བ་ཐོབ་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2559]
མི་གཉིས་ཞེས་པ་ནི་ཐེག་པ་རྣམ་གཉིས་ཀྱི་བསྟན་པ་ལ་གཟུད༌[^2151]པའོ། །

[Block 2560]
ཐེག་པ་རྣམ་གཉིས་ཀྱི་བསྟན་པ་རྒྱ་ཆུང་ཞིང་ངེས་པའི་དོན་མ་ཡིན་པས་མདོག་མི་སྡུག་ལ་མདངས་ངན་ཞེས་སྦྱར་རོ། །

[Block 2561]
ཡང་ན་བསྟན་པ་ཕྱོགས་གཅིག་པའི་མདོག་མི་སྡུག་པ་དང་། གཞུང་མ་རྫོགས་པའི་ཕྱིར་མདངས་ངན་ཞེས་སྦྱར་རོ། །

[Block 2562]
མདོ་ལས་དེ་ལ་གལ་ཏེ་འདི་སྐད་དུ་ལས་ཅི་བྱ་ཞེས་པ་ནས་སྨོས་ཤིག་ཅེས་པའི་བར་དུ་ཕྱག་དར་གྱི་ཕུང་པོ་ཞེས་པ་ནི་ཉོན་མོངས་པའི་ཚོགས་སོ། །

[Block 2563]
མདོ་ལས་དེ་ནས་མི་དེ་གཉིས་ཀྱིས་དབུལ་པོ་དེ་བཙལ༌[^2152]ནས་ཞེས་པ་ནས་མི་དབུལ་པོ་དེ་ཡང་ཁྱིམ་བདག་དེ་ལ་ཕར་འདུ་ཤེས་ཞེས་པའི་བར་དུ་ནི་མི་དེ་གཉིས་ཀྱི༌[^2153]བཀའ་མཉན་ཏེ༌[^2154]ཞེས་པ་ནི་ཐེག་པ་རྣམ་གཉིས་པ་ཉོན་མོངས་པ༌[^2155]སྤོང་བ་ལ་ཞུགས༌[^2156]ཞེས་པའི་དོན་ཏོ། །

[Block 2564]
སླར་ཡང་མི་ངན་པའི་ལས་བྱེད་ཅིང་ཞེས་པ་ནི་ཐེག་པ་རྣམ་གཉིས་དང་པོ་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་རྣམས་ཀྱང་ཐོས་པ་དང་། སེམས་པའི་ཤེས་རབ་ལ་འཇུག་པའོ། །

[Block 2565]
དེ་ཉེ་བར་བསྙེན་པ༌[^2157]དང་། ཐབས་ཀྱིས༌[^2158]དྲང་བའི་ཕྱིར་ཁྱིམ་བདག་དེ༌[^2159]བསྙེན་ཅིང་ཚིག་སྤྲས༌[^2160]པའོ། །

[Block 2566]
མདོ་ལས་ཁྱིམ་བདག་དེ་སྐར་ཁུང་གི་གསེབ་ནས་བུ་ཕྱག་དར་བྱེད་པ་མཐོང་ནས། གོས་དང་རྒྱན་ཕུད་དེ་བུའི་གན་དུ་ཕྱིན་ཞེས་པ་ནི་ལུས་ཀྱི་ཚུལ་འདྲ་བ་བསྟན་པ་ཡང་དང་པོ་ནས་ཐེག་པ་ཆེན་པོ་ལ་གཟུད་པའི༌[^2161]དབང་པོ་དང་མི་ལྡན་པས་བགས་ཀྱིས་ཐབས་ཀྱིས་དྲང་བ་དང་། བསྙེན་ཞེས་པའི་དོན་ཏེ། བསོད་ནམས་དང་ཡེ་ཤེས་མ་རྫོགས་པའི་ཕྱིར་རྒྱང་མ་ནས་མཐོང་ཞིང་རྒྱན་མེད་པའོ། །

[Block 2567]
ཞིང་རྣམ་པར་དག་པ་ན༌[^2162]བཞུགས་ཤིང་། རྒྱན་ཐམས་ཅད་ཀྱིས་བརྒྱན་པའི་སྐུ་བསྟན་ན་སྐྲག་ཅིང་ཉེར་མི་བཟོད་པའི་ཕྱིར་ཡུལ་ཁམས་ངན་པ་དང་། རྒྱན་མེད་པའི་ལུས་ཀྱིས༌[^2163]གདུལ་བར་འོས་པའི་ཕྱིར་གོས་དྲི་མ་ཅན་གྱོན་ཅིང་ལག་ན་ཕྱག་དར་གྱི་སྐོན་པ་ཐོགས་པ་བཞིན་དྲང་བའི་དོན་གྱིས་ཉོན་མོངས་པ་སེལ་བའི་ཕྱིར་ལས་ཀྱིས་གཞན་འདེབས༌[^2164]པར་སྟོན་ཅིང་། དེ་དང་སྨྲ་བར་བྱེད་པ་ནི། ཐུགས་རྗེའི༌[^2165]ཐབས་ཀྱིས་འདྲེན་ཅིང་། རྣམ་པར་དག་པའི་ཕྱོགས་ལ་བརྩོན་པར་གཞན་འདེབས༌[^2166]པའོ། །

[Block 2568]
གླ་གཞན་པས་སྐྱེད༌[^2167]དེ་སྦྱིན་ནོ་ཞེས་པ་ནི་སྔར་ཐོས་པ་དང་བསམས་པའི༌[^2168]ཤེས་རབ་ལས་དགེ་བའི་རྩ་བ་རྣམ་པ་བཞིར་སྤང་བ། གཞན༌[^2169]དུ་མ་འགྲོ་ཤིག་པ་ཡང་ལྟ་བ་ངན་པ་གཞན་ལས༌[^2170]ཟློག་པའི་དོན་ཏོ། །

[Block 2569]
ཅི་དང་ཅི་དགོས་པ་ཐམས་ཅད་སྦྱིན་ནོ་ཞེས་པ་ནི་རྣམ་པར་གྲོལ་བའི་མཐུ་ལས་བྱུང་བ་ཚད་མེད་པ་བཞི་ལ་སོགས་པའི་རྒྱུས་བསྐྱེད་པ་འཕགས་པའི་ཡོན་ཏན་ཐམས་ཅད་དོ། །

[Block 2570]
བུམ་པ་དང་། ཕྲུ་བ་དང་། ཤིང་དང་། ལན་ཚ་ཞེས་པ་ནི་ཟག་པ་དང་བཅས་པའི་ཡེ་ཤེས་རྣམ་གཉིས་ཀྱིས་ཟིན་པ་འཕགས་པ་ཉན་ཐོས་རྣམས་ཀྱི་རྫུ་འཕྲུལ་དང་། སྟོབས་དང་མངོན་པར་ཞེས༌[^2171]པ་དག་གོ། ཁྱོད་ཀྱི་ཕ་ཇི་ལྟ་བ་བཞིན་ཞེས་པ་ནི་འཕགས་པ་ཉན་ཐོས་རྣམས་ཉོན་མོངས་པ་སྤངས་ཤིང་འཕགས་པའི་གནས་སུ་སོན་པའི་ཕྱིར་བུ་ཞེས་བཀའ་སྩལ། ཡང་དག་པའི་བདེན་པ་ཉིད་མི་མཐོང་བའི་ཕྱིར་ནི་བུ་དང་འདྲ་བ་ཞེས་སྨོས་སོ། །

[Block 2571]
སྒྱུའམ༌[^2172]གྱ་གྱུའམ། གཡོ་ཞེས་པ་ནི་ལུས་དང་ངག་དང་ཡིད་གསུམ་གྱི་དྲི་མ་སྤོང༌[^2173]ཞེས་པའི་དོན་ཏོ། །

[Block 2572]
མི་དབུལ་པོ་དེ་བུ་ཞེས་མིང་དུ་བཏགས་པ་ཞེས་པ་ནི་འཕགས་པར་གྱུར་ཞེས་པའི་དོན་ཏོ། །

[Block 2573]
འབྲས་བུ་དང་པོ་ལ་གནས་པའོ། །

[Block 2574]
མདོ་ལས་ལོ་ཉི་ཤུ་འདས་པ་དང་ཞེས་པ་ནས་སྤྱིལ་པོ་དེ་ཉིད་ན་གནས་ཤིང་མཆིས་པ་ལ༌[^2174]ཞེས་པའི་བར་དུ་ནི། བསྒོམ་པའི་ལམ་ལ་གནས་པའོ། །

[Block 2575]
ཉི་ཤུ་ཞེས་པ་ནི་ཟག་པ་མེད་པའི་ཆོས་བཅུ་སྤྱོད་པས་ཁམས་གཉིས་ཀྱི་ཉོན་མོངས་པ་སྤོང་བའོ། །

[Block 2576]
སྤྱིལ་པོ་དེ་ཉིད་ན་གནས༌[^2175]པ་ནི་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ལ་གནས་པས་ཏིང་ངེ་འཛིན་ནས་མི་སློབ་པའི་ལམ་ལ་གནས་པ་གང་ཟག་ལ་བདག་མེད་པར་རྟོགས་པའི༌[^2176]རྣམ་པར་གྲོལ་བ་ཐོབ་པ་སྟེ། སེམས་ཅན་སྒྲོལ་བ་ལ་འཇིགས་པ་དང་། ཐོགས་པ་མེད་པར་གནས་པ། འབྲས་བུ་ཆེན་པོ་སྒྲུབ་པ་ལ་མི་འཇིགས་པའི་ཕྱིར། སྤྱིལ་པོ་དེ་ཉིད་ན་གནས་ཞེས་པའོ། །

[Block 2577]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཁྱིམ་བདག་དེ་བྲོ་འཚལ༌[^2177]བར་གྱུར་ཏེ་ཞེས་པ་ནས་དེ་ཐམས་ཅད་ཁྱོད་ཀྱིས༌[^2178]ཤེས་པར་འདོད་དོ་ཞེས་པའི་བར་དུ་ནི་དོན་ཆེན་པོ་ལ་དགའ་བའི་དོན་བསྟན་ཏེ། ཁྱིམ་བདག་དེ་ན་བར་གྱུར་ཞེས་པ་ནི། བཅོམ་ལྡན་འདས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས། ལོ་བཅུ་གཉིས་ལོན་པ་དང་སེམས་ཅན་རྣམས་ཉོན་མོངས་པ་ཕྱིར་ཞིང་འཕེལ་བར་གྱུར་པས་སེམས་ཅན་ཉོན་མོངས་པའི༌[^2179]ནད་ཀྱིས་བཏབ་པ༌[^2180]ན། བཅོམ་ལྡན་འདས་ཀྱང་བསྙུང་བ་ཞེས་པའི་དོན་ཏོ། །

[Block 2578]
དམ་པའི་ཆོས་འདི་བཤད་པའི་དུས་ནི་བཅོམ་ལྡན་འདས་མྱ་ངན་ལས་འདའ་བའི༌[^2181]དུས་དང་ཉེ་བས་སེམས་ཅན་མ༌[^2182]བསྒྲལ་བ་རྣམས་བསྒྲལ་ཟིན་པའི༌[^2183]ཕྱིར་ཁྱིམ་བདག་གུམ་པའི་དུས་ལ་བབ་པར་མཐོང་ཞེས་བྱའོ། །

[Block 2579]
སངས་རྒྱས༌[^2184]བྱང་ཆུབ་སེམས་དཔའ་རྣམས༌[^2185]འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་ཡོན་ཏན་ཐམས་ཅད་ནི་བང་མཛོད་མང་པོའི་ནོར་ཞེས་བྱའོ། །

[Block 2580]
དེ་ལ་ཡང་ཐེག་པ་ཆེན་པོ་ནི་ཤས་ཆེ་ཐེག་པ་ཆུང་ངུ་ནི་ཤས་ཆུང་ཞེས་སོ། །

[Block 2581]
སྦྱིན་པ་དང་སྦ་བར་བྱ་ཞེས་པ་ནི་བླང་བ་ནི་བདག་གི་དོན་ཏོ། །

[Block 2582]
སྦྱིན་པ་ནི་གཞན་གྱི་དོན་ཞེས་པའོ། །ཤེས་པར་བྱོས་ཤིག་ཅེས་བྱ་བ་ནི་ཐེག་པ་ཆེན་པོའི་གཞུང་མི་ཤེས་པ་ཤེས་པར་བྱ་བ་དང་། སེམས་མ་བསྐྱེད་པ་སྐྱེད་ཅིག་པར་བསྟན་པའོ། །

[Block 2583]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་པ་ནས་ཆུད་མ་གཟན༌[^2186]ཞེས་པའི་བར་དུ་ནི་འདིས༌[^2187]ཐེག་པ་ཆེན་པོ་ལ་མོས་པ་བསྟན་པ་སྟེ།[^2188] ཇི་ལྟར་འཇིག་རྟེན་ན་ཕ་དང་བུ་སྤྱོད་པ་མཐུན་པ་ལྟར། དེ་བཞིན་གཤེགས་པ་དང་། ཐེག་པ་རྣམ་གཉིས་ཀྱང་རྣམ་པར་གྲོལ་བ་དང་། དེ་བཞིན་ཉིད་མཐུན་པར་བསྟན་པས་ཆོས་ཆེན་པོ་ལ་གཞུག༌[^2189]ཅིང་། དོན་མཉམ་པར༌[^2190]གྱིས་ཤིག་པར་བསྟན་པའོ། །

[Block 2584]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་མི་དབུལ་པོ་དེ་ཞེས་པ་ནས་ཆུང་ཟད༌[^2191]ཀྱང་རེ་བ་མེད་དོ་ཞེས་པའི་བར་དུ་ནི་རེ་བ་མེད་པར་བསྟན་ཏེ། ཐེག་པ་རྣམ་གཉིས་ཀྱི་དེ་ལྟར་ཐེག་པ་ཆེན་པོའི་ཆོས་ཐོས་སུ་ཟིན་ཀྱང་ད་ཅུང་སེམས་ཞན༌[^2192]པ་སྔོན་གྱིས༌[^2193]འཛིན་ཅིང་། སྤོབས་པ་མི་ཆེ་བའི་དཔེའོ། །

[Block 2585]
མདོ་ལས་སྤྱིལ་པོ་དེར༌[^2194]གནས་ཤིང་ཞེས་པ་ནས་དེ་ཉིད་ཀྱི་རྗེས་སུ་སེམས་སོ་ཞེས་པའི་བར་དུ་ནི་སེམས་ཞན་པ༌[^2195]ད་དུང་མ་སྤངས་ཞེས་བསྡུས་པའོ། །

[Block 2586]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས། གཉེན་བཤེས་མང་པོ་དང་ཕྲད་དེ་ཞེས་པའི་བར་དུ་ནི་དེས་ཐོབ་པའི་དཔེ་བསྟན་ཏེ། དེ་ཡང་དུས་ལ་བབ་པ་དང་། མང་པོ་བསྡུས་ཏེ་གཏོད༌[^2196]པའོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནས་དམ་པའི་ཆོས་འདི་བསྟན་པའི་བར་དུ་ནི༌[^2197]ཁད་ཀྱིས༌[^2198]དབང་པོ་འབོགས༌[^2199]པའི་ཕྱིར་ཡོངས་སུ་སྨིན་པར་ཤེས་པའོ། །ཤེས་པ་ནི་སྟོང་པ་རྣམ་གཉིས་ཀྱི་དོན་ཤེས་པའོ། །

[Block 2587]
ཉམ་ང་ཞིང་ངོ་ཚ་བ་ནི་སྔོན་གྱི་སྤྱོད་པ་ཞན་པ༌[^2200]ཐེག་པ་ཆུང་ངུ་ལ་ཞུགས་པའི་སེམས་སོ། །

[Block 2588]
འཆི་བའི་དུས་ལ་བབ་པ་ཞེས་པ་ནི་ཡོངས་ལ་གཏད་པ༌[^2201]སྟེ། དམ་པའི་ཆོས་འདི་བཤད་པ་ནས་བཅོམ་ལྡན་འདས་མྱ་ངན་ལས་འདས་པའི་བར་དུ་ལོ་ལྔ་ཞིག་ལུས་པའི་ཕྱིར་འཆི་བའི་དུས་ལ་བབ་པའོ། །

[Block 2589]
གཉེན་བཤེས་མང་པོ་ཞེས་པ་ནི་འཕགས་པ་ཉན་ཐོས་ཆེན་པོ་དག་གོ། །

[Block 2590]
རྒྱལ་པོ་དང༌[^2202]བློན་པོ་ཞེས་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་རིགས་རྣམས་སོ། །

[Block 2591]
མདོ་ལས་ཁྱོད་ཉོན་ཅིག་འདི་ནི་ཁོ་བོའི་སྙིང་གི་བུ་ཁོ་བོས་བསྐྱེད་པ༌[^2203]སྟེ་ཞེས་པ་ནི་སྔོན་གྱི་རྒྱལ་བུ་བཅུ་དྲུག་གི་ཚེ་ན་ངའི་བསྟན་པ་འདི་ལ་སེམས་བསྐྱེད་དེ་དགེ་བའི་རྩ་བ་བཙུགས་པས་ངའི་གསུང་ལས་སྐྱེས་པ༌[^2204]ངའི་ཆོས་ཀྱིས་བསྐྱེད་པ་ཡིན་པས་ཡང་དག་པའི་སྲས་ཞེས་བྱའོ། །

[Block 2592]
མདོ་ལས་གྲོང༌[^2205]ཁྱེར་གྱི་མིང་འདི་འཁྱམས་ནས༌[^2206]ལོ་ལྔ་བཅུ་ལོན་ཏེ་ཞེས་པ་ནི་འཁོར་བར་འཁོར་བ་བསྟན་ཏེ། གྲོང་ཁྱེར་ཞེས་པ་ནི་ཐེག་པ་ཆེན་པོའོ། །

[Block 2593]
ཐེག་པ་ཆེན་པོར་རིགས་ངེས་པ་དང་། དབང་པོ་རྣོན་པོ་རྣམས་ནི་ལན་ཅིག་སེམས་བསྐྱེད་པས་ཕྱིར༌[^2207]ལྡོག་པར་ཡང་མི་འགྱུར་ན། དབང་པོ་ཞན་པ་དང་། རིགས་མ་ངེས་པ་རྣམས་ལྡོག་ཅིང་ལྟུང་བར༌[^2208]འགྱུར་བ༌[^2209]ཡོད་དོ་བར་བསྟན་ཏོ། །

[Block 2594]
མདོ་ལས་འདིའི་མིང་ནི་འདི་ཞེས་བྱ་ཞེས་པ་ནས་དེ་ཀུན་ཀྱང་འདི་ཉིད་ཤེས་སོ་ཞེས་པའི་བར་དུ་ནི་སྔོན་ཡང་དེ་བཞིན་གཤེགས་པ་ངའི་བསྟན་པ་ལ་ཞུགས་པ༌[^2210]ལས་རབ་ཏུ༌[^2211]འཁྱམས་པ་དང་། དེ༌[^2212]ཡང་ཐེག་པ་ཆེན་པོ་ལ་ཞུགས་ཞེས་པའི་དོན་ཏེ།[^2213] ཇི་ལྟར་འཕགས་པ་ཤཱ་རིའི་བུ་བསྐལ་པ༌[^2214]དྲུག་ཅུའི་བར་དུ་ཐེག་པ་ཆུང་ངུ་སྤྱོད་སྤྱོད་པ་ལས་ད་ཐེག་པ་ཆེན་པོ་ལ་ཞུགས་པ་ཉིད་གྲོང་ཁྱེར་དེ་ན་གནས་པ་ཞེས་བྱའོ། །

[Block 2595]
ཚོལ༌[^2215]ཞེས་པ་ནི་ཐུགས་རྗེས་དགོངས་པའི་དོན་ཏོ། །
--- END BLOCKS ---
