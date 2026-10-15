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
བྱས་པ་སྦྱངས་པ༌[^461]མ་མཛད་པའི་ངང་ཚུལ་འདི་ལ་ཡོད་པས་བྱས་པ་སྦྱངས་པ་མ་མཛད་པ་སྟེ། སྦྱངས་པ་མ་མཛད་པར་བདག་ཉིད་ཀྱིས་བྱ་བ་རྣམས་ལ་མཁས་པའོ། །

[Block 632]
བྱང་ཆུབ་སེམས་དཔའི་སའི་གཞིའི་རྣལ་འབྱོར་གྱི་གནས་ལས།

[Block 633]
མཐུའི་ལེའུ་རིམ་པར་ཕྱེ་བ་སྟེ་ལྔ་པའོ།། །།

[Block 634]
ཡོངས་སུ་སྨིན་པར་ནི་མདོར་བསྡུ་ན་རྣམ་པ་བཅུ༌[^462]དྲུག་ཅེས་བྱ་བའི་དོན་ནི། ཡོངས་སུ་སྨིན་པ་ནི་ཅི། གང་གིས།[^463] གང་དུ། ཅི་ཞིག་ཡོངས་སུ་སྨིན་པར་འགྱུར། གང་གི༌[^464]གང་ཞིག་གིས་ཡོངས་སུ་སྨིན་པར་བྱེད། ཡོངས་སུ་སྨིན་པའི་མཚན་ཉིད་ནི༌[^465]ཇི་ལྟ་བུར་འབྱུང་ཞེས་བྱ་བའོ། །

[Block 635]
དེ་ལ་ཡོངས་སུ་ངེས་པར་ཅི་ཞིག་ཡོངས་སུ༌[^466]སྨིན་པའི་ངོ་བོ་ཉིད་ནི་ཡོངས་སུ་སྨིན་པའམ། ཡོངས་སུ་སྨིན་པ་གང་ལ་བརྟེན་ནས་འཇུག་སྙམ༌[^467]ནས། དེ་ལ་འདི་ཡོངས་སུ་སྨིན་པར་བྱ་བས་ནི།[^468] ཡོངས་སུ་སྨིན་པའམ། འདི་དག་ལ་ཡོངས་སུ་སྨིན་པར་བྱ་བས་ཏེ། ཉན་ཐོས་ཀྱི་ཐེག་པ་པ་ལ་སོགས་པའོ། །

[Block 636]
དེ་ལ་ཡང་ངེས་པར་ཅི་ཞིག་ཡོངས་སུ་སྨིན་པར་བྱ་བ་ཡིན་པས་ཡོངས་སུ་སྨིན་པར་བྱ་བ་འདི་དག་ནི་ཡོངས་སུ་སྨིན་པའོ། །ཇི་ལྟ་བུའི་རིམ་གྱིས་ཤེ༌[^469]ན། ཆུང་ངུ་ལ་སོགས་པས་སོ། །

[Block 637]
འདིས་ཡོངས་སུ་སྨིན་པར་བྱེད་པས་ན། ཐབས་ནི་ཡོངས་སུ་སྨིན་པའོ། །

[Block 638]
ངེས་པར་འདིར་བྱེད་པ་པོ་འབྱུང་བས་ཡོངས་སུ་སྨིན་པར་གང་གིས་བྱེད་པ་ནི་ཡོངས་སུ་སྨིན་པའོ། །

[Block 639]
འདི་ལྟར་ཇི་ལྟར་ཤེས་སྙམ་པས་ནི༌[^470]ཡོངས་སུ་སྨིན་པའི་གང་ཟག་གི་མཚན་ཉིད་དོ། །

[Block 640]
རྨ་ཡོངས་སུ་སྨིན་པ་ཞེས་བརྗོད་པ་ནི། བརྟོལ་ལ་རག་པའོ། །

[Block 641]
དེ་བཞིན་དུ་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་སྤངས༌[^471]ལ་རག་པ་པའི༌[^472]རྒྱུད་ནི་ཡོངས་སུ་སྨིན་པ་ཞེས་བརྗོད་དོ། །

[Block 642]
བུམ་པ་དང་། རྗེའུ་དང་། ཁམ་ཕོར་ལ་སོགས་པའི་སྣོད་དང་། ཨ་མྲ༌[^473]དད་པ་ན་ས་ལ་སོགས་པ་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་འོས་གཉིས་སྨོས་པས་ནི་ཉེ་བར་ལོངས་སྤྱོད་པའི༌[^474]འོས་རྟེན་དང་བརྟེན་པ་གཉིས་རབ་ཏུ་བསྟན་པའི་དོན་ཏེ། རྟེན་ནི་ལུས་སོ། །

[Block 643]
བརྟེན་པ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བའི་ཆོས་སོ། །

[Block 644]
གོ་རིམ་ནི་དང་པོར་བརྟོལ་བ་ཡིན་ལ། ཕྱི་ནས་ཡོངས་སུ་ལོངས་སྤྱད་པ་ཞེས་བྱ་བ་ཡོངས་སུ་སྨིན་པའི་གང་ཟག་རིགས་ལ་གནས་པ་དང་། རིགས་ལ་མི་གནས་པའི་བྱེ་བྲག་གམ། བླ་ན་ཡོད་པའམ་བླ་ན་མེད་པའི་ཁྱད་པར་རམ། ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོའི་ཁྱད་པར་རོ། །

[Block 645]
གང་གང་ལ་ཡོངས་སུ་སྨིན་པར་བྱ་བའི་ཁྱད་པར་རྣམ་པ་དྲུག་གི༌[^475]བསྡུས་པའི་དོན་ནི་དེ་དག་ཡོངས་སུ་སྨིན་པ་ནི་ཡོངས་སུ་སྨིན་པ་སྟེ། ཡོངས་སུ་སྨིན་པ་དེའི་ཁྱད་པར་གསུམ་ནི་ཡོངས་སུ་སྨིན་པའོ། །

[Block 646]
དེ་དག་ལས་གཞན་པའི་གོ་རིམ་གྱི་ཁྱད་པར་གསུམ་ཡང་ཡོངས་སུ་སྨིན་པ་སྟེ། ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོའི་མཚན་ཉིད་དོ། །

[Block 647]
རྣམ་པར་སྨིན་པ་ཞེས་བྱ་བ་ནི། རྣམ་པར་སྨིན་པ་བརྒྱད་དེ། བདག་དང་གཞན་གྱི་དོན་གྱི་ལེའུར༌[^476]བསྟན་པའོ། །

[Block 648]
སྡིག་པ་མི་དགེ་བའི་ཆོས་རྣམས་ལ་སེམས་མི་འཇུག་ཅིང་སྒྲིབ་པ་ཆུང་བ་དང་། རྟོག་པ༌[^477]ཉུང་བ་དང་ཞེས་བྱ་བས་ནི། ལས་དང་ཉོན་མོངས་པའི་རྣམ་པར་རྟོག་པ་མི་མཐུན་པའི་ཕྱོགས་ཆུང་བར་གྱུར་པ་ཉིད་བསྟན་ཏོ། །

[Block 649]
དྲང་བ་ནི་རང་གི་བསམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་སྟོན་པ་ཉིད་དོ། །

[Block 650]
མཐུན་པར་འཛིན་པ་ནི་གདམས་ངག་རྗེས་སུ་བསྒྲུབ་པ༌[^478]ཉིད་དོ། །

[Block 651]
དྲན་པ་དང་ལྡན་པ་ནི་སྔར་བྱས་པ་དང་། སྔར༌[^479]སྨྲས་པའི་རྣམ་པར་རྟོག་པ་མི་མཐུན་པའི་ཕྱོགས་ཆུང་བར་གྱུར་པ་ཉིད་བསྟན་ཏོ། །

[Block 652]
དྲང་བ་ནི་རང་གི་བསམ་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི། དོན་འཛིན་པར་བྱེད་པའི་ཤེས་རབ་ཀྱི་ཁྱད་པར་སྟོན་པར་བྱེད་དེ། སེམས་ཀྱིས༌[^480]རབ་ཏུ་རྟོགས་པ་ཤེས་རབ་ཀྱིས་དོན་རབ་ཏུ་རྟོགས༌[^481]པ་ཉིད་དོ། །

[Block 653]
ཐམས་ཅད་ནས་ཉོན་མོངས་པ་ཐམས་ཅད་ལས་སེམས་པ་གཏན་དུ་རྣམ་པར་གྲོལ་བར་བྱེད་པ་ཞེས་བྱ་བ་ལ། ཐམས་ཅད་ནས་ཞེས་བྱ་བ་ནི་དམིགས་པ་ཐམས་ཅད་ནས་སོ། །

[Block 654]
གཏན་དུ་ཞེས་བྱ་བ་ནི་བག་ཆགས་རབ་ཏུ་སྤངས་པའོ། །

[Block 655]
ཉོན་མོངས་པ་ཐམས་ཅད་ལས་ཞེས་བྱ་བ་ནི། མཐོང་བ་དང་བསྒོམ་པས་སྤངས་པའི༌[^482]ཉོན་མོངས་པའོ། །

[Block 656]
ཡུན་རིང་པོ་ནས་གོམས་པ་ཞེས་བྱ་བས་ནི། དེའི་སྦྱོར་བ་མེད་པ་ཉིད་བསྟན་ཏོ། །

[Block 657]
དབང་པོ་དང་། དགེ་བའི་རྩ་བ་དང་། ཤེས་པ་ཡོངས་སུ་སྨིན་པའི་རྒྱུ་ནི་སྔོན་གྱི་སྐྱེ་བ་ལའོ། །

[Block 658]
རྒྱུད༌[^483]ཡོངས་སུ་མ་བརྟགས་པ༌[^484]ནི་མཐོང་བའི་ཆོས་ལའོ། །

[Block 659]
རྒྱུ་ཆུང་ངུ་ལ་གོམས་པ་ཞེས་བྱ་བ་ནི་དམ་པར༌[^485]བྱེད་པའི༌[^486]སྦྱོར་བ་དང་བྲལ་བས་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 660]
ཡོངས་སུ་སྨིན་པའི་ཐབས་ཉི་ཤུ་རྩ་བདུན་པོ་རྣམས་ཀྱི་བསྡུས་པའི་དོན་ནི། བསྟན་པ་དང་། བཤད་པ་སྟེ། འདི་དག་གི་གནས་སྐབས་སོ། །

[Block 661]
བསྟན་པ་ནི་ཁམས་བརྟས་པ༌[^487]དང་། ད་ལྟར་གྱི་རྐྱེན་ཉེ་བར་སྒྲུབ་པ་ཞེས་བྱ་བའོ། །

[Block 662]
འདི་དག་ལས་གཞན་པའི་ཐབས་རྣམས་ནི་བཤད་པའོ། །

[Block 663]
ཁམས་བརྟས་པའི༌[^488]བཤད་པ་ནི་དྲུག་གོ། །

[Block 664]
ཁམས་བརྟས་པ༌[^489]དེ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཆུང་ངུ་དང་ཆེན་པོའོ། །

[Block 665]
ཆུང་ངུས༌[^490]ནི་འཇུག་པར་འགྱུར་ལ། ཆེན་པོས་དགའ་བར་འཛིན་པའོ། །

[Block 666]
གང་དེ་ལྟར་འཇུག་པ་དེ་ཉིད་དང་པོར་འཇུག་པ་ཉིད་ཀྱང་ཡིན་ནོ། །

[Block 667]
ཡང་འདི་དག་གི་ཁྱད་པར་གང་ཡིན་ཞེ་ན། འཇུག་པ་ནི་ཁྱིམ་པ་དང་རབ་ཏུ་བྱུང་བའི༌[^491]གནས་སྐབས་གཉིས་དག་གི་བསླབ་པའི་གནས་ཡང་དག་པར་ལེན་པའོ། །

[Block 668]
དང་པོར་འཇུག་པ་ཡང་མ་ཡིན་ཏེ། རིག་པའི༌[^492]དོན་ལ་ཕན་ཡོན་མཐོང་ནས་འཇུག་པ་འདི་ཉིད་ལ་དང་པོར་འཇུག་པ་ཞེས་བརྗོད་དོ། །

[Block 669]
དང་པོར་འཇུག་པ་མ་ཡིན་པ་ནི། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས༌[^493]བཏང་སྙོམས་མི་མཛད་པ་ལ་རྟེན༌[^494]ཅིང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། འདི་ནི་ཁམས་བརྟས་པའི༌[^495]བཤད་པའོ། །

[Block 670]
དེ་ལ་རྣམ་པར་དག་པ་ཐག་རིང་བ་ནི། ལེ་ལོའམ། རྐྱེན་དང་མི་ལྡན་པ་སྟེ། སྔར་བརྩོན་འགྲུས༌[^496]བརྩམས་པའི་ཁམས་ལ་བརྟེན་པ་ཉིད་དང་། ལེ་ལོ་དང་རྐྱེན་དང་མི་ལྡན་པའོ། །
--- END BLOCKS ---
