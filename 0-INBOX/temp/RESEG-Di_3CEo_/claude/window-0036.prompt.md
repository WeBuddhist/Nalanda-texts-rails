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
[Block 1261]
དེ་ཡང་།

[Block 1262 [VERSE]]
ཇི་ལྟར་འཕངས་བཞིན་རིམ་གྱིས་རྒྱུན། །
སྐྱེས་ནས་ལས་དང་ཉོན་མོངས་ཀྱིས། །
འཇིག་རྟེན་ཕ་རོལ་དག་ཏུ་འགྲོ། །

[Block 1263]
ཚེའི་ལས་ཐ་དད་པའི་ཕྱིར་ཕུང་པོའི་རྒྱུན་ཐམས་ཅད་ཀྱིས་འཕེན་པར་འདྲ་བ་ནི་མ་ཡིན་པས། དེའི་ཕྱིར་གང་ཞིག་ཇི་སྲིད་དུ་འཕངས་པ་དེ་སྲིད་ནུར་ནུར་པོ་ལ་སོགས་པའི་རིམ་གྱིས་སྐྱེ་བར་འགྱུར་ཏེ། དབང་པོ་རྣམས་ཡོངས་སུ་སྨིན་ནས་ནི༌[^470]ཉོན་མོངས་པ་རྣམས་ཀུན་དུ་སྤྱོད་ཅིང་ལས་རྣམས་ཀྱང་ཉེ་བར་སོག༌[^471]པར་འགྱུར་རོ། །

[Block 1264]
དེ་དག་ལུས་ཞིག་ནས་ཡང་སྔ་མ་བཞིན་དུ་སྲིད་པ་བར་མའི་རྒྱུན་གྱིས་འཇིག་རྟེན་ཕ་རོལ་དུ་འགྲོ་སྟེ། དེ་ལྟར། སྲིད་པའི་འཁོར་ལོ་ཐོག་མ་མེད། །རྣམ་པ་དེས་ན་ལས་དང་ཉོན་མོངས་པའི་རྒྱུ་ལས་བྱུང་བའི་སྐྱེ་བ་དང་། ཡང་དེ་ལས་བྱུང་བའི་ལས་དང་ཉོན་མོངས་པ་རྣམས་དང་། ཡང་དེ་དག་ལས་སྐྱེ་བ་ཡིན་པས་ན་སྲིད་པའི་འཁོར་ལོ་ཐོག་མ་མེད་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1265 [HEADING]]
#### རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ། ^3-1-7-0

[Block 1266]
དེ་ལྟར་ཕུང་པོའི་རྒྱུན་སྐྱེ་བའི་གནས་སྐབས་གསུམ་བསྟན་པ་གང་ཡིན་པ་དེ་ནི།

[Block 1267 [VERSE]]
རྟེན་ཅིང་འབྲེལ་པར༌[^472]འབྱུང་བ་ཡི། །
ཡན་ལག་བཅུ་གཉིས་ཆ་གསུམ་མོ། །

[Block 1268]
དེ་ལ་ཡན་ལག་བཅུ་གཉིས་པོ་ནི་མ་རིག་པ་ནས་རྒ་ཤིའི་བར་རོ། །

[Block 1269]
ཆ་གསུམ་ནི་སྔོན་གྱི་དང་། ཕྱི་མའི་མཐའ་དང་། བར་མའི་སྐྱེ་བ་དག་གོ། །

[Block 1270]
དེ་ཡང་། སྔོན་དང་ཕྱི་མཐའ་གཉིས་གཉིས་དང་། །བར་དུ་བརྒྱད། མ་རིག་པ་དང་འདུ་བྱེད་རྣམས་ནི་སྔོན་གྱི་མཐར་རོ། །

[Block 1271]
སྐྱེ་བ་དང་རྒ་ཤི་ནི་ཕྱི་མའི་མཐར་རོ། །

[Block 1272]
ལྷག་མ་བརྒྱད་ནི་བར་དུའོ། །

[Block 1273]
དེ་དག་ཀྱང་། ཡོངས་རྫོགས་ལྡན་ལ། འབྱུང་སྟེ། གང་ཞིག་གནས་སྐབས་འདི་ཐམས་ཅད་ལ་རེག་པ་གང་བར་མ་དོ་ཁོ་ནར་འཆི་བ་ཡང་མ་ཡིན་ལ། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1274]
དེ་ལ། མ་རིག་ཉོན་མོངས་སྔོན་གནས་སྐབས། །ཚེ་སྔ་མ་ལ་ཉོན་མོངས་པའི་གནས་སྐབས་གང་ཡིན་པ་དེ་ནི་འདི་ལ་མ་རིག་པ་ཞེས་བྱའོ། །

[Block 1275]
འདུ་བྱེད་དག་ནི་སྔོན་ལས་ཀྱི།[^473] །གནས་སྐབས་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཚེ་སྔ་མའི་བསོད་ནམས་ལ་སོགས་པའི་ལས་ཀྱི་གནས་སྐབས་གང་ཡིན་པ་དེ་ནི་འདུ་བྱེད་རྣམས་ཞེས་བྱ་སྟེ།

[Block 1276 [VERSE]]
ལས་གང་གིས་འདིར་རྣམ་པར་སྨིན་པའོ། །
རྣམ་ཤེས་མཚམས་སྦྱོར༌[^474]ཕུང་པོ་ཡིན། །

[Block 1277]
མའི་མངལ་དུ་ཉིང་མཚམས་སྦྱོར་བའི་སྐད་ཅིག་མ་ལ་ཕུང་པོ་ལྔ་ནི་རྣམ་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 1278 [VERSE]]
མིང་དང་གཟུགས་ནི་དེ་ཕན་ཆད། །
སྐྱེ་མཆེད་དྲུག་དོད་ཚུན་ཆད་དོ། །

[Block 1279]
མཚམས་སྦྱོར་བའི་སེམས་ཕན་ཆད་ཇི་སྲིད་དུ་སྐྱེ་མཆེད་དྲུག་མ་དོད་ཀྱི་བར་སྐབས་དེ་ནི་མིང་དང་གཟུགས་ཞེས་བྱའོ། །

[Block 1280]
དེ་ནི་གསུམ་འདུས་ཚུན་ཆད་དོ། །

[Block 1281]
སྐྱེ་མཆེད་དྲུག་དོད་ནས་ཇི་སྲིད་དུ་དབང་པོ་དང་ཡུལ་དང་རྣམ་པར་ཤེས་པ་དང༌[^475]གསུམ་མ་འདུས་པ་དེ་སྲིད་ཀྱི་གནས་སྐབས་དེ༌[^476]ནི་སྐྱེ་མཆེད་དྲུག་ཅེས་བྱའོ། །

[Block 1282 [VERSE]]
རེག་པ་བདེ་སྡུག་ལ་སོགས་ཀྱི། །
རྒྱུ་ཤེས་ནུས་པ་ཚུན་ཆད་དོ། །

[Block 1283]
རེག་པ་ནི་དེ་སྲིད་དུ་འབྱུང་སྟེ། ཇི་སྲིད་དུ་ཚོར་བ་གསུམ་གྱི་རྒྱུ་བ་ཡོངས་སུ་གཅོད་པར་མི་ནུས་པའི་བར་རོ། །

[Block 1284]
ཡོངས་སུ་གཅོད་ནུས་ནས་ནི། ཚོར་འཁྲིག་ཚུན་ཆད། ཚོར་བའི་གནས་སྐབས་ནི་ཇི་སྲིད་དུ་འཁྲིག་པའི་འདོད་ཆགས་ཀུན་དུ་མི་སྤྱོད་པའི་བར་རོ། །

[Block 1285]
སྲིད་པ༌[^477]ནི། ལོངས་སྤྱོད་འཁྲིག་པའི་ཆགས་ཅན་གྱི། །འདོད་པའི་ཡོན་ཏན་དང་། འཁྲིག་པའི་འདོད་ཆགས་ཀུན་དུ་སྤྱོད་པའི་གནས་སྐབས་ཇི་སྲིད་དུ་ཡུལ་ཡོངས་སུ་ཚོལ་བ་ལ་མ་ཞུགས་པ་ནི་སྲེད་པའོ། །

[Block 1286 [VERSE]]
ཉེ་བར་ལེན་པ་ལོངས་སྤྱོད་རྣམས། །
ཐོབ་པར་བྱ་ཕྱིར་ཡོངས་རྒྱུག་པའི། །

[Block 1287]
གནས་སྐབས་གང་དུ་ཡུལ་ཐོབ་པར་བྱ་བའི་ཕྱིར་ཡོངས་སུ་ཚོལ་བ་ལ༌[^478]ཞུགས་པ་ཐམས་ཅད་དུ་རྒྱུག་པ་དེ་ནི་ལེན་པའོ། །

[Block 1288]
དེ་ལྟར་ཡོངས་སུ་རྒྱུག་པ་ན།

[Block 1289 [VERSE]]
དེ་སྲིད་འབྲས་བུ་འབྱུང་བ་ཡི། །
ལས་བྱེད་དེ་ནི་སྲིད་པ་ཡིན། །

[Block 1290]
དེ་ཡུལ་རྣམས་ཐོབ་པར་བྱ་བའི་ཕྱིར་ཡོངས་སུ་རྒྱུག་པ་ན་ཡང་སྲིད་པའི་ལས༌[^479]སོགས་པ་དེ་ནི་དེའི་སྲིད་པ་ཡིན་ནོ། །

[Block 1291]
ལས་དེས་ཀྱང་འདི་ནས་ཚེ་ཕྱི་མར་ཉིང་མཚམས་སྦྱོར་བར་འགྱུར་ཏེ། ཉིང་མཚམས་སྦྱོར་བ། དེ་ནི། སྐྱེ་བ་ཡིན། འདིར་རྣམ་པར་ཤེས་པའི་ཡན་ལག་གང་ཡིན་པ་དེ་ནི་ཚེ་གཞན་དུ་སྐྱེ་བ་ཡིན་ནོ། །

[Block 1292]
དེ་ཕན་ཆད། ཚོར་བའི་བར་ནི་རྒ་ཤི་ཡིན། །སྐྱེ་བ་ཕན་ཆད་ཚོར་བའི་གནས་སྐབས་ཀྱི་བར་ནི་རྒ་ཤི་ཡིན་ཏེ། དེ་ལ་ཡན་ལག་བཞི་པོ་མིང་དང་གཟུགས་དང་། སྐྱེ་མཆེད་དྲུག་དང་། རེག་པ་དང་། ཚོར་བ་གང་དག༌[^480]ཡིན་པ་དེ་དག་ཉིད་གཞན་དག་ཏུ་རྒ་ཤི་ཡིན་ནོ། །

[Block 1293]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མང་པོ་ཡོད་ཀྱང་།

[Block 1294 [VERSE]]
འདི་ནི་གནས་སྐབས་པར་འདོད་ལོ། །
གཙོ་བོའི་ཕྱིར་ན་ཡན་ལག་བསྒྲགས། །

[Block 1295]
མ་རིག་པ་ལ་སོགས་པ་གཙོ་བོ་ཡིན་པའི་གནས་སྐབས་སུ་ནི་མ་རིག་པ་ལ་སོགས་པ་དག་ཁོ་ནར་གསུངས་སོ། །

[Block 1296]
སེམས་ཅན་དུ་སྟོན་པ་ཁོ་ནའི་རྟེན་ཅིང་འབྲེལ་པ་ཆ་གསུམ་གསུངས་པ་ཡང་།

[Block 1297 [VERSE]]
སྔོན་དང་ཕྱི་མཐའ་བར་དག་ལ། །
རྨོངས་པ་རྣམ་པར་བཟློག་ཕྱིར་རོ། །

[Block 1298]
ཇི་ལྟར་སྔོན་གྱི་མཐའ་ལས་བར་མ་འབྱུང་བ་དང་། བར་མ་ལས་ཕྱི་མའི་མཐའ་ཞེས་བྱ་བ་རྨོངས་པ་འདི་རྣམ་པར་བཟློག་པའི་ཕྱིར་ཆ་གསུམ་པ་དང་སེམས་ཅན་དུ་སྟོན་པ་གསུངས་སོ། །

[Block 1299]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དེ་ཡང་འདིར་ཉོན་མོངས་པ་དང་། ལས་དང་། གཞིའི་རང་བཞིན་ཏེ། དེ་ལ། ཉོན་མོངས་གསུམ་མོ། །

[Block 1300]
མ་རིག་པ་དང་། སྲེད་པ་དང་། ལེན་པ༌[^481]རྣམས་སོ། །
--- END BLOCKS ---
