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
དེ་ལ་ཡང་རྟགས་གསུམ་སྔ་མ་དང་འདྲ་བར་སྦྱར་རོ། །

[Block 177 [HEADING]]
###### **དབྱེར་མེད་ཕྱག་རྒྱ་ཆེན་པོ་དང་ལྡན་པ།** ^1-1-1-2-1-2-3-0

[Block 178]
དབྱེར་མེད་ཕྱག་རྒྱ་ཆེན་པོ་ནི། ། སྔར་བཞིན་དུ་ཡང་སྒྲུབ་པ་པོས་གནས་ཕུན་སུམ་ཚོགས་པར་བྱ་བའི་རིམ་པ་བྱས་ལ་ལུས་ལྷའི་རྣམ་པར་སྔར་བཞིན་དུ་བསྒོམས་ལ། དེ་ཡང་གཉིས་དེ་ཡང་བརྟག་པ༌[^88]དང་པོར་འདུས་པ་ལ་དེ་ཡང་ལེའུ་དང་པོར་འདུས། དེ་ཡང་ཡི་གེ་བཞི་བཅུ་རྩ་བདུན་དུ་འདུས་དེ་ཡང་ཨེ་ཝཾ་མ་ཡཱ་བཞིར་འདུས་ལ་དེ་ཡང་ཨེ་ཝཾ་གཉིས༌[^89]ཐབས་དང་ཤེས་རབ་ཀྱི་ཡེ་ཤེས་ལྷན་སྐྱེས་སུ་འདོད་ཅིང་ཤེས་པར་བྱས་ལ་བསྒོམ་མོ། །

[Block 179]
དེ་ལྟར་སྒོམ་པ༌[^90]སྤྱོད་པ༌[^91]པོ་ལ་འཛུམ་པ་མཛད་ཅིང་ཉི་ཚེར་གཟིགས་ནས་གསུངས་པའོ། །

[Block 180]
དེར་དེ་རྣམས་ཀྱི་ཕྱིར་དེ་ལ་དེ་ནས་ཏེ་གནས་དང་འཁོར་སྐབས་དེར་སྦྱར་རོ། །

[Block 181]
བཅོམ་ལྡན་འདས་སྔ་མ་དང༌[^92]འདྲའོ། །

[Block 182]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་དང་གསུང་དང་ཐུགས་ཏེ་གསང་བར༌[^93]ཞེས་བྱ་བར་ཉོན་ཅིག །སྙིང་པོ་ཤིན་ཏུ་གསང་བར་ཞེས་བྱ་བར་ཉོན་ཅིག་རྗེ་བཙུན་ཆེ་གསང་བར་ཉོན་ཅིག་ཅེས་བྱའོ། །

[Block 183]
དེ་ནི་སྐུ་སྟེ་རྣམ་པར་སྣང་མཛད་སྐུའི་གསང་བ་བྱ་བའི་རྒྱུ༌[^94]དང་། གསུང་སྟེ་སྣང་བ་མཐའ་ཡས་གསུང་གི་གསང་བ་སྤྱོད་པའི་རྒྱུད་དང་ཐུགས་ཏེ་མི་བསྐྱོད་པ་ཐུགས་ཀྱི་གསང་བ་རྣལ་འབྱོར་ཀྱི་རྒྱུད་དེ་རྣམས་དང་ལྡན་པར་ཉོན་ཅིག །སྙིང་པོ་རྡོ་རྗེ་འཆང་སྟེ་ཤིན་ཏུ་གསང་བ་བླ་ན་མེད་པའི་རྒྱུད་དང་ལྡན་པ་དང་རྗེ་བཙུན་དགྱེས་པའི་རྡོ་རྗེ་ཆེས་གསང་བ་ལྷན་ཅིག་སྐྱེས་པའི་ཡེ་ཤེས་སུ་ཉོན་ཅིག་པའོ། །

[Block 184]
རྣམ་པར་སྣང་མཛད་ནི་རྣལ་འབྱོར་གྱི་སྟོན་པ་ཡིན། སྐུ་རྡོ་རྗེ་བྱ་བའི་རྒྱུད་དང་ཇི་ལྟར་འབྲེལ་ཞེ་ན། །ཀྲྀ་ཡ་ལུས་ཀྱི་བྱ་བ་གཙོར་སྟོན་པ་སྐུ་རྡོ་རྗེ་དང་སྐུའི་གསང་བར་འབྲེལ་ཏེ།[^95] གཉིས་ཀའི་རྒྱུད་ཀྱང་ཟེར། སྤྱོད་པའི་རྒྱུད་གསུངས་ཏེ་ལུས་ངག་གི་བཟླས་པ་གཙོར་སྟོན་པས༌[^96]སྣང་བ་མཐའ་ཡས་གསུང༌[^97]གསང་བར་རིགས་སོ། །

[Block 185]
ཡོ་ག་ཏིང་ངེ་འཛིན་གཙོ་བོར་སྟོན་པས་ཐུགས་མི་བསྐྱོད་པ་དང་ཐུགས་ཀྱི་གསང་བར་རིགས་སོ། །

[Block 186]
དེ་ནས་རྡོ་རྗེ་སྙིང་པོས་སྟན་ལས་ལངས་ཏེ། བླ་གོས་ཕྲག་པ་གཅིག་ཏུ་གཟར་ནས་པུས་མོ་གཡས་པའི་ལྷ་ང་ས་ལ་བཙུགས་ནས་འདི་སྐད་ཅེས་གསོལ་ཏོ། །

[Block 187]
གསང་བ་གསུམ་པོ་དེ་ཞུ་འཚལ། །ཞེས་པ་དང་། དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཨེ་མ་ཧོ་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་རྡོ་རྗེ་སྙིང་པོ་སྙིང་རྗེ་ཆེན་པོ་ལེགས་སོ་ལེགས་སོ་ཞེས་གསུངས་ཏེ། [^98]ཨེ་མའོ་ཞེས་པ་ནི་ངོ་མཚར་བ་སྟེ། སྡུད་པ་པོ་དང་ཆོས་ལའོ། །

[Block 188]
སྡུད་པ་པོ་ནི་རྣལ་འབྱོར་གྱི་དབང་ཕྱུག་བྱེ་བ་ཕྲག་བརྒྱད་ཅུའི་ནང་ནས༌[^99]རྡོ་རྗེ་སྙིང་པོ་ཞུ་བ་པོ་ངོ་མཚར་བ་དང་། ཆེས་གསང་བ་གསུམ་ལས་ཆེས་གསང་བ་དགྱེས་པའི་རྡོ་རྗེ་ཞུ་བ་ངོ་མཚར་བའོ། །

[Block 189]
བྱང་ཆུབ་སེམས་དཔའ་ནི་བདག་དོན་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 190]
ཆེན་པོ་ནི་གཞན་དོན་ཕུན་སུམ་ཚོགས་པའི་སྒོ་ནས་སོ། །

[Block 191]
རྡོ་རྗེ་སྙིང་པོ་ནི་རང་རིག་སྟེ༌[^100]ཤེས་རབ་ཆེན་པོ་སྙིང་རྗེ་ཆེན་པོ་ནི་ཐབས་ཀྱི་སྒོ་ནས་སོ། །

[Block 192]
ལེགས་སོ་ལེགས་སོ་ཞེས་པ་ནི་རང་དོན་དུ་ཞུས་པ་དང་གཞན་དོན་དུ་ཞུས་པས་ལེགས་པ་གཉིས་སོ། །

[Block 193]
ད་ལྟར་གྱི་དུས་དང་མ་འོངས་པའི་སྒོ་ནས་ལེགས་པར་འགྱུར་བ་གཉིས་སོ། །

[Block 194]
རང་གི་ངོ་བོ་ལ་ཤེས་རབ་དང་ཐབས་གཉིས་ཀྱི་སྒོ་ནས་ལེགས་སོ་བ་གཉིས༌[^101]གསུངས་སོ། །

[Block 195 [HEADING]]
#### མིང་གི་རྣམ་གྲངས་གཞན་གྱིས་བཅོམ་ལྡན་འདས་ཀྱིས་བསྟན་པ། ^1-1-2-0

[Block 196]
དེ་ལྟར་གནང་བ༌[^102]ལེགས་སོ་བ་བྱིན་ནས་སྐུ་རྡོ་རྗེ་ལ་སོགས་པ་རྡོ་རྗེ་སེམས་དཔའ་ལ་སོགས་པ་མིང་གི་རྣམ་གྲངས་གཞན་གྱིས་བཅོམ་ལྡན་འདས་ཀྱིས་བསྟན་པ་ནི་རྡོ་རྗེའི་ཚིག་དབྱིངས་དང་ལྡན་པ་ཡིན་ཏེ། ཡོན་ཏན་འདི་རྣམས་ཡོད་དེ་ཤེས་བྱ་དང་ལམ་དང་འབྲས་བུའི་དབང་དུ་བྱས་པ་དང་རྣམ་གཞག་གནས་སྐབས་ཀྱི་དབང་དུ་བྱས་ཏེ་བསྟན་པའོ། །

[Block 197 [HEADING]]
##### ཤེས་བྱའི་དབང་དུ་བྱས་པ། ^1-1-2-1-0

[Block 198]
དེ་ལ་ཤེས་བྱ་ནི་རྡོ་རྗེ་སེམས་དཔའ་སྟེ་སྟོང་པ་ཉིད་ཤེས་རབ་དང་། སེམས་དཔའ་ཆེན་པོ་ནི་ཐབས་ཏེ་སྣང་བ་དུ་མ་དང་དམ་ཚིག་སེམས་དཔའ་ཞེས་པ་ནི་དབྱེར་མེད་སྣང་སྟོང་ངོ་། །སྙིང་པོ་ཀྱེའི་རྡོ་རྗེ་ཞེས་བྱ་བ་ནི་དབྱེར་མེད་ལས་བྱུང་བ་ཆེ་བའི་བདག་ཉིད་དོ། །

[Block 199 [HEADING]]
##### ལམ་གྱི་དབང་དུ་བྱས་པ། ^1-1-2-2-0

[Block 200]
ལམ་ནི་རྡོ་རྗེ་སེམས་དཔའ་ཞེས་བྱ་བ་ནི་ལྟ་བ་སྟེ། སྟོང་པ་ཡུལ་དང་ཡུལ་ཅན་ནོ། །

[Block 201]
སེམས་དཔའ་ཆེན་པོ་ནི་སྒོམ་པ་སྟེ་བདེ་བ་ཆེན་པོའོ། །

[Block 202]
དམ་ཚིག་སེམས་དཔའ་ཞེས་བྱ་བ་ནི་སྤྱོད་པ་སྒོ་གསུམ་གྱི་ཚུལ་དང་སྙིང་པོ་ཞེས་བྱ་བ་ནི་འབྲས་བུ་རོ་གཅིག་གོ། །

[Block 203]
དེ་ནི་ཐུན་མོང་ལམ་མངོན་པར་རྟོགས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 204]
ལམ་ཁྱད་པར་ནི་རྡོ་རྗེ་སེམས་དཔའ་ཞེས་པ་ནི་དགའ་བ་དང་སེམས་དཔའ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་མཆོག་ཏུ་དགའ་བ་དང་། དམ་ཚིག་སེམས་དཔའ་ནི་དགའ་བྲལ་དང་སྙིང་པོ་དགྱེས་པའི་རྡོ་རྗེ་ཞེས་བྱ་བ་ནི་ལྷན་ཅིག་སྐྱེས་པའི་དགའ་བའོ། །

[Block 205]
དེ་ཡང་ཡོད་པ༌[^103]དང་ཐོབ་པའི་ཁྱད་པར་གཞན་ལུས་ལ་སོགས་པ་སྐྱེ་ལུགས་བླ་མའི་མན་ངག་ལས་ཤེས་པར་བྱའོ། །

[Block 206 [HEADING]]
##### འབྲས་བུའི་དབང་དུ་བྱས་པ། ^1-1-2-3-0

[Block 207 [VERSE]]
འབྲས་བུའི་རྡོ་རྗེ་སེམས་དཔའ་ནི་ཆོས་སྐུའོ། །
སེམས་དཔའ་ཆེན་པོ་ནི་ལོངས་སྐུའོ། །
དམ་ཚིག་སེམས་དཔའ་ནི་སྤྲུལ་སྐུའོ། །

[Block 208]
སྙིང་པོ་དགྱེས་པའི་རྡོ་རྗེ་ནི་བདེ་བ་ཆེན་པོའི་སྐུ་བསྟན་པའོ། །

[Block 209 [HEADING]]
##### རྣམ་གཞག་གནས་སྐབས་ཀྱི་དབང་དུ་བྱས་པ། ^1-1-2-4-0

[Block 210]
རྣམ་གཞག་རྡོ་རྗེ་སེམས་དཔའ་ནི་ཧེ་རུ་ཀ་ཕྱག་གཉིས་པའོ། །

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
--- END BLOCKS ---
