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
[Block 1296 [HEADING]]
##### ས་གང་ན་སེམས་གང་ལ་སེམས་ལས་བྱུང་བ་ཇི་སྙེད་ཅིག་འབྱུང་བ། ^2-2-2-2-0

[Block 1297 [HEADING]]
###### འདོད་པ་ན་སྤྱོད་པའི་སེམས། ^2-2-2-2-1-0

[Block 1298]
རྟོག་པ་དང་དཔྱོད་པ༌[^565]དང་འགྱོད་པ་དང་གཉིད་ལ་སོགས་པ་མ་ངེས་པ་གཞན་དག་ཀྱང་ཡོད་པས། དེ་ལ་སེམས་གང་ཞིག་ལ་སེམས་ལས་བྱུང་བ་དུ་ཞིག་གདོན་མི་ཟ་བར་འབྱུང་བ་བརྗོད་པར་བྱ་སྟེ། རེ་ཞིག་འདོད་པ་ན་སྤྱོད་པའི་སེམས་ནི་རྣམ་པ་ལྔ་སྟེ། དགེ་བ་དང་མི་དགེ་བ་རྣམ་པ་གཉིས་ཏེ། མ་འདྲེས་པ་དང་། ཉོན་མོངས་པ་གཞན་དང་མཚུངས་པར་ལྡན་པ་དང་། ལུང་དུ་མ་བསྟན་པ་རྣམ་པ་གཉིས་ཏེ། བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དང་། མ་བསྒྲིབས་པ༌[^566]ལ་ལུང་དུ་མ་བསྟན་པའོ། །

[Block 1299]
དེ་ལ་རེ་ཞིག་འདོད་པ་ན་སྤྱོད་པའི་སེམས་ནི་ངེས་པར་རྟོག་པ་དང་དཔྱོད་པ་དང་བཅས་པ་ཡིན་པས་དེའི་ཕྱིར་འདི་ལ།

[Block 1300 [HEADING]]
###### **དགེ་བ།** ^2-2-2-2-1-1-0

[Block 1301 [VERSE]]
འདོད་པའི་དགེ་བའི་སེམས་ལ་ནི། །
རྟོག་དང་དཔྱོད་དང་བཅས་པའི་ཕྱིར། །
སེམས་ལས་བྱུང་བ་ཉི་ཤུ་གཉིས། །

[Block 1302]
གདོན་མི་ཟ་བར་འབྱུང་སྟེ། ས་མང་པོ་པ་བཅུ་དང་། དགེ་བའི་ས་མང་པོ་པ་བཅུ་དང་། རྟོག་པ་དང་དཔྱོད་པའོ། །

[Block 1303]
ལ་ལ་དག་ཏུ་འགྱོད་པ་བསྣན། །དགེ་བའི་སེམས་ཐམས་ཅད་ལ་ནི་འགྱོད་པ་མེད་པས་གང་ལ་ཡོད་པ་དེར་དེ་ཉིད་ཀྱིས་གླགས་ན་སེམས་ལས་བྱུང་བ་ཉི་ཤུ་རྩ་གསུམ་འབྱུང་ངོ་། །འགྱོད་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞིག་ཅེ་ན། ངན་པར་བྱས་པའི་ངོ་བོ་ཉིད༌[^567]ནི་འགྱོད་པའོ། །

[Block 1304]
འདི༌[^568]ནི་འགྱོད་པ་ལ་དམིགས་པའི་ཆོས་ཡིད་ལ་གཅགས་པ་ལ་འགྱོད་པ་ཞེས་བྱ་སྟེ། དཔེར་ན་སྟོང་པ་ཉིད་ལ་དམིགས་པའི་རྣམ་པར་ཐར་པའི་སྒོ་ལ་སྟོང་པ་ཞེས་བྱ་བ་དང་། མི་སྡུག་པ་ལ་དམིགས་པའི་མ་ཆགས་པ་ལ་མི་སྡུག་པ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 1305]
འཇིག་རྟེན་ན་ཡང་གྲོང་ཐམས་ཅད་ལྷགས་སོ། །

[Block 1306]
ཡུལ་ཐམས་ཅད་ལྷགས་སོ་ཞེས་གནས༌[^569]པ་སྟོན་པ༌[^570]མཐོང་ལ། འགྱོད་པ་ཡང་ཡིད་ལ་གཅགས་པའི༌[^571]གནས་སུ་གྱུར་པ་ཡིན་ནོ། །

[Block 1307]
ཡང་ན་འདི་ནི་འབྲས་བུ་ལ་རྒྱུ་བཏགས་པ་ཡིན་ཏེ། དཔེར་ན་རེག་པའི་སྐྱེ་མཆེད་དྲུག་པོ་འདི་དག་ནི་སྔོན་གྱི་ལས་ཡིན་པར་རིག་པར་བྱའོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 1308]
འོ་ན་གང་མ་བྱས་པ་ལ་དམིགས་པ་དེ་ཇི་ལྟར་འགྱོད་པ་ཡིན་ཞེ་ན། མ་བྱས་པ་ལ༌[^572]བྱས་པ་ཞེས་བྱ་བ་ཡོད་དེ། བདག་གིས་མ་བྱས་པ་གང་ཡིན་པ་དེ་མ་ལེགས་པ་བྱས་སོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1309]
འགྱོད་པ་དགེ་བ་གང་ཞེ་ན། དགེ་བ་མ་བྱས་པ་དང་མི་དགེ་བ་བྱས་པ༌[^573]ནས་གདུང་བ་གང་ཡིན་པའོ། །

[Block 1310]
བཟློག་པ་ནི་འགྱོད་པ་མི་དགེ་བ་ཡིན་ཏེ། དེ་གཉི་ག་ཡང་གཉི་ག་ལ་བརྟེན་པ༌[^574]ཡིན་ནོ། །

[Block 1311 [HEADING]]
###### **མི་དགེ་བ་མ་འདྲེས་པ་དང་ལྟ་བ་དང་ལྡན་པ།** ^2-2-2-2-1-2-0

[Block 1312 [VERSE]]
མི་དགེ་བ་ནི་མ་འདྲེས་དང་། །
ལྟ་དང་ལྡན་ལའང་ཉི་ཤུ་འབྱུང་། །

[Block 1313]
མི་དགེ་བའི་སེམས་མ་འདྲེས་པ་གང་ཡིན་པ་དེ་ལ་ནི་སེམས་ལས་བྱུང་བ་ཉི་ཤུ་འབྱུང་སྟེ། ས་མང་པོ་པ་བཅུ་དང་། ཉོན་མོངས་པའི་ས་མང་པོ་པ་དྲུག་དང་། མི་དགེ་བའི་རྩ་བའི་ས་མང་པོ་པ་གཉིས་དང་། རྟོག་པ་དང་དཔྱོད་པའོ། །

[Block 1314]
མ་འདྲེས་པ་ཞེས་བྱ་བ་ནི། སེམས་གང་ལ་མ་རིག་པ་འབའ་ཞིག་ཡོད་ཀྱི་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པ༌[^575]གཞན་མེད་པའོ། །

[Block 1315]
མི་དགེ་བའི་སེམས་ལྟ་བ་དང་ལྡན་པ་ལ་ཡང་ཉི་ཤུ་འབྱུང་སྟེ། མ་འདྲེས་པ་ལ་གང་དག་འབྱུང་བ་ཁོ་ནའོ། །

[Block 1316]
ལྟ་བ་ལྷག་པའི་ཕྱིར་ཉི་ཤུ་རྩ་གཅིག་འབྱུང་བ་མ་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ། འདི་ལྟར་ས་མང་པོ་པ་ཁོ་ནའི་ཤེས་རབ་ཀྱི་ཁྱད་པར་འགའ་ཞིག་ལ་ལྟ་བ་ཞེས་བྱའོ། །

[Block 1317]
དེ་ལ་མི་དགེ་བ་ལྟ་བ་དང་ལྡན་པ་ནི་གང་ལ་ལོག་པར་ལྟ་བའམ། ལྟ་བ་མཆོག་ཏུ་འཛིན་པའམ། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་ཡོད་པའོ། །

[Block 1318 [HEADING]]
###### **ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་གཞན་དང་མཚུངས་པར་ལྡན་པ།** ^2-2-2-2-1-3-0

[Block 1319 [VERSE]]
ཉོན་མོངས་བཞི་དང་ཁྲོ་སོགས་དང་། །
འགྱོད་པ་དང་ནི་ཉི་ཤུ་གཅིག །

[Block 1320]
མི་དགེ་བའི་སེམས་འདོད་ཆགས་ཀྱང་རུང་། ཁོང་ཁྲོ་བ་ཡང་རུང་། ང་རྒྱལ་ཡང་རུང་། ཐེ་ཚོམ་ཡང་རུང་། ཉོན་མོངས་པ་བཞི་དང་མཚུངས་པར་ལྡན་པ་གང་ཡིན་པ་དེ་ལ་ནི་ཉི་ཤུ་རྩ་གཅིག་འབྱུང་སྟེ། ཉོན་མོངས་པ་དེ་དང་མ་འདྲེས་པར་བཤད་པ་ཉི་ཤུའོ། །

[Block 1321]
ཁྲོ་བ་ལ་སོགས་པ་ཉེ་བའི་ཉོན་མོངས་པ་ཇི་སྐད་བཤད་པ་དག་དང་མཚུངས་པར་ལྡན་པའི་སེམས་ལ་ཡང་ཉི་ཤུ་པོ་དེ་དག་དང་། ཉེ་བའི་ཉོན་མོངས་པ་དེ་དང་ཉི་ཤུ་རྩ་གཅིག་འབྱུང་ངོ་། །འགྱོད་པ་དང་ལྡན་པ་ལ་ཡང་ཉི་ཤུ་རྩ་གཅིག་འབྱུང་སྟེ། འགྱོད་པ་དེ་ཉིད་ཉི་ཤུ་རྩ་གཅིག་པ་ཡིན་ནོ། །

[Block 1322]
མདོར་ན་མི་དགེ་བའི་སེམས་མ་འདྲེས་པ་དང་། ལྟ་བ་དང་མཚུངས་པར་ལྡན་པ་ལ་ཡང་ཉི་ཤུ་འབྱུང་ལ། ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་གཞན་དང་མཚུངས་པར་ལྡན་པ་ལ་ནི་ཉི་ཤུ་རྩ་གཅིག་འབྱུང་ངོ་། །

[Block 1323 [HEADING]]
###### **བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ།** ^2-2-2-2-1-4-0

[Block 1324]
བསྒྲིབས་ལ་བཅོ་བརྒྱད། འདོད་པའི་ཁམས་ན་འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། མཐར་འཛིན་པར་ལྟ་བ་དང་མཚུངས་པར་ལྡན་པའི་སེམས་ནི་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའོ། །

[Block 1325]
དེ་ལ་ནི་སེམས་ལས་བྱུང་བ་བཅོ་བརྒྱད་འབྱུང་སྟེ། ས་དང༌[^576]པོ་པ་བཅུ་དང་། ཉོན་མོངས་པའི་ས་མང་པོ་པ་དྲུག་དང་། རྟོག་པ་དང་དཔྱོད་པའོ། །

[Block 1326]
ལྟ་བ་ནི་སྔ་མ་དང་འདྲ་བ་ཉིད་དེ་ལྷག་པ་མ་ཡིན་ནོ། །

[Block 1327 [HEADING]]
###### **མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ།** ^2-2-2-2-1-5-0

[Block 1328]
ལུང་མ་བསྟན་པ༌[^577]གཞན་ལ་བཅུ་གཉིས་དག་ཏུ་འདོད། བསྒྲིབས༌[^578]ལ་ལུང་དུ་མ་བསྟན་པ་ལས་གཞན་པ་ནི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའོ། །

[Block 1329]
དེ་ལ་ནི་སེམས་ལས་བྱུང་བ་བཅུ་གཉིས་འབྱུང་བར་འདོད་དེ། ས་མང་པོ་པ་བཅུ་དང་། རྟོག་པ་དང་དཔྱོད་པ་དག་གོ། །

[Block 1330]
ཉི་འོག་པ་དག་ནི་འགྱོད་པ་ལུང་དུ་མ་བསྟན་པར་ཡང་འདོད་ལ་ཡིད་མི་བདེ་བ་ཡང་ཡིད་བདེ་བ་དང་འདྲ་བར་ལུང་དུ་མ་བསྟན་པར་ཡང༌[^579]འདོད་དེ། དེ་དག་གི་ལྟར་ན་དེ་དང་མཚུངས་པར་ལྡན་པའི་སེམས་ལ་བཅུ་གསུམ་འབྱུང་བར་འགྱུར་རོ། །

[Block 1331 [HEADING]]
###### **གཉིད།** ^2-2-2-2-1-6-0

[Block 1332 [VERSE]]
གཉིད་ནི་ཀུན་ལ་མི་འགལ་ཕྱིར། །
གང་ལ་ཡོད་པ་དེས་བསྣན་ནོ། །

[Block 1333]
གཉིད་ནི་དགེ་བ་དང་། མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པ་དང་ཡིན་པའི༌[^580]ཕྱིར་ཇི་སྐད་བཤད་པའི་སེམས་ཐམས་ཅད་དང་མི་འགལ་བས། དེའི་ཕྱིར་གང་ལ་དེ་ཡོད་པ་དེ་ལ་དེས་བསྣན་པར་རིག་པར་བྱ་སྟེ། གང་ལ་ཉི་ཤུ་རྩ་གཉིས་འབྱུང་བ་དེ་ལ་ནི་ཉི་ཤུ་རྩ་གསུམ་མོ། །

[Block 1334]
[^581]གང་ལ་ཉི་ཤུ་རྩ་གསུམ་འབྱུང་བ་དེ་ལ་ནི་ཉི་ཤུ་རྩ་བཞིའོ༌[^582]ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 1335 [HEADING]]
###### བསམ་གཏན་དང་པོ་ལ་སོགས་པ། ^2-2-2-2-2-0
--- END BLOCKS ---
