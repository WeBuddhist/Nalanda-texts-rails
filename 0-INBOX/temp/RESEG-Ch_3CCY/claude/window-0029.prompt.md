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
[Block 1016]
གང་ཞིག་ལས་རང་བཞིན་མེད་པའོ་ཞེས་ཁོང་དུ་ཆུད་ན། དེས་ནི་ལས་ཕྱིན་ཅི་མ་ལོག་པའི་སྟོང་པ་ཉིད་དུ་ཡོངས་སུ་ཤེས་པར་འགྱུར་རོ། །

[Block 1017]
ལས་དེ་ཡང་མ་རིག་པའི་རྐྱེན་གྱིས་འདི་ནི་བདེན་པའོ་ཞེས་མངོན་པར་ཞེན་པ་སྟེ། ལས་རང་བཞིན་མེད་པའི་ཕྱིར་རང་བཞིན་མེད་པ་ལ་འབྲས་བུ་མི་འདོད་དོ། །

[Block 1018]
དེས་ན་དེས༌[^720]སྐུར་པ་བཏབ་ནས་ལོག་ལྟ་ཐོབ་པ༌[^721]མ་ཡིན༌[^722]ལས་ཀྱང་རང་བཞིན་མེད་པར་རྟོག་པས༌[^723]འདི་དག་བདེན་པར་མངོན་པར་ཞེན་པ་སྤོང་ལ། ལས་ལ་མ་ཆགས་པས་སླར་ཡང་ལས་མི་རྩོམ་མོ། །

[Block 1019]
ལས་མ་བརྩམས་པར་གྱུར་ན་ལས་ཀྱི་རྒྱུ་ཅན༌[^724]འབྲས་བུ་ལོག་གོ། །

[Block 1020]
ལས་ཀྱི་འབྲས་བུ་འཁོར་བ་ལས་ལོག་ན་ངེས་པར་འདི་ནི་མྱ་ངན་ལས་འདས་པ་ལ་གཞོལ་བར་འགྱུར་རོ་ཞེས་བྱ་སྟེ། དེ་ལྟར་དེ་ཁོ་ན་ཉིད་མཐོང་བས་ལས་ཡང་དག་པར་ཤེས་པ་སྟེ་རང་བཞིན་གྱིས་སྟོང་པར་རྟོག༌[^725]པའོ། །

[Block 1021]
དེ་ཁོ་ན་ཉིད་མཐོང་བས་མ་རིག་པ་སྤོང་ལ། མ་རིག་པ་སྤངས་ན༌[^726]རྒྱུ་མེད་པས་ལས་མི་འབྱུང་ངོ་། ། དེར་ལས་མེད་ན་གང་ཞིག་ལས་ལས་འབྱུང་བ་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་དེ་ལ་མི་འབྱུང་ངོ་། །རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་རྣམས་ཀྱང་སྐྱེ་བ་མེད་པར་གྱུར་ན་མྱ་ངན་ལས་འདས་པ་གྲུབ་པོ་ཞེས་བྱ་སྟེ། རིགས་པ་དེས་སྐྱེས་བུ་མངོན་པར་རློམ་པས་གནས་པ་ལ། རང་དང་གཞན་གྱི་དོན་སྒྲུབ་པ་ལ་མཁས་པས། ལས་རང་བཞིན་མེད་པར་སྒྲུབ་པའི་ཕྱིར་རོ། །

[Block 1022]
འདིར་སྨྲས་པ། གལ་ཏེ་ཇི་ལྟར་བསྒྲུབས་པའི་རིགས་པས་ལས་རང་བཞིན་མེད་པ་ཉིད་དུ་རྣམ་པར་འཇོག་ན། གང་ཞིག་འདི་དག་ལས་ལས་སྐྱེས་པའི་སེམས་ཅན་དང་སྣོད་ཀྱི་འཇིག་རྟེན་སྣ་ཚོགས༌[^727]དེ་ཡང་མི་འཐད་ལ། གང་ཡང་ལས་དང་བྱེད་པ་པོ་ཉེ་བར་བསྟན་པ་འདི་ཡང་ཐོབ་པར་མི་འགྱུར་རོ། །

[Block 1023]
རང་བཞིན་མེད་པའི་དྲི་ཟའི་གྲོང་ཁྱེར་ལ་སོགས་པས། འདི་ལྟར་རྣམ་པ་སྣ་ཚོགས་པའི་འབྲས་བུ་སྒྲུབ་པ་དང་བྱེད་པ་པོ་ཡོད་བཞིན་པ་ཡང་མི་འཐད་དོ་ཞེས་སོ། །

[Block 1024]
འོ་ན་དྲི་ཟའི་གྲོང་ཁྱེར་ལ་སོགས་པའི་དོན་ཀྱང་རྣམ་པར་ཤེས་པ་རང་གི་དམིགས་པ་ལ་དམིགས་པའི་དངོས་པོར་བསྒྲུབ༌[^728]བཞིན་པས་ན། སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་སྒྲུབ་པར་བྱེད་པ་པོར༌[^729]འགྱུར་ཏེ། རང་རང་གི་རྒྱུ་དང་རྐྱེན་ལ་བརྟེན་ནས་སྐྱེ་བཞིན་པས་བྱེད་པ་པོ་ཡོད་བཞིན་པར་འགྱུར་རོ། །

[Block 1025]
སྨྲས་པ། གལ་ཏེ་ཡང་རྣམ་པར་ཤེས་པའི་དམིགས་པ་ཉིད་དུ་བསྒྲུབས་ན། དེ་ལྟ་ན་ཡང་འཁྲུལ་པ་འཁྲུལ་པའི་རྒྱུ་ཉིད་དུ་བསྒྲུབས་པ་མ་ཡིན་ཏེ། རྣམ་པར་ཤེས་པ་མ་འཁྲུལ་བས་དེའི་ཕྱིར་མི་བདེན་པ་བདེན་པའི་རྒྱུར་མི་འགྱུར་བ་ཉིད་ལ། མི་བདེན་པ་ཡང་མི་བདེན་པའི་མ་ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 1026]
དེ་ལ་རྣམ་པར་ཤེས་པ་ཡང་མི་བདེན་པ་ཉིད་དུ་འདོད་ལ། དེ་ལྟ་ན་ཡང་རང་བཞིན་མེད་པ་ཡང་རང་བཞིན་མེད་པའི་འབྲས་བུ་རྫོགས་པར་བྱེད་པ་པོ་ཉིད་དུ་གསལ་བར་བྱེད་པ་ཤིན་ཏུ་གསལ་བར་དཔེར་ཉེ་བར་བསྟན་པས་གསུངས་པ།

[Block 1027 [HEADING]]
### ཚིགས་བཅད་བཞི་བཅུ་པ། ^1-40-0

[Block 1028 [VERSE]]
ཇི་ལྟར་བཅོམ་ལྡན་དེ་བཞིན་གཤེགས། །
རྫུ་འཕྲུལ་གྱིས་ནི་སྤྲུལ་པ་སྤྲུལ། །
སྤྲུལ་པ་དེ་ཡིས༌[^730]སླར་ཡང་ནི། །
སྤྲུལ་པ་གཞན་ཞིག་སྤྲུལ་པར་འགྱུར། །

[Block 1029]
བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཡོངས་སུ་རྫོགས་པའི་སེམས་ཅན་གྱི་བྱེ་བྲག་འགའ་ཞིག་ནི་ཆོས་རྣམས་ཀྱི་རང་བཞིན་ཇི་ལྟ་བ་དེ་ལྟར་རྟོགས་པའི༌[^731]ཕྱིར་རམ། ཇི་ལྟར་འདས་པའི་སངས་རྒྱས་ཐམས་ཅད་གཤེགས་པ། དེ་ལྟར་གཤེགས་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་ཞེས་བརྗོད་དོ། །

[Block 1030]
དེ་བཞིན་དུ་སྡེ་པ་གཞན་གྱི་གཞུང་ལས།

[Block 1031]
འོག་མིན་ཁོ་ནར་དེ་ཁོ་ན་ཉིད་རྣམ་པ་ཐམས་ཅད་དུ་མངོན་པར་རྟོགས༌[^732]པའོ། །

[Block 1032]
དེ་ཡང་གཙོ་བོ་དེ་བཞིན་གཤེགས་པའི་རྫུ་འཕྲུལ་གྱིས༌[^733]སྤྲུལ་པ་སྤྲུལ་ནས་འཛམ་བུའི་གླིང་དུ་མངོན་པར་བྱང་ཆུབ་པ་སྟོན་པར་བྱེད་དོ། །

[Block 1033]
སྤྲུལ་པའི་མངོན་པར་བྱང་ཆུབ༌[^734]དེ་ཡང་ཡང་དག་པའི་དེ་བཞིན་གཤེགས་པ་དང་མཐུ་མཉམ་པས་དགོས་པའི་དབང་གིས་སྤྲུལ་པ་གཞན་སྟོན་པར་མཛད་དེ། དེ་ཉིད་ཀྱིས་ན༌[^735]གསུངས་པ།

[Block 1034 [VERSE]]
མ་སྐྱེས་གནས་པ་མེད་པ་ཡི། །
འདི་ནི་ཆོས་ཀྱི་དབྱིངས་དང་མཚུངས། །
མངལ་དུ་འཇུག་པ་སྟོན་པ་ཡང་། །
འདི་དག་འཇིག་རྟེན་རྗེས་འཇུག་ཕྱིར། །

[Block 1035]
ཞེས་གསུངས་སོ། །

[Block 1036]
འཛམ་བུའི་གླིང་དུ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པ་ཉིད་ཡང་དག་པའི་དེ་བཞིན་གཤེགས་པ་ཡིན་དུ་ཆུག་ན་ཡང་། དེ་ལྟ་ན་ཡང་དེ་བཞིན་གཤེགས་པ་ནི་བསམ་གྱིས་མི་ཁྱབ་པའི་མཐུ་མངའ་བས། སྤྲུལ་པ་སྤྲུལ་ནུས་པའི་ནུས་པ་ཅན་ཉིད་དེ། བསམས་བཞིན་དུ་རྣམ་པ་དེ་ལྟ་བུའི་སྤྲུལ་པ་སྤྲུལ་ལ། གང་ཞིག་སྤྲུལ་པ་ལས་སྤྲུལ་པ་གཞན་ཡང་འཇུག་པར་མཛད་དོ། །

[Block 1037 [HEADING]]
### ཚིགས་བཅད་ཞེ་གཅིག་པ། ^1-41-0

[Block 1038 [VERSE]]
དེ་ལ་དེ་བཞིན་གཤེགས་སྟོང་སྤྲུལ། །
སྤྲུལ་པས་སྤྲུལ་པ་སྨོས་ཅི་དགོས། །
གཉིས་པོ་མིང་ཙམ་ཡོད་པ་ཡང་། །
གང་ཅི་རུང་སྟེ་རྟོག་པ་ཙམ། །

[Block 1039]
གང་འདིར་ཡང་དག་པའི་དེ་བཞིན་གཤེགས་པས་སྤྲུལ་པའི་སྤྲུལ་པ་དེ་ཉིད་རེ་ཞིག་སྟོང་པ་སྟེ་དེ་བཞིན་གཤེགས་པའི་རང་བཞིན་དང་བྲལ་བའོ། །

[Block 1040]
ཅི་འོན་ཏེ་གང་སྤྲུལ་པའི་སྤྲུལ་པ་ཐེ་ཚོམ་མེད་པར་འདི་ནི་དེ་བཞིན་གཤེགས་པའི་རང་བཞིན་དང་བྲལ་བ་ཡིན་གྱི། [^736]སྤྲུལ་པ་འདི་ཡང༌[^737]རྣམ་པ་ཐམས་ཅད་ཀྱིས་མེད་དོ་ཞེས་བརྗོད་པར་མི་ནུས་ཏེ། དེ་དག་ཉེ་བར་དམིགས་བཞིན་པའི་ཕྱིར་རོ་ཞེས་གསུངས་པ། གཉིས་པོའི་མིང་ཙམ་ཡོད་པ་ཡང་། །གང་ཅུང་ཟད་དེ་རྟོག་པ་ཙམ་ཞེས༌[^738]བྱ་བ་སྙིང་པོ་དང་བྲལ་བ་སྟེ་རང་བཞིན་དང་བྲལ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1041]
སླར་ཡང་ཇི་ལྟར་དེ་ཡོད་ཅེ་ན། གསུངས་པ་རྟོགས་པ༌[^739]ཙམ་ཞེས་བྱ་བ་ལ་ཡོངས་སུ་བརྟགས་པ་ཙམ་ཡང་དག་པ་མ་ཡིན་པར་སྒྲོ་བཏགས་པ་ཙམ་བརྫུན་པ་སླུ་བའི༌[^740]ཆོས་ཅན་ཙམ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1042]
རེ་ཞིག་དེ་དག་གི་རང་བཞིན་མེད་ལ། གལ་ཏེ་ཡང་འཁྲུལ་བ་ཙམ་དུ་ཡང་དམིགས་པ་མེད་དོ་ཞེས་བྱ་བར་གྱུར་ན་དེ་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ལ་གནོད་པར་ཡང་འགྱུར་ཏེ། རི་བོང་གི་རྭ་བཞིན་ཉེ་བར་དམིགས་པར་ཡང་མི་འགྱུར་ལ། འབྲས་བུ་གཞན་སྒྲུབ་པར་བྱེད་པར༌[^741]མི་འགྱུར་ཏེ། འདི་ཐམས་ཅད་ཀྱང་ཡོད་པས་དེས༌[^742]ཕྱིར་རྟོག་པ་ཙམ་སྟེ། ཀུན་རྫོབ་ཙམ་དུ་དེ་དག་ཡོད་དོ་ཞེས་རྣམ་པར་གཞག་གོ། །

[Block 1043]
དེ་ཡང་གང་རང་བཞིན་མེད་པ་མཐོང་བ་དེ་ནི་དོན་དམ་པ་མཐོང་ལ་ངོ་བོ་མི་དམིགས་པས་ཀྱང་དེ་ལ་མི་བདེན་པ་ལས་སྐྱེས་པ་ལ། སྲེད་པ་ཟད་པས༌[^743]རྣམ་པར་གྲོལ་བར་འགྱུར་རོ། །

[Block 1044]
དེ་ནི་འདི་ལྟར་བརྫུན་པར་མཐོང་པ་ནི་ཉོན་མོངས་པའི་རང་བཞིན་མཐོང་བས་རྣམ་པར་གྲོལ་ལོ་ཞེས་གནས་སོ། །

[Block 1045]
ཇི་ལྟར་ཡང་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་རང་བཞིན་མེད་པ་ལས་གཞན་རང་བཞིན་མེད་པ༌[^744]དེ་བཞིན་གཤེགས་པའི་རྣམ་པ་ཅན་གྱི་སྤྲུལ་པ་མཐའ་ཡས་པས་རྣམ་པ་སྣ་ཚོགས་པའི་བྱ་བ་སྒྲུབ་པ༌[^745]རུང་བ་རབ་ཏུ་འཇུག་པས།

[Block 1046 [HEADING]]
### ཚིགས་བཅད་ཞེ་གཉིས་པ། ^1-42-0

[Block 1047 [VERSE]]
དེ་བཞིན་བྱེད་པོ་སྤྲུལ་པར་མཚུངས། །
ལས་ནི་སྤྲུལ་པས་སྤྲུལ་དང་མཚུངས། །
རང་བཞིན་གྱིས་སྟོང་གང་ཅུང་ཟད། །
ཡོད་པ་དེ་དག་རྟོག་པ་ཙམ། །

[Block 1048]
ཇི་ལྟར་དེ་བཞིན་གཤེགས་པས་སྤྲུལ་པ་ལྟ་བུའི་ལས་ཀྱི་བྱེད་པ་པོ་མ་རིག་པའི་རྗེས་སུ་འབྲང་བའི་གང་ཟག་ནི། དེ་བཞིན་གཤེགས་པས་སྤྲུལ་པ་བཞིན་དུ་རང་བཞིན་མེད་ལ་འདི༌[^746]ཡང་རྟོག་པ་ཙམ་སྟེ། ཀུན་རྫོབ་ཙམ་བརྫུན་པ་སླུ་བའི༌[^747]ཆོས་ཅན་བྱིས་པའི་སྐྱེ་བོ་སླུ་བ༌[^748]ཙམ་རྨོངས་པའི་སྐྱེ་བོ་ཆགས་པ་ཙམ་དུ་ཡོད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1049]
གལ་ཏེ་ཡང་ལས་དེ་རང་བཞིན་མེད་པའི་བྱེད་པ་པོས་བསྐྱེད་ལ། དེ་ཡང་རང་བཞིན་མེད་པ་ཉིད་དུ་ཡོད་པས། འགྲོ་བ་སྣ་ཚོགས་པ་བསྐྱེད་པར་ནུས་པར་འགྱུར་རོ། །

[Block 1050]
འདིར་སྨྲས་པ། འདི་ནི་མི་རིགས་ཏེ། དཔེ་དང་དོན་དག་མི་འདྲ་བའི་ཕྱིར་རོ། །

[Block 1051]
དཔེ་ནི་ཡང་དག་པའི་དེ་བཞིན་གཤེགས་པ་ཡོད་ལ། དེའི་ཕྱིར་ཡང་དག་པ་ལས༌[^749]ཡང་དག་པ་མ་ཡིན་པའམ། ཡང་དག་པའི་སྤྲུལ་པ་འབྱུང་བར་འགྱུར་རོ་ཞེས་རིགས་སོ། །

[Block 1052]
འདིར་ཡང་དག་པའི་དངོས་པོ་མེད་ན་གང་ཞིག་སྤྲུལ་ནུས་པའི་བྱེད་པ་པོ་འཇུག་པའི་རྒྱུ་མཚན་ཉིད་དུ་རྟོགས་པར༌[^750]བྱེད་དེ། དེའི་ཕྱིར་དཔེ་དང་མི་འདྲའོ། །

[Block 1053]
སྨྲས་པ། གང་འདིར་ཡང་དག་པའི་དེ་བཞིན་གཤེགས་པ་ཡོད་དོ་ཞེས་མངོན་པར་འདོད་ན། དེ་བྱེད་པ་པོར་གྱུར་པའམ༌[^751]ལས་སུ་གྱུར་པའི་ཡང་དག་པ་ཉིད་དུ་ཡོངས་སུ་རྟོགས། [^752]གལ་ཏེ་རེ་ཞིག་བྱེད་པ་པོར་གྱུར་པར་ཡོངས་སུ་རྟོགས༌[^753]ན། དེ་ཡང་། ཡང་དག་པའི་དེ་བཞིན་གཤེགས་པའི་རང་བཞིན་མ་ཡིན་ཏེ། བྱེད་པ་པོའི་ཕྱིར་སྤྲུལ་པའི་བྱེད་པ་པོ་དེ་བཞིན་གཤེགས་པའི༌[^754]སྤྲུལ་པ་བཞིན། ཡང་ན་ལས་སུ་གྱུར་པས་ཡང་དག་པར་ཡོངས་སུ་རྟོགས༌[^755]ན། དེ་ལྟ་ན་ཡང་སྤྲུལ་པ་ནི་སྤྲུལ་པས་སྤྲུལ་པ་བཞིན་འདི་ལ་ཡང་དག་པར་བརྗོད་པར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1054]
ངེས་པར་དེ་བཞིན་གཤེགས་པ་ཡང་མེད་དམ་ཅི་ཞེ་ན། སུ་ཞིག་འདི་སྐད་དུ་ཡོད་པའམ་མེད་དོ་ཞེས་སྨྲ། གང་ཞིག་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་བ་རང་བཞིན་དུ་རྟོགས༌[^756]ན་དེ་ནི་དེ་ལ་ཡོད་པའམ་མེད་པར་ཡོངས་སུ་རྟོགས་པར༌[^757]བྱེད་ན། གང་ཡང་རང་བཞིན་མེད་པ་སྟེ་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་བཞིན་དུ༌[^758]རྟོག་པ་མེད་པ། སྤྲུལ་པ་བཞིན་དུ་རང་བཞིན་གྱིས་ཞི་བ་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་པས་དེ་ལ་ཡོད་པའམ་མེད་པར་བརྟག་པར་མི་བྱའོ། །

[Block 1055]
དེ་ན༌[^759]དེ་བཞིན་གཤེགས་པའི་རང་བཞིན་གྲུབ་པ་མེད་པས་དཔེ་དང་མི་འདྲ་བར་རྟོག་པར་ག་ལ་བྱེད། འདིར་སྨྲས་པ། གང་འདི་སྐད་དུ་སྨྲས་པའི་སྟོང་པ་ཉིད་ཀྱི་རང་བཞིན་མེད༌[^760]པས། གང་ཅུང་ཟད་ཡོད་པ་རྟོག་པ་ཙམ་ཞེས་པས། སླར་ཡང་ཅིའི་ཕྱིར་ན་འདི་དག་ཀྱང་རང་བཞིན་མེད་པ་དང་རྟོག་པ་ཙམ་དུ་ཡོད་པ་གཉིས་ཁས་ལེན་པར་བྱེད། གལ་ཏེ་སླར་ཡང་རང་བཞིན་ཡོད་པ་ཉིད་པས། རྟོག་པ་ཙམ་གྱི་དངོས་པོར་ཁས་མི་ལེན་ན། དེའི་ཚེ་སྐྱོན་ཅིར་འགྱུར་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་རང་བཞིན་ཡོད་པར་གྱུར་ན། དེའི་ཚེ་མྱ་ངན་ལས་འདས་པ་མེད་པར་འགྱུར་ལ། ཡོད་བཞིན་པ་ལ་བྱེད་པ་པོ་དོན་མེད་པའི་ཕྱིར་དང་། བྱེད་པ་པོ་ཡང་མེད་པར་འགྱུར་རོ། །
--- END BLOCKS ---
