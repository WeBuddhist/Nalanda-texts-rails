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
[Block 2171]
ཟག་པ་མེད་པའི་དང་པོ་ནི་གཉིས་ལས་ཏེ། རྒྱུ་གཅིག་ལས་བྱུང་བའི་ཆོས་ནི་མེད་དོ། །

[Block 2172]
རྒྱུ་རྒྱ་ཆེར་བཤད་པ་རྫོགས་སོ། །

[Block 2173]
[^1141]

[Block 2174 [HEADING]]
### རྐྱེན་རྣམས། ^2-5-0

[Block 2175]
རྐྱེན་རྣམས་གང་ཞེ་ན། རྐྱེན་ནི་བཞི་པོ་དག་ཏུ་གསུངས། །

[Block 2176 [HEADING]]
#### རྐྱེན་ཉིད་བཞི། ^2-5-1-0

[Block 2177]
གང་ནས་གསུངས་ཤེ་ན། མདོ་ལས་རྐྱེན་ཉིད་ནི་བཞི་སྟེ་རྒྱུའི་རྐྱེན་ཉིད་དང་། དེ་མ་ཐག་པའི་རྐྱེན་ཉིད་དང་། དམིགས་པའི་རྐྱེན་ཉིད་དང་། བདག་པོའི་རྐྱེན་ཉིད་དོ་ཞེས་གསུངས་སོ། །

[Block 2178]
རྐྱེན་དུ་འདྲ་བ་ནི་རྐྱེན་ཉིད་དོ། །

[Block 2179 [HEADING]]
##### རྒྱུའི་རྐྱེན། ^2-5-1-1-0

[Block 2180]
དེ་ལ༌[^1142]རྒྱུ་ཞེས་བྱ་བ་རྒྱུ་ལྔ་ཡིན། བྱེད་རྒྱུའི་རྒྱུ་མ་གཏོགས་པ་རྒྱུ་ལྔ་ནི་རྒྱུའི་རྐྱེན་ཡིན་ནོ། །

[Block 2181 [HEADING]]
##### མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན། ^2-5-1-2-0

[Block 2182 [VERSE]]
སེམས་དང་སེམས་བྱུང་སྐྱེས་པ་རྣམས། །
ཐ་མ་ཡིན༌[^1143]མཚུངས་དེ་མ་ཐག །

[Block 2183]
དགྲ་བཅོམ་པའི་ཐ་མ་མ་གཏོགས་པ་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ནི་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ཡིན་ཏེ། རྐྱེན་འདི་ནི་མཚུངས་པ་ཡང་ཡིན་ལ་དེ་མ་ཐག་པའི༌[^1144]ཡང་ཡིན་པས་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ཏོ། །

[Block 2184]
དེ་ཉིད་ཀྱི་ཕྱིར་མི་མཉམ་པར་འབྱུང་བའི་ཕྱིར་གཟུགས་ནི་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་མ་ཡིན་ཏེ། འདི་ལྟར་འདོད་པ་ན་སྤྱོད་པའི་གཟུགས་ཀྱི་མཇུག་ཐོགས་སུ་རེས་འགའ་ནི༌[^1145]འདོད་པ་ན་སྤྱོད་པ་དང་། གཟུགས་ན་སྤྱོད་པའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་གཟུགས་འབྱུང་ངོ་། །རེས་འགའ་ནི་འདོད་པ་ན་སྤྱོད་པ་དང་ཟག་པ་མེད་པ་འབྱུང་བས་གཟུགས་མངོན༌[^1146]དུ་འགྱུར་བ་འཆོལ་པ་ཡིན་ནོ། །

[Block 2185]
མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ནི་འཆོལ་པ་མ་ཡིན་ནོ། །

[Block 2186]
བཙུན་པ་དབྱིག༌[^1147]བཤེས་ན་རེ་རྒྱས་པ་ལས་བྱུང་བའི་གཟུགས་ཀྱི་རྒྱུད་གཅིག་མ་འགགས་པ་ཁོ་ནར་གཉིས་པ་འབྱུང་བའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 2187]
བཙུན་པ་ན་རེ་ཆེས་མང་བ་དང་ཉུང་ངུ་འབྱུང་བའི་ཕྱིར་ཏེ། རེས་འགའ་ནི་གཟུགས་མང་པོ༌[^1148]ལས་ཉུང་ངུ་འབྱུང་སྟེ། དཔེར་ན་སོག༌[^1149]མའི་ཐལ་བ་ལྟ་བུའོ། །

[Block 2188]
རེས་འགའ་ནི་ཉུང་ངུ་ལས་མང་པོ་འབྱུང་སྟེ། དཔེར་ན་ཤིང་པ་ཏའི་ས་བོན་ཆུང་ངུ་ལས་རིམ་གྱིས་ཡལ་ག་དུ་མ་སྐྱེ་བ་དང་ལྡན་པའི༌[^1150]ཤིང་ནྱ་གྲོ་དྷའི་བར་ལྟ་བུའོ་ཞེས་ཟེར་རོ། །

[Block 2189]
སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ལ་ཡང་དགེ་བ༌[^1151]དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པའི་སེམས་དག་དང་། རྟོག་པ་དང་དཔྱོད་པ་དང་བཅས་པ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་གསུམ་ལ་ཆེས་མང་བ་དང་ཉུང་ངུ་འབྱུང་བ་མ་ཡིན་ནམ་ཞེ་ན། རིགས་གཞན་ལ་ནི་ཡོད་ཀྱི་རང་གི་རིགས་ལ་ནི་མེད་དེ། ནམ་ཡང་ཚོར་བའམ་འདུ་ཤེས་ལ་སོགས་པ་ཆེས་མང་དུ་འབྱུང་བ་མེད་དོ། །

[Block 2190]
ཡང་ཅི་རང་གི་རིགས་ཁོ་ནའི་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ཡིན་ནམ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། འདིར་ནི་ཚོགས་མཐའ་དག་ཁོ་ན་ཚོགས་མཐའ་དག་གཞན་གྱི་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ཡིན་གྱི། འདིར་ནི་ཚོར་བ་ལ་སོགས་པའི་རྫས་ཉུང་ངུ་ལས་ཚོར་བ༌[^1152]ལ་སོགས་པའི་རྫས་མང་པོ་འབྱུང་བ་ནི་མ་ཡིན་ནོ༌[^1153]ཞེས་བྱ་བ་དེ་ཙམ་ཞིག་བཤད་པར༌[^1154]ཟད་དོ། །

[Block 2191]
རྒྱུད་འདྲ་བ་དག་ནི་རང་གི་རིགས་ཁོ་ནའི༌[^1155]མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ཡིན་ཏེ། སེམས་ཀྱང་སེམས་ཁོ་ནའི་ཡིན་ལ། ཚོར་བ་ཡང་ཚོར་བ་ཁོ་ནའི་ཡིན་ནོ་སྙམ་དུ་རྒྱས་པར་སེམས་ཤིང་གང་གི་ཚེ་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་མཇུག༌[^1156]ཐོགས་སུ་ཉོན་མོངས་པ་ཅན་འབྱུང་བའི༌[^1157]ཉོན་མོངས་པ་དེའི་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ནི་སྔོན་འགགས་པའི་ཉོན་མོངས་པ་ཡིན་ཏེ། དཔེར་ན་ལྡང་བའི་སེམས་ཀྱི་འགོག་པ་ལ་སྙོམས་པར་འཇུག་པའི་སེམས་ལྟ་བུའོ་ཞེས་ཟེར་ཏེ། དེ་སྐད་དུ་ནི་མི་བརྗོད་དོ། །

[Block 2192]
ལྡན་པ་མ་ཡིན་པའི་འདུ་བྱེད་རྣམས་ཀྱང་འཆོལ་བར་མངོན་དུ་གྱུར་པ་དེ་ཉིད་ཀྱི་ཕྱིར་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་མ་ཡིན་ཏེ། ཁམས་གསུམ་པ་དང་ལྡན་པ་མ་ཡིན་པ་རྣམས་ཅིག་ཅར་མངོན་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2193]
ཅིའི་ཕྱིར་མ་འོངས་པ་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་དུ་མི་འདོད་ཅེ་ན། མ་འོངས་པའི་དུས་ནི་འཆོལ་བ་ཡིན་པའི་ཕྱིར་ཏེ། སྔ་ཕྱི་མེད་པའི་ཕྱིར་རོ། །

[Block 2194]
འོ་ན་བཅོམ་ལྡན་འདས་ཀྱིས་མ་འོངས་པ་ཆེ་གེ་མོ་ཞིག་གི་མཇུག་ཏུ་མ་འོངས་པ་འདི་འབྱུང་ངོ་ཞེས་བྱ་བར་ཇི་ལྟར་མཁྱེན་ཅེ་ན། འདས་པ་དང་ད་ལྟར་གྱི་ལས་རྗེས་སུ་དཔག་པའི༌[^1158]ཕྱིར་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་ལས་འདི་ལྟ་བུའི་རྣམ་པར་སྨིན་པ་ནི་འདི་ལྟ་བུ་འམ་ཆོས་ལས་ཆོས༌[^1159]སྐྱེས་སོ་ཞེས་བྱ་བར་འདས་པའི་དུས་གཟིགས་ལ། ད་ལྟའི་ལས་འདི་ཡང་དེ་ལྟ་བུ་ཡིན་པས། དེ་ལྟ་བས་ན་འདི་ལས་ཀྱང་རྣམ་པར་སྨིན་པ་དེ་ལྟ་བུའམ། ཆོས་ལས་ཆོས་སྐྱེ་བར༌[^1160]འགྱུར་རོ་ཞེས་བྱ་བར་མཁྱེན་ལ། དེའི་མཁྱེན་པ་དེ་ཡང་རྗེས་སུ་དཔག་པ་ལས་བྱུང་བ་ཡང་མ་ཡིན་ཏེ། འདི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་འདས་པ་དང་ད་ལྟར་ལས་རྗེས་སུ་དཔག༌[^1161]ནས་མ་འོངས་པའི་རྫས་འཆོལ་པ་རྣམས་མངོན་སུམ་དུ་བརྟགས་ཏེ། གང་ཟག་འདིས་ལས་འདི་ལྟ་བུ་བྱས་པས་མ་འོངས་པའི་འབྲས་བུ་འདི་ཡོངས་སུ་བཟུང་ངོ་ཞེས་བྱ་བར་མཁྱེན་ཏོ་ཞེས་གྲག་གོ། །

[Block 2195]
དེ་ལྟ་ན་བཅོམ་ལྡན་འདས་ཀྱིས་སྔོན་གྱི་མཐའ་མ༌[^1162]གཟིགས་པར་ཕྱི་མའི་མཐའ་མི་མཁྱེན་པར་འགྱུར་རོ། །

[Block 2196]
གཞན་དག་ན་རེ་སེམས་ཅན་རྣམས་ཀྱི་རྒྱུད་ལ་འབྲས༌[^1163]བུའི་རྟགས་སུ་གྱུར་པ་སེམས་དང་ལྡན་པ་མ་ཡིན་པའི་འདུ་བྱེད་ཀྱི་ཁྱད་པར་ཞིག་ཡོད་དེ། བཅོམ་ལྡན་འདས་ཀྱིས་དེ་གཟིགས་ནས་བསམ་གཏན་ནམ་མངོན་པར་མཁྱེན་པ་མངོན་དུ༌[^1164]མཛད་བཞིན་དུ་ཡང་མ་འོངས་པ་མཁྱེན་ཏོ་ཞེས་ཟེར་རོ། །

[Block 2197]
མདོ་སྡེ་པ་རྣམས་ན་རེ་དེ་ལྟར༌[^1165]ན་བཅོམ་ལྡན་འདས་མཚན་མཁན༌[^1166]ཁོ་ན་ཡིན་པར་འགྱུར་གྱི་མངོན་སུམ་དུ་མཛད་པ་ནི་མ་ཡིན་ནོ། །

[Block 2198]
དེ་ལྟ་བས་ན་བཅོམ་ལྡན་འདས་ནི་བཞེད་པ་ཙམ་གྱིས་ཐམས་ཅད་མཁྱེན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་སངས་རྒྱས་རྣམས་ཀྱི་ཡུལ་ནི་བསམ་གྱིས་མི་ཁྱབ་བོ་ཞེས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 2199]
མ་འོངས་པའི་གོ་རིམས་ངེས་པར་གནས་པ་མེད་ན་ཅིའི་ཕྱིར་ཆོས་ཀྱི་མཆོག་གི་མཇུག་ཐོགས་སུ་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་ཁོ་ན་སྐྱེའི་གཞན་ནི་མ་ཡིན་ནོ། །

[Block 2200]
དེ་བཞིན་དུ་རྡོ་རྗེ་ལྟ་བུའི་མཇུག་ཐོགས་སུ་ཟད་པ་ཤེས་པ་ཁོ་ན་སྐྱེའི་གཞན་མ་ཡིན་པའི་བར་དུ་ཡིན་ཞེ་ན། གང་ཞིག་གང་ལ་རག་ལས་ཏེ་སྐྱེ་བ་དེ་ནི་དེའི་མཇུག་ཐོགས་སུ་སྐྱེ་སྟེ། དཔེར་ན་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་མེད་བཞིན་དུ་ཡང་ས་བོན་ལ་སོགས་པའི་མྱུ་གུ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 2201]
ཅིའི་ཕྱིར་དགྲ་བཅོམ་པའི་སེམས་དང་སེམས་ལས་བྱུང་བ་ཐ་མ་རྣམས་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་མ་ཡིན་ཞེ་ན། སེམས་གཞན་དང་འབྲེལ་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2202]
དེ་ལྟ་ན་འགགས་མ་ཐག་པའི་སེམས་ཡིད་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་མ་ཐག་པའི་རྣམ་པར་ཤེས་པ་མེད་པའི་ཕྱིར་སེམས་ཐ་མ་ཡིད་དུ་ཡང་མི་འགྱུར་བ༌[^1167]མ་ཡིན་ནམ། ཡིད་ནི་རྟེན་གྱི་དངོས་པོས་རབ་ཏུ་ཕྱེ་བ་ཡིན་གྱི། བྱེད་པས་རབ་ཏུ་ཕྱེ༌[^1168]བ་ནི་མ་ཡིན་པས་རྟེན་ནི་ཡོད་པ་ཉིད་ཀྱི་རྒྱུ་མ་ཚང་བས་རྣམ་པར་ཤེས་པ་གཞན་མི་སྐྱེ་བ་ཁོ་ནར་ཟད་དོ། །

[Block 2203]
མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ནི་བྱེད་པས་རབ་ཏུ་ཕྱེ་བ་ཡིན་ནོ། །

[Block 2204]
དེས་ཆོས་གང་འབྲས་བུར་གཟུང་བ༌[^1169]དེ་ནི་ཆོས་ཐམས་ཅད་དམ་སྲོག་ཆགས་ཐམས་ཅད་ཀྱིས་ཀྱང་ཇི་ལྟར་ཡང་མི་སྐྱེ་བར་དགག་པར་མི་ནུས་སོ། །

[Block 2205]
ཆོས་གང་དག་སེམས་ཀྱི་མཚུངས་པ་དེ་མ་ཐག་པ་ཅན་ཡིན་པ་དེ་དག་སེམས་ཀྱི་དེ་མ་ཐག་པ་ཅན་ཡང་ཡིན་ནམ༌[^1170]ཞེ་ན། མུ་བཞི་སྟེ། མུ་དང་པོ་ནི་སེམས་མེད་པའི་སྙོམས་པར་འཇུག་པ་ལས་ལྡང་བའི་སེམས་དང་། སྙོམས་པར་འཇུག་པའི་སྐད་ཅིག་མ་གཉིས་པ་ལ་སོགས་པ་དག་གོ། །

[Block 2206]
མུ་གཉིས་པ་ནི་སྙོམས་པར་འཇུག་པའི་སྐད་ཅིག་མ་དང་པོ་དང་སེམས་དང་བཅས་པའི་གནས་སྐབས་ཀྱི་སྐྱེ་བ་ལ་སོགས་པའོ། །

[Block 2207]
མུ་གསུམ་པ་ནི་སྙོམས་པར་འཇུག་པའི་སྐད་ཅིག་མ་དང་པོ་དང་། སེམས་དང་བཅས་པའི་གནས་སྐབས་དག་གོ། །

[Block 2208]
མུ་བཞི་པ་ནི་སྙོམས་པར་འཇུག་པའི་སྐད་ཅིག་མ་གཉིས་པ་ལ་སོགས་པ་དང་། ལྡང་བའི་སེམས་ཀྱི་སྐྱེ་བ་ལ་སོགས་པའོ། །

[Block 2209]
ཆོས་གང་དག་སེམས་ཀྱི་མཚུངས་པ་དེ་མ་ཐག་པ་ཅན་ཡིན་པ་དེ་དག་སྙོམས་པར་འཇུག་པའི་དེ་མ་ཐག་པ་ཅན༌[^1171]ཡིན་ནམ་ཞེ་ན། མུ་བཞི་སྟེ།

[Block 2210]
གསུམ་པ་དང་བཞི་པ་གང་དག་ཡིན་པ་དེ་དག་ནི་དང་པོ་དང་གཉིས་པ་དག་གོ། །
--- END BLOCKS ---
