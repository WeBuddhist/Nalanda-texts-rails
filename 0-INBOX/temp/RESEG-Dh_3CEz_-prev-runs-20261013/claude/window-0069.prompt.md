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
[Block 2416]
ཡང་གནས་ནི་དེ་ཡང་ལུས་རྫོགས་པའི་རིམ་པའོ། །

[Block 2417]
དེ་ནས་མཆོག་ཏུ་བདེ་བར་འབྲེལ་ཏེ་གཟུགས་མེད་པ་ནི་སེམས་སོ། །

[Block 2418 [VERSE]]
དེའི་ཕྱིར་ནི༌[^1051]ཆོས་ཉིད་བདེ་བ་ཡིན་པས་སོ། །
འགྲོ་ཀུན་ནི་སེམས་ཅན་ཀུན་ནོ། །

[Block 2419 [VERSE]]
ལྷན་ཅིག་སྐྱེས་པ་ནི་དབྱེར་མེད་པའི་བདེ་བའོ། །
དེའི་ཕྱིར་རང་བཞིན་ལྷན་ཅིག་སྐྱེས་པར་བརྗོད་དོ། །

[Block 2420]
རྣམ་དག་སེམས་ནི་དགའ༌[^1052]བའོ། །

[Block 2421]
རང་བཞིན་མྱ་ངན་ལས་འདས་པ་ནི་རྟོག་པ་སྟེ་སངས་རྒྱས་ཁོ་ནའོ།[^1053] །དེས་ནི་འདི་སྐད་སྟོན་ཏེ་ལུས་སེམས་ལྷན་ཅིག་སྐྱེས་པའི་རང་བཞིན་དུ་བསྟན་ཏོ། །

[Block 2422]
དེའི་ཕྱིར་འོན་ཀྱང་ཞེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པ་དེ་ལྟར་མིན་ཡང་ཞེས་པའོ། །

[Block 2423]
བག་ཆགས་ཕལ་པ་ནི་སྤྲིན་དང་ཁུ་རླངས་ལྟ་བུར་གློ་བུར་དུ་མངོན་པར་ཞེན་པའོ། །

[Block 2424]
ད་ནི་སྤང་བའི་ཚུལ་ཉམས་སུ་བླང་བའི་ཐབས་བསྟན་པའི་ཕྱིར། །དུག་གི༌[^1054]དུམ་བུ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཅིག་གིས་ལྟ་བ་ཤེས་རབ་ཀྱིས་སྤྲོ་བ་དང་མཚན་མས་སྤྲོས༌[^1055]པའི་དཔེ་སྟེ་དེ་ཡང་མུ་སྟེགས་སུ་འབྲེལ། དེ་ཡང་རྟག་ཆད་ཀྱི་སྤྲོས་པ་དུག་གི་དེ་ཉིད་ཤེས་པ་མི་གནོད་ལ་མ་ཤེས་ན་གནོད་པ་སྟེ། དེའི་ཕྱིར་མུ་སྟེགས་ཀྱིས་མི་ཤེས་པའོ། །

[Block 2425]
ཇི་ལྟར་རླུང་གིས་ཟིན་པ་ཞེས་པ་ནི་དབྱེར་མེད་སྤྱོད་པས་སྤྲོས་པའི་དཔེ་སྟེ། མི་གཙང་བ་དང་མི་དགེ་བས་ཟིན་པའོ། །

[Block 2426]
མོན་སྲན་སྟེར་བ་ནི་མི་གཙང་བ་དང་མི་དགེ་བ་ལ་སྤྱོད་དུ་འཇུག་པ་སྟེ་བཟློག་པའི་སྨན་གཉེན་པོའི་སྨན་ཡིན་པས་སོ། །

[Block 2427]
རླུང་གིས་རླུང་ལ་བསྣུན་པ་ནི་མི་མཐུན་པ་ལ་སྤྱོད་པས་མི་མཐུན་པ་ལྡོག་པའོ། །

[Block 2428]
དེ་ནས་སངས་རྒྱས་སུ་འབྲེལ་ཏེ་སངས་རྒྱས་པའི་ཉན་ཐོས་པ་དང་རང་རྒྱལ་གྱིས༌[^1056]མི་ཤེས་པའོ། །

[Block 2429]
རྣམ་རྟོག་ལས་ནི་ཞེས་པ་ནི་དབྱེར་མེད་འབྲས་བུ་སྤོང་བ་སྟེ་དེ་ཡང་རྣམ༌[^1057]རྟོག་སྤོང་བ་སྟེ། སྲིད་པས་སྲིད་པ་དག་པའི་ཕྱིར་རོ། །

[Block 2430]
རྟོག་པ་དང་བརྟགས་པས་མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་ཐོབ་པའོ། །

[Block 2431]
ཇི་ལྟར་རྣ་བར་ཆུ་ཞུགས་པ་འཁོར་བར་ཞུགས་པའི་དཔེའོ། །

[Block 2432]
ཆུ་གཞན་གྱིས་དགུག་པ་ནི་འཁོར་བ་ཉིད་འབྲས་བུར་གྱུར་པའི་དཔེའོ། །

[Block 2433]
དེ་བཞིན་དངོས་པོའི་རྣམ་རྟོག་ནི་དཔེ་ལས་བྱུང་བ་སྟེ། བརྟགས་པ་འཁོར་བ་སྤང་ངོ་། །རྣམ་པར་ངེས་པར་སྤོང་བར༌[^1058]བྱ་བ༌[^1059]ནི་འབྲས་བུ་ངེས་པར་འགྱུར་བ་ལ་མཁས་པའོ། །

[Block 2434]
ཡང་སངས་རྒྱས་སུ་འབྲེལ་ན་ནི་བསྐལ་པ་དུ་མར་སྦྱོང་བས་མི་ཤེས་སོ། །

[Block 2435]
ཇི་ལྟར་མི་ཤེས་པ་ནི་ཉོན་མོངས་ཐམས་ཅད་སྒོམ་པས་སྤོང་བ་སྟེ། མེ་ཡིས་ཡང་ནི༌[^1060]གདུང་བ་སྟེ་ནི་རིམ་གྱིས་བསྲུང་བའི་ཐབས་སོ། །

[Block 2436]
དེ་བཞིན་འདོད་ཆགས་ནི་དཔེ་ལས་འབྱུང་བའོ། །

[Block 2437]
འདོད་ཆགས་འདུལ་བ་ནི་རིམ་གྱིས་དལ་བུས་ཞུ་བ་དེ་ཆགས་པའི་ཆ་རྟོགས་པའི་མན་ངག་གོ། །

[Block 2438]
སངས་རྒྱས་པས་མི་ཤེས་པ་ནི་བྱ་བ་དང་སྤྱོད་པ་དང་རྣལ་འབྱོར་གྱི་རྒྱུད་ཀྱིས་སོ། །

[Block 2439]
ད་ནི་བསྡུས་ཏེ་ཆེ་བའི་བདག་ཉིད་བསྟན་པའི་ཕྱིར། སྐྱེ་བོ་མི་བཟང་པའི་ལས་ནི་བླ་མ་འཕགས་པ་དང་འདྲ་བའི་ཆོས་མ་ཐོབ་པས་སོ། །

[Block 2440]
གང་དང་གང་གི༌[^1061]སྤྱིར་ཉོན་མོངས་པ་དང་མཚུངས་པར་ལྡན་པའི་སེམས་སོ། །

[Block 2441]
འཆིང་འགྱུར་ནི་གནོད་པའོ། །

[Block 2442 [VERSE]]
ཐབས་ནི་རྗེས་སུ་བརྒྱུད་པའི༌[^1062]ཚུལ་ལོ། །
དེ་ཉིད་ལས་དང་ཉོན་མོངས་པའོ། །

[Block 2443 [VERSE]]
ཡང་ན་ལྟ་བ་ལ་སོགས་པའི་དེ་ཉིད་དོ། །
སྲིད་པའི་འཆིང་བ་ནི་འཁོར་བར་སྐྱེ་བའི་རྒྱུའོ། །
གྲོལ་བ་ནི་དེའི་ནུས་པ་འཇོམས་པའོ། །

[Block 2444]
ཡང་ན་ཐབས་ནི་བསྒོམ་པའོ། །

[Block 2445]
བཅས་པ་ནི་ལྟ་བའོ། །

[Block 2446]
དེ་ཉིད་ནི་སྤྱོད་པའོ། །

[Block 2447]
སྲིད་པ་ནི་འཆིང་བ་ལས་གྲོལ་བའོ། །

[Block 2448]
དེ་དག་གིས་སྤྱིར་བསྟན་ནས་སྒོམ་པ་ཁྱད་པར་དུ་བསྟན་པའི་ཕྱིར།

[Block 2449 [VERSE]]
ཆགས་པ་ཞེས་པ་ནི་ཐ་མལ་པའོ། །
འཇིག་རྟེན་འཆིང་བ་ནི་ལོ་ཀ་སྟེ།
ཕྱི་མ་ལ་གནོད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །
འདོད་ཆགས་ཉིད་རྗེས་སུ་ཆགས་པའི་སྒོམ་པའོ། །

[Block 2450]
རྣམ་གྲོལ་ནི་དེ་ཁོ་ན་ཉིད་ལ་མོས་པ་ཙམ་ནི་མ་ཡིན་གྱི།[^1063] ལྷན་ཅིག་སྐྱེས་པའི་རང་གི་མཚན་ཉིད་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 2451]
བཟློག་པའི་སྒོམ་པ་ཉིད་ནི་མཚོན་པ་སྟེ། སྒོམ་པ་དང་སྤྱོད་པ་ལ་བརྗོད་དུ་ཟིན་ཀྱང་ལྟ་བ་དང་འབྲས་བུ་ལ་ཡང་ངོ་། །ད་ནི་འབྲས་བུ་བསྟན་པའི་ཕྱིར། ཀུན་དུ་རུ་ལས་ཞེས་པ་སྟེ། དགའ་བ་ཆེན་པོ་གཅིག་ཉིད་ནི་ཞུ་བ་ཞེས་པའོ། །

[Block 2452]
ཚིགས་སུ་བཅད་པ་གཅིག་སྟེ་གོ་སླའོ། །

[Block 2453]
དེའི་བཤད་པ་ཡང་ཚིགས་སུ་བཅད་པ་ལྔ་སྟེ་གོ་སླའོ། །

[Block 2454]
ལུས་ལྷན་ཅིག་སྐྱེས་པའི་འབྲས་བུར་བསྟན་ནས་སེམས་བསྟན་པའི་ཕྱིར།[^1064] སེམས་ནི་ཆེན་པོ་ཉིད་ནི་སྔར་གྱི་དགའ་བ་ཆེན་པོ་སྟེ།

[Block 2455 [VERSE]]
དེ་ནས་བདེ་ཆེན་མཆོག་ཏུ་ཡང་འབྲེལ་ལོ། །
འདོད་ཆགས་ལ་སོགས་སེམས་ལྔ༌[^1065]ནི༌[^1066]ཉོན་མོངས་པའི་གནས་སྐབས་སོ། །
དབྱེ་བ་ནི་ཆེ་ལོང་དུ་དབྱེ་བས་སོ། །
--- END BLOCKS ---
