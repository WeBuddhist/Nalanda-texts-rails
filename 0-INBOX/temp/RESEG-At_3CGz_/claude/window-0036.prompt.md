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
[Block 1261 [VERSE]]
མདོ་དང་བསྟན་བཅོས་གླེགས་བམ་མཐོང་བ་ཡིས། །
གསུང་རབ་རྒྱ་མཚོ་ཟབ་མོའི་དོན་ལ་སྤྱོད། །
དེ་དག་ལོང་བ་ལྟ་བུར་གྱུར་པ་སྟེ། །
ཐེག་ཆེན་ལམ་མཆོག་དེ་ཡིས་ཤེས་པ་མིན། །

[Block 1262 [VERSE]]
དེ་བས་ལོག་རྟོགས་རྗེས་སུ་འབྲང་མི་བྱ། །
ལེགས་པའི་འབྱུང་གནས་ཐེག་པ་ཆེན་པོའི་ལམ། །
བླ་མ༌[^710]མིག་དང་འདྲ་བ་མེད་པ་ཡིས། །
མ་མཐོང་མི་མཐོང་མཐོང་བར་མི་འགྱུར་རོ། །

[Block 1263 [VERSE]]
ཐེག་པ་ཆེན་པོ་རྒྱ་མཚོ་ལྟར་ཟབ་ཅིང་། །
ནམ་མཁའ་ལྟ་བུར་ཤིན་ཏུ་རྒྱ་ཆེ་བ། །
བླ་མ་དང་བྲལ་རང་དགའ༌[^711]སྨྲ་བ་ཡིས།[^712] །
མདོ་དང་བསྟན་བཅོས་དག་གི༌[^713]གླེགས་བམ་དེ། །

[Block 1264 [VERSE]]
མཐོང་བས་ཚིམ་སྟེ་བླ་མ་སྟེན་མི་བྱེད། །
དེ་དག་གིས་ནི་ཐེག་པ་ཆེན་པོ་ཡི། །
གཏམ་གྱི་རིམ་པ་ཙམ་ཡང་མི་ཤེས་ན། །
ཟབ་དང་རྒྱ་ཆེའི་དོན་ལྟ་ག་ལ་ཡོད། །

[Block 1265 [VERSE]]
ཐེག་ཆེན་བག་ཆགས་བཟང་པོ་ཡོད་པ་ཡི།[^714] །
བླ་མ་དམ་པས་ཟིན་པའི་སྐྱེ་བོ་ནི། །
མཁས་པ་སུ་ཞིག་དེ་ཡི་རྗེས་སུ་འབྲང་། །
དིང་སང་བསྟན་པ་ནུབ་ཀར་གྱུར་པ་ཡི། །

[Block 1266 [VERSE]]
འཇིགས་པ་ཆེན་པོའི་དུས་འདི་བྱུང་བས་ན། །
རྟོགས་ལྡན་མཁས་པ་དག་གིས་བག་ཡོད་གྱིས།[^715] །
བླ་མ་བཟང་པོ་བརྒྱུད་པའི་གང་ཟག་ནི། །
ཡུལ་དང་ས་ཕྱོགས་གང་ན་ཡོད་པ་དྲི། །

[Block 1267 [VERSE]]
རྙེད་ནས་ཟླ་བའམ་ལོར་ཡང་བསྟེན་བྱས་ལ། །
བསྙེན་བཀུར་ཚུལ་བཞིན་བྱས་ལ་མཉེས་པར་བྱ། །
སྐྱེས་བུ་དེ་ཡི་ལུས་དང་ངག་དག་གི། །
སྤྱོད་ཚུལ་ཤིན་ཏུ་ངན་པར་སྤྱོད་ན་ཡང་། །

[Block 1268 [VERSE]]
དེ་ལ་མི་བལྟ་དམ་ཆོས་བླང་བར་བྱ། །
དཔེར་ན་བུང་བས་མེ་ཏོག་འཛིན་པའི་ཚེ། །
སྦྲང་རྩི་ཁྱེར་ནས་མེ་ཏོག་ལུས་པ་དང་། །
མཁས་པ་དེས་ཀྱང་དེ་དང་འདྲ་བར་སྤྱད།[^716] །

[Block 1269 [VERSE]]
སྤྱོད་ཚུལ་མི་བལྟ་དེ་ཡི་གདམས་ངག་མཉན། །
ཉེར་བསྟན་དེ་ལ་སེམས་ནི་གོམས་པས་ན། །
ཚེ་འདི་ཉིད་ལ་བྱང་ཆུབ་ཐོབ་བྱའི་ཕྱིར། །
འཁོར་ལོ་སྡོམ་པ་ལ་སོགས་གསང་སྔགས་ཀྱི།[^717] །

[Block 1270]
གདམས་ངག་བླ་མ་བརྒྱུད༌[^718]པ་ཅན་ལ་ཞུ། །

[Block 1271 [VERSE]]
དབང་བསྐུར༌[^719]གཉིས་པ་སྤངས་པ་ཡི། །
གསང་སྔགས་གཞུང་ལུགས་མི་ཤེས་ན། །
རྣམ་རྟོག་དུ་མས་བཅིངས་གྱུར་པས། །
མྱུར་དུ་སངས་རྒྱས་འགྲུབ་མི་འགྱུར། །

[Block 1272]
ཡང་སྨྲས་པ།

[Block 1273 [VERSE]]
ཐུབ་པའི་བསྟན་པ་མདངས་ཉམས་གྱུར་པ་ཡི། །
སྟོན་པའི་དམ་ཆོས་རྣམ་པར་འཇིག་པ་ནི།[^720] །
དིང་སང་དུས་ན་བསྟན་པ་འཇིག་པ་ན།[^721] །
སངས་རྒྱས་ཉིད་ཀྱི་སློབ་མ་མ་གཏོགས་པར། །

[Block 1274 [VERSE]]
ཕ་རོལ་པ་དང་ཐ་མལ་སྐྱེ་བོ་ཡིས། །
ཐུབ་པའི་བསྟན་པ་སུས་ཀྱང་འཇིག་མི་ནུས། །
ཁྱད་པར་དུ་ནི་རབ་ཏུ་བྱུང་བས་འཇིག །
ཁ་ཅིག་གསང་སྔགས་རྒྱུད་ཀྱི་རྗེས་འབྲངས་ནས། །

[Block 1275 [VERSE]]
ལོག་པར་སྤྱོད་ཅིང་གཞན་ལའང་ལོག་པར་སྟོན། །
ཁ་ཅིག་ཤེས་རབ་ཕ་རོལ་ཕྱིན་པ་ཡི། །
ཇི་བཞིན་ཡང་དག་དོན་ནི་མི་ཤེས་པར། །
རྒྱུ་དང་འབྲས་བུ་ལ་སོགས་ཀུན་རྫོབ་པ། །

[Block 1276 [VERSE]]
འགོག་ཅིང་རང་བཞིན་རྣམ་པར་དག་ཅེས་སྨྲ།[^722] །
ཁ་ཅིག་སོ་སོར་ཐར་པ་འདུལ་བ་ཡི།[^723] །
བསླབ་པ་ཇི་སྙེད་གསུངས་པ་བཏང་བྱས་ནས། །
ཞིང་དང་ཁེ་སོགས་ཁྱིམ་པ་དང་འདྲེ་ཞིང་། །

[Block 1277]
གཙུག་ལག་ཁང་ནའང་སྣ་ཚོགས་གཏམ༌[^724]གྱིས་སྤྱོད། །འཕགས་པ་ལང་ཀར་གཤེགས་པ་ལས།

[Block 1278 [VERSE]]
ང་ཡི་བསྟན་པ་སུན་འབྱིན་པ། །
ངུར་སྨྲིག་གི་ནི་གོས་བགོས་ཤིང་། །
འབྲས་བུ་ཡོད་དང་མེད་སྨྲ་བ། །
མ་འོངས་པ་ན་འབྱུང་བར་འགྱུར། །

[Block 1279]
ཞེས་གསུངས་སོ། །

[Block 1280]
ཡང་དེ་ཉིད་ལས།

[Block 1281]
རྩོད་པའི་དུས་ཀྱི་ཐ་མ་ལ། །འཇིག་རྟེན་དམ་ཆོས་མི་བསྒོམ་མོ། །

[Block 1282]
ཞེས་གསུངས་སོ། །

[Block 1283]
མཁས་པ་ཆེན་པོ་ནོར་གྱི་རྩ་ལག་གི་ཞལ༌[^725]ནས་ཀྱང་།

[Block 1284 [VERSE]]
སྟོན་པ་འཇིག་རྟེན་མིག་ནི་ཟུམ་གྱུར་ཅིང་། །
དཔང་གྱུར་སྐྱེ་བོ་ཕལ་ཆེར་ཟད་པ་ན། །
དེ་ཉིད་མ་མཐོང་རང་དགར་སྤྱོད་པ་ཡི། །
ངན་རྟོག༌[^726]རྣམས་ཀྱིས༌[^727]བསྟན་པ་འདི་དཀྲུགས་སོ། །

[Block 1285 [VERSE]]
རང་བྱུང་རང་འབྱུང་བསྟན་པ་གཅེས་འཛིན་རྣམས། །
མཆོག་ཏུ་ཞིར༌[^728]གཤེགས་འགྲོ་མགོན་མེད་པ་ན། །
འདོམས་མེད་ཡོན་ཏན་འཇོམས་པར་བྱེད་པ་ཡི། །
དྲི་མས་དགའ་མགུར་དིང་སང་འདི་ན་སྤྱོད། །

[Block 1286 [VERSE]]
དེ་ལྟར་ཐུབ་པའི་བསྟན་པ་ཉམས་དགའ་འདི། །
ལྐོག་མར་སྲོག་འབྱིན་འདྲ་དང་དྲི་མ་རྣམས། །
སྟོབས་དང་ལྡན་པའི་དུས་སུ་རིག༌[^729]ནས་ནི། །
ཐར་པ༌[^730]འདོད་པ་དག་གིས༌[^731]བག་ཡོད་གྱིས། །

[Block 1287]
ཞེས་གསུངས་སོ། །

[Block 1288 [HEADING]]
## བསྔོ་བ། ^a-0

[Block 1289 [VERSE]]
དམ་པའི་གདམས་ངག་རྒྱས་པར་བཀོད་པ་འདི། །
སངས་རྒྱས་བསྟན་པ་ཇི་སྲིད་གནས་ཀྱི་བར། །
སྙིང་རྗེ་བྱང་ཆུབ་སེམས་དང་ལྡན་པ་དེ། །
བརྩོན་འགྲུས་ཀྱིས་ནི་ཉིན་མཚན་སྤྱོད་གྱུར་ཅིག །

[Block 1290 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 1291 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 1292]
བྱང་ཆུབ་ལམ་གྱི༌[^732]སྒྲོན་མའི་དཀའ་འགྲེལ་ཞེས་བྱ་བ་བྷཾ་ག་ལའི་རྒྱལ་པོའི་རིགས་རྒྱུད་ཤཱཀྱའི་དགེ་སློང་མཁས་པ་ཆེན་པོ་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་མཛད་པ་དཱི་པཾ་ཀ་ར་ཤྲཱི་ཛྙཱ་ནས་མཛད་པ་རྫོགས་སོ།། །།

[Block 1293 [HEADING]]
### འགྱུར་བྱང། ^b-2-0

[Block 1294 [VERSE]]
དད་པའི་ས་གཞི་ཚུལ་ཁྲིམས་ས་བོན་བསྟེན། །
བྱམས་པའི་མྱུ་གུ་ཏིང་འཛིན་ཆུས་བརླན་པའི། །
རྩ་བ་སྙིང་རྗེ་ཆུ་བ་བྱང་ཆུབ་སེམས། །
ཡལ་ག་ཕར་ཕྱིན༌[^733]ལོ་མ་བསྡུ་བའི་དངོས། །

[Block 1295 [VERSE]]
མེ་ཏོག་ནོར་བདུན་འབྲས་བུ་རྗེས་དྲན་དྲུག །
དགེ་བཅུའི་དྲིས་ཁྱབ་སློབ་མའི་བྱ་ཚོགས་འདུ། །
ཤིང་མཆོག་དེ་འདྲའི་བྱང་ཆུབ་སེམས་དཔའ་ནི། །
བྷཾ་ག་ལར་འཁྲུངས་མར་མེ་མཛད་དཔལ་ཞབས། །

[Block 1296 [VERSE]]
དིང་སང་དུས་ན་སངས་རྒྱས་གདུང་འཚོབ་པ། །
སྐྱེ་བོ༌[^734]དབུས་ན་ཉི་མ་བཞིན་དུ་ལྷམ།[^735] །
སྙན་པར་རབ་གྲགས་ཆོས་ལུགས་བཟང་པོ་ཤེས། །
སྡོམ་པས་རབ་བསྡམས་མཁས་དང་ནུས་པར་ལྡན། །

[Block 1297 [VERSE]]
རིགས་ཅན་རྣམས་ཀྱི་བླ་མར་འོས་པ་སྟེ། །
དེ་ནི་སངས་རྒྱས་རྣམས་ཀྱི་སྲས་གཅིག་པུ། །
བསམ་དང་ལྷག་བསམ་གསེར་དང་ཟླ་ཚེས་འདྲ། །
ཕ་རོལ་འགྲོ་བ་དག་གི་བསམ་པ་དང་། །

[Block 1298 [VERSE]]
སྤྱོད་ལམ་མཐུན༌[^736]ཞིང་ཆོས་ཀྱི་བཤད་པའང་སྟོན། །
ནམ་ཡང་གང་ཟག་ཕ་རོལ་མི་དད་པ། །
དུག་དང་འདྲ་བར་སྤོང་བྱེད་བསམ་རྗེས་འཇུག །
བྱ་བ་ངན་སྤངས་སྤྱོད་ལམ་ཉམས་པ་མེད། །

[Block 1299 [VERSE]]
སྐད་ཅིག་སྐད་ཅིག་གཉེན་པོའི་སྟོབས་དང་ལྡན། །
ཕྲིན་ལས་བཟང་པོས་ཡུལ་ཕྱོགས༌[^737]དབུས་སུ་འཁྲུངས། །
སྐྱེ་བ་བཟང་པོ་རྒྱལ་པོའི་རིགས་སུ་འཁྲུངས། །
རིགས་བརྒྱུད༌[^738]བཟང་པོ་ཐེག་ཆེན་རིགས་སུ་འཁྲུངས། །

[Block 1300 [VERSE]]
སྨོན་ལམ་བཟང་པོས་སངས་རྒྱས་སྲས་སུ་འཁྲུངས། །
དེ་འདྲའི་བླ་མ་བྱང་ཆུབ་སེམས་དཔའ་ནི། །
མར་མེ་མཛད་དཔལ་ཡེ་ཤེས་སྙིང་རྗེ་ཅན། །
སྐྱེས་མཆོག་དེ་ལ་འདུན་པའི་སློབ་མ་ནི། །
--- END BLOCKS ---
