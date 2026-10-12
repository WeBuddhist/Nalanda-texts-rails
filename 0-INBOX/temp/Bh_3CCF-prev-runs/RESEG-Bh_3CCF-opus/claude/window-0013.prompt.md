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
[^66]: གོ་རིམས་ ༼སྣར། པེ།༽ གོ་རིམ་

[Block 457]
[^67]: རང་བཞིན་ནོ།།

[Block 458]
༼པེ།༽ རང་བཞིན་

[Block 459]
[^68]: མཛེས་ཀྱི་ ༼སྣར། པེ།༽ མཛེས་

[Block 460]
[^69]: གི་ཞེས་བྱ་བ་ ༼སྣར། པེ།༽ གི་ཞེས་པ་

[Block 461]
[^70]: སྲུང་བའི་ ༼སྣར།༽ བསྲུང་བའི་ ༼པེ།༽ གསུང་བའི་

[Block 462]
[^71]: རྣམས་ཀྱི་རིམ་པ་ ༼སྣར། པེ།༽ རྣམས་ཀྱི་

[Block 463]
[^72]: ཀྱི་ ༼སྣར། པེ།༽ ཀྱི་རིམ་པ་

[Block 464]
[^73]: ལ་སོགས་པ་ ༼སྣར། པེ།༽ ལ་སོགས་

[Block 465]
[^74]: བཀོད་ ༼པེ།༽ དཀོད་

[Block 466]
[^75]: ནི་ ༼པེ།༽ ན་

[Block 467]
[^76]: ཨོཾ་གྱི་ ༼སྣར། པེ།༽ ཨོཾ་གྱིས་

[Block 468]
[^77]: བླངས་ན་ ༼སྣར། པེ།༽ བླངས་ནས་

[Block 469]
[^78]: བསྒོམས་ ༼པེ།༽ བསྒོམ་

[Block 470]
[^79]: འབྲེལ་ཏེ། ༼སྣར། པེ།༽ འབྲེལ་ཏོ།

[Block 471]
[^80]: བསྒོམས་ ༼སྣར། པེ།༽ བསྒོམ་

[Block 472]
[^81]: ཡིད་ཀྱི་ ༼སྣར། པེ།༽ ཡིད་ཀྱིས་

[Block 473]
[^82]: རྣམས་ཀྱི་ ༼སྣར། པེ།༽ རྣམས་ཀྱིས་

[Block 474]
[^83]: གཞག་པར་ ༼སྣར། པེ།༽ བཞག་པར་

[Block 475]
[^84]: ལྡན་པ་ ༼སྣར། པེ།༽ ལྡན་པར་

[Block 476]
[^85]: གྲག་པ་ ༼སྣར། པེ།༽ གྲགས་པ་

[Block 477]
[^86]: གཞལ་ཡང་ ༼སྣར། པེ།༽ གཞལ་ཡས་

[Block 478]
[^87]: ལེན་པའི་ ༼སྣར། པེ།༽ ལེན་པ་ནི་

[Block 479]
[^88]: ཆེན་པོའི་ ༼སྣར། པེ།༽ ཆེན་པོ་

[Block 480]
[^89]: བསྐྱེད་པ་ ༼སྣར། པེ།༽ བསྐྱེད་

[Block 481]
[^90]: ནང་ན་ ༼སྣར། པེ།༽ ནང་ནས་

[Block 482]
[^91]: ཐུགས་ལ་ ༼སྣར། པེ།༽ ཐུགས་ལས་

[Block 483]
[^92]: སྤྲོས་ ༼སྣར། པེ།༽ སྤྲོས་པ་

[Block 484]
[^93]: མཚན་ཉིད་ ༼སྣར། པེ།༽ མཚན་

[Block 485]
[^94]: སྟོང་པ་ ༼ཅོ།༽ སྟོང་

[Block 486]
[^95]: གྱུར་པས་ ༼སྣར། པེ།༽ འགྱུར་བས་

[Block 487]
[^96]: བྱའོ། ༼སྣར། པེ།༽ བྱ་བའོ།

[Block 488]
[^97]: སྟེ་ཞེས་བྱ་བ་ ༼སྣར། པེ།༽ སྟེ་ཞེས་པ་

[Block 489]
[^98]: བྱ་བའི་ ༼སྣར། པེ།༽ བྱས་པའི་

[Block 490]
[^99]: གཞུག་ ༼སྣར། པེ།༽ བཞུགས་

[Block 491]
[^100]: བཀྲུ་བར་བྱ་བར་ ༼སྣར། པེ།༽ བཀྲུ་བར་

[Block 492]
[^101]: གསང་བ་ ༼སྣར། པེ།༽ བསད་བ་

[Block 493]
[^102]: སྣོད་ ༼སྣར། པེ།༽ ནང་

[Block 494]
[^103]: རང་བཞིན་གྱིས་ ༼སྣར། པེ།༽ རང་བཞིན་གྱི་

[Block 495]
[^104]: འདི་ ༼སྣར། པེ།༽ ནི་
--- END BLOCKS ---
