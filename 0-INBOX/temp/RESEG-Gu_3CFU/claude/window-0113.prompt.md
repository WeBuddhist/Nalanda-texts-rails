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
[Block 3956]
དགེ་འདུན་གྱི་ཁྲིམས་སུ་བཅའ་བ་བསྲུང་བར་བྱའོ། །

[Block 3957]
གློ་བུར་དུ་འོངས་པས་ཀྱང་དེ་ལས་མི་འགལ་བ་ཉིད་དུ་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལས་ཞེས་བྱ་བ་ནི་ཁྲིམས་སུ་བཅའ་བ་རྗེས་སུ་བསྲུང་བ་ལས་སོ། །

[Block 3958]
གློ་བུར་དུ་འོངས་པས་ཀྱང་དེ་ལ་རྗེས་སུ་བསྲུང་བར་བྱ་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3959]
ཡོད་དམ་མེད་པ་ཉིད་དང་ཇི་ལྟ་བུ་ཡོངས་སུ་ཤེས་པར་བྱ་བའི་ཕྱིར་དེས་དེ་དྲི་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཚོགས་འདི་ན་དགེ་འདུན་གྱི་ཁྲིམས་སུ་བྱ་བ་འགའ་ཞིག་ཡོད་དམ་འོན་ཏེ་མེད་ཡོད་ན་ཇི་ལྟ་བུ་ཞིག་ཅེས་བྱ་བ་དེ་ཡོངས་སུ་ཤེས་པར་བྱ་བའི་ཕྱིར་གློ་བུར་དུ་འོངས་པ་དེས་དེ་དྲི་བར་བྱའོ། །

[Block 3960]
དུས་གང་གི་ཚེ་ཞེ་ན། དེའི་ཕྱིར་ཧ་ཅང་ཡུན་རིང་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་ཧ་ཅང་ཡུན་རིང་དུ་གནས་པ་བས་སྔ་རོལ་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3961]
འཇུག་པ་དང་འཇུག་པའི་གནས་བཙལ་བ་པ་དང་རྫས་གཞག་པ་དང་རེ་ཞིག་བསྡད་པ་དེ་རྣམས་ཐམས་ཅད་ལས་ཇེ་དང་པོར་བྱའོ་ཞེས་བྱ་བའི་དོན་འདི་ལས་འདའ་བར་བྱ་བ་ལས་སྔ་རོལ་དུ་རིག་པར་བྱའོ། །

[Block 3962]
སངས་རྒྱས་ཀྱིས་གསུངས་པ་དགེ་འདུན་ལས་གཡོ་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཚེ་དང་ལྡན་པ་རྣམས་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་ཅེས་གང་གི་ཚེ་ཚེ་དང་ལྡན་པ་ཉེ་སྡེས་དགེ་འདུན་གྱི་ཁྲིམས་སུ་བྱ་བ་དྲལ་ཀྱང་ལྟུང་བ་མི་འབྱུང་བ་སྟེ། བཅོམ་ལྡན་འདས་ཀྱིས༌[^2710]བག་ཡངས་སུ་མཛད་དུ་ཟིན་ཀྱང་ཤིན་ཏུ་སྦྱངས་པའི་དབང་གིས་ལྟུང་བ་མི་འབྱུང་བ་ཉིད་དུ་གསུངས་པ་དེའི་འདི་བསྡུ་བའོ། །

[Block 3963]
ལྷུང་བཟེད་དང་ཆོས་གོས་དང་དྲ་བ་དང་ཕོར་བུ་དང་སྐ་རགས་དག་ལྷག་པ་འབུལ་བ་ན་དགེ་འདུན་གྱི་ཉེ་བར་གཞག་པའི་དོན་དུ་བླང་བར་བྱའོ། །

[Block 3964]
དེ་ལྟར་ཉེ་བར་གཞག་པ་ནི་དེ་དག་མེད་པ་རྣམས་ཀྱིས༌[^2711]ཅི་དགར་བསྐུར་རོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ལ་སོགས་པ་མེད་པ་རྣམས་ཀྱིས༌[^2712]གང༌[^2713]ལ་ཡོངས་སུ་ལོངས་སྤྱོད་པར་འོས་པ་ཉིད་དགེ་འདུན་དེ་རྣམས་ཀྱིས་བྱ་བ་ཤུགས་ཀྱིས༌[^2714]རྟོགས་པར་བྱའོ། །

[Block 3965]
འཁྲུར་འཇུག་པའི་སྤང་བ་རྣམ་པར་འབྱེད་པའོ། །

[Block 3966]
བཤང་བ་དང་གཅི་བ་དང་ལྗན་ལྗིན་དང་འདམ་རྫབ་ལ་སོགས་པས་མ་རུང་བར་གྱུར་པ༌[^2715]འཁྲུར་འཇུག་པ་ལ་ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་འདིར་འཁྲུར་འཇུག་པར་འོས་པ་ཉིད་ཡན་ལག་དྲི་མ་ཅན་ཉིད་ཀྱིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་གསལ་བ་ཉིད་དུ་བྱ་བའི་དོན་དུ་འདི་ཡིན་ནོ། །

[Block 3967]
དྲེའུ་རྔོག་དང་ཁྱིམ་པའི་གོས་དང་སྔས་ནང་ཚངས་ཅན་དང་རུང་བར་བྱས་པ་དང་སྤངས་པ་དང་དགེ་འདུན་གྱི་རྣམས་ལ་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་འདི་རྣམས་ཉེ་དུ་མ་ཡིན་པའི་དགེ་སློང་མ་ལ་འཁྲུར་འཇུག་པ་ལ་སོགས༌[^2716]པ་ལ་ཉེས་བྱས་སོ། །

[Block 3968]
དྲེའུ་རྔོག་ཁྱིམ་པ༌[^2717]མ་ཡིན་པའི་གཡོག་ཉིད་ཀྱིས་འདིའོ། །

[Block 3969]
ཁྱིམ་གྱི་གཡོག་པོ་ཉིད་ནི་དགེ་སློང་གི་གཡོག་ཉིད་ཀྱི་ཕྱིར་དེའི་རྫས་རྣམས་ལ་རུང་བ་ཉིད་དོ་ཞེས་བྱ་བ་འདིའི་འདི༌[^2718]སྤྲོས་པའོ། །

[Block 3970]
འདིར་ཉེ་བར་ལོངས་མ་སྤྱད་པ་ནི་མ་ཆགས་པའོ། །

[Block 3971]
ཁྱིམ་གྱི་གཡོག་དང་སྔས་རྟེན་མགོ་བོ་ཙམ་གྱིས༌[^2719]ལོངས་སྤྱོད་པར་སྐྱེས༌[^2720]པ་ཉིད་ཀྱི་ཕྱིར་དང་ལུས་ཐམས་ཅད་ལ་ཡང་དག་པར་རིག་པས་ལོངས༌[^2721]སྤྱོད་ཅིང་རྣམ་པར་མི་རྟོག་པ་ལ་རང་ཉིད་ལ་མི་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 3972]
འབུལ་བ་ལ་རང་ཉིད་འཕོ་བ་ཉིད་ཀྱི་ཕྱིར་དང་དགེ་འདུན་གྱི་རང་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 3973]
འཁྲུར་འཇུག་པའི་སྤང་བ་ཞུ་བའི་སྐབས་སོ།། །།

[Block 3974]
དགེ་སློང་མས་གོས་རིན་པོ་ཆེ་བརྗེ་བའི་ཕྱིར་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བརྗེ་བའི་ཕྱིར་ཡིན་གྱི་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་ཕྱིར་ནི་མ་ཡིན་ནོ། །

[Block 3975]
དགེ་སློང་མ་དང་ལྷན་ཅིག་བརྗེ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གོས་ཀྱི་ཕྱིར་འདིར་ཁྱད་པར་མེད་པའི་ཕྱིར་ཐམས་ཅད་ཀྱི་དབང་དུ་བྱས་ནས་མདོ་བྱས་པའོ། །

[Block 3976]
རྫས་ཇི་ལྟ་བུ་བརྗེ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་མཉམ་པས་སོ། །

[Block 3977]
ཡང་ན་དེ་དག་འགལ་བ་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མ་དང་ལྷན་ཅིག་དེ་བརྗེ་བར་བྱེད་པའི་དགེ་སློང་མ་དེ་དགའ་བར་འགྱུར་བས་རིན་ཐང་གིས་གཟུང་བ༌[^2722]ལ་ནི་བརྗེ་བའི༌[^2723]རྣམ་པ་ཉིད་དོ། །

[Block 3978]
གང་དུ་སྔ་བ༌[^2724]ལེན་པའི་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིས་ལེན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་ཉེ་དུ་མ་ཡིན་པའི་དགེ་སློང་མ་ལ་དེར་འདུ་ཤེས་པའམ་ཡིད་གཉིས་ཟ་བ་ཞེས་སྔར་བྱས་སོ། །ཇི་ལྟར་ལེན༌[^2725]ཞེ་ན། དེའི་ཕྱིར་རྣམ་པར་རིག་བྱེད་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅང་མི་སྨྲ་བ་དང་དུ་ལེན་པས་ཀྱང་མ་ཡིན་ལ་ཚིག་ལས་གཞན་པའི་རྣམ་པར་རིག་བྱེད་ཀྱིས་ཀྱང་མ་ཡིན་ནོ། །ཅི་ཞིག་གི་ཕྱིར་ལེན་ན་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་ལ་གོས་འབུལ་བ་དང་། ལེགས་པར་སྨྲ་བ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ་རབ་ཏུ་སྦྱིན་པ་ལའོ། །

[Block 3979]
བསྙེན་པར་རྫོགས་པར་བྱེད་པ་དག་དང་བོར་རླག༌[^2726]བྱུང་བ་དག་ལའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་ལས་ལེན་པ་ལ༌[^2727]ལྟུང་བ་མེད་དོ། །

[Block 3980]
དད་རྫས་བརྗོད་དེ་མདུན་དུ་བཞག་ནས་མི་ལྟོས་པར་སོང་བ་ལའོ་ཞེས་བྱ་བ་ནི་འབུལ་བར་བྱེད་པའི་དགེ་སློང་མ་ལས་ཕྱིར་སྤོང་བར་བྱེད་པ་ཉིད་ལ་དགེ་སློང་གིས་ཐོབ་ན་དད་རྫས་བརྗོད་དེ་བདག་ཉིད་དད་པ་ཅན་དུ་གྲགས་པར་ཤེས་ཏེ། རྫས་དེ་མདུན་དུ་བཞག་ནས་མི་ལྟོས་པར་སོང་བ་ནི་དེའི་ཚེ་བླངས་ན་ལྟུང་བ་མེད་དོ། །

[Block 3981]
ལེན་པའི་སྤང་བ་རྣམ་པར་འབྱེད་པའོ།། །།

[Block 3982]
ལག་ཏུ་འོངས་པ་ཉིད་ནི་ཐོབ་པ་ཉིད་དོ། །

[Block 3983]
བལྟ་བའི་ཉེན་ཀོར་དུ་གྱུར་པ་ནི་དེའི་དང་པོའོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་ལག་ཏུ་འོངས་པ་ཉིད་ལའོ། །

[Block 3984]
འདིར་གཞུང་ནི་གོས་ཀྱི་གཞིའི་ཞུ་བ་ལས།

[Block 3985]
ཇི་ཙམ་གྱིས་ན་གོས་ཐོབ་པ་ལགས། གང་ཚུན་ཆད་དེའི་ལག་ཏུ་འོངས་པར་གྱུར་པ་འམ་བལྟ་བའི་ཉེན་ཀོར་དུ་གྱུར་པ་ནའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3986]
ཉེ་བར་མ་གྱུར་པ་ནོད་པ་ཉིད་ནི་སྦྱོར་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་ཡི་གེ་ཁ་ཅིག་ལས་གྲོང་ཆེ་གེ་མོ་ཞིག་ན་གོས་མཆིས་ཀྱིས༌[^2728]དེ་ཚེ་དང་ལྡན་པ་ལས༌[^2729]གསོལ་ལོ་ཞེས་ཟེར་བ་ནོད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3987]
འདིར་ཉེ་བར་མ་གྱུར་པ་ནོད་པ་ཉིད་ཀྱི་ཕྱིར་གཞན༌[^2730]ནི་སྨད་པའི་རྒྱུ་མཐོང་བ་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་འདིར་འདི༌[^2731]ཤེས་པའོ། །

[Block 3988]
འདིར་དང་དུ་ལེན་པ་ཡང་ནོད་པ་ལ་ཤེས་པར་བྱ་སྟེ་གོ་བར་བྱ་བ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 3989]
དེ་ལྟར་གཞུང་ནི་འདི་ཡིན་ཏེ་སྔར་བཞག་པར་གྱུར་ནས་སྨྲས་པ་རྗེས་སུ་གནང་བར་བགྱི་ཡིས་འཕགས་པས་ལོངས་སྤྱད་དུ་གསོལ། བདག་ལ་བསོད་ནམས་སུ་འགྱུར་རོ་ཞེས་ཟེར་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པའོ། །

[Block 3990]
ཡང་ན་ཕྱིར་སྩལ༌[^2732]མི་འཚལ་བར་འབུལ་གྱིས་ལོངས་སྤྱད་དུ་གསོལ་ཞེ་འམ། གོས་ཆ་མི་མཐུན་པ་དང་བརྗེའོ་ཞེས་ཟེར་བ་བླངས་པར་གྱུར་པ་ལས་ཕྱིས་ཚེ་དང་ལྡན་པ་རིན་སྩལ༌[^2733]མི་འཚལ་ལོ་ཞེས་ཟེར་བ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་མདོ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 3991]
རྒྱ་ཆེ་བ་དང་ཐ་སྙད་ཀྱི་དབང་མ་ཡིན་པ་ཉིད་ནི་གོས་སྦྱིན་པ་ལ་སོགས་པ་ལ་གཙོ་བོ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཇི་ཙམ་དུ་རང་གི་ལུས་ཀྱིས་འཇུག་པ་ཉེ་བར་བཀག་པར་གྱུར་པ་ཉིད་ཀྱིས་མ་ཡིན་པ་དེ་ཙམ་དུ་འདིར་རྒྱ་ཆེ་བ་ལ་མངོན་པར་བརྟེན་པར་རིག་པར་བྱའོ། །

[Block 3992]
འདིར་གཉིས་པོ་འདི་ཐམས་ཅད་གཙོ་བོར་རིག་པར་བྱ་བ་སྟེ། ཐ་དད་པ་ནི་མ་ཡིན་ནོ། །

[Block 3993]
བོར་རླག༌[^2734]བྱུང་བ་རྙེད་པ་ལ་འདི་ཙམ་དུ་གཟུང་བ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 3994]
རེ་ཞིག་གི་སེམས་ཀྱིས་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། ཉེ་བར་གཡོགས་པ་འམ་བགོས་པའམ་དུས་རེ་ཞིག་པ་སྟེར་བ་ལ་གང་ཞིག་ཡིད་གཅུགས༌[^2735]པས་ལེན་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་མདོ་འདིས༌[^2736]བསྡུས་པ་ཡིན་ནོ། །

[Block 3995]
རིན་སྦྱིན་པ་བརྗེད་པ་ལའོ་ཞེས་བྱ་བ་ནི། ཚེ་དང་ལྡན་པ་སླར་ནོར་མ་སྦྱིན་ཅེས་ཟེར་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་འདིའི་རྗེས༌[^2737]ལ་དེར་འདི་གསུངས༌[^2738]སོ། །
--- END BLOCKS ---
