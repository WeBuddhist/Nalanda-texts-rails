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
[Block 491]
ཚིག་བཞི་པ་ལ། གཟུགས་ནི་གཟུགས་ལ་མི་དམིགས། གཟུགས་ནི་ཚོར་བ་ལ་མི་དམིགས་ཞེས་བྱ་བ་ལ་སོགས་པས་རང་གི་དངོས་པོ་དང་། གཞན་གྱི་དངོས་པོ་ལ་བཙལ་ན་ཆོས་ཐམས་ཅད་མི་དམིགས་པར་བསྟན་པ་སྟེ། འདིས་ནི་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་རྣམ་པ༌[^310]ཐམས་ཅད་དུ་ཞེས་བྱ་བ་བཤད་པ་ཡིན་ནོ། །

[Block 492 [HEADING]]
###### གློ་བུར་དུ་མིང་དུ་བཏགས་པ། ^1-1-7-2-5-0

[Block 493]
ཚིག་ལྔ་པ་ལ་འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བ་འདི་ནི་གློ་བུར་དུ་མིང་དུ་བཏགས་པ་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་སེམས་དཔའ་ནི་དོན་དམ་པ་སྟོང་པ་ཉིད་ཀྱི་རང་བཞིན་ཡིན་ན་ཀུན་རྫོབ་ཏུ་དེ་ལ་ཐ་སྙད་དུ་བྱ་བའི་ཕྱིར། བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བའི་མིང་གློ་བུར་དུ་བཏགས་པ་སྟེ། གློ་བུར་ཞེས་པ༌[^311]ནི་ངོ་བོ་ཉིད་དུ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 494]
འདི་ལྟར་ཆོས་ཐམས་ཅད་ཀྱི་མིང་ལྟར༌[^312]ཕྱོགས་བཅུ་གང་ནས་ཀྱང་མི་འོང་གང་དུ་ཡང་མི་འགྲོ་ཞེས་བྱ་བས་ནི་ཡོད་པ་མ་ཡིན་པ་ཉིད་སྟོན་ཏོ། །

[Block 495]
ཡང་དག་པར༌[^313]སྐྱེ་བའི་དུས་ན་ཡང་གང་ནས་ཀྱང་མི་འོང་ལ། འགག་པའི་དུས་ན་ཡང་གང་དུ་ཡང་མི་འགྲོའོ། །

[Block 496]
བྱང་ཆུབ་སེམས་དཔའི་མིང་འབའ་ཞིག་དེ་ལྟ་ཡིན་པར་མ་ཟད་ཀྱི། ཆོས་ཐམས་ཅད་ཀྱི་མིང་ཡང་འོང་བ་དང་འགྲོ་བ་མེད་པས་མེད་པར་བསྟན་ནས། དེ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའི་མིང་ཡང་གང་ནས་ཀྱང་མི་འོང་གང་དུ་ཡང་མི་འགྲོའོ་ཞེས་བྱ་བས་མཇུག་བསྡུས་ཏེ། ཆོས་ཐམས་ཅད་ཀྱི་མིང་དང་། བྱང་ཆུབ་སེམས་དཔའ་དང་། བྱང་ཆུབ་སེམས་དཔའི་མིང་ཡང་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 497]
དེ་ལྟར་མིང་མེད་པར་བསྟན་ནས། འདི་ལྟར་གཟུགས་ཞེས་བྱ་བ་དང་། ཚོར་བ་ཞེས་བྱ་བ་དང་། འདུ་ཤེས་ཞེས་བྱ་བ་དང་། འདུ་བྱེད་ཅེས་བྱ་བ་དང་། རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་འདི་དག་ནི་མིང་དུ་བཏགས་པ་ཙམ་དུ་ཟད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཀུན་བརྟགས་པའི་ཆོས་ཐམས་ཅད་མིང་དུ་ཟད་པར་བསྟན་ཏོ། །

[Block 498]
དེའི་འོག་ཏུ་འདི་ལྟར་གཟུགས་ཞེས་བྱ་བའི་མིང་དུ་བཏགས་པ་གང་ཡིན་པ་དེ་ནི་གཟུགས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཆོས་ཉིད་ཀྱི་གཟུགས་ལ་སོགས་པ་དང་། མིང་དག་ཐ་དད་པ་མ་ཡིན་པར་བསྟན་ཏེ། གཟུགས་ཞེས་བྱ་བའི་མིང་ཀུན་བརྟགས་པ་གང་ཡིན་པ་དེ་ནི་དོན་དམ་པའི་གཟུགས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 499]
དེ་སྐད་བསྟན་ནས་དེའི་འོག་ཏུ་འདི་ལྟར་མིང་ནི་མིང་གི་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་སྟེ། སྟོང་པ་གང་ཡིན་པ་དེ་ནི་མིང་མ་ཡིན་ནོ་ཞེས་བྱ་བས་མིང་དང་། སྟོང་པ་གཉིས༌[^314]ཐ་དད་པའི་གཏན་ཚིགས་བསྟན་ཏེ་ཀུན་བརྟགས་པའི་མིང་གང་ཡིན་པ་དེ་ནི་མིང་གི་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་ལ། དེའི་སྟོང་པ་ཉིད་གང་ཡིན་པ༌[^315]དེ་ནི་མིང་གི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 500]
དེ་ལྟར་མིང་ཡོད་པ་མ་ཡིན་པ་དང་། དོན་དམ་པའི་ཆོས་རྣམས་ཡོད་པའི་ཕྱིར་ཆོས་དེ་དག་མིང་གི་རང་བཞིན༌[^316]ནོ། །

[Block 501]
དེ་བས་ན་དོན་དམ་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡང་མིང་གི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ། །

[Block 502]
དེ་བས་ན་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བ་གློ་བུར་དུ་བཏགས་པ་ཡིན་པར་བསྟན་པའི་ཕྱིར། དེའི་ཕྱིར་འདི་ལྟ་སྟེ་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བ་འདི་ནི་མིང་ཙམ་མོ་ཞེས་བྱ༌[^317]བ་གསུངས་སོ། །

[Block 503]
དེ་བཞིན་དུ་ཁམས་དང་། སྐྱེ་མཆེད་དང་། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་རྣམས་ལ་ཡང་མཐུན་པར་བསྒྲེ་བར་བྱའོ། །

[Block 504]
ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་ལ་ནི་ཐ་དད་དེ། སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ཡང་མིང་མེད་མིང་ལ་ཡང་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་ཡང་ཀུན་བརྟགས་པ་ཉིད་ཡིན་ལ། མིང་ཡང་ཀུན་བརྟགས་པ་ཉིད་དོ། །

[Block 505]
དེ་ལ་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་མིང་གནས་པ་ཡང་མ་ཡིན་མིང་ལ་ཡང་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གནས་པ་མ་ཡིན་ཏེ། གཉི་ག་ཡང་སྒྱུ་མ་དང་མཚུངས་པས་དངོས་པོ་མེད་པའི་ཕྱིར་རོ། །

[Block 506]
དེ་བས་ན་འདི་ལྟར་མིང་གང་ཡིན་པ་དང་། སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གང་ཡིན་པ་དེ་གཉི་ག་ཡང་མེད་ཅིང་། མི་དམིགས་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་བཞིན་དུ་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 507 [HEADING]]
###### མངོན་པར་འགྲུབ་པ་ཤིན་ཏུ་མེད་པ། ^1-1-7-2-6-0

[Block 508]
ཚིག་དྲུག་པ་ལ། ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་འདི་ལྟར་བདག་ཤིན་ཏུ་མེད་པས་མི་དམིགས་ན། དེ་མངོན་པར་གྲུབ་པར༌[^318]འགྱུར་བ་ལྟ་ག་ལ་ཡོད་ཅེས་བྱ་བ་ལ་སོགས་པས་བདག་ལ་སོགས་པ་གང་ཟག་རྣམས་དང་། གཟུགས་ལ་སོགས་པ་ཆོས་རྣམས་ཤིན་ཏུ་མེད་ལ། ཡོད་པ་མ་ཡིན་ན༌[^319]མངོན་པར་འགྲུབ་པ་དང་། འབྱུང་བར་འགྱུར་བ་ལྟ་ག་ལ་ཡོད་དེ། དེ་བས་ན་ཆོས་ཐམས་ཅད་མངོན་པར་འགྲུབ་པ་ཤིན་ཏུ་མེད་པའི་མཚན་ཉིད་དུ་བསྟན་ཏོ། །

[Block 509]
མངོན་པར་འགྲུབ་པ་མེད་པ་ཞེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་ལ་བྱའོ། །

[Block 510 [HEADING]]
###### འདུས་པ་ལས་བྱུང་བའི་ངོ་བོ་ཉིད་མེད་པ། ^1-1-7-2-7-0

[Block 511]
ཚིག་བདུན་པ༌[^320]ལས་བྱུང་བའི་ངོ་བོ་ཉིད་མེད་དོ་ཞེས་བྱ་བ་ནི་རང་གི་ངོ་བོ་ལ་ངོ་བོ་ཉིད་ཅེས་བྱ་སྟེ། རང་གི་གང་ཡིན་པ་དེ་ཉིད་ངོ་བོ་ཉིད་ཅེས་བྱ་བར་འགྱུར་གྱི། གཞན་གྱི་ནི་མ་ཡིན་ནོ། །

[Block 512]
གཟུགས་ལ་སོགས་པའི་ཆོས་ཐམས་ཅད་ནི་བརྟེན་ནས་འབྱུང་གི། མ་བརྟེན་པར་ནི་མ་ཡིན་ནོ། །

[Block 513]
གང་ཟག་གཞན་ལས་བརྟེན་ཏེ་འབྱུང་བ་དེ་དག་ནི་གཞན་གྱི་ཉིད་ཡིན་གྱི། རང་གི་ནི་མ་ཡིན་ནོ། །

[Block 514]
དེ་བས་ན། ཆོས་ཐམས་ཅད་ནི་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པས། ངོ་བོ་ཉིད་མེད་པ་ཞེས་བྱའོ། །

[Block 515]
དེའི་ཕྱིར་གཟུགས་ལ་སོགས་པ་ཀུན་བརྟགས་པ་རྣམས་ནུས་པར་འགྱུར་བའི༌[^321]སྟོང་པ་ཉིད་གང་ཡིན་པ་དེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མ་ཡིན་ཞིང་། གཞན་ལ་ལྟོས་པ་མ་ཡིན་པས་དེ་ཉིད་ཆོས་ཐམས་ཅད་ཀྱི་ངོ་བོ་ཉིད་དུ་རིགས་སོ། །

[Block 516]
དེ་བས་ན་འདུས་པ་ལས་བྱུང་བའི་ངོ་བོ་ཉིད་མེད་དོ་ཞེས་བཤད་དེ། འདུས་པ་ལས་བྱུང་བ་ནི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 517]
འདུས་ནས་འབྱུང་བས་ན་འདུས་པ༌[^322]ལས་འབྱུང་བ༌[^323]ཞེས་བྱ་སྟེ། རྒྱུ་དང་རྐྱེན་ཚོགས་པ་ལས་འབྱུང་ཞེས་པའི༌[^324]ཐ་ཚིག་གོ། །

[Block 518]
དེ་ལ་འགྲེས་རྣམ་པ་གསུམ་དུ་བསྟན་ཏེ། འདུས་པ་ལས་བྱུང་བའི་ཕྱིར་ངོ་བོ་ཉིད་མེད་དོ་ཞེས་བྱ་བ་ནི་གཅིག་གོ། །

[Block 519]
མི་རྟག་པ་ལ་སོགས་པ་ཡིན་པའི་ཕྱིར་ངོ་བོ་ཉིད་མེད་དོ་ཞེས་བྱ་བ་ཡང་གཅིག་གོ། །

[Block 520]
ཐེར་ཟུག་ཏུ་གནས་པ་མ་ཡིན་ཞིང་རྣམ་པར་འཇིག་པ་མ་ཡིན་པའི་ཕྱིར་ངོ་བོ་ཉིད་མེད་དོ་ཞེས་བྱ་བ་ཡང་གཅིག་གོ། །

[Block 521]
ཆོས་ཐམས་ཅད་ནི་མི་རྟག་པ་སྟེ་གང་དང་ཡང་བྲལ་བས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ཉན་ཐོས་ཀྱི་ཐེག་པའི་ཚུལ་གྱིས་ནི་མི་རྟག་པ་ཞེས་བྱ་བ་ཆོས་སྐྱེས་པ་གྱེས་པ་དང་ཞིག་པ་ལ་བྱའོ། །

[Block 522]
འདིར་ནི་མི་རྟག་པའི་མཚན་ཉིད་དེ་ལྟ་མ་ཡིན་པར་སྟོན་ཏེ། གང་དང་ཡང་བྲལ་བས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཆེན་པོ་འདི་ལ་མི་རྟག་པའི་དོན་ནི་མེད་པའི་དོན་ཏོ་ཞེས་འབྱུང་བའི་ཕྱིར་མི་རྟག་པའི་སྒྲ་ནི་མེད་པ་ལ་བྱའོ། །

[Block 523]
ཇི་ལྟ་ཞེ་ན་རྟག་པ་ལས་བཟློག་པ་ནི་མི་རྟག་པ་ཞེས་བྱའོ། །

[Block 524]
རྟག་པ་ཞེས་བྱ་བ་ནི་གང་རྟག་ཏུ་ཡོད་པ་དེ་ལ་བྱ་སྟེ། དེ་བས་ན་མི་རྟག་པ་ཞེས་བྱ་བ་ནི་གང་རྟག་ཏུ་མེད་པ་དེ་ལ་བྱའོ། །

[Block 525]
གང་རྟག་ཏུ་དུས་ཐམས་ཅད་དུ་མེད་པ་དེ་ལ་མི་རྟག་ཅེས་བྱའོ། །

[Block 526]
དེའི་ཕྱིར་མེད་པའི་དོན་ནི་མི་རྟག་པའི་དོན་ཞེས་བྱའོ། །

[Block 527]
དེ་ལྟར་གཟུགས་ལ་སོགས་པ་ཀུན་བརྟགས་པའི་ཆོས་ཐམས་ཅད་མི་རྟག་པ་སྟེ། མེད་པའི་ཕྱིར་ཡོད་པ་ལས་གྱུར་པ་གང་ཡང་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 528]
ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་འདི་ལྟར་མི་རྟག་པ་གང་ཡིན་པ་དེ་ནི་དངོས་པོ་མེད་པ་དང་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ལ་མི་རྟག་པ་ཞེས་བྱ་བའི་སྒྲ་ནི་མེད་པ་དང་། དངོས་པོ་མ་ཡིན་པ་སྟེ། སྟོང་པ་ཉིད་ལ་བྱའོ། །

[Block 529]
ཟད་ཅེས་བྱ་བའི་སྒྲ་ནི་ཀུན་བརྟགས་པའི་ཆོས་རྣམས་ལ་བྱའོ། །

[Block 530]
དེ་ལྟར་ནི༌[^325]མི་རྟག་པ་གང་ཡིན་པ་དེ༌[^326]སྟོང་པ་ཉིད་དང་། ཀུན་བརྟགས་པའི་ཆོས་ཟད་པ་དངོས་པོ་མེད་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །
--- END BLOCKS ---
