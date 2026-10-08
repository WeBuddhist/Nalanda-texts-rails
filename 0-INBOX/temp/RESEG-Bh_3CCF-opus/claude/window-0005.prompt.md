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
[Block 176]
[^67]བདག་པོ་ལ་སོགས་པ་སེམས་དཔའ་གསུམ་ཞེས་བྱ་བ་ནི་དམ་ཚིག་སེམས་དཔའ་དང་ཡེ་ཤེས་སེམས་དཔའ་དང་ཏིང་ངེ་འཛིན་སེམས་དཔའི་བདག་ཉིད་ཅན་གྱི་དཀྱིལ་འཁོར་བ་རྣམས་ཀྱིའོ།།

[Block 177]
གནོད་མཛེས་རྒྱལ་པོ་ཞེས་པ་ནི་གནོད་མཛེས་ཀྱི༌[^68]རྒྱལ་པོས་ཀྱང་བཀུག་སྟེ་བསྐུལ་བའོ།།

[Block 178]
འདི་ནི་བདག་གིའོ་ཞེས་པ་ལ་འདི་ནི་ཞེས་པ་ནི་རྣལ་འབྱོར་པའོ།།

[Block 179]
བདག་ཅག་གི་ཞེས་བྱ་བ༌[^69]ནི་སེམས་ཅན་རྣམས་ཀྱིའོ།།

[Block 180]
ཕའོ་ཞེས་བྱ་བ་ནི་རྣལ་འབྱོར་པ་བདག་སྟེ། བདག་ཉིད་ཚོགས་དང་བཅས་པ་ལ་སེམས་ཅན་གྱི་ཚོགས་རྣམ་པ་མང་པོ་རྣམས་གཅེས་པར་འཛིན་པར་མངོན་དུ་བསམ་པར་བྱའོ།།

[Block 181]
གང་ཡིན་ཞེ་ན་ཞེས་པ་ལ་སོགས་པ་ནི་ལྷའི་སྐུ་གཉིས་པོ་མཆོག་དང་དམ་པ་ཡིན་པར་སྟོན་ཏོ།།

[Block 182]
སྒྲོན་མ་གསལ་བར་བྱེད་པ་ཞེས་བྱ་བའི་ལེའུ་བཅུ་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 183 [HEADING]]
## ལེའུ་བཅུ་གཅིག་པ། ^11-0

[Block 184]
ལེའུ་དང་པོ་ལས་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་རྡོ་རྗེ་དེ་བཞིན་གཤེགས་པ་ལ་སོགས་པ་ལས་རྫོགས་པའི་རིམ་པ་སྟོན་ཏོ།།

[Block 185]
དེ་ནས་འདི་གསུངས་མ་ཐག་ཏུ་ཞེས་པ་ལ་སོགས་པ་ནི་བསྐྱེད་པའི་རིམ་པ་སྟོན་ཏོ།།

[Block 186]
མཚན་མ་གསུམ་ཞེས་བྱ་བ་ནི་ཉི་མ་དང་ཟླ་བ་དང་པདྨ་རྣམས་གཅིག་ཏུ་གྱུར་པས་སྙིང་གར་ཡེ་ཤེས་སེམས་དཔའ་ཞལ་གཅིག་ཕྱག་གཉིས་པ་འཁོར་ལོ་དང་དྲིལ་བུ་འཛིན་པ་དང་། དེའི་ཐུགས་ཀར་ཡི་གེ་ཨོཾ་བསྒོམ་པ་ལ་བྱའོ།།

[Block 187]
དེ་ལྟར་འོད་དཔག་ཏུ་མེད་པ་ལ་སོགས་པ་རྣམས་ཀྱི་སྦྱོར་བ་ཡང་བསྒོམ་པར་བྱའོ།།

[Block 188]
དྲན་པ་གཅིག་པའི་ཏིང་ངེ་འཛིན།།ཞེས་བྱ་བ་ནི་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་རྣལ་འབྱོར་པས་སྲུང་བའི༌[^70]འཁོར་ལོ་ལ་སོགས་པའི་རིམ་གྱིས་རྡོ་རྗེ་འཛིན་པའི་བདག་ཉིད་ལྷ་སུམ་ཅུ་རྩ་གཉིས་པོ་སྐད་ཅིག་ཙམ་གྱི་རྣམ་པར་བསམ་མོ།།

[Block 189]
དེ་ནས་ཨོཾ་ཤཱུ་ནྱ་ཏཱ་ལ་སོགས་པའི་སྔགས་ཀྱི་རིམ་གྱིས་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་འཁོར་ལོ་ལྟ་བུར་བསམ་པར་བྱའོ།།

[Block 190]
དེ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་རིམ་པ༌[^71]སྒྲུབ་ཐབས་ཀྱི༌[^72]ཡང་རྗེས་སུ་ཆགས་པས་གདོན་པ་ལ་སོགས་པ་བསྒོམ་པར་བྱ་བ་ཡིན་ནོ།།

[Block 191]
དེ་བཞིན་དུ་ཐམས་ཅད་བསྐྱེད་ལ་ཞེས་བྱ་བ་ནི་ཧཱུཾ་ལས་སྐྱེས་པའི་ཉི་མ་དང་།།ཨ་ལས་སྐྱེས་པའི་པདྨ་དང་། དེ་ལས་སྐྱེས་པའི་ཡི་གེ་གསུམ་པོ་བསྐྱེད་པའོ།།

[Block 192]
གཟུགས་ཀྱི་ཕུང་པོ་ལ་སོགས་པ་རྣམས་དང་ཞེས་བྱ་བ་ནི་གཟུགས་ཀྱི་ཕུང་པོ་ལ་སོགས་པ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཞུགས་ཏེ། འོད་གསལ་བར་གྱུར་པ་ནི་མཆོད་པ་ཡིན་ནོ།།

[Block 193]
དང་པོར་མིག་གི་སྦུབས་ཞེས་བྱ་བ་ནི་མིག་གི་རྡོག་མ་ལ་སོགས་པ་སྟོང་པར་བྱས་ནས་འོད་གསལ་བར་གནས་པ་ལ། ཡི་གེ་ཐླིཾ་ལ་སོགས་པ་ལས་སྐྱེས་པའི་སའི་སྙིང་པོ་ལ་སོགས་པ༌[^73]བསམ་པར་བྱའོ།།

[Block 194]
རྡོ་རྗེ་ཨུཏྤལ་ཞེས་བྱ་བ་ནི་གསང་བའི་རྡོ་རྗེ་ཉིད་ཨུཏྤལའི་སྒྲར་བརྗོད་དོ།།

[Block 195]
དེ་བཞིན་གཤེགས་པའི་བཀོད༌[^74]པས་ཀྱང་བསྐྱེད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། རྣམ་པར་སྣང་མཛད་ཀྱི་རྣལ་འབྱོར་པས་རང་གི་མིག་གི་གནས་སུ་རྣམ་པར་སྣང་མཛད་དམ་སའི་སྙིང་པོ་དགོད་པར་བྱའོ།།

[Block 196]
དེ་བཞིན་དུ་འོག་ནས་བཤད་པའི་མི་བསྐྱོད་པ་ལ་སོགས་པ་རྣམས་ཀྱི་རྣལ་འབྱོར་པས་ཀྱང་རྣ་བ་ལ་སོགས་པ་ལ་མི་བསྐྱོད་པ་ལ་སོགས་པ་བསམ་པར་བྱའོ།།

[Block 197]
སྐུ་གསུམ་པོ་ཨོཾ་ཞེས་བྱ་བ་ནི་གཟུགས་དམན་པ་དང་འབྲིང་དང་མཆོག་རྣམས་བསྒྲུབ་པར་བཟུང་བའོ།།

[Block 198]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་བཅུ་གཅིག་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 199 [HEADING]]
## ལེའུ་བཅུ་གཉིས་པ། ^12-0

[Block 200]
དེ་ལྟར་ལམ་ཞེས་བྱ་བ་ནི་དབང་པོ་ལ་སོགས་པའི་རབ་ཏུ་འཇུག་པ་རྣམས་ཇི་ལྟ་བ་བཞིན་དུ་རྣམ་པར་དག་པའོ།།

[Block 201]
རིམ་པ་གཉིས་ཀྱི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་རྡོ་རྗེའི་ཀུན་རྫོབ་དང་དོན་དམ་པ་སྟེ། རྣལ་འབྱོར་པའི་བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པའོ།།

[Block 202]
ཕྱག་རྒྱ་ཆེན་པོ་ཡོངས་སུ་གྱུར་པ་ནི༌[^75]དེའི་འབྲས་བུ་སྟེ།།འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་དངོས་གྲུབ་བོ།།

[Block 203]
དང་པོར་རྣམ་པར་སྣང་མཛད་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དང་པོར་རྣམ་པར་སྣང་མཛད་ཀྱི་རྣལ་འབྱོར་དུ་བྱས་ལ་དེ་ནས་མདུན་གྱི་བར་སྣང་དུ་ཡི་གེ་ཨོཾ་གྱི༌[^76]འཁོར་ལོ་ཇི་སྲིད་དུ་དྲོད་སྐྱེས་པར་གྱུར་པ་དེ་སྲིད་དུ་བསྒོམ་མོ།།

[Block 204]
དེ་ནས་ལག་པས་བླངས་ན༌[^77]འགྲུབ་པར་འགྱུར་རོ།།

[Block 205]
དེ་ལྟར་མི་བསྐྱོད་པ་ལ་སོགས་པའི་རྣལ་འབྱོར་པས་ཀྱང་རྡོ་རྗེ་ལ་སོགས་པ་མངོན་དུ་གྱུར་པའི་བར་དུ་བསྒོམས༌[^78]ནས་ལག་པས་བླངས་ན་འགྲུབ་པར་འགྱུར་ཏེ། མིག་ཡངས་ཞེས་པ་འོག་ནས་འབྱུང་བའི་འབྲས་བུ་རྣམས་དང་འབྲེལ་ཏེ།[^79] །དེ་ལྟར་རི་ལུའི་དངོས་གྲུབ་རྣམས་ཀྱང་བལྟ་བར་བྱའོ།།

[Block 206]
མགོ་བོའི་སྒོར་ཞེས་བྱ་བ་ནི་སྤྱི་བོའི་སྟེང་གི་སྟེང་སྟེ་དེར་རི་ལུ་མངོན་དུ་གྱུར་པར་བྱས་ལ་ཚངས་པའི་སྒོ་དེ་ཉིད་དུ་རབ་ཏུ་ཞུགས་པར་བསྒོམས༌[^80]ན་འགྲུབ་བོ།།

[Block 207]
རབ་ཏུ་མཉམ་པའི་ཆ་ལུགས་འཛིན་པ་ནི་རང་གི་ལྷའི་སྦྱོར་བ་དང་མཐུན་པར་བརྗོད་པའོ།།

[Block 208]
ཡུལ་གཞན་དག་ཅེས་བྱ་བ་ནི་འདོད་ཆགས་ཀྱི་ཡུལ་ལོ།།

[Block 209]
ལུས་དང་ངག་དང་ཡིད་ཀྱི༌[^81]ཞེས་བྱ་བ་ནི་སྐུ་ལ་སོགས་པའི་ལྕགས་ཀྱུས་དེ་བཞིན་གཤེགས་པ་རྣམས་དྲངས་ནས་ནང་དུ་བཅུག་སྟེ། རྣལ་འབྱོར་པའི་རིན་པོ་ཆེ་ལྟ་བུའི་གང་ཟག་རྣམས་ཀྱི༌[^82]བསྒྲུབ་བྱ་དགུག་པའི་དོན་ཏོ།།

[Block 210]
དེ་ཉིད་ཀྱི་སྦྱོར་བ་བསྟན་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་རླུང་གི་དཀྱིལ་འཁོར་ལས་ཕབ་ལ་དབང་ཆེན་ལ་གཞག་པར༌[^83]བྱའོ།།

[Block 211]
སྐྱེ་བོ་སྐལ་བ་དང་ལྡན་པ༌[^84]ཞེས་བྱ་བ་ནི་རྣལ་འབྱོར་པས་གཞན་གྱི་དོན་དུ་བྱའོ།།

[Block 212]
གཞན་དག་ཏུ་ཞེས་བྱ་བ་ནི་གདུག་པ་ཅན་གྱི་སེམས་ཅན་ལའོ།།

[Block 213]
ཐུན་མོང་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་སྤྱོད་ཡུལ་མ་ཡིན་པའོ།།

[Block 214]
རྒྱས་གདབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྙོམས་པར་འཇུག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ།།

[Block 215]
ལག་པར་གནས་པ་ཞེས་བྱ་བ་ནི་བསྒྲུབ་པར་བྱ་བ་བཀུག་ལ་ལག་པས་བཟུང་སྟེ། བཟླས་པའི་སྔགས་ཀྱི་ཡི་གེ་དེ་ལ་དབང་དུ་བྱ་བ་ལ་སོགས་པའི་སྔགས་བཟླས་ཤིང་བསམ་གཏན་བྱ་བའོ།།
--- END BLOCKS ---
