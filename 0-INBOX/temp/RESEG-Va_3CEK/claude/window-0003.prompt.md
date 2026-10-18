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
སྲོག་གཅོད་པ་སྤོང་བ༌[^70]ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། བར་གྱི་ཚིག་མི་མངོན་པར་བྱས་པའི་ཕྱིར་རོ། །

[Block 107]
སྡོམ་པ་ཐོབ་ཀྱང་བསླབ་པའི་གཞི་རྣམས་ཤེས་པར་བྱ་བའི་ཕྱིར་བསྟན་པ་དགེ་སློང་བཞིན། །ཇི་ལྟར་དགེ་སློང་དང་དགེ་སྦྱོང་གི་སྡོམ་པ་ཐོབ་ཟིན་ཀྱང་ཤེས་པར་བྱ་བའི་ཕྱིར་ཁྱོད་ཀྱི༌[^71]འདི་དང་འདི་ལྟར་དུ༌[^72]བསྡམ་མོ་ཞེས་བསླབ་པའི་གཞི་རྣམས་ཡང་འཛིན་དུ་འཇུག་པ་ལྟར་དགེ་བསྙེན་ཡང་དེ་དང་འདྲ་བས་སྡོམ་པ་མེད་པའི་དགེ་བསྙེན་ནི་མེད་དོ། །

[Block 108 [HEADING]]
### སྣ་གཅིག་སྤྱོད་པ་ལ་སོགས་པའི་དགེ་བསྙེན། ^1-11-0

[Block 109 [VERSE]]
གལ་ཏེ་ཐམས་ཅད་སྡོམ༌[^73]ཡིན་ན། །
སྣ་གཅིག་སྤྱོད་སོགས་ཇི་ལྟ་བུ། །

[Block 110]
གལ་ཏེ་དགེ་བསྙེན་ཐམས་ཅད་དགེ་བསྙེན་གྱི་སྡོམ་པ་ལ་གནས་པ་ཡིན་ན་བཅོམ་ལྡན་འདས་ཀྱིས་སྣ་གཅིག་སྤྱོད་པ་དང་། ཕྱོགས་གཅིག་སྤྱོད་པ་དང་། ཕལ་ཆེར་སྤྱོད་པ་དང་། ཡོངས་སུ་རྫོགས་པར་སྤྱོད་པའི་དགེ་བསྙེན་ཞེས་གསུངས་པ་ཇི་ལྟ་བུ་ཡིན། དེ་བསྲུང་བ་ལ་གསུངས་ཞེས་གྲགས། །གང་ཞིག་བསླབ་པའི་གཞི་གང་སྲུང་བར༌[^74]བྱེད་པ་ནི་དེ་སྤྱོད་པ་ཞེས་གསུངས་པར་ཟད་ཀྱི་ཐམས་ཅད་ཀྱང་སྡོམ་པ་ལ་གནས་པར་ནི་འདྲའོ། །

[Block 111]
འདི་ནི་མདོ་ལས་འདས་པ་ཡིན་ནོ། །

[Block 112]
འདིར་ཅི་ཞིག་མདོ་ལས་འདས། འདི་ལྟར་སྲོག་གཅོད་པ༌[^75]སྤོང་ངོ་ཞེས་དགེ་བསྙེན་ཉིད༌[^76]དུ་ཁས་བླངས་པ་ཁོ་ནས་སྡོམ་པ་འཐོབ་པར་གསུངས་སོ་ཞེས་བྱ་བ་སྟེ། མདོའི་ཚིག་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 113]
མདོའི་ཚིག་ཇི་ལྟ་བུ་ཡིན༌[^77]ཞེ་ན། ཇི་ལྟར་མིང་ཆེན་གྱི་མདོ་ལས་གསུངས་པ་ལས་འབྱུང་བ་བཞིན་ཏེ། དེ་ཉིད་ལས་དགེ་བསྙེན་གྱི་མཚན་ཉིད་བསྟན་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 114]
གང་ལས་འདི་སྐད་དུ་ནམ་འཚོའི་བར་དུ་སྲོག་དང་བསྔོ་བ་སྐྱབས་སུ་སོང་བ་མངོན་པར་རབ་ཏུ་དང་བ་ཞེས་འབྱུང་བ་དེར་ནི་བདེན་པ་མཐོང་བ་དེ་དག་བདག་ཅག་གིས་སྲོག་ལ་ཐུག་ཀྱང་ཆོས་འདི་བཏང་དུ་མི་རུང་ངོ་ཞེས་ཤེས་ནས་དད་པའི་རྒྱུས་སྲོག་གི་ཕྱིར་ཡང་དམ་པའི་ཆོས་ལ་ཁས་འཆེ་བར་སྟོན་པ་ཡིན་གྱི་དེ་སྡོམ་པའི་མཚན་ཉིད་སྟོན་པ་ནི་མ་ཡིན་ནོ། །

[Block 115]
སྲོག་གཅོད་པ༌[^78]སྤོང་བ་ཞེས་ནི་གང་ནས་ཀྱང་མི་འབྱུང་ན་སུ་ཞིག་ཡོངས་སུ་མི་གསལ་བའི་དོན་འདི་འདོན་པར་བྱེད། ཚུལ་ཁྲིམས་ཉམས་པའི་དབང་དུ་བྱས་ནས་ནི་སྣ་གཅིག་སྤྱོད་པ་ལ་སོགས་པ་ཞུ་བ་ཉིད་ཀྱང་མི་འཐད་ན་ལན་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཏེ། དགེ་བསྙེན་གྱི་སྡོམ་པ་ཞེས་པ་སུ་ཞིག་གང་ཞིག་བསླབ་པའི་གཞི་གང་ཉམས་པར་མི་བྱེད་པ་དེ་ནི་དེ་སྤྱོད་པ་ཡིན་ནོ་ཞེས་བྱ་བར་མི་ཤེས་སོ། །

[Block 116]
དགེ་བསྙེན་གྱི་སྡོམ་པའི་ཚད་མི་ཤེས་པས༌[^79]བསླབ་པའི་གཞི་དེ་ཙམ་ཞིག་བཟོད་པ་ལ་ནི་བཙུན་པ་ཇི་ཙམ་གྱིས་ན་སྣ་གཅིག་སྤྱོད་པའི་དགེ་བསྙེན་དུ་འགྱུར་བ་ལགས་ཞེས་བྱ་བ་ནས་ཡོངས་སུ་རྫོགས་པར་སྤྱོད་པ་ལགས་ཞེས་བྱ་བའི་བར་དུ་ཞུ་བ་འདི་རུང་ངོ་། །གལ་ཏེ་སྡོམ་པ་མེད་པའམ་མ་ཚང་བར་ཡང་དགེ་བསྙེན་དུ་འགྱུར་ན་དགེ་སློང་དང་དགེ་སྦྱོང་དག་ཏུ་ཡང་འགྱུར་རོ། །

[Block 117]
རེ་ཞིག་ཇི་ལྟར་ན་དགེ་བསྙེན་གྱི་སྡོམ་པ་ལ་སོགས་པ་འདི་དག་གི་ཡན་ལག་ངེས་པ་ཡིན། སྟོན་པས་བཏགས་པའི་དབང་གིས་སོ། །

[Block 118]
དགེ་བསྙེན་ཉིད་ལ་སོགས་པ་ཡང་སྟོན་པས་བཏགས་པའི་དབང་གིས༌[^80]སོ་སོར་ངེས་པར་འདོད་པར་གྱིས་ཤིག །དགེ་བསྙེན་ནི་སྡོམ་པ་མེད་པར་ཡང་བཏགས་ཀྱི་དགེ་སློང་དང་དགེ་སྦྱོང་དག་ནི་མ་ཡིན་ནོ། །

[Block 119]
ཁ་ཆེ་བ་རྣམས་ནི་འདི་མི་འདོད་དོ། །

[Block 120]
སྡོམ་པ་ཐམས་ཅད་ཀྱང་། ཆུང་ངུ་ལ་སོགས༌[^81]ཡིད་ཇི་བཞིན། །ཆུང་ངུ་དང་། འབྲིང་དང་ཆེན་པོ་ཉིད་ནི་ཡང་དག་པར་ལེན་པའི་སེམས་ཀྱི་དབང་གིས་ཏེ། དེ་ལྟར་བྱས་ན་དགྲ་བཅོམ་པ་ལ༌[^82]ཡང་སོ་སོར་ཐར་པའི་སྡོམ་པ་ཆུང་ངུ་ཡོད་ལ། སོ་སོའི་སྐྱེ་བོ་ལ་ཡང་ཆེན་པོ་ཡོད་པར་འགྱུར་རོ། །

[Block 121]
ཡང་ཅི་སྐྱབས་སུ་འགྲོ་བ་མེད་པར་ཡང་སྡོམ་པ་མནོས་པ་ཁོ་ནས་དགེ་བསྙེན་དུ་འགྱུར་རམ་ཞེ་ན། མི་འགྱུར་ཏེ་མི་ཤེས་པ་ནི་མ་གཏོགས་སོ། །

[Block 122 [HEADING]]
### སྐྱབས་སུ་འགྲོ་བ། ^1-12-0

[Block 123]
གང་ཞིག་སངས་རྒྱས་དང་ཆོས་དང་དགེ་འདུན་ལ་སྐྱབས་སུ་འགྲོ་བ་དེ་ཅི་ལ་སྐྱབས་སུ་འགྲོ་ཞེ་ན།

[Block 124 [VERSE]]
གང་ཞིག་གསུམ་ལ་སྐྱབས་འགྲོ་དེ། །
སངས་རྒྱས་དགེ་འདུན་བྱེད་པའི་ཆོས། །
མི་སློབ་པ་དང་གཉི་ག་དང་། །
མྱ་ངན་འདས་ལ་སྐྱབས་སུ་འགྲོ། །

[Block 125]
གང་ཞིག་སངས་རྒྱས་ལ་སྐྱབས་སུ་འགྲོ་བ་དེ་ནི་སངས་རྒྱས་སུ་བྱེད་པའི་ཆོས་མི་སློབ་པ་ལ་སྐྱབས་སུ་འགྲོ་བ་ཡིན་ཏེ། གང་དག་གཙོ་བོར་གྱུར་པས་སྐུ་དེ་སངས་རྒྱས་ཞེས་བརྗོད་པའམ། ཡང་ན་གང་དག་བརྙེས་པས་ཐམས་ཅད་ཐུགས་སུ་ཆུད་པར་སྤྱོད་པའི་ཕྱིར་སངས་རྒྱས་ཡིན་པའོ། །

[Block 126]
དེ་དག་ཀྱང་གང་ཞེ་ན། ཟད་པ་ཤེས་པ་ལ་སོགས་པ་འཁོར་དང་བཅས་པ་ཡིན་ནོ། །

[Block 127]
གཟུགས་ཀྱི་སྐུ་ནི་སྔ་མ་དང་ཕྱི་མར་ཡང་བྱེ་བྲག་མེད་པའི་ཕྱིར་རོ། །

[Block 128]
ཅི་སངས་རྒྱས་ཐམས་ཅད་ལའམ། འོན་ཏེ་གཅིག་ལ་ཞེ་ན། མཚན་ཉིད་ཀྱི་སྒོ་ནས་ནི་སངས་རྒྱས་ཐམས་ཅད་ལ་སྟེ། ལམ་མཚན་ཉིད་མི་འདྲ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 129]
གང་ཞིག་དགེ་འདུན་ལ་སྐྱབས་སུ་འགྲོ་བ་དེ་ནི་དགེ་འདུན་དུ་བྱེད་པའི་ཆོས་སློབ་པ་དང་། མི་སློབ་པ་ལ་སྐྱབས་སུ་འགྲོ་བ་ཡིན་ཏེ། གང་དག་ཐོབ་པས་གང་ཟག་བརྒྱད་པོ་མི་ཕྱེད་པའི༌[^83]ཕྱིར་དགེ་འདུན་དུ་འགྱུར་བའོ། །

[Block 130]
ཅི་དགེ་འདུན་ཐམས་ཅད་ལའམ། འོན་ཏེ་གཅིག་ལ་ཞེ་ན། མཚན་ཉིད་ཀྱི་སྒོ་ནས་ནི་ཐམས་ཅད་ལ་སྟེ། ལམ་མཚན་ཉིད་མི་འདྲ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 131]
གང་མདོ་ལས་གང་ཡང་མ་འོངས་པའི་དུས་ན་དགེ་འདུན་ཞེས་བྱ་བ་འབྱུང་བར་འགྱུར་བ་དེ་ལ་ཡང་སྐྱབས་སུ་སོང་ཞིག་ཞེས༌[^84]གསུངས་སོ་ཞེ་ན། དེ་དག་གི་ནི༌[^85]མངོན་སུམ་དུ་འགྱུར་བའི་དགེ་འདུན་དཀོན་མཆོག་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 132]
གང་ཞིག་ཆོས་ལ་སྐྱབས་སུ་འགྲོ་བ་དེ་ནི་མྱ་ངན་ལས་འདས་པ་སོ་སོར་བརྟགས་པས་འགོག་པ་ལ་སྐྱབས་སུ་འགྲོ་བ་ཡིན་ཏེ།[^86] བདག་དང་གཞན་གྱི་རྒྱུད་ཀྱི་ཉོན་མོངས་པ་རྣམས་དང་། སྡུག་བསྔལ་ཞི་བར་མཚན་ཉིད་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 133]
གལ་ཏེ་མི་སློབ་པའི་ཆོས་དག་ཁོ་ན་སངས་རྒྱས་ཡིན་ན་ཇི་སྲིད་དེ་བཞིན་གཤེགས་པ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་ཕྱུང་བས་མཚམས་མེད་པར་འགྱུར། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ། རྟེན་ལ་གནོད་པ་བྱས་པས་དེ་དག་ལ་ཡང་གནོད་པ་བྱས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 134]
བསྟན་བཅོས་ལས་ནི་མི་སློབ་པའི་ཆོས་ཁོ་ན་སངས་རྒྱས་ཡིན་ནོ་ཞེས་དེ་སྐད་དུ་མི་འབྱུང་ངོ་། །འོ་ན་ཇི་སྐད་དུ་འབྱུང་ཞེ་ན། སངས་རྒྱས་སུ་བྱེད་པའི་ཆོས་ཞེས་འབྱུང་སྟེ། དེའི་ཕྱིར་རྟེན་སངས་རྒྱས་ཉིད་དུ་མ་བཀག༌[^87]པས་དེ་ནི་ཀླན་ཀར་མི་རུང་བ་ཉིད་དོ། །

[Block 135]
དེ་ལྟ་མ་ཡིན་ན་འཇིག་རྟེན་པའི་སེམས་ལ༌[^88]གནས་པ་སངས་རྒྱས་ཀྱང་མ་ཡིན་པར་འགྱུར། དགྲ་བཅོམ་པ་ཡང་མ་ཡིན་པར་འགྱུར་ལ་དགེ་སློང་དུ་བྱེད་པའི་ཚུལ་ཁྲིམས་ཁོ་ན་ཡང་དགེ་སློང་དུ་འགྱུར་རོ། །

[Block 136]
ཇི་ལྟར་གང་ཞིག་དགེ་སློང་ལ་མཆོད་པ་བྱེད་པ་དེ་དགེ་སློང་དུ་བྱེད་པའི་ཚུལ་ཁྲིམས་ལ་མཆོད་པ་བྱེད་པ་ཡིན་པ་དེ་བཞིན་དུ། གང་ཞིག་སངས་རྒྱས་ལ་སྐྱབས་སུ་འགྲོ་བ་དེ་ཡང་མི་སློབ་པ་སངས་རྒྱས་སུ་བྱེད་པའི་ཆོས་དག་ལ་སྐྱབས་སུ་འགྲོ་བ་ཡིན་ནོ། །

[Block 137]
གཞན་དག་ན་རེ་གང་ཞིག་སངས་རྒྱས་ལ་སྐྱབས་སུ་འགྲོ་བ་དེ་ནི་སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པ་བཅོ་བརྒྱད་ལ་སྐྱབས་སུ་འགྲོ་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 138]
སྐྱབས་སུ་འགྲོ་བ་རྣམས་ཀྱི་རང་བཞིན་ཅི་ཞེ་ན། ངག་གི་རྣམ་པར་རིག་བྱེད་ཀྱི་ངོ་བོ་ཉིད་དག་ཡིན་ནོ། །

[Block 139]
ཡང་སྐྱབས་ཀྱི་དོན་ཅི་ཞེ་ན། དེ་ལ་བརྟེན་ནས་སྡུག་བསྔལ་ཐམས་ཅད་ལས་གཏན་དུ་ངེས་པར་ཐར་པའི་ཕྱིར་རོ། །

[Block 140]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་།

[Block 141 [VERSE]]
འཇིགས་པས་སྐྲག་པའི་མི་རྣམས་ནི། །
ཕལ་ཆེར་རི་དང་ནགས་ཚལ་དང་། །
ཀུན་དགའ་དང་ནི་མཆོད་གནས་ཀྱི། །
ལྗོན་ཤིང་རྣམས་ལ་སྐྱབས་འགྲོ་སྟེ། །

[Block 142 [VERSE]]
སྐྱབས་དེ་གཙོ་བོ་མ་ཡིན་ཞིང་། །
སྐྱབས་དེ་མཆོག་གྱུར་མ་ཡིན་ལ། །
སྐྱབས་དེ་ལ་ནི་བརྟེན༌[^89]ནས་ཀྱང་། །
སྡུག་བསྔལ་ཀུན་ལས་མི་གྲོལ་གྱི། །

[Block 143 [VERSE]]
གང་ཚེ་གང་ཞིག་སངས་རྒྱས་དང་། །
ཆོས་དང་དགེ་འདུན་སྐྱབས་སོང་ལ། །
སྡུག་བསྔལ་སྡུག་བསྔལ་ཀུན་འབྱུང་དང་། །
སྡུག་བསྔལ་ཡང་དག་འདས་པ་དང་། །

[Block 144 [VERSE]]
འཕགས་ལམ་ཡན་ལག་བརྒྱད་བདེ་བ། །
མྱ་ངན་འདས་པར་འགྲོ་འགྱུར་དང་། །
འཕགས་པའི་བདེན་པ་བཞི་པོ་དག །
ཤེས་རབ་ཀྱིས་ནི་ལྟ་བྱེད་པ། །

[Block 145 [VERSE]]
སྐྱབས་དེ་གཙོ་བོ་ཡིན་པ་སྟེ། །
སྐྱབས་དེ་མཆོག་ཏུ་གྱུར་པ་ཡིན། །
སྐྱབས་དེ་ལ་ནི་བརྟེན་ནས་ཀྱང་། །
སྡུག་བསྔལ་ཀུན་ལས་འགྲོལ་བར༌[^90]འགྱུར། །
--- END BLOCKS ---
