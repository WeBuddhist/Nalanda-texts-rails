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
[Block 1226]
དེ་ལ་མིང་བསྟན་པ་ནི༌[^1182]མདོ་སྡེ་བཅུ་གཉིས་ཀྱི་མིང་བསྟན་པའོ། །

[Block 1227 [HEADING]]
###### **ཁྱད་པར་བསྟན་པ།** ^4-2-11-1-1-2-1-1-3-3-0

[Block 1228]
དེ་ལ་ཁྱད་པར་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ་རང་བཞིན་གྱི་ཁྱད་པར་དང་། བསྟན་པའི་ཁྱད་པར་རོ། །

[Block 1229 [HEADING]]
###### **རང་བཞིན་གྱི་ཁྱད་པར།** ^4-2-11-1-1-2-1-1-3-3-1-0

[Block 1230]
རང་བཞིན་གྱི་ཁྱད་པར་ནི་དབྱངས་ཀྱིས་བསྙད་པའི་ནང་ན་ཚིགས་སུ་བཅད་པ་མེད་ལ། ཚིགས་སུ་བཅད་པའི་ནང་ན་དབྱངས་ཀྱིས་བསྙད་པ་མེད་དེ་སྔ་ཕྱི་དང་། རྐྱང་པ་དང་བཟླས་པ་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 1231]
མདོ་སྡེ་དག་ལས་ཐོག་མ་འདི་སྐད་བདག་གིས་ཐོས་པ་ནས་ཐ་མ་རྗེས་སུ་སྤྱད་པའི་བར་དུ་མདོ༌[^1183]སྡེ་ཞེས་སྨོས་པས་སྡེ་བཅུ་གཉིས་ཀྱང་བསྡུས་ཏེ། མདོ༌[^1184]སྡེ་ནི་ཚིག་རྐྱང་པ་འབའ་ཞིག་ལ་བྱ་བས་དབྱངས་ཀྱིས་བསྙད་པ་དང་ཚིགས་སུ་བཅད་པ་མ་གཏོགས་པར་སྡེ་བདུན་པོ་ཀུན་ལ་བཅུ་གཉིས་ཚང་བར་ཡོད་པར་ཤེས་པར་བྱའོ། །

[Block 1232 [HEADING]]
###### **བསྟན་པའི་ཁྱད་པར།** ^4-2-11-1-1-2-1-1-3-3-2-0

[Block 1233]
བསྟན་པའི་ཁྱད་པར་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཆེན་པོ་ལ་ཚང་བར་ཡོད་ལ་ཐེག་པ་ཆུང་ངུ་ལ་དགུ་ལས་མེད་དེ། འདིའི་སྐབས་སུ་ཐེག་པ་ཆུང་ངུ་སྨོས་པས་ལུང་བསྟན་པ་དང་། ཆེད་དུ་བརྗོད་པ་དང་ཤིན་ཏུ་རྒྱས་པ་དང་གསུམ་མ་སྨོས་ཏེ། འདི་ནི་ཁྱད་པར་བསྟན་པའོ། །

[Block 1234 [HEADING]]
###### **དབང་པོ་ཇི་བཞིན་དུ་བཤད་པ།** ^4-2-11-1-1-2-1-2-0

[Block 1235]
མདོ་ལས་མི་མཁས་ངན་ལ་ཆགས་པར་གང་གྱུར༌[^1185]ཞེས་པ་ནས་དེ་ལས༌[^1186]མྱ་ངན་ལས༌[^1187]འདས་པ་ཉེ་བར་བསྟན་ཞེས་པའི་བར་དུ་ཚིག་ཕྱེད་དང་གཉིས་ཀྱིས་དབང་པོ་ཇི་ལྟ་བ་བཞིན་དུ་རྟོགས་པར༌[^1188]དཀའ་བ་བསྟན་པ་སྟེ། འདི་ལ་རྣམ་པ་ལྔའོ། །

[Block 1236]
དབང་པོ་རྟུལ་བས་གོ་དཀའ་བ་དང་ཆུང་ངུ་ལ་མོས་ཤིང་ཆེན་པོས་སྐྲག་པ་དང་འཁོར་བ་ལ་ཆགས་ཤིང་འཇིག་རྟེན་ལས་འདས་པ་ལ་མ་དད་པ་དང་། སྐལ་བ་ཡོད་ཀྱང་མི་སྤྱོད་པ་དང་། སྡུག་བསྔལ་མང་པོས་མངོན་དུ་གཟིར་བ་སྟེ།[^1189] དེ་དག་ལ་མྱ་ངན་ལས་འདས་པ་ཉེ་བར་བསྟན་པའོ། །

[Block 1237]
དབང་པོ་རྟུལ་ཞིང་མི་མཁས་ལ་ངན་ཏེ་འཁོར་བ་ལ་ཆགས་པས་སངས་རྒྱས་རྣམས་དང་ཕྲད་ཀྱང་ཐེག་པ་ཆེན་པོའི་ཆོས་ཟབ་མོ་མི་སྤྱོད་དེ༌[^1190]སྡིག་པ་མི་དགེ་བ༌[^1191]སྤྱོད་པས་སྡུག་བསྔལ་མྱོང་བར་འགྱུར༌[^1192]ཏེ། སྡུག་བསྔལ་ཐར་བར་བྱ་བའི་ཕྱིར་ཐེག་པ་གཉིས་ཀྱི་མྱ་ངན་ལས་འདས་པ་བསྟན་ཏོ། །

[Block 1238]
མདོ་ལས།

[Block 1239 [HEADING]]
###### **གནས་པར་བྱ་བ།** ^4-2-11-1-1-2-2-0

[Block 1240]
དེ་ལྟར་རང་བྱུང་བ༌[^1193]ནི་ཐབས་མཛད་པ། །ཞེས་པ་ནས་ཁྱེད་ཅག་སངས་རྒྱས་སུ་ཡང་འགྲུབ་པོ་ཞེས་པའི་བར་དུ་འདི་མན་ཆད་ཚིག་ཕྱེད་དང་བརྒྱད་ཀྱིས་གནས་པར་བྱ་བ་བསྟན་པ་སྟེ། དེ་ལ་ཚིག་གཅིག་ནི་སྤྱིར་བསྟན་ཏོ། །

[Block 1241]
ཚིག་གཅིག་ནི་བཤད་པའོ། །

[Block 1242]
ཚིག་བཞིས༌[^1194]བསྡུས་པའོ། །

[Block 1243]
ཚིག་གཅིག་ནི་གནས་པར་བསྐུལ་བའོ། །

[Block 1244 [HEADING]]
###### **སྤྱིར་བསྟན་པ།** ^4-2-11-1-1-2-2-1-0

[Block 1245]
འདི་ནི་སྤྱིར་བསྟན་པ་སྟེ། གཉིས་ཐབས་ཙམ་དུ་བསྟན་ནས་མཐར་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ཐེག་པ་གཅིག་ལ་འཇུག་པ་བསྟན་པའོ། །

[Block 1246 [HEADING]]
###### **བཤད་པ།** ^4-2-11-1-1-2-2-2-0

[Block 1247]
མདོ་ལས་ཅིའི་ཕྱིར་ཞེ་ན་སྐྱོབ་པ༌[^1195]དུས་ལ་སྡོད་ཅེས་པ་ནས་ཡང་དག་གདོན་མི་ཟ་བ༌[^1196]བཤད་དོ་ཞེས་པའི་བར་དུ་ནི་འདིར་སྤྱིར་བསྟན་པ་ལས་དམིགས་ཏེ། སྔོན་ཁྱོད་ཀྱི་དབང་པོ་མ་སྨིན་པས་ཐེག་པ་ཆེན་པོ་མི་རྟོགས་ཏེ་བསྟན་པའི་སྣོད་དུ་མ་གྱུར་ཏོ། །

[Block 1248]
ད་ནི་དབང་པོ་སྨིན་པས་དུས་ལ་བབ་སྟེ་གདོན་མི་ཟ་བའི་དོན་བཤད་དོ་ཞེས་བསྟན་ཏོ། །

[Block 1249]
མདོ་ལས།

[Block 1250 [HEADING]]
###### **བསྡུས་པ།** ^4-2-11-1-1-2-2-3-0

[Block 1251]
ང་ཡིས༌[^1197]བསྟན་པ་སྡེ་དགུ་དེ་རྣམས་ཀྱང་། །ཞེས་པ་ནས། །རབ་ཏུ་གཞུག་པའི་ཕྱིར་ནི་ངས་བཤད་དོ། །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིག་ཕྱེད་དང་ལྔས་བསྡུས་པ་བསྟན་པ་སྟེ། དེ་ལ་ཡང་གསུམ་དུ་དབྱེའོ། །

[Block 1252]
ཚིག་གཅིག་གིས་ནི་ཆོས་ཆུང་ངུ་ཡང་དག་པ་མ་ཡིན་ཏེ། ཆེན་པོ་ནི་ཡང་དག་པའོ་ཞེས་བསྟན་པའོ།[^1198] །ཚིག་གཅིག་གིས་ནི་ཆོས་ཆེན་པོ་དམ་པར་བསྟན་ཏེ་སྐྱེས་བུ་དམ་པ་ལ་བཤད་པ་བསྟན་པའོ། །

[Block 1253]
ཚིག་གཉིས་ཀྱིས་ནི་ཆོས་དང་གང་ཟག་བསྟན་པ་སྟེ། འདི་ནི་ཐོག་མ་སེམས་བསྐྱེད་པའི་མཐུ་སྟོབས་ཇི་ལྟ་བ་བཞིན་དུ་བསྟན་པ་སྡེ་དགུ་བཤད་དེ། མཐར་ཕྱིན་པ་མ་ཡིན་པས་ཆེན་པོ་ལ་རབ་ཏུ་གཞུག་གོ་ཞེས་བསྟན་ཏོ། །

[Block 1254]
མདོ་ལས།

[Block 1255]
འདི་ལྟར་རྟག་ཏུ་རྣམ་པར་དག་འགྱུར་བ། །ཞེས་པ་ནས། །དེ་ལ་ཤིན་ཏུ་རྒྱས་པའི་མདོ་སྡེ་བཤད། །ཅེས་པའི་བར་དུ་ནི་སྐབས་འདིར་ཆོས་ཆེན་པོ་དམ་པ་སྐྱེས་བུ་དམ་པ་ལ་བཤད་པ་བསྟན་ཏེ། མདོར་ན་བྱང་ཆུབ་སེམས་དཔའི་ཆོས་སྤྱོད་པ་ཐམས་ཅད་ལ་སངས་རྒྱས་ཀྱི་སྲས་ཞེས་བྱའོ། །

[Block 1256]
སངས་རྒྱས་ཀྱི་སྲས་ཀྱང་ཡོན་ཏན་ལྔ་དང་ལྡན་བའོ། །

[Block 1257]
ལྔ་གང་ཞེ་ན་བསམ་པ་རྣམ་པར་དག་པ་སྟེ་ཐེག་པ་ཆེན་པོའི་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་འབའ་ཞིག་ཚོལ་བ་དང་། མཉན༌[^1199]ངེས་པ་སྟེ་ངེས་པའི་སེམས་ཀྱིས༌[^1200]ཐེག་པ་ཆེན་པོ་ལ་བརྩོན་པ་དང་དབང་པོ་རྣོ་བ་སྟེ་སྡུག་བསྔལ༌[^1201]ལས་འདོན་ཅིང་བདེ་བ་བྱིན་པ༌[^1202]དང་། ཚད་མེད་པ་སྟེ་སངས་རྒྱས་མང་པོ་ལ་བསྙེན་བཀུར་བྱེད་པ་དང་། ཤིན་ཏུ་ཟབ་མོ་སྤྱོད་པ་སྟེ་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ལ་ནན་ཏན་བྱེད་པའོ། །

[Block 1258]
དེ་ཡང་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་སྟེ། ཆོས་བཅུ་པོ་འདི་དང་ལྡན་ན༌[^1203]བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་ཞེས་བྱའོ། །

[Block 1259]
གང་ཞེ་ན་དགེ་བའི་བཤེས་གཉེན་ལ་བསྙེན་བཀུར་བྱེད་པ་དང་། སངས་རྒྱས་མང་པོ་ལ་བྱ་བ་བྱེད་པ་དང་། དགེ་བའི་རྩ་བ་སྤྱོད་པ་དང་། ཆོས་མཆོག་ཚོལ་བ་དང་། སེམས་མཉེན༌[^1204]ཞིང་ངེས་པ་དང་། སྡུག་བསྔལ་ལ་བཟོད་པ་དང་། སྙིང་རྗེ་ཤས་ཆེ་བ་དང་། བསམ་པ་དག་པས་སྙོམས་པ་དང་། ཐེག་པ་ཆེན་པོ་ལ་མོས་པ་དང་། སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ཚོལ་བ་དང་བཅུ་སྟེ། ཡོན་ཏན་འདི་དག་དང་ལྡན་ན་སངས་རྒྱས་ཀྱི་སྲས་ཞེས་བྱ་སྟེ་ཐེག་པ་ཆེན་པོ་སྟོན་པར་འགྱུར་རོ། །

[Block 1260]
མདོ་ལས།

[Block 1261]
འདི་ལྟར་དེ་དག་བསམ་པ་རྫོགས་པ་དང་། །ཞེས་པ་ནས། །ཤིན་ཏུ་རྒྱས་པའི་མདོ་སྡེ་རབ་ཏུ་བཤད། །ཅེས་པའི༌[^1205]བར་དུ་ནི་ཡོན་ཏན་ལྔ་དང་ལྡན་པའི་གང་ཟག་མ་འོངས་པའི་དུས་སུ་འཚང་རྒྱ་བར་འགྱུར་རོ། །

[Block 1262]
དེ་ཡང་སངས་རྒྱས་དྲན་པའི་བསམ་པ་རྫོགས་པ་དང་། རྣམ་པར་དག་པའི་ཚུལ་ཁྲིམས་དང་ལྡན་པའོ། །

[Block 1263]
སངས་རྒྱས་དྲན་པ་ལ་རྣམ་པ་གཉིས་ཏེ་སེམས་ཀྱིས༌[^1206]དྲན་པ་དང་ཚིག་གིས་བརྗོད་པའོ། །

[Block 1264]
ཚུལ་ཁྲིམས་དང་ལྡན་པ་བསླབ་པ་གསུམ་རྫོགས་པ༌[^1207]ལ་ལུང་སྟོན་པར་འགྱུར་ཏེ། དེ་དག་ཐོས་ནས་ཤིན་ཏུ་དགའ་བར་འགྱུར་ཞེས་སྨོས་སོ། །

[Block 1265]
མདོ་ལས།
--- END BLOCKS ---
