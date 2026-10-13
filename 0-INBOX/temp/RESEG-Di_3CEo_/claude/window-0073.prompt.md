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
[Block 2556 [VERSE]]
གསུམ་པོ་བསོད་ནམས་བྱ་བ་དང་། །
དེ་བཞིན་དཔེར་ན་ལས་ལམ་བཞིན། །

[Block 2557]
དེ་ལ་སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་གཞི་ལ་ལུས་དང་ངག་གི་ལས་ནི་རྣམ་པ་གསུམ་ཆར་ཡིན་ནོ། །

[Block 2558]
དེ་ཀུན་ནས་སློང་བར་བྱེད་པའི་སེམས་པ་ནི་བསོད་ནམས་ཡང་ཡིན་ལ་བྱ་བ་ཡང་ཡིན་ནོ། །

[Block 2559]
དེ་དང་ལྷན་ཅིག་འབྱུང་བའི་ཆོས་རྣམས་ནི་བསོད་ནམས་ཁོ་ན་ཡིན་ནོ། །

[Block 2560]
ཚུལ་ཁྲིམས་ལས་བྱུང་བའི་ལུས་དང་ངག་གི་ལས་ཁོ་ན་ཡིན་པས་གསུམ་ཆར་ཡིན་ནོ། །

[Block 2561]
བསྒོམས་པ༌[^1022]ལས་བྱུང་བ་ལ་བྱམས་པ་ནི་བསོད་ནམས་ཀྱང་ཡིན་ལ་བསོད་ནམས་བྱ་བའི་གཞི་ཡང་ཡིན་ནོ། །

[Block 2562]
དེ་དང་ལྷན་ཅིག་འབྱུང་བའི་སེམས་པ༌[^1023]དང་ཚུལ་ཁྲིམས་ནི་བསོད་ནམས་ཀྱང་ཡིན་ལ་བྱ་བ་ཡང་ཡིན་ནོ། །

[Block 2563]
དེ་དང་མཚུངས་པར་ལྡན་པ་གཞན་དག་ནི་བསོད་ནམས་ཁོ་ན་ཡིན་ནོ། །

[Block 2564 [HEADING]]
##### སྦྱིན་པ། ^4-3-14-1-0

[Block 2565]
སྦྱིན་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན། གང་གིས་སྦྱིན་བྱེད་དེ་སྦྱིན་པ། མཆོད་དང་ཕན་འདོགས་འདོད་པ་ཡིས། །གང་གིས་གཞན་དག་ལ་མཆོད་པ་དང་ཕན་གདགས་པར་འདོད་པ་དག་གིས་སྦྱིན་པ་སྦྱིན་པར་བྱེད་པ་དེ་སྦྱིན་པའོ། །གང་གིས་སྦྱིན་པར་བྱེད་པ་དེ་ཡང་གང་ཞིག་ཅེ་ན། ལུས་དང་ངག་ལ་སློང་དང་བཅས། །སློང་བ་ཡང་གང་ཞིག་ཅེ་ན། ཚོགས་པ་གང་གིས་དེ་སློང་བར་བྱེད་པའོ། །

[Block 2566]
དེ་འབྲས་ལོངས་སྤྱོད་ཆེན་པོ་ཅན། །སྦྱིན་པ་གང་ཡིན་པ་དེ་ནི་འབྲས་བུ་ལོངས་སྤྱོད་ཆེན་པོ་ཅན་ཡིན་ནོ། །

[Block 2567]
སྦྱིན་པ་ན་ཡང་།

[Block 2568 [VERSE]]
བདག་གཞན་དོན་ཕྱིར་གཉིས་དོན་ཕྱིར། །
གཉིས་ཀའི་དོན་དུ་མིན་ཕྱིར་སྦྱིན། །

[Block 2569]
དེ་ལ་གང་འདོད་ཆགས་དང་མ་བྲལ་བས་མཆོད་རྟེན་ལ་སྦྱིན་པ་དེ་ནི་བདག་ཁོ་ནའི་དོན་དུའོ། །

[Block 2570]
གང་འདོད་ཆགས་དང་བྲལ་བས་ཕ་རོལ་ལ་སྦྱིན་པ་མཐོང་བའི་ཆོས་ལ་མྱོང་བ་མ་གཏོགས་པ་དེ་ནི་གཞན་ཁོ་ནའི་དོན་དུའོ། །

[Block 2571]
འདོད་ཆགས་དང་མ་བྲལ་བས་ཕ་རོལ་ལ༌[^1024]སྦྱིན་པ་གང་ཡིན་པ་དེ་ནི་གཉིས་ཀའི་དོན་གྱི་ཕྱིར་རོ། །

[Block 2572]
འཕགས་པ་འདོད་ཆགས་དང་བྲལ་བས་གང་མཆོད་རྟེན་ལ་འབུལ་བ་དེ་ནི་གཉིས་ཀའི་དོན་དུ་མ་ཡིན་ནོ། །

[Block 2573]
དེ་ནི་བཀུར་སྟི་དང་བྱས་པ་གཟོ་བ༌[^1025]འགའ་ཞིག༌[^1026]གིས་འབུལ་བར་ཟད་དོ། །

[Block 2574]
སྦྱིན་པའི་འབྲས་བུ་ལོངས་སྤྱོད་ཆེན་པོ་ཅན་ཞེས་སྤྱིར་བསྟན་པ།

[Block 2575 [VERSE]]
[^1027] དེ་ཡིས༌[^1028]ཁྱད་པར་སྦྱིན་བདག་དང་། །
དངོས་དང་ཞིང་གི་ཁྱད་པར་ལས། །

[Block 2576]
དེ་ལ་རེ་ཞིག །སྦྱིན་བདག་ཁྱད་འཕགས་དད་སོགས་ཀྱིས། །དད་པ་དང་ཚུལ་ཁྲིམས་དང་ཐོས་པ་ལ་སོགས་པའི་ཡོན་ཏན་དང་ལྡན་པའི་སྦྱིན་བདག་ནི་ཁྱད་པར་དུ་འཕགས་པའོ། །

[Block 2577]
དེའི་སྦྱིན་པ་དེ་ནི་སྦྱིན་བདག་གི་ཁྱད་པར་ལས་འབྲས་བུ་འབྱིན་པ་ལ་ཁྱད་པར་དུ་འཕགས་པར་འགྱུར་ཏེ།

[Block 2578 [VERSE]]
སྦྱིན་བདག་དེ་ལྟ་བུ་དེ་ནི། །
གུས་ལ་སོགས་པས་སྦྱིན་པར་བྱེད། །

[Block 2579]
གུས་པ་དང་། རང་གི་ལག་དང་། དུས་སུ་དང་། གཞན་ལ་མི་གནོད་པར་སྦྱིན་པར་བྱེད་དེ།

[Block 2580 [VERSE]]
དེ་ཕྱིར་བཀུར་སྟི་རྒྱ་ཆེན་དང་། །
དུས་དང་བར་ཆད་མེད་པར་རྙེད། །

[Block 2581]
དེའི་ཕྱིར་སྦྱིན་བདག་དེའི་སྦྱིན་པ་དེ་ནི་བྱིན་པས་གོ་རིམས༌[^1029]བཞིན་དུ་ཁྱད་པར་དེ་བཞིན༌[^1030]འབྱུང་ངོ་། །ཡང་ཇི་ལྟར་དངོས་པོ་ཁྱད་པར་དུ་འཕགས་ཤེ་ན། ཁ་དོག་ལ་སོགས་ཕུན་ཚོགས་དངོས། །ཁྱད་པར་དུ་འཕགས་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2582]
དངོས་པོ་དེ་ལྟ་བུ་བྱིན་པས་རིམ་པ་བཞིན་དུ།

[Block 2583 [VERSE]]
དེ་ལས་གཟུགས་བཟང་གྲགས་ལྡན་པ། །
དགའ་དང་ཤིན་ཏུ་གཞོན་ཤ་ཅན། །
དུས་སུ་རེག་ན་བདེ་ལུས་འགྱུར། །

[Block 2584]
ཁ་དོག་ཕུན་སུམ་ཚོགས་པ་བྱིན་པས་གཟུགས་བཟང་བ་དང་། དྲི་ཕུན་སུམ་ཚོགས་པ་བྱིན་པས་གྲགས་པ་ཕུན་སུམ༌[^1031]ཚོགས་པ་དང་། རོ་ཕུན་སུམ་ཚོགས་པ་བྱིན་པས་དགའ་བ་དང་། རེག་བྱ་ཕུན་སུམ་ཚོགས་པ་བྱིན་པས་ལུས་ཤིན་ཏུ་གཞོན་ཤ་ཅན་དང་། འདིའི་ལུས་དུས་སུ་རེག་ན་བདེ་བའི་ལུས་སུ་འགྱུར་རོ། །

[Block 2585]
ཡང་ཇི་ལྟར་ན་ཞིང་ཁྱད་པར༌[^1032]དུ་འཕགས་ཤེ་ན།

[Block 2586 [VERSE]]
འགྲོ་དང་སྡུག་བསྔལ་ཕན་འདོགས་དང་། །
ཡོན་ཏན་རྣམས་ཀྱིས༌[^1033]ཞིང་ཁྱད་འཕགས། །

[Block 2587]
རེ་ཞིག་འགྲོ་བ་ནི་ཇི་ལྟར་དུད་འགྲོའི་སྐྱེ༌[^1034]གནས་སུ་སྐྱེས་པ་ལ་སྦྱིན་པ་བྱིན་ན་རྣམ་པར་སྨིན་པ་བརྒྱ་འགྱུར་དུའོ། །

[Block 2588]
ཚུལ་ཁྲིམས་འཆལ་བར་གྱུར་པའི་མི་ལ་སྦྱིན་པ་བྱིན་ན་སྟོང་འགྱུར་དུའོ། །

[Block 2589]
སྡུག་བསྔལ་གྱིས༌[^1035]ཁྱད་པར་དུ་འཕགས་ཏེ། ཇི་ལྟར་ནད་པ་ལ་བྱིན་ན་རྣམ་པར་སྨིན་པ་ཚད་མེད་པར་གསུངས་པ་ལྟ་བུའོ། །

[Block 2590]
ཕན་འདོགས་པའི་ཁྱད་པར་ལས་ནི་འདི་ལྟ་སྟེ་ཕ་མའོ། །

[Block 2591]
ཡོན་ཏན་གྱི་ཁྱད་པར་ལས་ནི་ཇི་ལྟར་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ལ་བྱིན་ན་རྣམ་པར་སྨིན་པ་འབུམ་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 2592]
སྦྱིན་པ་ཐམས་ཅད་ཀྱི་ནང་ན། མཆོག་ནི་གྲོལ་བས་གྲོལ་བ་ལའང་། །འདོད་ཆགས་དང་བྲལ་བས་འདོད་ཆགས་དང་བྲལ་བ་ལ་བྱིན་པ་གང་ཡིན་པའོ། །

[Block 2593]
བྱང་ཆུབ་སེམས་དཔའ་ཡིས། གང་བྱང་ཆུབ་སེམས་དཔའ་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པར་བྱ་བའི་ཕྱིར་སྦྱིན་པ་དེ་ཡང་མཆོག་ཡིན་ནོ། །

[Block 2594]
དེ་མ་གཏོགས་པ་བཅོམ་ལྡན་འདས་ཀྱིས་སྦྱིན་པ་བརྒྱད་གསུངས་པ་དེ་དག་གི་ནང་ན་ནི། བརྒྱད་པ། མཆོག་ཡིན་ནོ་ཞེས་སྦྱར་རོ། །

[Block 2595]
བརྒྱད་གང་ཞེ་ན། ཉེ་བ་ལ་སྦྱིན་པ་དང་། འཇིགས་པས་སྦྱིན་པ་དང་། བདག་ལ་བྱིན་པས་སྦྱིན་པ་དང་། བདག་ལ་སྦྱིན་པར་འགྱུར་བས་སྦྱིན་པ་དང་། སྔོན་བདག་གི་ཕ་དང་མེས་པོ་དག་གིས་བྱིན་པས་སྦྱིན་པ་དང་། མཐོ་རིས་ཀྱི་དོན་དུ་སྦྱིན་པ་དང་། གྲགས་པའི་དོན་དུ་སྦྱིན་པ་དང་། སེམས་ཀྱི་རྒྱན༌[^1036]དང་། སེམས་ཀྱི་ཡོ་བྱད་དང་། རྣལ་འབྱོར་གྱི་ཚོགས་དང་། དོན་གྱི་མཆོག་གི་དོན་དུ་སྦྱིན་པ་བྱིན་པའོ། །
--- END BLOCKS ---
