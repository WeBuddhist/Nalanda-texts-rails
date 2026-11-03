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
[Block 3396]
ནུས་པ་གང་དང་ལྷན་ཅིག་ཏུ་འགྲོ་བ་ལ་དོགས་པ་དང་འགལ་བ་གཉིས་མི་སྲིད་པས་དེ་ལྟ་བུའི་ལམ་གྲོགས་དང་འཕྲད་པ་ལ་མི་འགྲོ་ན་ལྟུང་བར་འགྱུར་རོ། །

[Block 3397]
ཚེས་བཅུ་དྲུག་གི་འོག་རོལ༌[^2221]དུ་ལམ་གྲོགས་ལ་སྡོད་པ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 3398]
གསུམ་པ་ནི་གང་ལ་ཡུལ་འཁོར་དོགས་པ་དང་བཅས་པར་འགྲོ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྗོངས་རྒྱུ་ཞིང་ཞེས་བྱ་བར་སྦྱོར༌[^2222]རོ། །

[Block 3399]
དོགས་པ་དང་བཅས་པ་ཉིད་ནི་ཆོམ་རྐུན་པའི་འཇིགས་པས་འཇིགས་པ་དང་བཅས་པ་ཉིད་དོ། །

[Block 3400]
བཞི་པ་གང་ཡིན་པ་དེ་ནི་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་མི་མཐུན་པ་དང་བཅས་པར་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡུལ་འཁོར་དུ་འགྲོ་བ་ལའོ་ཞེས་བྱ་བའི་ཕྱིར༌[^2223]རྗེས་སྙེག་པའི༌[^2224]ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3401]
ཡུལ་འཁོར་གང་ན་དགྲ་བོ་མི་མཐུན་པ་ཡོད་པ་དེ་ནི་མི་མཐུན་པ་དང་བཅས་པ་ཡིན་ཏེ། ཕྱོགས་འདིར་སུ་ཡང་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་འགྲོ་བ་དགག་པའི་ཁྲིམས་སུ་བྱས་པའི་རྣམ་པར་གཞག་པའི་རྒྱུ་མཚན་ཡིན་གྱི། སྐྱེས་པ་ཉིད་ལ་སོགས་པའི་དོགས་པའི༌[^2225]རྒྱུ་མཚན་དུ་གྱུར་པ་ནི་མ་ཡིན་ནོ། །

[Block 3402]
གང་དུ་འཇིགས་པ་དང་བཅས་པ་ཉིད་དང་། མི་མཐུན་པ་དང་བཅས་པ་གཉིས་པོ་དེ་ལ་ཁ་ན་མ་ཐོ་བ་གཉིས་པོ་འདི་དག་ཀྱང་བསྐྱེད་པའོ། །

[Block 3403]
འཇིགས་པ་དང་བཅས་པའི་གནས་ཐོབ་པ་ནི། དོགས་པ་དང་བཅས་པའི་ལྟུང་བྱེད་བསྐྱེད་པའི་དུས་ཡིན་ནོ། །

[Block 3404]
མི་མཐུན་པ་དང་བཅས་པའི་ལྟུང་བྱེད་ལ་མི་མཐུན་པ་དང་བཅས་པ་ཉེ་བའི་གནས་ཐོབ་པ་བསྐྱེད་པའི་དུས་སོ། །

[Block 3405]
འགྲོ་བ་དང་མི་འགྲོ་བ་ལས་གྱུར་པའི་ལྟུང་བྱེད་བཞི་པའོ།། །།

[Block 3406]
ད་འདི་མན་ཆད་ནི་སྨྲ་བ་ལས་གྱུར་པའི་ལྟུང་བྱེད་གཉིས་སྟོན་ཏེ། དེ་གཉིས་ཀྱི་དང་པོ་ནི་གང་ལ་ལྷའི་གནས་ལ་སོགས་པ་དང་། མུ་སྟེགས་ཅན་གྱི་གནས་སུ་སོང་སྟེ། རྩོད་པར་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང༌[^2226]གི་དོན་གཅིག་རྟོགས་པའི་དུས་ན་ལྟུང་བྱེད༌[^2227]འབྱུང་བའོ། །

[Block 3407]
སྨྲ་བ་གཞན་ལ་རྩོམ་པ་གཅིག་པར་གྱུར་པ་ཉིད་ཀྱིས་དེ་ལ་ཞུགས་པའོ། །

[Block 3408]
འདྲ་བ་གཞན་ལ་རྣམ་པར་ངེས་པར་རྟོགས་པ་ལ་རྩོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 3409]
དེ་ལྟར་རྣམ་པར་འབྱེད་པ་ལས།

[Block 3410]
རྩོད་པ་ནི་འཐབ་ཀྲོལ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3411]
གཉིས་པ་བསྟན་པ་ནི་དེའི་ཕྱིར་སྐབས་མ་ཕྱེ་བར་དྲི་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་གི་ཚིག་གི་སྐབས་མ་ཕྱེ་བར་དྲི་བ་དེ་དྲིས་པ་ལ་ལྟུང་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3412]
འདིར་གླེང་གཞི་ལས་དགེ་སློང་ལ་གསུངས་མོད་ཀྱིས་ལྟུང་བ་རྣམ་པར་གཞག་པ་ལས།

[Block 3413]
སྤྱིར་བསྟན་གྱི་བྱེ་བྲག་འདི་བསྟན་པ་མ་ཡིན་ནོ། །

[Block 3414]
ཁྱིམ་པ་དང་མུ་སྟེགས་པ་དག་ལ་ཤིན་ཏུ་ཉེས་པ་སྟོབས་དང་ལྡན་པ་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་འདི་སྤྱིར༌[^2228]ཐམས་ཅད་ཁྱད་པར་མེད་པར་འཕངས་པའོ། །

[Block 3415]
སྟན་བཏིང་སྟེ་ཕན་ཚུན་ཀུན་དགའ་བར་བྱས་ནས་ལུང་འདྲི་བའི་སྦྱོར་བས་སྐབས་འབྱེད་དུ་གཞུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་འདི་ལ་ལུང་འདྲི་བའི་སྦྱོར་བ་ཡོད་པས་ན་ལུང་འདྲི་བའི་སྦྱོར་བ་དྲི་བར༌[^2229]བྱའོ། །

[Block 3416]
འདིར་གཞུང་ནི་ཆོས་མངོན་པ་དང་འདུལ་བའི་ལུང་ཅི་དག་བཀླགས་ཞལ་སྟོན་ཅིང་མཁྱེན་ཞེས་དྲི༌[^2230]བས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3417]
སྨྲ་བ་ལས་གྱུར་པའི་ལྟུང་བྱེད་གཉིས་སོ།། །།

[Block 3418]
ད་འདི་མན་ཆད་ནི་བཤང་བ་དང་འབྲེལ་པའི་ལྟུང་བྱེད་གསུམ་སྟོན་ཏེ། ཕྱི་སར་གཅིག་པུ་འགྲོ་བ་ལའོ་ཞེས་བྱ་བ་སྨྲས༌[^2231]ཏེ། འདིར་གཅི་བའི༌[^2232]ས་ནི་ཕྱི་སའོ།[^2233] །དབྱར་ཁང་གི་ཉེ་འཁོར་འདོམ་གང་ལས་ལོགས་ཤིག་པ་ནི་ཕྱི་རོལ་གྱི་དངོས་པོའོ། །

[Block 3419]
འདིར་དབྱར་ཁང་གི་ཉེ་འཁོར་ལས་འདའ་བ་ནི་དངོས་གཞིའི་དུས་ཏེ། བུད་མེད་དུ་གྱུར་པ་ལ་གྲོགས་ཉིད་དོ། །

[Block 3420]
ནུས་པ་གང་ཡང་རུང་བ༌[^2234]ལེན་དུ་བཅུག་པ་དགེ་སློང་མའམ་རབ་ཏུ་བྱུང་བ་ཁོ་ན་ལའོ། །

[Block 3421]
གཉིས་པ་བསྟན་པ་ནི་དེའི་ཕྱིར་རྩྭ་སྔོན་པོའི་སྟེང་དུ་བཤང་བ་དོར་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མི་འདོར་བ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 3422]
འདིར་མི་འདོར་བ་ཞེས་བྱ་བ་ནི་བཤང་བ་མེད་པ་ཞེས་ཤེས་པར་བྱའོ། །

[Block 3423]
སྔོན་པོ་ལ་མི་གཙང་བས་ཕོག་པ་ནི་འདིར་དངོས་གཞིའི་དུས་སོ། །

[Block 3424]
ནད་པ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 3425]
རྩྭ་སྔོན་པོ་ཐམས་ཅད་ལ་ཁྱབ་པ་ཉིད་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་རྗེས་སྙེག༌[^2235]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3426]
གང་ལ་གསུམ་པ་དེ་བརྗོད་པར་བྱ་སྟེ་དེའི་ཕྱིར་རྩིག་པའི་ཕག་ཏུ་མ་བལྟས་པར་བཤང་བ་དོར་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉེས་བྱས་སུ་འགྱུར་བའོ། །

[Block 3427]
རྩིག་པ་པུ་ཤུ་བཏགས་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། ར་བའི་ཕྱི་རོལ་དུ་མི་སླེབ་པར༌[^2236]གྱུར་ན། དེའི་ཚེ་ཕག་ཏུ་མ་བལྟས་པར་བཤང་བ་དོར་བ་ལ་ཉེས་པ་མེད་དོ། །

[Block 3428]
དེ་གནས་པ་ལ་འཇུག་པ་མ་ཡིན་ཏེ། བལྟ་བར་ནུས་པ་ཉིད་ལ་འདིར་བསྒྲུབ་པ་རིགས་པ་ཡིན་ཏེ། གལ་ཏེ་བསྒྲུབ་པར་མི་ནུས་པ་ཉིད་ཡིན་ན་ཉེས་པ༌[^2237]མི་རིགས་པ་ཉིད་ཡིན་ནོ། །

[Block 3429]
མི་གཙང་བ་ལ་བོང་རྡོག་འཕང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་གཞུང་ནི་ཕྲན་ཚེགས་དག་ལས་ཚེ་དང་ལྡན་པ་འོད་སྲུངས་ཆེན་པོ་ལྗན་ལྗིན་གྱི་དྲུང་དུ་འགྲོ་བ་དེ་སྦོམ་དགའ་མོས་མཐོང་ནས། དེ་མྱུར་བ་མྱུར་བར་སོང་ནས། ལྗན་ལྗིན་དེའི་སྟེང་དུ་བོང་བ་ཅར་ཅེས་ཟེར་བ་བསྣུན་པས་ཚེ་དང་ལྡན་པ་འོད་སྲུངས་ཆེན་པོའི་ཆོས་གོས་དང་ལྷུང་བཟེད་སྣོད་མི་གཙང་བའི་ཟེག་མས༌[^2238]མ་རུངས་པར་གྱུར་པ་ནས། བཅོམ་ལྡན་འདས་གྱིས་བཀའ་སྩལ་པ། དེ་ལྟ་བས་ན་དགེ་སློང་མས་དགེ་སློང་ལ་མི་གཙང་བས་མ་རུངས་པར་མི་བྱའོ། །

[Block 3430]
བྱེད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3431]
བཤང་བ་ལས་གྱུར་པའི་ལྟུང་བྱེད་གསུམ་མོ། །

[Block 3432]
ལྟུང་བྱེད་འབའ་ཞིག་ཏུ་གྱུར་པ་རྣམས་རྫོགས་སོ།། །།

[Block 3433 [HEADING]]
## དགེ་སློང་མའི་སོ་སོར་བཤགས་པར་བྱ་བ་རྣམས། ^8-0

[Block 3434]
གང་ལ་འོ་མ་སློང་བའི་སོ་སོར་བཤགས་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གཞན་གྱི་ཁྱིམ་ནས་བདག་གི་དོན་དུ་འོ་མ་བླངས་ཏེ་འཐུང་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་གནས་སྐབས་གང་ལ་འཐུང་བ་ལ་ཞེ་ན། དེའི་ཕྱིར་མི་ན་བས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གནས་སྐབས་གང་དང་ལྡན་པས་བླངས་པའི༌[^2239]གནས་སྐབས་དེ་དང་ལྡན་པས་ཞེས་བྱེ་བྲག་མ་སྨོས་པས་རྟོགས་པའོ། །

[Block 3435]
དེས་བསླངས་པའི་ཚེ་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བ་ནི། མི་ན་བ་དེས༌[^2240]བླངས་ཤིང་ཟ་བ་ལ་ལྟུང་བྱེད་ཅེས་བྱ་བ་འདིས་བྱས་པར་རིག་པར་བྱའོ། །
--- END BLOCKS ---
