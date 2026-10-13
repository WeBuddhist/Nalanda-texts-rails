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
ལ་ལའི་ཞལ་ནས་ནི༌[^110]ཇི་སྲིད་དམིགས་པ་དང་བཅས་པའི་སེམས་དེ་ནི་ཀུན་རྫོབ་ཀྱི་རྣམ་པ་སྟེ། སྨོན་པའི་སེམས་སོ་ཞེས་བཞེད་དོ། །

[Block 212]
གཞན་ནི་ཚོགས་ཀྱི་ལམ་པ་ཐར་པའི་ཆ་དང་མཐུན་པའི་དགེ་བའི་རྩ་བ་བསྐྱེད་པའི་སེམས་དེ་ནི་སྨོན་པའི་སེམས་ཡིན་ནོ་ཞེས་བཞེད་དོ། །

[Block 213]
ཁ་ཅིག་ནི་བསོད་ནམས་མངོན་པར་འདུ་བྱ་བ་དང་མི་ལྡན་པའི་སེམས་ནི་སྨོན་པའི་སེམས་ཡིན་ནོ་ཞེས་བཞེད་དོ། །

[Block 214]
ལ་ལ་ནི། འགྲོ་བར་འདོད་དང་འགྲོ་བ་ཡི། །ཞེས་པས་རྫོགས་པའི་བྱང་ཆུབ་ཡུལ་དུ་བྱེད་པ་ཙམ་དེ་ནི་སྨོན་པའི་སེམས་ཡིན་ནོ་ཞེས་བཞེད་དོ། །

[Block 215]
དེ་མ་ཡིན་པ་གཞན་ཡང་ཡོད་དེ་གཞུང་མངས་པར་འགྱུར་རོ། །

[Block 216 [HEADING]]
### གཉིས་པ་བྱང་ཆུབ་ཀྱི་སེམས་དེའི་ཆོ་ག། ^3-2-0

[Block 217]
གཉིས་པའི་དོན་ལ་ཡང་ཐ་དད་པར་གྱུར་ཏེ། དེ་དག་ཉིད་ཀྱིས་མཛད་པའི་གཞུང་དེ་དང་དེར་བལྟ་བར་བྱའོ། །

[Block 218 [HEADING]]
### གསུམ་པ་བྱང་ཆུབ་ཀྱི་སེམས་དེ་སྐྱེ་བའི་ཚུལ། ^3-3-0

[Block 219]
གསུམ་པའི་དོན་ལ་ཡང་ཁ་ཅིག་ནི་གང་ཟག་གི་དྲུང་དུ་བྱང་ཆུབ་ཀྱི་སེམས་བསྐྱེད་པས་ཀྱང་དེ་སྐྱེ་བར་བཞེད་དོ། །

[Block 220]
ལ་ལ་ནི་སངས་རྒྱས་ཀྱི་སྤྱན་སྔར་མ་ཡིན་པར་སེམས་བསྐྱེད་པར་མི་བྱའོ་ཞེས་བཤད་དོ། །

[Block 221]
གཞན་དག་ནི་འདི་སྐད་དུ། བྱང་ཆུབ་ཀྱི་སེམས་སྐྱེ་བ་ནི་རྣམ་པ་བཞིའི་ཚུལ་གྱིས་སྐྱེ་བར་འགྱུར་རོ་ཞེས་བཞེད་དོ། །

[Block 222]
དོན་འདི༌[^111]

[Block 223 [HEADING]]
### བཞི་པ་སེམས་དེའི་བསླབ་བྱའི་ཚུལ། ^3-4-0

[Block 224]
བཞི་པ་ལ་ཡང་ཐ་དད་པར་གྱུར་ཏེ། ཁ་ཅིག་གི་ཞལ་ནས་བྱང་ཆུབ་སེམས་དཔའ་ནི་ལྔ་སྟེ། སེམས་དང་པོ་བསྐྱེད་པ་དང་། སྤྱོད་པ་ལ་འཇུག་པ་དང་། ཕྱིར་མི་ལྡོག་པ་དང་། མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པ་དང་། སྐྱེ་བ་གཅིག་གིས་ཐོགས་པའོ། །

[Block 225]
དེ་ལ་སྔ་མ་གཉིས་ཀྱི་བསླབ་པ་ཇི་སྙེད་པའི་ཞེས་བཞེད་དོ། །

[Block 226]
ལ་ལས༌[^112]ནི་མདོ་ལས་གསུངས་པ་ཐམས་ཅད་བསྲུང་བར་བྱ་བ་ཡིན་ནོ་ཞེས་བཞེད་དོ། །

[Block 227]
ལ་ལ་ནི་ཚོགས་ཀྱི་ལམ་པའི་བསླབ་པ་ཇི་སྙེད་པ་བསྲུང་བར་བྱའོ་ཞེས་བཞེད་དོ། །

[Block 228]
གཞན་དག་ནི་བསླབ་པ་འདི་དང་འདི་ལྟ་བུ་ཞེས་མི་བཞེད་དོ། །

[Block 229]
ཁ་ཅིག་ནི་སྐྱབས་སུ་འགྲོ་བའི་བསླབ༌[^113]པའི་ཐོག་ཏུ་སྡོང་པོ་བཀོད་པ༌[^114]དང་། དགེ་བའི་རྩ་བ་ཡོངས་སུ་འཛིན་པའི་མདོ་དང་། དད་པའི་སྟོབས་བསྐྱེད་པའི་མདོ་ལ་སོགས་པར་ཡང་བཤད་མོད་ཀྱི། རེ་ཞིག་འཕགས་པ་འོད་སྲུངས་ཀྱིས་ཞུས་པའི་མདོ་ལས་བྱང་ཆུབ་ཀྱི་སེམས་བརྗེད་པར་འགྱུར་བ་དང་། བརྗེད་པར་མི་འགྱུར་བའི་ཆོས་བརྒྱད་བསྲུང་བར་བྱའོ་ཞེས་བཞེད་དོ། །

[Block 230]
དེ་དག་ནི་མཚོན་པ་ཙམ་དང་། འདི་ལྟར་སྔོན་གྱི་མཁས་པ་ཆེན་པོ་དེ་དག་གི་ལུགས་ཐམས་ཅད་འདིར་བཀོད་པར་གྱུར་ན་ནི་གཞུང་ཤིན་ཏུ་མངས་པར་འགྱུར་རོ། །

[Block 231]
སློབ་དཔོན་ཆེན་པོ་དེ་རྣམས་ནི་ཐེག་པ་ཆེན་པོའི་ལམ་ལ་ཚད་མའི་སྐྱེས་བུར་གྱུར་པ། བྱམས་པ་ཆེན་པོ་དང་སྙིང་རྗེ་ཆེན་པོ་ལ་གོམས་པ། བྱང་ཆུབ་ཀྱི་སེམས་རྣམ་པ་གཉིས་ལ་ཐུགས་བརྟན་པའོ། །

[Block 232]
དེ་ལ་སློབ་དཔོན་ཁ་ཅིག་གིས་ཕྱག་རྒྱ་ཆེན་པོའི་དངོས་གྲུབ་བརྙེས་པའོ། །

[Block 233]
ལ་ལས་ནི་བདེན་པ་གཟིགས་པའོ། །

[Block 234]
ལ་ལས་ནི་འཇིག་རྟེན་ཆོས་མཆོག་ཆེན་པོ་བརྙེས་ནས་སྤྲུལ་པའི་སྐུ་ལས་གདམས་ངག་ཐོབ་པ་དག་ཡིན་པ་དང་། མདོ་ཉིད་ན༌[^115]ཡང་དེ་དག་ཇི་ལྟར་བཞེད་པ་བཞིན་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པས། དེ་དག་ནི་ལམ་ཆེན་པོ་ཉིད་ཡིན་ནོ་ཞེས་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 235]
འོན་ཀྱང་རང་རང་གི་བླ་མ་དག་གིས་ཇི་ལྟར་གནང་བའི་ལུགས་དེ་གཟུང་བར་བྱའོ་ཞེས་བདག་གི་བླ་མ་དག་གསུང་ངོ་། །དེ་ལ་འདིར་རེ་ཞིག་སློབ་དཔོན་འཕགས་པ་ཀླུ་སྒྲུབ་དང་། སློབ་དཔོན་འཕགས་པ་ཐོགས་མེད་དང་། སློབ་དཔོན་འཕགས་པ་ཤཱན་ཏ་དེ་བ་དག་སྨོན་པ་བྱང་ཆུབ་ཀྱི་སེམས་བསྐྱེད་པའི་ཆོ་གའི་ཚུལ་འདི་ལ་ཐ་དད་པ་མེད་ཅིང་མཐུན་པ་དང་། ད་ལྟར་བདག་གི་བླ་མ་རྗེ་བཙུན་དཔལ་བྱང་ཆུབ་བཟང་པོ་དང་། བླ་མ་རྗེ་བཙུན་སུ་ཝརྞྞ་དྭཱི་པ་དག་ཀྱང་འཕགས་པ་དེ་དག་གི་རྗེས་སུ་འབྲང་བ་དང་། བདག་ཀྱང་བླ་མ་རྗེ་བཙུན་དེ་དག་གི་རྗེས་སུ་འབྲང་བ་ཡིན་པས་བདག་ལ་སློབ་མའི་ཚོགས་ཀྱིས་གསོལ་བ་བཏབ་ནས་བྱས་པའི་ཆོ་གའི་ཐབས་ཅུང་ཞིག་བདག་གིས༌[^116]བཀོད་པ་ནི་འཕགས་པ་ཀླུ་སྒྲུབ་དང་། འཕགས་པ་ཐོགས་མེད་དང་། འཕགས་པ་ཤཱན་ཏ་དེ་བ་དག་གི་ལུགས་ཡིན་ནོ་ཞེས་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 236]
དེ་དག་ནི་ཞར་ལ་བཤད་པའོ། །

[Block 237 [HEADING]]
## སྔོན་དུ་འགྲོ་བའི་ཆོས། ^4-0

[Block 238]
དེ་ལ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ལྗོན་ཤིང་སྐྱེ་བ་ལ་ཆུའི་རླན་ལྟ་བུའི་ཆོས་གཉིས་སྔོན་དུ་འགྲོ་བ་ཡིན་ཏེ། འདི་ལྟར་སེམས་སྦྱང་བ༌[^117]དང་། བླ་མ་ལ་ཡོན་དབུལ་བའོ། །

[Block 239 [HEADING]]
### བླ་མ་ལ་ཡོན་དབུལ་བ། ^4-1-0

[Block 240]
བླ་མ་ལ་ཡོན་དབུལ་བ་ཡང་འཕགས་པ་བསྐལ་པ་བཟང་པོའི་མདོ་དང་། སྙིང་རྗེ་ཆེན་པོ་ལས་ཇི་ལྟར་འབྱུང་བ་ལྟ་བུའོ། །

[Block 241 [HEADING]]
### སེམས་སྦྱང་བ། ^4-2-0

[Block 242]
སེམས་སྦྱང་བ་ནི་འཕགས་པ་ཀུན་དུ་བཟང་པོའི་སྨོན་ལམ་སྔར་ཇི་སྐད་བརྗོད་པ་དང་།[^118] ཡང་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པའི་ཚུལ་གྱིས་བྱ་བ་ཡིན་ནོ། །

[Block 243]
དེ་ནས་སྐྱེ་བོ་ཆེན་པོའི་ཆོས་ལུགས་ཤིང་རྟ་ཆེན་པོའི་ལམ་བླ་མ་གཅིག༌[^119]ནས་གཅིག་ཏུ་བརྒྱུད་པ་སློབ་དཔོན་ཆེན་པོ་ཤཱན་ཏ་དེ་བའི་ཆོ་གའམ། སློབ་དཔོན་ཆེན་པོ་ཐོགས་མེད་ཀྱི་ཆོ་གས་ཚད་མེད་པ་བཞི་པོ་བསྒོམ་པ་སྔོན་དུ་སོང་བས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པར་བྱའོ། །

[Block 244]
དེ་ལྟར་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའི་སློབ་མའི་རྒྱུད་དེ་ལས།

[Block 245]
སེམས་ཀྱི་ཁྱད་པར་ཇི་ལྟ་བུ་ཞིག་སྐྱེ་ཞེ་ན། དོན་འདི་ལ་དགོངས་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་འཕགས་པ་བློ་གྲོས་མི་ཟད་པས་བསྟན་པའི་མདོ་ལས་གསུངས་ཏེ། ཇི་སྐད་དུ། བློ་གྲོས་མི་ཟད་པས་སྨྲས་པ། བཙུན་པ་ཤཱ་ར་དྭ༌[^120]ཏིའི་བུ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་སེམས་དང་པོ་བསྐྱེད་པ་དེ་ནི་མི་ཟད་པའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། མ་འདྲེས་པའི་ཕྱིར་རོ། །

[Block 246]
སེམས་དེ་ནི་ཉོན་མོངས་པ་ཐམས་ཅད་དང་མ་འདྲེས་པར་སྐྱེས་སོ། །

[Block 247]
ཐེག་པ་གཞན་ལ་འདོད་པ་མེད་པས་སེམས་དེ་ནི་མ་འབྲེལ་བར་སྐྱེས་སོ། །

[Block 248]
ཕས་ཀྱི་རྒོལ་བ་ཐམས་ཅད་ཀྱིས་མི་འཕྲོགས་པས་སེམས་དེ་ནི་སྲ་བར་སྐྱེས་སོ། །

[Block 249]
སེམས་དེ་ནི་བདུད་ཐམས་ཅད་ཀྱིས་མི་ཕྱེད་པར་སྐྱེས་སོ། །

[Block 250]
དགེ་བའི་རྩ་བ་ཐམས་ཅད་ཡང་དག་པར་སྒྲུབ་པས་སེམས་དེ་བརྟན་པར་སྐྱེས་སོ། །
--- END BLOCKS ---
