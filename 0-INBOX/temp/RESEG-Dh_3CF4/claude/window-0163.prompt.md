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
[Block 5706]
དེ་ལྟར་རེ་ཞིག་བྱང་ཆུབ་སེམས་དཔའ་ལས་རྗེས་སུ་མ་བླངས་ན་རིགས་པ་མ་ཡིན་པ་ཉིད་དུ་བསྟན་ནས། ད་ནི་བདག་ཅག་ཉིད་ཀྱིས་མ་བླངས་པ་མི་མཐུན་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར།

[Block 5707 [VERSE]]
འདི་ཡིས་བྱས་ཏེ་ཅི་བདོག་པ། །
ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ།
གཞན་དུ་བྱས་ན་དོན་མེད་འགྱུར། །

[Block 5708]
ཞེས་བྱ་བ་འདི༌[^3646]དོན་མེད་པ་ཉིད་དུ་བསྒྲུབ༌[^3647]པའི་ཕྱིར། [^3648]བྱམས་པ་ཞེས་བྱ་བ་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 5709]
ཅི་བདོག་པ་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 5710]
བདོག་པ་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་སྦྱིན་པར་བྱ་བའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 5711]
བདག་ཅག་རྣམས་ཀྱིས་མ་བླངས་ན་དོན་མེད་པར་འགྱུར་བའི་ཕྱིར། བདག་ཅག་རྣམས་ཀྱིས་མ་བླངས་ནའོ། །

[Block 5712]
དེ་གང་ཡིན་ཞེ་ན། དེ་ནི་མགྲོན་ནོ། །

[Block 5713]
དེ་ལས་ཅི་ཞིག་བཀུར་སྟི་བྱ། །ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་མེ་ལ་སྦྱང་བ་དེས་བུ་ལོན་མེད་པ་སྟེ། དེས་མེས་མ་བསྲེགས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5714]
གལ་ཏེ་མ་བླངས་པ་དང་། མེ་ལ་སྦྱངས་པས་མ་བསྲེགས་ན། །དེ་ལྟར༌[^3649]ན་བཀུར་སྟི་ཅི་ཞིག་བྱས་པ་ཡིན་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར། དེ་བས་དེ་ལ་བླ་མ་བཞིན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5715]
དེ་བས་ན་ཞེས་བྱ་བ་ནི་མ་བླངས་ཤིང་དོན་མེད་པ་དེས་མགྲོན་གྱི་བསྙེན་བཀུར་མེད་པའི་ཕྱིར། དེ་ལས་གཞན་པ་དེའི་ཚིག་ཉན་པར་བྱས་ན་བཀུར་སྟི་ཉིད་དུ་བསྟན་པར་འགྱུར་རོ། །

[Block 5716]
བཀུར་སྟི་ཆེན་པོ་བྱ་བ་ཙམ་དུ་མ་ཟད་དེ། དེ་བདག་ལ་ཕན་པར་འགྱུར་བའི་ཕྱིར་ཡང་བཀུར་སྟི་ཆེན་པོ་བྱ་བའི་རིགས་ཏེ། དེའི་ཚིག་མཉན་པར་བྱ་བས་སོ། །

[Block 5717]
གལ་ཏེ་ཁྱེད་ཅག་གིས་དེ་ལ་བྱས་པ་གཟོ་བའི་ཕྱིར། དེ་ལ་མཆོད་པ་བྱས་ན་ཡང་དེ་བཞིན་དུ་བྱ་ཞིང་མངོན་པར་མཆོད་པའི་ཆོ་གའི་ཐབས་བསྟན་པའི་ཕྱིར། སྡུག་བསྔལ་འདི་ལས་ཐར་ནས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། སྡུག་བསྔལ་འདི་ལས་ཐར་པ་ཞེས་བྱ་བ་ནི་འབྲོག་དགོན་པ་འདིའི་སྡུག་བསྔལ་ལས༌[^3650]ཐར་པའོ། །

[Block 5718]
ཚོགས་པ་ནི་འདུས་པར་གྱུར་པའོ།[^3651] །དེ་དག་གི་ཚིག་ནི་དེ་དག་གི་ཚིག་གོ། །

[Block 5719]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་གླང་པོ་ཆེའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 5720 [HEADING]]
## སྐྱེས་པའི་རབས་བཅུ་པོ་འདི་དག་གི་གོ་རིམས། ^33-0

[Block 5721]
སྡོམ་ལ།

[Block 5722 [VERSE]]
བྱང་ཆུབ་ངང་པ་བྱང་ཆུབ་ཆེ། །
སྤྲེའུ་དང༌[^3652]རི་དྭགས་ཤ་ར་བྷ། །
རུ་རུ་སྤྲེའུ་རྒྱལ་བཟོད་པ་སྨྲ། །
ཚངས་དང་གླང་ཆེན་དེ་དག་བཅུ། །

[Block 5723]
སྡོམ་འདི་ནི་འཇིག་རྟེན་དུ་གྲགས་པ་ཡིན་ཏེ། སྐྱེས་པའི་རབས་བཅུ་པོ་འདི་དག་གི་གོ་རིམས་བདག་གིས་ནི་འདི་ལྟར་མཐོང་ངོ་། །

[Block 5724 [VERSE]]
བྱང་ཆུབ་ངང་པ་བྱང་ཆུབ་ཆེ། །
ཤ་ར་རུ་རུ་སྤྲེའུ་དང་། །
བཟོད་པ་སྨྲ་དང་སྤྲེའུ་རྒྱལ་དང་། །
གླང་ཆེན་ཚངས་པ་དེ་དག་བཅུ། །

[Block 5725]
འདིར་སྐྱེས་པའི་རབས་བཅུ་པོ་འདི་དག་གི་གོ་རིམས་ཀྱི་རྒྱུ་ཡང་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དབང་དུ་བྱས་པ་སྟེ། གཞན་གྱིས༌[^3653]གནོད་པ་བྱས་པ་ལ་མི་མཇེད་པའི༌[^3654]བཟོད་པ་དང་། སྡུག་བསྔལ་ལ་ཇི་མི་སྙམ་པའི་བཟོད་པ་དང་། ཆོས་ལ་ངེས་པར་སེམས་པའི་བཟོད་པའོ། །

[Block 5726]
དེ་ལ་ཆོས་ལ་ངེས་པར་སེམས་པའི་བཟོད་པའི་དབང་དུ་བྱས་ནས། ཚངས་པའི་སྐྱེས་པའི་རབས་ཡིན་ཏེ། ཆོས་ལ་ངེས་པར་སེམས་པའི་བཟོད་པ་ནི་ཟབ་ཅིང་རྒྱ་ཆེ་བའི་ཆོས་དག་ལ་འདོད་ཅིང་མི་སྐྲག་པའོ། །

[Block 5727]
བཟོད་པ་དེ་ཡང་བྱང་ཆུབ་སེམས་དཔའ་ལ་ཡོད་པ་ཡིན་ནོ་ཞེས་ཇི་ལྟར་ཤེས་པར་བྱ་ཞེ་ན། བདག་ཉིད་མངོན་པར་འདོད་པའི་ལྟ་བ་དེ་ལ་གཞན་ཡང་རབ་ཏུ་འགོད་པ་ཡིན་པའི་ཕྱིར། ཆོས་ལ་ངེས་པར་སེམས་པའི་བཟོད་པ་དེ་ནི་ཚངས་པའི་སྐྱེས་པའི་རབས་ཀྱིས་བརྗོད་པ་ཡིན་ནོ། །

[Block 5728]
གཞན་དུ་ན་ཇི་ལྟར་སྐྱེས་པའི་རབས་འདི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྐྱེས་པའི་རབས་སུ་བཤད། གལ་ཏེ་འདི་ལྟར་བློ་སྐྱེ་བར་འགྱུར་ཏེ། སྐྱེས་པའི་རབས་དེ་ཉིད་དུ་བསྟན་པའི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། མཚན་ཉིད་དུ་བཤད་པའི་སྐྱེས་པའི་རབས་འདི་ནི་རིགས་པ་ཡིན་ནོ་ཞེ་ན། དེ་ཡང་མི་རིགས་པ་ཉིད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། བཟོད་པ་གོང་ནས་གོང་དུ་ཁྱད་པར་དུ་བསྟན་པའི་སྐྱེས་པའི་རབས་ཀྱི་གོ་རིམས་རྣམ་པར་གཞག་པའི་ཕྱིར་ཏེ། བཟོད་པའི་ཚིག་དེ་ནི་ཞར་ལས༌[^3655]བྱུང་བའི་ཕྱིར་རོ། །

[Block 5729]
གཙོར༌[^3656]ནི་རང་བཞིན་གྱིས་ལྟ་བ་ངན་པ་ལ་ཞེན་པར་གྱུར་པ༌[^3657]ལ་ལྷག་པར་སྙིང་བརྩེ་བ༌[^3658]ཡིན་ཏེ། དེ་བས་ན་ཚངས་པའི་སྐྱེས་པའི་རབས་ནི་ཆོས་ལ་ངེས་པར་སེམས་པའི་དབང་དུ་བྱས་པ་ཉིད་དོ། །

[Block 5730]
སྤྲེའུའི་རྒྱལ་པོ་དང་། གླང་པོ་ཆེའི་སྐྱེས་པའི་རབས་སུ་ནི་སྡུག་བསྔལ་ལ་ཇི་མི་སྙམ་པའི་བཟོད་པའི་དབང་དུ་བྱས་པའོ། །

[Block 5731]
གཉིས་པོ་དེ་དག་ལས་ཀྱང་གནོད་པར་གྱུར་པའི་སྡུག་བསྔལ་ལ་ཇི་མི་སྙམ་པའི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དབང་དུ་བྱས་པ་ནི་སྤྲེའུ༌[^3659]རྒྱལ་པོའི་སྐྱེས་པའི་རབས་སུ་བསྟན་ཏེ་མི་བཟོད་པ་མེད་པའི་ཕྱིར་བཟོད་པའི་དབང་དུ་བྱས་པ་སྟེ། གནོད་པར་བྱེད་པའི་རྒྱལ་པོ་ལ་བཟོད་པར་བྱ་བ་ནི། འབྲེལ་པ་མེད་པའི་ཕྱིར་དང་། རྒྱལ་པོ་ཉིད་ཀྱང་ཕན་པ་བྱེད་པར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 5732]
གླང་པོ་ཆེའི་སྐྱེས་པའི་རབས་སུ་ནི་གཡང་ས་ནས་ལྟུང་བའི་སྡུག་བསྔལ་དང་། འཆི་བའི་སྡུག་བསྔལ་ལ་ཇི་མི་སྙམ་པའི་དབང་དུ་བྱས་པ་སྟེ། མ་འདྲིས་པའི་སྐྱེ་བོ་ལ་རྗེས་སུ་བརྩེ་བའི་ཕྱིར་རོ། །

[Block 5733]
དེ་ལས་གཞན་པ་སྐྱེས་པའི་རབས་བདུན་གྱིས་ནི་གནོད་པ་བྱས་པ་ལ་མི་མཇེད་པའི་བཟོད༌[^3660]པའི་དབང་དུ་བྱས་པའོ། །

[Block 5734]
གནོད་པ་བྱེད་པ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། བདག་དང་འབྲེལ་པ་དང་། བདག་ལ་གནོད་པ་བྱས་པའོ། །

[Block 5735]
བདག་དང་འབྲེལ་པ་ལ་གནོད་པ་བྱེད་པའི་དབང་དུ་བྱས་ནས། གཙུག་ཕུད་བྱང་ཆུབ་ཀྱི་སྐྱེས་པའི་རབས་སུ་རྒྱལ་པོ་དེས་རང་གི་ཆུང་མ་འཕྲོག་པར་བྱེད་པའི་གནོད་པས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 5736]
བདག་ལ་གནོད་པ་བྱེད་པ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། རྣམ་པར་འཚེ་བའི་གནོད་པ་དང་། གསོད་པའི་གནོད་པ་བྱེད་པའོ། །

[Block 5737]
དེ་ལས་རྣམ་པར་འཚེ་བའི་གནོད་པའི་དབང་དུ་བྱས་ནས། ངང་པ་དང་། བྱང་ཆུབ་ཆེན་པོའི་སྐྱེས་པའི་རབས་སུ་བསྟན་ཏེ། ལུས་དང་། སེམས་ལ་ཉེ་བར་གནོད་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5738]
ངང་པའི་སྐྱེས༌[^3661]པའི་རབས་སུ་ནི་རྙིས་བཟུང༌[^3662]བས་ལུས་ཀྱི་འཚེ་བ་ལ་འཇུག་པའི་གནོད་པ་ལས་བཟོད་པའོ། །

[Block 5739]
བྱང་ཆུབ་ཆེན་པོའི་སྐྱེས་པའི་རབས་སུ་ནི་སེམས་ལ་གནོད་པ་ཡིན་ཏེ། བརྙས་པས་ཉེ་བར་གཙེས་པས་འཇུག་པའི་གནོད་པ་ལ་བཟོད་པའོ། །

[Block 5740]
གསོད་པའི་གནོད་པར་བྱེད་པའི་དབང་དུ་བྱས་ནས་སྐྱེས་པའི་རབས་ལྷག་མ་བཞི་ཡིན་ཏེ། གསོད་པའི་གནོད་པ་བྱེད་པ༌[^3663]ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། གསོད་པའི་གནོད་པ་བྱེད་པར་སྦྱོར་བ་དང་། གསོད་པའི་གནོད༌[^3664]པར་སྦྱོར་བའོ། །

[Block 5741]
དེ་ལས་གསོད་པར༌[^3665]སྦྱོར་བའི་གནོད་པ་བྱེད་པའི་དབང་དུ་བྱས་ནས། ཤ་ར་བྷ་དང་། རུ་རུ་དང་། སྤྲེའུའི་སྐྱེས་པའི་རབས་སོ། །

[Block 5742]
དེ་ལ་ཤ་ར་བྷའི་སྐྱེས་པའི་རབས་སུ་ནི་བདག་ཉིད་ཀྱིས་མདའ་འཕེན་པ་དང་། གནོད་པ་མ་བྱས་ཏེ། ཕན་བཏགས་ཤིང་རྒྱལ་པོ་ལ་བཟོད་པ་སྟེ། སྦྱོར་བ་བྱེད་པ་ལ་བཟོད་པ་བྱེད་པའི་དབང་དུ་བྱས་པའོ། །

[Block 5743]
རུ་རུ་དང་། སྤྲེའུའི་སྐྱེས་པའི་རབས་སུ་ནི་བྱང་ཆུབ་སེམས་དཔས༌[^3666]དེ་གཉིས་ལ་ཕན་བཏགས་པ་ཡིན་དུ་ཟིན་ཀྱང་གནོད་པ་བྱེད་པར་འཇུག་པ་དེ་གཉིས་ལ་བཟོད་པའི་ཕྱིར་རོ། །

[Block 5744]
འདི་གཉིས་ལ་ཁྱད་པར་ནི་འདི་ཡོད་དེ། རུ་རུའི་སྐྱེས་པའི་རབས་སུ་ནི་རྒྱལ་པོ་བྱང་ཆུབ་སེམས་དཔའ་ལ་གསོད་པར༌[^3667]སྦྱོར་བས་སྦྱོར་དུ་བཅུག་པར་བསྟན་ཏེ། བདག་ཉིད་ཀྱིས་ནི་གསོད་པར༌[^3668]སྦྱོར་བ་མ་བརྩམས་སོ། །

[Block 5745]
སྤྲེའུའི་སྐྱེས་པའི་རབས་སུ་ནི་བྱང་ཆུབ་སེམས་དཔས་ཕན་བཏགས་པ་བྱས་པ་གང་ཡིན་པ་དེ་ལ་བདག་ཉིད་ཀྱིས་གསོད་པར་སྦྱོར་བ་རྩོམ་པའོ། །
--- END BLOCKS ---
