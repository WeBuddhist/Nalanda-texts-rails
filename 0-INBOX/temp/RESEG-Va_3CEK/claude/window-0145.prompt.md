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
[Block 5076]
དེ་བཞིན་དུ་ལས་ལས་འབྲས་བུ་འབྱུང་ངོ་། །[^3588]ཞེས་བྱ་བ་དེ་ཡང༌[^3589]ལས༌[^3590]ཞིག་པ་ལས་ཀྱང་མི་འབྱུང་ལ། མཇུག་ཐོགས་སུ་ཡང་མ་ཡིན་ནོ། །

[Block 5077]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། རྒྱུད་ཡོངས་སུ་འགྱུར་བའི་ཁྱད་པར་ལས་སོ། །

[Block 5078]
རྒྱུད་ནི་ཅི་ཡིན། ཡོངས་སུ་འགྱུར་བ་ནི་ཅི་ཡིན། ཁྱད་པར་ནི་ཅི་ཡིན་ཞེ་ན། ལས་སྔོན་དུ་འགྲོ་བའི་སེམས་ཕྱིར་ཞིང་འབྱུང་བ་གང་ཡིན་པ་དེ་ནི་རྒྱུད་ཡིན་ནོ། །

[Block 5079]
དེ་གཞན་དང་གཞན་དུ་སྐྱེ་བ་ནི་ཡོངས་སུ་འགྱུར་བ་ཡིན་ནོ། །

[Block 5080]
དེའི༌[^3591]མཇུག་ཐོགས་སུ་འབྲས་བུ་སྐྱེད་ནུས་པ་གང་ཡིན་པ་དེ་ནི་ཡོངས་སུ་འགྱུར་བ་གཞན་ལས་ཁྱད་པར་དུ་འཕགས་པའི་ཕྱིར་ཡོངས་སུ་འགྱུར་བའི་ཁྱད་པར་ཡིན་ཏེ། [^3592]དཔེར་ན་ཡང་སྲིད་པའི་ཉེ་བར་ལེན་པ་དང་བཅས་པའི་འཆི་བའི་སེམས་ལྟ་བུའོ། །

[Block 5081]
ལས་རྣམ་པ་སྣ་ཚོགས་པ་སྔོན་དུ་འགྲོ་བ་ཉིད་ཡིན་ཡང་ལས་གང་ལྕི་བའམ། ཉེ་བའམ། གོམས་པ་ཡིན་པ་དེས་བྱས་པའི་ནུས་པ༌[^3593]བསལ་བར་བྱེད་ཀྱི་གཞན་གྱིས་ནི་མ་ཡིན་ཏེ། ཇི་སྐད་དུ། ལས་ཀྱི་འཁོར་བ་ལྕི་གང་དང་། ཉེ་བ་གང་དང་གོམས་པ་གང་།[^3594] །

[Block 5082 [VERSE]]
སྔོན་བྱས་གང་ཡིན་དེ་ལས་ནི། །
སྔ་མ་སྔ་མ་རྣམ་སྨིན་འགྱུར། །

[Block 5083]
ཞེས་བཤད་པ་ལྟ་བུའོ། །

[Block 5084]
དེ་ལ་རྣམ་པར་སྨིན་པའི་རྒྱུས་བསྐྱེད་པ་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་བསྐྱེད་པའི་ནུས་པ་ནི་རྣམ་པར་སྨིན་པ་བསྐྱེད༌[^3595]ནས་ལྡོག་གོ། །

[Block 5085]
སྐལ་བ་མཉམ་པའི་རྒྱུས་བསྐྱེད་པ་རྒྱུ༌[^3596]མཐུན་པའི་འབྲས་བུ་བསྐྱེད་པའི་ནུས་པ་ནི་ཉོན་མོངས་པ་ཅན་རྣམས་ཀྱི་ནི་གཉེན་པོ་སྐྱེས་ནས་ལྡོག་གོ། །

[Block 5086]
ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་རྣམས་ཀྱི་ནི་སེམས་ཀྱི་རྒྱུན་གཏན་དུ་ལོག་པ་སྟེ། གང་གི་ཚེ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་ནའོ། །

[Block 5087]
ཡང་ཅིའི་ཕྱིར་ས་བོན་གྱི་འབྲས་བུ་བཞིན་དུ༌[^3597]རྣམ་པར་སྨིན་པ་གཞན་མི་སྐྱེ༌[^3598]ན། རེ་ཞིག་ཐམས་ཅད་དཔེ་དང་འདྲ་བ་ནི་མ་ཡིན་ནོ། །

[Block 5088]
དེ་ལ་ཡང་འབྲས་བུ་ཁོ་ན་ལས་འབྲས་བུ་གཞན་སྐྱེ་བ་མ་ཡིན་ནོ། །

[Block 5089]
འོ་ན་ཅི་ཞེ་ན། རྣམ་པར་འདྲུལ་བའི༌[^3599]ཁྱད་པར་ལས་སྐྱེས་པ་རྣམ་པར་འགྱུར་བའི་ཁྱད་པར་ལས་སྐྱེ་སྟེ། དེ་ལ་འབྱུང་བའི་རྣམ་པ་མྱུ་གུ་འགྲུབ་པར་བྱེད་པ་ཡོད་པ་གང་ཡིན་པ་དེ་ནི་དེའི་ས་བོན་ཡིན་གྱི་གཞན་ནི་མ་ཡིན་ནོ། །

[Block 5090]
འགྱུར་བའི་མིང་གིས་སམ། འདྲ་བའི་ཕྱིར་རྒྱུན་སྔ་མ་ཡང་ས་བོན་ཞེས་བྱའོ། །

[Block 5091]
དེ་བཞིན་དུ་འདི་ལ་ཡང་རྣམ་པར་སྨིན་པ་དེ་ལས་གལ་ཏེ་དམ་པ་དང་དམ་པ་མ་ཡིན་པའི་ཆོས་ཉན་པ་ལ་སོགས་པའི་རྐྱེན་ལས་སྐྱེས་པ་དགེ་བ་ཟག་པ་དང་བཅས་པའམ། མི་དགེ་བའི༌[^3600]སེམས་ཀྱི་འགྱུར་བ་སྐྱེ་ན་དེ་ལས་ནི་རྣམ་པར་སྨིན་པ་གཞན་སྐྱེའི༌[^3601]གཞན་དུ་ནི་མ་ཡིན་པས་འདི་ནི་མཚུངས་སོ། །

[Block 5092]
ཡང་ན་དེ་ནི་འདི་ལྟར་ཤེས་པར་བྱ་སྟེ། ཇི་ལྟར་མ་དུ་ལུང་གའི་མེ་ཏོག་རྒྱ་སྐྱེགས་ཀྱི་ཁུ་བས་ཁ་དོག་བསྒྱུར་བ་ལས་འབྲས་བུའི་ནང་དུ་རྒྱུད་ཡོངས་སུ་འགྱུར་བའི་ཁྱད་པར་ལས་སྐྱེས་པ་གེ་སར་དམར་པོ་སྐྱེ་བར་འགྱུར་ཞིང་དེ་ལས་ནི༌[^3602]གཞན་མི་སྐྱེ་བ་དེ་བཞིན་དུ་ལས་ལས་སྐྱེས་པའི་རྣམ་པར་སྨིན་པ་ལས་ཡང་རྣམ་པར་སྨིན་པ་གཞན་མི་སྐྱེའོ། །

[Block 5093]
ཆེ་ལོང་ཙམ་འདི་ནི་བདག་གི་བློས་རྟོགས་པར་བྱ་བ་རབ་ཏུ་བསྟན་པ་ཡིན་ཏེ། མཐུ་རྣམ་པ་སྣ་ཚོགས་པས་ཐ་དད་པའི་ལས་རྣམས་ཀྱིས་བསྒོས་པའི་རྒྱུ་རྣམས་གནས་སྐབས་འདིར་ཕྱིན་ན་འབྲས་བུ་འདི་ལྟ་བུ་མངོན་པར་འགྲུབ་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་རྣམས་ཁོ་ནའི་ཡུལ་ཡིན་ནོ། །

[Block 5094]
ཡང་སྨྲས་པ།

[Block 5095 [VERSE]]
ལས་དང་དེའི་བསྒོས་དེའི་འཇུག་རྙེད། །
དེ་ལས་འབྲས་བུ་སངས་རྒྱས་ལས། །
གཞན་གྱི་རྣམ་པ་ཐམས་ཅད་ནི། །
ངེས་པར་རབ་ཏུ་མི་ཤེས་སོ། །

[Block 5096 [HEADING]]
### ཕྱོགས་ཙམ་ཞིག་ཤིན་ཏུ་མཁས་པ་རྣམས་ལ་བསྟན་པ། ^6-4-0

[Block 5097 [VERSE]]
དེ་ལྟར་སངས་རྒྱས་རྣམས་ཀྱི་གསུང་རབ་རིགས་པའི་ལམ། །
ལེགས་པར་གསུངས་པའི་དག་པ་ཆོས་ཉིད་འདི་མཐོང་ནས། །
མུ་སྟེགས་ལོང་བ་ལྟས་ངན༌[^3603]སྣ་ཚོགས་གཡོ་རྣམས་ཀྱི། །
གཞུང་ལུགས་སྤངས་ཏེ་ལོང་བ་མ་ཡིན་རྣམས་འགྲོའོ། །

[Block 5098 [VERSE]]
དེ་བཞིན་གཤེགས་པ་ཉི་མའི་གསུང་འོད་ཀྱིས། །
སྣང་ལྡན་མྱ་ངན་འདས་གྲོང་ལམ་གཅིག་པ། །
བདག་མེད་འཕགས་པ་སྟོང་གིས༌[^3604]བགྲོད་པ་འདི། །
ཕྱེ་ཡང་དམན་པའི་མིག་གིས་མི་མཐོང་ངོ་། །

[Block 5099 [VERSE]]
དེ་ལྟར་འདི་ནི་ཕྱོགས་ཙམ་ཞིག །
རང་གི་མཐུ་ཡིས༌[^3605]རྣམ་འཕེལ་བའི། །
དུག་ལ་རྨ་ཡི་ཕྱོགས་བཞིན་དུ། །
ཤིན་ཏུ་མཁས་པ་རྣམས་ལ་བསྟན། །

[Block 5100 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 5101 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 5102]
ཆོས་མངོན་པའི་མཛོད་ལས་གང་ཟག་དགག་པ་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་དགུ་པ་སྟེ། ཆོས་མངོན་པའི་མཛོད་ཀྱི་བཤད་པ་སློབ་དཔོན་ཤཱཀྱའི་དགེ་སློང་དབྱིག་གཉེན་གྱིས་མཛད་པ་འདི་རྫོགས་སོ།། །།

[Block 5103 [HEADING]]
### འགྱུར་བྱང། ^b-2-0

[Block 5104]
རྒྱ་གར་གྱི་མཁན་པོ་ཛི་ན་མི་ཏྲ་དང་། ཞུ་ཆེན་གྱི་ལོ་ཙཱ་བ་བན་དེ་དཔལ་བརྩེགས་ཀྱིས་བསྒྱུར་ཞིང་ཞུས་ཏེ་གཏན་ལ་ཕབ་པ།། །།
--- END BLOCKS ---
