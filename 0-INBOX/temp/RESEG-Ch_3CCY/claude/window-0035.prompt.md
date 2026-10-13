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
### ཚིགས་བཅད་རེ་གཉིས་པ། ^1-61-0

[Block 1227]
དེ་ལས་ཀྱང་དེ་ཉིད་རྟོག་པས་ཕྱིན་ཅི་ལོག་བཞི་ལས་བྱུང་བའི་མ་རིག་མེད།

[Block 1228 [VERSE]]
དེ་མེད་འདུ་བྱེད་འབྱུང་བ་ནི། །
སྲིད་མིན་དེ་བཞིན་ལྷག་མ་རྣམས། །

[Block 1229]
དེ་ཁོ་ན་ཉིད་མཐོང་བ་ནི་ཕྱིན་ཅི་མ་ལོག་པ་སྟེ། དེ་ཁོ་ན་ཉིད་དེ༌[^881]མཐོང་བ་དེ་དང༌[^882]འགལ་བའི་ཕྱིར་ཕྱིན་ཅི་ལོག་རྣམས་ངེས་པར་སྤོང་ལ། དེ་སྤངས་པས་ཕྱིན་ཅི་ལོག་ལས་བྱུང་བའི་མ་རིག་པ་སྤོང་ངོ་། །མ་རིག་པ་སྤངས་པས་མ་རིག་པའི་རྐྱེན་གྱིས་འདུ་བྱེད་ལྡོག་ལ་ད་འགགས་པས་སྐྱེ༌[^883]བའི་རྐྱེན་གྱི་རྒས༌[^884]པ་དང་ཤི་བ་ལ་སོགས་པའི་བར་དུ་ཐམས་ཅད་ལྡོག་གོ། །

[Block 1230]
སླར་ཡང༌[^885]ཇི་ལྟར་མ་རིག་པ་འགགས་པས༌[^886]འདུ་བྱེད་ལ་སོགས་པ་འགག་ཅེ༌[^887]ན། བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 1231 [HEADING]]
### ཚིགས་བཅད་རེ་གསུམ་པ། ^1-62-0

[Block 1232 [VERSE]]
གང་ལ་གང་རྟེན་སྐྱེ་བའི་དངོས། །
དེ་དེ་མེད་པས༌[^888]དེ་མི་སྐྱེ། །
དངོས་དང་དངོས་མེད་འདུས་མ་བྱས། །
འདུས་བྱས་ཞི་བས་མྱ་ངན་འདས། །

[Block 1233]
གང་ཞིག་མ་རིག་པ་ཞེས་བྱ་བའི་རྒྱུ་ལ་བརྟེན་ནས་འདུ་བྱེད་ཅེས་བྱ་བའི་འབྲས་བུ་གང་ཞིག་སྐྱེ།[^889] འདུ་བྱེད་ཅེས་བྱ་བའི་འབྲས་བུ་དེའི་རྒྱུ་མ་རིག་པ་ཞེས་བྱ་བ་མེད་ན་མི་འབྱུང་ངོ་ཞེས་བྱ་སྟེ། དེ་ལྟར་མ་རིག་པ་ལ་སོགས་པ་མེད་ན་འདུ་བྱེད་ལ་སོགས་པ་སྲིད་པ་མ་ཡིན་ནོ། །

[Block 1234]
གང་གི་ཚེ་འདི་ལྟར་མ་རིག་པ་ལ་སོགས་པ་འཇུག་པ་མེད་ན་དེའི་ཚེ་དངོས་པོ་མེད་ལ། དངོས་པོ་མེད་ན་དེ་ཡང་ལོག་པའི་རང་བཞིན་དངོས་པོ་མེད་པ་ཡང་མེད་དོ་ཞེས་བྱ་སྟེ། གང་ཡང་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་མེད་ན་ཡང་། དངོས་པོའི་ཚུལ་གྱིས༌[^890]འདུས་བྱས་དང་དངོས་པོ་མེད་པའི་ཚུལ་གྱིས༌[^891]འདུས་མ་བྱས་མེད་དོ་ཞེས་བྱ་སྟེ། དངོས་དང་དངོས་མེད་དང་འདུས་བྱས་དང་འདུས་མ་བྱས་དག་ཞི་བའོ། །

[Block 1235]
ཞི་བ་ནི་མི་འཇུག་པ་ལ། དེ་ཉིད་མྱ་ངན་ལས༌[^892]འདས་པའོ། །

[Block 1236]
སླར་ཡང་འདུས་མ་བྱས་ཀྱི་ཚུལ༌[^893]མྱ་ངན་ལས་འདས་པ་ཡང་མ་ཡིན་ཏེ། འདུས་མ་བྱས་སུ་རྟོག་པ་འཇུག་པར་ཐལ་བས་སོ། །

[Block 1237]
འདིར་སྨྲས་པ། གང་སྨོས་པའི་དེ་ཁོ་ན་ཉིད་རྟོགས་པས་ཕྱིན་ཅི་ལོག་བཞི་ལས་བྱུང་བའི་མ་རིག་པ་མི་འབྱུང་ངོ་ཞེས་པས། སླར་ཡང་ཅི་མ་རིག་པའི་མཚན་ཉིད་དང་། དམིགས་པ་ནི་ཅི་ཞིག་གང་ལས་དེ་ཁོ་ན༌[^894]མཐོང་བ་ན་མི་འབྱུང་ངོ༌[^895]ཞེ་ན། མཚན་ཉིད་དང་དམིགས་པ་དག་བསྒྲུབ་པར་འདོད་པས་གསུངས་པ།

[Block 1238 [HEADING]]
### ཚིགས་བཅད་རེ་བཞི་པ། ^1-63-0

[Block 1239 [VERSE]]
རྒྱུ་རྐྱེན་ལས་སྐྱེས་དངོས་པོ་རྣམས། །
དངོས་པོར་ཁོང་དུ་ཆུད་པ་གང་། །
སྟོན་པས་མ་རིག་པར་གསུངས་ལ། །
དེ་ལས་ཡན་ལག་བཅུ་གཉིས་འཇུག །

[Block 1240]
རྒྱུ་དང་རྐྱེན་ལས་སྐྱེས་པའི་དངོས་པོ་ངོ་བོ་ཉིད་ཀྱིས༌[^896]མ་སྐྱེས་པ་ལ། དེ་དག་ལ་གང་ཞིག་རང་བཞིན་དུ་རྟོག་པ་དེ་ལ་མ་རིག་པར་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་ལ། ཡང་དག་པ་ཇི་ལྟ་བར་གནས་པའི་རང་བཞིན་མེད་པ་མ་རྟོགས་པའི་ཕྱིར། མ་རྟོགས་པ་ལས་མ་རིག་པ་ཞེས་བརྗོད་དོ། །

[Block 1241]
དེ་ཡང་རང་བཞིན་དུ་སྒྲོ་འདོགས་པ་ལ་ཞུགས་པའི་ཕྱིར་དང་། རང་བཞིན་ལ་དམིགས་པས་དེ་ཁོ་ན་ཉིད་ཡོངས་སུ་མ་ཤེས་པའི་ངོ་བོའི་ཕྱིར་མི་ཤེས་པའི་རང་བཞིན་ལ། མ་རིག་པ་དེ་ལས་འདུ་བྱེད་ལ་སོགས་པའི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་ཡན་ལག་བཅུ་གཉིས་འཇུག་གོ། །

[Block 1242]
ཡང་འདིའི་མ་རིག་པ་སྒྲོ་བཏགས་ནས་འཇུག་པ་ཇི་ལྟར་བཟློག་པར་བྱ་ཞེ་ན། གསུངས་པ།

[Block 1243 [HEADING]]
### ཚིགས་བཅད་རེ་ལྔ་པ། ^1-64-0

[Block 1244 [VERSE]]
དངོས་པོ་སྟོང་པར་ཡང་དག་པར། །
ཤེས་ན་རྨོངས་པ་མི་འཇུག་ལ། །
མ་རིག་ལེགས་པར་འགགས་པ་ཡིས། །
དེ་ནས་ཡན་ལག་བཅུ་གཉིས་འགག །

[Block 1245]
གང་ལ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡང་དག་པར་ཤེས་པ་སྟེ། ཡང་དག་པ་ཇི་ལྟ་བ་མཐོང་བ་དེ་ནམ་ཡང་ཆོས་རྣམས་ཀྱི་རང་བཞིན་དུ་སྒྲོ་མི་འདོགས་ལ། གང་གི་ཚེ་རང་བཞིན་དུ༌[^897]མི་འདོགས་པ་དེའི་ཚེ་འདིའི་མ་རིག་པ་སྤོང་ལ། མ་རིག་པ་སྤངས་པས་འདུ་བྱེད་ཀྱང་མི་སྐྱེ་ལ། ཇི་སྲིད་དུ་སྐྱེ་བ་མེད་པས་རྒས་པ་དང་འཆི་བ་མི་འབྱུང་བའི་བར་དུའོ། །

[Block 1246]
དེ་ལས་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དང་འདུས་བྱས་དང་འདུས་མ་བྱས་ཞི་བས་མྱ་ངན་ལས་འདས་པར་འགྱུར་རོ། །

[Block 1247]
སླར་ཡང་ཐར་པ་འདོད་པས་མ་རིག་པ་སྤོང་བར་འདོད༌[^898]པ་མ་རིག་པ་སྤོང་བར་འདོད་པས་དངོས་པོ་འདི་དག་ཇི་ལྟར་བལྟ་བར་བྱ། སྨྲས་པ། ཐར་པ་འདོད་པ་རྣམས་ཀྱིས་དེ་ཁོ་ན་ཉིད་ལ་བལྟ་བར་བྱ་ལ། དེ་ཁོ་ན་ཉིད་ཀྱང་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ལ། དེ་ཡང་མ་སྐྱེས༌[^899]པའོ། །

[Block 1248]
དེས་ན༌[^900]ཐར་པ་འདོད་པས་འདི་དག་ལ་དངོས་པོར་བལྟ་བར་མི་བྱའོ། །

[Block 1249]
འདིར་སྨྲས་པ། འོ་ན་དེ་ལྟར་ན་འདི་ལྟར་དངོས་པོ་ཐམས་ཅད་མ་མཐོང་ངོ་ཞེས་མི་ནུས་ཏེ། མིག་མ་ཉམས་ཤིང་མིག་བྱེ་བ་དང་ཡུལ་ཕུན་སུམ་ཚོགས་པ་སྣང་བ་དང་བཅས་པའི་སྔོན་པོ་ལ་སོགས་པ་མི་མཐོང་བར་མི་ནུས་སོ། །

[Block 1250]
དེ་བཞིན་དུ་རྣ་བ་ལ་སོགས་པའི་དབང་པོས་ཀྱང་རང་གི་ཡུལ་ཇི་ལྟ་བར་མི་འཛིན་པར་མི་ནུས་སོ། །

[Block 1251]
སྨྲས་པ། གལ་ཏེ་ཡང་དབང་པོ་ལ་ལྟོས་ནས་སྔོན་པོ་ལ་སོགས་པ་མངོན་སུམ་ལ། དེ་ལྟ་ན་ཡང་རིག་པས༌[^901]ཉེ་བར་དཔྱད་པ་ལས་སྐྱེས་པའི་བློའི་མངོན་སུམ་གང་ཞིག་དེ་ཉིད་འཛིན༌[^902]པའི་དབང་པོའི་མངོན་སུམ་པས་གླེངས་པའི༌[^903]ཕྱིར་རོ། །

[Block 1252]
འདི་ལྟར་རབ་རིབ་ཅན་ལ་མི་བདེན་པའི་སྐྲ་དང་སྦྲང་བུ་ལ་སོགས་པ་མངོན་སུམ་དུ་སོ་སོར་སྣང་ལ། དེ་དག་ཀྱང་རིགས་པ་དང་བཅས་པའི་བློའི་མངོན་སུམ་དུ་མེད་ལ། དེ་ནི་བློའི༌[^904]དབང་པོའི་མངོན་སུམ་དུ་ཡང་དེ་དག་གནས་པ་མ་ཡིན་ཏེ། རིགས་པའི་རྗེས་སུ་འབྲང་བའི་བློས་ཡང་དག་པའི་མངོན་སུམ་ཉིད་དུ་མངོན་པར་རློམ་པ་གསལ་བའི་ཕྱིར་རོ། །

[Block 1253]
གལ་ཏེ་དེ་ལྟ་ན་ཡང་དངོས་པོ་དེ་དག༌[^905]ཕྱིན་ཅི་ལོག་གི་ལས་ལས་བྱུང་བས་ཡང་དག་པ་མ་ཡིན་པའི་དོན་ཡོངས་སུ་གཅོད་པ་དབང་པོ་དང་ཡུལ་གྱི༌[^906]གནས་པར་ཡོད་པས་མངོན་སུམ་དུ་འགྱུར་རོ། །

[Block 1254]
དེ་ལྟ་ན་ཡང་རིགས་པས་ཉེ་བར་དཔྱོད་པ་ལ་ཞུགས་པའི་བློས་དེ་དག་གི་བློས༌[^907]མངོན་སུམ་ཉིད་ལྡོག་སྟེ། དེ་ནི་སྟོབས་ཅན་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་སྟེ། དེས་ན་དངོས་པོ་རྣམས་སུ་མངོན་པར་ཞེན་ནས་འཛིན་པའི་ཕྱིར་དང་། དེ་ཁོ་ན༌[^908]འཇུག་པའི་སྒོའི་ཕྱིར་དཔེའི་ཕྲེང་བ་གསུངས་པ།

[Block 1255 [HEADING]]
### ཚིགས་བཅད་རེ་དྲུག་པ། ^1-65-0

[Block 1256 [VERSE]]
དྲི་ཟའི་གྲོང་ཁྱེར་སྒྱུ་མ་དང་། །
སྨིག་རྒྱུ་དབུ་བ་ཆུ་བུར་དང་། །
གཟུགས་བརྙན་སྤྲུལ་པ་རྨི་ལམ་དང་། །
མགལ་མེ་དང་མཚུངས་འདུ་བྱེད་རྣམས། །

[Block 1257]
ཇི་ལྟར་དྲི་ཟའི་གྲོང་ཁྱེར་ལ་སོགས་པའི་དོན་ཏོ།[^909] །འདི་དག་ཉིད་རང་གི་རྒྱུ་དང་རྐྱེན་ཇི་ལྟ་བ་ལས་འབྱུང་ན་ཡང་། གྲོང་ཁྱེར་ལ་སོགས་པའི་རང་བཞིན་གྱིས་སྟོང་པ་གྲོང་ཁྱེར་ལ་སོགས་པ་ཉིད་དུ་སྣང་ལ། དེ་བཞིན་དུ་འདི་ལྟར་གཟུགས་དང་ཚོར་བ་ལ་སོགས་པའི་དངོས་པོ་ཡང་གཟུགས་དང་ཚོར་བ་ལ་སོགས་པའི་རང་བཞིན་གྱིས་སྟོང་པ་ཉིད་སྣང་བ་ལ། གཟུགས་དང་ཚོར་བ་ལ་སོགས་པ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 1258]
ཡང་དཔེ་གཅིག་ཉིད་ཀྱི༌[^910]རང་བཞིན་མེད་པ་ཉིད་རྟོགས་པར་འགྱུར་ན། དཔེ་མང་པོ་ཉིད་ཉེ་བར་བསྡུས་པ་ལ་དོན་མེད་དོ་ཞེ་ན། འདི་དག་དེ་ལྟར་མ་ཡིན་ཏེ། རང་བཞིན་མེད་པའི་དོན་ལ་འཁོར་བ་ཐོག་མ་མེད་པ་ནས་མ་གོམས་པའི་འཇིག་རྟེན་པ་དེ་དག་དཔེ་དུ་མས་འཇིག་རྟེན་པའི་སེམས་ལ་ཕེབས་པས། དེ་ཁོ་ན་ཉིད་ལ་ངེས་པ་སྐྱེད་པར༌[^911]འགྱུར་རོ། །

[Block 1259]
ཇི་སྐད་དུ།

[Block 1260 [VERSE]]
[^912]རེ་ཞིག་ཕུང་པོ་མི་གཙང་བ། །
རགས་པ་མངོན་སུམ་སྤྱོད་ཡུལ་ཏེ། །
རྟག་ཏུ་མཐོང་བར་གྱུར་ན་ཡང་། །
གང་ཚེ་སེམས་ནི་མི་གནས་པ། །

[Block 1261 [VERSE]]
དེ་ཚེ་ཤིན་ཏུ༌[^913]ཕྲ་ཞིང་ཟབ། །
དམ་ཆོས་འདི་ནི་གནས་མེད་པ། །
མངོན་སུམ་མིན་པ་ཇི་ལྟར་དུ། །
སེམས་ལ་བདེ་བླག་རྟོགས་པར༌[^914]འགྱུར། །

[Block 1262]
ཞེས་སོ། །

[Block 1263]
དེའི་སེམས་ལ་བདེ་བླག་ཏུ་འཇུག་པའི་ཕྱིར་དཔེ་མང་པོ་བསྟན་པ་ནི་རིགས་པ་ཉིད་དོ་ཞེས་བྱའོ། །

[Block 1264]
གཞན་ཡང་དཔེ་མང་པོ་ཉེ་བར་བཀོད་པས་འགའ་ཞིག་འགའ་ཞིག་ལ་ཤིན་ཏུ་ངེས་པར་འགྱུར་རོ་ཞེས་བྱ་སྟེ། དེ་ལ་དཔེ་དེས༌[^915]དེའི་དོན་བདེ་བླག་ཏུ་བདག་ཉིད་ཀྱིས་ཁོང་དུ་ཆུད་པས་དེས་ན་དཔེ་མང་པོ་ཉེ་བར་བསྡུ་བ་རིགས་པ་ཉིད་དོ། །

[Block 1265]
ཡང་ན་དངོས་པོར་འཛིན་པ་ཐ་དད་པས་དཔེ་ཐ་དད་པའོ། །
--- END BLOCKS ---
