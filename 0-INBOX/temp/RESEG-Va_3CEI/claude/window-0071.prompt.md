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
[Block 2486]
སྨོན་པ་མེད་པ་ནི་མྱ་ངན་ལས་འདས་པའི་འདུས་མ་བྱས་སོ། །

[Block 2487]
འདུས་བྱས་ཀྱི་ཆོས་ཐམས་ཅད་ནི་སྨོན་པ་མེད་པ་སྟེ། ཟག་པ་དང་བཅས་པ་དང་། ཟག་པ་མེད་པའི་ཤེས་རབ་ཀྱིས་བསྡུས་པའོ། །

[Block 2488]
བྱང་ཆུབ་སེམས་དཔའི་ཆོས་ཞེས་པ་ནི། བྱང་ཆུབ་ཀྱི་ཕྱོགས་རྣམས་ཀྱི་ཆོས་ཏེ། དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་དང་། ཡང་དག་པར་སྤོང་བ་བཞི་དང་། རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞི་དང་། དབང་པོ་ལྔ་དང་། སྟོབས་ལྔ་དང་། བྱང་ཆུབ་ཀྱི་ཡན་ལག་བདུན་དང་། འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པའོ། །

[Block 2489]
བྱང་ཆུབ་སེམས་དཔའ་ནི་རྣམ་པར་རོལ་པ་ཡང་རྣམ་པ་བཅུ་སྟེ། ལྷའི་སྐུ་ཚེ་སྤང་བ་དང་། གཞན་དུ་སྐྱེ་བ་སྟོན་པ་དང་། མངོན་དུ་བཙས་ཏེ་དགྱེས་རོལ་པ་དང་། ཁབ་ནས་བྱུང་བ་དང་། དཀའ་ཐུབ་མཛད་པ་དང་། བྱང་ཆུབ་ཀྱི་ཤིང་དྲུང་དུ་གཤེགས་པ་དང་། བདུད་འདུལ་བ་དང་། ཏིང་ངེ་འཛིན་གྱི་དགའ་བ་ལ་བཞུགས་ཤིང་། ལྷའི་ཡང་ལྷར་གྲུབ་པ་སྟོན་པ་དང་། ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་སྟོན་པ་དང་། མྱ་ངན་ལས་འདས་པ་སྟོན་པའོ། །

[Block 2490]
སངས་རྒྱས་ཀྱི་ཞིང་གི་རྒྱན་དག་ཅེས་པ་ནི། མདོ་ལས་རྒྱུ་རྣམ་པ་བརྒྱད་དེ། བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པས། ཡིད་གཅིག་ཏུ་མོས་པ་ལྷག་པའི་སྤྱོད་པ་ལ༌[^2073]མཁས་པས་བླ་ན་མེད་པར་མོས་པའི་ཡིད་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་སྤྱོད་པའི་སེམས་དང་ལྡན་པ་དག་གོ། །

[Block 2491]
ཚད་མེད་པ་བཞི་དང་། བསྡུ་བ་རྣམ༌[^2074]བཞི་དང་། ཐབས་མཁས་པས་བྱང་ཆུབ་ཀྱི་ཕྱོགས་རྣམས་སྤྱོད་པ་ཐམས་ཅད་བླ་ན་མེད་པར་བསྔོ་བ༌[^2075]ནི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའོ། །

[Block 2492]
མདོ་ལས་དེ་ཅིའི་སླད་དུ་ཞེ་ན། བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་མོས་པའི་སེམས་གཅིག་ཀྱང་བསྐྱེད་པར་མ་གྱུར་ཏེ་ཞེས་པའི་བར་དུ་ནི་གཏན་ཚིགས༌[^2076]སྨོས་པ་སྟེ། ལམ་མངོན་དུ་གྱུར་པས་སྡུག་བསྔལ་མི་སྐྱེ་བ་དང་། རྒས་པས་སྤྱོད་པ་གཞན་ལ་འཇུག་མི་ནུས་ཞེས་པའི་དོན་ཏོ། །

[Block 2493]
མདོ་ལས་བཅོམ་ལྡན་འདས་བདག་ཅག་གིས༌[^2077]བཅོམ་ལྡན་འདས་ཀྱི་དྲུང་ནས་ཞེས་པ་ནས་འདི་ལྟ་བུའི་རིན་པོ་ཆེ་འདི་ཐོབ་སྟེ་ཞེས་པའི་བར་དུ་ནི༌[^2078]འདིར་ཐེག་པ་ཆེན་པོའི་དོན་རྟོགས་པར༌[^2079]བསྟན་ཏེ། ལུང་བསྟན་པ་ཐོས་པ་དང་། ཆོས་བཤད་པའི་དགའ་བས་ངོམས་པ་དང་། ཐེག་པ་ཆེན་པོའི་ཆོས་རིན་པོ་ཆེ་ཐོབ་པའོ། །

[Block 2494 [HEADING]]
###### དཔེས་གླེང་བ། ^4-4-2-1-2-0

[Block 2495]
མདོ་ལས་བཅོམ་ལྡན་འདས་འདི་ལྟ་སྟེ་དཔེར་ན་མི་ལ་ལ་ཞིག་འདི་ལྟར་ཞེས་པ་ནི་ཚིག་དང་པོ་དེས་ནི།

[Block 2496]
བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའི་དཔེར་བསྟན་པ་ལས།

[Block 2497]
ལོགས༌[^2080]ཤིག་ཏུ་སོང་ཞེས་པ་ནི་འཁོར་བར་འཁོར་བའི་དཔེ་བསྟན། ནར་སོན་ཏེ་ཞེས་པ་ནི། ཕྱིས་སངས་རྒྱས་སུ་གྲུབ་པའི༌[^2081]དཔེ་བསྟན། ཕས་བུ་དྲན༌[^2082]ཡང་ཞེས་པ་ནི་ཐེག་པ་ཆེན་པོ་ལ་འཇུག་ཏུ་མི་བཏུབ་པའི་དཔེ་བསྟན། ཕས་རྒྱང་ནས་མཐོང་ཞེས་པ་ནི་ཐེག་པ་གཉིས་ཀྱི་དཔེ་བསྟན། ཁྱིམ་བདག་དེ་ལ་མཛོད་དང་ནོར་མང་དུ་ཡོད་ཅེས་པ་ནི་ཐེག་པ་ཆེན་པོའི༌[^2083]དཔེ་བསྟན་ཏོ།[^2084] །དེ་ན་གཞོན༌[^2085]ཞེས་པ་ནི་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་སེམས་མ༌[^2086]བསྐྱེད་པ་ལ་བྱའོ། །

[Block 2498]
མདོ་ལས་ཕའི་གནས༌[^2087]ནས་ལོགས་ཤིག་ཏུ་མཆིས་ལ་ཞེས་པ་ནས་ལོ་ལྔ་བཅུར་གནས་ཏེ་ཞེས་པའི་བར་དུ་ནི་འཇིག༌[^2088]རྟེན་དང་འཁོར་བའི་དཔེ་སྟེ། མདོ་ལས་དབང་པོ་རྣོན་པོ་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་ཇི་ལྟར་ཡུན་རིང་དུ་འཁོར་བར་འཁོར་ཡང་ངན་སོང་དུ་མི་ལྟུང་སྟེ། ཕྱིས་ཀྱང་བྱང་ཆུབ་ཀྱི་སེམས་སྐྱེ་ཞེས་པའི་དོན་ཏོ། །

[Block 2499]
ལས་ཀྱི་སྒྲིབ་པས་ཟིན་ཏེ་ཡིད་གཅིག་ཏུ་ངེས་པས་སངས་རྒྱས་མི་ཚོལ་བའི༌[^2089]ཕྱིར་ཕ་ལས་ལོགས་ཤིག་ཏུ་སོང་ཞེས་བྱའོ། །

[Block 2500]
ཡུལ་ཕྱོགས་གཞན་ཞེས་པ་ནི་སངས་རྒྱས་ཀྱི་ཡུལ་ལས་གཞན་དུ་གྱུར་པ་རྣམས་སོ། །

[Block 2501]
ལོ་ཉི་ཤུ་དང་སུམ་ཅུ་ཞེས་པ་ནི་རྒྱུད་རྣམ་ལྔར་འཁོར་ཞེས་པའི་དོན་ཏོ། །

[Block 2502]
མདོ་ལས་བཅོམ་ལྡན་འདས་དེ་ནས་མི་དེས་ཆེན་པོ་ཞིག་ཏུ་ལགས་ལ་ཞེས་པ་ནས། ཡུལ་ཕྱོགས་ཞིག་ཏུ་ཕྱིན་ཏེ་ཞེས་པའི་བར་དུ་ནི་སངས་རྒྱས་དང་ཕྲད་པའི་དཔེ་བསྟན་ཏེ། བྱང་ཆུབ་ཀྱི་སེམས་མ་སྟོར་བའི་ཕྱིར་ཐེག་པ་ཆེན་པོ་ཐོས་ཤིང་སངས་རྒྱས་སུ་གྲུབ་པ༌[^2090]ཞེས་པའི་དོན་ཏོ། །

[Block 2503]
དེ་ཡང་བུ་ནར་སོན་ཏེ་ཡུལ་འཁོར་དུ་ཕྱིན་པ་ན།[^2091] ཕས་ཀྱང་སྔ་ནས་བཙལ་བ་ལས་ཕྱིས༌[^2092]ཕྲད་ཅེས་པར་སྦྱར་ཏེ། འདི་ནི་དང་པོའོ། །

[Block 2504]
དང་པོ༌[^2093]ལ་ཡང་རྣམ་པ་དྲུག་ཏུ་དབྱེ་སྟེ། དབང་པོ་ཁད་ཀྱིས་སྨིན་པ་ནི་ནར་སོན་པ་དང་སྦྱར། ཤེས་རབ་མ་བསྒོམས་པ་ནི་དབུལ་པོར་གྱུར་ཞེས་པ་དང་སྦྱར་ཏེ། [^2094]འཁོར་བར་འཁོར་བ་ནི་ཕྱོགས་དང་ཕྱོགས་མཚམས་སུ་སོན་པ་དང་སྦྱར། སྐྱེ་ཞིང༌[^2095]སྡུག་བསྔལ་ལས་འབྱུང་བར་རྩོལ་བ་ནི་འཚོ་བ་ཚོལ་བ་དང་སྦྱར། ཤེས་རབ་རྣམ་གསུམ་གྱི་ལས་སྤྱོད་པ་ནི་ཁད་ཀྱིས༌[^2096]ཁྱིམ་དུ་ཉེ་བ་དང་སྦྱར་རོ། །

[Block 2505]
མདོ་ལས་དེའི་ཕ་དེ་ཡང་ཞེས་པ་ནས་འཚོ་བ་ཡང་མང་དུ་གྱུར་ཏེ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་རྣམ་པ་གསུམ་དུ་བསྡུས་ཏེ། སྔོན་ཚོལ་ཚོལ་བའི་བུ་མཁར་དུ་སླར་ཕྱིན་པ་དང་། ནོར་དང་འཚོ་བ་མང་བར་གྱུར་པ་དང་། གཡོག་དང་ཡུལ་ཆེན་པོར་གྱུར་པ་སྟེ། དེ་ལ་ཕ་ཞེས་པ་ནི༌[^2097]སྤྲུལ་པའི་སྐུ་སྟེ། དེ་བཞིན་གཤེགས་པ་ནི༌[^2098]སེམས་ཅན་གྱི་དོན་དང་འདྲེན་པ་མཛད་དུ་ཟིན་གྱིས་ཀྱང་། སེམས་ཅན་སོ་སོའི་ལས་ཀྱི༌[^2099]དབང་གིས་དེ་བཞིན་གཤེགས་པ་ལ་མི་ཕྱོགས་པ་དང་། ནོར་སྣ་ཚོགས་མང་ཞེས་པ་ནི་རིན་པོ་ཆེ་སྣ་བདུན་ཏེ། འཕགས་པའི་ནོར་བདུན་དང་སྦྱར། མཛོད་དང་བང་བ་ནི་འདུས་མ་བྱས་ཀྱི་ཆོས་ཀྱི་མཛོད་དང་ལྡན་ཞེས་པའི་དོན་ཏོ།[^2100] །ཉོན་མོངས་པ་རྣམས་ཀྱི་དབང་དུ་གྱུར་པའི་ཕྱིར་བྲན་དང་འདྲའོ། །

[Block 2506]
ཐབས་མཁས་པས་སྤྱོད་པ་ནི་གཡོག་དང་འདྲའོ། །

[Block 2507]
སྨོན་ལམ་དང་སྟོབས་ལ་སོགས་པ་ནི་ལས་བྱེད་པའི་མི་དང་སྦྱར་རོ། །

[Block 2508]
མངོན་པར་ཤེས་པ་ལྔ་ནི་གླང་པོ་ཆེ་དང་རྟ་དང་སྦྱར། ཐེག་པ་རྣམ༌[^2101]ལྔ་ནི་ཤིང་རྟ་དང་སྦྱར། སྤྱོད་པ་བརྒྱད་ཁྲི་བཞི་སྟོང་ནི། བ་ལང༌[^2102]དང་ལུག་མང་པོ་དང་ལྡན་པ་དང་སྦྱར། དོན་དམ་པ་དང༌[^2103]ཀུན་རྫོབ་ཀྱི་བསྟན་པ་ནི་ཁ་འདུ་ཞིང་འཕེལ་བ་དང་སྦྱར་རོ། །

[Block 2509]
དེ་བཞིན་གཤེགས་པའི་བསྟན་པ་སྒྲོགས་པ་ནི་འཚོ་བ་མང་བ་ཞེས་སྦྱར་རོ། །

[Block 2510]
དེ་ནས་བཅོམ་ལྡན་འདས་མི་དབུལ་པོ་དེ་ཞེས་པ་ནས། དེར་ཕྱིན་པར་གྱུར་ཏེ་ཞེས་པའི་བར་དུ་ནི། ཐེག་པ་རྣམ་གསུམ་གྱི་སྤྱོད་པ་ནི་གྲོང་དང་གྲོང་ཁྱེར་ཞེས་པའི་དོན་ཏེ། དེ་ལ་ཆོས་བཤད་པ་དང་། རྫུ་འཕྲུལ་བསྟན་པའི་དོན་ནི་ལྗོངས་དང་རྒྱལ་པོའི་ཕོ་བྲང་དང་སྦྱར་རོ། །

[Block 2511]
ཇི་ལྟར་གནས་ཐམས་ཅད་དུ་འཁྱམས་ཀྱང༌[^2104]རྒྱལ་པོའི་ཕོ་བྲང་དུ་ཕྱིན་པ་བཞིན་བསྟན་པ་སྣ་ཚོགས་ལ་ཞུགས་ཀྱང་རིགས་མ་འགྱུར༌[^2105]ཏེ། དེ་བཞིན་གཤེགས་པའི་རིགས་ཀྱི་གནས་སུ་འཁོར་ཅིང་། ཡབ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་དང་ཕྲད་ཅེས་པའི་དོན་ཏོ། །

[Block 2512]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་མི་དབུལ་པོའི་ཕ་དེ་ཞེས་པ་ནས་གཞན་སུ་ལ་ཡང་མི་སྨྲ་བར། འདི་སྙམ་དུ་བདག་ནི་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆེན་པོ་ལ་ཕྱོགས་སུ་མི་བཏུབ་པའི་དཔེ་སྟེ། ལོ་ལྔ་བཅུ་ཞེས་པ་ནི་རྒྱུད་རྣམ་ལྔར་འཁོར་བའི་དོན་ཏོ། །

[Block 2513]
ནང་དུ་གདུང་བ་མ་གཏོགས་པར་གཞན་སུ་ལ་མ་སྨྲ་ཞེས་པ་ནི་ཐེག་པ་ཆེན་པོའི་དོན་འདི་འཁོར་མང་པོའི་ནང་དུ་མ་གསུངས་ཞེས་པའི་དོན་ཏོ། །

[Block 2514]
གདུང་བ་ཞེས་པ་ནི་འགྲོ་བ་རྣམས་ཐེག་པ་གཅིག་པུ་འདིའི་སྣོད་དུ་མ༌[^2106]གྱུར་པས་གདུང་བ་ཞེས་སྦྱར་རོ། །

[Block 2515]
མདོ་ལས་རྒས་ཤིང་འཁོགས༌[^2107]ཏེ་འདུག་ན་ཞེས་པ་ནས་འདི་ལ་སྤྱོད་པར་གྱུར་ན་ནི་བདག་མྱ་ངན་མེད་པར་སེམས་ན་ཞེན༌[^2108]པའི་བར་དུ་ནི། ཐེག་པ་ཆེན་པོ་ལ་གནས་པར༌[^2109]ཡུན་རིང་བ་དང་། སྤྱོད་པ་རྫོགས་པའི་ཕྱིར་རྒས་འཁོགས༌[^2110]ཞེས་པའི་དོན་ཏོ། །

[Block 2516]
བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཟད་མི་ཤེས་པའི་ཕྱིར་ནོར་ཟས་དང་བང་མཛོད་མང་ཞེས་པའི་དོན་ཏོ། །

[Block 2517]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་བཞུགས་ཀྱང་ད་རུང༌[^2111]ཉན་ཐོས་པ་རྣམས་ཀྱིས༌[^2112]སངས་རྒྱས་ཀྱི་གདུང་འཚོ་བའི་ཕྱིར་བུ་མེད་པ་ཞེས་པའི་དོན་ཏོ། །

[Block 2518]
སངས་རྒྱས་ནམ་ཞིག་མྱ་ངན་ལས་འདའ་བར་སྟོན་པ་ན། ཐེག་པ་ཆེན་པོའི་ནོར་རྫས་དབང་པོ་མ་སྨིན་པ་རྣམས་ལ་གཏད་དུ་མེད་པའི་ཕྱིར་ཐུགས་རྗེས་མྱ་ངན་དུ་དགོངས་པ་ཞེས་སྦྱར་རོ། །

[Block 2519]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་མི་དབུལ་པོ་དེ་ཞེས་པ་ནས་གང་ན་བ་དེར་མཆིས་ཏེ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་བུ་དེས་ཕ་མཐོང་མ་ཐག་ཏུ་སྐྲག་ནས་བྲོས་པ་དང་། ཕའི་སྒོ་དྲུང་དུ་ཕྱིན་པ་དང་ཞེས་པ་ལ་ཚོལ་ཞིང་སོང་སོང་ཞེས་པ་ནི་འབྱུང་བའི་དོན་ཚོལ་བའོ། །

[Block 2520]
ཆེད་དུ་བཙལ་བ་མ་ཡིན་པར་གནས་དེར་སོན་པ་ནི་ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་དུ་འགྱུར་བར༌[^2113]སྨིན་པའི་དུས་ལ་བྱའོ། །

[Block 2521]
ཕའི་གནས་དེར་ཕྱིན་ཞེས་བྱ་བ་ནི་ལུང་དང་རིགས་པའི་སྒོ་ནས་སྤྱོད་པ་ལ་ཞུགས་ཞེས་པའི་དོན་ཏོ། །

[Block 2522]
གནས་གང་ན་བ་དེར་ཕྱིན་ཞེས་པ་ནི་ཐེག་པ་ཆེན་པོའི་ཕྱོགས་ལ་བསྙེན༌[^2114]ཞེས་པའི་དོན་ཏོ། །

[Block 2523]
འགྲོན་བུ་དང་གསེར་དང་། འབྲུ་མཛོད་མང་དུ་ཡོད་ཅེས་པ་ནི་ཐེག་པ་ཆེན་པོ་རིན་པོ་ཆེ་ཐམས་ཅད་ཀྱི་འབྱུང་གནས་སུ་གྱུར་པ་ཉིད་ལ་བྱའོ། །

[Block 2524]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་མི་དབུལ་པོ་དེའི་ཕ༌[^2115]ཞེས་པ་ནས། བརྒྱན་པ༌[^2116]ལ་མཆི་སྟེ་ཞེས་པའི་བར་དུ་ནི་འདིས་ཕ་མཐོང་བ་བསྟན་པ་ལ་ཡང་ཕ་བདེ་བར་འདུག་པ་དང་འཁོར་མང་པོས་བསྐོར་བའོ། །

[Block 2525]
མཐོང་ཞེས་པ་ནི་རྒྱང་མ་ནས་མཐོང་ཞེས་པའི་དོན་ཏེ།[^2117] ཐེག་པ་ཆེན་པོའི་སྤྱོད་པ་ལ་ད་དུང་རིང་ཞེས་པའི་དོན་ཏོ། །
--- END BLOCKS ---
