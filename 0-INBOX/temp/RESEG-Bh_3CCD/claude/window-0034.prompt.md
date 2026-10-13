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
[Block 1191]
རྒྱུ་འབྲས་ཀྱི་འབྲེལ་པས་ཀྱང་དབང་ཕྱུག་ལ་ནུས་པ་སྐྱེས་པས་དབང་ཕྱུག་འགོག་པར༌[^835]འགྱུར་རོ། །

[Block 1192]
དེ་ཡང་འདོད་པ་མ་ཡིན་ཏེ། དེ་རྟག༌[^836]པའི་ཕྱིར་རོ། །

[Block 1193]
རྒྱུ་རྣམས་ནི་ངེས་པར་འབྲས་བུ་དང་ལྡན་པར་མི་འགྱུར་ཞེས་ནུས་པ་ཁོ་ན་རྒྱུ་རུ་འགལ་བ་མེད་དོ། །

[Block 1194]
དེ་བས་ན་དབང་ཕྱུག་བྱེད་པ་པོར་མི་འགྱུར་རོ། །

[Block 1195]
འདུ་བའི་འབྲེལ་པས་དེའི་བདག་ཉིད་དུ་འཐད་ཅེ་ན། འདུ་བ་ཞེས་བྱ་བ་ཅི་ཡིན་ན་སྣམ་བུ་དང་སྣལ་མ་ཐ་དད་པ་དག་ལ་ཡང་འདིར་སྣལ་མ་ལ་སྣམ་བུ་ཞེས་ཐ་སྙད་ཡིན་ཞེ་ན། འོ་ན་ནི་སྣལ་མ་ལས༌[^837]མ་གཏོགས་པའི་སྣམ་བུ་གང་ཞིག་ཡོད། གང་ལ་ལྟོས་པས་དེ་དག་གི་འདུ་བའི་འབྲེལ་པར་འགྱུར། ཆུ༌[^838]དང་ཞེང་གི་བདག་ཉིད་ཁེབས་པ་ལ་སོགས་པའི་བྱ་བ་བྱེད་པ་སྣམ་བུ་ཡིན་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། དེའི་ཚེ་དེ་དག་སྣལ་མ་མ་ཡིན་གྱི་སྣམ་བུ་གཅིག་པུ་ཁོ་ན་དོན་གྱི་བྱ་བ་བྱེད་པས་སོ། །

[Block 1196]
གང་དོན་གྱི་བྱ་བ་བྱེད་པ་དེ་ཉིད་བདེན་པའི་དོན་ནོ། །

[Block 1197]
གལ་ཏེ་སྣམ་བུ་མ་ཡིན་ན་དེའི་ཚེ་སྣལ་མ་མ་ཡིན་པས་འབྲེལ་པ་མེད་དེ། གཉིས་ལ་འབྲེལ་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1198]
ཡང་ན་རྒྱུ་སྤུན་དང་སྣམ་བུ་རང་གི་བདག་ཉིད་དུ་གནས་པ་ཡིན་ན་དེའི་ཚེ། འབྲེལ་པ་མེད་དེ་རང་དབང་ཡིན་པས་སོ། །

[Block 1199]
ཇི་སྐད་དུ།

[Block 1200 [VERSE]]
གང་ཕྱིར་འབྲེལ་པ་གཞན་དབང་ནི། །
གྲུབ་པས་གཞན་དབང་གང་ཞིག་ཡོད། །
དེ་བས་དངོས་པོ་ཐམས་ཅད་ཀྱི། །
དེ་ཉིད་ཀྱིས་ནི་འབྲེལ་པ་མེད། །

[Block 1201]
ཅེས་འབྱུང་ངོ་། །གལ་ཏེ་འདུ་བའི་མཚན་ཉིད་ཀྱི་འབྲེལ་པས་སྣལ་མ་དང་སྣམ་བུའི་འབྲེལ་པ་ཡིན་ན་དེའི་ཚེ་འདུ་བ་ལ་གཞན་འདུ་བ་དང་དེ་ལ་ཡང་གཞན་དང་གཞན༌[^839]ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1202]
གལ་ཏེ་ལྟོས་པ་མེད་ན་དེའི་ཚེ་འབྲེལ་པ་མེད་པ་དེས་གང་གི་འབྲེལ་པ་བྱེད། དེ་བས་ན་སྣལ་མ་རྣམས་དང་སྣམ་བུ་དག༌[^840]ཐ་དད་པ་ཁོ་ནར་སྣང་བར་གྱུར༌[^841]ན། དེ་ལྟར་ཡང་མ་མཐོང་སྟེ། འདིར་སྣལ་མ་ལ་སྣམ་བུ་ཡོད་ཅེས་སྒྲ་དང་རྣམ་པར་རྟོག་པ་ཙམ་ཡིན་གྱི་ཚད་མ་མ་ཡིན་ནོ། །

[Block 1203]
དེ་བས་ན་དངོས་པོ་རྣམ་པར་དཔྱོད་པ་ན་སྣམ་བུ་ཞེས་བྱ་བ་མེད་དོ། །

[Block 1204]
སྣལ་མ་ཁོ་ན་ནི་ཐགས་མཁན་གྱི་ཡོངས་སུ་ལས་ཀྱི༌[^842]ནུས་པས་གནས་སྐབས་དེ་ལྟ་བུ་ཐོབ་པ་གང་གིས་ཁེབས་པ་ལ་སོགས་པའི་བྱ་བ་བྱེད་པའོ། །

[Block 1205]
བློ་དམན་པས་སྣམ་བུ་ཞེས་རྟོག་སྟེ། བུམ་པ་ཆག་པ་བཞིན་ནོ། །

[Block 1206]
དཔེར་ན་རྫ་མཁན་གྱི་སྤྲུལ་པའི་དུས་སུ་འཇིག་པའི་ཆོས་ཅན་ཁོ་ན་བུམ་པ་སྐྱེས་པ་དེ་འཇིག་པར་བྱེད་པ་རྒྱུ་གཞན་མེད་དོ། །

[Block 1207]
ཐོ་བ་ལ་སོགས་པ་ཕྲད་པའི་དུས་སུ་བུམ་པ་ཆག་གོ་ཞེས་འཇིག་རྟེན་པས་སེམས་སོ། །

[Block 1208]
བུམ་པ་དེ་འཇིག་རྟེན་པ་མ་ཡིན་ཏེ།

[Block 1209]
དང་པོ་ཁོ་ན་དེ༌[^843]འཇིག་པས་སོ། །

[Block 1210]
གྱོ་མོ་ལ་སོགས་པའི་འབྲས་བུའི་གནས་སྐབས་གཞན་སྐྱེས་པ་ཉིད་དོ། །

[Block 1211]
དེ་བཞིན་དུ་སྣལ་མ་རྣམས་ནི་ཁེབས་པ་ལ་སོགས་པའི་ལས་ཅན་ལ་སྣམ་བུར༌[^844]བཏགས་པའོ། །

[Block 1212]
དེའི་ཕྱིར་འདུ་བའི་འབྲེལ་པ་མེད་པས་དབང་ཕྱུག་དང་ནུས་པ་གཅིག་པ་མ་ཡིན་ནོ། །

[Block 1213]
གལ་ཏེ་ནུས་པ་དེས་ནུས་པ་གཞན་ལ་ལྟོས་པའམ་མི་ལྟོས་པ་ཡིན་དྲང་།[^845] གལ་ཏེ་ལྟོས་པར་བྱེད་ན་དེའི་ཚེ་དེས་ཀྱང་གཞན་ལ་ལྟོས་པ་དགོས་ཞེས་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1214]
ཡང་ན་ལྟོས་པ་མེད་ན་ནུས་པ་མེད་པ༌[^846]ནུས་པ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 1215]
དེ་བས་ན་སྐྱེད་པར༌[^847]མི་བྱེད་དོ། །

[Block 1216]
ནུས་པ་དང་དབང་ཕྱུག་ཐ་དད་པས་སྐྱོན་སྔ་མ་བཞིན་ནོ། །

[Block 1217]
དེ་ཉིད་ཀྱིས༌[^848]ན་ཀུན་ཤེས་པ་ཉིད༌[^849]ཀྱང་མི་རིགས་ཏེ་དེ་ལ་ཐམས་ཅད་ཤེས་པ་ཉིད༌[^850]གང་ཡིན་ཞེ་ན། ཐམས་ཅད་ཤེས་པ་ན་ཐམས་ཅད་ཤེས་པ་ཞེ་ན། འདས་པ་ལ་སོགས་པའི་དུས་གསུམ་ན་གནས་པའི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་ཀྱི་སྤྱོད་པ་ཤེས་པའམ། སེམས་ཀྱི་རང་བཞིན་ཤེས་ཤེ༌[^851]ན། གལ་ཏེ་འདས་པ་ལ་སོགས་པ་ཤེས་ན་དེའི་ཚེ་ཁྱུ་མཆོག་དང་འཕེལ་བ་ལ་སོགས་པས་བྱས་པའི་སྐར་མའི་བསྟན་བཅོས་ཡོངས་སུ་ཤེས་པས་ཕ་རོལ་པོའི་སེམས་ཀྱི་སྤྱོད་པ་དང་དུས་གསུམ་གྱི་མཚན་ཉིད་བདག་ཅག་གིས་ཀྱང་ཤེས་པས་ཐམས་ཅད་ཤེས་པར༌[^852]ཐལ་བར་འགྱུར་རོ། །

[Block 1218]
ཡང་ན་སེམས་ཀྱི་ངོ་བོ་ཉིད་ཤེས་པ་ཡིན་ན་བདག་ཡོད་པའམ་མེད་པར་ཤེས་ཤེ་ན། བདག་མེད་པར༌[^853]ནི་མི་ཤེས་ཏེ། དེ་ལྟར་མི་འདོད་པའི་ཕྱིར་རོ། །

[Block 1219]
བདག་ཡོད་པར་ཤེས་ཤེ༌[^854]ན། ངོ་མི་ཤེས་ཏེ་བདག་སྔོན་དུ་བཀག་པའི་ཕྱིར་རོ། །

[Block 1220]
དངོས་པོ་རྣམས་ཀྱི༌[^855]བདག་མེད་པ་ཁོ་ན་དོན་དམ་པ་ཡིན་ཏེ། དེ་ཡང་ལེའུ་གཉིས་པ་ལས་འཆད་པར་འགྱུར་ཏེ་དེའི་ཕྱིར་དེ་ནི་ཐམས་ཅད་ཤེས་པ་མ་ཡིན་ནོ། །

[Block 1221]
བྱེད་པ་ཡིན་དུ་འཇུག་ན་དེས་ནི་ཅིག་ཅར་དུ་ཐམས་ཅད་ཅིའི་ཕྱིར་སྐྱེ་བ་དང་འཇིག་པར་མི་བྱེད་པར་རིམ་གྱིས་པའི་ཕྱིར་མི་རྟག་པའོ། །

[Block 1222]
ལྟོས་པ་མེད་པའི་དངོས་པོས་ཅིག་ཅར་དང་རིམ་གྱིས་དོན་གྱི་བྱ་བ་མ་མཐོང་བས་ནམ་མཁའ་བཞིན་དུ༌[^856]དབང་ཕྱུག་མེད་དོ་ཞེས༌[^857]དབང་ཕྱུག་འདོད་པ་ལ་ལན་ནོ། །

[Block 1223 [HEADING]]
###### **དཔྱོད་པ་པ།** ^1-5-3-3-1-6-0

[Block 1224]
སྤྱོད་པ༌[^858]ལ་ཡང༌[^859]རྣམ་པ་གཉིས་ཏེ། བྱ་བའི་ཕྱོགས་ལ་གནས་པ་དང་། ཡེ་ཤེས་ཀྱི་ཕྱོགས་ལ་གནས་པའོ། །

[Block 1225]
དེ་ལ་བྱ་བའི་ཕྱོགས་ལ་གནས་པ་ལ་ཚད་མ་བརྒྱད་དེ། ཇི་སྐད་དུ།

[Block 1226 [VERSE]]
མངོན་སུམ་དང་ནི་རྗེས་དཔག༌[^860]དང་། །
སྒྲ་ལས་བྱུང་བ་དཔེ་དང་བཅས། །
དོན་གྱི་ཤུགས་དང་མེད་ཉིད་དང་། །
སྲིད་དང་ཡོད་སྙམ་དེ་བཞིན་ཏེ། །

[Block 1227]
ཞེས་བཤད་པས་སོ། །

[Block 1228]
ཚད་མ་དེ་རྣམས་ཀྱིས་དངོས་པོ་རྣམས་ལ་སྤྱི་དང་ཁྱད་པར་དུ་འཇོག་པར་བྱེད་དོ། །

[Block 1229]
མཆོད་སྦྱིན་ལ་སོགས་པ་སྲོག༌[^861]གཅོད་པ་དང་བཅས་པས་ཀྱང་མཐོ་རིས་དང་ཐར་པ་དག་འདོད་དོ། །

[Block 1230]
དེ་ཡང་མི་རིགས་ཏེ། དེ་རྣམས་ཀྱི་རིགས་སམ། གསལ་བའམ་སྤྱི༌[^862]དང་ལྡན་པའམ་དེའི་འབྲེལ་པའི་སྒྲ་དོན་ཡིན་ཞེ་ན། དེ་ལ་སྤྱི་ཞེས་བྱ་བ་གང་ཡང་དངོས་པོ་ལས་གུད༌[^863]ན་མེད་དེ་དམིགས་པའི་མཚན་ཉིད་དང་ལྡན་པ༌[^864]དེ་མི༌[^865]དམིགས་པའི་ཕྱིར་བུམ་པས་དབེན་པའི་ས་ཕྱོགས་བཞིན་ནོ།[^866] །
--- END BLOCKS ---
