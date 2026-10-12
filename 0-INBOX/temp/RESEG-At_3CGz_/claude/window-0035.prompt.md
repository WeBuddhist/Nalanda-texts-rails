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
ཆོས་སྤངས་པའི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ནི་འཕགས་པ་རྣམ་པར་འཐག་པའི་མདོ་ལས་འདི་སྐད་དུ་ཆོས་ལ་ལ་ནི་བཟང་ཞེས་པ་དང་། ཆོས་ལ་ལ་ངན་ནོ་ཞེས་ཟེར་ན་ཆོས་སྤངས་པའོ་ཞེས་པ་ལ་སོགས་པ་ཆོས་དུ་མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1227]
བླ་མ་དགེ་སློང་བསོད་སྙོམས་པའི་ཞལ་ནས་ཀྱང་།

[Block 1228 [VERSE]]
དེའི་ཕྱིར་གསང་སྔགས་ཐེག་པ་ལ། །
བདུད་ཀྱིས་སྨྲས་ཞེས་བརྙས་མི་བྱ། །
ཐེག་པ་ཀུན་ལ་སྤངས་པ༌[^683]ཡང་། །
འདི་གནས་ཕྱག་རྒྱ་ཆེན་པོ་ཐོབ། །

[Block 1229]
ཅེས་གསུངས་སོ། །

[Block 1230]
དེ་ལྟ་བུའི་གང་ཟག་ནི་སྙིང་རྗེའི་སེམས་ཀྱིས༌[^684]རྗེས་སུ་གཟུང་བར་བྱའོ། །

[Block 1231]
སྐུར་པ་འདེབས་པ་དེ་ཡང་གཉིས་ཏེ། ཆོས་ལ་སྐུར་པ་འདེབས་པ་དང་། གང་ཟག་ལ་སྐུར་པ་འདེབས་པའོ། །

[Block 1232 [HEADING]]
##### ཆོས་ལ་སྐུར་པ་འདེབས་པ། ^10-1-2-1-0

[Block 1233]
དེ་ལ་ཆོས་ལ་སྐུར་པ་འདེབས་པར་མི་བྱ་སྟེ། འཕགས་པ་འོད་སྲུངས་ཀྱིས་ཞུས་པ་ལས་འདི་སྐད་དུ། ཆོས་ཟབ་མོ་གང་དག་བློས་མི་རྟོགས་པ་དེ་ལ་སངས་རྒྱས་ཀྱི་བྱང་ཆུབ་ནི་མཐའ་ཡས་ཤིང་སེམས་ཅན་མོས་པ་ཐ་དད་པ་རྣམས་ལ་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་ཆོས༌[^685]བསྟན་པ་ལ་འཇུག་སྟེ། དེ་བཞིན་གཤེགས་པ་ཉིད་ཀྱིས་མཁྱེན་གྱི༌[^686]བདག་གིས་ནི་མི་ཤེས་ཏེ། དེ་བཞིན་གཤེགས་པས་མངོན་སུམ་མོ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^687]གསུངས་ཏེ། མདོ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 1234]
གཞན་ཡང་མདོ་དང་རྒྱུད་ཐམས་ཅད་དུ་དོན་འདི་བདག༌[^688]གིས་མཐོང་ངོ་། །

[Block 1235 [HEADING]]
##### གང་ཟག་ལ་སྐུར་པ་འདེབས་པ། ^10-1-2-2-0

[Block 1236]
གང་ཟག་ལ་ཡང་སྐུར་པ་གདབ་པར་མི་བྱ་སྟེ། འཕགས་པ་ལྷག་པའི་བསམ་པ་བསྐུལ་བ༌[^689]དང་། འཕགས་པ་ཆོས་ཐམས་ཅད་འབྱུང་བ་མེད་པར་བསྟན་པ་དག་ལས་ངའམ་ང་དང་འདྲ་བ་མ་གཏོགས་པར་གང་ཟག་གིས་གང་ཟག་གི༌[^690]ཚོད་གཟུང་བར༌[^691]མི་བྱ་སྟེ་ཉམས་པར་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 1237]
དེའི་ཉེས་པ་ནི་མདོ་ལས་གཞན་ཡང་མང་དུ་མཐོང་ངོ་། །དང་པོའི་སངས་རྒྱས་རྒྱུད་ཆེན་ལས། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྐང་པ་བཅུ་གཉིས་ཀྱི་དོན་བདག་གིས་བདག་གི་བླ་མར་གྱུར་པ་དགེ་སློང་བསོད་སྙོམས་པ་དང༌[^692]གསེར་གླིང་པའི་གདམས་ངག་ལ་བརྟེན་པ་ཡིན་ཏེ། བླ་མའི་ཞལ་ནས་དབང་བསྐུར་བ་ངེས་པར་བསྟན་པ་ཞེས་བྱ་བ་ལས་འདི་སྐད་དུ། དེ་ལ་དབང་ནི་རྣམ་པ་གཉིས་ཏེ། ཁྱིམ་པའི་ཕྱོགས་ལ་བརྟེན་པ་དང་།

[Block 1238 [VERSE]]
ཚངས་པར་སྤྱོད་པའི་ཕྱོགས་ལ་བརྟེན་པའོ། །
ཁྱིམ་པའི་ཕྱོགས་ལ་བརྟེན་པ་གང་ཞེ་ན།
ཇི་སྙེད་རྒྱུད་ལས་གསུངས་པ་ཐམས་ཅད་དོ། །

[Block 1239]
ཚངས་པར་སྤྱོད་པའི་ཕྱོགས་ལ་བརྟེན་པ༌[^693]གང་ཞེ་ན། དེ་དག་ཉིད་ལས་གསང་བ་དང་། ཤེས་རབ་ཡེ་ཤེས་སྤངས་པའོ། །

[Block 1240]
དེ༌[^694]ཅིའི་ཕྱིར་དེ་གཉིས་སྤངས་ཤེ་ན། འདི་ལྟར་སངས་རྒྱས་ཀྱི་ཆོས་ལ་བརྟེན་ནས་དགེ་བ་ཇི་སྙེད་ཅིག་འབྱུང་བ་དེ་དག་ཐམས་ཅད་ནི་བསྟན་པ་གནས་པ་ལས་འབྱུང་བ་ཡིན་ལ། བསྟན་པ་གནས་པ་ཡང་ཚངས་པར་སྤྱོད་པ་ཁོ༌[^695]ལ་ལྟོས་ཤིང་། དབང་བསྐུར་བ་གཉིས་ནི་ཚངས་པར་སྤྱོད་པའི་མི་མཐུན་པའི་གནས་སུ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1241]
དེ་བས་ན་དབང་བསྐུར་བ་གཉིས་ནི་ཚངས་པར་སྤྱོད་པ་ཟད་པར་བྱེད་པ་ཡིན་ལ། ཚངས་པར་སྤྱོད་པ་ཟད་ན་སངས་རྒྱས་ཀྱི་བསྟན་པ་ནུབ་པར་འགྱུར་ཞིང་། དེ་ནུབ་པས་བསོད་ནམས་མངོན་པར་འདུ་བྱ་བ་རྣམས་རྒྱུན་ཆད་པར་འགྱུར་ལ། གཞི་དེ་ལས་དགེ་བ་མ་ཡིན་པ་དཔག་ཏུ་མེད་པ་འབྱུང་བའི་ཕྱིར་དེ་གཉིས་ཚངས་པར་སྤྱོད་པ་རྣམས་ལ་སྤངས་སོ་ཞེས་གསུངས་སོ། །

[Block 1242]
དེ་ལྟར་ཡིན་ན་ཚངས་པར་སྤྱོད་པ་དག་གིས༌[^696]གསང་སྔགས་ལ་འཇུག་ཏུ་མི་རུང་ངོ་ཞེ་ན།

[Block 1243 [VERSE]]
རྒྱུད་ཀུན་ཉན་དང་འཆད་པ་དང་། །
སྦྱིན་སྲེག༌[^697]མཆོད་སྦྱིན་སོགས་བྱེད་པ། །
སློབ་དཔོན་དབང་བསྐུར་རྙེད་གྱུར་པ། །

[Block 1244]
ཞེས་བྱ་བ་འདི་སྨོས་སོ། །

[Block 1245]
གལ་ཏེ་ཚངས་པར་སྤྱོད་པའི་སྔགས་པས་རྒྱུད་ལ་སོགས་པ་ཉན་པ་དང་། གཞན་ལ་འཆད་པ་དང་། བལྟ་བ་དང་། སྦྱིན་སྲེག༌[^698]དང་། གཏོར་མ་དང་། བཟླས་བརྗོད་དག་བྱེད་པར་འདོད་ན་ནི་སློབ་དཔོན་དབང་བསྐུར་ཞེས་པ་བུམ་པའི་དབང་གིས་རུང་བ༌[^699]རྒྱུད་ཐམས་ཅད་དང་། དཀྱིལ་འཁོར་གྱི་ཆོ་ག་ཐམས་ཅད་ནས་གསལ་བར་གསུངས་སོ། །

[Block 1246]
འདིའི་དོན་བླ་མ་དགེ་སློང་བསོད་སྙོམས་པ་ཡ་བ་དྭཱི་པས་གསུངས་ཏེ། འདི་སྐད་དུ་དེ་ལྟ་ཡིན་ན་ཚངས་པར་སྤྱོད་པ་རྣམས་ནི་ཐེག་པ་ཆེན་པོའི་ཡང་ཐེག་པ༌[^700]ཆེན་པོའི་སྐལ་བ་ཅན་མ་ཡིན་པར་འགྱུར་རོ་ཞེ་ན། དེ་ནི་འདིར་ངེས་པར་འཁྲུལ་པར་སྤྱད་པར་བྱ་སྟེ། གང་གིས་བུམ་པ་དང་། སློབ་དཔོན་དང་རྗེས་སུ་གནང་བ་ཐོབ་པ་ཉིད་ཀྱི་རྒྱུད་ལ་སོགས་པ་བསྒྲུབ་པ་དང་། བཤད་པ་དང་མཉན་པ་དང་བལྟ་བ་ལ་དབང་བསྐུར་བའི༌[^701]ཕྱིར་སྐལ་བ་ཅན་ཡིན་ནོ། །

[Block 1247]
དེ་ལྟ་ན་ཁྱིམ་པ་དག་ལ་ཡང་གསང་བ་དང་། ཤེས་རབ་ཀྱི་དབང་དགོས་པ་མེད་པར་འགྱུར་རོ་ཞེ་ན། དེ་མི་དགོས་པ་ཡང་ཡིན་ལ། དེ་ལས་བཟློག་པ་ཡང་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་གསུངས་སོ། །

[Block 1248]
དེ་ཉིད་རིག་ལ་ཉེས་པ་མེད། །ཅེས་པ་འདིའི་དོན་ནི་བདག་ལ་བླ་མ་དག་གིས༌[^702]ཉེ་བར་བསྟན་པ་གནང་བ་མང་དུ་ཡོད་དེ། བླ་མ་དམ་པ་ཁ་ཅིག་གི་ཞལ་ནས་སྙིང་རྗེས་སེམས་ཅན་གྱི་དོན་རིག་ཅིང་སེམས་སྙིང་རྗེའི་དབང་དུ་སོང་བའི་བྱང་ཆུབ་སེམས་དཔས་ཅི་བྱས་ཀྱང་དེའི་རྒྱུད་ལ་ཉེས་པ་མེད་ཅིང་དེའི་རྗེས་ལ་ཡང་བསོད་ནམས་མང་དུ་འཕེལ་བར་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 1249]
དེ་ནི་བཟོད་པ་ཆུང་ངུ་ཐོབ་པ་ཡིན་ནོ། །

[Block 1250]
དམ་པ་ལ་ལའི་ཞལ་ནས་ཆོས་ཐམས་ཅད་སྒྱུ་མར་ཤེས་ཤིང་དེའི་དེ་ཁོ་ན་ཉིད་རིག་པའི་རྣལ་འབྱོར་པ་ལས་ཉེས་པར་འགྱུར་བ་གང་ཡང་མེད་དེ། འདི་སྐད་དུ།

[Block 1251 [VERSE]]
ཆུ་ཡི་ཟླ་བ་ལྟ་བུར་ནི། །
རྣལ་འབྱོར་པ་ནི་གང་གིས༌[^703]ཤེས། །
དེ་ནི་སྡིག་དང་བསོད་ནམས་སོགས། །
ནམ་ཡང་གོས་པར་མི་འགྱུར་རོ། །

[Block 1252 [VERSE]]
ནང་དང་ཕྱི་རོལ་གནས་འདི་ཀུན། །
སེམས་ཡིན་སྒྱུ་མ་ལྟ་བུ་སྟེ། །
དེ་ཡང་རྟག་མིན་ཆད་པ་མིན། །
གཉི་ག༌[^704]དག་ཏུའང་མི་རྟོག་ཅིང་། །

[Block 1253 [VERSE]]
དངོས་འཛིན་དུག་གིས་མ་གོས་པས། །
དེ་ལྟ་བུ་ནི་སུས་མཐོང་བ། །
སྒྱུ་མར་རིག་ལ་ཉེས་པ་མེད། །

[Block 1254]
ཅེས་གསུངས་ཏེ། ཆོས་ཀྱི་མཆོག་ཆུང་ངུ་ཐོབ་པ་ལ་ཉེས་པ་མེད་པའོ། །

[Block 1255]
བླ་མ་དགེ་སློང་བསོད་སྙོམས་པའི་ཉེས་པར་མི་འགྱུར་བ་ནི་བླ་མའི་ཞལ་སྔ་ནས་མཛད་པའི་གཞུང་དེ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 1256]
འདི་ནི་ལས་དང་པོ་པ་ད་ལྟ་ཉིད་ན་ཡང་ཉེས་པ་མེད་པའོ། །

[Block 1257]
དམ་པ་གཞན་ནི་འདི་སྐད་དུ་འཕགས་པ་འོད་སྲུངས་ཀྱིས་ཞུས་པའི་མདོ་དང་།[^705] བུད་མེད་འགྱུར་བ་ལུང་བསྟན་པའི་མདོ་དང་། དཔལ་མཆོག་དང་པོའི་རྒྱུད་དང་། འདུལ་བ་དོན་ཡོད་པའི་རྒྱུད་དང་། རྒྱུད་གཞན་དེ་མ་ཡིན་པ་དག་དང་། འཕགས་པ་ཀླུ་སྒྲུབ་དང་། སློབ་དཔོན་ཨཱརྱ་དེ་བ་ལ་སོགས་པའི་གཞུང་དེ་དག་གི་ཚུལ་གྱིས༌[^706]ཉེས་པར༌[^707]མི་འགྱུར་ཞིང་། དོན་དེ་ནི་དེ་ཁོ་ན་ཉིད་རིག་པ་ལ་ཉེས་པ་མེད་དེ་རྩེ་མོ་ཆུང་ངུ་ཐོབ་པ་ནའོ་ཞེས་གསུང་ངོ་། །དམ་པ་གཞན་ནི་འདི་སྐད་དུ་ཆོས་ཐམས་ཅད་ཀྱི་སྐྱེ་བ་མེད་པ་དོན་དམ་པ་བྱང་ཆུབ་ཀྱི་སེམས་བསྐྱེད་ཅིང་། དེ་རྒྱུད་ལ་སྐྱེས་པ་ལ་ཡང་ཉེས་པ་མེད་དེ། ཆོས་རྣམས་ཀྱི་དེ་ཁོ་ན་ཉིད་རིག་པ་ལ་ཉེས་པ་མེད་དོ་ཞེས་གསུང་སྟེ།[^708] འདི་ནི་བདེན་པ་མཐོང་བ་དག་ལ་ཉེས་པ༌[^709]པར་མི་འགྱུར་རོ། །

[Block 1258]
དེ་བས་ན་ལམ་ལ་གནས་པའི་རྣལ་འབྱོར་པ་དེས་ཉེས་པ་མེད་པ་དང་།

[Block 1259 [VERSE]]
ཉེས་པར་འགྱུར་བ་དག་ཤེས་པར་བྱའོ། །
ཡིད་བཞིན་ནོར་བུ་ལྟ་བུའི་སྤྲུལ་པའི་སྐུ། །
འདས་ཤིང་འཕགས་པ་ཀླུ་སྒྲུབ་ལ་སོགས་པའི། །
མཁས་པ་ཆེན་པོ་རྣམས་ཀྱང་མེད་པ་ན། །

[Block 1260 [VERSE]]
ཐུབ་པའི་དམ་ཆོས་ནུབ་ཏུ་ཉེ་བ་ཡི། །
དིང་སང་དུས་ན་སྨྱོན་པ་ལྟ་བུ་ཡི། །
ལོག་པར་རྟོགས་པའི་གང་ཟག་མང་པོ་བྱུང་། །
བླ་མ་བརྒྱུད་པའི་གདམས་ངག་བྲལ་བ་ཡི། །

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
--- END BLOCKS ---
