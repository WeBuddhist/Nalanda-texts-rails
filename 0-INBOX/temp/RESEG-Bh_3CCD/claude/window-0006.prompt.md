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
[Block 211]
གསང་བའི་པདྨ་ལ་ཡང་ཡི་གེ་བཾ་ལས་སྐྱེས་པའི་གོས་དཀར་མོ་མེའི་ཁམས་ཀྱི་རང་བཞིན་ཅན་རྣམ་པར་བསྒོམས་ཏེ། དེའི་ནང་གི་ཁོང་སྟོང་ལ་ཡང་རླུང་གི་ཁམས་ཀྱི་ངོ་བོ་ཉིད་ཡི་གེ་ཏཾ་ཡོངས་སུ་གྱུར་པ་ལས་དམ་ཚིག་སྒྲོལ་མ་ཡཾ་ཡོངས་སུ་གྱུར་པ་ལས་ཁོང་སྟོང་ནམ་མཁའ་ལྟ་བུ་བསྐྱེད་པར་བྱའོ། །

[Block 212]
དེའི་གཟུགས་ལ་གཟུགས་རྡོ་རྗེ་མ་དང་། དེའི་པདྨ་ལ་སོགས་པའི་དྲི་རྣམས་ལ་ཡང་དྲི་རྡོ་རྗེ་མ་དང་། དེའི་སྐད་སྙན་པ་ལ་སྒྲ་རྡོ་རྗེ་མ་དང་། དེའི་ཁ་མཆན་ཁུང་གཉིས་ནུ་མ་གཉིས་ལྟེ་བ༌[^129]ལ་སོགས་པའི་རོ་དྲུག་ལ༌[^130]རྡོ་རྗེ་མ་དེ་དག་ཛཿཧཱུྃ་བཾ་ཧོཿ །ས་བོན་ལས་སྐྱེས་པ་རྣམ་པར་དགོད་དོ། །

[Block 213]
དེ་རྣམས་དང་ལྷན་ཅིག་ཏུ་སའི་སྙིང་པོ་ལ་སོགས་པ་དང་སྙོམས་པར་ཞུགས་པར་བསམས་ཏེ། གཡས་པ་དང་གཡོན་པའི་ཕྱག་གཉིས་དང་ཁ་དང་གསང་བ་དང་། གཡས་པ་དང་གཡོན་པའི་དཔུང་པ་གཉིས་དང་དེ་བཞིན་དུ་གཡས་དང་གཡོན་པའི་པུས་མོ་དང་། སྤྱི་བོ་དང་རྐང་པའི་མཐིལ་དུ་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་རྡོ་རྗེ་རོ་ལངས་མ་དང་། གཞན་གྱིས་མི་ཐུབ་མ་དང་། ཁྲོ་གཉེར་མ་དང་། རལ་པ་གཅིག་མ་དང་། སྣ་ཚོགས་རྡོ་རྗེ་མ་དང་། རིན་ཆེན་སྣ་ཚོགས་མ་དང་། པདྨ་སྣ་ཚོགས་མ་དང་། ལས་སྣ་ཚོགས་མ་དང་། ནམ་མཁའ་རྡོ་རྗེ་མ་དང་། ས་འཛིན་མ་ཁྲོ་བོའི་རྒྱལ་པོ་རྣམས་ཀྱི་བཙུན་མོ། །

[Block 214]
གཤིན་རྗེ་གཤེད་ལ་སོགས་པ༌[^131]ཁྲོ་བོ་བཅུའི་མདོག་དང་མཚུངས་པ་ཞལ་གསུམ་པ༌[^132]ཕྱག་དྲུག་པ་དགོད་པར་བྱའོ། །

[Block 215]
དེའི་རྗེས་ལ་བདག་ཉིད་ཀྱི་རྡོ་རྗེ་ས་བོན་ཧཱུཾ་ལས་ཡོངས་སུ་རྫོགས་པའི་རྡོ་རྗེ་རྩེ་ལྔ་པའི་རྣམ་པ་ཚངས་པས་བྱིན་གྱིས་བརླབས་པའི་ནོར་བུའི་ཆ༌[^133]དང་ལྡན་པར་བྱ་སྟེ། ལྷ་མོ་ལ་ཡང་ཨ་ལས་སྐྱེས་པའི་པདྨ་དམར་པོ་འདབ་མ་བརྒྱད་པ། དེའི་ལྟེ་བར་ཆར་འབབ་པ་དགག་པར་བྱ་བའི་ཕྱིར་ཡི་གེ་ཕཊ་ཀྱིས་བྱིན་གྱིས་བརླབས་ཏེ་དེ་གཉིས་ཀ་ལས་ཀྱང་ཁ་དོག་སྣ་ལྔ་པའི་འོད་ཟེར་གྱི་འཁོར་ལོ་བྱུང་བར༌[^134]བསམས་ཏེ། བསྙེན་པ་མཆོག་ལ་སོགས་པའི་རིམ་གྱིས་བསྒྲུབ་པ་ལ་བརྩམ་པར༌[^135]བྱའོ། །

[Block 216]
དེ་ལ་བསྒྲུབ་བྱ་དང་སྒྲུབ་བྱེད་ཀྱི་སྦྱོར་བ་ནི་བསྙེན་པའོ། །

[Block 217]
རྡོ་རྗེ་དང་པདྨ་འདུས་པ་ནི་ཉེ་བར་སྒྲུབ་པའོ། །

[Block 218]
ས་བོན་གྱི༌[^136]བྱིན་གྱིས་བརླབས་པ་དེ་དག་གིས་བསྐྱོད་པ་ནི་སྒྲུབ་པའོ། །

[Block 219]
དེ་ལས་བདེ་བ་ཆེན་པོ་ཉམས་སུ་མྱོང་བ་ནི་སྒྲུབ་པ་ཆེན་པོའོ། །

[Block 220]
ཇི་སྐད་དུ་རྒྱུད་ཕྱི་མ་ལས།

[Block 221 [VERSE]]
གང་ཕྱིར་བསྒྲུབ་བྱ་སྒྲུབ་བྱེད་ཀྱི། །
སྦྱོར་བ་བསྙེན་པ་ཡིན་པར་འདོད། །
རྡོ་རྗེ་པདྨ་མཉམ་སྦྱོར་བས། །
ཉེ་བར་སྒྲུབ་པར་གསུངས་པ་ཡིན། །

[Block 222 [VERSE]]
སྒྲུབ་པ་བསྐྱོད་པ་རབ་བཤད་པ། །
ཧཱུྃ་ཕཊ་ཡང་དག་ལྡན་པ་སྟེ། །
རང་ངོ་རང་བདེ་ཞི་བ་ནི། །
སྒྲུབ་པ་ཆེན་པོ་ཡིན་པར་འདོད། །

[Block 223]
ཅེས་འབྱུང་ངོ་། །དེའི་འོག་ཏུ་འདོད་ཆགས་ཆེན་པོའི་དབྱངས་ཀྱིས་དེ་བཞིན་གཤེགས་པ་འཇུག་པ་སྔོན་དུ་འགྲོ་བ་རྡོ་རྗེ་དང་པདྨ་སྙོམས་པར་འཇུག་པའི་དུས་སུ་བཅོམ་ལྡན་འདས་རིན་ཆེན་འབྱུང་ལྡན་གྱི་སྔགས་བརྗོད་པར་བྱ་སྟེ། ཨོཾ་སརྦ་ཏ་ཐཱ་ག་ཏ་ཨ་ནུ་རཱ་ག་ན༌[^137]བཛྲ་སྭ་བྷཱ་བ་ཨཱཏྨ་ཀོ྅ཧཾ། ཡན་ལག་དང་ཉིང་ལག་ཐམས་ཅད་ལ་ཕྱུང་ཞིང་རྡོ་རྗེའི་ཆང་ཟུངས་སུ་གནས་པའི་བྱང་ཆུབ་ཀྱི་སེམས། ཧཱུྃ་གི་སྒྲ་བརྗོད་ཅིང་དེའི་འོག་ཏུ་ཕཊ་ཀྱི་སྒྲས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་འདུས་པའི་བློས་པདྨའི་ནང་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་དབྱུང་བར་བྱའོ། །

[Block 224]
དེའི་སྔགས་འདི་ཡིན་ཏེ། ཨོཾ་སརྦ་ཏ་ཐཱ་ག་ཏ་པཱུ་ཛ་བཛྲ་སྭ་བྷཱ་བ་ཨཱཏྨ་ཀོ྅ཧཾ། བཅོམ་ལྡན་འདས་དོན་ཡོད་གྲུབ་པའི་སྔགས་སོ། །

[Block 225]
བྱང་ཆུབ་ཀྱི༌[^138]སེམས་དེ་ཉིད་ཨོྃ་བཛྲ་དྷྲྀཀ་ཅེས་སྔགས་ཀྱི་ཚུལ་དུ་ཡོངས་སུ་གྱུར་པ་ལས་མི་བསྐྱོད་པ་ཞལ་གསུམ་པ་ཕྱག་དྲུག་པ་སྐུ་མདོག་སྔོན་པོ་མཆེ་བ་གཙིགས་པ་ཚམ་ངམ་པ་སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་ཅན་ཕྱིར་སྤྲོས་པ་དེས་ཞེ་སྡང་ལ་སོགས་པའི་སེམས་ཅན་གྱི་ཁམས་སྦྱངས་ལ། མངོན་པར་དགའ་བའི་འཇིག་རྟེན་གྱི་ཁམས་སུ་རབ་ཏུ་དགོད་དེ། སླར་ཡང་གཤེགས་ནས་ཕྱོགས་བཅུ་ལ་གཟིགས་ཏེ་རྡོ་རྗེ་སེམས་དཔའ་དེ་ཉིད་དང་ལྷན་ཅིག་ཏུ་མར་ལ་མར་ཐིམ་པ་བཞིན་དུ་གཅིག་ཏུ་གྱུར་པ་དཔལ་མི་བསྐྱོད་རྡོ་རྗེ་བསྒོམ་པར་བྱའོ། །

[Block 226]
ཕྱག་ལ་སོགས་པའི་བཤད་པའི་རྒྱུད་ལས་གསུངས་པ༌[^139]ནི་ཇི་སྐད་དུ།

[Block 227 [VERSE]]
ཨིནྡྲ་ནཱི་ལའི་མདོག་དང་མཚུངས། །
ཅུང་ཟད་མཆེ་བ་གཙིགས་པ་སྟེ། །
ཉི་མའི་དཀྱིལ་འཁོར་ལ་གནས་པ། །
ཞལ་གསུམ་ཕྱག་དྲུག་གཟི་བརྗིད་ཆེ། །

[Block 228 [VERSE]]
རྡོ་རྗེ་འཁོར་ལོ་ཆུ་སྐྱེས་ནི། །
གཡས་པའི་ཕྱག་དུ་བསྒོམ་པར་བྱ། །
དྲིལ་བུ་ཡིད་བཞིན་ནོར་བུ་དང་། །
དེ་བཞིན་རལ་གྲི་ཕྱག་གཡོན་ནའོ། །

[Block 229 [VERSE]]
མགོན་པོ་རྡོ་རྗེ་སྐྱིལ་ཀྲུང་ཅན། །
རལ་བའི་ཐོར་ཚུགས་འཛིན་པ་མཆོག །
ཞི་བ་རྗེས་ཆགས་སྒེག་པ་དང་། །
ཞལ་གསུམ་པོ༌[^140]ནི་རྣམ་པར་མཛེས། །

[Block 230 [VERSE]]
སྤྲོས་པའི་འོད་ཟེར་འཁོར་ལོས་ནི། །
ནམ་མཁའི་གཏོས་ནི་མ་ལུས་ཁྱབ། །
ཞེ་སྡང་རྡོ་རྗེའི༌[^141]གོ་འཕང་གནས། །
བདག་ཉིད་དེ་ལྟར་བསྒོམ་པར་བྱ། །

[Block 231]
ཞེས་འབྱུང་ངོ་། །དེའི་རྗེས་ལ་བྱང་ཆུབ་སེམས་ཀྱི་ཐིག་ལེ་གཉིས་པ་ཛི་ན་ཛྀཀ་ཞེས་སྔགས་ཀྱི་ཚུལ་དུ་སྤྲོས་ཏེ། པདྨའི་ནང་དུ་རྣམ་པར་སྣང་མཛད་ཀྱི་གཟུགས་ཡོངས་སུ་གྱུར་པ་ཕྱི་རོལ་དུ་སྤྲོས་ཏེ་གཏི་མུག་ལ་སྤྱོད་པའི་སེམས་ཅན་གྱི་ཁམས་སྦྱངས་ནས་འོག་མིན་གྱི་གནས་སུ་དགོད༌[^142]དེ། སླར་ཡང་གཤེགས་ནས་ཕྱོགས་བཅུར་གཟིགས་པ་སྔོན་དུ་འགྲོ་བས་མདུན་དུ་ཟླ་བའི་དཀྱིལ་འཁོར་འཁོར་ལོས་མཚན་པ་ལ་བཞུགས་པར༌[^143]བསྒོམ་པར་བྱའོ། །

[Block 232]
རྡོ་རྗེ་ཕྲེང་བ་ལས་ཀྱང་།

[Block 233 [VERSE]]
དེ་ཡི་རྩ་བའི་ཕྱག་ལ་ནི། །
འཁོར་ལོ་རྩིབས་ནི་བརྒྱད་པ་མཆོག །
ཁ་དོག་དཀར་ཞིང་ཀུནྡ་འདྲ། །
ཞི་བ་ཡི་ནི་གཟུགས་འཆང་བ། །

[Block 234 [VERSE]]
ལྷག་མ་ཐམས་ཅད་སྔོན་བཞིན་དུ། །
མདོར་བསྡུས་པར་ནི་ཤེས་པར་བྱ། །

[Block 235]
ཞེས་འབྱུང་ངོ་། །

[Block 236]
དེའི་རྗེས་སུ་སླར་ཡང་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེ་རདྣ་དྷྲྀཀ་ཅེས་བྱ་བའི་སྔགས་ཀྱི་ཚུལ་དུ་ཡོངས་སུ་གྱུར་པའི་རིན་ཆེན་འབྱུང་ལྡན་དེ་ཉིད་དུ་སྤྲོས་ཏེ་ཕྱིར་གཤེགས་ཤིང་ང་རྒྱལ་ལ་སྤྱོད་པའི་སེམས་ཅན་གྱི་ཁམས་སྦྱངས་ཏེ། རིན་ཆེན་འབྱུང་ལྡན་གྱི་འཇིག་རྟེན་གྱི་ཁམས་སུ་རབ་ཏུ་བཀོད་དེ། སླར་ཡང་གཤེགས་ནས་ཕྱོགས་བཅུར་གཟིགས་ནས་ལྷོའི༌[^144]ཕྱོགས་སུ་ཟླ་བའི་དཀྱིལ་འཁོར་ལ་རྩིབས་དྲུག་པའི་རིན་པོ་ཆེའི་སྟེང་དུ་བཞུགས་པར་བསམ་མོ། །

[Block 237]
དེའི་རྩ་བའི་ཕྱག་ན་ཡིད་བཞིན་གྱི་ནོར་བུ། སྐུ་མདོག་སེར་པོ་ཤེས་པར་བྱའོ། །

[Block 238]
ལྷག་མ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 239]
དེའི་རྗེས་སུ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེ་ཨཱ་རོ་ལྀཀ་ཅེས་བྱ་བའི་སྔགས་ཀྱི་ཚུལ་དུ་ཡོངས་སུ་གྱུར་པ་འོད་དཔག་ཏུ་མེད་པའི་གཟུགས་དེ་ཉིད་དུ་སྤྲོས་ཏེ། ཕྱི་རོལ་ཏུ་གཤེགས་ནས་འདོད་ཆགས་ལ་སྤྱོད་པའི་སེམས་ཅན་གྱི་ཁམས་སྦྱངས་ཏེ། བདེ་བ་ཅན་གྱི་འཇིག་རྟེན་གྱི་ཁམས་སུ་བཀོད་དེ། སླར་ཡང་གཤེགས་ནས་ཕྱོགས་བཅུ་ལ་གཟིགས་ཏེ་ནུབ་ཀྱི་ཕྱོགས་སུ་ཟླ་བ་དང་པདྨའི་སྟེང་དུ་བཞུགས་པར་བསམ་མོ། །

[Block 240]
འདིའི་རྩ་བའི་ཕྱག་གཉིས་ཀྱིས༌[^145]པདྨ་བསྐུམ་པ་རྒྱས་པར་བྱེད་པ་སྐུ༌[^146]མདོག་དམར་པོ་བསྒོམ་པར་བྱའོ། །

[Block 241]
ལྷག་མ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 242]
དེའི་རྗེས་སུ་ཡང་སླར་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེ་པྲཛྙཱ་དྷྲྀཀ་ཅེས་པའི་སྔགས་ཀྱི་ཚུལ་དུ་ཡོངས་སུ་གྱུར་པ་དེ་ལས་དོན་ཡོད་གྲུབ་པ་དེ་ཉིད་དུ་སྤྲོས་ཏེ་ཕྱི་རོལ་དུ་གཤེགས་ནས་ཕྲག་དོག་ལ་སྤྱོད་པའི་སེམས་ཅན་གྱི་ཁམས་སྦྱངས་ནས། མེ་ཏོག་ཅན་ཞེས་བྱ་བའི་སངས་རྒྱས་ཀྱི་ཞིང་དུ་རབ་ཏུ་གནས་པར་མཛད་ནས་སླར་ཡང་གཤེགས་ཏེ། ཕྱོགས་བཅུར་གཟིགས་ནས་བྱང་གི་ཕྱོགས་སུ་སྣ་ཚོགས་པདྨ་དང་སྣ་ཚོགས་རྡོ་རྗེས་མཚན་པའི་ཉི་མའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་བཞུགས་པར་བསམ་མོ། །

[Block 243]
དེའི་རྩ་བའི་ཕྱག་གཡས་པ་ལ་རལ་གྲི་དང་སྐུ་མདོག་སྔོ་བསངས༌[^147]སུ་བསམ་པར་བྱ་ཞེས་ལྷག་མ་རྣམས་སྔ་མ་བཞིན་ནོ། །

[Block 244]
དེ་དག་ནི་ཕུང་པོ་ལྔ་དང་། འབྱུང་བ་ཆེན་པོ་ལྔ་དང་། དབང་པོ་ལྔ་དང་། རྣམ་པར་ཤེས་པ་ལྔ་དང་། ནམ་མཁའ་རྣམ་པར་དག་པའི་ཡེ་ཤེས་ལྔའི་ངོ་བོ་ཉིད་དེ་བཞིན་གཤེགས་པ་ལྔ་པོ་ཤེས་པར་བྱའོ། །

[Block 245]
ཇི་སྐད་དུ།

[Block 246 [VERSE]]
ཞེ་སྡང་གཏི་མུག་འདོད་ཆགས་དང་། །
དམ་ཚིག་ནོར་བུའི་རིགས་དེ་བཞིན། །
དེ་དག་རིགས་ནི་ལྔ་ཉིད་དེ། །

[Block 247]
འདོད་དང་གྲོལ་བ་རབ་སྒྲུབ་བྱེད། ཅེས་འབྱུང་ངོ་། །དེའི་རྗེས་ལ་མོ་ཧ་ར་ཏི་ཞེས་སྔགས་ཀྱི་ཚུལ་དུ་ཡོངས་སུ་གྱུར་པའི་ཐིག་ལེ་ལས་སངས་རྒྱས་སྤྱན་མ་དེ་ཉིད་དུ་བསྐྱེད་པའི་ཕྱིར་སྤྲོས་ཏེ། བདག་ཏུ་གཏི་མུག་པའི་རྣམ་པར་རྟོག་པ་སྦྱངས་ཏེ༌[^148]སའི་ཁམས་ལ་མངོན་པར་ཞེན་པ་རྣམས་རྣམ་པར་སྣང་མཛད་ཀྱི་ཞིང་ལ་བཀོད་དེ། །སླར་ཡང་གཤེགས་ནས་མེའི་མཚམས་སུ་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་བཞུགས་པར་བསམ་མོ། །

[Block 248]
དེའི་རྗེས་སུ་དྭེ་ཥ་ར་ཏི་ཞེས་བྱ་བའི་སྔགས་ཀྱི་ཚུལ་དུ་ཡོངས་སུ་གྱུར་པའི་ཐིག་ལེ་ལས་མཱ་མ་ཀཱི་དེ་ཉིད་དུ་བསྐྱེད་ལ་ཆུའི་ཁམས་ལ་མངོན་པར་ཞེན་པ༌[^149]རྣམས་ཀྱི་བདག་ཏུ་ང་རྒྱལ་བའི་རྣམ་པར་རྟོག་པ་སྦྱངས་ཏེ། རིན་ཆེན་འབྱུང་ལྡན་གྱི་ཞིང་ཁམས་སུ་རྣམ་པར་དགོད༌[^150]དེ་སླར་ཡང་གཤེགས་ཤིང་བདེན་བྲལ་གྱི་མཚམས་སུ་པདྨ་དང་ཉི་མའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་བཞུགས་པར་བསམ་པར་བྱའོ། །

[Block 249]
དེའི་འོག་ཏུ་རཱ་ག་ར་ཏི་ཞེས་བྱ་བའི་སྔགས་ཀྱི་ཚུལ་དུ་ཡོངས་སུ་གྱུར་པ་ལས་གོས་དཀར་མོ་དེ་ཉིད་དུ་བསྐྱེད་དེ་ཕྱིར་སྤྲོས་ལ་མེའི་ཁམས་ལ་མངོན་པར་ཞེན་པ་རྣམས་ཀྱི་བདག་ཏུ་ཆགས་པའི་རྣམ་པར་རྟོག་པ་སྦྱངས་ཏེ། སྣང་བ་མཐའ་ཡས་ཀྱི་ཞིང་ཁམས་སུ་བཀོད་པར་བྱས་ལ། སླར་ཡང་གཤེགས་ཏེ་རླུང་གི་མཚམས་སུ་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་ལ་བཞུགས་པར་བསམ་མོ། །

[Block 250]
དེ་ནས་བཛྲ་ར་ཏི་ཞེས་བྱ་བའི་སྔགས་ཀྱི་ཚུལ་དུ་ཡོངས་སུ་གྱུར་པ་ཐིག་ལེ་ལས་ལྷ་མོ་སྒྲོལ་མ་དེ་ཉིད་དུ་བསྐྱེད་དེ་དེ་ཕྱིར་སྤྲོས་ལ་རླུང་གི་ཁམས་ལ་མངོན་པར་ཞེན་པ་རྣམས་ཀྱི་བདག་ཏུ་ལྟ་བའི་རྣམ་པར་རྟོག་པ་འཇོམས་ཤིང་དོན་ཡོད་གྲུབ་པའི་ཞིང་དུ་རྣམ་པར་དགོད༌[^151]དེ་སླར་ཡང་གཤེགས་ནས་དབང་ལྡན་གྱི་མཚམས་སུ་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་དུ་བཞུགས་པར་བསམ་མོ། །
--- END BLOCKS ---
