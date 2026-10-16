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
[Block 4376]
རང་དགར་ཅི་བདེར་སྤྱོད་པར་རིགས་པ༌[^2812]གང་ཡིན་པ་དེ་ནི་རང་དགར་ཅི་བདེར་སྤྱད་པར་རིགས་ཏེ། སྡིག་པ་དང་དགེ་བ་དག་ལ་སྤང་བ་དང་། བསྟེན་པའི་ཉེས་པ་དང་ཡོན་ཏན་མེད་པས་སོ། །

[Block 4377]
དེ་ལྟ་མོད་ཀྱི་འཇིག་རྟེན་པ་རྣམས་ཀྱི་ཁ་ན་མ་ཐོ་བས་འཇིགས་པར༌[^2813]བྱེད་དོ་ཞེས་དེ་ལྟར་རྟོག་ན་ཡང་སྨྲས་པ། འགྲོ་བས༌[^2814]འཕྱ་བ་དག་གིས་འཇིགས་ནས་སུ། །ཞེས་བྱ་བ་སྨོས་ཏེ། འཇིག་རྟེན་གྱིས༌[^2815]མི་སྨན་པར༌[^2816]སྨྲ་བས་འཇིགས་པའོ།[^2817] །བདག་གི་ཚིག་དང་མི་མཐུན་སྤྱོད་པ་ཡིན། །ཞེས་བྱ་བ་ནི་སྡིག་པ་བསྟེན་པ་དང་། དགེ་བ་སྒྲུབ་པ་ལ་སྐྱོན་དང་ཡོན་ཏན་མེད་དོ་ཞེས་སྨྲ་ན་སྡིག་པ་བསྟེན་པ་དང་། དགེ་བ་བསྟེན་པར་བྱེད་པ་ཡིན་པས་ན་བདག་གི་ཚིག་དང་མི་མཐུན་པར་སྤྱོད་པ་ཡིན་ཏེ། འགྲོ་བས༌[^2818]འཕྱ་བའི་ཉེས་པས་འཇིགས་པས་ནི༌[^2819]རང་གི་ཚིག་དང་མི་འགལ་བར་སྤྱོད་པའོ། །

[Block 4378]
དེ་ཡོད་ན་ནི་དེ་དག་ཀྱང་ཡོད་ཀྱི་ཆད་པར་སྨྲ་བ་འདི་ལ་ནི་འགྲོ་བས༌[^2820]འཕྱ་བའི་ཉེས་པ་མེད་དོ། །

[Block 4379]
འགྲོ་བས༌[^2821]འཕྱ་བའི་སྐྱོན་གཅིག་པུར༌[^2822]མ་ཟད་དེ། འདི་ལྟར་རང་གི་གྲུབ་པའི་མཐའི༌[^2823]ལས་བསྟན་པའི་བདེ་བའང་མི་འཐོབ་པ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར། འཇིག་རྟེན་ཚུལ་ལ་གནས་པར་གྱུར་ན་ནི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། རང་གི་གཞུང་ལུགས་ཞེས་བྱ་བ་ནི་རང་གི་གྲུབ་པའི་མཐའོ། །

[Block 4380]
རང་གི་གྲུབ་པའི་མཐའ་སྨྲ་བ་འཁྲུལ་པས་དོན་མེད་པར་འགྱུར་བ་ནི་བདེ་བ་འཐོབ་པ་སྟེ། དེ་བས་ན་འགྲོ་བས༌[^2824]འཕྱ་བར༌[^2825]འཇིགས་ན་རང་གི་གྲུབ་པའི་མཐའི་འབྲས་བུ་མི་ཐོབ་པས་སྨྲ་བ་དོན་མེད་པ་ནི་འཁྲུལ་པ་ཡིན་པས་སྨྲ་བ་འཁྲུལ་པའོ། །

[Block 4381]
སྨྲ་བའི་འཁྲུལ་པ་ཉིད་ནི་ཕྱིན་ཅི་ལོག་པ་ཡིན་ཏེ། དེའི་སྨྲ་བ་འཁྲུལ་པས་དོན་མེད་པ་གང་ཡིན་པ་དེ་ནི་སྨྲ་བ་འཁྲུལ་པས་དོན་མེད་པ་སྟེ། མཆོག་ཏུ་འབྲས་བུ་མེད་པའི་ཕྱིར་རོ། །

[Block 4382]
དེའི་ཚིག་ནི་བྱིས་པའི་ནང་ན་ཐ་མ་ཉིད་ཡིན་ཏེ། ལྟ་བ་ཐམས་ཅད་ཀྱི་ནང་ན་ཐ་ཆད་བཟུང་ཞིང་འཇུག་པའི་ཕྱིར་རོ། །

[Block 4383]
རྣམ་པ་སྣ་ཚོགས་ཡོན་ཏན་དང་ལྡན་པའི་ཤིང་ཞེས་བྱ་བ་ལ། བདག་གི་ལས་ཀྱིས་བྱ་བ་མ་ཡིན་པར་འབྱུང་བ་དག །[^2826]འཇིགས་པ་རྣམས་ཀྱང་ཕྱིས་ཡང་མི་སྐྱེའོ༌[^2827]ཞེས་ཁས་ལེན་ཅིང་ཇི་ལྟར་ཡང་ཤིང་གི་མཚན་ཉིད་འདི་ལྟ་བུར་འཇིག་རྟེན་ཡང་རྒྱུ་གང་ཞིག་ཡོད། དེ་ལྟ་ན་ཡང་འཇིག་རྟེན་ན་ནི་ཤིང༌[^2828]དང་འདྲ་བ་ཡིན་པས་དངོས་པོ་རྣམས་ཀྱི་རྒྱུ་འགྲུབ་པའི་དངོས་པོ་ཡིན་ཡང་དངོས་པོ་མེད་པའོ་ཞེས་སྨྲ་བ་སྟེ། ཆད་པར་སྨྲ་བ་ལ་ནི་འཇིག་རྟེན་ཕ་རོལ་མེད་པས་འབྲས་བུ་ཡིད་དུ་འོང་བ་མེད་དོ། །

[Block 4384]
དེས་ན་སྡིག་པ་ཐམས་ཅད་ཀྱི་ནང་ན་ཁྱད་པར་དུ་གྱུར་པ་ཡིན་ནོ། །

[Block 4385]
བྱས་ནས་སུ་ཞེས༌[^2829]བྱ་བ་ནི་གཞུང་ལུགས་ཀྱི་བསྟན་བཅོས་པའོ།[^2830] །དེ་གང་ཡིན་ཞེ་ན། དགེ་བའམ་མི་དགེ་བའོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྲིད་ཀྱི་ཕྱིར་རོ། །

[Block 4386]
རྗེས་སུ་འགྲོ་བ་ནི་དུས་ཕྱི་མ་སྟེ། ཕྱི་ནས་གང་ཞིག་ཅེས་བྱ་བ་ལ། དགོས་པ་དག་ནི་བྱུང་བར་གྱུར་པའི་ཚེ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ།

[Block 4387 [VERSE]]
ཕྱོགས་ཀྱི་ཆོས་དང་འགལ་བར་བསྟན་པའི་དོན་ཏོ། །
འོན་ཏེ་སྙིང་རྗེ་མེད་ཕྱིར་སྨད་འགྱུར་རམ། །

[Block 4388]
ཞེས་བྱ་བའི་ཚིགས་བཅད་བསྟན་པ་ལ། གྲུབ་པའི་མཐའི་སྐྱོན་བསྟན་པའི་ཕྱིར། སྨད་འགྱུར་ཞེས་བྱ་བ་སྨོས་པ་ཡིན་ཏེ། མཐོང་བའི་ཆོས་ལ་བདེ་བའི༌[^2831]ལས་མི་སྙན་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 4389]
འབྲས་བུ་སྡུག་བསྔལ་ཞེས་བྱ་བ་ནི་ཕ་རོལ་ཏུ་ངན་སོང་དུ་འགྲོ་བའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4390]
གཞུང་ལུགས་ཞེས་བྱ་བ་ནི་གཞུང་ལུགས་ཀྱི་བསྟན་བཅོས་སོ། །

[Block 4391]
གང་ན་རིགས་པའི་གཞུང་ལྡན་འདི༌[^2832]འདྲ་བ། །ཞེས་བྱ་བ་ནི་ཚེ་འདིར་སྨད་པར་བྱས་པ་དང་། འཇིག་རྟེན་ཕ་རོལ་ཏུ་ཡང་སྡུག་བསྔལ་གྱི་འབྲས་བུ་ཡིན་ཏེ། གང་ན་ལས་འདི་ཡོད་པ་དེར་གནོད་བཞིན་དུ་བྱེད་ཅིང་རིགས་པའི་གཞུང་ལུགས་འདིའོ། །

[Block 4392]
འདི་ལྟ་བུར༌[^2833]འཁྲུལ་པ་གང་ཡིན་པ༌[^2834]དེ་ནི་འཁྲུལ་པ་ཅི་འདྲ་བའོ། །

[Block 4393]
འཁྲུལ་པ་ནི་ཕོངས་པའོ། །

[Block 4394]
གཙུག་ལག་གི་ལམ་གྱི་ཞེས་བྱ་བ་ནི་གཙུག་ལག་གི་ཚུལ་གྱིས་ཏེ། གཙུག་ལག་ཅེས་བྱ་བ་ནི་བརྡ་ཙམ་དུ་སྦྱར་བ་ཡིན་ཏེ། གཙུག་ལག་ཉིད་ནི་མ་ཡིན་བསྟན་བཅོས་ཀྱི་ཚུལ་ཙམ་ཉིད་དོ། །

[Block 4395]
གཙུག་ལག་ཉིད་ལམ་ཡིན་པས་ན་གཙུག་ལག་ལམ་སྟེ། ཆོས་མ་ཡིན་པ་སྒྲུབ་པ་ལ་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 4396]
ལམ་ཡང་ཡིན་ལ་གསལ་བ་ཡང་ཡིན་པས་ལམ་ནི་གསལ་བའོ། །

[Block 4397]
དེས་བསྟན་པ་ནི་ལམ་གསལ་བར་བསྟན་པའོ། །

[Block 4398]
དེ་འཁོར་གྱི་ནང་ན་རྒྱལ་བར་གྱུར་པ་གང་ཡིན་པ་དེ་དག་ནི་འཁོར་གྱི་ནང་ན་རྒྱལ་བར་གྱུར་པའོ། །

[Block 4399]
སྤོབས་པ་ཆེ་བར་གོམས་པ་གང་ཡིན་པ་དེ་དག་ནི་སྤོབས་པ་ཆེ་བར༌[^2835]གོམས་པའོ། །

[Block 4400]
སྲོག་དང་བཅས་པའི་སྤྲེའུ་བཀུམ་པ་ནི་མ་ལགས་ཀྱི་ཞེས་བྱ་བ་འདིས་ནི། སྤྲེའུའི་པགས་པ་ཡོད་པ་ནི་སྤྲེའུ་སྤྲུལ་པ་ཡིན་གྱི་སྲོག་དང་བཅས་པ་ནི་མ་ཡིན་ནོ། །

[Block 4401]
དེ་སྲོག་མེད་པ་ཉིད་ཀྱིས་བསད་པ་ཡང་མེད་དོ། །

[Block 4402]
[^2836]དེ་བས་ན་བཀུམ་པའང་མ་ལགས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4403]
རྒྱུ་ལས་གྲུབ་པར་མཐོང་བཞིན༌[^2837]ལ། །ཞེས་བྱ་བ་འདིས་ནི་རྒྱུ་མེད་པར་སྨྲ་བ་དགག་པ་ཡིན་ནོ། །

[Block 4404]
རང་དབང་ཞེས་བྱ་བ་འདིས་ནི། དབང་ཕྱུག་རྒྱུར་སྨྲ་བ་འགོག་པ་ཡིན་ཏེ་གང་གི་ཕྱིར་དབང་ཕྱུག་རྒྱུར་སྨྲ་བ་གཞན་དབང་ཡིན་ཏེ། དབང་ཕྱུག༌[^2838]ལ་རག་ལས་པའི་ཚུལ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4405]
འཇིག་རྟེན་ཕ་རོལ་ཞེས་བྱ་བ་འདིས་ནི་ཆད་པར་སྨྲ་བ་དགག་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་ཆད་པར་སྨྲ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་ཤེས་པ་མ་ཡིན་ཏེ། འཇིག་རྟེན་ཕ་རོལ་ཁས་མི་ལེན་པའི་ཕྱིར་རོ། །

[Block 4406]
དགེ་བར་ཁས་ལེན་སྙིང་རྗེ་ཅན། །ཞེས་བྱ་བ་འདིས་ནི་ལུས་ཀྱི་བསྟན་བཅོས༌[^2839]རྗེས་སུ་འཇུག་པ་འགོག་པར་བྱེད་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་དེ་ནི་དགེ་བར་དམ་བཅའ་བ་མ་ཡིན་ཏེ། གཞན་ལ་ཁྲོ་བ་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 4407]
དེ་སྙིང་རྗེ་ཅན་ཡང་མ་ཡིན་ནོ། །

[Block 4408]
བཞི་པོ་འདི་དག་ནི་སྲོག་གཅོད་པའི་ཉེས་པ་མེད་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4409]
ཐམས་ཅད་སྔོན་གྱི་ལས་ཀྱིས་བྱས་པར་ལྟ་བ་དེ་ཅིའི་ཕྱིར་མ་བསྟན་ཅེ་ན། གང་གི་ཕྱིར་དེ་ནི་ལས་ཀྱི་རྒྱུ་ཉིད་དུ་སྒྲུབ་པ་ཡིན་ཏེ། འགྲོ་བ་རྣམས་དེ་ལྟར་སྒྲུབ་པ་ནི་སྲོག་ཆགས་གསོད་པར་བྱེད་དེ། དེ་ནི་ད་ལྟར་བྱུང་བའི་སྐྱེས་བུ་བྱེད་པའི་རྐྱེན་ཉི་ཚེར་འགྱུར་རོ། །

[Block 4410]
གཞུང་བྱེད་པ་ཞེས་བྱ་བ་ནི་མ་ཡིན་པའི་སྡིག་པའོ། །ཅིའི་ཕྱིར་ཞེ་ན། གྲགས་པ་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་རོ། །

[Block 4411]
གཞན་དུ་ན་གཞུང་མི་བྱེད་དེ། སྡིག་པ་ཉིད་ཡིན་པས་སོ། །

[Block 4412]
ཇི་ལྟར་ཁས་བླང་བར་བྱ༌[^2840]ཞེས་བྱ་བ་ནི་ཁས་ལེན་པར་བྱེད་པའོ། །

[Block 4413]
སྡིག་པ་ལ་སྡིག་པ་མ་ཡིན་པའི་ལྟ་བས་གང་དེ་གྲགས་པ་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་སྡིག་པ་མི་བྱེད་དེ། ཇི་ལྟར་རིགས་པས་སྨྲ་བ་ཁས་ལེན་པར་བྱེད་ཅེས་པ་སྟེ། གྲགས་པ་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར། གཞུང་མི་བྱེད་ཅེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 4414]
གཞན་དུ་ན༌[^2841]བྱེད་པ་དེ་ནི་དོན་གྱིས་མི་འགྲུབ་པའོ། །

[Block 4415]
དེས་ན་དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། མི་ཡི་བདག་པོ་ལྟ་བ་བཟང་ངམ་ངན།[^2842] །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །
--- END BLOCKS ---
