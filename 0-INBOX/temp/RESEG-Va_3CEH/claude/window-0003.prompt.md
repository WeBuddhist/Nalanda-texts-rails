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
དེ་ལས་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 107]
ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས་ནི་ས་དག་གོ། །

[Block 108]
ས་དག་ནི་བསླབ་པའོ། །

[Block 109]
བསླབ་པ་ལས་ནི་སྤངས་པ་དང་ཡེ་ཤེས་ཏེ། མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་ནི་སྐུ་གསུམ་གྱིས༌[^65]བསྡུས་པའོ། །

[Block 110]
དེ་དག་ཉིད་ནི་སངས་རྒྱས་ཞེས་བྱ་སྟེ། དེ་བས་ན་གོ་རིམས་ནི་འདི་ལྟར་བསྟན་ཏོ། །

[Block 111]
རྣམ་གྲངས་གཞན་ཡང་བྱང་ཆུབ་ཆེན་པོ་ཀུན་ཏུ་སྒྲུབ་པར་བྱེད་པ་ཞེས་བྱ་བ་ནི་སྤྲོས་པ་མེད་པ་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀུན་ཏུ་འདྲེན་པའོ། །

[Block 112]
ཤིན་ཏུ་འཐད་པ་ནི་རིགས་པའི་ཚད་མ་གསུམ་དང་མི་འགལ་ལོ།[^66] །མཐུན་པ་ཞེས་བྱ་བ་ནི་སྔར་རྗེས་སུ་མཐུན་པར་གྱུར༌[^67]ལ། ཕྱིས་འགལ་བ་མ་ཡིན་པ་སྟེ།[^68] ཇི་སྐད་དུ།

[Block 113 [VERSE]]
དགེ་ལ་རྗེས་སུ་ཆགས་པ་དང་། །
གནོད་ལ་ཕན་པ་བྱེད་པ་ལ། །
དཀར་ནག་ངོ་བོར་མི་ལྟ༌[^69]བའི། །
དང་པོའི་རྩ་བ་སྙིང་རྗེ་འདོད། །

[Block 114]
ཅེས་བྱ་བས༌[^70]སོ། །

[Block 115]
ཐམས་ཅད་མཁྱེན་པས༌[^71]ཡེ་ཤེས་འཐོབ་པར་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་རྒྱུན་མི་འཆད་པར་རྣམ་པ་ཐམས་ཅད་ཀྱིས་མཁྱེན་པ་འབྱུང་བ་ཉིད་དོ། །

[Block 116]
ཤིན་ཏུ་འཐད་པ་ལ་སོགས་པ་དག་གི་དོན་བཞིན༌[^72]ཡང་ཤིན་ཏུ་འཐད་པ་མཐུན་པ་འགལ་བ་མེད་པ་ཞེས་བྱ་བ་ནི་བསྟན་པ་དང་བཤད་པ་ཉིད་དེ། ཇི་ལྟར་ཞེ་ན། ཤིན་ཏུ་འཐད་པ་ནི་མཐུན་པ་འགལ་བ་མེད་པར་གནས་པས་སོ། །

[Block 117 [HEADING]]
### རྣམ་གྲངས་རྣམ་པར་གཞག་པ། ^1-3-0

[Block 118]
དེ་ལ་ཀུན་གཞི་རྣམ་པར་ཤེས་པ༌[^73]ཉིད་ཀྱི་ལུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཆོས་མངོན་པ་དེ་ཉིད་ལས་དང་པོར་བསྟན་པ་ཐོག་མ་མེད་པའི་དུས་ཀྱི་དབྱིངས་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་གསུངས་ཏེ།

[Block 119 [HEADING]]
#### ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཉིད་ཀྱི་ལུང། ^1-3-1-0

[Block 120 [VERSE]]
དབྱིངས་ཞེས་བྱ་བ་ནི་རྒྱུའོ། །
ཆོས་རྣམས་ཀུན་གྱི་གནས་ཡིན་ཏེ། །

[Block 121]
ཞེས་བྱ་བ་ནི་གང་རྒྱུ་ཡིན་པ་དེས་ན་ཆོས་ཐམས་ཅད་ཀྱི་གནས་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 122]
དེ་ཡོད་པས་དེ་ཆོས་རྣམས་ཀུན་གྱི་གནས་ཡོད་ན་འགྲོ་ཀུན་ཏེ། གང་སུ་འཁོར་བ་ན་ཡོད་པའི་འགྲོ་བའོ། །

[Block 123]
འགྲོ་བ་འབའ་ཞིག་མ་ཡིན་གྱི་མྱ་ངན་ལས་འདས་པའང་སྟེ། དེ་ཡོད་པས་ན་ཀུན་ནས་ཉོན་མོངས་པ་དང་མྱ་ངན་ལས་འདས་པ་ཉིད་ཀྱང་ངོ་། །དེ་ནི་ཤེས་བྱའི་གནས་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཉིད་ཀྱི་ལུང་ངོ་། །ལུང་གཞན་ཡང་།

[Block 124 [VERSE]]
ཆོས་རྣམས་ཀུན་གྱི་གནས་ཡིན༌[^74]ཏེ། །
རྣམ་ཤེས་ས་བོན་ཐམས་ཅད་པ། །

[Block 125]
ཞེས་བྱ་བ་ལ། རྐང་པ་དང་པོ་ནི་རྐང་པ་གཉིས་པས་བཤད་དོ། །

[Block 126]
དམ་པ་དག་ལ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་ངེས་པའི་ཚིག་ཡིན་གྱི། ཀུན་གཞི་རྣམ་པར་ཤེས་པ༌[^75]ནི་མ་ཡིན་ནོ། །

[Block 127]
དེར་སྦྱོར་བ་ཞེས་བྱ་བ་ནི་གནས་པའོ། །

[Block 128]
སྐྱེ་བ་ཅན་ཞེས་བྱ་བ་ནི་གང་དག་ལ་སྐྱེ་བ་ཡོད་པ་དེ་དག་ལ་སྐྱེ་བ་ཅན་ཞེས་བྱས་ནས་སོ། །

[Block 129]
ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་ཞེས་བྱ་བ་ནི་རྣམ་པར་བྱང་བ་ལས་བཟློག་པའི་དོན་ཏོ། །

[Block 130]
སེམས་ཅན་དག་སྐྱེས་པའི༌[^76]དེའི་བདག་ཉིད་དུ་སྦྱོར་བས་ཞེས་བྱ་བ་ནི་འཛིན་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 131 [HEADING]]
#### ལེན་པའི་རྣམ་པར་ཤེས་པ། ^1-3-2-0

[Block 132]
ཡང་འདིའི་ལུང་ནི་དགོངས་པ་ངེས་པར་འགྲེལ་པ་དེ་ལས་བློ་གྲོས་ཡངས་པ་འགྲོ་བ་དྲུག་གི་འཁོར་བ་འདི་ན་སེམས་ཅན་གང་དང་གང་དག་སེམས་ཅན་གྱི་རིས་གང་དང་གང་དུ་ཡང་སྒོ་ང་ལས་སྐྱེ་བའི༌[^77]སྐྱེ་གནས་སམ། ཡང་ན་མངལ་ལས་སྐྱེ་བའམ། ཡང་ན་དྲོད་གཤེར་ལས་སྐྱེ་བའམ། ཡང་ན་རྫུས་ཏེ་སྐྱེ་བའི་སྐྱེ་གནས་སུ་ལུས་མངོན་པར་འགྲུབ་ཅིང་འབྱུང་བར་འགྱུར་བ་དེའི༌[^78]དང་པོར༌[^79]འདི་ལྟར་ལེན་པ་རྣམ་པ་གཉིས་སོ།[^80] །རྟེན་པ༌[^81]དང་བཅས་པའི་དབང་པོ་གཟུགས་དང་། ལེན་པ་དང་། མཚན་མ་དང་། མིང་དང་། རྣམ་པར་རྟོག་པ༌[^82]ལ་ཐ་སྙད་འདོགས་པའི་སྤྲོས་པའི་བག་ཆགས་ལེན་པ་ལ་བརྟེན་ནས་ས་བོན་ཐམས་ཅད་པའི་སེམས་རྣམ་པར་སྨིན་ཅིང་འཇུག་ལ་རྒྱས་ཤིང་འཕེལ་བ་དང་ཡངས་པར་འགྱུར་རོ། །

[Block 133]
དེ་ལ་གཟུགས་ཅན་གྱི་ཁམས་ན་ནི་ལེན་པ་གཉི་ག་ཡོད་ལ། གཟུགས་ཅན་མ་ཡིན་པའི་ཁམས་ན་ནི་ལེན་པ་གཉིས་སུ་མེད་དོ། །

[Block 134]
བློ་གྲོས་ཡངས་པ་རྣམ་པར་ཤེས་པ་དེ་ནི་ལེན་པའི་རྣམ་པར་ཤེས་པ་ཞེས་ཀྱང་བྱ་སྟེ། འདི་ལྟར་དེས་ལུས་འདི་གཟུང་ཞིང་བླངས་པའི་ཕྱིར་རོ། །

[Block 135]
ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཞེས་ཀྱང་བྱ་སྟེ། འདི་ལྟར་དེ་ལུས་འདི་ལ་གྲུབ་པ་དང་། བདེ་བ་གཅིག་པའི་དོན་གྱིས་ཀུན་ཏུ་སྦྱོར་བ་དང་། རབ་ཏུ་སྦྱོར་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 136]
སེམས་ཞེས་ཀྱང་བྱ་སྟེ། འདི་ལྟར་དེ་ནི་གཟུགས་དང་། སྒྲ་དང་། དྲི་དང་། རོ་དང་། རེག་བྱ་དང་། ཆོས་རྣམས་ཀྱིས་ཀུན་ཏུ་བསགས་པ་དང་། ཉེ་བར་བསགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 137]
བློ་གྲོས་ཡངས་པ་ལེན་པའི་རྣམ་པར་ཤེས་པ་དེ་ལ་བརྟེན་ཅིང་གནས་ནས་རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་པོ་འདི་ལྟ་སྟེ། མིག་གི་རྣམ་པར་ཤེས་པ་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དག་འབྱུང་ངོ་། །དེ་ལ་རྣམ་པར་ཤེས་པ་དང་བཅས་པའི་མིག་དང་གཟུགས་རྣམས་ལ་བརྟེན་ནས་མིག་གི་རྣམ་པར་ཤེས་པ་འབྱུང་སྟེ། མིག་གི་རྣམ་པར་ཤེས་པ་དེ་དང་ལྷན་ཅིག་འཇུག་པ་དུས་དང༌[^83]སྤྱོད་ཡུལ་མཚུངས་པ་རྣམ་པར་རྟོག་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཡང་འབྱུང་ངོ་། །

[Block 138]
གལ་ཏེ་མིག་གི་རྣམ་པར་ཤེས་པ་གཅིག་ལན་ཅིག་འབྱུང་ན་ནི་མིག་གི་རྣམ་པར་ཤེས་པ་དང་། སྤྱོད་ཡུལ་མཚུངས་པ་རྣམ་པར་རྟོག་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཡང་གཅིག་ཁོ་ན་ཙམ༌[^84]ལན་ཅིག་འབྱུང་ངོ་། །གལ་ཏེ་རྣམ་པར་ཤེས་པའི་ཚོགས་གཉིས་སམ། གསུམ་མམ། བཞི་ལྷན་ཅིག་གམ། ལྔ་ཆར་ལྷན་ཅིག་བྱུང༌[^85]ན་ཡང་དེར་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་པོ་དང་སྤྱོད་ཡུལ་མཚུངས་པ་རྣམ་པར་རྟོག་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཡང་གཅིག་ཁོ་ན་ལན་ཅིག་འབྱུང་ངོ་། །དཔེའི་སྒོ་ནས་རྒྱས་པར་བློ་གྲོས་ཡངས་པ་འདི་ལྟ་སྟེ་དཔེར་ན་ཆུའི་ཀླུང་ཆེན་པོ་འབབ་པ་ལས༌[^86]གལ་ཏེ་རླབས་གཅིག་འབྱུང་བའི་རྐྱེན་ཉེ་བར་གནས་པར་གྱུར་ན་རླབས་གཅིག་ཁོ་ན་འབྱུང་ངོ་། །གལ་ཏེ་རླབས་གཉིས་སམ། གལ་ཏེ་རབ་ཏུ་མང་པོ་དག་འབྱུང་བའི་རྐྱེན་ཉེ་བར་གནས་པར་གྱུར་ན་རླབས་མང་པོ་དག་འབྱུང་ཞིང་ཆུའི་ཀླུང་དེ་རང་གི༌[^87]རྒྱུན་འཆད་པར་ཡང་མི་འགྱུར་ལ། ཡོངས་སུ་ཟད་པར་ཡང་མི་འགྱུར་རོ། །

[Block 139]
མེ་ལོང་གི་དཀྱིལ་འཁོར་ཡོངས་སུ་དག་པ་ལ་ཡང༌[^88]གལ་ཏེ་གཟུགས་བརྙན་གཅིག་འབྱུང་བའི་རྐྱེན་ཉེ་བར་གནས་པར་གྱུར་ན་གཟུགས་བརྙན་ཡང་གཅིག་ཁོ་ན་འབྱུང་ངོ་། །གལ་ཏེ་གཟུགས་བརྙན་གཉིས་སམ། གལ་ཏེ་རབ་ཏུ་མང་པོ་དག་འབྱུང་བའི་རྐྱེན་ཉེ་བར་གནས་པར་གྱུར་ན་གཟུགས་བརྙན་རབ་ཏུ་མང་པོ་དག་འབྱུང་ཞིང་། མེ་ལོང་གི་དཀྱིལ་འཁོར་དེ་གཟུགས་བརྙན་གྱི་དངོས་པོར་ཡོངས་སུ་འགྱུར་བ་ཡང་མ་ཡིན་ལ། ཡོངས་སུ་སྦྱོར་བར་ཡང་མི་མངོན་ནོ། །

[Block 140]
བློ་གྲོས་ཡངས་པ་དེ་བཞིན་དུ་ཆུ་ཀླུང་ལྟ་བུ་དང་། མེ་ལོང་ལྟ་བུའི་ལེན་པའི་རྣམ་པར་ཤེས་པ་དེ་ལ་བརྟེན་ཅིང་གནས་ནས་གལ་ཏེ་མིག་གི་རྣམ་པར་ཤེས་པ་གཅིག་ལན་ཅིག་འབྱུང་བའི་རྐྱེན་ཉེ་བར་གནས་པར་གྱུར་ན་ཡང་མིག་གི་རྣམ་པར་ཤེས་པ་ཡང་གཅིག་ཁོ་ན་ལན་ཅིག་འབྱུང་ངོ་། །གལ་ཏེ་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་ཆར་གྱི་བར་དག་ལན་ཅིག་འབྱུང་བའི་རྐྱེན་ཉེ་བར་གནས་པར་གྱུར་ན་ཡང་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་ཆར་ལན་ཅིག་འབྱུང་ངོ་། །བློ་གྲོས་ཡངས་པ་དེ་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་ཆོས་ཀྱི་ལུགས་ཤེས་པ་ལ་བརྟེན་ཅིང་ཆོས་ཀྱི་ལུགས་ཤེས་པ་ལ་གནས་ནས་སེམས་དང་། ཡིད་དང་། རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པ་ཡིན་ལ། དེ་བཞིན་གཤེགས་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དང་། ཡིད་དང་། རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པར་འདོགས་ན་དེ་ཙམ་གྱིས་ཐམས་ཅད་ཀྱི༌[^89]ཐམས་ཅད་དུ་འདོགས་སོ། །

[Block 141]
བློ་གྲོས་ཡངས་པ་གང་གི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ནང་གི་སོ་སོ་རང་གི་ལེན་པ་མི་མཐོང་། ལེན་པའི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་ལ། དེ་ཡང་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡིན་པ་དང་། ཀུན་གཞི་ཡང་མི་མཐོང་། ཀུན་གཞིའི༌[^90]རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་། བསགས་པ་ཡང་མི་མཐོང་། སེམས་ཀྱང་མི་མཐོང་། མིག་ཀྱང་མི་མཐོང་། གཟུགས་ཀྱང་མི་མཐོང་། མིག་གི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་། རྣ་བ༌[^91]ཡང་མི་མཐོང་། སྒྲ་ཡང་མི་མཐོང་། རྣ་བའི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་། སྣ་ཡང་མི་མཐོང་། དྲི་ཡང་མི་མཐོང་། སྣའི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་། ལྕེ་ཡང་མི་མཐོང་། རོ་ཡང་མི་མཐོང་། ལྕེའི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་། ལུས་ཀྱང་མི་མཐོང་། རེག་བྱ་ཡང་མི་མཐོང་། ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་ཞིང་། བློ་གྲོས་ཡངས་པ་གང་གི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ནང་གི་སོ་སོ་རང་གི་ཡིད་ཀྱང་མི་མཐོང་། ཆོས་རྣམས་ཀྱང་མི་མཐོང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཡང་མི་མཐོང་ལ། དེ་ཡང་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡིན་ན། དེ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དོན་དམ་པ་ལ་མཁས་པ་ཞེས་བྱ་སྟེ། དེ་བཞིན་གཤེགས་པ་ཡང་བྱང་ཆུབ་སེམས་དཔའ་དོན་དམ་པ་ལ་མཁས་པ་ནི་སེམས་དང་། ཡིད་དང་། རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པ་ཡིན་པར་འདོགས་སོ། །

[Block 142]
བློ་གྲོས་ཡངས་པ་དེ་ཙམ་གྱིས་སེམས་དང་། ཡིད་དང་། རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པ་ཡིན་ལ། དེ་བཞིན་གཤེགས་པ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དང་། ཡིད་དང་། རྣམ་པར་ཤེས་པའི་གསང་བ་ལ་མཁས་པར་འདོགས་ན་ཡང་དེ་ཙམ་གྱིས་འདོགས་སོ་ཞེས་བྱ་བ་དང་། ཡང་དོན་འདི་ཉིད་ཚིགས་སུ་བཅད་པ། ལེན་པའི་རྣམ་པར་ཤེས་པ་ཟབ་ཅིང་ཕྲ།[^92] །ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏེ་རྟོགས་པར་དཀའ་བའི་ཕྱིར་རོ། །

[Block 143]
ས་བོན་ཐམས་ཅད་ཆུ་བོའི་རྒྱུན་བཞིན་འབབ། །ཅེས་བྱ་བ་ནི་རིམ་གྱིས་འཇུག་པ་ཉིད་ཀྱིས་དེར་ས་བོན་ཐམས་ཅད་ཆུ་བོའི་རྒྱུན་བཞིན་དུ་སྐད་ཅིག་མའི༌[^93]རིམ་གྱིས་འཇུག་པས་སོ། །

[Block 144]
ལེན་པའི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་མིང་གི་རྣམ་གྲངས་དང་། ངེས་པའི་ཚིག་གོ། །

[Block 145]
བདག་ཏུ་རྟོག་པར་གྱུར་ན་མི་རུང་ཞེས་བྱ་བ་ནི་རྣམ་པ་གཅིག་ཏུ་ཞུགས་པ་ཉིད་ལ་བདག་ཏུ་རྟོག་པར་མ་བྱེད་ཅིག་པའོ། །
--- END BLOCKS ---
