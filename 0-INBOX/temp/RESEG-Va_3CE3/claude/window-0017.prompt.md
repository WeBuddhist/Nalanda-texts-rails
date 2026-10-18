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
[Block 596]
དེ་ལྟ་བས་ན་བྱང་ཆུབ་ཀྱི་ངོ་བོ་ཉིད་ནི་སེམས་དཔའ་ཡིན་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 597]
དེ་ལྟར་ན་སེམས་ཅན་ཐམས་ཅད་ཀྱང་བྱང་ཆུབ་སེམས་དཔར་མི་འགྱུར་རམ་ཞེ་ན། སྤྱིར་གླེང་བ༌[^376]ལ་ཁྱད་པར་དུ་བརྗོད་པར་འདོད་པས་ཁྱད་པར་དུ་བྱང་ཆུབ་དང་འབྲེལ་བའི་སེམས་དཔའ་ལ་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བས་འདི་ལ་ཉེས་པ་མེད་དོ། །

[Block 598]
དེ་ལས་གཞན་པའི་སེམས་ཅན་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་མི་ཚོལ་ཞིང་དེའི་དོན་མི་སྒྲུབ་པ་རྣམས་ནི་བྱང་ཆུབ་དང་འབྲེལ་བ་གང་ཡང་མེད་པའི་ཕྱིར་འདི༌[^377]ནི་ཁྱད་པར་དུ་བྱང་ཆུབ་དང་འབྲེལ་བའི་སེམས་དཔའ་ལ་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱའོ། །

[Block 599]
དེ་བས་ན་འདིའི་སྤྱོད་པ་ཁྱད་པར་ཅན་ཡང་སྟོན་ཏེ། བྱང་ཆུབ་དེས་ཀྱང་ཆོས་ཐམས་ཅད་ཀྱི་རྣམ་པ༌[^378]ཤེས་ཏེ་ཆོས་དེ་དག་ལ་མངོན་པར་ཞེན་པ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པས་ནི་ཤེས་ཏེ་དོན་དམ་པར་ནི་མངོན་པར་ཞེན་པ་མེད་དོ། །

[Block 600]
རྣམ་པ་གང་དག་དང་། རྟགས་གང་དག་དང་། མཚན་མ་གང་དག་གིས་ཞེས་བྱ་བ་ལ་རྣམ་པ་གང་གིས་ཞེས་བྱ་བ་ནི་བསྟན་པའོ། །

[Block 601]
རྟགས་དང་མཚན་མ་གཉིས་ནི་དེའི་བཤད་པའོ། །

[Block 602]
མིང་དང་། བརྡ་དང་བརྟགས་པ་ལ་སོགས་པ་ནི་རྟགས་སོ། །

[Block 603]
མཚན་ཉིད་དང་། སྤྱོད་པ་ནི་མཚན་མའོ། །

[Block 604]
ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུས་གང་ལ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་དེ་ནི་རིང་དུ་སོང་བ་སྟེ་ཞེས་བྱ་བ་ལ། ཆོས་ཐམས་ཅད་ཀྱི་ཕ་རོལ་ཏུ་སོང་བའི་ཤེས་རབ་ནི་ཆོས་དེ་དག་ཐམས་ཅད་ལས་རིང་དུ་གྱུར་པའི་ཕྱིར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ། །

[Block 605]
ཐབས་དང་རིགས་པས་རྟོགས་པ༌[^379]ནི་ཉེ་བར་རྟོགས་པའོ། །

[Block 606 [HEADING]]
###### གཟུགས་ཀྱི་མ་སྐྱེས་པ་གཟུགས་མ་ཡིན་པ། ^1-1-7-3-2-0

[Block 607]
དེའི་འོག་ཏུ་འགྲེས་གཉིས་པ་ནི། ཚེ་དང་ལྡན་པ་རབ་འབྱོར་ཅིའི་ཕྱིར་དེ་སྐད་དུ་གཟུགས་ཀྱི་མ་སྐྱེས་པ་གང་ཡིན་པ་དེ་ནི་གཟུགས་མ་ཡིན་ཞེས་ཟེར་ཞེས་བྱ་བ་ལ་སོགས་པས་སྟོན་ཏོ། །

[Block 608]
ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ༌[^380]ཏིའི་བུ་གཟུགས་ནི་གཟུགས་ཀྱིས་སྟོང་ཞེས་བྱ་བ་ནི་རྣམ་པར་བརྟགས་པའི་གཟུགས་དེ་གཟུགས་ཀྱི་དངོས་པོར་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 609]
གཟུགས་ཀྱི་སྟོང་པ་ཉིད་གང་ཡིན་པ་དེ་གཟུགས་མ་ཡིན་ཏེ་སྐྱེ་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཆོས་ཉིད་ཀྱི་གཟུགས་ཀྱི་རང་བཞིན་སྟོང་པ་ཉིད་གང་ཡིན་པ་དེ་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་མ་ཡིན་ཞིང་སྐྱེ་བའི་ངོ་བོ་ཉིད་ཀྱང་མ་ཡིན་ནོ། །

[Block 610]
ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ༌[^381]ཏིའི་བུ་རྣམ་གྲངས་དེས་ན་གཟུགས་ཀྱི་མ་སྐྱེས་པ་གང་ཡིན་པ་དེ་གཟུགས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཀུན་བརྟགས་པའི་གཟུགས་ནི་སྐྱེ་བ༌[^382]མེད་པ་སྟེ་སྐྱེ་བའི་ངོ་བོ་ཉིད་ཀྱང་མ་ཡིན་ནོ། །

[Block 611]
དེ་བས་ན་མི་སྐྱེ་བ་ནི་གཟུགས་མ་ཡིན་པར་དེ་ལྟར་གྲུབ་པོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 612 [HEADING]]
###### གཟུགས་ཀྱི་འགྲིབ་པ་གཟུགས་མ་ཡིན་པ། ^1-1-7-3-3-0

[Block 613]
དེའི་འོག་ཏུ་འགྲེས་གསུམ་པའི་སྐབས་ནི་ཚེ་དང་ལྡན་པ་རབ་འབྱོར་ཅིའི་ཕྱིར་ན་དེ་སྐད་དུ་གཟུགས་ཀྱི་འགྲིབ་པ་གང་ཡིན་པ་དེ་ནི་གཟུགས་མ་ཡིན་ཞེས་ཟེར་ཞེས༌[^383]བྱ་བ་ལ་སོགས་པས་སྟོན་ཏོ། །

[Block 614]
གཟུགས་གང་ཡིན་པ་དང་འགྲིབ་པ་གང་ཡིན་པ་དེ་གཉི་ག་ཡང་ལྡན་པ་ཡང་མ་ཡིན་མི་ལྡན་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ནི་སྔར་བཤད་པའི་ཚུལ་གྱིས་གཟུགས་ཀྱང་བརྟགས་པ། འགྲིབ་པ་ཡང་བརྟགས་པ་སྟེ། དེ་བས་ན་གཉི་ག་ཡང་མཚན་ཉིད་མེད་པའོ།[^384] །

[Block 615 [HEADING]]
###### མ་སྐྱེས་པ་ཡང་གཞན་མ་ཡིན་གཟུགས་ཀྱང་གཞན་མ་ཡིན་པ། ^1-1-7-3-4-0

[Block 616]
འགྲེས་བཞི་པ་ལ། མ་སྐྱེས་པ་ཡང་གཞན་མ་ཡིན་གཟུགས་ཀྱང་གཞན་མ་ཡིན་ཏེ། མ་སྐྱེས་པ་ཉིད་ཀྱང་གཟུགས་སོ།[^385] །གཟུགས་ཉིད་ཀྱང༌[^386]མ་སྐྱེས་པ་ཞེས་བྱ་བ་ནི་སྔར་བཤད་པའི་ཚུལ་གྱིས་གཟུགས་ཞེས་བྱ་བ་དང་མ་སྐྱེས་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཉིད་ལ་བྱ་སྟེ། དེའི་ཕྱིར་གཉིས་སུ་མེད་དོ། །

[Block 617]
གཟུགས་ཀྱི་མ་སྐྱེས་པ་མཐོང་བར་འགྱུར་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་མངོན་སུམ་དུ་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 618]
གཟུགས་མ་སྐྱེས་པ་ཞེས་བྱ་བ་ནི། སྔ་མ་བཞིན་དུ་ཆོས་ཉིད་ཀྱི་གཟུགས་དང་དེ་བཞིན་ཉིད་གཅིག་པའི་ཕྱིར་དེ་སྐད་བསྟན་ཏོ། །

[Block 619 [HEADING]]
#### གནས་བརྟན་གཉིས་ཀྱིས་དྲིས་པ་དང་ལན་འདེབས་པ། ^1-1-8-0

[Block 620]
འདི་མན་ཆད་ནི་གནས་བརྟན་གཉིས་ཀྱིས་དྲིས་པ་དང་ལན་འདེབས་པ་ཞིབ་མོར་འབྱུང་སྟེ། ཚེ་དང་ལྡན་པ་རབ་འབྱོར་གལ་ཏེ་གཟུགས་ཀྱང་སྐྱེ་བ་མེད་ལ༌[^387]སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ཀྱི་བར་དུ་ཡང་སྐྱེ་བ་མེད་པ་ཡིན༌[^388]ན་ནི་ཉན་ཐོས་ཀྱིས་ཀྱང༌[^389]ཉན་ཐོས་ཀྱི་བྱང་ཆུབ་ཐོབ་ཟིན་པར་མི༌[^390]འགྱུར་རམ༌[^391]ཞེས་བྱ་བ་ལ་སོགས་པས་ཅི་བསྟན་ཞེ་ན། གལ་ཏེ་གཟུགས་ལ་སོགས་པ་དང་། དེ་བཞིན་ཉིད་གཅིག་པ་ཡིན་ན། དེ་ལྟ་ན་གཟུགས་ལ་སོགས་པ་རྟོགས་པས་དེ་བཞིན་ཉིད་རྟོགས་པར་འགྱུར་རོ། །

[Block 621]
སེམས་ཅན་ཐམས་ཅད་ཀྱང་དོན་དམ་པ་མཐོང་བར་འགྱུར་རོ། །

[Block 622]
དེ་ལྟར་གྱུར་ན་སེམས་ཅན་ཐམས་ཅད་ཀྱིས་བསྒྲིམ་མི་དགོས་པ་ཉིད་དུ་སོ་སོའི་བྱང་ཆུབ་ཇི་ལྟ་བ་བཞིན་དུ་ཐོབ་པར་འགྱུར་རོ། །

[Block 623]
འོ་ན་ནི་བྱང་ཆུབ་རྣམ་པ་ལྔ་པོ་དག་ཀྱང་ཐ་དད་པ་མེད་པར་འགྱུར་རོ། །

[Block 624]
རྒྱུན་དུ་ཞུགས་པ་དང་། ལན་ཅིག་ཕྱིར་འོང་བ་དང་། ཕྱིར་མི་འོང་བ་དང་། དགྲ་བཅོམ་པ་དང་། རང་བྱང་ཆུབ་དང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་རྣམས་ཀྱང་འདྲེས་པར་འགྱུར་རོ། །

[Block 625]
དེ་ལྟར་གྱུར་ན་རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པ་ཡང་སངས་རྒྱས་ཡིན་པར་འགྱུར་ཏེ། ཉོན་མོངས་པ་ལྷག་མ་སྤོང་བར་འབད་པ་དོན་མེད་པར་འགྱུར་རོ། །

[Block 626]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱང་བྱང་ཆུབ་ཐོབ་ཟིན་པས་དཀའ་བ་སྤྱད་པ་ལ་སོགས་པ་དོན་མེད་པར་འགྱུར་རོ། །

[Block 627]
རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་དང་། ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་ཡང་དོན་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 628]
ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ༌[^392]ཏིའི་བུ་བདག་ནི་ཆོས་མ་སྐྱེས་པ་ལ་འཐོབ་པ་དང་། མངོན་པར་རྫོགས་པ༌[^393]ཡོད་པར༌[^394]མི་འདོད་དོ། །

[Block 629]
བདག་ནི་མ་སྐྱེས་པ་ལ་རྒྱུན་དུ་ཞུགས་པ་ཡོད་པར་མི་འདོད། རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ཡོད་པར་མི་འདོད་དོ་ཞེས་བྱ་བས་ཅི་བསྟན་ཞེ་ན། ཆོས་མ་སྐྱེས་པ་ནི་སུས་ཀྱང་ཐོབ་པའམ། མངོན་པར་རྟོགས་པར༌[^395]མི་ནུས། མ་སྐྱེས་པ་ལ་གང་ཡང་རྒྱུན་དུ་ཞུགས་པར་མི་འགྱུར་གྱི། ཀུན་བརྟགས་པའི་སྒྲིབ་པ་ཙམ་བསྩལ་བ༌[^396]ནི་གཟུང་བ༌[^397]དང་འཛིན་པའི་རྣམ་པར་རྟོག་པ་མེད་པའི་ཕྱིར་ཐོབ་པ་དང་མངོན་པར་རྟོགས་པར་འདོད་དོ། །

[Block 630]
དེ་བས༌[^398]ན་དེ་བཞིན་ཉིད་ཀྱིས་དེ་བཞིན་ཉིད་རྟོགས་པ་མ་ཡིན་ནོ་ཞེས་བསྟན་པ་ཡིན་ཏེ། དེ་བས་ན་གཟུགས་ལ་སོགས་པ་རྟོགས་པས་དེ་བཞིན་ཉིད་རྟོགས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་སྔར་སྨྲས་པའི་སྐྱོན་དེ་སྐྱོན་དུ་མི་འགྱུར་ཏེ་ཉོན་མོངས་པ་དང་། ཤེས་བྱའི་སྒྲིབ་པ་རྣམས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 631]
ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ༌[^399]ཏིའི་བུ་བདག་ནི་བྱང་ཆུབ་སེམས་དཔའ་དཀའ་བ་སྤྱད་པ་སྤྱོད་པར་མི་འདོད་ཅེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་དོན་དམ་པར་དེ་ལྟ་བུའི་རྣམ་པར་རྟོག་པ་མེད་པའི་ཕྱིར་དེ་སྐད་བསྟན་ཏོ། །

[Block 632]
བྱང་ཆུབ་སེམས་དཔའ་ནི་ས་བརྒྱད་པ༌[^400]ལ་མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པས་གང་གི༌[^401]ཚེ་ཆོས་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ༌[^402]མི་དམིགས་པ་དེའི་ཚེ་སྐྱེ་བ་ལ་སོགས་པ་དང་བྲལ་བར་དཀའ་བ་སྤྱད་པ་རྩོམ་སྟེ། དེའི་ཚེ་བྱང་ཆུབ་སེམས་དཔའ་མི་དམིགས་པ་ཡིད༌[^403]ལ་བྱེད་པ་དང་ལྡན་པ་ལ་མགོ་བཅད་པ་ལ་སོགས་པ་ལ་དཀའ་བའི་འདུ་ཤེས་སམ། སྡུག་བསྔལ་གྱི་འདུ་ཤེས་གང་ཡང་མི་འབྱུང་ངོ་ཞེས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཐམས་ཅད༌[^404]རྣམ་པ་ཐམས་ཅད་དུ་ཆོས་གང་ཡང་མི་ལེན་མི་དམིགས་སོ་ཞེས་བྱ་བ་མཇུག་གི་ཚིག་གིས་བསྟན་ཏོ། །

[Block 633]
ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ༌[^405]ཏིའི་བུ་བདག་ནི་མ་སྐྱེས་པ་ལ་དེ་བཞིན་གཤེགས་པ་ཡོད་པར་མི་འདོད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་མ་སྐྱེས་པ༌[^406]ཆོས་ཀྱི་སྐུ་ལ་དེ་བཞིན་གཤེགས་པ་གང་གིས་མ་སྐྱེས་པ་རྟོགས་པར་འགྱུར་བའི༌[^407]དེ་བཞིན་གཤེགས་པ་གཉིས་པ་ཡོད་པར་མི་འདོད་པའོ། །

[Block 634]
དེ་བས་ན་མ་སྐྱེས་པ་ཉིད་དེ་བཞིན་གཤེགས་པ་མ་སྐྱེས་པ་ཉིད་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཡིན་ནོ་ཞེས་སྟོན་ཏོ། །

[Block 635]
མ་སྐྱེས་པའི་ཆོས་ཀྱིས་ཀྱང་མ་སྐྱེས་པ་ཐོབ་པར་མི་འདོད་དོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ཀྱིས་དེ་བཞིན་ཉིད་ལ་རབ་ཏུ་རྟོགས་པར་བྱེད་པར༌[^408]མི་འདོད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །
--- END BLOCKS ---
