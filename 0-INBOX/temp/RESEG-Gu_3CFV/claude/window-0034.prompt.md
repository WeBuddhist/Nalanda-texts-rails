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
བུད་ཤིང་གི་དོན་དུ་ཤིང་ལྗོན་པ་དང་། མཎྜལ་གྱི་དོན་དུ་ས་བརྡུང་བ་ལ༌[^724]སོགས་པ་འདི་ལྟ་བུ་ལ་ཡང་། ཅི་འདིས་བཀག་པ་ཉིད་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ་ཞེས་བསྟན་པ་ནི་བརྡེག་པ་སྟེར་བའི་སྦོམ་པོ་ལ་འཇུག་པ་ལ་འདི་བཀག་པ་ཡིན་གྱི་གཞན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1192]
དེ་ལྟར་ཡང་ཚེ་དང་ལྡན་པས་རི་ཤིང་གཤེགས་པ་འཇུག་པ༌[^725]འབྱུང་བར་འགྱུར་རོ། །

[Block 1193]
བརྡེག་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1194]
གང་དུ་གཟས་པའི་ལྟུང་བྱེད་ཅེས་བྱ་བ་འདི་ལ་རྙོག་པ་ཅན་གྱི་སེམས་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་ནས་གཟས་པ་ནའོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་མཐའ་མ་ལ་ལྟོས་ནས་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་བརྡེག་པར་གཟས་པ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་འདིར་གཅིག་ཉིད་དུ་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་རྫས་རེ༌[^726]རེ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སོར་མོ་ལ་སོགས་པའི་རྫས་ཇི་སྙེད་གཟས་པ་དེ་སྙེད༌[^727]ཀྱི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1195]
གཟས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1196]
ཅི་ཞིག་བྱས་ན་གནས་ངན་ལེན་འཆབ་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཕམ་པར་གྱུར་པ་དང་དགེ་འདུན་ལྷག་མ་དག་བཅབ་པ༌[^728]ཞེས་བྱ་བ་སྨོས་ཏེ། གནས་ངན་ལེན་ཅེས་བྱ་བ་འཆད་པར་འགྱུར་བ་དང༌[^729]དེ་དང་འདི་ལ་འབྲེལ་པའོ། །

[Block 1197]
ཅི་བཅབ་པ་རྣམ་པ་ཐམས་ཅད་ལ་གནས་ངན་ལེན་དུ་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་བདེ་བ་ལ་མི་རེག་པ་དང་དགེ་སྦྱོང༌[^730]གི་ཚུལ་དང་ཚངས་པར་སྤྱོད་པའི་བར་ཆད་དང་། དགེ་འདུན་འཁྲུག་ཏུ་དོགས་པའི་དབང་ཉིད་མ་གཏོགས་པར་འཆབ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དབང་ཉིད་ཅེས་བྱ་བའི་སྒྲ་ནི་བདེ་བ་ལ་མི་རེག་པ་ལ་སོགས་པ་ཐམས་ཅད་དང་སྦྱར་བར་བྱའོ། །

[Block 1198]
བར་ཆད་ཅེས་བྱ་བའི་སྒྲ་ནི་དགེ་སྦྱོང་གི་ཚུལ་དང་། ཚངས་པར་སྤྱོད་པ་གཉིས་དང་སྦྱར་བར་བྱའོ། །

[Block 1199]
བདེ་བ་ལ་མི་རེག་པའི་དབང་ཉིད་དང་། དགེ་སྦྱོང༌[^731]གི་ཚུལ་གྱི་བར་ཆད་ཀྱི་དབང་ཉིད་དང་། ཚངས་པར་སྤྱོད་པའི་བར་ཆད་ཀྱི་དབང་ཉིད་དང་། དགེ་འདུན་འཁྲུག་ཏུ་དོགས་པའི་དབང་ཉིད་མ་གཏོགས་པར་གཞན་ཕམ་པར་འགྱུར་བ་དང་དགེ་འདུན་ལྷག་མ་དག་འཆབ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1200]
དེ་ལ་འདིར་དགེ་སྦྱོང་གི་བར་ཆད་ལ་སོགས་པ་ནི་དཔེ་ཙམ་དུ་རིག་པར་བྱའོ། །

[Block 1201]
གང་ཟག་གི་གཞི་འཁོར་དང་བཅས་པས་འཆབ་པའི་ཆོ་ག་ཤེས་པར་བྱའོ། །

[Block 1202]
དུས་གང་གི་ཚེ་བཅབས་ཤེ་ན། དེའི་ཕྱིར་ཉིན་མཚན་གྱི་མཐར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་གི་རྗེས་ལ་སྐྱ་རེངས་འཆར་ཀ་ཚུན་ཆད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1203]
སྔ་རོལ་དུ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ཉིན་མཚན་གྱི་མཐའི་སྔ་རོལ་དུ་འཆབ་པ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 1204]
ལྟུང་བ་གཞན་ཡང་ངོ་ཞེས་བྱ་བ་ཆུང་བ་ལ་དོན་འཐོབ་པ་ལས་ཕམ་པར་གྱུར་པ་དང་། དགེ་འདུན་གྱི་ལྷག་མ་དག་ལས་གཞན་པའི་ལྟུང་བྱེད་བཅབས་ན་ནི་ཉིན་མཚན་གྱི་མཐར་ཡང་ཉེས་བྱས་ལ་སྔ་རོལ་དུ་ཡང་ཉེས་བྱས་སོ། །

[Block 1205]
གནས་ངན་ལེན་འཆབ་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1206]
ཅི་ཞིག་བྱས་ན་ཟན་གཅོད་དུ་འཇུག་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ནད་ཀྱི་གཉེན་པོའི་དོན་ཉིད་མ་གཏོགས་པར་ཆེད་དུ་བསམས་ཏེ་ཁྱིམ་པ་སྦྱིན་པ་པོ་ཟན་གཅོད་དུ་བཅུག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཟན་གང་གི་སྦྱིན་པ་པོ་ཁྱིམ་པ་གང་ཡིན་པ་དེ་ནི་སྦྱིན་པ་པོ་ཁྱིམ་པའི་ཟན་ཏེ། དེ་གཅོད༌[^732]པ་ནི་དགེ་སློང་གི་ཆེད་དུ་བསམས་ཏེ་ཟན་གང་གིས་གཅོད༌[^733]དུ་བཅུག་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅི་རྣམ་པ་ཐམས་ཅད་དུ་བཅུག་པ་ལ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ནད་ཀྱི་གཉེན་པོའི་དོན་ཉིད་མ་གཏོགས་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1207]
གཅོད་དུ་བཅུག་པ་ནི་དེར་རང་གི་ཚིག་གིས་ཞེས་བྱ་བ་འཇུག་གོ། །

[Block 1208]
དེ་ལྟ་བས་ན་སྤྲིང་ཡིག་དང་ལག་ཡིག་དང་ལག་རྩིས་དང་། མངགས་པ་དང་བརྒྱུད་པ་དང་ཟུར་གྱིས་གཅོད་དུ་བཅུག་ན་ཉེས་བྱས་སོ། །

[Block 1209]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་གསུང་དེ་འདིས༌[^734]བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 1210]
སྦྱིན་བདག་ཁྱིམ་པ་དག་ཟན་གཅོད་པར་བྱེད་དུ་བཅུག་པ་འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་མུ་སྟེགས་ཅན་གྱི་ཁྱིམ་བདག་ཏུ་བྱེད༌[^735]དུ་བཅུག་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1211]
ཟན་གཅོད་དུ་འཇུག་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1212]
སེང་གེ་ལ་རེག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མེ་དང་འདྲ་བར་བསྙེན་པར༌[^736]དཀའ་ཞིང་བཟོད་པར་དཀའ་བ་ཉིད་ཡིན་པའི་ཕྱིར་རེག་པར་བྱ་བ་མ་ཡིན་ཏེ། རིན་པོ་ཆེའམ་དེ་དང་མཉམ་པ་ཉིད་ཀྱི་ཕྱིར་ནི་མ་ཡིན་ནོ། །

[Block 1213]
དེ་བས་ན་དེར་འཇུག་པའོ། །

[Block 1214]
རིན་པོ་ཆེ་འམ་དེ་དང་འདི་མཉམ་པས་དེ་རེག་པ་བཀག་པ་ལ་དུས་བྱིན་གྱིས་བརླབ་པའི་རྣམ་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་དུས་བྱིན་གྱིས་བརླབས་པའི༌[^737]ངོ་བོ་གསུངས་པ་ནི་སྟོན་པ་དང་ཆོས་དང་དགེ་འདུན་དང་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་རྣམས་ཀྱིས་ཆོས་དང་ལྡན་པའི་བྱ་བའི་དོན་ཉིད་དང་ལྷུང་བཟེད་དང་ཚོན་གྱི་ལས་ལ་བརྟག་པ་ནི་དུས་བྱིན་གྱིས་བརླབས་པ་ཡིན་ནོ་ཞེས་བྱ་བ༌[^738]སྨོས་ཏེ། དེ་རྣམས་ཀྱིས་ཆོས་དང་ལྡན་པའི་བྱ་བ་གང་ཡིན་པ་དེའི་དོན་ཉིད་ལ་རེག་པ་ལ་ལྷུང་བཟེད་དང་ཚོན་གྱི་ལས་ལ་བརྟགས་པ་ནི་དུས་བྱིན་གྱིས་བརླབས༌[^739]པའོ། །

[Block 1215]
འདིར་གཞུང་ནི་དུས་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་གསུངས་པ་དང་། དེ་དག་གིས་གང་གི་དོན་དུ་བྱིན་གྱིས་བརླབ་པ་མི་ཤེས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྟོན་པའི་བྱ་བ་དང་ཆོས་དང་དགེ་འདུན་དང་། སློབ་དཔོན་དང་མཁན་པོ་དང་། ཚངས་པ་མཚུངས་པར་སྤྱོད་པའི་བྱ་བས་མངོན་པར་བརྟེན་པ་ནི་བྱིན་གྱིས་བརླབ་པ་དང་། མངོན་པར་འདུ་བྱེད་པ་སེམས་ཀྱིས་འདིར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1216]
ཆོས་དང་ལྡན་པའི་བྱ་བའི་དོན་གྱི་དབང་ཉིད་ཀྱིས་ནི་འདིར་འཇུག་པར་རིགས་པ༌[^740]ཡིན་ཏེ། དེའི་ཕྱིར་ཆོས་དང་ལྡན་པའི་དོན་ཉིད་ཀྱི་ཚིག་གོ། །

[Block 1217]
སློབ་དཔོན་དང་མཁན་པོ་དག་ལ་ནི་མ་ཡིན་ཏེ་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་དག་ལ་ཡང་མ་ཡིན་ནོ། །

[Block 1218]
དེ་བས་ན་འདིར་དེ་དག་གི༌[^741]ཞེས་བྱ་བའི་ཚིག་གོ། །

[Block 1219]
འདིར་ལྷུང་བཟེད་དང་ཚོན་གྱི་ལས་ཞེས་སྨོས་པས་ནི། རང་གི་ལྷུང་བཟེད་དང་ཆོས་གོས་ཀྱི་ལས་བསྟན་ཏོ། །

[Block 1220]
ལྷུང་བཟེད་ཀྱི་ལས་བྱའོ་ཞེ་འམ། ཚོན་གྱི་ལས་བྱའོ་ཞེས་ཡིད་ཀྱིས་བརྟག་པ་གང་ཡིན་པ་དེ་ནི་དུས་བྱིན་གྱིས་བརླབ་པ་ཡིན་ནོ། །

[Block 1221]
ཡུན་རིང་དུ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དུས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1222]
འདིར་གཞུང་ནི་དགེ་སློང་དག་ལྷུང་བཟེད་ཀྱི་ལས་དང་ཚོན་གྱི༌[^742]ལས་དག་བྱེད་པ་ན་ཡང་དང་ཡང་བརྗེད་ངས་པས་མེ་ལ་རེག་ནས་དེ་དག་འགྱོད་པ་སྐྱེས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དུས་ཡུན་རིང་དུ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 1223]
ཅི་ཞིག་བྱས་ན་མེའི་ཐ་སྙད་ཀྱི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རྩེ་བ་ཉིད་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1224]
དེ་རྣམ་པ་གང་གིས་ཡིན་ཞེ་ན། རྩེ་བའི་ངོ་བོ་བསྟན་པའི་ཕྱིར་གཞན་ལ་གཏོང་བས་ཟླ་བ་དང་ཉི་མ་དང་མགལ་མེའི་འཁོར་ལོ་ལ་སོགས་པ་བྱེད་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཅི་ཞིག་རྩེ་བ་ལ་ཞེ་ན། དེའི་ཕྱིར་མེའི་ཞེས་བྱ་བ་སྨོས་སོ། །ཅི་རྩེ་བ་འབའ་ཞིག་ལ་ལྟུང་བ་འདིར་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་དུས་བྱིན་གྱིས་མ་བརླབས་པའི༌[^743]དགེ་སློང་ན་བའི་དབང་ཉིད་དུ་གནས་པ་མ་ཡིན་པས་རེག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མེ་ལ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1225]
ཇི་ལྟར་རེག་ན་ཞེ་ན་དེའི་ཕྱིར་རང་ངམ་བསྒོ་བས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་རྩེ་བས་རེག་པ༌[^744]འབའ་ཞིག་ལ་ལྟུང་བ༌[^745]འདིར་འགྱུར་རམ་ཞེ་ན་དེའི་ཕྱིར། སྦར་བ་དང་གསོད་པ་དང་རེག་པ་དང་མ་རེག་པའི་བུད་ཤིང་བསྐུལ་བ་དང་བཅས་པ་འདྲེན་པ་དང་མ་དག་མ་སྤུང་བ་དང་འབྲུ་བ་དག་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1226]
དུས་བྱིན་གྱིས་མ་བརླབས་པའམ་ན་བའི་དབང་ཉིད་དུ་གནས་པ་མ་ཡིན་པའི་རང་ངམ་བསྒོ་བས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1227]
མེ་སྦར་ཏམ༌[^746]གསོད་དམ༌[^747]མེས་རེག་པའི་བུད་ཤིང་བསྐུལ་ཏམ། མེས་མ་རེག་པའི་བུད་ཤིང་བསྐུལ་ཏམ། མེ་དང་བཅས་པའི་བུད་ཤིང་འདྲེན་ཏམ་བསྐུལ་ཏམ། མདག་མ་སྤུངས་སམ༌[^748]འབྲུ་བར་བྱེད་པ་འདི་རྣམས་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1228]
འདིར་གཞུང་ནི་དགེ་སློང་མེ་སྦར་བར་བྱེད་ན་དེས་དུས་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 1229]
བྱིན་གྱི༌[^749]མ་བརླབས་པར༌[^750]སྦར་བར་བྱེད་ན་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1230]
སྦར་ཏམ༌[^751]གསོད་པ་དག་ལ་ནི་འདི་ཡིན་ཏེ། བུད་ཤིང་མེས་རེག་པ་བསྐུལ་ཏམ། མས༌[^752]མ་རེག་པའི་བུད་ཤིང་བསྐུལ་ཏམ། མེ་དང་བཅས་ཤིང་འབྲེལ་པའི་བུད་ཤིང་ཕྱིར་དྲངས་སམ། མདག་མ་དག་སྤུངས་སམ་དེ་བཞིན་དུ་མགལ་བར་སྐུལ༌[^753]བར་བྱེད་དམ། མགལ་བ་འདྲེན་པར་བྱེད་དམ། ཤིང་འཛུད་པར་བྱེད་ན་ཐམས་ཅད་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
