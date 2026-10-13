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
[Block 491 [VERSE]]
བསྐྱེད་པའི་རིམ་པའི་ངོ་བོ་ནི། །
རགས་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན། །

[Block 492]
ཞེས་པ་རགས་པའི་སྐུ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་གང་ཡིན་པ༌[^224]དེ་བསྐྱེད་པའི་རིམ་པའི་ངོ་བོའོ། །

[Block 493]
གཞན་དུ་ནི༌[^225]ངོ་བོ་ཉིད་ཡིན་པ་དང་མ་ཡིན་པ་དང་ཐེ་ཚོམ་ཟ་བ་ལ་སོགས་པའི་ཉེས་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 494]
འདི་ལ་དབྱེ་བ་ནི་དུ་ཞིག་ཅེ་ན།

[Block 495 [VERSE]]
བསྐྱེད་པ་རྣམ་པ་གཉིས་ཡིན་ཏེ། །
སྦྱང་བྱ་དང་ནི་སྦྱོང་བྱེད་དོ། །

[Block 496]
ཞེས་པ་གང་སྦྱང་བར་བྱ་བ་འདི་ཡང༌[^226]གང་ཡིན་ཞེ་ན། སྦྱང་བྱ་སྣོད་བཅུད་རྣམ་པ་སྟེ། །ཞེས་པ་སྦྱང་བར་བྱ་བའི་བསྐྱེད་པ་ནི་ལས་ལས་སྐྱེས་པའི་སྣོད་བཅུད་ཀྱི་འཇིག་རྟེན་ནོ། །

[Block 497]
སྦྱོང་བྱེད་ཅེས་པའང་གང་ཡིན་ཞེ་ན།

[Block 498 [VERSE]]
སྦྱོང་བར་བྱེད་པ་རྣམ་པ་གཉིས། །
རྟེན་དང་བརྟེན་པའི་བསྐྱེད་པའོ། །

[Block 499]
ཞེས་པ་རྟེན༌[^227]ནི་འོག་གི་ཕྱོགས་ནས་འབྱུང་བ༌[^228]གཞལ་ཡས་ཁང་དང་བཅས་པའོ། །

[Block 500 [VERSE]]
བརྟེན་པ་ལ་ནི་རྣམ་པ་གཉིས། །
གཙོ་བོ་དང་ནི་འཁོར་བསྐྱེད་པའོ། །

[Block 501]
ཞེས་པ༌[^229]གཙོ་བོ་བསྐྱེད་པའི་རིམ་པ་དང་། །འཁོར་བསྐྱེད་པའི་རིམ་པ་སྐད་ཅིག་པའམ། རིམ་གྱིས་བསྐྱེད་པ་འདི་ནི་བསྐྱེད་པའི་རིམ་པའོ། །

[Block 502]
འདི་ལའང་ཅིའི་ཕྱིར་ཞེ་ན།

[Block 503 [VERSE]]
སེམས་ཅན་སྐྱེ་དང་མཐུན་ཕྱིར་དང་། །
རྣམ་པར་རྟོག་བློས་བསྐྱེད་ཕྱིར་རོ། །

[Block 504]
ཞེས་པ་སེམས་ཅན་གང་དག་མངལ་ནས་སྐྱེ་བ་ལ་སོགས་པ་དང་མཐུན་པ་དང་། རྣམ་པར་རྟོག་པའི་བློས་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 505]
བསྐྱེད་དང་རགས་པ་ལ་སོགས་པ། །རྣམ་གྲངས་ཡིན་པར་ཤེས་པར་བྱ། ཞེས་པ་བསྐྱེད་པའི་རིམ་པ་ཞེས་བྱ་བ་དང་། རགས་པའི་རྟོག་པ་བཟློག་པའི་གཉེན་པོ་ཞེས་བྱ་བ་དང་། རིང་པའི་རྒྱུ་དང་ཐུན་མོང་གི་རྒྱུ་དང་། འདི་དག་ནི་རྣམ་གྲངས་སུ་ཤེས་པར་བྱའོ། །

[Block 506]
ཆོས་དུ་དང་ལྡན་པ་ཡིན་ཞེ་ན།

[Block 507 [VERSE]]
རགས་པའི་སྐུ་ལ་དམིགས་ལ་སོགས། །
ལྔ་དྲུག་ལྡན་པ་དེ་ཉིད་དོ། །

[Block 508]
ཞེས་པ་རགས་པའི་སྐུ་ལ་དམིགས་པ་ཏིང་ངེ་འཛིན་ཡིན་པ་རྣམ་གྲངས་དང་ངེས་པའི་ཚིག་ཏུ་བཅས་པའོ། །

[Block 509]
དེ་ཇི་ལྟར་གཞན་སེལ་བ་ཡིན་ཞེ་ན།

[Block 510 [VERSE]]
གང་དུ་གཞན་དུ་ཐལ་འགྱུར་བ། །
སེལ་བར་བྱེད་ཕྱིར་དེ་སྐད་དོ། །

[Block 511]
ཞེས་པ་ནི་གོང་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 512]
འདིའི་གླེང་གཞི་ཡང་གང་ཡིན་ཞེ་ན།

[Block 513 [VERSE]]
གསང་བ་ལས་ནི་གཞན་དོན་དུ། །
ཇི་ལྟར་རིམ་འབྱུང་གླེང་གཞི་ཡིན། །

[Block 514]
ཞེས་པ་སེམས་ཅན་འདོད་ཆགས་ཅན་འདུལ་བ་དང་བྲལ་བ་དང་བར་མ་བསྐྱེད་པའི་རིམ་པ་ལ་འཕྲོད་པའི་དབང་དུ་ཟླ་བ་དང་རྡོ་རྗེ་ལ་སོགས་པ་འབྱུང་བར་འགྱུར་བ་གླེང་གཞིའོ། །

[Block 515]
འོ་ན་བསྐྱེད་པའི་དམིགས་པའང་གང་ཡིན་ཞེ་ན། དམིགས་པ་བསྐྱེད་པ་ལྷ་དང་གནས། །མང་བའམ་ནི་ཉུང་བའོ། །ཞེས་པ་རིམ་པའམ་ཅིག་ཅར་གྱིས་ལྷའི་སྐུ་དང་གཞལ་ཡས་ཁང་གི་རྣམ་པ་དང་། དེ་ཉིད་མང་བའམ་ཉུང་བའམ། ཆེ་བ་འམ་ཆུང་བ་ལ་དམིགས་པ་གང་ཡིན་པ་འདི་ནི་དམིགས་པ༌[^230]ཞེའོ། །

[Block 516]
དམིགས་པའང་ཐོབ་པའི་རྒྱུ་གང་ཡིན་ཞེ་ན།

[Block 517 [VERSE]]
ས་བོན་ཟས་དང་སྐོམ༌[^231]ལ་སོགས། །
འབྲས་བུ་ཐོབ་ཕྱིར་རྒྱུ་རུ་བཤད། །

[Block 518]
ཅེས་པ་གང་གི་རྒྱུད་ལ་བསྐྱེད་པའི༌[^232]ས་བོན་ཡོད་པ་དང་། ཟས་དང་སྐོམ་དང་སྨན་དང་། གནས་དང་ཡུལ་དང་གྲོགས་ལ་སོགས་པ་འབྲས་བུ་ཐོབ་པ་ལ་ཕན་པ་རྒྱུ་ཡིན་ཞེས་བྱའོ། །

[Block 519]
དུས་གང་གི་ཚེ་སྒོམ་ཞེ་ན། མཆོག་འདོད་པ་དང་དབང་བསྐུར་བ༌[^233]དང་།

[Block 520 [VERSE]]
ཚོགས་དང་གཏོར་མ་སྦྱིན་སྲེག་དང་། །
ཉམས་པ་བསྐང༌[^234]དང་ཐུན་མོང་འདོད། །
འདི་ཡི་དུས་ན་བསྒོམ་པར་བྱ། །

[Block 521]
ཞེས་པ་གང་མཆོག་འདོད་པའི་རྒྱུ་དག༌[^235]དང་། སློབ་མ་དབང་བསྐུར་བའི་དུས་དང་། ཚོགས་ཀྱི་འཁོར་ལོ་ཆེན་པོ་དང་། འདི་དག་གི་སྦྱོར་བ་གང་ཡིན་པའི་དུས་སུ་བསྐྱེད་པའི་རིམ་པ་ཉམས་སུ་བླང་བར་བྱའོ། །

[Block 522 [VERSE]]
འོ་ན་འབྲས་བུ་གང་ཡིན་ཞེ་ན། །
འབྲས་བུ་ཐུན་མོང་དངོས་གྲུབ་འབྱུང་། །

[Block 523]
ཞེས་པ་འབྲས་བུའང་གང་གིས་ཐུན་མོང་གི་དངོས་གྲུབ་བརྒྱད་ལ་སོགས་པ༌[^236]འགྲུབ་པར་འགྱུར་གྱི་གཞན་འོག་མ་རྣམས་ཀྱིས་ནི་མ་ཡིན་ཞེས་དགོངས་སོ། །

[Block 524]
འདི་དག་གི་སྔོན་དུ་འགྲོ་བའང་གང་ཡིན་ཞེ་ན།

[Block 525 [VERSE]]
མཚམས་བཅད་ཚོགས་གཉིས་བསགས་པ་ནི། །
འདི་ཡི་སྔོན་དུ་འགྲོ་བ་ཡིན། །

[Block 526]
ཞེས་པ། གང་གིས་བསྐྱེད་པའི་རིམ་པའི་སྔོན་དུ་ནི་དང་པོར་མཚམས་བཅད་པ་དང་། བསོད་ནམས་ཀྱི་ཚོགས་དང་། [^237]ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་ཡན་ལག་བསྒོམ་པར་བྱའོ།[^238] །རྟེན་གྱི་གང་ཟག་ཀྱང་གང་ཡིན་ཞེ་ན།

[Block 527 [VERSE]]
གང་འདི་ཚོགས་དང་སློབ་མ་ཡིས། །
འདི་ནི་བསླབ་པར་བྱ་བ་ཡིན། །

[Block 528]
ཞེས་པ་འདི་ནི་ཐུན་མོང་སྒྲུབ་པའི་དབང་དུ་བྱས་ཏེ་དེ་ཉིད་དོ། །

[Block 529]
གཞན་གྱི་དབང་དུ་བྱས་ཏེ་སློབ་མས་ཀྱང་ངོ་། །གནས་ཀྱང༌[^239]གང་དུ་ཞེ་ན།

[Block 530 [VERSE]]
གནས་ནི་ཡིད་མཐུན་ཉམས་དགའ་བར། །
རྣལ་འབྱོར་པ་ཡིས༌[^240]བསམ་གཏན་བསྒོམ། །
--- END BLOCKS ---
