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
[Block 141]
གསང་བ་སྒྲོགས་པ་དང་། ཕུང་པོ་སྨོད་པ་དང་།

[Block 142 [VERSE]]
དག་པའི་ཆོས་ལ་ཡིད་གཉིས་དང་། །
མིང་སོགས་བྲལ་ལ་དེར་རྟོག་དང་། །

[Block 143]
སེམས་སུན་འབྱིན་པ་དང་། དམ་ཚིག་མི་བསྟེན་པ་དང་། ཤེས་རབ་སྨོད་པ་དེ་རྣམས་སྤངས་པས་ཁྱད་པར་གྱི་བྱང་ཆུབ་ཀྱི་སེམས་མི་ཉམས་པར་བྱེད་པའོ། །

[Block 144]
ཡང་དེ་ནི་ལྟ་སྤྱོད་སྒོམ༌[^75]གསུམ་གྱི་རང་བཞིན་ཡང་ཡིན་ཏེ། ཆོས་ལ་ཡིད་གཉིས་དང་། མིང་སོགས་བྲལ་ལ་དེར་རྟོག་སྤངས་པས་ལྟ་བ་རྣམ་གཉིས༌[^76]རྟོགས་པའོ། །

[Block 145]
དང་པོ་དང་གཉིས་པ་དང་གསུམ་པ་དང་བཞི་པ་དང་ལྔ་པ་དང་དྲུག་པ་དང་བདུན་པ་དང་བརྒྱད་པ་དང༌[^77]བཅུ་པའི་དགུ་སྤངས་པས་སྒོམ་པའི༌[^78]མན་ངག་དང་། སེམས་སུན་འབྱིན་པ་དང་། དམ་ཚིག་མི་བསྟེན་པ༌[^79]དང་། ཤེས་རབ་སྨོད་པ་གསུམ་གྱིས༌[^80]དགུ་སྤངས་ཤིང་སྦྱངས་པས་སྤྱོད་པའོ། །

[Block 146]
དེ་གསུམ་མ་སྤངས་པར་བསྒོམས་པས་བཀའ་འདའ༌[^81]དང་། བླ་མ་བརྙས་པ་མ་སྤངས་པ་ཡིན་ནོ། །

[Block 147]
དེ་བས་ན་བཅུ་དང་ལྔ་བཅུ་ལ་ནན་ཏན་ཡང་དང་ཡང་དུ་བྱ་སྟེ་དངོས་གྲུབ་ཐམས་ཅད་ཀྱི་རྩ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 148]
ཉམས་ན་ཉེས་པ་ཐམས་ཅད་ཀྱང་འབྱུང་ངོ་། །དེ་ལྟར༌[^82]མ་ཡིན་པར་སྔགས་ཚིག་ཙམ་གྱིས་མན་ངག་བསྟན་ནས། །བླ་མར་ཁས་འཆེ་བ་ལྟུང་བའི་སྣོད་དུ་བསྒྲུབས་ན་མི་དགེ་བའི་རྒྱུ་བྱས་པས།[^83] མི་དགེ་བའི་བདག་པོའི་རྐྱེན་ཞེས་བྱ། སྡིག་པའི་གྲོགས་པོ་དང་། བདུད་སྡིག་ཅན་དང་། སླུ་བར་བྱེད་པ་ཞེས་བྱ་སྟེ་སྐྱོན་མང་དུ་མི་བརྗོད་དོ། །

[Block 149]
དེ་ལྟ་བུའི་བླ་མ་དང་སློབ་མ་དེ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཀྱི་ཆོས་ཀྱི་ཕུང་པོ་རྣམས་རྙེད་པ༌[^84]དང་བཀུར་སྟིའི་རྒྱུས༌[^85]བསྒྲུབས་པས་ངན་སོང་སྒྲུབ་པའི་ཐབས་དང་རྐྱེན་དེས་དུག་དང་བདུད་རྩི་འདྲེས་པ་དང་འདྲའོ། །

[Block 150]
དེ་བས་ན་བླ་མ་དམ་པ་བསྟེན་པ་གཅེས་པར་རྡོ་རྗེ་འཆང་ཆེན་པོས་གསུངས་སོ། །

[Block 151 [HEADING]]
## བསྔོ་བ། ^a-0

[Block 152 [VERSE]]
དམ་པའི་གྲོགས་དང་བླ་མ་དང་། །
མ་ཕྲད་སྲིད་པར་འཁྱམས་པ་ལས། །
ཕན་ཕྱིར་བླ་མའི་ལུང་བཞིན་དུ། །
བྲིས་པས་དེ་དག་ལ་ཕན་ཤོག །

[Block 153 [VERSE]]
འདི་མཐོང་ཙམ་གྱིས་སྐྱེ་བོ་རྣམས། །
ཆོས་ལ་ནན་ཏན་བྱ་བའི་རྒྱུར། །
གྱུར་ནས་བླ་མ་གཙོར་བྱེད་ཅིང་། །
སྒྲུབ༌[^86]ལ་ནན་ཏན་བྱེད་པའི་རྒྱུར། །

[Block 154 [VERSE]]
སྐལ་ངན་སྐྱེ་བོ་རྣམས་དང་ཕྲད་པ་ན། །
རང་སྐྱོན་དབང་གིས་སྨོད་པར་བྱེད་མོད་ཀྱི། །
དྲང་སྲོང་ཆེན་པོའི་ལུང་ནི་སུ་ཞིག་སྤོང་། །
དེ་ཕྱིར་དེ་དག་ལ་ཡང་གནོད༌[^87]མ་གྱུར། །

[Block 155 [VERSE]]
གསང་བ་བླ་ན་མེད་པ་ཡི། །
རྡོ་རྗེ་ཐེག་པའི་སྒོར་ཞུགས་པའི། །
རྣལ་འབྱོར་པ་རྣམས་བསླབ༌[^88]པའི་ཕྱིར། །
གསལ་བྱེད་མན་ངག་བཀོད་པའོ། །

[Block 156 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 157 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 158]
གསང་སྔགས་རྡོ་རྗེ་ཐེག་པའི་རྣལ་འབྱོར་པ་རྣམས་ཀྱི་བསླབ་པ་གསལ་བར་བྱེད་པའི་མན་ངག་ཅེས་བྱ་བ་སློབ་དཔོན་རྒྱལ་བའི་ལྷས་མཛད་པའི་རྩ་བའི་ལྟུང་བའི་འགྲེལ་པ་མཁས་པ་ཆེན་པོ་དཱི་པཾ་ཀཱ་ར་ཤྲཱི་ཛྙཱ་ནའི་ཞལ་སྔ་ནས་གསུངས་པ་རྫོགས་སོ།། །།

[Block 159 [HEADING]]
### འགྱུར་བྱང། ^b-2-0

[Block 160]
པཎྜི་ཏ་དེ་ཉིད་དང་ལོ་ཙཱ་བ་དགེ་སློང་ཚུལ་ཁྲིམས་རྒྱལ་བས་བསྒྱུར་བའོ།། །།

[Block 161]
[^1]: རྒྱུ་ ༼སྣར། པེ།༽ རྒྱུད་
[^2]: གཅིག ། ༼སྣར། པེ།༽ གཅིགགོ། །
[^3]: ལོག་པར་ ༼སྣར། པེ།༽ ལོག་པ་
[^4]: ཡོན་ ༼སྣར། པེ།༽ ཡོན་ཏན་
[^5]: ལྡན་པའི་ ༼སྣར། པེ།༽ ལྡང་བའི་
[^6]: བྱང་ཆུབ་ཀྱི་ ༼སྣར། པེ།༽ བྱང་ཆུབ་
[^7]: གཟུང་བར་ ༼སྣར། པེ།༽ བཟུང་བར་
[^8]: བྱས་ནས་ ༼སྣར། པེ།༽ བྱས་
[^9]: འབྲངས་ ༼སྣར། པེ།༽ འབྲང་
[^10]: དེ་ ༼སྣར། པེ།༽ དེས་
[^11]: པ་ ༼སྣར། པེ།༽ ས་
[^12]: བསྟབས་པ་ ༼སྣར། པེ།༽ བསྟན་པ་
[^13]: བཀུར་བྱེད་ ༼སྣར། པེ།༽ བསྐུར་ཞེས་
[^14]: གྱུར་པས་ ༼སྣར། པེ།༽ གྱུར་ནས་
[^15]: པ་སྟེ། ༼སྣར། པེ།༽ ནས་ནི།
[^16]: འདྲེན་མི་ ༼སྣར། པེ།༽ འདྲེན་མ་
[^17]: བསྒྲུབ་པ་ ༼སྣར། པེ།༽ སྒྲུབས་པ་
[^18]: བསྟན་ ༼སྣར།༽ བསྟེན་
[^19]: ལྟུང་བར་ ༼སྣར།༽ ལྷུང་བར་
[^20]: བྱམས་ ༼སྣར། པེ།༽ སྦྱངས་
[^21]: འདོད་པ་ ༼སྣར། པེ།༽ འདོགས་པ་
[^22]: བློ་ ༼སྣར།༽ གློ་
[^23]: སྟོབས་ཀྱིས་ ༼སྣར། པེ།༽ སྟོབས་ཀྱི་
[^24]: བསྐྱེད་པའི་ ༼སྣར། པེ།༽ སྐྱེད་པའི་
[^25]: བསགས་ ༼སྣར། པེ།༽ གསགས་
[^26]: བསྲུངས་པས་ ༼སྣར། པེ།༽ བསྲུངས་པ་
[^27]: མཚན་ ༼སྣར། པེ།༽ ཚན་
[^28]: བསྐྱེད་པའི་ ༼སྣར། པེ།༽ སྐྱེད་པའི་
[^29]: གོ་རིམས་ ༼སྣར། པེ།༽ གོ་རིམ་
[^30]: ཕུང་བ་ ༼སྣར། པེ།༽ འཕུང་བ་
[^31]: འབྱུང་བས་ ༼སྣར། པེ།༽ འབྱུང་བར་
[^32]: བསྲུང་བར་ ༼སྣར། པེ།༽ བསྲུངས་པར་
[^33]: གདུག་པ་ ༼སྣར། པེ།༽ གདུགས་པ་
[^34]: གྱི་སྦྱོར་ ༼ཅོ།༽ གྱི་སོར་
[^35]: བསྟེན་པ་ ༼སྣར། པེ།༽ སྟེན་པ་
[^36]: བརྟག་པར་ ༼སྣར། པེ།༽ བརྟགས་པར་
[^37]: དེ་ ༼སྣར། པེ།༽ དེའི་
[^38]: བསྒྲུབ་པར་ ༼སྣར། པེ།༽ སྒྲུབ་པར་
[^39]: གཞུག་གོ། ༼སྣར། པེ།༽ གཞུགས་སོ།
[^40]: བརྟེན་ ༼སྣར། པེ།༽ བརྟན་
[^41]: བསྒྲུབ་ ༼སྣར། པེ།༽ སྒྲུབ་
[^42]: རྟོག་པ་ ༼སྣར། པེ།༽ རྟོགས་པ་
[^43]: དེ་ཡང་ ༼སྣར། པེ།༽ དེ་ཡང་དང་པོ་བསྐྱེད་པའི་རིམ་པ་དང་སྦྱར་ཏེ་དེ་ཡང་
[^44]: བསགས། ༼སྣར། པེ།༽ བསགས་པས།
[^45]: གོ་རིམས་ ༼སྣར། པེ།༽ གོ་རིམ་
[^46]: རབ་ཀྱིས་ ༼སྣར། པེ།༽ རབ་ཀྱི་
[^47]: ཟློག་ ༼སྣར། པེ།༽ བཟློག་
[^48]: བླངས་པས་ ༼སྣར། པེ།༽ སྤངས་པས་
[^49]: མཉམ་གཞག་གི་ ༼པེ།༽ མཉམ་གཞིག་
[^50]: ལས་ ༼སྣར། པེ།༽ ལ་
[^51]: གཞིའི་ ༼སྣར། པེ།༽ བཞིའི་
[^52]: བྱམས་ ༼སྣར། པེ།༽ བྱམས་དང་
[^53]: བར་དུ་ ༼སྣར། པེ།༽ བར་དུ་བར་
[^54]: རྣམ་པ་ ༼སྣར། པེ།༽ རྣམས་པ་
[^55]: ཤེས་བཞིན་གྱིས་ ༼ཅོ།༽ ཤེས་བཞིན་གྱི་
[^56]: བསྒྲུབ་ ༼སྣར། པེ།༽ སྒྲུབ་
[^57]: ཟུང་འཇུག་ཏུ་ ༼སྣར། པེ།༽ ཟུང་དུ་འཇུག་པ་
[^58]: བླ་མ་དམ་ཚིག་ཉམས་པ་ ༼སྣར། པེ།༽ དམ་ཚིག་ཉམས་
[^59]: སྦྱང་བ་ ༼སྣར། པེ།༽ སྦྱོང་བ་
[^60]: བསླབས་པས་ ༼སྣར། པེ།༽ བརླབས་པས་
[^61]: ནི་ལམ་རིམ་ ༼ཅོ།༽ ནི་ལམ་
[^62]: ལུས་ ༼པེ།༽ ལུང་
[^63]: གོ་རིམས་ ༼སྣར། པེ།༽ གོ་རིམ་
[^64]: དེ་མ་བསྒོམས་ ༼སྣར། པེ།༽ དེ་བསྒོམ་
[^65]: ལགས་ ༼སྣར། པེ།༽ ལས་
[^66]: རྟོག་པ་ ༼སྣར། པེ།༽ རྟོགས་པ་
[^67]: རྟོག་པ་ ༼སྣར། པེ།༽ རྟོགས་པ་
[^68]: བྱེད་པ་ ༼སྣར། པེ།༽ བྱེད་པས་
[^69]: རྟོགས་པ་ ༼སྣར། པེ།༽ རྟོག་པ་
[^70]: རྟོགས་པས་ ༼སྣར། པེ།༽ རྟོག་པས་
[^71]: བཤེས་ ༼སྣར། པེ།༽ གཤེས་
[^72]: བལྟས་ ༼སྣར། པེ།༽ ལྟས་
[^73]: གཉིས་ཀ་མི་ ༼སྣར།༽ གཉིས་ཀ་མ་
[^74]: གདུག་ལ་ ༼ཅོ།༽ གདུག་པ་ ༼སྣར། པེ།༽ གདུགས་པ་
[^75]: སྒོམ་ ༼སྣར། པེ།༽ བསྒོམ་
[^76]: རྣམ་གཉིས་ ༼སྣར། པེ།༽ རྣམས་ཉིད་
[^77]: བརྒྱད་པ་དང་ ༼སྣར། པེ།༽ བརྒྱད་པ་
[^78]: སྒོམ་པའི་ ༼སྣར། པེ།༽ བསྒོམ་པའི་
[^79]: བསྟེན་པ་ ༼སྣར། པེ།༽ སྟེན་པ་
[^80]: གསུམ་གྱིས་ ༼སྣར། པེ།༽ གསུམ་གྱི་
[^81]: འདའ་ ༼སྣར། པེ།༽ འདས་
[^82]: དེ་ལྟར་ ༼སྣར། པེ།༽ དེ་ལྟ་
[^83]: བྱས་པས། ༼སྣར། པེ།༽ བྱས་པ་བས།
[^84]: རྙེད་པ་ ༼སྣར། པེ།༽ བརྙེད་པ་
[^85]: རྒྱུས་ ༼སྣར། པེ།༽ རྒྱུད་
[^86]: སྒྲུབ་ ༼སྣར། པེ།༽ བསྒྲུབ་
[^87]: ཡང་གནོད་ ༼སྣར། པེ།༽ འང་སྣོད་
[^88]: བསླབ་ ༼སྣར། པེ།༽ སླབ་
--- END BLOCKS ---
