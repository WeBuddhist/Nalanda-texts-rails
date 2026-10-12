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
དེ་དག་ནི་གསུངས་པའི་ཚིག་གི་དོན་ཡིན་ཏེ། རྒྱུད་ཐམས་ཅད་དང་། སྔོན་གྱི་སློབ་དཔོན་ཐམས་ཅད་དང་། ད་ལྟ༌[^662]ཉིད་ཀྱི་བླ་མ་མ་ལུས་པས་འདི་སྐད་དུ་གསུངས་ཞེས་པའོ། །

[Block 1192]
ཡང་ན་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་ལྷའི་པྲ་ཕབ་པ་དང་། རྨི་ལམ་དག་ཏུ་གང་ཟག་འདི་ནི་སྐྱེ་བ་སྔ་མ་ལ་གསང་སྔགས་སྤྱོད་སྤྱོད་པ་དག་ཡིན་ནོ་ཞེས་ཟེར་ན། དེས་བླ་མ་ཡོངས་སུ་མཉེས་པར་བྱས་ལ་བྱིན་གྱིས་བརླབ་པ་བྱས་ཏེ། འདི་ལྟར་སྒྲུབས༌[^663]ཤིག་ཅེས་གནང་བ་བྱིན་ལ། སྒྲུབ་པའི་ཆོ་གའི་ཐབས་སྦྱིན་པར་བྱའོ། །

[Block 1193]
ཆོ་ག་དེ་ཡང་འདི་ཡིན་ཏེ། འཕགས་པ་དམ་ཚིག་གསུམ་བཀོད་པའི་ཆོ་ག་དང་། བཅོམ་ལྡན་འདས་ནོར་བུ་རྒྱས་པའི་གཞལ་མེད་ཁང་གི་ཆོ་ག་དང་། བཅོམ་ལྡན་འདས་སྨན་གྱི་བླ་བཻ་ཌཱུརྱའི་འོད་ཀྱི་རྒྱལ་པོའི་ཆོ་གས་སྡིག་པ་སྦྱོང་བ་དང་། ཚོགས་བསགས་པ་བྱས་ལ་ལྟས་བཟང་པོ་བྱུང་བ་ན་གང་ཟག་དེས་གསང་སྔགས་ཀྱི་ཐེག་པ་ལ་འཇུག་པར་གནང་གི་འདི་ལྟར་སྐྱེ་བ་སྔ་མ་ལ་གསང་སྔགས་སྤྱད་པ་མ་ཡིན་པ་དང་། ཡང་ན་གསུམ་ལ་སྐྱབས་སུ་འགྲོ་བ་དང་། སྨོན་པ་བྱང་ཆུབ་ཀྱི་སེམས་བསྐྱེད་པ་དང་། འཇུག་པ་བྱང་ཆུབ་ཀྱི་སེམས་བསྐྱེད་པ་བྱས་པ་ཙམ་ལ་ནི་གསང་སྔགས་བསྟན་པ་དང་། དེས་བསྒྲུབ་པ་དང་བལྟ་བ་དང་མཉན་པ༌[^664]བྱ་བར་མ་གནང་སྟེ། འཇུག་པའི་ལམ་སོ་སོ་བ་ཡིན་པ་དང་། ཐེག་པ་དག་ནི་རྣམ་པར་ཐར་པ་བསྲེ་བར་མི་བྱ་བ་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས༌[^665]གང་ཟག་གི༌[^666]དབང་པོ་དང་ཁམས་དང་བག་ལ་ཉལ་མཁྱེན་པས༌[^667]ཐེག་པའི་ལམ་སོ་སོར་གསུངས་པ་ཡིན་ནོ། །

[Block 1194]
དེ་བས་ན་རྩ་བ་ནས་སྨྲས་པ་དེ་ལྟ་བས་ན།

[Block 1195 [VERSE]]
གལ་ཏེ་གསང་སྔགས་སྤྱོད་འདོད་པས། །
དེ་ཚེ་སློབ་དཔོན་དབང་བསྐུར༌[^668]ཕྱིར། །

[Block 1196]
ཞེས་སྨྲས་ཏེ། ཕ་རོལ་ཏུ་ཕྱིན་པའི་ལམ་དུ་འཇུག་ཅིང་སྤྱོད་འདོད་ན་ནི་སྔར་ཇི་ལྟར་བརྗོད་པ་བཞིན་དུ་བསླབ་པ་རྣམ་པ་གསུམ་ལ་བསླབ་པར་བྱ་བ་ཡིན་ལ། གལ་ཏེ་གསང་སྔགས་སྤྱོད་ཅིང་རྗེ་བཙུན་སྒྲོལ་མ་ལ་སོགས་པ་སྒྲུབ་པར་འདོད་ན་ནི་སློབ་དཔོན་གྱི་དབང་ཞེས་པ་བུམ་པའི་དབང་བསྐུར་བ༌[^669]ཞུ་བར་བྱའོ་ཞེས་པ་ནི་ཤློ་ཀའི་དོན་ཡིན་ནོ། །

[Block 1197]
འོ་ན་དབང་བསྐུར་བའི་བླ་མ་དེ་ལ་བླ་ཆོས༌[^670]དང་ཡོ་བྱད་མེད་པར་བྱ་བའམ་ཞེ་ན་མ་ཡིན་ཏེ། བསྙེན་བཀུར་རིན་ཆེན་ལ་སོགས་ཞེས་སོ། །

[Block 1198]
འོ་ན་ཡོ་བྱད་ཀྱིས༌[^671]ཕོངས་ཤིང་དབུལ་པོ་དག་གིས་ཇི་ལྟར་བྱ་ཞེ་ན། བཀའ་སྒྲུབ་ལ་སོགས༌[^672]ཞེས་པའོ། །

[Block 1199]
འདིར་སྐྱེ་བོ་འབྱོར་པ་ཅན་དག་གིས་ནི་རྒྱལ་སྲིད་རིན་པོ་ཆེ་བདུན་ལ་སོགས་པ་ཐ་ན་བདག་ཉིད་ཀྱི་ལུས་ཀྱང་དབུལ་བར་བྱ་སྟེ། ཇི་ལྟར་སློབ་དཔོན་སངས་རྒྱས་ཡེ་ཤེས་ཞབས་ལ་རྒྱལ་པོ་དེ་བ་པཱ་ལས་རྒྱལ་སྲིད་ཐམས་ཅད་ཕུལ་བའི་རྗེས་སུ་བཙུན་མོ་དང་རང་ཉིད་ཀྱང་ཕུལ་ནས་ཕྱིས་རྒྱལ་པོ་དང་བཙུན་མོ་གཉིས་གསེར་དེ་གཉིས་དང་མཉམ་པས་བསླུས་པ་ལྟ་བུའོ། །

[Block 1200]
དབུལ་པོ་དག་གིས་བཀའ་བསྒྲུབ་པ་དང་། ལུས་ཀྱི་བསྙེན་བཀུར་དང་། དཀྱིལ་འཁོར་དང་། མེ་ཏོག་ཡང་དང་ཡང་དུ་དབུལ་བ་ལ་སོགས་བྱའོ། །

[Block 1201]
དེ་ལྟ་བུའི་ཚུལ་གྱིས་བླ་མ་དམ་པ་མཉེས་པར་བྱའོ། །

[Block 1202]
དེ་ལྟར་བླ་མ་མཉེས་ཤིང་དགེས་པར་གྱུར་པ་དང་། དབང་བསྐུར་བ་ཐོབ་པར་བྱས་ནས་ལུས་ལ་སོགས་པའི་སྡིག་པ་ཐམས་ཅད་ལས་གྲོལ་ནས། དེས་སྡིག་པ་དག་པའི་རྒྱུས་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་དངོས་གྲུབ་ཐམས་ཅད་སྒྲུབ་པའི་སྐལ་བ་ཅན་དུ་འགྱུར་རོ། །

[Block 1203 [HEADING]]
### གསང་སྔགས་ལ་ལོག་པར་རྟོག་པ། ^10-1-0

[Block 1204]
དེ་ལྟར་གསང་སྔགས་ཀྱི་ཐེག་པ་ལ་གནས་ནས་འབད་པ་མེད་པར་མྱུར་དུ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པར་བྱས་ཏེ། གཞན་གྱི་དོན་མཐར་ཕྱིན་པར་བྱ་བའི་ཐབས་བསྟན་ནས། ད་ནི་གསང་སྔགས་ཀྱི་ཐེག་པ་ལ་ལོག་པར་རྟོག་པ་དག་དགག་པའི་ཕྱིར།

[Block 1205]
དང་པོ་སངས་རྒྱས་རྒྱུད་ཆེན་ལས། །ཞེས་པ་ལ་སོགས་པ་སྨྲས་ཏེ། འདིར་གསང་སྔགས་ལ་ལོག་པར་རྟོག་པ་ནི་གཉིས་ཏེ་སྒྲོ་འདོགས་པར་བྱེད་པ་དང་སྐུར་པ་འདེབས་པར་བྱེད་པའོ།[^673] །

[Block 1206]
སྔ་མ་ནི་ཚར་གཅད་པར་བྱའོ། །

[Block 1207]
ཕྱི་མ་ནི་རྗེས་སུ་གཟུང་བར་བྱའོ། །

[Block 1208 [HEADING]]
#### སྒྲོ་འདོགས་པར་བྱེད་པ། ^10-1-1-0

[Block 1209]
འདི་ལྟར་འདི་ན་ཁ་ཅིག་གསང་སྔགས་ཀྱི་རྒྱུད་ཆེན་པོ་མཐའ་དག་གི༌[^674]དགོངས་པ་ཡང་མི་ཤེས། བླ་མ་དམ་པས་ཀྱང་མ་ཟིན་ཅིང་། སྡིག་པའི་བཤེས་གཉེན་ལ༌[^675]བརྟེན་པས་གསང་སྔགས་ཀྱི་ཚུལ་ཇི་ལྟ་བར་མ་ཤེས་པ༌[^676]དགོངས་པ་ཅན་གྱི་བཀའ་ལ་བརྟེན་ནས་འདི་སྐད་དུ་བདག་ཅག་ནི་གསང་སྔགས་པའོ། །

[Block 1210]
བདག་ཅག་ནི་སྤྱོད་པ་ཐམས་ཅད་བག་ཡངས་སུ་བྱེད་ཅིང་ཕྱག་རྒྱ་ཆེན་པོའི་དངོས་གྲུབ་ཀྱང་མྱུར་དུ་ཐོབ་པར་འགྱུར་རོ་ཞེས་སྒྲོགས་ཤིང་གནས་པ་དེ་དག་ནི་ངན་འགྲོར་འགྲོ་བར་འགྱུར་ཏེ། དེ་བཞིན་གཤེགས་པའི་བཀའ་ལ་སྐུར་པ་བཏབ་པ་དང་། ཚངས་པར་སྤྱོད་པ་དག་སྦགས་པས་སངས་རྒྱས་ཀྱི་བསྟན་པ་ནུབ་པར་བྱས་པ་དང་། མངོན་སྤྱོད་དྲག་པོ་བྱས་པ་དང་། བུད་མེད་དག་བསྟེན་པས་ཕམ་པ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 1211]
དཔལ་ཡེ་ཤེས་གྲགས་པའི་ཞལ་ནས་འདི་སྐད་དུ་བདག་ཅག་རྣལ་འབྱོར་པ་ལ་བཅོམ་ལྡན་འདས་ཀྱིས༌[^677]གནང་བ་ཡིན་ནོ་ཞེས་ཟེར་ཞིང་སྒྲ་གསང་ཆེར་སྒྲོགས་པ་དང་། གཞན་ཡང་སྤྱོད་པ་ཐམས་ཅད་ཀྱང་བག་ཡངས་སུ་བྱེད་པ་དེ་དག་ནི་ངན་འགྲོར་འགྲོ་བར་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 1212]
བདག་གི་བླ་མ་དགེ་སློང་བསོད་སྙོམས་པ་ཡ་བ་དྭཱི་པའི་ཞལ་ནས་ཀྱང་། གལ་ཏེ་དབང་བསྐུར་བ་དེ་གཉིས་འཛིན་པར་བྱེད་ན། སློབ་དཔོན་དང་སློབ་མ་དང་བཅས་པ་ངན་འགྲོར་འགྲོ་བར་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 1213]
བཅོམ་ལྡན་འདས་ཀྱིས༌[^678]དགོངས་པ་ལུང་བསྟན་པའི་རྒྱུད་ཆེན་པོ་ལས།

[Block 1214 [VERSE]]
རྣལ་འབྱོར་མན་ངག་མེད་པ་དག །
ལྕགས་ཀྱུ་མེད་པ་བཞིན་དུ་སྤྱོད། །
བདག་ནི་རྣལ་འབྱོར་པ་ཞེས་ཟེར། །
ཆོས་ནི་གཡོ་ཡིས་བྱེད་པར་འགྱུར། །

[Block 1215 [VERSE]]
སྔགས་དང་ཕྱག་རྒྱའི་སྦྱོར་བ་ཡིས། །
འཚོ་བ་དག་ཀྱང་སྒྲུབ་པར་བྱེད། །
ཉེས་པ་ཅུང་ཟད་ཙམ་ལ་ཡང་། །
མངོན་སྤྱོད་དྲག་པོ་བྱེད་པར་འགྱུར། །

[Block 1216 [VERSE]]
འདི་ལྟར་སྒྲུབ་པའི་ཐབས་ཙམ་ཞིག །
ཤེས་ནས་རྒྱུད་ཆེན་འཆད་པར་བྱེད། །
གང་དུ་རྙེད་པ་ཐོབ་འགྱུར་བར། །
དམ་པའི་ཆོས་ནི་སྟོན་པར་བྱེད། །

[Block 1217]
ཅེས་བྱ་བ་ལ་སོགས་པ་མང་དུ་གསུངས་སོ། །

[Block 1218]
དེ་བཞིན་དུ་དཔལ་པདྨ་རྡོ་རྗེས་ཀྱང་དེ་ལྟ་བུའི་ཉེས་དམིགས་མང་དུ་གསུངས་ནས།

[Block 1219 [VERSE]]
དེ་ལྟ་བུ་དང་དེ་དག་ཉིད། །
ཀུན་ཀྱང་སྡིག་པའི་ལས་ཅན་ཏེ། །
དམ་པ་མིན་པའི་ལམ་ཞུགས་ནས། །
དམྱལ་བ་དག་ཏུ་འགྲོ་བར་འགྱུར། །

[Block 1220]
ཞེས་གསུངས་སོ། །

[Block 1221]
ཁུངས་མང་དུ་ཡོད་མོད་ཀྱི་ཡི་གེ་མངས་པར་འགྱུར་རོ། །

[Block 1222]
དེ་ལྟ་བུ་དག་ནི་སྙིང་རྗེའི་སེམས་ཀྱིས༌[^679]ཚར་གཅད་པར་བྱའོ། །

[Block 1223 [HEADING]]
#### སྐུར་པ་འདེབས་པར་བྱེད་པ། ^10-1-2-0

[Block 1224]
ཡང་འདི་ན་ལ་ལ་དག་འདི་སྐད་དུ་གསང་སྔགས་ཀྱི་ཚུལ་ཆེན་པོ་ཇི་ལྟ་བར་མི་ཤེས་པར༌[^680]གསང་སྔགས་ཀྱི་ཐེག་པས༌[^681]ཅི་ཞིག་བྱ། ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་གཙང་བ་དེ་ཉིད་ལ་འཇུག་པར་བྱའོ། །

[Block 1225]
འདི་ལྟར་བུད་མེད་བསྟེན་པས་ནི་མི་ཚངས་པར་སྤྱོད་པའི་ཕམ་པ་འོང་ལ། མངོན་སྤྱོད་དྲག་པོ་བྱས་པས་ནི་སྲོག་བཅད་པའི༌[^682]ཕམ་པ་འོང་བས་དེ་ལ་འཇུག་པར་མི་བྱའོ་ཞེས་རྒྱུད་ཀྱི་དགོངས་པ་མི་ཤེས་པར་སྐུར་པ་འདེབས་པ་དེ་དག་ནི་ཟབ་ཅིང་རྒྱ་ཆེ་བ་དབང་པོ་རྣོན་པོའི་སྤྱོད་ཡུལ་སངས་རྒྱས་ཀྱི་བསྟན་པའི་སྙིང་པོར་གྱུར་པ་སྐལ་པ་དང་། བག་ཆགས་དང་། ལས་འཕྲོར་ལྡན་པ་འགའི་སྤྱོད་ཡུལ་དུ་གྱུར་པ་ཡིན་པས་དེ་ལྟ་བུ་ལ་སྐུར་པ་འདེབས་པ་དེ་ནི་ངེས་པར་སེམས་ཅན་དམྱལ་བར་འགྲོ་བར་འགྱུར་བ་འདི་ལ་ཐེ་ཚོམ་མི་བྱ་སྟེ། དེ་བཞིན་གཤེགས་པའི་བཀའ་ལ་སྐུར་པ་བཏབ་པ་དང་། ཆོས་ཟབ་མོ་སྤངས་པའི་ཕྱིར་རོ། །

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
--- END BLOCKS ---
