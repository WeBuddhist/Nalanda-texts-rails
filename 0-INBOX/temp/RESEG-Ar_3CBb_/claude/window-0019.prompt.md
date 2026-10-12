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
[Block 666 [HEADING]]
### ལེའུ་བཅུ་གཅིག་པ། ^2-11-0

[Block 667]
ལེའུ་བཅུ་གཅིག་པ་ལས་ནི་སྔགས་ཀྱི་སྐུ་བསྐྱེད་པ་དང་ཡེ་ཤེས་ཀྱི་སྐུ་བསྐྱེད་པ་སྟོན་ཏོ་ཞེས་པ་ནི་སྔགས་ཀྱི་སྐུ་བསྐྱེད་པ་ནི་འདིས་བསྐྱེད་པའི་དབང་དུ་གསུངས་སོ། །

[Block 668]
ཡེ་ཤེས་ཀྱི་སྐུ་བསྐྱེད་པ་ནི་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུའི་དབང་དུ་བྱས་པའོ། །

[Block 669]
ཡང་ན་སྔགས་ཀྱི་སྐུ་བསྐྱེད་པ་ནི་བསྐྱེད་པའི་རིམ་པའོ། །

[Block 670]
ཡེ་ཤེས་ཀྱི་སྐུ་བསྐྱེད་པ་ནི་སྒྱུ་མ་ལྟ་བུའི་སྐུའོ། །

[Block 671]
ལེའུ་གང་ལ་སྔགས་ཀྱི་སྐུ་བསྐྱེད་པ་དང་ཡེ་ཤེས་ཀྱི་སྐུ་བསྐྱེད་པ་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 672 [HEADING]]
### ལེའུ་བཅུ་གཉིས་པ། ^2-12-0

[Block 673]
ལེའུ་བཅུ་གཉིས་པ་ལས་ནི་ཕྱག་རྒྱ་ཆེན་པོ་ཡོངས་སུ་གྱུར་པ་ཞེས་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོ་ནི་ཕྱག་རྒྱ་རྣམ་པ་བཞི་དང་ལྡན་པའི་སྐུའོ། །

[Block 674]
དེ་ཐོབ་པའི་ཐབས་གང་ལ་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 675 [HEADING]]
### ལེའུ་བཅུ་གསུམ་པ་དང་བཅུ་བཞི་པ། ^2-13-0

[Block 676]
ལེའུ་བཅུ་གསུམ་པ་དང་བཅུ་བཞི་པ་ལས་ནི་ལས་ཀྱི་ཚོགས་རྣམས་གསུངས་སོ་ཞེས་པ་ནི་ལས་ཀྱི༌[^327]ཚོགས་མང་བ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 677 [HEADING]]
### ལེའུ་བཅོ་ལྔ་པ། ^2-14-0

[Block 678]
ལེའུ་བཅོ་ལྔ་པ་ལས་ནི་དངོས་གྲུབ་ཐམས་ཅད་ནི་དེ་ཁོ་ན་ཉིད་རྟོགས་པ་ཉིད་ཀྱིས་འགྲུབ་པར་འགྱུར་རོ་ཞེས་བསྟན་པའི་ཕྱིར་ཞེས་པས་ནི་དེ་ཉིད་ཀྱི་དགོངས་པ་སྟོན་ཏོ། །

[Block 679]
ཅིའི་ཕྱིར་ཞེ་ན་དེའི་ཕྱིར་ཞེས་པའི་དོན་ཏོ། །

[Block 680]
དེ་བས་ན་དངོས་གྲུབ་ཐམས་ཅད་ནི་ཞེས་པས་ཐོབ་པར་བྱ་བའི་ཡུལ་བསྟན་པའོ། །

[Block 681]
དེ་ཁོ་ན་ཉིད་ཅེས་པ་འདིས༌[^328]ནི་ཐོབ་པར་བྱེད་པའི་ཐབས་བསྟན་ཏོ། །

[Block 682]
ཐབས་ཀྱང་ཅི་ཞིག་ཅེ་ན། སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ཞེས་བྱ་བར་སྦྱར་ཏེ་དེ་གང་ལ་སྟོན་པར་འགྱུར་བའི་ཏིང་ངེ་འཛིན་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 683 [HEADING]]
### ལེའུ་བཅུ་དྲུག་པ། ^2-15-0

[Block 684]
ལེའུ་བཅུ་དྲུག་པ་ལས་ནི་ལེའུ་བཞི་པ་ལས་གསུངས་པའི་རྡུལ་ཚོན་གྱི་དཀྱིལ་འཁོར་སྤྲོས་ནས་སྟོན་ཏོ་ཞེས་པ་ནི་ལེའུ་བཞི་པ་ལས་བཤད་པ་དེ་ཉིད་བཤད་ཀྱི་དེ་ལས་གཞན་པ་ནི་མ་ཡིན་ནོ་ཞེས་པའི་དོན་ཏོ། །

[Block 685]
རྡུལ་ཚོན་གྱི་དཀྱིལ་འཁོར་ཞེས་པ་འདིས་ནི་མ་འབྲེལ་པ་རྣམ་པར་གཅོད་པའོ། །

[Block 686]
[^329]ཡང་ན་ལེའུ་བཞི་པར་ནི་བསྐྱེད་པའི་དཀྱིལ་འཁོར་འབའ་ཞིག་ཉེ་བར་སྟོན་ཏོ། །

[Block 687]
འདིར་ནི་རྡུལ་ཚོན་གྱི་དཀྱིལ་འཁོར་དང་བཅས་ནས་སྟོན་ཏོ། །

[Block 688 [HEADING]]
### ལེའུ་བཅུ་བདུན་པ། ^2-16-0

[Block 689]
ལེའུ་བཅུ་བདུན་པ་ལས་ནི་དམ་ཚིག་དང་སྡོམ་པ་རབ་ཏུ་སྟོན་པ་ཡིན་ནོ་ཞེས་པ་ནི་དམ་ཚིག་དང་སྡོམ་པ་ནི་དམ་ཚིག་དང་སྡོམ་པ་ཉིད་དོ། །

[Block 690]
དེ་གང་ལ་སྟོན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 691]
འདི་དག་གིས་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པའི་དོན་མདོར་བསྡུས་པ་བསྟན་ཏོ། །

[Block 692 [HEADING]]
## བཤད་པ་མདོར་བསྡུས་པ། ^3-0

[Block 693]
དེ་ནས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་བཤད་པ་མདོར་བསྡུས་པ་བསྟན་པའི་ཕྱིར། འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་བྱ་བ་ནས་བྷ་ག་ལ་བཞུགས༌[^330]སོ་ཞེས་པའི་བར་དུ་ནི་བཤད་པའི་ཚུལ་རྣམ་པ་བཞི་དང་ལྡན་པར་བཤད་དོ་ཞེས་པ། ཡི་གེ་དང་། སྤྱི་དང་། སྦས་པ་དང་། མཐར་ཐུག་པ་རྣམ་པ་བཞིར་བསྟན་ཏོ། །

[Block 694]
འདི་སྐད་ཅེས་བྱ་བ་ལ་སོགས་པ་ལ་བཤད་པའི་ཚུལ་རྣམ་པ་བཞིས་བཤད་པ་འདི་ཡང་ཅི་སྒྲའི་འགྲོས་སོ་ཞེ་འམ་ནུས་པ་ཞེས་རྟོག་གྲང་ན། རེ་ཞིག་སྒྲའི་འགྲོས་སོ་ནི་མ་ཡིན་ཏེ། འབྲེལ་པ་ལ་སོགས་པ་ཡི་གེའི་དོན་ལ་ཚང་བའི་ཕྱིར་རོ། །

[Block 695]
ནུས་པ་ཞེས་བྱ་བ་ཡང་སྒྲའི་སྒོ་ནས་སམ་དོན་གྱི་སྒོ་ནས་ཞེས་རྟོག་གྲང་ན། རེ་ཞིག་སྒྲའི་སྒོ་ནས་ནི་མ་ཡིན་ཏེ། འདི་ལྟར་ཐམས་ཅད་ལ་བཤད་པ་བཞི་དང་ལྡན་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 696]
དེ་ལྟ་ན་ཡང་མ༌[^331]ཡིན་ནོ་ཞེ་ན་ཧ་ཅང་ཐལ་བར་འགྱུར་རོ། །

[Block 697]
གལ་ཏེ་དེ་ལྟར་མ་ཡིན་ན་ཡང༌[^332]ཇི་ལྟར་དེར་འགྱུར། དེ་ལྟ་མ་ཡིན་ཞེས་པའི་ངེས་པར་གཟུང་བ་ཡང༌[^333]ཅི་ཞིག་ཡོད། གལ་ཏེ་དོན་གྱི་སྒོ་ནས་མ༌[^334]ཡིན་ནོ་ཞེ་ན་ནི་འདིར་བརྗོད་པའི་སྒོ་ནས་སམ། དེ་ལས་གཞན་ཞིག་ཅེས་རྟོག་གྲང་ན། འདི་ཉིད་ཀྱི་ཡུལ་ནི་མ་ཡིན་ཏེ་སྦས་པ་དང་མཐར་ཐུག་པ་ལ་སོགས་པ་འདིས་མ་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 698]
འོན་ཏེ་བརྗོད་ན་ནི་ཧ་ཅང་དོན་མེད་པར་འགྱུར་རོ། །

[Block 699]
དོན་ཡོད་དོ་ཞེས་པའི་ངེས་པར་གཟུང་བ་ནི་ཅི་ཞིག་ཡོད། རྣམ་པ་གཞན་ཞིག་བརྗོད་པར་གྱུར་ན་ནི་འདི་ཉིད་ཀྱི་བརྗོད་བྱ་མ་ཡིན་པར་འགྱུར་ཏེ། དེ་ལྟ་ན་ནི་འཁྲུལ་པར་ཡང་འགྱུར་རོ། །

[Block 700]
ཇི་སྟེ་མ་འཁྲུལ་ན་ནི་གྲང་བའི་རེག་པས་ཀྱང་ཚ་བའི་རེག་པ་རྟོགས་པར་འགྱུར་རོ། །

[Block 701]
དེ་ལྟ་ན་ནི་དེ་ལས་བྱུང་བའམ། དེའི་བདག་ཉིད་ཀྱི་འབྲེལ་པར་ཡང་འགྱུར་རོ། །

[Block 702]
ཅི་སྟེ་གལ་ཏེ་ན་འབྲེལ་པ་ཡིན་ནོ་ཞེ་ན་ནི་དེ་ཉིད་འགལ་བར་རྣམ་པར་གནས་པར་ཡང་མི་རུང་སྟེ། མེ་དང་དུ་བ་བཞིན་ནོ། །

[Block 703]
ཅི་སྟེ་འགལ་བ་ཡིན་ནོ་ཞེ་ན་ནི། དེ་ལྟ་ན་ནི་འདི་ལ་འདུག་ས་གཅིག་པ་ལ་གནོད་པ་ཅི་ཞིག་ཡོད། །གལ་ཏེ་མི་གནོད་པ་ཅི་ཞིག་ཡོད༌[^335]དོ་ཞེ་ན༌[^336]མངོན་སུམ་དང་འགལ་བར་འགྱུར་རོ། །

[Block 704]
དེ་བས་ན་དོན་གཞན་ནི་བརྗོད་བྱ་མ་ཡིན་ནོ། །

[Block 705]
དོན་གྱི་སྒོ་ནས་ཀྱང་སྒྲ་ལ་བཤད་པར་བྱ་བའི་ཕྱིར་རིགས་པ་མ་ཡིན་ཏེ་གལ་ཏེ་དེ་ལྟ་ན་ནི་དོན་གོང་དུ་གཏན་ལ་དབབ་པར་འགྱུར་རོ། །
--- END BLOCKS ---
