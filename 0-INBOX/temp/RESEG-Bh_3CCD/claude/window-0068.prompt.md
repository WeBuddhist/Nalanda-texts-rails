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
[Block 2381]
སྒྲ་ཇི་བཞིན་པས་ནི་ཕྱིའི་སྤྲོས་པ་ཙམ་སྟོན་པར་བྱེད་པའི་ནུས་པ་ཡོད་ཀྱི་གཞན་ནི་མ་ཡིན་ནོ། །

[Block 2382]
ཤིན་ཏུ་སྤྲོས་པ་མེད་པའི་སྤྱོད་པ་ནི་རྫོགས་པའི་རིམ་པའི་ཡན་ལག་ཡིན་ཡང་སྒྲ་ཇི་བཞིན་པས་དེ་བསྒྲུབ་པར་བྱ་བ་མ་ཡིན་གྱི་འོན་ཀྱང་དེའི་མཚན་ཉིད་ཙམ་རྗོད་པར་བྱེད་པས་སྐྱོན་མེད་དོ། །

[Block 2383]
སྒྲ་ཇི་བཞིན་མ་ཡིན་པ་ནི་འཇིག་རྟེན་དང་བསྟན་བཅོས་ལས་ཕྱིར་གྱུར་པས་བསྐྱེད་པའི་རིམ་པ་ཙམ་ལ་ཡང་སྟོན་པར་བྱེད་པའི་ནུས་པ་མེད་ན་ཡང་། ཡན་ལག་ལྔ་དང་ལྡན་པའི་རྫོགས་པའི་རིམ་པ་ལ་ག་ལས་འགྱུར་ཏེ། བརྡ་ཙམ་སྟོན་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2384]
དེའི་ཕྱིར་ན་མཐའ་དྲུག་ལས་བཤད་པ་རྣམ་པ་བཞི་པོ་ཐ་དད་པ་ཁོ་ནའོ། །

[Block 2385 [HEADING]]
##### འཆད་པ་པོའི་རྒྱན། ^1-7-3-1-0

[Block 2386]
འཆད་པས་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིས་འཆད་པ་པོའི་རྒྱུན་བཤད་པ་ཡིན་ཏེ། གལ་ཏེ་འཆད་པ་པོས་གཞལ༌[^1557]བྱ་མ་ཤེས་ནས་སློབ་མ་རྣམས་ཀྱི་བསམ་པ་མ་ལོངས་ཤིང་བཤད་པར་བྱེད་ན། དེའི་ཚེ་ཐམས་ཅད་དཀྲུགས་པར་འགྱུར་རོ། །

[Block 2387]
སློབ་མའི་དབྱེ་བ་ཡོངས་སུ་ཤེས་པས་བཤད་པ་སྣ་ཚོགས་པ་བྱེད་པ་ལ་བརྩོན་པའི་འཆད་པ་པོ་ཡོད་ན། ཐམས་ཅད་མཛེས་པར་བྱེད་པས་འཆད་པ་པོའི་རྒྱན་ཡིན་ནོ། །

[Block 2388]
འདོད་པ་ནི་སྨོན་པ་སྟེ་སྲིད་པའི་དོན་དུ་ལུང་སྦྱར་རོ། །

[Block 2389]
གལ་ཏེ་འཆད་པ་པོས་བཤད་པར་འདོད་པ༌[^1558]དེའི་ཚེ་དབྱེ་བ་གཉིས་ཀྱིས་ཉན་དུ་གཞུག༌[^1559]པའི་ཕྱིར་བཤད་པར་བྱའོ། །

[Block 2390]
དེ་ལ་དབྱེ་བ་གཉིས་ནི་ཚོགས་པ་ལ་བཤད་པ་དང་། སློབ་མ་ལ་བཤད་པར་བསྟན་པའོ། །

[Block 2391]
དེ་ལ་ཚོགས་ཀྱི་ནང་དུ་གསང་བའི་དོན་གབ༌[^1560]པར་བྱས་ལ་བཤད་པ་གང་ཡིན་པ་དེ་ནི་ཚོགས་ལ་བཤད་པའོ། །

[Block 2392]
དབང་པོ་རྣོ་བའི་གང་ཟག་རྣམས་ལ་ཤིན་ཏུ་གསལ་བའི་དེ་ཁོ་ན་ཉིད་རབ་ཏུ་བསྟན་པ་ནི་སློབ་མ་ལ་བཤད་པའོ། །

[Block 2393 [HEADING]]
###### དང་པོ་ཚོགས་པ་ལ་བཤད་པ། ^1-7-3-1-1-0

[Block 2394]
དེ་ལ་དང་པོ་རྣམ་པ་ལྔ་སྟེ། ཇི་བཞིན་སྒྲ་ནི་སྒྲའི་རྒྱན་ནོ།[^1561] །

[Block 2395]
དགོངས་མིན་ནི་དོན་གྱི་རྒྱན་ནོ། །

[Block 2396]
དྲང་བའི་དོན་ནི་དོན་གྱི་རྒྱན་ནོ། །

[Block 2397]
ཡི་གེའི་དོན་ནི་སྒྲའི་རྒྱན་ནོ། །

[Block 2398]
[^1562]

[Block 2399]
དེ་ལྟར་ཡི་གེའི་དོན་དང་སྒྲ་ཇི་བཞིན་པ་སྒྲའི་རྒྱན་དག་དང་། དྲང་བའི་དོན་དང་དགོངས་པ་མ་ཡིན་པ་དང་། སྤྱིའི་དོན༌[^1563]རྣམས་ནི་དོན་གྱི་རྒྱན་ཏེ་ཚོགས་པ་ལ་བཤད་པ་ཡིན་ཏེ་བསྐྱེད་པའི་རིམ་པ་ཙམ་སྟོན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2400]
གལ་ཏེ་དབང་པོ་དམན་པས་རྟོགས་པར་བྱེད་པའི་དེ་ཁོ་ན་ཉིད་གསལ་བར་བཤད་པ་དགོངས་པ་མ་ཡིན་ནོ། །

[Block 2401]
[^1564]ཇི་ལྟར་ཚོགས་པ་ལ་བཤད་པར་འགྱུར། སྨྲས་པ། རྣམ་པར་དག་པ་ཙམ་སྟོན་པར་བྱེད་པས་སམ། རིགས་བརྒྱའི་དབྱེ་བས་ལུས་རྣམ་པར་དབེན་པ་སྟོན་པས་ན༌[^1565]སྐྱོན་མེད་དོ། །

[Block 2402]
གལ་ཏེ་རེས་འགའ་ཞིག་དགོངས་པ་མ་ཡིན་པས་རིམ་པ་ལྔའི་ནང་ནས་གང་ཡང་རུང་བ་སྟོན་པར་བྱེད་ན་དེའི་ཚེ་ཚོགས་པ་ལ་བཤད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2403]
གང་གི་ཚེ་བྱ་མཇུག་རིངས༌[^1566]འཕུར་བས་སྦྲུལ་དུ་མི་འགྱུར་རོ། །

[Block 2404 [HEADING]]
###### སློབ་མ་ལ་བཤད་པ། ^1-7-3-1-2-0

[Block 2405]
ཇི་བཞིན་མིན་སྒྲ་ནི་སྒྲའི་རྒྱན་ནོ། །

[Block 2406]
ངེས་དོན་ནི་དོན་གྱི་རྒྱན་ནོ། །

[Block 2407]
དགོངས་ཏེ་བཤད་པ་ནི་སྒྲའི་རྒྱན་ནོ། །

[Block 2408]
སྦས་པ་དང་མཐར་ཐུག་པ་དག་ནི་དོན་གྱི་རྒྱན་ཡིན་ཞེས་སློབ་མ་ལ་བཤད་པ་དབྱེ་བ་ལྔ་སྟེ། རྫོགས་པའི་རིམ་པ་བསྟན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2409]
བཤད་པའི་རྒྱུད་ཀྱི་རྗེས་འབྲངས་ནས། །ཞེས་པ་འདིས་ལུང་གི་ཚད་མ་བསྟན་ཏོ། །

[Block 2410]
དེ་ལྟར་མདོར་བསྡུས་ཏེ་འདུལ་བྱ༌[^1567]རྣམས་ལ་ནི་གང་ཟག་རྣམས་ལ་རིམ་པ་གཉིས་ལ་བརྟེན་ཏེ་སྔོན་དུ་བཤད་པའི་དབྱེ་བ་བདེ་བར་གཤེགས་པ་རྣམས་ཀྱིས་གསུངས་སོ། །

[Block 2411 [HEADING]]
##### ཉན་པ་པོའི་རྒྱན། ^1-7-3-2-0

[Block 2412]
ཉན་པ་པོའི་རྒྱན་བསྟན་པར་བྱ་བའི་ཕྱིར། རྣམ་པ་ཀུན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། །འཇིག་རྟེན་ནི་ངེས་གྱུར་པས། །ཞེས་པ་ལ། རིགས་སོ་སོར་ངེས་པ་ཅན་ནོ། །

[Block 2413]
དེ་བས་ན་ལྔ་ཡིན་ཏེ། བྱང་ཆུབ་སེམས་དཔའི་རིགས་ཅན་གཅིག་པུར་ཅིའི་ཕྱིར་མ་གསུངས་ཤེ་ན། རྣམ་པ་ཀུན་ཏུ་ཉན་འདོད་པའི། ཞེས་པས་ནི་ཐོས་པ་ལ་འཇུག་པ་བཏང་སྙོམས་བྱ་བར་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 2414]
བློ་ཡི་རྣམ་པ་དཔག་མེད་ཕྱིར། །ཞེས་པ་ནི་རིགས་སོ་སོར་ངེས་པའི་རྒྱུ་ཡིན་པས་སོ། །

[Block 2415]
ཨུཏྤ་ལ་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་མདོར་བསྟན་པའོ། །

[Block 2416]
རང་བཞིན་ཐ་དད་མིང་ཅན་དེ། །ཞེས་པ༌[^1568]དོན་དང་ལྡན་པའི་མིང་འཛིན་པའོ། །

[Block 2417 [VERSE]]
ཐམས་ཅད་མཁྱེན་པས་གསུངས་པ་ཡིན། །
ཞེས་པ་འདིས་རང་བཟོ་བཀག་པའོ། །
དེ་ནི་མ་ལུས་དོན་ཐོས་ནས། །

[Block 2418]
ཞེས་པ་ནི་རྒྱས་པར་བསྟན་པའོ། །

[Block 2419]
དོན་མ་ལུས་པ་ནི་གཞལ་བར་བྱ་བའི་དངོས་པོ་སློབ་དཔོན་གྱི་ཞལ་ནས་ཐོས་ཏེ། འཛིན་པ་ལ་ནི་རྣམ་པར་མཁས། །ཞེས་པ་ནི་ཕྱིན་ཅི་མ་ལོག་པར་འཛིན་པར་བྱེད་དོ། །

[Block 2420]
སྐད་ཅིག་གིས་ནི་བརྗེད༌[^1569]གྱུར་པ། །ཞེས་པ་ནི། དེ་ནས་ལངས་ཏེ་ཅང་མི་དྲན་པའོ། །
--- END BLOCKS ---
