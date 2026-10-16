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
[Block 6056]
སྙན་པ་ནི་རྒྱན་ཏེ། དེ་དེ་ལྟར་རྣམ་པ་བཞི་དང་ལྡན་པའི་སྙན་དངགས༌[^3883]བསྟན་པ་ཡིན་ནོ། །

[Block 6057]
གང་ལ༌[^3884]མཉན་པ་དང་། གང་མཉན་པ་དང་། མཉན་པ་དེའི་འབྲས་བུ་དང་བཅས་པ་དེའི་དབང་དུ་བྱས་ནས། ཁྱོད་ཀྱི་ཚིགས་སུ་བཅད་པ་སྙན་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 6058]
གང་ལས་མཉན་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ལས་སོ། །

[Block 6059]
གང་མཉན་པ་ཡིན་ཞེ་ན། ཡོན་ཏན་བཞི་དང་ལྡན་པའི་སྙན་དངགས་སོ།[^3885] །གང་ཉན་པ༌[^3886]ཡིན་ཞེ་ན། སུ་དཱ་སའི་བུའོ། །

[Block 6060]
མཉན་པ་དེའི་འབྲས་བུ་གང་ཡིན་ཞེ་ན། དེ་ཐོས་དགའ་བར་གྱུར་པའོ། །

[Block 6061]
དེའི་འབྲས་བུ་དང་བཅས་པ་ནི་མཆོག་སྦྱིན་པ་སྟེ། མཆོག་སློངས་ཤིག་པའོ། །

[Block 6062]
གང་གི་ཕྱིར་བདག་ལ་དགའ་བར་གྱུར་པ་དེ་ཙམ་གྱིས་མཆོག་སྦྱིན་པར་མི་ནུས་ཏེ། དེ་ཅིའི༌[^3887]ཕྱིར་ཞེ་ན། བདག་ལ་ཡང་རང་དབང་མེད་པར་གྱུར་པའི་ཕྱིར་རོ། །ཇི་ལྟར་རང་དབང་མེད་པ་ཡིན་ཞེ་ན། མི་རིགས་པ་བྱེད་པ་ལས་དགའ་བས་ཕམ་པའི་ཕྱིར་དང་། མི་དགེ་བ་སྤྱོད་པ་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 6063]
སྐྱོན་ནི་ཉེས་པའོ། །

[Block 6064]
དེ་སྐད་རེ་ཞིག་ང་ལ་མ་སྨྲ་ཞིག །ཅེས་བྱ་བ་གང་བསྟན་པ་ནི། སྦྱིན་པར་བྱ་བ་ཉིད་རེ་ཞིག་ཐོང་ཤིག་པ་སྟེ། ང་ནི་བདག་ལའོ། །

[Block 6065]
གང༌[^3888]གི་ཕྱིར་སྐྱོན་དང་བཅས་པའི་ཕྱིར་དང་། བདེན་པ་དང་ལྡན་པའི་བརྟུལ་ཞུགས་ཀྱི་མཆོག་སློང་བ་སྟེ། བདེན་པ་སྔོན་དུ༌[^3889]འགྲོ་བ་ཡིན་ན་ནི། མཆོག་གཞན་ཡང་སྦྱིན་པར་ནུས་པ་ཡིན་ཏེ། མཆོག་གཞན་ཡང་སྦྱིན་པར་ངེས་པར་གཟུང་བའི་ཕྱིར་རོ། །

[Block 6066]
སེམས་ཅན་རྣམས་ལ་གསོད་པར༌[^3890]སྤོངས། །ཞེས་བྱ་བ་ནི་སྲོག་གཅོད་པ་ལས་སླར་ཟློག་པའོ། །

[Block 6067]
བཙོན་དུ་གཟུང་བ༌[^3891]འདི་རྣམས་མ་ལུས་ཐོང་། །ཞེས་བྱ་བ་འདིས་ནི་མ་བྱིན་པར༌[^3892]ལེན་པ་ལས་སླར་ཟློག་པ་སྟེ། གང་གི་ཕྱིར། དེ་དག་མ་བྱིན་པར་ལེན་པ་ནི་ནན་གྱིས་ཁྱེར་བ་སྟེ། དེ་རྣམས་ཐོང་ཤིག་པའོ། །

[Block 6068]
གཞན་ཡང་སྦྱིན་པར་ནུས་པའི་མཆོག་སྦྱིན་པར་བྱ་སྟེ། མཆོག་སྦྱིན༌[^3893]གཞན་གསུམ་པོ་ཡང་ངེས་པར་སྦྱིན་པར་བྱས་པའི་ཕྱིར་རོ། །

[Block 6069]
བཙོན་དུ་གཟུང་བ་འདི་ཐོང་ཤིག་ཅེས་བྱ་བ་ནི་དགག་པ་དེར་ཟད་ཀྱི།[^3894] དམ་པ་སྔ་མ་གསུམ་ནི་ཁྱོད་ལ་འབུལ། །ཞེས་སྔར་སུ་དཱ་སའི་བུས་སྨྲས་པ་དེ་དག་ལས་མཆོག་གསུམ་ཡང་མེད་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་སྨྲས་པ། མི་ཤ་ཟ་བ་མ་བཏང་ན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 6070]
བདེན་པ་སྨྲ་བ་ཇི་ལྟར་མི་འགྱུར་ཞེ་ན། མིའི་ཤ་ཟ་བ་ཡོངས་སུ་མ་བཏང་ན་འདི་ལྟར་ཡང་མཆོག་གསུམ་སྦྱིན་པར་བྱའོ་ཞེས་དམ་བཅས་པ་སྟེ། དེ་ལྟར་མཆོག་སྦྱིན༌[^3895]པ་ཉིད་དུ་ཁས་བླངས་པ་ཇི་ལྟར་བདེན་པ་སྨྲ་བར་འགྱུར་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 6071]
བདེན་པའི་བརྟུལ་ཞུགས་ཞེས་སྨོས་པས་ནི་སྔ་མ་ཉིད་དུ་བསྟན་པས་དེ་བས་ན་ཉེས་པ་མེད་དེ། [^3896]ཡང་ན་དམ་པ་སྔ་མ་གསུམ་ནི་ཁྱོད་ལ་སྦྱིན་ཞེས་བྱ་བ་ཡིན་ཏེ། མཆོག་གསུམ་ཉིད་ཀྱི་དོན་ཡིན་གྱི། འདིའི་དོན་ནི་མ་ཡིན་ཏེ། དེ་ལྟར་ཉེས་པ་མེད་དོ་ཞེ་ན། དེའི་ཚིག་གིས་ཇི་ལྟར་སྲོག་གཅོད་པ་སྤོང་བར་འགྱུར་ཏེ། སྲོག་གཅོད་པ་མ་ཡིན་པར་ནི་མིའི་ཤ་མེད་པའི་ཕྱིར་རོ། །

[Block 6072]
བདག་གི་སྲོག་ཀྱང་ཡོངས༌[^3897]སྤངས་ནས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ཀྱང་གང་སྔར་ལྟར༌[^3898]བསྟན་པའི་མཆོག་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་དེའི་ཚིག་ལོག་པ་ཉིད་དུ་སྒྲུབ་པ་ཡིན་ཏེ། བདེན་པའི་བརྟུལ་ཞུགས་སུ་ཇི་ལྟར་འགྱུར་ཞེས་བྱ་བ་དེའི་རྗེས་སུ་བསྟན་པ་སྟེ། གལ་ཏེ་དེ་ལྟར་སྔར་གྱི་ཉེས་པ་དེ་ཡོངས་སུ་སྤོང་བར་ཇི་ལྟར་འགྱུར་ཞེས་པའོ། །

[Block 6073 [VERSE]]
རྒྱལ་པོ་ཁྱེད་ཀྱིས་སྲོག་ཆགས་རྣམས། །
མི་གསོད་པར༌[^3899]ཡང་ག་ལ་ནུས། །

[Block 6074]
ཞེས་བྱ་བ་དེའི་རྗེས་སུ་བསྟན་པ་ནི༌[^3900]འདི་ཡིན་ཏེ། ཤ་ཡི་ཕྱིར་ནི་མི་བསད་ན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་དོ། །

[Block 6075]
དེ་ལྟར་གྱུར་ན་ཞེས་བྱ་བ་ནི་བརྫུན་སྨྲ་བ་ལས་ལྡོག་པ་དང་། སྲོག་གཅོད་པ་ལས་ལྡོག་པ་སྟེ། དེ་བས་ན་དེ་གཉིས་ཀྱང་མ་བྱིན་པར་ཇི་ལྟར་མཆོག་གསུམ་པོ་དེ་དག་བྱིན་པ་ཡིན། མཆོག་གཅིག་པོ་སྐྱེ་བོ་བཙོན་དུ་བཟུང་བ་བཏང་བ་དེ་ཉིད་བྱིན་པ་ཡིན་ཏེ། མཆོག་གཞན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 6076]
རྒྱལ་སྲིད་ཉམས་ཞེས་བྱ་བ་འདིས༌[^3901]ནི་དོན་ལས་ཉམས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6077]
ནགས་ཚལ་ཞེས་བྱ་བ་འདིས་ནི་འདོད་པ་ཡོངས་སུ་ཉམས་པ་བསྟན་ཏོ། །

[Block 6078]
ཆོས་ལས་ཉམས་ཞེས་བྱ་བ་འདིས་ནི་ཆོས༌[^3902]ཡོངས་སུ་སྤངས་པའོ། །

[Block 6079]
མི་བསད་པ་དང་། བཟའ་བ་མ་ཟོས་པའི་ཕྱིར་གཏམ་ངན་ཐོབ་པའོ། །

[Block 6080]
དེ་ཉིད་ཀྱིས་ཆོས་ཉམས་པ་ཡིན་ཏེ། འདིས་ནི་འཇིག་རྟེན་ཕ་རོལ་ལ་གནོད་པ་ཐོབ་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 6081]
གཏམ་ངན་ཐོབ་ཅེས་བྱ་བ་འདིས་ནི་མཐོང་བའི་ཆོས་ཀྱི་གནོད་པ་ཐོབ་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6082]
གང་གི་ཕྱིར་ནི་རྒྱལ་སྲིད་ཉམས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སུ་དཱ་སའི་བུས་སྨྲས་པ། དེའི་རྗེས་སུ་བསྟན་པ་ནི༌[^3903]ཚིགས་བཅད་འདི་ཡིན༌[^3904]ཏེ། ཆོས་ལས་ཉམས་པར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་ཆོས་ལས་ཉམས་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་ཏོ། །

[Block 6083]
སྲིད་ལས་ཉམས་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་རྒྱལ་སྲིད་ལས་ཉམས་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་ཏོ། །

[Block 6084]
བདེ་བ༌[^3905]ལས་ཉམས་པར་འགྱུར་བ༌[^3906]ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི། ནགས་ཚལ་སྡུག་བསྔལ་བདག་གིས་མྱོང་། །ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་ཏོ། །

[Block 6085]
གྲགས་པ་ཉམས་པར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་གཏམ་ངན་པ་ཐོབ་པ་ཞེས་བྱ་བ་དེ་བསྟན་ཏོ། །

[Block 6086]
ཕུང་བར་གྱུར་པའི༌[^3907]འབྱུང་གནས་དེ། །ཞེས་བྱ་བའི་རྒྱུ་བཞི་པོ་དེ་དག་ཉིད༌[^3908]ཕུང་བའི་འབྱུང་གནས་སོ། །

[Block 6087]
བྱིན་ནས་འགྱོད་པ་སྐྱེ་བ་ཞེས་བྱ་བ་ནི། འགྱོད་པ་ཡོད་ན་ནི་འགྱོད་པ་སྐྱེ་བའོ། །

[Block 6088]
གལ་ཏེ་ཤ་མེད་ན་འཚོ་བར་མི་ནུས་ན་ནི་ཤའི་ཚུལ་བསྟན་པའི་ཕྱིར། སྨན་པ༌[^3909]མཁས་པས་བརྟགས་ཏེ་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 6089]
སྨན་པས་བརྟགས༌[^3910]པ་ནི་ཕན་པའོ། །

[Block 6090]
ལེགས་པར་སྦྱར་བའི་ཤ་ཞེས་བྱ་བ་ནི་སྨན་པས་ལེགས་པར་བརྟགས་པ༌[^3911]སྟེ། འདིས་ནི་གཡོས་ཀྱི་ཁྱད་པར་བསྟན་ཏོ། །

[Block 6091]
གནས་རྣམས༌[^3912]བཞི་ལས་སྐྱེས་པའི་ཤ་བསྟན་པ་ཡིན་ཏེ། དུས་ཇི་ལྟ་བ་དང་། ནད་གཞི༌[^3913]ཇི་ལྟ་བ་བཞིན་དུ་སྨན་པས༌[^3914]ན་བ་ཉིད་དུ་སྦྱར་རོ། །

[Block 6092]
དེ་ལྟར་རེ་ཞིག་ཡིད་དུ་འོང་ཞིང་འདོད་པའི་ཤ་རྙེད་ཅིང་འགྲུབ་པ་ཉིད་དུ་བསྟན་ནས། གཞན་ཡང་བདེ་བ་ཐོབ་པ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར། རྔ་སྒྲ་སྙན་པ་དབྱར་གྱི་འབྲུག་སྒྲ་བཞིན་དུ་སྒྲོགས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 6093]
རྔ་སྒྲ་སྙན་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་དང་པོས་ནི། སྦྱིན་པའི་འབྲས་བུ་ལོངས་སྤྱོད་ཆེན་པོའི་ཕན་ཡོན་ཡོངས་སུ་བཏང་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6094]
གཉེན་དང་། བུ་དང་། ནང་མི་ཞེས་བྱེ་བ་ཕྱེད་འོག་མས་ནི། བཟོད་པའི་འབྲས་བུ་གཡོག་འཁོར་མང་པོས་ཕན་ཡོན་ཡོངས་སུ་བཏང་བ་བསྟན་ཏོ། །

[Block 6095]
དགག་པར་བྱ་བ་དང་། དགག་པ་ལ་སྦྱར་ཞིང་དབང་བྱ་བ་དེ་གཉིས་ཀྱི་རྒྱུའི་དབང་དུ་བྱས་ནས། རྒྱལ་པོའི་སེམས་ཀྱི་དབང་དུ་བྱས་པ་སྟེ། རྒྱལ་པོའི་སེམས་ཀྱི་དབང་དུ་འགྲོ་བ་ནི་མི་རིགས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། ཕྱི་རོལ་གྱི་སྟོབས་དང་ལྡན་པ་ལས་ཀྱང་རྒྱལ་བར་ནུས་པ་ཡིན་པའི་ཕྱིར། ནང་གི་བདེ་བ་ནི་ཚར་བཅད་ཅིང་རྒྱལ་བར་བྱ་བ་དེ་ལ་སྡང་བར་བྱ་བ༌[^3915]མི་རིགས་སོ། །
--- END BLOCKS ---
