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

[Block 2596]
མི་རྟག་པ་ནི་སྡུག་བསྔལ་ལོ། །

[Block 2597]
ཞེས་གསུངས་པ་དེ་ངོ་བོ་ཉིད་ལས་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2598]
ཡང་གཞན་ཡང་།

[Block 2599 [VERSE]]
ངོ་བོ་ཉིད་ལས་ཡོད་མིན་ན། །
ཅི་ཞིག་ཀུན་ཏུ་འབྱུང་བར་འགྱུར། །
དེ་ཕྱིར་སྟོང་ཉིད་གནོད་བྱེད་ལ། །
ཀུན་འབྱུང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2600]
སྡུག་བསྔལ་དེ་ངོ་བོ་ཉིད་ལས་ཡོད་པ་མ༌[^1676]ཡིན་ན། ཅི་ཞིག་ཀུན་ཏུ་འབྱུང་བར་འགྱུར་ཏེ། ངོ་བོ་ཉིད་ལས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2601]
གང་གི་ཕྱིར་དེ་ལྟར་ཡིན་པ་དེའི་ཕྱིར་སྟོང་པ་ཉིད་ལ་གནོད་པ་བྱེད་པ་ལ་ཀུན་འབྱུང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2602 [VERSE]]
སྡུག་བསྔལ་ངོ་བོ་ཉིད་ཡོད་ལ། །
འགོག་པ་ཡོད་པ་མ་ཡིན་ནོ། །
ངོ་བོ་ཉིད་ནི་ཡོངས་གནས་ཕྱིར། །
འགོག་ལ་གནོད་པ་བྱེད་པ་ཡིན། །

[Block 2603]
སྡུག་བསྔལ་ངོ་བོ་ཉིད་ཀྱིས་ཡོད་པ་ལ་འགོག་པ་ཡོད་པ་མ་ཡིན་ཏེ་མི་འཇིག་པའི་ཕྱིར་རོ། །

[Block 2604]
དེས་ན་ངོ་བོ་ཉིད་ཡོངས་སུ་གནས་པའི་ཕྱིར་འགོག་པ་ལ་གནོད་པ་བྱེད་པ་ཡིན་ནོ། །

[Block 2605 [VERSE]]
ལམ་ནི་ངོ་བོ་ཉིད་ཡོད་ན། །
བསྒོམ་པ་འཐད་པར་མི་འགྱུར་རོ། །
ཅི་སྟེ་ལམ་དེ༌[^1677]བསྒོམ༌[^1678]བྱ་ན། །
ཁྱོད་ཀྱི་དངོས་ཉིད་ཡོད་མ་ཡིན། །

[Block 2606]
ལམ་ངོ་བོ་ཉིད་ཡོད་པར་འཛིན་ན་བསྒོམ་པ་འཐད་པར་མི་འགྱུར་ཏེ་དོན་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2607]
འདི་ལྟར་རྟག་པ་གང་ཡིན་པ་དེ་ལ་བསྒོམ་ཞིང་སྒྲུབ་པའི་ཐབས་མེད་པས་དེའི་ཕྱིར༌[^1679]ལམ་བསྒོམ་པ་འཐད་པར་མི་འགྱུར་རོ། །

[Block 2608]
ཅི་སྟེ་ལམ་བསྒོམ་པར་བྱ་བ་ཡིན་ན་ནི་ཁྱོད་ཀྱི་ངོ་བོ་ཉིད་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2609]
ཡང་གཞན་ཡང་།

[Block 2610 [VERSE]]
གང་ཚེ་སྡུག་བསྔལ་ཀུན་འབྱུང་དང་། །
འགོག་པ་ཡོད་པ་མ་ཡིན་ན། །
ལམ་གྱི༌[^1680]སྡུག་བསྔལ་འགོག་པ་ནི། །
གང་ཞིག་འཐོབ་པར་འགྱུར་བར་འདོད། །

[Block 2611]
གང་གི༌[^1681]ཚེ་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ་དང་འགོག་པའི་ཆོས་གསུམ་པོ་དག་ཡོད་པ་མ་ཡིན་པ་དེའི་ཚེ་ཁྱོད་ཀྱི་སྡུག་བསྔལ་འགོག་པ༌[^1682]གང་ཞིག་ལམ་གྱིས་འཐོབ་པར་འགྱུར་བར་འདོད། ཡང་གཞན་ཡང་།

[Block 2612 [VERSE]]
གལ་ཏེ་ངོ་བོ་ཉིད་ཀྱིས་ནི། །
ཡོངས་སུ་ཤེས་པ་མ་ཡིན་ན། །
དེ་ནི་ཇི་ལྟར་ཡོངས་ཤེས་འགྱུར། །
དངོས་ཉིད་གནས་ཤེས་མ་ཡིན་ནམ། །

[Block 2613]
གལ་ཏེ་སྡུག་བསྔལ་གང་ངོ་བོ་ཉིད་ཀྱིས་ཡོངས་སུ་ཤེས་པ་མ་ཡིན་ན། དེ་ཇི་ལྟར་ཡོངས་སུ་ཤེས་པར་བྱ་བར་ནུས་ཏེ། ངོ་བོ་ཉིད་ཀྱིས་ཡོངས་སུ་མ་ཤེས་པའི་ཕྱིར་རོ།[^1683] །

[Block 2614]
ཁྱོད་ཀྱི་ངོ་བོ་ཉིད་ཀྱིས༌[^1684]ངེས་པར་གནས་པ་ཡིན་ཞེས་མ་ཡིན་ནམ།

[Block 2615 [VERSE]]
དེ་བཞིན་དུ་ནི་ཁྱོད་ཉིད་ཀྱི། །
སྤང་དང་མངོན་སུམ་བྱ་བ་དང་། །
བསྒོམ་དང་འབྲས་བུ་བཞི་དག་ཀྱང་། །
ཡོངས་སུ་ཤེས་བཞིན་མི་རུང་ངོ་། །

[Block 2616]
དེ་བཞིན་དུ་ཁྱོད་ཉིད་ཀྱིས༌[^1685]ཀུན་འབྱུང་བ་སྤང་བ་དང་། འགོག་པ་མངོན་སུམ་དུ་བྱ་བ་དང་། ལམ་བསྒོམ་པ་དང་འབྲས་བུ་བཞི་པོ་དག་ཀྱང་སྡུག་བསྔལ་ཡོངས་སུ་ཤེས་པ་བཞིན་དུ་མི་རུང་སྟེ། ཀུན་འབྱུང་བ་ངོ་བོ་ཉིད་ཀྱིས། མ་སྤངས་པ་གང་ཡིན་པ་དེ་ཡང་སྤང་བར་མི་ནུས་ཏེ། ངོ་བོ་ཉིད་ཀྱིས་མ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 2617]
འགོག་པ་ངོ་བོ་ཉིད་ཀྱིས་མངོན་སུམ་དུ་མ་བྱས་པ་གང་ཡིན་པ་དེ་ཡང་མངོན་སུམ༌[^1686]དུ་བྱ་བར་མི་ནུས་ཏེ། ངོ་བོ་ཉིད་ཀྱིས་མངོན་སུམ་དུ་མ་བྱས་པའི་ཕྱིར་རོ། །

[Block 2618]
ལམ་ངོ་བོ་ཉིད་ཀྱིས་མ་བསྒོམས་པ༌[^1687]ཉིད་གང་ཡིན་པ་དེ་ཡང་བསྒོམས་པར༌[^1688]མི་ནུས་ཏེ། ངོ་བོ་ཉིད་ཀྱིས་མ་བསྒོམས་པའི༌[^1689]ཕྱིར་རོ། །

[Block 2619]
དེ་ལྟར་ན་འཕགས་པའི་བདེན་པ་བཞི་པོ་དེ་དག་ཡོངས་སུ་ཤེས་པ་དང་སྤངས་པ༌[^1690]དང་མངོན་སུམ་དུ་བྱ་བ་དང་། བསྒོམ་པའི་བྱ་བ་བཞི་པོ་དག་ཀྱང་མི་འཐད་དོ། །

[Block 2620]
ཡང་གཞན་ཡང་། འབྲས་བུ་བཞི་པོ་རྒྱུན་ཏུ་ཞུགས་པ་དང་། ལན་ཅིག་ཕྱིར་འོང་བ་དང་། ཕྱིར་མི་འོང་བ་དང་། དགྲ་བཅོམ་པ་དག་ཀྱང་བྱ་བ་བཞི་པོ་དག་མེད་པས་མི་རུང་ངོ་། །ཡང་གཞན་ཡང་།

[Block 2621 [VERSE]]
ངོ་བོ་ཉིད་ནི་ཡོངས་འཛིན་པས། །
འབྲས་བུ་ངོ་བོ་ཉིད་ཀྱིས་ནི། །
ཐོབ་པ་མིན་པ་གང་ཡིན་དེ། །
ཇི་ལྟར་ཐོབ་པར་ནུས་པར་འགྱུར། །

[Block 2622]
ངོ་བོ་ཉིད་ཡོངས་སུ་འཛིན་པས་འབྲས་བུ་ངོ་བོ་ཉིད་ཀྱིས་ཐོབ་པ་མ་ཡིན་པ་གང་ཡིན་པ་དེ་དག་ཀྱང་ཐོབ་པར་མི་ནུས་པར་འགྱུར་རོ། །

[Block 2623 [VERSE]]
འབྲས་བུ་མེད་ན་འབྲས་གནས་མེད། །
ཞུགས་པ་དག་ཀྱང་ཡོད་མ་ཡིན། །
གལ་ཏེ་སྐྱེས་བུ་གང་ཟག་བརྒྱད། །
དེ་དག་མེད་ན་དགེ་འདུན་མེད། །

[Block 2624]
དགེ་སྦྱོང༌[^1691]གི་འབྲས་བུ་རྣམས་མེད་ན་འབྲས་བུ་ལ་གནས་པ་དང་། ཞུགས་པའི་སྐྱེས་བུ་གང་ཟག་བརྒྱད་པོ་དག་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2625]
གལ་ཏེ་སྐྱེས་བུ་གང་ཟག་བརྒྱད་པོ་དེ་དག་མེད་ན་དགེ་འདུན་ཡང་མེད་དོ། །

[Block 2626]
ཡང་གཞན་ཡང་།

[Block 2627 [VERSE]]
འཕགས་པའི་བདེན་རྣམས་མེད་པའི་ཕྱིར། །
དམ་པའི་ཆོས་ཀྱང་ཡོད་མ་ཡིན། །
ཆོས་དང་དགེ་འདུན་ཡོད་མིན་ན། །
སངས་རྒྱས་ཇི་ལྟར་ཡོད་པར་འགྱུར། །

[Block 2628 [VERSE]]
ཁྱོད་ཀྱིས་སངས་རྒྱས་བྱང་ཆུབ་ལ། །
མ་བརྟེན་པར་ཡང་ཐལ་བར་འགྱུར། །
ཁྱོད་ཀྱིས་བྱང་ཆུབ་སངས་རྒྱས་ལ། །
མ་བརྟེན་པར་ཡང་ཐལ་བར་འགྱུར། །

[Block 2629 [VERSE]]
ཁྱོད༌[^1692]ཀྱི་ངོ་བོ་ཉིད་ཀྱིས་ནི། །
སངས་རྒྱས་མིན་པ་གང་ཡིན་དེས། །
བྱང་ཆུབ་བྱང་ཆུབ་སྤྱོད་པ་ལ། །
བརྩལ་ཀྱང་བྱང་ཆུབ་འཐོབ༌[^1693]མི་འགྱུར། །

[Block 2630 [VERSE]]
འགའ་ཡང་ཆོས་དང་ཆོས་མིན་པ། །
ནམ་ཡང་བྱེད་པར་མི་འགྱུར་ཏེ། །
མི་སྟོང་པ་ལ་ཅི་ཞིག་བྱ། །
ངོ་བོ་ཉིད་ལ་བྱ་བ་མེད། །
--- END BLOCKS ---
