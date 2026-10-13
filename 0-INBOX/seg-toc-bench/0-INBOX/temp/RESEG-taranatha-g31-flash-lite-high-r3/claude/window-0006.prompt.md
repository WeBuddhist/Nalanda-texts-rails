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
བྱེད་པ་ནི་གུས་པ་ཡང་དག་པར་ལྡན་པས་སོ། །

[Block 212]
བྱེད་པ་པོ་བློ་ལྡན་གང་གིས་སོ། །

[Block 213]
ཚུལ་ཇི་ལྟར་ན། འདིར་རབ་ཏུ་དང་ཞིང་བརྩོན་འགུས་དང་ལྡན་པས་ཏེ། བསྟོད་པ་འདི་བརྗོད་པ་དང་། སྲོད་དང་ཐོ་རངས་ལངས་པ་སྟེ་ལྡང་བ་ཡང་བར་བྱས་ནས། ཕྱག་འཚལ་བ་དང་མཆོད་པ་སྔོན་དུ་འགྲོ་བས། འཕགས་མའི་ཡོན་ཏན་ཡིད་ལ་དྲན་པས་སོ། །

[Block 214]
དེའི་ཕན་ཡོན་ནི་མི་འཇིགས་པ་ཐམས་ཅད་རབ་ཏུ་སྟེར་བ་སྟེ། འཇིགས་པ་ཆེན་པོ་བརྒྱད་དང་བཅུ་དྲུག་ལ་སོགས་པ་འཇིགས་པ་ཐམས་ཅད་ལས་སྐྱོབ་པ་དང་། མི་འཇིགས་པའི་གནས་དབང་ཕྱུག་ཕུན་སུམ་ཚོགས་པ་སྩོལ་བར་མཛད་པའོ། །

[Block 215]
འདིར་རབ་དང་བརྗོད་ཅིང་ཞེས་པ་ལ། རྒྱ་སྐད་དུ་བ་ཞེས་པ་ཡོད་བས་བརྩོན་པས་ཀློག་ཅིང་ཞེས་བརྗོད་ན་བདེའོ། །

[Block 216]
དེ་བས་ན་བློ་ལྡན་གང་གིས་སྲོང་སོགས་ཐུན་དྲུག་ཏུ་ལྷ་མོ་ལ་གུས་ཤིང་ཡོན་ཏན་དྲན་པའི་སྒོ་ནས། བརྩོན་པས་བསྟོད་པ་འདི་བཀླགས་ན། ཕན་ཡོན་འདི་དག་ཡོད་དོ་ཞེས་པ་སྟེ་གོང་འོག་ཐམས་ཅད་དུ་དེ་ལྟར་གོ་བར་བྱའོ། །

[Block 217]
སྡིག་པ་ནི་སྡིག་པའི་འབྲས་བུ་སྟེ། ནད་དང་གདོན་དང་། བྱུར་ཆགས་སྐལ་བ་ངན་པ་སྔར་ཡོད་རྣམས་ཐམས་ཅད་རབ་ཏུ་ཞི་ཞིང་སླར་འབྱུང་བར་འགྱུར་བ་རྣམས་བཟློག་པའོ། །

[Block 218]
དེ་བཞིན་དུ་སྔར་སྡིག་པའི་ལས་ཀྱི་མཐུས། ངན་འགྲོར་སྐྱེ་ངེས་པའི་ལས་ཅན་ཡིན་ཡང་། བསྟོད་པ་བཀླགས་པའི་གཟི་བརྗིད་ཀྱིས་སྡིག་ལས་ཟང་དེ་ངན་འགྲོའི་སྐྱེ་བ་ཐམས་ཅད་འཇོམས་པའི་གནས་སྐབས་ཐོབ་པ་ཉིད་དེ། ངན་འགྲོར་སྐྱེ་བར་མི་འགྱུར་རོ། །

[Block 219]
དེའི་ལྡོག་དོན་དུ་བདེ་འགྲོའི་སྐྱེ་བ་ཕུན་སུམ་ཚོགས་པ་འགྲུབ་པ་ཡང་བསྟན་ཏེ། དེས་ནི་འཁོར་བ་ཉིད་དུ་ཡང་ཚེ་འདི་དང་ཕྱི་མའི་ཕན་ཡོན་གཉིས་ཀར་བསྟན་ནོ། །

[Block 220]
རྒྱལ་བ་བྱེ་བ་སོགས་ལ་བསྟོད་པ་བཟླས་པ་དང་དེའི་སྒྲུབ་པ་ལ་གནས་པས། བཅོམ་ལྡན་འདས་མ་འདི་ཉིད་དང་ལྷན་ཅིག་ཏུ་གཤེགས་ཤིང་བཞུགས་པའི་རྒྱལ་བ་སངས་རྒྱས་སྤྲུལ་པའི་སྐུ་བྱེ་བ་ཕྱག་བདུན་རྣམས་ཀྱིས། ཞལ་ཡང་སྒྲུབ་པ་དེས་མྱུར་དུ་མཐོང་པར་འགྱུར་ལ། མཐོང་ནས་ཀྱང་དངོས་སམ་རྨི་ལམ་དུ་དེ་རྣམས་ཀྱིས་འོད་ཟེར་རམ་ཕྱག་ལས་བདུད་རྩིའི་རྒྱུན་འབབ་པས་དབང་བསྐུར་བར་འགྱུར་རོ། །

[Block 221]
འདིས་ནི་སློབ་མ་སྨིན་བྱེད་ཀྱི་ཚེ། ཆུ་དབང་བསྐུར་བ་ཡང་བསྟན་ནོ། །

[Block 222]
དེ་ལྟར་དབང་བསྐུར་བ་དེའི་རྐྱེན་གྱིས། སྒྲིབ་པ་མང་པོ་ནི་བྱང་། ཏིང་ངེ་འཛིན་དང་གཟུངས་ཀྱི་ཁྱད་པར་མང་པོ་ཐོབ་སྟེ་འཁོར་ཕུན་སུམ་ཚོགས་པ་འདི་ལས་ཆེས་ཆེ་བའི་ཡོན་ཏན་དུ་མ་ཉིད་དང་ལྡན་པའི་ཕྱག་རྒྱ་ཆེན་པོའི་དངོས་གྲུབ་རིམ་གྱིས་ཐོབ་པར་འགྱུར་ཞིང་། དེ་ཐོབ་ནས་ཀྱང་འཕགས་པའི་ས་རྣམས་བགྲོད་དེ། མཐར་ཐུག་རྫོགས་པའི་སངས་རྒྱས་ཀྱི་གོ་འཕང་དེར་འགྲོ་བར་འགྱུར་རོ། །ཞེས་ཐར་པ་དང་ཐམས་ཅད་མཁྱེན་པ་ཐོབ་པའི་ཕན་ཡོན་བསྟན་ནོ། །

[Block 223]
གནས་སྐབས་སྔགས་ཀྱི་མཐུས་ཕན་ཡོན་གཞན་ཡང་བསྟན་པའི་ཕྱིར།

[Block 224]
ཚིགས་བཅད་གསུམ་པ་གསུངས་པ་ལས།

[Block 225]
དེ་ཡི་དུག་ནི་སོགས་ལ། བརྟན་པ་ནག་པོ་བརྩེགས་པ་ལ་སོགས་པའི་དུག་དང་། གཡོ་བ་སྡིག་སྤྲུལ་དང་ལྷོག་པ་དང་ཤུ་བ་ལ་སོགས་པའི་དུག་སྟེ། གནས་པ་ཞེས་པ་ནི་བརྟན་པ་དང་མིང་གི་རྣམ་གྲངས་སུ་འགྱུར་བ་གོ་བདེ་བའི་ཕྱིར་གཉིས་ཀ་བརྗོད་པ་སྟེ། གཉན་ལོས་བརྟན་པའམ་ནི་གཡོ་བ་ཡང་རུང་ཞེས་པའམ། ནམ་མཁའ་བཟང་པོས། བརྟན་གཡོ་གང་ཡང་རུང་བ་དག་ནི། ཞེས་བཅོས་པ་གོ་བདེའོ། །

[Block 226]
དེ་ལྟ་བུའི་དུག་ནི་དག་པོ་ཆེན་པོ་སྟེ། སྲོག་འཕྲོག་པ་དང་སྡུག་བསྔལ་ཚབས་ཆེན་བསྐྱེད་པའོ། །

[Block 227]
དེ་ལྟ་བུའི་དུག་དེ་ཡང་སྒྲོལ་མའི་རིག་སྔགས་དྲན་པ་ཙམ་གྱིས། རབ་ཏུ་འཇིགས་པ་སྟེ་དེའི་གནོད་པ་རྣམས་སེལ་ཞིང་། བདུད་རྩིའི་ལ་སོགས་པར་འགྱུར་བའོ། །

[Block 228]
ཟོས་པ་དང་ནི་འཐུངས་པ་ཉིད་ཀྱང་ཞེས་པ་ལྟར་ན། དྲན་པས་རབ་ཏུ་སེལ་ཞེས་པའི་སྔ་རོལ་དུ་སྦྱར་ཏེ། དུག་དེ་ལྟ་བུ་ཟོས་པ་དང་འཐུངས་པ་ཉིད་ཀྱང་། རེག་པ་དུག་ཅན་གྱི་བྱུགས་པ་སོགས་ཀྱང་རིག་སྔགས་དྲན་པས་སྐད་ཅིག་ལ་སེལ་ཞེས་པའི་དོན་ཡིན་ལ། འགྱུར་གཞན་ལས་ཟོས་པ་དང་ནི་ཞེས་པ་འདི། དྲན་པས་ཞེས་པའི་ཚིག་གི་འོག་ཏུ་འདོན་པ་ལྟར་ན། ཤྭ་ལོ་ཀ་འོག་མ་དང་སྦྲེལ་བར་འགྲོ་མོད། འོན་ཀྱང་ཁ་དི་ཏཾ་པི་ཏ་མེ་ཝ་པ་ཅེས་འབྱུང་བ་ལྟར་ན། དཀྱུས་ཉིད་བདེའོ། །

[Block 229]
གདོན་དང་སོགས་ལ་གདོན་རྣམ་པ་སྣ་ཚོགས་ཀྱི་གནོད་པ་དང་། རིམས་ལ་སོགས་པའི་ནད་དང་། དུག་གིས་གཟིར་བ་ལ་སོགས་པའི་སྡུག་བསྔལ་གྱི་ཚོགས་རང་ལ་གནས་པ་རྣམས་ཀྱང་སྒྲོལ་མའི་རིག་སྔགས་འདིའི་མཐུས་རྣམ་པར་སྤངས་ཏེ། བདེ་བ་ཐོབ་པར་མ་ཟད། རིག་སྔགས་མཁན་པོ་དེས་ཡིད་ཀྱིས་བསམ་པ་ཙམ་མམ། ཞི་བའི་ལས་ཀྱི་སྦྱོར་བ་བྱས་པ་ཙམ་གིས། སེམས་ཅན་གཞན་པ་རྣམས་ལ་ཡང་སྡུག་བསྔལ་དེ་སྤོང་བར་བྱེད་དོ། །

[Block 230]
དེ་བཞིན་དུ་ཀུན་གྱིས་ཐ་མའི་ཚིག་རྐང་ཡར་བླངས་ཏེ་བགེགས་རྣམས་མེད་ཅིང་བདུད་ལ་སོགས་པ་རྣམས་སོ་སོར་འཇོམས་པར་འགྱུར་རོ། །

[Block 231]
གཉིས་གསུམ་བདུན་བདུན་དུ་སོགས་ལ་གཉིས་ནི་ཉིན་དང་མཚན་མོར་བརྗོད་པའོ། །

[Block 232]
གསུམ་ནི་ཉིན་དང་མཚན་ལ་ཡང་རུང་སྟེ་ཐུན་གསུམ་མོ། །

[Block 233]
དེ་རེ་རེར་ཡང་སྒྲུབ་པ་དང་འབྲེལ་བར་བསྟོད་པ་ལན་བདུན་དུ་བརྗོད་པ་སྟེ། བླ་མའི་ངག་ལས་འབྱུང་བ་ལྟར་རོ། །

[Block 234]
དེ་ལྟར་བརྗོད་ན་བུ་སྟེ་ཁྱིམ་པའི་ཕྱོགས་ལ་རིགས་བརྒྱུད་དམ། རབ་ཏུ་བྱུང་བའི་ཕྱོགས་ལ་ནི་ཆོས་ཀྱི་བུ་སློབ་མ་འདོད་པས་བུའམ་སློབ་མ་མང་པོ་དག་ཐོབ་པར་འགྱུར་ཞིང་། ནོར་འདོད་པས་ནི་ནོར་དང་ལོངས་སྤྱོད་རྣམས་ཉིད་ཐོབ་པར་འགྱུར་ལ། གཞན་ཡང་ཞི་བ་ལ་སོགས་པའི་ལས་དང་། རིལ་བུ་དང་མིག་སྨན་དང་། རལ་གྲི་དང་གནོད་སྦྱིན་མོ་དང་གཏེར་ཆེན་པོ་ལ་སོགས་པ། དངོས་གྲུབ་རྣམ་པ་སྣ་ཚོགས་པ་ཐམས་ཅད་ཐོབ་པར་འགྱུར་རོ། །

[Block 235]
འཕགས་མ་སྒྲོལ་མ་ལ་བསྟོད་པ། ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་རྣམ་པར་སྣང་མཛད་ཀྱིས་གསུངས་པ་ཞེས་པ་ལ་འདི་སྒྲོལ་མའི་རྒྱུད་ཀྱི་རྒྱལ་པོ་རྟོག་པ་བདུན་བརྒྱ་པ་ལས་འབྱུང་བའོ། །

[Block 236]
ཞེས་གགས་སོ། །

[Block 237]
ལས་སྣ་ཚོགས་པའི་རྒྱུད་དུ་གྲགས་པ་དེང་སང་ཕྱོགས་འདིར་ཡོད་བ་འདི་ནའང་སྣང་མོད། འདི་ནི་མཁས་པ་རྣམས་བརྩམས་རྒྱུད་ཡིན་པར་བཞེད་པ་དོན་ལ་གནས་པས་འདི་ནས་མིན་ནོ། །

[Block 238]
རྒྱུད་རྒྱས་པའི་དུམ་བུ་དང་།

[Block 239]
བསྡུས་རྒྱུད་ལ་སོགས་པ་ཡིན་པའང་མི་འགལ་ལོ། །རྫོགས་སོ་ནི་ས་མཱཔྟ་སྟེ་ཡང་དག་པར་ཐོབ་པའོ། །

[Block 240 [HEADING]]
## བསྔོ་བ། ^a-0

[Block 241 [VERSE]]
དུས་གསུམ་རྒྱལ་བའི་ཡུམ་གྱུར་ལ། །
བསྟོད་པའི་རྒྱུད་འདི་རབ་བཤད་ལས། །
དགེ་བ་གང་ཞིག་ཐོབ་པ་དེས། །
འཕགས་མའི་གོ་འཕང་འགྲུབ་པར་ཤོག །

[Block 242 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 243 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 244]
ཅེས་པ་ཕྱག་འཚལ་ཉེར་གཅིག་གིས་བསྟོད་པའི་རྣམ་པར་བཤད་པ་འདི་ཡང་ཏཱ་ར་ནཱ་ཐས་སྨྲས་པའོ། །
--- END BLOCKS ---
