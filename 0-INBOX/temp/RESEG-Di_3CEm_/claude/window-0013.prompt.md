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
བླ་ན་མེད་པའི་སྨོན་ལམ་རིན་པོ་ཆེ༌[^316]ཐོབ་པ་ནི་རབ་ཏུ་རྙེད་པ་སྟེ། བདེ་བར་འཚོ་བ་རྙེད་པ་ཡང་སྨོན་ལམ་རིན་པོ་ཆེ་འདི་ལྟ་བུ་ཐོབ་པས༌[^317]སོ། །

[Block 457]
དེ་ལྟ་བས་ན༌[^318]ཚེའི་མཆོག་ཐོབ་པར་བྱ་བའི་དངོས་པོ་ཐོབ་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 458 [VERSE]]
མི་ཚེ་འདིར་ཡང་དེ་དག་ལེགས་པར་འོངས།[^319] །
ཞེས་བྱ་བ་ནི་དགེ་བར་འོངས་པའོ། །
ཀུན་དུ་བཟང་པོ་དེ་ཡང་ཅི་འདྲ་བར། །

[Block 459]
ཞེས་བྱ་བ་ནི་དེ་ལྟར་རིང་པོར་མི་ཐོགས་པར་འགྱུར་བའོ། །

[Block 460]
ལས་ཀྱི་སྒྲིབ་པ་ཡོངས་སུ་འབྱང་བའི་ཡོན་ཏན་ནི་རྣམ་པ་བཞི་པ་སྟེ། དེ་ཡང་གང་ཞེ་ན། མཚམས་མེད་ལྔ་པོ་དག་གི་སྡིག་པ་རྣམས། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 461]
སྡིག་པ་མཚམས་མེད་པ་ལྔ་ནི་མ་བསད་པ་ལ་སོགས་པའོ། །

[Block 462]
གང་གིས་མི་ཤེས་དབང་གིས་བྱས་པ་དག །ཅེས་བྱ་བ་ནི་མི་ཤེས་པའི་རྩ་བ་ལས་བྱུང་བའི་ཕྱིར་འདོད་ཆགས་ལ་སོགས་པ་གཞན་དག་ལ་ཡང་མི་ཤེས་པའི་དབང་གིས་ཞེས་བྱ་བའོ། །

[Block 463]
དེའི་ཀུན་དུ་བཟང་པོ༌[^320]སྤྱོད་པའི་སྨོན་ལམ་འདི་གོང་མ༌[^321]བཞིན་དུ་བཟུང་ནས་དད་པའི་ཆུས་སེམས་བརླན་པར་བྱས་ཏེ་བརྗོད་པ་དང་། འཆད་པ་དང་། མོས་པར་བྱེད་པ་དང་། ཀློག་པ་དང་། འཆང་བ་དང་། སྒོམ་པ་རྣམས་བྱས་ན་མཚམས་མེད་པའི་སྡིག༌[^322]པ་ཡང་མྱུར་དུ་མ་ལུས་པར་ཡོངས་སུ་བྱང་བར་འགྱུར་རོ། །

[Block 464 [HEADING]]
#### ཚེ་ཕྱི་མའི་ཡོན་ཏན། ^2-10-2-0

[Block 465]
ཚེ་ཕྱི་མའི་ཡང་རྣམ་པ་གཉིས་ཏེ། རྒྱུས་བསྡུས་པ་དང་འབྲས་བུས་བསྡུས་པའོ། །

[Block 466]
དེ་ལ་རྒྱུས་བསྡུས་པ་ནི་ཡེ་ཤེས་དང་། མཚན་དང་དཔེ་བྱད་ཀྱིས་ལུས་བརྒྱན་པ་དང་། ནད་མེད་པའི་མཆོག་གི་མཚན་རྣམས་ཏེ། དེ་ཡང་གང་ཞེ་ན། ཡེ་ཤེས་དང་ནི་གཟུགས་དང་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 467]
ཡེ་ཤེས་ཞེས་བྱ་བ་ནི་ཤེས་པ་སྟེ། སྤྱོད་པ་ཐམས་ཅད་དང་ལྡན་པའོ། །

[Block 468]
གཟུགས་ཞེས་བྱ་བ་ནི་གཟུགས་ཡིད་འཕྲོག་པའོ། །

[Block 469]
མཚན་ཞེས་བྱ་བ་ནི་སྐྱེས་བུ་ཆེན་པོའི་མཚན་སུམ་ཅུ༌[^323]གཉིས་དབུའི་གཙུག་ཏོར་ལ་སོགས་པའོ། །

[Block 470]
མཚན་གྱི་འཁོར་དཔེ་བྱད་ཡིན་པས་ན་དེ་དང་ཡང་ལྡན་པར་རིག་པར་བྱའོ། །

[Block 471]
རིགས་དང༌[^324]ཞེས་བྱ་བ་ནི་བྲམ་ཟེ་དང་རྗེའུ་རིགས་ལ་སོགས་པ་གཞན་དག་ཀྱང་ངོ་། །ཁ་དོག་ཅེས་བྱ་བ་ནི་རུས་ཆེན་པོ་བཙུན་པ་རྣམས་སོ། །

[Block 472 [VERSE]]
ལྡན་པར་ཞེས་བྱ་བ་ནི་ཀུན་དང་ལྡན་པའོ། །
འགྱུར་ཞེས་བྱ་བ་ནི་དེ་ལྟར་འགྱུར་བའོ། །
བདུད་དང་མུ་སྟེགས་མང་པོས་དེ་མི་ཐུབ། །

[Block 473]
ཅེས་བྱ་བ་ནི་བདུད་མང་པོ་དང་མུ་སྟེགས་ཅན་མང་པོས་མི་ཚུགས་ཤིང་ཟིལ་གྱིས༌[^325]མི་ནོན་པའོ། །

[Block 474]
མཆོད་པར་གྱུར་ཅིག་ཅེས་བྱ་བ་ནི་ཁམས་གསུམ་པ་ཐམས་ཅད་ཀྱིས་མཆོད་པར་གྱུར༌[^326]ཅིག་པ་སྟེ། གང་གིས་ཀུན་དུ་བཟང་པོའི་སྤྱོད་པ་སྨོན་ལམ་འཛིན་ཅིང་སྟོན་པའོ།[^327] །

[Block 475]
འབྲས་བུས་བསྡུས་པ་ནི་བྱང་ཆུབ་ཀྱི་སྙིང་པོར་སོང་བ་དང་། སེང་གེའི་གདན་ལ་བཞུགས་པར་བསྟན་པ་དང་། བདུད་རྣམས་རབ་ཏུ་བཏུལ་བ་དང་། མངོན་པར་བྱང་ཆུབ་པ་སྟེ། ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་ལ་སོགས་པའི་མཚན་ཉིད་དོ། །དེ་ཡང་གང་ཞེ་ན། བྱང་ཆུབ་ཤིང་དབང་དྲུང་དུ་དེ་མྱུར་འགྲོ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། བཟང་པོ་སྤྱོད་པ་བླ་ན་མེད་པ་འདིས་ཤིན་ཏུ་བསགས་པའི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱིས་མྱུར་དུ་འགྲོའོ། །

[Block 476]
བྱང་ཆུབ་ཤིང་དབང་དྲུང་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་ཤིང་དབང་གི་དྲུང་དུའོ། །

[Block 477]
སོང་ནས༌[^328]ཀྱང་སྐྱིལ་མོ་ཀྲུང་བཅས་ཏེ་སེང་གེའི་གདན་ལ་འགྲོ་བ་ཐམས་ཅད་ལ་བདེ་ཞིང་ཕན་པའི་ཕྱིར་འདུག་ནས་བདུད་སྡེ་དང་བཅས་པར་བཏུལ་ཏེ། དེ་ནས་བླ་ན་མེད་པ་ཡང་དག་པར་བྱང་ཆུབ་ཏུ༌[^329]སངས་རྒྱས་ནས་བླ་ན་མེད་པའི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་མཛད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 478]
མདོར་ན་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་མ་ལུས་པར་བསྟན་ཏོ། །དེ་ཡང་གང་ཞེ་ན། གང་ཡང་བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་འདི། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 479]
གང་གིས་བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་འདི་འཆང་བ་དང་། སྟོན་པ་དང་། ཀློག་པའི་རྣམ་པར་སྨིན་པ་ནི་སུ་གང་གིས་ཤེས་ཤེ་ན། ཉན་ཐོས་དང་། རང་སངས་རྒྱས་ལ་སོགས་པ་གཞན་གྱིས་ནི་མ་ཡིན་ཏེ། གཙོ་བོ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^330]མཁྱེན་ཏེ། སྨོན་ལམ་རིན་པོ་ཆེའི་རྣམ་པར་སྨིན་པ༌[^331]ཇི་ལྟར་མཁྱེན་ཅེ་ན། བྱང་ཆུབ་མཆོག་ལ་ཞེས་བྱ་བ་སྟེ། བླ་ན་མེད་པའི་བྱང་ཆུབ་མཆོག་གི་འབྲས་བུའོ། །

[Block 480]
འཇིག་རྟེན་གྱི་ཕུན་སུམ་ཚོགས་པའི་ཡོན་ཏན་ཡང་མ་ལུས་པར་འདིར་བཤད༌[^332]པར་རིག་པར་བྱ་སྟེ། འཇིག་རྟེན་གྱི་ཕུན་སུམ་ཚོགས་པའི་ཡོན་ཏན་ནི་འདིའི་ཞར་གྱིས་འབྱུང་བར་རིག་པར་བྱའོ། །

[Block 481]
དེ་བས་ན་སྨོན་ལམ་འདི་ལ་དོགས་པ་དང་སོམ་ཉི༌[^333]མ་བྱེད་ཅིག་ཅེས་བྱའོ།[^334] །

[Block 482 [HEADING]]
### བསྔོ་བ་བསྟན་པ། ^2-11-0

[Block 483]
ད་ནི་བསྔོ་བ་བསྟན་པ་ཞེས་བྱ་བ་སྟེ། འཇམ་དཔལ་དཔའ་བོས་ཇི་ལྟར་མཁྱེན་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 484]
འཇམ་དཔལ་གྱིས་ཇི་ལྟར་མཁྱེན་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་ཀུན་དུ་བཟང་པོས་ཀྱང་དེ་བཞིན་དུ་སྟེ། དགེ་བའི་ཕུང་པོ་འདི་དག་ཐམས་ཅད་དེ་དག་གི༌[^335]རྗེས་སུ་བསྔོ་ཞིང་སློབ་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་བསྔོ་བའོ། །

[Block 485]
འདི་ནི་དེ་བཞིན་གཤེགས་པའི་བསྔོ་བ་སྟེ། དུས་གསུམ་གཤེགས་པའི༌[^336]རྒྱལ་བ་བ༌[^337]ཐམས་ཅད་ཀྱིས། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 486]
དུས་གསུམ་གཤེགས་པའི་རྒྱལ་བ་བཅོམ་ལྡན་འདས་ཐམས་ཅད་ཀྱིས་བླ་ན་མེད་པ་མཆོག་ཏུ་བསྔོ་བར་བསྔགས་ཤིང་བསྟོད་པ་སྟེ། དེ་ལྟར་བདག་གིས་བསྔོ་བ་ནི་བླ་ན་མེད་པ་མཆོག་ཀུན་དུ་བཟང་པོའི་སྤྱོད་པའི་དགེ་བའི་ཚོགས་འདི་ཀུན་ཀྱང་དེ་ལྟར་རོ། །

[Block 487]
འདི་ལ་ཚིགས་སུ་བཅད་པ་ཕྱེད་ཀྱིས་ནི་སྡིག་པའི་སྒྲིབ་པ་སྤོང་བའོ། །

[Block 488]
ཕྱེད་ཀྱིས་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་མཐུན་པའི་ལུས་ཡོངས་སུ་གཟུང༌[^338]བའོ། །དེ་ཡང་གང་ཞེ་ན། བདག་ནི་འཆི་བའི་དུས་བྱེད་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 489]
འཆི་བར་བྱེད་པ་ནི་འཆི་བ་སྟེ། འཆི་བའི་དུས་སུ་བཟང་པོ་སྤྱོད་པ་ལ་གང་གིས་བསྒྲིབས༌[^339]པར་འགྱུར་བའི་སྒྲིབ་པ་དེ༌[^340]ཐམས་ཅད་ཕྱིར་བསལ༌[^341]བའོ། །

[Block 490]
མངོན་པར་མཐོང་ཞེས་བྱ་བ་ནི་བཅོམ་ལྡན་འདས་སྣང་བ་མཐའ་ཡས་མངོན་སུམ་དུ་མཐོང་བའོ། །

[Block 491]
དེར་ཞེས་བྱ་བ་ནི་བདེ་བ་ཅན་གྱི་འཇིག་རྟེན་དུ་འགྲོ་བ་ལ་བྱའོ། །

[Block 492]
དེར་སོང་ནས༌[^342]ཞེས་བྱ་བ་ནི་བདེ་བ་ཅན་གྱི་སངས་རྒྱས་ཀྱི་ཞིང་དེར་སོང་བ་སྟེ། ཇི་ལྟར་སྨྲས་པ་བཞིན་སྨོན་ལམ་དུ་གདབ་པ༌[^343]དེ་ཀུན་བདག་གིས་མངོན་སུམ་དུ་རྫོགས་པར་གྱུར་ཅིག་པའོ། །

[Block 493]
དེ་དག་མ་ལུས་བདག་གིས་ཡོངས་སུ་བསྐང་། །ཅེས་བྱ་བ་ནི། སེམས་ཅན་ཐམས་ཅད་ལ་འདི་ལྟ་བུ་ཕན་པར་བྱ་བའོ། །ཇི་སྲིད་དུ་ཞེ་ན། འཇིག་རྟེན་ཇི་སྲིད་ཅེས་བྱ་བ་སྟེ། འཇིག་རྟེན་ཇི་སྲིད་པར་འགྲོ་བ་རྣམས་ཀྱི་དོན་བྱ་བའོ། །

[Block 494]
ལྷག་མ་ནི་ལུང་བསྟན་པ་ཐོབ་པ་དང་། སེམས་ཅན་གྱི་དོན་སྒྲུབ་པ་སྟེ། གང་ཞེ་ན། རྒྱལ་བའི་དཀྱིལ་འཁོར་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། རྒྱལ་བའི་དཀྱིལ་འཁོར་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་འཁོར་འདུས་པའོ། །

[Block 495]
བཟང་པོ་ཞེས་བྱ་བ་ནི་མཛེས་པའོ། །
--- END BLOCKS ---
