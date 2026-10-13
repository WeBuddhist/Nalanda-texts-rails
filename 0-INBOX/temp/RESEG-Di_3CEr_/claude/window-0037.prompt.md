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

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

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
[Block 1296]
དེའི་ཕྱིར་རྣམ་པ་ཀུན་ལ་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་གཞན་ཐུན་མོང་མ་ཡིན་པ་ཉིད་ནི་མི༌[^995]བརྗོད་དོ། །

[Block 1297]
དེ་བཞིན་དུ་འགལ་བ་དང་མ་ངེས་པའི་མཐའ་ཅན་དུ་མ་བརྗོད་དོ།[^996] །

[Block 1298]
ཇི་སྐད་དུ་ས་ལ་སོགས་པ་འདུས་ནས་ལུས་པོ་བརྩམས་པར་བརྗོད་པ་ལ་ཅི་རང་རང་གི་རིགས་སུའམ་ཞེས་ཐེ་ཚོམ་དུ་འགྱུར་ཏེ། ལྔའི༌[^997]རྟགས་དམིགས་པའི་ཕྱིར་དང་། རིགས་མི་མཐུན་གྱི་རྩོམ་པ༌[^998]བཀག་པའི་ཕྱིར་རོ་ཞེས་སོ། །

[Block 1299]
ཐེ་ཚོམ་གྱི་མདོ་དེ་ཙམ་གྱིས་མི་ཆོག་གོ་ཞེས་བརྗོད་དོ། །

[Block 1300]
འདིར་ཡང་སྤྱིར་མངོན་སུམ་པ་ལས༌[^999]ཡང་ཨུཏྤ་ལའི་དཀར་པོ་ལས་ཡོན་ཏན་ཉིད་དང་བརྟེན་པ་ཉིད་དང་ཡོན་ཏན་མེད་པ་ཉིད་རྣམས་ལ་ངེས་པར་མཐོང་གི་ཐེ་ཚོམ་ནི་མ་ཡིན་ནོ། །

[Block 1301]
དེའི་ཕྱིར་གང་རྣམ་པར་གཅོད་པ་མ་ཡིན་པའི་གཏན་ཚིགས་ཀྱི་སྤྱི༌[^1000]དེ་མངོན་སུམ་པ་ཉིད་དུ་ཐེ་ཚོམ་ཟའོ་ཞེས་བརྗོད་པར་མི་བྱ་སྟེ་དེ་ནི་ཉུང་བ༌[^1001]ཉིད་དོ། །

[Block 1302]
གལ་ཏེ་ཡང་ཡོད་པའི་གཏན་ཚིགས་མེད་པ་དང་། ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་ནི་ཐེ་ཚོམ་ཟ་བ་ཡིན་ལ། གང་བསྒྲུབ་བྱ་ལ་ཐེ་ཚོམ་ཟ་བ་དང་བརྗོད་པར་མ་བྱས་པས་ན་དེ་ལྟར་ཉུང་བར༌[^1002]བརྗོད་པ་ཡིན་ནོ། །

[Block 1303]
དཔེར་ན་འགའ་ཞིག༌[^1003]སྒྲ་ལ་མི་རྟག་པ་བསྒྲུབ་པ༌[^1004]ལ་མིག་གིས་གཟུང་བྱ་མ་བསྟན་ན་ནི་ཡུལ་ལ་ཐེ་ཚོམ་དུ་འགྱུར་བ་སྟེ་དུ་བ་ལ་སོགས་པ་ཉིད་ཀྱིས་མེ་ལ་སོགས་པ༌[^1005]བསྒྲུབ་པ་བཞིན་ནོ། །

[Block 1304]
དེ་ལྟར་ན་བྱེ་བྲག་པའི་གཏན་ཚིགས་ལྟར་སྣང་བ་ནི༌[^1006]སྒྲུབ་པར་དཀའོ། །

[Block 1305]
གཏན་ཚིགས་གཟུགས་བརྙན་དང་བཅས་པ་བརྗོད་ཟིན་ཏོ། །

[Block 1306]
ཚད་མ་ཀུན་ལས་བཏུས་པ་ལས་གཞན་གྱི་དོན་གྱི༌[^1007]རྗེས་སུ་དཔག་པའི་ལེའུ་སྟེ་གསུམ་པའོ།། །།

[Block 1307 [HEADING]]
## དཔེ་དང་དཔེ་ལྟར་སྣང་བ་བརྟགས་པའི་ལེའུ། ^4-0

[Block 1308 [HEADING]]
### དཔེ། ^4-1-0

[Block 1309 [VERSE]]
ཚུལ་གསུམ་རྟགས་ཤེས༌[^1008]བརྗོད་པ་ལས། །
ཕྱོགས་ཀྱི་ཆོས་སུ་ལེགས་གནས་པའི། །
ལྷག་མ་ཚུལ་གཉིས་སུ་གྲགས་པ། །
དཔེ་ཡིས་རབ་ཏུ་སྟོན་པར་བྱེད། །

[Block 1310]
རྟོག་གེའི་བསྟན་བཅོས་རྣམས་སུ་ནི་ཕྱོགས་ཀྱི་ཆོས་ཉིད་ཙམ་གཏན་ཚིགས་ཀྱི་སྦྱོར་བ་ཡིན་ནོ་ཞེས་གྲགས་ཏེ། དཔེར་ན་འདི་བྱས་པའི་ཕྱིར་ཞེས་པས་སྒྲ་མི་རྟག་པར་གོ་བར་བྱེད་པ་ལྟ་བུའོ། །

[Block 1311]
མཚན་ཉིད་ལྷག་མ་ནི་སྦྱོར་བ་ལ་མ་བརྗོད༌[^1009]པས་དེའི་དོན་དུ་དཔེ་བརྗོད་པར་བྱའོ། །

[Block 1312 [HEADING]]
#### ཆོས་མཐུན་པ་དང་ཆོས་མི་མཐུན་པའི་དཔེ། ^4-1-1-0

[Block 1313 [VERSE]]
བསྒྲུབ་བྱའི་རྗེས་སུ་འགྲོ་བའི་རྟགས། །
བསྒྲུབ་བྱ་མེད་ན་མེད་ཉིད་གང་། །
ཆོས་མཐུན་ཅིག་ཤོས་དང་བཅས་གཉིས། །
དཔེ་ལ་རབ་ཏུ་བསྟན་པར་བྱ། །

[Block 1314]
རྗེས་སུ་འགྲོ་བ༌[^1010]ཐམས་ཅད་དུ་འགྲོའོ།[^1011] །

[Block 1315]
གང་ཞེས་པ༌[^1012]ནི་བརྗོད་པར་བྱའོ། །

[Block 1316]
ཆོས་མཐུན་པ་ནི་རེ་ཞིག་སྒྲ་མི་རྟག་སྟེ་བྱས་པའི་ཕྱིར་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1317]
གལ་ཏེ་གང་རྩོལ་བ་ལས་བྱུང་བ་དེ་མི་རྟག་པར་བུམ་པ་ལ་སོགས་པ་ལ་མཐོང་བ་དེ་བཞིན་དུ་ཆོས་མི་མཐུན་པ་ལ་ཡང་རྟག་པ༌[^1013]རྩོལ་བ་ལས་མ་བྱུང་བར་ནམ་མཁའ་ལ་མཐོང་བའི་ཕྱིར་འདིར་ཡང་སྒྲུབ་བྱེད་ཀྱི་སྒོ་ནས་བསྒྲུབ་བྱ་སྒྲུབ་པར་བརྗོད་པར་བྱའོ། །

[Block 1318]
ཆོས་མཐུན་པར་གདོན་མི་ཟ་བར་གང་རྩོལ་བ་ལས་བྱུང་བ་དེ་མི་རྟག་གོ་ཞེས་བསྟན་ན་ནི་ཆོས་མི་མཐུན་པས་ཀྱང་གདོན་མི་ཟ་བར་བསྒྲུབ་བྱ་མེད་པ་ལ་མེད་པར་སྟོན་པར་འགྱུར་ཏེ། གཏན་ཚིགས་དེ་ཉིད་བསྒྲུབ་བྱ་མེད་པ་ལ་མེད་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 1319]
མ་ཡིན་དགག་ཅིང༌[^1014]དགག་པ་དང་། །དེ་བཞིན་མཚན་ཉིད་མེད་ལ༌[^1015]ཡང་། །

[Block 1320]
དེ་ལྟར་སྔ་མ་ནི་མ་ཡིན་པར་དགག་པ་ཡིན་ལ་ཕྱི་མ་ནི་མེད་དགག་གི༌[^1016]དགག་པ་ཡིན་པར་བརྗོད་དོ། །

[Block 1321]
དེ་ལྟ་ན་ནི་རྟག་པ་ཆོས་མ༌[^1017]བླངས་པར་ཆོས་མི་མཐུན་པའི་དཔེ་གྲུབ་པ་ཡིན་ནོ། །

[Block 1322]
གལ་ཏེ་ཡང་ཅི༌[^1018]བསྒྲུབ་བྱ་དང་ལྡན་པའི་གཏན་ཚིགས་གཅིག་བརྗོད་པས་གཉིས་པ་བསྒྲུབ་བྱ་མེད་པ་ལ་གཏན་ཚིགས་མེད་པར་རྒྱུ་གང་གིས་ན་ཡིན་ཏེ། གཏན་ཚིགས་མེད་པར་བསྒྲུབ་བྱ་མེད་པ་ནི་མ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟར་གཏན་ཚིགས་མཐུན་པའི་ཕྱོགས་ཁོ་ན་ལ་ཡོད་པ་ནི། བསྒྲུབ་བྱ་མེད་པ་ལ༌[^1019]བསྟན་པར་ནུས་ཀྱི་བཟློག་པ་ལས་ནི་མ་ཡིན་ནོ། །

[Block 1323]
གལ་ཏེ་འདི་ལྟར་བུམ་པ་དཔེར་བརྗོད་པ་དེ་ལྟ་ན་ནི་ཇི་ལྟར་གཏན་ཚིགས་བསྒྲུབ་བྱ་དང་ལྡན་པ་དེ་ལྟར་བསྒྲུབ་བྱ་གཏན་ཚིགས་དང་ལྡན་པར་འགྱུར་རོ་ཞེ་ན་མ་ཡིན་ཏེ། བརྗོད་པར་མི་བྱ་བའི་ཕྱིར་ཏེ། བུམ་པ་ནི་གང་བསྒྲུབ་བྱའི་རྗེས་སུ་འགྲོ་བ་ཅན་གྱིས༌[^1020]བྱས་པ་ཉིད་ཀྱི་ཁྱད་པར་དུ་བྱས་པ་བརྗོད་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1324]
ངག་གི་དོན་བསྟན་པ་ནི་ངེས་པར་བསྟན་པའི་དོན་གཙོ་བོ་ཡིན་ནོ། །

[Block 1325]
གཞན་ཡང་།

[Block 1326 [VERSE]]
མ་བྱས་པ་ལ་རྟག་པའམ། །
འཇིག་པ་ལས་འཛིན༌[^1021]འབྲས་ཉིད་དུ། །
འདིར་ནི་རྗེས་སུ་བརྗོད་བྱས་ནས། །
མ་ཁྱབ་འདོད་མིན་མཚུངས་རྗེས་འགྲོ། །

[Block 1327]
གལ་ཏེ་ཆོས་མཐུན་པའི་སྒོ་ནས་གང་མ་བྱས་པ་དེ་རྟག་གོ་ཞེས་བརྗོད་ན་ནི་མ་བྱས་པ་ཉིད་ཀྱིས་དམ་མ་བཅས་པའི་རྟག་པ་བསྒྲུབ་པར༌[^1022]འགྱུར་རོ། །

[Block 1328]
དེ་བཞིན་དུ་ཆོས་མི་མཐུན་པའི་སྒོ་ནས་གང་མི་རྟག་པ་དེ་བྱས་པའི་ཞེས་པ་ཡིན་ན་ནི་དེ་ལྟ༌[^1023]ན་ཡང་མི་རྟག་པ༌[^1024]བྱས་པ་ཉིད་དུ་བསྒྲུབ་པར༌[^1025]འགྱུར་རོ། །

[Block 1329]
མ་ཁྱབ་པའི༌[^1026]རྩོལ་བ་ལས་བྱུང་བ་ཉིད་ལ་གཏན་ཚིགས་ཀྱི་སྐྱོན་དེ་དག་ཡོད་པར་འགྱུར་ཏེ། གློག་ལ་སོགས་པ་རྟག་པ་ཉིད་དང་། བརྩལ་མ་ཐག་ཏུ་འབྱུང་བར༌[^1027]ཡང་འགྱུར་རོ་ཞེས་པ་ནི་སྐྱོན་ཡིན་ནོ། །

[Block 1330]
ཅི་སྟེ་སྐྱོན་དེ་ཡོད་དུ་ཆུག་མོད། གལ་ཏེ་བསྒྲུབ་བྱའི་གོ་བར་བྱེད་པའི་རྟགས་ཁྱབ་པར་མི་སྟོན་ན་ནི་མི་རྟག་པ་ལས་གཞན་པ༌[^1028]ལ་ཡང་སྲིད་པ་ཉིད་ཡིན༌[^1029]པའི་ཕྱིར་བསྒྲུབ་བྱ་མེད་པ་ལ་མེད་པའོ་ཞེས་བརྗོད་པར་མི་བྱའོ། །

[Block 1331]
དེ་སྟེ༌[^1030]ཡོད་པའི་དངོས་པོ་ཙམ་ཡིན་ན་ནི་བུམ་པ་མི་རྟག་པ་ཉིད་ཀྱང་རྩོལ་བ་ལས་བྱུང་བ༌[^1031]མེད་ན་མི་འབྱུང་བར༌[^1032]འགྱུར་བས༌[^1033]ན། དེ་ཕྱི་རོལ་གྱི་དོན་ལ་ལྟོས་པ་ཉིད་དུ་སྟོན་ཏོ་ཞེས་ནི་བརྗོད་པར་མི་བྱའོ། །

[Block 1332]
ཁྱབ་པ་ཉིད་ཀྱི་གཏན་ཚིགས་བསྒྲུབ་བྱ་རྗེས་སུ་སྒྲུབ་པོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1333]
འདིའི་གནས་སྐབས་སུ་ནི་དོན་གྱི་ཤུགས་ཁོ་ནས་བསྒྲུབ་བྱ་མེད་པ་ལ་གཏན་ཚིགས་མེད་པར་བརྗོད་པ་ཡིན་པས་ཆོས་མི་མཐུན་པའི་དཔེའི་སྦྱོར་བ་ནི་མི་བྱའོ། །

[Block 1334]
གང་གི་ཚེ་དཔེ་གཉིས་ཀ་སྦྱོར་བར་བྱེད་པ་དེའི་ཚེ་ནི་མི༌[^1034]མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་ཙམ་བསྟན་པ་ཡིན་ལ། ཁྱབ་པ་ནི་བསྒྲུབ་བྱ་མེད་པ་ལ་མེད་པ་བསྟན་པ་ཡིན་པས་འདི་སྐད་དུ་ཡང༌[^1035]བསྒྲུབ་བྱ་སྒྲུབ་པར་བྱེད་པའི་རྟགས་ཆོས་མཐུན་པ་དང་བཅས་པ་སྟོན་ཏོ་ཞེས་བརྗོད་པར་མི་བྱའོ། །

[Block 1335]
དེ་ལྟར་ཡང་གཏན་ཚིགས་ཀྱི༌[^1036]བསྒྲུབ་བྱ་རྗེས་སུ་སྒྲུབ་པའི་འགེགས་པའི་དོན་དུ་འགྱུར་གྱི་དོན་འགོག་པའི་དོན་དུ་ནི་མི་འགྱུར་ཏེ། མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་དང་གཉིས་ཀ་ཞེས་སྨྲས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
