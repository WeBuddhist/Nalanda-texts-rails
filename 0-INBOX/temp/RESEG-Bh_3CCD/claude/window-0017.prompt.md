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
ཨཱཿའི་དོན་ནི་སྣང་བ་མཐའ་ཡས་སོ། །

[Block 597]
ཡི་གེ་ཧཱུཾ་གི་དོན་ནི་མི་བསྐྱོད་པའོ། །

[Block 598]
སྭཱ་དང་ཧཱ་དག་གི་དོན་ནི་རིན་ཆེན་འབྱུང་ལྡན་དང་དོན་ཡོད་གྲུབ་པའོ། །

[Block 599]
དེ་བཞིན་དུ་གཞན་རྣམས་ཀྱི་བརྗོད་པར་བྱ་བའི༌[^401]དོན་ལ་བརྟེན༌[^402]ཏེ་རང་རང་གི་ལྷའི་བདག་ཉིད་ཀྱི་དོན་བརྟག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 600 [HEADING]]
###### སྔགས་ཀྱི་བརྡ། ^1-2-1-2-3-0

[Block 601]
སྔགས་ཀྱི་བརྡ་ཞེས་བྱ་བ་ནི་སྦྲུལ་དང་མགོ་མེད་དང་མཐའ་མེད་དང་བཏུ་བའོ། །

[Block 602]
དེ་ལ་ཨོཾ་དང་སྭཱ་ཧཱ་ལྡན་པ་ནི་སྦྲུལ་ལོ། །

[Block 603]
ཨོཾ་མེད་ཅིང་སྭཱ་ཧཱ་དང་ལྡན་པ་ནི་མགོ་མེད་དོ། །

[Block 604]
སྭཱ་ཧཱ་མེད་ཅིང་ཨོཾ་དང་ལྡན་པ་ནི་མཐའ་མེད་པའོ།[^403] །

[Block 605]
གཉིས་ཀ་སྤངས་པ་ནི་བཏུས་པའོ། །

[Block 606]
དེ་རྣམས་ཀྱི་དཔེ་ནི་ལེའུ་བཅུ་བཞི་པ་ལས་འཆད་པར་འགྱུར་རོ། །

[Block 607]
དེ་ཡང་ལས་ཀྱི་དབྱེ་བས་བརྡའི་དབྱེ་བ་སྟེ། ཞི་བ་དང་རྒྱས་པ་དང་དབང་དང་དགུག་པ་ལ་སོགས་པ་དག་ཏུ་དགོས་པའི༌[^404]ཕྱིར་རོ། །

[Block 608]
གཞན་ཡང་བརྡ་བཅུ་གཅིག་པོ་ནི་སྤེལ་བ་དང་འདྲེས་པ་དང་ཁ་སྦྱར་ལ་སོགས་པ་རྡོ་རྗེ་གཙུག་ཏོར་གྱི་རྒྱུད་ལས་རྟོགས་པར་བྱའོ། །

[Block 609]
དེ་བཞིན་དུ་ཡང་སྙིང་པོ་དང་། ཉེ་བའི་སྙིང་པོ་དང་། སྙིང་པོ་སྐུལ་བར༌[^405]བྱེད་པ་དང་། རྩ་བའི་སྔགས་དང་། ཕྲེང་བའི་སྔགས་དང་། རིག་སྔགས་དང་། གཟུངས་སྔགས་དང་། ས་བོན་དང་། མིང་གི་ཡི་གེ་དང་པོ་དང་། ཕྱུང་བའི་སྔགས་རྣམས་ནི་ལས་དང་རྗེས་སུ་མཐུན་པར༌[^406]བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་སོ། །

[Block 610]
དེ་ལ་སྙིང་པོ་ནི་བཅོམ་ལྡན་འདས་མངོན་དུ་རྗོད་པར་བྱེད་པའོ། །

[Block 611]
ཉེ་བའི་སྙིང་པོ་ནི་ཡན་ལག་གི་སྒོ་ནས་ཡིན་གྱི་དངོས་སུ་ནི་མ་ཡིན་ནོ། །

[Block 612]
དེ་དག་ནི་འདས་པའི་དུས་དང་ལས་ཀྱི་རབ་འབྱམས་སྒྲུབ༌[^407]ལ་ཤེས་པར་བྱའོ། །

[Block 613]
སྙིང་པོ་བསྐུལ་བ་ནི་ལྷའི་ཐུགས་ཀྱི་ནུས་པ་ནན་ཏན་གྱིས་བཀུག་ལ་བདག་ཉིད་ལ༌[^408]འཇུག་པའོ། །

[Block 614]
རྩ་བའི་སྔགས་ནི་མངོན་པར་འདོད་པའི་ལྷ་མངོན་དུ་བྱེད་པའོ། །

[Block 615]
ཕྲེང་བའི་སྔགས་ནི་མཆོད་པའི་མཐར་ཆུན་འཕྱང་འབུལ་བའོ། །

[Block 616]
རིག་པའི་སྔགས་ནི་ས་འོག་ལ་སོགས་པའི་དངོས་གྲུབ་སྒྲུབ་པའོ། །

[Block 617]
གཟུངས་སྔགས་ནི་རྒྱལ་པོ་ལ་སོགས་པའི་འཇིགས་པ་ཟློག༌[^409]པའོ། །

[Block 618]
ས་བོན་གྱི་སྔགས་ནི་དེ་བཞིན་གཤེགས་པ་དང་ལྷ་མོ་རྣམས་སྐྱེད་པའོ། །

[Block 619]
ཕྱུང་བའི་སྔགས་ནི་གསང་བའི་གནས་སུ་དམ་ཚིག་གི་དཀྱིལ་འཁོར་སྤྲོ་བར་བྱེད་པའོ། །

[Block 620]
མིང་གི་དང་པོའི་ཡི་གེ་རྣམས་ནི་ས་བོན་གྱི་སྔགས་ཀྱི་ཁྱད་པར་རོ། །

[Block 621]
དེ་བས་ན་བརྡའི་སྒོ་ནས་འདོད་པའི་དོན་ཐམས་ཅད་འགྲུབ་པ་ཡིན་ཞེས་སྔགས་ཀྱི་བརྡའོ། །

[Block 622 [HEADING]]
###### སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད། ^1-2-1-2-4-0

[Block 623]
སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་ནི་དེ་བཞིན་ཉིད་དོ། །

[Block 624]
ཆོས་ཐམས་ཅད་ཀྱི་དོན་དམ་པའི་འོད་གསལ་བས་བརྟགས་ཤིང་ཆོས་ཉིད་ཀྱི་མཚན་ཉིད་དོ། །

[Block 625]
གང་གི་ཕྱིར་དེ་ཁོ་ན་ཉིད་ཡོངས་སུ་ཤེས་པ་མེད་པར་ཞི་བ་ལ་སོགས་སྒྲུབ་པ་ལ་སྔགས་ཐམས་ཅད་དོན་དང་ལྡན་པར་མི༌[^410]འགྱུར་རོ། །

[Block 626]
ཇི་སྐད་དུ།

[Block 627 [VERSE]]
ཡི་གེའི་གཟུགས་ཅན་སྔགས་རྣམས་ནི། །
དེ་བས་དམ་པ་རྣམས་མི་འདོད། །
གང་ཕྱིར་རྩྭ༌[^411]མཆོག་ཙམ་ཉིད་ནི། །
འགུགས་པར་བྱེད་པར་མི་ནུས་སོ། །

[Block 628]
ཞེས་འབྱུང་ངོ་། །

[Block 629 [VERSE]]
མཐར་ཐུག་པའི་རིམ་པ་ལས་ཀྱང་། །
སོ་མཆུ་རྐན་དང་ལྕེ་སོགས་ཀྱིས། །
ངག་ནི་བསྐྱོད་པ་དང་ལྡན་པ། །
དེ་ནི་འགྱུར་བ་ཉིད་ཡིན་ཏེ། །

[Block 630]
མི་ཤིགས་པ་ཉིད་ག་ལས་འགྱུར། །ཞེས་པ་དང་། རྒྱུད་ཕྱི་མ་ལས་ཀྱང་སྔགས་ཀྱི་སྒྲ་མན་ཏྲའི་ཚིག་གི་སྒོ་ནས་སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་བསྟན་ཏེ། ཇི་སྐད་དུ།

[Block 631 [VERSE]]
དབང་པོ་དང་ནི་ཡུལ་དག་ལ། །
བརྟེན་ཏེ་ཡིད་ནི་གང་སྐྱེས་པ། །
དེ་ནི་མན་ཞེས་བརྗོད་པ་སྟེ། །
སྐྱོབ་པའི་དོན་གྱིས་ཏྲ་ཞེས་བྱ། །

[Block 632]
ཞེས་སོ། །

[Block 633]
ལུང་བསྟན་པ་ལས་ཀྱང་། །མན་ཏྲ་གསང་བར་བརྗོད་པའི་དོན་ཏོ། །

[Block 634]
དེ་བས་ན་སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་མི་ཤེས་ན་གང་ལས་བྱེད་པ་དེའི་ལས་དེ་རྣམས་འགྲུབ་པར་མི་འགྱུར་ཏེ། ངོ་བོ་ཉིད་ཡོངས་སུ་མི་ཤེས་པའི་ཕྱིར་བྱེ་མ་ལ་མར་བཞིན་ནོ། །

[Block 635]
སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་ཤེས་པའི་རྣལ་འབྱོར་པས་ཞི་བ་ལ་སོགས་པ་འབད་པ་མེད་པར་འགྲུབ་པར་འགྱུར་ཏེ། དེ་རྣམས་ཞར་ལ་འབྱུང་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
