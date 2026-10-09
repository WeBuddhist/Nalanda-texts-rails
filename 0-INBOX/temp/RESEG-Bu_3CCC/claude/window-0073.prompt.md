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
[Block 2556]
སྟོང་པ་ཉིད་བཟུང༌[^1649]ན་ཆོས་མ་ཡིན་པ་དང་ཆོས་ཉིད་དང་དེ་དག་གིས་བྱས་པའི་འབྲས་བུ་ཡོད་པ་དང་འཇིག་རྟེན་པའི་ཐ་སྙད་ཀུན་ལ་ཡང་གནོད་པ་བྱེད་པ་ཡིན་པས་དེ་ལྟ་བས་ན་དངོས་པོ་ཐམས་ཅད་སྟོང་པ་མ་ཡིན་ནོ། །

[Block 2557 [VERSE]]
དེ་ལ་བཤད་པ་ཁྱོད་ཀྱིས་ནི། །
སྟོང་ཉིད་དགོས་དང་སྟོང་ཉིད་དང་། །
སྟོང་ཉིད་དོན་ནི་མ་རྟོགས༌[^1650]པས། །
དེ་ཕྱིར་དེ་ལྟར་གནོད་པ་བྱེད། །

[Block 2558]
ཁྱོད་ཀྱིས་ནི་སྟོང་པ་ཉིད་བསྟན་པའི་དགོས་པ་གང་ཡིན་པ་དང་། སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་གང་ཡིན་པ་དང་སྟོང་པ་ཉིད་ཀྱི་དོན་གང་ཡིན་པ་དེ་དག་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་མ་རྟོགས༌[^1651]པ་དེའི་ཕྱིར་དེ་ལྟར་གནོད་པ་བྱེད་དོ། །

[Block 2559 [VERSE]]
སངས་རྒྱས་རྣམས་ཀྱིས༌[^1652]ཆོས་བསྟན་པ། །
བདེན་པ་གཉིས་ལ་ཡང་དག་བརྟེན། །
འཇིག་རྟེན་ཀུན་རྫོབ་པ༌[^1653]བདེན༌[^1654]དང་། །
དམ་པའི་དོན་གྱི་བདེན་པའོ། །

[Block 2560 [VERSE]]
གང་དག་བདེན་པ་དེ་གཉིས་ཀྱི། །
རྣམ་དབྱེ་རྣམ་པར་མི་ཤེས་པ། །
དེ་དག་སངས་རྒྱས་བསྟན་པ་ནི། །
ཟབ་མོའི་དེ་ཉིད་རྣམ་མི་ཤེས། །

[Block 2561]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱིས༌[^1655]ཆོས་བསྟན་པ་ནི་བདེན་པ་གཉིས་པོ་འདི་དག་ལ་བརྟེན་ནས་འབྱུང་སྟེ། འཇིག་རྟེན་པའི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་ངོ་བོ་ཉིད་སྟོང་པ་དག་ལ་འཇིག་རྟེན་གྱིས་ཕྱིན་ཅི་ལོག་མ་རྟོགས་པས་ཆོས་ཐམས་ཅད་སྐྱེ་བར་མཐོང་བ༌[^1656]གང་ཡིན་པ་སྟེ། དེ་ནི་དེ་དག་ཉིད་ལ་ཀུན་རྫོབ་ཏུ་བདེན་པ་ཉིད་ཡིན་པས་ཀུན་རྫོབ་ཀྱི་བདེན་པའོ། །

[Block 2562]
དོན་དམ་པའི་བདེན་པ་ནི་འཕགས་པ་རྣམས་ཀྱིས་ཕྱིན་ཅི་ལོག་ཏུ༌[^1657]ཐུགས་སུ་ཆུད་པས་ཆོས་ཐམས་ཅད་སྐྱེ་བ་མེད་པར་གཟིགས་པ་གང་ཡིན་པ་སྟེ་དེ་ནི་དེ་དག་ཉིད་ལ་དོན་དམ་པར་བདེན་པ་ཉིད་ཡིན་པས་དོན་དམ་པའི་བདེན་པའོ། །

[Block 2563]
དེ་ལ་གང་དག་ཀུན་རྫོབ་ཀྱི་བདེན་པ་དང་དོན་དམ་པའི་བདེན་པ་དེ་གཉིས་ཀྱི་རྣམ་པར་དབྱེ་བ༌[^1658]རྣམ་པར་མི་ཤེས་པ་དེ་དག་ནི་སངས་རྒྱས་ཀྱི་བསྟན་པ་ཟབ་མོའི་དེ་ཉིད་རྣམ་པར་མི་ཤེས་པ་ཡིན་ནོ། །

[Block 2564]
འདི་ལ་འདི་སྙམ་དུ་སྨྲ་བར་འདོད་པའི་དོན་ནི་ཆོས་ཐམས་ཅད་སྐྱེ་བ་མེད་པ་ཞེས་བྱ་བའི་དོན་དམ་པའི་བདེན་པ་དེ་ཉིད་ཡིན་ན། ཐ་སྙད་ཀྱི་བདེན་པ་གཉིས་པ་འདི་ཅི་དགོས་སྙམ་དུ་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 2565 [VERSE]]
ཐ་སྙད་ལ་ནི་མ་བརྟེན་པར། །
དམ་པའི་དོན་ནི་བསྟན་མི་ནུས། །
དམ་པའི་དོན་ལ་མ་བརྟེན་པར། །
མྱ་ངན་འདས་པ་ཐོབ་མི་འགྱུར། །

[Block 2566]
གང་གི་ཕྱིར་ཐ་སྙད་ལ་མ་བརྟེན་པར་དོན་དམ་པ་བསྟན་པར་མི་ནུས་པ་དང་། གང་གི་ཕྱིར་དོན་དམ་པ་ལ་མ་བརྟེན་པར་མྱ་ངན་ལས་འདས་པ་འཐོབ་པར་མི་འགྱུར་བ། དེའི་ཕྱིར་བདེན་པ་གཉིས་ཀ༌[^1659]གདགས་དགོས་སོ། །

[Block 2567 [VERSE]]
སྟོང་པ་ཉིད་ལ་ལྟ་ཉེས་ན། །
ཤེས་རབ་ཆུང་རྣམས་ཕུང་བར་བྱེད། །
ཇི་ལྟར་སྦྲུལ་ལ་བཟུང༌[^1660]ཉེས་དང་། །
རིག་སྔགས་ཉེས་པར་བསྒྲུབ་པ་བཞིན། །

[Block 2568]
དོན་དམ་པ་སྟོང་པ་ཉིད་ལ་ལྟ་ཉེས་ན༌[^1661]ཤེས་རབ་ཆུང་ངུ་དང་ལྡན་པ་ཕུང་བར་བྱེད་ཅིང་དེ་ལ་གནོད་པ་ཆེན་པོ་འབྱུང་བར་འགྱུར་ཏེ། ཇི་ལྟར་དཔེར་ན་སྦྲུལ་ལ་བཟུང་ཉེས་ན་ཕུང་བར་བྱེད་ཅིང་དེ་ལ་འཆི་བ་ལ་ཐུག་པའི་ཉེན་ཆེན་པོ་སྐྱེད་པར་བྱེད་པ་དང་། ཇི་ལྟར་དཔེར་ན་རིག་སྔགས་དང་གསང་སྔགས་བྱ་བ་དང་ཆོ་ག་ཉམས་པས་བསྒྲུབས༌[^1662]ཉེས་ན་ཕུང་བར་བྱེད་ཅིང་དེ་ལ་སྲོག་གི་མཐར་ཐུག་པའི་ཉེན་ཆེན་པོ་སྐྱེད་པར་བྱེད་པ་དེ་བཞིན་ནོ། །

[Block 2569 [VERSE]]
དེ་ཕྱིར་ཞན་པས་ཆོས་འདི་ཡི། །
གཏིང་རྟོགས་དཀའ་བར་མཁྱེན་གྱུར་ནས། །
ཐུབ་པའི་ཐུགས་ནི་ཆོས་བསྟན་ལས། །
རབ་ཏུ་ལོག་པར་གྱུར་པ་ཡིན། །

[Block 2570]
རྒྱུ་དེ་ཁོ་ནའི་ཕྱིར་ཤེས་རབ་ཞན་པ་རྣམས་ཀྱིས་ཆོས་འདིའི་གཏིང་རྟོགས་པར་དཀའ་བ་ཉིད་དུ་མཁྱེན་པར་གྱུར་ནས་བཅོམ་ལྡན་འདས་ཀྱི་ཐུགས་ཆོས་བསྟན་པ་ལས༌[^1663]རབ་ཏུ་ལོག་པར་གྱུར་པ་ཡིན་ནོ། །

[Block 2571 [VERSE]]
ཁྱོད་ནི་ང་ལ་སྟོང་པ་ཉིད། །
སྐྱོན་དུ་ཐལ་བར་འགྱུར་བ་ཡིས། །
སྤོང་བར་བྱེད་པ་གང་ཡིན་པ། །
དེ་ནི་སྟོང་ལ་མི་འཐད་དོ། །

[Block 2572]
ཁྱོད་ང་ལ་སྟོང་པ་ཉིད་སྐྱོན་དུ་ཐལ་བར་འགྱུར་བས་སྤོང་བར༌[^1664]བྱེད་པ་གང་ཡིན་པ་དེ་ནི་ངོ་བོ་ཉིད་སྟོང་པ་ལ་མི་འཐད་དོ། །

[Block 2573]
ཡང་གཞན་ཡང་།

[Block 2574 [VERSE]]
གང་ལ་སྟོང་པ་ཉིད་རུང་བ། །
དེ་ལ་ཐམས་ཅད་རུང་བར་འགྱུར། །
གང་ལ་སྟོང་ཉིད་མི་རུང་བ། །
དེ་ལ་ཐམས་ཅད་རུང༌[^1665]མི༌[^1666]འགྱུར། །

[Block 2575]
གང་ལ་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་རུང་བ་དེ་ལ་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པ་ཐམས་ཅད་རུང་བར་འགྱུར་རོ། །

[Block 2576]
གང་ལ་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་མི་རུང་བ་དེ་ལ་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པ་ཐམས་ཅད་མི་རུང་བར་འགྱུར་རོ། །

[Block 2577 [VERSE]]
ཁྱོད་ཉིད་རང་གི་སྐྱོན་རྣམས་ནི། །
ང་ལ་ཡོངས་སུ་སྒྱུར་བྱེད་པ། །
རྟ་ལ་མངོན་པར་ཞོན་བཞིན་དུ། །
རྟ་ཉིད་བརྗེད༌[^1667]པར་གྱུར་པ་བཞིན། །

[Block 2578]
ཁྱོད་ཉིད་རང་གི་སྐྱོན་རྣམས་ང༌[^1668]ལ་ཡོངས་སུ་སྒྱུར་བར༌[^1669]བྱེད་པ་ནི་རྟ་ལ་མངོན་པར་ཞོན་བཞིན་དུ་རྟ་དེ་ཉིད་བརྗེད་པར༌[^1670]འགྱུར་བ༌[^1671]བཞིན་ནོ། །

[Block 2579]
ཡང་གཞན་ཡང་།

[Block 2580 [VERSE]]
གལ་ཏེ་དངོས་རྣམས་དངོས་ཉིད་ལས། །
ཡོད་པར་རྗེས་སུ་ལྟ་བྱེད་ན། །
དེ་ལྟ་ཡིན་ན་དངོས་པོ་རྣམས། །
རྒྱུ་རྐྱེན་མེད་པར་ཁྱོད་ལྟའོ། །

[Block 2581 [VERSE]]
འབྲས་བུ་དང་ནི་རྒྱུ་ཉིད་དང་། །
བྱེད་པ་པོ་དང་བྱེད་དང་བྱ། །
སྐྱེ་བ་དང་ནི་འགག་པ་དང་། །
འབྲས་བུ་ལ་ཡང་གནོད་པ༌[^1672]བྱེད། །

[Block 2582]
གལ་ཏེ་དངོས་པོ་རྣམས་ངོ་བོ་ཉིད་ལ༌[^1673]ཡོད་པར་རྗེས་སུ་ལྟ་བར་བྱེད་ན། དེ་ལྟ་ན་ཁྱོད་དངོས་པོ་རྣམས་རྒྱུ་དང་རྐྱེན་མེད་པར་ལྟ་བ་ཡིན་ནོ། །

[Block 2583]
དེས་ན་འབྲས་བུ་དང་རྒྱུ་ཉིད་དང་བྱེད་པ་པོ་དང་བྱེད་པ་དང་བྱ་བ་དང་སྐྱེ་བ་དང་འགག་པ་དང་འབྲས་བུ་ལ་ཡང་གནོད་པ་བྱེད་པ་ཡིན་ནོ། །

[Block 2584 [VERSE]]
རྟེན་ཅིང་འབྲེལ་འབྱུང་གང་ཡིན་པ། །
དེ་ནི་སྟོང་པ་ཉིད་དུ་བཤད། །
དེ་ནི་བརྟེན༌[^1674]ནས་གདགས་པ་སྟེ། །
དེ་ཉིད་དབུ་མའི་ལམ་ཡིན་ནོ། །

[Block 2585 [VERSE]]
གང་ཕྱིར་རྟེན་འབྱུང་མ་ཡིན་པའི། །
ཆོས་འགའ་ཡོད་པ་མ་ཡིན་པ། །
དེ་ཕྱིར་སྟོང་པ་མ་ཡིན་པའི། །
ཆོས་འགའ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2586]
ཁོ་བོ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་གང་ཡིན་པ་དེ་ནི་སྟོང་པ་ཉིད་དུ་འཆད་དེ།

[Block 2587 [VERSE]]
དེ་ནི་བརྟེན་ནས་གདགས་པ་ཡིན་ཏེ། །
དེ་ཉིད་དབུ་མའི་ལམ་ཡིན་ནོ། །

[Block 2588]
དེ་ལ་དངོས་པོ་འགའ་ཞིག་ཡོད་པ་ཉིད་ཡིན་ན། དེ་ནི་བརྟེན་ནས་འབྱུང་བ་དང་བརྟེན་ནས་གདགས་པ་ཡིན་པས། གང་གི་ཕྱིར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མ་ཡིན་པའི་ཆོས་འགའ་ཡང་ཡོད་པ་མ་ཡིན་པ་དེའི་ཕྱིར་སྟོང་པ་མ་ཡིན་པའི་ཆོས་ནི་འགའ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2589 [VERSE]]
གལ་ཏེ་འདི་ཀུན་མི་སྟོང་ན། །
འབྱུང་བ་མེད་ཅིང་འཇིག་པ་མེད། །
འཕགས་པའི་བདེན་པ་བཞི་པོ་རྣམས། །
ཁྱོད་ལ་མེད་པར་ཐལ་བར་འགྱུར། །

[Block 2590]
གལ་ཏེ་འགྲོ་བ་འདི་ཀུན་མི་སྟོང་ན་དེའི་ཕྱིར་འབྱུང་བ་མེད་ཅིང་འཇིག་པ་མེད་དོ། །

[Block 2591]
དེ་དག་མེད་པའི་ཕྱིར་འཕགས་པའི་བདེན་པ་བཞི་པོ་རྣམས་ཁྱོད་ལ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 2592]
གལ་ཏེ་ཇི་ལྟ༌[^1675]ཞེ་ན་བཤད་པ།

[Block 2593 [VERSE]]
རྟེན་ཅིང་འབྲེལ་འབྱུང་མ་ཡིན་ན། །
སྡུག་བསྔལ་ཡོད་པར་ག་ལ་འགྱུར། །
མི་རྟག་སྡུག་བསྔལ་གསུངས་པ་དེ། །
ངོ་བོ་ཉིད་ལས་ཡོད་མ་ཡིན། །

[Block 2594]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མ་ཡིན་ན་སྡུག་བསྔལ་ཡོད་པར་མི་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན།

[Block 2595]
མདོ་སྡེ་དག་ལས།
--- END BLOCKS ---
