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
[Block 3151]
དེས་བསྔགས་པ་ལ་རྗེས་སུ་ཡི་རང་བའི་དོན་གྱི་ཚིག་ནི་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་འདིར་བུད་མེད་གང་ཞིག་འགལ་ཟླ་ཉིད་ཀྱིས་གནས་པ་དེ་དང་ལྷན་ཅིག་དགེ་སློང་དེ་ལ་བསྙེན་བཀུར་བྱས་པ་འདི་ནི་འཕགས་པ་ལ་བསྙེན་བཀུར་བྱས་པ་རྣམས་ཀྱི་མཆོག་སྟེ། གང་གི་ཕྱིར་ཁྱེད་ལྟ་བུའི་དགེ་སློང་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ལ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྔགས་པ་ལ། གང་ཞིག་འདི་ནི་དེ་ལྟར༌[^2152]ཡིན་ནོ་ཞེས་བྱ་བ་རྗེས་སུ་ཡི་རང་བའི་དོན་དུ་བརྗོད་པ་ནི་བསྔགས་པ་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 3152]
འདིར་དངོས་གཞི་ཁོ་ནའི་ཁ་ན་མ་ཐོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3153]
དེ་ཉིད་ཕྱིར་བཟླས་ནའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདི་བསྙེན་བཀུར་བྱས་པ་རྣམས་ཀྱི་མཆོག་ཅེས་བྱ་བ་ལ་སོགས་པ་དེས་བཟླས་ན་དགེ་སློང་གི་ཕྱིར་ཟློ་བར་བྱེད་དེ། དེས་བསྔགས་པ་ཉིད་ནི་ཡོད་པ་མ་ཡིན་ཏེ་དེ་ལས་བཟླས་པར་བྱས་པའོ། །

[Block 3154]
དེ་ལྟ་དེ་ལྟར་ཕྱིས་རྗེས་སུ་སྨྲ་བ་ཞེས་བྱ་བ་གང་གསུངས་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 3155]
དེ་དང་འཁྲིག་པ་དང་ཉེ་བར་མ་སྦྱར་ན་སྦྱོར་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གང་དུ་ཉེ་བར་མ་སྦྱར་བ་ལ་དེས་སྦྱོར་བ་ཉིད་དོ། །

[Block 3156]
དཔེར་ན་འདི་ལྟ་སྟེ། དགེ་སློང་ལ་འཁྲིག་པས་བསྙེན་བཀུར་བྱས་པར་གྱུར་ན་དེ་ནི་བསྙེན་བཀུར་རྣམས་ཀྱི་མཆོག་གོ་ཞེས་ཇི་ལྟར་ཡང་དགེ་སློང་དེས་འཁྲིག་པས་བསྙན་བཀུར༌[^2153]བར་བྱེད་ན་ཞེས་ཟེར་བ་ལྟ་བུའོ། །

[Block 3157]
འཁྲིག་པ་དང་ཉེ་བར་མ་སྦྱར་བ་ཡང༌[^2154]སྦྱོར་བ་ཉིད་དེ། དཔེར་ན་འདི་ལྟ་སྟེ་ཁོ་བོ༌[^2155]ལྟ་བུའི་དགེ་སློང་ལ་བསྙེན་བཀུར་བྱས་པར་གྱུར་པ་དེ་ནི་བསྙེན་བཀུར་རྣམས་ཀྱི་མཆོག་གོ་ཞེས་ཟེར་བ་ལྟ་བུ་སྟེ། དེ་གཉིས་ཀ་ཡང་སྦོམ་པོའི་ལྟུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3158]
གཉིས་ཀ་དང་ནི་དེའི་འོ་ཞེས་བྱ་བ་ནི་འཁྲིག་པའི་ལྟུང་བ་ལ༌[^2156]གཉིས་ཀ་དག་གིས་ཀྱང་ཉེ་བར་མ་སྦྱར་བ་ལ་སྦྱོར་བའི༌[^2157]སྦྱོར་བ་ཉིད་དོ། །

[Block 3159]
དཔེར་ན་འདི་ལྟ་སྟེ། དགེ་སློང་ལ་བསྙེན་བཀུར་བྱས་པར་གྱུར་པ་དེ་ནི་བསྙེན་བཀུར་རྣམས་ཀྱི་མཆོག་གོ་ཞེས་བྱ་བ་ལྟ་བུ་སྟེ། སྦྱོར་བ༌[^2158]ཉིད་ཀྱི་ཕྱིར་ཉེས་བྱས་སོ། །

[Block 3160]
བསྙེན་བཀུར་བསྔགས་པའོ།། །།

[Block 3161]
གང་དུ་སྨྱན་བྱེད་པའི་དགེ་འདུན་ལྷག་མ་བརྗོད་པར་འདོད་ནས་ཕྲད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཉིས་ཀྱིས་གཉིས་ཕྲད་ནའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3162]
འདིར་གཞུང་ནི་ཉེ་བ་འཁོར་གྱིས་ཞུས་པ་ལས།

[Block 3163]
ངེས་པར་མི་སྟེན་པར༌[^2159]བྱེད་པ་རྣམས་ལ་སྨྱན་བྱེད་པ་ལ་སྦོམ་པོའི༌[^2160]ཚིག་གོ། །

[Block 3164]
གང་དེའི༌[^2161]ཕོ་ཉ་དང་འབྲེལ་བ་ལ་བཟུང་བ་དང་བརྐུས་པ་དང་། ཕྱིར་ཞིང་བརྐུས་པ་གསུམ་གྱིས་བསྒྲུབས་པས་དགེ་འདུན་གྱི་ལྷག་མ་ཡིན་པར་གྱུར་ན། འདིར་ཡང་བརྗོད་པར་འགྱུར་ཏེ་ཕྲད་པ་མེད་པས་འདི་སྦོམ་པོ་ཉིད་དུ་གསུངས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་རྣམ་པར་གནས་སོ། །

[Block 3165]
འདུལ་བྱེད་ཀྱི་གཞུང་རྣམས་ལས་ཁྱིམ་བདག་གི་ཆུང་མ་ལ་ཅུང༌[^2162]ཟད་སྨྱན་བྱས་པ་དང་། དེས་དེ་རྐང་ལག་ལ་བཏེག་པར་བྱས་ཏེ།[^2163] ཁྱིམ་ནས་ཕྱིར་ཕྱུང་ནས་དེར་དགེ་སློང་གཞན་ཞིག་རིགས་དང་ཉེ་བར་འགྲོ་བ་དེས་དེ་དག་ཚོགས་པ་བྱས་ཏེ་དེ་དག་ཀྱང་ཕྲད་པར་གྱུར་པ་དང་། དགེ་སློང་དེ་ལ་འགྱོད་པ་སྐྱེས་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 3166]
འཕགས་པ་ཁྱིམ་པ་མིང་འདི་ཞེས་བྱ་བ་ཞིག་ཚུར་ཤོག་ཅེས་སྨྲ་བར་ནུས་སམ། སྨྲས་པ་ནུས་སོ། །

[Block 3167]
གལ་ཏེ་དགེ་འདུན་ལ་གུས་པར་བྱད༌[^2164]ནུས་ན་དེ་ལ་འདི་འབོད་པར་བགྱི་སྟེ། དེས་དེ་ལ་སྤྱད་པའི༌[^2165]རྒྱུ་བྱིན་ནོ། །

[Block 3168]
དགེ་སློང་དེས་གུས་པ་སོ་སོར་སད་པར༌[^2166]བྱ་སྟེ། ཁྱིམ་བདག་དེ་ལ་བོས་སོ། །

[Block 3169]
དེ་དག་ཕྲད་པར་གྱུར་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པ་འདུལ་བྱེད་དག་ལས་ཐམས་ཅད་ཉིད་དུ་ཕྲད་པ་ལ་ལྟུང་བར་བརྗོད་པའོ། །

[Block 3170]
དེ་དག་ཕྲད་པ་ཡོད་པར་གྱུར་ན་སྨྱན་བྱེད་པའི་དགེ་འདུན་ལྷག་མ་ཡིན་གྱི་ཕྲད་པ་མེད་པར་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེས་ཀྱང་ཤེས་པ་ཡིན་ནོ། །

[Block 3171]
གཞན་དུ་ན་ཚིག་འདི་ལ་དོན་དང་ལྡན་པ་ཉིད་སྐྱེ་བ་ནི་མ་ཡིན་ནོ། ། སུ་དང་ཕྲད་ཅེ་ན། དེའི་ཕྱིར་གཞན་དང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བདག་ཉིད་དང་སྨྱན་བྱེད་པ་ལ་ནི་མ་ཡིན་ནོ། །སུར་ཕྲད་ན་ཞེ་ན། དེའི་ཕྱིར་གཞན་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བདག་ཉིད་དུ་ཕྲད་པ་མ་ཡིན་གྱི་གཞན་དུ་ཕྲད་ནའོ། །

[Block 3172]
ཁྱད་པར་ཡོངས་སུ་མ་བཟུང་བས་ན་ཐམས་ཅད་ཀྱིས་སོ། །

[Block 3173]
མིའི་འགྲོ་བ་པ་གཉིས་ཕྲིན༌[^2167]གསུམ་རྣམས་ཀྱིས་བསྟེན་པར་བྱ་བ༌[^2168]རྨའི་སྒོ་རྣམས་དང་ལྡན་པ་ཐམས་ཅད་ལྡན་པ་བསྟེན་པས་མིའི༌[^2169]འགྲོ་བ་ལ་ཞེས་བྱ་བ་རྟོགས་པར་བྱ་སྟེ། བདག་ཉིད་ཡོངས་སུ་བཅད་པའི་དོན་དུ་མདོ་འདིའོ། །

[Block 3174]
དེའི་དོན་དུ་མི་མཐུན་པ་མཐུན་པར་བསྒྲུབ་པའི་ཕྱིར་སྤྲད་པར་བྱ་བ་ལས་སྤྲིང་བ་མནོས་པ་གཞན་དེ་ལ་གོ་བར་བྱས་ཤིང་དེས་སྨྲས་པ་སྔ་མ་ལ་བརྗོད་ནའོ་ཞེས་བྱ་བ་ལ། འདིས་ནི་ལྟུང་བ་རྗེས་སུ་བསྒྲུབས་པས༌[^2170]སྤྲད་པར་བྱ་བ་གཉིས་སུ་སྒྲུབ་པ༌[^2171]ལ་ཞེས་བྱ་བ་ནི་འདིར་ངག་གི་དོན་ཏོ། །

[Block 3175]
[^2172]མི་མཐུན་པ་མཐུན་པར་བསྒྲུབ་པའི་ཕྱིར་ཞེས་བྱ་བ་ལ། མི་མཐུན་པ་དག་ལ་མཐུན་པ་སྒྲུབ་པའི༌[^2173]དོན་དུའོ། །

[Block 3176]
འདིའི༌[^2174]མཐུན་པར་ཞེས་བྱ་བ་ཡང་ཡིད་གཅུགས༌[^2175]པའི་དངོས་པོ་ཉིད་དུ་བྱས་པ་ཡིན་གྱི། གཉིས་ཀྱིས༌[^2176]གཉིས་སྤྲད་པ་ནི་མ་ཡིན་ཏེ། དེ་ཡང་ཇི་ལྟར་ན་བསྒྲུབ་པར་མི་འགྱུར་ཞེས་བྱ་བ་དེའི་དོན་དུ་སྤྲིང་བ་མནོས་པས་ཞེས་བྱ་བ་སྨོས་ཏེ་ཕྲིན༌[^2177]མནོས་པ་ནའོ།[^2178] །སྤྲིང་བ་མནོས་པ་དེ་སུ་ལ་གོ་བར་བྱས་ན་ཞེ་ན། དེའི་ཕྱིར་སྤྲད་པར་བྱ་བ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྤྲད་པ་གང་ལ་བྱ་བ་དེ་ནི་སྤྲད་པར་བྱ་བའོ། །

[Block 3177]
གཞན་དེ་ལ་གོ་བར་བྱས་ཤིང་ཞེས་བྱ་བ་ནི་སྤྲིང་བ་མནོས་པ་དེའོ། །

[Block 3178]
དེ་ལ་ཞེས་བྱ་བ་ནི་སྤྲད་པར་བྱ་བ་ལའོ། །

[Block 3179]
སྤྲད་པར་བྱ་བ་གང་ལ་གོ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གཞན་ལ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་སྤྲིང་བ་མནོས་པ་དེ་ལས་གཞན་པ་དེ་ལའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3180]
དེས་སྨྲས་པ་ཞེས་བྱ་བ་ནི་དེ་གཞན་སྤྲད་པར་བྱ་བ་སྨྲས་པའོ། །

[Block 3181]
གང་ཞིག་འདི་སྤྲིང་བ་མནོས་པ་བརྗོད་པ་ལ་ལན་སྟེར་བ་དེ་ལ་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3182]
སྔ་མ་ལ་ཞེས་བྱ་བ་ནི་སྤྲད་པར་བྱ་བ་ལ་སྟེ་གང་ལས་སྤྲིང་བ་མནོས་པ་དེ་ལའོ། །

[Block 3183]
སྔ་མ་དེ༌[^2179]ལ་གཞན་དེས་སྨྲས་པ་དེ་ཇི་ལྟར་བྱས་ན་ཞེ་ན། དེའི་ཕྱིར་བརྗོད་ན་ཞེས་བྱ་བ་སྨོས་ཏེ། བརྗོད་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3184]
ཕྲད་པའི་དོན་དུ་ཡིད་གཅུགས་པ༌[^2180]བསྒྲུབ་པའི་ཕྱིར་མནོས་ཏེ་ཕྲིན༌[^2181]ཕར་སྐྱེལ་བར་བྱེད་དམ་ཕྲིན་ཚུར་སྐྱེལ་བར་བྱེད་པ་རྣམས་ལ་རྗེས་སུ་བསྒྲུབ་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3185]
འཇུག་པ་བར་མའི་ཕྱང་ཡར་ཐོས་པ་ཉིད་ན་དེ་བྱས་པ་ཉིད་ཅེས༌[^2182]བྱ་བ་ལ། འཇུག་པ་བར་མ་ཞེས་བྱ་བ་ནི་འཇུག་པ་དེ་བར་མར་གཏོགས་པས་འཇུག་པ་བར་མ་སྟེ་ཕྲིན་ལས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3186]
གང་གི་ཚེ་ན་སྤྲད་པར་བྱས་ནས་སྤྲིང་བ་མནོས་པ་དེ་ལ་གོ་བར་བྱས་པར་གྱུར་ན་དེའི་ཚེ་ན་གང་ཞིག་འདི་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་དམ་ངག་གི་རྣམ་པར་རིག་བྱེད་དམ་ཅང་མི་སྨྲ་བར་འཇུག་པ་གང་ཡིན་པས་ལན་སྟེར་བར་བྱེད་ན་བསྐུར་བ༌[^2183]པོ་ལ་མིག་གི་རྣམ་པར་ཤེས་པས་སམ་རྣ་བའི་རྣམ་པར་ཤེས་པས་སམ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་གྲངས་ཇི་ལྟ་བར་བསྐུར་བ་པོའི་ཁས་ལེན་པ་ལ་སྔ་མར་བརྗོད་པ་ལ་ཕྱང་ཡར་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3187]
ཇི་སྲིད་དུ་བསྟན་པར་འགྱུར་ཏེ། དབུས་དང་འབྲེལ་བའི་འཇུག་པ་དེ་གོ་བར་བྱེད་པ་ལ་བརྟེན་པའི་ལོ་རྒྱུས་ལ་དེའི་ཕྲིན་ལན་སྨྲ་བར་གོ་བར་བྱས་པའི་སྤྲིང་བར་བྱ་བས་བསྐུར་བ་པོ་འམ་སྨྲ་བ་པོ་འམ་གཞན་ལས་ཕྲིན་ལན། ཐོས་པ་དང་བྱས་པ་ཉིད་ལ་བསྐུར་བ་ལ་ཕྱང་ཡར་ཉིད་དོ། །

[Block 3188]
སྔ་མ་ལ་བརྗོད་ན་ཅི་ཡང་རུང་བའི་དོན་བསྒྲུབ་པ་ནི་འདིར་ཡན་ལག་གོ། །

[Block 3189]
དེ་ལྟར་འདི་ནི་མ་ཡིན་ཏེ་དེས༌[^2184]ན་བསྐུར་བར་བྱེད་པ་པོས༌[^2185]བསྒྲུབ་པར་འགྱུར་རོ། །

[Block 3190]
གང་གི་ཕྱིར་གལ་ཏེ་དེས་གོ་བར་མི་འགྱུར་ན་འདི་ནི་དེའི་ལན་སྟེར་བར་མི་འགྱུར་རོ། །
--- END BLOCKS ---
