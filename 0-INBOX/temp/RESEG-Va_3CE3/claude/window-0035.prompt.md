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
དེ་བཞིན་ཉིད་དེ་ཡང་ཆོས་ཉིད་གཞན་གང་གི་རྒྱུ་ཡང་མ་ཡིན་པའི་ཕྱིར་རང་བཞིན་མ་ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 1227]
དེ་བཞིན་ཉིད་དེ་འདུས་མ་བྱས་པའི་ཕྱིར་སུས་ཀྱང་མ་བྱས་པས་མ་བྱས་པ་ཞེས་བྱའོ། །

[Block 1228]
དེ་ཉིད་བསོད་ནམས་དང་བསོད་ནམས་མ་ཡིན་པ་མངོན་པར་འདུ་བྱེད་པ་གང་གིས་ཀྱང་མངོན་པར་འདུ་མ་བྱས་པའི་ཕྱིར། མངོན་པར་འདུ་མ་བྱས་པ་ཞེས་བྱའོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་སུས་ཀྱང་མ་མཐོང་མ་ཐོས་མ་རྟོགས་རྣམ་པར་མ་ཤེས་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི༌[^860]དམིགས་པ་དང་། དམིགས་པར་བྱ་བ་མཉམ་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་མཐོང་བ་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པ་རྣམ་པར་རྟོག་པ་དང་བཅས་པ་དེ་ལྟ་བུ་དག་གི༌[^861]སྤྱོད་ཡུལ་དུ་གྱུར་པ༌[^862]མ་ཡིན་པའི་ཕྱིར་རོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་བསམ་གྱིས་མི་ཁྱབ་པའོ་ཞེས་བྱ་བ་ནི་དུ་བས་མེ་མཚོན་པ་ལྟར། ཆོས་གཞན་གྱིས་བསམ་དུ་མི་ནུས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1229]
དེ་བས་ན་གཟུགས་ཀྱིས་མ་ཤེས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1230]
ཆོས་ཐམས་ཅད་དམིགས་སུ་མེད་པར་བྱེད་པའོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་དམིགས་སུ་མེད་པའི་མཚན་ཉིད་དུ་ཤེས་པར་བྱེད་པའོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ༌[^863]ཇི་ལྟར་སྤྱད་པར་བགྱི་ཞེས་བྱ་བ་ནི་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ལའོ། །

[Block 1231]
རང་བཞིན་ཤེས་པས་ཆོས་ཐམས་ཅད་ལ་སྤྱོད་ན་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པ་མ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར། གཟུགས་ལ་མི་སྤྱོད་ན་ཞེས་བྱ་བའི་འགྲེས་སོ། །

[Block 1232]
ལྷག་མཐོང་གི་ཤེས་པས་ཆོས་ཀྱི་མཚན་ཉིད་ལ་སྤྱོད་ན་སྤྱོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་བསྟན་པའི་ཕྱིར་འགྲེས་གཉིས་པའོ། །

[Block 1233]
གཟུགས་ཡོངས་སུ་རྫོགས་པའམ་ཡོངས་སུ་མ་རྫོགས་པ་ཞེས་བྱ་བ་ནི་སྒོམ་པ༌[^864]ཡོངས་སུ་རྫོགས་པ་ལས་དགོངས་ཏེ་གསུངས་པའོ། །

[Block 1234]
གཟུགས་མ་ཆགས་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཉིད་ཀྱི་གཟུགས་སྒྲིབ་པ་མེད་པའོ། །

[Block 1235]
དེ་ལྟར་སྤྱོད་ན་གཟུགས་ཆགས་པ་མེད་པ༌[^865]ཞེས་བྱ་བར་འདུ་ཤེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་སྒྲུབ་པའི་ཚེ་དེ་ལྟར་ཞུགས་ན་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཁོང་དུ་ཆུད་པའི་ཚེ་དེ་ལྟར་རབ་ཏུ་རྟོགས་པ༌[^866]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1236]
རབ་འབྱོར་ངོ་མཚར་དུ་གྱུར་པའི་ཚིག་དང་། དགེ་སློང་ཞིག་གི་ཚིག་དང་། བརྒྱ་བྱིན་གྱི་ཚིག་དང་། བསྲུང་བ་དང་བསྐྱབ་པ་དང་། སྦ་བ་དང་། མི་ནུས་པའི་ཚིག་རྣམས་ནི་ཐམས་ཅད་ཀྱང་འདྲའོ། །

[Block 1237]
གཟུགས་རློམ་སེམས་སུ་མི་བྱེད་ཅེས་བྱ་བ་ནི་བྱེད་པ་དང་། མཚན་ཉིད་ལ་སོགས་པའི་དངོས་པོར་རོ། །

[Block 1238]
གཟུགས་བདག་གི་ཞེས་བྱ་བར་རློམ་སེམས་སུ་མི་བྱེད་དོ་ཞེས་བྱ་བ་ནི་རྗེ་ཁོལ་གྱི་དངོས་པོར་རོ། །

[Block 1239]
གཟུགས་ལ་རློམ་སེམས་སུ་མི་བྱེད་ཅེས་བྱ་བ་ནི་གནས་དང་རྟེན་པའི༌[^867]དངོས་པོར་རོ། །

[Block 1240]
གཟུགས་ཀྱི་མཚན་མར་ཡང་རློམ་སེམས་སུ་མི་བྱེད་ཅེས་བྱ་བ་ནི་བརྡར་བཏགས་པའི༌[^868]དངོས་པོར་རོ། །

[Block 1241]
སངས་རྒྱས་སྟོང་བསྟན་པ་ནི་དེ་དག་དེ་ལ་དད་པའི༌[^869]ཕྱིར་རོ། །

[Block 1242]
བྱམས་པས་ཆོས་བཤད་པ་ཞུས་པའི་དུས་གསུམ་ཆར་དུ་ཡུན་འདི་ཉིད་བཤད་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1243 [HEADING]]
##### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཤིན་ཏུ་ཡོངས་སུ་དག་པ། ^1-2-5-4-0

[Block 1244]
དེའི་འོག་ཏུ་རབ་འབྱོར་གཟུགས་ཡོངས་སུ་དག་པའི་ཕྱིར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་དག་པའོ་ཞེས་བྱ་བ་ནི་གཟུགས་ལ་སོགས་པའི་ཆོས་དམིགས་པར་གྱུར་པ༌[^870]རྣམས་དྲི་མ་མེད་པར་གྱུར་པས༌[^871]ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་དེ་ཡང་རྣམ་པར་དག་པར་འགྱུར་རོ། །

[Block 1245]
རབ་འབྱོར་གཟུགས་ལ་སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པ་དང་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་དང་། རྣམ་པར་བྱང་བ་མེད་པ་ཞེས་བྱ་བ་ནི་གང་གི་ཚེ་གཟུགས་ཆོས་ཉིད་ཀྱི་རང་བཞིན་དུ་གནས༌[^872]གྱུར་ནས་སྐྱེ་བ་དང་འགག་པ་དང་ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བར་མི་སྣང་བ་དེའི་ཚེ་གཟུགས་དེ་ཡོངས་སུ་དག་པ་ཞེས་བྱའི༌[^873]གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 1246]
ནམ་མཁའ་ཡོངས་སུ་དག་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ནམ་མཁའ་ལ་གློ་བུར་གྱི་སྤྲིན་དང་ཁུག་རྣ་ཡོད་ཀྱང་དེ་རང་བཞིན་གྱིས་དག་པའི་ཕྱིར་ཡོངས་སུ་དག་པ་མ་ཡིན་པར་མི་འགྱུར་ཏེ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་དེ་བཞིན་ནོ་ཞེས་བསྟན་པའོ། །

[Block 1247]
ཡོངས་སུ་དག་པ་དང་གོས་པ༌[^874]མེད་པ་དང་། འཛིན་པ་མེད་པ་དང་། སྨྲ་བ་མེད་པ་དང་། རབ་ཏུ་བརྗོད་པ་མེད་པ་དང་། དམིགས་སུ་མེད་པའི་ཕྱིར་རྣམ་པ་དྲུག་གིས་ནམ་མཁའ་དང་མཚུངས་པར་བསྟན་ཏོ། །

[Block 1248]
ནམ་མཁའ༌[^875]སྨྲ་བ་མེད་པའི་ཕྱིར་ཞེས་བྱང་ནི་ནམ་མཁའ་ལ་དེ་ལས་གཞན་པ་རྣམས་སྨྲ་ཡང་། ནམ་མཁའ་ལ་ནི་སྨྲ་བའམ། མངོན་པར་བརྗོད་པ་མེད་དོ། །

[Block 1249]
དཔེར་ན་ནམ་མཁའ་ལ་བྲག་ཅ་གཉིས་ཀྱི་སྒྲ་གྲག་ཀྱང་། ནམ་མཁའ་ནི་སྨྲ་བ་དང་བཅས་པའོ་ཞེས་བརྗོད་དུ་མི་རུང་བ་ལྟ་བུའོ། །

[Block 1250]
ནམ་མཁའ་རབ་ཏུ་བརྗོད་པ་མེད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ནམ་མཁའ་ལ་ངོ་བོ་ཉིད་ཀྱིས་རབ་ཏུ་བརྗོད་པ་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1251]
ཡང་སྒྲ་ཙམ་ནི་སྨྲ་བའོ། །

[Block 1252]
མངོན་པར་བརྗོད་པའི༌[^876]རབ་ཏུ་བརྗོད་པའོ། །

[Block 1253]
རབ་འབྱོར་གཟུགས་ཤིན་ཏུ་རྣམ་པར་དག་པ་དང་། དམིགས་སུ་མེད་པ་དང་། སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པ༌[^877]དང་། ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་དང་། རྣམ་པར་བྱང་བ་མེད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་གང་གི་ཚེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདིས་ཆོས་ཐམས་ཅད་མཐོང་སྟེ། གཟུགས་ལ་སོགས་པའི་ཀུན་བརྟགས་པའི་ཉོན་མོངས་པ་དང་། རྣམ་པར་རྟོག་པ་སྤྲོས་པའི་དྲི་མ་མེད་པའི་ཕྱིར། རྣམ་པར་དག་པའི་རྣམ་པ་དང་། དམིགས་པ་ཐམས་ཅད་དང་བྲལ་བའི་ཕྱིར། དམིགས་སུ་མེད་པའི་རྣམ་པ་དང་། ཡོངས་སུ་གྲུབ་པའི་ཕྱིར་སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པའི་རྣམ་པ་དང་། རང་བཞིན་གྱིས་དབེན་པའི་ཕྱིར་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་དང་། རྣམ་པར་བྱང་བ་མེད་པའི་རྣམ་པར་མཐོང་བ༌[^878]དེའི་ཚེ་བདག་ཉིད་ཡོངས་སུ་དག་པ་ཞེས་བྱ་བའི་མིང་དུ་འགྱུར་རོ། །

[Block 1254 [HEADING]]
##### ཚེ་འདི་དང་ཚེ་ཕྱི་མ་ལ་འབྱུང་བའི་ཕན་ཡོན། ^1-2-5-5-0

[Block 1255]
དེ་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཤིན་ཏུ་ཡོངས་སུ་དག་པར༌[^879]བསྟན་ནས། དེའི་འོག་ཏུ་འདི་ལ་དད་པ་བསྐྱེད་པའི་ཕྱིར་དེ་ལ་མིག་གི་ནད་འབྱུང་བར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཚེ་འདི་དང་ཚེ་ཕྱི་མ་ལ་འབྱུང་བའི་ཕན་ཡོན་རྣམས་བསྟན་ཏོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ནི་སྐྱེ་བའམ་འགག་པའམ་ཀུན་ནས་ཉོན་མོངས་པའམ། རྣམ་པར་བྱང་བའམ། ཡོངས་སུ་བཟུང་བ་འམ་དོར་བའི་ཆོས་གང་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི་སྐྱེ་བ་དང་འགག་པ་ལ་སོགས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་མི་སྣང་ངོ་ཞེས་བསྟན་པའོ། །

[Block 1256]
དེ་ལྟར་འདུ་ཤེས་པར་ཡང་མི་བྱེད་ལ་དེ་ལྟར་མི་རྟོག་ཅིང་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་རིན་པོ་ཆེ་ཡོན་ཏན་མང་པོ་དང་ལྡན་པ་ཡིན་ནོ་སྙམ་དུ་ཡང་མི་རྟོག་པའོ། །

[Block 1257]
རབ་འབྱོར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་ཆོས་གང་ཡང་སྒྲུབ་པའམ་རྣམ་པར་སྟོན་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་མི་འགྱུར་བར༌[^880]ཡོངས་སུ་འགྲུབ་པས༌[^881]ཡོངས་སུ་གྲུབ་པ་དེའི་ཚེ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི༌[^882]དེ་ལྟར་སྣང་སྟེ། ཆོས་ཁྱད་པར་ཅན་གང་ཡང་བསྒྲུབ་པར་བྱའོ་སྙམ་པའི་རློམ་སེམས་ཀྱང་མེད། ཆོས་ཁྱད་པར་ཅན་རྣམས་ཀྱང༌[^883]བཟུང་ངོ་སྙམ་མམ།[^884] སྦྱིན་ནོ་སྙམ་པའི་རློམ་སེམས་ཀྱང་མེད། ཟག་པ་མེད་པའི་ཆོས་རྣམས་བསྐྱེད་དོ་སྙམ་མམ་ཆོས་ངན་པ་རྣམས་དག༌[^885]གོ་སྙམ་པའི་རློམ་སེམས་ཀྱང་མེད། འཁོར་བའི་ཆོས་རྣམས་རྒྱུན་བཅད་དོ་སྙམ་མམ། རྣམ་པར་བྱང་བ་རྣམས་བརྟག་པར་བྱའོ་སྙམ་པའི་རློམ་སེམས་ཀྱང་མེད། བདག་ནི་གཅིག་གོ་སྙམ་པའམ༌[^886]ཐ་དད་དོ་སྙམ་པའི་རློམ༌[^887]སེམས་ཀྱང་མེད། བདག་ནི་སྔོན་མ་བྱུང་བ་ལས༌[^888]བྱང་ཆུབ་སེམས་དཔའི༌[^889]སྤྱོད་པའི་སྟོབས་ཀྱིས་བྱུང་བ་སྟེ། སྒྲིབ་པ་ཐམས་ཅད་བྲལ་བའོ་སྙམ་པའི་རློམ་སེམས་ཀྱང་མེད།

[Block 1258]
སྔོན་ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་ལ་སོགས་པས་ཀུན་ནས་ཉོན་མོངས་པར་གྱུར་པ་ལས།

[Block 1259]
ཕྱིས་རྣམ་པར་དག་གོ་སྙམ་པའི་རློམ་སེམས་ཀྱང་མེད། ནག་པོའི་ཆོས་རྣམས་འགྲིབ་པར་བྱ་ཞིང་དཀར་པོའི་ཆོས་རྣམས་རྣམ་པར་འཕེལ་བར་བྱའོ་སྙམ་པའི་རློམ་སེམས་ཀྱང་མེད། དུས་གསུམ་དུ་གཏོགས་སོ་སྙམ་པའི་རློམ་སེམས་ཀྱང་མེད། ཁམས་གསུམ་དུ་དགོད་དོ་སྙམ་པའམ། ཡང་དག་པར་བཟླ་བར་བྱའོ་སྙམ་པའི་རློམ་སེམས་ཀྱང་མེད། བདག་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ༌[^890]སྦྱིན་པར་བྱེད་པའམ། དེའི་མི་མཐུན་པའི་ཕྱོགས་སེར་སྣ་ལ་སོགས་པ་སྤོང་བར་བྱེད་པའོ་སྙམ་པའི་རློམ་སེམས་ཀྱང་མེད་དོ། །

[Block 1260]
རབ་འབྱོར་དེ་བཞིན་གཤེགས་པ་རྣམས་བྱུང་ཡང་རུང་མ་བྱུང་ཡང་རུང་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་གནས་པའི་མཚན་ཉིད་དེ། གང་ཡང་ཅི་ཡང་མི་བྱེད་དོ་ཞེས་བསྟན་པའོ། །

[Block 1261]
ཆོས་གནས་པ་འདི་ཉིད་མཁྱེན་པས། དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་བ་དག་འཇིག་རྟེན་ན་སྣང་སྟེ། འདི་ཉིད་དེ་དག་གི་མངོན་པར་རྟོགས་པ་དང་། འདི་ཉིད་ཆོས་ཀྱི་འཁོར་ལོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1262]
རབ་འབྱོར་འདི་ནི་ཆོས་ཀྱི་འཁོར་ལོ་གཉིས་སུ་བསྐོར་བ་ཡང་མ་ཡིན། གཅིག་ཏུ་བསྐོར་བ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དོན་དམ་པར་ཆོས་ཐམས་ཅད་གྲངས་ལས་འདས་པའི་ཕྱིར་དེ་སྐད་བསྟན་ཏོ། །

[Block 1263]
ཆོས་གང་ཡང་བསྐོར་བའམ་མི་བསྐོར་བར་བྱ་བའི་ཕྱིར་ཉེ་བར་གནས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་རོ་ཞེས་བྱ་བའི་འདུ་ཤེས་སམ། རྣམ་པར་རྟོག་པ་སེལ་བར་བྱེད་པའོ། །

[Block 1264]
དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི༌[^891]ཆོས་ཐམས་ཅད་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱི་མཚན་ཉིད༌[^892]དུ་འཛིན་ཏོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1265 [HEADING]]
##### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཆོས་ཐམས་ཅད་ལ་འཇུག་པ། ^1-2-5-6-0
--- END BLOCKS ---
