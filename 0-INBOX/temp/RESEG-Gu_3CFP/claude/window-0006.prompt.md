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
དང་པོ་སེམས་བསྐྱེད་པའི་མཚན་ཉིད་དང་། ཁྱད་པར་གྱི་མཚན་ཉིད་དང་། རྒྱུན་མི་འཆད་པར་སེམས་བསྐྱེད་པའི༌[^117]རྐྱེན་བཞི་དང་། རྒྱུ་བཞི་དང་། རྒྱུ་དང་སྟོབས་གང་དག་གིས་སེམས་བསྐྱེད་པ་བསྟན་པས༌[^118]དེའི་མི་མཐུན་པ་ལས་ལྡོག་པ་དང་།

[Block 212]
དང་པོ་སེམས་བསྐྱེད་པར་བསྟེན༌[^119]པའི་ངོ་མཚར་རྨད་དུ་བྱུང་བའི་ཆོས་དང་། དེའི་ཕན་ཡོན་ནི་རང་གི་མཚན་ཉིད་དང་། ཁྱད་པར་གྱི་མཚན་ཉིད་དང་། སྐྱེ་བའི་རྒྱུ་དང་རྐྱེན་དང་སྟོབས་དང་། དེ་ལ་རྨོངས་པ་རྣམས་ལ་བསྟན་པ་དང་། ངོ་མཚར་རྨད་དུ་བྱུང་བའི་ཆོས་ལ་སོགས་པས་རིགས་མ༌[^120]ངེས་པ་དང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་རིགས་ལ་ཞུགས་པ་རྣམས་རྣམ་པར་བཟློག་ནས་གཞུག་པའི་དོན་དང་། མ་ངེས་པའི་རིགས་ཅན་རྣམས་སངས་རྒྱས་ཉིད་ལ་རབ་ཏུ་དགོད་ཅིང་ངེས་པར་བཟུང་བ་དང་། བྱང་ཆུབ་སེམས་དཔའི༌[^121]རིགས་ཅན་བག་མེད་པ་དང་། ཞུམ་པ་དང་ཡང་དག་པར་རབ་ཏུ་ཞུགས་པ་རྣམས་ལ་གོ་རིམ་ཇི་ལྟ་བ་བཞིན་དུ་ཡང་དག་པར་བཟུང་བ་དང་། ཡང་དག་པར་གཟེངས་བསྟོད་པ་དང་། ཡང་དག་པར་མགུ་བར་བྱ་བའོ། །

[Block 213]
འབྲས་བུ་དང་བཅས་པའི་བསོད་ནམས་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའི་ཕན་ཡོན་མདོར་བསྡུས་པའི་དོན་ནི་མཐོང་བའི་ཆོས་ལ་བདག་གི་ལུས་ལ་གནོད་པ་མེད་པ་དང་། འཁོར་ལོས་སྒྱུར་བའི་རྫུ་འཕྲུལ་གྱི་ཡོན་ཏན་ཞེས་བྱ་བ་ལ་སོགས་པ་བསྟན་པ་ནི། མ་འོངས་པའི་དུས་སུ་ཐོབ་པའི་སྐྱེ་བ་ལ་བདག་དང་གཞན་གྱི་དོན་སྒྲུབ་ནུས༌[^122]པའི་ལུས་རབ་ཏུ་འཐོབ་པ་སྟེ། ཚེ་བརྗེས་པའི་འོག་ཏུ་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །

[Block 214]
མཐོང་བའི་ཆོས་ཉིད་ལ་བདག་ལ་གནོད་པའི་ལུས་དང་སེམས་ཀྱི་གནས་ངན་ལེན་དང༌[^123]ཉམས་སྨད་པའི་ཕྱིར་བདག་ལ་གནོད་པའི་ངོ་བོ་མེད་དོ། །

[Block 215]
དེའི་བསོད་ནམས་ཀྱི་དབང་གིས་གཞན་གྱིས་བྱས་པའི་སྔགས་ལ་སོགས་པས་གཞན་ལ་གནོད་པ་ཡང་མེད་དོ།[^124] །བྱང་ཆུབ་སེམས་དཔའི༌[^125]རིགས་ལ་གནས་པ་ནི་རང་བཞིན་གྱིས་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །

[Block 216]
བདག༌[^126]དང་གཞན༌[^127]ལ་གནོད་པའི་ཉོན་མོངས་པ་མི་སྐྱེ་བ་དང་། དམན་པ་དང་མྱུར་དུ་མེད་པ་ནི་མཐོང་བའི་ཆོས་འདི་ལ་ཡང་ལྷག་པར་ཡང་བཟོད་པ་དང་དེས་པ་དང་ལྡན་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་པ་དང་། གཞན་གྱི་དོན་ལས་བརྩམས་ནས་ནི་གྲོང་གི་གནས་གང་ན་གནས་པ་དེར་ཡང་འཇིགས་པ་དང་འཇིགས་པར་འགྱུར་བ་དང་། མུ་གེའི་ཉེས་པ་རྣམས་དང་། མི་དང་མི་མ་ཡིན་པས་བྱས་པའི་གནོད་པ་མ་བྱུང་བ་རྣམས་ནི་འབྱུང་བར་མི་འགྱུར། བྱུང་བ་རྣམས་ནི་རྣམ་པར་ཞི་བར་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །

[Block 217]
མ་འོངས་པའི་ཕན་ཡོན་ནི་ངན་འགྲོར་སྐྱེ་བར་མི་འགྱུར་བ་ལ་སོགས་པ་སྔ་མ་བཞིན་དུ་རིག་པར་བྱ་སྟེ། འདི་ལྟ་སྟེ་རིགས་སུ་བསྟན་པའི་ཕན་ཡོན་དེ་དག་ཉིད་རྣམ་པ་ཐམས་ཅད་དུ་ཕན་ཡོན་དུ་བསྟན་པར་འགྱུར་རོ། །

[Block 218]
བྱང་ཆུབ་སེམས་དཔའི་ས་ལས་སེམས་བསྐྱེད་པའི་ལེའུ་རིམ་པར་ཕྱེ་བ་སྟེ་གཉིས་པའོ།། །།

[Block 219]
དེ་ལྟར་སེམས་བསྐྱེད་པ༌[^128]ཞེས་བྱ་བ་ནི། སེམས་བསྐྱེད་པའི་ལེའུ་ལས་ཇི་སྐད་བསྟན་པའོ། །ཇི་ལྟར་བསྟན་ཞེ་ན། འདི་ལ་བྱང་ཆུབ་སེམས་དཔའི་དང་པོ་སེམས༌[^129]བསྐྱེད་པ་ཞེས་བྱ་བ་ནས། སེམས་བསྐྱེད་པ་དེ་ཡང་། བྱང་ཆུབ་དེ་དང་། སེམས་ཅན་གྱི་དོན་ལ་དམིགས་ནས༌[^130]ཞེས་བྱ་བའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 220]
དེ་ལྟར་སེམས་བསྐྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བྱང་ཆུབ་སེམས་དཔའི༌[^131]སྤྱོད་པ་གང་ཞེས་བྱ་བ་ནི། སྦྱོར་བ་གང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 221]
སྤྱད་པར་བྱ་བ་རྣམས་ལ་སྤྱོད་པ་ཞེས་བྱ་བ༌[^132]ནས་སྤྱོད་པའོ། །

[Block 222]
སློབ་པ་ཞེས་བྱ་བ་ཡང་དོན་གཅིག་པས་བསླབ་བར་བྱ་བ་རྣམས་ལ་སློབ་པ་ཞེས་བྱ་བ༌[^133]ནས་སློབ་པ་ཞེས་བྱ་བ་དེའི་སྒྲས་ངོ་བོ་ཉིད་བསྒྲུབ༌[^134]པའོ། །

[Block 223]
དེའི་རྟེན་རྣམས་ཀྱིས་སྒོམ་པར་བྱེད་པས་གང་དག་སློབ་པ་ཞེས་བྱ་བའོ། །

[Block 224]
བྱེད་པ་པོའི་ལས་རྣམས་བྱ་བ་ཡིན་པས་གང་ལ་སློབ་པ་དང་ཞེས་བྱ་བའོ། །

[Block 225]
དེས་ལས་རྣམས་བྱེད་པ་ན་ཇི་ལྟ་བུའི་རྣམ་པར་གོམས་པར་བྱེད་ཅེས། ཇི་ལྟར་སློབ་པ་དང་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 226]
དེ་དག་ཐམས་ཅད་ཅེས་བྱ་བ་ནི། གསུམ་པོ་འདི་དག་ལ་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ཞེས་བྱ་བའོ། །

[Block 227]
བདག་གི་དོན་དང་གཞན་གྱི་དོན་ཞེས་བྱ་བ་ནི། བདག་དང་གཞན་གྱི་དོན་ལ་དམིགས་པ་ཉིད་ཀྱིས་བདག་གི་དོན་དང་གཞན་གྱི་དོན་ལ་བསླབ་པར་བྱ་བའོ། །

[Block 228]
བདག་དང་གཞན་གྱི་དོན་ལ་སློབ་པ་ནི་ཉོན་མོངས་པ་མེད་པའི་ཐབས་དང་། སྐྱོ་བ་མེད་པའི་ཐབས་ཀྱིས་མཐུ་ལ་བསླབ་པར་བྱའོ། །

[Block 229]
དེ་ལྟར་ཉོན་མོངས་པ་མེད་པ་དང་སྐྱོ་བ་མེད་པས་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱ་བ་དང་། བདག་གིས་སངས་རྒྱས་ཀྱི་ཆོས་ཡོངས་སུ་སྨིན་པར་བྱ་བའོ། །

[Block 230]
དེ་དག་གཉི་ག་ཡོངས་སུ་སྨིན་ན་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཅེས་བྱའོ། །

[Block 231]
འདི་རྣམས་ཀྱི་བསྡུས་པའི་དོན་དང་གོ་རིམ་ནི་དེ་ལྟར་རོ། །

[Block 232]
དེ་ལ་འབའ་ཞིག་ནི་རྣམ་པ་གཉིས་ཏེ། བདག་གི་དོན་གཞན་གྱི་དོན་དང་འབྲེལ་པ་དང་། གཞན་གྱི་དོན་བདག་གི་དོན་དང་འབྲེལ་བའོ། །

[Block 233]
ཡོངས་སུ་ཤེས་པར་བྱས་ལ་སྤང་བར་བྱའོ་ཞེས་བྱ་བ་ནི། སོ་སོར་བརྟགས་ནས་ཡོངས་སུ་གཏོང༌[^135]བའོ། །

[Block 234]
ཡོངས་སུ་ཤེས་ནས་གཏོང་བ༌[^136]ཉིད་ནི་རེ་རེའི་དོན་དུ་འགྱུར་ན་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་གི་ཕྱིར་རབ་ཏུ་སྤང་བར་བྱ་བ་ཡིན་ཞེ་ན། སྨྲས་པ། རང་གི་དོན་འབའ་ཞིག་ནི་སྤང་བར་བྱ་བ་སྟེ། ཇི་ལྟར་ཞེ་ན། བྱང་ཆུབ་སེམས་དཔའི་བྱ་བ་ལས་ཤིན་ཏུ་འདས་པའི་ཕྱིར་ཏེ། བྱང་ཆུབ་སེམས་དཔའི་བྱ་བ་ནི་གཞན་གྱི་དོན་ལ་ཞུགས་པའི་མཚན་ཉིད་ཅན་ཡིན་ལ། དེ་ལས་རབ་ཏུ་འདས་པའི་ཕྱིར་རོ། །

[Block 235]
གང་གི་ཕྱིར་གཞན་གྱི་དོན་འབའ་ཞིག་ཡོངས་སུ་ཤེས་ནས་སྤང༌[^137]བར་བྱ་བ་ཡིན་ཞེ་ན། སྨྲས་པ། རྗེས་སུ་མཐུན་པ་མ་ཡིན་པའི་ཕྱིར་ཏེ། རྗེས་སུ་མཐུན་པ་མ་ཡིན་པ་ནི་བདག་ཉིད་བྱང་ཆུབ་འཐོབ་པ་དང་འགལ་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 236]
བདག་ཉིད་བྱང་ཆུབ་ཐོབ་ན་སེམས་ཅན་གྱི་དོན་བྱེད་པས་སོ། །

[Block 237]
ལྷག་མ་རྣམས་ནི་ཞེས་བྱ་བ་ནི། འབའ་ཞིག་ལས་གང་གཞན་པའོ། །ཇི་ལྟ་བུ་ཞེ་ན། གཉི་གའི་དོན་ཏེ་དེ་ལ་ནི་བསླབ་པར་བྱ་བའོ། །

[Block 238]
ཉེས་པར་སྤྱད་པ་ཞེས་བྱ་བ་ནི། བདག་གི་བདེ་བ་འདོད་པས་སོ། །

[Block 239]
སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ༌[^138]བཤད་པ་ཞེས་བྱ་བ་ནི། ལེགས་པར་བཤད་པའི་ཕྱིར་གཟུང་བ་སྟེ། རབ་ཏུ་བསྟན་པའི་དོན་ཏོ།[^139] །གཞན་གྱིས་བཤད་པ་རྣམས་ནི་ཚོལ་བ་ལ་སོགས་པས་བདག་དང་གཞན་གྱི་དོན་དུ་ཡང༌[^140]མི་འགྱུར་བར་བསྟན་པའི་དོན་ཏེ། དེ་ནི་ཉེས་པར་བཤད་པ་ཉིད་ཀྱིས་སེར་སྣ་མེད་ན་ཡང་གཞན་གྱི་དོན་དུ་མི་འགྱུར་བས་སོ། །

[Block 240]
གང་གི་ཕྱིར་རང་གི་དོན་ལ་ཡང་བཟོད་པ་ཡང་དག་པར་བླངས་ནས་གནས་པ་ཞེས་མི་གཟུང་ཞེ་ན། བདག་ཉིད་མཐོ་རིས་འདོད་པ་ཡིན་ན་ཡང་མཐོང་བའི་ཆོས་ལ་ཡང་གཉི་གའི་དོན་བྱེད་ལ། ཕ་རོལ་དུ་ཡང་བྱེད་པས་སོ། །

[Block 241]
དེས་ན་རེ་ཞིག་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྔ་འབའ་ཞིག་གི་དབང་དུ་བྱས་ནས་རང་གི་དོན་ཞེས་བསྟན་ཏོ། །

[Block 242]
དགེ་བའི༌[^141]ཆོས་སྡུད་པའི་ཚུལ་ཁྲིམས་ཀྱི༌[^142]དབང་དུ་བྱས་ནས། འཇིག་རྟེན་གྱི་ཟང་ཟིང་གི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། འཇིག་རྟེན་གྱི་ཟང་ཟིང་གི་འབྲས་བུ་འདོད་པ་ཞེས་བྱ་བ་ནི། གཞན་པ་ཕ་རོལ་དུ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 243]
འཇིག་རྟེན་གྱི་ཟང་ཟིང་འཐོབ་པའི་རྒྱུར་ཞེས་བྱ་བ་ནི། མཐོང་བའི་ཆོས་ལའོ། །

[Block 244]
དེ་བཞིན་དུ་མཆོད་རྟེན་མཆོད་པ་ཡང་བདག་ཉིད་ཀྱི་དོན་འབའ་ཞིག་ཡིན་ལ་གཞན་གྱི་དོན་མེད་ཅེ་ན། མཆོད་རྟེན་མཆོད་པས་ཀྱང་རེས་འགའ་གཉི་གའི་དོན་དུ་ཡང་འགྱུར་ཏེ། འཇིག་རྟེན་གྱི་ཟང་ཟིང་གི་འབྲས་བུ་འདོད་པ་དང་། འཇིག་རྟེན་གྱི་ཟང་ཟིང་ལ་ལྟོས་པ་མེད་པར་དགེ་བའི་ཆོས་སྡུད་པ་དང་། བདག་ཉིད་ཀྱི་སངས་རྒྱས་ཀྱི་ཆོས་ཡོངས་སུ་སྨིན་པར་ཡང་དག་པར་གནས་པ་ནི་གཉི་གའི་དོན་ཉིད་དུ་ཡང་འགྱུར་རོ། །

[Block 245]
རྙེད་པ་འདོད་པ་ཞེས་བྱ་བ་ནི་གཞན་དག་ལས༌[^143]མཆོག་ཏུ་རྙེད་པ་འདོད་པའོ། །

[Block 246]
རྙེད་པའི་རྒྱུ་ཞེས་བྱ་བ་ནི། མཐོང་བ་ལ་དོན་མེད་པའི་རྙེད་པ་སྒྲུབ་པའོ། །

[Block 247]
གཞན་དག་གི་སྤྲོ་བ་སྐྱེད་པ་ཞེས་བྱ་བ་དང་། ཡང་དག་པ་མ་ཡིན་པའི་ཡོན་ཏན་སྣ་ཚོགས་སྟོན་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་ཀྱིས་ནི་གཞན་གྱི་དོན་མེད་པར་ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 248]
གལ་ཏེ་གཞན་རྣམས་ཡང་དག་པར་མགུ་བར་འགྱུར༌[^144]ན་གཞན་གྱི་དོན་ཡང་ཡོད་པར་འགྱུར་རོ་ཞེ་ན། དེ་ནི་མེད་པར་བསྟན་པ་ཡིན་ཏེ། དེ་ལྟར་ན་དགེ་བའི་ཆོས་སྡུད་པ་ཉིད་ཀྱི་ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 249]
བདག་ལ་བསྙེན་བཀུར་བྱ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སེམས་ཅན་གྱི་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 250]
བསྙེན་བཀུར་བྱ་བ་བདག་གིར་བྱ་བ་འདོད་པས་ཞེས་བྱ་བ་ནི་བསམ་པ་ཉིད་ཀྱིས་སོ། །
--- END BLOCKS ---
