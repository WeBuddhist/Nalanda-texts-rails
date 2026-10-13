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
[Block 1 [HEADING]]
## ༄༅། །གསང་བ་འདུས་པའི་མངོན་པར་རྟོགས་པའི་རྒྱན་གྱི་འགྲེལ་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ས་མཱ་ཛཿཨ་བྷི་ས་མ་ཡ་ཨཱ་ལངྐ་ར་བྲྀཏྟི། བོད་སྐད་དུ། གསང་བ་འདུས་པའི་མངོན་པར་རྟོགས་པའི་རྒྱན་གྱི་འགྲེལ་པ།

[Block 4 [VERSE]]
བཅོམ་ལྡན་འདས་རྡོ་རྗེ་སེམས་དཔའ་ལ་ཕྱག་འཚལ་ལོ། །
གང་ཞིག་མུན་འདྲས་གཏིབས་ཤིང་ཡང་དག་སྒྲོན་མ་མེད། །

[Block 5]
དེ་ཡི་སྒྲོན་མ་བྱ་ཕྱིར་རྟག་ཏུ་དགའ་བའི་མཆོག་སྐྱེས་ནས། །

[Block 6 [VERSE]]
བཅོམ་ལྡན་རྡོ་རྗེ་སེམས་དཔའ་དེ་ལ་རབ་བཏུད་དེ། །
མངོན་པར་རྟོགས་པའི་དོན་ནི་ཟླ་བ༌[^1]གྲགས་པས་བཤད། །

[Block 7 [HEADING]]
## ལམ་དང་འབྲས་བུའི་ས་བཅད། ^II-0

[Block 8]
གསང་སྔགས་ཐམས་ཅད་ནི་བསྡུ་ན་རྣམ་པ་གཉིས་ཏེ། དེ་བས་ན་དེ་བསྟན་པའི་ཕྱིར་ལམ་དང་འབྲས་བུར་བཅས་པའོ་ཞེས༌[^2]ལམ་དང་འབྲས་བུ་དག་ནི་གཉིས་ཁོ་ནའོ། །

[Block 9]
འོ་ན་རྣལ་འབྱོར་གྱི་མཚན་ཉིད་དང་གསུམ་དུ་མི་འགྱུར་རམ་ཞེ་ན། མི་འགྱུར་ཏེ། འདི་ལྟར་ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་ནི་ས་བོན་ཐོབ་པར་བྱེད་པས་ཐབས་སུ་བསྡུའོ། །

[Block 10]
ལམ་དང་འབྲས་བུ་ཞེས་བྱ་བ་འདི་ཡང་གང་ཡིན་དེ་ཉིད་མི་ཤེས་སོ་ཞེ་ན། འདི་ལྟར་རྟེན་དུ་གྱུར་པས་ན་ལམ་སྟེ། གང་ལ་གང་གིས་བརྟེན་པར་བྱ་བས་ལམ་སྟེ། ཤེས་རབ་དང་ཏིང་ངེ་འཛིན་ནོ། །ཤེས་རབ་ནི་སྨིན་པ་དང་གྲོལ་བའི་ལམ་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་པའོ། །ཤེས་རབ་ཀྱིས་རབ་ཏུ་རྣམ་པར་ཕྱེ་བ་དེ་ལ་རྩེ་གཅིག་པ་ནི་ཏིང་ངེ་འཛིན་ནོ། །

[Block 11]
འབྲས་བུ་ཞེས་བྱ་བ་ནི་སྐུ་གསུམ་ལ་སོགས་པའོ། །

[Block 12]
ལམ་ཞེས་བྱ་བ་ཡང་དུ་ཞིག་ཅེ་ན། དེ་བཤད་པ། ལམ་ནི་གཉིས་སུ་ཤེས་བྱ་སྟེ། །ཞེས་པ་ལམ་ཡང་ཡིན་གཉིས་ཀྱང་ཡིན་པས༌[^3]གཉིས་ཏེ། འདི་ལ་གཉིས་ཡོད་པས་ལམ་གཉིས་སོ། །

[Block 13]
དེ་ཡང་འདི་ལྟར་ཞུགས་པ་ཉིད་དང་། བརྟེན་པ་ཉིད་དང་། བདེ་བ་ཉིད་དང་། སྡུག་བསྔལ་སྤངས་པ་ཉིད་དང་། གཅིག་དང་གསུམ་གྱི་སྦྱོར་བ་སྤངས་པ་ཉིད་དང་། ཐོབ་པར་བྱེད་པ་དང་། སྤོང་བར་བྱེད་པ་ཉིད་ཀྱི་ཡང་ཕྱིར་རོ། །

[Block 14]
གཉིས་པོ་དེ་ཡང་གང་ཞེ་ན། སྨིན་པ་དང་ནི་གྲོལ་བའོ། །ཞེས་པ་གང་གིས་སྨིན་པ་སྟེ་རྒྱུད་འོས་སུ་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་སྨིན་པའི་ལམ་མོ། །

[Block 15]
གྲོལ་བའི་ལམ་ནི་གང་གིས་སྡུག་བསྔལ་གྱི་ཕུང་པོ་ལས་རྣམ་པར་གྲོལ་བར་བྱེད་པ་ཉིད་དོ། །

[Block 16 [HEADING]]
## སྨིན་པར་བྱེད་པ། ^1-0

[Block 17]
སྨིན་པར་བྱེད་པ་ཡང་གང་ཞིག་ཅེ་ན། སྨིན་པར་བྱེད་པ་ཞེས་བྱ་བ་ནི་གཉིས་ཏེ་འདི་ལ་གཉིས་ཡོད་པས་འདི་ནི་གཉིས་སོ། །

[Block 18]
གཉིས་པོ་ཡང་གང༌[^4]ཞེ་ན། དངོས་དང་དེ་ཡི་གྲོགས་སུ་འདོད། །ཅེས་པ་གང་སྨིན་པར་བྱེད་པ་ནི་གཉིས་ཏེ། སྨིན་པར་བྱེད་པ་དངོས་དང་། དེའི་གྲོགས་སྤྱོད་པའོ། །

[Block 19]
དེ་ལ་སྨིན་པར་བྱེད་པ་དངོས་ནི་གཙོ་བོའོ། །

[Block 20]
དེ་ལ་ཕན་པར་བྱེད་པ་ནི་དེའི་གྲོགས་སོ། །

[Block 21]
དངོས་ཞེས་བྱ་བའང་དུ་ཞིག་ཅེ་ན། སྨིན་པ༌[^5]དངོས་ནི་རྣམ་པ་བཞི་སྟེ་ཞེས་པ་འདི་ལ་བཞི་ཡོད་པས་འདི་ནི་རྣམ་པ་བཞིའོ། །

[Block 22]
བཞི་པོ་ཉིད་གང་ཡིན་ཞེ་ན།

[Block 23 [VERSE]]
བུམ་པ་དང་ནི་གསང་བ་དང་། །
ཤེས་རབ་ཡེ་ཤེས༌[^6]བཞི་པའོ། །

[Block 24]
ཞེས་པ་བུམ་པ་ནི་བུམ་པའི་དབང་ངོ་། །དེ་བཞིན་ཀུན་ལ་རང༌[^7]དབང་ཞེས་སྦྱར་རོ། །

[Block 25]
དེ་ལྟར་བཞི་ཡོད་པ་ཉིད་ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་གནས་གསུམ་འབྲས་བུ་དང་བཅས་པའམ་ཡང་ན་དུས་ལ་སོགས་པ་བཞི་ཉིད་ཀྱི་ཡང་ཕྱིར་རོ།[^8] །དེ་ལ་བུམ་པའི་དབང་ལ་ཡང་དུ་ཡོད་ཅེ་ན། །

[Block 26 [VERSE]]
དེ་ལ་བུམ་པའི་དབང་ལའང་། །
རྣམ་པར་དབྱེ་བ་སུམ་ཅུ་སྟེ། །

[Block 27]
ཞེས་པ་ནི་འདི་ལ་སུམ་ཅུ་ཡོད་པས་སུམ་ཅུའོ། །

[Block 28]
བུམ་པའི་དབང་ཡང་ཡིན་ལ་སུམ་ཅུའང་ཡིན་པས་སུམ་ཅུ་སྟེ། ཅི་སྲིད་དུ་བུམ་པ་ལ་ཡོད་པ་དེ་སྲིད་དུ༌[^9]གསང་བ་དང་ཤེས་རབ་ཡེ་ཤེས་ལའང་སྦྱར་རོ། །

[Block 29]
དེ་ཉིད་གང་དང་གང་ཞེ་ན་ཞེས་འདྲི་ན། ལན་དུ། ངོ་བོ་ཉིད་དང་རྣམ་དབྱེ་དང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དང་པོར་ལས་དང་པོ་པའི་གང་ཟག་ཁ་ཅིག་ངོ་བོ་མེད་པ་དང་མ་ཡིན་པ་དང་། ཐེ་ཚོམ་ཟ་སྟེ། འདི་ལྟར་འདི་ལ་ནི་ངོ་བོ་མེད་དོ་སྙམ་པ་དང་། འདི་ནི་ངོ་བོ་ཡོད་ཀྱང་འདིའི་ངོ་བོ་མ་ཡིན་སྙམ་པ་དང་། འདི་ལ་ངོ་བོ་ཡོད་པ་ཡིན་ནམ་མ་ཡིན་སྙམ་པ་དེའི་གཉེན་པོ་ལ་ངོ་བོ་སྨོས་སོ། །

[Block 30]
དེ་ལྟར་ངོ་བོ་ཡོད་ཀྱང་ངེས་པ་མ་སྐྱེས་པའི་གཉེན་པོར་ངེས་པའི་ཚིག་བསྙད་དོ། །

[Block 31]
དེའང་འདི་ཁོ་ན་ཡིན་གྱི་གཞན་མ་ཡིན་སྙམ་པའི་གཉེན་པོར་དབྱེ་བ་བསྙད་དོ། །

[Block 32]
འདི་དག་ནི་ཐ་དད་པ་ཡིན་ནོ་སྙམ་པའི་གཉེན་པོར་རྣམ་གྲངས་བསྙད་དོ། །

[Block 33]
རྣམ་པ་གཞན་དུ་ཐལ་བའི་གཉེན་པོར་ཆོས་དུ་དང་ལྡན་པ་བསྙད་དོ། །

[Block 34]
གཞན་དུ༌[^10]ཐལ་བའི་གཉེན་པོར་གཞན་སེལ་བ་བསྙད་དོ། །

[Block 35]
རྒྱུ་མེད་སྙམ་པའི་གཉེན་པོར་རྒྱུ་བསྙད་དོ། །

[Block 36]
སྔོན་གྱི་དུས་ན་བུམ་པ་དང་བུམ་པའི་འབྲས་བུ་མེད་དོ༌[^11]སྙམ་པའི་གཉེན་པོར་གླེང་གཞི་བསྙད་དོ། །

[Block 37]
གང་དུ་བྱ་བའི་ས་མི་ཤེས་པའི༌[^12]གཉེན༌[^13]པོར་གནས་བསྙད་དོ། །

[Block 38]
དུས་ཅི་ཙམ་ན་བྱ་བ་མི་ཤེས་པའི་གཉེན་པོར་དུས་བསྙད་དོ། །

[Block 39]
གང་ཟག་གང་གིས་བྱ་བ་མི་ཤེས་པའི་གཉེན་པོར་སློབ་དཔོན་བསྙད་དོ། །

[Block 40]
དེས་གང་ལ་བྱ་བ་མི་ཤེས་པའི་གཉེན་པོར་སློབ་མ་བསྙད་དོ། །
--- END BLOCKS ---
