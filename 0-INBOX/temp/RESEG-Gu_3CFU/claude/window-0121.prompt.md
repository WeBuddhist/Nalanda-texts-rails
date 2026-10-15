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
[Block 4236]
དེ་ལྟར་ཡང་མེད་པ་ཉིད་ལ་ལྟུང་བ་མེད་ཅེས་བྱ་བ་འདིར་སྐྱེས་པར་རིག་པར་བྱའོ། །

[Block 4237]
མཐོ་གང་གི་སྤང་བའོ།། །།

[Block 4238]
ཅི་ཞིག་བྱས་ན་བལ་ཐོགས་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཁྱེར་བ་མེད་ན་དཔག་ཚད་གསུམ་ལས་ལྷག་པར་ལུག་གི་བལ་ཁྱེར་ནའོ། །

[Block 4239]
ཡོད་ན་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱེར་བ་མེད་ན་དཔག་ཚད་གསུམ་ལས་འདས་པར་ཁུར་བ་ཡོད་པ་ལ་ཁུར་བ་ཉིད་དུ་བརྩམས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4240]
འགྲོ་བ་ནི་གཉིས་སུ་གསུངས་ཏེ། ལྟུང་བ་དང་བཅས་པ་དང་། ལྟུང་བ་མེད་པའོ། །

[Block 4241]
དེ་ལ་ལྟུང་བ་དང་བཅས་པ་ནི་བལ་ཐོགས་པ་དང་། དགེ་སློང་མ་དང་ལྷན་ཅིག་ལམ་དུ་འགྲོ་བ་དང་། དགེ་སློང་མ་དང་། ལྷན་ཅིག་གྲུར་འཇུག་པ་དང་། སྐྱེས་པ་མེད་པར་ལམ་དུ་འགྲོ་བ་དང་རྐུན་མ་དང་ལྷན་ཅིག་ལམ་དུ་འགྲོ་བའོ། །

[Block 4242]
དེ་ལ་ལྟུང་བ་མེད་པ་ནི་ཡང་ཡང་ཟ་བ་དང་། འདུས་ཤིང་ཟ་བ་དང་། ཁྲུས་བྱེད་པའོ། །

[Block 4243]
དེ་ལ་ལྟུང་བ་མེད་པ་ནི་དཔག་ཚད་ཕྱེད་དོ་ཞེས་འོག་ནས་འབྱུང་ངོ་། །དེའི་ཚད་ལྟུང་བ་ལ་བསྟན་པའི་ཕྱིར། ལམ་དུ་འགྲོ་བ་ནི་རྒྱང་གྲགས་ཀྱི་བདག་པོ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དམག་ལ་ལྟ་བའི་ཕྱིར་འགྲོ་བར་བྱ་བ་ལ་སོགས་པ་ལས་རྣམ་པར་བཅད་པའི་ཕྱིར་འདིར༌[^2896]ལམ་གྱི་ཚིག་གོ། །

[Block 4244]
གང་ཞིག་ཆུའི་ལམ་ནས་འགྲོ་བ་ནི་འདི་ཡིན་ཏེ་གྲུས་གང་ཡིན་པའོ། །

[Block 4245]
དེ་བས་ན་འདི་དང་འགྲོ་བའི་དོན་དུ་ལམ་བཟུང་བས་འཕངས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 4246]
དེ་ལྟར་ན་གྲུའི་ལམ་གྱིས་སོང་བ་དང་། ཆུའི་ལམ་གྱིས་སོང་བ་ཞེས་བྱ་བ་ནི་གྲགས་པའོ། །

[Block 4247]
དེ་བས་ན་རྐུན་མ་དང་ལྷན་ཅིག་གམ་སྐྱེས་པ་མེད་པར་བུད་མེད་དང་ལྷན་ཅིག་གྲུ་གཅིག་གི་ནང་དུ་འགྲོ་བར་མི་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 4248]
འདི་ནི་ཤིན་ཏུ་ཡང་སྐྱོན་དང་ལྡན་པ་ལམ་དུ་འགྲོ་བ་ལས་ཤིན་ཏུ་གསང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4249]
གླེང་གཞི་ལས་མི་འབྱུང་བས་འདིར་ཐ་དད་པའི༌[^2897]ཚིག་ནི་གྲུབ་པ་མ་ཡིན་ཞེས་བྱ་བ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 4250]
ཁྲུས་ལ་ནི་ཆོ་ག་འདི་མི་རིགས་པས་མ་གྲུབ་པའི་ཕྱིར་གྲུར་འགྲོ་བ་ལ་ཁྲུས་ལ་འོངས་པ་ཉིད་ལ་ཡང་ཡང་ཟ་བ་ལ༌[^2898]འདིར་ལྷག་པོར་མེད་པར་དེའི་དབང་གིས་ཀྱང༌[^2899]ཉམ་ཆུང་བ་དང་ཤིན་ཏུ་གྲགས་པ་དག་ལ་ཚོགས་སུ་ཟ་བ་ལ་འདིར་ཡོད་པ་ཡིན་ནོ། །

[Block 4251]
རྒྱུ་མཚན་ནི་སྦྱིན་པ་པོ་གཅིག༌[^2900]མ་གྲུབ་པའོ། །

[Block 4252]
བལ་ཐོགས་པའི་བསླབ་པའི་གཞི་གཞན་ཡོད་པས་ལྷག་པོར་གྱི་གླགས་མེད་པའོ། །

[Block 4253]
མཚན་ཉིད་བརྗོད་པ་ཉིད་ཀྱི་ཕྱིར་མདོ་འདི་ལ་ཐམས་ཅད་དུ་དབང་བྱས་པ་ཉིད་དོ། །

[Block 4254]
འདིའི་དམིགས་ཀྱིས་བསལ་བ༌[^2901]ནི་དཔག་ཚད་ཕྱེད་ཀྱི་ལམ་ཞེས་བྱ་བ་ནི་རྒྱང་གྲགས་ཀྱི་ཐ་མར་ཡོངས་སུ་རྫོགས་པ་ཉིད་འགྲོ་བའི་མཚན་ཉིད་ལ་འདི་ཙམ་རྫོགས་པ་ལ་ལྷག་པོར་རམ། དེ་འདིར་དེ་དང་ལྷན་ཅིག་སྐྱེས་པའི་རྣམ་པར་རིག་པ་ལ་དངོས་གཞི་རྒྱང་གྲགས་རེ་རེ་གཞན་དང་གཞན་ཞེས་བྱ་བ་འདིའི་བྱེད་པའོ། །

[Block 4255]
ཕྱེད་དུ་ན་སྦྱོར་བའོ་ཞེས་བྱ་བ་ནི་རྒྱང་གྲགས་ཀྱི་ཕྱེད་ཀྱི་བདག་པོ་ཉིད་དུ་སོང་ན་སྦྱོར་བར་འགྱུར་ཏེ། དེ་ཙམ་དུ་སོན་ན་སྦྱོར་བ་ཡོངས་སུ་རྫོགས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4256]
འདི་ནས་བརྩམས་ཏེ། སྦྱོར་བ་ཡོངས་སུ་རྫོགས་པའི་མཚན་ཉིད་དུ་གྱུར་པ་ཉིད་དོ། །

[Block 4257]
མདུན་དུ་ནི་ན་སྨད་པ་མེད་པ་ཉིད་དང་ན་སྨད་པའི་མདུན་ནས་ཉེས་བྱས་མེད་པ་འདི་ནས་བརྩམས་ཏེ་རྫོགས་པ་ཉིད་ལ་འདི་བྱེད་པའོ། །

[Block 4258]
འདིར་གཞུང་ནི་རྒྱང་གྲགས་ཕྱེད་དུ་སོན་པར་གྱུར་ན་ཉེས་བྱས་ཀྱི་ལྟུང་བར་འགྱུར་རོ། །

[Block 4259]
རྒྱང་གྲགས་སུ་སོན་ན་སྤང་བའི་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4260]
རྫུ་འཕྲུལ་གཞན་བས་ནམ་མཁའ་ལ་འགྲོ་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི། རྫུ་འཕྲུལ་དང་བཅས་པས་ནམ་མཁའ་ནས་འགྲོ་ན་ལྟུང་བ་མེད་དོ། །

[Block 4261]
རྣམ་པ་གཞན་གྱིས་ནམ་མཁའ་ནས་འགྲོ་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4262]
སྤྲུལ་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལས་ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲ་ནི། ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^2902]པའི་ཕྱིར་རོ། །

[Block 4263]
འདི་ཡང་རྫུ་འཕྲུལ་དང་བཅས་པར་འགྲོ་བ་ཞེས་བྱ་བ་དེའི་ཕྱིར༌[^2903]ལྟུང་བ་མེད་པའི་སྐབས་ཡོད་པ་ལ་རྩོམ་པ་འདིའོ།། །།

[Block 4264]
འདི་ཡང་མི་རིགས་པ་མ་ཡིན་ཏེ། །དེའི་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་ཡང་དག་པར་ལྡང་བར་བྱེད་པ་མངོན་པར་བརྩོན་པ་སྤྲུལ་པ་ལ་ཡོད་པའི་ཕྱིར་བརྒྱུད་ནས་འབྱུང་བའི་ཡོད་པས་མཚན་ཉིད་པ་ནི་མ་ཡིན་ནོ། །

[Block 4265]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 4266]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས༌[^2904]ནམ་མཁའ་ལས་བལ་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར། རྫུ་འཕྲུལ་གྱིས་ཁྱེར་ན་ནི་ལྟུང་བ་མེད་དོ། །

[Block 4267]
རྣམ་པ་གཞན་གྱིས་ཁྱེར་ན་ནི་ཉེས་བྱས་སོ། །

[Block 4268]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་སྤྲུལ་པས་རུང་བར་བགྱིས་པ་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སུ་འགྱུར་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4269]
ཞྭ་དང་ལྷམ་སྒྲོ་གུ་ཅན་དང་སྟོད་ཀོར་ནང་ཚངས་ཅན་དང་། རྒྱ་ཅང་དང་ལྕག་པོད༌[^2905]དང་ཤུར༌[^2906]བུ་ཕྲེའུ་ལ་སོགས་པའི་དོན་དུ་དེ་ཙམ་དག་ལ་ནི༌[^2907]ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཞྭ་ལ་སོགས་པའི་ཚད་ལྡང་བའི་བལ་རྣམས་ལ་ཞྭ་ལ་སོགས་པའི་ཚད་དུ་ཁྱེར་བ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4270]
རྒྱང་གྲགས་ཀྱི་ཚད་བརྗོད་པར་བྱ་སྟེ། རྡུལ་ཕྲ་རབ་དང་། རྡུལ་ཕྲ་མོ་དང་། ཆུ་དང་། ལྕགས་དང་། རི་བོང་དང་། ལུག་དང་། གླང་དང་། ཉི་ཟེར་གྱི་རྡུལ་དང་། སྲོ་མ་དང་། ཤིག་དང་། ནས་དང་། སོར་རྣམས་ནི་སྔ་མ་དྲུག་ལ་ཕྱི་མའོ། །

[Block 4271]
སོར་བཞི་དྲུག་ལ་ཁྲུ་གང་ངོ་། །ཁྲུ་ཕྱེད་དང་བཞི་ལ་ནི་མིའི་སྲིད་དོ། །

[Block 4272]
ཁྲུ་བཞི་ལ་གཞུ་གང་ངོ་། །དེ་ལྔ་བརྒྱ་ལ་རྒྱང་གྲགས་སོ་ཞེས་བྱ་བ་ནི་ནས་འབྲུ་དྲུག་གློས་གཞིབས་པ༌[^2908]ལ་སོར་གཅིག་ཏུ་རིག་པར་བྱ་སྟེ། འདིར་གཞུང་ནི་ནས་དྲུག་ལ་སོར་མོའི་ཚིགས་གཅིག་གོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4273]
སོར་མོ་གང་ཡིན་པའི་ཚིགས་ཀྱི་ཚིགས་ལ་ཞེས་བྱ་བ་ནི་འདི༌[^2909]བསྟན་པའི་དོན་དུ་འདིར་ཚིགས་ཀྱི་ཚིགས་རིག་པར༌[^2910]བྱའོ། །

[Block 4274]
འཇིགས་པ་དང་བཅས་པ་ཉིད་དུ་ནགས་ཁྲོད་དགོན་པ་བསྟེན་པ་ལ་དགེ་སློང་མས་དགོན་པར་གནས་པར་མི་བྱ་བ་གསུངས་པས་མངོན་པར་བསྟེན་པར་བྱ་བའི་དགོན་པའི་ངོ་བོ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དགོན་པའི་དང་པོ་ནི་དེའི་མཐའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྒྱང་གྲགས་ཀྱི་མཐར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4275]
ལུས་ཀྱིས༌[^2911]ཁུར་མི་བསྐུར༌[^2912]རོ་ཞེས་བྱ་བ་ལ་ལུས་ཀྱི་ཁུར་ཞེས་བྱ་བ་ཕྲག་གདང་གི་ཁུར་ལ་བྱ་སྟེ། ཕྲག་གདང་གིས༌[^2913]ཁུར་བསྐུར་བར༌[^2914]མི་བྱའོ། །
--- END BLOCKS ---
