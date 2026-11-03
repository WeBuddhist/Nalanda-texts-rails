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
[Block 2521]
བརྙས་པ་དང་བསྐྱིས་པ་དག་མི་སྦྱིན་པར་སེམས་པའོ་ཞེས་བྱ་བ་ལ། བརྣོགས་པ་ནི་འདིར་བརྐུས་པའོ། །

[Block 2522]
དེ་བས་ན་དེས་སྦྱིན་པར་མི་འགྱུར་བ་ཞེས་བྱ་བ་མི་སྦྱིན་པའི་ཀུན་ཏུ་རྟོག་པ་ལ་སྦྱོར་བ་ཉིད་རིགས་པ་ཡིན་ཏེ། སྣོན་པ་ལ་ཡང་བརྙས་པ་དང་བསྐྱིས་པ་དག་ལ་སྦོམ་པོ་སྟེ། མེ་སྦྱིན་པའི་ཀུན་ཏུ་རྟོག་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིར་རྣམ་པར་གཞག་པར་བྱའོ། །

[Block 2523]
གཞན་གྱི་དོན་དུ་བྱིན་པ་འགོད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡོན་བདག་གིས་དགེ་འདུན་ལ་མཆོད་རྟེན་ལ་སོགས་པའི་དོན་དུ་རྫས་དགེ་སློང་གི༌[^1715]ལག་ཏུ་བྱིན་པ་དེ་རྣམས་ཀྱིས་འགོད་པ་ལ་སྦོམ་པོ་སྟེ། འདིར་དོན་མི་ཤེས་པ་ཉིད་དགེ་འདུན་གྱི་བདག་ཉིད་ཀྱི་བདག་པོ་ལ་རྒྱུ་ཡིན་ཏེ། གང་གི་ཕྱིར་ཕམ་པ་དང་འདྲ་བའི་སྦོམ་པོའོ། །

[Block 2524]
གང་གི་ཕྱིར་དགེ་སློང་ནད་པས་དགེ་འདུན་ལ་རྫས་ཕུལ་བ་དགེ་འདུན་གྱི༌[^1716]འདི་ཤེས་པ་མ་ཡིན་ནོ། །

[Block 2525]
དགེ་འདུན་ལས་ཀྱང་ཉེ་གནས་དེ་དག་གིས༌[^1717]བརྐུ་བ་འདི་བྱས་པ་སྟེ་སྦྱིན་པ་པོ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2526]
དེ་བས་ན་བརྐུས་པ་ལ་ཕམ་པ་བསྐྱེད་པའོ། །

[Block 2527]
ཡོངས་སུ་མ་བཟུང་བ་ཡོངས་སུ་བཟུང་བར་འདུ་ཤེས་པའོ་ཞེས་བྱ་བ་ནི་དངོས་པོ་གང་སུས་ཀྱང་ཡོངས་སུ་མ་བཟུང་བ་ལ་འདི་ཡོངས་སུ་བཟུང་ངོ་སྙམ་པའི་འདུ་ཤེས་ཅན་གྱིས་བླངས་པ་ལ་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2528]
ཟན་དྲོན་དང་འབྲས་ཆང༌[^1718]དང་ཕྱེ་དང་ཉ་ཤ་དང་ཁུར་བ་ལ་སོགས་པའི་བསོད་སྙོམ་པ༌[^1719]གཞི་མེད་པ་ནོད་པའོ་ཞེས་བྱ་བ་ནི་གཞི་མེད་པ་ཞེས་བྱ་བ་མི་དབང་བའོ། །

[Block 2529]
ཟན་དྲོན་ལ་སོགས་པའི་བསོད་སྙོམས་ཐོབ་ཅིང་བཟུང་བ་ལ་སྦོམ་པོའོ། །

[Block 2530]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་བསོད་སྙོམས་འབྲས་ཆན་གཞི་མེད་པ་བླངས་ནས་དེ་འགྱོད་པ་སྐྱེས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཕམ་པར་མི་འགྱུར་ཏེ་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2531]
བསོད་སྙོམས་ལ་འབྲས་ཆན་ལ་ཇི་ལྟ་བ་བཞིན་དུ་བསོད་སྙོམས་ཕྱི་བ་སོགས༌[^1720]པ་ཇི་ལྟ་བ་མ་ཡིན་པ་ན་ན་ཀར་གྱུར་པའི་ནོར་ལེན་པ་ལ་མངོན་པར་ཞེན་པ་དེ་ལྟ་བུའི་ཁ་ཟས་ལ་ཞེས་བྱ་བ་འདི་འདིར་དམ་པ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་འདི་ལ་སྦོམ་པོའི་ལྟུང་བ་རྣམ་པར་ཤེས་ཏེ། ཕམ་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་མཐོང་བ་ཡིན་ནོ། །

[Block 2532]
མ་ཆོག་པ་ཉིད་ཀྱི་ཕྱིར་རིན་ཐང་བརྩི་བར་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་མ་གསུངས་པའི་ཕྱིར་གཞན༌[^1721]གྱིས་ཀྱང་མ་ཡིན་ནོ། །

[Block 2533]
མ་གསུངས་པ་ཉིད་ཀྱིས་མ་བླངས་པ་གཞན་གྱི་དོན་དུ་རྐུ་བ་མི་བསྐྱེད་པས་མ་ཐོབ་ཅིང་འདི་བཟུང་བ་ལ་གང་ཞིག་གཞི་མེད་པ་ཐོབ་པ་ནི་འདིར་རྐུ་བའོ། །

[Block 2534]
གཞན་གྱིས་བླངས་པར་མི་ཤེས་པ་ནི་གཞི་མེད་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རང་གི་དོན་ནམ་གཞན་གྱི་དོན་ལ་བསོད་སྙོམས་སམ་རྙེད་པ་གཞན་གྱིས་དེའི་དོན་དུ་བླངས་པ་ཉིད་ཡོད་པ་ལ་གལ་ཏེ་མི་ཤེས་ན་གཞན་གྱིས༌[^1722]བཟུང་བ་ཉིད་སླར་རྙེད་པར་གྱུར་པ་ལེན་ན་དེར་གཞི་མེད་པར་ཤེས་པར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2535]
མ་བཅོལ་བས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ལེན་པ་དེའི་དོན་གྱིས་འདིར་བཅོལ་བར་མ་གྱུར་པ་དེས་འདི་ལ་གལ་ཏེ་ཅུང་ཟད་ཐོབ་ཅིང་བཟུང་བ་ཡིན་ན༌[^1723]དེ་ལ་དེར་གཞི་མེད་པ་མ་ཡིན་ནོ། །

[Block 2536]
ལེན་པ་ཉིད་དེ་ལ་མི་འགྱུར་ན་ཅིའི་ཕྱིར་འདི་ལ་གཞི་མེད་པ་ཉིད་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2537]
མགྲོན་དུ་མ་བོས་པར་ཟན་ཟ་ན་ཉེས་བྱས་སོ༌[^1724]ཞེས་བྱ་བ་ནི་འདིར་རྙེད་པ་ནི་རྣམ་པ་གཉིས་ཏེ། བརྒྱ་ལ་བདག་པོས་ཤེས་ཏེ་འདི་བདག་གིས་མགྲོན་དུ་ནི་མ་བོས་མོད་ཀྱི་འོན་ཀྱང་སྦྱིན་ནོ་སྙམ་པ་དང་། མི་ཤེས་པས་སྦྱིན་པར་བྱེད་པའོ། །

[Block 2538]
སྔར་གྱི་ལ་མེད་པ་སྟེ། རྐུ་བའི་སྦྱོར་བ་ལ་ཉེས་བྱས་ཉིད་དོ། །

[Block 2539]
ཕྱི་མ་ལ་ནི་ཤིན་ཏུ་དྲང་བ་སྟེ། འདིར་དགའ་བས་བསོད་སྙོམས་བླངས་པ་ལས་མངོན་པར་ཞེན་པའོ། །

[Block 2540]
དེ་ལྟར་ན་ནི་འདིར་འཇིག་རྟེན་པ་ལ་རྐུ་བའི་བློ་མེད་པ་ཉིད་དེ་དེ་བས་ན་ཉེས་བྱས་སུ་རྣམ་པར་ཤེས་པའོ། །

[Block 2541]
རྐུ་བའི་ཆེད་དུ་འགྲོ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་གི་སྒྲས་ནི་ཉེས་བྱས་ཞེས་བྱ་བ་རྗེས་སུ་དྲང་བའི་དོན་དུའོ། །

[Block 2542]
སྔར་བླངས་པ་ལས་ཞེས་བྱ་བ་གང་ཞིག་བརྗོད་པ་དེར་འདི་ཁོངས་སུ་བསྡུ་བ་མ་ཡིན་ཏེ། དེ་བས་ན་མདོ་ཕྱི་མ་ལ་ཡན་ལག་ཏུ་གཏོགས་པ་མདོ་འདི་རིག་པར་བྱའོ། །

[Block 2543]
དེ་བས་ན༌[^1725]གྲོས་བྱེད་པ་ཐ་དད་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འགྲོ་བ་འདི་ལས་གྲོས་བྱེད་པར་གྱུར་པ་ངག་གི༌[^1726]ལས་སམ་ལུས་ཀྱི་བྱ་བའི་བདག་ཉིད་ཅན་གང་ཡིན་པ་དེ་ལ་མི་འགྲོ་བ་ལས་ཐ་དད་པ་ཉིད་མ་ཡིན་ཏེ། ཉེས་བྱས་འདི་ཉིད་ལ་དེ་ཁོངས་སུ་གཏོགས་པ་སྟེ། ཉེས་བྱས་གཉིས་པ་ནི་མ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 2544]
ཀུན་དུ་བཟུང་བ་མ་ཡིན་ནམ་ཞེས་ལེགས་པར་སོ་སོར་བརྟག་པར་བྱ་སྟེ་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འགྱོད་པ་དང་གཞན་གྱི་ཚིག་ལ་གླགས་གཅད་པའི༌[^1727]དོན་དུ་འདི་བཏགས༌[^1728]པའོ། །

[Block 2545]
དེ་ལྟར་ལེགས་པར་སོ་སོར་བརྟག་པར༌[^1729]བྱས་ནས་བླང་བར་བྱའོ། །

[Block 2546]
ཇི་ལྟར་ཀུན་དུ་བཟུང་བ་མ་ཡིན་པ་འདི་ཞེས་བྱ་བའི་བརྟན་པ་ངེས་པར་འགྱུར་རོ། །

[Block 2547]
ལུས་བསྙལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལུས་སྒྱེལ་ཅིང་བསྙལ་བ་ནི་གྲགས་པ་ལས་དགོས་པའི་དོན་དུའོ། །

[Block 2548]
བརྡུང་བ་དང་བརྡེགས་པ༌[^1730]ལ་སོགས་པ་གཞན་རྣམ་པར་འཁྲུགས་པར༌[^1731]གྱུར་པས་འདི་ལྟ་བུ་བསྙལ་བར་མི་བྱའོ། །

[Block 2549]
འབྲས་བུའི་མདུན་དུ་དགེ་སློང་གིས་བདག་ཉིད་དོར་བ་ལ་སྨྲ་བ༌[^1732]པ་གང་ཡིན་པའོ། །

[Block 2550]
སླར་དགེ་སློང་གི་ལུས་འགྱུར་བ་རྣམ་པ་དེ་ལྟ་བུ་མི་བྱའོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 2551]
ཚང་གཞིག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བྱེའུ་དང་ཕུག་རོན་ལ་སོགས་པའི་རྟེན་ནི་ཚང་ངོ་། །འདི་ལ་སྐུར་པ་གདབ་པ་ནི་དགེ་སློང་གི་གནས་སུ་སྒོ་ང་མེད་པ་ལ་སོགས་པ་གསལ་བའི་ཆོ་ག་ལ་སོགས་པ་རིག་པར་བྱའོ། །

[Block 2552]
མ་གནས་པ་དེར་ཆོས་གོས་ཀྱི་ཆ་མི་བླང་ངོ་ཞེས་བྱ་བ་ལ། གང་དུ་གནས་པ་ལ་རྙེད་པ་དེ་འབྱུང་བ་དེ་ལས་གཞན་དུ་ལོ་གཅིག་གི་ཆོས་གོས་རྙེད་པ་ལ་ཡང་མི་བླང་ངོ་། །འདིར་གཞུང་ནི་དགེ་སློང་གིས་དབྱར་གཞན་དུ་གནས་ལ། གཞན་དུ་དབྱར་གྱི་སོ་སོར༌[^1733]ཆ་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བའོ། །

[Block 2553]
སོ་སོའི་ཆ་ནི་སྐལ་བའོ། །

[Block 2554]
འདིར་ལོ་གཅིག་གི་ཚིག་ནི་དཔེ་ཡིན་ནོ། །

[Block 2555]
གཞན་དུ་ཡང་མི་ཐོབ་པ་འདི་བཀག་པའོ། །

[Block 2556]
ཆོམ་རྐུན་པ་ལས་སྦྱིན་བདག་གི་སེམས་ཀྱིས༌[^1734]ལེན་པ་ལ་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཆོམ་རྐུན་པ་དེའི་དྲུང་ནས་བླངས་པ༌[^1735]གང་ཡིན་པ་དེ་ལ་འདི་ནི་སྦྱིན་བདག་སྙམ་པའི༌[^1736]སེམས་ཀྱིས་ལེན་ན་དེ་ལ་ཉེས་པ་མེད་དོ། །

[Block 2557]
ཇི་ལྟར་གཞན་ལས༌[^1737]བླངས་པ་ལ་ཉེས་པ་མེད་པ་དེ་བཞིན་དུ་འདི་ལའོ། །

[Block 2558]
གང་གི་ཕྱིར་འདིས་བརྐུས་པ་དེ་ཉིད་ཀྱིས་འདི་འབྲེལ་པའོ། །

[Block 2559]
ནོར་འདི་ལ་འདི་ནི་བདག་པོ་སྟེ་དེ་ཉིད་ཀྱིས་འདི་གནང་བ་ཞེས་བྱ་བ་འདི་ལྟར་ཡོངས་སུ་མ་དག་པའི་སེམས་ཀྱིས་བླངས་པ་ལ་ལྟུང་བ་དང་བཅས་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2560]
དེ་བས་ན་སྦྱིན་པ་པོའི་སེམས་ཀྱིས་ཞེས་བྱ་བ་འདི་ནི་བྱེ་བྲག་གོ། །
--- END BLOCKS ---
