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
[Block 1156]
[^934]གཅིག་གི༌[^935]འཇིག་ན་གནས་པ་ཡི། །བདག་ཉིད་གང་ཡིན་དེ་དེའི་མིན། །

[Block 1157]
གནས་པ་དང་གནས་པ་མ་ཡིན་པ་དག་ནི་རྟེན་གྱི་བདག་ཉིད་གཅིག་ཡིན་ན་ཐ་དད་པ་ཅན་གྱིས༌[^936]ཆོས་གཞན་ཅི་ཞིག་ཡོད། དེ་ལྟར་ན་འགའ་ཞིག་ཏུ་ཡང་སྣ་ཚོགས་པ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 1158]
དོན་དག་རྣམ་པ་ཐམས་ཅད་དུ་ཐ་དད་པའམ་ཐ་དད་པ་མེད་པ་ཉིད་དུ་ཁས་བླངས་པའི་ཕྱིར། མི༌[^937]འགའ་ཞིག་འདོད་པར་མི་འགྱུར་ཞིང་། དངོས་པོ་ཡང་མ་ཡིན་ནོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 1159]
དེ་བས་ན་འདི་ནི་གྲུབ་པ་དང་བདེ་བ་གཅིག་པ་མ་ཡིན་ཏེ། དངོས་པོ་ཐ་དད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1160]
དེས་སྤྱི་ཁྱད་པར་བློར་མི་འགྱུར། །དེ་བས་ན་དོན་གཞན་འདི་ནི་ལྟོས་པ་མེད་པ་ཡིན་ཏེ། མ་བསྐྱེད་པ་ཉིད་ཀྱི་ཕྱིར་འདིའི་སྤྱིའམ་ཁྱད་པར་ཅན་ཞེས་བྱ་བའི་སྒྲ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1161]
གལ་ཏེ་གཞན་སེལ་བ་ལ་ཡང་དེ་མཚུངས་པར་ཐལ་བར་འགྱུར་རོ་ཞེ་ན། མཚུངས་པ་ཡང་མ་ཡིན་ཏེ། འདི་ལྟར།

[Block 1162 [VERSE]]
ལྡོག་པ་ངོ་བོ་ཉིད་མེད་ཕྱིར། །
གནས་དང་གནས་མིན་རྟོག་པ་མིན། །

[Block 1163]
གཞན་སེལ་བ་ཞེས་བྱ་བ་འགའ་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ཡང་རང་བཞིན་གྱི་རྗེས་སུ་སོང་བ་ཅན་རང་བཞིན་དང་གནས་པ་དང་འཇིག་པའི་རྣམ་པར་རྟོག་པ་དག་གིས་རྣམ་པར་རྟོག་པར་མི་འགྱུར་རོ། །

[Block 1164]
སྤྱི་ཡི་བློ་ཡང་བསླད་པ་ཡིན།[^938] །དེ་ཕྱིར་སུན་དབྱུང་བ་ཡང་མེད། །ལོག་པའི་ཤེས་པ་ཅན་འདི་ནི་ཡུལ་མེད་པ་ཅན་ཁོ་ན་ཡིན་ཏེ། དུ་མ་ལ་གཅིག་གི་རྣམ་པ༌[^939]ཅན་ཡིན་པ་དེ་ན༌[^940]ཡུལ་མེད་པའི་ཕྱིར། གནས་པའམ་མི་གནས་པ་མ་ཡིན་ནོ། །

[Block 1165]
གང་ཡང་འདི་སྐད་དུ་དེའི་བསྐྱེད་པ་པོ་ནི་དེའི་རང་བཞིན་ཡིན་ན།

[Block 1166 [VERSE]]
དེ་ཡི་སྐྱེད་བྱེད་ངོ་བོ་གང་། །
དེ་ཡང་ཇི་ལྟར་སྐྱེད་བྱེད་ཡིན། །

[Block 1167]
ཞེས་སྨྲས་པ་དེ་ལ་གཞན་ལ་སྐྱེད་པར་བྱེད་པའི་ངོ་བོ་མེད་དོ་ཞེས་ནི་མི་སྨྲའི། འོ་ན་ཅི་ཡིན་ཞེ་ན། གཅིག་གི་དེ་སྐྱེད་པར་བྱེད་པའི་རང་གི་ངོ་བོ་གང་ཡིན་པ་དེ་ནི་གཞན་གྱི་མ་ཡིན་ནོ་ཞེས་སྨྲའོ། །

[Block 1168]
གཞན་དག་ཀྱང་རང་གི་ངོ་བོ་ཁོ་ནས་སྐྱེད་པར་བྱེད་པ་ཡིན་གྱི་ངོ་བོས་ནི་མ་ཡིན་ཏེ། དེ་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 1169]
དེ་དག་ཀྱང་བདག་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་ངོ་བོ་ཉིད་ཀྱིས་ཐ་དད་པ་དང་དེ་སྐྱེད་པར་བྱེད་པ་འདི་ལ་འགལ་བ་ཅི་ཡོད། ངོ་བོ་གཅིག་དང་བྲལ་བ་ནི་དེའི་ངོ་བོར་མི་འགྱུར་ཏེ། དེའི་འབྲས་བུ་ཅན་མ་ཡིན་པ་མ་ཡིན་ནོ། །

[Block 1170]
དེ་ཉིད་ཀྱང་དེའི་འབྲས་བུ་བྱེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་རིགས་པ་ཅི་ཞིག་ཡོད། གཞན་ཡང་། ཐ་དད་ཁྱད་པར་སྐྱེད་བྱེད་ཡིན། །ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱད་པར་དེ་དག་ཀྱང་བདག་ཉིད་ཀྱི་དེས་ཕན་ཚུན་རྗེས་སུ་འགྲོ་བ་མེད་དེ། གཅིག་གིས་སྐྱེད་པར་བྱེད་པའི་ངོ་བོ་གང་ཡིན་པ་དེ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ཙམ་ནི་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1171]
གལ་ཏེ། དེ་དག་ཐ་དད་མེད་པར་ཡོད། །དེ་ལྟར་འགྱུར་ན་བདེན་ཏེ། ཁྱད་པར་དག་སྐྱེད་པར་བྱེད་པ་ཡིན་གྱི་དེ་དག་ཀྱང་ཁྱད་པར་ཅན་གྱི་ངོ་བོ་ནི་མ་ཡིན་ཏེ། འོན་ཀྱང་ཐ་དད་པ་མེད་པ་ཡང་ཡིན་ནོ། །

[Block 1172]
དེའི༌[^941]ནི་ནུས་པ་གཅིག་དང་ལྡན་པའི་ཕྱིར་སྐྱེད་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1173]
དེས༌[^942]སྐྱེད་བྱེད་པ༌[^943]མིན་པར་བཤད། །སྤྱིའི་ངོ་བོ་ཉིད་དུ་ཟིན་ཀྱང་དེས་དེ་དག་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེ་ལས་འཇིགས་པ༌[^944]མེད་པའི་ཕྱིར་རོ། །

[Block 1174]
གཅིག་ལ་གནས་པས་ཀྱང་འབྲས་བུ་བསྐྱེད་པར་རབ་ཏུ་ཐལ་བའི་ཕྱིར་ཞེས་བཤད་པ་ཡིན་ནོ། །

[Block 1175]
གཞན་ཡང༌[^945]མི་བསྟེན་པའི་སྣང་བ་ཡང་། ཐ་དད་བྱེད་པའི།[^946] ཡང་གི་སྒྲ་ནི་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་ལ་སོགས་པའི་ཁྱད་པར་དག་ཡིན་ནོ། །

[Block 1176]
དོན་ཐམས་ཅད་ཐ་དད་པ་མེད་པར་སེམས་པ་གང་ཡིན་པ་དེ་ནི་འདིར་དོན་དག་ལ་བློའི་སྣང་བ་ཐ་དད་པ་དང་ཆོས་འགལ་བ་གནས་པར་མི་འགྱུར་བའམ། དེ་ལ་ཡོད་ན་ཐ་དད་པ་མེད་པ་ཡིན་ཡང་ཐ་དད་པ་འགའ་ཞིག་ཏུ་ཡང་མི་འགྱུར་རོ། །

[Block 1177]
དེ་ལྟར་ན་གཅིག་གི་བདག་ཉིད་དང་འདྲ་བར་རྣམ་པར་དབྱེ་བ་འདིར་མི་འགྱུར་རོ། །

[Block 1178]
དེ་བས་ཐ་དད་པར་སྣང་བ་ལ་སོགས་པ་འདི་ནི་ཁྱད་པར་ཁོ་ན་ཡིན་ནོ། །

[Block 1179]
འདིར་ཐ་དད་པ་མེད་པའི་སྣང་བ་གཞན་མཐོང་བ་ནི་མེད་མོད་ཀྱི་གང་གི་སྟོབས་ཀྱིས་ཐ་དད་པ་མེད་པའི་ཤེས་པ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1180]
དེ་བས་ན་ཁྱད་པར་དེ་ཉིད་དོན།

[Block 1181 [VERSE]]
དེ་ནི་གཞན་ལས་ལྡོག་པ་ཡིན། །
དེ་ནི་རྒྱུ་དང་འབྲས་བུར་བཤད། །
དེ་ནི་རང་གི་མཚན་ཉིད་འདོད། །
སྐྱེས་བུ་ཀུན་གྱི་འཇུག་པ་ནི། །

[Block 1182]
དེ་སྤོང་ལེན་པའི་འབྲས་ཅན་ཡིན། །དོན་གྱི་བྱ་བ་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་དངོས་ཡིན་ནོ་ཞེས་བཤད་དེ། དེ་ཡང༌[^947]ཁྱད་པར་ཁོ་ན་ཡིན་ཏེ། གང་ཡང་སྤྱི་ཞེས་བྱ་བ་དེ་ནི་དེ་ཉིད་གཞན་ལྡོག་པ་ཡིན་ལ། དེ་ཉིད་དོན་ཉིད་ཡིན་ན་སྣང་བའི་ངོ་བོ་དམིགས་པའི་མཚན་ཉིད་དུ་མི་འགྱུར་བ་རིགས་པ་མ་ཡིན་ཏེ། ཁྱད་པར་དག་ལ་ཐ་དད་པ་མེད་པའི་ཤེས་པས་དེ་དམིགས་པའི་མཚན་ཉིད་དུ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1183]
གཞན་ཡང་།

[Block 1184 [VERSE]]
ཇི་ལྟར་ཐ་དད་མེད་ཁྱད་མེད། །
ན་ཡང་ཐམས་ཅད་ཀུན་སྒྲུབ་མིན། །

[Block 1185]
དེ་ལྟར་ཐ་དད་ཁྱད་མེད་ཡང་།[^948] །ཐམས་ཅད་ཐམས་ཅད་སྒྲུབ་བྱེད་མིན། །འདི་ལྟར་སྐྱེད་པར་བྱེད་པའི་རང་བཞིན་ལས་ཐ་དད་པ་འདི་སྐྱེ་བར་བྱེད་པར་འགྱུར། སྐྱེད་པར་བྱེད་པ་ཉིད་ཡིན་ན་ཡང་ཁྱད་པར་མེད་པའི་ཕྱིར། ཐམས་ཅད་སྐྱེད་པར་བྱེད་པར་འགྱུར་རོ་ཞེས་གང་བཤད་པ་ཡིན་ནོ། །

[Block 1186]
འདིར་བསྟན་ནས། གལ་ཏེ་ཁྱད་པར་མེད་པར་འགྱུར་བ་དེ་ལྟར་འགྱུར་ན་ནི་ཇི་ལྟར་བདག་ཉིད་ཐ་དད་པ་མེད་པར་སྨྲ་བ་འདིའི་ཐ་དད་པ་མེད་པ༌[^949]ཁྱད་པར་མེད་པ་ཡིན་ན་ཡང་ཐམས་ཅད་ཐམས་ཅད་ཀྱིས་སྐྱེད་པར༌[^950]བྱེད་པ་མ་ཡིན་པ་དེ་ལྟར་ཐ་དད་པ་ཁྱད་པར་མེད་པ་ཡིན་ན་ཡང་འགྱུར་རོ། །

[Block 1187]
ཡང་ན།

[Block 1188 [VERSE]]
ཐ་དད་ན་ཡང་འགའ་ཞིག་གིས། །
དངོས་ཆོས་ཉིད་ཀྱིས་བྱེད་པོར་འགྱུར། །
ཐ་དད་མེད་ན་གཅིག་དེ་ཡི། །
བྱ་བ་བྱེད་པ་འགལ་བར་འགྱུར། །

[Block 1189]
ཐ་དད་པ་ཙམ་དུ་ཁྱད་པར་མེད་པ་ཡིན་ན་ཡང་རང་གི་རྒྱུ་དང་རྐྱེན་གྱིས་ངེས་པའི་རང་བཞིན་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1190]
འགའ་ཁོ་ན་བྱེད་པ་པོར་འགྱུར་གྱི་གཞན་ནི་མ་ཡིན་ཏེ། དེའི་རང་བཞིན་ཅན་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

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
--- END BLOCKS ---
