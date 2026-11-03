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
[Block 5566]
གྲགས་པ་ནི་སྙན་པའི་ཕན་པ་དང་ལྡན་པའི་འགྲོ་བའི་སྡུག་བསྔལ་བསལ༌[^3547]བའོ། །

[Block 5567]
དེ་ཡང་ཤིང་རྟ་ཡོད་པ་དེ་ནི་ཤིང་རྟ་དག་གོ། །

[Block 5568]
བཀུར་སྟི་ཉིད་སྦྱིན་པའི་ཤིང་རྟ་གང་ཡིན་པ་དེ་ནི་བཀུར་སྟི་སྦྱིན་པའི་ཤིང་རྟ་སྟེ། ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པའི་ཤིང་རྟ་དག་གོ། །

[Block 5569]
ཡོན་ཏན་འབྱུང་བ་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་སྐྱེ་བ་ཡིན་པས་ཡོན་ཏན་འབྱུང་བ་སྟེ། དེ་ནི་ཤིང་རྟ་ཉིད་དེ་རང་གི་ལུས་སོ། །

[Block 5570]
མི་རྩུབ་པའི་མིག་དང་ལྡན་པ་གང༌[^3548]ཡིན་པ་དེ་ནི་མི་རྩུབ་མིག་ལྡན་ཏེ། མི་རྩུབ་པའི་བྱམས་པའོ། །

[Block 5571]
སྦྱིན་པ་དང་དུལ་བ་ནི་སྦྱིན་དུལ་ལོ། །

[Block 5572]
དེ་གཉིས་ཀྱི་འཁོར་ལོ་གང་ལ་ཡོད་པ་དེ་ནི་སྦྱིན་དུལ་འཁོར་ལོ༌[^3549]ཅན་ནོ། །

[Block 5573]
སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང༌[^3550]བསོད་ནམས་ཉིད་འདོད་པའི་བསོད་ནམས༌[^3551]པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5574]
དབང་པོ་དུལ་བ་ནི་དབང་པོ་བསྡམས་པའོ། །

[Block 5575]
དྲན་པ་ཉིད་སྲབ་སྐྱོགས་ཡིན་པས་དྲན་པའི་སྲབ་སྐྱོགས་ཅན་ནོ། །

[Block 5576]
བློ་གྲོས་དང་ལྡན་པ་ཉིད་ལྕག་ཡིན་པས་ཤེས་རབ་ཀྱི་སྐུལ་མའོ། །

[Block 5577]
ཐོས་པ་རྒྱ་ཆེ་བ་ཉིད་ཀྱི་མཚོན་གང་ལ་ཡོད་པ་དེ་ནི། ཐོས་པ་རྒྱ་ཆེན་མཚོན་ནོ། །

[Block 5578]
ངོ་ཚ་ཉིད་ཡོ་བྱད་ཡིན་པས་ངོ་ཚ་ཡོ་བྱད་དོ། །

[Block 5579]
བཅིངས་པ་མཛེས་པའི་གྲོགས་གང་ཡིན་པ་དེ་ནི་གྲོགས་མཛེས་པས་བཅིངས་པའོ། །

[Block 5580]
བཟོད་པ་ཉིད་ཀྱི་གཉའ་ཤིང་གང་ལ་ཡོད་པ་དེ་ནི་བཟོད་པའི༌[^3552]གཉའ་ཤིང་ངོ་། །འགྲོ་བ་བརྟན་པ༌[^3553]གང་ཡིན་པ་དེ་ནི་འགྲོ་བ་བརྟན༌[^3554]པའོ། །

[Block 5581]
ཚིག་ཉིད་ངན་པ་ཡིན་པས་ཚིག་ངན་ནོ། །

[Block 5582]
དེ་བསྡམས་པ་ནི་ཚིག་ངན་བསྡམས་པའོ། །

[Block 5583]
ཚིག་ངན་པ་ནི་བརྫུན་དུ་སྨྲ་བ་ལ་སོགས་པ་ངག༌[^3555]གི༌[^3556]སྐྱོན་རྣམ་པ་བཞིའོ། །

[Block 5584]
ཡིད་འོང་ཚིག་ཙམ་སྨྲ་བས་ཟབ་པའི་སྒྲ། །[^3557]ཞེས་བྱ་བ་ནི་ཚིག་ངན་པའི་མི་མཐུན་པའི་ཕྱོགས་དགེ་བའི་ལས་ཀྱི་ལམ་གཟུང༌[^3558]ངོ་། །བསྡམས་པ་མ༌[^3559]ཞིག་པས་ན་མཚམས་མ་བྱེ་ཞེས་བྱ་བ་འདིས་ནི་ཡང་དག་པའི་འཚོ་བ་བསྟན་ཏོ། །

[Block 5585]
སྤྱོད་པ་ངན་པའི་གྱ་གྱུ་སྤངས་པས་དྲང་། །ཞེས་བྱ་བ་འདིས་ནི་ཡང་དག་པའི་ལས་ཀྱི་མཐའ་བསྟན་ཏོ། །

[Block 5586]
རྒྱལ་མཚན་མཐོ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་ཉེ་བར་ཞི་བ་མཐོ་བའོ། །

[Block 5587]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་ཚངས་པའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 5588 [HEADING]]
## གླང་པོ་ཆེའི་སྐྱེས་པའི་རབས། ^32-0

[Block 5589]
གཞན་དག་ལ་ཕན་པ་ཡིན་པའི་ཕྱིར་གཞན་ལ་ཕན་པའོ། །

[Block 5590]
དེ་ཉིད་ཤས་ཆེ་བའི་སྡུག་བསྔལ་གང་ཡིན་པ་དེ་ནི་གཞན་ལ་ཕན་པར་བྱེད་པའི་སྡུག་བསྔལ་ལོ། །

[Block 5591]
ཡུལ་ལྗོངས་ཐག་རིང་དུ་གྱུར་པ་ཞེས་བྱ་བ་ནི། གྲོང་གི་སྐྱེ་བོ་དང་ཐག་བསྲིངས་པའོ། །

[Block 5592]
ཞི་བ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་ཡིན་ཏེ། ལུས་ཀྱི་ལས་ཀྱི་མཚན་ཉིད་དོ། །

[Block 5593]
སྤྱུགས་པ་ཞེས་བྱ་བ་ནི་ཡུལ་གྱི་སྐྱེ་བོ་དང་བྲལ་བར་བྱས་པའོ། །

[Block 5594]
ཁྲོས་པ་ཞེས་བྱ་བ་ནི་ཉེས་པ་ཡོད་པས་ཞེས་བྱ་བའི༌[^3560]དོན་ཏོ། །

[Block 5595]
དེ་དག་གིས་མི་རིགས་པ་བྱས་པ་ནི་ཉེས་པ་ཡོད་པས་རྒྱལ་པོས་སྤྱུགས་པའོ། །

[Block 5596]
གཅོམ་ཆུང་བ་ནི་གཟི་བརྗིད་ཆུང་བའོ། །

[Block 5597]
ཉམ་ཐག་ཅིང་ཕོངས་པའི་སྒྲ་འབའ་ཞིག་གང་ཡིན་པ་དེ༌[^3561]ནི་ཉམ་ཐག་ཕོངས་པའི༌[^3562]སྒྲ་འབའ་ཞིག་གོ། །

[Block 5598]
ནགས་ཚལ་དེ་ལོགས་སུ་འོང་བ་ནི་ནགས་ཚལ་དེ་ལ༌[^3563]མངོན་དུ་ཕྱོགས་ཏེ་འོང་བའོ། །

[Block 5599]
གངས་རིའི་རྩེ་མོ་འགྲོ་ཤེས་པ་འདྲ་བཞེས་བྱ་བས༌[^3564]ནི་མདོག་དང་མཚན་ཉིད་བསྟན་ཏོ། །

[Block 5600]
སྟོན་ཀའི་སྤྲིན་ནམ། ན་བུན་གྱི་ཚོགས་རླུང་གིས་བསྐྱོད་པ་བཞིན་ཞེས་བྱ་བ་ནི། འགྲོས་དང་། མདོག་དང་། ཚང་མཐུན་པ་བསྟན་ཏོ། །

[Block 5601]
མདོག་ཅུང་ཟད་དམར་ཞིང་སྣུམ་པ་གང་ཡིན་པ་དེ་ནི།

[Block 5602 [VERSE]]
སྣ་མདོག་ཅུང་ཟད་དམར་ཞིང་སྣུམ་པའོ། །
རྡུལ་དང་ཉི་མའི་འོད་ཟེར་ནི། །
རྡུལ་དང་ཉི་མའི་འོད་ཟེར་རོ། །

[Block 5603]
དེས་རེག་པ༌[^3565]ནི་རྡུལ་དང་ཉི་མའི་འོད་ཟེར་གྱིས་རེག་པ་སྟེ་དེ་བས་ནའོ། །

[Block 5604]
ཁ་དོག་མ་རུང་པ་གང་ཡིན་པ་དེ་ནི་ཁ་དོག་ཉམས་པའོ། །

[Block 5605]
རིད་པ་སྟེ། ཅིའི་ཕྱིར་རིད་པ་ཡིན་ཞེ་ན། དེ་ཉིད་སྨྲས་པ། མྱ་ངན་གདུངས་ཕོངས་ཞེས་བྱ་བ་ལ་མྱ་ངན༌[^3566]ནི་སེམས་ཀྱི་སྡུག་བསྔལ་ལོ། །
--- END BLOCKS ---
