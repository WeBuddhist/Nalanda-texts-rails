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
[Block 596]
མདོ་ལས་དགེ་སློང་དག་སྲོག་གཅོད་པ་ནི་རྣམ་པ་གསུམ་སྟེ། ཆགས་པ་ལས་སྐྱེས་པ་དང་། ཞེ་སྡང་ལས་སྐྱེས་པ་དང་། གཏི་མུག་ལས་སྐྱེས་པའོ་ཞེས་བྱ་བ་ནས་ལོག་པར་ལྟ་བའི་བར་དུ་གསུངས་པ་དེ་ལ་སྲོག་གཅོད་པ་ཆགས་པ་ལས་སྐྱེས་པ་ནི་ཅི་འདྲ་བ་ཞིག་ཅེས་བྱ་བ་དེ་ལ་སོགས་པ་བརྗོད་པར་བྱ་སྟེ། འདི་ལ་ལས་ཀྱི་ལམ་ཐམས་ཅད་ཆགས་པ་ལ་སོགས་པས་མཐར་ཕྱིན་པར་བྱེད་པ་ནི་མ་ཡིན་གྱི། སྦྱོར་བ་རྩ་བ་གསུམ་ལས༌[^421]སྐྱེས། །དེ་དག་གི་སྦྱོར་བ་ནི་མི་དགེ་བའི་རྩ་བ་གསུམ་ལས་སྐྱེས་པ་ཡིན་པས་ན་དང་པོ༌[^422]ཀུན་ནས་སློང་བའི་ཚིག་ལས་དེ་སྐད་བཤད་དོ། །

[Block 597]
དེ་ལ་སྲོག་གཅོད་པ་ཆགས་པ་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ། དེའི་ལུས༌[^423]ཀྱི་ཡན་ལག་གི་ཕྱིར་རམ། ནོར་གྱི་ཕྱིར་རམ། རྩེད་མོའི་ཕྱིར་རམ། བདག་གམ་མཛའ་བོ་ཡོངས་སུ་བསྐྱབ་པའི་ཕྱིར༌[^424]སྲོག་གཅོད་པར་བྱེད་པའོ། །

[Block 598]
ཞེ་སྡང་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ། ཁོན་ལས་ངེས་པར་འབྱུང་བར་བྱ་བའི་ཕྱིར་གསོད་པར་བྱེད་པའོ། །

[Block 599]
གཏི་མུག་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ། མཆོད་སྦྱིན་བྱེད་པ་རྣམས་དང་། རྒྱལ་པོས་ཆོས་འདོན་པ་ཚད་མར་བྱས་ནས་ཆོས་ཀྱི་བློས་གསོད་པ་དག་སྟེ། མི་བསྒྲུངས་པ་རྣམས་ཆད་པས་བཅད་ན། རྒྱལ་པོ་བསོད་ནམས་ཀྱི་སྣོད་དུ་འགྱུར་རོ་ཞེས་གྲགས་པ༌[^425]ལྟ་བུ་དང་། པར་སིག་པ་རྣམས་ཀྱི་ལྟ་བུ་སྟེ། དེ་དག་ནི་འདི་སྐད་དུ། ཕ་དང་མ་རྒས་སམ་ནད་ཚབས་ཆེན་པོས་ཐེབས་ན་གསད་པར༌[^426]བྱའོ་ཞེས་ཟེར་རོ། །

[Block 600]
གང་ཡང་འདི་སྐད་དུ་སྦྲུལ་དང་སྡིག་པ་དང་སྦྲང་བུ་ཏྲྱ༌[^427]མ་བུ་ཀ་ལ་སོགས་པ་རྣམས་ནི་མི་རྣམས་ལ་གདུང་བར་བྱེད་པ་ཡིན་པས་གསད་པར༌[^428]བྱའོ། །

[Block 601]
རི་དགས་དང་ཕྱུགས་དང་བྱ་དང་མ་ཧེ་ལ་སོགས་པ་རྣམས་ནི་ལོངས་སྤྱོད་པར་བྱ་བའི་ཕྱིར་གསད་པར་བྱའོ་ཞེས་ཟེར་བ་དང་། གང་ཡང་ལོག་པར་ལྟ་བས་རབ་ཏུ་བཅུག་པའི་སྲོག་གཅོད་པའོ། །

[Block 602]
མ་བྱིན་པར་ལེན་པ་ཆགས་པ་ལས་སྐྱེས་པ་ནི་གང་ཞིག་གང་དོན་དུ་གཉེར་བ་དེས་འཕྲོག་པའམ། གཞན་གྱི་རྙེད་པའམ་བཀུར་སྟིའམ༌[^429]གྲགས་པའི་ཕྱིར་རམ། བདག་གམ་མཛའ་བོ་ཡོངས་སུ་བསྐྱབ་པའི་ཕྱིར་འཕྲོག་པའོ། །

[Block 603]
ཞེ་སྡང་ལས་སྐྱེས་པ་ནི་ཁོ་ན་ལས་ངེས་པར་འབྱུང་བར་བྱ་བའི་ཕྱིར་འཕྲོག་པ་གང་ཡིན་པའོ། །

[Block 604]
གཏི་མུག་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ་རྒྱལ་པོས་ཆོས་འདོན་པ་ཚད་མར་བྱས་ནས་མི་བསྒྲུངས་པ༌[^430]ཆད་པས་བཅད་པའི་ཕྱིར་འཕྲོག་པ་ལྟ་བུ་དང་། འདི་ལྟ་སྟེ། བྲམ་ཟེ་རྣམས་ན་རེ་འདི་ཐམས་ཅད་ནི་ཚངས་པས་བྲམ་ཟེ་རྣམས་ལ་བྱིན་པ་ཡིན་ན་བྲམ་ཟེ་རྣམས་དམས་པས་དམངས་རིགས་རྣམས་ཡོངས་སུ་སྤྱོད་པར་ཟད་དེ། [^431]དེ་ལྟ་བས་ན་བྲམ་ཟེ་འཕྲོག་པ༌[^432]ན་བྲམ་ཟེ་བདག་ཉིད་ཀྱིས་ལེན་པ་ཡིན། བདག་ཉིད་ཀྱིས༌[^433]ཟ་བ་ཡིན། བདག་ཉིད་ཀྱིས༌[^434]གྱོན་པ་ཡིན། བདག་ཉིད་ཀྱིས༌[^435]སྦྱིན་པ་ཡིན་ནོ་ཞེས་ཟེར་བ་ལྟ་བུའོ། །

[Block 605]
དེ་དག་ལ་བདག་དང༌[^436]གཞན་གྱི་འདུ་ཤེས་མི་འབྱུང་བ་ནི་མ་ཡིན་ནོ། །

[Block 606]
གང་ཡང་ལོག་པར་ལྟ་བས་རབ་ཏུ་བཅུག་པའི་མ་བྱིན་པར་ལེན་པའོ། །

[Block 607]
འདོད་པས་ལོག་པར་གཡེམ་པ་ཆགས་པ་ལས་སྐྱེས་པ་ནི་གཞན་གྱི་ཆུང་མ་ལ་སོགས་པ་ལ་དེ་ལ་ཆགས་པའམ། རྙེད་པ་འམ་བཀུར་སྟིའི་ཕྱིར་རམ། བདག་གམ་མཛའ་བོ་ཡོངས་སུ་བསྐྱབ་པའི་ཕྱིར་མི་ཚངས་པར་སྤྱོད་པའོ། །

[Block 608]
ཞེ་སྡང་ལས་སྐྱེས་པ་ནི་ཁོན་ལས་ངེས་པར་འབྱུང་བར་བྱ་བའི་ཕྱིར་ཉལ་པོ་བྱེད་པ་གང་ཡིན་པའོ། །

[Block 609]
གཏི་མུག་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ། པར་སིག༌[^437]ལ་སོགས་པ་མ་ལ་སོགས་པ་ལ་ཉལ་བ་དང་། བ་ལང་འབྲིང༌[^438]གི་མཆོད་སྦྱིན་ལ་ཆོ་ག་ཅན་གྱི་ཆུ་བཏུང་ངོ་། །རྩྭ་བཅད་དོ། །

[Block 610]
མའི་གན་དུ་ཉལ་པོ་ལ་འགྲོའོ། །

[Block 611]
སྲིང་མོའི་གན་དུ་འགྲོའོ། །

[Block 612]
རུས་གཅིག་པའི་གན་དུ་འགྲོའོ་ཞེས་བྱ་བ་དང་། གང་དང་གང་ན་འདི་དག་རྙེད་པ་དེ་དང་དེར་འགྲོ་བར་བྱ་སྟེ། དེ་ལྟ་བས༌[^439]ན་བ་ལང་དང༌[^440]འཇིག་རྟེན་ལས་རྒྱལ་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ལྟ་བུ་དང་། གང་དག་བུད་མེད་ནི་གཏུན་དང་། མེ་ཏོག་དང་། འབྲས་བུ་དང་། ཟས་སྨིན་པ་དང་། ངོགས་དང་ལམ་དང་འདྲའོ་ཞེས་ཟེར་བ་ལྟ་བུའོ། །

[Block 613]
བརྫུན་དུ་སྨྲ་བ་ལ་སོགས་པ་ཆགས་པ་ལས་སྐྱེས་པ་དང་། ཞེ་སྡང་ལས་སྐྱེས་པ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 614]
བརྫུན་དུ་སྨྲ་བ་གཏི་མུག་ལས་སྐྱེས་པ་ནི༌[^441]ཇི་སྐད་དུ།

[Block 615 [VERSE]]
རྒྱལ་པོ་བཞད༌[^442]གད་ལྡན་དང་བུད་མེད་དང་། །
བག་མ་ལེན་པའི་ཚེ་དང་གསོད་པ་དང་། །
ནོར་ཀུན་འཕྲོག་ཚེ་བརྫུན་བྱས་གནོད་མེད་དེ། །
[^443]བརྫུན་ལྔ་ལྟུང་བར་བྱེད་པ་མིན་ཞེས་བཤད། །

[Block 616]
ཞེས་སྨྲས་པ༌[^444]ལྟ་བུ་དང་། གང་ཡང་ལོག་པར་ལྟ་བས་རབ་ཏུ་བཅུག་པའི་བརྫུན་དུ་སྨྲ་བའོ། །

[Block 617]
ཕྲ་མ༌[^445]ལ་སོགས་པ་གཏི་མུག་ལས་སྐྱེས་པ་ནི་ལོག་པའི་ལྟ་བས་རབ་ཏུ་བཅུག་པ་དང་། གང་ཡང་རིག་བྱེད་ལ་སོགས་པ་བསྟན་བཅོས་ངན་པ་རྡོལ༌[^446]བའོ། །

[Block 618]
ཇི་ལྟར་ན་བརྣབ་སེམས་ལ་སོགས་པ་ཆགས་པ་ལ་སོགས་པ་ལས་སྐྱེས་པ་ཡིན་ཞེ་ན།

[Block 619 [VERSE]]
དེ་ཡི་མཇུག་ཐོགས་ལས་བྱུང་ཕྱིར། །
བརྣབ་སེམས་སོགས་རྩ་གསུམ་ལས་སྐྱེས། །

[Block 620]
ཆགས་པའི་མཇུག་ཐོགས་སུ་བྱུང་བ་ནི་ཆགས་པ་ལས་སྐྱེས་པ་དག་ཡིན་ནོ། །

[Block 621]
ཞེ་སྡང་གི་མཇུག་ཐོགས་སུ་བྱུང་བ་ནི་ཞེ་སྡང་ལས་སྐྱེས་པ་དག་ཡིན་ནོ། །

[Block 622]
གཏི་མུག་གི་མཇུག་ཐོགས་སུ་བྱུང་བ་ནི་གཏི་མུག་ལས་སྐྱེས་པ་དག་ཡིན་ནོ། །

[Block 623]
མི་དགེ་བའི་ལས་ཀྱི་ལམ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 624 [HEADING]]
### དགེ་བའི་ལས་ཀྱི་ལམ། ^1-43-0

[Block 625]
དགེ་བའི་ལས་ཀྱི་ལམ་རྣམས་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 626 [VERSE]]
དགེ་བ་སྦྱོར་དང་མཇུག་བཅས་རྣམས། །
ཆགས་སྡང་གཏི་མུག་མེད་ལས་སྐྱེས། །

[Block 627]
དགེ་བའི་ལས་ཀྱི་ལམ་སྦྱོར་བ་དང་མཇུག་དང་། བཅས་པ་རྣམས་ནི་དགེ་བའི་སེམས་ཀྱིས་ཀུན་ནས་བསླང་བའི་ཕྱིར་དང་། དེ་ཡང་གདོན་མི་ཟ་བར་མ་ཆགས་པ་ལ་སོགས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་མ་ཆགས་པ་དང་ཞེ་སྡང་མེད་པ་དང་གཏི་མུག་མེད་པ་ལས་སྐྱེས་པ་དག་ཡིན་ནོ། །

[Block 628]
དེ་ལ་མི་དགེ་བའི་ལས་ཀྱི་ལམ་ནི༌[^447]སྦྱོར་བ་སྤོང་བ་ནི་དགེ་བའི་ལས་ཀྱི་ལམ་གྱི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 629 [VERSE]]
དངོས་སྤོང་བ་ནི་དངོས་ཡིན་ནོ། །
མཇུག་སྤོང་བ་ནི་མཇུག་ཡིན་ཏེ། །

[Block 630]
འདི་ལྟ་སྟེ་དགེ་ཚུལ་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་གནས་སྣ་ཚོགས་པར་འཇུག་པར་བྱེད། དགེ་འདུན་རྣམས་ལ་ཕྱག་འཚལ་བར་བྱེད། མཁན་པོ་ལ་གསོལ་བ་འདེབས་པར་བྱེད་པ་ནས་ལས་ལན་གཅིག་བརྗོད་པ་དང་། ལན་གཉིས་བརྗོད་པའི་བར་འདི་ནི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 631]
ལན་གསུམ་པ་བརྗོད་པའི་ཚེ་རྣམ་པར་རིག་བྱེད་དང་དེའི་སྐད་ཅིག་གི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་གང་ཡིན་པ༌[^448]འདི་ནི་ལས་ཀྱི་ལམ་དངོས་ཡིན་ནོ། །

[Block 632]
དེའི་འོག་ཏུ་ཇི་སྲིད་དུ་གནས་བསྒོ་བའམ།[^449] དེའི་རྟེན༌[^450]རྣམ་པར་རིག་པར་བྱེད་པ་དང་། ཇི་སྲིད་དུ་རྣམ་པར་རིག་པར༌[^451]བྱེད་པ་མ་ཡིན་པ་རྗེས་སུ་འབྲང་བ་འདི་ནི་མཇུག༌[^452]ཡིན་ནོ། །

[Block 633 [HEADING]]
### ལས་ཀྱི་ལམ་མཐར་ཕྱིན་པར་བྱེད་པ། ^1-44-0

[Block 634]
ལས་ཀྱི་ལམ་ཐམས་ཅད་ཆགས་པ་ལ་སོགས་པས་མཐར་ཕྱིན་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ་ཞེས་གང་བཤད་ན། འོ་ན་གང་ཞིག་གང་གིས་མཐར་ཕྱིན་པར་བྱེད་ཅེ་ན།

[Block 635 [VERSE]]
གསོད་དང་གནོད་སེམས་ཚིག་རྩུབ་པོ། །
ཞེ་སྡང་གིས་ནི་མཐར་ཕྱིན་བྱེད། །
--- END BLOCKS ---
