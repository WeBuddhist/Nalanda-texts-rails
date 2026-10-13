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
[Block 36]
དོན་ཡིན་ཕྱི་རོལ་གྱི་དོན་མེད་བཞིན་དུ་ཕྱི་རོལ་ལྟ་བུར་སྣང་བ་ནང་ན་ཡོད་པ་ཁོ་ན་དམིགས་པའི་རྐྱེན་ཡིན་ནོ། །

[Block 37]
རྣམ་ཤེས་ངོ་བོའི་ཕྱིར། །དེ་རྐྱེན་ཉིད་ཀྱང་ཡིན་ཕྱིར་རོ། །

[Block 38]
ནང་གི་རྣམ་པར་ཤེས་པ་ནི་དོན་དུ་སྣང་བ་དང་། དེ་ལས་སྐྱེས་པ་ཡིན་པས། ཆོས་ཉིད་གཉིས་དང་ལྡན་པའི་ཕྱིར་ནང་ན་ཡོད་པ་ཁོ་ན་དམིགས་པའི་རྐྱེན་ཡིན་ནོ། །

[Block 39 [HEADING]]
### ཚིགས་བཅད་བདུན་པ། ^1-7-0

[Block 40]
རེ་ཞིག་དེ་ལྟར་སྣང་བ་ཉིད་ཡིན་ལ་ནི་རག་ལ། [^16]དེའི་ཕྱོགས་གཅིག་པོ་ལྷན་ཅིག་སྐྱེས་པ་གོ་ཇི་ལྟར་རྐྱེན་ཡིན་ཞེ་ན། གཅིག་ནའང་མི་འཁྲུལ་ཕྱིར་ན་རྐྱེན། །ལྷན་ཅིག་པར་གྱུར་དུ་ཟིན་ཀྱང་འཁྲུལ་པ་མེད་པའི་ཕྱིར་གཞན་ལས་སྐྱེ་བའི༌[^17]རྐྱེན་དུ་འགྱུར་ཏེ། འདི་ལྟར་གཏན་ཚིགས་ཡོད་པ་དང་མེད་པ༌[^18]དག་ནི་ཡོད་པ་དང་མེད་པ་དག་གི་དེ་དང་ལྡན་པ་ཉིད་ན༌[^19]རྒྱུ༌[^20]དང་ལྡན་པ་རིམ་གྱིས་སྐྱེ་བ་དག་གི་ཡང་མཚན་ཉིད་ཡིན་པར་སྨྲའོ། །

[Block 41]
ཡང་ན། ནུས་པ་འཇོག་ཕྱིར་རིམ་གྱིས་ཡིན། །རིམ་གྱིས་ཀྱང་ཡིན་ཏེ། དོན་དུ་སྣང་བས༌[^21]དེ་ནི་རང་སྣང་བ་དང་མཐུན་པའི་འབྲས་བུ་སྐྱེད་པར་བྱེད་པར༌[^22]ནུས་པ། རྣམ་པར་ཤེས་པའི་རྟེན་ཅན་བྱེད་པས་མི་འགལ་ལོ། །

[Block 42]
གལ་ཏེ་འོ་ན་ནི༌[^23]ནང་གི་གཟུགས་ཁོ་ན་དམིགས་པའི་རྐྱེན་ཡིན་ན། ཇི་ལྟར་དེ་དང་མིག་ལ་བརྟེན་ན༌[^24]མིག་གི་རྣམ་པར་ཤེས་པ་སྐྱེ་ཞེ་ན།

[Block 43 [VERSE]]
ལྷན་ཅིག་བྱེད་དབང་ནུས་པ་ཡི།[^25] །
ངོ་བོ་གང་ཡིན་དབང་པོའང་ཡིན། །

[Block 44]
དབང་པོ་ནི་རང་གི་འབྲས་བུ་ལས་ནུས་པའི་ངོ་བོ་ཉིད་དུ་རྗེས་སུ་དཔག་གི་འབྱུང་བ་ལས་གྱུར་པ་ཉིད་དུ་ནི་མ་ཡིན་ནོ། །

[Block 45 [HEADING]]
### ཚིགས་བཅད་བརྒྱད་པ། ^1-8-0

[Block 46]
དེ་ཡང་རྣམ་རིག་ལ་མི་འགལ། །ནུས་པའི་རྣམ་པར་ཤེས་པ་ལ་ཡོད་ཀྱང་རུང་། བསྟན་དུ་མེད་པའི་རང་གི་ངོ་བོ་ལ་ཡོད་ཀྱང་རུང་སྟེ། འབྲས་བུ་སྐྱེད་པ༌[^26]ལ་ཁྱད་པར་མེད་དོ། །

[Block 47 [VERSE]]
དེ་ལྟར་ཡུལ་གྱི་ངོ་བོ་དང་། །
ནུས་པ་ཕན་ཚུན་རྒྱུ་ཅན་དང་། །
ཐོག་མ་མེད་དུ་འཇུག་པ་ཡིན། །

[Block 48]
མིག་ཅེས་བྱ་བའི་ནུས་པ་དང་། ནང་གི་གཟུགས་ལ་བརྟེན༌[^27]ནས་རྣམ་པར་ཤེས་པ་དོན་དུ་སྣང་བ་དམིགས་ཀྱིས་མ་བསྟན་པ༌[^28]སྐྱེའོ། །

[Block 49]
འདི་གཉིས་ཀྱང་ཕན་ཚུན་གྱི་རྒྱུ་ཅན་དང་། ཐོག་མ་མེད་པའི་དུས་ཅན༌[^29]ཡིན་ཏེ། རེས་འགའ༌[^30]ན་ནུས་པ་ཡོངས་སུ་སྨིན་པ་ལས་རྣམ་པར་ཤེས་པས༌[^31]ཡུལ་གྱི་རྣམ་པ་ཉིད༌[^32]འབྱུང་ལ་རེས་འགའ་ནི་དེའི་རྣམ་པ་ལ་ནུས་པའོ། །

[Block 50]
རྣམ་པར་ཤེས་པ་ལས༌[^33]དེ་གཉིས་གཞན་ཉིད་དང་གཞན་མ་ཡིན་པ་ཉིད་དུ་ཅི་དགར་བརྗོད་པར་བྱའོ། །

[Block 51]
དེ་ལྟར་ནང་གི་དམིགས་པ་ནི་ཆོས་ཉིད་གཉིས་དང་ལྡན་པའི་ཕྱིར་ཡུལ་དུ་མཐོང་ངོ་།[^34] །

[Block 52 [HEADING]]
## མཇུག་བྱང། ^a-0

[Block 53 [HEADING]]
### མཛད་བྱང། ^a-1-0

[Block 54]
དམིགས་པ་བརྟགས༌[^35]པའི་འགྲེལ་པ་སློབ་དཔོན་ཕྱོགས་ཀྱི་གླང་པོས་མཛད་པའོ།[^36] །

[Block 55]
[^1]: དེ་ ༼སྣར། པེ།༽ དེའི་
[^2]: ཤེས་པས་གང་གིས་ ༼སྣར། པེ།༽ ཤེས་པས་
[^3]: དག་གི་ ༼སྣར། པེ།༽ དག་
[^4]: ཉིད་ཀྱིས་ ༼སྣར། པེ།༽ ཉིད་ཀྱི་
[^5]: འདུས་པ་ ༼སྣར། པེ།༽ འདུས་བྱས་
[^6]: བློ་ཡི་ ༼སྣར། པེ།༽ བློ་ཡིས་
[^7]: ཐམས་ཅད་ནི་རྣམ་པ་དུ་མ་ཅན་ ༼སྣར། པེ།༽ ཐམས་ཅད་
[^8]: སྐྱེད་པའི་ ༼སྣར། པེ།༽ བསྐྱེད་པའི་
[^9]: རྒྱུ་ ༼སྣར། པེ།༽ རྒྱུའི་དངོས་པོ་
[^10]: སྲ་ ༼སྣར། པེ།༽ སྲ་བ་
[^11]: ཉིད་ཀྱང་དེ་དང་ ༼སྣར། པེ།༽ ཉིད་ཀྱང་
[^12]: ནི་ ༼སྣར། པེ།༽ ན་
[^13]: ཉིད་དོ། ༼སྣར། པེ།༽ ཉིད་དེ།
[^14]: འདོར་བར་བྱེད་ ༼སྣར། པེ།༽ འདོར་བ་མེད་
[^15]: གང་ཡིན་དེ། ༼སྣར།༽ གང་ཡིན་ཏེ།
[^16]: ལ་ནི་རག་ལ། ༼སྣར། པེ།༽ ལ་རེག་ན་
[^17]: སྐྱེ་བའི་ ༼སྣར། པེ།༽ སྐྱེས་པའི་
[^18]: གཏན་ཚིགས་ཡོད་པ་དང་མེད་པ་ ༼སྣར། པེ།༽ གཏན་ཚིགས་
[^19]: ན་ ༼སྣར། པེ།༽ ནི་
[^20]: རྒྱུ་ ༼སྣར། པེ།༽ རྒྱུ་དང་རྒྱུ་འབྲས་
[^21]: སྣང་བས་ ༼སྣར། པེ།༽ སྣང་བ་
[^22]: བྱེད་པར་ ༼སྣར། པེ།༽ བྱེད་པའི་
[^23]: འོ་ན་ནི་ ༼སྣར། པེ།༽ འོ་ན་
[^24]: བརྟེན་ན་ ༼སྣར། པེ།༽ བརྟེན་ནས་
[^25]: ནུས་པ་ཡི། ༼སྣར། པེ།༽ ནུས་པ་ཡིས།
[^26]: འབྲས་བུ་སྐྱེད་པ་ ༼སྣར། པེ།༽ འབྲས་བུ་བསྐྱེད་
[^27]: བརྟེན་ ༼སྣར། པེ།༽ རྟེན་
[^28]: བསྟན་པ་ ༼སྣར། པེ།༽ ཕྱེ་བ་
[^29]: དུས་ཅན་ ༼སྣར། པེ།༽ དུས་མ་
[^30]: རེས་འགའ་ ༼སྣར། པེ།༽ རེ་འགའ་
[^31]: ཤེས་པས་ ༼སྣར། པེ།༽ ཤེས་པའི་
[^32]: ཉིད་ ༼སྣར། པེ།༽ ཉིད་དུ་
[^33]: ལས་ ༼སྣར། པེ།༽ དང་
[^34]: དུ་མཐོང་ངོ་། ༼སྣར། པེ།༽ ཉིད་དུ་འཐད་དོ།
[^35]: བརྟགས་ ༼སྣར། པེ།༽ བརྟག་
[^36]: མཛད་པའོ། ༼སྣར། པེ།༽ མཛད་པ་རྫོགས་སོ།
--- END BLOCKS ---
