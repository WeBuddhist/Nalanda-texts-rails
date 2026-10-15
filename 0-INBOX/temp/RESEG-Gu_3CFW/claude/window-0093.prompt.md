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
[Block 3256]
དེས་ན༌[^3217]གནས་བརྟན་དང་བཅས་ཤིང་སོ་སོར་ཐར་པ་དང་བཅས་པའི་དགེ་འདུན་གཞན་ལ་དབུལ་ལོ་ཞེས་བྱ་བ་ནི་རྩོད་པ་སྦེད་པ་དེ༌[^3218]གནས་བརྟན་དང་བཅས་པ་སོ་སོར་ཐར་པ་དང་བཅས་པའི་དགེ་འདུན་ལ་དབུལ་བར་བྱའོ། །

[Block 3257]
སྔར་བྱུང་བ་བརྗོད་དེ་དུས་ཟླ་བ༌[^3219]གསུམ་དུ་དབུལ་ལོ་ཞེས་བྱ་བ་ནི་འདིར་ཁ་ཅིག་ནི་ཟླ་བ་དྲུག་གི་བར་དུ་བརྟན༌[^3220]ནས་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་དུ་སྨོས་པ་ཡིན་ཏེ་མདོ་སྡེ་འཛིན་པ་ལ་སོགས་པ་རྣམས་ལ་ལོ་གཅིག་གི་བར་དུ་བརྟེན༌[^3221]ནས་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3258]
ཤིན་ཏུ་ཡུན་རིང་པོར་འདིར་མང་པོ་རྣམས་ལ་འདི༌[^3222]ཀུན་ནས་ཉོན་མོངས་པར་རིགས༌[^3223]པ་མ་ཡིན་ནོ། །

[Block 3259]
དེ་བས་ན་དེ་ལ་མ་བརྟེན་ནོ། །

[Block 3260]
དེ་ནི་དེའི་འོ་ཞེས་བྱ་བ་ནི་དེ་ནི་རྩོད་པ་སྦེད་པར་བསྐོས་པ་དེའི་ཡིན་པ་སྟེ། དབུལ་བའི་བདག་ཉིད་ཀྱི་ལས་དེ་ནི་དབུལ་བ་ཐམས་ཅད་བསྡུས་པའི༌[^3224]ཕྱིར་མདོ་འདི་བྱས་སོ། །

[Block 3261]
ཕྱིར་ཕུལ་བ་ན་དེས་མདོ་སྡེ་དང་འདུལ་བ་དང་མ་མོ་འཛིན་པ་དག༌[^3225]ལའོ་ཞེས་བྱ་བ་ནི་གནས་བརྟན་དང་བཅས་སོ་སོར་ཐར་པ་དང་བཅས་པའི་དགེ་འདུན་གྱི༌[^3226]རྩོད་པ་དེ་ཉེ་བར་ཞི་བར་བྱེད་མ་ནུས་ཏེ། དེ་ཉིད་ལ་ཕུལ་བ་ན་མདོ་སྡེ་ལ་སོགས་པ་འཛིན་པ་དག་ལ་དབུལ་བར་བྱའོ། །

[Block 3262]
ཟླ་བ་དྲུག་ཏུའོ་ཞེས་བྱ་བ་ནི་སྔར་བྱུང་བ་བརྗོད་དེ་དུས་ཟླ་བ་དྲུག་ཏུ་དབུལ་ལོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3263]
དེ་དག་གིས༌[^3227]གནས་བརྟན་མཐུ་དང་ལྡན་པ་ལའོ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་འཛིན་པ་དང་འདུལ་བ་འཛིན་པ་དང་མ་མོ་འཛིན་པ་དག་གིས་རྩོད་པ༌[^3228]དེ་ཉིད་ཕྱིར་ཕུལ་བ་གང་ཞིག་གནས་བརྟན་གྲགས་པ་བས་ཀྱང་ཆེས་གྲགས་པ་གཙོ་བོ་བས་ཀྱང་ཆེས་གཙོ་བོ་དེ་ལ་དབུལ་བར་བྱའོ། །

[Block 3264]
ཐུག་པ་མེད་པར་རོ་ཞེས་བྱ་བ་ནི་དུས་ཐུག་པ་མེད་པར་དབུལ་ལོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འགྲོ་ས་གནས་མེད་པའི༌[^3229]ཕྱིར་ཕུལ་བ་གང་ཞིག་གནས་བརྟན་གྲགས་པ་བས་ཀྱང་ཆེས་གྲགས་པ་གཙོ་བོ་བས༌[^3230]ཀྱང་ཆེས་གཙོ་བོ་ལ་དབུལ་བར་བྱའོ། །

[Block 3265]
ཐུག་པ་མེད་པར་རོ་ཞེས་བྱ་བ་ནི་དུས་ཐུག་པ་མེད་པར་དབུལ་ལོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། [^3231]འགྲོ་ས་གནས་མེད་པའི་ཕྱིར་འདིར་དུས་དཔག་ཏུ་མེད་པ་ལ་བརྟེན་པར་མཛད་དོ། །

[Block 3266]
གནས་བརྟན་དེས་གདུལ་བར་བྱ་བ་དེ་གཉིས་ལ་ཇི་ལྟར་བསྒྲུབ་པར༌[^3232]བྱ་ཞེ་ན། དེའི་ཕྱིར་དེས་དེ་གཉིས་ལས་བདག་གིར་བྱ་བ་ཐ་ན་འདག༌[^3233]རྫས་དང་སོ་ཤིང་ཡན་ཆད་ཅུང་ཟད་ཀྱང་སྤང་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཡན་ལག་གི་སྒྲ་བྲི་བར་བྱ་བ་སྟེ་ཐ་ན་འདག༌[^3234]རྫས་དང་སོ་ཤིང་ཡན་ཆད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3267]
ལྷན་ཅིག་འགྲོ་བ་དང་འདུག་པ་དང་ལྷན་ཅིག་འཆག༌[^3235]སར་འཆག་པ༌[^3236]དང་གཏམ་འདྲེ་བ་དང་ཕེབས་པར་སྨྲ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་། དེས་དེ་གཉིས་ལས་ལྷན་ཅིག་ཏུ༌[^3237]སྤང་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3268]
རྗེས་སུ་འབྲེང་ན་དེ་དག་ལ་འདི་སྐད་ཅེས་ཚེ་དང་ལྡན་པ་དག་ཁྱེད་ཅག༌[^3238]ལེགས་པར༌[^3239]གསུངས་པའི་ཆོས་འདུལ་བ་ལ་རབ་ཏུ་བྱུང་ནས་འཐབ་པར་གྱུར་མཚང་འདྲུ་བར༌[^3240]གྱུར། རྩོད་པར་གྱུར་འགྱེད་པར་གྱུར་ཅིང་གནས་པ་ནི་མ་རྙེད་དེ་རྙེད་པ་མ་ཡིན་ནོ། །

[Block 3269]
ཉེས་པ༌[^3241]རྙེད་ཀྱི་ལེགས་པ་རྙེད་པ་མ་ཡིན་གྱི། ཚེ་དང་ལྡན་པ་དག་མ་འཐབ་ཅིག་མཚང་མ་འདྲུ་ཤིག །[^3242]མ་འགྱེད་ཅིག་འགྱེད་པ་གཉིས་ཀ་རྒྱལ་བ་མེད་དོ། །

[Block 3270]
རྒྱུག་པ་གཉིས་ཀ་རྒྱལ་བ་མེད་དོ། །

[Block 3271]
གཅིག་རྒྱལ་གཅིག་འཕམ་དུ་འགྱུར་རོ་ཞེས་བརྗོད་པར་བྱའོ་ཞེས༌[^3243]བྱ་བ་ནི་གལ་ཏེ་རྒོལ་བ་དང་ཕྱིར་རྒོལ་བའི་དགེ་སློང་དེ་དག་གནས་བརྟན་དེའི་རྗེས་སུ་འབྲང་བ་ན་དེས་དེ་དག་ལ་དེ་སྐད་ཅེས་བརྗོད་པར་བྱའོ། །

[Block 3272]
ཆེས་མང་བའི་བློས་ལེགས་པར་གཞག་པ་ནི་ལེགས་པ་སྒྲུབ་པའི་རྣམ་པ་གཞན་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཚོགས་པར་བྱུང་བ་དག་གིས་རྒྱུད་གཅིག་ཏུ་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཇི་སྐད་བསྟན་པའི་རྣམ་པ་དེ་དག་ལས་འདི་ལྟ་སྟེ། ཆེས་མང་བའི་བློས་ལེགས་པར་གཞག་པ་ཞེས་བྱ་བ་འདི་ནི་ལེགས་པར་སྒྲུབ་པའི་རྣམ་པ་གཞན་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 3273]
འདི་ནི་ཆོས་ཀྱི་རྣམ་པར་གཏན་ལ་དབབ་པ་ལ་སྲིད་ཀྱི་ཚུལ་ཁྲིམས་རྣམ་པར་གཏན་ལ་དབབ་པ་མི་སྲིད་དོ་ཞེས་བྱ་བ་ལ། འདི་ནི་ཞེས་བྱ་བ་ནི་ཆེས་མང་བའི་བློས་ལེགས་པར་གཞག་པ་འདི་ནི་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3274]
ཆོས་རྣམ་པར་གཏན་ལ་དབབ་པའི་ཞེས་བྱ་བ་ནི་ཅི་འདི་ཆོས་མ་ཡིན་ནམ་འོན་ཏེ་ཡིན་འདུལ་བ་ཡིན་ནམ་འོན་ཏེ་འདུལ་བ་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པས་ཆོས་རྣམ་པར་གཏན་ལ་དབབ་པ་ལ་ཡིན་གྱི་ཚུལ་ཁྲིམས་རྣམ་པར་གཏན་ལ་དབབ་པ་ལ་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེའི་ཕྱིར་དེའི་སྐབས་ཀྱིས་ཤེས་པ་ནི་འགྱེད་པ༌[^3244]གཉིས་དང་འབྲེལ་བ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། [^3245]ཚུལ་ཁྲིམས་རྣམ་པར་གཏན་ལ་དབབ་པ་ཞེས་བྱ་བ་ནི་འདིས་གཞི་བྱས་སམ་འོན་ཏེ་མ་བྱས་ཞེས་བྱ་བ་ལ་སོགས་པས་གཏན་ལ་ཕེབས་པ་ཡིན་པས༌[^3246]དེ་ནི་འགྱེད་པ་གཉིས་ལས་གཞན་པ༌[^3247]དག་གིས་ཤེས་པའི་ཡུལ་མ་ཡིན་པས་དེའི་ཕྱིར་རྟོག་པ༌[^3248]པོ་ཉིད་ཀྱིས་བསྟེན་པར༌[^3249]བྱ་བ་མེད་པར་ཤིན་ཏུ་མང་བ་འདི་དང་གནས་པ་ཞེས་བྱ་བ་བསྟེན་པའི་རྣམ་པ་གཞན་ནི་མེད་དོ། །

[Block 3275]
ཅི་འདི་ལ་དེ་བཞིན་དུ་བརྟེན་པར་བྱ་བའམ་ཞེ་ན། དེའི་ཕྱིར་རྒོལ་བ་དག་གིས་གཅེས་པར་གཟུང་བ་ཉིད་དང་། རབ་ཏུ་དམ་པ་ཉིད་དང་མི་ཟད་པ༌[^3250]ཉིད་ཡིན་ཞིང་དེ་དག་བྱེ་བར༌[^3251]དོགས་པ་ཉིད་ཀྱིས་དེ་ལ་བརྟེན་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་རྒོལ་བ་དང་ཕྱིར་རྒོལ་བ་དག་མངོན་པར་ཞེན་པ་རྣོན་པོས་རྩོད་པ༌[^3252]གཅེས་པར་གཟུང་བ་ཉིད་དང་། མངོན་པར་ཞེན་པ༌[^3253]མི་ཕྱེད་པས༌[^3254]གལ་ཏེ་རྩོད་པ་དེ་ཡལ་བར་བོར་ན་དེ་དག་རྣོན་པོས་ཕྱེ་བ་དོགས་པ་ཉིད་ཤེས་ཀྱང་བསམ་པ་ཁྱད་པར་ཅན་དང་། མངོན་པར་ཞེན་པས་མི་ཟད་པ་ཉིད་དུ་འགྱུར་ཞིང་མདོ་སྡེ་དང་འདུལ་བ་དང་མ་མོ་འཛིན་པ་ཉིད་རྣམ་པར་གནོན་པ་ཉིད་ཀྱིས་སོ། །

[Block 3276]
གལ་ཏེ་རྩོད་པ་དེ་ཡལ་བར་བོར་ན་དེ་དག་བྱེ་བར་དོགས་པ༌[^3255]ཉིད་ཀྱང་ཡོད་ན་དེའི་ཚེ་དགེ་འདུན་བྱེ་བར་གྱུར༌[^3256]ན་མི་རུང་ངོ་སྙམ་པའི་བསམ་པས་ཆེས་མང་བའི་བློས་ལེགས་པར་གཞག་པའི་ཞེས་བྱ་བ་ལེགས་པར་སྒྲུབ་པའི་རྣམ་པ་གཞན་ལ་བརྟེན་པར་བྱ་ཞིང་གཞན་དུ་མི་བྱའོ། །

[Block 3277]
བསྡམ་པར༌[^3257]བྱ་བ་མ་ཡིན་པའི་དོན་ལའོ་ཞེས་བྱ་བ་ནི་འདི་ལ་ལྟུང་བ་ཡིན་ནམ་མ༌[^3258]ཡིན༌[^3259]རྣམ་པར་གཏན་ལ་དབབ་པའི་དོན་ཏོ། །

[Block 3278]
གལ་ཏེ་ལྟུང་བ་ལས་བསྡམ་པར་བྱ་བའི་བདག་ཉིད་མ་ཡིན་གྱི་བཤགས་པར་བྱ་བའི་བདག་ཉིད་ཡིན་ན་དེས་ཀྱང་དོན་དེ་ལ་ཆེས་མང་བའི་བློས་ལེགས་པར་གཞག་པ་ཞེས་བྱ་བའི་ལེགས་པར་སྒྲུབ་པའི་རྣམ་པ་གཞན་ལ་བརྟེན་པར་བྱའི་བསྡམ་པར༌[^3260]བྱ་བའི་དོན་ཡིན་ན་དེ་ལ་ནི་རྣམ་པ་འདི་ལ་བརྟེན་པར་མི་བྱ་སྟེ་ཕྲན་ཚེགས་ཙམ་དུ་ཟད་པའི་ཕྱིར་རོ། །ཅི་དང་པོ་ཉིད་ནས་འདི་ལ་བརྟེན་པར་བྱའམ་ཞེ་ན། དེའི་ཕྱིར་གནས་བརྟེན་གྱི་མཐར་ཐུག་པ་དག༌[^3261]ཡོངས་སུ་ཉོན་མོངས་པར་གྱུར་པ་དག་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་འདུན་གཞི་པོ༌[^3262]དང་གསལ་བ་ལ་སོགས་པའི་རིམ་གྱིས་གནས་བརྟན་གྱི༌[^3263]མཐར་ཐུག་པའི་བར་དག་གིས་ཉོན་མོངས་པ་བརྩལ༌[^3264]ཀྱང་ཉེ་བར་མ་ཞི་བར་གྱུར་པ་ཉིད་ཡིན་ན་འདི་ལ་བརྟེན་པར་བྱའོ། །གང་གིས༌[^3265]འདི་ལ་བརྟེན་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་གཞི་བོས༌[^3266]སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3279]
དོན་འདི་ལ་ཆེས་མང་པོ་དག་ལ་བགྲང་བར་ཇི་ལྟར་བྱ་ཞེ་ན། དེའི་ཕྱིར་འདི་ལ་ཚུལ་ཤིང་བྲིམ་པས༌[^3267]བློ་གཟུང་བར༌[^3268]བྱ་བ་ཉིད་དོ། །

[Block 3280]
ཚུལ་ཤིང་འདྲིམ་པ་བསྐོ་བར་བྱའོ། །

[Block 3281]
དེས་ཚུལ་ཤིང་རྣམ་པ་གཉིས་དག་ཉེ་བར་གཞག་གོ། །

[Block 3282]
ཆོས་ཀྱི་ཚུལ་ཤིང་དག་ནི་ཡ་ཡོ་མེད་པ་དང་ཁྱར་ཁྱོར་མེད་པ་དང་ཆས་ཆུས་མེད་པ་དང་། ཁ་དོག་བཟང་བ་དང་དྲི་ཞིམ་པ་དང་རེག་པ་འཇམ་པ་དག་ཡིན་ལ། །ཅིག་ཤོས་ཀྱི་ནི་དེ་ལས་བཟློག་པའོ། །

[Block 3283]
དགེ་འདུན་ལ་འདུ་བར་གསོལ་ལོ། །

[Block 3284]
ཚུལ་ཤིང་འདྲིམ་པར་འགྱུར་གྱི༌[^3269]ཐམས་ཅད་ཀྱིས་འདུ་བར་བྱའོ། །

[Block 3285]
གལ་ཏེ་འདི་ལྟར་འདུན་པ་སྦྱིན་པས་ཚོགས་པ་དང་ཆོས་མ་ཡིན་པའི་ཚུལ་ཤིང་ལྷག་པར་འགྱུར་བ༌[^3270]སེམས་ན་བྲིམ་པར་མི་བྱའོ། །

[Block 3286]
འདྲིམ་པའི་ཚེ་ན་ལག་པ་གཡས་པས་ཆོས་ཀྱི་ཚུལ་ཤིང་དག་བཟུང་ཞིང་གཡོན་པས་ཅིག་ཤོས་དག་གོ། །

[Block 3287]
དེ་དག་གཡོགས་ཏེ་སྔ་མ་དག་སྣང་བར་བྱས་ནས་བརྗོད་པར་བྱའོ། །

[Block 3288]
གནས་བརྟན་འདི་དག་ནི་ཆོས་ཀྱི་ཚུལ་ཤིང་ཡ་ཡོ་མེད་པ༌[^3271]ཁྱར་ཁྱོར་མེད་པ་ཆས་ཆུས་མེད་པ་ཁ་དོག་བཟང་བ་དྲི་ཞིམ་པ་རེག་ན་འཇམ་པ་དག་ཡིན་གྱི༌[^3272]ལོང་ཤིག་ཅེས་སོ། །

[Block 3289]
ཅིག་ཤོས་ཚོལ་ན་ཚིག་གཉིས་ཀྱི་བར་དུ་མི་དབུལ་ལོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅིག་ཤོས་ཅེས་བྱ་བ་ནི་ཆོས་མ་ཡིན་པའི་ཚུལ་ཤིང་ངོ་། །གཡོགས་སམ་ཕྱེ་བ་གང་གིས་ཆོས་ཀྱི་མང་བར་འགྱུར་བ་དེ་ལྟར་བྲིམ་པར༌[^3273]བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གཡོགས་ཏེ་བྲིམ་ན༌[^3274]ཆོས་ཀྱི་ཚུལ་ཤིང་མང་བ་ལྟ་ན་ཡང་གཡོགས་ཏེ་བྲིམ་པར༌[^3275]བྱའོ། །

[Block 3290]
ཇི་སྟེ་ཕྱེ༌[^3276]སྟེ་བྲིམ་ན༌[^3277]ཆོས་ཀྱི་ཚུལ་ཤིང་མང་བར་འགྱུར་བ༌[^3278]ལྟ་ན་ཡང་ཕྱེ་སྟེ་བྲིམ་པར༌[^3279]བྱའོ། །

[Block 3291]
ཚེ་དང་ལྡན་པ་ཁྱོད་ཀྱི་མཁན་པོ་དང་སློབ་དཔོན་དང་མཁན་པོ་གཅིག་པ་དང་སློབ་དཔོན་གཅིག་པ་དང་གཏམ་འདྲེས་པ་དང་ཕེབས་པར་སྨྲ་བ་དང་སྨོས༌[^3280]འདྲིན་དང་འགྲོགས་པ་ཤེས་ཀྱི༌[^3281]ཆོས་ཀྱི་ཚུལ་ཤིང་བླངས་ཀྱིས་ཁྱོད་ཀྱིས་ཀྱང་ཆོས་ཀྱི་ཚུལ་ཤིང་ལོང་ཤིག །[^3282]ཁྱོད་དེ་དག༌[^3283]ལྷན་ཅིག་རྩོད་པར་གྱུར་ན་མ་ལེགས་སོ་ཞེས་རྣ་དྲུང་དུ་བཤུབ་བོ་ཞེས་བྱ་བ་ནི་བརྡ་སྤྲད་པའི་ཕྱིར་རྣ་དྲུང་དུ་བཤུབ་ཅིང་དེ་སྐད་ཡང་དང་ཡང་དུ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3292]
ཆོས་མ་ཡིན་པའི་ཚུལ་ཤིང་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལེན་ན་འདུལ་བ་དང་འགལ་བའི་ཉེས་བྱས་ཀྱི༌[^3284]ལྟུང་བ་བཤགས་པར་བྱའོ་ཞེས་བྱ་བ་དེའི་འདི་བསྡུས་པའོ། །

[Block 3293]
མདོ་སྡེ་དང་འདུལ་བ་དང་མ་མོ་འཛིན་པ་དག་ལ་མ་དྲིས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཚུལ་ཤིང་བླང་བར་བྱ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདི་ནི་ཐམས་ཅད་ཀྱི༌[^3285]དབང་དུ་བྱེད་པའོ། །

[Block 3294]
མདོ་སྡེ་འཛིན་པ་ལ་སོགས་པ་ལ་དྲི་བ་ནི་ཆོས༌[^3286]ཡོངས་སུ་ཤེས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 3295]
དེ་ལ་རང་གི་མ་ཡིན་པ་ཤིན་ཏུ་རྣམ་པར་གཏན་ལ་དབབ་པ་ཉིད་ལ་སྡེ་སྣོད་འཛིན་པ་རྣམས་ལ་དྲི་བ་འདི༌[^3287]བྱས་པ་ཉིད་དོ། །
--- END BLOCKS ---
