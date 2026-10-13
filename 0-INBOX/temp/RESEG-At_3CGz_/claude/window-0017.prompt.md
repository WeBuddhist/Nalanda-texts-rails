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
བཟོད་ཅེས་པ་ནི་ནུས་པ་དང་ལྡན་པ་སྟེ་སྡོམ་པ་འབོགས་པ་ལ་རག་མ་ལས་པར་ཆས་པའོ། །

[Block 597]
སྙིང་རྗེ་ལྡན་ཞེས་པ་ནི་སློབ་མ་ལ་བུའི་འདུ་ཤེས་དང་། གཞན་གྱི་སྡུག་བསྔལ་ལ་སེམས་མི་བཟོད་པའོ། །

[Block 598]
བླ་མ་ཞེས་བྱ་བ་ནི་བླ་མར་བྱ་བའི་གནས་སུ་གྱུར་པ་ཉིད་ལ་ནོད་པར་བྱའི་གཞན་ལས་ནི་མ་ཡིན་ཏེ། གུས་པས་བླ་མར་འཛིན་པ་དང་། དེའི་རྗེས་སུ་སློབ་མའི་ངང་ཚུལ་ཅན་དང་། དེས་བསྟན་པའི་དོན་ལ་གུས་པ་ཆེན་པོ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 599]
ཡང༌[^332]བླ་མ་དེ་ཕུན་སུམ་ཚོགས་པ་བཞི་དང་ལྡན་པ་ཡིན་ཏེ། ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པ་དང་། ཡོན་ཏན་ཕུན་སུམ༌[^333]ཚོགས་པ་དང་། བསམ་པ་ཕུན་སུམ༌[^334]ཚོགས་པ་དང་། སྦྱོར་བ་ཕུན་སུམ༌[^335]ཚོགས་པའོ། །

[Block 600]
དེ་ལ་བདག་ཉིད་གང་ཞིག་སྡོམ་པ་གང༌[^336]ལ་གནས་ཞེས་པས་ནི་ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 601]
སྡོམ་པའི་ཆོ་ག་ལ་མཁས་དང་། །སྡོམ་པ་འབོགས་པ་བཟོད་ཅེས་པས་ནི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 602]
ཡང་བཤད་པ། སྡོམ་ལ་གནས་ཞེས་པ་ནི་བླ་མ་དེས་སྡོམ་པ་བཏང་བ༌[^337]དང་། ཚུལ་ཁྲིམས་འཆལ་པ་དང་། ཆོས་མཐུན་པ་མ་ཡིན་པ་ལས༌[^338]སྡོམ་པ་མི་འཐོབ་བོ། །

[Block 603]
ཆོ་ག་ལ་མཁས་ཞེས་པ་ནི་ཆོ་ག་ལ་མཁས་པ་ལས་གནོད་པར་བྱའི་ཆོ་ག་མི་ཤེས་པ་ལས་ནི་དེ་ཉིད་ཆོ་ག་ཉམས་པས་སྡོམ་པ་མི་འཐོབ་པོ། །འབོགས་བཟོད་ཅེས་པ་ནི་རབ་ཏུ་དགའ་བའི་ཡིད་ཀྱིས་ཚུལ་འདི་ལྟ་བུ་ལ་འཇུག་པ་ནི་ལེགས་སོ། །

[Block 604]
བདག་གིས་ཐེ་ཚོམ་མེད་པར་སྡོམ་པ་སྦྱིན་པར་བྱའོ་སྙམ་དུ་སྡོམ་པ་སྟེར་བར་ནུས་པའོ།[^339] །

[Block 605]
སྙིང་རྗེར་ལྡན་ཞེས་པས་ནི་བསམ་པ་ཕུན་སུམ༌[^340]ཚོགས་པ་དང་། སྦྱོར་བ་ཕུན་སུམ༌[^341]ཚོགས་པ་བསྟན་ཏེ། དེ་ལ་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་ནི་དད་པ་ཉིད། བསམ་པ་ཐག་པ་ནས་བྱེད་པ་ཉིད་དང་། མ་ཆགས་པ་དང་སྙིང་རྗེ་དང་ལྡན་པ་ཉིད་དེ། བླ་མ་ལ་གུས་པ་དང་། འདོད་པ་ཆུང་བ་དང་། ཆོག་ཤེས་པ་དང་། ཟང་ཟིང་ལྷུར་མི་ལེན་པ་དང་། སྐྱོ་བ་མེད་པ་དང་། ཕ་རོལ་གྱི་ཉེས་པ་བཟོད་པ་དང་། ཁྲོ་བ་དང་ཁོན་དུ་འཛིན་པ་མེད་པའོ། །

[Block 606]
སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་ནི་དགེ་བའི་ཆོས་ཕྱིར་ཞིང་སྤེལ་བ་དང་། གུས་ཤིང་འཇུག་པ་དང་། བསླབ་པའི་གཞི༌[^342]རྣམས་ལ་མ་རྨོངས་པར་བྱེད་པ་དང་། སྤྲོ་བ་དང་ལེ་ལོ་མི་བྱེད་པ་དང་། འདོད་པའི་བདེ་བ་དང་། འདུ་འཛི་དག་ལ་མི་དགའ་བ་དང་། སེམས་རྣམ་པར་མ་གཡེངས་པའོ།[^343] །

[Block 607]
དེ་ལྟ་བུའི་བླ་མ་ལས་སྡོམ་པ་བླངས་ན་ཚུལ་ཁྲིམས་ཀྱི་བསླབ་པ་འཕེལ་བར་འགྱུར་རོ། །

[Block 608]
དེ་ལྟ་བུ་ནི།

[Block 609 [VERSE]]
ཡང་དག་མཚན་ཉིད་ལྡན་པ་ཡི། །
བླ་མ་བཟང་ལས་སྡོམ་པ་བླང་། །

[Block 610]
ཞེས་བདག་གིས༌[^344]བསམས་སོ། །

[Block 611]
དེ་ཡང་།

[Block 612 [VERSE]]
སྡོམ་པ་ལེན་པའི་ཆོ་ག་དང་། །
གྲངས་དང་སྡོམ་པ་གཏོང་བའི་རྒྱུ། །
མི་གཏོང་རྒྱུ་དང་ལྡན་པ་དང་། །
ཚུལ་ཁྲིམས་ཀྱི་ནི་ཕན་ཡོན་ཡིན། །

[Block 613]
ཞེས་པ་ནི་བསྡུས་པའོ། །

[Block 614]
འདིར་སྔོན་གྱི་མཁས་པ་ཆེན་པོ་དུ་མའི་ལུགས་ཡོད་མོད་ཀྱི་འོན་ཀྱང་སྐྱེ་བོ་ཆེན་པོའི་ཆོས་ལུགས་ཤིང་རྟ་ཆེན་པོའི་ལམ་ཆེན་པོ་ཡིན་པས། སློབ་དཔོན་ཐོགས་མེད་ཀྱི་ལུགས་དང་། རྗེ་བཙུན་ཞི་བ་ལྷའི་ལུགས་གཉིས་བཤད་པར་བྱའོ། །

[Block 615 [HEADING]]
### སྡོམ་པ་ལེན་པའི་ཆོ་ག། ^6-1-0

[Block 616]
སྡོམ་པ་ལེན་པའི་ཆོ་ག་ནི་སློབ་དཔོན་ཐོགས་མེད་ཀྱིས༌[^345]ཚུལ་ཁྲིམས་ཀྱི་ལེའུར་རྒྱས་པར་མཛད་པ་དང་། ཡང་ན་བདག་གིས༌[^346]བྱས་པའི་ཆོ་གར་བལྟ་བར་བྱའོ། །

[Block 617]
སློབ་དཔོན་མེད་པའི་ཆོ་ག་ཡང་ཚུལ་ཁྲིམས་ཀྱི་ལེའུ་དེ་ཉིད་ན་རྒྱས་སོ། །

[Block 618]
བདག་གིས་བྱས་པའི་ཆོ་ག་དེ་ནི་འཕགས་པ་ཐོགས་མེད་ཀྱི་རྗེས་སུ་འབྲངས་པའི་ཡིན་ནོ། །

[Block 619]
སློབ་དཔོན་ཞི་བའི་ལྷས་ནི་ཆོ་ག་འདི་སྤྱོད་པ་ལ་འཇུག་པར་ཡང་མཛད་མོད་ཀྱི། བསླབ་པ་ཀུན་ལས་བཏུས་པར་རྒྱས་པར་མཛད་དོ། །

[Block 620]
སློབ་དཔོན་མེད་པའི་ཆོ་ག་ཡང་དེ་ཉིད་དུ་གསལ་བར་མཛད་དོ། །

[Block 621]
འདིར་བདག་གིས།

[Block 622 [VERSE]]
དེ་ལ་འབད་པ་འདི་འདྲ་བའི། །
བླ་མ་གལ་ཏེ་མ་རྙེད༌[^347]ན། །
གཞན་ལ་སྡོམ་པ་ནོད་པ་ཡི། །
ཆོ་ག་ཡང་དག་བཤད་པར་བྱ། །
དེ་ལ་སྔོན་ཚེ་འཇམ་པའི་དབྱངས། །

[Block 623]
ཞེས་བྱ་བ་ནས། མི་དགེ་བའི་ལས་རྣམས་མི་བྱའོ། །ཞེས་པའི་བར་འདིར་བླ་མ་མེད་པའི་ཆོ་གར་བཀོད་དེ། ཨཾ་བ་རཱ་ཛའི་ཆོ་ག་འདི༌[^348]ནི་བླ་མ་ཡོད་པ་དང་། བླ་མ་མེད་པ་གཉིས་ཀའི་ཆོ་གའི་ཚིག༌[^349]ཡིན་ནོ་ཞེས་བླ་མ་དག་གསུང་བས་འདིར་བླ་མ་མེད་པའི་ཆོ་གར་བཀོད་དོ། །

[Block 624]
བསླབ་པ་ཀུན་ལས་བཏུས་པར་ནི་འདིས༌[^350]བླ་མ་ལས་བླངས་པའི་ཆོ་གར་གསུངས་མོད་ཀྱི། འོན་ཀྱང་བདག་ནི་ལུགས་དེ་གཉིས་ཀའི་རྗེས་སུ་འབྲང་བས༌[^351]ན་བླ་མ་ལས་བླངས་པའི༌[^352]ཆོ་ག༌[^353]ཚུལ་ཁྲིམས་ཀྱི་ལེའུ་ལ་བརྟེན་ཞིང་བཀོད་ལ། བླ་ན༌[^354]མེད་པའི་ཆོ་ག་ནི་བསླབ་པ་ཀུན་ལས་བཏུས་པ་ལ་བརྟེན་ཞིང་བཀོད་པ་ཡིན་ནོ། །

[Block 625 [HEADING]]
### ཚུལ་ཁྲིམས་ཀྱི་རྣམ་གྲངས། ^6-2-0

[Block 626]
ཚུལ་ཁྲིམས་ཀྱི་རྣམ་གྲངས་ནི་འཕགས་པ་ཐོགས་མེད་ཀྱིས༌[^355]མདོ་སྡེ་མ་ལུས་པ་ངོ་བོ་ཉིད་ལ་སོགས་པའི་ཚུལ་ཁྲིམས་དགུར་བསྡུས་ཏེ། ཚུལ་ཁྲིམས་ཀྱི་ལེའུ་དེ་ཉིད་ལས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཚུལ་ཁྲིམས་ནི་དེ་ཙམ་དུ་ཟད་དོ། །

[Block 627]
ཚུལ་ཁྲིམས་ཀྱི་བྱ་བ་ཡང་དེ་ཙམ་དུ་ཟད་དོ། །

[Block 628]
ཚུལ་ཁྲིམས་ཀྱི་ཕན་ཡོན་ཡང་དེ་ཙམ་དུ་ཟད་དོ། །

[Block 629]
དེ་ལས་གོང་ན་ཡང་མེད་དོ། །

[Block 630]
དེ་ལས་ལྷག་པ་ཡང་མེད་དོ་ཞེས་གསུངས་སོ། །

[Block 631]
སློབ་དཔོན་ཞི་བའི་ལྷས་ནི་མདོ་སྡེ་མ་ལུས་པ་གང་ཟག་གསུམ་གྱི་བསླབ་པ་མཛད་དེ། འདི་ལྟར་ཐེག་པ་ཆེན་པོ་ལ་གོམས་པ་ཆེ་བ་དང་། གོམས་པ་འབྲིང་དང་། གོམས་པ་ཆུང་བའོ། །

[Block 632]
གོམས་པ་ཆེ་བའི་དབང་དུ་མཛད་ནས་བསླབ་པ་ཀུན་ལས་བཏུས་པ་ནས།

[Block 633 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པ་ནི། །
རྒྱས་པར་ཐེག་པ་ཆེ་ལས་འབྱུང་། །

[Block 634]
ཞེས་འབྱུང་བ་དང་། སྤྱོད་འཇུག་ལས་ཀྱང་།

[Block 635]
རྒྱལ་སྲས་རྣམས་ཀྱིས༌[^356]མི་བསླབ་པ། །འགའ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །ཞེས་གསུངས་སོ། །
--- END BLOCKS ---
