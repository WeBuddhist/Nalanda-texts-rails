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
[Block 4166]
ལྕགས་ཀྱི༌[^4246]ཀ་བ་དག་གིས་སོ། །

[Block 4167]
དེ་དག་ལ་བ་དན་གདགས་སོ་ཞེས་བྱ་བ་ནི་ལྕགས་ཀྱི་ཀ་བ་དེ་དག་ལ་བ་དན་དག་གདགས་པ་ནི་ཆོས་དང་མཐུན་པའོ། །

[Block 4168]
རྗེས་སུ་འགྲོ་བ་བྱའོ། །

[Block 4169]
རྐང་རྒྱན་དང་རྣ་རྒྱན་མ་གཏོགས་པའི་རྒྱན་གདགས་སོ། །

[Block 4170]
སངས་རྒྱས་ཀྱི་སྐུ་གཟུགས་བརྙན་དང་བདག་པོ་གཞན་ལ་དེ་གཉིས་མ་གཏོགས་པའི་ཆོས་དང་མཐུན་པ་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པར་བྱའོ། །

[Block 4171]
སྤོས་ཀྱི་ལུས་སྦྱིན་པར་བྱའོ། །

[Block 4172]
ཁྱོགས་ཀྱིས་བསྐུར༌[^4247]རོ། །

[Block 4173]
ཤིང་རྟས་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་བསྐུར༌[^4248]རོ་ཞེས་བྱ་བར་སྦྱར་ཏེ་ཆོས་དང་མཐུན་པའོ། །

[Block 4174]
དེ་ལ་གདུགས་དང༌[^4249]རྒྱལ་མཚན་དང་བ་དན་དག་བསྒྲེང་ངོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་ཤིང་རྟ་དེ་ལའོ། །

[Block 4175]
དབུ་ལ་མེ་ཏོག་རྣ་རྒྱན་གདགས་སོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི༌[^4250]སྐུ་གཟུགས་ཀྱི་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4176]
མཆོད་ཡོན་དང་ཞབས་ལ་གསོལ་བ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལ་དབུལ་བ་ཆོས་དང་མཐུན་པའོ། །

[Block 4177]
དད་རྫས་ནི་གནས་པ་དང་། གཞོན་ནུ་དང་རྒན་པོ་དག་གིས་བླང་ངོ་། །གནས་བརྟན་རྣམས་ཀྱིས་བསྲུང་ངོ་ཞེས་བྱ་བ་ནི་དད༌[^4251]རྫས་སོ། །

[Block 4178]
ལམ་པོ་ཆེར་ཕྲེང་བའི་ཟ་མ་ཏོག་བྱའོ་ཞེས་བྱ་བ་ནི་མཆོད་ཡོན་དང་ཞབས༌[^4252]ལ་གསོལ་བ་མེ་ཏོག་དང་གོས་ལ་སོགས་པ་གཏོར་བ་དག་ས་ལ་མི་འབབ་པར༌[^4253]བྱ་བའི་ཕྱིར་དེ་དག་ལམ་སྲོལ་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4179]
ཕྲེང་བའི་ཟ་མ་ཏོག་གི་ནང་དུ་དྲིའི་ཟ་མ་ཏོག་གཞུག་གོ་ཞེས་བྱ་བ་ནི་ཕྲེང་བའི་ཟ་མ་ཏོག་གི་ནང་དུ་དྲིའི་ཟ་མ་ཏོག་གཞག་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4180]
ཕྲེང་བ་གདགས་སོ་ཞེས་བྱ་བ་ནི་ཕྲེང་བ་གདགས་པ་ཆོས་དང་མཐུན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4181]
མཆོད་པ་རྫོགས་ཤིང་རོལ་མོ་བརྟུལ་བ་དག་ན་སྐྱེ་བོའི་ཚོགས་ཕྱི་རོལ་དོང་བའི་ཚེ་རྒྱན་བརྟུལ་ལོ་ཞེས་བྱ་བ་སྨོས་ན་གང་གི་ཚེ་ཡིན་ཞེ་ན་དེའི་ཕྱིར་མཚན་མོའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉིན་མོ་ནི་ཕྱིར་དོང་དུ་ཟིན་ཀྱང་ཡང་ཕྱིར་འོངས་པ་དང་།

[Block 4182]
དང་པོ་ནས་ཕྱིར་མི་འོང་བ་ཡང་སྲིད་པས་འདི་དག་གི་འགྲོ་བ་ཡོད་པས་འདི་མི་བྱ་བ་ཉིད་དོ། །

[Block 4183]
བྱང་ཆུབ་སེམས་དཔའི༌[^4254]འབའ་ཞིག་ལ་དེ་ལ་དེ༌[^4255]ལྟར་བྱ་བར་མ་ཟད་ཀྱི། མཆོད་པ་ཐམས་ཅད་ལ་ཆོ་ག་དེ་ལྟར་བྱ་བ༌[^4256]རིག་པར་བྱའོ། །

[Block 4184]
ཤི་བའི་སྐབས་སུ་མཆོད་རྟེན་བྱ་བ་ལ་སོགས་པ་དང་འདྲ་བ་དང་བཅས་པ་བཤད་ཟིན་ཏོ། །

[Block 4185]
[^4257]

[Block 4186]
ད་ནི་མཆོད་རྟེན་དང་། ལྷ་དང་མཐའ་མེད་པའི་རབ་ཏུ་བྱུང་བའི་གནས་སྐབས་སུ་བབ་པ་བརྗོད་པར་བྱ་སྟེ། རབ་ཏུ་བྱུང་བའི་གནས་སུ་དུས་སྟོན་བྱ་བ་ཆོས་དང་མཐུན་ནོ་ཞེས་བྱ་བ་ནི་ཁང་པའི་དུས་སྟོན་ནི་འོས་པའོ། །

[Block 4187]
འདུལ་བ་རྒྱ་ཆེར་བསྟན་པ་བཤད་ཟིན་ཏོ།། །།

[Block 4188]
ད་ནི་འདུལ་བ་མདོར་བསྡུས་ནས་བརྗོད་པར་བྱ་སྟེ། མི་རུང་བ་དང་མཐུན་ལ་རུང་བ་དང༌[^4258]འགལ་བ་ནི་རུང་བ་མ་ཡིན་པར་བསྡུའོ་ཞེས་བྱ་བ་ནི་གང་རུང་བ་མ་ཡིན་པ་བསྟེན་ཅིང་རུང་བ་དང་འགལ་བ་དེ་ནི་རུང་བ་མ་ཡིན་ཏེ། དེ་ནི་འདིར་རུང་བ་མ་ཡིན་པར་མདོར་བསྡུའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4189]
ཕྱི་མ་དང་མཐུན་པ༌[^4259]ལ་སྔ་མ་དང་འགལ་བ་ནི་རུང་བར་རོ་ཞེས་བྱ་བ་ལ། ཕྱི་མ་ཞེས་བྱ་བ་ནི་རུང་བ་སྟེ། དེ་དང་མཐུན་ལ་སྔ་མ་ཞེས་བྱ་བ་ནི་མི་རུང་བ་སྟེ། དེ་དག་དང་འགལ་བ་ནི་རུང་བ་སྟེ། དེ་ནི་འདིར་རུང་བར་མདོར་བསྡུའོ། །

[Block 4190]
གནས་མལ་གྱི་གཞིའི་ཕྲན་ཚེགས་ལ་སོགས་པའི་སྐབས་སོ། །

[Block 4191]
གནས་མལ་གྱི་གཞི་རྫོགས་སོ། །

[Block 4192]
[^4260]

[Block 4193 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 4194 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 4195]
འདུལ་བ་མདོའི་འགྲེལ་པ་རང་གི་རྣམ་པར་བཤད་པ་ཞེས་བྱ་བ་གནས་བརྟན་ཡོན་ཏན་འོད་ཀྱིས་མཛད་པ་རྫོགས་སོ།། །།

[Block 4196 [VERSE]]
རིག་བྱེད་ཉི་མ་རྣམས་ནི་མ་ལུས་གདོན་བྱས་ནས། །
བསྟན་བཅོས་བཞི་པོ་རྣམས་ལ་མཉམ་པོའི༌[^4261]མཐུ་མངའ་བ། །
དགེ་སློང་ཡོན་ཏན་འོད་ཅེས་བྱ་བ་བྱུང་གྱུར་ཏེ། །
གང་ཞིག་ཤཱཀྱའི་སྲས་ཀྱིས་རབ་ཏུ་བསྐུལ་བར་གྱུར། །

[Block 4197 [VERSE]]
བསོད་སྙོམས་ཕྱིར་ནི་གང་གི༌[^4262]བར་སྣང་ལ་འཁོར་ཞིང་། །
ལྷ་རྣམས་ལུས་ཕྱེད་དག་གིས་བྱུང་བར༌[^4263]གྱུར་པ༌[^4264]ནི། །
བརྩོན༌[^4265]ལྡན་ཞལ་ཟས་བདུད་རྩི་རྣམས་ནི་འཛིན་མཛད་དེ། །
འོད་ཟེར་དང་ལྡན་རྒྱན་རྣམས་ཀྱིས་སྤྲས་གནས་པར་གྱུར། །

[Block 4198]
ནུ་མ་གཉིས་ཀྱི་ལྕིད་ཀྱིས་དུད་བྱས་ལྷ་ཡི་བུད་མེད་རྣམས་ནི་ཉམས་དགའ་བ། །ལག་པ་པདྨའི་ཟེ་འབྲུ༌[^4266]རྣམས༌[^4267]ལ་དབུལ་བ༌[^4268]ཆགས་པའི་ལག་དར་བཅས། །རོ་དང་བཅས་པའི་ཤིང་རྣམས་ལ་ནི་བྱུང་བའི་བཅའ་བ་དང་བཅས་པ། །རྟག་ཏུ་གཡུལ་ངོར་རྣམ་པར་རྒྱལ་བའི་ཕྱོགས་ནི་ཁ་ན་མ་ཐོ་ཉིད། །ཡེ་ཤེས་ལས་ནི་རབ་ཏུ་འཇུག་པའི་སྟེང་དུ་གང་གི་འགྲེལ་པ༌[^4269]བརྩམས་པ་སྟེ། ། བྱེ་བྲག་བཤད་པ་རྣམས་ལས་ཤིན་ཏུ་རྒྱ་ཆེན་ཚུལ་ནི་རྣམ་པར་གསལ་བྱེད་པ། །ཐམས་ཅད་དུ་ནི་སྣང་བར་བྱེད་པའི་འོད་ཟེར་ཚོགས་ཀྱིས་མུན་པའི་རབ་རིབ་ལྟར། །རིན་ཆེན་འབྱུང་གནས་མཆོག་གི་གྲུབ་མཐའ་ང་རྒྱལ་ཆེན་པོ་རྣམས་ནི་འཇིག་པར་བྱེད། །ཐེག་པ་རྒྱས་པས་ཟབ་པའི་སངས་རྒྱས་གསུང་གི་ཆུ་ཡི་ཕུང་པོ་ལས། །

[Block 4199]
རང་བྱུང༌[^4270]ཚུལ་ནི་རྣམ་པར་འཇོམས་པའི་ཤེས་རབ་ཀྱིས༌[^4271]བསྲུབས་ཡང་དག་པར། །ཤིན་ཏུ་དྲི་མེད་ཚུལ་གྱིས་རིན་ཆེན༌[^4272]རྣམས་ཀྱི་འོད་གསལ་འགྲེལ་པའི་དཔལ། །འགྲོ་བ་རྣམས་ཀྱི༌[^4273]དགེ་བའི་རྒྱུར་གྱུར་དེས་ནི་མྱུར་དུ་བཏུ་བར་བྱས། །མུན་པ་འཇོམས་ཤིང་ཚུལ་ཁྲིམས་ཡངས་པའི་འོད་ཟེར་ཅན་ནི་དཔལ་ལྡན་སྔོན་མེད་རི་བོང་ཅན། །རྩོད་པའི་དུས་སུ་སྐྱེས་པ་དྲི་མ་དང་བྲལ་གང་ཞིག་གྲགས་པ་རྫོགས་པ་ལེགས་པའི་བློ། །རྟག་ཏུ་མུ་སྟེགས་ཅན་གྱི་མཐུག་པའི༌[^4274]མུན་པ་ལས་རྒྱལ་ཤེས་རབ་རི་བོང་ཅན་གྱི་མཐར། །གྲགས་པའི་ཤེས་རབ་འཛིན་མཁས་དམན་པའི་ཚོགས་འཇོམས་ཤཱཀྱའི་འོད་ནི་གསལ་ལྡན་པ། །ཡང་དག་བསྟན་བཅོས་ཚུལ་གྱི༌[^4275]རབ་ཏུ་རྒྱས་པའི་པདྨ་གསལ་བར་བྱེད་ཅིང་ཐམས་ཅད་དུ། །སྐྱེས་བུ༌[^4276]ཤིན་ཏུ་རྣམ་དག་གྲགས་པའི་རྗེས་འགྲོ་གང་ཞིག་ཉི་མའི་གཤེས་གཉེན༌[^4277]ལ་བརྟེན་པའོ།། །།

[Block 4200 [VERSE]]
ཚིགས་བཅད་སྟོང་ཕྲག་བཅུ་བཞི་ནི། །
འདི་ཡི་ཚད་དུ་ཤེས་བྱ་སྟེ། །

[Block 4201]
དཔལ་ལྡན་རྒྱལ་ཆེན་ཐམས་ཅད་ཀྱིས།[^4278] །རྒྱལ་སྲིད་བྱེད་དུས་འདི་བྱས་སོ། །

[Block 4202]
འདུལ་བ་མདོའི་འགྲེལ་པ་བཅོམ་བརླག་མ་ཞེས་བྱ་བ། ཡུལ་བཅོམ་བརླག་གི་འཕགས་པ་གཞི༌[^4279]ཐམས་ཅད་ཡོད་པར་སྨྲ་བའི་རྩོད་པ་པ་ཆེན་པོ་རྣམས་ཀྱི་ཁྱུ་མཆོག་བསྟན་བཅོས་དུ་མ་མཛད་པ་གཞུང་འབུམ་ཕྲག་བཅོ་བརྒྱད་ལ་ཁ་ཏོན་མཛད་པའི་སློབ་དཔོན་ཡོན་ཏན་འོད་ཀྱིས་མཛད་པ་རྫོགས་སོ།། །།

[Block 4203 [HEADING]]
### འགྱུར་བྱང། ^b-2-0

[Block 4204]
འདི་ནི་དཔལ་ས་ཉིའི༌[^4280]གཙུག་ལག་ཁང་ཆེན་པོར་རྗེ་བཙུན་དམ་པ་རྒྱལ་པོ་ཆེན་པོའི་ཡང་ཆེན་པོ་དབང་ཕྱུག་དམ་པ་དཔལ་ཚུལ་ཁྲིམས་ཉི་མའི་ལྷ་རབ་ཏུ་རྒྱས་པར་གྱུར་པ་རྣམ་པར་རྒྱལ་བའི་རྒྱལ་སྲིད་ཀྱི་ལོ་ལ་བྲིས་པ་ཡིན་ནོ། །

[Block 4205]
གང་འདི་འདུལ་བའི་སྡེ་སྣོད་སྟོང་ཕྲག་ཉི་ཤུ་རྩ་ལྔ་ལས་ལྷག་པའི་འབུམ་ཕྲག་གཅིག་གི་དོན་གསལ་བར་བྱེད་པ་རང་གི་རྣམ་པར་བཤད་པ་ཞེས་བྱ་བ་ལོ་ཙཱ་བ་ཤཱཀྱའི་དགེ་སློང་ཚུལ་ཁྲིམས་འབྱུང་གནས༌[^4281]ཀྱིས་བསྒྱུར་བའི་བསོད་ནམས་གང་དེས་མཁན་པོ་དང་སློབ་དཔོན་དང་ཕ་དང་མ་སྔོན་དུ་འགྲོ་བར་བྱས་པའི་མ་ལུས་པའི་སེམས་ཅན་གྱི་ཕུང་པོས་བླ་ན་མེད་པའི་ཡེ་ཤེས་ཀྱི་འབྲས་བུ་ཐོབ་པར་གྱུར་ཅིག། །
--- END BLOCKS ---
