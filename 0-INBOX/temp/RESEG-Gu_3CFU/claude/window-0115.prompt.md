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
[Block 4026]
ཉེས་བྱས་ཙམ་ལ་ནི་འདི་བྱེད་པ་པོ་དེ། འདིས་ནི་ཞུ་བ་ལས་ཉེ་དུ་མ་ཡིན་པ་ལས་ཆོས་གོས་མི་ཆོག་པ་ཉིད་སློང་ན་ཉེས་བྱས་ཀྱི་ལྟུང་བར་འགྱུར་རོ། །

[Block 4027]
རྒྱུ་སློང་ན་ཡང་ཉེས་བྱས་སོ། །

[Block 4028]
སྤུན་སློང་ན་ཡང་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་དེ་དག་བསྡུས་པ་ཡིན་ནོ། །

[Block 4029]
དེའི་རང་བཞིན་ནི་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི། རྒྱུ་དང་སྤུན་གྱི་སྐུད་པ་དང་འདྲའོ། །

[Block 4030]
འདིས་ནི་ཐ་ག་བའི་ཞུ་བ་ལས།

[Block 4031]
བཙུན་པ་རེ་ཞིག་དགེ་སློང༌[^2750]རས་བལ་སློང་བར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 4032]
སློང་བའི་སྤང་བ་སྟེ་དྲུག་པའོ།། །།

[Block 4033]
བྱིན་གྱིས་བརླབ་པར་བྱ་བ་ཐམས་ཅད་མེད་ན་སློང་བར་རིག་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། ཐམས་ཅད་ཅེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་ཆོས་གོས་གསུམ་ལས་གཞན་པ་ལ་ཡང་ཡོ་བྱད་དང་ཆོས་གོས་བཅུ་གསུམ་པོ་རྣམས་ལ་ནི་རྗེས་སུ་གནང་བའོ། །

[Block 4034]
མེད་པར་གྱུར་ན་ཡོ་བྱད་ཐམས་ཅད་བླང་བར་རིག་པ༌[^2751]ཉིད་དོ། །

[Block 4035]
ཆོས་གོས་གསུམ་པོ༌[^2752]འབའ་ཞིག་ཏུ་མ་ཟད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4036]
འདིར་གཞུང་ནི། ཡི་གེ་ཁ་ཅིག་ལས་ནི་དབྱར་གྱི་རས་ཆེན་མི་སྨོས་པར་ཁྲུས་རས་ཞེས་འབྱུང་སྟེ། ཉེ་དུ་མ་ཡིན་པའི་དྲུང་ནས་སློང་བར་བྱེད་ན་ལྟུང་བ་མེད་ཅེས་བྱའོ། །

[Block 4037]
དེ་ནི་ལྟུང་བའི་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བ་ལ་དེ་ནི་ཞེས་བྱ་བ་ནི་སློང་བར་རིགས་པ་ལའོ། །

[Block 4038]
སྤྱི་ཙམ་ལ་འདི་ཉེ་བར་གནས་པ་སྟེ་རྫས་ལ་ཡང་མ་ཡིན་ནོ། །

[Block 4039]
འདིར་གང་ཟག་ནི་སློང་བར་རིགས་པར༌[^2753]བརྗོད་པར་རིག་པར་བྱའོ། །

[Block 4040]
ཉེ་དུ་མ༌[^2754]ཡིན་པ་ལས་ཆོས་གོས་སློང་བ་རིགས་པ་ཞེས་བྱ་བ་བྱས་ནས་སོ། །

[Block 4041]
སླར་ཡང་དེ་གང་ཞེ་ན་ཆོས་གོས་ཕྲོགས་པ་ལ་སོགས་པའོ། །

[Block 4042]
གང་ལས་འདིར་ཉེས་བྱས་བརྗོད་པ་ཉིད་ཀྱིས་སློང་བར༌[^2755]མི་རིགས་པ་སློང་བའི་རྙེད་པ་ལ་སྔ་མའི་ལྟུང་བའོ། །

[Block 4043]
འདི་ནི་སློང་བར་རིགས་པ་སློང་བར་བྱེད་པའི་དབང་གིས་བྱས་པའོ། །

[Block 4044]
དེ་གང་ལས་འབྱུང་ཞེ་ན། སོ་སོར་ཐར་པའི་མདོ་ལས་ཆོས་གོས་ཆུས་ཁྱེར་ན་ཉེ་དུ་མ་ཡིན་པའི་ཁྱིམ་བདག་གམ་ཁྱིམ་བདག་གི་ཆུང་མའི་དྲུང་དུ་སོང་སྟེ་ཆོས་གོས་བླང་བར་བྱའོ། །

[Block 4045]
དེ་ལ་གལ་ཏེ་བྲམ་ཟེ་དང་ཁྱིམ་བདག་དད་པ་ཅན་དག་གིས་ཆོས་གོས་རབ་ཏུ་མང་པོ་དག་དུས་ཀྱིས་སྟོབས་པར་གྱུར་པ་ན་དགེ་སློང་དེས་འདོད་ན་ཆོས་གོས་དེ་ལས་སྟོད་གཡོགས་དང་སྨད་གཡོགས་སུ་བཅས་པ་མན་ཆད་བླང་བར་བྱའོ། །

[Block 4046]
དེ་ལས་ལྷག་པར་ལེན་ན་སྤང་བའི་ལྟུང་བྱེད་དོ་ཞེས་སློང་བར་རིགས་པས་བླངས་ཏེ་ཐོབ་པ་ན་ལྟུང་བྱེད་དོ་ཞེས་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 4047]
གང་ཞིག་ཡང་རྣམ་པར༌[^2756]འབྱེད་པ་ལས་དགེ་སློང་གིས་ཁྱིམ་གྱི༌[^2757]ནང་དུ་འོག་མ་འོག་མ་ལ་སློང་བར་བྱེད་ཅིང་། དེ་བླངས་པ་ན་ཉེས་བྱས་སུ་འགྱུར་ཏེ་སྤང་བའི་ལྟུང་བྱེད་དོ་ཞེས་བརྗོད་དོ། །

[Block 4048]
དེ་ལ་སྦྱོར་བ་ཐོབ་པའི་ཕྱིར་སྔར་གྱི་བསླབ་པའི༌[^2758]གཞི་བརྗོད་པ་དངོས་གཞི་ཐོབ་པའི་ཕྱིར་གཉིས་ཀ་དང་འབྲེལ་པ་འདིར་བསླང་བར་བྱ་བ་དང་། སློང་བར་བྱེད་པའི་དབང་ཉིད་ཀྱིས་དེ་རྙེད་པ་འཛིན་པ་མ་ཡིན་ཏེ། གཞན་ཡང་བསླང་བར་བྱ་བ་དང་བསླབ་པའི་དབང་གིས་ཀྱང་བསླབ་པའི་གཞི་འདི་དང་འབྲེལ་པའོ། །

[Block 4049]
གཞན་དུ་ན་དངོས་གཞི་ལོངས་མ་སྤྱད་པ་ཉིད་ཐོབ་པའི་ཕྱིར་བསླང་བར་བྱ་བ་མ་ཡིན་པའི་དབང་གིས་གསུངས་པ་གང་ཡིན་པ་དེ་ནི་སྔར་གྱི་བསླབ་པའི་གཞི་དང་འབྲེལ་པ་བསླང་བར་བྱ་བ་དང་། སློང་བར༌[^2759]བྱེད་པ་གང་ཡིན་པ་དེ་ནི་འདིར་བསླབ་པའི་གཞི་ལས༌[^2760]འབྲེལ་པའོ། །

[Block 4050]
ཟུང་བསླང་བར་བྱ་བ་ཉིད༌[^2761]ཅེས་བྱ་བ་འཆད་པར་འགྱུར་བ་དེའི་རང་བཞིན་བསྟན༌[^2762]པར་བྱ་སྟེ། ཁྱིམ་པའི་སྟོད་གཡོགས་ཆེ་ཚད་ནི་རས་ཡུག་ཆེན་ཁྲུ་བཅུ་གཉིས་པའོ། །

[Block 4051]
སྨད་གཡོགས་ནི་རས་ཡུག་ཕྲན་བདུན་པ་དང་དོ༌[^2763]པའོ་ཞེས་བྱ་བ་ནི་འདིར་དགེ་སློང་གི་སྟོད་གཡོགས་ཆེ་ཚད་ཀྱི་རྐྱེན་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 4052]
དེ་བས་ན་དངོས་པོ་གསུམ་ནི་འདིར་ཆེ་ཚད་ཅེས་བྱ་བར་རྟོགས་པར༌[^2764]བྱའོ། །

[Block 4053]
དགེ་སློང་གི༌[^2765]ཆེ་ཚད་ནི། སྣམ་སྦྱར་དང་ཤམ་ཐབས་ཀྱི་རིམ་པ་ཇི་སྐད་བསྟན་པའོ་ཞེས་བྱ་བ་ནི། འདིར་ཆེ་ཚད་ཅེས་བྱ་བར་སྦྱར་རོ། །

[Block 4054]
ཟུང་བསླང་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སྟོད་གཡོགས་དང་སྨད་གཡོགས་ཀྱི་ཟུང་འདི་ལ་ཁྱིམ་པ་དག་དང་། དགེ་སློང་གི་ཟུང་འདི་དག་ལས་གང་བསླང་བར་བྱ་བ་ཉིད་ཡིན་ཅེ་ན། དེའི་ཕྱིར་གང་ཡང་རུང་བའོ་ཞེས་བྱ་བ་ནི། ཁྱིམ་པའི་སྟོད་གཡོགས་སྨད་གཡོགས་དང་བཅས་པ་འམ། དགེ་སློང་གི་སྟོད་གཡོགས་སྨད་གཡོགས་དང་བཅས་པའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4055]
ཤུགས་ཀྱིས་རྟོགས་པ་དང་དངོས་སུ་བརྗོད་པར་བྱ་སྟེ། ཚད་དེ་ལས་ལྷག་པ་ནི་བསླང་བར་བྱ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཐ་དད་པར་གྱུར་ཀྱང་རུང་ཐ་དད་པར་གྱུར་པ་མ་ཡིན་པ༌[^2766]ཡང་རུང་སྟེ། ཚད་ལས་ལྷག་པར་བསླང་བར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 4056]
དེའི་སྔ་མ༌[^2767]ཉིད་ལ་བསླབ་པའི་གཞི་ལས་ལྟུང་བའོ། །

[Block 4057]
འདིར་ཟུང་བཤད་པའི་ཚད་གཙོ་བོ་བརྗོད་པར་འདོད་པ་མ་ཡིན་པ་གཅིག་དང་འབྲེལ་པ་ཉིད་དེར་བྱས་པར་འགྱུར་རོ། །

[Block 4058]
འདིས་ཐ་དད་དུ་གྱུར་པ་ལ་ཆུང་བ་རྙེད་པ་ལ་རྫོགས་པར་བྱེད་པ་ལ་བླངས་པ༌[^2768]ཉིད་དོ། །

[Block 4059]
དེ་ནི་ཁྱིམ་པའི་སྟོད་གཡོགས་དང་སྨད་གཡོགས་ལས་འདའ་བར་བརྗོད་པར་བྱ་སྟེ། ཚད་དེ་ལས་ལྷག་པར་ནི་བསླང་བར་བྱ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 4060]
སྔ་མ་ལས༌[^2769]ན་ཁ་བསྐང་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བསླང་བར་བྱ་བ་ཉིད་མ་ཡིན་པའི་རྗེས་སྙེགས༌[^2770]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 4061]
སྔ་མ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པའི་སྟོད་གཡོགས་དང་སྨད་གཡོགས་མ་ཆོག་པ་རྙེད་པ་ལ་དེའི་ཁ་བསྐང་བ་བསླང་བར་མི་བྱ་བའི་དོན་ཏོ། །

[Block 4062]
ཁྱིམ་པའི་ཆེ་ཚད་ནི་ཁྲུ་བཅུ་གཉིས་པའོ་ཞེས་བྱ་བ་ནི་མཆོག་ཏུ་གྱུར་པ་ལ་ཁྱིམ་པའི་སྟོད་གཡོགས་དང༌[^2771]སྨད་གཡོགས་ཀྱི་ཚད་དུ་གསུངས་སོ། །

[Block 4063]
དེ་བས་ན་འདི་ལས་ཆུང་བ་ཐམས་ཅད་ཉིད་དུ་ཁྱིམ་པའི་སྟོད་གཡོགས་སྨད་གཡོགས་ལ་མེད་པ་མ་ཡིན་ནོ། །

[Block 4064]
སླར་གང་ཞིག་འདིའི་མཐར་ཐུག་པའི་རིགས་པ་ཡིན་ཏེ། རས་ཡུག་ཆེན་ཁྲུ་བཅུ་གཉིས་པ་དང་། རས་ཡུག་ཕྲན་བདུན་པ་དང་། དོ་པ་མན་ཆད་ནས་རས་ཡུག་ཆེན་ཁྲུ་ཕྱེད་དང་གསུམ་པ་དང་། ཇི་སྲིད་དུ་ཕྱེད་པ་དང་ལྔ་པའི་བར་དང་རས་ཡུག་ཕྲན་འཁོར་གསུམ་ཁེབས་པའི་ཚད་ཀྱི་བར་ནི་ཆུང་བའི་མཐའ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 4065]
གང་གི་ཕྱིར་འདིའི་དོན་གྲུབ་པ་ཉིད་ལ་མ་བླངས་པ༌[^2772]ཉིད་ནི་རྒྱུ་ཉིད་འདིར་མཐར་ཐུག་པའི་དོན་མཐར་ཐུག་པའི་ཁྱིམ་པའི་སྟོད་གཡོགས་དང་སྨད་གཡོགས་ཐོབ་པ་ལ་ཁྲུ་བཅུ་གཉིས་པ་ལ་སོགས་པ་ཁ་སྐོང་བར༌[^2773]བྱེད་པ་ལ་འདི་བསླང་བར་མི་བྱ་བ་ཉིད་བསྟན་པའོ། །
--- END BLOCKS ---
