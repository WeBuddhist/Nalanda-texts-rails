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
[Block 386]
འདིའི་དོན་ནི་རྡོ་རྗེ་སེམས་དཔའ་ཆུར་ཞུ་བའི་འོད་ཟེར་གྱིས་སེམས་ཅན་ཐམས་ཅད་ལ་རེག་པས་དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ཐོབ་པར་བྱས་པའི་ས་བསྒུལ་བའི་དེ་མ་ཐག་པར་ཀུན་བཞེངས་པར་གྱུར་ཏེ། དེ་བཞིན་གཤེགས་པ་རྡོ་རྗེ་འཛིན་པའི་སྤྱོད་པ་ལ་བཅོམ་ལྡན་འདས་ཉམས་སུ་བསྟར་ནས་བཞུགས་པ་ན༌[^160]ངོ་མཚར་དུ་ཆེའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བརྗོད་པ་ཡིན་ནོ། །

[Block 387]
དེ་ལྟར་བསྟན་པ་མཛད་ནས་གསུང་གི་རྡོ་རྗེ་ལ་བསྟོད་པར་མཛད་པ་རྡོ་རྗེ་ཆོས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟོན་ཏོ། །

[Block 388]
རྡོ་རྗེ་ཆོས་ཞེས་བྱ་བའི་ཚིག་ནི་ཕྱག་ན་རྡོ་རྗེ་ལ་བྱ་བ་ཡིན་ནོ། །

[Block 389]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་བཅུ་བདུན་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།། །།

[Block 390 [HEADING]]
## མཇུག་བྱང། ^a-0

[Block 391 [HEADING]]
### མཛད་བྱང། ^a-1-0

[Block 392]
སློབ་དཔོན་ལེགས་ལྡན་བྱེད༌[^161]ཀྱིས་མཛད་པ་སྒྲོན་མ་གསལ་བར་བྱེད་པའི་རྡོ་རྗེའི༌[^162]ཚིག་གི་དཀའ་བ་བཏུས་ཏེ་བཤད་པ་ཞེས་བྱ་བ་རྫོགས་སོ།། །།

[Block 393 [HEADING]]
### འགྱུར་བྱང། ^a-2-0

[Block 394]
རྒྱ་གར་གྱི་མཁན་པོ་རྒྱལ་བ་མཆོག་གི་ཞལ་སྔ་ནས༌[^163]དང་། །བོད་ཀྱི་ལོ་ཙཱ་བ་དགེ་སློང་དཔལ་ཤཱཀྱ་བརྩོན་འགྲུས་ཀྱིས་མཉན་ནས་བསྒྱུར་ཞིང་ཞུས་ཏེ་གཏན་ལ་ཕབ་པ།།[^164] །།

[Block 395]
[^1]: བཀླགས་པ་ ༼པེ།༽ ཀླགས་པ་
[^2]: ཅན་གྱི་ ༼པེ།༽ ཅན་གྱིས་
[^3]: ཤེས་རབ་ ༼སྣར། པེ།༽ ཤེས་རབ་དང་ཤེས་རབ་
[^4]: བྱ་བ་ ༼པེ།༽ བྱ་
[^5]: གཉིས་པོ་ནི་ཚིག་ ༼སྣར། པེ།༽ གཉིས་པོ་
[^6]: སྒྲུབ་ ༼སྣར།༽ བསྒྲུབ་
[^7]: བདག་གི་ ༼སྣར། པེ།༽ བདག་གིས་
[^8]: དེ་དག་ཀྱང་ ༼སྣར། པེ།༽ དེ་དག་ཡང་
[^9]: རྣམས་ ༼སྣར། པེ།༽ ནམ་
[^10]: བཞུགས་ ༼སྣར། པེ།༽ བཞུགས་པས་
[^11]: འཛིན་ ༼སྣར། པེ།༽ འཛིན་འཛིན་
[^12]: ཞུགས་པ་ ༼སྣར། པེ།༽ བཞུགས་པ་
[^13]: དེ་ནས་ནི་ ༼སྣར། པེ།༽ དེ་ནས་
[^14]: སྐྱེ་ ༼སྣར། པེ།༽ སྐྱེས་
[^15]: སྟོན་པའི་ ༼སྣར། པེ།༽ སྟོང་པའི་
[^16]: སྲུང་བའི་ ༼སྣར། པེ།༽ བསྲུང་བའི་
[^17]: མདུན་ ༼སྣར། པེ།༽ བདུན་
[^18]: ཚོགས་པ་ལ་ ༼སྣར། པེ།༽ ཚོགས་པ་
[^19]: རྣམས་ཉིད་ ༼སྣར། པེ།༽ རྣམས་
[^20]: ཞུགས་པ་ ༼སྣར། པེ།༽ བཞུགས་པ་
[^21]: གསུམ་གྱི་ ༼པེ།༽ གསུམ་གྱིས་
[^22]: དབྱེ་བ་ ༼སྣར། པེ།༽ བདེ་བ་
[^23]: འཛིན་པ་ ༼སྣར། པེ།༽ འཛིན་
[^24]: དེ་ནི་ ༼པེ།༽ དེའི་
[^25]: སྲོག་ ༼སྡེ།༽ སོག་
[^26]: གནས་པ་ཞེས་པ་ ༼སྣར། པེ།༽ གནས་པ་ཞེས་
[^27]: མཐོང་བ་ནི་ ༼སྣར། པེ།༽ མཐོང་བ་
[^28]: བརླབ་ ༼པེ།༽ རླབ་
[^29]: མཐར་ཐུག་པ་ ༼སྣར། པེ།༽ མཐར་ཐུག་པར་
[^30]: སྟོང་པ་ ༼སྣར། པེ།༽ སྟོང་
[^31]: བསྒོམ་པའི་ ༼སྣར། པེ།༽ སྒོམ་པའི་
[^32]: བསྒོམ་པ་ ༼སྡེ།༽ སྒོམ་པ་
[^33]: རྣམ་པ་ ༼སྣར། པེ།༽ རྣམ་པར་
[^34]: འགེགས་པ་ ༼སྣར། པེ།༽ འགོག་པ་
[^35]: པ་ ༼ཅོ།༽ བྱ་བ་
[^36]: དོན་གྱིས་ ༼སྣར། པེ།༽ དོན་གྱི་
[^37]: བསྒོམ་པ་ ༼སྣར། པེ།༽ བསྒོམས་པ་
[^38]: རང་བཞིན་གྱིས་ ༼སྣར། པེ།༽ རང་བཞིན་གྱི་
[^39]: ཐུགས་ཀྱིས་ ༼སྣར། པེ།༽ ཐུགས་ཀྱི་
[^40]: མཛད་ཀྱིས་ ༼སྣར། པེ།༽ མཛད་ཀྱི་
[^41]: གསུམ་པོ་རྣམ་ ༼སྣར། པེ།༽ གསུམ་
[^42]: པ་ ༼སྣར། པེ།༽ པ་རྣམས་
[^43]: དེ། ༼སྣར། པེ།༽ དོ། །

[Block 396]
[^44]: བཀོད་པ་ ༼པེ།༽ དཀོད་པ་
[^45]: བྱས་པ་ ༼པེ།༽ བྱ་བ་
[^46]: བཟངས་ ༼སྣར། པེ།༽ བཟང་
[^47]: ཆེན་པོའོ། །

[Block 397]
༼པེ།༽ ཆེན་པོ་
[^48]: རྣམས་ལ་ངེས་ ༼སྣར། པེ།༽ རྣམས་ལངས་
[^49]: བྱེད་པ་ ༼སྣར། པེ།༽ བྱེད་པར་
[^50]: གསུམ་ ༼སྣར། པེ།༽ གསུམ་པོ་
[^51]: བཤད་དོ། །

[Block 398]
༼སྣར། པེ།༽ བཤད་དེ་
[^52]: ཆོས་ཅན་ ༼སྣར། པེ།༽ ཆོས་
[^53]: པའོ། ༼སྣར། པེ།༽ ལའོ།
[^54]: སྔགས་ཀྱི་ ༼པེ།༽ སྔགས་ཀྱིས་
[^55]: ཉིད་དོ། ༼སྣར། པེ།༽ ཉིད་དེ།
[^56]: ཡེ་ཤེས་སོ་ཞེས་ ༼སྣར། པེ།༽ ཡེ་ཤེས་
[^57]: སོ་སོ་ ༼སྣར། པེ།༽ སོ་སོར་
[^58]: བྱ་བའོ། ༼པེ།༽ བྱའོ།
[^59]: སོ་སོ་ ༼སྣར། པེ།༽ སོ་སོར་
[^60]: རིམ་པར་ ༼སྣར། པེ།༽ རིམ་པ་
[^61]: འདོད་པ་ཅིག་ ༼སྣར། པེ།༽ འདོད་པ་གཅིག་
[^62]: རྣམས་ཀྱིས་ ༼སྣར། པེ།༽ རྣམས་ཀྱི་
[^63]: སྣ་ཚོགས་པའི་དགའ་བས་གདུལ་བྱ་སྣ་ཚོགས་ ༼པེ།༽ སྣ་ཚོགས་
[^64]: སྔགས་ཀྱི་ ༼སྣར། པེ།༽ སྔགས་ཀྱིས་
[^65]: སྤེལ་བ་ ༼སྣར། པེ།༽ སྤེལ་
[^66]: གོ་རིམས་ ༼སྣར། པེ།༽ གོ་རིམ་
[^67]: རང་བཞིན་ནོ། །

[Block 399]
༼པེ།༽ རང་བཞིན་
[^68]: མཛེས་ཀྱི་ ༼སྣར། པེ།༽ མཛེས་
[^69]: གི་ཞེས་བྱ་བ་ ༼སྣར། པེ།༽ གི་ཞེས་པ་
[^70]: སྲུང་བའི་ ༼སྣར།༽ བསྲུང་བའི་ ༼པེ།༽ གསུང་བའི་
[^71]: རྣམས་ཀྱི་རིམ་པ་ ༼སྣར། པེ།༽ རྣམས་ཀྱི་
[^72]: ཀྱི་ ༼སྣར། པེ།༽ ཀྱི་རིམ་པ་
[^73]: ལ་སོགས་པ་ ༼སྣར། པེ།༽ ལ་སོགས་
[^74]: བཀོད་ ༼པེ།༽ དཀོད་
[^75]: ནི་ ༼པེ།༽ ན་
[^76]: ཨོཾ་གྱི་ ༼སྣར། པེ།༽ ཨོཾ་གྱིས་
[^77]: བླངས་ན་ ༼སྣར། པེ།༽ བླངས་ནས་
[^78]: བསྒོམས་ ༼པེ།༽ བསྒོམ་
[^79]: འབྲེལ་ཏེ། ༼སྣར། པེ།༽ འབྲེལ་ཏོ།
[^80]: བསྒོམས་ ༼སྣར། པེ།༽ བསྒོམ་
[^81]: ཡིད་ཀྱི་ ༼སྣར། པེ།༽ ཡིད་ཀྱིས་
[^82]: རྣམས་ཀྱི་ ༼སྣར། པེ།༽ རྣམས་ཀྱིས་
[^83]: གཞག་པར་ ༼སྣར། པེ།༽ བཞག་པར་
[^84]: ལྡན་པ་ ༼སྣར། པེ།༽ ལྡན་པར་
[^85]: གྲག་པ་ ༼སྣར། པེ།༽ གྲགས་པ་
[^86]: གཞལ་ཡང་ ༼སྣར། པེ།༽ གཞལ་ཡས་
[^87]: ལེན་པའི་ ༼སྣར། པེ།༽ ལེན་པ་ནི་
[^88]: ཆེན་པོའི་ ༼སྣར། པེ།༽ ཆེན་པོ་
[^89]: བསྐྱེད་པ་ ༼སྣར། པེ།༽ བསྐྱེད་
[^90]: ནང་ན་ ༼སྣར། པེ།༽ ནང་ནས་
[^91]: ཐུགས་ལ་ ༼སྣར། པེ།༽ ཐུགས་ལས་
[^92]: སྤྲོས་ ༼སྣར། པེ།༽ སྤྲོས་པ་
[^93]: མཚན་ཉིད་ ༼སྣར། པེ།༽ མཚན་
[^94]: སྟོང་པ་ ༼ཅོ།༽ སྟོང་
[^95]: གྱུར་པས་ ༼སྣར། པེ།༽ འགྱུར་བས་
[^96]: བྱའོ། ༼སྣར། པེ།༽ བྱ་བའོ།
[^97]: སྟེ་ཞེས་བྱ་བ་ ༼སྣར། པེ།༽ སྟེ་ཞེས་པ་
[^98]: བྱ་བའི་ ༼སྣར། པེ།༽ བྱས་པའི་
[^99]: གཞུག་ ༼སྣར། པེ།༽ བཞུགས་
[^100]: བཀྲུ་བར་བྱ་བར་ ༼སྣར། པེ།༽ བཀྲུ་བར་
[^101]: གསང་བ་ ༼སྣར། པེ།༽ བསད་བ་
[^102]: སྣོད་ ༼སྣར། པེ།༽ ནང་
[^103]: རང་བཞིན་གྱིས་ ༼སྣར། པེ།༽ རང་བཞིན་གྱི་
[^104]: འདི་ ༼སྣར། པེ།༽ ནི་
[^105]: བའི་ ༼སྣར། པེ།༽ བར་
[^106]: དི་བ་ ༼སྣར། པེ།༽ དི་པ་
[^107]: ཐ་མར་ ༼སྣར། པེ།༽ མཐའ་མར་
[^108]: གསད་པའི་ ༼སྣར། པེ།༽ བསད་པའི་
[^109]: རྣམས་བཏོན་ཏོ། །

[Block 400]
༼སྣར། པེ།༽ རྣམས་གཏོན་ཏེ་
[^110]: བརླབས་པའི་ ༼སྣར། པེ།༽ བསླབས་པའི་
[^111]: དཔྱད་པར་ ༼སྣར། པེ།༽ བཅད་པར་
[^112]: བྱ་བའོ། ༼པེ།༽ བྱའོ།
[^113]: ཛ་ ༼སྣར། པེ།༽ ཛི་
[^114]: བཀྲི་བར་ ༼སྣར། པེ།༽ དཀྲི་བར་
[^115]: བསམས་པའི་ ༼སྣར། པེ།༽ བསམ་པའི་
[^116]: བསྒྲུབ་ ༼སྣར། པེ།༽ སྒྲུབ་
[^117]: ལུས་སྤོ་ ༼སྣར། པེ།༽ ལུས་པོ་
[^118]: སྤོ་ ༼པེ།༽ པོར་
[^119]: སྡུད་ ༼སྣར། པེ།༽ བསྡུད་
[^120]: བཏབ་པར་ ༼སྣར། པེ།༽ བཏང་བར་
[^121]: གཞག་པར་ ༼སྣར། པེ།༽ བཞག་པར་
[^122]: གཞག་ ༼སྣར། པེ།༽ བཞག་
[^123]: ལ་སོགས་པ་ ༼སྣར། པེ།༽ ལ་སོགས་
[^124]: ལས་ ༼སྣར། པེ།༽ ལ་
[^125]: དང་ ༼སྣར། པེ།༽ པདྨ་
[^126]: བྱ་ ༼པེ།༽ བྱ་བ་
[^127]: གཟུང་ ༼སྣར། པེ།༽ བཟུང་
[^128]: བརླབ་པར་ ༼སྣར།༽ བརླབས་པར་ ༼པེ།༽ རླབས་
[^129]: གནང་བ་ ༼སྣར། པེ།༽ སྣང་བ་
[^130]: འཚམ་ ༼སྣར། པེ།༽ མཚམ་
[^131]: ཆོས་ཉིད་ ༼སྣར། པེ།༽ ཆོས་
[^132]: དེ་བཞིན་དུ་ ༼སྣར། པེ།༽ དེ་བཞིན་
[^133]: ཉི་ ༼སྣར། པེ།༽ ཉིད་
[^134]: དེ་དག་ནི་ ༼སྣར། པེ།༽ དེ་དག་གི་
[^135]: པ་བཟའ་བ་ ༼སྣར། པེ།༽ པའི་དམ་པ་
[^136]: བསྒྲུབས་པས་ ༼སྣར། པེ།༽ བསྒྲུབ་པས་
[^137]: གཟུད་དོ། ༼པེ།༽ གཟུགས་སོ།
[^138]: གཟུང་མ་ ༼སྣར།༽ བཟུང་ལ་ ༼པེ།༽ གཟུང་ལ་
[^139]: གསད་པ་ ༼སྣར། པེ།༽ བསད་པ་
[^140]: ལེན་པ་ ༼སྣར། པེ།༽ ལེན་པར་
[^141]: ཕྱི་རོལ་གྱི་ ༼པེ།༽ ཕྱི་རོལ་གྱིས་
[^142]: ཀྱིས་ ༼སྣར། པེ།༽ ཀྱི་
[^143]: རྒྱན་གྱིས་ ༼སྣར། པེ།༽ བརྒྱན་གྱི་
[^144]: གནས་པར་ ༼སྣར། པེ།༽ གནས་པས་
[^145]: གཞག་པར་ ༼སྣར། པེ།༽ བཞག་པར་
[^146]: རིགས་ ༼སྣར། པེ།༽ རིག་
[^147]: བྱ་བ་ནི་ ༼སྣར། པེ།༽ བྱ་བ་
[^148]: གྱུར་ཏེ། ༼སྣར། པེ།༽ གྱུར་ཏོ།
[^149]: དྲེགས་པ་ ༼སྣར། པེ།༽ དྲེག་པ་
[^150]: རྣམ་པར་ ༼སྣར། པེ།༽ རྣམ་
[^151]: སྩོལ་བ་ ༼པེ།༽ བསྩོལ་བ་
[^152]: མེད་པའི་ཡང་བླ་ན་མེད་ ༼སྣར། པེ།༽ མེད་
[^153]: སློབ་དཔོན་གྱི་ ༼སྣར། པེ།༽ སློབ་དཔོན་གྱིས་
[^154]: སྩོལ་བས་ ༼སྣར། པེ།༽ རྩོལ་བས་
[^155]: བླུགས་ ༼པེ།༽ བླུག་
[^156]: བསམས་ ༼པེ།༽ བསམ་
[^157]: པ་ ༼སྣར། པེ།༽ པས་
[^158]: རྡོ་རྗེ་ཡང་ ༼སྣར། པེ།༽ རྡོ་རྗེ་
[^159]: མནན་པའི་ ༼སྣར། པེ།༽ གནས་པའི་
[^160]: བཞུགས་པ་ན་ ༼སྣར། པེ།༽ བཞུགས་པ་
[^161]: བྱེད་ ༼སྣར།༽ འབྱེད་
[^162]: རྡོ་རྗེའི་ ༼སྣར། པེ།༽ རྡོ་
[^163]: ཞལ་སྔ་ནས་ ༼སྣར། པེ།༽ ཞལ་སྔ་
[^164]: ཞིང་ཞུས་ཏེ་གཏན་ལ་ཕབ་པ། ༼སྣར།༽ ཞིང་གཏན་ལ་ཕཕབ་པ་བཀྲ་ཤིས ༼པེ།༽ ཞིང་གཏན་ལ་ཕཕབ་པ་མངྒཱལཾ།
--- END BLOCKS ---
