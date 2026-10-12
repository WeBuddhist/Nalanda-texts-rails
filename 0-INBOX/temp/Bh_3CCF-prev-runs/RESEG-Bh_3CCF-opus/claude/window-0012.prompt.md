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
[Block 421]
[^26]: གནས་པ་ཞེས་པ་ ༼སྣར། པེ།༽ གནས་པ་ཞེས་

[Block 422]
[^27]: མཐོང་བ་ནི་ ༼སྣར། པེ།༽ མཐོང་བ་

[Block 423]
[^28]: བརླབ་ ༼པེ།༽ རླབ་

[Block 424]
[^29]: མཐར་ཐུག་པ་ ༼སྣར། པེ།༽ མཐར་ཐུག་པར་

[Block 425]
[^30]: སྟོང་པ་ ༼སྣར། པེ།༽ སྟོང་

[Block 426]
[^31]: བསྒོམ་པའི་ ༼སྣར། པེ།༽ སྒོམ་པའི་

[Block 427]
[^32]: བསྒོམ་པ་ ༼སྡེ།༽ སྒོམ་པ་

[Block 428]
[^33]: རྣམ་པ་ ༼སྣར། པེ།༽ རྣམ་པར་

[Block 429]
[^34]: འགེགས་པ་ ༼སྣར། པེ།༽ འགོག་པ་

[Block 430]
[^35]: པ་ ༼ཅོ།༽ བྱ་བ་

[Block 431]
[^36]: དོན་གྱིས་ ༼སྣར། པེ།༽ དོན་གྱི་

[Block 432]
[^37]: བསྒོམ་པ་ ༼སྣར། པེ།༽ བསྒོམས་པ་

[Block 433]
[^38]: རང་བཞིན་གྱིས་ ༼སྣར། པེ།༽ རང་བཞིན་གྱི་

[Block 434]
[^39]: ཐུགས་ཀྱིས་ ༼སྣར། པེ།༽ ཐུགས་ཀྱི་

[Block 435]
[^40]: མཛད་ཀྱིས་ ༼སྣར། པེ།༽ མཛད་ཀྱི་

[Block 436]
[^41]: གསུམ་པོ་རྣམ་ ༼སྣར། པེ།༽ གསུམ་

[Block 437]
[^42]: པ་ ༼སྣར། པེ།༽ པ་རྣམས་

[Block 438]
[^43]: དེ། ༼སྣར། པེ།༽ དོ།།

[Block 439]
[^44]: བཀོད་པ་ ༼པེ།༽ དཀོད་པ་
[^45]: བྱས་པ་ ༼པེ།༽ བྱ་བ་
[^46]: བཟངས་ ༼སྣར། པེ།༽ བཟང་
[^47]: ཆེན་པོའོ།།

[Block 440]
༼པེ།༽ ཆེན་པོ་
[^48]: རྣམས་ལ་ངེས་ ༼སྣར། པེ།༽ རྣམས་ལངས་
[^49]: བྱེད་པ་ ༼སྣར། པེ།༽ བྱེད་པར་
[^50]: གསུམ་ ༼སྣར། པེ།༽ གསུམ་པོ་
[^51]: བཤད་དོ།།

[Block 441]
༼སྣར། པེ།༽ བཤད་དེ་

[Block 442]
[^52]: ཆོས་ཅན་ ༼སྣར། པེ།༽ ཆོས་

[Block 443]
[^53]: པའོ། ༼སྣར། པེ།༽ ལའོ།

[Block 444]
[^54]: སྔགས་ཀྱི་ ༼པེ།༽ སྔགས་ཀྱིས་

[Block 445]
[^55]: ཉིད་དོ། ༼སྣར། པེ།༽ ཉིད་དེ།

[Block 446]
[^56]: ཡེ་ཤེས་སོ་ཞེས་ ༼སྣར། པེ།༽ ཡེ་ཤེས་

[Block 447]
[^57]: སོ་སོ་ ༼སྣར། པེ།༽ སོ་སོར་

[Block 448]
[^58]: བྱ་བའོ། ༼པེ།༽ བྱའོ།

[Block 449]
[^59]: སོ་སོ་ ༼སྣར། པེ།༽ སོ་སོར་

[Block 450]
[^60]: རིམ་པར་ ༼སྣར། པེ།༽ རིམ་པ་

[Block 451]
[^61]: འདོད་པ་ཅིག་ ༼སྣར། པེ།༽ འདོད་པ་གཅིག་

[Block 452]
[^62]: རྣམས་ཀྱིས་ ༼སྣར། པེ།༽ རྣམས་ཀྱི་

[Block 453]
[^63]: སྣ་ཚོགས་པའི་དགའ་བས་གདུལ་བྱ་སྣ་ཚོགས་ ༼པེ།༽ སྣ་ཚོགས་

[Block 454]
[^64]: སྔགས་ཀྱི་ ༼སྣར། པེ།༽ སྔགས་ཀྱིས་

[Block 455]
[^65]: སྤེལ་བ་ ༼སྣར། པེ།༽ སྤེལ་

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
--- END BLOCKS ---
