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
[Block 526]
འདོད་དེ། དེ་ལ་སེམས་ཀྱི་རྟེན་ནི་དབང་པོ་དྲུག་དག་ཡིན་ཏེ། སྐྱེ་མཆེད་དྲུག་པོ་ཡང་སེམས་ཅན་གྱི་རྫས་ཀྱི་གཞི་ཡིན་ནོ། །

[Block 527]
མོ་དང་ཕོའི་དབང་པོ་དག་གིས་ནི་དེ་མོ་དང་ཕོར་བྱེ་བྲག་ཏུ་འབྱེད་དོ། །

[Block 528]
སྲོག་གི་དབང་པོས་ནི་གནས་པར་བྱེད་དོ། །

[Block 529]
ཚོར་བ་རྣམས་ཀྱིས་ནི་ཀུན་ནས་ཉོན་མོངས་པར་བྱེད་དོ། །

[Block 530]
དད་པ་ལ་སོགས་པ་ལྔས་ནི་རྣམ་པར་བྱང་བ་ལ་སོགས་པའི་ཚོགས་སོག༌[^212]པར་བྱེད་དོ། །

[Block 531]
གསུམ་གྱིས་ནི་རྣམ་པར་བྱང་བར་བྱེད་དེ། དེའི་ཕྱིར་མ་རིག་པ་ལ་སོགས་པ་ནི་དབང་པོ་ཉིད་དུ་མི་འདོད་དོ། །

[Block 532 [VERSE]]
ཡང་ན་འཇུག་པའི་རྟེན་དང་ནི། །
སྐྱེ་དང་གནས་དང་ཉེར་སྤྱོད་ལས། །
བཅུ་བཞི་དེ་བཞིན་ལྡོག་པ་ལ། །
དབང་པོ་རྣམས་ནི་གཞན་ཡིན་ནོ། །

[Block 533]
འཇུག་པའི་རྟེན་ནི་དབང་པོ་དྲུག་ཡིན་ནོ། །

[Block 534]
སྐྱེ་བ་ནི་མོ་དང་པོའི་དབང་པོ་དག་ལས་ཏེ། དེ་ལས་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 535]
གནས་པ་ནི་སྲོག་གི་དབང་པོ་སྟེ། དེས་གནས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 536]
ཚོར་བ་རྣམས་ཀྱིས་ནི་ཉེ་བར་སྤྱོད་པར་བྱེད་དེ། དེའི་ཕྱིར་དེ་དག་ནི་དབང་པོ་བཅུ་བཞི་ཡིན་ནོ། །

[Block 537]
རྣམ་པ་དེ་ཉིད་ཀྱིས་གཞན་དག་ནི་ལྡོག་པ་ཡིན་ནོ། །

[Block 538]
གང་གི་ཕྱིར་ལྡོག་པའི་རྟེན་ནི་དད་པ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 539]
སྐྱེ་བ་ནི་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ཡིན་ནོ། །

[Block 540]
གནས་པ་ནི་ཀུན་ཤེས་པའི་དབང་པོ་ཡིན་ནོ།[^213] །

[Block 541]
ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོས་ནི་ཉེ་བར་སྤྱོད་པར་བྱེད་དོ། །

[Block 542]
དེའི་ཕྱིར་དབང་པོ་དག་ནི་དེ་སྙེད་ཅིག་ཡིན་ལ། དེ་ཉིད༌[^214]ཀྱི་ཕྱིར་དེ་དག་གི་གོ་རིམས་ཀྱང་དེ་ཡིན་ནོ། །

[Block 543]
དེ་ལ་དབང་པོ་གང་དག་གཞན་དུ་མ་བསྟན་པ་དེ་དག་བསྟན་ཏེ། ལུས་ཚོར་སིམ་པ་མ་ཡིན་གང་། །སྡུག་བསྔལ་དབང་པོའོ། །

[Block 544]
སིམ་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་གནོད་པར་བྱེད་པའོ། །

[Block 545]
སིམ་པ་ནི་བདེ་བའོ། །

[Block 546]
ལུས་ཀྱི་ཚོར་བ་སིམ་པ་ནི་བདེ་བའི་དབང་པོའོ། །

[Block 547]
སིམ་པ་ཞེས་བྱ་བ་ནི་ཕན་འདོགས་པ་སྟེ། བསམ་གཏན་གསུམ་པ་ན། སེམས་ཀྱི་དེ་ནི་བདེ་དབང་པོ། །བསམ་གཏན་གསུམ་པ༌[^215]ནི་སེམས་ཀྱི་ཚོར་བ་སིམ་པ་དེ་ཉིད་བདེ་བའི་དབང་པོའོ། །

[Block 548]
གཞན་ན་དེ་ཡིད་བདེ་བ་ཡིན། །བསམ་གཏན་གསུམ་པ་ལས་གཞན་པ་འདོད་པའི་ཁམས་དང་བསམ་གཏན་དང་པོ་དང༌[^216]

[Block 549]
གཉིས་པ་ན་ནི་སེམས་ཀྱི་ཚོར་བ་སིམ་པ་གང་ཡིན་པ་དེ་ནི་ཡིད་བདེ་བའི་དབང་པོ་ཡིན་ནོ། །

[Block 550 [VERSE]]
སེམས་ཀྱི་ཚིམ་པ༌[^217]མ་ཡིན་པ། །
ཡིད་མི་བདེ་བའོ་བཏང་སྙོམས་ནི། །

[Block 551]
བར་མའོ། །

[Block 552]
སིམ་པ་ཡང་མ་ཡིན་སིམ་པ་མ་ཡིན་པ་ཡང་མ་ཡིན་པ་ནི་བར་མ་ཞེས་བརྗོད་དེ་བཏང་སྙོམས་ཀྱི་དབང་པོའོ། །ཅི་ལུས་ཀྱིའམ་སེམས་ཀྱི་ཞེས་བྱ་ཞེ་ན། སྨྲས་པ། གཉིས་གའི༌[^218]ཡིན་ནོ། །

[Block 553]
ཅིའི་ཕྱིར་འདི་བསྡུས་ནས་དབང་པོ་གཅིག་ཏུ་བྱས་ཤེ་ན། མི་རྟོག་ཕྱིར། སེམས་ཀྱི་བདེ་བ་དང་སྡུག་བསྔལ་བ་ནི་ཕལ་ཆེར་རྣམ་པར་རྟོག་པ་ལས་སྐྱེའི་ལུས་ཀྱིས༌[^219]ནི་མ་ཡིན་ནོ། །

[Block 554]
ཡུལ་གྱི་དབང་གིས་ནི་དགྲ་བཅོམ་པ་རྣམས་ལ་ཡང་སྐྱེ་བས་དེའི་ཕྱིར་དེ་དག་དབང་པོ་ཉིད་དུ་ཐ་དད་ཀྱི་ལུས་ཀྱི་དང་སེམས་ཀྱི་བཏང་སྙོམས་ནི་རྣམ་པར་མི་རྟོག་པ་ཁོ་ནར་རང་གི་ངང་གིས་སྐྱེ་བས་ལུས་ཀྱི་དང་སེམས་ཀྱི་ཞེས་བྱ་བ་དབང་པོ་གཅིག་ཏུ་བྱས་སོ། །

[Block 555]
མཐོང་བསྒོམ་མི་སློབ་ལམ་ལ་དགུ། །གསུམ་ཡིན། ཡིད་དང་བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་རྣམས་དང་། དད་པ་ལ་སོགས་པ་ལྔ་དང་། དབང་པོ་དགུ་པོ་དེ་དག་ནི་མཐོང་བ་དང་། བསྒོམ་པ་དང་། མི་སློབ་པའི་ལམ་དག་ལ་དབང་པོ་གསུམ་དུ་བརྗོད་དོ། །

[Block 556]
མཐོང་བའི་ལམ་ལ་ནི་མི་ཤེས་པ་ཀུན་ཤེས་པར་བྱེད་པ་ཞེས་བྱའོ། །

[Block 557]
བསྒོམ་པའི་ལམ་ལ་ནི་ཀུན་ཤེས་པ་ཡིན་ཏེ། ཕྲ་རྒྱས༌[^220]ལྷག་མ་སྤང་བའི་ཕྱིར་རོ། །

[Block 558]
མི་སློབ་པའི་ལམ་ལ་ནི་ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་ཡིན་ཏེ། དེའི་ངང་ཚུལ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 559 [HEADING]]
#### རྣམ་པའི་བྱེ་བྲག། ^2-1-2-0

[Block 560]
དབང་པོ་དེ་དག་ལ་ཟག་པ་དང་བཅས་པ་ནི་དུ། ཟག་པ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན། གསུམ་ནི་དྲི་མ་མེད། ཀུན་ཤེས་བྱེད་པའི་དབང་པོ་ལ་སོགས་པ་གསུམ་བཤད་མ་ཐག་པ་དེ་ནི་ཟག་པ་མེད་པ་ཡིན་ཏེ། དྲི་མ་རྣམས་ནི་ཟག་པའི་རྣམ་གྲངས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 561]
གཟུགས་ཅན་སྲོག་དང་སྡུག་བསྔལ་དག །ཟག་པ་དང་བཅས། དབང་པོ་གཟུགས་ཅན་བདུན་དང་། སྲོག་གི་དབང་པོ་དང་། སྡུག་བསྔལ་དང་ཡིད་མི་བདེ་བའི་དབང་པོ་དག་ནི་གཅིག་ཏུ་ཟག་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 562]
དགུ་རྣམ་གཉིས། ཡིད་དང་། བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་དག་དང་། དད་པ་ལ་སོགས་པ་ལྔ་དང་། དབང་པོ་དགུ་པོ་དེ་དག་ནི་ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པ་དག་གོ། །

[Block 563]
རྣམ་པར་སྨིན་པ་ཡིན་པ༌[^221]རྣམས་ནི་དུ། མ་ཡིན་པ་རྣམས་ནི་དུ་ཞེ་ན། རེ་ཞིག་གཅིག་ཏུ། སྲོག་ནི་རྣམ་སྨིན་བཅུ་གཉིས་གཉིས། །བཅུ་གཉིས་གང་ཞེ་ན། ཐ་མ་བརྒྱད་དང་ཡིད་མི་བདེ། མ་གཏོགས་པ་སྟེ། དད་པ་ལ་སོགས་པ་ཐ་མ་བརྒྱད་དང་། ཡིད་མི་བདེ་བ༌[^222]མ་གཏོགས་པ་སྲོག་གི་དབང་པོ་ལས་གཞན་བཅུ་གཉིས་ནི་རྣམ་པ་གཉིས་ཏེ། རྣམ་པར་སྨིན་པ་དང་། རྣམ་པར་སྨིན་པ་མ་ཡིན་པའོ། །

[Block 564]
དེ་ལ་མིག་ལ་སོགས་པ་བདུན་རྒྱས་པ་ལས་བྱུང་བ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་མ་ཡིན་ནོ། །

[Block 565]
ལྷག་མ་རྣམས་ནི་རྣམ་པར་སྨིན་པའོ། །
--- END BLOCKS ---
