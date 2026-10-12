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
[Block 601]
དེ་ལ་རྒྱུའི་གནས་ནི་གང་རིགས་ལ་གནས་པའི་གང་ཟག་གོ། །

[Block 602]
ཞུགས་པའི་གནས་ནི་སེམས་བསྐྱེད་པའོ། །

[Block 603]
སྦྱོར་བའི་གནས་ནི་སེམས་བསྐྱེད་ནས་འབྲས་བུ་མ་ཐོབ་ཚུན་ཆད་དོ། །

[Block 604]
འབྲས་བུའི་གནས་ནི་ཐོབ༌[^240]པའོ། །

[Block 605]
བྱ་བ་བཅས་པའི་གནས་ནི་སློབ་པའོ། །

[Block 606]
བྱ་བ་མེད་པའི་གནས་ནི་མི་སློབ་པའོ། །

[Block 607]
ཁྱད་པར་གྱི་གནས་ནི་མངོན་པར་ཤེས་པ་ལ་སོགས་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་ལྡན་པའོ། །

[Block 608]
བླ་མའི་གནས་ནི་ཉན་ཐོས་ལ་སོགས་པ་བས༌[^241]སར་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའོ།[^242] །བླ་ན་མེད་པའི་གནས་ནི་སངས་རྒྱས་ཏེ། དེའི་གོང་ན་གནས་མེད་པའི་ཕྱིར་རོ། །

[Block 609]
མོས་པའི་གནས་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་མོས་པས་སྤྱོད་པའི་ས་ཐམས་ཅད་དོ། །

[Block 610]
འཇུག་པའི་གནས་ནི་ས་དང་པོའོ། །

[Block 611]
ངེས་པར་འབྱུང་བའི་གནས་ནི་དེའི་གོང་མ་ས་དྲུག་པོ་དག་གོ། །

[Block 612]
ལུང་བསྟན་པའི་གནས་ནི་ས་བརྒྱད་པའོ། །

[Block 613]
བརྗོད་པའི་གནས་ནི་ས་དགུ་པའོ། །

[Block 614]
དབང་བསྐུར་བའི་གནས་ནི་ས་བཅུ་པའོ། །

[Block 615]
ཕྱིན་པའི་གནས་ནི་སངས་རྒྱས་ཀྱི་ཆོས་ཀྱི་སྐུའོ། །

[Block 616]
ཕན་ཡོན་གྱི་གནས་ནི་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུའོ། །

[Block 617]
བྱ་བ་སྒྲུབ་པའི་གནས་ནི་སྤྲུལ་པའི་སྐུའོ། །

[Block 618]
གནས་རྣམ་པ་མང་པོ་འདི་དག་ཐམས་ཅད་ཀྱང་མདོར་བསྡུ་ན།

[Block 619 [VERSE]]
ཆོས་ཀྱི་དབྱིངས་ལ་རྣམ་གསུམ་སྟེ། །
ཞེས་བྱ་བར་རིག་པར་བྱ་སྟེ།
མ་དག་མ་དག་དག་པ་དང་། །
རྣམ་པར་དག་པར་ཅི་རིགས་སྦྱར། །

[Block 620]
དེ་ལ་མ་དག་པའི་གནས་ནི་རྒྱུའི་གནས་ནས་ཉེ་བར་བཟུང་སྟེ། སྦྱོར་བ་པའི་བར་དུའོ། །

[Block 621]
མ་དག་པ་དང་དག་པའི་གནས་ནི་སློབ་པ་རྣམས་སོ། །

[Block 622]
རྣམ་པར་དག་པའི་གནས་ནི་མི་སློབ་པ་རྣམས་སོ། །

[Block 623 [VERSE]]
འདི་ལས་ཇི་ལྟར་འོས་འོས་སུ། །
གང་ཟག་རྣམ་པར་གཞག་པར་འདོད། །

[Block 624]
གནས་རབ་ཏུ་དབྱེ་བ་འདི་ལས་ཅི་རིགས་པར་གང་ཟག་རྣམས་རྣམ་པར་གཞག་པར་རིག་པར་བྱ་སྟེ། འདི་ནི་རིགས་ལ་གནས་པའོ། །

[Block 625]
འདི་ནི་ཞུགས་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 626]
གནས་བཤད་ཟིན་ཏོ། །

[Block 627 [HEADING]]
## འབྲས་བུ་ཐོབ་པ། ^6-0

[Block 628]
འབྲས་བུ་ཐོབ་པ་གང་ཞེ་ན།

[Block 629 [VERSE]]
སྣོད་གྱུར་རྣམ་པར་སྨིན་བརྗོད་དང་། །
དེ་ཡི་དབང་གིས་སྟོབས་དང་ནི། །
འདོད་དང་འཕེལ་དང་རྣམ་དག་སྟེ། །
དེ་དག་འབྲས་བུ་གོ་རིམས་བཞིན། །

[Block 630]
སྣོད་དུ་གྱུར་པ་དེ༌[^243]ནི་གང་དགེ་བ་དང་རྗེས་སུ་མཐུན་པའི་རྣམ་པར་སྨིན་པའོ། །

[Block 631]
སྟོབས་ནི་གང་སྣོད་དུ་གྱུར་པའི་དབང་གིས་དགེ་བ་ཤས་ཆེར་གྱུར་པའོ། །

[Block 632]
འདོད་པ་ནི་སྔོན་གོམས་པར་བྱས་པས་དགེ་བ་འདོད་པའོ། །

[Block 633]
འཕེལ་བ་ནི་གང་ད་ལྟར་བྱུང་བ་ན་དགེ་བའི་ཆོས་ལ་གོམས་པར་བྱས་པས་དགེ་བའི་རྩ་བ་རྒྱས་པའོ། །

[Block 634]
རྣམ་པར་དག་པ་ནི་གང་སྒྲིབ་པ་སྤངས་པའོ། །

[Block 635]
འདི་དག་ནི་འབྲས་བུ་རྣམ་པ་ལྔ་དང་གོ་རིམས་བཞིན་ཏེ། རྣམ་པར་སྨིན་པའི་འབྲས་བུ་དང་། བདག་པོའི་འབྲས་བུ་དང་། རྒྱུ་མཐུན་པའི་འབྲས་བུ་དང་། སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་དང་། བྲལ་བའི་འབྲས་བུའོ། །

[Block 636 [VERSE]]
ཕྱི་མ་ཕྱི་མ་ཐོག་མ་དང་། །
དེ་གོམས་བྱས་དང་རྫོགས་པའོ། །
རྗེས་སུ་མཐུན་དང་མི་མཐུན་ཕྱོགས། །
བྲལ་བ་དང་ནི་ཁྱད་པར་དང་། །

[Block 637 [VERSE]]
བླ་མ་དང་ནི་བླ་ན་མེད། །
འབྲས་བུ་གཞན་ཏེ་མདོར་བསྡུས་པའོ། །

[Block 638]
ཕྱི་མ་ཕྱི་མའི༌[^244]འབྲས་བུ་ནི་རིགས་ལས་སེམས་བསྐྱེད་པ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 639]
གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པར་རིག་པར་བྱའོ། །

[Block 640]
ཐོག་མའི་འབྲས་བུ་ནི་དང་པོར་འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་ཐོབ་པའོ། །

[Block 641]
གོམས་པར་བྱས་པའི་འབྲས་བུ་ནི་དེའི་ཕ་རོལ་སློབ་པའི་གནས་སོ། །

[Block 642]
རྫོགས་པའི་འབྲས་བུ་ནི་མི་སློབ་པའི་ཆོས་རྣམས་སོ། །

[Block 643]
རྗེས་སུ་མཐུན་པའི་འབྲས་བུ་ནི་རྒྱུའི་དངོས་པོས་ཕྱི་མ་ཕྱི་མ་འབྲས་བུ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 644]
མི་མཐུན་པའི་ཕྱོགས་ཀྱི་འབྲས་བུ་ནི་སྤོང་བའི་ལམ་སྟེ། ཐོག་མའི་འབྲས་བུ་གང་ཡིན་པ་དེ་ཉིད་དེ། དེ་ནི་མི་མཐུན་པའི་ཕྱོགས་གཉེན་པོ་ལ་བྱ་བར་འདོད་དོ། །

[Block 645]
བྲལ་བའི་འབྲས་བུ་ནི་གོམས་པར་བྱས་པའི་འབྲས་བུ་དང་རྫོགས་པའི་འབྲས་བུ་སྟེ། ཉོན་མོངས་པ་དང་བྲལ་བར་ནི་སློབ་པ་དང་མི་སློབ་པ་དང་གོ་རིམས་བཞིན་ནོ། །

[Block 646]
ཁྱད་པར་གྱི་འབྲས་བུ་ནི་མངོན་པར་ཤེས་པ་ལ་སོགས་པ༌[^245]ཡོན་ཏན་གྱི་ཁྱད་པར་རོ། །

[Block 647]
བླ་མའི་འབྲས་བུ་ནི་བྱང་ཆུབ་སེམས་དཔའི་ས་རྣམས་ཏེ། དེ་མ་ཡིན་པའི་ཐེག་པ་ལས་བླ་མར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 648 [VERSE]]
བླ་ན་མེད་པའི་འབྲས་བུ་ནི་སངས་རྒྱས་ཀྱི་སའོ། །
བཞི་པོ་འདི་དག་ནི་གོམས་པར་བྱས་པ་དང་།
རྫོགས་པའི་འབྲས་བུའི་རབ་ཏུ་དབྱེ་བ་ཉིད་དོ། །

[Block 649]
འབྲས་བུ་གཞན་འདི་དག་ནི་མདོར་བསྟན་པ་སྟེ། རྒྱས་པར་བྱ་བ་དཔག་ཏུ་མེད་དོ། །

[Block 650]
དེ་ལ་གཉེན་པོ་སྒོམ་པའི༌[^246]དོན་བསྡུས་པ་ནི་བྱང་བར་བྱ་བའི་སྒོམ་པ་དང་། བསྲབས་པའི་སྒོམ་པ༌[^247]དང་། ཡོངས་སུ་སྦྱང་བར༌[^248]བྱས་པའི་སྒོམ་པ་དང་། གོང་མ་ཡང་དག་པར་རྩོམ་པའི་སྒོམ་པ་དང་། [^249]མཐོང་བའི་ལམ་དང་འདྲེ་བའི་ཕྱིར་འདྲེ་བའི་སྒོམ་པ་དང་། ཞུགས་པའི་སྒོམ་པ་དང་། མཆོག་གི་སྒོམ་པ༌[^250]དང་། ཐོག་མའི་སྒོམ་པ༌[^251]དང་། བར་མའི་སྒོམ་པ༌[^252]དང་། མཐའི་སྒོམ་པ་དང་། བླ་མ་དང་བཅས་པའི་སྒོམ་པ་དང་། བླ་ན་མེད་པའི་སྒོམ་པ་སྟེ། གང་དམིགས་པ་དང་། ཡིད་ལ་བྱེད་པ་དང་། ཐོབ་པ་ཁྱད་པར་དུ་འཕགས་པའོ། །

[Block 651]
གནས་རྣམས་ཀྱི་དོན་བསྡུས་པ་ནི་རིགས་ལ་གནས་པའི་སྐལ་བ་ཡོད་པའི་གནས་དང་། སེམས་བསྐྱེད་ནས་བཟུང་སྟེ། སྦྱོར་བའི་བར་དུ་རྩོམ་པའི་གནས་དང་། མ་དག་པ་དང་དག་པའི་གནས་དང་། ཤིན་ཏུ་དག་པའི་གནས་དང་། རྒྱན་དང་བཅས་པའི་གནས་དང་། ས་བཅུ་ཁྱབ་པའི་ཕྱིར་ཁྱད་པར་བྱ་བའི་གནས་དང་། བླ་ན་མེད་པའི་གནས་སོ། །

[Block 652]
འབྲས་བུ་རྣམས་ཀྱི་དོན་བསྡུས་པ་ནི་བསྡུས་པ༌[^253]དང་། དེའི་བྱེ་བྲག་དང་། སྔོན་གོམས་པར་བྱས་པ་དང་། གོང་ནས་གོང་དུ་བསྒྲུབ་པ༌[^254]དང་། བསྟན་པ་དང་། བཤད་པའོ། །

[Block 653]
དེ་ལ་བསྡུས་པ་ནི་འབྲས་བུ་ལྔའོ། །

[Block 654]
དེའི་བྱེ་བྲག་ནི་ལྷག་མ་རྣམས་སོ། །

[Block 655]
སྔོན་གོམས་པར་བྱས་པ་ནི་རྣམ་པར་སྨིན་པའི་འབྲས་བུའོ། །

[Block 656]
དེ་གོང༌[^255]ནས་གོང༌[^256]དུ་བསྒྲུབ་པ་ནི་དེ་མ་ཡིན་པ་གཞན་བཞིའོ། །

[Block 657]
བསྟན་པ་ནི་ཕྱི་མ་ཕྱི་མའི་འབྲས་བུ་ལ་སོགས་པ་བཞིའོ། །

[Block 658]
བཤད་པ་ནི་རྗེས་སུ་མཐུན་པའི་འབྲས་བུ་ལ་སོགས་པ་དྲུག་སྟེ། དེ་དག་ཉིད་བཤད་པའི་ཕྱིར་རོ། །

[Block 659]
བསྟན་བཅོས་དབུས་དང་མཐའ་རྣམ་པར་འབྱེད་པ་ལས་གཉེན་པོ་བསྒོམ་པ་ཞེས་བྱ་བའི་ལེའུར་བཅད་པ་བཞི་པའི་འགྲེལ་པའོ།། །།

[Block 660 [HEADING]]
## ཐེག་པ་བླ་ན་མེད་པ། ^7-0

[Block 661]
ད་ནི་ཐེག་པ་བླ་ན་མེད་པ་བཤད་དགོས་པས་དེ་བརྗོད་དོ། །

[Block 662 [VERSE]]
བླ་མེད་ཉིད་ནི་སྒྲུབ་པ་དང་། །
དམིགས་པ་དང་ནི་ཡང་དག་འགྲུབ། །
བསྟན་པ་ཡིན་པར་འདོད་པའོ། །

[Block 663]
ཐེག་པ་ཆེན་པོ་བླ་ན་མེད་པ་ཉིད་རྣམ་པ་གསུམ་སྟེ། དེས་བླ་ན་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 664]
སྒྲུབ་པ་བླ་ན་མེད་པ་ཉིད་དང་། དམིགས་པ་བླ་ན་མེད་པ་ཉིད་དང་། ཡང་དག་པར་འགྲུབ་པ་བླ་ན་མེད་པ་ཉིད་དོ། །

[Block 665 [HEADING]]
### སྒྲུབ་པ་བླ་ན་མེད་པ་ཉིད། ^7-1-0

[Block 666]
དེ་ལ་སྒྲུབ་པ་བླ་ན་མེད་པ་ཉིད་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་བསྒྲུབ་པར་རིག་པར་བྱའོ། །

[Block 667 [VERSE]]
སྒྲུབ་པ་དག་ནི་རྣམ་དྲུག་སྟེ། །
ཕ་རོལ་ཕྱིན་པ་དེ་དག་ལའོ། །
དམ་པ་དང་ནི་ཡིད་བྱེད་དང་། །
རྗེས་མཐུན་ཆོས་མཐའ་སྤངས་པ་དང་། །

[Block 668]
ཁྱད་པར་ཅན་དང་ཁྱད་པར་མེད། །རྣམ་པ་དྲུག་པོ་འདི་དག་ནི་སྒྲུབ་པ་སྟེ། འདི་ལྟར་དམ་པར་སྒྲུབ་པ་དང་། ཡིད་ལ་བྱེད་པ་ལ་སྒྲུབ་པ་དང་། རྗེས་སུ་མཐུན་པའི་ཆོས་སྒྲུབ་པ་དང་། །མཐའ་གཉིས་རྣམ་པར་སྤངས་པ་སྒྲུབ་པ་དང་། ཁྱད་པར་ཅན་སྒྲུབ་པ་དང་། ཁྱད་པར་མེད་པ་སྒྲུབ་པའོ། །

[Block 669 [HEADING]]
#### དམ་པར་སྒྲུབ་པ། ^7-1-1-0

[Block 670]
དེ་ལ།

[Block 671 [VERSE]]
དམ་པ་བཅུ་གཉིས་བདག་ཉིད་དེ། །
རྒྱ་ཆེ་བ་དང་ཡུན་རིང་དང་། །
ཆེད་དུ་བྱ་དང་མི་ཟད་དང་། །
རྒྱུན་མི་འཆད་དང་ཚེགས་མེད་དང་། །

[Block 672 [VERSE]]
དབང་འབྱོར་པ་དང་ཡོངས་གཟུང་དང་། །
རྩོམ་དང་ཐོབ་དང་རྒྱུ་མཐུན་དང་། །
འགྲུབ་པ་དམ་པར་འདོད་པ་ཡིན། །

[Block 673]
རྣམ་པ་བཅུ་གཉིས་པོ་འདི་དག་ནི་དམ་པ་སྟེ། འདི་ལྟར་རྒྱ་ཆེ་བ་དམ་པ་དང་། ཡུན་རིང་བ་དམ་པ་དང་། ཆེད་དུ་བྱ་བ་དམ་པ་དང་། ཟད་མི་ཤེས་པ་དམ་པ་དང་། རྒྱུན་མི་འཆད་པ་དམ་པ་དང་། ཚེགས་མེད་པ་དམ་པ་དང་། དབང་འབྱོར་པ་དམ་པ་དང་། ཡོངས་སུ་གཟུང་བ༌[^257]དམ་པ་དང་། རྩོམ་པ་དམ་པ་དང་། རབ་ཏུ་ཐོབ་པ་དམ་པ་དང་། རྒྱུ་མཐུན་པ་དམ་པ་དང་། འགྲུབ་པ་དམ་པའོ། །

[Block 674]
དེ་ལ་རྒྱ་ཆེ་བ་དམ་པ་ནི། འཇིག་རྟེན་གྱི་ཕུན་སུམ་ཚོགས་པ་ཐམས་ཅད་མི་འདོད་པ་དང་མཆོག་ཏུ་རིག་པར་བྱའོ། །

[Block 675]
ཡུན་རིང་པ་དམ་པ་ནི་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་དུ་ཡོངས་སུ་བསྒོམས་པའི་ཕྱིར་རོ། །

[Block 676]
ཆེད་དུ་བྱ་བ་དམ་པ་ནི༌[^258]སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བྱ་བའི་ཆེད་ཀྱི་ཕྱིར་རོ། །

[Block 677]
ཟད་མི་ཤེས་པ་དམ་པ་ནི་བྱང་ཆུབ་ཆེན་པོར་ཡོངས་སུ་བསྔོས་པས་གཏན་དུ་ཡོངས་སུ་གཏུགས་པར་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 678]
རྒྱུན་མི་འཆད་པའི་དམ་པ་ནི་བདག་གཞན་མཉམ་པ་ཉིད་དུ་མོས་པའི་ཕྱིར་ཏེ། སེམས་ཅན་ཐམས་ཅད་ལ་སྦྱིན་པ་ལ་སོགས་པས་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 679]
ཚེགས་མེད་པ་དམ་པ་ནི་གཞན་གྱི་སྦྱིན་པ་ལ་སོགས་པ་ལ་རྗེས་སུ་ཡི་རང་བ་ཙམ་གྱིས༌[^259]ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 680]
དབང་འབྱོར་པ་དམ་པ་ནི་ནམ་མཁའ་མཛོད་ཀྱི་ཏིང་ངེ་འཛིན་ལ་སོགས་པ་སྦྱིན་པ་ལ་སོགས་པ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
