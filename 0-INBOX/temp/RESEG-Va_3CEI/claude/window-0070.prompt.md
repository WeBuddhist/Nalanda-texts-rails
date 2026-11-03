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
[Block 2451]
མདོ་ལས།

[Block 2452]
གང་དག་འཁོར་གྱི་དབུས་སུ་ཆོས་སྟོན་ཅིང་། །ཞེས་པ་ནས། དེ་ལ་ཁྱོད་ཀྱིས་མདོ་སྡེ་འདི༌[^2044]རབ༌[^2045]སྒྲོགས། །ཞེས་པའི་བར་དུ་ནི་མདོ་སྡེ་འདི་ཚོལ་བ་དང་རིམ་གྲོར་བྱེད་པ་རྣམ་པ༌[^2046]གཉིས་ལ་གཞན་གྱི༌[^2047]བསྟན་པ་ཐམས་ཅད་སྤངས་ཏེ། ཐེག་པ་ཆེན་པོའི་མདོ་སྡེ་འབའ་ཞིག་ཚོལ་བའི་ཕྱིར་ཚོལ་བ་བསྟན་ཏོ། །

[Block 2453]
མདོ་ལས།

[Block 2454]
ཇི་ལྟར་དེ་བཞིན་གཤེགས་པའི་གདུང་འཛིན་པ། །ཞེས་པ་ནས། དེ་དག་མདུན་དུ་མདོ་སྡེ་མཆོག་འདི་སྨྲོས།[^2048] །ཞེས་པའི༌[^2049]བར་དུ་ནི་མདོ་སྡེ་འདི་ལ་རིམ་གྲོ་བསྐྱེད་པ་དང་། བཤད་པར་འོས་པ་རྣམས་ཀྱི་མཚན་ཉིད་ཀྱི་བསྡུ་བ་བསྟན་ཏོ།། །།

[Block 2455 [HEADING]]
### དད་པའི་ལེའུ། ^4-4-0

[Block 2456]
འདི་མན་ཆད་དད་པའི་ལེའུ་བསྟན་ཏེ། གོང་དུ་དྲང་བ་དང་ངེས་པའི་ཚུལ་རྟོགས་པར༌[^2050]བྱ་བའི་ཕྱིར་དཔེས་དོན་མཚོན་པས་དབང་པོ་རྣོ་བ་འཕགས་པ་ཤཱ་རིའི་བུ་ལྟ་བུ་དང་། དབང་པོ་བར་མ་འཕགས་པ་བཞི་པོ་ཡང་དཔེ་དེ༌[^2051]ཉིད་ཀྱིས་དོན་གོ་བར་གྱུར་པས་ཟབ་མོ་ཉིད་ལ་མོས་པ་སྐྱེས་པའི་ཕྱིར་དད་པའི་ལེའུ་བསྟན་ཏོ། །

[Block 2457]
འཕགས་པའི་ཉན་ཐོས་པ༌[^2052]རྣམས་སྤྱོད་ཡུལ་དམ་པའི་མཐར་མ་ཕྱིན་པར་ཕྱིན་པ་ཙམ་དུ་སེམས་ཤིང་ཐེག་པ་ཆེན་པོ་བ་དང་ཁྱད་པར་མེད་པ་ཙམ་དུ་བསྙེམས་པ༌[^2053]དེའི་དོན་དུ་སྤྲང་པོ་དང་འདྲ་བར་བསྟན་པའི་ཕྱིར་འདིའི༌[^2054]ནང་ནས་སྤྲང་པོའི་དཔེ་བསྟན་ཏོ། །

[Block 2458]
དད་པ་ཞེས་པ་ནི་ཆོས་ཇི་བཞིན་པར་བཟོད་པ་སེམས་རྣམ་པར་དག་པའི་མཚན་ཉིད་དོ། །

[Block 2459 [HEADING]]
#### དགའ་བར་གྱུར་པ། ^4-4-1-0

[Block 2460 [HEADING]]
##### དགའ་བའི་མཚན་ཉིད། ^4-4-1-1-0

[Block 2461]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་རབ་འབྱོར་ཞེས་པ་ནས་ཤིན་ཏུ་དགའ་བར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་འཕགས་པ་དེ་བཞིན༌[^2055]དགའ་བར་གྱུར་པ་དང་། འཕགས་པ་དེ་བཞིན༌[^2056]བྱས་པ་གཟོ་བས་དྲིན་བསབ་པ་སྟེ། དེ་ལ་དང་པོས་དགའ་བའི་མཚན་ཉིད་བསྟན་པ་དང་། གུས་པའི་མཚན་ཉིད༌[^2057]བསྟན་པ་སྟེ་འདི་ནི་དང་པོའོ། །

[Block 2462]
ཚེ་དང་ལྡན་པ་ཞེས་པ་ནི་འཇིག་རྟེན་པ་ལུས་རིང་དུ་འཚོ་བའི་ཚེ་དང་འཕགས་པ་རྣམས་ཡེ་ཤེས་ཀྱི་སྲོག་གིས་འཚོ་བའི་ཚེ་གཉི་ག་དང་ལྡན་པས་ཚེ་དང་ལྡན་པ་ཞེས་བྱའོ། །

[Block 2463]
འཕགས་པ་གཞན་ནི་རུས་ལས་བཏགས་པ་དང་། ཆུང་ངུ་ལས་དགའ་བ༌[^2058]ལྟས་བཟང་པོ་ལས་བཏགས་པ་སྟེ། ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 2464]
སྔར་དཔེ་ལས་དོན་རྟོགས་པར༌[^2059]གྱུར་ཅིང་བླ་ན་མེད་པའི་ལུང་བསྟན་པ་ཐོས་པས་ཤིན་ཏུ་དགའ་བར་གྱུར་པའོ། །

[Block 2465 [HEADING]]
##### གུས་པའི་མཚན་ཉིད། ^4-4-1-2-0

[Block 2466]
མདོ་ལས་དེའི་ཚེ་སྟན་ལས་ལངས་ཏེ་ཞེས་པ་ནས་བཅོམ་ལྡན་འདས་ལ་འདི་སྐད་ཅེས་གསོལ་ཏོ་ཞེས་པའི་བར་དུ་ནི་གུས་པའི་ཚུལ་བསྟན་ཏེ། ཚུལ་དེ་ཡང་རྣམ་པ་དགུར་དབྱེའོ། །

[Block 2467]
སྟན༌[^2060]ལས་ལངས་པ་ནི་ཐེག་པ་རྣམ་གཉིས་ལས་འཕགས་ཤིང་སེམས་ཆེན་པོ་བསྐྱེད་པའི་དོན་ཏོ། །

[Block 2468]
གོས་ཚགས་བཅོས་ཞེས་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པས་བརྒྱན་ཞེས་པའི་དོན་ཏོ། །

[Block 2469]
ཕྲག་པ་གཅིག་ཏུ་གཟར་ཞེས་པ་ནི་ཐེག་པ་རྣམ་གཅིག་ལ་ཞུགས་ཤིང་བཀྲ་ཤིས་པའི་ཚུལ་སྟོན་པའོ། །

[Block 2470]
པུས་མོ་གཡས་པའི་ལྷ་ང་ས་ལ་བཙུགས་ཞེས་པ་ནི་ཐེག་པ་རྣམ་གཉིས་འཛིན་པའི་སེམས་ཐུལ་ཞེས་པའི་དོན་ཏོ། །

[Block 2471]
སེམས་གཅིག་ཏུ་བྱས་པ་ནི༌[^2061]ཐེག་པ་ཆེན་པོ་གཅིག་པོ་ཚོལ་གྱི༌[^2062]གཞན་མི་སེམས་པའི་དོན་ཏོ། །

[Block 2472]
ཐལ་མོ་སྦྱར་ཞེས་པ་ནི་སེམས་སངས་རྒྱས་ལ་འདུད་པ་དྲང་བ་དང་ངེས་པའི་དོན་བསྟན་པར་མོས་པའི་དོན་དང་། ལུས་དང་ངག་དང་ཡིད་གསུམ་དགའ་བར་དམིགས་པའི་དོན་ཏོ། །

[Block 2473]
མངོན་དུ་ལྟ་ཞིང་ཞེས་པ་ནི། ལུང༌[^2063]དང་གཞུང་གི་ཚུལ་རྟོགས་པར་འདོད་ཅེས་པའི་དོན་ཏོ། །

[Block 2474]
གསོལ་ཏོ་ཞེས་པ་ནི་དད་པའི་མཚན་ཉིད་བསྟན་ཏོ། །

[Block 2475 [HEADING]]
#### བྱས་པ་གཟོ་བས་དྲིན་བསབ་པ། ^4-4-2-0

[Block 2476 [HEADING]]
##### ཚིག་ལྷུག་པས་གསོལ་བ། ^4-4-2-1-0

[Block 2477 [HEADING]]
###### ཆོས་ལས་གླེང་བ། ^4-4-2-1-1-0

[Block 2478]
མདོ་ལས་བཅོམ་ལྡན་འདས་བདག་ཅག་རྒས༌[^2064]ཞེས་པ་ནས༌[^2065]བརྩོན་འགྲུས་བརྩམས་པའི་རྔོ་མི་ཐོགས་ཀྱི༌[^2066]ཞེས་པའི་བར་དུ་ནི། འཕགས་པ་བཞི་པོས་སླར་གསོལ་པ་སྟེ། སྔར་ནི་ཚིག་ལྷུག་པས་གསོལ། དེའི་འོག་ཏུ་ནི༌[^2067]ཚིགས་སུ་བཅད་པས་གསོལ། ཚིག་ལྷུག་པ་ལ་ཡང་རྣམ་པ་གསུམ་སྟེ། ཆོས་ལས་གླེང་བ་དང་། དཔེས་གླེང་བ་དང་། གཉི་ག་བསྡུས་ཏེ་གླེང་བའོ། །

[Block 2479]
དེ་ཡང་སྔོན་ཆོས་འདི་ཐོས་པས་མ་སྔངས་ཏེ་དེ་མངོན་སུམ༌[^2068]དུ་ཆུད་པའོ། །

[Block 2480]
དེ་ཡང་སྔར་ནི་བསྡུས་ཏེ་བསྟན། ཕྱིས་ནི་རྒྱས་པར་བསྟན་ཏོ། །

[Block 2481]
གསོལ་བ་ལ་ཡང་དགེ་འདུན་གྱི་ནང་ན་གྲལ་མཐོ་བ་དང་། ན་སོ་རྒན་པ་དང་། བྱང་ཆུབ་ཐོབ་བཞིན་པ་ཙམ་དུ་སེམས་པ་དང་། ཡང་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཆེན་པོ་ཚོལ་བར་མི་སེམས་པའོ། །

[Block 2482]
མདོ་ལས་ནམ་བཅོམ་ལྡན་འདས་ཀྱིས་ཆོས་སྟོན་ཅིང་ཞེས་པ་ནས། བདག་ཅག་གིས་མོས་པ་མ་བསྐྱེད་དོ་ཞེས་པའི་བར་དུ་ནི། སྔར་ཆོས་ཀྱི་དོན་གླེང་།[^2069] འོག་ཏུ་ནི་དགོངས་པའི་དོན་བསྟན་ཏེ། འདི་ནི་དང་པོ་དང་སྦྱར་རོ། །

[Block 2483]
འཕགས་པ་ཉན་ཐོས་པ་རྣམས་རང་གི་སྤྱོད་པ་བསྒྲུབ༌[^2070]ཅིང་སྔོན་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2071]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བཤད་པ་ན་སྟོང་པ་ཉིད་དང་། མཚན་མ་མེད་པ་དང་། སྨོན་པ་མེད་པ་ཉིད་ལ་སེམས་མི་འཇོག །ཐེག་པ་ཆེན་པོའི་ཆོས་བྱང་ཆུབ་ཀྱི་ཆོས་རྣམས་ལ་མི་སེམས་སོ། །

[Block 2484]
སྔོན་བཅོམ་ལྡན་འདས་ཀྱིས་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས༌[^2072]རྣམས་སྟོན་པའང་བདག་ཅག་ལུས་དང་ཡན་ལག་བྲོ་འཚལ་བར་གྱུར་ཞེས་སྨྲས་པ་ཡིན་ཏེ། སྟོང་པ་ནི་བདག་མེད་པའི་སྤྱོད་ཡུལ་ལོ། །

[Block 2485]
མཚན་མ་མེད་པ་ནི་འགོག་པའི་སྤྱོད་ཡུལ་ལོ། །

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
--- END BLOCKS ---
