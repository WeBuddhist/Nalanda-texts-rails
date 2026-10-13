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
དངོས་པོ་དང་དངོས་པོ་མེད་པའི་མཚན་མ་ལ་རྟོག་པ་ལས་བྱུང་བའི་འདོད་ཆགས་ལ་སོགས་པ་ནི༌[^65]ཁམས་གསུམ་ལས་མི་འདའ་བའི་རྒྱུར་གྱུར་པས་བྱིས་པ་རྣམས་ནི་འཆིང་བ་སྟེ། དེས་བྱིས་པ་དག་འཇུག་པ་ལ་རང་དབང་མེད་པར་བྱས་ནས་འགྲོ་བ་ལྔར་འཁོར་བ་ན་འཁོར་རོ། །

[Block 107]
དངོས་པོ་དང་དངོས་པོ་མེད་པ་མི་དམིགས་པ་ནི་དེའི་མཚན་མ་རྟོག༌[^66]པ་མེད་པའི་ཕྱིར༌[^67]མི་སྐྱེ་བས་ངེས་པར་འདོད་ཆགས་ལ་སོགས་པའི་རྒྱུན་ཆད་དོ། །

[Block 108]
དེ་དག་རྒྱུན་ཆད་པས་རྣམ་པར་གྲོལ་བར་འགྱུར་བས་ན།[^68] འདི་ཉིད་རྣམ་པར་གྲོལ་བའི་ཐབས་སུ་རིགས།[^69] །འདིར་སྨྲས་པ། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་ནི་ཡོད་དོ། །

[Block 109]
གལ་ཏེ་དེ་དག་མེད་དུ་ཟིན་ན་དེའི་ཚེ་ཁྱོད་ཀྱི་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ཡང་མེད་པར་འགྱུར་རོ། །

[Block 110]
འཁོར་བ་ནི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔའི་རང་གི་ངོ་བོ་ཡིན་པས་དངོས་པོའི་ངོ་བོ་སྟེ། ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ་དེ་དག་ཉིད་ལས༌[^70]ཉོན་མོངས་པས་འཕངས་ནས། འགྲོ་བ་རྣམས་སུ་འགྲོ་བ་ནས་འགྲོ་བ་གཞན་དུ་འགྲོ་བའི་ཕྱིར། འཁོར་བ་ཞེས་བྱ་བས་ན་དེ་ཡང་ཡོད་དོ། །

[Block 111]
དེ་ཡོད་པས་ན་དངོས་པོ་ཡོད་པ་ཉིད་དོ། །

[Block 112]
མྱ་ངན་ལས་འདས་པ་ཐར་པ་ནི་འཁོར་བ་ཟད་པའི་རང་བཞིན་ཏེ། སྡུག་བསྔལ་ཕྱིས༌[^71]མི་སྐྱེ་བས་དེའི༌[^72]དངོས་པོ་མེད་པའོ། །

[Block 113]
དེ་བས་ན་འཁོར་བ་མེད་པའི་དངོས་པོ་མྱ་ངན་ལས་འདས་པ་ཡང་སྲིད་དེ་ཡོད་དོ། །

[Block 114]
བཤད་པ་གལ་ཏེ་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་དེ་གཉིས་ཡོད་ན་ནི་དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉིས་ཀྱང་ཡོད་པར་འགྱུར་བ་ཞིག་ན། དེ་གཉིས་ནི་མེད་དོ། །

[Block 115]
འོ་ན་དེ་གཉིས་ཡོད་ཅེས༌[^73]བཅོམ་ལྡན་འདས་ཀྱིས་མ་གསུངས་སམ། འདི་ལྟར་འཁོར་བ་ཡོངས་སུ་ཟད་པར་བྱ་བ་དང་། མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་བྱ་བའི་ཕྱིར་ཡང་ཆོས་བསྟན་ཏོ། །

[Block 116]
གལ་ཏེ་དེ་དག་མེད་ན་དེའི་ཚེ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་ཆོས་བསྟན་པ་ཡང་དོན་མེད་པར་འགྱུར་བ་ཞིག་ན་དོན་མེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 117]
དེ་བས་ན་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ཡོད་པས་དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉིས་ཀྱང་གྲུབ་པོ། །བཤད་པ་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་གཉིས་སུ༌[^74]བཤད། སྨྲས་པ་འཕགས་པ་རྣམས་ལའོ། །

[Block 118]
གལ་ཏེ་འཕགས་པ་རྣམས་ལ་ནི། གལ་ཏེ་འཕགས་པར་གྱུར་ཟིན་པ་རྣམས་ལ་དེ་བཤད་པར་སེམས་ན་ནི་དེ་དག་དེ༌[^75]བཤད་པ་གང་གིས་འཕགས་པ་རྣམས་སུ་འགྱུར། དེ་ལྟར་ན་འོ་ན་ནི་འཕགས་པར་འགྱུར་བའི་ཕྱིར་དེ་བསྟན་ཏོ། །

[Block 119]
གལ་ཏེ་དེ་ལྟ༌[^76]ན་དེ་ཐོས་པ་དང་སེམས་པ་ལ་སོགས་པའི་རིམ་གྱིས་འཕགས་པར་འགྱུར་བས་འདི་ནི་འཕགས་པ་མ་ཡིན་པ་རྣམས་ཀྱི་ཆེད་དུ་གྱུར་ཏོ། །

[Block 120]
འཕགས་པ་མ་ཡིན་པ་དེ་དག་ནི་ཐོག་མ་མེད་པ་ཅན་གྱི་འཁོར་བ་ན་དངོས་པོར་ལྟ་བ་ལ་གོམས་པས་དེའི་གཉེན་པོར་འཁོར་བ་ལྡོག་པའི་མཚན་ཉིད་ཆོས་ཤིན་ཏུ་བཟང་པོ་མྱ་ངན་ལས་འདས་པ་མ་བསྟན་ན། དངོས་པོར་ཆགས་པ་ལས་བཟློག་པར་མི་ནུས་སོ། །

[Block 121]
འཇིག་རྟེན་ནི་བདེ་བ་རྒྱ་ཆེན་པོ་དང་ལྡན་པར་འདོད་པས་དེ་ལ་དེ་ཉེ་བར་བསྟན་ན་བདེ་བ་ལས་ཀྱང་བཟློག་པར་ནུས་ན། རབ་ཏུ་སྡུག་བསྔལ་ལ་སོགས་པ་ལྟ༌[^77]སྨོས་ཀྱང་ཅི་དགོས་ཏེ། དེ་བས་ན་མྱ་ངན་ལས་འདས་པ་དེ་བསྟན་ཏེ། དེ་སྐྱེ་བོ་བྱིས་པ་རྣམས་ཀྱི་ཆེད་དུ་གྱུར་པ་ཉིད་ཡིན་པར་བསྟན་པའི་ཕྱིར།

[Block 122 [HEADING]]
### ཚིགས་བཅད་ལྔ་པ། ^1-6-0

[Block 123 [VERSE]]
ཡང་དག་མ་མཐོང་འཇིག་རྟེན་དང་། །
མྱ་ངན་འདས་པར་རློམ་སེམས་ཏེ། །

[Block 124]
ཞེས་སྨོས་སོ། །

[Block 125]
དེ་ཁོ་ན་མ་མཐོང་བ་ནི་འཁོར་བ་ཞེས་བརྗོད་པ། འཇིག་རྟེན་དང་དེ་ལྡོག་པ་ཞེས་བརྗོད་པ་མྱ་ངན་ལས་འདས་པ་འདི་གཉིས་ལ་མི་མཐུན་པའི་ཕྱོགས་དང་གཉེན་པོའི་དངོས་པོར་གནས་ཤིང་གཅིག་ནི་བླང་གཅིག་ནི་དོར་བར་སེམས། དེ༌[^78]དེའི་ཕྱིར་ཏེ་སྐྱེ་བོ་འཁོར་བ་ལ་རྒྱབ་ཀྱིས་ལྟ་བར་འགྱུར་ཞིང༌[^79]དེ་ལྡོག་པ་ལ་མོས་པ་སྐྱེས་པ་དག་ལ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་བསྟན་པས་སྤང་བར་བྱ་བའི་སྐྱེ་བ་མེད་པ་བདེ་བར་རྟོགས་པར་ནུས་སོ། །

[Block 126]
དངོས་པོ་སྐྱེ་བ་མེད་པར་རྟོགས་ན་དངོས་པོ་མེད་པ་ལ་ཅི་ཞིག་གི་དངོས་པོ་མེད་པ་མྱ་ངན་ལས་འདས་པར་བརྟག་ཅེས་མྱ་ངན་ལས་འདས་པ་ལ་མངོན་པར་ཆགས་པ་ཡང་བདེ་བར་སྤོང་ནུས་སོ། །

[Block 127]
དེ་ལྟར་དེ་ཁོ་ན་ཉིད་མཐོང༌[^80]ལ་ཞུགས་ནས་འཕགས་པར་གྱུར་པ་དེ་ནི།

[Block 128 [VERSE]]
ཡང་དག་མཐོང་བས་འཇིག་རྟེན་དང་། །
མྱ་ངན༌[^81]འདས་པར་རློམ་སེམས་མེད། །

[Block 129]
འཕགས་པ་ངོ་བོ་ཉིད་མི་དམིགས་པའི་ཆོས་རྟོགས་པས་རབ་ཏུ་ཕྱེ་བ་རྣམས་ནི་དེ་གཉི་ག་མི་དམིགས་ཤིང་མི་རྟོག་གོ་ཞེས་བྱ་བར་དགོངས་སོ། །

[Block 130]
དེ་བས་ན་བྱིས་པའི་སྐྱེ་བོའི་རྟོག་པའི་དབང་དུ་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་གཉིས་ཡོད་དོ་ཞེས་བསྟན་པས་དངོས་པོ་དང་དངོས་པོ་མེད་པ་གཉིས་ཡོད་དོ་ཞེས་གང་སྨྲས་པ་དེ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 131]
གལ་ཏེ་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་གཉིས་འཕགས་པ་ལ་བསྟན་པ་མ་ཡིན་ན། འཕགས་པའི་བདེན་པ་བཞི་པོ་དེ་དག་བསྟན་པ་དེ་ཇི་ལྟར་རུང་བར་འགྱུར། གལ་ཏེ་འདི་དག་འཕགས་པ་རྣམས་ལ་བདེན་པ་ཡིན་ན་ནི་དེའི་ཚེ་འཕགས་པའི་བདེན་པ་རྣམས་ཞེས༌[^82]བྱར་རུང་ངོ་། །གལ་ཏེ་དེ་དག་འཕགས་པ་མ༌[^83]ཡིན་པ་དང་སྦྱར་ན་ནི་དེའི་ཚེ་འཕགས་པའི་བདེན་པ་ཞེས་བྱར་མི་རུང་ངོ་། །གལ་ཏེ་དེ་ལྟ་ན་འཕགས་པའི་ཐ་སྙད་བརྒྱད་ཀྱང་ཇི་ལྟར་རུང་བར་འགྱུར། དེ་དག་ནི་འཕགས་པ་ཉིད་ཀྱི་མ་ཡིན་གྱི། ཐ་སྙད་དེ་དག་ཟག་པ་དང་བཅས་པས༌[^84]འཇིག་རྟེན་གྱི་ཡིན་ནོ། །

[Block 132]
དེ་བས་ན་འཇིག་རྟེན་གྱི་དངོས་པོ་ལ་ཡང་གང་ཇི་ལྟར་གནས་པ་བཞིན་དུ་རང་གི་ངོ་བོ་ལས་མི་བསྒྱུར་བར་རྣམ་པར་གཞག་པ་དེ་ཡང་འཕགས་པ་ཞེས་བརྗོད་དུ་རུང་ངོ་། །

[Block 133]
ཡང་ན་འཕགས་པར་འགྱུར་བའི་བདེན་པ་རྣམས་ནི་འཕགས་པའི་བདེན་པ༌[^85]རྣམས་སོ། །

[Block 134]
གང་ལ་དམིགས་པ་ཡོད་པ་ཡང་དམིགས་པ་དེ་ནི་རྣམ་པ་གཉིས་ཏེ། དེ་ལ་ཕྱིན་ཅི་ལོག་དང་ཕྱིན་ཅི་མ་ལོག་པའོ། །

[Block 135]
དེ་ལ་ཕྱིན་ཅི་ལོག་ནི་བདེ་བ་ལ་སོགས་པར་འཛིན་པ་སྟེ། ཀུན་རྫོབ་ཏུ་ཡང་དེའི་བདག་ཉིད་དུ་དངོས་པོ་རྣམ་པར་མི་གནས་པའི་ཕྱིར་རོ། །

[Block 136]
ཕྱིན་ཅི་མ་ལོག་པ་ནི་སྡུག་བསྔལ་བ་ལ་སོགས་པ་སྟེ། [^86]དངོས་པོ་ཀུན་རྫོབ་ཏུ་ཡང་དེའི་བདག་ཉིད་དུ་དངོས་པོ་རྣམ་པར་མི་གནས་པའི་ཕྱིར་རོ། །

[Block 137]
ཕྱིན་ཅི་མ་ལོག་པ་ནི་སྡུག་བསྔལ་བ་ལ་སོགས་པ་སྟེ། དངོས་པོ༌[^87]ཀུན་རྫོབ་ཏུ་དེའི་བདག་ཉིད་དུ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 138]
དེ་ཙམ་ཞིག་དང་སྦྱར་ནས་འཕགས་པའི་ཐ་སྙད་ཅེས་བྱ་བ་བཞིན་དུ་འཕགས་པའི་བདེན་པ་རྣམས་ཞེས་བྱའོ། །

[Block 139]
ཅི་མྱ་ངན་ལས་འདས་པ་ཡང་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཡིན་ནམ། དེ་དེ་བཞིན་ཏེ། འཁོར་བར་ཡོངས་སུ་རྟོག་པ་ཡོད་ན་མྱ་ངན་ལས་འདས་པར་ཡོངས་སུ་རྟོག་སྟེ།[^88] དེ་གཉི་ག་ཡང་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 140]
དེ་བས་ན་བཅོམ་ལྡན་འདས་མ་ལས་གསུངས་པ། ཚེ༌[^89]དང་ལྡན་པ་རབ་འབྱོར་མྱ་ངན་ལས་འདས་པ་ཡང་སྒྱུ་མ་ལྟ་བུ་རྨི་ལམ་ལྟ་བུའོ་ཞེས་སྨྲའམ། ཤཱ་རིའི་བུ༌[^90]མྱ་ངན་ལས་འདས་པ་བས་ཆེས་ལྷག་པའི་ཆོས་ཤིག་ཡོད་ན་ཡང་སྒྱུ་མ་ལྟ་བུའོ་ཞེས་ཁོ་བོ་སྨྲའོ་ཞེས་འབྱུང་ངོ་། །གལ་ཏེ་དེ༌[^91]འཁོར་བར་རྟོག་པ་ལ་ལྟོས་པ་མ་ཡིན་ན་དེ་སྒྱུ་མ་ལྟ་བུར་མི་འགྱུར་རོ། །

[Block 141]
དེ་བས་ན་མྱ་ངན་ལས་འདས་པ་ཡང་ཀུན་རྫོབ་ཀྱི་བདེན་པར་ཡོངས་སུ་བརྟགས་པ་ཡིན་ནོ། །

[Block 142]
གལ་ཏེ་དེ་ལྟར་ན་མྱ་ངན་ལས་འདས་པ་དོན་དམ་པའི་བདེན་པའོ་ཞེས་ཇི་སྐད་དུ་བཤད། དེའི་བདག་ཉིད་དུ་འཇིག་རྟེན་ལ་མི་སླུ་བའི༌[^92]ཕྱིར་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱིས་དོན་དམ་པའི་བདེན་པ་ཞེས་བཤད་དོ། །

[Block 143]
སླུ་བ༌[^93]འདུས་བྱས་གང་ཡིན་པ་དེ་ནི་དོན་དམ་པའི་བདེན་པ་མ་ཡིན་ནོ། །

[Block 144]
བདེན་པ་གསུམ་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དེ་ངོ་བོ་ཉིད་ཡོད་པར་སྣང་བས་བྱིས་པ་རྣམས་ལ་སླུ་བའི༌[^94]ཕྱིར་ཀུན་རྫོབ་ཀྱི་བདེན་པར་རྣམ་པར་གཞག་གོ། །

[Block 145]
འོ་ན་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་དག་འདི་ལྟ་སྟེ། མི་སླུ་བའི་ཆོས་ཅན་མྱ་ངན་ལས་འདས་པ་འདི་ནི་བདེན་པའི་མཆོག་གཅིག་པུའོ་ཞེས་གསུངས་པ་དེ་ཇི་ལྟ་བུ། ཇི་ལྟར་འདུས་བྱས་ལོག་པར་སྣང་བས་བྱིས་པ་རྣམས་ལ་སླུ་བ༌[^95]དེ་བཞིན་དུ་མྱ་ངན་ལས་འདས་པ་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། རྟག་པར་སྐྱེ་བ་མེད་པའི་རང་གི་ངོ་བོར་གནས་པའི་ཕྱིར་དེ་ནི་བྱིས་པ་རྣམས་ལ་འདུས་བྱས་ལྟར་སྐྱེ་བའི་ངོ་བོར་ནམ་ཡང་མི་སྣང་ངོ་། །དེ་བས་ན་མྱ་ངན་ལས་འདས་པ་ནི་རྟག་ཏུ་མྱ་ངན་ལས་འདས་པ་ཉིད་དུ་གནས་པས་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱིས་དོན་དམ་པའི་བདེན་པ་ཞེས་བཤད་དོ། །
--- END BLOCKS ---
