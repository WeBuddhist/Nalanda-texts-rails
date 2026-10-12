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
[Block 491]
ཡང་གཞུང་ཁ་ཅིག་ལས་ནི་ཚུལ་དེ་ཉིད་ལས་བཏགས་པ༌[^266]ཡོད་པར་སྨྲ་བའི་སྡེ་པ་དེ་ཐམས་ཅད་ཡོད་པར་སྦྱར་ལ། མང་པོས་བཀུར་བའི་སྡེ་པ་ལ་ནི་གནས་མའི་བུའི༌[^267]སྡེ་པ་དང་། ཀུ་རུ་ཀུ་ལའི་སྡེ་པ་དང་། ས་སྒྲོགས་པའི་སྡེ་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 492]
ཡང་གཞུང་ཁ་ཅིག་ལས།

[Block 493 [VERSE]]
འོད་སྲུངས་ཞེས་བྱ་ཆོས་སྲུང་བ།[^268] །
ས་སྲུང་བ་དང་གཞི་ཀུན་ཡོད། །
ཤར་ནུབ་གངས་རི་བཏགས་པར༌[^269]སྨྲ། །
རྣམ་པར་ཕྱེ་སྨྲ་འཇིག་རྟེན་འདས། །

[Block 494 [VERSE]]
གོས་དམར་ཐོས་མང་སྲུང་བ་པ། །
ཀུ་རུ་ཀུ་ལ་གནས་མའི་བུ། །
རྒྱལ་བྱེད་པ་དང་འཇིགས་མེད་པ། །
གཙུག་ལག་ཁང་པ་ཆེན་པོ་པའོ། །

[Block 495 [VERSE]]
བཞི་དང་དྲུག་དང་ལྔ་དང་གསུམ། །
ཐ་དད་རྣམ་པ་བཅོ་བརྒྱད་འདོད། །
དེ་ལྟར་སྡེ་པ་བཅོ་བརྒྱད་དོ།[^270] །
ཤཱཀྱ་སེང་གེའི་བསྟན་པ་ནི། །

[Block 496 [VERSE]]
གནས་སོ་འགྲོ་བའི་བླ་མ་དེའི། །
སྔོན་གྱི་ཕྲིན་ལས་དབང་གིས་ཡིན། །
ཡུལ་དོན་སློབ་དཔོན་བྱེ་བྲག་དང་། །
ལྟ་བའི་བྱེ་བྲག་ཐ་དད་ཀྱི། །

[Block 497]
རྒྱུ་ཡིས་དེ་དག་ཐ་དད་བྱས། །སྟོན་པ་ཐ་དད་ཡོད་པ་མིན། །

[Block 498]
འདི་དག་གི་ལྟ་བ་དང་། ཚུལ་ཁྲིམས་ཀྱི་རྣམ་པར་གཞག་པ་ནི་གཞུང་ཆེན་པོ་དེ་དང་དེར་བལྟ་བར་བྱའོ། །

[Block 499]
རྩ་བ་ཉིད་བཤད་པར་བྱ་སྟེ། ཚངས་སྤྱོད་ཅེས་བྱ་བ་ནི་ཆང་དང་བུད་མེད་ཀྱི་ཡུལ་སྤངས་པའོ། །

[Block 500]
འདི་ལྟར་ཆང་གི་ཉེས་དམིགས་ཀྱང་ལུང་དེ་དང་དེ་དག་དང་། མདོ་སྡེ་དེ་དང་དེར་བལྟ་བར་བྱའོ། །

[Block 501]
བུད་མེད་ཀྱི་ཉེས་དམིགས་ཀྱང་ཐེག་པ་ཆེན་པོ་དང་ཐེག་པ་ཆུང་བའི་མདོ་དང་ལུང་རྣམས་སུ་བལྟ་བར་བྱ་སྟེ།

[Block 502]
ཇི་སྐད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས༌[^271]འཁྲིག་པ་བདུན་བསྟན་པ་ཞེས་བྱ་བ་ཐེག་པ་ཆུང་བའི་མདོ་ལས།

[Block 503]
བྲམ་ཟེ་འདི་ན་ཁ་ཅིག་བདག་ཚངས་པར་སྤྱོད་པར་ཁས་འཆེ་ཞིང་། བུད་མེད་དང་གཉིས་ཀྱིས༌[^272]གཉིས་སྤྲོད་པ་མེད་ཀྱང་བུད་མེད་ཀྱི་ལུས་ལ་མིག་གིས་བལྟས་ཏེ་དེའི་ཆ་བྱད་ལ་ཞེན་པ་དང་། བུད་མེད་དང་ལྷན་ཅིག་རྩེ་བ་དང་། ཅ་ཅོ་འདོན་པ་ཉམས་སུ་ལེན་པ་དང་། བུད་མེད་ཀྱི་བསྙེན་བཀུར་བྱེད་པ་ཉམས་སུ་ལེན་པ་དང་། རྩིག་པས་ཆོད་པ་དང་། ཡོལ་བས་ཆོད་པའི་བུད་མེད་ཀྱི་རྒྱན་དང་། གླུ་དང་གར་དང་རོལ་མོའི་སྒྲ་ཉམས་སུ་ལེན་པ་དང་། ཕ་རོལ་པོ་འདོད་པའི་ཡོན་ཏན་ལྔ་དང་ལྡན་པ་ལ་བལྟས་ནས་ཉམས་སུ་ལེན་པ་དང་། ལྷ་ལ་སོགས་པའི་གནས་སུ་ཚངས་པར་སྤྱོད་པ་ཡོངས་སུ་བསྔོ་བ་ཡང་དེ་བཞིན་ཏེ། ཚངས་པར་སྤྱོད་པ་ཡོངས་སུ་མ་དག་པའོ་ཞེས་གསུངས་པ་དང་། ཐེག་པ་ཆེན་པོའི་མདོ་ཆོས་བདུན་པ་ལས་ཀྱང་། རྣམ་པར་རྟོག་པས་ཀྱང་འདོད་པ་ལ་བརྟེན་པར་མི་བྱ་ན། གང་དབང་པོ་གཉིས་ཀྱིས༌[^273]སྦྱོར་བ་ལྟ་ཅི་སྨོས་ཞེས་གསུངས་སོ། །

[Block 504]
སྤྱིར་འདོད་པའི་ཉེས་དམིགས་ནི་རྒྱལ་པོ་ཤར་བའི་བུས་ཞུས་པ་དང་། འདོད་པ་ལ་གདམས་པའི་མདོ་ལས་ཤེས་པར་བྱའོ། །

[Block 505]
དེ་བས་ན་ཚངས་པར་སྤྱོད་པ་མ་ཡིན་པར་ཚངས་པར་སྤྱོད་པ་ལྟ་བུར་སྟོན་པ། དགེ་སྦྱོང་གི་རྟགས་དང་མཚན་མས་ང་རྒྱལ་དུ་བྱེད་པས་བྱང་ཆུབ་སེམས་དཔའ་ཁྱིམ་ན་གནས་པ་ཆོས་དང་མཐུན་པའི་སྒྲུབ་པ་དག་ལ༌[^274]རབ་ཏུ་བྱུང་བའོ་སྙམ་དུ་བརྙས་པར་བྱེད་པ། ཚུལ་འཆོས་པ་ཆོམ་རྐུན་ལྟ་བུ་སྟེ། མདོ་ལས་ཆོམ་རྐུན་ཟའོ། །

[Block 506]
ཆོམ་རྐུན་འཐུང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 507]
དེ་ལྟ་བུའི་སྡིག་པ་ཅན༌[^275]དགེ་སློང་དང་། དགེ་ཚུལ་གྱིས་ལྷ་དང་མིའི་མཆོད་རྟེན་དུ་གྱུར་པའི་ངུར་སྨྲིག་གི་གོས་དེ་གཟུང༌[^276]བར་མི་བྱ་སྟེ། ཆོས་གོས་འབར་བ་དང་ལྷུང་བཟེད་འབར་བ་ཞེས་བཤད་དོ། །

[Block 508]
ཇི་སྐད་དུ་ཚུལ་ཁྲིམས་འཆལ་པ་ཚར་གཅོད་པའི་མདོ་ལས།

[Block 509]
ཚུལ་ཁྲིམས་འཆལ་པའི་དགེ་སློང་གིས༌[^277]སྟོན་པའི་ངུར་སྨྲིག་གི་རྒྱལ་མཚན་སེ་གོལ་གཏོགས་པ་ཙམ་དུ་ཡང་བཅང་བར་མི་བྱའོ་ཞེས་གསུངས་པ་དང་། འདིའི༌[^278]ཉེས་དམིགས་ནི་འཕགས་པ་འོད་སྲུངས་ཀྱིས་ཞུས་པའི་མདོ་ལ་སོགས་པ་དེ་དང་དེར་བལྟ་བར་བྱའོ། །

[Block 510]
དེ་འདྲ་བའི་སྡིག་པ་ཅན་གྱི་དགེ་སྦྱོང་ལ་ཐེག་པ་ཆེན་པོའི་བསྟན་པ་དང་། ལམ་ཆེན་པོ་དེ་ལ་གཞུག་པར་མི་བྱའོ་སྙམ་མོ། །

[Block 511]
དེ་ལྟ་བུའི་ཉེས་པས་མ་ཕོག་ཅིང་རྣམ་པར་དག་པ་ནི་ཚངས་སྤྱོད་ཅེས་བྱའོ། །

[Block 512]
དགེ་བསྙེན་དང་དགེ་ཚུལ་དང་དགེ་སློབ་མ་ལས་ཀྱང་ཕུལ་དུ་བྱུང་བས་ན་དགེ་སློང་སྡོམ་པ་དག་ཏུ་བཞེད་ཅེས་སྨྲས་ཏེ། དགེ་སློང་གི་སྡོམ་པ་རྣམ་པར་དག་པ་ནི་ཐེག་པ་ཆེན་པོའི་གཞི་ཕུལ་དུ་བྱུང་ཞིང་ཁྱད་པར་འཕགས་པ་ཡིན་ནོ་ཞེས་བཅོམ་ལྡན་འདས་དེ་ལྟར་བཞེད་དོ། །

[Block 513]
དགེ་སློང་ཞེས་བྱ་བ་ནི་གསོལ་བ་དང་བཞིའི་ལས་ཀྱིས༌[^279]བསྙེན་པར་རྫོགས་པའོ། །

[Block 514]
དེ་ཡང་འདི་ལྟར་ལས་ནི་བཞི་སྟེ། གསོལ་བའི་ལས་དང་། གསོལ་བ་དང་། གཉིས་ཀྱི༌[^280]ལས་དང་། གསོལ་བ་དང་། བཞིའི་ལས་དང་། ལས་གསུམ་བརྗོད་པའི་ལས་སོ། །

[Block 515]
ལས་བཞི་པོ་དེ་དག་ཀྱང་གཞི་གཉིས་ལ་བརྟེན་ཏེ་སེམས་ཅན་དུ་བགྲང་བ་དང་། སེམས་ཅན་མ་ཡིན་པར་བགྲང་བའོ། །

[Block 516]
དེ་ལ་སེམས་ཅན་དུ་བགྲང་བའི་ལས་ནི་རབ་ཏུ་དབྱུང་བ་དང་། བསྙན་པར༌[^281]རྫོགས་པ་དང་། གང་ཟག་ཡིད་མཐུན་པར་བྱ་བ་དང་། ལྟུང་བ་ལས་བསླང་བ་དང་། དགར་བ་དང་། བསྐྲད་པ་དང་། དབྱར་གནས་པར་ཁས་བླངས་པ་དང་། ཞག་བདུན་དང་། ཉི་ཤུ་དང་། བཞི་བཅུར་བྱིན་གྱིས་བརླབ་པ་དང་། སེམས་ཅན་ལ་ཕན་གདགས་པ་དང་། ཆད་པས་གཅད་པའི༌[^282]ལས་གང་ཡིན་པ་དེ་ནི་སེམས་ཅན་དུ་བགྲང་བ་གཞིའི་ལས་ཞེས་བྱའོ། །

[Block 517]
སེམས་ཅན་དུ་བགྲང་བ་མ་ཡིན་པའི་ལས་ནི་ཆོས་གོས་དང་ལྷུང་བཟེད་བྱིན་གྱིས་བརླབ་པ་དང་། སྲ་བརྐྱང་བྱིན་གྱིས་བརླབ་པ་དང་། ཆོས་གོས་རྣམས་ཀྱང་མི་དབུལ་བར་གཟུང་བ་དང་། མཚམས་གཅད་པ་དང་། ཁྱིམ་རུང་བར་ཡིད་མཐུན་པར་བྱ་བ་དང་། དེ་ལྟ་བུ་དང་གཞིའི་ལས་གང་ཡིན་པ་དེ་ནི་སེམས་ཅན་བགྲང་བ་མ་ཡིན་པའི་ལས་སོ། །

[Block 518]
ལས་དེ་དག་ཀྱང་ཚོགས་གཉིས་ཀྱིས་བྱ་བ་དང་། བཞིས་བྱ་བ་དང་། ལྔས་བྱ་བ་དང་། བཅུས་བྱ་བ་དང་། ཉི་ཤུས་བྱ་བ་དང་། ཚོགས་བཞི་བཅུས་བྱ་བ་དང་། དགེ་འདུན་མཐུན་པས་བྱ་བའོ། །

[Block 519]
དེ་ལ་ཚོགས་གཉིས་ཀྱིས་བྱ་བའི་ལས་ནི་དགེ་སློང་གི་དགེ་འདུན་གྱི་མདུན་དུ་ལན་གསུམ་བརྗོད་པའི་བཤགས་པའི་ལས་ཀྱིས་ལྟུང་བྱེད་དམ། ཉེས་བྱས་ཀྱི༌[^283]ཉེས་པ་འཆགས་པར་བྱེད་དོ། །

[Block 520]
བཞིས་བྱ་བ་ནི་ཉེས་པ་སྦོམ་པོ་བཞིའི་མདུན་དུ་བཤགས་པའོ། །

[Block 521]
བཅུས་བྱ་བ་ནི་ཡུལ་དབུས་སུ་བསྙེན་པར་རྫོགས་པའི་ལས་སོ། །

[Block 522]
ཚོགས་ལྔས་བྱ་བ་ནི་མཐའ་འཁོབ་ཏུ་བསྙེན་པར་རྫོགས་པའི་ལས་སོ། །

[Block 523]
ཚོགས་ཉི་ཤུས་བྱས་པའི་ལས་ནི་དགེ་འདུན་ལྷག་མ་ལས་དབྱུང་བའི་ལས་སོ། །

[Block 524]
བཞི་བཅུས་བྱ་བའི་ལས་ནི་དགེ་སློང་མ་བསྙེན་པར་རྫོགས་པར་བྱ་བའི་ལས་སོ། །

[Block 525]
དགེ་འདུན་མཐུན་པས་བྱས་པའི་ལས་ནི་མཚམས་ཀྱི་ལས་དང་། གསོ་སྦྱོང་གི་ལས་དང་། དགག་དབྱེ་དང་གཞན་དེ་ལྟ་བུ་དང་མཐུན་པའི་ལས་སོ། །

[Block 526]
ཐམས་ཅད་ཡོད་པར་སྨྲ་བའི༌[^284]སྡེ་པའི་འདུལ༌[^285]བ་འཛིན་པ་བཙུན་པ་ཆོས་སྐྱོབ་དང་། བཙུན་པ་དབྱངས་སྒྲོགས༌[^286]དང་། བཙུན་པ་དབྱིག་བཤེས༌[^287]དང་། བཙུན་པ་སངས་རྒྱས་ལྷ་དང་། བཙུན་པ་བསམ་རྫོགས་དང་། མཁས་པ་ཆེན་པོ་ནོར་གྱི་རྩ་ལག་དང་། གནས་བརྟན་ཡོན་ཏན་འོད་དང་། བཙུན་པ་ཤཱཀྱ་འོད་ལ་སོགས་པ་དག་ན་རེ། རྣམ་པ་བཅུས་བསྙེན་པར་རྫོགས་ཏེ། རང་བྱུང་བས་ནི་སངས་རྒྱས་དང་རང་སངས་རྒྱས་སོ། །

[Block 527]
ངེས་པར་འཇུག་པ་ནི་རྟེན་ལྔ་པའོ། །

[Block 528]
དགེ་སློང་ཚུར་ཤོག་ཅེས་པས་ནི་གྲགས་པ་ལ་སོགས་པའོ། །

[Block 529]
སྟོན་པར་ཁས་བླངས་པས་ནི་འོད་སྲུངས་ཆེན་པོ་ལ་སོགས་པའོ། །

[Block 530]
དྲི་བས་མཉེས་པ༌[^288]ནི་ལེགས༌[^289]སྦྱིན་ལ་སོགས་པའོ། །
--- END BLOCKS ---
