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
[Block 526]
གང་གི་ཕྱིར་རླུང་ནི་ལུས་ཐམས་ཅད་ལ་ཁྱབ་པ་དང་། ལས་ཐམས་ཅད་བྱེད་ཅིང་སྲོག་ཆགས་ཐམས་ཅད་ཀྱི་སྲོག་ཏུ་གྱུར་པ་རྣམ་ཤེས་ཀྱི་བཞོན་པ་གཅིག་པུ་ཁོ་ནའོ། །

[Block 527]
དེ་ཡང་ཕུང་པོ་ལྔའི་དབྱེ་བས་ལྔ་རུ་འགྱུར་ཏེ། སྲོག་དང་། ཐུར་དུ་སེལ་བ་དང་། མེ་དང་མཉམ་པ་དང་། གྱེན་དུ་རྒྱུ་བ་དང་། ཁྱབ་པའོ། །

[Block 528]
དེ་ལ་སྲོག་ནི་ལྟེ་བ་ལ་གནས་ཤིང་རྣམ་པར་ཤེས་པའི་ཕུང་པོ་མངོན་པར༌[^367]སྐྱེད་པར་བྱེད་པའི་ལས་ཅན་ནོ། །

[Block 529]
ཐུར་དུ་སེལ་བ་ནི་བཤང་ལམ་ལ་གནས་ཤིང་ཚོར་བའི་ཕུང་པོ་མངོན་པར་སྐྱེད་པའི༌[^368]ལས་ཅན་ནོ། །

[Block 530]
གྱེན་དུ་རྒྱུ་བ༌[^369]ནི་མགྲིན་པ་ལ་གནས་ཤིང་འདུ་ཤེས་ཀྱི་ཕུང་པོ་མངོན་པར་སྐྱེད་པའི༌[^370]ལས་ཅན་ནོ། །

[Block 531]
མེ་དང་མཉམ་པ་ནི་སྙིང་ག་ན་གནས་ཤིང་འདུ་བྱེད༌[^371]ཀྱི་ཕུང་པོ་མངོན་པར་སྐྱེད་པའི༌[^372]ལས་ཅན་ནོ། །

[Block 532]
ཁྱབ་པར་བྱེད་པ་ནི་ལུས་ཀྱི་ཚིགས་ཐམས་ཅད་ལ་གནས་ཤིང་གཟུགས་ཀྱི་ཕུང་པོ་མངོན་པར་སྐྱེད་པའི༌[^373]ལས་ཅན་ནོ། །

[Block 533]
དེ་དག་ས་ལ་སོགས་པ་འབྱུང་བ་ཆེན་པོ་ལྔ་དང་། དེ་བཞིན་གཤེགས་པ་ལྔ་དང་། ཁ་དོག་ལྔ་དང་ལྡན་ཞིང་ཞི་བ་ལ་སོགས་པའི་ལས་བྱེད་པའི་ཡེ་ཤེས་ལྔའི་ངོ་བོ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 534]
ཡན་ལག་གི་རླུང་ནི་རྒྱུ་བ་དང་རྣམ་པར་རྒྱུ་བ་དང་ཀུན་ཏུ་རྒྱུ་བ་དང་། རབ་ཏུ་རྒྱུ་བ་དང་། ངེས་པར་རྒྱུ་བའོ། །

[Block 535]
དེ་དག་གི་མིག་ལ་སོགས་པའི་དབང་པོ་ལྔ་ལ་བརྟེན་ཏེ་གཟུགས་ལ་སོགས་པ་གཟུང་བའི་མཚན་ཉིད་ཅན་གྱི་ལས་བྱེད་དོ། །

[Block 536]
དེ་རྣམས་ཀྱང་དེ་བཞིན་གཤེགས་པ་ལྔའི་ངོ་བོ་ཉིད་དོ། །

[Block 537]
བཅུ་པོ་དེ་རྣམས་ཀྱི་མིང་ནི་སྒྲ་ཇི་བཞིན་མ་ཡིན་པས་དཔལ་སངས་རྒྱས་ཐམས་ཅད་དང་མཉམ་པར་སྦྱོར་བ་ལས་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་ཏེ།

[Block 538 [VERSE]]
ཀུ་ཊ་ཁྱ་དང་ཀུ་ཌ་དང་། །
ཀུ་ཌ་བྷ་དང་ཀུ་ཊི་ར། །
ཀ་ཀུ་ལཱ་ཚ་ཀུ་ལ་ཝ། །
ཀུ་ལཱ་བྷ་ཀོ་ལི༌[^374]ར་བ། །

[Block 539 [VERSE]]
སྲོག་དང་ཐུར་སེལ་མེ་མཉམ་དང་། །
གྱེན་དུ་དེ་བཞིན་ཁྱབ་བྱེད་དང་། །
གླང་པོ་རུས་སྦལ་རྩངས་པ་དང་། །
ལྷ་སྦྱིན༌[^375]དང་ནི་གཞུ་ལས་རྒྱལ། །

[Block 540]
ཞེས་འབྱུང་ངོ་། །རླུང་བཅུ་པོ་དེ་དག་གནས་དང་ཉོན་མོངས་པ་དང་ལས་ཀྱི་བྱེ་བྲག་ལ་བརྟེན་ཏེ་ཉིན་མཚན་དུ་ཟོ་ཆུན་བཞིན་དུ་སེམས་ཅན་གྱི་ཁམས་འཇུག་པར་བྱེད་པ་ན་འཁོར་བར་བྱེད་ཅིང་། ཡང་དང་ཡང་དུ་འཁོར་བའི་སྒོ་ནས་ཉིང་མཚམས་སྦྱོར་བ་ལ་བཅིངས་པས་ཉོན་མོངས་པར་བྱེད་དོ། །

[Block 541]
རླུང་དེ་རྣམས་ཀྱི་དེ་ཁོ་ན་ཉིད་ཡོངས་སུ་ཤེས་པས་གྲོལ་བར་འགྱུར་བས་དེ་བཤད་པར་བྱ་སྟེ། དེའི་དེ་ཁོ་ན་ཉིད་ནི་ཐིག་ལེ་བསྒོམ་པའོ། །

[Block 542]
གང་གི་ཕྱིར་ཐབས་དང་ཤེས་རབ༌[^376]སྙོམས་པར་ཞུགས་པའི་དུས་སུ་རྩ་སྟོང་ཕྲག་བདུན་ཅུ་རྩ་གཉིས་ཀྱི་འཁོར་ལོ་ལས་བྱུང་བའི་བྱང་ཆུབ་ཀྱི་སེམས་རྡོ་རྗེ་ནོར་བུའི་རྩེ་མོར་གོང་བུར༌[^377]གྱུར་པ་ན། རླུང་དང་ཉེ་བའི་རླུང་ཐམས་ཅད་རབ་ཏུ་ཞི་བར་གྱུར་པས་ན། གསལ་བ་དང་དགའ་བའི་རང་བཞིན་ཅན་གྱི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་མངོན་དུ༌[^378]འགྱུར་རོ། །

[Block 543]
དེའི་ཕྱིར་བདེ་བ་ཆེན་པོའི་དབང་གིས་རླུང་གཟུགས་མེད་ཀྱང་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེའི་གཟུགས་སུ༌[^379]འགྱུར་ཏེ། ཤིན་ཏུ་གྲང་བའི་དབང་གིས་ཆུའི་སྲ་བ་ཉིད་བཞིན་ནོ། །

[Block 544]
ཐིག་ལེ་དེ་ཡང་རྣམ་པ་གསུམ་སྟེ། གསང་བའི་སྣའི་རྩེ་མོར་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེ་གསུང་གི་རྡོ་རྗེའི་རྣལ་འབྱོར་པས་བསྒོམ་པར་བྱ་བ་དང་། སྙིང་གའི་པདྨའི་སྣའི་རྩེ་མོར་སྔགས་ཀྱི་ཐིག་ལེ་ཐུགས་ཀྱི་རྡོ་རྗེའི་རྣལ་འབྱོར་པས་བསྒོམ་པར་བྱ་བ་དང་། གདོང་གི་སྣའི་རྩེ་མོར་རླུང་གི་ཐིག་ལེ་འོད་ཟེར་ཅན་སྐུའི་རྡོ་རྗེའི་རྣལ་འབྱོར་པས་བསྒོམ་པར་བྱ་བའོ། །

[Block 545]
དེ་ལ་སྙོམས་པར་ཞུགས་པ་ལས་འབྱུང་བ་ཡན་ལག་དང་ཉིང་ལག་ཐམས་ཅད་ནས་འཕོ་བས་དམ་པ་དགའ་བའི་གནས་སྐབས་སུ། །རྡོ་རྗེ་དང་པདྨའི་སྣ་རུ་འཛིན་པར་གྱུར་པ་ན་ངག་གི་སྤྲོས་པ་ཐམས་ཅད་སྤངས་པ། བརྗོད་དུ་མེད་པའི་ཐིག་ལེ་འདོད་ཆགས་ཅན་གྱི་རྣལ་འབྱོར་པས་བསྒོམ་པར་བྱའོ་ཞེས་གསུང་གི་རྡོ་རྗེའི་རྣལ་འབྱོར་པའི་ཕྲ་མོའི་རྣལ་འབྱོར༌[^380]རོ། །

[Block 546]
སྤྱི་བོ་དང་ལྐོག་མ་དང་། སྙིང་ག་ན་གནས་པའི་ཡི་གེ་གསུམ་པོ་ལ་དམིགས་ཏེ། སྐུའི་རྡོ་རྗེའི་ས་བོན་གྱི་ཆ་རྣམས་སྟེང་ནས་བརྩམས་ཏེ་གཅིག་ནས་གཅིག་ཏུ་ཐིམ་པར་བྱས་ཏེ། འོག་གི་ཆ་གསུང་གི་རྡོ་རྗེའི་ཆ་རྣམས་ལ་འཇུག་པར་བྱ་སྟེ། དེའི་ཆ་རྣམས་ཀྱང་སྔ་མ་བཞིན་དུ་འཇུག་པར་བྱས་ལ་ཡི་གེ་ཧཱུཾ་དུ་ཐིམ་པར་བསམ་མོ། །

[Block 547]
ཡི་གེ་ཧཱུཾ་ཆ་བཞི་པ་ཡང་ཞབས་ཀྱུ་ནི་འ་ལ་ཐིམ་པ་དང་། འ་ཧ་ལ་ཐིམ་པ་དང་། ཧ་མགོ་བོ་ལ་ཐིམ་པ་དང་། མགོ་བོ་ཟླ་ཚེས་ལ་ཐིམ་པ་དང་། ཟླ་ཚེས་ཐིག་ལེ་ལ་ཐིམ་པ་དང་། ཐིག་ལེ་སེམས་རྩེ་གཅིག་པར་བྱས་པས་ནམ་མཁའ་ལྟ་བུའི་ངོ་བོ་ཉིད་དུ་གནས་པ་ནི་ཞེ་སྡང་རྡོ་རྗེའི་རྣལ་འབྱོར་པའི་ཕྲ་མོའི་རྣལ་འབྱོར་རོ། །

[Block 548]
དེ་བཞིན་དུ་ལུས་འདི་ལ་ཁམས་བཞིའི་རང་བཞིན་དཀྱིལ་འཁོར་བཞི་ཡོད་དེ། དེ་ཡང་མགྲིན་པ་དང་། སྙིང་ག་དང་། ལྟེ་བ་དང་། གསང་བར་གནས་པ་སྟེ། གྲུ་གསུམ་དང་། ཟླུམ་པོ་དང་། གཞུའི་དབྱིབས་ཅན་དང་། གྲུ་བཞིའོ། །

[Block 549]
དམར་པོ་དང་། དཀར་པོ་དང་། དུད་ཁ༌[^381]དང་། སེར་པོའི་མདོག་ཅན། མེ་དང་། ཆུ་དང་། རླུང་དང་། སའི་ངོ་བོ་ཉིད་དོ། །

[Block 550]
ཡཾ་རཾ་བཾ་ཁཾ་ཞེས་བྱ་བའི་ས་བོན་ལས་བྱུང་བ་དང་། སྣང་བ་མཐའ་ཡས་དང་། མི་བསྐྱོད་པ་དང་། དོན་ཡོད་གྲུབ་པ་དང་། རིན་ཆེན་འབྱུང་ལྡན་གྱིས༌[^382]བྱིན་གྱིས་བརླབས་པ་སྟེ་ཐབས་བསྟན་ནོ། །

[Block 551]
དེ་ནས་གོས་དཀར་མོ་དང་། མཱ་མ་ཀཱི་དང་། སྒྲོལ་མ་དང་། སངས་རྒྱས་སྤྱན་གྱིས༌[^383]བྱིན་གྱིས་རློབ་པ་ནི་ཤེས་རབ་ཀྱི་ངོ་བོ་ཉིད་དོ། །

[Block 552]
གཡས་པ་དང་། གཡོན་པ་དང་། གཉིས་ཀ་དང་། དམན་པར་རྒྱུ་བ་རྣམས་ཀྱི་སྣའི་སྒོར་བསྟན་ཏོ། །

[Block 553]
སྔ་དྲོ་དང་། ཉི་མ་ཕྱེད་དང་། ཕྱི་དྲོ་དང་། མཚམས་དག་གི་དུས་བསྟན་པ་དེ་བཞིན་དུ་ཡང་མཚན་མོར་རོ། །

[Block 554]
དབང་དང་ཞི་བ་དང་། དགུག་པ་དང་། རྒྱས་པ་ནི་ཕྲིན་ལས་སོ། །

[Block 555]
དཀྱིལ་འཁོར་དེ་རྣམས་ལས་ཐོ་རངས་ནས་བརྩམས་ཏེ། ཁ་དོག་དམར་པོའི་འོད་ཟེར་སྣའི་བུག་པ་གཡས་པ་ནས་འབྱུང་བར་འགྱུར་ཞིང་སྣའི་རྩེ་མོར་ཐུན་གྱི་ཕྱེད་ཀྱི་ཕྱེད་ཀྱི་བར་དུ་གནས་པར་འགྱུར་རོ། །

[Block 556]
དེ་བཞིན་དུ་ཐུན་གཉིས་པ་ལ་ཁ་དོག་ལྗང་སེར་ཅན། འོད་ཟེར་སྣའི་བུག་པ་གཡོན་ནས་འབྱུང་ཞིང་དེ་ཉིད་དུ་ཐུན་གྱི་ཕྱེད་ཀྱི་ཕྱེད་ཀྱི་བར་དུ་གནས་པའོ། །

[Block 557]
ཐུན་གསུམ་པ་ལ་ཡང་ཁ་དོག་སེར་པོ་འོད་ཟེར་གཉིས་ཀ་ལས་འབྱུང་ཞིང་སྣའི་བུག་པ་དེ་ཉིད་དུ་ཐུན་གྱི་ཕྱེད་ཀྱི་ཕྱེད་ཀྱི་བར་དུ་གནས་སོ། །

[Block 558]
ཐུན་བཞི་པ་ལ་ཡང་གཉིས་ཀ་ཁ་ནས་འབྱུང་ཞིང་འོན་ཀྱང་དལ་ཞིང་དམན་པར་རྒྱུ་བ་ཁ་དོག་དཀར་པོའི་འོད་ཟེར་འབྱུང་ཞིང་། དེ་ཡང་ཐུན་གྱི་ཕྱེད་ཀྱི་ཕྱེད་ཀྱི་བར་དུ་གནས་པ་སྟེ། མཚན་མོ་ཡང་དེ་བཞིན་ནོ། །

[Block 559]
དེ་ལྟར་ཉིན་མོ་དང་མཚན་མོ་ཐུན་བརྒྱད་ལ་ཆུ་ཚོད་དྲུག་ཅུའི་བར་དུ་སྟོང་ཕྲག་ཉི་ཤུ་རྩ་གཅིག་དང་དྲུག་བརྒྱ་དཀྱིལ་འཁོར་སོ་སོ༌[^384]དག་ཏུ་འཇུག་པ་དང་གནས་པ་དང་ལྡང་བའི་རིམ་གྱིས་རྒྱུ་བའོ། །

[Block 560]
དཀྱིལ་འཁོར་རེ་རེ་དག་ལ་བཞི་བཞིའི་བདག་ཉིད་ཡོད་དེ། ཆ་དེ་རྣམས་སུ་འཇུག་པ་ལ་སོགས་པའི༌[^385]ས་ཡ་བདུན༌[^386]ཅུ་རྩ་གཉིས་གསུངས་སོ། །

[Block 561 [HEADING]]
##### སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད། ^1-2-1-2-0

[Block 562]
དེ་དག་ཐམས་ཅད་ཀྱི་རྩ་བ་ནི་བཅོམ་ལྡན་འདས་མ་ཕྱི་མོའི་ཡི་གེ་བཞི་བཅུ་རྩ་དགུ་པའོ། །

[Block 563]
དེ་ཡི་ཡང་རྩ་བ་ནི་ལྟེ་བའི་འོག་འོད་གསལ་བའི་གནས་ལས་བྱུང་བ་སྲོག་ཅེས་བྱ་བའི་རླུང་ངོ་། །ཇི་སྐད་དུ།

[Block 564 [VERSE]]
ནམ་མཁའི་རླུང་ནི་ལུས་ལ་འབྱུང་བ་སྟེ། །
ཡང་དག་བརྗོད་པས་དབྱངས་ནི་ཁར་ཕྱིན་པ། །
གནས་གཞན་དག་ཏུ་རབ་ཏུ་ཕྱེ་བས་ན། །

[Block 565]
ཡི་གེ་ཉིད་དུ་གྱུར་པ་གང་ཡིན་དེ་སྒྲ་ཡིན། །
--- END BLOCKS ---
