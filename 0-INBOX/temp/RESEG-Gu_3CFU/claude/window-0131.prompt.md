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
[Block 4586]
དེའི་རང་གིས་བྱིན་པ༌[^3119]ཞེས་བྱ་བ་འདིར་གཟུང་བར༌[^3120]བྱ་བ་མ་ཡིན་ནོ། །

[Block 4587]
རྐུ་བའི་སེམས་མེད་པ་ལ་རང་གིས་བྱིན་པ༌[^3121]གཞན་གྱིས༌[^3122]དབྲོག་པ་ལ་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་རོ། །

[Block 4588]
ཡོད་པ་ལ་ནི༌[^3123]མ་སྦྱིན་པར་ལེན་པར་འགྱུར་རོ། །

[Block 4589]
འདིར་ཚེ་དང་ལྡན་པ་ཀུན་དགའ་བོ་ལ་རང་གི་བློས་ཞུགས་པར་གྱུར་ཏེ། ཁྱོད་ལ་བདག་གིས་མི་སྦྱིན་ཞེས་བྱ་བར༌[^3124]གསུངས་པའི་ཕྱིར་རོ། །

[Block 4590]
དེ་གོས་ཉིད་ཡིན་ནའོ་ཞེས་བྱ་བ་ནི་གླེང་གཞི་ལས༌[^3125]དབྲོག་པར་བྱ་བ་ཐམས་ཅད་ལ་དགེ་སློང་གི་ཡོ་བྱད་ལ་དངོས་གཞིའི་ལྟུང་བ་བྱེད་པ་ཉིད་དུ་གསུངས་ཏེ། ཤིན་ཏུ་ལྕི་བ་ཡང་འདིར་འཇུག་པ་སྤངས༌[^3126]པ་ཉིད་ཙམ་ནི་འདིར་ལྷག་པ་སྟེ་ལྟུང་བ་ལ་བྱེ་བྲག་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 4591]
འདིར་ནི༌[^3127]སླར་སྦྱིན་པར་བྱ་བ་ཉིད་སྤང་བ་ཉིད་དེ་འདི་ཡང་ལྟུང་བ་མེད་པ་ལ་ཡང་དངོས་པོ་ལ་གཞན༌[^3128]ཉིད་ཀྱི་ཕྱིར་འདིར་བྱད་པའི་རིགས་པ་ཉིད་དེ་དེ་བས་ན་དཔེ་འདི་ནི་གླེང་གཞིའི་དབང་གིས་བཟུང་བའོ། །

[Block 4592]
དགེ་སྦྱོང་གི་ཡོ་བྱད་ཐམས་ཅད་ལ་ཡང་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 4593]
དེའི་འམ་དེས་བསྐོས་པའི་ལུས་སམ་ངག་བསྡུས་པ་འམ་ཐ་དད་པ་དག་གིས་དབྲོག་པའི་དོན་དུ་ཞུགས་པ་ལྟ་བུ་ནི་བྱེད་པ་པོ་ཡིན་ཞེས་བྱ་བ་ལ། བསྡུས་པ་འམ་ཐ་དད་པ་ཞེས་བྱ་བ་ནི་འདི་དག་ལ་སོ་སོར་ལྟུང་བ་མེད་དེ་འདིར་གཉིས་པོ་འདི་དག་ཉིད་ལ་ཡོད་པ་ཉིད༌[^3129]ཅེས་བྱ་བ་འདིའི་འདི་བསྟན་པའོ། །

[Block 4594]
དེའི་ཞེས་བྱ་བ་ནི་ལྟུང་བ་འབྱིན་པར་བྱེད་པའི་འོ། །

[Block 4595]
འདིར་གཞན་བྱེད་དུ་འཇུག་པ་འམ་བྱས་པ་ལས་བྱེ་བྲག་ཅེས་བྱ་བ་འདི་བརྗོད་པའོ། །

[Block 4596]
འདིར་ཁ་ན་མ་ཐོ་བ་ཇི་ལྟ་བུ་གང་གི༌[^3130]ཕྱིར་བྱེད་པ་པོ་དག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ལུས་ལས་ཐ་དད་པའི་དངོས་པོར་གྱུར་པ་མཐར་ཐུག་པ་ན་མཐའིའོ། །

[Block 4597]
སྦྱོར་བ་ལ་ནི་ཉེས་བྱས་ཀྱིའོ༌[^3131]ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་དབྲལ་བར་བྱ་བ་བསྟན་པ་གང་ཡིན་པ་དེའི་ལུས༌[^3132]གང་ཡིན་པ་དེ་ལས་ཐ་དད་པའི་མཐར་ཐུག་པ་ལ་དངོས་གཞིའོ། །

[Block 4598]
སྦྱོར་བ་ལ་ནི་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4599]
དེའི་ཕྱིར་སྦྱིན་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་དབྲོག་པ་དེའོ། །

[Block 4600]
འདིར་ནི་འཇུ་བར་འོས་པ་ཉིད་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནི་གཉིས་ཀ་བསྟན་པའོ། །

[Block 4601]
འདིར་གཞུང་ནི་ལྷག་མ་ཡོད་པ་ཐམས་ཅད་སླར་བྱིན་ཅེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4602]
འདི་ལ་རང་གི་དོན་ཉིད་ཡན་ལག་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདིར་དགེ་སློང་ལ་བྲལ་བ་ཙམ་ནི་གཙོ་བོ་སྟེ་བདག་ཏུ་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 4603]
རང་གི་དོན་དང་གཞན་གྱི་དོན་དུ་ཞེས་བྱ་བ་ཁྱད་པར་ལ་མི་བསྟེན་པའི༌[^3133]དབྲོག་པའོ། །

[Block 4604]
དེ་བས་ན་གཞན་ངེས་པར་སྦྱོར་བས་བྲལ་བ་ལ་འདིར་དངོས་གཞིའི་ཁ་ན་མ་ཐོ་བ་ཉིད་ཅེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 4605]
རྫོགས་པར་མ་བསྙེན་པ་ལ༌[^3134]ནི་སྐྲོད་པ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་འདིར་སྐབས་མ་ཡིན་ཞེས་བྱ་བས་འདིར་ཞེས་བྱ་བའི་སྒྲ་འདི་ལ། འདི་ཞེས་བྱ་བ་ཡོངས་སུ་གྱུར་པ་ལ་འབྲེལ་པའོ། །

[Block 4606]
འདི་སྐྲོད་པ་ནི་དཔེར་ན༌[^3135]གཙུག་ལག་ཁང་ནས་སྐྲོད་པ་ལ་དགེ་སློང་མ་ལ་སོགས་པ་རྣམས་ལ་སྐྲོད་པར་བྱེད་པ་ཉིད་དང་བསྐྲད་པར་བྱ་བ་ཉིད་ལ་ཉེས་བྱས་སུ་གསུངས་སོ། །

[Block 4607]
ཁྱིམ་པ་རྣམས་ཀྱང་སྐྲོད་པར་བྱེད་པ་ནི་བསོད་ནམས་མ་ཡིན་པ་མང་དུ་འཕེལ་བར་འགྱུར་བ་དེ་བཞིན་དུ་འདི་ཡང་འདི་རྣམས་ལ་ཁ་ན་མ་ཐོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4608]
དེ་ལྟར་ཡང་འདིར་དགེ་སློང་མ་ལ་སོགས་པ་རྣམས་ལ་དབྲོག་པ་ཉིད་ལ་གཞུང་ནི་དགེ་སློང་མ་དང་དགེ་ཚུལ་དང་དགེ་ཚུལ་མས་ནི་ཉེས་བྱས་ཀྱི་ལྟུང་བར་འགྱུར་རོ། །

[Block 4609]
ཁྱིམ་པ་དང་ཁྱིམ་པ་མོས་ནི་བསོད་ནམས་མ་ཡིན་པ་མང་དུ་འཕེལ་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4610]
འཕྲོག་པ་ནི་རྣམ་པ་གསུམ་སྟེ། རང་གི་ཉིད་སེལ་བར་གྱུར་པ་དང་གཞན་ནི་རྣམ་པ་གཉིས་ཏེ། བློ་གྲོས་ངན་པས་བྱས་པ་དང་། རིགས་དོན་གྱི་དབང་དུ་བྱས་པའོ། །

[Block 4611]
དེ་ལ་བློ་གྲོས་ངན་པ་ནི་བློ་གྲོས་འདི་ནི་ལེགས་པ་མ་ཡིན་ཏེ། མཆོག་མ་ཡིན་པ་དང་ལྷག་པའི་ཆོས་སུ་གྱུར་པ་ནི་མ་ཡིན་ནོ། །

[Block 4612]
དེ་ལྟར་གང་ཞིག་གྲངས་སུ་འགྲོ་བ་དེས་སོ། །

[Block 4613]
འདི་ལྟ་སྟེ་ཡི་ཆད་པར་གྱུར་ཅིག །གནོད་པར་གྱུར་ཅིག །མཐུ་བརྟན༌[^3136]པར་གྱུར་ཅིག །སྟོབས་ཉེ་བར་གནས་པར་གྱུར་ཅིག་ཅེས༌[^3137]འདིས་འདི་བྱ་སྟེ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ལྟ་བུ་སྟེ། དེ་ལ་ཅི་ཐམས་ཅད་རྣམ་པ་གསུམ་པོ་འདིར་རྟོགས་པར་བྱ་བ་འམ་འོན་ཏེ་ཐམས་ཅད་མ་ཡིན། གང་དུ་འདིར་ཅི་ཞིག་རྟོགས་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་འདི་ཉིད་བརྗོད་པར་བྱ་བ་སྟེ། དེའི་ཕྱིར་རང་གི་ཉིད་སེལ་བར་གྱུར་པའི་འཕྲོག་པ་འདིར་བསྡུས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཞེས་བྱ་བ་བསླབ་པའི་གཞི་ལའོ། །

[Block 4614]
དབྲལ་བར་བྱ་བའི་ཆོས་གོས་ཀྱི་ཐ་མ་ལས་དེ༌[^3138]བསལ་བར་གྱུར་པ་འདིར་འཕྲོག་པ་བཟུང་བ༌[^3139]གང་ཡིན་པ་དེའི་དོན་དུ་འཇུག་པ༌[^3140]ལ་འདིར་སྦྱོར་བ་ལ་ཉེས་བྱས་སུ་བརྗོད་དོ། །

[Block 4615]
མཐར་ནི་དངོས་གཞིའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4616]
འདིར་གཞུང་ནི་དགེ་སློང་གོས་འོན་ཅིག་ཁྱོད་ལ་མི་སྦྱིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4617]
བློ་གྲོས་ངན་པས་བྱས་པ་ནི་རྗེས་སུ་འཕྲོད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཡི་ཆད་པར་གྱུར་ཅིག་ཅེས་བྱ་བ་བློ་གྲོས་ངན་པས་འཕྲོགས་པ༌[^3141]གང་ཡིན་པ་བྱེད་པར་གྱུར་པ་ནི་རྗེས་སུ་འཕྲོད་པ་ཉིད་ཡིན་ནོ། །

[Block 4618]
རྗེས་སུ་འཕྲོད་པ་ཉིད་ཀྱི་ཕྱིར་འདིར་ཉེས་བྱས་རྟོགས་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4619]
གནོད་པ་དང་མི་ཕན་པར་བྱེད་པ་ལ་འཇུག་པའི་གེགས༌[^3142]བྱ་བའི་ཕྱིར་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་གནོད་པ༌[^3143]བྱེད་པའི་ཕྱིར་འཇུག་པ་ལས་ཏེ། མི་ཕན་པར་བྱེད་པའི་ཕྱིར་རམ་གེགས་བྱ་བའི་ཕྱིར་འཕྲོག་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 4620]
འདིར་གཞུང་ནི་དོན་གཞན་དང་འདུལ་བའི་ཡོ་བྱད་ཀྱི་ཕྱིར་ནི་ལྟུང་བ་མེད་པའི་ཚིག་ཅེས་བྱ་བའོ། །

[Block 4621]
གཉིས་པོ་འདི་ལས་གཞན་དུ་ལྟུང་བ་འབྱུང་བར་འགྱུར་རོ། །

[Block 4622]
འཕྲོག་པའི་སྤང་བའོ།། །།

[Block 4623]
དགོན་པ༌[^3144]པའི་ཆོས་གོས་གཅིག༌[^3145]ལ་ནི་འཇིགས་པ་དང་བཅས་པ་ཉིད་ཡིན་ན་གྲོང་ཡང་རང་གི་གནས་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་དགོན་པ་ནི་འདིར་གནས་ཏེ་ཞེས་བྱ་བ་ནི་དགོན་པ་པ་ཞེས་བྱ་བའི་ཚིག་གིས་རྟོགས་པའོ། །

[Block 4624]
འདིར་ལོར་མ་ཚང་བ་ཉིད་ནི་འདིའི་བྱེ་བྲག་ཏུ་བྱུང་བ་ཡིན་ནོ། །

[Block 4625]
རྣམ་པར་འབྱེད་པ་ལས་ཀྱང་འདིའི་དོན་གསུངས་ཏེ། ལོ་ཕྱི་མ་ལ་ཉེ་བར་འབྲེལ་པར་འགྱུར་ཏེ། དེ་ནི་འདིར་རྟེན་པ༌[^3146]མ་ཡིན་ནོ། །
--- END BLOCKS ---
