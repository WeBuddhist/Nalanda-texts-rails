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
[Block 1961]
ཅིག་ཤོས་ཀྱིས༌[^1275]སྨྲས་པ་ཁྱོད་ཀྱིས་ལོག་པར་བཟུང་སྟེ། ལག་ན་མདུང་རྩེ་གསུམ་པ་ཐོགས་པ་ནི་དབང་ཕྱུག་ཆེན་པོའོ། །

[Block 1962]
ལག་ན་འཁོར་ལོ་ཐོགས་པ་ནི་སྲེད་མེད་ཀྱི་བུའོ། །ཞེས་དེ་གཉིས་རྩོད་པ་ན་ཉེ་འཁོར་ན་ཀུན་ཏུ་རྒྱུ་ཞིག་འདུག་པའི་གན་དུ་དོང་སྟེ་ཕྱག་འཚལ་ནས་དེ་ལ་རང་རང་གི་བསམ་པ་སྨྲས་པ་དང་། དེས་གཅིག་ལ་ནི་ཁྱོད་ཟེར་བ་བདེན་ནོ། །ཞེས་སྨྲས་པ་དང་། [^1276]ཅིག་ཤོས་ལ་ནི་མི་བདེན་ནོ། །ཞེས་གང༌[^1277]སྨྲས་ན།[^1278] དེ་ལ་ཀུན་ཏུ་རྒྱུ་དེས་ཇི་ལྟར་འདི་ན་དབང་ཕྱུག་ཆེན་པོ་ཡང་འགའ་ཡང་མེད་ལ། སྲེད་མེད་ཀྱི་བུ་ཡང་མེད་དེ། འདི་དག་ནི་རྩིག་པ་ལ་བརྟེན་པའི༌[^1279]རི་མོ་བྲིས་པའོ། །ཞེས་བྱ་བ་དེ་ལྟར་ཤེས་མོད་ཀྱི། འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་དབང་གིས་འདི་ནི་བདེན་ནོ། །

[Block 1963]
འདི་ནི་མི་བདེན༌[^1280]ནོ། །ཞེས་སྨྲས་པ་ལ་བརྫུན༌[^1281]གྱི་ཚིག་གི་སྐྱོན་ཅན་དུ་མ་གྱུར་པ་དེ་བཞིན་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་དངོས་པོ་རྣམས་ངོ་བོ་ཉིད་སྟོང་པར་གཟིགས་ཀྱང་། འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་དབང་གིས་འདི་ནི་ཡང་དག་པ་ཉིད་དོ། །

[Block 1964]
འདི་ནི་ཡང་དག་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1965 [VERSE]]
འདི་ནི་ཡང་དག་པ་ཉིད་དང་། །
ཡང་དག་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1966]
ཞེས་གསུངས་སོ། །

[Block 1967]
དོན་དམ་པར་ནི།

[Block 1968 [VERSE]]
ཡང་དག་མིན་མིན་ཡང་དག་མིན། །
དེ་ནི་སངས་རྒྱས་རྗེས༌[^1282]བསྟན་པའོ། །

[Block 1969]
དངོས་པོ་ངོ་བོ་ཉིད་སྟོང་པ་སྒྱུ་མ་དང་། རྨི་ལམ་དང་། སྨིག་རྒྱུ་དང་། གཟུགས་བརྙན་དང་། བྲག་ཆ་ལྟ་བུ་དག་ལ་ཇི་ལྟར་ཡང་དག་པ་ཉིད་དང་། ཡང་དག་པ་ཉིད་མ་ཡིན་པར་བརྗོད་དོ།[^1283] ། དེའི་ཕྱིར་དེ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་བསྟན་པ་ཡོད་པ་དང་། མེད་པ་ཉིད་ཀྱི་སྐྱོན་དང་བྲལ་བ། མུ་སྟེགས་བྱེད་ཐམས་ཅད་དང་ཐུན་མོང་མ་ཡིན་པ་དོན་དམ་པ་གསལ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 1970]
ཡང་ན་འདི་ནི་དོན་གཞན་ཏེ༌[^1284]ཁ་ཅིག་ན་རེ་ཐམས་ཅད་ཡོད་པ་ཉིད་ལས་སྐྱེའོ། །ཞེས་ཟེར་རོ། །

[Block 1971]
གཞན་དག་ན་རེ་རྒྱུ་ལ་འབྲས་བུ་སྔ་ན་མེད་པ་དག་ལས་སྐྱེའོ། །ཞེས་ཟེར་རོ། །

[Block 1972]
ཁ་ཅིག་ན་རེ་ཡོད་པ་དང་མེད་པ་ལས་སྐྱེའོ། །ཞེས་ཟེར་རོ། །

[Block 1973]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་བསྟན་པ་ནི་དངོས་པོ་རྒྱུ་དང་རྐྱེན་ལས་གདགས་པར་ཟད་ཀྱི་ཡོད་པ་དང་མེད་པ་ནི་མ་ཡིན་ནོ།[^1285] །དེ་ལྟར་ཡང་ཀཱ་ཏྱཱ་ཡ་ན་འཇིག་རྟེན་འདི་ནི་གཉིས་ལ་གནས་ཏེ། ཕལ་ཆེར་ཡོད་པ་ཉིད་ལ་གནས་པ་དང་། མེད་པ་ཉིད་ལ་གནས་སོ། །ཞེས་གསུངས་སོ། །

[Block 1974]
དེ་ལྟ་བས་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱིས་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་དབང་གིས་ཀྱང་དེ་དང་དེ་དག་གསུངས་པས། དེའི་ཕྱིར་དེ་ཁོ་ན་མཐོང་བར་འདོད་པ་རྣམས་ཀྱིས་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་དབང་གིས་གསུངས་པ་དག་ལ་མངོན་པར་མ་ཞེན་པར་བྱ་སྟེ།[^1286] དེ་ཁོ་ན་གང་ཡིན་པ་དེ་ཉིད་གཟུང་བར་བྱའོ། །

[Block 1975]
སྨྲས་པ། དེ་ཁོ་ནའི་མཚན་ཉིད་གང་ཡིན། བཤད་པ།

[Block 1976 [VERSE]]
གཞན་ལས་ཤེས་མིན་ཞི་བ་དང་། །
སྤྲོས་པ་རྣམས་ཀྱིས་མ་སྤྲོས་པ། །
རྣམ་རྟོག་མེད་དོན་ཐ་དད་མིན། །
དེ་ནི༌[^1287]དེ་ཉིད་མཚན་ཉིད་དོ། །

[Block 1977]
གཞན་ལས་ཤེས་མིན་ཞེས་བྱ་བ་ནི། འདི་ལ་གཞན་ལས་ཤེས་པ་མེད་པ་སྟེ། ལུང་མེད་པར་བདག་གི་མངོན་སུམ་དུ་འགྱུར་ཞིང་། བདག་ཉིད་ཀྱི་མངོན་སུམ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1978]
ཞི་བ༌[^1288]ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་སྟོང་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1979]
སྤྲོས་པ་རྣམས་ཀྱིས་མ་སྤྲོས་པ། །ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་གྱི་ཆོས་རྣམས་དང་བྲལ་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1980]
རྣམ་པར་རྟོག་པ་མེད་པ་ཞེས་བྱ་བ་ནི་འདི་ཞེས་བྱ་བ་དང་འདིའོ་ཞེས་རྣམ་པར་མ་བརྟགས་པའོ། །

[Block 1981]
དོན་ཐ་དད་པ་མ་ཡིན། ཞེས་བྱ་བ་ནི་འདི་ཡང་ཡིན་ལ། འདི་ཡང་ཡིན་ནོ། །ཞེས་དོན་དབྱེར་མེད་པའོ། །

[Block 1982]
དེ་ལ་གང་གི་ཕྱིར་རྣམ་པར་རྟོག་པ་མེད་པ་དེའི་ཕྱིར་སྤྲོས་པ་རྣམས་ཀྱིས་མ་སྤྲོས་པའོ། །

[Block 1983]
གང་གི་ཕྱིར་འཇིག་རྟེན་པའི་ཆོས་རྣམས་ཀྱིས་མ་སྤྲོས་པ་དེའི་ཕྱིར་ཞི་བའོ། །

[Block 1984]
གང་གི་ཕྱིར་ཞི་བ་དེའི་ཕྱིར་དོན་ཐ་དད་པ་མ་ཡིན་པ་སྟེ། དེའི་ཕྱིར་དེ་ལྟ་བུའི་རང་བཞིན་ཤེས་པ་རང་རིག་པ་གཞན་ལས༌[^1289]ཤེས་པ་མ་ཡིན་པ་གང་ཡིན་པ་དེ་ནི་དེ་ཁོ་ནའི་མཚན་ཉིད་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 1985]
འདི་ཡང་དེ་ཁོ་ནའི་མཚན་ཉིད་གཞན་ཡིན་ཏེ།

[Block 1986 [VERSE]]
གང་ལ༌[^1290]བརྟེན་ཏེ་གང་འབྱུང༌[^1291]བ། །
དེ་ནི་རེ་ཞིག་དེ་ཉིད་མིན། །
དེ་ལས་གཞན་པའང་མ་ཡིན་ཕྱིར། །
དེ༌[^1292]ཕྱིར་ཆད་མིན་རྟག་མ་ཡིན། །

[Block 1987]
འདི་ལྟར་གང་ལ་བརྟེན་ཏེ་གང་བྱུང་བ་དེ་ནི་རེ་ཞིག་དེ་ཉིད་མ་ཡིན་ནོ། །

[Block 1988]
དེ་ལས་གཞན་པའང་མ་ཡིན་ཏེ། གལ་ཏེ་དེ་དེ་ལས་གཞན་ཡིན་པར་གྱུར་ན་དེ་མེད་པར་ཡང་འབྱུང་བར་འགྱུར་བའི་རིགས་ན། མི་འབྱུང་བས་དེའི་ཕྱིར་དེ་ལས༌[^1293]གཞན་པའང་མ་ཡིན་ནོ། །

[Block 1989]
དཔེར་ན་ས་བོན་ལ༌[^1294]བརྟེན་ཏེ་མྱུ་གུ་བྱུང་བ་ནི་ས་བོན་གང་ཁོ་ན་ཡིན་པ་དེ་མྱུ་གུ་ཁོ་ན་མ་ཡིན་ལ་ས་བོན་ལས་གཞན་པ་མྱུ་གུའི་ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་ས་བོན་ལས་མྱུ་གུ་གཞན་པའང་མ་ཡིན་པ་བཞིན་ཏེ། དེ་ལྟར་གང་གི་ཕྱིར་གང་ལ་བརྟེན༌[^1295]ཏེ་གང་བྱུང་བ་དེ་དེ་ཉིད་ཀྱང་མ་ཡིན་ལ་དེ༌[^1296]ལས་གཞན་པའང་མ་ཡིན་པ་དེའི་ཕྱིར་ཆད་པ་ཡང་མ་ཡིན་ལ་རྟག་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1990]
འདི་ལྟར་ས་བོན་ཉིད་མྱུ་གུ་ཡིན་པར་གྱུར་ན། ས་བོན་རྟག་པར་འགྱུར་རོ། །

[Block 1991]
གང་གི་ཕྱིར་ས་བོན་ཉིད་མྱུ་གུ་མ་ཡིན་པ་དེའི་ཕྱིར་ས་བོན་རྟག་པ་མ་ཡིན་ནོ། །

[Block 1992]
གལ་ཏེ་ས་བོན་ཡང་གཞན་ཉིད་ལ་མྱུ་གུ་ཡང་གཞན་ཡིན་པར་གྱུར་ན་དེ་ལྟ་ན་ས་བོན་རྣམ་པ་ཐམས་ཅད་དུ་རྒྱུན་ཆད་པས་ཆད་པར་འགྱུར་རོ། །

[Block 1993]
གང་གི་ཕྱིར་ས་བོན་ལ༌[^1297]མྱུ་གུ་གཞན་མ་ཡིན་པ་དེའི་ཕྱིར་ས་བོན་ཆད་པ་མ་ཡིན་ཏེ། སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།

[Block 1994 [VERSE]]
གང་ཕྱིར་དངོས་པོ་འཇུག་འགྱུར་བ། །
དེས་ན་ཆད་པར་མི་འགྱུར་རོ། །
གང་ཕྱིར་དངོས་པོ་ལྡོག་འགྱུར་བ། །
དེས་ན་རྟག་པར་མི་འགྱུར་རོ། །

[Block 1995]
ཞེས་གསུངས་སོ། །

[Block 1996]
དེ་ལྟ་བས་ན། དེ་ཡང་དེ་ཉིད་དང་གཞན་ཉིད་དུ་བརྗོད་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར། རྟག་པ་ཡང་མ་ཡིན་ལ་ཆད་པ་ཡང་མ་ཡིན་པས་དེ་ཁོ་ནའི་མཚན་ཉིད་ཡིན་ནོ། །

[Block 1997 [VERSE]]
དོན་གཅིག་མིན་དོན་ཐ་དད་མིན། །
ཆད་པ་མ་ཡིན་རྟག་མིན་པ། །
དེ་ནི་སངས་རྒྱས་འཇིག་རྟེན་གྱི། །
མགོན་པོས༌[^1298]བསྟན་པ་བདུད་རྩི་ཡིན། །

[Block 1998]
དེ་ལྟར་མཐོ་རིས་དང་བྱང་གྲོལ་གྱི་ལམ་རྣམ་པར༌[^1299]འབྱེད་པ་དོན་གཅིག་པ་ཉིད༌[^1300]མ་ཡིན་ན༌[^1301]དོན་ཐ་དད་པ་མ་ཡིན་པ། ཆད་པ་མ་ཡིན་པ་རྟག་པ་མ་ཡིན་པ། གཅིག་པ་དང་ཐ་དད་པ་དང་ཆད་པ་དང་རྟག་པའི་སྐྱོན་ལས་ཕྱི་རོལ་དུ་གྱུར་པ། མཆོག་ཏུ་ཟབ་པ། དོན་དམ་པའི་དེ་ཁོ་ན་གསལ་བར་བྱེད་པ་དེ་ནི་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་བདེ་བ་ཐོབ་པར་བྱ་བའི་ཕྱིར། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཐམས་ཅད་མཁྱེན་པ་ཐམས་ཅད་གཟིགས་པ། སྟོབས་བཅུའི་སྟོབས་དང་ལྡན་པ། རྒྱུ་མེད་པར་བྱམས་པ་རྣམས་ཀྱིས༌[^1302]བསྟན་པ་བདུད་རྩི་ཡིན་ཏེ། དེ་བསྒྲུབ་པར༌[^1303]བྱའོ། །

[Block 1999]
འདི་ལྟར་དེར་ཞུགས་པ་རྣམས་ཀྱི་བདག་ཉིད་ཀྱི་མངོན་སུམ་དུ་གྱུར་པ་འཕྲལ་ཁོ་ན་ལ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 2000]
གང་དག་ཚོགས་མ་བྱས་པ་ཉིད་ཀྱིས་འཕྲལ་ལ་མ་གྲུབ་པ་དེ་དག་ལ་ཡང་ཚེ་རབས་གཞན་དག་ལ་ངེས་པར་འགྲུབ་པར་འགྱུར་ཏེ། སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།
--- END BLOCKS ---
