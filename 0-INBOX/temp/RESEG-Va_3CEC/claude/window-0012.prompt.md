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
[Block 421 [HEADING]]
###### **བདག་འབའ་ཞིག་གི་དོན་ལ་འཇུག་པ།** ^1-1-3-4-1-3-2-1-0

[Block 422]
དེ་ལ་དོན་ཉུང་ཞེས་བྱ་བས་བདག༌[^386]འབའ་ཞིག་གི་དོན་ལ་འཇུག་པ་བསྟན་ཏེ། བདག་ཞི་བར་བྱ་བ་དང་། གྲོལ་བར་བྱ་བ་དང་། མྱ་ངན་ལས་འདས་པར་བྱ་བ་ཙམ་ལས་བྱ་བ་གཞན་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 423 [HEADING]]
###### **གཞན་གྱི་དོན་མི་བྱེད་པ།** ^1-1-3-4-1-3-2-2-0

[Block 424]
བྱེད་པ་ཉུང་ཞེས་བྱ་བས་གཞན་གྱི་དོན་མི་བྱེད་པ་བསྟན་ཏེ། གཞན་ཞི་བར་བྱ་བ་དང་། མྱ་ངན་ལས་འདས་པར་བྱ་བ་ལ་མི་འབད་པར་བྱ་བས༌[^387]སོ། །

[Block 425 [HEADING]]
###### **ཉོན་མོངས་པ་ཆུང་བའི་རིགས།** ^1-1-3-4-1-3-3-0

[Block 426]
ཉོན་མོངས་པ་ཆུང་བའི་རིགས་ཀྱང་རྣམ་པ་གསུམ་སྟེ[^388]། ལུས་དབེན་པ་ལ༌[^389]དགའ་བ་དང་། སེམས་དབེན་པ་ལ་དགའ་བ་དང་། གནས་དབེན་པ་ལ་དགའ་བའོ། །

[Block 427 [HEADING]]
###### **ལུས་དབེན་པ་ལ་དགའ་བ།** ^1-1-3-4-1-3-3-1-0

[Block 428]
འདུ་འཛི་ལ་མི་དགའ་ཞིང་ཞེས་བྱ་བས་ལུས་དབེན་པ་ལ་དགའ་བ༌[^390]བསྟན་ཏེ། རང་བཞིན་གྱིས་འགྲོ་བ་མང་པོར༌[^391]དང་འདྲེ་བར་མ་མོས་ཤིང་བསེ་རུ་བཞིན་དུ་གཅིག་པུར་གནས་པར་མོས་པའི་ཕྱིར་རོ། །

[Block 429 [HEADING]]
###### **སེམས་དབེན་པ་ལ་དགའ་བ།** ^1-1-3-4-1-3-3-2-0

[Block 430]
དབེན་པ་ལ་དགའ་བ་ཞེས་བྱ་བས་སེམས་དབེན་པ་ལ་དགའ་བ་བསྟན་ཏེ། དེ་དག་འདོད་པ་དང་ཁོང་ཁྲོ་བའི་རྣམ་པར་རྟོག་པ་རིང་དུ་སྤོང་བར༌[^392]མོས་པས་སོ། །

[Block 431 [HEADING]]
###### **གནས་དབེན་པ་ལ་དགའ་བ།** ^1-1-3-4-1-3-3-3-0

[Block 432]
རབ་ཏུ་དབེན་པར་གནས་མལ་འཆའ་བ་ཞེས་བྱ་བས་གནས་དབེན་པ་ལ་དགའ་བ་བསྟན་ཏེ།[^393] ཤིང་དྲུང་དང་རི་སུལ་ན་གནས་འཆའ་བའི་ཕྱིར་རོ། །

[Block 433 [HEADING]]
###### རྐྱེན། ^1-1-3-4-2-0

[Block 434]
རྐྱེན་ཀྱང་རྣམ་པ་བཞི་སྟེ། ཡོན་ཏན་དང་། གནས་པ་དང་། རྟོགས་པ་དང་། འབྱུང་བའོ། །

[Block 435 [HEADING]]
###### **ཡོན་ཏན།** ^1-1-3-4-2-1-0

[Block 436]
ཡོན་ཏན་ཡང་རྣམ་པ་གསུམ་སྟེ།[^394] ཉོན་མོངས་པ་ཆུང་ཞིང་དགེ་བ་ཆེ་བ་དང་། རྫུ་འཕྲུལ་ཆེ་བ་དང་། འབྲས་བུའི༌[^395]ས་ལ་མངོན་པར་དགའ་བའོ། །

[Block 437 [HEADING]]
###### **ཉོན་མོངས་པ་ཆུང་ཞིང་དགེ་བ་ཆེ་བ།** ^1-1-3-4-2-1-1-0

[Block 438]
བསྙེན་པར་དཀའ༌[^396]ཞེས་བྱ་བས་ཉོན་མོངས་པ་ཆུང་ཞིང་དགེ་བ་ཆེ་བར༌[^397]བསྟན་ཏེ། མཐུ་དང་གཟི་བརྗིད་དང་བྱིན་རྣམས་ལ་གཞན་གྱིས་ཟིལ་གྱིས་མི་ནོན་ཞིང་དེས་གཞན་ཟིལ་གྱིས་གནོན་པའི་ཕྱིར་རོ། །

[Block 439 [HEADING]]
###### **རྫུ་འཕྲུལ་ཆེ་བ།** ^1-1-3-4-2-1-2-0

[Block 440]
མཐུ་ཆེ་བ་ཞེས་བྱ་བས་རྫུ་འཕྲུལ་ཆེ་བ་བསྟན་ཏེ། སྟོད་ནས་མེ་འབར་བ་དང་། སྨད་ནས་ཆུ་གྲང༌[^398]མོའི་རྒྱུན་འབབ་པ་དང་། གཅིག་ཏུ་གྱུར་ནས་མང་པོར་འགྱུར་བ་དང་། མང་པོར་གྱུར་ནས་གཅིག་ཏུ་འགྱུར་བ་ལ་སོགས་པའི་མཐུ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 441 [HEADING]]
###### **འབྲས་བུའི་ས་ལ་མངོན་པར་དགའ་བ།** ^1-1-3-4-2-1-3-0

[Block 442]
སྦྱིན་པའི་གནས་ཀྱི་ས་ལ་མངོན་པར་དགའ་བ་ཞེས་བྱ་བས་འབྲས་བུའི་ས་ལ་དགའ་བ་བསྟན་ཏེ། སྦྱིན་པའི་གནས་ཀྱིས་ནི་འགྲོ་བ་ཐམས་ཅད་ཀྱི་བསོད་ནམས་ཀྱི་ཞིང་དུ་གྱུར་པའི་དུས་དགྲ་བཅོམ་པའི་འབྲས་བུ་ཐོབ་པ་སྟེ། མངོན་པར་དགའ་བ་ནི་འབྲས་བུ་དེ་ཐོབ་པར་བྱ་བར་སེམས་མོས་པའོ། །

[Block 443 [HEADING]]
###### **གནས་པ།** ^1-1-3-4-2-2-0

[Block 444]
རྒྱུན་མི་འཆད་པར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལ་ལྟ་བ་ཞེས་བྱ་བས༌[^399]གནས་པ་བསྟན་ཏེ། རྒྱུན་མི་འཆད་པ༌[^400]ཞེས་བྱ་བས་ནི་རྟག་ཏུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 445]
རྒྱུ་དང་རྐྱེན་ལ་བརྟེན་ནས་དུས་མཉམ་དུ་འབྲས་བུ་འབྱུང་བ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྟེ། དེ་ཡང་ཕྱི་དང་ནང་གི་རྣམ་པ་གཉིས་སོ། །

[Block 446]
དེ་ལ་ཕྱིའི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ནི་ས་བོན་གྱི་རྐྱེན་གྱིས༌[^401]མྱུ་གུ་ལ་སོགས་པའོ། །

[Block 447]
ནང་གི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ནི་མ་རིག་པའི་རྐྱེན་གྱིས་འདུ་བྱེད་ཅེས་བྱ་བ་ལ་སོགས་བའོ། །

[Block 448]
ལྟ་བ་ནི་ཕྱི་ནང་གི་ཆོས་འདི་རྒྱུ་རྐྱེན་ལས་འབྱུང་བ༌[^402]ཙམ་དུ་ཟད་ཀྱི་བདག་དང་བྱེད་པ་པོ་མེད་པར་རྟོག་པའོ། །

[Block 449 [HEADING]]
###### **རྟོགས་པ།** ^1-1-3-4-2-3-0

[Block 450]
ངེས་པར་འབྱུང་བའི་དབྱིངས་གཅིག་ལ་རྟོག་པ་ཞེས་བྱ་བས་རྟོག་པ་བསྟན་ཏེ། ངེས་པར་འབྱུང་བའི༌[^403]དབྱིངས་ནི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་སོ། །

[Block 451]
མྱ་ངན་ལས༌[^404]འདས་པ་འབའ་ཞིག་ཏུ་གནས་པ་དང་འགྲོ་བར༌[^405]སེམས་པ་ནི་ངེས་པར་འབྱུང་བའི་དབྱིངས་གཅིག་ལ་རྟོག་པ་ཞེས་བྱའོ། །

[Block 452 [HEADING]]
###### **འབྱུང་བ།** ^1-1-3-4-2-4-0

[Block 453]
རང་འབྱུང་གི་ཡེ་ཤེས་ཀྱིས༌[^406]རབ་ཏུ་རྒལ་བ༌[^407]ཞེས་བྱ་བས་འབྱུང་བ་བསྟན་ཏེ། བདག་ཉིད་ཀྱི༌[^408]ཤེས་རབ་དང་ཡེ་ཤེས་ཀྱིས༌[^409]གང་ཟག་ལ་བདག་མེད་པར་རྟོགས༌[^410]ནས་ཉོན་མོངས་པ་སྤངས་ཏེ། ཁམས་གསུམ་ལས་རྒལ༌[^411]བར་གྱུར་པ་ནི་རང་བྱུང༌[^412]གི་ཡེ་ཤེས་ཀྱིས༌[^413]རབ་ཏུ་རྒལ་བ༌[^414]ཞེས་བྱའོ། །

[Block 454 [HEADING]]
###### འབྲས་བུ། ^1-1-3-4-3-0

[Block 455]
འབྲས་བུ་ཐོབ་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཏིང་ངེ་འཛིན་ཐོབ་པ་དང་། མངོན་པར་བྱང་ཆུབ་པ་ཐོབ་པའོ། །

[Block 456 [HEADING]]
###### **ཏིང་ངེ་འཛིན་ཐོབ་པ།** ^1-1-3-4-3-1-0

[Block 457]
ཏིང་ངེ་འཛིན་ཐོབ་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། མི་གཡོ་བ་ཐོབ་པ་དང་། རྒྱུན་དུ་ཡིད་ལ་བྱེད་པ་ཐོབ་པའོ། །

[Block 458 [HEADING]]
###### **མི་གཡོ་བ་ཐོབ་པ།** ^1-1-3-4-3-1-1-0

[Block 459]
དམིགས་པ་ལ་འཇུག་པ་ཐོབ་པ༌[^415]དང་ཞེས་བྱ་བས་མི་གཡོ་བ་ཐོབ་པ་བསྟན་ཏེ། དམིགས་པ་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ལ་སོགས་པ་ཏིང་ངེ་འཛིན་གྱི་ཡུལ་རྣམས་སོ། །

[Block 460]
འདུག་པ་ཐོབ་པ་ནི་ཡུལ་ལ་དམིགས་པའི་ཚེ་སེམས་རྩེ་གཅིག་པ་ལ་གནས་པ་ཐོབ་པ༌[^416]སྟེ། ཕྱི་རོལ་དུ་མི་གཡེང་བར་ནུས་པའོ། །
--- END BLOCKS ---
