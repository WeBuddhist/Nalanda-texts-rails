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
[Block 2661]
ཞེས་བྱ་བ་འདི་ནི་སྲིད་པ་མ་ཡིན་ནོ། །

[Block 2662 [VERSE]]
དེས་ན་ལུང་གི་དངོས་པོ་རྣམས། །
རྟོགས་པ་པོ་ཡི་རྣམ་འགས་ཀྱང་། །
མེད་ན་མི་འབྱུང་གྲགས་མིན་ན། །
དེ་དག་ལས་དོན་ངེས་གང་ཡིན། །

[Block 2663]
སྐྱེ་བོ་མི་ཤེས་པ་ལུང་གི་ཚད་མ་དེས་ཀུན་ནས་བསྟན་པའི་དོན་རྟོགས་པར་བྱ་བའི་ཕྱིར། ཚོལ་བར་བྱེད་དེ། ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རྟོགས་པར་བྱེད་པ་ནི་བསྟན་པ་ལ་ལྟོས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2664]
དབང་པོ་ལས་འདས་པའི་ཡོན་ཏན༌[^1825]གྱི་སྐྱེས་བུ་རྣམ་པར་འབྱེད་པར་མི་ནུས་པའི་ཕྱིར། འདོད་པའི་དོན་ཡོད་པ་ཉིད་མེད་པར་ཚིག་རྣམས་ཀྱི་འཇུག་པ་མཐོང་བ༌[^1826]མི་ཤེས་པ་ནི་འཁྲུལ་པ་མ་མཐོང་བ་ཅན༌[^1827]གྱི་སྐྱེས་བུ་དག་གི་ཚིག་ལ་ཡང་ཅི་དོན་ཇི་ལྟ་བ་ཅན་ནམ། མ་ཡིན་ཞེས་ཐེ་ཚོམ་དུ་འགྱུར་རོ། །

[Block 2665]
དེས་ན་འདིས་ནི་འགའ་ཞིག་གི་ཚིག༌[^1828]གིས་ཅུང་ཟད་ཀྱང་ངེས་པར་འགྱུར་བ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2666]
འདི་ཡི།

[Block 2667 [VERSE]]
དེ་ཕྱིར་དེ་ནི་ལོག་ན་ཡང་། །
དངོས་པོ་མེད་པ་གྲུབ་མི་འགྱུར། །

[Block 2668]
ལུང་ནི་ཐམས་ཅད་ཀྱི་ཡུལ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར། དངོས་པོ་ཡོད་ན་མི་སླུ་བས༌[^1829]འདི་འཇུག་པའི་ཕྱིར། དེ་ལོག་པའི་མཚན་ཉིད་ཅན་གྱི་མི་དམིགས་པས་མེད་པ་བསྒྲུབ་པར༌[^1830]འགྱུར་རོ། །

[Block 2669]
ཞེས་བཤད་པ་གང་ཡིན་པ་དེ་ཡང་འདི་ནི་ཐམས་ཅད་ཀྱི་ཡུལ་ཅན་ཉིད་ཡིན༌[^1831]ན་ཡང་དངོས་པོ་མེད་པར་མི་འཇུག་པར་འགྱུར་རོ། །

[Block 2670]
དེ་ལས་ཁོང་དུ་ཆུད་པར་འདོད་པའི་གྲུབ་པ་མེད་དོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2671 [VERSE]]
ངེས་མེད་ངེས་པའི་འབྲས་བུ་ཅན། །
མི་དམིགས་པ་ནི་མི་འགྲུབ་པོ། །

[Block 2672]
དེའི་ཕྱིར་ཚད་མ་གསུམ་ལོག་ཏུ་ཟིན་ཀྱང་བསྐལ་པའི་དོན་དག་མེད་པར་ངེས་པ་མ་ཡིན་ནོ། །

[Block 2673 [VERSE]]
རིག་བྱེད་ཚད་མ་དང་ནི་འགས་བྱེད༌[^1832]སྨྲ། །
ཁྲུས་ལ་ཆོས་འདོད་དང་ནི་རིགས་སྨྲ་དྲེགས། །
སྡིག་པ་གཞོམ་ཕྱིར་གདུང་བ་རྩོམ་ཞེས་པ། །
བླུན་པོ་ཤེས་རབ་འཆལ་པའི་རྟགས་ལྔ་ཡིན། །

[Block 2674 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 2675 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 2676]
རིག་པ་ཆེན་པོ་སའི་སྟེང་མ་ལུས་པ་ན་སྨྲ་བའི་གླང་པོ་ཆེའི་སྤྱི་བོ་གནོན་པར་མཛད་པའི་སེང་གེ་ཕྱོགས་མ་ལུས་པར་སྙན་པར་གྲགས་པ་ཅན།

[Block 2677]
དཔལ༌[^1833]ཆོས་ཀྱི་གྲགས་པས་སྦྱར་བ་ལས།

[Block 2678]
ཚད་མ་རྣམ་འགྲེལ་གྱི༌[^1834]ལེའུ་དང་པོའི་འགྲེལ་པ་རྫོགས་སོ།། །།
--- END BLOCKS ---
