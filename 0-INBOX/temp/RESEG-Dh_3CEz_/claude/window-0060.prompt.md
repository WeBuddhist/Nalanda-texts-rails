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
[Block 2101 [VERSE]]
རྡོ་རྗེ་སྙིང་པོ་ནི་སྡུད་པ་པོས་ཞུས་པས་སོ། །
མངོན་པར་བྱང་ཆུབ་ནི་རིམ་པ་གཉིས་སོ། །

[Block 2102]
བརྟག་པ་ནི་ཆོ་ག་ཞི་བ་མོའོ།[^919] །རྒྱལ་པོ་ནི་དེ་ཁོ་ན་ཉིད་དམ་རྫོགས་པའི་རིམ་པ་དང་ལྡན་པས་སོ། །

[Block 2103 [VERSE]]
ལེའུ་བཅུ་གཅིག་པ་ནི་ལྷག་མའོ། །
བརྟག་པ་དང་པོ་རྫོགས་སོ།། །།

[Block 2104 [HEADING]]
## བརྟག་པ་ཕྱི་མ། ^2-0

[Block 2105 [HEADING]]
### དང་པོ་རབ་གནས་ཀྱི་ལེའུ། ^2-1-0

[Block 2106]
ད་ནི་བརྟག་པ་ཕྱི་མར་བསྟན་པའི་དོན་བཤད་པའི་ཕྱིར། རྡོ་རྗེ་སྙིང་པོས་གསོལ་ཞེས་པ་ནི་མཁའ་འགྲོ་མ་རྣམས་དང་སོ་སོར་བསྡམས༌[^920]པའི་ཚུལ་གྱིས་སོ། །

[Block 2107 [VERSE]]
བཅོམ་ལྡན་རྡོ་རྗེ་ནི་རྡོ་རྗེ་འཛིན་པའོ། །
སྙིང་པོ་ནི་ས་ར་སྟེ་བཅུད་དུ་བསྡུས་པའོ། །

[Block 2108]
བདག་ནི་བདག་ཉིད་དམ་བདག་པོ་ཀྱེའི་རྡོ་རྗེའོ།[^921] །དེ་ནས་བཤད་དུ་གསོལ་ཞེས་བྱ་བར་འབྲེལ་ཏོ།[^922] །ཡང་ན་སངས་རྒྱས་ཐམས་ཅད༌[^923]བསྡུས་པའོ།[^924] །

[Block 2109 [VERSE]]
སྙིང་པོ་ནི་བཅུད་དུ་གྱུར་པའོ། །
རབ་གནས་ཀྱི་མཚན་ཉིད་དོ། །

[Block 2110]
དེ་བཤད་དུ་གསོལ་ཞེས་པར་འབྲེལ་ལོ།[^925] །དེའི་དོན་ནི་འདི་ཡིན་ནོ། །

[Block 2111 [HEADING]]
#### བསྙེན་པ། ^2-1-1-0

[Block 2112]
རབ་ཏུ་གནས་པ་ཡང་སྔོན་དུ་བསྙེན་པ་བྱ་སྟེ། རབ་མཐོང་སྔགས་ཀྱི་ཕ་རོལ་སོན། །ཞེས་བྱ་བ་ནི་དེ་ཡང་ཡན་ལག་དྲུག་གམ་ཏིང་ངེ་འཛིན་གསུམ་གྱིས་བྱས་ལ། དེ་ཡང་གསུམ་སྟེ།

[Block 2113 [VERSE]]
གྲངས་ཀྱི་བསྙེན་པ་འབུམ་དང་ཁྲི། །
གཙོ་དང་འཁོར་ནི་ཚང་བར་བྱ། །

[Block 2114]
དུས་ཀྱི་བསྙེན་པ་ཟླ་བ་དྲུག་གོམས་པ་ལ་སོགས་པ༌[^926]ཅི་རིགས་པར་ཤེས་པར་བྱའོ། །

[Block 2115]
མཚན་མ་ནི་ལྷས་གནང་བའམ། རྨི་ལམ་གྱི་བར་དུ་བཟང་པོ་འབྱུང་བ་དང་། སློབ་དཔོན་མཚན་ཉིད་དང་ལྡན་པ་ལ། ལན་གཉིས་དང་གསུམ་གྱི་བར་དུ་གསོལ་བ་གདབ་པར་བྱའོ། །

[Block 2116]
སྔར་སའི་ཆོ་ག་ཡང་ལེའུ་བཅུ་པ་ལྟར་བྱ་སྟེ། དེའི་སྔོན་དུ་བགེགས་བསལ་བའི་དོན་དུ་ཅི་གསུངས་སྦྱིན་སྲེག་བྱས་ནས་ཞེས་པ་ཆོ་ག་བཞིན་བྱའོ། །

[Block 2117]
སྟ་གོན་ལ་སོགས་བྱས་ནས་ནི། བྱ་བ་བདག་ཉིད་ལ་ལྡན་པ་ཕུན་སུམ་ཚོགས་པར་བྱ་བ་ནི་ཡན་ལག་དྲུག་གམ་སྦྱོར་བ་གསུམ་བྱས་ལ། དེ་ནས་སའི་ལྷ་མོ་ལྷག་པར་གནས་པ་ནི་རླུང་མཚམས་སུ་མཎྜལ་ཅིག་བྱས་ལ་མེ་ཏོག་གི་ཚོམ་བུ་ཅིག་བཀྲམ་སྟེ། པཾ་ལས་བུམ་པ་དེ་ལས་སའི་ལྷ་མོ་སྐུ་མདོག་སེར་བ་གཡས་པས་ཁས་ལེན་པ་གཡོན་པས་བུམ་པ་བསྣམས་པ་ཅིག༌[^927]བསྐྱེད་དེ། རང་བཞིན་པ་སྤྱན་དྲངས་ནས་མཆོད་པ་བྱས་ནས། མ་མ་རིན་ཆེན་ཞེས་བྱ་བ་དང་། ས་དང་ཕ་རོལ་ཕྱིན་པ་ཞེས་པ༌[^928]གཞན་ནས་བྱུང་བ་དང་ཚིག་གཉིས་ཀྱིས་དཔང་པོར་གསོལ་པ། བསྟིམ་པའམ་ཡང་ན་དཔང་པོར་བཞུགས་སོ། །

[Block 2118]
ལྷ་ལྷག་པར་གནས་པ་ནི་དཀྱིལ་འཁོར་ཁང་པའམ་གཞན་དུ་མཎྜལ་སྦྱོར་བ་ལྔས་བྱུགས་ལ། གཙོ་བོའི་གནས་སུ་དྲིའི་ཐིག་ལེ་གྲུ་བཞི་བྱ། གཞན་ལ་ཟླུམ་པོ་བྱ། པདྨ་དང་ཟླ་བ་བསམས་ལ་མེ་ཏོག་ཚོམ་བུ་རང་རང་གི་སྔགས་བཟླས་ཤིང་ལྷ་མོར་མོས་ལ། དེ་ལ་མར་མེ་དང་ལྷ་བཤོས་ལ་སོགས་པ་བཀྲམ་སྟེ། སློབ་དཔོན་གྱིས་ས་བོན་ཙམ་མམ་ཕྱག་མཚན་ལས་ལྷར་བསྐྱེད་ལ། ཡེ་ཤེས་འཁོར་ལོ་མདུན་དུ་བཀུག་པ་ལ་བླ་ན་མེད་པའི་མཆོད་པ་བྱས་ལ་དགུག་གཞུག་ལ་སོགས་པ་བྱ། དེ་ལ་སྐྱེ་མཆེད་བྱིན་གྱིས་བརླབ་པ༌[^929]དང་། སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་བརླབ༌[^930]དབང་བསྐུར་མཆོད་བསྟོད་བདུད་རྩི་མྱངས་ནས་བཟླས་པ་མཐར་ཐུག་པའི་བར་དུ་བྱས་ལ། རབ་གནས་ཀྱི་དོན་དུ་ཚིག་བསྒྱུར་ལ་བྱའོ། །

[Block 2119]
དེ་ནས་བུམ་པ་དང་། ཡོ་བྱད་ཀུན་ལྷག་པར་གནས་པ་བྱ། དེ་ནས་ཡོན་བདག་སློབ་མ་དབང་བསྐུར་ནས། སྟ་གོན་ཟངས་ཀྱིས་བྱ། མི་བསྐུར་ན་སྦྱང་བ་དང་། སྤྲོ་བ་བསྐྱེད་པ༌[^931]ཙམ་བྱའོ། །

[Block 2120 [VERSE]]
དེ་ནས་རབ་ཏུ༌[^932]གནས་པ་ལ། །
སྔ་བར་སྐུ་གཟུགས་སྦྱང་བ་དང་། །

[Block 2121]
ཞེས་བྱ་བ་ནི་སྟ་གོན་བྱེད་པ་དང་ཉིན་གཅིག་པར་བྱ་བའོ། །

[Block 2122 [HEADING]]
#### སྟ་གོན་བྱེད་པ། ^2-1-2-0

[Block 2123]
སྟ་གོན་བྱེད་པ་ནི་གཉིས་ཏེ། རྟེན་སྦྱང་བ་དང་། མགོན་པོ་བསྡུ་བའོ། །

[Block 2124 [HEADING]]
##### རྟེན་སྦྱང་བ། ^2-1-2-1-0

[Block 2125]
རྟེན་སྦྱང་བ་ནི་སྟེགས་བུ་ཁྲུ་གང་དཔངས་སུ་ཁྲུ་ཕྱེད་པའི་སྟེང་དུ་སྐུ་གཟུགས་གྲལ་ནས་ཕྱུང༌[^933]ལ། སྦྱང་བ་ལྔ་ནི་དང་པོ་ཁྲུས་ཀྱིས་སྦྱང་སྟེ། འདག་ཆལ་ལ་སོགས་པས་བཀྲུས་ཏེ། དེ་ནས་མེའི་ནང་དུ་ཡུངས་ཀར་བླུགས་ཤིང་སྦྱང་བའི་སྔགས་བཟླས་ཤིང་བསྐོར་ཞིང་བྱའོ། །

[Block 2126 [VERSE]]
དེ་ནས༌[^934]ཆུའི་ནང་དུ་སྔ་མ་བཞིན་བྱའོ། །
དེ་ནས་རྩྭ་དཱུར་བས་སྦྱང་ངོ་། །
དེ་ནས་ཤུན་པ་ལྔས་དྲིལ་ཕྱིས་བྱའོ། །
དེ་དག་མེད་ན་བ་བྱུང་ལྔ་དང་།

[Block 2127]
འབྲུ་མར་བསྐུས་ལ་བག་ཕྱེས་དྲིལ་ཕྱིས་བྱའོ། །

[Block 2128]
དེ་ནས་ལས་ཐམས་ཅད་པའི་བུམ་པ་ནས་ཁྲུས་བྱ། བཀྲ་ཤིས་གདོན་ཞིང་བྱབས་ལ་སྐུ་ཕྱིས་ལ་སྦྱང་ངོ་། །རས་རིས་དང་མཆོད་རྟེན་དང་ལྷ་ཁང་ལ་མེ་ལོང་ལ་ཁྲུས་བྱའོ། །

[Block 2129 [HEADING]]
##### མགོན་པོ་བསྡུ་བ། ^2-1-2-2-0

[Block 2130]
དེ་ནས་མགོན་པོ་བསྡུ་བ་ནི་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་སྤྱན་དྲངས་ལ་མཆོད་པ་དང་བསྟོད་པ་བྱས་ལ་གསོལ་བ་གདབ་པར་བྱའོ། །

[Block 2131]
དེ་ནས་ནང་པར་སྔ་བར་དབང་བསྐུར་ན་རྨི་ལམ་དྲིས་ཁ་སྦྱོར་ནམ་མཁའ་ལ་བཏེག་ལ། ཐིག་དང་ཚོན་དང་ཁ་སྦྱར་དབབ་པ་བསྲེའོ། །

[Block 2132]
དེ་ནས་རྒྱན་དགྲམ་བུམ་པ་དགོད་པ་ལ་སོགས་པ་བྱའོ། །

[Block 2133]
དེ་ནས་དཀྱིལ་འཁོར་བསྒྲུབ་པ་ནི་ཡན་ལག་དྲུག་གམ་སྦྱོར་བ་གསུམ་གྱི་བདག་ཉིད་ལ་ལྡན་པ་ཕུན་སུམ་ཚོགས་པ་ལས་ཀྱི་སློབ་མས་བྱས་ལ་བླ་མ་ལ་མོས་པ་འཕོ་བར་བསྒོམས་ནས། ས་བོན་ཕྱག་མཚན་ཙམ་ལས་ལྷ་བསྐྱེད། རང་བཞིན་གནས་ནས༌[^935]སྤྱན་དྲངས་པ་བསྲེས་ལ་མཆོད་བསྟོད་བདུད་རྩི་མྱང་བ་བྱའོ། །

[Block 2134 [HEADING]]
#### ནང་དུ་གནས་པ། ^2-1-3-0

[Block 2135]
དེ་ནས་ནང་དུ༌[^936]གནས་པ་ནི་བཞི་སྟེ་རབ་ཏུ་གནས་པ་དང་། མངའ་དབུལ་བ་དང་། སྤྱན་དབྱེ་བ་དང་། ཞལ་བསྲོ་བའོ། །

[Block 2136 [HEADING]]
##### རབ་ཏུ་གནས་པ། ^2-1-3-1-0

[Block 2137]
རབ་གནས་ལ་གཉིས་ཏེ། ཐུན་མོང་དང་ཁྱད་པར་གྱི་རབ་ཏུ་གནས་པའོ། །

[Block 2138 [HEADING]]
###### ཐུན་མོང་གི་རབ་ཏུ་གནས་པ། ^2-1-3-1-1-0

[Block 2139]
དེ་ལ་ཐུན་མོང་ནི་སྦྱང་བ་ལྔ་པོ་དང་མགོན་པོ་བསྡུས་པ་ལ་ཚིག་བསྒྱུར་ལ་བྱ། ཉིན་གཅིག་པ་དང་འདྲའོ། །

[Block 2140]
དེ་ལ་རྟེན་རང་རང་གི་ལྷ་གང་ཡིན་པར་བསྐྱེད། མི་གསལ་ན་ལྷག་པའི་ལྷར་བསྐྱེད། པོ་ཏི་ལ་སྔགས་ནི་ཨ་ལས་རྡོ་རྗེ་ཆོས་སུ། མདོ་སྡེ་ནི་སྣང་བ་མཐའ་ཡས་སུ། ཡུམ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་མར་པྲ༌[^937]ལས་བསྐྱེད། མཆོད་རྟེན་ནམ་གཙུག་ལག་ཁང་ནི་བྷྲཱུཾ་ལས་གཞལ་ཡས་ཁང་ངམ། རྡོ་རྗེ་དབྱིངས་ཀྱི་དབང་ཕྱུག་མར་བསྐྱེད། ནམ་མཁར་བཞུགས་པའི་སངས་རྒྱས་རྣམས། སྐུ་གཟུགས་སྙིང་གར་རབ་ཏུ་གཞུག །[^938]ཇི་ལྟར་སངས་རྒྱས་ཐམས་ཅད་ནི། དགའ་ལྡན་གནས་ཞེས་བྱ་བ་སྟེ། སྔར་གྱི་སྟ་གོན་ནམ་མཁར་སྤྱན་དྲངས་པ་བསྟིམ་པ་ཙམ་བྱས་ཏེ། བྱིན་གྱིས་བརླབ།[^939] དབང་བསྐུར། མཆོད་བསྟོད་བྱས་ལ་བཞུགས་སོ། །
--- END BLOCKS ---
