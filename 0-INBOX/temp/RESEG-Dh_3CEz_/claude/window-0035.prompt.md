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
[Block 1226 [HEADING]]
##### རྗེས་འཇུག། ^2-5-1-2-0

[Block 1227]
རྗེས་སུ་འཇུག་པ་ནི་ཉིད་ཀྱི་ཞེས་པས་གང་ཟག་བཞིའི་རིམ་པ་སྟོན་ཏེ། ཐོས་བསམ་གྱི་མཐར་ཕྱིན་པའི་རྟགས་མ་ཐོབ་ཀྱི་བར་དུ་ལས་དང་པོ་པའི་གང་ཟག་ཡིན་ཏེ། རང་ཉིད་ཀྱིས་དཀྱིལ་འཁོར་ལ་སོགས་པའི་ལས་ཐམས་ཅད་བྱའོ། །གཉིས་པ་གསུམ་པ་ཕབ་སྟེ་བྲི།[^1286] །ཞེས་པ་ཅུང་ཟད་ཡེ་ཤེས་ལ་དབང་བ་ནི་དབང་པོ་སྤྲིན་དང་འདྲ་བའི་རྟགས་དང་། མངོན་པར་ཤེས་པ་གཅིག་ཙམ་ཐོབ་པ་དང་།གསུམ་པ་ཡེ་ཤེས་ལ་དབང་བའི་རྟགས་ནི་དུ་བ་དང་། སྲིན་བུ་མེ་ཁྱེར་དང་མངོན་པར་ཤེས་པ་གསུམ་ཙམ་ཐོབ་པ་དང་། ཁྱེའུ་དང་བུ་མོ་གཞོན་ནུ་མ་ལས་ཡེ་ཤེས་ཕབ་སྟེ་འདྲི་རུ་གཞུག་གོ། །ཡང་དག་པའི་ཡེ་ཤེས་ལ་དབང་བའི་རྟགས་ནི་ནམ་མཁའ་ལྟ་བུ་མཐོང་བ་དང་། མངོན་པར་ཤེས་པ་ལྔ་ཐོབ་པས་དཀྱིལ་འཁོར་སྤྲུལ་ལ་དབང་བསྐུར་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1228 [HEADING]]
#### སྒྲུབ་པ། ^2-5-2-0

[Block 1229]
དེའི་དོན་ནི་འདི་ཡིན་ཏེ་སྔར་བསྟན་པས་བསྙེན་པ་རྫོགས་ནས། དེ་ནས་སྒྲུབ་པ་ནི་སའི་ཆོ་ག་དང་སྟ་གོན་གྱི་ཆོ་ག་དང་དབང་བསྐུར་བའོ། །

[Block 1230 [HEADING]]
##### སའི་ཆོ་ག། ^2-5-2-1-0

[Block 1231]
དེ་ལ་སའི་ཆོ་ག་ནི་ལེའུ་བཅུ་པ་ནས་བཤད་པ་བཞིན་དུ་བྱས་ལ།

[Block 1232 [HEADING]]
##### སྟ་གོན་གྱི་ཆོ་ག། ^2-5-2-2-0

[Block 1233]
སྟ་གོན་དུ་གནས་པ་དང་བུམ་པ་དང་སློབ་མ་སྟ་གོན༌[^1287]ནི་བརྟག་པ་ཕྱི་མའི་ལེའུ་དང་པོར་བཤད་པ་ལྟར་བྱའོ། །བུམ་པ་སྟ་གོན་ནམ༌[^1288]གྲངས་ནི་རྒྱས་པར་བསྡུ་ན་བཅུའམ་དྲུག་སྟེ། རྣམ་པར་རྒྱལ་བ་དང་། ལྷ་མོ་བརྒྱད་ཀྱི་བུམ་པ་དང་། ལས་ཐམས་ཅད་པ་དང་བཅུའོ། །ཡང་ན་རྣམ་རྒྱལ་གཙོ་བོའི་བུམ་པ་དང་ལྷ་མོ་བརྒྱད་པོ་རིགས་བཞི་རུ༌[^1289]བསྡུས་ལ་ལྔ། ལས་ཐམས་ཅད་པ་དང་དྲུག་གོ། །གང་བའི་བུམ་པ་ནི་ཅི་རིགས་པར་ཤེས་པར་བྱའོ། །

[Block 1234]
ལྷ་སོ་སོའི་མཚན་མས་མཚན་ལ༌[^1290]རིན་པོ་ཆེའི་བུམ་པའམ་གཞལ་ཡས་ཁང་དུ་བསྐྱེད། པཾ་ལས་པདྨ་འདབ་བརྒྱད་བསྐྱེད་ལ། རྣམ་པར་རྒྱལ་བའི་བུམ་པར་ས་བོན་ཙཾ་ལས་ལྷ་ཚང་བར་བསྐྱེད། ཡེ་ཤེས་པ་སྤྱན་དྲངས་ལ་མཆོད་བསྟོད་བཟླས་པ་བྱས་ལ་ལྷ་ཞུ་བར་བསམ་མོ། །གཞན་དག་ལ་ལྷ་རེ་རེའམ། ལྷ་གཉིས་གཉིས་བསྐྱེད་ལ་ཆོ་ག་སྔ་མ་བཞིན་བྱའོ། །དེ་ནས་སློབ་མའི་སྟ་གོན་ནི་ཁྲུས་བྱས་ཏེ་ཀུན་གྱིས་མཎྜལ་ཕུལ་ལ། དགའ་ཆེན་ཁྱོད་བདག་སྟོན་པ་བས། །ཞེས་བྱ་བ་ལ་སོགས་པས་གསོལ་བ་གདབ་པ་དང་། བུ་ཚུར་ཐེག་པ་ཆེན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྤྲོ་བ་བསྐྱེད་ལ། བདུན་རྣམ་པར་དག་པས་སྦྱང་བ་བྱ། དེ་ནས། ཐུབ་པ་ཉི་མ་མ་ལུས་པ།[^1291] །ཞེས་བྱ་བས་སྡོམ་པ་ལ་གསོལ་བ་གདབ། རྟོག་པ་རྣམས་ནི་ལེགས་པར་བསྡུས་ནས་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སྡོམ་པ་བཤད། སྡོམ་པ་དཔོག་གོ། །

[Block 1235]
དེ་ནས་སེམས་བསྐྱེད་པ་གསང་བ་སྟ་གོན་ལ་གནས་ཏེ་མཆོད་པར་བྱའོ། །དེ་ནས་སོ་ཤིང་དོར་བའི་ཆོ་ག་བྱ། ཧུབ་གསུམ་གྱིས་ཆུ་བླུད། ཀུ་ཤ་སྦྱིན་སྲུང་སྐུད་གདགས་ལ་ཟབ་ཅིང་རྒྱ་ཆེ་བའི་ཆོས་བཤད་པར་བྱའོ། །དེ་ནས་འབྱོར༌[^1292]ན་སྦྱིན་སྲེག་གིས་ལྷག་པར་གནས་པར་ཡང་བྱའོ། །རྨི་ལམ་མ་བརྗེད་པར་བསྒོས་ལ་ཉལ་ཁང་དུ་གཏང་། དེ་དག་གི་ཆོ་གར་བྱ་བ་ནི་མཚོ་སྐྱེས་ཀྱི་དཀྱིལ་འཁོར་གྱི་ཆོ་ག་ལྟར་ཤེས་པར་བྱའོ། །དེ་ནས་ནང་པར་སྔར་ལངས་ལ་རྨི་ལམ་བརྟག །མཆོད་བསྟོད་བྱ་སྟེ། སྟ་གོན་གྱི་དཀྱིལ་འཁོར་ནམ་མཁའ་ལ་བཏེག་ལ་ཉི་ཟླ་ཁ་སྦྱར་དུ་བཅུག །དབྱངས་ཡིག་གིས་རྒྱས་གདབ་པར་བྱའོ། །ཐིག་དང་ཚོན་ནི་ལེའུ་བཅུ་པ་ལྟར་ཤེས་པར་བྱའོ། །

[Block 1236]
དཀྱིལ་འཁོར་གྱི་མཚན་ཉིད་བསྟན་པ་ནི། འཕར་མ་གཅིག་དང་སྒོ་བཞི་པ། །ཞེས་བྱ་བ་ནས།བརྒྱད་པ་ཟེ་བ་བཅས་པར་བྲི། །ཞེས་བྱ་བའི་བར་དུ་དཀྱིལ་འཁོར་གྱི་རྣམ་དག་སྔར་བཞིན་ཤེས་པར་བྱའོ། །

[Block 1237]
དེ་ནས་མཚན་མ་ཙ་ཀླི་དགོད་པ་ནི།

[Block 1238 [VERSE]]
སྙིང་པོར༌[^1293]བསྐྱེད་པའི་ཐོད་པ་ཉིད། །
མདོག་དཀར་ཆ་ནི་གསུམ་པ་བྲི། །

[Block 1239]
དེའི་རྗེས་སུ་དབུས་སུ་ཐོད་པ་དཀར་པོ་ཡང་ཚིག་གཉིས་སྦྱར་རོ། །

[Block 1240]
དེ་ནས། དབང་ལྡན་དུ་ནི་ཤ་ར་བྷ། །ཞེས་བྱ་བ་ནས། ཕྱག་མཚན་བརྒྱད་དུ་རབ་ཏུ་གྲགས། །ཞེས་པ་སྟེ་རང་རང་གི་སྔགས་ལ་དེ་ཉིད་གསུམ་སྤེལ་ཞིང་ལྷ་རུ་མོས་པ་དགོད་པར་བྱའོ། །དེ་ནས་བུམ་པ་དགོད་པ་ནི་དེ་ནས་རྣམ་རྒྱལ་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་བུམ་པའི་ཡོ་བྱད་ཐམས་ཅད་གསོས་གདབ་སྟེ། སྟ་གོན་གྱི་གནས་ནས༌[^1294]རོལ་མོ་དང་བཅས་པས་སྤྱན་དྲངས་ལ་རྣམ་པར་རྒྱལ་བའི་བུམ་པ་ནི་གཙོ་བོའི་སྤྱན་སྔར་གཞག་པར་བྱའོ། །བུམ་པ་གཞན་རྣམས་ནི་རང་རང་གི་གནས་ལ་ཉེ་བར་གཞག༌[^1295]གོ། །ལས་ཐམས་ཅད་པའི་བུམ་པ་ནི་སྒོའི་གཡས་ཕྱོགས་སུ་དགོད་པར་བྱའོ། །

[Block 1241]
དེ་བཞིན་དུ་མཆོད་པ་ཐམས་ཅད་ཀྱང་ཉེ་བར་བཤམ། བླ་རེ་དང་རྒྱན་དང་གདུགས་དང་བདན་ལ་སོགས་པ་དང་རྟ་བབས༌[^1296]དང་རོལ་མོ་དང་། ན་བཟའི་བྱེ་བྲག་ཐམས་ཅད་ཀྱང་ལྷ་རྣམས་ལ་རས་ཟུང་རེ་རེ་དབུལ་བར་བྱའོ། །

[Block 1242]
དེ་ནས་དཀྱིལ་འཁོར་བསྒྲུབ་པ་ནི། །

[Block 1243 [VERSE]]
མང་དུ་བརྗོད་པས་ཅི་ཞིག་བྱ། །
ཇི་ལྟར་དེ་ཉིད་བསྡུས་པ་ཡི། །

[Block 1244]
དཀྱིལ་འཁོར་ཆོ་ག་དེ་བཞིན་བྱ།[^1297] །ཞེས་བྱ་བ་ནི་སྤྱིར་དེ་དག་ཐམས་ཅད་མཐུན་པར་ཤེས་པར་བྱའོ། །ཁྱད་པར་ནི་དཀྱིལ་འཁོར་གྱི་ཤར་སྒོ་རུ་སྟན་བདེ་བ་ལ༌[^1298]འདུག་སྟེ། ཡན་ལག་དྲུག་གི་རྣལ་འབྱོར་པ༌[^1299]སྦྱོར་བ་རྣམ་པ་གསུམ་བཟླས་པའི་བར་དུ་བྱ་བ་ནི་བདག་ཉིད་ལྡན་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 1245]
དེར་དཀྱིལ་འཁོར་གྱི་ལྷ་རྣམས་ས་བོན་ཕྱག་མཚན་ཙམ་ལས་བསྐྱེད་ལ་ཡེ་ཤེས་ཀྱི༌[^1300]འཁོར་ལོ༌[^1301]དགུག །སྐྱེ་མཆེད་དང་སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་བརླབ། མཆོད་བསྟོད་རྒྱས་པར་བྱ། བདུད་རྩི་མྱང་བ་བཟླས་པའི་བར་དུ་བྱའོ། །དེ་ནས་སློབ་མས་མཎྜལ་བྱས་ལ་གསོལ་བ་གདབ་པ་དང་ཆོ་ག་རྣམས་ནི་སྟ་གོན་གྱི་སྐབས་བཞིན་འདིར་བྱའོ། །དེ་དག་ཐུན་མོང་གི་ཆོ་ག་ཐམས་ཅད་ནི་ཇི་ལྟར་དེ་ཉིད་བསྡུས་པ་ལྟར་བྱའོ། །ཁྱད་པར་གྱི་ཆོ་ག་ནི་ལེའུ་བཅུ་པར་བསྟན་པ་བཞིན་ནོ། །འཇུག་པའི་ཆོ་ག་ལ་དམ་ཚིག་བསྒྲགས། མནའ་ཆུ་བླུད། དེ་ནས་ཡེ་ཤེས་དབབ་པ་དང་། མེ་ཏོག་དོར་བ་དང་། དཀྱིལ་འཁོར་ཀྱི་ལྷ་ངོ་བསྟན་ནས་དཀྱིལ་འཁོར་གྱི་དེ་ཁོ་ན༌[^1302]ཉིད་དང་ལྷའི་དེ་ཁོ་ན་ཉིད་བཅས་པ་ནི་འཇུག་པའི་རིམ་པའོ། །

[Block 1246 [HEADING]]
##### དབང་བསྐུར་བ། ^2-5-2-3-0

[Block 1247]
དེ་ནས་དབང་བསྐུར་བ་ལ་ཁྱད་པར་དུ་ཡི་དམ་གྱི་ལྷའི་དབང་བསྐུར་བ་དང་། བུམ་པའི་དབང་བསྐུར་བ་ནས་བརྩམས་ནས་རྗེས་སུ་གནང་བ་ཐུན་མོང་དང་ཁྱད་པར་དང་། དབུགས་དབྱུང་བ་དང་ལུང་བསྟན་པ་རྣམས་མཐུན་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1248 [HEADING]]
###### ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་བསྐུར་བ། ^2-5-2-3-1-0

[Block 1249]
དེ་ནས་ཁྱད་པར་གྱི་དབང་བསྐུར་བ༌[^1303]ནི་གསང་བའི་དབང་སྔོན་དུ་སོང་བས་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་བསྐུར་བ་ལ་གཉིས་ཏེ་ཆགས་ཅན་གྱི་དབང་བསྐུར་བ་དང་ཆགས་བྲལ་གྱི་དབང་བསྐུར་ལུགས་སོ། །

[Block 1250 [HEADING]]
###### **དང་པོ་ཆགས་ཅན་གྱི་དབང་བསྐུར་བ།** ^2-5-2-3-1-1-0

[Block 1251]
དང་པོ་བཤད་པ།

[Block 1252 [VERSE]]
བཅུ་གཉིས་བརྒྱད་གཉིས་ལོན་པ་ཡི། །
རིག་མ་བདེ་ཆེན་བརྒྱད་པོ་ཉིད། །

[Block 1253]
ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་ན་ཚོད་ཀྱི་ཡོན་ཏན་དང་། རིགས་ཀྱི་ཡོན་ཏན་དང་། སྦྱངས་པའི་ཡོན་ཏན་ལ་སོགས་པ་ནི་སྔ་མ་དང་འདྲ་བར་གཞུག་གོ། །

[Block 1254]
མ་དང་སྲིང་མོ་ཉིད་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྒྲ་ཇི་བཞིན་མ་ཡིན་པ་སྟེ་སློབ་དཔོན་གྱི་དབང་ནོད་པ་དང་། རང་དང་ལྷན་ཅིག་དབང་མནོས་པ་དང་། རང་གིས་བུམ་པའི་དབང་བསྐུར་བ་བྱས་པ་དང་། དེ་ལ་སོགས་པ་ཆོས་ཀྱིས་བསྡུས་པ་ཡིན་ནོ། །དམ་དུ་འཁྱུད་དང་འོ་བྱེད་པ། །ལ་སོགས་པ་ནས། དེ་ལ་རྩེད་མོ་རྩེ་བར་བྱ། །ཞེས་བྱ་བའི་བར་དུ་ནི་ཐུན་ཚོད་དང་པོའོ། །དེ་ནས་ཐུན་ཚོད་གཉིས་པ་ལ། །ཞེས་བྱ་བ་ནས། སློབ་དཔོན་ལ་སོགས་རབ་ཕྱེ་ནས།[^1304] །ཞེས་བྱ་བའི་བར་ནི་བྱ་བའི་རིམ་པ་སྟེ་མཆོད་པ་དང་བསྟོད་པ་དང་གསོལ་བ་གདབ་པ་སྔ་མ་བཞིན་དུའོ།[^1305] །དེ་ནས་དབང་བསྐུར་བ་དངོས་ནི་དེ་ཉིད་ལ་བསྟན་པར་བྱ།

[Block 1255 [VERSE]]
དགའ་བྲལ་དང་པོ་མཆོག་མཐའ་ཅན། །
ཐམས་ཅད་རྒྱུད་དུ་སྤྲོས་པ༌[^1306]སྟེ། །
མཐའ་ཡིས་མཐའ་ཡི་ཕྱེ་བ་ཉིད། །

[Block 1256]
ཅེས་བྱ་བ་ནི་རྒྱུད་ཀྱི་རིམ་པ་དང་སྦྱར་ཏེ་བྱ་བའི་རྒྱུད་དང་སྤྱོད་པའི་རྒྱུད་དང་རྣལ་འབྱོར་རྒྱུད་དང་། རྣལ་འབྱོར་བླ་ན་མེད་པའི་རྒྱུད་དེ།

[Block 1257]
དང་པོ་རུ་བལྟ་བ་ཙམ་གྱིས་དགའ་བའི་ཡེ་ཤེས་སྦས་ཏེ་བསྟན་པའོ། །གཉིས་པ་རུ་ལྷ་རྣམས་ཕན་ཚུན་དགོད་པ་ཙམ་གྱིས་མཆོག་དགའི་ཡེ་ཤེས་སྦས་ཏེ་བསྟན་པའོ། །གསུམ་པར་ནི་ལྷ་དམ་ཚིག་སེམས་དཔའ་དང་། །ཡེ་ཤེས་སེམས་དཔའ་ཕྱག་རྒྱ་འཁྱུད་པ་ཙམ་གྱིས་དགའ་བྲལ་གྱི་ཡེ་ཤེས་སྦས་ཏེ་བསྟན་ཏོ། །འདིར་ནི་ཀུན་དུ་རུའི་ལྷན་ཅིག་སྐྱེས་པའི་ཡེ་ཤེས་གཏན་ལ་ཕབ་སྟེ་བསྟན་ཏོ། །ཡང་དང་པོ་དགའ་བ་ལམ་ནས་ཞུགས་པ་ཡིན་ནོ། །གཉིས་པ་མཆོག་དགའ་གཉེན་པོ་དང་ལྡན་པ་ཡིན་ནོ། །གསུམ་པ་དགའ་བྲལ་གཉེན་པོར་གྱུར་པ་སྟེ་མི་མཐུན་པ་དང་བྲལ་བ་ཡིན་ནོ། །བཞི་པ་ལྷན་ཅིག་སྐྱེས་པ་སྟེ།གཉེན་པོ་འབའ་ཞིག་གི་ངོ་བོ་ཡིན་ནོ། །

[Block 1258 [HEADING]]
###### **ཆགས་བྲལ་གྱི་དབང་བསྐུར་བ།** ^2-5-2-3-1-2-0

[Block 1259]
དེ་ནས་ཆགས་བྲལ་གྱི་དབང་བསྐུར་བ་བསྟན་པ་ནི།རྡོ་རྗེ་མཆོད་པས་ཡང་སྦྱར་ནས། །ལྷ་དེ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཞུས་པའོ། །བཅོམ་ལྡན་འདས་བཀའ་སྩལ་ཞེས་བྱ་བ་ནི་ལན་ཏེ།

[Block 1260 [HEADING]]
###### **དེར་ནི་ཐོག་མ་ཐ་མ་མེད།** ^2-5-2-3-1-2-1-0

[Block 1261 [VERSE]]
དེར་ནི་ཐོག་མ་ཐ་མ་མེད། །
སྲིད་མེད་མྱ་ངན་འདས་པ་མེད། །
འདི་ནི་མཆོག་ཏུ་བདེ་ཆེན་ཉིད། །
བདག་མེད་གཞན་ཡང་མེད་པ་ཉིད། །

[Block 1262]
ཅེས་པ་སྟེ་འདིས་ནི་བྱ་རོག་གི་མིག་དང་འདྲ་བར་སྔ་མ་དང་ཕྱི་མ་གཉིས་ཀྱི་དོན་གཏན་ལ་འབེབས་ཏེ། ཤེས་བྱའི་དབང་དུ་བྱས་ཏེ་བཤད་པ་དང་། སྔ་ཕྱིའི་དོན་ལྷན་ཅིག་སྐྱེས་པར་གཏན་ལ་དབབ་པ་དང་། རྫོགས་པའི་རིམ་པ་མངོན་རྟོགས་ཅིག་ཅར་སྟོན་ཏོ། །

[Block 1263 [HEADING]]
###### **དང་པོ་ཤེས་བྱའི་དབང་དུ་བྱས་ཏེ་བཤད་པ།** ^2-5-2-3-1-2-1-1-0

[Block 1264]
དང་པོ༌[^1307]ནི་ཐོག་མ་སྟེ་དངོས་པོ་སྐྱེ་བར་མ་གྲུབ། དབུས་གནས་པ་མ་གྲུབ། ཐ་མ་འགག་པར་མ་གྲུབ། སྲིད་མེད་འཁོར་བའི་དངོས་པོ་ཐམས་ཅད་ཀྱང་མི་གནས་སོ། །མྱ་ངན་ལས་འདས་པར་ཡང་མི་གནས་སོ། །བདག་དང་གཞན་མེད་པ་སྟེ་གཟུང་བ་དང་འཛིན་པའི་དངོས་པོ་ཡང་མེད་དེ།[^1308] འདིར་ནི་མཆོག་ཏུ་བདེ་ཆེན་ནི་འབྲས་བུའི་མཚན་ཉིད་དེ་མ་བཅོས་པའི་རང་བྱུང་གི་ཡེ་ཤེས་ཆེན་པོ་སྟོན་ཏོ། །

[Block 1265 [HEADING]]
###### **སྔ་ཕྱིའི་དོན་ལྷན་ཅིག་སྐྱེས་པར་གཏན་ལ་དབབ་པ།** ^2-5-2-3-1-2-1-2-0
--- END BLOCKS ---
