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
[Block 71]
བདེ་བ་ལས་སེམས་རྩེ་གཅིག་ཏུ་འགྱུར་རོ། །

[Block 72]
སེམས་རྩེ་གཅིག་པ་ལས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་པར་འགྱུར་རོ། །

[Block 73]
ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་མཐོང་བར་འགྱུར་རོ། །

[Block 74]
ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་རབ་ཏུ་ཤེས། ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་རབ་ཏུ་མཐོང་ན་ཡིད་འབྱུང་བར་འགྱུར་རོ། །

[Block 75]
ཡིད་བྱུང་ན་མི་ཆགས་པར་འགྱུར་རོ། །

[Block 76]
མ་ཆགས་ན་རྣམ་པར་གྲོལ་བར་འགྱུར་ཏེ། དེ་ལྟར་ན་ཡང་དག་པ་ཇི་ལྟ་བ༌[^46]བཞིན་དུ་རབ་ཏུ་མཐོང་ནས་སེམས་རྣམ་པར་གྲོལ་བར་རྣམ་པར་གཞག༌[^47]གོ། །

[Block 77]
གལ་ཏེ་དོན་དམ་པ་མ་རྟོགས་པ་དག་གིས་སྔོན་པོ་ལ་སོགས་པའི་དོན་དེ་དག་ཡོངས་སུ་གཅོད་པའི་རང་གི་ངོ་བོ་གང་ཡིན་པ་དེ་ཉིད་ཀྱིས་ཕྱིན་ཅི་མ་ལོག་པར་གྱུར་ན་ནི་དེའི་ཚེ་དེ་ཇི་ལྟར་སྣང་བའི་དངོས་པོའི་ངོ་བོ་ཉིད་ཀྱི་དེ་ཁོ་ན་མཐོང་བའི་ཕྱིར་དགྲ་བཅོམ་པ་དག་བཞིན་དུ་དེ་དག་དངོས་པོ་མེད་པའི༌[^48]མི་སྐྱེ་བས་ལེན་པ་མེད་པའི་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པས་ཐར་བར་འགྱུར་ཏེ། ཇི་ལྟར་གང་ན་ལུས་ཀྱང་ཞིག་པ་དང་།

[Block 78 [VERSE]]
འདུ་ཤེས་འགགས་ཤིང་ཚོར་བྲལ་བ། །
འདུ་བྱེད་སྦྱོར་བ་ཀུན་སུན་འབྱིན། །
རྣམ་པར་ཤེས་པ་ནུབ་གྱུར་པ། །

[Block 79]
ཞེས་གསུངས་པ་དང་། དེ་བཞིན་དུ།

[Block 80 [VERSE]]
མ་ཞུམ་པ་ཡི་ལུས་ཀྱིས་ནི། །
ཚོར་བ་དང་དུ་ལེན་པ་ན། །
དེ་ཡི་སེམས་ཀྱི་རྣམ་པར་ཐར། །
མྱ་ངན་འདས་པ་མར་མེ་བཞིན། །

[Block 81]
ཞེས་འབྱུང་བ་ལྟ་བུའོ། །

[Block 82]
དེ་ལྟར་བྱིས་པ་རྣམས་ཀྱང་ཡང་དག་པ་མཐོང་བའི་ཕྱིར་དགྲ་བཅོམ་པ་བཞིན་དུ་དེ་དག་ཐམས་ཅད་བཏང་བས་མྱ་ངན་ལས་འདས་པར་འདོད་པར་གྱིས་ཤིག །འོན་ཏེ་དེ་དག་དགྲ་བཅོམ་པ་བཞིན་དུ་ཐམས་ཅད་མེད་པས་རྣམ་པར་གྲོལ་བར་མི་འདོད་ན། བྱིས་པ་མ་རིག་པ༌[^49]ཕྱིན་ཅི་ལོག་པ་དག་གང་ལ་ཇི་ལྟར་རྟོག་པ་དེ་བཞིན་དུ་ངེས་པར་མི་འགྱུར་ཏེ། དེ་བས་ན་དེ་དག་གི་ཡོད་པར་ལྟ་བ་ནི་དེ་ཁོ་ན་མཐོང་བར་མི་འགྱུར་རོ། །

[Block 83]
དེའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས། མིག་དང་རྣ་བ་སྣ་ཡང་ཚད་མ་མིན།[^50] །ལྕེ་དང་ལུས་དང་སེམས་ཀྱང་ཚད་མ་མིན།[^51] །

[Block 84 [VERSE]]
གལ་ཏེ་དབང་པོ་འདི་དག་ཚད་ཡིན་ན། །
འཕགས་པའི་ལམ་གྱིས་སུ་ལ་ཅི་ཞིག་བྱ། །
འདི་ལྟར་དབང་པོ་འདི་དག་ཚད་མིན་ཏེ། །
ངོ་བོ་ཉིད་ཀྱི་བེམས༌[^52]པོ་ལུང་མ་བསྟན། །

[Block 85]
དེ་ཕྱིར་མྱ་ངན་འདས་པའི་ལམ་འདོད་གང་། །དེས་ནི་འཕགས་པའི་ལམ་གྱི༌[^53]བྱ་བ་བྱོས། །ཞེས་གསུངས་སོ། །

[Block 86]
དེ་སྐད་དུ་འདི་དག་འདུ་བྱེད༌[^54]ལོག་པས༌[^55]བརྟགས་པ་སྟེ། །

[Block 87 [VERSE]]
ཡང་དག་མིན་ལ་ཡང་དག་ཡོད་ལ་མེད། །
མ་བྱུང་བ་དང་མ་སྐྱེས་ཆོས་རྣམས་ལ། །
ཡང་དག་ཉིད་དང་འབྱུང་བ་ལོག་པར་བརྟགས། །

[Block 88]
ཤེའོ། །

[Block 89]
དེ་དག་ཇི་ལྟར་ཡང་དག་པར་མཐོང་བ་མ་ཡིན་ཞེ་ན།

[Block 90]
ཡང་དེ་ཉིད་ལས།

[Block 91 [VERSE]]
གང་ཚེ་འདུས་བྱས་འདུས་མ་བྱས། །
ཡང་དག་ཡང་དག་མ་ཡིན་དང་། །
རབ་འབྲིང་ཐ་མའི་ཆོས་རྣམས་ལ། །
རྣམ་པ་ཀུན་ཏུ་སྤྱོད་པ་མེད། །

[Block 92 [VERSE]]
བརྟན་པ་བུད་མེད་ཅེས་མི་སྤྱོད། །
སྐྱེས་པ་ཞེས་ཀྱང་མི་རྟོག་སྟེ། །
ཆོས་སོ་ཅོག་ནི་མ་སྐྱེས་ཕྱིར། །
བཙལ་བར་བྱས་ཀྱང་མ་མཐོང་ངོ་། །

[Block 93 [VERSE]]
ཆོས་འདི་ཐམས་ཅད་མེད་པ་སྟེ། །
སྐྱེ་བ་མེད་ཅིང་འབྱུང་བའང་མེད། །
རྟག་ཏུ་སྟོང་པ་བྱེད་མེད་གནས། །
འདི་ནི་མཁས་པའི་སྤྱོད་ཡུལ་ཡིན། །

[Block 94]
ཞེས་གསུངས་སོ། །

[Block 95]
དེ་ལྟར་མཐོང་བ་ནི༌[^56]ཁོ་ན་མཐོང་བ་སྟེ། །དེ་ཡང་བྱིས་པ་རྣམས་ལ་མེད་དོ། །

[Block 96]
དེའི་ཕྱིར་དེ་ཁོ་ན་མཐོང་བ་མ་ཡིན་པས་དེ་དག་རྣམ་པར་ཐར་པར༌[^57]མི་གཞག་གོ། །

[Block 97]
གང་གི་ཕྱིར་དེ་ལྟར་མེད་པར་ལྟ་བ་དེ་ཉེས་པ་ཐམས་ཅད་ཀྱི་འབྱུང་གནས༌[^58]ཏེ། ངན་པར་འགྲོ་བའི་འབྲས་བུ་དང་མི་བདེ་བ་མྱོང་བའི་འབྲས་བུ་ཡང་ཡིན་པ་ལྟར། ཡོད་པར་ལྟ་བ་ཡང་སྐྱེ་བོ་བྱིས་པ་རྣམས་དང་འདྲིས་པ་བདེ་འགྲོའི་འབྲས་བུ་དང་། ཚེ་རབས་ཐམས་ཅད་བདེ་བ་མྱོང་བའི་འབྲས་བུ་སྟེ། །དེ་ལྟ་བས་ན་ལྟ་བ་གཉིས་འཁོར་བའི་འབྲས་བུ་ཡིན་པས་རིགས་པ་དང་འགལ་ལོ། །

[Block 98 [HEADING]]
### ཚིགས་བཅད་བཞི་པ། ^1-5-0

[Block 99 [VERSE]]
ཡོད་པས་རྣམ་པར་མི་གྲོལ་ཏེ། །
མེད་པས་སྲིད་པ་འདི་ལས་མིན། །

[Block 100]
གང་གི་ཕྱིར་མི་གཙང་བས་མི་གཙང་བ་བཀྲུ་བར་མི་འགྱུར་བ་དེའི་ཕྱིར་འཁོར་བའི་མི་གཙང་བ་འབྱུང་བར་འགྱུར་བའི་རྒྱུ་ལྟ་བ་འདི་གཉིས་ཀྱིས་སྲིད་པ་ལས་འདའ་བའི་མཚན་ཉིད་རྣམ་པར་གྲོལ་བ་ཐོབ་པར་མི་ནུས་སོ། །

[Block 101]
གལ་ཏེ་དེ་ལྟར་ཡོད་པ་དང་མེད་པར་ལྟ་བ་ནི་ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་ལས་རྣམ་པར་གྲོལ་བར་མི་འགྱུར་ན། རྣལ་འབྱོར་པ་དག༌[^59]ལྟ་བ་གང་གིས་རྣམ་པར་གྲོལ་བར་འགྱུར་ཞེ་ན།

[Block 102 [VERSE]]
དངོས་དང་དངོས་མེད་ཡོངས་ཤེས་པས། །
བདག་ཉིད་ཆེན་པོ་རྣམ་པར་གྲོལ། །

[Block 103]
ཞེས་བྱ་བ་སྨོས་པ་ཡིན་ཏེ། དངོས་པོ་ལ་མ་བརྟེན་པར་དངོས་པོ་མེད་པར་མི་འགྲུབ། དངོས་པོ༌[^60]དང་དངོས་པོ་མེད་པར༌[^61]གཉིས་ཀ་རང་གི་ངོ་བོར་གྲུབ་པ་མེད་པར་གནས་སོ། །

[Block 104]
དེ་གཉིས་དངོས་པོ་མེད་པར་ཡོངས་སུ་ཤེས་པ་དངོས་པོ་དང་དངོས་པོ༌[^62]མེད་པའི་རང་གི་ངོ་བོ་ལ་སོགས་ཡོངས་སུ་མི་རྟོག་པའི༌[^63]རང་བཞིན་གང་ཡིན་པ་དེ་ནི་དེ་ལྟར་དངོས་པོ་དང་དངོས་པོ་མེད་པ་ཕྱིན་ཅི་མ་ལོག་པར་ཡོངས་སུ་ཤེས་པ་སྟེ། དེ་ལྟར་ཡོངས་སུ་ཤེས་པ་དེས་བདག་ཉིད་ཆེན་པོ་རྣམས་ཀྱིས༌[^64]རྣམ་པར་གཞག་གོ། །

[Block 105]
དེའི་ཕྱིར་དེ་དག་སྐྱེ་བོ་བྱིས་པ་རྣམས་ལས་ཤིན་ཏུ་འདས་པ་དམིགས་པ་མེད་པའི་ཡེ་ཤེས་ལ་གནས་པས་དེ་དག་ཉིད་ཆེ་བའི་ཕྱིར་བདག་ཉིད་ཆེན་པོ་ཞེས་བྱ་སྟེ། འཕགས་པ་ཞེས་བརྗོད་དོ། །

[Block 106]
དངོས་པོ་དང་དངོས་པོ་མེད་པའི་མཚན་མ་ལ་རྟོག་པ་ལས་བྱུང་བའི་འདོད་ཆགས་ལ་སོགས་པ་ནི༌[^65]ཁམས་གསུམ་ལས་མི་འདའ་བའི་རྒྱུར་གྱུར་པས་བྱིས་པ་རྣམས་ནི་འཆིང་བ་སྟེ། དེས་བྱིས་པ་དག་འཇུག་པ་ལ་རང་དབང་མེད་པར་བྱས་ནས་འགྲོ་བ་ལྔར་འཁོར་བ་ན་འཁོར་རོ། །

[Block 107]
དངོས་པོ་དང་དངོས་པོ་མེད་པ་མི་དམིགས་པ་ནི་དེའི་མཚན་མ་རྟོག༌[^66]པ་མེད་པའི་ཕྱིར༌[^67]མི་སྐྱེ་བས་ངེས་པར་འདོད་ཆགས་ལ་སོགས་པའི་རྒྱུན་ཆད་དོ། །

[Block 108]
དེ་དག་རྒྱུན་ཆད་པས་རྣམ་པར་གྲོལ་བར་འགྱུར་བས་ན།[^68] འདི་ཉིད་རྣམ་པར་གྲོལ་བའི་ཐབས་སུ་རིགས།[^69] །འདིར་སྨྲས་པ། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་ནི་ཡོད་དོ། །

[Block 109]
གལ་ཏེ་དེ་དག་མེད་དུ་ཟིན་ན་དེའི་ཚེ་ཁྱོད་ཀྱི་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ཡང་མེད་པར་འགྱུར་རོ། །

[Block 110]
འཁོར་བ་ནི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔའི་རང་གི་ངོ་བོ་ཡིན་པས་དངོས་པོའི་ངོ་བོ་སྟེ། ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ་དེ་དག་ཉིད་ལས༌[^70]ཉོན་མོངས་པས་འཕངས་ནས། འགྲོ་བ་རྣམས་སུ་འགྲོ་བ་ནས་འགྲོ་བ་གཞན་དུ་འགྲོ་བའི་ཕྱིར། འཁོར་བ་ཞེས་བྱ་བས་ན་དེ་ཡང་ཡོད་དོ། །
--- END BLOCKS ---
