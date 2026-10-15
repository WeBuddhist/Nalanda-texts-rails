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
[Block 771]
བྱིན་ལེན་མ་བསྟབས་པ་དང་རུང་བར་མ་བྱས་པ་དང་དུས་མ་ཡིན་པར་བཟའ་བ་ལ་སོགས་པ་རུང་བར་བྱ་བ་དག་ལ་ཐམས་ཅད་དུ་རྩོམ་འདོད་པ་ལ་སོགས་པ་ན་བྱང་གི་སྒྲ་མི་སྙན་ན་གྲགས་པའི་ཡིད་ལ་བྱེད་པ་བྱའོ་ཞེས་བྱ་བ་ནི་རང་གིས་བྱེད་པར་འདྲ་བ་ལ་རྣམ་པར་དག་པར་གྱུར་པའི་སྡེ་འདི་སྐས་ཀྱི་གདང་བུ་ལྟ་བུར་གྱུར་པ་སྟེ། བྱེ་བྲག་ཐོབ་པའི་ཕྱིར་དེ་དང་འདྲ་བའོ།[^467] །ཇི་ལྟར་མངོན་པར་འདུ་བྱེད་པས་ཀྱང་ཡིད་ལས་ངེས་པར་འབྱུང་བ་ཞེས་བྱ་བ་ནི་རྩོམ་འདོད་པ་ནའོ། །

[Block 772]
དེ་བས་ན་འདིར་ཐམས་ཅད་དུ་བྱང་གི་སྒྲ་མི་སྙན་ན་གྲགས་པའི་ཕྱིར་རྩོམ་འདོད་པ་ལ་སོགས་པའོ། །

[Block 773]
ཐམས་ཅད་དུ་ཞེས་བྱ་བ་ནི་རྩ་བ་དང་འབྲས་བུ་ལ་བརྟེན་པ་འདི་ཉིད་ལ་མ་ཡིན་ནོ། །

[Block 774]
འདིར་སོགས་པའི་སྒྲས་ནི་ལེན་པ་དང་ཉེ་བར་ལེན་པའི་དོན་དུ་རིག་པར་བྱའོ། །

[Block 775]
ལག་པ་བསྙལ་བ་དང་འདབ་མ་དག་ཡོད་ན་སྐྱོགས་ཀྱིས་སྐོམ་མི་བཏུང་ངོ་ཞེས་བྱ་བ་ནི་ཆུ་ཉུང་ཟད་ཉིད་དང་ལམ་འགྲོན་ཤོར་བ་ལ་སོགས་པས་ལག་པ་བསྙལ་བ་མེད་པའོ། །

[Block 776]
མེད་ན་མ་བསྒྲིབས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ལག་པ་བསྙལ་བ་དང་འདབ་མ་དག་མེད་ན་སྐྱོགས་ཀྱིས་སྐོམ་བཏུང་བ་མ་བསྒྲིབས་པར་བཏུང་བར་མི་བྱའོ། །

[Block 777]
དེ་ཆུ་དང་བཅས་པ་ཉིད་ཡིན་ན་ཁ་མ་བཅད་པ་ཉིད་དུ་མི་གཞག་གོ་ཞེས་བྱ་བ་དེ་ལ་དེ་ཞེས་བྱ་བ་ནི་སྐྱོགས་སོ། །

[Block 778]
དེའི་ཁ་གབ་ནི་རྣམ་པ་གསུམ་སྟེ། ཤིང་ལས་བྱས་པ་དང་རྡོ་ལས་བྱས་པ་དང་ས་ལས་བྱས་པའོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་སྐྱོགས་ལའོ། །

[Block 779]
སྐྱོགས་གཞི་ཤིང་ལས་བྱས་པའམ་རྡོ་ལས་བྱས་པ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། གང་དུ་གནས་པའི་དོན་དུ་སྐྱོགས་འདི་གཞག་པར་བྱ་བ་དེ་ནི་སྐྱོགས་ཀྱི་གཞིའོ། །

[Block 780]
འདབ་མ་དག་སྣོད་ཉིད་དུ་སྤྱོད་པ་ནི་བྱིན་ལེན་མ་བྱས་པ་ཉིད་ལ་ཉེས་པ་མེད་དོ། །

[Block 781]
འདི་ལ་བརྔས་པ་དང་མ་བརྔས་པ་དག་ནི་ཁྱད་པར་མེད་དོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ཤིང་ལྗོན་པ་ལ་སོགས་པ་མ་བརྔས་པ་དག་ལ་ཡང་སྐྱེས་པ་ལས་འདི་རྣམས་དང་འབྲེལ་པས་འདིར་ཉེས་པ་མེད་པ་ནི་བྱིན་ལེན་མ་བྱས་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 782]
གཞན་མེད་ན༌[^468]མ་བརྔས་པ་དག་སྤྱད་དོ་ཞེས་བྱ་བ་ལ། གཞན་ཞེས་བྱ་བ་ནི་འདབ་མ་བརྔས་པའམ་དེའི་དོན་བྱེད་ནུས་པ་གཞན་ལའོ། །

[Block 783]
ཤིང་ལྗོན་པ་ལ་སོགས་པ་དག་དང་འབྲེལ་པའི་སྐོམ་ལ་སོགས་པ་འཐུང་བར་བྱེད་པ་བཞད་གད་དུ་འགྱུར་བས་མི་བྱའོ་ཞེས་བྱ་བ་འདི་ལ་བསྟན༌[^469]པའོ། །

[Block 784]
གསོག་འཇོག་གི་ལྟུང་བྱེད་དོ།། །།

[Block 785]
གཞན་དང་བྱིན་ལེན་སྟོབས་པ་མེད་ན་སྦྱིན་བདག་གིས་བསམ་པ་ཐག་པ་ནས་བཏང་བ་རང་གིས་བླངས་ཏེ་བཟའ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བྱིན་ལེན་མ་བསྟབས་པར་བཟའ་བ་ཐམས་ཅད་ལ་བྱང་གི་སྒྲ་མི་སྙན་པའི་དུས་སུ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་ཐམས་ཅད་དུ་ཤེས་པར་བྱའོ། །

[Block 786]
བྱིན་ལེན་བྱས་ཟིན་པའི་ཟས་གཞན་མེད་དམ་བྱིན་ལེན་སྟོབས་པ་པོ་གཞན་མེད་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 787]
གང་ཡང་རུང་བ་ཅིག་ཡོད་ན་ཉེས་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 788]
འདིར་གཞན་མེད་པའི་གཞུང་ནི་དགེ་སློང་གཅིག་གིས་བསོད་སྙོམས་བླངས་ཏེ། གཙུག་ལག་ཁང་དུ་བཞག་ནས་ཕྱི་རོལ་དུ་བྱུང་བ་དང་། ཁྱིམ་བདག་གཅིག་གིས་ཀྱང་བསོད་སྙོམས་གཅིག་ཁྱེར་ཏེ་འོངས་ནས་དེ་ཉིད་ཀྱི་སྟེང་དུ་བསོད་སྙོམས་གཞན་གཞག་པ་མཐོང་ནས་དེ་འགྱོད་པ་སྐྱེས་ཏེ་མི་ཟ་བའི༌[^470]སྐབས་དེ༌[^471]དགེ་སློང་དག་གིས་བཅོམ་ལྡན་འདས་ལ་གསོལ་པ་དང་། ཇི་སྲིད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གལ་ཏེ་བྱིན་ལེན་སྟོབས་པ་ཡོད་ན་ནི་བྱིན་ལེན་བྱས་ཏེ་བཟའ་བར་བྱའོ། །

[Block 789]
ཅི་སྟེ་མེད་ན་ནི་ཕྱིས་བྱིན་པ་གང་ཡིན་པ་དེ་བསལ་ཏེ་སྔ་མ་ཤོས་བཟའ་བར་བྱ་སྟེ། འདི་ལ་འགྱོད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 790]
བྱིན་ལེན་བསྟབས་པ་མེད་པའི་གཞུང་ནི་དེ་ཉིད་ལས་ཚོང་བ་རབ་ཏུ་མང་པོ་དག་གིས་སངས་རྒྱས་ལ་སོགས་པ་དགེ་སློང་གི་དགེ་འདུན་བཤོས་ལ་སྤྱན་དྲངས་ཏེ། དེ་དག་གིས༌[^472]ཟས་དག་སྤྱི་བུངས་བཅེར་བ་དང་། ཚོང་ཁང་དག་ཏུ་མེ་ཤོར་ནས་དེ་དག་མེ་གསོད་པའི་ཕྱིར། དོང་པ་དང་གདུགས་ཚོད་དག་ཀྱང་བབ་པར་གྱུར་ནས་དགེ་སློང་དག་གིས་ཇི་ལྟར་བསྒྲུབ་པར༌[^473]བྱ་བ་མི་ཤེས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་དག་གིས་བསམ་པ་དག་པས་བཏང་བ་ཡིན་པས་བྱང་གི་སྒྲ་མི་སྙན་པའི་དུས་སུ་བྱིན་གྱིས་བརླབ་ཅིང་བཟའ་བར་བྱ་སྟེ། འདི་ལ་འགྱོད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །ཤེས་གཙོ་བོ་བྱིན་ལེན་མ་བྱས་པ་ཉིད་ལའོ་ཞེས་འོག་ནས་འབྱུང་ན་དེ་བྱིན་ལེན་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེ་བརྗོད་པར་བྱ་སྟེ། མངོན་སུམ་དུ་མཚམས་ཀྱི་ནང་དུ་འཐོབ་པའི་ཕྱོགས་ན་གནས་པས་ལག་པ་བཀན་པས་ལུས་སམ་དེ་དང་འབྲེལ་པར་གྱེན་དུ་འདེགས་ནུས་པ་བསྙེན་པར་མ་རྫོགས་པ་མི་མ་ཡིན་པ་ལས་ཀྱང་སྦྱིན་པར་འདོད་པས་ཡན་ལག་གིས་སམ་དེ་དང་འབྲེལ་པས་བྱིན་པ་མནོས་པ་ནི་བྱིན་ལེན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མངོན་སུམ་དུ་ཞེས་བྱ་བ་ནི་མངོན་སུམ་དུ་ཕྱོགས་པ་སྟེ། གློའམ་རྒྱབ་ནས་བླངས་པ་ནི་བྱིན་ལེན་མ་ཡིན་ནོ། །

[Block 791]
མཚམས་ཀྱི་ནང་དུ་ཞེས་བྱ་བ་ལ་འདི་ནི་སྤྲོས་པ་སྟེ། མཚམས་གཞན་ན་གནས་པ་གང་ལ་ཡན་ལག་ཉིད་མ་ཡིན་ཞེས་གསུངས་སོ། །

[Block 792]
གྱེན་དུ་འདེགས་ནུས་པ་ལས་ཞེས་བྱ་བ་ནི་གང་ཞིག་སྦྱིན་པར་ནུས་པ་དེ་ལས་སོ། །

[Block 793]
མི་མ་ཡིན་པ་ལས་ཀྱང་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་དགེ་སློང་དགོན་པ་པ་རྣམས་ལ་དགོན་པ་ན་གནས་པའི་གླང་པོ་ཆེ་ཅང་ཤེས་དང་རྟ་ཅང་ཤེས་དང་སྤྲེའུ་ཅང་ཤེས་དག་གིས་ཤིང་ཐོག༌[^474]དག་འབུལ་བ་དགེ་སློང་དག་མི་ལེན་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གང་ལ་གྱེན་དུ་འདེགས་པ་ཡོད་པ་དེ་ལ་བྱིན་ལེན་ཡང་ཡོད་པས་བཟའ་བར་བྱ་སྟེ། འདི་ལ་འགྱོད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 794]
སྦྱིན་པར་འདོད་པས་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་དབང་མེད་པ་ལ་སོགས་པས་སྦྱིན་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 795]
ཡུལ་གྱིས་མི་སྨད་པར་བྱ་བ་ཉིད་ཡིན་ན་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་ཞོག་ཅིག་ཅེས་བསྟན་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཉེ་བར་བསྟན་པའི་དཀྱིལ་འཁོར་ལ་ཡང་བཏང་བ་ལ་སོ་སོར་འདོད་པ་ནི་བྱིན་ལེན་མནོས་པ་ཡིན་གྱི་ལུས་སམ་དེ་དང་འབྲེལ་པར་མནོས་པ་འབའ་ཞིག་ཏུ་ནི་མ་ཟད་དོ། །

[Block 796]
ལྷུང་བཟེད་དང་དེའི་གཞི་དག་ནི་གཅིག་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདི་དག་ལས་གཅིག་ཏུ་བྱེད་དུ་བཅུག་པ་དག་ལ་གཞན་དུ་ལྟུང་བ་མི་འདོད་པ་ལས་སྐྱེས་པར་ཤེས་པར་མི་བྱ་ཞེས་བྱ་བ་དེ༌[^475]ལ་འདི་བསྟན་པའོ། །

[Block 797]
སྤྲེའུ་རྣམས་ཀྱི་སྤྱོད་ཡུལ་ནི་ཡལ་ག་ཡིན་པས་དེ་ནས་དེའི་ཕྱིར་མི་འཐོབ་པའི་ས་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཡལ་ག་དེ་ནས་སྤྲེའུ་རྣམས་བྱིན་ལེན་བསྟབས་པ་དེའི་ཕྱིར་མི་འཐོབ་པའི་ས་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 798]
ཤིང་ཐོག༌[^476]དག་མན༌[^477]ཤེལ་དང་ཁྲི་དང་ཁྲིའུ་དང་ཐུ་བ་དང་ལྷུང་བཟེད་དག་གིས་བྱིན་ལེན་མནོད་དུ་མི་རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། བྱིན་ལེན་མནོད་དུ་ཞེས་བྱ་བ་ནི༌[^478]བྱིན་ལེན་གྱི་བདག་ཉིད་ཅན་ནི་བྱིན་ལེན་གྲུབ་པར་འགྱུར་བའི་སྣོད་དུ་རུང་བར་གྱུར་པ་ལའོ། །

[Block 799]
དེ་དག་གནས་པ་དག་གིས་ཅང་མི་སྨྲ་བས་སོ་སོར་བརྟག་པར་བྱ་བ་ལ། དེ་རྣམས་ཞེས་བྱ་བ་ནི་ཤིང་ཐོག་རྣམས་ལའོ། །

[Block 800]
སྙོམས་པར་འདྲིམ་པར་བྱེད་པ་མོས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྙོམས་པར་འདྲིམ་པ་འདི་ལ་ཡོད་པས་ན། སྙོམས་པར་འདྲིམ་པ་ཞེས་བྱ་བས་བསྡུས་པའོ། །

[Block 801]
འདིར་གཞུང་ནི་འདྲིམ་པའི་ཕྱིར་ཁྱིམ་པ་རྣམས་ཤིང་ཐོག་དག་མི་སྙོམས་པར་འདྲིམ་པར་བྱེད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་ཚུལ་དག་བྲིམ༌[^479]དུ་གཞུག་པར་བྱའོ། །

[Block 802]
དགེ་ཚུལ་དག་ཀྱང་མི་སྙོམས་པར་འདྲིམ་པར་བྱེད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་དག་གིས་ལག་པ་དག་བསྙལ་ཏེ་བྱིན་ལེན་བྱས་ནས་བྲིམ་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 803]
དགེ་སློང་བྱིན་ལེན༌[^480]བྱས་པས་བྲིམ་པ་ཉིད་ནི་རུང་བ་ཉིད་ཡིན་ནོ་ཞེས་ཟས་བྱིན་ལེན་བྱས་པ་བྲིམ་པ་ཉིད་ནི་རུང་བ་ཡིན་ཏེ། ཚུལ་དང་མི་མཐུན་པ་ཉིད་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 804]
མར་དང་འབྲུ་མར་དང་སྦྲང་རྩི་དང་བུ་རམ་གྱི་དབུ་བའི་བུམ་པ་དག་འདྲིམ་ན་རྩྭ༌[^481]དང་ལོ་མ་དག་ལ་སོགས་པ་དག་གིས༌[^482]གོས་དག༌[^483]བསྐྱབ་པར་བྱའོ། །

[Block 805]
བྲིམ་པར་བྱ་བ་གཅེས་པ་དང་བར་མ་དང་ཐ་མ་དག་སོ་སོར་བྱའོ་ཞེས་བྱ་བ་ནི་བྲིམ་པར་བྱ་བའི་ཟས་འདི་རྣམས་ནི་སོ་སོར་བྲིམ་པར་བྱ་སྟེ་མི་བསྲེ་བར་བྲིམ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 806]
ཨ་མྲ་ཞིམ་པོ་དག་ལོགས་ཤིག་ཏུ་བསལ༌[^484]ཏེ་བྲིམ་པར་བྱའོ་ཞེས་བྱ་བ་ལ་མདོ་སྔ་མ་འདི་སྙོམས་པར་བསལ་བའི་དོན་དུའོ། །

[Block 807]
འདི་རྣམས་ནི་རྒན་པ་ཉིད་མ་ཡིན་ཏེ། དེ་བས་ན་སྤྲོས་པ་འདི་ནི་རྒན་པ་དང་གཞོན་པ་དང་བར་མ་དག་ལ་ཤེས་པར་མི་བྱའོ། །

[Block 808]
འདྲིམ་པར་བྱེད་པ་ཡི༌[^485]ནི་མཁན་པོའམ་སློབ་དཔོན་གྱིས་མནོད་པར་བྱའོ། །

[Block 809]
མི་འཐོབ་པ་འཐོབ་ན་དྲུང་དུ་འདུག་པས་སོ་ཞེས་བྱ་བ་གལ་ཏེ་མཁན་པོའམ་སློབ་དཔོན་གྱིས་འདྲིམ་པར་བྱེད་པས་མི་ཐོབ་པ་ཐོབ་པ༌[^486]མི་རིགས་པ་ནི་གནས་གཞན་མ་ཡིན་པས་འདི་ལ་བྱིན་ལེན་དུ་བྱ་བའོ། །

[Block 810]
འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། འདྲིམ་པར་བྱེད་པའི་སྐལ་བ་ནི་མཁན་པོ་དང་སློབ་དཔོན་དག་གིས་མནོད་པར་བྱའོ། །
--- END BLOCKS ---
