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
[Block 526]
བསྙེན་པར་རྫོགས་ན་བཟོད་པ་གསོལ་ཟིན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མི་བཟོད་པ་བསྙེན་པར་མ་རྫོགས་པ་རྣམས་བསྙེན་པར་རྫོགས་པ་ཉིད་བཟོད་པ་ཉིད་ཀྱི་ཕྱིར་སླར་བཟོད་པ་གཞན་ནི་བྱ་བ་མ་ཡིན་ནོ། །

[Block 527]
བཟོད་པ་ཞེས་བྱ་བ་ནི་བཟོད་པར་བྱ་བའོ།[^377] །བཙུན་པ་དགེ་སློང་དག་བསྡིགས་པའི་ལས་བགྱིས་ནས་རེ་ཞིག་བསྙེན་པར་རྫོགས་པར་བགྱིད༌[^378]ན་བསྙེན་པར་རྫོགས་ཞེས་བགྱི་འམ། བསྙེན་པར་མ་རྫོགས་ཞེས་བགྱི། ཉེ་བ་འཁོར་བསྙེན་པར་རྫོགས་པ༌[^379]ཞེས་བྱ་སྟེ། བསྙེན་པར་རྫོགས་པར་བྱེད་པ་དག་ལ་ནི་འགལ་ཚབས་ཅན་དུ་འགྱུར་ལ། བཟོད་པ་ནི་གསོལ་ཟིན་པ་ཞེས་བྱ་བའོ་ཞེས་བྱ་བ༌[^380]ནི་གླེང་གཞི་དག་ལས་གསུངས་སོ། །

[Block 528]
གལ་ཏེ་བསྙེན་པར་རྫོགས་ནས་ཁས་མི་ལེན་པ་ནི་ཚོགས་པ་ཡོད་ན་ཡང་ཆད་པས་བཅད་དོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་ནས་ནི༌[^381]འཐབ་ཀྲོལ་མི་བྱེད་པ་ཉིད་ལ་སོགས་པ་རྒྱུ་བཟློག་པ་གལ་ཏེ་ཁས་མི་ལེན་ན་ཚོགས་པ་ཡོད་པ་ན་ཡང་ཆད་པའི་ལས་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 529]
གལ་ཏེ་མ་མཐོང་ངོ་ཞེས་བརྫུན་ཟེར་ན་ལྟུང་བྱེད་དོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་བདག་གིས་མ་མཐོང་ཞེས་བྱ་བ་གལ་ཏེ་བརྫུན་ཟེར་ན་ལྟུང་བར་བྱེད་པ་འདིའི་ལྟུང་བྱེད་དོ། །

[Block 530]
འདི་ལྟ་བུའི་རིགས་ཅན་གྱི་བརྫུན་དུ་སྨྲ་བ་རྣམས་ལ་ལྟུང་བྱེད་མེད་པར་དོགས་པར༌[^382]བྱ་བ་མ་ཡིན་ནོ། །

[Block 531 [VERSE]]
ལག་རྡུམ་དག་དང་རྐང་རྡུམ་དང་། །
ལག་སོར་ཟླུམ་པོར་འཇས་པ༌[^383]དང་། །
མཆུ་མེད་ལུས་ལ་རྨ་མཚན་ཅན། །
རྒན་ཆེས་པ་དང་གཞོན་ཆེས་དང་། །

[Block 532 [VERSE]]
འཐེང་པོ་སྨད་འཆལ་ཞར་བ་དང་། །
ལག་སོར་རྡུམ་རྒུར༌[^384]མིའུ་ཐུང་དང་། །
ལྦ་བ་ལྐུགས་པ་འོན་པ་དང་། །
རྟེན་འཕྱེ་དང་ནི་རྐང་བམ་དང་། །

[Block 533 [VERSE]]
བུད་མེད་ཀྱིས་དུབ་ཁུར་གྱིས་དུབ། །
མི་གང་ལམ་གྱིས་དུབ་རྣམས་དང་། །
ཡ་ཟ་མ་ལུག་གཏའ་གམ་དང་། །
དེ་ལྟ་བུ་ཡི་མི་རྣམས་ནི། །

[Block 534 [VERSE]]
དྲང་སྲོང་ཆེན་པོས་དགག་པར་མཛད། །
མཛེས་པ་རབ་ཏུ་དབྱུང་བ་དང་། །
ཡོངས་སུ་དག་པ་བསྙེན་རྫོགས་པར། །
རྫོགས་སངས་རྒྱས་ཀྱིས་རབ་མཁྱེན་ཏེ། །

[Block 535]
བདེན་པའི་མཚན་གྱིས་བཀའ་སྩལ་ཏོ། །ཞེས་བྱ་བ་ལ། ལག་རྡུམ་ཞེས་བྱ་བ་ནི་ནོར་བུ་འཆིང་བ་ནས་བཟུང་ནས་གང་རྣམས་ཀྱི་ལག་རྡུམ་མོ། །

[Block 536]
རྐང་རྡུམ་ཞེས་བྱ་བ་ནི་གང་རྣམས་ཀྱི༌[^385]ལོང་བུ་མན་ཆད་ཆད་པ་དེ་རྣམས་ནི་རྐང་རྡུམ་མོ། །

[Block 537]
གང་རྣམས་ཀྱི༌[^386]ལག་པའི་སོར་མོ་སྦྲུལ་གྱི་གདེངས་ཀ་འདྲ་བ་དེ་རྣམས་ནི་ལག་སོར་ཟླུམ་པོར་འཇས༌[^387]པའོ། །

[Block 538]
གང་རྣམས་ཀྱི་མཆུ་གཉིས་མེད་པ་དེ་རྣམས་ནི་མཆུ་མེད་པའོ། །

[Block 539]
གང་རྣམས་ཀྱི་ལུས་ལ་རྨ་མཚན༌[^388]ཡོད་པ་དེ་ནི་རྨ་མཚན་ཅན་ཏེ། ལག་པ་ལ་སོགས་པ་བྲིས་པ་ནི་རྨ་མཚན་ཅན་ཡིན་ཏེ་རྒྱུན་གྱིས་བྲབས་པ་དང་འདྲ་བར་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 540]
རྒན་ཆེས་པ་ཞེས་བྱ་བ་ནི༌[^389]བརྒྱ་ལོན་པ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 541]
གཞོན་ཆེས་པ་ཞེས་བྱ་བ་ནི་བྱ་རོག་སྐྲོད་མི་ནུས་པ་ལོ་བདུན་མ་ལོན་པ་རྣམས་སོ། །

[Block 542]
འཐེང་པོ་ནི་རྐང་པ་འཐིང་ཞིང་འགྲོ་བ་རྣམས་སོ། །

[Block 543]
སྨད་འཆལ་བ་ནི་བརླའི་ཕྱོགས་སུ་རླུང་བྱ་རྒོད་འགྲོས་ཀྱིས༌[^390]ཀུན་དུ་ཉམས་པར་གྱུར་པའོ། །

[Block 544]
ཞར་བ་ནི་མིག་ཡ་གཅིག་པའོ། །

[Block 545]
སོར་མོ་རྡུམ་པ་ནི་གང་གི་མཁྲིག༌[^391]མའི་ཕྱོགས་ན་མཚན་མ་ཙམ་གྱི་ལག་པ་ཡོད་ཅིང་ཅུང་ཟད་ཀྱང་བྱེད་མི་ནུས་པའོ། །

[Block 546]
ལྦ་བ་ཅན་ནི་མགྲིན་པ་ལྦ་བ་ཅན་གང་ལ་ཡོད་པ་དེ་ནི་ལྦ་བ་ཅན་ནོ། །

[Block 547]
ལྐུགས་པ་ནི་སྨྲ་མི་ནུས་པའོ། །

[Block 548]
རྟེན་འཕྱེ༌[^392]ནི་གང་རྟེན་དག་ལ་ལག་པ་གཉིས་སོ་སོར་བཞག་ནས་གཟུགས་བཞིས་ཕྱེ༌[^393]བའོ། །

[Block 549]
མིང་གཉིས་པ་ནི་གྲུམ་པོ་ཞེས་ཀྱང་བྱའོ། །

[Block 550]
བུད་མེད་ཀྱིས་དུབ་པ་ནི་བུད་མེད་རྣམས་ཤས་ཆེར་བསྟེན་པས་སྟོབས་ཟད་པ་སྟེ། གང་གི་ལུས་མི་བདེ་བ་བུད་མེད་ཀྱིས་དུབ་པའོ། །

[Block 551]
དེ་བཞིན་དུ་མི་བཟོད་པའི་ཁུར་ཐོགས་པའི་ཕྱིར་དང་། ལམ་དུ་འགྲོ་བ་དྲགས་པའི་ཕྱིར་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཁུར་གྱིས་དུབ་པ་དང་ལམ་གྱིས་དུབ་པ་རྣམས་སོ། །

[Block 552]
ཡ་ཟ་མ་ལུག་ནི་གང་རྣམས་ཀྱིས་ཇི་ལྟར་ཟོས་པ་དག་མ་ཞུ་བ་ཕྱིར་འབྱུང་བའོ། །

[Block 553]
ཁ་ཅིག་ནི་འདི་སྐད་ཅེས་ཟེར་ཏེ་གང་གིས་འགྲོ་བ་བཅིངས་པས་ཉམས་པ་བཅིངས་པ་ལས་གྲོལ༌[^394]ཡང་བཅིང་པ༌[^395]བཞིན་དུ་ཡོངས་སུ་འགྲོ་བར་བྱེད་པ་དང་། གང་རྣམས་ལང་ཚོ་ལ་བབ་པ་ཁོ་ནར་ནད་ལ་སོགས་པས་དེ་ལྟར་མི་ནུས་པ་ཉིད་བྱས་པ་མཐུག་པ་དང་རབ་ཏུ་སྟོབས་དང་ལྡན་པའི༌[^396]རྒས་པས་ཉེ་བར་གདུངས་པ་ལྟར་བྱ་བ་ཐམས་ཅད་མི་ནུས་པ་དེ་རྣམས་ནི་གཏའ་གམ་སྟེ། འབྱུང་བ་བཞིན་དུ་དེ་རྣམས་ཀྱི༌[^397]ལང་ཚོ་མ་ཉམས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 554]
བསྡུ་བར་བྱ་བའི་སྐབས་རྫོགས་ཏེ། རབ་ཏུ་བྱུང་བའི་གཞི་རྫོགས་སོ།། །།

[Block 555]
བཀོལ་བ་རྒྱལ་པོས་བཀྲབས་པའོ། །

[Block 556]
རྒྱལ་པོས་མ་གནང་བ་ཡུལ་ཐག་མི་རིང་བའོ་ཞེས་བྱ་བ་ལ། ཁྱོད་རྒྱལ་པོས་བཀྲབས་པ་མ་ཡིན་ནམ་ཞེས་བྱ་བ་རབ་ཏུ་འབྱུང་བ་ཉིད་ཉེ་བར་འོངས་པ་ལ༌[^398]དྲི་བར་བྱ་སྟེ། བསྙེན་པར་རྫོགས་པར་བྱེད་པ་རྣམས་ཀྱིས་ཀྱང་རྒྱལ་པོས་བཀྲབས་པ་རྒྱལ་པོས་མ་གནང་བ་ཡུལ་ཐག་མི་རིང་བ་ཉིད༌[^399]རབ་ཏུ་དབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་མི་བྱ་ཞེས་བྱ་བའོ། །

[Block 557]
གང་ཞིག་རབ་ཏུ་བྱུང་བའི་གཞི་ལ་མ་བཟུང་བ་དེ་ལ་འདིས་སྟོན་པར་བྱེད་པའོ། །

[Block 558]
གང་ཞིག་རྒྱལ་པོ་དེའམ་དེའི་རྗེ་བོ་ལ་རྣམ་པར་རྒྱལ་བ་དེ་དེ་ལས་གང་ཡང་རུང་བའི་གྲོགས་པོ་ལ་གང་ཞིག་དེའི་ཚིག་གིས་འབྲེལ་པ་དེ་ནི་འདིར་ཡུལ་ཐག་མི་རིང་བའོ། །

[Block 559]
བཀོལ་པ་ཆོམ་རྐུན་པར་གྲགས་པའོ་ཞེས་བྱ་བ་ནི་རྒྱལ་པོས་མ་གནང་བ་ཡུལ་ཐག་མི་རིང་བ་ཞེས་བྱ་བ་འདི་བཟློག་པའི་དོན་དུ་སླར་བཀོལ་བའི་ཚིག་སྟེ། ཁྱོད་ཆོམ་རྐུན་པར་གྲགས་པ་མ་ཡིན་ནམ་ཞེས་བྱ་བ་རབ་ཏུ་འབྱུང་བའི་དོན་དུ་ཉེ་བར་འོངས་པ་ལ་དྲི་བར་བྱ་ཞིང་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་རྣམས་ཀྱིས་ཀྱང་དྲི་བར་བྱ་སྟེ། ཆོམ་རྐུན་པར་གྲགས་པ་རབ་ཏུ་དབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་མི་བྱའོ། །

[Block 560]
ཆོ་ག་འདི་ཙམ་ཉིད་ཀྱིས་འདིར་འབྱུང་བའོ། །

[Block 561]
ཆོམ་རྐུན་པར་གྲགས་པ་ནི་རྒྱལ་མཚན་བཅིངས་པའོ། །

[Block 562]
གང་དུ་གང་ལ་རབ་ཏུ་གྲགས་པར་གྱུར་པ་ཉིད་མ་ཡིན་པ་དེར་དེ་ལ་རྒྱལ་མཚན་བཅིངས་པ་ཉིད་དོ། །

[Block 563]
ཤིང་རྟ་བྱེད་པ་དང་། ལྷམ་མཁན་དང་། གདོལ་པ་དང་། གཡུང་པོ་དང་། དེ་ལྟ་བུ་རབ་ཏུ་དབྱུང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། ཤིང་རྟ་བྱེད་པ་ནི་ལྷམ་མཁན་ནོ། །

[Block 564]
དེ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་ཟན་བཟའ་བར་མི་བྱ་བ་སྟེ། དགེ་ཚུལ་ཉིད་དང་སློབ་པ་ཉིད་ཀྱིས་བསྙེན་པར་རྫོགས་པར་འོས་པ་མ་ཡིན་པ་ཉིད་ཤིང་རྟ་མཁན་ལ་སོགས་པ་རྣམས་ལ་རབ་ཏུ་དབྱུང་བ་མ་ཡིན་པ་ཉིད་ཀྱི་རྒྱུ་མཚན་ནོ། །

[Block 565]
དེ་བས་ན་འདི་རྣམས་ལ་ཡང་མི་བྱ་བ་ཉིད་དུ་སྟོན་པའོ། །
--- END BLOCKS ---
