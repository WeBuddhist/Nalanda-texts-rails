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
ཆགས་པ་ལ་སོགས་པའི་ངོ་བོ་ཉིད་དང་མཚུངས་པར་ལྡན་པ་དང་། ཀུན་ནས་བསླང་བ་ནི་མི་དགེ་བའོ། །

[Block 492]
གཞན་ནི་ལུང༌[^203]དུ༌[^204]མ་བསྟན་པ་ཡིན་ནོ། །

[Block 493]
གཟུགས་དང་སྒྲའི་ཁམས་ནི་ལུས་དང་ངག་གི་རྣམ་པར་རིག་བྱེད་ཀྱིས་བསྡུས་པ་དགེ་བ་དང་མི་དགེ་བའི་སེམས་ཀྱིས་ཀུན་ནས་བསླང་བ་དག་ནི་དགེ་བ་དང་མི་དགེ་བ་ཡིན་ནོ། །

[Block 494]
དེ་ལས་གཞན་པ་དག་ནི་ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 495]
དགེ་བ་ལ་སོགས་པའི་དངོས་པོ་བཤད་ཟིན་ཏོ། །

[Block 496 [HEADING]]
#### འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པར་གཏོགས་པ། ^1-3-4-0

[Block 497 [HEADING]]
##### འདོད་ཁམས་གཏོགས་པ། ^1-3-4-1-0

[Block 498]
ཁམས་བཅོ་བརྒྱད་པོ་དེ་དག་ལས་འདོད་པར་གཏོགས་པ་རྣམས་ནི་དུ། གཟུགས་དང་གཟུགས་མེད་པར་གཏོགས་པ་རྣམས་ནི་དུ་ཞེ་ན། འདོད་ཁམས་གཏོགས་པ་ཐམས་ཅད་དོ། །

[Block 499]
གཏོགས་པ་ནི་མ་བྲལ་བ་སྟེ། འདོད་པའི་ཁམས་དང་ལྡན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 500 [HEADING]]
##### གཟུགས་ཀྱི་ཁམས་སུ་གཏོགས་པ། ^1-3-4-2-0

[Block 501]
གཟུགས་ཀྱི་ཁམས་ནི༌[^205]བཅུ་བཞིའོ། །

[Block 502]
གཟུགས་ཀྱི་ཁམས་ན་ནི་ཁམས་བཅུ་བཞི་སྟེ།

[Block 503 [VERSE]]
དྲི་དང་རོ་དང་སྣ་དང་ནི། །
ལྕེའི་རྣམ་པར༌[^206]ཤེས་ཁམས་མ་གཏོགས། །

[Block 504]
དེ་ན་དྲི་དང་རོ་དག་མེད།[^207] །དེ་གཉིས་ནི་ཁམས་ཀྱི་ཟས་ཡིན་པའི་ཕྱིར་ལ། དེ་དག་གི་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ཀྱང་དེར་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 505]
དེ་ལྟ༌[^208]བས་ན་དམིགས་པ་མེད་པའི་ཕྱིར་སྣ་དང་ལྕེའི་རྣམ་པར་ཤེས་པ་དག་ཀྱང་མེད་དོ། །

[Block 506]
དེ་ལྟ༌[^209]ན་ནི་འོ་ན་དེ་ནི་རེག་བྱའི་ཁམས་ཀྱང་མེད་པར་ཐལ་བར་འགྱུར་ཏེ། ཁམས་ཀྱི་ཟས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 507]
ཟས་ཀྱི་རང་བཞིན་མ་ཡིན་པ༌[^210]གང་ཡིན་པ་དེ་དེ་ན༌[^211]ཡོད་དོ། །

[Block 508]
དྲི་དང་རོ་དག་ཀྱང་དེ་ལྟར་ཐལ་བར་འགྱུར་རོ། །

[Block 509]
རེག་བྱ་དབང་པོའི་རྟེན་དང་གཞི་དང་བགོ་བ་ལ་སོགས་པའི་དངོས་པོར་ཡོད་དུ་ཆུག་ཀྱང་ཟས་མིད་པ་མེད་པར་དྲི་དང་རོ་དག་ལ་ཡོངས་སུ་ལོངས་སྤྱོད་པ་མེད་དེ། དེ་ལྟ་བས་ན་དེ་ན་ཟས་མིད་པའི་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ལ་དྲི་དང་རོ་དག་དགོས་པ་མེད་ཀྱི་རེག་བྱ་ནི་མ་ཡིན་ནོ། །

[Block 510]
གཞན་དག་ན་རེ་ནི་སྙོམས་པར་འཇུག་པའི་བསམ་གཏན་ལ་བརྟེན་ནས་འདིར་གཟུགས་རྣམས་ཀྱང་མཐོང་ཞིང་སྒྲ་རྣམས་ཀྱང་ཐོས་ལ་ཤིན་ཏུ་སྦྱངས་པ་དང་ལྷན་ཅིག་པར་གྱུར་པའི་རེག་བྱའི་ཁྱད་པར་གྱིས་ཀྱང་ལུས་ལ་ཕན་འདོགས་པས། དེའི་ཕྱིར་སྐྱེ་བའི་བསམ་གཏན་ན་གསུམ་པོ་དེ་དག་སྲིད་ཀྱི། དྲི་དང་རོ་དག་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 511]
དེ་ལྟ་ན་ནི་འོ་ན་སྣ་དང་ལྕེའི་དབང་པོ་དག་ཀྱང་མེད་པར་ཐལ་བར་འགྱུར་ཏེ། དགོས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 512]
དགོས་པ་ཡོད་དེ། དེ་དག་མེད་པར་ནི་རྟེན་མཛེས་པ་ཉིད་དང་། མངོན་པར་བརྗོད་པར་ཡང་མི་འགྱུར་རོ། །

[Block 513]
གལ་ཏེ་དགོས་པ་དེར་ཟད་ན་མཛེས་པར་བྱ་བའི་དོན་དང་། ཚིག་གི་དོན་དུ་རྟེན་ཁོ་ནས་ཆོག་གི་དབང་པོ་ནི་དགོས་པ་མེད་དོ།[^212] །དབང་པོ་མེད་པའི་རྟེན་ནི་མི་སྲིད་དེ། ཕོའི་དབང་པོའི་རྟེན་བཞིན་ནོ། །

[Block 514]
དེ་ནི་དགོས་པ་མེད་པའི་ཕྱིར་མི་སྲིད་པར་རིགས་ཀྱི་སྣ་དང་ལྕེའི་དབང་པོའི་རྟེན་ནི་དགོས་པ་དང་བཅས་པ་ཡིན་པས། དེའི་ཕྱིར་འདི་དག་ནི་དབང་པོ་མེད་པར་ཡང་སྲིད་པར་རིགས་སོ། །

[Block 515]
དགོས་པ་མེད་པར་ཡང་དབང་པོ་མངོན་པར་འགྲུབ་པར་འགྱུར་ཏེ། དཔེར་ན་མངལ་དུ་ངེས་པར་འཆི་བ་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 516]
དགོས་པ་མེད་པ་ཡིན་མོད་ཀྱི་རྒྱུ་མེད་པ་ཅན་ནི་མ་ཡིན་ནོ། །

[Block 517]
དབང་པོ་སྐྱེ་བའི་རྒྱུ་གང་ཞེ་ན། དབང་པོ་ལ་སྲེད་པ་དང་བཅས་པའི་ལས་ཀྱི་ཁྱད་པར་རོ། །

[Block 518]
གང་ཡང་ཡུལ་ལ་སྲེད་པ་དང་བྲལ་བ་དེ་ནི་གདོན་མི་ཟ་བར་དབང་པོ་ལས་ཀྱང་སྲེད་པ་དང་བྲལ་བ་ཡིན་པས་དེ་དག་གི་ཡུལ་ལ་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ལ་སྣ་དང་ལྕེའི་དབང་པོ་དག་འབྱུང་བར་འོས་པ་མ་ཡིན་ནོ། །

[Block 519]
ཡང་ན་ཕོའི་དབང་པོ་ཡང་ཅི་སྟེ་འགྲུབ་པར་མི་འགྱུར། མི་མཛེས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 520]
མདོམས་ཀྱི་སྦ་བ༌[^213]སྦུབས་སུ་ནུབ་པ་རྣམས་ཀྱི་ཅིའི་ཕྱིར་མི་མཛེས་པར་འགྱུར། དགོས་པའི་དབང་གིས་འབྱུང་བ་ཡང་མ་ཡིན་ནོ། །

[Block 521]
འོ་ན་ཅི་ཞེ་ན། རྒྱུའི་དབང་གིས་འབྱུང་བས་རྒྱུ་ཡོད་ན་མི་མཛེས་པར་བྱེད་བཞིན་དུ་ཡང་འབྱུང་བར་འགྱུར་བ་ཉིད་དོ། །

[Block 522]
འོ་ན་ནི་མདོ་ལས་དབང་པོ་རྣམས་མ་ཚང་བ་མེད་ཅིང་མེད་པ༌[^214]མ་ཡིན་ནོ་ཞེས་འབྱུང་བ་དང་འགལ་ལོ་ཞེ་ན། དེ་ན༌[^215]དབང་པོ་གང༌[^216]དག་སྲིད་པ་དེ་དག་གིས་དབང་པོ་མེད་པ་མ་ཡིན་པས་འདི་ལ་འགལ་བ་ཅི་ཞིག་ཡོད། དེ་ལྟ་མ་ཡིན་ན་ཕོའི་དབང་པོ་ཡང་ཡོད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 523]
འདི་སྐད་དུ་ལུས་ཀྱི་སྒོ་ནས་སྐྱེ་མཆེད་དྲུག་ལ་སྲེད་པ་ཀུན་དུ་སྤྱོད་ཀྱི་ཡུལ་གྱི་སྒོ་ནས་ནི་མ་ཡིན་པས་དེ་ན་སྣ་དང་ལྕེའི་དབང་པོ་དག་ནི་ཡོད་པ་ཉིད་ཀྱི་དྲི་དང་རོ་དག་ནི་མ་ཡིན་ནོ། །

[Block 524]
ཕོའི་དབང་པོ་ནི་འཁྲིག་པ་རེག་པའི་སྒོ་ནས་སྲེད་པ་ཀུན་ཏུ་སྤྱོད་པས་དེ་ལྟ་བས་ན་གཟུགས་ཀྱི་ཁམས་སུ་གཏོགས་པའི་ཁམས་བཅུ་བཞིའོ་ཞེས་བྱ་བ་དེ་གྲུབ་བོ་ཞེས་བརྗོད་དོ། །

[Block 525 [HEADING]]
##### གཟུགས་མེད་གཏོགས་པ། ^1-3-4-3-0

[Block 526 [VERSE]]
གཟུགས་མེད་གཏོགས་པ་ཡིད་དང་ནི། །
ཆོས་དང་ཡིད་ཀྱི་རྣམ་པར༌[^217]ཤེས། །

[Block 527]
ཁམས་གཟུགས་ཀྱི་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་དེར་སྐྱེ་སྟེ། དེའི་ཕྱིར་དེ་ནི་གཟུགས་ཀྱི་རང་བཞིན་གྱི་ཁམས་བཅུ་དང་དེ་དག་ལ་རྟེན་པ༌[^218]དང་དམིགས་པ་རྣམ་པར་ཤེས་པའི་ཁམས་ལྔ་ཡང་མེད་དོ། །

[Block 528 [HEADING]]
#### ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པ། ^1-3-5-0

[Block 529]
ཟག་པ་དང་བཅས་པ་རྣམས་ནི་དུ། ཟག་པ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན། ཡིད་དང་ཆོས་དང་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་གང་དག་བཤད་པ། དེ་གསུམ་ཟག་བཅས་ཟག་པ་མེད། །གང་དག་ལམ་གྱི་བདེན་པ་དང་འདུས་མ་བྱས་ཀྱིས་བསྡུས་པ་དེ་དག་ནི་ཟག་པ་མེད་པ་ཡིན་ནོ། །

[Block 530]
གཞན་དག་ནི་ཟག་པ་དང་བཅས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
