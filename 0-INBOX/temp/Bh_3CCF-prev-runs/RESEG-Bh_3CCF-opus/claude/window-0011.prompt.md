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
[Block 386]
ནམ་མཁའི་གཏོས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་མངོན་པར་རྟོགས་པའི་རིམ་པས་བསྟན་པ་ཡིན་པར་བརྗོད་དོ།།

[Block 387]
འདིའི་དོན་ནི་རྡོ་རྗེ་སེམས་དཔའ་ཆུར་ཞུ་བའི་འོད་ཟེར་གྱིས་སེམས་ཅན་ཐམས་ཅད་ལ་རེག་པས་དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱས་པའི་ས་བསྒུལ་བའི་དེ་མ་ཐག་པར་ཀུན་བཞེངས་པར་གྱུར་ཏེ། དེ་བཞིན་གཤེགས་པ་རྡོ་རྗེ་འཛིན་པའི་སྤྱོད་པ་ལ་བཅོམ་ལྡན་འདས་ཉམས་སུ་བསྟར་ནས་བཞུགས་པ་ན༌[^160]ངོ་མཚར་དུ་ཆེའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བརྗོད་པ་ཡིན་ནོ།།

[Block 388]
དེ་ལྟར་བསྟན་པ་མཛད་ནས་གསུང་གི་རྡོ་རྗེ་ལ་བསྟོད་པར་མཛད་པ་རྡོ་རྗེ་ཆོས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟོན་ཏོ།།

[Block 389]
རྡོ་རྗེ་ཆོས་ཞེས་བྱ་བའི་ཚིག་ནི་ཕྱག་ན་རྡོ་རྗེ་ལ་བྱ་བ་ཡིན་ནོ།།

[Block 390]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་བཅུ་བདུན་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 391 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 392 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 393]
སློབ་དཔོན་ལེགས་ལྡན་བྱེད༌[^161]ཀྱིས་མཛད་པ་སྒྲོན་མ་གསལ་བར་བྱེད་པའི་རྡོ་རྗེའི༌[^162]ཚིག་གི་དཀའ་བ་བཏུས་ཏེ་བཤད་པ་ཞེས་བྱ་བ་རྫོགས་སོ།།།།

[Block 394 [HEADING]]
### འགྱུར་བྱང། ^b-2-0

[Block 395]
རྒྱ་གར་གྱི་མཁན་པོ་རྒྱལ་བ་མཆོག་གི་ཞལ་སྔ་ནས༌[^163]དང་།།བོད་ཀྱི་ལོ་ཙཱ་བ་དགེ་སློང་དཔལ་ཤཱཀྱ་བརྩོན་འགྲུས་ཀྱིས་མཉན་ནས་བསྒྱུར་ཞིང་ཞུས་ཏེ་གཏན་ལ་ཕབ་པ།།[^164] །།

[Block 396]
[^1]: བཀླགས་པ་ ༼པེ།༽ ཀླགས་པ་

[Block 397]
[^2]: ཅན་གྱི་ ༼པེ།༽ ཅན་གྱིས་

[Block 398]
[^3]: ཤེས་རབ་ ༼སྣར། པེ།༽ ཤེས་རབ་དང་ཤེས་རབ་

[Block 399]
[^4]: བྱ་བ་ ༼པེ།༽ བྱ་

[Block 400]
[^5]: གཉིས་པོ་ནི་ཚིག་ ༼སྣར། པེ།༽ གཉིས་པོ་

[Block 401]
[^6]: སྒྲུབ་ ༼སྣར།༽ བསྒྲུབ་

[Block 402]
[^7]: བདག་གི་ ༼སྣར། པེ།༽ བདག་གིས་

[Block 403]
[^8]: དེ་དག་ཀྱང་ ༼སྣར། པེ།༽ དེ་དག་ཡང་

[Block 404]
[^9]: རྣམས་ ༼སྣར། པེ།༽ ནམ་

[Block 405]
[^10]: བཞུགས་ ༼སྣར། པེ།༽ བཞུགས་པས་

[Block 406]
[^11]: འཛིན་ ༼སྣར། པེ།༽ འཛིན་འཛིན་

[Block 407]
[^12]: ཞུགས་པ་ ༼སྣར། པེ།༽ བཞུགས་པ་

[Block 408]
[^13]: དེ་ནས་ནི་ ༼སྣར། པེ།༽ དེ་ནས་

[Block 409]
[^14]: སྐྱེ་ ༼སྣར། པེ།༽ སྐྱེས་

[Block 410]
[^15]: སྟོན་པའི་ ༼སྣར། པེ།༽ སྟོང་པའི་

[Block 411]
[^16]: སྲུང་བའི་ ༼སྣར། པེ།༽ བསྲུང་བའི་

[Block 412]
[^17]: མདུན་ ༼སྣར། པེ།༽ བདུན་

[Block 413]
[^18]: ཚོགས་པ་ལ་ ༼སྣར། པེ།༽ ཚོགས་པ་

[Block 414]
[^19]: རྣམས་ཉིད་ ༼སྣར། པེ།༽ རྣམས་

[Block 415]
[^20]: ཞུགས་པ་ ༼སྣར། པེ།༽ བཞུགས་པ་

[Block 416]
[^21]: གསུམ་གྱི་ ༼པེ།༽ གསུམ་གྱིས་

[Block 417]
[^22]: དབྱེ་བ་ ༼སྣར། པེ།༽ བདེ་བ་

[Block 418]
[^23]: འཛིན་པ་ ༼སྣར། པེ།༽ འཛིན་

[Block 419]
[^24]: དེ་ནི་ ༼པེ།༽ དེའི་

[Block 420]
[^25]: སྲོག་ ༼སྡེ།༽ སོག་

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
--- END BLOCKS ---
