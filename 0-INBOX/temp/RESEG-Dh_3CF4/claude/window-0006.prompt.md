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
[Block 211]
ཆོ་ག་ཤེས་པ་ནི་ངན་ངོན་ཙམ་གྱིས༌[^110]ཆོ་ག་ཤེས་པའོ། །

[Block 212]
བཟའ་བ་དང་བགོ་བ་ལ་སོགས་པའི་རྒྱུས་སོ། །

[Block 213]
སྙིང་རྗེའི་ཡོན་ཏན་ཞེས་བྱ་བ་ནི་གོམས་པས་སོ། །

[Block 214]
འཇིག་རྟེན་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་ནོ། །

[Block 215]
སྐྱེ་བོ་ནི་དེ་ན་གནས་པའི་སྐྱེ་བོ་ལ་བརྗོད་དོ། །

[Block 216]
མ་འདྲིས་པ་ནི་ཡོངས་སུ་འདྲིས་པར་མ་གྱུར་པའོ། །

[Block 217]
འང་གི་སྒྲ་ནི་སྲིད་པའི་དོན་ནོ། །

[Block 218]
ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་སྐྱེ་བོ་ལ་བྱམས་པར་གྱུར་པ་དེ་བཞིན་དུ་མ་འདྲིས་པའི་སྐྱེ་བོ་དང༌[^111]བྱང་ཆུབ་སེམས་དཔའ་དེ་ལ་བྱམས་པར་གྱུར་ཏོ། །

[Block 219]
འདོད་པ་ཆུང་བ་ནི་ཡོངས་སུ་བཟུང་བ་ལ་རྒྱབ་ཀྱིས་ཕྱོགས་པ་ཡིན་ཏེ། ཆོག་ཤེས་པའོ། །

[Block 220]
ངན་གཡོ་ཞེས་བྱ་བ་ནི་རྙེད་པ་དང་བཀུར་སྟིའི་ཆེད་དུ་སྤྱོད་ལམ་འཆོས་པའོ། །

[Block 221]
མི་ཤེས་པ་ནི་མངོན་པར་མི་ཤེས་པའོ། །

[Block 222]
ཆགས་པ་ནི། རྙེད་པ་དང་། གྲགས་པ་དང་། བདེ་བ་དག་ལའོ། །

[Block 223]
འདིས་ནི་ཆགས་པ་མེད་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 224]
དེ་ནི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 225]
ལྷ་རྣམས་ཀྱི་ཡིད་ཀྱང་མགུ་བར་གྱུར་པས་དང་ཞིང་གུས་པ་ལ་རབ་ཏུ་གཞོལ་བ་ནི་རྗེས་སུ་མཐུན་པའོ། །

[Block 226]
བྱེད་པ་ནི་བྱེད་པ་དང་ལྡན་པའོ། །

[Block 227]
དེ་ནི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 228]
རབ་ཏུ་བྱུང་བ་ནི་རྟགས༌[^112]དང་ལྡན་པར་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 229]
མིས་ཞེས་བྱ་བ་ནི་སྐྱེ་བོས་སོ། །

[Block 230]
ཐོས་ཏེ༌[^113]ཞེས་བྱ་བ་ནི་རྣ་བའི་དབང་པོ་གཏད་པ་ལས་སོ། །

[Block 231]
དེ་ནས་ཞེས་བྱ་བ་ནི་དེ་མ་ཐག་ཏུའོ། །

[Block 232]
ཡོན་ཏན་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། དེས་པ་ལ་སོགས་པའོ། །

[Block 233]
སེམས་དྲངས་ནས་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་འཛིན་པར་བྱེད་པ་སེམས་ཡིན་པས་སོ། །

[Block 234]
རྣམ་སྤངས་ཏེ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་དོར་བའོ། །

[Block 235]
དེ་གང་ཡིན་ཞེ་ན། གཉེན་དང་ཡོངས་སུ་བཟུང་བ་སྟེ། གཉེན་ནི་ཕ་དང་མ་དང་འབྲེལ་པའོ། །

[Block 236]
ཡོངས་སུ་བཟུང་བ་ནི། དབྱིག་དང་། གསེར་དང་། གླང་པོ་ཆེ་ལ་སོགས་པའོ། །

[Block 237]
དེའི་སློབ་མ་ཞེས་བྱ་བ་ནི། བྱང་ཆུབ་སེམས་དཔའ་དེའི་སློབ་མར་ཉེ་བར་ཁས་བླངས་པའོ། །ཇི་ལྟར་ཞེ་ན། འདི་ལྟར་དངོས་གྲུབ་གྲུབ༌[^114]པ་ལྟ་བུར་རོ། །

[Block 238]
ཡང་ན་དེའི་སློབ་མ་ནི། དངོས་གྲུབ་བཞིན་དུ་སྟེ་བྱ་བ་རྣམས་གྲུབ་པ་བཞིན་དུའོ། །

[Block 239]
གྱུར་པ་ནི་ཐོབ་པའོ། །

[Block 240]
ཚུལ་ཁྲིམས་ནི་སོ་སོ༌[^115]ཐར་པའི་སྡོམ་པའོ། །

[Block 241]
གཙང་བ་བསླབ་པའི་གཞི་ཡང་དག་པར་བསྲུང་བ༌[^116]ལ་སོགས་པའོ། །

[Block 242]
དབང་པོ་དུལ་བ་ནི་དང་པ་ལ་སོགས་པ་ཡོངས་སུ་གཟུང༌[^117]ངོ་། །བསྒོམ་པ༌[^118]ནི་གོམས་པའི་སྦྱོར་བས་སོ། །

[Block 243]
དྲན་པ་ཞེས་སྨོས་པས་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་གཟུང་ངོ་། །མ་ཉམས་པ་ནི་དྲན་པ་མངོན༌[^119]དུ་འགྲོ་བས་དྲན་པ་ཉེ་བར་གནས་པའོ། །

[Block 244]
རབ་ཏུ་དབེན་པ་ནི་རབ་ཏུ་དབེན་པར་བྱས་པ་སྟེ། ལུས་ངག་ཡིད་གསུམ་རྣམས་དབེན་པར་གནས་པས་སོ། །

[Block 245]
བྱམས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པས་ནི་སྙིང་རྗེ་དང་། དགའ་བ་དང་། བཏང་སྙོམས་གཟུང༌[^120]ངོ་། །ཡིད་ནི་སེམས་སོ། །

[Block 246]
ཏིང་ངེ་འཛིན་ནི་བསམ་གཏན་ནོ། །

[Block 247]
ཅི་ནུས་ཞེས༌[^121]བྱ་བ་ནི་གང་གང་ལ་ཅི་ནུས་པ་སྟེ་ཇི་ལྟར་ནུས་པའོ། །

[Block 248]
དང་པོ་ཚུལ་ཁྲིམས་ལ་གཞག་པར་སྟོན་ཏོ། །

[Block 249]
ཚུལ་ཁྲིམས་ལ་གནས་ནས་དབང་པོའི་སྒོ་སྡོམ་པའོ། །

[Block 250]
དེ་ལ་སོགས་པའི་རིམ་པ་ཇི་ལྟར་འཚམ་བ་བཞིན་དུ་ཅི་ནུས་པ་སྟེ། སྟོབས་ཇི་ལྟ་བ་བཞིན་དུ་རྗེས་སུ་སྟོན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
