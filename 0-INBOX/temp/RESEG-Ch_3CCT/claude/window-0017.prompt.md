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
ཞེས་པ་ནི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 597]
གཞན་ཡང་དབུགས་ཀྱི་རྒྱུ་བ་འགོག་པ་ཞེས་བྱ་བ་འདི་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 598 [VERSE]]
གང་གི་རྣ་བའི་བུ་ག་ནས། །
དབུགས་རྣམས་རབ་ཏུ་རྒྱུ་འགྱུར་བ། །
དེ་ལ་དམིགས་ཕྱིར་དེ་སྐད་དོ། །

[Block 599]
ཞེས་པ་གང་གིས་སྣའི་རྩེ་མོ༌[^261]ལ་དམིགས་ཏེ་ལུས་ཀྱི་གནས་ནས་རླུང་ཐམས་ཅད་འདུས་ནས། སྣའི་རྩེ་མོ་ལ་འཛིན་པ་འདི་ནི་དབུགས་ཀྱི་འགོག་པའོ། །

[Block 600]
འོ་ན་དབུགས་ཀྱང་ཇི་ལྟ་བུ་དམིགས་ཤེ་ན།

[Block 601 [VERSE]]
དཀར་པོ་ལ་སོགས་རྣམ་པ་ལ། །
ཡི་གེ་དང་བཅས་དེ་ཉིད་དམ། །
སྒྱུ་མ་ཙམ་དུ་དམིགས་པའོ། །

[Block 602]
ཞེས་པ་གང་ཞིག༌[^262]གིས་སྙིང༌[^263]ལ་སོགས་པ་ནས་འོད་ཟེར་ཁ་དོག་སྣ་ལྔ་དང་ཁ་དོག་སྣ་གསུམ་དང་། གཅིག་པ་དང་བསམ་གྱིས་མི་ཁྱབ་པ་ལ་སོགས་པ་གང་གནས་པ་དེ་ལས་དང་པོ་པས་ནི་ཡི་གེའི་ཕྲེང་བ་དང་བཅས་པའོ། །

[Block 603]
ཕྱི་ནས་ནི་ཕྲེང་བ་དང་བྲལ་བའི་འོད་ལ་དམིགས་པའོ། །

[Block 604]
དེ་ནས་འོད་ཀྱང་སྒྱུ་མ་ཙམ་དུ་དམིགས་པའོ། །

[Block 605]
ཕྲེང་བ་དང་བཅས་པ་ཞེས་བྱ་བའང་གང་ཞིག་གིས་ཇི་ལྟར་བཟླས་ཤེ་ན།

[Block 606 [VERSE]]
འབྱུང་བ་ཀཱ་ལིའི་ཕྲེང་བ་སྟེ། །
འཇུག་པ་ཨཱ་ལིའི་ཕྲེང་བ་ཡིན། །
འབྱུང་དང་འཇུག་པ་གང་ཡིན་པ། །
ཨོཾ་དང་ཧཱུཾ་ནི་རྩེ་མོར་འབར། །

[Block 607]
ཞེས་པ་གང་ཞིག་རླུང་འབྱུང་བའི་དུས་སུ་ཁ་དོག་ལྔ་དང་ལྡན་པའི་རླུང་ལ་ཀཱ་ལིའི་ཕྲེང་བ་རྒྱུ་བར་བྱས་ཏེ། དེའི་རྩེ་མོ་ལ་ཧཱུཾ་བསམ་པའམ། ཡང་ན་ངལ་བའི་དབང་དུ་ཨོཾ་བསམ་པའོ། །

[Block 608]
རླུང་འཇུག་པའི་དུས་སུ་འོད་ཟེར་ཁ་དོག་སྣ་ལྔ་ལ་ཨཱ་ལིའི་ཕྲེང་བ་སྟེ། རྩེ་མོ་གོང་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 609 [VERSE]]
དེ་ལའང་དུ་ཡོད་ཅེ་ན། །
སྐུ་དང་ཡི་གེ་ལ་སོགས་པས། །
བཟླས་པ་དུ་མའི་བདག་ཉིད་ཅན། །

[Block 610]
ཞེས་པ་བཟླས་པ་ནི་རིགས་དང་དམིགས་པའི་དབང་དུ་སྣ་ཚོགས་ཤིང་དཔག་ཏུ་མེད་པ་བསྟན་པར་ཤེས་པར་བྱའོ། །

[Block 611]
འོ་ན་རྡོ་རྗེ་བཟླས་པ་ཞེས་བྱ་བ། འདིར་གང་ལ་བརྟེན་ཞེ་ན།

[Block 612 [VERSE]]
གང་གི༌[^264]སྣ་ཡི་སྦྱོར་བ་ལ། །
བརྟེན་ནས་མཁས་པ་རྣམས་ཀྱིས༌[^265]འགྲུབ། །

[Block 613]
ཅེས་པ་དབུགས་ཀྱི་རྒྱུ་བ༌[^266]འགོག་པའི་བཟླས་པ་འདི་ནི་རྣལ་འབྱོར་པས་རང་གི་སྣའི་བུ་ག་ལ་བརྟེན་ནས་འགྲུབ་པར་འགྱུར་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ལམ་ཡིན་པ་ཉིད་དང་། བརྟེན་པར་བྱེད་པ་ཉིད་དང་། དགག་པར་རུང་བ་ཉིད་ཀྱི་ཕྱིར་དེ་སྐད་ཅེས་བྱའོ། །

[Block 614]
འོ་ན་འོག་གི་བཟླས་པ་ཞེས་བྱ་བ་འདི་གང་ཞིག་ཡིན་ཞེ་ན། བཤད་པ།

[Block 615]
རྡོ་རྗེ་རྩེ་ལ་གང་ཞིག་གིས། །དམིགས་པ་འོག་གི་དབང་དུ་གསུངས།

[Block 616]
[^267] །ཞེས་པ་ཐབས་ཀྱི་རྡོ་རྗེ་བྱིན་གྱིས་བརླབས་ཏེ། དེ་ལ་བརྟེན་ནས་འབྱུང་བ་དང་། འཇུག་པ་དང་གནས་པ་ལ་སློབ་པར་བྱེད་དོ། །

[Block 617]
དེའང་ཅིའི་ཕྱིར་ན།

[Block 618 [VERSE]]
འདོད་ཆགས་ཅན་རྣམས་འདུལ་བྱེད་ཕྱིར། །
སྦྱོར་བ་འདི་ནི་བསྟན་པ་ཡིན། །

[Block 619]
ཞེས་པ་སེམས་ཅན་འདོད་ཆགས་ཅན་ཁ་ཅིག་འདོད་པ་ལ་མངོན་པར་ཞེན་པ་དང་། ས་བོན་ལ་ཆགས་པ་དང་། འདུ་བའི་སྟོབས་ཅན་ལ་དེའི་སྦྱོར་བ་བསྟན་པར་བྱའོ། །

[Block 620]
གཞན་ཡང་འདོད་ཆགས་ཅན་ཞེས་བྱ་བ་ནི། འདོད་པའི་ཡོན་ཏན་ལྔ་ལ་ལྷག་པར་ཞེན་ཅིང་ཆགས་པ་སྟེ། དེའི་གཉེན་པོ་ནི་དབང་པོའི་རྒྱུ་བ་འགོག་པའང་ཡིན་པས༌[^268]དེ་དོན་མེད་པར་འགྱུར་རོ་ཞེ་ན་མ་ཡིན་ཏེ།

[Block 621 [VERSE]]
བུད་མེད་བརྟེན༌[^269]ལ་དགའ་བ་རྣམས། །
འདོད་ཆགས་ཅན་ཞེས་ཡང་དག་བཤད། །

[Block 622]
ཅེའོ། །

[Block 623]
འོ་ན་དེ་ལྟ་ན་ནི་བུད་མེད་ལ་མ་བརྟེན་པར་འགྲུབ་པར་མི་འགྱུར་ཞེ་ན་བདེན་ཏེ།

[Block 624 [VERSE]]
གང་ཞིག་མཚན་ལྡན་བུད་མེད་ལ། །
བརྟེན་ནས་བཟླས་པར་བྱ་བ་ཡིན། །

[Block 625]
ཞེས་པ་གང་གིས་རྡོ་རྗེ་དང་། གསང་བའི་རྩའི་ཡི་གེ་ལ་སོགས་པ་ལ་བརྟེན་ནས་འབྱུང་བ་དང་འཇུག་པ་དང་གནས་པ་ལ་བསླབས་ཏེ་གོང་བཞིན་ནོ། །

[Block 626]
དབུ་མ་ལ་བརྟེན་པའི་བཟླས་པ་ཞེས་བྱ་བའང་གང་ཡིན་ཞེ་ན།

[Block 627 [VERSE]]
སྙིང་གི་དབུས་ཀྱི་ས་བོན་ལས། །
གང་ཞིག་འབྱུང་དང་འཇུག་པ་དག །
གཞན་དུ་མི་འཕྲོ་དེ་ཉིད་དུ། །
གསལ་བ་ནང་གི་བཟླས་པ་ཡིན། །

[Block 628]
ཞེས་པ་སྙིང་གི་དབུས་སུ་ས་བོན་བསམས་ཏེ། དེ་ལས་རླུང་འབྱུང་བ་དང་འཇུག་པ་དང་། གནས་པ་ལ་བརྟེན༌[^270]པར་བྱ་ཞིང་བསླབ་པར་བྱའོ། །

[Block 629]
དེ་ཡང་དང་པོ༌[^271]དང་བར་མ་དང་ཐ་མའི་རིམ་པ་ནི་གོང་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 630]
འདི་དག་ལའང་ཅིའི་ཕྱིར། རྡོ་རྗེ་བཟླས་པ་སྙམ་པ་ལ། །རྡོ་རྗེས་བཟླས༌[^272]དང་རྡོ་རྗེར་བཟླས།[^273] །

[Block 631 [VERSE]]
རྡོ་རྗེ་ལ་ནི་དམིགས་པ་དང་། །
རྡོ་རྗེ་ཡིས༌[^274]དང་རྡོ་རྗེའི་ཕྱིར། །

[Block 632]
རྡོ་རྗེ་འབྱུང་དང་རྡོ་རྗེ་སྤོང་།[^275] །རྡོ་རྗེ་འཇོམས་དང་རྡོ་རྗེ་བྲལ། །ཞེས་པ་རྡོ་རྗེ་བཟླས་པ་ནི་འོད་ལྔའི་སྦྱོར་བས་སོ། །

[Block 633]
རྡོ་རྗེར༌[^276]ཞེས་པ་གང་ཡིན་ཞེ་ན།

[Block 634 [VERSE]]
དངོས་པོ་ཐམས་ཅད་རྡོ་རྗེ་ཡི། །
ངོ་བོར་བྱས་ཏེ་ཟློས༌[^277]ཕྱིར་དང་། །

[Block 635]
ཞེས་པ་ནི་གཟུང་བ་དང་འཛིན་པའི་རྣམ་པ་ཐམས་ཅད་རྡོ་རྗེའི་བཟླས་པའི་ངོ་བོར་བྱས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
