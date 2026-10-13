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
[Block 491 [VERSE]]
མྱ་ངན་འདས་པ་བདེན་གཅིག་པུ། །
རྒྱལ་བ་རྣམས་ཀྱིས་རྣམས༌[^308]གསུངས་པ། །
དེའི་ཚེ་ལྷག་མ་ལོག་པ་ཞེས། །
མཁས་པ་སུ་ཞིག་རྟོགས་མི་བྱེད། །

[Block 492]
ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 493]
བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་དག་འདི་ལྟ་སྟེ། མི་སླུ་བའི༌[^309]ཆོས་ཅན་མྱ་ངན་ལས་འདས་པ་འདི་ནི་བདེན་པའི་མཆོག་གཅིག་ཏུའོ༌[^310]ཞེས་གསུངས་ཏེ་ལུང་འདིས༌[^311]དོན་གྱིས་ན་ཤེས་རབ་ཅན་སུ་ཞིག་ཕུང་པོ་ལ་སོགས་པ་བརྫུན་པའི་དོན་ཁོང་དུ་ཆུད་པར་མི་འགྱུར། གང་གི་ཕྱིར་ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་དེ་དག་རྣམ་པ་དེ་ལྟར་རིགས་པ༌[^312]དང་། ལུང་གིས་རྣམ་པར་དཔྱད་ན་ངོ་བོ་ཉིད་ཀྱིས༌[^313]གྲུབ་པ་མེད་པ་དེའི་ཕྱིར་ངེས་པར།

[Block 494 [HEADING]]
### ཚིགས་བཅད་སོ་དྲུག་པ། ^1-37-0

[Block 495 [VERSE]]
ཇི་སྲིད་ཡིད་ཀྱིས༌[^314]རྣམ་གཡོ་བ། །
དེ་སྲིད་བདུད་ཀྱི་སྤྱོད་ཡུལ་ཏེ། །

[Block 496]
འཕགས་པའི་ཤེས་རབ་ཀྱི་དབང་པོའི་སྲོག་གི་བར་ཆད་བྱེད་པས་བདུད་དེ་དེ་ཡང་ཁམས་གསུམ་གྱིས་ཆེན་པོ་པ་ཕྱིན་ཅི་ལོག་བཞིའི་བློན་པོ་ཆེན་པོ་དང་ལྡན་པ་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པའི་འཁོར་གྱིས་རྟག་ཏུ་འཁོར་བ། འཕགས་པ་མ་ཡིན་པ་སྐྱེ་བོ་མཐའ་དག་གིས་སྨ་མ་ཕབ་པ། སྤྱོད་པ་བཟང་པོ་མ་ཡིན་པ༌[^315]ཞུགས་པའི་རྗེས་སུ་སོང་བ། འཁོར་བ་པའི་སེམས་ཅན་མ་ལུས་པ༌[^316]འཕེལ་བར་བྱེད་པ་མ་རིག་པ་ཞེས་བྱ་བ་ཡིན་ཏེ་ཚུལ་བཞིན་མ་ཡིན་པས་དངོས་པོ་ལ་རྣམ་པར་རྟོག་ན་མ་རིག་པའི་ཡུལ་ལས་མི་འདའ་བ་ཉིད་དུ་མངོན་ནོ། །

[Block 497]
གང་གི་ཚེ་དེ་བདུད་ཀྱི་སྤྱོད་ཡུལ་ཡིན་པ་དེའི་ཚེ་དེ་སྐྱེ་བ་མེད་ན་ཡིད་འཇུག་པ་མི་འབྱུང་བའི་ཕྱིར་བདུད་ཀྱི་ཡུལ་ཉིད་མེད་པར་འགྱུར་བས།

[Block 498 [VERSE]]
དེ་ལྟ་ཡིན་ན་འདི་ལ་ཡང་། །
ཉེས་པ་མེད་པར་ཅིས༌[^317]མི་འཐད། །

[Block 499]
འདི་ཞེས་བྱ་བ་ནི་དེའི་ངོ་བོ་ཉིད་སྐྱེ་བ་མེད་པ་ཡོངས་སུ་ཤེས་པ་ཡིན་པར་སྟོན་ཏེ། དེའི་དབང་དུ་བྱས་པའི་ཕྱིར་ཉེ་བར་གྱུར་པས་ཉེ་བ་མངོན་སུམ་གྱི་ཚིག་འདིས་འདི་ལ་ཞེས་བྱ་བ་བསྟན་ཏོ། །

[Block 500]
འདིའི་ཕྱིར་ཡང་ངོ་བོ་ཉིད་སྐྱེ་བ་མེད་པ་ཡོངས་སུ་ཤེས་པ་ན༌[^318]ངོ་བོ་ཉིད་ཡོངས་སུ་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 501]
དེའི་ཕྱིན་ཅི་ལོག་ཡོད་ན་ནི་ཡོད་ལ་མེད་ན་ནི་མེད་པའི་ཕྱིར་རོ། །

[Block 502]
དེ་ལྟར་བསྟན་པའི་ཕྱིར།

[Block 503 [HEADING]]
### ཚིགས་བཅད་སོ་བདུན་པ། ^1-38-0

[Block 504 [VERSE]]
མ་རིག་རྐྱེན་གྱིས་འཇིག་རྟེན་ཞེས། །
འདི་ལྟར་རྫོགས་པའི་སངས་རྒྱས་གསུང་། །
དེའི༌[^319]ཕྱིར་འཇིག་རྟེན་འདི་དག་ཀྱང་། །
རྣམ་པར་རྟོག་པ་ཅིས་མི་འཐད། །

[Block 505]
ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 506]
གང་གི་རྐྱེན་མ་རིག་པ་ཡིན་པ་དེ་མ་རིག་པའི་རྐྱེན་ལས་བྱུང་བ་སྟེ་འཇིག་རྟེན་ནོ། །

[Block 507]
འཇིག་རྟེན་ནི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་རྣམས་སོ། །

[Block 508]
དེ་ལ་མ་རིག་པའི་རྐྱེན་གྱིས་འདུ་བྱེད་རྣམས། འདུ་བྱེད་ཀྱི་རྐྱེན་གྱིས་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིས་འདི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་འཇིག་རྟེན་འདིའི་རྐྱེན་ནི་མ་རིག་པའོ་ཞེས་བསྟན་པ་དེའི་ཕྱིར། རང་གི་ངོ་བོ་གྲུབ་པ་མེད། །རང་གི་ངོ་བོ་གྲུབ་པ་རྫས་ལ་སོགས་པའི་རྐྱེན་ནི་མུན་པ་མ་ཡིན་ནོ། །

[Block 509]
དེ་བས་ན་མ་རིག་པ་རྐྱེན་དུ་གྱུར་པའི་ཕྱིར། འཇིག་རྟེན་རྣམ་པར་རྟོག་པ་ཅིའི་ཕྱིར་འཐད་དེ། འཇིག་རྟེན་རྣམ་པར་རྟོག་པ་ཙམ་དུ་འཐད་པ་ཉིད་དོ་ཞེས་བྱ་བར་དགོངས་སོ། །

[Block 510]
རྣམ་པར་རྟོག་པ་ནི་རྣམ་པར་རྟོག་པའོ། །

[Block 511]
རྣམ་པར་རྟོག་པ་ཙམ་དུ་ཟད་པས་ན་རྣམ་པར་རྟོག་པ་སྟེ། རྣམ་པར་རྟོག་པ་ཙམ་དུ་ཟད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 512]
རང་གི་ངོ་བོ་གྲུབ་པ་མེད་པས་མུན་ཁུང་ན་མིའི་ཚུལ་དུ་ཡོངས་སུ་རྟོག་པ་འབྱུང་བ་ལྟར་འཇིག་རྟེན་ཡང་རྣམ་པར་རྟོག་པ་ཙམ་དུ་རྣམ་པར་གཞག་གོ། །

[Block 513]
དེ་ལྟར་ཕྱིན་ཅི་ལོག་ཡོད་ན་འཇིག་རྟེན་ཡོད་པར་ཅི་བསྟན་ནས། ད་ནི་ཕྱིན་ཅི་ལོག་མེད་ན་མེད་པར་བསྟན་པའི་ཕྱིར།

[Block 514 [HEADING]]
### ཚིགས་བཅད་སོ་བརྒྱད་པ། ^1-39-0

[Block 515 [VERSE]]
མ་རིག་འགགས་པར་གྱུར་ན་ནི། །
གང་རྣམས་འགག་པར་འགྱུར་བ་རྣམས། །
དེ་དག་མི་ཤེས་ཀུན་བརྟགས་པར། །
ཅི་ཡི་ཕྱིར་ན་གསལ་མི་འགྱུར། །

[Block 516]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 517]
སྣང་བ་བྱུང་ན་མུན་ཁུང་ན་མེའི་ཚུལ་དུ་སྣང་བ་མི་དམིགས་པ་བཞིན་དུ་རིག་པ་བྱུང་ན། གང་ལོག་པ་དེ་ངེས་པར་མི་ཤེས་པས་ཡོངས་སུ་བརྟགས་པའི་ཕྱིར་ངོ་བོ་ཉིད་དུ་གྲུབ་པ་མེད་པར་གནས་སོ། །

[Block 518]
འདིའི་ཕྱིར་ཡང་འཇིག་རྟེན་དངོས་པོ་མེད་དེ། གཟུགས་བརྙན་བཞིན་དུ་རྒྱུ་དང་རྐྱེན་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 519]
དེ་ཉིད་བསྟན་པའི་ཕྱིར།

[Block 520 [HEADING]]
### ཚིགས་བཅད་སོ་དགུ་པ། ^1-40-0

[Block 521 [VERSE]]
རྒྱུ་ཡོད་པ་ལས་གང་བྱུང་ཞིང་། །
རྐྱེན་མེད་པར་ནི་གནས་པ་མེད། །
རྐྱེན་མེད་ཕྱིར་ཡང་འཇིག་འགྱུར་བ། །
དེ་ནི་ཡོད་པར་ཇི་ལྟར་ཤེས། །

[Block 522]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 523]
གལ་ཏེ་འཇིག་རྟེན་ངོ་བོ་ཉིད་དུ་གྲུབ་ན་ནི་དེའི་ཚེ༌[^320]རང་བཞིན་གྱི་ངོ་བོར་གྲུབ་པ་ཡོད་པས་རྒྱུ་དང་རྐྱེན་ལ་ལྟོས་ཏེ་འབྱུང་བར༌[^321]མི་འགྱུར་ཞིང་། རྒྱུ་དང་བཅས༌[^322]ལས་འབྱུང་བར་ཡང་མི་འགྱུར་ཏེ། ངོ་བོ་ཉིད་ནི་བྱས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 524]
གནས་པ་ཡང་རྐྱེན་ལ་རག་ལས་པར་མི་འགྱུར་རོ། །

[Block 525]
ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་ཡོད་ན་གཞན་དུ་འགྱུར་མི་སྲིད་དེ། འདི་ལྟར་གཞན་དུ་འགྱུར་བ་སྤང་བའི་ཕྱིར་གནས་པའི་རྐྱེན་བཙལ་བ་ནི་རིགས་པར༌[^323]འགྱུར་རོ། །

[Block 526]
གང་གནས་པའི་རྐྱེན་ལ་རག་ལས་པ་དེ་གཟུགས་བརྙན་བཞིན་དུ་ངོ་བོ་ཉིད་མེད་པར་གྲུབ་པ་ཡང་རིགས་སོ། །

[Block 527]
གང་ངོ་བོ་ཉིད་དུ་གྲུབ་པ་དེ་ནི་རང་བཞིན་གྱིས་མི་འགྱུར་བས་གནས་པའི་རྐྱེན་མེད་ཀྱང་ལྡོག་པ་མི་རིགས་སོ། །

[Block 528]
གང་གནས་པའི་རྐྱེན་མེད་ན་ལྡོག་པ་དེ་ནི་གཟུགས་བརྙན་བཞིན་དུ་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་མེད་པར་འོས་སོ། །

[Block 529]
གང་དེ་ལྟར་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་མེད་པ་དེ་གཞན་གྱིས་ཇི་ལྟར་ཡོད་པར་ཁོང་དུ་ཆུད་པའི་རྒྱུ་མེད་པས་དེ་ཡོད་པ་ཉིད་དུ་མི་རིགས་སོ་ཞེས་བྱ་བར་དགོངས་སོ། །

[Block 530]
མུ་སྟེགས་ཅན་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་མི་སྨྲ་བ་རྣམས་ཀྱི་དངོས་པོ་རྣམས་ལ་ངོ་བོ་ཉིད་ཡོད་པར་མངོན་པར་ཞེན་པ་གང་ཡིན་པ་དེ་ནི་རང་གི་གྲུབ་པའི་མཐའ་ལས་བྱུང་བ༌[^324]དང་མི་འགལ་བས།
--- END BLOCKS ---
