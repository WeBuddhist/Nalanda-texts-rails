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
[Block 2696]
དེ་དག་ཉིད་ལས་ཀུན་འབྱུང་བ་མཐོང་བས་སྤོང་བར༌[^1070]བྱ་བ་བདུན་དང་། འགོག་པ་མཐོང་བས་སྤོང་བར༌[^1071]བྱ་བ་བདུན་ཏེ། འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། ཚུལ་ཁྲིམས༌[^1072]དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་མ་གཏོགས་སོ། །

[Block 2697]
ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་བརྒྱད་དེ། འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། མཐར་འཛིན་པར་ལྟ་བ་མ་གཏོགས་སོ། །

[Block 2698]
དེ་ལྟར་ན༌[^1073]འདོད་པ་ན་སྤྱོད་པའི་ཕྲ་རྒྱས་སུམ་ཅུ་རྩ་གཉིས་ཡིན་ནོ། །

[Block 2699]
དེ་བཞིན་དུ་གཟུགས་ཀྱི་ཁམས་ན་ཉི་ཤུ་རྩ་བརྒྱད། གཟུགས་མེད་པའི་ཁམས་ན་ཉི་ཤུ་རྩ་བརྒྱད་ཡིན་ནོ། །

[Block 2700]
འདོད་པའི་ཁམས་ན་མཐོང་བས་སྤོང་བར༌[^1074]བྱ་བ་སོ་གཉིས་ཡིན་ལ། བཞི་ནི་བསྒོམ་པས་སྤང༌[^1075]བྱ་ཡིན། །འདི་ལྟ་སྟེ། འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། མ་རིག་པ་དང་། ང་རྒྱལ་ཏོ། །

[Block 2701]
[^1076]དེ་དག་ནི་འདོད་པ་ན་སྤྱོད་པའི་སུམ་ཅུ་རྩ་དྲུག་ཏུ་འགྱུར་རོ། །

[Block 2702]
ཁོང་ཁྲོ༌[^1077]མ་གཏོགས་དེ་དག་ཉིད། །གཟུགས་ཁམས། ཁོང་ཁྲོ་བ་རྣམ་པ་ལྔ་བོར་ནས་གཟུགས་སུ་གཏོགས་པའི་ཕྲ་རྒྱས་སུམ་ཅུ་རྩ་གཅིག་ཡིན་ནོ། །

[Block 2703]
གཟུགས་མེད་དེ་དང་འདྲ།

[Block 2704 [VERSE]]
སུམ་ཅུ་རྩ་གཅིག་ཁོ་ནའོ། །
དེ་ལྟར་དགུ་བཅུ་བརྒྱད་དུ་འདོད། །

[Block 2705]
དེ་ལྟར་ན་དེ་དག་རྣམ་པ་དང་བྱེ་བྲག་དང་ཁམས་ཀྱི་དབྱེ་བས་དགུ་བཅུ་རྩ་བརྒྱད་དུ་འདོད་དོ། །

[Block 2706]
དེ་བས་ན།

[Block 2707 [VERSE]]
སྲིད་རྩེ་ལས་སྐྱེས་བཟོད་པ་ཡིས། །
གཞོམ་བྱ་མཐོང་བས་སྤང་བྱ་ཉིད། །

[Block 2708]
བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་ནི་མ་ཡིན་ནོ། །

[Block 2709]
ལྷག་སྐྱེས་མཐོང་དང་བསྒོམ་གཉིས་ཀྱིས། །བཟོད་པས་གཞོམ་པར་བྱ་བ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ས་ལྷག་མ་དག་གི་ཆོས་དང་རྗེས་སུ་མཐུན་པའི་བཟོད་པས་སྤང་བར་བྱ་བ་རྣམས་ནི་ཅི༌[^1078]རིགས་པར་འཕགས་པ་རྣམས་ཀྱིས་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་ཡིན་ལ། སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱིས་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་གོ། །

[Block 2710]
བཟོད་པས་གཞོམ་མིན་བསྒོམ་ཁོ་ནས། །ས་གང་དག་ཕྲ་རྒྱས་གང་དག་ཤེས་པས་གཞོམ་པར་བྱ་བ་ཡོད་པས་དེ་དག་ནི་གཉིས་ཀའི་ཡང་རྟག་ཏུ་བསྒོམ་པས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 2711 [HEADING]]
### ལྟ་བ་ལྔའི་ངོ་བོ། ^5-2-0

[Block 2712]
ལྟ་བ་ལྔ་མིང་གི་སྒོ་ནས་བསྟན་གྱི་རང་གི་ངོ་བོའི་སྒོ་ནས་མ་བསྟན་པས་དེའི་ཕྱིར་དེའི་ངོ་བོ་བརྗོད་པར་བྱ་སྟེ།

[Block 2713 [VERSE]]
བདག་དང་བདག་གི་རྟག་ཆད་དང་། །
མེད་དང་དམན་ལ་མཆོག་ལྟ་དང་། །
རྒྱུ་མིན་ལམ་མིན་དེར་ལྟ་བ།[^1079] །
དེ་དག་ལྟ་བ་ལྔ་ཡིན་ནོ། །

[Block 2714]
བདག་དང་བདག་གིར་ལྟ་བ་ནི་འཇིག་ཚོགས་ལ་ལྟ་བའོ། །

[Block 2715]
བདག་ཏུ་མངོན་པར་འདོད་པའི་དངོས་པོ་དེ་ཉིད་ལ་རྟག་པར་ལྟ་བའམ་ཆད་པར་ལྟ་བ་ནི་མཐར་འཛིན་པའི་ལྟ་བའོ། །

[Block 2716]
སྡུག་བསྔལ་ལ་སོགས་པའི་བདེན་པ་ཡོད་ན་མེད་དོ་ཞེས་བྱ་བའི་ལྟ་བ་ནི་ལོག་པར་ལྟ་བའོ། །

[Block 2717]
དམན་པ་ཟག་པ་དང་བཅས་པ་ལ་མཆོག་ཏུ་ལྟ་བ་ནི་ལྟ༌[^1080]བ་མཆོག་ཏུ་འཛིན་པའོ། །

[Block 2718]
རྒྱུ་མ་ཡིན་པ་ལ་རྒྱུར་ལྟ་བ་དང་། ལམ་མ་ཡིན་པ་ལ་ལམ་དུ་ལྟ་བ་ནི་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པའོ། །

[Block 2719]
གཉིས་ཀ་ལ་ཡང་ལ་སོགས་པའི་སྒྲ་མི་མངོན་པར་བྱས་སོ། །

[Block 2720]
གལ་ཏེ་རྒྱུ་མ་ཡིན་པ་རྒྱུར་ལྟ་བ་དང་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་ཡིན་ནོ།[^1081] །

[Block 2721]
ཅིའི་ཕྱིར་ཀུན་འབྱུང་མཐོང་བས་སྤོང་བར༌[^1082]བྱ་བ་མ་ཡིན་ཞེ་ན། གང་ལས་དབང་ཕྱུག་གམ་སྐྱེ་དགུའི་བདག་པོ་ལ་རྒྱུར་ལྟ་བ་དེ་ནི་དེ་ལ་རྟག་པ་དང་གཅིག་བུ་དང་བདག་བྱེད་པ་པོར་མངོན་པར་ཞེན་ནས་ལྟ་སྟེ། དེ་ལྟ་བས་ན་འདི་ལྟར། དབང་ཕྱུག་སོགས་རྒྱུར་མངོན་ཞེན་པ། དེ་ནི།

[Block 2722 [VERSE]]
རྟག་བདག་ཕྱིན་ཅི་ལོག་པ་ཡིས། །
རབ་ཏུ་འཇུག་པས་དེའི་ཕྱིར་དེ། །
སྡུག་བསྔལ་མཐོང་བས་སྤང་བྱ་ཉིད། །

[Block 2723]
དེ་ལ་རྟག་པ་དང་བདག་ཏུ་འཛིན་པ་དེ་གཉིས་ནི་སྡུག་བསྔལ་མཐོང་བ་ཁོ་ནས་སྤོང་བར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་དེ་བྱས་པ་རྒྱུར་མངོན་པར་ཞེན་པ་ཡང་དེ་ཉིད་ཀྱིས་སྤོང་བར་འགྱུར་རོ། །

[Block 2724 [HEADING]]
#### ཕྱིན་ཅི་ལོག་བཞི། ^5-2-1-0

[Block 2725]
རྟག་བདག་ཕྱིན་ཅི་ལོག་པ་ཡིས། །ཞེས་གང་བཤད་པ་ཕྱིན་ཅི་ལོག་དེ་གཉིས་ཁོ་ནར་ཟད་དམ་ཞེ་ན། མ་ཡིན་ཏེ། འོན་ཀྱང་ཕྱིན་ཅི་ལོག་ནི་བཞི་སྟེ། དེ་ནི། ལྟ་བ་གསུམ་ལས༌[^1083]ཕྱིན་ཅི་ལོག །བཞི་ཚན།[^1084] མཐར་འཛིན་པར་ལྟ་བ་ལས་རྟག་པར་ལྟ་བ་ནི་རྟག་པར་ཕྱིན་ཅི་ལོག་གོ། །

[Block 2726]
ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་ལས་ནི་བདེ་བ་དང་གཙང་བར་ཕྱིན་ཅི་ལོག་གོ། །

[Block 2727]
འཇིག་ཚོགས་ལ་ལྟ་བ་ལས་ནི་བདག་ཏུ་ལྟ་བར་ཕྱིན་ཅི་ལོག་གོ། །

[Block 2728]
ཅིའི་ཕྱིར་ཉོན་མོངས་པ་གཞན་དག་ཕྱིན་ཅི་མ་ལོག་མ་ཡིན་ཞེ་ན། འདི་ལྟར་རྒྱུ་གསུམ་གྱིས་ཕྱིན་ཅི་ལོག་རྣམ་པར་གཞག་པ་འདི་ལྟ་སྟེ། ཕྱིན་ཅི་ལོག་ཕྱིར་དང་། དེས་རྟོག་ཕྱིར་དང་སྒྲོ་འདོགས་ཕྱིར། །ཆད་པར་ལྟ་བ་དང་། ལོག་པར་ལྟ་བ་ནི་སྒྲོ་འདོགས་པ་དག་མ་ཡིན་ནོ། །

[Block 2729]
ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་ནི་གཅིག་ཏུ་ཕྱིན་ཅི་ལོག་མ་ཡིན་ནོ། །

[Block 2730]
ཉོན་མོངས་པ་གཞན་དག་ནི་ངེས་པར་རྟོག་པར་བྱེད་པ་མ་ཡིན་པས་ཕྱིན་ཅི་ལོག་མ་ཡིན་ནོ། །

[Block 2731]
མདོ་ལས་འདུ་ཤེས་དང་། སེམས་དང་། ལྟ་བ་ཕྱིན་ཅི་ལོག་ཏུ་གསུངས་པ་དེ་ལ་ལྟ་བ་ཁོ་ན་ཕྱིན་ཅི་ལོག་ཡིན་ལ། སེམས་དང་འདུ་ཤེས་དེའི་དབང་གིས། །ལྟ་བ་ཕྱིན་ཅི་ལོག་གི་དབང་གིས་འདུ་ཤེས་དང་སེམས་ཕྱིན་ཅི་ལོག་ཏུ་བཤད་དོ། །

[Block 2732 [HEADING]]
### ང་རྒྱལ་བདུན། ^5-3-0

[Block 2733]
ཡང་ལྟ་བའི་ཕྲ་རྒྱས་ཁོ་ན་ལ་དབྱེ་བ་ཡོད་ཀྱི་གཞན་ལ་མེད་དམ་ཞེ་ན། ཡོད་པ་འདི་ལྟ་སྟེ། ང་རྒྱལ་བདུན། ང་རྒྱལ་དང་། ལྷག་པའི་ང་རྒྱལ་དང་། ང་རྒྱལ་ལས་ཀྱང་ང་རྒྱལ་དང་། ངའོ་སྙམ་པའི་ང་རྒྱལ་དང་། མངོན་པའི་ང་རྒྱལ་དང་། ཅུང་ཟད་སྙམ་པའི་ང་རྒྱལ་དང་། ལོག་པའི་ང་རྒྱལ་ལོ། །

[Block 2734]
དེ་ལ་ཆུང་ངུ་ལས་བདག་ཁྱད་པར་དུ་འཕགས་པའམ་མཉམ་པ༌[^1085]དང་མཉམ་མོ་སྙམ་དུ་སེམས་ཁེངས་པ་ནི་ང་རྒྱལ་ལོ། །

[Block 2735]
མཉམ་པ་བས་བདག་ཁྱད་པར་དུ་འཕགས་སོ་སྙམ་པ་ནི་ལྷག་པའི་ང་རྒྱལ་ལོ། །
--- END BLOCKS ---
