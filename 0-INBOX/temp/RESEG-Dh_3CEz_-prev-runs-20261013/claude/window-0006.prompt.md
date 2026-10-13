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
[Block 211]
སེམས་དཔའ་ཆེན་པོ་ནི་ཕྱག་བཞི་པ་དང་། དམ་ཚིག་སེམས་དཔའ་ནི་ཕྱག་དྲུག་པའོ། །

[Block 212]
སྙིང་པོ་དགྱེས་པའི་རྡོ་རྗེ་ནི་ཕྱག་བཅུ་དྲུག་པའོ། །

[Block 213 [HEADING]]
#### དེའི་དོན་རྒྱས་པར་བཤད་པ། ^1-1-3-0

[Block 214]
དེའི་དོན་རྒྱས་པར་བཤད་པ་ནི་དྲིས་ལན་གྱིས་འཆད་པའོ། །

[Block 215]
རྒྱས་པའི་ཚུལ་ནི་སྡུད་པ་པོས་མིང་གི་རྣམ་གྲངས་གཞན་དུ་བསྟན་པས་ཐེ་ཚོམ་དུ་གྱུར་ཏེ་ཡང་དྲིས་པ་དང་།

[Block 216 [VERSE]]
རྡོ་རྗེ་སྙིང་པོས་གསོལ་པ། །
གང་གི་ཕྱིར་རྡོ་རྗེ་སེམས་དཔའ་ལགས།
ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 217]
དེའི་ལན།

[Block 218 [VERSE]]
རྡོ་རྗེ་མི་ཕྱེད་ཅེས་བྱར་བརྗོད། །
སེམས་དཔའ་སྲིད་པ་གསུམ་གཅིག་པ། །
འདིས་ནི་ཤེས་རབ་རིག་པ་ཡིས། །
རྡོ་རྗེ་སེམས་དཔའ་བརྗོད་པར་བྱ། །

[Block 219]
ཞེས་བྱ་བ་ནི། [^104]སྟོང་པ་ཉིད་དུ་ཆོས་ཐམས་ཅད་དབྱེར་མི་ཕྱེད་པའོ། །

[Block 220]
སྲིད་པ་གསུམ་སྟེ་འདོད་ཁམས་གཟུགས་ཁམས་གཟུགས་མེད་པའི་ཁམས་གསུམ་སྟོང་པར་གཅིག་པའོ། །

[Block 221]
དེ་ཤེས་རབ་ཀྱིས་གཞལ་བར་བྱས་པས་རིག་པ་དེ་ཉིད་རྡོ་རྗེ་དང་ཆོས་མཐུན་པ་སྟེ།

[Block 222 [VERSE]]
སྲ་ཞིང་བརྟན་ལ་ཁོང་སྟོང་མེད། །
སྟོང་ཉིད་རྡོ་རྗེ་ཞེས་སུ་བཤད། །

[Block 223]
ཅེས་པའོ། །

[Block 224]
ཡེ་ཤེས་ཆེན་པོ་རོས་གང་ལ་ཐབས་རྣམ་པ་སྣ་ཚོགས་པའོ། །

[Block 225]
རྟག་ཏུ་དམ་ཚིག་ལ་སྤྱོད་ཕྱིར་ནི་སྤྱོད་པས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་སོགས་པས་སེམས་ཅན་གྱི་དོན་བྱེད་པའོ། །

[Block 226 [HEADING]]
##### དེ་དག་གི་བཤད་ཚུལ་སྦྱར་བ། ^1-1-3-1-0

[Block 227 [HEADING]]
###### བསྐྱེད་པའི་རིམ་པ། ^1-1-3-1-1-0

[Block 228]
དེ་དག་གི་བཤད་ཚུལ་སྦྱར་བ་ཡང་བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པའི༌[^105]ཚུལ་ཏེ། དེ་ལ་བསྐྱེད་པའི་རིམ་པ་ནི་སྒྲུབ་པ་པོ་ནས༌[^106]ཁ་བསྐང་བ་སྔ་མ་དང་འདྲའོ། །

[Block 229]
རྡོ་རྗེ་མི་ཕྱེད་ཅེས་བྱ་བ་མངོན་པར་བྱང་ཆུབ་པ་ལྔ་པོས་མི་ཕྱེད་པའི་སྐུར་བསྐྱེད་པའོ། །

[Block 230]
སེམས་དཔའ་སྲིད་པ་ནི་ཕུང་པོ་ལྔ་ལ་སོགས་པའི་རྩ་བར་རྣམ་པར་ཤེས་པའི་ཕུང་པོ་དེའི་དེ་ཁོ་ན་ཉིད་དགྱེས་པའི་རྡོ་རྗེ་སྟེ་རྒྱུའི་རྡོ་རྗེ་འཆང་ངོ་། །ཡེ་ཤེས་ཆེན་པོའི་རོས་གང་བ་ནི་རིག་མ་དང་བཅས་ཏེ་ཆགས་པས་ཞུ་བའོ། །

[Block 231]
རྟག་ཏུ་དམ་ཚིག་ལ་སྤྱོད་ཕྱིར་ནི་གླུའི་ངོར་བྱས་ཏེ། །འབྲས་བུའི་ཧེ་རུ་ཀར་ལངས་པའོ། །

[Block 232]
ཡང་ཁ་བསྐང་བ་ཡང་སྔ་མ་ལྟར་སྦྱར་རོ། །

[Block 233 [HEADING]]
###### རྫོགས་པའི་རིམ་པ། ^1-1-3-1-2-0

[Block 234]
རྫོགས་པའི་རིམ་པ་ནི་གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་དང་རང་ལུས་ཐབས་དང་ལྡན་པ་དང་། དབྱེར་མེད་ཕྱག་རྒྱ་ཆེན་པོའོ། །

[Block 235 [HEADING]]
###### **གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ།** ^1-1-3-1-2-1-0

[Block 236]
གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་ཡང་རྡོ་རྗེ་མི་ཕྱེད་ནི་ཆོས་འབྱུང་སྟོང་པའོ། །

[Block 237]
སེམས་དཔའ་སྲིད་པ་ནི་ཨ་ཝ་དྷཱུ་ཏཱི་དང་ལྡན་པའི་བྱ་རོག་གི་གདོང་པ༌[^107]ཅན་གྱི་གནས་སོ། །

[Block 238]
དེ་ནི་ཤེས་རབ་མའི་རིགས་པ་སྟེ། རྡོ་རྗེ་སེམས་དཔར༌[^108]བརྗོད་དོ། །

[Block 239]
ཡེ་ཤེས་ཆེན་པོ་རོས་གང་བ་ནི་ཐབས་ནོར་བུ་ནི་གཟུང་བའི་མན་ངག་གིས་བཀང་བ་སྟེ། དེ་ནས་ཐབས་ཀྱི་རིགས་པ་ཕུལ་དུ་ཕྱིན་པའི་ཡེ་ཤེས་མྱངས་པས་སེམས་དཔའ་ཆེན་པོར་བརྗོད་པར་བྱའོ། །

[Block 240]
རྟག་ཏུ་དམ་ཚིག་ལ་སྤྱོད་ཕྱིར། །ཞེས་བྱ་བ་ནི་རྟག་ཏུ་ནི་མི་འགྱུར་བ་སྟེ་ལྷན་ཅིག་པའོ། །

[Block 241]
ས་མ་ཡ་ནི་མཉམ་པའོ། །

[Block 242]
ཡ་ཡོ་ག་སྟེ་དེར་སྦྱོར་བ་ནི་ལུས་མཉམ་པར་སྦྱོར་བ་སྟེ་རྡོ་རྗེ་སྐྱིལ་མོ་ཀྲུང་ངོ་། །

[Block 243 [VERSE]]
རྟེན་མཉམ་པར་སྦྱོར་བ་ཐིག་ལེ་གཉིས་གནས་སོ། །
དེས་གཞན་དོན་ཡོངས་སུ་རྫོགས་པས་ནི།

[Block 244]
དམ་ཚིག་སེམས་དཔར་བརྗོད་པར་བྱ། །ཞེས་པའོ། །

[Block 245 [HEADING]]
###### **རང་ལུས་ཐབས་དང་ལྡན་པ།** ^1-1-3-1-2-2-0

[Block 246]
དེ་ལ་ཡང་ལུས་ཐབས་དང་ལྡན་པ་ལ་བརྟེན་པ་ཆགས་པ་འབྲིང་ནི་རྡོ་རྗེ་མི་ཕྱེད་ནི་ལྟེ་བའི་གནས་སྟོང་པའོ། །

[Block 247 [VERSE]]
སྲིད་པ་གསུམ་ནི་རྩ་གསུམ་མོ། །
གཅིག་ནི་ཨ་ཝ་དྡྷཱུ་ཏཱིར་བསྡུའོ། །

[Block 248]
དེར་སྐྱེས་པའི་ཡེ་ཤེས་ནི་གཟུང་འཛིན་དང་བྲལ་བས་ཤེས་རབ་ཀྱི་རིགས་པའོ། །

[Block 249]
དེས་ན་སྟོང་པ་ཉིད་ཀྱི་ཡེ་ཤེས་དང་ལྡན་པས་རྡོ་རྗེ་སེམས་དཔའ་ཞེས་བྱར་བརྗོད་ཅེས་པའོ། །

[Block 250]
ཡེ་ཤེས་ཆེན་པོ་རོས་གང་བ་ནི་བདེ་བ་ཆེན་པོ་ལས་ལུས་ཀུན་དུ་ཞུ་ཞིང་གང་བའོ། །
--- END BLOCKS ---
