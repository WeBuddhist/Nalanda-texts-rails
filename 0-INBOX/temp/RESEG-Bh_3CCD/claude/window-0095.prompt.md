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
[Block 3326]
མཁས་པ་ནི་དཔེར་ན་བློ་གྲོས་ཆེན་པོ་དེ་མཁས་པ་ཆེན་པོ༌[^2141]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3327]
བརྩོན་པ་ནི་དཔེར་ན་ཆེན་པོར་འགྲོ་བ་སྟེ་བརྩོན་འགྲུས་ཀྱིས༌[^2142]ཀུན་དུ་འགྲོ་བའོ། །

[Block 3328]
སྤྲོ་བ་ནི་དཔེར་ན་ཆེན་པོ་དགེ་བ་སྟེ་དགེ་བའི་ལས་རྣམས་ལ་བརྩོན་པའོ། །

[Block 3329]
རྨད་བྱུང་བྱེད་པ་ནི་དཔེར་ན་བསྟན་བཅོས་ཆེན་པོ་བརྩམ་པ༌[^2143]བཞིན་སྔར་མེད་པ་སྤྲུལ་པ་ལ་མཁས་པའོ། །

[Block 3330]
འདིར་ནི་མཆོག་གི་དོན་གཙོ་བོ་ཡིན་ཏེ། ཐམས་ཅད་ཀྱི་མཆོག་ཏུ་གྱུར་པའི་རྣམ་པ་ཡིན་ཞེས་བྱ་བའི་དོན༌[^2144]ཏོ། །

[Block 3331]
དོན་དམ་པའི་བདེན་པ་ཞེས་པ་ནས་སྔ་མ་བཞིན་ཞེས་བྱ་བའི༌[^2145]བར་དུ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་བསྟན་ཏོ། །

[Block 3332]
ངེས་པའི་དོན་ཞེས་པ་ནི་རིམ་པ༌[^2146]

[Block 3333]
བཞི་པ་དང་ཟུང་དུ་འཇུག་པ་རྗོད་པར་འདོད་པས་སོ། །

[Block 3334]
གཞུང་དེ་ཙམ་གྱིས་ནི་དཔལ་གསང་བ་འདུས་པའི་རྒྱུད་སྟོན༌[^2147]པར་བཞེད་པ༌[^2148]དཔལ་རྡོ་རྗེ་འཆང་ཆེན་པོས་མ་འོངས་པའི་སེམས་ཅན་གྱི་ཁམས་གདུལ་བར་བྱ་བའི་དོན་དུ་གནས་དང་བགེགས་བསྐྲད་པ་དང་སྟོང་པ་ཉིད་བསྒོམ་པ་དང་། ཡེ་ཤེས་ཀྱི་ས་གཞི་དང་གཞལ་ཡས་ཁང་བསྒོམ་པ་དང་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་དང་དོན་དམ་པའི་དཀྱིལ་འཁོར་དང་གདན་གྱི་དབྱེ་བ་དང་ཆོས་ཀྱི་དབྱིངས་ཀྱི་དེ་ཁོ་ན་ཉིད་མངོན་དུ་བྱ་བ་དང་། ས་བོན་ལས་ཕྱག་མཚན་བསྒོམ་པ་དང་། དེ་ཡོངས་སུ་གྱུར་པ་ལས་རྡོ་རྗེ་འཛིན་པ་སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་བསྐྱེད་པ་དང་། མིག་ལ་སོགས་པའི་བྱིན་གྱིས་རློབ་པ་དང་སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་རློབ་པའི་མཚན་ཉིད་དང་པོའི་རྣལ་འབྱོར་གྱི་ཏིང་ངེ་འཛིན་ལས་བསྒྲུབ་པ༌[^2149]རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྣ་ཚོགས་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་བཞུགས་སོ་ཞེས་བསྟན་ཏོ། །

[Block 3335]
དཔལ་གསང་བ་འདུས་པའི་རྒྱུད་གསུངས་པ༌[^2150]དང་དེ་བཞིན་གཤེགས་པ་སྤྲོ་བ༌[^2151]སྔོན་དུ་འགྲོ་བར་སློབ་དཔོན་དང་སློབ་མའི་འབྲེལ་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། དེ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དེའི་དགོངས་པ་ནི་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོ་དེས་མི་བསྐྱོད་པ་ལ་སོགས་པ་དེ་བཞིན་གཤེགས་པ་རྣམས་སྤྲོས་ཏེ། དེ་རྣམས་ཀྱི་ཆེད་དུ་བརྗོད་པ་ཉིད་བསྟན་ཏོ། །

[Block 3336]
ལྷའི་སྐུ་རྣམ་པ་གཉིས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་དཔལ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ལྷའི་རྣལ་འབྱོར་གཉིས་བསྒྲུབ་པར་བྱ་བའི་ཕྱིར་དེ་དང་རྗེས་སུ་མཐུན་པའི་ཏིང་ངེ་འཛིན་རྣམ་པ་གཉིས་བསྟན་པ་གང་ཡིན་པ་དེ་ནི་རྨད་དུ་བྱུང་བ་ཞེས་བསྟན་ཏོ། །

[Block 3337]
དེ་བཞིན་གཤེགས་པ་ཀུན་གྱི་ཞེས་བྱ་བ༌[^2152]ལ་སོགས་པས་དཔལ་གསང་བ་འདུས་པའི་རྒྱུད་དེ་དང་རྗེས་སུ་མཐུན་པར༌[^2153]བསྟན་ཏོ། །

[Block 3338]
དགོངས་པ་མ་ཡིན་པ་ནི་རིམ་པ་གཉིས་གཙོར་གྱུར་པའི་རྒྱུད་ཀྱི་དེ་ཁོ་ན་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3339]
ད་ནི་ཞེས་བྱ་བ་ལ་སོགས་པས་མཆོད་པ་སྔོན་དུ་འགྲོ་བར་གསོལ་བ་གདབ་པར་རིགས་ཏེ། དེ་བས་ན༌[^2154]

[Block 3340]
དང་པོ་ཕྱི་དང་ནང་གི་མཆོད་པའི་བྱེ་བྲག་ཡོངས་སུ་བསྟན་ཏོ།[^2155] །

[Block 3341]
འདུས་པ་མཛད་ནས་ཞེས་པ་ནི་མདུན་དུ་ཐམས་ཅད་གཅིག་ཏུ་བསྡུས་པ་མཛད་ནས་སོ། །

[Block 3342]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་མཆོད་པ་རྒྱས་པ་དེ་ཁོ་ན་ཉིད་དམ་ཚིག་རིན་པོ་ཆེའི་རྒྱ་མཚོའི་ཚོགས་ནི་ཞེས་པ་ལ་ཉེ་བར་སྤྱོད་པ་ལྔ་ལ་སོགས་པ་དང་བདུད་རྩི་ལྔ་དག་ནི་སྤྲིན་དང་འདྲ་བའོ། །

[Block 3343]
དེ་དག་གིས་ཡང་དག་པར་མཆོད་ནས་སོ། །

[Block 3344]
དྲང་བའི་དོན་ནི་ཕྱིའི༌[^2156]མེ་ཏོག་ལ་སོགས་པ་དང་བདུད་རྩིའི་མཆོད་པ་བརྗོད་པར་འདོད་པས་སོ། །

[Block 3345]
གཟུགས་ལ་སོགས་པ་སྟེ་ཞེས་པ་ནི་གཟུགས་རྡོ་རྗེ་མ་ལ་སོགས་པས་སོ།[^2157] །

[Block 3346]
བུད་མེད་རིན་པོ་ཆེ་ཞེས་པ་ནི་མཆོག་ཏུ་བདེ་བ་སྟེར་བར་བྱེད་པས་ན་རིན་པོ་ཆེའོ། །

[Block 3347]
དེ་རྣམས་ཀྱིས་མཆོད་དེ་ཕྱག་བཙལ༌[^2158]ནས་འདི་སྐད་ཅེས་གསོལ་ཏོ་ཞེས་པ་ནི་དེའི་དོན་འདི་ཡིན་ཏེ། རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཐུགས་ཀ་ནས་དེ་བཞིན་གཤེགས་པ་ལྔ་ཕྱུང༌[^2159]སྟེ། ཉེ་བར་སྤྱོད་པ་ལྔ་ལ་སོགས་པའི་ཕྱིའི་མཆོད་པ་དང་། བདུད་རྩི་ལྔའི༌[^2160]མཚན་ཉིད་ནང་གི༌[^2161]གསང་བའི་མཆོད་པ་དང་། གཟུགས་རྡོ་རྗེ་མ་ལ་སོགས་པའི་སྙོམས་པར་ཞུགས་པའི་གསང་བའི་མཆོད་པས། དེ་ཉིད་ལ་མཆོད་ཅིང༌[^2162]འདི་སྐད་ཅེས་གསོལ་ཏོ། །

[Block 3348]
ངེས་པའི་དོན་ནི་སྙོམས་པར་ཞུགས་པའི་མཆོད་པར་བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3349]
དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་གསོལ་བ་གདབ་པའོ། །

[Block 3350]
གཉིས་གཅིག་ཏུ་གྱུར་པ་ནི་སྟོང་པ་ཉིད་དང་སྙིང་རྗེའི་བདག་ཉིད་ཅེས་པའི་ཐ་ཚིག་གོ། །

[Block 3351]
ཡི་གེའི་དོན་ནི་དེ་ཉིད་ཙམ་སོ་སོར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3352]
རྡོ་རྗེ་དང་པདྨ་ཡང་དག་པར་སྦྱོར་བ་ནི་ཞེས་པ་ལ་གསང་བའི་རྡོ་རྗེ་དང༌[^2163]ཆུ་སྐྱེས་སྦྱངས་པ་ལས་ཁམས་གསུམ་གྱི་བདག་ཉིད་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3353]
སྤྱིའི་དོན་ནི་བསྐྱེད་པའི་རིམ་པ་བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །ཤེས་རབ་དང་། ཐབས་ཡང་དག་པར་སྦྱོར་བ་ནི་ཞེས་པ་ལ། ཤེས་རབ་ནི་འཇུག་པའི་རྣམ་པར་ཤེས་པ་འགོག་པར་བྱེད་པའི་མཚན་ཉིད་དེ་སྣང་བའི་ཡེ་ཤེས་སོ། །

[Block 3354]
ཐབས་ནི་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་འགོག་པར་བྱེད་པའི་མཚན་ཉིད་ཅན་སྣང་བ་མཆོད་པའི༌[^2164]ཡེ་ཤེས་སོ། །

[Block 3355]
ཡང་དག་པར་སྦྱོར་བ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་འགོག་པའི་མཚན་ཉིད་ཅན་སྣང་བ་ཐོབ་པའི་ཡེ་ཤེས་སོ། །

[Block 3356]
དོན་དེ་ལྟ་བུ་སྟོན་པར་བྱེད་པའི་ཕྱིར་ན་འདུས་པའོ། །

[Block 3357]
སྦས་པ་ནི་ཡེ་ཤེས་གསུམ༌[^2165]རྣམ་པར་དག་པའི༌[^2166]མཚན་ཉིད་གཙོར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3358]
ཡང་ན་ཤེས་རབ་ནི་ཡི་གེ་ཨཱཿའོ། །

[Block 3359]
ཐབས་ནི་ཧཱུྃ་ངོ་། །ཡང་དག་པར་སྦྱོར་བ་ནི་མ་ནིང་གི་ངོ་བོ་ཉིད་ཡི་གེ་ཨོཾ་མོ། །

[Block 3360]
དེ་རྣམས་ཀྱི་འཇུག་པ་ལ་སོགས་པའི་རིམ་པ་ལ་བརྟེན༌[^2167]ཏེ། དམ་ཚིག་གམ་ཡེ་ཤེས་ཀྱི་ཕྱག་རྒྱ་དང་། འབྲེལ་པས་ཡན་ལག་མ་ཉམས་པའི་མཚན་ཉིད་ཅན་བཟླས་པ་ནི་འདུས་པའོ་ཞེས༌[^2168]འདོད་ཆགས་ཀྱིས༌[^2169]ཆོས་བཤད་པའི་སྒོ་ནས་རྡོ་རྗེ༌[^2170]བཟླས་པ་བཤད་པའོ། །

[Block 3361]
ཡང་ན་ཤེས་རབ་ནི་ཟླ་བ་དང་འདྲ་བའི་སྣང་བའོ། །

[Block 3362]
ཐབས་ནི་ཉི་མ་དང་འདྲ་བའི་སྣང་བ་མཆེད་པའོ། །

[Block 3363]
[^2171]ཡང་དག་པར་སྦྱོར་བ་ནི་མཚམས་ཀྱི་སྣང་བ་དང་འདྲ་བ་ཐོབ་པའོ།[^2172] །

[Block 3364]
དེ་ཡོངས་སུ་གྱུར་པ་ལས་ཡང་དག་པར་སྐྱེས་པའི་སྒྱུ་མ་ལྟ་བུའི་ཡེ་ཤེས་ཀྱི་སྐུ་སྟེ། འདུས་པའོ་ཞེས་ཀུན་རྫོབ་ཀྱི་བདེན་པ་རྟོགས་པའི༌[^2173]མཚན་ཉིད་ཅན་བདག་བྱིན་གྱིས་རློབ་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 3365]
ཀུན་རྫོབ་དང་དོན་དམ་པའི་བདེན་པ་དག་ཏུ་འདུས་པ་ནི་ཞེས་པ་ལ་ཉེ་བར་མཚོན་པ་འདི་ཡིན་པས་ཡོད་པ་དང་མེད་པ་དང་། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དང་། རྣམ་པ་དང་། རྣམ་པ་མེད་པ་དང་། རྟག་པ་དང་། ཆད་པ་དང་། གཅིག་པུ་དང་། དུ་མ་དང་། ཐབས་དང་ཤེས་རབ་ལ་སོགས་པ་གཉིས༌[^2174]པོ་གཅིག་ཏུ་འདུས་པའི་རང་བཞིན་ནོ། །
--- END BLOCKS ---
