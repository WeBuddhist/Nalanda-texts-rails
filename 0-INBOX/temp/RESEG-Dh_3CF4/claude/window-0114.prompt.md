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
[Block 3991]
ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་ཕྱེད་དོ། །

[Block 3992]
དེ་བས་ཁྱོད་ནི་ཅི་བདེར་སོང་། །ཞེས་བྱ་བའི་ལན་ནི།

[Block 3993 [VERSE]]
གལ་ཏེ་གཅིག་གིས་མཉེས་གྱུར་ན། །
ཞེས་བྱ་བ་ཕྱེད་འོག་མ་ཡིན་ནོ། །
གལ་ཏེ་གཅིག་གིས་མཉེས་གྱུར་ན། །

[Block 3994]
ཞེས་བྱ་བ་ལ། འདི་བློ་དང་ན་ཚོད་ལ་སོགས་པ་མི་མཉམ་པ་དེ་ཁྱད་པར་ཡོད་དོ་ཞེས་རྟོག་པ་ལ། དེ་ཁྱད་པར་མེད་པར་བསྟན་པའི་ཕྱིར། བདག་ཅག་ཆུ་དང་ཞེང་ཡང་མཉམ། །ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3995]
ཆུ་དང་ཞེང་རྣམ་པ་གཉིས་ཀྱིས་ནི་བྱེ་བྲག་མེད་པ་སྟོན་ཏེ། [^2579]དེ་ཁྱད་པར་མེད་པས་སེམས་ཀྱང་ཁྱད་པར་མེད་དོ། །

[Block 3996]
གལ་ཏེ་ན་ཚོད་ལ་ཁྱད་པར་ཡོད་ན་ནི་ཤ་ལ་ཁྱད་པར་ཡོད་པར་འགྱུར་ཏེ། དེ་ཁྱད་པར་མེད་པར་བསྟན་པའི་ཕྱིར། ན་ཚོད་ལ་ཡང་རྒན་གཞོན་མེད། །ཅེས་བྱ་བ་འདིས་སོ། །

[Block 3997]
བདག་ལ་ཐུགས་ཆེས་མི་འགྱུར་ན། །[^2580]ཞེས་བྱ་བར་བཤད་པ་ནི་ཅི་ཞིག་ལྟར་དོགས་ན་དེ་ཡང་ཉེས་པ་མེད་དེ། གལ་ཏེ་སྔར་བྱའི་རྒྱལ་པོ་བཏང་སྟེ། བདག་ཀྱང་མ་བཟུང་བར་བཏང་ན་ནི་གཉི་ག་ལས་ཉམས་པར་འགྱུར་ན། དེའི་ཉེས་པ་མེད་པར་བྱ་བའི་ཕྱིར། ཁྱོད་ཀྱིས་བདག་ནི་སྔར་ཟུང་ལ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་འོག་མའོ། །

[Block 3998]
བདག་བཟུང་ཞིང་བྱའི་རྒྱལ་པོ་བཏང་ན་ནི་ཕན་ཡོན་འདི་དག་ཡིན་ཏེ། དེ་བསྟན་པའི་ཕྱིར།

[Block 3999 [VERSE]]
ཁྱོད་ཀྱི༌[^2581]རྙེད་པའང་དེ་བཞིན་ལ། །
ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ།
ཁྱོད་ཀྱི༌[^2582]རྙེད་པའང་དེ་བཞིན་ནོ། །
[^2583]དེ་བས་མཛའ་བོའང༌[^2584]དེ་བཞིན་འགྱུར། །

[Block 4000]
ཞེས་བྱ་བ་འདི་གཉིས་ཀྱིས་རྔོན་པའི་ཕན་ཡོན་བསྟན་ཏོ། །

[Block 4001]
བདག་གིས་གསོལ་བ་ཞེས་བྱ་བ་དག་དང་། ཁྱོད་ཀྱིས་བཏང་ནའང༌[^2585]ཇི་ལྟར་འགྱུར་བ་གཟིགས། །ཞེས་བྱ་བ་འདིས་ངང་པའི་རྒྱལ་པོའི་ཕན་ཡོན་བསྟན་པའོ། །

[Block 4002]
དེ་རང་གི་སྲོག་ལ་ཡང་མི་ལྟ་བར་ཞེས་བྱ་བས་ནི་གང་སྔར་བཤད་པའི།

[Block 4003 [VERSE]]
དེ་བས་བདག་གི་སྲོག་ནི་ཡལ་གྱུར་ཀྱང་། །
འདི་ནི་གཏོང་བར་བདག་གིས་མི་ནུས་སོ། །

[Block 4004]
ཞེས་བྱ་བ་དེ་བསྟན་པ་ཡིན་ནོ། །

[Block 4005]
ཇོ་བོ་ལ་སྙིང་ཉེ་ཞིང་བྱམས་པ་ཞེས་བྱ་བ་འདིས་ནི་གང་སྔར་བསྟན་པའི། ང་ཡི་རྒྱལ་པོ་སྲོག་དང་འདྲ་བའི་གྲོགས། །འདི་ནི་ཉམས་ཉེས༌[^2586]གྱུར་ཅེས་བྱ་བ་དེ་སྟོན་པ་ཡིན་ནོ། །

[Block 4006]
གང༌[^2587]ཆུ་གང་དང་ཁྲེལ་ལྟས་ཆེ་བའི་ཡོན་ཏན་གྱི་གཟི༌[^2588]བྱིན༌[^2589]དང་ཞེས་བྱ་བ་འདིས་ནི་བདེ་བ་སྦྱིན་པ་འདི༌[^2590]ནི་ཉམས་ཉེས༌[^2591]གྱུར་ཞེས་བྱ་བ་དེ་སྟོན་ཏོ། །

[Block 4007]
བརྟན་པའི་རྒྱན་གྱིས༌[^2592]བརྒྱན་ཅེས་བྱ་བ་འདིས་ནི་གང་སྔར་བཤད་པའི། བདག་ནི་སྡུག་བསྔལ་མི་བཞེད་ན། །ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་དག་སྟོན་པ་ཡིན་ནོ། །

[Block 4008]
འཇམ་པའི་རྒྱན་གྱིས་བརྒྱན་ཅེས་བྱ་བ་འདིས་ནི། བཟང་པོ་བདག་ཅག་སྨྲས་པ་འདིས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་དོན་དེ་སྟོན་ཏོ། །

[Block 4009]
ངོ་མཚར་ཆེ་ཞིང་རབ་ཏུ་གུས་པའི་དབང་གིས་ཞེས་བྱ་བ་ནི་དུད་འགྲོའི་སྐྱེ་གནས་སུ་གྱུར་པ་ཡིན་དུ་ཟིན་ཀྱང་། དེའི་ཡོན་ཏན་ལ་ངོ་མཚར་ཆེ་བས་གུས་པ་ཡིན་ཏེ། ཡོན་ཏན་ཁྱད་པར་དུ་གྱུར་པ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 4010]
ངོ་མཚར་དང་གུས་པ་གཉིས་བསྟན་པའི་ཕྱིར། ཇོ་བོའི་དོན་དུ་སྲོག་བཏང་བ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་སྨོས་སོ། །

[Block 4011]
སྙིང་རྗེ་ཅན་ཞེས་བྱ་བ་སྙིང་རྗེ་དང་ལྡན་པ་ཡིན་པས་སྙིང་རྗེ་ཅན་ཏེ། སྡུག་བསྔལ་དང་བྲལ་བ་དེ་དེས་དོན་དུ་གཉེར་བའི་སྙིང་རྗེའི་ཡོན་ཏན་སྟོན་པའོ། །

[Block 4012]
ཁྱོད་ཀྱིས་ལས་བྱས་དོན་མེད་མི་འགྱུར་ཕྱིར། །ཞེས་བྱ་བས་ནི། ཇི་ལྟར་བདག་དགའ་བར་འགྱུར་བར་ལས་བྱས་པ་ནི་ངང་པའི་རྒྱལ་པོ་ཁྱོད་ཀྱིས་བཏང་བ་སྟེ། དེའི་འབྲས་བུ་མེད་པར་མི་འགྱུར་བའོ། །

[Block 4013]
བདེ་བར་ཞེས་བྱ་བ་ནི་བག་ཚ་བ་མེད་པར་རོ། །

[Block 4014]
ཕོ་བྲང་ནང་དུ་རྒྱལ་པོའི་སྤྱན་སྔར་བྲིམས། །ཞེས་བྱ་བ་ནི་དབེན་པར་བསྟན་པ་མི་འདོད་ཅིང་ཕོ་བྲང་གི༌[^2593]ནང་དུ་འོས་པ༌[^2594]སྟེ། བདག་ཉིད་སྐྱེ་བོ་མང་པོའི་མངོན་དུ་བསྟན་པ་ནི་རང་གི་རིགས་པ་དང་མཐུན་པའི་ཕྱིར་རོ། །

[Block 4015]
མིའི༌[^2595]གཡོག་བཞིན་དུ་གཡོག་དང་བཅས་པའི་མཚན་ཉིད་དོ། །

[Block 4016]
མི་རེ་བ་དག་གང་ཡིན་པ་དེ་ནི། རེ་ཡང་མི་རེ་བ་དག་སྟེ་ཆེ་ཞིང་རྒྱ་ཆེ་བ་དག་གོ། །

[Block 4017]
མགུ་བར་འགྱུར་བ་ཞེས་བྱ་བ་འདིས་ནི་ཡིད་ལ་ཅི་འདོད་པ་ཉིད་སྟོན་ཏོ། །

[Block 4018]
བདེ་ཞིང་ཞེས་བྱ་བ་འདིས་ནི་འཇིགས་པ་མེད་པར་རོ། །

[Block 4019]
བྱ་འདི་གཉིས་ནི་ཞེས་བྱ་བས་ནི་ས་ལ་འགྲོ་བའི་སྤྱོད་ཡུལ་མ་ཡིན་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4020]
རབ་ཏུ་དགའ་ཞིང་ངོ་མཚར་ཆེ་བ་ཞེས་བྱ་བ་ནི་དགའ་བ་དང་། ངོ་མཚར་དུ་གྱུར་པ་གཉིས་ནི་དགའ་བ་དང་། ངོ་མཚར་རོ། །

[Block 4021]
དེ་ལ་རབ་ཏུ་དགའ་བ་ནི་འདོད་པའི་དོན་འགྲུབ༌[^2596]པས་སོ། །

[Block 4022]
ངོ་མཚར་ཆེར་གྱུར་པ་གཉིས་ནི་ཤིན་ཏུ་རྙེད་པར་དཀའ་བ་རྙེད་པའི་ཕྱིར་རོ། །

[Block 4023]
སྣ་ཚོགས་པའི་རིན་པོ་ཆེ་ནི་རིན་པོ་ཆེ་སྣ་ཚོགས་པའོ།[^2597] །རིན་པོ་ཆེ་སྣ་ཚོགས་པའི་འོད་ནི་འོད་ཟེར་ཏེ། [^2598]འོད་ཟེར་འཕྲོ་ཞིང་སྡུག་པའི་རྐང་པ་གང་ཡིན་པའི་སྟན་ནི་སྟན་དེའོ། །

[Block 4024]
སྤྲས་པ༌[^2599]ནི་གསལ་བར་བྱེད༌[^2600]པའོ། །

[Block 4025]
འོད་ཟེར་འཕྲོ་ཞིང་སྡུག་པ་ཞེས་བྱ་བ་ནི་དབྱིབས་སོ། །

[Block 4026]
ལྷའི་གདན་ཡང་ཡིན་པས་ལྷའི་གདན་རིམ་པ་དུ་མའོ། །

[Block 4027]
དེ་བཤམས་པ་ནི་ལྷའི་གདན་རིམ་པ་དུ་མར་བཤམས་པ་སྟེ། དེས་མངོན་པར་དགའ་བར་བྱ་བ་གང་ཡིན་པ་དེ་ནི་ལྷའི་གདན་རིམ་པ་དུ་མར་བཤམས་ཤིང་བཟང་བའོ། །

[Block 4028]
རྒྱབ་རྟེན་དང་བདེ་ཞིང་ཉམས་དགའ་བ་ནི་རྒྱབ་རྟེན་བདེ་ཞིང་ཉམས་དགའ་བའོ། །

[Block 4029]
བརྒྱན་པ་དང་བཅས་པ་ནི་རྒྱབ་རྟེན་བདེ་ཞིང་ཉམས་དགའ་བས་བརྒྱན་པའོ། །

[Block 4030]
བཙུགས་པའི་རྐང་རྟེན་གང་ཡིན་པ་འདི༌[^2601]ནི་རྐང་རྟེན་བཙུགས་པའོ། །
--- END BLOCKS ---
