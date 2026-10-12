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
[Block 491]
ཇི་སྐད་དུ་རིན་པོ་ཆེ་འབར་བའི་རྒྱུད་ལས་ཀྱང་། རིགས་ཀྱི་བུ་འདུལ་བ་ལ་དད་པར་གྱིས་ཤིག །དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་ཆེན་པོ་བཞི་ཡིན་ནོ་ཞེས་པ་ལྟ་བུའོ། །

[Block 492]
བསྐྱེད་པའི་རིམ༌[^239]དང་ལྡན་པ་དག །ཅེས་པ་ནི་བསྐྱེད་པའི་རིམ་པ་ནི་བསྐྱེད་པའི་རིམ་པ་ཉིད་དོ། །

[Block 493]
དེ་དང་གང་ལྡན་པ་ནི་བསྐྱེད་པའི་རིམ་པ་དང་ལྡན་པའོ། །

[Block 494]
འདི་ཡང་སྤྱིའི༌[^240]ཡིན་ཞེས་པར་སྦྱར་རོ། །

[Block 495]
འདི་ལ་ཡང་ཅིའི་ཕྱིར་སྤྱི་ཞེས་བྱ་ཞེ་ན། འདི་ནི་ཁྱབ་པའི་ཕྱིར༌[^241]སྤྱི་ཡིན་ཞེས་པའོ། །

[Block 496]
སྤྱིའི་དོན་ནི་སྤྱིའི་དོན་ཏེ་ཁྱབ་པའི་དོན་ཏོ། །

[Block 497]
དེ་ནས༌[^242]སྦས་པའི་དོན་བཤད་པ། འདོད་ཆགས་ཆོས་ནི་རབ་སྟོན་པ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ་འདོད་ཆགས་ཀྱི་ཆོས་ནི་འདོད་ཆགས་ཀྱི་ཆོས་ཏེ། འཕྱང་བ་དང་། འཁྱུད་པ་དང་། འཕྱང་ཐག༌[^243]ལ་སོགས་པའོ། །

[Block 498]
འདི་ཉིད་ནི་ཐུགས་ལས༌[^244]ཕྱུང་བའི་ཕྱིར་སྦས་པའོ། །

[Block 499]
ཀུན་རྫོབ་ཀྱི་བདེན་པ་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་སྟེ་སྒྱུ་མ་ལྟ་བུའི་སྐུའོ། །

[Block 500]
ཡེ་ཤེས་གསུམ་པོ་ནི་སྣང་བའི་ཡེ་ཤེས་ལ་སོགས་པའོ། །

[Block 501]
འདི་དག་ཀྱང་། སྙིང་པོ་ཡོད་པས་སྦས་པའོ། །ཞེས་པའོ། །

[Block 502]
དང་པོས་ནི་དབྱེ་བ་བསྟན་ཏོ། །

[Block 503]
གཉིས་པས་ནི་ངེས་པའི་ཚིག་བསྟན་ཏོ། །

[Block 504]
གསུམ་པས་ནི་མིང་བསྟན་ཏོ། །

[Block 505]
དེ་ལྟར་སྦས་པའི་དོན་བསྟན་ནས། ད་ནི་མཐར་ཐུག་པའི་དོན་བསྟན་པར་བྱ་སྟེ། དེའི་ཕྱིར། འོད་གསལ་བ་ནི་རབ་སྟོན་དང་། །ཞེས་བྱ་བ༌[^245]སྨོས་ཏོ། །

[Block 506]
འོད་གསལ་བ་ནི་འོད་གསལ་བ་སྟེ། དོན་དམ་པའི་བདེན་པའོ། །

[Block 507]
ཟུང་དུ་འཇུག་པ་ནི་ཟུང་དུ་འཇུག་པ་སྟེ་གཉིས་སུ་མེད་པའི་དོན་ཏོ། །

[Block 508]
རྣམ་པ་གཉིས་ནི་འོད་གསལ་བ་དང་། ཟུང་དུ་འཇུག་པའོ། །

[Block 509]
ཐ༌[^246]མས་ནི་ངེས་པའི་ཚིག་བསྟན་ཏོ། །

[Block 510]
དེ་ལྟར་མཐའི་དབྱེ་བ་བསྟན་ནས་ད་ནི་བཤད་པའི་དབྱེ་བ་བསྟན་པའི་ཕྱིར། འཆད་པར༌[^247]ཉན་པར་འདོད་པ་ལ། །ཞེས་བྱ་བ་སྨོས་ཏེ་འཆད་པར་འདོད་པ་ནི་སློབ་དཔོན་ནོ། །

[Block 511]
ཉན་པར་འདོད་པ་ནི་སློབ་མའོ། །

[Block 512]
སློབ་མའི་དབྱེ་བ་ལ་གཉིས་ཡོད་པས་ན། དབྱེ་བ་ཡང་ནི་གཉིས་ཡིན་ཏེ། །ཞེས་སྨོས་སོ། །

[Block 513]
དེ་ཉིད་གང་ཞེ་ན།

[Block 514 [VERSE]]
ཚོགས་ལ་བཤད་པ་སྟོན་པ་དང་། །
གཉིས་པ་སློབ་མ་ལ་བཤད་པའོ། །

[Block 515]
ཞེས་སྨོས་ཏེ་དེ་ལ་ཚོགས་ལ་བཤད་པ་ནི་གང་ཞིག་ཡིན་ཅིའི་ཕྱིར་ཚོགས་ལ་བཤད་པ་ཞེས་བྱ་ཞེ་ན། ཇི་བཞིན་སྒྲ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཇི་བཞིན་པའི་སྒྲ་ནི་ཇི་བཞིན་པའི༌[^248]སྒྲའོ། །

[Block 516]
དེ་བཞིན་དུ་སྤྱིའི་དོན་གྱི་བར་ནི་ཚོགས་ལ་བཤད་པའོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་དེའི་སྣོད་དུ་གྱུར་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 517]
སློབ་མ་ལ་བཤད་པ་དུ་ཞིག །ཅིའི་ཕྱིར་སློབ་མ་ལ་བཤད་པ། །ཞེས་བྱ་ཞེ་ན། ཇི་བཞིན་མིན་སྒྲ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཇི་བཞིན་མིན་པ་ལ་སོགས་པ་རྣམ་པ་ལྔ་པོ་འདི་ནི་སློབ་མ་ལ་བཤད་པའོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་དེའི་སྣོད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 518]
དེ་ལྟར་བཤད་པ་རྣམ་པ་གཉིས་བསྟན་ནས། ད་ནི་གང་ཟག་གི་དབྱེ་བ་བསྟན་པའི་ཕྱིར། རྣམ་པ་ཀུན་དུ་ཉན་འདོད་པའི། །ཞེས་གསུངས་ཏེ་དུས་དང་རྣམ་པ་ཐམས་ཅད་དུ་ཉན་པར་འདོད་པའི་གང་ཟག་ཅེས་པའི་དོན་ཏོ། །

[Block 519]
རིགས་དུ་ཡོད་ཅེ་ན། །

[Block 520 [VERSE]]
བློ་ཡི་རྣམ་པ་དཔག་མེད་ལས། །
གང་ཟག་རྣམ་པ་ལྔར་འདོད་དོ། །

[Block 521]
ཞེས་སྨོས་ཏེ། འདི་ལྟར་རིགས་ཀྱི་དབང་དུ་དཔག་ཏུ་མེད་དེ། དཔེའི་དབང་དུ་རྣམ་པ་ལྔར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 522]
ལྔ་པོ་ཉིད་གང་ཡིན་སུས་གསུངས་ཤེ་ན།

[Block 523 [VERSE]]
ཨུཏྤ་ལ་དང་པད་དཀར་དང་། །
པདྨ་ཙནྡན་རིན་པོ་ཆེའི། །
རང་བཞིན་ཐ་དད་མིང་གིས་ཏེ། །
ཐམས་ཅད་མཁྱེན་པས་གསུངས་པ་ཡིན། །

[Block 524]
ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 525]
དེ་ལ་ཨུཏྤལ་ཞེས་བྱ་བའི་གང་ཟག་ནི་གང་ཞིག །ཅིའི་ཕྱིར་ཨུཏྤལ་གྱི་གང་ཟག་ཏུ་བརྟག་ཅེ་ན། བཤད་པ།

[Block 526 [VERSE]]
དེ་ནི་མ་ལུས་ཐོས་གྱུར་ལ། །
འཛིན་པ་ལ་ནི་རྣམ་པར་མཁས། །

[Block 527]
ཞེས་སྨོས་ཏེ་བཀའ་དང་བསྟན་བཅོས་ཐམས་ཅད་མ་ལུས་པར་ཐོས་པ་ནི་མ་ལུས་པར༌[^249]ཐོས་པའོ། །

[Block 528]
འཛིན་པ་ལ་ནི༌[^250]རྣམ་པར་མཁས། །ཞེས་པ་ནི་ཐོས་པ་ཙམ་གྱིས༌[^251]ཐམས་ཅད་ཁོང་དུ་ཆུད་པའོ། །

[Block 529]
སྐད་ཅིག༌[^252]ཙམ་གྱིས་བརྗེད༌[^253]འགྱུར་བ། །ཞེས་པ་ནི་བླ་མ་དང་བྲལ་བ་ཙམ་གྱིས་བརྗེད་པར༌[^254]འགྱུར་རོ། །

[Block 530]
དེའི་མིང་ཅི་ཞེ་ན། ཨུཏྤལ་ཞེས་བྱ་བའི་གང་ཟག་གོ། །ཞེས་སྨོས་ཏེ། ཨུཏྤལ་དང་འདྲ་བས་ཨུཏྤ་ལ་ལྟ་བུའི་གང་ཟག་གོ། །
--- END BLOCKS ---
