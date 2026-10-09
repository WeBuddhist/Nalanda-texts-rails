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

[Block 2736 [VERSE]]
དེ་དག་སྐྱེ་ལས་རབ་ཏུ་འབྱུང་། །
དེ་ལྟར་སྡུག་བསྔལ་ཕུང་པོ་ནི། །
འབའ་ཞིག་པ་འདི་འབྱུང་བར་འགྱུར། །
དེ༌[^1740]ཕྱིར་མཁས་རྣམས་འཁོར་བ་ཡི། །

[Block 2737 [VERSE]]
རྩ་བའི་འདུ་བྱེད་འདུ་མི་བྱེད། །
དེ་ཕྱིར་མི་མཁས་བྱེད་པ་ཡིན། །
མཁས་མིན་དེ་ཉིད་མཐོང་ཕྱིར་རོ། །
མ་རིག་འགགས་པར་གྱུར་ན་ནི། །

[Block 2738 [VERSE]]
འདུ་བྱེད་རྣམས་ཀྱང་འབྱུང་མི་འགྱུར། །
མ་རིག་འགག་པར་འགྱུར་བ་ནི། །
ཤེས་པ་དེ་ཉིད་བསྒོམས་པས༌[^1741]སོ། །
དེ་དང་དེ་ནི་འགགས་གྱུར་པས། །

[Block 2739 [VERSE]]
དེ་དང་དེ་ནི་མངོན་མི་འབྱུང་། །
སྡུག་བསྔལ་ཕུང་པོ་འབའ་ཞིག་པ། །
དེ་ནི་དེ་ལྟར་ཡང་དག་འགག །

[Block 2740]
བྱིས་པ་མ་རིག་པས་བསྒྲིབས་པས་ཡང་སྲིད་པའི་ཕྱིར་སེམས་ཅན་དམྱལ་བ་ལ་སོགས་པ་འདུ་བྱེད་པའི་འདུ་བྱེད་རྣམ་པ་གསུམ་པོ་དག་ལུས་དང་ངག་དང་ཡིད་དག་གིས་མངོན་པར་འདུ་བྱེད་དོ། །

[Block 2741]
ལས་དགེ་བ་དང་མི་དགེ་བ་ཇི་ལྟར་མངོན་པར་འདུས་བྱས་པ་ཆེན་པོ་དང་འབྲིང་དང་ཆུང་ངུ་གང་དག་ཡིན་པ་དེ་དག་གིས་སེམས་ཅན་དམྱལ་བ་ལ་སོགས་པའི་འགྲོ་བ་རྣམས་སུ་འགྲོའོ། །

[Block 2742]
དེ་ལ་འདུ་བྱེད་ཀྱི་རྐྱེན་ཅན་གྱིས༌[^1742]རྣམ་པར་ཤེས་པ༌[^1743]ཇི་ལྟར་འགྲོ་བ་རྣམས་སུ་ཞུགས་པར་གྱུར་པས་མིང་དང་གཟུགས་ཆགས་པར་འགྱུར་རོ། །

[Block 2743]
མིང་དང་གཟུགས་ཆགས་པར་གྱུར་ན་མིང་དང་གཟུགས་ཆགས་པ་ལས་སྐྱེ་མཆེད་དྲུག་འབྱུང་བར་འགྱུར་རོ། །

[Block 2744]
སྐྱེ་མཆེད་དྲུག་ལ་བརྟེན་ནས་དེ་ལས༌[^1744]རེག་པ་འབྱུང་བར་འགྱུར་ཏེ། རེག་པ་དེ་སྐྱེ་བའི་རིམ་པ་ནི་འདི་ཡིན་ཏེ། མིང་དང་གཟུགས་དང་ཡིད་ལ་བྱེད་པ་ལ་བརྟེན་ནས་སྐྱེ་བ་ཁོ་ན་ཡིན་ཏེ། དེ་ལྟར་མིང་དང་གཟུགས་ལ་བརྟེན་ནས་རྣམ་པར་ཤེས་པ་སྐྱེ་བར་འགྱུར་ཞིང་། དེ་ལྟར་མིང་དང་གཟུགས་དང་རྣམ་པར་ཤེས་པ་གསུམ་པོ་འདུས་པ་གང་ཡིན་པ་དེ་ནི་རེག་པའོ། །

[Block 2745]
རེག་པ་ལས་ཚོར་བ་ཀུན་ཏུ་འབྱུང་བར་འགྱུར་རོ། །

[Block 2746]
ཚོར་བའི་རྐྱེན་གྱིས་སྲེད་པ་སྟེ། ཚོར་བའི་དོན་ལ་སྲེད་པར་འགྱུར་རོ། །

[Block 2747]
སྲེད་པར་གྱུར་ན་ཉེ་བར་ལེན་པ་རྣམ་པ་བཞི་པོ་དག་ཉེ་བར་ལེན་པར་འགྱུར་རོ། །

[Block 2748]
ཉེ་བར་ལེན་པ་ཡོད་ན་ལེན་པ་པོའི་སྲིད་པ་རབ་ཏུ་འབྱུང་བར་འགྱུར་ཏེ། གལ་ཏེ་ཉེ་བར་ལེན་པ་མེད་ན་དེས་ན་གྲོལ་བར་འགྱུར་ཏེ། དེའི་སྲིད་པ་འབྱུང་བར་མི་འགྱུར་བ་འགའ༌[^1745]ཞིག་ན། གང་གི་ཕྱིར་ཉེ་བར་ལེན་པ་དང་བཅས་པ་དེའི་ཕྱིར་སྲིད་པ་འབྱུང་བར་འགྱུར་ཏེ། སྲིད་པ་དེ་ཡང་ཕུང་པོ་ལྔ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 2749]
སྲིད་པ་ལས་ནི་སྐྱེ་བ་འབྱུང་བ་ཡིན་ནོ།[^1746] །སྐྱེ་བ་ལས་རྒ་ཤི་དང་མྱ་ངན་དང་སྨྲེ་སྔགས་འདོན་པ་དང་། སྡུག་བསྔལ་བ་དང་ཡིད་མི་བདེ་བ་དང་། འཁྲུག་པ་རྣམས་འབྱུང་སྟེ། དེ་ལྟར་སྡུག་བསྔལ་གྱི་ཕུང་པོ་སྡུག་བསྔལ་གྱི་ཚོགས་འབའ་ཞིག་མ་འདྲེས་པ་འདི་འབྱུང་བར་འགྱུར་རོ། །

[Block 2750]
དེའི་ཕྱིར་མཁས་པ་རྣམས་ནི་འཁོར་བའི་རྩ་བའི་འདུ་བྱེད་རྣམས་འདུ་མི་བྱེད་དོ། །

[Block 2751]
དེའི་ཕྱིར་མི་མཁས་པ་རྣམས་ནི་འདུ་བྱེད་རྣམས་ཀྱི་བྱེད་པ་པོ་ཡིན་གྱི་མཁས་པ་རྣམས་ནི་མ་ཡིན་ཏེ། དེ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་ཉིད་མཐོང་བའི་ཕྱིར་ཏེ།[^1747] དེ་ལ་མ་རིག་པ་མ་འགགས་པར་གྱུར་ན་འདུ་བྱེད་རྣམས་ཀྱང་འབྱུང་བར་མི༌[^1748]འགྱུར་རོ། །

[Block 2752]
མ་རིག་པ་འགག་པར་འགྱུར་བ་ནི་ཡན་ལག་བཅུ་གཉིས་ཤེས་པ་དེ་ཉིད་བསྒོམ་པ་གོམས་པར་བྱ་བ་དང་། བརྟན་པོ༌[^1749]ཉིད་དུ་བྱས་པས༌[^1750]སོ། །

[Block 2753]
སྲིད་པའི་ཡན་ལག་དེ་དང་དེ་འགགས་པར་གྱུར་པས་སྲིད་པའི་ཡན་ལག་དེ་དང་དེ་མངོན་པར་མི་འབྱུང་སྟེ། དེ་ལྟར་སྡུག་བསྔལ་གྱི་ཕུང་པོ་སྡུག་བསྔལ་གྱི་ཚོགས་འབའ་ཞིག་པ་མ་འདྲེས་པ་དེ་ཡང་དག་པར་འགག་ཅིང་གཏན་འགག་པར་འགྱུར་རོ། །

[Block 2754]
སྲིད་པའི་ཡན་ལག་བཅུ་གཉིས་པོ་དེ་དག་ལ་འཇུག་པ་རྒྱ་ཆེར༌[^1751]མདོ་སྡེ་དང་ཆོས་མངོན་པ་དག་ལས་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 2755]
མདོར་བསྡུས་པའི་དབང་གིས་འདི་ལའང༌[^1752]བརྗོད་དོ། །

[Block 2756]
སྲིད་པའི་ཡན་ལག་བཅུ་གཉིས་བརྟག་པ་ཞེས་བྱ་བ་སྟེ། རབ་ཏུ་བྱེད་པ་ཉི་ཤུ་རྩ་དྲུག་པའོ།། །།

[Block 2757 [HEADING]]
## ལྟ་བ་བརྟག་པ། ^27-0

[Block 2758]
འདིར་སྨྲས་པ། ད་ཁྱོད་ཀྱིས་ཉན་ཐོས་ཀྱི་ཐེག་པ་དང་མཐུན་པའི་མདོ༌[^1753]སྡེའི་མཐའ་ལ་བརྟེན་ནས་ལྟ་བའི་རྣམ་པ་རྣམས་མི་སྲིད་པར་སྟོན་ཅིག །འདིར་བཤད་པ།

[Block 2759 [VERSE]]
འདས་པའི་དུས་ན་བྱུང༌[^1754]ཞེས་དང་། །
མ་བྱུང་འཇིག་རྟེན་རྟག་སོགས་པར། །
ལྟ་བ་གང་ཡིན་དེ་དག་ནི། །
སྔོན་གྱི་མཐའ་ལ་བརྟེན་པ་ཡིན། །

[Block 2760 [VERSE]]
མ་འོངས་དུས་གཞན་འབྱུང་འགྱུར་དང་། །
མི་འབྱུང་འཇིག་རྟེན་མཐའ་སོགས༌[^1755]པར། །
ལྟ་བ་གང་ཡིན་དེ་དག་ནི། །
ཕྱི་མའི་མཐའ་ལ་བརྟེན་པ་ཡིན། །

[Block 2761]
ཟག་པ་ཐམས་ཅད་སྡོམ་པའི་རྣམ་གྲངས་ཞེས༌[^1756]བྱ་བའི་མདོ་སྡེ་ལས་གསུངས་པ་བདག་སྔོན་འདས་པའི་དུས་ན་བྱུང་བར་གྱུར་ཅེས་བྱ་བ་དང་། བདག་སྔོན་འདས་པའི་དུས་ན་བྱུང་བར་མ་གྱུར་ཅེས་བྱ་བའི་རྒྱུ་འདིས་འཇིག་རྟེན་རྟག་པ་ལ་སོགས་པར་ལྟ་བ་གང་ཡིན་པ་དེ་དག་ནི་སྔོན་གྱི་མཐའ་ལ་བརྟེན་པ་ཡིན་ནོ། །

[Block 2762]
བདག་མ་འོངས་པའི་དུས་གཞན་དུ་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བ་དང་། བདག་མ་འོངས་པའི་དུས་གཞན་དུ་འབྱུང་བར་མི་འགྱུར་ཞེས་བྱ་བའི་རྒྱུ་འདིས་འཇིག་རྟེན་མཐའ་ཡོད་པ་ལ་སོགས་པར་ལྟ་བ་གང་ཡིན་པ་དེ་དག་ནི་ཕྱི་མའི་མཐའ་ལ་བརྟེན་པ་ཡིན་ནོ། །

[Block 2763]
དེ་དག་ནི་མི་འཐད་དེ། རིགས་པ༌[^1757]གང་གིས་ཤེ་ན། བཤད་པར་བྱ་སྟེ།

[Block 2764 [VERSE]]
འདས་པའི་དུས་ན་བྱུང་གྱུར་ཅེས། །
བྱ་བ་དེ་ནི་མི་འཐད་དོ། །
སྔོན་ཚེ་རྣམས་སུ་གང་བྱུང་བ། །
དེ་ཉིད་འདི་ནི་མ་ཡིན་ནོ། །

[Block 2765 [VERSE]]
དེ་ཉིད་བདག་ཏུ་འགྱུར་སྙམ་ན། །
ཉེ་བར་ལེན་པ་ཐ་དད་འགྱུར། །
ཉེ་བར་ལེན་པ་མ་གཏོགས་པར། །
ཁྱོད་ཀྱི་བདག་ནི་གང་ཞིག་ཡིན། །

[Block 2766 [VERSE]]
ཉེ་བར་ལེན་པ་མ་གཏོགས་པའི། །
བདག་ཡོད་མ་ཡིན་བྱས་པའི་ཚེ། །
ཉེ་བར་ལེན་ཉིད་བདག་ཡིན་ན། །
ཁྱོད་ཀྱི་བདག་ནི་མེད་པ་ཡིན། །

[Block 2767 [VERSE]]
ཉེ་བར་ལེན་ཉིད་བདག་མ་ཡིན། །
དེ་ནི་འབྱུང་དང་འཇིག་པ་ཡིན། །
ཉེ་བར་བླང་བ་ཇི་ལྟ་བུར། །
ཉེ་བར་ལེན་པོ༌[^1758]ཡིན་པར་འགྱུར། །

[Block 2768 [VERSE]]
བདག་ནི་ཉེ་བར་ལེན་པ་ལས། །
གཞན་དུ་འཐད་པ་ཉིད་མ་ཡིན། །
གལ་ཏེ་གཞན་ན་ལེན་མེད་པར། །
གཟུང་ཡོད་རིགས་ན་གཟུང་དུ་མེད། །

[Block 2769 [VERSE]]
དེ་ལྟར་ལེན་ནས༌[^1759]གཞན་མ་ཡིན། །
དེ་ནི་ཉེར་ལེན་ཉིད་ཀྱང་མིན། །
བདག་ནི་ཉེ་བར་ལེན་མེད་མིན། །
མེད་པ་ཉིད་དུའང་དེ་མ་ངེས། །

[Block 2770]
བདག་སྔོན་འདས་པའི་དུས་ན་བྱུང་བར་གྱུར་ཅེས་བྱ་བ་དེ་ནི་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྔོན་གྱི་ཚེ་རབས་སུ་གང་བྱུང་བར་གྱུར་པ་དེ་ཉིད་ད་ལྟར༌[^1760]གྱི་བདག་འདི་མ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
