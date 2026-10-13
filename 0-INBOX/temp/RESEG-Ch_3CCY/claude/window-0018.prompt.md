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
[Block 631]
དེ་ལ་གལ་ཏེ་དེ་དག་རང་བཞིན་ཡོད་ན་གནས་པ་མེད་པའི་རང་གི་མཚན་ཉིད་དུ་མི་འགྱུར་ཞིང་། འདུ་བྱེད་རྣམས་འཇིག་པ་མེད་པ་ཐོབ་པར་འགྱུར་ལ། ངོ་བོ་ཉིད་གྲུབ་པའི་ཕྱིར་རང་བཞིན་ཡོད་བཞིན་པའོ། །

[Block 632]
ཡོད་བཞིན་པ་མ་ཡིན་པ་ལ་གཞན་དུ་འགྱུར་བ་ཡང་མི་སྲིད་དོ། །

[Block 633]
འོ་མའི་གནས་སྐབས་ཉིད་དུ་གནས་བཞིན་པའི་འོ་མ་གཞན་དུ་གྱུར་པས༌[^503]ཞོའི་དངོས་པོའི་མཚན་ཉིད་དུ་མི་སྲིད་པའམ། གཞོན་ནུ་ཡང་གཞོན་ནུའི་གནས་སྐབས་ཉིད་དུ་གནས་བཞིན་པ་རྒས་པའི་གནས་སྐབས་གཞན་ཐོབ་ནས། འདི་ལས་གཞན་དུ་གྱུར་པར་རྣམ་པར་འཇོག་པར་བྱེད་ལ། དེ་ཡང་མི་རིགས་ཏེ། འདི་གནས་སྐབས་གཞན་ཐོབ་པ་ཅི་ཞིག་ཡོད། གལ་ཏེ་འོ་མ་ལ་ནི་དེ་མི་རུང་སྟེ། འོ་མའི་གནས་སྐབས་དང་འགལ་བའི་ཞོའི་གནས་སྐབས་སུ་དེ་ཇི་ལྟར་འོ་མ་ནི༌[^504]གནས་སྐབས་ཉིད་དུ་གནས་ལ། དེ་མེད་ན་འོ་མའི་རྣམ་པར་གཞག་པ་མེད་པ་ཉིད་དུ་འགྱུར། དེ་ལས་ཀྱང་འོ་མ་དང་ཞོའི་གནས་སྐབས་དག་གཅིག་ཏུ་གྱུར་པ་མེད་པའི་ཕྱིར་འོ་མ་ལ་ཞོའི་དངོས་པོ་མེད་ལ། དངོས་པོ་མེད༌[^505]ན་འདི་ལ་ཞོའི་དངོས་པོ་ག་ལ་ཞིག་ཅེས་བྱའོ། །

[Block 634]
དེ་ལྟར་རང་གི་མཚན་ཉིད་ཁས་བླངས་པར་གྱུར་ན་འདིས་དངོས་པོ་རྣམས་ཡོངས་སུ་འགྱུར་བ་མི་སྲིད་པའི་ཕྱིར་ལ། གཞན་དུ་འགྱུར་བ་མེད་པར་གྱུར་ན་རང་བཞིན་མེད་པར་མི་འགྱུར་རོ། །

[Block 635]
འོ་མ་རང་གི་མཚན་ཉིད་ལས་ཡོངས་སུ་མི་འགྱུར་བའི་དངོས་པོར་གྱུར་ན། ཇི་སྐད་དུ་བསྒྲུབས་པའི་རིགས་པས་བརྟག་པར་ཡོད་པར་ཐལ་ལོ། །

[Block 636]
དངོས་པོ་འབའ་ཞིག་ཙམ་ཁས་བླངས་པར་གྱུར་ན་རང་བཞིན་མེད་པ་མེད་པའི་འཇིག་པ་ཡང་ཐོབ་པར་མི་འགྱུར་བ་ཡང་མ་ཡིན་ཏེ། རང་གི་མཚན་ཉིད་ཡོད་བཞིན་པ་ལ་རང་བཞིན་དུ་རྣམ་པར་གཞག་གི་མེད་པ་ལ་ནི་མ་ཡིན་ཏེ། དངོས་པོ་ཉིད་དུ་རྣམ་པར་གཞག་པ་དེ་དང་འགལ་བ་དངོས་པོ་མེད་པ་མི་འཐད་པས་སོ། །

[Block 637]
དངོས་པོ་ལས་བཟློག་པས་ན་དངོས་པོ་མེད་པ་སྟེ་འཇིག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 638]
རྣམ་པར་འཇིག་པ༌[^506]མེད་པར་འགྱུར་གྱི་རང་བཞིན་ནི་མ་ཡིན་ལ། ཞིག་པ་ཡང་རང་གི་མཚན་ཉིད་ཡོད་བཞིན་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 639]
དེ་ལ་འདི་ལྟར་ཇི་སྐད་དུ་སྨོས་པའི་སྐྱོན་ཡོད་པའི་ཕྱིར་དངོས་པོར་སྨྲ་བར་མི་རིགས་སོ། །

[Block 640]
འདིར་སྨྲས་པ། གལ་ཏེ་ཡང་ཁྱོད་ཀྱིས༌[^507]དངོས་པོར་སྨྲ་བ་བཀག་ཀྱང་དེ་ལྟ་ན༌[^508]དངོས་པོ་མ་བཀག་གོ་ཞེས་བྱ་སྟེ། དེ་ནི་རེ་ཞིག་ཡོད་ལ། གང་དེའི་རང་བཞིན་ལ་དེ་ལས་ཅིག༌[^509]ཤོས་མ་མཐོང་བའི་ཕྱིར་རང་བཞིན་གྱིས༌[^510]རྣམ་པར་གཞག་པ་ཐོབ་པོ། །འདི་ལྟ་སྟེ། མེའི་དངོས་པོ་དེའི་གང་ཞིག་དྲོ་བ་ལ། དེ་ལ་དེ་ལས་གཞན་པ་མ་མཐོང་བའི་ཕྱིར་རང་བཞིན་ཞེས་རྣམ་པར་འཇོག་ལ་དངོས་པོ་འབའ་ཞིག་པ་གྲུབ་པས་རང་བཞིན་གྲུབ་པ་དང་གཞན་གྱི་དངོས་པོ་གྲུབ་པ་དང་དངོས་པོ་མེད་པ་གྲུབ་པར་མི་རུང་པ་མ་ཡིན་ཏེ། འདི་ལྟར་གཤེར་བའི་རང་བཞིན་ཅན་གྱི་ཆུ་རང་བཞིན་གཞན་ལ་ལྟོས་ནས་གཞན་གྱི་དངོས་པོ་ཞེས་རྣམ་པར་འཇོག་ལ། དེ་ཡང་དངོས་པོ་ཞིག་པ་ལ་དངོས་པོ་མེད་པ་ཞེས་རྣམ་པར་འཇོག་སྟེ། དེའི་ཕྱིར་དངོས་པོ་ཡོད་པ་ལས་རང་གི་དངོས་པོ་དང་གཞན་གྱི་དངོས་པོ་དང་དངོས་པོ་མེད་པ་ཡོད་དོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་དངོས་པོ་ཉིད་ཡོད་ན་རང་གི་དངོས་པོ་དང་གཞན་གྱི་དངོས་པོ་དང་དངོས་པོ་མེད་པ་ཡོད་པར་འགྱུར་གྱི། རང་བཞིན་དང་བྲལ་བ་ལ་དངོས་པོ་འཐད་པ་མ་ཡིན་ཏེ། རི་བོང་གི་རྭ་ལ་སོགས་པ་ཡང་དངོས་པོར་ཐལ་བར་འགྱུར་རོ། །

[Block 641]
དེའི་ཕྱིར་མེད་ལ་གང་གི་ཚེ་མེད་པ་དེའི་ཚེ་དེ་ལ།

[Block 642 [HEADING]]
### ཚིགས་བཅད་བཅུ་བདུན་པ། ^1-17-0

[Block 643 [VERSE]]
མེད་ལ་རང་དངོས་གཞན་དངོས་སམ། །
དངོས་མེད༌[^511]འགྱུར་བ་ག་ལ་ཞིག །
དེས་ན་རང་དངོས་གཞན་དངོས་དང་། །
དངོས་མེད་ཕྱིན་ཅི་ལོག་པ་ཡིན། །

[Block 644]
མེད་པ་ནི་ཡོད་བཞིན་པ་མ་ཡིན་པའི་རི་བོང་གི་རྭ་བཞིན་དུ་རང་བཞིན་མེད་ལ། རང་གི་དངོས་པོ་ཉིད་ཀྱང་དངོས་པོ་གཞན་འགའ་ཞིག་ལ་ལྟོས་ནས་གཞན་གྱི་དངོས་པོ་ཞེས་རྣམ་པར་འཇོག་ལ། རང་གི་དངོས་པོ་མེད་ན་གཞན་གྱི་དངོས་པོ་ཡང་མེད་དོ། །

[Block 645]
རང་གི་དངོས་པོ་དང་གཞན་གྱི་དངོས་པོ་དག་མེད་ན་ཡང་སུ་ཞིག་དང་བྲལ་ནས་དངོས་པོ་མེད་པར་འགྱུར། འོ་ན་རང་གི་དངོས་པོ་ལ་སོགས་པ་དག་མེད་ན། འདི་ལྟར་ཁམས་གསུམ་པའི་ཐ་སྙད་རྣམས་ཇི་ལྟར་ཞེ་ན། སྨྲས་པ། ཅི་མི་བདེན་པས་འཇིག་རྟེན་གྱི་ཐ་སྙད་འགེགས་སམ། ཁོ་བོ་འདི་སྐད་དུ་ཡང་སྨྲས་ཏེ།[^512] གང་དེ་ལྟར་དངོས་པོ་ལ་སོགས་པ་དཔྱད་ན་མི་སྲིད་ལ། འཇིག་རྟེན་པ་ཡང་དེས་ཐ་སྙད་བྱེད་ལ། གཞན་གྱི་དངོས་པོ་དང་། རང་གི་དངོས་པོ་དང་། དངོས་པོ་མེད་པ་ཡང་དེས་ན་ཕྱིན་ཅི་ལོག་པ་སྟེ། འཇིག་རྟེན་པའི་ཕྱིན་ཅི་ལོག་ཙམ་ལ་ལྟོས་ནས་གང་ཡང་དེ་དག་གྲུབ་པའི་ཕྱིར་རོ་ཞེས་དགོངས་པའོ། །

[Block 646]
འདིར་སྨྲས་པ།

[Block 647 [HEADING]]
### ཚིགས་བཅད་བཅོ་བརྒྱད་པ། ^1-18-0

[Block 648 [VERSE]]
གལ་ཏེ་དངོས་པོ་སྟོང་གྱུར་ན། །
འགག་པ་མེད་ཅིང་སྐྱེ་མི་འགྱུར། །
གལ་ཏེ་དངོས་པོ་སྟོང་པ་སྟེ། །

[Block 649]
ཡོད་བཞིན་པ་མ་ཡིན་པར་འགྱུར་ན། ཡོད་བཞིན་པ་མ་ཡིན་པའི་ཕྱིར་རི་བོང་གི་རྭ་བཞིན་མི་སྐྱེ་བར་འགྱུར་ཞིང་། འགག་པར་ཡང་མི་འགྱུར་རོ། །

[Block 650]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་དངོས་པོའི་སྐྱེ་བ་དང་འགག་པ་གསུངས་ཏེ། དེའི་ཕྱིར་སྐྱེ་བ་དང་འགག་པ་དང་ལྡན་པའི་ཕྱིར་དངོས་པོ་སྟོང་པ་མ་ཡིན་ནོ། །

[Block 651]
ཡང་ན་འདི་སྙམ་དུ་སེམས་ཏེ། དེ་གྲུབ་ན་རང་བཞིན་ཡོད་པ་ཉིད་ལ། རང་བཞིན་དེ་ཡང་མེད་པ་ལས་སྟོང་པ་ཉིད་དོ་ཞེ་ན། འོ་ན་དེ་ལྟ་བུ་ཡང་།

[Block 652 [VERSE]]
ངོ་བོ་ཉིད་ཀྱིས་སྟོང་ན་ཡང་། །
གང་ལ་འགག་ཅིང་གང་ལ་སྐྱེ། །

[Block 653]
གང་གི་ངོ་བོ་མེད་ན་དེ་ན་རི་བོང་གི་རྭ་ལྟར་འགག་པ་དང་སྐྱེ་བ་ཡང་མི་འབྱུང་ངོ་། །དངོས་པོ་རྣམས་སྐྱེ་བ་དང་འགག་པ་ཡང་ཡོད་པས་འདི་དག་གི་རང་བཞིན་ཡོད་དོ་ཞེས་བྱ་ལ། དེ་གྲུབ་ན་རང་གི་དངོས་པོ་དང་གཞན་གྱི་དངོས་པོ་ཡང་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན། འདིར་སྨྲས་པ། གལ་ཏེ་སྐྱེ་བ་དང་འགག་པར་འགྱུར་ན། དེ་ནི་དེ་དང་ལྡན་པའི་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་གྲུབ་པར་འགྱུར་ལ། དེ་དག་ཀྱང་མེད་དེ། ཇི་ལྟར་བྱས་ན། འདིར་སྐྱེ་བ་དང་འགག་པ་གཉིས་སུ་བརྟག་པ་འདི་ནི། དངོས་པོ་ལ་བརྟེན་ནས་བརྟག་པར་ནུས་ཀྱི་གཞན་དུ་མ་ཡིན་ལ། དེ་དག་དེའི་ཚེ་སྐྱེ་བ་དང་འཇིག་པའི་དངོས་པོར་འཇུག་པར་གྱུར་ན། ཅིག་ཅར་རམ་ཐ་དད་པར་འཇུག་པར་འགྱུར་ན། གཉི་གར་ཡང་འཇུག་པར༌[^513]མི་སྲིད་དོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 654]
[^514]

[Block 655 [HEADING]]
### ཚིགས་བཅད་བཅུ་དགུ་པ། ^1-19-0

[Block 656 [VERSE]]
དངོས་དང་དངོས་མེད་ཅིག་ཅར་མེད། །
དངོས་པོ་མེད་ན་དངོས་མེད་མིན། །
རྟག་པར་དངོས་པོ་དངོས་མེད་ཀྱང་། །
དངོས་མེད་ལས་གཞན་དངོས་མི་སྲིད། །

[Block 657]
སྲིད་པས་ན་དངོས་པོ་སྟེ་སྐྱེའི། [^515]དངོས་པོ་མེད་པ་སྟེ་འཇིག་པའོ། །

[Block 658]
དངོས་པོ་དང་དངོས་པོ་མེད་པ་ནི་དངོས་པོ་དང་དངོས་པོ་མེད་པའོ། །

[Block 659]
དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་མེད་པས་དངོས་པོ་དང་དངོས་པོ་མེད་པའོ།[^516] །རེ་ཞིག་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་ཅིག་ཅར་ཏེ་དུས་གཅིག་ཉིད་དུ་མེད་དེ། ཕན་ཚུན་འགལ༌[^517]བའི་ཕྱིར་མེད་པས་དངོས་པོ་གཅིག་ལ་དུས་གཅིག་ཏུ་སྐྱེ་བ་དང་འཆི་བ་མི་འཐད་དོ་ཞེས་བྱ་སྟེ། དེ་ལྟར་རེ་ཞིག་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་ཅིག་ཅར་མེད་པའོ། །

[Block 660]
ད་ནི་རིམ་གྱིས་ཀྱང་ཡང་དག་པ་ཇི་ལྟ་བར་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་མེད་པས་དེ་བཞིན་དུ་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 661 [VERSE]]
དངོས་པོ་མེད་ན་དངོས་མེད་མིན། །
རྟག་ཏུ་དངོས་པོ་དངོས་མེད་ཀྱང་། །

[Block 662]
ཞེས་བྱ་བ་ལ། གལ་ཏེ་དངོས་པོ་ལས་གཞན་དུ་དངོས་པོ་མེད་པ་འཇུག་ན་དེའི་ཚེ་འཇིག་པ་དང་བྲལ་བའི་ནམ་མཁའ་ལ་སོགས་པ་ལ་ཡང་སྐྱེ་བ་འཇུག་པར་འགྱུར་ཏེ། དེ་ནི་མི་འཇུག་གོ། །

[Block 663]
དེའི་ཕྱིར་དངོས་པོ་མེད་ན་དངོས་པོ་མེད་པ་མ་ཡིན་ནོ། །

[Block 664]
གཞན་ཡང་འདུས་བྱས་ཀྱི་མཚན་ཉིད་མི་རྟག་པའི་ཕྱིར་དངོས་པོའི་མཚན་ཉིད་ལ་དེ་ཡང་ནམ་ཡང་དངོས་པོ་ལས་འཕྲུལ༌[^518]ནས་གང་ལ་འདི་མེད་པ་ཡང་མ་ཡིན་ལ། དེ་ནི་དངོས་པོའི་མཚན་ཉིད་ལས་གྲོལ་བའི་ཕྱིར་ཡོད་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 665]
དངོས་པོའི་མཚན་ཉིད་ལས་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་འདི་ལ་སྐྱེ་བ་ཡང་བཟོད་པ་མ་ཡིན་ཏེ། དེ་ནི་དངོས་པོའི་མཚན་ཉིད་ལས་བཟློག་པའི་ཕྱིར་རོ། །

[Block 666]
དེ་ལྟར་རེ་ཞིག་དངོས་པོ་མེད་ན་དངོས་པོ་མེད་པ་ཡང་མ་ཡིན་ཏེ། ཇི་ལྟར་ཡང་དངོས་པོ་མེད་ན་དངོས་པོ་མེད་པ་ཡང་མི་འཐད་ན། དེ་ལྟར་རྟག་པར་དངོས་པོ་དང་དངོས་པོ་མེད་པ་ཡང་མེད་ན་མེད་དོ་ཞེས་བྱ་བ་འདི་དང་འབྲེལ་ཏོ། །

[Block 667]
དངོས་པོ་དང་དངོས་པོ༌[^519]མེད་པ་ནི༌[^520]དངོས་པོ་ཡོད་པ་དང་དངོས་པོ་མེད་པ་ཞེས་བྱ་སྟེ། མི་རྟག་པ་ལ་བརྗོད་དོ། །

[Block 668]
དངོས་པོ་མེད་པ་དེ་ཡང་རྟག་ཏུ་དངོས་པོ་མེད་ན་མེད་ལ། གལ་ཏེ་ཡོད་ན་སྐྱེ་བ་མེད་པར་ཡང་རྣམ་པར་འཇིག་པར་འགྱུར་རོ། །

[Block 669]
དེ་ལས་ཀྱང་འདུས་མ་བྱས་ཀྱང་འགྱུར་ལ། མ་སྐྱེས་པ་ཡང་འཆི་བར་འགྱུར་རོ། །

[Block 670]
དེ་ནི་འདི་ལྟར་དངོས་པོ་མེད་ན་དངོས་པོ་མེད་པ་ཡང་མེད་ལ། གང་གི་ཚེ་དངོས་པོ་མེད་པ་དག་དེ་ལྟར་དཔྱད་བཞིན་པས་ཅིག་ཅར་རམ་ཐ་དད་པར་གྲུབ་པ་མེད་པས་དེའི་ཚེ་དེ་དག་གི་རང་བཞིན་མ་གྲུབ་ན་དངོས་པོ་འཇུག་པ་མེད་དོ། །
--- END BLOCKS ---
