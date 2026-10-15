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
[Block 4971]
ཡི་གེ་གཞན་ལས་ཤེས་པ་འདིར་རྟགས་ནི་བསྔོ་བར་བྱ་ཞེས་གསུངས་པའོ། །

[Block 4972]
རིང་དུ་མ་འབྲེལ་བ་ཉིད་དགེ་སློང་གི་དགེ་འདུན་ལས་ཟས་ཀྱི་རྙེད་པ་མ་ཡིན་པ་ཞེས་བྱ་བའོ། །

[Block 4973]
ཟས་ཀྱི་ཡིན་པར་གྱུར་པའི་དགེ་འདུན་གྱིས་རྙེད་པ་ལ་དགེ་སློང་རྣམས་ཀྱི་ཡང་དགེ་འདུན་གང་ཡིན་པ་སྟེ། གཞན་རྣམས་ནི་མ་ཡིན་ནོ། །

[Block 4974]
འདིར་ཟས་ཀྱི་རྗེས་སུ་འབྲངས༌[^3361]པས་འདི་ལ་ཉེས་བྱས་སུ་རྟོགས་པར་བྱའོ། །

[Block 4975]
རྙེད་པ་ཞེས་བྱ་བ་ལ་རྙེད་པ་ནི་རྣམ་པ་གཉིས་ཏེ། གོས་ཀྱི་རྙེད་པ་དང་ཟང་ཟིང་གི་རྙེད་པའོ། །

[Block 4976]
དོན་འདི་ལ་ནི་གོས་ཀྱི་རྙེད་པ་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ་འདི་འདིར་ཟས་མ་ཡིན་པའི་ཚིག་གི་གཞུང་སྟེ། འདིར་གཞུང་ནི་ལོག་པར་བསྔོས་པ་ཉིད་ཀྱིས་ཞེས་བྱ་བ་སྟེ། ཆོས་ཀྱིས༌[^3362]ཇི་ལྟར་བཤེས་ངོར་མ་བྱིན་ཞེས་བྱ་བའོ། །

[Block 4977]
གཞན་ཡང་འདིར་གཉིས་ཀ་འདོད་པ་ལ་སོགས་པ་ལོག་པའི་རྣམ་པ་ཡོད་དེ། དེ་དམིགས་ཀྱིས་བསལ་བ་ལ་ཉེས་པ་མེད་པའམ། ན་སྨད་པ་ཉིད་ནི་རིགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་བྱེ་བྲག་མེད་པར་གསུངས་སོ། །ཅི་ཞིག་གིས་དམིགས་ཀྱིས་བསལ་བ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་གིས་ཞེས་བྱ་བ་སྨོས་ཏེ། ཤིན་ཏུ་འདིར་སྔོ་བར༌[^3363]བྱེད་ཅེས་བྱ་བ་མདོ་ལས་མང་པོ་ཚིག་གིས་རེ་རེ་བཞིན་དུ་ཡང་བརྗོད་པ་ལ་འདིར་ལྟུང་བ་ཡིན་ཏེ། ཅིག་ཅར་མང་པོ་རྣམས་བརྗོད་པ་ལ་ཇི་ཙམ་དུ་སྐུར་པ་གདབ་པར་བྱ་བའི་ལྟུང་བ་རྣམས་དེ་ཙམ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིར་གཅིག་པའི་ཚིག་གིས་འདིར་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 4978]
གཞན་ལ་ཡང་ཞེས་བྱ་བ་ནི་སྐུར་པ་གདབ་པར་བྱ་བ་ཐོབ་པ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་ཉན་པ་པོ་གཞན་ལ་ཡང་གོ་བར་བྱེད་ན་འདིར་དངོས་གཞི་སྟེ། འོན་ཀྱང་གང་ཡང་རུང་བའི་མིའི་འགྲོ་བར་གཏོགས་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4979]
འདི་ལ་སྟེར་བར་འདོད་ན་བརྫུན་དུ་སྨ་བ་ལ་དངོས་གཞིའོ། །

[Block 4980]
མི་སྟེར་བར་འདོད་ན་ཉེས་བྱས་སོ། །

[Block 4981]
གཉིས་ཀའི་བརྫུན་དུ་མི་སྨྲ་བ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 4982]
ལོག་པ་ཉིད་དུ་ཤེས་བཞིན་དེ་མ་ཡིན་པ་ལ་སྟེར་བ་ལ་ནི་ཉེས་བྱས་སོ༌[^3364]ཞེས་བྱ་བ་འདིར་རྣམ་པར་གཞག་པ་འདི་རིག་པར་བྱའོ། །

[Block 4983]
མིང་མ་སྨོས་པར་ཞེས་བྱ་བ་ནི་མིང་མ་ཡིན་པར་བཟུང་བ་ཉིད་ལ་ཡང་འདིར་དངོས་གཞི་ཁོ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4984]
བརྗོད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་བསྔོ་བ་ཉིད་ཀྱིས་སོ། །

[Block 4985]
ཡང་དག་པ་མ་ཡིན་པའི་དོན་ཉིད་ཅེས་བྱ་བ་འདི་ནི་དངོས་གཞིའོ། །

[Block 4986]
སྐུར་པ་འདེབས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 4987]
ཁྱད་དུ་གསོད་པའི་ལྟུང་བྱེད་སྨྲ་བར་འདོད་ནས་འདུལ་བ་དང་ལྡན་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདུལ་བ་དང་ཡང་དག་པར་ལྡན་པའི་སོ་སོར་ཐར་པའམ། དེ་རྣམ་པར་འབྱེད་པ་ལ་སོགས་པར༌[^3365]གཏོགས་པ་ལའོ། །

[Block 4988]
ཕྲན་ཚེགས་དང་སིལ་བུ་དང་གླེང་གཞི་རྣམས་སམ་གཞི་རྣམས་ལ་འདུལ་བའི་མ་མོ་འམ། འདུལ་བའི་དཀའ་འགྲེལ་ལམ༌[^3366]འདུལ་བ་དྲུག་པ་འམ་གཅིག་ལས་འཕྲོས་པ་འམ་འདུལ་བ་མ་མོ་ལ་ཡང་དག་པར་གནས་པ་བརྗོད་པ་གང་ཡིན་པ་ལ་བརྙས་ཐབས་སུ་གྱུར་པ་ན་ཁྱད་དུ་གསོད་པའི་ལྟུང་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4989]
འདིར་བརྙས་ཐབས་ཀྱི་བྱེ་བྲག་ལས་ལྟུང་བའི་བྱེ་བྲག་ཏུ་ཤེས་པར་བྱའི་འདོན་པའི་བྱེ་བྲག་ལས་ནི་མ་ཡིན་ཏེ། གཅིག་ཏུ་འདོན་པ་ལ་ངག་རྣམས་ཐམས་ཅད་ལ་ལྟུང་བ་གཅིག་ཉིད་དེ་གཞན་ལ་ནི་གཞན་ཞེས་བྱ་བ་ཆ་ཤས་དང་རྒྱུད༌[^3367]དང་སྔགས་དང་སོ་སོར་ཐར་པའི་མདོ་འདོན་པ་ལས་ཕམ་པའི་ཆོས་བཞི་འདོན་པར་གྱུར་པ་རྣམས་ལ་བརྗོད་པར་བྱ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་འདིར་སོ་སོར་ཐར་པའི་མདོ་ལས་གསུངས་པ་ནི་འདུལ་བ་ལྷག་མ་རྣམས་ཀྱི༌[^3368]དཔེ་ཙམ་དུ་ཟད་དེ། ཇི་སྲིད་དུ་དགེ་སློང་གིས་འདུལ་བ་དང་ལྡན་པ་གང་ཇི་ཙམ་བརྗོད་པ་ལ་བརྙས་ཐབས་བྱེད་ན་ཐམས་ཅད་དུ་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་རྣམ་པར་འབྱེད་པ་ལས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4990]
མདོ་སྡེ་ལས་ནི་ཉེས་བྱས་ཞེས་བྱ་བ་ནི་འདུལ་བ་དང་ལྡན་པ་ལས་གཞན་པའི་མདོ་སྡེ་མངོན་པ་དང་འདུལ་བའི་མདོ་དག་གི་རྣམ་པར་འབྱེད་པ་ཉིད་ཀྱི་ཕྱིར་འདི་ལས་ལྷག་པ་མེད་པ་ཞེས་བྱ་བ་འདིར་རྗེས་སུ་འགྲོ་བའོ། །

[Block 4991]
ཁྱད་དུ་གསོད་པའོ།། །།

[Block 4992]
ལག་གི་བླས་མཆོད་རྟེན་དང་དགེ་འདུན་གྱི་དོན་དུ་ཤིང་ལྗོན་པར༌[^3369]བཅད་པར་བྱའོ་ཞེས་བྱ་བ་སྟེ། ཇི་ལྟར་ཞེ་ན། དེའི་ཕྱིར་དེའི་མདུན་རོལ་དུ་ཉི་མ་བདུན་ནམ་བརྒྱད་དག་ནས་དེའི་དྲུང་དུ་དཀྱིལ་འཁོར་དང་དྲི་དང་མེ་ཏོག་དང་མར་མེ་དང་གཏོར་མ་སྦྱིན་པ་དང་རྒྱུན་ཆགས་གསུམ་གདོན་པ་དང་སྦྱིན་པ་བཤད་པ་དག་བྱས་ནས། ལྷ་གང་དག་ཤིང་ལྗོན་པ་འདི་ལ་གནས་པ་དེ་དག་གནས་གཞན་ཚོལ་ཅིག །ཤིང་ལྗོན་པ་འདིས་མཆོད་རྟེན༌[^3370]ནམ་དགེ་འདུན་གྱི་བྱ་བ་བྱེད་པར་འགྱུར་རོ་ཞེས་བརྗོད་ནས་སྨྲ་བ་པོས་ཤེས་པར་གྱིས་ཤིག་ཅེས་སོ༌[^3371]ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་མདུན་རོལ་དུ་ཞེས་བྱ་བ་ནི་གཅོད་པའི་མདུན་རོལ་དུ་སྦྱིན་པ་བཤད་པར་བྱས་ནས་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་དེ་ན་གནས་པའི་ལྷ་ལ་བརྟེན་པར་བྱས་ནས་ཞེས་བྱ་བ་དོན་གྱིས་ཤེས་པར་བྱའོ། །

[Block 4993]
མཆོད་རྟེན༌[^3372]ནམ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན༌[^3373]གྱི་དོན་ཉིད་ལ་མཆོད་རྟེན་པ༌[^3374]ཞེས་བྱ་བ་བརྗོད་པར་བྱའོ། །

[Block 4994]
དགེ་འདུན་གྱི་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་དོན་ཉིད་ལ་ཞེས་བྱ་བ་ནི་བརྗོད་པར་བྱའོ། །

[Block 4995]
གལ་ཏེ་མེ་འབྱུང་བའམ་ཁྲག་འཛག་པ་འམ་ཡལ་ག༌[^3375]འགུལ་བའམ་ལོ་མ་ལྷགས་པ་ལ་སོགས་པ་རྣམ་པར་འགྱུར་བ་སྟོན་ན། དེས་ཞིང་ལ་སྦྱིན་པ་དང་སེར་སྣ་དག་གི་བསྔགས་པ་དང་བསྔགས་པ་མ་ཡིན་པ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། ཞིང་དང་ལྷན་ཅིག་ཏུ་སྦྱིན་པ་ནི་ངེས་ཞིང་ལ་སྦྱིན་པའོ། །

[Block 4996]
ཞིང་ནི་སངས་རྒྱས་དང་དགེ་འདུན་གྱི་བདག་ཉིད་ལ་བསྔགས་པ་བརྗོད་པར་བྱའོ། །

[Block 4997]
སྦྱིན་པ་ལ་ཡང་སེར་སྣའི་བསྔགས་པ་མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4998]
མི་གཏོང་ན་གཅད་པར༌[^3376]མི་བྱའོ་ཞེས་བྱ་བ་ན༌[^3377]དེ་ལྟར་བྱས་ཀྱང་མེ་འབྱུང་བ་ལ་སོགས་པའི་རྣམ་པར་འགྱུར་བས་མི་གཏོང་ན་གཅད་པར༌[^3378]མི་བྱའོ། །

[Block 4999]
ཤེས༌[^3379]གཙོ་བོའོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 5000]
མ་ཉམས་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྟེ། གང་དུ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ས་བོན་དང་ཁྱེའུ་ཁ་འཐོན་པ༌[^3380]རུང་བ་དག་གིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ས་བོན་རུང་བར་མ་བྱས་པ་དང་། ཁྱེའུ་ཁ་འཐོན་པ༌[^3381]ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5001]
འདིར་རྩྭ༌[^3382]ལ་སོགས་པ་སྐྱེ་བ་ཁྱེའུ་ཁ་འཐོན་པ༌[^3383]ཞེས་བྱ་བར་བརྗོད་དོ། །

[Block 5002]
རུང་བར་མ་བྱས་པ་ཞེས་སྨོས་པས་ནི་རུང་བར་བྱས་པ༌[^3384]ཉིད་ཡོད་ཀྱང་ས་བོན་ཉིད་ལ་ལྟུང་བ་མེད་ཅེས༌[^3385]བྱ་བར་རིག་པར་བྱའོ། །

[Block 5003]
འདིར་ཅི་ཞིག་རྗེས་སུ་བསྒྲུབ་ན་དེ་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཐ་ན་རྩ་རྒྱུན་ཡན༌[^3386]ཆད་ཉམས་པར་བྱས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡན་ཆད་ཀྱི་སྒྲས་ནི་མངོན་པར་ཁྱབ་པར་བྱས་པའི་དོན་ལའོ། །

[Block 5004]
ཐ་ན་རྩ་རྒྱུན་གྱི་ཡན་ཆད་ཀྱི་ས་བོན་འདི་དག་ལ་ཁྱེའུ་ཁ་འཐོན་པ༌[^3387]སྟེ། གང་ཡང་རུང་བ་དག་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5005]
འདིར་གཞུང་ནི་ཤིང་ལྗོན་པའི་རྩ་རྒྱུན་འབྱིན་པར་བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5006]
ཇི་ལྟར་ཉམས་པ་དང་གཅོད་པ་དང་རུང་བ་ལ་སོགས་པ་ཉིད་ཀྱིས༌[^3388]ཅིར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཇི་ལྟར་ཡང་རུང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཉིད་བསྟན་པའི་ཕྱིར་སྤྲུལ་པས༌[^3389]ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 5007]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས༌[^3390]ཤིང་ཏོག་རྣམས་སྤྲུག་ཅིང་གློག་པར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། གལ་ཏེ་ཤིང་ཏོག་སྨིན་པ་དག་ཡིན་ན་ནི་ཉེས་བྱས་སོ། །

[Block 5008]
ཇི་སྟེ་མ་སྨིན་པ་དག་ཡིན་ན་ནི་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5009]
རྩ་བ་དང་འདམ༌[^3391]རྫབ་དང་ས་རྡུལ་ལ་སོགས་པ་དག་གིས་མནན་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་རན་ནམ་འདམ་རྫབ་བམ་ས་རྡུལ་གྱིས༌[^3392]ཤིང་ལྗོན་པ་ཉམས་པར་གྱུར་ཅིག །རྣམ་པར་ཉམས་པར༌[^3393]གྱུར་ཅིག་ཅེས་གནོན་པར་བགྱིད་ཅིང་རྩྭ༌[^3394]སྔོན་པོ་ས་རྡུལ་ལམ་ཕྱེ་མའམ་གཞན་གང་ཡང་རུང་བས་འགེབས་པར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5010]
འདིར་སྦྱོར་བ་ཙམ་ལ་དགོངས་ནས་ཤིང་ལ་སོགས་པ་མནན་པ་ལ་སོགས་པ་ལ་ཉེས་བྱས་ཀྱི་ཚིག་གོ། །
--- END BLOCKS ---
