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
[Block 1401]
འཇིག༌[^972]རྟེན་སྟོན་པ་ཞེས་བྱ་བ་ནི་རྣམ་པ་བཅུ་གཅིག་གིས་འཇིག་རྟེན་སྟོན་པར་བཤད་དེ། ཕུང་པོའི་འཇིག་རྟེན་སྟོན་པ་དང་། ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་བརྟགས་པ་དམིགས་སུ་མེད་པར་སྟོན་པ་དང་། སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་ཀྱི་སྤྱོད་པ་དང་། དབྱེ་བ་ལ་སོགས་པ་སྟོན་པ་དང་། ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་སྟོན་པ་དང་། ཆོས་ཐམས་ཅད༌[^973]མཚན་ཉིད་མེད་པའི་མཚན་ཉིད་དུ་སྟོན་པ་དང་། བྱས་པ་གཟོ་ཞིང་བྱས་པ་ཚོར་བའི་དབང་དང་། ཆོས་ཐམས་ཅད་ཤེས་པ་པོ་མེད་ཅིང་། མཐོང་བ་པོ་མེད་པར་སྟོན་པ་དང་། མ་མཐོང་བའི་ཆོས་ཐམས་ཅད་སྟོན་པ་དང་། འཇིག་རྟེན་སྟོང་པ་ཉིད་དུ་བརྗོད་པ༌[^974]རིག་པར་བྱེད་ཤེས་པར་བྱེད། རྣམ་པར་ཤེས་པར་བྱེད་སྟོན་པར་བྱེད་པའི་དབང་དང་། འཇིག་རྟེན་འདི་བསམ་གྱིས་མི་ཁྱབ་ཅིང་དབེན་ལ། ནང་ལ་སོགས་པ་སྟོང་ཞིང་ཞི་བར་སྟོན་པ་དང་། འཇིག་རྟེན་འདི་དང་འཇིག་རྟེན་ཕ་རོལ་པོའི་འདུ་ཤེས་མེད་པས་སོ། །

[Block 1402 [HEADING]]
###### ཕུང་པོའི་འཇིག་རྟེན་སྟོན་པ། ^1-2-5-12-1-0

[Block 1403]
དེ་ལ་རབ་འབྱོར་ཕུང་པོ་ལྔ་ནི་དེ་བཞིན་གཤེགས་པས་འཇིག་རྟེན་དུ་གསུངས་སོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཕུང་པོ་ལྔ་པོ་འདི་དག་འཇིག་པར་སྟོན་པ་མ་ཡིན། རབ་ཏུ་འཇིག་པར་སྟོན་པ་མ་ཡིན་ཏེ༌[^975]ཞེས་བྱ་བ་ལ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཕུང་པོའི་དེ་བཞིན་ཉིད་འབའ་ཞིག་མཐོང་གི་ཀུན་བརྟགས་པའི་ཕུང་པོ་ནི་མ་ཡིན་ནོ། །

[Block 1404]
འཇིག་པ་དང་རབ་ཏུ་འཇིག་པ་ཞེས་བྱ་བ་ནི་ཆུད་ཟ་བ་དང་མ་རུང་བར་འགྱུར་བ་ལ་བྱའོ། །

[Block 1405 [HEADING]]
###### ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་བརྟགས་པ་དམིགས་སུ་མེད་པར་སྟོན་པ། ^1-2-5-12-2-0

[Block 1406]
[^976]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཉིད་ཀྱང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་མོ་འདི་ཉིད་ལ་མེད་ཅིང་མི་དམིགས་ན་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ༌[^977]གཟུགས་ཡོད་པའམ་དམིགས་པར་ལྟ་ག་ལ་འགྱུར་ཞེས་བྱ་བ་ནི་དམིགས་པར་བྱ་བ་དང་། དམིགས་པར་བྱེད་པས་མཉམ་པས་མཉམ་པར་གྱུར་པའི་ཚེ། རྣམ་པར་མི་རྟོག་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཉིད་ཀྱང་མི་སྣང་ན་གཟུགས་ལ་སོགས་པ་ལྟ་ཅི་སྨོས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1407 [HEADING]]
###### སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་ཀྱི་སྤྱོད་པ་དང་དབྱེ་བ་སྟོན་པ། ^1-2-5-12-3-0

[Block 1408]
རབ་འབྱོར་དེ་བཞིན་གཤེགས་པས་སེམས་ཅན་དེ་དག་གི་སེམས་བསྡུས་པ་དང་། སྤྲོས་པ་ནི་ཆོས་ཉིད་ཀྱིས་ཡང་དག་པ་ཇི་ལྟ་བ་ཉིད་དུ་རབ་ཏུ་མཁྱེན་ཏོ་ཞེས་བྱ་བ་ནི་སེམས་ཀྱི་ཆོས་ཉིད་གཟིགས་པས། སེམས་བསྡུས་པ་དང་། སྤྲོས་པ་རྣམས་ཡང་དག་པ་ཇི་ལྟ་བ་ཉིད་མ་ཡིན་ཞིང་མེད་པར་མཁྱེན་པ་ལ་སེམས་བསྡུས་པ་དང་། སྤྲོས་པ་མཁྱེན་པ་ཞེས་བྱའོ། །

[Block 1409]
དེ་ནས་ཡང་སེམས་བསྡུས་པ་དང་སྤྲོས་པ་དེ་དག་ཇི་ལྟར་མཁྱེན་ཞེས་གསོལ་པ་དང་། ཟད་པ་དང་འདོད་ཆགས་དང་བྲལ་བ་དང་འགག་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྟོན་ཏེ། སེམས་ཅན༌[^978]ཟད་པའི་ཆོས་ཉིད་དང་། འདོད་ཆགས་དང་བྲལ་བའི་ཆོས་ཉིད་དང་འགག་པའི་ཆོས་ཉིད་དང་སྤོང་བའི་ཆོས་ཉིད་དང་། ངོ་བོ་ཉིད་ཀྱིས་དབེན་པར་མཁྱེན་པ་ལ་སེམས་དེ་དག་མཁྱེན་ཞེས་བཤད་དོ།

[Block 1410]
[^979] །དེའི་འོག་ཏུ་རབ་འབྱོར་སེམས་འདོད་ཆགས་དང་བཅས་པ་གང་ཡིན་པ་དེ་ནི་སེམས་ཀྱི་ཡང་དག་པ་ཇི་ལྟ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བས་འདོད་ཆགས་དང་བཅས་པའི་སེམས་ལ་སོགས་པ་མཁྱེན་པར་སྟོན་ཏོ། །

[Block 1411]
འདི་ལ་འདོད་ཆགས་དང་བཅས་པའི་སེམས་ལ་འདོད་ཆགས་དང་བཅས་པའི་སེམས་སུ་ཡང་དག་པ་ཇི་ལྟ༌[^980]བ་བཞིན་དུ་རབ་ཏུ་མཁྱེན་ཞེས་བྱ་བ་ལ་འདིར་གལ་ཏེ་འདོད་ཆགས་དང་། སེམས་དང་། འདོད་ཆགས་དང་བཅས་པ་ཉིད་ཀྱང་དེ་ལྟར་ཤེས་ན་འདོད་ཆགས་དང་བཅས་པ་ཞེས་བྱ་བའི་སེམས་ཀྱི་ཆོས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡོད་པ་མ་ཡིན་གྱི་ཡང་དག་པ་ཇི་ལྟ་བ་ཉིད་ཅེས་བྱ་བའི་ཆོས་ངོ་བོ་ཉིད་ཀྱིས་དབེན་པ་ལ་སེམས་ཀྱི་ཆོས་ཡང་དག་པ་ཇི་ལྟ་བ་ཉིད་ཅེས་བྱའོ། །

[Block 1412]
དེ་བཞིན་གཤེགས་པ་ཤེས་རབ་ཤིན་ཏུ་རྣམ་པར་དག་པ༌[^981]ནི་སེམས་སམ། འདོད་ཆགས་སམ། སེམས་ལས་བྱུང་བའི་ཆོས་སམ། འདོད་ཆགས་དང་བཅས་པ་ལ་སོགས་པར་མི་བཟུང༌[^982]སྟེ། འདོད་ཆགས་དང་བཅས་པ་ལ་སོགས་པའི་གནས་སྐབས་ཀྱི་ཀུན་བརྟགས་པ་དེ་ཤིན་ཏུ་མེད་པའི་ཕྱིར་རོ། །

[Block 1413]
དེ་བས་ན་འདིར་ཚིག་གི་དོན་ནི་འདི་ཡིན་པར་ཤེས་པར་བྱ་སྟེ། འདོད་ཆགས༌[^983]བཅས་པའི་སེམས་ཡང་དག་པ་ཇི་ལྟ་བ་ཉིད་མ་ཡིན་ཞིང་དེ་བདེན་པ་མ་ཡིན་པས་དེ་སྤངས་ཏེ། ཡང་དག་པ་ཇི་ལྟ་བ་ཉིད་ཀྱི་རྣམ་པར་རབ་ཏུ་མཁྱེན་ཏོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1414]
དེ་བས༌[^984]ཡང་འདོད་ཆགས་དང་བྲལ་བའི་སེམས་ཡང་དག་པ་ཇི་ལྟ་བ་ཉིད་དུ་རབ་ཏུ་མཁྱེན་པ་སྟོན་ཏེ། རབ་འབྱོར་སེམས་འདོད་ཆགས་དང་བྲལ་བ་གང་ཡིན་པ་དེ་སེམས་འདོད་ཆགས་དང་བཅས་པ་མ་ཡིན་ཞེས་བྱ་བས་ཅི་བསྟན་ཞེ་ན་སེམས་འདོད་ཆགས་དང་བྲལ་བ་དང་། འདོད་ཆགས་དང་བཅས་པ་ཉིད་དོན་དམ་པར་མེད་པ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི། འོན་ཀྱང་ཀུན༌[^985]བརྟགས་པའི་བདག་ཉིད་དུ་ཡང་འདོད་ཆགས་དང་བྲལ་བའི་གནས་སྐབས་ན། འདོད་ཆགས་དང་བཅས་པ་ཞེས་བརྗོད་པར་མི་ནུས་ཏེ། འདོད་ཆགས་དང་བཅས་པ་དང་འདོད་ཆགས་དང་བྲལ་བ་གཉིས་སེམས༌[^986]གཅིག་ལ་མི་སྲིད་པ་དང་། སེམས་གཉིས་ཅིག་ཅར་མི་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1415]
དེ་བས་ན་ཡང་དག་པ་མ་ཡིན་པར་ཡང་མ་ཟད་ཀྱི། ཀུན་བརྟགས་པའི་རྣམ་པར་ཡང་འདོད་ཆགས་དང་བྲལ་བ་ལ་འདོད་ཆགས་དང་བཅས་པ་ཞེས་བྱར་མི་རུང་བས།

[Block 1416 [VERSE]]
འདོད་ཆགས་དང་བྲལ་བ་ཉིད་ཅེས་བཤད་དོ། །
དེ་བཞིན་དུ་ཞེ་སྡང་དང་བྲལ་བ་དང་།
གཏི་མུག་དང་བྲལ་བ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1417]
སེམས་རྒྱ་ཆེ་བ་ལ་རྒྱ་ཆེ༌[^987]ཞེས་བྱ་བ་དང་། རབ་འབྱོར་འདི་ལ་དེ་བཞིན་གཤེགས་པས་སེམས་ཅན་དེ་དག་གི་སེམས་རྒྱ་ཆེ་བ་མ་ཡིན་ཞུམ་པ་མ་ཡིན་པར་རབ་ཏུ་མཁྱེན་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་བསྟན་པར་འགྱུར་ཏེ། འདིའི་སེམས་ནི་རྒྱ་ཆེ་བའོ། །

[Block 1418]
གཞན་གྱི་སེམས་ནི་ཞུམ་པའོ། །

[Block 1419]
འདིའི་སེམས་ནི་འཕེལ་བའོ། །

[Block 1420]
གཞན་གྱི་སེམས་ནི་འགྲིབ་པའོ། །

[Block 1421]
འདིའི་སེམས་ནི་ཁྱབ་པར་འགྲོ་བའོ། །

[Block 1422]
གཞན་གྱི་སེམས་ནི་ཁྱབ་པར་འགྲོ་བ་མ་ཡིན་པའོ་ཞེས་བྱ་བར་མི་གཟིགས་ཀྱི། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ལ་བརྟེན་ནས། སེམས་རྒྱ་ཆེ་བ་དེ་དངོས་པོ་མེད་ཅིང་ཡོད་པ་མ་ཡིན་པ། ངོ་བོ་ཉིད་མེད་པར་རབ་ཏུ་མཁྱེན་པ་ནི་སེམས་རྒྱ་ཆེ་བ་ལ་སེམས་རྒྱ་ཆེ་བར་ཡོངས་སུ་མཁྱེན་ནས། དེ་ཡང་དག་པ་ཇི་ལྟ་བ་ཉིད་དུ་དངོས་པོ་མེད་པར་རབ་ཏུ་མཁྱེན་ཏོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 1423]
དེ་བཞིན་དུ་ཆེན་པོར་གྱུར་པ་ཞེས་བྱ་བ་འདིར་ཡང་རབ་འབྱོར་འདི་ལ་དེ་བཞིན་གཤེགས་པས་སེམས་ཅན་གཞན་དང་གང་ཟག་གཞན༌[^988]དག་གི་སེམས་འོང་བ་མེད་པ་དང་། འགྲོ་བ་མེད་པ་དང་གནས་པ་མེད་པ་དང་། [^989]སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པར་གཟིགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྟོན་ཏེ། ཆེན་པོ་ཞེས་བྱ་བ་འདི་ལ་ཆེན་པོ་ནི་སྐྱེ་བའི་དབང་དང་། ཡང་དག༌[^990]པར་གནས་པའི་དབང༌[^991]དང་གནས་ཤིང་ཡངས་པའི་མཚན་ཉིད་གཞན་དུ་གྱུར་པས་འགྱུར་རོ། །

[Block 1424]
གྱུར་པ་ཞེས་བྱ་བ་དེ་ནི་འོང་བ་དང་འགྲོ་བའི་དབང་གིས་འགྱུར་ཏེ། དེ་བཞིན་གཤེགས་པའི་ཤེས་རབ་ཀྱིས༌[^992]ནི་དེ་ལྟ་བུར་མི་གཟིགས་ཀྱི་དངོས་པོ་མེད་པར་ངོ་བོ་ཉིད་ཁོ་ནར་གཟིགས་སོ། །

[Block 1425]
དེ་ལྟར་ན་སེམས་ཆེན་པོར་གྱུར་པ་ལ་སེམས་ཆེན་པོར་འགྱུར་བ་མེད་པས་འདིའི་དངོས་པོ་མེད་པར་རབ་ཏུ་མཁྱེན་པ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1426]
སེམས་ཚད་མེད་པ་ཞེས་བྱ་བས་འདི་སྟོན་ཏེ། སེམས་ཅན་དེ་བདག༌[^993]གི་སེམས་དེ༌[^994]གནས་པ་མ་ཡིན་པ་དང་རྒྱུན་ཆད་པ་མ་ཡིན་པ་དང་། ཡོངས་སུ་གནས་པ་མ་ཡིན་པ་དང་། ཡོངས་སུ་མི་གནས་པ་མ་ཡིན་པར་ཡང་དག་པར་རྗེས་སུ་གཟིགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^995]འདི་སྐད་བསྟན་ཏེ། ཚད་མེད་པ་ནི་ཁྱབ་པར་གནས་པའམ། དབྱིབས་ཀྱི་དབང་གིས་འགྱུར་གྲང་ན། དེ་བཞིན་གཤེགས་པ་ནི་དེ་ལྟ་བུའི་ཚད་མེད་པ་འདི༌[^996]སེམས་མི་གཟིགས་ཀྱི་སེམས་ཐམས་ཅད་མི་གནས་པ་དང་། རྟེན་མེད༌[^997]པར་གཟིགས་ཏེ། དེ་ལྟར་གཟིགས་པ་ན་ཚད་མེད་པའི་སེམས་ཡང་དག་པ་ཇི་ལྟ་བ་ཉིད་དུ་རབ་ཏུ་མཁྱེན་ཏོ་ཞེས་བྱའོ། །

[Block 1427]
སེམས་དེ་མཚན་ཉིད་མེད་པ། ངོ་བོ་ཉིད་དང་བྲལ་བར་གཟིགས་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་མེད་པ་དང་། མཚན་ཉིད་མེད་པའི་ཕྱིར་བསྟན་པར་མི་ནུས་པས་བསྟན་དུ་མེད་པར་གཟིགས་སོ། །

[Block 1428]
སྤྱན་ལྔ་ལ་སེམས་དེ་དག་སྣང་བར་མི་འགྱུར་ཞེས་བྱ་བ་ནི་བསགས་པའི༌[^998]ཕྱིར་སེམས་ཏེ། ཀུན་བརྟགས་པ་ལ་བྱའོ། །

[Block 1429]
དེ་ཡང་དེའི་བདག་ཉིད་ཀྱིས་ཡོད་པ་མ་ཡིན་ཏེ། མེད་པ་ཉིད་ཀྱི་ཕྱིར་དེ་ཁོ་ན་གཟིགས་པ་རྣམས་ཀྱི་སྤྱན་ལ༌[^999]སྣང་བར་མི་འགྱུར་རོ། །

[Block 1430]
དེ་བས་ན་སེམས་ནི་བལྟར་མེད་པའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །།

[Block 1431]
བམ་པོ་ཉི་ཤུ་གཅིག་པ། སེམས་གསལ་བ་དང་། བྱིང་བ་དང་བཙུམས་པ་དང་།[^1000] བཀྲམ་པ་ཞེས་བྱ་བ་ནི་མུ་སྟེགས་ཅན་ལྟ་བ་ཕྱིན་ཅི་ལོག་པ་རྣམས་སེམས་རྟག་པར༌[^1001]འཛིན་པའི་དབང་གིས་ནི་གསལ་བའོ། །

[Block 1432]
ཆད་པར་འཛིན་པའི་དབང་གིས་ནི་བྱིང་བའོ། །

[Block 1433]
སྐུར་པ་འདེབས་པའི་དབང་གིས་ནི་བཙུམས༌[^1002]པའོ། །

[Block 1434]
སྒྲོ་འདོགས་པའི་དབང་གིས་ནི་བཀྲམ་པ་སྟེ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་མཁྱེན་ཏོ། །

[Block 1435]
གཟུགས་ལ་བརྟེན༌[^1003]ཅེས་བྱ་བ་ནི་ཕུང་པོ་ལྔ་ལས་བརྩམས་ཏེ་སྐྱེའོ༌[^1004]ཞེས་བྱ་བར་བསྟན་པའོ། །

[Block 1436]
དེ་ནི་གཟུགས་ལ་གནས་པའོ་ཞེས་བྱ་བ་ནི་གཟུགས་ལ་གནས་ཏེ་སེམས་འཕྲོ་བ་དང་། གཟུགས་བདག་གོ༌[^1005]ཞེས་མངོན་པར་ཞེན་ནས་སྨྲའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1437]
དེ་བཞིན་དུ་དེ་ནི་ཚོར་བ་ལ་གནས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1438]
དེ་བཞིན་དུ་ལྟ་བར་གྱུར་པ་ལས་སེམས་འཕྲོ་བ་ལ་སོགས་པ་ཡང་བསྟན་ནས། ད་ནི་རྣམ་པར་རྟོག་པའི་སྤྲོས་པའི་འཕྲོ་བ་ལ་སོགས་པས་བསྟན་པའི་ཕྱིར་གསུངས་པ། རབ་འབྱོར་གཞན་ཡང་དེ་བཞིན་གཤེགས་པས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ལ་བརྟེན་ནས༌[^1006]གཟུགས་མཁྱེན་ཏོ། །

[Block 1439 [HEADING]]
###### ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་སྟོན་པ། ^1-2-5-12-4-0

[Block 1440]
གཟུགས་ཇི་ལྟར་མཁྱེན་ཞེ་ན་ཇི་ལྟར་དེ་བཞིན་ཉིད་དུ༌[^1007]འགྱུར་བ་མེད་ཅིང་རྣམ་པར་རྟོག་པ་མེད་ལ། མཚན་མ་མེད་ཅིང་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམ་པ་དྲུག་གིས་ཆོས་ཐམས་ཅད་དེ་བཞིན་ཉིད་དུ༌[^1008]བདག་ཉིད་དུ་མཁྱེན་ཏོ། །
--- END BLOCKS ---
