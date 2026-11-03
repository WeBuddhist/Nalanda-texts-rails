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
[Block 2346]
དེ་ལ༌[^1714]རྡུལ་ཕྲ་བར་ཏུ་བཅོམ་ཡང་རུང་། བློས་རོ་ལ་སོགས་པའི་ཆོས་བསལ་ཀྱང་རུང་གཟུགས་ཀྱི་རང་བཞིན་གྱི་བློ་འཇུག་པ་ཉིད་དེ། ཚོར་བ་ལ་སོགས་པ་ཡང་དེ་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 2347]
དེ་ནི་དོན་དམ་པར་ཡོད་པའི་ཕྱིར་དོན་དམ་པའི་བདེན་པ་ཞེས་བྱའོ། །

[Block 2348]
སྔོན་གྱི་སློབ་དཔོན་རྣམས༌[^1715]ན་རེ། ཇི་ལྟར་འཇིག་རྟེན་ལས་འདས་པའི་ཤེས་པའམ། དེའི་རྗེས་ལ་ཐོབ་པ་འཇིག་རྟེན་པས་འཛིན་པ་དེ་ལྟར་ནི་དོན་དམ་པའི་བདེན་པ་ཡིན་ནོ། །

[Block 2349]
ཇི་ལྟར་གཞན་གྱིས་འཛིན་པ་དེ་ལྟར་ནི༌[^1716]ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2350]
བདེན་པ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 2351 [HEADING]]
#### མངོན་པར་རྟོགས་པའི་རིམ་པ། ^3-1-3-0

[Block 2352]
ཇི་ལྟར་ན་དེ་དག་མཐོང་བར་འགྱུར་བ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དང་པོ་འཇུག་པ་ལས་བརྩམས་ཏེ་བརྗོད་པར་བྱའོ། །

[Block 2353 [HEADING]]
##### ཚུལ་གནས་ཐོས་བསམ་བསྒོམ་པ། ^3-1-3-1-0

[Block 2354 [VERSE]]
ཚུལ་གནས་ཐོས་དང་བསམ་གཏན་པ། །
བསྒོམ་པ་ལ་ནི་རབ་ཏུ་སྦྱོར། །

[Block 2355]
བདེན་པ་རྣམས་མཐོང་བར་འདོད་པ་ནི་དང་པོ་ཁོ་ནར་ཚུལ་ཁྲིམས་སྲུང་བར་བྱེད་དོ། །

[Block 2356]
དེའི་འོག་ཏུ་བདེན་པ་མཐོང་བ་དང་མཐུན་པའི་ཐོས་པ་འཛིན་པའམ། དོན་ཉན་པར་བྱེད་དོ། །

[Block 2357]
ཐོས་ནས་ཕྱིན་ཅི་མ་ལོག་པར་སེམས་པར་བྱེད་དོ། །

[Block 2358]
བསམས་ནས་ཏིང་ངེ་འཛིན་སྒོམ་པ་ལ་རབ་ཏུ་སྦྱོར་བར་བྱེད་དོ། །

[Block 2359]
[^1717]དེ་ཐོས་པ་ལས་བྱུང་བའི་ཤེས་རབ་ལ་བརྟེན་ནས་བསམ་པ༌[^1718]ལས་བྱུང་བ་སྐྱེའོ། །

[Block 2360]
བསམ་པ༌[^1719]ལས་བྱུང་བ་ལ་བརྟེན་ནས་བསྒོམ་པ༌[^1720]ལས་བྱུང་བ༌[^1721]སྐྱེའོ། །ཤེས་རབ་འདི་དག་གི་མཚན་ཉིད་ཅི་ཞེ་ན།

[Block 2361 [HEADING]]
##### ཐོས་སོགས་ལས་བྱུང་བའི་བློ། ^3-1-3-2-0

[Block 2362 [VERSE]]
ཐོས་སོགས་ལས་བྱུང་བློ་རྣམས་ནི། །
མིང་དང་གཉི་ག་དོན་ཡུལ་ཅན། །

[Block 2363]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་ཐོས་པ་ལས་བྱུང་བའི་ཤེས་རབ་ནི་མིང་ལ་དམིགས་པ་ཡིན་ལ། བསམ་པ་ལས་བྱུང་བ་ནི་མིང་དང་དོན་ལ་དམིགས་པ་ཡིན་ཏེ། རེས་འགའ་ནི་ཡི་གེས་དོན་འདྲེན་པར་བྱེད་དོ། །

[Block 2364]
བསྒོམ༌[^1722]པ་ལས་བྱུང་བ་ནི་དོན་ལ་དམིགས་པ་ཁོ་ན་ཡིན་ཏེ། དེ་ནི་ཡི་གེ་ལ་མི་ལྟོས་པར་དོན་ལ་འཇུག་གོ། །

[Block 2365]
དཔེར་ན་སྟོང་རྐྱལ་ལེགས་པར་མ་ལོབས་པ་ཆུའི་ནང་དུ་འཇུ་བར་བྱ་བ་མི་གཏོང་བ་ཁོ་ན་ཡིན་ལ། ཅུང་ཟད་ལོབས་པ་ནི་རེས་འགའ་ནི་གཏོང་རེས་འགའ་ནི་འཇུ་བར་བྱེད་དོ། །

[Block 2366]
ལེགས་པར་ལོབས་པ་ནི་འཇུ་བར་བྱ་བ་ལ་མི་ལྟོས་པར་རྒལ་བ་ལྟ་བུ་སྟེ་འདི་ནི་དཔེ་ཡིན་ནོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 2367]
གཞན་དག་ན་རེ་རྟོག་པ་འདི་ལ་ནི་མིང་ལ་དམིགས་པ་གང་ཡིན་པ་དེ་ནི་ཐོས་པ་ལས་བྱུང་བ་ཡིན་པར་འགྱུར་ལ། དོན་ལ་དམིགས་པ་གང་ཡིན་པ་དེ་ནི་བསྒོམ་པ༌[^1723]ལས་བྱུང་བ་ཡིན་པར་འགྱུར་བས་བསམ་པ༌[^1724]ལས་བྱུང་བའི་ཤེས་རབ་འགྲུབ་པར་མི་འགྱུར་གྱི། ཐོས་པ་ལས་བྱུང་བའི་ཤེས་རབ་ནི་ཡིད་ཆེས་པའི་ལུང་ཚད་མ་ཉིད་ལས་སྐྱེས་པའི་ངེས་པ་ཡིན་ནོ། །

[Block 2368]
བསམ་པ་ལས་བྱུང་བ་ནི༌[^1725]རིགས་པས་ངེས་པར་བརྟགས་པ་ལ༌[^1726]སྐྱེས་པ་ཡིན་ནོ། །

[Block 2369]
བསྒོམ་པ༌[^1727]ལས་བྱུང་བའི་ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ནི་འདི་དག་གི་མཚན་ཉིད་ཁ་ན་མ་ཐོ་བ་མེད་པར་སྣང་ངོ་ཞེས་ཟེར་རོ། །

[Block 2370 [HEADING]]
##### བསྒོམ་པ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་བ། ^3-1-3-3-0

[Block 2371]
དེ་ལྟར་བསྒོམ་པ་ལ་རབ་ཏུ་བརྩོན་པ་དེ་ཇི་ལྟར་ན་སྒོམ་པ༌[^1728]རྫོགས་པར་འགྱུར་ཞེ་ན། བསྲིངས་གཉིས་ལྡན་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་འདུ་འཛི་དང་མི་དགེ་བའི་རྣམ་པར་རྟོག་པ་ཐག༌[^1729]བསྲིངས་པའི་ཕྱིར་ལུས་དང་སེམས་དག་གིས་བསྲིངས་པ་ཡིན་ན་རྫོགས་པར་འགྱུར་རོ། །

[Block 2372]
འོ་ན་བསྲིངས་པ་དེ་གཉིས་སུ་ལ་སླ་ཞེ་ན། འདོད་པ་ཆུང་བ་དང་། ཆོག་ཤེས་པ་ལ་སླའི། ཆོག་མི་ཤེས་པ་དང་། འདོད་ཆེན་ཅན་ལ་མ་ཡིན་ནོ། །

[Block 2373 [HEADING]]
###### ཆོག་མི་ཤེས་པ་དང་འདོད་ཆེན་ཅན། ^3-1-3-3-1-0

[Block 2374]
ཆོག་མི་ཤེས་པ་འདི་ནི་གང་ཞིག་ཡིན་ནོ། །

[Block 2375]
[^1730]འདོད་ཆེན་ཅན་ནི་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 2376 [VERSE]]
རྙེད་ལ་ཡང་སྲེད་ཆོག་མི་ཤེས། །
མ་རྙེད་ལ་འདོད་འདོད་ཆེན་ཅན། །

[Block 2377]
ཆོས་མངོན་པ་པ་རྣམས་ན་རེ་ཆོས་གོས་ལ་སོགས་པ་གྱ་ནོམ་པ་རྙེད་པ་ལ་ཡང་དང་ཡང་དུ་འདོད་པ་ནི་ཆོག་མི་ཤེས་པ་ཡིན་ལ། མ་རྙེད་པ་དག་ལ་དེ་འདོད་པ་ནི་འདོད་ཆེན་ཅན་ཡིན་ནོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 2378]
ཡང་དང་ཡང་དུ་འདོད་པ་དེ་ཡང་མ་རྙེད་པ་ཁོ་ན་ལ་ཡིན་གྱི་རྙེད་པ་ལ་ནི་མ་ཡིན་པ་མ་ཡིན་ནམ། འདི་གཉིས་ལ་ཁྱད་པར༌[^1731]ཅི་ཞིག་ཡོད་དེ་འདི་ནི་བརྗོད་པར་བྱ་དགོས་སོ། །

[Block 2379]
འདི་ལྟར་ནི་རུང་སྟེ། གྱ་ནོམ་པ་མ་ཡིན་པ་དང་། མང་པོ་མ་ཡིན་པ་རྙེད་པས་ཡིད་མི་བདེ་བ༌[^1732]ནི་ཆོག་མི་ཤེས་པ་ཡིན་ནོ། །

[Block 2380]
གྱ་ནོམ་པ་དང་མང་པོ་མ་རྙེད་པས༌[^1733]འདོད་པ་ནི་འདོད་ཆེན་ཅན་ཡིན་ནོ། །

[Block 2381]
བཟློག་པ་དེ་ཡི༌[^1734]གཉེན་པོ་དག །ཆོག་མི་ཤེས་པ་དང་། འདོད་ཆེན་ཅན་ལས་བཟློག་པ་ནི་དེ་དག་གི་གཉེན་པོ་ཆོག་ཤེས་པ་དང་། འདོད་ཆེན་ཆུང་བ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2382]
དེ་གཉིས་ཁམས་གསུམ་གཏོགས་དྲི་མེད། །དེའི་གཉེན་པོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཁམས་གསུམ་པ་དག་དང་། མི་ལྡན་པ་དག་ཀྱང་ཡིན་ནོ། །

[Block 2383]
ཆོག་མི་ཤེས་པ་དང་། འདོད་ཆེན་ཅན་ནི་འདོད་པ་ན་སྤྱོད་པ་དག་ཁོ་ན་ཡིན་ནོ། །

[Block 2384]
འདོད་ཆེན་ཆུང་བ་དང་ཆོག་ཤེས་པ་འདི་གཉིས་ཀྱི་རང་བཞིན་ཅི་ཞེ་ན། མ་ཆགས་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་དག་ནི་མ་ཆགས་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 2385 [HEADING]]
###### འཕགས་པའི་རིགས་བཞི། ^3-1-3-3-2-0
--- END BLOCKS ---
