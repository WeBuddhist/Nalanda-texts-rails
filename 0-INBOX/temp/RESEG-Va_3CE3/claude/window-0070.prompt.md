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
[Block 2451 [HEADING]]
##### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་པོ། ^1-2-7-47-0

[Block 2452]
བམ་པོ་ཉི་ཤུ༌[^1754]ལྔ་པ། དེ་ལྟ་བུའི་ཟབ་མོའི་གནས་ཐོས་ནས། བཅོམ་ལྡན་འདས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི༌[^1755]ཟབ་པོ༌[^1756]ཞེས་བྱ་བ་ལ་སོགས་པ་གསོལ་ཏེ། དཔེ་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 2453]
དཔེར་ན་མི་དེས། རྩ་བ་དང་། ཤུན་པ་དང་ཡལ་ག་དང་། ལོ་མ་དང་། མེ་ཏོག་དང་། འབྲས་བུ་འདོད་པར་གྱུར་ན། ཐོག་མར་དེ་དག་མི་དམིགས་པ་དེ་བཞིན་དུ། བྱང་ཆུབ་སེམས་དཔས་ཀྱང་ཆོས་ཐམས་ཅད༌[^1757]མི་དམིགས་སོ། །ཇི་ལྟར་ཕྱིས་མི་དེས་སྡོང་བུ་བསྐྱེད་ན། རྩ་བ་དང་ཤུན་པ་ལ་སོགས་པ་རྙེད་ནས་ཉེ་བར་སྤྱོད་པ་དེ་བཞིན་དུ། བསོད་ནམས་དང་། ཡེ་ཤེས་ཀྱི་ཚོགས་དུ་མ་བསྐྱེད་ན་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་ནས་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པ་དང་། བདེ་བ་ཉེ་བར་སྤྱོད་པར་བྱེད་པར་ཤེས་པར་བྱའོ། །

[Block 2454 [HEADING]]
##### དེ་བཞིན་གཤེགས་པར་གདགས་པ། ^1-2-7-48-0

[Block 2455]
རབ་འབྱོར་དེ་བཞིན་ཉིད་གང་གིས་དེ་བཞིན་གཤེགས་པར་གདགས་པ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་དུ་གཤེགས་པས་ན་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱའོ། །

[Block 2456]
བྱང་ཆུབ་སེམས་དཔའ་ཡང་དེ་བཞིན་ཉིད་དུ་གཤེགས་པ་ཡིན་ཏེ། དེ་བས་ན་དེ་བཞིན་གཤེགས་པ་ཉིད་དུ་བརྗོད་པར་བྱའོ། །

[Block 2457]
བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་དེ་བཞིན་ཉིད་འདི་ལ་གནས་ཏེ་ཞེས་བྱ་བ་འགྲེས་གཉིས་པ་ལ་དེ་བཞིན་ཉིད་ཁོང་དུ་ཆུད་ཅིང་རྟོགས་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ༌[^1758]སྟེ། དེ་བཞིན་ཉིད་འདི་ཡང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 2458]
དེའི་འོག༌[^1759]ཏུ་དེ་བཞིན་ཉིད་དང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པའི་ཕན་ཡོན་དང་བསོད་ནམས་འཕེལ་བ་ནི་གོ་སླའོ། །

[Block 2459]
བྱང་ཆུབ་སེམས་དཔའ་ཞུགས་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཀྱི་ལམ་ལ་གནས་པའོ། །

[Block 2460 [HEADING]]
##### རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་དངོས་པོ་མེད་པ། ^1-2-7-49-0

[Block 2461]
རབ་འབྱོར་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཅེས་བྱ་བ་ནི་དངོས་པོ་མེད་པས། མཚན་ཉིད་མེད་པ་ཞེས་བྱ་བ་ནི་དངོས་པོའི་ཆོས་ལས་འདས་པའི་ཕྱིར་དངོས་པོ་མེད་པའོ། །

[Block 2462]
རང་དང་སྤྱིའི་མཚན་ཉིད་དང་བྲལ་བའི་ཕྱིར་མཚན་ཉིད་མེད་པའོ། །

[Block 2463]
མིང་དང་མཚན་མ་ཐམས་ཅད་དང་བྲལ་བའི་ཕྱིར་མཚན་མ་མེད་པའོ། །

[Block 2464]
རྩོལ་བ་མེད་པའི་ཕྱིར་ལྷུན་གྱིས་གྲུབ་པའོ། །

[Block 2465]
འདུས་མ་བྱས་པའི་ཕྱིར་སྐྱེ་བ་མེད་པའོ། །

[Block 2466]
གནས་པ་མེད་པའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་འབྱུང་བ་མེད་པའོ། །

[Block 2467]
རབ་འབྱོར་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ནི་དངོས་པོ་མེད་པ་ལ་དམིགས་པའོ་ཞེས་བྱ་བ་ནི་དངོས་པོ་མེད་པ་ལས་བརྩམས་ནས་འཇུག་ཅེས་བྱ་བའི་ཐ་ཚིག་སྟེ། དམིགས་པའི་རྐྱེན་ནི་མ་ཡིན་ནོ། །

[Block 2468]
དྲན་པས་དབང་བསྒྱུར་བ་ཞེས་བྱ་བ་ནི་སྔོན་གྱི་རྒྱུའི་དབང་གིས་བརྗོད་ཀྱི་དེའི་ཚེ་ནི་མ་ཡིན་ནོ། །

[Block 2469 [HEADING]]
##### འདུས་པ་ལས་བྱུང་བའི་ངོ་བོ་ཉིད་མེད་པ། ^1-2-7-50-0

[Block 2470]
རབ་འབྱོར་འདུས་པ་ལས་བྱུང་བའི་ངོ་བོ་ཉིད་མེད་ཅེས་བྱ་བ་ནི་གཟུགས་དང་ཚོར་བ་ལ་སོགས་པ་ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་དེ། རྐྱེན་གཞན་གྱི་དབང་ལས་བྱུང་བའི་ཕྱིར་འདུས་པ་ལས་བྱུང༌[^1760]ཞེས་བྱ་སྟེ། གཞན་གྱི་དབང་བྱ་བའི་ཕྱིར་དེ་ལྟ་བུའི་ངོ་བོ་ཉིད་ཀྱི༌[^1761]མིང་དུ་འགྱུར་རོ། །

[Block 2471]
གང་ལ་འདུས་པ་ལས་བྱུང་བའི་ངོ་བོ་ཉིད་མེད་པ་སྟེ༌[^1762]དངོས་པོ་མེད་པའོ་ཞེས་བྱ་བ་ནི་ཆོས་གང་གཞན་ལ་རག་ལས་པ་ཡིན་གྱི། ངོ་བོ་ཉིད་ཅེས་བྱ་བ་མ་ཡིན་པ་དེ་དངོས་པོ་མེད་པ་ཞེས་ཏེ།[^1763] རི་བོང་གི་རྭ་ལ་སོགས་པ་ལྟར་གཏན་མེད་པའི་ཕྱིར་མེད་པ་ནི་མ་ཡིན་གྱི་དངོས་པོ་ཡོད་པའི་ཆོས་ལས་བཟློག་པའི་ཕྱིར་དངོས་པོ་མེད་པའོ། །

[Block 2472]
དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཅེས་བྱ་བ་ནི་གཟུགས་ལ་སོགས་པ་ཀུན་བརྟགས་པའི་ཆོས་རྣམས་ལ་དངོས་པོ་མེད་པ་ཞེས་བྱའོ། །

[Block 2473]
དེ་ལ་བཟློག་པའི་ངོ་བོ་ཉིད་ཀྱང་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཅེས་བྱའོ། །

[Block 2474 [HEADING]]
##### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད། ^1-2-7-51-0

[Block 2475]
དེའི་འོག་ཏུ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པ་དང་ཐབས་མཁས་པ་དག་བསྟན་ཏོ། །

[Block 2476]
དེ་ལ་བཅོམ་ལྡན་འདས་ཆོས་རྣམས་ཆོས༌[^1764]ཉིད་དང་བྲལ་བ་ལགས་སམ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཆོས་ཐམས་ཅད་དང་བྲལ་བ་ཡིན་ན་དེ་ལྟ་ན་ནི་ཤེས་པར་བྱ་བ་དང་ཤེས་པར་བྱེད་པ་ཡང་མེད་པས་འདི་ནི༌[^1765]ཤེས་པར་བྱས་སོ་ཞེས་བྱ་བར་བརྗོད་དུ་མི་རུང་ངོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2477]
དངོས་པོས་ཀྱང་དངོས་པོ་འཚལ་བར་མི་རུང་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པས་ཀུན་བརྟགས་པ་ཤེས་པར་མི་རུང་སྟེ། མེད་པའི་ཕྱིར་ཇི་ལྟར་སྒྱུ་མའི་གླང་པོ་ཆེས་སྒྱུ་མའི་གླང་པོ་ཆེའི་རྗེས་ལྟ་བུའོ། །

[Block 2478]
དངོས་པོ་མེད་པས་ཀྱང་དངོས་པོ་མེད་པ༌[^1766]ཤེས་པར་མི་རུང་སྟེ། ཇི་ལྟར་ནམ་མཁས་ནམ་མཁའ་ལྟ་བུའོ། །

[Block 2479]
དངོས་པོས་ཀྱང་དངོས་པོ་མེད་པ་ཤེས་པར་མི་རུང་སྟེ། ཇི་ལྟར་སྒྱུ་མའི་མིས་ནམ་མཁའ་ལྟ་བུའོ། །

[Block 2480]
དངོས་པོ་མེད་པས་ཀྱང་དངོས་པོ་ཤེས་པར་མི་རུང་སྟེ། ཇི་ལྟར་ནམ་མཁས་སྒྱུ་མའི་མི་བཞིན་ཏེ་འདི་ནི་དངོས་པོ་ཡོད་པ་དང་དངོས་པོ་མེད་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 2481 [HEADING]]
##### ཀུན་རྫོབ་དང་དོན་དམ་པའི་དེ་བཞིན་ཉིད། ^1-2-7-52-0

[Block 2482]
བཅོམ་ལྡན་འདས་ཅི་ལགས་འཇིག་རྟེན་གྱི་ཀུན་རྫོབ་ཀྱང་གཞན་ཞིག་ལ། དོན་དམ་པ་ཡང་གཞན་ལགས་སམ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་གྱི་ཀུན་རྫོབ་དངོས་པོ་མེད་པའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་དོན་དམ་པ་ཞུས་པའོ། །

[Block 2483]
འཇིག་རྟེན་ཀུན་རྫོབ་ཀྱི་དེ་བཞིན་ཉིད༌[^1767]གང་ཡིན་པ་དེ་ཉིད་དོན་དམ་པའི་དེ་བཞིན་ཉིད་ཡིན་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་གྱི་ཀུན་རྫོབ་ཅེས་བྱ་བ་གཟུགས་ལ་སོགས་པའི་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་གང་ཡིན་པ་དེ་ཉིད་དོན་དམ་པའི་དེ་བཞིན་ཉིད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2484 [HEADING]]
##### སངས་རྒྱས་ཀྱི་མཚན་ཉིད་དང་ངེས་པའི་ཚིག། ^1-2-7-53-0

[Block 2485]
རབ་འབྱོར་ཡང་དག་པའི་དོན་ནི་སངས་རྒྱས་ཞེས་བྱ་སྟེ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་ངོ་བོ་ཉིད་ཀྱི་མཚན་ཉིད་གསུངས་པ་སྟེ་ཡང་དག་པའི་དོན་དེ་བཞིན་ཉིད་ཆོས་ཀྱི་སྐུ་ལ་སངས་རྒྱས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2486]
དེས་ཡང་དག་པའི་དོན་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པས་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམ་པ་གསུམ་གྱིས་ངེས་པའི་ཚིག་གསུངས་པ་སྟེ། བཅོམ་ལྡན་འདས་ཀྱིས་ནི་དགྲ་བཅོམ་པའི་ལམ་གྱི་ཡེ་ཤེས་ཀྱིས་ཡང་དག་པའི་ཆོས་མྱ་ངན་ལས་འདས་པ་ཉིད་སངས་རྒྱས་པར་འགྱུར་བ་དང་། དེའི་འོག་ཏུ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཡེ་ཤེས་ཀྱིས་ཡང་དག་པའི་དོན་སྟོང་པ་དང་ཞི་བ་ལ་སོགས་པའི་དོན་དུ་རྟོགས་པ་དང་། དེའི་རྗེས་ལ་ཐོབ་པ་དང༌[^1768]ཐམས་ཅད་མཁྱེན་པ་ཉིད་པའི༌[^1769]ཡེ་ཤེས་ཀྱིས༌[^1770]ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་རྗེས་སུ་རྟོགས་པར་འགྱུར་ཏེ། དེ་ལྟར་ཡང་དག་པའི་ཆོས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པ་དང་། ཡང་དག་པའི་དོན་རབ་ཏུ་རྟོགས་པ་དང་། ཆོས་ཐམས་ཅད་ཇི་ལྟ་བ་བཞིན་དུ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པའི་ཕྱིར་སངས་རྒྱས་ཞེས་བྱའོ། །

[Block 2487 [HEADING]]
##### བྱང་ཆུབ་རྣམ་པ་གསུམ་དུ་བསྟན་པ། ^1-2-7-54-0

[Block 2488]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་ཅེས་བགྱི་བ་དེ་གང་གི་ཚིག་བླ་དགས་ལགས་སོ༌[^1771]ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱང་རྣམ་པ་གསུམ་དུ་བསྟན་ཏེ་ངོ་བོ་ཉིད་དང་མཚན་ཉིད་དང་ངེས་པའི་ཚིག་གིས་སོ། །

[Block 2489 [HEADING]]
###### ངོ་བོ་ཉིད། ^1-2-7-54-1-0

[Block 2490]
དེ་ལ་ངོ་བོ་ཉིད་རྣམ་པ་གཉིས་ཏེ། ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་དང་། ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་དོ། །
--- END BLOCKS ---
