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
[Block 106]
དེ་ཇི་སྙེད་པའི་འདིང་བར་བྱེད་པའོ་ཞེས་བྱ་བ་ལ། དེའི་སྒྲས་ནི་ཆོས་གོས་སུམ་ཕྲུགས་ལ་བཟུང་ངོ་། །ཆོས་གོས་སུམ་ཕྲུགས་དེ་ཇི་སྙེད་པ་དེ་སྙེད་ཀྱི་གདིང་བར༌[^92]བྱེད་པའི་དགེ་སློང་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 107]
དེ་ནི་ཆོས་གོས་གཞན་བྱིན་གྱིས་བརླབ་པ་ཡིན་པས་དེའི་ཕྱིར་བྱིན་གྱིས་བརླབས་པ༌[^93]དག་ཕྱུང་ནས་སོ་ཞེས་བྱ་བ་ནི་ཚོགས་པ་ལ་མི༌[^94]བརྟེན་པས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། རང་གི་རྫས་ནི་དོན་དུ་ངེས་པར་སྦྱར་བ་འདི་ཡིན་ཏེ། གང་གིས་ནི་མཐུན་པའོ། །

[Block 108]
བདག་པོས་མི་འདོར་བའི་རྫས༌[^95]དོན་ལ་ངེས་པར་སྦྱོར་བ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་བདག་པོ་རྣམས་ཀྱིས་འདིར༌[^96]འདོད་པས་བླང་བར་བྱའོ།[^97] །ཅི་ཚོགས་པ་རྗེས་སུ་བགྲང་བར་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཞག་མ་ལོན་པར་ཚོགས་པས་མོས་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚོགས་པ་ཁས་ལེན་པ་ལ་རྩོམ་པ་འདིའོ། །

[Block 109]
མངོན་སུམ་དུ་ཕྱོགས་པའི་དབང་གིས་ཚོགས་པ་འབྱོར་པའོ། །

[Block 110]
ཚོགས་པ་ལ་ཚོགས་པས་མངོན་དུ་ཕྱོགས་པ་ཉིད་ནི་ཤིན་ཏུ་སྟོབས་དང་ལྡན་པ་སྟེ། དེ་ལྟ་བས་ན་ཆོ་ག་འདི་གང་གི་ཚེ་ཞེ་ན། དེའི་ཕྱིར་ཞག་མ་ལོན་པར་ཞེས་བྱ་བ་སྨོས་ཏེ། ཞག་མ་ལོན་པ་ནི་ཉི་མ་གང་ལ་ཆོས་གོས་དེ་འབྱོར་པའི་ཉི་མ་དེ་ཉིད་ལ་བདག་པོ་རྣམས་ཀྱིས་ཚོགས་པ་དེ་ལ་འདོད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 111]
འདིར་གཞུང་ནི། ཇེ༌[^98]

[Block 112]
དང་པོ་ཁོ་ནར་ཚོགས་པས་ཆོས་གོས་འདི་ནི་དབྱར་གནས་པའི་དགེ་འདུན་གྱི་ཆོས་གོས་ཀྱི་རྙེད་པ་གྲུབ་པ་ལགས་ཏེ། གལ་ཏེ་དགེ་འདུན་བཞེད་ན་ཆོས་གོས་འདིས་དགེ་འདུན་གྱི༌[^99]སྲ་བརྐྱང་འདིང༌[^100]པར་འགྱུར་རོ་ཞེས་མོས་པར་བྱའོ། །

[Block 113]
དེའི་འོག་ཏུ་ཉི་མ་གཞན་ལ་གནས་མལ་བཤམ་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 114]
ཉི་མ་གཞན་ལ་མོས་པར༌[^101]བྱ་བའི་ཉི་མ་དེ་ཉིད་དམ། ཉི་མ་གཉིས་པ་ལ་བློ་མཐུན་པར་བྱ་བའི་དགེ་སློང་ཁོ་ནར་ངེས་པ་མེད་དེ། དེའི་ཕྱིར་དོན་འདི་ལ་གདིང་བའི་ཉི་མ་གང་ཉིད་ལ་བརྗོད་པ་དེ་ཉིད་ལ་མཐུན་པའི་བློ་ཞེས་བྱ་བ་འདི་ལྟར་རྩེ་གཅིག་པ་ཉིད་དུ་དེ་ལྟར་གནས་པ་ཡིན་གྱི།

[Block 115]
གཉིས་པ་ཉིད་ལ་ནི་མ་ཡིན་ཏེ་འདིར་དགོས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 116]
མཚམས་ཀྱི་ནང་དུ་བློ་མཐུན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བཞེད་ན་ཆོས་གོས་སྲ་བརྐྱང་ཉིད་བྱ་བའོ། །

[Block 117]
གདིང་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མཚམས་ཀྱི་ནང་དུ་བློ་མཐུན་པར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 118]
དབྱར་གནས་པ་ལ༌[^102]ནི་མཚམས་སྦྱར་བ་ནི་གང་ཞིག་གདིང་བ་ཡང་ངོ་ཞེས་བྱ་བའོ། །

[Block 119]
དབྱར་གནས་པའི་ཞིང་ལས་གཞན་པ་བློ་མཐུན་པ་འདི་མི་དགེ་བ་བསྐྱེད་པའོ། །

[Block 120]
གང་གི་ཕྱིར་གདིང་བ་བྱས་པ་ལ་འདི་ལ་མཚམས་སྦྱར་བ་ནི་མ་ཡིན་ནོ། །

[Block 121]
དེ་ཐམས་ཅད་ནི་གདིང་བ་ལ་བྱེད་པ་ཉིད་དེ། དེའི་ཕྱིར་བརྗོད་པ་ལ་ཡང་མཚམས་ཀྱི་ནང་དུ་བྱ་བ་ཉིད་ཅེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 122]
གང་ལ་དེ་འབྱུང་བའོ་ཞེས་བྱ་བ་ནི་རྣམ་པ་གང་གིས་གདིང་བ་མི་འབྱུང་བ་སྟེ། སྔར་དབྱར་གནས་པར་ཁས་བླངས་པ་དེ་དག་ལས་གཞན་གདིང་བ་པོར་བློ་མཐུན་པར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 123]
དེ་ལ༌[^103]གཏད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཏན་པ་གདིང་བར་བློ་མཐུན་པར་བྱས་པ་དེ་ཉིད་ལའོ། །ཇི་ལྟར་གཏད་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གསོལ་བར་བྱས་ཏེ་ཞེས་བྱ་བ་སྨོས་ཏེ། གསོལ་བ་འབའ་ཞིག་གི་ལས་བྱ་སྟེ། གཏད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 124]
གང་གི་ཚེ་ཆོས་གོས་མཐུན་པར་བྱས་པའི་ཉི་མ་དེ་ཉིད་ལ་ཡང་འདིང་བ༌[^104]པོ་ལ་གཏད་པར་བྱའོ་ཞེས་བྱ་བ་དེ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 125]
གང་གི་ཕྱིར་ཆོས་གོས་བློ་མཐུན་པར་བྱས་པ་ཉི་མ་གཞན་དུ་གཞག་པར་རིགས་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 126]
བཀྲུ་བ༌[^105]དང་དྲུབས་པ༌[^106]དང་ཁ་བསྒྱུར་བ་དག་ལ་དེས་སྔོན་དུ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེས་ཞེས་བྱ་བ་ནི་གཏན་པ་འདིང་བར༌[^107]བྱེད་པའོ། །ཇི་ལྟར་སྔོན་དུ་འགྲོ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གཉིས་སམ་གསུམ་རྗེས་སུ་བསྒྲུབ་པས༌[^108]སོ་ཞེས་བྱ་བ༌[^109]སྨོས་ཏེ། བྱ་བ་གཉིས་སམ་གསུམ་གྱི་ལས་རྗེས་སུ་བསྒྲུབ་པས་སོ། །

[Block 127]
ཟིན་པ་ཞིག་གྲུབ་ན་རང་གིས་ཁབ༌[^110]སྲུབས་གཉིས་སམ་གསུམ་དྲུབ་པར༌[^111]བྱའོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་ཆོས་གོས་དེ༌[^112]བྱས་ཟིན་པ་ཞིག་གྲུབ་ན་དེའི་ཚེ་སྲ་བརྐྱང་འདིང་བ༌[^113]པོས་དེ་རང་གིས་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 128]
འདིར་གཞུང་ནི། དགེ་སློང་གཏན་པ་འདིང༌[^114]བས་གཏན་པ་འདིང༌[^115]བའི་ཆོས་གོས་བཀྲུ་བར་བྱ་བ་དང་དྲུབ་པར༌[^116]བྱ་བ་དང་། ཁ་བསྒྱུར་བར་བྱ་བ་ལ་སྔོན་དུ་འགྲོ་བར་བྱའོ། །

[Block 129]
གལ་ཏེ་ཟིན་པ་ཞིག་རྙད༌[^117]ན་དེའི་འོག་ཏུ་ཐ་ན་ཁབ་སྲུབས་གཉིས་སམ་གསུམ་དྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 130]
མནོས་པ་དང་རང་བྱེད་པ་དང་། དེའི་མཇུག་དག་ཏུ་གོ་རིམས་བཞིན་དུ་འདིང་བར༌[^118]འགྱུར་རོ། །

[Block 131]
གདིང་ངོ་། །བཏིང་ངོ་སྙམ་དུ་སེམས་བསྐྱེད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། མནོས་པ་ཞེས་བྱ་བ་ནི་དང་པོ་དགེ་འདུན་ལས་གཏན་པ་གདིང་བའི༌[^119]ཆོས་གོས་མནོས་པའི་ཚེའོ། །

[Block 132]
གང་ཞིག་དེར་འདི་རང་གིས་སྒྲུབ་པར་བྱེད་པ་ན་སྔོན་དུ་འགྲོ་བར་འགྱུར་བ་ཟིན་པ་ཞིག་གྲུབ་ན་དེའི་རང་གི་བྱས་པ་དང་བྱེད་པ་དང་། དེའི་མཇུག་དག་ཏུ་གོ་རིམས་བཞིན་དུ་འདིང་བར༌[^120]འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སེམས་གསུམ་པོ་རྣམས་བསྐྱེད་པར་བྱའོ། །

[Block 133]
དང་པོ་ཉམས་ན་མི་འབྱུང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མནོས་པའི་ཚེ་ན་འདིང་བར༌[^121]འགྱུར་རོ་སྙམས༌[^122]དུ་འདི་ཉམས་པ་ལ་གཞན་འོག་མ་གཉིས་རྗེས་སུ་བསྒྲུབ་པས་གདིང་བར་བྱེད་པ་པོ་མི་འབྱུང་བ་མ་ཡིན་ཏེ་འབྱུང་ངོ་། །ཚེ་དང་ལྡན་པ་དག་བདག་སང་གཏན་པ་འདིར་བར༌[^123]འགྱུར་གྱིས་ཁྱེད་ཅག་གིས་རང་རང་གི༌[^124]ཆོས་གོས་རྣམས་དབྱུང་བར་བྱའོ་ཞེས་ཚོགས་པ་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་ཉིད་ཀྱི་ཚིག་གིས་ཤེས་པར་བྱ་སྟེ། སང་འདིང་བར༌[^125]འགྱུར་བ་ཉིད་ལ་འདི་བརྗོད་པའོ། །

[Block 134]
འོ་ན་ཆོས་གོས་གཞན་བྱིན་གྱིས་བརླབ་པ་ཞེས་བྱ་བ་དེ་འདོན་པ་ལ་འཇུག་པ་གྲུབ་པ་དེ་བས་ན་བརྗོད་པ་འདི་དོན་མེད་དོ་ཞེ༌[^126]ན་བརྗོད་པར་བྱ་སྟེ། ཁ་ཅིག་མི་མཁས་པ་དང༌[^127]མཁས་པ་དག་དྲན་པ་བརྗེད་ངས་པ་འབྱུང་སྟེ་དེའི་དོན་དུ་འདི་བྱའོ། །

[Block 135]
འདུ་བའི་སྐབས་རྗེས་སུ་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གདིང་བའི་དོན་དུ་དགེ་འདུན་གང་འདུ༌[^128]བ་གང་ཡིན་པ་དེའི་སྐབས་འདི་ནི་གནས་མལ་བཤམ་པ་དང་། གཎྜཱི་བརྡུང་བ་དང་དྲིས་པའི་ཚིག་གིས་ཡང་དག་པར་བསྒོ་བ༌[^129]རྣམས་ལ་སྟེ་འདིང་བར༌[^130]བྱེད་པ་པོས་བསྒྲུབ་ཅིང་འདིང་བར༌[^131]བྱེད་པ་ཡང་དག་པར་བསྐོ་བ་དང་། དེ་མ་ཐག་པའི་བློ་གདིང་བ་འདིང་བའི༌[^132]དོན་དུ་གང་ཞིག་ཅེས༌[^133]བྱ་བ་དེར་རྟོགས༌[^134]པའོ། །

[Block 136]
དྲི་དང་མེ་ཏོག་གིས་མཆོད་ཅིང་བདུག་སྤོས་དྲི་ཞིམ་པོས་བདུག་པ༌[^135]དུ་མ་གཟེབ་ཀྱི་སྤྲོག་མར་ལྷན་ཅིག་གཞག་པ་ཐོགས་ཏེ། རྒན་རིམས་སུ༌[^136]འདུག་པས་གདིང་བ༌[^137]བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཁ་ཅིག༌[^138]དུ་མ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་གསུམ་མོ། །

[Block 137]
གཅིག་ཏུ་ཞེས་བྱ་བ་ནི་གཟེབ་ཀྱི་སྤྲོག་མར་གནས་པ་ཐོགས་ཏེའོ། །

[Block 138]
དུ་མ་ནི་ཆོས་གོས་ཕྲུགས་གསུམ་སྟེ་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 139]
དུས་གང་གི་ཚེ་ཞེ་ན། དེའི་ཕྱིར་ཚེས་བཅུ་དྲུག་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ།

[Block 140 [VERSE]]
ཚེས་བཅུ་དྲུག་གི་ནང་པར་རོ། །
ཟླ་བ་གང་གི་ཚེ་ན་ཞེ་ན།
དེའི་ཕྱིར་སྟོན་ཟླ་འབྲིང་པོའི་འོ། །

[Block 141]
ལན་གསུམ་བཟླས་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་ཞག༌[^139]ལན་གསུམ་དུ་བཟླས་པས་ཤེ་ན། དེའི་ཕྱིར་གདིང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཏིང་ངོ་ཞེས་བྱ་བའི་སྔགས་འདི་མཚོན་པ་ཙམ་མོ། །

[Block 142]
དགེ་སློང་རེ་རེའི་མདུན་དུ་འདུག་སྟེ་བཏིང་ངོ་ཞེས་གོ༌[^140]བར་བྱ་བ་ནི་དགེ་སློང་དགེ་སློང་གི་མདུན་དུ་འདུག་སྟེ་བཏིང་ངོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་འདི་ཡང་སྔགས་ཀྱི་མཚོན་པ་ཙམ་ཡིན་ནོ། །

[Block 143]
ཅིའི་ཕྱིར་ཡང་དེ་གདིང་བ༌[^141]ལྟར་ལྷན་ཅིག་ཉིད་ཀྱིས་དགེ་འདུན་ལ་ཞུ་བར་མི་བྱ་ཞེ་ན། བྱེ་བྲག་ཏུ་ཆེར་འབྱུང་བ་ཉིད་གྲུབ་པ་ཡོད་མོད་ཅེས་བྱ་བ་མཐོང་བ་ཡིན་ནོ། །

[Block 144]
གཞན་གྱིས་ནི་ལེགས་པར་བཏིང་ངོ་། །ཤིན་ཏུ་བཏིང༌[^142]ངོ་། །འདི་ལ་རྙེད་པ་དང་ཕན་ཡོན་གང་ཡོད་པའི༌[^143]བདག་གི་ཡིན་ནོ་ཞེས་སོ་ཞེས་བྱ་བ་ནི་གང་གི་མདུན་དུ་གནས་པའི་གདིང་བ་པོས་བཏིང་ངོ་ཞེས་བྱ་བ་ཞུས་པ་དེ་ནི་འདིར་གཞན་ནོ། །

[Block 145]
འདི་ལ་རྗེས་སུ་ཡི་རང་བ་ནི་ཉམས་སུ་མྱོང་བ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སོ་སོར་ཉམས་སུ་མྱོང་བ་དེ་ནི་བཏིང་བའི་བྱེད་པ་འདི་བསྐྱེད་པ་ཉིད་དེ།[^144] དེ་བཞིན་དུ་སོ་སོར་ཉམས་སུ་མྱོང་བར་མ་བྱས་པ་ཉིད་འཐོབ་སྟེ། འདི་ལ་རྗེས་སུ་ཡི་རང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
