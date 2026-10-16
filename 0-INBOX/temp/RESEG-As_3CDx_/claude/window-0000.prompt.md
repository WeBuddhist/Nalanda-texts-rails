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
### ༄༅། །མདོ་སྡེ་དགོངས་པ་ངེས་པར་འགྲེལ་པའི་མདོའི་རྣམ་པར་བཤད་པ།༼སྟོད་ཆ།༽

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ཨཱརྱ་སནྡྷི་ནིར་མོ་ཙ་ནཾ་སཱུ་ཏྲ་སྱ་བྱཱ་ཁྱཱ་ན༌[^1]མ། བོད་སྐད་དུ། འཕགས་པ་དགོངས་པ་ངེས་པར་འགྲེལ་པའི་མདོའི་རྣམ་པར་བཤད་པ། དཀོན་མཆོག་གསུམ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [HEADING]]
## དོན་རྣམ་པ་ལྔ། ^1-0

[Block 5]
འཕགས་པ་དགོངས་པ་ངེས་པར་འགྲེལ་པའི་མདོ་འདི་ནི་མདོར་བསྡུ་ན་དོན་རྣམ་པ་ལྔས་བསྟན་ཏེ། བསྡུས་པའི་དོན་དང་། དགོས་པ་དང་། ཚིག་གི་དོན་དང་། མཚམས་སྦྱར་བ་དང་། བརྒལ་བའི་དོན་ཏོ། །

[Block 6 [HEADING]]
### བསྡུས་པའི་དོན། ^1-1-0

[Block 7]
དེ་ལ་རེ་ཞིག་བསྡུས་པའི་དོན་ནི༌[^2]རྣམ་པ་གཉིས་ཏེ། གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པ༌[^3]དང་། མདོ་སྡེའི་ལུས་རྣམ་པར་གཞག་པའོ། །

[Block 8 [HEADING]]
#### གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པ། ^1-1-1-0

[Block 9]
དེ་ལ་གླེང་གཞིའི༌[^4]ཁྱད་པར་རྣམ་པར་གཞག་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཐུན་མོང་གི་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པ་དང་། ཐུན་མོང་མ་ཡིན་པའི་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པའོ། །

[Block 10 [HEADING]]
##### ཐུན་མོང་གི་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པ། ^1-1-1-1-0

[Block 11]
དེ་ལ་ཐུན་མོང་གི་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པ་ནི་གང་གི་དུས་ན། གང་གིས་བཤད་པའི༌[^5]མདོ་སྡེ་ཐམས་ཅད་ཀྱི་ཐུན་མོང་གི་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པའོ། །

[Block 12]
དེ་ཡང་ཕུན་སུམ་ཚོགས་པ་རྣམ་པ་གཉིས་ཀྱིས་བསྟན་ཏེ། དུས་ཕུན་སུམ་ཚོགས་པ་དང་། སྟོན་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 13 [HEADING]]
###### དུས་ཕུན་སུམ་ཚོགས་པ། ^1-1-1-1-1-0

[Block 14]
དེ་ལ་གང་གི་དུས་ན་བཤད་ཅེ་ན། དུས་ཕུན་སུམ་ཚོགས་པ་ནས་ཏེ།[^6]

[Block 15]
དེ་ནི་མདོ་ལས།

[Block 16]
འདི་སྐད་བདག་གིས་ཐོས་པ་དུས་གཅིག་ན་ཞེས་གསུངས་པས་བསྟན་ཏེ། དེའི་ཕུན་སུམ་ཚོགས་པ་ནི་དེ་བཞིན་གཤེགས་པ་འཇིག་རྟེན་དུ་བྱུང་ཞིང་མདོ་སྡེ་དཀོན་མཆོག་འདི་ལྟ་བུ་དག་མངོན་སུམ་དུ་ཐོས་པའི་སྐབས་ཡོད་པའོ། །

[Block 17 [HEADING]]
###### སྟོན་པ་ཕུན་སུམ་ཚོགས་པ། ^1-1-1-1-2-0

[Block 18]
གང་གིས་བཤད་ཅེ་ན་སྟོན་པ་ཕུན་སུམ་ཚོགས༌[^7]པ་སྟེ།

[Block 19]
དེ་ཡང་མདོ་ལས།

[Block 20]
བཅོམ་ལྡན་འདས་ཞེས་གསུངས་པས་བསྟན་ཏེ། དེའི་ཕུན་སུམ་ཚོགས་པ་ནི་ལེགས་པ་དྲུག་དང་ལྡན་པ་དང་། བདུད་བཞི་བཅོམ་པ་ལ་སོགས་པ་བཅོམ་ལྡན་འདས་ཉིད་ཀྱི་རྒྱུད་ལ་མངའ་བའི་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 21]
དེ་གཉིས་ནི་མདོ་སྡེ་ཐམས་ཅད་ལ་སྤྱིར་འདྲ་བར་བསྟན་པ་ཡིན་པས་ཐུན་མོང༌[^8]གི་གླེང་གཞིའི༌[^9]ཁྱད་པར་རྣམ་པར་གཞག་པ་ཞེས་བྱའོ། །

[Block 22 [HEADING]]
##### ཐུན་མོང་མ་ཡིན་པའི་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པ། ^1-1-1-2-0

[Block 23]
དེ་ལ་ཐུན་མོང་མ་ཡིན་པའི་གླེང་གཞིའི༌[^10]ཁྱད་པར་རྣམ་པར་གཞག་པ་ནི་གང་ན་ཅི་འདྲ་བ་ཞིག་ཇི་ལྟ་བུ་དག་དང་བཞུགས་པའི་རིམ་གྱིས་མདོ་སྡེའི༌[^11]གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པའོ། །

[Block 24]
དེ་ནི་ཕུན་སུམ་ཚོགས་པ་རྣམ་པ་གསུམ་གྱིས་བསྟན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱི༌[^12]གནས་ཕུན་སུམ་ཚོགས་པ་དང་། ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་དང་། འཁོར་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 25 [HEADING]]
###### གནས་ཕུན་སུམ་ཚོགས་པ། ^1-1-1-2-1-0

[Block 26]
དེ་ལ་གང་ལ་བཞུགས་ཤེ་ན། གནས་ཕུན་སུམ་ཚོགས་པ་སྟེ། དེ་ནི་མདོ་ལས་གཞལ་མེད་ཁང་ཆེན་པོ་ཞེས་གསུངས་པས་བསྟན་ཏོ། །

[Block 27]
དེའི་ཕུན་སུམ་ཚོགས་པ་ནི་མདོ་ལས།

[Block 28]
རིན་པོ་ཆེ་སྣ་བདུན་མཆོག་ཏུ་འབར་བ་བཀོད་པ་འཇིག་རྟེན་གྱི་ཁམས་དཔག་ཏུ་མེད་པ་རྒྱས་པར་འགེངས་པའི་འོད་ཟེར་རྒྱ་ཆེན་པོ་རབ་ཏུ་འབྱུང་བ་ཞེས་བྱ་བ་ནས་རིན་པོ་ཆེའི་པདྨའི་རྒྱལ་པོ་ཆེན་པོ་ཡོན་ཏན་མཐའ་ཡས་པས་བརྒྱན་པའི་བཀོད་པ་ལ་བརྟེན་ནས་བཞུགས་ཏེ་ཞེས་གསུངས་པའི་བར་གྱི་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 29 [HEADING]]
###### ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ། ^1-1-1-2-2-0

[Block 30]
ཅི་འདྲ་བ་ཅིག༌[^13]བཞུགས་ཤེ་ན། ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པས་ཏེ། དེ་ནི་མདོ་ལས་བཅོམ་ལྡན་འདས་ཞེས་གསུངས་པས་བསྟན་ཏོ། །

[Block 31]
དེའི་ཕུན་སུམ་ཚོགས་པ་ནི་མདོ་ལས།

[Block 32]
ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནས། ནམ་མཁའི་ཁམས་ཀྱི༌[^14]མཐས་གཏུགས་པ་དེ་ཞེས་གསུངས་པའི་བར་གྱི་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 33 [HEADING]]
###### འཁོར་ཕུན་སུམ་ཚོགས་པ། ^1-1-1-2-3-0

[Block 34]
དེ་ཇི་ལྟ་བུ་དག་དང་བཞུགས་ཤེ་ན། འཁོར་ཕུན་སུམ་ཚོགས་པ་དག་དང་སྟེ། དེ་ལ་འཁོར་ཕུན་སུམ་ཚོགས་པ་ནི་རྣམ་པ་གཉིས་ཏེ། ཉན་ཐོས་ཀྱི་འཁོར་ཕུན་སུམ་ཚོགས་པ་དང་། བྱང་ཆུབ་སེམས་དཔའི་འཁོར་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 35 [HEADING]]
###### **ཉན་ཐོས་ཀྱི་འཁོར་ཕུན་སུམ་ཚོགས་པ།** ^1-1-1-2-3-1-0

[Block 36]
དེ་ལ་ཉན་ཐོས་ཀྱི་འཁོར་ཕུན་སུམ་ཚོགས་པ་ནི་མདོ་ལས།

[Block 37]
ཉན་ཐོས་ཀྱི་དགེ་འདུན་ཚད་མེད་པ་ཐམས་ཅད་ཀྱང་ཅང་ཤེས་པ་ཞེས་གསུངས་པས་བསྟན་ཏོ། །

[Block 38]
དེའི་ཕུན་སུམ་ཚོགས་པ་ནི་མདོ་ལས།

[Block 39]
སངས་རྒྱས་ཀྱི་སྲས་ཞེས་བྱ་བ༌[^15]ནས། དེ་བཞིན་གཤེགས་པའི་བཀའ་ལ་ཤིན་ཏུ་ཞུགས་པ་ཤ་སྟག་ཅེས་གསུངས་པའི་བར་གྱི་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 40 [HEADING]]
###### **བྱང་ཆུབ་སེམས་དཔའི་འཁོར་ཕུན་སུམ་ཚོགས་པ།** ^1-1-1-2-3-2-0
--- END BLOCKS ---
