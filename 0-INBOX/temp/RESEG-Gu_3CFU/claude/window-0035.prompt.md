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
རིང་པོར་མ་སོན་པར་ཐམས་ཅད་ཀྱི་ཐ་མར་ལ་ལའི་ཅུང་ཟད་མ་ལུས་སམ་ཞེས་འཕྲལ་དུ་དྲན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་གནས་བརྟན་ཉིད་དོ། །

[Block 1227]
གསར་བུ་རྣམས་མི་རྒོད་པ་ཉིད་དང་མ་ཁེངས་པ་ཉིད་ལ་དགོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། རྒོད་པ་ནི་ཉེ་བར་མ་ཞི་བའོ། །

[Block 1228]
ཁེངས་པ་ཉིད་ནི་རེངས་པ་ཉིད་དེ་དེ༌[^875]དག་བཟློག་པ་ལ་རབ་ཏུ་དགོད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1229]
ཁྱིམ་ཕྱིར་ཉེ་བ་ནི་ཐམས་ཅད་ཀྱིས་ཐམས་ཅད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་མི་རྒོད་པ་ཉིད་དང་མ་ཁེངས་པ་ཉིད་ལ་དགོད་པར་བྱའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 1230]
འགྲོ་བར་ཆས་པ་ནི་གནས་བརྟེན༌[^876]ཉིད་མ་ཡིན་ཏེ། འོན་ཀྱང་གཞན་ཡང་སྟེ་གསར་དུ་ཞུགས་པ་ཉིད་རྣམས་ནི་མ་ཡིན་ཏེ། འོན་ཀྱང་གཞན་ལ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1231]
ཀུན་ཤེས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་འགྲོ་བར་ཆས་པའི་དགེ་འདུན་གྱི་གནས་བརྟན་ནོ། །

[Block 1232]
དགེ་འདུན་ནི་སྤྱོད་པ་དང་སྤྱོད་ལམ་བརྟན་པ་དང་ལུང་ནོད་པ་ལ་སོགས་པ་དང་ཟས་ཀྱི་རྙེད་པ་དང་ནད་པ་ལ་བགོ་བཤའ་བྱ་བ་ལ་སོགས་པའི་བྱ་བ་བསྒྲུབ་པས་ཕན་གདགས་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སྤྱོད་པ་ནི་ཡུལ་ལོ། །

[Block 1233]
སྤྱོད་ལམ་ནི་སྤྱོད་ལམ་མོ། །

[Block 1234]
དེ་དག་བསྟན་པ་ནི་འདི་ནི་ཡུལ་ལོ། །

[Block 1235]
འདི་ནི་ཡུལ་མ་ཡིན་པ་དེ་ལྟར་འགྲོ་བར་བྱའོ༌[^877]ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1236]
ལུང་ནོད་པ་ལ་སོགས་པ་ཞེས་བྱ་བ་འདི་ལ་ཁ་ཏོན་ལ་སོགས་པ་རྣམས་ནི་སོགས་ཀྱི་སྒྲས་གཟུང་ངོ་། །དབྱར་གནས་པར་ཁས་བླངས་པས་གཙུག་ལག་ཁང་གི་བྱི་དོར་མི་བྱེད་པ་ལ་གྲོས་བཏབ་སྟེ་བྱི་དོར་བྱེད་དུ་གཞུག་ཅིང་བྱི་དོར་བྱེད་པ་ལ་ནི་སྤྲོ་བར་བྱའོ། །

[Block 1237]
ཐམས་ཅད་ཀྱི་འཁོར་དུ་གཏོགས་པ་གཏམ་འདོད་པ་དག་ལ་རྗེས་སུ་མཐུན་པའི་ཆོས་ཉེ་བར་བསྒྲུབ་པས་ཕན་གདགས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དེས་འཁོར་དུ་གཏོགས་པ་རྣམས་གཏམ་འདོད་ན་དེ་ནས་གང་ཞིག་གང་ལ་རྗེས་སུ་མཐུན་པའི་ཆོས་ཉེ་བར་བསྡུས་པས་དེས༌[^878]རྗེས་སུ་གཟུང་བར་བྱའོ། །

[Block 1238]
ཐམས་ཅད་ཀྱིས་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་སོ། །

[Block 1239]
དབྱར་གནས་པར༌[^879]ཁས་བླངས་པའི་དགེ་འདུན་གྱི༌[^880]གནས་བརྟན་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 1240]
མི་སྨྲ་བ་ཉིད་ལ་དགའ་བ་དག༌[^881]བཏང་སྙོམས་སུ་གཞག་སྟེ། སྨྲ་བའི་དངོས་པོ་ནི་སྨྲ་བ་ཉིད་འདིར་མི་སྨྲ་བའི་དངོས་པོ་འཕགས་པ་ཞེས་བྱ་བ་མངོན་པར་འདོད་པ་སྟེ་མི་སྨྲ་བ་ཙམ་ནི་མ་ཡིན་ནོ། །

[Block 1241]
ཁྱིམ་པ་ཉེ་བར་འོངས་པའི་འཚལ་མ་སྦྱོར་དུ་གཞུག་གོ་ཞེས་བྱ་བ་ནི་འདི་རྣམས་ལ་ཁ་ཟས་སྦྱིན་པར་རིགས་པ་ཞེས་བྱ་བའོ། །

[Block 1242]
དགེ་སློང་རྣམས་ལ་གོ་བར་བྱས་ནས་གལ་ཏེ་དགེ་སློང་དེ་རྣམས་ལ་དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་བརྗོད་ཅིང་གོ་བར༌[^882]མི་བྱེད་པའམ་ཁྱིམ་པ་དེ་རྣམས་ཟར་མི་འདོད་ན་དེའི་ཚེ་མི་བྱེད་དམ་མི་འདོད་ན་དེ་དག་ལ་ཆོས་དང་ལྡན་པའི་གཏམ་བྱས་ནས་བདག་ཅག་ལ་འདི་ཡོད་དོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1243]
དེ་དང་ལྡན་པ་ཐམས་ཅད་ཀྱིས༌[^883]འཁོར་ལ་སོ་སོར་བརྟག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་འཁོར་དང་ལྡན་པ་ཐམས་ཅད་མ༌[^884]ཡིན་ཏེ། དགེ་འདུན་གྱི་གནས་བརྟན་ཉིད་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1244]
དོན་མེད་པར་སྤྱོད་པ་ཚར་གཅད༌[^885]དོ་ཞེས་བྱ་བ་ནི་འཁོར་དང་ལྡན་པ་ཐམས་ཅད་ཀྱིས་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 1245]
ཇི་ལྟར་དོན་མེད་པས་དུས་འདའ་བར་མི་བྱེད་པ་དང་རབ་ཏུ་བྱུང་བ་དང་རབ་ཏུ་བྱུང་བ༌[^886]དོན་མེད་པར་ཡང་མི་བྱེད་པ་དེ་ལྟར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1246]
དེ་ལ་འགྲོ་བ་ལ་སོགས་པ་ལ་དེ་ཇི་ལྟ་བ་བཞིན་དུ་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར༌[^887]གནས་པར་བགྱི། ཇི་ལྟར༌[^888]འགྲོ་བར་བགྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཡང་དག་པར་ཞུགས་པ་ལ་ལྟོས་པའི་སོགས་ཀྱི་སྒྲའོ། །

[Block 1247]
དེ་ལ་ཞེས་བྱ་བ་ནི་འཁོར་ལའོ། །

[Block 1248]
དེ་ཇི་ལྟ་བ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་འཁོར་ཇི་ལྟ་བས་དེ་འཁོར་དང་རྗེས་སུ་མཐུན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1249]
གཏམ་སྣ་ཚོགས་དང་འགལ་བ་མེད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་ལ་ཞེས་བྱ་བ་དང་སྦྱར་ཏེ་ཆོས་འདུལ་བ་དང་འགལ་ལོ། །

[Block 1250]
འགལ་བ་མེད་པར་བྱ་བ་ནི་འགལ་བ་མེད་པ་སྟེ། གཏམ་སྣ་ཚོགས་པ་དང་འདྲེས་པའོ། །

[Block 1251]
ཕྱི་བཞིན་འབྲང་བ་དགེ་སྦྱོང་མདུན་དུ་འགྲོ་བར་མི་བྱའོ། །

[Block 1252]
འདུག་པར་མི་བྱའོ་ཞེས་བྱ༌[^889]ནི་སྔོན་དུ་འམ་ཕྱི་ནས་དགེ་སྦྱོང་གིས་འདུག་པར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1253]
སྨྲ་ནས་སྨྲ་བར་བྱ་ཞིང་ཞེས་བྱ་བ་ནི་མི་སྨྲ་བར་ཅུང་ཟད་བརྗོད་པར་མི་བྱའོ་ཞེས་བྱ་བའོ། །

[Block 1254]
བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདི་ལ་མདུན་དུ་དགེ་སྦྱོང་གིས་སྨྲ་བ་དེ་བསྒྲུབ་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1255]
གཏམ་གྱི་བར་ཆད་མི་བྱའོ་ཞེས་བྱ༌[^890]བ་ནི་དགེ་སྦྱོང་བླ་མ་གཏམ་བྱེད་པས་ན་བར་དུ་གཏམ་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1256]
ཆོས་མ་ཡིན་པ་སྨྲ་བ༌[^891]ཞེས་བྱ་བ་ནི་དགེ་སྦྱོང་བླ་མ་སྟེ་བཟློག་པར་བྱའོ། །

[Block 1257]
ཆོས་ཀྱིས༌[^892]རྗེས་སུ་ཡི་རང་བར་བྱའོ། །

[Block 1258]
ཆོས་དང་ལྡན་པའི་རྙེད་པ་བྱུང་ན་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཕྱི་བཞིན་འབྲང་བའི་དགེ་སྦྱོང་ངོ་། །དེ་ནི་ཕྱི་བཞིན་འབྲང་བའི་དགེ་སྦྱོང་གི་ཚུལ་ཁྲིམས་ཡིན་ནོ། །

[Block 1259]
ཁྱིམ་དུ་འགྲོ་བའི་ཚུལ་ཁྲིམས་བརྗོད་པར་བྱ་སྟེ། ཁྱིམ་དུ་མི་རྒོད་པ་དང་མ་ཁེངས་པ་དང་མི་གནས་པར་བྱའོ་ཞེས་བྱ་བ་ལ་མི་རྒོད་པ་དང་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཁྱིམ་དུ་འགྱུར་རོ། །

[Block 1260]
མ་ཁེངས་པ་དང་མི་གནས་པར་བྱ་བ་ལ་ཁྱིམ་ནས་འགྲོ་བར་འདོད་པ་ཉིད་ནི་མི་གནས་པ་ཉིད་དོ། །

[Block 1261]
མིག་དམད་པ་དང་ཁྱིམ་པ་རྣམས་ལ་ཆོས་དང་ལྡན་པའི་གཏམ་བྱའོ་ཞེས་བྱ་བ་ལ། མིག་དམད་པ་ཞེས་བྱ་བ་ནི་ཡུལ་རྣམས་ལས་ཏེ། མིག་སོ་སོར་དམད་པར་བྱས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1262]
ཁྱིམ་པ་རྣམས་ལ་ཆོས་དང་ལྡན་པའི་གཏམ་བྱའོ། །

[Block 1263]
སྦྱིན་པ་དང་དུལ་བ་དང་ཡང་དག་པར་སྡོམ་པ་དང་ཚངས་པར་སྤྱོད་པ་ལ་གནས་པ་དང་གསོ་སྦྱོང་དང་སྐྱབས་སུ་འགྲོ་བ་དང་བསླབ་པའི་གཞི་གཟུང་བ་དག་ལ་དེ་རྣམས་ངེས་པར་སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་རྣམས་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་རྣམས་སོ། །

[Block 1264]
དུལ་བ་ནི་དབང་དུ་བྱེད་པ་སྟེ། དབང་པོ་རྣམས་དང་ལུས་དང་ངག་དག་ལ་དབང་དུ་བྱེད་པ་ཉིད་དོ། །

[Block 1265]
ཡང་དག་པར་སྡོམ་པ་ནི་འདི་རྣམས་ལ་འགྲོ་བ་མེད་པ་སྟེ། འདུལ་བ་དང་འདུལ་བ་ཉིད་ལ་གནས་པའོ། །
--- END BLOCKS ---
