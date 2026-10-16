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
ཞིང་རྨེད་པ་ནི་དཔྱ་དབུལ་བའི་རྩ་བའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4447]
དེ་དག་ལ་ཚོང་ཟོང་སྣ་ཚོགས་ཞེས་བྱ་བ་འདི་སྨོས་ཏེ། མཁར་དང་། ནོར་གྱི་རང་བཞིན་ལས་བརྩམས་པ་སྟེ། སྣ་ཚོགས་པའི་ཚོང་ཟོང་གང་ཡིན་པ་དེ་དག་གོ། །

[Block 4448]
དེ་དག་གི་ཉོ་བ་དང་། འཚོང་བ་ནི་ཉོ་ཚོང་ངོ་། །རྣམ་པ་སྣ་ཚོགས་པའི་ཉོ་ཚོང་བྱེད་པ་ནི་ཚོང་ཟོང་སྣ་ཚོགས་ཉོ་ཚོང༌[^2872]བྱེད་པ་སྟེ། །དེ་ནི་ཚོང་པ་རྣམས་ཡིན་ཏེ། ཡུལ་གཞན་དང་། ཆུ་དང་། ཐང་དང་།

[Block 4449 [VERSE]]
ལེན་དུ་འགྲོ་བའི་དབང་དུ་བྱས་པའོ། །
ཕོ་བྲང་འཁོར་གྱི་མི་ཞེས་བྱ་བ་ནི།
གྲོང་ན་གནས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 4450]
ཤོ་གམ་གཅོད་ཅིང་དཔྱ་དབུལ་བ་ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཤོ་གམ་གཅོད་ཅིང་དཔྱ་དབུལ་བའི་ཐ་མལ་པའི་གྲོང་གི་མི་སྟེ། འདིས་ནི་རྫོང་གི་རང་བཞིན་བསྟན་ཏོ། །

[Block 4451]
ཚོང་པ་རྣམས་ཤོ་གམ་གཅོད་ཅིང་དཔྱ་དབུལ་བ་ཞེས་བྱ་བ་འདིས་ནོར་གྱི་རང་བཞིན་བསྟན་ཏེ། ཚོང་པའི་སྐྱེ་བོ་ཡིན་པའི་ཕྱིར་དེ་བསྲུངས༌[^2873]ན་ནོར་ཡང་བསྲུངས་པར༌[^2874]འགྱུར་ཏེ། ནོར་གྱི་ཚོང་པ་རྣམས༌[^2875]ལ་རག་ལུས་པའི་ཕྱིར་རོ། །

[Block 4452]
དེ་གཉིས་ཀའི་ཕྱོགས་གཅིག་ཏུ་བྱས་ཏེ་ནོར་གྱི་ཕུན་སུམ་ཚོགས་པར་བསྟན་ཏོ། །

[Block 4453]
སྐྱོན་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་བཀའ་ཁྲིམས་ཀྱི་རང་བཞིན་གྱི་དབང་དུ་བྱས་པའོ། །

[Block 4454]
མ་བཀུར་ན་ཞེས་བྱ་བ་ནི་བཀའ་ཁྲིམས་ཀྱིས༌[^2876]མ་བཀུར་བ་སྟེ། མ་བསྟན་པའི༌[^2877]སྐྱོན་བསྟན་ཏོ། །

[Block 4455]
ཡོངས་སུ་མ་བསྐྱངས་པ་དག་དེས་ཡོངས་སུ་མ་བསྐྱངས་པའི་ཕྱིར། གཞན་གྱི་རང་བཞིན་ཡུལ་མི་སྔར་བསྐྱངས་པའི་སྒྲུབ་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4456]
ད་ནི་རྗེས་སུ་གཟུང་བ༌[^2878]དང་། དཔྱ་དབབ་པའི་བསྒྲུབ་པའི་དབང་དུ་བྱས་ནས། དེ་བཞིན་ཚུལ་ལྡན་མཁས་པ་དགེ་བ་དང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གསུམ་སྨོས་སོ། །

[Block 4457]
དེ་ལ་ཕན་གདགས་པ་བསྒྲུབ་པའི་དབང་དུ་བྱས་ནས། དེ་བཞིན་ཚུལ་ལྡན་མཁས་པ་དགེ་བ་དང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། རང་གི་སྐྱེ་བོ་གནས་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། གནས་པ་དང་། རིགས་སོ། །

[Block 4458]
དེ་ལ་གནས་པའི་དབང་དུ་བྱས་པ་ནི་ཚིགས་བཅད་དང་པོ་འདི་ཡིན་ནོ། །

[Block 4459]
ཚུལ་ཁྲིམས་དང་། ཐོས་པ་དང་། རྣལ་འབྱོར་དང༌[^2879]ཚུལ་ཁྲིམས་དང་། ཐོས་པ་དང་། རྣལ་འབྱོར་ཏེ་དེས་དགེ་བ་རྣམས་སོ། །

[Block 4460]
རྣལ་འབྱོར་ཞེས་སྨོས་པས་ནི་ཞི་གནས་དང་། ལྷག་མཐོང་གཟུང༌[^2880]ངོ་། །ཚུལ་ཁྲིམས་ཀྱི་ཞི་གནས་ཀྱི་སྟེང་དུ༌[^2881]བཤད་ཅེས་བྱ་བ༌[^2882]ཞི་གནས་དང་ལྷག་མཐོང་ཉིད་དུ་བསྟན་ཏེ་དེས་དགེ་བ་རྣམས་སོ། །

[Block 4461]
དགེ་བ་དེ་དག་རབ་ཏུ་མཐོང་བ་འདིས་ནི་རང་གི་དོན་སྒྲུབ་པ༌[^2883]ཕུན་སུམ་ཚོགས་པ༌[^2884]བསྟན་ཏོ། །

[Block 4462]
ཡོན་ཏན་ཆེ་བར་གྲགས་པས་དགེ་བ་རྣམས། །ཞེས་བྱ་བ་འདིས༌[^2885]ནི་གཞན་གྱི་དོན་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 4463]
ཆེ་བར་གྲགས་པ་ཉིད་ནི་ཆེ་བར་གྲགས་པའོ། །

[Block 4464]
ཆེ་བར་གྲགས་པ་དེ་ཉིད་ཡོན་ཏན་ཡིན་པས་དེ་ཉིད་ཀྱི་ཡོན་ཏན་སྒྲོགས་པ་གང་ཡིན་པ་དེ་དག་ནི་ཡོན་ཏན་ཆེ་བར་གྲགས་པའོ། །

[Block 4465]
སྨད་ཅིང་ཡལ་བར་བོར་ན་ཞེས་བྱ་བ་འདིས་ནི་མངོན་དུ་ལྡང་བ་དང་། ཕྱག་འཚལ་བ་དང་། བསྙེན་བཀུར་བ་དང་། རྗེས་སུ་བསྟན་པ་དང་། མཉན་པ་ལ་སོགས་པ་སྤང༌[^2886]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4466]
མཐོ་རིས་འགྲོ་བའི་སྒོ་དང་འགྲོལ་བར༌[^2887]འགྱུར། །ཞེས་བྱ་བ་འདིས་ནི་མངོན་པར་མཐོ་བ་དང་ངེས་པར་ལེགས་བའི་རྒྱུ་དེ་སྐྱེས་བུ་དམ་པ་ལ་བརྙས་ཤིང་སྨད་པ་དང་། མ་བསྐྱངས་པ་དེས་མཐོ་རིས་ཀྱི་སྒོའི་མཚན་ཉིད་དུ༌[^2888]མངོན་པར་མཐོ་བ་དང་འགལ་བ་ཉིད་དོ། །

[Block 4467]
དཔྱ་དབབ་པ་ཞེས་བྱ་བ་དེ་བསྒྲུབ་པའི༌[^2889]དབང་ཏུ་བྱས་ནས། འབྲས་བུ་མ་སྨིན་ཤིང་ལས་གང་འཐོག་པ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་སྨོས་ཏེ་དུས་ལ་མ་བབ་པར་དཔྱ་ཕབ་ཅིང་བླངས་པའི་སྐྱོན་བསྟན་པའི་ཕྱིར། འབྲས་བུ་མ་སྨིན༌[^2890]ཤིང་ལས་གང་འཐོག་པ། །ཞེས་བྱ་བ་ལྟ་བུ་ནི་ཆོས་མ་ཡིན་པས་དཔྱ་ཕབ་པའོ། །

[Block 4468]
ས་བོན་ཆུད་གསོན་ཅེས་བྱ་བ་ལྟ་བུ་ནི་ཡུལ་ཡང་ཕུང་ལ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4469]
རོ་ཡང་དེས་མ་མྱོང་ཞེས་བྱ་བ་ལྟ་བུ་ནི་དེས་ཆོས་མ་ཡིན་པས་དཔྱ་ཕབ་པས་ཕན་མི་ཐོགས་པ་ཉིད་དོ། །

[Block 4470]
སྔར་བསྟན་པའི་སྐྱོན་གྱི༌[^2891]མི་མཐུན་པའི་ཕྱོགས་ཆོས་ཀྱིས་བསྲུངས་པའི་ཡོན་ཏན་བསྟན་པའི་ཕྱིར། དེ་ལྟར་ལྗོན་ཤིང་ཡོན་ཏན་ཕུན་སུམ་ཚོགས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། སྨིན་པའི་བར་དུ་ཡོངས་སུ་བསྐྱངས་ན་སྟེ། ཤིང་ལྟ་བུ་ནི་རྒྱལ་པོས་བསྲུངས་པའི་ཡུལ་ལོ། །

[Block 4471]
ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པའི་འབྲས་བུ་སྟེར་བ་ལྟ་བུ་ནི་ཆོས་དང་། སྲིད་དང་། བདེ་བ་འབྱོར་པར་བྱེད་པ་ལྟ་བུར་སྦྱར་རོ། །

[Block 4472]
བློན་པོ་མཛངས་པ༌[^2892]གློ་བ་ཉེ་བ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་བློན་པོ་དང་། མཛའ་བོའི་སྐྱེ་བོའི་དབང་དུ་བྱས་པ་སྟེ། གློ་བ་ཉེ་བ་ཞེས་བྱ་བ་ནི་དེའི་བློ་དང་མཐུན་པར་འདོད་པའོ། །

[Block 4473]
མཛངས་པ༌[^2893]ཞེས་བྱ་བ་ནི་ལྷན་ཅིག་སྐྱེས་པ་དང་། སྦྱོར་བ་ལས་བྱུང་བའི་ཤེས་རབ་དང་ལྡན་པའོ། །

[Block 4474]
གློ་བ་ཉེ་བ་ཞེས་བྱ་བ་འདིས་ནི་ནུས་པ་བསྟན་ཏོ། །

[Block 4475]
གྲོགས་པོ་སྐྱོན་མེད་ཅེས་བྱ་བ་ནི་འཁྲུལ་པ་མེད་པར་སྤྱོད་པའོ། །

[Block 4476]
བདག་གི་ནང་མི་རྣམས་ཞེས་བྱ་བ་ནི༌[^2894]སྐྱོན་མེད་པ་སྟེ་འཁྲུལ་པ༌[^2895]མེད་པར་སྤྱོད་པའོ། །

[Block 4477]
དགའ་བར་སྨྲ་བས་ཞེས་བྱ་བ༌[^2896]ནི་ཚིག་སྙན་པ་བསྟན་ཏོ། །

[Block 4478]
[^2897]རིམ་གྲོར་བཅས་པའི་བྱ་དགའ་སྩལ་བ་དང་། །[^2898]ཞེས་བྱ་བ་འདིས་ནི་རིམ་གྲོ་དང་བྱ་དགའ་གཉིས་ཏེ།[^2899] དེས་ནི་རིམ་གྲོ་དང་འདི་གསུམ་གྱིས་ནི་བསྡུ༌[^2900]བའི་དངོས་པོ་བསྟན་ཏེ། སྦྱིན་པ་དང་། སྙན་པར་སྨྲ་བ་དང་། དོན་མཐུན་པ་དང་། དོན་སྤྱོད་པ་ལས་དོན་སྤྱོད་པ་ནི་རྒྱལ་པོ་ལ་མེད་པའི་ཕྱིར་མ་སྨོས་ཏེ། བསྡུ༌[^2901]བའི་དངོས་པོ་བཞི་པ་མེད་དོ། །

[Block 4479]
དེ་བས་ཞེས་བྱ་བ་ནི། གང་སྔར་བསྟན་པའི།

[Block 4480 [VERSE]]
ས་ལ་འཁོད་པ་ཆོས་ཀྱིས་སྐྱོང་ལ་བག་མེད་སྤོངས། །
དེ་ལྟར་བྱས་ན་གྲགས་པ་དང་ནི་མཐོ་རིས་འཐོབ། །

[Block 4481]
ཅེས་བྱ་བ་སྟེ། དེ་ལྟར་བསྟན་པ་དང་། སྤང་བའི་ཕན་ཡོན་ནི༌[^2902]གང་ཡིན་ཞེ་ན། དེའི་ཕན་ཡོན་བསྟན་པའི་ཕྱིར། འབངས་རྣམས་སྐྱོན་ལ༌[^2903]མི་དགའ་ཞེས་བྱ་བ་ཕྱེད་འོག་མའོ། །

[Block 4482]
ཕན་ཡོན་རྣམ་པ་སྣ་ཚོགས་པ་ནི་བདག་ཉིད་ཀྱི་གྲགས་པ་འཐོབ་པ་དང་། འབངས་རྣམས་ཀྱི་ཡོན་ཏན་དང་། སྐྱོན་གཉིས་ལ་དགའ་བ་དང་། མི་འགལ་བར་འགྱུར་བ་སྟེ།

[Block 4483]
དང་པོ་བདག་ཉིད་ཀྱི་ཕུན་སུམ་ཚོགས་པས་ནི་བདག་གི་གྲགས་པ་འཐོབ་པའོ། །

[Block 4484]
ཇི་ལྟར་འབངས་རྣམས་ཀྱི་ཡོན་ཏན་དང་། སྐྱོན་ལ་ཐོབ་པ་དང་མི་འགལ་བ་ཡིན་ཞེ་ན། དེ་སྒྲུབ་པའི་ཕྱིར། ཁྱོད་ཀྱིས་ཆོས་སྤྱོད༌[^2904]གྱུར་ན་མི་ཡི་འཇིག་རྟེན་ཕལ་ཆེར་ནི། །ཞེས་བྱ་བ་སྨོས་ཏེ། ཕལ་ཆེར་ཞེས་བྱ་བ་ནི་མང་པོར་སྟོན་པ་ཡིན་ཏེ། འདིས་ནི་གཏན་དུ་སྤྱོད་པ་དེ་མ་གཏོགས་པའོ། །

[Block 4485]
ལེགས་པར་སྤྱོད་ལ༌[^2905]ཕྱོགས་ཤིང་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་སྒྲུབ་པའི་ཕན་ཡོན་ནོ། །
--- END BLOCKS ---
