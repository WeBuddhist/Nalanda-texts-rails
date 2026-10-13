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
[Block 456]
ཡིད་ནི་ལུས་ཅན་མ་ཡིན་པས་ཚད་ཡོངས་སུ་མ་ཆད་པས་མི་དཔྱོད་དོ། །

[Block 457]
ད་ནི་གང་འདི་དག་རྣམ་པར་ཤེས་པའི་ཁམས་དྲུག་བཤད་པ་ཇི་ལྟར་དེ་དག་གི་ཡུལ་ད་ལྟར་བ་དང་དུས་གསུམ་ཡིན་པ་ལྟར་རྟེན་ཀྱང་དེ་ལྟ་བུ་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ཏེ། ཐ་མའི་རྟེན་འདས། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་རྟེན་ནི་འགགས༌[^177]མ་ཐག་པའི་ཡིད་དོ། །

[Block 458]
ལྔ་རྣམས་ནི། དེ་དག་ལྷན་ཅིག་སྐྱེས་པའང་ཡིན། །དེ་ལ་མིག་གི་རྣམ་པར་ཤེས་པའི་ལྷན་ཅིག་སྐྱེས་པའི་རྟེན་ནི་མིག་ནས་ལུས་ཀྱི་རྣམ་པར་ཤེས་པའི་བར་དུ་ཡང་ལུས་ཡིན་ལ།[^178] དེ་དག་གི༌[^179]འདས་པའི་རྟེན་ཡིད་ཡིན་ནོ། །

[Block 459]
ཡང་རྣམ་པར་ཤེས་པ་ནི་གཉིས་ཀ་ལ་རག་ལུས་ཏེ་སྐྱེ་ན༌[^180]ཅིའི་ཕྱིར་མིག་ལ་སོགས་པ་ཁོ་ན་ལ་བརྟེན་ཅེས་བྱ་བའི་གཟུགས་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ་ཞེ་ན།

[Block 460 [VERSE]]
དེ་དག་གྱུར་པས་འགྱུར་ཉིད་ཕྱིར། །
བརྟེན་ནི༌[^181]མིག་ལ་སོགས་པ་ཡིན། །

[Block 461]
མིག་ལ་སོགས་པ་རྣམས་གྱུར་པས་རྣམ་པར་ཤེས་པ་རྣམས་འགྱུར་བ་ཡིན་ཏེ། ཕན་པ་དང་གནོད་པ་དང་། གསལ་བ་དང་མི་གསལ་བ་ཉིད་ཀྱི་རྗེས་སུ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 462]
གཟུགས་ལ་སོགས་པ་རྣམས་གྱུར་པས༌[^182]དེ་དག་འགྱུར་བ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་དེ་ཁོ་ན་རྟེན་ཡིན་ནོ། །

[Block 463]
ཡང་དེ་དག་གིས་ནི་གཟུགས་ལ་སོགས་པ་རྣམ་པར་ཤེས་ན། ཅིའི་ཕྱིར་མིག་ལ་སོགས་པ་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་ལ། གཟུགས་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པ་མ་ཡིན་ཞེ་ན། གང་གི་ཕྱིར་དེ་དག་གི་རྟེན་ནི་མིག་ལ་སོགས་པ་ཡིན་པ།

[Block 464 [VERSE]]
དེ་ཕྱིར་ཐུན་མོང་མ་ཡིན་ཕྱིར། །
དེ་དག་གིས་ནི་རྣམ་ཤེས་བསྟན། །

[Block 465]
མིག་ནི་རྣམ་པར་ཤེས་པ་གཞན་གྱི་རྟེན་དུ་འགྱུར་བར་མི་ནུས་ལ། གཟུགས་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་དམིགས་པར་ཡང་འགྱུར་ལ། མིག་གི་རྣམ་པར་ཤེས་པའི་དམིགས་པར༌[^183]ཡང་འགྱུར་ཏེ། ལུས་ཀྱི་བར་དུ་ཡང་དེ་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 466]
དེ་ལྟ་བས་ན་རྟེན་དུ་གྱུར་པའི་ཕྱིར་དང་། ཐུན་མོང་མ་ཡིན་པའི་ཕྱིར་དེ་དག་ཁོ་ནས་རྣམ་པར་ཤེས་པ་བསྟན་གྱི་གཟུགས་ལ་སོགས་པ་ནི་མ་ཡིན་ཏེ། དཔེར་ན་རྔ་བོ་ཆེའི་སྒྲ་དང་། ནས་ཀྱི་མྱུ་གུ་བཞིན་ནོ། །

[Block 467]
ཡང་ལུས་གང་ལ་གནས་ཏེ་མིག་གིས༌[^184]གཟུགས་རྣམས་ལ་ལྟ་བ་ན། ཅི་ལུས་དང་མིག་དང་གཟུགས་དང་རྣམ་པར་ཤེས་པ་དེ་རྣམས་ས་གཅིག་པ༌[^185]ཁོ་ན་ཞིག་ཡིན་ནམ། འོན་ཏེ་གཞན་གྱིས་པ་ཡང་ཡིན་ཞེ་ན། སྨྲས་པ། ཐམས་ཅད་ལ་བྱེ་བྲག་ཡོད་དེ། དེ་ལ་ངེས་པ་འདི་ཡིན་ཏེ། ལུས་ལ་འོག་གི་མིག་མ་ཡིན། །ལས་དང་མིག་དང་གཟུགས་རྣམས་ནི་འདོད་པ་ན་སྤྱོད་པ་ནས༌[^186]བསམ་གཏན་བཞི་པའི་བར་ས་ལྔ་པ་ཡིན་ནོ། །

[Block 468]
མིག་གི་རྣམ་པར་ཤེས་པ་ནི་འདོད་པ་ན་སྤྱོད་པ་དང་། བསམ་གཏན་དང་པོའི་ས་པ་དང་ས་གཉིས་པ་ཡིན་ནོ། །

[Block 469]
དེ་ལས་གང་སའི༌[^187]ལུས་ཡིན་པའི་ས་དེ་པའམ། ས་གོང་མའི་ཡིན་གྱི་ས་འོག་མའི་མ་ཡིན་ནོ། །

[Block 470]
འདིའི་མིག་གི་ཡུལ་ནི་དེའི་ས་པ་འམ་ས་འོག་མའི་གཟུགས་ཡིན་གྱི། མིག་གི༌[^188]གོང་མའི་གཟུགས་མ་ཡིན། ས་གོང་མའི་གཟུགས་ས་འོག་མའི་མིག་གིས་མཐོང་བར་ནི་ནམ་ཡང་མི་ནུས་སོ། །

[Block 471]
རྣམ་པར་ཤེས་པའང་། ས་གོང་མའི་མ་ཡིན་ཏེ། གཟུགས་བཞིན་ནོ། །

[Block 472]
དེ་ཡི་གཟུགས། ལུས་ཀྱིའང་གཉིས་ཀ་ཐམས་ཅད་དུ་དེའི་ཞེས་བྱ་བ་བཤད་མ་ཐག་པའི་མིག་གི་རྣམ་པར་ཤེས་པའི་ཡུལ་ནི་གོང་མ་དང་འོག་མ་དང་རང་གི་ས་པའི་གཟུགས་ཐམས་ཅད་དུ་ཡིན་ལ། ལུས་ཀྱིའང་གཟུགས་དང་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་དུ་ཡིན་ནོ། །

[Block 473]
ཇི་ལྟར་མིག་འདི་རྒྱས་པར་བཤད་པ་ལྟར། རྣ་བའང་དེ་བཞིན།

[Block 474 [VERSE]]
ལུས་ལ་གོང་མའི་རྣ་བ་མིན། །
རྣ་བས་གོང་མའི་སྒྲ་མ་ཡིན། །
རྣམ་པར་ཤེས་པའང་སྒྲ་ནི་འདིའི། །
ལུས་ཀྱིའང་གཉིས་ཀ་ཐམས་ཅད་དུ། །

[Block 475]
གསུམ་དག་ནི། ཐམས་ཅད་རང་གི་ས་པ་ཉིད། །སྣ་དང་ལྕེ་དང་ལུས་ཀྱི་ཁམས་རྣམས་ཀྱི་ནི་ལུས་དང་ཡུལ་དང་རྣམ་པར་ཤེས་པ་རྣམས་རང་གི་ས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 476]
སྤྱིར་བསྟན་ནས༌[^189]དམིགས་ཀྱིས་བསལ་བ་གསུངས་པ་ནི། ལུས་ཀྱི་རྣམ་ཤེས་འོག་དང་ནི། །རང་གི་ས་པ་ལུས་དང་ལུས་ཀྱི་ཁམས་དང་རེག་བྱ་ནི་རྟག་ཏུ་རང་གི་ས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 477]
ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་ནི་ཁ་ཅིག་གི་རང་གི་ས་པ་ཡིན་ཏེ་འདི་ལྟ་སྟེ། འདོད་པའི་ཁམས་དང༌[^190]བསམ་གཏན་དང་པོར་སྐྱེས་པ་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 478]
ཁ་ཅིག་ནི་ས་འོག་མ་པ༌[^191]ཡིན་ཏེ། འདི་ལྟ་སྟེ། བསམ་གཏན་གཉིས་པ་ལ་སོགས་པར་སྐྱེས་པ་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 479]
ཡིད་མ་ངེས་ཏེ། རེས་འགའ་ནི་ལུས་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་། ཆོས་དག་དང་མཚུངས་པའི་ས་པའི་ཡིད་ཡིན་ལ། རེས་འགའ་ནི་ས་གོང་མ་དང་འོག་མ་པ་ཡིན་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་ས་ལྔ་པའི་ལུས་ལ་ཡང་སྙོམས་པར་འཇུག་པ་དང་། སྐྱེ་བའི་ཚེ་ཡིད༌[^192]ལ་སོགས་པའི་ས་ཐམས་ཅད་པ་དག་ཡིན་ནོ། །

[Block 480 [HEADING]]
#### ཤེས་པར་བྱ་བ། ^1-18-18-0

[Block 481]
འདི་དཔྱད་པར་བྱ་སྟེ། ཁམས་བཅོ་བརྒྱད་པོ་རྣམ་པར་ཤེས་པ་དྲུག་པོ་རྣམས་ལས་གང་གིས་ཤེས་པར་བྱ་བ་ཡིན་ཞེ་ན། སྨྲས་པ། གཉིས་ཀྱི་རྣམ་ཤེས་ཕྱི་ཡི༌[^193]ལྔ། །གཟུགས་ལ་སོགས་པའི་ཡུལ་རྣམས་ནི་མིག་ལ་སོགས་པ་ལ་བརྟེན་པའི༌[^194]རྣམ་པར་ཤེས་པ་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་ཤེས་པར་བྱ་བའོ། །

[Block 482]
ལྷག་མ་ཁམས་བཅུ་གསུམ་དག་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཉིད་ཀྱིས་ཤེས་པར་བྱ་བའོ་ཞེས་བརྗོད་པར་འགྱུར་རོ། །

[Block 483 [HEADING]]
#### རྟག་པ། ^1-18-19-0

[Block 484]
ཁམས་བཅོ་བརྒྱད་པོ་དེ་དག་ལས་རྟག་པ་རྣམས་ནི་དུ། མི་རྟག་པ་རྣམས་ནི་དུ་ཞེ་ན། འདུས་མ་བྱས་ཆོས་རྟག་པའོ། །

[Block 485]
དེས་ན་ཆོས་ཀྱི༌[^195]ཁམས་ཀྱི་ཕྱོགས་གཅིག་རྟག་ལ་ལྷག་མ་རྣམས་ནི་མི་རྟག་པ་ཡིན་ནོ། །

[Block 486 [HEADING]]
#### དབང་པོ། ^1-18-20-0

[Block 487]
དབང་པོ་རྣམས་ནི་དུ། དབང་པོ་མ་ཡིན་པ་རྣམས་ནི་དུ་ཞེ་ན།

[Block 488 [VERSE]]
ཆོས་ཀྱི་ཕྱེད་དང་གང་དག་ནི། །
བཅུ་གཉིས་ནང་གིར་བཤད་དབང་པོ། །

[Block 489]
དེ་ལ་ཆོས་ཞེས༌[^196]བྱ་བའི་ཕྱེད་ནི་སྲོག་གི་དབང་པོ་ལ་སོགས་པ་དབང་པོ་བཅུ་གཅིག་དང་། མི་ཤེས་པ་ཀུན་ཤེས་པར་བྱེད་པ་ལ་སོགས་པ་དབང་པོའི་ཆ་སྟེ། ཆོས་ཀྱི་ཁམས་ཀྱི་ཕྱོགས་གཅིག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 490]
ནང་གི་བཅུ་གཉིས་ནི་མིག༌[^197]ལ་སོགས་པ་རང་གི་མིང་གིས་སྨོས་པ་ལྔ་དང་། ཡིད་ཀྱི་དབང་པོ་ནི་སེམས་ཀྱི་ཁམས་བདུན་ནོ། །

[Block 491]
ཕོ་དང་མོའི་དབང་པོ་དག་ནི་ལུས་ཀྱི་ཕྱོགས་གཅིག་གོ། །

[Block 492]
ལྷག་མ་ཁམས་ལྔ་པོ་དེ་དག་དང་ཆོས་ཀྱི་ཁམས་ཀྱི་ཕྱོགས་ནི་དབང་པོ་མ་ཡིན་པ་ཞེས་བྱ་བར་གྲུབ་པོ། །ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་བསྟན་པ་ཞེས་བྱ་སྟེ། མཛོད་ཀྱི་གནས་དང་པོའོ།། །།

[Block 493 [HEADING]]
## དབང་པོ་བསྟན་པ། ^2-0

[Block 494 [HEADING]]
### དབང་པོ་རྣམས་བཤད་པ། ^2-1-0

[Block 495 [HEADING]]
#### དབང་པོའི་དོན། ^2-1-1-0
--- END BLOCKS ---
