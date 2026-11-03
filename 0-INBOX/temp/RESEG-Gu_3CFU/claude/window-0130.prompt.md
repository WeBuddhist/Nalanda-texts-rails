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

[Block 4556]
འདིར་དོན་ལྷག་པར་བསྒྲུབ་པ་ནི་སྐྱོན་ཡིན་ཏེ། འདིར་དོན་ལྷག་པར་འགྱུར་རོ་ཞེས་བྱ་བ་གཙོ་བོ་ཉིད་དུ་ཤེས་པའོ། །

[Block 4557]
གལ་ཏེ་སྦྱིན་བདག་གི་ཟད་ནའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དེ་འདི་ལྟར་ཐ་ག་པ་ལས་ངེས་པར་སྦྱར་བ་འཐོབ་པ༌[^3105]ན་སྦྱིན་བདག་གི་སྐུད་པ་ལ་སོགས་པ་ཟད་པར་གྱུར་ན་གཞན་ལ་བླངས་པས་གྲུབ་པ་ནི་འདིར་སྐྱོན་ཡིན་ཏེ་དེ་བས་ན་ཟད་པ་མེད་པ་ལ་འདི་མེད་པའོ། །

[Block 4558]
འདིར་འཐག་པ་བསྐྱེད་པས་ནི་རིན་སྐྱེ་ལ་རིན་སྐྱེས་པ་ནི་སྦྱིན་བདག་གི་ཟད་པར་འགྱུར་བར་རིག་པར་བྱའོ། །

[Block 4559]
རྔན་པ་མ་བྱིན་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཡང་ཚེ་དང་ལྡན་པ་ཐ་ག་པ་འདི་ལྟར་ཁོ་བོས་གླ་རྔན་ཅུང་ཟད་ཉིད་བསྒྲུབ་པར༌[^3106]བྱའོ་ཞེས་བྱ་བ་རང་གིས་ཀྱང་འདིར་འབྲས་བཟང་བའི་དོན་དུ་འདིར་རིན་སྦྱིན་པ་ལ་འདིར་མི་སྡོད་པ་སྲིད་པའོ། །

[Block 4560]
མི་སྡོད་ཅིང་ཉོ་བ་མེད་པར་ཡང་བླངས་པས་ཁོ་ལག་ཆེ་བ་ཉིད་དམ་འབྲས་བཟང་བ་ཉིད་དུ་མི་འགྱུར་ཏེ། ཉེ་བར་བསྒྲུབ་པ་འདི་ཡང་འཚོང་བ་མེད་པར་བླངས་པ་ལ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 4561]
བླངས་པས་གཞན་ལ་བསྒྲུབས་པས༌[^3107]ཏེ་འདིའི་དོན་དུ་མདོ་འདི་སྨྲས་སོ། །

[Block 4562]
འདོད་པའི་ཚོང་བ་མེད་པ་འདིར་རྐུ་བ་ལ་ཡང་བསྐྱེད་པར་རིག་པར་བྱའོ། །

[Block 4563]
སྦྱིན་པར་བྱེད་པས་དེའི་དོན་དུ་རྗེས་སུ་མ་གནང་བ་ལྟ་བུ་ནི་བྱེད་པ་པོ་དག་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། འདི་རྗེས་སུ་མ་གནང་བ་ཁོ་ལག་ཆེ་བ་ཉིད་དང་འབྲས་བཟང་བ་ཉིད་ལ་འདིའི་དོན་ཞེས་བྱ་བ་དེའི་རྗེས་སུ་མ་གནང་བ་ལྟུང་བའི་བྱེད་པ་པོ་འམ་གོས་དེའི་དངོས་པོ་ནི་དེ་ཉིད་དོ། །

[Block 4564]
སུས༌[^3108]རྗེས་སུ་མ་གནང་བ་ཞེས་བྱ་བ་སྨོས་པ་ལ་སྦྱིན་པར་བྱེད་པ་པོས་ཞེས་བྱ་བའི་ཚིག་གོ། །

[Block 4565]
ཁས་བླངས་པ་ལེན་པར་མི་བྱེད་ཅིང་རིན་ཐང་ལ་འཇུག་པར་མི་བྱེད་ན་སྦྱིན་བདག་མ་ཡིན་པ་ཡང་འདིར་སྦྱིན་པ་པོར་འགྱུར་རོ། །

[Block 4566]
དེ་བས་ན་དེ་ལ་འདིས་མ་བཟུང་བ་ཉིད་དོ། །

[Block 4567]
བླངས་པར་གྱུར་པས་རྗེས་སུ་གནང་བ་གང་ཡིན་པ་དེ་ལ་བླངས་པ་བསྒྲུབ་པ་ལས་ལྷག་པ་མ་ཡིན་ནོ། །

[Block 4568]
དེ་ལ་ཡང་འདིར་སྐྱོན་ཉིད་ཅེས་བྱ་བ་འདིར་བརྗོད་པ་ལ་གོ་བར་གྱུར་པའོ། །

[Block 4569]
དེ་བས་ན་བླངས་པ་མེད་པར་རང་དད་པས་མགྲོན་དུ་གཉེར་བ་མ་ཡིན་ན་རྗེས་སུ་གནང་བ་གང་ཡིན་པ་དེ་འདིར་བཟུང་བ་ཞེས་བྱ་བར་རྟོགས་པའོ། །

[Block 4570]
འདིར་གཞུང་ནི་འདི་ལྟར་བཅོལ་བའི་མདུན་རོལ་དུ༌[^3109]སྔར་རྗེས་སུ་མ་གནང་ན་ཞེས་གསུངས་པའོ།[^3110] །ཡན་ལག་འདི་རྣམས་ནི་ལྟུང་བའི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 4571]
འདི་རྣམས་ནི་གང་དུ་སྟེ་ཇི་ལྟ་བུ་འཐག་པའི་བསླབ་པའི་གཞི་ཁ་ན་མ་ཐོ་བའི་བྱེད་པ་པོ་རྣམས་ཤེ་ན། གྲུབ་པ་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གོས་གྲུབ་པའི་གནས་སྐབས་ན་དངོས་གཞིའི་ལྟུང་བའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4572]
མདུན་རོལ་དུ་དེའི་ཕྱིར་བསམས་པ༌[^3111]ལས་བྱུང་བ་རྗེས་སུ༌[^3112]བསྒྲུབ་པ་ཐ་དད་པ་ནི་ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བ་ནི་གོས་གྲུབ་པའི་མདུན་རོལ་དུའོ། །

[Block 4573]
ཕྱིར་ཞེས་བྱ་བ་ནི་གཅིག་དང་གཅིག་ཏུ་འདི་དང་འབྲེལ་པའི་བསམས་པ༌[^3113]ལས་བྱུང་བ་རྗེས་སུ་བསྒྲུབ་པ་ལ་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་རྣམས་ཏེ། དེའི་བསྒྲུབ་པ་ལ་བརྟེན་ནས་ཇི་སྲིད་དུ་རྩོམ་པ་གཅིག་ཏུ་གྱུར་པའི་རྗེས་སུ་བསྒྲུབ་པ༌[^3114]དེ་སྲིད་དུ་འདིར་གཅིག་རྗེས་སུ་བསྒྲུབ་པ་ཉིད་ཀྱིས་མངོན་པར་བརྟེན་པ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 4574]
འདིར་གཞུང་ནི་དགེ་སློང་ཆོས་གོས་ཀྱི་དོན་དུ་ཇི་ཙམ་དུ་ཅུང་ཟད་ལག་པ་དག་འཁྲུ་བར་བྱེད་པ་དང་། ལྷུང་བཟེད་འཁྲུ་བར་བྱེད་པ་དང་འགྲོ་བ་དང་འོང་བ༌[^3115]དང་བསོད་སྙོམས་ཐོབ་ནས་ཐ་ག་པ་ལ་སྦྱིན་པར་བྱེད་ན་ཐམས་ཅད་དུ་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 4575]
གོས་གྲུབ་ན་ནི་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4576]
འདིར་ཡང་དང་ཡང་དུ་འདོད་པ་ཅན་ཇི་ཙམ་ཅུང་ཟད་ཅེས་བྱ་བ་དང་། ཐམས་ཅད་ཅེས་བྱ་བའི་ཚིག་ནི་རྣམ་པར་གནས་པ་ཡིན་ཏེ། །ལག་པ་འཁྲུ་བ་ལ་སོགས་པ་བསྒྲུབ་པར་འདོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 4577]
འདི་རྣམས་ལ་རྩོམ་པ་གཅིག་ཉིད་དུ་གྱུར་པའི་ཕྱིར་ཞེས་བྱ་བ་དེ་ལྟར་གསུངས་སོ། །

[Block 4578]
མ་བསྒོ་བས་ཉེ་བར་འགྲོ་བ་ནི་དེ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཉེས་བྱས་སོ། །

[Block 4579]
བདག་གི་དོན་བསྒྲུབ་པ་མ་བསྒོ་བར་དགའ་བ་ཙམ་གྱིས་ཉེ་བར་འགྲོ་བ་གང་ཡིན་པ་དེ་ནི་འདིར་བཟུང་བ་སྟེ། གཞན་ལ་སྔར་བསྟན་པ་ལས་ལྷག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 4580]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 4581]
དགེ་སློང་གི་ཕྱིར་ཁྱིམ་པས་གོས་འཐག་ཏུ་བཅུག་ནས་དགེ་སློང་དེ་ཡང་ཉེ་བར་འགྲོ་ན་ཐ་དད་པར་མི་བྱེད་ཀྱང་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4582]
འཐག་ཏུ་འཇུག་པ་དང་འཐག་པ་བསྐྱེད་པའི་སྤང་བའོ།། །།

[Block 4583]
འཕྲོག་པའི་སྤང་བ་ལ་ཡན་ལག་གང་དག་བྱེད་པ་པོ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དབྲལ་བར་བྱ་བ་དགེ་སློང་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལས་གོས་ཕྲོག་པར༌[^3116]བྱེད་པ་དེ་དགེ་སློང་ཉིད་ཡིན་ནའོ། །

[Block 4584]
དབྲོག་པར་བྱ་བ་རང་གི་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདི་རང་གིས་བྱིན་པ་ལ་འདིར་གལ་ཏེ་འདི༌[^3117]བཟུང་ན་དབྲོག་པའི་ཉེས་པར་འགྱུར་རོ། །

[Block 4585]
བདེ་བླག་ཏུ་གཞན་གྱིས་བྱིན་པ་ལ་ཉེས་པ་འདི་ལ་གཞན་གྱིས་དབྱུང་བར༌[^3118]བྱ་བ་ཉིད་གསུངས་པ་ཁོ་ན་སྟེ། དོན་ལ་ནི་མ་ཡིན་ཏེ་སྦྱིན་བདག་གི་ཚིག་གི་སྤང་བ་བརྗོད་པའི་ཕྱིར་རོ། །

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
--- END BLOCKS ---
