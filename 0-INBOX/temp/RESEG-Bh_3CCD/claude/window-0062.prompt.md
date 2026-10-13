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
དེ་ནས་དེའི་ཡན་ལག་ཁོ་ན་རིམ་པ་གཉིས་གཙོར་གྱུར་པའི་བཤད་པ་ནི་རྣམ་པ་བཞིའོ། །

[Block 2172]
འཆད་པའི་རྒྱན་ལྔ་པ་སྟེ་རྣམ་པ་གཉིས་སོ། །

[Block 2173]
ཉན་པ་པོའི་རྒྱན་དྲུག་པ་སྟེ་རྣམ་པ་ལྔའོ། །

[Block 2174]
བདུན་པའི་དབྱེ་བ་རྣམ་པ་གཉིས་ཏེ་ཞེས་བྱ་བ་ལ་བརྗོད་པར་བྱ་བའི་དོན་མ་ལུས་པ་བསྡུས་པའི༌[^1461]རྒྱན་ཡིན་ཏེ་རིམ་པ་གཉིས་གཙོར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 2175]
དེ་ལས་གཞན་པ་རྒྱན༌[^1462]མེད་དེ་མི་དགོས་པའི་ཕྱིར་རོ། །

[Block 2176]
མདོར་བསྡུས་པ་ནི་མདོར་བསྟན་པས་སོ། །

[Block 2177]
དེའི་དགོངས་པ་ནི་འདི་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཛིན་པས་ངག་ཇི་སྲིད་གསུམ་པ༌[^1463]དེ་དག་ཟབ་པ་དང་རྒྱ་ཆེ་བ་དང་། སྣ་ཚོགས་ཀྱི་དོན་སྟོན་པར་བྱེད་པའི་ཕྱིར། རྒྱན་དུ་མ་དང་ལྡན་པ་ཡིན་པས་མདོར་བསྡུས་པ་ནི་འདིར་བདུན་གཟུང་བར་བྱས་སོ། །

[Block 2178]
རྒྱས་པར་བསྟན་པར་བྱ་བའི་ཕྱིར། བཤད་པའི་རྒྱུད་ཀྱི་རྗེས་སུ་འབྲངས་ནས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། དགོངས་པ་ལུང་བསྟན་པ་ལ་སོགས་པའི་བཤད་པའི་རྒྱུད་ཀྱི་རྗེས་སུ་འབྲངས་ནས་ཞེས་བྱ་བ༌[^1464]འདིས་རང་བཟོར་བཀག་པ་བསྟན་ཏོ། །

[Block 2179]
རྒྱན་ནི་བདུན་པོ་རྣམས་ཀྱིས་ནི། །ཞེས་བྱ་བ༌[^1465]ངེས་པར་གཟུང་བའི༌[^1466]དྲུག་པའོ། །

[Block 2180]
རིམ་པ་བཞིན་དུ་ནི་མདོར་བསྟན་པའི་ཚིག་གི་རྗེས་སུ་འབྲང་བས༌[^1467]སོ། །

[Block 2181]
རེ་རེ་ཡི་ནི་གླེང་བསླངས་པ༌[^1468]ལ་སོགས་པ་རྣམས་ཀྱིའོ། །

[Block 2182]
བསྟན་པ་དག་ཅེས་པ་ནི་ཁོ་བོས་འཆད་དོ། །

[Block 2183 [VERSE]]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། །
རྒྱུད་འདིའི་མིང་ནི་ཅི་ཞིག་ཡིན། །

[Block 2184]
ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པས་དྲི་ཚིག་ལྔ་བསྟན་ཏོ། །

[Block 2185]
ལན་སྨྲས་པ། རྒྱུད་ཀྱི་མཚན་ནི་མིང་ཡིན་ལ། ཞེས་པ་ནི་མཚན་ནི་མིང་སྟེ། དེ་ཡང་རྒྱུད་རྗོད་པར་བྱེད་པ་དཔལ་གསང་བ་འདུས་པ་ཞེས་བྱའོ། །

[Block 2186]
ཇི་སྐད་དུ།

[Block 2187 [VERSE]]
བསྟན་བཅོས་དག་ནི་ཐམས་ཅད་ཀྱི། །
ལས་རྣམས་གང་ཅིའང་རུང་བ་ཡི། །
མིང་མེད་པས་ནི་འཇིག་རྟེན་འདི། །
ལོང་བའམ་ལྐུགས་པ༌[^1469]འདྲ་བར་འགྱུར། །

[Block 2188]
ཞེས་འབྱུང་ངོ་། །སྐྱེ་བོ་འདོད་ཆགས་ཅན་དོན་དུ། །ཞེས་པ་ནི་དོན་དུ་རྒྱུ་མཚན་ཏེ་རྒྱུའོ། །

[Block 2189]
གང་ལ་བརྟེན༌[^1470]ཏེ་བཅོམ་ལྡན་འདས་ཀྱིས༌[^1471]རྒྱུད་གསུངས་སོ། །

[Block 2190]
འདོད་ཆགས་ཅན་ཞེས་ཉེ་བར་མཚོན་པ་སྟེ་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པ་ལྔས་དཀྲུགས་པའི་སྐྱེ་བོ་རྣམས་ལ་གཟིགས་ནས་དེ་རྣམས་སྦྱང་བར༌[^1472]བྱ་བའི་ཕྱིར་རིམ་པ་གཉིས་སྟོན་པར་བྱེད་པའི་རྒྱུད་གསུངས་ཏེ། ཇི་སྐད་དུ།

[Block 2191 [VERSE]]
ཞེ་སྡང་གཏི་མུག་འདོད་ཆགས་དང་། །
ཡིད་བཞིན་ནོར་བུ་དམ་ཚིག་སྟེ། །
རིགས་ལྔར་གཏོགས་པ་འདི་རྣམས་ཀྱིས། །
འདོད་དང་ཐར་པ་རབ་བསྒྲུབ་པའོ། །

[Block 2192]
ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2193]
དེ་ལྟར་འདོད་ཆགས་ལ་སོགས་པའི་རིགས་ཅན་གྱི་སྐྱེ་བོ་རྗེས་སུ་གཟུང་བར་བྱེད་པ་རིམ་པ་གཉིས་པོ་ནི་བརྗོད་པར་བྱའོ། །

[Block 2194]
ཇི་སྐད་དུ།

[Block 2195 [VERSE]]
བརྗོད་བྱ་མེད་པའི་ངག་རྣམས་ནི། །
གང་ཕྱིར་བྱ་རོག་སྐད་བཞིན་ནོ། །
དེའི་ཕྱིར་བསྟན་བཅོས་བརྩམས་དུས་སུ། །
བརྗོད་བྱ་སྔོན་དུ་མངོན་པར་བརྗོད། །

[Block 2196]
ཅེས་འབྱུང་ངོ་། །

[Block 2197]
བརྗོད་བྱ་དང་རྗོད་པར་བྱེད་པ་འདི་དག་གི་ཐབས་དང་ཐབས༌[^1473]ལས་བྱུང་བའི་མཚན་ཉིད་ཀྱི་འགྲེལ་པ་མ་བཤད་ཀྱང་ཤེས་པར་བྱ་སྟེ།

[Block 2198 [VERSE]]
དེ་དག་གནས་པའི་ཕྱིར་རོ། །
འདི་ཡི༌[^1474]བྱེད་པོ་རྡོ་རྗེ་སེམས། །

[Block 2199]
ཞེས་པ་ནི་རྡོ་རྗེ་སེམས་དཔའ་བྱེད་པ་པོ་ཡིན་པས་ཉན་པ་པོ་རྣམས་བཀུར་སྟི་དང་བཅས་པར༌[^1475]འཇུག་པར་འགྱུར་བ་དེ་ཉིད་ཀྱི་ཕྱིར་ཟུར་གྱིས་འབྲེལ་པ་ཡང་བསྟན་ཏོ། །

[Block 2200]
དཔེར་ན་དགའ་ལྡན་གྱི་གནས་སུ་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་སེམས་དཔའ་དཔལ་གསང་བ་འདུས་པའི་རྒྱུད་གསུངས་པ་ན་དེ་ལ་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་ཞུས་པར་གྱུར་ཏོ་ཞེས་དོན་གྱི་ཤུགས་ཀྱིས་ཉན་པ་པོ་དང་འཆད་པ་པོའི་འབྲེལ་པ་ཡིན་ནོ། །

[Block 2201]
གང་ལ་བརྟེན་ཏེ་འཆད་པ་པོས་བཤད་པ་དང་། ཉན་པ་པོས་ཉན་པ་དེ་ནི་སྒྲ་དང་དོན་གྱི་འབྲེལ་པ་རྟོགས་པར་བྱའོ། །

[Block 2202]
ཇི་སྐད་དུ།

[Block 2203 [VERSE]]
གང་ཕྱིར་འབྲེལ་པ་ཡོད་པས་ན། །
ཉན་པ་པོ་ཡི་འཇུག་འགྲུབ་པ། །
དེ་ཕྱིར་བསྟན་བཅོས་ཐམས་ཅད་ཀྱི། །
སྔོན་དུ་འབྲེལ་པ་རྟོགས་པར་བྱ། །

[Block 2204]
ཞེས་འབྱུང་ངོ་། །ཚད་དག་ཀྱང་ནི་བཤད་བྱ་སྟེ། །ཞེས་བྱ་བ་ནི་བརྗོད་པར་བྱ་བ་དང་རྗོད་པར་བྱེད་པའི་བསྟན་བཅོས་ཀྱི་ཁྱད་པར་རོ། །

[Block 2205]
དེ་ཡང་བརྗོད་བྱ་དང་རྗོད་བྱེད་གཉིས་ཀའི་ཡན་ལག་ལས་གཞན་མ་ཡིན་ནོ། །

[Block 2206]
ལེའུ་དེ་བཞིན་ཆོ་ག་དང་། །ཞེས་པ་ནི་ལེའུ་ལ་སོགས་པ་བཞི་པོ་ནི་གཞུང་རྫོགས་པའི་གནས་ཡིན་ཏེ། གང་གི་ཕྱིར་ཡོངས་སུ་གཅོད་ཅིང་གཞལ་བྱ་གང་དུ༌[^1476]རྫོགས་པར་བྱེད་པ་དེ་ནི་ལེའུ་འོ། །

[Block 2207]
གཞན་དུ་ནི༌[^1477]ལེའུ་བཅོ་བརྒྱད་ཀྱི་བདག་ཉིད་ཀྱི་རྒྱུད་ངེས་པར་མི་འགྱུར་ཏེ། མང་ཉུང་གི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2208]
དེ་བཞིན་དུ་ཆོ་ག་ལ་སོགས་པ་ཡང་ཤེས་པར་བྱའོ། །

[Block 2209]
ཇི་སྐད་དུ། ཡོངས་སུ་གཅོད་པས་ལེའུ་སྟེ།

[Block 2210 [VERSE]]
སྟོང་པ་ཉིད་ཀྱི་ཆོ་གར་འགྱུར། །
སྤྲོས་པ་མང་བས་དུམ་བུ་སྟེ། །
སྒྲིབ་པ་མེད་པས་རིམ་པ་ཕྱེ། །
--- END BLOCKS ---
