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
[Block 5636]
འདི་ལྟར་གྱུར་པ་ལ་ཕན་འདོགས་པ་ཡང་ཤིན་ཏུ་དཀོན་ཞེས་བྱ་བ་ལ་འདི་དག་ཅེས་བྱ་བ་ནི་མི་སྐྱེ་བའོ། །

[Block 5637]
འདི་ལྟར་ཞེས་བྱ་བ་ནི་ད་ལྟར་བྱུང་བའི་དགེ་བ་དེས་མེད་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5638]
བདག་ནི་རྙེད་པར་བླ་བ༌[^3601]སྟེ། མིའི་སྐྱེ་བ་ལ་བསོད་ནམས་ཀྱི་ཚོགས་ལ༌[^3602]གོམས་པར་བྱས་པས་སྐྱེ་བ་གཞན་གྱི་རྒྱུ་བསྟན་པའི་ཕྱིར། བདག་གི་སྤྱོད་ཡུལ་གནས་སུ་ལྷགས་པར་གྱུར། །ཅེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5639]
[^3603]འདི་འདྲའི་མགྲོན་ཀྱང༌[^3604]བསོད་ནམས་བྱས་པས་འཐོབ། །ཅེས་བྱའོ།[^3605] །གལ་ཏེ་བདག་གིས་བོས་ཏེ། འདིར་འོངས་པ་མ་ཡིན་ན་ཡང་བསོད་ནམས་བྱས་པས་འཐོབ་ཅེས་བྱ་བ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། སྤྱོད་ཡུལ་གནས་སུ་ལྷགས་པར་གྱུར་པའི་ཕྱིར་ཏེ། རང་གིས་དོན་དུ་གཉེར་བ་ཉིད༌[^3606]བསྟན་ཏོ། །

[Block 5640]
ཕོངས་ཤིང་ཉམ་ཐག་གྱུར་ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་བ་ཉིད་དོ། །

[Block 5641]
གཉེན་དང་བྲལ་བ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་འབྲང་བ་མེད་པ་བསྟན་ཏོ། །

[Block 5642]
རྒྱུ་འདི་གསུམ་གྱིས་ནི་དེ་སྙིང་རྗེའི་གནས་སུ་བསྟན་ཏེ། དོན་དུ་གཉེར་བ་དང་། སྡུག་བསྔལ་བ་དང་། རྗེས་སུ་འབྲང་བ་མེད་པ་སྟེ། དེ་བས་ན་བསྐྱབ་པའི་རིགས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5643]
སྡུག་བསྔལ་མང་པོའི་གནས་ཞེས་བྱ་བ་ལ་ཅིའི་ཕྱིར་ཞེ་ན། རྟག་ཏུ་ན་བའི་ཕྱིར་ཏེ། ལྷན་ཅིག་སྐྱེས་པའི་སྡུག་བསྔལ་གྱིས་སོ། །

[Block 5644]
ཉོན་མོངས་པ་མང་པོའི་གཞི་ཞེས་བྱ་བ་ནི། གནོད་པ་སྣ་ཚོགས་སྐྱེ་བའི་ཉོན་མོངས་པའི་གཞི་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5645]
དེ་ནས་དེ་དག་ལ་ཁ་ཅིག་ནི་ཞེས་བྱ་བའི་ཚིག་གིས་ནི།

[Block 5646 [VERSE]]
སེམས་མི་བརྟན་པའི་དབང་དུ་བྱས་པའོ། །
བདག་ཅག་མགོན་མེད་རྣམས་ཀྱི༌[^3607]མགོན། །

[Block 5647]
ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི། སེམས་སྟོབས་བར་མའི་དབང་དུ་བྱས་པའོ། །

[Block 5648]
གཞན་ནི་སེམས་རབ་ཏུ་བརྟན་པས་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སེམས་བརྟན་པའི་དབང་དུ་བྱས་པའོ། །

[Block 5649]
བདེ་འགྲོ་ཐོབ་ཕྱིར་ཞེས་བྱ་བ་ནི་མི་ཉིད་དུ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 5650]
མི་དབང་རྒྱལ་སྲིད༌[^3608]གདུགས་གཅིག་དཔའ༌[^3609]ཕྱིར་ཞེས་བྱ་བ་ནི། རྒྱལ་སྲིད་ཀྱི་ཕྱིར་ཡང་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5651]
མཐོ་རིས་བདེ་མཆོག་མྱོང་བའི་ཕྱིར་མ་ཡིན། །ཞེས་བྱ་བ་ནི་འདོད་པ་ན་སྤྱོད་པའི་མངོན་པར་མཐོ་བ་ཐོབ་པའི་ཕྱིར་ཡང་མ་ཡིན་ནོ། །

[Block 5652]
ཚངས་པའི་གནས་ཕྱིར་མ་ཡིན་ཞེས་བྱ་བ་ནི། གཟུགས་དང་། གཟུགས་མེད་པ་ནི་གཡང་སར༌[^3610]མངོན་པར་མཐོ་བ་ཐོབ་པའི་ཕྱིར་ཡང་མ་ཡིན་པའོ། །

[Block 5653]
ཐར་པའི་བདེ་ཕྱིར་མིན་ཞེས་བྱ་བ་ནི། ཉན་ཐོས་དང་། རང་སངས་རྒྱས་ཀྱི་ཕྱིར་ཡང་མ་ཡིན་པའོ། །

[Block 5654]
གཡང་སར་ལྟུང་སྟེ་ཞིག་ན་ནི་འཆི་བའོ། །

[Block 5655]
དེ་གཉིས་ཀྱིས་བྱས་པའི་སྡུག་བསྔལ་ནི་གཡང་སར་ལྟུང་སྟེ་ཞིག་ནས་འཆི་བའི་སྡུག་བསྔལ་ལོ། །

[Block 5656]
དེ་ལ་མི་ལྟ་བ་གང་ཡིན་པ་དེ་ནི་གཡང་སར་ལྟུང་སྟེ་ཞིག་ནས་འཆི་བའི་སྡུག་བསྔལ་ལ་མི༌[^3611]ལྟ་བའོ། །

[Block 5657]
ས་ཕྱོགས་དེ་ཞེས་བྱ་བ་ནི་དེ་དག་ལ་སྔར་ཕྱོགས་གང་བསྟན་པའི་ཕྱོགས་དེར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5658]
གངས་རིའི་རྩེ་མོ་ཞེས་བྱ་བ་ནི་གངས་རི་ནས་ལྷུང་བ་དེའི་གངས་རི་དེའི༌[^3612]རྩེ་མོ་ཉིད་དོ། །

[Block 5659]
གནམ་གྲུམ་པའི་སྒྲ་གང་ལ་ཡོད་པ་དེ་ནི། གནམ་གྲུམ་སྒྲ་བཞིན་ནོ། །

[Block 5660]
མ་བཏགས་ཞེས་བྱ་བ་ནི་དཔག་བསམ་གྱི་ཤིང་ལས་བྱུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5661 [VERSE]]
མེ་ཏོག་ཀུ་མུད་སྤུངས་ལྟར་མཛེས། །
ཟླ་བའི་འོད་ཟེར་སྤུངས་པ་བཞིན། །

[Block 5662]
ཞེས་བྱ་བ་དེ་དེ་གཉིས་ཀྱིས་མདོག་བསྟན་ཏོ། །

[Block 5663]
འདི་ནི་དེ་ཡི་གཟུགས་བརྙན་ཞིག །ཅེས་བྱ་བ་འདིས་ནི་ཁ་དོག་དང་། དབྱིབས་གཉིས་མཉམ༌[^3613]པར་བསྟན་ཏོ། །

[Block 5664]
བདག་ཅག་རྣམས་ཀྱི་ཆོ་རིགས་དང་། ཚུལ་དང་། དད་པ་ཅི་འདྲ་ཞེས་བྱ་བ་འདིས་ནི་ཡོན་ཏན་དང་། ཕན་གདགས་པའི་ཞིང་ཉིད་མ་ཡིན་པ༌[^3614]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5665]
ཡང་ན་ཡོན་ཏན་གྱི་ཞིང་ཉིད་མ་ཡིན་པའོ། །

[Block 5666]
ཆོ་རིགས་ཞེས༌[^3615]སྨོས་པས་ནི་བྲམ་ཟེའི་རིགས་ནི་འཇིག་རྟེན་པ་རྣམས་ཀྱིས་བཀུར་བའི་གནས་ཡིན་པའི་ཕྱིར་དེ་ཡང་མ་མཐོང་བའོ། །

[Block 5667]
ངང་ཚུལ་གྱི༌[^3616]ཞེས་བྱ་བ་ནི་ཡོན་ཏན་གྱི་ཞིང་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5668]
དད་པ་ཞེས་བྱ་བ་ནི་ཕན་འདོགས་པའི་ཞིང་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5669]
སྐལ་མཉམ་ཞེས་བྱ་བ་ནི་སྙིང་རྗེའི་ཞིང་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5670]
མ་ཐོས་པར་ཞེས་བྱ་བ་ནི་མ་འདྲིས་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5671]
ཕོངས་ཤིང་ཉམ་ཐག་ཅེས་བྱ་བ་ནི་སྡུག་བསྔལ་བ་ཉིད་དོ། །

[Block 5672]
[^3617]འཇིགས་ལ༌[^3618]མྱ་ངན་གདུངས་ཞེས་བྱ་བ་ནི་རྗེས་སུ་འབྲང་བ༌[^3619]མེད་པའོ། །

[Block 5673]
སྤྱོད་བཟང་འདི་འདྲ་གང་དུ་བསླབས་ཞིག་གུ། །ཞེས་བྱ་བ་ནི་མཁན་པོ་གང་ཡིན་པའི་དོན་ཏོ། །

[Block 5674]
བླ་མ་གང་ལ་གནས་ནས་བསྙེན་བཀུར་བྱས། །ཞེས་བྱ་བ་ནི་དཔོན་གང་ལ་བསྙེན་བཀུར༌[^3620]བྱས་པའོ། །

[Block 5675]
དེ་ནི་འདི་ལས་མངོན་ཞེས་བྱ་བ་ནི་གཟུགས་དང་རྗེས་སུ་མཐུན་པ་ཉིད་ཀྱིས་ཡོན་ཏན་མངོན་པའི་དོན་ཏོ། །
--- END BLOCKS ---
