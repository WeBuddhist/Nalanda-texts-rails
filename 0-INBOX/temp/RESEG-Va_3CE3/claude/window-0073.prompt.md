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
[Block 2556 [HEADING]]
###### ཉོན་མོངས་པ་མེད་པ། ^1-2-7-55-1-0

[Block 2557]
དེ་ལ་ཉོན་མོངས་པ་མེད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ནི་བདག་གི་ཕྱིར་གཞན་དག་ལ་ཉོན་མོངས་པ་སྐྱེ་བར་མ་གྱུར་ཅིག་ཅེས་བྱིན་གྱིས་བརླབས་ནས་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་ཏེ། སྔོན་གྱི་སྨོན་ལམ་གྱི་སྟོབས་ཀྱིས་གཞན་གྱི་རྒྱུད་ལ་ཉོན་མོངས་པ་སྐྱེ་བའི་སྐབས་མི་འབྱེད་པ་དེ་ནི་ཉོན་མོངས་པ་མེད་པའི་སྙོམས་པར་འཇུག་པ་ཞེས་བྱའོ། །

[Block 2558 [HEADING]]
###### སྨོན་ལམ་གྱི་ཤེས་པ། ^1-2-7-55-2-0

[Block 2559]
དེ་ལ་སྨོན་ལམ་གྱི་ཤེས་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ནི་དུས་གསུམ་དང་ཁམས་གསུམ་གྱི་ཆོས་རྣམས་ལས་ཤེས་པར་བྱ་བར་བསྡུས་པའི་ཆོས། འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པར་གཏོགས་པ་གང་ཡང༌[^1820]རུང་བ་འགའ་ཞིག་ཤེས་པར་བྱ་བའི་ཕྱིར་སྨོན་ལམ་བཏབ་པས་ན་དེ་དེ་མ་ཐག་ཏུ་ཤེས་པ་གང་གི༌[^1821]ཤེས་པར་གྱུར་པ་དེ་སྨོན་ལམ་སྔོན་དུ་འགྲོ་བའི་ཤེས་པ་ཡིན་པས་སྨོན་ནས༌[^1822]ཤེས་པ་ཞེས་བྱའོ། །

[Block 2560 [HEADING]]
###### ཡོངས་སུ་དག་པ་བཞི། ^1-2-7-55-3-0

[Block 2561 [HEADING]]
###### **གནས་ཡོངས་སུ་དག་པ།** ^1-2-7-55-3-1-0

[Block 2562]
དེ་ལ་ཡོངས་སུ་དག་པ་བཞི་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ། སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཉོན་མོངས་པའི་གནས་ངན་ལེན་ཐམས་ཅད་གནས་དང་ཤིན་ཏུ་བྲལ་བར་གྱུར་པ་དང་། བདག་གི་ལུས་ཀྱང་ཇི་ལྟར་འདོད་པ་བཞིན་ལེན་པ་དང་། གནས་པ་དང་འཆི་འཕོ་བ༌[^1823]རྣམས་ལ་རང༌[^1824]དབང་དུ་གྱུར་པ་ནི་གནས་ཡོངས་སུ་དག་པའོ། །

[Block 2563 [HEADING]]
###### **དམིགས་པ་ཡོངས་སུ་དག་པ།** ^1-2-7-55-3-2-0

[Block 2564]
སྤྲུལ་པ་དང་། ཡོངས་སུ་བསྒྱུར་བའི་གྲངས་སུ་གཏོགས་པ་དང་། དམིགས་པ་ཐམས་ཅད་ལ་དབང་དུ་གྱུར་པ་ནི་དམིགས་པ་ཡོངས་སུ་དག་པའོ། །

[Block 2565 [HEADING]]
###### **སེམས་ཡོངས་སུ་དག་པ།** ^1-2-7-55-3-3-0

[Block 2566]
སེམས་ཀྱི་གནས་ངན་ལེན་ཐམས་ཅད་དང་བྲལ་བས་སེམས་ལ་རྣམ་པ་ཐམས་ཅད་དུ་དགེ་བ་འཕེལ་བ་ནི་སེམས་ཡོངས་སུ་དག་པའོ། །

[Block 2567 [HEADING]]
###### **ཡེ་ཤེས་ཡོངས་སུ་དག་པ།** ^1-2-7-55-3-4-0

[Block 2568]
མ་རིག་པའི་ཕྱོགས་ཀྱི་གནས་ངན་ལེན་ཐམས་ཅད་དང་བྲལ་བས་ཤེས་པར་བྱ་བ་ཐམས་ཅད་ལ་ཤེས་པ་སྒྲིབ་པ་མེད་པ་དབང་དུ་གྱུར་པ་ནི་ཡེ་ཤེས་ཡོངས་སུ་དག་པའོ། །

[Block 2569 [HEADING]]
###### དབང་བཅུ། ^1-2-7-55-4-0

[Block 2570 [HEADING]]
###### **ཚེ་ལ་དབང་བ།** ^1-2-7-55-4-1-0

[Block 2571]
དེ་ལ་དབང་བཅུ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་ཇི་སྲིད་འདོད་པ་དེ་སྲིད་དུ་འདུག་པ་ནི་ཚེ་ལ་དབང་བའོ། །

[Block 2572 [HEADING]]
###### **སེམས་ལ་དབང་བ།** ^1-2-7-55-4-2-0

[Block 2573]
བསམ་གཏན་དང་ཚད་མེད་པ་དང་། རྣམ་པར་ཐར་པ་ལ་སོགས་པ་སེམས་གནས་པ་གང་གིས་གནས་པར་འདོད་པ་དེས་ཇི་ལྟར་འདོད་པ་བཞིན་གནས་པ་འདི་ནི་སེམས་ལ་དབང་བའོ། །

[Block 2574 [HEADING]]
###### **ཡོ་བྱད་ལ་དབང་བ།** ^1-2-7-55-4-3-0

[Block 2575]
ཀུན་དུ་བརྟགས་པ་ཙམ་གྱིས་དེ་མ་ཐག་ཏུ། དེའི་བཟའ་བ་ལ་སོགས་པ་ཡོ་བྱད་ཐམས་ཅད་ཇི་ལྟར་འདོད་པ་བཞིན་འབྱོར་པ་འདི་ནི༌[^1825]ཡོ་བྱད་ལ་དབང་བའོ། །

[Block 2576 [HEADING]]
###### **ལས་ལ་དབང་བ།** ^1-2-7-55-4-4-0

[Block 2577]
སྐྱེ་བར་འགྱུར་བའི་ལས༌[^1826]ཐམས་ཅད་ལ་ཇི་ལྟར་འདོད་པ་བཞིན་དུ་བསྒྱུར༌[^1827]བ་འདི་ནི་ལས་ལ་དབང་བའོ། །

[Block 2578 [HEADING]]
###### **སྐྱེ་བ་ལ་དབང་བ།** ^1-2-7-55-4-5-0

[Block 2579]
སྐྱེ་བའི་གནས་ཐམས་ཅད་དུ། གང་དུ་འདོད་པར་ཇི་ལྟར་འདོད་པ་བཞིན་དུ་སྐྱེ་བ་འདི་ནི་སྐྱེ་བ་ལ་དབང་བའོ། །

[Block 2580 [HEADING]]
###### **མོས་པ་ལ་དབང་བ།** ^1-2-7-55-4-6-0

[Block 2581]
དངོས་པོ་གང་དང་གང་ཇི་ལྟར་མོས་པར་བྱས་པ་དེ་དག་དེ་བཞིན་དུ་འགྲུབ་པ་འདི་ནི་མོས་པ་ལ་དབང་བའོ། །

[Block 2582 [HEADING]]
###### **སྨོན་ལམ་ལ་དབང་བ།** ^1-2-7-55-4-7-0

[Block 2583]
དེའི་སྨོན་ལམ་ཐམས་ཅད་ཇི་ལྟར་འདོད་པ་བཞིན་དུ་འགྲུབ་པ་འདི་ནི་སྨོན་ལམ་ལ་དབང་བའོ། །

[Block 2584 [HEADING]]
###### **རྫུ་འཕྲུལ་ལ་དབང་བ།** ^1-2-7-55-4-8-0

[Block 2585]
རྫུ་འཕྲུལ་གྱི་དགོས་པ་ཐམས་ཅད་ཇི་ལྟར་འདོད་པ་བཞིན་དུ་འགྲུབ་པ་འདི་ནི་རྫུ་འཕྲུལ་ལ་དབང་བའོ། །

[Block 2586 [HEADING]]
###### **ཡེ་ཤེས་ལ་དབང་བ།** ^1-2-7-55-4-9-0

[Block 2587]
གང་ཡང་ཤེས་པར་བྱ་བའི་དངོས་པོར་རབ་ཏུ་ཟབ་པ་ཤེས་པར་འདོད་པ་དེ་དག་མྱུར་བ་ཉིད་དུ་ཤེས་པ་འདི་ནི་ཡེ་ཤེས་ལ་དབང་བའོ། །

[Block 2588 [HEADING]]
###### **ཆོས་ལ་དབང་བ།** ^1-2-7-55-4-10-0

[Block 2589]
མིང་གི་ཚོགས་དང་། ཚིག་གི་ཚོགས་དང་། ཡི་གེའི་ཚོགས་རྣམས་ཇི་ལྟར་འདོད་པ་བཞིན་ཐོབ་པ་དང་། ཆོས་ཐམས་ཅད་ཡང་དག་པར་རྣམ་པར་དགོད་པ་ལ་མཁས་པ་འདི་ནི་ཆོས་ལ་དབང་བའོ། །

[Block 2590 [HEADING]]
###### དེ་བཞིན་གཤེགས་པའི་བསྲུང་བ་མེད་པ་གསུམ། ^1-2-7-55-5-0

[Block 2591]
དེ་ལ་དེ་བཞིན་གཤེགས་པའི་བསྲུང་བ༌[^1828]མེད་པ་གསུམ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སྲུང་བ༌[^1829]མེད་པ་གསུམ་ནི་གཞུང་ཉིད་ལས་གོ་སླའོ། །

[Block 2592 [HEADING]]
###### དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ། ^1-2-7-55-6-0

[Block 2593]
རྗེས་སུ་ཆགས་པ་དང་། ཁོང་ཁྲོ་བ་མེད་པས་དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ་ནི་གོ་སླའོ། །

[Block 2594 [HEADING]]
###### བསྙེལ་བ་མི་མངའ་བའི་ཆོས་ཉིད། ^1-2-7-55-7-0

[Block 2595]
བསྙེལ་བ་མི་མངའ་བའི་ཆོས་ཉིད་ཅེས་བྱ་བ་ནི་གང་དང་གང་གི་ཚེ་ཇི་ལྟར་སེམས་ཅན་གྱི་དོན་མཛད༌[^1830]པ་དེའི་ཚེ། དེ་བཞིན་གཤེགས་པ་དེ་བཞིན་དུ་སྒྲུབ་པ༌[^1831]ནི་བསྙེལ་བ་མི་མངའ་བའི་ཆོས་ཉིད་དོ། །
--- END BLOCKS ---
