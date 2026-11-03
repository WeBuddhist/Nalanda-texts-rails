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
[Block 4691 [VERSE]]
སངས་རྒྱས་ཀྱི་སྲས་རྣམས་ཚད་མ་ཡིན་ནོ། །
སྟོན་པ་འཇིག་རྟེན་མིག་ནི་ཟུམ་གྱུར་ཅིང་། །
དབང་གྱུར་སྐྱེ་བོ་ཕལ་ཆེར་ཟད་པ་ན། །

[Block 4692]
དེ་ཉིད་མ་མཐོང་རང་དགར་གྱུར་པ་ཡི།[^3328] །

[Block 4693 [VERSE]]
ངན་རྟོག་རྣམས་ཀྱིས་བསྟན་པ་འདི་དཀྲུགས་སོ། །
རང་བྱུང་རང་བྱུང་བསྟན་པ་གཅེས་འཛིན་རྣམས། །
མཆོག་ཏུ་ཞིར་གཤེགས་འགྲོ་མགོན་མེད་པ་ན། །
འདོམས་མེད་ཡོན་ཏན་འཇོམས་པར་བྱེད་པ་ཡི། །

[Block 4694 [VERSE]]
དྲི་མས་དགའ་མགུར་དེང་སང་འདི་ན་སྤྱོད། །
དེ་ལྟར་ཐུབ་པ་དག་གི༌[^3329]བསྟན་པ་ནི། །
ལྐོག་མར་སྲོག་ཕྱིན་འདྲ་དང་དྲི་མ་རྣམས། །
སྟོབས་དང་ལྡན་པའི་དུས་སུ་རིག་ནས་ནི། །

[Block 4695]
ཐར་པ་འདོད་པ་དག་གིས་བག་ཡོད་གྱིས། །ཆོས་མངོན་པའི་མཛོད་ཀྱི་བཤད་པ་ལས་སྙོམས་པར་འཇུག་པ་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་བརྒྱད་པའོ།། །།

[Block 4696]
[^3330]

[Block 4697 [HEADING]]
## གང་ཟག་དགག་པ་བསྟན་པ། ^6-0

[Block 4698]
ཡང་ཅི་འདི་ལས་གཞན་ལ་ཐར་པ་ཡོད་དམ་ཞེ་ན། མེད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། བདག་ཏུ་ལྟ་བ་ཕྱིན་ཅི་ལོག་ལ་ཞེན་པ་ཉིད་ཀྱི་ཕྱིར་ཏེ། ཕུང་པོའི་རྒྱུད་ཁོ་ན་ལ་བདག་ཏུ་འདོགས་པ༌[^3331]ནི་ངེས་པར་མི་འཛིན་ཏོ། །

[Block 4699]
འོ་ན་ཅི་ཞེ་ན། རྫས་གཞན་ཁོ་ན་ལ་བདག་ཏུ་ཡོངས་སུ་རྟོགས་པར་བྱེད་ལ། ཉོན་མོངས་པ་རྣམས་ནི་བདག་ཏུ་འཛིན་པ་ལས་རབ་ཏུ་སྐྱེ་བ་ཡིན་ནོ། །

[Block 4700 [HEADING]]
### བདག་ཏུ་མངོན་པར་བརྗོད་པ་ཕུང་པོའི་རྒྱུད་ཁོ་ན་ལ་འཇུག་པ། ^6-1-0

[Block 4701]
བདག་ཏུ་མངོན་པར་བརྗོད་པ་འདི་ནི་ཕུང་པོའི༌[^3332]རྒྱུད་ཁོ་ན་ལ་འཇུག་གི །བརྗོད་པར་བྱ་བ་གཞན་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ཇི་ལྟར་ཁོང་དུ་ཆུད་ཅེ་ན། མངོན་སུམ་དང་། རྗེས་སུ་དཔག་པ་མེད་པའི་ཕྱིར་ཏེ། ཆོས་གང་དག་ཡོད་པ་དེ་དག་ནི་བར༌[^3333]ཆད་བྱེད་པ་མེད་ན་མངོན་སུམ་དུ་དམིགས་པ་ཡིན་ཏེ། དཔེར་ན་ཡུལ་དྲུག་དང་ཡིད་ལྟ་བུའོ། །

[Block 4702]
ཡང་ན་རྗེས་སུ་དཔག་པས་དམིགས་པ་ཡིན་ཏེ། དཔེར་ན་དབང་པོ༌[^3334]ལྟ་བུའོ། །

[Block 4703]
དེ་ལ་འདི་ནི་རྗེས་སུ་དཔག་པ་ཡིན་ཏེ། རྒྱུ་ཡོད་ཀྱང་རྒྱུ་གཞན་མེད་ན་འབྲས་བུ་མེད་པར་མཐོང་ལ་ཡོད་ན་ནི་ཡང་ཡོད་པར་མཐོང་བ་སྟེ། དཔེར་ན་མྱུ་གུ་ལྟ་བུའོ། །

[Block 4704]
ཡུལ་སྣང་བར་གྱུར་པ་དང་རྒྱུ་ཡིད་ལ་བྱེད་པ་ཡོད་ཀྱང་ཡུལ་འཛིན་པ་མེད་པར་མཐོང་ལ། ཡང་ཡོད་པར་མཐོང་བ་སྟེ། ལོང་བ་དང་འོན་པ་ལ་སོགས་པ༌[^3335]དང་། མ་ལོང་བ་དང་མ་འོན་པ་ལ་སོགས་པ༌[^3336]ལྟ་བུའོ། །

[Block 4705]
དེའི་ཕྱིར་དེ་ལ་ཡང་རྒྱུ་གཞན་མེད་པ་དང་། ཡོད་པར་ངེས་ལ། རྒྱུ་གཞན་གང་ཡིན་པ་དེ་ནི་དབང་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ནི་རྗེས་སུ་དཔག་པ་ཡིན་ནོ། །

[Block 4706]
བདག་ནི་དེ་ལྟར་ཡོད་པ་མ་ཡིན་པས་བདག་མེད་དོ། །

[Block 4707 [HEADING]]
### གནས་མའི་བུ་རྣམས་གང་ཟག་ཡོད་པར་འདོད་པ། ^6-2-0

[Block 4708]
འོ་ན་གང་གནས་མའི་བུ་རྣམས་གང་ཟག་ཡོད་པར་འདོད་པ་ཇི་ལྟ་བུ། འདི་ནི་རེ་ཞིག་དཔྱད་པར་བྱ་བ་ཡིན་ཏེ། ཅི་དེ་དག་རྫས་སུ་འདོད་དམ། འོན་ཏེ་བཏགས་པར་འདོད། རྫས་སུ་ཞེས་བྱ་བ་འདི་ཡང་ཅི་ཡང་ཅི༌[^3337]ཞིག །བཏགས་པར་ཞེས་བྱ་བ་འདི་ཡང་ཅི་ཞིག་ཡིན། གལ་ཏེ་གཟུགས་ལ་སོགས་པ་བཞིན་དུ་དངོས་པོ་གཞན་ཞིག་ཡིན་ནོ་ཞེ་ན་ནི་རྫས་སུ་ཡོད་པ་ཡིན་ནོ། །

[Block 4709]
གལ་ཏེ་འོ་མ་ལ་སོགས་པ་བཞིན་དུ་སྤྱི་ཡིན་ནོ་ཞེ་ན་ནི་བཏགས་པར་ཡོད་པ་ཡིན་ནོ། །

[Block 4710 [HEADING]]
#### རྫས་སུ་ཡོད་པ། ^6-2-1-0

[Block 4711]
དེ་ལས་ཅིར་འགྱུར། རེ་ཞིག་གལ་ཏེ་རྫས་སུ་ཡོད་ན་ནི་དེ་རང་བཞིན་ཐ་དད་པའི་ཕྱིར་ཕུང་པོ་རྣམས་ལས་གཞན་ནོ་ཞེས་བརྗོད་པར་བྱ་སྟེ། ཕན་ཚུན་གྱི་ཕུང་པོ་བཞིན་ནོ། །

[Block 4712]
འདིའི་རྒྱུ་ཡང་བརྗོད་དགོས་སོ། །

[Block 4713]
འོན་ཏེ་འདུས་མ་བྱས་ཡིན་ན་ནི་དེའི་ཕྱིར་མུ་སྟེགས་ཅན་གྱི་ལྟ་བར་ཡང༌[^3338]ཐལ་བར་འགྱུར་ལ། དགོས་པ་མེད་པ་ཉིད་དུ་ཡང་འགྱུར་རོ། །

[Block 4714 [HEADING]]
#### བཏགས་པར་ཡོད་པ། ^6-2-2-0

[Block 4715]
འོན་ཏེ་བཏགས་པར་ཡོད་དོ་ཞེ་ན་ནི་ཁོ་བོ་ཅག་ཀྱང་དེ་སྐད་ཅེས་སྨྲས་སོ།[^3339] །དེ་ནི་རྫས་སུ་ཡོད་པ་ཁོ་ན་ཡང་མ་ཡིན་ལ་བཏགས་པར་ཡོད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 4716 [HEADING]]
#### ཕུང་པོ་རྣམས་རྒྱུར་བྱས་ནས་གང་ཟག་ཏུ་འདོགས་པ། ^6-2-3-0

[Block 4717]
འོ་ན་ཅི་ཞེ་ན། ད་ལྟར་གྱི་ནང་གི་ཟིན་པའི་ཕུང་པོ་རྣམས་རྒྱུར་བྱས་ནས་གང་ཟག་ཏུ་འདོགས་སོ། །

[Block 4718]
ལོང་བ་ལྟ་བུའི་ཚིག་དོན་མི་གསལ་བ་འདི་ནི་མི་གོའོ། །

[Block 4719]
རྒྱུར་བྱས་ནས་ཞེས་བྱ་བ་འདི་ཅི། གལ་ཏེ་འདིའི་དོན་ཕུང་པོ་རྣམས་ལ་དམིགས་ནས་ཞེས་བྱ་བ་འདི་ཡིན་ནོ་ཞེ་ན་ནི། དེ་དག་ཁོ་ན་ལ་གང་ཟག་ཏུ་འདོགས་པར་ཟད་དོ། །

[Block 4720]
[^3340]དཔེར་ན་གཟུགས་ལ་སོགས་པ་ལ་དམིགས་ནས། དེ་དག་ཁོ་ན་ལ་འོ་མ་འདོགས་པ༌[^3341]བཞིན་ནོ། །

[Block 4721]
འོན་ཏེ་འདིའི་དོན་ཕུང་པོ་རྣམས་ལ་བརྟེན་ནས་ཞེས་བྱ་བ་འདི་ཡིན་ནོ་ཞེ་ན་ནི་ཕུང་པོ་རྣམས་གང་ཟག་གདགས་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་སྐྱོན་དེ་ཉིད་དུ་འགྱུར་རོ། །

[Block 4722]
དེ་ནི་དེ་ལྟར་མི་འདོགས་སོ། །

[Block 4723]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། ཇི་ལྟར་བུད་ཤིང་རྒྱུར་བྱས་ནས་མེ་འདོགས་པ་བཞིན་ནོ། །ཇི་ལྟར་ན་བུད་ཤིང་རྒྱུར་བྱས་ནས་མེ་འདོགས་ཤེ་ན། བུད་ཤིང་མེད་པར་མེ་མི་འདོགས་མོད་ཀྱི། བུད་ཤིང་ལས་མེ་གཞན་ཡིན་པར་དམ་བཅའ་བར་ཡང་མི་ནུས་ལ། གཞན་མ་ཡིན་པར་དམ་བཅའ་བར་ཡང་མི་ནུས་ཏེ། གལ་ཏེ་གཞན་ཡིན་ན་ནི་བུད་ཤིང་དྲོ་བ་ཉིད་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 4724]
འོན་ཏེ་གཞན་མ་ཡིན་ན་ནི་བསྲེག་བྱ་ཉིད་སྲེག་བྱེད་ཡིན་པར་འགྱུར་རོ། །

[Block 4725]
དེ་ལྟར་ཕུང་པོ་རྣམས་མེད་པར་ཡང་གང་ཟག་མི་འདོགས་ལ། ཕུང་པོ་རྣམས་ལས་གཞན་ཡིན་པར་དམ་བཅའ་བར་ཡང་མི་ནུས་ཏེ་རྟག་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 4726]
གཞན་མ་ཡིན་པར་ཡང་དམ་བཅའ་བར་མི་ནུས་ཏེ་ཆད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 4727]
རེ་ཞིག་ཀྱེ་བུད་ཤིང་ནི་ཅི། མེ་ནི་ཅི་ཡིན་པ་སྨྲོས་ཤིག་དང་། དེ་ལས་ཇི་ལྟར་ན་བུད་ཤིང་རྒྱུར་བྱས་ནས་མེ་འདོགས་པར་ཤེས་པར་བྱའོ། །

[Block 4728]
འདི་ལ་ཅི་ཞིག་བརྗོད་པར་བྱ། བསྲེག་བྱ་ནི་བུད་ཤིང་ཡིན་ལ་སྲེག་བྱེད་ནི་མེ་ཡིན་པར་ཟད་མོད། འདིར་བསྲེག་པར་བྱ་བ་ནི་ཅི། སྲེག་པར་བྱེད་པ་ནི་ཅི་ཡིན་པ་དེ་ཉིད་བརྗོད་པར་བྱའོ། །

[Block 4729]
རེ་ཞིག་འཇིག་རྟེན་ན༌[^3342]ནི་ཤིང་ལ་སོགས་པ་མ༌[^3343]འབར་བ་ལ་བུད་ཤིང་ཞེས་ཀྱང་བྱ་ལ་བསྲེག་བྱ་ཞེས་ཀྱང་བྱའོ། །

[Block 4730]
འབར་བ་ལ་ནི་མེ་ཞེས་ཀྱང་བྱ་ལ་སྲེག་བྱེད་ཅེས་ཀྱང་བྱ་སྟེ། འབར་བ་དང་ཤིན་ཏུ་ཚ་བ་གང་ཡིན་པ་དེས་དེ་ཚིག་པ་དང་སྲེག་པར་བྱེད་དེ། རྒྱུད་འགྱུར་བར་བྱེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
