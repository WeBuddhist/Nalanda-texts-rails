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

[Block 1231 [VERSE]]
དེའི་རྗེས་སུ་འགྲོ་བ་ཡིན་ན་ཡང་། །
ཐམས་ཅད་གཉི་གའི་ངོ་བོ་ཉིད། །
ཡིན་དེའི་ཁྱད་པར་བསལ་བའི་ཕྱིར། །
ཞོ་འཐུང་ཞེས་ནི་བརྗོད་པ་ན། །

[Block 1232]
ཅིའི་ཕྱིར་རྔ་མོ་ལ་མི༌[^977]རྒྱུག །འདི་ལྟར་རྔ་མོ་ཡང་ཞོར་འགྱུར་ཞིང་དེ་ཉིད་ཀྱང་རྔ་མོ་མ་ཡིན་ཏེ། གང་གིས་གཞན་ཡང་རྔ་མོར་འགྱུར། །དེ་བཞིན་དུ་ཞོ་ཡང་རྔ་མོར་འགྱུར་ལ་དེ་ཉིད་ཀྱང་ཞོ་མ་ཡིན་ཏེ། གང་གིས་གཞན་ཡང་ཞོར་འགྱུར། དེ་བས་ན་འདི་དག་གཅིག་ལ་ཡང་དེའི་ངོ་བོ་འགའ་ཞིག་མེད་པ་མ་ཡིན་པའི་ཕྱིར་དང་། འགྱུར་བ་མ་ཡིན་པའི་རང་གི་ངོ་བོ་ལ་ངེས་པ་མེད་པའི་ཕྱིར། ཁྱད་པར་ཅུང་ཟད་ཀྱང་མེད་པས་ཞོ་འཐུང་ཅིག་ཅེས་བརྗོད་པ་ན་རྔ་མོ་ཡང་ཟོས་པར་འགྱུར་རོ། །

[Block 1233 [VERSE]]
ཅི་སྟེ་ཕུལ་བྱུང་འགའ་ཞིག་ཡོད། །
གང་གི་ཁྱད་པར་འཇུག་འགྱུར་ན། །
དེ་ཉིད་ཞོ་ཡིན༌[^978]དེ་གཞན་ལ། །
མེད་ཕྱིར་མཆོག་ཏུ་གཉི་ག་མེད། །

[Block 1234]
ཅི་སྟེ་འདི་དག་ལ་ཕུལ་དུ་དབྱུང་བ་འགའ་ཞིག་ཡོད་ན་གང་ཞིག་འདི་ལ་འདི་སྐད་དུ་བརྗོད་པ་ན༌[^979]འོ་མའི་རྣམ་པར་འགྱུར་བ་ཁོ་ན་ལ་འཇུག་པར་འགྱུར་གྱི། གཞན་ལ་མ་ཡིན་ནོ་ཞེ་ན། ཕུལ་དུ་བྱུང་བའི་དོན་བྱེད་པ་དོན་དུ་གཉེར་བའི་འཇུག་པའི་ཡུལ་དེ་ཉིད་དེའི་འབྲས་བུའི་ཁྱད་པར་གྱི་ཉེ་བར་ལེན་པའི་ངོ་བོས་མཚོན་པའི་རང་བཞིན་ཅན་ནི་ཞོའི་དངོས་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1235]
དེ་འདྲ་བའི་རང་བཞིན་དེ་ཡང་གཞན་ལ་ཡོད་པ་མ་ཡིན་ཏེ། དོན་དུ་གཉེར་བའི་འཇུག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1236]
དེ་བས་ན་དེ་ལ་གཉི་གའི་ངོ་བོ་མེད་དོ་ཞེས་བྱ་བ་ནི་མཐའ་གཅིག་ཏུ་སྨྲ་བའོ། །

[Block 1237]
གཞན་ཡང་།

[Block 1238 [VERSE]]
ཐམས་ཅད་ཀུན་བདག་ཉིད་ཡིན་ན། །
བློ་སྒྲ་ཐ་དད་པར་མི་འགྱུར། །
ཐ་དད་བསྡུས་པ་སྨྲ་བ་ན། །
དེ་མེད་ཕྱིན་ན་སྲིད་མ་ཡིན། །

[Block 1239]
ནམ་མཁའི་གོས་ཅན་དེ་ནི་ཇི་ལྟར་དངོས་པོ་རྣམས་ཀྱི་རྣམ་པར་དབྱེ་བ་མེད་པའི་ཕྱིར། འགའ་ཞིག་ལ་ཡང་སོ་སོར་ངེས་པའི་རྣམ་པ་གཅིག་མ་མཐོང་བར་རྣམ་པ་གཞན་དང་འདྲེས་པ་མེད་པ་དང་ལྡན་པ་ཅན་གྱི་བློས་དོན་ལ་མོས་པའམ། བརྗོད་པར་འགྱུར། དེ་ལས་ཁྱད་པར་གཟུང་བ་མེད་པའི་ཕྱིར། རྔ་མོ་ཞོར་འགྱུར་ཞིང་མི་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་བསྡུས་པ་སྨྲ་བར་མི་འགྱུར་རོ། །

[Block 1240]
གཞན་ཡང་རྣམ་པ་མ་འདྲེས་པ་བདག་རྟོགས་ནས་སྡུད་པར་འགྱུར་ཏེ། ངོ་བོ་གཅིག་དང་འདྲེས་པ་ཅན་གྱི་བློ་ནི་འགའ་ཞིག་ལ་སོ་སོར་ངེས་པའི་ཕྱིར་རོ། །

[Block 1241]
དེའི་སྣང་བའི་ཁྱད་པར་གྱིས་བྱས་པ་ཉིད་ཀྱི་ངོ་བོ་དེ་དག་ནི་རང་བཞིན་ཐ་དད་པར་ཡང་འགྱུར་ཏེ། གཅིག་དང་དུ་མའི་ཐ་སྙད་ཀྱི་སྣང་བའི་ཡུལ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1242]
དེ་ལྟར་ན་གཅིག་པོ་དེ་གཉི་གའི་ངོ་བོ་ཉིད་དུ་མི་འགྱུར་བ་དེའི་ཕྱིར་དེ་ནི་ལོག་པར་སྨྲ་བ་ཡིན་ནོ། །

[Block 1243]
དངོས་པོ་རྣམས་རང་བཞིན་གྱི་རྗེས་སུ་འགྲོ་བ་འགའ་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ལྟར་གནས་སོ། །

[Block 1244]
ཐ་དད་པའི་མཚན་ཉིད་ཁོ་ན་སྤྱི་ཡིན་ཏེ། འོན་ཀྱང་འགའ་ཞིག་ནི་ངོ་བོ་ཉིད་ཀྱིས་ཤེས་པ་གཅིག་ལ་སོགས་པའི་འབྲས་བུ་ཅན་ཡིན་པ་ལ་འགའ་ཞིག་ནི་མ་ཡིན་ནོ། །

[Block 1245]
དངོས་པོ་རྣམས་ཀྱི་རང་གི་ངོ་བོ་ཐ་དད་པའི་སྤྱི་ཡིན་ཡང་བླ་སྟེ། གང་ནུས་པ་མེད་པ་དག་ལ་ནི་རང་གི་ངོ་བོ་ཉིད་ཡོད་པ་མ་ཡིན་ན། དེ་ལ་ཇི་ལྟར་རང་བཞིན་ཐ་དད་པའི་ཡུལ་ཅན་གྱི་སྒྲ་དག །དེ་དག་ལ་ཡང་གདོན་མི་ཟ་བར་སྒྲ་འཇུག་པར་འགྱུར་ཏེ། རྣམ་པ་འགའ་ཞིག་གིས་ཀྱང་རྣམ་པར་མ་གཞག་པ་དག་ལ་ནི་སྒྲུབ་པ་དང་དགག་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1246]
འདི་ལྟར་ཐམས་ཅད་ལ་མེ་ནི་དྲོ་བའི་རང་བཞིན་ཡིན་གྱི། དྲོ་བ་མེད་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པའི་རྟེན་གྱི་ཐ་སྙད་འདིར་མི་འགྱུར་ཏེ། རང་བཞིན་གཞན་མེད་པ་ལ་ནི་རྣམ་པ་འགའ་ཞིག་གིས་རྣམ་པར་གཞག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1247]
རྣམ་པ་ཐམས་ཅད་དུ་རྟོགས་པ་མེད་པའི་ཕྱིར། མེའི་རང་བཞིན་རྟོགས་པ་མེད་པ་ཞེས་བྱ་བ་ཡིན་ན་ནི། འགྲོ་བ་རྨོངས་པར་འགྱུར་རོ། །

[Block 1248]
དེ་ལྟར་ནི་འགྱུར་ན་དེ་ལ་འགའ་ཞིག་མེད་པ་འགོག་པ་མ་ཡིན་ཏེ། དྲོ་བ་མེད་པ་ཡོད་པ་ཁོ་ན་དོན་གཞན་འགོག་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1249]
ད་ནི་ཇི་ལྟར་ཡོད་པ་དང་མེད་པ་ཡིན་ཞེ་ན། ཐམས་ཅད་མེད་པ་ཉིད་ནི་མི་སྨྲའི། དེ་ལ་མེད་དོ་ཞེའོ། །

[Block 1250]
དངོས་པོ་ཐམས་ཅད་ལ་ནི་ཡུལ་དང་། དུས་དང་། ཆོས་འགོག་པར་བྱེད་པ་ཡིན་གྱི། ཆོས་ཅན་མ་ཡིན་ཏེ། དེ་བཀག་ན་དེའི་ཡུལ་ཅན་གྱི་སྒྲ་འཇུག་པ་མེད་པའི་ཕྱིར་དང་། ཡུལ་མ་བསྟན་པ་ལ་དགག་པའི་སྦྱོར་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1251]
འོ་ན་ཡུལ་ལ་སོགས་པ་དེ་ཡང་ཇི་ལྟར་དགག་པ་ཡིན། འདི་ལྟར་དེ་ལ་ཡང་ཡུལ་ལ་སོགས་པ་བཀག་པ་མེད་ཅིང་དོན་ཡང་མ་ཡིན་ནོ། །

[Block 1252]
གལ་ཏེ་འབྲེལ་པ་བཀག་པ་ཡིན་ནོ་ཞེ་ན།

[Block 1253]
དེ་བཀག་པ་ན་ཡང་བའི་ཕྱིར། །ཉེས་པ་མཚུངས་པ་མ་ཡིན་ནམ། །

[Block 1254]
མེད་པའི་སྒྲ་འཇུག་པར་མི་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པའམ། མེད་པ་འདི་བཀག་པ་ན་དེ་དང་འདྲ་བར་ཆོས་ཅན་ཡང་བཀག་པ་ཡིན་ནོ། །

[Block 1255]
འབྲེལ་པ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བཀག་པ་ནི་མ་ཡིན་ནོ། །

[Block 1256]
འོ་ན་ཅི་ཡིན་ཞེ་ན། འདི་ན་ད་ནི་དེ་ལྟ་བུའི་བུམ་པ་མེད་དོ་ཞེས་བསྟན་པ་ན། འདི་དང་འབྲེལ་པ་ཡོད་པ་མ་ཡིན་པའམ། དེ་དང་ལྡན་པའི་ཆོས་མེད་དོ་ཞེས་རྟོགས་པར་འགྱུར་བ་དེ་ལྟར་འབྲེལ་པ་བཀག་པར་འགྱུར་རོ། །

[Block 1257]
ཇི་སྲིད་འདི་ལ་འབྲེལ་པ་འམ་ཆོས་ཡོད་པ་མ་ཡིན་ནོ་སྙམ་པའི་བློར་མི་འགྱུར་བ་དེ་ལྟ་ན་ཡང་ཇི་ལྟར་བཀག་པ་ཡིན། རྣམ་པ་འགའ་ཞིག་ཡོད་ན་ཡང་འདི་སྲིད་པ་མ་ཡིན་ཏེ། མེད་པ་དག་ལ་དེ་ལྟ་བུའི་ངོ་བོ་མེད་པའི་ཕྱིར་རོ། །

[Block 1258]
དེ་བས་ན་འབྲེལ་པ་མེད་པ་རྟོགས་པ་ལས་འདི་འདི་ན་མེད་དོ་ཞེས་བྱ་བ་དང་པོ་རྟོགས་པ་དེ་ནི་དེ་མེད་པར་མི་འགྱུར་བའམ། དེ་མེད་པ་རྟོགས་པ་ན༌[^980]རྟོགས་པར་འདོད་པ་ཇི་ལྟ་བ་བཞིན་དུ་དེ་ལས་འབྱུང་བ་ཅན་གྱི་སྒྲ་གང་གིས་ཟློག༌[^981]པར་བྱེད། རྣམ་པར་རྟོག་པ་རྣམས་ཀྱི་ཡུལ་མ་ཡིན་པ་གང་ཡིན་པ་དེ་ཉིད་ནི་སྒྲ་རྣམས་ཀྱིས་མ་ཡིན་ནོ། །

[Block 1259]
གལ་ཏེ་དེ་དག་འཇུག་པ་ཡིན་ན་ཚིག་ནི་གང་གིས་འགོག་པར་བྱེད། བརྗོད་པར་བྱ་བ་མ་ཡིན་པའི་དོན་བློ་དག་གིས་དམིགས་པ་མ་ཡིན་ནོ། །

[Block 1260]
འབྲེལ་པ་ཡང་རང་གི་ངོ་བོས་བརྗོད་པ་མེད་པར་བསྟན་ཏོ། །

[Block 1261]
བརྗོད་པ་ཡིན་ན་ནི་འབྲེལ་པ་ཉིད་དུ་བློ་ལ༌[^982]གནས་པའི་ཕྱིར་བསམ་པ་ཇི་ལྟ་བ་བཞིན་རྟོགས་པ་མ་ཡིན་ནོ། །

[Block 1262]
དེ་བས་ན་འདི་རྟོགས་འགྱུར་བ་ཡང་འབྲེལ་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར། རང་གི་ངོ་བོས་བརྗོད་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1263]
དེ་བས་ན་མེད་པ་དང་འདྲ་བར་འབྲེལ་པ་ལ་ཡང་ཐལ་བར་འགྱུར་བ་མེད་དོ།། །།

[Block 1264]
བམ་པོ་དྲུག་པ། གཞན་ཡང་མེད་པ་བརྗོད་པར་བྱ་བར་སྨྲ་བ་འདི་ལ་ལན་འདེབས་པ་ན། མི་སྨྲ་ན་ཇི་ལྟར་ལན་གདབ༌[^983]པར་བྱ། ཚིག་འདི་ལ་ཡང་ཇི་ལྟར་མེད་པ་བརྗོད་པ་མ་ཡིན་ན། [^984]འོན་ཏེ་མེད་པ་ཉིད་མི་འདོད་པ་དེ་བས་ན་བརྗོད་པ་མ་ཡིན། དེ་ཉིད་ན་ནི་མེད་པ་ཡོད་པ་མ་ཡིན་ནོ། །ཞེས་བྱ་བ་ཇི་ལྟ་བ༌[^985]ཡིན། གང་ཡང་དེའི་དོན་བཀག་པ་ན་དོན་མེད་པའི་སྒྲ་མི་སྦྱོར་བའི་ཕྱིར། ཡུལ་མེད་པའི་དགག་པའི་སྦྱོར་བ་མེད་དོ་ཞེས་བྱ་བ་འདི་འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 1265]
དེ་བས་ན་མེད་པ་དག་ལ་སྒྲ་དག་ཀྱང་ཡོད་པར་འགྱུར་རོ། །
--- END BLOCKS ---
