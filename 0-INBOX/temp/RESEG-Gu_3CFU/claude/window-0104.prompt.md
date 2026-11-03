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
[Block 3641]
འདིར་ལུང་ནི་སྦྱོར་བ་ནི་ཡོངས་སུ་དག་པ་ཉིད་དེ། འདིར་རྒྱུན༌[^2503]ལ་དེར་འཛིན་པ་མ་ཡིན་ནོ། །

[Block 3642]
སྦྱོར་བ་དེས་དེ་དང་འབྲེལ་བའི་རྫས་ཀྱི་ཁྱད་པར་བུམ་པ་དང་སྣམ་བུ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 3643]
ཞག་བདུན་པ་ལ་ནི་རིགས་མཐུན་པ་ལའོ་ཞེས་བྱ་བ་ནི་རྫས་ཀྱི་རིགས་འདྲ་བ་ལ་ཞག་བདུན་པའི་དོན་དུ་ལྷག་པར་གནས་པ་ལ་རྗེས་སུ་འཇུག་པ་ཉིད་ཡོད་པ་འདི་ལ་སྐྱེས་པ་ཉིད་དོ། །

[Block 3644]
འདིར་རྣམ་པར་འབྱེད་པའི་གཞུང་འགའ་ཞིག་ལས་མར་དང་འབྲེལ་བ་ནི་མར་ལའོ། །

[Block 3645]
འབྲུ་མར་དང་འབྲེལ་པ་ནི་འབྲུ་མར་ལའོ། །

[Block 3646]
སྦྲང་རྩི་དང་འབྲེལ་པ་ནི་སྦྲང་རྩི་ལའོ། །

[Block 3647]
ཧྭགས་དང་འབྲེལ་པ་ནི་ཧྭགས་ལའོ། །

[Block 3648]
འབྲེལ་པ་དང་བཅས་པ་ནི་འབྲེལ་པ་དང་བཅས་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3649]
དོན་ཐ་དད་པས་འདི་ལྟ་བུ་ཉིད་དུ་རྣམ་པར་གཞག་པའོ། །

[Block 3650]
ལྟུང་བ་དེ་ཡོད་ན་ཡོ་བྱད་ཙམ་བདག་གིར༌[^2504]བྱས་པ་ལ་སྤང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སྤང་བའི་ལྟུང་བྱེད་དེ་ཡོད་ནའོ། །

[Block 3651]
རང་བཞིན་གྱིས་མ་གྲུབ་པ་ལ་སྤང་བའི་ལྟུང་བྱེད་དག་ཏུ་བྱེད་པ་ལ་གང་དུ་ཡོ་བྱད་འགའ་ཞིག་ལ་སྤང་བའི་ལྟུང་བྱེད་ལས་སྐྱེས་པ་ཉིད་དོ། །

[Block 3652]
འདི་ནི་སྤང་བའི་ལྟུང་བྱེད་ལས་མ་སྐྱེས་པ་ཉིད་བྱས་པར་རིག་པར་བྱའོ། །

[Block 3653]
སྤང་བ་ཉིད་ཙམ་ལ་ཆོ་ག་འདི་ལྟ་སྟེ་སྤང་བའི་ལྟུང་བྱེད་རང་བཞིན་གྱིས་མ་བྱས་པ་ཉིད་ལ་ཇི་སྲིད་དུ་ཐམས་ཅད་འགྲུབ་པ༌[^2505]དངོས་པོ་ཐམས་ཅད་དེ་དངོས་པོ་གང་ལས་ལྟུང་བ་དེ་བསྐྱེད་པ་དེའི་དངོས་པོ་བཞིན་དུ་དེ་ལ་ཡང་བྲལ་བ་མ་བྱས་པའོ། །

[Block 3654 [VERSE]]
དེའི་ཕྱིར་ལྟུང་བ་ནི་བཤགས༌[^2506]པར་བྱ་མི་དགོས་ཏེ། །
དེའི་གཞི་ལས་ལྟུང་བ་མ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 3655]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་ཆོས་གོས་སྤང་བ་མ་སྤངས་ཤིང་བྲལ་བར་མ་བྱས་ལ་ལྟུང་བ་དེ་ཡང་མ་བཤགས་པར་གཞན་ཞིག་རྙེད་ན་དེ་ཡང་སྤང་བ་ཡིན་ཏེ། སྔ་མའི༌[^2507]ཤུགས་ཀྱིས་སོ་ཞེས༌[^2508]བྱ་བ་ལ་སོགས་པ་གསུངས་པ༌[^2509]ཡིན་ནོ། །

[Block 3656]
ཆུང་བ༌[^2510]ཉིད་ཀྱི་དུམ་བུ་དེ་ནི་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་དེ་ནི་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་སྤང་བ་ཉིད་དོ། །

[Block 3657]
འཁོར་ཡུག༌[^2511]གི༌[^2512]མཐའ་མཉམ་པ་ནི༌[^2513]སྤང་བའི་ལྟུང་བྱེད་རྣམས་ལ་དེ་བས་ན་མ་ཚང་བ་རྣམས་ལ་ཞེས་བྱ་བར་གཏོགས་པའོ། །

[Block 3658]
འཁོར་ཡུག་མཉམ་པ༌[^2514]ལས་མ་ཚང་བ་ཉིད་ལ་དུམ་བུ་ནི་སྤང་བ་ཉིད་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3659]
སྤང་བ་ཉིད་ལ་འདི་དུམ་བུ་ཉིད་དུ་འབྲེལ་པ་ལ་དུམ་བུ་རྣམས་ལ་བྲལ་བར་མ་བྱས་པ་ལ་བྱེད་པའོ། །

[Block 3660]
འདིར་གཞུང་ནི་ཉེ་བ་འཁོར་གྱིས་ཞུས་པ་ལས་བཙུན་པ་དགེ་སློང་གིས་ཆོས་གོས་སྤང་བ་ཚིག་གམ་སྲོག་ཆགས་དག༌[^2515]དང་སྲིལ་དག་གིས་འཚལ་བར་གྱུར་ན་དེ་ལ་ཕྱ་ཕྱེ་འམ་དམ་དུམ་གང་དག་མཆིས་པ་དག་སྤང་བར་བགྱི་འམ་ཉེ་བ་འཁོར་མི་བྱ་སྟེ། ལྟུང་བྱེད་འགའ་ཞིག༌[^2516]བཤགས་པར་བྱའོ། །

[Block 3661]
ལྷག་པར་གནས་པར༌[^2517]བྱ་བ་མ་ཡིན་ཞེས་གསུངས་པ་དེ་ཉིད་དེ་རྣམས་ལ་ལྷག་པར་གནས་པ་དེ་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 3662]
དགེ་འདུན་གྱི་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་མངའ་བ་གང་ཟག་གིས་བདག་ཉིད་དུ་རིས་སུ་བཅད་པ་དང་། དགེ་འདུན་མངའ་རིས་སུ་མ་བཅད་པའོ། །

[Block 3663]
སྤང་བའི་ལྟུང་བྱེད་དག་གིས༌[^2518]ཡང་འཆང་བ་དང་འབྲལ་བ་དང་འཇོག་པ་དེའི་རྒྱུས་སྤང་བའི༌[^2519]ལྟུང་བྱེད་རྣམས་ལ་ཡང་དེར་གང་ཟག་གཅིག་པ༌[^2520]དང་འདྲ་བར་གང་ཟག་རེ་རེས་བདག་ཏུ་བྱས་པས་ཡང་དག་པར་གནས་པའོ། །

[Block 3664]
དགེ་འདུན་མངའ་རིས་སུ་བཅད་པའི་དགེ་འདུན་དང་འབྲེལ་པ་ལ་བདག་ཏུ་བྱས་པས་སུ་ཞིག་མེད་པས་འཆང་བ་དང་འཇོག་པའི་རྒྱུས་སྤང་བའི་ལྟུང་བྱེད་དག་གི་ཡང་སྐབས་མེད་པས་གནས་པའི་རྒྱུས་ལྷག་པར༌[^2521]གནས་པ་ལ་མངའ༌[^2522]རིས་སུ་མ་བཅད་པ་མི་སྲིད་པའི་ཕྱིར་གང་ཟག་གཅིག་གིས་དགེ་འདུན་རིགས་སུ་བཅད་པ་དང་ལྷག་པར་འབྲེལ་བ་གནས་པ་སྤང་བའི་ལྟུང་བྱེད་ལ་གླག༌[^2523]ཡོད་དེ་དེ་བས་ན་མདོ་འདི་ཡིན་ནོ། །

[Block 3665]
འདིར་གཞུང་ནི་ཉེ་བ་འཁོར་གྱིས༌[^2524]ཞུས་པ་ལས།

[Block 3666]
བཙུན་པ་དགེ་སློང་གིས་དགེ་འདུན་གྱི་ཆོས་གོས་བྱིན་གྱིས༌[^2525]བརླབས་ནས༌[^2526]མཚམས་ཀྱི་སླད་རོལ་ཏུ་འབྲལ་བར་བགྱིད་ན་ཆོས་གོས་དང་བྲལ་ཞེས་བགྱི་འམ་མ་བྲལ་ཞེས་བགྱི་བཀའ་སྩལ་པ། ཆོས་གོས་དང་བྲལ་ཞེས་བྱའོ། །

[Block 3667]
ཆོས་གོས་དེ་སྤང་བར་བགྱིའམ། ཉེ་བ་འཁོར་མི་བྱ་སྟེ། ལྟུང་བྱེད་འབའ་ཞིག་བཤགས་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3668]
དེ་བས་ན་གང་དུ་རང་ཉིད་ལ་གཏད་པ་ཉིད་མ་ཡིན་པ་ནི་འདི་ལྟ་སྟེ་དགེ་འདུན་གྱི་ཆོས་གོས་དེ་ལ་བྱ་བ་ཉིད་དོ། །

[Block 3669]
འདི་ལ་མེད་པ་དེ་ཉིད་གཙོ་བོའོ་ཞེས་བྱ་བ་ནི་འདི་ལ་དངོས་པོ་དེ༌[^2527]ཡོད་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི་འདི་ལ་དངོས་པོ་དེ་མེད་པས་ན་མེད་པའོ། །

[Block 3670]
མེད་པའི་དངོས་པོ་ནི་མེད་པ་ཉིད་དོ། །

[Block 3671]
དེ་ཉིད་སྤང་བ་ཉིད་ལ་གཙོ་བོ་ཡིན་གྱི་སྤང་བར་བྱ་བའི་རྫས་ནི་གཙོ་བོ་མ་ཡིན་ནོ། །

[Block 3672]
ཐམས་ཅད་མེད་པས་འདི་ལ་བྱ་བ་ཉིད་དུ་ཤེས་ནས་འདིར་ཅི་ཞིག་བྱ་བ་ཞེས་བྱ་བ་ཐེ་ཚོམ་མི་བྱ་ཞེས་བྱ་བ་འདི་ལ་འདི་བྱེད་པའོ། །

[Block 3673]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 3674]
བཙུན་པ་དགེ་སློང་གིས་ཆོས་གོས་སྤང་བ་ཉམས་པར་གྱུར་ན་ལྟུང་བྱེད་བཤགས་པར་བགྱི་འམ། ཉེ་བ་འཁོར་མ་དག་པ་ནི་བཤགས་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3675]
འདི་གསུམ་ནི་སྲ་བརྐྱང་བཏིང་བ་ལ་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་འཆང་བ་འམ་འབྲལ་བ་དང་འཇོག་པ་ལྷག་པར་གནས་པའོ། །

[Block 3676]
ཐུན་མོང་བ་ནི་སོང་ཟིན་ཏོ།། །།

[Block 3677]
དེ་ནས་སོ་སོའི་སྐབས་བརྗོད་པར་བྱ་སྟེ། གང་དུ་འཆང་བའི་སྤང་བའི་ལྟུང་བྱེད་བསྐྱེད་ཅེ་ན། དེའི་ཕྱིར་ཡོད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་སུ་ཡོད་ཅེ་ན། དེའི་ཕྱིར་རང་གི་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཐམས་ཅད་ལ་ཡང་མ་ཡིན་ནོ། །

[Block 3678]
འོ་ན་གང་ཞེ་ན། དེའི་ཕྱིར་ཞག་བཅུར་རྗེས་སུ་ཞུགས་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3679]
དུས་གང་གི་ཚེ་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གཞན་གྱི་ཉི་མའི་དང་པོ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་རྗེས་སུ་ཞུགས་པའི་དུས་འདི་ཞག་བཅུར་བརྗོད་པ་གང་ཡིན་པ་དེ་ལས་གཞན་པའི་ཞག་ལ་དང་པོར་སྐྱ་རེངས༌[^2528]འཆར་བའི་སྐད་ཅིག་མ་དང་པོ་ལའོ། །

[Block 3680]
རང་ཉིད་གང་དུ་སྟེ་དུས་ཙམ་གང་ཞིག་ལ་ཡོད་པ་ན་ཞེ་ན། དེའི་ཕྱིར་གོས་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །
--- END BLOCKS ---
