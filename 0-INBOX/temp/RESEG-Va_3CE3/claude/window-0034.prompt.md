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
འཚལ་བ་མ་མཆིས་པ་ཞེས་བྱ་བ་འདིས་ནི་རྣམ་པར་དག་པ་རྣམ་པར་མི་རྟོག་པའི་མཚན་ཉིད་ཡིན་པར་བསྟན། རྣམ་པར་དག་པས་གཟུགས་མི་ཤེས་སོ་ཞེས་བྱ་བ་འདིས་ནི་ཆོས་རྣམས་དངོས་པོ་མེད་པའི་མཚན་ཉིད་ཡིན་པར་བསྟན་ཏེ། གཉིས་ཀྱིས་ནི་དམིགས་པར་བྱ་བ་དང་། དམིགས་པར་བྱེད་པ་དངོས་པོ་མེད་པའི་མཚན་ཉིད་བསྟན་ཏོ། །

[Block 1192]
བཅོམ་ལྡན་འདས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ལ་སྨན་པར༌[^842]མི་བགྱིད་གནོད་པར་མི་བགྱིད་ཅེས་བྱ་བ་ནི་གང་གི་ཕྱིར་དེ་གཉིས་ཀ་ཡང་དེ་བཞིན་ཉིད་ཀྱི་མཚན་ཉིད་ཀྱིས་ཤིན་ཏུ་རྣམ་པར་དག་པའི་ཕྱིར་ཏེ། དེ་བཞིན་ཉིད་ནི་དེ་བཞིན་ཉིད་ལ༌[^843]ཕན་པའམ་གནོད་པར་མི་བྱེད་དེ། ནམ་མཁའ་ལ་ནམ་མཁའ་བཞིན་ནོ། །

[Block 1193]
དེ་བས་ན་ཆོས་ཀྱི་དབྱིངས་འདུག་པ་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་བཤད་དེ། ཆོས་ཀྱི་སྐུ་ནི་དུས་ཐམས་ཅད་དུ་གནས་པའི་མཚན་ཉིད་ཡིན་ན་དེ་ལ་སུ་ཞིག་ཕན་པ་དང་། གནོད་པ་བྱེད་པ་ཡོད་ཅེས་བསྟན་པའོ། །

[Block 1194]
བཅོམ་ལྡན་འདས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམ་པར་དག་པ་ནི་ཆོས་གང་ཡོངས་སུ་ལེན་པ་མ་མཆིས་སོ་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཤིན་ཏུ་རྣམ་པར་དག་པ་ཡོངས་སུ་འཛིན་པ་ཐམས་ཅད་མེད་པའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་ཏེ། གལ་ཏེ་ཆོས་འགའ་ཞིག་ཡོངས་སུ་འཛིན་ན་རྣམ་པར་དག་པར་མི་འགྱུར་རོ། །

[Block 1195]
དེའི་འོག་ཏུ་གནས་བརྟན་རབ་འབྱོར་གྱིས་བཅོམ་ལྡན་འདས་བདག་རྣམ་པར་དག་པའི་སླད་དུ་གཟུགས་རྣམ་པར་དག་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ནི་བདག་དངོས་པོ་མེད་པ་ཉིད་ཀྱི་ཕྱིར། གཟུགས་ལ་སོགས་པ་དངོས་པོ་མེད་པའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1196]
འདིར་ནི་རྣམ་པར་དག་པ་ཞེས་བྱ་བ་དངོས་པོ་མེད་པ་ལ་བྱ་བའི་ཕྱིར་རོ། །

[Block 1197]
དེ་བས་ན་རབ་འབྱོར་བདག་མེད་པའི་ཕྱིར་གཟུགས་མེད་པ་ནི་ཤིན་ཏུ་རྣམ་པར་དག་པའོ་ཞེས་གསུངས་སོ། །

[Block 1198]
སྔར་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམ་པར་དག་པ་བསྟན་ཏོ། །

[Block 1199]
ད་ནི་བདག་མེད་པ་རྣམ་པར་དག་པ་བསྟན་ཏེ། རབ་འབྱོར་ཤེས་པ་མ་རྙེད་མ་སྟོར་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་སྔོན་མ་བྱུང་བའི་ཡེ་ཤེས་ཐོབ་ཅིང་རྙེད་པ་མེད་ལ། ཡེ་ཤེས་རྙེད་པ་ཡང་ཆུད་ཟོས་པ་མེད་དེ། དེ་ལྟར་གཉིས་ཀ་མེད་པས་བྱང་ཆུབ་ཀྱང་མེད་དོ། །

[Block 1200]
བྱང་ཆུབ་ཅེས་བྱ་བ་ཡང་ཀུན་བརྟགས་པ་ཉིད་དོ། །

[Block 1201]
གཉིས་སུ་མ་མཆིས་ཤིང་རྣམ་པར་དག་པ་ཞེས་བྱ་བ་ནི་ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བ་གཉིས་མེད་པའི་ཕྱིར་སྔོན་གྱི་ཚེ་ཡང་ངོ་བོ་ཉིད་ཀྱིས་རྣམ་པར་དག་པས་ནམ་མཁའ་བཞིན་དུ་ཀུན་ནས་ཉོན་མོངས་པ་མེད་དོ། །

[Block 1202]
ཡོངས་སུ་གྲུབ་པའི་གནས་སྐབས་ན་ཡང་ནམ་མཁའ་བཞིན་དུ་སྔོན་མ་བྱུང་བའི་རྣམ་པར་བྱང་བ་མེད་དོ།། །།

[Block 1203 [HEADING]]
#### ཟབ་པར་ཡིད་ཆེས་པར་བྱ་བ། ^1-2-5-0

[Block 1204 [HEADING]]
##### ཀུན་དུ་མཐའ་ཡས་པ་བཤད་པ། ^1-2-5-1-0

[Block 1205]
བམ་པོ་ཉི་ཤུ་པ། དེ་ལྟར་རྣམ་པར་དག་པ་བཤད་པ་ཡོངས་སུ་རྫོགས་པར་བྱས་ནས། དེའི་འོག་ཏུ་ཟབ་པར་ཡིད་ཆེས་པར་བྱ་བའི་ཕྱིར་ཀུན་དུ་མཐའ་ཡས་པ་བཤད་པར་བརྩམས་པ། གཟུགས་ཀུན་ཏུ་མཐའ་ཡས་པའི་ཕྱིར་ཞེས་བྱ་བ་སྟེ་རྟག་པ་དང་ཆད་པ་མེད་པ་དང་། སྔོན་གྱི་མཐའ་དང་ཕྱི་མའི་མཐའ་དང༌[^844]དབུས་ཀྱི་མཐའ་མེད་པའི་ཕྱིར་ཀུན་ཏུ་མཐའ་ཡས་པའོ། །

[Block 1206]
དེ་བས་ན་རབ་འབྱོར་མཐའ་ལས་འདས་པ༌[^845]སྟོང་པ་ཉིད་དང་ཐོག་མ་དང་ཐ་མ་མེད་པའི་སྟོང་པ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 1207]
རབ་འབྱོར་གྱིས་གསོལ་པ། བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་དེ་ལྟར་རྟོག་པ་གང་ལགས་པ༌[^846]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ལ༌[^847]བྱང་ཆུབ་སེམས་དཔའ༌[^848]ལགས་ཞེས་བྱ་བ་གནས་བརྟན་རབ་འབྱོར་གྱིས་ཅིའི་ཕྱིར་ཞུས་ཤེ་ན། དེ་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཡུལ་དོན་ཟབ་པ་དེ་ཅིའི་སླད་དུ་བྱང་ཆུབ་སེམས་དཔའ་ཉིད་ཀྱི་ལགས་སངས་རྒྱས་རྣམས་ཀྱི་མ་ལགས་ཞེས་ཞུས་པའོ། །

[Block 1208]
རབ་འབྱོར་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་མཐར་ཕྱིན་ཅིང་། བྱ་བ་བྱས་པ་མ་ཡིན་གྱི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ལམ་གྱི་རྣམ་པ་སྟེ། དེ་བས་ན་བྱང་ཆུབ་སེམས་དཔའ་ཉིད་ཀྱིས༌[^849]ཞེས་བྱའོ། །

[Block 1209]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཚུ་རོལ་གྱི་འགྲམ་མམ། ཕ་རོལ༌[^850]འགྲམ་མམ། གཉིས་ཀ་མ་མཆིས་པ་ལ་ཡང་མི་དམིགས་སོ་ཞེས་བྱ་བ་ཅི་ལས་དགོངས་ཤེ་ན་ཕ་རོལ་ཏུ་སོན་པའམ། ཕ་རོལ་གྱི་མཐར་ཕྱིན་པའམ། ཕ་རོལ་གྱི་ངོ་བོ་ཉིད་ལ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་གྲང་ན། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡིན་དུ་ཟིན་ཀྱང་། ཚུ་རོལ་གྱི་འགྲམ་ན་ཡང་མི་གནས་ཕ་རོལ་གྱི་འགྲམ་ན་ཡང་མི་གནས་འགྲམ་འདི་གཉིས་ལས་མ༌[^851]གཏོགས་པ་གཞན་དུ་འང་མི་དམིགས་པའི་ཕྱིར་དེ་སྐད་གསུངས་ཏེ། ཚུ་རོལ་གྱི་འགྲམ་ཞེས་བྱ་བ་ནི་འདུས་བྱས་སུ་གཏོགས་པའོ། །

[Block 1210]
ཕ་རོལ་གྱི་འགྲམ་ཞེས་བྱ་བ་ནི་འདུས་མ་བྱས་སུ་གཏོགས་པའོ། །

[Block 1211]
དེ་སྐད་གསོལ་པ་དང་བཅོམ་ལྡན་འདས་ཀྱིས་ཤིན་ཏུ་རྣམ་པར་དག་པའི་ཕྱིར་རོ་ཞེས་གསུངས་ཏེ། གལ་ཏེ་འགྲམ་འགའ་ཞིག་དམིགས་ན་དེ་ལྟ་ན་ནི་རྣམ་པར་དག་པ་ཉིད་དུ་མི་འགྱུར་ཏེ། གང་གི་ཕྱིར་གང་ཡང་མེད་པ་དེའི་ཕྱིར་ཤིན་ཏུ་རྣམ་པར་དག་པ་སྟེ། ཤིན་ཏུ་རྣམ་པར་དག་པ་ཉིད་ཀྱི་ཕྱིར་འགྲམ་གཉིས་དང་། གཞན་ན་ཡང་མི་གནས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1212]
རབ་འབྱོར་དུས་གསུམ་མཉམ་པ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཐོག་མ་དང་ཐ་མ་མེད་པའི་སྟོང་པ་ཉིད་ཀྱི་ཕྱིར་དུས་གསུམ་མཉམ་པ་ཉིད་དུ་ཡོངས་སུ་ཤེས་པས་ཚུ་རོལ་གྱི་འདུ་ཤེས་སམ་ཕ་རོལ་གྱི་འདུ་ཤེས་མེད་དེ། དེ་བས་ན་ཚུ་རོལ་གྱི་འགྲམ་ན་ཡང་མི་གནས་ཕ་རོལ་གྱི་འགྲམ་ན་ཡང་མི་གནས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1213 [HEADING]]
##### ཆགས་པ་དང་མ་ཆགས་པ་བཤད་པ། ^1-2-5-2-0

[Block 1214]
དམིགས་པ་དང་མི་དམིགས་པར་སྤྱོད་པའི་དབང་གིས་ཟབ་པར་ཡིད་ཆེས་པར་བྱ་བའི་ཕྱིར། དེའི་འོག་ཏུ་ཆགས་པ་དང་། མ་ཆགས་པ་བཤད་པའི་སྐབས་ཕྱེ་བ་ཡང༌[^852]མིང་དུ་ཡང་ཆགས་པ་ཡིན། མཚན་མར་ཡང་ཆགས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་ལ་མིང་དུ་འཛིན་པ་ནི་ཀུན་བརྟགས་པའོ[^853]། །བརྡ་ལ༌[^854]མཚན་མར་འཛིན་པ་ནི་རྣམ་པར་བརྟགས་པ་སྟེ། གཉི་ག་ཡང་སྒྲིབ་པའི་བདག་ཉིད་ཡིན་པས་ཆགས་པ་ཞེས་བྱའོ། །

[Block 1215]
རབ་འབྱོར་ཆོས་ཐམས་ཅད་ནི༌[^855]མཚན་མ་མེད་པ་སྟེ། མིང་མེད་པའོ་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྤྱོད་ཡུལ་ཡིན་པར་བསྟན་པའོ། །

[Block 1216]
བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་དེ་ལྟར་ལེགས་པར་བཤད་ཅིང་ལེགས་པར་མཐར་གཏུགས་པ་ནི་ངོ་མཚར་ཆེའོ་ཞེས་བྱ་བ་ནི་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་བསྟན་པའོ། །

[Block 1217]
གཟུགས་སྟོང་ཞེས་བྱ་བར་འདུ་ཤེས་ན་ཆགས་པའོ་ཞེས་བྱ་བ་ནི་དམིགས་པའི་ཚུལ་གྱིས་དེ་ལྟར་སེམས་པའོ།[^856] །གཟུགས་ལ་གཟུགས་ཞེས་བྱ་བར་འདུ་ཤེས་མེད་དོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི༌[^857]ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་དོ། །

[Block 1218]
ཆོས་རྣམས་ལ་ཆོས་ཞེས་བྱ་བར་འདུ་ཤེས་འདུ་ཤེས༌[^858]མེད་དོ་ཞེས་བྱ་བ་ནི་མི་སྣང་བའོ། །

[Block 1219]
ཀཽ་ཤི་ཀ་གཟུགས་ཀྱི་རང་བཞིན་ཡོངས་སུ་བསྔོ་བར་མི་ནུས་སོ་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་གནས་པའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་ཡོངས་སུ་འགྱུར་བ་མེད་པས་དམིགས་པའི་ཚུལ་གྱིས་བྱང་ཆུབ་ཏུ་ཡོངས་སུ་བསྔོ་བར་མི་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1220]
རབ་འབྱོར་ཁྱོད་ལ་ཆགས་པའི་རྣམ་པ་དེ་བས་ཀྱང་ཕྲ་བ་གཞན་དག་ཀྱང་བསྟན་པར་བྱ་ཞེས་བྱ༌[^859]བ་ནི་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ལ་སྒྲིབ་པར་འགྱུར་བའོ། །

[Block 1221 [HEADING]]
##### ཟབ་མོ་ཁོང་དུ་ཆུད་པ་བསྟན་པ། ^1-2-5-3-0

[Block 1222]
བཅོམ་ལྡན་འདས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཟབ་པོ་ཞེས་བྱ་བ་ནི་སྔར་གནས་བརྟན་ཤཱ་རིའི་བུས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་པ་དང་། མོས་པར་དཀའ་བར་ཡིད་ཆེས་པར་བྱ་བའི་ཕྱིར་བཤད་པའི་སྐབས་ཕྱེ་བས། ད་ནི་གནས་བརྟན་རབ་འབྱོར་གྱིས་བདག་ཉིད་ཀྱིས་ཟབ་མོ་ཁོང་དུ་ཆུད་པ་བསྟན་པའི་ཕྱིར། བཅོམ་ལྡན་འདས་ཟབ་པོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 1223]
རབ་འབྱོར་ཆོས་ཐམས་ཅད་རང་བཞིན་གྱིས་རྣམ་པར་དབེན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཆོས་ཐམས་ཅད་ནི་དུས་ཐམས་ཅད་དུ་ཆགས་པ་ཐམས་ཅད་ཡོངས་སུ་སྤངས་པ། རང་བཞིན་ཡོངས་སུ་སྤངས་པ་རང་བཞིན་གྱིས་དབེན་པ་ཡིན་ན། འོན་ཀྱང་ཀུན་བརྟགས་པའི་ཆགས་པ་ཡང་དམིགས་ལ་ཀུན་བརྟགས་པའི་ཆགས་པ་དམིགས་ཀྱང་ཆོས་ཐམས་ཅད་ནི་ངོ་བོ་ཉིད་ཀྱིས་གོས་པ་མེད་པ་སྟེ་དབེན་པའི་ཕྱིར་ཟབ་པའོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་མ་བྱས་པ་མངོན་པར་འདུས་མ་བྱས་པ་ཞེས་བྱ་བ་ནི། ཆོས་ཀྱི་སྐུའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་དེ་ལ་བསྒྲུབ་པར་བྱ་བ་འམ་མངོན་པར་འདུ་བྱ་བ་མེད་དོ། །

[Block 1224]
ཆོས་ཀྱི་རང་བཞིན་ནི་གཉིས་མ་ཡིན་ཏེ། གཅིག་ཏུ་ཟད་དོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་དུ་ཆོས་ཐམས་ཅད་ངོ་བོ་ཉིད་གཅིག་ན་འོན་ཀྱང་བདག་ཉིད་ཐ་དད་པར་སྣང་བའི་ཕྱིར། མངོན་པར་རྟོགས་པར་དཀའ་བའོ། །

[Block 1225]
དེ་བཞིན་ཉིད་ཆོས་རྣམས་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རང་བཞིན་ཞེས་བྱའོ། །

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
--- END BLOCKS ---
