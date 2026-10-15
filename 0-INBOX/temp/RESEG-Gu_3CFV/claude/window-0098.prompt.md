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

[Block 3436]
གང་ལ་སོ་སོར་བཤགས་པར་བྱ་བ་གཞན་དགུ་པོ་དག་ཏུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཞོ་དང་། [^2241]ཞུན་མར་དང་། འབྲུ་མར་དང་། སྦྲང་རྩི་དང་། བུ་རམ་གྱི་ལྦུ་བ༌[^2242]དང་། ཉ་ཤ་དང་ཤ་སྐམ་རྣམས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཞན་གྱི་ཁྱིམ་ནས་བདག་གི་དོན་དུ་བླངས་ཏེ་འཐུངས་ཟོས་པ་ལའོ་ཞེས་བྱ་བའི་རྗེས་སྙེག་པའི་ཕྱིར་ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3437]
དེ་དག་ལ་གཞན་བསླངས་པ་ལས༌[^2243]གཞན་ཐོབ་པ་ལ་ནི་ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བ་ནི། འདིར་འོ་མ་ལ་སོགས་པ་སྔར་བསྟན་པ་དེ་དག་ལས༌[^2244]གང་ཡང་རུང་བ་གཞན་པ༌[^2245]བསླངས་པ་ལས་གང་ཡང་རུང་བ་གཞན་ཐོབ་ཅིང་ཟོས་པ་ལ་ནི་ཉེས་པ་ན་སྨད་པ་མེད་དོ། །

[Block 3438]
མི་བསོད་པ་ལ༌[^2246]ཡང་ངོ་ཞེས་བྱ་བ་ནི་བསླངས་ཏེ་ཐོབ་པ་ལ་ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འོ་མ་ལ་སོགས་པ༌[^2247]བསོད་པ་སློང་བ་ལ་མི་བསོད་པ་ཐོབ་པ་ལ་ཡང་ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3439]
དེར་རྟོགས་པ་ལ་དེ་ཐོབ་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་ན་སྨད་པ༌[^2248]མེད་དོ་ཞེས་བྱ་བའི་རྗེས་སྙེག་པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3440]
མི་བསོད་པར་བསོད་པ་དེ་བསླངས་པ་ལས་འོ་མ་ལ་སོགས་པ་བསོད་པ་དེ་ཐོབ་ཅིང་ཟོས་སམ་འཐུངས་པ་ལ་ཡང་ཉེས་པ༌[^2249]ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3441]
འདིར་ཐམས་ཅད་དུ་འདིར་བཟའ་བ་ཉེ་བར་མཚོན་པའི་རྙེད་པའི་ཞེས་སྨོས་པར་རིག་པར༌[^2250]བྱའོ། །

[Block 3442]
བསོད་པ་རྒྱུ་མཚན་གྱི་ཐོབ་པ་དང་བསླངས་པ་ལ་བསོད་པ་སློང་བའི་རྒྱུ་མཚན་ལ་མི་བསོད་པ་རྙེད་པ་ལ་ན་སྨད་པར་བརྗོད་དོ། །

[Block 3443]
དེ་ལ་འདིར་ཅི་རང་གིས་གཞན་ལ་བསླངས་པས་ཐོབ་པ་ལ་གཞན་བསླངས་པའི་རྒྱུས༌[^2251]ཐོབ་པ་ལ་ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་རྫོགས་པའོ། །

[Block 3444]
གང་ལ་ན་སྨད་པ་མེད་པའི་ཞེས་སྨོས་པ་དེ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དེ་ནི་ཉེས་བྱས་བྱེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ནི་ཞེས་བྱ་བ་ནི་བསླངས་པའི་རྒྱུས་ཐོབ་པ་ལའོ། །

[Block 3445]
བྱེ་བྲག་མ་སྨོས་པ༌[^2252]སྦྱོར་བ་ལ་དངོས་གཞི་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 3446]
འདིར་ལྷག་མ་ཐམས་ཅད་ནི་བསོད་པ་སློང་བའི་ལྟུང་བྱེད་ཀྱི་སྐབས་སུ་ཤེས་པར་བྱའོ། །

[Block 3447]
སོ་སོར་བཤགས་པར་བྱ་བ་བཅུ་གཅིག་པ་བསྟན་པར་བྱ་བའི་ཕྱིར་སེང་གེ་ལས་གྱུར་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དམག་དཔོན་སེང་གེའི་གླེང་གཞི་ལས་དགེ་སློང་རྣམས་ཀྱིས་སོ་སོར་བཤགས་པར་བྱ་བ་གང་ཡིན་པ་དེ་ནི་དགེ་སློང་མ༌[^2253]རྣམས་ཀྱི་ཡང་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3448]
སོ་སོར་བཤགས་པར་བྱ་བ་རྣམས་རྫོགས་སོ།། །།

[Block 3449 [HEADING]]
## དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ། ^9-0

[Block 3450]
ཤམ་ཐབས་རྐེད་པར་སྣང་བར་བགོ་བར་མི་བྱའོ། །

[Block 3451]
ཆགས་པར་གྱུར་ཅིང་ཁྱིམ་གཞན་དུ་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མི་འདོད་བཞིན་དུ་རྐྱེན་གྱི་དབང་གིས༌[^2254]འགྲོ་དགོས་པ་ལ་སྐད་ཅིག་རེ་རེ་རྩེ་གཅིག་པར་ལྷག་པར་མི་གནས་པ་ལ་ལྟུང་བ་མེད་པར་ཤེས་པར་བྱའོ། །

[Block 3452]
འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བའི་ཚིག་ནི་དཔེ་ཙམ་དུ་ཟད་དེ་སོང་ཟིན་པའི་གནས་སྐབས་ལ་ཡང་ཁ་ན་མ་ཐོ་བར་འགྱུར་རོ། །

[Block 3453]
དེ་ལྟར་ཡང་གླེང་གཞི་ནི་དེ་རྣམས་ལེགས་པར་ཞུགས་པ་ན་དེ་དག་གིས་སྐྱེས་བུ་གཟུགས་བཟང་བ་མཛེས་པ་བལྟ་ན་སྡུག་པ་མཐོང་བ་དང་། དེ་རྣམས་མཐོང་ནས་ཆགས་པར་གྱུར་ཏོ་ཞེས་གསུངས་པ་ཉིད་འདིར་རིག་པར༌[^2255]བྱའོ། །

[Block 3454]
དགེ་སློང་དག་ལས་གྱུར་པ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི། གང་དག་དགེ་སློང་རྣམས་ལ་བརྗོད་པར་བྱས་པ་གཞན་བསླབ་པ་རྣམས་བལྟ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3455]
རྗེས་སུ་མ་གནང་བ་ཉིད་ནི་སྟན༌[^2256]ལ་ཁྱིམ་གྱི་ནང་དུ་འདུག་པ་དང་རྩྭ་སྔོན་པོ་ཡོད་པའི་ས་ཕྱོགས་སུ་བཤང་བ་འདོར་བ་ལ་ལྟུང་བྱེད་ཀྱི་རྣམ་པའོ་ཞེས་བྱ་བའི་ཆོ་ག་འདི་ལ་གནོད་པ་ཉིད་དུ་རིག་པར༌[^2257]བྱའོ། །

[Block 3456]
བསླབ་པ་རྣམས་སོ། །

[Block 3457]
དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་རྫོགས་སོ།། །།

[Block 3458 [HEADING]]
## རྣམ་པར་འབྱེད་པར་གཏོགས་པ་ཕལ་ཆེ་བ་ཕྱིར་བསྟན་པ་རྣམས། ^10-0

[Block 3459]
ཞུ་བར་གཏོགས་པ་ལ་སོ་སོ་བ་དང་ཐུན་མོང་བ༌[^2258]རྣམ་པར་གནས་པ་གཉིས་ལས།

[Block 3460]
སོ་སོ་བ་གང་ཡིན་པ་དེ་འདིར་མ་སྨོས་ཀྱང་ཐམས་ཅད་དུ་རིགས་པ་མཉམ་པ་ཉིད་ཀྱི་ཕྱིར་ཐམས་ཅད་དུ་འགྲོ་བ་ཉིད་ཀྱིས་རྣམ་པར་ཤེས་ནས་ཐམས་ཅད་དུ་རང་གི་ཡུལ་ལ་དབང་དུ་བྱེད་པ་ཉིད་ཀྱིས༌[^2259]ཉེ་བར་འབྲེལ་པའོ། །

[Block 3461]
ད་འདི་མན་ཆད་ནི་ཕལ་ཆེར་རྣམ་པར་འབྱེད་པ་ལ་གཏོགས་པ་ཉིད་ཀྱིས་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་ཉམས་པ་དང་མ་སྐྱེས་པ་གཉིས་ལྟུང་བ་ལ་སྦྱོར་བ་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉམས་པ་ཞེས་བྱ་བ་ནི་ཕམ་པར་གྱུར་པ་སྟེ། འདི་ལ་སྡོམ་པ་ཡོད་དུ་ཟིན་ཀྱང་དེ་ལྟ་མོད་ཀྱི་དགོས་པ་མེད་པ་ཉིད་དུ་འགྱུར་ཏེ། བསྙེན་པར་རྫོགས་པ་ཉིད་དང་། དགེ་ཚུལ་ཉིད་ཀྱི་ལམ་ལ་གནས་པའོ། །

[Block 3462]
མ་སྐྱེས་པ་ཞེས་བྱ་བ་ནི་སྡོམ་པ་མ་ཐོབ་པ་སྟེ། ལྟུང་བའི་གྲངས་དང་མི་སྤྱོད་པ་དང་ལྡན་པ་ལ་ཉེས་བྱས་སོ། །

[Block 3463]
ཉམས་པ་ལ་ནི་དམིགས་ཀྱིས༌[^2260]བསལ་བ་སྟེ། བསྙེན་པར་རྫོགས་པ་ཅན་ཉིད་ཀྱི་ཕྱིར་མ་སྐྱེས་པ་ནི་སྒྲུབ་པ་ཡིན་ཏེ། གང་ལ་འདི་དང་འགྲོ་བ་ལ་བདག་ཉིད་ཀྱིས་ཉེ་བར་བསྟན་པ་དེ་ནི་དེ་དང་རྗེས་སུ་མཐུན་པ་ཡིན་ཏེ། དེ་བས་ན་མ་སྐྱེས་པ་ལ་ཉེས་པ༌[^2261]འདི་འབྱུང་ངོ་། །ཕམ་པར་གྱུར་པ་ལ་ནི་སྡོམ་པ་ཡོད་དུ་ཟིན་ཀྱང་དེ་ལྟ་མོད་ཀྱི། དགོས་པ་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 3464]
འདིར་སྡོམ་པ་མེད་པ་དང་འདྲ་བ་ཉིད་དུ་རྟོགས་པའི་རྒྱུ་ཞེས་བྱ་བར་བརྗོད་དོ། །

[Block 3465]
འདིར་གཞུང་ནི། སྔར་ལྟུང་བ་བྱུང་བ་དང་། རྐུ་ཐབས་སུ་གནས་པ་དང་།

[Block 3466]
དང་པོ་འཁྲུགས་པ༌[^2262]དང་། མ་ནིང་དང་། དགེ་སློང་མ་སུན་ཕྱུང་བས་ཉམས་པར་བྱས་པ་ནི་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3467]
འདིར༌[^2263]རྐུ་ཐབས་སུ་གནས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ནི་མ་སྐྱེས་པ་ཐམས་ཅད་ཀྱི་དཔེ་ཙམ་དུ་ཟད་དོ། །

[Block 3468]
དེ་བས་ན་ཐམས་ཅད་མ་སྐྱེས་པའི་ཁོངས་སུ་བསྡུ་བར་བྱས་སོ། །

[Block 3469]
སྔར་ལྟུང་བ་བྱུང་བ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་སྔར་བསྙེན་པར་རྫོགས་པ་ཉིད་ཀྱི་ཚེ་ན་ལྟུང་བ་བྱུང་བར༌[^2264]རིག་པར་བྱ་བའོ། །

[Block 3470]
བསྙེན་པར་མ་རྫོགས་ཤིང་རབ་ཏུ་བྱུང་བས་བླངས་པ་ལས་འདས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་རྗེས་སུ་སྙེག་པའི༌[^2265]ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །
--- END BLOCKS ---
