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
ཐར་པའི་ཆ་དང་མཐུན་པ་དང་ཁྱད་པར་ཅི་ཡོད་ཅེ་ན། བར་ཆད་བྱེད་པ་མེད་ན་བདེན་པ་མཐོང་བ་ལ་ཆེས་ཉེ་བ་ཉིད་ཡིན་ནོ། །

[Block 2627]
རྩེ་མོ་ཐོབ་པ་རྩ་མི་འཆད། །རྩེ་མོ་ཐོབ་པ་ནི་ཡོངས་སུ་ཉམས་ཀྱང་དགེ་བའི་རྩ་བ་རྣམས་ཀུན་ཏུ་མི་འཆད་ཀྱི་ངན་སོང་དུ་ཡང་འགྲོ་ལ་མཚམས་མེད་པ་དག་ཀྱང་བྱེད་དོ། །

[Block 2628]
བཟོད་ཐོབ་ངན་སོང་མི་འགྲོའོ། །

[Block 2629]
བཟོད་པ་ལས་ནི་རྣམ་པར་ཉམས་ཀྱང་ངན་སོང་དུ་མི་འགྲོ་སྟེ། དེར་འགྲོ་བའི་ལས་དང་ཉོན་མོངས་པ་ཐག་བསྲིངས་པའི་ཕྱིར་རོ། །

[Block 2630]
བཟོད་པ་ཐོབ་པ་ཁོ་ནས་འགྲོ་བ་དང་། སྐྱེ་གནས་དང་། སྐྱེ་བ་དང་། ལུས་དང་། སྲིད་པ་དང་། ཉོན་མོངས་པ་རྣམས་ལས༌[^1822]ཁ་ཅིག་གིས༌[^1823]མི་སྐྱེ་བའི་ཆོས་ཉིད་ཐོབ་སྟེ། ངན་སོང་གི་འགྲོ་བ་རྣམས་དང་། སྒོ་ང་ལས་སྐྱེས་པ༌[^1824]དང་། དྲོད་གཤེར་ལས་སྐྱེས་པའི༌[^1825]སྐྱེ་གནས་དག་དང་། འདུ་ཤེས་མེད་པའི་སེམས་ཅན་དག་དང་། བྱང་གི་སྒྲ་མི་སྙན་དང་། ཚངས་པ་ཆེན་པོར་སྐྱེ་བ་རྣམས་དང་། ཟ་མ་དང་། མ་ནིང་དང་མཚན་གཉིས་པའི་ལུས་རྣམས་དང་བརྒྱད་པ་ལ་སོགས་པའི་སྲིད་པ༌[^1826]རྣམས༌[^1827]དང་། མཐོང་བས་སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་རྣམས་ཀྱི་མི་སྐྱེ་བའི་ཆོས་ཉིད་འཐོབ་བོ། །

[Block 2631]
དེ་དག་ནི་ཅི་རིགས་པར་ཏེ། ཆུང་ངུས་ནི་ངན་སོང་གི་འགྲོ་བ་རྣམས་ཀྱི་མི་སྐྱེ་བ་འཐོབ་ལ། ཆེན་པོས་ནི་གཞན་དག་གིའོ། །

[Block 2632 [HEADING]]
###### རིགས་གསུམ། ^3-1-3-6-7-0

[Block 2633]
ཉན་ཐོས་ལ་སོགས་པའི་རིགས་ཐ་དད་པའི་ཕྱིར་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་རིགས་གསུམ་ཡིན་ཏེ། དེ་ལ། གཉིས་སློབ་རིགས་ལས་བཟློག་ནས་ནི། །སངས་རྒྱས་སུ་འགྱུར། དྲོ་བར་གྱུར་པ་དང་། རྩེ་མོར་སྐྱེས་པ་ཉན་ཐོས་ཀྱི་རིགས་ལས་བཟློག་ནས་ཡང་སངས་རྒྱས་སུ་འགྱུར་བ་ནི་སྲིད་ཀྱི་བཟོད་པ་ཐོབ་པ་ལ་ནི་དེ་ལྟ་བུ་མི་སྲིད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། ངན་སོང་བཟློག་པའི་ཕྱིར་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་གཞན་ལ་ཕན་འདོགས་པའི་གཞན་གྱི་དབང་གིས་ངན་སོང་དུ་ཡང་འགྲོའོ་ཞེས་གྲག་གོ། །

[Block 2634]
རིགས་དེ་ཉིད་བཟློག་ཏུ་མི་རུང་བའི་ཕྱིར་མི་སྲིད་དོ། །

[Block 2635]
གཞན་གསུམ་ཡང་། བཟློག་ནས་འགྱུར་ཞེས་བྱ་བར་སྦྱར་ཏེ། ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་གསུམ་ཡང་ཉན་ཐོས་ཀྱི་རིགས་ལས་ལྡོག་ནས་སངས་རྒྱས་ལས་གཞན་པར་འགྱུར་ཏེ་རང་སངས་རྒྱས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2636]
རང་སངས་རྒྱས་ཀྱི་རིགས་རྣམས་ནི་བཟློག་པར་མི་ནུས་ཏེ། འདི་ལྟར།

[Block 2637 [VERSE]]
སྟོན་དང་བསེ་རུ་བྱང་ཆུབ་པར། །
བསམ་གཏན་མཐའ་རྟེན་གཅིག་ལ་ཀུན། །
སྟོན་པ་ནི་སངས་རྒྱས་སོ། །

[Block 2638]
བསེ་རུ་ལྟ་བུ༌[^1828]ནི་རང་སངས་རྒྱས་ཏེ། དེ་གཉིས་ནི་ཏིང་ངེ་འཛིན་མི་གཡོ་བ་དང་། གསལ་བའི་ཕྱིར་བསམ་གཏན་བཞི་པ་ཁོ་ན་ལ་བརྟེན་ཏེ་སྟན་གཅིག་ཁོ་ན་ལ་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་ནས་བཟུང་སྟེ། བྱང་ཆུབ་ཀྱི་བར་དུ་སྐྱེད་པར་བྱེད་དོ། །

[Block 2639]
བྱང་ཆུབ་ནི་ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པའི༌[^1829]ཡེ་ཤེས་ཡིན་ནོ་ཞེས་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 2640]
གཞན་དག་ན་རེ་མི་སྡུག་པ་ནས་བཟུང་སྟེ། བྱང་ཆུབ་ཀྱི་བར་དུའོ་ཞེས་ཟེར་རོ། །

[Block 2641]
གང་དག་བསེ་རུ་ལྟ་བུ་ལས་གཞན་པའི་རང་སངས་རྒྱས་ཡོད་པར་འདོད་པ་དེའི་རིགས་རྣམས་ནི་བཟློག་པར་དགག་པ་མེད་དོ། །

[Block 2642 [HEADING]]
##### ཐར་པའི་ཆ་དང་མཐུན་པ། ^3-1-3-7-0

[Block 2643]
ཅི་ཚེ་དང་པོ་ཁོ་ན་ལ་སྦྱོར་བ་བྱས་ཏེ་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་སྐྱེད་པར་བྱེད་དམ་ཞེ་ན། དེ་ལྟ་བུ་ནི་མེད་ཀྱི་ངེས་པར་དེའི་སྔོན་དུ་ཐར་པའི་ཆ་མཐུན་བསྐྱེད་པར་བྱ་དགོས་སོ། །

[Block 2644]
ཐམས་ཅད་པས་ཤིན་ཏུ། མྱུར་བའི་སྲིད་པ་གསུམ་གྱིས་ཐར། །ས་བོན་འདེབས་པ་དང་། འབྲུ་སྐྱེ་བ༌[^1830]དང་། འབྲས་བུ་ཆགས་པ་བཞིན་དུ་ཚེ་གཅིག་ལ་ནི་ཐར་པའི་ཆ་དང་མཐུན་པའི་དགེ་བའི་རྩ་བ་སྐྱེད་པར༌[^1831]བྱེད་དོ། །

[Block 2645]
གཉིས་པ་ལ་ནི་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་སྐྱེད་པར་བྱེད་དོ། །

[Block 2646]
གསུམ་པ་ལ༌[^1832]ནི་འཕགས་པའི་ལམ་སྐྱེད་པར་བྱེད་དེ། ཆོས་ཉིད་འདི་ལ་ནི་རྒྱུད་རིམ་གྱིས་འཇུག་པ་དང་། ཡོངས་སུ་སྨིན་པ་དང་། རྣམ་པར་གྲོལ་བར་འགྱུར་རོ། །

[Block 2647]
ཐར་པའི་ཆ་དང་མཐུན་པ་དེ་ཡང་ཐོས་བསམ་ལས་བྱུང་བ་ཡིན་པར་བརྗོད་དེ། བསྒོམ་པ་ལས་བྱུང་བ་ནི་མ་ཡིན་ནོ། །

[Block 2648]
ལས་དུ་དག་ཅིག་ཅེ་ན། ལས་གསུམ་མོ། །

[Block 2649]
[^1833]གཙོ་བོར་ནི་ཡིད་ཀྱི་ལས་ཡིན་ནོ། །

[Block 2650]
དེའི་སྨོན་ལམ་གྱིས་ཡོངས་སུ་བཟུང་བའི་ཕྱིར་ལུས་དང་ངག་གི་ལས་ཀྱང་ཐར་པའི་ཆ་དང་མཐུན་པ་ཡིན་ཏེ། ལ་ལ་ཞིག་གིས་ཟས་འགའ་ཙམ་བྱིན་ནས་སམ་བསླབ་པ་འགའ་ཙམ་ཡང༌[^1834]མནོས་ནས་ཐར་པ་འདོད་པའི་སྟོབས་བསྐྱེད་པས་ཐར་པའི་ཆ་དང་མཐུན་པའི༌[^1835]འཕེན་པར་འགྱུར་རོ། །

[Block 2651]
དེ་ཡང་། མི་ཡི་ནང་ནས་འཕེན་པར་བྱེད། །མི་རྣམས་ཀྱི་ནང་ཁོ་ན་དང་། གླིང་གསུམ་ནས་འཕེན་གྱི་གཞན་ནས་ནི་མ་ཡིན་ཏེ། ཅི་རིགས་པར་ཤེས་རབ་དང་སྐྱོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2652]
ཐར་པའི་ཆ་དང་མཐུན་པ་ཞར་ལས་འོངས་པ༌[^1836]བཤད་ཟིན་ཏོ། །

[Block 2653 [HEADING]]
##### མཐོང་བའི་ལམ། ^3-1-3-8-0

[Block 2654]
མངོན་པར་རྟོགས་པའི་རིམ་པ་བཤད་པར་བརྩམས་པ་དེ་ལ་ཆོས་ཀྱི་མཆོག་གི་བར་རྣམས་ནི་བཤད་ཟིན་ཏོ། །

[Block 2655]
ལྷག་མ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར།

[Block 2656 [HEADING]]
###### བདེན་པ་མངོན་པར་རྟོགས་པ་སེམས་བཅུ་དྲུག། ^3-1-3-8-1-0

[Block 2657 [VERSE]]
འཇིག་རྟེན་པ་ཡི་ཆོས་མཆོག་ལས། །
ཆོས་ཀྱི་བཟོད་པ་ཟག་པ་མེད། །

[Block 2658]
ཅེས་བྱ་བ་འདི་སྨོས་ཏེ། འཇིག་རྟེན་པའི་ཆོས་ཀྱི་མཆོག་གི་མཇུག་ཐོགས་སུ་ཆོས་ཤེས་པའི་བཟོད་པ་ཟག་པ་མེད་པ་སྐྱེའོ། །

[Block 2659]
དམིགས་པ་གང་ལ་ཞེ་ན། འདོད་སྡུག་བསྔལ་ལ། དེའི་དམིགས་པ་ནི༌[^1837]འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་ཡིན་ཏེ། དེ་ནི་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་ཞེས་བྱའོ། །

[Block 2660]
ཟག་པ་མེད་པ་ཉིད་ཡིན་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་རྒྱུ་མཐུན་པས་བྱེ་བྲག་ཏུ་བྱས་ཏེ། ཆོས་ཤེས་པའི་ཕྱིར་བཟོད་པ་ནི་ཆོས་ཤེས་པའི་བཟོད་པ་སྟེ་མེ་ཏོག་དང་འབྲས་བུའི་ཤིང་བཞིན་ནོ། །

[Block 2661]
དེ་ཉིད་ངེས་པར་འཇུག་པ་ཞེས་བྱ་སྟེ། ཡང་དག་པ་ཉིད་དུ་ངེས་པར་ཞུགས་པའི་ཕྱིར་རོ། །

[Block 2662]
ཡང་དག་པ་ཉིད་ནི་མདོ་ལས་མྱ་ངན་ལས་འདས་པ་ཡིན་པར་བཤད་དོ། །

[Block 2663]
དེར་ངེས་པ་ནི་ངེས་པ་སྟེ་གཅིག་ཏུ་གྱུར་པའོ། །

[Block 2664]
དེར་འཇུག་པ་ནི་མངོན་པར་འགྲོ་བ་སྟེ། དེ་སྐྱེས་ན་འཕགས་པའི་གང་ཟག་ཅེས་བྱའོ། །

[Block 2665]
མ་འོངས་པས་ནི་སོ་སོའི་སྐྱེ་བོ་ཉིད་ཟློག་པར་བྱེད་དོ། །
--- END BLOCKS ---
