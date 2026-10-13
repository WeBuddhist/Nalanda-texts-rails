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
[Block 36]
ཞེས་པས་བླ་མ་དམ་པ་ལ་བརྟེན་པར་བྱའོ། །

[Block 37]
སྤུན་ལ་ཉེས་པ་བརྗོད་པ་དང་བྱམས་པ་སྤོང་བ་གཉིས་ལྟུང་བའི་ངོ་བོ་གཅིག་ལ་དེ་འབྱུང་བའི་རྒྱུ་ཡང་གཅིག་སྟེ། དེའི་རྒྱུ་ནི་སྔོན་དུ་ཐུན་མོང་གི་ལམ་བྱམས༌[^20]སྙིང་རྗེ་མ་སྦྱངས་པས་སེམས་ཅན་ལ་ཕན་འདོད་པ༌[^21]དང་། གཅེས་པར་འཛིན་པའི་བློ༌[^22]མེད་ལ་དེའི་དབང་གིས་གནོད་ཅིང་སྨོད་པ་ལ་སོགས་པའི་རྐྱེན་ཕྲ་མོ་མི་བཟོད་དེ། དེའི་ཕྱིར་སྤུན་ལ་ཉེས་པ་བརྗོད་ཅིང་སེམས་ཅན་ལ་བྱམས་པ་སྤོང་བ་དེས་དེ་གཉིས་ངོ་བོ་གཅིག་སྟེ་གཞན་ལ་གནོད་པར་འདྲ་བས་སོ། །

[Block 38]
བྱང་ཆུབ་སེམས་སྤོང་དང་གྲུབ་པའི་མཐའ་སྨོད་པ་གཉིས་རྒྱུ་དང་ངོ་བོ་གཅིག་སྟེ། རྒྱུ་ནི་བྱམས་པ་དང་སྙིང་རྗེའི་སྟོབས་ཀྱིས༌[^23]བྱང་ཆུབ་ཀྱི་སེམས་བརྟན་པར་མ་བྱས་པར་བླངས་སུ་ཟིན་ཡང་མི་བརྟན་ཏེ། དེ་ཡང་།

[Block 39 [VERSE]]
ཐམས་ཅད་ལ་ནི་ལྷག་པའི་གནས། །
གང་དུ་ཐམས་ཅད་འཇིག་པ་སྟེ། །
བསྐལ་པ་བྱེ་བ་སྟོང་དུ་ཡང་། །
ཡང་དག་བསྐྱེད་པའི༌[^24]དགེ་བ་ཆེ། །

[Block 40 [VERSE]]
བྱང་ཆུབ་སེམས་ནི་བསྐྱེད་པ་ཡི། །
བསོད་ནམས་ཚོགས་ནི་བསགས༌[^25]པས་སོ། །
བསྐལ་པ་བྱེ་བས་འབྱུང་བ་ནི། །
སྐད་ཅིག་ཉིད་ལ་རྣམ་པར་འཇིག །

[Block 41 [VERSE]]
དེ་བས་དོན་དེ་བསྲུངས་པས༌[^26]ནི། །
དེ་བཞིན་གཤེགས་པས་རབ་ཏུ་གསུངས། །

[Block 42]
ཞེས་འབྱུང་བས་བྱང་ཆུབ་སེམས་དེ་སྤངས་པ་དང་། སྤངས་པའི་ཚད་དང་། དེའི་ཉེས་པའོ། །

[Block 43]
སྤངས་པ་ནི་གསུམ་སྟེ། བླ་མ་ལ་བརྟེན་ནས་དང་། སྤུན་ལ་བརྟེན་ནས་དང་། །སེམས་ཅན་ལ་བརྟེན་ནས་སྤོང་བའོ། །

[Block 44]
ཚད་ནི་རྟེན་གསུམ་པོ་དེ་ལ་བརྟེན་ནས་ཉོན་མོངས་པའི་བསམ་པས་གཡོ་སྒྱུ་ལ་སོགས་པས་ཉིན་མཚན༌[^27]ཆ་ཅི་རིགས་པར་འདས་པའོ། །

[Block 45]
དགེ་བའི་རྩ་བ་རྩད་ནས་འབྱིན་པ་ནི་ཉེས་པའོ། །

[Block 46]
གཞན་གྱི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་བར་ཆད་བྱས་ན་ཡང་ཉེས་པ་ཆེ་བར་ཤེས་པར་བྱའོ། །

[Block 47]
དེ་ལ་རང་གི་ཐེག་པ་ནི་ཐེག་པ་ཆེན་པོ་གཉིས་སོ། །

[Block 48]
གཞན་ནི་ཉན་ཐོས་ཀྱིའོ། །

[Block 49]
སྨོད་པ་ནི་གོང་མ་ལྟར་མི་སྦྱོང་ཞིང་སྨོད་པ་སྟེ། རང་མི་གནས་ཤིང་གཞན་མི་འཛུད་པའོ། །

[Block 50]
གསང་བ་སྒྲོགས་པ་དང་། ཕུང་པོ་སྨོད་པ་གཉིས་རྒྱུ་དང་ངོ་བོ་གཅིག་སྟེ། རིམ་གྱིས་མ་སྦྱངས་པའི་ཕྱིར་སྣོད་དུ་མ་གྱུར་པ་ལ་གསང་བའི་དོན་གྲུབ་པར་གནས་པའི་དོན་ལྟ་བ་རྣམ་པ་གཉིས་ལ་སོགས་པ་བསྟན་པས་ཕུང་པོ་ལྷའི་བདག་ཉིད་ལ་སོགས་པ་བསྐྱེད་པའི༌[^28]གོ་རིམས༌[^29]སྤོང་བས་རྒྱུ་དང་ངོ་བོ་གཅིག་གོ། །

[Block 51]
དེ་ཡང་།

[Block 52 [VERSE]]
ལྷ་ཡི་གཟུགས་ནི་བསྒོམས་པ་ལ། །
སེམས་ཀྱི་བརྩོན་པ་དག་ལ་ནི། །
གླེགས་བམ་ཙམ་ཡང་བསྟན་པ་ནི། །
སྦྱིན་པར་མི་བྱ་ཤེས་བྱ་སྟེ། །

[Block 53 [VERSE]]
རྡོ་རྗེ་ཡེ་ཤེས་རབ་སྤོང་བས། །
རྨོངས་པ་དམྱལ་བར་འགྲོ་བར་འགྱུར། །
དེ་ཡི་དམྱལ་བའི་རྒྱུར་གྱུར་པས། །
མི་དེའང་དམྱལ་བར་འགྲོ་བར་འགྱུར། །

[Block 54 [VERSE]]
དེ་དང་བདག་གཞན་ཕུང་བ༌[^30]ནི། །
འབྱུང་བས༌[^31]ངེས་པར་བསྲུང་བར༌[^32]བྱ། །

[Block 55]
ཞེས་སོ། །

[Block 56]
ཆོས་ལ་ཡིད་གཉིས་ཟ་བ་དང་། །སྡུག་ལ་བྱམས་སེམས་གཉིས་རྒྱུ་དང་ངོ་བོ་གཅིག་སྟེ། དེ་ཡང་སེམས་ཅན་ཐམས་ཅད་རང་བཞིན་དག་པ་འོད་གསལ་དང་ཟུང་འཇུག་གི་རང་བཞིན་དུ་གཅིག་པ་ལ་དེ་གཉིས་ལ་ཐེ་ཚོམ་ཟ་སྟེ། འཁོར་བ་དང་ཞི་བའི་ཕྱག་རྒྱ་ཆེན་པོ་ཟུང་དུ་མ་རྟོགས་པའི་དབང་གིས་གདུག་པ༌[^33]ཅན་དེ་གནོད་ཅིང་དམོད་པ་ལ་སོགས་པ་བྱང་ཆུབ་ཀྱི་རྐྱེན་དུ་བྱུང་བ་ལ་རྡེག་པ་ལ་སོགས་པ་དྲག་ཤུལ་གྱི་སྦྱོར༌[^34]བས་ཕན་པ་མ་ཡིན་པར་བསྒྲུབས་པས་རྒྱུ་དང་ངོ་བོ་གཅིག་གོ། །

[Block 57]
མིང་སོགས་བྲལ་བའི་ཆོས་ལ་དེར་རྟོག་པ་དང་། དད་ལྡན་སེམས་སུན་འབྱིན་པ་རྒྱུ་དང་ངོ་བོ་གཅིག་སྟེ། མིང་ལ་སོགས་པ་བྲལ་བ་ནི་གྲུབ་པའི་གནས་པའི་དོན་ནམ་མཁའ་ལྟ་བུའི་རང་བཞིན་འོད་གསལ་བ་ལ་དངོས་པོ་དང་མཚན་མར་བརྟགས་པའི་རྒྱུས་དེ་ལ་དད་པའི་སེམས་ཅན་དབང་པོ་རབ་དང་ལྡན་པ་རྣམས་སུན་འབྱིན་ཏེ། མ་ཞུགས་པ་ལ་མི་འཇུག་ལ། ཞུགས་པ་བཟློག་ཅིང་བརྟན་པར་མི་བྱེད་པས་སོ། །

[Block 58]
དམ་ཚིག་མི་བསྟེན་པ་དང་ཤེས་རབ་སྨོད་པ་གཉིས་ཀྱང་། བདུད་རྩི་ལྔ་ལ་སོགས་པའི་དམ་ཚིག་མི་བསྟེན་པ༌[^35]ནི་ཤེས་རབ་སྨོད་པའི་རྒྱུ་ཡིན་ཏེ། དེ་ལ་སྨོད་པ་ཉིད་དེ་སྤོང་བའི་རྒྱུའོ། །

[Block 59]
དེས་ན་དང་པོར་བླ་མ་གྲུབ་པ་ཐོབ་པའི་ཚིག་གི་ཉམས་དང་ལྡན་པ་བརྟགས་ལ་ལེགས་པར་བླང་གི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 60]
དེས་ན།

[Block 61 [VERSE]]
བླ་མ་དང་ནི་སློབ་མ་དག །
མཚུངས་པར་དམ་ཚིག་ཉམས་གྱུར་པས། །
དཔའ་བོས་དང་པོར་སློབ་དཔོན་དང་། །
སློབ་མའི་འབྲེལ་པ་བརྟག་པར༌[^36]བྱ། །

[Block 62]
ཞེས་པས་སོ། །

[Block 63]
དེ་ལྟར་ལྟུང་བ་དེ་རྣམས་ལས་འདས་པ་ན་ཉེས་པ་བསྟན་པ་ནི་སློབ་དཔོན་ལ་སྨོད་པ་དེ་ཞེས་པ་ནི་མཚོན་པའི་དོན་ཏེ། ལྟུང་བ་གཞན་ལ་ཉེས་པ་འདྲ་བར་ཤེས་པར་བྱ་བའི་ལྕི་ཡང་ནི་ཡོད་དེ། དེའི་ཉེས་པ་ནི་ཡམས་དང་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་གཅིག་གོ། །

[Block 64]
རྒྱལ་པོ་མེ་དང་ཞེས་པའི་ཚིགས་སུ་བཅད་པ་གཅིག་གོ། །

[Block 65]
དེ༌[^37]ཕྱིར་ནམ་ཡང་ཚིགས་སུ་བཅད་པ་གསུམ་མོ། །

[Block 66]
གལ་ཏེ་བསམ་པའི་སྒོ་ནས་ཉམས་ན་བླ་མའི་སྤྱན་སྔར་མཎྜལ་ལ་སོགས་པས་མཆོད་ལ་ཉེས་པ་མིང་གིས་བཤགས་ཏེ་ཕྱིས་བསྡམ་ཞིང་བླ་མ་ལ་སངས་རྒྱས་ཀྱི་བློ་ཉིས་འགྱུར་དུ་བསླབ་སྟེ། དེའི་ཕན་ཡོན་བསྟན་པའི་ཕྱིར་བླ་མ་ལ་ནི་ཞེས་པའི་ཚིགས་སུ་བཅད་པ་གཅིག་གོ། །

[Block 67]
དེ་བཞིན་དུ་ལྟུང་བ་ལྷག་མ་རྣམས་ཀྱང་བསམ་པའི་བྱེ་བྲག་གིས་བསྐང་བར་བྱའོ། །

[Block 68]
དེས་ན་དང་པོར་བླ་མ་ལེགས་པར་བརྟག་ཅིང་ལེགས་པར་བསྟེན་ལ། དེ་ནས་སྣོད་དུ་བསྒྲུབ་པར༌[^38]གསོལ་བ་གདབ། དེས་ཀྱང་རྗེས་སུ་བརྩེ་བའི་སྒོ་ནས་སྣོད་དུ་བསྒྲུབས་ཏེ།

[Block 69]
དང་པོ་འཁོར་བའི་ཉེས་དམིགས་དང་།

[Block 70 [VERSE]]
ལྷ་དང་བླ་མ་ལ་བརྟེན་དུ་གཞུག་གོ།[^39] །
དེ་ནས་ཐུན་མོང་པའི་སྐྱབས་འགྲོ་ལ་བརྟེན་ལ།
སོ་སོར་ཐར་པའི་སྡོམ་པ་བརྟེན༌[^40]དུ་གཞུག །

[Block 71]
དེ་ནས་ཁྱད་པར་གྱི་སྐྱབས་འགྲོ་ལ་བརྟེན་ནས་བྱང་ཆུབ་ཀྱི་སེམས་བརྟན་དུ་གཞུག །དེ་ནས་འཇུག་པའི་སྡོམ་པ་ལེགས་པར་བྱིན་ལ་དབང་བཞིའི་སྒོ་ནས་ལྟ་སྤྱོད་སྒོམ་གསུམ་གྱི་རྟོགས་པ་བསྒྲུབ༌[^41]པོ། །དེ་ནས་རྟོག་པ༌[^42]དང་མཐུན་པའི་ལམ་ལ་སྦྱར་ཏེ། དེ་ཡང༌[^43]བསྐྱེད་པའི་རིམ་པའི་དུས་སུ་བླ་མ་དང་ལྷ་ཐ་མི་དད་པ་ལ་ཚོགས་བསགས།[^44] ལྟུང་བ་དང་པོའི་རྒྱུ་སྤངས། གོ་རིམས༌[^45]དེ་རྣམས་དབང་པོ་རབ་ཀྱིས༌[^46]ཆོས་ཐམས་ཅད་ཟུང་འཇུག་ཏུ་རྟོགས་པ་སྒྲུབ་པའི་ཐབས་སུ་ཤེས་པར་བྱའོ། །

[Block 72]
འབྲིང་དང་ཐ་མས་ཐ་མལ་པའི་རྟོག་པ་ཟློག༌[^47]པའི་ཐབས་སུ་ཤེས་པར་བྱ་བའི་ཕྱིར་ཕྱིན་ཅི་མ་ལོག་པས་ལྟུང་བ་གཉིས་པ་དང་བདུན་པ་དང་བརྒྱད་པ་དང་དྲུག་པ་དང་བཅུ་གཉིས་པའི་རྒྱུ་སྤངས། ཐུན་མོང་གི་ལམ་བྱམས་པ་དང་སྙིང་རྗེ་བྱང་ཆུབ་ཀྱི་སེམས་དང་ལྡན་པ་དང་། ཐུན་མོང་མ་ཡིན་པའི་ལམ་རྣལ་འབྱོར་དང་བདག་དང་གནས་བསྲུང་བས་ལྟུང་བ་གསུམ་པ་དང་བཞི་པ་དང་ལྔ་པ་དང་དགུ་པ་དང་བཅུ་པའི་རྒྱུ་སྤངས། དེ་ནས་རྫོགས་པའི་རིམ་པ་ལ་བརྟེན་ནས་ཆོས་ཐམས་ཅད་འོད་གསལ་དུ་རྟོགས་པ་བསྒྲུབས་ནས། བདུད་རྩི་ལྔ་ལ་སོགས་པའི་དམ་ཚིག་བརྟེན་པས་བཅུ་གསུམ་པ་དང་བཅུ་བཞི་པ་དང་བཅུ་གཅིག་པའི་རྒྱུ་སྤངས། ཡང་ན་ལྷ་ལ་གསང་བ་དང་ཤེས་རབ་དང་བཞི་པ་བླངས་པས༌[^48]བཅུ་བཞི་པ་དང་བཅུ་གསུམ་པའི་རྒྱུ་སྤངས། དེ་ལྟར་ན་བཅུ་བཞི་པོ་རྣམས་མཉམ་གཞག་གི༌[^49]ལས་ཀྱི་རིམ་པ་ལས༌[^50]འདུས་པས་རྗེས་ཀྱིས་ཀྱང་དེའི་བདག་ཉིད་དུ་བྱ་དགོས་པའི་ངེས་པ་བསྐྱེད་ཅིང་བརྟན་པར་བྱའོ། །

[Block 73 [HEADING]]
## དངོས་གཞིའི་དབང་དུ་བྱས་ནས་ལྟུང་བ་རེ་རེ། ^2-0

[Block 74]
དངོས་གཞིའི༌[^51]དབང་དུ་བྱས་ནས་ལྟུང་བ་རེ་རེ་ལ་ལྟུང་བའི་ངོས་འཛིན་དང་རྐྱེན་གང་གིས་བྱུང་བ་དང་། ཉེས་པ་དང་། ཚུལ་ཇི་ལྟར་མི་འབྱིན་པའི་ཐབས་སོ། །

[Block 75]
བདེ་གཤེགས་བཀའ་ནི་འཁོར་བའི་ཉེས་པ་ནས་བྱས་ཞེས་དང་། བྱས་གཟོ་དང་། བྱམས༌[^52]སྙིང་རྗེ་དང་འཇུག་པའི་སྡོམ་པའི་བར་དུ༌[^53]བརྟན་པར་བྱ་བ་དང་། ཁྱད་པར་ཅན་དབང་རྣམ་པ༌[^54]བཞིས་སྣོད་དུ་བསྒྲུབས་ནས་ལྟ་བ་ལ་སོགས་པའི་མན་ངག་ནི་བདེ་གཤེགས་ཀྱི་བཀའོ། །
--- END BLOCKS ---
