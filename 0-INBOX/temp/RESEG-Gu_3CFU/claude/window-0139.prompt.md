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
[Block 4866]
གང་ཟག་ཇི་ལྟ་བུ་དང་ཁ་ན་མ་ཐོ་བ་ཇི་ལྟ་བུ་ལ་འདིར་འདུ་ཤེས་ཀྱི་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གཉུག་མར་གནས་པ་དང་ལས་བྱེད་པ་དང་འདུན་པ་འབུལ་བ་རྣམས་ཁོ་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་སྨོས་ཏོ། །

[Block 4867]
དེས༌[^3309]འདི་རྣམས་ལ་ཡང་དག་པར་བཞག་པ་ཉིད་ལ་ངེས་པ་ཞེས་བྱ་བ་འདི་ལས་མདུན་དུ་གང་ཞིག་འདུ་ཤེས་པར་གྱུར་པ་ཉིད་ཀྱི་སྐྱོ་སྔོགས་བྱེད་པ་དེ་འདི་རྣམས་ལ་དངོས་གཞིའོ། །

[Block 4868]
དངོས་གཞིའི་གནས་ལ་ཡང་གཞན་ལ་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་འདི་ལ་སྤྲོས་པ་འདི་རིག༌[^3310]པར་བྱའོ། །

[Block 4869]
ལྟ་བ་སྨྲ་བ་དང་གློ་བུར་དུ་འོངས་པ་དག་ལ་ནི་ཉེས་བྱས་ཁོ་ནའོ་ཞེས་བྱ་བ་ནི་གློ་བུར་དུ་འོངས་པ་ཉིད་ཡིན་པས་རྒྱུས༌[^3311]མི་ཤེས་པའི་ཕྱིར་རྩོད་པའི་གཞི་དང་བཅས་པ་ལ་འདི་ཐོག་མ་དང་བར་དང་ཐ་མར་མངོན་པར་མི༌[^3312]ཤེས་པའི་ལྟ་བ་སྨྲས་པ་ཉིད་ནི་སྐྱོ་སྔོགས་བྱེད་པ་འདི་དག་གི་ལྟ་བ་སྨྲ་བར་བྱེད་པ་དག་ནི་འདི་མི་འདོད་ཅེས་བྱ་བ་ངེས་པ་འདི་དག་ལ་ཡང་དག་པར་བཞག་པ་ཉིད་ལ་ངེས་པ་མེད་ཅེས་བྱ་བ་དེའི་ཕྱིར་གང་ཞིག་རྒྱུས་མི་ཤེས་པར་འགྱུར་རོ། །

[Block 4870]
སྐྱོ་སྔོགས་བྱེད་པ་དེ་བས་ན་འདི་ནི་ཉེས་བྱས་སོ། །

[Block 4871]
རྩོད་པ་གཞན་ཉིད་ལ་རྩོད་པ་གཞན་དུ་ཤེས་པ་ནི་དེ་དང་འདྲ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྩོད་པ་གཞན་ཉིད་ཀྱིས༌[^3313]འདུ་ཤེས་པ་ལ་རྩོད་པ་དེ་དང་ལྡན་པ་ཉིད་དོ། །

[Block 4872]
རྩོད་པ་གཞན་ཉིད་ནི་ངག་གིས་འདིའི་འདུ་ཤེས་པ་ནི་དེར་གྱུར་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4873]
ན་སྨད་པའི་ངོ་བོ་ལ་འདི་བསྟན་པའོ། །

[Block 4874]
འདིར་རྩོད་པ་ཉིད་ཚད་མར་ཡིན་གྱི་དེའི་བྱེ་བྲག་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིར་རྣམ་པར་གཞག་པ་འདི་ཡིན་ནོ། །

[Block 4875]
ལྟུང་བའི་ཕྱིར་རྩོད་པ་ཉིད་དུ་འདུ་ཤེས་པ་ལ་ནི་ན་སྨད་པ་མེད་དོ། །

[Block 4876]
དེ་བཞིན་དུ་གཞན་ལས་ཏ་དེའི་ཕྱིར་འདི་བྱེད་པའོ། །

[Block 4877]
ལས་ཀྱི་འབྲས་བུ་ལ་གནས་པ་ལ་དེ་མ་ཡིན་པ་ཉིད་ཀྱིས་ཀུན་དུ་སྤྱོད་པ་ལ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ལས་ཀྱི་འབྲས་བུ་ལ་གནས་པ་ལ་ནི་ཤེས་པ་ལ་སོགས་པའི་ལས་ཀྱི་འབྲས་བུ་ཐོབ་པ་ལ་ལས་ཀྱི་འབྲས་བུ་ལ་གནས་པ་དེར་གནས་པ་ཉིད་ཀྱི་ཀུན་དུ་སྤྱོད་པ་ལ་ནི་ཕྱེད་ཉིད་དོ། །

[Block 4878]
ཡོངས་སུ༌[^3314]རྫོགས་པའི་ཀུན་དུ་སྤྱོད་པ་ཉིད་ལ་ནི་ཉེས་བྱས་སུ་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4879]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་དགེ་སློང་གིས་བསླབ་པ་བྱིན་པ་ལ་འདི་སྐད་ཅེས་ཁྱོད་བསླབ་པ་པོ་མ་ཡིན་ནོ་ཞེས་བགྱིས་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4880]
སྐྱོ་སྔོགས་བྱེད་པའོ།། །།

[Block 4881]
འདི་ལ་བྱེད་པ་པོ་ཉིད་ནི་བུད་མེད་དོ། །

[Block 4882]
ཁྱིམ་པ་མོ་ལ་སྟོན་པ་ལའོ། །

[Block 4883]
སྐྱེས་པ་མེད་པར་རོ། །

[Block 4884]
རེག་པའོ་ཞེས་བྱ་བ་སྔར་བསྟན་པ་དེ་ལ་ཉེ་བར་མི་གནས་པ་ཉིད་ལ་རེག་པའི་སྐྱེས་པ་ལ་བསྟན་པའི་ལྟུང་བྱེད་གང་ལ་བྱེད་པ་པོ་ཉིད་བུད་མེད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྟོན་པ་ལའོ་ཞེས་བྱ་བ་ནི་སྨོས་སོ།[^3315] །ཅི་ཞིག་སྟོན་པ་ལ་ཞེ་ན། དེའི་ཕྱིར་ཆོས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གྲོང་འདིའི་ལམ་འདི་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་ལས་ཡང་དག་པའི་བསམ་པས་ཆོས་ཀྱི་རྗེས་སུ་འགྲོ་བར་བྱའོ། །

[Block 4885]
འདིར་བརྫུན་པའི་དངོས་པོ་ལ་ནི་སྒོ་ཡིན་ཏེ་གང་ཞིག་བུད་མེད་ལ་རང་དབང་མེད་པར་འཚེ་བའོ། །

[Block 4886]
འདིའི་ཕྱིར་རང་དགར་སྨྲ་བའི་རྣམ་པས་དཔེ་ཡིན་ཏེ་ཞེས་བྱ་བ་འདི་ལ་འདིར་བསླབ་པའི་གཞི་དང་འབྲེལ་པའི་ཆོ་ག་དྲུག་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡོངས་སུ་བཟུང་བའོ། །

[Block 4887]
མཁས་པས་གོང་ནས་གོང་དུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡང་འདྲི་བ་སྟེ་ཇི་ཙམ་ལས་ཤེ་ན། དེའི་ཕྱིར་ཚིག་དྲུག་པ་ལས་ལྷག་པར་རོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4888]
གང་ཟག༌[^3316]ཇི་ལྟ་བུས་ཤེ་ན། དེའི་ཕྱིར་ལྷག་པ་ཉིད་དུ་ཤེས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དོན་ཡོད་པའི་དེར་འདུ་ཤེས་པ་ལ་དངོས་གཞི་བསྟན་པའོ། །

[Block 4889]
དེར་མེད་པ་ལ་ལྟུང་བ་ཉེས་བྱས་ཞེས་བྱ་བའོ། །

[Block 4890]
དེ་བས་ན་འདུ་ཤེས་འདི་ལ་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བ་འདི་ལས་ཤེས་པ་པོ་ཉིད་དོ། །

[Block 4891]
འདིར་ཡིད་གཉིས་ཟ་ན་ནི་ཡིད་གཉིས་ནི་འདུ་ཤེས་དང་འདྲའོ་ཞེས་བྱ་བས་ལྟུང་བ་རྣམ་པར་གཞག་པར་རིག་པར་བྱའོ། །

[Block 4892]
ཚིག་སྔ་མ་ལ་ནི་རྩོམ་པ་ལྔ་པ༌[^3317]ལས་སོ་ཞེས་བྱ་བ་ནི་ཚིག་ལྔ་པའི་ཆོས་རྩོམ་པ་ལ་ཚིག་ལྔ་ལས་ལྷག་པར་སྟོན་པ་ན་གཞན་ཐམས་ཅད་ལ་དྲུག་པ་ལས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4893]
དོན་ལྔ་པ་ཡོངས་སུ་རྫོགས་པ་ལ་འདིར་མང་པོ་ཉིད་དོ། །

[Block 4894]
ཐམས་ཅད་དུ་དྲུག་པ་ལ་ཞེས་བྱ་བའི་འདི་རྣམ་པར་གཞག་པའོ། །

[Block 4895]
ཡོངས་སུ་རྫོགས་པ་དང་ཡོངས་སུ་མ་རྫོགས་པ་དོན་གཅིག་པ་ཆད་པ་ལ་བརྟེན་པའི་ཚིག་ནི་འདིར་ཚིག་གོ། །

[Block 4896]
གནས་སྐབས་ཀྱི་དོན་བསྟན་པ་ལ་བརྗོད་པར་འདོད་པ་ལ་གཟུགས་མི་རྟག་གོ་ཞེས་བྱ་བ་འདི་ལ་ཚིག་ཉིད་དོ། །

[Block 4897]
གཟུགས་ཙམ་གྱི་དོན་རྗེས་སུ་བཤད་པ་སྨྲ་བར་འདོད་པ་ལ་ཕུང་པོ་ནི་ལྔ་སྟེ། གཟུགས་དང་ཚོར་བ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། གཟུགས་ཞེས་བྱ་བ་འདི་ཉིད་ལ་ཚིག་གོ། །

[Block 4898]
འདིར་མདོར་བསྟན་པ་ལ་ནི་རྒྱས་པར་བཤད་པ་ཚད་མ་ཡིན་པའི་ཕྱིར་ཐ་མི་དད་པར་རིག་པར་བྱ་སྟེ། དཔེར་ན་ཕུང་པོ་ལྔ་ཞེས་བྱ་བ༌[^3318]ལྟ་བུའོ། །

[Block 4899]
མཁས་པས་གོང་ནས་གོང་དུ་དྲིས་པ་གཏན་ལ་དབབ་པ་བྱས་པ་དང་། སློབ་གཉེར་བསོད་པ་དང་། ཁ་ཏོན་ཞུ་བ་དང་། དམིགས་ཀྱིས་དྲི་བ་དང་། དུས་ཁྲིམས་དབོག་པ་དང་ཡོན་བཤད་པ་དག་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མཁས་པས་གོང་ནས་གོང་དུ་དྲིས་པ་གཏན་ལ་དབབ་པ་བྱས་པ་དང་། སློབ་གཉེར་བསོད་པ་དང་། ཁ་ཏོན་ཞུ་བ་དང་། དམིགས་ཀྱིས་དྲི་བ་དང་། དུས་ཁྲིམས་དབོག་པ་དང་། ཡོན་བཤད་པ་ལ་བརྟེན་པ་ལ་ཡང་བྱེད་པ་པོ་ཉིད་ནི་མ་ཡིན་ཏེ། དེ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 4900]
འདིར་རང་དང་ཉེ་བའི་གཞིར་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4901]
འདིར་ཁ་ཏོན་ཞུ་བ་སྨོས་པས་ཀློག་པ་ཡང་བསྡུས་པ་ཡིན་ནོ། །

[Block 4902]
བཙུན༌[^3319]མོ་ཕྲེང་ལྡན་མ་དང་དབྱར་ཚུལ་མ་གཉིས་ཀྱིས་ཀློག་པའི་ཕྱིར་ཅི་བཀླགས༌[^3320]ལགས་སམ་ཞེས་བྱ་བ་དང་ལྷོགས་ཤིག་ཅེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 4903]
དུས་ཁྲིམས་དབོག་པ་དང་ཡོན་བཤད་པ་གཉིས་ཀྱི་གཞུང་ནི་ཞུ་བའི་གཞུང་ཁ་ཅིག་ལས་ཡོན་བཤད་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 4904]
བསྙེན་གནས་ཡན་ལག་བརྒྱད་དང་ལྡན་པ་དབོག་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4905]
གནས་གཞན་དུ་ནི་སྔ་མ་མ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། གནས་གཞན་དུ་ཞེས་བྱ་བ་ནི་ཁང་བཟངས༌[^3321]ལ་སོགས་པར་སྟོན་པ་ལ་སྔ་མ་གནས་ཁང་ལ་སོགས་པར་བྱས་པ་དང་ལྷན་ཅིག་མ་བྱས་པ་ཉིད་དེ། དེ་ལ་ལྟུང་བ་རྣམ་པར་གཞག་པར་མི་བྱའོ་ཞེས་བྱ༌[^3322]བའི་དོན་ཏོ། །
--- END BLOCKS ---
