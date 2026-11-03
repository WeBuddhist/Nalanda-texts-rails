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
དེ་ལྟར་ན་འདི་ལ་འགལ་བ་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 1192]
གཅིག་ཉིད་ཡིན་ན་ཡང་དེ་ནི་དེ་ཉིད་ལས་འདི་ལྟར་བྱེད་པ་པོ༌[^951]མ་ཡིན་པ་ཉིད་ཅེས་བྱ་བ་དེ་ནི་འགལ་བ་ཡིན་ནོ། །

[Block 1193]
གལ་ཏེ་ཐ་དད་ཡོད་དེའི་ཕྱིར། །བྱ་མེད༌[^952]ལྷན་ཅིག་བྱེད་མི་བྱེད། །

[Block 1194]
འོན་ཏེ་ཡང་རྣམ་པ་ཐམས་ཅད་དུ་ཐ་དད་པ་མེད་པར་ནི་མི་སྨྲ་སྟེ། ཐ་དད་པ་ཡང་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1195]
དེ་བས་ན་བྱེད་པ་པོ་འགའ་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1196]
དེ་ལྟར༌[^953]རྣམ་པ་འགའ་ཞིག་གི༌[^954]ཐ་དད་པའི་ཕྱིར་ལྷན་ཅིག་བྱེད་པ་ནི་བྱེད་པ་པོར་མི་འགྱུར་རོ། །

[Block 1197 [VERSE]]
འོན་ཏེ་རིམ་བཞིན་བྱེད་པོ་ཉིད། །
དེ་ཅི་དངོས༌[^955]དེ་ཉིད་ཡིན་ནམ། །

[Block 1198]
འོན་ཏེ་ཡང་འགའ་ཞིག་ཀྱང་བྱེད་པ་པོ་མ་ཡིན་པ་ནི་མེད་པར་འགྱུར་ཏེ། ཐམས་ཅད་ཐམས་ཅད་ལ་གོ་རིམས་བཞིན་དུ་ཉེ་བར་སྦྱོར་བའི་ཕྱིར་རམ། དེར་ཉེ་བར་གནས་པའི་ངོ་བོ་གཞན་ཡོངས་སུ་གྱུར་པའི་ནུས་པ་ཉེ་བར་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 1199]
གཅིག་ནི་ཇི་ལྟར་གོ་རིམས་དེ་ཉིད་ཀྱི་རྟེན་ཅན་ཡིན༌[^956]པའམ། ཐ་དད་པ་མེད་པར་ཡོངས་སུ་གྱུར་པའམ། རྣམ་པ་འགའ་ཞིག་གི་ཁྱད་པར་ཡིན་ན་གཅིག་པ་ཉིད་ཉམས་པའི་ཕྱིར་དེ་ནི་ཅིར་ཡང་མི་རུང་ངོ་། །གཞན་ཡང་།

[Block 1200 [VERSE]]
དེ་ལྡན་དངོས་པོ་ཤིན་ཏུ་ནི། །
ཐ་དད་ཐ་དད་མེད་འགྱུར་བའམ། །
འདྲ་བའི་བདག་ཉིད་ཅན་མེད་ན། །
དེ་དག་ཕན་ཚུན་ཐ་དད་འགྱུར། །

[Block 1201]
གལ་ཏེ་ཐ་དད་པ་མེད་པའི་བདག་ཉིད་དམ།[^957] རང་གི་བདག་ཉིད་དུ་གྱུར་པས་ཐ་དད་པའི་དངོས་པོ་དག་ནི་དེས་ཐ་དད་པ་མེད་པའི་བདག་ཉིད་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་དེ་དང་ལྡན་པར་འགྱུར་བ་ཐ་དད་པར་ཡང་གང་ལས་ཕན་ཚུན་ཐ་དད་པ་ཡིན། སྤྱི་སྟེ་དེ་ནི་དེའི་སྤྱིའི་བདག་ཉིད་མ་ཡིན་ཏེ། དེའི་བདག་ཉིད་དེས་ཀྱང་དེ་ལྟ་བུར་འགྱུར་བར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1202]
དེ་ལྟ་བུའི་ངོ་བོ་ཡིན༌[^958]ན་དེའི་ཆོས་སུ་མི་འགྱུར་ཏེ། གཅིག་པོ་འདི་ནི་འཇུག་པ་དང་ལྡོག་པ་ཅན་གྱི་རང་བཞིན་དུ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1203]
བདག་ཉིད་ཐམས་ཅད་ཀྱིས་ནི་ཐ་དད་པ་མེད་པ་ཁོ་ན་ནི་མ༌[^959]ཡིན་ཏེ། གལ་ཏེ་དེ་ཡང་ཐ་དད་འགྱུར། །འགའ་ཞིག་ལ་ཡང་འདིའི་ཐ་དད་པའམ་ཐ་དད་པ་མེད་པར་ངེས་པ་མ་ཡིན་ཏེ། སྤྱི་དང་ཁྱད་པར་ཞེས་ཐ་དད་པ་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 1204]
གལ་ཏེ་བདག་ཉིད་གང་གིས་དེ།[^960] །

[Block 1205 [VERSE]]
ཁྱད་པར་སྤྱི་ཞེས་བྱ་བ་དེ། །
ཐ་དད་དེ་ཡི་བདག་ཉིད་ཀྱིས། །

[Block 1206]
ཐ་དད་ཉིད་དེ་གལ་ཏེ་སྤྱི་དང་ཁྱད་པར་དག་བདག་ཉིད་གང་ལ་བརྟེན་ནས་སྤྱི་དང་ཁྱད་པར་ཞེས་བྱ་བ་བདག་ཉིད་དེས་ཐ་དད་པ་དེའི་ཚེ་ཐ་དད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1207]
གང་གི་ཕྱིར་དེ་དག་ནི་གལ་ཏེ་དེ་དག་གི་རང་གི་བདག་ཉིད་ཡིན་ན་ཐ་དད་པ་ཅན་དེ་དག་ཐ་དད་པ་ཁོ་ན་ཡིན་ཏེ། སྤྱི་དང་ཁྱད་པར་དག་ནི་རང་བཞིན་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 1208]
རང་གི་ངོ་བོ་ནི༌[^961]དངོས་པོ་ཡིན་ནོ། །

[Block 1209]
དེ་ལྟ་ན།

[Block 1210 [VERSE]]
ཇི་ལྟར་བུམ་སོགས་ཕན་ཚུན་བཞིན། །
སྤྱི་དང་ཁྱད་པར༌[^962]ཅན་མི་འགྱུར། །

[Block 1211]
ཁྱད་པར་དང་སྤྱི་དག་ནི་ཐ་དད་ན་ཡང་ཁྱད་པར་དང་སྤྱི་དང་ལྡན་པ་མ་ཡིན་ལ། སྤྱི་དང༌[^963]ཁྱད་པར་ལྡན་པ་མ་ཡིན་ཏེ། ཕན་ཚུན་འབྲེལ་པ་མེད་པའི་ཕྱིར། །བུམ་པ་ལ་སོགས་པ་བཞིན་ནོ་ཞེས་བཤད་པ་ཡིན་ནོ། །

[Block 1212]
གཞན་ཡང་།

[Block 1213]
བདག་ཉིད་གང་གི་མདུན་བྱས་ནས། །དེས་སྒྲུབ་འབྲས་བུ་འདོད་པ་ཅན། །

[Block 1214]
སྐྱེས་བུ་འདི་ནི་འཇུག་པར་གྱུར།[^964] །

[Block 1215 [VERSE]]
དེ་རྟེན་ཐ་དད་ཐ་དད་མེད། །
དཔྱད་བྱ་རང་བདག་ཉིད་ཐ་དད། །
ལྡོག་པ་མཚུངས་པ་ཉིད་དག་ནི། །
ཡོད་ཉིད་དངོས་པོ་རྗེས་འགྲོ་མེད། །
འཇུག་པ་ལ་སོགས་ཐལ་འགྱུར་ཕྱིར། །
བ་ལང་རྟ་ལས་ཐ་དད་པའམ། །

[Block 1216]
ཐ་དད་པ་མ་ཡིན་ཞེས༌[^965]ཁྱད་པར་མེད་པར་འདྲི་བར་བྱེད་པ༌[^966]ཐམས་ཅད་ཁྱད་པར་ཁོ་ན་ལ་དངོས་པོའི་རང་གི་ངོ་བོ་ཡིན་ན་ཞེས་ལྷག་པར་བྱས་ནས་འཇུག་པར་འགྱུར་ཏེ། དེ་ཉིད་ལ་དེ་སྐད་ཅེས་བརྗོད་ཀྱི། རྫས་ཉིད་ལ་སོགས་པ་ལ་ནི་འདིས་བརྗོད་པ་མ་ཡིན་ཏེ། བདག་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་ཐ་དད་པར་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 1217]
དོན་ལ་ནི་དེར་མ་འཁྲུལ་པའི་ཕྱིར་དེ་ལས་རྟོགས་པར་འགྱུར་རོ། །

[Block 1218]
དེ་དག་ནི་སློབ་དཔོན་གྱིས་དཔྱད་ཟིན་ཏོ། །

[Block 1219]
དེ་བས་ན་འདི་ལ་བ་ལང་ལ་སོགས་པའི་སྒྲ་ཉེ་བར་བྱས་པའི་དོན་ལ་ཐ་དད་པའམ་ཐ་དད་པ་མེད་པ་འདྲི་བར་བྱེད་ཅིང་དོན་གཞན་ཉེ་བར་འགོད་པས་དེ་ལ་བློ་གཉིས་ཅིའི་ཕྱིར་བྱེད། དེའི་ཕྱིར་འདིའི་བདག་ཉིད་གང་ཞིག་གཞན་དང་ཐུན་མོང་མ་ཡིན་པ་འདི་མདུན་དུ་བྱས་ནས་ཁྱད་པར་ཅན་གྱི་དོན་བྱེད་པ་དོན་དུ་གཉེར་བ་སྐྱེས་བུ་འདི་འཇུག་པར་འགྱུར་ཏེ། དཔེར་ན་བ་ལང་ལ་རྨོ་བ་དང་བཞོ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 1220]
གཞན་སྲིད་པའོ། །

[Block 1221]
[^967]དོན་ལ༌[^968]མ་ཡིན་ཏེ། དཔེར་ན་གཡུལ་དུ་འཇུག་པ་ལྟ་བུའོ། །

[Block 1222]
རང་གི་ངོ་བོ་ཉིད་བདག་ཉིད་ཇི་ལྟ་བུའི་སྒྲས་བརྗོད་པ་ཡིན་གྱི། རྫས་ཉིད་ལ་སོགས་པའི་སྤྱི་ནི་མ་ཡིན་ཏེ། དེ་བརྗོད་པ་དེའི་ཚེ་ཐོབ་པར༌[^969]མངོན་པར་འདོད་པ་ཉིད་མེད་པའི་ཕྱིར་དང་། བ་ལང་ལ་སོགས་པ་ལ་རྗེས་སུ་ཞུགས་པའི་ཕྱིར་དང་། དེའི་བདག་ཉིད་དུ་གྱུར་པ་དག་གི་རྗེས་སུ་འགྲོ་བ་དག་མེད་པས་དེ་ལ་གཉི་གའི་ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 1223]
འདི་ལ༌[^970]ཡང་དངོས་པོ་དེ་ཉིད་ལ་ཡང་རྣམ་པ་རྣམས་ཀྱིས་བརྒལ་ཞིང་བརྟག་པ་ཡིན་ནོ། །

[Block 1224]
དེ་ནི་ཐ་དད་པ་ཡིན་ན་ཡང་རྫས་ཉིད་ལ་སོགས་པ་ཐ་དད་པ་མེད་པ་འདི་ལ་འགལ་བ་མེད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1225]
ལྡོག་པའི་མཚན་ཉིད་ཅན་གྱི་སྤྱི༌[^971]དང་ཐམས་ཅད་ལ་རང་གི་ངོ་བོ་ཐ་དད་པ་ཁས་བླངས་པའི་ཕྱིར་རོ། །

[Block 1226]
སྤྱི་རང་བཞིན་དུ་གྱུར་པ་ཐ་དད་པ༌[^972]མེད་པ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 1227]
རང་གི་བདག་ཉིད་ཀྱིས་ཐ་དད་པ་མེད་དུ་ཟིན་ཀྱང་དེའི་རང་གི་ངོ་བོའི་རྒྱུ་ཅན་དོན་བྱེད་པ་དོན་དུ་གཉེར་བ་དག་གི་ནི་གཉི་ག་ལ་མཚུངས་པར་འཇུག་པར༌[^973]འགྱུར་རོ། །

[Block 1228]
གཅིག་ཀྱང་དེའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར། དེ་ནི་དོན་གྱི་བྱ་བ་བྱེད་པ་ཡིན་ལ། དེ་ལས་གཞན་པ་ཡང་དེ་དང་མཚུངས་པའི་ཕྱིར།

[Block 1229 [VERSE]]
དེ་ཡང་ཅིའི་ཕྱིར་མི་བྱེད། །
དེས་ངོ་ཚ་མེད་མཁའ་གོས་ཅན། །
གང་ཅིའང་རིགས་མིན་འཁྲུལ་སྨྲ་བ། །
དེ་དག་ཀྱང་ནི་བསལ་བ་ཡིན། །
མཐའ་གཅིག་པ་ཉིད་སྲིད་ཕྱིར་རོ། །

[Block 1230]
ནམ་མཁའི་གོས་ཅན་འདི་ནི་ཅི་ཡང་མི་རིགས་པ་སྟེ། མི་འཚམ་པ་བླང་བར་བྱ་བ་དང་། དོར་བར་བྱ་བ་མེད་པ་སྟེ༌[^974]ཡོངས་སུ་མཐར་ཕྱིན་པ་མེད་པས་འཁྲུལ་པ་རྔ་མོ་ནི་ཞོར་འགྱུར་ཞིང་མི་འགྱུར་རོ་ཞེས་སྨྲ་བ༌[^975]གང་ཡིན་པ་དེ་དག་ཀྱང་འདི་ཉིད་ཀྱིས་བསལ་བ་ཡིན་ཏེ། ངོ་བོ་ཉིད༌[^976]མཐའ་གཅིག་ཏུ་ཐ་དད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
