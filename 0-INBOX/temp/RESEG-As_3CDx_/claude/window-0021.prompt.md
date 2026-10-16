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
[Block 736]
གཞན་ནི་བརྫུན་པའོ་ཞེས་བྱ་བ་ནི་འདི་ལས་བདེན་པ༌[^565]ལྷག་པ་ལོགས་ཤིག་ན་མེད་དོ་ཞེས་ཟེར་བ་ནི་དེ་ནི་དེ་དག་གི་ཕྱིར༌[^566]ཉེ་བར་བརྟག་པར་བྱ་དགོས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེའི་ཚེ་ན་ལོག་པར་རྟོག་པའི་ཕྱིར་རོ། །

[Block 737 [HEADING]]
###### **རྣམ་པར་བྱང་བའི་ཕྱོགས་དང་མཐུན་པའི་དཔེའི་དངོས་པོ།** ^4-1-1-3-1-2-0

[Block 738]
དེ་ལ་སེམས་ཅན་གང་དག་བྱིས་པའི་རང་བཞིན་ཅན་མ་ཡིན་པ། རྨོངས་པའི་རང་བཞིན་ཅན་མ་ཡིན་པ། ཤེས་རབ་དང་ལྡན་པའི་རང་བཞིན་ཅན་ཞེས་བྱ་བ་ནི་སྔ་མ་ལས་བཟློག་པ༌[^567]ཡིན་ནོ། །

[Block 739]
སྣང་བ་གང་ཡིན་པ་འདི་ནི་མེད་དོ་ཞེས་བྱ་བ་ཡང་སྔ་མ་ལས་བཟློག་པ་ཡིན་ནོ། །

[Block 740]
རྣམ་གྲངས་ཀྱི་འདུ་ཤེས་ཞེས༌[^568]བྱ་བ་ནི་དེ་དག་གི་དངོས་པོ་གཅིག་ལ་ཡང་མིང་གི་རྣམ་གྲངས་ཐ་དད་པ་དུ་མར་འདོགས་པའི་འདུ་ཤེས་འབྱུང་བའོ། །

[Block 741]
སྒྱུ་མ་བྱས་པ་འདི་ནི་ཡོད་ཅེས་བྱ་བ་ནི་གླང་པོ་ཆེ་ལ་སོགས་པའི་མཚན་མ་སེམས་ལས་བྱུང་བ་སྣང་བ་ཙམ་གྱི༌[^569]མཚན་མ་སྟེ། དེས་ནི་སྒྱུ་མ་ལ་ཡང་གླང་པོ་ཆེ་ལ་སོགས་པ་ལོག་པར་མི་འཛིན་པ་བསྟན་ཏོ། །

[Block 742]
མི་སླུ་བར༌[^570]བྱེད་པ་འདི་ནི་ཡོད་དོ་ཞེས་བྱ་བས་ནི་སྒྱུ་མའི་སྒྱུ་རྩལ་ལ་སོགས་པ་དེ་དག་ལ་ཡང་ཕྱི་རོལ་གྱི་དངོས་པོ་ལོག་པར་མི་འཛིན་པ་བསྟན་ཏོ། །

[Block 743]
རྗེས་སུ་ཐ་སྙད་མི་འདོགས་ཀྱི་ཞེས་བྱ་བས་ནི་དཔེས་མཚོན་པའི་དོན་གྱི་འཇུག༌[^571]ནས་འཕགས་པའི་ཤེས་པ་དང་། འཕགས་པའི་བདེན་པས་བརྗོད་དུ་མེད་པར་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ཤིང་ཞེས་འབྱུང་བའི་དོན་དེ་མཚོན་པར་བྱེད་དོ། །

[Block 744]
འདི་ལྟར་དོན་རྣམ་པར་རིག་པར་བྱ་བའི་ཕྱིར་རྗེས་སུ་ཐ་སྙད་འདོགས་པར་བྱེད་དེ་ཞེས་བྱ་བས་ནི་དཔེས་མཚོན་པའི་དོན་གྱི་འཇུག༌[^572]ནས་བརྗོད་དུ་མེད་པའི་ཆོས་ཉིད་དེ་ཉིད་མངོན་པར་རྫོགས་པར་རྟོགས་པར་བྱ་བའི་ཕྱིར་འདུས་བྱས་དང་འདུས་མ་བྱས་ཞེས་མིང་དུ་བཏགས་པ་ཡིན་ནོ་ཞེས་འབྱུང་བའི་དོན་དེ་མཚོན་པར་བྱེད་དེ། འདི་ལྟར་དོན་རྣམ་པར་རིག་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་དོན་གང་ཡིན་པ་ཉིད་ལ་མིང་དེ་སྐད་བཏགས་པའི་དོན་དེ་རྣམ་པར་རིག་པར་བྱ་བའི་ཕྱིར་མིང་དེ་སྐད་ཅེས་རྗེས་སུ་ཐ་སྙད་འདོགས་པར་བྱེད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 745]
དེ་ནི་དེ་དག་གིས༌[^573]ཕྱིས་ཉེ་བར་བརྟག་པར་བྱ་མི་དགོས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེའི་ཚེ་ན་གཏན་ལ་བབ་པར་རྟོགས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 746]
དེ་དག་ནི་དཔེའི་དངོས་པོ་རྣམ་པར་གཞག་པ་རྣམ་པ་གཉིས་ཀྱིས༌[^574]ཚིག་གི་དོན་བཤད་པ་ཡིན་ནོ། །

[Block 747 [HEADING]]
###### དཔེས་མཚོན་པའི་དོན། ^4-1-1-3-2-0

[Block 748]
ད༌[^575]ནི་དཔེས་མཚོན་པའི་དོན་རྣམ་པ་གཉིས་ཀྱིས༌[^576]ཚིག་གི་དོན་བཤད་པར་བྱ་སྟེ། དེ་ལ་དེ་བཞིན་དུ་སེམས་ཅན་གང་དག་བྱིས་པའི་རང་བཞིན་ཅན་སོ་སོའི་སྐྱེ་བོར་གྱུར་པ་ཤེས་རབ་འཕགས་པ་འཇིག་རྟེན་ལས་འདས་པ་མ་ཐོབ་པ་སྟེ། གོ་རིམས༌[^577]བཞིན་དུ་སྦྱར་རོ། །

[Block 749]
འདུས་བྱས་དང་འདུས་མ་བྱས་དེ་མཐོང་ངམ། ཐོས་ན་ཞེས་བྱ་བ་ནི་འདུས་བྱས་ཀྱི་མཚན་མ་དང་འདུས་མ༌[^578]བྱས་ཀྱི་མཚན་མ་རྣམ་པར་རིག་པ་ཙམ་དེ་མཐོང་ངམ་ཐོས་ནས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 750]
སྣང་བ་གང་ཡིན་པ་དེ་ནི་ཡོད་དོ་སྙམ་དུ་སེམས་ཤིང་ཞེས་བྱ་བས་ནི་ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་ལ་མངོན་པར་ཞེན་པ་བསྟན་ཏོ། །

[Block 751]
དེ་དག་ཇི་ལྟར་མཐོང་བ་དང་ཇི་ལྟར་ཐོས་པ་བཞིན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་ལ་ལོག་པར་མངོན་པར་ཞེན་པ་བསྟན་ཏོ། །

[Block 752]
དེ་ནི་དེ་དག་གི༌[^579]ཕྱིས་ཉེ་བར་བརྟག་པར་བྱ་དགོས་པ་ཡིན་ནོ༌[^580]ཞེས་བྱ་བས་ནི་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་མ་མཐོང་བ་བསྟན་ཏོ། །

[Block 753]
དེ་ལ་སེམས་ཅན་གང་དག་བྱིས་པའི་རང་བཞིན་ཅན་མ་ཡིན་པ་བདེན་པ་མཐོང་བ་ཤེས་རབ་འཕགས་པ་འཇིག་རྟེན་ལས་འདས་པ་ཐོབ་པ་ཆོས་ཐམས་ཅད་ཀྱི་བརྗོད་དུ་མེད་པའི་ཆོས་ཉིད་མངོན་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་སྔ་མ་ལས་བཟློག་པ་ཡིན་ནོ། །

[Block 754]
འདུས་བྱས་དང་འདུས་མ་བྱས་སྣང་བ་གང་ཡིན་པ་འདི་ནི་མེད་ཀྱི་ཞེས་བྱ་བ་ནི་ཕྱི་རོལ་ན་རྫས་སུ་གྲུབ་པའི་ཡུལ་དུ་གྱུར་པ་མེད་པའོ། །

[Block 755]
འདིར་གང་ལ་བརྗོད་པ་འཇུག་པར་འགྱུར་བ་དེ་ཉིད་ཀྱི་དབང་དུ་བྱས་པའི་ཕྱིར་འདུས་བྱས་དང་འདུས་མ་བྱས་ཞེས་བྱ་བ་ལ་སོགས་པ་བཏགས་པའི་ཡོད་པ་གང་ཡིན་པ་དེ་དག་མེད་པར་བསྟན་ཏོ། །

[Block 756]
རྫས་སུ་ཡོད་པ་དེ་བཞིན་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུ་ཡིན་ཡང་རྣམ་པར་རིག་པ་ཙམ་དུ་ཡོད་པར་འདོད་ན་གནོད་པ་མེད་དེ། དེའི་ཕྱིར་གང་ལ་འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་འདུ་ཤེས་དང་། འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་རྣམ་གྲངས་ཀྱི་འདུ་ཤེས་འབྱུང་བ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་བཞིན་ཉིད་ལ་ནི་འདུ་ཤེས་འབྱུང་བར༌[^581]འགྱུར་བ་མེད་དེ། འབྱུང་ན་ཡང་དེའི་མཚན་མ་ལ་འབྱུང་བས་དེ་ཡང་རྣམ་པར་རིག་པ་ཙམ་ཉིད་ཡིན་ཏེ། དེའི་ཕྱིར་རྣམ་པར་རྟོག་པ་ལས་བྱུང་བ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 757]
འདུ་བྱེད་ཀྱི་མཚན་མ་ཞེས་བྱ་བ་ནི་དངོས་པོ་ལ་གཟུགས་དང་། སྒྲ་དང་། དྲི་དང་། རོ་དང་། རེག་བྱ་དང་། སྐྱེས་པ་དང་། བུད་མེད་དང་། སྐྱེ་བ་དང་། རྒ་བ་དང་། ན་བ་དང་། འཆི་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུ་ལྷག་པར་སྒྲོ་བཏགས་པ་གང་ཡིན་པ་སྟེ། དེ་ཉིད་རྣམ་པར་རིག་པ་ཙམ་གྱི་མཚན་མ་ཡིན་ནོ། །

[Block 758]
དེ་བཞིན་ཉིད་ཀྱི་མཚན་མ་གང་ཡིན་པ་དེ་ཡང་འདུ་ཤེས༌[^582]ཀྱི་མཚན་མ་ཁོ་ན་སྟེ། འདུས་བྱས་པའི་ཕྱིར་རོ། །

[Block 759]
སྒྱུ་མ་ལྟ་བུ་འདི་ནི་ཡོད་ཅེས་བྱ་བ་ནི་ཕྱི་རོལ་གྱི་དངོས་པོར་ཡོད་པ་མ་ཡིན་གྱི་རྣམ་པར་རིག་པ་ཙམ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 760]
བློ་རྣམ་པར་རྨོངས་པར་བྱེད་པ་འདི་ནི་ཡོད་དོ་ཞེས་བྱ་བ་ནི་ཡང་དག་པ་མ་ཡིན་པའི་ཀུན་དུ་རྟོག་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་ཏེ། དེ་དག་གིས་ནི་ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་ལ་མངོན་པར་ཞེན་པ་མེད་པར་བསྟན་ཏོ། །

[Block 761]
དེ་དག་ཇི་ལྟར་མཐོང་བ་དང༌[^583]ཇི་ལྟར་ཐོས་པ་བཞིན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་ལ་ལོག་པར་མངོན་པར་ཞེན་པ་མེད༌[^584]པར་བསྟན་ཏོ། །

[Block 762]
འདི་ལྟར་དོན་རྣམ་པར་རིག་པར་བྱ་བའི་ཕྱིར་རྗེས་སུ་ཐ་སྙད་འདོགས་པར་བྱེད་དེ་ཞེས་བྱ་བ་ནི་ཀུན་རྫོབ་ཀྱི་ཤེས་པ་དང་མཐོང་བ་སྟེ། འོག་ནས་བརྗོད་དུ་མེད་པའི་ཆོས་ཉིད་དེ་ཉིད་མངོན་པར་རྫོགས་པར་རྟོགས་པར་བྱ་བའི་ཕྱིར་འདུས་བྱས་དང་འདུས་མ་བྱས་ཞེས་མིང་དུ་བཏགས་པ་ཡིན་ནོ་ཞེས་འབྱུང་བ་དང་སྦྱར་རོ། །

[Block 763]
དེ་ནི་དེ་དག་གིས་ཕྱིས༌[^585]ཉེ་བར་བརྟག་པར༌[^586]བྱ་མི་དགོས་པ་ཡིན་ནོ་ཞེས་བྱ་བས་ནི་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་གྲུབ་པར༌[^587]བསྟན་ཏོ། །

[Block 764]
རིགས་ཀྱི་བུ་དེ་ལྟར་ན་ཞེས་བྱ་བ༌[^588]ལ་སོགས་པས་ནི་དོན་གྱི་མཇུག་བསྡུ་བ༌[^589]བསྟན་ཏེ། དེ་ལྟར་ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་དང་བྲལ་བ་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་ཀྱིས་དངོས་པོ་དེ༌[^590]ཤེས་པ་དང་མཐོང་བས་རྟོགས་པ་ནི་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་མཐོང་བ་ཡིན་པས་དེ་ནི་ཆོས་རྣམས་ཀྱི་དེ་བཞིན་ཉིད་དོན་དམ་པ་ཆོས་བདག་མེད་པ་ཉིད་གཉིས་སུ་མེད་པའི་མཚན་ཉིད་ཡིན་པས་བརྗོད་དུ་མེད་པའི་མཚན་ཉིད་ཀྱང་ཡིན་ཏེ། དེ་ནི་རྣམ་པར་གཏན་ལ་དབབ་པའི་དཔེའི་དངོས་པོ་རྣམ་པར་གཞག་པ་ཡིན་ནོ། །

[Block 765 [HEADING]]
##### དངོས་པོ་བསྡུ་བ་རྣམ་པར་གཞག་པ། ^4-1-1-4-0

[Block 766]
དེའི་འོག་ཏུ་དེ་དག་གི་དངོས་པོ་བསྡུ་བའི་རྣམ་པར་གཞག་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། དེ་དག་གི་དངོས་པོ་བསྡུ་བ་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་ནི་དོན་དམ་པ་བརྗོད་དུ་མེད་པའི་མཚན་ཉིད་དང་གཉིས་སུ་མེད་པའི་མཚན་ཉིད༌[^591]དང་ལྡན་པ་སྔར་བསྟན་པའི་ཚིག་གི་དོན་དེ་དག་གི་དངོས་པོ་ཚིགས་སུ་བཅད་པས་མདོར་བསྡུ་བའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་གང་ཡིན་པའོ། །

[Block 767]
དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། དེ་ནས་བྱང་ཆུབ་སེམས་དཔའ་དོན་ཟབ་དགོངས་པ་ངེས་པར་འགྲེལ་གྱིས་དེའི་ཚེ་ཚིགས་སུ་བཅད་པ་འདི་དག་སྨྲས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^592]ཚིགས་སུ་བཅད་པ༌[^593]གཉིས་གསུངས་ཏེ། ཚིགས་སུ་བཅད་པ་གཉིས་ལས་ཚིགས་སུ་བཅད་པ་དང་པོའི་རྩ་བ་གོང་མ་གཉིས་ཀྱིས་ནི་རྣམ་པར་བྱང་བའི་ཕྱོགས་བསྟན་ཏོ། །

[Block 768]
རྩ་བ་འོག་མ་གཉིས་ཀྱིས་ནི་ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས་བསྟན་ཏོ། །

[Block 769]
ཚིགས་སུ་བཅད་པ༌[^594]གཉིས་པས་ནི་ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས་ལ་གནས་པ་རྣམས་ཀྱི༌[^595]ཉེས་དམིགས་བསྟན་ཏོ། །

[Block 770 [HEADING]]
###### རྣམ་པར་བྱང་བའི་ཕྱོགས། ^4-1-1-4-1-0

[Block 771]
དེ་ལ་ཚིགས་སུ་བཅད་པ་དང་པོའི་རྩ་བ་གོང་མ་གཉིས་ནི།

[Block 772 [VERSE]]
ཟབ་མོའི་བྱིས་པའི་སྤྱོད་ཡུལ་མ་ཡིན་པ། །
བརྗོད་མེད་གཉིས་མེད་རྒྱལ་བས་བསྟན་མཛད་ཀྱང་། །

[Block 773]
ཞེས་གསུངས་པ་ཡིན་ཏེ། དེ་ནི་དོན་དམ་པའི་ཟབ་མོའི་སྤྱོད་ཡུལ་མ་ཡིན་པ༌[^596]བརྗོད་དུ་མེད་པའི་མཚན་ཉིད་དང་། གཉིས་སུ་མེད་པའི་མཚན་ཉིད་དང་ལྡན་པ། རྒྱལ་བ་སྟོབས་བཅུ་དང་ལྡན་པ། ཐུགས་རྗེ་དམ་པ་མངའ་བས་བསྟན་པའི་སྒོ་ནས་མཚན་ཉིད་གཉིས་ཀྱི་དངོས་པོ་བསྡུ་བ་བསྟན་ཏེ། དེ་གཉིས་ཀྱི༌[^597]རྣམ་པར་བྱང་བའི་ཕྱོགས་ཀྱང་བསྟན་པ་ཡིན་ནོ། །

[Block 774 [HEADING]]
###### ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས། ^4-1-1-4-2-0

[Block 775]
རྩ་བ་གོང་མ་གཉིས་ནི།
--- END BLOCKS ---
