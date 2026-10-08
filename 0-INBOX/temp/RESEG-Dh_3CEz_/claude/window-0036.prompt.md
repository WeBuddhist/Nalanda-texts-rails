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
[Block 1261]
བཟའ་བ་ནི་བདེ་བར་ལོངས་སྤྱོད་པའོ། །

[Block 1262]
སེམས་ཅན་དེ་དེ་ནི་ཡུལ་ལ་སྣང་བའི་ཤེས་པ་ཐ་དད་དོ། །

[Block 1263]
དབང་དུ་འགྱུར་བ་ནི་དེ་རྣམས་བདེ་བར་འདུ་བའོ། །

[Block 1264 [VERSE]]
དེ་ནི་རང་ལུས་ཐབས་ལ་བརྟེན་པའོ། །
རྡོ་རྗེ་ནི་སྟོང་པ་ཉིད་དོ། །
སྲ་ཞིང་བརྟན་ལ་ཁོང་སྟོང་མིན། །
སྟོང་ཉིད་རྡོ་རྗེ་ཞེས་སུ་བརྗོད། །

[Block 1265]
ཅེས་གསུངས་སོ། །

[Block 1266]
ཐོད་པ་ནི་སྣང་བའོ། །

[Block 1267]
སྙོམས་འཇུག་ནི་དབྱེར་མེད་པའོ། །

[Block 1268]
སྐྱེ་བོ་གང་དང་གང་རྣམས་ལ་སྣང་བ་སྣ་ཚོགས་པའོ། །

[Block 1269]
ཤ་ནི་མཁས་པས་བཟའ་བར་བྱ་བ་ནི་གཉིས་སུ་མེད་པར་མྱོང་བའོ། །

[Block 1270 [VERSE]]
སེམས་ཅན་དེ་དེ་དབང་དུ་འགྱུར་བ་ནི། །
སྣང་བ་ཐམས་ཅད་དེར་སྦྱོར་བའོ། །
དེ་ནི༌[^614]བརྟེན་པ་ཆོས་ནས་འཇུག་པའོ། །

[Block 1271]
ཡང་ན་རྡོ་རྗེ་ནི་ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པའོ། །

[Block 1272]
ཐོད་པ་ནི་དེ་བསྟེན་པ་སྟེ་བདེ་བ་སྐྱོང་བ་དང་ལྡན་པའོ། །

[Block 1273]
སྦྱོར་བ་ནི་བསྟེན་པའི་ཐབས་འདོད་པའི་ཡོན་ཏན་ལ་སོགས་པའོ། །

[Block 1274 [VERSE]]
སོ་སོའི་སྐྱེ་བོ་ནི་ཡིད་མཐུན༌[^615]ན་གནས་པའོ། །
ཤ་ནི་རྟོག་པ་དང་བརྟགས་པའོ། །

[Block 1275 [VERSE]]
མཁས་པ་ནི་གཟུང་འཛིན་གྱི་སྟོང་པའི་ཤེས་རབ་ལའོ། །
བཟའ་བ་ནི་བདེ་བ་ལ་སྤྱོད་པའི་ཐབས་སོ། །

[Block 1276]
སེམས་ཅན་དེ་དེ་ནི་དབང་པོ་རང་སྣང་གི་མན་ངག་གོ། །

[Block 1277 [VERSE]]
དབང་དུ་འགྱུར་བ་ནི་སྤྱོད་ལམ་དང་བསྲེགས་པའི༌[^616]ངག་གོ། །
དེ་ནི་གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོ་ལ་བརྟེན་པའོ། །

[Block 1278]
ལེའུ་བདུན་པའོ།། །།

[Block 1279 [HEADING]]
### བརྒྱད་པ་རིམ་པ་གཉིས་ཀའི་གཞིའམ་མ་རྟེན། ^1-8-0

[Block 1280]
དེ་ནས་ཞེས་པ་ནི༌[^617]རྫོགས་པའི་རིམ་པ་བསྟན་ནས། དེའི་རྗེས་ལ་བསྐྱེད་རིམ་རྫོགས་རིམ་གཉིས་ཀའི་ལེའུ་བསྟན་པར་འདོད་པའོ། །

[Block 1281]
རྣལ་འབྱོར་མ་ནི་ལམ་གཉིས་ཀྱི་དབང་དུ་བྱས་པའི་བདག་མེད་མ་ལ་སོགས་པའིའོ། །

[Block 1282]
འཁོར་ལོ་ནི་དེ་དག་འདུ་བའི་གནས་ཏེ། གཞལ་ཡས་ཁང་དང་བཅས་པ༌[^618]ལྷན་ཅིག་སྐྱེས་པར་རོ། །

[Block 1283]
འདིར་ཡང་སྒྲུབ་པ་པོ་ནས་ཚོགས་བསགས་པ་ཡན་ཆད་ལྷའི་ལེའུ་དང་འདྲ་བ་ལས།

[Block 1284]
ཁྱད་པར་ནི་བདག་མེད་མའི༌[^619]ང་རྒྱལ་གྱིས་ཐམས་ཅད་བྱས་ལ་ཚོགས་ཀྱི་ཞིང་ཡང་ཧེ་རུ་ཀ་ཕྱག་བཅུ་དྲུག་པ་ལ་ལྷ་མོ་བརྒྱད་ཀྱིས་བསྐོར་བ་སྤྱན་དྲངས་ལ༌[^620]ཚོགས་བསག་པར་བྱའོ། །

[Block 1285]
སྲུང་བ༌[^621]མཚམས་ཀྱི་འཁོར་ལོའི་ནང་དུ་ནམ་མཁའི་དབུས་སུ༌[^622]བྷ་ག་ཞེས་པའི་སྡོམ་རྩ་བའི་ཚིག་སྦྱར་ལ། ནམ་མཁའ་ལ་དབྱིངས༌[^623]མེད་ཀྱང་ཁྲོ་བ་དང་ཆགས་པ་ཅན་འདུལ་བའི་དོན་དུ་གྲུ་གསུམ་དུ་བསྟན་པ་དང་། སྐྱེ་གནས་དང་སྒོ་བསྟུན་པའི་ཕྱིར་གྲུ་གསུམ་དཀར་པོ་ནང་ཁོང་སྟོང༌[^624]ཡངས་པར་བསྒོམ་མོ། །

[Block 1286]
ཟུར་གསུམ་ནི་ཁམས་གསུམ་མམ་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་མམ་ལུས་ངག་ཡིད་གསུམ་རྣམ་པར་དག་པའོ། །

[Block 1287]
ཁ་དོག་དཀར་པོ་ཉོན་མོངས་པའི་སྐྱོན་གྱིས་མ་གོས་པའོ། །

[Block 1288]
ནང་ཁོང་སྟོང་ནི་ཆོས་ཀྱི་དབྱིངས་སྟོང་པ་ཉིད་མཚོན་ནོ། །

[Block 1289]
སྟེང་ཡངས་པ་ནི་སའི་རིམ་པ་གོང་ནས་གོང་དུ་ཡོན་ཏན་འཕེལ་བར་མཚོན་པའོ། །

[Block 1290]
དེ་ནི་ཕྱིའི་གཞི་དང་ནང་གི་གཞི་བསྟན་ནས་རྟེན་གཞལ་ཡས་ཁང་བསྟན་པ་ནི་འཁོར་ལོ་ས་དང་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1291]
སྤྱིར་གཞལ་ཡས་ཁང་སྒྲུབ་ལུགས་གཉིས་ཏེ། འབྱུང་བ་རིམ་བརྩེགས༌[^625]ནི་ལྷའི་རྒྱལ་པོའི་ཁང་བཟངས་སྒྲུབ་ལུགས་དང་། འབྱུང་བ་ཡོངས་བསྒྱུར་མིའི་རྒྱལ་པོའི་ཁང་བཟངས་སྒྲུབ་པའི་ལུགས་སོ། །

[Block 1292]
འདིར་ནི་མིའི་རྒྱལ་པོའི་ཁང་བཟངས་སྒྲུབ་པའི་ལུགས་ཏེ།[^626] དེ་གཉིས་གོ་རིམས་ངེས་པ་ཡང་བསྟན་ཏོ། །

[Block 1293]
འདི་ཡང་རྒྱུད་དུ་བསྟན་པའི་ཕྱིར་སའི་འཁོར་ལོ་བཞིན་དུ་ཆུ་ལ་སོགས་པ་ཡང་མཚོན་ཏེ་ཤེས་པར་བྱའོ། །

[Block 1294]
སྔོན་འགྲོ་ནི་འདོད་ཁམས་སུ་ཁང་བཟངས་ལ་སོགས་པར་ཆོས་མཐུན་པར་ཆུའི་སྔོན་དུ་ས་སྟེ། གཞན་དག་ལ་ཡང་དེ་བཞིན་ནོ། །

[Block 1295]
ཇི་ལྟར་རིགས་པ་མེ་ལ་བསྟན་ཀྱང་དེ་བཞིན་དུ་ས་ནི་ལཾ་ལས་བྱུང་བ་སེར་པོ་གྲུ་བཞི་པ་རྡོ་རྗེས་མཚན་པའོ། །

[Block 1296]
ཆུ་ནི་བཾ་ལས་གྱུར་པས་དཀར་པོ་ཟླུམ་པོ་བུམ་པས་མཚན་པ་སྟེ། ལྷ་ནི་རླུང་ལ་བཤད་ཀྱང་སྔ་མ་བཞིན་ཏེ་སངས་རྒྱས་སྤྱན་ལ་སོགས་པའོ། །

[Block 1297 [HEADING]]
#### རྣམ་པར་ཤེས་པའི་ཁམས་བསྟན་པ། ^1-8-2-0

[Block 1298]
གཞི་འབྱུང་བ་ནམ་མཁའ་རྐྱེན་གྱི་འབྱུང་བ་བཞི་བསྟན་ནས་རྣམ་པར་ཤེས་པའི་ཁམས༌[^627]བསྟན་པའི་ཕྱིར་ཇི་ལྟར་ནི་གཞི་དང་རྐྱེན་དེ་ལྟར་ཡིན་ན། རྒྱུ་ཇི་ལྟར་ཞེས་དྲིས་པའོ། །

[Block 1299]
སྒོམ་པ་པོ་ནི་ཚོགས་གཉིས་ཀྱིས་སྦྱངས་པའི་རྣལ་འབྱོར་པའི་སེམས་སོ། །

[Block 1300]
འབྱུང་བ་ནི་བར་དོར་འཇུག་པའི་རང་བཞིན་ཏེ་ཁྱབ་པའོ། །
--- END BLOCKS ---
