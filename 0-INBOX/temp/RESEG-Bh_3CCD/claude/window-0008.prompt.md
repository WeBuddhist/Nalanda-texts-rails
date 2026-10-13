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
[Block 281]
ལྷག་མ་ནི་བདག་པོ་བཞིན་ནོ། །

[Block 282]
དེ་ནས་བིགྷྣཱནྟ་ཀྲྀཏ་ཅེས་བྱ་བའི་སྔགས་ལས་སྐྱེས་པ་བགེགས་མཐར་བྱེད་དེ་ཉིད་དུ་སྤྲོས་ནས་ཕྱིར༌[^166]གཤེགས་ཏེ། ལྷའི་བུའི་བདུད་དང་རྣམ་པར་སྨིན་པའི༌[^167]སྒྲིབ་པ་དང་ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་དང་། གཡེང་བ་རྣམས་རྣམ་པར་འཇོམས་ཤིང་ཏིང་ངེ་འཛིན་གྱི་དབང་པོ་ལ༌[^168]སེམས་ཅན་ཐམས་ཅད་རབ་ཏུ་དགོད༌[^169]དེ། སླར་ཡང་གཤེགས་ནས་བྱང་ཕྱོགས་ཀྱི་སྒོར་པདྨ་དང་ཉི་མའི་དཀྱིལ་འཁོར་ལ་བཞུགས་སོ། །

[Block 283]
རྩ་བའི་ཕྱག་གཡས་པས་རྡོ་རྗེ་འཛིན་པ་སྐུ་མདོག་མརྒད་ལྟ་བུ་སྟེ། ལྷག་མ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 284]
ཁྲོ་བོ་དེ་རྣམས་གཡས་བརྐྱང་པ་དང་གཡོན་བརྐྱང་བ་དང༌[^170]མཉམ་པ་དང་མི་མཉམ་པའི་སྟང་སྟབས་ཀྱིས་བཞུགས་པར་བསམ་མོ། །

[Block 285]
དེའི་འོག་ཏུ་སྭཱ་ཧཱ་ཨཱཿཨོཾ་ཧཱུཾ་བྷྲཱུཾ་ས་བོན་དྲུག་ལས་རྫོགས་པ་མི་གཡོ་མགོན་དང་། དབྱུག་སྔོན་ཅན་དང་། འདོད་པའི་རྒྱལ་པོ་དང་། སྟོབས་པོ་ཆེ་དང་། གནོད་མཛེས་ཀྱི་རྒྱལ་པོ་དང་། གཙུག་ཏོར་འཁོར་ལོས་སྒྱུར་བ་སྔ་མ་བཞིན་དུ་སྤྲོས་ནས་ཕྱིར་གཤེགས་ཏེ་མིག་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པ་དྲུག་གི་རྣམ་པར་རྟོག་པའི༌[^171]དྲི་མ་སྦྱངས་ཏེ། སེམས་ཅན་གྱི་ཁམས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་དང་ལྡན་པ་དང་མངོན་པར་ཤེས་པ་དྲུག་ཐོབ་པར་བྱས་ཏེ། སླར་ཡང་གཤེགས་ཏེ་ཤར་ལ་སོགས་པའི་སྒོའི་མཚམས་རྣམས་དང་། སྟེང་དང་འོག་དག་ཏུ་བཞུགས་པར་བསམ་མོ། །

[Block 286]
དེ་རྣམས་ཀྱི་སྐུ་མདོག་ནི་རང་རང་གི་རིགས་དང་མཐུན་པ་ཞེས་ལ་ལ་འདོད་དོ། །

[Block 287]
དྲུག་ཅར་སྐུ་མདོག་ནག་པོ་ཡིན་ཞེས་དཔལ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་སྔ་ནས་བཞེད་དོ། །

[Block 288]
དེ་དག་གཡོན་བརྐྱང་པའི་སྟང་སྟབས་ཅན་ནོ། །

[Block 289]
ཁྲོ་བོ་བཅུ་པོ་མིག༌[^172]གཡོ་ཞིང་ཟླུམ་པའི་སྨིན་མ་ཁམ་པ། ཤངས་ཟླུམ༌[^173]པ། དབུ་སྐྲ་འབར་ཞིང་གྱེན་དུ་བརྫེས་པ། ཞལ་གསུམ་པ། སྤྱན་གསུམ་པ། ཕྱག་དྲུག་པ། མིའུ་ཐུང་གི་རྣམ་པ་ཅན། མཆེ་བ་གཙིགས་ཤིང་ཚམ་ངམ་པ། ལྗགས་བསྒུལ་ཞིང་མེ་སྟག་འཕྲོ་བ་རིགས་ཀྱི་ཀླུ་བརྒྱད་ཀྱིས་རྒྱན༌[^174]བྱས་པ། འཇིགས་པའི་གཟུགས་ཅན་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་རྡོ་རྗེ་རོ་ལངས་མ་དང་། ཁྲོ་གཉེར་མ་དང་། གཞན་གྱིས་མི་ཐུབ་མ༌[^175]དང་། རལ་པ་གཅིག་མ་དང་། རྡོ་རྗེ་སྣ་ཚོགས་མ་དང་། རིན་ཆེན་སྣ་ཚོགས་མ་དང་། པདྨ་སྣ་ཚོགས་མ་དང་། ལས་སྣ་ཚོགས་མ་དང་། ས་འཛིན་མ་དང་། ནམ་མཁའ་རྡོ་རྗེ་མ་ཁྲོ་བོའི་རྒྱལ་པོའི་བཙུན་མོ་རྣམས་དེ་དག་གི་ཆོས་ཉིད་དག་གིས་འཁྱུད་པར་བསམ་མོ། །

[Block 290]
མི་གཡོ་མགོན་ལ་སོགས་པའི་ཁྲོ་བོ་དྲུག་གི་རྩ་བའི་ཕྱག་གཡས་པའི་དང་པོ་རྣམས་ལ་ལྕགས་ཀྱུ་དང་། དབྱུག་པ་དང་། རྩེ་གསུམ་དང་། རལ་གྲི་དང་། རྡོ་རྗེ་དང་། འཁོར་ལོ་དག་ཤེས་པར་བྱའོ། །

[Block 291]
ལྷག་མ་རྣམས་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 292]
རྒྱུད་ཕྱི་མ་ལས་ཀྱང་།

[Block 293 [VERSE]]
ལྕགས་ཀྱུ་དབྱུག་པ་རྩེ་གསུམ་དང་། །
རལ་གྲི་རྡོ་རྗེ་འཁོར་ལོ་སྟེ། །
འདོད་པ་དབྱུག་སྔོན་མི་གཡོ་སྟོབས། །
སྟེང་འོག་གནོད་མཛེས་གཙུག་ཏོར་གྱིའོ། །

[Block 294]
ཞེས་འབྱུང་ངོ་། །སྲུང་བའི་འཁོར་ལོ་འདི་ནི་ནང༌[^176]གི་དེ་བཞིན་གཤེགས་པ་དང་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་སྙོམས་པར་ཞུགས་པ་རྣམས་ཀྱི་ཏིང་ངེ་འཛིན་བསྲུང་བའི་དོན་དང་། བགེགས་རྣམ་པར་འཇིགས་པར༌[^177]བྱ་བའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱི་ཁྲོ་བོའི་རྒྱལ་པོའི་དཀྱིལ་འཁོར་གསུངས་སོ། །

[Block 295 [VERSE]]
ལེའུ་བཅུ་གསུམ་པ་ལས་ཀྱང་། །
འགོག་པའི་རྡོ་རྗེ་ཁྲོ་བོ་ནི། །
སངས་རྒྱས་འཁོར་ལོ་ལ་བརྟེན་པས། །
ཏིང་འཛིན་ཡེ་ཤེས་རྡོ་རྗེ་རྣམས། །

[Block 296]
རྡོ་རྗེ་ཁྲོ་བོས་ལས་འགྲུབ་འགྱུར། །ཞེས་འབྱུང་ངོ་། །དེ་ལྟར་ཡོངས་སུ་གྲུབ་པའི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ལྷ་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་བདག་ཉིད་ལ་བལྟས་ཏེ། གཞལ་ཡས་ཁང་པའི་ཕྱི་རོལ་དུ་ཡི་གེ་སྭཱ་ལས་བྱུང་བའི་བཻ་ཌཱུརྱ་དང་པདྨ་རཱ་ག་དང་ཨིནྡྲ་ནཱི་ལའི༌[^178]ནོར་བུའི་ཁྱད་པར་རྣམས་ཀྱིས་སྤྲུལ་པའི་སྐས༌[^179]ཀྱི་རིམ་པ་ཅན་ཆུ་དངས་པའི༌[^180]ནང་དུ་སྐྱེས་པའི་གསེར་གྱི་པདྨ་ཅན་གྱི་རྫིང་རྣམས་དང་། དེ་བཞིན་དུ་ཡང་དེ་ལས་སྐྱེས་པའི་བཻ་ཌཱུརྱའི་སྡོང་པོ་ཅན་གསེར་བཙོ༌[^181]མའི་ཁ་དོག་དང༌[^182]ལྡན་པའི་པདྨའི་ལྟེ་བ་ལ་བཞུགས་པ་བསམ་གཏན་ལ་འཇུག་པའི་དེ་བཞིན་གཤེགས་པ་རྣམས་སོ། །

[Block 297]
དེའི་ཡང་ཕྱི་རོལ་ཏུ་མེ་ཏོག་དང་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པའི་ཡོངས་སུ༌[^183]འདུ་ལ་སོགས་པའི་ཤིང་སྣ་ཚོགས་པ་རྣམས་ཀྱི་རྩ་བར་ཀྲྀཥྞ་ས་ལེའི་པགས་པའི་གདན་ལ་བཞུགས་པའི་རང་སངས་རྒྱས་དང་དགྲ་བཅོམ་པ་མཐའ་ཡས་པས་མཛེས་པའོ། །

[Block 298]
དེའི་ཡང་ཕྱི་རོལ་ཏུ་གདུགས་དང་རྒྱལ་མཚན་དང་བ་དན་དང༌[^184]གཡེར་ཀ་དང་རྭ་དུང་དང་རྫ་རྔ་དང་རྔ་ཟླུམ་དང་པི་ཝང་དང་གླིང་བུ་དང༌[^185]རྒྱུད་མངས་དང་ཆལ་ཅུང་པི་རིལ་དང་། ཏམ་བུ་ར་དང་རྐེད་ཕྲན་ལ་སོགས་པ༌[^186]རོལ་ཆ་སྣ་ཚོགས་པ་འཛིན་པའི་ལྷ་མོ་རྣམས་ཀྱིས་བརྒྱན་པའོ། །

[Block 299]
དེའི་ཡང་ཕྱི་རོལ་དུ་རིན་པོ་ཆེ་སྣ་བདུན་ནི་འཁོར་ལོ་རྩིབས་བརྒྱད་ལ་ཁ་དོག་སེར་པོ་དང་གླང་པོ་རིན་པོ་ཆེ་ནི་མཆེ་བ་དྲུག་པ་ཁ་དོག་དཀར་པོ་དང་། རྟ་རིན་པོ་ཆེ་ནི་ཁ་དོག་ལྗང་གུ་དང་བུད་མེད་རིན་པོ་ཆེ་ནི་ལོ་བཅུ་དྲུག་གི་རྣམ་པ་སྔོ་བསངས་མ་ཚུལ་ཁྲིམས་དང་ལྡན་པ་དང་། ཡིད་བཞིན་ནོར་བུ་རིན་པོ་ཆེ་ནི་རྩིབས་དྲུག་པ་ཁ་དོག་སེར་པོ་དང་། ཁྱིམ་བདག་རིན་པོ་ཆེ་ནི་མདོག་དམར་པོ་མཛོད་མི་ཟད་པ་དང་ལྡན་པ་དང་། [^187]དམག་དཔོན་རིན་པོ་ཆེ་ནི་མདུང་དང་རལ་གྲི་འཛིན་ཞིང་ཁ་དོག་ནག་པོ་གོ་ཆ་དང་བཅས་པ་བསྒོམ་པར་བྱའོ། །

[Block 300]
དེའི་ཕྱི་རོལ་དུ་ལྷའི་གནས་རིས་དྲུག་གི་ལྷའི་བུ་མོ་སྣ་ཚོགས་པ་དང་བཅས་པ་མཆོད་རྫས་སྣ་ཚོགས་ཐོགས་པར་བསམ་མོ། །

[Block 301]
དེའི་ཡང་ཕྱི་རོལ་དུ་གནོད་སྦྱིན་དང་། སྲིན་པོ་དང་། འབྱུང་པོ་དང་། ཡི་དྭགས་དང་། ཤ་ཟ་དང་། གྲུལ་བུམ་དང་། བརྗེད་བྱེད་དང་། མཁའ་འགྲོ་མ་དང་། དྲི་ཟ་དང་། ལྷ་མ་ཡིན་དང་། ནམ་མཁའ་ལྡིང་དང་། མི་འམ་ཅི་དང་། ལྟོ་འཕྱེ་དང་། མི་དང་། མི་མ་ཡིན༌[^188]དང་། རྐང་མེད་དང་། རྐང་གཉིས་པ༌[^189]དང་། རྐང་བཞི་པ༌[^190]དང་། རྐང་མང་བ་རྣམས་སྟེང་དུ་ལག་པ་ཚོལ་བ་ལ་བརྩོན་པ་ཀི༌[^191]ལི་ཀི༌[^192]ལིའི་སྒྲ་རྗོད་པར་བྱེད་པ་རྣམས་ཀྱིས་བསྐོར་བའོ། །

[Block 302]
གཞལ་ཡས་ཁང་པའི་འོག་ཏུ་ཡང་ས་འོག་བདུན་གྱི་བར་དུ་ཁྱབ་པར་བྱེད་པ་ཡི་གེ་ཧཱ་ཡོངས་སུ་གྱུར་པ་ལས་རྡོ་རྗེ་རྒྱ་གྲམ་བསམ་མོ། །

[Block 303]
སྟེང་དུ་ཡང་བ་དན་དང་གཡེར་ཁ་རྣམས་སྲིད་པའི་རྩེ་མོའི་བར་དུ་སླེབས་པར༌[^193]བསམ་མོ། །

[Block 304]
དེ་ལྟ་བུའི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་མཐོང་ནས་དབུས་ཀྱི་བདག་པོར་གྱུར་པའི་རྣལ་འབྱོར་པས་སྔ་མ་བཞིན་དུ་རེག་བྱ་རྡོ་རྗེ་མའི་ཆོས་འབྱུང་བའི་ཕྱག༌[^194]རྒྱའི་ནང་དུ་སྣ་ཚོགས་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་བདེ་བ་ཆེན་པོ་འདོད་པའི་དབང་གིས་གསང་བའི་རྡོ་རྗེ་རབ་ཏུ་འཇུག་པས་བ་སྤུའི་ཁུང་བུ་ནས་ངེས་པར་འབྱུང་བའི་འོད་ཟེར་ལྕགས་ཀྱུའི་རྣམ་པས་ཕྱོགས་བཅུ་ན་བཞུགས་པའི་དེ་བཞིན་གཤེགས་པ་དབང་བསྐུར་བའི་དོན་དུ་འགུགས་ཤིང་གསོལ་བ་གདབ་པར་བྱའོ། །

[Block 305]
ཀྱེ་བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་རྣམས་བླ་ན་མེད་པའི་དབང་བསྐུར་བས༌[^195]བདག་ལ་དབང་བསྐུར་བ༌[^196]མཛོད་ཅིག་པའོ། །

[Block 306]
གསོལ་བ་བཏབ་པ་གསན་མ་ཐག་ཏུ། བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་དང་ལྷ་མོ་དང༌[^197]བྱང་ཆུབ་སེམས་དཔའ་ཁྲོ་བོ༌[^198]འཁོར་དང་བཅས་པ་གསེར་གྱི་མེ་ཏོག་སྣ་ཚོགས་པ་ཐོགས་པ་དང་། ལ་ལ་ནི་རོལ་ཆ་སྣ་ཚོགས་པའི་སྒྲས་ཕྱོགས་ཀྱི་ཆ་རྣམས་ཁྱབ་པར་བྱས་ལ་ཁ་ཅིག་ཀྱང་མཆོད་པ་རྣམ་པ་ལྔ་ལག་ན་ཐོགས་པ་དང་། ལ་ལ་ཡང་བདུད་རྩི་ལྔས་བཀང་བའི་སྣོད་འཛིན་པ། དེ་བཞིན་དུ་ཡང་ཁ་ཅིག་དྲི་བཟང་པོའི་ཆུས་བཀང་བའི་རིན་པོ་ཆེའི་བུམ་པ་ཐོགས་པ་གཞན་དག་ཀྱང་བསྟོད་པའི་ཚིག་རྣམས་བརྗོད་པ༌[^199]ལ་བརྩོན་པ། གཞན་དག་ཀྱང་བཀྲ་ཤིས་པའི་ཚིགས་སུ་བཅད་པ་རྗོད་པར་བྱེད་པ། ལ་ལ་ནི་རྡོ་རྗེའི་གླུ་ལེན་པ། ལ་ལ་ནི་གར་བྱེད་ཅིང་ནམ་མཁའི་དབྱིངས་ནས་གཤེགས་ཤིང་སྒྲུབ་པ་པོ་ལ་མངོན་པར་ཕྱོགས་པ། དཀྱིལ་འཁོར་གྱི་འཁོར་ལོའི་བདག་པོ་འཁོར་དང་བཅས་པ་ལ་དབང་བསྐུར་བ་མཛད་པར་བསམ་མོ། །

[Block 307]
དེའི་དུས་སུ་ཡང་སྔགས་དང་ཚིགས་སུ་བཅད་པ༌[^200]བརྗོད་པར༌[^201]མཛད་དེ། ཇི་ལྟར་བལྟམས་པ༌[^202]ཙམ་གྱིས་ནི།

[Block 308 [VERSE]]
དེ་བཞིན་གཤེགས་ཀུན་དབང་བསྐུར་བ། །
ལྷ་ཡི་ཆུ་ནི་དག་པ་ཡིས། །
དེ་བཞིན་ཁྱོད་ལ་དབང་བསྐུར་རོ། །

[Block 309]
ཨོཾ་སརྦ་ཏ་ཐཱ་ག་ཏ་ཨ་བྷི་ཥེ་ཀ༌[^203]ས་མ་ཡ༌[^204]ཤྲཱི་ཡེ་ཧཱུཾ། དབང་བསྐུར་མ་ཐག་ཏུ་དབུས་ཀྱི་བདག་པོའི་ཅོད་པན་དུ་རྡོ་རྗེ་འཆང་བའོ། །

[Block 310]
རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་དེ་བཞིན་གཤེགས་པ་བཞི་ལ་རྡོ་རྗེ་འཆང་བ་ཉིད་དོ། །

[Block 311]
སྤྱན་ལ་སོགས་པ་བཞི་ནི་རྣམ་པར་སྣང་མཛད་དང་། རིན་ཆེན་འབྱུང་ལྡན་དང་། འོད་དཔག་ཏུ་མེད་པ་དང་། དོན་ཡོད་གྲུབ་པའོ། །

[Block 312]
གཟུགས་རྡོ་རྗེ་མ༌[^205]ལ་སོགས་པ་ཡང་དེ་བཞིན་ནོ། །

[Block 313]
སའི་སྙིང་པོ་དང་བྱམས་པ་དག་ལ་རྣམ་པར་སྣང་མཛད་ཉིད་དོ། །

[Block 314]
ཕྱག་ན་རྡོ་རྗེ་དང་ནམ་མཁའི་སྙིང་པོ་དག་ལ་རིན་ཆེན་འབྱུང་ལྡན་ནམ་མི་བསྐྱོད་པའོ། །

[Block 315]
འཇམ་དཔལ་དང་སྤྱན་རས་གཟིགས་ཀྱི་དབང་ཕྱུག་ལ་འོད་དཔག་ཏུ་མེད་པའོ། །

[Block 316]
ཀུན་དུ་བཟང་པོ་དང་སྒྲིབ་པ་རྣམ་པར་སེལ་བ་ལ་དོན་ཡོད་གྲུབ་པའོ། །

[Block 317]
གཤིན་རྗེ་གཤེད་ལ་སོགས་པ་བཞི་ལ་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའོ། །

[Block 318]
འདོད་པའི་རྒྱལ་པོ་ལ་སོགས་པ་བཞི་ལ་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའམ་མི་བསྐྱོད་པའོ། །

[Block 319]
ཇི་སྐད་དུ། ཁྲོ་བོ་ཞེ་སྡང་གནས་ལས་འབྱུང་། །ཞེས་གསུངས་སོ། །

[Block 320]
རྡོ་རྗེ་རོ་ལངས་མ་ལ་སོགས་པ་རྣམས་ལ་གཤིན་རྗེ་གཤེད་ཁོ་ནའོ། །
--- END BLOCKS ---
