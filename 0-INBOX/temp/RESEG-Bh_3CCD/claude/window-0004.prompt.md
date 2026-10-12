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
[Block 141 [VERSE]]
སྐུ་ཡི་རྡོ་རྗེར་ཆུད་པ་ཡི། །
སངས་རྒྱས་ཆོ་ག་བཞིན་བསམས་ཏེ། །
དོན་དམ་པ་ཡི་རྡོ་རྗེ་ཡིས། །
དེ་བཞིན་ཉིད་དུ་འཇུག་པར་བྱ། །

[Block 142 [VERSE]]
དེ་བཞིན་གཤེགས་པའི་ཚོགས་བསད་ན། །
དངོས་གྲུབ་ངེས་པར་ཐོབ་པར་འགྱུར། །

[Block 143]
ཞེས་འབྱུང་ངོ་། །དེའི་རྗེས་ལ་སྔོན་དུ་བཤད་པའི་པདྨའི་སྟེང་དུ་ཡི་གེ་གསུམ་ལས་བྱུང་བའི་ཉི་མ་དང་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་དེ་བཞིན་གཤེགས་པའི་རིགས་དང་རྗེས་སུ་མཐུན་པའི་ཁ་དོག་རྣམ་པར་བསྒོམས་ཏེ། དེའི་སྟེང་དུ་ཡི་གེ་གསུམ་ལས་བྱུང་བའི་ཟླ་བའི་དཀྱིལ་འཁོར་བསམས་ཏེ། འོག་གི་ཟླ་བ་དང་ཉི་མ་དང་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་དེ་ཉིད་དུ་བཞུགས་པར་བསམ་མོ། །

[Block 144]
རྣམ་པར་བྱང་བའི་ཞེན་པ་ཡོངས་སུ་བཟློག་པར་བྱ་བའི་ཕྱིར་སྔགས་འདི་བརྗོད་པར་བྱ་སྟེ། ཨོཾ་དྷརྨ་དྷཱ་ཏུ་ཛྙཱ་ན་བཛྲ་སྭ་བྷཱ་བ་ཨཱཏྨ་ཀོ྅ཧཾ། དེ་ནས་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་ཡི་གེ་གསུམ་པོ་སྔར་བཤད་པའི་ཁ་དོག་ཅན་རྣམ་པར་དགོད་དེ།

[Block 145]
ཡི་གེ་གཉིས་ཐུགས་ཀྱི་རྡོ་རྗེའི་ས་བོན་ལ་ངེས་པར་འཇུག་ཅིང་དེ་ཡོངས་སུ་གྱུར་པ་ལས།

[Block 146]
[^76] རྡོ་རྗེ་དམར་པོ་ཡི་གེ་ཧཱུཾ་གིས་བྱིན་གྱིས་བརླབས་པ། དེའི་འོད་ཟེར་རྣམས་ཀྱིས་ནམ་མཁའི་དབྱིངས་ན་གནས་པའི་དེ་བཞིན་གཤེགས་པའི་ཚོགས་དེ་ཉིད་དུ་འཇུག་པར་བྱས་ལ་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བྱ་སྟེ། བཅོམ་ལྡན་འདས་ཆུ་ཤེལ་གྱི་ནོར་བུའི་འོད་དང་འདྲ་བ་ཞལ་གསུམ་པ་ཕྱག་དྲུག་པ། ཟླ་བའི་དཀྱིལ་འཁོར་ལ་བཞུགས་པ། དཀར་པོ་དང་། ནག་པོ་དང་། དམར་པོ་སྟེ། ཞལ་གསུམ་མཛེས་པ། རལ་པའི་ཐོར༌[^77]ཚུགས་འཛིན་ཅིང་རྡོ་རྗེའི༌[^78]སྐྱིལ་མོ་ཀྲུང་ཅན། རྡོ་རྗེ་དང་། འཁོར་ལོ་དང་། པདྨ་གཡས་ན་བསྣམས་པ། དྲིལ་བུ་དང་། ཡིད་བཞིན་གྱི་ནོར་བུ་དང་། རལ་གྲི་གཡོན་ན་བསྣམས་པ། རྒྱན་ཐམས་ཅད་ཀྱིས་བརྒྱན་པ་བདག་ཉིད་བསྒོམ་པར་བྱ་ཞེས་དབུས་ཀྱི་བདག་པོ་བསྐྱེད་པའི༌[^79]མཚན་ཉིད་ཡན་ལག་བཅུ་དང་ལྡན་པའི་རྣལ་འབྱོར་རོ། །

[Block 147 [HEADING]]
##### རྗེས་སུ་རྣལ་འབྱོར། ^1-1-1-2-0

[Block 148]
དེའི་རྗེས་སུ་རང་གི་སྙིང་གའི་ས་བོན་གྱི་འོད་ཟེར་ལས་བཅོམ་ལྡན་འདས་མི་བསྐྱོད་པ་སྤྲོས་ཏེ་སེམས་ཅན་གྱི་ཁམས་མ་ལུས་པའི་ཉོན་མོངས་པ་ཞེ་སྡང་རྣམ་པར་དག་པར་བྱས་ཏེ། སླར་ཡང་གཤེགས་ཤིང་བདག་རྡོ་རྗེ་འཛིན་པ་ལ་ཞུགས་ཏེ་འོ་མ་དང་ཆུ་བཞིན་དུ་གཅིག་གི་དངོས་པོར༌[^80]གྱུར་པར་བསམ་མོ། །

[Block 149]
དེ་ཞུགས་མ་ཐག་ཏུ་ཉི་མའི་དཀྱིལ་འཁོར་ལ་བཞུགས་པ་ནོར་བུ་ཨིནྡྲ་ནཱི་ལའི་མདོག་ཅན་བཅོམ་ལྡན་འདས་ཞེ་སྡང་རྡོ་རྗེ་མི་བསྐྱོད་པ་ཞེས་བྱ་བ་བསྒོམ་པར་བྱའོ། །

[Block 150]
དེའི་ཐུགས་ཀར་བཾ་ལས་སྐྱེས་པའི་པདྨའི་སྟེང་དུ་ཨ་ལས་སྐྱེས་པའི་ཟླ་བ་ལ་ས་བོན་ཧཱུཾ་ལས་སྐྱེས་པའི་རྡོ་རྗེ་ལས་བྱུང་བའི་ཐུགས་རྡོ་རྗེ་འཛིན་པ་དེ་དང་འདྲ་བར་བསམས་ཏེ། དེའི་ཐུགས་ཀར་དེ་བཞིན་དུ་པདྨ་དང་ཟླ་བ་ལ་གནས་པ། རང་གི་ཆོས་ཀྱི་ཡི་གེ་ཧཱུྃ་ཏིང་ངེ་འཛིན་སེམས་དཔའ་ཞེས་བྱ་བ་རྣམ་པར་དགོད་དེ། ཆོས་དང་ལོངས་སྤྱོད་དང་སྤྲུལ་པའི་སྐུའི་བདག་ཉིད་བསྒོམ་པར་བྱ་ཞེས་རྗེས་སུ་རྣལ་འབྱོར་རོ། །

[Block 151 [HEADING]]
##### ཤིན་ཏུ་རྣལ་འབྱོར། ^1-1-1-3-0

[Block 152]
དེའི་རྗེས་སུ་མིག་གཉིས་ལ་ཐླིཾ་ལས་སྐྱེས་པའི་སའི་སྙིང་པོའོ། །

[Block 153]
རྣ་བ་གཉིས་ལ་ཨོཾ་ལས་སྐྱེས་པའི་ཕྱག་ན་རྡོ་རྗེའོ། །

[Block 154]
སྣ་བུག་གཉིས་ལ་ཨོཾ་ལས་སྐྱེས་པའི་ནམ་མཁའི་སྙིང་པོའོ། །

[Block 155]
ལྕེ་ལ་ཨོཾ་ལས་སྐྱེས་པའི་སྤྱན་རས་གཟིགས་དབང་ཕྱུག་གོ། །

[Block 156]
ལུས་ལ་ཨོཾ་ལས་སྐྱེས་པའི་སྒྲིབ་པ་རྣམ་པར་སེལ་བའོ། །

[Block 157]
ཡིད་ལ་ཨོཾ་ཧཱུཾ་ལས་སྐྱེས་པའི་འཇམ་པའི་དབྱངས་སོ། །

[Block 158]
རྩ་རྒྱུས་ཐམས་ཅད་ལ་ཡི་གེ་མཻཾ་ལས་སྐྱེས་པའི་བྱམས་པའོ། །

[Block 159]
ཡི་གེ་སཾ་ལས་ཀུན་ཏུ་བཟང་པོ་ཚིག་གིས༌[^81]ཐམས་ཅད་ལ་དགོད་པར་བྱའོ། །ཞེས་མིག་ལ་སོགས་པའི་སྐྱེ་མཆེད་བྱིན་གྱིས་བརླབ༌[^82]པའོ། །

[Block 160]
སྲ་བའི་མཚན་ཉིད་ཇི་སྲིད་ཤ་དང་རུས་པ་ལ་སོགས་པའི་ཚོགས་དེ་ལ་ཡི་གེ་ལཾ་ལས་སྐྱེས་པའི་སངས་རྒྱས་སྤྱན་མའོ། །

[Block 161]
ཇི་སྲིད་གཤེར་བའི་མཚན་ཉིད་ཁྲག་ལ་སོགས་པ་དེ་དག་ལ་ཡི་གེ༌[^83]ཨེ་ཝཾ་མ་ལས་སྐྱེས་པའི་མཱ་མ་ཀཱིའོ། །

[Block 162]
ཇི་སྲིད་དྲོད་ཀྱི་ཆ་དེ་དག་ཏུ་ཡི་གེ་བཾ་ལས་སྐྱེས་པའི་གོས་དཀར་མོའོ། །

[Block 163]
ཇི་སྲིད་གཡོ་འགུལ་ལ་སོགས་པ་དེ་དག་ལ་ཡི་གེ༌[^84]ཏཾ་ལས་སྐྱེས་པའི་དམ་ཚིག་སྒྲོལ་མ་དགོད་ཅེས་ཁམས་བྱིན་གྱིས་བརླབ་པའོ། །

[Block 164]
སྤྱི་བོར་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་ཡི་གེ་ཨོཾ་ལས་སྐྱེས་པའི་རྣམ་པར་སྣང་མཛད་དོ། །

[Block 165]
མགྲིན་པར་པདྨའི་སྟེང་དུ་ཡི་གེ་ཨཱཿལས་སྐྱེས་པའི་འོད་དཔག་ཏུ་མེད་པའོ། །

[Block 166]
ཐུགས་ཀའི་རྡོ་རྗེ་དང་ཉི་མའི་སྟེང་དུ་ཡི་གེ་ཧཱུཾ་ལས་སྐྱེས་པའི༌[^85]མི་བསྐྱོད་པའོ། །

[Block 167]
ལྟེ་བར་ཡི་གེ་སྭཱ་ལས་སྐྱེས་པའི༌[^86]རིན་ཆེན་འབྱུང་ལྡན་ནོ། །

[Block 168]
རྐང་པ་དག་ལ་ཡི་གེ་ཧཱ་ལས་སྐྱེས་པ་དོན་ཡོད་གྲུབ་པ་དགོད་པར་བྱ་ཞེས་ཕུང་པོ་བྱིན་གྱིས་བརླབ་པའོ། །

[Block 169]
སླར་ཡང་གཤིན་རྗེ་གཤེད་དཔུང་པ་གཡས་ལའོ། །ཤེས་རབ་མཐར་བྱེད་དཔུང་པ་གཡོན་ལའོ། །

[Block 170]
ཁ་ལ༌[^87]རྟ་མགྲིན་ནོ། །

[Block 171]
རྡོ་རྗེ་ལ་བདུད་རྩི་འཁྱིལ་པའོ། །

[Block 172]
ལག་པ་གཡས་པ་ལ་མི་གཡོ་མགོན་ནོ། །

[Block 173]
གཡོན་པ་ལ་འདོད་པའི་རྒྱལ་པོའོ། །

[Block 174]
པུས་མོ་གཡས་པ་ལ་དབྱུག་སྔོན་ཅན་ནོ། །

[Block 175]
གཡོན་པ་ལ་སྟོབས་པོ་ཆེའོ། །

[Block 176]
སྤྱི་བོ་ལ་གཙུག་ཏོར་འཁོར་ལོས་སྒྱུར་བའོ། །

[Block 177]
རྐང་པའི་འོག་ཏུ་གནོད་མཛེས་ཀྱི་རྒྱལ་པོ་དགོད་པར་བྱ་ཞེས་ཡན་ལག་དང་ཉིང་ལག་ཐམས་ཅད་དུ་དགོད་པ་ནི་ཤིན་ཏུ་རྣལ་འབྱོར་རོ། །

[Block 178 [HEADING]]
##### རྣལ་འབྱོར་ཆེན་པོ། ^1-1-1-4-0

[Block 179]
དེའི་སྤྱི་བོར་ཡི་གེ་ཨོཾ་ལས་བྱུང་བའི་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་ཡི་གེ་ཨོཾ་ཁ་དོག་དཀར་པོ་དགོད་དེ། དེའི་འོད་ཟེར་གྱི་ཚོགས་ལས་ཕྱི་རོལ་དུ་སངས་རྒྱས་སྤྱན་མའི་ཚོགས་སྤྲོས་ཏེ། ནམ་མཁའི་ཁམས་ན༌[^88]འོག་མིན་གྱི་གནས་སུ་བཞུགས་པའི་བཅོམ་ལྡན་འདས་སྐུ་རྡོ་རྗེ་འཁོར་དང་བཅས་པ་སངས་རྒྱས་སྤྱན་མའི་ཚོགས་དེས་རྗེས་སུ་ཆགས་པར་བྱས་ལ་ཕྱག་གི་ཞགས་པས་མགྲིན་པར་བཅིངས་ཏེ་བཀུག་ལ་གཞལ་ཡས་ཁང་པའི་མདུན་དུ་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་བཞུགས་པར་བསམས་ཏེ། འདི་ལྟར་གསོལ་བ་གདབ་པར་བྱ་སྟེ།

[Block 180 [VERSE]]
དཔལ་ལྡན་སངས་རྒྱས་སྐུ་འཆང་བ། །
རྡོ་རྗེ་མི་ཕྱེད་གསུམ་བསྒོམས་པས། །
དེང་བདག་བྱིན་བརླབས་གོ་འཕང་ནི། །
སྐུ་ཡི་རྡོ་རྗེར༌[^89]མཛད་དུ་གསོལ། །
--- END BLOCKS ---
