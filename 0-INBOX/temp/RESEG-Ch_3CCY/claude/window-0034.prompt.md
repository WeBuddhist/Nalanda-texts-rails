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
འདིར་རེ་ཞིག་རྣམ་པར་ཤེས་སོ་ཞེས་པས་རྣམ་པར་ཤེས་པ་པོ་ཡོད་དེ། ཕུང་པོ་ལ་བརྟེན་ནས་བརྟགས་པའི་གང་ཟག་བྱེད་པ་པོར་གྱུར་པའོ། །

[Block 1192]
དེ་གང་གིས༌[^864]རྣམ་པར་ཤེས་སོ་ཞེས་དེ་ནི་འདིའི་བྱེད་པ་ཡིན་ལ། གང་ཞིག་རྣམ་པར༌[^865]ཤེས་སོ་ཞེས་དེ་ནི་འདིའི་ལས་སོ། །

[Block 1193]
བྱེད་པ་དང་ལས་མེད་པར་བྱེད་པ་པོ་ཡོད་པར་རིགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་སྟེ། དེས་ན་བྱེད་པ་པོ་ཡོད་པས་ན། དེ་བཞིན་དུ་ཤེས་བྱ་དང་ཤེས་པ་པོ་ཡོད་དོ་ཞེས་བྱའོ། །

[Block 1194]
སྨྲས་པ། གལ་ཏེ་ཤེས་པ་པོ་ཉིད་ཡོད་ན། རྣམ་པར་ཤེས་པ་དང་ཤེས་བྱ་ཡོད་པར་འགྱུར་ན། གང་ཇི་སྲིད་དུ་རྣམ་པར་ཤེས་པ་དང་ཤེས་བྱ་དག་མེད་པས་ལས་དང་བྱེད་པ་དང་བྲལ་བའི་ཕྱིར། བྱེད་པ་པོ་ཉིད་འགའ་ཡང་ག་ལ་ཞིག་ཅེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 1195 [VERSE]]
ཤེས་བྱ་ཤེས་པ་མེད་པའི་ཕྱིར། །
དེ་ཕྱིར་ཤེས་པ་པོ་ཉིད་མེད། །

[Block 1196]
ཅེས་པས། ཤེས་པ་པོ་མེད་པས་ཤེས་པ་དང་ཤེས་བྱ་མེད་དོ་ཞེས་གྲུབ་པོ། །འདིར་སྨྲས་པ། ཕྱི་རོལ་དང་ནང་གི་སྐྱེ་མཆེད་དག་ཡོད་པ་ཉིད་དེ། དེ་དག་མི་རྟག་པར་ཉེ་བར་བསྟན་པའི༌[^866]བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ། འདུས་བྱས་ཐམས་ཅད་མི་རྟག་པའོ་ཞེས་སོ། །

[Block 1197]
གལ་ཏེ་ན་ཡང་ནང་དང་ཕྱི་རོལ་གྱི་བདག་ཉིད་ཀྱི་སྐྱེ་མཆེད་མེད་ན། དེའི་ཚེ་ཅི་གལ་ཏེ་ཐམས་ཅད་མི་རྟག་པར་འགྱུར་ཞེས་བྱ།[^867] དེའི་ཕྱིར་མི་རྟག་པ་ཉིད་བསྟན་པས་དངོས་པོ་ཐམས་ཅད་གྲུབ་བོ་ཞེ་ན། སྨྲས་པ། བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་ཏེ།

[Block 1198 [HEADING]]
### ཚིགས་བཅད་ང་བརྒྱད་པ། ^1-57-0

[Block 1199 [VERSE]]
ཐམས་ཅད་མི་རྟག་ཅུང་ཟད་ཀྱང་། །
མི་རྟག་མེད་ལ་ཡང་ན་རྟག །
དངོས་པོ་ཡོད་ན་རྟག་པ་དང་། །
མི་རྟག་པར་འགྱུར་དེ་ག་ལ། །

[Block 1200]
དེ་ལ་བཅོམ་ལྡན་འདས་ཀྱིས་གང་འདི་སྐད་དུ༌[^868]ཐམས་ཅད་མི་རྟག་གོ་ཞེས་གསུངས་ཞེས་བྱའོ། །

[Block 1201]
དེ་རྣམ་པར་འཇིག་པའི་དངོས་པོའི་རང་གི་མཚན་ཉིད་མཐོང་བ་མིན་ལ། འོན་ཀྱང་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་མ་གཟིགས་ལ། དངོས་པོ་ཐམས་ཅད་ཀྱི་རང་བཞིན་མ་གཟིགས་པས་སྙིང་པོ་མེད་པ་ཉིད་གསལ་བར༌[^869]བྱེད་པ་ལ་ལྟོས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ༌[^870]འདི་ནི་རང་བཞིན་ལ་ལོག་པར་རྟོགས་པ༌[^871]དགག་པའི་དོན་དུའོ། །

[Block 1202]
དོན་དམ་པར་ནི་རྣམ་པར་དཔྱད་ན་མི་རྟག་པ་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 1203]
ཡང༌[^872]རྟག་པའོ། །

[Block 1204]
འདི་དག་གཉི་ག་ཡང་དོན་དམ་པར་མ་གྲུབ་པོ་ཞེས་དགོངས་སོ། །ཅིའི་ཕྱིར་སླར་ཡང་འདི་དག་གཉི་ག་མ་གྲུབ་ཅེ་ན། སྨྲས་པ། གང་གི་ཕྱིར་དངོས་པོར་ཡོད་ན་རྟག་པའམ་མི་རྟག་པར་འགྱུར་ན། དངོས་པོ་དེ་ག་ལ་ཞིག་གོ་སྟེ། ཇི་སྐད་དུ་སྨོས་པའི་རིགས་པས་དངོས་པོ་མེད་པར་བསྒྲུབ་པའི་ཕྱིར་དངོས་པོ་དེ་ག་ལ་ཞིག་པའོ། །

[Block 1205]
དངོས་པོ་དེ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1206]
དངོས་པོ་མེད་པར་གྱུར་པ་ལ་རྟག་པ་ཉིད་དམ་མི་རྟག་པ་ཉིད་ག་ལ་ཞིག །དེའི་ཕྱིར་དངོས་པོ་རྣམས་སྙིང་པོ་མེད་པ་ཉིད་དུ་གསལ་བར་བྱེད་པ་ལ་ལྟོས་ནས་འདི་དག་གསུངས་པ་ཉིད་ལ་རང་བཞིན་མེད་པ་གསལ་བར་བྱེད་པ་ཡིན༌[^873]ནོ་ཞེས་བྱ་སྟེ། རྣམ་པ་ཐམས་ཅད་དུ་ཚིག་འདི་དག་གིས་རང་བཞིན་གསལ་བར་སྒྲུབ་པར༌[^874]བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1207]
ཇི་ལྟར་ཡང་དངོས་པོ་མེད་པས་རྟག་པ་དང་མི་རྟག་པའི་ལོག་པར་རྟོག་པ༌[^875]འབྱུང་བ་མི་སྲིད་པས། དེ་བཞིན་དུ་སྡུག་པ་དང་མི་སྡུག་པ་དག་གི་ཕྱིན་ཅི་ལོག་ཀྱང་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་མེད་པར་གྱུར་པས་འབྱུང་མི་སྲིད་ལ། དེ་མེད་པས་སྡུག་པ་དང་མི་སྡུག་པའི་ཕྱིན་ཅི་ལོག་གི་རྒྱུ་ཅན་གྱི་འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་ཀྱང་མི་རིགས་སོ་ཞེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 1208 [HEADING]]
### ཚིགས་བཅད་ང་དགུ་པ། ^1-58-0

[Block 1209 [VERSE]]
སྡུག་དང་མི་སྡུག་ཕྱིན་ཅི་ལོག །
རྐྱེན་སྐྱེས་ཆགས་སྡང་གཏི་མུག་སྟེ། །
དེ་ཕྱིར་ངོ་བོས་འདོད་ཆགས་དང་། །
ཞེ་སྡང་གཏི་མུག་ཡོད་མ་ཡིན། །

[Block 1210]
དེ་ལ་སྡུག་པ་ཞེས་བརྗོད་པ་ཡིད་དང་མཐུན་པའི་ཕྱིན་ཅི་ལོག་པས་མི་སྡུག་པའོ། །

[Block 1211]
ཕྱིན་ཅི་ལོག་ཀྱང་རྟག་པ་བདག་མེད་པ་གཙང་བའོ་ཞེས་སོ། །

[Block 1212]
དེ་ལ་སྡུག་པ་ལ་བརྟེན་ནས་འདོད་ཆགས་འབྱུང་། མི་སྡུག་པ་ལ་བརྟེན་ནས་ཞེ་སྡང་འབྱུང་ཞིང་། ཕྱིན་ཅི་ལོག་ལ་བརྟེན་ནས་གཏི་མུག་འབྱུང་ངོ་། །དངོས་པོའི་རང་བཞིན་ཡོད་ན་དེ་ལ་སྡུག་པ་ལ་སོགས་པར་རམ། རྟག་པ་ལ་སོགས་པ་ཉིད་དུ་རྟོག་པ་ལས་འདོད་ཆགས་ལ་སོགས་པར་འགྱུར་ན། དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་མེད་པས༌[^876]སྡུག་པ་ལ་སོགས་པ་མེད་པའི་ཕྱིར། དེའི་རྒྱུ་ཅན་གྱི་འདོད་ཆགས་དང་ཞེ་སྡང་དང༌[^877]གཏི་མུག་ཀྱང་ཡོད་པ་མ་ཡིན་ལ། དངོས་པོའི་རང་བཞིན་མེད་པ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་སྡུག་པ་ལ་སོགས་པ་མི་སྲིད་པས་འདོད་ཆགས་ལ་སོགས་པ་མི་རིགས་སོ། །

[Block 1213]
འདི་ལྟར་ཡང་སྡུག་པ་ལ་སོགས་པ་མི་སྲིད་པས་མི་རུང་ངོ་ཞེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 1214 [HEADING]]
### ཚིགས་བཅད་དྲུག་ཅུ་པ། ^1-59-0

[Block 1215 [VERSE]]
གང་ཕྱིར་དེ་ཉིད་ལ་ཆགས་ཤིང་། །
དེ་ལ་ཞེ་སྡང་དེ་ལ་རྨོངས། །
དེ་ཕྱིར་རྣམ་པར་རྟོག་པས་བསྐྱེད། །
རྣམ་རྟོག་དེ་ཡང་དེ་ཉིད་མེད། །

[Block 1216]
འདིར་སྡུག་པ་ཞེས་བྱ་བ་ངོ་བོ་ཉིད་ཀྱིས་མེད་དེ། རྒྱུ་མཚན་ཅིའི་ཕྱིར་ན། གང་གི་ཕྱིར་གང་ཞིག་ཁོ་ན་ཁ་དོག་དང་དབྱིབས་གཞོན་ཤ་ཅན་ལ་སོགས་པ་དང་ལྡན་པའི་དངོས་པོར་གྱུར་པ་གང་ཅི་ཡང་རུང་བ་ལ་འདོད་ཆགས་ཅན་འགའ་ཞིག་ཤིན་ཏུ་ཡིད་དུ་འོང་བར་གྱུར་པ་ལ་སྡུག་པའི་རྣམ་པར་བརྗོད་ལ། དེ་ཉིད་ལ་ཞེ་སྡང་ཅན་འགའ་ཞིག་གིས་མི་སྡུག་པར་བརྗོད་དེ། འདི་ལྟ་སྟེ་ཆུང་མ་གཉིས་ཀྱི་གཟུགས་ལ། ཆུང་མ་དག་ཞེ་སྡང་བ་ལྟ་བུ་སྟེ། གང་ཁོ་ན་ལ་ཁྱོ་ཤིན་ཏུ་ཆགས་པ་དེ་ཉིད་ལ་ཆུང་མ་དག་ཞེ་སྡང་བར་འགྱུར་ལ། དེའི་རང་བཞིན་ཡོངས་སུ་མ་ཤེས་པས་དེ་ལ་འགའ་ཞིག་རྨོངས་པར་འགྱུར་རོ། །

[Block 1217]
དངོས་པོ་གཅིག་ཉིད་སྐད་ཅིག༌[^878]ལ་ཕན་ཚུན་དུ་འགལ་བའི་དོན་དེ་དག་མི་སྲིད་དོ། །

[Block 1218]
དེས་ན་དངོས་པོ་གཅིག་ལ་རང་བཞིན་གསུམ་མི་སྲིད་ལ། རྣམ་པར་རྟོག་པས་དེའི་ཕན་ཚུན་ཐ་དད་པར་རུང་ངོ་། །

[Block 1219]
ཡང་ན་འདི་སྙམ་དུ་སེམས་ན། གལ་ཏེ་ཡང་དངོས་པོ་རྣམ་པ་གསུམ་གཅིག་ཉིད་དུ་མི་འགྱུར་ལ། དེ་ལྟ་ན་ཡང་དེའི་རྣམ་པར་རྟོག་པ་རེ་ཞིག་ཡོད་ལ། དེས་ན་དེ་ཡོད་པས་དེ་ལས་སྐྱེས་པའི་འདོད་ཆགས་ལ་སོགས་པ་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། རྣམ་རྟོག་དེ་ཡང་དེ་ཁོ་ན་ཉིད་དུ་མ་ཡིན་ཏེ། ལོག་པའི་རྣམ་པར་བསྐྱེད་པ་རྣམས་ལ་བདེན་པའི་རང་བཞིན་མི་སྲིད་པ་དང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཕྱིར་ཡང་རྣམ་པར་རྟོག་པ་ཡང་དེ་ཁོ་ན་ཉིད་དུ་མེད་དོ། །

[Block 1220]
དེ་མེད་ན་དེ་ལས་སྐྱེས་པའི་འདོད་ཆགས་ལ་སོགས་པ་ཡང་མེད་དོ་ཞེས་གྲུབ་བོ།། །།

[Block 1221]
འདི་ལྟར་ཡང་རྣམ་པར་རྟོག་པ་དེ་ཁོ་ན་ཉིད་དུ་མེད་པ་སྟེ། གང་གི་ཕྱིར།

[Block 1222 [HEADING]]
### ཚིགས་བཅད་རེ་གཅིག་པ། ^1-60-0

[Block 1223 [VERSE]]
རྟོག་བྱ་མེད་ན་རྣམ་རྟོག་གང་། །
དེ་མེད་རྣམ་རྟོག་ག་ལ་ཞིག །
དེ་ཕྱིར་རྟོག་བྱ་རྐྱེན་སྐྱེ་ཕྱིར། །
སྟོང་ཡིན་རྣམ་པར་རྟོག་པ་ཡང་། །

[Block 1224]
གལ་ཏེ་རྣམ་པར་རྟོག་པར་བྱ་བའི་དངོས་པོ་ཅུང་ཟད་ཡོད་ན་དེ་ལ་རྟོག་པར་བྱེད་པ་རྣམ་པར་རྟོག་པ་སྐྱེ་ལ། དེ་ཡང་དངོས་པོ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་ལ། དེས་ན་དེ་ལ་རྣམ་པར་རྟོག་བྱ་མེད་ན་རྣམ་རྟོག་མེད་དོ་ཞེས་བྱ་སྟེ། སྟོང་ཡིན་རྣམ་པར་རྟོག་པ་ཡང་། །གལ་ཏེ༌[^879]རྣམ་པར་རྟོག་པར་བྱ་བའི༌[^880]རང་བཞིན་སྟོང་པའོ། །

[Block 1225]
དེ་ལས་དངོས་པོ་གང་ཡང་རུང་བའི་རང་བཞིན་མི་དམིགས་པས། རྣམ་པར་རྟོག་བྱ་དང་རྟོག་པ་དག་ཏུ་ཡོངས་སུ་མི་རྟོག་པའི་ཕྱིར་དེ་ཁོ་ན་ཉིད་རྟོག་པར་འགྱུར་རོ། །

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
--- END BLOCKS ---
