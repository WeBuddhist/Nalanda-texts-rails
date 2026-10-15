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
དགེ་སློང་ཞེས་སྨོས་པ་ནི་མཚོན་པ་ཙམ་དུ་ཟད་དེ་ཆོས་འདི་ལ་རབ་ཏུ་བྱུང་བ་ཐམས་ཅད་ཀྱང་སྤྱིར་བསྡུ་བའོ།[^3070] །དེ་ལ་ཐ་ཆད་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྤངས་པ་དེ་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4517]
གཞན་དུ་ན་ཡང་ལྷུང་བཟེད་ཐ་ཆད་གང་ཡིན་པ་དེ་འདི་ལ་སྦྱིན་པར་བྱའོ། །

[Block 4518]
འོན་ཏེ་དེ་ཉིད་དགེ་འདུན་དེ་ལ་ཐ་ཆད་འབྱུང་བར་འགྱུར་ན་དེ་ཉིད་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་དོ། །

[Block 4519]
བྲིམ་པས་བསྙིགས་པར༌[^3071]བྱའོ་ཞེས་བྱ་བ་ནི་ཐ་ཆད་དེ་དགེ་འདུན་དེ་ལས་སོ། །

[Block 4520]
བྱེད་པ་པོ་ཇི་ལྟ་བུས་བྲིམ་པས་དགེ་འདུན་ལས་ཐ་ཆད་དེ་བསྙིགས་པར༌[^3072]བྱ་ཞེ་ན་དེའི་ཕྱིར་བསྐོས་པས༌[^3073]སོ། །

[Block 4521]
དེས་སང་དེ་བྱེད་པར་འགྱུར་བ་ན་ཚོགས་ཀྱི་དུས་སུ་དགེ་འདུན་ལ་གཞལ་བར༌[^3074]བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཞེས་བྱ་བ་ནི་བྲིམ་པ་ལ་བྱའོ། །

[Block 4522]
དེ་ཞེས་བྱ་བ་ནི་བསྐོས་པས་སོ། །ཇི་སྐད་གཞལ་བར༌[^3075]བྱ་ཞེ་ན། དེའི་ཕྱིར་ཚེ་དང་ལྡན་པ་དག་བདག་སང་ལྷུང་བཟེད་འབྲེལ་པ་མེད་པ་འདྲིམ་པར་འགྱུར་གྱིས་ཁྱེད་ཅག་རང་རང་གི་ལྷུང་བཟེད་དག་ཐོགས་ལ་དགེ་འདུན་གྱི་ནང་དུ་གཤེགས་པར་མཛོད་ཅིག་ཅེས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྷུང་བཟེད་འབྲེལ་པ༌[^3076]མེད་པ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་འདི་ཨུ་ན་དྷ་ཏེ་འབྲེལ་པ་མེད་པ་དང་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་མ་ཡིན་པ་དང་།[^3077] འཆག་པར་བྱ་བ་མ་ཡིན་པ་དང་། འབངས་བཞིན་དུ་སྤང་བ་དང་བཅས་པ་ཞེས་བྱ་བ་འདི་ནི་འདིའི་མིང་ངོ་། །འཁོད་པའི་དོན་དུ་ནན་ཏན་བྱའོ་ཞེས་བྱ་བ་ནི་བསྐོས་པ་ཉིད་ཀྱིས་གཉིས་ཀ་དག་གི་སྔ་རོལ་དུ་ཞེས་བྱ་བའི་མདོ་འདི་ལས་ཇི་སྲིད་དུ་བསྐོས་པ་ལ་ཞེས་བྱ་བ་དབང་དུ་བྱ་བ་ཉིད་ལེན་པ་དང་མ་བླངས་པ་ཞེས་བྱ་བ་འདི་དག་ལ་ཤུགས་ཀྱིས་ལེན་པ་པོའི་བྱེད་པ་པོ༌[^3078]ཉིད་དུ་རྟོགས་པར་བྱའོ། །

[Block 4523]
བསྔགས་པ་བརྩམ་ཞིང་དབུལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། དེས་ལྷུང་བཟེད་ཀྱི་དབང་དུ་བྱ་བ་སྟེ། རྣམ་པ་ཇི་ལྟ་བུའི་བསྔགས་པ་བརྩམ་ཞིང་དབུལ་བར་བྱ་ཞེ་ན་དེའི་ཕྱིར་གནས་བརྟན་ལྷུང་བཟེད་འདི་ནི་ཤིན་ཏུ་གསལ་བ་དབྱིབས་ལེགས་པ་ལོངས་སྤྱད༌[^3079]བཟོད་པ་ལགས་ཀྱི་གལ་ཏེ་བཞེད་ན་སྣོམས༌[^3080]ཤིག་ཅེས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་འདི་ལྟ་བུ་ཉིད༌[^3081]ཐམས་ཅད་ལ་བརྗོད་པར་བྱ་འམ་ཞེ་ན་དེའི་ཕྱིར་ཡོན་ཏན་ཇི་ལྟ་བ་བཞིན་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ནི་དཔེ་ཡིན་ནོ། །

[Block 4524]
གང་ལ་ཡོན་ཏན་གང་དང་གང་ཡོད་པ་དེ་དང་དེ་དག་ལ་བརྗོད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4525]
འདོད་ན་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འདོད་པ་ཡོད་ན་གཟུང་བར༌[^3082]བྱའོ། །

[Block 4526]
མེད་ན་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4527]
བར་དུ་ཆོད་པས་བླངས་པ་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་གཅིག་གིས་བར་དུ་ཆོད་པ་ཉིད་ནི་བརྟེན༌[^3083]པའོ། །

[Block 4528]
གང་གི་ཕྱིར་གསུམ་པས་བླངས་པ་ན་དུ་མས་བར་དུ་ཆོད་པ་ཉིད་ལ་ནི་ཤིན་ཏུ་ཡང་བླང་བར་མི་བྱ་བ་ཉིད་དུ་བྱའོ་ཞེས་བྱ་བ་འདི་བརྗོད་དོ། །

[Block 4529]
སློང་བ་ཡོད་ན་ཚིག་གཉིས་པ་ལ་ནི་མི་སྦྱིན་ཞིང་གསུམ་པ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཚིག་གསུམ་པ༌[^3084]ལ་ནི་མི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 4530]
འབྲེལ་པ་མེད་པར་ཤིན་ཏུ་འདའ་བར་བྱེད་ན་ཞེས་བྱ་བ་འདི་ཙམ་ནི་འདིར་རྒྱུ་མཐོང་བ་ཡིན་ཏེ། དེ་བས་ན་གསུམ་པའི་ཚིག་ལ་ཅི་ནས༌[^3085]ཀྱང་སྦྱིན་པར་བྱ་བ་ཉིད་དོ། །

[Block 4531]
ལྟུང་བ་བྱུང་བ་ལ་སྤང་བར་མི་བྱ་བ་ཉིད་དང་བྱིན་གྱིས་བརླབ་པར་མི་བྱ་བ་ཉིད་དག་གོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབ་པར་ཡང་མི་བྱ་བ་ཉིད་དང་། སྤང་བར་མི་བྱ་བ་ཉིད་ཅེས་བྱ་བ་འདི༌[^3086]ལྟར་བསྐོས་པས་ལྟུང་བར་འགྱུར་བ་ལ་གོ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4532]
ཉེ་བར་སྤྱོད་པ་ལ་མ་ཆག་གི་བར་དུ་དལ་བུ་དལ་བུས་སྤྱོད་ཅིག་ཅེས་སོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ༌[^3087]ལ་གོ་བར་བྱ་ཞེས་པ་ཉིད་དུ་རིམ་གྱིས་དལ་བུ་དལ་བུས་ཡོངས་སུ་ལོངས་སྤྱད་པར་བྱ་སྟེ། ཇི་སྲིད་དུ་ནམ་ཆག་པའི་མཐར་ཐུག་གི་བར་དུ་བཟུང་ནས་ཞེས་བྱ་བ་འདིས་འདི་བསྡུས་པའོ། །

[Block 4533]
འདིར་འཆང་བའི་ཉེས་པ་སྐྱེས་པ༌[^3088]མེད་དོ་ཞེས་བྱ་བའི་ཆོ་ག་འདི་ཉིད་ཀྱི་ཕྱིར་རྟོགས་པར་བྱའོ། །

[Block 4534]
དེ་གཉིས་ཀས་ཀུན་དུ་སྤྱད་པར་བྱའོ་ཞེས་བྱ་བ་ལ་གཉིས་ཀས་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་དག་གིས་སོ། །

[Block 4535]
དེས་ཞེས་བྱ་བ་ནི་ལྟུང་བ་བྱུང་བས་དེ་ཀུན་དུ་སྤྱད་པར་བྱའོ། །

[Block 4536]
འདིའི་ཆད་པའི་ལས་ནི་འདི་ལྟ་སྟེ། ལྷུང་བཟེད་གཞན་ལ་དད་པས་གཅོད་པའི་དོན་དུའོ།[^3089] །དེ་ལ་ཡོ་བྱད་ཆེས་བཟང་པོ་ངེས་པར་སྦྱར་བར་བྱའི༌[^3090]ཞེས་བྱ་བ་ནི་གང་འདི་ཐ་ཆད་འདི་ལྟ་བུ་བྱུང་ནས་འདི་ལ་སྦྱིན་པ་དེ་ལ་ལྷུང་བཟེད་ཀྱི༌[^3091]སྣོད་དང་ཁ་གཡོགས་ལ་སོགས་པ་ཡོ་བྱད་ཆེས་བཟང་པོ་ངེས་པར་སྦྱར་བར་བྱ་བའོ།[^3092] །སྤྱོད་པ་ནི་ཆེས་ཡང་བའོ་ཞེས་བྱ་བ་ནི་བསོད་སྙོམས་བླང་བ་ལ་སོགས་པ་ལ་ངེས་པར་སྦྱར་བར་བྱའོ། །

[Block 4537]
ཟས་ཀྱི་བྱ་བ་ཉིད་ལ་ནི་མི་བྱ་བ་ཁོ་ནའོ་ཞེས་བྱ་བ་ནི་ཟས་བཟའ་བའི་བྱ་བ་བསྒྲུབ་པ་ཉིད་ལ་ནི་འདི་ངེས་པར་སྦྱར་བར་མི་བྱ་བ་ཁོ་ནའོ། །

[Block 4538]
ལྷུང་བཟེད་ཚོལ་བའི་སྤང་བའོ།། །།

[Block 4539]
གང་དུ་འཐག་ཏུ་འཇུག་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རིན་ཐང་མེད་པར་བསྒོ་བས་སམ་གཞན་གྱིས་ཀྱང་འཐག་ཏུ་བཅུག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱིམ་པ་ཉེ་དུ་མ་ཡིན་པ་ཞེས་བྱ་བ་སྔར་བསྟན་པའི་རིན་ཐང་མེད་པར་ངག་གིས་བསྒོ་བས་འཐག་ཏུ་བཅུག་ན་དངོས་གཞིའི་ལྟུང་བར་འགྱུར་རོ། །

[Block 4540]
རང་གིས་བསྒོ་བ་གཅིག་པུར་མ་ཟད་ཀྱི་འོན་ཀྱང་ཕོ་ཉ་ལ་སོགས་པ་གཞན་གྱིས་ཀྱང་འཐག་ཏུ་བཅུག་ན་དངོས་གཞིའི་ལྟུང་བ་ཁོ་ནའོ། །

[Block 4541]
ཕན་ཚུན་བརྒྱུད༌[^3093]ནས་བྱེད་དུ་བཅུག་ན་ན་སྨད་པའི་ཚིག་ལ་དམིགས་ཀྱིས་བསལ་བའོ། །

[Block 4542]
འདིར་གླེང་གཞི་ལས་འདི་ཤེས་པ་ཡིན་ཏེ། བླངས་པའི་སྐུད་པ་ཉིད་འདི་ལ་མ་ཆོག་པར་སོང་བ་སྟེ། དགེ་སློང་གིས༌[^3094]ཉེ་དུ་ལ་སྐུད་པ་བླངས་ནས་ཐ་ག་པ་ཉེ་དུ་མ་ཡིན་པ༌[^3095]ལ་འཐག་ཏུ་བཅུག་ནས་སློང་བ་པོ་དེ་ལ་ནི་ལྟུང་བ་མེད་ལ་ཐ་ག༌[^3096]པ་ཉེ་དུ་མ་ཡིན་པ་ལ༌[^3097]འཐག་ཏུ་བཅུག་པ་ནི་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4543]
གཞན་ཉིད་དང་བཅས་པ་ལ་ནི་དེ་ལ་བྱས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གཞན་དང་ལྷན་ཅིག་ཏུ་གང་གིས་གང་བྱེད་པ་དེ་ནི་དེས་མ་བྱས་པར་གྱུར་པ་མ༌[^3098]ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4544]
ཉེ་དུ་དང་ཉེ་དུ་མ་ཡིན་པ་གཉིས་ཀ་ལས་འཐག་ཏུ་བཅུག་ན་ཡང་ཉེ་དུའི་ཕྱིར་ལྟུང་བ་མེད་ཀྱི་ཉེ་དུ་མ་ཡིན་པའི་དབང་གིས་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ། །

[Block 4545]
བདག་ཉིད་དང་ཉེ་དུ་མ་ཡིན་པར་བཅས་པས་བདག་ཉིད་ལ་དགོས་པ་ཉིད་བྱ་བའི་ཕྱིར་དགེ་སློང་བཟོ་བྱེད་པ་ལ་ཉེས་བྱས་ཞེས་བྱ་བ༌[^3099]གསུངས་པ་གང་ཡིན་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 4546]
རིན་བྱིན་པ་དང་མ་བྱིན་པ་གཉིས་ཀ་ལ་འཐག་ཏུ་བཅུག་ན་ཡང་ཆོ་ག་འདི་རྣམ་པར་གཞག་པའོ། །

[Block 4547]
འདི་ཡང་འདིས་བྱེ་བྲག་ཡོངས་སུ་མ་བཟུང་བའི་ཕྱིར་བསྡུས་པའོ། །

[Block 4548]
འཐག་ཏུ་བཅུག་པའི་སྤང་བའོ།། །།

[Block 4549]
འཐག་པ་སྐྱེད་པ༌[^3100]དང་འཕེལ་བར་འགྱུར་བའི་སྤང་བའི༌[^3101]ཡན་ལག་གང་དག་བྱེད་པ་པོར་གྱུར་པ་དེ་དག་གང་ཞེ་ན། དེའི་ཕྱིར་བཏགས༌[^3102]པར་བྱ་བ་བསམས་པ༌[^3103]ལས་བྱུང་བ་ཉིད་དོ་ཞེས་ཏེ། བསམ་པ་དགོས་པ་འདི་ལ་ཡོད་པས་ན་སེམས་པའོ། །

[Block 4550]
དེའི་དངོས་པོ་སེམས་པ་ལས་བྱུང་བའོ། །

[Block 4551]
དེའི་ཞེས་བྱ་བ་འདིས་ནི་ལྟུང་བ་བཟུང་བའོ། །

[Block 4552]
ཁོ་ལག་ཆེ་བ་ཉིད་དང་འབྲས་བཟང་བ་ཉིད་ལ་ཐ་ག་པ་ངེས་པར་སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་ནི་རིང་བ་ནི་འདི་ཙམ་ཞེང་ཆེ་བ་ནི་འདི་ཙམ་ཞེས་བྱ་བ་ཁོ་ལག་ཆེ་བ་ཉིད་ལ་འདི་ངེས་པར་སྦྱར་བར་བྱས་པའོ། །

[Block 4553]
གོས་གཞན་འདོད་པ་མ་ཡིན་པ་ལ་སྦྱིན་པ་པོས་དོན་གྱིས་བསྒྲུབ་པའོ། །

[Block 4554]
གང་ཞིག་ཁོ་ལག་ཆེ་བ་ཉིད་ལ་ཚེ་དང་ལྡན་པ་ཐ་ག་པ་ཉིད་ལ་གོས་འདི་ཞེང་ཆེ་བ་དང་ཁྲུན་རིང་བ་དང་ཐར་གྱིས་ཞག་པ་དང་ཐག་རན་བཟང་བ་ལེགས་པར་གྱིས་ཤིག་ཅེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4555]
ཐག་རན་བཟང་བ་དང་བྱེར་ཟུག་སྙོམས་པ་དང་ཤས་བཟང་བ་དང༌[^3104]སང་སེང་མེད་པ་ཞེས་བྱ་བ་རྣམ་པར་བཤད་པར་སྦྱར་རོ།། །།
--- END BLOCKS ---
