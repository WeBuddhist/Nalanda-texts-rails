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
[Block 666]
དེ་ལ་འདི་འདྲི་སྟེ། ཅི་གང་གི་ཚེ་ས་བོན་ལས་མྱུ་གུ་ལ་སོགས་པ་སྐྱེ་བའི་ཕྱིར། མྱུ་གུ་སྐྱེ་བ་དེ་མ་བྱུང་མ་སྐྱེས་པ་ཞིག་སྐྱེ་འམ། འོན་ཏེ་བྱུང་ཞིང་སྐྱེས་ཟིན་པ་ཞིག་སྐྱེ་ཞེས་བྱ་བའོ། །

[Block 667]
དེ་སྐད་ཅེས༌[^440]སྨྲས་པ་དང་། གལ་ཏེ་མྱུ་གུ་མ་སྐྱེས་པ་སྐྱེ་ན་ནི་མ་སྐྱེས་པ་ཐམས་ཅད་ཀྱང་ངེས་པ་མེད་པར་སྐྱེ་བར་འགྱུར་རོ། །

[Block 668]
གལ་ཏེ་སྐྱེས་ཟིན་པ་ཞིག་སྐྱེ་ན་ནི་ཡང་དང་ཡང་དུ་བཟླས་ཏེ། སྐྱེ་བར་འགྱུར་བ་ལ་སོགས་པ་རིགས་པ་དང་འགལ་བར་འགྱུར་བའི་ཕྱིར་གཉི་ག་ལྟར་ཡང་སྨྲར་མི་རུང་ནས། ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ༌[^441]ཏིའི་བུ་བདག་ནི་མ་སྐྱེས་པའི་ཆོས་ཀྱང་སྐྱེ་བར་མི་འདོད། [^442]སྐྱེས་པའི་ཆོས་ཀྱང་སྐྱེ་བར་མི་འདོད་དོ་ཞེས་གནས་བརྟན་གྱིས༌[^443]སྨྲས་ཏེ། མ་སྐྱེས་པ་ནི་མ་སྐྱེས་པ་ཉིད་ཀྱི་ཕྱིར་མེད་དེ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་མི་སྐྱེའོ། །

[Block 669]
སྐྱེས་པ་ཡང་སྐྱེས་ཟིན་པ༌[^444]ཉིད་ཀྱི་ཕྱིར་ཡང༌[^445]མི་སྐྱེ་སྟེ། དེ་བས་ན་དོན་དམ་པར་སྐྱེ་བའི་ཆོས་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 670]
དེ་སྐད་སྨྲས་པ་དང་འགའ་ཞིག་མ་སྐྱེས་པའི་ཆོས་རི་བོང་གི་རྭ་ལ༌[^446]སྐྱེ་བ་མེད་དམ་སྐྱེས་པ་འདས་པ་རྣམས་ལ་སྐྱེ་བ་མེད་དམ་ཞེས་སྨྲར་འོང་ཞེས་དེའི་ཕྱིར། ཚེ་དང་ལྡན་པ་རབ་འབྱོར་ཁྱོད༌[^447]མ་སྐྱེས་པའི་ཆོས་སྐྱེ་བར་མི་འདོད་པ་གང་ཡིན་ཞེས་བྱ་བ་དང་། སྐྱེས་པ་སྐྱེ་བར་མི་འདོད་པ་གང་ཡིན་ཞེས་བྱ་བའི་འགྲེས་གཉིས་དྲིས་སོ། །

[Block 671]
ཡང་སྐྱེ་བ་བསྩལ་བའི་ཕྱིར། ཚེ་དང་ལྡན་པ་རབ་འབྱོར་ཅི༌[^448]མ་སྐྱེས་པའི་ཆོས་སྐྱེ་བར་འགྱུར་རམ། འོན་ཏེ་སྐྱེས་པའི་ཆོས་སྐྱེ་བར་འགྱུར་ཞེས་དེ་སྐད་སྨྲས་པ་དང་། མི་སྐྱེ་བ་ནི་འདུས་མ་བྱས་པའི་ཕྱིར་མི་སྐྱེ་ལ། སྐྱེ་བ་ཡང་ཀུན་བརྟགས་པ་སྟེ། ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་མི་སྐྱེ་བས་གནས་བརྟན་གྱིས། ཚེ་དང་ལྡན་པ་ཤ་ར་དྭི་ཏི༌[^449]བུ་སྐྱེ་བ་ཡང་མི་སྐྱེ། མི་སྐྱེ་བ་ཡང་མི་སྐྱེའོ་ཞེས་བྱ་བ་གསུངས་པ་དེའི་གཏན་ཚིགས་སུ་ཚེ་དང་ལྡན་པ་ཤ་ར་དྭི༌[^450]ཏིའི་བུ་འདི་ལྟར་སྐྱེ་བ་གང་ཡིན་པ་དང་མི་སྐྱེ་བ་གང་ཡིན་པ་དེ་གཉིས་ཀ་ཡང་ལྡན་པ་ཡང་མ་ཡིན་མི་ལྡན་པ་ཡང་མ་ཡིན་ཏེ། མི་སྐྱེ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ཡང་གསུངས་ཏེ། དེ་ལྟ་ཡིན༌[^451]ཡང་གཉི་ག་ཡང་དོན་དམ་པར་དེ་བཞིན་ཉིད་ཙམ་དུ་ཟད་དོ་ཞེས་བྱ་བར་དགོངས་པའོ། །

[Block 672]
དེ་སྐད་བསྟན་ནས༌[^452]སྐྱེ་བ་མེད་པའི༌[^453]འགྲེས་སྔར་བསྟན་པ་ཉིད་ཀྱང་བསྟན་ཏེ། དེ་ལྟར་ན་གཟུགས་སྐྱེ་བ་མེད་དོ་ཞེས་བྱ་བ་ནས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་བར་དུ་སྐྱེ་བ་མེད་དོ་ཞེས་བསྟན་ནས། ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ༌[^454]ཏིའི་བུ་རྣམ་གྲངས་འདིས་ན་བརྗོད་པ་ནི་སྐྱེ་བ་མེད་པ་སྟེ། སྤོབས་པ་ཡང་སྐྱེ་བ་མེད་ལ། ཆོས་ཀྱང་སྐྱེ་བ་མེད་དེ་གང་དག་ལས་བརྩམས་ཏེ་བརྗོད་པར་སྤོབས་པའི་ཆོས་དེ་དག་ཀྱང་སྐྱེ་བ་མེད་པའོ་ཞེས་མཇུག་བསྡུས་སོ། །

[Block 673]
ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ༌[^455]ཏིའི་བུ་གཟུགས་རང་བཞིན་གྱིས་སྟོང་པ་སྟེ་ཞེས་བྱ་བ་ནི་ཆོས་ཉིད་ཀྱི་གཟུགས་བསྟན་པ་སྟེ། དེ་བས་ན་དེ་ནི་ནང་ན་ཡང་མི་གནས་ཕྱི་རོལ་ན་ཡང་མི་གནས། གཉིས་ཀ་མེད་པར་ཡང་མི་དམིགས་སོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 674]
གལ་ཏེ་དེ་འགའ་ཞིག་ལ་གནས་ན་ནང་ངམ་ཕྱི་རོལ་ལམ། གཉི་ག་ལས་གཞན་འགའ་ཞིག་ལ་གནས་གྲང་ན། འདི་ལྟར་དེ་གསུམ་ཆར་ལ་ཡང་དོན་དམ་པར་མེད་དེ། དེ་བས་ན་མི་གནས་པའོ། །

[Block 675]
དེ་སྐད་བསྟན་ནས་གནས་པ་དང་མི་གནས་པ་དེ་ཉིད་ཀྱི་མཚན་ཉིད་ལེགས་པར་རྒྱ་བསྐྱེད་དེ་བྱང་ཆུབ་ཀྱི་ལམ་ཡོངས་སུ་སྤྱད་པའི་ཐབས་སྟོན་ཏེ། འཇིག་རྟེན་པ་ཡང་ཡོད་འཇིག་རྟེན་ལས་འདས་པ་ཡང་ཡོད་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 676]
འཇིག་རྟེན་ལས་མི་གཡོ་མི་འཕགས་མི་འདའ་ཞེས་པ་བྱ་དེ༌[^456]ཀུན་བརྟགས་པ་ལས་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། བཟོད་པ་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོའི་དབང་གིས་རྣམ་པ་གསུམ་མོ། །

[Block 677]
ལྷག་མ་ནི་དོན་གསལ་ལོ། །

[Block 678]
གང་དག་གིས་འཇིག་རྟེན་དུ་འགྱུར་བ་ཞེས་བྱ་བ་ལ་སོགས་པའི༌[^457]ཚིག་བདུན་ནི་དེ་ལ་ཁ་ཅིག་ཏུ་ནི་འཇིག་རྟེན་གྱི་སྒྲ་ཕུང་པོ་ལྔ་ལ་བྱ། ཁ་ཅིག་ཏུ་ནི་སེམས་ཅན་གྱི་འཇིག་རྟེན། ཁ་ཅིག་ཏུ་ནི་སྣོད་ཀྱི་འཇིག་རྟེན། ཁ་ཅིག་ཏུ་ནི་སོ་སོའི་སྐྱེ་བོའི་འཇིག་རྟེན། ཁ་ཅིག་ཏུ་ནི་འཁོར་བ། ཁ་ཅིག་ཏུ་ནི་ཀུན་བརྟགས་པའི་ཆོས་རྣམས། ཁ་ཅིག་ཏུ་ནི་འདོད་པའི་ཡོན་ཏན་ལྔ་རྣམས་ལ་བྱ་སྟེ། གང་དག་གིས་འཇིག་རྟེན་དུ་འགྱུར་བ་ཞེས་བྱ་བ་ནི་ཕུང་པོའི་འཇིག་རྟེན་ནོ། །

[Block 679]
གང་དག་འཇིག་རྟེན་འགྲུབ་པར་བྱེད་པ་ཞེས་བྱ་བ་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་ནོ། །

[Block 680]
གང་དག་འཇིག་རྟེན་དང་མཉམ་པ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པའི་ཆོས་རྣམས་དང་མཉམ་པའོ། །

[Block 681]
གང་དག་གིས་འཇིག་རྟེན༌[^458]གྱི་ཕྱིར་སྦྱིན་པ་ཞེས་བྱ་བ་ནི་འདོད་པའི་ཡོན་ཏན་ལྔ་འཇིག་རྟེན་གྱི་ཕྱིར་སྦྱིན་པའོ། །

[Block 682]
གང་དག་གིས་འཇིག་རྟེན་ལས་འབྱུང་བར་མི་འགྱུར་བ་ཞེས་བྱ་བ་ནི་འཁོར་བའི་འཇིག་རྟེན་ལས་སོ། །

[Block 683]
གང་དག་འཇིག་རྟེན་འབྱུང་བར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་སོ་སོའི་སྐྱེ་བོའི་འཇིག་རྟེན་ཏེ། འབྱུང་བ་ནི་འཕེལ་བའི་ཕྱིར་རོ། །

[Block 684]
གང་དག་འཇིག་རྟེན་དུ་འབྱུང་བར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་དུ་སེམས་ཅན་གྱི་འཇིག་རྟེན་འབྱུང་ངོ་། །གང་དག་གིས་འཇིག་རྟེན་སྒྲོལ་བ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གྱི་འཇིག་རྟེན་ནོ། །

[Block 685]
གང་དག་འཇིག་རྟེན་སེལ་བར་བྱེད་པ་ཞེས་བྱ་བ་ནི་འདོད་པའི་ཡོན་ཏན་ལྔ་རྣམས་སོ། །

[Block 686]
འཇིག་རྟེན་གྱིས་གང་དག་གིས་སྒྲོལ་བར་བྱེད་པ་ཞེས་བྱ་བ་ནི་འཕགས་པའི་གང་ཟག་གི་འཇིག་རྟེན་གྱིས་སོ། །

[Block 687]
གང་དག་འཇིག་རྟེན་མ་ཡིན་པར་འགྱུར༌[^459]ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གྲུབ་པར་འགྱུར་བའོ། །

[Block 688]
གང་དག་གིས་འཇིག་རྟེན་ལས་འབྱུང་བར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་འཁོར་བའི་འཇིག་རྟེན་ལས་འབྱུང་བའོ། །

[Block 689]
གང་དག་འཇིག་རྟེན་ལས་སྒྲོལ་བ་ཞེས་བྱ་བ་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་ལས་སོ། །

[Block 690]
གང་དག་འཇིག་རྟེན་དུ་སྒྲོལ་བར་བྱེད་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་འཇིག་རྟེན་རྣམས་སུའོ། །

[Block 691]
ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ༌[^460]ཏིའི་བུ་ལེགས་སོ་ལེགས་སོ། །

[Block 692]
ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ༌[^461]ཏིའི་བུས་ཡང་དག་པའི་ཚིག་བརྗོད་པས་དོན་ཉིད་ཡོངས་སུ་བཟུང་བ་ནི་ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ༌[^462]ཏིའི་བུ་དམིགས་སུ་ཕེབས་སོ་ཞེས་བྱ་བ་ནི་ཤཱ་རིའི་བུའི་ཚིག་ལ་ཚིག་རྣམ་པ་གསུམ་གྱིས་རྗེས་སུ་ཡི་རང་བའི་ཚིག་སྟེ། ལེགས་ཤིང་རིགས་པས་དམིགས་སུ་ཕེབས་པར་དོན་ཡོངས་སུ་བཟུང་ངོ་ཞེས་སྟོན་ཏོ། །

[Block 693]
སེམས་ཅན་མེད་པའི་ཕྱིར་ཡིད་ལ་བྱེད་པ་མེད་པར་རིག་པར་བྱའོ། །

[Block 694]
སེམས་ཅན་སྟོང་པ་ཉིད་ཀྱི་ཕྱིར་ཡིད་ལ་བྱེད་པ་སྟོང་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 695]
སེམས་ཅན་དབེན་པ་ཉིད་ཀྱི་ཕྱིར་ཡིད་ལ་བྱེད་པ་དབེན་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 696]
སེམས་ཅན་ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་ཡིད་ལ་བྱེད་པ་ངོ་བོ་ཉིད་མེད་པར་རིག་པར་བྱའོ། །

[Block 697]
སེམས་ཅན་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བ་མེད་པའི་ཕྱིར་ཡིད་ལ་བྱེད་པ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བ་མེད་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ཡིད་ལ་བྱེད་པ་དེ་ལྔ་དེ་ལས་གཞན་པ་རྣམས་ལ་མེད་དེ་དེ་བས་ན་དེ་དག་བྱང་ཆུབ་སེམས་དཔའ་མ་ཡིན་ནོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 698]
དེ་བས་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ༌[^463]ཆེན་པོ་ནི་གནས་པ་འདི་དང་། ཡིད་ལ་བྱེད་པ་འདི་དང་མ་བྲལ་ལོ་ཞེས་བདག་སྨྲའོ་ཞེས་བསྟན་ཏོ། །

[Block 699]
དེ་ལྟར་རེ་ཞིག་ཆོ་འཕྲུལ་བསྟན་པ་དང་བཅས། འབྲས་བུ་བསྟན་པ་དང་བཅས་པར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འབྲིང་དུ་བཤད་པ་ཡོངས་སུ་རྫོགས་པར་བྱས་པ་ཡིན་ནོ། །

[Block 700]
དེ་བཞིན་གཤེགས་པ༌[^464]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདིས་མདོ་དང་འབྲིང་དང་རྒྱས་པ་རྣམ་པ་གསུམ་དུ་བསྟན་ཏོ་ཞེས་བཤད་དེ། དེ་ལ་འདུལ་བའི་དབང་གིས་མདོ་དང་འབྲིང་གི་ཚུལ་གཉིས་ནི་བསྟན་ཟིན་ཏོ། །

[Block 701]
[^465]

[Block 702 [HEADING]]
### རྒྱས་པར་བཤད་པ། ^1-2-0

[Block 703 [HEADING]]
#### ལྷའི་དབང་པོས་ཞུས་པ། ^1-2-1-0

[Block 704]
འདི་མན་ཆད་ནི་འདུལ་བའི་འགྲོ་བའི་ཡོངས་སུ་མ་སྨིན་པ་རྣམས་ཀྱི་ཐེ་ཚོམ་སྐྱེས་ཤིང་སྐྱེས་པ་རྣམས་བསལ་བས་ཡོངས་སུ་སྨིན་པར་བྱས་ནས་ཡོངས་སུ་སྨིན་པ་རྣམས་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་རྟོགས་པར་བྱེད་པ་ཀུན་རྫོབ་དང་དོན་དམ་པའི་ཚུལ་རྣམ་པར་དབྱེ་བས་རྒྱས་པ་རྣམ་པ་གཉིས་སུ་བསྟན་ཏེ། དེ་ནས་སྟོང་གསུམ་གྱི་སྟོང་ཆེན་པོའི་འཇིག་རྟེན་གྱི་ཁམས་འདི་ན་རྒྱལ་པོ་ཆེན་པོ་གང་དག་འཁོད་པ་དེ་དག་ཐམས་ཅད་དང་། ལྷའི་བུ་བྱེ་བ་ཁྲག་ཁྲིག་འབུམ་ཕྲག་དུ་མ་ལྷན་ཅིག་ཏུ་འཁོར་དེ་ཉིད་དུ་འདུས་པར་གྱུར་ཏོ༌[^466]ཞེས་བྱ་བ་ལ་སོགས་པས་ཅིའི་ཕྱིར་ལྷ་རྣམས་འདུས་པར༌[^467]ཡང་བསྟན་ལ། དེ་བཞིན་གཤེགས་པའི་མཐུ་བརྗོད་པའི་སྐབས་ནི་གང་ཡིན་ཞེ་ན། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་པ་འདི་སྔོན་མ་བྱུང་བའི་ཕྱིར་སྔོན་མ་བྱུང་བའི་ཆོས་བསྟན་པའི་ལྟས་སུ་འཁོར་འདུས་པ་ཡང་མདོར་བསྟན་དགོས་སོ། །

[Block 705]
འོད་ཟེར་འབྱིན་ཅིང་འོད་བཀོད་པ་ཡང་སྟོན་ཞེས་འབྱུང་བས་ན་ཆོས་བཤད་པའི་ལྟས་བསྟན་པའི་ཕྱིར་འོད་བསྟན་པ་མཛད་པར་རིག་པར་བྱའོ། །
--- END BLOCKS ---
