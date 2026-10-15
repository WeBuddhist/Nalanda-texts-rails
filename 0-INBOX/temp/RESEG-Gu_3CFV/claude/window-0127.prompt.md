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
[Block 4446]
རྫུ་འཕྲུལ་དང་སྒྱུ་མ་བྱས་པ་དག་ཀྱང་དེ་ལྟར་གྱུར་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། ཐ་སྙད་མ་ཡིན་པ་ཉིད་དུ་བྱས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4447]
ཟླ་བ་དང་། ཉི་མ་དང་། སྐར་མའི་འོད་དང་དབའ་ཀློང་གི་རླབས་དག་ཀྱང་མི་བརྟན་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། བརྟན་པ་ཞེས་བྱ་བ་འདི་ཉིད་ཀྱིས་འདི་རྣམས༌[^3103]མ་ཡིན་པར༌[^3104]དགག་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4448]
མཚམས་དང་མ་འབྱར་བ་ལ་དེའི་མཚན་མ་ཉིད་མ་ཡིན་ནོ། །

[Block 4449]
དེ་ལྟ་བས་ན་འདིར་འོད་ཟེར་རྣམས་མངོན་པར་བརྟེན་པ་ཟླ་བ་ལ་སོགས་པ་ལ༌[^3105]ཡང་མ་ཡིན་ཏེ། འདིར་དོགས་པའི་སྐབས་མེད་པའི་ཕྱིར་རོ། །

[Block 4450]
འདིར་དེའི་ཁྱད་པར་གྱི་ངོ་བོས་ཟླ་བ་ལ་སོགས་པ་ཉེ་བར་བཟུང་བའོ། །

[Block 4451]
དེ་བཞིན་དུ་དབའ་ཀློང༌[^3106]གི་རླབས་འགྲམ་དུ་འབྱུང་བ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 4452]
མཚམས་སུ་ཆུ་ནི་མཚམས་གཞན་དང་འདྲའོ་ཞེས་བྱ་བ་ནི། འདི་ལ་མཚམས་ཀྱི་ནང་དུ་ཆུས་ཆོད་ན་མཚམས་ཐ་དད་པ་ཉིད་དེ་ཞེས་བྱ་བ་འདི་ལ་དེའི་མཚམས་ཀྱི་ནང་དུ་ལྟུང་བ་གཅིག་པུར་མ་ཟད་དེ། འོན་ཀྱང་མཚམས་ཉིད་ཐ་དད་པ༌[^3107]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4453]
འདི་ནི་གནས་བྱིན་གྱིས་བརླབས་པ་སྟེ། གང་ཞིག་མཚམས་ལ་མངོན་པར་བརྟེན་པ་ཡིན་གྱི། ཆུ་ལ་ནི་འདི་རྣམས་ཀྱི་གནས་ཉིད་དུ་བྱིན་གྱིས་བརླབ་པར་བྱ་བའི་གནས་ཉིད་ཡོད་པ་མ་ཡིན་ཏེ། ཇི་ལྟར་བསྟེན་པ༌[^3108]ལའང་ཡོད་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གནས་པར་གྱུར་པ་མ་ཡིན་པ་ཉིད་ཀྱིས་སོ། །

[Block 4454]
མཚམས་ལ་དེ་དང་ལྡན་པ་ཉིད་ལ་ཇི་སྲིད་དུ་ཆུས་མི་འཁྱེར་བ་དེ་སྲིད་དུ་མཚམས་ཀྱི་ཡུལ་མ་ཡིན་ནོ། །

[Block 4455]
ཆུ་མེད་པར་གྱུར་ན་མཚམས་དེ་ལས་སྐྱེས་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4456]
བར་དུ་ཆོད་ན་གཅིག་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། གང་དུ་ཕྱོགས་གཅིག་གིས་ཀྱང་འབྲེལ་པ༌[^3109]མེད་པར་དེར་མཚམས་གཅིག་པ་ཉིད་ལས་སྐྱེས་པར་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4457]
མཚམས་གཅིག་ལ་གནས་པ་མ་ཡིན་པ་དེ་ལྟར་རྣམ་པར་བཅད་པའི་སའི་ཆར་གནས་པ་དུ་མའི་ཚོགས་རྣམ་པར་བཅད་ནས་ཅིག་ཅར་མཚམས་བཅད་པ་ལས་བླང་བ་དེ་ལྟ་བས་ན་འདི་ལདེ་ལྟར་བྱེད་པའོ། །

[Block 4458]
གལ་ཏེ་ཟམ་པ་བརྟན་པོ་ཡོད་ན་དེ་ཡུལ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་བཙུན་པ་ཆབ་ཀྱི་མཚམས་ལས་འདར་རུང་ངམ། ཉེ་བ་འཁོར་མི་རུང་ངོ་། །གལ་ཏེ་ཟམ་པ་བརྟན་པོ་ཡོད་ན་ནི་རུང་ངོ་ཞེས་གསུངས་སོ། །

[Block 4459]
དེ་བཞིན༌[^3110]ན་ཡང་ཕྱིར་བྱས་ན་ནི་རྗེས་སུ་འཇུག་གོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་ཟམ་པའོ། །ཇི་ལྟ་བུ་ཞིག་པ་ཡང་ཕྱིས་བྱ༌[^3111]ཞེ་ན། དེའི་ཕྱིར་སྦྱོར་བ་མ་བཏང་བ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡང་ཕྱིར་བྱ་བ་གང་ལ་སྦྱོར་བ་མ་བཏང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4460]
དུས་ཇི་སྲིད་དུ་སྦྱོར་བ་མ་བཏང་བ་ཉིད་ཀྱང་ཕྱིར་བྱས་ནས་རྗེས་སུ་འཇུག་ཅེ་ན། དེའི་ཕྱིར༌[^3112]ཞག་བདུན་ཕན་ཆད་ནི་མི་འཇུག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། །མི་འཇུག་གོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4461]
ནམ་མཁའ་ནི་བར་དུ་ཆད་པར་གྱུར་པ་ཡིན་པས་དེ་ལ་ཡོད་པ་ཉིད་ཀྱི༌[^3113]ཐ་སྙད་ཀྱང་མེད་ན་འབྲེལ་པ་ལྟ་ག་ལ་ཡོད་ཅེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་ནམ་མཁའ་ལའོ། །

[Block 4462]
ས་དང་དེ་དང་འབྲེལ་པའི་རང་གི་ཆ་ཡང་རུང་སྟེ། འདི་ལ་གཉིས་ཀའི་ཆ་ལ་ཡང་མཚམས་གཅིག་གིས་འབྲེལ་པ་མ་ཡིན་ནོ། །

[Block 4463]
འདིར་གནས་ཁང་གི་ནང་ན་འདུག་པའི་ནམ་མཁའ་ཡང་མཚམས་ལ་འཇུག་པ་མ་ཡིན་ཏེ། མཚམས་གཅིག་པ་ཉིད་ཀྱང་མ་ཡིན་ཏེ་དེ་འདིར་དེ་ལྟ༌[^3114]བས་ན་དེ་བྱེད་པའོ། །

[Block 4464]
འདིར་གཞུང་ནི་བཙུན་པ་ནམ་མཁའ་ལ་མཆིས་པ་དག་དང་། དོག་ས་ལ་མཆིས་པ་དག་ལྷན་ཅིག་ལས་བགྱིར་རུང་ངམ། ཉེ་བ་འཁོར་མི་རུང་ངོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དང་། གང་ཡངས་དང་དེ་དང་འབྲེལ་བ་རྣམས་ཀྱིས་མི་རུང་བ་ཉིད་དེ་ལ་ནི་བསྡུས་པའོ། །

[Block 4465]
དབུས་ནས་དཔག་ཚད་ཕྱེད་དང་གསུམ་གྱི༌[^3115]མཐའ་ལས་ལྷག་པར་མཚམས་བཅད་པ་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི། དཔག་ཚད་ཕྱེད་དང་གསུམ་གྱི་མཐའ་ཚུན་ཆད་དུ་ཞེས་བྱ་བ་གང་ཞིག་སྨོས་པ་གང་ཞིག་མ་གྲགས་པ་ཡང་དེ་ལས་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བ་མེད་པ་ཙམ་ཞེས་བྱ་བ་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 4466]
བཙུན་པ་མཚམས་ཆེན་པོའི་ཚད་ཇི་ཙམ་ལགས། ཉེ་བ༌[^3116]འཁོར་དཔག་ཚད་ཕྱེད་དང་གསུམ་མོ། །

[Block 4467]
བཙུན་པ་དཔག་ཚད་ཕྱེད་དང་གསུམ་ཕན་ཆད་མཚམས་སུ་རུང་ངམ། ཉེ་བ༌[^3117]འཁོར་མི་རུང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4468]
དེར་གང་ཞིག་ཚད་འདི་བརྗོད་པ་ནི་ཞུ་བ་ལས་གསུངས་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 4469]
འོག་དང་སྟེང་དུ་སྲ་བ་དང་འབྲེལ་པ་ལ་གཞི་དང་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། དཔག་ཚད་ཕྱེད་དང་གསུམ་གྱི་མཐའ་ཡན་ཆད་དང་མན་ཆད་ས་དང་རྡོ་དང་རྩིག་པ་དང་ཤིང་ལྗོན་པ་དང་། [^3118]ཤིང་ལ་སོགས་པའི་སྲ་བ་དང་འབྲེལ་པའི་རྫས་གང་ཡིན་པ་ལ་ནི་དེའི་རང་བཞིན་ཅན་གྱི་འབྲེལ་པ་ལ་གཞི་དང་ལྡན་པ་བཞིན་དུ་མཚམས་ལ་ཡོད་པའོ། །

[Block 4470]
མཚམས་ཆེན་པོའི་དབང་དུ་བྱས་ནས་ཚིག་དེའོ། །

[Block 4471]
གཞན་དུ་ཇི་ལྟར་བྲིས་པ་བཞིན་དུ་ཞེས་རྟོགས་པར་བྱའོ། །

[Block 4472]
དེ་ལྟར་ཡང་དཀྱིལ་འཁོར་ལ་ནི་ཚད་གཞན་དང་འབྲེལ་པ་གང་ཡིན་པ་དེ་ལ་དེར་ཞུགས་པ་མ་ཡིན་ནོ། །

[Block 4473]
དེ་ཡོངས་སུ་སྤོངས་པས༌[^3119]ཡང་མཚམས་ལས་སྐྱེས་པར་རིག་པར་མི་བྱའོ། །

[Block 4474]
ས་གཞི་མཚམས་མ་བཅད་པ་ཉིད་དུ་མི་འབྲལ་བའི་གནང་བ་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི། བཅོས་མའི་གནས་སུ་མི་འབྲལ་བའི་གནང་བའི་ཡུལ་ཡིན་པ་དེ་བས་དེ་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 4475]
ཞུ་བ་ལས་འདི་དང་པོར་བྱས་ཏེ་དེས་ནི་དེ༌[^3120]མི་ཞིག་གོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 4476]
བཅད་པ་ཞིག་ན་ཞིག་གོ་ཞེས་བྱ་བ་ལ། ཞིག་པ་ནི་མཚམས་བཅད་པ་ལས་གྲོལ་བའོ། །

[Block 4477]
དེ་ཞིག་ན་མི་འབྲལ་བའི་གནང་བ་ཞིག་གོ། །

[Block 4478]
དེས་ནི་དེ་མི་ཞིག་ག༌[^3121]ཞེས་བྱ་བ་ནི། མི་འབྲལ་བའི་གནང་བ་ཞིག་པ་དེས་ནི་མཚམས་བཅད་པ་དེ་མི་ཞིག་པའོ། །

[Block 4479]
མཆོད་རྟེན་དང་། གཙུག་ལག་ཁང་དང་། གཙང་ཁང་ཕྱུར་བུ་དང་འཁོར་ས་དང་། གསོ་སྦྱོང་གི་གནས་དག་ཏུ་ཕྱག་དར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། འདིར་ཕྱག་དར་བྱ་བ་ནི་གནས་ཁང་ངམ་ཁྱམས་སམ་རྫིང་བུའི་ཚད་ཙམ་ཞིག་ཕྱགས་ན་ཕྱག་དར་བྱས་པ་ཉིད་དུ་ཤེས་པར་བྱ༌[^3122]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4480]
འདི་ནི་མ་མོ་ལས་ཉེས་བྱས་ཏེ། ནད་པས་ཞེས་བྱ་བ་དང་པོར་བྱ་སྟེ། གནས་ཞེས་བྱ་བའི་མཐར་ཐུག་པ་དང་། ཕུལ་བ་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པའི་མདོ་འདི་ནི་ཞུས་པ༌[^3123]ལས་སོ། །

[Block 4481]
དགེ་འདུན་ལ་འདུན་པ་ལ་སོགས་པ་ཕུལ་བ་ནི་ཕུལ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། གང་ཟག་ལ་འདུན་པ་ལ་སོགས་པའི་ཚིག་ལྷུག་པ་ལས་ཕུལ་བ་གསུངས་པ་ཡིན་ཏེ། དེ་བས་ན་དགེ་འདུན་ལ་ཕུལ་བ་ཉིད་ལ་མ་ཕུལ་བ་ཉིད་དུ་ལ་ལ་ཞིག་དོགས་པར་འགྱུར་པ་དེ་བས་ན། དེ་བཟློག་པའི༌[^3124]དོན་དུ་འདི་གསུངས་པ་ཡིན་ནོ། །

[Block 4482]
དེ་ལས་གང་ཡང་རུང་བས་དེ་བརྗོད་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ལས་ཞེས་བྱ་བ༌[^3125]ནི་དགེ་འདུན་ལས་སོ། །

[Block 4483]
གང་དུ་འདི་ལ་ཕུལ་བ་དེ་ཡོད་པར་འགྱུར་རོ། །

[Block 4484]
དེ་བརྗོད་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལ་འདུན་པ་ལ་སོགས་པ་ཕུལ་བ་དེའོ། །

[Block 4485]
འོ་ན་བརྗོད་པ་འདི་དོན་མེད་པ་ཁོ་ན་ཡིན་ཏེ། འདིར་སྨྲ་བ་པོ་འབྱུང་བ་ནི་མི་རིགས་པ་ཁོ་ན་སྟེ། གང་གི་ཕྱིར་གོ་བ་བསྐྱེད་པའི་དོན་དུ་འདི༌[^3126]ནི་མངོན་སུམ་ཉིད་དུ༌[^3127]ཕུལ་བ་པོས་གོ་བ་བསྐྱེད་དོ་ཞེ་ན། དེ་ནི་བདེན་མོད་ཀྱི་འོན་ཀྱང་ཆོ་ག་ལ་འཇུག་པ་ལ་ཕུལ་བ་མ་བྱས་པ་ཉིད་དོ། །
--- END BLOCKS ---
