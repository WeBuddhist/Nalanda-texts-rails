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
[Block 701]
དེ་དང་འབྲེལ་པའི་རྒྱུན་གྱིས་རེག་པ་ནི་དེ་ལ་རེག་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་དང་འབྲེལ་པའི་རྒྱུན་ལ་རེག་པ་དེ་འོ་མ་ལ་སོགས་པ་དེ་ལ་དེར་རེག་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 702]
ནོར་བ་དང་བརྗེད་པས་ཀྱང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རེག་པ་ལ་རེག་པ་ཉིད་དོ། །

[Block 703]
དེ་གཉིས་ཀྱིས་སྤོས་པ་གཞག་པའི་ཕྱིར་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ནོར་བ་དང་བརྗེད་པ་དེ་ཉིད་ཀྱིས་སྤོས་པ་ཕྱིར་གཞག་པར་བྱ་བའི་དོན་དུ་རེག་པ་ཡང་རེག་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 704]
གནས་ཀྱི་ཐག་ཤིན་ཏུ་ཉེ་བར་བསྐུར་རོ་ཞེས་བྱ་བ་ནི་གནས་གང་དུ་བར་སྐབས་ཀྱི་ཐག་ཤིན་ཏུ་ཉེ་བ་ཡོད་པ་དེར་སྤོང་བ་ལ་ཉེ་བར་བསྐུར་བར་བྱའོ། །

[Block 705]
གནས་ཀྱི་ཐག་ཤིན་དུ་རིང་བར་ཁྱེར་ན་དེ་ལ་རྗེས་སུ་གནང་བ་ཉིད་ཀྱི་ཕྱིར་རེག་པ་ཉིད་ཤེས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ཤེས་པར་བྱའོ། །

[Block 706]
གཡེལ་བས་ལག་ཉར་བླངས་པ་ཉིད་དང་བྱིན་ལེན་བླངས་པ་ཉིད་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། གཡེལ་བས་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་འདུལ་བ་ལ་མ་མོས་པའམ་དེ་ཉིད་ལ་ཐེ་ཚོམ་དུ་བྱེད་ཅིང་འཛིན་ལ་ལག་ཏུ་ལེན་པ་དག་འབྱུང་བ་མ་ཡིན་ནོ། །

[Block 707]
འདིར་གཞུང་ནི་ངོ་ཚ་མེད་པ་དང་གཡེལ་བས་ཞེས་བྱ་བ་འདི་གསུངས་སྟེ། གང་ཞིག་གཡེལ་བས་འབྱུང་ཞིང་རྒྱལ་མཚན་དེ་འཛིན་པ་དེ་ནི་འདིར་ངོ་ཚ་མེད་པ་ཉིད་དུ་མངོན་པར་འདོད་པ་རྣམ་པར་གནས་པ་ཡིན་གྱི་ཕམ་པ་བྱུང་བ༌[^413]ནི་མ་ཡིན་ནོ། །

[Block 708]
དེ་བས་ན་དེ་ལ་འདིར་བཟུང་བར་མ་མཛད་དོ། །

[Block 709]
བྱིན་ལེན་སྟོབས་པར༌[^414]འོས་པ་དང༌[^415]འབྲེལ་པ་མ་བྲལ་བའི་བླང་བ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བཟའ་བར་བྱ་བ་གང་ལ་བྱིན་ལེན་དེ་སྟོབས་པར་འོས་པའི་གང་ཟག་དང་འབྲེལ་པ་གང་ཡིན་པ་དེ་དང་ཇི་སྲིད་དུ་མ་བྲལ་བ་དེའི་བླང་བ་ཡང་ལག་ཉར་བླངས་པ་ཉིད་ཀྱང་མ་ཡིན་ལ་བྱིན་ལེན་བྱས་པ་ཉིད་ཀྱང་མ་ཡིན་ནོ། །

[Block 710]
དེས་གཟུང་བའི༌[^416]ཐག་པ་ལ་དང་འབྲེལ་པ་ཉིད༌[^417]ནི་འབྲེལ་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེས་ཞེས༌[^418]བྱ་བ་ནི་བྱིན་ལེན་སྟོབས་པར་འོས་པས་སོ། །

[Block 711]
གཟུང་བའི༌[^419]ཞེས་བྱ་བ་ནི། གང་ཞིག་དེ་ཐག་པ་ལ་སོགས་པ་དེ་དང་ཟས་སུ་འབྲེལ་པ་ཉིད་ཡིན་ན་བྱིན་ལེན་སྟོབས་པར་འོས་པའི་ཟས་དང་འབྲེལ་པ་ཉིད་ཡིན་ནོ། །

[Block 712]
སྡོམ་པས་མཉམ་པ་ལྟ་བ་ཐ་མི་དད་པ་དག་གིས་གསོག་འཇོག་བྱས་པ་དང་། བྱིན་ལེན་བྱས་པ་དང་ལག་ཉར་བླངས་པ་དག་ནི་གཅིག་པ་ཉིད༌[^420]ཡིན་ནོ་ཞེས་བྱ་བ་ནི།

[Block 713]
ལྟ་བ་ཐ་དད་པའི་ཕྱིར་འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 714]
བཙུན་པ་རྗེས་སུ་ཁས་མ་བླངས་པས་བྱིན་ལེན་བགྱིས་པ་འཚལ་བར་བགྱི་འམ་ཉེ་བ་འཁོར་མི་བྱའོ། །

[Block 715]
བཙུན་པ་རྗེས་སུ་ཁས་བླངས་པས༌[^421]བྱིན་ལེན་བགྱིས་པ་འཚལ་བར་བགྱི་འམ། ཉེ་བ་འཁོར་མི་བྱའོ་ཞེས་བྱ་བ་འདི་ནི་ལྟ་བ་ཐ་མི་དད་པ་དག་གིས་ཞེས་བྱ་བ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 716]
མཆོག་དང་མཆོག་མ་ཡིན་པར་རོ་ཞེས་བྱ་བ་ལ། མཆོག་དང་ཞེས་བྱ་བ་ནི་སྡོམ་པ་མཆོག་དང་ལྡན་པ་དེས་གཞན་ལ་སྡོམ་པ་གཅིག་པ་ཉིད་དེ་གཞན་དམན་པ་གང་ཡིན་པ་དེ་ནི་དེས་གཞན་མཆོག་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 717]
དགེ་སློང་མའི་གསོག་འཇོག་བྱས་པ་ནི་དགེ་སློབ་མ་དང་བསླབ་པ་བྱིན་པ་མོས་ཀྱང་གསོག་འཇོག་བྱས་པ་ཉིད་ལ་དེ་གཉིས་ཀྱིས་གསོག་འཇོག་བྱས་པ་ནི་དགེ་སློང་མས་གསོག་འཇོག་བྱས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 718]
སྐྱེས་པ་དང་བུད་མེད་དག་ནི་ཕན་ཚུན་ཁྱིམ་པ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི། དཔེར་ན་ཁྱིམ་པས་ལག་ཉར་བླངས་པ་དང་བྱིན་ལེན་བྱས་པ་དང་གསོག་འཇོག་བྱས་པ་དགེ་སློང་ལ་སོགས་པའི་ལག་ཉར་བླངས་པ་དང་བྱིན་ལེན་བྱས་པ་དང་། གསོག་འཇོག་བྱས་པ་ཉིད་མ་ཡིན་པ་དེ་བཞིན་དུ་དགེ་སློང་དང་དགེ་སློང་མ་དང་བསླབ་པ་བྱིན་པས་ཀྱང་དགེ་སློང་དང་དགེ་སློང་མ་དང་བསླབ་པ་བྱིན་པ་མོ་དང་དགེ་སློང༌[^422]མ་རྣམས་ཀྱི༌[^423]མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 719]
དགེ་ཚུལ་དག་གི༌[^424]ལ་རེག་པ་ནས་སྦེད་པའི་བར་ལ་ཉེས་པར་མི་འགྱུར་བ་ནི་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ལ། རེག་པ་ནས་སྦེད་པའི་བར་ལ་ཞེས་བྱ་བ་ནི་དེ་ལ་རེག་པ་ནས་སྦེད་པའི་བདག་ཉིད་ཀྱི་རེག་པའི་བར་ལའོ། །

[Block 720]
ཉེས་པར་མི་འགྱུར་བ་ནི་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི། གང་གིས༌[^425]ལག་ཉར་བླངས་པ་ལ་སོགས་པའི༌[^426]ཉེས་པར་མི་འགྱུར་བ་དེ་བཞིན་དུ་དགེ་ཚུལ་དབང་བ་གང་ཡིན་པ་དེ་དགེ་སློང་གིས་སྦེད་པར་བྱེད་དུ་ཟིན་ཀྱང་དེས་དགེ་སློང་དེ་ཉིད་དང་དགེ་སློང་གཞན་གང་ལ་རུང་བ་མ་ཡིན་པ་ཉིད་དུ་མི་འགྱུར་ལ། དགེ་ཚུལ་མ་དབང་བ་གང་ཡིན་པ་དེ་དགེ་སློང་མས་སྦེད་པར་བྱེད་དུ་ཟིན་ཀྱང་དེས་དགེ་སློང་མ་དེ་ཉིད་དང་དགེ་སློང་མ་གཞན་དག་ལ་རུང་བ་མ་ཡིན་པ་ཉིད་དུ་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 721]
འདི་དགེ་ཚུལ་གྱི་ཡིན་པས་ན་དགེ་ཚུལ་གྱིའོ། །

[Block 722]
ལྟོས་པ་དང་བཅས་པས་བྱིན་པ་ནི་བཏང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ལག་ཉར་བླངས་པ་ལ་སོགས་པ་ལ༌[^427]ལྟོས་པ་དང་བཅས་པས་གཞན་ལ་སྟེར་ན་དེས་དེ་ཟ་བ་ལ་ལག་ཉར་བླངས་པ་ཉིད་དང་གསོག་འཇོག་གི༌[^428]ཕྱེད་ཉིད་དེ་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 723]
ལྟོས་པ་མེད་པར་བཏང་བ་ལ་ལྟོས་པ་དང་བཅས་པ་ཉིད་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གསོག་འཇོག་དང་ལག་ཉར་བླངས་པ༌[^429]ལ་སོགས་པ་ལ་ལྟོས་པ་མེད་པར་བཏང་བ་ལ་ལྟོས་པ་དང་བཅས་པ་ཡོད་ན་བྱིན་ལེན་བྱ་བ་དང་བཟའ་བ་ལ་ཕྱེད་ཉིད་དེ་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 724]
དེའི་ཕྱིར་དེ་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་ལྟོས་པ་མེད་པར་གཏང་པ་དེ༌[^430]ནི་ལྟོས་པ་དང་བཅས་པ་ཉིད་ཀྱི་ཕྱེད་ཉིད་ཡིན་པ་དེ་བས་ན་འདི་བླང་བར་མི་བྱ་སྟེ། བཟའ་བའི་དོན་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 725]
གང་གི་ཕྱིར་བླངས་པ་ལ་ངེས་པར་ལྟོས་པ་དང་བཅས་པ་ཉིད་སྐྱེ་བ་ཡིན་ནོ། །ཤེས་བཞིན་དུ་མི་བླང་ངོ་ཞེས་བྱ་བ་ནི་ལྟོས་པ་མེད་པར་གཏད་པ་དེ་ཤེས་བཞིན་དུ་ཕྱིར་བླངས་ན་རྟོགས་པ་དང་བཅས་པ་ཉིད་དུ་འགྱུར་ལ། མི་ཤེས་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 726]
དེ་བས་ན༌[^431]ཤེས་བཞིན་དུ་བླང་བར་མི་བྱའོ། །

[Block 727]
མི་ཤེས་པས་བླངས་པ་ལ་ནི་ཉེས་པ་མེད་དོ། །

[Block 728]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་ཀུན་དགའ་ར་བ༌[^432]འམ་དགེ་ཚུལ་ལ་ཟས་བརྩལ་བ་དེ་གཉིས་ཀྱི་དེ་ཉིད་ལ་སླར་བརྩལ་ན་འཚལ་བར་བགྱི་འམ། གལ་ཏེ་མངོན་པར་མ་བསམས་ན་བཟའ་བར་བྱའོ། །

[Block 729]
བླང་བར་བགྱིའམ་ཉེ་བ་འཁོར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 730]
མངོན་པར་མ་བསམས་ན་ཞེས་བྱ་བ་ནི་འཐོབ་བོ་སྙམ་དུ་ཡིད་ཀྱིས་མ་བསམས་ནའོ། །

[Block 731]
གླེང་གཞི་དག་ལས་ཀྱང་ལྟོས་པ་དང་བཅས་པས༌[^433]ཟོས་ནའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 732]
ཤས་མནོད་པ་དང་དེ་འགུགས་པའི་ཕྱིར་རེག་པ་ནི་རྐྱེན་དེ་ལྟ་བུ་དག་ཡོད་ན་རུང་བ་མ་ཡིན་པ་ཉིད་དུ་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ལ། ཤས་མནོད་པ་ཞེས་བྱ་བ་ནི་སྐལ་བ་སློང་བའོ། །

[Block 733]
བཀུག་པར་འགྱུར་བ༌[^434]ནི་འདི་གཙུག་ལག་ཁང་དུ་ཁྱེར་བ་བྱེད་པ་ཉིད་ཅེས་བྱ་བ་སྐལ་བ་ལེན་པ་གསུངས་པ་གང་ཡིན་པ་དེ་ལ་རེག་པ་ལ་མི་རུང་བ་ཉིད་ནི་མ་ཡིན་ནོ། །ཅི་དུས་ཐམས་ཅད་དུ་འམ་ཞེ་ན། མ་ཡིན་ཞེས་བྱ་བ་བསྟན་པ་ནི་དེའི་ཕྱིར་རྐྱེན་དེ་ལྟ་བུ་དག་ཡོད་ན་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྙེན་པར་མ་རྫོགས་པ་དག་མེད་པའམ་ནད་པ་ཉིད་ལ་གྲུ་དང་ཤིང་རྟ་གནས་པ་ལ་སྦྱར་བ་འདི་དག་ལ་གཞན་མེད་པ་ལ་གྲོགས་བྱེད་པ་པོ་དང་གྲོགས་བྱེད་པ་ལ་ཞུགས་པ་གཞན་མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 734]
ཤིང་རྟ་ལ་ནི་ཁ་ལོ་བའི་སྟན་མ་གཏོགས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདི་དག་ཐམས་ཅད་ཀྱང་རྐྱེན་དེ་ལྟ་བུ་དག་ཡོད་པ༌[^435]ན་ཞེས་བྱ་བའི་རྗེས་སུ་སྦྱར་བར༌[^436]རིག་པར་བྱའོ། །

[Block 735]
རྐྱེན་དེ་ལྟ་བུ་རྣམས་ནི་ཤིང་རྟ་བསྐུལ་བར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིར་གསུངས་སོ། །

[Block 736]
མི་བྱ་བར་བརྗོད་པ་ཙམ་དུ་ཟད་པ་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 737]
བཟའ་བར་བྱ་བ་ནང་དུ་བཅུག་པའི་ཤིང་རྟ་ནི་རེག་པར་བྱ་བ་ཉིད་མ་ཡིན་ཏེ། མི་རེག་ཏུ་མི་རུང་བའི་རྐྱེན་དེ་ལྟ་བུ་དག་ཡོད་ན་དེའི་ཚེ་ཡང༌[^437]ཁ་ལོ་བའི་སྟན་གཅིག་པོ་སྟེ༌[^438]གཏོགས་པའི་ཤིང་རྟ་ལ་རེག་པར་བྱའོ། །

[Block 738]
འདིར་ཤིང་རྟ་ལ་རེག་པ་ལ་མི༌[^439]རུང་བ་ཉིད་ནི་མ་ཡིན་ཏེ། ཤིང་རྟ་དང་འབྲེལ༌[^440]པའི་ཟས་སུ་བྱ་བ་ལ་འདི་བསྟན་པའོ། །

[Block 739]
གང་བ༌[^441]ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འབྲས་ལ་སོགས་པས་ཁ་ལོ་བའི་སྟན་གྱིས་ཤིང་རྟ་ཉིད་སྤངས་པ་ཉིད་དོ། །

[Block 740]
ནད་པ་ཞོན་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཟས་ཀྱིས༌[^442]སྟོང་པའི་ཤིང་རྟ་དག༌[^443]ཡང་ཁ་ལོ་བའི་སྟན་སྤངས་པ་ཉིད་ཁོ་ནའོ། །
--- END BLOCKS ---
