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
[Block 2521]
ད་གང་ལ་ཕྱིན་ཅི་ལོག་དག་སྲིད་པ་བདག་ཉིད་ཀྱིས་རྣམ་པར་དཔྱོད་ཅིག །

[Block 2522]
ཡང་གཞན་ཡང་།

[Block 2523 [VERSE]]
ཕྱིན་ཅི་ལོག་རྣམས་མ་སྐྱེས་ན། །
ཇི་ལྟ་བུར་ན་ཡོད་པར་འགྱུར། །
ཕྱིན་ཅི་ལོག་རྣམས་སྐྱེ་མེད་ན། །
ཕྱིན་ཅི་ལོག་ཅན་ག་ལ་ཡོད། །

[Block 2524]
ཕྱིན་ཅི་ལོག་གང་དག་ངོ་བོ་ཉིད་ལས་མ་སྐྱེས་པ་དེ་དག་ཇི་ལྟ་བུར་ན་ཡོད་པར་འགྱུར། ད་ཕྱིན་ཅི་ལོག་དེ་རྣམས་ངོ་བོ་ཉིད་ལས་སྐྱེ་བ་མེད་ན་ཕྱིན་ཅི་ལོག་ཅན་ཡོད་པར་ག་ལ་འགྱུར།

[Block 2525 [VERSE]]
དངོས་པོ་བདག་ལས་མི་སྐྱེ་སྟེ། །
གཞན་ལས་སྐྱེ་བ་ཉིད་མ་ཡིན། །
བདག་དང་གཞན་ལས་ཀྱང་མིན་ན། །
ཕྱིན་ཅི་ལོག་ཅན་ག་ལ་ཡོད། །

[Block 2526]
ཡང་གཞན་ཡང་།

[Block 2527 [VERSE]]
གལ་ཏེ་བདག་དང་སྡུག་པ་དག །
རྟག་དང་བདེ་བ་ཡོད་ན་ནི། །
བདག་ཤེས་སྡུག་ཤེས་རྟག་ཤེས་དང་། །
བདེ་ཤེས་ཕྱིན་ཅི་ལོག་མ་ཡིན། །

[Block 2528]
གལ་ཏེ་བདག་དང་སྡུག་པ་དང་རྟག་པ་དང་བདེ་བ་ཞེས་བྱ་བ་བཞི་པོ་དེ་དག་ཡོད་ན་ནི་དེ་དག་ཡོད་པའི་ཕྱིར་རོ།[^1639] །རྟག་ཏུ་ཤེས་པ་དང་། སྡུག་པར་ཤེས་པ་དང་། རྟག་པར་ཤེས་པ་དང་། བདེ་བར་ཤེས་པ་དེ་དག་ཕྱིན་ཅི་ལོག་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 2529]
དེ་ལ་འདི་སྙམ་དུ་བདག་དང་སྡུག་པ་དང་རྟག་པ་དང་བདེ་བ་ཞེས་བྱ་བ་བཞི་པོ་དེ་དག་ནི་ཡོད་པ་མ་ཡིན་གྱི་བདག་མེད་པ་ལ་སོགས་པ་བཞི་པོ་དག་ནི་ཡོད་དེ། དེ་དག་ལ་ཕྱིན་ཅི་ལོག་ཏུ་འཛིན་པས་ཕྱིན་ཅི་ལོག་དག་ཀྱང་ཡོད་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 2530 [VERSE]]
གལ་ཏེ་བདག་དང་སྡུག་པ་དང་། །
རྟག་དང་བདེ་བ་མེད་ན་ནི། །
བདག་མེད་མི་སྡུག་མི་རྟག་དང་། །
སྡུག་བསྔལ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2531]
གལ་ཏེ་བདག་དང་སྡུག་པ་དང་རྟག་པ་དང་བདེ་བ་ཞེས་བྱ་བ་བཞི་པོ་དེ་དག་མེད་ན་ནི། དེ་དག་མེད་པའི་ཕྱིར་བདག་མེད་པ་དང་མི་སྡུག་པ་དང་མི་རྟག་པ་དང་སྡུག་བསྔལ་ཞེས་བྱ་བ་བཞི་པོ་དག་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། ལྟོས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2532]
དེའི་ཕྱིར་རྒྱུའི་ཁྱད་པར་འདིས་ཀྱང་ཕྱིན་ཅི་ལོག་རྣམས་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2533 [VERSE]]
དེ་ལྟར་ཕྱིན་ཅི་ལོག་འགགས་པས། །
མ་རིག་པ་ནི་འགག་པར་འགྱུར། །
མ་རིག་འགགས་པར་གྱུར་ན་ནི། །
འདུ་བྱེད་ལ་སོགས་འགག་པར༌[^1640]འགྱུར། །

[Block 2534]
དེ་ལྟར་ལམ་གྱིས༌[^1641]ཕྱིན་ཅི་ལོག་རྣམས་འགག་ལ། ཕྱིན་ཅི་ལོག་འགགས་པས་མ་རིག་པ་འགག །མ་རིག་པ་འགགས་པས་འདུ་བྱེད་ལ་སོགས་པའི་དོན་འགག་པར་འགྱུར་རོ། །

[Block 2535 [VERSE]]
གལ་ཏེ་ལ་ལའི་ཉོན་མོངས་པ། །
གང་དག་ངོ་བོ་ཉིད་ཡོད་ན། །
ཇི་ལྟ་བུར་ན་སྤོང་བར་འགྱུར། །
ཡོད་པ་སུ་ཞིག་སྤོང་བར་བྱེད། །

[Block 2536]
གལ་ཏེ་ལ་ལའི་ཉོན་མོངས་པ་གང་དག་ངོ་བོ་ཉིད་ཀྱིས་ཡོད་ཅིང་ཡང་དག་པ་དང་དེ་ཁོ་ན་དང་བདེན་པ་ཡིན་ན་དེ་དག་ཇི་ལྟར་སྤང་བར༌[^1642]འགྱུར། ཡོད་པ་སུ་ཞིག་སྤོང་བར་བྱེད་དེ་སྤོང་བར་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 2537]
དེ་ལ་འདི་སྙམ་དུ་ཉོན་མོངས་པ་རྣམས་ནི༌[^1643]ངོ་བོ་ཉིད་ཀྱིས་མེད་པ་ཉིད་ཡིན་ཏེ། ངོ་བོ་ཉིད་ཀྱིས་མེད་པ་དེ་དག་སྤོང་བར་བྱེད་དོ་སྙམ་དུ་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 2538 [VERSE]]
གལ་ཏེ་ལ་ལའི་ཉོན་མོངས་པ། །
གང་དག་ངོ་བོ་ཉིད་མེད་ན། །
ཇི་ལྟ་བུར་ན་སྤོང་བར་འགྱུར། །
མེད་པ་སུ་ཞིག་སྤོང་བར་བྱེད། །

[Block 2539]
གལ་ཏེ་ལ་ལའི་ཉོན་མོངས་པ་གང་དག་ངོ་བོ་ཉིད་ཀྱིས་མེད་ཅིང་ཡང་དག་པ་དེ༌[^1644]དང་དེ་ཁོ་ན་དང་བདེན་པ་མ་ཡིན་ན། དེ་དག་ཇི་ལྟར་སྤོང་བར་འགྱུར། མེད་པ་སུ་ཞིག་སྤོང་བར་བྱེད་དེ་སྤང་བར་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 2540]
ཕྱིན་ཅི་ལོག་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་ཉི་ཤུ་གསུམ་པའོ།། །།

[Block 2541 [HEADING]]
## འཕགས་པའི་བདེན་པ་བརྟག་པ། ^24-0

[Block 2542]
འདིར་སྨྲས་པ།

[Block 2543 [VERSE]]
གལ་ཏེ་འདི་དག་ཀུན་སྟོང་ན། །
འབྱུང་བ་མེད་ཅིང་འཇིག་པ་མེད། །
འཕགས་པའི་བདེན་པ་བཞི་པོ་རྣམས། །
ཁྱོད་ལ་མེད་པར་ཐལ་བར་འགྱུར། །

[Block 2544 [VERSE]]
འཕགས་པའི་བདེན་པ་བཞི་མེད་པས། །
ཡོངས་སུ་ཤེས་དང་སྤང་བ་དང་། །
བསྒོམ༌[^1645]དང་མངོན་དུ་བྱ་བ་དག །
འཐད་པར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 2545 [VERSE]]
དེ་དག་ཡོད་པ་མ་ཡིན་པས། །
འབྲས་བུ་བཞི་ཡང་ཡོད་མ་ཡིན། །
འབྲས་བུ་མེད་ན་འབྲས་གནས་མེད། །
ཞུགས་པ་དག་ཀྱང་ཡོད་མ་ཡིན། །

[Block 2546 [VERSE]]
གལ་ཏེ་སྐྱེས་བུ་གང་ཟག་བརྒྱད། །
དེ་དག་མེད་ན་དགེ་འདུན་མེད། །
འཕགས་པའི་བདེན་རྣམས་མེད་པའི་ཕྱིར། །
དམ་པའི་ཆོས་ཀྱང་ཡོད་མ་ཡིན། །
ཆོས་དག༌[^1646]དགེ་འདུན་ཡོད་མིན་ན། །
སངས་རྒྱས་ཇི་ལྟར་ཡོད་པར་འགྱུར། །

[Block 2547]
དེ་སྐད་སྨྲས་ན་དཀོན་མཆོག་ནི།[^1647] །གསུམ་ལ་གནོད་པ་བྱེད་པ་ཡིན། །གལ་ཏེ་འགྲོ་བ་འདི་དག་ཀུན་སྟོང་ན་དེའི་ཕྱིར་འབྱུང་བ་མེད་ཅིང་འཇིག་པ་མེད་དོ། །

[Block 2548]
དེ་དག་མེད་པས་འཕགས་པའི་བདེན་པ་བཞི་པོ་རྣམས་ཁྱོད་ལ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 2549]
འཕགས་པའི་བདེན་པ་བཞི་མེད་པས་སྡུག་བསྔལ་ཡོངས་སུ་ཤེས་པ་དང་ཀུན་འབྱུང་བ་སྤང་བ་དང་ལམ་བསྒོམ་པ་དང་འགོག་པ་མངོན་སུམ་དུ་བྱ་བ་དག་འཐད་པར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 2550]
སྡུག་བསྔལ་ཡོངས་སུ་ཤེས་པ་དང་ཀུན་འབྱུང་བ་སྤང་བ་དང་ལམ་བསྒོམ་པ་དང་འགོག་པ་མངོན་སུམ་དུ་བྱ་བ་དེ་དག་ཡོད་པ་མ་ཡིན་པས་དགེ་སྦྱོང་གི་འབྲས་བུ་བཞི་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2551]
དགེ་སྦྱོང་གི་འབྲས་བུ་མེད་ན། འབྲས་བུ་ལ་གནས་པ་དང་ཞུགས་པ་སྐྱེས་བུ་གང་ཟག་བརྒྱད་པོ་དག་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2552]
གལ་ཏེ་སྐྱེས་བུ་གང་ཟག་བརྒྱད་པོ་དེ་དག་མེད་ན་དགེ་འདུན་མེད་དེ། ཡང་གཞན་ཡང་། འཕགས་པའི་བདེན་པ་རྣམས་མེད་པའི་ཕྱིར་དམ་པའི་ཆོས་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2553]
དམ་པའི༌[^1648]ཆོས་དང་དགེ་འདུན་ཡོད་པ་མ་ཡིན་ན་སངས་རྒྱས་ཇི་ལྟར་ཡོད་པར་འགྱུར་ཏེ། དེ་སྐད་དུ་སྟོང་པ་ཉིད་དུ་སྨྲ་ན་དཀོན་མཆོག་གསུམ་ལ་གནོད་པ་བྱེད་པ་ཡིན་ནོ། །

[Block 2554]
ཡང་གཞན་ཡང་།

[Block 2555 [VERSE]]
སྟོང་ཉིད་འབྲས་བུ་ཡོད་པ་དང་། །
ཆོས་མ་ཡིན་དང་ཆོས་ཉིད་དང་། །
འཇིག་རྟེན་པ་ཡི་ཐ་སྙད་ནི། །
ཀུན་ལ་གནོད་པ་བྱེད་པ་ཡིན། །

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
--- END BLOCKS ---
