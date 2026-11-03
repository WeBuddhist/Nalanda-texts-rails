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
དེ་རྣམ་པར་གཅད་པར་གོ་རིམས་བཞིན་དུ་རྗེས་སུ་དཔག་པར་བྱ་བ་ལ་ཡོད་པ་དང་། ངེས་པར་གཟུང་བ༌[^110]སྨོས་ཏེ། ཡུལ་ཁྱད་པར་ཅན་དུ་ངེས་པར་གཟུང་བ༌[^111]ནི་འདོད་པའི་དོན་རྟོགས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 142]
དེ་ལྟ་མ་ཡིན་ན་བཤད་མ་ཐག་པའི་དོན་རྟོགས་པར་མི་འགྱུར་རོ། །

[Block 143]
བྱེ་བྲག༌[^112]ལ་སོགས་པ་ནི་རྗེས་སུ་དཔག་པར་བྱ་བ་ཁོ་ན་ལ་ཡོད་པ་ཐུན་མོང་མ་ཡིན་པ་མ་ངེས་པ་ཡང་དངོས་སུ་གཏན་ཚིགས་ཡིན་པར་ཁས་ལེན་ཏེ། དཔེར་ན་གསོན་པོའི་ལུས་ནི་བདག་དང་བཅས་པ་ཡིན་ཏེ། སྲོག་ལ་སོགས་པ་དང་ལྡན་པའི་ཕྱིར་རོ༌[^113]ཞེས་ཟེར་བ་ལྟ་བུའོ། །

[Block 144]
དེ་བཟློག་པའི་ཕྱིར་མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་བརྗོད་དོ། །

[Block 145]
ཕྱོགས་ཀྱི་མཚན་ཉིད་འདི་རྣམ་པ་གཉི་ག་ཡང་ཧ་ཅང་ཁྱབ་ཆེ་བའི༌[^114]ཉེས་པ་ཡོད་ལ། དེ་དག་ལ་གཏན་ཚིགས་དང་དཔེ་མ་གྲུབ་པ་སྨྲ་བ་ཡང་ཡོད་པའི་ཕྱིར་ཏེ། དེའི་ཕྱིར་ཡང་ཕྱོགས་ཀྱི་མཚན་ཉིད་བསྟན་པ། [^115]གྲངས་ཅན་པ་རྣམས་ནི་རྒོལ་བ་དང་ཕྱིར་རྒོལ་བ་དག་ལ་མ་གྲུབ་པ་ཡང་བསྒྲུབ་པར་བྱ་བ་ཉིད་དུ་སྟོན་ཏེ། དཔེར་ན་མིག་ལ་སོགས་པ་ནི་གཞན་གྱི་དོན་ཡིན་ནོ་ཞེས་ཟེར་བ་ལྟ་བུའོ། །

[Block 146]
གཞན་གྱི་དོན་ནི་སྤྱི་ཡིན་པས་དེའི་ཕྱིར་རང་གི་ངོ་བོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 147]
ཁོ་ན་ཞེས་བྱ་བ་ནི་ཧ་ཅང་ཡང་ཁྱབ་ཆེས་པའི་ཉེས་པ་བསལ་བའི་ཕྱིར་རོ། །

[Block 148]
གྲངས་ཅན་པ་ལ་སོགས་པ་ནི་རྒོལ་བ་མི་འདོད་ཀྱང་བླ་སྟེ། བསྟན་བཅོས་བྱེད་པར༌[^116]འདོད་པ་ཐམས་ཅད་བསྒྲུབ་པར་བྱ་བ་ཁོ་ན་ཡིན་ནོ་ཞེས་བྱ་བར་རྟོགས་སོ། །

[Block 149]
[^117]

[Block 150]
དེའི་སྒོ་ནས་བྱས་པ་ཉིད་ལ་སོགས་པ་ཡང་དག་པའི་སྒྲུབ་པ་ལ་ཡང་འགལ་བ་རྗོད་པར༌[^118]བྱེད་དེ། དེ་དང་འདྲ་བར་ཆོས་ཅན་སྒྲ་ལ་ནམ་མཁའི་ཡོན་ཏན་ཡང་མེད་པར་བསྒྲུབ་པའི༌[^119]ཕྱིར། བྱེ་བྲག་པ༌[^120]ལ་སོགས་པའི་གཏན་ཚིགས་ནི་འགལ་བ་ཡིན་ནོ་ཞེས་ཟེར་བ་ལྟ་བུ་སྟེ། དེའི་ཕྱིར་བདག་ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 151]
གྲངས་ཅན་པ་ལ་སོགས་པ་ན་རེ་ཚིག་ཏུ་སྨྲས་པ་ཁོ་ན་བསྒྲུབ་པར་བྱ་བ་ཡིན་གྱི་མ་སྨྲས་པ་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་ཞེས་གྲགས་ཏེ།[^121] དེའི་ཕྱིར་འདོད་པ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 152 [HEADING]]
### འགལ་བ། ^5-4-0

[Block 153]
རྒྱལ་དཔོག་པ་རྣམས་ནི་རང་རིག་པའི་མངོན་སུམ་དུ་རབ་ཏུ་གྲུབ་པ་བློ་དང་བདེ་བ་ལ་སོགས་པ་ཡང་མངོན་སུམ་མ་ཡིན་པ་དེ༌[^122]ཉིད་དུ་རབ་ཏུ་ཤེས་ཏེ། དེ་དག་གིས༌[^123]དམ་བཅའ་བ་ནི་སྒྲ་མཉན་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་དུ་དམ་བཅའ་བ་དེ་བཞིན་དུ། མངོན་སུམ་གྱི༌[^124]གནོད་པ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར། འགལ་བ་དང་པོ་བརྗོད་དོ། །

[Block 154]
དེ་དག་ཉིད་སྒྲ་རྟག་པ༌[^125]ཉིད་སྒྲ༌[^126]ཤེས་ལ། གྲངས་ཅན་པ་ལ་སོགས་པ་གསལ་བར་སྨྲ་བ་རྣམས་ཀྱང་རྟག་པ་ཉིད་དུ་གསལ་བ་ཁོ་ནར་ཁས་ལེན་པས། དེའི་ཕྱིར་རྗེས་སུ་དཔག་པས་གནོད་པ་བསལ་ཏོ། །

[Block 155]
བརྡ་སྤྲོད་པ༌[^127]ཁ་ཅིག་སྒྲ་བཟང་པོ་ཁོ་ན་རྗོད་པར་བྱེད་པ་ཡིན་གྱི་མི་བཟང་བ་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་བ་ནི། དངོས་པོ་ཐམས་ཅད་སྒྲ༌[^128]བརྗོད་པར་བྱ་བ་ཉིད་དུ་རུང་བར་འདོད་པ་ཙམ་གྱི་རྗེས་སུ་བྱེད་པ་སྐྱེ་བོ་གནག་རྫི་མོ༌[^129]ཡན་ཆད་ལ་གྲགས་པ་འདོད་པར༌[^130]བྱེད་པ་ཡིན་ཏེ།[^131] དེའི་ཕྱིར་གྲགས་པས་གསལ་བ༌[^132]བསལ་ཏོ། །

[Block 156]
འཇིག་རྟེན་རྒྱང་པན་པ༌[^133]རྣམས་ནི་གཞན་དག་ལ་རང་གི་བརྗོད་པར༌[^134]འདོད་པའི་དོན་ལྐོག་ཏུ་གྱུར་པ་ཚིག་རྟགས་དེ་མེད་ན་མི༌[^135]འབྱུང་བའི་སྒོ་ནས་རྗེས་སུ་དཔོག་པར་བྱེད་ཀྱང་། རྗེས་སུ་དཔག་པ་ཚད་མ་མ་ཡིན་ནོ་ཞེས་བྱ་བར་རབ་ཏུ་ཤེས་ཏེ། དེའི་ཕྱིར་རང་གི་ཚིག་དང་འགལ་བ་བརྗོད་དོ། །

[Block 157 [HEADING]]
### གཏན་ཚིགས་ལྟར་སྣང་བ། ^5-5-0

[Block 158]
རིགས་པ་ཅན་རྣམས་ནི་གཏན་ཚིགས་ལྟར་སྣང་བ་རྣམས་ཀྱི་མཚན་ཉིད་ནི། འཁྲུལ་པ་དང་བཅས་པ་དང་། འགལ་བ་དང་། སྐབས་དང་། མཚུངས་པ་དང་། བསྒྲུབ་པར་བྱ་བ་དང་། མཚུངས་པ་དང་། དུས་ལས་འདས་པ་ནི་གཏན་ཚིགས་ལྟར་སྣང་བ་དག་ཡིན་ནོ་ཞེས་གཞན་དུ་འཆད་པར་བྱེད་དེ། དེ་ལ་འཁྲུལ་པ་དང་བཅས་པ་མ་ངེས་པ་ཡིན་ཏེ། དཔེར་ན་སྒྲ་ནི་རྟག་པ་སྟེ། ལུས་ཅན་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 159]
གྲུབ་པའི་མཐའ་ཁས་བླངས་པས་དེ་དང་འགལ་བར་བྱེད་པ་ནི་འགལ་བ་སྟེ། དཔེར་ན་བྱེ་བྲག་ནི༌[^136]རྡུལ་ཕྲ་རབ་དག་ནི་ལུས་ཅན་མ་ཡིན་པའི་ཕྱིར་རྩོམ་པར་བྱེད་པ་མ་ཡིན༌[^137]ཞེས་ཟེར་བ་ལྟ་བུའོ། །

[Block 160]
གང་གི་ཕྱིར་སྐབས་བསམ་པ༌[^138]དེ་གཏན་ལ་དབབ་པའི་ཕྱིར། བསྟན་པ་ནི་སྐབས་དང་མཚུངས་པ་སྟེ། དཔེར་ན་བདག་ནི་རྟག་པ་སྟེ་ལུས་ལས་གཞན་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 161]
བསྒྲུབ་པར་བྱ་བ་དང་ཁྱད་པར་མེད་པ༌[^139]བསྒྲུབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་བསྒྲུབ་པར་བྱ་བ་དང་མཚུངས་ཏེ། དཔེར་ན་སྒྲ་ནི་རྟག་པ་སྟེ། ལུས་ཅན་མ་ཡིན་པའི་ཕྱིར་བློ་ལྟ་བུ་ཞེས་བྱ་བ་ལྟ་བུ༌[^140]དང་། གཞན་དག་ན་རེ་རྫས་ཡིན་ཏེ། ལུས་ལས་འོང་བ་དང་ལྡན་པའི་ཕྱིར་རོ་ཞེས་དཔེར་རྗོད་པར༌[^141]བྱེད་པ་ལྟ་བུའོ། །

[Block 162]
དུས་འདས་ནས་བསྟན་པ་ནི་དུས་ལས་འདས་པ་སྟེ། དཔེར་ན་སྒྲ་ནི་མི་རྟག་པ་སྟེ་བུམ་པ་བཞིན་ནོ་ཞེས་སྨྲས་ནས་དྲིས་པ་དང་བྱས་པའི་ཕྱིར་རོ་ཞེས་གཏན་ཚིགས་སྨྲས་པ༌[^142]ལྟ་བུའོ་ཞེས་ཟེར་རོ། །

[Block 163]
བྱེ་བྲག་པ་རྣམས་ན་རེ་སྟོན་པ་མ་ཡིན་པ་ནི་རབ་ཏུ་མ་གྲུབ་པ་དང་། མེད་པ་དང་། ཐེ་ཚོམ་ཟ་བའོ་ཞེས་ཟེར་ཏེ། གང་ལ་རྟགས་དང་རྟགས་ཅན་དག་འབྲེལ་པར་མ་གྲུབ་པ་དེ་ལ་མ་གྲུབ་པ་ཡིན་ནོ། །

[Block 164]
འབྲེལ་པ་མེད་པ་ནི་མེད་པ་སྟེ། དཔེར་ན་རྭ་ཅན་ཡིན་པའི་ཕྱིར་རྟའོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 165]
རྭ་ཅན་ཡིན་པའི་ཕྱིར་བ་ལང་ངོ་ཞེས་བྱ་བ་ལྟ་བུ་ནི་ཐེ་ཚོམ་ཟ་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 166]
དེ་དག་དགག་པའི་ཕྱིར་དང་གཞན་གྱིས་རབ་ཏུ་སྦྱར་བའི་གཏན་ཚིགས་རྣམས་ཀྱི་མ་གྲུབ་པ་ཉིད་ལ་སོགས་པའི་སྐྱོན་བརྗོད་པའི༌[^143]ཕྱིར་གཏན་ཚིགས་ལྟར་སྣང་བ་དག་བསྟན་ཏོ། །

[Block 167]
ཤིང་དག་ལ་སེམས་ཡོད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ནམ་མཁའི་གོས་ཅན་རྣམས་ཀྱིས་དམ་འཆའ་བ་ཡིན་ནོ། །

[Block 168]
བདེ་བ་ལ་སོགས་པ་ལ་སེམས་མེད་དོ་ཞེས་བྱ་བ་ནི་གྲངས་ཅན་པ་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 169]
བདག་ནི་ཐམས་ཅད་ལ༌[^144]ཡོད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རིགས་པ་ཅན་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 170]
སྒྲ་ནི་རྟག་པ་ཡིན་ནོ༌[^145]ཞེས་བྱ་བ་ནི་དཔྱོད་པ༌[^146]པ་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 171]
སྐྱེས་བུ་ཐམས་ཅད་ཐམས་ཅད་མཁྱེན་པ་ཉིད་མ་ཡིན་པར་དམ་འཆའ་བ་ནི་རྒྱལ་དཔོག་པ་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 172]
རང་གི་སྡེ་པ་ཁ་ཅིག་ཀྱང་འདོད་པ་ལ་གནོད་པ་བྱེད་པ་ཞེས་བྱ་བ་འགལ་བ་གཞན་ཡང་ཡོད་དོ་ཞེས་རྗོད་པར་བྱེད་དོ། །

[Block 173]
[^147]དེ་དགག་པའི་ཕྱིར་འདོད་པ་ལ་གནོད་པ་བྱེད་པ་འགལ་བ་གསུམ་པ་མ་ཡིན་ནམ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 174]
རིགས་པ་ཅན་རྣམས་ན་རེ། གསོན་པོའི་ལུས་ནི་བདག་དང་བཅས་པ་ཡིན་ཏེ། སྲོག་ལ་སོགས་པ་དང་ལྡན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 175]
རང་གི་སྡེ་པ་ཁ་ཅིག་ནི་དངོས་པོའི་སྟོབས་ཀྱིས་ཞུགས་པའི་རྗེས་སུ་དཔག་པ་ལ་ཡང་འགལ་བ་མི་འཁྲུལ་པ་ཅན་ཞེས་བྱ་བ་མ་ངེས་པའི་གཏན་ཚིགས་ཡོད་དོ་ཞེས་བརྗོད་དེ། དེ་ལ་དཔེར་བརྗོད་པ༌[^148]ནི་དཔེར་ན་སྒྲ་མི་རྟག་པ་སྟེ་བྱས་པའི་ཕྱིར་བུམ་པ་ལྟ་བུའོ་ཞེས་བྱ་བ་ལ་ཡང༌[^149]གང་གི་ཚེ་གཞན་ཞིག་གིས་བརྒལ་ཏེ། སྒྲ་ནི་རྟག་པ་སྟེ་མཉན་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་སྒྲ་ཉིད་ལྟ་བུའོ་ཞེས་སྨྲས་པ་དེའི་ཚེ་སྦྱོར་བ་སྔ་མ་མ་ངེས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ་ཞེས་གྲགས་ཏེ།[^150] དེ་དགག་པའི་ཕྱིར་འགལ་བ་མི་འཁྲུལ་བ་ཅན་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 176]
པེའི་ལུ་ཀ་ན་རེ་སྤྱི་ནི་ཐམས་ཅད་ན༌[^151]ཡོད་པ་ཡིན་ཏེ། གསལ་བ་དག་དང་དེ་དག་གི༌[^152]སྟོང་བ་ཐམས་ཅད་ན་ཡོད་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 177]
པེའི་ཐ་ར་ན་རེ་དེ་ནི་གསལ་བ་ཐམས་ཅད་ན་ཡོད་པ་ཡིན་གྱི།[^153] བར་གྱི་ཡུལ་ལ་ཡོད་པ་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 178 [HEADING]]
### དཔེ་ལྟར་སྣང་བ། ^5-6-0

[Block 179]
རིགས་པ་ཅན་ལ་སོགས་པ་ནི་མཚན་ཉིད་གསུམ་པའི་གཏན་ཚིགས་ལས་མ་གཏོགས་པ་དཔེ་ཞེས་བྱ་བ་སྒྲུབ་པའི་ཡན་ལག་ཡོད་དོ་ཞེས་ཟེར་ཏེ། དེ་བསལ་བའི་ཕྱིར། མཚན་ཉིད་གསུམ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 180]
གཞན་གྱིས༌[^154]རབ་ཏུ་སྦྱར་བའི་དཔེ་ཁ་ཅིག་ཀྱང་སྐྱོན་ཅན་ཉིད་དུ་བརྗོད་པའི་ཕྱིར། དཔེ་ལྟར་སྣང་བ་ཉེ་བར་བཀོད་དེ།[^155] བྱེ་བྲག་པ་ལ་སོགས་པའི་ལྟར་ན་རྡུལ་ཕྲ་རབ་རྣམས་ནི་རྟག་པ་ཡང་ཡིན་ལ་ལུས་ཅན་ཡང་ཡིན་ཏེ། ལུས་ཅན་ནི་རྫས་ཐམས་ཅད་ན་ཡོད་པ་མ་ཡིན་པའི་མཚན་ཉིད་ཡིན་ནོ། །
--- END BLOCKS ---
