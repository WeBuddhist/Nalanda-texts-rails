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
[Block 1996]
[^1202]དགོས་པའི་དབང་གིས་ཞེས་བྱ་བ་ནི༌[^1203]དགོས་པ་ལ་རྗེས་སུ་དགའ་བའོ། །

[Block 1997]
སྦྱིན་པ་ལ་ཆགས་ཤིང་ཞུགས་པ་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་ལ༌[^1204]དགའ་བ་ཉིད་དུ༌[^1205]ཞུགས་པ་ཡིན་ཏེ། ཞེན་པ་ཉིད་དུ༌[^1206]ཞུགས་པ་སྟེ། གཏོང་བར༌[^1207]དཀའ་བ་དེས་སེམས་ཟིལ་གྱིས་གནོན་པ་ལ་གནས་པས། སྦྱིན་པ་ལ་ཆགས་ཤིང་ཞུགས་པ་འདི་ལྟར་ཤེས་པའོ། །

[Block 1998]
གང་གི་འགྲམ་པ་བུང་བ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་གྱི་ལན་ནི་ཚུལ་གྱི་རིམ་པ་ལ་མི་ལྟ་བ་ཞེས་བྱ་བ་འདི་ཡིན་ནོ། །

[Block 1999]
ཚུལ་དང་འགལ་བའི་ལམ་དུ་སོང་བ་འདིས་ཞེས་བྱ་བའི་ལན་ནི། རྒྱལ་སྲིད་ལ་དབང་བྱེད་དུ་བཅུག་པ་ནི༌[^1208]དེ་ལྟར་བྱ་བ་ཡང་མི་རིགས་སོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 2000]
རྒྱལ་པོའི༌[^1209]དཔལ་ནི་ཇི་ལྟར་འགོ་བར་འགྱུར། །ཞེས་བྱ་བའི་ལན་ནི། འདིས་ཀྱང་རང་གི་གླང་པོ་ཆེ་བྱིན་ཟིན་པས་སྒྱུགས་པ༌[^1210]འདྲ་བ་ལྟ་སུ་ཞིག་འཕྲོག་པར་བྱེད་ཅེས་བྱ་བ་ཡིན་ནོ། །

[Block 2001]
འདི་ནི་ཡལ་བར་བོར་ན་ཁྱོད་ལ་གནོད། །ཅེས་བྱ་བའི་ལན་ནི་སུ་ཞིག་སླར་འཕྲོག་ཅེས་བྱ་བ་སྟེ། འདི་ལ་རང་གི་གླང་པོ་ཆེ་བྱིན་པ་ནི་སྐྱུགས་པ་དང་འདྲ་བར་ལྟོས་པ༌[^1211]མེད་པར་བཏང་བ་དེ་ལ་གཞན་སུ་ཞིག་འཕྲོག་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2002]
འོན་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བཅོར་མེད་པ་ཉིད་དུ་བརྟགས་ཤིང་བཟུང་ནས་བྱ་བ་གཞན་གྱིས་བསྟན་པའི་ཕྱིར་བརྩམས་སོ། །

[Block 2003]
རྒྱལ་པོ་ཆེན་པོ་ཐམས་ཅད་སྒྲོལ་འདི་ནི་དོན་འདི་ལྟ་བུ་དག་ལ་གཏམས་པ་ཙམ་གྱིས་མཆིས་སུ་འཚལ་བ་མ་ལགས་སོ༌[^1212]ཞེས་བྱ་བ་འདིས་ནི་གླང་པོ་ཆེ་སླར་ཕྲོགས་ན་དེ་རིགས་པ་ཉིད་དུ་མངོན་པར་ཁས་ལེན་པ་ཡིན་ནོ། །

[Block 2004]
སྐྱོན་མ་ཡིན་པ་སྐྱོན་དུ་བཟུང་བའི་སྐྱོན་གང་ཡིན་པ་དེ་ཉིད་ནི་ཡོན་ཏན་ལ་སྨོད་པའོ། །

[Block 2005]
ཡང་ན་ཁྱེད་ཅག་གི་ས་སྐྱོན་དུ་བཟུང་བ༌[^1213]བྱས་པའོ། །

[Block 2006]
བདག་གི་བུ་ཞེས་བྱ་བ་ནི་གཞན་དག་ལ་ཡང་འདི་ལྟ་བུའི་བྱ་བ་སྟེ། གསད་པ༌[^1214]དང་། བཅིང་བ་དང་། རྡེག་པ་མི་བྱེད་པ་ཡིན་ན། ཇི་ལྟར་བདག་གི་བུ་ལ་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2007]
བཅིང་ངམ་རྡེག་པར་ཞེས་བྱ་བ་ནི་རྡེག་པ་མ་བསྟན་པའི་ཚིག་གིས་འཁྲུག་པ་བསྐུལ་བ་དེའི་ཚིག་བསྟན་ཏོ། །

[Block 2008]
ཁྱོད་ཀྱི་སྲས་ཞེས་བྱ་བ་ནི་འཁྲུག་པའི༌[^1215]ཚིག༌[^1216]ཉིད་དོ། །

[Block 2009]
གཟི་ཆེ་ཞེས་བྱ་བས་ནི་སྤྲོ་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2010]
འཁོར་གསུམ་བསྟན༌[^1217]ལ་མཁས་ཤིང་ཞེས་བྱ་བ་འདིས་ནི་གསང་ཚིག་གི་ནུས་པ་བསྟན་པ་སྟེ། ཆོས་དང་། དོན་དང་། འདོད་པ་ནི་གཅིག་ལ་གཅིག་འགལ་བ་བསྟན༌[^1218]པར་འཁོར་གསུམ་བསྟན་པ༌[^1219]ལ་མཁས་པར་གྱུར་ཏོ།[^1220] །ཆོས་ལ་རབ་ཏུ་དགའ་བས་ཞེས་བྱ་བ་ནི་སྤྲོ་བའི་ནུས་པ་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2011]
ཚུལ་ལ་མི་ལྟ་ཞེས་བྱ་བས་ནི་གསང་ཚིག་གི་ནུས་པ་ཉམས་པར་བསྟན་ཏོ། །

[Block 2012]
གང་གི་ཕྱིར་ཆོས་དང་དོན་དང་འདོད་པ་ལྷག་པར་བསྟན་པས༌[^1221]ནི་རང་བཞིན་གྱིས་གཞན་འགོག་པར་བྱེད་དོ་ཞེས་བྱ་བའི་བསྟན་བཅོས་ཀྱི་ཚིག་གིས་དེའི་ཚིག་དང་འགལ་ལོ། །

[Block 2013]
ཚུལ་ལ་ལྟོས་པ༌[^1222]མེད་པ་དེས། །འདི་ནི་དཀའ་ཐུབ་ནག་ས༌[^1223]ན་གནས་པར་འོས། །ཞེས་བྱ་བ་འདིས་ནི་གཙོ་བོའི་ནུས་པ་མེད་པར་བསྟན་ཏེ། ཚུལ་ལ་ལྟོས་པ༌[^1224]མེད་པའི་ཕྱིར་རོ། །

[Block 2014]
འདི་ལ་ཅིའི་ཕྱིར་སྤྱུགས༌[^1225]པའི་རྒྱུ་བསྟན་པ་འདིའི་དབང་དུ་བྱས་པ་ནི། ས་ཡི་བདག་པོ་རྣམས་ཀྱི་ཚུལ་ཉེས་སྐྱོན། །ཞེས་བྱ་བའོ། །

[Block 2015]
མོད་ཀྱི་ཞེས་བྱ་བ་ནི་དེ་ལྟ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2016]
ཚུལ་ཉེས་སྐྱོན་ཞེས་བྱ་བ་ལ། ཚུལ་ངན་པའི་སྐྱོན་གང་ཡིན་པ་དེ་ནི་ཚུལ་ཉེས་སྐྱོན་ནོ། །

[Block 2017]
དེ་ལ་བརྟེན་པ་རྣམས་ལ་ཞེས་བྱ་བ་ནི་རང་བཞིན་གྱིས་སོ། །

[Block 2018]
བཅོས་སུ་རུང་བ་མཆིས་པ་ནི་བཅོས་སུ་བཟོད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2019]
བཟོད་པ་གང་དག་གི༌[^1226]ཡིན་ཞེ་ན། དེ་དག་དེ་ལ་བརྟེན་པ་རྣམས་ཞེས༌[^1227]བྱ་བ་སྟེ་ཚུལ་ཉེས་པའི་སྐྱོན་དེ་དག་གོ། །

[Block 2020]
དེ་ལ་བརྟེན་པ༌[^1228]ལ་ལྟ་བ་གང་དག་ཡིན་ཞེ་ནས་བདག་རྣམས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། གཙོ་བོ་ཉམས་ན་ཉམས་པའི་ཕྱིར་རོ། །

[Block 2021]
གང་གི་ཕྱིར་རྩ་བར་གྱུར་པའི་རྒྱལ་པོ་དེ་ཉམས་ནའོ། །

[Block 2022]
འདི་སྐད་སྟོན་པ་ཡིན་ཏེ། རྒྱལ་པོའི་ཚུལ་ཉེས་པའི་སྐྱོན་ནི་དེ་ལ་བརྟེན་པ་རྣམས་ལ་འབྱུང་མོད་ཀྱི། འོན་ཀྱང་བཅོས་སུ་རུང་བར་སྣང་ངོ་། །གང་གི་ཕྱིར་གཙོ་བོ་ཉམས་ན་ནི་དེའི་ཚུལ་ཉེས་པ་དེའི་སྐྱོན་བཅོས་པར་མི་ནུས་ཞེས་སྟོན་ཏེ། གཙོ་བོ་ཉམས་ན་དེ་ལ་བརྟེན་པ་རྣམས་ཀྱང་ཉམས་པར་འགྱུར་རོ། །

[Block 2023]
དེས་ན་འདི་ཉིད་ཚུལ་ཉེས་པའི་སྐྱོན་རྒྱལ་པོ་ལ་བྱུང་ན་དེ་ལ་བརྟེན་པ་རྣམས་ཀྱིས་བཅོས་པར༌[^1229]མི་ནུས་པར་སྣང་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་རྩ་བར་གྱུར་པའི་གཙོ་བོ་ཉམས་པའི་ཕྱིར་རོ། །

[Block 2024]
དེའི་ཕྱིར་དེ་དག་གི་ནི་གསོ་བ་ཉིད་དུ་འགྱུར་གྱི་གང་གི་ཕྱིར་དེ་ཉམས་ན་ནི་གང་གིས་གསོ་བར་འགྱུར་ཞེས་བྱའོ། །

[Block 2025]
སྲིད་ཉམས་མི་བཟོད་ཅེས་བྱ་བ་ནི་ཁྱོད་ཀྱི༌[^1230]སྲིད་ཉམས་པ་འམ་འཇིག་པར་མི་བཟོད་པ་གང་ཡིན་པ་དེ་ནི་མི་བཟོད་པའོ། །

[Block 2026]
ཡང་ན་མི་བཟོད་པ་གང་ལ་ཡོད་པ་དེ་མི་བཟོད་པ་སྟེ། ཁྱོད་ཀྱི་སྲིད་ཉམས་མི་བཟོད་པའོ། །ཅིའི་ཕྱིར་གཏང་བ༌[^1231]ཡིན་ཞེ་ན། སྨྲས་པ་དཀའ་ཐུབ་འཕེལ་བ་ཞེས་སྨོས་སོ། །

[Block 2027]
ཅིའི་ཕྱིར་དེ་ཉིད་དུ་དཀའ་ཐུབ་འཕེལ་བར་འགྱུར་ན་གྲུབ་པས་བསྟན་པའི༌[^1232]ཕྱིར་རོ། །

[Block 2028]
བྱམས་ཤིང་སྤོབས་པ་དང་ཡིད་གཅུགས༌[^1233]པའི་དབང་གིས་ཞེས་བྱ་བ་ལ། བྱམས་པ་ནི་དགའ་བ་དང་བདག་པོ་དང་འབྲེལ་པ་མེད་པས་བྱམས་པའི་བདག་གིར་བྱེད་བའོ། །

[Block 2029]
ཡིད་གཅུགས་པ༌[^1234]ནི་ཉེས་པར་དོགས་པ་མེད༌[^1235]པས་སོ། །

[Block 2030]
ཚུལ་མ་ཡིན་པས་ཞེས་བྱ་བ་ནི། བསྟན་ངག༌[^1236]གི་བསྟན་བཅོས་ལམ་ལོག་པ་ཡིན་པའི་ཕྱིར་ཚུལ་མ་ཡིན་པས་སོ། །

[Block 2031]
དེའི་རྒྱུ་ཅན་གྱི་ཕན་པ་མ་ཡིན་པར་འགྱུར་བ་ནི་ཉམས་པར་དོགས་པ་ཞེས་སྨོས་པ་སྟེ། ཕན་པ་མཆོག་ཏུ་བྱེད་པ་དེ་ལའོ། །

[Block 2032]
ལྷ་རྒྱལ་སྲིད་ཀྱི་དཔལ་འདི་ལྟར་ཚབ་བཙལ་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་བྱམས་པའི་དབང་གིས་བསྟན་ཏོ། །

[Block 2033]
ལྷ་ཅི་མི་མཁྱེན་ནམ༌[^1237]ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སྤོབས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 2034]
ཚུལ་དང་འགལ་བའི་ལམ་ཞེས་བྱ་བ་འདི་དང་། རྒྱལ་པོ་ཆེན་པོ་ཐམས་ཅད་སྒྲོལ་འདི་ནི་དོན་འདི་ལྟ་བུ་དག་ལ་ཞེས་བྱ་བ་འདི་ནི་ཡིད་གཅུགས༌[^1238]པའི་དབང་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2035]
གྲགས་པ་ཐོབ་པ་སེང་གེའི་ཁྲི་ལ་འོས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་འདིར་མཐོང་བའི་འབྲས༌[^1239]བུ་བསྐྱེད༌[^1240]པའོ། །
--- END BLOCKS ---
