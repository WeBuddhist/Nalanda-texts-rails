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
[Block 141]
བར་མ་ནི་བསྒྲུབ༌[^80]པའིའོ། །

[Block 142]
མཁས་པ་དང་འབྲས་བུ་ནི་ཐ་མའིའོ། །

[Block 143]
བདེ་འགྲོར་སྐྱེས་པ་ལས་གྱུར་པ་ནི་ཁྱད་པར་གྱི་དབང་དུ་བྱས་པའི་རྟགས་སོ། །

[Block 144]
ངན་འགྲོར་སྐྱེས་པ་ལས་གྱུར་པའི་ཁྱད་པར་གྱི་དབང་དུ་བྱས་པ་ནི། འདི་ལ་བྱང་ཆུབ་སེམས་དཔའ་ནི་ཡུན་རིང་པོ༌[^81]ཞིག་ན་ཞེས་བྱ་བ་ལ་སོགས་པའི་གཞུང་ཡིན་ནོ། །

[Block 145]
དཀར་པོའི་ཆོས་དང་མི་མཐུན་པ་དང་མི་ཐོབ་པའི་རྒྱུ་ལ་རྒོལ་བ་དང་། ལན་གདབ་པ་ལས་བརྩམས་ནས། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་རང་བཞིན་གྱིས་ཡོན་ཏན་དང་ལྡན་ཞིང་དཀར་པོའི་ཆོས་དང་ལྡན་ན་གང་གིས་ན་དུས་རྟག་ཏུ་དཀར་པོའི་ཆོས་དང་མི་ལྡན་ཞེ་ན། དེ་ལྟ་བུའི་རྒོལ་བའི་ལན་གདབ་པར་གསུངས་པ། ཇི་སྲིད་དཀར་པོའི་ཕྱོགས་ཀྱི་ཆོས་དང་མི་མཐུན་པ་ཉེ་བའི་ཉོན་མོངས་པ་བཞི་ལས་མ་ལུས་པའམ་འགས་ཀྱང་ཉོན་མོངས་པར་མ་གྱུར་ན་སྐྱེད་པར་དཀའ་བ་གཙོ་བོར་གྱུར་པ་བསམ་གྱིས་མི་ཁྱབ་པ་མི་གཡོ་བ་བླ་ན་མེད་པ་དེ་བཞིན་གཤེགས་པའི་གོ་འཕང་ཐོབ་པ་ཉིད་དེ། རྒྱུའི་ངོ་བོ་དང་ལྡན་པ་ནི༌[^82]ཡིན་གྱི། གཞན་དང་ལྡན་ན་ནི༌[^83]མ་ཡིན་པས་སོ། །

[Block 146]
གལ་ཏེ་དེ་ཡོད་པ་ཉིད་ཡིན་ན་གང་གིས་བླ་ན་མེད་པའི་གོ་འཕང་འཐོབ་པར༌[^84]མི་འགྱུར་ཞེ་ན། རྒོལ་བ་འདིའི་ལན་གདབ་པའི་དོན་ནི། རྒྱུ་བཞིས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་མི་ནུས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 147]
བྱང་ཆུབ་སེམས་དཔའི་སའི་གཞིའི་རྣལ་འབྱོར་གྱི་གནས་ལས།

[Block 148]
དང་པོའི་རིམ་པར་ཕྱེ་བའོ།། །།

[Block 149]
དེ་ལས་གཞན་པའི་ཡང་དག་པའི་སྨོན་ལམ་རྣམས་བསྡུས་པ༌[^85]ཡིན་ཞེས་བྱ་བ་ནི་སེམས་བསྐྱེད་པ་དེ་ལས་གཞན་པའི་ཡང་དག་པའི་སྨོན་ལམ་བསྡུས་པའི་ཕྱིར་རྟེན་ཉིད་དུ་བསྟན་ཏོ། །

[Block 150]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་ཡང་བྱེད་ཅིང་ཞེས་བྱ་བ་ནི། ཡོངས་སུ་མྱ་ངན་ལས་འདས་པའི༌[^86]རིགས་ཅན་རྣམས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 151]
སེམས་ཅན་ཐམས་ཅད་ཤིན་ཏུ་མཐར་ཐུག་པའི་མྱ་ངན་ལས་འདས་པ་ལ་འགོད་པ་ཞེས་བྱ་བ་ནི། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་རིགས་ཅན་གྱི་དབང་དུ་བྱས་པའོ། །

[Block 152]
དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ཞེས་བྱ་བ་ནི། སངས་རྒྱས་ཀྱི་རིགས་ཅན་གྱི་དབང་དུ་བྱས་པའོ། །

[Block 153]
སེམས་བསྐྱེད་པ་དེ་ནི་དགེ་བ་སྟེ། ཅི་ལྟར་བྱས་ནས་ཤེ་ན། བྱང་ཆུབ་ཀྱི་ཕྱོགས་རྣམས་ཀྱི་དགེ་བའི་རྩ་བ་ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ནི་ཤེས་རབ་ལ་སོགས་པའི་ངོ་བོ་ཉིད་ཡིན་ལ། དེ་རྣམས་སྡུད་པའི་ཕྱིར་དགེ་བའོ། །ཇི་ལྟར་སྡུད་ཅེ་ན། སྨྲས་པ། དེ་རྣམས་ཀྱི་ཐོག་མར་འགྲོ་བའི་དོན་གྱི་ཕྱིར་རོ། །

[Block 154]
མཆོག་ཏུ་ལེགས་པའི་ཡོན་ཏན་དང་ལྡན་པའི་ཕྱིར་དགེ་བའམ། ཤེས་རབ་དང་སྙིང་རྗེའི་དགེ་བའི་རྩ་བ་དང་ལྡན་པས་ཀྱང་སྙིང་རྗེ་ནི་ཞེ་སྡང་མེད་པའི་མཚན་ཉིད་ཅན་ནོ། །

[Block 155]
དེ་བཞིན་དུ་རྒྱུ་གཉིས་དག་གིས་དགེ་བ་ཁོ་ན་སྟེ། དགེ་བའི་རྩ་བ་ཡོན་ཏན་དུ་བྱེད་པ་ཉིད་དང་། དགེ་བའི་རྩ་བ་ཡང་དག་པར་སྦྱོར་བའོ། །

[Block 156]
གཞན་ཡང་སེམས་ཅན་ཐམས་ཅད་ལ་བརྟེན་པའི་ལུས་དང་ངག་དང་ཡིད་ཀྱི་ཉེས་པར་སྤྱོད་པ་དང་མི་མཐུན་པའི་ཕྱིར་དང་། མི་དགེ་བའི་རྩ་བ་ཡང་དག་པར་སྦྱོར་བའི༌[^87]ཀུན་ནས་སློང་བ་སྲོག་གཅོད་པ་ལ་སོགས་པ་ཉེས་པར༌[^88]སྤྱོད་པ་དང་མི་མཐུན་པའི་ཕྱིར༌[^89]ཡང་དགེ་བའོ། །

[Block 157]
ཡང་ན་མཆོག་ཏུ་དགེ་བའི་ཡོན་ཏན་ཉིད་ཀྱིས་དགེ་བ་སྟེ། བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་དགེ་བའི་རྩ་བའོ། །

[Block 158]
འདི་ལྟར་ཡང་དག་པར་སྡུད་པ་དེ་དག་ཀྱང་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་རྣམས་ཀྱི་ཐོག་མར་འགྲོ་བའི་ཕྱིར་དགེ་བའོ། །

[Block 159]
བཟང་བ་ནི་གཞན་ལ་ཕན་པའི་ཕྱིར་ཞུགས་པ་ཉིད་དོ། །

[Block 160]
མི་འགྱུར་བ་ཉིད་ཀྱིས་ན་ལེགས་པའོ། །

[Block 161]
འདི་ལྟར་བསྟན་པར་འགྱུར་ཏེ། ལྔ་པོ་འདི་དག་གི་ངོ་བོ་ནི་གང་། སེམས་བསྐྱེད་པའི་མཚན་ཉིད་ནི་གང་། རྣམ་པ་ནི་གང་། དམིགས་པ་ནི་གང་དང་ཡང་དག་པར་ལྡན། ཁྱད་པར་གང་གིས་ཁྱད་པར་དུ་འཕགས་པའི་ཆོས་དང་མཚུངས་པར་ལྡན༌[^90]པར་འབྱུང་ཞེས་བྱ་བ་ནི་རིགས་དང་འཇུག་པ་དང་ངེས་པར་འབྱུང་བ་ཞེས་བྱ་བའི་ས་རྣམ་པ་གསུམ་སྟེ། དེས་ན་སའི་རིགས་གསུམ་གྱིས་བསྡུས་པ་ཉིད་དེ། དེ་ལ༌[^91]འཇུག་པས་བསྡུས་པ་བསྟན་པ་ནི། སེམས་བསྐྱེད་པ་དེ་ནི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཀྱི་རྩ་བ་ཞེས་བྱ་བ༌[^92]སྟེ། རྒྱུ་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་གི་འབྲས་བུ་ཡིན་ཞེ་ན། སྨྲས་པ། སྙིང་རྗེའི་རྒྱུ་མཐུན་པ་ཞེས་བྱ་བའོ། །

[Block 162]
ཆོ་འཕྲུལ་བསམ་གྱིས་མི་ཁྱབ་པ་ནི། ཆོ་འཕྲུལ་རྣམ་པ་གསུམ་སྟེ། རྫུ་འཕྲུལ་དང་། ཀུན་བརྗོད་པ༌[^93]དང་། རྗེས་སུ་བསྟན་པའི་ཆོ་འཕྲུལ་ལོ། །

[Block 163]
གཞན་མངོན་པར་ཤེས་པ་ལ་སོགས་པ་མདོ་ལས་ཇི་ལྟར་འབྱུང་བའི་གྲོང་ཁྱེར་དུ་འཇུག་པ་ན་ལོང་བ་རྣམས་ཀྱིས་མིག་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་མཐུའོ། །

[Block 164]
མཐུ་དེ་གང་ལས་ཐོས་པ་དང་མཐོང་བ་སྟེ། ཡིད་ཆེས་པ་དང་། མངོན་སུམ་གྱི༌[^94]ཚད་མས་ཉེ་བར་དམིགས་པ་དང་། མི་སླུ་བའི་ལུང་གིས་བསྟན་པའོ། །

[Block 165]
གང་ལ་གནས་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའོ། །

[Block 166]
ཞུགས་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི། བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 167]
བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ལས་བརྩམས་ཏེ་ཞེས་བྱ་བ་ནི། ཉན་ཐོས་ཀྱི་ཐེག་པའི་དམ་པའི་ཆོས་ལ་ཡང་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ལས་བརྩམས་ནས་ཉན་པའོ། །

[Block 168]
བྱང་ཆུབ་སེམས་དཔའི་སྡེ་སྣོད་ཅེས་བྱ་བ་ནི། ཤིན་ཏུ་རྒྱས་པའོ། །

[Block 169]
ཉེ་བའི་ཉོན་མོངས་པ་བཅུའི་བསྡུས་པའི་དོན་ནི། འཇུག་པའི་བར་དུ་གཅོད་པ་དང་། འཇུག་པའི་ཤིན་ཏུ་བར་དུ་གཅོད་པ་དང་། སྒྲུབ་པའི་བར་དུ་གཅོད་པའོ། །

[Block 170]
དེ་ལ་འཇུག་པའི་རྒྱུ་ནི་གསུམ་སྟེ། ཤེས་རབ་ལྷག་པ་དང་། ཁ་ན་མ་ཐོ་བས་འཛེམ་པ་དང་། བདག་ལ་ལྟོས་ནས་སེམས་ཅན་ལ་སྙིང་རྗེ་བའོ། །

[Block 171]
གསུམ་པོ་འདིའི་མི་མཐུན་པའི་ཕྱོགས་སུ་གྱུར་པ་གསུམ་ནི་ཉེ་བའི་ཉོན་མོངས་པ་སྟེ། གཏི་མུག་ཤས་ཆེ་བ་དང་། ངོ་ཚ་མེད་ཅིང་ཁྲེལ་མེད་པ་ཤས་ཆེ་བ་དང་། ཕྲག་དོག་དང་སེར་སྣ་ཤས་ཆེ་བ་སྟེ། དེ་དག་ནི་འཇུག་པར་དཀའ་བ་ཉིད་དོ། །

[Block 172]
སྒྲིབ་པ་གསུམ་གྱིས་བསྒྲིབས་པས་གཉིས་ཀར༌[^95]ཡང་སྒྲིབ་པ་ཉིད་དེ། སྡུག་བསྔལ་གྱིས་བསྡུས་པ་ནི་རྣམ་པར་སྨིན་པའི་སྒྲིབ་པར་བསྡུས་སོ། །

[Block 173]
གནས་ངན་ལེན་དང་ཉོན་མོངས་པ་ཤས་ཆེ་བ་ནི། ཉོན་མོངས་པའི་སྒྲིབ་པའོ། །

[Block 174]
ཉེས་པར་སྤྱོད་པ་ཤས་ཆེ་བ་ནི་ལས་ཀྱི་སྒྲིབ་པའོ། །

[Block 175]
ཡང་ན་སྡུག་བསྔལ་དང་གནས་ངན་ལེན་ནི་སྡུག་བསྔལ་ཏེ། རྣམ་པར་སྨིན་པའི་སྒྲིབ་པའོ། །

[Block 176]
སྒྲིབ་པ་གསུམ་པོ་འདི་དག་གིས་འཇུག་པར་དཀའ་བ་ཉིད་དེ། དེའི་བར་དུ་གཅོད་པས་སོ། །

[Block 177]
བག་མེད་པ་དང་། ལེ་ལོ་དང་། མ་དད་པ་ཤས་ཆེ་བ་རྣམས་ནི་སྒྲུབ་པའི་བར་དུ་གཅོད་པའོ། །

[Block 178]
བྱ་བ་ངན་པ་ལ་ཆགས་པ་ཉིད་དང་། བར་དུ་ཉམས་པ་དང་། ཐོབ་པར་བྱ་བ་དང་། ཐོབ་པར་བྱེད་པ་ལ་དད་པ་མེད་པ་དང་། བག་མེད་པས་མི་སྒྲུབ་པ་དང་། དེ་བཞིན་དུ་ལེ་ལོས་ཞུགས་སུ་ཟིན་ན་ཡང་བར་ནས་མངོན་པར་ལྡོག་པ་སྟེ། མ་དད་པའི་ཤས་ཆེ་བ་རྣམས་ཀྱིས་སྒྲུབ་པ་གཡེལ་བའོ། །

[Block 179]
སེམས་བསྐྱེད་པའི་རྐྱེན་བཞིའི་བསྡུས་པའི་དོན་ནི། བྱང་ཆུབ་སེམས་དཔའི་རིགས་ངེས་པ༌[^96]སེམས་བསྐྱེད་པའི་རྐྱེན་གཉིས་དང་། བྱང་ཆུབ་ཏུ་གྱུར་པའི་སེམས་བསྐྱེད་པའི་རྐྱེན་གཉིས་སོ། །

[Block 180]
བྱང་ཆུབ་སེམས་དཔའི་རིགས༌[^97]ངེས་པ་རྣམ་པ་གཉིས་ནི་རྒྱ་ཆེ་བ་ལ་མོས་པ་དང་། ཟབ་པ་ལ་མོས་པའོ། །
--- END BLOCKS ---
