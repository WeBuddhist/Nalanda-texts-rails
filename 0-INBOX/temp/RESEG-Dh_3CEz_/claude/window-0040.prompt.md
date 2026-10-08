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
[Block 1401]
བདེ་བ་ནི་མཚོན་བྱེད་དོན་དམ་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 1402]
འཁོར་ལོ་ནི་གཅོད་ཅིང་སྦྱོང་བས་ཤེས་རབ་སྟོང་པ་ཉིད་ཟུར་ལ་སྐྱེའོ། །

[Block 1403]
སྔོན་འགྲོ་ཞེས་པ་ཞུ་བ་ནི༌[^671]མན་ངག་གི་ཤུགས་ཀྱིས་བསྟན་པ་སྟེ༌[^672]མཚོན་བྱེད་ཀུན་རྫོབ་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 1404]
རིགས་པ་ཇི་བཞིན་རང་རིག་ནི་མཚོན་བྱེད་དབྱེར་མེད་རང་རིག་གསལ་བའོ། །

[Block 1405]
ལྷ་བྱང་ཆུབ་སེམས་ནི་མཚོན་བྱ་དོན་དམ་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 1406]
ཇི་ལྟར་འབྱུང་བ་ཞུ་བ་ནི་མཚོན་བྱ་ཀུན་རྫོབ་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 1407]
[^673]ལྷན་ཅིག་སྐྱེས་པ་རྣམ་པ་གཉིས་ནི་གཉིས་མེད་དེ་མཚོན་བྱ་ལྷན་སྐྱེས་སོ། །

[Block 1408 [VERSE]]
དེ་དག་ནི་གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པའོ། །
ཡང་ན་ནམ་མཁའི་པདྨ་ནི་ལྟེ་བའི་པདྨ་སྟོང་པའོ། །

[Block 1409]
བྷ་གའི་ཡེ་ཤེས་ནི་ཡེ་ཤེས་ཀྱི་སྐལ་བ་དང་ལྡན་པས་བྷ་ག་སྟེ་བདེ་ཆེན་གྱི་གནས་སོ། །

[Block 1410]
སྒོམ་པ་སྙོམས་འཇུག་ནི་འོག་དང་སྟེང་དུ་འོད་ཟེར་དང་། ཐིག་ལེའི་ཚུལ་དུ་རྒྱུ་བའོ། །

[Block 1411]
དེའི་བདེ་བ་ནི་འཁོར་ལོ་བཞིའི་ལམ་ནས་སོ། །

[Block 1412]
སྔོན་འགྲོ་ཞུ་བ་ནི་རྟེན་སྔོན་དུ་འགྲོ་བའི༌[^674]ཞུ་བས་སོ། །

[Block 1413]
ཇི་ལྟར་རིགས་པར་རང༌[^675]རིག་ནི་བརྟེན་པའི་ཆོས་བདེ་བ་རང་རིག་ཏུ་ཉམས་སུ་མྱོང་བའོ། །

[Block 1414]
ལྷ་བྱང་ཆུབ་སེམས་ནི་མ་ཞེན་པར་རྣམ་པར་རོལ་བའོ། །

[Block 1415 [VERSE]]
ཞུ་བ་ནི་ཡང་རྟེན་སྔོན་དུ་འགྲོ་བའོ། །
ལྷན་སྐྱེས་རྣམས་གཉིས་ནི་གཉིས་མེད་དོ། །

[Block 1416]
དེ་དག་ནི་མཚོན་བྱ་མཚོན་བྱེད་དུ་ལྷན་ཅིག་སྐྱེས་པ་ཡང་སྔ་མ་ལྟར་བཤད་དོ། །

[Block 1417]
དེ་ནི་རང་ལུས་ཐབས་ལ་བརྟེན་པའོ། །

[Block 1418]
བརྟེན་པ་ཆོས་ནས་འཇུག་པའི་ཕྱག་རྒྱ་ཆེན་པོ་ནི་ནམ་མཁའི་ཁམས་ནི་པདྨ་ཞེས་པ་ཤེས་རབ་ཀྱི་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་དུ་རྟོགས་པའོ། །

[Block 1419]
བྷ་ག་ནི་ཐབས་སྣང་བ་སྒོམ་པའོ། །

[Block 1420]
དེ་གཉིས་ཀྱིས་འཁོར་ལོ་དེ་གཙོད༌[^676]ཅིང་སྦྱོང་བར་བྱེད་དོ། །

[Block 1421]
དེ་ཁོ་ན་བྱང་ཆུབ་ཀྱི་སེམས་མོས་པ་ཙམ་དུ་བསྒོམ༌[^677]པར་བྱའོ། །

[Block 1422]
ཡང་ནམ་མཁའི་ཁམས་ནི་པདྨའི་སྐུད་པ་དང་འདྲ་བས་ན༌[^678]ཁོང་སྟོང་ཕྱག་རྒྱ་ཆེན་པོའི་རྟེན་ནོ། །

[Block 1423 [VERSE]]
བྷ་ག་ཡེ་ཤེས་ནི་དེར་ཡེ་ཤེས་རང་འབར་བའོ། །
སྒོམ་པ་སྙོམས་འཇུག་ནི་དབང་པོ་དང་བའི་ཐབས་སོ། །

[Block 1424]
དེའི་བདེ་བ་ནི༌[^679]ཐབས་སོ། །

[Block 1425 [VERSE]]
འཁོར་ལོ་ནི་ཤེས་རབ་བོ། །
སྔོན་འགྲོ་ཞུ་བ་ནི་དེའི་རྟེན་ནོ། །
རིག་པ༌[^680]རང་རིག༌[^681]ནི་དབྱེར་མེད་དོ། །

[Block 1426]
བྱང་ཆུབ་སེམས་ནི་མཚོན་བྱ་ཤེས་རབ་པོ། །ལྷ་རྣམས་ནི་ཐབས་སོ། །

[Block 1427]
འབྱུང་བ་ཞུ་བ་ནི་མཚོན་བྱའི་རྟེན་ནོ།[^682] །ལྷན་ཅིག་སྐྱེས་པ་རྣམ་པ་གཉིས་ནི་མཚོན་བྱ་དབྱེར་མེད་དོ། །

[Block 1428]
ཕྱག་རྒྱ་ཆེན་པོ་ལ་ཇི་ལྟར་མཚོན་བྱ་མཚོན་བྱེད་དུ་འགྱུར་ཞེ་ན། བླ་མའི་མན་ངག་གི་སྟོབས་སམ། ཕྱག་རྒྱ་ཆེན་པོ་དབང་བསྐུར་གྱི་ཁུ་བའི༌[^683]ཐིག་ལེ་ཀུན་རྫོབ། བདེ་བ་དོན་དམ་རང་རིག་དབྱེར་མེད། མཚོན་བྱ་ནི་རྟེན་དབང་པོ་ཁྱད་པར་ཅན་འཇའ་ཚོན་ལྟ་བུའི་ཐིག་ལེ་ནི་ཀུན་རྫོབ། ཟག་པ༌[^684]མེད་པའི་བདེ་བ་དོན་དམ། རང་རིག་མཚན་ཉིད་གསུམ་དང་ལྡན་པ་གསུམ་དང་བྲལ་བ་དབྱེར་མེད་པ་རང་འབྱུང་གི་ཡེ་ཤེས་སོ། །

[Block 1429]
བཤད་པ་དེ་རྣམས་ནི་སྐབས་འདིར་ལྷན་ཅིག་སྐྱེས་པ་གཏན་ལ་དབབ་པར་ཡང་འགྲོའོ། །

[Block 1430]
སྒོམ་པར་ཡང་འགྲོ་སྟེ་སྔོན་དུ་འགྲོ་བ་དང་། རྟགས་རྣམས་སྔ་མ་བཞིན་དུ་སྦྱོར༌[^685]རོ། །

[Block 1431 [HEADING]]
##### དབྱེ་བའི་རྣམ་པར་གཞག་པ། ^1-8-6-2-0

[Block 1432]
ད་ནི་དབྱེ་བའི་རྣམ་པར་གཞག་པ༌[^686]བསྟན་པའི་ཕྱིར།

[Block 1433 [VERSE]]
ཚིགས་སུ་བཅད་པ་གཉིས་ཏེ་གོ་སླའོ། །
དེ་ཉིད་ཕྱིར་ན་ཞེས་པ་ནི།
ལྷན་ཅིག་སྐྱེས་པ་དབྱེ་བའི་ཕྱིར། །
དགའ་བ་བཞི་ཡི་རབ་དབྱེ་བ། །

[Block 1434]
ཞེས་པ་ནི་དགའ་བ་ལ་ཡང་བཞིར་དབྱེ་བའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། རྫོགས་པའི་རིམ་པའི་ཕྱོགས་ལས་ཞེས་པ་སྟེ༌[^687]དེའི་དབང་དུ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1435]
འདི་ལྟར།[^688] ལྷན་ཅིག་སྐྱེས་པ་རྣམ་པ་བཞི། །ཞེས་པ་ནི། ལྷན་ཅིག་སྐྱེས་པ་དང་དགའ་བ་ངོ་སྦྱར་བའོ། །

[Block 1436 [VERSE]]
དེ་དག་ཇི་ལྟར་ཞེ་ན། །
དགའ་བ་ལས་ནི་དང་པོའོ། །

[Block 1437]
དཔའ་བོ༌[^689]ཉིད་ནི་སྐྱེས་བུ་ཐབས་ཀྱི་ལྷན་སྐྱེས་སོ། །

[Block 1438]
མཆོག་ཏུ་དགའ་བ་གཉིས་པའོ། །

[Block 1439 [VERSE]]
རྣལ་འབྱོར་མའི་བཙུན་མོ་ཤེས་རབ་ཀྱི་ལྷན་སྐྱེས་སོ། །
ཤིན་ཏུ་བདེ་དགའ་ནི་དགའ་བྲལ་གྱི་གསུམ་པའོ། །
ཐམས་ཅད༌[^690]དེས་ནི་ཀུན་རྫོབ༌[^691]མཚོན་བྱེད་ལྷན་སྐྱེས་སོ། །

[Block 1440]
དེ་བདེ་ཐབས་ལས་ནི་དགའ་བས་ལྷན་སྐྱེས་ཏེ་བཞི་པའོ། །
--- END BLOCKS ---
