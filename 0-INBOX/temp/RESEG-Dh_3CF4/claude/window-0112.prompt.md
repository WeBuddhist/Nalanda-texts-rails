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
[Block 3921]
སྐྱོན་དང་བཅས་ཤིང་ཚུལ་མ་ཡིན་པ་གང་ཡིན་པ་དེ་ནི་སྐྱོན་དང་བཅས་ཤིང་མི་རིགས་པའོ། །

[Block 3922]
ཟླ་བ་དང་རྒྱུ་སྐར་དང་སྐར་མ་ནི་ཟླ་བ་དང་རྒྱུ་སྐར་དང་སྐར་མ་སྟེ། སྟོན་གྱི་དུས་ལ་བབ་ཅིང་དྲི་མ་མེད་པའི་སྐར་མ་དང་རྒྱུ་སྐར་གྱི་རྒྱན་གང་ལ་ཡོད་པ་ཉིད་དེ་དེ་བས་ནའོ། །

[Block 3923]
ངང་པའི་ཚོགས་མང་པོ་ཞེས་བྱ་བ་ནི་ངང་པའི་ཁྱུ་མང་པོས༌[^2536]མཚོ་དེར་འདོད་པར་བྱ་བའི་གཏམ་བརྗོད་དེ། འདོང་བ་ནི་མཚོ་དེར་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 3924]
ཡིད་དུ་འོང་བའི་བཀོད་པ་ཡིན་བས་ཡིད་དུ་འོང་བའི༌[^2537]བཀོད་པའོ། །

[Block 3925]
ཡོན་ཏན་མཉམ་པ་མེད་པ་ནི་ཡོན་ཏན་མཚུངས་པ་མེད་པར་གྱུར་པའོ། །

[Block 3926]
གསེར་གྱི་འདབ་མ་ལྟར་མཛེས་པའི་འདབ་མ་གང་ལ་ཡོད་པ་དེ་ནི་གསེར་གྱི་འདབ་མ་ལྟར་མཛེས་པའི་འདབ་མའོ། །

[Block 3927]
གདོང་དང་རྐང་པ་གཉིས་མཛེས་པ་ནི་གདོང་དང་རྐང་པ་གཉིས་མཛེས་པ་སྟེ། གསེར་བཙོམ་བས་ཀྱང་ལྷག་པར་མཛེས་སོ། །

[Block 3928]
དེ་ཡང་ཚད་ལྷག་པ་དང་ལེགས་པའི་ལུས་ཅན་གང་ཡིན་པ་དེ་གཉིས་སོ། །

[Block 3929]
མཁས་པར་གྲགས་པ་གང་ཡིན་པ་དེ་ནི་དེ་གཉིས་གཟུང་བའི་ཕྱིར་རོ། །

[Block 3930]
ངང་པའི་མཆོག་དེ་གནས་དང་སྤྱོད་ཡུལ་ཞེས་བྱ་བ་ནི་གནས་པའི་ཕྱོགས་ས། །ཉེས་སུ་དོགས་པ་མེད་པ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། བྲིད་པའི་ཐབས་མཁས་པའི་ཕྱིར་རོ། །

[Block 3931]
བག་མེད་པ་ཉིད་བརླག་པ་ཡིན་པས་བག་མེད་བརླག༌[^2538]པའོ། །

[Block 3932]
དེ༌[^2539]བག་མེད༌[^2540]བརླག་པའི་འབྱུང་གནས་ཡིན་པས་ན་འབྱུང་ཁུང་ངོ་། །དེ་ལྟ་བུར་ཞེས་བྱ་བ་ནི་བཅིང་བའི་རྣམ་པར་རོ། །

[Block 3933]
འཇིགས་པ་དང་བཅས་པ་ཡིན་ནོ། །ཞེས་བྱ་བ་ནི་བདག་ཉིད་བཅིངས་སོ་ཞེས་བརྗོད་པའི་ཚིག་དེས་གཞན་མི་བདེ་བར་འགྱུར་བས་དེ་ལྟར་སྨྲས་པའོ། །

[Block 3934]
ཡང་ན་ཉམས་ཉེས༌[^2541]པར་གྱུར་པའི་ཚུལ་ཏེ། བདག་ཉིད་བཅིངས་སོ་ཞེས་བསྒྲགས་ན་ཡང་འདིར་ཉེས་པ་མེད་དོ། །

[Block 3935]
འཇིགས་པས་སྐྲག་ལ་བརྟབས་པ༌[^2542]གང་ཡིན་པ་དེ་ནི་འཇིགས་ཤིང་སྐྲག༌[^2543]ལ་བརྟབས༌[^2544]པའོ། །

[Block 3936]
བྱམས་པས་བཅིངས་པའི་ཡིད་ནི་རང་གི་སྲོག་དང་བྲལ་བ་ཡང་མི་སེམས་སོ། །གང་གི་ཕྱིར་ཞེ་ན། རང་གི་སྲོག་དང་བྲལ་བའི་སྡུག་བསྔལ་ནི་ཤིན་ཏུ་ཆེ་བ་ཡིན་མོད་ཀྱང་།[^2545] དེ་བས་ཀྱང་ཤིན་ཏུ་ཤས་ཆེ་བའི་སྡུག་བསྔལ་གྱིས་ཞེས་སྦྱར་ཏེ། མྱ་ངན་དང་སྡུག་བསྔལ་ནི་མྱ་ངན་དང་སྡུག་བསྔལ་ལ་ལོ། །

[Block 3937]
སྡུག་བསྔལ་ནི་ལུས་ཀྱིའོ། །

[Block 3938]
མྱ་ངན་སེམས་ཀྱི་སྟེ། དེ་དག་ནི་གང་གི་ཕྱིར་ཉམས་ཉེས༌[^2546]པས་བྱས་པའོ། །

[Block 3939]
སོང་ཤིག་སོང་ཤིག་ཅེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་བསྡུས་པའི་དོན་ནི་དེ་ལ་གནོད་པར་འགྱུར་བའི་ཕྱིར་དང་། བདག་གི་ཉམས་ཉེས༌[^2547]པའི་གྲོགས་མི༌[^2548]ནུས་པའི་ཕྱིར་རོ། །

[Block 3940]
ཇི་ལྟར་བཤད་པའི་རྒྱུ་དེ་གཉི་གའི་གནས་སྐབས་ཀྱང་མི་རིགས་པར་བསྟན་པའི་ཕྱིར། འདི་ན༌[^2549]མཆིས་ཀྱང་འགུམ་པར་ངེས་མ་མཆིས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3941]
སོང་ཤིག་སོང་ཤིག་ཅེས་བྱ་བའི་ཚིགས་བཅད་དེར་གང་བསྟན་པ། དེ་གཉིས་ཀྱི་ལན་བསྟན་པའི་ཕྱིར། འདི་ན་མཆིས་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་བསྟན་ཏེ།

[Block 3942]
འདི་ན་འདུག་པའི་མི་རིགས་སོ་ཞེས་བྱ་བའི་ལན་ནི་འདི་ན་མཆིས་པ་ལས།

[Block 3943]
གལ་ཏེ་གུད་དུ་མཆིས་ཀྱང་རྒ་ཤི་མེད་པར་འགྱུར་ན་འདི་ན༌[^2550]འདུག་པའི་མི་རིགས་ན་དེ་མེད་པས་སོ། །

[Block 3944]
སོང་ཅིག་ཅེས་བྱ་བའི་ལན་ནི་ངེས་མ་མཆིས་ཞེས་བྱ་བ་ཡིན་ཏེ། གལ་ཏེ་འགྲོ་བར་མི་འགྱུར་ན་གདོན་མི་ཟ་བར་གསོད་པ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟ་ན་ནི་སོང་ཤིག་ཅེས་སྨྲ་བའི་རིགས་ན་དེ་ཡང་མེད་དོ། །

[Block 3945]
གྲོགས་བྱར་ག་ལ་ཡོད་ཅེས་བྱ་བ་དེའི་ལན་ནི་བདེ་བའི་ཚེ་ན་རྟག་ཏུ་ཁྱོད་བཀུར་བ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 3946]
ང་ནི་འདི་ལྟར་གྱུར་པ་ལ་ཞེས་བྱ་བ་དེའི་ལན་ནི། ཉམས་ཉེས༌[^2551]ཚེ་ན་དོར་དུ་ག་ལ་རུང་། །ཞེས་བྱ་བའི་ཚིག་གིས་ཏེ། ཐ་མལ་པའི་ཚེ་ཡང་མ་བཏང་ན་འདི་ལྟར་གྱུར་པ་ནི༌[^2552]ལྟ་ཅིའི་ཕྱིར་དོར་ཞེས་པའོ། །

[Block 3947]
གལ་ཏེ་འདི་ན་མ་མཆིས་ཀྱང་འགུམ་པར་ངེས་པ་མ་མཆིས་པ་དང་། དེ་ལྟར་ཡོངས་སུ་བོར་ཞིང་བཏང་ན་ཡང་གཅིག་ཏུ་འཆི་བ་དང་། རྒ་བ་མེད་པ་ནི་མ་ཡིན་པར༌[^2553]འགྲོ་བར་ནི་མི་རིགས་པས་འདུག་པ་ནི་རིགས་པ་ཉིད་དེ་དེའི་ཕྱིར་སྨྲས་པ། བདག་གི་སྲོག་བཟུང༌[^2554]ཙམ་གྱི་ཕྱིར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3948]
བདག་ཉིད་ཀྱི་སྲོག་ཡིན་པས་བདག་གི་སྲོག་གོ། །

[Block 3949]
བདག་གི་སྲོག་ཉིད་གཟུང་བ་ཡིན་པས་བདག་གི་སྲོག་གཟུང་བའོ། །

[Block 3950]
དེ་ཙམ་ཉིད་ཡིན་པས་ན་བདག་གི་སྲོག་གཟུང་བ་ཙམ་མོ། །

[Block 3951]
དེས་ན་བདག་གི་སྲོག་གཟུང་བ༌[^2555]ཙམ་གྱི་ཕྱིར་ཏེ། རང་གི་སྲོག་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3952]
གཏམ་ངན་པ་ཡིན་པའི་ཕྱིར་གཏམ་ངན་ནོ། །

[Block 3953]
གཏམ་ངན་པ་ཉིད་ཆར་ཡིན་པས་གཏམ་ངན་པ་ཆར་བཞིན་དུ་འབབ་པའོ། །

[Block 3954]
དེའི་སྐྱབས་ནི་གཏམ་ངན་ཆར་བཞིན་འབབ་པའི་སྐྱབས་སོ། །

[Block 3955]
འདིར་སྒྲིབ་པར་བྱེད་པ་ཡིན་པས་སྐྱབས་ཏེ། འདིས་ནི་བདག་ཉིད་ཁྲེལ་ཡོད་པར་བསྟན་ཏོ། །

[Block 3956 [VERSE]]
རྒྱལ་པོ་ཆེན་པོ་ཉམས་ཉེས༌[^2556]པ། །
བོར་ཏེ་མཆི་བའི༌[^2557]ཆོས་མ་མཆིས། །

[Block 3957]
ཞེས་བྱ་བ་ནི་ངོ་ཚ་ཤེས་པའི་དབང་དུ་བྱས་པ་སྟེ། བདག་དང་ཆོས་ཀྱི་དབང་དུ་བྱས་ནས་ཁ་ན་མ་ཐོ་བ་ལ་འཛེམ༌[^2558]ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 3958]
བདེ་བའི་ཚེ་ན་རྟག་ཏུ་ཁྱོད་བཀུར་ལ། །ཉམས་ཉེས༌[^2559]ཚེ་ན་ཞེས་བྱ་བ་སྟེ། ཕོངས་པར་གྱུར་བ་ནི༌[^2560]བདག་གིས་བོར་ན་ག་ལ་ཞིག་རུང་སྟེ། སྨྲས་པ། ཁྱོད་ནི་ཅིར་གྱུར་པ་ཞེས་བྱ་བ་ཡིན་ཏེ།

[Block 3959]
དང་པོ་ཁྱོད་ཇི་ལྟར་གྱུར་པ་དེ་ལྟར་བདག་ཉིད་ཀྱང་འགྱུར་བར་འཚལ་ལོ་ཞེས་བྱ་བའོ། །

[Block 3960]
དེའི་ལན་བྱང་ཆུབ་སེམས་དཔས་སྨྲས་པ། ཚང་མང་ཞེས་བྱ་བས་ནི་ངེས་པར་གསོད་པར་འགྱུར་བའི་དོན་ཏོ། །
--- END BLOCKS ---
