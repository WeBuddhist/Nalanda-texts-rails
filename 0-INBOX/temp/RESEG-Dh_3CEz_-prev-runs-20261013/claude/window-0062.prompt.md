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
[Block 2171]
བཅུ་གཉིས་པས་ནི་དབང་བཞིའི་སྡོམ༌[^947]གྱི་ཚིག་དང་དབང་བསྐུར་བའི་ཚིགས་བཅད༌[^948]སྔར་མ་གསུངས་པའི་ཁ་སྐོང༌[^949]བསྟན་ཏོ། །

[Block 2172]
རབ་གནས་ཀྱི་ལེའུ་བཤད་པ་སྟེ་དང་པོའོ།། །།

[Block 2173 [HEADING]]
### བརྟག་པ་གཉིས་པའི་ལེའུ་གཉིས་པ། ^2-2-0

[Block 2174]
ད་ནི་བརྟག་པ་སྔ་མའི་རིམ་པ་གཉིས་ཀྱིས་ཐོབ་པའི་ཐབས་དང་ཤེས་རབ་མི་ཕྱེད་པ་ཕྱག་རྒྱ༌[^950]ཆེན་པོ་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་རྡོ་རྗེ་སྙིང་པོས་དྲིས་པའོ། །

[Block 2175]
ཆོས་ཀུན་ཞེས་པ་ནི་གཟུགས་ལ་སོགས་པའི་རང་བཞིན་ནོ། །

[Block 2176 [VERSE]]
ནམ་མཁའ་ལྟ་བུ་ནི་ཤེས་རབ་ཟབ་མོའི༌[^951]དཔེའོ། །
རྒྱ་མཚོ་ལྟ་བུས་ནི༌[^952]ལྷག་མ་སྟེ་ཐབས་ཟབ་པའི་དཔེའོ། །

[Block 2177]
དེ་ཡང་རིམ་པ་གཉིས་ཀྱི་དོན་ནི་ཟབ་པ༌[^953]སྟེ་དབྱེར་མེད་པ་ཡིན་ན།

[Block 2178 [VERSE]]
བསྐྱེད་རིམ་སྐུ་ཞེས་པ་སྟེ་རིལ་པོའི་མཚན་མའོ། །
ཇི་ལྟར་རམ་དེ་བཞིན་ཞེས་པ་ནི་དཔེའོ། །
རང་འདོད་ལྷའི་གཟུགས་ནི་ལྷག་པའི་ལྷའོ། །

[Block 2179]
སེམས་ཅན་གཟུགས་བསྒོམ་པ། ཇི་ལྟར་བསྒྲུབ་ནི་ཕྱག་རྒྱ་ཆེན་པོ་སྟེ་སྤོང་བའི་སྒྲའོ། །

[Block 2180]
ཡང་ན་ཐབས་དེ་ཞུ་འཚལ་ཞེས་ཞུས་པའོ།[^954] །བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པའི་ལན་དུའོ། །

[Block 2181]
བདག་མེད་རྣལ་འབྱོར་ནི་ཆོས་ཀྱི་སྐུ་ཤེས་རབ་དང་ལྡན་པའོ། །

[Block 2182 [VERSE]]
ཧེ་རུ་ཀ་དཔལ་ནི་ལོངས་སྐུ་ཐབས་སོ། །
གཞན་པའི་སེམས་ནི་ཤེས་རབ་དང་ཐབས་མ་ཡིན་པའོ། །
སྐད་ཅིག་ཀྱང་ནི་ཡུད་ཙམ་དུ་ཡང་ངོ་། །

[Block 2183]
དངོས་གྲུབ་འདོད་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོ་དབྱེར་མེད་པའི་ཕྱིར་རོ། །

[Block 2184]
མི་གནས་པ་ནི་གཞན་པའི་སེམས་སོ། །

[Block 2185]
ད་ནི་བསྟན་པ་དེ་བཤད་པའི་ཕྱིར་ཡང་དང་པོ་གོམས་པར་བྱེད་དུས་ནི་བཟང་པོར་རྟག་ཏུ་འབྲེལ་ཏེ།

[Block 2186 [VERSE]]
ལས་སྨིན་ཅིང་བྱང་བ་ལ་ཡང་མ་ཡིན་པའོ། །
གནས་ཀྱང༌[^955]སྔགས་པ་ནི་བདེ་བ་སྐྱེད་པ༌[^956]འཆད་པར་འགྱུར་བའོ། །
སེམས་གཅིག་མཉམ་གཞག་ནི་དེའི་ཡོན་ཏན་ནོ། །
གནས་བཟང་པོ་ནི་དེས་ཡོན་ཏན་སྐྱེད་པའི་ཕྱིར་རོ། །

[Block 2187]
རང་ཁྱིམ་ནི་རྣལ་འབྱོར་པའི་འོ། །

[Block 2188]
མཚན་དུས་ནི་ནེ་སེ་ག་ལ་སྟེ་དུས་སམ་དུས་མཚན་མ་རྒྱུ་བའི་གནས་སོ། །

[Block 2189]
གྲུབ་པའི་སེམས་ནི་ཕྱག་རྒྱ་ཆེན་པོ་ལ་དམིགས་པའོ། །

[Block 2190]
རྣལ་འབྱོར་མ་བསྒོམ་ནི་འདོད་པའི་ལྷ་བདག་མེད་པའོ།[^957] །

[Block 2191 [VERSE]]
ཤེས་རབ་ཅན་ནི་ནམ་མཁའ་ལྟ་བུའོ། །
ཡང་ན་ནི་འདོད་པའི་ལྷ་མོས་ཕྱོགས་གཞན་དུའོ། །
ཧེ་རུ་ཀ་དཔལ་ནི་དགྱེས་པའི་རྡོ་རྗེའོ། །

[Block 2192]
དེ་ཡང་ལ་ལ་དག་ཕྱག་བཅུ་དྲུག་པ་ཁོ་ན་ལ་འདོད་དོ། །

[Block 2193]
འདིར་ནི་རྡོ་རྗེ་བདག་མེད་མ་དང་གཉིས་ཀྱིས་མྱུར་བ་ཉིད་དུ་ཕྱག་རྒྱ་ཆེན་པོ་བསྒྲུབ་པར་འདོད་དེ། འོ་ན་ལྷ་གཞན་དག་གིས་མ་ཡིན་ཞེ་ན། གཞན་དག་གིས་ནི་མྱུར་བ་ཉིད་དུ་ཕྱག་རྒྱ་ཆེན་པོ་ཐོབ་པ་མ་ཡིན་ཏེ། སོ་སོར་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་སོ་སོར་ངེས་པའི་ཕྱིར། སཱ་ལུ་ལ་སོགས་པའི་ས་བོན་བཞིན་ནོ། །

[Block 2194]
ཇི་སྐད་དུ་ཡང་།

[Block 2195 [VERSE]]
འཇམ་དཔལ་གྱིས་ནི་བློ་འཕེལ་བྱེད། །
སོ་སོར་འབྲང་མ༌[^958]བྱིས་པ་སུན། །
ནག་པོ་ཆེན་པོས་ཚར་གཅོད་འགྱུར། །

[Block 2196]
ཞེས་རྒྱ་ཆེར་གསུངས་སོ། །

[Block 2197]
དེ་ནས་ཧེ་རུ་ཀ་ཕྱག་བཅུ་དྲུག་པ་དང་བདག་མེད་མའི་གཟུགས་ནི་ཚུལ་ལམ་རང་བཞིན་ནོ། །

[Block 2198]
ཐབས་རྒྱ་མཚོ་ལྟ་བུའོ། །

[Block 2199]
དེའི་ཕྱིར་ཏུམྤི་སྟེ་ཀུ་བ་ལྟ་བུ་མ་ཡིན་པའི་གནས་ཡོན་ཏན་དང་བཅས་པའོ། །

[Block 2200]
ཡང་སྤྱོད་ལམ་གྱི་དུས་སུ་ཡང་ཡོན་ཏན་དང་བཅས་པ་བསྟན་པའི་ཕྱིར།

[Block 2201 [VERSE]]
རྐང་པ་འཁྲུ་བ་ལ་སོགས་པ་ནི་གོ་སླའོ། །
བརྟུལ་ཞུགས་ཅན་ཐབས་དང་བཅས་པའི་ཧེ་རུ་ཀར༌[^959]མོས་པའོ། །

[Block 2202]
རྣལ་འབྱོར་མ་ནི་ཤེས་རབ་དང་བཅས་པའི་བདག་མེད་མ་སྟེ་ལོངས་སྐུའོ། །

[Block 2203 [VERSE]]
རྣམ་པར་བསྒོམ་པ་ནི་ལོངས་སྤྱོད་ལ་མོས་པའོ། །
གཞན་པའི་ཚུལ་ལ་སོགས་པ་ནི་སྔ་མ་ལྟར་རོ། །
ད་ནི་མཉམ་པར་གཞག་པ་བསྟན་པའི་ཕྱིར། །

[Block 2204]
བསམ་གཏན་ནི་དབྱེར་མེད་པ་དང་ལྡན་པའི་རྩེ་གཅིག་པའོ། །

[Block 2205]
ཉོན་མོངས་པ་ནི༌[^960]འཇིགས་པའི་ཡོན་ཏན་ནོ། །

[Block 2206]
རྡོ་རྗེ་སྙིང་པོ་ནི་བོད་པའོ།[^961] །ང་ཡིས་བཤད༌[^962]ནི་བཅོམ་ལྡན་འདས་ཉིད་ཀྱི་ཞལ་གྱིས་བཞེས་པའོ། །

[Block 2207]
བརྩེ་བ་ནི་སེམས་ཅན་དོན་དུ་སྟེ་གཞན་དུའོ། །

[Block 2208 [VERSE]]
དངོས་གྲུབ་དོན་ནི་བདག་དོན་ནོ། །
ཡང་བསྡུ་བ་ནི་ཕྱོགས་གཞན་མ་ཡིན་ནོ། །

[Block 2209]
ཟླ་བ་ཕྱེད་དུ་རྟོགས་ནི་བསྒོམ་པ་སྟེ་དུས་མྱུར་བའི་ཚད་དོ། །

[Block 2210]
བསམ་པ་ཐམས་ཅད་སྤངས༌[^963]ནི་ཉོ་ཚོང་དང་ཞིང་ལས་ལ་སོགས་པའོ། །
--- END BLOCKS ---
