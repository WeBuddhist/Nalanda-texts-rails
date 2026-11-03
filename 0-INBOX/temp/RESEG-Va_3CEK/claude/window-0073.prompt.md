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
[Block 2556]
རྣམ་པ་གཏོད་ཅེས་བྱ་བ་འདི་ཅི་ཞེ་ན།

[Block 2557]
དང་པོ་ཉིད་དུ་བདེན་པ་རྣམས་ལ་རྣམ་པ་དག་འགོད་པའོ། །

[Block 2558]
གཞན་དག་གིས་ཀྱང་འཕེལ་བར་བྱེད། དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་ཆར་གྱིས་ཀྱང་དེ་དག་འཕེལ་བར་བྱེད་དོ། །

[Block 2559]
རྣམ་པར་འཕེལ་བར་བྱེད་པ་ན་སྔོན་ཐོབ་པ་རྣམས་མངོན་སུམ་དུ་མི་བྱེད་དེ། དགའ་བ་ཆེན་པོ་མེད་པའི་ཕྱིར་རོ། །

[Block 2560 [HEADING]]
###### བཟོད་པ། ^3-1-3-6-3-0

[Block 2561]
དེ་ལས་བཟོད་པ་ཡང་སྐྱེ་སྟེ། དེ༌[^1794]ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོའི་རིམ་གྱིས་མངོན་པར་འཕེལ་བ་དག་ལས་ཡང་། བཟོད་པ་སྐྱེ་སྟེ། ཡོངས་སུ་མི་ཉམས་པའི་སྒོ་ནས་བདེན་པ་ལ་ཆེར་བཟོད་པའི་ཕྱིར་རོ། །

[Block 2562]
དེ་ཡང་རྣམ་པ་གསུམ་སྟེ། ཆུང་ངུ་དང་། འབྲིང་དང་། ཆེན་པོའོ། །

[Block 2563]
དེ་ལ་རྣམ་པ་གཉིས་དེ་བཞིན། ། རྩེ་མོ་རྣམས་ཇི་སྐད་བཤད་པ་ལྟར་བཟོད་པ་ཆུང་ངུ་དང་འབྲིང་དག་ཀྱང་དེ་དང་འདྲ་སྟེ། དེ་ཁོ་ན་བཞིན་དུ་རྣམ་པ་གཏོད་པའི་ཕྱིར་རོ། །

[Block 2564]
རྣམ་པར་འཕེལ་བ་ལ་ནི་ཁྱད་པར་འདི་ཡོད་དེ། བཟོད་པ་ནི། ཐམས་ཅད་ཆོས་ཀྱིས་འཕེལ་བར་བྱེད་ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་ཁོ་ནས་འཕེལ་བར་བྱེད་ཀྱི་གཞན་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 2565]
ཆེན་པོ་འདོད་གཏོགས་སྡུག་བསྔལ་ཡུལ། །བཟོད་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། དེ་ནི་ཆོས་ཀྱི་མཆོག་དང་ཉེ་བའི་ཕྱིར་འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་ལ་དམིགས་པ་ཁོ་ནའོ། །

[Block 2566]
དེ་ཉིད་ཀྱི་ཕྱིར་དྲོ་བར་གྱུར་པ་ལ་སོགས་པའི་ངེས་པ་མ་སྨོས་པའི་ཕྱིར་ཁམས་གསུམ་པའི་སྡུག་བསྔལ་ལ་སོགས་པ་ལ་དམིགས་པ་ཉིད་དུ་གྲུབ་པོ། །གང་གི་ཚེ་གཟུགས་དང་གཟུགས་མེད་པའི་གཉེན་པོ་ལ་སོགས་པ་བདེན་པའི་རྣམ་པ་དམིགས་པ་རེ་རེ་ནས་ཕྲི་ནས་འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་ཁོ་ན་ལ་སྐད་ཅིག་མ་གཉིས་སུ་ཡིད་ལ་བྱེད་པའི་བར་དེ་ཐམས་ཅད་ནི་བཟོད་པ་འབྲིང་ཡིན་ལ། གང་གི་ཚེ་སྐད་ཅིག་མ་གཅིག་ཁོ་ན་ཡིན་པ་དེའི་ཚེ་ནི་ཆེན་པོ་ཡིན་ནོ་ཞེས་གྲག་གོ། །

[Block 2567]
དེ་ནི་སྐད་ཅིག་གཅིག །དེ་ནི་སྐད་ཅིག་མ་གཅིག་ཡིན་གྱི་རྒྱུན་ཆགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2568 [HEADING]]
###### ཆོས་མཆོག། ^3-1-3-6-4-0

[Block 2569]
དེ་བཞིན་དུ་ཆོས་མཆོག །དེ་དག་ཀྱང་བཟོད་པ་ཆེན་པོ་ཇི་ལྟ་བ་བཞིན་དུ་འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ༌[^1795]དམིགས་པ་དང་སྐད་ཅིག་མ་གཅིག་པ་དག་ཡིན་ནོ། །

[Block 2570]
དེ་དག་ནི་འཇིག་རྟེན་པ་ཡང་ཡིན་ལ་ཆོས་ཀྱི་མཆོག་ཀྱང་ཡིན་ཞིང་། འཇིག་རྟེན་པ་ཐམས་ཅད་ཀྱི་མཆོག་ཏུ་གྱུར་པའི་ཕྱིར་འཇིག་རྟེན་པའི་ཆོས་ཀྱི་མཆོག་རྣམས་ཏེ། སྐལ་བ་མཉམ་པའི་རྒྱུ་མེད་པར་དེའི་རྩལ་གྱིས་ལམ་འདྲེན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2571]
དྲོ་བར་གྱུར་པ་ལ་སོགས་པ་དེ་དག་ནི་དྲན་པ་ཉེ་བར་གཞག་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ཤེས་རབ་ཀྱི་བདག་ཉིད་ཅེས་བྱ་བའོ།[^1796] །ཐམས་ཅད་ཕུང་པོ་ལྔ། འཁོར་དང་བཅས་ཏེ་སྨོས་པའི་ཕྱིར་རོ། །

[Block 2572]
ཐོབ་པ་མ་གཏོགས། ཐོབ་པ༌[^1797]རྣམས་ནི་དྲོ་བར་གྱུར་པ་ལ་སོགས་པས་མ་བསྡུས་ཏེ། འཕགས་པ་ལ་དེ་མངོན་སུམ་དུ་གྱུར་པས་དྲོ་བར་གྱུར་པ་ལ་སོགས་པ་ཡང་མངོན་སུམ་དུ་འགྱུར་དུ་འོངས་པས་སོ། །

[Block 2573]
དེ་ལ་བདེན་པ་གསུམ་ལ་དམིགས་པའི་དྲོ་བར་གྱུར་པ་རྣམ་པ་གཏོད་པ་ལ་ནི་ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་ད་ལྟར་བྱུང་བ་ཡིན་ལ་མ་འོངས་པ་ནི་བཞི་ཆར་འཐོབ་བོ། །

[Block 2574]
འགོག་པའི་བདེན་པ་ལ་དམིགས་པ་ལ་ནི་དེ་ཁོ་ན་གཉི་ག་ཡིན་ནོ། །

[Block 2575]
རྣམ་པ་དག་ནི་ཐམས་ཅད་དུ་འདྲ་བ་ཡིན་ནོ། །

[Block 2576]
རྣམ་པར་འཕེལ་བ་ལ་ནི་བཞི་ལས་གང་ཡང་རུང་བ་ཞིག་ཡིན་ལ་མ་འོངས་པ་ནི་བཞི་ཆར་རོ། །

[Block 2577]
འགོག་པ་ལ་དམིགས་པ་དེ་ཁོ་ན་ལ་ནི་ཐ་མ་ཡིན་ལ་མ་འོངས་པ་ནི་བཞི་ཆར་རོ། །

[Block 2578]
རྣམ་པ་ནི་ཐམས་ཅད་དོ། །

[Block 2579]
[^1798]རིགས་རྣམས་ཐོབ་ཟིན་པའི་ཕྱིར་རོ། །

[Block 2580]
རྩེ་མོ་བདེན་པ་བཞི་ལ་དམིགས་པ་རྣམ་པ་གཏོད་པ་དང་། འགོག་པ་ལ་དམིགས་པ་འཕེལ་བ་ལ་ནི་ཐ་མ་ཡིན་ལ་མ་འོངས་པ་ནི་བཞི་ཆར་རོ། །

[Block 2581]
རྣམ་པ་ནི་ཐམས་ཅད་དོ། །

[Block 2582]
བདེན་པ་གསུམ་ལ་དམིགས་པ་རྣམ་པར་འཕེལ་བ་ལ་ནི་བཞི་ལས་གང་ཡང་རུང་བ་ཞིག་ཡིན་ལ་མ་འོངས་པ་ནི་བཞི་ཆར་རོ། །

[Block 2583]
རྣམ་པ་ནི་ཐམས་ཅད་དོ། །

[Block 2584]
བཟོད་པ་རྣམས་ལ་ནི་ཐམས་ཅད་དུ་ཐ་མ་ཡིན་ལ་མ་འོངས་པ་ནི་བཞི་ཆར་རོ། །

[Block 2585]
རྣམ་པ་ནི་ཐམས་ཅད་དོ། །

[Block 2586]
ཆོས་ཀྱི་མཆོག་དག་ལ་ནི་ཐ་མ་ཡིན༌[^1799]ལ་མ་འོངས་པ་ནི་བཞི་ཆར་རོ། །

[Block 2587]
རྣམ་པ་ནི༌[^1800]བཞི་ཁོ་ན་སྟེ། གཞན་མེད་པའི་ཕྱིར་དང་། མཐོང་བའི་ལམ་དང་འདྲ་བའི་ཕྱིར་རོ། །

[Block 2588]
དེ་ལྟ་ན་ངེས་འབྱེད་ཆ་མཐུན་རྣམ་པ་བཞི་བཞི་པོ་འདི་དག་ནི་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པའི་དགེ་བའི་རྩ་བ་དག་ཡིན་ཏེ། འདི་ལྟ་སྟེ། དྲོ་བར་གྱུར་པ་དང་། རྩེ་མོ་རྣམས་དང་། བཟོད་པ་རྣམས་དང་། ཆོས་ཀྱི་མཆོག་རྣམས་སོ། །

[Block 2589]
དེ་དག་ལས་གཉིས་ནི་ཡོངས་སུ་ཉམས་པའི་སྒོ་ནས་གཡོ་བའི་ཕྱིར་ཆུང་ངུ་དག་ཡིན་ནོ། །

[Block 2590]
བཟོད་པ་རྣམས་ནི་འབྲིང་ཡིན་ནོ། །

[Block 2591]
ཆོས་ཀྱི་མཆོག་རྣམས་ནི་ཆེན་པོ་ཡིན་ནོ། །

[Block 2592 [HEADING]]
###### ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་ཞེས་བྱ་བའི་དོན། ^3-1-3-6-5-0

[Block 2593]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། ངེས་པར་འབྱེད་པས་ན་ངེས་པར་འབྱེད་པ་སྟེ། འཕགས་པའི་ལམ་མོ། །

[Block 2594]
དེས་ཐེ་ཚོམ་སྤོང་བའི་ཕྱིར་དང་། བདེན་པ་རྣམས་ལ་འདི་ནི་སྡུག་བསྔལ་ལོ་ཞེས་བྱ་བ་ནས་འདི་ནི་ལམ་མོ་ཞེས་བྱ་བའི་བར་དུ་རྣམ་པར་འབྱེད་པའི་ཕྱིར་རོ། །

[Block 2595]
དེའི་ཆ་ནི་མཐོང་བའི་ལམ་གྱི་ཕྱོགས་གཅིག་ཡིན་ཏེ། དེ་འདྲེན་པར་བྱེད་པ་ཉིད་ཀྱིས་ཕན་འདོགས་པའི་ཕྱིར་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་སོ། །
--- END BLOCKS ---
