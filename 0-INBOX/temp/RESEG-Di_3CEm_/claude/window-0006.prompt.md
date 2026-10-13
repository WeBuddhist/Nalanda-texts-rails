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
[Block 211]
བྱང་ཆུབ་སེམས་དཔའི་སློབ་པ༌[^92]ལ་ཤིན་ཏུ་གུས་པར་བྱས་ནས་ཉེས་པ་མི་སྤྱོད་པས་ན་ཉམས་པ་མེད་པའི་ཕྱིར་ཉམས་པ་མེད་པའོ། །

[Block 212]
འདས་པའི་ཡུལ་ལ་རེ་བའི་སྲེད་པ་སྐྱེ་བ་དང་། མ་འོངས་པ་དང་ཚེ་ཕྱི་མ་རྣམས་སུ་སྨོན་པའི་སྲེད་པ་དང་། དེ་ལྟར༌[^93]བྱུང་བ་ལ་ཞེན་པའི་སྲེད་པ་སྟེ། དུས་གསུམ་གྱི་སྲེད་པའི་ཁབ་ཀྱིས་ཅུང་ཟད་དུ་ཡང་མ་གཙེས་པས་ན་སྐྱོན་མེད་པའོ། །

[Block 213]
ས་བཞིན་དུ་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ཀྱི་འདོད་པ་ཕུན་སུམ་ལྡན་པར་བྱེད་པ་དང་། ཐམས་ཅད་ཀྱི་གདུང་བ༌[^94]ཡོངས་སུ་སེལ་བ་དང་། ཐམས་ཅད་ཀྱི་ནད་འཇོམས་པ་དང་། ལྷ་དང་མི་རྣམས་ཀྱི་དོན་ཚད་མེད་པར་བསྒྲུབ་པ༌[^95]འབའ་ཞིག༌[^96]པ་ལ་འཇུག་པ་སྟེ། སྒྲའི་ཚུལ་དུའང་ལུས་དང་སེམས་ཀྱི་གདུང་བ་བསིལ་བར་བྱེད་པས་ན་ཚུལ་ཁྲིམས་སོ། །

[Block 214]
ཚུལ་ཁྲིམས་ནི་སྤྱད་པར་བྱ་བ་ཡིན་པས་ན་སྤྱོད་པ་ཞེས་བྱ་བའོ། །

[Block 215]
དེ་ལྟར་རྟག་པར་ནམ་བྱང་ཆུབ་ཀྱི་བར་དུ་སྤྱོད་པ་ནི་ཚུལ་ཁྲིམས་སྤྱོད་པ་དྲི་མ་མེད་པ༌[^97]ཡོངས་སུ་དག་པའམ་མ་ཉམས་པ་སྐྱོན་མེད་པར་སྤྱོད་པ་སྟེ། འདི་ནི་བྱང་ཆུབ་ཀྱི་སེམས་མི་བརྗེད་པའི་རྒྱུ་གཉིས་པའོ། །

[Block 216]
ལྷ་ཡི་སྐད་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ལྷ་ལ་ནི་ལྷའི་སྐད་ཀྱིས་སོ། །

[Block 217]
ཀླུ་དང་གནོད་སྦྱིན་དང་གྲུལ་བུམ་དང་མི་རྣམས་ལ་ཡང་སོ་སོའི་སྐད་ཀྱིས༌[^98]སོ། །

[Block 218]
མདོར་ན་འགྲོ་བ་ཇི་སྙེད་པ་ཐམས་ཅད་ཀྱི་སྐད་དུ་དེ་དག་ཐམས་ཅད་ལ་དེ་ལྟ་བུའི་སྐད་དུ་ཆོས་བཤད་པ་ནི་ནམ་བྱང་ཆུབ་ཀྱི་བར་དུའོ། །

[Block 219]
འདི་ནི་རྒྱུ་གསུམ་པའོ། །

[Block 220]
དེས་ཤིང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ངེས་པ་ནི་སེམས་ཀྱི་རྒྱུད་མཉེན་པའོ། །

[Block 221]
ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་སྦྱིན་པ་ལ་སོགས་པ་བཅུ་པོའོ།[^99] །

[Block 222]
དེ་ལ་རབ་ཏུ་བརྩོན་པ་ནི་མི་སྐྱོ་བའི་ཡིད་ཀྱིས་ཡོངས་སུ་བརྩོན་པར་བྱེད་པའོ། །

[Block 223]
བྱང་ཆུབ་ཀྱི་སེམས་ནི་ནམ་དུ་གར་ཡང་མི་འདོར་བར་བྱ་བ་སྟེ། མི་འདོར་བར་ནི་ནམ་བྱང་ཆུབ་པའི་བར་དུ་སྟེ། འདི་ནི་རྒྱུ་བཞི་པའོ། །

[Block 224]
ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་བཞི་པོས་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ལ་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་བསྒྲིབས་པར༌[^100]གྱུར་པ་དེ་དག་གི་གཉེན་པོ་བསྟན་པའོ། །

[Block 225]
ད་ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་མི་མཐུན་པའི་ཕྱོགས་རབ་ཏུ་སྤོང་བར་སྟོན་ཏེ། གང་ཞེ་ན། སྡིག་པ་གང་རྣམས་སྒྲིབ་པར་གྱུར་པ་དག །ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 226]
སྡིག་པ་སྒྲིབ་པར་གྱུར་པ་བྱང་ཆུབ་ཀྱི་སེམས་ལ་བར་ཆད་བྱེད་པ་དེ་དག་ཐམས་ཅད་ཀུན་ཡོངས་སུ་ཟད་ཅིང་སྤོང་བར་གྱུར་ཅིག་པའོ། །

[Block 227 [HEADING]]
#### ཆགས་པ་མེད་པར་སྦྱོར་བ། ^2-8-3-0

[Block 228]
ད་ནི་ཆགས་པ་མེད་པར་སྦྱོར་བ༌[^101]ནི་རྣམ་པ་གསུམ་པ་སྟེ། གང་ལས་དང་། གང་ན་དང་། ཇི་ལྟར་དང་གསུམ་མོ། །

[Block 229]
ལས་དང་ཉོན་མོངས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །གང་ལས་ཤེ་ན། ལས་དང་ཉོན་མོངས་པ་དང་བདུད་ཀྱི་ལས་རྣམས་ལས་སོ། །

[Block 230]
ལས་དེ་དམིགས་ཀྱིས་མ་ཕྱེད་པ༌[^102]ན་དགེ་བ་དང་མི་དགེ་བ་དང་མི་གཡོ་བ་དང་རྣམ་པ་གསུམ་ཆར་གཟུང་ངོ་། །དེ་ལ་མི་དགེ་བའི་ལས་དང་ཉོན་མོངས་པ་དང་བདུད་ཀྱི་ལས་རྣམས་ལས་རྣམ་པར་གྲོལ་ཞིང་དེ་དག་ལ་མི་ཆགས་པར་རྟག་ཏུ་སྤྱོད་པ་སྟེ། གང༌[^103]ཞེ་ན། ལྷ་ལ་སོགས་པའི་འཇིག་རྟེན་འགྲོ་བ་ན་གནས་པའི་ཚེའོ། །ཇི་ལྟ་བུ་ཞེ་ན། ཇི་ལྟར་པདྨོ་ཆུས་མི་ཆགས་པ་བཞིན། །ཞེས་བྱ་བ་སྟེ། ཇི་ལྟར་པདྨ་ཆུ་ལས་སྐྱེས་ཀྱང་ཆུས་མི་ཆགས་པ་དེ༌[^104]བཞིན་དུ་ལས་དང་ཉོན་མོངས་པ་དང་བདུད་ཀྱི་ལས༌[^105]ལ་སོགས་པ་འཇིག་རྟེན་གྱི་ཆོས་རྣམས་ཀྱིས་མི་ཆགས་པར་སྤྱོད་པའོ། །

[Block 231]
དེ་ལྟར་དགེ་བ་དང་མི་གཡོ་བ་གཉིས་ལས་ཀྱང་འབྲས་བུ་རྣམ་པར་སྨིན་པ་ལ༌[^106]རེ་བ་མེད་པར་བྱ་ཞིང་ཆགས་པ་མེད་པར་བྱ་སྟེ། འགྲོ་བ་ཐམས་ཅད་ལ་ཕན་ཞིང་བདེ་བ་འབའ་ཞིག་སྤྱོད་ཅིང་སྒྲུབ་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ཡིན་པར་བརྗོད་དོ། །ཇི་ལྟར་ཞེ་ན། དཔེར་ན། ཉི་ཟླ་ནམ་མཁར་ཐོགས་པ་མེད་ལྟར་སྤྱད། །ཅེས་བྱ་བ་སྟེ། ཉི་མ་དང་ཟླ་བ་ནི་འཇིག་རྟེན་ན་ཡིད་བཞིན་གྱི་ནོར་བུ་བཞིན་དུ་གཞན་གྱི་དོན་བྱེད་པ་ལ་བཞུགས་ཤིང༌[^107]བདག་གི༌[^108]ཅུང་ཟད་ལའང་མི་ཆགས་པར་ཉིན་མཚན་དུ་ནམ་མཁའ་ལ་རྒྱུ་བ་དེ་དང་འདྲ་བར་རོ། །

[Block 232]
དེ་ལ་བདུད་ཅེས་བྱ་བ་ནི་དགེ་བའི་སྲོག་གི་བར་ཆད་བྱེད་པས་བྱང་ཆུབ་དང་མི་མཐུན་པར་བྱེད་ཅིང་དམ་པའི་ལམ་ལས་ཟློག་པ་སྟེ། སྒྲའི་ཚུལ་དུའང་ཆོས་ཀྱིས་འཚོ་བའི་བར་ཆད༌[^109]བྱེད་ཅིང་གསོད་པས་ན་བདུད་ཅེས་བྱའོ། །

[Block 233]
དེའི་ལས་ནི་ཕན་པའི་དངོས་པོ་ལ་རྒྱུས༌[^110]འཚེ་བའོ།[^111] །

[Block 234 [HEADING]]
#### སེམས་ཅན་ལ་ཕན་གདགས་པ། ^2-8-4-0

[Block 235]
ཚེ་འདི་དང་ཕྱི་མ་ལ་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་གདགས་པ་སྟེ་རྣམ་པ་བཞི་པའོ། །དེ་ཡང་གང་ཞེ་ན། ངན་སོང་སྡུག་བསྔལ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 236]
འགྲོ་བ་ཐམས་ཅད་སྡིག་པས་སྡུག་བསྔལ་ཞིང་ངན་སོང་རྣམ་པ་གསུམ་དུ་སྐྱེས་པ་དེ་དག་རབ་ཏུ་ཞི་བར་བྱའོ། །

[Block 237]
དེ་ལ་ཡང་ཅིའི་ཕྱིར་ངན་སོང་གི་སྡུག་བསྔལ་འབའ་ཞིག་ཞི་བ་ཞེས་བྱ་ཞེ་ན། དེ་དག་གིས་ཤིན་ཏུ་གནོད་པར་བྱེད་པས་ན་གཙོ་བོར་བཤད་པ་ཡིན་གྱིས།[^112] འཁོར་བ་ཐམས་ཅད་ཀྱི་སྡུག་བསྔལ་ཡང་དེ་བཞིན་དུ་རབ་ཏུ་ཞི་བར་བྱ་བར་རིག་པར་བྱའོ། །

[Block 238]
ཅིའི་ཕྱིར་འགྲོ་བ་ཐམས་ཅད་མཆོག་ཏུ་བདེ་བ་ལ་འགོད་པར༌[^113]བྱ་ཞེ་ན། དེ་ལྟར་འགྲོ་བ་ཐམས་ཅད་ལ་ཕན་པར་སྤྱོད་པར༌[^114]བྱ་བ༌[^115]སྟེ། བླ་ན་མེད་པའི་ཡེ་ཤེས་ཐོབ་ཀྱི་བར་དུ་ཡོངས་སུ་མི་སྐྱོ་བའི་ཡིད་ཀྱིས་གཞན་དུ་མི་སྦྱོར་བར་སྤྱོད་པར་བྱ་བའོ། །ཇི་སྲིད་ཀྱི་བར་དུ་ཞེ་ན། ཞིང་གི་ཁྱོན་དང་ཕྱོགས་རྣམས་ཇི་ཙམ་པར་ཞེས་བྱ་བ་སྟེ། ཇི་ཙམ་པར་ཞེས་བྱ་བ་ནི་ཇི་སྲིད་པའོ། །

[Block 239]
ཞིང་གི་ཁྱོན་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་ཞིང་གི་ཁྱོན་ཇི་ཙམ་པ་སྟེ། བསྐལ་པ་གཅིག་ནས་གཅིག་ཏུ་གནས་པའོ། །

[Block 240]
ཕྱོགས་ཞེས་བྱ་བ་ནི་ཕྱོགས་བཅུར་སྦྱར་བར་བྱའོ། །

[Block 241 [HEADING]]
#### གོ་ཆ་བགོ་བ། ^2-8-5-0

[Block 242]
གོ་ཆ་བགོས་པ་ནི་རྣམ་པ་ལྔ་སྟེ། དེ་ཡང་རྣམ་པ་གསུམ་མོ། །

[Block 243]
སེམས་ཅན་གྱི་སྤྱོད་པའི་རྗེས་སུ་འཇུག་པ་དང་། སངས་རྒྱས་ཀྱི་ཆོས་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་དང་། དམ་པའི་ཆོས་རབ་ཏུ་བསྒྲགས་པ་རྣམས་ཏེ། དེ་ཡང་གང་ཞེ་ན། སེམས་ཅན་དག་གི་སྤྱོད༌[^116]དང་མཐུན་པར་འཇུག །ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 244]
སེམས་ཅན་རྣམས་ལ་རྒྱུ༌[^117]མེད་པའི་རང་བཞིན་སྤྱོད་པ་དང་། བདེ་བར་གནས་པ་དང་སེམས་ཀྱི་རྗེས་སུ་མཐུན་པར་འཛིན་ཅིང་སྤྱོད་པའོ། །

[Block 245]
བྱང་ཆུབ་སྤྱོད་པ་ཡོངས་སུ་རྫོགས་བྱེད་ཅིང་། །ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་པའི་དོན་དུ་སྤྱོད་པ་ནི་བྱང་ཆུབ་ཀྱི་སྤྱོད་པ་སྟེ། དེ་ཡོངས་སུ་རྫོགས་པ་ནི་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་འགྲུབ་པར་བྱེད་པའོ། །

[Block 246]
བཟང་པོ་སྤྱོད་པ་དག་ནི་རབ་སྟོན་ཅིང་། །ཞེས་བྱ་བ་ལ་འདིར་བཟང་པོ་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་དམ་པའི་ཆོས་འཆད་པ་ཉིད་གཟུང༌[^118]སྟེ་ཐབས་ཀྱིས༌[^119]སྒྲོ་བཏགས་པ་དང་། འཆད་པ་དང་། སྟོན་པའོ། །

[Block 247]
མ་འོངས་བསྐལ་པ་ཀུན་དུ་སྤྱོད་པར་གྱུར། །ཅེས་བྱ་བ་ནི་མ་འོངས་པའི་བསྐལ་པ་མཐའ་ཡས་པ་ཐམས་ཅད་དུ་མི་སྐྱོ་བའི་ཡིད་ཀྱིས་སྤྱོད་པའོ། །

[Block 248 [HEADING]]
#### སྐལ་བ་མཐུན་པའི་བྱང་ཆུབ་སེམས་དཔའ་བསྟེན་པ། ^2-8-6-0

[Block 249]
ལུས་དང་ངག་དང་ཡིད་ཀྱི༌[^120]སྤྱོད་པ་དང་། སྨོན་ལམ་གྱིས་སྐལ་བ༌[^121]མཉམ་པའི་བྱང་ཆུབ་སེམས་དཔའ་དང་མཐུན་པར་བསྟན་པ༌[^122]སྟེ་དེ་ནི་རྣམ་པ་དྲུག་པའོ། །དེ་ཡང་གང་ཞེ་ན། བདག་གི་སྤྱོད་དང་མཚུངས་པར་གང་སྤྱོད་པ། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 250]
བདག་གི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་དང་མཐུན་པར་གང་སྤྱོད་པ་དེ་དག་དང་རྟག་པར་ནམ་བྱང་ཆུབ་པའི་བར་དུ་འགྲོགས་པ་དང་། ལུས་དང་ངག་དང་ཡིད་ཀྱིས་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་དང་། སྨོན་ལམ་དེ་དང་ལྷན་ཅིག་ཏུ་སྤྱོད་པར་ཤོག་ཤིག༌[^123]པའོ། །
--- END BLOCKS ---
