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
[Block 2626]
བདུན་མཐོ་བ་ཞེས་བྱ་བ་ནི་ཕྱག་དང་ཞབས་ཀྱི་བོལ་གཉིས་དང་། དཔུང་མགོ་གཉིས་དང་ལྟག་པ་སྟེ། དེ་དག་ཤས་རྒྱས་པའི་ཕྱིར་རོ། །

[Block 2627]
སྔོན་གྱི་ལས་ནི་བཟའ་བ་དང་། བཏུང་བ་དང་། བལྡགས་པ༌[^1873]དང་། བཅའ་བ་གྱ་ནོམ་པ་རྣམས་ཞེས་བྱ་བ་ནི་གྱ་ནོམ་པ་བྱིན་པས་ཕྱག་དང་། ཞབས་འཇམ་ཞིང་གཞོན་ཤ༌[^1874]ཆགས་པར་འགྱུར་རོ།[^1875] །བཟའ་བའི་དངོས་པོ་མང་དུ་བྱིན་པས་ནི་བདུན་མཐོ་བར་གྱུར་ཏོ། །

[Block 2628]
ཡང་ན་ཞབས་གཉིས་ཀྱིས༌[^1876]གཤེགས་ནས། ཕྱག་གཉིས་ཀྱིས་བྱིན་པའི་ཕྱིར་རོ། །

[Block 2629]
ཡང་ན་ཕྱག་གཉིས་ཀྱིས་བྱིན་ནས་སེམས་ཅན་རྣམས་བདག་གི་ཞབས་ལ་གཞོལ་བར་བྱས་པའི་ཕྱིར་ཕྱག་དང་ཞབས་གཉིས་དེ་ལྟ་བུར་གྱུར༌[^1877]ཏོ། །

[Block 2630]
བདུན་མཐོ་བ་ནི་ཁམས་བདུན་ཚིམ་པར་བྱས་པ་དང་མཐུན་པའི་ཕྱིར་རོ། །

[Block 2631]
ལས་གཅིག་གིས་མཚན་གཉིས་འབྱུང་བར་ཇི་ལྟར་ཤེས་པར་བྱ་ཞེ་ན། ལས་གཅིག་ཡིན་དུ་ཟིན་ཀྱང་ཤིན་ཏུ་ཆེར་བྱས་ཤིང་བསྩགས༌[^1878]པས་མཚན་གཉིས་སམ་གསུམ་ཡང་འགྲུབ་པར་འགྱུར་ཞེས་བཤད་དོ། །

[Block 2632]
སོར་མོ་རིང་བ་ཞེས་བྱ་བ་ནི་ཧ་ཅང་རིང་བ་དང་། ཧ་ཅང་ཐུང་བ་དང་། ཧ་ཅང་སྦོམ་པ་དང་། ཧ་ཅང་ཕྲ་བ་དང་ཡོ་བ་ལ་སོགས་པ་སོར་མོའི་སྐྱོན་རྣམས་སྤངས་ཤིང་སྐྱོན་མེད་ལ། ཕྱག་གི་མཐིལ་དང་འཚམ་པ། ཚད་དང་ལྡན་པ་སོར་མོ་མཐར་གྱིས་ཤས༌[^1879]རྒྱས་ཏེ། རྩེ་མོ་ཕྲ་བ་གང་ཡིན་པ་དེ་ལ་སོར་མོ་རིང་བ་ཞེས་བྱའོ། །

[Block 2633]
རྟིང་པའི་སྐྱོན་ཐམས་ཅད་དང་བྲལ་བ། ཚད་དང་ལྡན་པ། ཞབས་དང་འཚམ་པའི་རྟིང་པ་དང་ལྡན་པའི་ཕྱིར། རྟིང་པ་ཡངས་པ་སྟེ།

[Block 2634]
དེ་ལ་ཞབས་ཀྱི་མཐིལ་ཐམས་ཅད་ལ་ཆ་བཞིར་བྱས་པ་ལས།

[Block 2635]
ཆ་གསུམ་ནི་ཞབས། ཆ་གཅིག་ནི་རྟིང་པར་གྱུར་ན་ཚད་དང་ལྡན་པ་ཞེས་བྱའོ། །

[Block 2636]
ཆུ་ཞེང་གབ་པ་ཕུན་སུམ་ཚོགས་པ་དང་ཕང་མཐོ་བའི་ཕྱིར་སྐུ་ཆེ་བའོ། །

[Block 2637]
མི་གཞན་ལྟར་ཕྲག་པ་དང་། རྐེད་པ་དང་པུས་མོ་རྣམས་ལས་གང་ཡང་རུང་བ་འམ། མདུན་དང་རྒྱབ་དང་གློ༌[^1880]གྱེ་གུ་དང་ཡ་ཡོ་མེད་པའི་ཕྱིར་སྐུ་དྲང་བའོ། །

[Block 2638]
སོར་མོ་རིང་བ་དང་། རྟིང་པ་ཡངས་པ་ཞེས་བྱ་བ་འདི་ལ་རིང་བ་དང་ཡངས་པའི་སྒྲ་ནི་རན་པ་དང་རྐྱེན་དུ་བབ་པའི་ཚིག་ཡིན་གྱི། ཧ་ཅང་རིང་བ་དང་ཧ་ཅང་ཡངས་པའི་སྒྲ༌[^1881]ནི་མ་ཡིན་ནོ། །

[Block 2639]
སྔོན་གྱི་ལས་བཤད་པ་ཡང་། གསད་པ་ལས་ཐར་པར་བྱས་པ་དང་། བཟའ་བ་དང་བཏུང་བ་ལ་སོགས་པ་བྱིན་པས་སྲོག་གི་རིམ་གྲོ་བྱས་པ་དང་། སྲོག་གཅོད་པ་སྤངས་པ་ཀུན་ཏུ་བསྟེན་པས༌[^1882]ཞེས་བྱ་བ་འདི་ལ་ཡང་གསད་པར་གྱུར་པའི༌[^1883]མི་རྣམས་ཚེ་ཐུང་བ་ལས་ཐར་པར་བྱས་པས་ཚེ་ཐ་མལ་པར་གནས་ཀྱི། གློ་བུར་དུ་ཚེ་རིང་བར་འགྱུར་བ༌[^1884]ནི་མ་ཡིན་ནོ། །

[Block 2640]
དེ་བཞིན་དུ་འཚོ་བའི་ཡོ་བྱད་རྣམས་བྱིན་པས་ཀྱང་ཚེ་ཐུང་བ་མེད་པར་བྱས་པ་ཡིན་གྱི་གློ་བུར་དུ་ཚེ་རིང་དུ་བྱས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2641]
དེ་བཞིན་དུ་འདིར་ཡང་རྟིང་པ་དང་། སོར་མོ་དག་ཐུང་བ་མེད་པ་ཉིད་རིང་བ་ཡིན་གྱི། ལྷག་པར་རིང་བ་ནི་མ་ཡིན་ནོ། །

[Block 2642]
ཁྲུ་བདུན་དུ་འཕགས་པར་མཐོ་བ་ཞེས་བྱ་བ་ནི་མི་ཐ་མལ་པའི་ལུས་པས་འཕགས་པར་མཐོ་བ་སྟེ། སྐུ་ཐ་མལ་པའི་ཚད་ལ་བྱའོ། །

[Block 2643]
སྤྱི་གཙུག་བལྟར༌[^1885]མི་མཐོང་བའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱི་གཟུགས་ཀྱི་སྐུའི་ཚད་ངེས་པར་བྱ་མི་ནུས་སོ། །

[Block 2644]
སྲོག་གཅོད་པ་སྤངས་པས་ལུས་ཀྱི་ལས་མི་དྲང་བ་མེད་པའི་ཕྱིར་སྐུ་དྲང་པོ་དང་མཐུན་ནོ། །

[Block 2645]
ཞབས་འབར་འབུར་མེད་པ་ཞེས་བྱ་བ་ནི་པུས་མོའི་ཚིགས་དང་། ལོང་མོའི་ཚིགས་ཀྱི་རུས་པ་མཐོ་བ༌[^1886]ལ་འབར་འབུར་ཅན་ཞེས་བྱ་སྟེ། དེ་མེད་ཅིང་ཤིན་ཏུ༌[^1887]མངོན་ལ་རབ་ཏུ་ནུབ་པ་གང་ཡིན་པ་དེ་ལ་ཞབས་འབར་འབུར་མེད་པ་ཞེས་བྱའོ། །

[Block 2646]
གཞན་དག་གི་ནི་རུས་པ་དེ་གཉིས་ཆེ་བས་རྐང་པ་དང་། བྱིན་པ་མི་སྡུག་པ་ཡིན་ནོ། །

[Block 2647]
མི་མཉེན་པས་འགྲོ་ན་མི་བདེ་སྟེ་འགྲོས་མི་སྡུག་པར༌[^1888]འགྱུར་རོ། །

[Block 2648]
བཅོམ་ལྡན་འདས་ཀྱི༌[^1889]ཚིགས་མི༌[^1890]མངོན་པས་བྱིན་པ་མཛེས་སོ། །

[Block 2649]
མཉེན་པས་འགྲོས་སྡུག་པ་ཡིན་ནོ། །

[Block 2650]
གཞན་དག་ན་རེ་མི་ཕལ་རྣམས་ཀྱི་ལོང་བུའི༌[^1891]རུས་པ་ནི་རྐང་པའི་རྒྱབ་ལོགས་སུ་འབྱུང་སྟེ། དེ་བས་ན་དེ་དག་གི་རྐང་པ་གཟེར་བཏབ་པ་འདྲ་ལ། མི་མཉེན་པས་ཅི་བདེར༌[^1892]བསྒྱུར་དུ་མི་རུང་ལ་འགྲོ་བ་ན་ཡང་རྐང་པའི་མཐིལ་མི་སྣང་ངོ་ཞེས་ཟེར་རོ། །

[Block 2651]
སྐྱེས་བུ་ཆེན་པོ་རྣམས་ཀྱི་ལོང་མོའི་རུས་པ་ནི་ཞབས་ཀྱི་གོང་བས་མཐོ་བའི་ཕྱོགས་སུ་འབྱུང་ངོ་། །དེ་དག་གི་སྐུ་ཡང་རོ་སྨད་འབའ་ཞིག་གཡོའི། རོ་སྟོད་གཡོ་བར་མི་མངོན་ནོ། །

[Block 2652]
ཞབས་ཀྱང་བདེ་བླག་ཏུ་བསྒྱུར་དུ་རུང་ལ། མདུན་རྒྱབ་དང་། གཡས་གཡོས་སུ༌[^1893]འདུག་སྟེ་བལྟས་ཀྱང་ཞབས་ཀྱི་མཐིལ་སྣང་ཞིང་འགྲོས་སྡུག་གོ། །

[Block 2653]
སྐུའི་སྤུ་གྱེན་དུ་ཕྱོགས་པ་ཞེས་བྱ་བ་ནི་སྐྱེས་བུ་ཆེན་པོ་རྣམས་ཀྱི་སྐུའི་སྤུ་རྣམས་སྤུའི་ཁུང་བུ་ནས་སྐྱེ་བ་ན། ཞལ་བཟང་པོ་ལ་གྱེན་དུ་ལྟ་བ་འདྲ་བར་རྩེ་མོ༌[^1894]གྱེན་དུ་ལྟ་ཞིང་སྐྱེ་བའོ། །

[Block 2654]
སྔོན་གྱི་ལས་ཀྱང་དགེ་བའི་ཆོས་བླངས་པ་རྣམས་ཇི་ལྟར་གོང་ནས་གོང་དུ་འཕེལ་བར་འགྱུར་བ་དེ་བཞིན་དུ་ཞབས་ཀྱི་ཕྱོགས་མཐོ་བ་དང་། སྤུ་ཁ་གྱེན་དུ་ལྟ་ཞིང་མཐོན་པོར་འབྱུང་བ་དང༌[^1895]མཐུན་ནོ། །

[Block 2655]
བྱིན་པ་རི་དགས་ཨེ་ན་ཡའི༌[^1896]ལྟ་བུ་ཞེས་བྱ་བ་ནི་རི་དགས་ཨེ་ན༌[^1897]ཡའི་བྱིན་པ་དང་འདྲ་བ་གང་ཡིན་པ་དེ་ལ༌[^1898]རི་དགས་ཨེ་ན༌[^1899]ཡའི་ལྟ་བུ་ཞེས་བྱའོ། །

[Block 2656]
མི་ཕལ་གྱི་བྱིན་པ་ནི་ཕྱོགས་གཅིག་ཏུ་ཤ་རློ་བོར་གྱུར་པའམ། ཡོ༌[^1900]བའམ། ཧ་ཅང་སྦོམ་པའམ། ཧ་ཅང་རིང་བའམ་ཐུང་བ་ཡིན་གྱི། སྐྱེས་བུ་ཆེན་པོ་རྣམས་ཀྱི་ནི་ཤ་མཁྲེགས་ལ་བྱིན་གྱིས་ཕྲ་ཞིང་དབྱིབས་སྙོམས་པ་དང་། ཤིན་ཏུ་ཟླུམ་ཞིང་ཆུ་ཞེང་གབ་པ་སྟེ། སོར་བཅོ་བརྒྱད་ཙམ་གྱི་ཕྱོགས་ན་ཡོད་དོ། །

[Block 2657]
སྔོན་གྱི་ལས་ཀྱང་བཟོའི་ལས་དང་རིག་པའི་གནས་རྣམས་གུས་པར་བྱས་ཤིང་བྱིན་པས་སློབ་མ་དེ་རྣམས་འཕེལ་ཞིང་རྒྱས་པར་གྱུར་པ་དང་། ཡོ་བྱད་རྣམས་བྱིན་པས་དེ་དག་སྟོབས་དང་ལྡན་པར་གྱུར༌[^1901]ཏེ། དེ་དང་མཐུན་པར་ཤ་སྐྱེས་པའི་ཕྱིར་བྱིན་པ་རི་དགས་ཨེ་ན༌[^1902]ཡའི་ལྟ་བུར་གྱུར་ཏོ། །

[Block 2658]
དེ་ནི་མྱུར་དུ་འཛིན་པའི་སྔ་ལྟས་སོ་ཞེས་བྱ་བ་ནི་སྐྱེས་བུ་ཆེན་པོ་དེ་སངས་རྒྱས་ཀྱིས་གསུངས་པ་ཐམས་ཅད་མྱུར་དུ་འཛིན་ཅིང་། དེ་བཞིན་གཤེགས་པ་ཡང་སེམས་ཅན་ཐམས་ཅད་ཀྱིས་ཞུས་པའི་རྒྱུན་རྣམས་སྐད་ཅིག་གཅིག་གིས་འཛིན་ཏོ། །

[Block 2659]
ཕྱག་སྦོམ་ཞིང་རིང་བ་ཞེས་བྱ་བ་ལ། སྦོམ་པ་ནི་སྦོམ་ལག་ཆེ་བའི་ཕྱིར་རོ། །

[Block 2660]
རིང་བ་ནི་པུས་མོར་སླེབས་པའི་ཕྱིར་ཁྲུན་རིང་བའོ། །

[Block 2661]
སྔོན་གྱི་ལས་ཀྱང་ཕྱག་བརྐྱང༌[^1903]སྟེ་རིང་དུ་བྱས་ནས་གཞན་ལ་སྦྱིན་པ་བྱིན་པ་དང་། སྦྱིན་པར་བྱ་བའི་ཆོས་རྒྱ་ཆེ་བའི་ཕྱིར་མཐུན་ནོ། །

[Block 2662]
མདོམས་ཀྱི༌[^1904]སྦ་བ་སྦུབས་སུ་ནུབ་པ༌[^1905]ཞེས་བྱ་བ་ལ། མདོམས༌[^1906]ཀྱི་སྦ་བ་ནི་མདོམས༌[^1907]སུ་སྦ་བ་ཡིན་པས་མདོམས༌[^1908]ཀྱི་སྦ་བ་སྟེ། མདོམས༌[^1909]ཀྱི་སྦ་བ་སྦུབས་སུ་ནུབ་ཅིང་། མི་མངོན་པ་གང་ཡིན་པ་དེ་ལ་མདོམས༌[^1910]ཀྱི་སྦ་བ་སྦུབས་སུ་ནུབ་པ་ཞེས་བྱ་སྟེ། གསེར་གྱི་པདྨའི་སྙིང་པོ་སྦུབས་སུ་ནུབ་པ་འདྲ་བར་མདོམས༌[^1911]ཀྱི་སྦ་བའི་ཕྱོགས་སྦུབས་ཀྱི་ནང་དུ་མི་མངོན་པར་གྱུར་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2663]
སྔོན་གྱི་ལས་ཀྱང་མཛའ་བཤེས་དང་གཉེན་འདབ་ལ་སོགས་པ་འདུམ་པར་བྱས་པ་དང་། མ་ཕྱེ་བའི་ཕྱིར་སྦུབས་དང་སྦ་བ་དག་དེ་ལྟར་མཐུན་པར་གྱུར་ཏོ། །

[Block 2664]
གསང་ཐུབ་པར་བྱས་པས་སྦ་བའི་ཕྱོགས་མི་མངོན་པར་གྱུར་ཏེ་མཐུན་ནོ། །

[Block 2665]
མདོག་གསེར་འདྲ་བ་ཞེས་བྱ་བ་འདིས་ནི་སྐུ་མཁྲེགས་ཤིང་སྣུམ་ལ་ཁ་དོག་རབ་ཏུ་གསལ་བར་བསྟན་ཏོ། །
--- END BLOCKS ---
