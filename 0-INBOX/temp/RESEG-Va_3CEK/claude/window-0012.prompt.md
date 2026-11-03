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
### སྲིད་པ་བར་མ་ན་ལས་ཀྱི་འཕེན་པ། ^1-28-0

[Block 422]
ཅི་སྲིད་པ་བར་མ་ན་ཡང་ལས་ཀྱི་འཕེན་པ་ཡོད་དམ་ཞེ་ན་སྨྲས་པ། ཡོད་དེ།

[Block 423 [VERSE]]
སྲིད་པ་བར་མ་འདོད་ཁམས་སུ། །
འཕེན་པ་རྣམ་པ་ཉི་ཤུ་གཉིས། །

[Block 424]
འདོད་པ་ན་སྤྱོད་པའི་སྲིད་པ་བར་མ་ནི་ལས་རྣམ་པ་ཉི་ཤུ་རྩ་གཉིས་འཕེན་ཏེ། ཇི་ལྟར་བྱས་པས་ཤེ་ན། མངལ་གྱི་གནས་སྐབས་ལྔ་སྟེ། ནུར་ནུར་པོ་དང་། མེར་མེར་པོ་དང་། ནར་ནར་པོ་དང་། གོར་གོར་པོ་དང་། རྐང་ལག་འགྱུས་པའི་གནས་སྐབས་རྣམས་སོ། །

[Block 425]
སྐྱེས་པའི་གནས་སྐབས་རྣམ་པ༌[^307]ལྔ་སྟེ། བྱིས་པ་དང་། གཞོན་ནུ་དང་། དར་ལ་བབ་པ་དང་། དར་ཡོལ་བ་དང་། རྒན་པོའི༌[^308]གནས་སྐབས་རྣམས་སོ། །

[Block 426]
དེ་ལ་སྲིད་པ་བར་མ་ནི་ནུར་ནུར་པོ་མྱོང་བར་འགྱུར་བར་ངེས་པ་དང་མ་ངེས་པའི་ལས་ཀྱང་འཕེན་པར་བྱེད་པ་ནས། དེ་བཞིན་དུ་རྒན་པོ་མྱོང་བར་འགྱུར་བ་དང་། སྲིད་པ་བར་མ་མྱོང་བར་འགྱུར་བའི་བར་དུ་འཕེན་པར་བྱེད་དོ། །

[Block 427]
དེ་ནི་མཐོང་ཆོས་འབྲས་བུ་ཡིན། །སྲིད་པ་བར་མའི༌[^309]ལས་ངེས་པ་རྣམ་པ་བཅུ་གཅིག་བཤད་པ་གང་ཡིན་པ་དེ་ནི་མཐོང་བའི་ཆོས་ལ༌[^310]མྱོང་བར་འགྱུར་བ་ཡིན་པར་རིག་པར་བྱའོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་རིས་གཅིག་ཁོ་ན་ཡིན། །དེ་ནི་རིས་མཐུན་པ་གཅིག་ཁོ་ན་ཡིན་ཏེ། སྲིད་པ་བར་མ་གང་ཡིན་པ་དང་། དེའི་རྒྱུ་ལས་བྱུང་བ་གནས་སྐབས་བཅུ་པོ་གང་དག་ཡིན་པ་དེ་ནི་ལས་གཅིག་གིས་འཕངས་པ་ཡིན་ནོ། །

[Block 428]
དེ་ཉིད་ཀྱི་ཕྱིར་སྲིད་པ་བར་མ་མྱོང་བར་འགྱུར་བའི་ལས་གཞན་མ་བཤད་དེ། དེ་ནི་སྐྱེས་ནས༌[^311]མྱོང་བར་འགྱུར་བ་ཁོ་ནས་འཕངས་པའི་ཕྱིར་རོ། །

[Block 429 [HEADING]]
### ངེས་པའི་ལས། ^1-29-0

[Block 430]
ཡང་ངེས་པའི་ལས་ཅི་འདྲ་བར་རིག་པར་བྱ་ཞེ་ན།

[Block 431 [VERSE]]
ཉོན་མོངས་རབ་དང་དྲག་པོ་དང་། །
ཡོན་ཏན་ཞིང་དང་རྒྱུན་ཆགས་སུ། །
བྱས་པ་གང་ཞིག་ཡིན་པ་དང་། །
ཕ་མ་གསོད་གང་དེ་ངེས་སོ། །

[Block 432]
ཉོན་མོངས་པ་དྲག་པོས་བྱས་པའི་ལས་གང་ཡིན་པ་དང་། རབ་ཏུ་དང་བ་དྲག་པོས་བྱས་པ་གང་ཡིན་པ་དང་། རྒྱུན་དུ་བྱེད་པ་གང་ཡིན་པ་དང་། ཡོན་ཏན༌[^312]གྱི་ཞིང་ལ་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་ངེས་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ། དེ་ལ་ཡོན་ཏན་གྱི་ཞིང་ནི་དཀོན་མཆོག་གསུམ་མམ། འགའ་ཞིག་གིས༌[^313]འབྲས་བུ་དང་། སྙོམས་པར་འཇུག་པ་ཁྱད་པར་ཅན་ཐོབ་པའི་གང་ཟག་ཁྱད་པར་ཅན་ཏེ། དེ་ལ་ནི་ཉོན་མོངས་པ་དང་རབ་ཏུ་དང་བ་དྲག་པོ་དང་། རྒྱུན་དུ་བྱེད་པ་མེད་པར་ཡང་དགེ་བའམ་མི་དགེ་བའི་ལས་ངེས་པར་འགྱུར་རོ། །

[Block 433]
ཕ་མ་ནི་ཕ་དང་མ་སྟེ། ཕ་དང་མ་གཉིས་གསོད་པའི་ལས་དེ་ནི་ཅི་འདྲ་ཡང་རུང་སྟེ། ངེས་པར་འགྱུར་རོ། །

[Block 434]
གཞན་ནི་མ་ཡིན་ནོ། །

[Block 435 [HEADING]]
### མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས། ^1-30-0

[Block 436]
ཡང་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཅི་འདྲ་བར་རིག་པར་བྱ་ཞེ་ན།

[Block 437 [VERSE]]
མཐོང་ཆོས་འབྲས་བུ་ཅན་གྱི་ལས། །
ཞིང་དང་བསམ་པའི་ཁྱད་པར་ལས། །

[Block 438]
མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས། །

[Block 439]
ཞིང་གི་ཁྱད་པར་ལས་འགྱུར་བ་ནི་དཔེར་ན་དགེ་སློང་ཞིག་གིས་དགེ་འདུན་ལ་བུད་མེད་དོ་ཞེས་ཐབ་མོ་བརྒལ་བ་ལས་མཚན་གྱུར་ཏོ་ཞེས་གྲགས་པ༌[^314]ལྟ་བུའོ། །

[Block 440]
བསམ་པའི་ཁྱད་པར་ལས་ནི་དཔེར་ན་ཉུང་རུམ་ཞིག་གིས་གླང་ཞིག་རླིག་པ་དབྱུང་བ་ལས་ཐར་བར་བྱས་པས་སྐྱེས་པ་ཉིད་དུ་གྱུར་པ་ལྟ་བུའོ། །

[Block 441]
ཡང་ན། ས་དེའི་འདོད་ཆགས་གཏན་བྲལ་ཕྱིར། །ཡང་ན་ལས་དགེ་བའམ་མི་དགེ་བའི་ལས༌[^315]གང་ཡིན་པ་དེ་ལས་གཏན་དུ་འདོད་ཆགས་དང་བྲལ་བ་ཡིན་པའི༌[^316]ཕྱིར་ལས་དེ་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་རོ། །

[Block 442]
ལས་ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། རྣམ་སྨིན་ངེས་པ་གང་ཡིན་པའོ། །

[Block 443]
ལས་གང་རྣམ་པར་སྨིན་པར་ངེས་ལ། གནས་སྐབས་སུ་ཡང་མ་ཡིན།[^317] མ་ངེས་པ་ཡང་མ་ཡིན་པ་དེ་ནི་དེ་ལྟར་ངེས་ཀྱི་གནས་སྐབས་གཞན་དུ་ངེས་པ་གང་ཡིན་པ་དེ་ནི་དེ་དང་ལྡན་བཞིན་དུ་གཏན་དུ་འདོད་ཆགས་དང་བྲལ༌[^318]མི་སྲིད་པས་དེ་ཉིད་དུ་རྣམ་པར་སྨིན་པར་འགྱུར་རོ། །

[Block 444]
མ་ངེས་པ་གང་ཡིན་པ་དེ་ནི་གཏན་དུ་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་རྣམ་པར་མི༌[^319]སྨིན་པ་ཉིད་དོ། །

[Block 445]
གང་དུ་གདོན་མི་ཟ་བར་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས་སུ་འགྱུར་བའི་ཞིང་དེ་ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། སྨྲས་པ་སངས་རྒྱས་ལ་སོགས་པ་དགེ་སློང་གི་དགེ་འདུན་དང་གང་ཟག་ལྔ་པོ། །

[Block 446 [VERSE]]
གང་དག་འགོག་བྱམས་ཉོན་མོངས་མེད། །
མཐོང་དང་དགྲ་བཅོམ་འབྲས་ལངས་པ། །

[Block 447]
དེ་ལ༌[^320]ཕན་གནོད་བྱས་པ་ཡིས།[^321] །འབྲས་བུ་འཕྲལ་དུ་མྱོང་བར་འགྱུར། །འགོག་པའི་སྙོམས་པར་འཇུག་པ་ལས་ལངས་པ་ནི་སྙོམས་པར་འཇུག་པ་མྱ་ངན་ལས་འདས་པ་དང་འདྲ་བའི་ཕྱིར་སེམས་མཆོག་ཏུ་ཞི་བ་འཐོབ་སྟེ། དེ་ནི་མྱ་ངན་ལས་འདས་པར་སོན་པ་ལས་སླར་ལོག་པ་དང་འདྲ་བ་ཡིན་ནོ། །

[Block 448]
ཉོན་མོངས་པ་མེད་པ་ལས་ལངས་པའི་རྒྱུད་ནི་སེམས་ཅན་ཚད་མེད་པ་ལ་ཉོན་མོངས་པ་མེད་པ་དང་ལྡན་པའི་ལྷག་པའི་བསམ་པ་དང་རྗེས་སུ་འབྲེལ་པ་དང་། ཤིན་ཏུ་གསལ་བའི་བསོད་ནམས་ཚད་མེད་པས་ཡོངས་སུ་བསྒོས་པ་དང་རྗེས་སུ་འབྲེལ་པ་ཡིན་ནོ། །

[Block 449]
བྱམས་པ་ལས་ལངས་པའི་རྒྱུད་ནི་སེམས་ཅན་ཚད་མེད་པ་ལ་ཕན་པའི་ལྷག་པའི་བསམ་པ་དང་རྗེས་སུ་འབྲེལ་པ་དང་། ཤིན་ཏུ་གསལ་བའི་བསོད་ནམས་ཚད་མེད་པས་ཡོངས་སུ་བསྒོས་པ་དང་རྗེས་སུ་འབྲེལ་པ་ཡིན་ནོ། །

[Block 450]
མཐོང་བའི་ལམ་ལས་ལངས་པའི་རྒྱུད་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་མ་ལུས་པར་སྤངས་པའི་ཕྱིར་གནས་ཡོངས་སུ་གྱུར་པ་སར་པ་ཡིན་པ་དྲི་མ་མེད་པ་ཡིན་ནོ། །

[Block 451]
དགྲ་བཅོམ་པ་ཉིད་ཀྱི་འབྲས་བུ་ལས་ལངས་པའི་རྒྱུད་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་མ་ལུས་པར་སྤངས་པའི༌[^322]ཕྱིར་གནས་ཡོངས་སུ་གྱུར་པ་སར་པ་ཡིན་པས་དྲི་མ་མེད་པ་ཡིན་ནོ། །

[Block 452]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་དག་ལས་ཕན་པ་དང་། གནོད་པ་བྱས་པ་རྣམས་ཀྱི་འབྲས་བུ་མཐོང་བའི་ཆོས་ཁོ་ན་ལ་ངེས་པ་འཐོབ་པར་འགྱུར་རོ། །

[Block 453]
ལྷག་མ་བསྒོམ་པའི་ལམ་ནི་རང་བཞིན་དང་འབྲས་བུ་ཡོངས་སུ་མ་རྫོགས་པ་ཅན་ཉིད་ཀྱི་ཕྱིར་དེ་ལས་ལངས་པ་རྣམས་ཀྱི་རྒྱུད་དེ་ལྟར་གནས་ཡོངས་སུ་གྱུར་པ་སར་པ་དང་དག་པ་མ་ཡིན་པས་དེ་དག་ནི་དེ་ལྟར་བསོད་ནམས་ཀྱི་ཞིང་མ་ཡིན་ནོ། །

[Block 454 [HEADING]]
### ལས་ཀྱི་རྣམ་པར་སྨིན་པ་སེམས་ཀྱི་ཚོར་བ་དང་ལུས་ཀྱི་ཚོར་བ། ^1-31-0

[Block 455]
རྣམ་པར་སྨིན་པའི་གཙོ་བོ་ནི་ཚོར་བ་ཡིན་པས་དེའི་ཕྱིར་འདི་དཔྱད་པར༌[^323]བྱ་སྟེ། ལས་ཀྱི་རྣམ་པར་སྨིན་པ་སེམས་ཀྱི་ཚོར་བ་ཁོ་ན་ཡིན་ལ་ལུས་ཀྱི་མ་ཡིན་པ་ཡོད་དམ། ལུས་ཀྱི་ཁོ་ན་ཡིན་ལ་སེམས་ཀྱི་མ་ཡིན་པ་ཡང་ཡོད་དམ་ཞེ་ན། སྨྲས་པ། ཡོད་དེ།

[Block 456 [VERSE]]
རྣམ་པར་རྟོག་པ་མེད་པ་ཡི། །
དགེ་བའི་ལས་ཀྱི་རྣམ་སྨིན་ནི། །
སེམས་ཀྱི་ཚོར་བ་ཁོ་ནར་འདོད། །

[Block 457]
རྣམ་པར་རྟོག་པ་མེད་པའི་ལས་ནི་བསམ་གཏན་ཁྱད་པར་ཅན་ནས་སྲིད་པའི་རྩེ་མོའི་བར་དག་ན་ཡོད་དེ། དགེ་བའི་ལས་རྣམ་པར་རྟོག་པ་མེད་པ་དེའི་རྣམ་པར་སྨིན་པ་ནི་སེམས་ཀྱི་ཚོར་བ་ཁོ་ན་ཡིན་ནོ། །ཅིའི་ཕྱིར་ལུས་ཀྱི་མ་ཡིན་ཞེ་ན། དེ་ནི་གདོན་མི་ཟ་བར་རྟོག་པ་དང་དཔྱོད་པ་དང་དཔྱད་པ༌[^324]ཡིན་པའི་ཕྱིར་རོ། །

[Block 458]
མི་དགེ་བ༌[^325]ནི་ལུས་ཀྱི་ཡིན། །མི་དགེ་བའི༌[^326]ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ནི་ལུས་ཀྱི་ཚོར་བ་ཁོ་ན་ཡིན་ནོ། །ཅིའི་ཕྱིར་སེམས་ཀྱི་མ་ཡིན་ཞེ་ན། དེའི་རྣམ་པར་སྨིན་པ་ནི་སྡུག་བསྔལ་གྱི་ཚོར་བ་ཡིན་ལ། སེམས་ཀྱི་སྡུག་བསྔལ་གྱི་ཚོར་བ་ནི་ཡིད་མི་བདེ་བ་ཡིན་ཏེ། ཡིད་མི་བདེ་བ་ནི་རྣམ་པར་སྨིན་པ་མ་ཡིན་ནོ་ཞེས་དེ་ནི་བཤད་ཟིན་ཏོ། །

[Block 459 [HEADING]]
### སེམས་གཡེང་བ། ^1-32-0

[Block 460]
འོ་ན་སེམས་ཅན་རྣམས་ཀྱི་སེམས་གཡེང་བར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་སེམས་གང་ཞིག་ལ་གནས་པ་ཡིན། རྒྱུ་ནི་ཅི་ཞིག་གིས་འགྱུར་ཞེ་ན།
--- END BLOCKS ---
