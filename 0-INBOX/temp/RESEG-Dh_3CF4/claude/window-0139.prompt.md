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
བདག་ལ་ཕན་འདོགས་ཞེས་བྱ་བ་ནི་གཞན་ལ་ཕན་པ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 4867]
བདག་གི་ཕུན་སུམ་ཚོགས་པ་ཡང་རྣམ་པ་གསུམ་སྟེ། གཟུགས་ཀྱི་ལུས་ཕུན་སུམ་ཚོགས་པ་དང་། མིང་གི་ལུས༌[^3150]ཕུན་སུམ་ཚོགས་པ་དང་། བྱ་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 4868]
གསེར་བཙོ་མའི་ཁ་དོག་གསལ་བ་འདྲ་བ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གཟུགས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 4869]
དེ་སེམས་རྣོ་བ་ཞེས་བྱ་བས༌[^3151]ནི་ཤེས་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 4870]
འཁྲུལ་འཁོར་དང་གཏོར་ཞེས་བྱ་བ་དག་གིས་ནི་བྱ་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 4871]
རི་དགས་མང་པོ་རྗེས་སུ་འབྲང་བ་རྣམས་ལ་ཡང་སློབ་ཅེས་བྱ་བ་ལ་སོགས་པས་ནི་བདག་ལ་ཕན་འདོགས་ཞེས་བྱ་བ་བསྟན་ཏོ། །

[Block 4872]
རི་དགས་ཀྱི་བདག་པོ་ཞེས་བྱ་བས་ནི་མཆོད་པ་ཞེས་བྱ་བ་བསྟན་ཏོ། །

[Block 4873]
ཆུ་ཆེན་འབྲུབ་པ༌[^3152]རབ་ཏུ་དྲག་པོ་ཡིས། །ཞེས་བྱ་བ་འདིའི་བསྡུས་པའི་དོན་ནི། བདག་ཉིད་ཀྱི་སྙིང་རྗེའི་གནས་སུ་གྱུར་པ་ཐམས་ཅད་བསྒྲགས་པ་ཡིན་ཏེ། [^3153]སྙིང་རྗེའི་ཞིང་ནི་གསུམ་སྟེ། ཕོངས་པ་དང་། སྡུག་བསྔལ་བ་ཉིད་དང་། རྗེས་སུ་འབྲང་བ་མེད་པའོ། །

[Block 4874]
ཆུ་ཆེན་འབྲུབ་པ༌[^3154]རབ་ཏུ་དྲག་པོ་ཡིས། །ཁྱེར་ནས་ཞེས་བྱ་བ་འདིས་ནི་སྡུག་བསྔལ་བ་ཉིད་བསྟན་ཏོ། །

[Block 4875]
མགོན་མེད་གཟིངས་ཀྱང་ཡོད་མ་ཡིན། །ཞེས་བྱ་བས་ནི་སེམས་ཅན་དང་། སེམས་ཅན་མ་ཡིན་པའི་བར་དུ་བགྲང་བ་མེད་པའོ།[^3155] །ཕོངས་ཤིང་ཉམ་ཐག་ཅེས་བྱ་བ་དང་། མྱུར་དུ་བརྒྱུགས་ཏེ༌[^3156]ཟུང་ཞེས་བྱ་བས་ནི་བདག་ཉིད་ཕོངས་པ་ཉིད་དོ། །

[Block 4876]
སྡུག་བསྔལ་བྱམས་པས༌[^3157]ཞེས་བྱ་བ་ནི་ཐུགས་རྗེ་ཅན་ནོ། །

[Block 4877]
མྱུར་བ་ནི་མགྱོགས་པའོ། །

[Block 4878]
མྱུར་དུ་རྒྱུག་པའི༌[^3158]རྒྱུ་བསྟན་པའི་ཕྱིར། ད་ནི་བཤོལ་དུ་རུང་བ་མ་ཡིན་ཏེ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4879]
མྱུར་བས་རྒྱུག་པ༌[^3159]ཅིའི་ཕྱིར་ཞེ་ན། སྡོད་པར༌[^3160]མི་ཚུགས་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་བཤོལ་དུ་མི་རུང་ཞེ་ན། དཔུང་པ་དང་རྐང་པ་དག་གིས་བཤོལ་དུ་མི་རུང་བའི་ཕྱིར་ཏེ། དེ་གཉི་གས་སྡོད་པར་མི་ནུས་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་དཔུང་པས་བཤོལ་དུ་མི་རུང་བར་འགྱུར་ཞེ་ན། ངལ་ཞིང་དུབ་པས་དཔུང་པ་ཡང་འགྱུར་བར་མི་ནུས་ཞེས་པས་སོ། །ཅིའི་ཕྱིར་རྐང་པས་བཤོལ་དུ་མི་རུང་བར་འགྱུར་ཞེ་ན། ཟུག་ཅིང་འབོག་ཏུ་རུང་བའང་ཅུང་ཟད་མེད། །ཅེས་པས་སོ། །

[Block 4880]
དུས་ལ་བབ་ཅེས་བྱ་བས་ནི་དུས་ལས་འདས་ན་རྒལ་བར་མི་ནུས་པར་བསྟན་ཏོ། །

[Block 4881]
འཇིགས་པ་དང་། མི་དགའ་བ་དང་། ངལ་བ་དང་། དུབ་པ་མེད་པར་བྱེད་པ་ཞེས་བྱ་བ་ལ། འཇིགས་པ་ནི༌[^3161]འཆི་བས་སོ། །

[Block 4882]
མི་དགའ་པ་ནི་རྗེས་སུ་འབྲང་བ་མེད་པས་སོ། །

[Block 4883]
ངལ་བ་ནི་ངལ་ཞིང་དུབ་པས་དཔུང་པ་འགྱུར་མི་ནུས་པ་དང་། ཟུག་ཅིང་འབོག་ཏུ་རུང་བ་ཅུང་ཟད་མེད་པས་སོ། །

[Block 4884]
སྙིང་རྗེ་ཞེས་བྱ་བ་ནི་ལྷག་པར་སྙིང་རྗེ་བར་གྱུར་པའོ། །

[Block 4885]
དེས་གདུངས་པའི་གསལ་བའི་ཚིག་གང་ཡིན་པ་དེ་ནི་གསལ་བའི་ཚིག་སྙིང་རྗེས་གདུངས་པའོ། །

[Block 4886]
འབབ་ཆུ་དྲག་པོའི་འཇིང༌[^3162]དེར་ཞུགས། །ཞེས་བྱ་བ་ཅིའི་ཕྱིར་ཞེ་ན། བསྒྲལ་བར་ངེས་པར་བྱས་པའི་ཕྱིར་ཏེ།

[Block 4887 [VERSE]]
འདིས་ནི་གཞན་ལ་སྙིང་རྗེ་ཆེ་བར་བསྟན་ཏོ། །
བདག༌[^3163]སྲོག་ཡལ་བར་བོར༌[^3164]ཡང་མི་སེམས་པར། །

[Block 4888]
ཞེས་བྱ་བ་འདིས་ནི་བདག་ལ་ཆགས་པ་མེད་པར་བསྟན་ཏོ། །

[Block 4889]
གཞན་མ་ཚང་བས་ནི་ཆུ་དྲག་པོ་དེར་ཞུགས་པར་མི་ནུས་པའི་ཕྱིར་རོ། །ཇི་ལྟ་བུར་ཞུགས་ཤེ་ན། དགྲ༌[^3165]དཔུང་ལྟ་བུར་རོ། །

[Block 4890]
ཇི་ལྟར་ཞེ་ན། དགྲའི་དཔུང་རྣམ་པར་འཇོམས་པའི་དཔའ་བོ་བཞིན་ནོ། །

[Block 4891]
དེའི་རྒྱབ་ཏུ་ཞོན་པར་གྱུར་ཅེས་བྱ་བ་ནི་ཅིའི་ཕྱིར་ཞེ་ན། སྐྲག་པས་ཉེན་པ་ཡིན་ཏེ། འཆི་བས་སྐྲག་པའི་ཕྱིར་དང་། ཡན་ལག་འཁུམས་པའི་ཕྱིར་རོ། །

[Block 4892]
ཡིད་ཏུ༌[^3166]འོང་བའི་འགྲམ་དུ་མ་ཉམས་ཕྱིན་པ་ནི་ལྗིད་ཀྱིས་རབ་ཏུ་ནོན་པ་དང་། འབབ་ཆུ་དྲག་པོའི་ཤུགས་ཀྱིས་བདས་པར་གྱུར་ཀྱང་དཔའ་སྙིང་བརྟན༌[^3167]ལ་རྩོལ་བ་དྲག་པོའི་ཕྱིར་རོ། །

[Block 4893]
ཉེ་དུ་དང་གྲོགས་པོ་དག་ནི་ཉེ་དུ་དང་གྲོགས་པོའོ།[^3168] །དེ་དག་ཉིད་མཛའ་བོ་ཡིན་པས༌[^3169]ཉེ་དུ་དང་གྲོགས་པོ་མཛའ་བོའོ། །

[Block 4894]
གྲོགས་བྱ་ཞིང་ཕན་འདོགས་པ་ཡང་ཡིན་ལ། ཉེ་དུ་དང་། གྲོགས་པོ་དང་། མཛའ་བོ་ཡང་ཡིན་པས་གྲོགས་བྱས་ཤིང་ཕན་བཏགས་པའི་ཉེ་དུ་དང་གྲོགས་པོ་དང༌[^3170]མཛའ་བོའོ། །

[Block 4895]
དེ་དག་ལ་འང་རྙེད་པར་དཀའ་བ་ཡིན་པས། གྲོགས་བྱས་ཤིང༌[^3171]ཕན་བཏགས་པ་དེ་ལྟ་བུ་ཉེ་དུ་དང་གྲོགས་པོ་དང་མཛའ་བོ་སུ་ལའང་མེད་པ་ཉིད་དེ། །[^3172]ངོ་མཚར་ཆེ་བ་དེས༌[^3173]མགུ་བར་གྱུར་པ་ནི་ངོ་མཚར་ཆེ་བ་དེས་སེམས་མགུ་བར་གྱུར་པའོ། །

[Block 4896]
དེས་ཕྱག་འཚལ་ཏེ་ཞེས་བྱ་བ་ལ། ཕྱག་འཚལ་བའི་རྒྱུ་བསྟན་པའི་ཕྱིར་ངོ་མཚར་ཆེ་བར་གྱུར་པ་དེས་སེམས་རབ་ཏུ་མགུ་བར་གྱུར་པ་དང་། དེའི་གཟུགས་བཟང་པོ་དེས་ཀྱང་ཡ་མཚན་དང་ཞེས་སྐྱེས་པར་གྱུར་པས་དེ་ལ་ཕྱག་འཚལ་བའོ། །

[Block 4897]
འདི་ལྟ་བུ་དག་བྱར༌[^3174]མི་ནུས། །ཞེས་བྱ་བ་ནི་གཉེན་བཤེས་དང་། བྱམས་པར་གྱུར་པ་དག་གིས་ཀྱང་བདག་ལ་སྐྱོབ་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 4898]
དེ་བས་ཅི་བགྱིའི་བཀའ་སྩལ་པས། །ཞེས་བྱ་བས་ནི་ཤིན་ཏུ་རྗེས་སུ་གཟུང་བའི༌[^3175]ཕྱིར་རོ། །

[Block 4899]
གང་དུ་ཞེས་བྱ་བ་ནི་ལས་སོ། །

[Block 4900]
རང་བཞིན་གྲུབ་པ་ཞེས་བྱ་བ་ནི་དེའི་ཆོས་ཉིད་རང་བཞིན་གྱིས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 4901]
འགྱུར་བ་ཞེས་བྱ་བ་ནི་དྲིན་གཟོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4902]
དེའི་ཞེས་བྱ་བ༌[^3176]ནི་སྐྱེ་བོ་དམ་པ་འདིའི་དོན་ཏེ། དོན་འདི་གང་ཡིན་ཞེ་ན། སེམས་ཅན་འདི་ལྟ་བུ་ཞིག་གིས་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་བསྟན་པའོ། །

[Block 4903]
ཤ་བཟའ་བར་རུང་བས་ནི་བཟར་རུང་བའོ། །

[Block 4904]
རབ་ཏུ་ཆགས་པར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་གཟུགས་ཀྱི་ཡོན་ཏན་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 4905]
དེ་གཉི་གས་ཉམས་པར་འགྱུར་བ་ནི། སྙིང་རྗེ་ཆུང་བ་ཡིན་ཏེ། ངའི་ལུས་ནི་ཤ་བཟར་རུང་བ་དང་རབ་ཏུ་ཆགས་པར་འགྱུར་བ་ཡིན་ལ། མི་རྣམས་ཀྱི་སྙིང་ནི་རབ་ཏུ་ཆགས་པར་བྱེད་པའི་གཟུགས་ཡོད་པས་སོ། །
--- END BLOCKS ---
