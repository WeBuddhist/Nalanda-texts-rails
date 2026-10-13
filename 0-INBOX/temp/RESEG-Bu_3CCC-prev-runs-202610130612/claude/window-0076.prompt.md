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
[Block 2661]
རེ་ཞིག་མྱ་ངན་ལས་འདས་པ་ནི་རྣམ་པ་ཐམས་ཅད་དུ་ཡང་དངོས་པོ་མ་ཡིན་ནོ།[^1710] །གལ་ཏེ་དངོས་པོ་ཡིན་པར་གྱུར་ན། རྒ་ཤིའི་མཚན་ཉིད་ཅན་ཡིན་པར་ཐལ་བར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། རྒ་ཤི་མེད་པའི་དངོས་པོ་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2662]
ཡང་གཞན་ཡང་།

[Block 2663 [VERSE]]
གལ་ཏེ་མྱ་ངན་འདས་དངོས་ན། །
མྱ་ངན་འདས་པ་འདུས་བྱས་འགྱུར། །
དངོས་པོ་འདུས་བྱས་མ་ཡིན་པ། །
འགའ་ཡང་ཇི་ལྟར་ཡོད་མ་ཡིན། །

[Block 2664]
གལ་ཏེ་མྱ་ངན་ལས་འདས་པ་དངོས་པོ་ཡིན་ན་དེའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་འདུས་བྱས་སུ་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་འདུས་བྱས་མ་ཡིན་པ་ནི་འགའ་ཡང་ཇི་ལྟར་ཡང་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2665]
ཡང་གཞན་ཡང་།

[Block 2666 [VERSE]]
གལ་ཏེ་མྱ་ངན་འདས་དངོས་ན། །
ཇི་ལྟར་མྱང་འདས་དེ་བརྟེན་མིན། །
དངོས་པོ་བརྟེན་པ་མ་ཡིན་པ། །
འགའ་ཡང་ཡོད་པ༌[^1711]ཡིན་ནོ། །

[Block 2667]
གལ་ཏེ་མྱ་ངན་ལས་འདས་པ་དངོས་པོ་ཡིན་པར་འདོད་ན་མྱ་ངན་ལས་འདས་པ་ལ་བརྟེན་པ་མ་ཡིན་ནོ་ཞེས་གང་སྨྲས་པ་དེ་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་བརྟེན་པ་མ་ཡིན་པ་ནི་འགའ་ཡང་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ལྟ་བས་ན། མྱ་ངན་ལས་འདས་པ་ནི་དངོས་པོ་མ་ཡིན་ནོ། །

[Block 2668]
འདིར་སྨྲས་པ། འོ་ན་མྱ་ངན་ལས་འདས་པ་ནི་དངོས་པོ་མེད་པ་ཡིན་ནོ། །

[Block 2669]
འདིར་བཤད་པ།

[Block 2670 [VERSE]]
གལ་ཏེ་མྱ་ངན་འདས་དངོས་མིན། །
དངོས་མེད་ཇི་ལྟར་རུང་བར་འགྱུར། །

[Block 2671]
གལ་ཏེ་མྱ་ངན་ལས་འདས་པ་ཇི་ལྟར་དངོས་པོ་ཡིན་པར་མ་གྱུར་པས་ན་དངོས་པོ་མེད་པ་མ༌[^1712]ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་རབ་ཏུ་གྲུབ་པར་གྱུར་ན། དངོས་པོ་མེད་པ་ཡང་རབ་ཏུ་འགྲུབ་པར་འགྱུར་བའི་ཕྱིར་རོ།། །།

[Block 2672]
དབུ་མའི་རྩ་བའི་འགྲེལ་པ་བུདྡྷ་པཱ་ལི་ཏ། བམ་པོ་བཅུ་པ་སྟེ་ཐ་མའོ། །

[Block 2673]
ཡང་གཞན་ཡང་།

[Block 2674 [VERSE]]
གང་ལ་མྱ་ངན་འདས་དངོས་མིན། །
དེ་ལ་དངོས་མེད་ཡོད་མ་ཡིན། །

[Block 2675]
གང་ལ༌[^1713]མྱ་ངན་ལས་འདས་པ་དངོས་པོ་ཡིན་པར་འདོད་པ་དེ་ལ་དངོས་པོ་མེད་པ་ཡོད་པ་མ་ཡིན་ཏེ། འདི་ལྟར་གང་དངོས་པོ་ཡོད་པ་དེ་དངོས་པོ་མེད་པ་ཞེས་བྱ་བར་མི་རིགས་པའི་ཕྱིར་ཏེ། དེ་ལྟ་བས་ན། མྱ་ངན་ལས་འདས་པ་ནི་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 2676]
ཡང་གཞན་ཡང་།

[Block 2677 [VERSE]]
གལ་ཏེ་མྱ་ངན་འདས་དངོས་མིན། །
ཇི་ལྟར་མྱང་འདས་དེ་བརྟེན་མིན། །
གང་ཞིག་བརྟེན་པ༌[^1714]མ་ཡིན་པའི། །
དངོས་མེད་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2678]
གལ་ཏེ་མྱ་ངན་ལས་འདས་པ་དངོས་པོ་ཡོད་པ་མ༌[^1715]ཡིན་པར་འདོད་ན། མྱ་ངན་ལས་འདས་པ་དེ་བརྟེན་པ་མ་ཡིན་ནོ་ཞེས་གང་སྨྲས་པ་དེ་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། གང་བརྟེན་པ་མ་ཡིན་པའི་དངོས་པོ་མེད་པ་ནི་འགའ་ཡང་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ལྟ་བས་ན་མྱ་ངན་ལས་འདས་པ་ནི་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 2679]
སྨྲས་པ། འོ་ན་མྱ་ངན་ལས་འདས་པ་ཇི་ལྟ་བུ་ཡིན་པར་བརྗོད་པར་བྱ། བཤད་པ།

[Block 2680 [VERSE]]
འོང་བ་དང་ནི་འགྲོ་བའི་དངོས། །
རྟེན་ཏམ་རྒྱུར་བྱས་གང་ཡིན་པ། །
དེ་ནི་བརྟེན༌[^1716]མིན་རྒྱུར་བྱས་མིན། །
མྱ་ངན་འདས་པ་ཡིན་པར་བསྟན། །

[Block 2681]
ཕྱིན་ཅི་ལོག་མ་རྟོགས༌[^1717]པས་འོང་བ་དང་འགྲོ་བའི་དངོས་པོ་ཕུང་པོ་རྣམས་རྟེན་ཏམ་རྒྱུར་བྱས་པ་གང་ཡིན་པ་དེ་ཉིད་ཕྱིན་ཅི་ལོག༌[^1718]པས་བརྟེན་པ་མ་ཡིན་ཞིང་། རྒྱུར་བྱས་པ་མ་ཡིན་པས་ཕུང་པོ་རྣམས་མི་འབྱུང་བ་ནི། མྱ་ངན་ལས་འདས་པ་ཡིན་པར་བསྟན་ཏོ། །

[Block 2682]
ཡང་གཞན་ཡང་།

[Block 2683 [VERSE]]
འབྱུང་བ་དང་ནི་འཇིག་པ་དག །
སྤང་བར་སྟོན་པས་བཀའ་སྩལ་ཏོ། །
དེ་ཕྱིར་མྱ་ངན་འདས་པ་ནི། །
དངོས་མིན་དངོས་མེད་མིན་པར་རིགས། །

[Block 2684]
བཅོམ་ལྡན་འདས་ཀྱིས་འབྱུང་བ་དང་འཇིག་པ་དག་སྤང་བར་བཀའ་སྩལ་པས་དེའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་ནི་དངོས་པོ་ཡང་མ་ཡིན་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་པར་རིགས་སོ། །

[Block 2685]
འདིར་སྨྲས་པ། འོ་ན་མྱ་ངན་ལས་འདས་པ་ནི་དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉི་ག་ཡིན་ནོ། །

[Block 2686]
འདིར་བཤད་པ།

[Block 2687 [VERSE]]
གལ་ཏེ་མྱ་ངན་འདས་པ་ནི། །
དངོས་དང་དངོས་མེད་གཉིས་ཡིན་ན། །
དངོས་དང་དངོས་པོ་མེད་པ་དག །
ཐར་པར་འགྱུར་བ་དེ་མི་རིགས། །

[Block 2688]
གལ་ཏེ་མྱ་ངན་ལས་འདས་པ་དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉི་ག་ཡིན་ན། དེ་ལྟ་ན་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་ཐར་པ་ཡིན་པར་འགྱུར་བས་དེ་ཡང་མི་རིགས་ཏེ་ཕན་ཚུན་འགལ་བ་གཉིས་དུས་གཅིག་ཏུ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 2689]
ཡང་གཞན་ཡང་།

[Block 2690 [VERSE]]
གལ་ཏེ་མྱ་ངན་འདས་པ་ནི། །
དངོས་དང་དངོས་མེད་གཉིས་ཡིན་ན། །
མྱ་ངན་འདས་པ་མ་བརྟེན༌[^1719]མིན། །
དེ་ནི་གཉིས་ལ་བརྟེན་ཕྱིར་རོ། །

[Block 2691]
གལ་ཏེ་མྱ་ངན་ལས་འདས་པ་དངོས་པོ་དང་དངོས་པོ༌[^1720]མེད་པ་གཉིས༌[^1721]ཡིན་ན་དེ་ལྟ་ན་མྱ་ངན་ལས་འདས་པ་མ་བརྟེན་པ་མ་ཡིན་པར་འགྱུར་ཏེ། མྱ་ངན་ལས་འདས་པ་དེ་དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉིས་ལ་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 2692]
དེ་ནི་མི་འདོད་པས་དེའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉི་ག་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2693]
ཡང་གཞན་ཡང་འདིའི་ཕྱིར་རིགས་པ་མ་ཡིན་ཏེ།

[Block 2694 [VERSE]]
གལ་ཏེ་མྱ་ངན་འདས་པ་ནི། །
དངོས་དང་དངོས་མེད་གཉིས་ཡིན་ན། །
མྱ་ངན་འདས་པ་འདུས་མ་བྱས། །
དངོས་དང་དངོས་མེད་འདུས་བྱས་ཡིན། །

[Block 2695]
མྱ་ངན་ལས་འདས་པ་ནི་དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉི་ག་ཡིན་པར་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། མྱ་ངན་ལས་འདས་པ་ནི་འདུས་མ་བྱས་ཡིན་ལ༌[^1722]དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉིས་ནི་འདུས་བྱས༌[^1723]པའི་ཕྱིར་རོ། །

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
--- END BLOCKS ---
