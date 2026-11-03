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
དགེ་ཚུལ་མས་ཀྱང་དགེ་ཚུལ་མ་ལ་ཕྱག་བྱའོ་ཞེས༌[^3492]གསུངས་པ་དེ་བས་ན་དེ་ལ་དེ༌[^3493]བྱེད་པའོ། །

[Block 3432]
མདོ་སྔ་མས་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པས་མཆོག་ལ་རབ་ཏུ་བྱུང་བས༌[^3494]ཕྱག་བྱའོ་ཞེས་བསྟན་པ་ལ་དགེ་ཚུལ་ཕས་དགེ་སློབ་མ་དང་དགེ་སློང་མ་ལ་ཕྱག༌[^3495]བྱ་བར་ཐལ་བར་འགྱུར་བ་དང་། མདོ་འདིས་ནི་མཉམ་ན་རྒན་པ་ལའོ་ཞེས་བྱ་སྟན༌[^3496]པས་དགེ་སློང་དང་དགེ་སློང་མ་ཡང་སོ་སོར་ཐར་པའི་སྡོམ་པས་མཉམ་པ་ཡིན་པས། དགེ་སློང་མ་ལ་དགེ་སློང་གིས་ཕྱག་བྱ་བར་ཐལ་བར་འགྱུར་བ་དང་། དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་ཡང་སོ་སོར་ཐར་པའི་སྡོམ་པས་མཉམ་པ་ཡིན་པས་དགེ་ཚུལ་མ་རྒན་པ་ལ་དགེ་ཚུལ་གྱིས་ཕྱག་བྱ་བར༌[^3497]ཐལ་བར་འགྱུར་བས༌[^3498]དེ་བསལ་བའི་ཕྱིར་མདོ་དེ་གཉིས་ཀྱི་བྱེ་བྲག་བསྟན་པར་བྱ་སྟེ། དེའི་ཕྱིར། མཚན་ཐ་མི་དད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཚན་མཐུན་པ་དག་ལ་ཆོ་ག་འདི་ཡིན་གྱི་མཚན་མི་མཐུན་པ་དག་གི་ནི་མ་ཡིན་ནོ། །

[Block 3433]
ཇི་ལྟར་སྐྱེས་པས་བུད་མེད་ལ་ཕྱག་མི་བྱ་བ་དེ་བཞིན་དུ་བུད་མེད་ཀྱིས་ཀྱང་སྐྱེས་པ་ལ་ཕྱག་མི་བྱ་བར་ཐར་བར་འགྱུར་བ་དེ་དམིགས་ཀྱིས་བསལ་བའི་ཕྱིར། སྐྱེས་པ་མི་དམན་པ་ལ་བུད་མེད་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་སོ་སོར་ཐར་པའི་སྡོམ་པས་བུད་མེད་པས་མི་དམན་ན་གསར་བུ་ལ་ཡང་བུད་མེད་ཀྱིས་ཕྱག་བྱ་ན་དུས་མཉམ་པའམ་རྒན་པ་ལ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3434]
ཆོ་ག་དེ་དག་ཐམས་ཅད་ཀྱི་དམིགས་ཀྱིས་བསལ་བའི༌[^3499]ཕྱིར། ས་གཞན་ན་གནས་པ་དང་ཉམས་པ་དང་དགེ་སློང་མ༌[^3500]སུན་ཕྱུང་བ་དང་། ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པ་དང་། ཐ་དད་པར་གནས་པ་དང་། མཚམས་མེད་པ༌[^3501]བྱས་པ་དང་། ཉལ་བ་དང་སྙོམས་པར་ཞུགས་པ་དང་བྲེལ་བ༌[^3502]དང་སེམས་གཞན་དུ་སོང་བ་དང་རྒྱབ་ཀྱིས༌[^3503]ཕྱོགས་པ་དང་ཁྱིམ་གཞན་ན་འདུག་པ་དང་ཟས་ཀྱི་གྲལ༌[^3504]ན་འདུག་པ་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ས་གཞན་ན་གནས་པ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པ་ལ་སོགས་པ་བསླབ་པ་བྱིན་པ་དང་། དེའི་ངོ་བོ་ཉིད་ཚོལ་བ་དང་མཐུན་པ་སྦྱིན་པ་ལ་སོགས་པའོ། །

[Block 3435]
ཉམས་པ་ཞེས་བྱ་བ་ནི་གནས་པར་མི་བྱ་བའོ། །

[Block 3436]
དགེ་སློང་མ་སུན་ཕྱུང་བ་དང་མཚམས་མེད་པ་བྱས་པ་ཞེས་བྱ་བ༌[^3505]ནི། མུ་སྟེགས་ཅན་ཞུགས་པ་དང་། རྐུ་ཐབས་སུ་གནས་པ་དང་། ཟ་མ་དང་། མ་ནིང་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྡོམ་པའི་ཞིང་མ་ཡིན་པར་གྱུར་པ་དག་བསྡུས་སོ། །

[Block 3437]
ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པ་ཞེས་བྱ་བ་སྨོས་པས་ནི་ཐ་དད་པས་གནས་པའི༌[^3506]བྱེ་བྲག་གོ། །

[Block 3438]
ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པའི་ཐ་དད་པ༌[^3507]གནས་པ་གང་ཡིན་པ་ཞེས་བྱ་བ་དེས་ནི་ཆོས་ཀྱི་ཕྱོགས་དང་མཐུན་པ་གནས་པའི་ཐ་དད་པ་ལ་ཕྱག་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 3439]
ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པ་ཞེས་སྨོས་པས་ནི་རང་གི་ཕྱོགས་ཀྱིས་ཀྱང་ཕྱག་མི་བྱ་བར་ཐལ་བར་འགྱུར་བ༌[^3508]ཞེས་བྱ་བས་འདིར་ཐ་དད་པར་གནས་པར་བསྡུས་སོ། །

[Block 3440]
ཉལ་བ་ཞེས་བྱ་བ་ནི་གློས་ཕབ་སྟེ་ཉལ་བའོ། །

[Block 3441]
སྙོམས་པར་ཞུགས་པ་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་ལའོ། །

[Block 3442]
བྲེལ་བ་ཞེས་བྱ་བ་ནི་བྱ་བ་རྗེས་སུ་བསྒྲུབ་པ་ལ་སེམས་གཞོལ་བའོ། །

[Block 3443]
སེམས་གཞན་དུ་སོང་ཞེས་བྱ་བ་ནི་ཕྱག་འཚལ་བ་ལ་སེམས་གཏོད་པ་མི་སྦྱིན་པའོ། །

[Block 3444]
རྒྱབ་ཀྱིས་ཕྱོགས་པ་ཞེས་བྱ་བ་ནི་མདུན་ཕར་པ་ལྟས་པའོ། །

[Block 3445]
ཁྱིམ་གཞན་ན་འདུག་པ་ཞེས་བྱ་བའི་སྒྲ་ལས་ཁྱིམ་གྱི་ནང་ན༌[^3509]འདུག་པ་ཞེས་བྱ་བ་དང་སྦྱར་ཏེ་ཁྱིམ་པའི་ཁྱིམ་ན་འདུག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3446]
ཁྱིམ་པས་རབ་ཏུ་བྱུང་བ་ལའོ་ཞེས་བྱ་བ་ནི་མ་གཏོགས་པའི་ཇི་སྐད་བསྟན་པ་དེ་དག་ལས་གཞན་པ༌[^3510]ཐམས་ཅད་ལ་ཕྱག་བྱའོ།[^3511] །ཁྱིམ་གཞན་ན་འདུག་པ་ལ་ཡང་མ་གཏོགས་པར་མི་རིགས་ཏེ། ཁྱིམ་གཞན་ནི་ཁྱིམ་པ་རྣམས་ཀྱི་སྤྱོད་ཡུལ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3447]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི་ཁྱིམ་བདག་གི་ཆུང་མ་བདེ་ཆེན་མ་དད་པ༌[^3512]སྐྱེས་པ་གནས་ནས་ཕྱིར་བྱུང་སྟེ། བཅོམ་ལྡན་འདས་ཀྱི་ཞབས་ལ་ཕྱག་བྱས་སོ་ཞེས་གྲགས་པ་ཡིན་ནོ། །

[Block 3448]
ཆུས་བཏབ་པས་སྲོག་ཕྱིར་བཟློག་པའི་ཕྱིར༌[^3513]ཚེ་དང་ལྡན་པ་ལམ༌[^3514]ཕྲན་གྱི་ཞབས་ལ་ཕྱག་བྱས་ནས་བཟོད་པ་གསོལ་བ་ཞེས་ཐོས་པ་ཡིན་ནོ། །

[Block 3449]
མ་གཏོགས་པ་གཞན་ཐམས་ཅད་ལ་ནི་ཁྱིམ་པས་ཀྱང་ཕྱག་མི་བྱ་བར་རིགས་ཏེ། འདི་ལྟར་ཡོངས་སུ་གནས་པ་ལ་སོགས་པ་དག་ལ་ཡང་དེ་དང་མི་འབྱུང་བ་ཉིད་ལ་སོགས་པ་སྨོས་ཏེ། ཁྱིམ་པ་དག་གིས་ཀྱང་ཕྱག་བྱ་བར་མི་རིགས་ཏེ། ནན་ཏུར་བྱས་པ་དག་ཀྱང་སྤངས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3450]
དེ་ལ་ཁྱིམ་པའི་སྙོམས་པར་ཞུགས་པ་སྤང་བ་ནི་འདི་ཡིན་ཏེ། གང་ཞིག་ལྷ་ལ་མཆོད་པའི་རྣམ་པ་ནི་མ་ཡིན་པ་ནི་འདི་ལྟ་སྟེ། མེའི་ཁང་པ་ལ་སོགས་པར་སྙོམས་པར་ཞུགས་པ་ཁ་ཅིག་རྣམས་ལ་ནི་ཁ་ཅིག་ཏུ་ལྷ་རྣམས་ཀྱིས༌[^3515]ཕྱག་འཚལ་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 3451]
འདིར་དེ་དག་གི་གཞུང་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་ཚེ་དང་ལྡན་པ་ཉེ་བ༌[^3516]འཁོར་གྱིས་ཞུས་པ། བཙུན་པ་ཕྱག་མི་བྱ་བ་དུ་མཆིས་ཉེ་བ༌[^3517]འཁོར་སུམ་ཅུ་རྩ་གཉིས་ཏེ། བསྡིགས་པའི་ལས་བྱས་པ་དང་། སྨད་པའི་ལས་བྱས་པ་དང་། བསྐྲད་པའི་ལས་བྱས་པ་དང་། ཕྱིར་འགྱེད་པའི་ལས་བྱས་པ་དང་། མ་མཐོང་བས་གནས་ནས་ཕྱུང་བ་དང་། ཕྱིར་མ༌[^3518]འཆོས་པས་གནས་ནས༌[^3519]ཕྱུང་བ་དང་། སྡིག་པ་ཅན་གྱི་ལྟ་བའི་རྣམ་པ་མི་གཏོང་བས་གནས་ནས་ཕྱུང་བ་དང་། ཡོངས་སུ་གནས་པར༌[^3520]བྱེད་པ་དང་། [^3521]མགུ་བ་སྤྱོད་པ་དང་གཞི་ནས་མགུ་བ་སྤྱོད་པ་དང་། བསླབ་པ་བྱིན་པ་དང་། ཟ་མ་དང་མ་ནིང་དང་དགེ་སློང་མ་སུན་ཕྱུང་བ་དང་། རྐུ་ཐབས་སུ་གནས་པ་དང༌[^3522]གནས་པར་མི་བྱ་བ་དང་། མ་བསད་པ་དང་། ཕ་བསད་པ༌[^3523]དང་། དགྲ་བཅོམ་པ་བསད་པ༌[^3524]དང་། དགེ་འདུན་གྱི་དབྱེན་བྱས་པ་དང་དེ་བཞིན་གཤེགས་པ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་ཕྱུང་བ་དང་། གཅེར་བུ༌[^3525]དང་ཆོས་གོས་གཅིག་པ་དང་ཉལ་བ་དང་། སྙོམས་པར་ཞུགས་པ་དང་། རྒྱབ་ཀྱིས་ཕྱོགས་པ་དང་། སོ་ཤིང་ཟ་བ་དང་། བཤང་བ་བྱེད་པ་དང་། གཅི་བ་བྱེད་པ་དང་། ཁྱིམ་གཞན་ན་འདུག་པའོ། །

[Block 3452]
བཙུན་པ་ཕྱག་བགྱི་བ་དུ་མཆིས། ཉེ་བ༌[^3526]འཁོར་ལྔ་སྟེ། ཁྱིམ་པས་རབ་ཏུ་བྱུང་བ་ལ་དང་། བསྙེན་པར་མ་རྫོགས་པས་བསྙེན་པར་རྫོགས་པ་ལ་དང་། གཞོན་པས་རྒན་པ་ལ་དང་། དགེ་སློང་མ་བསྙེན་པར་རྫོགས་ནས་ལོ་བརྒྱ་ལོན་པས་དེ་རིང་བསྙེན་པར་རྫོགས་པའི་དགེ་སློང་ལ་དང་། དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ལ༌[^3527]ལྷ་དང་བཅས་པའི་འཇིག་རྟེན་གྱིས་ཕྱག་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3453]
འདིར་ཁ་ཅིག་ཏུ་བྲེལ་བ་དང་སེམས་གཞན་དུ་སོང་བ་དང་ཟས་ཀྱི་གྲལ༌[^3528]ན་འདུག་པ་དག་ནི་གཞུང་གཞན་ནས་བསྡུས་སོ། །

[Block 3454]
ཐམས་ཅད་ཀྱིས་སངས་རྒྱས་ལའོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་ཡང་རུང་རབ་ཏུ་བྱུང་བ་ཡང་རུང་བུད་མེད་ཀྱང་རུང་སྐྱེས་པ་ཡང་རུང་རྒན་པ་ཡང་རུང་གཞོན་པ་ཡང་རུང་བ་ཐམས་ཅད་ཀྱིས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་ཕྱག་བྱའོ། །

[Block 3455]
གཙུག་ལག་ཁང་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གིས༌[^3529]གཙུག་ལག་ཁང་བྱ་བ་ལ་མི་རུང་བ་མེད་པའོ། །

[Block 3456]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི་འདི་ལྟ་སྟེ། དགེ་སློང་ཀུན་དགའ་ར་བ་དེ་ཉིད་དུ་ཕྱོགས་བཞིའི་དགེ་སློང་གི་དགེ་འདུན་གྱི་ཕྱིར་གཙུག་ལག་ཁང་ཁ་སྲོ་བར༌[^3530]བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3457]
ངོས་གཅིག་གི་དབུས་སུ་དྲི་གཙང་ཁང་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། འདིར་ངོས་ཞེས་བྱ་བ་ནི་ཕྱོགས་ཏེ། ཤར་ལ་སོགས་པའི་ཕྱོགས་གཅིག་གི་དབུས་སུ་དྲི་གཙང་ཁང་བྱ་བ་ཉིད་ཡིན་པའོ། །

[Block 3458]
དེའི་མདུན་དུ༌[^3531]སྒོ་ཁང་ངོ་ཞེས་བྱ་བ་ནི་དྲི་གཙང་ཁང་དེའི་མདུན་གྱི་བྱང་གཏད་ཀྱི་ངོས་སུ་སྒོ་ཁང་བརྩིག་པར་བྱའོ། །

[Block 3459]
[^3532]གཙུག་ལག་ཁང་གི་དབྱིབས་ནི་གྲུ་བཞི་བཟང་བ་ཉིད་དེ་རྣམ་པ་གཞན་ཡང་བཀག་པ་ནི་མེད་པར་ཤེས་པར་བྱའོ། །

[Block 3460]
ཁྱམས་གསུམ་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གྲུ་བཞི་པ་བཟང་ངོ་ཞེས་བྱ་བ་རྗེས་སུ་སྦྱར་ཏེ།

[Block 3461 [VERSE]]
གྲུ་བཞི་ལ་ངོས་གསུམ་ལས་ཁྱམས་བཏགས་པ་བཟང་ངོ་། །
འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ།
ཁྱིམ་བདག་རྗེས་སུ་གནང་གིས་བྱེད་དུ་ཆུག་ཅིག །

[Block 3462]
དེ་ཇི་ལྟ་བུར༌[^3533]བྱེད་དུ་གཞུག་པ་མི་ཤེས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གལ་ཏེ་གནས་ཁང་གསུམ་པ་བྱེད་དུ་འཇུག་ན། དབུས་སུ་དྲི་གཙང་ཁང་བྱེད་དུ་གཞུག་ཅིང་གཉིས་སུ་གནས་ཁང་གཉིས་སོ། །

[Block 3463]
ཁྱམས༌[^3534]གསུམ་ལ་ནི་དེ་བཞིན་དུ་གནས་ཁང་དགུ་དག་གོ། །

[Block 3464]
ཁྱམས་བཞི་ལ་ནི་དབུས་སུ་སྒོ་ཁང་གི་བྱང་གཏད་དུ་དྲི་གཙང་ཁང་ངོ་། །སྒོ་ཁང་གི་ངོས་གཉིས་སུ་གནས་ཁང་གཉིས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3465]
མནོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདིས་ནི་དོན་གྱིས་དེའི་ས་གཞི་ཉེན་ཀོར་དང་བཅས་པ་མནོད༌[^3535]པར་རིགས་པར་བྱའོ། །

[Block 3466]
གཙུག་ལག་ཁང་དུ་གནས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བྱའོ་ཞེས་བྱ་བ་དང་མནོད་པར༌[^3536]བྱའོ་ཞེས་བྱ་བ༌[^3537]དེ་གཉིས་ཀྱིས་གནས་པར་བྱ་བ་མ་བསྡུས་ཏེ། དེ་གཉིས་ཀྱིས་གཞན་གྱི་དོན་དུ་བྱ་བ་དང་། མནོད་པར་བྱ་བ་ཡང་སྲིད་པས་རྩོམ་པ་འདིའོ། །

[Block 3467]
གཞན་དག་དགེ་འདུན་གྱི་གཞིར༌[^3538]དགེ་འདུན་གྱི་ཕྱིར་རམ་གང་ཟག་དགེ་སློང་གི་ཕྱིར་གནས་ཀྱི་གཞི་བྱེད་པ་རྗེས་སུ་གནང་བར་བྱའོ། །

[Block 3468]
གལ་ཏེ་སྦྱིན་བདག་ཡོད་ན་དེས་རྗེས་སུ་གནང་བ་ནའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དགེ་འདུན་གྱི་གཞི་དེ་ལ་སྦྱིན་བདག་ཡོད་ན་དེས་རྗེས་སུ་གནང་ན་དགེ་འདུན་གྱི་ཕྱིར་རམ་གང་ཟག་གི་ཕྱིར། གནས་ཀྱི་གཞི་བྱེད་པ་རྗེས་སུ་གནང་བར་བྱའོ། །

[Block 3469]
གྲོང་ཁྱེར་གྱི་ཕྱི་རོལ་ལམ་ནང་དུ་བསྟི་བའི་གནས་དག་རུང་ངོ་ཞེས་བྱ་བ་ནི་གང་དུ་དགེ་སློང་དག་བསོད་སྙོམས་པའི་དོན་དུ་འཇུག་པ་རྣམས་ཀྱི་ཚ་བ་དང་། ངལ་བ་རྣམས་ལ་སོགས་པ་བསལ་བའི་ཕྱིར་བསྟི་བའི་གནས་མི་འོང་བའི་གནས་ཞེས་བྱ་བ་དེ་བྱེད་དུ་གཞུག་པར་རུང་ངོ་། །འདིར་གཞུང་ནི་གལ་ཏེ་བཅོམ་ལྡན་འདས་ཀྱིས་རྗེས་སུ་གནང་ན་བདག་གྲོང་ཁྱེར་གྱི་སླད་རོལ་དུ་བསྟི་བའི་གནས་བགྱིད་དུ་སྩལ་ཏེ་ཞེས་བྱ་བ་ནས། ཁྱིམ་བདག་རྗེས་སུ་གནང་གིས་རྩིགས༌[^3539]ཤིག་ཅེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3470]
འདིར་གྲོང་ཁྱེར་གྱི་ཕྱི༌[^3540]རོལ་དུ་ཞེས་གསུངས་པ་ནི། བྱུང་བའི་དབང་གིས་སྨོས་པ་ཡིན་གྱི།[^3541] གྲོང་ཁྱེར་གྱི་ནང་དུ་ཡང་འགལ་བ་མེད་པས་འདིར་གཉིས་ཀ་མདོར་བསྡུས་སོ། །
--- END BLOCKS ---
