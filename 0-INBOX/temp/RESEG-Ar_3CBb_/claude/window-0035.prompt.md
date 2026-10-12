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
ལ་ལ་ནི་རེག་བྱའི་ལྷ་མོར་གྱུར་ཏེ་བདག་ཉིད་ཀུན་དུ་མཉེས་པར་གྱུར་ཏོ། །

[Block 1227]
ལ་ལ་ནི་སྙོམས་པར་ཞུགས་པའི་ཡུམ༌[^634]དུ་གྱུར་ཏེ་བདག་ཉིད་ཀུན་དུ་མཉེས་པར་གྱུར་ཏོ། །

[Block 1228]
འདི་དག་གི་དུས་སུ་ཡང་རོལ་པ་སྣ་ཚོགས་ཀྱི་གླུ་དང་རོལ་མོ་སྣ་ཚོགས་ཀྱི་གར་དང་། རོལ་པ་སྣ་ཚོགས་ཀྱིས༌[^635]འཕྱང་བ་དང་། རོལ་པ་སྣ་ཚོགས་ཀྱིས་སྒེག༌[^636]པ་དང་། རོལ་པ་སྣ་ཚོགས་ཀྱིས༌[^637]རྩེ་བ་ལ་སོགས་པ་ལ༌[^638]ཀུན་དུ་སྤྱོད་པ་ཡོངས་སུ་སྤྱོད་དོ། །

[Block 1229]
[^639]ད་ནི་སྐུ་གསུམ་ཡང་བཤད་པར་བྱ་སྟེ། ཆོས་ཀྱི་སྐུ་ལ་སོགས་པ་འདི༌[^640]གཅིག་པའམ་ཐ་དད་པར་འགྱུར།[^641] དེ་ལས་ཅིར་འགྱུར་གལ་ཏེ་གཅིག་པ་ཡིན་ན་ནི་སྣང་བ༌[^642]ཉིད་དང་འགལ་བར་འགྱུར་ལ། ཐ་དད་ན་ནི་རིགས་པས་འཁྲུགས་སོ་ཞེ་ན་མ་ཡིན་པའི་ཕྱིར། [^643]སྐུ་གསུམ་དག་ནི་ཞེས་པ་ཆོས་ཀྱི་སྐུ་དང་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་དང་སྤྲུལ་པའི་སྐུའོ། །

[Block 1230]
ཐ་དད་ན་ནི་འགལ་བར་གནས་སོ། །

[Block 1231]
དེ་སུས་བསྟན་ཞེ་ན། སྐྱོབ་པས་བསྟན་ཏེ་སེམས་ཅན་ཐ་དད་པ་ལ་གཞོལ་བའི་དབང་དུ་བྱ་སྟེ་བཅོམ་ལྡན་འདས་ཀྱིས༌[^644]སྐུ་གསུམ་ཐ་དད་པར་བསྟན་ཏོ་ཞེས་བྱ་བ་དྲང་བའི་དོན་ཏོ། །

[Block 1232]
འོ་ན་ངེས་པའི་དོན་དུ་ཇི་ལྟར་བསྟན་ཞེ་ན། རྫོགས་པའི་རིམ་གྱི་སྦྱོར་བ་ཡིས། །ཞེས་པ་ནི་ཆོས་ཀྱི་སྐུ་ལ་སོགས་པའི་ཟུང་འཇུག་སློབ་པའི་རིམ་པས་སོ། །ཅིར་འགྱུར་ཞེ་ན། གཅིག་ཏུ་ཡང་ནི་འགྱུར་བ་ཡིན། །ཞེས་པ་དབྱེར་མེད་དོ་ཞེས་པ་སྟེ། གང་ཞིག་གང་དང་གང་དུ་གཉིས་སུ་མེད་ཅིང་གཉིས་སུ་དབྱེར་མེད་པའི་རང་བཞིན་ཅན་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1233]
གང་ཞིག་སངས་རྒྱས་སྐུའི་མཚན་ཉིད། །ཅེས་པ་ནི་སྒྱུ་མ་ལྟ་བུའི་སྐུའོ། །

[Block 1234]
ཀུན་རྫོབ་ཀྱི་བདེན་པ་ནི་སྣང་བ་ཙམ་དུ་མི་སླུ་བ་སྟེ་རིམ་པ༌[^645]གསུམ་པའོ། །

[Block 1235]
དེ་ཉིད་རྫོགས་པའི་སྦྱོར་གྱུར་པས། །ཞེས་པ་ནི་རིལ་པོར་འཛིན་པ་དང་རྗེས་སུ་གཞིག་པའི་སྦྱོར་བས་སོ། །ཅིར་འགྱུར་ཞེ་ན། འོད་གསལ་པས་ནི་རྣམ་པར་དག །ཅེས་པ། གཅིག་དང་དུ་མ་དང་བྲལ་བར་གྱུར་ཞེས་པའོ། །

[Block 1236]
འདིས་ནི་སྒྱུ་མ་ལྟ་བུ་དེ་ཉིད་འོད་གསལ་བར་འགྱུར་བ་བསྟན་ཏོ། །

[Block 1237]
དེ་ནས་གང་གིས་སྣང་བ་འདི་ཉིད་ཡོངས་སུ་དག་པས་ལྷ་དང་ལྷ་མོར་འགྱུར་རོ་ཞེས་བསྟན་པའི་ཕྱིར། ཚིག་གི་ལམ་གྱི་ཡུལ་འདི་ཉིད། །ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཚིག་གི་ལམ་ནི་ཚིག་གི་བརྗོད་པའི་ཡུལ་ཏེ་སྣོད་དང་བཅུད་ཀྱི་འཇིག་རྟེན་ནོ། །

[Block 1238]
གཙོ་བོ་ནི་ཡབ་རྣམས་སོ། །

[Block 1239]
གཙོ་མོ་ནི་ཤེས་རབ་ཉིད་དེ་དེའི་སྐུར་སྣང་བ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1240]
སེམས་ཅན་ཀུན་ལ་ཕན་བྱའི་ཕྱིར། །ཞེས་པ་ནི་སེམས་ཅན་རྣམས་བྱང་ཆུབ་ལ་སོགས་པའི་ལམ་ལ་དགོད་པའོ། །

[Block 1241]
འཇའ་ཚོན་བཞིན་དུ་སྣང་བ་ཡིན། །ཞེས་པ་ནི་ཕྱོགས་གཅིག་གི་དཔེ་ཉེ་བར་བསྒྲུབས༌[^646]པའོ། །

[Block 1242]
དེ་ནས་སེམས་གསུམ་གྱི་མིང་གི་རྣམ་གྲངས་བསྟན་པ་ནི། །སེམས་དང་སེམས་འབྱུང་མ་རིག༌[^647]པ། །ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ་འདི་དག་ནི་ཤེས་པ་གསལ་བའི་བྱེ་བྲག་གིས་རྣམ་པར་གནས་པར་འགྱུར་བའོ། །ཤེས་རབ་ཐབས་དང་ཞེས་བྱ་བས༌[^648]ནི་བྱེད་པ་ལ་ལྟོས༌[^649]ཏེ་རྣམ་པར་གཞག༌[^650]གོ། །

[Block 1243]
སྟོང་དང་ཞེས་བྱ་བ་བརྗོད་པ་བཤད་པར་བྱ་བའི་ཕྱིར། རང་བཞིན༌[^651]སྣང་བ༌[^652]དབྱེ༌[^653]ཤེས་ནས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རང་བཞིན་ནི་འཁྲུལ་བ༌[^654]ཉིད་དེ་གང་ཞིག་གང་དང་བྲལ་བའི་དུས་ན་འབྱུང་བ༌[^655]དེ་ལ་དེ་སྐད་ཅེས་བྱའོ་སྣང་བ་ནི་བཤད་ཟིན་ཏོ། །

[Block 1244]
དེ་ཤེས་ནས་ཅི་བྱེད༌[^656]ཅེ་ན། དེ་ནས་སྤྱོད་པ་རབ་ཏུ་བྱ། །ཞེས་པ༌[^657]གང་ཞིག་གང་གིས༌[^658]དུས་སུ་གནས་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །དེ་ཅིར་འགྱུར་ཞེ་ན། ལས་ཀྱི་ལུས་ནི་ཡོངས་སྤངས་ནས། །ཞེས་པ་ནི་ཐ་མལ་པའི་ལུས་སྤངས་པའོ། །

[Block 1245]
རྡོ་རྗེའི་སྐུ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་སྟེ། གང་གིས༌[^659]གང་ལ་གནས་ན་གང་ཞིག་གང་དུ་འགྱུར་བ༌[^660]དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1246]
ད༌[^661]ནི་གང་ཞིག་གང་གིས་དུས་སུ་ཇི་ལྟར་བྱ་ཞེ་ན། ཐུགས༌[^662]ལ་འཇིག་རྟེན་པ་རྣམས་ཀྱི། །དོན་སྤྱོད་བཞག་ནས་ཞེས་པ་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བྱའོ་ཞེས་བསམ་པར་བྱའོ། །ཇི་ལྟར་བྱ་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཀུན་རྫོབ་ཏུ། །སྐུ་སྤྲུལ་ནས་ཞེས་སྟོང་པ་ཉིད་ཀྱི་ངང་ལ་སྣང༌[^663]བ་ལ་སོགས་པ་རིམ་གྱིས༌[^664]ལྷའི་སྐུར་ལྡང་བའོ། །

[Block 1247]
ཇི་ལྟ་ཇི་ལྟར་འདོད་ལ་སྤྱོད། །ཅེས་པ་ནི་འདོད་པའི་ཡོན་ཏན་ལྔ་ལ་ཇི་ལྟར་འདོད་པ་བཞིན་སྤྱོད་པའོ། །དེ་ཅིར་འགྱུར་ཞེ་ན།

[Block 1248 [VERSE]]
ཡིད་བཞིན་ནོར་བུ་མཆོག་བཞིན་དུ། །
ཞེས་པ་ནི་དཔེ་བསྟན་པའོ། །
འདོད་པ་ཐམས་ཅད་སྟེར་བར་འགྱུར། །

[Block 1249]
ཞེས་པ་ནི་རང་གང་འདོད་པའི་ཡོན་ཏན་ཐམས་ཅད་འབྱུང་བའོ། །

[Block 1250]
སངས་རྒྱས་རྣམས་ཀྱི་ཕུན་ཚོགས་ཀྱང་། །ཞེས་པ་ནི་སངས་རྒྱས་ཀྱི་ཡོན་ཏན་མ་ལུས་པའོ། །

[Block 1251]
སྟོབས་ཀྱི༌[^665]བླངས་ནས་སྤྱོད་པར་འགྱུར། །ཞེས་པ་ནི་གོང་དང་འབྲེལ་པ༌[^666]ཉིད་དོ། །

[Block 1252]
ད་ནི་གང་ཞིག་གིས་སྤྱོད་པ་ལ་བསླབ་པའི་ཆོ་ག་ཇི་ལྟར་བྱ། དེ་ལས་ཅིར་འགྱུར་ཞེ་ན།

[Block 1253 [VERSE]]
རྣལ་འབྱོར་དབང་པོ་གང་གང་འདོད། །
ཅེས་པ་ནི་གཟུགས་ལ་སོགས་པའོ། །
དེ་དེ་ཐོགས་པ༌[^667]མེད་པར་བྱ། །

[Block 1254]
ཞེས་པ་ནི་དགག་པར་མི་བྱ་ཞེས་པའོ། །ཅིར༌[^668]འགྱུར་ཞེ་ན།

[Block 1255 [VERSE]]
མཉམ་པར་མ་བཞག་རྣལ་འབྱོར་པ། །
རྟག་ཏུ་མཉམ་པར་འཇོག་པར་འགྱུར། །

[Block 1256]
ཞེས་པ་ནི་དེའི་ཡོན་ཏན་བསྟན་ཏོ། །

[Block 1257]
འདི་ཡང་ཁ་ཅིག་འདི་སྐད་ཅེས་ཀྱེ་མ་འདི་ཅི་གང་གིས་གང་ལ་གནས་པ་དེའི༌[^669]དེར་འགྱུར་བ་ཞིག་གམ། དེ་ལས་གཞན་པས་ཀྱང་འགྱུར།

[Block 1258]
དང་པོ་ལྟར་ན་ནི་གང་ཞིག་བྱེད་པ་གང་ཞིག་ཀྱང་བྱེད་པར་འགྱུར་བས་དེས་ཀྱང་དེ་ལྟར་འགྱུར་རོ། །

[Block 1259]
དེ་ལས་གཞན་དུ་ནི་འདི་ལ་ཡང་གནོད་པར་འགྱུར་རོ། །

[Block 1260]
ཕྱི་མ་ལྟར་ན་ཡང་རང་གི་འདོད་པ་ལས་གཞན་དུ་གྱུར་པ༌[^670]ཉིད་དོ་ཞེ་ན་འདི་ཡང་གོང་དུ་བསྟན་པ་ཉིད་དོ། །

[Block 1261]
ཆགས་པ་ལ་དགའ་བའི་རྣལ་འབྱོར་པ་གང་ཞིག་གིས་གང་དུ་ཇི་ལྟར་གནས་པར་ཇི་ལྟར་འགྱུར་ཞེ་ན། རྡོ་རྗེ་པདྨོ་མཉམ་སྦྱོར་བས། །ཞེས་བྱ༌[^671]ནི་ཕོ་དང་མོའི་དབང་པོ་གཉིས་སྙོམས་པར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 1262]
ཡེ་ཤེས་གསུམ་གྱི་ཆ་རིག་པ། །ཞེས་བྱ་བ་ནི་རང་བཞིན་མེད་པའི༌[^672]སྐྱེ་བ་དང་འགག་པའི་བྱེ་བྲག་གི་ཡེ་ཤེས་གསུམ་རིག་པའོ། །

[Block 1263 [VERSE]]
བློ་ལ་གོས་དང་མ་གོས་པ། །
[^673]ཞེས་པ་ནི་གཟུང་བ་དང་འཛིན་པའོ། །
དེར་ནི་བདེ་བར་རྟག་ཏུ་གནས། །

[Block 1264]
ཞེས་པ་ནི་བདེ་བ་ཉིད་ལ་གནས་པའོ་ཞེའོ། །

[Block 1265]
འདི་དག་གི་དོན་ཡང་གང་གིས༌[^674]རང་གི་བདག་ཉིད་ཀུན་དུ་གནས་པར་གྱུར་ནས་གང་དུ་གང་དང་འབྲེལ་པར༌[^675]བྱས་ནས་ཀུན་དུ་བདེ་བའི་རྣམ་པ་ཅན་གྱི་སེམས་དང་པོ་ནི་དེའི་སྐུར་པ་ལ༌[^676]གཟུང་ངོ་། །དེར་ནི་དང་པོ་འཕེལ་བར་འགྱུར་རོ། །
--- END BLOCKS ---
