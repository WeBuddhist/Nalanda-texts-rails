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
[Block 456 [HEADING]]
#### ཐོགས་པ་དང་བཅས་པ་དང་ཐོགས་པ་མེད་པ། ^1-3-2-0

[Block 457]
ཐོགས་པ་དང་བཅས་པ་རྣམས་ནི་དུ། ཐོགས་པ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན། ཐོགས་དང་བཅས་པ་གཟུགས་ཅན་བཅུ། །གཟུགས་ཀྱི་ཕུང་པོས་བསྡུས་པའི་ཁམས་བཅུ་གང་དག་བཤད་པ་དེ་དག་ནི་ཐོགས་པ་དང་བཅས་པ༌[^185]ཡིན་ཏེ། ཐོགས་པ་ཞེས་བྱ་བ་ནི་རྡུགས་པའོ། །

[Block 458]
དེ་ཡང་རྣམ་པ་གསུམ་སྟེ། སྒྲིབ་པ་དང་ཡུལ་དང་དམིགས་པ་ལ་ཐོགས་པའོ། །

[Block 459 [HEADING]]
##### སྒྲིབ་པ་ལ་ཐོགས་པ། ^1-3-2-1-0

[Block 460]
དེ་ལ་སྒྲིབ་པ་ལ་ཐོགས་པ་ནི་རང་གི་ཡུལ་དུ་གཞན་སྐྱེ་བའི་གེགས་བྱེད་པ་སྟེ། དཔེར་ན་ལག་པ་འམ། རྡོ་བ་ལ་ལག་པ་རྡུགས་ཤིག༌[^186]ཐོགས་པའམ། རྡོ་བ་ཡང་དེ་གཉིས་ལ་ཐོགས་པ་ལྟ་བུའོ། །

[Block 461 [HEADING]]
##### ཡུལ་ལ་ཐོགས་པ། ^1-3-2-2-0

[Block 462]
ཡུལ་ལ་ཐོགས་པ་ནི་མིག་ལ་སོགས་པ་ཡུལ་ཅན་རྣམས་གཟུགས་ལ་སོགས་པ་ཡུལ་རྣམས་ལ་ཐོགས་པ་སྟེ། བཏགས་པ་ལས་ཇི་སྐད་དུ། ཆུ་ལ་ཐོགས་པ་ལ་སྐམ་ལ་མ་ཡིན་པའི་མིག་ཀྱང་ཡོད་དེ། དཔེར་ན་ཉ་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 463]
སྐམ་ཐོགས་ལ་ཆུ་ལ་མ་ཡིན་པ་ཡང་ཡོད་དེ། མི་ཕལ་ཆེ་བའི༌[^187]ལྟ་བུའོ། །

[Block 464]
གཉི་གར་ཐོགས་པ་ཡང་ཡོད་དེ། ཆུ་སྲིན་བྱིས་པ་གསོད་པ་དང་།[^188] སྦལ་བ་དང་། ཤ་ཟ་བ༌[^189]དང་། ཉ་པ༌[^190]ལ་སོགས་པ་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 465]
གཉི་གར་མ་ཡིན་པ་ཡང་ཡོད་དེ། རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 466]
མིག་གང་མཚན་མོ་ཐོགས་ལ་ཉིན་པར་མ་ཡིན་པ་ཡོད་དེ། ཕ་ཝང་དང་། འུག་པ་ལ་སོགས་པ༌[^191]རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 467]
ཉིན་པར་ཐོགས་ལ་མཚན་མོ་མ་ཡིན་པ་ནི་མི་ཕལ་ཆེའི་ལྟ་བུའོ། །

[Block 468]
མཚན་མོ་དང་ཉིན་པར་ཐོགས་པ་ནི་ཁྱི་དང་། ཝ་དང་། རྟ་དང་། གུང་དང་། བྱི་ལ་ལ་སོགས་པ་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 469]
གཉི་གར་ཡང་མ་ཡིན་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ་ཞེས་གསུངས་པ་ལྟ་བུ་སྟེ། འདི་ནི་ཡུལ་ལ་ཐོགས་པའོ། །

[Block 470 [HEADING]]
##### དམིགས་པ་ལ་ཐོགས་པ། ^1-3-2-3-0

[Block 471]
དམིགས་པ་ལ༌[^192]ཐོགས་པ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་རང་གི་དམིགས་པ་དག་ལ་ཐོགས་པའོ། །

[Block 472]
ཡུལ་དང་དམིགས་པ་དག་ལ་བྱེ་བྲག་ཅི་ཡོད་ཅེ་ན། གང་ལ་གང་ཞིག་བྱེད་པ་དེ་ནི་ཡུལ་ཡིན་ལ། གང་ཞིག་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱིས་འཛིན་པ་དེ་ནི་དམིགས་པ་ཡིན་ནོ། །

[Block 473]
ཡང་ཇི་ལྟར་ན་རང་གི་ཡུལ་ལ༌[^193]དམིགས་པ་ལ་འཇུག་པ་ལ་ཐོགས་པ་ཞེས་བྱ་ཞེ་ན། དེ་ལས་གཞན་དུ་མི་འཇུག་པའི་ཕྱིར་རོ། །

[Block 474]
ཡང་ན་འདི་ལ་གཏོད་པ་ནི་ཐོགས་པ་ཡིན་ཏེ། རང་གི་ཡུལ་ལ་འཇུག་པ་གང་ཡིན་པའོ། །

[Block 475]
དེ་ལྟ་བས་ན་འདིར་བཅུ་པོ་དག་ནི་སྒྲིབ་པ་ལ་ཐོགས་པས་ཐོགས་པ་དང་བཅས་པ་ཉིད་དུ་རིག་པར་བྱ་སྟེ། ཕན་ཚུན་སྒྲིབ་པའི་ཕྱིར་རོ། །

[Block 476]
ཆོས་གང་དག་ཡུལ་ལ༌[^194]ཐོགས་པས་ཐོགས་པ་དང་བཅས་པ་དེ་དག་སྒྲིབ་པ་ལ་ཐོགས་པས་ཀྱང་ཡིན་ནམ་ཞེ་ན། མུ་བཞི་སྟེ། མུ་དང་པོ་ནི་སེམས་ཀྱི་ཁམས་བདུན་དག་དང་། ཆོས་ཀྱི་ཁམས་ཀྱི་ཕྱོགས་མཚུངས་པར་ལྡན་པ་གང་ཡིན་པའོ། །

[Block 477]
གཉིས་པ་ནི་ཡུལ་ལྔ་པོ་དག་གོ། །

[Block 478]
གསུམ་པ་ནི་དབང་པོ་ལྔ་དག་གོ། །

[Block 479]
བཞི་པ་ནི་མཚུངས་པར་ལྡན་པ་མ་གཏོགས་པ༌[^195]ཆོས་ཀྱི་ཁམས་ཀྱི་ཕྱོགས་སོ། །

[Block 480]
གང་དག་ཡུལ་ལ་ཐོགས་པས་ཐོགས་པ་དང་བཅས་པ་དེ་དག་ཉིད་དམིགས་པ་ལ་ཐོགས་པས་ཀྱང་ཡིན་ནམ་ཞེ་ན། ཚིག་ཕྱི་མ་དང་སྦྱོར་བ་སྟེ། རེ་ཞིག་དམིགས་པ་ལ་ཐོགས་པ༌[^196]གང་དག་ཡིན་པ་དེ་དག་ནི་ཡུལ་ལ་ཐོགས་པས་ཀྱང་ཡིན་ནོ། །

[Block 481]
ཡུལ་ལ་ཐོགས་པས་ཡིན་ལ་དམིགས་པ་ལ་ཐོགས་པས་མ་ཡིན་པ་ཡང་ཡོད་དེ་དབང་པོ་ལྔ་རྣམས་སོ། །

[Block 482]
བཙུན་པ་གཞོན་ནུ་ལན༌[^197]ན་རེ་ནི་གང་ལ་ཡིད་སྐྱེ་བར་འདོད་པ་ལ་གཞན་དག་གིས་ཐོགས་པར་བྱེད༌[^198]ནུས་པ་དེ་ནི་ཐོགས་པ་དང་བཅས་པ་ཡིན་པར་ཤེས་པར་བྱ་ལ། བཟློག་པ་ནི་ཐོགས་པ་མེད་པར་འདོད་དོ་ཞེས་ཟེར་རོ། །

[Block 483]
ཐོགས་པ་དང་བཅས་པ་དག་བཤད་ཟིན་ཏོ། །

[Block 484 [HEADING]]
#### དགེ་བ་ལ་སོགས་པའི་དངོས་པོ། ^1-3-3-0

[Block 485]
ཁམས་བཅོ་བརྒྱད་པོ་དེ་དག་ལས་དགེ་བ་རྣམས་ནི་དུ། མི་དགེ་བ་རྣམས་ནི་དུ། ལུང་དུ་མ་བསྟན་པ་རྣམས་ནི་དུ་ཞེ་ན། ལུང་མ་བསྟན་བརྒྱད། བརྒྱད་པོ་དག་གང་ཞེ་ན། ཐོགས་པ་དང་བཅས་པ་བཅུ་བཤད་པ་གང་དག་ཡིན་པ། དེ་དག་ཉིད། གཟུགས་སྒྲ་མ་གཏོགས་དབང་པོ་ལྔ་རྣམས་དང་། དྲི་དང་རོ་དང་རེག་བྱའི་ཁམས་རྣམས་དང་བརྒྱད་པོ་དེ་དག་ནི་དགེ་བ་དང་མི་དགེ་བའི་ངོ་བོར་ལུང་བསྟན་དུ་མེད་པའི་ཕྱིར་ལུང་དུ་མ་བསྟན་པ་དག་གོ། །

[Block 486]
གཞན་དག་ན་རེ་ནི༌[^199]རྣམ་པར་སྨིན་པའི་ཕྱིར་ལུང་བསྟན་དུ་མེད་པའི་ཕྱིར༌[^200]ཞེས་ཟེར་ཏེ། དེ་ལྟར༌[^201]ན་ནི་ཟག་པ་མེད་པ་ལ་ཐལ་བར་འགྱུར་རོ། །

[Block 487]
གཞན་རྣམ་གསུམ། གཞན་ཁམས་བཅུ་པོ་དག་ནི་དགེ་བ་དང་མི་དགེ་བ་དང༌[^202]ལུང་དུ་མ་བསྟན་པ་ཡང་ཡིན་ཏེ། དེ་ལ་སེམས་ཀྱི་ཁམས་བདུན་མ་ཆགས་པ་ལ་སོགས་པ་དང་མཚུངས་པར་ལྡན་པ་དག་ནི་དགེ་བ་ཡིན་ནོ། །

[Block 488]
ཆགས་པ་ལ་སོགས་པ་དང་མཚུངས་པར་ལྡན་པ་དག་ནི་མི་དགེ་བ་ཡིན་ནོ། །

[Block 489]
གཞན་དག་ནི་ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 490]
ཆོས་ཀྱི་ཁམས་ནི་མ་ཆགས་པ་ལ་སོགས་པའི་ངོ་བོ་ཉིད་དང་མཚུངས་པར་ལྡན་པ་དང་། ཀུན་ནས་བསླང་བ་དང་། སོ་སོར་བརྟགས་པས་འགོག་པ་ནི་དགེ་བའོ། །

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
--- END BLOCKS ---
