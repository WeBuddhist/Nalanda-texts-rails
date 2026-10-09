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
[Block 2696]
དེ་ལྟ་བས་ན་རྒྱུའི་ཁྱད་པར་འདིས་ཀྱང་མྱ་ངན་ལས་འདས་པ་ནི་དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉི་ག་ཡིན་པར་མི་རིགས་སོ། །

[Block 2697]
འདིར་སྨྲས་པ། མྱ་ངན་ལས་འདས་པ་ནི་དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉི་ག༌[^1724]ཡང་མ་ཡིན་གྱི་གང་ལ་དེ་གཉིས་ཡོད་པ་དེ་ནི་མྱ་ངན་ལས་འདས་པ་ཡིན་ནོ། །

[Block 2698]
འདིར་བཤད་པ།

[Block 2699 [VERSE]]
གལ་ཏེ་མྱ་ངན་འདས་པ་ལ། །
དངོས་དང་དངོས་མེད་གཉིས་ཡོད་ན། །
དེ་གཉིས་གཅིག་ལ་ཡོད་མིན་ཏེ། །
སྣང་བ་དང་ནི་མུན་པ་བཞིན། །

[Block 2700]
མྱ་ངན་ལས་འདས་པ་ལ་དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉིས་ཡོད་པར་ཡང་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། ཕན་ཚུན་མི་མཐུན་པ་དེ་གཉིས་ཡུལ་གཅིག་ན་དུས་གཅིག་ཏུ་ལྷན་ཅིག་ཡོད་པར་མི་རིགས་པའི་ཕྱིར་ཏེ། དཔེར་ན་སྣང་བ་དང་མུན་པ་བཞིན་པས་དེ་ལ་གང་ལ་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དེ་གཉིས་ཡོད་པ་དེ་མྱ་ངན་ལས་འདས་པ་ཡིན་ནོ་ཞེས་གང་སྨྲས་པ་དེ་མི་རིགས་སོ། །

[Block 2701]
འདིར་སྨྲས་པ། མྱ་ངན་ལས་འདས་པ་ནི་དངོས་པོ་ཡང་མ་ཡིན། དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 2702]
འདིར་བཤད་པ།

[Block 2703 [VERSE]]
དངོས་མིན་དངོས་པོ་མེད་མིན་པ། །
མྱ་ངན་འདས་པར་གང་སྟོན་པ། །
དངོས་པོ་མེད་དང་དངོས་པོ་དག །
གྲུབ་ན་དེ་ནི་འགྲུབ་པར་འགྱུར། །

[Block 2704]
ཁྱོད་ཀྱིས༌[^1725]མྱ་ངན་ལས་འདས་པ་ནི་དངོས་པོ་ཡང་མ་ཡིན་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་ནོ་ཞེས་གང་སྨྲས་པ་དེ་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་ཡང་མ་ཡིན་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་པ་ཞེས་བྱ་བར་གསལ་བ་དང་། འཛིན་པ་དང་། རྩོལ་བའི་བློ་གང་ཡིན་པ་དེ་ནི་དངོས་པོ་མེད་པ་དང་དངོས་པོ་དག་གྲུབ་ན་དེ་ཡང་འགྲུབ་པར་འགྱུར་བ་ཡིན་ན། དངོས་པོ་མེད་པ་དང་དངོས་པོ་དེ་དག་མ་གྲུབ་པས་དེའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་དངོས་པོ་ཡང་མ་ཡིན་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་མི་འཐད་དོ། །

[Block 2705]
ཡང་གཞན་ཡང་།

[Block 2706 [VERSE]]
གལ་ཏེ་མྱ་ངན་འདས་པ་ནི། །
དངོས་མིན་དངོས་པོ་མེད་མིན་ན། །
དངོས་མིན་དངོས་པོ་མེད་མིན་ཞེས། །
གང་ཞིག་གིས་ནི་དེ་མངོན་བྱེད། །

[Block 2707]
གལ་ཏེ་མྱ་ངན་ལས་འདས་པ་དངོས་པོ་ཡང་མ་ཡིན་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་པ་ཡིན་ན། དངོས་པོ་ཡང་མ་ཡིན། དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་པ་དེ་དག་ནི་མེད་དེ་དེ་དག་མེད་པའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་དངོས་པོ་ཡང་མ་ཡིན་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་ཞེས་གང་ཞིག་གིས་དེ་མངོན་པར་བྱེད་ཅིང་མཚོན་པར་བྱེད་འཛིན་པར་བྱེད་འདོགས་པར༌[^1726]བྱེད་དེ། དེ་ལྟ་བས་ན་མྱ་ངན་ལས་འདས་པ་དངོས་པོ་ཡང་མ་ཡིན་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ཡང་མི་རིགས་སོ། །

[Block 2708]
འདིའི་ཕྱིར་ཡང་མྱ་ངན་ལས་འདས་པ་མི་འཐད་དེ། ཇི་ལྟར་ཞེ་ན།

[Block 2709 [VERSE]]
བཅོམ་ལྡན་མྱ་ངན་འདས་གྱུར་ནས། །
ཡོད་པར་མི་མངོན་དེ་བཞིན་དུ། །
མེད་དོ་ཞེའམ་གཉི་ག་དང་། །
གཉིས་མིན་ཞེས་བྱ་མི་མངོན་ནོ། །

[Block 2710 [VERSE]]
བཅོམ་ལྡན་བཞུགས་པར་གྱུར་ན་ཡང་། །
ཡོད་པ༌[^1727]མི་མངོན་དེ་བཞིན་དུ། །
མེད་དོ་ཞེའམ་གཉི་ག་དང་། །
གཉིས་མིན་ཞེས་ཀྱང་མི་མངོན་ནོ། །

[Block 2711]
གང་གི་ཕྱིར་བཅོམ་ལྡན་འདས་མྱ་ངན་ལས་འདས་སམ་བཞུགས་པར་གྱུར་ཀྱང་རུང་སྟེ། ཡོད་དོ་ཞེའམ་མེད་དོ་ཞེའམ། ཡོད་ཀྱང་ཡོད་ལ་མེད་ཀྱང་མེད་དོ་ཞེའམ། ཡོད་པ་ཡང་མ་ཡིན། མེད་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བར་མི་མངོན་ཞིང་མཚོན་དུ་མེད་གཟུང་དུ་མེད་གདགས་སུ་མེད་པ་དེའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་ཡང་གདགས་སུ་མེད་དེ། དེ་མེད་ན་མྱ་ངན་ལས་འདས་པ་གང་གི་ཡིན་པར་འགྱུར། དེ་ལྟ་བས་ན་རྣམ་པ་ཐམས་ཅད་ཀྱིས་ཀྱང་མྱ་ངན་ལས་འདས་པ་མི་འཐད་དོ། །

[Block 2712]
ཡང་གཞན་ཡང་། འཁོར་བ་མྱ་ངན་ལས་འདས་པས།[^1728] །

[Block 2713 [VERSE]]
ཁྱད་པར་ཅུང་ཟད་ཡོད་མ་ཡིན། །
མྱ་ངན་འདས་པ་འཁོར་བ་ལས། །
ཁྱད་པར་ཅུང་ཟད་ཡོད་མ་ཡིན། །

[Block 2714]
འདི་ལ་ཕུང་པོའི་རྒྱུན་ལ་བརྟེན་ནས་འཁོར་བ་ཞེས་གདགས་ན། ཕུང་པོ་དེ་དག་ནི་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་པའི་ཕྱིར་ཇི་ལྟར་གཏན་སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པའི་ཆོས་ཅན་ཡིན་པ་དེ་ལྟར་ཁོ་བོས་དང་པོ་ཁོ་ནར་བསྟན་ཟིན་པས། དེའི་ཕྱིར་ཆོས་ཐམས་ཅད་སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པ་མཉམ་པ་ཉིད་ཀྱིས་འཁོར་བ་ནི་མྱ་ངན་ལས་འདས་པ་ལས་ཁྱད་པར་ཅུང་ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2715]
ཇི་ལྟར་འཁོར་བ་མྱ་ངན་ལས་འདས་པ་ལས་ཁྱད་པར་ཅུང་ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་པ་དེ་བཞིན་དུ་མྱ་ངན་ལས་འདས་པ་ཡང་འཁོར་བ་ལས་ཁྱད་པར་ཅུང་ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2716 [VERSE]]
མྱ་ངན་འདས་མཐའ་གང་ཡིན་པ། །
དེ་ནི་འཁོར་བའི་མཐའ་ཡིན་ཏེ། །
དེ་གཉིས་ཁྱད་པར་ཅུང་ཟད་ནི། །
ཤིན་ཏུ་ཕྲ་བའང་ཡོད་མ་ཡིན། །

[Block 2717]
མྱ་ངན་ལས་འདས་པ་དང་། འཁོར་བའི་ཡང་དག་པའི་མཐའ་དང་། སྐྱེ་བ་མེད་པའི་མཐའ་དང་། ཡང་དག་པའི་མཐར་ཐུག་པ་གང་ཡིན་པ་དེ་དག་ནི་དམིགས་སུ་མེད་པར་མཉམ་པ་ཉིད་ཀྱིས་ཁྱད་པར་ཤིན་ཏུ་ཕྲ་བ་ཅུང་ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2718 [VERSE]]
འགགས་པར་གྱུར་དང་མཐའ་སྩོགས༌[^1729]དང་། །
རྟག་ལ་སོགས་པར་ལྟ་བ་དག །
མྱ་ངན་འདས་དང་ཕྱི་མཐའ་དང་། །
སྔོན་གྱི་མཐའ་ལ་བརྟེན་པ་ཡིན། །

[Block 2719]
དེ་བཞིན་གཤེགས་པ་འགགས་པར་གྱུར་ནས་ཡོད་པ་དང་མེད་པ་དང་། ཡོད་ཀྱང་ཡོད་ལ་མེད་ཀྱང་མེད་པ་དང་། ཡོད་པ་ཡང་མ་ཡིན་མེད་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བར་ལྟ་བ་གང་དག་ཡིན་པ་དང་། འཇིག་རྟེན་མཐའ་ཡོད་པ་དང་། འཇིག་རྟེན་མཐའ་མེད་པ་དང་། མཐའ་ཡོད་ཀྱང་ཡོད་ལ་མཐའ་མེད་ཀྱང་མེད་པ་དང་། མཐའ་ཡོད་པ་ཡང་མ་ཡིན་མཐའ་མེད་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བར་ལྟ་བ་གང་དག༌[^1730]ཡིན་པ་དང་། འཇིག་རྟེན་རྟག་པ་དང་། འཇིག་རྟེན་མི་རྟག་པ་དང་། རྟག་ཀྱང་རྟག་ལ། མི་རྟག་ཀྱང་མི་རྟག་པ་དང་། རྟག་པ་ཡང་མ་ཡིན་མི་རྟག་པ་ཡང་མ་ཡིན་ནོ༌[^1731]ཞེས་བྱ་བར་ལྟ་བ་གང་དག་ཡིན་པ་དེ་དག་ནི་གོ་རིམས་བཞིན་དུ་མྱ་ངན་ལས་འདས་པ་དང་ཕྱི་མའི་མཐའ་དང་སྔོན་གྱི་མཐའ་ལ་བརྟེན་པ་ཡིན་ནོ། །

[Block 2720]
དེ་ལ།

[Block 2721 [VERSE]]
དངོས་པོ་ཐམས་ཅད་སྟོང་པ་ལ། །
མཐའ་ཡོད་ཅི་ཞིག་མཐའ་མེད་ཅི། །
མཐའ་དང་མཐའ་མེད་ཅི་ཞིག་ཡིན། །
མཐའ་མིན་མཐའ་མེད་མིན་པ་ཅི། །

[Block 2722 [VERSE]]
དེ་ཉིད་ཅི་ཞིག་གཞན་ཅི་ཡིན། །
རྟག་པ་ཅི་ཞིག་མི་རྟག་ཅི། །
རྟག་དང་མི་རྟག་གཉི་ག་ཅི། །
གཉི་ག་མིན་པའང་ཅི་ཞིག་ཡིན། །

[Block 2723]
དམིགས་པ་ཐམས་ཅད་ཉེར་ཞི་ཞིང་།[^1732] །

[Block 2724 [VERSE]]
སྤྲོས་པ་ཉེར་ཞི་ཞི་བ༌[^1733]སྟེ། །
སངས་རྒྱས་ཀྱིས་ནི་གང་དུ་ཡང་། །
སུ་ལའང་ཆོས་འགའ་མ་བསྟན་ཏོ། །
མྱ་ངན་ལས་འདས་པ་བརྟག༌[^1734]པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་ཉི་ཤུ་ལྔ་པའོ།། །།

[Block 2725 [HEADING]]
## སྲིད་པའི་ཡན་ལག་བཅུ་གཉིས་བརྟག་པ། ^26-0

[Block 2726]
འདིར་སྨྲས་པ། ཁྱོད་ཀྱིས༌[^1735]ཐེག་པ་ཆེན་པོའི་གཞུང་ལུགས་ཀྱིས་དོན་དམ་པ་ལ་འཇུག་པ་ནི་བསྟན་ཟིན་ན། ད་ཁྱོད་ཀྱིས་ཉན་ཐོས་ཀྱི་གཞུང་ལུགས་ཀྱི༌[^1736]དོན་དམ་པ་ལ་འཇུག་པ་སྟོན་ཅིག །འདིར་བཤད་པ།

[Block 2727 [VERSE]]
མ་རིག་བསྒྲིབས་པས་ཡང་སྲིད་ཕྱིར། །
འདུ་བྱེད་རྣམ་པ་གསུམ་པོ་དག །
མངོན་པར་འདུ་བྱེད་གང་ཡིན་པའི། །
ལས་དེ་དག་གིས་འགྲོ་བར་འགྲོ། །

[Block 2728 [VERSE]]
འདུ་བྱེད་རྐྱེན་ཅན་རྣམ་པར་ཤེས། །
འགྲོ་བ་རྣམས་སུ་འཇུག་པར་འགྱུར། །
རྣམ་པར་ཤེས་པ་ཞུགས་གྱུར་ན། །
མིང་དང་གཟུགས་ནི་ཆགས་པར་འགྱུར། །

[Block 2729 [VERSE]]
མིང་དང་གཟུགས་ནི་ཆགས་གྱུར་ན། །
སྐྱེ་མཆེད་དྲུག་ནི་འབྱུང་བར་འགྱུར། །
སྐྱེ་མཆེད་དྲུག་ལ་བརྟེན་ནས་ནི། །
དེ་ལས་རེག་པ་འབྱུང་བར་འགྱུར། །
མིང་དང་གཟུགས་དང་དྲན་བྱེད་ལ།

[Block 2730]
[^1737] །

[Block 2731 [VERSE]]
བརྟེན་ནས་སྐྱེ་བ་ཁོ་ན་ཡིན། །
དེ་ལྟར་མིང་དང་གཟུགས་བརྟེན་ནས། །
རྣམ་པར་ཤེས་པ་སྐྱེ་བར་འགྱུར། །
མིང༌[^1738]དང་གཟུགས་དང་རྣམ་པར་ཤེས། །

[Block 2732 [VERSE]]
གསུམ་པོ་འདུས་པ་གང་ཡིན་པ། །
དེ་ནི་རེག་པ་རེག་དེ་ལས། །
ཚོར་བ་ཀུན་ཏུ་འབྱུང་བར་འགྱུར། །
ཚོར་བའི་རྐྱེན་གྱིས༌[^1739]སྲེད་པ་སྟེ། །

[Block 2733 [VERSE]]
ཚོར་བའི་དོན་ལ་སྲེད་པར་འགྱུར། །
སྲེད་པར་གྱུར་ན་ཉེ་བར་ལེན། །
རྣམ་པ་བཞི་པོ་ཉེར་ལེན་འགྱུར། །
ཉེར་ལེན་ཡོད་ན་ལེན་པ་པོའི། །

[Block 2734 [VERSE]]
སྲིད་པ་རབ་ཏུ་འབྱུང་བར་འགྱུར། །
གལ་ཏེ་ཉེ་བར་ལེན་མེད་ན། །
གྲོལ་བར་འགྱུར་ཏེ་སྲིད་མི་འགྱུར། །
སྲིད་པ་དེ་ཡང་ཕུང་པོ་ལྔ། །

[Block 2735 [VERSE]]
སྲིད་པ་ལས་ནི་སྐྱེ་བ་འབྱུང་། །
རྒ་ཤི་དང་ནི་མྱ་ངན་དང་། །
སྨྲེ་སྔགས་འདོན་བཅས་སྡུག་བསྔལ་དང་། །
ཡིད་མི་བདེ་དང་འཁྲུག་པ་རྣམས། །
--- END BLOCKS ---
