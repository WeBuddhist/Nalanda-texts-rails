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
[Block 5601]
མདོག་ཅུང་ཟད་དམར་ཞིང་སྣུམ་པ་གང་ཡིན་པ་དེ་ནི།

[Block 5602 [VERSE]]
སྣ་མདོག་ཅུང་ཟད་དམར་ཞིང་སྣུམ་པའོ། །
རྡུལ་དང་ཉི་མའི་འོད་ཟེར་ནི། །
རྡུལ་དང་ཉི་མའི་འོད་ཟེར་རོ། །

[Block 5603]
དེས་རེག་པ༌[^3565]ནི་རྡུལ་དང་ཉི་མའི་འོད་ཟེར་གྱིས་རེག་པ་སྟེ་དེ་བས་ནའོ། །

[Block 5604]
ཁ་དོག་མ་རུང་པ་གང་ཡིན་པ་དེ་ནི་ཁ་དོག་ཉམས་པའོ། །

[Block 5605]
རིད་པ་སྟེ། ཅིའི་ཕྱིར་རིད་པ་ཡིན་ཞེ་ན། དེ་ཉིད་སྨྲས་པ། མྱ་ངན་གདུངས་ཕོངས་ཞེས་བྱ་བ་ལ་མྱ་ངན༌[^3566]ནི་སེམས་ཀྱི་སྡུག་བསྔལ་ལོ། །

[Block 5606]
གདུངས་ཕོངས༌[^3567]ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་སྡུག་བསྔལ་ཏེ། དེ་གཉིས་ཀྱིས་རིད་པར་གྱུར་པའོ། །

[Block 5607]
མིའི་སྐད་དུ་སྨྲ་ཞིང་ཞེས་བྱ་བ་ནི། ཨ་ལ་སོགས་པའི་ཡི་གེའི༌[^3568]ཁྱད་པར་གྱིས་སོ། །

[Block 5608]
མི་འཇིགས་པའི་སྦྱིན་པར་ཁས་ལེན་པ་ཞེས་བྱ་བ་ནི་ང་ལས་ཁྱེད་འཇིགས་པ༌[^3569]མི་འབྱུང་གི་མ་འཇིགས་ཤིག༌[^3570]མ་འཇིགས་ཤིག་ཅེས་བྱ་བའི་ཚིག་གོ།[^3571] །དགའ་བར་བྱེད་པ་ཞེས་བྱ་བ་ནི་ཁྱེད་ཅག་སུ་ཞིག །ཅིའི་ཕྱིར་འདི་ལྟར་གྱུར་ཅིང་འདི་ན་འཁོད། །ཅེས་བྱ་བ་ལ་སོགས་པ་གང་ཡིན་པ༌[^3572]དེ་ཉིད་དེ། ཚིག་འདི་གཉིས་ཀྱིས་དོན་བསྟན་པའོ། །

[Block 5609]
ཁྲོས་པའི་རླུང་ལངས་ཞེས་བྱ་བ་ནི༌[^3573]བདག་ཉིད་ལ་སྐྱོན་མེད་པར་རྒྱལ་པོས་སྤྱུགས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5610]
སྐལ་བ་ལྷག་མ་ཞེས་བྱ་བ་འདིས་ནི་བདག་ཉིད་འཚོ་བ་ཉིད་དུ་རེ་བའོ། །

[Block 5611]
ལྷ་དཔལ་མངོན་དུ་ཞེས་བྱ་བ་ནི་དེ་མཐོང་བས་བདག་ཉིད་དགའ་བ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5612]
[^3574]བཤེས་པས་ཀྱང་ལྷག་པ་མཐོང་བའི་ཕྱིར། སྐལ་བ་ལྷག་མ་ཡོད་པའོ། །

[Block 5613]
གཉེན་པས་ཀྱང་ལྷག་པ༌[^3575]མཐོང་བའི་ཕྱིར་ནི། ལྷ་དཔལ་མངོན་དུ་གྱུར་པའོ། །

[Block 5614]
ཕོངས་པ་འདི་ལས་ཞེས་བྱ་བ་ནི་འབྲོག་དགོན་པ་ན་སྡུག་བསྔལ་ཞིང་ཕོངས༌[^3576]པའོ། །

[Block 5615]
སྙིང་རྗེ་མེད་ཅིང་ཞེས་བྱ་བ་ནི་སྙིང་རྗེ༌[^3577]དང་མི་ལྡན་པའོ། །

[Block 5616]
འཛེམ་པ་མེད་པ༌[^3578]ནི་ཁྲེལ་མེད་པ་སྟེ། འཇིག་རྟེན་གྱི་བརྗོད་པ་ལ་མི་ལྟ་བའོ། །

[Block 5617]
ཕྱི་ཚེ་མི་སེམས་ཤིང་ཞེས་བྱ་བ་འདིས་ནི་བདག་ཉིད་ལ་ལྟོས་པ༌[^3579]ཉིད་དུ་སྟོན་པའོ།[^3580] །

[Block 5618]
ངན་སོང་དུ་འགྲོ་བར་མི་སེམས་པའི་ཕྱིར། རང་ལ་ཕན་པ་ལ་མི་ལྟ་བ་སྟེ། འདིས་ནི་མངོན་པར་མཐོ་བ་དང་། ངེས་པར་ལེགས་པ་ཡོད་པའི་མཚན་ཉིད་དག་ལ་ཕན་པ་ལ་མི་སེམས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5619]
བདག་ལ་ཕན་པ་ལ་མི་ལྟ་ཞིང་། ཚེ་ཕྱི་མ་ལ་མི་སེམས་པའི་རྒྱུའི་དབང་དུ་བྱས་ནས། སྨྲས་པ། རྒྱལ་པོའི་དཔལ་གློག་ལྟར་མི་བརྟན་པ་དང་དབང་པོ་ཕྲོགས་པའི་ཕྱིར་རོ། །

[Block 5620]
ཡང་ན་སྙིང་རྗེ་མེད་ཅིང་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^3581]བཞིའི་རྒྱུ་བསྟན་པ་ཡིན་ཏེ། རྒྱལ་བའི༌[^3582]དཔལ་མི་བརྟན་པ་དང་། དབང་པོ་ཕྲོགས་པའི་ཕྱིར་རོ། །

[Block 5621]
ཡང་ན་རང་ལ་ཕན་པ་ལ་ལྟོས་པ༌[^3583]མེད་ཀྱི༌[^3584]རྒྱུ་ནི་རྒྱལ་པོའི་དཔལ་མི་བརྟན་པས་དབང་པོ་ཕྲོགས་པའི་ཕྱིར་རོ། །

[Block 5622]
གཞན་གསུམ་ནི་སྙིང་རྗེ་མེད་ཅིང་མི་འཛེམ་པ་དང་། ཚེ་ཕྱི་མ་མི་སེམས་པ་ལ་སོགས་པའོ། །

[Block 5623]
འཆི་བདག་དེའུ་རེ་འོང་བར་དེ་མི་སེམས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གཉིས་ཀྱིས་བསྟན་ཏེ། འཆི་བདག་དེའུ་རེ་འོང་བར་དེ་མི་སེམས་ཞེས་བྱ་བ་འདི༌[^3585]ཚིགས༌[^3586]བཅད་ཀྱི་དང་པོ་ཕྱེད་ཀྱིས་ནི། ཚེ་ཕྱི་མ་ལ་མི་སེམས་པའི་རྒྱུ་གཉིས་ཡིན་ཏེ། ཚེ་ཕྱི་མ་མི་སེམས་པའི་བློ་ཡོད་པར་མི་འགྱུར་བ་ནི། འཆི་བ་ཉེ་བར་གནས་པ༌[^3587]མཐོང་བའི་ཕྱིར་དང་། འཆི་བ་ཡོད་ཀྱང་སྡིག་པ་ཡོད་པར་མི་ཤེས་པའམ། མ་ཐོས༌[^3588]པའོ། །

[Block 5624]
འཛེམ་པ་མེད་པའི་རྒྱུ་བསྟན་པ་ནི་ཚིགས་བཅད་ཕྱེད་འོག་མ༌[^3589]ཡིན་ཏེ། གཉི་གའི་རྒྱུས་ཀྱང་འཛེམ་པ་མེད་པ་སྟེ། ཕན་པར་སྟོན་པའི་དགེ་བའི་བཤེས་གཉེན་མེད་པའི་ཕྱིར། རྣམ་རྟོག་ཞེན་པས་གདམས་སུ་མེད་པའམ། མགོན་མེད་པར་གྱུར་པས༌[^3590]སོ། །

[Block 5625]
སྙིང་རྗེ་མེད་པའི་རྒྱུ་བསྟན་པའི་ཕྱིར། ནད་ཀྱི་གཞིར༌[^3591]གྱུར་ཅེས་བྱ་བ་སྨོས་ཏེ། ལུས་ཞེས་བྱ་བ་འདིས་ནི་མི༌[^3592]གཙང་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5626]
གཅིག་པུ་ཞེས་བྱ་བ་འདིས་ནི་བདག་པོ་དང་བྲལ་བའི་ཕྱིར་བདག་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5627]
ནད་ཅེས་བྱ་བ་ནི་སྡུག་བསྔལ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5628]
ཆུད་ཟ་བའི་ཞེས་བྱ་བ་འདིས་ནི་མི་རྟག་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5629]
ཀྱི་ཧུད་གཏི་མུག་ཅེས་བྱ་བ་འདིས་ནི་མ་རིག་པས༌[^3593]ཉེ་བར་བཅོམ་པ་སྟེ། ཟིལ་གྱིས་མནན་པ༌[^3594]ཉིད་དུ་སྟོན་ཏེ། སེམས་ཅན་རྣམས་ནི་ཕྱིན་ཅི་ལོག་རྣམ་པ་བཞིས་ཕྱིན་ཅི་ལོག་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5630]
ནད་མང་བརྒྱའི་གནས་ཞེས་བྱ་བས༌[^3595]ནི་གང་གི་སྡུག་བསྔལ་དང་ལྡན་པ་བསྟན་ཏོ། །

[Block 5631]
ལུས་འདི་སྡུག་བསྔལ་ཉམ་ཐག་པ། །ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་གྱིས་ཉམ་ཐག་པ་གཞན་དག་གོ། །

[Block 5632]
འདི་རྣམས་ཕོངས༌[^3596]ལས་བསྒྲལ་བའི་གཟེངས་གྱུར་པ། །ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་ལས་བསྒྲལ་བའི་གཟིངས་ཏེ། སྡུག་བསྔལ་གྱི་ལུས་ཀྱི་རྒྱུས་གཞན་སྡུག་བསྔལ་ལས་བསྒྲལ་བས་འབྲས་བུ་དང་བཅས་པ་ཉིད་དུ་བྱའོ་ཞེས་བྱ་སྟེ། དེས་ན་བྱང་ཆུབ་སེམས་དཔའི་ལུས་སྡུག་བསྔལ་མང་པོའི་གནས་ཡིན་པ་དེ་བཞིན་དུ་འདི་དག་གི༌[^3597]ལུས་ཀྱང་ཡིན་ནོ། །

[Block 5633]
ཅིའི་ཕྱིར་ལུས་འདི་བསྒྲལ་བའི་གཟིངས་སུ་གྱུར་པ་ཞེས་བྱ་བའི་རྒོལ་བའི་སྐབས་ཤེས་པར་བྱས་ནས། རང་དང་གཞན་གྱི་ལུས་ཀྱི་ཁྱད་པར་བརྫུན་པའི༌[^3598]ཕྱིར། མི་ཡི་ལུས་སུ་སྐྱེས་པ་ཡིས། །ཞེས༌[^3599]བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5634]
མཐོ་རིས་ཐར་པའི་བདེ་བ་ཐོབ་པར་ནུས་པ་ཞེས་བྱ་བ་འདིས་ནི་མིའི་ལུས་ཀྱིས་མངོན་པར་མཐོ་བ་དང་། ངེས་པར་ལེགས་པ༌[^3600]ཐོབ་པར་ནུས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5635]
བདག་གི་མཐོང་བའི་ཆོས་ཀྱི་ལུས་ཀྱིས་ནི་མི་ནུས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5636]
འདི་ལྟར་གྱུར་པ་ལ་ཕན་འདོགས་པ་ཡང་ཤིན་ཏུ་དཀོན་ཞེས་བྱ་བ་ལ་འདི་དག་ཅེས་བྱ་བ་ནི་མི་སྐྱེ་བའོ། །

[Block 5637]
འདི་ལྟར་ཞེས་བྱ་བ་ནི་ད་ལྟར་བྱུང་བའི་དགེ་བ་དེས་མེད་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5638]
བདག་ནི་རྙེད་པར་བླ་བ༌[^3601]སྟེ། མིའི་སྐྱེ་བ་ལ་བསོད་ནམས་ཀྱི་ཚོགས་ལ༌[^3602]གོམས་པར་བྱས་པས་སྐྱེ་བ་གཞན་གྱི་རྒྱུ་བསྟན་པའི་ཕྱིར། བདག་གི་སྤྱོད་ཡུལ་གནས་སུ་ལྷགས་པར་གྱུར། །ཅེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5639]
[^3603]འདི་འདྲའི་མགྲོན་ཀྱང༌[^3604]བསོད་ནམས་བྱས་པས་འཐོབ། །ཅེས་བྱའོ།[^3605] །གལ་ཏེ་བདག་གིས་བོས་ཏེ། འདིར་འོངས་པ་མ་ཡིན་ན་ཡང་བསོད་ནམས་བྱས་པས་འཐོབ་ཅེས་བྱ་བ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། སྤྱོད་ཡུལ་གནས་སུ་ལྷགས་པར་གྱུར་པའི་ཕྱིར་ཏེ། རང་གིས་དོན་དུ་གཉེར་བ་ཉིད༌[^3606]བསྟན་ཏོ། །

[Block 5640]
ཕོངས་ཤིང་ཉམ་ཐག་གྱུར་ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་བ་ཉིད་དོ། །
--- END BLOCKS ---
