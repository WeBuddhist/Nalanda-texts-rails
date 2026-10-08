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
[Block 1751]
ཆུ་དེ་ཤར་ནས་ནུབ་ཏུ་རྒྱུ་བ་དང་། །ལྷོ་ནས་བྱང་དུ་རྒྱུ་བ་དང་། གཡས་སུ་འཁོར་ཞིང་འཁྱིལ་ན་མཚན་མ་བཟང་བ་དང་ངན་པ་ཡང་ཤེས་པར་བྱའོ། །

[Block 1752 [HEADING]]
###### སྔགས་དང་ཕྱག་རྒྱས་སྦྱང་བ། ^1-10-1-3-2-0

[Block 1753]
སྔགས་དང་ཕྱག་རྒྱས་སྦྱང་བ་ནི་ལག་པ་གཡས་པ་རྡོ་རྗེ་རྩེ་གསུམ་པའི་ཕྱག་རྒྱ་བཅས་ལ། ས་ལ་བརྡབ་ཅིང་ཨོཾ་སརྦ་པཱ་བཾ་ད་ཧ་ན་མཱ་མ་རཀྵ་རཀྵ་ཧཱུཾ་ཕཊ་སྭཱ་ཧཱ་ཞེས་བརྗོད་དོ། །

[Block 1754 [HEADING]]
###### ཏིང་ངེ་འཛིན་གྱིས་སྦྱང་བ། ^1-10-1-3-3-0

[Block 1755]
ཏིང་ངེ་འཛིན་ནི་ས་གཞི་དེ་མི་དམིགས་པར་བསྒོམ་ཞིང་ཤིན་ཏུ་དག་པར་བསམ་མོ། །

[Block 1756 [VERSE]]
ཁ་ཅིག་ཏུ་ནི་ལས་དང་བྱ་བས་སྦྱང་ངོ་། །
ཁ་ཅིག་ཏུ་ནི་སྔགས་དང་ཕྱག་རྒྱས་སྦྱང་ངོ་། །
ཁ་ཅིག་ཏུ་ནི་ཏིང་ངེ་འཛིན་ཙམ་མོ། །
དེ་དག་ནི་ཅི་རིགས་པར་ཤེས་པར་བྱའོ། །

[Block 1757 [HEADING]]
##### བྱིན་གྱིས་བརླབ་པ། ^1-10-1-4-0

[Block 1758]
དེ་ནས་བྱིན་གྱིས་བརླབ་པ་ནི་ཁཾ་ལས་ས་གཞི་སྟོང་པ་ཉིད་དུ་བསམ། ལཾ་ལས་གསེར་གྱི་ས་གཞི་ཆེན་པོར་བྱིན་གྱིས་བརླབ། སུཾ་ལས་རི་རབ་རིན་པོ་ཆེ་སྣ་བཞིའི་རང་བཞིན་དུ་བྱིན་གྱིས་བརླབ།[^822] ཧཱུཾ་ལས་ས་གཞི་རྡོ་རྗེར༌[^823]བྱིན་གྱིས་བརླབ།[^824] ཨོཾ་བཛྲ་མེ་དི་ནཱི་བཛྲི་བྷ་བ་བནྡྷ་ཧཱུཾ་ཞེས་བརྗོད་དོ། །

[Block 1759]
རྡོ་རྗེའི་ས་གཞིའི་རང་བཞིན་ནམ་མཁའི་ཁམས་རྣམ་པར་དག་པར་བསམ་མོ། །

[Block 1760 [HEADING]]
##### ས་གཞི་ཡོངས་སུ་གཟུང་བ། ^1-10-1-5-0

[Block 1761]
ས་གཞི་ཡོངས་སུ་གཟུང་བ་ནི་མེ་ལོང་ངོས་ལྟར་མཉམ་པའི་དཀྱིལ་འཁོར་གྱི་དབུས་སུ་འདུག་ལ། ཡན་ལག་དྲུག་གི་རྣལ་འབྱོར་རམ་སྦྱོར་བ་རྣམ་པ་གསུམ་བསྒོམ་སྟེ། བཟླས་པའི་མཐར་ཐུག་གི་བར་དུ་བྱའོ། །

[Block 1762]
དེ་ཡང་འོག་ནས།

[Block 1763 [VERSE]]
ཁྲུས་དང་གཙང་སྦྲ་དྲི་ཞིམ་ལུས། །
སྣ་ཚོགས་རྒྱན་གྱིས༌[^825]རྣམ་པར་བརྒྱན། །
སློབ་དཔོན་དཀྱིལ་འཁོར་འཇུག་པ་ཉིད། །
འབད་པས་ཧཱུཾ་ལས་རྡོ་རྗེ་ཅན། །

[Block 1764 [VERSE]]
བྱས་ཏེ་ཕྱི་ནས་དཀྱིལ་འཁོར་བྲི། །
ཞེས་བྱ་བ་སའི་ཆོ་ག་དང༌[^826]འབྲེལ་ལོ། །
དེའི་རྗེས་ལ་ཚད་ཛི་ཙམ་དུ་ཞེ་ན།
དཀྱིལ་འཁོར་ཁྲུ་གསུམ་ནི་ཆུང་བའི་ཚད་དོ། །

[Block 1765 [VERSE]]
དེ་ཡང་སྐུ་གསུམ་པའི་བདག་ཉིད་པས་སོ། །
སོར་གསུམ་ནི་སྐུ་གསུང་ཐུགས་སོ། །

[Block 1766]
དའི་རྗེས་ལ་བསྲུང་བའི་ཕྱིར། རྡོ་རྗེ་སེམས་དཔའ་བསྙེམས་བྱས་ནི་གསོལ་བ་གདབ་པའི་རྗེས་ལ་ལྡང་བ་དང་འགྱིང་བ་དང་། ཀུན་དུ་ལྟ་བ་དང་རྡོ་རྗེའི་འགྲོས་ཀྱིས་བསྐོར་བའོ། །

[Block 1767]
གཡས་བརྐྱང་ཞེས་པ་ནི་གཡས་བརྐྱང་ལ་སོགས་པ་སྟང་སྟབས་རྣམས་བྱ་བའམ། གཙོ་བོའི་འདུག་ཚུལ་སྐྱིལ་ཀྲུང་ཕྱེད་པ་ཡིན་ཏེ་གཡོན་བསྐུམ་པས་གནས་སོ། །

[Block 1768]
ཕྱག་གཉིས་དགྱེས་པའི་རྡོ་རྗེར་སྦྱར་བ་ནི་ཕྱག་གཉིས་པའི་ཧེ་རུ་ཀ་མ་ཡིན་ཏེ། རྡོ་རྗེ་དྲིལ་བུ་གཉིས་ཀྱི་ཕྱག་རྒྱ་དང་ལྡན་པར་སྦྱར་བའོ། །

[Block 1769]
སློབ་དཔོན་དཀྱིལ་འཁོར་དུ་འཇུག་པ་ན། རེ་ཁཱའི་ནང་དུ་སོང་སྟེ་བལྟས་ནས་མེ་ཏོག་གི་ཕྲེང་བ་དབུལ་ལོ། །

[Block 1770]
འདིར་ནི་དཀྱིལ་འཁོར་བསྒྲུབ་པ་དང་འབྲེལ་བའོ། །

[Block 1771]
འདི་ཡང་སྔོན་དུ་ཤེས་པའི་གོ་རིམས་ཏེ་སློབ་དཔོན་གྱིས་ཇི་ལྟར་བྱས་ནས་འཇུག་ཅེ་ན། ཁྲུས་དང་གཙང་སྦྲ་ནི་ཆུ་དང་ས་ལ་སོགས་པའམ་ཏིང་ངེ་འཛིན་གྱིས་སོ། །

[Block 1772]
ཡང་དྲི་ཞིམ་ལུས་ནི་གོས་སར་པའོ། །

[Block 1773]
སྣ་ཚོགས་རྒྱན་ནི་རིན་པོ་ཆེའམ་རུས་པའི་རྒྱན་ནོ། །

[Block 1774]
རྣམ་པར་བརྒྱན་ནི་མགུལ་རྒྱན་ལ་སོགས་པ་རིམ་པར་བཀོད་པའོ། །

[Block 1775]
ཧཱུཾ་ཧཱུཾ་བསྙེམས་པ་ནི་ང་རྒྱལ་ལམ་ལྡང་བ་ལ་སོགས་པ་རྡོ་རྗེ་འགྲོས་ཀྱིས་དུས་བརྗོད་པའོ། །

[Block 1776]
ཧི་ཧི་རྣམ་པར༌[^827]འཇིགས་པ་ནི་ཧ་ཧ་ལ་སོགས་པ་བརྒྱད་དེ་སྟང་སྟབས་ཀྱི་དུས་སུ་བརྗོད་པའོ། །

[Block 1777 [HEADING]]
##### བསྲུང་བ། ^1-10-1-6-0

[Block 1778]
དེའི་དོན་ནི་དེ་ཡིན་ཏེ་བསྲུང་བ་ནི་རྣམ་པ་དྲུག་སྟེ། རྡོ་རྗེ་བལྟ་བས་བསྲུང་བ་དང་། དེངས་ཤིག་པས་བསྲུང་བ་དང་། བཀའ་བསྒོ་བས་བསྲུང་བ་དང་། རྡོ་རྗེ་འགྲོས་ཀྱིས་བསྲུང་བ་དང་། སྟང་སྟབས་ཀྱིས་བསྲུང་བ་དང་། རྡོ་རྗེ་ཕུར་པས་བསྲུང་བའོ། །

[Block 1779 [HEADING]]
###### རྡོ་རྗེ་བལྟ་བས་བསྲུང་བ། ^1-10-1-6-1-0

[Block 1780]
དེ་ལ་ལྟ་བས་བསྲུང་བ་ནི། སྔར་གྱི་ས་གཟུང་བའི་སློབ་དཔོན་ལ་གྲོགས་གཽ་རཱི་ལ་སོགས་པ་བཞིའི་ང་རྒྱལ་དང་ལྡན་པ་བཞི་ཡིས་མཆོད་པ་ཅིག་བྱས་ཏེ། དེ་བཞིན་གཤེགས་པ་ཀུན་ཞི་བ། །ཞེས་བྱ་བ་ལ་སོགས་པ་བསྟོད་པ་དང་། གསོལ་བ་བཏབ་པའི་རྗེས་ལ། སྔར་གྱི་དཀྱིལ་འཁོར་ལ་མཆོད་པ་ཅིག༌[^828]བྱས་ཏེ། མ་དང་ཊ་ལས་མིག་ཉི་ཟླར་བསྐྱེད། ཨ་ལས་རྐང་པ་རྡོ་རྗེར་བསྐྱེད་ལ་སྔར་གྱི་དཀྱིལ་འཁོར་ནམ་མཁའ་ལ་བཀོད་དེ་ཧཱུཾ་ཕཊ་ཅེས་བརྗོད་ལ། ཉི་མ་དང་ཟླ་བའི་མིག་གིས་གསད་པ༌[^829]དང་གསོ་བ་བྱའོ། །

[Block 1781 [HEADING]]
###### དེངས་ཤིག་པས་བསྲུང་བ། ^1-10-1-6-2-0

[Block 1782]
དེ་ནས་དེངས་ཤིག་པས་བསྲུང་བ་ནི་དབང་ལྡན་གྱི་མཚམས་སུ་ཕྱིན་ལ། །བདག་ཉིད་ཁྲོ་བོའི་ང་རྒྱལ་གྱིས་འདི་སྐད་བརྗོད་པར་བྱའོ། །

[Block 1783]
ས་ཕྱོགས་འདིར་སློབ་དཔོན་འདི་ཞེས་བྱ་བ་སློབ་མ་འདི་ཞེས་བྱ་བ་རྫོགས་པའི་བྱང་ཆུབ་ལ་རྫོགས་པར་བྱ་བ་དང་། སེམས་ཅན་ཐམས་ཅད་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པར་བྱ་བའི་ཕྱིར་དཀྱིལ་འཁོར་རྒྱལ་པོ་འདི་ཞེས་བྱ་བ་རྩོམ་གྱིས། །གང་སུ་ཡང་རུང་བས་ས་ཕྱོགས་འདི་ན་གནས་པའི་ལྷ་དང་། ལྷ་མ་ཡིན་དང་། གནོད་སྦྱིན་དང་། སྲིན་པོ་དང་། ཡི་དགས་དང་། ཤ་ཟ་དང་། བརྗེད་བྱེད་དང་། འབྱུང་པོ་དང་། གནོན་པོ་དང་། ནམ་མཁའ་ལྡིང་དང་། མིའམ་ཅི་དང་། རིག༌[^830]འཛིན་ལ་སོགས་པ་རྒན་པོ་དང་རྒན་མོ་དང་འཁོར་དང་གཡོག་ཏུ་བཅས་པ་རྣམས་འདིར་མ་གནས་པར་གཞན་དུ་དེངས་ཤིག །དེ་ལྟར་རྡོ་རྗེ་འཛིན་གྱི་བཀའ་ཐོས་ནས་མྱུར་བ་ཉིད་དུ་དེངས་ཤིག །གང་དག་མི་འགྲོ་བ་དེ་དག་ནི་ཕྱག་ན་རྡོ་རྗེ་རབ་ཏུ་འབར་བ་ཧཱུཾ་ཀ་ར་ཤིན་ཏུ་ཁྲོས་པས་ཡེ་ཤེས་ཀྱི་རྡོ་རྗེ་ཆེན་པོ་ཀུན་ནས་རབ་ཏུ་འབར་བས་མགོ་བོ༌[^831]ཚལ་པ་བརྒྱར་འགས་པར་འགྱུར་ཏ་རེ་ཞེས་ལན་གསུམ་བརྗོད་དོ། །

[Block 1784 [HEADING]]
###### བཀའ་བསྒོ་བས་བསྲུང་བ། ^1-10-1-6-3-0

[Block 1785]
དེ་ནས་བཀའ་བསྒོ་བའི་བསྲུང་བ་ནི།

[Block 1786 [VERSE]]
ང་ནི་དཔལ་ལྡན་རྡོ་རྗེ་འཆང་། །
ཉོན་ཅིག་བར་ཆད་བགེགས་ཀྱི་ཚོགས། །
སྲུང་བའི་འཁོར་ལོའི་སྦྱོར་བ་ཡིས། །
ལུས་ངག་ཡིད་ལ་གནོད་པ་རྣམས། །

[Block 1787]
འདིར་ནི་འཇིགས༌[^832]འཇོམས་གཞན་དུ་མིན། །ཞེས་རྡོ་རྗེའི་གནས་སུ་འཁོར་ལོ་དང་རིན་པོ་ཆེ་དང་། པདྨ་དང་རལ་གྲི༌[^833]སྦྱར་ལ་ཚིགས་སུ་བཅད་པ་ལྔ་སྦྱར་གྱིས༌[^834]བསྐྲད་པར་བྱའོ། །

[Block 1788 [HEADING]]
###### རྡོ་རྗེ་འགྲོས་ཀྱིས་བསྲུང་བ། ^1-10-1-6-4-0

[Block 1789]
རྡོ་རྗེ་འགྲོས་ཀྱིས༌[^835]བསྐྲད་པ་ནི་རྡོ་རྗེ་རྩེ་གཅིག་པ་དང་རྩེ་གསུམ་པ་དང་། སྣ་ཚོགས་རྡོ་རྗེའི་འགྲོས་ཀྱིས་དཀྱིལ་འཁོར་བསྐོར་ཞིང་བསྲུང་བར་བྱའོ། །

[Block 1790 [HEADING]]
###### སྟང་སྟབས་ཀྱིས་བསྲུང་བ། ^1-10-1-6-5-0
--- END BLOCKS ---
