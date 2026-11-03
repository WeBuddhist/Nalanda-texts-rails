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

[Block 146]
ཞེས་གསུངས་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་སྐྱབས་སུ་འགྲོ་བ་རྣམས་ནི་སྡོམ་པ་ཡང་དག་པར་བླངས་པ་ཐམས་ཅད་ལ་སྒོར་གྱུར་པ་ཡིན་ནོ། །

[Block 147 [HEADING]]
### འདོད་པས་ལོག་པར་གཡེམ་པ་སྤོང་བ། ^1-13-0

[Block 148]
ཡང་ཅིའི་ཕྱིར་སྡོམ་པ་གཞན་དག་ལས་ནི་མི་ཚངས་པར་སྤྱོད་པ་སྤོང་བ་བསླབ་པའི་གཞིར་རྣམ་པར་བཞག་ལ། དགེ་བསྙེན་ལ་ནི་འདོད་པས༌[^91]ལོག་པར་གཡེམ་པ་ལས༌[^92]སྤོང་བ་བསླབ་པའི་གཞིར་རྣམ་པར་གཞག་ཅེ་ན།

[Block 149 [VERSE]]
ལོག་གཡེམ་ཤིན་ཏུ་སྨད་ཕྱིར་དང་། །
སླ་ཕྱིར་མི་བྱེད་ཐོབ་ཕྱིར་རོ། །

[Block 150]
འདོད་པས་ལོག་པར་གཡེམ་པ་ནི་གཞན་དག་གི་ཆུང་མ་སུན་འབྱིན་པའི་ཕྱིར་དང་། ངན་སོང་བའི་རྒྱུ་ཡིན་པའི་ཕྱིར་འཇིག་རྟེན་ན་ཤིན་ཏུ་སྨད་པ་ཡིན་གྱི་མི་ཚངས་པར་སྤྱོད་པ་ནི་དེ་ལྟ་མ་ཡིན་པ་དང་། ཁྱིམ་ན་གནས་པ༌[^93]འདོད་པས༌[^94]ལོག་པར་གཡེམ་པ་ལས་བསྡམས༌[^95]བླའི་མི་ཚངས་པར་སྤྱོད་པ་ལས་ནི་དཀའ་བའི་ཕྱིར། དཀའ་བ༌[^96]བྱེད་པར་མི་སྤྲོ་བར་འགྱུར་བ་དང་། འཕགས་པ་རྣམས་ཚེ་རབས་གཞན་དག་ཏུ་ཡང་མི་སྤྱོད་པའི་ཕྱིར་འདོད་པས་ལོག་པར་གཡེམ་པ་མི་བྱེད་པའི་སྡོམ་པ་ཐོབ་ཀྱི་མི་ཚངས་པར་སྤྱོད་པ་ནི་དེ་ལྟ༌[^97]མ་ཡིན་པས་སློབ་པ་ཚེ་རབས་གཞན་དུ་གྱུར་པ་དགེ་བསྙེན་གྱི་སྡོམ་པ་ལ་གནས་པ་མ་ཡིན་པར་འགྱུར་དུ་འོང་བས་དགེ་བསྙེན་ལ་ཡང་དེ་ཁོ་ན་ལས་ལྡོག་པ་སྡོམ་པར༌[^98]རྣམ་པར་གཞག་གོ། །

[Block 151]
མི་བྱེད་པར་ངེས་པ་ནི་མི་བྱེད་པའི་སྡོམ་པའོ། །

[Block 152]
གང་དག་དགེ་བསྙེན་ཡིན་བཞིན་དུ་ཆུང་མ་ལེན་པར་བྱེད་ན་ཅི་དེ་དག་གིས་དེ་ལས་ཀྱང་སྡོམ་པ་ཐོབ་བམ། འོན་ཏེ་མ་ཡིན་ཞེ་ན། ཉི་ཚེ་བའི་སྡོམ་པ་ཐོབ་པར་འགྱུར་དུ་འོང་བས་འཐོབ་བོ། །ཇི་ལྟར་ན་སྡོམ་པ་ཉམས་པར་མི་འགྱུར་ཞེ་ན། འདི་ལྟར།

[Block 153 [VERSE]]
སྡོམ་པ་ཇི་ལྟར་ཁས་བླངས༌[^99]བཞིན། །
འཐོབ་ཀྱི་རྒྱུད་ལས་མ་ཡིན་ནོ། །

[Block 154]
དེ་དག་གི་སྡོམ་པ་ནི་ཇི་ལྟར་ཁས་ལེན་པ་དེ་བཞིན་འཐོབ་བོ། །

[Block 155]
དེ་དག་ཇི་ལྟར་ཁས་ལེན་ཞེ་ན་བདག་འདོད་པས་ལོག་པར་གཡེམ་པ་སྤོང་ངོ་ཞེས་ཁས་ལེན་གྱི། བདག་གི་རྒྱུད་འདི་ལ་མི་ཚངས་པར་སྤྱོད་པར་མི་བྱའོ་ཞེས་ནི༌[^100]མ་ཡིན་ཏེ། དེའི་ཕྱིར་དེ་དག་གིས་གཞི་དེ་ལས་འདོད་པས་ལོག་པར་གཡེམ་པའི་ཡན་ལག་ཁོ་ན་སྡོམ་པ་འཐོབ་ཀྱི་མི་ཚངས་པར་སྤྱོད་པ་ནི་མ་ཡིན་པས་ཆུང་མར་གྱུར་པ་ལ་སྡོམ་པ་ཉམས་པ༌[^101]མེད་དོ། །

[Block 156 [HEADING]]
### བརྫུན་དུ་སྨྲ་བ་སྤོང་བ། ^1-14-0

[Block 157]
ཡང་ཅིའི་ཕྱིར་བརྫུན་དུ་སྨྲ་བ་སྤོང་བ་ཁོ་ན་དགེ་བསྙེན་གྱི་སྡོམ་པ་ལ་བསླབ་པའི་ཡན་ལག་ཏུ་བཞག་ལ་ཕྲ་མ༌[^102]ལ་སོགས་པ་ལས་ནི་མ་ཡིན་ཞེ་ན། རྒྱུ་གསུམ་པོ་དེ་དག་ཉིད་ཀྱི་ཕྱིར་ཏེ།

[Block 158 [VERSE]]
བརྫུན་སྨྲ་ཤིན་ཏུ་སྨད་ཕྱིར་དང་། །
སླ་ཕྱིར་མི་བྱེད་འཐོབ་ཕྱིར་རོ། །
བསླབ་པ་ཐམས་ཅད་འདས་གྱུར་ན། །
བརྫུན་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར། །

[Block 159]
བསླབ་པ་ཐམས་ཅད་དུ་འདས་ན་དྲི་བར་བྱ་བ་ལ་བདག་གིས་དེ་ལྟ་བུ་མ་བྱས་སོ་ཞེས་བྱ་བ་འདི་ཉེ་བར་གནས་པར་འགྱུར་ཏེ། བརྫུན་དུ་སྨྲ་བར་ཐལ་བར་འགྱུར་བས་དེའི་ཕྱིར་ཇི་ལྟར་ན་འདས་པར་བྱས་ཀྱང་བདག་ཉིད་འཆགས་པར་འགྱུར་སྙམ་ནས་བརྫུན་དུ་སྨྲ་བ་ལས་ཟློག་པ༌[^103]བཤད་དོ། །

[Block 160 [HEADING]]
### བཅས་པའི་ཁ་ན་མ་ཐོ་བ་མྱོས་འགྱུར། ^1-15-0

[Block 161]
ཡང་ཅིའི་ཕྱིར་བཅས་པའི༌[^104]ཁ་ན་མ་ཐོ་བ་ལས༌[^105]འདིར་བསླབ་པའི་གཞིར་རྣམ་པར་མ་བཞག་ཅེ་ན།

[Block 162]
བཅས་པའི༌[^106]ཁ་ན་མ་ཐོ་བ། །མྱོས་འགྱུར་ལས།

[Block 163]
རྣམ་པར་གཞག་གོ། །

[Block 164]
ཅིའི་ཕྱིར་མྱོས་པར་འགྱུར་བ་ཁོ་ན་ལས་ཡིན་གྱི་གཞན་ལས་ནི༌[^107]མ་ཡིན་ཞེ་ན་གཞན་སྲུང་ཕྱིར་རོ། །

[Block 165]
མྱོས་པར་འགྱུར་བ་འཐུངས་ན་ཡན་ལག་གཞན་དང་གཞན་དག་ཀྱང་མི་སྲུང་བར་འགྱུར་རོ། །

[Block 166]
ཇི་ལྟར་ན་མྱོས་པར་འགྱུར་བ་འཐུང་བ་བཅས་པའི༌[^108]ཁ་ན་མ་ཐོ་བ་ཡིན་པར་ཤེས་ཤེ་ན། རང་བཞིན་གྱིས༌[^109]ཁ་ན་མ་ཐོ་བའི་མཚན་ཉིད་མེད་པའི་ཕྱིར་ཏེ། རང་བཞིན་གྱིས༌[^110]ཁ་ན་མ་ཐོ་བ་ནི་སེམས་ཉོན་མོངས་པ་ཅན་ཁོ་ནས་སྤྱོད་པ་ཡིན་ན་ཆང་ནི་ཇི་སྲིད་མྱོས་པར་མི་འགྱུར་བར་གཉེན་པོའི་བློ་ཁོ་ནས་བཏུང་བར་ནུས་སོ། །

[Block 167]
གང་མྱོས་པར་འགྱུར་བ་ཡིན་པར་ཤེས་ནས་འཐུང་བའི་སེམས་དེ་ཉིད་ཉོན་མོངས་པ་ཅན་ཡིན་ནོ། །

[Block 168]
གང་མྱོས་པར་མི་འགྱུར་བའི་དྲོད་རིག་ནས་འཐུང་བ་དེ་ནི་ཉོན་མོངས་པ་ཅན་མ་ཡིན་ནོ། །

[Block 169]
འདུལ་བ་འཛིན་པ་རྣམས་ན་རེ་མྱོས་པར་འགྱུར་བ་འཐུང་བ་ནི་རང་བཞིན་གྱིས༌[^111]ཁ་ན་མ་ཐོ་བ་ཡིན་ཏེ། བཙུན་པ་ཇི་ལྟར་བྲོ་གཡོག་བགྱི། །ཉེ་བ༌[^112]འཁོར་རང་བཞིན་གྱིས༌[^113]ཁ་ན་མ་ཐོ་བ་མ་གཏོགས་པ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་ལ། ཤཱཀྱ་ནད་པ་རྣམས་ལ་ཡང་མྱོས་པར་འགྱུར་བ་འཐུང་བ་མ་གནང་ངོ་། །འདི་སྐད་དུ་དགེ་སློང་དག་ང་སྟོན་པ་ཡིན་པར་སྨྲ་བ་རྣམས་ཀྱིས་མྱོས་པར་འགྱུར་བ་རྩྭའི་རྩེ་མོས་ཀྱང་བཏུང་བར་མི་བྱའོ་ཞེས་ཀྱང་གསུངས་ཏེ། དེའི་ཕྱིར་རང་བཞིན་གྱིས༌[^114]ཁ་ན་མ་ཐོ་བ་ཡིན་པར་མངོན་ནོ། །

[Block 170]
སྲོག་གཅོད་པ་ལ་སོགས་པ་བཞིན་དུ་འཕགས་པ་རྣམས་ཚེ་འཕོས་ཀྱང་མི་སྤྱོད་པའི་ཕྱིར་དང་། ལུས་ཀྱི་ཉེས་པར་སྤྱོད་པ་ཞེས་ཀྱང་འབྱུང་བའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 171]
ཆོས་མངོན་པ་བ་རྣམས་ན་རེ། མ་ཡིན་ཏེ། ནད་པ་རྣམས་ལ་བཅས་པའི༌[^115]ཁ་ན་མ་ཐོ་བ་སྤྱིར་བསྟན་མོད་ཀྱི། ཡང་མྱོས་པར་འགྱུར་བའི་དྲོད་མ་ངེས་པར་ཐལ་བར་འགྱུར་བ་ཡོངས་སུ་སྤང་བའི་ཕྱིར་མྱོས་པར་འགྱུར་བ་དམིགས་ཀྱིས་བསྟན་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་རྩྭའི་རྩེ་མོས་འཐུང་བ་བཀག་པ་ཡིན་ནོ། །

[Block 172]
འཕགས་པ་རྣམས་མི་སྤྱོད་པ་ནི་ངོ་ཚ་དང་ལྡན་པའི་ཕྱིར་དང་། དེས་ཀྱང་དྲན་པ་ཉམས་པར་བྱེད་པའི་ཕྱིར་ཅུང་ཟད་ཀྱང༌[^116]མི་གསོལ་ཏེ། དུག་བཞིན་དུ་མ་ངེས་པའི་ཕྱིར་རོ། །

[Block 173]
ཉེས་པར་སྤྱོད་པ་ཞེས་འབྱུང་བ་ནི་བག་མེད་པའི་གནས་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་འདི་ལ་བག་མེད་པའི་གནས་ཞེས་སྨོས་ཀྱི་གཞན་དག་ལ་ནི་མ་ཡིན་ཏེ། དེ་དག་ལ༌[^117]ནི་རང་བཞིན་གྱིས༌[^118]ཁ་ན་མ་ཐོ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 174]
ཧ་ཅང་ཀུན་དུ་བསྟེན་པས༌[^119]ངན་འགྲོར་འགྲོ་བར་གསུངས་པ་ནི་དེའི་ཞར་ལ་མི་དགེ་བའི་རྒྱུན་ཡང་དང་ཡང་དུ་འཇུག་པས་ངན་སོང་བའི་ལས་འཕེན་པ་འམ་འཇུག་པ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 175]
འབྲུའི་ཆང་དང་སྦྱར་བའི་ཆང་མྱོས་པར་འགྱུར་བ་བག་མེད་པའི་གནས་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། འབྲུའི་ཆང་ནི་ཟས་ལས་སྦྱར་བའི་བཏུང་བའོ། །

[Block 176]
སྦྱར་བའི་ཆང་ནི་རྫས་ལས་སྦྱར་བའི་བཏུང་བའོ། །

[Block 177]
དེ་དག་ཀྱང་རེས་འགའ་མྱོས་པར་འགྱུར་བའི་དངོས་པོར་མ་རེད་པའམ་ཡལ་བར་འགྱུར་བས་དེའི་ཕྱིར་མྱོས་པར་འགྱུར་བ་ཞེས་བྱ་བར་སྨོས་སོ། །

[Block 178]
གླ༌[^120]གོར་ཞོ་ཤ་དང་ཁྲེ་རྒོད༌[^121]ལ་སོགས་པ་ཡང་མྱོས་པར་བྱེད་པས་འབྲུའི་ཆང་དང་སྦྱར་བའི་ཆང་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 179]
བཅས་པའི༌[^122]ཁ་ན་མ་ཐོ་བ་ཡིན་ཡང་བག་མེད་པ་ཐམས་ཅད་ཀྱི་གནས་སུ་གྱུར་པས་བསྒྲིམས༌[^123]ཏེ་སྤང་བར་བྱ་བ་ཉིད་ཡིན་པའི་རྒྱུ་ཤེས་པར་བྱ་བའི་ཕྱིར་བག་མེད་པའི་གནས་ཞེས་སྨོས་སོ། །

[Block 180 [HEADING]]
### སྡོམ་པ་གང་ལས་འཐོབ་པ། ^1-16-0
--- END BLOCKS ---
