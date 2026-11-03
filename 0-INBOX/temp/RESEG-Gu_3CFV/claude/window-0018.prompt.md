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
[Block 631]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 632]
བཙུན་པ་དེ་ཉིད་ན་དགེ་སློང་དང་བཅས་ཤིང་དེ་ཉིད་ན་ཁྱིམ་པ་དང་བཅས་ན་དེར་དགུང་དུ་ལགས་པ་དང་དེར་བསྒྲལ་བར་འཚལ་བར་བགྱི་འམ༌[^367]མི་བགྱི། ཉེ་བ་འཁོར་བཟའ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 633]
གནས་སྟོང་པར་བྱས་པ་ཞིག་ཏུ་གལ་ཏེ་དགེ་སློང་རེ་ཞིག་གནས་པར་གྱུར་ན་དེ་ཡང་དགེ་སློང་གནས་སུ་རུང་བ་ཉིད་ཡིན་ནོ། །

[Block 634]
ཁྱིམ་པའི་རྫས་མ་བཏོན༌[^368]ན་ནི་སྟོང་པར་བྱ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 635]
དགེ་ཚུལ་རྣམས་ཀྱི་གང་ཟག་གི་གནས་དང་། དགེ་ཚུལ་འཚོགས༌[^369]ས་སྤྱིར་དབང་བའི་གནས་དེ་ནི་དགེ་སློང་གི་གནས་ཉིད་མ་ཡིན་ནོ། །

[Block 636]
དགེ་སློང་གི་གནས་སམ་དགེ་སློང་གི་དགེ་འདུན་གྱི་གནས་ན་དགེ་ཚུལ་ཙམ་གནས་སུ་ཟིན་ཀྱང་དེ་ལྟ་མོད་ཀྱི། དགེ་སློང་གི་གནས་ཉིད་ཡིན་ཏེ། དགེ་ཚུལ་རྣམས་ནི་དགེ་སློང་གི་འཁོར་ཡིན་པའི་ཕྱིར་རོ། །

[Block 637]
ལག་ཉར་བླངས་པ་དང་ནང་དུ་བཙོས་པ་དང་། དགེ་སློང་གིས་བཙོས་པ་དེ་དག་དུས་ཀྱི་ཕྱིར་དགག་པར༌[^370]མཛད་པར་འཚོ་བའི་བར་དུ་བཅང་བ་དག་ནི་མ་བསྡུས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་དག་དགག་པ་མཛད་པ་ཞེས་བྱ་བ་ནི་ལག་ཉར་བླངས་པ་ལ་སོགས་པ་དེ་དག་བཟའ་བར་མི་བྱའོ་ཞེས་དགག་པ་མཛད་པ་ལའོ། །

[Block 638]
དུས་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་ནི་གུང་ཚིགས་ཚུན་ཆད་ཀྱི་སྔ་དྲོ་དང་དེ༌[^371]ཕྱིན་ཆད་ཐུན་ཚོད་ཀྱི་དུས་དེ་ཉིད་ལ་གང་དུ་ལག་ཉར་བླངས་པ་ལ་སོགས་པ་བྱས་ན་དུས་དེ་ཉིད་དུ་བཟའ་བར་བྱ་བ་དེ་ཉིད་ཡིན་གྱི་དེ་ཕན་ཆད་དུ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 639]
གཞུང་ཁ་ཅིག༌[^372]ལས་བཙུན་པ་ལྟུང་བར་བྱ་བའི་སྨན་རང་གིས་བླངས་ན༌[^373]བྱིན་ལེན་བྱ་བ་འདི་གསུངས་ཏེ་ལག་ཉར་བླངས་པ་དང་ནང་དུ་བཙོས་པ་དང་དགེ་སློང་གིས་བཙོས་པ་དེ་རྣམས་རྙེད་པར་གྱུར་ན་བཟའ་བར་བྱའམ། ཉེ་བ་འཁོར་བཟའ་བར་བྱ་སྟེ་དུས་ཀྱི་ཕྱིར་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 640]
གཞུང་གཞན་ལས་ཀྱང་ས་གཞི་རུང་བ་ལ་འཚོ་བའི་བར་དུ་བཅང་བའི༌[^374]སྨན་རྙེད་ན་བཟའ་བར་མི་བྱ་འམ། བཀའ་སྩལ་བ་བཟའ་བར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 641]
གཉིས་པོ་འདི་དག་མཉམ་པར་སྦྱར་ནས་འདི་སྐད་ཅེས་གསུངས་སོ། །

[Block 642]
གཞུང་སྔ་མ་ལས་ནང་དུ་ཞག་ལོན་པའི་ཚིག་བྱས་པ་དེ་ལ་གཞུང་ཕྱི་མ་དང་འགལ་བའི་ཕྱིར་ཉམས་པ་ཉིད་དུ་ཤེས་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་འདིར་ནང་དུ་ཞག་ལོན་པ་བཟའ་བར་བྱ་བ་ཉིད་བཀག་པ་ཡིན་ནོ། །

[Block 643]
སྔ་མ་ལ་ཡང་དུས་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་འདི་དང་སྦྱར་བས་ཀྱང་ཉམས་པ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 644]
གང་གི་ཕྱིར་སྔ་དྲོ་ནས་བརྩམས་ཏེ་ཉི་མ་ཡོལ་བའི་མཐར་ཐུག་པ་དེ་དང་དེའི་འོག་ཏུ་དུས་གཞན་ཐུན་མཚམས་ཀྱི་མཐར་ཐུག་པའི་དུས་འདི་དག་ལ་གང་དུ་ལག་ཉར་བླངས་པ་ལ་སོགས་པ་འདི་བྱས་པའི་དུས་དེ་ཉིད་དུ་བཟའ་བར་བྱ་བ་ཡིན་གྱི། དེ་ཚུན་ཆད་དུ་ནི་མ་ཡིན་ཞེས་བྱ་བ་ནི་དུས་ཀྱི་ཕྱིར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 645]
ཉིན་མཚན་གྱི་ཆ་ཐ་མ་ལ་ཡང་གནས་པ་ཉིད་ནི་ཞག་ལོན་པ་ཉིད་ཅེས་བྱ་བར་བརྗོད་དོ། །

[Block 646]
གལ་ཏེ་དེ་ལྟར་ཡིན་ན་གཞུང་ཕྱི་མ་ཡོངས་སུ་སྤངས་པས༌[^375]དུས་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་འདི་དང་མི་ལྡན་པ་ཡོངས་སུ་སྤངས་ནས་ཞག་ལོན་པ་ཉིད་སྤངས་ཚིག་ལྷག་མ་མཛད་དོ་ཞེས་འདིར་མཉམ་པར་སྦྱར་བའོ། །

[Block 647]
འདིར་གཞུང་སྔ་མ་བཟུང་བ་ལས་ནང་དུ་བཙོས་པ་རྣམས་ལ་དེ་དག་དགག་པ་མ་བསྡུས་པ་ཉིད་ཡིན་ནོ། །

[Block 648]
དུས་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་འདི་བསྟན་ཏོ། །

[Block 649]
ཕྱི་མ་ནི་འཚོ་བའི་བར་དུ་བཅང་བ་ཞེས་བྱ་བ་འདི་དང་རྗེན་པར་སྤངས་པ་ཡང་མཛད་པ་ཡིན་ཏེ་དེའི་དོན་ནི་འདི་ཡིན་ནོ། །

[Block 650]
ལག་ཉར་བླངས་པ་ལ་སོགས་པ་རྣམས་བཟའ་བར་བྱའི། དུས་གཞན་དུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དུས་ཀྱི་ཕྱིར་བཟའ་བ་དགག་པར་བྱས་པ་གང་ཡིན་པ་དེ་བཀག་པས་འཚོ་བའི་བར་དུ་བཅང་བ་དག་བསྡུས་པ་ཡིན༌[^376]ནོ། །

[Block 651]
དེ་རྣམས་ཇི་སྐད་བསྟན་པའི་ཆོ་གས་ལག་ཏུ་བླངས་པ་ཇི་སྲིད་འཚོའི༌[^377]བར་དུ་བཟའ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 652]
ལྷག་པར་གནས་པ་རྣམས་ལ་ནི་ཚུལ་འདི་ཡིན་ནོ། །

[Block 653]
ལྷག་པར་མི་གནས་པ་རྣམས་ལ་ནི་དུས་ཀྱི་ཕྱིར་བསྡུས་པ་ཉིད་ཡིན་ནོ། །

[Block 654]
འབགས་པ་ནི་ཟས་ཀྱི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ལ། ལྷུང་བཟེད་ལ་སོགས་པ་ཟས་ལ་སོགས་པས་འབགས་པ་གང་ཡིན་པ་དེ་ནི་ཟས་ཕྱེད་ཉིད་ཡིན་གྱི་ཟས་རྫོགས་པ་ཉིད་ནི་མ་ཡིན་ཏེ། ན་སྨད་པར་བྱས་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 655]
འདི་ནི་བཟའ་བར་གྱུར་པ་ཉིད་ལ་ཐ་སྙད་དུ་གདགས་པ་མ་ཡིན་པ་འདིས་ཤེས་པར་བྱའོ། །

[Block 656]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་ལྷུང་བཟེད་དང་ལྷུང་བཟེད་ཆུང་ངུ་དང་ཁ་གཟར་དང་ཚྭ་ཁུག་དང་ལྷུང་བཟེད་ཀྱི་སྣོད་དང་གོས་དང༌[^378]མེ་ཤེལ་དང་། ཁྲི་དང་ཁྲིའུ་དང་ཁར་བ༌[^379]དང་བུམ་པ་དང་རིལ་བ་དང་ལྡེ་མིག་དང་ལྡེ་མིག་ཀྱོག་པོ་དང༌[^380]གསོག་འཇོག་བྱས་པས་འབགས་པ་ཟ་ན་ཐམས་ཅད་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 657]
འདིར་ཟས་ཀྱི་ཕྱིར་འབགས་པ་སྟེ་ཟོས་ནའོ་ཞེས་བྱ་བའི་ཚིག་སྟེ་རང་ལོངས་སྤྱོད་པའི་ཕྱིར་ནི་མ་ཡིན་ནོ། །

[Block 658]
འདི་རྣམས་ནི་མཐའ་མེད་པར་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་རོ།[^381] །གསོག་འཇོག་གི་མཚན་ཉིད་ལ་དེ་དང་འདྲེས་པའི་ཁ་ཟས་ཟ་བ་ནི་འདིར་དེ་ཡོངས་སུ་ལོངས་སྤྱོད་པར་མངོན་པར་འདོད་པ་ཞེས་བྱ་བར་རྣམ་པར་གཞག་པའོ། །

[Block 659]
ཁ་དྲི་མ་ཅན་གྱིས་བཟའ་བ་དང་བཏུང་བ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ཁའི་ནང་མ་དག་པས་བཟའ་བ་དང་བཏུང་བ་དག་ཟོས་སམ་འཐུངས་ན་དེ་དང་རེག་པས་ཁ་དྲི་མ་ཅན་དུ་གྱུར་པས༌[^382]ཟན་གྱི་ཕྱིར༌[^383]ཉིད་དེ་གཞན་དུ་འཇུག་པར་བྱེད་ན་ལྟུང་བ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 660]
འདིར་གཞུང་ནི་དགེ་སློང་གིས༌[^384]ཁ་མ་བཀྲུས་པར་སྐོམ་འཐུངས་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །ཇི་ཙམ་གྱིས་ནི༌[^385]ཁ་དག་པ་ཡིན་ཞེ་ན། དེའི་ཕྱི་རོལ་ནི་ལྕི་བའམ་སས་ཀུན་ནས་དྲུད༌[^386]དེ་ཆུས་བཤལ་ན་དག་པ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཆུ་གཉིས་ནི་དག་པ་འདིས་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 661]
སིལ་བུ་རྣམས་ལས་འདི་ལ་སོགས་པ་ཡང་དག་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 662]
ནང་ནི༌[^387]ཆུ་མཁུར་བ་དོའམ་གསུམ་གྱིས་བཤལ་ནའོ་ཞེས་བྱ་བ་ནི་ཁའི་ནང་གི་དག་པ་འདི་ཡིན་ནོ། །

[Block 663]
ལྷུང་བཟེད་ནི་བསམ་པ་ཐག་པས་ལན་གཉིས་སམ་ལན་གསུམ་བཀྲུ་བཤལ་བྱས་ན་སྒྲ་མི་སྙན་ཡང་དག་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ལྷུང་བཟེད་ནི་བསམ་པ་ཐག་པས་གུས་པར་བྱ་སྟེ་ལན་གཉིས་ལན་གསུམ་དུ་བསྒྱུར་ལོག་བྱ་ཞིང་ཐོ་རངས་ཀྱི་ཆུ་ལ་སོགས་པས་བཀྲུ་བཤལ་བྱས་ན་སྒྲ་མི་སྙན་ཅིང་སྒྲ་སང་སང་པོ་མ་བྱུང་དུ་ཟིན་ཀྱང་དག་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 664]
རྩི་ལངས་པ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ལ་ཞེས་བྱ་བའི་སྒྲ་འཇུག་པ་ཡིན་ཏེ། ལྷུང་བཟེད་དག་པར་བྱས་པ་ལ་ང༌[^388]ལངས་པ་ནི་རྩི་ལངས་པ་སྟེ། དེ་ལ་ནི་ཉེས་པ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 665]
འབགས་པ་མེད་པར་རེག་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ལྷུང་བཟེད་བཟའ་བར་བྱ་བ་ལ་རེག་ཀྱང་འབགས་པ་མེད་ན་དེ་ལ་ཡང་ཉེས་པ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 666]
ལྕི་སྐམ་མམ་ལྕི་བའམ་ས་གང་ཡང་རུང་བ་ལན་གསུམ་བཀྲུས་པ་ལ་སྣུམ་པ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 667]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་དགེ་སློང་གིས༌[^389]ལྷུང་བཟེད་ལྕི་སྐམ་མམ་ལྕི་བའམ་སས་ལན་གསུམ་འཁྲུ་བར་བགྱིད་ཅིང་དེ་ཡང་སྣུམ་ཞིང་སྣུམ་བག་ཆགས་པར་གྱུར་ན་ཡོངས་སུ་ལོངས་སྤྱད་པར་བགྱི་འམ། ཉེ་བ་འཁོར་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་ཐ་སྙད་དུ་བྱ་བའི་རིན་མི་ཆོག་པའི་ཕྱིར་རོ། །

[Block 668]
འདིར་ལྕི་སྐམ་ལ་སོགས་པ་གསུམ་པོ་འདི་དཔེ་ཙམ་དུ་ཟད་ཀྱི་གཞན་དག་ཀྱང་རུང་བར་རིག་པར་བྱའོ། །

[Block 669]
ལངས་པ་བསལ་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་དེ་ལྷུང་བཟེད་དག་པར་བྱས་པ་ལ་སྣུམ་བག་གམ་ཚོན་རྩིའི་བག་སྐོ་ལ་སོགས་པ་དག་ཕྲད་པས་ལངས་པར་གྱུར་ན་བསལ་བར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 670]
འདིར་གཞུང་ནི་དགེ་སློང་ཞིག་ལ་ལྷུང་བཟེད་འཕྲེན་ཆེན་ཞིག་ཡོད་ནས། དེས་དེར་ཁུ་བ༌[^390]བྱིན་ལེན་བྱས་པ་ན་སྣུམ་བག་འཐོན་ཅིང་སྟེང་དུ་ཞག་ཉ་མིག་ཆགས༌[^391]ཤིང་འདུག་ནས་དགེ་སློང་དེ༌[^392]འགྱོད་པ་སྐྱེས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྟེང་གི་སྣུམ་བསལ་ཏེ་བཏུང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
