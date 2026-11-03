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
[Block 876]
དེ་ལ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དབང་དེ་ལའོ། །

[Block 877]
གཉི་ག་ཞེས་བྱ་བ་ནི་དེ་ཁོ་ན་ཉིད་མཐོང་བ་དང་། མ་མཐོང་བ་དག་གོ། །

[Block 878]
དེ་ཕྱིར་ཞེས་བྱ་བ་ནི་རྒྱུ་དེས་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ་འདི་ལྟར་གཞན་གྱི་དབང་ལ་ཀུན་ཏུ་བརྟགས་པ་ནི་མེད་ལ། ཡོངས་སུ་གྲུབ་པ་ནི་ཡོད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 879 [HEADING]]
### སྔར་བསྟན་པའི་ཚིག་གི་དོན་ཚིག་གི་ལྷག་མས་སྟོན་པ། ^2-22-0

[Block 880 [HEADING]]
#### ཤིན་ཏུ་རྣམ་པར་དག་པའི་བློ་མངའ་བ། ^2-22-1-0

[Block 881]
བྱིས་པ་ཕྱིན་ཅི་ལོག་ཏུ་འཛིན་པ་ལ་སྔར་བསྟན་པའི་ཚིག་གི་དོན་ཚིག་གི༌[^583]ལྷག་མས་ཡང་དག་པར་སྟོན་ཏེ། དེ་ལ་ཀུན་ཏུ་སྤྱོད་པ་གཉིས་མི་མངའ་བ་ཞེས་བྱ་བ་ནི་གཉིས་སུ་སྤྱོད་པ་འདི་ལ་མི་མངའ་བས་དེ་ནི་ཀུན་དུ་སྤྱོད་པ་འདི་ལ༌[^584]མི་མངའ་བ་སྟེ། ཇི་ལྟར་ཉན་ཐོས་དང་། རང་སངས་རྒྱས་རྣམས་ཀྱི་ཤེས་པ་ནི་བསྒྲིབས་པ་དང་མ་བསྒྲིབས་པ་ཅན་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 882]
ཡོད་པ་དང་མེད་པ་གཉིས་སུ་མེད་པའི་མཚན་ཉིད་མཆོག་ཏུ་རྣམ་པར་དག་པ་སྟེ། རྣམ་པར་དག་པའི་དེ་བཞིན་ཉིད་དེ་ནི་མཚན་ཉིད་མེད་པའི་ཆོས་ཏེ། གང་གི་ཕྱིར་རེ་ཞིག་འདི་ལ་དངོས་པོའི་མཚན་ཉིད་ནི་མེད་དེ། འདི་ལྟར་ཆོས་ཐམས་ཅད་མེད་པས་སོ། །

[Block 883]
མེད་པའི་མཚན་ཉིད་ཀྱང་མ་ཡིན་ཏེ། དངོས་པོའི་རང་གི་མཚན་ཉིད་ལ་གནས་པས་སོ། །

[Block 884]
མཚན་ཉིད་མེད་པའི་ཆོས་མཆོག་ཏུ་རྣམ་པར་དག་པ་རྟོགས་པས་ན་དེ་ནི་དེ་བཞིན་ཉིད་མཆོག་ཏུ་རྣམ་པར་དག་པར་གཤེགས་པར་མཛད་པའི་ཡོན་ཏན་ཞེས་བྱ་བ་སྟེ། མཆོག་ཉིད་དུ་རྟོགས་པས༌[^585]ན་མཆོག་ཏུ་གཤེགས་པར་མཛད་པ་སྟེ། གཤེགས་པ་ཞེས་བྱ་བ་ནི་འགྲོ་བ་ཞེས་བྱ་བའི་དོན་ཡིན་པའི་ཕྱིར་འགྲོ་བའི་ཐ་ཚིག་གོ། །

[Block 885]
སངས་རྒྱས་ཀྱི་མཛད་པ་ལྷུན་གྱིས་གྲུབ་པ་རྒྱུན་མི་གཅོད་པར་གནས་པའི་ཡོན་ཏན་ཞེས་བྱ་བ་ལ། སངས་རྒྱས་ཀྱི༌[^586]མཛད་པ་ལ་དམིགས་ནས་གནས་པ་སྟེ། དེས་རྣམ་པར་གནས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 886]
སྒྲིབ་པ་ཐམས་ཅད་ཀྱི་གཉེན་པོ་བསྒོམས་པའི་ཡོན་ཏན་དང་ཞེས་བྱ་བ་ནི་སྒྲིབ་པ་ཐམས་ཅད་ཀྱི་གཉེན་པོ་འདི་ལྟར་དུས་ཐམས་ཅད་དུ་བསྒོམ་པའི༌[^587]བློའོ། །

[Block 887]
འཇིག་རྟེན་དུ་སྐྱེས་ཀྱང་འཇིག་རྟེན་གྱི་ཆོས་ཀྱིས་མི་འཕྲོགས་པ་ཞེས་བྱ་བ་ལ། དེ་འཇིག་རྟེན་གྱི་སྤྱོད་ཡུལ་དུ་འཇིག་རྟེན་དུ་སྐྱེས་པ༌[^588]ཡིན་ན་ཡང་རྙེད་པ་ལ་སོགས་པའི་འཇིག་རྟེན་པའི་ཆོས་ཀྱིས་འདི་ལྟར་མི་གོས་པའོ། །

[Block 888]
ཆོས་རྣམ་པར་གཞག་པའི་ཡོན་ཏན་ཞེས་བྱ་བ་ནི་ཚད་མེད་པ་ཉིད་དང་། བསམ་གྱིས་མི་ཁྱབ་པ་ཉིད་ཀྱི་མདོ་སྡེ་ལ་སོགས་པའི་ཆོས་བྱིས་བས་རྟོགས་པར་དཀའ་བ་རྣམས་མཁྱེན་པས་ཤིན་ཏུ་རྣམ་པར་དག་པའི་བློ་མངའ་བ་སྟེ། ཤིན་ཏུ་རྣམ་པར་དག་པའི་བློ་ཞེས་བྱ་བའི་ཐ༌[^589]ཚིག་འདི་དག་ནི་ཚིག་སོ་སོ་ཐམས་ཅད་ལ་སྦྲེལ་བར་བྱའོ། །

[Block 889]
ཕྱི་མ་ལ་ཆོས་འབྱུང་བ་མཁྱེན་པའི་ཡོན་ཏན་ཞེས་བྱ་བ༌[^590]ནི་ཡེ་ཤེས་ཀྱིས་མ་འོངས་པ་ན་ཆོས་འདི་ལྟ་བུ་འབྱུང་ངོ་ཞེས་བྱ་བ་མཁྱེན་པའི་ཐ་ཚིག་གོ། །

[Block 890]
སྐུ་དཔག་ཏུ་མེད་པས་སེམས་ཅན་འདུལ་བ་སྦྱོར་བའི་ཡོན་ཏན་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་སེམས་དཔའ་ལུས་དཔག་ཏུ་མེད་པ་གང་གིས་སེམས་ཅན་རྣམས་འདུལ་བར་མཛད་པ་སྟེ། དེས་སངས་རྒྱས་ལས༌[^591]བདག་དང་གཞན་མཉམ་པ་ཉིད་དུ་ཤེས་པ་འཐོབ་པ་དང་། ཡེ་ཤེས་མནོས་པ་ཉིད་ཡིན་པའི་ཕྱིར་སངས་རྒྱས་ཉིད་ཀྱིས༌[^592]གདུལ་བྱ་རྣམས་ལ་མཛད་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 891]
ཆོས་ཀྱི་སྐུ་མཉམ་པ་ལ་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་གྲུབ་པའི་ཡོན་ཏན་ཞེས་བྱ་བ་ནི་གཉིས་སུ་མེད་པའི་ཆོས༌[^593]ཀྱི་སྐུ་ནི་ཆོས་ཀྱི་སྐུ་མཉམ་པ་སྟེ། དེ་ལྟ་བས་ན་འདིར་གཉིས་སུ་མེད་པའི་སྐུ་ཤིན་ཏུ་རྣམ་པར་དག་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐོབ་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 892]
དེ་བཞིན་གཤེགས་པ་ཐ་མི་དད་པ་རྣམ་པར་ཐར་པར་མཛད་པའི་ཡེ་ཤེས་ཀྱིས༌[^594]མཐར་ཕྱིན་པ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པ་ཐ་མི་དད་པ་ལ་མོས་པར་མཛད་པའི་ཡེ་ཤེས་ཀྱིས་མཐར་ཕྱིན་པ་ཞེས་བྱ་བ༌[^595]སྟེ། འདིར་རྣམ་པར་ཐར་པ་ནི་མོས་པའོ། །

[Block 893]
སངས་རྒྱས་ཀྱི་སྐུ་གསུམ་གྱི་ཡུལ་ཡོངས་སུ༌[^596]ཆད་པའི་ཡོན་ཏན་ཞེས་བྱ་བ་ལ། འདི་ལྟར་རེ་ཞིག་ཆོས་ཀྱི་སྐུའི༌[^597]ཡུལ་ནི་འདི་དག་གོ་ཞེས་ཡོངས་སུ་བཅད་པར་མི་ནུས་སོ། །

[Block 894]
དེ་བཞིན་དུ་ལོངས་སྤྱོད་རྫོགས་པ་དང་། སྤྲུལ་པའི་སྐུ་ཡང་འཇིག་རྟེན་ཁམས་འདི་སྙེད་དོ་ཞེས་བཅད་པར་མི་ནུས་སོ། །

[Block 895]
ཆོས་ཀྱི་དབྱིངས་ཀྱི་མཆོག་ཅེས་བྱ་བ་ནི་གང་འདིར་རྣམ་པར་དག་པའི་ཆོས་ཀྱི་དབྱངས༌[^598]དེ་ནི་མཆོག་ཡིན་པས་ཆོས་ཀྱི་དབྱིངས་དེ་ཡང་མཆོག་ཡིན་ནོ། །

[Block 896]
ནམ་མཁའི་ཁམས་ཀྱི་མཐས༌[^599]གཏུགས་པ་ཞེས་བྱ་བ་ནི་ནམ་མཁའ་ལྟར་སངས་རྒྱས༌[^600]ཡེ་ཤེས་མི་ཟད་པའི་ཕྱིར་ཤིན་ཏུ་རྣམ་པར་དག་པའི་བློ་མངའ་བ་ཞེས་བྱའོ། །

[Block 897 [HEADING]]
#### དོན་གྱི་དབང་དུ་བྱ་བ། ^2-22-2-0

[Block 898]
ཡང་དོན་གྱི་དབང་དུ་བྱ་བའི་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པ་དང་བདེ་བར་བྱ་བའི་ལྷག་པའི་བསམ་པ་ཞེས་བྱ་བ་གཞན་གྱི་དོན་འདི་ནི་ལས་ཀྱི་ཚིག་ལྷག་མ་བཅུ་དྲུག་གིས་བསྟན་ཏེ། དེ་ལ་བདེ་བར་བྱ་བའི་ལྷག་པའི་བསམ་པའི་ལས་ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ལ་འཛུད་པ་ཞེས་བྱ་བ་སྟེ། འདི་ལྟར་སེམས་ཅན་དེ་དག་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ལ་བཙུད་པར་གྱུར་པས་དེས་ཀྱང་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་སྦྱོར་བས༌[^601]མར་མེ་གཅིག་ལས་མར་མེ་སྟོང་དུ་གྱུར་པ་ལྟར་བདེ་བར་བྱ་བའི་ལྷག་པའི་བསམ་པ་ཡང་དག་པར་བསྟན་པར་འགྱུར་རོ། །

[Block 899]
དེ་བཞིན་དུ་ཚིག་ཐམས་ཅད་ལ་ཡང་ཕན་པ་དང་བདེ་བར་བྱ་བའི་ལྷག་པའི་བསམ་པ་ལ༌[^602]སྦྱར་བར་བྱའོ། །

[Block 900]
བདག་ཅི་རི༌[^603]ཞེས་ཡོངས་སུ་ཤེས་པ་དང་ཞེས་བྱ་བ་ནི་ཕན་པ་དང་བདེ་བར་བྱ་བའི་ལྷག་པའི་བསམ་པ་ཡོད་ལ། ཡང་ཕྱིན་ཅི་ལོག་ཀྱང་ཡོད་ན་ནི་འདི་ལྟར་ལ་ལ་ཕན་པ་དང་བདེ་བར་བྱ་བའི་ལྷག་པའི་བསམ་པ་ཉིད་ཀྱིས་མྱོས་པར་འགྱུར་བའི་བཏུང་བ་ལ་སོགས་པ་ལ་ངེས་པར་སྦྱོར་བར་བྱེད་དོ། །

[Block 901]
གལ་ཏེ་དེས་བདག་ཉིད་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡོངས་སུ་ཤེས་པ་ཡིན་ན། དེ་དང་རྗེས་སུ་མཐུན་པ་ལ་སེམས་ཅན་རྣམས་ལ་ཡང་ཉེ་བར་སྟོན་པར་བྱེད་དོ། །

[Block 902]
ང་རྒྱལ་དང་ལྡན་པར་གྱུར་པ་ནི་མི་ཤེས་བཞིན་དུ་འདི་ལྟར་ཕན་བཏགས་པའི༌[^604]སེམས་ཀྱིས་ཕན་པ་མ་ཡིན་པ༌[^605]ལ་སྦྱོར་བར༌[^606]བྱེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 903]
ང་རྒྱལ་བཅོམ་པ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ང་རྒྱལ་བཅོམ་པའི་སེམས་ཀྱིས་གསོལ་བ་འདེབས་པ་ལ་སྡོད་པ་མེད་པར་ཆོས་སྟོན་པ་ཞེས་བྱ་བའི་ཐ༌[^607]ཚིག་གོ། །

[Block 904]
ལྷག་པའི་བསམ་པ་བརྟན་པ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་སེམས་ཅན་ཕྱིན་ཅི་ལོག་ཏུ་སྒྲུབ་པ་ལ་སེམས་བརྟན་པ་ཉིད་ཀྱི་ཕྱིར་ཁྲོས་པས༌[^608]ཕན་པའི་ལྷག་པའི་བསམ་པ་མི་འདོར་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 905]
བཅོས་མ་མ་ཡིན་པར་བྱམས་པ་ཞེས་བྱ་བ་ནི་གང་རྙེད་པའི་རྒྱུས་སེམས་ཅན་རྣམས་ལ་ཕན་པ་དང་བདེ་བར༌[^609]མི་བྱེད་པ་དང་ལྷག་པའི་བསམ་པ་དང་ལྡན་པ་དང་། ཕན་པ་བྱེད་པ་ཡིན་ནོ་ཞེས་ཇི་ལྟར་ཤེས་པར་གྱུར༌[^610]ཞེས་བྱ་བ་མ་ཡིན་པའོ། །

[Block 906]
དེ་དང་མཐུན་པའི་ལུས་དང་ངག་གི་ལས་དག་སྟེ། དེ་ལ་ཚིག་ཅུང་ཟད་ཀྱིས་སྔོན་དུ་གསོང་པོར་སྨྲ་བ་ནི་ངག་གི་ལས་སོ། །

[Block 907]
འདིར་བདེ་བ་ཉིད་རྒྱུན་མི་གཅོད་པའི་སྙིང་རྗེ་ཆེན་པོ་དང་། བཞིན་འཛུམ་པ་ནི༌[^611]ལུས་ཀྱི༌[^612]ལས་ཏེ། དེ་ལ་ཚིག་ཅུང་ཟད་ཅེས་བྱ་བ་ནི་འདི་ལྟར་ཆོས་ཀྱི་གཏམ་བྱེད་པའོ། །

[Block 908]
སྙིང་རྗེ་ཆེན་པོ་ཡོངས་སུ་མ་ཆད་པ་ནི་སྡུག་བསྔལ༌[^613]གྱིས་སྡུག་བསྔལ་བ་དང་བདེ་བ་རྣམས་ནི་འགྱུར་བའི་སྡུག་བསྔལ་དང་། སྡུག་བསྔལ་ཡང་མ་ཡིན་བདེ་བ་ཡང་མ་ཡིན་པ་ནི་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་ཉིད་ཀྱིས་སྡུག་བསྔལ་བ་ལ་བདེ་བ་དང་སྡུག་བསྔལ་གཉིས་སུ་མེད་པའོ། །

[Block 909]
མི་ཞུམ་པའི་ལས་ནི་བདག་གིས་སངས་རྒྱས་ཉིད་བསྒྲུབ་པར༌[^614]ག་ལ་ནུས་ཞེས་བྱ་བའི་རྣམ་པས་བདག་ཉིད་ལ་སྤྱོད་པ་མེད་པའོ། །

[Block 910]
ཡིད་ཡོངས་སུ་མི་སྐྱོ་བ་ཞེས་བྱ་བ་ནི་གང་སངས་རྒྱས་ཉིད་བསྒྲུབ་པ༌[^615]ལ་སྐྱེ་བ༌[^616]མེད་པའོ། །

[Block 911]
ཐོས་པ་དང་དོན་གྱིས་ངོམས་མི་མྱོང་བ་ཞེས་བྱ་བ་ནི་གང་ཐོས་པ་མང་པོ་ཉིད་ཡིན་ན་ཡང་བཏང་སྙོམས་དང་བཅས་པར་མི་འགྱུར་བའོ། །

[Block 912]
སྤྱོད་ལམ་ཐམས་ཅད་དུ་བྱང་ཆུབ་ཀྱི་སེམས་ཡོངས་སུ་སྦྱོང་བར་བྱེད་པ་དང་ཞེས་བྱ་བའི་ཚིག་གི་དོན་ནི་སྤྱོད་ལམ་ཡོངས་སུ་དག་པའི་མདོ༌[^617]བཞིན་ནོ། །

[Block 913]
ཁྱད་པར་དུ་འགྲོ་བའི་ལས་ཞེས་བྱ་བ་ལ། ཕན་པའི་ལྷག་པའི་བསམ་པ་འཕེལ་བར་བྱེད་པའི་རྒྱུར་གྱུར་པ་ཡོངས་སུ་རྫོགས་པ་སྦྱོར་བའི་ལས་དྲུག་པོ་འདི་དག་མང་དུ་བྱས་པས་རྫོགས་པར་འགྱུར་རོ། །

[Block 914]
གུས་པར་བྱས་ཏེ་དགོན་པ་ལ་གནས་ཞེས་བྱ་བ་ནི་དེ་ལ་གནས་པ་ན་བདེན་པ་མ་ཡིན་པའི་རྣམ་པར་རྟོག་པ་ཡོངས་སུ་སྤོང་བའོ། །

[Block 915]
འཇིག་རྟེན་གྱིས༌[^618]སྣ་ཚོགས་ཞེས་བྱ་བ་ནི་གང་དང་གང་བྱེད་པ་ལ་སོགས་པའོ། །
--- END BLOCKS ---
