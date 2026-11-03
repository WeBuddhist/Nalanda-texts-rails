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
[Block 806]
བཙུན་པ་རབ་འབྱོར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ལྟར་ཟབ་པ། འདི་ལྟར་མཐོང་བར་དཀའ་བ་ཞེས་བྱ་བ་ལ། གཏིང་དཔག་དཀའ་བས་ན་ཟབ་པའོ། །

[Block 807]
རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔའི་ཡུལ་མ་ཡིན་པའི་ཕྱིར་མཐོང་བར༌[^543]དཀའ་བའོ། །

[Block 808]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཡུལ་མ་ཡིན་པའི་ཕྱིར་རྟོགས་པར་དཀའ་བའོ། །

[Block 809]
ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་ཐམས་ཅད་ཉེ་བར་ཞི་བའི་ཕྱིར་ཞི་བའོ། །

[Block 810]
སྡུག་བསྔལ་ཐམས་ཅད་ཀྱི་བར་དག་ཉེ་བར་ཞི་བའི་ཕྱིར་གྱ་ནོམ་པའོ། །

[Block 811]
རྣམ་པར་རྟོག་པའི་སྤྲོས་པ་ཐམས་ཅད་ཉེ་བར་ཞི་བའི་ཕྱིར་ཕྲ་བའོ། །

[Block 812]
སོ་སོ་རང་གིས་རིག་པ༌[^544]ཡིན་པའི་ཕྱིར་གཞན་མ་ཡིན་པའོ། །

[Block 813]
བསམ་པའི་ལམ་ལས་འདས་པའི་ཕྱིར། རྟོག་གེའི་སྤྱོད་ཡུལ་མ་ཡིན་པའོ། །

[Block 814]
ཆོས་ཐམས་ཅད་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རྟོགས་པ་ལ་མཁས་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་མཁས་པའོ། །

[Block 815]
འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་རྟོགས་པའི་གནས་ཀྱི་མཆོག་ཡིན་པས་ཤིན་ཏུ་འཕགས་པའོ། །

[Block 816]
ཉན་ཐོས་དང་། རང་སངས་རྒྱས་རྣམས་ཀྱི་སྤྱོད་ཡུལ་མ་ཡིན་པ་དང་། ཕྱིར་མི་ལྡོག་པ་རྣམས་ཉིད་ཀྱིས་རིག་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་མཁས་པ་དང་མཛངས་པས་རིག་པར་བྱའོ། །

[Block 817]
ལེན་པར་བྱེད་པར་འགྱུར་ཞེས་བྱ་བ་ནི་འཛིན་པའོ། །

[Block 818]
བདེན་པ་མཐོང་བའི་གང་ཟག་གམ། དགྲ་བཅོམ་པ་ཟག་པ་ཟད་པ་འམ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྔར་ཀུན་རྫོབ་ཏུ་ཚོལ་བར་བྱེད་པ་བསྟན་ཏོ། །

[Block 819]
དེ་ལ་དོན་དམ་པར་ན་བྱང་ཆུབ་སེམས་དཔའ་ལ་བདེན་པ་མཐོང་བ་ཞེས་གསུངས་སོ། །

[Block 820]
བྱང་ཆུབ་ཏུ་འགྱུར་བ་ནི་དགྲ་བཅོམ་པ་ཞེས་བྱ་བའོ།

[Block 821]
[^545] །དེ་ལྟར་ཀུན་རྫོབ་ཏུ་བསྟན་ནས་ཡང༌[^546]དོན་དམ་པར་བསྟན་པ་དེ་དག་ནི་གཟུགས་སྟོང་ངོ་ཞེས་བྱ་བར་རྣམ་པར་རྟོག་པར༌[^547]མི་འགྱུར་ཞེས་བྱ་བ་ནས། ལེན་པར་བྱེད་པ་སུ་ཡང་མེད་དོ་ཞེས་བྱ་བའི་བར་དུ་སྟེ། འདིས་ནི་གང་དག་དེ་ལྟར་རྣམ་པར་མི་རྟོག་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མངོན་སུམ་དུ་བྱས་པར་གྱུར་པ༌[^548]དེ་དག་ཉིད་ཚོལ་བར་བྱེད་པ་ཡིན་ཏེ། དེ་དག་ཀྱང་དོན་དམ་པར་བཙལ་བར་བྱ་བ་མེད་པའི་ཕྱིར་ཚོལ་བར་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་སྟོན་ཏོ། །

[Block 822]
དེ་སྐད་སྨྲས་པ་དང་། གནས་བརྟན་ཤ་ར་དྭ༌[^549]ཏིའི་བུས་འཆད་པ་པོ་དང་། ཉན་པ་པོ་མེད་པར་དམ་བཅས་པ་ལུང་དང་འགལ་བར་བསྟན་པས། ཚེ་དང་ལྡན་པ་རབ་འབྱོར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས་ཐེག་པ་གསུམ་རྒྱ་ཆེར་མ༌[^550]བསྟན་ཏམ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ཐེག་པ་གསུམ་བཤད་པ་དང་། ས་བཅུ་ཡོངས་སུ་བཟུང་བ༌[^551]དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་བྱང་ཆུབ་སེམས་དཔའི་ལམ་དང་། དེ་བཞིན་གཤེགས་པའི་རིགས་སུ་སྐྱེ་བ་དང་། མངོན་པར་ཤེས་པས་རྣམ་པར་རྩེ་བས་གནས་པ༌[^552]དང་། ཆོས་ཉན་པ་དང་། མི་བརྗེད་པ་དང་། སེམས་འཁྲུགས་པ་མེད་པ་དང་། སྤོབས་པའི་ཡོན་ཏན་བདུན་ལ་སོགས་པ་ཆོས་འདི་རྣམས་བསྟན་ཏེ། བདག་ཅག་གིས་ཀྱང་ཐོས་སོ་ཞེས་སྟོན་ཏོ། །

[Block 823]
དེའི་འོག་ཏུ་གནས་བརྟན་རབ་འབྱོར་གྱིས་ཆོས་འདི་རྣམས་མི་དམིགས་པའི་ཚུལ་གྱིས་བཤད་ཀྱི། དོན་དམ་པར་ནི་ཡོད་པ་མ་ཡིན་ཏེ། དེ་བས་ན་བཤད་པ་ཡང་འཁྲུལ་པ་ཙམ་མོ་ཞེས་བསྟན་པའི་ཕྱིར། ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ༌[^553]ཏིའི་བུ་དེ་དེ་བཞིན་ནོ་དེ་དེ་བཞིན་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 824]
དེ་དག༌[^554]སྟོང་པ་ཡིན་པའི་གཏན་ཚིགས་ནང་སྟོང་པ་ཉིད་དང་ཞེས་བྱ་བ་ནས་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་ཀྱི་བར་གྱི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 825]
ལྷའི་བུ་རྣམས་ལ་ཡེ་ཤེས་ཀྱི་སྣང་བ༌[^555]འབྱུང་བའི་མཚན་མ་བསྟན་པའི་ཕྱིར་མེ་ཏོག་གི་མཆོད་པ་བསྟན་ཏེ། མེ་ཏོག་འདི་དག་སྤྲུལ་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བསམས༌[^556]པ་འོག་ནས༌[^557]བསྟན་པའི་སྐབས་དབྱེ་བའི་ཕྱིར་རོ། །

[Block 826]
ཀཽ་ཤི་ཀ་མེ་ཏོག་འདི་དག་མ་བྱུང་བ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་མ་སྐྱེས་པ་སྟེ། སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཡིན་གྱི། མེ་ཏོག་གི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ་ཞེས་སྟོན་ཏོ། །

[Block 827]
ཀཽ་ཤི་ཀ་གཟུགས་ཀྱང་མ་བྱུང་བ་སྟེ། གང་མ་བྱུང་བ་དེ་ནི་གཟུགས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དོན་དམ་པའི་གཟུགས་ལ་འདུས་བྱས་ཀྱི་སྐྱེ་བ་མེད་པའི་ཕྱིར་གཟུགས་མ་བྱུང་བའོ་ཞེས་བསྟན་པའོ། །

[Block 828]
དེ་ལྟར་འདུས་མ་བྱས་པ། མ་སྐྱེས་པ་ལ་ཀུན་བརྟགས་པའི་གཟུགས་ཀྱི་མཚན་ཉིད་མེད་པའི་ཕྱིར་མ་སྐྱེས་པ་གང་ཡིན་པ་དེ་གཟུགས་མ་ཡིན་ནོ་ཞེས་བསྟན་པའོ། །

[Block 829]
བཏགས་པ་དང་ཡང་མི་འགལ་ལ། ཆོས་ཉིད་ཀྱང་སྟོན་ཏེ༌[^558]ཞེས་བྱ་བ་ནི་ཀུན་རྫོབ་དང་དོན་དམ་པར་མི་འགལ་བར་བསྟན་ཏོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ།། །།

[Block 830 [HEADING]]
##### ཇི་ལྟར་བསླབ་པར་བྱ་ཞེས་དྲིས་པའི་ལན། ^1-2-1-3-0

[Block 831]
བམ་པོ་བཅོ་བརྒྱད་པ། ཀཽ་ཤི་ཀ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོའི༌[^559]དེ་ལྟར་ཆོས་ཐམས་ཅད་བརྟགས་པ་ཙམ་དུ་རིག་པར་བྱས་ཏེ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་བསླབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་སྔར་རྣམ་པ་གསུམ་དུ་ཞུས་པ༌[^560]ལས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ཇི་ལྟར་བསླབ་པར་བགྱི་ཞེས་ཐ་མར་ཞུས་པ་དེ་སྟོན་ཏོ། །

[Block 832]
གཟུགས་ལ་མི་སློབ་ཅེས་བྱ་བ་ལ་སོགས་པ༌[^561]ནི་མི་སློབ་པ་ཉིད་སློབ་པ་སྟེ་དཔེར་ན་གནས་པ་མེད་པ་ཉིད་གནས་པའོ་ཞེས་བྱ་བ་ལྟ་བུར་སྟོན་ཏོ། །

[Block 833]
གཟུགས་ལ་སོགས་པ་དངོས་པོ་མེད་པར་མཐོང་བས་གཟུགས་ལ་སོགས་པ་ལ་མི་སློབ་ཅེས་བྱའོ་ཞེས་བསྟན་པའི་ཕྱིར། འདི་ལྟར་གང་ལ་བསླབ་པར་བྱ་བའི་གཟུགས་དེ་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 834]
གཟུགས་ལ་སོགས་པ་ཅིའི་ཕྱིར་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་ཞེས་བརྒྱ་བྱིན་གྱིས་དྲིས་པ་དང་། སྟོང་པ་ཡིན་པས་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་ངོ་ཞེས་བསྟན་པའི་ཕྱིར། གཟུགས༌[^562]གཟུགས་ཀྱིས་སྟོང་ངོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 835]
མི་སློབ་པའི་གཏན་ཚིགས་སུ། ཀཽ་ཤི་ཀ་གཟུགས་སྟོང་པ་ཉིད་ནི་གཟུགས་སྟོང་པ་ཉིད་ལ་མི་སློབ་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སློབ་པ་གང་ཡིན་པ་དང་གང་ལ་སློབ་པ་དེ་གཉིས་ཀ་ཡང་མེད་པའི་ཕྱིར་སློབ་པ་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 836]
དེའི་འོག་ཏུ་ཀཽ་ཤི་ཀ་གང་གཟུགས་སྟོང་པ་ཉིད་ལ་མི་སློབ་ཅེས་བྱ་བ་ནས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་སྟོང་པ་ཉིད་ཀྱི་བར་ལ་མི་སློབ་པ་དེ་ནི་གཉིས་སུ་བྱར་མེད་པར་གཟུགས་སྟོང་པ་ཉིད་ལ་སློབ་པོ་ཞེས་བྱ་བ་ནས་གཉིས་སུ་བྱར་མེད་པར་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ༌[^563]སྟོང་པ་ཉིད་ལ་སློབ་པོ་ཞེས་བྱ་བ་ནི་གང་མི་སློབ་པ་དེ་ཉིད་སློབ་པ༌[^564]ཡིན་པར་སྟོན་ཏོ། །

[Block 837]
གཉིས་སུ་བྱར་མེད་པར་ཞེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་དུ་གཅིག་པའི་ཕྱིར་གཅིག་གི་སྟོང་པ་ཉིད་ལ་བསླབས་ན་ཆོས་ཐམས་ཅད་ཀྱི་སྟོང་པ་ཉིད་ལ་བསླབ་པ༌[^565]ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 838]
དེ་བས་ན། གཅིག་གི་སྟོང་པ་ཉིད་གང་ཡིན་པ་དེ་ནི༌[^566]ཀུན་གྱི་སྟོང་པ་ཉིད་ཅས་བཤད་དོ། །

[Block 839]
དེའི་འོག་ཏུ་ཀཽ་ཤི་ཀ་གང་གཉིས་སུ་བྱར་མེད་པ༌[^567]གཟུགས་སྟོང་པ་ཉིད་ལ་སློབ་པ་ཞེས་བྱ་བ་ནས་གཉིས་སུ་བྱར་མེད་པར་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ལ་སློབ་པ་དེ་ནི་སངས་རྒྱས་ཀྱི་ཆོས༌[^568]གྲངས་མེད། དཔག་ཏུ་མེད་པ་རྣམས་ལ་བསླབ་པ༌[^569]ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་དེ་ལྟར་ཆོས་ཐམས་ཅད་ཀྱི་སྟོང་པ་ཉིད་ལ་བསླབ་པ༌[^570]དེ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་ནས། སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཀྱི་བར་དག་ལ་བསླབ་པ༌[^571]ཡིན་ནོ་ཞེས་སྟོན་ཏོ། །

[Block 840]
དེའི་འོག་ཏུ་དེ་ནི་གཟུགས་འཕེལ་བར་བྱ་བ་དང་འགྲིབ་པར་བྱ་བའི་ཕྱིར་མི་སློབ་པོ་ཞེས་བྱ་བ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་རྣམས་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཀྱི་བར་དག་ལ་སློབ་པ་དེ་གཟུགས་ལ་སོགས་པ་ལ་འཕེལ་བར་བྱ་བའམ། འགྲིབ་པར་བྱ་བ་མེད་པར་སྟོན་ཏེ། དཀར་པོའི་ཕྱོགས་འཕེལ་བར་བྱ་བའམ། ནག་པོའི་ཕྱོགས་འགྲིབ་པར་བྱ་བའི་ཕྱིར་མི་སློབ་པོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 841]
དེའི་འོག་ཏུ་དེ་ནི་གཟུགས་ཡོངས་སུ་གཟུང་བ༌[^572]དང་མེད་པར་བྱ་བའི་ཕྱིར་མི་སློབ་པོ་ཞེས་བྱ་བ་ནི་གང་ལ་དེ་ལྟར་འཕེལ་བར་བྱ་བ་དང་། འགྲིབ་པར་བྱ་བའི་ཆོས་རྣམས་མེད་པ་དེ་ལ་ཁྱད་པར་དུ་འཕགས་པའི་ཆོས་རྣམས་ཡོངས་སུ་བཟུང་ཞིང་ཆོས་ངན་པ་རྣམས་ཆུད་གསན་པར་བྱ་བ་མེད་པར་སྟོན༌[^573]ཏོ། །

[Block 842]
དེ་སྐད་སྨྲས་པ་དང་། ཚེ་དང་ལྡན་པ་རབ་འབྱོར་ཅིའི་ཕྱིར་དེ༌[^574]ཡོངས་སུ་འཛིན་པ་དང་མེད་པར་བྱ་བའི་ཕྱིར་མི་སློབ་ཅེས་གསུངས་པ་ནི་གནས་བརྟན་ཤཱ་རིའི་བུས་དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་ཆོས་ངན་པ་རྣམས་ཡོངས་སུ་སྤོང་ཞིང་ཁྱད་པར་དུ་འཕགས་པའི་ཆོས་རྣམས་ཐོབ་པར༌[^575]བྱེད་ན་དེ་ལ་ཅིའི་ཕྱིར་ཡོངས་སུ་འཛིན་པ་དང་། མེད་པར་བྱ་བ་མེད་ཅེས་འདྲི་བའོ། །

[Block 843]
དེ་སྐད་ཅེས་སྨྲས་པ་དང་། གནས་བརྟན་རབ་འབྱོར་གྱིས་གཟུགས་ལ་གཟུགས་ཡོངས་སུ་མི་འཛིན་ཏོ་ཞེས་བྱ་བ་གསུངས་ཏེ། གཟུང་བ་དང་འཛིན་པ་རྣམས་མེད་པར་སྟོན་ཏོ། །

[Block 844]
དེའི་གཏན་ཚིགས་སུ་སྟོང་པ་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 845]
གཟུགས་ཀྱི་སྐྱེ་བ་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གློ་བུར་ལ་ནི་སྐྱེ་བ་མེད་དོ། །
--- END BLOCKS ---
