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
[Block 3501]
དེས་ཆོམ་རྐུན་པའི་རང་དབང་ཉིད་མེད་པར་མི་ཤེས་པར་སྒོ་དབྱེ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་གི་སྲུང༌[^3574]མ་དེས་གཞན་དག་གཙུག་ལག་ཁང་གི་སྒོ་ཕྱེ་ཤིག་ཅེས་ཟེར་ན། ཆོམ་རྐུན་པའི་རང་དབང་ཉིད་མེད་པ་ངེས་པར་མི་ཤེས་པར་སྒོ་དབྱེ་བར་མི་བྱའོ། །

[Block 3502]
འདིར་ངེས་པར་ཤེས་པར་བྱ་བའི་ཐབས་གང་ཞེ་ན། དེའི་ཕྱིར་ཁང་སྟེང་དུ་འཛེགས་ལ་བལྟ༌[^3575]སྟེ། ཁྱོད་རིམས་ཀྱིས༌[^3576]མ་བཏབ་བམ་ཞེས་བརྗོད་པ་ནི་འདིར་ཐབས་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱོད་རིམས་ཀྱིས༌[^3577]མ་བཏབ་བམ་ཞེས་བརྡ་སྐད་བརྗོད་པ་ནི་སྨྲར་གཞུག་པའོ། །

[Block 3503]
གནས་དང་མིང་དང་ཕ་མ་ལ་སོགས་པ་སོ་སོར་ཤེས་པར་བྱེད་དུ་གཞུག་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་བརྗོད་པ་ནི་ཐབས་ཡིན་ནོ། །

[Block 3504]
འདི་རྗོད་པར་བྱེད་དུ་གཞུག་པའོ། །

[Block 3505]
ཡིད་མ་ཆེས་ཤིང་འཇིགས་པ་དང་བཅས་པ་ཉིད་ལ་སྒོ་དབྱེ་བར་མི་བྱའོ། །

[Block 3506]
དགོན་པ་བས་ཁྱི་བཅང་བར་བྱའོ། །

[Block 3507]
དེས་ནང་པར་སྔར་ལངས་མ་ཐག་ཁོ་ནར་གཙུག་ལག་ཁང་དང་མཆོད་རྟེན་གྱི་འཁོར་ས་བལྟ་བར་བྱའོ་ཞེས་བྱ་བ་ལ།[^3578] དེས་ཞེས་བྱ་བ་ནི་ཁྱི༌[^3579]འཆང་བ་པོས༌[^3580]སོ། །

[Block 3508]
ལངས་མ་ཐག་ཅེས་བྱ་བ་ལ་ལངས་མ་ཐག་ཁོ་ནར་ཞེས་བྱ་བའི་སྒྲས་ནི་བྱ་བ་གཞན་དག་མ་བྱས་པའི་མདུན་རོལ་དུ་བལྟ་བར་བྱའོ་ཞེས་བསྟན་པས་ནི་ཉི་མ་ཤར་བར་ལངས་པ་འདིས་བཀག་པ་ཡིན་ནོ། །

[Block 3509]
གལ་ཏེ་དེས་བཤང་བ་བྱས་ན་དོར་བར་བྱ་ཞིང་གཅི་བ་བྱས་ན་ཕྱི་བར་བྱ། གལ་ཏེ་སྡེར་མོ་དག་གིས་བྲད་ན་མཉམ་པར་བྱའོ། །

[Block 3510]
དེ་དག་གི༌[^3581]གནས་དག་ཏུ་དཀྱིལ་འཁོར་བྱའོ་ཞེས་བྱ་བ་ནི་བཤང་བ་ལ་སོགས་པ་དེ་དག་གི༌[^3582]གནས་དག་ཏུ་བྱའོ། །ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3511]
དེ་ཇི་ལྟར་གསོ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དེ་ལ་ལྷུང་བཟེད་ཀྱི་ལྷག་རོལ་སྦྱིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ་ཁྱི་དེ་ལའོ། །གང་དུ་དེ་སྦྱིན་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་མཆོད་རྟེན་དང་གཙུག་ལག་ཁང་གི་ཉེན་ཀོར་གྱི་ཕྱི༌[^3583]རོལ་དུའོ། །

[Block 3512]
སྤྱོད་ལམ་ཅི་འདོད་པས་ལུང་དབོག་གོ་ཞེས་བྱ་བ་ལ། ལུང་དབོག་པ་ནི་སྤྱོད་ལམ་བཞི་པོ་དག་ལས་ཅི་འདོད་པས་དབོག་ན་ཡང་དེ་ལ་ཉེས་པ་མེད་པའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3513]
གསར་བུས་མནོད་པའི༌[^3584]ཕྱིར་ཁམས་སྙོམས་པ་ཉིད་དྲི་སྟེ། ཕྱག་བྱ་བ་སྔར་བཏང་བའི་སྤྱོད་ལམ་བསྟེན་པར༌[^3585]བྱའོ་ཞེས་བྱ་བ་ནི་གསར་བུས་བླ་མ་ལ་ཀླག་པའི་ལུང་མནོད་པའི་ཕྱིར། སྔར་ཕྱག་བྱ་སྟེ་བསྙུན་གསོལ་ནས་བྱ་བའི་སྤྱོད་ལམ་བསྟེན་པར༌[^3586]བྱའོ། །

[Block 3514]
རྒན་པས་ནི་ཕྱག་མི་བྱ་བར་བསྙུན་གསོལ་ནས་སོ། །

[Block 3515]
ཐལ་མོ་བསྣོལ་ཏེ་བཅང་ངོ་ཞེས་བྱ་བ་ནི་ལག་པ་གཉིས་ཀྱིས་ཐལ་མོ་བསྣོལ་ཏེ་བཅང་བའི་སྤྱོད་ལམ་བསྟེན་པར་བྱའོ། །

[Block 3516]
ལུས་དང་སེམས་བཏུད་དོ་ཞེས་བྱ་བ་ནི་ལུས་བཏུད་པ་དང་སེམས་བཏུད་པར་བྱ་བ་སྟེ། ང་རྒྱལ་གྱིས་སེམས་ཁེངས་པའི་ཡན་ལག་ཀྱང་སེམས་དམའ་བ་ཉིད་ཡིན་ལ་གུས་པ་དང་བཅས་པ་ཉིད་ཀྱང་སེམས་དམའ་བ་ཉིད་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3517]
དྲང་པོར་རོ་ཞེས་བྱ་བ་ནི་གྱ་གྱུ་མེད་པ་དང་སྒྱུ་དང་གཡོ་མེད་པར་བྱའོ། །

[Block 3518]
ལུང་འབོགས་པར༌[^3587]བྱེད་པ་གནས་ཇི་ལྟ་བུ་དེ་ལྟ་བུར་གྱུར་པའི་སྤྱོད་ལམ་བསྟེན་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་འཆག་པ་ན་གོམ་པ་སྲི་བས་བཅག་པའིའོ་ཞེས་བྱ་བ༌[^3588]སྨོས་ཏེ། ལུང་འབོགས་པར༌[^3589]བྱེད་པ་འཆག་པ་ན་ལུང་ནོད་པར་བྱེད་པས་གོམ་པ་སྲི་བར་བཅག་པའི་སྤྱོད་ལམ་བསྟེན་པར་བྱའོ།[^3590] །འགྲེང་བ་དང་འགྲེང་བའི་འོ་ཞེས་བྱ་བ་ནི་ལུང་འབོགས་པར༌[^3591]བྱེད་པ༌[^3592]འགྲེང་བ་ན་ལུང་ནོད་པར་བྱེད་པས་ཀྱང་འགྲེང་བའི་སྤྱོད་ལམ་བསྟེན་པར་བྱའོ། །

[Block 3519]
འདུག་པ༌[^3593]དང་ཉལ་བ་ན་འདུག་པའི་འོ་ཞེས་བྱ་བ་ནི་བསྟེན་པར་བྱའོ།[^3594] །གང་དུ་འདུག་པའི་སྤྱོད་ལམ་བསྟེན་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་སྟན་ཆེས་དམའ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཆེས་རྒན་པ་ནི། རྗེས་སུ་གནང་བ་ལ་མི་ལྟོས་པ་ཉིད་ཀྱིས་རང་འདུག་པར་བྱའོ། །

[Block 3520]
གསར་བུས་རྗེས་སུ་གནང་བ་ལ་ལྟོས་ཏེ་འདུག་པར་བྱ་བ་བསྟན་པའི་ཕྱིར་གསར་བུས༌[^3595]ནི་བསྒོ༌[^3596]ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་ལུང་འབོགས་པར༌[^3597]བྱེད་པས་བསྒོ༌[^3598]ཞིང་རྗེས་སུ་གནང་ན་འདུག་པར་བྱའོ། །

[Block 3521]
མ་བསྒོ་བའི༌[^3599]ཆོ་ག་བསྟན་པའི་ཕྱིར། མ་བསྒོ་ན་ཙོག་པུས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདུག་པ༌[^3600]བསྟེན་པར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3522]
མནོད་པར་བྱ་བ༌[^3601]མང་བ་ཉིད་ཡིན་ན་ཞུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ལུང་མནོད་པར་བྱ་བའི་གཞུང་མང་བ་ཉིད་ཡིན་ན་འདུག་པའི་ཕྱིར་ལུང་འབོགས་པར༌[^3602]བྱེད་པ་ལ་ཞུ་བར་བྱའོ། །

[Block 3523]
འདིར་གཞུང་ནི་གལ་ཏེ་གསར་བུས་ཡིན་ལ། མང་དུ་ནོད་ན་སློབ་དཔོན་ལ་ཞུས་ཏེ་སྟན་ཆེས་དམའ་བ་ལ་འདུག་ནས་ལུང་མནོད་པར༌[^3603]བྱའོ། །

[Block 3524]
ཇི་སྟེ༌[^3604]ཉུང་དུ་ནོད་ན་ནི་ཙོག་བུས་འདུག་སྟེའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3525]
ཐོས་པའི་ཉེན་ཀོར༌[^3605]མ་གཏོགས་པ་སྣང་བའི་ཉེན་ཀོར་དུ་འདུག་སྟེ་ཁ་ཏོན་བྱའོ་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཉེན་ཀོར་དུ་གནས་ནས་སོ། །

[Block 3526]
གདམས་ངག་ནི་མཐའ་གཅིག་ཏུ་སོང་སྟེ་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྒོམ་པའི་གདམས་ངག་གོ། །

[Block 3527]
ལུང་འབོགས་པ༌[^3606]དང་མནོད་པའི༌[^3607]ཤིན་ཏུ་ལེགས་པར་བསླབས་པ༌[^3608]དང་། ཤིན་ཏུ་ཡོངས་སུ་བྱང་བ་དང་ཐེ་ཚོམ་མེད་པར་བྱས་ཏེའོ། །

[Block 3528]
གནས་ཁང་དང་ཟས་ལ་བསྐོ་བ་དང་ཐུག་པ་དང་བག་ཆོས་དང་ཤིང་ཐོག༌[^3609]འདྲིམ་པ་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་ཁང་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་བར་བྱའོ། །

[Block 3529]
ཐུག་པ་དང་བག་ཆོས་དང་ཤིང་ཐོག༌[^3610]འདྲིམ་པ་ཡང་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^3611]སྒྲ་དང་སྦྱར་རོ། །

[Block 3530]
བར་བུར་འདྲིམ་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3531]
གཞུང་ཁ་ཅིག་ལས་ནི་བར་བུར་འདྲིམ་པ་ཞེས་བྱ་བ་འདིའི་མིང་ཕྲན་ཚེགས་འདྲིམ་པ་ཞེས་འབྱུང་ངོ་། །བར་བུར་ཞེས་བྱ་བ་དེ་ཅི་ཡིན་ཞེ་ན་དེའི་ཕྱིར། ལྷག་རོལ་ཕྱི་དེ་ཉིན་པར་བྲིམ་པར༌[^3612]བྱ་བ་ནི་དེ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་བག་ཆོས་ལ་སོགས་པ་བྲིམ་པའི༌[^3613]ལྷག་རོལ་ལུས་པས་སུ་ཡང་བྲིམ་པར༌[^3614]མི་བྱེད་པ་ན། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བར་བུར་བྲིམ་པ༌[^3615]བསྐོ་བར་བྱ་ཞིང་དེས་དེ་དག་ཕྱི་དེ་ཉིན་པར་བྲིམ་པར༌[^3616]བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3532]
སྣོད༌[^3617]སྤྱད་འདྲུབ་པའོ་ཞེས་བྱ་བ་ནི་བསྐོ་བར་བྱའོ། །

[Block 3533]
དབྱར་གྱི༌[^3618]རས་ཆེན་ནོ་ཞེས་བྱ་བ་ནི་སྦེད་པ་པོ་བསྐོ་བར་བྱའོ། །

[Block 3534]
སྣམ་སྦྱར་ཞེས་བྱ་བ་ནི་འདི་ལ་དགེ་འདུན་གྱི་བསམ་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་ཤེས་པའོ། །

[Block 3535]
ཆོས་གོས་བསྟན་པའོ་ཞེས་བྱ་བ་ནི་སྦེད་པ་པོ་བསྐོ་བར་བྱའོ། །

[Block 3536]
གང་ཞིག་འདི་གདིང་བ་པོ་བསྟན་པ་སྟེ། འདིར་སྦེད་པའོ་ཞེས་བྱ་བར་རྗོད་པ་པོ༌[^3619]རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3537]
གོས་དག་གོ་ཞེས་བྱ་བ་ནི་སྦེད་པ་པོ་བསྐོ་བར་བྱའོ། །

[Block 3538]
འགྱེད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གོས་སྦེད་པ་དང་འགྱེད་པ་པོ་དེ་གཉིས་བསྐོ་བར༌[^3620]བྱའོ། །

[Block 3539]
དགེ་སྐོས་དང་མངག༌[^3621]གཞུག་གོ་ཞེས་བྱ་བ་ནི༌[^3622]སྐོས་ཅི་རིགས་པར་སྦྱར་བའི་ཕྱིར་བསྡུས་པའོ། །

[Block 3540]
དགེ་སྐོས་ཀྱི་བྱ་བ་དང་བག་ཡངས་སུ་གྱུར་པ་དང་དེས་བྱ་བ་གང་ཡིན་པ་དེས་དེ་འགྲུབ་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
