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
སྨྲས་པ། བདག་ནི་ཡོད་པ་ཁོ་ན་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། འཁོར་བ་ཡོད་པའི་ཕྱིར་ཏེ། འདི་ལ་བཅོམ་ལྡན་འདས་ཀྱིས།

[Block 1262]
དམ་ཆོས་རྣམ་པར་མི་ཤེས་པའི། །བྱིས་པ་ལ་ནི་འཁོར་བ་རིང་། །ཞེས་གསུངས་སོ། །

[Block 1263]
དེ་བཞིན་དུ་དགེ་སློང་དག་དེ་ལྟ་བས་ན་ཁྱོད་ཀྱིས༌[^782]འཁོར་བ་ཟད་པར་བྱ་བའི་ཕྱིར་ནན་ཏན་བྱ་ཞིང་དེ་ལྟར་བསླབ་པར་བྱའོ་ཞེས་ཀྱང་བཀའ་སྩལ་ཏོ། །

[Block 1264]
དེའི་ཕྱིར། གང་རིང་བར་བསྟན་པ་དང་། གང་ཟད་པར་བྱ་བའི་ཕྱིར་ནན་ཏན་བྱ་བ༌[^783]བསྟན་པའི་འཁོར་བ་དེ་ཡོད་དོ། །

[Block 1265]
མེད་དུ་ཟིན་ཀྱང༌[^784]ཇི་ལྟ་རིང་བ་དང་ཟད་པར་འགྱུར། དེ་ལྟ་བས་ན། རིང་བ་དང་ཟད་པར་གསུངས་པས་འཁོར་བ་ཡོད་དོ། །

[Block 1266]
འཁོར་བ་ན༌[^785]ཡོད་ན་འཁོར་བ་པོ་ཡང་ཡོད་པར་མངོན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། འོངས་ཤིང་འོངས་ཤིང་ཡང་དང་ཡང་དེར་འགྲོ་བས་ན། འཁོར་བ་ཞེས་བྱ་བའི་ཕྱིར་ཏེ། གང་འོངས་ཤིང་འོངས་ཤིང་འགྲོ་བ་དེ་ནི་བདག་ཡིན་ནོ། །

[Block 1267]
དེའི་ཕྱིར་བདག་ནི་ཡོད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1268]
བཤད་པ། ཅི་ཁྱོད་ཀྱིས་སྦྲང་རྩི་མཐོང་ལ་གཡང་ས་མ་མཐོང་ངམ། ཁྱོད་ཀྱིས་འཁོར་བ་རིང་བ་དང་ཟད་པར་གསུངས་པ་མཐོང་ལ། གང་གི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གཞན་འདི་མ་མཐོང་གོ། །

[Block 1269 [VERSE]]
སྔོན་མཐའ་མངོན་ནམ་ཞེས་ཞུས་ཚེ། །
ཐུབ་པ་ཆེན་པོས་མིན་ཞེས་གསུངས། །
འཁོར་བ་ཐོག་མ་ཐ་མེད་དེ། །
དེ་ལ་སྔོན་མེད་ཕྱི་མ་མེད།

[Block 1270]
[^786] །བཅོམ་ལྡན་འདས་ཐམས་ཅད་མཁྱེན་པ། ཐམས་ཅད་གཟིགས་པ། ཐུབ་པ་ཆེན་པོས་དགེ་སློང་དག་འཁོར་བ་ལ་ཐོག་མ་དང་ཐ་མ་མེད་དོ།[^787] །སྔོན་གྱི་མཐའ་མི་མངོན་ནོ་ཞེས་བཀའ་སྩལ་པས་དེའི་ཕྱིར་ཐོག་མ་དང་ཐ་མ་མེད་པར་གསུངས་པས་བཅོམ་ལྡན་འདས་ཀྱིས་འཁོར་བ་ཡང་ངོ་བོ་ཉིད་སྟོང་པར་བསྟན་ཏོ། །

[Block 1271]
འདི་ལྟར་གལ་ཏེ་འཁོར་བ་པ་ཞེས་བྱ་བ་དངོས་པོ་འགའ་ཞིག༌[^788]ཡོད་པར་གྱུར་པ༌[^789]ན་དེ་ལ་ཐོག་མ་ཡང་ཡོད།[^790] ཐ་མ་ཡང་ཡོད་པར་འགྱུར་བར༌[^791]ཐེ་ཚོམ་མེད་དོ།[^792] །འདི་ལྟར་དངོས་པོ་ཡོད་པ་ལ་ཐོག་མ་མེད་པ་དང་ཐ་མ་མེད་པར་ཇི་ལྟར་འགྱུར། དེ་ལྟ་བས་ན་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་དབང་གིས་འཁོར་བ་རིང་བ་དང་། ཟད་པར་གསུངས་ཀྱི་བཅོམ་ལྡན་འདས་ཀྱིས་དོན་དམ་པ་བསྟན་པའི་དབང་གིས་ནི། དེ་ལ་སྔོན་མེད་ཕྱི་མ་མེད། །ཅེས་གསུངས་སོ། །

[Block 1272]
དེ་ལྟ་བས་ན་ཐོག་མ་དང་ཐ་མ་མེད་པར་གསུངས་པས་འཁོར་བ་ཞེས་བྱ་བ་དངོས་པོ་འགའ་ཡང་མི་འཐད་དོ། །

[Block 1273]
དེ་མེད་ན་འཁོར་བ་པོ་ཇི་ལྟ་བུ་ཞིག་འཐད་པར་འགྱུར།

[Block 1274]
སྨྲས་པ། དེ་ལྟར་འཁོར་བའི་ཐོག་མ་དང་ཐ་མ་བཀག་ཏུ་ཟིན་ཀྱང་། དབུས་མ་བཀག་པས་དེ་ཡོད་པའི་འཁོར་བ་ཡོད་པ་ཁོ་ན་སྟེ། འདི་ལྟར་དངོས་པོ་མེད་པ་ལ་དབུས་ཡོད་པར་ཇི་ལྟར་འགྱུར། དེ་ལྟ་བས་ན་དབུས་ཡོད་པའི་ཕྱིར་འཁོར་བ་ཡོད་པ་ཁོ་ནའོ། །

[Block 1275]
འཁོར་བ་ཡོད་པའི་ཕྱིར་འཁོར་བ་པོ་ཡང་ཡོད་པ་ཁོ་ནའོ། །

[Block 1276]
བཤད་པ། གལ་ཏེ་དབུས་ཉིད་ཡོད་པར་གྱུར་ན་ནི་དབུས་ཡོད་པའི་ཕྱིར་འཁོར་བ་ཡང་ཡོད་པར་འགྱུར་གྲང་ན། དེའི་དབུས་ཉིད་མི་འཐད་པས་དེ་ཡོད་པའི་ཕྱིར་འཁོར་བ་ཡོད་པར་ག་ལ་འགྱུར།

[Block 1277 [VERSE]]
གང་ལ་ཐོག་མེད་ཐ་མེད་པ། །
དེ་ལ་དབུས་ནི་ག་ལ་ཡོད། །

[Block 1278]
གང་ལ་ཐོག་མ་དང་ཐ་མ་མེད་པ་དེ་ལ་དབུས་ཡོད་པར་ཇི་ལྟར་འགྱུར། འདི་ལྟར་ཐོག་མ་དང་ཐ་མ་ལ་ལྟོས་ནས་དབུས་འགྲུབ་པར་འགྱུར་བ་ཡིན་ན། དེ་ལ་ཐོག་མ་དང་ཐ་མ་དེ་ཡང་མེད་དེ། དེ་མེད་པའི་ཕྱིར་དེའི་དབུས་ཡོད་པར་ག་ལ་འགྱུར། སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་། ཐོག་མ་དབུས་དང་ཐ་མ་མེད།[^793] །

[Block 1279 [VERSE]]
སྐྱེ་བའི་སྔ་རོལ་མི་སྲིད་དེ། །
གཉིས་གཉིས་དག་ནི་མ་གཏོགས་པར། །
རེ་རེས་རྩོམ་པར་ཇི་ལྟར་འགྱུར། །

[Block 1280]
ཞེས་གསུངས་སོ། །

[Block 1281 [VERSE]]
དེ་ཕྱིར་དེ་ལ་སྔ་ཕྱི་དང་། །
ལྷན་ཅིག་རིམ་པ་མི་འཐད་དོ། །

[Block 1282]
དེའི་ཕྱིར་དེ་ལ་སྔ་ཕྱི་དང་ལྷན་ཅིག་གི་གོ་རིམས་དག་མི་སྲིད་དོ། །

[Block 1283]
དེ་ལྟར་གང་གི་ཕྱིར་འཁོར་བ་ལ་ཐོག་མ་དང་དབུས་དང་ཐ་མ་དག་མེད་པ་དེའི་ཕྱིར་འདིར་འཁོར་བ་པོའི་སྐྱེ་བ་དང་རྒ་ཤི་དག་ལ་ཡང་སྔ་ཕྱི་ལྷན་ཅིག་གི་རིམ་པ་དག་མེད་དོ། །

[Block 1284]
དེ་དག་ཇི་ལྟར་ཞེ་ན།

[Block 1285 [VERSE]]
གལ་ཏེ་སྐྱེ་བ་སྔར་གྱུར་པ། །
རྒ་ཤི་འཕྱི་བ་ཡིན་ན་ནི། །
སྐྱེ་བ་རྒ་ཤི་མེད་པ་དང་། །
མ་ཤི་བར་ཡང་སྐྱེ་བར་འགྱུར། །

[Block 1286]
གལ་ཏེ་སྐྱེ་བ་སྔ་བར་གྱུར་ལ། དེའི་འོག་ཏུ་ཕྱིས༌[^794]རྒ་ཤི་དག་ལ་ཡང་སྔ་ཕྱི༌[^795]འབྱུང་བ་ཡིན་ན་དེ་ལྟ་ན་སྐྱེ་བ་དེ་ལ་རྒ་ཤི་མེད་པར་འགྱུར་རོ། །

[Block 1287]
དེ་ལ་རྒ་ཤི་མེད་པར་གྱུར༌[^796]ན་ཕྱིས་རྒ་ཤི་ག་ལས་འོང་བར་འགྱུར། ཅི་སྟེ་འོང་ན་ནི་རྒ་ཤི་གཞི་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1288]
དེ་དང་ཕྲད་དུ་ཟིན་ན་ཡང་དེ་ལ་ཅིར་ཡང་མི་འགྱུར་ཏེ། ངོ་བོ་ཉིད་ཀྱིས་རྒ་ཤི་མེད་པའི་ཕྱིར་རོ། །

[Block 1289]
ཡང་གཞན་ཡང་། མ་ཤི་བ་ཡང་སྐྱེ་བར་འགྱུར་ཏེ། འདི་ལྟར་སྐྱེ་བ་སྔ་བར་བརྟགས༌[^797]ན་དེ་སྔར་གཞན་དུ་མ་ཤི་བར་འདིར་སྐྱེ་བར་ཐལ་བར་འགྱུར་རོ། །

[Block 1290]
དེ་ལྟ་ན་འཁོར་བ་ཐོག་མ་དང་ལྡན་པར་འགྱུར་ཏེ། དེ་ཡང་མི་འདོད་པས་དེའི་ཕྱིར་སྐྱེ་བ་སྔ་ལ་རྒ་ཤི་འཕྱི་བར་མི་འཐད་དོ། །

[Block 1291]
ཅི་སྟེ་སྐྱོན་དེ༌[^798]གྱུར་ན་མི་རུང་ངོ་སྙམ་པས་རྒ་ཤི་སྔ་མ་ཁོ་ན་ཡིན་ལ། སྐྱེ་བ་འཕྱིའོ་ཞེ་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 1292 [VERSE]]
གལ་ཏེ་སྐྱེ་བ་འཕྱི་གྱུར་ལ། །
རྒ་ཤི་སྔ་བ་ཡིན་ན་ནི། །
སྐྱེ་བ་མེད་པའི་རྒ་ཤི་ནི། །
རྒྱུ་མེད་པར་ནི་ཇི་ལྟར་འགྱུར། །

[Block 1293]
གལ་ཏེ་དེའི་རྒ་ཤི་སྔ་བར་གྱུར་ལ། སྐྱེ་བ་འཕྱི་བར༌[^799]གྱུར་ན་དེ་ལྟ་ན་གཞི་མེད་པའི་རྒ་ཤི་རྒྱུ་མེད་པར་ཐལ་བར་འགྱུར་བས་དེ་ཡང་མི་འདོད་དོ། །

[Block 1294]
འདི་ལྟར་མ་སྐྱེས་ཤིང་མེད་པའི་རྒ་ཤི་གཞི་མེད་ཅིང་རྒྱུ་མེད་པར་ཇི་ལྟར་འབྱུང་བར་འགྱུར། སྐྱེས་ཤིང་ཡོད་པ་ལ་རྒ་ཤི་བསྟན་པར་རིགས་སོ། །

[Block 1295]
དེ་ལྟ་བས་ན་སྐྱེ་བ་འཕྱི་ལ་རྒ་ཤི་སྔ་བར་ཡང་མི་འཐད་དོ། །

[Block 1296]
སྨྲས་པ། དེ་དག་ལ་སྔ་ཕྱི་མེད་དེ། དེ་ནི་རྒ་ཤི་དང་རྗེས་སུ་འབྲེལ་བཞིན་པ་ཁོ་ནར་སྐྱེའོ། །

[Block 1297]
བཤད་པ།

[Block 1298 [VERSE]]
སྐྱེ་བ་དང་ནི་རྒ་ཤི་དག །
ལྷན་ཅིག་རུང་བ་མ་ཡིན་ནོ། །

[Block 1299]
སྐྱེ་བ་དང་རྒ་ཤི་དག་ལྷན་ཅིག་ཉིད་དུ་འགྱུར་བར་མི་འཐད་དོ། །

[Block 1300]
ཅི་སྟེ་འགྱུར་ན་ནི།
--- END BLOCKS ---
