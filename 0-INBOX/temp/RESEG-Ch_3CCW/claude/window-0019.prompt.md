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
[Block 666]
དེ་ལ་ཉེས་པར་སེམས་པ་སེམས་པ་ནི་གང་དག་ལུས་མི་གཙང་བ་དང་སྐད་ཅིག་ཅིང་འཇིག་པའི་ངང་ཅན་ལ་གཙང་བ་དང་། མི་འཇིག་པའི་ངང་ཅན་དུ་སེམས་པའོ། །

[Block 667]
ཉེས་པར་སྨྲ་བ་སྨྲ་བ་ཞེས་བྱ་བ་ནི་བསྔགས་པར་མི་འོས་པ་རྟག་ཏུ་ཕན་གདགས་དགོས་པ་སྡུག་བསྔལ་གྱི་བདག་ཉིད་ཅན་གྱི་ལུས་ལ་མིང་དང་ཚིག་དང་ཡི་གེའི་ཚོགས་སྣ་ཚོགས་ཀྱིས་བསྔགས་པ་བརྗོད་པའོ། །

[Block 668]
ཉེས་པར་བྱེད་པའི་ལས་བྱེད་པ་ཞེས་བྱ་བ་ནི་མི་དགེ་བའི་རྣམ་པར་སྨིན་པ་སྡུག་བསྔལ་དུ་འགྱུར་བའི་ལས་རྩོམ་པའོ། །

[Block 669]
དེ་ལྟར་བྱིས་པ་དེ་དག༌[^395]མི་གཙང་བཞིན་དུ་གཟུགས་ལ་ཆགས་སོ། །

[Block 670]
བར་མ་ནི་གང་དག་མི་གཙང་བ་ལ་ཇི་ལྟར་གནས་པ་བཞིན་དུ་སྨོད་ཅིང་གཟུགས་ལ་སྡུག་བསྔལ་བརྒྱ་ཕྲག་དུ་མ་བསྩགས་པར་མཐོང་སྟེ། གཟུགས་ལ་འདོད་ཆགས་དང་བྲལ་བར་གྱུར་ནས་བསམ་གཏན་དང་གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པ་འཐོབ་སྟེ། འདོད་པའི་ཁམས་ལས་ཤིན་ཏུ་འདས་པ་དེ་དག་ནི་བར་མའོ། །

[Block 671]
གང་དག་གཟུགས་ཀྱང་ངོ་བོ་ཉིད་ཀྱིས་མེད་དེ། གཟུགས་བརྙན་བཞིན་དུ་ཁོང་དུ་ཆུད་པ་དེ་དག་ནི་གཟུགས་ལ་སོགས་པའི༌[^396]རྣམ་པར་རྟོག་པ་རྣམས་ལས་གདོན་མི་ཟ་བར།

[Block 672 [VERSE]]
གཟུགས་ཀྱི་རང་བཞིན་ཤེས་པ་ཡིས། །
བློ་མཆོག་རྣམས་ནི་རྣམ་པར་གྲོལ། །

[Block 673 [HEADING]]
### ཚིགས་བཅད་ང་དྲུག་པ། ^1-57-0

[Block 674]
དོན་དེ་ཉིད་རྣམ་པར་དབྱེ་བ་བསྟན་པའི་ཕྱིར། སྡུག་ཆེས་པ་ལ་ཆགས་པར་འགྱུར།[^397] །

[Block 675 [VERSE]]
དེ་ལས་ལྡོག་པས་འདོད་ཆགས་བྲལ། །
སྒྱུ་མའི་སྐྱེས་བུ་ལྟར་དབེན་པར། །
མཐོང་བས་མྱ་ངན་འདས་པར་འགྱུར། །

[Block 676]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 677]
སྒྱུ་མའི་སྐྱེས་བུ་བཞིན་དུ་འགྲོ་བ་དབེན་ཞིང་སྟོང་སྟེ། མྱ་ངན་ལས་འདས་པ་མཐོང་ནས་གང་དག་མྱ་ངན་ལས་འདས་པར་གྱུར་པ་དེ་དག་ནི་བློའི་མཆོག་དང་ལྡན་པ་སྟེ། དེ་དག་ཀྱང་ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་བཅོམ་ལྡན་འདས་སུ་ཤེས་པར་བྱའོ། །

[Block 678]
བར་མ་དག་ནི་འཇིག་རྟེན་པ་རྣམས་ཏེ། འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བའོ། །

[Block 679]
བྱིས་པ་རྣམས་ནི་འདོད་པ་ལ་ཆགས་པར་ཤེས་པར་བྱའོ། །

[Block 680]
སྒྱུ་མའི་སྐྱེས་བུ་བཞིན་དུ་འགྲོ་བ་དབེན་པར་མཐོང་ནས་མྱ་ངན་ལས་འདས་པ་ཇི་ལྟར་འགྱུར་ཞེ་ན།

[Block 681 [HEADING]]
### ཚིགས་བཅད་ང་བདུན་པ། ^1-58-0

[Block 682 [VERSE]]
ལོག་པའི་ཤེས་པས་མངོན་གདུང་བའི། །
ཉོན་མོངས་སྐྱོན་རྣམས་གང་ཡིན་ཏེ། །
དངོས་དང་དངོས་མེད་རྣམ་རྟོག་པ། །
དོན་ཤེས་གྱུར་ལ་མི་འབྱུང་ངོ་། །

[Block 683]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 684]
གང་གིས་འགྲོ་བ་སྒྱུ་མ་བཞིན་དུ་དམིགས་པ་དེས་དངོས་པོ་དང་དངོས་པོ་མེད་པའི་རང་གི་མཚན་ཉིད་ངོ་བོར་མི་དམིགས་པས་དངོས་པོ་དང་དངོས་པོ་མེད་པར་ཡོངས་སུ་ཤེས་ཏེ། དེ་གཉིས་ལ་ཡོངས་སུ་མི་རྟོག༌[^398]པའི་ཕྱིར་རྣམ་པར་མི་རྟོག་པ་ཡིན་ནོ། །

[Block 685]
དངོས་པོ་དང་དངོས་པོ་མེད་པ་རྣམས་རྣམ་པར་བཤིག་པ་དོན་ཤེས་པ་དེ་ལ་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པ་གང་ཡིན་པ་དེ་དག་གདོན་མི་ཟ་བར་འཁོར་བའི་རྒྱུར་མི་འགྱུར་རོ། །

[Block 686]
ཉོན་མོངས་པ་དེ་དག་ནི་ལོག་པའི་ཤེས་པས་མངོན་པར་གདུང་བ་རྣམས་ལ་འབྱུང་ངོ་། །མངོན་དུ༌[^399]གདུང་བའི་ངང་ཚུལ་ཅན་ནི་མངོན་པར་གདུང་བ་ཅན་ནོ། །

[Block 687]
ལོག་པའི་ཤེས་པས་མངོན་པར་གདུང་བས་ལོག་པའི་ཤེས་པས་མངོན་པར་གདུང་བའོ། །

[Block 688]
ཕྱིན་ཅི་ལོག་པ་དག་ཡུལ་ལ་དམིགས་པ་རྙེད་ནས་ཉོན་མོངས་པ་རྣམས་ཀྱིས་གདུང་བར༌[^400]བྱེད་དོ། །

[Block 689]
དོན་རྟོགས་པ་ལ་ནི་དེ་དག་མེད་པས༌[^401]གདོན་མི་ཟ་བར་མྱ་ངན་ལས་འདའོ། །

[Block 690]
བྱིས་པ་རྣམས་ནི་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པས་མྱ་ངན་ལས་འདས་པར་མི་འཐད་དོ། །

[Block 691]
དེ་དག་ནི་འདོད་ཆགས་དང་འདོད་ཆགས་དང་བྲལ་བའི་གནས་ལ་ཡོངས་སུ་རྟོག་པས་ཇི་ལྟར་དམིགས་པའི་ཡུལ་ལ་ཆགས་པ་དང་། མི་ཆགས་པ་ཡོད་པར་འགྱུར། འཕགས་པ་དག་ནི་འཁོར་བ་འདི་ལ།

[Block 692 [HEADING]]
### ཚིགས་བཅད་ང་བརྒྱད་པ། ^1-59-0

[Block 693 [VERSE]]
གནས་ཡོད་ན་ནི་འདོད་ཆགས་དང་། །
འདོད་ཆགས་བྲལ་བ་དམིགས་འགྱུར་ན། །
གནས་མེད་བདག་ཉིད་ཆེན་པོ་རྣམས། །
ཆགས་པ་མེད་ཅིང་ཆགས་བྲལ་མིན། །

[Block 694]
གང་ལ་ཆགས་པ་དེ་ཡང་དམིགས་ལ་གང་ལ་མི་ཆགས་པ་དེ་ཡང་དམིགས་ན་ནི་ཆགས་པ་དང་མི་ཆགས་པ་གཉིས་སུ་རུང་ངོ་། །དངོས་པོ་ལ་རང་གི་ངོ་བོར་སྒྲོ་མི་འདོགས༌[^402]ན༌[^403]འདོད་ཆགས་དང༌[^404]བྲལ་བ་དག་མི་འབྱུང་ངོ་། །འཕགས་པ་རྣམས་ནི་དངོས་པོའི་རང་གི་ངོ་བོ་མི་དམིགས་པས་དེ་བས་ན་དེ་དག་གནས་མེད་དེ། དམིགས་པ་མེད་པས་ངེས༌[^405]པར་མྱ་ངན༌[^406]ལས་འདའོ། །

[Block 695]
དེའི་ཕྱིར་དེ་ལྟར་རྣམ་པར་དཔྱད་ན།

[Block 696 [HEADING]]
### ཚིགས་བཅད་ང་དགུ་པ། ^1-60-0

[Block 697 [VERSE]]
གང་དག་རྣམ་པར་དབེན་པ༌[^407]ལ། །
གཡོ་བའི་ཡིད་ཀྱང་མི་གཡོ་སྟེ། །
ཉོན་མོངས་སྦྲུལ་གྱིས་དཀྲུགས་པ༌[^408]ཡི། །
མི་བཟད་སྲིད་པའི་རྒྱ་མཚོ་རྒལ།

[Block 698]
[^409] །རང་བཞིན་གྱིས་རྒོད་པའི་ཕྱིར་སེམས་སྤྲེའུ་ལྟ་བུ་དབེན་པ་འགྲོ་བ་སྟོང་པ་ཞེས་དམིགས་པ་འདི་ལ་གང་དག་བསྟན་པར་གནས་པ་དག་ནི་སྲིད་པའི་རྒྱ་མཚོ་ཉོན་མོངས་པའི་སྦྲུལ་གྱིས་གང་བ་དམིགས་པ་རྒལ༌[^410]བའོ། །

[Block 699]
ད་ནི་རབ་ཏུ་བྱེད་པའི་དགེ་བ་ཡོངས་སུ་བསྔོ་བའི་ཕྱིར།

[Block 700 [HEADING]]
### ཚིགས་བཅད་དྲུག་ཅུ་པ། ^1-61-0

[Block 701 [VERSE]]
དགེ་བ་འདི་ཡིས་སྐྱེ་བོ་ཀུན། །
བསོད་ནམས་ཡེ་ཤེས་ཚོགས་བསགས་ཏེ། །
བསོད་ནམས་ཡེ་ཤེས་ལས་བྱུང་བ། །
དམ་པ་གཉིས་ནི་ཐོབ་པར་ཤོག །

[Block 702]
ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 703]
ཤེས་རབ་མ་གཏོགས་པ་དང་ཤེས་རབ་ཀྱི་རྒྱུ་མ་གཏོགས་པ་སེམས་ཅན་གྱི༌[^411]ཁམས་མཐའ་དག་ཡོངས་སུ་ཤེས་པར་བྱ་བའི་ཕྱིར་བསྒྲུབས་པ་དགེ་བ་དཔག་ཏུ་མེད་པ་ཐམས་ཅད་ནི་བསོད་ནམས་ཀྱི་ཚོགས་ཤེས་པ༌[^412]བསྟན་ཏེ། [^413]ཤེས་རབ་དང་ཤེས་རབ་ཀྱི་རྒྱུ་སངས་རྒྱས་སུ་འགྲུབ་པར་ཡོངས་སུ་བསྔོ་བ་ཐམས་ཅད་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་སོ། །

[Block 704]
སྐྱེ་བོ་ཐམས་ཅད་ཀྱིས་ཚོགས་དེ་གཉིས་བསགས་ཏེ་ཉེ་བར་བསྒྲུབས་ནས་བསོད་ནམས་ཡེ་ཤེས་ལས་བྱུང་བའི་དམ་པ་བླ་ན་མེད་པ་ཐོབ་པར་ཤོག་ཤིག །[^414]བྱུང་བ་ནི་སྐྱེས་པའོ། །

[Block 705]
བསོད་ནམས་དང་ཡེ་ཤེས་ལས་བྱུང་བ་དེ་དག་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་ལས་བྱུང་བ་སྟེ། དེ་གཉིས་གང་ཞེ་ན། གཟུགས་ཀྱི་སྐུ་དང་ཆོས་ཀྱི་སྐུའོ། །
--- END BLOCKS ---
