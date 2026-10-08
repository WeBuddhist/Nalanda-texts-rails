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
[Block 1331]
སྐབས་ཁ་ཅིག་ཏུ་ཧེ་རུ་ཀ་རྣམས་ལ་སྦྱར་ཞེས་གསུངས་སོ། །

[Block 1332]
ད་ནི་གཞན་སེལ་བ་བསྟན་པའི་ཕྱིར། ཨཱ་ལི་ཀཱ་ལི་ལ་སོགས་པ་གསུངས་ཏེ།

[Block 1333 [VERSE]]
ཨཱ་ལི་ཀཱ་ལི་ནི་སྔར་གྱི་རྐྱེན་གཉིས་སོ། །
མཉམ་སྦྱོར་བ་ནི་རྒྱུ་ས་བོན་བསྐུལ་བའོ། །

[Block 1334]
རྡོ་རྗེ་སེམས་དཔའ༌[^645]ནི་འབྲས་བུ་བདེ་བ་ཆེན་པོའི་རྒྱུའི་རྡོ་རྗེ་འཆང་བདག་མེད་མའི་རང་བཞིན་དུ་བསྟན་པའོ། །

[Block 1335]
གདན་ཞེས་པ་ནི་རྐྱེན་ཇི་ལྟར་བྱ་ཞེ་ན། ལ་ལ་དག་མ་རྫོགས་པའི་རྡོ་རྗེ་སེམས་དཔར༌[^646]འདོད་དེ། རྡོ་རྗེ་ནི་མཚན་མའོ།[^647] །སེམས་དཔའ་ནི་ས་བོན་ཏེ་གདན་ནི་ཉི་མ་དང་ཟླ་བའོ། །

[Block 1336]
ཁ་ཅིག་ནི་ཟླ་བ་ཉི་མ་ཆ་ཕྲུགས་གཉིས་སུ་བྱ་སྟེ། ཆ་གཅིག་ཞུ་ནས་རྡོ་རྗེ་སེམས་དཔར་གྱུར། ཆ་གཅིག་རྡོ་རྗེ་སེམས་དཔའི་གདན་གྱི་སྦྱོར་བ་བྱས་པ་ལ་འདོད་དོ། །

[Block 1337]
ཁ་ཅིག་ནི་བཏགས་ཏེ་བསྟན་པ་ཡིན་ཏེ། རྡོ་རྗེ་འཆང་བསྐྱེད་པའི་དུས་སུ། ཉི་ཟླ་གཉིས་ཀྱིས་གདན་གྱི་སྦྱོར་བ་བྱས་པས། རྡོ་རྗེ་སེམས་དཔའ་རྫོགས་པ་ལ་ཡང་འབྲས་བུ་ལ་ཡང་རྒྱུའི་མིང་བཏགས་ཏེ། གདན་ཅན་ཞེས་བསྟན་ཏེ་དཔེར་ན་ནས་རྒྱུའི་དུས་ན་རྐྱེན་ལུད་མང་པོ་དང་ལྡན་པར་བྱས་པ་ལ་འབྲས་བུ་སྨིན་པའི་དུས་སུ་འདི་ལུད་ཆེན་པོ་དང་ལྡན་པའོ་ཞེས་ཟེར་བ་ལྟ་བུའོ། །

[Block 1338]
གཞུང་སྔ་མ་གཉིས་པོ་ནི་མཛེས་པ་མ་ཡིན་ནོ། །

[Block 1339]
ཕྱི་མ་འདོད་པའོ། །

[Block 1340]
ཡི་གེ་ལས་བྱུང་ཞེས་པ་ནི་བསྐུལ་བའི་རྒྱུ་ཉིད་དོ། །

[Block 1341]
གོང་བུ་ནི་པིནྟ་སྟེ་འདུས་པའི་འབྲས་བུའི་ཚུལ་རྡོ་རྗེ་སེམས་དཔའི་གཟུགས་སོ། །

[Block 1342]
ཧཱུཾ་ཕཊ་ཡི་གེ་འདོད་མི་བྱ། །ཞེས་པ་ནི་རྒྱུའི་རྡོ་རྗེ་འཆང་རྗེས་སུ་ཆགས་པའི་ཞུ་བ་ལས་མི་བསྐྱོད་པའོ། །

[Block 1343 [VERSE]]
སེམས་དཔའི་གཟུགས་བརྙན་ལས་བྱུང་བ། །
ཞེས་པ་ནི་རྒྱུའི་རྡོ་རྗེ་འཆང་གྱུར༌[^648]པའོ། །

[Block 1344]
ཧཱུཾ་ཧཱུཾ་ཕཊ་ཕཊ་དྲག་པོ་ཡང་མི་འདོད་པའོ། །

[Block 1345]
ཐུགས་ཀའི་ཨཾ་གིས་རྐྱེན་བྱས་ནས། ཤིང་འབྲས་ཚོས་པ་ལྟ་བུར་རྡོ་རྗེ་འཆང་དཀར་པོ་རྡོ་རྗེ་བདག་མེད༌[^649]མ་ནག་མོ་ཅིག་ཏུ་གྱུར་ཏོ། །

[Block 1346]
དེ་སྐད་དུ་ཡང་། །

[Block 1347 [VERSE]]
རྡོ་རྗེ་སེམས་དཔའ་ལས་བྱུང་བའི། །
རིག་མའི་སྐྱེས་བུ་དམ་པར་བསྒོམ། །

[Block 1348]
ཞེས་གསུངས་སོ།

[Block 1349]
[^650] །དེ་ཉིད་བཤད་པ། དཀྱིལ་འཁོར་བདག་མོ་རྣམ་པར་བསྒོམ། །ཞེས་པ་ནི་འབྲས་བུའི་ཧེ་རུ་ཀ་ལྟ་བུར་གྱུར་པའོ། །

[Block 1350]
དེའི་མཚན་ཉིད་ཅི་འདྲ་སྙམ་པ་ལ། ཕྱག་མཚན་ཞལ་སོགས་གོང་མ་བཞིན། །ཞེས་པ་ནི་རྡོ་རྗེ་ལུ་གུ་རྒྱུད་མ་དང་ཕག་མོ་ལྟ་བུའོ། །

[Block 1351]
ཟླ་བ་ཆུ་ཤེལ་ནོར་བུའི་འོད། །ཅེས་པ་ནི་སློབ་དཔོན་དག་གིས་གཞན་དག་དུ་མར་བཤད་ཀྱིས་ཀྱང་། འདིར་ནི་བདག་མེད་མའི་རང་བཞིན་གྱི་དཔེ་སྟོན་ཏེ། དེ་ཡང་ཤེས་རབ་ཀྱི་དཔེ་ནི་ཟླ་བ་དང་ཆུ་ཤེལ་ལྟར་དང་ཞིང་གསལ་བའོ། །

[Block 1352]
ཐབས་ཀྱི་དཔེ་ནི་འོད་ཟེར་ལྟ་བུར་སྣང་བའོ། །

[Block 1353]
དེ་དག་གི་དོན་ནི་ཐབས་ཤེས་རབ་རང་བཞིན་ཏེ། དེ་ཡང་བདག་མེད་མའི་རང་བཞིན་ནི་ཤེས་རབ་ཡིན་ལ། ཐབས་ནི་གནས་སྐབས་དེ་རང་བཞིན་ཏེ༌[^651]ཐ་མའོ།[^652] །དེའི་ཕྱིར་གོང་གི་དཔེ་བསྟན་པའོ། །

[Block 1354]
ད་ནི་འཁོར་རྒྱས་པར་བསྟན་པའི་ཕྱིར།

[Block 1355 [VERSE]]
འདི་ལྟར་ཐམས་ཅད་རྫོགས་པ་ཉིད། །
ཅེས་བྱ་བ་ནི་བསྟན་པའོ། །

[Block 1356]
ད་ནི་བཤད་པ་སྟེ།

[Block 1357 [VERSE]]
ཟླ་བ་ཉི་མའི་རབ་དབྱེ་བས། །
ཞེས་པ་ནི་རྐྱེན་གཉིས་སོ། །
ཨཱ་ལཱི་ཤེས་རབ་ཀཱ་ལི་ཐབས། །
ཞེས་པ་ནི་རྐྱེན་གྱི་རང་བཞིན་ནོ། །

[Block 1358 [VERSE]]
ཡི་གེའི་དབྱེ་བ་སོ་སོ་ཡིན། །
ཞེས་པ་ནི་ས་བོན་ནོ། །

[Block 1359]
ཟླ་བ་དང་ཉི་མ་དང་ས་བོན་སོ་སོ་ལས་མཚན་མ་གྲི་གུག །ལྟེ་བ་ལ་ས་བོན་གྱིས་མཚན་པ་དེ་ལས་སྤྲོས་པ་དང་བསྡུས་ནས་གཅིག་ཏུ་ཞུ་བ་དང་། དེ་ནས་སོ་སོའི་སྐུར་བསྐྱེད་པ་མངོན་པར་བྱང་ཆུབ་པ་ལྔ་སྔ་མ་བཞིན་སྦྱར་རོ། །

[Block 1360]
དཀར་མོ་ལ་སོགས་པ་རྡོ་རྗེ་རྣལ་འབྱོར་མ་སྔོན་དུ་ཡོད་ཀྱང་དཀར་མོ་སྔོན་ལ་སྨོས་པ་ནི་ཚོར་བའི་ཕུང་པོ་གཙོ་བོའམ་ཕྱིའི་དཀར་མོ་དང་གཉིས་སུ་གཟུང་བའི་དོན་དུ་སྨོས་པའོ། །

[Block 1361]
འབྲས་བུའི་ལྷ་རྣམས་སོ་སོར་གྲུབ་པའོ། །

[Block 1362]
རེ་ཞིག་ནང་གི་རིམ་པ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་བཞི་དང་ཡང་ཚིགས་སུ་བཅད་པ་བཞི་དང་གཉིས་དང་རྐང་པ་གཉིས་དང་ཚིགས་སུ་བཅད་པ་གཉིས་ཀྱིས་ནི་བསྐྱེད་པ་ལྷ་རྣམས་ཀྱི་གནས་དང་ཆ་བྱད་དང་དེ་ཁོ་ན་ཉིད་དང་ཡོན་ཏན་དང་རྣམ་པར་དག་པས་བཤད་པ་སྟེ་གོ་སླའོ། །

[Block 1363]
བསྐྱེད་རིམ་གྱི༌[^653]ཞེན་པ་སྤངས༌[^654]པའི་ཕྱིར་རྫོགས་རིམ་ལ་འཇུག་པའི་ཡན་ལག་དྲུག་གི་རྣལ་འབྱོར་བསྟན་པ་སྟེ། འདིས་ནི་འཁོར་ལོ་རྣམ་བསྒོམས་ནས།

[Block 1364 [VERSE]]
དངོས་གྲུབ་མྱུར་དུ་ཐོབ་པར་འགྱུར། །
ཞེས་པ་ནི་སེམས་དཔའ་སུམ་བརྩེགས༌[^655]དང་། །

[Block 1365]
ཡེ་ཤེས་ཀྱི་འཁོར་ལོ་དགུག་པ་དང་སྐུ་གསུང་ཐུགས་དང་སྐྱེ་མཆེད་བྱིན་གྱིས་བརླབ་པ་དང་། དབང་བསྐུར་བ་དང་མཆོད་པ་དང་བསྟོད་པ་དང་བདུད་རྩི་མྱང་བ་སྟེ། རེག་པའི༌[^656]རྣལ་འབྱོར་བསྟན་ཏོ།[^657] །དེ་ལ་སེམས་གཟུང་བ་ནི་གྲངས་ལ་བསླབ་པ་དང་། [^658]དབྱིབས་ལ་བསླབ་པ་དང་། ཁ་དོག་ལ་བསླབ་པ་དང་ཕྱག་མཚན་དང་རྒྱན་དང་ཆ་ལུགས་ཀྱི་བར་དུ་སེམས་གཟུང་ངོ་། །ཕྲ་མོ་ལ་བསླབ་པ་ནི།

[Block 1366]
དང་པོ་ནག་པོ༌[^659]རབ་ཏུ་བསྒོམ། །ཞེས་པ་ལ་སོགས་པ་ནི་སྙིང་གར་ཧཱུཾ་ནག་པོ་གཅིག །

[Block 1367 [VERSE]]
དམར་པོ་ནི་མགྲིན་པར་ཨཱཾ་ངོ་། །
སེར་པོ་ནི་དཔྲལ་བར་ཛྲཱྀཾ་ངོ་། །
ལྗང་གུ་ནི་ལྟེ་བར་ཁཾ་ངོ་། །
སྔོན་པོ་ནི་ནམ་ཚོང་དུ༌[^660]ཧཱུཾ་ངོ་། །

[Block 1368]
དཀར་པོ་ནི་སྤྱི་བོར་བྷྲཱུཾ་མོ། །

[Block 1369]
དེ་རྣམས་ནི་དེ་བཞིན་གཤེགས་པ་དྲུག་གི་ངོ་བོ་ཡང་རྫོགས་པའི་རིམ་པ་ལ་འཇུག་པའི་ཡན་ལག་ཏུ་དཀྱིལ་འཁོར་གྱི་ཁ་དོག་རིམ་པ་དྲུག་ཏུ་ཡང་བསྒོམ་སྟེ་རགས་པ་ལྷའི་ཞེན་པ་སྤོང་ངོ་། །རང་བཞིན་དེ་བཞིན་གཤེགས་པ་དྲུག་ཏུ་རྒྱས་གདབ་པའོ། །

[Block 1370]
དགའ་བྲལ་མཐར་ཡང་དེ་བཞིན་ནོ། །ཞེས་པ་ནི་ཟབ་པའི་རྣལ་འབྱོར་བསྟན་པ་སྟེ་འོག་ནས་རྒྱས་པར་འཆད་དོ། །
--- END BLOCKS ---
