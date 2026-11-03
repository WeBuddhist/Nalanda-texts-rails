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
[Block 3221]
ཇི་ལྟར་ཚིག་གིས་ཇི་ལྟར་བསྟན་པའི་དོན་ཡོངས་སུ་ཐོབ་པས་ལྟུང་བ་དེ་བཞིན་དུ་སྤྲིང་ཡིག་ལ་སོགས་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3222]
འདིར་མཚན་མ་ནི་གང་མཐོང་ནས་སོ་སོར་གོ་བ་སྟེ། དཔེར་ན་སྐྲ་དང་ཁ་སྤུ་བྲེགས་ནས་རིང་པོ་མ་ལོན་པ་འམ་གོས་དམར་སེར་གྱོན་པ་ཉིད་དམ་ཡན་ལག་དང་འབྲེལ་པའི་ཤིང་དཔུང་ཆད་ལྟ་བུའོ། །

[Block 3223]
ཡུལ་ནི་ས་ཕྱོགས་ཏེ་སྐྱེད་མོས་ཚལ་ལ་སོགས་པའོ། །

[Block 3224]
བརྡ་ནི་དངོས་པོ་ཅུང་ཟད་མ་ཡིན་པར་གྱུར་པའི་མཚན་མ་སྟེ། དཔེར་ན་སྔ་དྲོ་འམ་ཉི་མ་ཕྱེད༌[^2213]དམ་ཕྱི་དྲོ་ཞེས་བྱ་བའི་དུས་ཀྱི་རྣམ་པར་གཞག་པའོ། །

[Block 3225]
བརྡ་ནི་བརྡའི་ཡུལ་ཉིད་ཀྱི་ཕྱིར་འདིར་བརྡས་བརྗོད་པའོ། །

[Block 3226]
འདིར་ཐམས་ཅད་དུ་བརྡའི་དབང་གིས་གོ་བར་གྱུར་པ་སྟེ། འདིར་ནི་ཅུང་ཟད་མ་ཡིན་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་བརྡ་ཙམ་གྱི་དབང་ཉིད་ཞེན་པར་བྱས་ནས་བརྗོད་པ་འདི་བྱས་སོ། །

[Block 3227]
འདིར་གཞུང་ནི་རྒྱུ་གསུམ་གྱིས་མངགས་པ་ལ་ཕྲིན༌[^2214]བསྐུར་བར་འགྱུར་གྱི་ཚུར་སྐྱེལ་བ༌[^2215]ནི་མ་ཡིན་ནོ། །

[Block 3228]
གསུམ་གང་ཞེ་ན། ཡུལ་ཕྱོགས་དང་། བརྡ་དང་མཚན་མས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 3229]
སྨད་འཚོང་མ༌[^2216]ནི་མི་མཐུན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དེའི་སྐད་ཅིག་ལ་ཕྲད་པའམ། ལན་བདུན་དུ་ཕྲད་པའི་ཆུང་མ་བརྗོད་པ་སྟེ། ཡུན་ཐུང༌[^2217]ངུ་ཕྲད་པ་ཞེས་བྱ་བ་འདིར༌[^2218]འདིའི་དོན་ཤེས་པ་ཡིན་ནོ། །

[Block 3230]
བཤད་པ་ཡང་དེ་བཞིན་དུ་སྟེ། དེའི་སྐད་ཅིག་ལ་ཕྲད་པ་ནི་ཡུད་ཙམ་ཕྲད་པ་བརྗོད་པ་ཡིན་ནོ། །

[Block 3231]
སྨད་འཚོང་མའི་དེའི་ལུས་ཀྱི་དོན་དུ་ཉེ་བར་གཟུང་བ་ཞེས་བྱ་བ་ནི་འདིའི་རྣམ་པར་གཞག་པར༌[^2219]འགྱུར་རོ། །

[Block 3232]
ཐམས་ཅད་ཀྱིས་ཐམས་ཅད་དུ་ཉེ་བར་གཟུང་བ་ལ་དེའི་སྐད་ཅིག་ཙམ་དུ་ཕྲད་པ་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 3233]
གཞན་གྱིས་ཡོངས་སུ་བཟུང་བ་ལ་ཆུང་མ་ཉིད་མེད་པས་འདི་ནི་ཁ་དུམ་པ༌[^2220]ཡིན་ཏེ། དེ་ལ་སྨད་འཚོང་བ༌[^2221]ཉིད་དུ་ཐོབ་པ་ཡོད་པར་གྱུར་པ་ལ་དུས་ཐམས་ཅད་དུ་ཐམས་ཅད་ཀྱི་ཕྱིར་སྨད་འཚོང་མ་ལ་ཆུང་མ་ཉིད་དུ་ཤེས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་མ་ཕྲད་པ་ཉིད་འདི་ལ་འདིར་ཤེས་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3234]
དེའི་འདི་ནི་བསྡུ་བའོ། །

[Block 3235]
འདི་ནི་ཀུན་དུ་སྦྱར་བར་གྱུར་པ་ཞེས་བྱ་བ་ཤེས་པར་བྱ་བ་ཡང་མ་ཡིན་ཏེ། འདི་ལ་ལུས་འདུད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 3236]
བདག་པོ་ཉིད་མ་ཡིན་པས་བཞི་པ་མན་ཆད་ཞུགས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་བཞི་པ་མན་ཆད་འཇུག་པ་ཉིད་གང་ཡིན་པ་བདག་པོ་ཉིད་མ་ཡིན་པས་བདག་གིས༌[^2222]ཉིད་ཁས་བླངས་པས་ནི་མ་ཡིན་པར་འཇུག་པ་ཉིད་གང་ཡིན་པ་དེ་ཡང་མི་འཐོབ་པ་མེད་པར་གླ་མེད་པར་འདོད་པ་ཙམ་གྱི་དབང་གིས་དོན་དུ་གཉེར་བ་མེད་པར་སྨད་འཚོང་མ་ལ་འཇུག་པ་གང་ཡིན་པ་གཞན་ལ་ཡང་དེ་ནི་ཆོ་ག་འདིའི་ཡུལ་བཞི་པོ་ལ་སྐྱེས་པར་འགྱུར་རོ། །

[Block 3237]
བཞི་པོ་མ་ཡིན་པ་ལ་བདག་ཉིད་དུ་གྱུར་པ་ཉིད་དང་བཅས་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་འདིར་མི་རིགས་པའོ། །

[Block 3238]
འདིར་ཁ་དུམ་པའི་ཚིག་གང་ཡིན་པ་དེ་ལ་ནི་འདི་བསྡུ་བའོ། །

[Block 3239]
གང་ཞིག་ཡང་ཉེ་བ་འཁོར་གྱིས་ཞུས་པ་ལས།

[Block 3240]
དགེ་སློང་གིས་ལན་གྲངས་གཉིས་ལས་ལྷག་པ་ལ་སྤྲིང་བ་མནོས་ཏེ། ཕྲིན༌[^2223]ཕར་སྐྱེལ་ཚུལ་སྐྱེལ་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། དགེ་འདུན་ལྷག་མར་རོ། །

[Block 3241]
དགེ་སློང་གིས་ལན་གྲངས་མང་པོ་ལས་ལྷག་པ་ལ་སྤྲིང་བ་མནོས་ཏེ། ཕྲིན་ཕར་སྐྱེལ་ཚུར་སྐྱེལ་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་བྱ་བ་གསུངས་པ་ཡང་བསྡུས་པ་ཡིན་ནོ། །

[Block 3242]
དེ་ཁྱད་པར་འདི་དང་བཅས་པ་ལ་འདི་བསྡུ་བའོ། །

[Block 3243]
བདག་ཏུ་གྱུར་པ་དང་བཅས་པ་མ་ཡིན་པའི་བསམ་པ་ཁ་དུམ་པ་ཉིད་ཀྱིས་ཞེས་བྱ་བའི་ཚིག་འདིའོ། །

[Block 3244]
དེ་བས་དྲི་བ་བརྗོད་པ་ཤེས་པར་བྱའོ། །

[Block 3245]
འདིར་ལན་གྲངས་ཞེས་བྱ་བ་ལ། ལན་ཞེས་བྱ་བ་ནི་རེས་ལ་བྱའོ། །

[Block 3246]
ལན་གྱིས༌[^2224]དོན་དེའི་ཡང་དང་ཡང་དུ་གོམས་པ་ནི་ལན་གྲངས་ཞེས་བྱའོ། །

[Block 3247]
ལན་གྲངས་གཉིས་ཕྲད་པའི་རེས་གྲུབ་པ་དེ་ནི་ལན་གྲངས་གཉིས་ཞེས་བྱའོ། །

[Block 3248]
གང་ལན་གྲངས་མང་དུ་ཕྲད་པའི་རེས་གྲུབ་པ་དེ་ནི་ལན་གྲངས་མང་ངོ་ཞེས་བྱ་བ་སྟེ་གསུམ་པའོ། །

[Block 3249]
འདིར་གསུམ་པ་ལན་གྲངས་མང་བ་ཉིད་ཀྱིས་སོ། །

[Block 3250]
འདིར་གཉིས་ཀ་དག་ཀྱང་སྤྲིང་བ་མནོས་པ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ༌[^2225]ཞེས་བྱ་བ་ནི་བཞི་པ་མན་ཆད་ཅེས་བྱ་བ་གསུངས་སོ། །

[Block 3251]
འཐབས་པ་ཉིད་ནི་ཉམས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མཐུན་པ་ཉིད་ཅེས་བྱ་བར་སྦྱར་རོ། །

[Block 3252]
འདིར་འཐབས་པའི་སྐད་ཅིག་མ་དང་པོ་ལ་ནི་འདས་པ་ཉིད་དུ་བརྗོད་དེ། དེའི་རྗེས་ལ་འཐབས་པའི་གནས་སྐབས་ལ་ཡང་ཉམས་པ་ཉིད་འདི་གང་ལ་མཛའ་གཅུགས༌[^2226]ཉམས་པའི་དོན་དུ་ནི༌[^2227]ཚིག་འདིའོ། །

[Block 3253]
དེ་བས་ན་འཐབས་པ་མེད་པར་ཡང་ཕྲ་མ་ལ་སོགས་པས་མཛའ་གཅུགས༌[^2228]ཉམས་པར་གྱུར་པ་དེ་ལ་ནི་མཐུན་པ་ཉིད་ཉམས་པ་ཡིན་ནོ། །

[Block 3254]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་ཆུང་མ་ཐ་མ་བཞི་པོ་དེའི་དེ་མ་ཐག་ཏུ་འཐབས་པའི་འོག་ཏུ་སྡུམ་བྱེད་ཅིང་མཐུན་པར་འགྱུར་ཏེ། ཚོགས་པ་རྙེད་ན་དགེ་འདུན་ལྷག་མའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3255]
འདིར་དེའི་འོག་ཏུ་དང༌[^2229]དེ་མ་ཐག་པའི་ཚིག་འདི་མཛའ་གཅུགས༌[^2230]ཉམས་པ་གསལ་བ་ཉིད་ཐོབ་པའི་དོན་དུའོ། །

[Block 3256]
དེ་བས་ན་དེའི་འོག་ཏུ་འཐབས་པ་ཉིད་དང་ཡུན་རིང་པོར་འཐབས་པ་ཉིད་ལ་འདིས་ཉམས་པར་མ་བྱས་པ་ཉིད་ཅེས་བྱ་བ་ཤེས་པར་མི་བྱ་སྟེ་དེའི་ཕྱིར་འདི་ལ་སྨད་པར་བྱའོ། །

[Block 3257]
གལ་ཏེ་དེ་དབང་བ་ཆུང་མ་མ་ཡིན་པར་བསྒྲགས་པ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་གང་དུ་འདི་ལ་ཕྲད་པ་དེ་གལ་ཏེ་དེ་ནི་དེའི་དབང་དུ་འགྱུར་རོ། །

[Block 3258]
ཆུང་མ་མ་ཡིན་པ་ཞེས་བྱ་བ་རྗེས་སུ་བཅུག་པ་ཉིད་ལ་ཉམས་པ་ཉིད་དེ་འཐབས་པ་ཙམ་འགའ་ཞིག་གིས་དེ་ཉམས་པར་མ་ཟད་དོ། །

[Block 3259]
འཐབས་པ་ཉིད་ཀྱི་མོད་ལ་དང་། འོག་ཏུ་དང་དུམ་པ་བཅད་པ་ཉིད་དང་རྡེའུ་གསུམ་གཏོར་བ་ཉིད་དང་ཆོ་ག་བཏང་བ་ཉིད་དང་ཆུང་མ་མ་ཡིན་པར་བསྒྲགས་པ་ཉིད་དང་། དྲིལ་བསྒྲགས་པ་ཉིད་དག་ནི་སྲོག་དང་ལྡན་པ་ཉིད་དག་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སྤྲད་པར་བྱ་བ་སྲོག་དང་ལྡན་པ་ཉིད་ཇི་སྙེད་སྤྲད་པར་འདོད་པ་དེ་རྣམས་ལ་ལྟུང་བ་དེ་སྙེད་པ་དེ་རྣམས་དེ་བཞིན་དུ་བསྐྱེད་པའོ། །

[Block 3260]
དེའི་འོག་ཏུ་འཐབས་པ་ལ་སོགས་པའི་ཆོས་ཇི་ཙམ་པ་འདི་རྣམས་ཡོད་པར་གྱུར་པ་ལ་འཇུག་པ་དེ་སྙེད་རྣམས་ལ་ཞེས་བྱ་བ་འདི་ལ་དེ་སྟོན་པའོ། །
--- END BLOCKS ---
