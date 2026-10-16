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
[Block 596 [VERSE]]
བདག་གིས་རུང་བ་མ་ཡིན་འདིས། །
རུང་བའི་དངོས་པོ་བཙལ་སྙམ་དུ། །

[Block 597]
ཞེས་བྱ་བ་ནི་གསེར་དངུལ་འདིས་དེ་བཞིན་གཤེགས་པའི་སྐུ་གཟུགས་ལུགས་སུ་བླུགས་ཤིང་རིས་སུ་བྲིས་པ་དང་། དྷརྨ་བྲིས་ཤིང་གླེགས་བམ་དུ་བྱས་པ་དང་། དགེ་འདུན་སྤྱི་ལ་འབུལ་བའི་བསམས་པས༌[^462]བླངས་ན་ཉེས་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 598]
དགེ་སྦྱོང་གིས༌[^463]ཁེ་སྤོགས་འདོད་པའི་ཕྱིར་བདག་གི་ནོར་གཞན་ལ་འཚོང་དུ་བཅོལ་ཏམ། གཞན་གྱི་ནོར་བདག་གིས༌[^464]བླངས་ཏེ་ཚོང་བྱས་ན་ཉེས་བྱས་སོ། །

[Block 599]
དཀོན་མཆོག་གསུམ་གྱི་ཕྱིར་རམ། དེ་ལྟར་མ་བྱས་ན་སྨན༌[^465]ཟོང་ཙམ་ཡང་མེད་ལ་འཚོ་བ་ཡང་འཆད་པར་འགྱུར་བ་ཞིག་གམ། བསོད་ནམས་བྱ་བ་ཞིག་ཏུ་བསམས་ཏེ་ཚོང་གི་ཁེ་སྤོགས་བྱ་དགོས་ན་ཡང་བདག་ཉིད་ཀྱིས་མི་བྱའི། ཁྱིམ་པ་གཞན་ལ་བཅོལ་བར་བྱའོ། །

[Block 600]
དེ་ལྟར་བཅོལ་བའི་འོས་མེད་ན་ཡང་བདག་ཉིད་ཚོང་བྱེད་པའི་ཚེ་བདག་གིས༌[^466]ནན་དང་མཐུས་མི་བྱའོ། །

[Block 601]
རུང་ངམ་མི་རུང་དགའ་མི་དགའ། །ཞེས་ལན་གསུམ་གྱི་བར་དུ་དྲིས་ལ། མི་དགའ་བ་མེད་དེ་རུང་ངོ་ཞེས་ཟེར་ན་ཚོང་བྱའོ། །

[Block 602]
ཕ་རོལ་པོ་མ་དད་བཞིན་དུ་ནན་གྱིས་ཚོང་བྱས་ཏེ་རིན་བརྩིས༌[^467]ལ་ཐོབ་ན་ཕམ་པར་འགྱུར་རོ། །

[Block 603]
དེ་ལྟར་འདི་ཡན་ཆད་དུ་དགེ་སྦྱོང་གི་བསླབ་ཚིག༌[^468]བཅུ་པོ་མདོ་ཙམ་དུ་བཤད་ཟིན་ཏོ།། །།

[Block 604]
འདོད་པས་བར་དུ་གཅོད་བྱེད༌[^469]ཅིང་། །རྫོགས་སངས་རྒྱས་ཀྱིས༌[^470]བཀའ་སྩལ་པ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་རབ་ཏུ་བྱུང་བ་རྣམས་འདོད་པའི་ཡོན་ཏན་ལྔ་ལ་བརྟེན༌[^471]པ་རྣམས་ནི་མཐོ་རིས་དང་ཐར་པ་ལ་བར་དུ་གཅོད་པའོ་ཞེས་བཀའ་སྩལ་པ་ལས།

[Block 605]
ཉེ་དགའི་སློབ་མ་དགེ་སྦྱོང་ཚེར་མ་ཅན༌[^472]དང་མཆོད་སྦྱིན་གཉིས་ན་རེ་འདོད་པས་བར་དུ་གཅོད་པའོ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ནི་དེ་ལྟར་མ་ཡིན་ཏེ།

[Block 606]
འདོད་པ་ལ་བརྟེན་ཀྱང་བར་དུ་གཅོད་པར་མི་འགྱུར་ཏེ་དེའི་དོན་བདག་གིས་ཤེས་སོ་ཞེས་སྨྲས་པ༌[^473]ལས།

[Block 607]
བཅོམ་ལྡན་འདས་ལ་གསོལ་ཏེ༌[^474]བཀའ་སྩལ་པ། དེ་སྐད་དུ་སྨྲ་བ་ལ་དང་པོར་ཚིག་འཇམ་པོས༌[^475]སྨྲོས་ཤིག །དེས་མ་བཏུབ་ན་གསོལ་བ་དང་། བཞིའི་ལས་ཀྱིས་དགེ་ཚུལ་གཏི་མུག་མ་སྨྲ་ཤིག༌[^476]ཅེས་བསྒོ་ཞིག །དེ་སྐད་དུ་བསྒོ་བ་ལས་ཀྱང་མ་བཏུབ་སྟེ་དེ་སྐད་སྨྲ་ན་དགེ་འདུན་གྱིས་འཚོ་བའི་ཡོ་བྱད་དུ་གཏོགས་པ་ལོངས་སྤྱོད་རྣམས་དང་ཕྲལ་ནས། གཙུག་ལག་ཁང་ནས་བསྐྲད་པར་བྱའོ། །

[Block 608]
དེ་ལྟར་བསྐྲད་པའི་དགེ་སྦྱོང་དེ་ནི་དགེ་སྦྱོང༌[^477]དང་གཉིས་གནས་ཁང་གཅིག་ཏུ་ཉལ་བ་གནང་བ་དེ་ལ་མེད་ན། ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་རྣམས་དང་སྤྱོད་པ་གཅིག་ཅིང་ཡོ་བྱད་གཅིག་པ་དང་། ལྟ་བ་གཅིག་པ་རྣམས་ཀྱང་དེ་ལ་མེད་པས་ན།

[Block 609 [VERSE]]
དེ་ནས་རོ་དང་འདྲ་བར་འགྱུར་རོ། །
འཕྱར་དང་རྟ་གད་བྱེད་ལ་སོགས། །

[Block 610]
འཆི་བར་བསམས་ཏེ་མི་བྱའོ། །ཞེས་བྱ་བ་ལ། རབ་ཏུ་བྱུང་བ་རྣམས་ནི་དུལ་ཞིང་ཞི་བའི་རང་བཞིན་པས།[^478] གདོལ་པ་དང་མ་རབས་ཀྱི་ཆོས་ལུས་ཀྱི་སྒོ་ནས་མཆོང་ཞིང་བརྒལ་བ་ལ་སོགས་པ་དག་དང་། ངག་གི་སྒོ་ནས་རྟ་གད་དྲག་པོ་ལ་སོགས་པ་མི་བྱའོ། །ཅིའི་ཕྱིར་ཞེ་ན། འཕྱར་བ་ནི་མ་བརྟགས་པའི་ཆོས་ཡིན་པ་དང་། རྟ་གད་དང་གག་ཚིལ་བྱེད་པ་ནི་རླུང་འཚུབ་ཅིང་སྔོན་ཤི་བ་དག་བྱུང་བས།

[Block 611 [VERSE]]
དེའི་ཕྱིར་འཆི་བར་བསམས་ཤིང་མི་བྱའོ། །
གླལ་ཚེ་ལག་ལ་སོགས་པ་ཡིས། །
ཁ་དགབ་པར་ཡང་ནན་ཏན་བྱ། །

[Block 612]
ཅིའི་ཕྱིར་ཞེ་ན། སོ་སྣང་བ་དང་གཅན་གཟན་ཆད་པ་ལྟར་ཤིན་ཏུ་མི་མཛེས་པའི་ཕྱིར་རོ། །

[Block 613 [VERSE]]
རྒན་ལ་སྦྲིད་བྱུང་ཕྱག༌[^479]བྱ་སྟེ། །
གཞོན་ལ་ནད་མེད་གྱུར་ཞེས་བྱ། །
ཁྱིམ་པ་སྦྲིད་པ་བྱུང་བ་དང་། །
ཡུན་རིང༌[^480]སོས་ཞེས་བརྗོད་པར་བྱ། །

[Block 614]
ཞེས་བྱ་བ་ལས།

[Block 615]
རྒན་པ་ནི་བདག་པས་ཚུལ་ཁྲིམས་དང་ཤེས་པ་རྒན་པའམ་མཁན་པོ་དང་སློབ་དཔོན་ནོ། །

[Block 616]
གཞོན་པ་ནི་བདག་པས་ད་དག་གིས་དམའ་བ་ཆུང་བའོ། །

[Block 617]
ཡུན་རིངས་པོས༌[^481]ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་རྣམས་ནི་ཚེ་རིང་བ་ལ་དགའ་བའི་ཕྱིར་རོ། །

[Block 618 [VERSE]]
བླ་མ་དག་གི་མདུན་དག་ཏུ། །
སྣབས་དང་མཆིལ་མ་མི་དོར་ཞིང་། །
སོ་ཤིང་བཅའ་བར་མི་བྱའོ། །
དེ་བཞིན་སྟན༌[^482]ལ་མི་འདུག་ཅིང་། །

[Block 619 [VERSE]]
མདུན་དུ་བཅག་པར་མི་བྱའོ། །
གོས༌[^483]གཅིག་དག་ཀྱང་བགོ་མི་བྱ། །
ཁྱེད་རེངས་སུ་ཡང་མི་དབྱུང་ངོ་། །

[Block 620]
ཞེས་བྱ་བ་ལ། མཁན་པོ་དང་སློབ་དཔོན་དང་ཤེས་པ་དང་ཚུལ་ཁྲིམས་ཀྱི་ཡོན་ཏན་གྱིས་འཕགས་པ་རྣམས་ནི་བླ་མ་སྟེ། དེ་དག་གི་མདུན་དུ་མིང་གིས་འབྱུང་བ་དེ་དག་མི་དོར་མི་བྱའོ། །ཅིའི་ཕྱིར་ཞེ་ན། མ་རབས་སྨད་པའི་ཆོས་ཡིན་པ་དང་། མ་གུས་ཤིང་བསྙེམས་པའི་ཚུལ་ཡིན་པས་སྤང་བར་བྱའོ། །

[Block 621]
སོ་ཤིང་ཟ་ན་ཡང་ཕུ་རུང་གིས་ཁ་བཀབ༌[^484]སྟེ་བཟའ་བར་བྱའོ། །

[Block 622]
བླ་མ་རྣམས་ལ་ཇི་ལྟར་བྱ་ཞེ་ན། རྒན་པོ་རྣམས་ལ་སྡོམ་ཅན་གྱིས། །གུས་བཅས་ཞེ་སར་བཅས་པར་བྱ་བ་སྟེ། རྒན་པ་གོང་དུ་སྨོས་པ་རྣམས་ལ་ལུས་ཀྱི་སྒོ་ནས་ཀྱང་གུས་ཤིང་ཞི་བར་བྱ་བ་དང་། ངག་གི་སྒོ་ནས་ཀྱང་ཚིག་འཇམ་ཞིང་གསོང་པོར་སྨྲ་བ་དང་ཞེ་ས་དང་བཅས་པར་བྱའོ། །

[Block 623]
བསླབ་པ་ཕྲ་མོའི་གནས་བསྟན་ཟིན་ཏོ།། །།

[Block 624 [HEADING]]
## ཕྱི་དྲོ་ཕན་ཆད་ཀྱི་བྱ་བ། ^7-0

[Block 625 [VERSE]]
ལག་པ་དག་པར་བསྙལ་ནས་ནི། །
བུམ་པ་ལ་སོགས་རྡུལ་མེད་བྱ། །

[Block 626]
ཞེས་བྱ་བ་ནི་ཟས་ཟོས་པའི་འོག་ཏུ། ཁ་ལག་ལེགས་པར་བཀྲུས་ནས་ནང་པར་སྤྱད་པར་བྱ་བའི་ཆུ་བཙག༌[^485]ཅིང་བླང་བར་བྱའོ། །

[Block 627]
ཆུའི་སྣོད་བུམ་པ་ལ་སོགས་པ་རྡུལ་དང་དྲི་མ་མེད་པར་སྲོག་ཆགས་མེད་པར་བརྟགས་ནས་ཆུ་ཡང་བཙག༌[^486]ཅིང་བླང་བར་བྱ་སྟེ། ཆུ་བཙག་པའི༌[^487]ཐབས་ནི།

[Block 628 [VERSE]]
སྲོག་ཆགས་ཡོད་ན་ལེགས་པར་བཙག །
ཅེས་པའི་སྐབས་སུ་བསྟན་པ་བཞིན་ནོ། །
གནས་མེད་པར་ནི་གནས་མི་བྱ། །

[Block 629]
ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་ནས་ལོ་བཅུའམ། ལྔ་མ་ལོན་གྱི་བར་དུ་གནས་མ་བཅས་པར་གནས་སུ་མི་དབང་བས་དགེ་སྦྱོང་རྣམས་ཀྱིས་གནས་མེད་པར་ཞག་གཅིག་ཀྱང་གནས་སུ་མི་གནང་ངོ་ཞེས་བཀའ་སྩལ་ཏོ། །

[Block 630 [VERSE]]
དགེ་འདུན་མལ་སྟན་ལ་སོགས་པ། །
དྲན་པ་མེད་པར་འདུག་མི་བྱ། །

[Block 631]
ཞེས་བྱ་བ་ནི། དགེ་འདུན་སྤྱིའི་མལ་ཆ་དང་སྟན་ཁྲི་དང་ཁྲིའུ་ལ་སོགས་པ་ནི་ཤིན་ཏུ་སྤྱད་པར་བྱ་བ་མ་ཡིན་པས་མི་རྟག་པ་ལ་སོགས་པའི་ཆོས་དྲན་པར་བྱས་ཏེ་འདུག་པར་མི་བྱའོ། །

[Block 632]
དེ་ལྟ་བུའི་དྲན་པ་མེད་པར་ནི་འདུག་པར་མི་བྱའོ། །

[Block 633]
དེ་ལྟ་བུའི་ཆོས་ཡིད་ལ་བྱེད་པ་དང་ལྡན་པས་འདུག་ཏུ་གནང་སྟེ། དེ་བས་ན་དྲན༌[^488]དང་ལྡན་ན་ཉེས༌[^489]མེད་དོ། །

[Block 634 [VERSE]]
སོ་བཀྲུ་བ་དང་ཆུ་བཏུང༌[^490]དང་། །
བཤང་གཅི་བྱེད་དུ་འགྲོ་བ་དང་། །
མཚམས་ནང་སྟོན་ལ་ཕྱག་བྱ་བ། །
དེ་དག་མ་ཞུས་ཉེས་མེད་དོ། །

[Block 635]
ཞེས་བྱ་བའི་མིང་གིས་འབྱུང་བ་འདི་དག་ནི་མཁན་པོ་དང་སློབ་དཔོན་ལ་མ་ཞུས་ཀྱང་ཉེས་པར་མི་འགྱུར་རོ་ཞེས་བསྟན་ཏོ། །
--- END BLOCKS ---
