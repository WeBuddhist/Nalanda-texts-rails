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
[Block 826]
སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པ་ནི་ཡང་སྲིད་པར་སྐྱེ་བ་དང་། སྐྱེས་པའི༌[^336]སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་སྐད་ཅིག་རེ་རེ་ལ་བྱུང་བ༌[^337]དང་། ཡང་སྲིད་པའི་རྒྱུན་ཏོ། །

[Block 827]
དེའི་གཉེན་པོ་ནི་སྐྱེ་བ་མེད་པ་ཤེས་པ་དང་། འབྱུང་བ་མེད་པ་ཤེས་པ་དང་། ངོ་བོ་ཉིད་མེད་པ་ཤེས་པའོ། །

[Block 828]
ཀུན་ནས་ཉོན་མོངས་པ་རྣམ་པ་དེ་གསུམ་དང་བྲལ་བ་ནི་རྣམ་པར་བྱང་བའོ། །

[Block 829]
དེ་ལ་སྟོང་པ་ཉིད་ཤེས་པ་ལ་སོགས་པས་ཤེས་བྱ་སྟོང་པ་ཉིད་ལ་སོགས་པའི་ཆོས་རྣམས་ཀུན་ནས་ཉོན་མོངས་པ་རྣམ་པ་གསུམ་པོ་དེ་དག་དང་ཅི་རིགས་པར་སྟོང་པ་ཉིད་ལ་སོགས་པའི་བར་དུ་མི་བྱེད་ཀྱི། རང་བཞིན་གྱིས་སྟོང་པ་ཉིད་ལ་སོགས་ཏེ། ཆོས་ཀྱི་དབྱིངས་རང་བཞིན་གྱིས་ཀུན་ནས་ཉོན་མོངས་པ་ཅན་དུ་མ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 830]
གལ་ཏེ་ཆོས་ཀྱི་དབྱིངས་ཀུན་ནས་ཉོན་མོངས་པར་གྱུར་པའམ། རྣམ་པར་དག་པར་འགྱུར་བའོ་སྙམ་དུ་རྣམ་པར་རྟོག་པ་འདི་ནི་མཐའ་སྟེ། རང་བཞིན་གྱིས་ཀུན་ནས་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ལ་ནི༌[^338]ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 831]
མཐའ་དེ་གཉིས་ཡོངས་སུ་སྤང་བའི་ཕྱིར༌[^339]དབུ་མའི་ལམ་སྟེ། གང་སྟོང་པ་ཉིད་ཀྱིས་ཆོས་རྣམས་སྟོང་པར་མི་བྱེད༌[^340]ཀྱི་ཆོས་རྣམས་ཉིད་ཀྱིས་སྟོང་པའོ་ཞེས་འབྱུང་བ་ལ་སོགས་པའོ། །

[Block 832]
གཞན་ཡང་རྣམ་པར་རྟོག་པའི་མཐའ་གཉིས་རྣམ་པ་བདུན་ཏེ། འདི་ལྟ་སྟེ། དངོས་པོ་ཡོད་པར་རྣམ་པར་རྟོག་པ་ཡང་མཐའོ། །

[Block 833]
དངོས་པོ་མེད་པར་རྣམ་པར་རྟོག་པ་ཡང་མཐའོ། །

[Block 834]
[^341]གང་ཟག་ཡོད་དེ༌[^342]དེ་གཞིག་པའི་ཕྱིར་སྟོང་པ་ཉིད་དོ། །

[Block 835]
ཡང་ན་བདག་མེད་པ་ཡང་མེད་དོ་སྙམ་དུ་རྟོག་པའི་ཕྱིར་ཏེ། རྣམ་པར་རྟོག་པའི་མཐའ་འདི་གཉིས་སྤང་བའི་ཕྱིར་དབུ་མའི་ལམ་སྟེ། འདི་ལྟ་སྟེ། གང་ཟག་རྣམ་པར་གཞིག་པའི་ཕྱིར་སྟོང་པ་ཉིད་མ་ཡིན་གྱི་སྟོང་པ་ཉིད་ཀྱིས་སྟོང་སྟེ། སྔོན་གྱི་མཐའ་སྟོང་པ་དང་། ཕྱི་མའི་མཐའ་སྟོང་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱ་ཆེར་འབྱུང་བའོ། །

[Block 836]
ཞི་བར་བྱ་བ༌[^343]རྣམ་པ་ཡང་མཐའོ། །

[Block 837]
ཞི་བར་བྱེད་པ་རྣམ་པར༌[^344]རྟོག་པ་ཡང་མཐའ་སྟེ། སྤང་བར་བྱ་བ་དང་། སྤོང་བར་བྱེད་པ་རྣམ་པར་རྟོག་པས་སྟོང་པ་ཉིད་ཀྱིས༌[^345]སྐྲག་པའི་ཕྱིར་རོ། །

[Block 838]
རྣམ་པར་རྟོག་པའི་མཐའ་དེ་གཉིས་ཡོངས་སུ་སྤང་བའི༌[^346]ཕྱིར་དཔེ་ནམ་མཁའོ། །

[Block 839]
སྐྲག་པར་བྱ་བར་རྣམ་པར་རྟོག་པ་ཡང་མཐའོ། །

[Block 840]
སྐྲག་པར་བྱ་བ་དེ་ལས་འཇིགས་པར་རྣམ་པར་རྟོག་པ་ཡང་མཐའ་སྟེ། སྡུག་བསྔལ་གྱིས་ཁོང་དངངས༌[^347]པས་ཀུན་བརྟགས་པའི་གཟུགས་ལ་སོགས་པ་ལ་སྐྲག་པའི་ཕྱིར་རོ། །

[Block 841]
རྣམ་པར་རྟོག་པའི་མཐའ་དེ་གཉིས་ཡོངས་སུ་སྤང་བའི༌[^348]ཕྱིར་དཔེ་ནི་རི་མོ་མཁན་ནོ། །

[Block 842]
དཔེ་སྔ་མ་ནི་ཉན་ཐོས་རྣམས་ལས་བརྩམས་པའོ། །

[Block 843]
འདི་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལས་བརྩམས་པའོ། །

[Block 844]
གཟུང་བར་རྣམ་པར་རྟོག་པ་ཡང་མཐའོ། །

[Block 845]
འཛིན་པར་རྣམ་པར་རྟོག་པ་ཡང་མཐའོ། །

[Block 846]
རྣམ་པར་རྟོག་པའི་མཐའ་དེ་གཉིས་ཡོངས་སུ་སྤང་བའི་ཕྱིར་དཔེ་སྒྱུ་མ་མཁན་ནོ། །

[Block 847]
རྣམ་པར་རིག་པ་ཙམ་དུ་ཤེས་པས་དོན་དངོས་པོ་མེད་པར་བྱས་ནས། དོན་དངོས་པོ་མེད་པར་ཤེས་པ་དེས་ཀྱང་རྣམ་པར་རིག་པ་ཙམ་དུ་ཤེས་པ་དེ་ཉིད་རྣམ་པར་བཟློག་གོ། །

[Block 848]
དོན་དངོས་པོ་མེད་ན་རྣམ་པར་རིག་པ་མི་སྲིད་པའི་ཕྱིར་ཏེ། དེ་ལྟར་ན་འདི་ནི་འདིར་མཚུངས་སོ། །

[Block 849]
ཡང་དག་པ་ཉིད་དུ་རྣམ་པར་རྟོག་པ་ཡང་མཐའོ། །

[Block 850]
ལོག་པ་ཉིད་དུ་རྣམ་པར་རྟོག་པ་ཡང་མཐའ་སྟེ། ཡང་དག་པར་སོ་སོར་རྟོག་པ་ན་ཡང་དག་པ་ཉིད་དུ་འམ། ལོག་པ་ཉིད་དུ་རྟོག་པའོ། །

[Block 851]
མཐའ་དེ་གཉིས་ཡོངས་སུ་སྤང་བའི་ཕྱིར་དཔེ་ཤིང་གཉིས་ལས་མེ་འབྱུང་བ་སྟེ། དཔེར་ན་མེའི་མཚན་ཉིད་མ་ཡིན་པ་ཤིང་གཉིས་ལས་མེ་འབྱུང་སྟེ། བྱུང་ནས་ཀྱང་ཤིང་གཉིས་ཚིག་པར་བྱེད་དོ། །

[Block 852]
དེ་བཞིན་དུ་ཡང་དག་པ་ཉིད༌[^349]ཀྱི་མཚན་ཉིད་མ་ཡིན་པ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་སོ་སོར་རྟོག་པ་ལས་ཡང་དག་པ་ཉིད་ཀྱི་མཚན་ཉིད་འཕགས་པའི་ཤེས་རབ་ཀྱི་དབང་པོ་སྐྱེ་སྟེ། སྐྱེས་ནས་ཀྱང་ཡང་དག་པར་སོ་སོར་རྟོག་པ་དེ་ཉིད་རྣམ་པར་འཇིག་པར་བྱེད་དེ། དེ་ལྟ་བས་ན་འདི་ནི་འདིར་མཚུངས་སོ། །

[Block 853]
ཡང་དག་པར་སོ་སོར་རྟོག་པ་ཡང་དག་པ་ཉིད་ཀྱི་མཚན་ཉིད་མ་ཡིན་ཀྱང་ལོག་པ་ཉིད་ཀྱི་མཚན་ཉིད་ཀྱང༌[^350]མ་ཡིན་ཏེ། ཡང་དག་པ་ཉིད་ཀྱི་རྗེས་སུ་མཐུན་པའི་ཕྱིར་རོ། །

[Block 854]
བྱེད་པར་རྣམ་པར་རྟོག་པ་ཡང་མཐའོ། །

[Block 855]
མི་བྱེད་པར་རྣམ་པར་རྟོག་པ་ཡང་མཐའ་སྟེ། ཡེ་ཤེས་ནི༌[^351]བློ་སྔོན་དུ་འགྲོ་བས་བྱེད་པའམ་མཐུ་མེད་པར་རྟོག་པའོ། །

[Block 856]
རྣམ་པར་རྟོག་པའི་མཐའ་དེ་གཉིས་ཡོངས་སུ་སྤང་བའི་ཕྱིར་དཔེ་མར་མེའོ། །

[Block 857]
སྐྱེ་བ་མེད་པར་རྣམ་པར་རྟོག་པ་ཡང་མཐའོ། །

[Block 858]
དུས་མཉམ་པ་ཉིད་དུ་རྣམ་པར་རྟོག་པ་ཡང་མཐའ་སྟེ། གལ་ཏེ་གཉེན་པོ་མ་སྐྱེས་པའམ། ཀུན་ནས་ཉོན་མོངས་པ་ཡུན་རིང་བ་ཉིད་དུ་རྟོག་པའོ། །

[Block 859]
རྣམ་པར་རྟོག་པའི་མཐའ་དེ་གཉིས་སྤང་བའི་ཕྱིར་མར་མེའི་དཔེ་གཉིས་པའོ། །

[Block 860]
མཐའ་གཉིས་སྤང་བའི་སྒྲུབ་པ་བཤད་ཟིན་ཏོ། །

[Block 861 [HEADING]]
#### ཁྱད་པར་ཅན་སྒྲུབ་པ། ^7-1-5-0

[Block 862]
ཁྱད་པར་ཅན་དང་ཁྱད་པར་མེད་པ་སྒྲུབ་པ་གང་ཞེ་ན།

[Block 863 [VERSE]]
ཁྱད་པར་ཅན་དང་ཁྱད་མེད༌[^352]ནི། །
ས་བཅུ་དག་ཏུ་ཤེས་པར་བྱ། །

[Block 864]
ས་གང་ལ་ཕ་རོལ་ཏུ་ཕྱིན་པ་གང་གི་ཤས་ཆེ་བ་དེ་ནི་ཁྱད་པར་ཅན་ནོ། །

[Block 865 [HEADING]]
#### ཁྱད་པར་མེད་པ་སྒྲུབ་པ། ^7-1-6-0

[Block 866]
ཐམས་ཅད་དུ་ཐམས་ཅད་ལ་ཡང་དག་པར་བསྒྲུབ་པ་ནི༌[^353]ཁྱད་པར་མེད་པའོ། །

[Block 867]
བསྒྲུབ་པ་བླ་ན་མེད་པ་ཉིད་བཤད་ཟིན་ཏོ། །

[Block 868 [HEADING]]
### དམིགས་པ་བླ་ན་མེད་པ་ཉིད། ^7-2-0

[Block 869]
དམིགས་པ་བླ་ན་མེད་པ་ཉིད་གང་ཞེ་ན།

[Block 870 [VERSE]]
རྣམ་པར་གཞག་དང་དེ་བཞིན་དབྱིངས། །
བསྒྲུབ༌[^354]དང་སྒྲུབ་དང་འཛིན་པ་དང་། །
ངེས་པར་འཛིན་དང་རབ་ཏུ་འཛིན། །
རབ་ཏུ་རྟོགས་དང་རབ་རྒྱས་དང་། །

[Block 871 [VERSE]]
རྣམ་པར་རྟོག་དང་རྣལ་འདུག་དང་། །
ཕུལ་དུ་བྱུང་བའི་དམིགས་པར་འདོད། །

[Block 872]
དམིགས་པ་ནི་རྣམ་པ་བཅུ་གཉིས་པོ་འདི་དག་སྟེ། འདི་ལྟར་ཆོས་བརྟགས་པ་རྣམ་པར་གཞག་པའི་དམིགས་པ་དང་། ཆོས་ཀྱི་དབྱིངས་ཀྱི་དམིགས་པ་དང་། བསྒྲུབ་བྱའི་དམིགས་པ་དང་། [^355]སྒྲུབ་པའི་དམིགས་པ་དང་། འཛིན་པའི་དམིགས་པ་དང་། ངེས་པར་འཛིན་པའི་དམིགས་པ་དང་། རབ་ཏུ་འཛིན་པའི་དམིགས་པ་དང་། རབ་ཏུ་རྟོགས་པའི༌[^356]དམིགས་པ་དང་། རབ་ཏུ་རྒྱས་པའི་དམིགས་པ་དང་། རྣམ་པར་ཁོང་དུ་ཆུད་པའི་དམིགས་པ་དང་། རྣལ་དུ་འདུག་པའི་དམིགས་པ་དང་། ཕུལ་དུ་བྱུང་བའི་དམིགས་པའོ།[^357] །དེ་ལ་དང་པོ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པའི་ཆོས་གང་དག་རྣམ་པར་འཇོག་པའོ། །

[Block 873]
གཉིས་པ་ནི་དེ་བཞིན་ཉིད་དོ། །

[Block 874]
གང་གསུམ་པ་དང་བཞི་པ་དེ་དག་ཉིད་ལ་གོ་རིམས་བཞིན་ཏེ། ཆོས་ཀྱི་དབྱིངས་རབ་ཏུ་རྟོགས་པས༌[^358]ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པའི་ཆོས་རྣམས་ཁོང་དུ་ཆུད་པའི་ཕྱིར་རོ། །

[Block 875]
ལྔ་པ་ནི་ཐོས་པ་ལས་བྱུང་བའི་ཤེས་པའི་དམིགས་པའོ། །

[Block 876]
དྲུག་པ་ནི་བསམས་པ༌[^359]ལས་བྱུང་བའི་སྟེ་རྟོགས་ནས་འཛིན་པའི་ཕྱིར་རོ། །

[Block 877]
བདུན་པ་ནི་བསྒོམས་པ་ལས་བྱུང་བའི་སྟེ། སོ་སོ་རང་གིས་འཛིན་པའི་ཕྱིར་རོ། །

[Block 878]
བརྒྱད་པ་ནི་ས་དང་པོ་ལ་མཐོང་བའི་ལམ་གྱིའོ། །

[Block 879]
དགུ་པ་ནི་བསྒོམ་པའི་ལམ་གྱི་སྟེ། ས་བདུན་པའི་བར་དུའོ། །

[Block 880]
བཅུ་པ་ནི་དེ་ཉིད་ལ་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་ལམ་གྱི་སྟེ། ཆོས་རྣམ་པར་ཁོང་དུ་ཆུད་པའི་ཕྱིར་རོ། །

[Block 881]
བཅུ་གཅིག་པ་ནི་ས་བརྒྱད་པ་ལའོ། །

[Block 882]
བཅུ་གཉིས་པ་ནི་ས་དགུ་པ་ལ་སོགས་པ་གསུམ་ལའོ། །

[Block 883]
དང་པོའི་གཉིས་པོ་དེ་དག་ནི་དེ་དང་དེའི་དུས་ན་དེ་དང་དེའི་དམིགས་པའི་མིང་འཐོབ་པོ། །དམིགས་པ་བཤད་ཟིན་ཏོ། །

[Block 884 [HEADING]]
### ཡང་དག་པར་འགྲུབ་པ་བླ་ན་མེད་པ་ཉིད། ^7-3-0

[Block 885]
ཡང་དག་པར་འགྲུབ་པ་གང་ཞེ་ན།

[Block 886 [VERSE]]
མ་ཚང་མེད་དང་མི་སྤོང་དང་། །
མི་གཡེང་བ་དང་རབ་རྫོགས་དང་། །
ཡང་དག་སྐྱེད༌[^360]དང་འཕེལ་བ་དང་། །
ལས་སུ་རུང་དང་མི་གནས་དང་། །

[Block 887 [VERSE]]
སྒྲིབ་པ་མེད་པ་ཉིད་དང་དེ། །
རྒྱུན་མི་གཅོད་པ་ཡང་དག་འགྲུབ། །

[Block 888]
ཡང་དག་པར་འགྲུབ་པ་ནི་རྣམ་པ་བཅུ་པོ་འདི་དག་སྟེ། དེ་ལ་རྐྱེན་མ་ཚང་བ་མེད་པ་ནི་རིགས་ཡང་དག་པར་འགྲུབ་པའོ། །

[Block 889]
ཐེག་པ་ཆེན་པོ་མི་སྤང་བ་ནི་མོས་པ་ཡང་དག་པར་འགྲུབ་པའོ། །

[Block 890]
ཐེག་པ་དམན་པར་མི་གཡེང་བ་ནི༌[^361]སེམས་བསྐྱེད་པ༌[^362]ཡང་དག་པར་འགྲུབ་པའོ། །

[Block 891]
ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པ་ནི་བསྒྲུབ་པ་ཡང་དག་པར་འགྲུབ་པའོ། །

[Block 892]
འཕགས་པའི་ལམ་བསྐྱེད་པ་ནི་སྐྱོན་མེད་པར་འཇུག་པ་ཡང་དག་པར་འགྲུབ་པའོ། །

[Block 893]
དགེ་བའི་རྩ་བ་འཕེལ་བ་ནི་ཡུན་རིང་པོ་ནས་འདྲིས་པར་བྱ་བའི་ཕྱིར་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པ་ཡང་དག་པར་འགྲུབ་པའོ། །

[Block 894]
སེམས་ལས་སུ་རུང་བ་ནི་ཞིང་ཡོངས་སུ་དག་པ་ཡང་དག་པར་འགྲུབ་པའོ། །

[Block 895]
འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ལ་མི་གནས་པ་ནི་ཕྱིར་མི་ལྡོག་པའི་ས་ལ་ལུང་བསྟན་པ་འཐོབ་པ་ཡང་དག་པར་འགྲུབ་པ་སྟེ། འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་གཉིས་ལས་མི་ལྡོག་པའི་ཕྱིར་རོ། །

[Block 896]
སྒྲིབ་པ་མེད་པ་ནི་སངས་རྒྱས་ཀྱི་ས་ཡང་དག་པར་འགྲུབ་པའོ། །

[Block 897]
དེ་རྒྱུན་མི་གཅོད་པ་ནི་བྱང་ཆུབ་ཀུན་དུ་སྟོན་པ་ཡང་དག་པར་འགྲུབ་པའོ། །

[Block 898]
དེ་ལྟར་ན་འདི་ནི། དབུས་རྣམ་འབྱེད་པའི་བསྟན་བཅོས་ཏེ། །དབུ་མའི་ལམ་རབ་ཏུ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 899]
འདི་ནི་དབུས་དང་མཐའ་རྣམ་པར་འབྱེད་པ་ཡང་ཡིན་ཏེ། དབུས་དང་མཐའ་གཉིས་རབ་ཏུ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 900]
ཡང་ན་ཐོག་མ་དང་མཐའ་མ་སྤངས་པའི་དབུས་རབ་ཏུ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 901]
རྟོག་པར༌[^363]དཀའ་དང་སྙིང་པོའི༌[^364]དོན། །རྟོག་གེའི༌[^365]སྤྱོད་ཡུལ་མ་ཡིན་པ་དང་། ཕས་ཀྱི་རྒོལ་བ་དག་གིས་མི་ཤིགས་པའི་ཕྱིར་ཏེ་གོ་རིམས་བཞིན་ནོ། །

[Block 902]
དོན་ཆེན་ནི་བདག་དང་གཞན་གྱི་དོན་གྱི༌[^366]ཆེད་ཀྱི་ཕྱིར་རོ། །

[Block 903]
དེ་བཞིན་ཀུན་གྱི་དོན་ནི་ཐེག་པ་གསུམ་ཆར་གྱི་དབང་དུ་བྱས་པའི་ཕྱིར་རོ། །

[Block 904]
དོན་མེད་ཐམས་ཅད་སེལ་བའོ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་སྤོང་བར་བྱེད་པའོ། །

[Block 905]
བླ་ན་མེད་པ་ཉིད་ཀྱི་དོན་བསྡུས་པ་ནི་མདོར་བསྡུ་ན་བླ་ན་མེད་པ་ཉིད་རྣམ་གསུམ་སྟེ། སྒྲུབ་པ༌[^367]དང་། བསྒྲུབ་པའི་གཞི་དང་། བསྒྲུབས་པའི༌[^368]འབྲས་བུའོ། །
--- END BLOCKS ---
