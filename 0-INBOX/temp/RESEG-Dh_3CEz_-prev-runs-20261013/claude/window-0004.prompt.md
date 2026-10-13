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
[Block 141]
ཤྲུ་ཏ་སྟེ་དགོངས་པའི་སྐད་དུ་ཐོས་པ་དེའི་དབང་གིས་དུས་ལ་སོགས་པའི་སྐབས་ངག་བརྡ་དང་ལུས་བརྡས་སྨྲའོ། །

[Block 142]
ཨེ་ཀ་སྨིན༌[^73]ས་མ་ཡ་སྟེ་དགའ་བ་རྣམས་དང་སྐད་ཅིག་གི་དུས་སུ་གཅིག་པ་སྟེ། ཤེས་པ་སྐྱེས་པའི་ཚུལ་སྤོང་བ་དང་ཐོབ་པའི་ཚུལ་དུ་འབྱུང་བའོ། །

[Block 143]
ཡང་བཟའ་བ་སྟོན་མོའི་དུས་སུ་དམ་ཚིག་གཅིག་པའོ། །

[Block 144]
དེ་དག་གིས་ཀྱང་བརྗོད་བྱའི་ཆོས་ཐམས་ཅད་དང་རྗོད་བྱེད་ཀྱི་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་རྣམས་དཔལ་དགྱེས་པའི་རྡོ་རྗེར་འདུས། དུས་ཟླ་བ་དང་ལོ་ལ་སོགས་པར་བསྒོམས་པས་དང་པོ་སྤྲིན་དང་འདྲ་བ་དང་།

[Block 145 [VERSE]]
གཉིས་པ་དུ་བ་ལྟ་བུ་སྟེ། །
གསུམ་པ་སྲིན་བུ་མེ་ཁྱེར་འདྲ། །
བཞི་པ་མར་མེ་ལྟ་བུ་སྟེ། །
ལྔ་པ་ཐམས་ཅད་སྣང་བ་སྟེ། །

[Block 146]
སྤྲིན་མེད་ནམ་མཁའ་ལྟ་བུའོ། །

[Block 147]
གཟུང་བ་དང་བྲལ་བ་དང་། འཛིན་པ་དང་བྲལ་བ་དང་། གཉིས་ག་དང་བྲལ་བ་དང་། ཡེ་ཤེས་རང་རིག་འཆར་བ་དང་།

[Block 148 [VERSE]]
ཆོས་ཉིད་མཐོང་བ་ལྔ་བའོ། །
རྗེས་ཐོབ་སྒྱུ་མའི༌[^74]རྨི་ལམ་སོགས། །
སྒྱུ་མའི་དཔེ་བརྒྱད་རིམ་པར་མཐོང་། །
དེ་ལ་སྤྱོད་པ་རྣམ་གསུམ་བྱ། །

[Block 149]
དེ་ནས་འབྲས་བུ་གོ་འཕང་གནས། །ཞེས་བྱ་སྟེ། གང་ཟག་སྤྲོས་པ་ལ་དགའ་བས་ལམ་དེ་བསྒོམ་མོ། །

[Block 150 [HEADING]]
###### **དེ་ཉིད་རྫོགས་པའི་རིམ་པར་བསྒོམ་པ།** ^1-1-1-2-1-2-0

[Block 151]
དེ་ཉིད་རྫོགས་པའི་རིམ་པར་བསྒོམ་པ་ནི་གསུམ་སྟེ། གང་ཟག་དབང་པོ་དམན་པ་ཆགས་པ་ཤས་ཆེ་བས་གཞན་ལུས་ལ་བརྟེན་པ་དང་དབང་པོ་འབྲིང་ཆགས་པ་ཡང་འབྲིང་ནི་རང་ལུས་དང་ལྡན་པ་དང་དབང་པོ་རབ་ཆགས་པ་ཆུང་བས་དབྱེར་མེད་ཕྱག་རྒྱ་ཆེན་པོ་དང་ལྡན་པའོ། །

[Block 152 [HEADING]]
###### **གཞན་ལུས་ལ་བརྟེན་པ།** ^1-1-1-2-1-2-1-0

[Block 153]
དེ་ལ་དབང༌[^75]བསྐྱེད་པའི་རིམ་པ་ཉུང་ལྡན་ཏེ་སྔར་མཎྜལ་དང་མཆོད་པ་ཅུང་ཟད་ཙམ་ལ་བརྟེན་པའི་སྒྲུབ་པ་པོས་མོས་པའི་རྣལ་འབྱོར་རམ། བསྐྱེད༌[^76]པའི་རྣལ་འབྱོར་རམ་བྱིན༌[^77]གྱིས་ཐ་མལ་གྱི་རྣམ་པ་བསྒྱུར་ཏེ། དེ་ཡང་། བདག་མེད་རྣལ་འབྱོར་ལྡན་པའམ། ཡང་ན་ཧེ་རུ་ཀ་དཔལ་བརྩོན། །ཞེས་པ་རྟེན་ཁྱད་པར་ཅན་ནམ་ལྷན་ཅིག་བསྒོམས་ལ། ལས་ཀྱི་ཕྱག་རྒྱ་ཡང་འོག་ནས་གཡུང་མོ་རྡོ་རྗེ་རིགས་ཞེས་བྱ་བ་དང་། གཞན་གྱི་རིགས་ལས་བྱུང་བའམ།

[Block 154 [VERSE]]
གང་གི་སྲིན་ལག་རྩ་བ་ན། །
རྡོ་རྗེ་རྩེ་དགུ་པར་གྱུར་པ། །

[Block 155]
ཞེས་བྱ་བ་ལ་སོགས་པས་བརྟགས་ཤིང་བཙལ་ལ།

[Block 156 [VERSE]]
དགེ་བ་བཅུ་ནས་བརྩམས་ནས་ནི། །
དེ་ནི༌[^78]ཆོས་ནི་རབ་ཏུ་དབྱེ། །

[Block 157]
དབང་བསྐུར་སྙིང་རྗེར་ལྡན་པ་དེ་དང་ལྷན་ཅིག་བསྒོམས་ཏེ། དེ་ཡང་ལྷར་མོས་པ་ལ་སོགས་པ་བསྒོམས་ལ། སྟན་བདེ་བ་ལ་འདུག་སྟེ་དེ་ལ་ཨེ་སྟེ་ཤེས་རབ་ཀྱི་གསང་བའི་གནས་སུ། ཝ་སྟེ་ཐབས་ཀྱི་གསང་བའི་གནས་སུ། ད་ཐིག་ལེ་ཟླ་བ་དང་ཉི་མ་འདྲེས་པའོ། །

[Block 158]
དེ་ཉིད་སྟོན་པའི་བདག་ཉིད་མ༌[^79]ཡཱ་སྟེ་ཕྱག་རྒྱའི་བདག་པོ་བསྒོམ་མོ། །

[Block 159]
ཤྲུ་ཏ་ནི་འཛག་ཅིང་རྒྱུ་བ་སྟེ་སེམས་དབབ་པ་དང་གཟུང་བ་དང་བཟློག་པ་ལ་སོགས་པའོ། །

[Block 160]
དུས་གཅིག་ནི་ལྷན་ཅིག་སྐྱེས་པའི་དགའ་བའི་དུས་སུ་གཅིག་པ་སྟེ།

[Block 161 [VERSE]]
དགའ་བ་གསུམ་གྱི་རིམ་གྱིས་བསྐྱེད་ནས་བསྒོམ་པའོ། །
བཅོམ་ལྡན་འདས་དེ་ཐིག་ལེ་དེ་སྟོན་པར་བཤད་དེ།
བཅོམ་ལྡན་འདས་ལ་སོགས་པའི་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 162]
དེ་བཞིན་གཤེགས་པ་ནས་བྷ་ག་རྣམས་ལ་ཡིས་ནི་ཨེ་ཝཾ་དེ་གནས་སུ་བསྟན་པའི་ཕྱིར་ཡོན་ཏན་གྱི་ཁྱད་པར་བརྗོད་པའོ།[^80] །དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ཕུང་པོ་ལྔ་དང་ལུས་ངག་ཡིད་གསུམ་ཧྲྀ་ད་ཡ་བཅུད་དུ་བསྡུས་པ་བཙུན་མོ་ནི་ཕྱག་རྒྱའི་ཕུང་པོ་དང་འབྱུང་བས་བསྡུས་པས་ཧྲྀ་ད་ཡ་སྟེ་ཐིག་ལེར་གསང་བའི་གནས་སུ་བཞུགས་ཞེས་བྱ་སྟེ། ས་སྟེངས་སུ་ཟུང་ས་འོག་ཏུ་གནས་པ་སྟེ། དེ་ཡང་།

[Block 163 [VERSE]]
གཉིས་འདས་ནས་ནི་གཉིས་གནས་པ། །
རྒྱུ་ལ་འབྲས་བུས་རྒྱས་གདབ་པའམ། །
འབྲས་བུ་ལ་ཡང་རྒྱུས་རྒྱས་གདབ། །

[Block 164]
ཅེས་བྱ་བས་གནས་པའམ། ལུས་ཀྱི༌[^81]བཛྲ་ཨངྒ་ལ་སོགས་པས་བཞུགས་པའོ། །

[Block 165]
དེ་ཡང་ཐུན་དང་པོ་ཆུང་ངུ་རུ་བསྒོམ་ཞིང་དེ་ནས་ཇེ་ཆེ་ཇེ་ཆེར་བསྲིང༌[^82]ཞིང་བསྒོམས་པས་རྟགས་འབྱུང་སྟེ། །སེམས་ཟིན་པའི་རྟགས་ནི་རྒྱལ་པོ་དཔུང་བུ་ཆུང་གིས་མི་བསྐྱོད་པ་ལ་སོགས་པ་འབྱུང་བའོ། །

[Block 166]
དེ་ཁོ་ན་ཉིད་ལ་འཇུག་པའི་རྟགས་ནི་སྔ་མའི་རྣམ་པ་ལྔ་པོ་འབྱུང་ངོ་། །དངོས་གྲུབ་འགྲུབ་པའི་རྟགས་ནི་ཐིག་ལེ་སྔ་མ་དེ་མིག་ཏུ་བསྒོམས་པས་མིག་གི་མངོན་པར་ཤེས་པ་འབྱུང་ངོ་། །དེ་བཞིན་དུ་རྣ་བ་དང་ལུས་དང་ཡིད་ཀྱི་གནས་སུ་བསྒོམས་ན་མངོན་པར་ཤེས་པ་རྣམས་འབྱུང་ངོ་། །

[Block 167 [HEADING]]
###### **རང་ལུས་དང་ལྡན་པ།** ^1-1-1-2-1-2-2-0

[Block 168]
རང་ལུས་ཡང༌[^83]ནི་ཡང་སྒྲུབ་པ་པོས་སྔ་མ་ལྟར་སྔོན་དུ་འགྲོ་བ་རྣམས་བསྒོམས་ལ་ཨེ་སྟེ་སྐྱེ་གནས་སུ། བ་སྟེ་སྤྱི་བོའི་གནས་ལ་སོང༌[^84]སྟེ་ཐིག་ལེའི་ཚུལ་དུ་འཁྲིགས་ཤིང་གནས་པ་དང་། རྒྱུན་མི་འཆད་པར་རྒྱུ་བའོ། །

[Block 169]
མ༌[^85]ཡཱ་ནི་བདག་ཉིད་དེ་རང་གི་ལུས་སུ་བསྒོམ་པའོ། །

[Block 170]
དུས་གཅིག་ནི་ཡང་ལྷན་ཅིག་སྐྱེས་པའི་དགའ་བ་སྟེ། དམ་ཚིག་གི་དགའ་བ་བཞི་ལུགས་འབྱུང་དང་ལུགས་བཟློག་ཏུ་སྐྱེ་སྟེ་དེ་ལས་ལྷན་ཅིག་སྐྱེས་པ་བསྒོམ་མོ། །

[Block 171]
བཅོམ་ལྡན་འདས་ནི་རང་ལུས་སུ་བསྒོམ་པ་དེས་མི་མཐུན་པ་འཇོམས་པ་དང་ཡེ་ཤེས་དང་ལྡན་ཏེ་རང་རང་ངོ་བོ་མཚོན་བྱ་མཚོན་བྱེད་མྱོང་བ་དེས་མཚོན་བྱ་གཉུག་མའི་ཡེ་ཤེས་དྲུངས་ཕྱུང་སྟེ། དམ་ཚིག་གི་དགའ་བ་ཆུ༌[^86]སྐྱོགས་གང་གི་ལན་ཚྭ་རྒྱ་མཚོའི་ཆུར་གི་གཏོགས༌[^87]པ་ལྟ་བུར་ཤེས་པའོ། །

[Block 172]
དེ་བཞིན་གཤེགས་པ་རྣམས་ཐམས་ཅད་ནི་ཕུང་པོ་ལྔའོ། །

[Block 173 [VERSE]]
སྐུ་གསུང་ཐུགས་ནི་སྒོ་གསུམ་མོ། །
བཙུན་མོ་ནི་འབྱུང་བ་དག་པའོ། །

[Block 174]
བྷ་ག་རྣམས་ལ་ཡིད་ནི་ཆོས་ཀུན་རང་གི་ལུས་སུ་བསྒོམས་པས་མི་མཐུན་པ་འཇོམས་པ་དང་ཡེ་ཤེས་དང་ལྡན་པས་སོ། །

[Block 175]
བཞུགས་སོ་ཞེས་པ་ནི་ལུས་གདོད་མ་ནས་རང་ཉིད་ཀྱིས་དག་པའོ། །

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
--- END BLOCKS ---
