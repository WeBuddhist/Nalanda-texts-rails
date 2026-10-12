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
[Block 246]
དེ་ནས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ་ཤེས་པར་བྱ་བ་ཡིན་པར་བསྟན་པའི་ཕྱིར།

[Block 247 [VERSE]]
དེ་བས་བླ་མའི་བཀའ་དྲིན་གྱིས། །
འབད་དེ་རྣམ་པར་ཤེས་ནས་ནི། །

[Block 248]
ཞེས་པ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ་ནི་དབང་དང་དམ་ཚིག་དང་མི་ལྡན་པ་ལ་གསང་བ་སྟོན་པར་བྱེད་པ་དང་། སློབ་དཔོན་སྨོད་པར་བྱེད་པ་དང་། སློབ་དཔོན་གྱི་གདམས་ངག་རྗེས་སུ་མི་འཛིན་པ་དང་ཉན་ཐོས་ཀྱི་རིགས་ཅན་དང་། རང་སངས་རྒྱས་ཀྱི་རིགས་ཅན་དང་། བྱང་ཆུབ་སེམས་དཔའི་རིགས་ཅན་དང་། རིགས་མ་ངེས་པ་ལ་སོགས་པ་རྣམས་ཀྱིས༌[^133]ནམ་ཡང་རྙེད་པར་མི་འགྱུར་ཞིང་། བླ་མའི་གདམས་ངག་རྗེས་སུ་འཛིན་པར་བྱེད་པ་དང་། དད་པ་དང་དམ་ཚིག་ལ་སོགས་པ་དང་ལྡན་པ་དང་། ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་གྱི་གང་ཟག་རྒྱུའི་རྒྱུད་ཀྱང་ཤེས་པར་བྱའོ། །

[Block 249]
དེ་ནས་གཞན་ལ་ཆོས་བསྟན་པར་འདོད་ནས་བཤད་པའི་དབྱེ་བར་བསྟན་པའི་ཕྱིར། སེམས་ཅན་རྗེས་སུ༌[^134]གཟུང་འདོད་པས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། བླ་མའི་གདམས་ངག་ལ་བརྟེན་ནས། དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པའི་དོན་ཇི་ལྟ་བུ་རྣམ་པར་ཤེས་པའི་གང་ཟག་དེས་མ་འོངས་པའི་སེམས་ཅན་བློ་དམན་པ་རྗེས་སུ་གཟུང་བར་བྱ་བའི་ཕྱིར་བཤད་པའི་རྒྱུད་ཀྱི་རྗེས་སུ་འབྲངས༌[^135]ཏེ་བཤད་པའི་ཕྱིར། དེའི་རྣམ་པར་དབྱེ་བ་ཞེས་བྱ་བ་སྨོས་པའི་ཕྱིར་རོ། །

[Block 250]
འདིས་རྒྱན་བདུན་བཤད་པར་དམ་བཅས་པ་ཡང་ཡིན་ནོ། །

[Block 251 [HEADING]]
## རྒྱན་རྣམ་པ་བདུན། ^1-0

[Block 252]
དེ་ཉིད་ཀྱི་དབྱེ་བ་མདོར་བསྟན་པའི་ཕྱིར། གླེང་བསླང་བ་ཡི་གྲངས་ནི་ལྔ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། གླེང་བསླང་བ༌[^136]ཡང་ཡིན་ལ།

[Block 253]
ལྔ༌[^137]ཡང་ཡིན་པས་གླེང་བསླང་བ༌[^138]ལྔའོ། །རིགས་པ་ཡང་ནི་རྣམ་པ་བཞི། །ཞེས་པ་རིགས་པ་ནི་འཐད་པ་སྟེ། འཐད་པའི་ཆོས་རྣམ་པ་བཞི་ཞེས་པའི་ཐ་ཚིག་གོ། །

[Block 254]
རྒྱས་བཤད་མཐའ་ནི་རྣམ་པ༌[^139]དྲུག །ཅེས་པ་བསྡུས་པའི་བཤད་པ་ནི་མ་ཡིན་གྱི།

[Block 255]
འདིར་རྒྱས་པའི་བཤད་པ་ཁོ་ནའོ། །རྒྱས་པར་བཤད་པ་ཡང་ཡིན་ལ། །

[Block 256]
མཐའ་དྲུག་ཀྱང་ཡིན་པས་འདིར་རྒྱས་བཤད་མཐའ་དྲུག་གོ། །

[Block 257 [VERSE]]
བཤད་པ་ཡང་ནི་རྣམ་པ༌[^140]བཞི། །
ཞེས་པ་བཤད་པ་ནི་བསྟན་པ་སྟེ།
བསྟན་པའི་ཆོས་རྣམ་པ་བཞི་ཞེས་བྱའོ། །
ལྔ་པའི་དབྱེ་བ་རྣམ་པ་གཉིས། །

[Block 258]
ཞེས་པའི་ལྔ་པ་ནི་ལྔ་པ་སྟེ་གྲངས་ཀྱི་ལྔ་པའོ། །

[Block 259]
དེའི་དབྱེ་བ་གཉིས་ནི་ཚོགས་དང་།

[Block 260 [VERSE]]
སློབ་མའི་བྱེ་བྲག་གིས་སོ། །
དྲུག་པའི་དབྱེ་བ་ལྔ་དང་ལྡན། །

[Block 261]
ཞེས་པ་ནི་ཚོགས་ཀྱི་དང་སློབ་མའི་གནས་སྐབས་ཀྱི་དབྱེ་བ་ཡིན་ནོ། །

[Block 262]
བདུན་པའི་དབྱེ་བ་རྣམ་པ་གཉིས་ཏེ། །ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པས་དོན་མཐའ་དག་བདེན་པ་རྣམ་པ་གཉིས་སུ་བསྟན་པའོ། །

[Block 263]
འདི་དག་གིས་ནི་མདོར་བསྡུས་པ་བསྟན་པའོ། །

[Block 264]
རྒྱན་རྣམས་མདོར་བསྡུས་པའོ་ཞེས་བསྟན་པ་འདིས་ནི་རྒྱན་རྒྱས་པར་བསྟན་པ་ནི་མ་ཡིན་ནོ་ཞེས་སོ། །

[Block 265]
རྒྱས་པར་ཡང་གང་ཞིག་ལས་ཤེས་པར་བྱ་ཞེ་ན། བཤད་པའི་རྒྱུད་ཀྱི་རྗེས་འབྲངས༌[^141]ནས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། བཤད་པའི་རྒྱུད་ནི་ལྷ་མོ་བཞིས་ཞུས་པ་ལ་སོགས་པའོ། །

[Block 266]
དེའི་རྗེས་སུ་འབྲངས་ནས་བདག་གིས་བཤད་ཅེས་སྦྱར་རོ། །ཅི་བཤད་ཅེ༌[^142]ན།

[Block 267 [VERSE]]
རྒྱན་ནི་བདུན་པོ་རྣམས་ཀྱི་ནི། །
རིམ་པ་བཞིན་དུ་རེ་རེ་ཡི། །
རྒྱས་པ་དག་ནི་བདག་གིས་བྱ། །

[Block 268]
ཞེས་པ་གླེང་བསླང་བའི་གྲངས་རྒྱས་པ་དང་། རིགས་པ་རྒྱས་པར་བཤད་པ་དང་། མཐའ་དྲུག་རྒྱས་པར་བཤད་པ་ལ་སོགས་པའོ། །

[Block 269]
དེ་ལ་དང་པོ་གླེང་བསླང་བའི་གྲངས་རྒྱས་པར་བཤད་པ་ནི༌[^143]རྣམ་པ་གཉིས་ཏེ། དྲིས་པ་དང་། ལན་དུ་བཅས་པའོ། །

[Block 270]
དྲི་བ་བསྟན་པའི་ཕྱིར་རྒྱུད་འདིའི་མིང་ནི་ཅི་ཞིག་ཡིན། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། མིང་མེད་པ་དང་མིང་མ་ཡིན་པ་དང་། མིང་ལོག་པ་རྣམས༌[^144]བསལ་བར་བྱ་བའི་ཕྱིར། རྒྱུད་འདིའི་མིང་ནི་ཅི་ཞིག་ཡིན་ཞེས་སྨོས་ཏེ། དགོས་པ་མེད་པ་དང་། དགོས་པ་མ་ཡིན་པ་དང་།

[Block 271 [VERSE]]
དགོས་པ་ལོག་པ་བསལ་བའི་ཕྱིར། །
གང་གི་དོན་དུ་འདི་ཉིད་མཛད། །

[Block 272]
ཅེས་དགོས་པ་དྲི༌[^145]བའོ། །

[Block 273]
བྱེད་པ་པོ་མེད་པ་དང་། བྱེད་པ་པོ་མ་ཡིན་པ་དང་། བྱེད་པ་པོ་ལོག་པ་བསལ་བའི་དོན་དུ། སུ་ཞིག་བྱེད་པ་པོ་ཞེས་འདྲི་བའོ། །

[Block 274]
ཚད་མེད་པ་དང་། མ་ཡིན་པ་ལ་སོགས་པ་བསལ་བའི་ཕྱིར། འདིའི་ཚད་གང་ཞེས་ཚད༌[^146]འདྲི་བའོ། །

[Block 275]
དེ་ཉིད་བཤད་པ་དང་པོའི་ལན་དུ་བསྟན་པའི་ཕྱིར། རྒྱུད་ཀྱི་མཚན་ནི་མིང་ཡིན་ལ། །ཞེས་སྨོས་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་དང་གསུང་དང་ཐུགས་གསང་བ་འདུས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 276]
དེ་བཞིན་གཤེགས་པའི་རྒྱུད་ཀྱི་མིང་ཇི་སྙེད་པའོ། །

[Block 277]
དེ་བས་ན་གང་ལ་དེ་དག་གི་རྟགས་སུ་འབྲེལ་ཏེ། འདིའི་མིང་གང་ཞིག་ཡིན་ཞེ་ན། གསང་བ་འདུས་པ་ཞེས་བྱ་བ་འདི་ཉིད་ཡིན་ཞེས་སྦྱར་རོ། །

[Block 278]
གསང་བ་འདུས་པ་འདི༌[^147]གང་གི༌[^148]དོན་དུ་མཛད་ཅེས་པའི་ལན་དུ། སྐྱེ་བོ་འདོད༌[^149]ཅན་དོན་དུ་མཛད། །ཅེས་སྦྱར་ཏེ། གོང་དུ་བཤད་པ་ཉིད་དང་འོག་ནས་ཀྱང་ལེགས་པར་སྟོན་པ་ཉིད་ཀྱི་ཕྱིར་མ་བཤད་དོ། །

[Block 279]
འདིའི་བྱེད་པ་པོ་གང་ཞིག་ཡིན་ཞེས་པའི་ལན་དུ། འདིའི་དོན་བྱེད་པ༌[^150]པོ་རྡོ་རྗེ་སེམས་དཔའ༌[^151]ཞེས་སྨོས་ཏེ། གང་གིས༌[^152]གང་ཞིག་བྱེད་པ་དེ་ནི་འདིའི་བྱེད་པ་པོ་ཞེས་སྦྱར་རོ། །

[Block 280]
བྱེད་པ་པོ་ཞེས་པ་ནི་གསུང་བ་པོ་ཞེས་པའོ། །

[Block 281]
གང་ཞིག་ཡིན་ཞེ་ན། རྡོ་རྗེ་སེམས་དཔའ་ཡིན་ཞེས་སྦྱར་རོ། །

[Block 282]
འདི་དག་གིས་ནི་འདི་སྐད་དུ་སྟོན་པར་འགྱུར་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ༌[^153]གསུང་བ་པོ་རྡོ་རྗེ་འཆང་ཡིན་ཞེས་སྦྱར་རོ། །

[Block 283]
འདིའི་ཚད་གང་ཡིན་ཞེས་པའི་ལན་དུ།

[Block 284 [VERSE]]
ཚད་དག་ཀྱང་ནི་བཤད་བྱ་སྟེ། །
ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ།
ལེའུ་དང་དེ་བཞིན་ཆོ་ག་དང་། །

[Block 285]
ཞེས་པ་ལེའུ་བཅུ་བདུན་ཡོད་ཅེས་པ་ནི་ལེའུའི་ཚད་དོ། །
--- END BLOCKS ---
