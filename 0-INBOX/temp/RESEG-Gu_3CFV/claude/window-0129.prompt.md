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
[Block 4516]
དེ་ལྟ་བས་ན་མི་སྲིད་པ་ལས་གཞན་དུ་འགྱུར་བ་ཉིད་ལ་དེ་རྗེས་སུ་གནང་བའོ། །

[Block 4517]
སྒྲ་མི་འདོད་ན་མདོར་བསྡུས་པས་སོ་ཞེས་བྱ་བ་ནི། གང་དག་འདིར་སྦྱར་བ་དེ་དག་སྒྲ་མི་འདོད་ན་མདོར་བསྡུས་པས་གསོ་སྦྱོང་བྱ་བའོ།[^3146] །དེ་ཙམ་ཡང་ན་བྱིན་གྱིས་བརླབ་པོ་ཞེས་བྱ་བ་ནི་མདོར་བསྡུས་པས་བྱ་བ༌[^3147]ལ་སྒྲ་ཇི་ཙམ་འབྱུང་བར་འགྱུར་བའི་སྒྲ་དེ་ཙམ་ཡང་འགྲོན་པ་དག་གིས་མི་འདོད་ན་སོ་སོ་ནས་བྱིན་གྱིས་བརླབ་པར་བྱ་སྟེ། འཁོར་དང་བཅས་པ་ལ་སྒྲ༌[^3148]ལས་གྲོལ་བ་མེད་པས་སོ་སོ་ནས་ཞེས་བྱ་བར་བསྒྲུབ་པར་བྱའོ། །

[Block 4518]
དད་པ་ཅན་དང་གཙོ་བོ་དག་དགའ་བར་འགྱུར་བལྟ་ན་ཆོ་ག་རྗེས་སུ་བསྒྲུབ་པ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་དོ། །

[Block 4519]
དྲུང་དུ་གསོ་སྦྱོང་བྱས༌[^3149]པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། གནས་མལ་གྱི་གཞིར་གཏོགས་པ་ལས་འདིར་གཉིས་པོ་དེ་དག་གྲངས་སོ། །

[Block 4520]
ཕོངས་པའི་ཚེ་ཁྱིམ་པའི་དྲུང་དུ་བཤགས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཆོམ་རྐུན་པ་དག་ལ་དེ་སྐད་གསུངས་པ་ཡིན་མོད་ཀྱི། ཁྱིམ་པ་གཞན་དག་ལ་ཡང་རུང་བ་ཉིད་ཡིན་པའི་ཕྱིར་འདི་རྣམ་པར་གཞག་གོ། །

[Block 4521]
དེ་ལྟ་བས་ན་ཀྱལ་ཀ་ཅན་ལ་སོགས་པ་དང་རྩེ་རྒོད་ལ་སོགས་པ་ལ་རྒུད་པ༌[^3150]དེ་ཐོབ་པ་དང་དྲུང་དུའོ། །

[Block 4522]
དེ་ལྟ་བས་ན་དེ་དང་ཉེ་བར་འབྲེལ་ལོ། །

[Block 4523]
རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་མ་རྫོགས་པའི་དྲུང་དུ་ཡང་དེ་དག༌[^3151]ནི་ཤིན་ཏུ༌[^3152]ཉེས་པ་མེད་པས་དེ་ལས་ཤེས་པར་བྱའོ། །

[Block 4524]
དེ་ལ་ཆོ་ག་རྗེས་སུ་བསྒྲགས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་ལའོ། །

[Block 4525]
ཆོ་ག་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བའི་བསླབ་པ་རྣམས་ལ་ཡང་ངོ་། །རྒྱལ་པོ་ལ་གོ་བར་བྱ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། ཆོ་ག་དག་རྗེས་སུ་ཐོབ་པར་བྱ་བ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་དེ། འདིར་རྒྱལ་པོ་ནི་དཔེ་ཙམ་དུ་ཟད་དེ་གང་དུ་ཁྱིམ་གྱི་བདག་པོ་ལ༌[^3153]ཆོས་དང་ལྡན་པའི་དོན་འགྲུབ་པར༌[^3154]དེ་ལ་རིག་པར་བྱའོ། །

[Block 4526]
སྡོམ་པ་མཆོག་དང་འབྲེལ་བར་བྱ་བ་དམན་པ་ལ་བླངས་ཤིང་གཟུང་བ་ཉེ་བར་མི་བྱའོ། །

[Block 4527]
ཆོ་ག་ཐོས་པར་མི་བྱའོ་ཞེས་བྱ་བ་དེ་དང་ལྡན་པར་རིག་པར་བྱའོ། །

[Block 4528]
གཞན་མ་རྫོགས་པ་ལ་མི་འཆགས་པ༌[^3155]མེད་དོ་ཞེས་བྱ་བ་ལ། གཞན་ཞེས་བྱ་བ་ནི་འདོན་པ་གཉིས་པ་ལ་སོགས་པའོ། །

[Block 4529]
སྡེ་ཚན་ཐམས་ཅད་འདོན་པར་བརྩམས་པ་མ་རྫོགས་པའོ། །

[Block 4530]
རེག་ནའོ་ཞེས་གང་ཞིག་གསུངས་པ་ནི་མ་རྫོགས་པ་དེ་ལ་མི་ཆགས་པ་མེད་དོ། །

[Block 4531]
འོན་ཀྱང་ཉེས་བྱས༌[^3156]ཙམ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4532]
ཆོས་མ་ཡིན་པ་མི་བྱའོ་ཞེས་གང་ཞིག་གསུངས་པ་དེ་འདིར་གསོ་སྦྱོང་གི་ཆོས་ཞེས་བྱ་བར་བརྗོད་པར་བྱ་སྟེ། གདོན་པར་བྱ་བ་དང་དེའི་ཚད་དང་དུས་དང་འདོན་པར་བྱེད་པ་རྣམས་དེ་ཁོ་ན་བཞིན་ཉེ་བར་མ་བཟུང་བ༌[^3157]ནི་འདིར་ཆོས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ཁོ་ན་བཞིན་ཞེས་བྱ་བ་ནི་བསྟན་པར་བྱས་ནས་དང་པོ་ལ་སོགས་པ་ཉིད་དེ་ཁོ་ན་བཞིན་ཉེ་བར་མ་བཟུང་བ་ནི་སོ་སོར༌[^3158]ཐར་པ་ལས་གཞན་ཡང་བསྟན་པར་བྱས་ཏེ། བསྟན་པ་ཉིད་རྗེས་སུ་མ་བཟུང་བ་ནི་གླེང་གཞི་མི་འདོན་ཅིང་གཞན་མ་བརྗོད་པ་རྣམས་ནི༌[^3159]ཐོས་པ་བསྒྲགས་པས་སྒྲུབ་པར་མི་བྱེད་པ་རྣམས་བསྟན་པར་བྱ་སྟེ། འདི་ཙམ་ཉིད་རྗེས་སུ་མ་བཟུང་བའོ། །

[Block 4533]
གསོལ་བ་མ་བྱས་པ་ལ་ནི་རྩེ་གཅིག་ཏུ་རིག་པར་བྱ་སྟེ། གྲོས་མ་བྱས་པ་དག་ལ་དེ་བྱེད་པ་ནི་གང་ཞིག་མི་ཤེས་པ་ཞེས་བྱ་བ་སྟེ། གསོ་སྦྱོང་གི་དུས་ལས་དུས་གཞན་དུ་བྱེད་པ་ནི་དུས་ཉེ་བར་མ་བཟུང་བའོ། །

[Block 4534]
གང་ཟག་གང་དག་གི་དབང་དུ་གསོ་སྦྱོང་བྱེད་པའི་དབང་དུ་བསྙེན་པར་རྫོགས་པ་དང་བཅས་པ་དང་ལྟ་བ་དང་ཚུལ་ཁྲིམས་དག་གིས་རིགས་མཐུན་པ་དེ་རྣམས་ལས་གཞན་པས་བྱེད་པའོ། །

[Block 4535]
ཡང་ན་འདོན་པར་མི་བྱེད་པ་དང་མི་འཛིན་པའོ། །

[Block 4536]
གནས་དེ་ནས་འགའ་ཡང་མ་སོང་བ་ཉིད་ཡིན་ན་ངེས་པ་ཡིན་ནོ་ཞེས་སྔར་གང་བསྟན་པ་དེ་ལ་དེའི་ངོ་བོ་བསྟན་པའི་ཕྱིར། ཐོས་པའི་ཉེ་འཁོར་ལས་འདས་པ་ཉིད་ནི་སོང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལས་སོ། །

[Block 4537]
གསོ་སྦྱོང་གི་གཞི་དང་འབྲེལ་པ་རྣམ་པར་འབྱེད་པ་ལ་སོགས་པའི་སྐབས་སོ། །

[Block 4538]
གསོ་སྦྱོང་གི་གཞི་རྫོགས་སོ།། །།

[Block 4539 [HEADING]]
## དབྱར་གྱི་གཞི། ^12-0

[Block 4540]
དབྱར་གནས་པར་ཁས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དུས་ཇི་སྲིད་དུ་ཞེ་ན། དེའི་ཕྱིར་ཟླ་བ་གསུམ་དུའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4541]
ཉི་མ་གང་ལ་དེ་རྣམས་དེ་སྲིད་དུ་ཁས་བླང་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཚེས་བཅུ་དྲུག་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4542]
ཟླ་བ་གང་གི་ཞེ་ན་དེའི་ཕྱིར། དབྱར་ཟླ་འབྲིང་པོ་ཉའི་ཕྱི་དེ་ཉིན་པར་གྱིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དབྱར་ཟླ་འབྲིང་པོ་ཉའི་ཕྱི་དེ་ཉིན་པར་ཞེས་བྱ་བ་ནི་དབྱར་འབྲིང་པོ་ཚེས་བཅུ་དྲུག་གི་ཚེས་སུ་གྱུར་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4543]
དབྱར་ཉེ་བར་སྒྲུབ་པ་དབྱར་ཟླ་འབྲིང་པོར་སྒྲུབ་པ༌[^3160]ཞེས་བྱ་བའི་ཚིག་གང་ཞིག་ཡང་དག་པར་བྱེད་པའོ། །

[Block 4544]
དབྱར་ཞེས་བྱ་བ་ནི་དེར༌[^3161]ཉེ་བར་སྒྲུབ་པའོ་ཞེས་བྱ་བ་དེའི་དོན་ཏོ། །

[Block 4545]
གང་ཟག་ཉེ་བར་འགྲོ་བ་མ་ཡིན་པ་རྒྱུ་མཚན་ཉིད་ཀྱིས་སོ་སོར་ཉེ་བར་གནས་པས་དབྱར་ཞེས་བྱ་བའོ། །

[Block 4546]
དབྱར་ཟླ་ཐ་ཆུངས༌[^3162]ཉའིའོ་ཞེས་བྱ་བ་ནི་དེ་མ་ཐག་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4547]
དེའི་མཐར་དབྱར་ཟླ་ཐ་ཆུངས༌[^3163]ཉའི་ཕྱི་དེ་ཉིན་པར་ཞེས་བྱ་བ་ནི། ཉའི་དེ་མ་ཐག་པ་ནི་ཚེས་བཅུ་དྲུག་སྟེ། སྟོན་ཟླ་ར་བའི་ཚེས༌[^3164]ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4548]
ཞག་བཅུའམ་ཟླ་བ་ཕྱེད་ཀྱིས་འབྱུང་བར་འགྱུར་བ་ཉིད་ན་གཙུག་ལག་ཁང་བྱི་དོར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་པར་ཁས་བླངས་པ༌[^3165]ཞེས་བྱ་བའི་སྐབས་ཀྱིས་རྟོགས་པའོ། །

[Block 4549]
ཁ་ཅིག་ལས་ནི་བདུན་ནམ་བརྒྱད་ནའོ་ཞེས་བྱ་བ་ནི་ལུགས་ཁ་ཅིག་ལས་ཞེས་བྱ་བར་དགོངས་སོ། །

[Block 4550]
ཉི་མ་སྔ་མ་ལ་གནས་མལ་བསྡོག་གོ་ཞེས་བྱ་བ་ནི། ཁས་བླངས་པ་དེའི་ཉི་མ་སྔ་མ་སྟེ་ཚེས་བཅུ་དྲུག་པའི་སྔ་མ་ལ་ཚེས་བཅོ་ལྔ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4551]
ཁྲིའུ་དང་ཆོལ་ཟངས་ཡན་ཆད་དོ་ཞེས་བྱ་བ་ནི་ཐ་ན་ཁྲིའུ་དང་ཆོལ་ཟངས་ཀྱི་བར་ཡན་ཆད་ཀྱང་དེའི་ཉིན་མོ་བསྡོག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4552]
དེ་སྟོབས་པ་བསྐོ་བར༌[^3166]བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་སྒྲས་ནི་གནས་མལ་སྟོབས་པ་ཡང་བསྡུས་པའོ། །

[Block 4553]
མི་ནུས་ན་དུ་མའོ་ཞེས་བྱ་བ་ནི་གཅིག་གིས་གནས་མལ༌[^3167]སྟོབས་པར་མི་ནུས་པ་ན། གནས་མལ་སྟོབས་པ་དུ་མ་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4554]
བསྐོས་པའི་འོག་ཏུ་དེས་ཅི་ཞིག་བྱ་ཞེ་ན། དེའི་ཕྱིར། དེས་དྲི་དག་གིས་བསྐུས་པའི་ཚུལ་ཤིང་གཟེབ་ཀྱི་སྤྲོག་མར་རས་དཀར་པོ་བཏིང་བས་དཀྲིས་པ་དག་རྒན་རིམས༌[^3168]སུ་བཞག༌[^3169]ནས། ཚེ་དང་ལྡན་པ་དག་གནས་འདི་ན་ཁྲིམས་སུ་བཅས་པ༌[^3170]འདི་དང་འདི་ཡོད་དེ། ཁྱེད་ཅག་ལས་གང་ཁྲིམས་སུ་བྱ་བ་འདི་དང་འདིས་གནས་པར་སྤྲོ་བ་དེས་ནི་ཚུལ་ཤིང་ལོང་ཤིག༌[^3171]ཁྱེད་ཅག་ལས་སུས་ཀྱང་དབྱར་དགེ་འདུན་གྱི་ནང་དུ་འཁྲུག་ལོང་བསྐྱེད་པར་མི་བྱའོ། །

[Block 4555]
ཁྱེད་ཅག་ལས་གང་གིས་འགའ་ཞིག་ལས་ཅུང་ཟད་ཤེས་པ་དེས་ང་སྨྲོས་ཤིག །ཁྱེད་ཅག་ལས་གང་དབྱར་གྱི་ནང་དུ་དགེ་འདུན་ལས་འཁྲུག་ལོང་སྐྱེད་པར༌[^3172]འགྱུར་བ་དེ་ལ་དགེ་འདུན་གྱིས་ཕྱིས་ཉེ་བར་བརྟག་པར་དགོངས་སོ་ཞེས་དགེ་སློང་རྣམས་ལ་གོ་བར་བྱའོ་ཞེས་སྨོས་ཏེ། དེས་ཞེས༌[^3173]བྱ་བ་ནི་གནས་མལ་སྟོབས་པས་སོ། །
--- END BLOCKS ---
